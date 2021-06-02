#  MINLP written by GAMS Convert at 04/21/18 13:54:11
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        343       61      234       48        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        264      210       54        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        868      754      114        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,0.26351883),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,0.26351883),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,0.26351883),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,0.22891574),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,0.22891574),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,0.22891574),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,0.21464835),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,0.21464835),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,0.21464835),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,0.17964414),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,0.17964414),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,0.17964414),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,0.17402843),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,0.17402843),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,0.17402843),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,0.15355962),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,0.15355962),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,0.15355962),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,0.1942283),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,0.1942283),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,0.1942283),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,0.25670555),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,0.25670555),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,0.25670555),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,0.27088619),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,0.27088619),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,0.27088619),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,0.28985675),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,0.28985675),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,0.28985675),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,0.25550303),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,0.25550303),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,0.25550303),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,0.19001726),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,0.19001726),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,0.19001726),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,0.23803143),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,0.23803143),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,0.23803143),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,0.23312962),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,0.23312962),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,0.23312962),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,0.27705307),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,0.27705307),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,0.27705307),initialize=0)
m.x46 = Var(within=Reals,bounds=(5.68,5.96),initialize=5.68)
m.x47 = Var(within=Reals,bounds=(40.18,42.0933333333333),initialize=40.18)
m.x48 = Var(within=Reals,bounds=(94.7666666666667,99.28),initialize=94.7666666666667)
m.x49 = Var(within=Reals,bounds=(59.0533333333333,61.8666666666667),initialize=59.0533333333333)
m.x50 = Var(within=Reals,bounds=(53.7333333333333,56.2866666666667),initialize=53.7333333333333)
m.x51 = Var(within=Reals,bounds=(37.7266666666667,41.5),initialize=37.7266666666667)
m.x52 = Var(within=Reals,bounds=(59.6466666666667,62.4933333333333),initialize=59.6466666666667)
m.x53 = Var(within=Reals,bounds=(59.2733333333333,62.24),initialize=59.2733333333333)
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
m.b76 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b77 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b78 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b79 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b80 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b81 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b82 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b83 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b84 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b85 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b86 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b87 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b88 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b89 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b90 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b91 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b92 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b93 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b94 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b95 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b96 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b97 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b98 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.x114 = Var(within=Reals,bounds=(0.25788969,0.35227087),initialize=0.25788969)
m.x115 = Var(within=Reals,bounds=(0.25788969,0.35227087),initialize=0.25788969)
m.x116 = Var(within=Reals,bounds=(0.25788969,0.35227087),initialize=0.25788969)
m.x117 = Var(within=Reals,bounds=(-0.98493628,-0.7794471),initialize=-0.7794471)
m.x118 = Var(within=Reals,bounds=(-0.98493628,-0.7794471),initialize=-0.7794471)
m.x119 = Var(within=Reals,bounds=(-0.98493628,-0.7794471),initialize=-0.7794471)
m.x120 = Var(within=Reals,bounds=(0,0.0580296499999999),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,0.0580296499999999),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,0.0580296499999999),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,0.0546689399999999),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,0.0546689399999999),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,0.0546689399999999),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,0.09360565),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,0.09360565),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,0.09360565),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,0.0476880399999999),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,0.0476880399999999),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,0.0476880399999999),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,0.05276021),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,0.05276021),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,0.05276021),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,0.04905388),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,0.04905388),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,0.04905388),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,0.07731692),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,0.07731692),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,0.07731692),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,0.08211741),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,0.08211741),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,0.08211741),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,0.08436757),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,0.08436757),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,0.08436757),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,0.06987597),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,0.06987597),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,0.06987597),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,0.04788831),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,0.04788831),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,0.04788831),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,0.0668875099999999),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,0.0668875099999999),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,0.0668875099999999),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,0.07276512),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,0.07276512),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,0.07276512),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,0.1742468),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,0.1742468),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,0.1742468),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,0.1210427),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,0.1210427),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,0.1210427),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,0.1319561),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,0.1319561),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,0.1319561),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,0.12126822),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,0.12126822),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,0.12126822),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,0.10450574),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,0.10450574),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,0.10450574),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,0.11691138),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,0.11691138),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,0.11691138),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,0.17458814),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,0.17458814),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,0.17458814),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,0.17650501),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,0.17650501),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,0.17650501),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,0.18562706),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,0.18562706),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,0.18562706),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,0.14212895),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,0.14212895),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,0.14212895),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,0.17114392),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,0.17114392),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,0.17114392),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,0.1603645),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,0.1603645),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,0.1603645),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,0.18267189),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,0.18267189),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,0.18267189),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x235 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.b255 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b256 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b257 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b258 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b259 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b260 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b261 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b262 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b263 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   m.x99 + m.x100 + m.x101 + m.x102 + m.x103 + m.x104 + m.x105 + m.x106 + m.x107 + m.x108
                        + m.x109 + m.x110 + m.x111 + m.x112 + m.x113, sense=minimize)

