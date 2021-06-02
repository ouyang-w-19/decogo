"""Manages and stores solver settings"""

# class Settings uses dictionary of settings names and its default value
# this dictionary is used for automatic creation of attributes of the class

# in order to add the new setting just simply add the name, its default value
# with small explanation
import logging

logger = logging.getLogger('decogo')

# default settings
_setting_names_default_val = \
    {'lp_solver': 'gurobi',  # LP solver name
     'nlp_solver': 'ipopt',  # NLP solver name
     'minlp_solver': 'scip',  # MINLP solver

     'mip_solver': 'gurobi',  # MIP solver name 'gurobi', change MIP solver to
     # 'gurobi_persistent' for more solution points

     'scip_settings': [('limits/stallnodes', 1000), ('limits/gap', 0),
                       ('limits/restarts', 5)],
     'ipopt_settings': [('tol', 1e-1), ('dual_inf_tol', 1e1),
                        ('constr_viol_tol', 1e-1), ('compl_inf_tol', 1e0)],
     'gurobi_settings': [('NumericFocus', 1), ('Method', 1)],

     # general
     'strategy': 'CG',  # strategy for solver; can be 'OA' or 'CG' or
     # 'ADAPTCG' or 'DynCG'
     'maxtime': 1e10,  # maximum running time for the solver in seconds
     'logger_level': 'info',  # 'debug' - detailed info about solution
     # process, 'info' - only important information

     # Decomposition
     # estimate the bounds for unbounded variables during the decomposition
     'decomp_estimate_var_bounds': False,

     # OA
     'oa_eps_active_constraint': 0.01,  # accuracy for active constraint
     'oa_eps_rel_obj_val': 0.001,  # relative accuracy for stopping the OA
     # algorithm, i.e. c(x_star) - c(x_oa) < eps
     'oa_max_iter': 20,  # max number of iterations for main OA algorithm
     'oa_eps_start': 0.01,  # accuracy of LP solution improvement during OA start
     'oa_line_search': True,  # switch on/off line search
     'oa_fix_and_refine': False,  # switch on/off fix-and-refine

     # CG
     'cg_min_inner_point_distance': 1e-5,  # minimum distance to inner points
     'cg_generate_columns_with_nlp': False,  # True - try to generate columns
     # with NLP solver, False - with MINLP solver
     'cg_max_iter': 15,  # maximum number of iteration during CG
     'cg_add_local_cut': True,  # indicates if to add a local cut when solving
     # CG subproblem
     'cg_sub_gradient_max_iter': 5,  # maximum number of subgradient iterations
     'cg_fast_fw_max_iter': 10,  # maximum number of iteration during FW CG
     'cg_check_convergence': False, # indicates whether in the end of
     # the algorithm subproblems are solved exactly for convergence check
     'cg_max_main_iter': 20,  # maximum iteration number for
     # the main iteration
     'cg_fast_fw': True,  # to use fast fw cg instead of approx cg in start
     'cg_fast_approx': True,  # to use approx subproblem solving in fast cg
     'cg_find_solution': True,  # switch on or off find solution heuristics
     'cg_find_sol_mip_pool': 100,  # to set num of solution pool in
     # solving mip proj prob
     'cg_find_sol_mip_pool_tau': 0.5,  # to set value of tau for local
     # search of projection point
     'cg_find_sol_mip_pool_max_round': 5,  # to set max iteration of
     # local search

     # Refactory for FW/CG
     'user_defined_input_model': False,  # switch on/off user-defined input
     # model

     # Dyn-cg
     'block_agg_option': 'successive',  # select the strategy of block
     # aggregation; can be 'successive' or 'random'
     # or 'viol_copy_constr'
     'max_num_atomic_block_in_agg_block': 2,  # maximum number of atomic blocks
     # that are aggregated in a single
     # aggregated block
     'min_num_atomic_block_in_agg_block': 1,  # minimum number of atomic blocks
     'num_hyper_block_per_iter': 1,   # maximum number of hyper blocks created
     # per iteration
     'max_size_hyper_block': 2,  # maximum number of atomic blocks that are
     # combined in a single hyper block
     'hyper_block_mip_pool': 1,  # to set num of solution pool in
     # solving mip proj prob for hyper/agg sub-problems
     'creat_hyper_block_test': False,  # to test fast cg for fixed hyper blocks
     'standard_cg': False,  # to run standard cg at end of fast cg iterations
     'max_iter_fast_cg_init': 15,  # maximum iteration number for
     # fast cg for atomic blocks
     'max_iter_fast_cg_hyper': 5,  # maximum iteration number for
     # fast cg for hyper blocks
     'max_iter_fast_cg_active': 3,  # maximum iteration number for
     # fast cg for active blocks
     'max_iter_standard_cg': 5,  # maximum iteration number for
     # fast cg for active blocks


     }


