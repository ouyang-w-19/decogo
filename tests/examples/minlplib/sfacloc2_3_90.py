#  MINLP written by GAMS Convert at 04/21/18 13:54:11
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        497       61      388       48        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        292      217       75        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1283     1148      135        0
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
m.x46 = Var(within=Reals,bounds=(1.92,2.02),initialize=1.92)
m.x47 = Var(within=Reals,bounds=(3.82,4.01333333333333),initialize=3.82)
m.x48 = Var(within=Reals,bounds=(4.53333333333333,4.76),initialize=4.53333333333333)
m.x49 = Var(within=Reals,bounds=(5.39333333333333,5.96),initialize=5.39333333333333)
m.x50 = Var(within=Reals,bounds=(36.3533333333333,42.0933333333333),initialize=36.3533333333333)
m.x51 = Var(within=Reals,bounds=(85.7466666666667,99.28),initialize=85.7466666666667)
m.x52 = Var(within=Reals,bounds=(6.28,6.59333333333333),initialize=6.28)
m.x53 = Var(within=Reals,bounds=(53.4333333333333,61.8666666666667),initialize=53.4333333333333)
m.x54 = Var(within=Reals,bounds=(48.6133333333333,56.2866666666667),initialize=48.6133333333333)
m.x55 = Var(within=Reals,bounds=(33.9533333333333,41.5),initialize=33.9533333333333)
m.x56 = Var(within=Reals,bounds=(53.9666666666667,62.4933333333333),initialize=53.9666666666667)
m.x57 = Var(within=Reals,bounds=(77.0533333333333,80.9066666666667),initialize=77.0533333333333)
m.x58 = Var(within=Reals,bounds=(24.9066666666667,26.1466666666667),initialize=24.9066666666667)
m.x59 = Var(within=Reals,bounds=(36.1866666666667,38),initialize=36.1866666666667)
m.x60 = Var(within=Reals,bounds=(56.3133333333333,62.24),initialize=56.3133333333333)
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
m.b99 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b100 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b101 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b102 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b103 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b104 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b105 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x218 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x235 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x255 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x258 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.b262 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b263 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b264 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b265 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b266 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b267 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b268 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b269 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b270 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b271 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b272 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b273 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b274 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b275 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b276 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b277 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b278 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b279 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b280 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b281 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b282 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b283 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b284 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b285 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b286 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b287 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b288 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b289 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b290 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b291 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   m.x106 + m.x107 + m.x108 + m.x109 + m.x110 + m.x111 + m.x112 + m.x113 + m.x114 + m.x115
                        + m.x116 + m.x117 + m.x118 + m.x119 + m.x120, sense=minimize)

m.c2 = Constraint(expr=-m.x46*m.x1*m.b61 + m.x217 >= 0)

m.c3 = Constraint(expr=-m.x46*m.x2*m.b62 + m.x218 >= 0)

m.c4 = Constraint(expr=-m.x46*m.x3*m.b63 + m.x219 >= 0)

m.c5 = Constraint(expr=-m.x47*m.x4*m.b64 + m.x220 >= 0)

m.c6 = Constraint(expr=-m.x47*m.x5*m.b65 + m.x221 >= 0)

m.c7 = Constraint(expr=-m.x47*m.x6*m.b66 + m.x222 >= 0)

m.c8 = Constraint(expr=-m.x48*m.x7*m.b67 + m.x223 >= 0)

m.c9 = Constraint(expr=-m.x48*m.x8*m.b68 + m.x224 >= 0)

m.c10 = Constraint(expr=-m.x48*m.x9*m.b69 + m.x225 >= 0)

m.c11 = Constraint(expr=-m.x49*m.x10*m.b70 + m.x226 >= 0)

m.c12 = Constraint(expr=-m.x49*m.x11*m.b71 + m.x227 >= 0)

m.c13 = Constraint(expr=-m.x49*m.x12*m.b72 + m.x228 >= 0)

m.c14 = Constraint(expr=-m.x50*m.x13*m.b73 + m.x229 >= 0)

m.c15 = Constraint(expr=-m.x50*m.x14*m.b74 + m.x230 >= 0)

m.c16 = Constraint(expr=-m.x50*m.x15*m.b75 + m.x231 >= 0)

m.c17 = Constraint(expr=-m.x51*m.x16*m.b76 + m.x232 >= 0)

m.c18 = Constraint(expr=-m.x51*m.x17*m.b77 + m.x233 >= 0)

m.c19 = Constraint(expr=-m.x51*m.x18*m.b78 + m.x234 >= 0)

m.c20 = Constraint(expr=-m.x52*m.x19*m.b79 + m.x235 >= 0)

m.c21 = Constraint(expr=-m.x52*m.x20*m.b80 + m.x236 >= 0)

m.c22 = Constraint(expr=-m.x52*m.x21*m.b81 + m.x237 >= 0)

m.c23 = Constraint(expr=-m.x53*m.x22*m.b82 + m.x238 >= 0)

m.c24 = Constraint(expr=-m.x53*m.x23*m.b83 + m.x239 >= 0)

m.c25 = Constraint(expr=-m.x53*m.x24*m.b84 + m.x240 >= 0)

m.c26 = Constraint(expr=-m.x54*m.x25*m.b85 + m.x241 >= 0)

m.c27 = Constraint(expr=-m.x54*m.x26*m.b86 + m.x242 >= 0)

m.c28 = Constraint(expr=-m.x54*m.x27*m.b87 + m.x243 >= 0)

m.c29 = Constraint(expr=-m.x55*m.x28*m.b88 + m.x244 >= 0)

m.c30 = Constraint(expr=-m.x55*m.x29*m.b89 + m.x245 >= 0)

m.c31 = Constraint(expr=-m.x55*m.x30*m.b90 + m.x246 >= 0)

m.c32 = Constraint(expr=-m.x56*m.x31*m.b91 + m.x247 >= 0)

m.c33 = Constraint(expr=-m.x56*m.x32*m.b92 + m.x248 >= 0)

m.c34 = Constraint(expr=-m.x56*m.x33*m.b93 + m.x249 >= 0)

