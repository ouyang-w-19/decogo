#  MINLP written by GAMS Convert at 04/21/18 13:54:10
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        422       91      313       18        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        262      232       30        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1148     1043      105        0
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
m.x31 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,0.26351883),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,0.26351883),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,0.26351883),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,0.22891574),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,0.22891574),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,0.22891574),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,0.21464835),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,0.21464835),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,0.21464835),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,0.17964414),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,0.17964414),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,0.17964414),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,0.17402843),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,0.17402843),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,0.17402843),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,0.15355962),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,0.15355962),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,0.15355962),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,0.1942283),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,0.1942283),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,0.1942283),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,0.25670555),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,0.25670555),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,0.25670555),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,0.27088619),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,0.27088619),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,0.27088619),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,0.28985675),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,0.28985675),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,0.28985675),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,0.25550303),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,0.25550303),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,0.25550303),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,0.19001726),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,0.19001726),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,0.19001726),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,0.23803143),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,0.23803143),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,0.23803143),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,0.23312962),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,0.23312962),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,0.23312962),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,0.27705307),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,0.27705307),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,0.27705307),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,2.02),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,4.01333333333333),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,4.76),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,5.96),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,42.0933333333333),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,99.28),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,6.59333333333333),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,61.8666666666667),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,56.2866666666667),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,41.5),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,62.4933333333333),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,80.9066666666667),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,26.1466666666667),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,38),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,62.24),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.x121 = Var(within=Reals,bounds=(0.25788969,0.35227087),initialize=0.25788969)
m.x122 = Var(within=Reals,bounds=(0.25788969,0.35227087),initialize=0.25788969)
m.x123 = Var(within=Reals,bounds=(0.25788969,0.35227087),initialize=0.25788969)
m.x124 = Var(within=Reals,bounds=(-0.98493628,-0.7794471),initialize=-0.7794471)
m.x125 = Var(within=Reals,bounds=(-0.98493628,-0.7794471),initialize=-0.7794471)
m.x126 = Var(within=Reals,bounds=(-0.98493628,-0.7794471),initialize=-0.7794471)
m.x127 = Var(within=Reals,bounds=(0,0.0580296499999999),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,0.0580296499999999),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,0.0580296499999999),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,0.0546689399999999),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,0.0546689399999999),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,0.0546689399999999),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,0.09360565),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,0.09360565),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,0.09360565),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,0.0476880399999999),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,0.0476880399999999),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,0.0476880399999999),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,0.05276021),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,0.05276021),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,0.05276021),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,0.04905388),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,0.04905388),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,0.04905388),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,0.07731692),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,0.07731692),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,0.07731692),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,0.08211741),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,0.08211741),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,0.08211741),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,0.08436757),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,0.08436757),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,0.08436757),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,0.06987597),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,0.06987597),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,0.06987597),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,0.04788831),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,0.04788831),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,0.04788831),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,0.0668875099999999),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,0.0668875099999999),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,0.0668875099999999),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,0.07276512),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,0.07276512),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,0.07276512),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,0.1742468),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,0.1742468),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,0.1742468),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,0.1210427),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,0.1210427),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,0.1210427),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,0.1319561),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,0.1319561),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,0.1319561),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,0.12126822),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,0.12126822),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,0.12126822),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,0.10450574),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,0.10450574),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,0.10450574),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,0.11691138),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,0.11691138),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,0.11691138),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,0.17458814),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,0.17458814),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,0.17458814),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,0.17650501),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,0.17650501),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,0.17650501),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,0.18562706),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,0.18562706),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,0.18562706),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,0.14212895),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,0.14212895),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,0.14212895),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,0.17114392),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,0.17114392),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,0.17114392),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,0.1603645),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,0.1603645),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,0.1603645),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,0.18267189),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,0.18267189),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,0.18267189),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.b232 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b233 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b234 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b235 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b236 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b237 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b238 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b239 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b240 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b241 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b242 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b243 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b244 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b245 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b246 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b247 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b248 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b249 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b250 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b251 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b252 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b253 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b254 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b255 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b256 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b257 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b258 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b259 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b260 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b261 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   m.x106 + m.x107 + m.x108 + m.x109 + m.x110 + m.x111 + m.x112 + m.x113 + m.x114 + m.x115
                        + m.x116 + m.x117 + m.x118 + m.x119 + m.x120, sense=minimize)

m.c2 = Constraint(expr=-(m.x91*m.x46*m.x1 + m.x91*m.x47*m.x2 + m.x91*m.x48*m.x3) + m.x217 == 0)

m.c3 = Constraint(expr=-(m.x92*m.x49*m.x4 + m.x92*m.x50*m.x5 + m.x92*m.x51*m.x6) + m.x218 == 0)

m.c4 = Constraint(expr=-(m.x93*m.x52*m.x7 + m.x93*m.x53*m.x8 + m.x93*m.x54*m.x9) + m.x219 == 0)

m.c5 = Constraint(expr=-(m.x94*m.x55*m.x10 + m.x94*m.x56*m.x11 + m.x94*m.x57*m.x12) + m.x220 == 0)

m.c6 = Constraint(expr=-(m.x95*m.x58*m.x13 + m.x95*m.x59*m.x14 + m.x95*m.x60*m.x15) + m.x221 == 0)

m.c7 = Constraint(expr=-(m.x96*m.x61*m.x16 + m.x96*m.x62*m.x17 + m.x96*m.x63*m.x18) + m.x222 == 0)

m.c8 = Constraint(expr=-(m.x97*m.x64*m.x19 + m.x97*m.x65*m.x20 + m.x97*m.x66*m.x21) + m.x223 == 0)

m.c9 = Constraint(expr=-(m.x98*m.x67*m.x22 + m.x98*m.x68*m.x23 + m.x98*m.x69*m.x24) + m.x224 == 0)

