#  MINLP written by GAMS Convert at 04/21/18 13:54:11
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        394       46      316       32        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        215      155       60        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1004      914       90        0
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
m.x31 = Var(within=Reals,bounds=(1.92,2.02),initialize=1.92)
m.x32 = Var(within=Reals,bounds=(3.82,4.01333333333333),initialize=3.82)
m.x33 = Var(within=Reals,bounds=(4.53333333333333,4.76),initialize=4.53333333333333)
m.x34 = Var(within=Reals,bounds=(5.39333333333333,5.96),initialize=5.39333333333333)
m.x35 = Var(within=Reals,bounds=(36.3533333333333,42.0933333333333),initialize=36.3533333333333)
m.x36 = Var(within=Reals,bounds=(85.7466666666667,99.28),initialize=85.7466666666667)
m.x37 = Var(within=Reals,bounds=(6.28,6.59333333333333),initialize=6.28)
m.x38 = Var(within=Reals,bounds=(53.4333333333333,61.8666666666667),initialize=53.4333333333333)
m.x39 = Var(within=Reals,bounds=(48.6133333333333,56.2866666666667),initialize=48.6133333333333)
m.x40 = Var(within=Reals,bounds=(33.9533333333333,41.5),initialize=33.9533333333333)
m.x41 = Var(within=Reals,bounds=(53.9666666666667,62.4933333333333),initialize=53.9666666666667)
m.x42 = Var(within=Reals,bounds=(77.0533333333333,80.9066666666667),initialize=77.0533333333333)
m.x43 = Var(within=Reals,bounds=(24.9066666666667,26.1466666666667),initialize=24.9066666666667)
m.x44 = Var(within=Reals,bounds=(36.1866666666667,38),initialize=36.1866666666667)
m.x45 = Var(within=Reals,bounds=(56.3133333333333,62.24),initialize=56.3133333333333)
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
m.b69 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b70 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b71 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b72 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b73 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b74 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b75 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x156 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
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
m.b200 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b201 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b202 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b203 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b204 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b205 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b206 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b207 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b208 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b209 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b210 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b211 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b212 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b213 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b214 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   m.x76 + m.x77 + m.x78 + m.x79 + m.x80 + m.x81 + m.x82 + m.x83 + m.x84 + m.x85 + m.x86 + m.x87
                        + m.x88 + m.x89 + m.x90, sense=minimize)

m.c2 = Constraint(expr=-m.x31*m.x1*m.b46 + m.x155 >= 0)

m.c3 = Constraint(expr=-m.x31*m.x2*m.b47 + m.x156 >= 0)

m.c4 = Constraint(expr=-m.x32*m.x3*m.b48 + m.x157 >= 0)

m.c5 = Constraint(expr=-m.x32*m.x4*m.b49 + m.x158 >= 0)

m.c6 = Constraint(expr=-m.x33*m.x5*m.b50 + m.x159 >= 0)

m.c7 = Constraint(expr=-m.x33*m.x6*m.b51 + m.x160 >= 0)

m.c8 = Constraint(expr=-m.x34*m.x7*m.b52 + m.x161 >= 0)

m.c9 = Constraint(expr=-m.x34*m.x8*m.b53 + m.x162 >= 0)

m.c10 = Constraint(expr=-m.x35*m.x9*m.b54 + m.x163 >= 0)

m.c11 = Constraint(expr=-m.x35*m.x10*m.b55 + m.x164 >= 0)

m.c12 = Constraint(expr=-m.x36*m.x11*m.b56 + m.x165 >= 0)

m.c13 = Constraint(expr=-m.x36*m.x12*m.b57 + m.x166 >= 0)

m.c14 = Constraint(expr=-m.x37*m.x13*m.b58 + m.x167 >= 0)

m.c15 = Constraint(expr=-m.x37*m.x14*m.b59 + m.x168 >= 0)

m.c16 = Constraint(expr=-m.x38*m.x15*m.b60 + m.x169 >= 0)

m.c17 = Constraint(expr=-m.x38*m.x16*m.b61 + m.x170 >= 0)

m.c18 = Constraint(expr=-m.x39*m.x17*m.b62 + m.x171 >= 0)

m.c19 = Constraint(expr=-m.x39*m.x18*m.b63 + m.x172 >= 0)

m.c20 = Constraint(expr=-m.x40*m.x19*m.b64 + m.x173 >= 0)

m.c21 = Constraint(expr=-m.x40*m.x20*m.b65 + m.x174 >= 0)

m.c22 = Constraint(expr=-m.x41*m.x21*m.b66 + m.x175 >= 0)

m.c23 = Constraint(expr=-m.x41*m.x22*m.b67 + m.x176 >= 0)

m.c24 = Constraint(expr=-m.x42*m.x23*m.b68 + m.x177 >= 0)

m.c25 = Constraint(expr=-m.x42*m.x24*m.b69 + m.x178 >= 0)

