import os
import numpy as np

from pathlib import Path

from to_layer.meshparser.mshparser import MSHParser
from to_layer.tomodel.subdomain import SubDomain
from to_layer.tomodel.todecomposer import TODecomposer
from to_layer.tomodel.to_input_model import TOInputModel
from to_layer.tomodel.tousermodel import TOModelBase
from to_layer.tomodel.boundary_condition import BoundaryConditions

root = Path(__file__).parent.parent                     # get projects root path
geometry_path = os.path.join(root, 'Geometry')          # determine geometry folder
msh_file = os.path.join(geometry_path, 'topopt.msh')    # define the explicit mesh file

p = MSHParser(msh_file)     # create an instance of the parser with teh mesh file


fixations_2 = [1, 4]                # define a fixation boundary with 2 fixed nodes
fixations_5 = [1, 4, 14, 15, 16]    # define a fixation boundary with 5 fixed nodes

# create an instance of manual boundary conditions
manual_boundary_conditions = BoundaryConditions(
    outer_forces={2: np.array([0, -1])},
    fixed_nodes=fixations_2,
    nodes=list(range(1, 26))
)

# get the TOModelBase object using the parser
base_model: TOModelBase = p.get_base_model(_bc=manual_boundary_conditions)

cut_nodes = [15, 18, 24, 9, 12, 22, 21, 20, 6]   # define the node which will be cut due to the decomposer
cut_nodes.sort()     # sort the node; note absolutely necessary

# element ids per sub-domain
cell_eids = {
    1: [13, 14, 17, 18],
    2: [21, 22, 25, 26],
    3: [23, 24, 27, 28],
    4: [15, 16, 19, 20]
}

# Initialization of Sub-Domains
raw_subdomains = {}

for sid, nodes in cell_eids.items():
    sd_elements = {}
    for i, n in enumerate(nodes):
        sd_elements[n] = base_model.elements[n]
    raw_subdomains[sid] = SubDomain(sd_elements, sid)

decomposer = TODecomposer(cut_nodes, raw_subdomains, base_model)    # define the decomposer

ref_model = base_model.reformulate(decomposer)  # apply the decomposer to the base model and get the ref model

inp_model = TOInputModel(ref_model)     # get the input model for decogo