m.c10 = Constraint(expr=-(m.x99*m.x70*m.x25 + m.x99*m.x71*m.x26 + m.x99*m.x72*m.x27) + m.x225 == 0)

m.c11 = Constraint(expr=-(m.x100*m.x73*m.x28 + m.x100*m.x74*m.x29 + m.x100*m.x75*m.x30) + m.x226 == 0)

m.c12 = Constraint(expr=-(m.x101*m.x76*m.x31 + m.x101*m.x77*m.x32 + m.x101*m.x78*m.x33) + m.x227 == 0)

m.c13 = Constraint(expr=-(m.x102*m.x79*m.x34 + m.x102*m.x80*m.x35 + m.x102*m.x81*m.x36) + m.x228 == 0)

m.c14 = Constraint(expr=-(m.x103*m.x82*m.x37 + m.x103*m.x83*m.x38 + m.x103*m.x84*m.x39) + m.x229 == 0)

m.c15 = Constraint(expr=-(m.x104*m.x85*m.x40 + m.x104*m.x86*m.x41 + m.x104*m.x87*m.x42) + m.x230 == 0)

m.c16 = Constraint(expr=-(m.x105*m.x88*m.x43 + m.x105*m.x89*m.x44 + m.x105*m.x90*m.x45) + m.x231 == 0)

m.c17 = Constraint(expr=   m.x1 + m.x2 + m.x3 == 1)

m.c18 = Constraint(expr=   m.x4 + m.x5 + m.x6 == 1)

m.c19 = Constraint(expr=   m.x7 + m.x8 + m.x9 == 1)

m.c20 = Constraint(expr=   m.x10 + m.x11 + m.x12 == 1)

m.c21 = Constraint(expr=   m.x13 + m.x14 + m.x15 == 1)

m.c22 = Constraint(expr=   m.x16 + m.x17 + m.x18 == 1)

m.c23 = Constraint(expr=   m.x19 + m.x20 + m.x21 == 1)

m.c24 = Constraint(expr=   m.x22 + m.x23 + m.x24 == 1)

m.c25 = Constraint(expr=   m.x25 + m.x26 + m.x27 == 1)

m.c26 = Constraint(expr=   m.x28 + m.x29 + m.x30 == 1)

m.c27 = Constraint(expr=   m.x31 + m.x32 + m.x33 == 1)

m.c28 = Constraint(expr=   m.x34 + m.x35 + m.x36 == 1)

m.c29 = Constraint(expr=   m.x37 + m.x38 + m.x39 == 1)

m.c30 = Constraint(expr=   m.x40 + m.x41 + m.x42 == 1)

m.c31 = Constraint(expr=   m.x43 + m.x44 + m.x45 == 1)

m.c32 = Constraint(expr=   2.02*m.x1 + 4.01333333333333*m.x4 + 4.76*m.x7 + 5.96*m.x10 + 42.0933333333333*m.x13
                         + 99.28*m.x16 + 6.59333333333333*m.x19 + 61.8666666666667*m.x22 + 56.2866666666667*m.x25
                         + 41.5*m.x28 + 62.4933333333333*m.x31 + 80.9066666666667*m.x34 + 26.1466666666667*m.x37
                         + 38*m.x40 + 62.24*m.x43 <= 213.053333333333)

m.c33 = Constraint(expr=   2.02*m.x2 + 4.01333333333333*m.x5 + 4.76*m.x8 + 5.96*m.x11 + 42.0933333333333*m.x14
                         + 99.28*m.x17 + 6.59333333333333*m.x20 + 61.8666666666667*m.x23 + 56.2866666666667*m.x26
                         + 41.5*m.x29 + 62.4933333333333*m.x32 + 80.9066666666667*m.x35 + 26.1466666666667*m.x38
                         + 38*m.x41 + 62.24*m.x44 <= 213.053333333333)

m.c34 = Constraint(expr=   2.02*m.x3 + 4.01333333333333*m.x6 + 4.76*m.x9 + 5.96*m.x12 + 42.0933333333333*m.x15
                         + 99.28*m.x18 + 6.59333333333333*m.x21 + 61.8666666666667*m.x24 + 56.2866666666667*m.x27
                         + 41.5*m.x30 + 62.4933333333333*m.x33 + 80.9066666666667*m.x36 + 26.1466666666667*m.x39
                         + 38*m.x42 + 62.24*m.x45 <= 213.053333333333)

m.c35 = Constraint(expr=   m.x121 + m.x127 >= 0.29424122)

m.c36 = Constraint(expr=   m.x122 + m.x128 >= 0.29424122)

m.c37 = Constraint(expr=   m.x123 + m.x129 >= 0.29424122)

m.c38 = Constraint(expr=   m.x121 + m.x130 >= 0.29760193)

m.c39 = Constraint(expr=   m.x122 + m.x131 >= 0.29760193)

m.c40 = Constraint(expr=   m.x123 + m.x132 >= 0.29760193)

m.c41 = Constraint(expr=   m.x121 + m.x133 >= 0.35149534)

m.c42 = Constraint(expr=   m.x122 + m.x134 >= 0.35149534)

m.c43 = Constraint(expr=   m.x123 + m.x135 >= 0.35149534)

m.c44 = Constraint(expr=   m.x121 + m.x136 >= 0.30458283)

m.c45 = Constraint(expr=   m.x122 + m.x137 >= 0.30458283)

m.c46 = Constraint(expr=   m.x123 + m.x138 >= 0.30458283)

m.c47 = Constraint(expr=   m.x121 + m.x139 >= 0.29951066)

m.c48 = Constraint(expr=   m.x122 + m.x140 >= 0.29951066)

