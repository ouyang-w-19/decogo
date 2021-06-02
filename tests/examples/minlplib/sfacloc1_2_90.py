#  MINLP written by GAMS Convert at 04/21/18 13:54:10
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        349       76      256       17        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        200      170       30        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        929      854       75        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1),initialize=0)
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
m.x17 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,1),initialize=0)
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
m.x31 = Var(within=Reals,bounds=(0,0.26351883),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,0.26351883),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,0.22891574),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,0.22891574),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,0.21464835),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,0.21464835),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,0.17964414),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,0.17964414),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,0.17402843),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,0.17402843),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,0.15355962),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,0.15355962),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,0.1942283),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,0.1942283),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,0.25670555),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,0.25670555),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,0.27088619),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,0.27088619),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,0.28985675),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,0.28985675),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,0.25550303),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,0.25550303),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,0.19001726),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,0.19001726),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,0.23803143),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,0.23803143),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,0.23312962),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,0.23312962),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,0.27705307),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,0.27705307),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,2.02),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,4.01333333333333),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,4.76),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,5.96),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,42.0933333333333),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,99.28),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,6.59333333333333),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,61.8666666666667),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,56.2866666666667),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,41.5),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,62.4933333333333),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,80.9066666666667),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,26.1466666666667),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,38),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,62.24),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.x91 = Var(within=Reals,bounds=(0.25788969,0.35227087),initialize=0.25788969)
m.x92 = Var(within=Reals,bounds=(0.25788969,0.35227087),initialize=0.25788969)
m.x93 = Var(within=Reals,bounds=(-0.98493628,-0.7794471),initialize=-0.7794471)
m.x94 = Var(within=Reals,bounds=(-0.98493628,-0.7794471),initialize=-0.7794471)
m.x95 = Var(within=Reals,bounds=(0,0.0580296499999999),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,0.0580296499999999),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,0.0546689399999999),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,0.0546689399999999),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,0.09360565),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,0.09360565),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,0.0476880399999999),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,0.0476880399999999),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,0.05276021),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,0.05276021),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,0.04905388),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,0.04905388),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,0.07731692),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,0.07731692),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,0.08211741),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,0.08211741),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,0.08436757),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,0.08436757),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,0.06987597),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,0.06987597),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,0.04788831),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,0.04788831),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,0.0668875099999999),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,0.0668875099999999),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,0.07276512),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,0.07276512),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,0.1742468),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,0.1742468),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,0.1210427),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,0.1210427),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,0.1319561),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,0.1319561),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,0.12126822),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,0.12126822),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,0.10450574),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,0.10450574),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,0.11691138),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,0.11691138),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,0.17458814),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,0.17458814),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,0.17650501),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,0.17650501),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,0.18562706),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,0.18562706),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,0.14212895),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,0.14212895),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,0.17114392),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,0.17114392),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,0.1603645),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,0.1603645),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,0.18267189),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,0.18267189),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.b170 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b171 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b172 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b173 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b174 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b175 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b176 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b177 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b178 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b179 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b180 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b181 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b182 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b183 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b184 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b185 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b186 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b187 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b188 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b189 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b190 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b191 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b192 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b193 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b194 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b195 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b196 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b197 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b198 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b199 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   m.x76 + m.x77 + m.x78 + m.x79 + m.x80 + m.x81 + m.x82 + m.x83 + m.x84 + m.x85 + m.x86 + m.x87
                        + m.x88 + m.x89 + m.x90, sense=minimize)

m.c2 = Constraint(expr=(-m.x61*m.x32*m.x2) - m.x61*m.x31*m.x1 + m.x155 == 0)

m.c3 = Constraint(expr=(-m.x62*m.x34*m.x4) - m.x62*m.x33*m.x3 + m.x156 == 0)

m.c4 = Constraint(expr=(-m.x63*m.x36*m.x6) - m.x63*m.x35*m.x5 + m.x157 == 0)

m.c5 = Constraint(expr=(-m.x64*m.x38*m.x8) - m.x64*m.x37*m.x7 + m.x158 == 0)

m.c6 = Constraint(expr=(-m.x65*m.x40*m.x10) - m.x65*m.x39*m.x9 + m.x159 == 0)

m.c7 = Constraint(expr=(-m.x66*m.x42*m.x12) - m.x66*m.x41*m.x11 + m.x160 == 0)

m.c8 = Constraint(expr=(-m.x67*m.x44*m.x14) - m.x67*m.x43*m.x13 + m.x161 == 0)

m.c9 = Constraint(expr=(-m.x68*m.x46*m.x16) - m.x68*m.x45*m.x15 + m.x162 == 0)