m.c35 = Constraint(expr=-m.x57*m.x34*m.b94 + m.x250 >= 0)

m.c36 = Constraint(expr=-m.x57*m.x35*m.b95 + m.x251 >= 0)

m.c37 = Constraint(expr=-m.x57*m.x36*m.b96 + m.x252 >= 0)

m.c38 = Constraint(expr=-m.x58*m.x37*m.b97 + m.x253 >= 0)

m.c39 = Constraint(expr=-m.x58*m.x38*m.b98 + m.x254 >= 0)

m.c40 = Constraint(expr=-m.x58*m.x39*m.b99 + m.x255 >= 0)

m.c41 = Constraint(expr=-m.x59*m.x40*m.b100 + m.x256 >= 0)

m.c42 = Constraint(expr=-m.x59*m.x41*m.b101 + m.x257 >= 0)

m.c43 = Constraint(expr=-m.x59*m.x42*m.b102 + m.x258 >= 0)

m.c44 = Constraint(expr=-m.x60*m.x43*m.b103 + m.x259 >= 0)

m.c45 = Constraint(expr=-m.x60*m.x44*m.b104 + m.x260 >= 0)

m.c46 = Constraint(expr=-m.x60*m.x45*m.b105 + m.x261 >= 0)

m.c47 = Constraint(expr=   m.b61 + m.b62 + m.b63 == 1)

m.c48 = Constraint(expr=   m.b64 + m.b65 + m.b66 == 1)

m.c49 = Constraint(expr=   m.b67 + m.b68 + m.b69 == 1)

m.c50 = Constraint(expr=   m.b70 + m.b71 + m.b72 == 1)

m.c51 = Constraint(expr=   m.b73 + m.b74 + m.b75 == 1)

m.c52 = Constraint(expr=   m.b76 + m.b77 + m.b78 == 1)

m.c53 = Constraint(expr=   m.b79 + m.b80 + m.b81 == 1)

m.c54 = Constraint(expr=   m.b82 + m.b83 + m.b84 == 1)

m.c55 = Constraint(expr=   m.b85 + m.b86 + m.b87 == 1)

m.c56 = Constraint(expr=   m.b88 + m.b89 + m.b90 == 1)

m.c57 = Constraint(expr=   m.b91 + m.b92 + m.b93 == 1)

m.c58 = Constraint(expr=   m.b94 + m.b95 + m.b96 == 1)

m.c59 = Constraint(expr=   m.b97 + m.b98 + m.b99 == 1)

m.c60 = Constraint(expr=   m.b100 + m.b101 + m.b102 == 1)

m.c61 = Constraint(expr=   m.b103 + m.b104 + m.b105 == 1)

m.c62 = Constraint(expr=   2.02*m.b61 + 4.01333333333333*m.b64 + 4.76*m.b67 + 5.96*m.b70 + 42.0933333333333*m.b73
                         + 99.28*m.b76 + 6.59333333333333*m.b79 + 61.8666666666667*m.b82 + 56.2866666666667*m.b85
                         + 41.5*m.b88 + 62.4933333333333*m.b91 + 80.9066666666667*m.b94 + 26.1466666666667*m.b97
                         + 38*m.b100 + 62.24*m.b103 <= 213.053333333333)

m.c63 = Constraint(expr=   2.02*m.b62 + 4.01333333333333*m.b65 + 4.76*m.b68 + 5.96*m.b71 + 42.0933333333333*m.b74
                         + 99.28*m.b77 + 6.59333333333333*m.b80 + 61.8666666666667*m.b83 + 56.2866666666667*m.b86
                         + 41.5*m.b89 + 62.4933333333333*m.b92 + 80.9066666666667*m.b95 + 26.1466666666667*m.b98
                         + 38*m.b101 + 62.24*m.b104 <= 213.053333333333)

m.c64 = Constraint(expr=   2.02*m.b63 + 4.01333333333333*m.b66 + 4.76*m.b69 + 5.96*m.b72 + 42.0933333333333*m.b75
                         + 99.28*m.b78 + 6.59333333333333*m.b81 + 61.8666666666667*m.b84 + 56.2866666666667*m.b87
                         + 41.5*m.b90 + 62.4933333333333*m.b93 + 80.9066666666667*m.b96 + 26.1466666666667*m.b99
                         + 38*m.b102 + 62.24*m.b105 <= 213.053333333333)

m.c65 = Constraint(expr=   m.x121 + m.x127 >= 0.29424122)

m.c66 = Constraint(expr=   m.x122 + m.x128 >= 0.29424122)

m.c67 = Constraint(expr=   m.x123 + m.x129 >= 0.29424122)

m.c68 = Constraint(expr=   m.x121 + m.x130 >= 0.29760193)

m.c69 = Constraint(expr=   m.x122 + m.x131 >= 0.29760193)

m.c70 = Constraint(expr=   m.x123 + m.x132 >= 0.29760193)

m.c71 = Constraint(expr=   m.x121 + m.x133 >= 0.35149534)

m.c72 = Constraint(expr=   m.x122 + m.x134 >= 0.35149534)

m.c73 = Constraint(expr=   m.x123 + m.x135 >= 0.35149534)

m.c74 = Constraint(expr=   m.x121 + m.x136 >= 0.30458283)

m.c75 = Constraint(expr=   m.x122 + m.x137 >= 0.30458283)

m.c76 = Constraint(expr=   m.x123 + m.x138 >= 0.30458283)

m.c77 = Constraint(expr=   m.x121 + m.x139 >= 0.29951066)

m.c78 = Constraint(expr=   m.x122 + m.x140 >= 0.29951066)

m.c79 = Constraint(expr=   m.x123 + m.x141 >= 0.29951066)

m.c80 = Constraint(expr=   m.x121 + m.x142 >= 0.30694357)

m.c81 = Constraint(expr=   m.x122 + m.x143 >= 0.30694357)

m.c82 = Constraint(expr=   m.x123 + m.x144 >= 0.30694357)

m.c83 = Constraint(expr=   m.x121 + m.x145 >= 0.33520661)

m.c84 = Constraint(expr=   m.x122 + m.x146 >= 0.33520661)

m.c85 = Constraint(expr=   m.x123 + m.x147 >= 0.33520661)

