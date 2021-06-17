"""Implements colgen for pyomo minlp input model """

from pyomo.core.base import Expression
from pyomo.core.expr.visitor import identify_variables
from pyomo.environ import ConcreteModel, Objective, Set, Param, Block
from pyomo.network import Port, Arc
from pyomo.core.base.constraint import IndexedConstraint, \
    Constraint, ScalarConstraint
from pyomo.core.base.var import _GeneralVarData, Var, ScalarVar
from pyomo.core.expr.numeric_expr import NegationExpression, \
    MonomialTermExpression, ProductExpression, SumExpression, \
    LinearExpression

from decogo.util.block_vector import BlockVector

from decogo.model.constraints import LinearConstraint, ObjectiveFunction, \
    VarDomain, NonLinearConstraint
from decogo.model.model_decomposer import PyomoModelDecomposer
from decogo.model.input_model_base import InputModelBase, OriginalProblemBase, \
    CutPoolCG, SubProblemsBase, SubModelBase

from decogo.pyomo_minlp_model.subproblem import PyomoMinlpSubProblem, \
    PyomoLineSearchSubProblem, PyomoProjectionSubProblem, \
    PyomoResourceProjectionSubProblem
from decogo.pyomo_minlp_model.nlp_master_problem import NlpProblem
from decogo.pyomo_minlp_model.projection_master_problem import \
    NlpResourceProjectionProblem, \
    MipProjectionMasterProblem

from decogo.solver.settings import Settings

import logging
import copy
logger = logging.getLogger('decogo')


