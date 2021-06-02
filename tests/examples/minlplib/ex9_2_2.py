#  NLP written by GAMS Convert at 04/21/18 13:51:48
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         12        9        0        3        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         11       11        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         27       17       10        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,20),initialize=0)

m.obj = Objective(expr=m.x2*m.x2 + (-10 + m.x3)*(-10 + m.x3), sense=minimize)

m.c2 = Constraint(expr=   m.x2 <= 15)

m.c3 = Constraint(expr= - m.x2 + m.x3 <= 0)

m.c4 = Constraint(expr= - m.x2 <= 0)

m.c5 = Constraint(expr=   m.x2 + m.x3 + m.x4 == 20)

m.c6 = Constraint(expr= - m.x3 + m.x5 == 0)

m.c7 = Constraint(expr=   m.x3 + m.x6 == 20)

m.c8 = Constraint(expr=m.x4*m.x8 == 0)

m.c9 = Constraint(expr=m.x5*m.x9 == 0)

m.c10 = Constraint(expr=m.x6*m.x10 == 0)

m.c11 = Constraint(expr=m.x7*m.x11 == 0)

m.c12 = Constraint(expr=   2*m.x2 + 4*m.x3 + m.x8 - m.x9 + m.x10 == 60)
