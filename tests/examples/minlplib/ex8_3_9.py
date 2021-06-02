#  NLP written by GAMS Convert at 04/21/18 13:51:47
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         46       46        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         79       79        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        327      113      214        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x3 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x4 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x5 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x6 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x7 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x8 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x9 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x10 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x11 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x12 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x13 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x14 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x15 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x16 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x17 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x18 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x19 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x20 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x21 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x22 = Var(within=Reals,bounds=(0,1000),initialize=100)
m.x23 = Var(within=Reals,bounds=(0,1000),initialize=100)
m.x24 = Var(within=Reals,bounds=(0,1000),initialize=100)
m.x25 = Var(within=Reals,bounds=(0,1000),initialize=100)
m.x26 = Var(within=Reals,bounds=(0,1000),initialize=100)
m.x27 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x28 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x29 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x30 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x31 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x32 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x33 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x34 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x35 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x36 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x37 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x38 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x39 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x40 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x41 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x42 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x43 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x44 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x45 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x46 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x47 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x48 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x49 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x50 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x51 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x52 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x53 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x54 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x55 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x56 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x57 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x58 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x59 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x60 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x61 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x62 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x63 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x64 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x65 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x66 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x67 = Var(within=Reals,bounds=(0,1000),initialize=100)
m.x68 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x69 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x70 = Var(within=Reals,bounds=(0,10000),initialize=1)
m.x71 = Var(within=Reals,bounds=(0,10000),initialize=1)
m.x72 = Var(within=Reals,bounds=(0,10000),initialize=1)
m.x73 = Var(within=Reals,bounds=(0,10000),initialize=1)
m.x74 = Var(within=Reals,bounds=(0,10000),initialize=1)
m.x75 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,10000),initialize=0)

m.obj = Objective(expr= - m.x69, sense=minimize)

m.c2 = Constraint(expr= - m.x2 - m.x3 - m.x4 - m.x5 - m.x6 == -100)

m.c3 = Constraint(expr= - m.x2 + m.x7 - m.x37 - m.x42 - m.x47 - m.x52 - m.x57 == 0)

m.c4 = Constraint(expr= - m.x3 + m.x8 - m.x38 - m.x43 - m.x48 - m.x53 - m.x58 == 0)

m.c5 = Constraint(expr= - m.x4 + m.x9 - m.x39 - m.x44 - m.x49 - m.x54 - m.x59 == 0)

m.c6 = Constraint(expr= - m.x5 + m.x10 - m.x40 - m.x45 - m.x50 - m.x55 - m.x60 == 0)

m.c7 = Constraint(expr= - m.x6 + m.x11 - m.x41 - m.x46 - m.x51 - m.x56 - m.x61 == 0)

m.c8 = Constraint(expr=m.x12*m.x7 - (m.x27*m.x37 + m.x29*m.x42 + m.x31*m.x47 + m.x33*m.x52 + m.x35*m.x57) - 0.45*m.x2
                        == 0)

m.c9 = Constraint(expr=m.x13*m.x7 - (m.x28*m.x37 + m.x30*m.x42 + m.x32*m.x47 + m.x34*m.x52 + m.x36*m.x57) - 0.55*m.x2
                        == 0)

m.c10 = Constraint(expr=m.x14*m.x8 - (m.x27*m.x38 + m.x29*m.x43 + m.x31*m.x48 + m.x33*m.x53 + m.x35*m.x58) - 0.45*m.x3
                         == 0)

m.c11 = Constraint(expr=m.x15*m.x8 - (m.x28*m.x38 + m.x30*m.x43 + m.x32*m.x48 + m.x34*m.x53 + m.x36*m.x58) - 0.55*m.x3
                         == 0)

m.c12 = Constraint(expr=m.x16*m.x9 - (m.x27*m.x39 + m.x29*m.x44 + m.x31*m.x49 + m.x33*m.x54 + m.x35*m.x59) - 0.45*m.x4
                         == 0)

m.c13 = Constraint(expr=m.x17*m.x9 - (m.x28*m.x39 + m.x30*m.x44 + m.x32*m.x49 + m.x34*m.x54 + m.x36*m.x59) - 0.55*m.x4
                         == 0)

m.c14 = Constraint(expr=m.x18*m.x10 - (m.x27*m.x40 + m.x29*m.x45 + m.x31*m.x50 + m.x33*m.x55 + m.x35*m.x60) - 0.45*m.x5
                         == 0)

