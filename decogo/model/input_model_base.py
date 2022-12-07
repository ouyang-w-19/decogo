"""Implement base class of general input model"""

from abc import ABC, abstractmethod
from numpy import ndarray
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
    :type cuts: decogo.model.constraints.CutPool
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
    def local_solve(self, result, direction, start_point=None):
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
    def global_solve(self, result, direction, start_point=None):
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


