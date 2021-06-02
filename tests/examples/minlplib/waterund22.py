#  NLP written by GAMS Convert at 04/21/18 13:55:19
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        136       63       18       55        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        147      147        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1017      561      456        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,100000),initialize=0)

m.obj = Objective(expr=   m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13 + m.x14
                        + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20 + m.x21 + m.x22 + m.x23 + m.x24 + m.x25 + m.x26
                        + m.x27 + m.x28 + m.x29 + m.x30 + m.x31 + m.x32 + m.x33 + m.x34 + m.x35 + m.x36, sense=minimize)

m.c2 = Constraint(expr= - m.x2 - m.x9 - m.x16 - m.x23 - m.x30 + m.x37 - m.x51 - m.x58 - m.x65 - m.x72 - m.x79 - m.x86
                        - m.x93 == 0)

m.c3 = Constraint(expr= - m.x3 - m.x10 - m.x17 - m.x24 - m.x31 + m.x38 - m.x52 - m.x59 - m.x66 - m.x73 - m.x80 - m.x87
                        - m.x94 == 0)

m.c4 = Constraint(expr= - m.x4 - m.x11 - m.x18 - m.x25 - m.x32 + m.x39 - m.x53 - m.x60 - m.x67 - m.x74 - m.x81 - m.x88
                        - m.x95 == 0)

m.c5 = Constraint(expr= - m.x5 - m.x12 - m.x19 - m.x26 - m.x33 + m.x40 - m.x54 - m.x61 - m.x68 - m.x75 - m.x82 - m.x89
                        - m.x96 == 0)

m.c6 = Constraint(expr= - m.x6 - m.x13 - m.x20 - m.x27 - m.x34 - m.x55 - m.x62 - m.x69 - m.x76 - m.x83 - m.x90 - m.x97
                        == -80)

m.c7 = Constraint(expr= - m.x7 - m.x14 - m.x21 - m.x28 - m.x35 - m.x56 - m.x63 - m.x70 - m.x77 - m.x84 - m.x91 - m.x98
                        == -80)

m.c8 = Constraint(expr= - m.x8 - m.x15 - m.x22 - m.x29 - m.x36 - m.x57 - m.x64 - m.x71 - m.x78 - m.x85 - m.x92 - m.x99
                        == -70)

m.c9 = Constraint(expr=   m.x37 - m.x44 - m.x51 - m.x52 - m.x53 - m.x54 - m.x55 - m.x56 - m.x57 == 0)

m.c10 = Constraint(expr=   m.x38 - m.x45 - m.x58 - m.x59 - m.x60 - m.x61 - m.x62 - m.x63 - m.x64 == 0)

m.c11 = Constraint(expr=   m.x39 - m.x46 - m.x65 - m.x66 - m.x67 - m.x68 - m.x69 - m.x70 - m.x71 == 0)

m.c12 = Constraint(expr=   m.x40 - m.x47 - m.x72 - m.x73 - m.x74 - m.x75 - m.x76 - m.x77 - m.x78 == 0)

m.c13 = Constraint(expr= - m.x48 - m.x79 - m.x80 - m.x81 - m.x82 - m.x83 - m.x84 - m.x85 == -30)

m.c14 = Constraint(expr= - m.x49 - m.x86 - m.x87 - m.x88 - m.x89 - m.x90 - m.x91 - m.x92 == -100)

m.c15 = Constraint(expr= - m.x50 - m.x93 - m.x94 - m.x95 - m.x96 - m.x97 - m.x98 - m.x99 == -90)

m.c16 = Constraint(expr=m.x37*m.x100 - (m.x51*m.x124 + m.x58*m.x130 + m.x65*m.x136 + m.x72*m.x142) - m.x2 - 6*m.x9
                         - 4*m.x16 - 7*m.x23 - 6*m.x30 - 421*m.x79 - 112*m.x86 - 491*m.x93 == 0)