m.c26 = Constraint(expr=-m.x43*m.x25*m.b70 + m.x179 >= 0)

m.c27 = Constraint(expr=-m.x43*m.x26*m.b71 + m.x180 >= 0)

m.c28 = Constraint(expr=-m.x44*m.x27*m.b72 + m.x181 >= 0)

m.c29 = Constraint(expr=-m.x44*m.x28*m.b73 + m.x182 >= 0)

m.c30 = Constraint(expr=-m.x45*m.x29*m.b74 + m.x183 >= 0)

m.c31 = Constraint(expr=-m.x45*m.x30*m.b75 + m.x184 >= 0)

m.c32 = Constraint(expr=   m.b46 + m.b47 == 1)

m.c33 = Constraint(expr=   m.b48 + m.b49 == 1)

m.c34 = Constraint(expr=   m.b50 + m.b51 == 1)

m.c35 = Constraint(expr=   m.b52 + m.b53 == 1)

m.c36 = Constraint(expr=   m.b54 + m.b55 == 1)

m.c37 = Constraint(expr=   m.b56 + m.b57 == 1)

m.c38 = Constraint(expr=   m.b58 + m.b59 == 1)

m.c39 = Constraint(expr=   m.b60 + m.b61 == 1)

m.c40 = Constraint(expr=   m.b62 + m.b63 == 1)

m.c41 = Constraint(expr=   m.b64 + m.b65 == 1)

m.c42 = Constraint(expr=   m.b66 + m.b67 == 1)

m.c43 = Constraint(expr=   m.b68 + m.b69 == 1)

m.c44 = Constraint(expr=   m.b70 + m.b71 == 1)

m.c45 = Constraint(expr=   m.b72 + m.b73 == 1)

m.c46 = Constraint(expr=   m.b74 + m.b75 == 1)

m.c47 = Constraint(expr=   2.02*m.b46 + 4.01333333333333*m.b48 + 4.76*m.b50 + 5.96*m.b52 + 42.0933333333333*m.b54
                         + 99.28*m.b56 + 6.59333333333333*m.b58 + 61.8666666666667*m.b60 + 56.2866666666667*m.b62
                         + 41.5*m.b64 + 62.4933333333333*m.b66 + 80.9066666666667*m.b68 + 26.1466666666667*m.b70
                         + 38*m.b72 + 62.24*m.b74 <= 302.08)

m.c48 = Constraint(expr=   2.02*m.b47 + 4.01333333333333*m.b49 + 4.76*m.b51 + 5.96*m.b53 + 42.0933333333333*m.b55
                         + 99.28*m.b57 + 6.59333333333333*m.b59 + 61.8666666666667*m.b61 + 56.2866666666667*m.b63
                         + 41.5*m.b65 + 62.4933333333333*m.b67 + 80.9066666666667*m.b69 + 26.1466666666667*m.b71
                         + 38*m.b73 + 62.24*m.b75 <= 302.08)

m.c49 = Constraint(expr=   m.x91 + m.x95 >= 0.29424122)

m.c50 = Constraint(expr=   m.x92 + m.x96 >= 0.29424122)

m.c51 = Constraint(expr=   m.x91 + m.x97 >= 0.29760193)

m.c52 = Constraint(expr=   m.x92 + m.x98 >= 0.29760193)

m.c53 = Constraint(expr=   m.x91 + m.x99 >= 0.35149534)

m.c54 = Constraint(expr=   m.x92 + m.x100 >= 0.35149534)

m.c55 = Constraint(expr=   m.x91 + m.x101 >= 0.30458283)

m.c56 = Constraint(expr=   m.x92 + m.x102 >= 0.30458283)

m.c57 = Constraint(expr=   m.x91 + m.x103 >= 0.29951066)

m.c58 = Constraint(expr=   m.x92 + m.x104 >= 0.29951066)

m.c59 = Constraint(expr=   m.x91 + m.x105 >= 0.30694357)

m.c60 = Constraint(expr=   m.x92 + m.x106 >= 0.30694357)

m.c61 = Constraint(expr=   m.x91 + m.x107 >= 0.33520661)

m.c62 = Constraint(expr=   m.x92 + m.x108 >= 0.33520661)

m.c63 = Constraint(expr=   m.x91 + m.x109 >= 0.3400071)

m.c64 = Constraint(expr=   m.x92 + m.x110 >= 0.3400071)

m.c65 = Constraint(expr=   m.x91 + m.x111 >= 0.35227087)

m.c66 = Constraint(expr=   m.x92 + m.x112 >= 0.35227087)

m.c67 = Constraint(expr=   m.x91 + m.x113 >= 0.34225726)

m.c68 = Constraint(expr=   m.x92 + m.x114 >= 0.34225726)

m.c69 = Constraint(expr=   m.x91 + m.x115 >= 0.32776566)

