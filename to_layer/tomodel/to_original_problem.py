import logging
import numpy as np

from decogo.model.input_model_base import OriginalProblemBase
from decogo.util.block_vector import BlockVector
from decogo.model.input_model_base import CutPoolCG

from to_layer.utils.utils import create_random_point, reward_function, penalization_function

logger = logging.getLogger("decogo")


class TOOriginalProblem(OriginalProblemBase):

    adding_points_to_ia = 50
    used_simp_iter_for_fast = 10

    pertubation_threshold: tuple = (0.2, 0.2)
    pertubation_range = 0.6

    infeasible_pertubated_points = 0

    def __init__(self, model, cuts: CutPoolCG):

        super().__init__()

        self.input_model = model

        self.model = model.model

        self.cuts = cuts

        self.ele_list = list(self.model.base_model.elements.keys())

    def trans_to_orig_space(self, point: BlockVector):
        _x = np.array([y_k[:len(self.model.sub_domains[block_id + 1].Elements)] for block_id, y_k in point.vectors.items()])
        _x = np.reshape(_x, (_x.size,))

        # TODO: Not completely done!
        _u = np.array([y_k[len(self.model.sub_domains[block_id + 1].Elements):] for block_id, y_k in point.vectors.items()])

        return _x, _u

    def local_solve(self, start_point: BlockVector, result, problem, iter=None,
                    **kwargs):

        _x_start, _u_start = self.trans_to_orig_space(start_point)

        self.model.base_model.SimpProblem.max_main_iterations = 100
        try:
            # penalization section
            if self.input_model.penalization_approach:
                _x_start = reward_function(_x_start, y_p=self.input_model.penalization_factor)

            _name = None

            _x, _u, _obj = self.model.base_model.SimpProblem.solve(_x_start, output=True, model_name=_name)

            # penalization sections
            if self.input_model.penalization_approach:
                _x = penalization_function(_x, y_p=2)
                _obj += sum(_x)

            if result.primal_bound > _obj:
                result.set_new_primal_bound(_obj, np.concatenate((_x, _u)))

        except ZeroDivisionError:

            logger.info("Can not solve original SIMP-Problem due to presented initial values!")

    def __check_point__(self, _x: np.array, _u: np.array):

        if self.input_model.model.base_model.FEModel.check_displacements(_u) is False:
            self.infeasible_pertubated_points += 1
            logger.info("Pertubated point is not feasible due to violating displacement bounds!")
            return False

        y = BlockVector()

        x_indices = np.array(list(self.model.base_model.elements.keys()))

        for sub_domain_id, sub_domain in self.model.sub_domains.items():
            _eles = list(sub_domain.Elements.keys())
            _indices = np.array([np.where(e == x_indices)[0][0] for e in _eles]).squeeze()
            x_domain = _x[_indices]
            u_domain = _u[np.array(sub_domain.Dofs)[:] - 1]
            y.set_block(sub_domain_id - 1, np.concatenate((x_domain, u_domain)))

        checker = np.array([cut.eval(y) for cut in self.cuts.global_cuts])

        if np.any(checker != 0):
            logger.info("Pertubated point is not feasible because local constraints are violated!\n"
                        "violations: {}".format(checker))
            self.infeasible_pertubated_points += 1
            return False
        else:
            logger.info("Found Feasible Point!")
            return True

    def get_blockwise_point(self, _x, _u) -> np.array:

        y = []
        for domain_id, sub_domain in self.model.sub_domains.items():
            u_domain = _u[np.array(sub_domain.Dofs)[:] - 1]
            eles = list(sub_domain.Elements.keys())
            e_indices = [self.ele_list.index(i) for i in eles]
            x_domain = _x[e_indices]
            # penalize x_domain
            if self.input_model.penalization_approach:
                x_domain = penalization_function(x_domain, y_p=self.input_model.penalization_factor)
            y.append(np.concatenate((x_domain, u_domain)).tolist())

        return np.array(y)

    # start_point is  in image space
    # it is just more to find a feasible point of the original problem than calculate the complete model with simp
    def local_solve_fast(self, start_point: BlockVector, result, problem,
                         iter=None, **kwargs):

        self.model.base_model.SimpProblem.max_main_iterations = self.used_simp_iter_for_fast

        self.model.base_model.SimpProblem.shape = (4, 4)

        x_start, u_start = self.trans_to_orig_space(start_point)

        _x, _u, _c = self.model.base_model.SimpProblem.solve(x_start, output=False)

        if self.input_model.integer:
            _x, _u, _c = self.input_model.model.base_model.FEModel.transform_relaxed_point(_x)

        if self.input_model.penalization_approach:
            _x_initial = penalization_function(_x, self.input_model.penalization_factor)
            _y_initial = np.concatenate((_x_initial, _u))
            _c_initial = _c + _x_initial.sum()
        else:
            _x_initial = _x
            _y_initial = np.concatenate((_x_initial, _u))
            _c_initial = _c

        # adjust rhs of volume constraint in accordance to the one constraint
        # self.cuts.global_cuts[len(self.model.copies)].rhs = _x_initial.sum()
        # set a first primal bound
        result.set_new_primal_bound(_c_initial, _y_initial)

        # set inner points of primal bound to IA
        y = self.get_blockwise_point(_x_initial, _u)
        for i in range(len(self.model.sub_domains)):
            problem.add_inner_point(i, y[i],
                                    min_inner_point_dist=self.input_model.settings.cg_min_inner_point_distance)

        # Create inner points due to pertubation to make LP-IA more flexible in accordance to
        # density distribution
        for i in range(self.adding_points_to_ia):

            # return not penalized x
            x_pert, u_pert = create_random_point(self.model.base_model.FEModel, _x,
                                                 threshold=self.pertubation_threshold, f_range=self.pertubation_range,
                                                 binary=self.input_model.integer)

            if self.__check_point__(x_pert, u_pert) is True:

                y = self.get_blockwise_point(x_pert, u_pert)

                for j in range(len(self.model.sub_domains)):
                    # add an inner point to LP-IA
                    problem.add_inner_point(j, y[j],
                                            min_inner_point_dist=self.input_model.settings.cg_min_inner_point_distance)

        logger.info("Pertubation Statistics: {} of {} points are infeasible\n".format(self.infeasible_pertubated_points,
                                                                                      self.adding_points_to_ia))
