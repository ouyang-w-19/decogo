"""Implements OA master problems"""

import logging

import numpy as np
from pyomo.environ import ConstraintList, Objective, minimize, Var, RangeSet, \
    Reals, SolverFactory, ConcreteModel, Block, Suffix, SolverStatus, \
    TerminationCondition

from decogo.pyomo_problem.master_problem_base import MasterProblemBase
from decogo.util.block_vector import BlockVector

logger = logging.getLogger('decogo')


class OaMasterProblem(MasterProblemBase):
    """Class for defining an outer master problem

    .. math::
        \\begin{equation}
        \\begin{split}
            \\min \\ &c^Tx,\\newline
            &x \\in P \\cap Y
        \\end{split}
        \\end{equation}
    """

    def __init__(self, block_model):
        super().__init__(block_model)
        self.model.name = 'Outer master problem'

        self.set_default_objective()

    def set_default_objective(self):
        """Sets a linear objective function with the costs given from the
        original formulation"""
        expr = \
            sum(self.block_model.cuts.obj.c[k, n] *
                self.model.blocks[k + 1].Y[n + 1]
                for k in range(self.block_model.num_blocks)
                for n in range(self.block_model.block_sizes[k])) + \
            self.block_model.cuts.obj.const

        self.model.del_component('obj')
        self.model.obj = Objective(expr=expr)


class MipOaMasterProblem(OaMasterProblem):
    """Class for defining MIP Outer Approximation master problem

    .. math::
        \\begin{equation}
        \\begin{split}
            \\min \\ &c^Tx,\\newline
            &x \\in P \\cap Y \\cap \\hat{G}
        \\end{split}
        \\end{equation}

    where :math:`\\hat{G}` is an Outer Approximation of nonlinear feasible
    set :math:`G`

    :param approx_data: Object where the linearization cuts are stored
    :type approx_data: ApproxData
    """

    def __init__(self, block_model, approx_data):
        super().__init__(block_model)
        self.model.name = 'MIP OA problem'

        self.approx_data = approx_data

        # add linearization cuts
        for k in range(self.block_model.num_blocks):
            self.model.blocks[k + 1].linearization_cuts = ConstraintList()

    def add_linearization_cuts(self, number_of_cuts):
        """Adds linearization cuts

        :param n: Number of cuts to be added
        :type n: dict
        """

        def get_expr(model, k, i):
            return sum(self.approx_data.linearization_cuts[k, i].lhs[k, n] *
                       model.blocks[k + 1].Y[n + 1]
                       for n in range(self.block_model.block_sizes[k]))

        for k in range(self.block_model.num_blocks):
            for i in range(self.approx_data.linearization_cuts.num_cuts(k) -
                           number_of_cuts[k],
                           self.approx_data.linearization_cuts.num_cuts(k)):
                if self.approx_data.linearization_cuts[k, i].relation == "<=":
                    self.model.blocks[k + 1].linearization_cuts.add(
                        expr=get_expr(self.model, k, i) <=
                             self.approx_data.linearization_cuts[k, i].rhs)
                elif self.approx_data.linearization_cuts[k, i].relation == ">=":
                    self.model.blocks[k + 1].linearization_cuts.add(
                        expr=get_expr(self.model, k, i) >=
                             self.approx_data.linearization_cuts[k, i].rhs)
                # equality constraint does not exist in this case


