#  NLP written by GAMS Convert at 04/21/18 13:51:47
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         93       93        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        127      127        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        669      132      537        0
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
m.x22 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x23 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x24 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x25 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x26 = Var(within=Reals,bounds=(0,10),initialize=0.2)
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
m.x37 = Var(within=Reals,bounds=(0,1000),initialize=100)
m.x38 = Var(within=Reals,bounds=(0,1000),initialize=100)
m.x39 = Var(within=Reals,bounds=(0,1000),initialize=100)
m.x40 = Var(within=Reals,bounds=(0,1000),initialize=100)
m.x41 = Var(within=Reals,bounds=(0,1000),initialize=100)
m.x42 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x43 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x44 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x45 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x46 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x47 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x48 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x49 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x50 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x51 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x52 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x53 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x54 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x55 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x56 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x57 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x58 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x59 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x60 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x61 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x62 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x63 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x64 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x65 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x66 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x67 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x68 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x69 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x70 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x71 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x72 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x73 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x74 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x75 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x76 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x77 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x78 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x79 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x80 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x81 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x82 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x83 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x84 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x85 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x86 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x87 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x88 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x89 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x90 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x91 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x92 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x93 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x94 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x95 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x96 = Var(within=Reals,bounds=(0,1000),initialize=50)
m.x97 = Var(within=Reals,bounds=(0,1000),initialize=100)
m.x98 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x99 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x100 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x101 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x102 = Var(within=Reals,bounds=(0,10),initialize=0.2)
m.x103 = Var(within=Reals,bounds=(0,10000),initialize=1)
m.x104 = Var(within=Reals,bounds=(0,10000),initialize=1)
m.x105 = Var(within=Reals,bounds=(0,10000),initialize=1)
m.x106 = Var(within=Reals,bounds=(0,10000),initialize=1)
m.x107 = Var(within=Reals,bounds=(0,10000),initialize=1)
m.x108 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,10000),initialize=0)

m.obj = Objective(expr=-m.x99/m.x101, sense=minimize)

m.c2 = Constraint(expr= - m.x2 - m.x3 - m.x4 - m.x5 - m.x6 == -100)

m.c3 = Constraint(expr= - m.x2 + m.x7 - m.x67 - m.x72 - m.x77 - m.x82 - m.x87 == 0)

m.c4 = Constraint(expr= - m.x3 + m.x8 - m.x68 - m.x73 - m.x78 - m.x83 - m.x88 == 0)

m.c5 = Constraint(expr= - m.x4 + m.x9 - m.x69 - m.x74 - m.x79 - m.x84 - m.x89 == 0)

m.c6 = Constraint(expr= - m.x5 + m.x10 - m.x70 - m.x75 - m.x80 - m.x85 - m.x90 == 0)

m.c7 = Constraint(expr= - m.x6 + m.x11 - m.x71 - m.x76 - m.x81 - m.x86 - m.x91 == 0)

m.c8 = Constraint(expr=m.x12*m.x7 - (m.x42*m.x67 + m.x47*m.x72 + m.x52*m.x77 + m.x57*m.x82 + m.x62*m.x87) - 6*m.x2 == 0)

m.c9 = Constraint(expr=m.x13*m.x7 - (m.x43*m.x67 + m.x48*m.x72 + m.x53*m.x77 + m.x58*m.x82 + m.x63*m.x87) == 0)

m.c10 = Constraint(expr=m.x14*m.x7 - (m.x44*m.x67 + m.x49*m.x72 + m.x54*m.x77 + m.x59*m.x82 + m.x64*m.x87) == 0)

m.c11 = Constraint(expr=m.x15*m.x7 - (m.x45*m.x67 + m.x50*m.x72 + m.x55*m.x77 + m.x60*m.x82 + m.x65*m.x87) - 0.6*m.x2
                         == 0)

m.c12 = Constraint(expr=m.x16*m.x7 - (m.x46*m.x67 + m.x51*m.x72 + m.x56*m.x77 + m.x61*m.x82 + m.x66*m.x87) == 0)