m.c2 = Constraint(expr=(-1.01*m.x1*m.b54) - 1.01*m.b54*m.x1 + m.x210 >= 0)

m.c3 = Constraint(expr=(-1.01*m.x2*m.b55) - 1.01*m.b55*m.x2 + m.x211 >= 0)

m.c4 = Constraint(expr=(-1.01*m.x3*m.b56) - 1.01*m.b56*m.x3 + m.x212 >= 0)

m.c5 = Constraint(expr=(-2.00666666666667*m.x4*m.b57) - 2.00666666666667*m.b57*m.x4 + m.x213 >= 0)

m.c6 = Constraint(expr=(-2.00666666666667*m.x5*m.b58) - 2.00666666666667*m.b58*m.x5 + m.x214 >= 0)

m.c7 = Constraint(expr=(-2.00666666666667*m.x6*m.b59) - 2.00666666666667*m.b59*m.x6 + m.x215 >= 0)

m.c8 = Constraint(expr=(-2.38*m.x7*m.b60) - 2.38*m.b60*m.x7 + m.x216 >= 0)

m.c9 = Constraint(expr=(-2.38*m.x8*m.b61) - 2.38*m.b61*m.x8 + m.x217 >= 0)

m.c10 = Constraint(expr=(-2.38*m.x9*m.b62) - 2.38*m.b62*m.x9 + m.x218 >= 0)

m.c11 = Constraint(expr=-m.x46*m.x10*m.b63 + m.x219 >= 0)

m.c12 = Constraint(expr=-m.x46*m.x11*m.b64 + m.x220 >= 0)

m.c13 = Constraint(expr=-m.x46*m.x12*m.b65 + m.x221 >= 0)

m.c14 = Constraint(expr=-m.x47*m.x13*m.b66 + m.x222 >= 0)

m.c15 = Constraint(expr=-m.x47*m.x14*m.b67 + m.x223 >= 0)

m.c16 = Constraint(expr=-m.x47*m.x15*m.b68 + m.x224 >= 0)

m.c17 = Constraint(expr=-m.x48*m.x16*m.b69 + m.x225 >= 0)

m.c18 = Constraint(expr=-m.x48*m.x17*m.b70 + m.x226 >= 0)

m.c19 = Constraint(expr=-m.x48*m.x18*m.b71 + m.x227 >= 0)

m.c20 = Constraint(expr=(-3.29666666666667*m.x19*m.b72) - 3.29666666666667*m.b72*m.x19 + m.x228 >= 0)

m.c21 = Constraint(expr=(-3.29666666666667*m.x20*m.b73) - 3.29666666666667*m.b73*m.x20 + m.x229 >= 0)

m.c22 = Constraint(expr=(-3.29666666666667*m.x21*m.b74) - 3.29666666666667*m.b74*m.x21 + m.x230 >= 0)

m.c23 = Constraint(expr=-m.x49*m.x22*m.b75 + m.x231 >= 0)

m.c24 = Constraint(expr=-m.x49*m.x23*m.b76 + m.x232 >= 0)

m.c25 = Constraint(expr=-m.x49*m.x24*m.b77 + m.x233 >= 0)

m.c26 = Constraint(expr=-m.x50*m.x25*m.b78 + m.x234 >= 0)

m.c27 = Constraint(expr=-m.x50*m.x26*m.b79 + m.x235 >= 0)

m.c28 = Constraint(expr=-m.x50*m.x27*m.b80 + m.x236 >= 0)

m.c29 = Constraint(expr=-m.x51*m.x28*m.b81 + m.x237 >= 0)

m.c30 = Constraint(expr=-m.x51*m.x29*m.b82 + m.x238 >= 0)

m.c31 = Constraint(expr=-m.x51*m.x30*m.b83 + m.x239 >= 0)

m.c32 = Constraint(expr=-m.x52*m.x31*m.b84 + m.x240 >= 0)

m.c33 = Constraint(expr=-m.x52*m.x32*m.b85 + m.x241 >= 0)

m.c34 = Constraint(expr=-m.x52*m.x33*m.b86 + m.x242 >= 0)

m.c35 = Constraint(expr=(-40.4533333333333*m.x34*m.b87) - 40.4533333333333*m.b87*m.x34 + m.x243 >= 0)

m.c36 = Constraint(expr=(-40.4533333333333*m.x35*m.b88) - 40.4533333333333*m.b88*m.x35 + m.x244 >= 0)

m.c37 = Constraint(expr=(-40.4533333333333*m.x36*m.b89) - 40.4533333333333*m.b89*m.x36 + m.x245 >= 0)

m.c38 = Constraint(expr=(-13.0733333333333*m.x37*m.b90) - 13.0733333333333*m.b90*m.x37 + m.x246 >= 0)

