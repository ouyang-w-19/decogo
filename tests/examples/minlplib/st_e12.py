#  NLP written by GAMS Convert at 04/21/18 13:54:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          4        2        0        2        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        5        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         12       10        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)

m.obj = Objective(expr=m.x1**0.6 + m.x2**0.6 - 6*m.x1 - 4*m.x3 + 3*m.x4, sense=minimize)

m.c1 = Constraint(expr= - 3*m.x1 + m.x2 - 3*m.x3 == 0)

m.c2 = Constraint(expr=   m.x1 + 2*m.x3 <= 4)

m.c3 = Constraint(expr=   m.x2 + 2*m.x4 <= 4)
