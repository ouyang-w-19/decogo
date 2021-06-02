#  NLP written by GAMS Convert at 04/21/18 13:55:19
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         88       45        6       37        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        122      122        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        620      335      285        0
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

m.obj = Objective(expr=   m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13 + m.x14
                        + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20 + m.x21 + m.x22 + m.x23 + m.x24 + m.x25 + m.x26
                        + m.x27 + m.x28 + m.x29, sense=minimize)

m.c2 = Constraint(expr= - m.x2 - m.x9 - m.x16 - m.x23 + m.x30 - m.x44 - m.x51 - m.x58 - m.x65 - m.x72 - m.x79 - m.x86
                        == 0)

m.c3 = Constraint(expr= - m.x3 - m.x10 - m.x17 - m.x24 + m.x31 - m.x45 - m.x52 - m.x59 - m.x66 - m.x73 - m.x80 - m.x87
                        == 0)

m.c4 = Constraint(expr= - m.x4 - m.x11 - m.x18 - m.x25 + m.x32 - m.x46 - m.x53 - m.x60 - m.x67 - m.x74 - m.x81 - m.x88
                        == 0)

m.c5 = Constraint(expr= - m.x5 - m.x12 - m.x19 - m.x26 + m.x33 - m.x47 - m.x54 - m.x61 - m.x68 - m.x75 - m.x82 - m.x89
                        == 0)

m.c6 = Constraint(expr= - m.x6 - m.x13 - m.x20 - m.x27 + m.x34 - m.x48 - m.x55 - m.x62 - m.x69 - m.x76 - m.x83 - m.x90
                        == 0)

m.c7 = Constraint(expr= - m.x7 - m.x14 - m.x21 - m.x28 - m.x49 - m.x56 - m.x63 - m.x70 - m.x77 - m.x84 - m.x91 == -95)

m.c8 = Constraint(expr= - m.x8 - m.x15 - m.x22 - m.x29 - m.x50 - m.x57 - m.x64 - m.x71 - m.x78 - m.x85 - m.x92 == -50)

m.c9 = Constraint(expr=   m.x30 - m.x37 - m.x44 - m.x45 - m.x46 - m.x47 - m.x48 - m.x49 - m.x50 == 0)

m.c10 = Constraint(expr=   m.x31 - m.x38 - m.x51 - m.x52 - m.x53 - m.x54 - m.x55 - m.x56 - m.x57 == 0)

m.c11 = Constraint(expr=   m.x32 - m.x39 - m.x58 - m.x59 - m.x60 - m.x61 - m.x62 - m.x63 - m.x64 == 0)

m.c12 = Constraint(expr=   m.x33 - m.x40 - m.x65 - m.x66 - m.x67 - m.x68 - m.x69 - m.x70 - m.x71 == 0)

m.c13 = Constraint(expr=   m.x34 - m.x41 - m.x72 - m.x73 - m.x74 - m.x75 - m.x76 - m.x77 - m.x78 == 0)

m.c14 = Constraint(expr= - m.x42 - m.x79 - m.x80 - m.x81 - m.x82 - m.x83 - m.x84 - m.x85 == -55)

m.c15 = Constraint(expr= - m.x43 - m.x86 - m.x87 - m.x88 - m.x89 - m.x90 - m.x91 - m.x92 == -80)

m.c16 = Constraint(expr=m.x30*m.x93 - (m.x44*m.x108 + m.x51*m.x111 + m.x58*m.x114 + m.x65*m.x117 + m.x72*m.x120)
                         - 4*m.x2 - 7*m.x9 - 7*m.x16 - 6*m.x23 - 809*m.x79 - 1052*m.x86 == 0)

m.c17 = Constraint(expr=m.x30*m.x94 - (m.x44*m.x109 + m.x51*m.x112 + m.x58*m.x115 + m.x65*m.x118 + m.x72*m.x121)
                         - 5*m.x2 - 8*m.x9 - 3*m.x16 - 4*m.x23 - 899*m.x79 - 229*m.x86 == 0)

m.c18 = Constraint(expr=m.x30*m.x95 - (m.x44*m.x110 + m.x51*m.x113 + m.x58*m.x116 + m.x65*m.x119 + m.x72*m.x122)
                         - 9*m.x2 - m.x9 - m.x16 - 9*m.x23 - 985*m.x79 - 783*m.x86 == 0)

m.c19 = Constraint(expr=m.x31*m.x96 - (m.x45*m.x108 + m.x52*m.x111 + m.x59*m.x114 + m.x66*m.x117 + m.x73*m.x120)
                         - 4*m.x3 - 7*m.x10 - 7*m.x17 - 6*m.x24 - 809*m.x80 - 1052*m.x87 == 0)

