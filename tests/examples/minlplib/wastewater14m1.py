#  NLP written by GAMS Convert at 04/21/18 13:55:06
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         47       35        0       12        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         75       75        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        321      181      140        0
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
m.x56 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,1000000),initialize=0)

m.obj = Objective(expr=   m.x70 + m.x71 + m.x72 + m.x73 + m.x74, sense=minimize)

m.c2 = Constraint(expr= - m.x46 - m.x54 - m.x55 - m.x56 - m.x57 - m.x58 == -50)

m.c3 = Constraint(expr= - m.x47 - m.x59 - m.x60 - m.x61 - m.x62 - m.x63 == -120)

m.c4 = Constraint(expr= - m.x48 - m.x64 - m.x65 - m.x66 - m.x67 - m.x68 == -70)

m.c5 = Constraint(expr= - m.x21 - m.x26 - m.x31 - m.x36 - m.x41 - m.x54 - m.x59 - m.x64 + m.x70 == 0)

m.c6 = Constraint(expr= - m.x22 - m.x27 - m.x32 - m.x37 - m.x42 - m.x55 - m.x60 - m.x65 + m.x71 == 0)

m.c7 = Constraint(expr= - m.x23 - m.x28 - m.x33 - m.x38 - m.x43 - m.x56 - m.x61 - m.x66 + m.x72 == 0)

m.c8 = Constraint(expr= - m.x24 - m.x29 - m.x34 - m.x39 - m.x44 - m.x57 - m.x62 - m.x67 + m.x73 == 0)

m.c9 = Constraint(expr= - m.x25 - m.x30 - m.x35 - m.x40 - m.x45 - m.x58 - m.x63 - m.x68 + m.x74 == 0)

m.c10 = Constraint(expr= - m.x21 - m.x22 - m.x23 - m.x24 - m.x25 - m.x49 + m.x70 == 0)

m.c11 = Constraint(expr= - m.x26 - m.x27 - m.x28 - m.x29 - m.x30 - m.x50 + m.x71 == 0)

m.c12 = Constraint(expr= - m.x31 - m.x32 - m.x33 - m.x34 - m.x35 - m.x51 + m.x72 == 0)

m.c13 = Constraint(expr= - m.x36 - m.x37 - m.x38 - m.x39 - m.x40 - m.x52 + m.x73 == 0)

m.c14 = Constraint(expr= - m.x41 - m.x42 - m.x43 - m.x44 - m.x45 - m.x53 + m.x74 == 0)

m.c15 = Constraint(expr= - m.x46 - m.x47 - m.x48 - m.x49 - m.x50 - m.x51 - m.x52 - m.x53 + m.x69 == 0)

m.c16 = Constraint(expr=m.x21*m.x11 + m.x26*m.x13 + m.x31*m.x15 + m.x36*m.x17 + m.x41*m.x19 - m.x70*m.x1 + 10*m.x54
                         + 110*m.x59 + 100*m.x64 == 0)

m.c17 = Constraint(expr=m.x21*m.x12 + m.x26*m.x14 + m.x31*m.x16 + m.x36*m.x18 + m.x41*m.x20 - m.x70*m.x2 + 200*m.x54
                         + 140*m.x59 + 25*m.x64 == 0)

m.c18 = Constraint(expr=m.x22*m.x11 + m.x27*m.x13 + m.x32*m.x15 + m.x37*m.x17 + m.x42*m.x19 - m.x71*m.x3 + 10*m.x55
                         + 110*m.x60 + 100*m.x65 == 0)

m.c19 = Constraint(expr=m.x22*m.x12 + m.x27*m.x14 + m.x32*m.x16 + m.x37*m.x18 + m.x42*m.x20 - m.x71*m.x4 + 200*m.x55
                         + 140*m.x60 + 25*m.x65 == 0)

m.c20 = Constraint(expr=m.x23*m.x11 + m.x28*m.x13 + m.x33*m.x15 + m.x38*m.x17 + m.x43*m.x19 - m.x72*m.x5 + 10*m.x56
                         + 110*m.x61 + 100*m.x66 == 0)

m.c21 = Constraint(expr=m.x23*m.x12 + m.x28*m.x14 + m.x33*m.x16 + m.x38*m.x18 + m.x43*m.x20 - m.x72*m.x6 + 200*m.x56
                         + 140*m.x61 + 25*m.x66 == 0)

m.c22 = Constraint(expr=m.x24*m.x11 + m.x29*m.x13 + m.x34*m.x15 + m.x39*m.x17 + m.x44*m.x19 - m.x73*m.x7 + 10*m.x57
                         + 110*m.x62 + 100*m.x67 == 0)

m.c23 = Constraint(expr=m.x24*m.x12 + m.x29*m.x14 + m.x34*m.x16 + m.x39*m.x18 + m.x44*m.x20 - m.x73*m.x8 + 200*m.x57
                         + 140*m.x62 + 25*m.x67 == 0)

m.c24 = Constraint(expr=m.x25*m.x11 + m.x30*m.x13 + m.x35*m.x15 + m.x40*m.x17 + m.x45*m.x19 - m.x74*m.x9 + 10*m.x58
                         + 110*m.x63 + 100*m.x68 == 0)

m.c25 = Constraint(expr=m.x25*m.x12 + m.x30*m.x14 + m.x35*m.x16 + m.x40*m.x18 + m.x45*m.x20 - m.x74*m.x10 + 200*m.x58
                         + 140*m.x63 + 25*m.x68 == 0)

m.c26 = Constraint(expr=   m.x1 <= 145)

m.c27 = Constraint(expr=   m.x2 <= 400)

m.c28 = Constraint(expr=   m.x3 <= 110)

m.c29 = Constraint(expr=   m.x4 <= 90)

m.c30 = Constraint(expr=   m.x5 <= 90)

m.c31 = Constraint(expr=   m.x6 <= 100)

m.c32 = Constraint(expr=   m.x7 <= 200)

m.c33 = Constraint(expr=   m.x8 <= 90)

m.c34 = Constraint(expr=   m.x9 <= 50)

m.c35 = Constraint(expr=   m.x10 <= 80)

m.c36 = Constraint(expr= - 0.1*m.x1 + m.x11 == 0)

m.c37 = Constraint(expr= - m.x2 + m.x12 == 0)

m.c38 = Constraint(expr= - 0.3*m.x3 + m.x13 == 0)

m.c39 = Constraint(expr= - 0.1*m.x4 + m.x14 == 0)

m.c40 = Constraint(expr= - m.x5 + m.x15 == 0)

m.c41 = Constraint(expr= - 0.2*m.x6 + m.x16 == 0)

m.c42 = Constraint(expr= - 0.5*m.x7 + m.x17 == 0)

m.c43 = Constraint(expr= - m.x8 + m.x18 == 0)

m.c44 = Constraint(expr= - 0.35*m.x9 + m.x19 == 0)

m.c45 = Constraint(expr= - 0.4*m.x10 + m.x20 == 0)

m.c46 = Constraint(expr=m.x49*m.x11 + m.x50*m.x13 + m.x51*m.x15 + m.x52*m.x17 + m.x53*m.x19 + 10*m.x46 + 110*m.x47
                         + 100*m.x48 - 10*m.x69 <= 0)

m.c47 = Constraint(expr=m.x49*m.x12 + m.x50*m.x14 + m.x51*m.x16 + m.x52*m.x18 + m.x53*m.x20 + 200*m.x46 + 140*m.x47
                         + 25*m.x48 - 5*m.x69 <= 0)
