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
#        562      442      120        0
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
m.x14 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,100),initialize=0)

m.obj = Objective(expr= - 12*m.x17 - 9*m.x18 - 13*m.x19 - 10*m.x20 - 8*m.x21 - 12*m.x22 - 9*m.x23 - 13*m.x24 - 10*m.x25
                        - 8*m.x26 - 12*m.x27 - 9*m.x28 - 13*m.x29 - 10*m.x30 - 8*m.x31 - 2*m.x32 + m.x33 - 3*m.x34
                        + 2*m.x36 - 2*m.x37 + m.x38 - 3*m.x39 + 2*m.x41 - 2*m.x42 + m.x43 - 3*m.x44 + 2*m.x46 - 3*m.x47
                        - 4*m.x49 - m.x50 + m.x51 - 3*m.x52 - 4*m.x54 - m.x55 + m.x56 - 3*m.x57 - 4*m.x59 - m.x60
                        + m.x61 - 6*m.x62 - 3*m.x63 - 7*m.x64 - 4*m.x65 - 2*m.x66 - 6*m.x67 - 3*m.x68 - 7*m.x69
                        - 4*m.x70 - 2*m.x71 - 6*m.x72 - 3*m.x73 - 7*m.x74 - 4*m.x75 - 2*m.x76 - 8*m.x89 - 5*m.x90
                        - 9*m.x91 - 6*m.x92 - 4*m.x93, sense=minimize)

m.c2 = Constraint(expr=   m.x17 + m.x18 + m.x19 + m.x20 + m.x21 + m.x22 + m.x23 + m.x24 + m.x25 + m.x26 + m.x27 + m.x28
                        + m.x29 + m.x30 + m.x31 <= 600)

m.c3 = Constraint(expr=   m.x32 + m.x33 + m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 + m.x42 + m.x43
                        + m.x44 + m.x45 + m.x46 <= 600)

m.c4 = Constraint(expr=   m.x47 + m.x48 + m.x49 + m.x50 + m.x51 + m.x52 + m.x53 + m.x54 + m.x55 + m.x56 + m.x57 + m.x58
                        + m.x59 + m.x60 + m.x61 <= 50)

m.c5 = Constraint(expr=   m.x62 + m.x63 + m.x64 + m.x65 + m.x66 + m.x67 + m.x68 + m.x69 + m.x70 + m.x71 + m.x72 + m.x73
                        + m.x74 + m.x75 + m.x76 <= 600)

m.c6 = Constraint(expr=   m.x89 + m.x90 + m.x91 + m.x92 + m.x93 <= 600)

m.c7 = Constraint(expr=   m.x17 + m.x18 + m.x19 + m.x20 + m.x21 + m.x32 + m.x33 + m.x34 + m.x35 + m.x36 + m.x47 + m.x48
                        + m.x49 + m.x50 + m.x51 + m.x62 + m.x63 + m.x64 + m.x65 + m.x66 <= 600)

m.c8 = Constraint(expr=   m.x22 + m.x23 + m.x24 + m.x25 + m.x26 + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 + m.x52 + m.x53
                        + m.x54 + m.x55 + m.x56 + m.x67 + m.x68 + m.x69 + m.x70 + m.x71 <= 600)

m.c9 = Constraint(expr=   m.x27 + m.x28 + m.x29 + m.x30 + m.x31 + m.x42 + m.x43 + m.x44 + m.x45 + m.x46 + m.x57 + m.x58
                        + m.x59 + m.x60 + m.x61 + m.x72 + m.x73 + m.x74 + m.x75 + m.x76 <= 600)

m.c10 = Constraint(expr=   m.x17 + m.x22 + m.x27 + m.x32 + m.x37 + m.x42 + m.x47 + m.x52 + m.x57 + m.x62 + m.x67 + m.x72
                         + m.x89 <= 100)

m.c11 = Constraint(expr=   m.x18 + m.x23 + m.x28 + m.x33 + m.x38 + m.x43 + m.x48 + m.x53 + m.x58 + m.x63 + m.x68 + m.x73
                         + m.x90 <= 200)

m.c12 = Constraint(expr=   m.x19 + m.x24 + m.x29 + m.x34 + m.x39 + m.x44 + m.x49 + m.x54 + m.x59 + m.x64 + m.x69 + m.x74
                         + m.x91 <= 100)

m.c13 = Constraint(expr=   m.x20 + m.x25 + m.x30 + m.x35 + m.x40 + m.x45 + m.x50 + m.x55 + m.x60 + m.x65 + m.x70 + m.x75
                         + m.x92 <= 100)