m.c17 = Constraint(expr=m.x37*m.x101 - (m.x51*m.x125 + m.x58*m.x131 + m.x65*m.x137 + m.x72*m.x143) - 2*m.x2 - 2*m.x9
                         - 8*m.x16 - 9*m.x23 - 9*m.x30 - 316*m.x79 - 429*m.x86 - 476*m.x93 == 0)

m.c18 = Constraint(expr=m.x37*m.x102 - (m.x51*m.x126 + m.x58*m.x132 + m.x65*m.x138 + m.x72*m.x144) - 2*m.x2 - 2*m.x9
                         - 6*m.x16 - 5*m.x23 - 2*m.x30 - 391*m.x79 - 505*m.x86 - 197*m.x93 == 0)

m.c19 = Constraint(expr=m.x37*m.x103 - (m.x51*m.x127 + m.x58*m.x133 + m.x65*m.x139 + m.x72*m.x145) - 5*m.x2 - 3*m.x9
                         - 3*m.x16 - m.x23 - m.x30 - 352*m.x79 - 266*m.x86 - 493*m.x93 == 0)

m.c20 = Constraint(expr=m.x37*m.x104 - (m.x51*m.x128 + m.x58*m.x134 + m.x65*m.x140 + m.x72*m.x146) - 2*m.x2 - 6*m.x9
                         - 2*m.x16 - m.x23 - 6*m.x30 - 461*m.x79 - 481*m.x86 - 399*m.x93 == 0)

m.c21 = Constraint(expr=m.x37*m.x105 - (m.x51*m.x129 + m.x58*m.x135 + m.x65*m.x141 + m.x72*m.x147) - 10*m.x2 - m.x16
                         - 4*m.x30 - 489*m.x79 - 505*m.x86 - 495*m.x93 == 0)

m.c22 = Constraint(expr=m.x38*m.x106 - (m.x52*m.x124 + m.x59*m.x130 + m.x66*m.x136 + m.x73*m.x142) - m.x3 - 6*m.x10
                         - 4*m.x17 - 7*m.x24 - 6*m.x31 - 421*m.x80 - 112*m.x87 - 491*m.x94 == 0)

m.c23 = Constraint(expr=m.x38*m.x107 - (m.x52*m.x125 + m.x59*m.x131 + m.x66*m.x137 + m.x73*m.x143) - 2*m.x3 - 2*m.x10
                         - 8*m.x17 - 9*m.x24 - 9*m.x31 - 316*m.x80 - 429*m.x87 - 476*m.x94 == 0)

m.c24 = Constraint(expr=m.x38*m.x108 - (m.x52*m.x126 + m.x59*m.x132 + m.x66*m.x138 + m.x73*m.x144) - 2*m.x3 - 2*m.x10
                         - 6*m.x17 - 5*m.x24 - 2*m.x31 - 391*m.x80 - 505*m.x87 - 197*m.x94 == 0)

m.c25 = Constraint(expr=m.x38*m.x109 - (m.x52*m.x127 + m.x59*m.x133 + m.x66*m.x139 + m.x73*m.x145) - 5*m.x3 - 3*m.x10
                         - 3*m.x17 - m.x24 - m.x31 - 352*m.x80 - 266*m.x87 - 493*m.x94 == 0)

m.c26 = Constraint(expr=m.x38*m.x110 - (m.x52*m.x128 + m.x59*m.x134 + m.x66*m.x140 + m.x73*m.x146) - 2*m.x3 - 6*m.x10
                         - 2*m.x17 - m.x24 - 6*m.x31 - 461*m.x80 - 481*m.x87 - 399*m.x94 == 0)

m.c27 = Constraint(expr=m.x38*m.x111 - (m.x52*m.x129 + m.x59*m.x135 + m.x66*m.x141 + m.x73*m.x147) - 10*m.x3 - m.x17
                         - 4*m.x31 - 489*m.x80 - 505*m.x87 - 495*m.x94 == 0)

m.c28 = Constraint(expr=m.x39*m.x112 - (m.x53*m.x124 + m.x60*m.x130 + m.x67*m.x136 + m.x74*m.x142) - m.x4 - 6*m.x11
                         - 4*m.x18 - 7*m.x25 - 6*m.x32 - 421*m.x81 - 112*m.x88 - 491*m.x95 == 0)

