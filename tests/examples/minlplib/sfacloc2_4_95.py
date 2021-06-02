#  MINLP written by GAMS Convert at 04/21/18 13:54:11
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        446       76      306       64        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        341      272       69        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1140      988      152        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,0.26351883),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,0.26351883),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,0.26351883),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,0.26351883),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,0.22891574),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,0.22891574),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,0.22891574),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,0.22891574),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,0.21464835),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,0.21464835),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,0.21464835),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,0.21464835),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,0.17964414),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,0.17964414),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,0.17964414),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,0.17964414),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,0.17402843),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,0.17402843),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,0.17402843),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,0.17402843),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,0.15355962),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,0.15355962),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,0.15355962),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,0.15355962),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,0.1942283),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,0.1942283),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,0.1942283),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,0.1942283),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,0.25670555),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,0.25670555),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,0.25670555),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,0.25670555),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,0.27088619),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,0.27088619),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,0.27088619),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,0.27088619),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,0.28985675),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,0.28985675),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,0.28985675),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,0.28985675),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,0.25550303),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,0.25550303),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,0.25550303),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,0.25550303),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,0.19001726),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,0.19001726),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,0.19001726),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,0.19001726),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,0.23803143),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,0.23803143),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,0.23803143),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,0.23803143),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,0.23312962),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,0.23312962),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,0.23312962),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,0.23312962),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,0.27705307),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,0.27705307),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,0.27705307),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,0.27705307),initialize=0)
m.x61 = Var(within=Reals,bounds=(5.68,5.96),initialize=5.68)
m.x62 = Var(within=Reals,bounds=(40.18,42.0933333333333),initialize=40.18)
m.x63 = Var(within=Reals,bounds=(94.7666666666667,99.28),initialize=94.7666666666667)
m.x64 = Var(within=Reals,bounds=(59.0533333333333,61.8666666666667),initialize=59.0533333333333)
m.x65 = Var(within=Reals,bounds=(53.7333333333333,56.2866666666667),initialize=53.7333333333333)
m.x66 = Var(within=Reals,bounds=(37.7266666666667,41.5),initialize=37.7266666666667)
m.x67 = Var(within=Reals,bounds=(59.6466666666667,62.4933333333333),initialize=59.6466666666667)
m.x68 = Var(within=Reals,bounds=(59.2733333333333,62.24),initialize=59.2733333333333)
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
m.b99 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b100 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b101 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b102 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b103 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b104 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b105 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b106 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b109 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b128 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.x144 = Var(within=Reals,bounds=(0.25788969,0.35227087),initialize=0.25788969)
m.x145 = Var(within=Reals,bounds=(0.25788969,0.35227087),initialize=0.25788969)
m.x146 = Var(within=Reals,bounds=(0.25788969,0.35227087),initialize=0.25788969)
m.x147 = Var(within=Reals,bounds=(0.25788969,0.35227087),initialize=0.25788969)
m.x148 = Var(within=Reals,bounds=(-0.98493628,-0.7794471),initialize=-0.7794471)
m.x149 = Var(within=Reals,bounds=(-0.98493628,-0.7794471),initialize=-0.7794471)
m.x150 = Var(within=Reals,bounds=(-0.98493628,-0.7794471),initialize=-0.7794471)
m.x151 = Var(within=Reals,bounds=(-0.98493628,-0.7794471),initialize=-0.7794471)
m.x152 = Var(within=Reals,bounds=(0,0.0580296499999999),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,0.0580296499999999),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,0.0580296499999999),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,0.0580296499999999),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,0.0546689399999999),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,0.0546689399999999),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,0.0546689399999999),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,0.0546689399999999),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,0.09360565),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,0.09360565),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,0.09360565),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,0.09360565),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,0.0476880399999999),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,0.0476880399999999),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,0.0476880399999999),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,0.0476880399999999),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,0.05276021),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,0.05276021),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,0.05276021),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,0.05276021),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,0.04905388),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,0.04905388),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,0.04905388),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,0.04905388),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,0.07731692),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,0.07731692),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,0.07731692),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,0.07731692),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,0.08211741),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,0.08211741),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,0.08211741),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,0.08211741),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,0.08436757),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,0.08436757),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,0.08436757),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,0.08436757),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,0.06987597),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,0.06987597),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,0.06987597),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,0.06987597),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,0.04788831),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,0.04788831),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,0.04788831),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,0.04788831),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,0.0668875099999999),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,0.0668875099999999),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,0.0668875099999999),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,0.0668875099999999),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,0.07276512),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,0.07276512),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,0.07276512),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,0.07276512),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,0.1742468),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,0.1742468),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,0.1742468),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,0.1742468),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,0.1210427),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,0.1210427),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,0.1210427),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,0.1210427),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,0.1319561),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,0.1319561),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,0.1319561),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,0.1319561),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,0.12126822),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,0.12126822),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,0.12126822),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,0.12126822),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,0.10450574),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,0.10450574),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,0.10450574),initialize=0)
m.x235 = Var(within=Reals,bounds=(0,0.10450574),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,0.11691138),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,0.11691138),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,0.11691138),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,0.11691138),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,0.17458814),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,0.17458814),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,0.17458814),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,0.17458814),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,0.17650501),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,0.17650501),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,0.17650501),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,0.17650501),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,0.18562706),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,0.18562706),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,0.18562706),initialize=0)
m.x255 = Var(within=Reals,bounds=(0,0.18562706),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,0.14212895),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,0.14212895),initialize=0)
m.x258 = Var(within=Reals,bounds=(0,0.14212895),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,0.14212895),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,0.17114392),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,0.17114392),initialize=0)
m.x262 = Var(within=Reals,bounds=(0,0.17114392),initialize=0)
m.x263 = Var(within=Reals,bounds=(0,0.17114392),initialize=0)
m.x264 = Var(within=Reals,bounds=(0,0.1603645),initialize=0)
m.x265 = Var(within=Reals,bounds=(0,0.1603645),initialize=0)
m.x266 = Var(within=Reals,bounds=(0,0.1603645),initialize=0)
m.x267 = Var(within=Reals,bounds=(0,0.1603645),initialize=0)
m.x268 = Var(within=Reals,bounds=(0,0.18267189),initialize=0)
m.x269 = Var(within=Reals,bounds=(0,0.18267189),initialize=0)
m.x270 = Var(within=Reals,bounds=(0,0.18267189),initialize=0)
m.x271 = Var(within=Reals,bounds=(0,0.18267189),initialize=0)
m.x272 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x273 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x274 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x275 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x276 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x277 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x278 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x279 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x280 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x281 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x282 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x283 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x284 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x285 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x286 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x287 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x289 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x290 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x291 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x292 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x293 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x294 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x295 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x296 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x297 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x298 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x299 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x300 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x301 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x302 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x303 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x304 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x305 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x306 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x307 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x309 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x311 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x312 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x313 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x314 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x315 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x316 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x317 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x318 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x319 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x320 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x321 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x322 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x323 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x324 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x325 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x326 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x327 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x328 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.x329 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.x330 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.x331 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.b332 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b333 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b334 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b335 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b336 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b337 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b338 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b339 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b340 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   m.x129 + m.x130 + m.x131 + m.x132 + m.x133 + m.x134 + m.x135 + m.x136 + m.x137 + m.x138
                        + m.x139 + m.x140 + m.x141 + m.x142 + m.x143, sense=minimize)