m.c20 = Constraint(expr=m.x31*m.x97 - (m.x45*m.x109 + m.x52*m.x112 + m.x59*m.x115 + m.x66*m.x118 + m.x73*m.x121)
                         - 5*m.x3 - 8*m.x10 - 3*m.x17 - 4*m.x24 - 899*m.x80 - 229*m.x87 == 0)

m.c21 = Constraint(expr=m.x31*m.x98 - (m.x45*m.x110 + m.x52*m.x113 + m.x59*m.x116 + m.x66*m.x119 + m.x73*m.x122)
                         - 9*m.x3 - m.x10 - m.x17 - 9*m.x24 - 985*m.x80 - 783*m.x87 == 0)

m.c22 = Constraint(expr=m.x32*m.x99 - (m.x46*m.x108 + m.x53*m.x111 + m.x60*m.x114 + m.x67*m.x117 + m.x74*m.x120)
                         - 4*m.x4 - 7*m.x11 - 7*m.x18 - 6*m.x25 - 809*m.x81 - 1052*m.x88 == 0)

m.c23 = Constraint(expr=m.x32*m.x100 - (m.x46*m.x109 + m.x53*m.x112 + m.x60*m.x115 + m.x67*m.x118 + m.x74*m.x121)
                         - 5*m.x4 - 8*m.x11 - 3*m.x18 - 4*m.x25 - 899*m.x81 - 229*m.x88 == 0)

m.c24 = Constraint(expr=m.x32*m.x101 - (m.x46*m.x110 + m.x53*m.x113 + m.x60*m.x116 + m.x67*m.x119 + m.x74*m.x122)
                         - 9*m.x4 - m.x11 - m.x18 - 9*m.x25 - 985*m.x81 - 783*m.x88 == 0)

m.c25 = Constraint(expr=m.x33*m.x102 - (m.x47*m.x108 + m.x54*m.x111 + m.x61*m.x114 + m.x68*m.x117 + m.x75*m.x120)
                         - 4*m.x5 - 7*m.x12 - 7*m.x19 - 6*m.x26 - 809*m.x82 - 1052*m.x89 == 0)

m.c26 = Constraint(expr=m.x33*m.x103 - (m.x47*m.x109 + m.x54*m.x112 + m.x61*m.x115 + m.x68*m.x118 + m.x75*m.x121)
                         - 5*m.x5 - 8*m.x12 - 3*m.x19 - 4*m.x26 - 899*m.x82 - 229*m.x89 == 0)

m.c27 = Constraint(expr=m.x33*m.x104 - (m.x47*m.x110 + m.x54*m.x113 + m.x61*m.x116 + m.x68*m.x119 + m.x75*m.x122)
                         - 9*m.x5 - m.x12 - m.x19 - 9*m.x26 - 985*m.x82 - 783*m.x89 == 0)

m.c28 = Constraint(expr=m.x34*m.x105 - (m.x48*m.x108 + m.x55*m.x111 + m.x62*m.x114 + m.x69*m.x117 + m.x76*m.x120)
                         - 4*m.x6 - 7*m.x13 - 7*m.x20 - 6*m.x27 - 809*m.x83 - 1052*m.x90 == 0)

m.c29 = Constraint(expr=m.x34*m.x106 - (m.x48*m.x109 + m.x55*m.x112 + m.x62*m.x115 + m.x69*m.x118 + m.x76*m.x121)
                         - 5*m.x6 - 8*m.x13 - 3*m.x20 - 4*m.x27 - 899*m.x83 - 229*m.x90 == 0)

m.c30 = Constraint(expr=m.x34*m.x107 - (m.x48*m.x110 + m.x55*m.x113 + m.x62*m.x116 + m.x69*m.x119 + m.x76*m.x122)
                         - 9*m.x6 - m.x13 - m.x20 - 9*m.x27 - 985*m.x83 - 783*m.x90 == 0)

m.c31 = Constraint(expr=-m.x30*(m.x108 - m.x93) == -702)

m.c32 = Constraint(expr=-m.x30*(m.x109 - m.x94) == -3294)

m.c33 = Constraint(expr=-m.x30*(m.x110 - m.x95) == -918)

m.c34 = Constraint(expr=-m.x31*(m.x111 - m.x96) == -102138)

m.c35 = Constraint(expr=-m.x31*(m.x112 - m.x97) == -32364)

m.c36 = Constraint(expr=-m.x31*(m.x113 - m.x98) == -2088)

m.c37 = Constraint(expr=-m.x32*(m.x114 - m.x99) == -118198)

m.c38 = Constraint(expr=-m.x32*(m.x115 - m.x100) == -36838)

m.c39 = Constraint(expr=-m.x32*(m.x116 - m.x101) == -113678)

m.c40 = Constraint(expr=-m.x33*(m.x117 - m.x102) == -8568)

m.c41 = Constraint(expr=-m.x33*(m.x118 - m.x103) == -44948)

