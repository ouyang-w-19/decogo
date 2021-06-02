#  NLP written by GAMS Convert at 04/21/18 13:53:09
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        120       85        0       35        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         77       77        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        561      401      160        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,1),initialize=0)
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
m.x38 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,15),initialize=0)

m.obj = Objective(expr=   5*m.x38 - 10*m.x39 - 15*m.x40 + 9*m.x41 + 5*m.x42 - 3*m.x43 - 18*m.x44 - 23*m.x45 + m.x46
                        - 3*m.x47 - 6*m.x48 - 21*m.x49 - 26*m.x50 - 2*m.x51 - 6*m.x52 - 5*m.x53 - 20*m.x54 - 25*m.x55
                        - m.x56 - 5*m.x57 - 4*m.x58 - 19*m.x59 - 24*m.x60 - 4*m.x62 - 7*m.x63 - 22*m.x64 - 27*m.x65
                        - 3*m.x66 - 7*m.x67 - 5*m.x68 - 20*m.x69 - 25*m.x70 - m.x71 - 5*m.x72 - 5*m.x73 - 20*m.x74
                        - 25*m.x75 - m.x76 - 5*m.x77, sense=minimize)

m.c2 = Constraint(expr=   m.x38 + m.x39 + m.x40 + m.x41 + m.x42 <= 85)

m.c3 = Constraint(expr=   m.x43 + m.x44 + m.x45 + m.x46 + m.x47 <= 85)

m.c4 = Constraint(expr=   m.x48 + m.x49 + m.x50 + m.x51 + m.x52 <= 85)

m.c5 = Constraint(expr=   m.x53 + m.x54 + m.x55 + m.x56 + m.x57 <= 85)

m.c6 = Constraint(expr=   m.x58 + m.x59 + m.x60 + m.x61 + m.x62 <= 85)

m.c7 = Constraint(expr=   m.x63 + m.x64 + m.x65 + m.x66 + m.x67 <= 85)

m.c8 = Constraint(expr=   m.x68 + m.x69 + m.x70 + m.x71 + m.x72 <= 85)

m.c9 = Constraint(expr=   m.x73 + m.x74 + m.x75 + m.x76 + m.x77 <= 85)

m.c10 = Constraint(expr=   m.x38 + m.x39 + m.x40 + m.x41 + m.x42 + m.x43 + m.x44 + m.x45 + m.x46 + m.x47 + m.x48 + m.x49
                         + m.x50 + m.x51 + m.x52 + m.x53 + m.x54 + m.x55 + m.x56 + m.x57 <= 85)

m.c11 = Constraint(expr=   m.x58 + m.x59 + m.x60 + m.x61 + m.x62 + m.x63 + m.x64 + m.x65 + m.x66 + m.x67 + m.x68 + m.x69
                         + m.x70 + m.x71 + m.x72 + m.x73 + m.x74 + m.x75 + m.x76 + m.x77 <= 85)

m.c12 = Constraint(expr=   m.x38 + m.x43 + m.x48 + m.x53 + m.x58 + m.x63 + m.x68 + m.x73 <= 15)

m.c13 = Constraint(expr=   m.x39 + m.x44 + m.x49 + m.x54 + m.x59 + m.x64 + m.x69 + m.x74 <= 25)

m.c14 = Constraint(expr=   m.x40 + m.x45 + m.x50 + m.x55 + m.x60 + m.x65 + m.x70 + m.x75 <= 10)

m.c15 = Constraint(expr=   m.x41 + m.x46 + m.x51 + m.x56 + m.x61 + m.x66 + m.x71 + m.x76 <= 20)

m.c16 = Constraint(expr=   m.x42 + m.x47 + m.x52 + m.x57 + m.x62 + m.x67 + m.x72 + m.x77 <= 15)

m.c17 = Constraint(expr= - 0.7*m.x38 + 0.2*m.x43 + 0.3*m.x53 + 0.4*m.x58 + 0.3*m.x68 + 0.2*m.x73 <= 0)

m.c18 = Constraint(expr=   0.2*m.x38 + 0.1*m.x43 + 0.2*m.x48 - 0.5*m.x53 + 0.1*m.x58 - 0.6*m.x63 - 0.2*m.x68
                         - 0.0999999999999999*m.x73 <= 0)