m.c39 = Constraint(expr=(-13.0733333333333*m.x38*m.b91) - 13.0733333333333*m.b91*m.x38 + m.x247 >= 0)

m.c40 = Constraint(expr=(-13.0733333333333*m.x39*m.b92) - 13.0733333333333*m.b92*m.x39 + m.x248 >= 0)

m.c41 = Constraint(expr=(-19*m.x40*m.b93) - 19*m.b93*m.x40 + m.x249 >= 0)

m.c42 = Constraint(expr=(-19*m.x41*m.b94) - 19*m.b94*m.x41 + m.x250 >= 0)

m.c43 = Constraint(expr=(-19*m.x42*m.b95) - 19*m.b95*m.x42 + m.x251 >= 0)

m.c44 = Constraint(expr=-m.x53*m.x43*m.b96 + m.x252 >= 0)

m.c45 = Constraint(expr=-m.x53*m.x44*m.b97 + m.x253 >= 0)

m.c46 = Constraint(expr=-m.x53*m.x45*m.b98 + m.x254 >= 0)

m.c47 = Constraint(expr=   m.b54 + m.b55 + m.b56 == 1)

m.c48 = Constraint(expr=   m.b57 + m.b58 + m.b59 == 1)

m.c49 = Constraint(expr=   m.b60 + m.b61 + m.b62 == 1)

m.c50 = Constraint(expr=   m.b63 + m.b64 + m.b65 == 1)

m.c51 = Constraint(expr=   m.b66 + m.b67 + m.b68 == 1)

m.c52 = Constraint(expr=   m.b69 + m.b70 + m.b71 == 1)

m.c53 = Constraint(expr=   m.b72 + m.b73 + m.b74 == 1)

m.c54 = Constraint(expr=   m.b75 + m.b76 + m.b77 == 1)

m.c55 = Constraint(expr=   m.b78 + m.b79 + m.b80 == 1)

m.c56 = Constraint(expr=   m.b81 + m.b82 + m.b83 == 1)

m.c57 = Constraint(expr=   m.b84 + m.b85 + m.b86 == 1)

m.c58 = Constraint(expr=   m.b87 + m.b88 + m.b89 == 1)

m.c59 = Constraint(expr=   m.b90 + m.b91 + m.b92 == 1)

m.c60 = Constraint(expr=   m.b93 + m.b94 + m.b95 == 1)

m.c61 = Constraint(expr=   m.b96 + m.b97 + m.b98 == 1)

m.c62 = Constraint(expr=   2.02*m.b54 + 4.01333333333333*m.b57 + 4.76*m.b60 + 5.96*m.b63 + 42.0933333333333*m.b66
                         + 99.28*m.b69 + 6.59333333333333*m.b72 + 61.8666666666667*m.b75 + 56.2866666666667*m.b78
                         + 41.5*m.b81 + 62.4933333333333*m.b84 + 80.9066666666667*m.b87 + 26.1466666666667*m.b90
                         + 38*m.b93 + 62.24*m.b96 <= 213.053333333333)

m.c63 = Constraint(expr=   2.02*m.b55 + 4.01333333333333*m.b58 + 4.76*m.b61 + 5.96*m.b64 + 42.0933333333333*m.b67
                         + 99.28*m.b70 + 6.59333333333333*m.b73 + 61.8666666666667*m.b76 + 56.2866666666667*m.b79
                         + 41.5*m.b82 + 62.4933333333333*m.b85 + 80.9066666666667*m.b88 + 26.1466666666667*m.b91
                         + 38*m.b94 + 62.24*m.b97 <= 213.053333333333)

m.c64 = Constraint(expr=   2.02*m.b56 + 4.01333333333333*m.b59 + 4.76*m.b62 + 5.96*m.b65 + 42.0933333333333*m.b68
                         + 99.28*m.b71 + 6.59333333333333*m.b74 + 61.8666666666667*m.b77 + 56.2866666666667*m.b80
                         + 41.5*m.b83 + 62.4933333333333*m.b86 + 80.9066666666667*m.b89 + 26.1466666666667*m.b92
                         + 38*m.b95 + 62.24*m.b98 <= 213.053333333333)

m.c65 = Constraint(expr=   m.x114 + m.x120 >= 0.29424122)

m.c66 = Constraint(expr=   m.x115 + m.x121 >= 0.29424122)

m.c67 = Constraint(expr=   m.x116 + m.x122 >= 0.29424122)

m.c68 = Constraint(expr=   m.x114 + m.x123 >= 0.29760193)

m.c69 = Constraint(expr=   m.x115 + m.x124 >= 0.29760193)

m.c70 = Constraint(expr=   m.x116 + m.x125 >= 0.29760193)

m.c71 = Constraint(expr=   m.x114 + m.x126 >= 0.35149534)