class PyomoInputModel(InputModelBase):
    """User-defined input model for pyomo MINLP problems

    :param model: Input Pyomo model
    :type model: ConcreteModel
    :param blocks: List (blockwise) of original string names of variables
    :type blocks: list
    :param block_sizes: List of variable numbers per sub-model
    :type block_sizes: list
    :param sense: Indicates the the problem is minimization (1) or  \
    maximization (-1)
    :type sense: int
    :param sub_problems: list of SubProblems blockwise
    :type sub_problems: list
    :param original_problem: container of original problem
    :type original_problem: PyomoOriginalProblem
    :param cuts: container of linear constraints
    :type cuts: CutPoolCG
    :param sub_models: list of containers for variables from a single \
    block and local nonlinear constraints blockwise
    :type sub_models: list
    """

    def __init__(self, model):
        # region preprocessing of pyomo model
        self.settings = Settings()
        self._remove_unpicklable_objects_pyomo_model(model)
        self.decomposer = PyomoModelDecomposer(model, self.settings)
        model, blocks, model_sense = self.decomposer.decompose()
        self.blocks = blocks  # string names for the variables in the block
        num_blocks = len(blocks)
        self.block_sizes = [len(item) for item in blocks]
        self.sense = model_sense
        self.model = model
        # endregion

        # region construct cuts
        block_sizes, blocks, obj, global_cuts, local_cuts \
            = self._construct_cut_pool()
        cuts = CutPoolCG(block_sizes, blocks, obj, global_cuts, local_cuts)
        # endregion

        # region construct sub_problems, original_problem
        sub_models = [PyomoSubModel(self.model,
                                    self.blocks[block_id], block_id)
                      for block_id in range(num_blocks)]
        sub_problems = [PyomoSubProblems(sub_models, cuts, block_id,
                                         self.settings)
                        for block_id in range(num_blocks)]

        original_problem = PyomoOriginalProblem(sub_models,
                                                cuts, self.settings)
        # endregion

        super().__init__(sub_problems, original_problem, cuts, sub_models)

    def _construct_cut_pool(self):
        block_sizes = [len(item) for item in self.blocks]
        blocks = self.blocks

        # region objective reading and initialization
        obj_name, objective = \
            next(self.model.component_map(Objective).items())
        obj_expr = objective.expr
        degree = obj_expr.polynomial_degree()
        if degree is None or degree > 1:
            raise ValueError(
                'Dev: Objective is not linear, check the reformulation')
        coef, obj_const = self._get_linear_term_data(obj_expr)
        obj = ObjectiveFunction(coef, block_sizes, obj_const)
        # endregion

        # region linear constraints reading and initialization
        global_cuts = []
        local_cuts = {}
        for k in range(len(block_sizes)):
            local_cuts[k] = []

        for block_obj in self.model.block_data_objects():
            for con_name, con_obj in \
                    block_obj.component_map(Constraint,
                                            active=True).items():
                if con_obj.__class__ is ScalarConstraint:
                    self._read_constraint_object(con_obj, local_cuts,
                                                 global_cuts)
                elif con_obj.__class__ is IndexedConstraint:
                    for index in con_obj:
                        self._read_constraint_object(con_obj[index], local_cuts,
                                                     global_cuts)
        # endregion

        return block_sizes, blocks, obj, global_cuts, local_cuts

    def _read_constraint_object(self, con_obj, local_cuts, global_cuts):
        """Reads Pyomo constraints, detects if the constraint is linear.
        If yes, then it creates the linear constraint

        :param con_obj: Pyomo constraint object
        :type con_obj: Constraint
        """
        con_expr = con_obj.body
        if con_expr.polynomial_degree() == 1:
            coef, const = self._get_linear_term_data(con_expr)

            rhs = None
            relation = None
            if con_obj.equality is True:
                relation = "="
                rhs = con_obj.upper.value
            elif con_obj.upper is not None and con_obj.strict_upper is False:
                relation = "<="
                rhs = con_obj.upper.value
            elif con_obj.upper is not None and con_obj.strict_upper:
                relation = "<"
                rhs = con_obj.upper.value
            elif con_obj.lower is not None and con_obj.strict_lower is False:
                relation = ">="
                rhs = con_obj.lower.value
            elif con_obj.lower is not None and con_obj.strict_lower:
                relation = ">"
                rhs = con_obj.lower.value

            rhs -= const
            lin_con = LinearConstraint(coef, relation, rhs, self.block_sizes)

            if lin_con.is_local is True:
                local_cuts[lin_con.block_id].append(lin_con)
            else:
                global_cuts.append(lin_con)

    def _get_linear_term_data(self, expr):
        """Recursive function for reading and getting data for linear terms

        :param expr: Linear expression to parse
        :type expr: Expression
        :return: List of coefficients and constant
        :rtype: (list, int)
        """
        coef = []
        const = 0
        if expr.__class__ is SumExpression:
            for term in expr.args:
                new_coef, new_const = self._get_linear_term_data(term)
                for block_id, idx, val in new_coef:
                    coef.append((block_id, idx, val))
                const += new_const
        elif expr.__class__ is MonomialTermExpression:
            if isinstance(expr.args[0], (int, float)):
                coef_val = expr.args[0]
                var_name = expr.args[1].name
            else:
                var_name = expr.args[0].name
                coef_val = expr.args[1]
            k, i = self._get_variable_index_by_name(var_name)
            coef.append((k, i, coef_val))
        elif expr.__class__ is NegationExpression:
            new_coef, new_const = self._get_linear_term_data(expr.args[0])
            # multiply by -1, since it is negation expression
            for block_id, idx, val in new_coef:
                coef.append((block_id, idx, -val))
            const -= new_const
        elif expr.__class__ is ProductExpression:
            # if ProductExpression is here, than it is should be that one
            # argument is a number and the other is SumExpression
            if isinstance(expr.args[0], (int, float)):
                new_coef, new_const = self._get_linear_term_data(expr.args[1])
                multiplier = expr.args[0]
            else:
                new_coef, new_const = self._get_linear_term_data(expr.args[0])
                multiplier = expr.args[1]

            for block_id, idx, val in new_coef:
                coef.append((block_id, idx, multiplier * val))
            const += multiplier * new_const
        elif expr.__class__ is LinearExpression:
            for index, val in enumerate(expr.linear_coefs):
                var_name = expr.linear_vars[index].name
                k, i = self._get_variable_index_by_name(var_name)
                coef.append((k, i, val))
        elif expr.__class__ is Var or expr.__class__ is _GeneralVarData or \
                expr.__class__ is ScalarVar:
            k, i = self._get_variable_index_by_name(expr.name)
            coef.append((k, i, 1))
        elif isinstance(expr, (int, float)):
            const = expr
        else:
            raise ValueError(
                'Dev: Found expression object type which was not considered')
        return coef, const

    def _get_variable_index_by_name(self, var_name):
        """Get variable index from the list of blocks for sparse vector
        initialization

        :param var_name: Original variable name
        :type var_name: str
        :return: Pair of indices: block id and index in the block
        :rtype: (int, int)
        """
        j = 0  # index for iteration over the blocks
        while True:
            try:
                i = self.blocks[j].index(var_name)
                k = j
                break
            except ValueError:
                j += 1
        return k, i

    @staticmethod
    def _remove_unpicklable_objects_pyomo_model(model):
        """ Removes unpicklable objects from Pyomo model object. This is because
        multiprocessing is based on serialization and some objects cannot be
        serialized (pickled).
        This method does the following:

        * removes objects Port and Arcs, since they contain weakref objects

        * sets to None the 'rule' property for Constraint, Objective and Param, \
        since it might contain lambda function

        * sets to None property 'initialize' and '_init_values._init' for Set, \
        since it might contain lambda function

        :param model: Pyomo model
        :type model: ConcreteModel
        """
        for block_obj in model.block_data_objects():
            for port in block_obj.component_objects(Port):
                block_obj.del_component(port)
            for arc in block_obj.component_objects(Arc):
                block_obj.del_component(arc)

        for obj in model.component_objects(
                [Objective, Constraint, Param, Block]):
            obj._rule = None
            obj.rule = None

        # if here some exceptions occur, then check whether attributes still
        # exist
        for obj in model.component_objects([Set]):
            obj._init_values._init = None
            obj.initialize = None