m.c19 = Constraint(expr= - 0.0999999999999999*m.x38 + 0.3*m.x43 + 0.3*m.x53 + 0.2*m.x58 + 0.1*m.x68 - 0.2*m.x73 <= 0)

m.c20 = Constraint(expr= - 0.7*m.x38 - 0.0999999999999999*m.x43 - 0.3*m.x48 - 0.4*m.x53 + 0.3*m.x58 + 0.3*m.x63
                         - 0.2*m.x68 - 0.0999999999999999*m.x73 <= 0)

m.c21 = Constraint(expr= - 0.9*m.x39 - 0.2*m.x49 + 0.1*m.x54 + 0.2*m.x59 - 0.2*m.x64 + 0.1*m.x69 <= 0)

m.c22 = Constraint(expr=   0.6*m.x39 + 0.5*m.x44 + 0.6*m.x49 - 0.1*m.x54 + 0.5*m.x59 - 0.2*m.x64 + 0.2*m.x69 + 0.3*m.x74
                         <= 0)

m.c23 = Constraint(expr= - 0.5*m.x39 - 0.1*m.x44 - 0.4*m.x49 - 0.1*m.x54 - 0.2*m.x59 - 0.4*m.x64 - 0.3*m.x69 - 0.6*m.x74
                         <= 0)

m.c24 = Constraint(expr= - 0.4*m.x39 + 0.2*m.x44 - 0.0999999999999999*m.x54 + 0.6*m.x59 + 0.6*m.x64 + 0.1*m.x69
                         + 0.2*m.x74 <= 0)

m.c25 = Constraint(expr= - 0.8*m.x40 + 0.0999999999999999*m.x45 - 0.1*m.x50 + 0.2*m.x55 + 0.3*m.x60 - 0.1*m.x65
                         + 0.2*m.x70 + 0.0999999999999999*m.x75 <= 0)

m.c26 = Constraint(expr=   0.6*m.x40 + 0.5*m.x45 + 0.6*m.x50 - 0.1*m.x55 + 0.5*m.x60 - 0.2*m.x65 + 0.2*m.x70 + 0.3*m.x75
                         <= 0)

m.c27 = Constraint(expr= - 0.6*m.x40 - 0.2*m.x45 - 0.5*m.x50 - 0.2*m.x55 - 0.3*m.x60 - 0.5*m.x65 - 0.4*m.x70 - 0.7*m.x75
                         <= 0)

m.c28 = Constraint(expr= - 0.9*m.x40 - 0.3*m.x45 - 0.5*m.x50 - 0.6*m.x55 + 0.1*m.x60 + 0.1*m.x65 - 0.4*m.x70 - 0.3*m.x75
                         <= 0)

m.c29 = Constraint(expr= - 0.7*m.x41 + 0.2*m.x46 + 0.3*m.x56 + 0.4*m.x61 + 0.3*m.x71 + 0.2*m.x76 <= 0)

m.c30 = Constraint(expr=   0.8*m.x41 + 0.7*m.x46 + 0.8*m.x51 + 0.0999999999999999*m.x56 + 0.7*m.x61 + 0.4*m.x71
                         + 0.5*m.x76 <= 0)

m.c31 = Constraint(expr= - 0.4*m.x41 - 0.3*m.x51 - 0.0999999999999999*m.x61 - 0.3*m.x66 - 0.2*m.x71 - 0.5*m.x76 <= 0)

m.c32 = Constraint(expr= - 0.6*m.x41 - 0.2*m.x51 - 0.3*m.x56 + 0.4*m.x61 + 0.4*m.x66 - 0.1*m.x71 <= 0)

m.c33 = Constraint(expr= - 1.1*m.x42 - 0.2*m.x47 - 0.4*m.x52 - 0.1*m.x57 - 0.4*m.x67 - 0.1*m.x72 - 0.2*m.x77 <= 0)

m.c34 = Constraint(expr= - 0.0999999999999999*m.x47 - 0.7*m.x57 - 0.0999999999999999*m.x62 - 0.8*m.x67 - 0.4*m.x72
                         - 0.3*m.x77 <= 0)