m.c72 = Constraint(expr=   m.x115 + m.x127 >= 0.35149534)

m.c73 = Constraint(expr=   m.x116 + m.x128 >= 0.35149534)

m.c74 = Constraint(expr=   m.x114 + m.x129 >= 0.30458283)

m.c75 = Constraint(expr=   m.x115 + m.x130 >= 0.30458283)

m.c76 = Constraint(expr=   m.x116 + m.x131 >= 0.30458283)

m.c77 = Constraint(expr=   m.x114 + m.x132 >= 0.29951066)

m.c78 = Constraint(expr=   m.x115 + m.x133 >= 0.29951066)

m.c79 = Constraint(expr=   m.x116 + m.x134 >= 0.29951066)

m.c80 = Constraint(expr=   m.x114 + m.x135 >= 0.30694357)

m.c81 = Constraint(expr=   m.x115 + m.x136 >= 0.30694357)

m.c82 = Constraint(expr=   m.x116 + m.x137 >= 0.30694357)

m.c83 = Constraint(expr=   m.x114 + m.x138 >= 0.33520661)

m.c84 = Constraint(expr=   m.x115 + m.x139 >= 0.33520661)

m.c85 = Constraint(expr=   m.x116 + m.x140 >= 0.33520661)

m.c86 = Constraint(expr=   m.x114 + m.x141 >= 0.3400071)

m.c87 = Constraint(expr=   m.x115 + m.x142 >= 0.3400071)

m.c88 = Constraint(expr=   m.x116 + m.x143 >= 0.3400071)

m.c89 = Constraint(expr=   m.x114 + m.x144 >= 0.35227087)

m.c90 = Constraint(expr=   m.x115 + m.x145 >= 0.35227087)

m.c91 = Constraint(expr=   m.x116 + m.x146 >= 0.35227087)

m.c92 = Constraint(expr=   m.x114 + m.x147 >= 0.34225726)

m.c93 = Constraint(expr=   m.x115 + m.x148 >= 0.34225726)

m.c94 = Constraint(expr=   m.x116 + m.x149 >= 0.34225726)

m.c95 = Constraint(expr=   m.x114 + m.x150 >= 0.32776566)

m.c96 = Constraint(expr=   m.x115 + m.x151 >= 0.32776566)

m.c97 = Constraint(expr=   m.x116 + m.x152 >= 0.32776566)

m.c98 = Constraint(expr=   m.x114 + m.x153 >= 0.30438256)

m.c99 = Constraint(expr=   m.x115 + m.x154 >= 0.30438256)

m.c100 = Constraint(expr=   m.x116 + m.x155 >= 0.30438256)

m.c101 = Constraint(expr=   m.x114 + m.x156 >= 0.28538336)

m.c102 = Constraint(expr=   m.x115 + m.x157 >= 0.28538336)

m.c103 = Constraint(expr=   m.x116 + m.x158 >= 0.28538336)

m.c104 = Constraint(expr=   m.x114 + m.x159 >= 0.27950575)

m.c105 = Constraint(expr=   m.x115 + m.x160 >= 0.27950575)

m.c106 = Constraint(expr=   m.x116 + m.x161 >= 0.27950575)

m.c107 = Constraint(expr= - m.x114 + m.x120 >= -0.29424122)

m.c108 = Constraint(expr= - m.x115 + m.x121 >= -0.29424122)

m.c109 = Constraint(expr= - m.x116 + m.x122 >= -0.29424122)

m.c110 = Constraint(expr= - m.x114 + m.x123 >= -0.29760193)

m.c111 = Constraint(expr= - m.x115 + m.x124 >= -0.29760193)

m.c112 = Constraint(expr= - m.x116 + m.x125 >= -0.29760193)

m.c113 = Constraint(expr= - m.x114 + m.x126 >= -0.35149534)

m.c114 = Constraint(expr= - m.x115 + m.x127 >= -0.35149534)

m.c115 = Constraint(expr= - m.x116 + m.x128 >= -0.35149534)

m.c116 = Constraint(expr= - m.x114 + m.x129 >= -0.30458283)

m.c117 = Constraint(expr= - m.x115 + m.x130 >= -0.30458283)

m.c118 = Constraint(expr= - m.x116 + m.x131 >= -0.30458283)

m.c119 = Constraint(expr= - m.x114 + m.x132 >= -0.29951066)

m.c120 = Constraint(expr= - m.x115 + m.x133 >= -0.29951066)

m.c121 = Constraint(expr= - m.x116 + m.x134 >= -0.29951066)

m.c122 = Constraint(expr= - m.x114 + m.x135 >= -0.30694357)

m.c123 = Constraint(expr= - m.x115 + m.x136 >= -0.30694357)

m.c124 = Constraint(expr= - m.x116 + m.x137 >= -0.30694357)

m.c125 = Constraint(expr= - m.x114 + m.x138 >= -0.33520661)