m.c2 = Constraint(expr=(-1.01*m.x1*m.b69) - 1.01*m.b69*m.x1 + m.x272 >= 0)

m.c3 = Constraint(expr=(-1.01*m.x2*m.b70) - 1.01*m.b70*m.x2 + m.x273 >= 0)

m.c4 = Constraint(expr=(-1.01*m.x3*m.b71) - 1.01*m.b71*m.x3 + m.x274 >= 0)

m.c5 = Constraint(expr=(-1.01*m.x4*m.b72) - 1.01*m.b72*m.x4 + m.x275 >= 0)

m.c6 = Constraint(expr=(-2.00666666666667*m.x5*m.b73) - 2.00666666666667*m.b73*m.x5 + m.x276 >= 0)

m.c7 = Constraint(expr=(-2.00666666666667*m.x6*m.b74) - 2.00666666666667*m.b74*m.x6 + m.x277 >= 0)

m.c8 = Constraint(expr=(-2.00666666666667*m.x7*m.b75) - 2.00666666666667*m.b75*m.x7 + m.x278 >= 0)

m.c9 = Constraint(expr=(-2.00666666666667*m.x8*m.b76) - 2.00666666666667*m.b76*m.x8 + m.x279 >= 0)

m.c10 = Constraint(expr=(-2.38*m.x9*m.b77) - 2.38*m.b77*m.x9 + m.x280 >= 0)

m.c11 = Constraint(expr=(-2.38*m.x10*m.b78) - 2.38*m.b78*m.x10 + m.x281 >= 0)

m.c12 = Constraint(expr=(-2.38*m.x11*m.b79) - 2.38*m.b79*m.x11 + m.x282 >= 0)

m.c13 = Constraint(expr=(-2.38*m.x12*m.b80) - 2.38*m.b80*m.x12 + m.x283 >= 0)

m.c14 = Constraint(expr=-m.x61*m.x13*m.b81 + m.x284 >= 0)

m.c15 = Constraint(expr=-m.x61*m.x14*m.b82 + m.x285 >= 0)

m.c16 = Constraint(expr=-m.x61*m.x15*m.b83 + m.x286 >= 0)

m.c17 = Constraint(expr=-m.x61*m.x16*m.b84 + m.x287 >= 0)

m.c18 = Constraint(expr=-m.x62*m.x17*m.b85 + m.x288 >= 0)

m.c19 = Constraint(expr=-m.x62*m.x18*m.b86 + m.x289 >= 0)

m.c20 = Constraint(expr=-m.x62*m.x19*m.b87 + m.x290 >= 0)

m.c21 = Constraint(expr=-m.x62*m.x20*m.b88 + m.x291 >= 0)

m.c22 = Constraint(expr=-m.x63*m.x21*m.b89 + m.x292 >= 0)

m.c23 = Constraint(expr=-m.x63*m.x22*m.b90 + m.x293 >= 0)

m.c24 = Constraint(expr=-m.x63*m.x23*m.b91 + m.x294 >= 0)

m.c25 = Constraint(expr=-m.x63*m.x24*m.b92 + m.x295 >= 0)

m.c26 = Constraint(expr=(-3.29666666666667*m.x25*m.b93) - 3.29666666666667*m.b93*m.x25 + m.x296 >= 0)

m.c27 = Constraint(expr=(-3.29666666666667*m.x26*m.b94) - 3.29666666666667*m.b94*m.x26 + m.x297 >= 0)

m.c28 = Constraint(expr=(-3.29666666666667*m.x27*m.b95) - 3.29666666666667*m.b95*m.x27 + m.x298 >= 0)

m.c29 = Constraint(expr=(-3.29666666666667*m.x28*m.b96) - 3.29666666666667*m.b96*m.x28 + m.x299 >= 0)

m.c30 = Constraint(expr=-m.x64*m.x29*m.b97 + m.x300 >= 0)

m.c31 = Constraint(expr=-m.x64*m.x30*m.b98 + m.x301 >= 0)

m.c32 = Constraint(expr=-m.x64*m.x31*m.b99 + m.x302 >= 0)

m.c33 = Constraint(expr=-m.x64*m.x32*m.b100 + m.x303 >= 0)

m.c34 = Constraint(expr=-m.x65*m.x33*m.b101 + m.x304 >= 0)

m.c35 = Constraint(expr=-m.x65*m.x34*m.b102 + m.x305 >= 0)

m.c36 = Constraint(expr=-m.x65*m.x35*m.b103 + m.x306 >= 0)

m.c37 = Constraint(expr=-m.x65*m.x36*m.b104 + m.x307 >= 0)

m.c38 = Constraint(expr=-m.x66*m.x37*m.b105 + m.x308 >= 0)

m.c39 = Constraint(expr=-m.x66*m.x38*m.b106 + m.x309 >= 0)

m.c40 = Constraint(expr=-m.x66*m.x39*m.b107 + m.x310 >= 0)

m.c41 = Constraint(expr=-m.x66*m.x40*m.b108 + m.x311 >= 0)

m.c42 = Constraint(expr=-m.x67*m.x41*m.b109 + m.x312 >= 0)

m.c43 = Constraint(expr=-m.x67*m.x42*m.b110 + m.x313 >= 0)

m.c44 = Constraint(expr=-m.x67*m.x43*m.b111 + m.x314 >= 0)

m.c45 = Constraint(expr=-m.x67*m.x44*m.b112 + m.x315 >= 0)

