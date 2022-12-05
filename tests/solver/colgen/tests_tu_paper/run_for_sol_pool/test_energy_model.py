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
    superstructure = 'S16'
    load_case = 'L16'
    load_cases_per_block = 6
    data_instance = 1
    tau = 0.5
    pool_size = 100
    max_round = 5
    example = 1

    model = generate_model(superstructure, load_case, load_cases_per_block,
                           data_instance)


    with open('decogo.set', 'w') as file:
        file.write('strategy = DIOR\n')
        file.write('maxtime = 43200\n')
        file.write('cg_max_iter = 5\n')
        file.write('cg_sub_gradient_max_iter = 3\n')
        file.write('decomp_estimate_var_bounds = False\n')
        file.write('cg_normalize_duals = False\n')
        file.write('cg_max_main_iter = 20\n')  # main iteration limit
        # ========================= primal heuristics =========================
        file.write('cg_find_solution = True\n')  # comment to switch off
        # findSol
        file.write('dior_mip_proj_target_const = True\n')  # target const
        # ----------------------------------------- switching
        file.write('dior_find_sol_mip_option = False \n')  # use FindSol
        file.write('dior_find_sol_feasibility_pump = False \n')  # use
        # FindSol_FP
        file.write('dior_find_sol_perturb_heu = True \n')  # use
        # FindSol_perturbed_heu
        file.write('cg_find_sol_mip_pool = ' + str(pool_size) + '\n')
        file.write('cg_find_sol_mip_pool_tau = ' + str(tau) + '\n')
        file.write('cg_find_sol_mip_pool_max_round = ' + str(max_round) + '\n')
        # -----------------------------------------
        # ----------------------------------------- switching
        # file.write('dior_nlp_resource_proj_option_mip = True\n')  # using mip
        # for blockwise fixing
        # file.write('dior_nlp_resource_proj_option_rounding = True\n')  # using
        # # rounding for blockwise fixing
        # -----------------------------------------
        file.write('dior_fp_nlp_perturb_resource_proj = False\n')  # using nlp
        # perturb resource proj in find_sol_fp
        # ===================================================================
        file.write('cg_fast_fw = True\n')  # switch off fast CG
        file.write('cg_fast_approx = True\n')  # using exact problem
        # solving in fast CG

        file.close()

    solver = DecogoSolver()
    file_name = 'DESS_model_{0}{1}_{2}_pool_size_{3}_tau_{4}_max_search_round_{5}_ex_{6}.txt'.format(
        superstructure, load_case, data_instance, pool_size, tau, max_round, example)
    solver.optimize(model, file_name)

    os.remove('decogo.set')
