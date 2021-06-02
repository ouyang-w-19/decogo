#  MINLP written by GAMS Convert at 04/21/18 13:54:11
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        240       46      162       32        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        187      148       39        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        596      520       76        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,0.26351883),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,0.26351883),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,0.22891574),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,0.22891574),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,0.21464835),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,0.21464835),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,0.17964414),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,0.17964414),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,0.17402843),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,0.17402843),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,0.15355962),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,0.15355962),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,0.1942283),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,0.1942283),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,0.25670555),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,0.25670555),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,0.27088619),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,0.27088619),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,0.28985675),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,0.28985675),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,0.25550303),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,0.25550303),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,0.19001726),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,0.19001726),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,0.23803143),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,0.23803143),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,0.23312962),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,0.23312962),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,0.27705307),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,0.27705307),initialize=0)
m.x31 = Var(within=Reals,bounds=(5.68,5.96),initialize=5.68)
m.x32 = Var(within=Reals,bounds=(40.18,42.0933333333333),initialize=40.18)
m.x33 = Var(within=Reals,bounds=(94.7666666666667,99.28),initialize=94.7666666666667)
m.x34 = Var(within=Reals,bounds=(59.0533333333333,61.8666666666667),initialize=59.0533333333333)
m.x35 = Var(within=Reals,bounds=(53.7333333333333,56.2866666666667),initialize=53.7333333333333)
m.x36 = Var(within=Reals,bounds=(37.7266666666667,41.5),initialize=37.7266666666667)
m.x37 = Var(within=Reals,bounds=(59.6466666666667,62.4933333333333),initialize=59.6466666666667)
m.x38 = Var(within=Reals,bounds=(59.2733333333333,62.24),initialize=59.2733333333333)
m.b39 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b40 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b41 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b42 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b43 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b44 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b45 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b46 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b47 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b48 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b49 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b50 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b51 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b52 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b53 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b54 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b55 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b56 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b57 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b58 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b59 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b60 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b61 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b62 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b63 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b64 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b65 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b66 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b67 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b68 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.x84 = Var(within=Reals,bounds=(0.25788969,0.35227087),initialize=0.25788969)
m.x85 = Var(within=Reals,bounds=(0.25788969,0.35227087),initialize=0.25788969)
m.x86 = Var(within=Reals,bounds=(-0.98493628,-0.7794471),initialize=-0.7794471)
m.x87 = Var(within=Reals,bounds=(-0.98493628,-0.7794471),initialize=-0.7794471)
m.x88 = Var(within=Reals,bounds=(0,0.0580296499999999),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,0.0580296499999999),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,0.0546689399999999),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,0.0546689399999999),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,0.09360565),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,0.09360565),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,0.0476880399999999),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,0.0476880399999999),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,0.05276021),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,0.05276021),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,0.04905388),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,0.04905388),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,0.07731692),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,0.07731692),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,0.08211741),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,0.08211741),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,0.08436757),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,0.08436757),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,0.06987597),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,0.06987597),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,0.04788831),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,0.04788831),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,0.0668875099999999),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,0.0668875099999999),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,0.07276512),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,0.07276512),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,0.1742468),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,0.1742468),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,0.1210427),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,0.1210427),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,0.1319561),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,0.1319561),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,0.12126822),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,0.12126822),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,0.10450574),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,0.10450574),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,0.11691138),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,0.11691138),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,0.17458814),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,0.17458814),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,0.17650501),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,0.17650501),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,0.18562706),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,0.18562706),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,0.14212895),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,0.14212895),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,0.17114392),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,0.17114392),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,0.1603645),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,0.1603645),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,0.18267189),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,0.18267189),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.b178 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b179 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b180 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b181 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b182 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b183 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b184 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b185 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b186 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   m.x69 + m.x70 + m.x71 + m.x72 + m.x73 + m.x74 + m.x75 + m.x76 + m.x77 + m.x78 + m.x79 + m.x80
                        + m.x81 + m.x82 + m.x83, sense=minimize)

