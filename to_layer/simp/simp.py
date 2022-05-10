import numpy as np
import os

from to_layer.fea.fea import FEModel
from to_layer.simp.output import SimpOutput
from to_layer.elements.element import Element


"""
Requirements: elements (K_e) and total stiffness matrices (K); initial value for volume fracture; penalty factor p;
filter size r_min
optional parameters: max. number of iterations
Main loop:
    1: FE-Analysis
    2: Objective function and sensitivity
    3: Filtering sensitivity
    4: Design update with optimal criteria method
    5: print results and plot densities
"""


class SimpProblem:
    # User defined Parameters
    volfrac: float = 0.44
    rmin: float = 1.5
    loop: int = 0
    Emin: float = 1e-9
    Emax: float = 1.0
    p: int = 3
    filter = "sensitivity"
    eta: float = 0.5
    max_main_iterations: int = 50
    # ---------------------------
    H: np.array = None
    FE_Model: FEModel = None
    # Volume Section
    V0: float = None
    V: float = None
    # Output Section
    out: SimpOutput = None
    save_out: bool = False

    shape: tuple = None

    feasible_solution = False

    def solve(self, x_init, d_k=None, output=False, model_name: str = 'test'):

        if output:
            self.setup_output(name=model_name)

        self.loop = 0
        c = None
        u = None
        g_oc = 0
        x_old = x_init
        x_new = x_old.copy()
        change = 1

        for i, (e_id, element) in enumerate(self.Elements.items()):
            element.x = x_init[i]
        # incorporate decogo direction
        if d_k is not None:
            self.FE_Model.F = d_k

        # determine initial volume
        self.V0 = self.get_v(x_init)

        while not self.loop == self.max_main_iterations and change >= 1e-3:

            self.loop += 1
            # update elements stiffness matrices
            for i, (e_id, element) in enumerate(self.Elements.items()):
                element.update_stiffness_matrix(e_min=self.Emin, e_max=self.Emax, p=self.p)
            # FEA
            # update domain's stiffness matrix
            self.FE_Model.K = self.FE_Model.get_k()
            # inc. boundary conditions to new K
            if len(self.FE_Model.boundary_conditions.fixed_nodes) > 0:
                self.FE_Model.K, self.FE_Model.F = self.FE_Model.incorporate_boundary_conditions(self.FE_Model.K,
                                                                                                 self.FE_Model.F)
            # solve and get u
            u, self.feasible_solution = self.FE_Model.solve()
            # a false feasible solution can indicate a static undetermined system
            # update elements properties
            for e_id, element in self.Elements.items():
                element.update_element_displacements(u, np.array(self.FE_Model.global_dofs))
                element.update_flexibility()
                element.derive_flexibility(p=self.p, e_max=self.Emax, e_min=self.Emin)
            # calc current objective
            c = np.dot(np.dot(u.T, self.FE_Model.K), u)

            # apply filter for each element
            for j, (e_id, element) in enumerate(self.Elements.items()):
                element.apply_sensitivity_filter(self.Elements, self.H[j])

            dc = np.array([element.dCe_filtered for e_id, element in self.Elements.items()])
            x_old = np.array([element.x for e_id, element in self.Elements.items()])

            if output and self.loop == 1:
                self.out.update(self.loop, c, x_new, change)

            # optimality criteria
            x_new, g_oc = self.__oc__(x_old, dc, g_oc)

            # update elements densities
            for i, (e_id, element) in enumerate(self.Elements.items()):
                element.x = x_new[i]
            # update change
            change = np.linalg.norm(x_new - x_old, np.inf)

            if output:
                self.out.update(self.loop, c, x_new, change)

        if output:
            self.out.close_figure()

        return x_new, u, c

    def __oc__(self, x_old, dc, g_oc):
        gt = 0
        l1 = 0
        l2 = 1e9
        move = 0.2
        eta = 0.5

        x_new = np.zeros_like(x_old)
        while (l2 - l1) / (l1 + l2) > 1e-3:

            lmid = 0.5 * (l2 + l1)
            x_new[:] = np.maximum(1e-3,
                                  np.maximum(x_old - move,
                                             np.minimum(1.0, np.minimum(x_old + move, x_old * (-dc / lmid) ** eta))))
            gt = g_oc + np.sum((x_new - x_old))

            # actives = np.array([0, 3, 12])

            # x_new[actives] = 1

            # gt = self.get_v(x_new) - self.V0
            if gt > 0:
                l1 = lmid
            else:
                l2 = lmid

        return x_new, gt

    def __set_convolutional_operator__(self, el_i: Element):
        hj = np.zeros((len(self.Elements), ))

        for n_id, n in el_i.neighbours.items():
            if n_id in self.Elements.keys():
                i = self.ListElements.tolist().index(n_id)
                hj[i] = self.rmin - np.linalg.norm(el_i.centroid - n.centroid)
        return hj

    def setup_output(self, name):
        self.out = SimpOutput(name=name)

        self.out.design_shape = self.shape
        # self.out.solution_path = os.path.join(self.out.solutions_path, name)

    def configure(self, _config: dict):
        self.volfrac = _config["volfrac"]
        self.p = _config["penalization_factor"]
        self.Emin = _config["emin"]
        self.Emax = _config["emax"]
        self.rmin = _config["rmin"]
        self.filter = _config["filter"]

    def get_v(self, _x: np.array):
        return sum([e.V * _x[i] for i, (eid, e) in enumerate(self.Elements.items())])

    def __init__(self, nnodes: int, eles: dict, fe_model: FEModel):

        # Dimension section
        self.NNodes = nnodes
        self.Nodes = list(range(self.NNodes))
        self.DoFs = list(range(self.NNodes * 2))  # TODO: Replace 2 with dof per node number
        # end Dimension section
        # Element section
        self.Elements = eles
        self.ListElements = np.array(list(self.Elements.keys()))
        self.H = np.zeros((len(self.Elements), len(self.Elements)))
        for i, (e_id, element) in enumerate(self.Elements.items()):
            # determine elements neighbours within a radius
            element.determine_neighbours(self.Elements, r=self.rmin)
            # set up convolutional operator H for specific Simp Problem
            self.H[i] = self.__set_convolutional_operator__(element)
        # end Element section
        # FEA section
        self.FE_Model = fe_model
        # end FEA section
        # Variables section
        self.Var_u = ['u{}'.format(n) for n in self.DoFs]  # displacement variables
        self.Var_x = ['x_old{}'.format(n) for n in self.Elements]  # density variables
        # end Variables section
