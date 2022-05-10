# returns the same as from topy or topopt model
# required for creating element-objects
import numpy as np


rs = {
        1: (-1, -1),
        2: (1, -1),
        3: (1, 1),
        4: (-1, 1)
    }

shape_functions = {
        1: lambda r, s: 1 / 4 * (1 - r) * (1 - s),
        2: lambda r, s: 1 / 4 * (1 + r) * (1 - s),
        3: lambda r, s: 1 / 4 * (1 + r) * (1 + s),
        4: lambda r, s: 1 / 4 * (1 - r) * (1 + s),
}

# sub stiffness matrix of a simple C2D4 element
def __k_sub__(__nu):
    return np.array([1 / 2 - __nu / 6,
                     1 / 8 + __nu / 8,
                     -1 / 4 - __nu / 12,
                     -1 / 8 + 3 * __nu / 8,
                     -1 / 4 + __nu / 12,
                     -1 / 8 - __nu / 8,
                     __nu / 6,
                     1 / 8 - 3 * __nu / 8])

# returns the stiffness matrix depending on the Young's Modulus and the poission's ratio
def ke(e, nu):
    k = __k_sub__(nu)
    return e / (1 - nu ** 2) * np.array([[k[0], k[1], k[2], k[3], k[4], k[5], k[6], k[7]],
                                         [k[1], k[0], k[7], k[6], k[5], k[4], k[3], k[2]],
                                         [k[2], k[7], k[0], k[5], k[6], k[3], k[4], k[1]],
                                         [k[3], k[6], k[5], k[0], k[7], k[2], k[1], k[4]],
                                         [k[4], k[5], k[6], k[7], k[0], k[1], k[2], k[3]],
                                         [k[5], k[4], k[3], k[2], k[1], k[0], k[7], k[6]],
                                         [k[6], k[3], k[4], k[1], k[2], k[7], k[0], k[5]],
                                         [k[7], k[2], k[1], k[4], k[3], k[6], k[5], k[0]]])