m.c70 = Constraint(expr=   m.x92 + m.x116 >= 0.32776566)

m.c71 = Constraint(expr=   m.x91 + m.x117 >= 0.30438256)

m.c72 = Constraint(expr=   m.x92 + m.x118 >= 0.30438256)

m.c73 = Constraint(expr=   m.x91 + m.x119 >= 0.28538336)

m.c74 = Constraint(expr=   m.x92 + m.x120 >= 0.28538336)

m.c75 = Constraint(expr=   m.x91 + m.x121 >= 0.27950575)

m.c76 = Constraint(expr=   m.x92 + m.x122 >= 0.27950575)

m.c77 = Constraint(expr= - m.x91 + m.x95 >= -0.29424122)

m.c78 = Constraint(expr= - m.x92 + m.x96 >= -0.29424122)

m.c79 = Constraint(expr= - m.x91 + m.x97 >= -0.29760193)

m.c80 = Constraint(expr= - m.x92 + m.x98 >= -0.29760193)

m.c81 = Constraint(expr= - m.x91 + m.x99 >= -0.35149534)

m.c82 = Constraint(expr= - m.x92 + m.x100 >= -0.35149534)

m.c83 = Constraint(expr= - m.x91 + m.x101 >= -0.30458283)

m.c84 = Constraint(expr= - m.x92 + m.x102 >= -0.30458283)

m.c85 = Constraint(expr= - m.x91 + m.x103 >= -0.29951066)

m.c86 = Constraint(expr= - m.x92 + m.x104 >= -0.29951066)

m.c87 = Constraint(expr= - m.x91 + m.x105 >= -0.30694357)

m.c88 = Constraint(expr= - m.x92 + m.x106 >= -0.30694357)

m.c89 = Constraint(expr= - m.x91 + m.x107 >= -0.33520661)

m.c90 = Constraint(expr= - m.x92 + m.x108 >= -0.33520661)

m.c91 = Constraint(expr= - m.x91 + m.x109 >= -0.3400071)

m.c92 = Constraint(expr= - m.x92 + m.x110 >= -0.3400071)

m.c93 = Constraint(expr= - m.x91 + m.x113 >= -0.34225726)

m.c94 = Constraint(expr= - m.x92 + m.x114 >= -0.34225726)

m.c95 = Constraint(expr= - m.x91 + m.x115 >= -0.32776566)

m.c96 = Constraint(expr= - m.x92 + m.x116 >= -0.32776566)

m.c97 = Constraint(expr= - m.x91 + m.x117 >= -0.30438256)

m.c98 = Constraint(expr= - m.x92 + m.x118 >= -0.30438256)

m.c99 = Constraint(expr= - m.x91 + m.x119 >= -0.28538336)

m.c100 = Constraint(expr= - m.x92 + m.x120 >= -0.28538336)

m.c101 = Constraint(expr= - m.x91 + m.x121 >= -0.27950575)

m.c102 = Constraint(expr= - m.x92 + m.x122 >= -0.27950575)

m.c103 = Constraint(expr= - m.x91 + m.x123 >= -0.25788969)

m.c104 = Constraint(expr= - m.x92 + m.x124 >= -0.25788969)

m.c105 = Constraint(expr=   m.x93 + m.x127 >= -0.9536939)

m.c106 = Constraint(expr=   m.x94 + m.x128 >= -0.9536939)

m.c107 = Constraint(expr=   m.x93 + m.x129 >= -0.9004898)

m.c108 = Constraint(expr=   m.x94 + m.x130 >= -0.9004898)

m.c109 = Constraint(expr=   m.x93 + m.x131 >= -0.9114032)

m.c110 = Constraint(expr=   m.x94 + m.x132 >= -0.9114032)

m.c111 = Constraint(expr=   m.x93 + m.x133 >= -0.90071532)

m.c112 = Constraint(expr=   m.x94 + m.x134 >= -0.90071532)

m.c113 = Constraint(expr=   m.x93 + m.x135 >= -0.88043054)

m.c114 = Constraint(expr=   m.x94 + m.x136 >= -0.88043054)

m.c115 = Constraint(expr=   m.x93 + m.x137 >= -0.8680249)

m.c116 = Constraint(expr=   m.x94 + m.x138 >= -0.8680249)

m.c117 = Constraint(expr=   m.x93 + m.x139 >= -0.81034814)

m.c118 = Constraint(expr=   m.x94 + m.x140 >= -0.81034814)

m.c119 = Constraint(expr=   m.x93 + m.x141 >= -0.80843127)

m.c120 = Constraint(expr=   m.x94 + m.x142 >= -0.80843127)

m.c121 = Constraint(expr=   m.x93 + m.x143 >= -0.7794471)

m.c122 = Constraint(expr=   m.x94 + m.x144 >= -0.7794471)

m.c123 = Constraint(expr=   m.x93 + m.x145 >= -0.79930922)