m.c13 = Constraint(expr=m.x17*m.x8 - (m.x42*m.x68 + m.x47*m.x73 + m.x52*m.x78 + m.x57*m.x83 + m.x62*m.x88) - 6*m.x3
                         == 0)

m.c14 = Constraint(expr=m.x18*m.x8 - (m.x43*m.x68 + m.x48*m.x73 + m.x53*m.x78 + m.x58*m.x83 + m.x63*m.x88) == 0)

m.c15 = Constraint(expr=m.x19*m.x8 - (m.x44*m.x68 + m.x49*m.x73 + m.x54*m.x78 + m.x59*m.x83 + m.x64*m.x88) == 0)

m.c16 = Constraint(expr=m.x20*m.x8 - (m.x45*m.x68 + m.x50*m.x73 + m.x55*m.x78 + m.x60*m.x83 + m.x65*m.x88) - 0.6*m.x3
                         == 0)

m.c17 = Constraint(expr=m.x21*m.x8 - (m.x46*m.x68 + m.x51*m.x73 + m.x56*m.x78 + m.x61*m.x83 + m.x66*m.x88) == 0)

m.c18 = Constraint(expr=m.x22*m.x9 - (m.x42*m.x69 + m.x47*m.x74 + m.x52*m.x79 + m.x57*m.x84 + m.x62*m.x89) - 6*m.x4
                         == 0)

m.c19 = Constraint(expr=m.x23*m.x9 - (m.x43*m.x69 + m.x48*m.x74 + m.x53*m.x79 + m.x58*m.x84 + m.x63*m.x89) == 0)

m.c20 = Constraint(expr=m.x24*m.x9 - (m.x44*m.x69 + m.x49*m.x74 + m.x54*m.x79 + m.x59*m.x84 + m.x64*m.x89) == 0)

m.c21 = Constraint(expr=m.x25*m.x9 - (m.x45*m.x69 + m.x50*m.x74 + m.x55*m.x79 + m.x60*m.x84 + m.x65*m.x89) - 0.6*m.x4
                         == 0)

m.c22 = Constraint(expr=m.x26*m.x9 - (m.x46*m.x69 + m.x51*m.x74 + m.x56*m.x79 + m.x61*m.x84 + m.x66*m.x89) == 0)

m.c23 = Constraint(expr=m.x27*m.x10 - (m.x42*m.x70 + m.x47*m.x75 + m.x52*m.x80 + m.x57*m.x85 + m.x62*m.x90) - 6*m.x5
                         == 0)

m.c24 = Constraint(expr=m.x28*m.x10 - (m.x43*m.x70 + m.x48*m.x75 + m.x53*m.x80 + m.x58*m.x85 + m.x63*m.x90) == 0)

m.c25 = Constraint(expr=m.x29*m.x10 - (m.x44*m.x70 + m.x49*m.x75 + m.x54*m.x80 + m.x59*m.x85 + m.x64*m.x90) == 0)

m.c26 = Constraint(expr=m.x30*m.x10 - (m.x45*m.x70 + m.x50*m.x75 + m.x55*m.x80 + m.x60*m.x85 + m.x65*m.x90) - 0.6*m.x5
                         == 0)

m.c27 = Constraint(expr=m.x31*m.x10 - (m.x46*m.x70 + m.x51*m.x75 + m.x56*m.x80 + m.x61*m.x85 + m.x66*m.x90) == 0)

m.c28 = Constraint(expr=m.x32*m.x11 - (m.x42*m.x71 + m.x47*m.x76 + m.x52*m.x81 + m.x57*m.x86 + m.x62*m.x91) - 6*m.x6
                         == 0)

m.c29 = Constraint(expr=m.x33*m.x11 - (m.x43*m.x71 + m.x48*m.x76 + m.x53*m.x81 + m.x58*m.x86 + m.x63*m.x91) == 0)

m.c30 = Constraint(expr=m.x34*m.x11 - (m.x44*m.x71 + m.x49*m.x76 + m.x54*m.x81 + m.x59*m.x86 + m.x64*m.x91) == 0)

