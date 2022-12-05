import os
import sys
from pyomo.environ import *

# add Decogo source files to path
# very important to do it before importing Decogo
path = os.path.dirname(os.getcwd())
while os.path.basename(path) != 'decogo':
    path = os.path.dirname(path)
sys.path.insert(0, path)

from decogo.solver.decogo import DecogoSolver
from decogo.pyomo_minlp_model.input_model import PyomoInputModel

if __name__ == '__main__':
    # region define Pyomo model

    model = m = ConcreteModel()

    m.x1 = Var(within=Reals, bounds=(0, 1.38629436111989), initialize=0)
    m.x2 = Var(within=Reals, bounds=(0, 1.38629436111989), initialize=0)
    m.x3 = Var(within=Reals, bounds=(0, 1.38629436111989), initialize=0)
    m.x4 = Var(within=Reals, bounds=(0, 1.38629436111989), initialize=0)
    m.x5 = Var(within=Reals, bounds=(0, 1.38629436111989), initialize=0)
    m.x6 = Var(within=Reals, bounds=(0, 1.38629436111989), initialize=0)
    m.x7 = Var(within=Reals, bounds=(5.7037824746562, 8.00636756765025),
               initialize=5.7037824746562)
    m.x8 = Var(within=Reals, bounds=(5.7037824746562, 8.00636756765025),
               initialize=5.7037824746562)
    m.x9 = Var(within=Reals, bounds=(5.7037824746562, 8.00636756765025),
               initialize=5.7037824746562)
    m.x10 = Var(within=Reals, bounds=(5.7037824746562, 8.00636756765025),
                initialize=5.7037824746562)
    m.x11 = Var(within=Reals, bounds=(5.7037824746562, 8.00636756765025),
                initialize=5.7037824746562)
    m.x12 = Var(within=Reals, bounds=(5.7037824746562, 8.00636756765025),
                initialize=5.7037824746562)
    m.x13 = Var(within=Reals, bounds=(4.45966, 397.747), initialize=4.45966)
    m.x14 = Var(within=Reals, bounds=(3.7495, 882.353), initialize=3.7495)

    x_index = [15, 16, 17, 18, 19]
    m.x_index = Set(initialize=x_index)
    m.x = Var(m.x_index, within=Reals)
    m.x[15].value = 4.49144
    m.x[16].value = 3.14988
    m.x[17].value = 3.04452
    m.x[18].value = 0.729961
    m.x[19].value = 0.530628
    m.x[15].setub(833.333)
    m.x[16].setub(638.298)
    m.x[17].setub(666.667)
    m.x[18].setub(2.11626)
    m.x[19].setub(1.91626)
    m.x[15].setlb(4.49144)
    m.x[16].setlb(3.14988)
    m.x[17].setlb(3.04452)
    m.x[18].setlb(0.729961)
    m.x[19].setlb(0.530628)

    m.x20 = Var(within=Reals, bounds=(1.09024, 2.47654), initialize=1.09024)
    m.x21 = Var(within=Reals, bounds=(-0.133531, 1.25276), initialize=0)
    m.x22 = Var(within=Reals, bounds=(0.0487901, 1.43508), initialize=0.0487901)
    m.b23 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b24 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b25 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b26 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b27 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b28 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b29 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b30 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b31 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b32 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b33 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b34 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b35 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b36 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b37 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b38 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b39 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b40 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b41 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b42 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b43 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b44 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b45 = Var(within=Binary, bounds=(0, 1), initialize=0)
    m.b46 = Var(within=Binary, bounds=(0, 1), initialize=0)

    m.obj = Objective(expr=250 * exp(m.x1 + 0.6 * m.x7) + 250 * exp(
        m.x2 + 0.6 * m.x8) + 250 * exp(m.x3 + 0.6 * m.x9) + 250 * exp(m.x4 +
                                                                      0.6 * m.x10) + 250 * exp(
        m.x5 + 0.6 * m.x11) + 250 * exp(m.x6 + 0.6 * m.x12), sense=minimize)

    m.c2 = Constraint(expr=m.x7 - m.x13 >= 2.06686275947298)

    m.c3 = Constraint(expr=m.x8 - m.x13 >= 0.693147180559945)

    m.c4 = Constraint(expr=m.x9 - m.x13 >= 1.64865862558738)

    m.c5 = Constraint(expr=m.x10 - m.x13 >= 1.58923520511658)

    m.c6 = Constraint(expr=m.x11 - m.x13 >= 1.80828877117927)

    m.c7 = Constraint(expr=m.x12 - m.x13 >= 1.43508452528932)

    m.c8 = Constraint(expr=m.x7 - m.x14 >= -0.356674943938732)

    m.c9 = Constraint(expr=m.x8 - m.x14 >= -0.22314355131421)

    m.c10 = Constraint(expr=m.x9 - m.x14 >= -0.105360515657826)

    m.c11 = Constraint(expr=m.x10 - m.x14 >= 1.22377543162212)

    m.c12 = Constraint(expr=m.x11 - m.x14 >= 0.741937344729377)

    m.c13 = Constraint(expr=m.x12 - m.x14 >= 0.916290731874155)

    m.c14 = Constraint(expr=m.x7 - m.x[15] >= -0.356674943938732)

    m.c15 = Constraint(expr=m.x8 - m.x[15] >= 0.955511445027436)

    m.c16 = Constraint(expr=m.x9 - m.x[15] >= 0.470003629245736)

    m.c17 = Constraint(expr=m.x10 - m.x[15] >= 1.28093384546206)

    m.c18 = Constraint(expr=m.x11 - m.x[15] >= 1.16315080980568)

    m.c19 = Constraint(expr=m.x12 - m.x[15] >= 1.06471073699243)

    m.c20 = Constraint(expr=m.x7 - m.x[16] >= 1.54756250871601)

    m.c21 = Constraint(expr=m.x8 - m.x[16] >= 0.832909122935104)

    m.c22 = Constraint(expr=m.x9 - m.x[16] >= 0.470003629245736)

    m.c23 = Constraint(expr=m.x10 - m.x[16] >= 0.993251773010283)

    m.c24 = Constraint(expr=m.x11 - m.x[16] >= 0.182321556793955)

    m.c25 = Constraint(expr=m.x12 - m.x[16] >= 0.916290731874155)

    m.c26 = Constraint(expr=m.x7 - m.x[17] >= 0.182321556793955)

    m.c27 = Constraint(expr=m.x8 - m.x[17] >= 1.28093384546206)

    m.c28 = Constraint(expr=m.x9 - m.x[17] >= 0.8754687373539)

    m.c29 = Constraint(expr=m.x10 - m.x[17] >= 1.50407739677627)

    m.c30 = Constraint(expr=m.x11 - m.x[17] >= 0.470003629245736)

    m.c31 = Constraint(expr=m.x12 - m.x[17] >= 0.741937344729377)

    m.c32 = Constraint(expr=m.x1 + m.x[18] >= 1.85629799036563)

    m.c33 = Constraint(expr=m.x2 + m.x[18] >= 1.54756250871601)

    m.c34 = Constraint(expr=m.x3 + m.x[18] >= 2.11625551480255)

    m.c35 = Constraint(expr=m.x4 + m.x[18] >= 1.3609765531356)

    m.c36 = Constraint(expr=m.x5 + m.x[18] >= 0.741937344729377)

    m.c37 = Constraint(expr=m.x6 + m.x[18] >= 0.182321556793955)

    m.c38 = Constraint(expr=m.x1 + m.x[19] >= 1.91692261218206)

    m.c39 = Constraint(expr=m.x2 + m.x[19] >= 1.85629799036563)

    m.c40 = Constraint(expr=m.x3 + m.x[19] >= 1.87180217690159)

    m.c41 = Constraint(expr=m.x4 + m.x[19] >= 1.48160454092422)

    m.c42 = Constraint(expr=m.x5 + m.x[19] >= 0.832909122935104)

    m.c43 = Constraint(expr=m.x6 + m.x[19] >= 1.16315080980568)

    m.c44 = Constraint(expr=m.x1 + m.x20 >= 0)

    m.c45 = Constraint(expr=m.x2 + m.x20 >= 1.84054963339749)

    m.c46 = Constraint(expr=m.x3 + m.x20 >= 1.68639895357023)

    m.c47 = Constraint(expr=m.x4 + m.x20 >= 2.47653840011748)

    m.c48 = Constraint(expr=m.x5 + m.x20 >= 1.7404661748405)

    m.c49 = Constraint(expr=m.x6 + m.x20 >= 1.82454929205105)

    m.c50 = Constraint(expr=m.x1 + m.x21 >= 1.16315080980568)

    m.c51 = Constraint(expr=m.x2 + m.x21 >= 1.09861228866811)

    m.c52 = Constraint(expr=m.x3 + m.x21 >= 1.25276296849537)

    m.c53 = Constraint(expr=m.x4 + m.x21 >= 1.19392246847243)

    m.c54 = Constraint(expr=m.x5 + m.x21 >= 1.02961941718116)

    m.c55 = Constraint(expr=m.x6 + m.x21 >= 1.22377543162212)

    m.c56 = Constraint(expr=m.x1 + m.x22 >= 0.741937344729377)

    m.c57 = Constraint(expr=m.x2 + m.x22 >= 0.916290731874155)

    m.c58 = Constraint(expr=m.x3 + m.x22 >= 1.43508452528932)

    m.c_list = ConstraintList()

    m.c_list.add(m.x4 + m.x22 >= 1.28093384546206)

    m.c_list.add(m.x5 + m.x22 >= 1.30833281965018)

    m.c_list.add(m.x6 + m.x22 >= 0.78845736036427)

    m.c_list.add(250000 * exp(m.x[18] - m.x13) + 150000 * exp(
        m.x[19] - m.x14) + 180000 * exp(m.x20 - m.x[15]) + 160000 * exp(
        m.x21 - m.x[16]) + 120000 * exp(m.x22 - m.x[17]) <= 6000)

    m.c_list.add(m.x1 - 0.693147180559945 * m.b29 - 1.09861228866811 * m.b35 - 1.38629436111989 * m.b41 == 0)

    m.c_list.add(m.x2 - 0.693147180559945 * m.b30 - 1.09861228866811 * m.b36 - 1.38629436111989 * m.b42 == 0)

    m.c65 = Constraint(
        expr=m.x3 - 0.693147180559945 * m.b31 - 1.09861228866811 * m.b37 - 1.38629436111989 * m.b43 == 0)

    m.c66 = Constraint(
        expr=m.x4 - 0.693147180559945 * m.b32 - 1.09861228866811 * m.b38 - 1.38629436111989 * m.b44 == 0)

    m.c67 = Constraint(
        expr=m.x5 - 0.693147180559945 * m.b33 - 1.09861228866811 * m.b39 - 1.38629436111989 * m.b45 == 0)

    m.c68 = Constraint(
        expr=m.x6 - 0.693147180559945 * m.b34 - 1.09861228866811 * m.b40 - 1.38629436111989 * m.b46 == 0)

    m.c69 = Constraint(expr=m.b23 + m.b29 + m.b35 + m.b41 == 1)

    m.c70 = Constraint(expr=m.b24 + m.b30 + m.b36 + m.b42 == 1)

    m.c71 = Constraint(expr=m.b25 + m.b31 + m.b37 + m.b43 == 1)

    m.c72 = Constraint(expr=m.b26 + m.b32 + m.b38 + m.b44 == 1)

    m.c73 = Constraint(expr=m.b27 + m.b33 + m.b39 + m.b45 == 1)

    m.c74 = Constraint(expr=m.b28 + m.b34 + m.b40 + m.b46 == 1)

    # endregion

    with open('decogo.set', 'w') as file:
        # =========================refactory  colgen ===========================
        file.write('strategy = CG\n')
        file.write('user_defined_input_model = True\n')  # disable
        # user-defined model
        # ================== CG settings ======================================
        file.write('maxtime = 1000\n')  # maximum computation/solving time
        file.write('cg_max_iter = 5\n')
        file.write('cg_sub_gradient_max_iter = 3\n')
        file.write('decomp_estimate_var_bounds = False\n')
        file.write('cg_normalize_duals = False\n')
        file.write('cg_max_main_iter = 20\n')  # main iteration limit
        file.write('cg_fast_fw = False\n')  # switch off fast CG
        file.write('cg_fast_approx = True\n')  # disable exact problem
        # solving in fast CG

        file.close()

    # create solver instance
    solver = DecogoSolver()

    # user-defined model with solvers for
    # sub-problems and original problems (primal heuristics)
    # input model is general MINLP Pyomo model
    model_user_defined = PyomoInputModel(model)
    # solve the model
    solver.optimize(model_user_defined)
