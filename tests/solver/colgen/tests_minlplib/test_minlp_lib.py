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
    problem_names = ['batch']

    # solver settings
    tau = 0.5
    pool_size = 100
    max_round = 5

    with open('decogo.set', 'w') as file:
        # file.write('strategy = ADAPTCG\n')  # static hyper-blocks (aggregating
        # two nonlinear atomic blocks)
        file.write('strategy = CG\n')
        file.write('maxtime = 1000\n')
        file.write('cg_max_iter = 5\n')
        file.write('cg_sub_gradient_max_iter = 3\n')
        file.write('decomp_estimate_var_bounds = False\n')
        file.write('cg_normalize_duals = False\n')
        file.write('cg_max_main_iter = 20\n')  # main iteration limit
        # ========================= primal heuristics =========================
        file.write('cg_find_solution = True\n')
        file.write('cg_find_sol_mip_pool = ' + str(pool_size) + '\n')
        file.write('cg_find_sol_mip_pool_tau = ' + str(tau) + '\n')
        file.write('cg_find_sol_mip_pool_max_round = ' + str(max_round) + '\n')
        # ===================================================================
        file.write('cg_fast_fw = False\n')  # switch off fast CG
        # file.write('cg_fast_fw = True\n')  # switch on fast CG
        file.write('cg_fast_approx = True\n')  # using exact problem
        # solving in fast CG

        file.close()

    # add tests to the test class
    for name in problem_names:
        module_obj = \
            importlib.import_module('tests.examples.minlplib.' + str(name))
        input_model = module_obj.model
        input_model.name = name

        # solution with Decogo
        solver = DecogoSolver()
        file_name='logs\\MINLPlib\\' + name + '.txt'
        # solver.optimize(input_model, file_name=file_name)
        solver.optimize(input_model)