m.c29 = Constraint(expr=m.x39*m.x113 - (m.x53*m.x125 + m.x60*m.x131 + m.x67*m.x137 + m.x74*m.x143) - 2*m.x4 - 2*m.x11
                         - 8*m.x18 - 9*m.x25 - 9*m.x32 - 316*m.x81 - 429*m.x88 - 476*m.x95 == 0)

m.c30 = Constraint(expr=m.x39*m.x114 - (m.x53*m.x126 + m.x60*m.x132 + m.x67*m.x138 + m.x74*m.x144) - 2*m.x4 - 2*m.x11
                         - 6*m.x18 - 5*m.x25 - 2*m.x32 - 391*m.x81 - 505*m.x88 - 197*m.x95 == 0)

m.c31 = Constraint(expr=m.x39*m.x115 - (m.x53*m.x127 + m.x60*m.x133 + m.x67*m.x139 + m.x74*m.x145) - 5*m.x4 - 3*m.x11
                         - 3*m.x18 - m.x25 - m.x32 - 352*m.x81 - 266*m.x88 - 493*m.x95 == 0)

m.c32 = Constraint(expr=m.x39*m.x116 - (m.x53*m.x128 + m.x60*m.x134 + m.x67*m.x140 + m.x74*m.x146) - 2*m.x4 - 6*m.x11
                         - 2*m.x18 - m.x25 - 6*m.x32 - 461*m.x81 - 481*m.x88 - 399*m.x95 == 0)

m.c33 = Constraint(expr=m.x39*m.x117 - (m.x53*m.x129 + m.x60*m.x135 + m.x67*m.x141 + m.x74*m.x147) - 10*m.x4 - m.x18
                         - 4*m.x32 - 489*m.x81 - 505*m.x88 - 495*m.x95 == 0)

m.c34 = Constraint(expr=m.x40*m.x118 - (m.x54*m.x124 + m.x61*m.x130 + m.x68*m.x136 + m.x75*m.x142) - m.x5 - 6*m.x12
                         - 4*m.x19 - 7*m.x26 - 6*m.x33 - 421*m.x82 - 112*m.x89 - 491*m.x96 == 0)

m.c35 = Constraint(expr=m.x40*m.x119 - (m.x54*m.x125 + m.x61*m.x131 + m.x68*m.x137 + m.x75*m.x143) - 2*m.x5 - 2*m.x12
                         - 8*m.x19 - 9*m.x26 - 9*m.x33 - 316*m.x82 - 429*m.x89 - 476*m.x96 == 0)

m.c36 = Constraint(expr=m.x40*m.x120 - (m.x54*m.x126 + m.x61*m.x132 + m.x68*m.x138 + m.x75*m.x144) - 2*m.x5 - 2*m.x12
                         - 6*m.x19 - 5*m.x26 - 2*m.x33 - 391*m.x82 - 505*m.x89 - 197*m.x96 == 0)

m.c37 = Constraint(expr=m.x40*m.x121 - (m.x54*m.x127 + m.x61*m.x133 + m.x68*m.x139 + m.x75*m.x145) - 5*m.x5 - 3*m.x12
                         - 3*m.x19 - m.x26 - m.x33 - 352*m.x82 - 266*m.x89 - 493*m.x96 == 0)

m.c38 = Constraint(expr=m.x40*m.x122 - (m.x54*m.x128 + m.x61*m.x134 + m.x68*m.x140 + m.x75*m.x146) - 2*m.x5 - 6*m.x12
                         - 2*m.x19 - m.x26 - 6*m.x33 - 461*m.x82 - 481*m.x89 - 399*m.x96 == 0)

m.c39 = Constraint(expr=m.x40*m.x123 - (m.x54*m.x129 + m.x61*m.x135 + m.x68*m.x141 + m.x75*m.x147) - 10*m.x5 - m.x19
                         - 4*m.x33 - 489*m.x82 - 505*m.x89 - 495*m.x96 == 0)

