*************************
Class inheritance diagram
*************************

The classes of six packages (model, problem, solver, utility, pyomo_problem, pyomo_input_model) are presented here.

model
=====
.. inheritance-diagram:: decogo.model.block_model decogo.model.constraints
    decogo.model.model_decomposer decogo.model.block_model decogo.model.input_model_base
    :parts: 1

problem
=======
.. inheritance-diagram:: decogo.problem.approx_data
    decogo.problem.decomposed_problem decogo.problem.inner_master_problem
    decogo.problem.master_problem
    :parts: 1

solver
======
.. inheritance-diagram:: decogo.solver.decogo
    decogo.solver.colgen decogo.solver.dyn_block_colgen
    decogo.solver.oa decogo.solver.refactory_colgen
    decogo.solver.results
    decogo.solver.settings
    :parts: 1

utility
=======
.. inheritance-diagram:: decogo.util.block_vector
    :parts: 1


pyomo_input_model
============================================
Package pyomo_input_layer implements the user-defined Pyomo based input model for CG.

.. inheritance-diagram:: decogo.pyomo_input_model.input_model
    decogo.pyomo_input_model.master_problem_base
    decogo.pyomo_input_model.subproblem
    decogo.pyomo_input_model.nlp_master_problem
    decogo.pyomo_input_model.projection_master_problem
    :parts: 1

pyomo_problem
=============
Package pyomo_problem implements the sub-problem solving, primal heuristics for
CG, OA and DBCG algorithms, which are based on Pyomo model. The implementation
parts of CG and DBCG will be integrated into Packages problem and pyomo_input_model
after refactory. The classes of this package are grouped as follows:

- Pyomo OA master problems

.. inheritance-diagram:: decogo.pyomo_problem.master_problem_base
    decogo.pyomo_problem.oa_master_problem decogo.pyomo_problem.nlp_master_problem
    :parts: 1

- Pyomo projection master problems

.. inheritance-diagram:: decogo.pyomo_problem.projection_master_problem
    :parts: 1

- Pyomo sub-problems

.. inheritance-diagram:: decogo.pyomo_problem.subproblem
    :parts: 1

- Pyomo-based containers for master problems and decomposed problems
.. inheritance-diagram:: decogo.pyomo_problem.pyomo_master_problem
    decogo.pyomo_problem.pyomo_decomposed_problem
    :parts: 1