#  NLP written by GAMS Convert at 04/21/18 13:55:19
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        136       63       18       55        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        126      126        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        828      372      456        0
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

m.obj = Objective(expr=   m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13 + m.x14
                        + m.x15, sense=minimize)

m.c2 = Constraint(expr= - m.x2 - m.x9 + m.x16 - m.x30 - m.x37 - m.x44 - m.x51 - m.x58 - m.x65 - m.x72 == 0)

m.c3 = Constraint(expr= - m.x3 - m.x10 + m.x17 - m.x31 - m.x38 - m.x45 - m.x52 - m.x59 - m.x66 - m.x73 == 0)

m.c4 = Constraint(expr= - m.x4 - m.x11 + m.x18 - m.x32 - m.x39 - m.x46 - m.x53 - m.x60 - m.x67 - m.x74 == 0)

m.c5 = Constraint(expr= - m.x5 - m.x12 + m.x19 - m.x33 - m.x40 - m.x47 - m.x54 - m.x61 - m.x68 - m.x75 == 0)

m.c6 = Constraint(expr= - m.x6 - m.x13 - m.x34 - m.x41 - m.x48 - m.x55 - m.x62 - m.x69 - m.x76 == -20)

m.c7 = Constraint(expr= - m.x7 - m.x14 - m.x35 - m.x42 - m.x49 - m.x56 - m.x63 - m.x70 - m.x77 == -60)

m.c8 = Constraint(expr= - m.x8 - m.x15 - m.x36 - m.x43 - m.x50 - m.x57 - m.x64 - m.x71 - m.x78 == -70)

m.c9 = Constraint(expr=   m.x16 - m.x23 - m.x30 - m.x31 - m.x32 - m.x33 - m.x34 - m.x35 - m.x36 == 0)

m.c10 = Constraint(expr=   m.x17 - m.x24 - m.x37 - m.x38 - m.x39 - m.x40 - m.x41 - m.x42 - m.x43 == 0)

m.c11 = Constraint(expr=   m.x18 - m.x25 - m.x44 - m.x45 - m.x46 - m.x47 - m.x48 - m.x49 - m.x50 == 0)

m.c12 = Constraint(expr=   m.x19 - m.x26 - m.x51 - m.x52 - m.x53 - m.x54 - m.x55 - m.x56 - m.x57 == 0)

m.c13 = Constraint(expr= - m.x27 - m.x58 - m.x59 - m.x60 - m.x61 - m.x62 - m.x63 - m.x64 == -30)

m.c14 = Constraint(expr= - m.x28 - m.x65 - m.x66 - m.x67 - m.x68 - m.x69 - m.x70 - m.x71 == -70)

m.c15 = Constraint(expr= - m.x29 - m.x72 - m.x73 - m.x74 - m.x75 - m.x76 - m.x77 - m.x78 == -40)

m.c16 = Constraint(expr=m.x16*m.x79 - (m.x30*m.x103 + m.x37*m.x109 + m.x44*m.x115 + m.x51*m.x121) - 15*m.x9 - 300*m.x58
                         - 400*m.x65 - 90*m.x72 == 0)

m.c17 = Constraint(expr=m.x16*m.x80 - (m.x30*m.x104 + m.x37*m.x110 + m.x44*m.x116 + m.x51*m.x122) - 25*m.x2 - 140*m.x58
                         - 155*m.x65 - 100*m.x72 == 0)

m.c18 = Constraint(expr=m.x16*m.x81 - (m.x30*m.x105 + m.x37*m.x111 + m.x44*m.x117 + m.x51*m.x123) - 2*m.x2 - 200*m.x58
                         - 180*m.x65 - 300*m.x72 == 0)

m.c19 = Constraint(expr=m.x16*m.x82 - (m.x30*m.x106 + m.x37*m.x112 + m.x44*m.x118 + m.x51*m.x124) - 4*m.x2 - 9*m.x9
                         - 170*m.x58 - 220*m.x65 - 220*m.x72 == 0)