m.c124 = Constraint(expr=   m.x94 + m.x146 >= -0.79930922)

m.c125 = Constraint(expr=   m.x93 + m.x147 >= -0.84280733)

m.c126 = Constraint(expr=   m.x94 + m.x148 >= -0.84280733)

m.c127 = Constraint(expr=   m.x93 + m.x149 >= -0.81379236)

m.c128 = Constraint(expr=   m.x94 + m.x150 >= -0.81379236)

m.c129 = Constraint(expr=   m.x93 + m.x151 >= -0.82457178)

m.c130 = Constraint(expr=   m.x94 + m.x152 >= -0.82457178)

m.c131 = Constraint(expr=   m.x93 + m.x153 >= -0.80226439)

m.c132 = Constraint(expr=   m.x94 + m.x154 >= -0.80226439)

m.c133 = Constraint(expr= - m.x93 + m.x125 >= 0.98493628)

m.c134 = Constraint(expr= - m.x94 + m.x126 >= 0.98493628)

m.c135 = Constraint(expr= - m.x93 + m.x127 >= 0.9536939)

m.c136 = Constraint(expr= - m.x94 + m.x128 >= 0.9536939)

m.c137 = Constraint(expr= - m.x93 + m.x129 >= 0.9004898)

m.c138 = Constraint(expr= - m.x94 + m.x130 >= 0.9004898)

m.c139 = Constraint(expr= - m.x93 + m.x131 >= 0.9114032)

m.c140 = Constraint(expr= - m.x94 + m.x132 >= 0.9114032)

m.c141 = Constraint(expr= - m.x93 + m.x133 >= 0.90071532)

m.c142 = Constraint(expr= - m.x94 + m.x134 >= 0.90071532)

m.c143 = Constraint(expr= - m.x93 + m.x135 >= 0.88043054)

m.c144 = Constraint(expr= - m.x94 + m.x136 >= 0.88043054)

m.c145 = Constraint(expr= - m.x93 + m.x137 >= 0.8680249)

m.c146 = Constraint(expr= - m.x94 + m.x138 >= 0.8680249)

m.c147 = Constraint(expr= - m.x93 + m.x139 >= 0.81034814)

m.c148 = Constraint(expr= - m.x94 + m.x140 >= 0.81034814)

m.c149 = Constraint(expr= - m.x93 + m.x141 >= 0.80843127)

m.c150 = Constraint(expr= - m.x94 + m.x142 >= 0.80843127)

m.c151 = Constraint(expr= - m.x93 + m.x145 >= 0.79930922)

m.c152 = Constraint(expr= - m.x94 + m.x146 >= 0.79930922)

m.c153 = Constraint(expr= - m.x93 + m.x147 >= 0.84280733)

m.c154 = Constraint(expr= - m.x94 + m.x148 >= 0.84280733)

m.c155 = Constraint(expr= - m.x93 + m.x149 >= 0.81379236)

m.c156 = Constraint(expr= - m.x94 + m.x150 >= 0.81379236)

m.c157 = Constraint(expr= - m.x93 + m.x151 >= 0.82457178)

m.c158 = Constraint(expr= - m.x94 + m.x152 >= 0.82457178)

m.c159 = Constraint(expr= - m.x93 + m.x153 >= 0.80226439)

m.c160 = Constraint(expr= - m.x94 + m.x154 >= 0.80226439)

m.c161 = Constraint(expr=   m.x1 - m.x95 - m.x125 == 0)

m.c162 = Constraint(expr=   m.x2 - m.x96 - m.x126 == 0)

m.c163 = Constraint(expr=   m.x3 - m.x97 - m.x127 == 0)

m.c164 = Constraint(expr=   m.x4 - m.x98 - m.x128 == 0)

m.c165 = Constraint(expr=   m.x5 - m.x99 - m.x129 == 0)

m.c166 = Constraint(expr=   m.x6 - m.x100 - m.x130 == 0)

m.c167 = Constraint(expr=   m.x7 - m.x101 - m.x131 == 0)

m.c168 = Constraint(expr=   m.x8 - m.x102 - m.x132 == 0)

m.c169 = Constraint(expr=   m.x9 - m.x103 - m.x133 == 0)

m.c170 = Constraint(expr=   m.x10 - m.x104 - m.x134 == 0)

m.c171 = Constraint(expr=   m.x11 - m.x105 - m.x135 == 0)

m.c172 = Constraint(expr=   m.x12 - m.x106 - m.x136 == 0)

m.c173 = Constraint(expr=   m.x13 - m.x107 - m.x137 == 0)

m.c174 = Constraint(expr=   m.x14 - m.x108 - m.x138 == 0)

m.c175 = Constraint(expr=   m.x15 - m.x109 - m.x139 == 0)

m.c176 = Constraint(expr=   m.x16 - m.x110 - m.x140 == 0)

m.c177 = Constraint(expr=   m.x17 - m.x111 - m.x141 == 0)

