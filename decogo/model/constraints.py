"""Stores constraint data"""

import numpy as np
from pyomo.core.base.constraint import SimpleConstraint, IndexedConstraint, \
    Constraint
from pyomo.core.base.var import _GeneralVarData, SimpleVar, Var
from pyomo.core.expr.calculus.derivatives import differentiate, Modes
from pyomo.core.expr.logical_expr import EqualityExpression
from pyomo.core.expr.numeric_expr import NegationExpression, \
    MonomialTermExpression, ProductExpression, SumExpression, \
    ExpressionBase, LinearExpression
from pyomo.core.expr.visitor import identify_variables
from pyomo.environ import Objective

from decogo.util.block_vector import SparseBlockVector


class VarDomain:
    """This class stores the variable data.

    :param _upper_bound: Upper bound of the variable
    :type _upper_bound: float
    :param _lower_bound: Lower bound of the variable
    :type _lower_bound: float
    :param _type: Type of the variable, i.e. real, integer, binary
    :type _type: str
    """

    def __init__(self, upper_bound, lower_bound, type):
        """Constructor method"""
        self._upper_bound = upper_bound
        self._lower_bound = lower_bound
        self._type = type

    @property
    def upper_bound(self):
        """Gets the upper bound of the variable"""
        return self._upper_bound

    @upper_bound.setter
    def upper_bound(self, val):
        """Sets the upper bound of the variable"""
        self._upper_bound = val

    @property
    def lower_bound(self):
        """Gets the lower bound of the variable"""
        return self._lower_bound

    @lower_bound.setter
    def lower_bound(self, val):
        """Sets the lower bound of the variable"""
        self._lower_bound = val

    @property
    def type(self):
        """Gets the type of the variable"""
        return self._type


class LinearConstraint:
    """Class for storing the linear constraint

    :param lhs: Coefficients of right hand side of constraint
    :type lhs: SparseBlockVector
    :param relation: Constraint relation
    :type relation: str
    :param rhs: Right hand side value of constraint
    :type rhs: float
    :param is_local: Indicates of constraint is local, i.e. non zero values \
    of right hand are within the same block
    :type is_local: bool
    :param block_id: If constraint is local, then block is is assigned, \
    otherwise it is None
    :type block_id: int or None
    """

    def __init__(self, lhs, relation, rhs, block_sizes, const=0, block_id=None):
        """Constructor method"""

        self.lhs = SparseBlockVector(lhs, block_sizes)
        self.const = const

        self.relation = relation
        self.rhs = rhs

        if block_id is not None:
            self.block_id = block_id

        # by default constraint is global
        self.is_local = False

        # check if constr is local
        self._is_local()

    def _is_local(self):
        """Checks if constraint is local"""
        if len(self.lhs.blocks) == 1:
            self.is_local = True
            self.block_id = self.lhs.blocks[0]

    def eval(self, x):
        """Computes violation of constraint

        :param x: Given point to evaluate
        :type x: BlockVector
        :return: Violation of the constraint
        :rtype: float
        """
        viol = 0
        lhs = self.lhs.scalar_prod(x)
        value = lhs - self.rhs

        if self.relation == "<=":
            if value > 0:
                viol = value
        elif self.relation == "=":
            if value != 0:
                viol = value
        elif self.relation == ">=":
            if value < 0:
                viol = value
        return viol