m.c126 = Constraint(expr= - m.x115 + m.x139 >= -0.33520661)

m.c127 = Constraint(expr= - m.x116 + m.x140 >= -0.33520661)

m.c128 = Constraint(expr= - m.x114 + m.x141 >= -0.3400071)

m.c129 = Constraint(expr= - m.x115 + m.x142 >= -0.3400071)

m.c130 = Constraint(expr= - m.x116 + m.x143 >= -0.3400071)

m.c131 = Constraint(expr= - m.x114 + m.x147 >= -0.34225726)

m.c132 = Constraint(expr= - m.x115 + m.x148 >= -0.34225726)

m.c133 = Constraint(expr= - m.x116 + m.x149 >= -0.34225726)

m.c134 = Constraint(expr= - m.x114 + m.x150 >= -0.32776566)

m.c135 = Constraint(expr= - m.x115 + m.x151 >= -0.32776566)

m.c136 = Constraint(expr= - m.x116 + m.x152 >= -0.32776566)

m.c137 = Constraint(expr= - m.x114 + m.x153 >= -0.30438256)

m.c138 = Constraint(expr= - m.x115 + m.x154 >= -0.30438256)

m.c139 = Constraint(expr= - m.x116 + m.x155 >= -0.30438256)

m.c140 = Constraint(expr= - m.x114 + m.x156 >= -0.28538336)

m.c141 = Constraint(expr= - m.x115 + m.x157 >= -0.28538336)

m.c142 = Constraint(expr= - m.x116 + m.x158 >= -0.28538336)

m.c143 = Constraint(expr= - m.x114 + m.x159 >= -0.27950575)

m.c144 = Constraint(expr= - m.x115 + m.x160 >= -0.27950575)

m.c145 = Constraint(expr= - m.x116 + m.x161 >= -0.27950575)

m.c146 = Constraint(expr= - m.x114 + m.x162 >= -0.25788969)

m.c147 = Constraint(expr= - m.x115 + m.x163 >= -0.25788969)

m.c148 = Constraint(expr= - m.x116 + m.x164 >= -0.25788969)

m.c149 = Constraint(expr=   m.x117 + m.x168 >= -0.9536939)

m.c150 = Constraint(expr=   m.x118 + m.x169 >= -0.9536939)

m.c151 = Constraint(expr=   m.x119 + m.x170 >= -0.9536939)

m.c152 = Constraint(expr=   m.x117 + m.x171 >= -0.9004898)

m.c153 = Constraint(expr=   m.x118 + m.x172 >= -0.9004898)

m.c154 = Constraint(expr=   m.x119 + m.x173 >= -0.9004898)

m.c155 = Constraint(expr=   m.x117 + m.x174 >= -0.9114032)

m.c156 = Constraint(expr=   m.x118 + m.x175 >= -0.9114032)

m.c157 = Constraint(expr=   m.x119 + m.x176 >= -0.9114032)

m.c158 = Constraint(expr=   m.x117 + m.x177 >= -0.90071532)

m.c159 = Constraint(expr=   m.x118 + m.x178 >= -0.90071532)

m.c160 = Constraint(expr=   m.x119 + m.x179 >= -0.90071532)

m.c161 = Constraint(expr=   m.x117 + m.x180 >= -0.88043054)

m.c162 = Constraint(expr=   m.x118 + m.x181 >= -0.88043054)

m.c163 = Constraint(expr=   m.x119 + m.x182 >= -0.88043054)

m.c164 = Constraint(expr=   m.x117 + m.x183 >= -0.8680249)

m.c165 = Constraint(expr=   m.x118 + m.x184 >= -0.8680249)

m.c166 = Constraint(expr=   m.x119 + m.x185 >= -0.8680249)

m.c167 = Constraint(expr=   m.x117 + m.x186 >= -0.81034814)

m.c168 = Constraint(expr=   m.x118 + m.x187 >= -0.81034814)

m.c169 = Constraint(expr=   m.x119 + m.x188 >= -0.81034814)

m.c170 = Constraint(expr=   m.x117 + m.x189 >= -0.80843127)

m.c171 = Constraint(expr=   m.x118 + m.x190 >= -0.80843127)

m.c172 = Constraint(expr=   m.x119 + m.x191 >= -0.80843127)

m.c173 = Constraint(expr=   m.x117 + m.x192 >= -0.7794471)

m.c174 = Constraint(expr=   m.x118 + m.x193 >= -0.7794471)

m.c175 = Constraint(expr=   m.x119 + m.x194 >= -0.7794471)

m.c176 = Constraint(expr=   m.x117 + m.x195 >= -0.79930922)

m.c177 = Constraint(expr=   m.x118 + m.x196 >= -0.79930922)

m.c178 = Constraint(expr=   m.x119 + m.x197 >= -0.79930922)