m.c178 = Constraint(expr=   m.x18 - m.x112 - m.x142 == 0)

m.c179 = Constraint(expr=   m.x19 - m.x113 - m.x143 == 0)

m.c180 = Constraint(expr=   m.x20 - m.x114 - m.x144 == 0)

m.c181 = Constraint(expr=   m.x21 - m.x115 - m.x145 == 0)

m.c182 = Constraint(expr=   m.x22 - m.x116 - m.x146 == 0)

m.c183 = Constraint(expr=   m.x23 - m.x117 - m.x147 == 0)

m.c184 = Constraint(expr=   m.x24 - m.x118 - m.x148 == 0)

m.c185 = Constraint(expr=   m.x25 - m.x119 - m.x149 == 0)

m.c186 = Constraint(expr=   m.x26 - m.x120 - m.x150 == 0)

m.c187 = Constraint(expr=   m.x27 - m.x121 - m.x151 == 0)

m.c188 = Constraint(expr=   m.x28 - m.x122 - m.x152 == 0)

m.c189 = Constraint(expr=   m.x29 - m.x123 - m.x153 == 0)

m.c190 = Constraint(expr=   m.x30 - m.x124 - m.x154 == 0)

m.c191 = Constraint(expr=   m.b192 + m.b193 >= 1)

m.c192 = Constraint(expr=   m.b190 + m.b195 >= 1)

m.c193 = Constraint(expr=   m.b189 + m.b193 >= 1)

m.c194 = Constraint(expr=   m.b189 + m.b192 + m.b194 >= 1)

m.c195 = Constraint(expr=   m.b189 + m.b191 + m.b195 >= 1)

m.c196 = Constraint(expr=   m.b189 + m.b190 >= 1)

m.c197 = Constraint(expr=   m.b188 + m.b195 >= 1)

m.c198 = Constraint(expr=   m.b188 + m.b192 >= 1)

m.c199 = Constraint(expr=   m.b187 + m.b194 >= 1)

m.c200 = Constraint(expr=   m.b187 + m.b192 + m.b195 >= 1)

m.c201 = Constraint(expr=   m.b187 + m.b191 >= 1)

m.c202 = Constraint(expr=   m.b187 + m.b189 + m.b195 >= 1)

m.c203 = Constraint(expr=   m.b187 + m.b189 + m.b192 >= 1)

m.c204 = Constraint(expr=   m.b187 + m.b188 >= 1)

m.c205 = Constraint(expr=   m.b186 + m.b194 >= 1)

m.c206 = Constraint(expr=   m.b186 + m.b192 + m.b195 >= 1)

m.c207 = Constraint(expr=   m.b186 + m.b191 >= 1)

m.c208 = Constraint(expr=   m.b186 + m.b189 >= 1)

m.c209 = Constraint(expr=   m.b186 + m.b187 >= 1)

m.c210 = Constraint(expr=   m.b185 + m.b194 >= 1)

m.c211 = Constraint(expr=   m.b185 + m.b192 + m.b195 >= 1)

m.c212 = Constraint(expr=   m.b185 + m.b191 >= 1)

m.c213 = Constraint(expr=   m.b185 + m.b189 + m.b195 >= 1)

m.c214 = Constraint(expr=   m.b185 + m.b189 + m.b192 >= 1)

m.c215 = Constraint(expr=   m.b185 + m.b188 >= 1)

m.c216 = Constraint(expr=   m.b185 + m.b187 >= 1)

m.c217 = Constraint(expr=   m.b185 + m.b186 >= 1)

m.c218 = Constraint(expr=   m.b195 + m.b200 >= 1)

m.c219 = Constraint(expr=   m.b195 + m.b199 + m.b201 >= 1)

m.c220 = Constraint(expr=   m.b195 + m.b198 + m.b202 >= 1)

m.c221 = Constraint(expr=   m.b195 + m.b197 >= 1)

m.c222 = Constraint(expr=   m.b195 + m.b196 + m.b202 >= 1)

m.c223 = Constraint(expr=   m.b195 + m.b196 + m.b199 >= 1)

m.c224 = Constraint(expr=   m.b194 + m.b201 >= 1)

m.c225 = Constraint(expr=   m.b194 + m.b199 + m.b202 >= 1)

m.c226 = Constraint(expr=   m.b194 + m.b198 >= 1)

m.c227 = Constraint(expr=   m.b194 + m.b196 >= 1)

m.c228 = Constraint(expr=   m.b193 + m.b202 >= 1)

m.c229 = Constraint(expr=   m.b193 + m.b199 >= 1)

m.c230 = Constraint(expr=   m.b193 + m.b196 >= 1)

m.c231 = Constraint(expr=   m.b192 + m.b200 >= 1)

m.c232 = Constraint(expr=   m.b192 + m.b199 + m.b201 >= 1)