m.c31 = Constraint(expr=m.x35*m.x11 - (m.x45*m.x71 + m.x50*m.x76 + m.x55*m.x81 + m.x60*m.x86 + m.x65*m.x91) - 0.6*m.x6
                         == 0)

m.c32 = Constraint(expr=m.x36*m.x11 - (m.x46*m.x71 + m.x51*m.x76 + m.x56*m.x81 + m.x61*m.x86 + m.x66*m.x91) == 0)

m.c33 = Constraint(expr= - m.x7 + m.x37 == 0)

m.c34 = Constraint(expr= - m.x8 + m.x38 == 0)

m.c35 = Constraint(expr= - m.x9 + m.x39 == 0)

m.c36 = Constraint(expr= - m.x10 + m.x40 == 0)

m.c37 = Constraint(expr= - m.x11 + m.x41 == 0)

m.c38 = Constraint(expr=m.x42*m.x37 - (m.x12*m.x7 + m.x103*(-m.x108 - m.x110)) == 0)

m.c39 = Constraint(expr=m.x43*m.x37 - (m.x13*m.x7 + m.x103*(0.5*m.x108 - m.x109 - m.x111)) == 0)

m.c40 = Constraint(expr=m.x44*m.x37 - (m.x14*m.x7 + m.x103*m.x109) == 0)

m.c41 = Constraint(expr=m.x45*m.x37 - (m.x15*m.x7 + m.x103*m.x110) == 0)

m.c42 = Constraint(expr=m.x46*m.x37 - (m.x16*m.x7 + m.x103*m.x111) == 0)

m.c43 = Constraint(expr=m.x47*m.x38 - (m.x17*m.x8 + m.x104*(-m.x112 - m.x114)) == 0)

m.c44 = Constraint(expr=m.x48*m.x38 - (m.x18*m.x8 + m.x104*(0.5*m.x112 - m.x113 - m.x115)) == 0)

m.c45 = Constraint(expr=m.x49*m.x38 - (m.x19*m.x8 + m.x104*m.x113) == 0)

m.c46 = Constraint(expr=m.x50*m.x38 - (m.x20*m.x8 + m.x104*m.x114) == 0)

m.c47 = Constraint(expr=m.x51*m.x38 - (m.x21*m.x8 + m.x104*m.x115) == 0)

m.c48 = Constraint(expr=m.x52*m.x39 - (m.x22*m.x9 + m.x105*(-m.x116 - m.x118)) == 0)

m.c49 = Constraint(expr=m.x53*m.x39 - (m.x23*m.x9 + m.x105*(0.5*m.x116 - m.x117 - m.x119)) == 0)

m.c50 = Constraint(expr=m.x54*m.x39 - (m.x24*m.x9 + m.x105*m.x117) == 0)

m.c51 = Constraint(expr=m.x55*m.x39 - (m.x25*m.x9 + m.x105*m.x118) == 0)

m.c52 = Constraint(expr=m.x56*m.x39 - (m.x26*m.x9 + m.x105*m.x119) == 0)

m.c53 = Constraint(expr=m.x57*m.x40 - (m.x27*m.x10 + m.x106*(-m.x120 - m.x122)) == 0)

m.c54 = Constraint(expr=m.x58*m.x40 - (m.x28*m.x10 + m.x106*(0.5*m.x120 - m.x121 - m.x123)) == 0)

m.c55 = Constraint(expr=m.x59*m.x40 - (m.x29*m.x10 + m.x106*m.x121) == 0)

m.c56 = Constraint(expr=m.x60*m.x40 - (m.x30*m.x10 + m.x106*m.x122) == 0)

m.c57 = Constraint(expr=m.x61*m.x40 - (m.x31*m.x10 + m.x106*m.x123) == 0)

m.c58 = Constraint(expr=m.x62*m.x41 - (m.x32*m.x11 + m.x107*(-m.x124 - m.x126)) == 0)

m.c59 = Constraint(expr=m.x63*m.x41 - (m.x33*m.x11 + m.x107*(0.5*m.x124 - m.x125 - m.x127)) == 0)

m.c60 = Constraint(expr=m.x64*m.x41 - (m.x34*m.x11 + m.x107*m.x125) == 0)

