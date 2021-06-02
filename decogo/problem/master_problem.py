"""Manages inner master problems"""

import logging

from decogo.problem.inner_master_problem import InnerMasterProblem, \
    MiniInnerMasterProblem, ExtendedInnerMasterProblem

logger = logging.getLogger('decogo')


class MasterProblems:
    """Container class for managing all master problems

    :param inner_master_problem: Inner Approximation master problem
    :type inner_problem: InnerMasterProblem
    """

    def __init__(self, block_model, approx_data):
        """Constructor method"""
        # CG master problems
        self.inner_problem = InnerMasterProblem(block_model, approx_data)

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

    def add_inner_point(self, block_id):
        """Adds inner point to the
        :class:`~problem.inner_master_problem.InnerMasterProblem` by calling
        :meth:`~problem.inner_master_problem.InnerMasterProblem.add_column`

        :param block_id: Block identifier
        :type block_id: int
        """
        self.inner_problem.add_column(block_id)

        # # for mini_inner_problem
        # if self.dyn_cg is True:
        #     if block_id in \
        #             range(self.mini_inner_problem.block_model.num_blocks):
        #         self.mini_inner_problem.add_column(block_id)