m.c46 = Constraint(expr=(-40.4533333333333*m.x45*m.b113) - 40.4533333333333*m.b113*m.x45 + m.x316 >= 0)

m.c47 = Constraint(expr=(-40.4533333333333*m.x46*m.b114) - 40.4533333333333*m.b114*m.x46 + m.x317 >= 0)

m.c48 = Constraint(expr=(-40.4533333333333*m.x47*m.b115) - 40.4533333333333*m.b115*m.x47 + m.x318 >= 0)

m.c49 = Constraint(expr=(-40.4533333333333*m.x48*m.b116) - 40.4533333333333*m.b116*m.x48 + m.x319 >= 0)

m.c50 = Constraint(expr=(-13.0733333333333*m.x49*m.b117) - 13.0733333333333*m.b117*m.x49 + m.x320 >= 0)

m.c51 = Constraint(expr=(-13.0733333333333*m.x50*m.b118) - 13.0733333333333*m.b118*m.x50 + m.x321 >= 0)

m.c52 = Constraint(expr=(-13.0733333333333*m.x51*m.b119) - 13.0733333333333*m.b119*m.x51 + m.x322 >= 0)

m.c53 = Constraint(expr=(-13.0733333333333*m.x52*m.b120) - 13.0733333333333*m.b120*m.x52 + m.x323 >= 0)

m.c54 = Constraint(expr=(-19*m.x53*m.b121) - 19*m.b121*m.x53 + m.x324 >= 0)

m.c55 = Constraint(expr=(-19*m.x54*m.b122) - 19*m.b122*m.x54 + m.x325 >= 0)

m.c56 = Constraint(expr=(-19*m.x55*m.b123) - 19*m.b123*m.x55 + m.x326 >= 0)

m.c57 = Constraint(expr=(-19*m.x56*m.b124) - 19*m.b124*m.x56 + m.x327 >= 0)

m.c58 = Constraint(expr=-m.x68*m.x57*m.b125 + m.x328 >= 0)

m.c59 = Constraint(expr=-m.x68*m.x58*m.b126 + m.x329 >= 0)

m.c60 = Constraint(expr=-m.x68*m.x59*m.b127 + m.x330 >= 0)

m.c61 = Constraint(expr=-m.x68*m.x60*m.b128 + m.x331 >= 0)

m.c62 = Constraint(expr=   m.b69 + m.b70 + m.b71 + m.b72 == 1)

m.c63 = Constraint(expr=   m.b73 + m.b74 + m.b75 + m.b76 == 1)

m.c64 = Constraint(expr=   m.b77 + m.b78 + m.b79 + m.b80 == 1)

m.c65 = Constraint(expr=   m.b81 + m.b82 + m.b83 + m.b84 == 1)

m.c66 = Constraint(expr=   m.b85 + m.b86 + m.b87 + m.b88 == 1)

m.c67 = Constraint(expr=   m.b89 + m.b90 + m.b91 + m.b92 == 1)

m.c68 = Constraint(expr=   m.b93 + m.b94 + m.b95 + m.b96 == 1)

m.c69 = Constraint(expr=   m.b97 + m.b98 + m.b99 + m.b100 == 1)

m.c70 = Constraint(expr=   m.b101 + m.b102 + m.b103 + m.b104 == 1)

m.c71 = Constraint(expr=   m.b105 + m.b106 + m.b107 + m.b108 == 1)

m.c72 = Constraint(expr=   m.b109 + m.b110 + m.b111 + m.b112 == 1)

m.c73 = Constraint(expr=   m.b113 + m.b114 + m.b115 + m.b116 == 1)

m.c74 = Constraint(expr=   m.b117 + m.b118 + m.b119 + m.b120 == 1)

m.c75 = Constraint(expr=   m.b121 + m.b122 + m.b123 + m.b124 == 1)

m.c76 = Constraint(expr=   m.b125 + m.b126 + m.b127 + m.b128 == 1)

m.c77 = Constraint(expr=   2.02*m.b69 + 4.01333333333333*m.b73 + 4.76*m.b77 + 5.96*m.b81 + 42.0933333333333*m.b85
                         + 99.28*m.b89 + 6.59333333333333*m.b93 + 61.8666666666667*m.b97 + 56.2866666666667*m.b101
                         + 41.5*m.b105 + 62.4933333333333*m.b109 + 80.9066666666667*m.b113 + 26.1466666666667*m.b117
                         + 38*m.b121 + 62.24*m.b125 <= 153.54)

m.c78 = Constraint(expr=   2.02*m.b70 + 4.01333333333333*m.b74 + 4.76*m.b78 + 5.96*m.b82 + 42.0933333333333*m.b86
                         + 99.28*m.b90 + 6.59333333333333*m.b94 + 61.8666666666667*m.b98 + 56.2866666666667*m.b102
                         + 41.5*m.b106 + 62.4933333333333*m.b110 + 80.9066666666667*m.b114 + 26.1466666666667*m.b118
                         + 38*m.b122 + 62.24*m.b126 <= 153.54)

m.c79 = Constraint(expr=   2.02*m.b71 + 4.01333333333333*m.b75 + 4.76*m.b79 + 5.96*m.b83 + 42.0933333333333*m.b87
                         + 99.28*m.b91 + 6.59333333333333*m.b95 + 61.8666666666667*m.b99 + 56.2866666666667*m.b103
                         + 41.5*m.b107 + 62.4933333333333*m.b111 + 80.9066666666667*m.b115 + 26.1466666666667*m.b119
                         + 38*m.b123 + 62.24*m.b127 <= 153.54)

m.c80 = Constraint(expr=   2.02*m.b72 + 4.01333333333333*m.b76 + 4.76*m.b80 + 5.96*m.b84 + 42.0933333333333*m.b88
                         + 99.28*m.b92 + 6.59333333333333*m.b96 + 61.8666666666667*m.b100 + 56.2866666666667*m.b104
                         + 41.5*m.b108 + 62.4933333333333*m.b112 + 80.9066666666667*m.b116 + 26.1466666666667*m.b120
                         + 38*m.b124 + 62.24*m.b128 <= 153.54)

m.c81 = Constraint(expr=   m.x144 + m.x152 >= 0.29424122)

m.c82 = Constraint(expr=   m.x145 + m.x153 >= 0.29424122)

m.c83 = Constraint(expr=   m.x146 + m.x154 >= 0.29424122)

m.c84 = Constraint(expr=   m.x147 + m.x155 >= 0.29424122)

