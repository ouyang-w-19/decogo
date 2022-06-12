from decogo.solver.decogo import DecogoSolver

from to_layer.config import config_decogo, Configuration_TOLayer

from models.topopt_model import inp_model


if __name__ == "__main__":

    solver = DecogoSolver()

    config_decogo()

    inp_model.configure(Configuration_TOLayer)

    solver.optimize(inp_model)


