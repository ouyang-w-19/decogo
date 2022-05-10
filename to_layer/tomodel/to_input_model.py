import numpy as np

from decogo.model.input_model_base import InputModelBase
from decogo.model.input_model_base import CutPoolCG
from decogo.solver.settings import Settings
from decogo.model.constraints import ObjectiveFunction, LinearConstraint
from decogo.util.block_vector import BlockVector

from to_layer.tomodel.to_reformulated_user_model import TOReformulatedUserModel
from to_layer.tomodel.to_sub_model import TOSubModel
from to_layer.tomodel.to_sub_problem import TOSubProblem
from to_layer.tomodel.to_original_problem import TOOriginalProblem
from to_layer.utils.utils import penalization_function


class TOInputModel(InputModelBase):

    # Zero Displacements Constraints
    zeros_consideration: bool = False
    # -----------------------------
    # Penalization Region
    penalization_approach: bool = False
    penalization_factor = 2
    # -----------------------------
    # CG-Stabilization
    use_cg_stabilization: bool = False
    delta: float = 0
    eps: float = 0
    x_bar: np.array = None
    u_bar: np.array = None
    g_bar: np.array = None
    # -----------------------------
    # Integer Consideration
    integer: bool = False
    # -----------------------------
    # Bounds
    # Displacements
    u_max: float = None
    u_min: float = None
    # Densities
    x_max = None
    x_min = 0
    # -----------------------------

    def __init__(self, inp_model: TOReformulatedUserModel):
        # preprocessing
        self.model = inp_model
        self.settings = Settings()
        self.blocks = self.model.blocks
        self.block_sizes = self.model.block_sizes
        num_blocks = len(self.blocks)
        self.sense = 1
        self.__get_bounds__()
        # end preprocessing
        self.one_constraint = self.get_global_one_constraint()
        # cut construction
        block_sizes, blocks, obj, global_cuts, local_cuts = self._construct_cut_pool()
        self.cuts = CutPoolCG(block_sizes=block_sizes, blocks=blocks, obj=obj,
                              global_cuts=global_cuts, local_cuts=local_cuts)

        # end cuts construction

        sub_models = [TOSubModel(self, blocks[block_id], block_id)
                      for block_id in range(num_blocks)]

        sub_problems = [TOSubProblem(sub_models, self.cuts, block_id, self.settings)
                        for block_id in range(num_blocks)]

        original_problem = TOOriginalProblem(self, self.cuts)

        super().__init__(sub_problems, original_problem, self.cuts, sub_models)

    def get_global_one_constraint(self):
        bm = self.model.base_model
        ones = []
        for node in bm.FEModel.boundary_conditions.outer_forces:
            for i, e in bm.elements.items():
                if node in e.Nodes:
                    ones.append(list(bm.elements.keys()).index(i))

        for node in bm.FEModel.boundary_conditions.fixed_nodes:
            for i, e in bm.elements.items():
                if node in e.Nodes:
                    ones.append(list(bm.elements.keys()).index(i))

        return ones

    def _construct_cut_pool(self):
        block_sizes = self.block_sizes
        blocks = self.blocks
        block_number = len(self.block_sizes)

        # Objective Function
        if self.penalization_approach:
            obj = ObjectiveFunction(self.model.obj_coefficients, self.block_sizes, 0)
        else:
            obj = ObjectiveFunction(self.model.f_coefficients, self.block_sizes, 0)
        # ---------------------------------------------------------------------

        global_cuts = []
        local_cuts = {}

        # Global Cuts
        # copy constraints
        for i in self.model.copies:
            global_cuts.append(LinearConstraint(i, "=", 0, self.block_sizes))
        # ---------------------------------------------------------------------
        # zero constraints could be global cuts
        """
        if self.zeros_consideration:
            for i in self.model.zeros:
                global_cuts.append(LinearConstraint(i, "=", 0, self.block_sizes))
        """
        # ---------------------------------------------------------------------

        # global volume constraint
        # TODO: implement explicit volumes of elements
        # right hand side of constraint
        if self.penalization_approach is False:
            rhs = len(self.model.base_model.elements) * self.model.base_model.SimpProblem.volfrac
        else:
            rhs = penalization_function(np.array([self.model.base_model.SimpProblem.volfrac] *
                                                 len(self.model.base_model.elements)),
                                        y_p=self.penalization_factor).sum()

        global_cuts.append(LinearConstraint(self.model.volumes, "<=",
                                            rhs,
                                            self.block_sizes))

        # One-Constraint: Maybe not working well?
        """
        for i, j in enumerate(self.model.ones):
            global_cuts.append(LinearConstraint(j, "=", 1, self.block_sizes))
        """
        # ---------------------------------------------------------------------
        # Local Constraints
        """"
        for i, j in enumerate(self.model.ones):
            if j[0][0] in local_cuts:
                local_cuts[j[0][0]].append(LinearConstraint(j, "=", 1, self.block_sizes))
            else:
                local_cuts[j[0][0]] = [LinearConstraint(j, "=", 1, self.block_sizes)]
        """
        # ---------------------------------------------------------------------
        return block_sizes, blocks, obj, global_cuts, local_cuts

    # TODO: Check Correctness! or rather check if any other definitions of bounds exists
    def __get_bounds__(self):

        # Density Bounds
        if self.penalization_approach:
            self.x_max = penalization_function(np.array([0.5]))[0] * 1.1
        else:
            self.x_max = 1

    def get_c(self, _x: np.array, _u: np.array) -> float:
        y = self.get_block_vector(_x, _u)

        _c = self.cuts.obj.eval(y)

        return _c

    def get_block_vector(self, _x: np.array, _u: np.array) -> BlockVector:

        y = BlockVector()

        e_list = list(self.model.base_model.elements.keys())

        for domain_id, domain in self.model.cells.items():
            domain_eles = np.array(list(domain.Elements.keys()))
            x_block = _x[np.array([np.where(e_list == de) for de in domain_eles]).flatten()]
            u_block = _u[np.array(domain.Dofs)[:] - 1]
            y_block = np.concatenate((x_block, u_block))
            y.set_block(domain_id - 1, y_block)

        return y

    def configure(self, _config: dict):
        # configure Simp Problems

        _simp_config: dict = _config["SimpProblem"]
        # Attention also update problems of sub-domains
        # base model
        base_problem = self.model.base_model.SimpProblem.configure(_simp_config)

        # sub domains
        for domain_id, domain in self.model.cells.items():
            domain.SubSimpProblem.configure(_simp_config)

        # Pertubation Section
        _pert_config = _config["Pertubation"]
        self.original_problem.adding_points_to_ia = _pert_config["adding_points"]
        self.original_problem.used_simp_iter_for_fast = _pert_config["fast_sol_simp_iter"]
        self.original_problem.pertubation_threshold = _pert_config["threshold"]
        self.original_problem.pertubation_range = _pert_config["force_range"]

        # Penalization Approach
        if _config["use_penalization_approach"]:
            self.penalization_approach = True
            self.penalization_factor = _config["CGPenalization"]["factor"]

        # Stabilizer Section
        if _config["use_stabilizer"]:
            self.use_cg_stabilization = True
            self.delta = _config["CGStabilizer"]["delta"]
            self.eps = _config["CGStabilizer"]["eps"]

        # general section
        if _config["integer_consideration"]:
            self.integer = True