m.c49 = Constraint(expr=   m.x123 + m.x141 >= 0.29951066)

m.c50 = Constraint(expr=   m.x121 + m.x142 >= 0.30694357)

m.c51 = Constraint(expr=   m.x122 + m.x143 >= 0.30694357)

m.c52 = Constraint(expr=   m.x123 + m.x144 >= 0.30694357)

m.c53 = Constraint(expr=   m.x121 + m.x145 >= 0.33520661)

m.c54 = Constraint(expr=   m.x122 + m.x146 >= 0.33520661)

m.c55 = Constraint(expr=   m.x123 + m.x147 >= 0.33520661)

m.c56 = Constraint(expr=   m.x121 + m.x148 >= 0.3400071)

m.c57 = Constraint(expr=   m.x122 + m.x149 >= 0.3400071)

m.c58 = Constraint(expr=   m.x123 + m.x150 >= 0.3400071)

m.c59 = Constraint(expr=   m.x121 + m.x151 >= 0.35227087)

m.c60 = Constraint(expr=   m.x122 + m.x152 >= 0.35227087)

m.c61 = Constraint(expr=   m.x123 + m.x153 >= 0.35227087)

m.c62 = Constraint(expr=   m.x121 + m.x154 >= 0.34225726)

m.c63 = Constraint(expr=   m.x122 + m.x155 >= 0.34225726)

m.c64 = Constraint(expr=   m.x123 + m.x156 >= 0.34225726)

m.c65 = Constraint(expr=   m.x121 + m.x157 >= 0.32776566)

m.c66 = Constraint(expr=   m.x122 + m.x158 >= 0.32776566)

m.c67 = Constraint(expr=   m.x123 + m.x159 >= 0.32776566)

m.c68 = Constraint(expr=   m.x121 + m.x160 >= 0.30438256)

m.c69 = Constraint(expr=   m.x122 + m.x161 >= 0.30438256)

m.c70 = Constraint(expr=   m.x123 + m.x162 >= 0.30438256)

m.c71 = Constraint(expr=   m.x121 + m.x163 >= 0.28538336)

m.c72 = Constraint(expr=   m.x122 + m.x164 >= 0.28538336)

m.c73 = Constraint(expr=   m.x123 + m.x165 >= 0.28538336)

m.c74 = Constraint(expr=   m.x121 + m.x166 >= 0.27950575)

m.c75 = Constraint(expr=   m.x122 + m.x167 >= 0.27950575)

m.c76 = Constraint(expr=   m.x123 + m.x168 >= 0.27950575)

m.c77 = Constraint(expr= - m.x121 + m.x127 >= -0.29424122)

m.c78 = Constraint(expr= - m.x122 + m.x128 >= -0.29424122)

m.c79 = Constraint(expr= - m.x123 + m.x129 >= -0.29424122)

m.c80 = Constraint(expr= - m.x121 + m.x130 >= -0.29760193)

m.c81 = Constraint(expr= - m.x122 + m.x131 >= -0.29760193)

m.c82 = Constraint(expr= - m.x123 + m.x132 >= -0.29760193)

m.c83 = Constraint(expr= - m.x121 + m.x133 >= -0.35149534)

m.c84 = Constraint(expr= - m.x122 + m.x134 >= -0.35149534)

m.c85 = Constraint(expr= - m.x123 + m.x135 >= -0.35149534)

m.c86 = Constraint(expr= - m.x121 + m.x136 >= -0.30458283)

m.c87 = Constraint(expr= - m.x122 + m.x137 >= -0.30458283)

m.c88 = Constraint(expr= - m.x123 + m.x138 >= -0.30458283)

m.c89 = Constraint(expr= - m.x121 + m.x139 >= -0.29951066)

m.c90 = Constraint(expr= - m.x122 + m.x140 >= -0.29951066)

m.c91 = Constraint(expr= - m.x123 + m.x141 >= -0.29951066)

m.c92 = Constraint(expr= - m.x121 + m.x142 >= -0.30694357)

m.c93 = Constraint(expr= - m.x122 + m.x143 >= -0.30694357)

m.c94 = Constraint(expr= - m.x123 + m.x144 >= -0.30694357)

m.c95 = Constraint(expr= - m.x121 + m.x145 >= -0.33520661)

m.c96 = Constraint(expr= - m.x122 + m.x146 >= -0.33520661)

m.c97 = Constraint(expr= - m.x123 + m.x147 >= -0.33520661)

m.c98 = Constraint(expr= - m.x121 + m.x148 >= -0.3400071)

m.c99 = Constraint(expr= - m.x122 + m.x149 >= -0.3400071)

m.c100 = Constraint(expr= - m.x123 + m.x150 >= -0.3400071)

m.c101 = Constraint(expr= - m.x121 + m.x154 >= -0.34225726)

m.c102 = Constraint(expr= - m.x122 + m.x155 >= -0.34225726)

m.c103 = Constraint(expr= - m.x123 + m.x156 >= -0.34225726)

m.c104 = Constraint(expr= - m.x121 + m.x157 >= -0.32776566)

m.c105 = Constraint(expr= - m.x122 + m.x158 >= -0.32776566)

m.c106 = Constraint(expr= - m.x123 + m.x159 >= -0.32776566)

m.c107 = Constraint(expr= - m.x121 + m.x160 >= -0.30438256)

m.c108 = Constraint(expr= - m.x122 + m.x161 >= -0.30438256)

m.c109 = Constraint(expr= - m.x123 + m.x162 >= -0.30438256)

m.c110 = Constraint(expr= - m.x121 + m.x163 >= -0.28538336)

m.c111 = Constraint(expr= - m.x122 + m.x164 >= -0.28538336)

m.c112 = Constraint(expr= - m.x123 + m.x165 >= -0.28538336)