m.c86 = Constraint(expr=   m.x121 + m.x148 >= 0.3400071)

m.c87 = Constraint(expr=   m.x122 + m.x149 >= 0.3400071)

m.c88 = Constraint(expr=   m.x123 + m.x150 >= 0.3400071)

m.c89 = Constraint(expr=   m.x121 + m.x151 >= 0.35227087)

m.c90 = Constraint(expr=   m.x122 + m.x152 >= 0.35227087)

m.c91 = Constraint(expr=   m.x123 + m.x153 >= 0.35227087)

m.c92 = Constraint(expr=   m.x121 + m.x154 >= 0.34225726)

m.c93 = Constraint(expr=   m.x122 + m.x155 >= 0.34225726)

m.c94 = Constraint(expr=   m.x123 + m.x156 >= 0.34225726)

m.c95 = Constraint(expr=   m.x121 + m.x157 >= 0.32776566)

m.c96 = Constraint(expr=   m.x122 + m.x158 >= 0.32776566)

m.c97 = Constraint(expr=   m.x123 + m.x159 >= 0.32776566)

m.c98 = Constraint(expr=   m.x121 + m.x160 >= 0.30438256)

m.c99 = Constraint(expr=   m.x122 + m.x161 >= 0.30438256)

m.c100 = Constraint(expr=   m.x123 + m.x162 >= 0.30438256)

m.c101 = Constraint(expr=   m.x121 + m.x163 >= 0.28538336)

m.c102 = Constraint(expr=   m.x122 + m.x164 >= 0.28538336)

m.c103 = Constraint(expr=   m.x123 + m.x165 >= 0.28538336)

m.c104 = Constraint(expr=   m.x121 + m.x166 >= 0.27950575)

m.c105 = Constraint(expr=   m.x122 + m.x167 >= 0.27950575)

m.c106 = Constraint(expr=   m.x123 + m.x168 >= 0.27950575)

m.c107 = Constraint(expr= - m.x121 + m.x127 >= -0.29424122)

m.c108 = Constraint(expr= - m.x122 + m.x128 >= -0.29424122)

m.c109 = Constraint(expr= - m.x123 + m.x129 >= -0.29424122)

m.c110 = Constraint(expr= - m.x121 + m.x130 >= -0.29760193)

m.c111 = Constraint(expr= - m.x122 + m.x131 >= -0.29760193)

m.c112 = Constraint(expr= - m.x123 + m.x132 >= -0.29760193)

m.c113 = Constraint(expr= - m.x121 + m.x133 >= -0.35149534)

m.c114 = Constraint(expr= - m.x122 + m.x134 >= -0.35149534)

m.c115 = Constraint(expr= - m.x123 + m.x135 >= -0.35149534)

m.c116 = Constraint(expr= - m.x121 + m.x136 >= -0.30458283)

m.c117 = Constraint(expr= - m.x122 + m.x137 >= -0.30458283)

m.c118 = Constraint(expr= - m.x123 + m.x138 >= -0.30458283)

m.c119 = Constraint(expr= - m.x121 + m.x139 >= -0.29951066)

m.c120 = Constraint(expr= - m.x122 + m.x140 >= -0.29951066)

m.c121 = Constraint(expr= - m.x123 + m.x141 >= -0.29951066)

m.c122 = Constraint(expr= - m.x121 + m.x142 >= -0.30694357)

m.c123 = Constraint(expr= - m.x122 + m.x143 >= -0.30694357)

m.c124 = Constraint(expr= - m.x123 + m.x144 >= -0.30694357)

m.c125 = Constraint(expr= - m.x121 + m.x145 >= -0.33520661)

m.c126 = Constraint(expr= - m.x122 + m.x146 >= -0.33520661)

m.c127 = Constraint(expr= - m.x123 + m.x147 >= -0.33520661)

m.c128 = Constraint(expr= - m.x121 + m.x148 >= -0.3400071)

m.c129 = Constraint(expr= - m.x122 + m.x149 >= -0.3400071)

m.c130 = Constraint(expr= - m.x123 + m.x150 >= -0.3400071)

m.c131 = Constraint(expr= - m.x121 + m.x154 >= -0.34225726)

m.c132 = Constraint(expr= - m.x122 + m.x155 >= -0.34225726)

m.c133 = Constraint(expr= - m.x123 + m.x156 >= -0.34225726)

m.c134 = Constraint(expr= - m.x121 + m.x157 >= -0.32776566)

m.c135 = Constraint(expr= - m.x122 + m.x158 >= -0.32776566)

m.c136 = Constraint(expr= - m.x123 + m.x159 >= -0.32776566)

m.c137 = Constraint(expr= - m.x121 + m.x160 >= -0.30438256)

m.c138 = Constraint(expr= - m.x122 + m.x161 >= -0.30438256)

m.c139 = Constraint(expr= - m.x123 + m.x162 >= -0.30438256)

m.c140 = Constraint(expr= - m.x121 + m.x163 >= -0.28538336)

m.c141 = Constraint(expr= - m.x122 + m.x164 >= -0.28538336)

m.c142 = Constraint(expr= - m.x123 + m.x165 >= -0.28538336)

m.c143 = Constraint(expr= - m.x121 + m.x166 >= -0.27950575)

m.c144 = Constraint(expr= - m.x122 + m.x167 >= -0.27950575)

m.c145 = Constraint(expr= - m.x123 + m.x168 >= -0.27950575)

m.c146 = Constraint(expr= - m.x121 + m.x169 >= -0.25788969)

m.c147 = Constraint(expr= - m.x122 + m.x170 >= -0.25788969)

m.c148 = Constraint(expr= - m.x123 + m.x171 >= -0.25788969)

m.c149 = Constraint(expr=   m.x124 + m.x175 >= -0.9536939)

m.c150 = Constraint(expr=   m.x125 + m.x176 >= -0.9536939)

m.c151 = Constraint(expr=   m.x126 + m.x177 >= -0.9536939)

m.c152 = Constraint(expr=   m.x124 + m.x178 >= -0.9004898)

m.c153 = Constraint(expr=   m.x125 + m.x179 >= -0.9004898)

