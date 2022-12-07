"""Implements and manages all sub-problems"""

import logging
from abc import ABC

import numpy as np
from pyomo.core import ConcreteModel, Param, RangeSet, Var, ConstraintList, \
    Objective, minimize, maximize
from pyomo.core.expr.visitor import identify_variables, replace_expressions
from pyomo.environ import Binary, Integers, Reals, SolverStatus, \
    TerminationCondition
from pyomo.opt import SolverFactory

logger = logging.getLogger('decogo')


class PyomoSubProblemBase:
    """Base class for construction of Pyomo model. Here are implemented
    methods for creating local linear and nonlinear constraints

    :param block_model: Block model
    :type block_model: BlockModel
    :param block_id: Block identifier
    :type block_id: int
    :param model: Pyomo model
    :type model: ConcreteModel
    """

    def __init__(self, sub_models, cuts, block_id):
        """Constructor method"""
        self.block_id = block_id
        self.sub_model = sub_models[block_id]
        self.cuts = cuts

        self.model = ConcreteModel()

        self.model.Y = Var(RangeSet(cuts.block_sizes[block_id]))
        for n in range(1, self.sub_model.block_size + 1):
            lb = self.sub_model.variables[n - 1].lower_bound
            self.model.Y[n].value = lb

            self.model.Y[n].setlb(lb)

            ub = self.sub_model.variables[n - 1].upper_bound
            self.model.Y[n].setub(ub)

            if self.sub_model.variables[n - 1].type == "Binary":
                self.model.Y[n].domain = Binary
                self.model.Y[n].value = 0
            elif self.sub_model.variables[n - 1].type == "Integers":
                self.model.Y[n].domain = Integers
            else:
                self.model.Y[n].domain = Reals

        self.model.lin_con = ConstraintList()

        def lin_con_rule(model, k, m):
            return sum(cuts.local_cuts[k][m].lhs[self.block_id, n] *
                       model.Y[n + 1] for n in range(sub_models[k].block_size))

        for m, local_constr in enumerate(cuts.local_cuts[block_id]):
            if local_constr.relation == "<=":
                self.model.lin_con.add(expr=lin_con_rule(self.model, block_id,
                                                         m) <= local_constr.rhs)
            elif local_constr.relation == "=":
                self.model.lin_con.add(expr=lin_con_rule(self.model, block_id,
                                                         m) == local_constr.rhs)
            elif local_constr.relation == ">=":
                self.model.lin_con.add(expr=lin_con_rule(self.model, block_id,
                                                         m) >= local_constr.rhs)

        self.model.nonlin_constr = ConstraintList()
        for constr in self.sub_model.nonlin_constr:
            expr = constr.expr.clone()
            vars_in_expr = identify_variables(expr)
            substitution_map = {}  # map for replacing the objects in
            # the expression
            for var in vars_in_expr:
                index = self.sub_model.vars_in_block.index(
                    var.name)
                substitution_map[id(var)] = self.model.Y[index + 1]
            new_expr = replace_expressions(expr, substitution_map)
            self.model.nonlin_constr.add(expr=new_expr)

    def solve(self, solver_name, start_point=None, solver_options=None):
        """Base method for calling the external solver to solve the model

        :param solver_name: External solver name
        :type solver_name: str
        :param start_point: Starting point for the solver, defaults to ``None``
        :type start_point: ndaray or None
        :param solver_options: Options for external solver, defaults to ``None``
        :type solver_options: list
        :return: Solution point, primal bound, dual bound, flag if the primal \
        bound is feasible
        :rtype: tuple
        """

        if start_point is not None:
            for i in range(len(self.model.Y)):
                self.model.Y[i + 1].value = start_point[i]

        # solving the problem
        opt = SolverFactory(solver_name)

        # # set solver options
        # # options are pairs: (parameter name, value)
        # if solver_options is not None:
        #     for key, value in solver_options:
        #         opt.options[key] = value
        #
        # results = opt.solve(self.model, tee=False)

        def recursive_solve(opt_recursive, options=None, iter_i=10):
            solver_error = False
            try:
                if options is not None:
                    for key, value in solver_options:
                        opt_recursive.options[key] = value
                result_recursive = opt_recursive.solve(self.model, tee=False)
            except ValueError as error:
                logger.info(error)
                if iter_i - 2 < 6:
                    logger.info('error: cannot solve')
                    solver_error = True
                    result_recursive = None
                else:
                    logger.info('solve: max_iter = {0}'.format(iter_i - 2))
                    result_recursive, solver_error = \
                        recursive_solve(opt_recursive, options=('max_iter',
                                                                iter_i - 2),
                                        iter_i=iter_i - 2)
            return result_recursive, solver_error

        results, error_in_solver = recursive_solve(opt, solver_options)

        sol_is_feasible = True
        dual_bound = None
        primal_bound = None
        y_new = np.zeros(shape=len(self.model.Y))
        if error_in_solver:
            sol_is_feasible = False
        else:
            if results.solver.status == SolverStatus.ok:
                sol_is_feasible = True
            elif results.solver.status == SolverStatus.warning:
                if results.solver.termination_condition == \
                        TerminationCondition.infeasible:
                    sol_is_feasible = False
                    logger.info(self.model.name + ' is infeasible')
                elif results.solver.termination_condition == \
                        TerminationCondition.maxIterations:
                    sol_is_feasible = False

            for i in range(len(self.model.Y)):
                y_new[i] = self.model.Y[i + 1].value

            primal_bound = self.model.obj.expr()

            # by default dual bound is equal to primal bound
            dual_bound = primal_bound
            if solver_name == 'scip' and solver_options is not None:
                log_lines = opt._log.split('\n')
                for line in log_lines:
                    if line.startswith('Dual Bound'):
                        dual_bound = float(line.split(':')[1].strip())

        return y_new, primal_bound, dual_bound, sol_is_feasible

    def add_linear_constraint(self):
        """Adds new linear constraint"""

        def lin_con_rule(model, constr):
            return sum(constr.lhs[self.block_id, n] * model.Y[n + 1]
                       for n in
                       range(self.cuts.block_sizes[self.block_id]))

        constr = self.cuts.local_cuts[self.block_id][
            -1]  # this takes the last one
        if constr.relation == "<=":
            self.model.lin_con.add(
                expr=lin_con_rule(self.model, constr) <= constr.rhs)
        elif constr.relation == "=":
            self.model.lin_con.add(
                expr=lin_con_rule(self.model, constr) == constr.rhs)
        elif constr.relation == ">=":
            self.model.lin_con.add(
                expr=lin_con_rule(self.model, constr) >= constr.rhs)

    def set_nlp(self):
        """Relaxes integer varaibles to continious"""
        for i, var_domain in enumerate(
                self.sub_model.variables):
            if var_domain.type == "Integers":
                self.model.Y[i + 1].domain = Reals
            elif var_domain.type == "Binary":
                self.model.Y[i + 1].domain = Reals

    def unset_nlp(self):
        """Sets to integer type for the variables which are integer in the
        original formulation"""
        for i, var_domain in enumerate(
                self.sub_model.variables):
            if var_domain.type == "Integers":
                self.model.Y[i + 1].domain = Integers
            elif var_domain.type == "Binary":
                self.model.Y[i + 1].domain = Binary

    def update_var_lower_bound(self, index):
        """Updates the lower bound of the variable. The value is taken form
        the BlockModel

        :param index: Index (block_id, index)
        :type index: tuple
        """
        k, i = index
        self.model.Y[i + 1].setlb(
            self.sub_models[k].variables[i].lower_bound)

    def update_var_upper_bound(self, index):
        """Updates the upper bound of the variable. The value is taken form
        the BlockModel

        :param index: Index (block_id, index)
        :type index: tuple
        """
        k, i = index
        self.model.Y[i + 1].setub(
            self.sub_models[k].variables[i].upper_bound)

    def fix_integers(self, x):
        """Fixes integer variables with given value

        :param x: Given array
        :type x: ndarray
        """
        for i, var in enumerate(
                self.sub_model.variables):
            if var.type == 'Integer' or var.type == 'Binary':
                self.model.Y[i + 1].value = x[i]
                self.model.Y[i + 1].fix()

    def unfix_integers(self):
        """Unfixes all integer variables"""
        for i, var in enumerate(
                self.sub_model.variables):
            if var.type == 'Integers' or var.type == 'Binary':
                self.model.Y[i + 1].unfix()

    def add_objective(self):
        """Sets default objective function, i.e. :math:`c_k^Tx_k`, where
        :math:`c_k` - partial objective from the original model
        """

        def objective_rule(model):
            ans_obj = 0

            ans_obj += sum(
                self.cuts.obj.c[self.block_id, n] * model.Y[n + 1]
                for n in range(self.cuts.block_sizes[self.block_id]))

            ans_obj += self.cuts.obj.const

            return ans_obj

        self.model.del_component('obj')
        self.model.obj = Objective(rule=objective_rule, sense=minimize)

    def set_objective(self, direction):
        """Sets the objective function with given direction vector

        :param direction: Given vector
        :type direction: ndarray
        """

        new_obj_expr = sum(direction[n] * self.model.Y[n + 1]
                           for n in range(
            self.sub_model.block_size))

        self.model.del_component('obj')

        self.model.obj = Objective(expr=new_obj_expr)


