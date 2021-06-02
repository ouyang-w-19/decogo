#  NLP written by GAMS Convert at 04/21/18 13:54:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          6        1        0        5        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          4        4        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         19       16        3        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=2*m.x1 - m.x1**2 - m.x2**2 - m.x3**2 + 2*m.x3, sense=minimize)

m.c1 = Constraint(expr=   m.x1 + m.x2 - m.x3 <= 1)

m.c2 = Constraint(expr= - m.x1 + m.x2 - m.x3 <= -1)

m.c3 = Constraint(expr=   12*m.x1 + 5*m.x2 + 12*m.x3 <= 34.8)

m.c4 = Constraint(expr=   12*m.x1 + 12*m.x2 + 7*m.x3 <= 29.1)

m.c5 = Constraint(expr= - 6*m.x1 + m.x2 + m.x3 <= -4.1)
