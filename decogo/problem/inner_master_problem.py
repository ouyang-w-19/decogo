"""Implements inner master problem"""

import logging
import numpy as np
from pyomo.environ import ConcreteModel, RangeSet, Var, Reals, Block, \
    ConstraintList, Set, Suffix, Param, Objective, \
    SolverFactory, Constraint, Binary, SolverStatus

from decogo.util.block_vector import BlockVector

logger = logging.getLogger('decogo')


class InnerMasterProblem:
    """Class for defining inner master problem which is solved over the convex
    hull of inner points

    .. math::
        \\begin{equation}
        \\begin{split}
            \\min \\ & c^T x(z) + \\sum\\limits_{i \\in [m]} \\gamma_i s_i,
            \\newline
            &Ax(z) \\leq b + s, \\newline
            &\\sum_{j \\in [S_k]} z_{kj}=1, \\newline
            & x_k(z_k) = \\sum_{j \\in [S_k]} z_{kj} y_{kj}, \\newline
            &z_{kj} \\geq 0, j \\in [S_k], k \\in K,
            & s \\geq 0, \\gamma > 0
        \\end{split}
        \\end{equation}

    where :math:`S_k \\subset \\mathbb{R}^{n_k}` is a set of inner points.

    The problem is constructed in the transformed space in the following way

    .. math::
        \\begin{equation}
        \\begin{split}
            \\min &\\sum\\limits_{k \\in K} w_{k0}(z_k) +
            \\sum\\limits_{i \\in [m]} \\gamma_i s_i, \\newline
            & \\sum\\limits_{k \\in K} w_{k}(z_k) \\leq b + s, \\newline
            &\\sum_{j \\in [R_k]} z_{kj}=1, z_{kj} \\geq 0, \\newline
            &w_k(z_k)=\\sum_{j \\in [R_k]} z_{kj}r_{kj}, \\newline
            &j \\in [R_k], k \\in K, s \\geq 0,\\gamma > 0
        \\end{split}
        \\end{equation}

    where :math:`R_k \\subset \\mathbb{R}^{m + 1}` is a set of columns.

    :param block_model: Block model
    :type block_model: BlockModel
    :param approx_data: Class that stores inner points and columns
    :type approx_data: ApproxData
    """

    def __init__(self, block_model, approx_data):
        """Constructor method"""
        self.block_model = block_model
        self.approx_data = approx_data

        self.model = ConcreteModel()
        self.model.name = 'Inner master problem'

        self.model.num_blocks = RangeSet(self.block_model.num_blocks)

        def block_rule(component, k):

            # integrate linear block directly
            if self.block_model.sub_models[k - 1].linear:
                # create variables
                component.Y = Var(RangeSet(1, self.block_model.block_sizes[k - 1]),
                                  domain=Reals, initialize=0)
                for n in range(1, self.block_model.block_sizes[k - 1] + 1):
                    lb = self.block_model.sub_models[k - 1].variables[n - 1].lower_bound
                    component.Y[n].value = lb
                    component.Y[n].setlb(lb)

                    ub = self.block_model.sub_models[k - 1].variables[n - 1].upper_bound
                    component.Y[n].setub(ub)

                # add local linear constraints
                def con_expr(component, k, j):
                    return sum(self.block_model.cuts.local_cuts[k][j].lhs[k, n] *
                               component.Y[n + 1]
                               for n in range(self.block_model.block_sizes[k]))

                component.lin_con = ConstraintList()
                for j, con in enumerate(self.block_model.cuts.local_cuts[k - 1]):
                    if con.relation == "<=":
                        component.lin_con.add(expr=con_expr(component, k - 1, j)
                                                   <= con.rhs)
                    elif con.relation == "=":
                        component.lin_con.add(expr=con_expr(component, k - 1, j)
                                                   == con.rhs)
                    elif con.relation == ">=":
                        component.lin_con.add(expr=con_expr(component, k - 1, j)
                                                   >= con.rhs)

            else:
                component.z_set = Set(dimen=1)
                component.z = Var(component.z_set,
                                  domain=Reals, bounds=(0, None))

        self.model.blocks = Block(self.model.num_blocks, rule=block_rule)

        # define slacks
        self.model.slack_pos = Var(
            RangeSet(self.block_model.cuts.num_of_global_cuts), domain=Reals,
            bounds=(0, None), initialize=0)

        self.model.slack_neg = Var(
            RangeSet(self.block_model.cuts.num_of_global_cuts), domain=Reals,
            bounds=(0, None), initialize=0)

        # init objective and lin constraints
        self.model.lin_con = ConstraintList()

        # get linear block index
        lin_block_ids = []
        for k in range(self.block_model.num_blocks):
            if self.block_model.sub_models[k].linear:
                lin_block_ids.append(k)

        def lin_block_expr(arg_lin_block_ids, j):
            if len(arg_lin_block_ids) > 0:
                return sum(self.block_model.cuts.global_cuts[j].lhs[i, n] *
                           self.model.blocks[i + 1].Y[n + 1]
                           for i in arg_lin_block_ids
                           for n in range(self.block_model.block_sizes[i]))
            else:
                return 0

        # global constraints
        for m in range(self.block_model.cuts.num_of_global_cuts):
            if self.block_model.cuts.global_cuts[m].relation == "<=":
                self.model.lin_con.add(
                    expr=lin_block_expr(lin_block_ids, m) -
                    self.model.slack_pos[m + 1] <=
                    self.block_model.cuts.global_cuts[m].rhs)
            elif self.block_model.cuts.global_cuts[m].relation == "=":
                self.model.lin_con.add(expr=lin_block_expr(lin_block_ids, m) -
                                       self.model.slack_pos[m + 1] +
                                       self.model.slack_neg[m + 1] ==
                                       self.block_model.cuts.global_cuts[m].rhs)
            elif self.block_model.cuts.global_cuts[m].relation == ">=":
                self.model.lin_con.add(expr=lin_block_expr(lin_block_ids, m) +
                                       self.model.slack_neg[m + 1] >=
                                       self.block_model.cuts.global_cuts[m].rhs)

        self.model.gamma = \
            Param(RangeSet(self.block_model.cuts.num_of_global_cuts),
                  initialize=0, mutable=True, within=Reals)

        # objective
        lin_block_obj_expr = 0

        if len(lin_block_ids) > 0:
            lin_block_obj_expr = sum(self.block_model.cuts.obj.c[k, n] *
                                     self.model.blocks[k + 1].Y[n + 1]
                                     for k in lin_block_ids
                                     for n in
                                     range(self.block_model.block_sizes[k]))

        # objective function
        obj_expr = sum(self.model.gamma[i + 1] * (self.model.slack_pos[i + 1] +
                                                  self.model.slack_neg[i + 1])
                       for i in
                       range(self.block_model.cuts.num_of_global_cuts)) + \
            self.block_model.cuts.obj.const + lin_block_obj_expr

        self.model.obj = Objective(expr=obj_expr)

        # suffix-object to store duals
        self.model.dual = Suffix(direction=Suffix.IMPORT)

    def add_column(self, block_id):
        """Adds a new column for block by the following procedure:

        1. Add a new variable :math:`z`
        2. Update the objective with a new column (at zero index)
        3. Update the global constraints with the new column

        :param block_id: Block identifier
        :type block_id: int
        """

        # get the last of index of the column since this column has to be added
        i = len(self.approx_data.inner_points.points[block_id]) - 1
        point, column = self.approx_data.inner_points.points[block_id][-1]

        # add new variable z
        self.model.blocks[block_id + 1].z_set.add(i + 1)
        self.model.blocks[block_id + 1].z.add(i + 1)
        self.model.blocks[block_id + 1].z[i + 1].value = 0

        # check if constraint is constructed sum_j z_kj = 1, if not it is
        # needed to add
        if self.model.blocks[block_id + 1].component('z_con') is None:
            # construct the constraint
            self.model.blocks[block_id + 1].z_con = Constraint(
                expr=self.model.blocks[block_id + 1].z[i + 1] == 1)
        else:
            # add new variable to existing constraint
            self.model.blocks[block_id + 1].z_con.set_value(
                self.model.blocks[block_id + 1].z_con.body +
                self.model.blocks[block_id + 1].z[i + 1] == 1)

        # add column to the objective
        new_expression = self.model.obj.expr + column[0] * \
            self.model.blocks[block_id + 1].z[i + 1]
        self.model.obj.set_value(new_expression)

        # add the column to the linear constraints (update the constraint list
        # of global constraint) index m + 1 for column, because the first
        # entry refers to objective
        for m in range(self.block_model.cuts.num_of_global_cuts):
            if self.block_model.cuts.global_cuts[m].relation == "<=":
                self.model.lin_con[m + 1].set_value(
                    self.model.lin_con[m + 1].body +
                    column[m + 1] * self.model.blocks[block_id + 1].z[i + 1] <=
                    self.model.lin_con[m + 1].upper)
            elif self.block_model.cuts.global_cuts[m].relation == "=":
                self.model.lin_con[m + 1].set_value(
                    self.model.lin_con[m + 1].body +
                    column[m + 1] * self.model.blocks[block_id + 1].z[i + 1] ==
                    self.model.lin_con[m + 1].upper)
            elif self.block_model.cuts.global_cuts[m].relation == ">=":
                self.model.lin_con[m + 1].set_value(
                    self.model.lin_con[m + 1].body +
                    column[m + 1] * self.model.blocks[block_id + 1].z[i + 1] >=
                    self.model.lin_con[m + 1].lower)

    def set_slack_weights(self, slack_weights):
        """Sets slack weights in the objective function

        :param slack_weights: Values for slack weights
        :type slack_weights: ndarray
        """
        for i in range(self.block_model.cuts.num_of_global_cuts):
            self.model.gamma[i + 1] = slack_weights[i]

    def compute_and_set_default_slack_weights(self):
        """Computes slack weights by defaults method, i.e. it is computed
        based on the zero resource of all columns in the following way
        :math:`\\gamma_i = 1.1\\max\\limits_{w_j \\in R_k, k \\in K} w_{j0},
        i \\in [m]`"""
        max_val = float('-inf')
        for k in range(self.block_model.num_blocks):
            for j in range(self.approx_data.get_inner_points_size(k)):
                point, column = self.approx_data.inner_points[k, j]
                if column[0] > max_val:
                    max_val = column[0]
        if max_val < 1e2:
            max_val = 1e2

        slack_weights = np.full(shape=self.block_model.cuts.num_of_global_cuts,
                                fill_value=1.1 * max_val)

        self.set_slack_weights(slack_weights)

    def solve(self, solver_name):
        """Solves the problem by calling an external solver

        :param solver_name: External solver name
        :type solver_name: str
        :return: Index of active cells blockwise, weights of the columns \
        :math:`z`, solution in original space, \
        solution in image space, slack values, dual solution and objective value
        :rtype: tuple

        .. Note::
            The comments where the dual values are extracted
        """
        opt = SolverFactory(solver_name)
        opt.solve(self.model, tee=False)

        # get duals
        try:
            duals = np.zeros(shape=self.block_model.cuts.num_of_global_cuts)
            for i in self.model.lin_con:
                # here one has to make sure if corrects sign of dual values
                # is returned all solvers normally return the marginal values
                # as dual values since for our formulation it is necessary to
                # have the Lagrange multipliers, i.e. -marginal value
                # newer versions of Ipopt (starting from 3.10.3 or 3.10.4)
                # return the marginal value, then put '-'
                # Gurobi returns marginal value, then put '-'
                # Other solvers were not checked
                duals[i - 1] = -self.model.dual[self.model.lin_con[i]]
        except KeyError:
            duals = None

        # get z variable values
        z = BlockVector()
        x = BlockVector()  # solution point in the original space
        w = BlockVector()  # solution point in the image space
        for k in range(self.block_model.num_blocks):
            z.set_block(k, np.zeros(
                shape=self.approx_data.get_inner_points_size(k)))

            resulting_point = np.zeros(shape=self.block_model.block_sizes[k])

            resulting_column = np.zeros(
                shape=self.block_model.cuts.num_of_global_cuts + 1)

            if self.block_model.sub_models[k].linear is False:
                for j in range(self.approx_data.get_inner_points_size(k)):
                    z[k, j] = self.model.blocks[k + 1].z[j + 1].value
                    point, column = self.approx_data.inner_points[k, j]
                    resulting_point += \
                        self.model.blocks[k + 1].z[j + 1].value * point
                    resulting_column += \
                        self.model.blocks[k + 1].z[j + 1].value * column
            else:
                for n in range(self.block_model.block_sizes[k]):
                    resulting_point[n] = self.model.blocks[k + 1].Y[n + 1].value

                resulting_column = \
                    self.block_model.trans_into_im_space(k, resulting_point)

            x.set_block(k, resulting_point)
            w.set_block(k, resulting_column)

        obj_value = self.block_model.cuts.obj.eval(x)

        slacks = [0] * self.block_model.cuts.num_of_global_cuts
        for i in range(self.block_model.cuts.num_of_global_cuts):
            slacks[i] = (self.model.slack_pos[i + 1].value,
                         self.model.slack_neg[i + 1].value)

        return z, x, w, slacks, duals, obj_value