class PyomoOriginalProblem(OriginalProblemBase):
    """User-defined local solve for pyomo MINLP problems

    :param cuts: Container which stores all linear constraints \
    (global and local) and objective function
    :type cuts: CutPoolCG
    :param sub_models: List of sub-models
    :type sub_models: list
    :param nlp_problem: NLP master problem
    :type nlp_problem: NlpProblem
    :param mip_projection_master_problem: MIP projection master problem
    :type mip_projection_problem: MipProjectionMasterProblem
    :param nlp_resource_projection_problem: NLP projection master problem
    :type nlp_resource_projection_problem: NlpResourceProjectionProblem
    """
    def __init__(self, sub_models, cuts, settings):
        """Constructor method"""
        super().__init__()
        self.settings = settings
        # NLP master problems
        self.nlp_problem = NlpProblem(sub_models, cuts)

        # projection problems
        self.mip_projection_problem = \
            MipProjectionMasterProblem(sub_models, cuts)
        self.nlp_resource_projection_problem = \
            NlpResourceProjectionProblem(sub_models, cuts)

    def local_solve_fast(self, start_point, result, problem, iter=None):

        # solve NLP resource projection problem
        tilde_y, obj_val_nlp_1st, sol_is_feasible = \
            self.solve_nlp_resource_proj_problem(self.settings.nlp_solver,
                                                 point_to_project=start_point)

        if sol_is_feasible:
            logger.info('-------------------------------------')
            # tilde_y: NLP project point
            c_tilde_y = self.nlp_problem.cuts.obj.eval(tilde_y)
            logger.info('solve_nlp_resource_proj obj: {0} '
                        .format(result.sense * round(c_tilde_y, 4)))
            logger.info('-------------------------------------')
        else:
            logger.info('-------------------------------------')
            logger.info('solve_nlp_resource_proj not feasible')
            c_tilde_y = 0
            logger.info('-------------------------------------')

        c_tilde_x = 0
        if sol_is_feasible:
            # solve MIP project problem
            hat_x, _, sol_is_feasible = \
                self.solve_mip_proj_problem(self.settings.mip_solver,
                                            point_to_project=tilde_y)

            if sol_is_feasible:
                # NLP problem with fixed integers
                tilde_x, obj_val, sol_is_feasible = \
                    self.nlp_solve(self.settings.nlp_solver,
                                   point_to_fix=hat_x,
                                   start_point=hat_x)
            else:
                logger.info('-------------------------------------')
                logger.info('solve_mip_projct_problem not feasible')
                logger.info('-------------------------------------')

            # testing findSol
            if sol_is_feasible:
                logger.info('-------------------------------------')
                # tilde_x: fixed NLP solution
                c_tilde_x = obj_val
                logger.info('solve_fixed_nlp_problem obj: {0} '
                            .format(result.sense * round(c_tilde_x, 4)))
                logger.info('-------------------------------------')
            else:
                logger.info('-------------------------------------')
                logger.info('solve_fixed_nlp_problem not feasible')
                logger.info('-------------------------------------')

        if sol_is_feasible is True:
            logger.info('{0: <50}{1: <30}'
                        .format('Gap (c_tilde_y '
                                'and c_tilde_x):',
                                result.get_gap(c_tilde_x, c_tilde_y)))

            result.set_new_primal_bound(obj_val, tilde_x)

            for k in range(self.nlp_problem.cuts.num_blocks):
                problem.add_inner_point(
                    k, tilde_x.get_block(k),
                    self.settings.cg_min_inner_point_distance)

            logger.info('\nAfter solving fixed NLP projection problem, '
                        'the solution point is feasible')

            if iter is None:  # this is for printing number of iteration
                # in the logger when generating feasible candidate
                logger.info('{0: <50}{1: <30}'
                            .format('Projection Gap (c(x_NLP_proj) '
                                    'and primal bound):',
                                    result.get_gap(
                                        result.primal_bound, c_tilde_y)))
                logger.info('\nFeasible candidate obtained in this '
                            'iteration: {0}'
                            .format(result.sense * obj_val))
            else:
                logger.info('{0: <50}{1: <30}'
                            .format('Projection Gap (c(x_NLP_proj) '
                                    'and primal bound):',
                                    result.get_gap(
                                        result.primal_bound, c_tilde_y)))
                logger.info('\nFeasible candidate obtained in '
                            'iter {0}: {1}'
                            .format(int(iter),
                                    result.sense * obj_val))

        else:
            if iter is None:  # this is for printing number of
                # iteration in the logger when generating feasible candidate
                logger.info('\nNo feasible candidate obtained in this '
                            'iteration')
            else:
                logger.info('\nNo feasible candidate obtained in iter {0}'
                            .format(int(iter)))
        logger.info('\n=======================================================')

    def local_solve(self, start_point, result, problem, iter=None):
        mip_solver = 'gurobi_persistent'
        pool_solutions = self.settings.cg_find_sol_mip_pool

        old_feasible_obj_val = float('inf')
        tau = self.settings.cg_find_sol_mip_pool_tau
        ii = 1
        logger.info('\n---------------------------------------------------')
        logger.info('Local search iter {0}'.format(ii))
        while True:

            hat_x_list, _, sol_is_feasible = \
                self.solve_mip_proj_problem(solver_name=mip_solver,
                                            point_to_project=start_point,
                                            pool_solutions=pool_solutions)

            if sol_is_feasible is False:
                logger.info('mip proj problem is infeasible')
                break

            i_max = len(hat_x_list)
            hat_x = hat_x_list[0]
            logger.info('Solution pool generated from '
                        'solving MIP project problem: {0}'.format(i_max))
            logger.info('Solution pool: solution 1')

            i = 0
            feasible_obj_val = float('inf')
            feasible_obj_point = None

            while True:
                i += 1
                c_hat_x = problem.block_model.cuts.obj.eval(hat_x)
                logger.info('---------------MIP-projection--------------------')
                logger.info('c_hat_x: {0}'.format(c_hat_x))
                logger.info('-------------------------------------------------')

                try:
                    # NLP problem with fixed integers
                    tilde_x, obj_val, sol_is_feasible = \
                        self.nlp_solve(self.settings.nlp_solver,
                                       point_to_fix=hat_x,
                                       start_point=hat_x)
                except ValueError:
                    sol_is_feasible = False

                if sol_is_feasible is True:
                    improved = result.set_new_primal_bound(obj_val, tilde_x)

                    if obj_val < feasible_obj_val:
                        feasible_obj_val = obj_val
                        feasible_obj_point = copy.copy(tilde_x)

                    for k in range(problem.block_model.num_blocks):
                        problem.add_inner_point(
                            k, tilde_x.get_block(k),
                            self.settings.cg_min_inner_point_distance)
                    logger.info('\nAfter solving fixed NLP projection problem, '
                                'the solution point is feasible')
                    if improved is True:
                        logger.info('the feasible solution point improves')
                        logger.info('Obj. value: {0}'.format(
                            result.sense * result.primal_bound))
                    else:
                        logger.info('the feasible solution point does '
                                    'not improve')
                        logger.info('Obj. value: {0}'.format(
                            result.sense * obj_val))
                else:
                    logger.info(
                        '\nAfter solving fixed NLP the solution point is '
                        'infeasible')

                if iter is None and sol_is_feasible is True:  # this is
                    # for printing number of iteration in
                    # the logger when generating feasible candidate
                    logger.info('Feasible candidate obtained in this '
                                'iteration: {0}'
                                .format(result.sense * obj_val))
                elif iter is not None and sol_is_feasible is True:
                    logger.info('Feasible candidate '
                                'obtained in iter {0}: round {1}: pool {2}: {3}'
                                .format(int(iter), ii, i,
                                        result.sense * obj_val))
                elif iter is not None and sol_is_feasible is False:
                    logger.info('No feasible candidate '
                                'obtained in iter {0}: round {1}: pool {2}'
                                .format(int(iter), ii, i))

                if i == i_max:
                    break
                else:
                    hat_x = hat_x_list[i]
                    logger.info('\nSolution pool: solution {0}'.format(i + 1))

            if feasible_obj_val < old_feasible_obj_val:
                logger.info(
                    '\n---------------------------------------------------')
                if iter is None and feasible_obj_val \
                        is not float('inf'):
                    logger.info('Best feasible candidate obtained in this '
                                'iteration: {0}'
                                .format(result.sense *
                                        feasible_obj_val))
                elif iter is not None and feasible_obj_val \
                        is not float('inf'):
                    logger.info('Best feasible candidate '
                                'obtained in iter {0}: {1}'
                                .format(int(iter),
                                        result.sense *
                                        feasible_obj_val))

                start_point = start_point * tau + feasible_obj_point * (1 - tau)
                old_feasible_obj_val = feasible_obj_val
                ii += 1

                logger.info('Local search iter {0}'.format(ii))

            else:
                logger.info('New search does not find better '
                            'local feasible solution')
                break

            if ii == self.settings.cg_find_sol_mip_pool_max_round:
                logger.info('reaches local search round limit {0}'.format(ii))
                break

    def nlp_solve(self, solver_name, point_to_fix=None, start_point=None,
                  cut_direction=None):
        """Solves :class:`~problem.nlp_master_problem.NlpProblem`.
        Solved mostly with fixed integer variables

        :param solver_name: External solver name
        :type solver_name: str
        :param point_to_fix: Point to be fixed using the integer variables
        :type point_to_fix: BlockVector
        :param start_point: Point for the warm start for the external solver
        :type start_point: BlockVector
        :param cut_direction: Objective direction
        :type cut_direction: BlockVector
        :return: Solution point, objective value, flag if the solution point \
        is feasible
        :rtype: tuple
        """
        if point_to_fix is not None:
            self.nlp_problem.fix_integers(point_to_fix)

        if cut_direction is not None:
            self.nlp_problem.set_new_objective(cut_direction)

        x, obj_val, duals, sol_is_feasible = \
            self.nlp_problem.solve(solver_name,
                                   start_point=start_point)

        if point_to_fix is not None:
            self.nlp_problem.unfix_all_variables()

        if cut_direction is not None:
            self.nlp_problem.set_default_objective()

        return x, obj_val, sol_is_feasible

    def solve_mip_proj_problem(self, solver_name, point_to_project,
                               target_value=float('inf'), pool_solutions=100):
        """Solves
        :class:`~problem.projection_master_problem.MipProjectionMasterProblem`

        :param solver_name: External solver name
        :type solver_name: str
        :param point_to_project: Point to project from, it is in the original \
        space
        :type point_to_project: BlockVector
        :return: Solution point, objective value
        :rtype: tuple
        """

        self.mip_projection_problem.set_projection_point(
            point_to_project)

        self.mip_projection_problem.update_optimality_cut(target_value)

        x, obj_val, duals, sol_is_feasible = \
            self.mip_projection_problem.solve(solver_name, pool_solutions
                                              =pool_solutions)
        # depending on solver name, x can contain more solution points

        return x, obj_val, sol_is_feasible

    def solve_nlp_resource_proj_problem(self, solver_name, point_to_project,
                                        target_value=float('inf'),
                                        start_point=None):
        """Solves
        :class:`~problem.projection_master_problem.NlpResourceProjectionProblem`

        :param solver_name: External solver name
        :type solver_name: str
        :param point_to_project: Point to project from, it is in the image space
        :type point_to_project: BlockVector
        :param start_point: Starting point for external solver
        :type start_point: BlockVector
        :return: Solution point, objective value, flag indicating if the \
        solution point is infeasible, \
        slack value of the soft fixing of target cut
        :rtype: tuple
        """

        self.nlp_resource_projection_problem\
            .set_projection_point(point_to_project)
        self.nlp_resource_projection_problem.update_optimality_cut(target_value)

        x_sol, obj_val, _, sol_is_feasible = \
            self.nlp_resource_projection_problem.solve(solver_name,
                                                       start_point=
                                                       start_point)

        return x_sol, obj_val, sol_is_feasible


