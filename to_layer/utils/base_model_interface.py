from to_layer.utils.node import Node
from to_layer.elements.element import Element
from to_layer.tomodel.boundary_condition import BoundaryConditions
from typing import List, Dict


class BaseModelInterface:
    """
    flag = 0 -> fixed node
    flag = 1 -> loaded node
    """

    _model_dict: dict = None

    _node_dict: dict = None
    _element_dict: dict = None
    _boundary_dict: dict = None
    BaseModelDict: dict = None

    def get_model_dict(self):
        return {'nodes': self._node_dict,
                'elements': self._element_dict,
                'boundary_conditions': self._boundary_dict}

    def __init__(self, _nodes: Dict[int, Node], _elements: Dict[int, Element], _bc: BoundaryConditions):
        self._node_dict = {i: {'coords': [n.x, n.y, n.z], 'flag': 0}
                           for i, n in _nodes.items()}

        # raw dict for elements
        self._element_dict = {}
        for e_id, e in _elements.items():
            self._element_dict[e_id] = {'type': 3, 'nodes': list(e.Nodes.keys())}

        self._boundary_dict = {
            'fixed_nodes': list(map(int, _bc.fixed_nodes)),
            'fixed_dofs': _bc.fixed_dofs.tolist(),
            'force_dict': {int(n): vec.tolist() for n, vec in _bc.outer_forces.items()},
            'force_vector': _bc.force_vector.tolist()
        }

        self.BaseModelDict = self.get_model_dict()
