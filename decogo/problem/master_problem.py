"""This module manages inner master problems."""

import logging

from decogo.problem.inner_master_problem import InnerMasterProblem

logger = logging.getLogger('decogo')


class MasterProblems:
    """A container class for managing all master problems. This version
    is used for algorithm CG in the refactory of decogo, not available for
    algorithm DBCG.

    :param block_model: Block model
    :type block_model: BlockModel
    :param approx_data: Class that stores inner points and columns
    :type approx_data: ApproxData
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

    def add_inner_point(self, block_id):
        """Adds inner point to the
        :class:`~problem.inner_master_problem.InnerMasterProblem` by calling
        :meth:`~problem.inner_master_problem.InnerMasterProblem.add_column`

        :param block_id: Block identifier
        :type block_id: int
        """
        self.inner_problem.add_column(block_id)

