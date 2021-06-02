#  NLP written by GAMS Convert at 04/21/18 13:53:10
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         87       64        0       23        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         93       93        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        559      439      120        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,100),initialize=0)

m.obj = Objective(expr= - 8*m.x14 - 5*m.x15 - 9*m.x16 - 6*m.x17 - 4*m.x18 - 12*m.x34 - 9*m.x35 - 13*m.x36 - 10*m.x37
                        - 8*m.x38 - 12*m.x39 - 9*m.x40 - 13*m.x41 - 10*m.x42 - 8*m.x43 - 12*m.x44 - 9*m.x45 - 13*m.x46
                        - 10*m.x47 - 8*m.x48 - 2*m.x49 + m.x50 - 3*m.x51 + 2*m.x53 - 2*m.x54 + m.x55 - 3*m.x56 + 2*m.x58
                        - 2*m.x59 + m.x60 - 3*m.x61 + 2*m.x63 - 3*m.x64 - 4*m.x66 - m.x67 + m.x68 - 3*m.x69 - 4*m.x71
                        - m.x72 + m.x73 - 3*m.x74 - 4*m.x76 - m.x77 + m.x78 - 6*m.x79 - 3*m.x80 - 7*m.x81 - 4*m.x82
                        - 2*m.x83 - 6*m.x84 - 3*m.x85 - 7*m.x86 - 4*m.x87 - 2*m.x88 - 6*m.x89 - 3*m.x90 - 7*m.x91
                        - 4*m.x92 - 2*m.x93, sense=minimize)

m.c2 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 + m.x42 + m.x43 + m.x44 + m.x45
                        + m.x46 + m.x47 + m.x48 <= 600)

m.c3 = Constraint(expr=   m.x49 + m.x50 + m.x51 + m.x52 + m.x53 + m.x54 + m.x55 + m.x56 + m.x57 + m.x58 + m.x59 + m.x60
                        + m.x61 + m.x62 + m.x63 <= 600)

m.c4 = Constraint(expr=   m.x64 + m.x65 + m.x66 + m.x67 + m.x68 + m.x69 + m.x70 + m.x71 + m.x72 + m.x73 + m.x74 + m.x75
                        + m.x76 + m.x77 + m.x78 <= 50)

m.c5 = Constraint(expr=   m.x79 + m.x80 + m.x81 + m.x82 + m.x83 + m.x84 + m.x85 + m.x86 + m.x87 + m.x88 + m.x89 + m.x90
                        + m.x91 + m.x92 + m.x93 <= 600)

m.c6 = Constraint(expr=   m.x14 + m.x15 + m.x16 + m.x17 + m.x18 <= 600)

m.c7 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x49 + m.x50 + m.x51 + m.x52 + m.x53 + m.x64 + m.x65
                        + m.x66 + m.x67 + m.x68 + m.x79 + m.x80 + m.x81 + m.x82 + m.x83 <= 600)

m.c8 = Constraint(expr=   m.x39 + m.x40 + m.x41 + m.x42 + m.x43 + m.x54 + m.x55 + m.x56 + m.x57 + m.x58 + m.x69 + m.x70
                        + m.x71 + m.x72 + m.x73 + m.x84 + m.x85 + m.x86 + m.x87 + m.x88 <= 600)

m.c9 = Constraint(expr=   m.x44 + m.x45 + m.x46 + m.x47 + m.x48 + m.x59 + m.x60 + m.x61 + m.x62 + m.x63 + m.x74 + m.x75
                        + m.x76 + m.x77 + m.x78 + m.x89 + m.x90 + m.x91 + m.x92 + m.x93 <= 600)

m.c10 = Constraint(expr=   m.x14 + m.x34 + m.x39 + m.x44 + m.x49 + m.x54 + m.x59 + m.x64 + m.x69 + m.x74 + m.x79 + m.x84
                         + m.x89 <= 100)

m.c11 = Constraint(expr=   m.x15 + m.x35 + m.x40 + m.x45 + m.x50 + m.x55 + m.x60 + m.x65 + m.x70 + m.x75 + m.x80 + m.x85
                         + m.x90 <= 200)

m.c12 = Constraint(expr=   m.x16 + m.x36 + m.x41 + m.x46 + m.x51 + m.x56 + m.x61 + m.x66 + m.x71 + m.x76 + m.x81 + m.x86
                         + m.x91 <= 100)

m.c13 = Constraint(expr=   m.x17 + m.x37 + m.x42 + m.x47 + m.x52 + m.x57 + m.x62 + m.x67 + m.x72 + m.x77 + m.x82 + m.x87
                         + m.x92 <= 100)