m.c2 = Constraint(expr=(-1.01*m.x1*m.b39) - 1.01*m.b39*m.x1 + m.x148 >= 0)

m.c3 = Constraint(expr=(-1.01*m.x2*m.b40) - 1.01*m.b40*m.x2 + m.x149 >= 0)

m.c4 = Constraint(expr=(-2.00666666666667*m.x3*m.b41) - 2.00666666666667*m.b41*m.x3 + m.x150 >= 0)

m.c5 = Constraint(expr=(-2.00666666666667*m.x4*m.b42) - 2.00666666666667*m.b42*m.x4 + m.x151 >= 0)

m.c6 = Constraint(expr=(-2.38*m.x5*m.b43) - 2.38*m.b43*m.x5 + m.x152 >= 0)

m.c7 = Constraint(expr=(-2.38*m.x6*m.b44) - 2.38*m.b44*m.x6 + m.x153 >= 0)

m.c8 = Constraint(expr=-m.x31*m.x7*m.b45 + m.x154 >= 0)

m.c9 = Constraint(expr=-m.x31*m.x8*m.b46 + m.x155 >= 0)

m.c10 = Constraint(expr=-m.x32*m.x9*m.b47 + m.x156 >= 0)

m.c11 = Constraint(expr=-m.x32*m.x10*m.b48 + m.x157 >= 0)

m.c12 = Constraint(expr=-m.x33*m.x11*m.b49 + m.x158 >= 0)

m.c13 = Constraint(expr=-m.x33*m.x12*m.b50 + m.x159 >= 0)

m.c14 = Constraint(expr=(-3.29666666666667*m.x13*m.b51) - 3.29666666666667*m.b51*m.x13 + m.x160 >= 0)

m.c15 = Constraint(expr=(-3.29666666666667*m.x14*m.b52) - 3.29666666666667*m.b52*m.x14 + m.x161 >= 0)

m.c16 = Constraint(expr=-m.x34*m.x15*m.b53 + m.x162 >= 0)

m.c17 = Constraint(expr=-m.x34*m.x16*m.b54 + m.x163 >= 0)

m.c18 = Constraint(expr=-m.x35*m.x17*m.b55 + m.x164 >= 0)

m.c19 = Constraint(expr=-m.x35*m.x18*m.b56 + m.x165 >= 0)

m.c20 = Constraint(expr=-m.x36*m.x19*m.b57 + m.x166 >= 0)

m.c21 = Constraint(expr=-m.x36*m.x20*m.b58 + m.x167 >= 0)

m.c22 = Constraint(expr=-m.x37*m.x21*m.b59 + m.x168 >= 0)

m.c23 = Constraint(expr=-m.x37*m.x22*m.b60 + m.x169 >= 0)

m.c24 = Constraint(expr=(-40.4533333333333*m.x23*m.b61) - 40.4533333333333*m.b61*m.x23 + m.x170 >= 0)

m.c25 = Constraint(expr=(-40.4533333333333*m.x24*m.b62) - 40.4533333333333*m.b62*m.x24 + m.x171 >= 0)

m.c26 = Constraint(expr=(-13.0733333333333*m.x25*m.b63) - 13.0733333333333*m.b63*m.x25 + m.x172 >= 0)

m.c27 = Constraint(expr=(-13.0733333333333*m.x26*m.b64) - 13.0733333333333*m.b64*m.x26 + m.x173 >= 0)

m.c28 = Constraint(expr=(-19*m.x27*m.b65) - 19*m.b65*m.x27 + m.x174 >= 0)

m.c29 = Constraint(expr=(-19*m.x28*m.b66) - 19*m.b66*m.x28 + m.x175 >= 0)

m.c30 = Constraint(expr=-m.x38*m.x29*m.b67 + m.x176 >= 0)

