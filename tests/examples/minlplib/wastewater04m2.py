#  NLP written by GAMS Convert at 04/21/18 13:55:06
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         66       60        0        6        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         56       56        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        212      176       36        0
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
m.x42 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,1000000),initialize=0)

m.obj = Objective(expr=   m.x14 + m.x15, sense=minimize)

m.c2 = Constraint(expr= - m.x5 - m.x9 - m.x10 == -40)

m.c3 = Constraint(expr= - m.x6 - m.x11 - m.x12 == -40)

m.c4 = Constraint(expr= - m.x1 - m.x3 - m.x9 - m.x11 + m.x14 == 0)

m.c5 = Constraint(expr= - m.x2 - m.x4 - m.x10 - m.x12 + m.x15 == 0)

m.c6 = Constraint(expr= - m.x1 - m.x2 - m.x7 + m.x14 == 0)

m.c7 = Constraint(expr= - m.x3 - m.x4 - m.x8 + m.x15 == 0)

m.c8 = Constraint(expr= - m.x5 - m.x6 - m.x7 - m.x8 + m.x13 == 0)

m.c9 = Constraint(expr= - m.x24 - m.x32 - m.x34 == -4000)

m.c10 = Constraint(expr= - m.x25 - m.x33 - m.x35 == -800)

m.c11 = Constraint(expr= - m.x26 - m.x36 - m.x38 == -600)

m.c12 = Constraint(expr= - m.x27 - m.x37 - m.x39 == -8000)

m.c13 = Constraint(expr= - m.x32 + 4000*m.x52 == 0)

m.c14 = Constraint(expr= - m.x33 + 800*m.x52 == 0)

m.c15 = Constraint(expr= - m.x34 + 4000*m.x53 == 0)

m.c16 = Constraint(expr= - m.x35 + 800*m.x53 == 0)

m.c17 = Constraint(expr= - m.x36 + 600*m.x54 == 0)

m.c18 = Constraint(expr= - m.x37 + 8000*m.x54 == 0)

m.c19 = Constraint(expr= - m.x38 + 600*m.x55 == 0)

m.c20 = Constraint(expr= - m.x39 + 8000*m.x55 == 0)

m.c21 = Constraint(expr= - m.x24 + 4000*m.x48 == 0)

m.c22 = Constraint(expr= - m.x25 + 800*m.x48 == 0)

m.c23 = Constraint(expr= - m.x26 + 600*m.x49 == 0)

m.c24 = Constraint(expr= - m.x27 + 8000*m.x49 == 0)

m.c25 = Constraint(expr= - m.x9 + 40*m.x52 == 0)

m.c26 = Constraint(expr= - m.x10 + 40*m.x53 == 0)

m.c27 = Constraint(expr= - m.x11 + 40*m.x54 == 0)

m.c28 = Constraint(expr= - m.x12 + 40*m.x55 == 0)

m.c29 = Constraint(expr= - m.x5 + 40*m.x48 == 0)

m.c30 = Constraint(expr= - m.x6 + 40*m.x49 == 0)

m.c31 = Constraint(expr=   m.x48 + m.x52 + m.x53 == 1)

m.c32 = Constraint(expr=   m.x49 + m.x54 + m.x55 == 1)

m.c33 = Constraint(expr= - 200*m.x14 + m.x16 + m.x20 + m.x32 + m.x36 <= 0)

m.c34 = Constraint(expr= - 200*m.x14 + m.x17 + m.x21 + m.x33 + m.x37 <= 0)

m.c35 = Constraint(expr= - 200*m.x15 + m.x18 + m.x22 + m.x34 + m.x38 <= 0)

m.c36 = Constraint(expr= - 200*m.x15 + m.x19 + m.x23 + m.x35 + m.x39 <= 0)

m.c37 = Constraint(expr=   0.05*m.x16 + 0.05*m.x20 + 0.05*m.x32 + 0.05*m.x36 - m.x40 == 0)

m.c38 = Constraint(expr=   m.x17 + m.x21 + m.x33 + m.x37 - m.x41 == 0)

m.c39 = Constraint(expr=   m.x18 + m.x22 + m.x34 + m.x38 - m.x42 == 0)

m.c40 = Constraint(expr=   0.024*m.x19 + 0.024*m.x23 + 0.024*m.x35 + 0.024*m.x39 - m.x43 == 0)

m.c41 = Constraint(expr= - m.x16 - m.x18 - m.x28 + m.x40 == 0)

m.c42 = Constraint(expr= - m.x17 - m.x19 - m.x29 + m.x41 == 0)

m.c43 = Constraint(expr= - m.x20 - m.x22 - m.x30 + m.x42 == 0)

m.c44 = Constraint(expr= - m.x21 - m.x23 - m.x31 + m.x43 == 0)

m.c45 = Constraint(expr=m.x40*m.x44 - m.x16 == 0)

m.c46 = Constraint(expr=m.x41*m.x44 - m.x17 == 0)

m.c47 = Constraint(expr=m.x40*m.x45 - m.x18 == 0)

m.c48 = Constraint(expr=m.x41*m.x45 - m.x19 == 0)

m.c49 = Constraint(expr=m.x42*m.x46 - m.x20 == 0)

m.c50 = Constraint(expr=m.x43*m.x46 - m.x21 == 0)

m.c51 = Constraint(expr=m.x42*m.x47 - m.x22 == 0)

m.c52 = Constraint(expr=m.x43*m.x47 - m.x23 == 0)

m.c53 = Constraint(expr=m.x40*m.x50 - m.x28 == 0)

m.c54 = Constraint(expr=m.x41*m.x50 - m.x29 == 0)

m.c55 = Constraint(expr=m.x42*m.x51 - m.x30 == 0)

m.c56 = Constraint(expr=m.x43*m.x51 - m.x31 == 0)

m.c57 = Constraint(expr=m.x14*m.x44 - m.x1 == 0)

m.c58 = Constraint(expr=m.x14*m.x45 - m.x2 == 0)

m.c59 = Constraint(expr=m.x15*m.x46 - m.x3 == 0)

m.c60 = Constraint(expr=m.x15*m.x47 - m.x4 == 0)

m.c61 = Constraint(expr=m.x14*m.x50 - m.x7 == 0)

m.c62 = Constraint(expr=m.x15*m.x51 - m.x8 == 0)

m.c63 = Constraint(expr=   m.x44 + m.x45 + m.x50 == 1)

m.c64 = Constraint(expr=   m.x46 + m.x47 + m.x51 == 1)

m.c65 = Constraint(expr= - 10*m.x13 + m.x24 + m.x26 + m.x28 + m.x30 <= 0)

m.c66 = Constraint(expr= - 10*m.x13 + m.x25 + m.x27 + m.x29 + m.x31 <= 0)