m.c20 = Constraint(expr=m.x16*m.x83 - (m.x30*m.x107 + m.x37*m.x113 + m.x44*m.x119 + m.x51*m.x125) - 3*m.x9 - 130*m.x58
                         - 110*m.x65 - 80*m.x72 == 0)

m.c21 = Constraint(expr=m.x16*m.x84 - (m.x30*m.x108 + m.x37*m.x114 + m.x44*m.x120 + m.x51*m.x126) - 2*m.x2 - 200*m.x58
                         - 190*m.x65 - 115*m.x72 == 0)

m.c22 = Constraint(expr=m.x17*m.x85 - (m.x31*m.x103 + m.x38*m.x109 + m.x45*m.x115 + m.x52*m.x121) - 15*m.x10 - 300*m.x59
                         - 400*m.x66 - 90*m.x73 == 0)

m.c23 = Constraint(expr=m.x17*m.x86 - (m.x31*m.x104 + m.x38*m.x110 + m.x45*m.x116 + m.x52*m.x122) - 25*m.x3 - 140*m.x59
                         - 155*m.x66 - 100*m.x73 == 0)

m.c24 = Constraint(expr=m.x17*m.x87 - (m.x31*m.x105 + m.x38*m.x111 + m.x45*m.x117 + m.x52*m.x123) - 2*m.x3 - 200*m.x59
                         - 180*m.x66 - 300*m.x73 == 0)

m.c25 = Constraint(expr=m.x17*m.x88 - (m.x31*m.x106 + m.x38*m.x112 + m.x45*m.x118 + m.x52*m.x124) - 4*m.x3 - 9*m.x10
                         - 170*m.x59 - 220*m.x66 - 220*m.x73 == 0)

m.c26 = Constraint(expr=m.x17*m.x89 - (m.x31*m.x107 + m.x38*m.x113 + m.x45*m.x119 + m.x52*m.x125) - 3*m.x10 - 130*m.x59
                         - 110*m.x66 - 80*m.x73 == 0)

m.c27 = Constraint(expr=m.x17*m.x90 - (m.x31*m.x108 + m.x38*m.x114 + m.x45*m.x120 + m.x52*m.x126) - 2*m.x3 - 200*m.x59
                         - 190*m.x66 - 115*m.x73 == 0)

m.c28 = Constraint(expr=m.x18*m.x91 - (m.x32*m.x103 + m.x39*m.x109 + m.x46*m.x115 + m.x53*m.x121) - 15*m.x11 - 300*m.x60
                         - 400*m.x67 - 90*m.x74 == 0)

m.c29 = Constraint(expr=m.x18*m.x92 - (m.x32*m.x104 + m.x39*m.x110 + m.x46*m.x116 + m.x53*m.x122) - 25*m.x4 - 140*m.x60
                         - 155*m.x67 - 100*m.x74 == 0)

m.c30 = Constraint(expr=m.x18*m.x93 - (m.x32*m.x105 + m.x39*m.x111 + m.x46*m.x117 + m.x53*m.x123) - 2*m.x4 - 200*m.x60
                         - 180*m.x67 - 300*m.x74 == 0)

m.c31 = Constraint(expr=m.x18*m.x94 - (m.x32*m.x106 + m.x39*m.x112 + m.x46*m.x118 + m.x53*m.x124) - 4*m.x4 - 9*m.x11
                         - 170*m.x60 - 220*m.x67 - 220*m.x74 == 0)

m.c32 = Constraint(expr=m.x18*m.x95 - (m.x32*m.x107 + m.x39*m.x113 + m.x46*m.x119 + m.x53*m.x125) - 3*m.x11 - 130*m.x60
                         - 110*m.x67 - 80*m.x74 == 0)

m.c33 = Constraint(expr=m.x18*m.x96 - (m.x32*m.x108 + m.x39*m.x114 + m.x46*m.x120 + m.x53*m.x126) - 2*m.x4 - 200*m.x60
                         - 190*m.x67 - 115*m.x74 == 0)

m.c34 = Constraint(expr=m.x19*m.x97 - (m.x33*m.x103 + m.x40*m.x109 + m.x47*m.x115 + m.x54*m.x121) - 15*m.x12 - 300*m.x61
                         - 400*m.x68 - 90*m.x75 == 0)