m.c233 = Constraint(expr=   m.b192 + m.b198 + m.b202 >= 1)

m.c234 = Constraint(expr=   m.b192 + m.b197 >= 1)

m.c235 = Constraint(expr=   m.b192 + m.b196 + m.b202 >= 1)

m.c236 = Constraint(expr=   m.b192 + m.b196 + m.b199 >= 1)

m.c237 = Constraint(expr=   m.b192 + m.b195 + m.b201 >= 1)

m.c238 = Constraint(expr=   m.b192 + m.b195 + m.b199 + m.b202 >= 1)

m.c239 = Constraint(expr=   m.b192 + m.b195 + m.b198 >= 1)

m.c240 = Constraint(expr=   m.b192 + m.b195 + m.b196 >= 1)

m.c241 = Constraint(expr=   m.b192 + m.b194 + m.b202 >= 1)

m.c242 = Constraint(expr=   m.b192 + m.b194 + m.b199 >= 1)

m.c243 = Constraint(expr=   m.b192 + m.b194 + m.b196 >= 1)

m.c244 = Constraint(expr=   m.b191 + m.b201 >= 1)

m.c245 = Constraint(expr=   m.b191 + m.b199 + m.b202 >= 1)

m.c246 = Constraint(expr=   m.b191 + m.b198 >= 1)

m.c247 = Constraint(expr=   m.b191 + m.b196 >= 1)

m.c248 = Constraint(expr=   m.b191 + m.b195 + m.b202 >= 1)

m.c249 = Constraint(expr=   m.b191 + m.b195 + m.b199 >= 1)

m.c250 = Constraint(expr=   m.b191 + m.b195 + m.b196 >= 1)

m.c251 = Constraint(expr=   m.b191 + m.b194 + m.b202 >= 1)

m.c252 = Constraint(expr=   m.b191 + m.b194 + m.b199 >= 1)

m.c253 = Constraint(expr=   m.b191 + m.b194 + m.b196 >= 1)

m.c254 = Constraint(expr=   m.b190 + m.b202 >= 1)

m.c255 = Constraint(expr=   m.b190 + m.b199 >= 1)

m.c256 = Constraint(expr=   m.b190 + m.b196 >= 1)

m.c257 = Constraint(expr=   m.b189 + m.b200 >= 1)

m.c258 = Constraint(expr=   m.b189 + m.b199 + m.b201 >= 1)

m.c259 = Constraint(expr=   m.b189 + m.b198 + m.b202 >= 1)

m.c260 = Constraint(expr=   m.b189 + m.b197 >= 1)

m.c261 = Constraint(expr=   m.b189 + m.b196 + m.b202 >= 1)

m.c262 = Constraint(expr=   m.b189 + m.b196 + m.b199 >= 1)

m.c263 = Constraint(expr=   m.b189 + m.b195 + m.b201 >= 1)

m.c264 = Constraint(expr=   m.b189 + m.b195 + m.b199 + m.b202 >= 1)

m.c265 = Constraint(expr=   m.b189 + m.b195 + m.b198 >= 1)

m.c266 = Constraint(expr=   m.b189 + m.b195 + m.b196 >= 1)

m.c267 = Constraint(expr=   m.b189 + m.b194 + m.b202 >= 1)

m.c268 = Constraint(expr=   m.b189 + m.b194 + m.b199 >= 1)

m.c269 = Constraint(expr=   m.b189 + m.b194 + m.b196 >= 1)

m.c270 = Constraint(expr=   m.b189 + m.b192 + m.b201 >= 1)

m.c271 = Constraint(expr=   m.b189 + m.b192 + m.b199 + m.b202 >= 1)

m.c272 = Constraint(expr=   m.b189 + m.b192 + m.b198 >= 1)

m.c273 = Constraint(expr=   m.b189 + m.b192 + m.b196 >= 1)

m.c274 = Constraint(expr=   m.b189 + m.b192 + m.b195 + m.b202 >= 1)

m.c275 = Constraint(expr=   m.b189 + m.b192 + m.b195 + m.b199 >= 1)

m.c276 = Constraint(expr=   m.b189 + m.b192 + m.b195 + m.b196 >= 1)

m.c277 = Constraint(expr=   m.b189 + m.b191 + m.b202 >= 1)

m.c278 = Constraint(expr=   m.b189 + m.b191 + m.b199 >= 1)

m.c279 = Constraint(expr=   m.b189 + m.b191 + m.b196 >= 1)

m.c280 = Constraint(expr=   m.b188 + m.b202 >= 1)

m.c281 = Constraint(expr=   m.b188 + m.b199 >= 1)

m.c282 = Constraint(expr=   m.b188 + m.b196 >= 1)

m.c283 = Constraint(expr=   m.b187 + m.b201 >= 1)

m.c284 = Constraint(expr=   m.b187 + m.b199 + m.b202 >= 1)

m.c285 = Constraint(expr=   m.b187 + m.b198 >= 1)

