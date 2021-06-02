#  NLP written by GAMS Convert at 04/21/18 13:55:06
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         43       35        0        8        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        119      119        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        403      277      126        0
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
m.x75 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,1000000),initialize=0)

m.obj = Objective(expr=   m.x112 + m.x113 + m.x114 + m.x115 + m.x116 + m.x117 + m.x118, sense=minimize)

m.c2 = Constraint(expr= - m.x64 - m.x76 - m.x77 - m.x78 - m.x79 - m.x80 - m.x81 - m.x82 == -80)

m.c3 = Constraint(expr= - m.x65 - m.x83 - m.x84 - m.x85 - m.x86 - m.x87 - m.x88 - m.x89 == -450)

m.c4 = Constraint(expr= - m.x66 - m.x90 - m.x91 - m.x92 - m.x93 - m.x94 - m.x95 - m.x96 == -230)

m.c5 = Constraint(expr= - m.x67 - m.x97 - m.x98 - m.x99 - m.x100 - m.x101 - m.x102 - m.x103 == -90)

m.c6 = Constraint(expr= - m.x68 - m.x104 - m.x105 - m.x106 - m.x107 - m.x108 - m.x109 - m.x110 == -330)

m.c7 = Constraint(expr= - m.x15 - m.x22 - m.x29 - m.x36 - m.x43 - m.x50 - m.x57 - m.x76 - m.x83 - m.x90 - m.x97 - m.x104
                        + m.x112 == 0)

m.c8 = Constraint(expr= - m.x16 - m.x23 - m.x30 - m.x37 - m.x44 - m.x51 - m.x58 - m.x77 - m.x84 - m.x91 - m.x98 - m.x105
                        + m.x113 == 0)

m.c9 = Constraint(expr= - m.x17 - m.x24 - m.x31 - m.x38 - m.x45 - m.x52 - m.x59 - m.x78 - m.x85 - m.x92 - m.x99 - m.x106
                        + m.x114 == 0)

m.c10 = Constraint(expr= - m.x18 - m.x25 - m.x32 - m.x39 - m.x46 - m.x53 - m.x60 - m.x79 - m.x86 - m.x93 - m.x100
                         - m.x107 + m.x115 == 0)

m.c11 = Constraint(expr= - m.x19 - m.x26 - m.x33 - m.x40 - m.x47 - m.x54 - m.x61 - m.x80 - m.x87 - m.x94 - m.x101
                         - m.x108 + m.x116 == 0)

m.c12 = Constraint(expr= - m.x20 - m.x27 - m.x34 - m.x41 - m.x48 - m.x55 - m.x62 - m.x81 - m.x88 - m.x95 - m.x102
                         - m.x109 + m.x117 == 0)

m.c13 = Constraint(expr= - m.x21 - m.x28 - m.x35 - m.x42 - m.x49 - m.x56 - m.x63 - m.x82 - m.x89 - m.x96 - m.x103
                         - m.x110 + m.x118 == 0)

m.c14 = Constraint(expr= - m.x15 - m.x16 - m.x17 - m.x18 - m.x19 - m.x20 - m.x21 - m.x69 + m.x112 == 0)

m.c15 = Constraint(expr= - m.x22 - m.x23 - m.x24 - m.x25 - m.x26 - m.x27 - m.x28 - m.x70 + m.x113 == 0)

m.c16 = Constraint(expr= - m.x29 - m.x30 - m.x31 - m.x32 - m.x33 - m.x34 - m.x35 - m.x71 + m.x114 == 0)

m.c17 = Constraint(expr= - m.x36 - m.x37 - m.x38 - m.x39 - m.x40 - m.x41 - m.x42 - m.x72 + m.x115 == 0)

m.c18 = Constraint(expr= - m.x43 - m.x44 - m.x45 - m.x46 - m.x47 - m.x48 - m.x49 - m.x73 + m.x116 == 0)

m.c19 = Constraint(expr= - m.x50 - m.x51 - m.x52 - m.x53 - m.x54 - m.x55 - m.x56 - m.x74 + m.x117 == 0)

m.c20 = Constraint(expr= - m.x57 - m.x58 - m.x59 - m.x60 - m.x61 - m.x62 - m.x63 - m.x75 + m.x118 == 0)

