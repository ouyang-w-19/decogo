import numpy as np


def get_indices_from_two_arrays(main: np.ndarray, sub: np.ndarray):
    _idx = np.array([np.where(s == main) for s in sub])
    _idx = np.reshape(_idx, (len(_idx, )))
    return _idx


# TODO: ATTENTION: Only works for 2 dofs at the moment
def get_dofs(n):
    return np.array([2 * n - 1, 2 * n])


def visualize_object(obj: object):
    none_user_props = ["__dict__", "__weakref__", "__doc__", "__init__", "__module__"]
    print("Object: {}".format(obj.__class__.__name__))
    for key, value in obj.__dict__.items():
        if key not in none_user_props:
            print("{}: {}".format(key, type(value)))


def create_random_point(fe_model, x: np.array, threshold: tuple = (0.2, 0.2),
                        f_range=float(0),
                        binary: bool = False,
                        ones: list = None):
    """
    Create a random point which is similar to a given x distribution
    :param fe_model: Domain's FE-Model
    :param x: Density Distribution
    :param threshold: Decision Factor for a fractional density
    :param f_range: Defines a percentage range for the pertubation the force vector
    :param binary: differs between binary or continuous variables
    :param ones: provide indices where x needs to be 1
    :return: random x and u
    """
    # pertubate x
    x_pert = np.zeros_like(x)
    for i, _x in np.ndenumerate(x):
        if _x > threshold[1]:
            x_pert[i] = 1
        elif _x < threshold[0]:
            x_pert[i] = 0
        else:
            if binary:
                x_pert[i] = np.random.randint(0, 2, 1)[0]
            else:
                x_pert[i] = np.random.uniform(0, 1, 1)[0]

    if ones is not None:
        for i in ones:
            x_pert[i] = 1

    # pertubate f
    _f = fe_model.F * np.random.uniform(low=1 - f_range / 2, high=1 + f_range / 2, size=len(fe_model.F))
    # update FEModel
    # fe_model.F = _f
    fe_model.K = fe_model.get_k(_x=x_pert)
    if len(fe_model.boundary_conditions.fixed_nodes) > 0:
        fe_model.K, _f = fe_model.incorporate_boundary_conditions(fe_model.K, _f)
    u = fe_model.solve(f_user=_f)[0]

    return x_pert, u


def penalization_function(x: np.array, y_p=float(1)):
    """
    Penalizes x-values which are not binary
    :param x: original density distribution from SIMP as array
    :param y_p: Penalization Factor >= 1
    :return: Penalized Density Distribution
    """
    return - 4 * y_p * (x[:] ** 2 - x[:])


def reward_function(x: np.array, y_p=float(1)):
    """
    Transforms penalized values back to physical ones, inverse function of penalization function
    :param x: Penalized density values as array
    :param y_p: Penalization Factor >=1
    :return: Physical Density Distribution
    """
    return -0.5 * (np.sqrt(-(x[:] / y_p) + 1) - 1)

