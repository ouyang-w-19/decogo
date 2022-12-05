import os
import sys

# add Decogo source files to path
# very important to do it before importing Decogo
path = os.path.dirname(os.getcwd())
while os.path.basename(path) != 'decogo':
    path = os.path.dirname(path)
sys.path.insert(0, path)

from decogo.solver.decogo import DecogoSolver
from tests.examples.tu.DESSLib_testmodel.DESS_blockstructure import generate_model

if __name__ == '__main__':
    # instance setting:
    superstructure = 'S4'
    load_case = 'L4'
    load_cases_per_block = 6
    data_instance = 1

    # solve the same instance n_runs times
    n_runs = 1

    # primal heuristic setting:
    tau = 0.5
    pool_size = 50
    max_round = 5

    # CG setting
    standard_cg = True
    max_standard_cg = 3

    # hyper block setting
    n_hyper_block = 2
    size_hyper_block = 4

    model = generate_model(superstructure, load_case, load_cases_per_block,
                           data_instance)

    for i in range(1, n_runs + 1):  # run multiple times
        # create setting file
        with open('decogo.set', 'w') as file:
            # ================= dyn block colgen ===============================
            file.write('strategy = DBCG\n')
            file.write('user_defined_input_model = False\n')  # disable
            # user-defined model
            # ================== CG settings ===================================
            file.write('maxtime = 43200\n')  # 12 hours
            file.write('cg_max_iter = 5\n')
            file.write('cg_sub_gradient_max_iter = 3\n')
            file.write('decomp_estimate_var_bounds = False\n')
            file.write('cg_fast_fw_max_iter = 5\n')
            file.write('cg_max_main_iter = 5\n')
            file.write('num_hyper_block_per_iter = 2\n')
            file.write('max_iter_fast_cg_init = 10\n')
            file.write('max_iter_fast_cg_hyper = 4\n')
            file.write('max_iter_fast_cg_active = 2\n')
            file.write('max_iter_standard_cg = ' + str(max_standard_cg) + '\n')
            file.write('standard_cg = ' + str(standard_cg) + '\n')
            file.write('num_hyper_block_per_iter = '
                       '' + str(n_hyper_block) + '\n')
            file.write('max_size_hyper_block = ' + str(size_hyper_block) + '\n')
            # ========================= primal heuristics ======================
            file.write('cg_find_solution = True\n')
            file.write('cg_find_sol_mip_pool = ' + str(pool_size) + '\n')
            file.write('cg_find_sol_mip_pool_tau = ' + str(tau) + '\n')
            file.write('cg_find_sol_mip_pool_max_round = '
                       + str(max_round) + '\n')
            file.close()

        solver = DecogoSolver()
        # file_name = '{0}{1}_{2}_pool_{3}_num_{4}_size_{5}_standard_cg_{6}-' \
        #             '{7}.txt'.format(superstructure, load_case, data_instance,
        #                              pool_size, n_hyper_block,
        #                              size_hyper_block, max_standard_cg, i)
        # solver.optimize(input_model, file_name=file_name)  # generate log file
        solver.optimize(model)
