import numpy as np

from to_layer.utils.utils import get_dofs


class BoundaryConditions:
    # Node Section
    global_nodes = []
    local_nodes = []
    node_number = 0
    # DoFSection
    dofs_per_node = 0
    global_dofs = []
    local_dofs = []
    dof_number = 0
    # Outer Force Section
    outer_forces = {}
    outer_forces_vec: np.array = None
    # End Section
    # Boundary Force Section
    boundary_forces = {}
    boundary_forces_vec: np.array = None
    # End Section
    # Reaction Force Section
    reaction_forces = {}
    reaction_forces_vec: np.array = None
    # End Section
    # complete force vector section
    force_vector = []
    # End Section
    # Displacement Section
    fixed_nodes = []
    fixed_dofs = []
    fixed_dofs_mask = []

    # conditions = {}

    # End Section

    def create_fixed_dofs_mask(self, ndofs):
        self.fixed_dofs_mask = np.zeros((ndofs,))
        for dof in self.fixed_dofs:
            self.fixed_dofs_mask[dof - 1] = 1

    def __map_fixed_dofs__(self):
        _d = [get_dofs(n) for n in self.fixed_nodes]
        _d = np.reshape(np.array(_d), (len(self.fixed_nodes) * self.dofs_per_node,))
        return _d

    def __create_force_vector_from_dict(self, f_dict: dict):
        _f = np.zeros((self.dof_number,))

        for node, vec in f_dict.items():
            dofs = get_dofs(node)
            idx = np.array([np.where(d == self.global_dofs)[0] for d in dofs]).squeeze()
            _f[idx] = vec
        return _f

    def __create_force_dict_from_vector__(self, f_vec: np.array):
        re_dim_f = np.reshape(f_vec, (self.node_number, int(self.dof_number / self.node_number)))
        f_dict = dict(zip(self.global_nodes, re_dim_f))

        for node, f_vec in f_dict.copy().items():
            if np.all(f_vec.round(6) == 0):
                f_dict.pop(node)

        return f_dict

    def update_boundary_force(self, f_boundary: dict):
        self.boundary_forces = f_boundary
        self.boundary_forces_vec = self.__create_force_vector_from_dict(self.boundary_forces)

    def __init__(self, outer_forces: dict, fixed_nodes: list, nodes: list, dofs_per_node=2,
                 boundary_forces: dict = None):

        self.global_nodes = nodes
        self.local_nodes = list(range(1, len(self.global_nodes) + 1))
        self.node_number = len(self.global_nodes)

        self.dofs_per_node = dofs_per_node

        self.dof_number = len(nodes) * dofs_per_node
        self.global_dofs = np.array([get_dofs(n) for n in self.global_nodes]).reshape((self.dof_number,))
        self.local_dofs = [list(range(1, self.dof_number + 1))]

        self.outer_forces = outer_forces
        self.outer_forces_vec = self.__create_force_vector_from_dict(outer_forces)

        self.fixed_nodes = fixed_nodes
        self.fixed_dofs = self.__map_fixed_dofs__()

        if boundary_forces is None:
            self.boundary_forces = {}
            self.boundary_forces_vec = np.zeros((self.dof_number,))
        else:
            self.update_boundary_force(boundary_forces)

        self.force_vector = self.outer_forces_vec + self.boundary_forces_vec