m.c10 = Constraint(expr=(-m.x69*m.x48*m.x18) - m.x69*m.x47*m.x17 + m.x163 == 0)

m.c11 = Constraint(expr=(-m.x70*m.x50*m.x20) - m.x70*m.x49*m.x19 + m.x164 == 0)

m.c12 = Constraint(expr=(-m.x71*m.x52*m.x22) - m.x71*m.x51*m.x21 + m.x165 == 0)

m.c13 = Constraint(expr=(-m.x72*m.x54*m.x24) - m.x72*m.x53*m.x23 + m.x166 == 0)

m.c14 = Constraint(expr=(-m.x73*m.x56*m.x26) - m.x73*m.x55*m.x25 + m.x167 == 0)

m.c15 = Constraint(expr=(-m.x74*m.x58*m.x28) - m.x74*m.x57*m.x27 + m.x168 == 0)

m.c16 = Constraint(expr=(-m.x75*m.x60*m.x30) - m.x75*m.x59*m.x29 + m.x169 == 0)

m.c17 = Constraint(expr=   m.x1 + m.x2 == 1)

m.c18 = Constraint(expr=   m.x3 + m.x4 == 1)

m.c19 = Constraint(expr=   m.x5 + m.x6 == 1)

m.c20 = Constraint(expr=   m.x7 + m.x8 == 1)

m.c21 = Constraint(expr=   m.x9 + m.x10 == 1)

m.c22 = Constraint(expr=   m.x11 + m.x12 == 1)

m.c23 = Constraint(expr=   m.x13 + m.x14 == 1)

m.c24 = Constraint(expr=   m.x15 + m.x16 == 1)

m.c25 = Constraint(expr=   m.x17 + m.x18 == 1)

m.c26 = Constraint(expr=   m.x19 + m.x20 == 1)

m.c27 = Constraint(expr=   m.x21 + m.x22 == 1)

m.c28 = Constraint(expr=   m.x23 + m.x24 == 1)

m.c29 = Constraint(expr=   m.x25 + m.x26 == 1)

m.c30 = Constraint(expr=   m.x27 + m.x28 == 1)

m.c31 = Constraint(expr=   m.x29 + m.x30 == 1)

m.c32 = Constraint(expr=   2.02*m.x1 + 4.01333333333333*m.x3 + 4.76*m.x5 + 5.96*m.x7 + 42.0933333333333*m.x9
                         + 99.28*m.x11 + 6.59333333333333*m.x13 + 61.8666666666667*m.x15 + 56.2866666666667*m.x17
                         + 41.5*m.x19 + 62.4933333333333*m.x21 + 80.9066666666667*m.x23 + 26.1466666666667*m.x25
                         + 38*m.x27 + 62.24*m.x29 <= 302.08)

m.c33 = Constraint(expr=   2.02*m.x2 + 4.01333333333333*m.x4 + 4.76*m.x6 + 5.96*m.x8 + 42.0933333333333*m.x10
                         + 99.28*m.x12 + 6.59333333333333*m.x14 + 61.8666666666667*m.x16 + 56.2866666666667*m.x18
                         + 41.5*m.x20 + 62.4933333333333*m.x22 + 80.9066666666667*m.x24 + 26.1466666666667*m.x26
                         + 38*m.x28 + 62.24*m.x30 <= 302.08)

m.c34 = Constraint(expr=   m.x91 + m.x95 >= 0.29424122)

m.c35 = Constraint(expr=   m.x92 + m.x96 >= 0.29424122)

m.c36 = Constraint(expr=   m.x91 + m.x97 >= 0.29760193)

m.c37 = Constraint(expr=   m.x92 + m.x98 >= 0.29760193)

m.c38 = Constraint(expr=   m.x91 + m.x99 >= 0.35149534)

m.c39 = Constraint(expr=   m.x92 + m.x100 >= 0.35149534)

m.c40 = Constraint(expr=   m.x91 + m.x101 >= 0.30458283)

m.c41 = Constraint(expr=   m.x92 + m.x102 >= 0.30458283)

m.c42 = Constraint(expr=   m.x91 + m.x103 >= 0.29951066)

m.c43 = Constraint(expr=   m.x92 + m.x104 >= 0.29951066)

m.c44 = Constraint(expr=   m.x91 + m.x105 >= 0.30694357)

m.c45 = Constraint(expr=   m.x92 + m.x106 >= 0.30694357)

m.c46 = Constraint(expr=   m.x91 + m.x107 >= 0.33520661)

m.c47 = Constraint(expr=   m.x92 + m.x108 >= 0.33520661)

m.c48 = Constraint(expr=   m.x91 + m.x109 >= 0.3400071)

