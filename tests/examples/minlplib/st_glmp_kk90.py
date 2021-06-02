#  NLP written by GAMS Convert at 04/21/18 13:54:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          8        4        1        3        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          6        6        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         20       18        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x2 = Var(within=Reals,bounds=(3,6),initialize=3)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x4*m.x5 + m.x3, sense=minimize)

m.c1 = Constraint(expr=   2*m.x1 + 3*m.x2 >= 9)

m.c2 = Constraint(expr=   3*m.x1 - m.x2 <= 8)

m.c3 = Constraint(expr= - m.x1 + 2*m.x2 <= 8)

m.c4 = Constraint(expr=   m.x1 + 2*m.x2 <= 12)

m.c6 = Constraint(expr=   m.x1 - m.x3 == 0)

m.c7 = Constraint(expr=   m.x1 - m.x2 - m.x4 == -5)

m.c8 = Constraint(expr=   m.x1 + m.x2 - m.x5 == 1)
