#  MINLP written by GAMS Convert at 04/21/18 13:54:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          9        5        0        4        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        2        0        3        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         23       17        6        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(1,12),initialize=1)
m.i2 = Var(within=Integers,bounds=(1,12),initialize=1)
m.i3 = Var(within=Integers,bounds=(1,12),initialize=1)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   2*m.i1 + m.i2 + 1.4142135*m.i3, sense=minimize)

m.c1 = Constraint(expr=(-0.15*m.i1*m.i2) - 0.14142135*m.i2*m.i3 - 0.1319*m.i1*m.i3 + m.x4 == 0)

m.c2 = Constraint(expr=   1.7317*m.i2 + 1.03366*m.i3 - m.x4 <= 0)

m.c3 = Constraint(expr=   0.634*m.i1 + 2.828*m.i3 - m.x4 <= 0)

m.c4 = Constraint(expr=   0.5*m.i1 - 2*m.i2 - m.x4 <= 0)

m.c5 = Constraint(expr= - 0.5*m.i1 + 2*m.i2 - m.x4 <= 0)

m.c6 = Constraint(expr=(-1 + m.i1)*(-2 + m.i1)*(-3 + m.i1)*(-5 + m.i1)*(-8 + m.i1)*(-10 + m.i1)*(-12 + m.i1) == 0)

m.c7 = Constraint(expr=(-1 + m.i2)*(-2 + m.i2)*(-3 + m.i2)*(-5 + m.i2)*(-8 + m.i2)*(-10 + m.i2)*(-12 + m.i2) == 0)

m.c8 = Constraint(expr=(-1 + m.i3)*(-2 + m.i3)*(-3 + m.i3)*(-5 + m.i3)*(-8 + m.i3)*(-10 + m.i3)*(-12 + m.i3) == 0)