m.c85 = Constraint(expr=   m.x144 + m.x156 >= 0.29760193)

m.c86 = Constraint(expr=   m.x145 + m.x157 >= 0.29760193)

m.c87 = Constraint(expr=   m.x146 + m.x158 >= 0.29760193)

m.c88 = Constraint(expr=   m.x147 + m.x159 >= 0.29760193)

m.c89 = Constraint(expr=   m.x144 + m.x160 >= 0.35149534)

m.c90 = Constraint(expr=   m.x145 + m.x161 >= 0.35149534)

m.c91 = Constraint(expr=   m.x146 + m.x162 >= 0.35149534)

m.c92 = Constraint(expr=   m.x147 + m.x163 >= 0.35149534)

m.c93 = Constraint(expr=   m.x144 + m.x164 >= 0.30458283)

m.c94 = Constraint(expr=   m.x145 + m.x165 >= 0.30458283)

m.c95 = Constraint(expr=   m.x146 + m.x166 >= 0.30458283)

m.c96 = Constraint(expr=   m.x147 + m.x167 >= 0.30458283)

m.c97 = Constraint(expr=   m.x144 + m.x168 >= 0.29951066)

m.c98 = Constraint(expr=   m.x145 + m.x169 >= 0.29951066)

m.c99 = Constraint(expr=   m.x146 + m.x170 >= 0.29951066)

m.c100 = Constraint(expr=   m.x147 + m.x171 >= 0.29951066)

m.c101 = Constraint(expr=   m.x144 + m.x172 >= 0.30694357)

m.c102 = Constraint(expr=   m.x145 + m.x173 >= 0.30694357)

m.c103 = Constraint(expr=   m.x146 + m.x174 >= 0.30694357)

m.c104 = Constraint(expr=   m.x147 + m.x175 >= 0.30694357)

m.c105 = Constraint(expr=   m.x144 + m.x176 >= 0.33520661)

m.c106 = Constraint(expr=   m.x145 + m.x177 >= 0.33520661)

m.c107 = Constraint(expr=   m.x146 + m.x178 >= 0.33520661)

m.c108 = Constraint(expr=   m.x147 + m.x179 >= 0.33520661)

m.c109 = Constraint(expr=   m.x144 + m.x180 >= 0.3400071)

m.c110 = Constraint(expr=   m.x145 + m.x181 >= 0.3400071)

m.c111 = Constraint(expr=   m.x146 + m.x182 >= 0.3400071)

m.c112 = Constraint(expr=   m.x147 + m.x183 >= 0.3400071)

m.c113 = Constraint(expr=   m.x144 + m.x184 >= 0.35227087)

m.c114 = Constraint(expr=   m.x145 + m.x185 >= 0.35227087)

m.c115 = Constraint(expr=   m.x146 + m.x186 >= 0.35227087)

m.c116 = Constraint(expr=   m.x147 + m.x187 >= 0.35227087)

m.c117 = Constraint(expr=   m.x144 + m.x188 >= 0.34225726)

m.c118 = Constraint(expr=   m.x145 + m.x189 >= 0.34225726)

m.c119 = Constraint(expr=   m.x146 + m.x190 >= 0.34225726)

m.c120 = Constraint(expr=   m.x147 + m.x191 >= 0.34225726)

m.c121 = Constraint(expr=   m.x144 + m.x192 >= 0.32776566)

m.c122 = Constraint(expr=   m.x145 + m.x193 >= 0.32776566)

m.c123 = Constraint(expr=   m.x146 + m.x194 >= 0.32776566)

m.c124 = Constraint(expr=   m.x147 + m.x195 >= 0.32776566)

m.c125 = Constraint(expr=   m.x144 + m.x196 >= 0.30438256)

m.c126 = Constraint(expr=   m.x145 + m.x197 >= 0.30438256)

m.c127 = Constraint(expr=   m.x146 + m.x198 >= 0.30438256)

m.c128 = Constraint(expr=   m.x147 + m.x199 >= 0.30438256)

m.c129 = Constraint(expr=   m.x144 + m.x200 >= 0.28538336)

m.c130 = Constraint(expr=   m.x145 + m.x201 >= 0.28538336)

m.c131 = Constraint(expr=   m.x146 + m.x202 >= 0.28538336)

m.c132 = Constraint(expr=   m.x147 + m.x203 >= 0.28538336)

m.c133 = Constraint(expr=   m.x144 + m.x204 >= 0.27950575)

m.c134 = Constraint(expr=   m.x145 + m.x205 >= 0.27950575)

m.c135 = Constraint(expr=   m.x146 + m.x206 >= 0.27950575)

m.c136 = Constraint(expr=   m.x147 + m.x207 >= 0.27950575)

m.c137 = Constraint(expr= - m.x144 + m.x152 >= -0.29424122)

m.c138 = Constraint(expr= - m.x145 + m.x153 >= -0.29424122)

m.c139 = Constraint(expr= - m.x146 + m.x154 >= -0.29424122)

m.c140 = Constraint(expr= - m.x147 + m.x155 >= -0.29424122)

m.c141 = Constraint(expr= - m.x144 + m.x156 >= -0.29760193)

m.c142 = Constraint(expr= - m.x145 + m.x157 >= -0.29760193)

m.c143 = Constraint(expr= - m.x146 + m.x158 >= -0.29760193)

m.c144 = Constraint(expr= - m.x147 + m.x159 >= -0.29760193)

m.c145 = Constraint(expr= - m.x144 + m.x160 >= -0.35149534)

m.c146 = Constraint(expr= - m.x145 + m.x161 >= -0.35149534)

m.c147 = Constraint(expr= - m.x146 + m.x162 >= -0.35149534)

m.c148 = Constraint(expr= - m.x147 + m.x163 >= -0.35149534)

m.c149 = Constraint(expr= - m.x144 + m.x164 >= -0.30458283)

m.c150 = Constraint(expr= - m.x145 + m.x165 >= -0.30458283)

m.c151 = Constraint(expr= - m.x146 + m.x166 >= -0.30458283)

m.c152 = Constraint(expr= - m.x147 + m.x167 >= -0.30458283)

m.c153 = Constraint(expr= - m.x144 + m.x168 >= -0.29951066)

m.c154 = Constraint(expr= - m.x145 + m.x169 >= -0.29951066)

m.c155 = Constraint(expr= - m.x146 + m.x170 >= -0.29951066)

