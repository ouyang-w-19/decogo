"""Stores approximation data generated during the solution process"""

import copy
import logging

import numpy as np

from decogo.model.constraints import LinearConstraint
from decogo.util.block_vector import BlockVector

logger = logging.getLogger('decogo')


class ApproxData:
    """Wrapper class for storing approximation data, i.e. inner points,
    linearization cuts, valid compact cuts and cells.

    :param block_model: Block model
    :type block_model: BlockModel
    :param inner_points: Stores the inner points
    :type inner_points: InnerPoints
    :param linearization_cuts: Stores linearization cuts (for OA algorithm)
    :type linearization_cuts: LinearizationCuts
    :param compact_cuts: Stores valid compact cuts
    :type compact_cuts: CompactCuts
    """

    def __init__(self, block_model):
        """Constructor method"""
        # self.block_model = block_model
        self.inner_points = InnerPoints(block_model)
        self.linearization_cuts = LinearizationCuts(block_model)
        self.compact_cuts = CompactCuts(block_model)

    def add_linearization_cuts(self, y, eps, x=None, block_id=None):
        """Adds linearization cuts by calling
        :meth:LinearizationCuts.add_linearization_cuts"""
        return self.linearization_cuts.add_linearization_cuts(y, eps, x=x,
                                                              block_id=block_id)

    def add_inner_point(self, block_id, point, min_inner_point_distance=None):
        """Adds inner point by calling :meth:`InnerPoints.add_point`"""
        return self.inner_points.add_point(block_id, point,
                                           min_inner_point_distance)

    def get_min_inner_point(self, block_id, direction):
        """Gets inner point with respect to the minimum value computed with
        some direction in original space by calling
        :meth:`InnerPoints.get_min_inner_point`"""
        return self.inner_points.get_min_inner_point(block_id, direction)

    def get_min_column(self, block_id, direction):
        """Gets column with respect to the minimum value computed with some
        direction in image space by calling
        :meth:`InnerPoints.get_min_column`"""
        return self.inner_points.get_min_column(block_id, direction)

    def get_inner_points_size(self, block_id):
        """Gets inner points size by calling :meth:`InnerPoints.get_size`"""
        return self.inner_points.get_size(block_id)

    def add_compact_cut(self, block_id, lhs, relation, rhs):
        """Add valid compact cut by calling :meth:`CompactCuts.add`"""
        self.compact_cuts.add(block_id, lhs, relation, rhs)

    def get_compact_cuts_size(self):
        """Gets compact cut size by calling :meth:`CompactCuts.get_length`"""
        return self.compact_cuts.get_length()