m.c14 = Constraint(expr=   m.x21 + m.x26 + m.x31 + m.x36 + m.x41 + m.x46 + m.x51 + m.x56 + m.x61 + m.x66 + m.x71 + m.x76
                         + m.x93 <= 100)

m.c15 = Constraint(expr=   0.5*m.x17 + 0.5*m.x22 + 0.5*m.x27 - 1.5*m.x32 - 1.5*m.x37 - 1.5*m.x42 - 1.5*m.x47 - 1.5*m.x52
                         - 1.5*m.x57 - m.x62 - m.x67 - m.x72 - 0.5*m.x89 <= 0)

m.c16 = Constraint(expr= - m.x17 - m.x22 - m.x27 + m.x32 + m.x37 + m.x42 + 0.5*m.x47 + 0.5*m.x52 + 0.5*m.x57 + 0.5*m.x62
                         + 0.5*m.x67 + 0.5*m.x72 + 0.5*m.x89 <= 0)

m.c17 = Constraint(expr=   1.5*m.x18 + 1.5*m.x23 + 1.5*m.x28 - 0.5*m.x33 - 0.5*m.x38 - 0.5*m.x43 - 0.5*m.x48 - 0.5*m.x53
                         - 0.5*m.x58 + 0.5*m.x90 <= 0)

m.c18 = Constraint(expr= - 1.5*m.x18 - 1.5*m.x23 - 1.5*m.x28 + 0.5*m.x33 + 0.5*m.x38 + 0.5*m.x43 <= 0)

m.c19 = Constraint(expr=   m.x19 + m.x24 + m.x29 - m.x34 - m.x39 - m.x44 - m.x49 - m.x54 - m.x59 - 0.5*m.x64 - 0.5*m.x69
                         - 0.5*m.x74 <= 0)

m.c20 = Constraint(expr= - 1.6*m.x19 - 1.6*m.x24 - 1.6*m.x29 + 0.4*m.x34 + 0.4*m.x39 + 0.4*m.x44 - 0.1*m.x49 - 0.1*m.x54
                         - 0.1*m.x59 - 0.1*m.x64 - 0.1*m.x69 - 0.1*m.x74 - 0.1*m.x91 <= 0)

m.c21 = Constraint(expr=   m.x20 + m.x25 + m.x30 - m.x35 - m.x40 - m.x45 - m.x50 - m.x55 - m.x60 - 0.5*m.x65 - 0.5*m.x70
                         - 0.5*m.x75 <= 0)

m.c22 = Constraint(expr= - m.x20 - m.x25 - m.x30 + m.x35 + m.x40 + m.x45 + 0.5*m.x50 + 0.5*m.x55 + 0.5*m.x60 + 0.5*m.x65
                         + 0.5*m.x70 + 0.5*m.x75 + 0.5*m.x92 <= 0)

m.c23 = Constraint(expr=   m.x21 + m.x26 + m.x31 - m.x36 - m.x41 - m.x46 - m.x51 - m.x56 - m.x61 - 0.5*m.x66 - 0.5*m.x71
                         - 0.5*m.x76 <= 0)

m.c24 = Constraint(expr= - m.x21 - m.x26 - m.x31 + m.x36 + m.x41 + m.x46 + 0.5*m.x51 + 0.5*m.x56 + 0.5*m.x61 + 0.5*m.x66
                         + 0.5*m.x71 + 0.5*m.x76 + 0.5*m.x93 <= 0)

m.c25 = Constraint(expr=   m.x2 + m.x3 + m.x4 + m.x5 + m.x6 == 1)

m.c26 = Constraint(expr=   m.x7 + m.x8 + m.x9 + m.x10 + m.x11 == 1)

m.c27 = Constraint(expr=   m.x12 + m.x13 + m.x14 + m.x15 + m.x16 == 1)

m.c28 = Constraint(expr=-m.x2*m.x77 + m.x17 == 0)

m.c29 = Constraint(expr=-m.x3*m.x77 + m.x18 == 0)

m.c30 = Constraint(expr=-m.x4*m.x77 + m.x19 == 0)

m.c31 = Constraint(expr=-m.x5*m.x77 + m.x20 == 0)

m.c32 = Constraint(expr=-m.x6*m.x77 + m.x21 == 0)

m.c33 = Constraint(expr=-m.x7*m.x78 + m.x22 == 0)

m.c34 = Constraint(expr=-m.x8*m.x78 + m.x23 == 0)

m.c35 = Constraint(expr=-m.x9*m.x78 + m.x24 == 0)

m.c36 = Constraint(expr=-m.x10*m.x78 + m.x25 == 0)