m.c49 = Constraint(expr=   m.x92 + m.x110 >= 0.3400071)

m.c50 = Constraint(expr=   m.x91 + m.x111 >= 0.35227087)

m.c51 = Constraint(expr=   m.x92 + m.x112 >= 0.35227087)

m.c52 = Constraint(expr=   m.x91 + m.x113 >= 0.34225726)

m.c53 = Constraint(expr=   m.x92 + m.x114 >= 0.34225726)

m.c54 = Constraint(expr=   m.x91 + m.x115 >= 0.32776566)

m.c55 = Constraint(expr=   m.x92 + m.x116 >= 0.32776566)

m.c56 = Constraint(expr=   m.x91 + m.x117 >= 0.30438256)

m.c57 = Constraint(expr=   m.x92 + m.x118 >= 0.30438256)

m.c58 = Constraint(expr=   m.x91 + m.x119 >= 0.28538336)

m.c59 = Constraint(expr=   m.x92 + m.x120 >= 0.28538336)

m.c60 = Constraint(expr=   m.x91 + m.x121 >= 0.27950575)

m.c61 = Constraint(expr=   m.x92 + m.x122 >= 0.27950575)

m.c62 = Constraint(expr= - m.x91 + m.x95 >= -0.29424122)

m.c63 = Constraint(expr= - m.x92 + m.x96 >= -0.29424122)

m.c64 = Constraint(expr= - m.x91 + m.x97 >= -0.29760193)

m.c65 = Constraint(expr= - m.x92 + m.x98 >= -0.29760193)

m.c66 = Constraint(expr= - m.x91 + m.x99 >= -0.35149534)

m.c67 = Constraint(expr= - m.x92 + m.x100 >= -0.35149534)

m.c68 = Constraint(expr= - m.x91 + m.x101 >= -0.30458283)

m.c69 = Constraint(expr= - m.x92 + m.x102 >= -0.30458283)

m.c70 = Constraint(expr= - m.x91 + m.x103 >= -0.29951066)

m.c71 = Constraint(expr= - m.x92 + m.x104 >= -0.29951066)

m.c72 = Constraint(expr= - m.x91 + m.x105 >= -0.30694357)

m.c73 = Constraint(expr= - m.x92 + m.x106 >= -0.30694357)

m.c74 = Constraint(expr= - m.x91 + m.x107 >= -0.33520661)

m.c75 = Constraint(expr= - m.x92 + m.x108 >= -0.33520661)

m.c76 = Constraint(expr= - m.x91 + m.x109 >= -0.3400071)

m.c77 = Constraint(expr= - m.x92 + m.x110 >= -0.3400071)

m.c78 = Constraint(expr= - m.x91 + m.x113 >= -0.34225726)

m.c79 = Constraint(expr= - m.x92 + m.x114 >= -0.34225726)

m.c80 = Constraint(expr= - m.x91 + m.x115 >= -0.32776566)

m.c81 = Constraint(expr= - m.x92 + m.x116 >= -0.32776566)

m.c82 = Constraint(expr= - m.x91 + m.x117 >= -0.30438256)

m.c83 = Constraint(expr= - m.x92 + m.x118 >= -0.30438256)

m.c84 = Constraint(expr= - m.x91 + m.x119 >= -0.28538336)

m.c85 = Constraint(expr= - m.x92 + m.x120 >= -0.28538336)

m.c86 = Constraint(expr= - m.x91 + m.x121 >= -0.27950575)

m.c87 = Constraint(expr= - m.x92 + m.x122 >= -0.27950575)

m.c88 = Constraint(expr= - m.x91 + m.x123 >= -0.25788969)

m.c89 = Constraint(expr= - m.x92 + m.x124 >= -0.25788969)

m.c90 = Constraint(expr=   m.x93 + m.x127 >= -0.9536939)

m.c91 = Constraint(expr=   m.x94 + m.x128 >= -0.9536939)

m.c92 = Constraint(expr=   m.x93 + m.x129 >= -0.9004898)

m.c93 = Constraint(expr=   m.x94 + m.x130 >= -0.9004898)

m.c94 = Constraint(expr=   m.x93 + m.x131 >= -0.9114032)

m.c95 = Constraint(expr=   m.x94 + m.x132 >= -0.9114032)

m.c96 = Constraint(expr=   m.x93 + m.x133 >= -0.90071532)

m.c97 = Constraint(expr=   m.x94 + m.x134 >= -0.90071532)

m.c98 = Constraint(expr=   m.x93 + m.x135 >= -0.88043054)

m.c99 = Constraint(expr=   m.x94 + m.x136 >= -0.88043054)