class PyomoSubModel(SubModelBase):
    """Container class which stores the variables from the single block and
    local nonlinear constraints.

    :param model: Input Pyomo model
    :type model: ConcreteModel
    :param vars_in_block: List of original variable names from the model
    :type vars_in_block: list
    :param block_id: Identifier for block
    :type block_id: int
    :param variables: List of all variables with all necessary properties
    :type variables: list
    :param block_size: Number of variables in the sub-model
    :type block_size: int
    :param integer: Indicates if the current sub-model contains variable of \
    integer type
    :type integer: bool
    :param nonlin_constr: List of local nonlinear constraints stored using \
    original Pyomo expression
    :type nonlin_constr: list
    """

    def __init__(self, model, vars_in_block, block_id):
        """Constructor method"""
        super().__init__(vars_in_block, block_id)

        # region Var creation
        for var_name in self.vars_in_block:
            var = model.find_component(var_name)
            self.variables.append(VarDomain(var.ub, var.lb, var.domain.name))
            if var.domain.name == 'Binary' or var.domain.name == 'Integers':
                self.integer = True
        # endregion

        # region creating NonlinearConstraint
        for block_obj in model.block_data_objects():
            for con_name, con_obj in \
                    block_obj.component_map(Constraint,
                                            active=True).items():
                if con_obj.__class__ is ScalarConstraint:
                    self.read_nonlinear_constraint(con_obj)
                elif con_obj.__class__ is IndexedConstraint:
                    for index in con_obj:
                        self.read_nonlinear_constraint(con_obj[index])
                else:
                    raise ValueError(
                         'Dev: Found constraints object type which '
                         'was not considered')
        # endregion

        # check if block is linear
        if len(self.nonlin_constr) == 0:
            self.linear = True

    def read_nonlinear_constraint(self, con_obj):
        """Determines if the given constraint belongs to this sub-model.
        If yes, it adds to the list of nonlinear constraints by copying the
        Pyomo expression

        :param con_obj: Pyomo constraint object
        :type con_obj: ScalarConstraint or IndexedConstraint
        """
        con_expr = con_obj.body
        degree = con_expr.polynomial_degree()
        if degree is None or degree > 1:
            # check if constraint belongs to the current block
            if self.constraint_vars_in_block(con_obj.expr) is True:
                self.nonlin_constr.append(
                    NonLinearConstraint(con_obj.expr.clone(),
                                        self.vars_in_block))

    def constraint_vars_in_block(self, expr):
        """Checks if the Pyomo expression belongs to the current sub-model

        :param expr: Pyomo expression.
        :type expr: Expression
        """
        vars_in_expr = identify_variables(expr)
        contained = True
        for var in vars_in_expr:
            if var.name not in self.vars_in_block:
                contained = False
                break
        return contained

    def compute_gradients(self):
        """Computes gradients for each nonlinear constraint and stores in the
        constraint object"""
        for con in self.nonlin_constr:
            con.compute_gradient()

    def round(self, point):
        """Round point to the closest integer

        :param point: Given point
        :type point: ndarray
        :return: New rounded point
        :rtype: ndarray
        """
        rounded_point = copy.deepcopy(point)
        for i, var in enumerate(self.variables):
            if var.type == 'Integers' or var.type == 'Binary':
                rounded_point[i] = round(point[i])
        return rounded_point


