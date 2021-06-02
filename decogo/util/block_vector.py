"""Implements sparse and dense block vector data structures"""

import copy
from collections import Sequence
from collections import defaultdict

import numpy as np
import math
from scipy.sparse import coo_matrix


class SparseBlockVector:
    """Class for storing the values in sparse format blockwise.
    It consists of k blocks. Each block uses the standard Python sparse
    matrix with dimension :math:`1 \\times n_k`, where :math:`n_k`
    is the block size

    :param vectors: Sparse matrices stored blockwise
    :type vectors: dict
    :param blocks_size: Size of the blocks
    :type blocks_size: list
    :param blocks: Block ids which contain nonzero values
    :type blocks: list
    """

    def __init__(self, values, blocks_size):
        """Constructor method

        :param values: List of tuples (block_id, index, value)
        :type values: list
        :param blocks_size: Number of variables per block
        :type blocks_size: list
        """
        self.vectors = {}
        self.blocks_size = blocks_size

        # dictionary: block -> data, col
        data, col = defaultdict(list), defaultdict(list)

        for (item_block, item_column, item_data) in values:
            data[item_block].append(item_data)
            col[item_block].append(item_column)

        for block_id in data.keys():
            row = [0] * len(col[block_id])
            column_size = blocks_size[block_id]
            self.vectors[block_id] = coo_matrix(
                (data[block_id], (row, col[block_id])),
                shape=(1, column_size)).tocsr()

        self.blocks = list(self.vectors.keys())

    def __getitem__(self, item):
        """Index operator

        :param item: Input index as tuple: (block_id, index)
        :type item: tuple
        :return: Value associated with the given index
        :rtype: float
        """
        block_id, column = item
        try:
            elem = self.vectors[block_id][0, column]
        except KeyError:
            elem = 0

        return elem

    def scalar_prod(self, x):
        """Scalar product computation (or dot product) computed blockwise,
        :math:`v=\\sum_{k \\in K}a_k^Tx_k`

        :param x: Input vector
        :type x: SparseBlockVector or BlockVector
        :return: Value for scalar product :math:`v`
        :rtype: float
        """
        val = 0
        for block_id in x.vectors.keys():
            try:
                val += self.vectors[block_id].dot(x.vectors[block_id])
            except KeyError:
                val += np.array([0.0])

        return val[0]

    def maxabs(self, block_id=None):
        """Finds maximum element by absolute value

        :param block_id: Block id where to look for the maximum value
        :type block_id: int, optional
        :return: Max element by absolute value
        :rtype: float or None
        """
        try:
            if block_id is not None:
                max_elem = abs(max(self.vectors[block_id].min(),
                               self.vectors[block_id].max(), key=abs))
            else:
                max_elem = float('-inf')
                for k in self.blocks:
                    elem = abs(max(self.vectors[k].min(), self.vectors[k].max(),
                               key=abs))
                    max_elem = max(elem, max_elem)
        except KeyError:
            max_elem = None

        return max_elem

    @property
    def num_blocks(self):
        """Return number of blocks

        :return: Return number of blocks
        :rtype: int
        """
        return len(self.blocks)

    def get_block(self, block_id):
        """Gets vector associated with the given block id

        :param block_id: Given block identifier
        :type block_id: int
        :return: Sparse vector (matrix)
        :rtype: coo_matrix or None
        """
        if block_id in self.vectors:
            return self.vectors[block_id]
        else:
            return None

    def get_block_size(self, k):
        """Get block size associated with the given block id

        :param k: Given block identifier
        :type k: int
        :return: Block size
        :rtype: int
        """
        return self.blocks_size[k]

    def get_norm(self):

        norm_value = 0
        for k in self.blocks:
            norm_value += sum(i**2 for i in self.vectors[k].data)
        norm_value = math.sqrt(norm_value)

        return norm_value