class PyomoMinlpSubProblem(PyomoSubProblemBase):
    """Class for defining the following sub-problem

    .. math::
        \\begin{equation}
        \\begin{split}
            \\min \\ &d_k^Ty_k, \\newline
            &y_k \\in X_k, d_k \\in \\mathbb{R}^{n_k}
        \\end{split}
        \\end{equation}
    """

    def __init__(self, sub_models, cuts, block_id):
        """Constructor method"""
        super().__init__(sub_models, cuts, block_id)


class PyomoProjectionSubProblem(PyomoSubProblemBase):
    """Class for defining a projection sub-problem

    .. math::
        \\begin{equation}
        \\begin{split}
            \\min \\ &||y_k-x_k||^2,\\newline
            &y_k \\in G_k, x_k \\text{ is fixed}
        \\end{split}
        \\end{equation}
    """

    def __init__(self, sub_models, cuts, block_id):
        """Constructor method"""
        super().__init__(sub_models, cuts, block_id)

        self.model.X = Param(RangeSet(self.cuts.block_sizes[block_id]),
                             mutable=True, initialize=0)

        self.model.obj = Objective(expr=self.obj_rule())
        self.model.name = 'Projection sub problem'

    def obj_rule(self):
        """Defines the objective function

        :return: Objective expression
        :rtype: Expression
        """
        expr = sum(pow((self.model.Y[n + 1] - self.model.X[n + 1]), 2)
                   for n in
                   range(self.sub_model.block_size))

        return expr

    def set_projection_point(self, point_to_project):
        """Sets projection point, i.e. :math:`x_k`

        :param point_to_project: Projection point
        :type point_to_project: ndarray
        """
        for i in range(len(self.model.X)):
            self.model.X[i + 1].value = point_to_project[i]