m.c154 = Constraint(expr=   m.x126 + m.x180 >= -0.9004898)

m.c155 = Constraint(expr=   m.x124 + m.x181 >= -0.9114032)

m.c156 = Constraint(expr=   m.x125 + m.x182 >= -0.9114032)

m.c157 = Constraint(expr=   m.x126 + m.x183 >= -0.9114032)

m.c158 = Constraint(expr=   m.x124 + m.x184 >= -0.90071532)

m.c159 = Constraint(expr=   m.x125 + m.x185 >= -0.90071532)

m.c160 = Constraint(expr=   m.x126 + m.x186 >= -0.90071532)

m.c161 = Constraint(expr=   m.x124 + m.x187 >= -0.88043054)

m.c162 = Constraint(expr=   m.x125 + m.x188 >= -0.88043054)

m.c163 = Constraint(expr=   m.x126 + m.x189 >= -0.88043054)

m.c164 = Constraint(expr=   m.x124 + m.x190 >= -0.8680249)

m.c165 = Constraint(expr=   m.x125 + m.x191 >= -0.8680249)

m.c166 = Constraint(expr=   m.x126 + m.x192 >= -0.8680249)

m.c167 = Constraint(expr=   m.x124 + m.x193 >= -0.81034814)

m.c168 = Constraint(expr=   m.x125 + m.x194 >= -0.81034814)

m.c169 = Constraint(expr=   m.x126 + m.x195 >= -0.81034814)

m.c170 = Constraint(expr=   m.x124 + m.x196 >= -0.80843127)

m.c171 = Constraint(expr=   m.x125 + m.x197 >= -0.80843127)

m.c172 = Constraint(expr=   m.x126 + m.x198 >= -0.80843127)

m.c173 = Constraint(expr=   m.x124 + m.x199 >= -0.7794471)

m.c174 = Constraint(expr=   m.x125 + m.x200 >= -0.7794471)

m.c175 = Constraint(expr=   m.x126 + m.x201 >= -0.7794471)

m.c176 = Constraint(expr=   m.x124 + m.x202 >= -0.79930922)

m.c177 = Constraint(expr=   m.x125 + m.x203 >= -0.79930922)

m.c178 = Constraint(expr=   m.x126 + m.x204 >= -0.79930922)

m.c179 = Constraint(expr=   m.x124 + m.x205 >= -0.84280733)

m.c180 = Constraint(expr=   m.x125 + m.x206 >= -0.84280733)

m.c181 = Constraint(expr=   m.x126 + m.x207 >= -0.84280733)

m.c182 = Constraint(expr=   m.x124 + m.x208 >= -0.81379236)

m.c183 = Constraint(expr=   m.x125 + m.x209 >= -0.81379236)

m.c184 = Constraint(expr=   m.x126 + m.x210 >= -0.81379236)

m.c185 = Constraint(expr=   m.x124 + m.x211 >= -0.82457178)

m.c186 = Constraint(expr=   m.x125 + m.x212 >= -0.82457178)

m.c187 = Constraint(expr=   m.x126 + m.x213 >= -0.82457178)

m.c188 = Constraint(expr=   m.x124 + m.x214 >= -0.80226439)

m.c189 = Constraint(expr=   m.x125 + m.x215 >= -0.80226439)

m.c190 = Constraint(expr=   m.x126 + m.x216 >= -0.80226439)

m.c191 = Constraint(expr= - m.x124 + m.x172 >= 0.98493628)

m.c192 = Constraint(expr= - m.x125 + m.x173 >= 0.98493628)

m.c193 = Constraint(expr= - m.x126 + m.x174 >= 0.98493628)

m.c194 = Constraint(expr= - m.x124 + m.x175 >= 0.9536939)

m.c195 = Constraint(expr= - m.x125 + m.x176 >= 0.9536939)

m.c196 = Constraint(expr= - m.x126 + m.x177 >= 0.9536939)

m.c197 = Constraint(expr= - m.x124 + m.x178 >= 0.9004898)

m.c198 = Constraint(expr= - m.x125 + m.x179 >= 0.9004898)

m.c199 = Constraint(expr= - m.x126 + m.x180 >= 0.9004898)

m.c200 = Constraint(expr= - m.x124 + m.x181 >= 0.9114032)

m.c201 = Constraint(expr= - m.x125 + m.x182 >= 0.9114032)

m.c202 = Constraint(expr= - m.x126 + m.x183 >= 0.9114032)

m.c203 = Constraint(expr= - m.x124 + m.x184 >= 0.90071532)

m.c204 = Constraint(expr= - m.x125 + m.x185 >= 0.90071532)

m.c205 = Constraint(expr= - m.x126 + m.x186 >= 0.90071532)

m.c206 = Constraint(expr= - m.x124 + m.x187 >= 0.88043054)

m.c207 = Constraint(expr= - m.x125 + m.x188 >= 0.88043054)

m.c208 = Constraint(expr= - m.x126 + m.x189 >= 0.88043054)

m.c209 = Constraint(expr= - m.x124 + m.x190 >= 0.8680249)

m.c210 = Constraint(expr= - m.x125 + m.x191 >= 0.8680249)

m.c211 = Constraint(expr= - m.x126 + m.x192 >= 0.8680249)

m.c212 = Constraint(expr= - m.x124 + m.x193 >= 0.81034814)

m.c213 = Constraint(expr= - m.x125 + m.x194 >= 0.81034814)

m.c214 = Constraint(expr= - m.x126 + m.x195 >= 0.81034814)

m.c215 = Constraint(expr= - m.x124 + m.x196 >= 0.80843127)

m.c216 = Constraint(expr= - m.x125 + m.x197 >= 0.80843127)

m.c217 = Constraint(expr= - m.x126 + m.x198 >= 0.80843127)

m.c218 = Constraint(expr= - m.x124 + m.x202 >= 0.79930922)

m.c219 = Constraint(expr= - m.x125 + m.x203 >= 0.79930922)

m.c220 = Constraint(expr= - m.x126 + m.x204 >= 0.79930922)

m.c221 = Constraint(expr= - m.x124 + m.x205 >= 0.84280733)