m.c37 = Constraint(expr=-m.x11*m.x78 + m.x26 == 0)

m.c38 = Constraint(expr=-m.x12*m.x79 + m.x27 == 0)

m.c39 = Constraint(expr=-m.x13*m.x79 + m.x28 == 0)

m.c40 = Constraint(expr=-m.x14*m.x79 + m.x29 == 0)

m.c41 = Constraint(expr=-m.x15*m.x79 + m.x30 == 0)

m.c42 = Constraint(expr=-m.x16*m.x79 + m.x31 == 0)

m.c43 = Constraint(expr=-m.x2*m.x80 + m.x32 == 0)

m.c44 = Constraint(expr=-m.x3*m.x80 + m.x33 == 0)

m.c45 = Constraint(expr=-m.x4*m.x80 + m.x34 == 0)

m.c46 = Constraint(expr=-m.x5*m.x80 + m.x35 == 0)

m.c47 = Constraint(expr=-m.x6*m.x80 + m.x36 == 0)

m.c48 = Constraint(expr=-m.x7*m.x81 + m.x37 == 0)

m.c49 = Constraint(expr=-m.x8*m.x81 + m.x38 == 0)

m.c50 = Constraint(expr=-m.x9*m.x81 + m.x39 == 0)

m.c51 = Constraint(expr=-m.x10*m.x81 + m.x40 == 0)

m.c52 = Constraint(expr=-m.x11*m.x81 + m.x41 == 0)

m.c53 = Constraint(expr=-m.x12*m.x82 + m.x42 == 0)

m.c54 = Constraint(expr=-m.x13*m.x82 + m.x43 == 0)

m.c55 = Constraint(expr=-m.x14*m.x82 + m.x44 == 0)

m.c56 = Constraint(expr=-m.x15*m.x82 + m.x45 == 0)

m.c57 = Constraint(expr=-m.x16*m.x82 + m.x46 == 0)

m.c58 = Constraint(expr=-m.x2*m.x83 + m.x47 == 0)

m.c59 = Constraint(expr=-m.x3*m.x83 + m.x48 == 0)

m.c60 = Constraint(expr=-m.x4*m.x83 + m.x49 == 0)

m.c61 = Constraint(expr=-m.x5*m.x83 + m.x50 == 0)

m.c62 = Constraint(expr=-m.x6*m.x83 + m.x51 == 0)

m.c63 = Constraint(expr=-m.x7*m.x84 + m.x52 == 0)

m.c64 = Constraint(expr=-m.x8*m.x84 + m.x53 == 0)

m.c65 = Constraint(expr=-m.x9*m.x84 + m.x54 == 0)

m.c66 = Constraint(expr=-m.x10*m.x84 + m.x55 == 0)

m.c67 = Constraint(expr=-m.x11*m.x84 + m.x56 == 0)

m.c68 = Constraint(expr=-m.x12*m.x85 + m.x57 == 0)

m.c69 = Constraint(expr=-m.x13*m.x85 + m.x58 == 0)

m.c70 = Constraint(expr=-m.x14*m.x85 + m.x59 == 0)

m.c71 = Constraint(expr=-m.x15*m.x85 + m.x60 == 0)

m.c72 = Constraint(expr=-m.x16*m.x85 + m.x61 == 0)

m.c73 = Constraint(expr=-m.x2*m.x86 + m.x62 == 0)

m.c74 = Constraint(expr=-m.x3*m.x86 + m.x63 == 0)

m.c75 = Constraint(expr=-m.x4*m.x86 + m.x64 == 0)

m.c76 = Constraint(expr=-m.x5*m.x86 + m.x65 == 0)

m.c77 = Constraint(expr=-m.x6*m.x86 + m.x66 == 0)

m.c78 = Constraint(expr=-m.x7*m.x87 + m.x67 == 0)

m.c79 = Constraint(expr=-m.x8*m.x87 + m.x68 == 0)

m.c80 = Constraint(expr=-m.x9*m.x87 + m.x69 == 0)

m.c81 = Constraint(expr=-m.x10*m.x87 + m.x70 == 0)

m.c82 = Constraint(expr=-m.x11*m.x87 + m.x71 == 0)

m.c83 = Constraint(expr=-m.x12*m.x88 + m.x72 == 0)

m.c84 = Constraint(expr=-m.x13*m.x88 + m.x73 == 0)

m.c85 = Constraint(expr=-m.x14*m.x88 + m.x74 == 0)

m.c86 = Constraint(expr=-m.x15*m.x88 + m.x75 == 0)

m.c87 = Constraint(expr=-m.x16*m.x88 + m.x76 == 0)