m.c35 = Constraint(expr=m.x19*m.x98 - (m.x33*m.x104 + m.x40*m.x110 + m.x47*m.x116 + m.x54*m.x122) - 25*m.x5 - 140*m.x61
                         - 155*m.x68 - 100*m.x75 == 0)

m.c36 = Constraint(expr=m.x19*m.x99 - (m.x33*m.x105 + m.x40*m.x111 + m.x47*m.x117 + m.x54*m.x123) - 2*m.x5 - 200*m.x61
                         - 180*m.x68 - 300*m.x75 == 0)

m.c37 = Constraint(expr=m.x19*m.x100 - (m.x33*m.x106 + m.x40*m.x112 + m.x47*m.x118 + m.x54*m.x124) - 4*m.x5 - 9*m.x12
                         - 170*m.x61 - 220*m.x68 - 220*m.x75 == 0)

m.c38 = Constraint(expr=m.x19*m.x101 - (m.x33*m.x107 + m.x40*m.x113 + m.x47*m.x119 + m.x54*m.x125) - 3*m.x12 - 130*m.x61
                         - 110*m.x68 - 80*m.x75 == 0)

m.c39 = Constraint(expr=m.x19*m.x102 - (m.x33*m.x108 + m.x40*m.x114 + m.x47*m.x120 + m.x54*m.x126) - 2*m.x5 - 200*m.x61
                         - 190*m.x68 - 115*m.x75 == 0)

m.c40 = Constraint(expr=-m.x16*(m.x103 - m.x79) == -10560)

m.c41 = Constraint(expr=-m.x16*(m.x104 - m.x80) == -4320)

m.c42 = Constraint(expr=-m.x16*(m.x105 - m.x81) == -4560)

m.c43 = Constraint(expr=-m.x16*(m.x106 - m.x82) == -12000)

m.c44 = Constraint(expr=-m.x16*(m.x107 - m.x83) == -3960)

m.c45 = Constraint(expr=-m.x16*(m.x108 - m.x84) == -6000)

m.c46 = Constraint(expr=-m.x17*(m.x109 - m.x85) == -2400)

m.c47 = Constraint(expr=-m.x17*(m.x110 - m.x86) == -3400)

m.c48 = Constraint(expr=-m.x17*(m.x111 - m.x87) == -1150)

m.c49 = Constraint(expr=-m.x17*(m.x112 - m.x88) == -5000)

m.c50 = Constraint(expr=-m.x17*(m.x113 - m.x89) == -2000)

m.c51 = Constraint(expr=-m.x17*(m.x114 - m.x90) == -5000)

m.c52 = Constraint(expr=-m.x18*(m.x115 - m.x91) == -7200)

m.c53 = Constraint(expr=-m.x18*(m.x116 - m.x92) == -2400)

m.c54 = Constraint(expr=-m.x18*(m.x117 - m.x93) == -2880)

m.c55 = Constraint(expr=-m.x18*(m.x118 - m.x94) == -8000)

m.c56 = Constraint(expr=-m.x18*(m.x119 - m.x95) == -4000)

m.c57 = Constraint(expr=-m.x18*(m.x120 - m.x96) == -2400)

m.c58 = Constraint(expr=-m.x19*(m.x121 - m.x97) == -9000)

m.c59 = Constraint(expr=-m.x19*(m.x122 - m.x98) == -14130)

m.c60 = Constraint(expr=-m.x19*(m.x123 - m.x99) == -11700)

m.c61 = Constraint(expr=-m.x19*(m.x124 - m.x100) == -9000)

m.c62 = Constraint(expr=-m.x19*(m.x125 - m.x101) == -5400)

m.c63 = Constraint(expr=-m.x19*(m.x126 - m.x102) == -18000)

m.c64 = Constraint(expr=   m.x79 <= 112)

m.c65 = Constraint(expr=   m.x80 <= 54)

m.c66 = Constraint(expr=   m.x81 <= 12)

m.c67 = Constraint(expr=   m.x82 <= 134)

