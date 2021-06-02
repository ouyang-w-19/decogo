#  NLP written by GAMS Convert at 04/21/18 13:54:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          7        1        6        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        5        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         19       15        4        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=0.25*m.x1*m.x1 - m.x1 + 0.25*m.x2*m.x2 - m.x2 + 0.25*m.x3*m.x3 - m.x3 + 0.25*m.x4*m.x4 - m.x4
                       , sense=minimize)

m.c1 = Constraint(expr=   m.x1 + m.x2 >= 1)

m.c2 = Constraint(expr=   2*m.x3 + 2*m.x4 >= 4)

m.c3 = Constraint(expr=   m.x1 + m.x3 >= 3)

m.c4 = Constraint(expr=   m.x2 + m.x4 >= 4)

m.c5 = Constraint(expr= - m.x2 - 2*m.x3 - 3*m.x4 >= -8)

m.c6 = Constraint(expr= - 3*m.x2 - m.x3 - 2*m.x4 >= -10)
