#  NLP written by GAMS Convert at 04/21/18 13:54:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         10        1        0        9        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          4        4        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         28       26        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=15*m.x1 - m.x1**2 - m.x2**2 - 2*m.x2 + m.x3, sense=minimize)

m.c1 = Constraint(expr= - 4*m.x1 - 3*m.x2 + 4*m.x3 <= 30)

m.c2 = Constraint(expr=   4*m.x1 + 9*m.x2 - 2*m.x3 <= 114)

m.c3 = Constraint(expr=   2*m.x2 - m.x3 <= 8)

m.c4 = Constraint(expr=   2*m.x1 + 15*m.x2 - 8*m.x3 <= 64)

m.c5 = Constraint(expr=   m.x2 <= 14)

m.c6 = Constraint(expr= - 4*m.x1 + 3*m.x2 - 2*m.x3 <= -18)

m.c7 = Constraint(expr=   4*m.x1 - 9*m.x2 + 4*m.x3 <= -6)

m.c8 = Constraint(expr= - 6*m.x1 + 5*m.x2 - 4*m.x3 <= -40)

m.c9 = Constraint(expr=   4*m.x1 - 9*m.x2 - 3*m.x3 <= -132)