m.c100 = Constraint(expr=   m.x93 + m.x137 >= -0.8680249)

m.c101 = Constraint(expr=   m.x94 + m.x138 >= -0.8680249)

m.c102 = Constraint(expr=   m.x93 + m.x139 >= -0.81034814)

m.c103 = Constraint(expr=   m.x94 + m.x140 >= -0.81034814)

m.c104 = Constraint(expr=   m.x93 + m.x141 >= -0.80843127)

m.c105 = Constraint(expr=   m.x94 + m.x142 >= -0.80843127)

m.c106 = Constraint(expr=   m.x93 + m.x143 >= -0.7794471)

m.c107 = Constraint(expr=   m.x94 + m.x144 >= -0.7794471)

m.c108 = Constraint(expr=   m.x93 + m.x145 >= -0.79930922)

m.c109 = Constraint(expr=   m.x94 + m.x146 >= -0.79930922)

m.c110 = Constraint(expr=   m.x93 + m.x147 >= -0.84280733)

m.c111 = Constraint(expr=   m.x94 + m.x148 >= -0.84280733)

m.c112 = Constraint(expr=   m.x93 + m.x149 >= -0.81379236)

m.c113 = Constraint(expr=   m.x94 + m.x150 >= -0.81379236)

m.c114 = Constraint(expr=   m.x93 + m.x151 >= -0.82457178)

m.c115 = Constraint(expr=   m.x94 + m.x152 >= -0.82457178)

m.c116 = Constraint(expr=   m.x93 + m.x153 >= -0.80226439)

m.c117 = Constraint(expr=   m.x94 + m.x154 >= -0.80226439)

m.c118 = Constraint(expr= - m.x93 + m.x125 >= 0.98493628)

m.c119 = Constraint(expr= - m.x94 + m.x126 >= 0.98493628)

m.c120 = Constraint(expr= - m.x93 + m.x127 >= 0.9536939)

m.c121 = Constraint(expr= - m.x94 + m.x128 >= 0.9536939)

m.c122 = Constraint(expr= - m.x93 + m.x129 >= 0.9004898)

m.c123 = Constraint(expr= - m.x94 + m.x130 >= 0.9004898)

m.c124 = Constraint(expr= - m.x93 + m.x131 >= 0.9114032)

m.c125 = Constraint(expr= - m.x94 + m.x132 >= 0.9114032)

m.c126 = Constraint(expr= - m.x93 + m.x133 >= 0.90071532)

m.c127 = Constraint(expr= - m.x94 + m.x134 >= 0.90071532)

m.c128 = Constraint(expr= - m.x93 + m.x135 >= 0.88043054)

m.c129 = Constraint(expr= - m.x94 + m.x136 >= 0.88043054)

m.c130 = Constraint(expr= - m.x93 + m.x137 >= 0.8680249)

m.c131 = Constraint(expr= - m.x94 + m.x138 >= 0.8680249)

m.c132 = Constraint(expr= - m.x93 + m.x139 >= 0.81034814)

m.c133 = Constraint(expr= - m.x94 + m.x140 >= 0.81034814)

m.c134 = Constraint(expr= - m.x93 + m.x141 >= 0.80843127)

m.c135 = Constraint(expr= - m.x94 + m.x142 >= 0.80843127)

m.c136 = Constraint(expr= - m.x93 + m.x145 >= 0.79930922)

m.c137 = Constraint(expr= - m.x94 + m.x146 >= 0.79930922)

m.c138 = Constraint(expr= - m.x93 + m.x147 >= 0.84280733)

m.c139 = Constraint(expr= - m.x94 + m.x148 >= 0.84280733)

m.c140 = Constraint(expr= - m.x93 + m.x149 >= 0.81379236)

m.c141 = Constraint(expr= - m.x94 + m.x150 >= 0.81379236)

m.c142 = Constraint(expr= - m.x93 + m.x151 >= 0.82457178)

m.c143 = Constraint(expr= - m.x94 + m.x152 >= 0.82457178)

m.c144 = Constraint(expr= - m.x93 + m.x153 >= 0.80226439)

m.c145 = Constraint(expr= - m.x94 + m.x154 >= 0.80226439)

m.c146 = Constraint(expr=   m.x31 - m.x95 - m.x125 == 0)

m.c147 = Constraint(expr=   m.x32 - m.x96 - m.x126 == 0)

m.c148 = Constraint(expr=   m.x33 - m.x97 - m.x127 == 0)

m.c149 = Constraint(expr=   m.x34 - m.x98 - m.x128 == 0)

m.c150 = Constraint(expr=   m.x35 - m.x99 - m.x129 == 0)