m.c31 = Constraint(expr=-m.x38*m.x30*m.b68 + m.x177 >= 0)

m.c32 = Constraint(expr=   m.b39 + m.b40 == 1)

m.c33 = Constraint(expr=   m.b41 + m.b42 == 1)

m.c34 = Constraint(expr=   m.b43 + m.b44 == 1)

m.c35 = Constraint(expr=   m.b45 + m.b46 == 1)

m.c36 = Constraint(expr=   m.b47 + m.b48 == 1)

m.c37 = Constraint(expr=   m.b49 + m.b50 == 1)

m.c38 = Constraint(expr=   m.b51 + m.b52 == 1)

m.c39 = Constraint(expr=   m.b53 + m.b54 == 1)

m.c40 = Constraint(expr=   m.b55 + m.b56 == 1)

m.c41 = Constraint(expr=   m.b57 + m.b58 == 1)

m.c42 = Constraint(expr=   m.b59 + m.b60 == 1)

m.c43 = Constraint(expr=   m.b61 + m.b62 == 1)

m.c44 = Constraint(expr=   m.b63 + m.b64 == 1)

m.c45 = Constraint(expr=   m.b65 + m.b66 == 1)

m.c46 = Constraint(expr=   m.b67 + m.b68 == 1)

m.c47 = Constraint(expr=   2.02*m.b39 + 4.01333333333333*m.b41 + 4.76*m.b43 + 5.96*m.b45 + 42.0933333333333*m.b47
                         + 99.28*m.b49 + 6.59333333333333*m.b51 + 61.8666666666667*m.b53 + 56.2866666666667*m.b55
                         + 41.5*m.b57 + 62.4933333333333*m.b59 + 80.9066666666667*m.b61 + 26.1466666666667*m.b63
                         + 38*m.b65 + 62.24*m.b67 <= 302.08)

m.c48 = Constraint(expr=   2.02*m.b40 + 4.01333333333333*m.b42 + 4.76*m.b44 + 5.96*m.b46 + 42.0933333333333*m.b48
                         + 99.28*m.b50 + 6.59333333333333*m.b52 + 61.8666666666667*m.b54 + 56.2866666666667*m.b56
                         + 41.5*m.b58 + 62.4933333333333*m.b60 + 80.9066666666667*m.b62 + 26.1466666666667*m.b64
                         + 38*m.b66 + 62.24*m.b68 <= 302.08)

m.c49 = Constraint(expr=   m.x84 + m.x88 >= 0.29424122)

m.c50 = Constraint(expr=   m.x85 + m.x89 >= 0.29424122)

m.c51 = Constraint(expr=   m.x84 + m.x90 >= 0.29760193)

m.c52 = Constraint(expr=   m.x85 + m.x91 >= 0.29760193)

m.c53 = Constraint(expr=   m.x84 + m.x92 >= 0.35149534)

m.c54 = Constraint(expr=   m.x85 + m.x93 >= 0.35149534)

m.c55 = Constraint(expr=   m.x84 + m.x94 >= 0.30458283)

m.c56 = Constraint(expr=   m.x85 + m.x95 >= 0.30458283)

m.c57 = Constraint(expr=   m.x84 + m.x96 >= 0.29951066)

m.c58 = Constraint(expr=   m.x85 + m.x97 >= 0.29951066)

m.c59 = Constraint(expr=   m.x84 + m.x98 >= 0.30694357)

m.c60 = Constraint(expr=   m.x85 + m.x99 >= 0.30694357)

m.c61 = Constraint(expr=   m.x84 + m.x100 >= 0.33520661)

m.c62 = Constraint(expr=   m.x85 + m.x101 >= 0.33520661)

m.c63 = Constraint(expr=   m.x84 + m.x102 >= 0.3400071)

m.c64 = Constraint(expr=   m.x85 + m.x103 >= 0.3400071)

m.c65 = Constraint(expr=   m.x84 + m.x104 >= 0.35227087)

