"""This module implements base class for Pyomo master problems used in MINLP
primal heuristics."""

import logging
import math

from pyomo.core import ConcreteModel, RangeSet, Var, Binary, Integers, Reals, \
    Block, ConstraintList, Objective, Constraint, Suffix, NonNegativeReals, \
    Param
from pyomo.environ import SolverFactory, SolverStatus

from decogo.util.block_vector import BlockVector

logger = logging.getLogger('decogo')


class MasterProblemBase:
    """A base class for master problems in original space.

    :param sub_models: List of sub-models
    :type sub_models: list
    :param cuts: Container which stores all linear constraints \
    (global and local) and objective function
    :type cuts: CutPool
    """

    def __init__(self, sub_models, cuts):
        """Constructor method"""
        self.sub_models = sub_models
        self.cuts = cuts

        # creates Pyomo model (variable and linear constraints)
        self.model = ConcreteModel()
        self.model.num_blocks = RangeSet(self.cuts.num_blocks)

        # block initialization with the rule
        self.model.blocks = Block(self.model.num_blocks, rule=self.block_rule)

        # define slacks here, however they are not necessary always. That's
        # why fix them
        self.model.slack_pos = \
            Var(RangeSet(self.cuts.num_of_global_cuts),
                domain=NonNegativeReals,
                initialize=0)
        self.model.slack_pos.fix()

        self.model.slack_neg = \
            Var(RangeSet(self.cuts.num_of_global_cuts),
                domain=NonNegativeReals,
                initialize=0)
        self.model.slack_neg.fix()

        # create params for slack weights
        self.model.gamma_pos = \
            Param(RangeSet(self.cuts.num_of_global_cuts),
                  initialize=0,
                  mutable=True)

        self.model.gamma_neg = \
            Param(RangeSet(self.cuts.num_of_global_cuts),
                  initialize=0,
                  mutable=True)

        def lin_global_con_rule(model, m):
            return sum(self.cuts.global_cuts[m].lhs[k, n] *
                       model.blocks[k + 1].Y[n + 1]
                       for k in range(self.cuts.num_blocks)
                       for n in range(self.cuts.block_sizes[k]))

        # this is global constraints
        self.model.lin_con = ConstraintList()
        for m in range(self.cuts.num_of_global_cuts):
            if self.cuts.global_cuts[m].relation == "<=":
                self.model.lin_con.add(
                    expr=lin_global_con_rule(self.model, m) <=
                    self.cuts.global_cuts[m].rhs +
                    self.model.slack_pos[m + 1])
            elif self.cuts.global_cuts[m].relation == "=":
                self.model.lin_con.add(
                    expr=lin_global_con_rule(self.model, m) ==
                    self.cuts.global_cuts[m].rhs +
                    self.model.slack_pos[m + 1] -
                    self.model.slack_neg[m + 1])
            elif self.cuts.global_cuts[m].relation == ">=":
                self.model.lin_con.add(
                    expr=lin_global_con_rule(self.model, m) >=
                    self.cuts.global_cuts[m].rhs +
                    self.model.slack_neg[m + 1])

        # suffix-object to store duals
        self.model.dual = Suffix(direction=Suffix.IMPORT)

    def block_rule(self, component, k):
        component.Y = Var(RangeSet(1, self.cuts.block_sizes[k - 1]),
                          initialize=0)
        for n in range(1, self.cuts.block_sizes[k - 1] + 1):
            lb = self.sub_models[k - 1].variables[
                n - 1].lower_bound
            component.Y[n].value = lb

            component.Y[n].setlb(lb)

            ub = self.sub_models[k - 1].variables[n - 1].upper_bound
            component.Y[n].setub(ub)

            if self.sub_models[k - 1].variables[n - 1].type == \
                    "Binary":
                component.Y[n].domain = Binary
                component.Y[n].value = 0
            elif self.sub_models[k - 1].variables[n - 1].type == \
                    "Integers":
                component.Y[n].domain = Integers
            else:
                component.Y[n].domain = Reals

        # define slacks here for local linear constraints, however they are
        # not necessary always. That's why fix them
        num_local_cuts = self.cuts.num_of_local_cuts[k - 1]
        component.slack_pos = Var(RangeSet(num_local_cuts),
                                  domain=NonNegativeReals, initialize=0)
        component.slack_pos.fix()
        component.slack_neg = Var(RangeSet(num_local_cuts),
                                  domain=NonNegativeReals, initialize=0)
        component.slack_neg.fix()

        component.gamma_pos = Param(RangeSet(num_local_cuts), initialize=0,
                                    mutable=True)
        component.gamma_neg = Param(RangeSet(num_local_cuts), initialize=0,
                                    mutable=True)

        def lin_local_con_rule(component, k, j):
            return sum(self.cuts.local_cuts[k][j].lhs[k, n] *
                       component.Y[n + 1]
                       for n in range(self.cuts.block_sizes[k]))

        # create local linear constraints within block
        component.lin_con = ConstraintList()
        for j, con in enumerate(self.cuts.local_cuts[k - 1]):
            if con.relation == "<=":
                component.lin_con.add(
                    expr=lin_local_con_rule(component, k - 1,j) <=
                    con.rhs + component.slack_pos[j + 1])
            elif con.relation == "=":
                component.lin_con.add(
                    expr=lin_local_con_rule(component, k - 1, j) ==
                    con.rhs + component.slack_pos[j + 1] -
                    component.slack_neg[j + 1])
            elif con.relation == ">=":
                component.lin_con.add(
                    expr=lin_local_con_rule(component, k - 1, j) >=
                    con.rhs + component.slack_neg[j + 1])

        # compact linear constraints
        component.compact_lin_con = ConstraintList()

    def set_default_objective(self):
        """Abstract method for setting the objective function"""
        pass

    def set_new_objective(self, direction):
        """Sets linear objective function with given direction vector

        :param direction: Given vector
        :type direction: BlockVector
        """
        expr = sum(direction[k, n] * self.model.blocks[k + 1].Y[n + 1]
                   for k in range(self.cuts.num_blocks)
                   for n in range(self.cuts.block_sizes[k]))

        self.model.del_component('obj')
        self.model.obj = Objective(expr=expr)

    def relax_integers(self, block_id=None):
        """Relaxes all variables to continuous in pyomo model

        :param block_id: Block identifier, defaults to ``None``. If this \
        parameter is given, then relaxation is set only for this block
        :type block_id: int ot None
        """
        if block_id is None:
            for k in range(self.cuts.num_blocks):
                for i, var_domain in enumerate(
                        self.sub_models[k].variables):
                    if var_domain.type == "Integers":
                        self.model.blocks[k + 1].Y[i + 1].domain = Reals
                    elif var_domain.type == "Binary":
                        self.model.blocks[k + 1].Y[i + 1].domain = Reals
        else:
            for i, var_domain in enumerate(
                    self.sub_models[block_id].variables):
                if var_domain.type == "Integers":
                    self.model.blocks[block_id + 1].Y[i + 1].domain = Reals
                elif var_domain.type == "Binary":
                    self.model.blocks[block_id + 1].Y[i + 1].domain = Reals

    def set_integers(self, block_id=None):
        """Sets integer varaibles as in original formulation

        :param block_id: Block identifier, defaults to ``None``. If this \
        parameter is given, then setting back is \
        done only for this block
        :type block_id: int ot None
        """
        if block_id is None:
            for k in range(self.cuts.num_blocks):
                for i, var_domain in enumerate(
                        self.sub_models[k].variables):
                    if var_domain.type == "Integers":
                        self.model.blocks[k + 1].Y[i + 1].domain = Integers
                    elif var_domain.type == "Binary":
                        self.model.blocks[k + 1].Y[i + 1].domain = Binary
        else:
            for i, var_domain in enumerate(
                    self.sub_models[block_id].variables):
                if var_domain.type == "Integers":
                    self.model.blocks[block_id + 1].Y[i + 1].domain = Integers
                elif var_domain.type == "Binary":
                    self.model.blocks[block_id + 1].Y[i + 1].domain = Binary

    def fix_all_variables(self, point, block_id):
        """Fixes all variables to some values, except for one block

        :param point: Given to fix at
        :type point: BlockVector
        :param block_id: Block identifier where are NOT fixed
        :type block_id: int
        """
        for k in range(self.cuts.num_blocks):
            if k != block_id:
                for i in range(self.cuts.block_sizes[k]):
                    self.model.blocks[k + 1].Y[i + 1].value = point[k, i]
                    self.model.blocks[k + 1].Y[i + 1].fix()

    def unfix_all_variables(self):
        """Unfixes all variables"""
        for k in range(self.cuts.num_blocks):
            for i in range(self.cuts.block_sizes[k]):
                self.model.blocks[k + 1].Y[i + 1].unfix()

    def fix_integers(self, point, blocks=None):
        """Fixes integer variables using the given point. Integer variables
        can be fixed either in all block or at some of the blocks

        :param point: Given point to fix
        :type point: BlockVector
        :param blocks: Blocks where to fix the integer variables, defaults \
        to ``None``. If this value is ``None`` in all blocks integers are fixed
        :type blocks: list or set
        """
        if blocks is None:
            for k in range(self.cuts.num_blocks):
                for i, var in enumerate(self.sub_models[k].variables):
                    var_type = self.sub_models[k].variables[i].type
                    if var_type == "Integers" or var_type == "Binary":
                        self.model.blocks[k + 1].Y[i + 1].value = point[k, i]
                        self.model.blocks[k + 1].Y[i + 1].fix()
        else:
            for k in blocks:
                for i, var in enumerate(self.sub_models[k].variables):
                    var_type = self.sub_models[k].variables[i].type
                    if var_type == "Integers" or var_type == "Binary":
                        self.model.blocks[k + 1].Y[i + 1].value = point[k, i]
                        self.model.blocks[k + 1].Y[i + 1].fix()

    def add_linear_local_constraint(self, block_id):
        """Adds linear local constraint which is already stored in BlockModel

        :param block_id: Block identifier
        :type block_id: int
        """

        def lin_con_rule(model, constr):
            return sum(
                constr.lhs[block_id, n] * model.blocks[block_id + 1].Y[n + 1]
                for n in range(self.cuts.block_sizes[block_id]))

        # this takes the last one from block model
        constr = self.cuts.local_cuts[block_id][-1]
        if constr.relation == "<=":
            self.model.blocks[block_id + 1].lin_con.add(
                expr=lin_con_rule(self.model, constr) <= constr.rhs)
        elif constr.relation == "=":
            self.model.blocks[block_id + 1].lin_con.add(
                expr=lin_con_rule(self.model, constr) == constr.rhs)
        elif constr.relation == ">=":
            self.model.blocks[block_id + 1].lin_con.add(
                expr=lin_con_rule(self.model, constr) >= constr.rhs)

    def update_optimality_cut(self, rhs):
        """Adds an optimality cut, i.e. :math:`c^Tx \\leq c_0`

        :param rhs: Right hand side of the constraint (in fact, primal bound)
        :type rhs: float
        """
        if rhs == float('inf') or math.isnan(rhs):
            con_obj = self.model.find_component('optimality_cut')
            if con_obj is not None:
                con_obj.deactivate()
        else:
            # first we check if an optimality cut exists in the model
            if self.model.find_component('optimality_cut') is not None:
                # just update the right hand side of the cut
                self.model.primal_bound.value = rhs
                self.model.optimality_cut.activate()
            else:
                # create a new constraint
                self.model.primal_bound = Param(initialize=rhs, mutable=True)
                self.model.optimality_cut = \
                    Constraint(
                        expr=sum(self.cuts.obj.c[k, i] *
                                 self.model.blocks[k + 1].Y[i + 1]
                                 for k in range(self.cuts.num_blocks)
                                 for i in range(self.cuts.block_sizes[k]))
                        <= self.model.primal_bound)

    def update_var_lower_bound(self, index):
        """Updates the lower bound by given index

        :param index: Index as pair (block_id, index)
        :type index: tuple
        """
        # the lower bound is taken from the block model, since it is already
        # updated
        k, i = index
        var = self.sub_models[k].variables[i]
        self.model.blocks[k + 1].Y[i + 1].setlb(var.lower_bound)

    def update_var_upper_bound(self, index):
        """Updates the upper bound by given index

        :param index: Index as pair (block_id, index)
        :type index: tuple
        """
        # the upper bound is taken from the block model, since it is already
        # updated
        k, i = index
        var = self.sub_models[k].variables[i]
        self.model.blocks[k + 1].Y[i + 1].setub(var.upper_bound)

    def deactivate_blocks(self, kt):

        # method for deactivating the blocks such that we can define an
        # aggregated subproblem from master problem

        # assume kt is a tuple
        kt = set(kt)  # more efficient whether element belongs to set

        for k in range(self.cuts.num_blocks):
            if k not in kt:
                # deactivate all constraints under this block
                self.model.blocks[k + 1].deactivate()

                # fix variables to zero
                self.model.blocks[k + 1].Y.fix(0)

    def activate_blocks(self, kt):

        # method for activating the blocks back

        # assume kt is a tuple
        kt = set(kt)  # more efficient whether element belongs to set

        for k in range(self.cuts.num_blocks):
            if k not in kt:
                # deactivate all constraints under this block
                self.model.blocks[k + 1].activate()

                # unfix variables
                self.model.blocks[k + 1].Y.unfix()

    def deactivate_global_constraints(self, indices):

        # assumption 'indices' has all constraints which have to be activated

        indices = set(indices)

        for i in range(self.cuts.num_of_global_cuts):
            if i not in indices:
                self.model.lin_con[i + 1].deactivate()

    def activate_global_constraints(self, indices):

        indices = set(indices)

        for i in range(self.cuts.num_of_global_cuts):
            if i not in indices:
                self.model.lin_con[i + 1].activate()

    def solve(self, solver_name, start_point=None, solver_options=None):
        """Solves the model by calling an external solver and gets back the
        result

        :param solver_name: External solver name
        :type solver_name: str
        :param start_point: Starting point for the solver, defaults to ``None``
        :type start_point: BlockVector or None
        :param solver_options: External solver options, defaults to ``None``
        :type solver_options: list or None
        :return: Solution point, objective value, dual solution and flag \
        indicating whether the solution is feasible
        :rtype: tuple
        """

        if start_point is not None:
            for k in range(len(self.model.blocks)):
                for n in range(len(self.model.blocks[k + 1].Y)):
                    self.model.blocks[k + 1].Y[n + 1].value = start_point[k, n]

        opt = SolverFactory(solver_name)

        # set solver options
        # options are pairs: (parameter name, value)
        if solver_options is not None:
            for key, value in solver_options:
                opt.options[key] = value

        result = opt.solve(self.model, tee=False)

        sol_is_feasible = True
        if result.solver.status == SolverStatus.warning:
            sol_is_feasible = False
            logger.info('Master problem is {0}: {1}'.format(
                result.solver.termination_condition,
                self.model.name))

        # get duals
        try:
            duals = [0] * self.cuts.num_of_global_cuts
            for i in self.model.lin_con:
                duals[i - 1] = self.model.dual[self.model.lin_con[i]]
        except KeyError as error:
            duals = None
            # logger.info('KeyError: {0}'.format(error))

        # get solution point
        x_sol = BlockVector(self.cuts.block_sizes)
        for k in range(len(self.model.blocks)):
            for n in range(len(self.model.blocks[k + 1].Y)):
                x_sol[k, n] = self.model.blocks[k + 1].Y[n + 1].value

        obj_val = self.model.obj.expr()

        return x_sol, obj_val, duals, sol_is_feasible