m.c156 = Constraint(expr= - m.x147 + m.x171 >= -0.29951066)

m.c157 = Constraint(expr= - m.x144 + m.x172 >= -0.30694357)

m.c158 = Constraint(expr= - m.x145 + m.x173 >= -0.30694357)

m.c159 = Constraint(expr= - m.x146 + m.x174 >= -0.30694357)

m.c160 = Constraint(expr= - m.x147 + m.x175 >= -0.30694357)

m.c161 = Constraint(expr= - m.x144 + m.x176 >= -0.33520661)

m.c162 = Constraint(expr= - m.x145 + m.x177 >= -0.33520661)

m.c163 = Constraint(expr= - m.x146 + m.x178 >= -0.33520661)

m.c164 = Constraint(expr= - m.x147 + m.x179 >= -0.33520661)

m.c165 = Constraint(expr= - m.x144 + m.x180 >= -0.3400071)

m.c166 = Constraint(expr= - m.x145 + m.x181 >= -0.3400071)

m.c167 = Constraint(expr= - m.x146 + m.x182 >= -0.3400071)

m.c168 = Constraint(expr= - m.x147 + m.x183 >= -0.3400071)

m.c169 = Constraint(expr= - m.x144 + m.x188 >= -0.34225726)

m.c170 = Constraint(expr= - m.x145 + m.x189 >= -0.34225726)

m.c171 = Constraint(expr= - m.x146 + m.x190 >= -0.34225726)

m.c172 = Constraint(expr= - m.x147 + m.x191 >= -0.34225726)

m.c173 = Constraint(expr= - m.x144 + m.x192 >= -0.32776566)

m.c174 = Constraint(expr= - m.x145 + m.x193 >= -0.32776566)

m.c175 = Constraint(expr= - m.x146 + m.x194 >= -0.32776566)

m.c176 = Constraint(expr= - m.x147 + m.x195 >= -0.32776566)

m.c177 = Constraint(expr= - m.x144 + m.x196 >= -0.30438256)

m.c178 = Constraint(expr= - m.x145 + m.x197 >= -0.30438256)

m.c179 = Constraint(expr= - m.x146 + m.x198 >= -0.30438256)

m.c180 = Constraint(expr= - m.x147 + m.x199 >= -0.30438256)

m.c181 = Constraint(expr= - m.x144 + m.x200 >= -0.28538336)

m.c182 = Constraint(expr= - m.x145 + m.x201 >= -0.28538336)

m.c183 = Constraint(expr= - m.x146 + m.x202 >= -0.28538336)

m.c184 = Constraint(expr= - m.x147 + m.x203 >= -0.28538336)

m.c185 = Constraint(expr= - m.x144 + m.x204 >= -0.27950575)

m.c186 = Constraint(expr= - m.x145 + m.x205 >= -0.27950575)

m.c187 = Constraint(expr= - m.x146 + m.x206 >= -0.27950575)

m.c188 = Constraint(expr= - m.x147 + m.x207 >= -0.27950575)

m.c189 = Constraint(expr= - m.x144 + m.x208 >= -0.25788969)

m.c190 = Constraint(expr= - m.x145 + m.x209 >= -0.25788969)

m.c191 = Constraint(expr= - m.x146 + m.x210 >= -0.25788969)

m.c192 = Constraint(expr= - m.x147 + m.x211 >= -0.25788969)

m.c193 = Constraint(expr=   m.x148 + m.x216 >= -0.9536939)

m.c194 = Constraint(expr=   m.x149 + m.x217 >= -0.9536939)

m.c195 = Constraint(expr=   m.x150 + m.x218 >= -0.9536939)

m.c196 = Constraint(expr=   m.x151 + m.x219 >= -0.9536939)

m.c197 = Constraint(expr=   m.x148 + m.x220 >= -0.9004898)

m.c198 = Constraint(expr=   m.x149 + m.x221 >= -0.9004898)

m.c199 = Constraint(expr=   m.x150 + m.x222 >= -0.9004898)

m.c200 = Constraint(expr=   m.x151 + m.x223 >= -0.9004898)

m.c201 = Constraint(expr=   m.x148 + m.x224 >= -0.9114032)

m.c202 = Constraint(expr=   m.x149 + m.x225 >= -0.9114032)

m.c203 = Constraint(expr=   m.x150 + m.x226 >= -0.9114032)

m.c204 = Constraint(expr=   m.x151 + m.x227 >= -0.9114032)

m.c205 = Constraint(expr=   m.x148 + m.x228 >= -0.90071532)

m.c206 = Constraint(expr=   m.x149 + m.x229 >= -0.90071532)

m.c207 = Constraint(expr=   m.x150 + m.x230 >= -0.90071532)

m.c208 = Constraint(expr=   m.x151 + m.x231 >= -0.90071532)

m.c209 = Constraint(expr=   m.x148 + m.x232 >= -0.88043054)

m.c210 = Constraint(expr=   m.x149 + m.x233 >= -0.88043054)

m.c211 = Constraint(expr=   m.x150 + m.x234 >= -0.88043054)

m.c212 = Constraint(expr=   m.x151 + m.x235 >= -0.88043054)

m.c213 = Constraint(expr=   m.x148 + m.x236 >= -0.8680249)

m.c214 = Constraint(expr=   m.x149 + m.x237 >= -0.8680249)

m.c215 = Constraint(expr=   m.x150 + m.x238 >= -0.8680249)

m.c216 = Constraint(expr=   m.x151 + m.x239 >= -0.8680249)

m.c217 = Constraint(expr=   m.x148 + m.x240 >= -0.81034814)

m.c218 = Constraint(expr=   m.x149 + m.x241 >= -0.81034814)

m.c219 = Constraint(expr=   m.x150 + m.x242 >= -0.81034814)

m.c220 = Constraint(expr=   m.x151 + m.x243 >= -0.81034814)

m.c221 = Constraint(expr=   m.x148 + m.x244 >= -0.80843127)

m.c222 = Constraint(expr=   m.x149 + m.x245 >= -0.80843127)

m.c223 = Constraint(expr=   m.x150 + m.x246 >= -0.80843127)

m.c224 = Constraint(expr=   m.x151 + m.x247 >= -0.80843127)

m.c225 = Constraint(expr=   m.x148 + m.x248 >= -0.7794471)

m.c226 = Constraint(expr=   m.x149 + m.x249 >= -0.7794471)