m.c286 = Constraint(expr=   m.b187 + m.b196 >= 1)

m.c287 = Constraint(expr=   m.b187 + m.b195 + m.b202 >= 1)

m.c288 = Constraint(expr=   m.b187 + m.b195 + m.b199 >= 1)

m.c289 = Constraint(expr=   m.b187 + m.b195 + m.b196 >= 1)

m.c290 = Constraint(expr=   m.b187 + m.b192 + m.b202 >= 1)

m.c291 = Constraint(expr=   m.b187 + m.b192 + m.b199 >= 1)

m.c292 = Constraint(expr=   m.b187 + m.b192 + m.b196 >= 1)

m.c293 = Constraint(expr=   m.b187 + m.b189 + m.b202 >= 1)

m.c294 = Constraint(expr=   m.b187 + m.b189 + m.b199 >= 1)

m.c295 = Constraint(expr=   m.b187 + m.b189 + m.b196 >= 1)

m.c296 = Constraint(expr=   m.b186 + m.b201 >= 1)

m.c297 = Constraint(expr=   m.b186 + m.b199 + m.b202 >= 1)

m.c298 = Constraint(expr=   m.b186 + m.b198 >= 1)

m.c299 = Constraint(expr=   m.b186 + m.b196 >= 1)

m.c300 = Constraint(expr=   m.b186 + m.b195 + m.b202 >= 1)

m.c301 = Constraint(expr=   m.b186 + m.b195 + m.b199 >= 1)

m.c302 = Constraint(expr=   m.b186 + m.b195 + m.b196 >= 1)

m.c303 = Constraint(expr=   m.b186 + m.b192 + m.b202 >= 1)

m.c304 = Constraint(expr=   m.b186 + m.b192 + m.b199 >= 1)

m.c305 = Constraint(expr=   m.b186 + m.b192 + m.b196 >= 1)

m.c306 = Constraint(expr=   m.b185 + m.b201 >= 1)

m.c307 = Constraint(expr=   m.b185 + m.b199 + m.b202 >= 1)

m.c308 = Constraint(expr=   m.b185 + m.b198 >= 1)

m.c309 = Constraint(expr=   m.b185 + m.b196 >= 1)

m.c310 = Constraint(expr=   m.b185 + m.b195 + m.b202 >= 1)

m.c311 = Constraint(expr=   m.b185 + m.b195 + m.b199 >= 1)

m.c312 = Constraint(expr=   m.b185 + m.b195 + m.b196 >= 1)

m.c313 = Constraint(expr=   m.b185 + m.b192 + m.b202 >= 1)

m.c314 = Constraint(expr=   m.b185 + m.b192 + m.b199 >= 1)

m.c315 = Constraint(expr=   m.b185 + m.b192 + m.b196 >= 1)

m.c316 = Constraint(expr=   m.b185 + m.b189 + m.b202 >= 1)

m.c317 = Constraint(expr=   m.b185 + m.b189 + m.b199 >= 1)

m.c318 = Constraint(expr=   m.b185 + m.b189 + m.b196 >= 1)

m.c319 = Constraint(expr=   m.x31 - 2.02*m.b185 >= 0)

m.c320 = Constraint(expr=   m.x32 - 4.01333333333333*m.b186 >= 0)

m.c321 = Constraint(expr=   m.x33 - 4.76*m.b187 >= 0)

m.c322 = Constraint(expr=   m.x34 - 5.68*m.b188 >= 0)

m.c323 = Constraint(expr=   m.x34 - 5.96*m.b189 >= 0)

m.c324 = Constraint(expr=   m.x35 - 38.2666666666667*m.b190 >= 0)

m.c325 = Constraint(expr=   m.x35 - 40.18*m.b191 >= 0)

m.c326 = Constraint(expr=   m.x35 - 42.0933333333333*m.b192 >= 0)

m.c327 = Constraint(expr=   m.x36 - 90.2533333333333*m.b193 >= 0)

m.c328 = Constraint(expr=   m.x36 - 94.7666666666667*m.b194 >= 0)

m.c329 = Constraint(expr=   m.x36 - 99.28*m.b195 >= 0)

m.c330 = Constraint(expr=   m.x37 - 6.59333333333333*m.b196 >= 0)

m.c331 = Constraint(expr=   m.x38 - 56.24*m.b197 >= 0)

m.c332 = Constraint(expr=   m.x38 - 59.0533333333333*m.b198 >= 0)

m.c333 = Constraint(expr=   m.x38 - 61.8666666666667*m.b199 >= 0)

m.c334 = Constraint(expr=   m.x39 - 51.1733333333333*m.b200 >= 0)

m.c335 = Constraint(expr=   m.x39 - 53.7333333333333*m.b201 >= 0)

m.c336 = Constraint(expr=   m.x39 - 56.2866666666667*m.b202 >= 0)