m.c179 = Constraint(expr=   m.x117 + m.x198 >= -0.84280733)

m.c180 = Constraint(expr=   m.x118 + m.x199 >= -0.84280733)

m.c181 = Constraint(expr=   m.x119 + m.x200 >= -0.84280733)

m.c182 = Constraint(expr=   m.x117 + m.x201 >= -0.81379236)

m.c183 = Constraint(expr=   m.x118 + m.x202 >= -0.81379236)

m.c184 = Constraint(expr=   m.x119 + m.x203 >= -0.81379236)

m.c185 = Constraint(expr=   m.x117 + m.x204 >= -0.82457178)

m.c186 = Constraint(expr=   m.x118 + m.x205 >= -0.82457178)

m.c187 = Constraint(expr=   m.x119 + m.x206 >= -0.82457178)

m.c188 = Constraint(expr=   m.x117 + m.x207 >= -0.80226439)

m.c189 = Constraint(expr=   m.x118 + m.x208 >= -0.80226439)

m.c190 = Constraint(expr=   m.x119 + m.x209 >= -0.80226439)

m.c191 = Constraint(expr= - m.x117 + m.x165 >= 0.98493628)

m.c192 = Constraint(expr= - m.x118 + m.x166 >= 0.98493628)

m.c193 = Constraint(expr= - m.x119 + m.x167 >= 0.98493628)

m.c194 = Constraint(expr= - m.x117 + m.x168 >= 0.9536939)

m.c195 = Constraint(expr= - m.x118 + m.x169 >= 0.9536939)

m.c196 = Constraint(expr= - m.x119 + m.x170 >= 0.9536939)

m.c197 = Constraint(expr= - m.x117 + m.x171 >= 0.9004898)

m.c198 = Constraint(expr= - m.x118 + m.x172 >= 0.9004898)

m.c199 = Constraint(expr= - m.x119 + m.x173 >= 0.9004898)

m.c200 = Constraint(expr= - m.x117 + m.x174 >= 0.9114032)

m.c201 = Constraint(expr= - m.x118 + m.x175 >= 0.9114032)

m.c202 = Constraint(expr= - m.x119 + m.x176 >= 0.9114032)

m.c203 = Constraint(expr= - m.x117 + m.x177 >= 0.90071532)

m.c204 = Constraint(expr= - m.x118 + m.x178 >= 0.90071532)

m.c205 = Constraint(expr= - m.x119 + m.x179 >= 0.90071532)

m.c206 = Constraint(expr= - m.x117 + m.x180 >= 0.88043054)

m.c207 = Constraint(expr= - m.x118 + m.x181 >= 0.88043054)

m.c208 = Constraint(expr= - m.x119 + m.x182 >= 0.88043054)

m.c209 = Constraint(expr= - m.x117 + m.x183 >= 0.8680249)

m.c210 = Constraint(expr= - m.x118 + m.x184 >= 0.8680249)

m.c211 = Constraint(expr= - m.x119 + m.x185 >= 0.8680249)

m.c212 = Constraint(expr= - m.x117 + m.x186 >= 0.81034814)

m.c213 = Constraint(expr= - m.x118 + m.x187 >= 0.81034814)

m.c214 = Constraint(expr= - m.x119 + m.x188 >= 0.81034814)

m.c215 = Constraint(expr= - m.x117 + m.x189 >= 0.80843127)

m.c216 = Constraint(expr= - m.x118 + m.x190 >= 0.80843127)

m.c217 = Constraint(expr= - m.x119 + m.x191 >= 0.80843127)

m.c218 = Constraint(expr= - m.x117 + m.x195 >= 0.79930922)

m.c219 = Constraint(expr= - m.x118 + m.x196 >= 0.79930922)

m.c220 = Constraint(expr= - m.x119 + m.x197 >= 0.79930922)

m.c221 = Constraint(expr= - m.x117 + m.x198 >= 0.84280733)

m.c222 = Constraint(expr= - m.x118 + m.x199 >= 0.84280733)

m.c223 = Constraint(expr= - m.x119 + m.x200 >= 0.84280733)

m.c224 = Constraint(expr= - m.x117 + m.x201 >= 0.81379236)

m.c225 = Constraint(expr= - m.x118 + m.x202 >= 0.81379236)

m.c226 = Constraint(expr= - m.x119 + m.x203 >= 0.81379236)

m.c227 = Constraint(expr= - m.x117 + m.x204 >= 0.82457178)

m.c228 = Constraint(expr= - m.x118 + m.x205 >= 0.82457178)

m.c229 = Constraint(expr= - m.x119 + m.x206 >= 0.82457178)

m.c230 = Constraint(expr= - m.x117 + m.x207 >= 0.80226439)

m.c231 = Constraint(expr= - m.x118 + m.x208 >= 0.80226439)

m.c232 = Constraint(expr= - m.x119 + m.x209 >= 0.80226439)