m.c227 = Constraint(expr=   m.x150 + m.x250 >= -0.7794471)

m.c228 = Constraint(expr=   m.x151 + m.x251 >= -0.7794471)

m.c229 = Constraint(expr=   m.x148 + m.x252 >= -0.79930922)

m.c230 = Constraint(expr=   m.x149 + m.x253 >= -0.79930922)

m.c231 = Constraint(expr=   m.x150 + m.x254 >= -0.79930922)

m.c232 = Constraint(expr=   m.x151 + m.x255 >= -0.79930922)

m.c233 = Constraint(expr=   m.x148 + m.x256 >= -0.84280733)

m.c234 = Constraint(expr=   m.x149 + m.x257 >= -0.84280733)

m.c235 = Constraint(expr=   m.x150 + m.x258 >= -0.84280733)

m.c236 = Constraint(expr=   m.x151 + m.x259 >= -0.84280733)

m.c237 = Constraint(expr=   m.x148 + m.x260 >= -0.81379236)

m.c238 = Constraint(expr=   m.x149 + m.x261 >= -0.81379236)

m.c239 = Constraint(expr=   m.x150 + m.x262 >= -0.81379236)

m.c240 = Constraint(expr=   m.x151 + m.x263 >= -0.81379236)

m.c241 = Constraint(expr=   m.x148 + m.x264 >= -0.82457178)

m.c242 = Constraint(expr=   m.x149 + m.x265 >= -0.82457178)

m.c243 = Constraint(expr=   m.x150 + m.x266 >= -0.82457178)

m.c244 = Constraint(expr=   m.x151 + m.x267 >= -0.82457178)

m.c245 = Constraint(expr=   m.x148 + m.x268 >= -0.80226439)

m.c246 = Constraint(expr=   m.x149 + m.x269 >= -0.80226439)

m.c247 = Constraint(expr=   m.x150 + m.x270 >= -0.80226439)

m.c248 = Constraint(expr=   m.x151 + m.x271 >= -0.80226439)

m.c249 = Constraint(expr= - m.x148 + m.x212 >= 0.98493628)

m.c250 = Constraint(expr= - m.x149 + m.x213 >= 0.98493628)

m.c251 = Constraint(expr= - m.x150 + m.x214 >= 0.98493628)

m.c252 = Constraint(expr= - m.x151 + m.x215 >= 0.98493628)

m.c253 = Constraint(expr= - m.x148 + m.x216 >= 0.9536939)

m.c254 = Constraint(expr= - m.x149 + m.x217 >= 0.9536939)

m.c255 = Constraint(expr= - m.x150 + m.x218 >= 0.9536939)

m.c256 = Constraint(expr= - m.x151 + m.x219 >= 0.9536939)

m.c257 = Constraint(expr= - m.x148 + m.x220 >= 0.9004898)

m.c258 = Constraint(expr= - m.x149 + m.x221 >= 0.9004898)

m.c259 = Constraint(expr= - m.x150 + m.x222 >= 0.9004898)

m.c260 = Constraint(expr= - m.x151 + m.x223 >= 0.9004898)

m.c261 = Constraint(expr= - m.x148 + m.x224 >= 0.9114032)

m.c262 = Constraint(expr= - m.x149 + m.x225 >= 0.9114032)

m.c263 = Constraint(expr= - m.x150 + m.x226 >= 0.9114032)

m.c264 = Constraint(expr= - m.x151 + m.x227 >= 0.9114032)

m.c265 = Constraint(expr= - m.x148 + m.x228 >= 0.90071532)

m.c266 = Constraint(expr= - m.x149 + m.x229 >= 0.90071532)

m.c267 = Constraint(expr= - m.x150 + m.x230 >= 0.90071532)

m.c268 = Constraint(expr= - m.x151 + m.x231 >= 0.90071532)

m.c269 = Constraint(expr= - m.x148 + m.x232 >= 0.88043054)

m.c270 = Constraint(expr= - m.x149 + m.x233 >= 0.88043054)

m.c271 = Constraint(expr= - m.x150 + m.x234 >= 0.88043054)

m.c272 = Constraint(expr= - m.x151 + m.x235 >= 0.88043054)

m.c273 = Constraint(expr= - m.x148 + m.x236 >= 0.8680249)

m.c274 = Constraint(expr= - m.x149 + m.x237 >= 0.8680249)

m.c275 = Constraint(expr= - m.x150 + m.x238 >= 0.8680249)

m.c276 = Constraint(expr= - m.x151 + m.x239 >= 0.8680249)

m.c277 = Constraint(expr= - m.x148 + m.x240 >= 0.81034814)

m.c278 = Constraint(expr= - m.x149 + m.x241 >= 0.81034814)

m.c279 = Constraint(expr= - m.x150 + m.x242 >= 0.81034814)

m.c280 = Constraint(expr= - m.x151 + m.x243 >= 0.81034814)

m.c281 = Constraint(expr= - m.x148 + m.x244 >= 0.80843127)

m.c282 = Constraint(expr= - m.x149 + m.x245 >= 0.80843127)

m.c283 = Constraint(expr= - m.x150 + m.x246 >= 0.80843127)

m.c284 = Constraint(expr= - m.x151 + m.x247 >= 0.80843127)

m.c285 = Constraint(expr= - m.x148 + m.x252 >= 0.79930922)

m.c286 = Constraint(expr= - m.x149 + m.x253 >= 0.79930922)

m.c287 = Constraint(expr= - m.x150 + m.x254 >= 0.79930922)

m.c288 = Constraint(expr= - m.x151 + m.x255 >= 0.79930922)

m.c289 = Constraint(expr= - m.x148 + m.x256 >= 0.84280733)

m.c290 = Constraint(expr= - m.x149 + m.x257 >= 0.84280733)

m.c291 = Constraint(expr= - m.x150 + m.x258 >= 0.84280733)

m.c292 = Constraint(expr= - m.x151 + m.x259 >= 0.84280733)

m.c293 = Constraint(expr= - m.x148 + m.x260 >= 0.81379236)

m.c294 = Constraint(expr= - m.x149 + m.x261 >= 0.81379236)

m.c295 = Constraint(expr= - m.x150 + m.x262 >= 0.81379236)

m.c296 = Constraint(expr= - m.x151 + m.x263 >= 0.81379236)

m.c297 = Constraint(expr= - m.x148 + m.x264 >= 0.82457178)

m.c298 = Constraint(expr= - m.x149 + m.x265 >= 0.82457178)