class PyomoSubProblems(SubProblemsBase):
    """Container class for managing all sub-problems

    :param minlp_sub_problem: Sub-probem with linear objective
    :type minlp_sub_problem: PyomoMinlpSubProblem
    :param proj_sub_problem: Pure projection sub-problem
    :type proj_sub_problem: PyomoProjectionSubProblem
    :param resource_constrained_sub_problem: Resource constrained sub-problem \
    for checking the feasibility of the resources
    :type resource_constrained_sub_problem: PyomoResourceConstrainedSubProblem
    :param line_search_sub_problem: Line search sub-problem
    :type line_search_sub_problem: PyomoLineSearchSubProblem
    """

    def __init__(self, sub_models, cuts, block_id, settings):
        """Constructor method
        :param approx_data:
        """
        self.block_id = block_id
        self.settings = settings
        self.integer = sub_models[block_id].integer
        super().__init__(block_id)

        self.minlp_sub_problem = \
            PyomoMinlpSubProblem(sub_models, cuts, block_id)

        self.proj_sub_problem = \
            PyomoProjectionSubProblem(sub_models, cuts, block_id)

        self.line_search_sub_problem = \
            PyomoLineSearchSubProblem(sub_models, cuts, block_id)

        self.resource_proj_sub_problem = \
            PyomoResourceProjectionSubProblem(sub_models, cuts, block_id)

    def global_solve(self, result, direction, start_point=None):

        solver_name = self.settings.minlp_solver
        solver_options = self.settings.get_minlp_solver_options()

        y_new, primal_bound, dual_bound, sol_is_feasible = \
            self.minlp_solve(solver_name, solver_options=solver_options,
                             start_point=start_point, direction=direction)

        return y_new, primal_bound, dual_bound, sol_is_feasible

    def local_solve(self, result, direction, start_point=None):

        solver_options = self.settings.get_nlp_solver_options()
        # in order to solve NLP relaxation of MINLP problem it is not
        # necessary explicitly to relax integer variables
        # the NLP solver simply treats them as continuous variables
        unfixed_tilde_y, new_point_obj_val, dual_bound, sol_is_feasible = \
            self.minlp_solve(
                self.settings.nlp_solver, direction=direction,
                solver_options=solver_options, start_point=start_point)

        if self.integer is True:
            result.cg_num_fixed_nlp_problems += 1

            rounded_point = \
                self.minlp_sub_problem.sub_model.round(
                    unfixed_tilde_y)
            # start_point is used for fixing the integers
            tilde_y, new_point_obj_val, dual_bound, sol_is_feasible = \
                self.fixed_minlp_solve(
                    self.settings.nlp_solver,
                    start_point=rounded_point,
                    direction=direction,
                    solver_options=solver_options)

        else:
            tilde_y = unfixed_tilde_y

        return tilde_y, new_point_obj_val, dual_bound, sol_is_feasible

    def minlp_solve(self, solver_name, solver_options=None, start_point=None,
                    direction=None, cell=None):
        """Solves :class:`MinlpSubProblem`

        :param solver_name: External solver name
        :type solver_name: str
        :param solver_options: External solver options, defaults to ``None``
        :type solver_options: list or None
        :param start_point: Staring point for the solver, defaults to ``None``
        :type start_point: ndarray or None
        :param direction: Direction for the objective, defaults to ``None``
        :type direction: ndarray or None
        :param cell: Cell, defaults to ``None``
        :type cell: Cell or None
        :return: Solution point, primal and dual bound
        :rtype: tuple
        """
        if direction is None:
            self.minlp_sub_problem.add_objective()
        else:
            self.minlp_sub_problem.set_objective(direction)

        if cell is not None:
            self.minlp_sub_problem.add_cell_constraints(cell)

        y_new, primal_bound, dual_bound, sol_is_feasible = \
            self.minlp_sub_problem.solve(solver_name,
                                         solver_options=solver_options,
                                         start_point=start_point)

        if cell is not None:
            self.minlp_sub_problem.remove_cell_constraints()

        return y_new, primal_bound, dual_bound, sol_is_feasible

    def fixed_minlp_solve(self, solver_name, start_point, solver_options=None,
                          direction=None, cell=None):
        """Solves :class:`MinlpSubProblem` with fixed integer variables

        :param solver_name: External solver name
        :type solver_name: str
        :param start_point: Staring point for the solver, and point which is \
        used for fixing the integers
        :type start_point: ndarray or None
        :param solver_options: External solver options, defaults to ``None``
        :type solver_options: list or None
        :param direction: Direction for the objective, defaults to ``None``
        :type direction: ndarray or None
        :param cell: Cell, defaults to ``None``
        :type cell: Cell or None
        :return: Solution point, primal and dual bound
        :rtype: tuple
        """
        if direction is None:
            self.minlp_sub_problem.add_objective()
        else:
            self.minlp_sub_problem.set_objective(direction)

        if cell is not None:
            self.minlp_sub_problem.add_cell_constraints(cell)

        self.minlp_sub_problem.fix_integers(start_point)

        y_new, primal_bound, dual_bound, sol_is_feasible = \
            self.minlp_sub_problem.solve(solver_name,
                                         solver_options=solver_options,
                                         start_point=start_point)

        self.minlp_sub_problem.unfix_integers()

        if cell is not None:
            self.minlp_sub_problem.remove_cell_constraints()

        return y_new, primal_bound, dual_bound, sol_is_feasible

    def nlp_proj_solve(self, solver_name, point_to_project, start_point=None):
        """Solves :class:`ProjSubProblem`

        :param solver_name: External solver name
        :type solver_name: str
        :param point_to_project: Projection point
        :type point_to_project: ndarray
        :param start_point: Staring point for the solver, defaults to ``None``
        :type start_point: ndarray or None
        :return: Solution point, primal bound and flag indicating the \
        feasibility of primal solution
        :rtype: tuple
        """
        self.proj_sub_problem.set_projection_point(point_to_project)

        y_new, primal_bound, dual_bound, sol_is_feasible = \
            self.proj_sub_problem.solve(solver_name,
                                        start_point=start_point)

        return y_new, primal_bound, sol_is_feasible

    def resource_proj_solve(self, solver_name, point_to_project,
                            solver_options=None, start_point=None):
        """Solves :class:`ResourceProjSubProblem`

        :param solver_name: External solver name
        :type solver_name: str
        :param point_to_project: Projection point
        :type point_to_project: ndarray
        :param start_point: Staring point for the solver, defaults to ``None``
        :type start_point: ndarray or None
        :return: Solution point, primal bound and flag indicating the \
        feasibility of primal solution
        :rtype: tuple
        """
        self.resource_proj_sub_problem.set_projection_point(point_to_project)

        y_new, primal_bound, dual_bound, sol_is_feasible = \
            self.resource_proj_sub_problem.solve(solver_name,
                                                 start_point=start_point,
                                                 solver_options=solver_options)

        return y_new, primal_bound, sol_is_feasible

    def solve_line_search_subproblem(self, solver_name, exterior_point,
                                     interior_point):
        """Solves :class:`LineSearchSubProblem`

        :param solver_name: External solver name
        :type solver_name: str
        :param exterior_point: Exterior point
        :type exterior_point: ndarray
        :param interior_point: Interior point
        :type interior_point: ndarray
        :return: value of parameter :math:`\\alpha` and solution point
        :rtype: tuple
        """
        self.line_search_sub_problem.set_interior_exterior_points(
            exterior_point, interior_point)

        alpha, point = self.line_search_sub_problem.solve(solver_name)

        return alpha, point

    def add_linear_constraint(self):
        """Adds linear constraints to sub-problems"""
        self.minlp_sub_problem.add_linear_constraint()
        self.proj_sub_problem.add_linear_constraint()

    def update_var_lower_bound(self, index):
        """Updates the lower bound of variable by index

        :param index: Index of the variable (block_id, index)
        :type index: tuple
        """
        self.minlp_sub_problem.update_var_lower_bound(index)
        self.proj_sub_problem.update_var_lower_bound(index)
        self.line_search_sub_problem.update_var_lower_bound(index)

    def update_var_upper_bound(self, index):
        """Updates the upper bound of variable by index

        :param index: Index of the variable (block_id, index)
        :type index: tuple
        """
        self.minlp_sub_problem.update_var_upper_bound(index)
        self.proj_sub_problem.update_var_upper_bound(index)
        self.line_search_sub_problem.update_var_upper_bound(index)