m.c151 = Constraint(expr=   m.x36 - m.x100 - m.x130 == 0)

m.c152 = Constraint(expr=   m.x37 - m.x101 - m.x131 == 0)

m.c153 = Constraint(expr=   m.x38 - m.x102 - m.x132 == 0)

m.c154 = Constraint(expr=   m.x39 - m.x103 - m.x133 == 0)

m.c155 = Constraint(expr=   m.x40 - m.x104 - m.x134 == 0)

m.c156 = Constraint(expr=   m.x41 - m.x105 - m.x135 == 0)

m.c157 = Constraint(expr=   m.x42 - m.x106 - m.x136 == 0)

m.c158 = Constraint(expr=   m.x43 - m.x107 - m.x137 == 0)

m.c159 = Constraint(expr=   m.x44 - m.x108 - m.x138 == 0)

m.c160 = Constraint(expr=   m.x45 - m.x109 - m.x139 == 0)

m.c161 = Constraint(expr=   m.x46 - m.x110 - m.x140 == 0)

m.c162 = Constraint(expr=   m.x47 - m.x111 - m.x141 == 0)

m.c163 = Constraint(expr=   m.x48 - m.x112 - m.x142 == 0)

m.c164 = Constraint(expr=   m.x49 - m.x113 - m.x143 == 0)

m.c165 = Constraint(expr=   m.x50 - m.x114 - m.x144 == 0)

m.c166 = Constraint(expr=   m.x51 - m.x115 - m.x145 == 0)

m.c167 = Constraint(expr=   m.x52 - m.x116 - m.x146 == 0)

m.c168 = Constraint(expr=   m.x53 - m.x117 - m.x147 == 0)

m.c169 = Constraint(expr=   m.x54 - m.x118 - m.x148 == 0)

m.c170 = Constraint(expr=   m.x55 - m.x119 - m.x149 == 0)

m.c171 = Constraint(expr=   m.x56 - m.x120 - m.x150 == 0)

m.c172 = Constraint(expr=   m.x57 - m.x121 - m.x151 == 0)

m.c173 = Constraint(expr=   m.x58 - m.x122 - m.x152 == 0)

m.c174 = Constraint(expr=   m.x59 - m.x123 - m.x153 == 0)

m.c175 = Constraint(expr=   m.x60 - m.x124 - m.x154 == 0)

m.c176 = Constraint(expr=   m.b177 + m.b178 >= 1)

m.c177 = Constraint(expr=   m.b175 + m.b180 >= 1)

m.c178 = Constraint(expr=   m.b174 + m.b178 >= 1)

m.c179 = Constraint(expr=   m.b174 + m.b177 + m.b179 >= 1)

m.c180 = Constraint(expr=   m.b174 + m.b176 + m.b180 >= 1)

m.c181 = Constraint(expr=   m.b174 + m.b175 >= 1)

m.c182 = Constraint(expr=   m.b173 + m.b180 >= 1)

m.c183 = Constraint(expr=   m.b173 + m.b177 >= 1)

m.c184 = Constraint(expr=   m.b172 + m.b179 >= 1)

m.c185 = Constraint(expr=   m.b172 + m.b177 + m.b180 >= 1)

m.c186 = Constraint(expr=   m.b172 + m.b176 >= 1)

m.c187 = Constraint(expr=   m.b172 + m.b174 + m.b180 >= 1)

m.c188 = Constraint(expr=   m.b172 + m.b174 + m.b177 >= 1)

m.c189 = Constraint(expr=   m.b172 + m.b173 >= 1)

m.c190 = Constraint(expr=   m.b171 + m.b179 >= 1)

m.c191 = Constraint(expr=   m.b171 + m.b177 + m.b180 >= 1)

m.c192 = Constraint(expr=   m.b171 + m.b176 >= 1)

m.c193 = Constraint(expr=   m.b171 + m.b174 >= 1)

m.c194 = Constraint(expr=   m.b171 + m.b172 >= 1)

m.c195 = Constraint(expr=   m.b170 + m.b179 >= 1)

m.c196 = Constraint(expr=   m.b170 + m.b177 + m.b180 >= 1)

m.c197 = Constraint(expr=   m.b170 + m.b176 >= 1)

m.c198 = Constraint(expr=   m.b170 + m.b174 + m.b180 >= 1)

m.c199 = Constraint(expr=   m.b170 + m.b174 + m.b177 >= 1)

m.c200 = Constraint(expr=   m.b170 + m.b173 >= 1)

m.c201 = Constraint(expr=   m.b170 + m.b172 >= 1)

m.c202 = Constraint(expr=   m.b170 + m.b171 >= 1)

m.c203 = Constraint(expr=   m.b180 + m.b185 >= 1)

