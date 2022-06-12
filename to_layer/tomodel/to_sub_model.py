import numpy as np

from decogo.model.input_model_base import SubModelBase
from decogo.model.constraints import VarDomain

from to_layer.tomodel.subdomain import SubDomain


class TOSubModel(SubModelBase):

    nonlin_constr = [1]

    integer: bool = False

    int_mapper = {
        True: 'int',
        False: 'real'
    }

    # Stabilization Section
    bar_uk: np.array = None
    # ---------------------

    def get_one_indices(self):
        oi = []
        for one in self.inp_model.model.ones:
            for cons in one:
                if cons[0] == self.block_id:
                    oi.append(cons[1])
        return oi

    def __init__(self, model, vars_in_block, block_id):

        super().__init__(vars_in_block=vars_in_block, block_id=block_id)

        self.ref_model = model.model
        self.inp_model = model

        self.block_id = block_id
        self.linear = False
        self.integer = self.inp_model.integer

        self.one_constraint = self.get_one_indices()

        self.sub_domain: SubDomain = self.ref_model.sub_domains[block_id + 1]

        self.nonlin_constr = [1]

        # bar_uk is required for stabilizer
        self.bar_uk = self.inp_model.model.base_model.FEModel.U[np.array(self.sub_domain.Dofs)[:] - 1]

        # Variables Creation
        for i, var in enumerate(vars_in_block):

            if str(var).startswith('x_'):

                if self.inp_model.penalization_approach:

                    self.variables.append(VarDomain(self.inp_model.x_max,
                                                    0, self.int_mapper[self.integer]))
                else:
                    self.variables.append(VarDomain(1, 0, self.int_mapper[self.integer]))

            else:
                self.variables.append(VarDomain(self.sub_domain.FEModel.u_bounds[1][i-len(self.sub_domain.Elements)],
                                                self.sub_domain.FEModel.u_bounds[0][i-len(self.sub_domain.Elements)],
                                                'real'))

        # End Variables Creation
        """
        # p_k: Global Constraints P acc. to block k
        self.p_k = []
        for cut in self.inp_model.cuts.global_cuts:
            if self.block_id in cut.lhs.blocks:
                self.p_k.append(cut)

        # self.ak = self.__get_global_constraint_factors()

        # self.Ak = self.__create_resource_matrix__()
        """
