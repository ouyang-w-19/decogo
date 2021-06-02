#  NLP written by GAMS Convert at 04/21/18 13:53:09
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        110       71        0       39        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         73       73        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        518      390      128        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,75),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,75),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,75),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,75),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,75),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,75),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,75),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,75),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,10),initialize=0)

m.obj = Objective(expr= - 9*m.x42 - 18*m.x43 - 8*m.x44 - 3*m.x45 - 13*m.x46 - 22*m.x47 - 12*m.x48 - 7*m.x49 - 14*m.x50
                        - 23*m.x51 - 13*m.x52 - 8*m.x53 - 6*m.x54 - 15*m.x55 - 5*m.x56 - 11*m.x58 - 20*m.x59 - 10*m.x60
                        - 5*m.x61 - 11*m.x62 - 20*m.x63 - 10*m.x64 - 5*m.x65 - 7*m.x66 - 16*m.x67 - 6*m.x68 - m.x69
                        - 5*m.x70 - 14*m.x71 - 4*m.x72 + m.x73, sense=minimize)

m.c2 = Constraint(expr=   m.x42 + m.x43 + m.x44 + m.x45 <= 75)

m.c3 = Constraint(expr=   m.x46 + m.x47 + m.x48 + m.x49 <= 75)

m.c4 = Constraint(expr=   m.x50 + m.x51 + m.x52 + m.x53 <= 75)

m.c5 = Constraint(expr=   m.x54 + m.x55 + m.x56 + m.x57 <= 75)

m.c6 = Constraint(expr=   m.x58 + m.x59 + m.x60 + m.x61 <= 75)

m.c7 = Constraint(expr=   m.x62 + m.x63 + m.x64 + m.x65 <= 75)

m.c8 = Constraint(expr=   m.x66 + m.x67 + m.x68 + m.x69 <= 75)

m.c9 = Constraint(expr=   m.x70 + m.x71 + m.x72 + m.x73 <= 75)

m.c10 = Constraint(expr=   m.x42 + m.x43 + m.x44 + m.x45 + m.x46 + m.x47 + m.x48 + m.x49 <= 75)

m.c11 = Constraint(expr=   m.x50 + m.x51 + m.x52 + m.x53 + m.x54 + m.x55 + m.x56 + m.x57 + m.x58 + m.x59 + m.x60 + m.x61
                         <= 75)

m.c12 = Constraint(expr=   m.x62 + m.x63 + m.x64 + m.x65 + m.x66 + m.x67 + m.x68 + m.x69 + m.x70 + m.x71 + m.x72 + m.x73
                         <= 75)

m.c13 = Constraint(expr=   m.x42 + m.x46 + m.x50 + m.x54 + m.x58 + m.x62 + m.x66 + m.x70 <= 10)

m.c14 = Constraint(expr=   m.x43 + m.x47 + m.x51 + m.x55 + m.x59 + m.x63 + m.x67 + m.x71 <= 25)

m.c15 = Constraint(expr=   m.x44 + m.x48 + m.x52 + m.x56 + m.x60 + m.x64 + m.x68 + m.x72 <= 30)

m.c16 = Constraint(expr=   m.x45 + m.x49 + m.x53 + m.x57 + m.x61 + m.x65 + m.x69 + m.x73 <= 10)

m.c17 = Constraint(expr= - 2*m.x42 + m.x46 + m.x50 - 2*m.x58 - 1.2*m.x62 + 2*m.x66 <= 0)

m.c18 = Constraint(expr=   3*m.x42 - 2*m.x46 + 2.5*m.x50 - 0.3*m.x58 - 0.3*m.x62 - 2*m.x66 <= 0)

m.c19 = Constraint(expr=   0.75*m.x42 - 0.25*m.x46 - 0.25*m.x50 - 0.25*m.x54 + 0.75*m.x58 + 0.75*m.x62 - 1.55*m.x66
                         - 0.25*m.x70 <= 0)

m.c20 = Constraint(expr= - 0.25*m.x42 + 1.25*m.x46 + 0.15*m.x50 + 0.25*m.x54 + 0.85*m.x58 + 2.75*m.x62 + 2.15*m.x66
                         + 0.25*m.x70 <= 0)

m.c21 = Constraint(expr= - m.x42 - 2*m.x46 + m.x50 - 3*m.x54 - 3*m.x58 + 0.0999999999999996*m.x62 - 2.5*m.x66 - m.x70
                         <= 0)

m.c22 = Constraint(expr=   4*m.x42 - m.x46 + 5*m.x50 - m.x54 + 2*m.x58 - 2*m.x62 - 2.1*m.x66 - 3*m.x70 <= 0)

m.c23 = Constraint(expr= - 3*m.x43 - m.x55 - 3*m.x59 - 2.2*m.x63 + m.x67 - m.x71 <= 0)

m.c24 = Constraint(expr=   3.5*m.x43 - 1.5*m.x47 + 3*m.x51 + 0.5*m.x55 + 0.2*m.x59 + 0.2*m.x63 - 1.5*m.x67 + 0.5*m.x71
                         <= 0)

