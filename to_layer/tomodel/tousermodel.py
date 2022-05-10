import numpy as np

from typing import Dict, List

from to_layer.utils.utils import get_dofs
from to_layer.utils.node import Node
from to_layer.tomodel.boundary_condition import BoundaryConditions
from to_layer.tomodel.to_reformulated_user_model import TOReformulatedUserModel
from to_layer.fea.fea import FEModel
from to_layer.simp.simp import SimpProblem
from to_layer.elements.element import Element


class TOModelBase:
    """
    Defines the Original Topology Optimization Problem. Every Problem requires an instance of this class

    Attributes
    ----------
    elements : dict[int, Element]
        :key global element ID
        :value Element-object to the corresponding element ID

    nodes : list[int]
        list of global node ID's

    Nodes : dict[int, Node]
        :key global node ID
        :value Node-object to the corresponding node ID

    dofs : list[int]
        list of global degrees of freedom

    FEModel : FEModel
        Object which defines the corresponding finite element model

    SimpProblem : SimpProblem
        Object which defines the corresponding SIMP-Problem

    nelx : int
        number of elements in x-direction; may outdated!!; just can be used on 2D Models with square elements

    nely : int
        number of elements in y-direction; may outdated!!; just can be used on 2D Models with square elements

    nelz : int
        number of elements in z-direction; may outdated!!; just can be used on 2D Models with square elements

    """
    elements: Dict[int, Element] = {}
    nodes: List[int] = None
    Nodes: Dict[int, Node] = None
    dofs = []

    FEModel: FEModel = None
    SimpProblem: SimpProblem = None

    nelx: int = 0
    nely: int = 0
    nelz: int = 0

    var_x = []
    var_u = []
    vars = []
    param_f = []

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

    def get_volume(self):
        return sum(e.x * e.V for i, e in self.elements.items())

    def display(self):
        """
        prints properties of current original model to console
        :return: None
        """
        print("Topology Optimization Model:\n")
        print("Dimension: {}\n".format("2D"))
        print("Number of Nodes:              \t{}\n".format(len(self.nodes)))
        print("Number of Elements:           \t{}\n".format(len(self.elements)))
        print("Number of Degrees of Freedom: \t{}\n".format(len(self.dofs)))
        print("Dimension of Stiffness Matrix:\t{}x{}".format(len(self.dofs), len(self.dofs)))
        print("Densities Variables x_i:\n")
        print("\tNumber: {}\n".format(len(self.var_x)))
        print("\tVariables: {}\n".format(self.var_x))
        print("Displacement Variables u_i:\n")
        print("\tNumber: {}\n".format(len(self.var_u)))
        print("\tVariables: {}\n".format(self.var_u))
        print("Symbolic Force Vector f in accordance to Dofs:\n {}\n".format(self.param_f))
        print("Boundary Conditions of the Model:\n")
        print("Fixation:\n")
        print("\tFixed Nodes in Space: {}\n".format(self.FEModel.boundary_conditions.fixed_nodes))
        print("\tCorresponding Dofs: {}\n".format(self.FEModel.boundary_conditions.fixed_dofs))
        print("\tZero Displacement Variables:\n")
        for d in self.FEModel.boundary_conditions.fixed_dofs:
            print("\tu_{} = 0".format(d))
        print("\nLoads:\n")
        print("\tForce Vector f: {}".format(self.FEModel.boundary_conditions.force_vector))

    def reformulate(self, decomposer):
        """
        reformulates the original domain to the block-separable domain formulation
        :param decomposer: a decomposer is applied to the original model
        :type TODecomposer
        :return:
        """
        return TOReformulatedUserModel(self, decomposer)

    def __init__(self, nodes: dict, elements: dict, boundary_conditions: BoundaryConditions,
                 dofs_per_node: int,
                 nelx=0, nely=0, nelz=0):
        """
        Constructor for original domain;
        :param nodes:
        :param elements:
        :param boundary_conditions:
        :param dofs_per_node:
        :param nelx:
        :param nely:
        :param nelz:
        """
        # General properties
        self.Nodes = nodes
        self.nodes = list(self.Nodes.keys())
        self.dofs = [get_dofs(n) for n in self.nodes]
        self.dofs = np.reshape(self.dofs, (dofs_per_node * len(self.nodes),))
        # Set Elements
        self.elements = elements

        # Design Space Section
        # OUTDATED!!!!
        self.nelx = nelx
        self.nely = nely
        self.nelz = nelz

        # FEA section
        self.FEModel = FEModel(self.nodes, self.elements, boundary_conditions)
        self.FEModel.solve()  # solve for initial values
        self.FEModel.set_bounds(self.FEModel.U)

        # set up Simp-Problem for original problem
        self.SimpProblem = SimpProblem(len(self.nodes), self.elements, self.FEModel)

        # var section
        # just for visualization
        self.var_x = ["x_{}".format(e) for e in self.elements]
        self.var_u = ["u_{}".format(d) for d in self.dofs]
        self.param_f = ["f_{}".format(d) for d in self.dofs]
        self.vars = self.var_x + self.var_u