m.c299 = Constraint(expr= - m.x150 + m.x266 >= 0.82457178)

m.c300 = Constraint(expr= - m.x151 + m.x267 >= 0.82457178)

m.c301 = Constraint(expr= - m.x148 + m.x268 >= 0.80226439)

m.c302 = Constraint(expr= - m.x149 + m.x269 >= 0.80226439)

m.c303 = Constraint(expr= - m.x150 + m.x270 >= 0.80226439)

m.c304 = Constraint(expr= - m.x151 + m.x271 >= 0.80226439)

m.c305 = Constraint(expr=   m.x1 - m.x152 - m.x212 == 0)

m.c306 = Constraint(expr=   m.x2 - m.x153 - m.x213 == 0)

m.c307 = Constraint(expr=   m.x3 - m.x154 - m.x214 == 0)

m.c308 = Constraint(expr=   m.x4 - m.x155 - m.x215 == 0)

m.c309 = Constraint(expr=   m.x5 - m.x156 - m.x216 == 0)

m.c310 = Constraint(expr=   m.x6 - m.x157 - m.x217 == 0)

m.c311 = Constraint(expr=   m.x7 - m.x158 - m.x218 == 0)

m.c312 = Constraint(expr=   m.x8 - m.x159 - m.x219 == 0)

m.c313 = Constraint(expr=   m.x9 - m.x160 - m.x220 == 0)

m.c314 = Constraint(expr=   m.x10 - m.x161 - m.x221 == 0)

m.c315 = Constraint(expr=   m.x11 - m.x162 - m.x222 == 0)

m.c316 = Constraint(expr=   m.x12 - m.x163 - m.x223 == 0)

m.c317 = Constraint(expr=   m.x13 - m.x164 - m.x224 == 0)

m.c318 = Constraint(expr=   m.x14 - m.x165 - m.x225 == 0)

m.c319 = Constraint(expr=   m.x15 - m.x166 - m.x226 == 0)

m.c320 = Constraint(expr=   m.x16 - m.x167 - m.x227 == 0)

m.c321 = Constraint(expr=   m.x17 - m.x168 - m.x228 == 0)

m.c322 = Constraint(expr=   m.x18 - m.x169 - m.x229 == 0)

m.c323 = Constraint(expr=   m.x19 - m.x170 - m.x230 == 0)

m.c324 = Constraint(expr=   m.x20 - m.x171 - m.x231 == 0)

m.c325 = Constraint(expr=   m.x21 - m.x172 - m.x232 == 0)

m.c326 = Constraint(expr=   m.x22 - m.x173 - m.x233 == 0)

m.c327 = Constraint(expr=   m.x23 - m.x174 - m.x234 == 0)

m.c328 = Constraint(expr=   m.x24 - m.x175 - m.x235 == 0)

m.c329 = Constraint(expr=   m.x25 - m.x176 - m.x236 == 0)

m.c330 = Constraint(expr=   m.x26 - m.x177 - m.x237 == 0)

m.c331 = Constraint(expr=   m.x27 - m.x178 - m.x238 == 0)

m.c332 = Constraint(expr=   m.x28 - m.x179 - m.x239 == 0)

m.c333 = Constraint(expr=   m.x29 - m.x180 - m.x240 == 0)

m.c334 = Constraint(expr=   m.x30 - m.x181 - m.x241 == 0)

m.c335 = Constraint(expr=   m.x31 - m.x182 - m.x242 == 0)

m.c336 = Constraint(expr=   m.x32 - m.x183 - m.x243 == 0)

m.c337 = Constraint(expr=   m.x33 - m.x184 - m.x244 == 0)

m.c338 = Constraint(expr=   m.x34 - m.x185 - m.x245 == 0)

m.c339 = Constraint(expr=   m.x35 - m.x186 - m.x246 == 0)

m.c340 = Constraint(expr=   m.x36 - m.x187 - m.x247 == 0)

m.c341 = Constraint(expr=   m.x37 - m.x188 - m.x248 == 0)

m.c342 = Constraint(expr=   m.x38 - m.x189 - m.x249 == 0)

m.c343 = Constraint(expr=   m.x39 - m.x190 - m.x250 == 0)

m.c344 = Constraint(expr=   m.x40 - m.x191 - m.x251 == 0)

m.c345 = Constraint(expr=   m.x41 - m.x192 - m.x252 == 0)

m.c346 = Constraint(expr=   m.x42 - m.x193 - m.x253 == 0)

m.c347 = Constraint(expr=   m.x43 - m.x194 - m.x254 == 0)

m.c348 = Constraint(expr=   m.x44 - m.x195 - m.x255 == 0)

m.c349 = Constraint(expr=   m.x45 - m.x196 - m.x256 == 0)

m.c350 = Constraint(expr=   m.x46 - m.x197 - m.x257 == 0)

m.c351 = Constraint(expr=   m.x47 - m.x198 - m.x258 == 0)

m.c352 = Constraint(expr=   m.x48 - m.x199 - m.x259 == 0)

m.c353 = Constraint(expr=   m.x49 - m.x200 - m.x260 == 0)

m.c354 = Constraint(expr=   m.x50 - m.x201 - m.x261 == 0)

m.c355 = Constraint(expr=   m.x51 - m.x202 - m.x262 == 0)

m.c356 = Constraint(expr=   m.x52 - m.x203 - m.x263 == 0)

m.c357 = Constraint(expr=   m.x53 - m.x204 - m.x264 == 0)

m.c358 = Constraint(expr=   m.x54 - m.x205 - m.x265 == 0)

m.c359 = Constraint(expr=   m.x55 - m.x206 - m.x266 == 0)

m.c360 = Constraint(expr=   m.x56 - m.x207 - m.x267 == 0)

m.c361 = Constraint(expr=   m.x57 - m.x208 - m.x268 == 0)

m.c362 = Constraint(expr=   m.x58 - m.x209 - m.x269 == 0)

m.c363 = Constraint(expr=   m.x59 - m.x210 - m.x270 == 0)

m.c364 = Constraint(expr=   m.x60 - m.x211 - m.x271 == 0)

m.c365 = Constraint(expr=   m.b333 + m.b334 >= 1)

m.c366 = Constraint(expr=   m.b332 + m.b334 >= 1)

m.c367 = Constraint(expr=   m.b332 + m.b333 >= 1)

m.c368 = Constraint(expr=   m.b334 + m.b336 >= 1)

