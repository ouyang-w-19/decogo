import os
import csv
import pandas as pd
import pyomo.environ as pyomo
import pyomo.network as network
from math import ceil

# ==============================================================================
# *** USER-INPUT *** :
# --------------------
superstructure = 'S12'  # 'S4', 'S8', 'S12', 'S16'
load_case = 'L24'       # 'L1', 'L2', 'L4', 'L6', 'L8', 'L12', 'L16', 'L24'
load_cases_per_block = 6
data_instance = 1     # 0, 1, ..., 9
solver_name = 'baron'
# Note: There are 2 additional load cases in every file, that are only used for
# correct sizing. So L1 contains 3 Load cases and L2 contains 4, etc...
# ==============================================================================


# ==============================================================================
# DATA AND PREPROCESSING:
# -----------------------
# Get DESSLib data from csv-file
ins_name = '%s%s_%s' % (superstructure, load_case, data_instance)
path = os.path.join('C:/Solver/decogo/tests/examples/tu/DESSLib_testmodel', 'DESSLib_instances',
                    superstructure, load_case, ins_name, 'ins%s.csv' % ins_name)
if os.path.isfile(path):

    with open(path) as f:
        csv_reader = csv.reader(f)
        header = next(csv_reader)[1:]
        comp_data = pd.DataFrame(columns=header)
        for row in csv_reader:
            if row[0].startswith('AC') or row[0].startswith('TC') or \
                    row[0].startswith('CHP') or row[0].startswith('Boiler'):
                comp_data.loc[row[0]] = pd.Series(
                    index=header, data=[float(j) for j in row[1:]])
            elif row[0] == 'demands':
                demands = [int(j) for j in row[1:]]
            elif row[0] == 'part':
                part = [float(j) for j in row[1:]]
            elif row[0] == 'E_heat':
                E_heat = [float(j) for j in row[1:]]
            elif row[0] == 'E_cold':
                E_cold = [float(j) for j in row[1:]]
            elif row[0] == 'E_el':
                E_el = [float(j) for j in row[1:]]
            elif row[0] == 'gamma_CF':
                gamma_CF = float(row[1])
            elif row[0] == 'i':
                i = float(row[1])
            elif row[0] == 'p_gas_buy':
                p_gas_buy = float(row[1])
            elif row[0] == 'p_el_buy':
                p_el_buy = float(row[1])
            elif row[0] == 'p_el_sell':
                p_el_sell = float(row[1])
            else:
                continue
else:
    raise ValueError('Could not find the file for the requested scenario. '
                     'Please, check your input!')

# present value factor:
apvf = ((1 + i)**gamma_CF - 1) / (i * (1 + i)**gamma_CF)

# Number of time related blocks (round up to next integer!):
total_nbr_of_load_cases = int(load_case.lstrip('L')) + 2  # 2 sizing steps
nbr_of_time_blocks = ceil(total_nbr_of_load_cases/load_cases_per_block)
# Create a list with global load case tuples:
# E.g.: [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 1), (6, 1), (7, 1), ...]
# Probably there is a nicer way, but it works for now ...
lc, hr, blc = [], 0, 0  # init
while hr < total_nbr_of_load_cases:
    for ts_in_block in range(load_cases_per_block):
        if len(lc) < total_nbr_of_load_cases:
            lc.append((hr, blc))
            hr += 1
        else:
            break
    blc += 1
# ==============================================================================


# ==============================================================================
# PYOMO MODEL:
# ------------
m = pyomo.ConcreteModel()

m.lc_set = pyomo.Set(dimen=2, initialize=lc, ordered=True)
m.slices = pyomo.Set(initialize=range(nbr_of_time_blocks), ordered=True)
m.lc_set_slices = pyomo.Set(m.slices, dimen=2, within=m.lc_set,
                            ordered=True, initialize=
                            lambda _m, slc: [lc_tup for lc_tup in lc
                                             if lc_tup[1] == slc])
# Weighting of each load case
m.part = pyomo.Param(m.lc_set, initialize={
    _lc: part[j] for j, _lc in enumerate(m.lc_set)})