m.c35 = Constraint(expr= - 0.7*m.x42 - 0.3*m.x47 - 0.6*m.x52 - 0.3*m.x57 - 0.4*m.x62 - 0.6*m.x67 - 0.5*m.x72 - 0.8*m.x77
                         <= 0)

m.c36 = Constraint(expr= - 1.5*m.x42 - 0.9*m.x47 - 1.1*m.x52 - 1.2*m.x57 - 0.5*m.x62 - 0.5*m.x67 - m.x72 - 0.9*m.x77
                         <= 0)

m.c37 = Constraint(expr=   m.x20 + m.x21 + m.x22 + m.x23 == 1)

m.c38 = Constraint(expr=   m.x24 + m.x25 + m.x26 + m.x27 == 1)

m.c39 = Constraint(expr=   m.x28 + m.x29 + m.x30 + m.x31 + m.x32 == 1)

m.c40 = Constraint(expr=   m.x33 + m.x34 + m.x35 + m.x36 + m.x37 == 1)

m.c41 = Constraint(expr=-m.x20*m.x10 + m.x38 == 0)

m.c42 = Constraint(expr=-m.x20*m.x11 + m.x39 == 0)

m.c43 = Constraint(expr=-m.x20*m.x12 + m.x40 == 0)

m.c44 = Constraint(expr=-m.x20*m.x13 + m.x41 == 0)

m.c45 = Constraint(expr=-m.x20*m.x14 + m.x42 == 0)

m.c46 = Constraint(expr=-m.x21*m.x10 + m.x43 == 0)

m.c47 = Constraint(expr=-m.x21*m.x11 + m.x44 == 0)

m.c48 = Constraint(expr=-m.x21*m.x12 + m.x45 == 0)

m.c49 = Constraint(expr=-m.x21*m.x13 + m.x46 == 0)

m.c50 = Constraint(expr=-m.x21*m.x14 + m.x47 == 0)

m.c51 = Constraint(expr=-m.x22*m.x10 + m.x48 == 0)

m.c52 = Constraint(expr=-m.x22*m.x11 + m.x49 == 0)

m.c53 = Constraint(expr=-m.x22*m.x12 + m.x50 == 0)

m.c54 = Constraint(expr=-m.x22*m.x13 + m.x51 == 0)

m.c55 = Constraint(expr=-m.x22*m.x14 + m.x52 == 0)

m.c56 = Constraint(expr=-m.x23*m.x10 + m.x53 == 0)

m.c57 = Constraint(expr=-m.x23*m.x11 + m.x54 == 0)

m.c58 = Constraint(expr=-m.x23*m.x12 + m.x55 == 0)

m.c59 = Constraint(expr=-m.x23*m.x13 + m.x56 == 0)

m.c60 = Constraint(expr=-m.x23*m.x14 + m.x57 == 0)

m.c61 = Constraint(expr=-m.x24*m.x15 + m.x58 == 0)

m.c62 = Constraint(expr=-m.x24*m.x16 + m.x59 == 0)

m.c63 = Constraint(expr=-m.x24*m.x17 + m.x60 == 0)

m.c64 = Constraint(expr=-m.x24*m.x18 + m.x61 == 0)

m.c65 = Constraint(expr=-m.x24*m.x19 + m.x62 == 0)

m.c66 = Constraint(expr=-m.x25*m.x15 + m.x63 == 0)

m.c67 = Constraint(expr=-m.x25*m.x16 + m.x64 == 0)

m.c68 = Constraint(expr=-m.x25*m.x17 + m.x65 == 0)

m.c69 = Constraint(expr=-m.x25*m.x18 + m.x66 == 0)

m.c70 = Constraint(expr=-m.x25*m.x19 + m.x67 == 0)

m.c71 = Constraint(expr=-m.x26*m.x15 + m.x68 == 0)

m.c72 = Constraint(expr=-m.x26*m.x16 + m.x69 == 0)

m.c73 = Constraint(expr=-m.x26*m.x17 + m.x70 == 0)

m.c74 = Constraint(expr=-m.x26*m.x18 + m.x71 == 0)

