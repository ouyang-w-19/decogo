import numpy as np


class Node:
    # General Properties
    nid = int(0)
    index = int(0)
    x = float(0.0)
    y = float(0.0)
    z = float(0.0)

    n_vec = np.array([x, y, z])

    # Displacement properties
    dx = float(0.0)
    dy = float(0.0)
    dz = float(0.0)
    dn_vec = np.array([dx, dy, dz])

    # Force properties
    fx = float(0.0)
    fy = float(0.0)
    fz = float(0.0)
    f_vec = np.array([fx, fy, fz])

    # Helpers
    # TODO: Implement it in BaseModel
    attached_elements = []

    def __init__(self, nid, x, y, z=0, index=-1):

        self.nid = nid
        self.index = index

        self.x = x
        self.y = y
        self.z = z

        self.n_vec = np.array([x, y, z])
