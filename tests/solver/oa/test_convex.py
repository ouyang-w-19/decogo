import importlib
import os
import sys

# add Decogo source files to path
# very important to do it before importing Decogo
path = os.path.dirname(os.getcwd())
while os.path.basename(path) != 'decogo':
    path = os.path.dirname(path)
sys.path.insert(0, path)

from decogo.solver.decogo import DecogoSolver

if __name__ == '__main__':

    # 'batchdes', 'syn05h', 'batch', 'batch0812', 'fac1', 'fac2', 'fac3',
    # 'syn05h', 'syn10h', 'tls2', 'clay0305h'
    problem_names = ['batchdes']

    # solver settings
    with open( 'decogo.set', 'w') as file:
        file.write("maxtime = 5400\n")
        file.write('strategy = OA\n')
        file.write('decomp_estimate_var_bounds = True')
        file.close()

    for name in problem_names:
        module_obj = \
            importlib.import_module('tests.examples.minlplib.' + str(name))
        input_model = module_obj.model
        input_model.name = name

        # solution with Decogo
        solver = DecogoSolver()
        # file_name='logs\\convex_examples\\' + name + '.txt'
        solver.optimize(input_model)

