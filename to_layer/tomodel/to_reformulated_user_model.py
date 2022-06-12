import numpy as np

from decogo.util.block_vector import SparseBlockVector

from to_layer.tomodel.todecomposer import TODecomposer


class TOReformulatedUserModel:

    base_model = None
    decomposer: TODecomposer
    blocks = []
    block_sizes = []
    sub_domains = {}
    cutted_nodes = []
    f: SparseBlockVector
    f_vals = []
    all_vars = []
    blockwise_vars = {}
    copies = []
    zeros = []
    volumes = []
    copy_relevant_vars = []

    def get_c(self, _x: np.array, _u: np.array):

        elements = np.array(list(self.base_model.elements.keys()))

        _c = 0

        for domain_id, sub_domain in self.sub_domains.items():
            _e_domains = np.array(list(sub_domain.Elements.keys()))
            _u_domain = _u[np.array(sub_domain.Dofs)[:] - 1]
            _x_domain = _x[np.array([np.where(elements == e) for e in _e_domains]).flatten()]
            _c += sub_domain.get_c(_x_domain, _u_domain)

        return _c

    def display(self):
        print("Reformulated Model:\n")
        print("New Variables:\n")
        print("\tNumber: {}\n".format(len(self.all_vars)))
        print("\tVariables: {}\n".format(self.all_vars))
        print("Copy Constraints:\n")
        print("\tNumber: {}\n".format(len(self.copies)))
        for sym in self.decomposer.symbolic_copy_constraints:
            print("\t{}".format(sym))
        print("\nNumber of cells: {}\n".format(len(self.sub_domains)))
        for i, c in self.sub_domains.items():
            print("SubDomain-ID: {}\n".format(c.SubDomain_ID))
            print("\tGlobal Nodes: {}\n".format(c.Nodes))
            print("\tGlobal DoFs: {}\n".format(c.Dofs))
            print("\tElements: {}\n".format(list(c.Elements.keys())))
            print("\tVariables: {}\n".format(self.blockwise_vars[i]))
            print("\tSubDomain specific force vector for sub problem: {}\n".format(c.FEModel.F))
            print("\tSubDomain specific fixation vector (u=0; 1 indicates that the corresponding DoF"
                  " is fixed): {}\n".format(c.FEModel.boundary_conditions.fixed_nodes))

    def __get_f_as_sparse_block_vector__(self):
        coeffs = []
        for sd_id, sub_domain in self.sub_domains.items():
            idx = np.where(sub_domain.FEModel.F != 0)[0][:]
            for i in idx:
                coeffs.append((sd_id-1, i + len(sub_domain.Elements), sub_domain.FEModel.F[i]))
        # return needs to be sparse block vector from decogo for forces in sub-domains
        return SparseBlockVector(coeffs, self.decomposer.block_sizes), coeffs

    def __get_global_volume_constraint__(self):
        global_volume_constraint = []
        for sd_id, sub_domain in self.sub_domains.items():
            block_id = sd_id - 1
            for i, (e_id, element) in enumerate(sub_domain.Elements.items()):
                global_volume_constraint.append((block_id, i, element.V))
        return global_volume_constraint

    def __determine_penalized_objective_function__(self):
        coeffs = []
        for sd_id, sub_domain in self.sub_domains.items():
            # penalized densities
            for e in range(len(sub_domain.Elements)):
                coeffs.append((sd_id - 1, e, 1))
            # force coefficients
            idx = np.where(sub_domain.FEModel.F != 0)[0][:]
            for i in idx:
                coeffs.append((sd_id - 1, i + len(sub_domain.Elements), sub_domain.FEModel.F[i]))
        # return needs to be sparse block vector from decogo for forces in sub-domains
        return SparseBlockVector(coeffs, self.decomposer.block_sizes), coeffs

    def get_one_elements(self):
        ones = []
        # loaded elements
        for domain_id, domain in self.sub_domains.items():
            for node, vec in domain.FEModel.boundary_conditions.outer_forces.items():
                for i, element in domain.Elements.items():
                    if node in element.Nodes:
                        ones.append([(domain_id - 1, list(domain.Elements.keys()).index(i), 1)])
            # fixed nodes
            for node in domain.FEModel.boundary_conditions.fixed_nodes:
                for i, element in domain.Elements.items():
                    if node in element.Nodes:
                        ones.append([(domain_id - 1, list(domain.Elements.keys()).index(i), 1)])
        return ones

    def __init__(self, base_model, decomposer: TODecomposer):
        self.base_model = base_model
        self.decomposer = decomposer
        self.blocks, self.block_sizes = self.decomposer.decompose()
        self.sub_domains = self.decomposer.cells
        self.cutted_nodes = self.decomposer.cutted_nodes
        self.f_sparse, self.f_coefficients = self.__get_f_as_sparse_block_vector__()

        self.all_vars = [self.sub_domains[c].Vars for c in self.sub_domains]
        self.all_vars = np.reshape(self.all_vars, (sum(self.block_sizes), )).tolist()

        self.blockwise_vars = {b_id: self.sub_domains[b_id].Vars for b_id in self.sub_domains}

        self.copies = self.decomposer.get_copy_constraints()
        self.zeros = self.decomposer.get_zero_constraints()

        self.volumes = self.__get_global_volume_constraint__()
        self.ones = self.get_one_elements()

        self.copy_relevant_vars = self.decomposer.mapping_copy_constraints

        self.penalized_objective_sparse, self.obj_coefficients = self.__determine_penalized_objective_function__()
