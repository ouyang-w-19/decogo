"""Stores the results obtained by the solver"""

import logging
import time

logger = logging.getLogger('decogo')


class Results:
    """Class which stores and makes some manipulations with the results.
    The results are: primal/dual bound, primal solution point, timings, gap"""

    def __init__(self):
        """Constructor method"""

        self.strategy = None  # solver strategy
        self.sense = None  # sense of the original problem, i.e. min or max

        # general timing info
        self.start_clock_time = 0  # stores time of CPU at start of the solution process
        self.total_time = 0  # total time spent for running the solver
        self.decomp_time = 0  # time spent for decomposition
        self.containers_time = 0  # time spent for containers creation

        # region OA summary info
        self.sub_problem_time = 0  # time spent for solving sub problems
        self.init_time = 0  # time spent for oa_start
        self.main_alg_time = 0  # time spent for oa main algorithm

        self.num_iter = 0  # number of iterations
        self.primal_bound = float('inf')  # primal bound
        self.primal_sol_point = None  # solution to primal bound of optimal value
        self.dual_bound = float('-inf')  # dual bound
        # endregion

        # region DIOR summary info
        self.main_iterations = 0  # number of main iterations
        self.optimal_subproblems = True  # indicates if all subproblems were solved to optimality
        self.num_cg_iterations = 0  # number of CG iterations
        self.cg_num_minlp_problems = 0  # number of MINLP subproblems during CG
        self.cg_num_unfixed_nlp_problems = 0  # number of unfixed NLP subproblems during CG
        self.cg_num_fixed_nlp_problems = 0  # number of fixed NLP subproblems during CG
        self.cg_relaxation = float('inf')  # objective value of CG relaxation
        self.num_outer_iterations = 0  # number inner outer MIP iterations
        self.compact_oa_obj_val = float('-inf')  # objective value of compact OA
        self.compact_ia_obj_val = float('-inf')  # objective value of compact MIP IA
        self.num_of_columns_after_cg = 0  # number of columns after CG
        self.sub_problem_number_after_cg = 0  # number of solved subproblems after CG
        self.total_number_columns = 0  # total number of columns
        self.total_sub_problem_number = 0  # total number of solved subproblems
        self.c_tilde_y = float('inf')  # objective value in the NLP projected point
        self.total_number_columns_blockwise = {}  # total number of columns
        self.current_used_time = float('inf')  # used time during the running
        # endregion

    def set_new_primal_bound(self, primal_bound, point):
        """Sets new primal bound and primal point.

        :param primal_bound: Primal bound
        :type primal_bound: float
        :param point: Point which corresponds to the primal bound
        :type point: BlockVector
        """
        improved = False
        if primal_bound < self.primal_bound:
            improved = True
            self.primal_bound = primal_bound
            self.primal_sol_point = point

        return improved

    def get_gap(self, primal_bound, dual_bound):
        """Computes the gap in percentage between primal and dual bound

        :param primal_bound: Primal bound
        :type primal_bound: float
        :param dual_bound: Dual bound
        :type dual_bound: float
        :return: Gap
        :rtype: float
        """
        diff = abs(dual_bound - primal_bound)
        return round(
            100 * diff / (max(abs(primal_bound), abs(dual_bound)) + 1e-5),
            10)  # or min?

    def print_results(self):
        """Prints summary of results at the end of the logging process
        depending on the strategy"""
        self.calculate_total_time()
        self.print_decomp_time_and_total_time()

        if self.strategy == 'OA':
            self.print_oa_stats()
        elif self.strategy == 'CG':
            self.print_col_gen_stats()
        elif self.strategy == 'ADAPTCG':
            self.print_col_gen_stats()
        elif self.strategy == 'DynCG':
            self.print_col_gen_stats()

    def print_decomp_time_and_total_time(self):
        """Prints total time and decomposition time"""
        logger.info('\n{0: <50}{1: <30}'.format('Total time:', self.total_time))
        logger.info('\n{0: <50}{1: <30}'.format('Reformulation time:',
                                                self.decomp_time + self.containers_time))

        logger.info(
            '{0: <50}{1: <30}'.format('Decomposition time:', self.decomp_time))

        logger.info(
            '{0: <50}{1: <30}'.format('Containers time:', self.containers_time))

    def print_oa_stats(self):
        """Prints OA stats"""
        logger.info(
            '\n{0: <50}{1: <30}'.format('Number of iterations:', self.num_iter))

        logger.info('{0: <50}{1: <30}'.format('Dual bound:',
                                              self.sense * self.dual_bound))

        logger.info(
            '{0: <50}{1: <30}'.format('Primal bound:',
                                      round(self.sense * self.primal_bound, 10)))

        logger.info('{0: <50}{1: <30}'.format('Gap:',
                                              self.get_gap(self.primal_bound,
                                                           self.dual_bound)))

        logger.info('\n{0: <50}{1: <30}'.format('Oa start time:',
                                                self.init_time))

        logger.info('{0: <50}{1: <30}'.format('Oa main algorithm time:',
                                              self.main_alg_time))

        logger.info('{0: <50}{1: <30}'.format('Algorithm time:',
                                              self.init_time + self.main_alg_time))

        logger.info('{0: <50}{1: <30}'.format('Sub problems time:',
                                              self.sub_problem_time))

    def print_col_gen_stats(self):
        """Print Column Generation stats"""
        logger.info(
            '\n{0: <50}{1: <30}'.format('Primal bound:',
                                        round(self.sense * self.primal_bound,
                                              10)))

        logger.info('\n{0: <50}{1: <30}'.format('Main iterations:', self.main_iterations))
        logger.info('{0: <50}{1: <30}'.format('Number of CG iterations:',
                                                self.num_cg_iterations))

        logger.info('{0: <50}{1: <30}'.format('CG relaxation obj. value:',
                                              self.sense * self.cg_relaxation))

        logger.info('{0: <50}{1: <30}'.format('Number of MINLP subproblems:',
                                              self.cg_num_minlp_problems))

        logger.info(
            '{0: <50}{1: <30}'.format('Number of unfixed NLP subproblems:',
                                      self.cg_num_unfixed_nlp_problems))

        logger.info(
            '{0: <50}{1: <30}'.format('Number of fixed NLP subproblems:',
                                      self.cg_num_fixed_nlp_problems))

        logger.info(
            '{0: <50}{1: <30}'.format('Number of solved sub-problems after CG:',
                                      self.sub_problem_number_after_cg))

        logger.info('{0: <50}{1: <30}'.format('Number of columns after CG:',
                                              self.num_of_columns_after_cg))
        logger.info(
            '{0: <50}{1: <30}'.format('CG Gap (CG relaxation and primal bound):',
                                      self.get_gap(self.primal_bound,
                                                   self.cg_relaxation)))

        logger.info('{0: <50}{1: <30}'.format('Total number of columns:',
                                              self.total_number_columns))

    def add_sub_problem_time(self, time):
        """Accumulates sub-problem time

        :param time: Time to add
        :type time: float
        """
        self.sub_problem_time += time

    def calculate_total_time(self):
        """Calculates total time"""
        self.total_time = time.time() - self.start_clock_time