m.c113 = Constraint(expr= - m.x121 + m.x166 >= -0.27950575)

m.c114 = Constraint(expr= - m.x122 + m.x167 >= -0.27950575)

m.c115 = Constraint(expr= - m.x123 + m.x168 >= -0.27950575)

m.c116 = Constraint(expr= - m.x121 + m.x169 >= -0.25788969)

m.c117 = Constraint(expr= - m.x122 + m.x170 >= -0.25788969)

m.c118 = Constraint(expr= - m.x123 + m.x171 >= -0.25788969)

m.c119 = Constraint(expr=   m.x124 + m.x175 >= -0.9536939)

m.c120 = Constraint(expr=   m.x125 + m.x176 >= -0.9536939)

m.c121 = Constraint(expr=   m.x126 + m.x177 >= -0.9536939)

m.c122 = Constraint(expr=   m.x124 + m.x178 >= -0.9004898)

m.c123 = Constraint(expr=   m.x125 + m.x179 >= -0.9004898)

m.c124 = Constraint(expr=   m.x126 + m.x180 >= -0.9004898)

m.c125 = Constraint(expr=   m.x124 + m.x181 >= -0.9114032)

m.c126 = Constraint(expr=   m.x125 + m.x182 >= -0.9114032)

m.c127 = Constraint(expr=   m.x126 + m.x183 >= -0.9114032)

m.c128 = Constraint(expr=   m.x124 + m.x184 >= -0.90071532)

m.c129 = Constraint(expr=   m.x125 + m.x185 >= -0.90071532)

m.c130 = Constraint(expr=   m.x126 + m.x186 >= -0.90071532)

m.c131 = Constraint(expr=   m.x124 + m.x187 >= -0.88043054)

m.c132 = Constraint(expr=   m.x125 + m.x188 >= -0.88043054)

m.c133 = Constraint(expr=   m.x126 + m.x189 >= -0.88043054)

m.c134 = Constraint(expr=   m.x124 + m.x190 >= -0.8680249)

m.c135 = Constraint(expr=   m.x125 + m.x191 >= -0.8680249)

m.c136 = Constraint(expr=   m.x126 + m.x192 >= -0.8680249)

m.c137 = Constraint(expr=   m.x124 + m.x193 >= -0.81034814)

m.c138 = Constraint(expr=   m.x125 + m.x194 >= -0.81034814)

m.c139 = Constraint(expr=   m.x126 + m.x195 >= -0.81034814)

m.c140 = Constraint(expr=   m.x124 + m.x196 >= -0.80843127)

m.c141 = Constraint(expr=   m.x125 + m.x197 >= -0.80843127)

m.c142 = Constraint(expr=   m.x126 + m.x198 >= -0.80843127)

m.c143 = Constraint(expr=   m.x124 + m.x199 >= -0.7794471)

m.c144 = Constraint(expr=   m.x125 + m.x200 >= -0.7794471)

m.c145 = Constraint(expr=   m.x126 + m.x201 >= -0.7794471)

m.c146 = Constraint(expr=   m.x124 + m.x202 >= -0.79930922)

m.c147 = Constraint(expr=   m.x125 + m.x203 >= -0.79930922)

m.c148 = Constraint(expr=   m.x126 + m.x204 >= -0.79930922)

m.c149 = Constraint(expr=   m.x124 + m.x205 >= -0.84280733)

m.c150 = Constraint(expr=   m.x125 + m.x206 >= -0.84280733)

m.c151 = Constraint(expr=   m.x126 + m.x207 >= -0.84280733)

m.c152 = Constraint(expr=   m.x124 + m.x208 >= -0.81379236)

m.c153 = Constraint(expr=   m.x125 + m.x209 >= -0.81379236)

m.c154 = Constraint(expr=   m.x126 + m.x210 >= -0.81379236)

m.c155 = Constraint(expr=   m.x124 + m.x211 >= -0.82457178)

m.c156 = Constraint(expr=   m.x125 + m.x212 >= -0.82457178)

m.c157 = Constraint(expr=   m.x126 + m.x213 >= -0.82457178)

m.c158 = Constraint(expr=   m.x124 + m.x214 >= -0.80226439)

m.c159 = Constraint(expr=   m.x125 + m.x215 >= -0.80226439)

m.c160 = Constraint(expr=   m.x126 + m.x216 >= -0.80226439)

m.c161 = Constraint(expr= - m.x124 + m.x172 >= 0.98493628)

m.c162 = Constraint(expr= - m.x125 + m.x173 >= 0.98493628)

m.c163 = Constraint(expr= - m.x126 + m.x174 >= 0.98493628)

m.c164 = Constraint(expr= - m.x124 + m.x175 >= 0.9536939)

m.c165 = Constraint(expr= - m.x125 + m.x176 >= 0.9536939)

m.c166 = Constraint(expr= - m.x126 + m.x177 >= 0.9536939)

m.c167 = Constraint(expr= - m.x124 + m.x178 >= 0.9004898)

m.c168 = Constraint(expr= - m.x125 + m.x179 >= 0.9004898)

m.c169 = Constraint(expr= - m.x126 + m.x180 >= 0.9004898)

m.c170 = Constraint(expr= - m.x124 + m.x181 >= 0.9114032)

m.c171 = Constraint(expr= - m.x125 + m.x182 >= 0.9114032)

m.c172 = Constraint(expr= - m.x126 + m.x183 >= 0.9114032)

m.c173 = Constraint(expr= - m.x124 + m.x184 >= 0.90071532)

m.c174 = Constraint(expr= - m.x125 + m.x185 >= 0.90071532)

m.c175 = Constraint(expr= - m.x126 + m.x186 >= 0.90071532)