# ==============================================================================


# ==============================================================================
# ELECTRICITY HUB:
# ----------------
# buy, sell, sink (CHP), source (TC)
m.elec_hub = pyomo.Block()
m.elec_hub.E_el = pyomo.Param(m.lc_set, initialize={
    _lc: E_el[j] for j, _lc in enumerate(m.lc_set)})
m.elec_hub.IN = network.Port()
m.elec_hub.OUT = network.Port()
def r_subblock_elec_hub(b, slc):
    slc_idx = sorted(set(b.model().lc_set_slices[slc]))
    b.ELEC_BUY = pyomo.Var(slc_idx, within=pyomo.NonNegativeReals, bounds=(0, 100000))
    b.ELEC_SELL = pyomo.Var(slc_idx, within=pyomo.NonNegativeReals, bounds=(0, 100000))
    b.ELEC_IN = pyomo.Var(slc_idx, within=pyomo.NonNegativeReals, bounds=(0, 100000))
    b.ELEC_OUT = pyomo.Var(slc_idx, within=pyomo.NonNegativeReals, bounds=(0, 100000))
    b.parent_block().IN.add(b.ELEC_IN, 'ELEC_%s' % slc, network.Port.Extensive,
                            include_splitfrac=False)
    b.parent_block().OUT.add(b.ELEC_OUT, 'ELEC_%s' % slc, network.Port.Extensive,
                             include_splitfrac=False)
m.elec_hub.subblocks = pyomo.Block(m.slices, rule=r_subblock_elec_hub)

def r_elec_balance(comp, *t):
    ELEC_IN = comp.subblocks[t[1]].ELEC_IN
    ELEC_OUT = comp.subblocks[t[1]].ELEC_OUT
    ELEC_BUY = comp.subblocks[t[1]].ELEC_BUY
    ELEC_SELL = comp.subblocks[t[1]].ELEC_SELL
    return ELEC_BUY[t] + ELEC_IN[t] == ELEC_SELL[t] + ELEC_OUT[t] + comp.E_el[t]
m.elec_hub.con_elec_balance = pyomo.Constraint(m.lc_set, rule=r_elec_balance)
# ==============================================================================


# ==============================================================================
# FUEL SOURCE:
# ------------
m.fuel_src = pyomo.Block()
m.fuel_src.OUT = network.Port()

def r_subblock_fuel_src(b, slc):
    slc_idx = sorted(set(b.model().lc_set_slices[slc]))
    b.FUEL = pyomo.Var(slc_idx, within=pyomo.NonNegativeReals, bounds=(0, 100000))
    b.parent_block().OUT.add(b.FUEL, 'FUEL_%s' % slc, network.Port.Extensive,
                             include_splitfrac=False)
m.fuel_src.subblocks = pyomo.Block(m.slices, rule=r_subblock_fuel_src)
# ==============================================================================


# ==============================================================================
# HEAT HUB:
# ---------
m.heat_hub = pyomo.Block()
m.heat_hub.E_heat = pyomo.Param(m.lc_set, initialize={
    _lc: E_heat[j] for j, _lc in enumerate(m.lc_set)})
m.heat_hub.IN = network.Port()
m.heat_hub.OUT = network.Port()
def r_subblock_heat_hub(b, slc):
    slc_idx = sorted(set(b.model().lc_set_slices[slc]))
    b.HEAT_IN = pyomo.Var(slc_idx, within=pyomo.NonNegativeReals, bounds=(0, 100000))
    b.HEAT_OUT = pyomo.Var(slc_idx, within=pyomo.NonNegativeReals, bounds=(0, 100000))
    b.parent_block().IN.add(b.HEAT_IN, 'HEAT_%s' % slc, network.Port.Extensive,
                            include_splitfrac=False)
    b.parent_block().OUT.add(b.HEAT_OUT, 'HEAT_%s' % slc, network.Port.Extensive,
                             include_splitfrac=False)
m.heat_hub.subblocks = pyomo.Block(m.slices, rule=r_subblock_heat_hub)