m.c14 = Constraint(expr=   m.x18 + m.x38 + m.x43 + m.x48 + m.x53 + m.x58 + m.x63 + m.x68 + m.x73 + m.x78 + m.x83 + m.x88
                         + m.x93 <= 100)

m.c15 = Constraint(expr= - 0.5*m.x14 + 0.5*m.x34 + 0.5*m.x39 + 0.5*m.x44 - 1.5*m.x49 - 1.5*m.x54 - 1.5*m.x59 - 1.5*m.x64
                         - 1.5*m.x69 - 1.5*m.x74 - m.x79 - m.x84 - m.x89 <= 0)

m.c16 = Constraint(expr=   0.5*m.x14 - m.x34 - m.x39 - m.x44 + m.x49 + m.x54 + m.x59 + 0.5*m.x64 + 0.5*m.x69 + 0.5*m.x74
                         + 0.5*m.x79 + 0.5*m.x84 + 0.5*m.x89 <= 0)

m.c17 = Constraint(expr=   0.5*m.x15 + 1.5*m.x35 + 1.5*m.x40 + 1.5*m.x45 - 0.5*m.x50 - 0.5*m.x55 - 0.5*m.x60 - 0.5*m.x65
                         - 0.5*m.x70 - 0.5*m.x75 <= 0)

m.c18 = Constraint(expr= - 1.5*m.x35 - 1.5*m.x40 - 1.5*m.x45 + 0.5*m.x50 + 0.5*m.x55 + 0.5*m.x60 <= 0)

m.c19 = Constraint(expr=   m.x36 + m.x41 + m.x46 - m.x51 - m.x56 - m.x61 - m.x66 - m.x71 - m.x76 - 0.5*m.x81 - 0.5*m.x86
                         - 0.5*m.x91 <= 0)

m.c20 = Constraint(expr= - 0.1*m.x16 - 1.6*m.x36 - 1.6*m.x41 - 1.6*m.x46 + 0.4*m.x51 + 0.4*m.x56 + 0.4*m.x61 - 0.1*m.x66
                         - 0.1*m.x71 - 0.1*m.x76 - 0.1*m.x81 - 0.1*m.x86 - 0.1*m.x91 <= 0)

m.c21 = Constraint(expr=   m.x37 + m.x42 + m.x47 - m.x52 - m.x57 - m.x62 - m.x67 - m.x72 - m.x77 - 0.5*m.x82 - 0.5*m.x87
                         - 0.5*m.x92 <= 0)

m.c22 = Constraint(expr=   0.5*m.x17 - m.x37 - m.x42 - m.x47 + m.x52 + m.x57 + m.x62 + 0.5*m.x67 + 0.5*m.x72 + 0.5*m.x77
                         + 0.5*m.x82 + 0.5*m.x87 + 0.5*m.x92 <= 0)

m.c23 = Constraint(expr=   m.x38 + m.x43 + m.x48 - m.x53 - m.x58 - m.x63 - m.x68 - m.x73 - m.x78 - 0.5*m.x83 - 0.5*m.x88
                         - 0.5*m.x93 <= 0)

m.c24 = Constraint(expr=   0.5*m.x18 - m.x38 - m.x43 - m.x48 + m.x53 + m.x58 + m.x63 + 0.5*m.x68 + 0.5*m.x73 + 0.5*m.x78
                         + 0.5*m.x83 + 0.5*m.x88 + 0.5*m.x93 <= 0)

m.c25 = Constraint(expr=   m.x2 + m.x5 + m.x8 + m.x11 == 1)

m.c26 = Constraint(expr=   m.x3 + m.x6 + m.x9 + m.x12 == 1)

m.c27 = Constraint(expr=   m.x4 + m.x7 + m.x10 + m.x13 == 1)

m.c28 = Constraint(expr=-m.x2*m.x19 + m.x34 == 0)

m.c29 = Constraint(expr=-m.x2*m.x20 + m.x35 == 0)

m.c30 = Constraint(expr=-m.x2*m.x21 + m.x36 == 0)

m.c31 = Constraint(expr=-m.x2*m.x22 + m.x37 == 0)

m.c32 = Constraint(expr=-m.x2*m.x23 + m.x38 == 0)

m.c33 = Constraint(expr=-m.x3*m.x24 + m.x39 == 0)

m.c34 = Constraint(expr=-m.x3*m.x25 + m.x40 == 0)

m.c35 = Constraint(expr=-m.x3*m.x26 + m.x41 == 0)

m.c36 = Constraint(expr=-m.x3*m.x27 + m.x42 == 0)