m.c21 = Constraint(expr= - m.x64 - m.x65 - m.x66 - m.x67 - m.x68 - m.x69 - m.x70 - m.x71 - m.x72 - m.x73 - m.x74 - m.x75
                         + m.x111 == 0)

m.c22 = Constraint(expr=m.x15*m.x8 + m.x22*m.x9 + m.x29*m.x10 + m.x36*m.x11 + m.x43*m.x12 + m.x50*m.x13 + m.x57*m.x14 - 
                        m.x112*m.x1 + 12*m.x76 + 50*m.x83 + 500*m.x90 + 400*m.x97 + 120*m.x104 == 0)

m.c23 = Constraint(expr=m.x16*m.x8 + m.x23*m.x9 + m.x30*m.x10 + m.x37*m.x11 + m.x44*m.x12 + m.x51*m.x13 + m.x58*m.x14 - 
                        m.x113*m.x2 + 12*m.x77 + 50*m.x84 + 500*m.x91 + 400*m.x98 + 120*m.x105 == 0)

m.c24 = Constraint(expr=m.x17*m.x8 + m.x24*m.x9 + m.x31*m.x10 + m.x38*m.x11 + m.x45*m.x12 + m.x52*m.x13 + m.x59*m.x14 - 
                        m.x114*m.x3 + 12*m.x78 + 50*m.x85 + 500*m.x92 + 400*m.x99 + 120*m.x106 == 0)

m.c25 = Constraint(expr=m.x18*m.x8 + m.x25*m.x9 + m.x32*m.x10 + m.x39*m.x11 + m.x46*m.x12 + m.x53*m.x13 + m.x60*m.x14 - 
                        m.x115*m.x4 + 12*m.x79 + 50*m.x86 + 500*m.x93 + 400*m.x100 + 120*m.x107 == 0)

m.c26 = Constraint(expr=m.x19*m.x8 + m.x26*m.x9 + m.x33*m.x10 + m.x40*m.x11 + m.x47*m.x12 + m.x54*m.x13 + m.x61*m.x14 - 
                        m.x116*m.x5 + 12*m.x80 + 50*m.x87 + 500*m.x94 + 400*m.x101 + 120*m.x108 == 0)

m.c27 = Constraint(expr=m.x20*m.x8 + m.x27*m.x9 + m.x34*m.x10 + m.x41*m.x11 + m.x48*m.x12 + m.x55*m.x13 + m.x62*m.x14 - 
                        m.x117*m.x6 + 12*m.x81 + 50*m.x88 + 500*m.x95 + 400*m.x102 + 120*m.x109 == 0)

m.c28 = Constraint(expr=m.x21*m.x8 + m.x28*m.x9 + m.x35*m.x10 + m.x42*m.x11 + m.x49*m.x12 + m.x56*m.x13 + m.x63*m.x14 - 
                        m.x118*m.x7 + 12*m.x82 + 50*m.x89 + 500*m.x96 + 400*m.x103 + 120*m.x110 == 0)

m.c29 = Constraint(expr=   m.x1 <= 400)

m.c30 = Constraint(expr=   m.x2 <= 100)

m.c31 = Constraint(expr=   m.x3 <= 50)

m.c32 = Constraint(expr=   m.x4 <= 570)

m.c33 = Constraint(expr=   m.x5 <= 100)

m.c34 = Constraint(expr=   m.x6 <= 30)

m.c35 = Constraint(expr=   m.x7 <= 640)

m.c36 = Constraint(expr= - 0.9*m.x1 + m.x8 == 0)

m.c37 = Constraint(expr= - 0.6*m.x2 + m.x9 == 0)

m.c38 = Constraint(expr= - 0.15*m.x3 + m.x10 == 0)

m.c39 = Constraint(expr= - 0.26*m.x4 + m.x11 == 0)

m.c40 = Constraint(expr= - 0.1*m.x5 + m.x12 == 0)

m.c41 = Constraint(expr= - 0.4*m.x6 + m.x13 == 0)

m.c42 = Constraint(expr= - 0.3*m.x7 + m.x14 == 0)

m.c43 = Constraint(expr=m.x69*m.x8 + m.x70*m.x9 + m.x71*m.x10 + m.x72*m.x11 + m.x73*m.x12 + m.x74*m.x13 + m.x75*m.x14
                         + 12*m.x64 + 50*m.x65 + 500*m.x66 + 400*m.x67 + 120*m.x68 - 4*m.x111 <= 0)