class Settings:
    """Class which stores all settings. The attributes in the are not set
    explicitly in the constructor method. Instead they are set dynamically
    from the dictionary with default values defined above. Non-default
    settings should be set in the file decogo.set, which should be located
    in the working directory of the script
    """

    def __init__(self):
        """Constructor method"""
        # create attributes and assign the default values
        for key in _setting_names_default_val.keys():
            self.__setattr__(key, _setting_names_default_val[key])

        # read non default settings from file
        non_def_settings = self._settings_file_reader()

        self._validate_non_default_settings(non_def_settings)

        # assign non default settings
        for key in non_def_settings.keys():
            self.__setattr__(key, non_def_settings[key])

    def _settings_file_reader(self):
        """Reads non-default settings from file decogo.set
        (located in the working directory). The file should should be in the
        following form:

        setting1 = value1
        setting2 = value2
        """

        def isnumber(x):
            """Utility function, which checks if the character
            string is a number"""
            try:
                float(x)
                return True
            except ValueError:
                return False

        def isbool(x):
            """Utility function which checks if the character
            is a boolean value"""
            x = x.lower()
            if x == 'true' or x == 'false':
                return True

        def str2bool(x):
            """Utility function, which converts string to boolean value"""
            if x == 'True' or x == 'true':
                return True
            elif x == 'False' or x == 'false':
                return False

        non_def_settings = {}
        try:
            with open('decogo.set') as f:
                data = f.readlines()
                for line in data:
                    splitted_line = line.split('=')

                    # remove whitespaces at the beginning and at the end
                    splitted_line = [item.strip() for item in splitted_line]

                    # check if setting is a number or boolean
                    if isnumber(splitted_line[1]):
                        non_def_settings[splitted_line[0]] = \
                            float(splitted_line[1])
                    elif isbool(splitted_line[1]):
                        non_def_settings[splitted_line[0]] = \
                            str2bool(splitted_line[1])
                    else:
                        non_def_settings[splitted_line[0]] = splitted_line[1]
        except FileNotFoundError:
            # if the file is not found, then default settings are used
            pass

        return non_def_settings

    def _validate_non_default_settings(self, settings):
        """Validates nondefault settings, i.e. checks if the values of the
        settings are in the right form

        :param settings: Dictionary of settings
        :type settings: dict
        :raises ValueError: Invalid for value for some setting
        """
        for key in settings:
            if key == 'strategy':
                if settings[key] not in ['OA', 'CG', 'ADAPTCG', 'DynCG']:
                    raise ValueError(
                        'Invalid value for setting \'{0}\'. '
                        'It must be a string.'.format(key))
            elif key == 'block_agg_option':
                if settings[key] not in [ 'successive', 'random', 'viol_copy_constr']:
                    raise ValueError(
                        'Invalid value for setting \'{0}\'. '
                        'It must be a string.'.format(key))
            elif key == 'cg_subproblem_sol_percent':
                if type(settings[key]) not in [int, float]:
                    raise ValueError('Invalid value for setting \'{0}\'. '
                                     'It must be int or float.'.format(key))
                else:
                    if settings[key] > 100 or settings[key] < 0:
                        raise ValueError('Invalid value for setting \'{0}\'. '
                                         'It must be from 0 to 100.'.format(key))
            elif 'solver' in key:
                if type(settings[key]) is not str:
                    raise ValueError(
                        'Invalid value for setting \'{0}\'. '
                        'It must be a string.'.format(key))
            else:
                if type(settings[key]) not in [bool, float]:
                    raise ValueError('Invalid value for setting \'{0}\'. '
                                     'It must be float or bool.'.format(key))

    def get_minlp_solver_options(self):
        """Gets MINLP solver options

        :return: List of nondefault options for external solver
        :rtype: list
        """
        solver_options = None
        if self.minlp_solver == 'scip':
            if len(self.scip_settings) > 0:
                solver_options = self.scip_settings

        return solver_options

    def get_nlp_solver_options(self):
        """Gets NLP solver options

        :return: List of nondefault options for external solver
        :rtype: list
        """
        solver_options = None
        if self.nlp_solver == 'ipopt':
            if len(self.ipopt_settings) > 0:
                solver_options = self.ipopt_settings

        return solver_options

    def get_lp_solver_options(self):
        """Gets NLP solver options

        :return: List of nondefault options for external solver
        :rtype: list
        """
        solver_options = None
        if self.lp_solver == 'gurobi':
            if len(self.gurobi_settings) > 0:
                solver_options = self.gurobi_settings

        return solver_options