m.c66 = Constraint(expr=   m.x85 + m.x105 >= 0.35227087)

m.c67 = Constraint(expr=   m.x84 + m.x106 >= 0.34225726)

m.c68 = Constraint(expr=   m.x85 + m.x107 >= 0.34225726)

m.c69 = Constraint(expr=   m.x84 + m.x108 >= 0.32776566)

m.c70 = Constraint(expr=   m.x85 + m.x109 >= 0.32776566)

m.c71 = Constraint(expr=   m.x84 + m.x110 >= 0.30438256)

m.c72 = Constraint(expr=   m.x85 + m.x111 >= 0.30438256)

m.c73 = Constraint(expr=   m.x84 + m.x112 >= 0.28538336)

m.c74 = Constraint(expr=   m.x85 + m.x113 >= 0.28538336)

m.c75 = Constraint(expr=   m.x84 + m.x114 >= 0.27950575)

m.c76 = Constraint(expr=   m.x85 + m.x115 >= 0.27950575)

m.c77 = Constraint(expr= - m.x84 + m.x88 >= -0.29424122)

m.c78 = Constraint(expr= - m.x85 + m.x89 >= -0.29424122)

m.c79 = Constraint(expr= - m.x84 + m.x90 >= -0.29760193)

m.c80 = Constraint(expr= - m.x85 + m.x91 >= -0.29760193)

m.c81 = Constraint(expr= - m.x84 + m.x92 >= -0.35149534)

m.c82 = Constraint(expr= - m.x85 + m.x93 >= -0.35149534)

m.c83 = Constraint(expr= - m.x84 + m.x94 >= -0.30458283)

m.c84 = Constraint(expr= - m.x85 + m.x95 >= -0.30458283)

m.c85 = Constraint(expr= - m.x84 + m.x96 >= -0.29951066)

m.c86 = Constraint(expr= - m.x85 + m.x97 >= -0.29951066)

m.c87 = Constraint(expr= - m.x84 + m.x98 >= -0.30694357)

m.c88 = Constraint(expr= - m.x85 + m.x99 >= -0.30694357)

m.c89 = Constraint(expr= - m.x84 + m.x100 >= -0.33520661)

m.c90 = Constraint(expr= - m.x85 + m.x101 >= -0.33520661)

m.c91 = Constraint(expr= - m.x84 + m.x102 >= -0.3400071)

m.c92 = Constraint(expr= - m.x85 + m.x103 >= -0.3400071)

m.c93 = Constraint(expr= - m.x84 + m.x106 >= -0.34225726)

m.c94 = Constraint(expr= - m.x85 + m.x107 >= -0.34225726)

m.c95 = Constraint(expr= - m.x84 + m.x108 >= -0.32776566)

m.c96 = Constraint(expr= - m.x85 + m.x109 >= -0.32776566)

m.c97 = Constraint(expr= - m.x84 + m.x110 >= -0.30438256)

m.c98 = Constraint(expr= - m.x85 + m.x111 >= -0.30438256)

m.c99 = Constraint(expr= - m.x84 + m.x112 >= -0.28538336)

m.c100 = Constraint(expr= - m.x85 + m.x113 >= -0.28538336)

m.c101 = Constraint(expr= - m.x84 + m.x114 >= -0.27950575)

m.c102 = Constraint(expr= - m.x85 + m.x115 >= -0.27950575)

m.c103 = Constraint(expr= - m.x84 + m.x116 >= -0.25788969)

m.c104 = Constraint(expr= - m.x85 + m.x117 >= -0.25788969)

m.c105 = Constraint(expr=   m.x86 + m.x120 >= -0.9536939)

m.c106 = Constraint(expr=   m.x87 + m.x121 >= -0.9536939)

m.c107 = Constraint(expr=   m.x86 + m.x122 >= -0.9004898)

m.c108 = Constraint(expr=   m.x87 + m.x123 >= -0.9004898)