m.c40 = Constraint(expr=-m.x37*(m.x124 - m.x100) == -19900)

m.c41 = Constraint(expr=-m.x37*(m.x125 - m.x101) == -1700)

m.c42 = Constraint(expr=-m.x37*(m.x126 - m.x102) == -19700)

m.c43 = Constraint(expr=-m.x37*(m.x127 - m.x103) == -18600)

m.c44 = Constraint(expr=-m.x37*(m.x128 - m.x104) == -47600)

m.c45 = Constraint(expr=-m.x37*(m.x129 - m.x105) == -7300)

m.c46 = Constraint(expr=-m.x38*(m.x130 - m.x106) == -6700)

m.c47 = Constraint(expr=-m.x38*(m.x131 - m.x107) == -4300)

m.c48 = Constraint(expr=-m.x38*(m.x132 - m.x108) == -7700)

m.c49 = Constraint(expr=-m.x38*(m.x133 - m.x109) == -20800)

m.c50 = Constraint(expr=-m.x38*(m.x134 - m.x110) == -5000)

m.c51 = Constraint(expr=-m.x38*(m.x135 - m.x111) == -13600)

m.c52 = Constraint(expr=-m.x39*(m.x136 - m.x112) == -8640)

m.c53 = Constraint(expr=-m.x39*(m.x137 - m.x113) == -640)

m.c54 = Constraint(expr=-m.x39*(m.x138 - m.x114) == -2000)

m.c55 = Constraint(expr=-m.x39*(m.x139 - m.x115) == -600)

m.c56 = Constraint(expr=-m.x39*(m.x140 - m.x116) == -7040)

m.c57 = Constraint(expr=-m.x39*(m.x141 - m.x117) == -2480)

m.c58 = Constraint(expr=-m.x40*(m.x142 - m.x118) == -12240)

m.c59 = Constraint(expr=-m.x40*(m.x143 - m.x119) == -12420)

m.c60 = Constraint(expr=-m.x40*(m.x144 - m.x120) == -3150)

m.c61 = Constraint(expr=-m.x40*(m.x145 - m.x121) == -14400)

m.c62 = Constraint(expr=-m.x40*(m.x146 - m.x122) == -810)

m.c63 = Constraint(expr=-m.x40*(m.x147 - m.x123) == -15660)

m.c64 = Constraint(expr=   m.x100 <= 65)

m.c65 = Constraint(expr=   m.x101 <= 465)

m.c66 = Constraint(expr=   m.x102 <= 166)

m.c67 = Constraint(expr=   m.x103 <= 56)

m.c68 = Constraint(expr=   m.x104 <= 33)

m.c69 = Constraint(expr=   m.x105 <= 346)

m.c70 = Constraint(expr=   m.x106 <= 448)

m.c71 = Constraint(expr=   m.x107 <= 414)

m.c72 = Constraint(expr=   m.x108 <= 268)

m.c73 = Constraint(expr=   m.x109 <= 191)

m.c74 = Constraint(expr=   m.x110 <= 350)

m.c75 = Constraint(expr=   m.x111 <= 243)

m.c76 = Constraint(expr=   m.x112 <= 171)

m.c77 = Constraint(expr=   m.x113 <= 496)

m.c78 = Constraint(expr=   m.x114 <= 406)

m.c79 = Constraint(expr=   m.x115 <= 486)

m.c80 = Constraint(expr=   m.x116 <= 323)

m.c81 = Constraint(expr=   m.x117 <= 355)

m.c82 = Constraint(expr=   m.x118 <= 139)

m.c83 = Constraint(expr=   m.x119 <= 211)

m.c84 = Constraint(expr=   m.x120 <= 469)

m.c85 = Constraint(expr=   m.x121 <= 65)

m.c86 = Constraint(expr=   m.x122 <= 259)

m.c87 = Constraint(expr=   m.x123 <= 328)

m.c88 = Constraint(expr=   m.x124 <= 264)