class MiniInnerMasterProblem(InnerMasterProblem):
    """ mini inner master problem for fast minlp subproblem solving; multiple
    instances can be constructed for parallel computing of sub-problems.
    """
    def __init__(self, block_model, approx_data):
        super().__init__(block_model, approx_data)

    def set_objective(self, dir_im_space):
        # add direction into objective function
        new_c = BlockVector()
        for k in range(self.block_model.num_blocks):
            dir_orig_space_k = \
                self.block_model.trans_into_orig_space(k, dir_im_space)
            new_c.set_block(k, dir_orig_space_k)

        obj_expr = 0

        for k in range(self.block_model.num_blocks):
            if self.block_model.sub_models[k].linear:
                obj_expr += sum(new_c[k, n] * self.model.blocks[k + 1].Y[n + 1]
                                for n in range(self.block_model.block_sizes[k]))
            else:
                for j in range(self.approx_data.inner_points.get_size(k)):
                    point = self.approx_data.inner_points[k, j][0]
                    obj_expr += sum(new_c[k, n] * point[n] for n in
                                    range(self.block_model.block_sizes[k])) * \
                        self.model.blocks[k + 1].z[j + 1]

        self.model.del_component('obj')
        self.model.obj = Objective(expr=obj_expr)

    def deactivate_global_constraints(self, indices):

        # assumption 'indices' has all constraints which hav to be active

        indices = set(indices)

        for i in range(self.block_model.cuts.num_of_global_cuts):
            if i not in indices:
                self.model.lin_con[i + 1].deactivate()

    def activate_global_constraints(self, indices):

        indices = set(indices)

        for i in range(self.block_model.cuts.num_of_global_cuts):
            if i not in indices:
                self.model.lin_con[i + 1].activate()

    def deactivate_blocks(self, kt):

        # method for deactivating the blocks such that we can define an
        # aggregated subproblem from master problem

        # assume kt is a tuple
        kt = set(kt)  # more efficient whether element belongs to set

        for k in range(self.block_model.num_blocks):
            if k not in kt:
                # deactivate all constraints under this block
                self.model.blocks[k + 1].deactivate()

                # fix variables to zero
                if self.block_model.sub_models[k].linear is False:
                    self.model.blocks[k + 1].z.fix(0)
                else:
                    self.model.blocks[k + 1].Y.fix(0)

    def activate_blocks(self, kt):

        # method for activating the blocks back

        # assume kt is a tuple
        kt = set(kt)  # more efficient whether element belongs to set

        for k in range(self.block_model.num_blocks):
            if k not in kt:
                # deactivate all constraints under this block
                self.model.blocks[k + 1].activate()

                # unfix variables
                if self.block_model.sub_models[k].linear is False:
                    self.model.blocks[k + 1].z.unfix()
                else:
                    self.model.blocks[k + 1].Y.unfix()