m.c42 = Constraint(expr=-m.x33*(m.x119 - m.x104) == -19788)

m.c43 = Constraint(expr=-m.x34*(m.x120 - m.x105) == -82600)

m.c44 = Constraint(expr=-m.x34*(m.x121 - m.x106) == -4100)

m.c45 = Constraint(expr=-m.x34*(m.x122 - m.x107) == -90400)

m.c46 = Constraint(expr=   m.x93 <= 857)

m.c47 = Constraint(expr=   m.x94 <= 479)

m.c48 = Constraint(expr=   m.x95 <= 781)

m.c49 = Constraint(expr=   m.x96 <= 71)

m.c50 = Constraint(expr=   m.x97 <= 990)

m.c51 = Constraint(expr=   m.x98 <= 998)

m.c52 = Constraint(expr=   m.x99 <= 650)

m.c53 = Constraint(expr=   m.x100 <= 759)

m.c54 = Constraint(expr=   m.x101 <= 54)

m.c55 = Constraint(expr=   m.x102 <= 905)

m.c56 = Constraint(expr=   m.x103 <= 120)

m.c57 = Constraint(expr=   m.x104 <= 452)

m.c58 = Constraint(expr=   m.x105 <= 366)

m.c59 = Constraint(expr=   m.x106 <= 169)

m.c60 = Constraint(expr=   m.x107 <= 169)

m.c61 = Constraint(expr=   m.x108 <= 870)

m.c62 = Constraint(expr=   m.x109 <= 540)

m.c63 = Constraint(expr=   m.x110 <= 798)

m.c64 = Constraint(expr=   m.x111 <= 658)

m.c65 = Constraint(expr=   m.x112 <= 1176)

m.c66 = Constraint(expr=   m.x113 <= 1010)

m.c67 = Constraint(expr=   m.x114 <= 1173)

m.c68 = Constraint(expr=   m.x115 <= 922)

m.c69 = Constraint(expr=   m.x116 <= 557)

m.c70 = Constraint(expr=   m.x117 <= 1031)

m.c71 = Constraint(expr=   m.x118 <= 781)

m.c72 = Constraint(expr=   m.x119 <= 743)

m.c73 = Constraint(expr=   m.x120 <= 1192)

m.c74 = Constraint(expr=   m.x121 <= 210)

m.c75 = Constraint(expr=   m.x122 <= 1073)

m.c76 = Constraint(expr=-(m.x49*m.x108 + m.x56*m.x111 + m.x63*m.x114 + m.x70*m.x117 + m.x77*m.x120) - 4*m.x7 - 7*m.x14
                         - 7*m.x21 - 6*m.x28 - 809*m.x84 - 1052*m.x91 >= -22990)

m.c77 = Constraint(expr=-(m.x49*m.x109 + m.x56*m.x112 + m.x63*m.x115 + m.x70*m.x118 + m.x77*m.x121) - 5*m.x7 - 8*m.x14
                         - 3*m.x21 - 4*m.x28 - 899*m.x84 - 229*m.x91 >= -61940)

m.c78 = Constraint(expr=-(m.x49*m.x110 + m.x56*m.x113 + m.x63*m.x116 + m.x70*m.x119 + m.x77*m.x122) - 9*m.x7 - m.x14
                         - m.x21 - 9*m.x28 - 985*m.x84 - 783*m.x91 >= -8740)

m.c79 = Constraint(expr=-(m.x50*m.x108 + m.x57*m.x111 + m.x64*m.x114 + m.x71*m.x117 + m.x78*m.x120) - 4*m.x8 - 7*m.x15
                         - 7*m.x22 - 6*m.x29 - 809*m.x85 - 1052*m.x92 >= -30900)

m.c80 = Constraint(expr=-(m.x50*m.x109 + m.x57*m.x112 + m.x64*m.x115 + m.x71*m.x118 + m.x78*m.x121) - 5*m.x8 - 8*m.x15
                         - 3*m.x22 - 4*m.x29 - 899*m.x85 - 229*m.x92 >= -6700)

m.c81 = Constraint(expr=-(m.x50*m.x110 + m.x57*m.x113 + m.x64*m.x116 + m.x71*m.x119 + m.x78*m.x122) - 9*m.x8 - m.x15
                         - m.x22 - 9*m.x29 - 985*m.x85 - 783*m.x92 >= -37200)

m.c82 = Constraint(expr=   m.x30 <= 54)

m.c83 = Constraint(expr=   m.x31 <= 174)

m.c84 = Constraint(expr=   m.x32 <= 226)

m.c85 = Constraint(expr=   m.x33 <= 68)

m.c86 = Constraint(expr=   m.x34 <= 100)

m.c87 = Constraint(expr=   m.x35 <= 0)

m.c88 = Constraint(expr=   m.x36 <= 0)
