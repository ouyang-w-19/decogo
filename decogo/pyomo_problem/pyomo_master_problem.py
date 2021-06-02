"""Manages all Pyomo master problems"""

import logging

from decogo.problem.inner_master_problem import InnerMasterProblem, \
    MiniInnerMasterProblem, ExtendedInnerMasterProblem
from decogo.pyomo_problem.nlp_master_problem import NlpProblem
from decogo.pyomo_problem.oa_master_problem import OaMasterProblem, \
    MipOaMasterProblem, CompactOaMasterProblem
from decogo.pyomo_problem.oa_master_problem import SlackMipOaMasterProblem
from decogo.pyomo_problem.projection_master_problem import \
    NlpResourceProjectionProblem, \
    MipProjectionMasterProblem
from decogo.util.block_vector import BlockVector

logger = logging.getLogger('decogo')


class PyomoMasterProblems:
    """Container class for managing all master problems

    :param inner_master_problem: Inner Approximation master problem
    :type inner_problem: InnerMasterProblem
    :param compact_oa_master_problem: Compact OA master problem
    :type compact_oa_problem: CompactOaMasterProblem
    :param oa_master_problem: OA master problem with valid cuts generated \
    after solving the sub-problems
    :type oa_problem: OaMasterProblem
    :param mip_oa_master_problem: MIP OA master with linearization cuts
    :type mip_oa_problem: MipOaMasterProblem
    :param slack_mip_oa_problem: MIP OA master with linearization cuts \
    used for solving regarding fixed variables
    :type slack_mip_oa_problem: SlackMipOaMasterProblem
    :param nlp_problem: NLP master problem
    :type nlp_problem: NlpProblem
    :param mip_projection_master_problem: MIP projection master problem
    :type mip_projection_problem: MipProjectionMasterProblem
    :param nlp_resource_projection_problem: NLP projection master problem
    :type nlp_resource_projection_problem: NlpResourceProjectionProblem
    """

    def __init__(self, block_model, approx_data, strategy):
        """Constructor method"""
        # CG master problems
        self.strategy = strategy
        if self.strategy == 'DynCG':
            self.inner_problem = \
                ExtendedInnerMasterProblem(block_model, approx_data)
            # mini master problem
            self.mini_inner_problem = MiniInnerMasterProblem(block_model,
                                                             approx_data)
        elif self.strategy == 'CG':
            self.inner_problem = InnerMasterProblem(block_model, approx_data)

        # OA master problems
        if self.strategy == 'OA':
            self.compact_oa_problem = CompactOaMasterProblem(block_model,
                                                             approx_data)
            self.oa_problem = OaMasterProblem(block_model)
            self.mip_oa_problem = MipOaMasterProblem(block_model, approx_data)
            self.slack_mip_oa_problem = SlackMipOaMasterProblem(block_model,
                                                                approx_data)
        # NLP master problems
        self.nlp_problem = NlpProblem(block_model)

        # projection problems
        self.mip_projection_problem = MipProjectionMasterProblem(block_model)
        self.nlp_resource_projection_problem = \
            NlpResourceProjectionProblem(block_model)

    def solve_ia(self, solver_name, slack_weights=None):
        """Solves :class:`~problem.inner_master_problem.InnerMasterProblem`

        :param solver_name: External solver name
        :type solver_name: str
        :param slack_weights: Slack weights, defaults to ``None``
        :type slack_weights: ndarray
        :return: Active (selected) cells, weights for inner points, solution \
        point in original space, solution in image space, slack values, \
        dual solution, objective value
        :rtype: tuple
        """

        if slack_weights is not None:
            self.inner_problem.set_slack_weights(slack_weights)
        else:
            # compute and set slack weights with default method
            self.inner_problem.compute_and_set_default_slack_weights()
        if self.strategy == 'DynCG':
            z_output, x, w, slacks, duals, obj_value, slack_hyper_max, \
                slack_hyper = self.inner_problem.solve(solver_name)

            return z_output, x, w, slacks, duals, obj_value, slack_hyper_max, \
                slack_hyper
        else:
            z_output, x, w, slacks, duals, obj_value \
                = self.inner_problem.solve(solver_name)

            return z_output, x, w, slacks, duals, obj_value

    def solve_mini_ia(self, solver_name, hyper_block, dir_im_space):

        self.mini_inner_problem.set_objective(dir_im_space)
        global_con_indices = \
            self.mini_inner_problem.block_model.global_con_hyper_block(
                hyper_block)
        self.mini_inner_problem.deactivate_global_constraints(
            global_con_indices)
        self.mini_inner_problem.deactivate_blocks(hyper_block)

        z, x, w, slacks, duals, obj_value = \
            self.mini_inner_problem.solve(solver_name)

        # activate back
        self.mini_inner_problem.activate_blocks(hyper_block)
        self.mini_inner_problem.activate_global_constraints(global_con_indices)

        return x, global_con_indices, slacks

    def solve_compact_oa(self, solver_name, direction=None, bounds=None,
                         solver_options=None):
        """Solves :class:`~problem.oa_master_problem.CompactOaMasterProblem`

        :param solver_name: External solver name
        :type solver_name: str
        :param direction: Direction vector, defaults to ``None``
        :type direction: ndarray
        :param bounds: Tuple of upper and lower resource bounds, defaults \
        to ``None``
        :type bounds: tuple
        :param solver_options: External solver options, defaults to ``None``
        :type solver_options: list
        :return: Solution point, dual solution and objective value
        :rtype: tuple
        """
        if direction is not None:
            self.compact_oa_problem.set_new_objective(direction)

        if bounds is not None:
            self.compact_oa_problem.set_bounds(bounds[0], bounds[1])

        w, duals, obj_val = \
            self.compact_oa_problem.solve(solver_name,
                                          solver_options=solver_options)

        if direction is not None:
            self.compact_oa_problem.set_default_objective()

        if bounds is not None:
            self.compact_oa_problem.remove_bounds()

        return w, duals, obj_val

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

    def solve_agg_mip_proj_problem(self, solver_name, point_to_project,
                                   agg_blocks,
                                   target_value=float('inf'),
                                   pool_solutions=10):
        """Solves aggregated sub-problem of
        :class:`~problem.projection_master_problem.MipProjectionMasterProblem`.
        It is not full master problem anymore, instead it is an aggregated
        sub-problem with several blocks

        :param solver_name: External solver name
        :type solver_name: str
        :param point_to_project: Point to project from, it is in the original \
        space
        :type point_to_project: BlockVector
        :param agg_blocks: indices of atomic blocks to aggregate
        :type agg_blocks: tuple or list
        :param glob_con_indices: indices of global constraints to consider in \
        aggregated subproblem
        :type glob_con_indices: tuple or list
        :return: Solution point, objective value
        :rtype: tuple
        """

        self.mip_projection_problem.deactivate_blocks(agg_blocks)
        global_con_indices = \
            self.mip_projection_problem.block_model.global_con_hyper_block(
                agg_blocks)
        self.mip_projection_problem.\
            deactivate_global_constraints(global_con_indices)

        self.mip_projection_problem.set_projection_point(
            point_to_project)

        self.mip_projection_problem.update_optimality_cut(target_value)

        x, obj_val, duals, sol_is_feasible = \
            self.mip_projection_problem.solve(solver_name,
                                              pool_solutions=pool_solutions,
                                              agg_blocks=agg_blocks)

        self.mip_projection_problem.activate_blocks(agg_blocks)
        self.mip_projection_problem.activate_global_constraints(
            global_con_indices)

        return x, obj_val, sol_is_feasible

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

    def agg_nlp_solve(self, solver_name, agg_blocks,
                      point_to_fix=None, start_point=None, cut_direction=None):
        """Solves :class:`~problem.nlp_master_problem.NlpProblem`.
        Solved mostly with fixed integer variables

        :param solver_name: External solver name
        :type solver_name: str
        :param agg_blocks: indices of atomic blocks to aggregate
        :type agg_blocks: tuple or list
        :param glob_con_indices: indices of global constraints to consider in \
        aggregated subproblem
        :type glob_con_indices: tuple or list
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

        self.nlp_problem.deactivate_blocks(agg_blocks)
        global_con_indices = \
            self.nlp_problem.block_model.global_con_hyper_block(
                agg_blocks)
        self.nlp_problem.deactivate_global_constraints(global_con_indices)

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

        # activate back
        self.nlp_problem.activate_blocks(agg_blocks)
        self.nlp_problem.activate_global_constraints(global_con_indices)

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

    def solve_agg_nlp_resource_proj_problem(self, solver_name, point_to_project,
                                            agg_blocks, glob_con_indices,
                                            target_value=float('inf'),
                                            start_point=None):
        """Solves
        :class:`~problem.projection_master_problem.NlpResourceProjectionProblem`

        :param solver_name: External solver name
        :type solver_name: str
        :param point_to_project: Point to project from, it is in the image space
        :type point_to_project: BlockVector
        :param agg_blocks: indices of atomic blocks to aggregate
        :type agg_blocks: tuple or list
        :param glob_con_indices: indices of global constraints to consider in \
        aggregated subproblem
        :type glob_con_indices: tuple or list
        :param start_point: Starting point for external solver
        :type start_point: BlockVector
        :return: Solution point, objective value, flag indicating if the \
        solution point is infeasible, \
        slack value of the soft fixing of target cut
        :rtype: tuple
        """

        self.nlp_resource_projection_problem.deactivate_blocks(agg_blocks)
        self.nlp_resource_projection_problem.deactivate_global_constraints(
            glob_con_indices)

        self.nlp_resource_projection_problem\
            .set_projection_point(point_to_project)
        self.nlp_resource_projection_problem.update_optimality_cut(target_value)

        x_sol, obj_val, _, sol_is_feasible = \
            self.nlp_resource_projection_problem.solve(solver_name,
                                                       start_point=start_point)

        # activate back
        self.nlp_resource_projection_problem.activate_blocks(agg_blocks)
        self.nlp_resource_projection_problem.activate_global_constraints(
            glob_con_indices)

        return x_sol, obj_val, sol_is_feasible

    def agg_minlp_solve(self, solver_name, agg_blocks,
                        solver_options=None, cut_direction=None):
        """Solves :class:`~problem.nlp_master_problem.NlpProblem` as aggregated
        MINLP subproblem

        :param solver_name: External solver name
        :type solver_name: str
        :param agg_blocks: indices of atomic blocks to aggregate
        :type agg_blocks: tuple or list
        :param glob_con_indices: indices of global constraints to consider in \
        aggregated subproblem
        :type glob_con_indices: tuple or list
        :param cut_direction: Objective direction
        :type cut_direction: BlockVector
        :return: Solution point, objective value, flag if the solution point \
        is feasible
        :rtype: tuple
        """

        self.nlp_problem.deactivate_blocks(agg_blocks)
        global_con_indices = \
            self.nlp_problem.block_model.global_con_hyper_block(
                agg_blocks)
        self.nlp_problem.deactivate_global_constraints(global_con_indices)

        if cut_direction is not None:
            self.nlp_problem.set_new_objective(cut_direction)

        x, primal_bound, duals, sol_is_feasible = \
            self.nlp_problem.solve(solver_name, solver_options=solver_options)

        if cut_direction is not None:
            self.nlp_problem.set_default_objective()

        # activate back
        self.nlp_problem.activate_blocks(agg_blocks)
        self.nlp_problem.activate_global_constraints(global_con_indices)

        return x, primal_bound, sol_is_feasible

    def solve_mip_oa(self, solver_name):
        """Solves :class:`~problem.oa_master_problem.MipOaMasterProblem`

        :param solver_name: External solver name
        :type solver_name: str
        :param start_point: Point for the warm start for the external solver
        :type start_point: BlockVector
        :return: Solution point, objective value
        :rtype: tuple
        """
        x_oa, obj_val, duals, sol_is_feasible = \
            self.mip_oa_problem.solve(solver_name)

        return x_oa, obj_val

    def solve_integer_relaxed_oa(self, solver_name):
        """Solves :class:`~problem.oa_master_problem.MipOaMasterProblem` with
        relaxed integer variables

        :param solver_name: External solver name
        :type solver_name: str
        :return: Solution point, objective value
        :rtype: tuple
        """
        self.mip_oa_problem.relax_integers()

        x_oa, obj_val, duals, sol_is_feasible = \
            self.mip_oa_problem.solve(solver_name)

        self.mip_oa_problem.set_integers()

        return x_oa, obj_val, duals

    def solve_mipoa_with_slacks(self, solver_name, x, block_id):
        """Solves
        :class:`~problem.oa_master_problem.MipOaMasterProblemWithSlacks`
        with k-th unfixed or set of unfixed blocks

        :param solver_name: External solver name
        :type solver_name: str
        :param x: Point for fixing
        :type x: BlockVector
        :param block_id: Blocks not to fix
        :type block_id: int or set
        :return: Solution point, objective value, flag if the slacks are zero
        :rtype: tuple
        """
        self.slack_mip_oa_problem.fix_all_variables(x, block_id=block_id)
        self.slack_mip_oa_problem.set_objective(block_id)

        x_sol, obj_val, duals, sol_is_feasible, slacks_are_zero = \
            self.slack_mip_oa_problem.solve(solver_name)

        self.slack_mip_oa_problem.unfix_all_variables()

        return x_sol, obj_val, slacks_are_zero

    def solve_outer_master_problem(self, solver_name):
        """Solves :class:`~problem.oa_master_problem.OaMasterProblem`

        :param solver_name: External solver name
        :type solver_name:
        :return: Solution point, objective value, dual solution
        :rtype: tuple
        """
        x, obj_val, duals, sol_is_feasible = \
            self.oa_problem.solve(solver_name)

        return x, obj_val, duals

    def add_linearization_cuts(self, number_of_cuts):
        """Adds the last :math:`n` linearization cuts

        :param n: Number of cuts to add
        :type n: dict
        """
        self.mip_oa_problem.add_linearization_cuts(number_of_cuts)
        self.slack_mip_oa_problem.add_linearization_cuts(number_of_cuts)

    def update_var_lower_bound(self, index):
        """Updates lower bound of the variable by calling
        :meth:`~problem.master_problem_base.MasterProblemBase.update_var_lower_bound`

        :param index: Index as pair (block_id, index)
        :type index: tuple
        """
        self.oa_problem.update_var_lower_bound(index)
        self.mip_oa_problem.update_var_lower_bound(index)
        self.slack_mip_oa_problem.update_var_lower_bound(index)
        self.nlp_problem.update_var_lower_bound(index)

    def update_var_upper_bound(self, index):
        """Updates lower bound of the variable by calling
        :meth:`~problem.master_problem_base.MasterProblemBase.update_var_upper_bound`

        :param index: Index as pair (block_id, index)
        :type index: tuple
        """
        self.oa_problem.update_var_upper_bound(index)
        self.mip_oa_problem.update_var_upper_bound(index)
        self.slack_mip_oa_problem.update_var_upper_bound(index)
        self.nlp_problem.update_var_upper_bound(index)

    def add_inner_point(self, block_id):
        """Adds inner point to the
        :class:`~problem.inner_master_problem.InnerMasterProblem` by calling
        :meth:`~problem.inner_master_problem.InnerMasterProblem.add_column`

        :param block_id: Block identifier
        :type block_id: int
        """
        self.inner_problem.add_column(block_id)

        # mini_inner_problem
        if self.strategy == 'DynCG':
            if block_id in \
                    range(self.mini_inner_problem.block_model.num_blocks):
                self.mini_inner_problem.add_column(block_id)

    def add_lin_local_constr(self, block_id):
        """Adds linear local constraints. It takes the last local constraint
        stored in the :class:`model.block_model.BlockModel`

        :param block_id: Block identifier
        :type block_id: int
        """
        self.oa_problem.add_linear_local_constraint(block_id)

    def add_compact_lin_local_constr(self, block_id, lhs, relation, rhs):
        """Adds compact linear constraint to master problems

        :param block_id: Block identifier
        :type block_id: int
        :param lhs: Left hand side of the constraints
        :type lhs: ndarray
        :param relation: Relation of the constraint
        :type relation: str
        :param rhs: Right hand side of the constraint
        :type rhs: float
        """

        self.compact_oa_problem.add_compact_lin_local_const(block_id, lhs,
                                                            relation, rhs)