m.c61 = Constraint(expr=m.x65*m.x41 - (m.x35*m.x11 + m.x107*m.x126) == 0)

m.c62 = Constraint(expr=m.x66*m.x41 - (m.x36*m.x11 + m.x107*m.x127) == 0)

m.c63 = Constraint(expr=-m.x42*m.x42 + m.x108 == 0)

m.c64 = Constraint(expr=-m.x47*m.x47 + m.x112 == 0)

m.c65 = Constraint(expr=-m.x52*m.x52 + m.x116 == 0)

m.c66 = Constraint(expr=-m.x57*m.x57 + m.x120 == 0)

m.c67 = Constraint(expr=-m.x62*m.x62 + m.x124 == 0)

m.c68 = Constraint(expr= - 0.6*m.x43 + m.x109 == 0)

m.c69 = Constraint(expr= - 0.6*m.x48 + m.x113 == 0)

m.c70 = Constraint(expr= - 0.6*m.x53 + m.x117 == 0)

m.c71 = Constraint(expr= - 0.6*m.x58 + m.x121 == 0)

m.c72 = Constraint(expr= - 0.6*m.x63 + m.x125 == 0)

m.c73 = Constraint(expr= - 0.6*m.x42 + m.x110 == 0)

m.c74 = Constraint(expr= - 0.6*m.x47 + m.x114 == 0)

m.c75 = Constraint(expr= - 0.6*m.x52 + m.x118 == 0)

m.c76 = Constraint(expr= - 0.6*m.x57 + m.x122 == 0)

m.c77 = Constraint(expr= - 0.6*m.x62 + m.x126 == 0)

m.c78 = Constraint(expr=-0.1*m.x43*m.x43 + m.x111 == 0)

m.c79 = Constraint(expr=-0.1*m.x48*m.x48 + m.x115 == 0)

m.c80 = Constraint(expr=-0.1*m.x53*m.x53 + m.x119 == 0)

m.c81 = Constraint(expr=-0.1*m.x58*m.x58 + m.x123 == 0)

m.c82 = Constraint(expr=-0.1*m.x63*m.x63 + m.x127 == 0)

m.c83 = Constraint(expr=   m.x37 - m.x67 - m.x68 - m.x69 - m.x70 - m.x71 - m.x92 == 0)

m.c84 = Constraint(expr=   m.x38 - m.x72 - m.x73 - m.x74 - m.x75 - m.x76 - m.x93 == 0)

m.c85 = Constraint(expr=   m.x39 - m.x77 - m.x78 - m.x79 - m.x80 - m.x81 - m.x94 == 0)

m.c86 = Constraint(expr=   m.x40 - m.x82 - m.x83 - m.x84 - m.x85 - m.x86 - m.x95 == 0)

m.c87 = Constraint(expr=   m.x41 - m.x87 - m.x88 - m.x89 - m.x90 - m.x91 - m.x96 == 0)

m.c88 = Constraint(expr= - m.x92 - m.x93 - m.x94 - m.x95 - m.x96 + m.x97 == 0)

m.c89 = Constraint(expr=m.x97*m.x98 - (m.x92*m.x42 + m.x93*m.x47 + m.x94*m.x52 + m.x95*m.x57 + m.x96*m.x62) == 0)

m.c90 = Constraint(expr=m.x97*m.x99 - (m.x92*m.x43 + m.x93*m.x48 + m.x94*m.x53 + m.x95*m.x58 + m.x96*m.x63) == 0)

m.c91 = Constraint(expr=m.x97*m.x100 - (m.x92*m.x44 + m.x93*m.x49 + m.x94*m.x54 + m.x95*m.x59 + m.x96*m.x64) == 0)

m.c92 = Constraint(expr=m.x97*m.x101 - (m.x92*m.x45 + m.x93*m.x50 + m.x94*m.x55 + m.x95*m.x60 + m.x96*m.x65) == 0)

m.c93 = Constraint(expr=m.x97*m.x102 - (m.x92*m.x46 + m.x93*m.x51 + m.x94*m.x56 + m.x95*m.x61 + m.x96*m.x66) == 0)