def r_heat_balance(comp, *t):
    HEAT_IN = comp.subblocks[t[1]].HEAT_IN
    HEAT_OUT = comp.subblocks[t[1]].HEAT_OUT
    return HEAT_IN[t] == HEAT_OUT[t] + comp.E_heat[t]
m.heat_hub.con_heat_balance = pyomo.Constraint(m.lc_set, rule=r_heat_balance)
# ==============================================================================


# ==============================================================================
# COLD SINK:
# ----------
m.cold_snk = pyomo.Block()
m.cold_snk.E_cold = pyomo.Param(m.lc_set, initialize={
    _lc: E_cold[j] for j, _lc in enumerate(m.lc_set)})
m.cold_snk.IN = network.Port()

def r_subblock_cold_snk(b, slc):
    slc_idx = sorted(set(b.model().lc_set_slices[slc]))
    b.COLD_IN = pyomo.Var(slc_idx, within=pyomo.NonNegativeReals)
    b.parent_block().IN.add(b.COLD_IN, 'COLD_%s' % slc, network.Port.Extensive,
                            include_splitfrac=False)
m.cold_snk.subblocks = pyomo.Block(m.slices, rule=r_subblock_cold_snk)

def r_cold_balance(comp, *t):
    return comp.subblocks[t[1]].COLD_IN[t] == comp.E_cold[t]
m.cold_snk.con_cold_balance = pyomo.Constraint(m.lc_set, rule=r_cold_balance)
# ==============================================================================


# ==============================================================================
# GAS BOILER:
# -----------
def create_gas_boiler(name):
    m.add_component(name, pyomo.Block())
    gb = m.find_component(name)
    gb.IN = network.Port()
    gb.OUT = network.Port()
    gb.SIZE_NOM = pyomo.Var(within=pyomo.NonNegativeReals, bounds=(
        comp_data['N_min'].loc[name], comp_data['N_max'].loc[name]))
    gb.INVEST = pyomo.Var(within=pyomo.NonNegativeReals, bounds=(0, 300000))
    gb.BI_EX = pyomo.Var(within=pyomo.Binary, initialize=1)

    def r_subblock_gas_boiler(b, slc):
        slc_idx = sorted(set(m.lc_set_slices[slc]))
        b.U = pyomo.Var(slc_idx, within=pyomo.NonNegativeReals, bounds=(0, 16000))
        b.U_IN = pyomo.Var(slc_idx, within=pyomo.NonNegativeReals, bounds=(0, 16000))
        b.V = pyomo.Var(slc_idx, within=pyomo.NonNegativeReals, bounds=(0, 14000))
        b.BI_OP = pyomo.Var(slc_idx, within=pyomo.Binary, initialize=1)
        b.parent_block().IN.add(b.U_IN, 'FUEL_%s' % slc, network.Port.Extensive,
                                include_splitfrac=False)
        b.parent_block().OUT.add(b.V, 'HEAT_%s' % slc, network.Port.Extensive,
                                 include_splitfrac=False)
    gb.subblocks = pyomo.Block(m.slices, rule=r_subblock_gas_boiler)

    # Add constraints:
    gb.con_couple_bi_op = pyomo.Constraint(m.lc_set, rule=rule_couple_bi_op)
    gb.con_limit = pyomo.Constraint(m.lc_set, rule=rule_limit_output)
    gb.con_min_load = pyomo.Constraint(m.lc_set, rule=rule_min_load)
    gb.con_couple_ex_op = pyomo.Constraint(m.lc_set, rule=rule_couple_ex_op)
    # gb.con_nom_min = pyomo.Constraint(rule=rule_nom_min)
    # gb.con_nom_max = pyomo.Constraint(rule=rule_nom_max)

    def rule_invest_gb(b):
        return b.INVEST == b.BI_EX * 1.85484 * (
                (11418.6 + 64.115 * b.SIZE_NOM ** 0.7978) * 1.046 * (
                    1.0917 - 1.1921e-6 * b.SIZE_NOM))
    gb.con_invest = pyomo.Constraint(rule=rule_invest_gb)

    def rule_perf_gb(b, *t):  # performance curve
        U = b.subblocks[t[1]].U
        V = b.subblocks[t[1]].V
        return U[t] == 1 / 0.9 * (0.1021 * V[t] ** 2 / b.SIZE_NOM
                                  + 0.8355 * V[t] + 0.0666 * b.SIZE_NOM)
    gb.con_perf = pyomo.Constraint(m.lc_set, rule=rule_perf_gb)

    def rule_perf_gb_2(b, *t):  # performance curve
        U = b.subblocks[t[1]].U
        U_IN = b.subblocks[t[1]].U_IN
        BI_OP = b.subblocks[t[1]].BI_OP
        return U_IN[t] == U[t] * BI_OP[t]
    gb.con_perf_2 = pyomo.Constraint(m.lc_set, rule=rule_perf_gb_2)

    # Add arcs:
    m.add_component('arc_fuel_src_%s' % name, network.Arc(
        src=m.fuel_src.OUT, dest=gb.IN))
    m.add_component('arc_%s_heat_hub' % name, network.Arc(
        src=gb.OUT, dest=m.heat_hub.IN))