m.c222 = Constraint(expr= - m.x125 + m.x206 >= 0.84280733)

m.c223 = Constraint(expr= - m.x126 + m.x207 >= 0.84280733)

m.c224 = Constraint(expr= - m.x124 + m.x208 >= 0.81379236)

m.c225 = Constraint(expr= - m.x125 + m.x209 >= 0.81379236)

m.c226 = Constraint(expr= - m.x126 + m.x210 >= 0.81379236)

m.c227 = Constraint(expr= - m.x124 + m.x211 >= 0.82457178)

m.c228 = Constraint(expr= - m.x125 + m.x212 >= 0.82457178)

m.c229 = Constraint(expr= - m.x126 + m.x213 >= 0.82457178)

m.c230 = Constraint(expr= - m.x124 + m.x214 >= 0.80226439)

m.c231 = Constraint(expr= - m.x125 + m.x215 >= 0.80226439)

m.c232 = Constraint(expr= - m.x126 + m.x216 >= 0.80226439)

m.c233 = Constraint(expr=   m.x1 - m.x127 - m.x172 == 0)

m.c234 = Constraint(expr=   m.x2 - m.x128 - m.x173 == 0)

m.c235 = Constraint(expr=   m.x3 - m.x129 - m.x174 == 0)

m.c236 = Constraint(expr=   m.x4 - m.x130 - m.x175 == 0)

m.c237 = Constraint(expr=   m.x5 - m.x131 - m.x176 == 0)

m.c238 = Constraint(expr=   m.x6 - m.x132 - m.x177 == 0)

m.c239 = Constraint(expr=   m.x7 - m.x133 - m.x178 == 0)

m.c240 = Constraint(expr=   m.x8 - m.x134 - m.x179 == 0)

m.c241 = Constraint(expr=   m.x9 - m.x135 - m.x180 == 0)

m.c242 = Constraint(expr=   m.x10 - m.x136 - m.x181 == 0)

m.c243 = Constraint(expr=   m.x11 - m.x137 - m.x182 == 0)

m.c244 = Constraint(expr=   m.x12 - m.x138 - m.x183 == 0)

m.c245 = Constraint(expr=   m.x13 - m.x139 - m.x184 == 0)

m.c246 = Constraint(expr=   m.x14 - m.x140 - m.x185 == 0)

m.c247 = Constraint(expr=   m.x15 - m.x141 - m.x186 == 0)

m.c248 = Constraint(expr=   m.x16 - m.x142 - m.x187 == 0)

m.c249 = Constraint(expr=   m.x17 - m.x143 - m.x188 == 0)

m.c250 = Constraint(expr=   m.x18 - m.x144 - m.x189 == 0)

m.c251 = Constraint(expr=   m.x19 - m.x145 - m.x190 == 0)

m.c252 = Constraint(expr=   m.x20 - m.x146 - m.x191 == 0)

m.c253 = Constraint(expr=   m.x21 - m.x147 - m.x192 == 0)

m.c254 = Constraint(expr=   m.x22 - m.x148 - m.x193 == 0)

m.c255 = Constraint(expr=   m.x23 - m.x149 - m.x194 == 0)

m.c256 = Constraint(expr=   m.x24 - m.x150 - m.x195 == 0)

m.c257 = Constraint(expr=   m.x25 - m.x151 - m.x196 == 0)

m.c258 = Constraint(expr=   m.x26 - m.x152 - m.x197 == 0)

m.c259 = Constraint(expr=   m.x27 - m.x153 - m.x198 == 0)

m.c260 = Constraint(expr=   m.x28 - m.x154 - m.x199 == 0)

m.c261 = Constraint(expr=   m.x29 - m.x155 - m.x200 == 0)

m.c262 = Constraint(expr=   m.x30 - m.x156 - m.x201 == 0)

m.c263 = Constraint(expr=   m.x31 - m.x157 - m.x202 == 0)

m.c264 = Constraint(expr=   m.x32 - m.x158 - m.x203 == 0)

m.c265 = Constraint(expr=   m.x33 - m.x159 - m.x204 == 0)

m.c266 = Constraint(expr=   m.x34 - m.x160 - m.x205 == 0)

m.c267 = Constraint(expr=   m.x35 - m.x161 - m.x206 == 0)

m.c268 = Constraint(expr=   m.x36 - m.x162 - m.x207 == 0)

m.c269 = Constraint(expr=   m.x37 - m.x163 - m.x208 == 0)

m.c270 = Constraint(expr=   m.x38 - m.x164 - m.x209 == 0)

m.c271 = Constraint(expr=   m.x39 - m.x165 - m.x210 == 0)

m.c272 = Constraint(expr=   m.x40 - m.x166 - m.x211 == 0)

m.c273 = Constraint(expr=   m.x41 - m.x167 - m.x212 == 0)

m.c274 = Constraint(expr=   m.x42 - m.x168 - m.x213 == 0)

m.c275 = Constraint(expr=   m.x43 - m.x169 - m.x214 == 0)

m.c276 = Constraint(expr=   m.x44 - m.x170 - m.x215 == 0)

m.c277 = Constraint(expr=   m.x45 - m.x171 - m.x216 == 0)

m.c278 = Constraint(expr=   m.b269 + m.b270 >= 1)

m.c279 = Constraint(expr=   m.b267 + m.b272 >= 1)

m.c280 = Constraint(expr=   m.b266 + m.b270 >= 1)

m.c281 = Constraint(expr=   m.b266 + m.b269 + m.b271 >= 1)

m.c282 = Constraint(expr=   m.b266 + m.b268 + m.b272 >= 1)

m.c283 = Constraint(expr=   m.b266 + m.b267 >= 1)

m.c284 = Constraint(expr=   m.b265 + m.b272 >= 1)

m.c285 = Constraint(expr=   m.b265 + m.b269 >= 1)

m.c286 = Constraint(expr=   m.b264 + m.b271 >= 1)

m.c287 = Constraint(expr=   m.b264 + m.b269 + m.b272 >= 1)

m.c288 = Constraint(expr=   m.b264 + m.b268 >= 1)

m.c289 = Constraint(expr=   m.b264 + m.b266 + m.b272 >= 1)

