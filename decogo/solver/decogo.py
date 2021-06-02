"""Main module for running the solution process"""

import logging
import os
import time
from multiprocessing import Process, Pipe
from threading import Thread

import psutil
import pyutilib.subprocess.GlobalData
from pyomo.environ import Objective, Constraint, Set, Param, Block
from pyomo.network import Port, Arc

from decogo.model.block_model import PyomoBlockModel, BlockModel
from decogo.model.model_decomposer import PyomoModelDecomposer
from decogo.pyomo_problem.pyomo_decomposed_problem import PyomoDecomposedProblem
from decogo.problem.decomposed_problem import \
    DecomposedProblem
from decogo.solver.colgen import ColGen
from decogo.solver.refactory_colgen import RefactoryColGen
from decogo.solver.oa import OaSolver
from decogo.solver.results import Results
from decogo.solver.settings import Settings

pyutilib.subprocess.GlobalData.DEFINE_SIGNAL_HANDLERS_DEFAULT = False

logger = logging.getLogger('decogo')


class DecogoSolver:
    """Class which starts the solution process
    """

    @staticmethod
    def _remove_unpicklable_objects_pyomo_model(model):
        """Removes unpicklable objects from Pyomo model object. This is because
        multiprocessing is based on serialization and some objects cannot be
        serialized (pickled).
        This method does the following:

        * removes objects Port and Arcs, since they contain weakref objects

        * sets to None the 'rule' property for Constraint, Objective and Param, \
        since it might contain lambda function

        * sets to None property 'initialize' and '_init_values._init' for Set, \
        since it might contain lambda function

        :param model: Pyomo model
        :type model: ConcreteModel
        """
        try:
            for block_obj in model.block_data_objects():
                for port in block_obj.component_objects(Port):
                    block_obj.del_component(port)
                for arc in block_obj.component_objects(Arc):
                    block_obj.del_component(arc)

            for obj in model.component_objects(
                    [Objective, Constraint, Param, Block]):
                obj._rule = None
                obj.rule = None

            # if here some exceptions occur, then check whether attributes still
            # exist
            for obj in model.component_objects([Set]):
                obj._init_values._init = None
                obj.initialize = None
        except AttributeError:
            pass

    def optimize(self, input_model, file_name=None):
        """Main driver method which starts the process of solving

        :param input_model: Pyomo model
        :type input_model: ConcreteModel
        :param file_name: Name of the file where the logging information written
        :type file_name: str or None
        """

        self._remove_unpicklable_objects_pyomo_model(input_model)

        # sharing pyomo model to the process using Pipe or Queue is a bad idea,
        # since it is very slow. This could help return the solution in a
        # nice way (with pyomo model).
        # The only possibility is to transform the lifted solution point into
        # original formulation and assign this values to original pyomo model.
        # This must be much faster, since we need to return relatively simple
        # object after finishing the process.
        # For that we could use Pipe or Queue
        p = DecogoProcess(input_model, file_name)

        # get maximum time for running the solver
        max_time = p.get_max_time()

        p.start()

        # set max time for process to run
        p.join(max_time)

        if p.is_alive():
            p.close()

        p.join()

        # remove files that are left by pyomo after interrupting the process
        directory_name = os.getcwd()
        files = os.listdir(directory_name)
        for item in files:
            if item.endswith('.nl') or item.endswith('.sol') or \
                    item.endswith('.log') or item.endswith('.lp'):
                os.remove((os.path.join(directory_name, item)))


class DecogoProcess(Process):
    """Class which is responsible for solver process. The main idea of this
    class is reliable way to set maximum executation time of the whole solver.

    :param input_model: Pyomo model
    :type input_model: ConcreteModel
    :param file_name: Name of the file where the log info should be written
    :type file_name: str or None
    :param solver: Solver manager
    :type solver: DecogoSolverManager
    :param solver_thread: solver single thread which runs the solver
    :type solver_thread: Thread
    """
    def __init__(self, input_model, file_name=None):
        """Constructor method"""
        super().__init__()
        self.input_model = input_model
        self.file_name = file_name

        self.solver = DecogoSolverManager()
        self.solver_thread = None
        self._parent_conn, self._child_conn = Pipe()

    def run(self):
        """Method for running the solver"""
        self.solver_thread = Thread(target=self.solver.solve,
                                    args=(self.input_model, self.file_name))
        self.solver_thread.daemon = True
        self.solver_thread.start()

        while True:
            if self._child_conn.poll():
                logger.info('\nEXIT: timeout')
                self.solver.results.print_results()
                break
            if self.solver_thread.is_alive():
                self.solver_thread.join(0.5)  # heartbeat for checking
            else:
                break

        self._exit()

    def _exit(self):
        """Finishes the process and all sub-processes and exits"""

        # terminate all child processes. The purpose of this to stop processes
        # of other solvers
        # (SCIP, bonmin etc)
        current_process = psutil.Process()
        for child in current_process.children(recursive=True):
            child.terminate()

        self._child_conn.close()

    def close(self):
        """Closes process"""
        # The actual value we are sending to child does not matter because
        # the while loop in `run` will break upon receipt of any object.
        self._parent_conn.send('STOP')

    def get_max_time(self):
        """Gets max time for running the solver process"""
        return self.solver.settings.maxtime