# ==============================================================================


# ==============================================================================
# COMBINED HEAT AND POWER:
# ------------------------
def create_chp(name):
    m.add_component(name, pyomo.Block())
    chp = m.find_component(name)
    chp.IN = network.Port()
    chp.OUT_HEAT = network.Port()
    chp.OUT_ELEC = network.Port()
    chp.SIZE_NOM = pyomo.Var(within=pyomo.NonNegativeReals, bounds=(
        comp_data['N_min'].loc[name], comp_data['N_max'].loc[name]))
    chp.INVEST = pyomo.Var(within=pyomo.NonNegativeReals, bounds=(0, 830000))
    chp.BI_EX = pyomo.Var(within=pyomo.Binary, initialize=1)

    def r_subblock_chp(b, slc):
        slc_idx = sorted(set(m.lc_set_slices[slc]))
        b.U = pyomo.Var(slc_idx, within=pyomo.NonNegativeReals, bounds=(0, 8500))
        b.U_IN = pyomo.Var(slc_idx, within=pyomo.NonNegativeReals, bounds=(0, 8500))
        b.V = pyomo.Var(slc_idx, within=pyomo.NonNegativeReals, bounds=(0, 3200))
        b.V_EL = pyomo.Var(slc_idx, within=pyomo.NonNegativeReals, bounds=(0, 3800))
        b.V_EL_OUT = pyomo.Var(slc_idx, within=pyomo.NonNegativeReals, bounds=(0, 3800))
        b.BI_OP = pyomo.Var(slc_idx, within=pyomo.Binary, initialize=1)
        b.parent_block().IN.add(b.U_IN, 'FUEL_%s' % slc, network.Port.Extensive,
                                include_splitfrac=False)
        b.parent_block().OUT_HEAT.add(b.V, 'HEAT_%s' % slc, network.Port.Extensive,
                                      include_splitfrac=False)
        b.parent_block().OUT_ELEC.add(b.V_EL_OUT, 'ELEC_%s' % slc, network.Port.Extensive,
                                      include_splitfrac=False)
    chp.subblocks = pyomo.Block(m.slices, rule=r_subblock_chp)

    # Add constraints:
    chp.con_couple_bi_op = pyomo.Constraint(m.lc_set, rule=rule_couple_bi_op)
    chp.con_limit = pyomo.Constraint(m.lc_set, rule=rule_limit_output)
    chp.con_min_load = pyomo.Constraint(m.lc_set, rule=rule_min_load)
    chp.con_couple_ex_op = pyomo.Constraint(m.lc_set, rule=rule_couple_ex_op)
    # chp.con_nom_min = pyomo.Constraint(rule=rule_nom_min)
    # chp.con_nom_max = pyomo.Constraint(rule=rule_nom_max)

    def rule_invest_chp(b):
        eta_nom_th = 0.498 - 3.55e-5 * b.SIZE_NOM
        eta_nom_el = 0.87 - eta_nom_th
        return b.INVEST == b.BI_EX * 9332.6 * (b.SIZE_NOM * eta_nom_el / eta_nom_th)**0.539
    chp.con_invest = pyomo.Constraint(rule=rule_invest_chp)

    def rule_perf_chp_fuel(b, *t):
        U = b.subblocks[t[1]].U
        V = b.subblocks[t[1]].V
        return U[t] == 550.3 - 1328 * V[t] / b.SIZE_NOM - 0.4537 * b.SIZE_NOM \
            + 668.3 * (V[t] / b.SIZE_NOM)**2 + 2.649 * V[t] \
            + 9.571e-5 * b.SIZE_NOM**2
    chp.con_perf_fuel = pyomo.Constraint(m.lc_set, rule=rule_perf_chp_fuel)

    def rule_perf_chp_elec(b, *t):
        V_EL = b.subblocks[t[1]].V_EL
        V = b.subblocks[t[1]].V
        return V_EL[t] == 518.8 - 1203 * V[t] / b.SIZE_NOM \
            - 0.5361 * b.SIZE_NOM + 579.3 * (V[t] / b.SIZE_NOM)**2 \
            + 1.464 * V[t] + 7.728e-5 * b.SIZE_NOM**2
    chp.con_perf_elec = pyomo.Constraint(m.lc_set, rule=rule_perf_chp_elec)

    def rule_perf_chp_fuel_2(b, *t):
        U = b.subblocks[t[1]].U
        U_IN = b.subblocks[t[1]].U_IN
        BI_OP = b.subblocks[t[1]].BI_OP
        return U_IN[t] == U[t] * BI_OP[t]
    chp.con_perf_fuel_2 = pyomo.Constraint(m.lc_set, rule=rule_perf_chp_fuel_2)

    def rule_perf_chp_elec_2(b, *t):
        V_EL = b.subblocks[t[1]].V_EL
        V_EL_OUT = b.subblocks[t[1]].V_EL_OUT
        BI_OP = b.subblocks[t[1]].BI_OP
        return V_EL_OUT[t] == V_EL[t] * BI_OP[t]
    chp.con_perf_elec_2 = pyomo.Constraint(m.lc_set, rule=rule_perf_chp_elec_2)

    # Add arcs:
    m.add_component('arc_fuel_src_%s' % name, network.Arc(
        src=m.fuel_src.OUT, dest=chp.IN))
    m.add_component('arc_%s_heat_hub' % name, network.Arc(
        src=chp.OUT_HEAT, dest=m.heat_hub.IN))
    m.add_component('arc_%s_elec_hub' % name, network.Arc(
        src=chp.OUT_ELEC, dest=m.elec_hub.IN))
