"""Class which implements Column Generation"""

import copy
import logging
import math
import time
import operator

import numpy as np

from decogo.solver.settings import Settings
from decogo.util.block_vector import BlockVector

logger = logging.getLogger('decogo')


class DynBlockColGen:
    """Class which implements Dynamic Block and Column Generation algorithm

    :param problem: Decomposed problem class, which stores all input data
    :type problem: DecomposedProblem
    :param settings: Settings class
    :type settings: Settings
    :param result: Class which stores the results
    :type result: Results
    """

    def __init__(self, problem, settings, result):
        """Constructor method"""
        self.problem = problem
        self.result = result
        self.settings = settings

    def solve(self):
        """
        main method for the dynamic CG algorithm
        """

        check_w, duals = self.ia_init()

        # increase duals
        max_val = abs(max(duals, key=abs))
        duals = np.full(shape=self.problem.block_model.cuts.num_of_global_cuts,
                        fill_value=100*max_val)

        # select nonlinear atomic blocks
        t_set_atomic = [k for k in range(self.problem.block_model.num_blocks)]

        # generate columns for atomic blocks using fast column generation
        self.fw_column_generation(check_w=check_w, duals=duals,
                                  t_set=t_set_atomic)
        j = 0
        while True:
            j += 1
            tic = time.time()
            # solve extended inner master problem
            z, x_ia, w_check, slacks, duals, obj_value_ia, _, _ = \
                self.problem.master_problems.solve_ia(self.settings.lp_solver)
            max_slack_value = max(max(item) for item in slacks)
            sum_slack_values = sum(item[0] + item[1] for item in slacks)
            logger.info('{0: <15}{1: <30}{2: <30}'
                        '{3: <30}'.format('CG iter(atomic)', 'IA obj. value',
                                          'max slack value IA',
                                          'sum slack values IA'))

            logger.info('{0: <15}{1: <30}{2: <30}''{3: <30}'
                        .format(j, self.result.sense *
                                self.result.cg_relaxation,
                                max_slack_value, sum_slack_values))
            time_cg = round(time.time() - tic, 2)
            logger.info('Time used for init FastCG '
                        'in iter {0}: --{1}-- seconds'
                        .format(j, time_cg))
            self.result.current_used_time += time_cg
            logger.info('-----------------------------------------------------')
            logger.info('Elapsed time: --{0}-- seconds'
                        .format(round(self.result.current_used_time, 2)))
            logger.info('-----------------------------------------------------')

            # find solution performed always in the beginning
            if self.result.primal_bound == float('inf'):
                logger.info(
                    '-----------------------------------------------------')
                tic = time.time()
                self.find_solution_init(j)
                time_find_solution = round(time.time() - tic, 2)
                logger.info('Time used for init FindSol '
                            'in iter {0}: --{1}-- seconds'
                            .format(j, time_find_solution))
                self.result.current_used_time += time_find_solution
                logger.info(
                    '-----------------------------------------------------')
                logger.info('Elapsed time: --{0}-- seconds'
                            .format(round(self.result.current_used_time, 2)))
                logger.info(
                    '-----------------------------------------------------')

                if self.result.primal_bound < float('inf'):
                    logger.info('Found the first feasible solution')

                    logger.info('IA obj. val: {0}'.format(
                        self.result.cg_relaxation * self.result.sense))
                    logger.info('Elapsed time: {0}'.format(
                        self.result.current_used_time))

            if j == self.settings.max_iter_fast_cg_init:
                break

            if max_slack_value < 10e-5:
                self.result.cg_relaxation = obj_value_ia

            self.fw_column_generation(check_w=w_check, duals=duals,
                                      t_set=t_set_atomic)

        if self.settings.standard_cg:
            self.column_generation(duals=duals, x_ia=x_ia)

        self.result.main_iterations = 0

        j = 0
        while True:
            j += 1
            self.result.main_iterations += 1

            if self.settings.creat_hyper_block_test:
                kt_test_list = [(6, 8), (0, 4), (3, 7), (1, 5), (1, 5)]
                tic = time.time()
                kt_test = kt_test_list[j-1]
                hat_t_set = self.test_create_new_hyper_block(kt_test)
                time_new_block = time.time() - tic
                self.result.current_used_time += time_new_block
                logger.info(
                    '-----------------------------------------------------')
                logger.info('Elapsed time: --{0}-- seconds'
                            .format(round(self.result.current_used_time, 2)))
                logger.info(
                    '-----------------------------------------------------')
            else:
                tic = time.time()
                hat_t_set = self.create_new_hyper_block(
                    check_w=w_check, z=z, duals=duals,
                    num_hyper_block=self.settings.num_hyper_block_per_iter,
                    max_size_hyper=self.settings.max_size_hyper_block)

                time_new_block = time.time() - tic
                self.result.current_used_time += time_new_block
                logger.info(
                    '-----------------------------------------------------')
                logger.info('Elapsed time: --{0}-- seconds'
                            .format(round(self.result.current_used_time, 2)))
                logger.info(
                    '-----------------------------------------------------')

            i = 0
            while hat_t_set:
                i += 1
                # fw colgen for new hyper blocks
                w_check = self.fw_column_generation(check_w=w_check,
                                                    duals=duals,
                                                    t_set=hat_t_set)
                tic = time.time()
                # solve extended inner master problem
                z, _, w_ia, slacks, duals_new, obj_value_ia, \
                    slacks_hyper_max, _ = \
                    self.problem.master_problems.solve_ia(
                        self.settings.lp_solver)
                # check if the extended inner master problem is infeasible
                if z is not None:
                    self.result.cg_relaxation = obj_value_ia
                    max_slack_value = max(max(item) for item in slacks)
                    sum_slack_values = sum(item[0] + item[1] for item in slacks)
                    logger.info('{0: <15}{1: <30}{2: <30}'
                                '{3: <30}'.format('CG iter(new)',
                                                  'IA obj. value',
                                                  'max slack value IA',
                                                  'sum slack values IA'))

                    logger.info('{0: <15}{1: <30}{2: <30}{3: <30}'
                                .format(i, self.result.sense *
                                        self.result.cg_relaxation,
                                        max_slack_value, sum_slack_values))
                    logger.info('{0: <15}{1: <30}'
                                .format('CG iter(new)',
                                        'max slack value hyper block'))
                    logger.info('{0: <15}{1: <30}'
                                .format(i, slacks_hyper_max))
                    if slacks_hyper_max + sum_slack_values < 10e-5:
                        self.result.cg_relaxation = obj_value_ia

                    w_check = w_ia
                    duals = duals_new
                else:
                    logger.info('Extended inner master problem is infeasible')

                time_fast_cg = round(time.time() - tic, 2)
                logger.info('Time used for ia (hyper block) '
                            'in iter {0}-{1}: --{2}-- seconds'
                            .format(j, i, time_fast_cg))
                self.result.current_used_time += time_fast_cg
                logger.info(
                    '-----------------------------------------------------')
                logger.info('Elapsed time: --{0}-- seconds'
                            .format(round(self.result.current_used_time, 2)))
                logger.info(
                    '-----------------------------------------------------')
                if i == self.settings.max_iter_fast_cg_hyper:
                    break

            t_set = [t for t in
                     self.problem.approx_data.inner_points.points.keys()]
            i = 0
            while True:
                i += 1
                # fw colgen for active blocks
                check_w = self.fw_column_generation(check_w=check_w,
                                                    duals=duals,
                                                    t_set=t_set)
                tic = time.time()
                # solve extended inner master problem
                z, x_ia, w_ia, slacks, duals_new, obj_value_ia, \
                    slacks_hyper_max, _ = \
                    self.problem.master_problems.solve_ia(
                        self.settings.lp_solver)
                # check if the extended inner master problem is infeasible
                if z is not None:
                    self.result.cg_relaxation = obj_value_ia
                    max_slack_value = max(max(item) for item in slacks)
                    sum_slack_values = sum(item[0] + item[1] for item in slacks)
                    logger.info('{0: <15}{1: <30}{2: <30}'
                                '{3: <30}'.format('CG iter(active)',
                                                  'IA obj. value',
                                                  'max slack value IA',
                                                  'sum slack values IA'))

                    logger.info('{0: <15}{1: <30}{2: <30}{3: <30}'
                                .format(i, self.result.sense *
                                        self.result.cg_relaxation,
                                        max_slack_value, sum_slack_values))

                    logger.info('{0: <15}{1: <30}'
                                .format('CG iter(active)',
                                        'max slack value hyper block'))
                    logger.info('{0: <15}{1: <30}'
                                .format(i, slacks_hyper_max))
                    if slacks_hyper_max + sum_slack_values < 10e-5:
                        # logger.info('Slacks (hyper blocks) '
                        #             'are eliminated via FW colgen')
                        # # break
                        self.result.cg_relaxation = obj_value_ia

                    check_w = w_ia
                    duals = duals_new
                else:
                    logger.info('Extended inner master problem is infeasible')

                time_fast_cg = round(time.time() - tic, 2)
                logger.info('Time used for ia (active block) '
                            'in iter {0}-{1}: --{2}-- seconds'
                            .format(j, i, time_fast_cg))
                self.result.current_used_time += time_fast_cg
                logger.info(
                    '-----------------------------------------------------')
                logger.info('Elapsed time: --{0}-- seconds'
                            .format(round(self.result.current_used_time, 2)))
                logger.info(
                    '-----------------------------------------------------')

                if i == self.settings.max_iter_fast_cg_active:
                    break

            if self.settings.standard_cg:
                self.column_generation(duals=duals, x_ia=x_ia)

            if self.settings.cg_find_solution:
                tic = time.time()
                self.find_solution(x_ia, self.result.main_iterations)
                time_find_solution = time.time() - tic
                self.result.current_used_time += time_find_solution
                logger.info('Time used for FindSol '
                            'in iter {0}: --{1}-- seconds'
                            .format(self.result.main_iterations,
                                    time_find_solution))
                logger.info('-------------------------------------------------')
                logger.info('Elapsed time at FindSol iter {0}: --{1}-- seconds'
                            .format(self.result.main_iterations,
                                    round(self.result.current_used_time, 2)))
                logger.info('-------------------------------------------------')

            if j == self.settings.cg_max_main_iter:
                logger.info('\nIteration limit')
                break

    def ia_init(self, duals=None):
        """Initialization of inner approximation

        :param duals: Initial dual vector for initialization
        :type duals: ndarray
        """

        logger.info('\nInitialization')

        tic = time.time()

        # initial dual vector
        if duals is None:
            duals = np.zeros(shape=self.problem
                             .block_model.cuts.num_of_global_cuts)

        duals, check_w = self.sub_gradient(duals)

        time_sub_gradient = round(time.time() - tic, 2)
        logger.info('\nTime used for SubGradient: --{0}-- seconds'
                    .format(time_sub_gradient))
        self.result.current_used_time += time_sub_gradient

        logger.info('-----------------------------------------------------')
        logger.info('Elapsed time: --{0}-- seconds'
                    .format(round(self.result.current_used_time, 2)))
        logger.info('-----------------------------------------------------')

        return check_w, duals

    def column_generation(self, approx_solver=False, duals=None, x_ia=None):
        """Performs column generation steps (see paper)

        :param subset_of_blocks: apply column generation for reduced block set
        :type subset_of_blocks: list or None
        :param approx_solver: enables approximate solving of subproblems in \
        column generation
        :type approx_solver: bool
        :return: Dual solution from IA master problem regarding global \
        constraints
        :rtype: ndarray
        """

        logger.info('\n=======================================================')
        if approx_solver:
            logger.info('Column generation: approximated subproblem solving')
        else:
            logger.info('Column generation')
        new_columns_generated = \
            [0] * self.problem.approx_data.inner_points.get_num_blocks()
        num_minlp_problems_solved = self.result.cg_num_minlp_problems

        i = 0
        if duals is None or x_ia is None:
            tic = time.time()
            # solve extended inner master problem
            _, x_ia, _, _, duals, obj_value_ia, _, _ = \
                self.problem.master_problems.solve_ia(self.settings.lp_solver)
            self.result.cg_relaxation = obj_value_ia
            self.result.current_used_time += time.time() - tic

        while True:
            i += 1
            reduced_cost_direction = np.concatenate(([1], duals))

            _, _, tilde_t_set = \
                self.get_active_block(reduced_cost_direction)
            # linear atomic blocks not included in tilde_t_set
            blocks = tilde_t_set

            # generate new columns
            generate_column_time_list = {}
            reduced_cost_list = {}

            # generate columns according to dual values
            for k in blocks:
                hyper_block = self.problem.approx_data.inner_points.KT[k]
                if len(hyper_block) == 1:
                    tic = time.time()
                    _, _, reduced_cost_list[k], new_point, _ = \
                        self.generate_column(k, reduced_cost_direction,
                                             approx_solver=approx_solver,
                                             x_k=x_ia.get_block(k))
                    generate_column_time_list[k] = round(time.time() - tic, 2)
                    if new_point is True:
                        new_columns_generated[k] += 1
                    self.result.current_used_time += time.time() - tic
                else:
                    tic = time.time()
                    _, _, reduced_cost_list[k], new_point, _ = \
                        self.generate_column_hyper_block(hyper_block,
                                                         reduced_cost_direction)
                    generate_column_time_list[k] = round(time.time() - tic, 2)
                    if new_point is True:
                        new_columns_generated[k] += 1
                    self.result.current_used_time += time.time() - tic

            # solve extended inner master problem
            tic = time.time()
            z, x_ia, w_ia, slacks, duals, obj_value_ia, _, _ = \
                self.problem.master_problems.solve_ia(self.settings.lp_solver)
            self.result.cg_relaxation = obj_value_ia
            max_slack_value = max(max(item) for item in slacks)
            sum_slack_values = sum(item[0] + item[1] for item in slacks)
            logger.info('{0: <15}{1: <30}{2: <30}'
                        '{3: <30}'.format('CG iter', 'IA obj. value',
                                          'max slack value IA',
                                          'sum slack values IA'))

            logger.info('{0: <15}{1: <30}{2: <30}''{3: <30}'
                        .format(i, self.result.sense *
                                self.result.cg_relaxation,
                                max_slack_value, sum_slack_values))
            self.result.current_used_time += time.time() - tic
            logger.info('-------------------------------------------------')
            logger.info('Elapsed time: --{0}-- seconds'
                        .format(round(self.result.current_used_time, 2)))
            logger.info('-------------------------------------------------')

            if i >= self.settings.max_iter_standard_cg:
                logger.info('Iteration limit')
                logger.info('Reduced cost: {0}'
                            .format(str(reduced_cost_list)))
                logger.info('New columns added: {0}'
                            .format(str(new_columns_generated)))
                break

            logger.info('Reduced cost: {0}'
                        .format(str(reduced_cost_list)))

            if all([item >= -1e-6 for item in
                    reduced_cost_list.values()]) is True:
                logger.info('Reduced costs greater than zero')
                logger.info('New columns added: {0}'
                            .format(str(new_columns_generated)))
                break

        self.result.num_cg_iterations += i

        # number of MINLP subproblems during CG
        logger.info(
            'number of minlp subproblems '
            'solved during CG: {0}'.format(self.result.cg_num_minlp_problems -
                                           num_minlp_problems_solved))
        logger.info('\n=======================================================')

    def fw_column_generation(self, check_w, duals, t_set):
        """ Performs fast FW column generation steps (see paper) """

        logger.info('---------------------------------------------------------')
        logger.info('Fast fw column generation')

        tic_fast_cg = time.time()

        direction = np.concatenate(([1], duals))

        # sigma_cg = abs(duals) + value?
        sigma_cg = abs(duals)

        # todo: refactor this, make use of BlockVector,
        # if neccessary extend BlockVector class
        for j, (index, vector) in enumerate(check_w.vectors.items()):
            if j == 0:
                check_w_array = np.array(vector.reshape(1, len(vector)))
            else:
                check_w_array = \
                    np.concatenate((check_w_array,
                                    vector.reshape(1, len(vector))))

        global_cuts_rhs = []
        for cut in self.problem.block_model.cuts.global_cuts:
            global_cuts_rhs.append(cut.rhs)
        global_cuts_rhs = np.array(global_cuts_rhs)

        # num_unfixed_nlp_problems_solved = \
        #     self.result.cg_num_unfixed_nlp_problems
        gamma_cg_plus = 1

        # logger.info('{0: <15}'
        #             .format('hat_t_set:'))
        # logger.info(list(t_set))
        i = 0
        tilde_v, tilde_w, tilde_t_set = \
            self.get_active_block(dir_im_space=direction, t_set=t_set)
        # logger.info('{0: <15}'
        #             .format('active block:'))
        # active_block = {ti: self.problem.approx_data.inner_points.KT[ti]
        #                 for ti in tilde_t_set}
        # logger.info(active_block)
        # v_plus <- tilde_v
        for j, (index, vector) in enumerate(tilde_v.vectors.items()):
            if j == 0:
                v_plus_array = np.array(vector.reshape(1, len(vector)))
            else:
                v_plus_array = \
                    np.concatenate((v_plus_array,
                                    vector.reshape(1, len(vector))))

        new_columns_generated = {t: 0 for t in t_set}
        # generate_column_time_list = {}

        while True:
            i += 1
            # solve sub-problems for t in tilde_t_set and add columns
            for t in tilde_t_set:
                hyper_block = self.problem.approx_data.inner_points.KT[t]
                if len(hyper_block) == 1:
                    # logger.info('{0: <15}{1: <30}'
                    #             .format('atomic block:', t))
                    is_new_point = \
                        self.fast_solve_atomic_sub_problem(block_id=t,
                                                           dir_im_space=
                                                           direction,
                                                           w_k=
                                                           tilde_w.get_block(t))
                else:
                    # logger.info('{0: <15}{1: <30}'
                    #             .format('hyper block:', t))
                    is_new_point = \
                        self.fast_solve_agg_sub_problem(
                            dir_im_space=direction, hyper_block=hyper_block,
                            mip_pool=self.settings.hyper_block_mip_pool)

                if is_new_point:
                    new_columns_generated[t] += is_new_point

            if i == self.settings.cg_fast_fw_max_iter:
                logger.info('{0: <30}{1: <15}'
                            .format('reach max iteration:', i))
                break

            tilde_v, tilde_w, tilde_t_set = \
                self.get_active_block(dir_im_space=direction, t_set=t_set)
            # logger.info('{0: <15}'
            #             .format('active block:'))
            # active_block = {ti: self.problem.approx_data.inner_points.KT[ti]
            #                 for ti in tilde_t_set}
            # logger.info(active_block)
            # logger.info(list(tilde_t_set))
            # logger.info(list(new_columns_generated.values()))

            # use column
            for j, (index, vector) in enumerate(tilde_v.vectors.items()):
                if j == 0:
                    tilde_v_array = np.array(vector.reshape(1, len(vector)))
                else:
                    tilde_v_array = \
                        np.concatenate((tilde_v_array,
                                        vector.reshape(1, len(vector))))

            # the operations add, substract and multiplication by scalar is
            # implemented in BlockVector class. Maybe it is easier to use them
            # The implementation of summing the components of BlockVector
            # can implemented and added there

            # determining the step size
            coeff_w_r_array = tilde_v_array - check_w_array
            coeff_a = np.multiply((np.sum(coeff_w_r_array[:, 1:], axis=0)
                                   - global_cuts_rhs), sigma_cg)
            coeff_a = \
                2 * np.dot(coeff_a, np.sum(coeff_w_r_array[:, 1:], axis=0))
            coeff_b = np.multiply(sigma_cg,
                                  np.sum(check_w_array[:, 1:], axis=0))
            coeff_b = 2 * np.dot(coeff_b,
                                 np.sum(coeff_w_r_array[:, 1:], axis=0))
            coeff_b += np.sum(coeff_w_r_array[:, 0], axis=0)

            if coeff_a == 0:  # tilda_w equals nu_plus
                logger.info('tilda_w equals nu_plus')
                break
            else:
                theta_cg = - coeff_b / coeff_a
            # logger.info('theta_cg: {0}'.format(theta_cg))
            if theta_cg == 0:
                break

            # update step
            add_term = theta_cg * (tilde_v_array - check_w_array)
            v_array = copy.copy(v_plus_array)
            v_plus_array = check_w_array + add_term
            # fast FW step
            gamma_cg = gamma_cg_plus
            gamma_cg_plus = 0.5 * (1 + math.sqrt(4 * gamma_cg ** 2
                                                 + 1))
            check_w_array = v_plus_array + \
                (gamma_cg - 1) / gamma_cg_plus * \
                (v_plus_array - v_array)

            gap = {}
            for k in range(self.problem.block_model.num_blocks):
                if self.problem.block_model.sub_models[k].linear is False:
                    gap[k] = np.dot(direction, (check_w_array[k, :] -
                                                tilde_v_array[k, :]))

            # logger.info('Value of gap (g_k):')
            # logger.info(gap)

            # logger.info('Number of new columns in the current iteration:')
            # logger.info(new_columns_generated)

            # update direction
            direction = 2 * np.multiply(sigma_cg, np.sum(check_w_array[:, 1:],
                                                         axis=0) -
                                        global_cuts_rhs)
            direction = np.concatenate(([1], direction))

        logger.info('hat_t_set:')
        logger.info(list(t_set))
        logger.info('New columns in FastCG:')
        logger.info(list(new_columns_generated.values()))

        # todo: refactor this, make use of BlockVector,
        # if neccessary extend BlockVector class
        check_w = BlockVector()
        for k in range(self.problem.block_model.num_blocks):
            check_w.set_block(k, check_w_array[k])

        # # number of unfixed nlp subproblems during CG
        # logger.info('number of unfixed nlp subproblems '
        #             'solved during CG: {0}'
        #             .format(self.result.cg_num_unfixed_nlp_problems -
        #                     num_unfixed_nlp_problems_solved))
        time_fast_cg = round(time.time() - tic_fast_cg, 2)
        self.result.current_used_time += time_fast_cg
        logger.info('Time used for solving subproblem'
                    ': --{0}-- seconds'.
                    format(time_fast_cg))
        logger.info('---------------------------------------------------------')

        return check_w

    def sub_gradient(self, direction_vector):
        """Performs sub-gradient iterations

        :param direction_vector: Initial vector for sub-gradient iterations
        :type direction_vector: ndarray
        :return: Final direction vector
        :rtype: tuple
        """

        y = BlockVector()

        # create an array of rhs of global constraints
        b = np.zeros(shape=self.problem.block_model.cuts.num_of_global_cuts)
        for j, cut in enumerate(self.problem.block_model.cuts.global_cuts):
            b[j] = cut.rhs

        iteration = 0
        alpha = 1
        logger.info('\nSubgradient steps')
        logger.info('{0: <15}{1: <30}{2: <30}'
                    .format('Subgra.iter', 'Lagrange bound', 'alpha'))

        direction_vector_prev = copy.deepcopy(direction_vector)
        lag_sol_prev = float('-inf')

        violation = np.zeros(
            shape=self.problem.block_model.cuts.num_of_global_cuts)

        while iteration < self.settings.cg_sub_gradient_max_iter:
            time_generate_column_sub_gradient_list = {}
            new_columns_generated = [0] * self.problem.block_model.num_blocks
            iteration += 1
            lag_sol = 0
            direction = np.concatenate(([1], direction_vector))
            for k in range(self.problem.block_model.num_blocks):
                if self.problem.block_model.sub_models[k].linear:
                    # solve the sub-problem of linear atomic block
                    # logger.info('{0: <15}{1: <30}'
                    #             .format('linear block:', k))
                    dir_orig_space = \
                        self.problem.block_model.trans_into_orig_space(
                            k, direction)
                    feasible_point, _, _, _ = \
                        self.problem.sub_problems[k].minlp_solve(
                            solver_name='gurobi',
                            direction=dir_orig_space)
                    y.set_block(k, feasible_point)
                else:
                    # logger.info('{0: <15}{1: <30}'
                    #             .format('nonlinear block:', k))
                    tic = time.time()
                    feasible_point, primal_bound, reduced_cost, new_point, _ = \
                        self.generate_column(k, direction)
                    time_generate_column_sub_gradient_list[k] = round(
                        time.time() - tic, 2)
                    if new_point is True:
                        new_columns_generated[k] += 1
                    y.set_block(k, feasible_point)
                    lag_sol += primal_bound

            lag_sol -= np.dot(direction_vector, b)

            logger.info('{0: <15}{1: <30}{2: <30}'
                        .format(iteration, self.result.sense * lag_sol, alpha))

            if iteration == 1:
                violation = self.problem.eval_viol_lin_global_constraints(y)

                lag_sol_prev = lag_sol
                direction_vector_prev = copy.deepcopy(direction_vector)
            else:
                # update the step
                if lag_sol <= lag_sol_prev:
                    alpha *= 0.5
                    direction_vector = copy.deepcopy(direction_vector_prev)
                else:
                    alpha *= 2
                    violation = self.problem.eval_viol_lin_global_constraints(y)

                    lag_sol_prev = lag_sol
                    direction_vector_prev = copy.deepcopy(direction_vector)

            if all(abs(item) <= 1e-1 for item in violation):
                # if no violation, stop
                break

            # update direction
            direction_vector += alpha * violation

        check_w = BlockVector()

        # taking most recent generated column into check_w
        for k in range(self.problem.block_model.num_blocks):
            column = \
                self.problem.block_model.trans_into_im_space(k, y.get_block(k))
            check_w.set_block(k, column)

        return direction_vector, check_w

    def generate_column(self, block_id, direction, heuristic=True,
                        approx_solver=False, x_k=None):
        """Generates the inner point (and corresponding column) either
        with MINLP sub-problem or with NLP sub-problem (too heuristically);
        adds valid local linear cut to heu_oa_master_problem if any

        :param block_id: Block identifier
        :type block_id: int
        :param direction: Direction in image space
        :type direction: ndarray
        :param heuristic: Indicates if the sub-problem must be solved \
        heuristically
        :type heuristic: bool
        :param approx_solver: enables approximate solving of subproblems in \
        column generation
        :type approx_solver: bool
        :param x_k: start_point for solving subproblems
        :type x_k: BlockVector or None
        :return: Inner point, primal bound, reduced cost of new point, \
        bool value indicating whether new point is generated and \
        corresponding column
        :rtype: tuple
        """

        # todo not clear what are we doing with this

        if approx_solver:  # approximate solve minlp subproblem
            feasible_point, primal_bound, reduced_cost, is_new_point, \
                column = self.approx_solve_minlp_subproblem(
                    block_id, direction, x_k=x_k)
        else:
            if self.settings.cg_generate_columns_with_nlp is True:
                feasible_point, primal_bound, reduced_cost, is_new_point, \
                    column = self.approx_solve_minlp_subproblem(block_id,
                                                                direction,
                                                                x_k=x_k)
                if reduced_cost > -0.01:
                    feasible_point, reduced_cost, primal_bound, _, \
                        is_new_point, column = \
                        self.solve_minlp_subproblem(
                            block_id, direction, heuristic=heuristic)
            else:
                feasible_point, reduced_cost, primal_bound, _, is_new_point, \
                    column = self.solve_minlp_subproblem(
                        block_id, direction, heuristic=heuristic)

        reduced_cost = round(reduced_cost, 3)

        return feasible_point, primal_bound, reduced_cost, is_new_point, column

    def generate_column_hyper_block(self, hyper_block, direction,
                                    heuristic=True):
        """Generates the inner point (and corresponding column) either
        with MINLP sub-problem;
        adds valid local linear cut to heu_oa_master_problem if any

        :param block_id: Block identifier
        :type block_id: int
        :param direction: Direction in image space
        :type direction: ndarray
        :param heuristic: Indicates if the sub-problem must be solved \
        heuristically
        :type heuristic: bool
        :param approx_solver: enables approximate solving of subproblems in \
        column generation
        :type approx_solver: bool
        :param x_k: start_point for solving subproblems
        :type x_k: BlockVector or None
        :return: Inner point, primal bound, reduced cost of new point, \
        bool value indicating whether new point is generated and \
        corresponding column
        :rtype: tuple
        """

        feasible_point, reduced_cost, primal_bound, is_new_point, \
            column = self.solve_agg_minlp_subproblem(
                dir_im_space=direction, hyper_block=hyper_block,
                heuristic=heuristic)

        reduced_cost = round(reduced_cost, 3)

        return feasible_point, primal_bound, reduced_cost, is_new_point, column

    def solve_minlp_subproblem(self, block_id,
                               dir_im_space,
                               compute_reduced_cost=True,
                               heuristic=True):
        """Solves MINLP subproblem, adds inner point, \
        (either in compact form or in the original) and computes reduced cost \
        for the new inner point

        :param block_id: Block identifier
        :type block_id: int
        :param dir_im_space: Direction in image space
        :type dir_im_space: ndarray
        :param compute_reduced_cost: Indicates if reduced cost has to be \
        computed
        :type compute_reduced_cost: bool
        :param heuristic: Indicates if the sub-problem must be solved \
        heuristically
        :type heuristic: bool
        :return: Inner point (feasible point), reduced cost value, \
        primal bound of the sub-problem, dual bound of the sub-problem, \
        bool value indicating whether new inner point was generated, \
        corresponding column to the inner point
        :rtype: tuple
        """

        self.result.cg_num_minlp_problems += 1

        # can be None in case of initialization of the inner master problem
        reduced_cost = None
        is_new_point = False

        # transform into original space the direction
        dir_orig_space = \
            self.problem.block_model.trans_into_orig_space(block_id,
                                                           dir_im_space)

        if heuristic is True:
            solver_options = self.settings.get_minlp_solver_options()
        else:
            solver_options = None

        # solve the sub-problem
        feasible_point, primal_bound, dual_bound, _ = \
            self.problem.sub_problems[block_id].minlp_solve(
                solver_name=self.settings.minlp_solver,
                solver_options=solver_options,
                direction=dir_orig_space)

        column = None
        if compute_reduced_cost is True:
            # compute reduced cost

            # get the best inner point with given direction
            best_point, best_obj_val = self.problem.get_min_inner_point(
                block_id, dir_orig_space)
            reduced_cost = primal_bound - best_obj_val  # absolute reduced cost

            if reduced_cost < 0:
                # add the inner point with negative absolute reduced cost
                is_new_point, _, column = \
                    self.problem.add_inner_point(block_id, feasible_point)
        else:
            is_new_point, _, column = \
                self.problem.add_inner_point(
                    block_id, feasible_point,
                    self.settings.cg_min_inner_point_distance)

        if column is None:
            column = self.problem.block_model.trans_into_im_space(
                block_id, feasible_point)

        # check if subproblem is solved to optimality
        gap = abs(primal_bound - dual_bound) / (
                max(abs(primal_bound), abs(dual_bound)) + 1e-5)
        if gap > 0.0001:
            self.result.optimal_subproblems = False

        return feasible_point, reduced_cost, primal_bound, dual_bound, \
               is_new_point, column

    def get_slack_directions(self, slacks):
        """Computes new direction based on the slack values of IA master problem

        :param slacks: Slack values stored as a list of tuples
        :type slacks: list
        :return: New direction in image space
        :rtype: ndarray
        """

        # get maximum slack value
        max_slack_value = max(max(item) for item in slacks)

        direction_image_space = np.zeros(
            shape=self.problem.block_model.cuts.num_of_global_cuts + 1)
        for m, slack in enumerate(slacks):
            # check if slacks are zero
            if any(item != 0 for item in slack) and \
                    max(slack) > 0.1 * max_slack_value:
                direction_image_space[m + 1] = 1

        return direction_image_space

    def approx_solve_minlp_subproblem(self, block_id, dir_im_space, x_k=None):
        """Solves MINLP subproblem approximately, adds inner point \
        (either in compact form or in the original) and computes reduced cost
        for the new inner point

        :param block_id: Block identifier
        :type block_id: int
        :param dir_im_space: Direction in image space
        :type dir_im_space: ndarray
        :param x_k: start_point for solving subproblems
        :type x_k: BlockVector or None
        :return: Inner point (feasible point), reduced cost value, \
        primal bound of the sub-problem, dual bound of the sub-problem, \
        bool value indicating whether new inner point was generated, \
        corresponding column to the inner point
        :rtype: tuple
        """

        # todo that's fast solve MINLP, it is regarding aggregation

        self.result.cg_num_unfixed_nlp_problems += 1

        dir_orig_space = self.problem.block_model.trans_into_orig_space(
            block_id, dir_im_space)

        if x_k is not None:
            best_point = x_k
            best_point_obj_val = np.dot(dir_orig_space, best_point)
        else:
            best_point, best_point_obj_val = self.problem.get_min_inner_point(
                block_id, dir_orig_space)

        solver_options = self.settings.get_nlp_solver_options()

        # in order to solve NLP relaxation of MINLP problem it is not
        # necessary explicitly to relax integer variables
        # the NLP solver simply treats them as continuous variables
        unfixed_tilde_y, new_point_obj_val, _, sol_is_feasible = \
            self.problem.sub_problems[block_id].minlp_solve(
                self.settings.nlp_solver, direction=dir_orig_space,
                solver_options=solver_options, start_point=best_point)

        if self.problem.block_model.sub_models[block_id].integer is True:
            self.result.cg_num_fixed_nlp_problems += 1

            rounded_point = self.problem.round(block_id, unfixed_tilde_y)
            # start_point is used for fixing the integers
            tilde_y, new_point_obj_val, sol_is_feasible = \
                self.problem.sub_problems[block_id].fixed_minlp_solve(
                    self.settings.nlp_solver,
                    start_point=rounded_point,
                    direction=dir_orig_space,
                    solver_options=solver_options)

        else:
            tilde_y = unfixed_tilde_y

        reduced_cost = 0
        column = None
        is_new_point = False
        if sol_is_feasible is True:
            reduced_cost = (new_point_obj_val - best_point_obj_val) / (
                    max(abs(new_point_obj_val),
                        abs(best_point_obj_val)) + 1e-5)
            is_new_point, _, column = \
                self.problem.add_inner_point(block_id, tilde_y,
                                             min_inner_point_dist=
                                             self.settings
                                             .cg_min_inner_point_distance)
        else:
            tilde_y = None
            new_point_obj_val = None

        return tilde_y, new_point_obj_val, reduced_cost, is_new_point, column

    def find_solution_init(self, iter_index=None):
        """Method to generate a feasible solution and therefore reducing
        the slacks to zero in innerMaster problem

        :param iter_index: number of main iteration when the method is called
        :type: int
        """
        logger.info('\n=======================================================')
        logger.info('Find solution - init')

        # solve IA master problem
        z, x_ia, w_ia, slacks, duals, obj_value_ia, _, _ = \
            self.problem.master_problems.solve_ia(self.settings.lp_solver)
        self.result.cg_relaxation = obj_value_ia

        # solve NLP resource projection problem
        tilde_y, obj_val_nlp_1st, sol_is_feasible = \
            self.problem.master_problems.solve_nlp_resource_proj_problem(
                self.settings.nlp_solver, w_ia, float('inf'))

        if sol_is_feasible:
            logger.info('-------------------------------------')
            # tilde_y: NLP project point
            c_tilde_y = self.problem.block_model.cuts.obj.eval(tilde_y)
            logger.info('solve_nlp_resource_proj obj: {0} '
                        .format(self.result.sense * round(c_tilde_y, 4)))
            logger.info('-------------------------------------')
        else:
            logger.info('-------------------------------------')
            logger.info('solve_nlp_resource_proj not feasible')
            c_tilde_y = 0
            logger.info('-------------------------------------')

        c_tilde_x = 0
        if sol_is_feasible:
            # solve MIP project problem
            hat_x, _, sol_is_feasible = \
                self.problem.master_problems.solve_mip_proj_problem(
                    self.settings.mip_solver, tilde_y, float('inf'))

            if sol_is_feasible:
                # NLP problem with fixed integers
                tilde_x, obj_val, sol_is_feasible = \
                    self.problem.master_problems.nlp_solve(
                        self.settings.nlp_solver, point_to_fix=hat_x,
                        start_point=hat_x)
            else:
                logger.info('-------------------------------------')
                logger.info('solve_mip_projct_problem not feasible')
                logger.info('-------------------------------------')

            # testing findSol
            if sol_is_feasible:
                logger.info('-------------------------------------')
                # tilde_x: fixed NLP solution
                c_tilde_x = obj_val
                logger.info('solve_fixed_nlp_problem obj: {0} '
                            .format(self.result.sense * round(c_tilde_x, 4)))
                logger.info('-------------------------------------')
            else:
                logger.info('-------------------------------------')
                logger.info('solve_fixed_nlp_problem not feasible')
                logger.info('-------------------------------------')

        if sol_is_feasible is True:
            logger.info('{0: <50}{1: <30}'
                        .format('Gap (c_tilde_y '
                                'and c_tilde_x):',
                                self.result.get_gap(c_tilde_x, c_tilde_y)))

            self.result.set_new_primal_bound(obj_val, tilde_x)

            for k in range(self.problem.block_model.num_blocks):
                # self.problem.master_problems.inner_problem.model.blocks[
                #     k + 1].z_set.pprint()
                new_point, _, _ = \
                    self.problem.add_inner_point(k, tilde_x.get_block(k),
                                                 self.settings
                                                 .cg_min_inner_point_distance)
                # # for testing slack elimination
                # if new_point:
                #     print('add feasible point: block ' + str(k))
                #     i = len(self.problem.approx_data.inner_points.points[k])
                #     self.problem.master_problems.inner_problem.model.blocks[
                #         k + 1].z[i].fix(1)
                #     self.problem.master_problems.inner_problem.model.slack_pos.fix(0)
                #     self.problem.master_problems.inner_problem.model.slack_neg.fix(
                #         0)
                # self.problem.master_problems.inner_problem.model.blocks[
                #     k + 1].z_set.pprint()

            logger.info('\nAfter solving fixed NLP projection problem, '
                        'the solution point is feasible')

            if iter_index is None:  # this is for printing number of iteration
                # in the logger when generating feasible candidate
                logger.info('{0: <50}{1: <30}'
                            .format('Projection Gap (c(x_NLP_proj) '
                                    'and primal bound):',
                                    self.result.get_gap(
                                        self.result.primal_bound, c_tilde_y)))
                logger.info('\nFeasible candidate obtained in this '
                            'iteration: {0}'
                            .format(self.result.sense * obj_val))
            else:
                logger.info('{0: <50}{1: <30}'
                            .format('Projection Gap (c(x_NLP_proj) '
                                    'and primal bound):',
                                    self.result.get_gap(
                                        self.result.primal_bound, c_tilde_y)))
                logger.info('\nFeasible candidate obtained in '
                            'iter {0}: {1}'
                            .format(int(iter_index),
                                    self.result.sense * obj_val))

        else:
            if iter_index is None:  # this is for printing number of
                # iteration in the logger when generating feasible candidate
                logger.info('\nNo feasible candidate obtained in this '
                            'iteration')
            else:
                logger.info('\nNo feasible candidate obtained in iter {0}'
                            .format(int(iter_index)))
        logger.info('\n=======================================================')

    def find_solution(self, x_ia, iter_index=None):
        """Primal heuristics method

        :param iter_index: number of main iteration when the method is called
        :type: int
        :param x_ia: primal solution of inner LP
        :type: BlockVector
        """
        logger.info('\n=======================================================')
        logger.info('Find solution - projection from ia solution - '
                    'local search')

        mip_solver = 'gurobi_persistent'
        pool_solutions = self.settings.cg_find_sol_mip_pool

        old_feasible_obj_val = float('inf')
        tau = self.settings.cg_find_sol_mip_pool_tau
        ii = 1
        logger.info('\n---------------------------------------------------')
        logger.info('Local search iter {0}'.format(ii))
        while True:

            hat_x_list, _, sol_is_feasible = \
                self.problem.master_problems.solve_mip_proj_problem(
                    solver_name=mip_solver,
                    point_to_project=x_ia,
                    pool_solutions=pool_solutions)

            if sol_is_feasible is False:
                logger.info('mip proj problem is infeasible')
                break

            i_max = len(hat_x_list)
            hat_x = hat_x_list[0]
            logger.info('Solution pool generated from '
                        'solving MIP project problem: {0}'.format(i_max))
            logger.info('Solution pool: solution 1')

            i = 0
            feasible_obj_val = float('inf')
            feasible_obj_point = None

            while True:
                i += 1
                c_hat_x = self.problem.block_model.cuts.obj.eval(hat_x)
                logger.info('---------------MIP-projection--------------------')
                logger.info('c_hat_x: {0}'.format(c_hat_x))
                logger.info('-------------------------------------------------')

                try:
                    # NLP problem with fixed integers
                    tilde_x, obj_val, sol_is_feasible = \
                        self.problem.master_problems.nlp_solve(
                            self.settings.nlp_solver, point_to_fix=hat_x,
                            start_point=hat_x)
                except ValueError:
                    sol_is_feasible = False

                if sol_is_feasible is True:
                    improved = self.result.set_new_primal_bound(obj_val,
                                                                tilde_x)

                    if obj_val < feasible_obj_val:
                        feasible_obj_val = obj_val
                        feasible_obj_point = copy.copy(tilde_x)

                    # for k in range(self.problem.block_model.num_blocks):
                    #     self.problem.add_inner_point(
                    #         k, tilde_x.get_block(k),
                    #         self.settings.cg_min_inner_point_distance)
                    self.add_feasible_sol_to_inner_point(tilde_x)

                    logger.info('\nAfter solving fixed NLP projection problem, '
                                'the solution point is feasible')
                    if improved is True:
                        logger.info('the feasible solution point improves')
                        logger.info('Obj. value: {0}'.format(
                            self.result.sense * self.result.primal_bound))
                    else:
                        logger.info('the feasible solution point does '
                                    'not improve')
                        logger.info('Obj. value: {0}'.format(
                            self.result.sense * obj_val))
                else:
                    logger.info(
                        '\nAfter solving fixed NLP the solution point is '
                        'infeasible')

                if iter_index is None and sol_is_feasible is True:  # this is
                    # for printing number of iteration in
                    # the logger when generating feasible candidate
                    logger.info('Feasible candidate obtained in this '
                                'iteration: {0}'
                                .format(self.result.sense * obj_val))
                elif iter_index is not None and sol_is_feasible is True:
                    logger.info('Feasible candidate '
                                'obtained in iter {0}: round {1}: pool {2}: {3}'
                                .format(int(iter_index), ii, i,
                                        self.result.sense * obj_val))
                elif iter_index is not None and sol_is_feasible is False:
                    logger.info('No feasible candidate '
                                'obtained in iter {0}: round {1}: pool {2}'
                                .format(int(iter_index), ii, i))

                if i == i_max:
                    break
                else:
                    hat_x = hat_x_list[i]
                    logger.info('\nSolution pool: solution {0}'.format(i + 1))

            if feasible_obj_val < old_feasible_obj_val:
                logger.info(
                    '\n---------------------------------------------------')
                if iter_index is None and feasible_obj_val \
                        is not float('inf'):
                    logger.info('Best feasible candidate obtained in this '
                                'iteration: {0}'
                                .format(self.result.sense *
                                        feasible_obj_val))
                elif iter_index is not None and feasible_obj_val \
                        is not float('inf'):
                    logger.info('Best feasible candidate '
                                'obtained in iter {0}: {1}'
                                .format(int(iter_index),
                                        self.result.sense *
                                        feasible_obj_val))

                x_ia = x_ia * tau + feasible_obj_point * (1 - tau)
                old_feasible_obj_val = feasible_obj_val
                ii += 1

                logger.info('Local search iter {0}'.format(ii))

            else:
                logger.info('New search does not find better '
                            'local feasible solution')
                break

            if ii == self.settings.cg_find_sol_mip_pool_max_round:
                logger.info('reaches local search round limit {0}'.format(ii))
                break

    def fast_solve_atomic_sub_problem(self, block_id, dir_im_space, w_k):
        """Solves MINLP subproblem approximately, adds inner point \
        (either in compact form or in the original) and computes reduced cost
        for the new inner point

        :param block_id: Block identifier
        :type block_id: int
        :param dir_im_space: Direction in image space
        :type dir_im_space: ndarray
        :param w_k: given column
        :type w_k: ndarray
        :return: Inner point (feasible point), primal bound of the sub-problem, \
        dual bound of the sub-problem, \
        bool value indicating whether new inner point was generated, \
        corresponding column to the inner point
        :rtype: tuple
        """

        solver_options = self.settings.get_nlp_solver_options()

        start_point, _, _ = \
            self.problem.sub_problems[block_id].resource_proj_solve(
                self.settings.nlp_solver, w_k)

        # direction must be in the original space
        dir_orig_space = self.problem.block_model.trans_into_orig_space(
            block_id, dir_im_space)

        # in order to solve NLP relaxation of MINLP problem it is not
        # necessary explicitly to relax integer variables
        # the NLP solver simply treats them as continuous variables
        unfixed_tilde_y, new_point_obj_val, _, sol_is_feasible = \
            self.problem.sub_problems[block_id].minlp_solve(
                self.settings.nlp_solver, direction=dir_orig_space,
                solver_options=solver_options, start_point=start_point)

        if self.problem.block_model.sub_models[block_id].integer is True:

            rounded_point = self.problem.round(block_id, unfixed_tilde_y)
            # start_point is used for fixing the integers
            tilde_y, new_point_obj_val, sol_is_feasible = \
                self.problem.sub_problems[block_id].fixed_minlp_solve(
                    self.settings.nlp_solver,
                    start_point=rounded_point,
                    direction=dir_orig_space,
                    solver_options=solver_options)

        else:
            tilde_y = unfixed_tilde_y

        is_new_point = False
        if sol_is_feasible is True:
            is_new_point, _, _ = \
                self.problem.add_inner_point(
                    block_id, tilde_y,
                    min_inner_point_dist=
                    self.settings.cg_min_inner_point_distance)

        return is_new_point

    def fast_solve_agg_sub_problem(self, dir_im_space, hyper_block,
                                   mip_pool=1):
        # hyper_block contains indices of atomic blocks
        # solve mini inner master problem
        check_x, _, _ = \
            self.problem.master_problems.solve_mini_ia(
                self.settings.lp_solver, hyper_block, dir_im_space)

        # solve aggregated MIP projection problem with mip pool option
        if mip_pool == 1:
            hat_y, _, _ = \
                self.problem.master_problems.solve_agg_mip_proj_problem(
                    solver_name='gurobi', point_to_project=check_x,
                    agg_blocks=hyper_block)
            hat_y_set = [hat_y]
        elif mip_pool > 1:
            hat_y_set, _, _ = \
                self.problem.master_problems.solve_agg_mip_proj_problem(
                    solver_name='gurobi_persistent', point_to_project=check_x,
                    agg_blocks=hyper_block, pool_solutions=mip_pool)
        else:
            hat_y_set = []

        # direction in the original space as a full vector
        dir_orig_space_full = \
            BlockVector(self.problem.block_model.block_sizes)
        # we compute direction only for relevant indices of hyperblock
        for k in hyper_block:
            dir_orig_space_full.set_block(
                k, self.problem.block_model.trans_into_orig_space(
                    k, dir_im_space))
        # num of added new columns
        is_new_point_num = 0
        for hat_y in hat_y_set:
            # solve fixed NLP
            tilde_x, _, sol_is_feasible = \
                self.problem.master_problems.agg_nlp_solve(
                    self.settings.nlp_solver, hyper_block,
                    point_to_fix=hat_y, start_point=hat_y,
                    cut_direction=dir_orig_space_full)

            block_id, _ = self.problem.approx_data.inner_points.check_block(
                hyper_block)
            if sol_is_feasible:
                # add column
                is_new_point, _, _ = \
                    self.problem.add_inner_point(block_id, tilde_x)
            else:
                print('no column added for block '+str(block_id))
                is_new_point = False
            is_new_point_num += is_new_point

        return is_new_point_num

    def solve_agg_minlp_subproblem(self, dir_im_space, hyper_block,
                                   heuristic=True):
        # hyper_block contains indices of atomic blocks
        self.result.cg_num_minlp_problems += 1

        # can be None in case of initialization of the inner master problem
        reduced_cost = None
        is_new_point = False

        if heuristic is True:
            solver_options = self.settings.get_minlp_solver_options()
        else:
            solver_options = None

        # direction in the original space as a full vector
        dir_orig_space_full = \
            BlockVector(self.problem.block_model.block_sizes)
        # we compute direction only for relevant indices of hyperblock
        for k in hyper_block:
            dir_orig_space_full.set_block(
                k, self.problem.block_model.trans_into_orig_space(
                    k, dir_im_space))

        feasible_point, primal_bound, sol_is_feasible = \
            self.problem.master_problems.agg_minlp_solve(
                solver_name=self.settings.minlp_solver,
                solver_options=solver_options,
                agg_blocks=hyper_block,
                cut_direction=dir_orig_space_full)

        block_id, _ = self.problem.approx_data.inner_points.check_block(
            hyper_block)

        column = None
        # compute reduced cost

        # get the best inner point with given direction
        _, best_obj_val = self.problem.get_min_inner_point(
            block_id, dir_orig_space_full)
        reduced_cost = primal_bound - best_obj_val  # absolute reduced cost

        if reduced_cost < 0:
            # add the inner point with negative absolute reduced cost
            is_new_point, _, column = \
                self.problem.add_inner_point(block_id, feasible_point)

        return feasible_point, reduced_cost, primal_bound, is_new_point, column

    def get_active_block(self, dir_im_space, t_set=None):

        tilde_v = BlockVector()
        tilde_t_set = []
        if t_set is None:
            t_set = list(self.problem.approx_data.inner_points.points.keys())

        t_set_enumerate = copy.copy(t_set)
        hat_t_set = copy.copy(t_set)
        for t in t_set_enumerate:
            if t in range(self.problem.block_model.num_blocks):
                # handle linear atomic block
                if self.problem.block_model.sub_models[t].linear:
                    if t in hat_t_set:
                        hat_t_set.remove(t)
            else:
                # select hyper-blocks with empty column
                if self.problem.approx_data.inner_points.get_size(t) == 0:
                    tilde_t_set.append(t)
                    hat_t_set.remove(t)

        # set of atomic block indices from t_set
        hat_k_set = []
        for t in hat_t_set:
            for k in self.problem.approx_data.inner_points.KT[t]:
                # remove linear atomic block from hat_k_set
                if self.problem.block_model.sub_models[k].linear is False:
                    if k not in hat_k_set:
                        hat_k_set.append(k)
        # fill resources for linear atomic block and
        # missing atomic blocks from hat_k_set
        for k in range(self.problem.block_model.num_blocks):
            if self.problem.block_model.sub_models[k].linear:
                # solve the sub-problem of linear atomic block
                dir_orig_space = \
                    self.problem.block_model.trans_into_orig_space(
                        k, dir_im_space)
                feasible_point, _, _, _ = \
                    self.problem.sub_problems[k].minlp_solve(
                        solver_name='gurobi',
                        direction=dir_orig_space)
                column = \
                    self.problem.block_model.trans_into_im_space(
                        k, feasible_point)
                tilde_v.set_block(k, column)
            else:
                if k not in hat_k_set:
                    column, _ = \
                        self.problem.get_min_column(k, dir_im_space)
                    tilde_v.set_block(k, column)

        # calculate minimum resources/column and select active blocks from
        # blocks (with columns) in t_set
        tilde_w = BlockVector()
        tilde_t_k_set = {k: k for k in hat_k_set}
        max_obj_val = {k: float('-inf') for k in hat_k_set}
        for t in hat_t_set:
            if t in range(self.problem.block_model.num_blocks):
                column, obj_val = \
                    self.problem.get_min_column(t, dir_im_space)
                tilde_w.set_block(t, column)
                # tilde_v.set_block(t, column)
                if obj_val > max_obj_val[t]:
                    max_obj_val[t] = obj_val
                    tilde_t_k_set[t] = t
            else:
                column_2d_array, _ = \
                    self.problem.get_min_column(t, dir_im_space)
                tilde_w.set_block(t, column_2d_array)
                for index, i in enumerate(
                        self.problem.approx_data.inner_points.KT[t]):
                    column = column_2d_array[index]
                    obj_val = np.dot(dir_im_space, column)
                    if self.problem.block_model.sub_models[i].linear is False:
                        if obj_val >= max_obj_val[i]:
                            max_obj_val[i] = obj_val
                            tilde_t_k_set[i] = t

        # select active blocks from blocks (with columns) in t_set
        for k in hat_k_set:
            t = tilde_t_k_set[k]
            if t not in tilde_t_set:
                tilde_t_set.append(t)
            if t == k:
                column = tilde_w.get_block(k)
                tilde_v.set_block(k, column)
            else:
                column_2d_array = tilde_w.get_block(t)
                index = self.problem.approx_data.inner_points.KT[t].index(k)
                column = column_2d_array[index]
                tilde_v.set_block(k, column)

        return tilde_v, tilde_w, tilde_t_set

    def create_new_hyper_block(self, check_w, duals, z, num_hyper_block=1,
                               max_size_hyper=2):
        logger.info('---------------------------------------------------------')
        logger.info('Create new hyper block')
        hat_t_set = list(self.problem.approx_data.inner_points.KT.keys())
        max_weight_z = {}
        tilde_w = BlockVector()

        # todo is it necessary to initialize resource value for linear blocks?
        for k in range(self.problem.block_model.num_blocks):
            if self.problem.block_model.sub_models[k].linear is True:
                # remove linear blocks from hat_t_set to avoid none-value
                # of z for linear blocks
                if k in hat_t_set:
                    hat_t_set.remove(k)
                tilde_w.set_block(k, check_w.get_block(k))

        for t in hat_t_set:
            z_t = z.get_block(t)
            index, value = max(enumerate(z_t), key=operator.itemgetter(1))
            max_weight_z[t] = (index, value)

        def get_max_weight_block(t_set):
            max_weight = 0
            for t in t_set:
                if max_weight_z[t][1] > max_weight:
                    max_weight = max_weight_z[t][1]
                    t_max = t
                    j_max = max_weight_z[t][0]
            return t_max, j_max

        # find the block-wise resources with the maximum z value
        while True:
            t_max, j_max = get_max_weight_block(hat_t_set)
            _, column = self.problem.approx_data.inner_points[t_max, j_max]
            kt = self.problem.approx_data.inner_points.KT[t_max]
            if len(kt) == 1:
                tilde_w.set_block(kt[0], column)
                hat_t_set_enumerate = copy.copy(hat_t_set)
                for t in hat_t_set_enumerate:
                    if kt[0] in self.problem.approx_data.inner_points.KT[t]:
                        hat_t_set.remove(t)
            else:
                for k in kt:
                    tilde_w.set_block(k, column[k])
                    hat_t_set_enumerate = copy.copy(hat_t_set)
                    # remove blocks with overlapping atomic block k with
                    # block t_max
                    for t in hat_t_set_enumerate:
                        if k in self.problem.approx_data.inner_points.KT[t]:
                            hat_t_set.remove(t)

            # finish when hat_t_set is [], find tilde_w
            if not hat_t_set:
                break
            # else:
            #     logger.info(hat_t_set)

        # calculate resource difference for each global constraints
        u_value = {}
        for m in range(self.problem.block_model.cuts.num_of_global_cuts):
            w_diff = np.array([check_w[k, m] - tilde_w[k, m] for k
                               in range(self.problem.block_model.num_blocks)])
            # print(w_diff)
            # w_diff = abs(w_diff)
            u_value[m] = sum(w_diff) * duals[m]

        # each global constraint represents one possible block aggregation
        def get_available_global_constraint():
            hat_m_set = []
            for m in range(self.problem.block_model.cuts.num_of_global_cuts):
                # extract tuple of indices of atomic blocks that have
                # variables in global constraint m
                kt_m = copy.copy(
                    self.problem.block_model.cuts.global_cuts[m].lhs.blocks)
                kt_m.sort()
                # logger.info(kt_m)
                kt_m = tuple(kt_m)
                # avoid repeated global constraints
                if kt_m not in \
                        self.problem.approx_data.inner_points.points.values():
                    # avoid too large hyper block, choose copy constraints
                    if len(kt_m) <= max_size_hyper:
                        hat_m_set.append(m)

            return hat_m_set

        hat_m_set = get_available_global_constraint()
        tilde_t_set = []
        # Create new hyper blocks by selecting global constraints with
        # the largest weighted resource difference value
        while True:
            if not hat_m_set:
                break
            u_value_hat_m = {m: u_value[m] for m in hat_m_set}
            m_max = max(u_value_hat_m.items(), key=operator.itemgetter(1))[0]
            hat_m_set.remove(m_max)
            kt_m_max = copy.copy(
                self.problem.block_model.cuts.global_cuts[m_max].lhs.blocks)
            kt_m_max.sort()
            # logger.info(kt_m_max)
            kt_m_max = tuple(kt_m_max)
            t_new, is_new_hyper_block = \
                self.problem.approx_data.inner_points.check_block(kt_m_max)
            # double check if repeated hyper block
            if is_new_hyper_block:
                tilde_t_set.append(t_new)
                logger.info('{0: <4}{1: <30}'.format(t_new, str(kt_m_max)))
                # enable limited number of hyper-blocks as output
                if len(tilde_t_set) >= num_hyper_block:
                    break

            hat_m_set_enumerate = copy.copy(hat_m_set)
            for m in hat_m_set_enumerate:
                for k in kt_m_max:
                    kt_m = copy.copy(
                        self.problem.block_model.cuts.global_cuts[m].lhs.blocks)
                    if k in kt_m:
                        # avoid overlapping atomic blocks for new hyper blocks
                        if m in hat_m_set:
                            hat_m_set.remove(m)
                            # logger.info(hat_m_set)

        # add new column according to feasible solution
        if self.result.primal_sol_point is not None:
            self.add_feasible_sol_to_inner_point(self.result.primal_sol_point,
                                                 tilde_t_set)
        return tilde_t_set

    def add_feasible_sol_to_inner_point(self, x, t_set=None):

        if t_set is None:
            t_set = list(self.problem.approx_data.inner_points.KT.keys())

        for t, kt in self.problem.approx_data.inner_points.KT.items():
            if t in t_set:
                if len(kt) == 1:
                    if self.problem.block_model.sub_models[t].linear is False:
                        self.problem.add_inner_point(
                            t, x.get_block(t),
                            self.settings.cg_min_inner_point_distance)
                else:
                    self.problem.add_inner_point(
                        t, x, self.settings.cg_min_inner_point_distance)

    def test_create_new_hyper_block(self, kt_m_max):
        # testing one hyper-block on cutting convex relaxation bound
        tilde_t_set = []
        t_new, is_new_hyper_block = \
            self.problem.approx_data.inner_points.check_block(kt_m_max)
        # double check if repeated hyper block
        if is_new_hyper_block:
            tilde_t_set.append(t_new)
            logger.info('{0: <4}{1: <30}'.format(t_new, str(kt_m_max)))
            # enable one hyper-block as output

        return tilde_t_set