m.c176 = Constraint(expr= - m.x124 + m.x187 >= 0.88043054)

m.c177 = Constraint(expr= - m.x125 + m.x188 >= 0.88043054)

m.c178 = Constraint(expr= - m.x126 + m.x189 >= 0.88043054)

m.c179 = Constraint(expr= - m.x124 + m.x190 >= 0.8680249)

m.c180 = Constraint(expr= - m.x125 + m.x191 >= 0.8680249)

m.c181 = Constraint(expr= - m.x126 + m.x192 >= 0.8680249)

m.c182 = Constraint(expr= - m.x124 + m.x193 >= 0.81034814)

m.c183 = Constraint(expr= - m.x125 + m.x194 >= 0.81034814)

m.c184 = Constraint(expr= - m.x126 + m.x195 >= 0.81034814)

m.c185 = Constraint(expr= - m.x124 + m.x196 >= 0.80843127)

m.c186 = Constraint(expr= - m.x125 + m.x197 >= 0.80843127)

m.c187 = Constraint(expr= - m.x126 + m.x198 >= 0.80843127)

m.c188 = Constraint(expr= - m.x124 + m.x202 >= 0.79930922)

m.c189 = Constraint(expr= - m.x125 + m.x203 >= 0.79930922)

m.c190 = Constraint(expr= - m.x126 + m.x204 >= 0.79930922)

m.c191 = Constraint(expr= - m.x124 + m.x205 >= 0.84280733)

m.c192 = Constraint(expr= - m.x125 + m.x206 >= 0.84280733)

m.c193 = Constraint(expr= - m.x126 + m.x207 >= 0.84280733)

m.c194 = Constraint(expr= - m.x124 + m.x208 >= 0.81379236)

m.c195 = Constraint(expr= - m.x125 + m.x209 >= 0.81379236)

m.c196 = Constraint(expr= - m.x126 + m.x210 >= 0.81379236)

m.c197 = Constraint(expr= - m.x124 + m.x211 >= 0.82457178)

m.c198 = Constraint(expr= - m.x125 + m.x212 >= 0.82457178)

m.c199 = Constraint(expr= - m.x126 + m.x213 >= 0.82457178)

m.c200 = Constraint(expr= - m.x124 + m.x214 >= 0.80226439)

m.c201 = Constraint(expr= - m.x125 + m.x215 >= 0.80226439)

m.c202 = Constraint(expr= - m.x126 + m.x216 >= 0.80226439)

m.c203 = Constraint(expr=   m.x46 - m.x127 - m.x172 == 0)

m.c204 = Constraint(expr=   m.x47 - m.x128 - m.x173 == 0)

m.c205 = Constraint(expr=   m.x48 - m.x129 - m.x174 == 0)

m.c206 = Constraint(expr=   m.x49 - m.x130 - m.x175 == 0)

m.c207 = Constraint(expr=   m.x50 - m.x131 - m.x176 == 0)

m.c208 = Constraint(expr=   m.x51 - m.x132 - m.x177 == 0)

m.c209 = Constraint(expr=   m.x52 - m.x133 - m.x178 == 0)

m.c210 = Constraint(expr=   m.x53 - m.x134 - m.x179 == 0)

m.c211 = Constraint(expr=   m.x54 - m.x135 - m.x180 == 0)

m.c212 = Constraint(expr=   m.x55 - m.x136 - m.x181 == 0)

m.c213 = Constraint(expr=   m.x56 - m.x137 - m.x182 == 0)

m.c214 = Constraint(expr=   m.x57 - m.x138 - m.x183 == 0)

m.c215 = Constraint(expr=   m.x58 - m.x139 - m.x184 == 0)

m.c216 = Constraint(expr=   m.x59 - m.x140 - m.x185 == 0)

m.c217 = Constraint(expr=   m.x60 - m.x141 - m.x186 == 0)

m.c218 = Constraint(expr=   m.x61 - m.x142 - m.x187 == 0)

m.c219 = Constraint(expr=   m.x62 - m.x143 - m.x188 == 0)

m.c220 = Constraint(expr=   m.x63 - m.x144 - m.x189 == 0)

m.c221 = Constraint(expr=   m.x64 - m.x145 - m.x190 == 0)

m.c222 = Constraint(expr=   m.x65 - m.x146 - m.x191 == 0)

m.c223 = Constraint(expr=   m.x66 - m.x147 - m.x192 == 0)

m.c224 = Constraint(expr=   m.x67 - m.x148 - m.x193 == 0)

m.c225 = Constraint(expr=   m.x68 - m.x149 - m.x194 == 0)

m.c226 = Constraint(expr=   m.x69 - m.x150 - m.x195 == 0)

m.c227 = Constraint(expr=   m.x70 - m.x151 - m.x196 == 0)

m.c228 = Constraint(expr=   m.x71 - m.x152 - m.x197 == 0)

m.c229 = Constraint(expr=   m.x72 - m.x153 - m.x198 == 0)

m.c230 = Constraint(expr=   m.x73 - m.x154 - m.x199 == 0)

m.c231 = Constraint(expr=   m.x74 - m.x155 - m.x200 == 0)

m.c232 = Constraint(expr=   m.x75 - m.x156 - m.x201 == 0)

m.c233 = Constraint(expr=   m.x76 - m.x157 - m.x202 == 0)

m.c234 = Constraint(expr=   m.x77 - m.x158 - m.x203 == 0)

m.c235 = Constraint(expr=   m.x78 - m.x159 - m.x204 == 0)

m.c236 = Constraint(expr=   m.x79 - m.x160 - m.x205 == 0)

m.c237 = Constraint(expr=   m.x80 - m.x161 - m.x206 == 0)

m.c238 = Constraint(expr=   m.x81 - m.x162 - m.x207 == 0)