m.c290 = Constraint(expr=   m.b264 + m.b266 + m.b269 >= 1)

m.c291 = Constraint(expr=   m.b264 + m.b265 >= 1)

m.c292 = Constraint(expr=   m.b263 + m.b271 >= 1)

m.c293 = Constraint(expr=   m.b263 + m.b269 + m.b272 >= 1)

m.c294 = Constraint(expr=   m.b263 + m.b268 >= 1)

m.c295 = Constraint(expr=   m.b263 + m.b266 >= 1)

m.c296 = Constraint(expr=   m.b263 + m.b264 >= 1)

m.c297 = Constraint(expr=   m.b262 + m.b271 >= 1)

m.c298 = Constraint(expr=   m.b262 + m.b269 + m.b272 >= 1)

m.c299 = Constraint(expr=   m.b262 + m.b268 >= 1)

m.c300 = Constraint(expr=   m.b262 + m.b266 + m.b272 >= 1)

m.c301 = Constraint(expr=   m.b262 + m.b266 + m.b269 >= 1)

m.c302 = Constraint(expr=   m.b262 + m.b265 >= 1)

m.c303 = Constraint(expr=   m.b262 + m.b264 >= 1)

m.c304 = Constraint(expr=   m.b262 + m.b263 >= 1)

m.c305 = Constraint(expr=   m.b272 + m.b277 >= 1)

m.c306 = Constraint(expr=   m.b272 + m.b276 + m.b278 >= 1)

m.c307 = Constraint(expr=   m.b272 + m.b275 + m.b279 >= 1)

m.c308 = Constraint(expr=   m.b272 + m.b274 >= 1)

m.c309 = Constraint(expr=   m.b272 + m.b273 + m.b279 >= 1)

m.c310 = Constraint(expr=   m.b272 + m.b273 + m.b276 >= 1)

m.c311 = Constraint(expr=   m.b271 + m.b278 >= 1)

m.c312 = Constraint(expr=   m.b271 + m.b276 + m.b279 >= 1)

m.c313 = Constraint(expr=   m.b271 + m.b275 >= 1)

m.c314 = Constraint(expr=   m.b271 + m.b273 >= 1)

m.c315 = Constraint(expr=   m.b270 + m.b279 >= 1)

m.c316 = Constraint(expr=   m.b270 + m.b276 >= 1)

m.c317 = Constraint(expr=   m.b270 + m.b273 >= 1)

m.c318 = Constraint(expr=   m.b269 + m.b277 >= 1)

m.c319 = Constraint(expr=   m.b269 + m.b276 + m.b278 >= 1)

m.c320 = Constraint(expr=   m.b269 + m.b275 + m.b279 >= 1)

m.c321 = Constraint(expr=   m.b269 + m.b274 >= 1)

m.c322 = Constraint(expr=   m.b269 + m.b273 + m.b279 >= 1)

m.c323 = Constraint(expr=   m.b269 + m.b273 + m.b276 >= 1)

m.c324 = Constraint(expr=   m.b269 + m.b272 + m.b278 >= 1)

m.c325 = Constraint(expr=   m.b269 + m.b272 + m.b276 + m.b279 >= 1)

m.c326 = Constraint(expr=   m.b269 + m.b272 + m.b275 >= 1)

m.c327 = Constraint(expr=   m.b269 + m.b272 + m.b273 >= 1)

m.c328 = Constraint(expr=   m.b269 + m.b271 + m.b279 >= 1)

m.c329 = Constraint(expr=   m.b269 + m.b271 + m.b276 >= 1)

m.c330 = Constraint(expr=   m.b269 + m.b271 + m.b273 >= 1)

m.c331 = Constraint(expr=   m.b268 + m.b278 >= 1)

m.c332 = Constraint(expr=   m.b268 + m.b276 + m.b279 >= 1)

m.c333 = Constraint(expr=   m.b268 + m.b275 >= 1)

m.c334 = Constraint(expr=   m.b268 + m.b273 >= 1)

m.c335 = Constraint(expr=   m.b268 + m.b272 + m.b279 >= 1)

m.c336 = Constraint(expr=   m.b268 + m.b272 + m.b276 >= 1)

m.c337 = Constraint(expr=   m.b268 + m.b272 + m.b273 >= 1)

m.c338 = Constraint(expr=   m.b268 + m.b271 + m.b279 >= 1)

m.c339 = Constraint(expr=   m.b268 + m.b271 + m.b276 >= 1)

m.c340 = Constraint(expr=   m.b268 + m.b271 + m.b273 >= 1)

m.c341 = Constraint(expr=   m.b267 + m.b279 >= 1)

m.c342 = Constraint(expr=   m.b267 + m.b276 >= 1)

m.c343 = Constraint(expr=   m.b267 + m.b273 >= 1)

m.c344 = Constraint(expr=   m.b266 + m.b277 >= 1)

m.c345 = Constraint(expr=   m.b266 + m.b276 + m.b278 >= 1)

m.c346 = Constraint(expr=   m.b266 + m.b275 + m.b279 >= 1)

m.c347 = Constraint(expr=   m.b266 + m.b274 >= 1)

m.c348 = Constraint(expr=   m.b266 + m.b273 + m.b279 >= 1)

m.c349 = Constraint(expr=   m.b266 + m.b273 + m.b276 >= 1)

m.c350 = Constraint(expr=   m.b266 + m.b272 + m.b278 >= 1)

m.c351 = Constraint(expr=   m.b266 + m.b272 + m.b276 + m.b279 >= 1)

m.c352 = Constraint(expr=   m.b266 + m.b272 + m.b275 >= 1)

m.c353 = Constraint(expr=   m.b266 + m.b272 + m.b273 >= 1)

m.c354 = Constraint(expr=   m.b266 + m.b271 + m.b279 >= 1)

m.c355 = Constraint(expr=   m.b266 + m.b271 + m.b276 >= 1)

m.c356 = Constraint(expr=   m.b266 + m.b271 + m.b273 >= 1)

m.c357 = Constraint(expr=   m.b266 + m.b269 + m.b278 >= 1)

m.c358 = Constraint(expr=   m.b266 + m.b269 + m.b276 + m.b279 >= 1)