m.c204 = Constraint(expr=   m.b180 + m.b184 + m.b186 >= 1)

m.c205 = Constraint(expr=   m.b180 + m.b183 + m.b187 >= 1)

m.c206 = Constraint(expr=   m.b180 + m.b182 >= 1)

m.c207 = Constraint(expr=   m.b180 + m.b181 + m.b187 >= 1)

m.c208 = Constraint(expr=   m.b180 + m.b181 + m.b184 >= 1)

m.c209 = Constraint(expr=   m.b179 + m.b186 >= 1)

m.c210 = Constraint(expr=   m.b179 + m.b184 + m.b187 >= 1)

m.c211 = Constraint(expr=   m.b179 + m.b183 >= 1)

m.c212 = Constraint(expr=   m.b179 + m.b181 >= 1)

m.c213 = Constraint(expr=   m.b178 + m.b187 >= 1)

m.c214 = Constraint(expr=   m.b178 + m.b184 >= 1)

m.c215 = Constraint(expr=   m.b178 + m.b181 >= 1)

m.c216 = Constraint(expr=   m.b177 + m.b185 >= 1)

m.c217 = Constraint(expr=   m.b177 + m.b184 + m.b186 >= 1)

m.c218 = Constraint(expr=   m.b177 + m.b183 + m.b187 >= 1)

m.c219 = Constraint(expr=   m.b177 + m.b182 >= 1)

m.c220 = Constraint(expr=   m.b177 + m.b181 + m.b187 >= 1)

m.c221 = Constraint(expr=   m.b177 + m.b181 + m.b184 >= 1)

m.c222 = Constraint(expr=   m.b177 + m.b180 + m.b186 >= 1)

m.c223 = Constraint(expr=   m.b177 + m.b180 + m.b184 + m.b187 >= 1)

m.c224 = Constraint(expr=   m.b177 + m.b180 + m.b183 >= 1)

m.c225 = Constraint(expr=   m.b177 + m.b180 + m.b181 >= 1)

m.c226 = Constraint(expr=   m.b177 + m.b179 + m.b187 >= 1)

m.c227 = Constraint(expr=   m.b177 + m.b179 + m.b184 >= 1)

m.c228 = Constraint(expr=   m.b177 + m.b179 + m.b181 >= 1)

m.c229 = Constraint(expr=   m.b176 + m.b186 >= 1)

m.c230 = Constraint(expr=   m.b176 + m.b184 + m.b187 >= 1)

m.c231 = Constraint(expr=   m.b176 + m.b183 >= 1)

m.c232 = Constraint(expr=   m.b176 + m.b181 >= 1)

m.c233 = Constraint(expr=   m.b176 + m.b180 + m.b187 >= 1)

m.c234 = Constraint(expr=   m.b176 + m.b180 + m.b184 >= 1)

m.c235 = Constraint(expr=   m.b176 + m.b180 + m.b181 >= 1)

m.c236 = Constraint(expr=   m.b176 + m.b179 + m.b187 >= 1)

m.c237 = Constraint(expr=   m.b176 + m.b179 + m.b184 >= 1)

m.c238 = Constraint(expr=   m.b176 + m.b179 + m.b181 >= 1)

m.c239 = Constraint(expr=   m.b175 + m.b187 >= 1)

m.c240 = Constraint(expr=   m.b175 + m.b184 >= 1)

m.c241 = Constraint(expr=   m.b175 + m.b181 >= 1)

m.c242 = Constraint(expr=   m.b174 + m.b185 >= 1)

m.c243 = Constraint(expr=   m.b174 + m.b184 + m.b186 >= 1)

m.c244 = Constraint(expr=   m.b174 + m.b183 + m.b187 >= 1)

m.c245 = Constraint(expr=   m.b174 + m.b182 >= 1)

m.c246 = Constraint(expr=   m.b174 + m.b181 + m.b187 >= 1)

m.c247 = Constraint(expr=   m.b174 + m.b181 + m.b184 >= 1)

m.c248 = Constraint(expr=   m.b174 + m.b180 + m.b186 >= 1)

m.c249 = Constraint(expr=   m.b174 + m.b180 + m.b184 + m.b187 >= 1)

m.c250 = Constraint(expr=   m.b174 + m.b180 + m.b183 >= 1)

m.c251 = Constraint(expr=   m.b174 + m.b180 + m.b181 >= 1)

m.c252 = Constraint(expr=   m.b174 + m.b179 + m.b187 >= 1)

m.c253 = Constraint(expr=   m.b174 + m.b179 + m.b184 >= 1)

m.c254 = Constraint(expr=   m.b174 + m.b179 + m.b181 >= 1)

