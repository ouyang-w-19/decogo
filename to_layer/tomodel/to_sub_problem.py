import logging
import numpy as np

from decogo.model.input_model_base import SubProblemsBase

from to_layer.tomodel.to_sub_model import TOSubModel
from to_layer.utils.utils import penalization_function, reward_function, create_random_point
from to_layer.pyomo.global_solver import GlobalSolver

logger = logging.getLogger("decogo")


class TOSubProblem(SubProblemsBase):

    _global_solver : GlobalSolver = None

    sub_gradient_iter = 0
    column_number = 10
    threshold = 0.2

    temp_columns = []

    def __init__(self, sub_models, cuts, block_id, settings):

        self.block_id = block_id
        self.settings = settings
        self.integer = sub_models[block_id].integer
        self.cuts = cuts
        self.sub_model: TOSubModel = sub_models[self.block_id]

        self._global_solver = GlobalSolver(self.sub_model.sub_domain.FEModel)

        super().__init__(self.block_id)

    def solve_by_simp(self, _y_tilde: np.ndarray, _direction: np.ndarray = None):

        self.temp_columns = []

        self.sub_model.sub_domain.SubSimpProblem.shape = (2, 2)  # TODO: Configure Shape for SubDomains

        if _y_tilde is not None:
            _x = _y_tilde[:len(self.sub_model.sub_domain.Elements)]

            # include penalization
            # decogo provide a penalized density distribution
            if self.sub_model.inp_model.penalization_approach:
                _x = reward_function(_x, y_p=self.sub_model.inp_model.penalization_factor)

            _u = _y_tilde[len(self.sub_model.sub_domain.Elements):]
            self.sub_model.sub_domain.FEModel.u_base = _u
            # get current boundary forces depending on x_init and u
            _g = self.sub_model.sub_domain.get_boundary_forces(_x, _u, method='ku')[1]
        else:
            # determine initial homogeneous density distribution
            _x = np.ones((len(self.sub_model.sub_domain.Elements)))[:] *\
                 [self.sub_model.sub_domain.SubSimpProblem.volfrac]
            # take initial u from the displacements of the base model
            _u = self.sub_model.inp_model.model.base_model.FEModel.U[np.array(self.sub_model.sub_domain.Dofs)[:] - 1]
            # set basic u for indeterminate systems
            self.sub_model.sub_domain.FEModel.set_bounds(_u)
            _g = self.sub_model.sub_domain.FEModel.boundary_conditions.boundary_forces_vec

        # incorporate direction vector to simp
        # direction equals f from original objective function so there are no boundary forces
        # hence the relevant force vector is _direction + _g
        if _direction is not None:
            if self.sub_model.inp_model.use_cg_stabilization:
                _direction = self.stabilize_direction(_direction)
            _G = _direction[len(self.sub_model.sub_domain.Elements):]  # + _g
        else:
            _G = self.sub_model.sub_domain.FEModel.boundary_conditions.outer_forces_vec + _g

        # print(_x)
        # solve the sub-domain by simp # TODO: rename d_k parameter to h_k = (d_k + g_k); Test only d_k
        _x_new, _u_new, _obj_new = self.sub_model.sub_domain.SubSimpProblem.solve(_x, d_k=_G, output=False)

        # _x_new, _u_new, _obj_new = \
        #     self.sub_model.sub_domain.FEModel.incorporate_one_constraint(_x_new, self.sub_model.one_constraint)

        if self.sub_model.inp_model.use_cg_stabilization:
            _u_new = self.stabilize_displacements(_u_new)

        # penalize x-simp
        if self.sub_model.inp_model.penalization_approach:
            _x_new = penalization_function(_x_new, y_p=self.sub_model.inp_model.penalization_factor)
            _obj_new += _x_new.sum()

        if self.sub_model.integer:
            _x_new, _u_new, _obj_new = self.sub_model.sub_domain.FEModel.transform_relaxed_point(_x_new)

        return _x_new, _u_new, _obj_new

    # Is called for CG and fast CG
    # or rather solving without using the direction
    def local_solve(self, result, direction, start_point=None, **kwargs):

        # include argument problem into kwargs
        if 'problem' in kwargs:
            problem = kwargs['problem']
        else:
            problem = None

        try:
            x_new, u_new, obj_new = self.solve_by_simp(start_point, _direction=direction)

            y = np.concatenate((x_new.round(), u_new))

            feasible = self.sub_model.sub_domain.FEModel.check_displacements(u_new)

            self.add_pertubated_columns(problem, x_new)

        except ZeroDivisionError:
            logger.info("SIMP-SubProblem is not solved! There were illogical initial values provided by Decogo!")
            y = np.zeros((len(self.sub_model.vars_in_block), ))
            obj_new = float('inf')
            feasible = False

        # y_new, primal bound, dual bound, is y_new feasible
        return y, obj_new, obj_new, feasible

    # ---------------------------------------

    # Is called for sub-gradient
    # or rather solver depends on direction
    # direction is already q = d^T \cdot A_k
    def global_solve(self, result, direction, start_point=None, **kwargs):

        # include argument problem into kwargs
        if 'problem' in kwargs:
            problem = kwargs['problem']
        else:
            problem = None

        self.sub_gradient_iter += 1
        if start_point is None:
            if problem.get_min_inner_point(self.block_id, direction)[1] != float('inf'):
                start_point = problem.get_min_inner_point(self.block_id, direction)[0]
        try:
            if self.sub_gradient_iter == 1:
                _d = direction
            else:
                _d = None
            x_new, u_new, obj_new = self.solve_by_simp(start_point, _direction=direction)

            y = np.concatenate((x_new, u_new))

            feasible = self.sub_model.sub_domain.FEModel.check_displacements(u_new)

        except ZeroDivisionError:
            logger.info("SIMP-SubProblem is not solved! There were illogical initial values provided by Decogo!")
            y = np.zeros((len(self.sub_model.vars_in_block), ))
            obj_new = float('inf')
            feasible = False

        # y_new, primal bound, dual bound, is y_new feasible
        return y, obj_new, obj_new, feasible

    def stabilize_direction(self, dk):

        fk = self.sub_model.sub_domain.FEModel.boundary_conditions.outer_forces_vec
        gk = self.sub_model.sub_domain.FEModel.boundary_conditions.boundary_forces_vec

        hk = fk + gk

        for (i, ), hki in np.ndenumerate(hk):

            if dk[len(self.sub_model.sub_domain.Elements) + i] > hki + self.sub_model.inp_model.delta:

                dk[len(self.sub_model.sub_domain.Elements) + i] = hki + self.sub_model.inp_model.delta

            elif dk[len(self.sub_model.sub_domain.Elements) + i] < hki - self.sub_model.inp_model.delta:

                dk[len(self.sub_model.sub_domain.Elements) + i] = hki - self.sub_model.inp_model.delta

        return dk

    def stabilize_displacements(self, uk):

        for (i,), uki in np.ndenumerate(uk):

            if uki > self.sub_model.bar_uk[i] + self.sub_model.inp_model.eps:

                uk[i] = self.sub_model.bar_uk[i] + self.sub_model.inp_model.eps

            elif uki < self.sub_model.bar_uk[i] - self.sub_model.inp_model.eps:

                uk[i] = self.sub_model.bar_uk[i] - self.sub_model.inp_model.eps

        return uk

    def add_pertubated_columns(self, problem, x: np.array):
        logger.info("Adding pertubated columns for Sub-Problems")
        for i in range(5):
            x_pert, u_pert = create_random_point(self.sub_model.sub_domain.FEModel, x,
                                                 threshold=(0.2, 0.2), f_range=0.4,
                                                 binary=self.sub_model.integer,
                                                 ones=self.sub_model.one_constraint)

            problem.add_inner_point(self.block_id, np.concatenate((x_pert, u_pert)))