m.c233 = Constraint(expr=   m.x1 - m.x120 - m.x165 == 0)

m.c234 = Constraint(expr=   m.x2 - m.x121 - m.x166 == 0)

m.c235 = Constraint(expr=   m.x3 - m.x122 - m.x167 == 0)

m.c236 = Constraint(expr=   m.x4 - m.x123 - m.x168 == 0)

m.c237 = Constraint(expr=   m.x5 - m.x124 - m.x169 == 0)

m.c238 = Constraint(expr=   m.x6 - m.x125 - m.x170 == 0)

m.c239 = Constraint(expr=   m.x7 - m.x126 - m.x171 == 0)

m.c240 = Constraint(expr=   m.x8 - m.x127 - m.x172 == 0)

m.c241 = Constraint(expr=   m.x9 - m.x128 - m.x173 == 0)

m.c242 = Constraint(expr=   m.x10 - m.x129 - m.x174 == 0)

m.c243 = Constraint(expr=   m.x11 - m.x130 - m.x175 == 0)

m.c244 = Constraint(expr=   m.x12 - m.x131 - m.x176 == 0)

m.c245 = Constraint(expr=   m.x13 - m.x132 - m.x177 == 0)

m.c246 = Constraint(expr=   m.x14 - m.x133 - m.x178 == 0)

m.c247 = Constraint(expr=   m.x15 - m.x134 - m.x179 == 0)

m.c248 = Constraint(expr=   m.x16 - m.x135 - m.x180 == 0)

m.c249 = Constraint(expr=   m.x17 - m.x136 - m.x181 == 0)

m.c250 = Constraint(expr=   m.x18 - m.x137 - m.x182 == 0)

m.c251 = Constraint(expr=   m.x19 - m.x138 - m.x183 == 0)

m.c252 = Constraint(expr=   m.x20 - m.x139 - m.x184 == 0)

m.c253 = Constraint(expr=   m.x21 - m.x140 - m.x185 == 0)

m.c254 = Constraint(expr=   m.x22 - m.x141 - m.x186 == 0)

m.c255 = Constraint(expr=   m.x23 - m.x142 - m.x187 == 0)

m.c256 = Constraint(expr=   m.x24 - m.x143 - m.x188 == 0)

m.c257 = Constraint(expr=   m.x25 - m.x144 - m.x189 == 0)

m.c258 = Constraint(expr=   m.x26 - m.x145 - m.x190 == 0)

m.c259 = Constraint(expr=   m.x27 - m.x146 - m.x191 == 0)

m.c260 = Constraint(expr=   m.x28 - m.x147 - m.x192 == 0)

m.c261 = Constraint(expr=   m.x29 - m.x148 - m.x193 == 0)

m.c262 = Constraint(expr=   m.x30 - m.x149 - m.x194 == 0)

m.c263 = Constraint(expr=   m.x31 - m.x150 - m.x195 == 0)

m.c264 = Constraint(expr=   m.x32 - m.x151 - m.x196 == 0)

m.c265 = Constraint(expr=   m.x33 - m.x152 - m.x197 == 0)

m.c266 = Constraint(expr=   m.x34 - m.x153 - m.x198 == 0)

m.c267 = Constraint(expr=   m.x35 - m.x154 - m.x199 == 0)

m.c268 = Constraint(expr=   m.x36 - m.x155 - m.x200 == 0)

m.c269 = Constraint(expr=   m.x37 - m.x156 - m.x201 == 0)

m.c270 = Constraint(expr=   m.x38 - m.x157 - m.x202 == 0)

m.c271 = Constraint(expr=   m.x39 - m.x158 - m.x203 == 0)

m.c272 = Constraint(expr=   m.x40 - m.x159 - m.x204 == 0)

m.c273 = Constraint(expr=   m.x41 - m.x160 - m.x205 == 0)

m.c274 = Constraint(expr=   m.x42 - m.x161 - m.x206 == 0)

m.c275 = Constraint(expr=   m.x43 - m.x162 - m.x207 == 0)

m.c276 = Constraint(expr=   m.x44 - m.x163 - m.x208 == 0)

m.c277 = Constraint(expr=   m.x45 - m.x164 - m.x209 == 0)

m.c278 = Constraint(expr=   m.b256 + m.b257 >= 1)

m.c279 = Constraint(expr=   m.b255 + m.b257 >= 1)

m.c280 = Constraint(expr=   m.b255 + m.b256 >= 1)

m.c281 = Constraint(expr=   m.b257 + m.b259 >= 1)

m.c282 = Constraint(expr=   m.b257 + m.b258 >= 1)

m.c283 = Constraint(expr=   m.b256 + m.b259 >= 1)

m.c284 = Constraint(expr=   m.b256 + m.b258 >= 1)

m.c285 = Constraint(expr=   m.b255 + m.b259 >= 1)