m.c337 = Constraint(expr=   m.x40 - 35.84*m.b203 >= 0)

m.c338 = Constraint(expr=   m.x40 - 37.7266666666667*m.b204 >= 0)

m.c339 = Constraint(expr=   m.x40 - 39.6133333333333*m.b205 >= 0)

m.c340 = Constraint(expr=   m.x40 - 41.5*m.b206 >= 0)

m.c341 = Constraint(expr=   m.x41 - 56.8066666666667*m.b207 >= 0)

m.c342 = Constraint(expr=   m.x41 - 59.6466666666667*m.b208 >= 0)

m.c343 = Constraint(expr=   m.x41 - 62.4933333333333*m.b209 >= 0)

m.c344 = Constraint(expr=   m.x42 - 80.9066666666667*m.b210 >= 0)

m.c345 = Constraint(expr=   m.x43 - 26.1466666666667*m.b211 >= 0)

m.c346 = Constraint(expr=   m.x44 - 38*m.b212 >= 0)

m.c347 = Constraint(expr=   m.x45 - 59.2733333333333*m.b213 >= 0)

m.c348 = Constraint(expr=   m.x45 - 62.24*m.b214 >= 0)

m.c349 = Constraint(expr= - m.x76 + m.x155 <= 0)

m.c350 = Constraint(expr= - m.x76 + m.x156 <= 0)

m.c351 = Constraint(expr= - m.x77 + m.x157 <= 0)

m.c352 = Constraint(expr= - m.x77 + m.x158 <= 0)

m.c353 = Constraint(expr= - m.x78 + m.x159 <= 0)

m.c354 = Constraint(expr= - m.x78 + m.x160 <= 0)

m.c355 = Constraint(expr= - m.x79 + m.x161 <= 0)

m.c356 = Constraint(expr= - m.x79 + m.x162 <= 0)

m.c357 = Constraint(expr= - m.x80 + m.x163 <= 0)

m.c358 = Constraint(expr= - m.x80 + m.x164 <= 0)

m.c359 = Constraint(expr= - m.x81 + m.x165 <= 0)

m.c360 = Constraint(expr= - m.x81 + m.x166 <= 0)

m.c361 = Constraint(expr= - m.x82 + m.x167 <= 0)

m.c362 = Constraint(expr= - m.x82 + m.x168 <= 0)

m.c363 = Constraint(expr= - m.x83 + m.x169 <= 0)

m.c364 = Constraint(expr= - m.x83 + m.x170 <= 0)

m.c365 = Constraint(expr= - m.x84 + m.x171 <= 0)

m.c366 = Constraint(expr= - m.x84 + m.x172 <= 0)

m.c367 = Constraint(expr= - m.x85 + m.x173 <= 0)

m.c368 = Constraint(expr= - m.x85 + m.x174 <= 0)

m.c369 = Constraint(expr= - m.x86 + m.x175 <= 0)

m.c370 = Constraint(expr= - m.x86 + m.x176 <= 0)

m.c371 = Constraint(expr= - m.x87 + m.x177 <= 0)

m.c372 = Constraint(expr= - m.x87 + m.x178 <= 0)

m.c373 = Constraint(expr= - m.x88 + m.x179 <= 0)

m.c374 = Constraint(expr= - m.x88 + m.x180 <= 0)

m.c375 = Constraint(expr= - m.x89 + m.x181 <= 0)

m.c376 = Constraint(expr= - m.x89 + m.x182 <= 0)

m.c377 = Constraint(expr= - m.x90 + m.x183 <= 0)

m.c378 = Constraint(expr= - m.x90 + m.x184 <= 0)

m.c379 = Constraint(expr=   m.b188 - m.b189 >= 0)

m.c380 = Constraint(expr=   m.b190 - m.b191 >= 0)

m.c381 = Constraint(expr=   m.b191 - m.b192 >= 0)

m.c382 = Constraint(expr=   m.b193 - m.b194 >= 0)

m.c383 = Constraint(expr=   m.b194 - m.b195 >= 0)

m.c384 = Constraint(expr=   m.b197 - m.b198 >= 0)

m.c385 = Constraint(expr=   m.b198 - m.b199 >= 0)

m.c386 = Constraint(expr=   m.b200 - m.b201 >= 0)

m.c387 = Constraint(expr=   m.b201 - m.b202 >= 0)

m.c388 = Constraint(expr=   m.b203 - m.b204 >= 0)

m.c389 = Constraint(expr=   m.b204 - m.b205 >= 0)

m.c390 = Constraint(expr=   m.b205 - m.b206 >= 0)

m.c391 = Constraint(expr=   m.b207 - m.b208 >= 0)

m.c392 = Constraint(expr=   m.b208 - m.b209 >= 0)

m.c393 = Constraint(expr=   m.b213 - m.b214 >= 0)

m.c394 = Constraint(expr=   m.x93 - m.x94 >= 0)
