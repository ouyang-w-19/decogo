"""Implements projection master problems"""

import logging

from pyomo.core import ConstraintList, Param, RangeSet, Objective, \
    Var, Reals
from pyomo.environ import SolverFactory, SolverStatus

from decogo.pyomo_minlp_model.master_problem_base import MasterProblemBase
from decogo.pyomo_minlp_model.nlp_master_problem import NlpProblem
from decogo.util.block_vector import BlockVector

logger = logging.getLogger('decogo')


class NlpResourceProjectionProblem(NlpProblem):
    """Class for defining NLP projection master problem (integer variables
    are relaxed or fixed)

    .. math::
        \\begin{equation}
        \\begin{split}
            \\min \\ &\\sum\\limits_{k \\in K} ||A_kx_k - w_k||_2,\\newline
            &x \\in P \\cap G, \\newline
            &w_k \\in \\mathbb{R}^{m + 1} \\text{ and is fixed}
        \\end{split}
        \\end{equation}
    """

    def __init__(self, sub_models, cuts):
        """Constructor method"""
        super().__init__(sub_models, cuts)
        self.model.name = 'QP NLP problem'

        for k in range(self.cuts.num_blocks):
            self.model.blocks[k + 1].w = Param(
                RangeSet(self.cuts.num_of_global_cuts + 1),
                initialize=0,
                mutable=True)

        self.set_objective()

    def set_objective(self):
        """Sets objective function"""

        expr = 0
        for k in range(self.cuts.num_blocks):
            for j in range(self.cuts.num_of_global_cuts + 1):
                if j == 0:
                    expr += \
                        (sum(self.cuts.obj.c[k, i] *
                             self.model.blocks[k + 1].Y[i + 1]
                             for i in range(self.cuts.block_sizes[k])) -
                         self.model.blocks[k + 1].w[j + 1]) ** 2
                else:
                    expr += (sum(
                        self.cuts.global_cuts[j - 1].lhs[k, i] *
                        self.model.blocks[k + 1].Y[i + 1]
                        for i in range(self.cuts.block_sizes[k])) -
                             self.model.blocks[k + 1].w[j + 1]) ** 2

        self.model.del_component('obj')
        self.model.obj = Objective(expr=expr)

    def set_projection_point(self, point_to_project):
        """Sets value for parameter :math:`w_k` (projection point).

        :param point_to_project: Given value for :math:`w`
        :type point_to_project: BlockVector
        """
        for k in range(self.cuts.num_blocks):
            for j in range(self.cuts.num_of_global_cuts + 1):
                self.model.blocks[k + 1].w[j + 1].value = point_to_project[k, j]

    def solve(self, solver_name, start_point=None, solver_options=None):
        """Solves the model by calling an external solver and gets back the
        result

        :param solver_name: External solver name
        :type solver_name: str
        :param start_point: Starting point for the solver, defaults to ``None``
        :type start_point: BlockVector or None
        :param solver_options: External solver options, defaults to ``None``
        :type solver_options: list or None
        :return: Solution point, objective value, dual solution and flag \
        indicating whether the solution is feasible
        :rtype: tuple
        """
        if start_point is not None:
            for k in range(len(self.model.blocks)):
                for n in range(len(self.model.blocks[k + 1].Y)):
                    self.model.blocks[k + 1].Y[n + 1].value = start_point[k, n]

        opt = SolverFactory(solver_name)

        def recursive_solve(opt_recursive, options=None, iter_i=10):
            solver_error = False
            try:
                if options is not None:
                    for key, value in options:
                        opt_recursive.options[key] = value
                result_recursive = opt_recursive.solve(self.model, tee=False)
            except ValueError as error:
                logger.info(error)
                if iter_i - 2 < 2:
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

        result, error_in_solver = recursive_solve(opt, solver_options)

        sol_is_feasible = True
        if error_in_solver:
            sol_is_feasible = False
        else:
            if result.solver.status == SolverStatus.warning:
                sol_is_feasible = False
                logger.info('Master problem is {0}: {1}'.format(
                    result.solver.termination_condition,
                    self.model.name))

        if sol_is_feasible:
            # get duals
            try:
                duals = [0] * self.cuts.num_of_global_cuts
                for i in self.model.lin_con:
                    duals[i - 1] = self.model.dual[self.model.lin_con[i]]
            except KeyError:
                duals = None

            # get solution point
            x_sol = BlockVector(self.cuts.block_sizes)
            for k in range(len(self.model.blocks)):
                for n in range(len(self.model.blocks[k + 1].Y)):
                    x_sol[k, n] = self.model.blocks[k + 1].Y[n + 1].value

            obj_val = self.model.obj.expr()

        else:  # infeasible
            duals = None
            x_sol = None
            obj_val = None

        return x_sol, obj_val, duals, sol_is_feasible