# ==============================================================================


# ==============================================================================
# TURBO CHILLER:
# ------------
def create_turbo_chiller(name):
    m.add_component(name, pyomo.Block())
    tc = m.find_component(name)
    tc.IN = network.Port()
    tc.OUT = network.Port()
    tc.SIZE_NOM = pyomo.Var(within=pyomo.NonNegativeReals, bounds=(
        comp_data['N_min'].loc[name], comp_data['N_max'].loc[name]))
    tc.INVEST = pyomo.Var(within=pyomo.NonNegativeReals, bounds=(0, 1550000))
    tc.BI_EX = pyomo.Var(within=pyomo.Binary, initialize=1)

    def r_subblock_turbo_chiller(b, slc):
        slc_idx = sorted(set(m.lc_set_slices[slc]))
        b.U = pyomo.Var(slc_idx, within=pyomo.NonNegativeReals, bounds=(0, 3000))
        b.U_IN = pyomo.Var(slc_idx, within=pyomo.NonNegativeReals, bounds=(0, 3000))
        b.V = pyomo.Var(slc_idx, within=pyomo.NonNegativeReals, bounds=(0, 10000))
        b.BI_OP = pyomo.Var(slc_idx, within=pyomo.Binary, initialize=1)
        b.parent_block().IN.add(b.U_IN, 'ELEC_%s' % slc, network.Port.Extensive,
                                include_splitfrac=False)
        b.parent_block().OUT.add(b.V, 'COLD_%s' % slc, network.Port.Extensive,
                                 include_splitfrac=False)
    tc.subblocks = pyomo.Block(m.slices, rule=r_subblock_turbo_chiller)

    # Add constraints:
    tc.con_couple_bi_op = pyomo.Constraint(m.lc_set, rule=rule_couple_bi_op)
    tc.con_limit = pyomo.Constraint(m.lc_set, rule=rule_limit_output)
    tc.con_min_load = pyomo.Constraint(m.lc_set, rule=rule_min_load)
    tc.con_couple_ex_op = pyomo.Constraint(m.lc_set, rule=rule_couple_ex_op)
    # tc.con_nom_min = pyomo.Constraint(rule=rule_nom_min)
    # tc.con_nom_max = pyomo.Constraint(rule=rule_nom_max)

    def rule_invest_tc(b):
        return b.INVEST == b.BI_EX * 0.8102 * b.SIZE_NOM * (
                179.63 + 4991.3436 * b.SIZE_NOM**-0.6794)
    tc.con_invest = pyomo.Constraint(rule=rule_invest_tc)

    def rule_perf_tc(b, *t):  # performance curve
        U = b.subblocks[t[1]].U
        V = b.subblocks[t[1]].V
        return U[t] == 1 / 5.54 * (0.8119 * V[t]**2 / b.SIZE_NOM
                                   - 0.1688 * V[t] + 0.3392 * b.SIZE_NOM)
    tc.con_perf = pyomo.Constraint(m.lc_set, rule=rule_perf_tc)

    def rule_perf_2(b, *t):
        U = b.subblocks[t[1]].U
        U_IN = b.subblocks[t[1]].U_IN
        BI_OP = b.subblocks[t[1]].BI_OP
        return U_IN[t] == U[t] * BI_OP[t]
    tc.con_perf_2 = pyomo.Constraint(m.lc_set, rule=rule_perf_2)

    # Add arcs:
    m.add_component('arc_elec_hub_%s' % name, network.Arc(
        src=m.elec_hub.OUT, dest=tc.IN))
    m.add_component('arc_%s_cold_snk' % name, network.Arc(
        src=tc.OUT, dest=m.cold_snk.IN))
