import os

WD = os.getcwd()


Configuration_TOLayer = {
    'use_stabilizer': False,
    'use_penalization_approach': False,
    'integer_consideration': False,
    'is_reported': True,
    'report_name': 'NLP',

    'SimpProblem': {
        'volfrac': 0.44,
        'penalization_factor': 3,
        'emin': 1e-9,
        'emax': 1,
        'rmin': 1.44,
        'filter': 'sensitivity'
    },

    'FEModel': {
        'preferred_solver': 'direct'
    },

    'Pertubation': {
        'adding_points': 10,
        'fast_sol_simp_iter': 10,
        'threshold': (0.3, 0.7),  # (lower upper)
        'force_range': 0.4
    },

    'CGPenalization': {
        'factor': 2.0
    },
    'CGStabilizer': {
        'delta': 1.0,
        'eps': 1.0
    }

}


def config_decogo():

    with open('decogo.set', 'w') as file:
        file.write('strategy = CG\n')
        file.write('maxtime = 1000\n')  # 12 hours
        file.write('cg_max_iter = 5\n')
        file.write('cg_sub_gradient_max_iter = 5\n')
        file.write('decomp_estimate_var_bounds = False\n')
        file.write('cg_normalize_duals = False\n')
        file.write('cg_max_main_iter = 5\n')  # main iteration limit
        # ========================= primal heuristics =========================
        file.write('cg_find_solution = True\n')
        # ===================================================================
        file.write('cg_fast_fw = False\n')  # switch off fast CG
        file.write('cg_fast_approx = False\n')  # using exact problem
        # solving in fast CG
        # ===================================================================
        # switch on user-defined input model
        file.write('user_defined_input_model = True\n')
        # test parameters
        file.write('lp_solver = gurobi\n')
        file.write('cg_check_convergence = True\n')
        file.write('cg_generate_columns_with_nlp = False')
        file.close()

        return True
