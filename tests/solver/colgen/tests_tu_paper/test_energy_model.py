import os
import sys

# add Decogo source files to path
# very important to do it before importing Decogo
path = os.path.dirname(os.getcwd())
while os.path.basename(path) != 'decogo':
    path = os.path.dirname(path)
sys.path.insert(0, path)

from decogo.solver.decogo import DecogoSolver
from tests.examples.tu.DESSLib_testmodel.DESS_blockstructure import \
    generate_model

if __name__ == '__main__':
    superstructure = 'S4'
    load_case = 'L4'
    load_cases_per_block = 6
    data_instance = 1
    tau = 0.5
    pool_size = 100
    max_round = 5
    n_runs = 1

    model = generate_model(superstructure, load_case, load_cases_per_block,
                           data_instance)

    for i in range(1, n_runs + 1):
        # create setting file
        with open('decogo.set', 'w') as file:
            # ================= refactory colgen ===============================
            file.write('strategy = CG\n')
            file.write('user_defined_input_model = False\n')
            # switch off user-defined input model
            # ================== CG settings ===================================
            file.write('maxtime = 1000\n')  # maximum computation/solving time
            file.write('cg_max_iter = 5\n')
            file.write('cg_sub_gradient_max_iter = 3\n')
            file.write('decomp_estimate_var_bounds = False\n')
            file.write('cg_normalize_duals = False\n')
            file.write('cg_max_main_iter = 20\n')  # main iteration limit
            file.write('cg_fast_fw = False\n')  # switch off fast CG
            file.write('cg_fast_approx = True\n')  # using exact problem
            # solving in fast CG
            # ========================= primal heuristics ======================
            file.write('cg_find_solution = True\n')
            file.write('cg_find_sol_mip_pool = ' + str(pool_size) + '\n')
            file.write('cg_find_sol_mip_pool_tau = ' + str(tau) + '\n')
            file.write(
                'cg_find_sol_mip_pool_max_round = ' + str(max_round) + '\n')
            # ==================================================================
            file.close()

        solver = DecogoSolver()
        # file_name = 'DESS_model_{0}{1}_{2}_pool_size_{3}_tau_{4}' \
        #             '_max_search_round_{5}_run_{6}.txt'.format(
        #                 superstructure, load_case, data_instance,
        #                 pool_size, tau, max_round, i)
        # solver.optimize(input_model, file_name=file_name)  # generate log file
        result = solver.optimize(model)