m.c359 = Constraint(expr=   m.b266 + m.b269 + m.b275 >= 1)

m.c360 = Constraint(expr=   m.b266 + m.b269 + m.b273 >= 1)

m.c361 = Constraint(expr=   m.b266 + m.b269 + m.b272 + m.b279 >= 1)

m.c362 = Constraint(expr=   m.b266 + m.b269 + m.b272 + m.b276 >= 1)

m.c363 = Constraint(expr=   m.b266 + m.b269 + m.b272 + m.b273 >= 1)

m.c364 = Constraint(expr=   m.b266 + m.b268 + m.b279 >= 1)

m.c365 = Constraint(expr=   m.b266 + m.b268 + m.b276 >= 1)

m.c366 = Constraint(expr=   m.b266 + m.b268 + m.b273 >= 1)

m.c367 = Constraint(expr=   m.b265 + m.b279 >= 1)

m.c368 = Constraint(expr=   m.b265 + m.b276 >= 1)

m.c369 = Constraint(expr=   m.b265 + m.b273 >= 1)

m.c370 = Constraint(expr=   m.b264 + m.b278 >= 1)

m.c371 = Constraint(expr=   m.b264 + m.b276 + m.b279 >= 1)

m.c372 = Constraint(expr=   m.b264 + m.b275 >= 1)

m.c373 = Constraint(expr=   m.b264 + m.b273 >= 1)

m.c374 = Constraint(expr=   m.b264 + m.b272 + m.b279 >= 1)

m.c375 = Constraint(expr=   m.b264 + m.b272 + m.b276 >= 1)

m.c376 = Constraint(expr=   m.b264 + m.b272 + m.b273 >= 1)

m.c377 = Constraint(expr=   m.b264 + m.b269 + m.b279 >= 1)

m.c378 = Constraint(expr=   m.b264 + m.b269 + m.b276 >= 1)

m.c379 = Constraint(expr=   m.b264 + m.b269 + m.b273 >= 1)

m.c380 = Constraint(expr=   m.b264 + m.b266 + m.b279 >= 1)

m.c381 = Constraint(expr=   m.b264 + m.b266 + m.b276 >= 1)

m.c382 = Constraint(expr=   m.b264 + m.b266 + m.b273 >= 1)

m.c383 = Constraint(expr=   m.b263 + m.b278 >= 1)

m.c384 = Constraint(expr=   m.b263 + m.b276 + m.b279 >= 1)

m.c385 = Constraint(expr=   m.b263 + m.b275 >= 1)

m.c386 = Constraint(expr=   m.b263 + m.b273 >= 1)

m.c387 = Constraint(expr=   m.b263 + m.b272 + m.b279 >= 1)

m.c388 = Constraint(expr=   m.b263 + m.b272 + m.b276 >= 1)

m.c389 = Constraint(expr=   m.b263 + m.b272 + m.b273 >= 1)

m.c390 = Constraint(expr=   m.b263 + m.b269 + m.b279 >= 1)

m.c391 = Constraint(expr=   m.b263 + m.b269 + m.b276 >= 1)

m.c392 = Constraint(expr=   m.b263 + m.b269 + m.b273 >= 1)

m.c393 = Constraint(expr=   m.b262 + m.b278 >= 1)

m.c394 = Constraint(expr=   m.b262 + m.b276 + m.b279 >= 1)

m.c395 = Constraint(expr=   m.b262 + m.b275 >= 1)

m.c396 = Constraint(expr=   m.b262 + m.b273 >= 1)

m.c397 = Constraint(expr=   m.b262 + m.b272 + m.b279 >= 1)

m.c398 = Constraint(expr=   m.b262 + m.b272 + m.b276 >= 1)

m.c399 = Constraint(expr=   m.b262 + m.b272 + m.b273 >= 1)

m.c400 = Constraint(expr=   m.b262 + m.b269 + m.b279 >= 1)

m.c401 = Constraint(expr=   m.b262 + m.b269 + m.b276 >= 1)

m.c402 = Constraint(expr=   m.b262 + m.b269 + m.b273 >= 1)

m.c403 = Constraint(expr=   m.b262 + m.b266 + m.b279 >= 1)

m.c404 = Constraint(expr=   m.b262 + m.b266 + m.b276 >= 1)

m.c405 = Constraint(expr=   m.b262 + m.b266 + m.b273 >= 1)

m.c406 = Constraint(expr=   m.x46 - 2.02*m.b262 >= 0)

m.c407 = Constraint(expr=   m.x47 - 4.01333333333333*m.b263 >= 0)

m.c408 = Constraint(expr=   m.x48 - 4.76*m.b264 >= 0)

m.c409 = Constraint(expr=   m.x49 - 5.68*m.b265 >= 0)

m.c410 = Constraint(expr=   m.x49 - 5.96*m.b266 >= 0)

m.c411 = Constraint(expr=   m.x50 - 38.2666666666667*m.b267 >= 0)

m.c412 = Constraint(expr=   m.x50 - 40.18*m.b268 >= 0)

m.c413 = Constraint(expr=   m.x50 - 42.0933333333333*m.b269 >= 0)

m.c414 = Constraint(expr=   m.x51 - 90.2533333333333*m.b270 >= 0)

m.c415 = Constraint(expr=   m.x51 - 94.7666666666667*m.b271 >= 0)

m.c416 = Constraint(expr=   m.x51 - 99.28*m.b272 >= 0)

m.c417 = Constraint(expr=   m.x52 - 6.59333333333333*m.b273 >= 0)

m.c418 = Constraint(expr=   m.x53 - 56.24*m.b274 >= 0)

m.c419 = Constraint(expr=   m.x53 - 59.0533333333333*m.b275 >= 0)

m.c420 = Constraint(expr=   m.x53 - 61.8666666666667*m.b276 >= 0)

m.c421 = Constraint(expr=   m.x54 - 51.1733333333333*m.b277 >= 0)

m.c422 = Constraint(expr=   m.x54 - 53.7333333333333*m.b278 >= 0)

m.c423 = Constraint(expr=   m.x54 - 56.2866666666667*m.b279 >= 0)

