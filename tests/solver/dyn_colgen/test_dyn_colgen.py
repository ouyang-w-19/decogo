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

    # NLP: st_e05 st_e30 st_e31 st_glmp_kky ex5_4_2 ex7_2_4 ex8_4_1 alkyl chain50
    # pooling_adhya1pq pooling_adhya2stp pooling_adhya2pq ex9_2_3 wastewater02m1
    # kall_congruentcircles_c62 weapons

    # MINLP: tln2 graphpart_3pm-0234-0234 graphpart_3pm-0244-0244
    # graphpart_3pm-0244-0244 sfacloc2_2_95
    # genpooling_meyer04 otpop sssd20-04persp sssd25-04persp util

    problem_names = ['sssd25-04persp']

    with open('decogo.set', 'w') as file:
        file.write('strategy = DynCG\n')
        file.write('maxtime = 1000\n') # 12 hours
        file.write('cg_max_iter = 5\n')
        file.write('cg_sub_gradient_max_iter = 3\n')
        file.write('decomp_estimate_var_bounds = False\n')

        file.close()

    for name in problem_names:
        module_obj = \
            importlib.import_module('tests.examples.minlplib.' + str(name))
        input_model = module_obj.model
        input_model.name = name

        # solution with Decogo
        solver = DecogoSolver()
        # file_name='logs\\' + name + '.txt'
        solver.optimize(input_model, file_name=None)