m.c239 = Constraint(expr=   m.x82 - m.x163 - m.x208 == 0)

m.c240 = Constraint(expr=   m.x83 - m.x164 - m.x209 == 0)

m.c241 = Constraint(expr=   m.x84 - m.x165 - m.x210 == 0)

m.c242 = Constraint(expr=   m.x85 - m.x166 - m.x211 == 0)

m.c243 = Constraint(expr=   m.x86 - m.x167 - m.x212 == 0)

m.c244 = Constraint(expr=   m.x87 - m.x168 - m.x213 == 0)

m.c245 = Constraint(expr=   m.x88 - m.x169 - m.x214 == 0)

m.c246 = Constraint(expr=   m.x89 - m.x170 - m.x215 == 0)

m.c247 = Constraint(expr=   m.x90 - m.x171 - m.x216 == 0)

m.c248 = Constraint(expr=   m.b239 + m.b240 >= 1)

m.c249 = Constraint(expr=   m.b237 + m.b242 >= 1)

m.c250 = Constraint(expr=   m.b236 + m.b240 >= 1)

m.c251 = Constraint(expr=   m.b236 + m.b239 + m.b241 >= 1)

m.c252 = Constraint(expr=   m.b236 + m.b238 + m.b242 >= 1)

m.c253 = Constraint(expr=   m.b236 + m.b237 >= 1)

m.c254 = Constraint(expr=   m.b235 + m.b242 >= 1)

m.c255 = Constraint(expr=   m.b235 + m.b239 >= 1)

m.c256 = Constraint(expr=   m.b234 + m.b241 >= 1)

m.c257 = Constraint(expr=   m.b234 + m.b239 + m.b242 >= 1)

m.c258 = Constraint(expr=   m.b234 + m.b238 >= 1)

m.c259 = Constraint(expr=   m.b234 + m.b236 + m.b242 >= 1)

m.c260 = Constraint(expr=   m.b234 + m.b236 + m.b239 >= 1)

m.c261 = Constraint(expr=   m.b234 + m.b235 >= 1)

m.c262 = Constraint(expr=   m.b233 + m.b241 >= 1)

m.c263 = Constraint(expr=   m.b233 + m.b239 + m.b242 >= 1)

m.c264 = Constraint(expr=   m.b233 + m.b238 >= 1)

m.c265 = Constraint(expr=   m.b233 + m.b236 >= 1)

m.c266 = Constraint(expr=   m.b233 + m.b234 >= 1)

m.c267 = Constraint(expr=   m.b232 + m.b241 >= 1)

m.c268 = Constraint(expr=   m.b232 + m.b239 + m.b242 >= 1)

m.c269 = Constraint(expr=   m.b232 + m.b238 >= 1)

m.c270 = Constraint(expr=   m.b232 + m.b236 + m.b242 >= 1)

m.c271 = Constraint(expr=   m.b232 + m.b236 + m.b239 >= 1)

m.c272 = Constraint(expr=   m.b232 + m.b235 >= 1)

m.c273 = Constraint(expr=   m.b232 + m.b234 >= 1)

m.c274 = Constraint(expr=   m.b232 + m.b233 >= 1)

m.c275 = Constraint(expr=   m.b242 + m.b247 >= 1)

m.c276 = Constraint(expr=   m.b242 + m.b246 + m.b248 >= 1)

m.c277 = Constraint(expr=   m.b242 + m.b245 + m.b249 >= 1)

m.c278 = Constraint(expr=   m.b242 + m.b244 >= 1)

m.c279 = Constraint(expr=   m.b242 + m.b243 + m.b249 >= 1)

m.c280 = Constraint(expr=   m.b242 + m.b243 + m.b246 >= 1)

m.c281 = Constraint(expr=   m.b241 + m.b248 >= 1)

m.c282 = Constraint(expr=   m.b241 + m.b246 + m.b249 >= 1)

m.c283 = Constraint(expr=   m.b241 + m.b245 >= 1)

m.c284 = Constraint(expr=   m.b241 + m.b243 >= 1)

m.c285 = Constraint(expr=   m.b240 + m.b249 >= 1)

m.c286 = Constraint(expr=   m.b240 + m.b246 >= 1)

m.c287 = Constraint(expr=   m.b240 + m.b243 >= 1)

m.c288 = Constraint(expr=   m.b239 + m.b247 >= 1)

m.c289 = Constraint(expr=   m.b239 + m.b246 + m.b248 >= 1)

m.c290 = Constraint(expr=   m.b239 + m.b245 + m.b249 >= 1)

m.c291 = Constraint(expr=   m.b239 + m.b244 >= 1)

m.c292 = Constraint(expr=   m.b239 + m.b243 + m.b249 >= 1)

m.c293 = Constraint(expr=   m.b239 + m.b243 + m.b246 >= 1)

m.c294 = Constraint(expr=   m.b239 + m.b242 + m.b248 >= 1)

m.c295 = Constraint(expr=   m.b239 + m.b242 + m.b246 + m.b249 >= 1)

m.c296 = Constraint(expr=   m.b239 + m.b242 + m.b245 >= 1)

m.c297 = Constraint(expr=   m.b239 + m.b242 + m.b243 >= 1)

m.c298 = Constraint(expr=   m.b239 + m.b241 + m.b249 >= 1)

m.c299 = Constraint(expr=   m.b239 + m.b241 + m.b246 >= 1)

m.c300 = Constraint(expr=   m.b239 + m.b241 + m.b243 >= 1)

m.c301 = Constraint(expr=   m.b238 + m.b248 >= 1)

m.c302 = Constraint(expr=   m.b238 + m.b246 + m.b249 >= 1)

m.c303 = Constraint(expr=   m.b238 + m.b245 >= 1)