m.c255 = Constraint(expr=   m.b174 + m.b177 + m.b186 >= 1)

m.c256 = Constraint(expr=   m.b174 + m.b177 + m.b184 + m.b187 >= 1)

m.c257 = Constraint(expr=   m.b174 + m.b177 + m.b183 >= 1)

m.c258 = Constraint(expr=   m.b174 + m.b177 + m.b181 >= 1)

m.c259 = Constraint(expr=   m.b174 + m.b177 + m.b180 + m.b187 >= 1)

m.c260 = Constraint(expr=   m.b174 + m.b177 + m.b180 + m.b184 >= 1)

m.c261 = Constraint(expr=   m.b174 + m.b177 + m.b180 + m.b181 >= 1)

m.c262 = Constraint(expr=   m.b174 + m.b176 + m.b187 >= 1)

m.c263 = Constraint(expr=   m.b174 + m.b176 + m.b184 >= 1)

m.c264 = Constraint(expr=   m.b174 + m.b176 + m.b181 >= 1)

m.c265 = Constraint(expr=   m.b173 + m.b187 >= 1)

m.c266 = Constraint(expr=   m.b173 + m.b184 >= 1)

m.c267 = Constraint(expr=   m.b173 + m.b181 >= 1)

m.c268 = Constraint(expr=   m.b172 + m.b186 >= 1)

m.c269 = Constraint(expr=   m.b172 + m.b184 + m.b187 >= 1)

m.c270 = Constraint(expr=   m.b172 + m.b183 >= 1)

m.c271 = Constraint(expr=   m.b172 + m.b181 >= 1)

m.c272 = Constraint(expr=   m.b172 + m.b180 + m.b187 >= 1)

m.c273 = Constraint(expr=   m.b172 + m.b180 + m.b184 >= 1)

m.c274 = Constraint(expr=   m.b172 + m.b180 + m.b181 >= 1)

m.c275 = Constraint(expr=   m.b172 + m.b177 + m.b187 >= 1)

m.c276 = Constraint(expr=   m.b172 + m.b177 + m.b184 >= 1)

m.c277 = Constraint(expr=   m.b172 + m.b177 + m.b181 >= 1)

m.c278 = Constraint(expr=   m.b172 + m.b174 + m.b187 >= 1)

m.c279 = Constraint(expr=   m.b172 + m.b174 + m.b184 >= 1)

m.c280 = Constraint(expr=   m.b172 + m.b174 + m.b181 >= 1)

m.c281 = Constraint(expr=   m.b171 + m.b186 >= 1)

m.c282 = Constraint(expr=   m.b171 + m.b184 + m.b187 >= 1)

m.c283 = Constraint(expr=   m.b171 + m.b183 >= 1)

m.c284 = Constraint(expr=   m.b171 + m.b181 >= 1)

m.c285 = Constraint(expr=   m.b171 + m.b180 + m.b187 >= 1)

m.c286 = Constraint(expr=   m.b171 + m.b180 + m.b184 >= 1)

m.c287 = Constraint(expr=   m.b171 + m.b180 + m.b181 >= 1)

m.c288 = Constraint(expr=   m.b171 + m.b177 + m.b187 >= 1)

m.c289 = Constraint(expr=   m.b171 + m.b177 + m.b184 >= 1)

m.c290 = Constraint(expr=   m.b171 + m.b177 + m.b181 >= 1)

m.c291 = Constraint(expr=   m.b170 + m.b186 >= 1)

m.c292 = Constraint(expr=   m.b170 + m.b184 + m.b187 >= 1)

m.c293 = Constraint(expr=   m.b170 + m.b183 >= 1)

m.c294 = Constraint(expr=   m.b170 + m.b181 >= 1)

m.c295 = Constraint(expr=   m.b170 + m.b180 + m.b187 >= 1)

m.c296 = Constraint(expr=   m.b170 + m.b180 + m.b184 >= 1)

m.c297 = Constraint(expr=   m.b170 + m.b180 + m.b181 >= 1)

m.c298 = Constraint(expr=   m.b170 + m.b177 + m.b187 >= 1)

m.c299 = Constraint(expr=   m.b170 + m.b177 + m.b184 >= 1)

m.c300 = Constraint(expr=   m.b170 + m.b177 + m.b181 >= 1)

m.c301 = Constraint(expr=   m.b170 + m.b174 + m.b187 >= 1)

m.c302 = Constraint(expr=   m.b170 + m.b174 + m.b184 >= 1)

m.c303 = Constraint(expr=   m.b170 + m.b174 + m.b181 >= 1)

m.c304 = Constraint(expr=   m.b173 - m.b174 >= 0)