class BlockVector:
    """This class stores dense vector with the respect to blocks

    :param vectors: Dense vectors stored blockwise
    :type vectors: dict
    :param blocks_size: Size of the blocks
    :type blocks_size: list
    :param blocks: Block identifiers
    :type blocks: list
    """

    def __init__(self, blocks_size=None):
        """Constructor method"""
        self.vectors = {}
        self.blocks_size = blocks_size

        if blocks_size is not None:
            for block_id in range(len(blocks_size)):
                self.vectors[block_id] = np.zeros(shape=blocks_size[block_id],
                                                  dtype=float)

        self.blocks = list(self.vectors.keys())

    def __getitem__(self, item):
        """Index operator

        :param item: Input index in tuple (block_id, index)
        :type item: tuple
        :return: Value associated to index
        :rtype: float
        """
        block_id, index = item
        return self.vectors[block_id][index]

    def get_block(self, block_id):
        """Get vector associated to the blocks

        :param block_id: Block identifier
        :return: Vector
        :rtype: ndarray
        """
        return self.vectors[block_id]

    def set_block(self, block_id, array):
        """Sets vector associated to block

        :param block_id: Block identifier
        :type block_id: int
        :param array: Array to set
        :type array: ndarray
        """
        self.vectors[block_id] = array
        self.blocks = list(self.vectors.keys())

    def __setitem__(self, key, value):
        """Index operator

        :param key: Index as tuple: (block_id, index)
        :type key: tuple
        :param value: Value to set
        :type value: float
        """
        block_id, index = key
        self.vectors[block_id][index] = value

    def __str__(self):
        """String operator

        :return: Nicer way of string representation
        :rtype: str
        """
        val = \
            '\n'.join(np.array2string(self.vectors[key],
                                      formatter={'float': lambda x: "%.3f" % x})
                      for key in self.vectors.keys())
        return val

    @property
    def num_blocks(self):
        """Return number of blocks

        :return: Number of blocks
        :rtype: int
        """
        return len(self.vectors.keys())

    def __add__(self, other):
        """Operator +

        :param other: Other vector
        :type other: BlockVector
        :return: Sum of two vectors
        :rtype: BlockVector
        """
        res = copy.deepcopy(self)
        for k in range(self.num_blocks):
            for n in range(len(self.vectors[k])):
                res[k, n] = self[k, n] + other[k, n]
        return res

    def __sub__(self, other):
        """Operator -

        :param other: Other vector
        :type other: BlockVector
        :return: Difference of two vectors
        :rtype: BlockVector
        """
        res = copy.deepcopy(self)
        for k in range(self.num_blocks):
            for n in range(len(self.vectors[k])):
                res[k, n] = self[k, n] - other[k, n]
        return res

    def __eq__(self, other):
        """Operator ==, checks if two vectors are equal

        :param other: Other vector
        :type other: BlockVector
        :return: True or False
        :rtype: bool
        """
        equal = True
        for k in range(self.num_blocks):
            for n in range(len(self.vectors[k])):
                if abs(self[k, n] - other[k, n]) < 0.0001:
                    equal = True
                else:
                    return False
        return equal

    def __mul__(self, other):
        """Multiplication operator. Currently supports only scalar types for
        multiplication

        :param other: Scalar value
        :type other: float
        :return: Vector multiplied by scalar value
        :rtype: BlockVector
        :raise ValueError: If :attr:`other` is not a sequence
        """
        # supports only scalar types for multiplication
        # check if 'other' is scalar
        if isinstance(other, Sequence) is False:
            res = BlockVector(self.blocks_size)
            for k in range(self.num_blocks):
                res.vectors[k] = other * self.vectors[k]
            return res
        else:
            raise ValueError('Multiplication for sequences is not supported')

    def __truediv__(self, other):
        """True division operator. Currently supports only scalar types for
        division

        :param other: Scalar value
        :type other: float
        :return: Vector divided by scalar value
        :rtype: BlockVector
        :raise ValueError: If :attr:`other` is not a sequence
        """
        # supports only scalar types for division
        # check if 'other' is scalar
        if isinstance(other, Sequence) is False:
            res = BlockVector(self.blocks_size)
            for k in range(self.num_blocks):
                res.vectors[k] = self.vectors[k] / other
            return res
        else:
            raise ValueError('Division for sequences is not supported')

    def __abs__(self):
        """Absolute value operator

        :return: New vector with absolute values
        :rtype: BlockVector
        """
        res = copy.deepcopy(self)
        for k in range(self.num_blocks):
            res.set_block(k, np.abs(res.get_block(k)))
        return res


def infinity_norm(x):
    """Computes infinity norm, i.e.
    :math:`||x||_\\infty = \\max\\limits_{k \\in K, i \\in n_k}|x_{ki}|`

    :param x: Input vector
    :type x: BlockVector or SparseBlockVector
    :return: Value of infinity norm
    :rtype: float
    """
    res = 0
    for k in x.blocks:
        res = max(res, np.linalg.norm(x.get_block(k), ord=np.inf))
    return res
