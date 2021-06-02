"""Main module for managing block model and approximation data"""

import logging

import numpy as np

from decogo.problem.approx_data import ApproxData
from decogo.pyomo_problem.pyomo_master_problem import PyomoMasterProblems
from decogo.pyomo_problem.subproblem import PyomoSubProblems

logger = logging.getLogger('decogo')


class PyomoDecomposedProblem:
    """This class contains all subproblems, master problems and approximation
    data and methods for manipulating them (add, update etc.)

    :param block_model: Block model
    :type block_model: BlockModel
    :param approx_data: Approximation data class (Inner points, linearization \
    cuts, etc.)
    :type approx_data: ApproxData
    :param sub_problems: Contains all necessary Pyomo subproblems
    :type sub_problems: list
    :param master_problems: Contains all necessary Pyomo master problems
    :type master_problems: PyomoMasterProblems
    """

    def __init__(self, block_model, strategy):
        """Constructor method"""
        self.block_model = block_model
        self.approx_data = ApproxData(block_model)
        self.sub_problems = [PyomoSubProblems(block_model, k)
                             for k in range(self.block_model.num_blocks)]
        self.master_problems = PyomoMasterProblems(self.block_model,
                                                   self.approx_data,
                                                   strategy=strategy)

        self.linear_block = [k for k in range(self.block_model.num_blocks)
                             if self.block_model.sub_models[k].linear is True]

    def add_linear_local_constraint(self, block_id, lhs, relation, rhs):
        """Adds a new valid local linear constraint to block model cut pool
        and to the sub-problems
        
        :param block_id: Block identifier
        :type block_id: int
        :param lhs: Left hand side of the constraint
        :type lhs: ndarray
        :param relation: Relation of the constraint :math:`\\leq, \\geq, =`
        :type relation: str
        :param rhs: Right hand side of the constraint
        :type rhs: float
        """
        coeff = []
        for i in range(self.block_model.block_sizes[block_id]):
            if lhs[i] != 0:
                coeff.append((block_id, i, lhs[i]))

        if len(coeff) > 0:
            self.block_model.cuts.add_lin_local_constr(coeff, relation,
                                                       rhs,
                                                       self.block_model.block_sizes)
            # update master problems
            self.master_problems.add_lin_local_constr(block_id)

    def add_compact_lin_local_constr(self, block_id, lhs, relation, rhs):
        """Adds valid compact linear cut to master problems and to the
        container, see :meth:`problem.approx_data.ApproxData.add_compact_cut`"""
        if np.allclose(lhs, np.zeros(shape=len(lhs))) is False:
            # adds valid local linear cuts (D) to master problems in
            # corresponding im/orig space
            added_compact_cut = \
                self.master_problems.add_compact_lin_local_constr(block_id, lhs,
                                                                  relation, rhs)
            if added_compact_cut:
                self.approx_data.add_compact_cut_heu_oa(block_id, lhs, relation,
                                                        rhs)

            self.sub_problems[block_id].add_compact_lin_local_constr(lhs,
                                                                     relation,
                                                                     rhs)
            self.approx_data.add_compact_cut(block_id, lhs, relation, rhs)

    def update_var_lower_bound(self, new_lower_bound, index):
        """Updates the lower bound of the given variable at block model and
        Pyomo models

        :param new_lower_bound: New lower bound
        :type new_lower_bound: float
        :param index: Index of the variable as tuple (block_id, index)
        :type index: tuple
        """
        # update in block model
        self.block_model.update_var_lower_bound(new_lower_bound, index)

        # update in Pyomo models
        self.master_problems.update_var_lower_bound(index)

        k, i = index
        self.sub_problems[k].update_var_lower_bound(index)

    def update_var_upper_bound(self, new_upper_bound, index):
        """Updates the upper bound of the given variable at block model and
        Pyomo models

        :param new_upper_bound: New lower bound
        :type new_upper_bound: float
        :param index: Index of the variable as tuple (block_id, index)
        :type index: tuple
        """
        # update in block model
        self.block_model.update_var_upper_bound(new_upper_bound, index)

        # update in Pyomo models
        self.master_problems.update_var_upper_bound(index)

        k, i = index
        self.sub_problems[k].update_var_upper_bound(index)

    def compute_gradients(self):
        """Computes gradients of the nonlinear constraints (used by OA
        solver)"""
        self.block_model.compute_gradients()

    def add_linearization_cuts(self, y, eps, x=None, block_id=None):
        """Adds the linearization cuts to Pyomo models and to the list of
        cuts, see :meth:`problem.approx_data.ApproxData.add_linearization_cuts`

        :param y: Linearization point
        :type y: BlockVector or ndarray
        :param eps: Accuracy for defining the active constraints
        :type eps: float
        :param x: Solution of OA relaxation
        :type x: BlockVector or ndarray or None
        :param block_id: Block identifier
        :type block_id: int or None
        :return: Number of new added cuts
        :rtype: int
        """
        # add linearization cuts to ApproxData
        n_cuts = self.approx_data.add_linearization_cuts(y, eps, x=x,
                                                         block_id=block_id)
        self.master_problems.add_linearization_cuts(n_cuts)

        return n_cuts

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

    def max_viol_nonlin_constr(self, x):
        """Determines if the solution is feasible regarding the nonlinear
        constraints by computing the maximum violation,
        see :meth:`model.block_model.BlockModel.max_violation_nonlinear_constraints`"""
        return self.block_model.max_violation_nonlinear_constraints(x)

    def eval_viol_lin_global_constraints(self, point):
        """Evaluates the violation of global linear constraints, see
        :meth:`model.block_model.BlockModel.evaluate_violation_linear_global_constraints`"""
        return self.block_model.eval_viol_lin_global_constraints(point)

    def round(self, block_id, point):
        """Rounds point to the closest integer, see
        :meth:`model.block_model.BlockModel.round`"""
        return self.block_model.round(block_id, point)