m.c25 = Constraint(expr=   0.5*m.x43 - 0.5*m.x47 - 0.5*m.x51 - 0.5*m.x55 + 0.5*m.x59 + 0.5*m.x63 - 1.8*m.x67 - 0.5*m.x71
                         <= 0)

m.c26 = Constraint(expr= - m.x43 + 0.5*m.x47 - 0.6*m.x51 - 0.5*m.x55 + 0.1*m.x59 + 2*m.x63 + 1.4*m.x67 - 0.5*m.x71 <= 0)

m.c27 = Constraint(expr= - 2*m.x43 - 3*m.x47 - 4*m.x55 - 4*m.x59 - 0.9*m.x63 - 3.5*m.x67 - 2*m.x71 <= 0)

m.c28 = Constraint(expr=   3*m.x43 - 2*m.x47 + 4*m.x51 - 2*m.x55 + m.x59 - 3*m.x63 - 3.1*m.x67 - 4*m.x71 <= 0)

m.c29 = Constraint(expr= - 0.5*m.x44 + 2.5*m.x48 + 2.5*m.x52 + 1.5*m.x56 - 0.5*m.x60 + 0.3*m.x64 + 3.5*m.x68 + 1.5*m.x72
                         <= 0)

m.c30 = Constraint(expr=   0.5*m.x44 - 4.5*m.x48 - 2.5*m.x56 - 2.8*m.x60 - 2.8*m.x64 - 4.5*m.x68 - 2.5*m.x72 <= 0)

m.c31 = Constraint(expr=   0.1*m.x44 - 0.9*m.x48 - 0.9*m.x52 - 0.9*m.x56 + 0.1*m.x60 + 0.1*m.x64 - 2.2*m.x68 - 0.9*m.x72
                         <= 0)

m.c32 = Constraint(expr= - 0.3*m.x44 + 1.2*m.x48 + 0.1*m.x52 + 0.2*m.x56 + 0.8*m.x60 + 2.7*m.x64 + 2.1*m.x68 + 0.2*m.x72
                         <= 0)

m.c33 = Constraint(expr= - 2*m.x44 - 3*m.x48 - 4*m.x56 - 4*m.x60 - 0.9*m.x64 - 3.5*m.x68 - 2*m.x72 <= 0)

m.c34 = Constraint(expr=   3*m.x44 - 2*m.x48 + 4*m.x52 - 2*m.x56 + m.x60 - 3*m.x64 - 3.1*m.x68 - 4*m.x72 <= 0)

m.c35 = Constraint(expr= - 2*m.x45 + m.x49 + m.x53 - 2*m.x61 - 1.2*m.x65 + 2*m.x69 <= 0)

m.c36 = Constraint(expr=   2*m.x45 - 3*m.x49 + 1.5*m.x53 - m.x57 - 1.3*m.x61 - 1.3*m.x65 - 3*m.x69 - m.x73 <= 0)

m.c37 = Constraint(expr= - m.x49 - m.x53 - m.x57 - 2.3*m.x69 - m.x73 <= 0)

m.c38 = Constraint(expr= - 1.3*m.x45 + 0.2*m.x49 - 0.9*m.x53 - 0.8*m.x57 - 0.2*m.x61 + 1.7*m.x65 + 1.1*m.x69 - 0.8*m.x73
                         <= 0)

m.c39 = Constraint(expr= - m.x45 - 2*m.x49 + m.x53 - 3*m.x57 - 3*m.x61 + 0.0999999999999996*m.x65 - 2.5*m.x69 - m.x73
                         <= 0)

m.c40 = Constraint(expr=   3*m.x45 - 2*m.x49 + 4*m.x53 - 2*m.x57 + m.x61 - 3*m.x65 - 3.1*m.x69 - 4*m.x73 <= 0)

m.c41 = Constraint(expr=   m.x22 + m.x23 == 1)

m.c42 = Constraint(expr=   m.x24 + m.x25 + m.x26 == 1)

m.c43 = Constraint(expr=   m.x27 + m.x28 + m.x29 == 1)

m.c44 = Constraint(expr=   m.x30 + m.x31 + m.x32 + m.x33 == 1)

m.c45 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 == 1)

m.c46 = Constraint(expr=   m.x38 + m.x39 + m.x40 + m.x41 == 1)

m.c47 = Constraint(expr=-m.x22*m.x10 + m.x42 == 0)

m.c48 = Constraint(expr=-m.x22*m.x11 + m.x43 == 0)

m.c49 = Constraint(expr=-m.x22*m.x12 + m.x44 == 0)

m.c50 = Constraint(expr=-m.x22*m.x13 + m.x45 == 0)

m.c51 = Constraint(expr=-m.x23*m.x10 + m.x46 == 0)

m.c52 = Constraint(expr=-m.x23*m.x11 + m.x47 == 0)

m.c53 = Constraint(expr=-m.x23*m.x12 + m.x48 == 0)

m.c54 = Constraint(expr=-m.x23*m.x13 + m.x49 == 0)