class NonLinearConstraint:
    """Class for nonlinear constraint. This class stores original nonlinear
    Pyomo expression

    :param expr: Original Pyomo expression of nonlinear constraint
    :type expr: Expression
    :param orig_var_names_in_block: Original variable names from the input \
    Pyomo model
    :type orig_var_names_in_block: list
    :param _fun: Function :math:`f(x)`, where :math:`f(x)` is the function \
    from the constraint :math:`f(x) \\leq b`
    :type _fun: Expression
    :param relation: Relation of the constraint, i.e equality or inequality
    :type relation: str or None
    :param _vars_objects: Pyomo variable objects from the parameter expr and \
    is used only for OA solver
    :type _vars_objects: list or None
    :param gradient: Gradient computed symbolically and is used only in OA \
    solver
    :type gradient: dict
    """

    def __init__(self, expr, orig_var_names_in_block):
        """Constructor method"""
        self.expr = expr

        # this list also preserves the order of the variables
        self.orig_var_names_in_block = orig_var_names_in_block

        # the following attributes are necessary for computing gradients and
        # evaluation of constraints
        self._fun = None  # function
        self._rhs = None  # right hand side
        self.relation = None  # relation
        self._decompose()

        # only is needed for convex OA, and computed only for OA solver
        self._vars_objects = None
        self.gradient = None

    def _decompose(self):
        """Decomposes the nonlinear constraint :math:`f(x) \\leq b`, into
        function (left hand side), relation and right hand side. If :math:`f(
        x) \\geq b`, then the expression is reverted and represented
        as :math:`b \\leq f(x)`
        """
        if self.expr.__class__ is EqualityExpression:
            self._fun = self.expr.args[0]
            self.relation = '='
            self._rhs = self.expr.args[1]
        else:
            if isinstance(self.expr.args[0], ExpressionBase) is True:
                self._fun = self.expr.args[0]
                self.relation = '<='
                self._rhs = self.expr.args[1]
            else:
                self._fun = self.expr.args[1]
                self.relation = '>='
                self._rhs = self.expr.args[0]

    def eval(self, x):
        """Evaluates violation of the constraint

        :param x: Given point to evaluate
        :type x: list
        :return: Violation and value of the constraint
        :rtype: (float, float)
        """
        violation = 0

        self._assign_values_to_vars(x)
        value = self._fun() - self._rhs

        if self.relation == '=':
            if abs(value) > 1e-3:
                violation = abs(value)
        elif self.relation == '<=':
            if value > 1e-3:
                violation = value
        elif self.relation == '>=':
            if value < -1e-3:
                violation = abs(value)

        return violation, value

    def compute_gradient(self):
        """Computes just a gradient symbolically with sympy"""
        self._vars_objects = list(identify_variables(self.expr))
        gradient_list = differentiate(self._fun, wrt_list=self._vars_objects,
                                      mode=Modes.sympy)

        # create a map var_name -> partial derivative
        self.gradient = {}
        for i, var in enumerate(self._vars_objects):
            self.gradient[var.name] = gradient_list[i]

    def compute_gradient_at_point(self, x):
        """Evaluates already computed gradient at given point

        :param x: Given point to evaluate
        :type x: list
        :return: Gradient with the respect to variables
        :rtype: dict
        """
        grad_map = {}
        for key in self.gradient.keys():
            if isinstance(self.gradient[key], ExpressionBase) or isinstance(
                    self.gradient[key], Var):
                self._assign_values_to_vars(x)
                grad_map[key] = self.gradient[key]()
            else:
                grad_map[key] = self.gradient[key]

        return grad_map

    def _assign_values_to_vars(self, x):
        """Internal method used for evaluation of nonlinear function
        represented with Pyomo variables. This method exploits the property
        that Var objects are mutable objects, one has to be careful with that.
        It uses the list of variable objects in the attributes. Since these
        objects are mutable objects, any changes of variable value will be
        also effective in all expressions where these variables are contained.
        So it is enough to assign the value of variable in one place. However
        this looks very dangerous.

        :param x: Given evaluation point
        :type x: list
        """

        for i, val in enumerate(x):
            # get variable name from original variable names
            var_name = self.orig_var_names_in_block[i]
            for var_obj in self._vars_objects:
                # find the variable object with the same name and assign the
                # value
                if var_obj.name == var_name:
                    var_obj.value = val
                    break


class ObjectiveFunction:
    """This class stores the linear objective function.

    :param c: Linear objective function, stores the coefficients in sparse \
    format
    :type c: SparseBlockVector
    :param const: Constant value of objective value
    :type const: float
    """

    def __init__(self, coef, block_sizes, const):
        """Constructor method"""
        self.c = SparseBlockVector(coef, block_sizes)
        self.const = const

    def eval(self, x):
        """Evaluates the objective function \
         :math:`\\sum_\\limits{k \\in K} c_k x_k`

        :param x: Given point for evaluation
        :type x: BlockVector
        :return: the value of the objective function for :math:`x`
        :rtype: float
        """
        return self.c.scalar_prod(x)


