import numpy as np

from to_layer.elements.element import Element
from to_layer.elements.C2D4Simple import ke
from to_layer.utils.node import Node

from to_layer.tomodel.tousermodel import TOModelBase
from to_layer.tomodel.boundary_condition import BoundaryConditions

nodes = {}      # initialize dict for nodes
elements = {}   # initialize dict for elements

base_nodes = list(range(1, 26))         # set up the list of node-ids; N = {1,...,25}
element_numbers = list(range(1, 17))    # set up list of element-ids; M = {1,...,16}

# Design Space Section; works only for this model because of the 2 dimensional space and square elements
element_space = np.array(element_numbers).reshape((4, 4)).T     # set up a 2D design space for the elements
node_space = np.array(base_nodes).reshape((5, 5)).T             # set up a 2D design space for the nodes

col = -1    # will be equivalent to x-coordinate of a node
row = 0     # will be equivalent to y-coordinate of a node
# Determine dict for nodes
for i, n_id in enumerate(base_nodes):
    if n_id % 5 == 1:
        row = 4
        col += 1
    nodes[n_id] = Node(n_id, float(col), float(row), z=0.0, index=i)    # Node object is created
    row -= 1
# Determine dict for elements
for e_id in element_numbers:
    i = int(np.where(element_space == e_id)[0])     # get x-position in design space
    j = int(np.where(element_space == e_id)[1])     # get y-position in design space

    element_nodes = node_space[i:i+2, j:j+2].reshape((4, ))     # get the corresponding nodes
    element_nodes = element_nodes[[2, 3, 1, 0]]                 # reorder node-ids so they fit to element formulation
    elements[e_id] = Element(e_id, {n: nodes[n] for n in element_nodes}, ke(1, 0.3))  # Element object is created

outer_forced_nodes = [25]                                       # create a list of loaded nodes
f_dict = {n: np.array([0, -1]) for n in outer_forced_nodes}     # create the dict for outer forces
fixed_nodes = [1, 5]                                            # create a list of fixed nodes

bc = BoundaryConditions(f_dict, fixed_nodes, list(base_nodes))  # create the boundary conditions nodes

base_model = TOModelBase(nodes, elements, bc, 2)                # create the instance of TOModelBase
# define the simple design space by hand of 4 x 4 elements
base_model.SimpProblem.shape = (4, 4)
# base_model can be used for further actions or rather will be imported for optimization