m.c304 = Constraint(expr=   m.b238 + m.b243 >= 1)

m.c305 = Constraint(expr=   m.b238 + m.b242 + m.b249 >= 1)

m.c306 = Constraint(expr=   m.b238 + m.b242 + m.b246 >= 1)

m.c307 = Constraint(expr=   m.b238 + m.b242 + m.b243 >= 1)

m.c308 = Constraint(expr=   m.b238 + m.b241 + m.b249 >= 1)

m.c309 = Constraint(expr=   m.b238 + m.b241 + m.b246 >= 1)

m.c310 = Constraint(expr=   m.b238 + m.b241 + m.b243 >= 1)

m.c311 = Constraint(expr=   m.b237 + m.b249 >= 1)

m.c312 = Constraint(expr=   m.b237 + m.b246 >= 1)

m.c313 = Constraint(expr=   m.b237 + m.b243 >= 1)

m.c314 = Constraint(expr=   m.b236 + m.b247 >= 1)

m.c315 = Constraint(expr=   m.b236 + m.b246 + m.b248 >= 1)

m.c316 = Constraint(expr=   m.b236 + m.b245 + m.b249 >= 1)

m.c317 = Constraint(expr=   m.b236 + m.b244 >= 1)

m.c318 = Constraint(expr=   m.b236 + m.b243 + m.b249 >= 1)

m.c319 = Constraint(expr=   m.b236 + m.b243 + m.b246 >= 1)

m.c320 = Constraint(expr=   m.b236 + m.b242 + m.b248 >= 1)

m.c321 = Constraint(expr=   m.b236 + m.b242 + m.b246 + m.b249 >= 1)

m.c322 = Constraint(expr=   m.b236 + m.b242 + m.b245 >= 1)

m.c323 = Constraint(expr=   m.b236 + m.b242 + m.b243 >= 1)

m.c324 = Constraint(expr=   m.b236 + m.b241 + m.b249 >= 1)

m.c325 = Constraint(expr=   m.b236 + m.b241 + m.b246 >= 1)

m.c326 = Constraint(expr=   m.b236 + m.b241 + m.b243 >= 1)

m.c327 = Constraint(expr=   m.b236 + m.b239 + m.b248 >= 1)

m.c328 = Constraint(expr=   m.b236 + m.b239 + m.b246 + m.b249 >= 1)

m.c329 = Constraint(expr=   m.b236 + m.b239 + m.b245 >= 1)

m.c330 = Constraint(expr=   m.b236 + m.b239 + m.b243 >= 1)

m.c331 = Constraint(expr=   m.b236 + m.b239 + m.b242 + m.b249 >= 1)

m.c332 = Constraint(expr=   m.b236 + m.b239 + m.b242 + m.b246 >= 1)

m.c333 = Constraint(expr=   m.b236 + m.b239 + m.b242 + m.b243 >= 1)

m.c334 = Constraint(expr=   m.b236 + m.b238 + m.b249 >= 1)

m.c335 = Constraint(expr=   m.b236 + m.b238 + m.b246 >= 1)

m.c336 = Constraint(expr=   m.b236 + m.b238 + m.b243 >= 1)

m.c337 = Constraint(expr=   m.b235 + m.b249 >= 1)

m.c338 = Constraint(expr=   m.b235 + m.b246 >= 1)

m.c339 = Constraint(expr=   m.b235 + m.b243 >= 1)

m.c340 = Constraint(expr=   m.b234 + m.b248 >= 1)

m.c341 = Constraint(expr=   m.b234 + m.b246 + m.b249 >= 1)

m.c342 = Constraint(expr=   m.b234 + m.b245 >= 1)

m.c343 = Constraint(expr=   m.b234 + m.b243 >= 1)

m.c344 = Constraint(expr=   m.b234 + m.b242 + m.b249 >= 1)

m.c345 = Constraint(expr=   m.b234 + m.b242 + m.b246 >= 1)

m.c346 = Constraint(expr=   m.b234 + m.b242 + m.b243 >= 1)

m.c347 = Constraint(expr=   m.b234 + m.b239 + m.b249 >= 1)

m.c348 = Constraint(expr=   m.b234 + m.b239 + m.b246 >= 1)

m.c349 = Constraint(expr=   m.b234 + m.b239 + m.b243 >= 1)

m.c350 = Constraint(expr=   m.b234 + m.b236 + m.b249 >= 1)

m.c351 = Constraint(expr=   m.b234 + m.b236 + m.b246 >= 1)

m.c352 = Constraint(expr=   m.b234 + m.b236 + m.b243 >= 1)

m.c353 = Constraint(expr=   m.b233 + m.b248 >= 1)

m.c354 = Constraint(expr=   m.b233 + m.b246 + m.b249 >= 1)

m.c355 = Constraint(expr=   m.b233 + m.b245 >= 1)

m.c356 = Constraint(expr=   m.b233 + m.b243 >= 1)

m.c357 = Constraint(expr=   m.b233 + m.b242 + m.b249 >= 1)

m.c358 = Constraint(expr=   m.b233 + m.b242 + m.b246 >= 1)

m.c359 = Constraint(expr=   m.b233 + m.b242 + m.b243 >= 1)

m.c360 = Constraint(expr=   m.b233 + m.b239 + m.b249 >= 1)

m.c361 = Constraint(expr=   m.b233 + m.b239 + m.b246 >= 1)

m.c362 = Constraint(expr=   m.b233 + m.b239 + m.b243 >= 1)

m.c363 = Constraint(expr=   m.b232 + m.b248 >= 1)

m.c364 = Constraint(expr=   m.b232 + m.b246 + m.b249 >= 1)

m.c365 = Constraint(expr=   m.b232 + m.b245 >= 1)