class DecogoSolverManager:
    """Class which manages algorithms of the solver. It performs the
    decomposition, creates the settings, calls the algorithms and stores
    the results

    :param decomposer: Instance of the class which performs the decomposition
    :type decomposer: PyomoModelDecomposer
    :param problem: Decomposed problem
    :type problem: PyomoDecomposedProblem or DecomposedProblem
    :param logger_handler: Logger instance
    :type logger_handler: DecogoLogger
    :param settings: Instance of solver settings
    :type settings: Settings
    :param results: Instance of solver results
    :type results: Results
    """

    def __init__(self):
        """Constructor method"""
        self.decomposer = None
        self.problem = None  # is created within automatic decomposition

        self.logger_handler = None
        self.settings = Settings()
        self.results = Results()
        os.remove('decogo.set')

    def solve(self, input_model, file_name=None):
        """Performs basic operations of the solver: decomposition,
        algorithm execution and showing the results

        :param input_model: Input Pyomo model
        :type input_model: ConcreteModel
        :param file_name: Name of the file where the logs should be stored
        :type file_name: str or None
        """
        self.logger_handler = DecogoLogger(self.settings.logger_level,
                                           file_name)

        self.results.start_clock_time = time.time()
        self.results.strategy = self.settings.strategy

        try:
            self._automatic_decomposition(
                input_model, user_defined_model=
                self.settings.user_defined_input_model)
            logger.info('-----------------------------------------------------')
            logger.info('Used time: {0}'.format(self.results.current_used_time))
            logger.info('-----------------------------------------------------')

            if self.settings.strategy == 'OA':
                solver = OaSolver(self.problem, self.settings, self.results)
            elif self.settings.strategy == 'CG':
                if self.settings.user_defined_input_model:
                    solver = RefactoryColGen(self.problem, self.settings,
                                             self.results)
                else:
                    solver = ColGen(self.problem, self.settings, self.results)
            solver.solve()  # it's ok, the solver strategy is always provided

        except Exception:
            logger.exception('\nEXIT: Some exception')
        finally:
            self.results.print_results()
            self.logger_handler.clean_up()

    def _automatic_decomposition(self, input_model, user_defined_model=False):
        """Peforms automatic decomposition of the input model

        :param input_model: Input Pyomo model
        :type input_model: ConcreteModel
        """
        if not user_defined_model:
            self.decomposer = PyomoModelDecomposer(input_model, self.settings)

            self.results.decomp_time = time.time()
            model, blocks, model_sense = self.decomposer.decompose()
            self.results.decomp_time = time.time() - self.results.decomp_time
            self.results.current_used_time = self.results.decomp_time
            self.results.sense = model_sense

            self.results.containers_time = time.time()
            block_model = PyomoBlockModel(model, blocks, model_sense)
            self.problem = PyomoDecomposedProblem(block_model,
                                                  strategy=
                                                  self.settings.strategy)
            self.results.containers_time = time.time() - \
                self.results.containers_time
            self.results.current_used_time += self.results.containers_time
        else:
            self.results.sense = input_model.sense
            block_model = BlockModel(input_model)
            self.problem = DecomposedProblem(block_model,
                                             input_model.sub_problems,
                                             input_model.original_problem)


class DecogoLogger:
    """Class which is responsible for the logging of the solver. It sets up
    the logs of the solver
    """

    def __init__(self, level, file_name=None):
        """Constructor method"""
        if level == 'debug':
            level = logging.DEBUG
        elif level == 'info':
            level = logging.INFO

        if file_name is None:
            self._set_up_into_console(level)
        else:
            self._set_up_into_file(file_name, level)

    def _set_up_into_file(self, file_name, level):
        """Sets up the logger into file

        :param file_name: Name of the file
        :type file_name: str
        :param level: logger level
        :type level: logging.DEBUG, logging.INFO etc
        """
        logger.setLevel(level)

        ch = logging.FileHandler(file_name, mode='w')
        ch.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(message)s')

        ch.setFormatter(formatter)
        logger.addHandler(ch)

    def _set_up_into_console(self, level):
        """Sets up the logger into console

        :param level: logger level
        :type level: logging.DEBUG, logging.INFO etc
        """

        logger.setLevel(level)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(message)s')

        ch.setFormatter(formatter)
        logger.addHandler(ch)

    def clean_up(self):
        """Cleans all logger handlers"""
        for i, handler in enumerate(logger.handlers):
            logger.handlers[i].close()
            logger.removeHandler(handler)