m.c109 = Constraint(expr=   m.x86 + m.x124 >= -0.9114032)

m.c110 = Constraint(expr=   m.x87 + m.x125 >= -0.9114032)

m.c111 = Constraint(expr=   m.x86 + m.x126 >= -0.90071532)

m.c112 = Constraint(expr=   m.x87 + m.x127 >= -0.90071532)

m.c113 = Constraint(expr=   m.x86 + m.x128 >= -0.88043054)

m.c114 = Constraint(expr=   m.x87 + m.x129 >= -0.88043054)

m.c115 = Constraint(expr=   m.x86 + m.x130 >= -0.8680249)

m.c116 = Constraint(expr=   m.x87 + m.x131 >= -0.8680249)

m.c117 = Constraint(expr=   m.x86 + m.x132 >= -0.81034814)

m.c118 = Constraint(expr=   m.x87 + m.x133 >= -0.81034814)

m.c119 = Constraint(expr=   m.x86 + m.x134 >= -0.80843127)

m.c120 = Constraint(expr=   m.x87 + m.x135 >= -0.80843127)

m.c121 = Constraint(expr=   m.x86 + m.x136 >= -0.7794471)

m.c122 = Constraint(expr=   m.x87 + m.x137 >= -0.7794471)

m.c123 = Constraint(expr=   m.x86 + m.x138 >= -0.79930922)

m.c124 = Constraint(expr=   m.x87 + m.x139 >= -0.79930922)

m.c125 = Constraint(expr=   m.x86 + m.x140 >= -0.84280733)

m.c126 = Constraint(expr=   m.x87 + m.x141 >= -0.84280733)

m.c127 = Constraint(expr=   m.x86 + m.x142 >= -0.81379236)

m.c128 = Constraint(expr=   m.x87 + m.x143 >= -0.81379236)

m.c129 = Constraint(expr=   m.x86 + m.x144 >= -0.82457178)

m.c130 = Constraint(expr=   m.x87 + m.x145 >= -0.82457178)

m.c131 = Constraint(expr=   m.x86 + m.x146 >= -0.80226439)

m.c132 = Constraint(expr=   m.x87 + m.x147 >= -0.80226439)

m.c133 = Constraint(expr= - m.x86 + m.x118 >= 0.98493628)

m.c134 = Constraint(expr= - m.x87 + m.x119 >= 0.98493628)

m.c135 = Constraint(expr= - m.x86 + m.x120 >= 0.9536939)

m.c136 = Constraint(expr= - m.x87 + m.x121 >= 0.9536939)

m.c137 = Constraint(expr= - m.x86 + m.x122 >= 0.9004898)

m.c138 = Constraint(expr= - m.x87 + m.x123 >= 0.9004898)

m.c139 = Constraint(expr= - m.x86 + m.x124 >= 0.9114032)

m.c140 = Constraint(expr= - m.x87 + m.x125 >= 0.9114032)

m.c141 = Constraint(expr= - m.x86 + m.x126 >= 0.90071532)

m.c142 = Constraint(expr= - m.x87 + m.x127 >= 0.90071532)

m.c143 = Constraint(expr= - m.x86 + m.x128 >= 0.88043054)

m.c144 = Constraint(expr= - m.x87 + m.x129 >= 0.88043054)

m.c145 = Constraint(expr= - m.x86 + m.x130 >= 0.8680249)

m.c146 = Constraint(expr= - m.x87 + m.x131 >= 0.8680249)

m.c147 = Constraint(expr= - m.x86 + m.x132 >= 0.81034814)

m.c148 = Constraint(expr= - m.x87 + m.x133 >= 0.81034814)

m.c149 = Constraint(expr= - m.x86 + m.x134 >= 0.80843127)

m.c150 = Constraint(expr= - m.x87 + m.x135 >= 0.80843127)

m.c151 = Constraint(expr= - m.x86 + m.x138 >= 0.79930922)