class InnerPoints:
    """Class which stores inner points and corresponding columns

    :param block_model: Block model
    :type block_model: BlockModel
    :param points: Points stored blockwise as dictionary of lists
    :type points: dict
    """

    def __init__(self, block_model):
        """Constructor method"""

        self.block_model = block_model

        # how we store the points:
        # we create the dictionary (k -> [list of tuples (hat_y_k, w_k)])
        # where k is block_id, hat_y_k is a point and w_k is a column defined
        # by w_k = (c_k*hat_y_k, A_k*hat_y_k)
        self.points = {}
        for k in range(self.block_model.num_blocks):
            self.points[k] = []

        # container for indexes of atomic block in aggregated block
        self.KT = {}
        # initialize KT for atomic blocks
        for k in range(self.block_model.num_blocks):
            self.KT[k] = (k,)

    def __getitem__(self, item):
        """Index operator

        :param item: Given index as tuple (block_id, index)
        :type item: tuple
        :return: tuple (point, column), i.e point and corresponding column
        :rtype: tuple
        """
        k, j = item
        return self.points[k][j]

    def is_new_point(self, block_id, column, min_inner_point_distance=None):
        """Computes minimum distance (based on the infinity norm) of column to
        all columns in one block

        :param block_id: Block identifier
        :type block_id: int
        :param column: Given possibly new column
        :type column: ndarray
        :param min_inner_point_distance: Threshold for identifying if the \
        column is new
        :type min_inner_point_distance: float or None
        :return: Result if the column is new
        :rtype: bool
        """
        min_dist = float('inf')

        if len(self.KT[block_id]) == 1:
            # find minimum distance to columns
            for p, col in self.points[block_id]:
                dist = np.linalg.norm(column - col, ord=np.inf)
                if dist < min_dist:
                    min_dist = dist

            new_point = False
            if min_dist >= 1e-10:
                # makes sure that completely identical column is not added
                # to the inner points
                if min_inner_point_distance is not None:
                    if min_dist > min_inner_point_distance:
                        new_point = True
                    else:
                        new_point = False
                else:
                    new_point = True

        elif len(self.KT[block_id]) > 1:
            # find minimum distance to long columns
            for p, col in self.points[block_id]:
                dist_sum = 0
                for i in self.KT[block_id]:
                    dist = np.linalg.norm(column[i] - col[i], ord=np.inf)
                    dist_sum += dist
                if dist_sum < min_dist:
                    min_dist = dist_sum

            new_point = False
            if min_dist >= 1e-10:
                # makes sure that completely identical column is not added
                # to the inner points
                if min_inner_point_distance is not None:
                    if min_dist > min_inner_point_distance:
                        new_point = True
                    else:
                        new_point = False
                else:
                    new_point = True

        return new_point

    def add_point(self, block_id, point, min_inner_point_distance=None):
        """Adds the new point and column. If ``min_inner_point_distance``
        is ``None``, the column is always added (based on the reduced cost
        computation)

        :param block_id: Block identifier
        :type block_id: int
        :param point: Given new point
        :type point: ndarray
        :param min_inner_point_distance: Threshold for identifying if the \
        column is new
        :type min_inner_point_distance: float or None
        :return: Tuple which containes the flag if the column is new, \
        point and corresponding column
        :rtype: tuple
        """
        if len(self.KT[block_id]) == 1:
            if self.block_model.sub_models[block_id].linear is False:
                column = self.block_model.trans_into_im_space(block_id, point)
                new_point = self.is_new_point(block_id, column,
                                              min_inner_point_distance)
            else:
                # add no column to linear atomic block
                new_point = False
                column = self.block_model.trans_into_im_space(block_id, point)

            if new_point is True:
                self.points[block_id].append((point, column))

            return new_point, point, column

        elif len(self.KT[block_id]) > 1:
            # sub-problem for hyper block generate list of points for
            # atomic blocks and list of columns are transformed from the points
            # K_t = [k1, k2]
            # column_t_j = { k1: column_k1_j, k2:column_k2_j}
            column_dict = {}
            point_dict = {}
            for i in self.KT[block_id]:
                point_dict[i] = point.get_block(i)
                column = self.block_model.trans_into_im_space(i, point_dict[i])
                column_dict[i] = column
            new_point = self.is_new_point(block_id, column_dict,
                                          min_inner_point_distance)

            if new_point is True:
                self.points[block_id].append((point_dict, column_dict))

            return new_point, point_dict, column_dict

    def get_min_inner_point(self, block_id, dir_orig_space):
        """Get the inner point based on the minimum value regarding the
        direction in original space, i.e. :math:`y = {\\mathrm{argmin\ }}
        d^Tx, x \\in S`, where :math:`S` is the set of inner points

        :param block_id: Block identifier
        :type block_id: int
        :param dir_orig_space: Given direction
        :type dir_orig_space: ndarray
        :return: Point and corresponding minimum value
        :rtype: tuple
        """
        min_point = 0
        min_obj_val = float('inf')

        if len(self.KT[block_id]) == 1:

            for point, column in self.points[block_id]:
                obj_val = np.dot(dir_orig_space, point)
                if obj_val < min_obj_val:
                    min_obj_val = obj_val
                    min_point = point

        elif len(self.KT[block_id]) > 1:

            for point, column in self.points[block_id]:
                obj_val = 0
                for k in self.KT[block_id]:
                    obj_val += np.dot(dir_orig_space.get_block(k), point[k])
                if obj_val < min_obj_val:
                    min_obj_val = obj_val
                    min_point = point

        return min_point, min_obj_val

    def get_min_column(self, block_id, dir_im_space):
        """Get the column based on the minimum value regarding the direction
        in image space, i.e. :math:`y = {\\mathrm{argmin\ }} d^Tx, x \\in S`,
        where :math:`S` is the set of inner points

        :param block_id: Block identifier
        :type block_id: int
        :param dir_im_space: Given direction
        :type dir_im_space: ndarray
        :return: Column and corresponding minimum value
        :rtype: tuple
        """
        min_column = 0
        min_obj_val = float('inf')

        if len(self.KT[block_id]) == 1:

            for point, column in self.points[block_id]:
                obj_val = np.dot(dir_im_space, column)
                if obj_val < min_obj_val:
                    min_obj_val = obj_val
                    min_column = column

        elif len(self.KT[block_id]) > 1:

            for _, column_dict in self.points[block_id]:
                obj_val = 0
                for (k, column) in column_dict.items():
                    obj_val += np.dot(dir_im_space, column)
                if obj_val < min_obj_val:
                    min_obj_val = obj_val
                    min_column_dict = column_dict

            # transform to 2-D array
            min_column = np.array([[]])
            for (_, column) in min_column_dict.items():
                if min_column.shape[1] == 0:
                    min_column = \
                        np.concatenate((min_column, np.array([column])), axis=1)
                else:
                    min_column = \
                        np.concatenate((min_column, np.array([column])), axis=0)

        return min_column, min_obj_val

    def get_size(self, block_id):
        """Gets the size of inner points of the given block

        :param block_id: Block identifier
        :type block_id: int
        :return: Size of the inner points
        :rtype: int
        """
        return len(self.points[block_id])

    def get_estimated_nadir_point(self, block_id):
        """Gets maximum value for each component of the existing columns

        :param block_id: Block identifier
        :type block_id: int
        :return: Vector with maximum components
        :rtype: ndarray
        """
        w = np.full(shape=self.block_model.cuts.num_of_global_cuts + 1,
                    fill_value=-np.inf)

        for _, column in self.points[block_id]:
            w = np.maximum(w, column)

        return w

    def get_estimated_ideal_point(self, block_id):
        """Gets minimum value for each component of the existing columns

        :param block_id: Block identifier
        :type block_id: int
        :return: Vector with minimum components
        :rtype: ndarray
        """
        w = np.full(shape=self.block_model.cuts.num_of_global_cuts + 1,
                    fill_value=np.inf)

        for _, column in self.points[block_id]:
            w = np.minimum(w, column)

        return w

    def check_block(self, kt):
        # check if kt exists in KT, if not, add kt to KT and return index t
        # if yes, return index of kt in KT
        # is_new_hyper_block = False
        # if kt in self.KT.values():
        #     block_id = list(self.KT.keys())[list(self.KT.values()).index(kt)]
        # else:
        #     block_id = max(self.points.keys()) + 1
        #     self.points[block_id] = []
        #     self.KT[block_id] = kt
        #     is_new_hyper_block = True

        is_new_hyper_block = True
        block_id = None
        if kt in self.KT.values():
            is_new_hyper_block = False
            block_id = list(self.KT.keys())[list(self.KT.values()).index(kt)]
        else:
            # avoid overlapping between hyper-blocks
            hyper_k = [item[k] for item in self.KT.values() if len(item) > 1
                       for k in range(len(item))]
            for k in kt:
                if k in hyper_k:
                    is_new_hyper_block = False

            if is_new_hyper_block:
                block_id = max(self.points.keys()) + 1
                self.points[block_id] = []
                self.KT[block_id] = kt

        return block_id, is_new_hyper_block

    def get_num_blocks(self):
        return len(self.KT)