m.c286 = Constraint(expr=   m.b255 + m.b258 >= 1)

m.c287 = Constraint(expr=   m.x46 - 5.96*m.b255 >= 0)

m.c288 = Constraint(expr=   m.x47 - 42.0933333333333*m.b256 >= 0)

m.c289 = Constraint(expr=   m.x48 - 99.28*m.b257 >= 0)

m.c290 = Constraint(expr=   m.x49 - 61.8666666666667*m.b258 >= 0)

m.c291 = Constraint(expr=   m.x50 - 56.2866666666667*m.b259 >= 0)

m.c292 = Constraint(expr=   m.x51 - 39.6133333333333*m.b260 >= 0)

m.c293 = Constraint(expr=   m.x51 - 41.5*m.b261 >= 0)

m.c294 = Constraint(expr=   m.x52 - 62.4933333333333*m.b262 >= 0)

m.c295 = Constraint(expr=   m.x53 - 62.24*m.b263 >= 0)

m.c296 = Constraint(expr= - m.x99 + m.x210 <= 0)

m.c297 = Constraint(expr= - m.x99 + m.x211 <= 0)

m.c298 = Constraint(expr= - m.x99 + m.x212 <= 0)

m.c299 = Constraint(expr= - m.x100 + m.x213 <= 0)

m.c300 = Constraint(expr= - m.x100 + m.x214 <= 0)

m.c301 = Constraint(expr= - m.x100 + m.x215 <= 0)

m.c302 = Constraint(expr= - m.x101 + m.x216 <= 0)

m.c303 = Constraint(expr= - m.x101 + m.x217 <= 0)

m.c304 = Constraint(expr= - m.x101 + m.x218 <= 0)

m.c305 = Constraint(expr= - m.x102 + m.x219 <= 0)

m.c306 = Constraint(expr= - m.x102 + m.x220 <= 0)

m.c307 = Constraint(expr= - m.x102 + m.x221 <= 0)

m.c308 = Constraint(expr= - m.x103 + m.x222 <= 0)

m.c309 = Constraint(expr= - m.x103 + m.x223 <= 0)

m.c310 = Constraint(expr= - m.x103 + m.x224 <= 0)

m.c311 = Constraint(expr= - m.x104 + m.x225 <= 0)

m.c312 = Constraint(expr= - m.x104 + m.x226 <= 0)

m.c313 = Constraint(expr= - m.x104 + m.x227 <= 0)

m.c314 = Constraint(expr= - m.x105 + m.x228 <= 0)

m.c315 = Constraint(expr= - m.x105 + m.x229 <= 0)

m.c316 = Constraint(expr= - m.x105 + m.x230 <= 0)

m.c317 = Constraint(expr= - m.x106 + m.x231 <= 0)

m.c318 = Constraint(expr= - m.x106 + m.x232 <= 0)

m.c319 = Constraint(expr= - m.x106 + m.x233 <= 0)

m.c320 = Constraint(expr= - m.x107 + m.x234 <= 0)

m.c321 = Constraint(expr= - m.x107 + m.x235 <= 0)

m.c322 = Constraint(expr= - m.x107 + m.x236 <= 0)

m.c323 = Constraint(expr= - m.x108 + m.x237 <= 0)

m.c324 = Constraint(expr= - m.x108 + m.x238 <= 0)

m.c325 = Constraint(expr= - m.x108 + m.x239 <= 0)

m.c326 = Constraint(expr= - m.x109 + m.x240 <= 0)

m.c327 = Constraint(expr= - m.x109 + m.x241 <= 0)

m.c328 = Constraint(expr= - m.x109 + m.x242 <= 0)

m.c329 = Constraint(expr= - m.x110 + m.x243 <= 0)

m.c330 = Constraint(expr= - m.x110 + m.x244 <= 0)

m.c331 = Constraint(expr= - m.x110 + m.x245 <= 0)

m.c332 = Constraint(expr= - m.x111 + m.x246 <= 0)

m.c333 = Constraint(expr= - m.x111 + m.x247 <= 0)

m.c334 = Constraint(expr= - m.x111 + m.x248 <= 0)

m.c335 = Constraint(expr= - m.x112 + m.x249 <= 0)

m.c336 = Constraint(expr= - m.x112 + m.x250 <= 0)

m.c337 = Constraint(expr= - m.x112 + m.x251 <= 0)

m.c338 = Constraint(expr= - m.x113 + m.x252 <= 0)

m.c339 = Constraint(expr= - m.x113 + m.x253 <= 0)

m.c340 = Constraint(expr= - m.x113 + m.x254 <= 0)

m.c341 = Constraint(expr=   m.b260 - m.b261 >= 0)

m.c342 = Constraint(expr=   m.x117 - m.x118 >= 0)

m.c343 = Constraint(expr=   m.x118 - m.x119 >= 0)
