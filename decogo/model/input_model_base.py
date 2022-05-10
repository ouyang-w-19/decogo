"""Implement base class of general input model"""

from abc import ABC, abstractmethod
from numpy import ndarray
import numpy as np
from decogo.model.constraints import LinearConstraint
from decogo.solver.results import Results
from decogo.problem.decomposed_problem import DecomposedProblem


class InputModelBase(ABC):
    """ Base class which stores data of the input model and
    solver of sub-problems and original problem (primal heuristics).

    :param sub_problems: list of SubProblems blockwise
    :type sub_problems: list
    :param original_problem: container of original problem
    :type original_problem: subclass of OriginalProblemBase
    :param cuts: container of linear constraints
    :type cuts: CutPoolCG
    :param sub_models: list of containers for variables from a single \
    block and local nonlinear constraints blockwise
    :type sub_models: list
    """
    def __init__(self, sub_problems, original_problem, cuts, sub_models):
        super().__init__()
        self.sub_problems = sub_problems
        self.original_problem = original_problem
        self.cuts = cuts
        self.sub_models = sub_models

    @abstractmethod
    def _construct_cut_pool(self):
        """ Base method for generating the parameters of cut_pool

        :return: block_sizes, blocks, obj, global_cuts, local_cuts
        :rtype: tuple
        """


class OriginalProblemBase(ABC):
    """ container class for original_problem with user-defined solver
     """

    def __init__(self):
        """Constructor method"""
        super().__init__()

    @abstractmethod
    def local_solve(self, start_point, result, problem, iter=None):
        """ Method for solving original problem
        non-optimal/heuristically/locally

        :param start_point: Starting point for the solver, defaults to ``None``
        :type start_point: ndarray
        :param result: stores and makes some manipulations with the CG results
        :type result: Results
        :param problem: stores all problem objects
        :type problem: DecomposedProblem
        :param iter: index of iterations in main algorithm
        :type iter: int
        """
        pass

    @abstractmethod
    def local_solve_fast(self, start_point, result, problem, iter=None):
        """ Method for fast solving original problem
        non-optimal/heuristically/locally

        :param start_point: Starting point for the solver, defaults to ``None``
        :type start_point: ndarray
        :param result: stores and makes some manipulations with the CG results
        :type result: Results
        :param problem: stores all problem objects
        :type problem: DecomposedProblem
        :param iter: index of iterations in main algorithm
        :type iter: int
        """
        pass


class SubModelBase(ABC):
    """Abstract base class which stores the variables from the single
    block and local nonlinear constraints.

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
    :param nonlin_constr: List of local nonlinear constraints
    :type nonlin_constr: list
    """

    def __init__(self, vars_in_block, block_id):
        """Constructor method"""

        super().__init__()

        # stores original names of the variables in the block
        self.vars_in_block = vars_in_block
        self.block_id = block_id
        self.variables = []
        self.nonlin_constr = []
        self.block_size = len(vars_in_block)
        self.integer = False
        self.linear = False


class SubProblemsBase(ABC):
    """ Base class for constructing a generalised model of sub-problems
    with user-defined solvers.

    :param block_id: Block identifier
    :type block_id: int
    """

    def __init__(self, block_id):
        """Constructor method"""
        super().__init__()
        self.block_id = block_id

    @abstractmethod
    def local_solve(self, result, direction, start_point=None, **kwargs):
        """ Method for solving sub-problem
        non-optimal/heuristically/locally

        :param result: stores and makes some manipulations with the CG results
        :type result: Results
        :param direction: Given vector
        :type direction: ndarray
        :param start_point: Starting point for the solver, defaults to ``None``
        :type start_point: ndarray or None
        :return: Solution point (ndarray), primal bound, dual bound,\
        flag if the primal bound is feasible
        :rtype: tuple
        """
        pass

    @abstractmethod
    def global_solve(self, result, direction, start_point=None, **kwargs):
        """ Method for solving
        sub-problem globally/near-optimal or calling an exact solver

        :param result: stores and makes some manipulations with the CG results
        :type result: Results
        :param direction: Given vector
        :type direction: ndarray
        :param start_point: Starting point for the solver, defaults to ``None``
        :type start_point: ndaray or None
        :return: Solution point (ndarray), primal bound, dual bound,\
        flag if the primal bound is feasible
        :rtype: tuple
        """
        pass


class CutPoolCG:
    """A class for containing linear constraints.

    This class contains both local and global linear constraints, obj function.

    :param block_sizes: Number of variables in block
    :type block_sizes: list
    :param blocks: List of original variable names blockwise
    :type blocks: list
    :param obj: Objective function
    :type obj: ObjectiveFunction
    :param global_cuts: List of global constraints
    :type global_cuts: list
    :param local_cuts: Stores the list of local cuts blockwise
    :type local_cuts: dict
    """

    def __init__(self, block_sizes=[], blocks=[], obj=None,
                 global_cuts=[], local_cuts={}):
        """Constructor method
        """
        self.block_sizes = block_sizes
        self.blocks = blocks
        self.obj = obj
        self.global_cuts = global_cuts
        self.local_cuts = local_cuts

    def add_lin_local_constr(self, coeff, relation, b, block_sizes):
        """Adds linear local constraint

        :param coeff: Coefficients of left hand side
        :type coeff: list
        :param relation: Constraint relation
        :type relation: str
        :param b: Right hand side of the constraint
        :type b: float
        :param block_sizes: Number of variables blockwise
        :type block_sizes: list
        """
        lin_con = LinearConstraint(coeff, relation, b, block_sizes)
        self.local_cuts[lin_con.block_id].append(lin_con)

    @property
    def num_of_cuts(self):
        """Gets total number of all linear constraints

        :return: Number of all linear constraint
        :rtype: int
        """
        num_cuts = len(self.global_cuts)
        for k in self.local_cuts.keys():
            num_cuts += len(self.local_cuts[k])

        return num_cuts

    @property
    def num_blocks(self):
        """Gets total number of blocks

        :return: Number of blocks
        :rtype: int
        """
        return len(self.block_sizes)

    @property
    def num_of_global_cuts(self):
        """Gets the number of linear global constraints

        :return: Number of global constraints only
        :rtype: int
        """
        return len(self.global_cuts)

    @property
    def num_of_local_cuts(self):
        """Gets the number of linear local constraints blockwise

        :return: Number of local constraints blockwise
        :rtype: int
        """
        return [len(self.local_cuts[k]) for k in range(len(self.block_sizes))]

    def evaluate_violation_global_constraints(self, point):
        """Evaluates violation of all global constraints

        :param point: Given point to evaluate
        :type point: BlockVector
        :return: Violation vector, which corresponds to violation of each \
        global constraint
        :rtype: ndarray
        """
        violation = np.zeros(shape=self.num_of_global_cuts)

        for i, cut in enumerate(self.global_cuts):
            viol = cut.eval(point)
            violation[i] = viol

        return violation