m.c305 = Constraint(expr=   m.b175 - m.b176 >= 0)

m.c306 = Constraint(expr=   m.b176 - m.b177 >= 0)

m.c307 = Constraint(expr=   m.b178 - m.b179 >= 0)

m.c308 = Constraint(expr=   m.b179 - m.b180 >= 0)

m.c309 = Constraint(expr=   m.b182 - m.b183 >= 0)

m.c310 = Constraint(expr=   m.b183 - m.b184 >= 0)

m.c311 = Constraint(expr=   m.b185 - m.b186 >= 0)

m.c312 = Constraint(expr=   m.b186 - m.b187 >= 0)

m.c313 = Constraint(expr=   m.b188 - m.b189 >= 0)

m.c314 = Constraint(expr=   m.b189 - m.b190 >= 0)

m.c315 = Constraint(expr=   m.b190 - m.b191 >= 0)

m.c316 = Constraint(expr=   m.b192 - m.b193 >= 0)

m.c317 = Constraint(expr=   m.b193 - m.b194 >= 0)

m.c318 = Constraint(expr=   m.b198 - m.b199 >= 0)

m.c319 = Constraint(expr=   m.x93 - m.x94 >= 0)

m.c320 = Constraint(expr=   m.x61 - 0.1*m.b170 == 1.92)

m.c321 = Constraint(expr=   m.x62 - 0.193333333333333*m.b171 == 3.82)

m.c322 = Constraint(expr=   m.x63 - 0.226666666666667*m.b172 == 4.53333333333333)

m.c323 = Constraint(expr=   m.x64 - 0.286666666666667*m.b173 - 0.28*m.b174 == 5.39333333333333)

m.c324 = Constraint(expr=   m.x65 - 1.91333333333333*m.b175 - 1.91333333333333*m.b176 - 1.91333333333333*m.b177
                          == 36.3533333333333)

m.c325 = Constraint(expr=   m.x66 - 4.50666666666667*m.b178 - 4.51333333333333*m.b179 - 4.51333333333333*m.b180
                          == 85.7466666666667)

m.c326 = Constraint(expr=   m.x67 - 0.313333333333333*m.b181 == 6.28)

m.c327 = Constraint(expr=   m.x68 - 2.80666666666667*m.b182 - 2.81333333333333*m.b183 - 2.81333333333333*m.b184
                          == 53.4333333333333)

m.c328 = Constraint(expr=   m.x69 - 2.56*m.b185 - 2.56*m.b186 - 2.55333333333333*m.b187 == 48.6133333333333)

m.c329 = Constraint(expr=   m.x70 - 1.88666666666667*m.b188 - 1.88666666666667*m.b189 - 1.88666666666667*m.b190
                          - 1.88666666666667*m.b191 == 33.9533333333333)

m.c330 = Constraint(expr=   m.x71 - 2.84*m.b192 - 2.84*m.b193 - 2.84666666666667*m.b194 == 53.9666666666667)

m.c331 = Constraint(expr=   m.x72 - 3.85333333333333*m.b195 == 77.0533333333333)

m.c332 = Constraint(expr=   m.x73 - 1.24*m.b196 == 24.9066666666667)

m.c333 = Constraint(expr=   m.x74 - 1.81333333333333*m.b197 == 36.1866666666667)

m.c334 = Constraint(expr=   m.x75 - 2.96*m.b198 - 2.96666666666667*m.b199 == 56.3133333333333)

m.c335 = Constraint(expr= - m.x76 + m.x155 <= 0)

m.c336 = Constraint(expr= - m.x77 + m.x156 <= 0)

m.c337 = Constraint(expr= - m.x78 + m.x157 <= 0)

m.c338 = Constraint(expr= - m.x79 + m.x158 <= 0)

m.c339 = Constraint(expr= - m.x80 + m.x159 <= 0)

m.c340 = Constraint(expr= - m.x81 + m.x160 <= 0)

m.c341 = Constraint(expr= - m.x82 + m.x161 <= 0)

m.c342 = Constraint(expr= - m.x83 + m.x162 <= 0)

m.c343 = Constraint(expr= - m.x84 + m.x163 <= 0)

m.c344 = Constraint(expr= - m.x85 + m.x164 <= 0)

m.c345 = Constraint(expr= - m.x86 + m.x165 <= 0)

m.c346 = Constraint(expr= - m.x87 + m.x166 <= 0)

m.c347 = Constraint(expr= - m.x88 + m.x167 <= 0)

m.c348 = Constraint(expr= - m.x89 + m.x168 <= 0)

m.c349 = Constraint(expr= - m.x90 + m.x169 <= 0)
