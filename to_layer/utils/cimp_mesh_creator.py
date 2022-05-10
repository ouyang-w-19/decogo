import os

from to_layer.tomodel.subdomain import SubDomain
from to_layer.tomodel.boundary_condition import BoundaryConditions


class MFEMMesh:
    dimension: int = 0
    elements: dict = None
    element_number: int = 0

    nodes: dict = None
    node_number: int = 0

    boundary_conditions: BoundaryConditions = None

    mesh_path: str = None
    file: open = None

    @staticmethod
    def convert_list_to_str(_li):
        ret = ""
        for n in _li:
            ret += str(n) + " "
        return ret

    def get_boundary_number(self):
        n = 0
        number_fixed_nodes = len(self.boundary_conditions.fixed_nodes)
        n += number_fixed_nodes
        number_loaded_nodes = len(self.boundary_conditions.boundary_forces.keys()) + \
                              len(self.boundary_conditions.outer_forces.keys())
        n += number_loaded_nodes
        return n

    def write_file(self):
        with open(self.mesh_path, "w+") as self.file:
            self.file.write("MFEM mesh v1.0\n\n")
            self.file.write("dimension\n")
            self.file.write("{}\n\n".format(self.dimension))
            self.file.write("elements\n")
            self.file.write("{}\n".format(self.element_number))
            for e_id, element in self.elements.items():
                self.file.write("{} {} {}\n".format(1, 3, self.convert_list_to_str(list(element.Nodes.keys()))))
            self.file.write("\n")
            self.file.write("boundary\n")
            self.file.write("{}\n".format(self.get_boundary_number()))  # number of boundary elements
            for n in self.boundary_conditions.fixed_nodes:
                self.file.write("{} {} {}\n".format(2, 0, n))
            for node, N in self.boundary_conditions.boundary_forces.items():
                self.file.write("{} {} {}\n".format(3, 0, node))
            for node, N in self.boundary_conditions.outer_forces.items():
                self.file.write("{} {} {}\n".format(3, 0, node))
            self.file.write("\n")
            self.file.write("vertices\n")
            self.file.write("{}\n".format(self.node_number))
            self.file.write("{}\n".format(self.dimension))
            for n_id, node in self.nodes.items():
                self.file.write("{}\n".format(self.convert_list_to_str(list(node.n_vec[:self.dimension]))).lstrip())

    def __init__(self, domain: SubDomain, dir_path: str):

        self.mesh_path = os.path.join(dir_path, "sd{}.mesh".format(domain.SubDomain_ID))

        self.dimension = domain.dofs_per_node  # TODO: not very exact but works for the moment

        self.elements = domain.Elements
        self.element_number = len(self.elements)

        self.nodes = {}
        for e_id, element in self.elements.items():
            self.nodes = {**self.nodes, **element.Nodes}
        self.node_number = len(self.nodes)

        self.boundary_conditions = domain.FEModel.boundary_conditions