m.c152 = Constraint(expr= - m.x87 + m.x139 >= 0.79930922)

m.c153 = Constraint(expr= - m.x86 + m.x140 >= 0.84280733)

m.c154 = Constraint(expr= - m.x87 + m.x141 >= 0.84280733)

m.c155 = Constraint(expr= - m.x86 + m.x142 >= 0.81379236)

m.c156 = Constraint(expr= - m.x87 + m.x143 >= 0.81379236)

m.c157 = Constraint(expr= - m.x86 + m.x144 >= 0.82457178)

m.c158 = Constraint(expr= - m.x87 + m.x145 >= 0.82457178)

m.c159 = Constraint(expr= - m.x86 + m.x146 >= 0.80226439)

m.c160 = Constraint(expr= - m.x87 + m.x147 >= 0.80226439)

m.c161 = Constraint(expr=   m.x1 - m.x88 - m.x118 == 0)

m.c162 = Constraint(expr=   m.x2 - m.x89 - m.x119 == 0)

m.c163 = Constraint(expr=   m.x3 - m.x90 - m.x120 == 0)

m.c164 = Constraint(expr=   m.x4 - m.x91 - m.x121 == 0)

m.c165 = Constraint(expr=   m.x5 - m.x92 - m.x122 == 0)

m.c166 = Constraint(expr=   m.x6 - m.x93 - m.x123 == 0)

m.c167 = Constraint(expr=   m.x7 - m.x94 - m.x124 == 0)

m.c168 = Constraint(expr=   m.x8 - m.x95 - m.x125 == 0)

m.c169 = Constraint(expr=   m.x9 - m.x96 - m.x126 == 0)

m.c170 = Constraint(expr=   m.x10 - m.x97 - m.x127 == 0)

m.c171 = Constraint(expr=   m.x11 - m.x98 - m.x128 == 0)

m.c172 = Constraint(expr=   m.x12 - m.x99 - m.x129 == 0)

m.c173 = Constraint(expr=   m.x13 - m.x100 - m.x130 == 0)

m.c174 = Constraint(expr=   m.x14 - m.x101 - m.x131 == 0)

m.c175 = Constraint(expr=   m.x15 - m.x102 - m.x132 == 0)

m.c176 = Constraint(expr=   m.x16 - m.x103 - m.x133 == 0)

m.c177 = Constraint(expr=   m.x17 - m.x104 - m.x134 == 0)

m.c178 = Constraint(expr=   m.x18 - m.x105 - m.x135 == 0)

m.c179 = Constraint(expr=   m.x19 - m.x106 - m.x136 == 0)

m.c180 = Constraint(expr=   m.x20 - m.x107 - m.x137 == 0)

m.c181 = Constraint(expr=   m.x21 - m.x108 - m.x138 == 0)

m.c182 = Constraint(expr=   m.x22 - m.x109 - m.x139 == 0)

m.c183 = Constraint(expr=   m.x23 - m.x110 - m.x140 == 0)

m.c184 = Constraint(expr=   m.x24 - m.x111 - m.x141 == 0)

m.c185 = Constraint(expr=   m.x25 - m.x112 - m.x142 == 0)

m.c186 = Constraint(expr=   m.x26 - m.x113 - m.x143 == 0)

m.c187 = Constraint(expr=   m.x27 - m.x114 - m.x144 == 0)

m.c188 = Constraint(expr=   m.x28 - m.x115 - m.x145 == 0)

m.c189 = Constraint(expr=   m.x29 - m.x116 - m.x146 == 0)

m.c190 = Constraint(expr=   m.x30 - m.x117 - m.x147 == 0)

m.c191 = Constraint(expr=   m.b179 + m.b180 >= 1)

m.c192 = Constraint(expr=   m.b178 + m.b180 >= 1)

m.c193 = Constraint(expr=   m.b178 + m.b179 >= 1)

m.c194 = Constraint(expr=   m.b180 + m.b182 >= 1)

