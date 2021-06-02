"""Implements NLP master problem"""

from pyomo.core import ConstraintList
from pyomo.core.expr.visitor import identify_variables, replace_expressions

from decogo.pyomo_problem.oa_master_problem import OaMasterProblem


class NlpProblem(OaMasterProblem):
    """Class for defining the NLP master problem. Used for obtaining solution
    with fixed or relaxed integer variables

    .. math::
        \\begin{equation}
        \\begin{split}
            \\min \\ &c^Tx,\\newline
            &x \\in P \\cap G
        \\end{split}
        \\end{equation}
    """

    def __init__(self, block_model):
        """Constructor method"""
        super().__init__(block_model)
        self.model.name = 'NLP master problem'

        # non linear constraints creation
        for k in range(self.block_model.num_blocks):
            self.model.blocks[k + 1].nonlin_constr = ConstraintList()
            for constr in self.block_model.sub_models[k].nonlin_constr:
                expr = constr.expr.clone()
                vars_in_expr = identify_variables(expr)
                # map for replacing the objects in the expression
                substitution_map = {}
                for var in vars_in_expr:
                    index = block_model.sub_models[k].vars_in_block.index(
                        var.name)
                    substitution_map[id(var)] = self.model.blocks[k + 1].Y[
                        index + 1]
                new_expr = replace_expressions(expr, substitution_map)
                self.model.blocks[k + 1].nonlin_constr.add(expr=new_expr)
