*************************
Class inheritance diagram
*************************

Here are presented the classes of all four packages
(model, problem, solver and utility).

Model
=====
.. inheritance-diagram:: decogo.model.block_model decogo.model.constraints
    decogo.model.model_decomposer decogo.model.block_model decogo.model.input_model_base
    :parts: 1

Pyomo MINLP input model for refactory Colgen
============================================
.. inheritance-diagram:: decogo.pyomo_minlp_model.input_model
    decogo.pyomo_minlp_model.master_problem_base
    decogo.pyomo_minlp_model.subproblem
    decogo.pyomo_minlp_model.nlp_master_problem
    decogo.pyomo_minlp_model.projection_master_problem
    :parts: 1

Problem
=======
.. inheritance-diagram:: decogo.problem.approx_data
    decogo.problem.decomposed_problem
    :parts: 1

Inner master problems
=====================
.. inheritance-diagram:: decogo.problem.inner_master_problem
    decogo.problem.master_problem
    :parts: 1

Pyomo OA master problems
========================
.. inheritance-diagram:: decogo.pyomo_problem.master_problem_base
    decogo.pyomo_problem.oa_master_problem decogo.pyomo_problem.nlp_master_problem
    :parts: 1

Pyomo projection master problems
================================
.. inheritance-diagram:: decogo.pyomo_problem.projection_master_problem
    :parts: 1

Pyomo sub-problems
==================
.. inheritance-diagram:: decogo.pyomo_problem.subproblem
    :parts: 1

Solver
======
.. inheritance-diagram:: decogo.solver.decogo
    decogo.solver.colgen decogo.solver.oa decogo.solver.results
    decogo.solver.settings
    :parts: 1

Utility
=======
.. inheritance-diagram:: decogo.util.block_vector
    :parts: 1