class CutPool:
    """Container class for linear constraints. It contains both local and \
     global linear constraints.

    :param block_sizes: Number of variables in block
    :type block_sizes: list
    :param blocks: List of original variable names blockwise
    :type blocks: list
    :param obj: Objective function
    :type obj: ObjectiveFunction
    :param global_cuts: List of global constraints
    :type global_cuts: list
    :param local_cuts: Stores the list of local cuts blockwise
    :type local_cuts: dict
    :param copy_constraints: Stores the list of copy_constraints
    :type copy_constraints: list
    :param blocks_copy_constraints: Stores num of copy_constraints in each pair of blocks
    :type blocks_copy_constraints: dict
    """

    def __init__(self, model, blocks):
        """Constructor method

        :raise ValueError: If objective function is not linear
        """
        self.block_sizes = [len(item) for item in blocks]
        self.blocks = blocks

        # region objective reading and initialization
        obj_name, objective = next(model.component_map(Objective).iteritems())
        obj_expr = objective.expr
        degree = obj_expr.polynomial_degree()
        if degree is None or degree > 1:
            raise ValueError(
                'Dev: Objective is not linear, check the reformulation')
        coef, obj_const = self._get_linear_term_data(obj_expr)
        self.obj = ObjectiveFunction(coef, self.block_sizes, obj_const)
        # endregion

        # region linear constraints reading and initialization
        self.global_cuts = []
        self.local_cuts = {}
        for k in range(len(self.block_sizes)):
            self.local_cuts[k] = []

        for block_obj in model.block_data_objects():
            for con_name, con_obj in \
                    block_obj.component_map(Constraint,
                                            active=True).iteritems():
                if con_obj.__class__ is SimpleConstraint:
                    self._read_constraint_object(con_obj)
                elif con_obj.__class__ is IndexedConstraint:
                    for index in con_obj:
                        self._read_constraint_object(con_obj[index])

        # copy constraints
        self.copy_constraints = []
        self.blocks_copy_constraints = {}
        for cut_index in range(len(self.global_cuts)):
            self._add_copy_constraint(cut_index)
        # endregion

    def _read_constraint_object(self, con_obj):
        """Reads Pyomo constraints, detects if the constraint is linear.
        If yes, then it creates the linear constraint

        :param con_obj: Pyomo constraint object
        :type con_obj: Constraint
        """
        con_expr = con_obj.body
        if con_expr.polynomial_degree() == 1:
            coef, const = self._get_linear_term_data(con_expr)

            rhs = None
            relation = None
            if con_obj.equality is True:
                relation = "="
                rhs = con_obj.upper.value
            elif con_obj.upper is not None and con_obj.strict_upper is False:
                relation = "<="
                rhs = con_obj.upper.value
            elif con_obj.upper is not None and con_obj.strict_upper:
                relation = "<"
                rhs = con_obj.upper.value
            elif con_obj.lower is not None and con_obj.strict_lower is False:
                relation = ">="
                rhs = con_obj.lower.value
            elif con_obj.lower is not None and con_obj.strict_lower:
                relation = ">"
                rhs = con_obj.lower.value

            rhs -= const
            lin_con = LinearConstraint(coef, relation, rhs, self.block_sizes)

            if lin_con.is_local is True:
                self.local_cuts[lin_con.block_id].append(lin_con)
            else:
                self.global_cuts.append(lin_con)

    def _get_linear_term_data(self, expr):
        """Recursive function for reading and getting data for linear terms

        :param expr: Linear expression to parse
        :type expr: Expression
        :return: List of coefficients and constant
        :rtype: (list, int)
        """
        coef = []
        const = 0
        if expr.__class__ is SumExpression:
            for term in expr.args:
                new_coef, new_const = self._get_linear_term_data(term)
                for block_id, idx, val in new_coef:
                    coef.append((block_id, idx, val))
                const += new_const
        elif expr.__class__ is MonomialTermExpression:
            if isinstance(expr.args[0], (int, float)):
                coef_val = expr.args[0]
                var_name = expr.args[1].name
            else:
                var_name = expr.args[0].name
                coef_val = expr.args[1]
            k, i = self._get_variable_index_by_name(var_name)
            coef.append((k, i, coef_val))
        elif expr.__class__ is NegationExpression:
            new_coef, new_const = self._get_linear_term_data(expr.args[0])
            # multiply by -1, since it is negation expression
            for block_id, idx, val in new_coef:
                coef.append((block_id, idx, -val))
            const -= new_const
        elif expr.__class__ is ProductExpression:
            # if ProductExpression is here, than it is should be that one
            # argument is a number and the other is SumExpression
            if isinstance(expr.args[0], (int, float)):
                new_coef, new_const = self._get_linear_term_data(expr.args[1])
                multiplier = expr.args[0]
            else:
                new_coef, new_const = self._get_linear_term_data(expr.args[0])
                multiplier = expr.args[1]

            for block_id, idx, val in new_coef:
                coef.append((block_id, idx, multiplier * val))
            const += multiplier * new_const
        elif expr.__class__ is LinearExpression:
            for index, val in enumerate(expr.linear_coefs):
                var_name = expr.linear_vars[index].name
                k, i = self._get_variable_index_by_name(var_name)
                coef.append((k, i, val))
        elif expr.__class__ is Var or expr.__class__ is _GeneralVarData or \
                expr.__class__ is SimpleVar:
            k, i = self._get_variable_index_by_name(expr.name)
            coef.append((k, i, 1))
        elif isinstance(expr, (int, float)):
            const = expr
        else:
            raise ValueError(
                'Dev: Found expression object type which was not considered')
        return coef, const

    def _get_variable_index_by_name(self, var_name):
        """Get variable index from the list of blocks for sparse vector
        initialization

        :param var_name: Original variable name
        :type var_name: str
        :return: Pair of indices: block id and index in the block
        :rtype: (int, int)
        """
        j = 0  # index for iteration over the blocks
        while True:
            try:
                i = self.blocks[j].index(var_name)
                k = j
                break
            except ValueError:
                j += 1
        return k, i

    def add_lin_local_constr(self, coeff, relation, b, block_sizes):
        """Adds linear local constraint

        :param coeff: Coefficients of left hand side
        :type coeff: list
        :param relation: Constraint relation
        :type relation: str
        :param b: Right hand side of the constraint
        :type b: float
        :param block_sizes: Number of variables blockwise
        :type block_sizes: list
        """
        lin_con = LinearConstraint(coeff, relation, b, block_sizes)
        self.local_cuts[lin_con.block_id].append(lin_con)

    @property
    def num_of_cuts(self):
        """Gets total number of all linear constraints

        :return: Number of all linear constraint
        :rtype: int
        """
        num_cuts = len(self.global_cuts)
        for k in self.local_cuts.keys():
            num_cuts += len(self.local_cuts[k])

        return num_cuts

    @property
    def num_of_global_cuts(self):
        """Gets the number of linear global constraints

        :return: Number of global constraints only
        :rtype: int
        """
        return len(self.global_cuts)

    @property
    def num_of_local_cuts(self):
        """Gets the number of linear local constraints blockwise

        :return: Number of local constraints blockwise
        :rtype: int
        """
        return [len(self.local_cuts[k]) for k in range(len(self.block_sizes))]

    def evaluate_violation_global_constraints(self, point):
        """Evaluates violation of all global constraints

        :param point: Given point to evaluate
        :type point: BlockVector
        :return: Violation vector, which corresponds to violation of each \
        global constraint
        :rtype: ndarray
        """
        violation = np.zeros(shape=self.num_of_global_cuts)

        for i, cut in enumerate(self.global_cuts):
            viol = cut.eval(point)
            violation[i] = viol

        return violation

    def _add_copy_constraint(self, cut_index):
        """ Evaluate and add a global cut if it is a copy constraint
        :param cut_index: index of a global cut in global_cuts
        :type cut_index: int
        """
        cut = self.global_cuts[cut_index]
        copy_constraint_coeff_sum = 0

        if cut.relation != '=':
            copy_constraint_coeff_sum = 100
        else:
            if cut.rhs != 0:
                copy_constraint_coeff_sum = 100
            else:
                if cut.lhs.num_blocks != 2:
                    copy_constraint_coeff_sum = 100
                else:
                    for k in cut.lhs.vectors.keys():
                        if cut.lhs.vectors[k].data.size != 1:
                            copy_constraint_coeff_sum = 100
                            break
                        else:
                            copy_constraint_coeff_sum += cut.lhs.vectors[k].data[0]

        if copy_constraint_coeff_sum == 0:
            [k1, k2] = cut.lhs.vectors.keys()
            if k1 > k2:
                if (k2, k1) in self.blocks_copy_constraints.keys():
                    self.blocks_copy_constraints[k2, k1] += 1
                else:
                    self.blocks_copy_constraints[k2, k1] = 1
            else:
                if (k1, k2) in self.blocks_copy_constraints.keys():
                    self.blocks_copy_constraints[k1, k2] += 1
                else:
                    self.blocks_copy_constraints[k1, k2] = 1
            self.copy_constraints.append(cut)