m.c15 = Constraint(expr=m.x19*m.x10 - (m.x28*m.x40 + m.x30*m.x45 + m.x32*m.x50 + m.x34*m.x55 + m.x36*m.x60) - 0.55*m.x5
                         == 0)

m.c16 = Constraint(expr=m.x20*m.x11 - (m.x27*m.x41 + m.x29*m.x46 + m.x31*m.x51 + m.x33*m.x56 + m.x35*m.x61) - 0.45*m.x6
                         == 0)

m.c17 = Constraint(expr=m.x21*m.x11 - (m.x28*m.x41 + m.x30*m.x46 + m.x32*m.x51 + m.x34*m.x56 + m.x36*m.x61) - 0.55*m.x6
                         == 0)

m.c18 = Constraint(expr= - m.x7 + m.x22 == 0)

m.c19 = Constraint(expr= - m.x8 + m.x23 == 0)

m.c20 = Constraint(expr= - m.x9 + m.x24 == 0)

m.c21 = Constraint(expr= - m.x10 + m.x25 == 0)

m.c22 = Constraint(expr= - m.x11 + m.x26 == 0)

m.c23 = Constraint(expr=m.x27*m.x22 - (m.x12*m.x7 - m.x70*m.x75) == 0)

m.c24 = Constraint(expr=m.x28*m.x22 - (m.x13*m.x7 + m.x70*m.x75) == 0)

m.c25 = Constraint(expr=m.x29*m.x23 - (m.x14*m.x8 - m.x71*m.x76) == 0)

m.c26 = Constraint(expr=m.x30*m.x23 - (m.x15*m.x8 + m.x71*m.x76) == 0)

m.c27 = Constraint(expr=m.x31*m.x24 - (m.x16*m.x9 - m.x72*m.x77) == 0)

m.c28 = Constraint(expr=m.x32*m.x24 - (m.x17*m.x9 + m.x72*m.x77) == 0)

m.c29 = Constraint(expr=m.x33*m.x25 - (m.x18*m.x10 - m.x73*m.x78) == 0)

m.c30 = Constraint(expr=m.x34*m.x25 - (m.x19*m.x10 + m.x73*m.x78) == 0)

m.c31 = Constraint(expr=m.x35*m.x26 - (m.x20*m.x11 - m.x74*m.x79) == 0)

m.c32 = Constraint(expr=m.x36*m.x26 - (m.x21*m.x11 + m.x74*m.x79) == 0)

m.c33 = Constraint(expr=-m.x27*m.x28 + m.x75 == 0)

m.c34 = Constraint(expr=-m.x29*m.x30 + m.x76 == 0)

m.c35 = Constraint(expr=-m.x31*m.x32 + m.x77 == 0)

m.c36 = Constraint(expr=-m.x33*m.x34 + m.x78 == 0)

m.c37 = Constraint(expr=-m.x35*m.x36 + m.x79 == 0)

m.c38 = Constraint(expr=   m.x22 - m.x37 - m.x38 - m.x39 - m.x40 - m.x41 - m.x62 == 0)

m.c39 = Constraint(expr=   m.x23 - m.x42 - m.x43 - m.x44 - m.x45 - m.x46 - m.x63 == 0)

m.c40 = Constraint(expr=   m.x24 - m.x47 - m.x48 - m.x49 - m.x50 - m.x51 - m.x64 == 0)

m.c41 = Constraint(expr=   m.x25 - m.x52 - m.x53 - m.x54 - m.x55 - m.x56 - m.x65 == 0)

m.c42 = Constraint(expr=   m.x26 - m.x57 - m.x58 - m.x59 - m.x60 - m.x61 - m.x66 == 0)

m.c43 = Constraint(expr= - m.x62 - m.x63 - m.x64 - m.x65 - m.x66 + m.x67 == 0)

m.c44 = Constraint(expr=m.x67*m.x68 - (m.x62*m.x27 + m.x63*m.x29 + m.x64*m.x31 + m.x65*m.x33 + m.x66*m.x35) == 0)

m.c45 = Constraint(expr=m.x67*m.x69 - (m.x62*m.x28 + m.x63*m.x30 + m.x64*m.x32 + m.x65*m.x34 + m.x66*m.x36) == 0)

m.c46 = Constraint(expr=   m.x70 + m.x71 + m.x72 + m.x73 + m.x74 == 100)