class LinearizationCuts:
    """This class computes and stores the linearization cuts which are used
    for OA solver

    :param block_model: Block model
    :type block_model: BlockModel
    :param cuts: List of linearization cuts
    :type cuts: dict
    """

    def __init__(self, block_model):
        """Constructor method"""
        self.block_model = block_model
        self.cuts = {k: [] for k in range(self.block_model.num_blocks)}

    def add_linearization_cuts(self, y, eps, x=None, block_id=None):
        """This method decides for which cases to compute linearization cuts.
        The cuts are computed with formula :math:`g(y) + \\nabla g(y)^T(x-y)
        \\leq 0`, where :math:`y` is a linearization point.

        Depending on the input values the cuts are added in the following cases:

        * if ``x`` is ``None``, then the cuts are added to active constraint \
        at point y.
        * if ``x`` is not ``None``, then the cuts are added only for \
        constraint which are violated at point x and are  active at point y

        * if ``block_id`` is ``None``, then linearization cuts are added to \
        the all blocks

        :param y: Linearization point
        :type y: BlockVector or ndarray
        :param eps: Accuracy for checking if the constraint is active
        :type eps: float
        :param x: point of OA solution
        :type x: BlockVector or ndarray or None
        :param block_id: Block identifier
        :type block_id: int or None
        :return: Number of new added cuts
        :rtype: int
        """
        # linearization cuts at point y are the following: g(y) +
        # grad g(y)*(x-y) <= 0
        number_of_cuts = [0] * self.block_model.num_blocks
        if x is None:
            if block_id is None:
                for k, sub_model in enumerate(self.block_model.sub_models):
                    for j, nonlin_con in enumerate(sub_model.nonlin_constr):
                        viol, val = nonlin_con.eval(y.get_block(k))
                        if abs(val) < eps:
                            number_of_cuts[k] += \
                                self.compute_and_add_linearization_cut(
                                    k, j, y.get_block(k))
            else:
                for j, nonlin_con in enumerate(
                        self.block_model.sub_models[block_id].nonlin_constr):
                    viol, val = nonlin_con.eval(y)
                    if abs(val) < eps:
                        number_of_cuts[block_id] += \
                            self.compute_and_add_linearization_cut(block_id,
                                                                   j, y)
        else:
            if block_id is None:
                for k, sub_model in enumerate(self.block_model.sub_models):
                    for j, nonlin_con in enumerate(sub_model.nonlin_constr):
                        viol, val = nonlin_con.eval(x.get_block(k))
                        if viol > 0:
                            viol, val = nonlin_con.eval(y.get_block(k))
                            if abs(val) < eps:
                                number_of_cuts[k] += \
                                    self.compute_and_add_linearization_cut(
                                        k, j, y.get_block(k))
            else:
                for j, nonlin_con in enumerate(
                        self.block_model.sub_models[block_id].nonlin_constr):
                    viol, val = nonlin_con.eval(x)
                    if viol > 0:
                        viol, val = nonlin_con.eval(y)
                        if abs(val) < eps:
                            number_of_cuts[block_id] += \
                                self.compute_and_add_linearization_cut(
                                    block_id, j, y)

        return number_of_cuts

    def compute_and_add_linearization_cut(self, block_id, j, y):
        """Method which computes the linearization cut for nonlinear constraint
        of the k-th block regarding a reference point y

        :param block_id: Block identifier
        :type block_id: int
        :param j: Nonlinear constraint index
        :type j: int
        :param y: Reference point
        :type y: ndarray
        :return: ``positive integer``, which correspond to the number of \
        added cuts, if all gradient values are ok (and the cut was possible \
        to compute), i.e. no :math:`\\infty` numbers, ``0`` - otherwise
        :rtype: int
        """
        constraint = self.block_model.sub_models[block_id].nonlin_constr[j]
        gradient = constraint.compute_gradient_at_point(y)

        # local linear constraint creation g(y) + grad g(y)*(x-y) <= 0
        # reformulated grad g(y)*x <= grad(y)*y - g(y), y is given point,
        # x is variable
        lhs = []
        rhs = 0

        for var_name in gradient.keys():
            i = constraint.orig_var_names_in_block.index(var_name)
            if not np.isnan(gradient[var_name]):
                grad = gradient[var_name]
                lhs.append((block_id, i, grad))
                rhs += y[i] * grad
            else:
                return 0

        # eval the function g at point y
        viol, val_g = constraint.eval(y)
        rhs -= val_g

        if constraint.relation == '>=':
            self.cuts[block_id].append(
                LinearConstraint(lhs, ">=", rhs, self.block_model.block_sizes))
        else:
            self.cuts[block_id].append(
                LinearConstraint(lhs, "<=", rhs, self.block_model.block_sizes))

        return 1

    def num_cuts(self, block_id):
        """Get number of cuts

        :param block_id: Block identifier
        :type block_id: int
        :return: Number of the cuts
        :rtype: int
        """
        return len(self.cuts[block_id])

    def __getitem__(self, item):
        """Index operator

        :param item: Given index
        :type item: tuple
        :return: The cuts associated with the index
        :rtype: LinearConstraint
        """
        k, i = item
        return self.cuts[k][i]


