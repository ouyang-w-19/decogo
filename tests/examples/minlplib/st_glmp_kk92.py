#  NLP written by GAMS Convert at 04/21/18 13:54:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          9        3        0        6        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        5        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         21       19        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(-3,1),initialize=0)
m.x2 = Var(within=Reals,bounds=(-3,4),initialize=0)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x4*m.x5, sense=minimize)

m.c1 = Constraint(expr= - 4*m.x1 + m.x2 <= 12)

m.c2 = Constraint(expr= - 4*m.x1 - 2*m.x2 <= 12)

m.c3 = Constraint(expr=   m.x1 - 2*m.x2 <= 6)

m.c4 = Constraint(expr=   m.x1 - m.x2 <= 3)

m.c5 = Constraint(expr=   m.x1 + m.x2 <= 2)

m.c6 = Constraint(expr=   2*m.x1 + m.x2 <= 2)

m.c8 = Constraint(expr=   m.x1 + m.x2 - m.x4 == 0)

m.c9 = Constraint(expr=   m.x1 - m.x2 - m.x5 == 0)