class ExtendedInnerMasterProblem:
    """Class for defining inner master problem which is solved over the convex
    hull of inner points

    .. math::
        \\begin{equation}
        \\begin{split}
            \\min \\ & c^T x(z) + \\sum\\limits_{i \\in [m]} \\gamma_i s_i,
            \\newline
            &Ax(z) \\leq b + s, \\newline
            &\\sum_{j \\in [S_k]} z_{kj}=1, \\newline
            & x_k(z_k) = \\sum_{j \\in [S_k]} z_{kj} y_{kj}, \\newline
            &z_{kj} \\geq 0, j \\in [S_k], k \\in K,
            & s \\geq 0, \\gamma > 0
        \\end{split}
        \\end{equation}

    where :math:`S_k \\subset \\mathbb{R}^{n_k}` is a set of inner points.

    The problem is constructed in the transformed space in the following way

    .. math::
        \\begin{equation}
        \\begin{split}
            \\min &\\sum\\limits_{k \\in K} w_{k0}(z_k) +
            \\sum\\limits_{i \\in [m]} \\gamma_i s_i, \\newline
            & \\sum\\limits_{k \\in K} w_{k}(z_k) \\leq b + s, \\newline
            &\\sum_{j \\in [R_k]} z_{kj}=1, z_{kj} \\geq 0, \\newline
            &w_k(z_k)=\\sum_{j \\in [R_k]} z_{kj}r_{kj}, \\newline
            &j \\in [R_k], k \\in K, s \\geq 0,\\gamma > 0
        \\end{split}
        \\end{equation}

    where :math:`R_k \\subset \\mathbb{R}^{m + 1}` is a set of columns.

    :param block_model: Block model
    :type block_model: BlockModel
    :param approx_data: Class that stores inner points and columns
    :type approx_data: ApproxData
    """

    def __init__(self, block_model, approx_data):
        """Constructor method"""
        self.block_model = block_model
        self.approx_data = approx_data

        self.model = ConcreteModel()
        self.model.name = 'Extended inner master problem'

        # Introduce auxiliary variables for convex combination of columns in
        # atomic blocks
        num_of_global_cuts = self.block_model.cuts.num_of_global_cuts
        self.model.num_resource = RangeSet(num_of_global_cuts + 1)
        self.model.num_blocks = RangeSet(self.block_model.num_blocks)
        self.model.w = Var(self.model.num_blocks * self.model.num_resource,
                           domain=Reals)
        self.model.hyper_block_id = Set(dimen=1)

        def block_rule(component, k):

            # integrate linear block directly
            if self.block_model.sub_models[k - 1].linear:
                # create variables
                component.Y = Var(RangeSet(1, self.block_model.block_sizes[k - 1]),
                                  domain=Reals, initialize=0)
                for n in range(1, self.block_model.block_sizes[k - 1] + 1):
                    lb = self.block_model.sub_models[k - 1].variables[n - 1].lower_bound
                    component.Y[n].value = lb
                    component.Y[n].setlb(lb)

                    ub = self.block_model.sub_models[k - 1].variables[n - 1].upper_bound
                    component.Y[n].setub(ub)

                # add local linear constraints
                def con_expr(component, k, j):
                    return sum(self.block_model.cuts.local_cuts[k][j].lhs[k, n] *
                               component.Y[n + 1]
                               for n in range(self.block_model.block_sizes[k]))

                component.lin_con = ConstraintList()
                for j, con in enumerate(self.block_model.cuts.local_cuts[k - 1]):
                    if con.relation == "<=":
                        component.lin_con.add(expr=con_expr(component, k - 1, j)
                                                   <= con.rhs)
                    elif con.relation == "=":
                        component.lin_con.add(expr=con_expr(component, k - 1, j)
                                                   == con.rhs)
                    elif con.relation == ">=":
                        component.lin_con.add(expr=con_expr(component, k - 1, j)
                                                   >= con.rhs)

            else:
                component.z_set = Set(dimen=1)
                component.z = Var(component.z_set,
                                  domain=Reals, bounds=(0, 1))

        self.model.blocks = Block(self.model.num_blocks, rule=block_rule)

        # initialize resource overlapping constraints of for atomic blocks
        def w_con_rule(model, m_index):
            return self.model.w[k, m_index] == 0

        def w_con_linear_rule(model, m_index):
            if m_index == 1:
                # obj resource
                return self.model.w[k, m_index] == \
                       sum(self.block_model.cuts.obj.c[k-1, n] * model.Y[n + 1]
                           for n in range(self.block_model.block_sizes[k-1]))
            else:
                # global constraint resource
                return self.model.w[k, m_index] == \
                       sum(self.block_model.cuts.global_cuts[m_index-2].lhs[k-1,
                                                                            n]
                           * model.Y[n + 1]
                           for n in range(self.block_model.block_sizes[k-1]))

        for k in self.model.num_blocks:
            if self.block_model.sub_models[k-1].linear:
                self.model.blocks[k].w_con = \
                    Constraint(self.model.num_resource, rule=w_con_linear_rule)
            else:
                self.model.blocks[k].w_con = \
                    Constraint(self.model.num_resource, rule=w_con_rule)

        # define slacks
        self.model.slack_pos = Var(
            RangeSet(self.block_model.cuts.num_of_global_cuts), domain=Reals,
            bounds=(0, None), initialize=0)

        self.model.slack_neg = Var(
            RangeSet(self.block_model.cuts.num_of_global_cuts), domain=Reals,
            bounds=(0, None), initialize=0)

        # init objective and lin constraints
        self.model.lin_con = ConstraintList()

        # global constraints with auxiliary columns
        for m in range(self.block_model.cuts.num_of_global_cuts):
            if self.block_model.cuts.global_cuts[m].relation == "<=":
                self.model.lin_con.add(
                    expr=sum(self.model.w[k, m + 2]
                             for k in self.model.num_blocks) -
                    self.model.slack_pos[m + 1] <=
                    self.block_model.cuts.global_cuts[m].rhs)
            elif self.block_model.cuts.global_cuts[m].relation == "=":
                self.model.lin_con.add(
                    expr=sum(self.model.w[k, m + 2]
                             for k in self.model.num_blocks) -
                    self.model.slack_pos[m + 1] +
                    self.model.slack_neg[m + 1] ==
                    self.block_model.cuts.global_cuts[m].rhs)
            elif self.block_model.cuts.global_cuts[m].relation == ">=":
                self.model.lin_con.add(expr=sum(self.model.w[k, m + 2]
                                                for k in self.model.num_blocks) +
                                       self.model.slack_neg[m + 1] >=
                                       self.block_model.cuts.global_cuts[m].rhs)

        self.model.gamma = \
            Param(RangeSet(self.block_model.cuts.num_of_global_cuts + 1),
                  initialize=0, mutable=True, within=Reals)

        # objective function
        obj_expr = sum(self.model.gamma[i + 1] * (self.model.slack_pos[i + 1] +
                                                  self.model.slack_neg[i + 1])
                       for i in
                       range(self.block_model.cuts.num_of_global_cuts)) + \
            sum(self.model.w[k, 1]
                for k in self.model.num_blocks) + \
            self.block_model.cuts.obj.const

        self.model.obj = Objective(expr=obj_expr)

        # suffix-object to store duals
        self.model.dual = Suffix(direction=Suffix.IMPORT)

    def add_column(self, block_id):
        """Adds a new column for block by the following procedure:

        1. Add a new variable :math:`z`
        2. Update the objective with a new column (at zero index)
        3. Update the global constraints with the new column

        :param block_id: Block identifier
        :type block_id: int
        """

        # get the last of index of the column since this column has to be added
        i = len(self.approx_data.inner_points.points[block_id]) - 1
        point, column = self.approx_data.inner_points.points[block_id][-1]

        if len(self.approx_data.inner_points.KT[block_id]) == 1:
            # add new variable z
            self.model.blocks[block_id + 1].z_set.add(i + 1)
            self.model.blocks[block_id + 1].z.add(i + 1)
            self.model.blocks[block_id + 1].z[i + 1].value = 0

            # check if constraint is constructed sum_j z_kj = 1, if not it is
            # needed to add
            if self.model.blocks[block_id + 1].component('z_con') is None:
                # construct the constraint
                self.model.blocks[block_id + 1].z_con = Constraint(
                    expr=self.model.blocks[block_id + 1].z[i + 1] == 1)
            else:
                # add new variable to existing constraint
                self.model.blocks[block_id + 1].z_con.set_value(
                    self.model.blocks[block_id + 1].z_con.body +
                    self.model.blocks[block_id + 1].z[i + 1] == 1)

            # add new variable to existing overlapping
            # constraint: w_ki = sum_{t}rt_ki for atomic blocks
            for m in self.model.num_resource:
                self.model.blocks[block_id + 1].w_con[m].set_value(
                    self.model.blocks[block_id + 1].w_con[m].body -
                    column[m-1] *
                    self.model.blocks[block_id + 1].z[i + 1] == 0)

        elif len(self.approx_data.inner_points.KT[block_id]) > 1:
            hyper_block_obj = self.check_hyper_block(block_id)
            # add new variable z
            hyper_block_obj.z_set.add(i + 1)
            hyper_block_obj.z.add(i + 1)
            hyper_block_obj.z[i + 1].value = 0

            # check if constraint is constructed sum_j z_kj = 1, if not it is
            # needed to add
            if hyper_block_obj.component('z_con') is None:
                # construct the constraint
                hyper_block_obj.z_con = \
                    Constraint(expr=hyper_block_obj.z[i + 1] == 1)
            else:
                # add new variable to existing constraint
                hyper_block_obj.z_con.set_value(
                    hyper_block_obj.z_con.body + hyper_block_obj.z[i + 1] == 1)

            # add new variable to existing overlapping constraints:
            # w_ki = v_ki for atomic blocks
            for k in hyper_block_obj.kt:
                for m in self.model.num_resource:
                    hyper_block_obj.w_con[k, m].set_value(
                        hyper_block_obj.w_con[k, m].body -
                        column[k-1][m-1] * hyper_block_obj.z[i + 1] == 0)

    def set_slack_weights(self, slack_weights):
        """Sets slack weights in the objective function

        :param slack_weights: Values for slack weights
        :type slack_weights: ndarray
        """
        for i in range(self.block_model.cuts.num_of_global_cuts + 1):
            self.model.gamma[i + 1] = slack_weights[i]

    def compute_and_set_default_slack_weights(self):
        """Computes slack weights by defaults method, i.e. it is computed
        based on the zero resource of all columns in the following way
        :math:`\\gamma_i = 1.1\\max\\limits_{w_j \\in R_k, k \\in K} w_{j0},
        i \\in [m]`"""
        max_val = float('-inf')
        for k in range(self.block_model.num_blocks):
            for j in range(self.approx_data.get_inner_points_size(k)):
                point, column = self.approx_data.inner_points[k, j]
                if column[0] > max_val:
                    max_val = column[0]
        if max_val < 1e2:
            max_val = 1e2

        slack_weights = np.full(shape=
                                self.block_model.cuts.num_of_global_cuts + 1,
                                fill_value=1.1 * max_val)

        self.set_slack_weights(slack_weights)

    def solve(self, solver_name):
        """Solves the problem by calling an external solver

        :param solver_name: External solver name
        :type solver_name: str
        :return: Index of active cells blockwise, weights of the columns \
        :math:`z`, solution in original space, \
        solution in image space, slack values, dual solution and objective value
        :rtype: tuple

        .. Note::
            The comments where the dual values are extracted
        """
        opt = SolverFactory(solver_name)
        result = opt.solve(self.model, tee=False)

        sol_is_feasible = True
        if result.solver.status == SolverStatus.warning:
            sol_is_feasible = False
            logger.info('Master problem is {0}: {1}'.format(
                result.solver.termination_condition,
                self.model.name))

        duals = None
        z = None
        x = None
        w = None
        slacks = None
        obj_value = None

        if sol_is_feasible:
            # get duals
            try:
                duals = np.zeros(shape=self.block_model.cuts.num_of_global_cuts)
                for i in self.model.lin_con:
                    # here one has to make sure if corrects sign of dual values
                    # is returned all solvers normally return the marginal
                    # values as dual values since for our formulation it is
                    # necessary to have the Lagrange multipliers, i.e.
                    # -marginal value newer versions of Ipopt (starting from
                    # 3.10.3 or 3.10.4) return the marginal value, then put '-'
                    # Gurobi returns marginal value, then put '-'
                    # Other solvers were not checked
                    duals[i - 1] = -self.model.dual[self.model.lin_con[i]]
            except KeyError:
                duals = None
            # get z variable values
            z = BlockVector()
            x = BlockVector()  # solution point in the original space
            w = BlockVector()  # solution point in the image space
            for k in range(self.block_model.num_blocks):
                z.set_block(k, np.zeros(
                    shape=self.approx_data.get_inner_points_size(k)))

                resulting_point = \
                    np.zeros(shape=self.block_model.block_sizes[k])

                resulting_column = np.zeros(
                    shape=self.block_model.cuts.num_of_global_cuts + 1)

                if self.block_model.sub_models[k].linear is False:
                    for j in range(self.approx_data.get_inner_points_size(k)):
                        z[k, j] = self.model.blocks[k + 1].z[j + 1].value
                        point, column = self.approx_data.inner_points[k, j]
                        resulting_point += \
                            self.model.blocks[k + 1].z[j + 1].value * point
                        resulting_column += \
                            self.model.blocks[k + 1].z[j + 1].value * column
                else:
                    for n in range(self.block_model.block_sizes[k]):
                        resulting_point[n] = \
                            self.model.blocks[k + 1].Y[n + 1].value

                    resulting_column = \
                        self.block_model.trans_into_im_space(k, resulting_point)

                x.set_block(k, resulting_point)
                w.set_block(k, resulting_column)

            obj_value = self.block_model.cuts.obj.eval(x)
            # add z value for hyper-blocks
            for k in self.approx_data.inner_points.KT.keys():
                if k not in range(self.block_model.num_blocks):
                    z.set_block(k, np.zeros(
                        shape=self.approx_data.get_inner_points_size(k)))
                    hyper_block = self.check_hyper_block(k)
                    for j in range(self.approx_data.get_inner_points_size(k)):
                        z[k, j] = hyper_block.z[j + 1].value

            slacks = [0] * self.block_model.cuts.num_of_global_cuts
            for i in range(self.block_model.cuts.num_of_global_cuts):
                slacks[i] = (self.model.slack_pos[i + 1].value,
                             self.model.slack_neg[i + 1].value)

            slacks_hyper = {}
            slacks_hyper_max = 0
            for block_id in self.model.hyper_block_id:
                hyper_block = \
                    self.model.find_component(
                        'hyper_block_{0}'.format(block_id))
                slack_array = {}
                for k in hyper_block.kt:
                    for t in self.model.num_resource:
                        slack_array[k, t] = (hyper_block.slack_pos[k, t].value,
                                             hyper_block.slack_neg[k, t].value)
                        slack_value = max(slack_array[k, t])
                        if slack_value > slacks_hyper_max:
                            slacks_hyper_max = slack_value
                slacks_hyper[block_id] = slack_array

        return z, x, w, slacks, duals, obj_value, slacks_hyper_max, slacks_hyper

    def check_hyper_block(self, block_id):
        # add hyper block in pyomo model if not exist, return block obj
        if self.model.component('hyper_block_{0}'.format(block_id)) is None:
            new_block_obj = Block()
            # initialize some block data, here can be done what is necessary
            new_block_obj.z_set = Set(dimen=1)
            new_block_obj.z = Var(new_block_obj.z_set,
                                  domain=Reals, bounds=(0, None))
            kt_value = [i+1 for i in
                        self.approx_data.inner_points.KT[block_id]
                        if self.block_model.sub_models[i].linear is False]

            new_block_obj.kt = Set(dimen=1, initialize=kt_value)

            # define slacks
            new_block_obj.slack_pos = Var(
                new_block_obj.kt,
                self.model.num_resource,
                domain=Reals,
                bounds=(0, None), initialize=0)

            new_block_obj.slack_neg = Var(
                new_block_obj.kt,
                self.model.num_resource,
                domain=Reals,
                bounds=(0, None), initialize=0)

            # initialize overlapping constraints
            def w_con_rule_hyper_block(obj, k, m_index):
                return self.model.w[k, m_index] - obj.slack_pos[k, m_index] \
                       + obj.slack_neg[k, m_index] == 0

            new_block_obj.w_con = \
                Constraint(new_block_obj.kt, self.model.num_resource,
                           rule=w_con_rule_hyper_block)

            # add block as attribute to the model
            self.model.add_component('hyper_block_{0}'.format(block_id),
                                     new_block_obj)
            hyper_block = \
                self.model.find_component('hyper_block_{0}'.format(block_id))
            # add hyper block slacks to obj function
            new_expression = self.model.obj.expr + \
                sum(self.model.gamma[i] * (hyper_block.slack_pos[k, i] +
                                           hyper_block.slack_neg[k, i])
                    for i in self.model.num_resource for k in hyper_block.kt)
            self.model.obj.set_value(new_expression)
            self.model.hyper_block_id.add(block_id)

        hyper_block = \
            self.model.find_component('hyper_block_{0}'.format(block_id))

        return hyper_block