m.c366 = Constraint(expr=   m.b232 + m.b243 >= 1)

m.c367 = Constraint(expr=   m.b232 + m.b242 + m.b249 >= 1)

m.c368 = Constraint(expr=   m.b232 + m.b242 + m.b246 >= 1)

m.c369 = Constraint(expr=   m.b232 + m.b242 + m.b243 >= 1)

m.c370 = Constraint(expr=   m.b232 + m.b239 + m.b249 >= 1)

m.c371 = Constraint(expr=   m.b232 + m.b239 + m.b246 >= 1)

m.c372 = Constraint(expr=   m.b232 + m.b239 + m.b243 >= 1)

m.c373 = Constraint(expr=   m.b232 + m.b236 + m.b249 >= 1)

m.c374 = Constraint(expr=   m.b232 + m.b236 + m.b246 >= 1)

m.c375 = Constraint(expr=   m.b232 + m.b236 + m.b243 >= 1)

m.c376 = Constraint(expr=   m.b235 - m.b236 >= 0)

m.c377 = Constraint(expr=   m.b237 - m.b238 >= 0)

m.c378 = Constraint(expr=   m.b238 - m.b239 >= 0)

m.c379 = Constraint(expr=   m.b240 - m.b241 >= 0)

m.c380 = Constraint(expr=   m.b241 - m.b242 >= 0)

m.c381 = Constraint(expr=   m.b244 - m.b245 >= 0)

m.c382 = Constraint(expr=   m.b245 - m.b246 >= 0)

m.c383 = Constraint(expr=   m.b247 - m.b248 >= 0)

m.c384 = Constraint(expr=   m.b248 - m.b249 >= 0)

m.c385 = Constraint(expr=   m.b250 - m.b251 >= 0)

m.c386 = Constraint(expr=   m.b251 - m.b252 >= 0)

m.c387 = Constraint(expr=   m.b252 - m.b253 >= 0)

m.c388 = Constraint(expr=   m.b254 - m.b255 >= 0)

m.c389 = Constraint(expr=   m.b255 - m.b256 >= 0)

m.c390 = Constraint(expr=   m.b260 - m.b261 >= 0)

m.c391 = Constraint(expr=   m.x124 - m.x125 >= 0)

m.c392 = Constraint(expr=   m.x125 - m.x126 >= 0)

m.c393 = Constraint(expr=   m.x91 - 0.1*m.b232 == 1.92)

m.c394 = Constraint(expr=   m.x92 - 0.193333333333333*m.b233 == 3.82)

m.c395 = Constraint(expr=   m.x93 - 0.226666666666667*m.b234 == 4.53333333333333)

m.c396 = Constraint(expr=   m.x94 - 0.286666666666667*m.b235 - 0.28*m.b236 == 5.39333333333333)

m.c397 = Constraint(expr=   m.x95 - 1.91333333333333*m.b237 - 1.91333333333333*m.b238 - 1.91333333333333*m.b239
                          == 36.3533333333333)

m.c398 = Constraint(expr=   m.x96 - 4.50666666666667*m.b240 - 4.51333333333333*m.b241 - 4.51333333333333*m.b242
                          == 85.7466666666667)

m.c399 = Constraint(expr=   m.x97 - 0.313333333333333*m.b243 == 6.28)

m.c400 = Constraint(expr=   m.x98 - 2.80666666666667*m.b244 - 2.81333333333333*m.b245 - 2.81333333333333*m.b246
                          == 53.4333333333333)

m.c401 = Constraint(expr=   m.x99 - 2.56*m.b247 - 2.56*m.b248 - 2.55333333333333*m.b249 == 48.6133333333333)

m.c402 = Constraint(expr=   m.x100 - 1.88666666666667*m.b250 - 1.88666666666667*m.b251 - 1.88666666666667*m.b252
                          - 1.88666666666667*m.b253 == 33.9533333333333)

m.c403 = Constraint(expr=   m.x101 - 2.84*m.b254 - 2.84*m.b255 - 2.84666666666667*m.b256 == 53.9666666666667)

m.c404 = Constraint(expr=   m.x102 - 3.85333333333333*m.b257 == 77.0533333333333)

m.c405 = Constraint(expr=   m.x103 - 1.24*m.b258 == 24.9066666666667)

m.c406 = Constraint(expr=   m.x104 - 1.81333333333333*m.b259 == 36.1866666666667)

m.c407 = Constraint(expr=   m.x105 - 2.96*m.b260 - 2.96666666666667*m.b261 == 56.3133333333333)

m.c408 = Constraint(expr= - m.x106 + m.x217 <= 0)

m.c409 = Constraint(expr= - m.x107 + m.x218 <= 0)

m.c410 = Constraint(expr= - m.x108 + m.x219 <= 0)

m.c411 = Constraint(expr= - m.x109 + m.x220 <= 0)

m.c412 = Constraint(expr= - m.x110 + m.x221 <= 0)

m.c413 = Constraint(expr= - m.x111 + m.x222 <= 0)

m.c414 = Constraint(expr= - m.x112 + m.x223 <= 0)

m.c415 = Constraint(expr= - m.x113 + m.x224 <= 0)

m.c416 = Constraint(expr= - m.x114 + m.x225 <= 0)

m.c417 = Constraint(expr= - m.x115 + m.x226 <= 0)

m.c418 = Constraint(expr= - m.x116 + m.x227 <= 0)

m.c419 = Constraint(expr= - m.x117 + m.x228 <= 0)

m.c420 = Constraint(expr= - m.x118 + m.x229 <= 0)

m.c421 = Constraint(expr= - m.x119 + m.x230 <= 0)

m.c422 = Constraint(expr= - m.x120 + m.x231 <= 0)
