import itertools
import numpy as np

from to_layer.elements.C2D4Simple import shape_functions, rs
from typing import List


# NOTE: In general the object's properties are updated -> get values from properties
class Element:
    # Node and Geometry Section
    node_number: int = 4
    dimension: int = 2
    dofs_per_node: int = 2
    centroid = np.zeros((3,))
    neighbours: dict = {}
    V: float = None
    node_perm: np.array = None
    # Dof Section
    Dofs: dict = {}  # represents the elements dofs regarding its nodes
    DoFHelper = []  # list of dofs of the element
    dof_number = node_number * dofs_per_node
    # FE-Section
    Ke = np.empty((dof_number, dof_number))  # current element stiffness matrix
    Ke0 = np.empty_like(Ke)  # initial element stiffness matrix for Ke = x^p * Ke0
    Ue = {}  # keys: nodes values: corresponding displacements
    Ue_vec = np.empty((dof_number,))  # complete displacement vector for elements
    Fe = {}  # current force dict keys: nodes value: corresponding force vector
    Fe0 = {}  # initial force dict keys: nodes value: corresponding force vector
    Fe_vec = np.empty((dof_number,))  # complete force vector of element
    # SIMP Section
    x = 1  # actual density
    xold = 0.0  # step-1 density
    Ce = 0.0  # flexibility
    dCe = 0.0  # derived flexibility
    ddCe = 0.0 # derived derived flexibility

    @staticmethod
    def pairwise(iterable):
        """
           Same as itertools.pairwise but it seams that the function not available anymore
           :parameter iterable : any iterable
           :return list with permutations
       """
        a, b = itertools.tee(iterable)
        next(b, None)
        return zip(a, b)

    def __create_node_permutation__(self):

        _nodes = list(self.Nodes.keys())

        self.node_perm = list(self.pairwise(_nodes))
        self.node_perm.append((_nodes[-1], _nodes[0]))
        self.node_perm = np.array(self.node_perm)

        for i, combi in enumerate(self.node_perm):
            self.node_perm[i] = np.sort(combi)
    
    # set neighbors of an element depending on the radius r
    def determine_neighbours(self, elements: dict, r=1.5):

        for i, (e_id, element) in enumerate(elements.items()):
            d = np.linalg.norm(element.centroid - self.centroid)
            if 0 <= d <= r:
                self.neighbours[e_id] = element
    
    # determine element's centroid
    def set_centroid(self):
        _arr = np.array([self.Nodes[n_id].n_vec for n_id in self.Nodes])
        self.centroid = np.array(
            [
                np.mean(_arr[:, 0]), np.mean(_arr[:, 1]), np.mean(_arr[:, 2])
            ]
        )
    
    # update the elemen's stiffness matrix regarding the SIMP approach
    def update_stiffness_matrix(self, e_min=1e-9, e_max=1, p=3):
        self.Ke = (e_min + self.x ** p * (e_max - e_min)) * self.Ke0
    
    # update nodal forces of element's nodes using the gaussian approach with the mean value at gaussian integration points
    def update_nodal_forces(self, u_out=None):
        _nodes = list(self.Nodes.keys())
        if u_out is not None:
            self.Fe_vec = np.dot(self.Ke, u_out)
            _f = self.Fe_vec.reshape((len(self.Nodes), self.dofs_per_node))
            self.Fe = dict(zip(_nodes, _f))
        else:
            self.Fe_vec = np.dot(self.Ke, self.Ue_vec)
            _f = self.Fe_vec.reshape((len(self.Nodes), self.dofs_per_node))
            self.Fe0 = dict(zip(_nodes, _f))
    
    # udpate the elemets displacements regarding a domain's global displacements  
    def update_element_displacements(self, u_glob: np.array, domain_global_dofs: np.array):

        idx = np.array([np.where(domain_global_dofs == d)[0] for d in self.DoFHelper]).squeeze()

        ue_glob = u_glob[idx]

        ux_mask = np.array(list(range(0, len(self.Nodes) * self.dofs_per_node - 1, 2)))
        uy_mask = np.array(list(range(1, len(self.Nodes) * self.dofs_per_node + 1, 2)))

        eux = ue_glob[ux_mask]
        euy = ue_glob[uy_mask]

        self.Ue_vec = []
        # Checks outstanding if required!!!
        # Transfer displacements to gaussian integration points regarding the element formulation
        for it, p in rs.items():
            self.Ue_vec.append(sum(shape_functions[j + 1](p[0], p[1]) * eux[j] for j in range(len(self.Nodes))))
            self.Ue_vec.append(sum(shape_functions[j + 1](p[0], p[1]) * euy[j] for j in range(len(self.Nodes))))

        self.Ue_vec = np.array(self.Ue_vec)

        for n_id, node in self.Nodes.items():
            self.Ue[n_id] = \
                self.Ue_vec[list(self.Nodes.keys()).index(n_id) * 2: list(self.Nodes.keys()).index(n_id) * 2 + 2]
    
    # update elements flexibility, two different methods implemented
    # 1: using just elements properties -> parameter d_ke is none -> u^T Ke u
    # 2: regarding a force from outside -> parameter d_ke: np.array -> u^T d_ke
    def update_flexibility(self, d_ke=None):
        self.Ce_unit = np.dot(np.dot(self.Ue_vec.T, self.Ke0), self.Ue_vec)
        if d_ke is not None:
            self.Ce = np.dot(d_ke.T, self.Ue_vec)
        else:
            self.Ce = np.dot(np.dot(self.Ue_vec.T, self.Ke), self.Ue_vec)
    
    # derive the flexibility in accordance to SIMP-Approach
    def derive_flexibility(self, p=3, e_min=1e-9, e_max=1):
        dk = -p * (self.x ** (p - 1)) * (e_max - e_min) * self.Ke0
        self.dCe = np.dot(np.dot(self.Ue_vec.T, dk), self.Ue_vec)
    
    # derive the derived flexibility regarding the SIMP-Approach
    def derive_derived_flexibility(self, p=3, e_min=1e-9, e_max=1):
        ddk = -p * (p - 1) * self.x ** (p - 2) * (e_max - e_min) * self.Ke0
        self.ddCe = np.dot(np.dot(self.Ue_vec.T, ddk), self.Ue_vec)
        return self.ddCe
    
    # apply sensitivity filter using a convolutional factor from SIMP
    def apply_sensitivity_filter(self, domain_elements, hj):

        xj = np.array([element.x for e_id, element in domain_elements.items()])

        dcj = np.array([element.dCe for e_id, element in domain_elements.items()])

        self.dCe_filtered = (1 / (np.maximum(self.x, 1e-3)) * hj.sum()) * (hj * xj * dcj).sum()
    
    # get the volume of the element (or rather the cross-section, or volume with a depth of 1 :D)
    def get_volume(self):
        _n_indices = list(self.Nodes.keys())
        _v1 = self.Nodes[_n_indices[0]].n_vec - self.Nodes[_n_indices[2]].n_vec
        _v2 = self.Nodes[_n_indices[1]].n_vec - self.Nodes[_n_indices[3]].n_vec
        return 0.5 * np.linalg.norm(np.cross(_v1, _v2))

    def __init__(self, e_id: int, nodes: dict, ke: np.array, dense_x: float = 1.0):
        self.id = e_id
        self.Nodes = nodes  # dict with nodes as objects
        self.__create_node_permutation__()
        self.set_centroid()
        self.Ke = ke  # element's stiffness matrix
        self.Ke0 = ke  # create a copy to store the initial stiffness matrix
        # dict with: keys: Nodes, values: corr. dofs
        # TODO: Just works for two dofs at a node at the moment
        self.Dofs = {n: list(range(2 * n - 1, 2 * n + 1)) for n in self.Nodes.keys()}

        # elements displacements; init with zeros;
        # has to be calculated by using the element's shape functions
        self.Ue = {n: np.zeros((2,)) for n in self.Nodes.keys()}
        self.Ue_vec = np.zeros((len(self.Dofs),))
        # elements nodal forces; init with zeros
        self.Fe_vec = self.Ue_vec.copy()
        self.Fe0 = self.Ue.copy()

        self.DoFHelper = []

        for n in self.Dofs:
            for d in self.Dofs[n]:
                self.DoFHelper.append(d)

        self.x = dense_x

        self.Ce = 0
        self.Ce_unit = 0
        self.dCe = 0
        self.ddCe = 0
        self.dCe_filtered = 0

        self.V = self.get_volume()

        self.neighbours = {}

        for nid, node in self.Nodes.items():
            if self.id not in node.attached_elements:
                node.attached_elements.append(self.id)