m.c37 = Constraint(expr=-m.x3*m.x28 + m.x43 == 0)

m.c38 = Constraint(expr=-m.x4*m.x29 + m.x44 == 0)

m.c39 = Constraint(expr=-m.x4*m.x30 + m.x45 == 0)

m.c40 = Constraint(expr=-m.x4*m.x31 + m.x46 == 0)

m.c41 = Constraint(expr=-m.x4*m.x32 + m.x47 == 0)

m.c42 = Constraint(expr=-m.x4*m.x33 + m.x48 == 0)

m.c43 = Constraint(expr=-m.x5*m.x19 + m.x49 == 0)

m.c44 = Constraint(expr=-m.x5*m.x20 + m.x50 == 0)

m.c45 = Constraint(expr=-m.x5*m.x21 + m.x51 == 0)

m.c46 = Constraint(expr=-m.x5*m.x22 + m.x52 == 0)

m.c47 = Constraint(expr=-m.x5*m.x23 + m.x53 == 0)

m.c48 = Constraint(expr=-m.x6*m.x24 + m.x54 == 0)

m.c49 = Constraint(expr=-m.x6*m.x25 + m.x55 == 0)

m.c50 = Constraint(expr=-m.x6*m.x26 + m.x56 == 0)

m.c51 = Constraint(expr=-m.x6*m.x27 + m.x57 == 0)

m.c52 = Constraint(expr=-m.x6*m.x28 + m.x58 == 0)

m.c53 = Constraint(expr=-m.x7*m.x29 + m.x59 == 0)

m.c54 = Constraint(expr=-m.x7*m.x30 + m.x60 == 0)

m.c55 = Constraint(expr=-m.x7*m.x31 + m.x61 == 0)

m.c56 = Constraint(expr=-m.x7*m.x32 + m.x62 == 0)

m.c57 = Constraint(expr=-m.x7*m.x33 + m.x63 == 0)

m.c58 = Constraint(expr=-m.x8*m.x19 + m.x64 == 0)

m.c59 = Constraint(expr=-m.x8*m.x20 + m.x65 == 0)

m.c60 = Constraint(expr=-m.x8*m.x21 + m.x66 == 0)

m.c61 = Constraint(expr=-m.x8*m.x22 + m.x67 == 0)

m.c62 = Constraint(expr=-m.x8*m.x23 + m.x68 == 0)

m.c63 = Constraint(expr=-m.x9*m.x24 + m.x69 == 0)

m.c64 = Constraint(expr=-m.x9*m.x25 + m.x70 == 0)

m.c65 = Constraint(expr=-m.x9*m.x26 + m.x71 == 0)

m.c66 = Constraint(expr=-m.x9*m.x27 + m.x72 == 0)

m.c67 = Constraint(expr=-m.x9*m.x28 + m.x73 == 0)

m.c68 = Constraint(expr=-m.x10*m.x29 + m.x74 == 0)

m.c69 = Constraint(expr=-m.x10*m.x30 + m.x75 == 0)

m.c70 = Constraint(expr=-m.x10*m.x31 + m.x76 == 0)

m.c71 = Constraint(expr=-m.x10*m.x32 + m.x77 == 0)

m.c72 = Constraint(expr=-m.x10*m.x33 + m.x78 == 0)

m.c73 = Constraint(expr=-m.x11*m.x19 + m.x79 == 0)

m.c74 = Constraint(expr=-m.x11*m.x20 + m.x80 == 0)

m.c75 = Constraint(expr=-m.x11*m.x21 + m.x81 == 0)

m.c76 = Constraint(expr=-m.x11*m.x22 + m.x82 == 0)

m.c77 = Constraint(expr=-m.x11*m.x23 + m.x83 == 0)

m.c78 = Constraint(expr=-m.x12*m.x24 + m.x84 == 0)

m.c79 = Constraint(expr=-m.x12*m.x25 + m.x85 == 0)

m.c80 = Constraint(expr=-m.x12*m.x26 + m.x86 == 0)

m.c81 = Constraint(expr=-m.x12*m.x27 + m.x87 == 0)

m.c82 = Constraint(expr=-m.x12*m.x28 + m.x88 == 0)

m.c83 = Constraint(expr=-m.x13*m.x29 + m.x89 == 0)

m.c84 = Constraint(expr=-m.x13*m.x30 + m.x90 == 0)

m.c85 = Constraint(expr=-m.x13*m.x31 + m.x91 == 0)

m.c86 = Constraint(expr=-m.x13*m.x32 + m.x92 == 0)

m.c87 = Constraint(expr=-m.x13*m.x33 + m.x93 == 0)