m.c89 = Constraint(expr=   m.x125 <= 482)

m.c90 = Constraint(expr=   m.x126 <= 363)

m.c91 = Constraint(expr=   m.x127 <= 242)

m.c92 = Constraint(expr=   m.x128 <= 509)

m.c93 = Constraint(expr=   m.x129 <= 419)

m.c94 = Constraint(expr=   m.x130 <= 515)

m.c95 = Constraint(expr=   m.x131 <= 457)

m.c96 = Constraint(expr=   m.x132 <= 345)

m.c97 = Constraint(expr=   m.x133 <= 399)

m.c98 = Constraint(expr=   m.x134 <= 400)

m.c99 = Constraint(expr=   m.x135 <= 379)

m.c100 = Constraint(expr=   m.x136 <= 387)

m.c101 = Constraint(expr=   m.x137 <= 512)

m.c102 = Constraint(expr=   m.x138 <= 456)

m.c103 = Constraint(expr=   m.x139 <= 501)

m.c104 = Constraint(expr=   m.x140 <= 499)

m.c105 = Constraint(expr=   m.x141 <= 417)

m.c106 = Constraint(expr=   m.x142 <= 275)

m.c107 = Constraint(expr=   m.x143 <= 349)

m.c108 = Constraint(expr=   m.x144 <= 504)

m.c109 = Constraint(expr=   m.x145 <= 225)

m.c110 = Constraint(expr=   m.x146 <= 268)

m.c111 = Constraint(expr=   m.x147 <= 502)

m.c112 = Constraint(expr=-(m.x55*m.x124 + m.x62*m.x130 + m.x69*m.x136 + m.x76*m.x142) - m.x6 - 6*m.x13 - 4*m.x20
                          - 7*m.x27 - 6*m.x34 - 421*m.x83 - 112*m.x90 - 491*m.x97 >= -25520)

m.c113 = Constraint(expr=-(m.x55*m.x125 + m.x62*m.x131 + m.x69*m.x137 + m.x76*m.x143) - 2*m.x6 - 2*m.x13 - 8*m.x20
                          - 9*m.x27 - 9*m.x34 - 316*m.x83 - 429*m.x90 - 476*m.x97 >= -24240)

m.c114 = Constraint(expr=-(m.x55*m.x126 + m.x62*m.x132 + m.x69*m.x138 + m.x76*m.x144) - 2*m.x6 - 2*m.x13 - 6*m.x20
                          - 5*m.x27 - 2*m.x34 - 391*m.x83 - 505*m.x90 - 197*m.x97 >= -18320)

m.c115 = Constraint(expr=-(m.x55*m.x127 + m.x62*m.x133 + m.x69*m.x139 + m.x76*m.x145) - 5*m.x6 - 3*m.x13 - 3*m.x20
                          - m.x27 - m.x34 - 352*m.x83 - 266*m.x90 - 493*m.x97 >= -23680)

m.c116 = Constraint(expr=-(m.x55*m.x128 + m.x62*m.x134 + m.x69*m.x140 + m.x76*m.x146) - 2*m.x6 - 6*m.x13 - 2*m.x20
                          - m.x27 - 6*m.x34 - 461*m.x83 - 481*m.x90 - 399*m.x97 >= -1040)

m.c117 = Constraint(expr=-(m.x55*m.x129 + m.x62*m.x135 + m.x69*m.x141 + m.x76*m.x147) - 10*m.x6 - m.x20 - 4*m.x34
                          - 489*m.x83 - 505*m.x90 - 495*m.x97 >= -36320)

m.c118 = Constraint(expr=-(m.x56*m.x124 + m.x63*m.x130 + m.x70*m.x136 + m.x77*m.x142) - m.x7 - 6*m.x14 - 4*m.x21
                          - 7*m.x28 - 6*m.x35 - 421*m.x84 - 112*m.x91 - 491*m.x98 >= -3440)

