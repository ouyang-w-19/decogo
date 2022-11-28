*******
Example
*******

Here we present one simple example of executing the solver with
`model <http://www.minlplib.org/alan.html>`_ from MINLPlib:

.. code-block:: python
   :linenos:

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


   if __name__ == '__main__':
       # define Pyomo model
       model = m = ConcreteModel()

       m.x1 = Var(within=Reals, bounds=(0, None), initialize=0.302884615384618)
       m.x2 = Var(within=Reals, bounds=(0, None), initialize=0.0865384615384593)
       m.x3 = Var(within=Reals, bounds=(0, None), initialize=0.504807692307693)
       m.x4 = Var(within=Reals, bounds=(0, None), initialize=0.10576923076923)
       m.b6 = Var(within=Binary, bounds=(0, 1), initialize=0)
       m.b7 = Var(within=Binary, bounds=(0, 1), initialize=0)
       m.b8 = Var(within=Binary, bounds=(0, 1), initialize=0)
       m.b9 = Var(within=Binary, bounds=(0, 1), initialize=0)

       m.obj = Objective(expr=m.x1 * (4 * m.x1 + 3 * m.x2 - m.x3) + m.x2 * (
                   3 * m.x1 + 6 * m.x2 + m.x3) + m.x3 * (m.x2 - m.x1 + 10 * m.x3)
                         , sense=minimize)

       m.c1 = Constraint(expr=m.x1 + m.x2 + m.x3 + m.x4 == 1)

       m.c2 = Constraint(expr=8 * m.x1 + 9 * m.x2 + 12 * m.x3 + 7 * m.x4 == 10)

       m.c4 = Constraint(expr=m.x1 - m.b6 <= 0)

       m.c5 = Constraint(expr=m.x2 - m.b7 <= 0)

       m.c6 = Constraint(expr=m.x3 - m.b8 <= 0)

       m.c7 = Constraint(expr=m.x4 - m.b9 <= 0)

       m.c8 = Constraint(expr=m.b6 + m.b7 + m.b8 + m.b9 <= 3)

       with open('decogo.set', 'w') as file:
           file.write('strategy = CG\n')
           file.write('maxtime = 1000\n')
           file.write('cg_max_iter = 5\n')
           file.write('cg_sub_gradient_max_iter = 3\n')
           file.write('decomp_estimate_var_bounds = False\n')
           file.write('cg_normalize_duals = False\n')
           file.write('cg_max_main_iter = 20\n')  # main iteration limit
           # ========================= primal heuristics =========================
           file.write('cg_find_solution = True\n')
           # ===================================================================
           file.write('cg_fast_fw = False\n')  # switch off fast CG
           file.write('cg_fast_approx = True\n')  # using exact problem
           # solving in fast CG

           file.close()

       # create solver instance
       solver = DecogoSolver()

       # solve the model
       solver.optimize(model)
