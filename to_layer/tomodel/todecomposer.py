import numpy as np

from to_layer.tomodel.subdomain import SubDomain
from to_layer.tomodel.boundary_condition import BoundaryConditions
from typing import List, Dict


class TODecomposer:
    cutted_nodes: List[int] = []            # List of cut nodes
    cells: Dict[int, SubDomain] = {}        # Dict with Sub-Domains
    wu_elements: Dict[int, List[int]] = {}  # keys: node-ids, values: list of elements where node is used
    wu_cells: Dict[int, List[int]] = {}     # keys: node-ids, values: list of sub-domains where node is used
    wu_dofs: Dict[int, List[int]] = {}      # keys: dof-ids,  values: list of sub-domains where dof is used
    user_model = None

    blocks: List[List[str]] = []  # list of lists: inner list for each SD, containing vars
    block_sizes: List[int] = []  # list with sub-domain sizes (number of variables in each block)

    mapping_copy_constraints = []
    symbolic_copy_constraints = []

    def get_wu_nodes_in_elements(self):
        wn = {}
        for n in self.cutted_nodes:
            wn[n] = []
            for element in self.user_model.elements:
                if n in self.user_model.elements[element].Nodes.keys():
                    wn[n].append(element)
        return wn

    def get_wu_nodes_in_cells(self):
        wc = {}
        for n in self.cutted_nodes:
            wc[n] = []
            for c in self.cells:
                if n in self.cells[c].Nodes:
                    wc[n].append(c)
        return wc

    def get_wu_dofs_in_cells(self):
        wd = {}
        for node in self.wu_cells:
            c_dofs = np.array([2 * node - 1, 2 * node])
            wd[c_dofs[0]] = self.wu_cells[node]
            wd[c_dofs[1]] = self.wu_cells[node]
        return wd

    def decompose(self):
        blocks = []
        for c in self.cells:
            blocks.append(
                [self.cells[c].Vars]
            )
        blocks = np.squeeze(blocks, 1).tolist()

        block_sizes = [len(cv) for cv in blocks]
        return blocks, block_sizes

    def get_copy_constraints(self):

        """
        Returns the decogo specific formulation of the copy constraints;
        also creates the mapping for copy constraints relevant displacement variables
        """

        copy_list = []

        for d in self.wu_dofs:

            master_var = {
                "b_id": self.wu_dofs[d][0] - 1,
                "cell": self.cells[self.wu_dofs[d][0]],
                "global_dof": d,
                "local_dof": self.cells[self.wu_dofs[d][0]].get_local_dof_index(d),
                "var_index_in_block": self.cells[self.wu_dofs[d][0]].get_local_dof_index(d) +
                                      len(self.cells[self.wu_dofs[d][0]].Elements),
                "value": 1
            }

            self.mapping_copy_constraints.append(master_var)

            in_cells = self.wu_dofs[d]
            for i in range(1, len(in_cells)):
                # appends decogo relevant list (for sparse block vectors)
                copy_list.append([(master_var["b_id"], master_var["var_index_in_block"] - 1, master_var["value"]),
                                  (in_cells[i] - 1, self.cells[in_cells[i]].get_local_dof_index(d) +
                                   len(self.cells[in_cells[i]].Elements) - 1, -1)])

                self.symbolic_copy_constraints.append("u_{}{} = u_{}{}".format(
                    master_var["b_id"] + 1, master_var["global_dof"], in_cells[i], d))

        return copy_list

    def get_zero_constraints(self):
        fixed_constraints = []
        for dof in self.user_model.FEModel.boundary_conditions.fixed_dofs:
            for c_id, cell in self.cells.items():
                if dof in cell.Dofs:
                    block_id = c_id - 1
                    loc_dof = cell.get_local_dof_index(dof)
                    fixed_constraints.append([(block_id, len(cell.Elements) + loc_dof - 1, 1)])
        return fixed_constraints

    def display(self):
        print("Decomposer for the 4x4-Model:\n")
        print("User-defined cutted nodes (will define the cells of the model): {}\n".format(self.cutted_nodes))

        print("These cutted nodes result in the following cell sizes: {}\n".format(self.block_sizes))

    def create_domains_boundary_condition(self, subdomain: SubDomain) -> BoundaryConditions:
        # create a list of fixed nodes for the subdomain
        fixations = [n for n in self.user_model.FEModel.boundary_conditions.fixed_nodes if n in subdomain.Nodes]
        # ----------------------------------
        # create the dict for outer forces
        f_outer = {}
        for node, vector in self.user_model.FEModel.boundary_conditions.outer_forces.items():
            if node in subdomain.Nodes:
                if node in self.cutted_nodes:
                    f_outer[node] = vector[:] / len(self.wu_cells[node])
                else:
                    f_outer[node] = vector
        # ----------------------------------

        return BoundaryConditions(f_outer, fixations, subdomain.Nodes, boundary_forces=None)

    def __init__(self, cutted_nodes: list, sub_domains: dict, user_model):
        self.cutted_nodes = cutted_nodes
        self.cutted_nodes.sort()
        self.cells = sub_domains
        self.user_model = user_model

        self.wu_elements = self.get_wu_nodes_in_elements()
        self.wu_cells = self.get_wu_nodes_in_cells()
        self.wu_dofs = self.get_wu_dofs_in_cells()

        self.blocks, self.block_sizes = self.decompose()

        # update raw cell's boundaries, forces, etc.
        for domain_id, domain in self.cells.items():
            domain.update_domain(self.cutted_nodes,
                                 self.user_model.FEModel.U[np.array(domain.Dofs)[:] - 1],
                                 self.create_domains_boundary_condition(domain))