# ==============================================================================


# ==============================================================================
# ABSORPTION CHILLER:
# -------------------
def create_absorption_chiller(name):
    m.add_component(name, pyomo.Block())
    ac = m.find_component(name)
    ac.IN = network.Port()
    ac.OUT = network.Port()
    ac.SIZE_NOM = pyomo.Var(within=pyomo.NonNegativeReals, bounds=(
        comp_data['N_min'].loc[name], comp_data['N_max'].loc[name]))
    ac.INVEST = pyomo.Var(within=pyomo.NonNegativeReals, bounds=(0, 410000))
    ac.BI_EX = pyomo.Var(within=pyomo.Binary, initialize=1)

    def r_subblock_absorption_chiller(b, slc):
        slc_idx = sorted(set(m.lc_set_slices[slc]))
        b.U = pyomo.Var(slc_idx, within=pyomo.NonNegativeReals, bounds=(0, 11000))
        b.U_IN = pyomo.Var(slc_idx, within=pyomo.NonNegativeReals, bounds=(0, 11000))
        b.V = pyomo.Var(slc_idx, within=pyomo.NonNegativeReals, bounds=(0, 6500))
        b.BI_OP = pyomo.Var(slc_idx, within=pyomo.Binary, initialize=1)
        b.parent_block().IN.add(b.U_IN, 'HEAT_%s' % slc, network.Port.Extensive,
                                include_splitfrac=False)
        b.parent_block().OUT.add(b.V, 'COLD_%s' % slc, network.Port.Extensive,
                                 include_splitfrac=False)

    ac.subblocks = pyomo.Block(m.slices, rule=r_subblock_absorption_chiller)

    # Add constraints:
    ac.con_couple_bi_op = pyomo.Constraint(m.lc_set, rule=rule_couple_bi_op)
    ac.con_limit = pyomo.Constraint(m.lc_set, rule=rule_limit_output)
    ac.con_min_load = pyomo.Constraint(m.lc_set, rule=rule_min_load)
    ac.con_couple_ex_op = pyomo.Constraint(m.lc_set, rule=rule_couple_ex_op)
    # ac.con_nom_min = pyomo.Constraint(rule=rule_nom_min)
    # ac.con_nom_max = pyomo.Constraint(rule=rule_nom_max)

    def rule_invest_ac(b):
        return b.INVEST == b.BI_EX * 0.50401 * 17554.18 * b.SIZE_NOM**0.4345
    ac.con_invest = pyomo.Constraint(rule=rule_invest_ac)

    def rule_perf_ac(b, *t):  # performance curve
        U = b.subblocks[t[1]].U
        V = b.subblocks[t[1]].V
        return U[t] == (1 / 0.67) * (0.8333 * V[t]**2 / b.SIZE_NOM
                                     - 0.0833 * V[t] + 0.25 * b.SIZE_NOM)
    ac.con_perf = pyomo.Constraint(m.lc_set, rule=rule_perf_ac)

    def rule_perf_ac_2(b, *t):
        U = b.subblocks[t[1]].U
        U_IN = b.subblocks[t[1]].U_IN
        BI_OP = b.subblocks[t[1]].BI_OP
        return U_IN[t] == U[t] * BI_OP[t]
    ac.con_perf_ac_2 = pyomo.Constraint(m.lc_set, rule=rule_perf_ac_2)

    # Add arcs:
    m.add_component('arc_heat_hub_%s' % name, network.Arc(
        src=m.heat_hub.OUT, dest=ac.IN))
    m.add_component('arc_%s_cold_snk' % name, network.Arc(
        src=ac.OUT, dest=m.cold_snk.IN))