m.c369 = Constraint(expr=   m.b334 + m.b335 >= 1)

m.c370 = Constraint(expr=   m.b333 + m.b336 >= 1)

m.c371 = Constraint(expr=   m.b333 + m.b335 >= 1)

m.c372 = Constraint(expr=   m.b332 + m.b336 >= 1)

m.c373 = Constraint(expr=   m.b332 + m.b335 >= 1)

m.c374 = Constraint(expr=   m.x61 - 5.96*m.b332 >= 0)

m.c375 = Constraint(expr=   m.x62 - 42.0933333333333*m.b333 >= 0)

m.c376 = Constraint(expr=   m.x63 - 99.28*m.b334 >= 0)

m.c377 = Constraint(expr=   m.x64 - 61.8666666666667*m.b335 >= 0)

m.c378 = Constraint(expr=   m.x65 - 56.2866666666667*m.b336 >= 0)

m.c379 = Constraint(expr=   m.x66 - 39.6133333333333*m.b337 >= 0)

m.c380 = Constraint(expr=   m.x66 - 41.5*m.b338 >= 0)

m.c381 = Constraint(expr=   m.x67 - 62.4933333333333*m.b339 >= 0)

m.c382 = Constraint(expr=   m.x68 - 62.24*m.b340 >= 0)

m.c383 = Constraint(expr= - m.x129 + m.x272 <= 0)

m.c384 = Constraint(expr= - m.x129 + m.x273 <= 0)

m.c385 = Constraint(expr= - m.x129 + m.x274 <= 0)

m.c386 = Constraint(expr= - m.x129 + m.x275 <= 0)

m.c387 = Constraint(expr= - m.x130 + m.x276 <= 0)

m.c388 = Constraint(expr= - m.x130 + m.x277 <= 0)

m.c389 = Constraint(expr= - m.x130 + m.x278 <= 0)

m.c390 = Constraint(expr= - m.x130 + m.x279 <= 0)

m.c391 = Constraint(expr= - m.x131 + m.x280 <= 0)

m.c392 = Constraint(expr= - m.x131 + m.x281 <= 0)

m.c393 = Constraint(expr= - m.x131 + m.x282 <= 0)

m.c394 = Constraint(expr= - m.x131 + m.x283 <= 0)

m.c395 = Constraint(expr= - m.x132 + m.x284 <= 0)

m.c396 = Constraint(expr= - m.x132 + m.x285 <= 0)

m.c397 = Constraint(expr= - m.x132 + m.x286 <= 0)

m.c398 = Constraint(expr= - m.x132 + m.x287 <= 0)

m.c399 = Constraint(expr= - m.x133 + m.x288 <= 0)

m.c400 = Constraint(expr= - m.x133 + m.x289 <= 0)

m.c401 = Constraint(expr= - m.x133 + m.x290 <= 0)

m.c402 = Constraint(expr= - m.x133 + m.x291 <= 0)

m.c403 = Constraint(expr= - m.x134 + m.x292 <= 0)

m.c404 = Constraint(expr= - m.x134 + m.x293 <= 0)

m.c405 = Constraint(expr= - m.x134 + m.x294 <= 0)

m.c406 = Constraint(expr= - m.x134 + m.x295 <= 0)

m.c407 = Constraint(expr= - m.x135 + m.x296 <= 0)

m.c408 = Constraint(expr= - m.x135 + m.x297 <= 0)

m.c409 = Constraint(expr= - m.x135 + m.x298 <= 0)

m.c410 = Constraint(expr= - m.x135 + m.x299 <= 0)

m.c411 = Constraint(expr= - m.x136 + m.x300 <= 0)

m.c412 = Constraint(expr= - m.x136 + m.x301 <= 0)

m.c413 = Constraint(expr= - m.x136 + m.x302 <= 0)

m.c414 = Constraint(expr= - m.x136 + m.x303 <= 0)

m.c415 = Constraint(expr= - m.x137 + m.x304 <= 0)

m.c416 = Constraint(expr= - m.x137 + m.x305 <= 0)

m.c417 = Constraint(expr= - m.x137 + m.x306 <= 0)

m.c418 = Constraint(expr= - m.x137 + m.x307 <= 0)

m.c419 = Constraint(expr= - m.x138 + m.x308 <= 0)

m.c420 = Constraint(expr= - m.x138 + m.x309 <= 0)

m.c421 = Constraint(expr= - m.x138 + m.x310 <= 0)

m.c422 = Constraint(expr= - m.x138 + m.x311 <= 0)

m.c423 = Constraint(expr= - m.x139 + m.x312 <= 0)

m.c424 = Constraint(expr= - m.x139 + m.x313 <= 0)

m.c425 = Constraint(expr= - m.x139 + m.x314 <= 0)

m.c426 = Constraint(expr= - m.x139 + m.x315 <= 0)

m.c427 = Constraint(expr= - m.x140 + m.x316 <= 0)

m.c428 = Constraint(expr= - m.x140 + m.x317 <= 0)

m.c429 = Constraint(expr= - m.x140 + m.x318 <= 0)

m.c430 = Constraint(expr= - m.x140 + m.x319 <= 0)

m.c431 = Constraint(expr= - m.x141 + m.x320 <= 0)

m.c432 = Constraint(expr= - m.x141 + m.x321 <= 0)

m.c433 = Constraint(expr= - m.x141 + m.x322 <= 0)

m.c434 = Constraint(expr= - m.x141 + m.x323 <= 0)

m.c435 = Constraint(expr= - m.x142 + m.x324 <= 0)

m.c436 = Constraint(expr= - m.x142 + m.x325 <= 0)

m.c437 = Constraint(expr= - m.x142 + m.x326 <= 0)

m.c438 = Constraint(expr= - m.x142 + m.x327 <= 0)

m.c439 = Constraint(expr= - m.x143 + m.x328 <= 0)

m.c440 = Constraint(expr= - m.x143 + m.x329 <= 0)

m.c441 = Constraint(expr= - m.x143 + m.x330 <= 0)

m.c442 = Constraint(expr= - m.x143 + m.x331 <= 0)

m.c443 = Constraint(expr=   m.b337 - m.b338 >= 0)

m.c444 = Constraint(expr=   m.x148 - m.x149 >= 0)

m.c445 = Constraint(expr=   m.x149 - m.x150 >= 0)

m.c446 = Constraint(expr=   m.x150 - m.x151 >= 0)