m.c75 = Constraint(expr=-m.x26*m.x19 + m.x72 == 0)

m.c76 = Constraint(expr=-m.x27*m.x15 + m.x73 == 0)

m.c77 = Constraint(expr=-m.x27*m.x16 + m.x74 == 0)

m.c78 = Constraint(expr=-m.x27*m.x17 + m.x75 == 0)

m.c79 = Constraint(expr=-m.x27*m.x18 + m.x76 == 0)

m.c80 = Constraint(expr=-m.x27*m.x19 + m.x77 == 0)

m.c81 = Constraint(expr=-m.x28*m.x2 + m.x38 == 0)

m.c82 = Constraint(expr=-m.x29*m.x2 + m.x39 == 0)

m.c83 = Constraint(expr=-m.x30*m.x2 + m.x40 == 0)

m.c84 = Constraint(expr=-m.x31*m.x2 + m.x41 == 0)

m.c85 = Constraint(expr=-m.x32*m.x2 + m.x42 == 0)

m.c86 = Constraint(expr=-m.x28*m.x3 + m.x43 == 0)

m.c87 = Constraint(expr=-m.x29*m.x3 + m.x44 == 0)

m.c88 = Constraint(expr=-m.x30*m.x3 + m.x45 == 0)

m.c89 = Constraint(expr=-m.x31*m.x3 + m.x46 == 0)

m.c90 = Constraint(expr=-m.x32*m.x3 + m.x47 == 0)

m.c91 = Constraint(expr=-m.x28*m.x4 + m.x48 == 0)

m.c92 = Constraint(expr=-m.x29*m.x4 + m.x49 == 0)

m.c93 = Constraint(expr=-m.x30*m.x4 + m.x50 == 0)

m.c94 = Constraint(expr=-m.x31*m.x4 + m.x51 == 0)

m.c95 = Constraint(expr=-m.x32*m.x4 + m.x52 == 0)

m.c96 = Constraint(expr=-m.x28*m.x5 + m.x53 == 0)

m.c97 = Constraint(expr=-m.x29*m.x5 + m.x54 == 0)

m.c98 = Constraint(expr=-m.x30*m.x5 + m.x55 == 0)

m.c99 = Constraint(expr=-m.x31*m.x5 + m.x56 == 0)

m.c100 = Constraint(expr=-m.x32*m.x5 + m.x57 == 0)

m.c101 = Constraint(expr=-m.x33*m.x6 + m.x58 == 0)

m.c102 = Constraint(expr=-m.x34*m.x6 + m.x59 == 0)

m.c103 = Constraint(expr=-m.x35*m.x6 + m.x60 == 0)

m.c104 = Constraint(expr=-m.x36*m.x6 + m.x61 == 0)

m.c105 = Constraint(expr=-m.x37*m.x6 + m.x62 == 0)

m.c106 = Constraint(expr=-m.x33*m.x7 + m.x63 == 0)

m.c107 = Constraint(expr=-m.x34*m.x7 + m.x64 == 0)

m.c108 = Constraint(expr=-m.x35*m.x7 + m.x65 == 0)

m.c109 = Constraint(expr=-m.x36*m.x7 + m.x66 == 0)

m.c110 = Constraint(expr=-m.x37*m.x7 + m.x67 == 0)

m.c111 = Constraint(expr=-m.x33*m.x8 + m.x68 == 0)

m.c112 = Constraint(expr=-m.x34*m.x8 + m.x69 == 0)

m.c113 = Constraint(expr=-m.x35*m.x8 + m.x70 == 0)

m.c114 = Constraint(expr=-m.x36*m.x8 + m.x71 == 0)

m.c115 = Constraint(expr=-m.x37*m.x8 + m.x72 == 0)

m.c116 = Constraint(expr=-m.x33*m.x9 + m.x73 == 0)

m.c117 = Constraint(expr=-m.x34*m.x9 + m.x74 == 0)

m.c118 = Constraint(expr=-m.x35*m.x9 + m.x75 == 0)

m.c119 = Constraint(expr=-m.x36*m.x9 + m.x76 == 0)

m.c120 = Constraint(expr=-m.x37*m.x9 + m.x77 == 0)