# ==============================================================================


# ==============================================================================
# General constraint definitions:
def rule_couple_bi_op(b, *t):
    # Eq. 6: OUTPUT <= OP.BINARY * max.size
    max_size = comp_data['N_max'].loc[b.name]
    return b.subblocks[t[1]].V[t] <= b.subblocks[t[1]].BI_OP[t] * max_size

def rule_limit_output(b, *t):
    # Eq. 7: OUTPUT <= NOM.SIZE
    return b.subblocks[t[1]].V[t] <= b.SIZE_NOM

def rule_min_load(b, *t):
    # Eq. 8: OUTPUT >= min_load * NOM.SIZE - (1-OP.BINARY) * min_load * max.size
    min_load = comp_data['alpha_min'].loc[b.name]
    max_size = comp_data['N_max'].loc[b.name]
    return b.subblocks[t[1]].V[t] >= b.SIZE_NOM * min_load - (
            1 - b.subblocks[t[1]].BI_OP[t]) * min_load * max_size

def rule_couple_ex_op(b, *t):
    # Eq. 9: EXIST.BINARY >= OP.BINARY
    return b.BI_EX >= b.subblocks[t[1]].BI_OP[t]

# It is a bit different than in equation 5. I added the existence binary since
# I want the nominal size to be zero if it does not exist.
def rule_nom_min(b):
    # Eq. 5-1: NOM.SIZE >= min.size * EXIST.BINARY
    return b.SIZE_NOM >= comp_data['N_min'].loc[b.name]

def rule_nom_max(b):
    # Eq. 5-2: NOM.SIZE <= max.size * EXIST.BINARY
    return b.SIZE_NOM <= comp_data['N_max'].loc[b.name]
# ==============================================================================


# ==============================================================================
# Create components one by one...
for c_name in comp_data.index:
    if c_name.startswith('Boiler'):
        create_gas_boiler(c_name)
    elif c_name.startswith('TC'):
        create_turbo_chiller(c_name)
    elif c_name.startswith('AC'):
        create_absorption_chiller(c_name)
    elif c_name.startswith('CHP'):
        create_chp(c_name)
# ==============================================================================