m.c119 = Constraint(expr=-(m.x56*m.x125 + m.x63*m.x131 + m.x70*m.x137 + m.x77*m.x143) - 2*m.x7 - 2*m.x14 - 8*m.x21
                          - 9*m.x28 - 9*m.x35 - 316*m.x84 - 429*m.x91 - 476*m.x98 >= -27360)

m.c120 = Constraint(expr=-(m.x56*m.x126 + m.x63*m.x132 + m.x70*m.x138 + m.x77*m.x144) - 2*m.x7 - 2*m.x14 - 6*m.x21
                          - 5*m.x28 - 2*m.x35 - 391*m.x84 - 505*m.x91 - 197*m.x98 >= -18560)

m.c121 = Constraint(expr=-(m.x56*m.x127 + m.x63*m.x133 + m.x70*m.x139 + m.x77*m.x145) - 5*m.x7 - 3*m.x14 - 3*m.x21
                          - m.x28 - m.x35 - 352*m.x84 - 266*m.x91 - 493*m.x98 >= -21200)

m.c122 = Constraint(expr=-(m.x56*m.x128 + m.x63*m.x134 + m.x70*m.x140 + m.x77*m.x146) - 2*m.x7 - 6*m.x14 - 2*m.x21
                          - m.x28 - 6*m.x35 - 461*m.x84 - 481*m.x91 - 399*m.x98 >= -31440)

m.c123 = Constraint(expr=-(m.x56*m.x129 + m.x63*m.x135 + m.x70*m.x141 + m.x77*m.x147) - 10*m.x7 - m.x21 - 4*m.x35
                          - 489*m.x84 - 505*m.x91 - 495*m.x98 >= -23920)

m.c124 = Constraint(expr=-(m.x57*m.x124 + m.x64*m.x130 + m.x71*m.x136 + m.x78*m.x142) - m.x8 - 6*m.x15 - 4*m.x22
                          - 7*m.x29 - 6*m.x36 - 421*m.x85 - 112*m.x92 - 491*m.x99 >= -31640)

m.c125 = Constraint(expr=-(m.x57*m.x125 + m.x64*m.x131 + m.x71*m.x137 + m.x78*m.x143) - 2*m.x8 - 2*m.x15 - 8*m.x22
                          - 9*m.x29 - 9*m.x36 - 316*m.x85 - 429*m.x92 - 476*m.x99 >= -4480)

m.c126 = Constraint(expr=-(m.x57*m.x126 + m.x64*m.x132 + m.x71*m.x138 + m.x78*m.x144) - 2*m.x8 - 2*m.x15 - 6*m.x22
                          - 5*m.x29 - 2*m.x36 - 391*m.x85 - 505*m.x92 - 197*m.x99 >= -700)

m.c127 = Constraint(expr=-(m.x57*m.x127 + m.x64*m.x133 + m.x71*m.x139 + m.x78*m.x145) - 5*m.x8 - 3*m.x15 - 3*m.x22
                          - m.x29 - m.x36 - 352*m.x85 - 266*m.x92 - 493*m.x99 >= -23380)

m.c128 = Constraint(expr=-(m.x57*m.x128 + m.x64*m.x134 + m.x71*m.x140 + m.x78*m.x146) - 2*m.x8 - 6*m.x15 - 2*m.x22
                          - m.x29 - 6*m.x36 - 461*m.x85 - 481*m.x92 - 399*m.x99 >= -10010)

m.c129 = Constraint(expr=-(m.x57*m.x129 + m.x64*m.x135 + m.x71*m.x141 + m.x78*m.x147) - 10*m.x8 - m.x22 - 4*m.x36
                          - 489*m.x85 - 505*m.x92 - 495*m.x99 >= -17080)

m.c130 = Constraint(expr=   m.x37 <= 100)

m.c131 = Constraint(expr=   m.x38 <= 100)

m.c132 = Constraint(expr=   m.x39 <= 40)

m.c133 = Constraint(expr=   m.x40 <= 90)

m.c134 = Constraint(expr=   m.x41 <= 0)

m.c135 = Constraint(expr=   m.x42 <= 0)

m.c136 = Constraint(expr=   m.x43 <= 0)
