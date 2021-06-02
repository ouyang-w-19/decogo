#  NLP written by GAMS Convert at 04/21/18 13:55:06
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         22       16        0        6        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         24       24        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         90       58       32        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,1000000),initialize=0)

m.obj = Objective(expr=   m.x22 + m.x23, sense=minimize)

m.c2 = Constraint(expr= - m.x13 - m.x17 - m.x18 == -40)

m.c3 = Constraint(expr= - m.x14 - m.x19 - m.x20 == -40)

m.c4 = Constraint(expr= - m.x9 - m.x11 - m.x17 - m.x19 + m.x22 == 0)

m.c5 = Constraint(expr= - m.x10 - m.x12 - m.x18 - m.x20 + m.x23 == 0)

m.c6 = Constraint(expr= - m.x9 - m.x10 - m.x15 + m.x22 == 0)

m.c7 = Constraint(expr= - m.x11 - m.x12 - m.x16 + m.x23 == 0)

m.c8 = Constraint(expr= - m.x13 - m.x14 - m.x15 - m.x16 + m.x21 == 0)

m.c9 = Constraint(expr=m.x9*m.x5 + m.x11*m.x7 - m.x22*m.x1 + 100*m.x17 + 15*m.x19 == 0)

m.c10 = Constraint(expr=m.x9*m.x6 + m.x11*m.x8 - m.x22*m.x2 + 20*m.x17 + 200*m.x19 == 0)

m.c11 = Constraint(expr=m.x10*m.x5 + m.x12*m.x7 - m.x23*m.x3 + 100*m.x18 + 15*m.x20 == 0)

m.c12 = Constraint(expr=m.x10*m.x6 + m.x12*m.x8 - m.x23*m.x4 + 20*m.x18 + 200*m.x20 == 0)

m.c13 = Constraint(expr=   m.x1 <= 200)

m.c14 = Constraint(expr=   m.x2 <= 200)

m.c15 = Constraint(expr=   m.x3 <= 200)

m.c16 = Constraint(expr=   m.x4 <= 200)

m.c17 = Constraint(expr= - 0.05*m.x1 + m.x5 == 0)

m.c18 = Constraint(expr= - m.x2 + m.x6 == 0)

m.c19 = Constraint(expr= - m.x3 + m.x7 == 0)

m.c20 = Constraint(expr= - 0.024*m.x4 + m.x8 == 0)

m.c21 = Constraint(expr=m.x15*m.x5 + m.x16*m.x7 + 100*m.x13 + 15*m.x14 - 10*m.x21 <= 0)

m.c22 = Constraint(expr=m.x15*m.x6 + m.x16*m.x8 + 20*m.x13 + 200*m.x14 - 10*m.x21 <= 0)