class SlackMipOaMasterProblem(MipOaMasterProblem):
    """Class for MIP Outer Approximation problem with slacks

    .. math::
        \\begin{equation}
        \\begin{split}
            \\min \\ &c_k^Tx + \\gamma\\sum\\limits_{j \\in [m]}s_j,\\newline
            &x_k \\in Y_k \\cap \\hat{G}, \\newline
            & a_{kj}^Tx \\leq b_j + s_j, j \\in [m], \\newline
            & x_{\ell} \\text{ is fixed}, \\ell \\in K\\setminus{k}, \\gamma > 0
        \\end{split}
        \\end{equation}
    """

    def __init__(self, block_model, approx_data):

        super().__init__(block_model, approx_data)
        self.model.name = 'OA problem with slacks'

        # unfix slacks
        self.model.slack_pos.unfix()
        self.model.slack_neg.unfix()

        for k in range(self.block_model.num_blocks):
            self.model.blocks[k + 1].slack_pos.unfix()
            self.model.blocks[k + 1].slack_neg.unfix()

    def set_objective(self, block_id):
        """Sets objective function

        :param block_id: Block identifier
        :type block_id: int
        """
        gamma = self.block_model.cuts.obj.c.maxabs(block_id)
        if gamma is None:
            gamma = 1
        else:
            gamma = abs(self.block_model.cuts.obj.c.maxabs(block_id))

        # set weights for slacks of global constraints
        for j in range(self.block_model.cuts.num_of_global_cuts):
            self.model.gamma_pos[j + 1].value = gamma
            self.model.gamma_neg[j + 1].value = gamma

        expr = sum(self.block_model.cuts.obj.c[block_id, n] *
                   self.model.blocks[block_id + 1].Y[n + 1]
                   for n in range(self.block_model.block_sizes[block_id]))

        # sum of slacks for global constraints
        expr += sum(self.model.gamma_pos[i + 1] * self.model.slack_pos[i + 1] +
                    self.model.gamma_neg[i + 1] * self.model.slack_neg[i + 1]
                    for i in range(self.block_model.cuts.num_of_global_cuts))

        # set weights for slacks of linear local constraints
        for k in range(self.block_model.num_blocks):
            for j in range(self.block_model.cuts.num_of_local_cuts[k]):
                self.model.blocks[k + 1].gamma_pos[j + 1].value = gamma
                self.model.blocks[k + 1].gamma_neg[j + 1].value = gamma

        expr += sum(self.model.blocks[k + 1].gamma_pos[j + 1] *
                    self.model.blocks[k + 1].slack_pos[j + 1] +
                    self.model.blocks[k + 1].gamma_neg[j + 1] *
                    self.model.blocks[k + 1].slack_neg[j + 1]
                    for k in range(self.block_model.num_blocks)
                    for j in range(self.block_model.cuts.num_of_local_cuts[k]))

        self.model.del_component('obj')
        self.model.obj = Objective(expr=expr, sense=minimize)

    def solve(self, solver_name, start_point=None, solver_options=None):
        """Calls the base method
        :meth:`~problem.oa_problem_base.OaMasterProblemBase.solve` and
        additionally returns the flag if slacks are zeros

        .. Note::
            If the solution is reported by the solver to be infeasible, then
            the variable bounds are too small
        """

        x_sol, obj_val, duals, sol_is_feasible = super().solve(
            solver_name=solver_name, start_point=start_point,
            solver_options=solver_options)
        # if the solution is infeasible, then the variable bounds are too small

        # check if slacks are zeros
        slacks_are_zero = True
        for i in range(self.block_model.cuts.num_of_global_cuts):
            if self.model.slack_pos[i + 1].value > 0.0001:
                slacks_are_zero = False
                break
            if self.model.slack_neg[i + 1].value > 0.0001:
                slacks_are_zero = False
                break

        return x_sol, obj_val, duals, sol_is_feasible, slacks_are_zero