class MipProjectionMasterProblem(MasterProblemBase):
    """Class for defining MIP projection master problem defined using
    infinity norm

    .. math::
        \\begin{equation}
        \\begin{split}
            \\min \\ &||x - y||_\\infty,\\newline
            &x \\in P \\cap Y , y \\text{ is fixed}
        \\end{split}
        \\end{equation}

    The problem is reformulated in the following way

    .. math::
        \\begin{equation}
        \\begin{split}
            \\min \\ &t, \\newline
            &-t \\leq x - y \\leq t, \\newline
            &x \\in P \\cap Y , y \\text{ is fixed}
        \\end{split}
        \\end{equation}
    """

    def __init__(self, sub_models, cuts):
        super().__init__(sub_models, cuts)

        for k in range(self.cuts.num_blocks):
            self.model.blocks[k + 1].point_to_project = \
                Param(RangeSet(self.cuts.block_sizes[k]),
                      mutable=True,
                      initialize=0)

        self.set_objective()

    def set_objective(self):
        """Sets objective function"""
        self.model.t = Var(domain=Reals, initialize=0)

        expr = self.model.t

        self.model.del_component('obj')
        self.model.obj = Objective(expr=expr)

        # norm constraints -t <= x - y <= t
        self.model.norm_constraints = ConstraintList()
        for k in range(self.cuts.num_blocks):
            for i in range(self.cuts.block_sizes[k]):
                self.model.norm_constraints.add(
                    self.model.blocks[k + 1].Y[i + 1] -
                    self.model.blocks[k + 1].point_to_project[i + 1] <=
                    self.model.t)
                self.model.norm_constraints.add(
                    -(self.model.blocks[k + 1].Y[i + 1] -
                      self.model.blocks[k + 1].point_to_project[i + 1]) <=
                    self.model.t)

    def set_projection_point(self, point):
        """Sets projection point ``y``

        :param point: Given point
        :type point: BlockVector
        """
        for k in range(self.cuts.num_blocks):
            for i in range(self.cuts.block_sizes[k]):
                self.model.blocks[k + 1].point_to_project[i + 1].value = \
                    point[k, i]

    def solve(self, solver_name, start_point=None, solver_options=None,
              pool_solutions=10, agg_blocks=None):
        """todo"""
        if solver_name == 'gurobi_persistent':
            # special implementation for extracting solution pool,
            # which works only for gurobi
            if start_point is not None:
                for k in range(len(self.model.blocks)):
                    for n in range(len(self.model.blocks[k + 1].Y)):
                        self.model.blocks[k + 1].Y[n + 1].value = \
                            start_point[k, n]

            # explicitly remove the component for getting the duals,
            # since Gurobi complains
            # self.model.del_component('dual')

            opt = SolverFactory(solver_name)

            # set solver options
            # options are pairs: (parameter name, value)
            if solver_options is not None:
                for key, value in solver_options:
                    opt.options[key] = value

            # number of solutions to be stored
            opt.options['PoolSolutions'] = pool_solutions  # N
            # logger.info('PoolSolutions = {0}'.format(pool_solutions))

            # Strategy how to find feasible solutions:
            # 0 - no effort to find the N feasible solutions (sol. count <= N)
            # 1 - force to have N feasible solutions with random quality
            # 2 - force to have N best feasible solutions
            pool_search_mode = 1
            opt.options['PoolSearchMode'] = pool_search_mode
            # logger.info('PoolSearchMode = {0}'.format(pool_search_mode))

            opt.set_instance(self.model)
            result = opt.solve(tee=False)

            sol_is_feasible = True
            if result.solver.status == SolverStatus.warning:
                sol_is_feasible = False
                logger.info('Master problem is {0}: {1}'.format(
                    result.solver.termination_condition,
                    self.model.name))

            duals = None

            # retrieve solutions
            # stores list of solutions
            x_sol = []
            for i in range(opt.get_model_attr('SolCount')):
                opt.set_gurobi_param('SolutionNumber', i)  # move to the
                # next sol.

                current_sol = BlockVector(self.cuts.block_sizes)
                if agg_blocks is None:
                    for k in range(len(self.model.blocks)):
                        for n in range(len(self.model.blocks[k + 1].Y)):
                            pyomo_var = self.model.blocks[k + 1].Y[n + 1]
                            current_sol[k, n] = \
                                opt.get_var_attr(pyomo_var, 'Xn')
                else:
                    for k in agg_blocks:
                        for n in range(len(self.model.blocks[k + 1].Y)):
                            pyomo_var = self.model.blocks[k + 1].Y[n + 1]
                            current_sol[k, n] = \
                                opt.get_var_attr(pyomo_var, 'Xn')
                x_sol.append(current_sol)

            obj_val = self.model.obj.expr()

        else:
            x_sol, obj_val, duals, sol_is_feasible = \
                super().solve(solver_name, start_point, solver_options)

        return x_sol, obj_val, duals, sol_is_feasible
