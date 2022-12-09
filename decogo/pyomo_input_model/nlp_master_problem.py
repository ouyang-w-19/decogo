"""This modules implements NLP master problem"""

from pyomo.core.expr.visitor import identify_variables, replace_expressions

from decogo.pyomo_input_model.master_problem_base import MasterProblemBase
from pyomo.environ import ConstraintList, Objective


class NlpProblem(MasterProblemBase):
    """A class for defining the NLP master problem. Used for obtaining solution
    with fixed or relaxed integer variables.

    .. math::
        \\begin{equation}
        \\begin{split}
            \\min \\ &c^Tx,\\newline
            &x \\in P \\cap G
        \\end{split}
        \\end{equation}

    :param sub_models: List of sub-models
    :type sub_models: list
    :param cuts: Container which stores all linear constraints \
    (global and local) and objective function
    :type cuts: CutPool
    """

    def __init__(self, sub_models, cuts):
        """Constructor method"""
        super().__init__(sub_models, cuts)

        self.set_default_objective()

        self.model.name = 'NLP master problem'

        # non linear constraints creation
        for k in range(self.cuts.num_blocks):
            self.model.blocks[k + 1].nonlin_constr = ConstraintList()
            for constr in self.sub_models[k].nonlin_constr:
                expr = constr.expr.clone()
                vars_in_expr = identify_variables(expr)
                # map for replacing the objects in the expression
                substitution_map = {}
                for var in vars_in_expr:
                    index = sub_models[k].vars_in_block.index(
                        var.name)
                    substitution_map[id(var)] = self.model.blocks[k + 1].Y[
                        index + 1]
                new_expr = replace_expressions(expr, substitution_map)
                self.model.blocks[k + 1].nonlin_constr.add(expr=new_expr)

    def set_default_objective(self):
        """Sets a linear objective function with the costs given from the
        original formulation"""
        expr = \
            sum(self.cuts.obj.c[k, n] *
                self.model.blocks[k + 1].Y[n + 1]
                for k in range(self.cuts.num_blocks)
                for n in range(self.cuts.block_sizes[k])) + \
            self.cuts.obj.const

        self.model.del_component('obj')
        self.model.obj = Objective(expr=expr)
