"""Main module for storing model data."""

import logging

import numpy as np
import scipy.sparse as sp
from pyomo.environ import ConcreteModel

from decogo.model.constraints import PyomoCutPool
from decogo.pyomo_input_model.input_model import PyomoSubModel
from decogo.util.block_vector import BlockVector

logger = logging.getLogger('decogo')


class BlockModel:
    """This class stores sub-models and cut pool.

    :param blocks: List (block-wise) of original string names of variables
    :type blocks: list
    :param sense: Indicates the the problem is minimization (1) or  \
    maximization (-1)
    :type sense: int
    :param cuts: Container which stores all linear constraints \
    (global and local) and objective function
    :type cuts: PyomoCutPool
    :param sub_models: List of sub-models
    :type sub_models: list
    """

    def __init__(self, blocks, sense, cuts, sub_models):
        """Constructor method"""

        self.blocks = blocks  # string names for the variables in the block
        self.num_blocks = len(blocks)  # Number of blocks (sub-models)
        self.block_sizes = [len(item) for item in blocks]  # List of variable
        # numbers per sub-model
        self.sense = sense
        self.cuts = cuts
        self.sub_models = sub_models
        self.non_zero_resources = self.get_non_zero_resources()  # Stores the
        # indices (block-wise) of nonzero left-hand side of the coupling
        # constraints
        self.print_model_stats()

    def get_non_zero_resources(self):
        """Determines the indices of nonzero resources blockwise, i.e.
        checks whether left-hand side of the coupling constraints is nonzero,
        i.e. :math:`A_k \\neq 0`

        :return: indices of nonzero resources of nonzero
        :rtype: dict
        """
        indices = {}
        for k in range(self.num_blocks):
            indices[k] = set()

            # check if c_k is nonzero
            c_k = self.cuts.obj.c.get_block(k)
            if c_k is not None:
                indices[k].add(0)

            for i, cut in enumerate(self.cuts.global_cuts):
                a_k = cut.lhs.get_block(k)
                if a_k is not None:
                    indices[k].add(i + 1)  # shifted by 1 because of objective

        return indices

    def eval_viol_lin_global_constraints(self, point):
        """Evaluates the violation of global linear constraints, see
        :meth:`model.constraints.PyomoCutPool.evaluate_violation_global_constraints`
        """
        return self.cuts.evaluate_violation_global_constraints(point)

    def trans_into_orig_space(self, block_id, direction):
        """Computes :math:`d_k^TA_k, d_k \\in \\mathbb{R}^{m+1}`, where
        :math:`m` is the number of global constraints

        :param block_id: Block identifier
        :type block_id: int
        :param direction: Array with dimension :math:`m+1`, where :math:`m` is \
        the number of global constraints
        :type direction: list or ndarray
        :return: An array with the dimension of :math:`n_k`, where \
        :math:`n_k` is size of the k-th block
        :rtype: ndarray
        """

        block_size = self.block_sizes[block_id]

        # add c_k to the matrix
        A_k = self.cuts.obj.c.get_block(block_id)

        # first row can be all zeros row
        if A_k is None:
            A_k = sp.csr_matrix([0 for i in range(block_size)],
                                shape=(1, block_size))

        for m in range(self.cuts.num_of_global_cuts):
            row_k = self.cuts.global_cuts[m].lhs.get_block(block_id)

            if row_k is None:
                # the row is completely zero, that's why it is None
                row_k = sp.csr_matrix([0 for i in range(block_size)],
                                      shape=(1, block_size))
                A_k = sp.vstack((A_k, row_k), format='csr')
            else:
                # the row is not all zero
                # merge the rows a_jk into matrix A_k
                A_k = sp.vstack((A_k, row_k), format='csr')

        # multiply A_k^T*direction
        result = A_k.transpose().dot(direction)

        return result

    def trans_into_im_space(self, block_id, point):
        """Compute :math:`w=A_kx_k`, where :math:`x_k \\in \\mathbb{R}^{n_k}`

        :param block_id: Block identifier
        :type block_id: int
        :param point: Point in the original space
        :type point: ndarray
        :return: Point w in the image space, i.e. \
        :math:`w \\in \\mathbb{R}^{m+1}`
        :rtype: ndarray
        """

        block_size = self.block_sizes[block_id]

        # merge the rows c_k and a_jk into matrix A_k
        A_k = self.cuts.obj.c.get_block(block_id)

        # first row can be all zeros row
        if A_k is None:
            A_k = sp.csr_matrix([0] * block_size, shape=(1, block_size))

        for j in range(self.cuts.num_of_global_cuts):
            row_k = self.cuts.global_cuts[j].lhs.get_block(block_id)
            if row_k is None:
                # the row is completely zero, that's why it is None
                row_k = sp.csr_matrix([0] * block_size, shape=(1, block_size))
                A_k = sp.vstack((A_k, row_k), format='csr')
            else:
                # the row is not all zero
                # merge the rows a_jk into matrix A_k
                A_k = sp.vstack((A_k, row_k), format='csr')

        # transform
        w = A_k.dot(point)

        return w

    def num_nonzero_m_k(self, block_id):
        """Compute :math:`w=A_kx_k`, where :math:`x_k \\in \\mathbb{R}^{n_k}`

        :param block_id: Block identifier
        :type block_id: int
        :param point: Point in the original space
        :type point: ndarray
        :return: Point w in the image space, i.e. \
        :math:`w \\in \\mathbb{R}^{m+1}`
        :rtype: ndarray
        """

        block_size = self.block_sizes[block_id]

        # merge the rows c_k and a_jk into matrix A_k
        A_k = self.cuts.obj.c.get_block(block_id)

        # first row can be all zeros row
        if A_k is None:
            A_k = sp.csr_matrix([0] * block_size, shape=(1, block_size))

        for j in range(self.cuts.num_of_global_cuts):
            row_k = self.cuts.global_cuts[j].lhs.get_block(block_id)
            if row_k is None:
                # the row is completely zero, that's why it is None
                row_k = sp.csr_matrix([0] * block_size, shape=(1, block_size))
                A_k = sp.vstack((A_k, row_k), format='csr')
            else:
                # the row is not all zero
                # merge the rows a_jk into matrix A_k
                A_k = sp.vstack((A_k, row_k), format='csr')

        return np.count_nonzero(A_k.data)

    def print_model_stats(self):
        """Computes and prints the statistics of the new block model, i.e.
        mean, min, max of the new block sizes
        """
        logger.info('Block separable reformulation:')
        logger.info('{0: <50}{1: <30}'.format('Number of blocks:',
                                              len(self.block_sizes)))

        n_nonlin_blocks = sum(1 for sub_model in self.sub_models if
                              len(sub_model.nonlin_constr) > 0)
        logger.info('{0: <50}{1: <30}'.format('Number of nonlinear blocks:',
                                              n_nonlin_blocks))

        logger.info('{0: <50}{1: <30}'.format('Min size of blocks:',
                                              min(self.block_sizes)))

        max_block_size = max(self.block_sizes[k] for k in range(self.num_blocks)
                             if len(self.sub_models[k].nonlin_constr) > 0)
        logger.info('{0: <50}{1: <30}'.format(
            'Max size of blocks (without linear blocks):', max_block_size))

        logger.info('{0: <50}{1: <30}'.format(
            'Max size of blocks (including linear blocks):',
            max(self.block_sizes)))

        logger.info(
            '{0: <50}{1: <30}'.format('Number of vars:', sum(self.block_sizes)))

        logger.info('{0: <50}{1: <30}'.format('Number of global constraints:',
                                              self.cuts.num_of_global_cuts))

        non_zero_res = ','.join((str(len(self.non_zero_resources[k])) for k in
                                 range(self.num_blocks)))
        logger.info(
            '{0: <50}{1: <30}'.format('Number of nonzero resources per block:',
                                      non_zero_res))

        # equalities/inequalities count of global constraints
        equalities = 0
        inequalities = 0
        for cut in self.cuts.global_cuts:
            if cut.relation == '=':
                equalities += 1
            else:
                inequalities += 1
        logger.info('{0: <50}{1: <30}'.format(
            'Number of equal./inequal. of global constraints:',
            '{0}/{1}'.format(equalities, inequalities)))

        # copy constraints
        # logger.info('{0: <50}{1: <30}'.format(
        #     'Total number of copy constraints:',
        #     '{0}'.format(len(self.cuts.copy_constraints))))
        # for [k1, k2] in self.cuts.blocks_copy_constraints.keys():
        #     logger.info('{0: <50}{1: <30}'
        #                 .format('Number of copy constraints (block {0} <-> '
        #                         'block {1}):'
        #                         .format(k1, k2),
        #                         '{0}'
        #                         .format(self.cuts
        #                                 .blocks_copy_constraints[k1, k2])))

        # testing lin_con_hyper_block
        # self.problem.block_model.lin_con_hyper_block([0, 1, 2, 3])

    def global_con_hyper_block(self, kt):
        # find indices of global constraints that need to be active
        # for hyper block
        global_con_indices = []
        if len(kt) > 1:
            for m in range(self.cuts.num_of_global_cuts):
                if set(self.cuts.global_cuts[m].lhs.blocks).\
                        issubset(set(kt)):
                    global_con_indices.append(m)

        return global_con_indices