m.c68 = Constraint(expr=   m.x83 <= 12)

m.c69 = Constraint(expr=   m.x84 <= 30)

m.c70 = Constraint(expr=   m.x85 <= 32)

m.c71 = Constraint(expr=   m.x86 <= 12)

m.c72 = Constraint(expr=   m.x87 <= 47)

m.c73 = Constraint(expr=   m.x88 <= 56)

m.c74 = Constraint(expr=   m.x89 <= 40)

m.c75 = Constraint(expr=   m.x90 <= 100)

m.c76 = Constraint(expr=   m.x91 <= 10)

m.c77 = Constraint(expr=   m.x92 <= 80)

m.c78 = Constraint(expr=   m.x93 <= 54)

m.c79 = Constraint(expr=   m.x94 <= 39)

m.c80 = Constraint(expr=   m.x95 <= 80)

m.c81 = Constraint(expr=   m.x96 <= 60)

m.c82 = Constraint(expr=   m.x97 <= 45)

m.c83 = Constraint(expr=   m.x98 <= 93)

m.c84 = Constraint(expr=   m.x99 <= 70)

m.c85 = Constraint(expr=   m.x100 <= 177)

m.c86 = Constraint(expr=   m.x101 <= 20)

m.c87 = Constraint(expr=   m.x102 <= 20)

m.c88 = Constraint(expr=   m.x103 <= 200)

m.c89 = Constraint(expr=   m.x104 <= 90)

m.c90 = Constraint(expr=   m.x105 <= 50)

m.c91 = Constraint(expr=   m.x106 <= 234)

m.c92 = Constraint(expr=   m.x107 <= 45)

m.c93 = Constraint(expr=   m.x108 <= 80)

m.c94 = Constraint(expr=   m.x109 <= 80)

m.c95 = Constraint(expr=   m.x110 <= 80)

m.c96 = Constraint(expr=   m.x111 <= 70)

m.c97 = Constraint(expr=   m.x112 <= 156)

m.c98 = Constraint(expr=   m.x113 <= 80)

m.c99 = Constraint(expr=   m.x114 <= 200)

m.c100 = Constraint(expr=   m.x115 <= 100)

m.c101 = Constraint(expr=   m.x116 <= 110)

m.c102 = Constraint(expr=   m.x117 <= 90)

m.c103 = Constraint(expr=   m.x118 <= 139)

m.c104 = Constraint(expr=   m.x119 <= 130)

m.c105 = Constraint(expr=   m.x120 <= 90)

m.c106 = Constraint(expr=   m.x121 <= 145)

m.c107 = Constraint(expr=   m.x122 <= 250)

m.c108 = Constraint(expr=   m.x123 <= 200)

m.c109 = Constraint(expr=   m.x124 <= 277)

m.c110 = Constraint(expr=   m.x125 <= 80)

m.c111 = Constraint(expr=   m.x126 <= 220)

m.c112 = Constraint(expr=-(m.x34*m.x103 + m.x41*m.x109 + m.x48*m.x115 + m.x55*m.x121) - 15*m.x13 - 300*m.x62 - 400*m.x69
                          - 90*m.x76 >= -4000)

m.c113 = Constraint(expr=-(m.x34*m.x104 + m.x41*m.x110 + m.x48*m.x116 + m.x55*m.x122) - 25*m.x6 - 140*m.x62 - 155*m.x69
                          - 100*m.x76 >= -800)

m.c114 = Constraint(expr=-(m.x34*m.x105 + m.x41*m.x111 + m.x48*m.x117 + m.x55*m.x123) - 2*m.x6 - 200*m.x62 - 180*m.x69
                          - 300*m.x76 >= -600)

m.c115 = Constraint(expr=-(m.x34*m.x106 + m.x41*m.x112 + m.x48*m.x118 + m.x55*m.x124) - 4*m.x6 - 9*m.x13 - 170*m.x62
                          - 220*m.x69 - 220*m.x76 >= -1600)

