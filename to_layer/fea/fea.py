import numpy as np

from to_layer.tomodel.boundary_condition import BoundaryConditions
from scipy.optimize import least_squares


class FEModel:

    F = None  # Systems Force Vector
    K = None  # Systems Stiffness Matrix
    U = None  # Total Displacements
    R = None  # Reaction Forces

    node_number = 0
    dofs_per_node = 2
    dimension: int = 0

    global_nodes = []
    elements = {}
    boundary_conditions = {}

    is_undetermined = False

    # Bounds for u and the base for, used for trust regions
    u_base: np.array = None
    u_bounds: tuple = None
    delta = 2

    # TODO: Current state: quick and dirty, SHALL: Create new method without if statement, use sparse
    def get_k(self, _x=None, p=3):
        k = np.zeros((self.dof_number, self.dof_number))
        for dict_it, (e_id, element) in enumerate(self.elements.items()):
            local_dofs = np.where([self.global_dofs == d for d in element.DoFHelper])[1]
            for it, i in enumerate(local_dofs):
                for jt, j in enumerate(local_dofs):
                    if _x is None:
                        k[i, j] += element.Ke[it, jt]
                    else:
                        k_val = ((1e-9 + _x[dict_it] ** p * (1 - 1e-9)) * element.Ke0)[it, jt]
                        k[i, j] += k_val

        return k

    def incorporate_boundary_conditions(self, k: np.array, f: np.array):

        local_fixed_dofs = np.where([self.global_dofs == d
                                     for d in self.boundary_conditions.fixed_dofs])[1]

        for i, d in enumerate(local_fixed_dofs):

            k[:, d] = 0
            k[d, :] = 0
            k[d, d] = 1
            f[d] = 0

        return k, f

    def get_reaction_forces(self):
        self.R = self.get_k(_x=np.array([e.x for i, e in self.elements.items()])).dot(self.U)
        return self.R

    def solve(self, f_user=None):
        """
        solves the FE-System; also updates the systems displacements including the displacements for the objects
        of the elements
        :param f_user: optional specific rhs
        :return: system's displacements, feasibility of solution
        """

        if f_user is not None:
            _f = f_user
        else:
            _f = self.F

        # system is statically determined so it possible to solve the system using a direct solver
        if self.is_undetermined is False:

            self.U = np.linalg.solve(self.K, _f)
            solution_is_feasible = True

        # system is statically indeterminate so a least square approach with a trust region
        # for displacements is used
        else:

            # make the objective function for least square problem
            def make_func(_k, _f):
                def func(_u):
                    return np.dot(_k, _u) - _f
                return func

            # define bounds
            self.set_bounds(self.u_base)
            # solve the indeterminate system using scipy's least square solver
            res = least_squares(make_func(self.K, _f), self.u_base, bounds=self.u_bounds,
                                method='dogbox')

            self.U = res.x
            self.set_bounds(self.U)  # update u-base

            solution_is_feasible = True

        # set reaction forces
        self.get_reaction_forces()
        # update element properties
        for e_id, element in self.elements.items():
            element.update_element_displacements(self.U, self.global_dofs)
            element.update_nodal_forces()

        return self.U, solution_is_feasible

    def set_bounds(self, u_domain):
        self.u_base = u_domain
        self.u_bounds = (
            u_domain - self.delta * np.absolute(u_domain),  # u_lower
            u_domain + self.delta * np.absolute(u_domain)   # u_upper
        )

        self.u_bounds[0][self.u_bounds[0] == 0] -= 1e-3
        self.u_bounds[1][self.u_bounds[1] == 0] += 1e-3

    def check_displacements(self, _u) -> bool:
        if np.all(_u > self.u_bounds[0]) and np.all(_u < self.u_bounds[1]):
            return True
        else:
            return False

    def __get_updates__(self, _x: np.array):
        self.K = self.get_k(_x)

        if len(self.boundary_conditions.fixed_nodes) > 0:
            self.K, self.F = self.incorporate_boundary_conditions(self.K, self.F)

        _u = self.solve()[0]

        return _x, _u, np.dot(np.dot(_u.T, self.K), _u)

    def transform_relaxed_point(self, _x: np.array):

        return self.__get_updates__(_x.round())

    def incorporate_one_constraint(self, _x: np.array, _one_indices: np.array):
        for i in _one_indices:
            _x[i] = 1

        return self.__get_updates__(_x)

    def __init__(self, nodes: list, elements: dict, boundary_conditions: BoundaryConditions, dim=2):
        self.node_number = len(nodes)
        self.dof_number = self.node_number * self.dofs_per_node
        self.local_nodes = list(range(1, self.node_number + 1))
        self.local_dofs = list(range(1, self.dof_number + 1))
        self.dimension = dim
        self.elements = elements

        self.global_dofs = np.unique(np.array([self.elements[i].DoFHelper
                                               for i in self.elements]))
        self.global_nodes = nodes
        self.boundary_conditions = boundary_conditions

        self.F = self.boundary_conditions.force_vector
        self.K = self.get_k(np.array([e.x for i, e in self.elements.items()]))

        if len(self.boundary_conditions.fixed_nodes) > 1:
            self.is_undetermined = False
        else:
            self.is_undetermined = True

        if len(self.boundary_conditions.fixed_nodes) > 0:
            self.K, self.F = self.incorporate_boundary_conditions(self.K, self.F)