class PyomoResourceProjectionSubProblem(PyomoSubProblemBase):
    """Class for defining a projection sub-problem

    .. math::
        \\begin{equation}
        \\begin{split}
            \\min \\ &||A_kx_k - w_k||^2,\\newline
            &y_k \\in G_k, w_k \\text{ is fixed}
        \\end{split}
        \\end{equation}
    """

    def __init__(self, sub_models, cuts, block_id):
        """Constructor method"""
        super().__init__(sub_models, cuts, block_id)

        self.model.w = Param(RangeSet(self.cuts.num_of_global_cuts + 1),
                             mutable=True, initialize=0)

        self.model.obj = Objective(expr=self.obj_rule())
        self.model.name = 'Resource projection sub problem'

    def obj_rule(self):
        """Defines the objective function

        :return: Objective expression
        :rtype: Expression
        """
        expr = 0
        for j in range(self.cuts.num_of_global_cuts + 1):
            if j == 0:
                expr += \
                    (sum(self.cuts.obj.c[self.block_id, i] * self.model.Y[i + 1]
                         for i in range(self.cuts.block_sizes[self.block_id])) -
                     self.model.w[j + 1]) ** 2
            else:
                expr += \
                    (sum(self.cuts.global_cuts[j - 1].lhs[self.block_id, i] *
                         self.model.Y[i + 1]
                    for i in range(self.cuts.block_sizes[self.block_id])) -
                         self.model.w[j + 1]) ** 2

        return expr

    def set_projection_point(self, point_to_project):
        """Sets projection point, i.e. :math:`w_k`

        :param point_to_project: Projection point
        :type point_to_project: ndarray
        """
        for i in range(len(self.model.w)):
            self.model.w[i + 1].value = point_to_project[i]


class PyomoLineSearchSubProblem(PyomoSubProblemBase):
    """Class defines line search sub-problem between exterior point
    :math:`x_k^{ext}` and interior point :math:`x_k^{int}`

    .. math::
        \\begin{equation}
        \\begin{split}
            \\max \\ & \\alpha, \\newline
            &y_k = \\alpha x_k^{ext} + (1 - \\alpha) x_k^{int}, \\newline
            &y_k \\in X_k
        \\end{split}
        \\end{equation}
    """

    def __init__(self, sub_models, cuts, block_id):
        super().__init__(sub_models, cuts, block_id)

        self.model.lin_con.deactivate()

        # variable for finding the point on the line between x_hat and x_star
        self.model.alpha = Var(bounds=(0, 1), initialize=0, within=Reals)

        # objective
        self.model.obj = Objective(expr=self.model.alpha, sense=maximize)

        self.model.interior_point = Param(
            RangeSet(self.cuts.block_sizes[block_id]), mutable=True,
            initialize=0)
        self.model.exterior_point = Param(
            RangeSet(self.cuts.block_sizes[block_id]), mutable=True,
            initialize=0)

        self.model.line_search_con = ConstraintList()
        for i in range(self.cuts.block_sizes[self.block_id]):
            self.model.line_search_con.add(
                self.model.Y[i + 1] == self.model.alpha *
                self.model.exterior_point[i + 1] +
                (1 - self.model.alpha) * self.model.interior_point[i + 1])

    def set_interior_exterior_points(self, exterior_point, interior_point):
        """Sets values of two endpoints

        :param exterior_point: Exterior point
        :type exterior_point: ndarray
        :param interior_point: Interior point
        :type interior_point: ndarray
        """
        for i in range(self.cuts.block_sizes[self.block_id]):
            self.model.exterior_point[i + 1].value = exterior_point[i]
            self.model.interior_point[i + 1].value = interior_point[i]

    def solve(self, solver_name, start_point=None, solver_options=None):
        """Solves the subproblem and gets value of :math:`\\alpha`. For more
        info, see base method :meth:`SubProblemBase.solve`
        """
        y_new, primal_bound, dual_bound, sol_is_feasible = \
            super().solve(solver_name, start_point=start_point,
                          solver_options=solver_options)

        alpha = self.model.alpha.value

        return alpha, y_new

