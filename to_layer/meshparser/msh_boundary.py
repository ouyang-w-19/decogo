# maps the dimension of an element to a geometry
MappingDimToGeometry = {
    0: "point",
    1: "curve",
    2: "plane",
    3: "space"
}


class MSHBoundary:
    """
    mainly stores data, also maps dimension to a geometry
    """
    physical_dimension: int = 0
    tag: int = 0
    name: str = ""
    boundary_geometry: str = ""

    def __init__(self, dim, tag, name):
        self.physical_dimension = dim
        self.tag = tag
        self.name = name
        self.boundary_geometry = MappingDimToGeometry[self.physical_dimension]
