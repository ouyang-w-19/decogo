#  NLP written by GAMS Convert at 04/21/18 13:55:06
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         15       12        0        3        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         20       20        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         61       45       16        0
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

m.obj = Objective(expr=   m.x18 + m.x19, sense=minimize)

m.c2 = Constraint(expr= - m.x9 - m.x13 - m.x14 == -60)

m.c3 = Constraint(expr= - m.x10 - m.x15 - m.x16 == -20)

m.c4 = Constraint(expr= - m.x5 - m.x7 - m.x13 - m.x15 + m.x18 == 0)

m.c5 = Constraint(expr= - m.x6 - m.x8 - m.x14 - m.x16 + m.x19 == 0)

m.c6 = Constraint(expr= - m.x5 - m.x6 - m.x11 + m.x18 == 0)

m.c7 = Constraint(expr= - m.x7 - m.x8 - m.x12 + m.x19 == 0)

m.c8 = Constraint(expr= - m.x9 - m.x10 - m.x11 - m.x12 + m.x17 == 0)

m.c9 = Constraint(expr=m.x5*m.x3 + m.x7*m.x4 - m.x18*m.x1 + 400*m.x13 + 800*m.x15 == 0)

m.c10 = Constraint(expr=m.x6*m.x3 + m.x8*m.x4 - m.x19*m.x2 + 400*m.x14 + 800*m.x16 == 0)

m.c11 = Constraint(expr=   m.x1 <= 200)

m.c12 = Constraint(expr=   m.x2 <= 1000)

m.c13 = Constraint(expr= - 0.01*m.x1 + m.x3 == 0)

m.c14 = Constraint(expr= - 0.2*m.x2 + m.x4 == 0)

m.c15 = Constraint(expr=m.x11*m.x3 + m.x12*m.x4 + 400*m.x9 + 800*m.x10 - 10*m.x17 <= 0)