m.c195 = Constraint(expr=   m.b180 + m.b181 >= 1)

m.c196 = Constraint(expr=   m.b179 + m.b182 >= 1)

m.c197 = Constraint(expr=   m.b179 + m.b181 >= 1)

m.c198 = Constraint(expr=   m.b178 + m.b182 >= 1)

m.c199 = Constraint(expr=   m.b178 + m.b181 >= 1)

m.c200 = Constraint(expr=   m.x31 - 5.96*m.b178 >= 0)

m.c201 = Constraint(expr=   m.x32 - 42.0933333333333*m.b179 >= 0)

m.c202 = Constraint(expr=   m.x33 - 99.28*m.b180 >= 0)

m.c203 = Constraint(expr=   m.x34 - 61.8666666666667*m.b181 >= 0)

m.c204 = Constraint(expr=   m.x35 - 56.2866666666667*m.b182 >= 0)

m.c205 = Constraint(expr=   m.x36 - 39.6133333333333*m.b183 >= 0)

m.c206 = Constraint(expr=   m.x36 - 41.5*m.b184 >= 0)

m.c207 = Constraint(expr=   m.x37 - 62.4933333333333*m.b185 >= 0)

m.c208 = Constraint(expr=   m.x38 - 62.24*m.b186 >= 0)

m.c209 = Constraint(expr= - m.x69 + m.x148 <= 0)

m.c210 = Constraint(expr= - m.x69 + m.x149 <= 0)

m.c211 = Constraint(expr= - m.x70 + m.x150 <= 0)

m.c212 = Constraint(expr= - m.x70 + m.x151 <= 0)

m.c213 = Constraint(expr= - m.x71 + m.x152 <= 0)

m.c214 = Constraint(expr= - m.x71 + m.x153 <= 0)

m.c215 = Constraint(expr= - m.x72 + m.x154 <= 0)

m.c216 = Constraint(expr= - m.x72 + m.x155 <= 0)

m.c217 = Constraint(expr= - m.x73 + m.x156 <= 0)

m.c218 = Constraint(expr= - m.x73 + m.x157 <= 0)

m.c219 = Constraint(expr= - m.x74 + m.x158 <= 0)

m.c220 = Constraint(expr= - m.x74 + m.x159 <= 0)

m.c221 = Constraint(expr= - m.x75 + m.x160 <= 0)

m.c222 = Constraint(expr= - m.x75 + m.x161 <= 0)

m.c223 = Constraint(expr= - m.x76 + m.x162 <= 0)

m.c224 = Constraint(expr= - m.x76 + m.x163 <= 0)

m.c225 = Constraint(expr= - m.x77 + m.x164 <= 0)

m.c226 = Constraint(expr= - m.x77 + m.x165 <= 0)

m.c227 = Constraint(expr= - m.x78 + m.x166 <= 0)

m.c228 = Constraint(expr= - m.x78 + m.x167 <= 0)

m.c229 = Constraint(expr= - m.x79 + m.x168 <= 0)

m.c230 = Constraint(expr= - m.x79 + m.x169 <= 0)

m.c231 = Constraint(expr= - m.x80 + m.x170 <= 0)

m.c232 = Constraint(expr= - m.x80 + m.x171 <= 0)

m.c233 = Constraint(expr= - m.x81 + m.x172 <= 0)

m.c234 = Constraint(expr= - m.x81 + m.x173 <= 0)

m.c235 = Constraint(expr= - m.x82 + m.x174 <= 0)

m.c236 = Constraint(expr= - m.x82 + m.x175 <= 0)

m.c237 = Constraint(expr= - m.x83 + m.x176 <= 0)

m.c238 = Constraint(expr= - m.x83 + m.x177 <= 0)

m.c239 = Constraint(expr=   m.b183 - m.b184 >= 0)

m.c240 = Constraint(expr=   m.x86 - m.x87 >= 0)
