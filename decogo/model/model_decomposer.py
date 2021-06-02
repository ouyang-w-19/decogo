"""Performs automatic reformulation of the Pyomo model"""

import itertools
import logging
import os

import networkx as nx
from pyomo.core.base.constraint import Constraint, IndexedConstraint, \
    SimpleConstraint
from pyomo.core.base.var import Var, SimpleVar, IndexedVar
from pyomo.core.expr.numeric_expr import ProductExpression, SumExpression, \
    UnaryFunctionExpression, PowExpression, \
    DivisionExpression, NegationExpression, AbsExpression, \
    MonomialTermExpression
from pyomo.core.expr.visitor import identify_variables, replace_expressions
from pyomo.environ import ConcreteModel, Block, Objective, minimize, maximize, \
    SolverFactory, Reals, Set

logger = logging.getLogger('decogo')


class PyomoModelDecomposer:
    """This class performs the decomposition of the Pyomo model based on the
    defined blocks. If for definition of Pyomo model keyword Block was used
    explicitly, then the reformulation is not performed.

    :param model: Input pyomo model
    :type model: ConcreteModel
    :param settings: Settings
    :type settings: Settings
    :param blocks: List of original names (strings) of variables collected \
    blockwise
    :type blocks: list
    :param original_obj_sense: Indicates the sense of the objective \
    (maximization or minimization)
    :type original_obj_sense: int
    :param number_defined_blocks: Number of defined blocks of the original \
    model, defaults to 1
    :type number_defined_blocks: int
    :param nconstraints: Overall number of the constraints of the input model \
    :type nconstraints: int
    :param nvars: Number of variables of the input model
    :type nvars: int
    """

    def __init__(self, model, settings):
        """Constructor method"""
        self.model = model
        self.settings = settings
        self.blocks = []  # only names of the variables
        self.original_obj_sense = self.model.obj.sense
        self.number_defined_blocks = 1  # by default is one block

        self.nconstraints = 0
        self.nvars = 0

    def decompose(self):
        """The function which calls other functions for block detection and
        reformulation. Reformulates Pyomo model as block-separable with
        linear objective, with nonlinear local constraints and linear global
        constraints.

        :return: Reformulated model, variables (string names) collected \
        blockwise, original objective sense
        :rtype: (ConcreteModel, list, int)
        """
        self._compute_number_of_defined_blocks()
        self._compute_initial_statistics()
        self._preprocessing()
        self._compute_blocks()

        # no reformulation if the blocks are given
        if self.number_defined_blocks == 1:
            self._reformulate()

        return self.model, self.blocks, self.original_obj_sense

    def _find_connected_components(self):
        """Construct the graph which describes the sparsity pattern of the
        Hessian of the Lagrangian. Two nodes are connected if the
        corresponding variables are contained in the same nonlinear expression.
        """

        # construct graph for all variables
        G = nx.Graph()
        for var_name in self.model.component_map(Var):
            G.add_node(var_name)

        # store nonlinear variables in order later to create one common block
        # for linear variables
        nonlinear_vars = set()

        for object_name, object in self.model.component_map(
                [Objective, Constraint], active=True).iteritems():
            if isinstance(object, Objective):
                expr = object.expr
            else:
                expr = object.body
            self._add_edges_to_graph(G, expr, nonlinear_vars)

        # block that contains only linear variables, i.e. variables that are
        # contained only linear expressions
        linear_block = []
        for component in nx.connected_components(G):
            if component.issubset(nonlinear_vars):
                self.blocks.append(list(component))
            else:
                # here component should consist of one variable element
                linear_block.append(component.pop())

        if len(linear_block) != 0:
            self.blocks.append(linear_block)

    def _add_edges_to_graph(self, g, expr, nonlinear_vars):
        """ Recursive function for construction of the sparsity graph.
        The two nodes are connected if respective variables contained in the
        same nonlinear expression.

        :param g: Graph
        :type g: Graph
        :param expr: Expression which is currently processed
        :type expr: Expression
        :param nonlinear_vars: List of nonlinear variables
        :type nonlinear_vars: set
        """
        if expr.__class__ is SumExpression:
            for term in expr.args:
                self._add_edges_to_graph(g, term, nonlinear_vars)
        elif expr.__class__ is NegationExpression:
            for term in expr.args:
                self._add_edges_to_graph(g, term, nonlinear_vars)
        elif expr.__class__ is MonomialTermExpression:
            pass
        elif expr.__class__ is DivisionExpression or expr.__class__ is PowExpression or \
                expr.__class__ is UnaryFunctionExpression:
            vars_objects = identify_variables(expr)
            # add edges to graph
            var_names = list(item.name for item in vars_objects)
            for pair in itertools.combinations(var_names, 2):
                g.add_edge(pair[0], pair[1])
            nonlinear_vars.update(var_names)  # store nonlinear variables
        elif expr.__class__ is ProductExpression:
            # product expression consists of tuple of length two
            # if one element is a number and the other SumExpression, then it
            # is necessary to go one level further, i.e. into SumExpression
            if any(isinstance(term, (int, float)) for term in expr.args) and \
                    any(term.__class__ is SumExpression for term in expr.args):
                for term in expr.args:
                    if term.__class__ is SumExpression:
                        self._add_edges_to_graph(g, term, nonlinear_vars)
            else:
                vars_objects = identify_variables(expr)
                # add edges to graph
                var_names = list(item.name for item in vars_objects)
                for pair in itertools.combinations(var_names, 2):
                    g.add_edge(pair[0], pair[1])
                nonlinear_vars.update(var_names)  # store nonlinear variables
        elif expr.__class__ is AbsExpression:
            raise Exception('Dev: abs expressions are not supported yet')

    def _compute_initial_statistics(self):
        """Compute initial statistics such as number of variables and
        constraints
        """
        if self.number_defined_blocks == 1:
            nvars = self.model.nvariables()
            nconstraints = self.model.nconstraints()
        else:
            nvars = 0
            for var_obj in self.model.component_objects(Var, active=True):
                if var_obj.__class__ is SimpleVar:
                    nvars += 1
                elif var_obj.__class__ is IndexedVar:
                    nvars += len(var_obj)

            nconstraints = 0
            for con_obj in self.model.component_objects(Constraint,
                                                        active=True):
                if con_obj.__class__ is SimpleConstraint:
                    nconstraints += 1
                elif con_obj.__class__ is IndexedConstraint:
                    nconstraints += len(con_obj)

        logger.info('Original model:')
        logger.info('{0: <50}{1: <30}'.format('Number of variables:', nvars))
        logger.info(
            '{0: <50}{1: <30}'.format('Number of constraints:', nconstraints))
        logger.info('')

    def _preprocessing(self):
        """Performs the following preprocessing steps:

        * deletes trivial constraints (i.e. :math:`x \\leq a`) and updates the \
        variables bounds;

        * checks if objective sense is :math:`\\max`; if so, then \
        :math:`\\max f(x) = \\min -f(x)`

        * estimates bounds of unbounded variables, if the respective setting \
        is set to ``True``
        """

        # check if no variables have the name 'new' in their names
        if self.number_defined_blocks == 1:
            # we don't proceed with it, if we don't do the reformulation
            for block_obj in self.model.block_data_objects():
                for var_name, var_obj in block_obj.component_map(Var,
                                                                 active=True).iteritems():
                    if 'new' in var_name:
                        raise Exception(
                            'Modelling issue: some of the variables contain '
                            'word "new", rename these variables')

        # delete trivial constraints and check if no constraints have the name
        # 'new' in their names
        for block_obj in self.model.block_data_objects():
            for con_name, con_obj in block_obj.component_map(Constraint,
                                                             active=True).iteritems():
                if self.number_defined_blocks == 1:  # we don't check it, since we don't do reformulation
                    if 'new' in con_name:
                        raise Exception(
                            'Modelling issue: some of the constraints contain \ '
                            'word "new", rename these constraints')
                if con_obj.__class__ is SimpleConstraint:
                    if isinstance(con_obj.body, Var):
                        var_obj = con_obj.body
                        if con_obj.equality:
                            var_obj.setub(con_obj.upper.value)
                            var_obj.setlb(con_obj.lower.value)
                            var_obj.value = con_obj.lower.value
                        elif con_obj.upper is not None:
                            var_obj.setub(con_obj.upper.value)
                        elif con_obj.lower is not None:
                            var_obj.setlb(con_obj.lower.value)
                        block_obj.del_component(con_name)
                elif con_obj.__class__ is IndexedConstraint:
                    for index in con_obj:
                        if isinstance(con_obj[index].body, Var):
                            var_obj = con_obj[index].body
                            if con_obj[index].equality:
                                var_obj.setub(con_obj[index].upper.value)
                                var_obj.setlb(con_obj[index].lower.value)
                                var_obj.value = con_obj[index].lower.value
                            elif con_obj[index].upper is not None:
                                var_obj.setub(con_obj[index].upper.value)
                            elif con_obj.lower is not None:
                                var_obj.setlb(con_obj[index].lower.value)
                            con_obj[index].deactivate()

        if self.settings.decomp_estimate_var_bounds is True:
            self._estimate_var_bounds()

        # if objective sense is max, then max obj(x) = min -obj(x)
        obj_name, obj = next(
            self.model.component_map(Objective, active=True).iteritems())
        if obj.sense == -1:  # if obj sense is max
            obj.sense = 1  # set to min
            obj.expr = -obj.expr

    def _get_blocks(self):
        """Identifies the blocks if the there are more defined blocks than one
        (by default in Pyomo each model has at least one block always),
        i.e. it is used explicitly keyword Block. The variables which appear
        only in linear blocks are merged into one block.
        """
        for block_obj in self.model.component_data_objects(Block):
            var_names_list = []
            for var_name, var_obj in \
                    block_obj.component_map(Var, active=True).iteritems():
                if var_obj.__class__ is SimpleVar:
                    var_names_list.append(var_obj.name)
                elif var_obj.__class__ is IndexedVar:
                    for index in var_obj:
                        var_names_list.append(var_obj[index].name)

            if len(var_names_list) != 0:
                self.blocks.append(var_names_list)

        self._add_copy_constraints()
        self._merge_linear_blocks()

    def _add_copy_constraints(self):
        """Adds copy constraints in the following case:

        If some nonlinear constraints have not all variables in the same block,
        then the common variable for these constraints is identified. For
        this variable, a new variable and corresponding copy constraint is
        created.In the expression trees of the nonlinear constraints, a common
        variable is replaced by the new variable
        """

        # dictionary: variable name -> list of nonlinear constraints names that
        # contain this variable
        variables_constraints_dict = {}
        for con_obj in self.model.component_objects(Constraint, active=True):
            if con_obj.__class__ is SimpleConstraint:
                degree = con_obj.expr.polynomial_degree()
                if degree is None or degree > 1:
                    blocks_vars_dict = self._determine_block_expr(con_obj.expr)
                    if len(blocks_vars_dict) > 1:
                        for key in blocks_vars_dict:
                            for var_to_copy_name in blocks_vars_dict[key]:
                                if var_to_copy_name in variables_constraints_dict:
                                    variables_constraints_dict[
                                        var_to_copy_name].append(con_obj.name)
                                else:
                                    variables_constraints_dict[
                                        var_to_copy_name] = [con_obj.name]
            elif con_obj.__class__ is IndexedConstraint:
                for index in con_obj:
                    degree = con_obj[index].expr.polynomial_degree()
                    if degree is None or degree > 1:
                        blocks_vars_dict = self._determine_block_expr(
                            con_obj[index].expr)
                        if len(blocks_vars_dict) > 1:
                            for key in blocks_vars_dict:
                                for var_to_copy_name in blocks_vars_dict[key]:
                                    if var_to_copy_name in variables_constraints_dict:
                                        variables_constraints_dict[
                                            var_to_copy_name].append(
                                            con_obj[index].name)
                                    else:
                                        variables_constraints_dict[
                                            var_to_copy_name] = [
                                            con_obj[index].name]

        # find the variable which is contained in the constraints the most
        # frequently or just that are contained more
        # than once in different constraints
        # and enforce to copy the variable not from the subblocks
        for var_to_copy_name in variables_constraints_dict:
            if len(variables_constraints_dict[
                       var_to_copy_name]) > 1 and 'subblocks' not in var_to_copy_name:
                # this is a hard fix
                var_to_copy = self.model.find_component(var_to_copy_name)
                for con_name in variables_constraints_dict[var_to_copy_name]:
                    constraint_obj = self.model.find_component(con_name)
                    # get the parent Block object to which are assigned other
                    # variables, except the one which
                    # has to be copied
                    constr_variables = list(
                        identify_variables(constraint_obj.expr))
                    for var in constr_variables:
                        if var.name != var_to_copy.name:
                            parent_block = var.parent_block()
                            break

                    # new copy variable creation
                    if parent_block.component('copy_variables') is None:
                        # variables initialization, it looks like one variable
                        # could be enough, but it considered that it could be
                        # more. That's why indexed variable and indexed
                        # constraint is used
                        parent_block.copy_variables_index_set = Set()
                        parent_block.copy_variables = Var(
                            parent_block.copy_variables_index_set)

                        # constraint initialization
                        parent_block.copy_constraints_index_set = Set()
                        parent_block.copy_constraints = Constraint(
                            parent_block.copy_constraints_index_set)
                        add_new_variable = True
                    else:
                        # we need to check if the current variable have been
                        # already copied. If yes, then we don't add new
                        # variable and new constraint and just use the existing
                        # variable
                        add_new_variable = True
                        for idx in parent_block.copy_constraints:
                            copy_constraints_vars = identify_variables(
                                parent_block.copy_constraints[idx].expr)
                            for copy_con_var in copy_constraints_vars:
                                if var_to_copy_name == copy_con_var.name:
                                    add_new_variable = False
                                else:
                                    new_copy_variable = copy_con_var
                            if add_new_variable is False:
                                break

                    if add_new_variable is True:
                        # add new variable
                        parent_block.copy_variables_index_set.add(
                            len(parent_block.copy_variables_index_set) + 1)
                        new_copy_variable = parent_block.copy_variables.add(
                            len(parent_block.copy_variables_index_set))
                        new_copy_variable.domain = var_to_copy.domain
                        new_copy_variable.setlb(var_to_copy.lb)
                        new_copy_variable.setub(var_to_copy.ub)

                        # add new variable to the list of blocks
                        for k, block in enumerate(self.blocks):
                            if block[0].startswith(parent_block.name) is True:
                                block.append(new_copy_variable.name)
                                break

                        # add new copy constraint
                        parent_block.copy_constraints_index_set.add(
                            len(parent_block.copy_constraints_index_set) + 1)
                        parent_block.copy_constraints.add(
                            len(parent_block.copy_constraints_index_set),
                            var_to_copy == new_copy_variable)

                    # expression with new copied variable
                    substitution_map = {}
                    for var in constr_variables:
                        if var.name == var_to_copy_name:
                            substitution_map[id(var)] = new_copy_variable
                        else:
                            substitution_map[id(var)] = var
                    new_expr = replace_expressions(constraint_obj.expr,
                                                   substitution_map)
                    constraint_obj.set_value(new_expr)

    def _merge_linear_blocks(self):
        """Merges linear blocks into one block, nonlinear are left as they are

        :raise ValueError: If variable of nonlinear constraint belongs to \
        different blocks
        """
        # from the beginning assume that all blocks are linear
        linear_blocks_list = [True] * len(self.blocks)

        for con_obj in self.model.component_objects(Constraint, active=True):
            if con_obj.__class__ is SimpleConstraint:
                degree = con_obj.expr.polynomial_degree()
                if degree is None or degree > 1:
                    blocks_vars_dict = self._determine_block_expr(con_obj.expr)
                    if len(blocks_vars_dict) > 1:
                        raise ValueError(
                            'Variables of nonlinear constraint seem to belong '
                            'to different blocks')
                    # it is expected that dictionary will have one key, and we
                    # need exactly this key
                    linear_blocks_list[next(iter(blocks_vars_dict))] = False
            elif con_obj.__class__ is IndexedConstraint:
                for index in con_obj:
                    degree = con_obj[index].expr.polynomial_degree()
                    if degree is None or degree > 1:
                        blocks_vars_dict = self._determine_block_expr(
                            con_obj[index].expr)
                        if len(blocks_vars_dict) > 1:
                            raise ValueError(
                                'Variables of nonlinear constraint seem to '
                                'belong to different blocks')
                        # it is expected that dictionary will have one key, and
                        # we need exactly this key
                        linear_blocks_list[next(iter(blocks_vars_dict))] = False

        # merge
        new_blocks = []
        linear_block = []
        for k in range(len(linear_blocks_list)):
            if linear_blocks_list[k] is True:
                linear_block += self.blocks[k]
            else:
                new_blocks.append(self.blocks[k])

        if len(linear_block) != 0:
            new_blocks.append(linear_block)
            self.blocks = new_blocks

    def _compute_blocks(self):
        """Calls functions depending on the number of defined blocks. If there
        is only one block detected, then is constructs the sparsity graph
        depending on the expressions. If there are more than one block, then it
        simply reads the blocks as defined.
        """
        if self.number_defined_blocks > 1:
            self._get_blocks()
        else:
            self._find_connected_components()

    def _determine_block_expr(self, expr):
        """Assigns the block identifier to the given expression. If the
        variables in the expression are contained in other blocks, it returns
        also this blocks

        :param expr: Expression which needs to be assigned to the blocks
        :type expr: Expression
        :return: Block identifier -> variable names dictionary. If length of \
        dictionary is greater than 1, it means that variables of the \
        expression are contained in the several blocks
        :rtype: dict
        """
        expr_variable_objects = identify_variables(expr)
        expr_variable_names = set(item.name for item in expr_variable_objects)

        block_vars_dict = {}
        for k, block in enumerate(self.blocks):
            intersection = set(block).intersection(expr_variable_names)
            if len(intersection) == len(expr_variable_names):
                # this means variables from expressions are subset of the
                # block, and there is no point to continue the search in
                # other blocks
                block_vars_dict[k] = intersection
                return block_vars_dict
            else:
                if len(intersection) > 0:
                    block_vars_dict[k] = intersection

        return block_vars_dict

    def _reformulate(self):
        """Performs block-separable reformulation for the case if one block
        is identified. For that case it computes the blocks based on the
        nonlinear expressions
        """

        # handle objective
        obj_name, obj = next(self.model.component_map(Objective).iteritems())
        self._find_separable_sub_expr_and_replace(obj.expr)

        # handle constraints
        for con_name, con_obj in self.model.component_map(
                Constraint).iteritems():
            # avoid checking already reformulated constraints
            if 'new' not in con_name:
                # if all variables belong to the same block, then we don't do
                # the reformulation
                blocks_var_dict = self._determine_block_expr(con_obj.body)
                if len(blocks_var_dict) > 1:
                    self._find_separable_sub_expr_and_replace(con_obj.body)

    def _find_separable_sub_expr_and_replace(self, expr):
        """Recursive function for walking through the expression trees and
        substituting the nonlinear expressions which belong to the one block
        by a new variable

        :param expr: Expression which is processed
        :type expr: ProductExpression, SumExpression, \
        UnaryFunctionExpression, \ PowExpression, DivisionExpression, \
        NegationExpression, AbsExpression, MonomialTermExpression, Var
        :return: Block id to which this expression belongs. For some \
        subexpressions that should not be substituted None is returned.
        :rtype: int, None
        """

        if expr.__class__ is SumExpression:
            local_expr = {k: 0 for k in range(len(self.blocks))}
            indices_to_remove = []
            for i, term in enumerate(expr._args_):
                k = self._find_separable_sub_expr_and_replace(term)
                if k is not None:
                    local_expr[k] += term
                    indices_to_remove.append(i)

            # reformulation
            if len(indices_to_remove) is not 0:
                expr._args_ = [item for idx, item in enumerate(expr._args_) if
                               idx not in indices_to_remove]
                for k in local_expr:
                    if local_expr[k] is not 0:
                        # create new variable
                        lower, upper = self._comp_bounds_new_vars(
                            local_expr[k].clone())
                        new_variable_name = self._create_new_var(lower, upper,
                                                                 block_id=k)
                        self._create_local_nonlin_constraint(local_expr[k],
                                                             new_variable_name)
                        expr._args_.append(
                            self.model.__getattribute__(new_variable_name))
                expr._nargs = len(expr._args_)
        elif expr.__class__ is NegationExpression:
            term = expr._args_[0]
            k = self._find_separable_sub_expr_and_replace(term)

            # reformulation
            if k is not None:
                # create new variable
                lower, upper = self._comp_bounds_new_vars(term.clone())
                new_variable_name = self._create_new_var(lower, upper,
                                                         block_id=k)
                self._create_local_nonlin_constraint(term, new_variable_name)
                expr._args_ = (self.model.__getattribute__(new_variable_name),)
        elif expr.__class__ is MonomialTermExpression:
            return None
        elif expr.__class__ is DivisionExpression or expr.__class__ is PowExpression \
                or expr.__class__ is UnaryFunctionExpression:
            blocks_vars_dict = self._determine_block_expr(expr)
            # it is expected that dictionary will have one key, and we need
            # exactly this key
            return next(iter(blocks_vars_dict))
        elif expr.__class__ is ProductExpression:
            if any(isinstance(term, (int, float)) for term in expr.args) and \
                    any(term.__class__ is SumExpression for term in expr.args):
                for term in expr.args:
                    if term.__class__ is SumExpression:
                        self._find_separable_sub_expr_and_replace(term)
            else:
                blocks_vars_dict = self._determine_block_expr(expr)
                # it is expected that dictionary will have one key, and we need
                # exactly this key
                return next(iter(blocks_vars_dict))
        elif expr.__class__ is AbsExpression:
            raise Exception('Dev: abs expressions are not supported yet')

    def _compute_number_of_defined_blocks(self):
        """Gets the number of blocks in the model. This includes also root block
        (any Pyomo model has at least one block).
        """
        number_defined_blocks = len(list(self.model.block_data_objects()))
        self.number_defined_blocks = number_defined_blocks

    @staticmethod
    def _comp_bounds_new_vars(expr):
        """Computes bounds of new variables based on expression

        :param expr: Expression for which the bounds are computed
        :type expr: Expression
        :return: Upper and lower bound of the expression
        :rtype: (int, int)
        """
        new_model = ConcreteModel()
        var_list = list(identify_variables(expr))
        substitute_map = {}

        for var in var_list:
            if var.lb == float('-inf') or var.ub == float('inf'):
                return float('-inf'), float('inf')
            else:
                var_object = Var(bounds=(var.lb, var.ub), initialize=var.lb)
                new_model.add_component(var.name, var_object)
                substitute_map[id(
                    var)] = var_object  # for replacing expressions is necessary

        # objects should the same in the model and expression
        new_expr = replace_expressions(expr,
                                       substitute_map)
        new_model.obj = Objective(expr=new_expr, sense=minimize)
        opt = SolverFactory('scip')

        # add termination condition
        f_obj = open("scip.set", "w")
        f_obj.write("limits/time = 2")
        f_obj.close()

        results = opt.solve(new_model, tee=False)
        if results.solver.Message == 'time limit reached':
            lower = float('-inf')
        else:
            try:
                lower = new_model.obj.expr()
            except ZeroDivisionError:
                lower = float('-inf')

        new_model.obj.sense = maximize
        results = opt.solve(new_model, tee=False)
        if results.solver.Message == 'time limit reached':
            upper = float('inf')
        else:
            try:
                upper = new_model.obj.expr()
            except ZeroDivisionError:
                upper = float('inf')

        os.remove('scip.set')
        return lower, upper

    def _create_new_var(self, lower, upper, block_id):
        """Creates a new variable and adds it to the block list
        """
        new_variable = Var(within=Reals, bounds=(lower, upper),
                           initialize=lower)

        self.nvars += 1
        new_variable_name = 'x_new%d' % self.nvars
        self.model.add_component(new_variable_name, new_variable)

        # add new variable to block list
        self.blocks[block_id].append(new_variable_name)

        return new_variable_name

    def _create_local_nonlin_constraint(self, lhs_expr, rhs_var_name):
        """Creates local nonlinear constraints
        """
        self.nconstraints += 1
        new_con = Constraint(
            expr=lhs_expr - self.model.__getattribute__(rhs_var_name) == 0)
        self.model.add_component('cnew%s' % (self.nconstraints), new_con)

    def _estimate_var_bounds(self):
        """Estimates the bounds of the unbounded variables:

        * if :math:`x_i` has no lower bound, \
         then :math:`\\underline{x}_i = \\min x_i, x \\in P \\cap X`
        * if :math:`x_i` has no upper bound, then \
        :math:`\\overline{x}_i = \\max x_i, x \\in P \\cap X`
        """

        # save objective
        obj_name, obj_old = next(
            self.model.component_map(Objective).iteritems())
        self.model.del_component(obj_name)

        # set settings for scip with root node and aggressive heuristics

        file = open("scip.set", "w")

        file.write("limits/nodes = 1 \n"
                   "limits/time = 5 \n"
                   "presolving/restartfac = 0.03 \n"
                   "presolving/restartminred = 0.06 \n"
                   "constraints/setppc/cliquelifting = TRUE \n"
                   "presolving/boundshift/maxrounds = -1 \n"
                   "presolving/dualagg/maxrounds = -1 \n"
                   "presolving/tworowbnd/maxrounds = -1 \n"
                   "presolving/redvub/maxrounds = -1 \n"
                   "presolving/implfree/maxrounds = -1 \n"
                   "propagating/probing/maxuseless = 1500 \n"
                   "propagating/probing/maxtotaluseless = 75")
        file.close()

        opt = SolverFactory('scip')

        for block_obj in self.model.block_data_objects():
            for var_name, var_obj in block_obj.component_map(Var).iteritems():
                if var_obj.__class__ is SimpleVar:
                    if var_obj.lb is None or var_obj.ub is None:
                        self.model.obj = Objective(expr=var_obj)

                        if var_obj.lb is None:
                            # minimizing
                            opt.solve(self.model, tee=False)

                            for line in opt._log.split('\n'):
                                if "Dual Bound" in line:
                                    lb = float(line.split(":")[1])

                            # update bound
                            var_obj.setlb(lb)

                        if var_obj.ub is None:
                            # maximizing
                            self.model.obj.sense = -1
                            opt.solve(self.model, tee=False)

                            for line in opt._log.split('\n'):
                                if "Dual Bound" in line:
                                    ub = float(line.split(":")[1])

                            # update bound
                            var_obj.setub(ub)

                        self.model.del_component('obj')
                elif var_obj.__class__ is IndexedVar:
                    for index in var_obj:
                        if var_obj[index].lb is None or \
                                var_obj[index].ub is None:
                            self.model.obj = Objective(expr=var_obj[index])

                            if var_obj[index].lb is None:
                                # minimizing
                                opt.solve(self.model, tee=False)

                                for line in opt._log.split('\n'):
                                    if "Dual Bound" in line:
                                        lb = float(line.split(":")[1])

                                # update bound
                                var_obj[index].setlb(lb)

                            if var_obj[index].ub is None:
                                # maximizing
                                self.model.obj.sense = -1
                                opt.solve(self.model, tee=False)

                                for line in opt._log.split('\n'):
                                    if "Dual Bound" in line:
                                        ub = float(line.split(":")[1])

                                # update bound
                                var_obj[index].setub(ub)

                            self.model.del_component('obj')

        self.model.add_component('obj',
                                 obj_old)  # add old objective component back

        os.remove("scip.set")