# ==============================================================================
# Add symmetry breaks on existence binary variables and nom. size variables:
# This is not in the model description of DESSLib but it is useful!
def add_symmetry_break(comp_type, use_nom_size=True, use_exist_binary=True):
    if comp_type not in ['AC', 'TC', 'Boiler', 'CHP']:
        return
    m.add_component(comp_type + '_set', pyomo.Set(initialize=[
        c for c in comp_data.index if c.startswith(comp_type)], ordered=True))
    comp_set = m.find_component(comp_type + '_set')

    if use_nom_size:
        def r_sym_break_nom_size(_m, c):
            if c != comp_set.last():
                curr_comp = _m.find_component(c)
                next_comp = _m.find_component(comp_set.next(c))
                return curr_comp.SIZE_NOM >= next_comp.SIZE_NOM
            else:
                return pyomo.Constraint.Skip
        m.add_component('sym_break_nom_size_'+comp_type,
                        pyomo.Constraint(comp_set, rule=r_sym_break_nom_size))
    if use_exist_binary:
        def r_sym_break_exist_bi(_m, c):
            if c != comp_set.last():
                curr_comp = _m.find_component(c)
                next_comp = _m.find_component(comp_set.next(c))
                return curr_comp.BI_EX >= next_comp.BI_EX
            else:
                return pyomo.Constraint.Skip
        m.add_component('sym_break_exist_bi_'+comp_type,
                        pyomo.Constraint(comp_set, rule=r_sym_break_exist_bi))

for c_type in ['AC', 'TC', 'Boiler', 'CHP']:
    add_symmetry_break(c_type)
# ==============================================================================


# ==============================================================================
# OBJECTIVE FUNCTION:
# -------------------
def obj_rule(_m):
    # Electricity cost dictionary
    cf_elec = {key: 0 for key in _m.lc_set}  # init zeros
    for sb in _m.elec_hub.subblocks.values():
        for j in sb.ELEC_SELL:
            cf_elec[j] = sb.ELEC_SELL[j] * p_el_sell - sb.ELEC_BUY[j] * p_el_buy
    # Fuel cost dictionary
    cf_fuel = {key: 0 for key in _m.lc_set}  # init zeros
    for sb in _m.fuel_src.subblocks.values():
        for j in sb.FUEL:
            cf_fuel[j] = sb.FUEL[j] * p_gas_buy
    # Append investment and operation and maintenance cost
    cf_om, cf_invest = 0, 0
    for c in _m.component_objects(pyomo.Block, active=True):
        if hasattr(c, 'INVEST'):
            cf_om += c.INVEST * comp_data['m_s'].loc[c.name]
            cf_invest += c.INVEST

    # Return objective function
    return apvf * (sum(_m.part[_lc] * 8760 * (cf_elec[_lc] - cf_fuel[_lc])
                       for _lc in _m.lc_set) - cf_om) - cf_invest

m.obj = pyomo.Objective(rule=obj_rule, sense=pyomo.maximize)
# ==============================================================================


# ==============================================================================
# NETWORK:
# --------
# Model transformation: Expand the arcs
pyomo.TransformationFactory("network.expand_arcs").apply_to(m)

# Problem: Symmetry in results because the expanded variables have domain Reals!
for blk in m.component_objects(pyomo.Block, active=True):
    if blk.name.endswith('_expanded'):
        for v in blk.component_objects(pyomo.Var, active=True):
            v.domain = pyomo.NonNegativeReals
# ==============================================================================


# ==============================================================================
# SOLVE:
# ------
solver = pyomo.SolverFactory(solver_name)
if solver_name == 'scip':
    solver.options['limits/time'] = 300  # 'limits/gap=0.01'
elif solver_name == 'baron':
    solver.options['MaxTime'] = 43200  # 12 hours

file_name = 'DESS_model_{0}{1}_{2}_{3}.txt'.format(
    superstructure, load_case, data_instance, solver_name)
res = solver.solve(m, tee=False, logfile=file_name)

with open(file_name, 'a') as file:
    file.write('Lower bound: {0}\n'.format(res.problem.lower_bound))
    file.write('Upper bound: {0}\n'.format(res.problem.upper_bound))
file.close()


# ==============================================================================