class CompactCuts:
    """Class that stores valid compact linear cuts got after solving the
    subproblems. They are defined with :math:`a^Tw \\leq b`, where :math:`a,
    w \\in \\mathbb{R}^{m+1}, m` is the number of global linear constraints

    :param block_model: Block model
    :type block_model: BlockModel
    :param cuts: Cuts stored blockwise as a dictionary with list as values
    :type cuts: dict
    """

    def __init__(self, block_model):
        """Constructor method"""
        self.block_model = block_model
        self.cuts = {k: [] for k in range(self.block_model.num_blocks)}
        self.rhs = {k: [] for k in range(self.block_model.num_blocks)}

    def add(self, block_id, lhs, relation, rhs):
        """Add new compact linear cut

        :param block_id: Block identifier
        :type block_id: int
        :param lhs: Left hand side of the constraint
        :type lhs: ndarray
        :param relation: Relation of the constraint
        :type relation: str
        :param rhs: Right hand side of the constraint
        :type rhs: float
        """
        self.cuts[block_id].append((copy.deepcopy(lhs), relation))
        self.rhs[block_id].append(rhs)

    def __getitem__(self, key):
        """Index operator

        :param key: Given index as tuple: (block_id, index)
        :type key: tuple
        :return: Cut associated with index
        :rtype: tuple
        """
        block_id, i = key
        (lhs, relation) = self.cuts[block_id][i]
        rhs = self.rhs[block_id][i]
        value = (lhs, relation, rhs)
        return value

    def __setitem__(self, key, value):
        """Index operator

        :param item: Given index as tuple: (block_id, index)
        :type item: tuple
        :param value: Left hand side, relation, right hand side
        :type value: tuple
        :return: Cut associated with index
        :rtype: tuple
        """
        block_id, i = key
        (lhs, relation, rhs) = value
        self.cuts[block_id][i] = (lhs, relation)
        self.rhs[block_id][i] = rhs

    def get_length(self):
        """ Get number of the cuts for each block

        :return: List of the cuts number blockwise
        :rtype: list
        """
        return [len(self.cuts[k]) for k in range(self.block_model.num_blocks)]
