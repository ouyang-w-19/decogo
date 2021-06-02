#  NLP written by GAMS Convert at 04/21/18 13:54:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          5        1        3        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        5        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         13        9        4        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,27),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,16),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,10),initialize=0)

m.obj = Objective(expr=m.x1*m.x3 + m.x2*m.x4, sense=minimize)

m.c1 = Constraint(expr=   m.x1 + 3*m.x2 >= 30)

m.c2 = Constraint(expr=   2*m.x1 + m.x2 >= 20)

m.c3 = Constraint(expr= - 1.6667*m.x3 + m.x4 >= 10)

m.c4 = Constraint(expr=   m.x3 + m.x4 <= 15)
