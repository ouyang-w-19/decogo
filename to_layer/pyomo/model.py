import numpy as np

from pyomo.environ import *
from to_layer.fea.fea import FEModel


class PymTOModel:

    _domain: FEModel = None
    _max_allowed_stress = 300

    complete_force_vector: np.array = None
    original_force_vector: np.array = None
    boundary_force_vector: np.array = None

    def __init__(self, domain: FEModel):
        self._domain = domain

        self.boundary_force_vector = self._domain.boundary_conditions.boundary_forces_vec
        self.original_force_vector = self._domain.boundary_conditions.outer_forces_vec
        self.complete_force_vector = self.original_force_vector + self.boundary_force_vector

    def get_model(self):
        """
        defines the initial Pyomo-Model depending on a FEModel
        :return: Concrete Model
        """
        m = ConcreteModel()
        u_init = self._domain.solve()[0]

        init_data = {i: u_init[i] for i in range(len(self._domain.global_dofs))}
        # define indices
        m.IDX_elements = Set(initialize=list(self._domain.elements.keys()))
        m.IDX_dofs = RangeSet(0, len(self._domain.global_dofs) - 1)

        # define parameters
        m.F = Param(m.IDX_dofs,
                    initialize={i: self.complete_force_vector[i] for i in range(len(self._domain.global_dofs))})

        # define variables
        m.rho = Var(m.IDX_elements, within=Binary, initialize=1)
        m.u = Var(m.IDX_dofs, bounds=(-1e3, 1e3), initialize=init_data)

        # define objective
        def objective_rule(_m):
            return sum(_m.rho[e] for e in _m.IDX_elements)
        m.objective = Objective(rule=objective_rule)

        # define elasticity constraint
        def elasticity_rule(_m, _i):
            lhs = 0
            _global_i = self._domain.global_dofs[_i]
            for _j in range(len(self._domain.global_dofs)):
                _global_j = self._domain.global_dofs[_j]
                for e_id, element in self._domain.elements.items():
                    if _global_i in element.DoFHelper and _global_j in element.DoFHelper:
                        _i_index = np.where(element.DoFHelper == _global_i)[0][0]
                        _j_index = np.where(element.DoFHelper == _global_j)[0][0]
                        lhs += _m.rho[e_id] * element.Ke0[_i_index, _j_index] * _m.u[_j]
            return lhs == self.complete_force_vector[_i]
        m.elasticity_constraint = Constraint(m.IDX_dofs, rule=elasticity_rule)

        # define stress constraint
        def stress_rule(_m, _e):
            _bq = []
            _bq_temp = 0
            _sigma = []
            _sigma_temp = 0
            _element = self._domain.elements[_e]

            _stress_components = _element.stress_components
            for _i in range(_stress_components):
                _bq_temp = 0
                for _j in _element.DoFHelper:
                    _j_index = np.where(np.array(_element.DoFHelper) == _j)[0][0]
                    _bq_temp += _element.B[_i, _j_index] * _m.u[_j]
                _bq.append(_bq_temp)

            for _i in range(_stress_components):
                _sigma_temp = 0
                for _j in range(_stress_components):
                    _sigma_temp += _element.E[_i, _j] * _bq[_j]
                _sigma.append(_sigma_temp)
            return 0, _sigma[0] ** 2 + _sigma[1] ** 2 - _sigma[0] * _sigma[1] + 3 * _sigma[2] ** 2, 600
        m.stress_constraint = Constraint(m.IDX_elements, rule=stress_rule)

        return m
