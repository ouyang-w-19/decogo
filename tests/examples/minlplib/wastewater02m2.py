#  NLP written by GAMS Convert at 04/21/18 13:55:06
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         45       42        0        3        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         42       42        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        143      119       24        0
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
m.x24 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,1000000),initialize=0)

m.obj = Objective(expr=   m.x14 + m.x15, sense=minimize)

m.c2 = Constraint(expr= - m.x5 - m.x9 - m.x10 == -60)

m.c3 = Constraint(expr= - m.x6 - m.x11 - m.x12 == -20)

m.c4 = Constraint(expr= - m.x1 - m.x3 - m.x9 - m.x11 + m.x14 == 0)

m.c5 = Constraint(expr= - m.x2 - m.x4 - m.x10 - m.x12 + m.x15 == 0)

m.c6 = Constraint(expr= - m.x1 - m.x2 - m.x7 + m.x14 == 0)

m.c7 = Constraint(expr= - m.x3 - m.x4 - m.x8 + m.x15 == 0)

m.c8 = Constraint(expr= - m.x5 - m.x6 - m.x7 - m.x8 + m.x13 == 0)

m.c9 = Constraint(expr= - m.x20 - m.x24 - m.x25 == -24000)

m.c10 = Constraint(expr= - m.x21 - m.x26 - m.x27 == -16000)

m.c11 = Constraint(expr= - m.x24 + 24000*m.x38 == 0)

m.c12 = Constraint(expr= - m.x25 + 24000*m.x39 == 0)

m.c13 = Constraint(expr= - m.x26 + 16000*m.x40 == 0)

m.c14 = Constraint(expr= - m.x27 + 16000*m.x41 == 0)

m.c15 = Constraint(expr= - m.x20 + 24000*m.x34 == 0)

m.c16 = Constraint(expr= - m.x21 + 16000*m.x35 == 0)

m.c17 = Constraint(expr= - m.x9 + 60*m.x38 == 0)

m.c18 = Constraint(expr= - m.x10 + 60*m.x39 == 0)

m.c19 = Constraint(expr= - m.x11 + 20*m.x40 == 0)

m.c20 = Constraint(expr= - m.x12 + 20*m.x41 == 0)

m.c21 = Constraint(expr= - m.x5 + 60*m.x34 == 0)

m.c22 = Constraint(expr= - m.x6 + 20*m.x35 == 0)

m.c23 = Constraint(expr=   m.x34 + m.x38 + m.x39 == 1)

m.c24 = Constraint(expr=   m.x35 + m.x40 + m.x41 == 1)

m.c25 = Constraint(expr= - 200*m.x14 + m.x16 + m.x18 + m.x24 + m.x26 <= 0)

m.c26 = Constraint(expr= - 1000*m.x15 + m.x17 + m.x19 + m.x25 + m.x27 <= 0)

m.c27 = Constraint(expr=   0.01*m.x16 + 0.01*m.x18 + 0.01*m.x24 + 0.01*m.x26 - m.x28 == 0)

m.c28 = Constraint(expr=   0.2*m.x17 + 0.2*m.x19 + 0.2*m.x25 + 0.2*m.x27 - m.x29 == 0)

m.c29 = Constraint(expr= - m.x16 - m.x17 - m.x22 + m.x28 == 0)

m.c30 = Constraint(expr= - m.x18 - m.x19 - m.x23 + m.x29 == 0)

m.c31 = Constraint(expr=m.x28*m.x30 - m.x16 == 0)

m.c32 = Constraint(expr=m.x28*m.x31 - m.x17 == 0)

m.c33 = Constraint(expr=m.x29*m.x32 - m.x18 == 0)

m.c34 = Constraint(expr=m.x29*m.x33 - m.x19 == 0)

m.c35 = Constraint(expr=m.x28*m.x36 - m.x22 == 0)

m.c36 = Constraint(expr=m.x29*m.x37 - m.x23 == 0)

m.c37 = Constraint(expr=m.x14*m.x30 - m.x1 == 0)

m.c38 = Constraint(expr=m.x14*m.x31 - m.x2 == 0)

m.c39 = Constraint(expr=m.x15*m.x32 - m.x3 == 0)

m.c40 = Constraint(expr=m.x15*m.x33 - m.x4 == 0)

m.c41 = Constraint(expr=m.x14*m.x36 - m.x7 == 0)

m.c42 = Constraint(expr=m.x15*m.x37 - m.x8 == 0)

m.c43 = Constraint(expr=   m.x30 + m.x31 + m.x36 == 1)

m.c44 = Constraint(expr=   m.x32 + m.x33 + m.x37 == 1)

m.c45 = Constraint(expr= - 10*m.x13 + m.x20 + m.x21 + m.x22 + m.x23 <= 0)
