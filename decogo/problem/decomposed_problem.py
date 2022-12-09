"""This module manages block model, approximation data and all problems."""

import logging

from decogo.problem.approx_data import ApproxData
from decogo.problem.master_problem import MasterProblems

logger = logging.getLogger('decogo')


class DecomposedProblem:
    """This class contains all sub-problems, master problems and approximation
    data and methods for manipulating them (add, update etc.)

    :param block_model: Block model
    :type block_model: BlockModel
    :param sub_problems: Contains all necessary sub-problems
    :type sub_problems: list
    :param original_problem: Contains original problem
    :type original_problem: subclass of OriginalProblemBase
    """

    def __init__(self, block_model, sub_problems, original_problem):
        """Constructor method"""
        self.block_model = block_model
        self.approx_data = ApproxData(block_model)  # Approximation data class
        # (Inner points, linearization cuts, etc.)
        self.sub_problems = sub_problems
        self.original_problem = original_problem
        self.master_problems = MasterProblems(self.block_model,
                                              self.approx_data)  # Contains all
        # necessary Pyomo (inner) master problems
        self.linear_block = [k for k in range(self.block_model.num_blocks)
                             if self.block_model.sub_models[k].linear is True]

    def add_inner_point(self, block_id, point, min_inner_point_dist=None):
        """Adds an inner point to the list of points and updates
        corresponding master problems, see
        :meth:`problem.approx_data.ApproxData.add_inner_point`"""

        # add column just for nonlinear block
        if block_id not in self.linear_block:
            is_new_point, point, column = \
                self.approx_data.add_inner_point(block_id, point,
                                                 min_inner_point_dist)
            if is_new_point is True:
                self.master_problems.add_inner_point(block_id)

                # add column of hyper block to corresponding atomic blocks
                if len(self.approx_data.inner_points.KT[block_id]) > 1:
                    # print('add column to hyper block ' + str(block_id))
                    for k in self.approx_data.inner_points.KT[block_id]:
                        is_new_point_mini, _, _ = \
                            self.approx_data.add_inner_point(k, point[k])
                        if is_new_point_mini is True:
                            self.master_problems.add_inner_point(k)
                        #     print('add column to atomic block ' + str(k))
                        # else:
                        #     print('not new column for atomic block ' + str(k))
            #     else:
            #         print('add column to atomic block ' + str(block_id))
            # else:
            #     if len(self.approx_data.inner_points.KT[block_id]) > 1:
            #         print('not new column for hyper block ' + str(block_id))
            #     else:
            #         print('not new column for atomic block ' + str(block_id))

            return is_new_point, point, column
        else:
            return False, point, None

    def get_min_inner_point(self, block_id, direction):
        """Gets inner point with respect to the minimum value computed with
        some direction in original space, see
        :meth:`problem.approx_data.ApproxData.get_min_inner_point`"""
        return self.approx_data.get_min_inner_point(block_id, direction)

    def get_min_column(self, block_id, direction):
        """Gets column with respect to the minimum value computed with some
        direction in image space, see
        :meth:`problem.approx_data.ApproxData.get_min_column`"""
        return self.approx_data.get_min_column(block_id, direction)

    def get_inner_points_size(self, block_id):
        """Gets inner points size, see
        :meth:`problem.approx_data.ApproxData.get_inner_points_size`"""
        return self.approx_data.get_inner_points_size(block_id)

    def eval_viol_lin_global_constraints(self, point):
        """Evaluates the violation of global linear constraints, see
        :meth:`model.block_model.BlockModel.evaluate_violation_linear_global_constraints`"""
        return self.block_model.eval_viol_lin_global_constraints(point)

