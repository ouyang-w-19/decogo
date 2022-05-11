import os
import sys

# add Decogo source files to path
# very important to do it before importing Decogo
path = os.path.dirname(os.getcwd())
while os.path.basename(path) != 'decogo':
    path = os.path.dirname(path)
sys.path.insert(0, path)

from decogo.solver.decogo import DecogoSolver

from to_layer.config import config_decogo, Configuration_TOLayer

from tests.examples.to_problem.models.topopt_model import inp_model

if __name__ == "__main__":
    solver = DecogoSolver()

    config_decogo()

    inp_model.configure(Configuration_TOLayer)

    solver.optimize(inp_model)