m.c116 = Constraint(expr=-(m.x34*m.x107 + m.x41*m.x113 + m.x48*m.x119 + m.x55*m.x125) - 3*m.x13 - 130*m.x62 - 110*m.x69
                          - 80*m.x76 >= -600)

m.c117 = Constraint(expr=-(m.x34*m.x108 + m.x41*m.x114 + m.x48*m.x120 + m.x55*m.x126) - 2*m.x6 - 200*m.x62 - 190*m.x69
                          - 115*m.x76 >= -2000)

m.c118 = Constraint(expr=-(m.x35*m.x103 + m.x42*m.x109 + m.x49*m.x115 + m.x56*m.x121) - 15*m.x14 - 300*m.x63 - 400*m.x70
                          - 90*m.x77 >= -18000)

m.c119 = Constraint(expr=-(m.x35*m.x104 + m.x42*m.x110 + m.x49*m.x116 + m.x56*m.x122) - 25*m.x7 - 140*m.x63 - 155*m.x70
                          - 100*m.x77 >= -3300)

m.c120 = Constraint(expr=-(m.x35*m.x105 + m.x42*m.x111 + m.x49*m.x117 + m.x56*m.x123) - 2*m.x7 - 200*m.x63 - 180*m.x70
                          - 300*m.x77 >= -4800)

m.c121 = Constraint(expr=-(m.x35*m.x106 + m.x42*m.x112 + m.x49*m.x118 + m.x56*m.x124) - 4*m.x7 - 9*m.x14 - 170*m.x63
                          - 220*m.x70 - 220*m.x77 >= -7200)

m.c122 = Constraint(expr=-(m.x35*m.x107 + m.x42*m.x113 + m.x49*m.x119 + m.x56*m.x125) - 3*m.x14 - 130*m.x63 - 110*m.x70
                          - 80*m.x77 >= -3600)

m.c123 = Constraint(expr=-(m.x35*m.x108 + m.x42*m.x114 + m.x49*m.x120 + m.x56*m.x126) - 2*m.x7 - 200*m.x63 - 190*m.x70
                          - 115*m.x77 >= -5400)

m.c124 = Constraint(expr=-(m.x36*m.x103 + m.x43*m.x109 + m.x50*m.x115 + m.x57*m.x121) - 15*m.x15 - 300*m.x64 - 400*m.x71
                          - 90*m.x78 >= -1400)

m.c125 = Constraint(expr=-(m.x36*m.x104 + m.x43*m.x110 + m.x50*m.x116 + m.x57*m.x122) - 25*m.x8 - 140*m.x64 - 155*m.x71
                          - 100*m.x78 >= -1750)

m.c126 = Constraint(expr=-(m.x36*m.x105 + m.x43*m.x111 + m.x50*m.x117 + m.x57*m.x123) - 2*m.x8 - 200*m.x64 - 180*m.x71
                          - 300*m.x78 >= -7000)

m.c127 = Constraint(expr=-(m.x36*m.x106 + m.x43*m.x112 + m.x50*m.x118 + m.x57*m.x124) - 4*m.x8 - 9*m.x15 - 170*m.x64
                          - 220*m.x71 - 220*m.x78 >= -1400)

m.c128 = Constraint(expr=-(m.x36*m.x107 + m.x43*m.x113 + m.x50*m.x119 + m.x57*m.x125) - 3*m.x15 - 130*m.x64 - 110*m.x71
                          - 80*m.x78 >= -2800)

m.c129 = Constraint(expr=-(m.x36*m.x108 + m.x43*m.x114 + m.x50*m.x120 + m.x57*m.x126) - 2*m.x8 - 200*m.x64 - 190*m.x71
                          - 115*m.x78 >= -3150)

m.c130 = Constraint(expr=   m.x16 <= 120)

m.c131 = Constraint(expr=   m.x17 <= 50)

m.c132 = Constraint(expr=   m.x18 <= 80)

m.c133 = Constraint(expr=   m.x19 <= 90)

m.c134 = Constraint(expr=   m.x20 <= 0)

m.c135 = Constraint(expr=   m.x21 <= 0)

m.c136 = Constraint(expr=   m.x22 <= 0)