class CompactOaMasterProblem:
    """Class for defining compact outer master problem

    .. math::
        \\begin{equation}
        \\begin{split}
            \\min &\\sum\\limits_{k \\in K} w_{k0}, \\newline
                &\\sum\\limits_{k \\in K} w_k \\leq b, \\newline
                &w_k \\in D_k \\subset \\mathbb{R}^{m + 1}, k \\in K
        \\end{split}
        \\end{equation}

    where :math:`D_k` is an Outer Approximation

    :param block_model: Block model
    :type block_model: BlockModel
    :param approx_data: Class that stores compact linear constraints, \
    generated during solving the sub-problems
    :type approx_data: ApproxData
    :param model: Pyomo model
    :type model: ConcreteModel
    """

    def __init__(self, block_model, approx_data):
        """Constructor method"""
        self.block_model = block_model
        self.approx_data = approx_data
        self.model = ConcreteModel()

        self.model.num_blocks = RangeSet(self.block_model.num_blocks)
        self.model.name = 'Compact OA'

        def block_rule(component, k):
            # by default all bound are equal 0, later they are redefined
            component.w = Var(
                RangeSet(self.block_model.cuts.num_of_global_cuts + 1),
                initialize=0,
                domain=Reals,
                bounds=(None, None))
            # valid linear constraints got from block model or after solving
            # subproblems
            component.lin_con = ConstraintList()

        self.model.blocks = Block(self.model.num_blocks, rule=block_rule)

        def lin_global_con_rule(model, j):
            return sum(model.blocks[k + 1].w[j + 2]
                       for k in range(self.block_model.num_blocks))

        self.model.lin_con = ConstraintList()
        for j in range(self.block_model.cuts.num_of_global_cuts):
            if self.block_model.cuts.global_cuts[j].relation == "<=":
                self.model.lin_con.add(
                    expr=lin_global_con_rule(self.model, j) <=
                         self.block_model.cuts.global_cuts[j].rhs)
            elif self.block_model.cuts.global_cuts[j].relation == "=":
                self.model.lin_con.add(
                    expr=lin_global_con_rule(self.model, j) ==
                         self.block_model.cuts.global_cuts[j].rhs)
            elif self.block_model.cuts.global_cuts[j].relation == ">=":
                self.model.lin_con.add(
                    expr=lin_global_con_rule(self.model, j) >=
                         self.block_model.cuts.global_cuts[j].rhs)

        self.set_default_objective()

        # suffix-object to store duals
        self.model.dual = Suffix(direction=Suffix.IMPORT)

    def set_default_objective(self):
        """Sets objective"""
        self.model.del_component('obj')
        self.model.obj = Objective(expr=sum(
            self.model.blocks[k + 1].w[1]
            for k in range(self.block_model.num_blocks))
                                        + self.block_model.cuts.obj.const)

    def add_compact_lin_local_const(self, block_id, lhs, relation, rhs,
                                    added_compact_cut=True):
        """Adds compact linear constraints

        :param block_id: Block identifier
        :type block_id: int
        :param lhs: Left hand side of the constraint
        :type lhs: ndarray
        :param relation: Relation of the constraint
        :type relation: str
        :param rhs: Right hand side of the constraint
        :type rhs: float
        """
        expr = sum(lhs[i] * self.model.blocks[block_id + 1].w[i + 1]
                   for i in range(self.block_model.cuts.num_of_global_cuts + 1))

        if relation == '>=':
            self.model.blocks[block_id + 1].lin_con.add(expr >= rhs)
        elif relation == '=':
            self.model.blocks[block_id + 1].lin_con.add(expr == rhs)
        elif relation == '<=':
            self.model.blocks[block_id + 1].lin_con.add(expr <= rhs)

        if not added_compact_cut:
            logger.info('added compact cut in compact oa problem: {0}'
                        .format(str(expr) + relation + str(rhs)))

    def set_new_objective(self, direction):
        """Sets new linear objective

        :param direction: Given direction
        :type direction: ndarray
        """
        # remove the objective
        self.model.del_component('obj')
        self.model.obj = Objective(
            expr=sum(direction[j] * self.model.blocks[k + 1].w[j + 1]
                     for j in
                     range(self.block_model.cuts.num_of_global_cuts + 1)
                     for k in range(self.block_model.num_blocks)))

    def set_bounds(self, lb_w, ub_w):
        """Sets bounds on the variables

        :param lb_w: Lower bounds vector
        :type lb_w: BlockVector
        :param ub_w: Upper bounds vector
        :type ub_w: BlockVector
        """
        for k in range(self.block_model.num_blocks):
            for j in range(self.block_model.cuts.num_of_global_cuts + 1):
                self.model.blocks[k + 1].w[j + 1].setlb(lb_w[k, j])
                self.model.blocks[k + 1].w[j + 1].setub(ub_w[k, j])

    def remove_bounds(self):
        """Resets the bounds of all variables"""
        for k in range(self.block_model.num_blocks):
            for j in range(self.block_model.cuts.num_of_global_cuts + 1):
                self.model.blocks[k + 1].w[j + 1].setlb(None)
                self.model.blocks[k + 1].w[j + 1].setub(None)

    def solve(self, solver_name, solver_options=None):
        """Solves the problem by calling an external solver

        :param solver_name: External solver name
        :type solver_name: str
        :param solver_options: Options for external solver
        :type solver_options: list
        :return: Solution point, dual solution and objective value
        :rtype: tuple
        """
        opt = SolverFactory(solver_name)

        if solver_options is not None:
            for key, value in solver_options:
                opt.options[key] = value

        results = opt.solve(self.model, tee=False)

        if results.solver.status == SolverStatus.warning:
            if results.solver.termination_condition == TerminationCondition.infeasibleOrUnbounded:
                logger.info(self.model.name + ' is infeasible or unbounded')

        # get duals
        duals = np.zeros(shape=self.block_model.cuts.num_of_global_cuts)
        for i in range(self.block_model.cuts.num_of_global_cuts):
            # see inner master problem why '-' is here
            duals[i] = -self.model.dual[self.model.lin_con[i + 1]]

        # get solution point (resources)
        w = BlockVector([self.block_model.cuts.num_of_global_cuts + 1] *
                        self.block_model.num_blocks)
        for k in range(self.block_model.num_blocks):
            for j in range(self.block_model.cuts.num_of_global_cuts + 1):
                w[k, j] = self.model.blocks[k + 1].w[j + 1].value

        obj_val = self.model.obj.expr()

        return w, duals, obj_val