class PyomoBlockModel(BlockModel):
    """This class takes Pyomo model and stores sub-models and cut pool derived
    from the Pyomo model.

    :param model: Input Pyomo model
    :type model: ConcreteModel
    :param blocks: List (block-wise) of original string names of variables
    :type blocks: list
    :param sense: Indicates the the problem is minimization (1) or  \
    maximization (-1)
    :type sense: int
    """

    def __init__(self, model, blocks, sense):
        """Constructor method"""

        self.model = model
        cuts = PyomoCutPool(model, blocks)
        num_blocks = len(blocks)
        sub_models = [PyomoSubModel(model, blocks[block_id], block_id) for
                      block_id in range(num_blocks)]

        super().__init__(blocks, sense, cuts, sub_models)

    def compute_gradients(self):
        """Computes gradients for nonlinear constraints"""
        for sub_model in self.sub_models:
            sub_model.compute_gradients()

    def update_var_lower_bound(self, new_lower_bound, index):
        """Updates the lower bound of the variable with the given index"""
        k, i = index
        self.sub_models[k].variables[i].lower_bound = new_lower_bound

    def update_var_upper_bound(self, new_upper_bound, index):
        """Updates the upper bound of the variable with the given index"""
        k, i = index
        self.sub_models[k].variables[i].upper_bound = new_upper_bound

    def max_violation_nonlinear_constraints(self, x):
        """Determines if the solution is feasible regarding the nonlinear
        constraints by computing the maximum violation

        :param x: Given point
        :type x: BlockVector
        :return: Maximum violation and index of most violated constraint as \
        tuple (viol, block_id, index)
        :rtype: tuple
        """
        violation = 0
        idx = None

        for k in range(self.num_blocks):
            for i, constr in enumerate(self.sub_models[k].nonlin_constr):
                viol, val = constr.eval(x.get_block(k))
                if viol > violation:
                    violation = viol
                    idx = k, i

        return violation, idx

    def round(self, block_id, point):
        """Rounds point to the closest integer

        :param block_id: Block identifier
        :type block_id: int
        :param point: Given point
        :type point: ndarray
        :return: New rounded point
        :rtype: ndarray
        """
        return self.sub_models[block_id].round(point)

