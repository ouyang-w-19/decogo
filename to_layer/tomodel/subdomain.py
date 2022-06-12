import numpy as np

from to_layer.tomodel.boundary_condition import BoundaryConditions
from to_layer.elements.element import Element
from to_layer.utils.utils import get_dofs
from to_layer.utils.node import Node
from to_layer.fea.fea import FEModel
from to_layer.simp.simp import SimpProblem

from typing import Dict, List


class SubDomain:
    Elements: Dict[int, Element] = {}
    Nodes: List[Node] = []
    Dofs: List[int] = []
    dofs_per_node: int = 2
    SubDomain_ID: int = 0

    Dimension: int = 2

    celx: int = 0  # hopefully out-dated
    cely: int = 0  # hopefully out-dated
    celz: int = 0  # hopefully out-dated

    x_init = np.empty((len(Elements),))
    u_init = np.empty((len(Dofs),))
    y_init = np.empty((len(Elements) + len(Dofs),))

    Var_x = []
    Var_u = []
    Vars = []

    domain_boundary_nodes = []
    domain_boundary_dofs = []
    node_to_element_mapping = {}

    FEModel = None

    SubSimpProblem = None

    def get_v(self, _x: np.array):
        return sum(_x[i] * element.V for i, (e_id, element) in enumerate(self.Elements.items()))

    def get_c(self, _x: np.array, _u: np.array):
        """
        Calculates flexibility of sub-domain depending on x and u
        :param _x: density distribution; shape must fit to element number
        :type np.array
        :param _u: displacements in the domain
        :type np.array
        :return: _c flexibility
        """
        _k = self.FEModel.get_k(_x)
        return np.dot(np.dot(_u.T, _k), _u)

    def get_x_vec_cell(self):
        return np.array([element.x for e_id, element in self.Elements.items()])

    def __get__vars__(self):
        x = ["x_{}{}".format(self.SubDomain_ID, e) for e in self.Elements]
        u = ["u_{}{}".format(self.SubDomain_ID, d) for d in self.Dofs]
        return x, u

    def get_local_dof_index(self, global_dof):
        index_in_dofs = self.Dofs.index(global_dof)
        return self.LocalDofs[index_in_dofs]

    def get_global_dof_index(self, local_dof):
        index_in_dofs = self.LocalDofs.index(local_dof)
        return self.Dofs[index_in_dofs]

    def update_boundary_nodes(self, cutted_nodes: list):
        self.domain_boundary_nodes = []
        for n in self.Nodes:
            if n in cutted_nodes:
                self.domain_boundary_nodes.append(n)

    def update_boundary_dofs(self):
        self.domain_boundary_dofs = [get_dofs(n) for n in self.domain_boundary_nodes]
        self.domain_boundary_dofs = np.reshape(self.domain_boundary_dofs, (len(self.domain_boundary_nodes * 2),))

    def get_boundary_forces(self, x: np.array, u: np.array, update=False, method='ku'):

        """
        :param method: gauss: use mean values of gaussian integration points from boundary-nodes elements
        ku: solve k_domain dot u_domain - f_outer; is default
        :param x: domain's densities; length is number of elements in domain
        :param u: domain's displacement; length is number of dofs in domain
        :param update: differs if just a return is required, or if this method also update the objects
        :return: (dict where keys are the nodes and values are corresponding force vector at node, total force vector
        of domain's boundary forces)
        """

        g_dict = {}  # initialize g_dict; not required for g_vec

        if method == 'ku':
            # solve k_domain dot u_domain - f_domain_outer
            # get k for corresponding density distribution
            _k = self.FEModel.get_k(_x=x)
            if len(self.FEModel.boundary_conditions.fixed_nodes) > 0:
                _k, _ = self.FEModel.incorporate_boundary_conditions(_k, self.FEModel.F)
            g_vec = np.dot(_k, u) - self.FEModel.boundary_conditions.outer_forces_vec
            # create the return dict
            for boundary_node in self.domain_boundary_nodes:  # there is an entry in dict for every boundary node
                ndofs = get_dofs(boundary_node)  # get the global dofs for the node
                # extract the force vector from g_vec
                _g = g_vec[np.array([self.get_local_dof_index(d) for d in ndofs])[:] - 1]
                # set entry
                g_dict[boundary_node] = _g

        elif method == 'gauss':
            g_vec = np.zeros((len(self.Dofs),))
            for boundary_node in self.domain_boundary_nodes:
                attached_elements = self.node_to_element_mapping[boundary_node]
                _gn = np.zeros((self.dofs_per_node,))
                for element_number in attached_elements:
                    current_element: Element = self.Elements[element_number]
                    current_element.x = x[list(self.Elements.keys()).index(element_number)]
                    current_element.update_stiffness_matrix()
                    current_element.update_element_displacements(u, np.array(self.Dofs))
                    current_element.update_nodal_forces()  # e.Fe0 is updated

                    _gn += current_element.Fe0[boundary_node]

                _gn[:] /= len(attached_elements)
                g_dict[boundary_node] = _gn

                # update g_vec
                ndofs = get_dofs(boundary_node)  # get the global dofs for the node
                # extract the force vector from g_vec
                g_vec[np.array([self.get_local_dof_index(d) for d in ndofs])[:] - 1] += _gn

        else:
            raise NotImplemented("Can not recognize method! Available methods are ku and gauss")

        if update:
            self.FEModel.boundary_conditions.boundary_forces_vec = g_vec
            self.FEModel.boundary_conditions.boundary_forces = g_dict
            self.FEModel.F = self.FEModel.boundary_conditions.boundary_forces_vec + \
                             self.FEModel.boundary_conditions.outer_forces_vec

        return g_dict, g_vec

    def __get_fixed_nodes__(self, global_fixed_nodes: list):
        return [n for n in global_fixed_nodes if n in self.Nodes]

    def update_domain(self, cut_nodes: list, u_domain: np.array, bc: BoundaryConditions):
        self.update_boundary_nodes(cut_nodes)
        self.update_boundary_dofs()

        self.FEModel = FEModel(self.Nodes, self.Elements, bc)

        # base model is calculated before so there no extra
        # determine boundary forces
        f_boundary = self.get_boundary_forces(
            np.array([e.x for i, e in self.Elements.items()]),
            u_domain,
            update=False, method='ku')[0]
        # update boundary forces in Boundary Conditions
        self.FEModel.boundary_conditions.update_boundary_force(f_boundary)
        # update the sub-domain's total force vector
        self.FEModel.F = self.FEModel.boundary_conditions.outer_forces_vec +\
                         self.FEModel.boundary_conditions.boundary_forces_vec
        # reincorporate boundary conditions if necessary and set u_base vector for static indeterminate domains
        if len(self.FEModel.boundary_conditions.fixed_nodes) > 0:
            self.FEModel.K, self.FEModel.F = self.FEModel.incorporate_boundary_conditions(self.FEModel.K,
                                                                                          self.FEModel.F)
            if len(self.FEModel.boundary_conditions.fixed_nodes) > 1:
                self.FEModel.is_undetermined = False
            else:
                self.FEModel.is_undetermined = True
        else:
            self.FEModel.is_undetermined = True

        # Define bounds for FEModel
        self.FEModel.set_bounds(u_domain)
        # Set SimpProblem
        self.SubSimpProblem = SimpProblem(len(self.Nodes), self.Elements, self.FEModel)

    def set_init_vectors(self, u_glob: np.array, x_sub_domain: np.array):
        self.x_init = x_sub_domain
        idx = np.array(self.Dofs)[:] - 1
        self.u_init = u_glob[idx]
        self.y_init = np.concatenate([self.x_init, self.u_init])

    def __init__(self, elements: dict, subdomain_id: int, dim=2, celx=0, cely=0, celz=0):
        self.Elements = elements
        self.Dimension = dim
        self.Nodes = []
        self.Dofs = []
        self.SubDomain_ID = subdomain_id
        self.celx = celx
        self.cely = cely
        self.celz = celz
        for e in self.Elements:
            ce = self.Elements[e]
            for n in ce.Nodes.keys():
                if n not in self.Nodes:
                    self.Nodes.append(n)
            for d in ce.DoFHelper:
                if d not in self.Dofs:
                    self.Dofs.append(d)
        self.Nodes.sort()
        self.Dofs.sort()

        self.LocalDofs = list(range(1, len(self.Dofs) + 1))

        # Var Section
        x_str, u_str = self.__get__vars__()
        self.Var_x = x_str
        self.Var_u = u_str
        self.Vars = self.Var_x + self.Var_u
        # Set Initialization Vectors
        self.x_init = np.zeros((len(self.Elements, )))
        self.u_init = np.zeros((len(self.Dofs, )))
        self.y_init = np.concatenate([self.x_init, self.u_init])
        # End Section

        # create the node to element mapping
        # key = node number
        # value = list of elements
        self.node_to_element_mapping = {}
        for n in self.Nodes:
            self.node_to_element_mapping[n] = []
            for en, ele in self.Elements.items():
                if n in ele.Nodes.keys():
                    self.node_to_element_mapping[n].append(en)

        # initialize variables and update them with decomposer
        # set up cells FE-Model
        self.FEModel = None
        # set up Simp-Problem for
        self.SubSimpProblem = None

        # Volume Section
        self.V0 = self.get_v(np.array([1] * len(self.Elements)))
        self.Vf0 = self.get_v(np.array([e.x for i, e in self.Elements.items()]))
        self.Vf = self.get_v(np.array([e.x for i, e in self.Elements.items()]))
