"""Implements OA algorithm for convex problems"""

import copy
import logging
import time

from decogo.solver.settings import Settings
from decogo.util.block_vector import BlockVector
from decogo.solver.colgen import AlgorithmBase

logger = logging.getLogger('decogo')


class OaSolver(AlgorithmBase):
    """Class which implements OA method for convex problems

    :param problem: Decomposed problem class, which stores all input data
    :type problem: DecomposedProblem
    :param settings: Settings class
    :type settings: Settings
    :param result: Class which stores the results
    :type result: Results
    :param x_center: Point inside of the feasible nonlinear set, which is \
    used for the line search
    :type x_center: BlockVector or None

    .. Note::
        If there are any numerical instability (infeasible OA after some
        iterations, no improvement of OA etc), the following things should be
        checked:

        * Do all variables have the bounds? If not, at least try to estimate \
        them;
        * Are the linearization cuts added using the points from local \
        optimization? If yes, then don't add them;
        * Check the sign of new constraints of the reformulation, i.e. switch \
        from :math:`==` to :math:`\\leq` in decomposer.
    """

    def __init__(self, problem, settings, result):
        """Constructor method"""
        super().__init__(problem, settings, result)
        self.x_center = None  # the interior point

    def solve(self):
        """Main method which calls all necessary methods for the OA algorithm.
        See papers for more info"""
        logger.info('\nInitialization')
        self.init_oa()

        timer = time.time()
        hat_x = self.solve_oa()

        logger.info('\nMain algorithm')
        logger.info('{0: <7}{1: <25}{2: <20}'.format('iter', 'dual bound',
                                                     'primal bound'))

        while True:
            self.result.num_iter += 1

            tilde_x, primal_bound, prim_sol_is_feasible = self.local_solve(
                hat_x)

            if self.result.get_gap(self.result.primal_bound,
                                   self.result.dual_bound) <= \
                    self.settings.oa_eps_rel_obj_val:
                logger.info(
                    '{0: <7}{1: <25}{2: <20}'.format(
                        self.result.num_iter,
                        round(self.result.sense * self.result.dual_bound, 10),
                        round(self.result.sense * self.result.primal_bound,10)))

                logger.info('\nEXIT: gap is closed')
                break

            self.cut_refine(hat_x)
            self.fix_and_refine(tilde_x)

            hat_x = self.solve_oa()

            logger.info(
                '{0: <7}{1: <25}{2: <20}'.format(
                    self.result.num_iter,
                    round(self.result.sense * self.result.dual_bound, 10),
                    round(self.result.sense * self.result.primal_bound, 10)))

            if self.result.num_iter >= self.settings.oa_max_iter:
                logger.info('\nEXIT: maximum number of iterations exceeded')
                break

            if self.result.get_gap(self.result.primal_bound,
                                   self.result.dual_bound) <= \
                    self.settings.oa_eps_rel_obj_val:
                logger.info('\nEXIT: gap is closed')
                break

        timer = time.time() - timer
        self.result.main_alg_time = timer

    def init_oa(self):
        """Initial phase of OA algorithm, which solves only LP OA master
        problems"""
        timer = time.time()
        self.problem.compute_gradients()

        dual_bound_prev = self.result.dual_bound
        num_iter = 0

        logger.info('{0: <7}{1: <25}'.format('iter', 'LP relaxation of MIP'))

        while True:
            num_iter += 1

            hat_x = self.solve_lp_oa()

            hat_y = self.project(hat_x)
            self.problem.add_linearization_cuts(hat_y,
                                                self.settings.oa_eps_active_constraint,
                                                hat_x)

            logger.info(
                '{0: <7}{1: <25}'.format(num_iter,
                                         self.result.sense * self.result.dual_bound))

            if abs(dual_bound_prev - self.result.dual_bound) <= \
                    self.settings.oa_eps_start:
                break

            dual_bound_prev = self.result.dual_bound
        logger.info('LP relaxation: {0}\n'.format(self.result.sense *
                                                  self.result.dual_bound))

        self.solve_nlp_const_obj(hat_x)

        # solve nlp problem without fixing the integer variables
        self.add_unfixed_nlp_cuts(hat_x)

        # perform line search
        if self.settings.oa_line_search:
            logger.info('LP relaxation with line search')
            dual_bound_prev = float('inf')
            num_iter = 0
            while True:
                num_iter += 1

                hat_x = self.solve_lp_oa()

                self.add_line_search_cuts(hat_x, self.x_center)

                hat_y = self.project(hat_x)
                self.problem.add_linearization_cuts(hat_y,
                                                    self.settings.oa_eps_active_constraint)

                logger.info(
                    '{0: <7}{1: <25}'.format(num_iter,
                                             self.result.sense * self.result.dual_bound))

                if abs(dual_bound_prev - self.result.dual_bound) <= \
                        self.settings.oa_eps_start:
                    break

                dual_bound_prev = self.result.dual_bound

        timer = time.time() - timer
        self.result.init_time = timer

    def solve_oa(self):
        """Solves MIPOA master problem

        :return: Solution point
        :rtype: BlockVector
        """
        # make timing here, if necessary
        hat_x, dual_obj_val = \
            self.problem.master_problems.solve_mip_oa(
                solver_name=self.settings.mip_solver)
        self.result.dual_bound = dual_obj_val

        return hat_x

    def local_solve(self, hat_x):
        """Solves NLP master problem with fixed integer variables

        :param hat_x: Pint for fixing integer variables and starting point
        :type hat_x: BlockVector
        :return: Solution point, objective value and flag if the solution \
        point is infeasible
        :rtype: tuple
        """
        tilde_x, primal_bound, prim_sol_is_feasible = \
            self.problem.master_problems.nlp_solve(self.settings.nlp_solver,
                                                   point_to_fix=hat_x,
                                                   start_point=hat_x)
        # this could cause numerical instability,
        # i.e. after adding cuts from fixed NLP the OA master problem can
        # become infeasible
        self.problem.add_linearization_cuts(tilde_x,
                                            self.settings.oa_eps_active_constraint,
                                            x=hat_x)

        if prim_sol_is_feasible is True:
            self.result.set_new_primal_bound(primal_bound, tilde_x)

        return tilde_x, primal_bound, prim_sol_is_feasible

    def project(self, hat_x, block_id=None):
        """Solves projection sub-problems

        :param hat_x: Point to project
        :type hat_x: BlockVector
        :param block_id: If it is not ``None``, then it performs projection \
        for one blocks, otherwise - for all
        :type block_id: int or None
        :return: Solution of projection sub-problems
        :rtype: BlockVector
        """
        start_time = time.time()

        try:
            if block_id is None:
                y = BlockVector(self.problem.block_model.block_sizes)
                for block_id in range(self.problem.block_model.num_blocks):
                    y_sol_k, _, _ = \
                        self.problem.sub_problems[block_id].nlp_proj_solve(
                            solver_name=self.settings.nlp_solver,
                            point_to_project=hat_x.get_block(block_id))
                    y.set_block(block_id, y_sol_k)
            else:
                # if k is not None we pass here x_hat as a local vector, i.e.
                # hat_x_k and we have similar result - y_k
                y, _, _ = \
                    self.problem.sub_problems[block_id].nlp_proj_solve(
                        solver_name=self.settings.nlp_solver,
                        point_to_project=hat_x)

        except ValueError as e:
            if e.args[0] == \
                    'Cannot load a SolverResults object with bad status: error':
                logger.info('Ipopt exited with the error during projection '
                            'step. Skipping adding the linearization cuts')
            y = hat_x

        self.result.add_sub_problem_time(time.time() - start_time)

        return y

    def cut_refine(self, hat_x):
        """Calls methods for refinement of OA with projection and line search

        :param hat_x: Infeasible point regarding nonlinear set
        :type hat_x: BlockVector
        """
        y_hat = self.project(hat_x)
        self.problem.add_linearization_cuts(y_hat,
                                            self.settings.oa_eps_active_constraint,
                                            x=hat_x)

        if self.settings.oa_line_search:
            self.add_line_search_cuts(hat_x, self.x_center)

    def solve_lp_oa(self):
        """Solves intger relaxation of MIPOA master problem

        :return: Solution point
        :rtype: BlockVector
        """
        # make timing here, if necessary
        x_hat, obj_val, duals = \
            self.problem.master_problems.solve_integer_relaxed_oa(
                solver_name=self.settings.lp_solver)
        self.result.dual_bound = obj_val

        return x_hat

    def solve_nlp_const_obj(self, hat_x):
        """Solve the NLP problem with zero objective vector
        in order to get the interior point for performing the line search

        :param hat_x: Starting point
        :type hat_x: BlockVector
        """
        # make timing here, if necessary
        cut_direction = BlockVector(
            self.problem.block_model.block_sizes)  # zero objective
        x_center, obj_val, sol_is_feasible = \
            self.problem.master_problems.nlp_solve(self.settings.nlp_solver,
                                                   start_point=hat_x,
                                                   cut_direction=cut_direction)
        self.x_center = x_center

    def fix_and_refine(self, tilde_x):
        """Performs fix-and-refine procedure, which solves fixed MIPOA
        sub-problems with slacks and projection sub-problems. See paper for
        more info

        :param tilde_x: Point to fix
        :type tilde_x: BlockVector
        :return: Solution point from MIPOA sub-problems and slacks
        :rtype: tuple
        """
        if self.settings.oa_fix_and_refine:
            hat_x = copy.deepcopy(tilde_x)

            start_time = time.time()

            i = 0
            while True:
                # list of booleans that says if the slacks at each block
                # iteration were zero or not
                slacks = []

                for k in range(self.problem.block_model.num_blocks):
                    hat_y_k = self.project(hat_x.get_block(k), k)
                    self.problem.add_linearization_cuts(hat_y_k,
                                                        self.settings.oa_eps_active_constraint,
                                                        block_id=k)

                    # make timing, if necessary
                    hat_x, obj_val, slacks_are_zero = \
                        self.problem.master_problems.solve_mipoa_with_slacks(
                            solver_name=self.settings.mip_solver,
                            x=hat_x, block_id=k)

                    slacks.append(slacks_are_zero)

                i += 1

                if self.int_changed(hat_x, tilde_x) is False:
                    break

                tilde_x = hat_x
            self.result.add_sub_problem_time(time.time() - start_time)

            return hat_x, slacks

    def int_changed(self, point1, point2):
        """Checks if the values of integer variables between two points are
        changed

        :param point1: First point
        :type point1: BlockVector
        :param point2: Second point
        :type point2: BlockVector
        :return: ``True`` if changed, ``False`` - otherwise
        :rtype: bool
        """
        for k in range(self.problem.block_model.num_blocks):
            for i, var in enumerate(
                    self.problem.block_model.sub_models[k].variables):
                if var.type == 'Integers' or var.type == 'Binary':
                    if point1[k, i] != point2[k, i]:
                        return True

        return False

    def add_line_search_cuts(self, hat_x, star_x):
        """Performs line-search between two points. At resulting point it adds
        linearization cuts

        :param hat_x: Point outside of the feasible nonlinear set
        :type hat_x: BlockVector
        :param star_x: Point inside of the feasible nonlinear set
        :type star_x: BlockVector
        """
        # make timing here if necessary
        alpha = []
        y = BlockVector(self.problem.block_model.block_sizes)

        start_time = time.time()
        try:
            for k in range(self.problem.block_model.num_blocks):
                alpha_k, y_k = self.problem.sub_problems[
                    k].solve_line_search_subproblem(
                    self.settings.nlp_solver, hat_x.get_block(k),
                    star_x.get_block(k))
                alpha.append(alpha_k)
                y.set_block(k, y_k)
        except ValueError as e:
            if e.args[0] == 'Cannot load a SolverResults object with bad ' \
                            'status: error':
                logger.info('Skipping line search in this iteration because of '
                            'sub-solver error')
                return

        self.result.add_sub_problem_time(time.time() - start_time)

        self.problem.add_linearization_cuts(y,
                                            self.settings.oa_eps_active_constraint,
                                            x=hat_x)

    def add_unfixed_nlp_cuts(self, hat_x):
        """Solve NLP problem without fixing the integer variables
        and adds cuts at the result

        :param hat_x: Starting point
        :type hat_x: BlockVector
        """
        # make timing here, if necessary

        bar_x, upper_bound, sol_is_feasible = \
            self.problem.master_problems.nlp_solve(
                solver_name=self.settings.nlp_solver, start_point=hat_x)

        # adds just cuts at x_bar
        self.problem.add_linearization_cuts(bar_x,
                                            self.settings.oa_eps_active_constraint)