m.c55 = Constraint(expr=-m.x24*m.x14 + m.x50 == 0)

m.c56 = Constraint(expr=-m.x24*m.x15 + m.x51 == 0)

m.c57 = Constraint(expr=-m.x24*m.x16 + m.x52 == 0)

m.c58 = Constraint(expr=-m.x24*m.x17 + m.x53 == 0)

m.c59 = Constraint(expr=-m.x25*m.x14 + m.x54 == 0)

m.c60 = Constraint(expr=-m.x25*m.x15 + m.x55 == 0)

m.c61 = Constraint(expr=-m.x25*m.x16 + m.x56 == 0)

m.c62 = Constraint(expr=-m.x25*m.x17 + m.x57 == 0)

m.c63 = Constraint(expr=-m.x26*m.x14 + m.x58 == 0)

m.c64 = Constraint(expr=-m.x26*m.x15 + m.x59 == 0)

m.c65 = Constraint(expr=-m.x26*m.x16 + m.x60 == 0)

m.c66 = Constraint(expr=-m.x26*m.x17 + m.x61 == 0)

m.c67 = Constraint(expr=-m.x27*m.x18 + m.x62 == 0)

m.c68 = Constraint(expr=-m.x27*m.x19 + m.x63 == 0)

m.c69 = Constraint(expr=-m.x27*m.x20 + m.x64 == 0)

m.c70 = Constraint(expr=-m.x27*m.x21 + m.x65 == 0)

m.c71 = Constraint(expr=-m.x28*m.x18 + m.x66 == 0)

m.c72 = Constraint(expr=-m.x28*m.x19 + m.x67 == 0)

m.c73 = Constraint(expr=-m.x28*m.x20 + m.x68 == 0)

m.c74 = Constraint(expr=-m.x28*m.x21 + m.x69 == 0)

m.c75 = Constraint(expr=-m.x29*m.x18 + m.x70 == 0)

m.c76 = Constraint(expr=-m.x29*m.x19 + m.x71 == 0)

m.c77 = Constraint(expr=-m.x29*m.x20 + m.x72 == 0)

m.c78 = Constraint(expr=-m.x29*m.x21 + m.x73 == 0)

m.c79 = Constraint(expr=-m.x30*m.x2 + m.x42 == 0)

m.c80 = Constraint(expr=-m.x31*m.x2 + m.x43 == 0)

m.c81 = Constraint(expr=-m.x32*m.x2 + m.x44 == 0)

m.c82 = Constraint(expr=-m.x33*m.x2 + m.x45 == 0)

m.c83 = Constraint(expr=-m.x30*m.x3 + m.x46 == 0)

m.c84 = Constraint(expr=-m.x31*m.x3 + m.x47 == 0)

m.c85 = Constraint(expr=-m.x32*m.x3 + m.x48 == 0)

m.c86 = Constraint(expr=-m.x33*m.x3 + m.x49 == 0)

m.c87 = Constraint(expr=-m.x34*m.x4 + m.x50 == 0)

m.c88 = Constraint(expr=-m.x35*m.x4 + m.x51 == 0)

m.c89 = Constraint(expr=-m.x36*m.x4 + m.x52 == 0)

m.c90 = Constraint(expr=-m.x37*m.x4 + m.x53 == 0)

m.c91 = Constraint(expr=-m.x34*m.x5 + m.x54 == 0)

m.c92 = Constraint(expr=-m.x35*m.x5 + m.x55 == 0)

m.c93 = Constraint(expr=-m.x36*m.x5 + m.x56 == 0)

m.c94 = Constraint(expr=-m.x37*m.x5 + m.x57 == 0)

m.c95 = Constraint(expr=-m.x34*m.x6 + m.x58 == 0)

m.c96 = Constraint(expr=-m.x35*m.x6 + m.x59 == 0)

m.c97 = Constraint(expr=-m.x36*m.x6 + m.x60 == 0)

m.c98 = Constraint(expr=-m.x37*m.x6 + m.x61 == 0)

m.c99 = Constraint(expr=-m.x38*m.x7 + m.x62 == 0)

m.c100 = Constraint(expr=-m.x39*m.x7 + m.x63 == 0)

m.c101 = Constraint(expr=-m.x40*m.x7 + m.x64 == 0)

m.c102 = Constraint(expr=-m.x41*m.x7 + m.x65 == 0)

m.c103 = Constraint(expr=-m.x38*m.x8 + m.x66 == 0)

m.c104 = Constraint(expr=-m.x39*m.x8 + m.x67 == 0)

m.c105 = Constraint(expr=-m.x40*m.x8 + m.x68 == 0)

m.c106 = Constraint(expr=-m.x41*m.x8 + m.x69 == 0)

m.c107 = Constraint(expr=-m.x38*m.x9 + m.x70 == 0)

m.c108 = Constraint(expr=-m.x39*m.x9 + m.x71 == 0)

m.c109 = Constraint(expr=-m.x40*m.x9 + m.x72 == 0)

m.c110 = Constraint(expr=-m.x41*m.x9 + m.x73 == 0)