m.c424 = Constraint(expr=   m.x55 - 35.84*m.b280 >= 0)

m.c425 = Constraint(expr=   m.x55 - 37.7266666666667*m.b281 >= 0)

m.c426 = Constraint(expr=   m.x55 - 39.6133333333333*m.b282 >= 0)

m.c427 = Constraint(expr=   m.x55 - 41.5*m.b283 >= 0)

m.c428 = Constraint(expr=   m.x56 - 56.8066666666667*m.b284 >= 0)

m.c429 = Constraint(expr=   m.x56 - 59.6466666666667*m.b285 >= 0)

m.c430 = Constraint(expr=   m.x56 - 62.4933333333333*m.b286 >= 0)

m.c431 = Constraint(expr=   m.x57 - 80.9066666666667*m.b287 >= 0)

m.c432 = Constraint(expr=   m.x58 - 26.1466666666667*m.b288 >= 0)

m.c433 = Constraint(expr=   m.x59 - 38*m.b289 >= 0)

m.c434 = Constraint(expr=   m.x60 - 59.2733333333333*m.b290 >= 0)

m.c435 = Constraint(expr=   m.x60 - 62.24*m.b291 >= 0)

m.c436 = Constraint(expr= - m.x106 + m.x217 <= 0)

m.c437 = Constraint(expr= - m.x106 + m.x218 <= 0)

m.c438 = Constraint(expr= - m.x106 + m.x219 <= 0)

m.c439 = Constraint(expr= - m.x107 + m.x220 <= 0)

m.c440 = Constraint(expr= - m.x107 + m.x221 <= 0)

m.c441 = Constraint(expr= - m.x107 + m.x222 <= 0)

m.c442 = Constraint(expr= - m.x108 + m.x223 <= 0)

m.c443 = Constraint(expr= - m.x108 + m.x224 <= 0)

m.c444 = Constraint(expr= - m.x108 + m.x225 <= 0)

m.c445 = Constraint(expr= - m.x109 + m.x226 <= 0)

m.c446 = Constraint(expr= - m.x109 + m.x227 <= 0)

m.c447 = Constraint(expr= - m.x109 + m.x228 <= 0)

m.c448 = Constraint(expr= - m.x110 + m.x229 <= 0)

m.c449 = Constraint(expr= - m.x110 + m.x230 <= 0)

m.c450 = Constraint(expr= - m.x110 + m.x231 <= 0)

m.c451 = Constraint(expr= - m.x111 + m.x232 <= 0)

m.c452 = Constraint(expr= - m.x111 + m.x233 <= 0)

m.c453 = Constraint(expr= - m.x111 + m.x234 <= 0)

m.c454 = Constraint(expr= - m.x112 + m.x235 <= 0)

m.c455 = Constraint(expr= - m.x112 + m.x236 <= 0)

m.c456 = Constraint(expr= - m.x112 + m.x237 <= 0)

m.c457 = Constraint(expr= - m.x113 + m.x238 <= 0)

m.c458 = Constraint(expr= - m.x113 + m.x239 <= 0)

m.c459 = Constraint(expr= - m.x113 + m.x240 <= 0)

m.c460 = Constraint(expr= - m.x114 + m.x241 <= 0)

m.c461 = Constraint(expr= - m.x114 + m.x242 <= 0)

m.c462 = Constraint(expr= - m.x114 + m.x243 <= 0)

m.c463 = Constraint(expr= - m.x115 + m.x244 <= 0)

m.c464 = Constraint(expr= - m.x115 + m.x245 <= 0)

m.c465 = Constraint(expr= - m.x115 + m.x246 <= 0)

m.c466 = Constraint(expr= - m.x116 + m.x247 <= 0)

m.c467 = Constraint(expr= - m.x116 + m.x248 <= 0)

m.c468 = Constraint(expr= - m.x116 + m.x249 <= 0)

m.c469 = Constraint(expr= - m.x117 + m.x250 <= 0)

m.c470 = Constraint(expr= - m.x117 + m.x251 <= 0)

m.c471 = Constraint(expr= - m.x117 + m.x252 <= 0)

m.c472 = Constraint(expr= - m.x118 + m.x253 <= 0)

m.c473 = Constraint(expr= - m.x118 + m.x254 <= 0)

m.c474 = Constraint(expr= - m.x118 + m.x255 <= 0)

m.c475 = Constraint(expr= - m.x119 + m.x256 <= 0)

m.c476 = Constraint(expr= - m.x119 + m.x257 <= 0)

m.c477 = Constraint(expr= - m.x119 + m.x258 <= 0)

m.c478 = Constraint(expr= - m.x120 + m.x259 <= 0)

m.c479 = Constraint(expr= - m.x120 + m.x260 <= 0)

m.c480 = Constraint(expr= - m.x120 + m.x261 <= 0)

m.c481 = Constraint(expr=   m.b265 - m.b266 >= 0)

m.c482 = Constraint(expr=   m.b267 - m.b268 >= 0)

m.c483 = Constraint(expr=   m.b268 - m.b269 >= 0)

m.c484 = Constraint(expr=   m.b270 - m.b271 >= 0)

m.c485 = Constraint(expr=   m.b271 - m.b272 >= 0)

m.c486 = Constraint(expr=   m.b274 - m.b275 >= 0)

m.c487 = Constraint(expr=   m.b275 - m.b276 >= 0)

m.c488 = Constraint(expr=   m.b277 - m.b278 >= 0)

m.c489 = Constraint(expr=   m.b278 - m.b279 >= 0)

m.c490 = Constraint(expr=   m.b280 - m.b281 >= 0)

m.c491 = Constraint(expr=   m.b281 - m.b282 >= 0)

m.c492 = Constraint(expr=   m.b282 - m.b283 >= 0)

m.c493 = Constraint(expr=   m.b284 - m.b285 >= 0)

m.c494 = Constraint(expr=   m.b285 - m.b286 >= 0)

m.c495 = Constraint(expr=   m.b290 - m.b291 >= 0)

m.c496 = Constraint(expr=   m.x124 - m.x125 >= 0)

m.c497 = Constraint(expr=   m.x125 - m.x126 >= 0)
