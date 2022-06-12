from pyomo.environ import *

from to_layer.pyomo.model import PymTOModel
from to_layer.fea.fea import FEModel

from typing import Type


class GlobalSolver:

    _model: ConcreteModel = None
    _solver: SolverFactory = None

    @property
    def Model(self):
        return self._model

    def solve(self, **kwargs):
        self._model.display()

        res = self._solver.solve(self._model, tee=True)
        self._model.display()
        return res

    def __init__(self, domain: FEModel):
        _m = PymTOModel(domain)
        self._model = _m.get_model()
        self._solver = SolverFactory('scipampl')
