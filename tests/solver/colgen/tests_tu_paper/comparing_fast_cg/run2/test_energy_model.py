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
    superstructure = 'S4'
    load_case = 'L4'
    load_cases_per_block = 6
    data_instance = 1

    model = generate_model(superstructure, load_case, load_cases_per_block,
                           data_instance)

    # I removed the part of the code which runs the same model sequentially,
    # it takes time and it is not so important, therefore
    # I would not concentrate on making sequential runs
    with open('decogo.set', 'w') as file:
        file.write('strategy = DIOR\n')
        file.write('maxtime = 172800\n')
        file.write('cg_max_iter = 5\n')
        file.write('cg_sub_gradient_max_iter = 3\n')
        file.write('decomp_estimate_var_bounds = False\n')
        file.write('cg_normalize_duals = False\n')
        file.write('dior_inner_outer_max_iter = 1\n')    # loop 2
        file.write('cg_max_main_iter = 20\n')  # loop 3
        # ========================= primal heuristics =========================
        file.write('dior_find_sol_rho = 0.9\n')  # set rho value for nlp
        # resource proj problem
        file.write('cg_find_solution = False\n')  # comment to switch off
        # findSol
        file.write('dior_mip_proj_target_const = True\n')  # target const
        # ----------------------------------------- switching
        # file.write('dior_find_sol_mip_option = True \n')  # use FindSol
        # file.write('dior_find_sol_feasibility_pump = True \n')  # use
        # FindSol_FP
        file.write('dior_find_sol_perturb_heu = True \n')  # use
        # FindSol_perturbed_heu
        # -----------------------------------------
        # ----------------------------------------- switching
        # file.write('dior_nlp_resource_proj_option_mip = True\n')  # using mip
        # for blockwise fixing
        # file.write('dior_nlp_resource_proj_option_rounding = True\n')  # using
        # # rounding for blockwise fixing
        # -----------------------------------------
        file.write('dior_fp_nlp_perturb_resource_proj = True\n')  # using nlp
        # perturb resource proj in find_sol_fp
        # ===================================================================
        file.write('dior_ioa_refine_fw_iter_max = 50 \n')
        # file.write('dior_ioa_refine_fw_option = False\n')  # solve conv_hull
        # # using ipopt
        file.write('dior_ioa_refine_fw_t_param = 0.2\n')  # t_param

        file.write('cg_fast_fw = False\n')  # switch off fast CG
        # file.write('cg_fast_approx = False\n')  # using exact problem
        # solving in fast CG
        file.write('cg_subproblem_sol_percent = 40\n')

        file.close()

    solver = DecogoSolver()
    file_name = 'DESS_model_{0}{1}_{2}_fw_off.txt'.format(
        superstructure, load_case, data_instance)
    solver.optimize(model, file_name)
    # solver.optimize(model)
