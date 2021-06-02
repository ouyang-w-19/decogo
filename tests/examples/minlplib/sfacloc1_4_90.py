#  MINLP written by GAMS Convert at 04/21/18 13:54:11
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        495      106      370       19        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        324      294       30        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1367     1232      135        0
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
m.x46 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,0.26351883),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,0.26351883),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,0.26351883),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,0.26351883),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,0.22891574),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,0.22891574),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,0.22891574),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,0.22891574),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,0.21464835),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,0.21464835),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,0.21464835),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,0.21464835),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,0.17964414),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,0.17964414),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,0.17964414),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,0.17964414),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,0.17402843),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,0.17402843),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,0.17402843),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,0.17402843),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,0.15355962),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,0.15355962),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,0.15355962),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,0.15355962),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,0.1942283),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,0.1942283),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,0.1942283),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,0.1942283),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,0.25670555),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,0.25670555),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,0.25670555),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,0.25670555),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,0.27088619),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,0.27088619),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,0.27088619),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,0.27088619),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,0.28985675),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,0.28985675),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,0.28985675),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,0.28985675),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,0.25550303),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,0.25550303),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,0.25550303),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,0.25550303),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,0.19001726),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,0.19001726),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,0.19001726),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,0.19001726),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,0.23803143),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,0.23803143),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,0.23803143),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,0.23803143),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,0.23312962),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,0.23312962),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,0.23312962),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,0.23312962),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,0.27705307),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,0.27705307),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,0.27705307),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,0.27705307),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,2.02),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,4.01333333333333),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,4.76),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,5.96),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,42.0933333333333),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,99.28),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,6.59333333333333),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,61.8666666666667),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,56.2866666666667),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,41.5),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,62.4933333333333),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,80.9066666666667),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,26.1466666666667),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,38),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,62.24),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.x151 = Var(within=Reals,bounds=(0.25788969,0.35227087),initialize=0.25788969)
m.x152 = Var(within=Reals,bounds=(0.25788969,0.35227087),initialize=0.25788969)
m.x153 = Var(within=Reals,bounds=(0.25788969,0.35227087),initialize=0.25788969)
m.x154 = Var(within=Reals,bounds=(0.25788969,0.35227087),initialize=0.25788969)
m.x155 = Var(within=Reals,bounds=(-0.98493628,-0.7794471),initialize=-0.7794471)
m.x156 = Var(within=Reals,bounds=(-0.98493628,-0.7794471),initialize=-0.7794471)
m.x157 = Var(within=Reals,bounds=(-0.98493628,-0.7794471),initialize=-0.7794471)
m.x158 = Var(within=Reals,bounds=(-0.98493628,-0.7794471),initialize=-0.7794471)
m.x159 = Var(within=Reals,bounds=(0,0.0580296499999999),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,0.0580296499999999),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,0.0580296499999999),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,0.0580296499999999),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,0.0546689399999999),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,0.0546689399999999),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,0.0546689399999999),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,0.0546689399999999),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,0.09360565),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,0.09360565),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,0.09360565),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,0.09360565),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,0.0476880399999999),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,0.0476880399999999),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,0.0476880399999999),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,0.0476880399999999),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,0.05276021),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,0.05276021),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,0.05276021),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,0.05276021),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,0.04905388),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,0.04905388),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,0.04905388),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,0.04905388),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,0.07731692),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,0.07731692),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,0.07731692),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,0.07731692),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,0.08211741),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,0.08211741),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,0.08211741),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,0.08211741),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,0.08436757),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,0.08436757),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,0.08436757),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,0.08436757),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,0.06987597),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,0.06987597),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,0.06987597),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,0.06987597),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,0.04788831),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,0.04788831),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,0.04788831),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,0.04788831),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,0.0668875099999999),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,0.0668875099999999),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,0.0668875099999999),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,0.0668875099999999),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,0.07276512),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,0.07276512),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,0.07276512),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,0.07276512),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,0.1742468),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,0.1742468),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,0.1742468),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,0.1742468),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,0.1210427),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,0.1210427),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,0.1210427),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,0.1210427),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,0.1319561),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,0.1319561),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,0.1319561),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,0.1319561),initialize=0)
m.x235 = Var(within=Reals,bounds=(0,0.12126822),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,0.12126822),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,0.12126822),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,0.12126822),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,0.10450574),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,0.10450574),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,0.10450574),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,0.10450574),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,0.11691138),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,0.11691138),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,0.11691138),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,0.11691138),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,0.17458814),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,0.17458814),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,0.17458814),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,0.17458814),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,0.17650501),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,0.17650501),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,0.17650501),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,0.17650501),initialize=0)
m.x255 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x258 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,0.18562706),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,0.18562706),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,0.18562706),initialize=0)
m.x262 = Var(within=Reals,bounds=(0,0.18562706),initialize=0)
m.x263 = Var(within=Reals,bounds=(0,0.14212895),initialize=0)
m.x264 = Var(within=Reals,bounds=(0,0.14212895),initialize=0)
m.x265 = Var(within=Reals,bounds=(0,0.14212895),initialize=0)
m.x266 = Var(within=Reals,bounds=(0,0.14212895),initialize=0)
m.x267 = Var(within=Reals,bounds=(0,0.17114392),initialize=0)
m.x268 = Var(within=Reals,bounds=(0,0.17114392),initialize=0)
m.x269 = Var(within=Reals,bounds=(0,0.17114392),initialize=0)
m.x270 = Var(within=Reals,bounds=(0,0.17114392),initialize=0)
m.x271 = Var(within=Reals,bounds=(0,0.1603645),initialize=0)
m.x272 = Var(within=Reals,bounds=(0,0.1603645),initialize=0)
m.x273 = Var(within=Reals,bounds=(0,0.1603645),initialize=0)
m.x274 = Var(within=Reals,bounds=(0,0.1603645),initialize=0)
m.x275 = Var(within=Reals,bounds=(0,0.18267189),initialize=0)
m.x276 = Var(within=Reals,bounds=(0,0.18267189),initialize=0)
m.x277 = Var(within=Reals,bounds=(0,0.18267189),initialize=0)
m.x278 = Var(within=Reals,bounds=(0,0.18267189),initialize=0)
m.x279 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x280 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x281 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x282 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x283 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x284 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x285 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x286 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x287 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x289 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x290 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x291 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x292 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x293 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.b294 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b295 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b296 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b297 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b298 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b299 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b300 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b301 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b302 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b303 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b304 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b305 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b306 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b307 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b308 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b309 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b310 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b311 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b312 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b313 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b314 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b315 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b316 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b317 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b318 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b319 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b320 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b321 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b322 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b323 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   m.x136 + m.x137 + m.x138 + m.x139 + m.x140 + m.x141 + m.x142 + m.x143 + m.x144 + m.x145
                        + m.x146 + m.x147 + m.x148 + m.x149 + m.x150, sense=minimize)

m.c2 = Constraint(expr=-(m.x121*m.x61*m.x1 + m.x121*m.x62*m.x2 + m.x121*m.x63*m.x3 + m.x121*m.x64*m.x4) + m.x279 == 0)

m.c3 = Constraint(expr=-(m.x122*m.x65*m.x5 + m.x122*m.x66*m.x6 + m.x122*m.x67*m.x7 + m.x122*m.x68*m.x8) + m.x280 == 0)

m.c4 = Constraint(expr=-(m.x123*m.x69*m.x9 + m.x123*m.x70*m.x10 + m.x123*m.x71*m.x11 + m.x123*m.x72*m.x12) + m.x281
                        == 0)

m.c5 = Constraint(expr=-(m.x124*m.x73*m.x13 + m.x124*m.x74*m.x14 + m.x124*m.x75*m.x15 + m.x124*m.x76*m.x16) + m.x282
                        == 0)

m.c6 = Constraint(expr=-(m.x125*m.x77*m.x17 + m.x125*m.x78*m.x18 + m.x125*m.x79*m.x19 + m.x125*m.x80*m.x20) + m.x283
                        == 0)

m.c7 = Constraint(expr=-(m.x126*m.x81*m.x21 + m.x126*m.x82*m.x22 + m.x126*m.x83*m.x23 + m.x126*m.x84*m.x24) + m.x284
                        == 0)

m.c8 = Constraint(expr=-(m.x127*m.x85*m.x25 + m.x127*m.x86*m.x26 + m.x127*m.x87*m.x27 + m.x127*m.x88*m.x28) + m.x285
                        == 0)

m.c9 = Constraint(expr=-(m.x128*m.x89*m.x29 + m.x128*m.x90*m.x30 + m.x128*m.x91*m.x31 + m.x128*m.x92*m.x32) + m.x286
                        == 0)

m.c10 = Constraint(expr=-(m.x129*m.x93*m.x33 + m.x129*m.x94*m.x34 + m.x129*m.x95*m.x35 + m.x129*m.x96*m.x36) + m.x287
                         == 0)

m.c11 = Constraint(expr=-(m.x130*m.x97*m.x37 + m.x130*m.x98*m.x38 + m.x130*m.x99*m.x39 + m.x130*m.x100*m.x40) + m.x288
                         == 0)

m.c12 = Constraint(expr=-(m.x131*m.x101*m.x41 + m.x131*m.x102*m.x42 + m.x131*m.x103*m.x43 + m.x131*m.x104*m.x44)
                         + m.x289 == 0)

m.c13 = Constraint(expr=-(m.x132*m.x105*m.x45 + m.x132*m.x106*m.x46 + m.x132*m.x107*m.x47 + m.x132*m.x108*m.x48)
                         + m.x290 == 0)

m.c14 = Constraint(expr=-(m.x133*m.x109*m.x49 + m.x133*m.x110*m.x50 + m.x133*m.x111*m.x51 + m.x133*m.x112*m.x52)
                         + m.x291 == 0)

m.c15 = Constraint(expr=-(m.x134*m.x113*m.x53 + m.x134*m.x114*m.x54 + m.x134*m.x115*m.x55 + m.x134*m.x116*m.x56)
                         + m.x292 == 0)

m.c16 = Constraint(expr=-(m.x135*m.x117*m.x57 + m.x135*m.x118*m.x58 + m.x135*m.x119*m.x59 + m.x135*m.x120*m.x60)
                         + m.x293 == 0)

m.c17 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 == 1)

m.c18 = Constraint(expr=   m.x5 + m.x6 + m.x7 + m.x8 == 1)

m.c19 = Constraint(expr=   m.x9 + m.x10 + m.x11 + m.x12 == 1)

m.c20 = Constraint(expr=   m.x13 + m.x14 + m.x15 + m.x16 == 1)

m.c21 = Constraint(expr=   m.x17 + m.x18 + m.x19 + m.x20 == 1)

m.c22 = Constraint(expr=   m.x21 + m.x22 + m.x23 + m.x24 == 1)

m.c23 = Constraint(expr=   m.x25 + m.x26 + m.x27 + m.x28 == 1)

m.c24 = Constraint(expr=   m.x29 + m.x30 + m.x31 + m.x32 == 1)

m.c25 = Constraint(expr=   m.x33 + m.x34 + m.x35 + m.x36 == 1)

m.c26 = Constraint(expr=   m.x37 + m.x38 + m.x39 + m.x40 == 1)

m.c27 = Constraint(expr=   m.x41 + m.x42 + m.x43 + m.x44 == 1)

m.c28 = Constraint(expr=   m.x45 + m.x46 + m.x47 + m.x48 == 1)

m.c29 = Constraint(expr=   m.x49 + m.x50 + m.x51 + m.x52 == 1)

m.c30 = Constraint(expr=   m.x53 + m.x54 + m.x55 + m.x56 == 1)

m.c31 = Constraint(expr=   m.x57 + m.x58 + m.x59 + m.x60 == 1)

m.c32 = Constraint(expr=   2.02*m.x1 + 4.01333333333333*m.x5 + 4.76*m.x9 + 5.96*m.x13 + 42.0933333333333*m.x17
                         + 99.28*m.x21 + 6.59333333333333*m.x25 + 61.8666666666667*m.x29 + 56.2866666666667*m.x33
                         + 41.5*m.x37 + 62.4933333333333*m.x41 + 80.9066666666667*m.x45 + 26.1466666666667*m.x49
                         + 38*m.x53 + 62.24*m.x57 <= 153.54)

m.c33 = Constraint(expr=   2.02*m.x2 + 4.01333333333333*m.x6 + 4.76*m.x10 + 5.96*m.x14 + 42.0933333333333*m.x18
                         + 99.28*m.x22 + 6.59333333333333*m.x26 + 61.8666666666667*m.x30 + 56.2866666666667*m.x34
                         + 41.5*m.x38 + 62.4933333333333*m.x42 + 80.9066666666667*m.x46 + 26.1466666666667*m.x50
                         + 38*m.x54 + 62.24*m.x58 <= 153.54)

m.c34 = Constraint(expr=   2.02*m.x3 + 4.01333333333333*m.x7 + 4.76*m.x11 + 5.96*m.x15 + 42.0933333333333*m.x19
                         + 99.28*m.x23 + 6.59333333333333*m.x27 + 61.8666666666667*m.x31 + 56.2866666666667*m.x35
                         + 41.5*m.x39 + 62.4933333333333*m.x43 + 80.9066666666667*m.x47 + 26.1466666666667*m.x51
                         + 38*m.x55 + 62.24*m.x59 <= 153.54)

m.c35 = Constraint(expr=   2.02*m.x4 + 4.01333333333333*m.x8 + 4.76*m.x12 + 5.96*m.x16 + 42.0933333333333*m.x20
                         + 99.28*m.x24 + 6.59333333333333*m.x28 + 61.8666666666667*m.x32 + 56.2866666666667*m.x36
                         + 41.5*m.x40 + 62.4933333333333*m.x44 + 80.9066666666667*m.x48 + 26.1466666666667*m.x52
                         + 38*m.x56 + 62.24*m.x60 <= 153.54)

m.c36 = Constraint(expr=   m.x151 + m.x159 >= 0.29424122)

m.c37 = Constraint(expr=   m.x152 + m.x160 >= 0.29424122)

m.c38 = Constraint(expr=   m.x153 + m.x161 >= 0.29424122)

m.c39 = Constraint(expr=   m.x154 + m.x162 >= 0.29424122)

m.c40 = Constraint(expr=   m.x151 + m.x163 >= 0.29760193)

m.c41 = Constraint(expr=   m.x152 + m.x164 >= 0.29760193)

m.c42 = Constraint(expr=   m.x153 + m.x165 >= 0.29760193)

m.c43 = Constraint(expr=   m.x154 + m.x166 >= 0.29760193)

m.c44 = Constraint(expr=   m.x151 + m.x167 >= 0.35149534)

m.c45 = Constraint(expr=   m.x152 + m.x168 >= 0.35149534)

m.c46 = Constraint(expr=   m.x153 + m.x169 >= 0.35149534)

m.c47 = Constraint(expr=   m.x154 + m.x170 >= 0.35149534)

m.c48 = Constraint(expr=   m.x151 + m.x171 >= 0.30458283)

m.c49 = Constraint(expr=   m.x152 + m.x172 >= 0.30458283)

m.c50 = Constraint(expr=   m.x153 + m.x173 >= 0.30458283)

m.c51 = Constraint(expr=   m.x154 + m.x174 >= 0.30458283)

m.c52 = Constraint(expr=   m.x151 + m.x175 >= 0.29951066)

m.c53 = Constraint(expr=   m.x152 + m.x176 >= 0.29951066)

m.c54 = Constraint(expr=   m.x153 + m.x177 >= 0.29951066)

m.c55 = Constraint(expr=   m.x154 + m.x178 >= 0.29951066)

m.c56 = Constraint(expr=   m.x151 + m.x179 >= 0.30694357)

m.c57 = Constraint(expr=   m.x152 + m.x180 >= 0.30694357)

m.c58 = Constraint(expr=   m.x153 + m.x181 >= 0.30694357)

m.c59 = Constraint(expr=   m.x154 + m.x182 >= 0.30694357)

m.c60 = Constraint(expr=   m.x151 + m.x183 >= 0.33520661)

m.c61 = Constraint(expr=   m.x152 + m.x184 >= 0.33520661)

m.c62 = Constraint(expr=   m.x153 + m.x185 >= 0.33520661)

m.c63 = Constraint(expr=   m.x154 + m.x186 >= 0.33520661)

m.c64 = Constraint(expr=   m.x151 + m.x187 >= 0.3400071)

m.c65 = Constraint(expr=   m.x152 + m.x188 >= 0.3400071)

m.c66 = Constraint(expr=   m.x153 + m.x189 >= 0.3400071)

m.c67 = Constraint(expr=   m.x154 + m.x190 >= 0.3400071)

m.c68 = Constraint(expr=   m.x151 + m.x191 >= 0.35227087)

m.c69 = Constraint(expr=   m.x152 + m.x192 >= 0.35227087)

m.c70 = Constraint(expr=   m.x153 + m.x193 >= 0.35227087)

m.c71 = Constraint(expr=   m.x154 + m.x194 >= 0.35227087)

m.c72 = Constraint(expr=   m.x151 + m.x195 >= 0.34225726)

m.c73 = Constraint(expr=   m.x152 + m.x196 >= 0.34225726)

m.c74 = Constraint(expr=   m.x153 + m.x197 >= 0.34225726)

m.c75 = Constraint(expr=   m.x154 + m.x198 >= 0.34225726)

m.c76 = Constraint(expr=   m.x151 + m.x199 >= 0.32776566)

m.c77 = Constraint(expr=   m.x152 + m.x200 >= 0.32776566)

m.c78 = Constraint(expr=   m.x153 + m.x201 >= 0.32776566)

m.c79 = Constraint(expr=   m.x154 + m.x202 >= 0.32776566)

m.c80 = Constraint(expr=   m.x151 + m.x203 >= 0.30438256)

m.c81 = Constraint(expr=   m.x152 + m.x204 >= 0.30438256)

m.c82 = Constraint(expr=   m.x153 + m.x205 >= 0.30438256)

m.c83 = Constraint(expr=   m.x154 + m.x206 >= 0.30438256)

m.c84 = Constraint(expr=   m.x151 + m.x207 >= 0.28538336)

m.c85 = Constraint(expr=   m.x152 + m.x208 >= 0.28538336)

m.c86 = Constraint(expr=   m.x153 + m.x209 >= 0.28538336)

m.c87 = Constraint(expr=   m.x154 + m.x210 >= 0.28538336)

m.c88 = Constraint(expr=   m.x151 + m.x211 >= 0.27950575)

m.c89 = Constraint(expr=   m.x152 + m.x212 >= 0.27950575)

m.c90 = Constraint(expr=   m.x153 + m.x213 >= 0.27950575)

m.c91 = Constraint(expr=   m.x154 + m.x214 >= 0.27950575)

m.c92 = Constraint(expr= - m.x151 + m.x159 >= -0.29424122)

m.c93 = Constraint(expr= - m.x152 + m.x160 >= -0.29424122)

m.c94 = Constraint(expr= - m.x153 + m.x161 >= -0.29424122)

m.c95 = Constraint(expr= - m.x154 + m.x162 >= -0.29424122)

m.c96 = Constraint(expr= - m.x151 + m.x163 >= -0.29760193)

m.c97 = Constraint(expr= - m.x152 + m.x164 >= -0.29760193)

m.c98 = Constraint(expr= - m.x153 + m.x165 >= -0.29760193)

m.c99 = Constraint(expr= - m.x154 + m.x166 >= -0.29760193)

m.c100 = Constraint(expr= - m.x151 + m.x167 >= -0.35149534)

m.c101 = Constraint(expr= - m.x152 + m.x168 >= -0.35149534)

m.c102 = Constraint(expr= - m.x153 + m.x169 >= -0.35149534)

m.c103 = Constraint(expr= - m.x154 + m.x170 >= -0.35149534)

m.c104 = Constraint(expr= - m.x151 + m.x171 >= -0.30458283)

m.c105 = Constraint(expr= - m.x152 + m.x172 >= -0.30458283)

m.c106 = Constraint(expr= - m.x153 + m.x173 >= -0.30458283)

m.c107 = Constraint(expr= - m.x154 + m.x174 >= -0.30458283)

m.c108 = Constraint(expr= - m.x151 + m.x175 >= -0.29951066)

m.c109 = Constraint(expr= - m.x152 + m.x176 >= -0.29951066)

m.c110 = Constraint(expr= - m.x153 + m.x177 >= -0.29951066)

m.c111 = Constraint(expr= - m.x154 + m.x178 >= -0.29951066)

m.c112 = Constraint(expr= - m.x151 + m.x179 >= -0.30694357)

m.c113 = Constraint(expr= - m.x152 + m.x180 >= -0.30694357)

m.c114 = Constraint(expr= - m.x153 + m.x181 >= -0.30694357)

m.c115 = Constraint(expr= - m.x154 + m.x182 >= -0.30694357)

m.c116 = Constraint(expr= - m.x151 + m.x183 >= -0.33520661)

m.c117 = Constraint(expr= - m.x152 + m.x184 >= -0.33520661)

m.c118 = Constraint(expr= - m.x153 + m.x185 >= -0.33520661)

m.c119 = Constraint(expr= - m.x154 + m.x186 >= -0.33520661)

m.c120 = Constraint(expr= - m.x151 + m.x187 >= -0.3400071)

m.c121 = Constraint(expr= - m.x152 + m.x188 >= -0.3400071)

m.c122 = Constraint(expr= - m.x153 + m.x189 >= -0.3400071)

m.c123 = Constraint(expr= - m.x154 + m.x190 >= -0.3400071)

m.c124 = Constraint(expr= - m.x151 + m.x195 >= -0.34225726)

m.c125 = Constraint(expr= - m.x152 + m.x196 >= -0.34225726)

m.c126 = Constraint(expr= - m.x153 + m.x197 >= -0.34225726)

m.c127 = Constraint(expr= - m.x154 + m.x198 >= -0.34225726)

m.c128 = Constraint(expr= - m.x151 + m.x199 >= -0.32776566)

m.c129 = Constraint(expr= - m.x152 + m.x200 >= -0.32776566)

m.c130 = Constraint(expr= - m.x153 + m.x201 >= -0.32776566)

m.c131 = Constraint(expr= - m.x154 + m.x202 >= -0.32776566)

m.c132 = Constraint(expr= - m.x151 + m.x203 >= -0.30438256)

m.c133 = Constraint(expr= - m.x152 + m.x204 >= -0.30438256)

m.c134 = Constraint(expr= - m.x153 + m.x205 >= -0.30438256)

m.c135 = Constraint(expr= - m.x154 + m.x206 >= -0.30438256)

m.c136 = Constraint(expr= - m.x151 + m.x207 >= -0.28538336)

m.c137 = Constraint(expr= - m.x152 + m.x208 >= -0.28538336)

m.c138 = Constraint(expr= - m.x153 + m.x209 >= -0.28538336)

m.c139 = Constraint(expr= - m.x154 + m.x210 >= -0.28538336)

m.c140 = Constraint(expr= - m.x151 + m.x211 >= -0.27950575)

m.c141 = Constraint(expr= - m.x152 + m.x212 >= -0.27950575)

m.c142 = Constraint(expr= - m.x153 + m.x213 >= -0.27950575)

m.c143 = Constraint(expr= - m.x154 + m.x214 >= -0.27950575)

m.c144 = Constraint(expr= - m.x151 + m.x215 >= -0.25788969)

m.c145 = Constraint(expr= - m.x152 + m.x216 >= -0.25788969)

m.c146 = Constraint(expr= - m.x153 + m.x217 >= -0.25788969)

m.c147 = Constraint(expr= - m.x154 + m.x218 >= -0.25788969)

m.c148 = Constraint(expr=   m.x155 + m.x223 >= -0.9536939)

m.c149 = Constraint(expr=   m.x156 + m.x224 >= -0.9536939)

m.c150 = Constraint(expr=   m.x157 + m.x225 >= -0.9536939)

m.c151 = Constraint(expr=   m.x158 + m.x226 >= -0.9536939)

m.c152 = Constraint(expr=   m.x155 + m.x227 >= -0.9004898)

m.c153 = Constraint(expr=   m.x156 + m.x228 >= -0.9004898)

m.c154 = Constraint(expr=   m.x157 + m.x229 >= -0.9004898)

m.c155 = Constraint(expr=   m.x158 + m.x230 >= -0.9004898)

m.c156 = Constraint(expr=   m.x155 + m.x231 >= -0.9114032)

m.c157 = Constraint(expr=   m.x156 + m.x232 >= -0.9114032)

m.c158 = Constraint(expr=   m.x157 + m.x233 >= -0.9114032)

m.c159 = Constraint(expr=   m.x158 + m.x234 >= -0.9114032)

m.c160 = Constraint(expr=   m.x155 + m.x235 >= -0.90071532)

m.c161 = Constraint(expr=   m.x156 + m.x236 >= -0.90071532)

m.c162 = Constraint(expr=   m.x157 + m.x237 >= -0.90071532)

m.c163 = Constraint(expr=   m.x158 + m.x238 >= -0.90071532)

m.c164 = Constraint(expr=   m.x155 + m.x239 >= -0.88043054)

m.c165 = Constraint(expr=   m.x156 + m.x240 >= -0.88043054)

m.c166 = Constraint(expr=   m.x157 + m.x241 >= -0.88043054)

m.c167 = Constraint(expr=   m.x158 + m.x242 >= -0.88043054)

m.c168 = Constraint(expr=   m.x155 + m.x243 >= -0.8680249)

m.c169 = Constraint(expr=   m.x156 + m.x244 >= -0.8680249)

m.c170 = Constraint(expr=   m.x157 + m.x245 >= -0.8680249)

m.c171 = Constraint(expr=   m.x158 + m.x246 >= -0.8680249)

m.c172 = Constraint(expr=   m.x155 + m.x247 >= -0.81034814)

m.c173 = Constraint(expr=   m.x156 + m.x248 >= -0.81034814)

m.c174 = Constraint(expr=   m.x157 + m.x249 >= -0.81034814)

m.c175 = Constraint(expr=   m.x158 + m.x250 >= -0.81034814)

m.c176 = Constraint(expr=   m.x155 + m.x251 >= -0.80843127)

m.c177 = Constraint(expr=   m.x156 + m.x252 >= -0.80843127)

m.c178 = Constraint(expr=   m.x157 + m.x253 >= -0.80843127)

m.c179 = Constraint(expr=   m.x158 + m.x254 >= -0.80843127)

m.c180 = Constraint(expr=   m.x155 + m.x255 >= -0.7794471)

m.c181 = Constraint(expr=   m.x156 + m.x256 >= -0.7794471)

m.c182 = Constraint(expr=   m.x157 + m.x257 >= -0.7794471)

m.c183 = Constraint(expr=   m.x158 + m.x258 >= -0.7794471)

m.c184 = Constraint(expr=   m.x155 + m.x259 >= -0.79930922)

m.c185 = Constraint(expr=   m.x156 + m.x260 >= -0.79930922)

m.c186 = Constraint(expr=   m.x157 + m.x261 >= -0.79930922)

m.c187 = Constraint(expr=   m.x158 + m.x262 >= -0.79930922)

m.c188 = Constraint(expr=   m.x155 + m.x263 >= -0.84280733)

m.c189 = Constraint(expr=   m.x156 + m.x264 >= -0.84280733)

m.c190 = Constraint(expr=   m.x157 + m.x265 >= -0.84280733)

m.c191 = Constraint(expr=   m.x158 + m.x266 >= -0.84280733)

m.c192 = Constraint(expr=   m.x155 + m.x267 >= -0.81379236)

m.c193 = Constraint(expr=   m.x156 + m.x268 >= -0.81379236)

m.c194 = Constraint(expr=   m.x157 + m.x269 >= -0.81379236)

m.c195 = Constraint(expr=   m.x158 + m.x270 >= -0.81379236)

m.c196 = Constraint(expr=   m.x155 + m.x271 >= -0.82457178)

m.c197 = Constraint(expr=   m.x156 + m.x272 >= -0.82457178)

m.c198 = Constraint(expr=   m.x157 + m.x273 >= -0.82457178)

m.c199 = Constraint(expr=   m.x158 + m.x274 >= -0.82457178)

m.c200 = Constraint(expr=   m.x155 + m.x275 >= -0.80226439)

m.c201 = Constraint(expr=   m.x156 + m.x276 >= -0.80226439)

m.c202 = Constraint(expr=   m.x157 + m.x277 >= -0.80226439)

m.c203 = Constraint(expr=   m.x158 + m.x278 >= -0.80226439)

m.c204 = Constraint(expr= - m.x155 + m.x219 >= 0.98493628)

m.c205 = Constraint(expr= - m.x156 + m.x220 >= 0.98493628)

m.c206 = Constraint(expr= - m.x157 + m.x221 >= 0.98493628)

m.c207 = Constraint(expr= - m.x158 + m.x222 >= 0.98493628)

m.c208 = Constraint(expr= - m.x155 + m.x223 >= 0.9536939)

m.c209 = Constraint(expr= - m.x156 + m.x224 >= 0.9536939)

m.c210 = Constraint(expr= - m.x157 + m.x225 >= 0.9536939)

m.c211 = Constraint(expr= - m.x158 + m.x226 >= 0.9536939)

m.c212 = Constraint(expr= - m.x155 + m.x227 >= 0.9004898)

m.c213 = Constraint(expr= - m.x156 + m.x228 >= 0.9004898)

m.c214 = Constraint(expr= - m.x157 + m.x229 >= 0.9004898)

m.c215 = Constraint(expr= - m.x158 + m.x230 >= 0.9004898)

m.c216 = Constraint(expr= - m.x155 + m.x231 >= 0.9114032)

m.c217 = Constraint(expr= - m.x156 + m.x232 >= 0.9114032)

m.c218 = Constraint(expr= - m.x157 + m.x233 >= 0.9114032)

m.c219 = Constraint(expr= - m.x158 + m.x234 >= 0.9114032)

m.c220 = Constraint(expr= - m.x155 + m.x235 >= 0.90071532)

m.c221 = Constraint(expr= - m.x156 + m.x236 >= 0.90071532)

m.c222 = Constraint(expr= - m.x157 + m.x237 >= 0.90071532)

m.c223 = Constraint(expr= - m.x158 + m.x238 >= 0.90071532)

m.c224 = Constraint(expr= - m.x155 + m.x239 >= 0.88043054)

m.c225 = Constraint(expr= - m.x156 + m.x240 >= 0.88043054)

m.c226 = Constraint(expr= - m.x157 + m.x241 >= 0.88043054)

m.c227 = Constraint(expr= - m.x158 + m.x242 >= 0.88043054)

m.c228 = Constraint(expr= - m.x155 + m.x243 >= 0.8680249)

m.c229 = Constraint(expr= - m.x156 + m.x244 >= 0.8680249)

m.c230 = Constraint(expr= - m.x157 + m.x245 >= 0.8680249)

m.c231 = Constraint(expr= - m.x158 + m.x246 >= 0.8680249)

m.c232 = Constraint(expr= - m.x155 + m.x247 >= 0.81034814)

m.c233 = Constraint(expr= - m.x156 + m.x248 >= 0.81034814)

m.c234 = Constraint(expr= - m.x157 + m.x249 >= 0.81034814)

m.c235 = Constraint(expr= - m.x158 + m.x250 >= 0.81034814)

m.c236 = Constraint(expr= - m.x155 + m.x251 >= 0.80843127)

m.c237 = Constraint(expr= - m.x156 + m.x252 >= 0.80843127)

m.c238 = Constraint(expr= - m.x157 + m.x253 >= 0.80843127)

m.c239 = Constraint(expr= - m.x158 + m.x254 >= 0.80843127)

m.c240 = Constraint(expr= - m.x155 + m.x259 >= 0.79930922)

m.c241 = Constraint(expr= - m.x156 + m.x260 >= 0.79930922)

m.c242 = Constraint(expr= - m.x157 + m.x261 >= 0.79930922)

m.c243 = Constraint(expr= - m.x158 + m.x262 >= 0.79930922)

m.c244 = Constraint(expr= - m.x155 + m.x263 >= 0.84280733)

m.c245 = Constraint(expr= - m.x156 + m.x264 >= 0.84280733)

m.c246 = Constraint(expr= - m.x157 + m.x265 >= 0.84280733)

m.c247 = Constraint(expr= - m.x158 + m.x266 >= 0.84280733)

m.c248 = Constraint(expr= - m.x155 + m.x267 >= 0.81379236)

m.c249 = Constraint(expr= - m.x156 + m.x268 >= 0.81379236)

m.c250 = Constraint(expr= - m.x157 + m.x269 >= 0.81379236)

m.c251 = Constraint(expr= - m.x158 + m.x270 >= 0.81379236)

m.c252 = Constraint(expr= - m.x155 + m.x271 >= 0.82457178)

m.c253 = Constraint(expr= - m.x156 + m.x272 >= 0.82457178)

m.c254 = Constraint(expr= - m.x157 + m.x273 >= 0.82457178)

m.c255 = Constraint(expr= - m.x158 + m.x274 >= 0.82457178)

m.c256 = Constraint(expr= - m.x155 + m.x275 >= 0.80226439)

m.c257 = Constraint(expr= - m.x156 + m.x276 >= 0.80226439)

m.c258 = Constraint(expr= - m.x157 + m.x277 >= 0.80226439)

m.c259 = Constraint(expr= - m.x158 + m.x278 >= 0.80226439)

m.c260 = Constraint(expr=   m.x61 - m.x159 - m.x219 == 0)

m.c261 = Constraint(expr=   m.x62 - m.x160 - m.x220 == 0)

m.c262 = Constraint(expr=   m.x63 - m.x161 - m.x221 == 0)

m.c263 = Constraint(expr=   m.x64 - m.x162 - m.x222 == 0)

m.c264 = Constraint(expr=   m.x65 - m.x163 - m.x223 == 0)

m.c265 = Constraint(expr=   m.x66 - m.x164 - m.x224 == 0)

m.c266 = Constraint(expr=   m.x67 - m.x165 - m.x225 == 0)

m.c267 = Constraint(expr=   m.x68 - m.x166 - m.x226 == 0)

m.c268 = Constraint(expr=   m.x69 - m.x167 - m.x227 == 0)

m.c269 = Constraint(expr=   m.x70 - m.x168 - m.x228 == 0)

m.c270 = Constraint(expr=   m.x71 - m.x169 - m.x229 == 0)

m.c271 = Constraint(expr=   m.x72 - m.x170 - m.x230 == 0)

m.c272 = Constraint(expr=   m.x73 - m.x171 - m.x231 == 0)

m.c273 = Constraint(expr=   m.x74 - m.x172 - m.x232 == 0)

m.c274 = Constraint(expr=   m.x75 - m.x173 - m.x233 == 0)

m.c275 = Constraint(expr=   m.x76 - m.x174 - m.x234 == 0)

m.c276 = Constraint(expr=   m.x77 - m.x175 - m.x235 == 0)

m.c277 = Constraint(expr=   m.x78 - m.x176 - m.x236 == 0)

m.c278 = Constraint(expr=   m.x79 - m.x177 - m.x237 == 0)

m.c279 = Constraint(expr=   m.x80 - m.x178 - m.x238 == 0)

m.c280 = Constraint(expr=   m.x81 - m.x179 - m.x239 == 0)

m.c281 = Constraint(expr=   m.x82 - m.x180 - m.x240 == 0)

m.c282 = Constraint(expr=   m.x83 - m.x181 - m.x241 == 0)

m.c283 = Constraint(expr=   m.x84 - m.x182 - m.x242 == 0)

m.c284 = Constraint(expr=   m.x85 - m.x183 - m.x243 == 0)

m.c285 = Constraint(expr=   m.x86 - m.x184 - m.x244 == 0)

m.c286 = Constraint(expr=   m.x87 - m.x185 - m.x245 == 0)

m.c287 = Constraint(expr=   m.x88 - m.x186 - m.x246 == 0)

m.c288 = Constraint(expr=   m.x89 - m.x187 - m.x247 == 0)

m.c289 = Constraint(expr=   m.x90 - m.x188 - m.x248 == 0)

m.c290 = Constraint(expr=   m.x91 - m.x189 - m.x249 == 0)

m.c291 = Constraint(expr=   m.x92 - m.x190 - m.x250 == 0)

m.c292 = Constraint(expr=   m.x93 - m.x191 - m.x251 == 0)

m.c293 = Constraint(expr=   m.x94 - m.x192 - m.x252 == 0)

m.c294 = Constraint(expr=   m.x95 - m.x193 - m.x253 == 0)

m.c295 = Constraint(expr=   m.x96 - m.x194 - m.x254 == 0)

m.c296 = Constraint(expr=   m.x97 - m.x195 - m.x255 == 0)

m.c297 = Constraint(expr=   m.x98 - m.x196 - m.x256 == 0)

m.c298 = Constraint(expr=   m.x99 - m.x197 - m.x257 == 0)

m.c299 = Constraint(expr=   m.x100 - m.x198 - m.x258 == 0)

m.c300 = Constraint(expr=   m.x101 - m.x199 - m.x259 == 0)

m.c301 = Constraint(expr=   m.x102 - m.x200 - m.x260 == 0)

m.c302 = Constraint(expr=   m.x103 - m.x201 - m.x261 == 0)

m.c303 = Constraint(expr=   m.x104 - m.x202 - m.x262 == 0)

m.c304 = Constraint(expr=   m.x105 - m.x203 - m.x263 == 0)

m.c305 = Constraint(expr=   m.x106 - m.x204 - m.x264 == 0)

m.c306 = Constraint(expr=   m.x107 - m.x205 - m.x265 == 0)

m.c307 = Constraint(expr=   m.x108 - m.x206 - m.x266 == 0)

m.c308 = Constraint(expr=   m.x109 - m.x207 - m.x267 == 0)

m.c309 = Constraint(expr=   m.x110 - m.x208 - m.x268 == 0)

m.c310 = Constraint(expr=   m.x111 - m.x209 - m.x269 == 0)

m.c311 = Constraint(expr=   m.x112 - m.x210 - m.x270 == 0)

m.c312 = Constraint(expr=   m.x113 - m.x211 - m.x271 == 0)

m.c313 = Constraint(expr=   m.x114 - m.x212 - m.x272 == 0)

m.c314 = Constraint(expr=   m.x115 - m.x213 - m.x273 == 0)

m.c315 = Constraint(expr=   m.x116 - m.x214 - m.x274 == 0)

m.c316 = Constraint(expr=   m.x117 - m.x215 - m.x275 == 0)

m.c317 = Constraint(expr=   m.x118 - m.x216 - m.x276 == 0)

m.c318 = Constraint(expr=   m.x119 - m.x217 - m.x277 == 0)

m.c319 = Constraint(expr=   m.x120 - m.x218 - m.x278 == 0)

m.c320 = Constraint(expr=   m.b301 + m.b302 >= 1)

m.c321 = Constraint(expr=   m.b299 + m.b304 >= 1)

m.c322 = Constraint(expr=   m.b298 + m.b302 >= 1)

m.c323 = Constraint(expr=   m.b298 + m.b301 + m.b303 >= 1)

m.c324 = Constraint(expr=   m.b298 + m.b300 + m.b304 >= 1)

m.c325 = Constraint(expr=   m.b298 + m.b299 >= 1)

m.c326 = Constraint(expr=   m.b297 + m.b304 >= 1)

m.c327 = Constraint(expr=   m.b297 + m.b301 >= 1)

m.c328 = Constraint(expr=   m.b296 + m.b303 >= 1)

m.c329 = Constraint(expr=   m.b296 + m.b301 + m.b304 >= 1)

m.c330 = Constraint(expr=   m.b296 + m.b300 >= 1)

m.c331 = Constraint(expr=   m.b296 + m.b298 + m.b304 >= 1)

m.c332 = Constraint(expr=   m.b296 + m.b298 + m.b301 >= 1)

m.c333 = Constraint(expr=   m.b296 + m.b297 >= 1)

m.c334 = Constraint(expr=   m.b295 + m.b303 >= 1)

m.c335 = Constraint(expr=   m.b295 + m.b301 + m.b304 >= 1)

m.c336 = Constraint(expr=   m.b295 + m.b300 >= 1)

m.c337 = Constraint(expr=   m.b295 + m.b298 >= 1)

m.c338 = Constraint(expr=   m.b295 + m.b296 >= 1)

m.c339 = Constraint(expr=   m.b294 + m.b303 >= 1)

m.c340 = Constraint(expr=   m.b294 + m.b301 + m.b304 >= 1)

m.c341 = Constraint(expr=   m.b294 + m.b300 >= 1)

m.c342 = Constraint(expr=   m.b294 + m.b298 + m.b304 >= 1)

m.c343 = Constraint(expr=   m.b294 + m.b298 + m.b301 >= 1)

m.c344 = Constraint(expr=   m.b294 + m.b297 >= 1)

m.c345 = Constraint(expr=   m.b294 + m.b296 >= 1)

m.c346 = Constraint(expr=   m.b294 + m.b295 >= 1)

m.c347 = Constraint(expr=   m.b304 + m.b309 >= 1)

m.c348 = Constraint(expr=   m.b304 + m.b308 + m.b310 >= 1)

m.c349 = Constraint(expr=   m.b304 + m.b307 + m.b311 >= 1)

m.c350 = Constraint(expr=   m.b304 + m.b306 >= 1)

m.c351 = Constraint(expr=   m.b304 + m.b305 + m.b311 >= 1)

m.c352 = Constraint(expr=   m.b304 + m.b305 + m.b308 >= 1)

m.c353 = Constraint(expr=   m.b303 + m.b310 >= 1)

m.c354 = Constraint(expr=   m.b303 + m.b308 + m.b311 >= 1)

m.c355 = Constraint(expr=   m.b303 + m.b307 >= 1)

m.c356 = Constraint(expr=   m.b303 + m.b305 >= 1)

m.c357 = Constraint(expr=   m.b302 + m.b311 >= 1)

m.c358 = Constraint(expr=   m.b302 + m.b308 >= 1)

m.c359 = Constraint(expr=   m.b302 + m.b305 >= 1)

m.c360 = Constraint(expr=   m.b301 + m.b309 >= 1)

m.c361 = Constraint(expr=   m.b301 + m.b308 + m.b310 >= 1)

m.c362 = Constraint(expr=   m.b301 + m.b307 + m.b311 >= 1)

m.c363 = Constraint(expr=   m.b301 + m.b306 >= 1)

m.c364 = Constraint(expr=   m.b301 + m.b305 + m.b311 >= 1)

m.c365 = Constraint(expr=   m.b301 + m.b305 + m.b308 >= 1)

m.c366 = Constraint(expr=   m.b301 + m.b304 + m.b310 >= 1)

m.c367 = Constraint(expr=   m.b301 + m.b304 + m.b308 + m.b311 >= 1)

m.c368 = Constraint(expr=   m.b301 + m.b304 + m.b307 >= 1)

m.c369 = Constraint(expr=   m.b301 + m.b304 + m.b305 >= 1)

m.c370 = Constraint(expr=   m.b301 + m.b303 + m.b311 >= 1)

m.c371 = Constraint(expr=   m.b301 + m.b303 + m.b308 >= 1)

m.c372 = Constraint(expr=   m.b301 + m.b303 + m.b305 >= 1)

m.c373 = Constraint(expr=   m.b300 + m.b310 >= 1)

m.c374 = Constraint(expr=   m.b300 + m.b308 + m.b311 >= 1)

m.c375 = Constraint(expr=   m.b300 + m.b307 >= 1)

m.c376 = Constraint(expr=   m.b300 + m.b305 >= 1)

m.c377 = Constraint(expr=   m.b300 + m.b304 + m.b311 >= 1)

m.c378 = Constraint(expr=   m.b300 + m.b304 + m.b308 >= 1)

m.c379 = Constraint(expr=   m.b300 + m.b304 + m.b305 >= 1)

m.c380 = Constraint(expr=   m.b300 + m.b303 + m.b311 >= 1)

m.c381 = Constraint(expr=   m.b300 + m.b303 + m.b308 >= 1)

m.c382 = Constraint(expr=   m.b300 + m.b303 + m.b305 >= 1)

m.c383 = Constraint(expr=   m.b299 + m.b311 >= 1)

m.c384 = Constraint(expr=   m.b299 + m.b308 >= 1)

m.c385 = Constraint(expr=   m.b299 + m.b305 >= 1)

m.c386 = Constraint(expr=   m.b298 + m.b309 >= 1)

m.c387 = Constraint(expr=   m.b298 + m.b308 + m.b310 >= 1)

m.c388 = Constraint(expr=   m.b298 + m.b307 + m.b311 >= 1)

m.c389 = Constraint(expr=   m.b298 + m.b306 >= 1)

m.c390 = Constraint(expr=   m.b298 + m.b305 + m.b311 >= 1)

m.c391 = Constraint(expr=   m.b298 + m.b305 + m.b308 >= 1)

m.c392 = Constraint(expr=   m.b298 + m.b304 + m.b310 >= 1)

m.c393 = Constraint(expr=   m.b298 + m.b304 + m.b308 + m.b311 >= 1)

m.c394 = Constraint(expr=   m.b298 + m.b304 + m.b307 >= 1)

m.c395 = Constraint(expr=   m.b298 + m.b304 + m.b305 >= 1)

m.c396 = Constraint(expr=   m.b298 + m.b303 + m.b311 >= 1)

m.c397 = Constraint(expr=   m.b298 + m.b303 + m.b308 >= 1)

m.c398 = Constraint(expr=   m.b298 + m.b303 + m.b305 >= 1)

m.c399 = Constraint(expr=   m.b298 + m.b301 + m.b310 >= 1)

m.c400 = Constraint(expr=   m.b298 + m.b301 + m.b308 + m.b311 >= 1)

m.c401 = Constraint(expr=   m.b298 + m.b301 + m.b307 >= 1)

m.c402 = Constraint(expr=   m.b298 + m.b301 + m.b305 >= 1)

m.c403 = Constraint(expr=   m.b298 + m.b301 + m.b304 + m.b311 >= 1)

m.c404 = Constraint(expr=   m.b298 + m.b301 + m.b304 + m.b308 >= 1)

m.c405 = Constraint(expr=   m.b298 + m.b301 + m.b304 + m.b305 >= 1)

m.c406 = Constraint(expr=   m.b298 + m.b300 + m.b311 >= 1)

m.c407 = Constraint(expr=   m.b298 + m.b300 + m.b308 >= 1)

m.c408 = Constraint(expr=   m.b298 + m.b300 + m.b305 >= 1)

m.c409 = Constraint(expr=   m.b297 + m.b311 >= 1)

m.c410 = Constraint(expr=   m.b297 + m.b308 >= 1)

m.c411 = Constraint(expr=   m.b297 + m.b305 >= 1)

m.c412 = Constraint(expr=   m.b296 + m.b310 >= 1)

m.c413 = Constraint(expr=   m.b296 + m.b308 + m.b311 >= 1)

m.c414 = Constraint(expr=   m.b296 + m.b307 >= 1)

m.c415 = Constraint(expr=   m.b296 + m.b305 >= 1)

m.c416 = Constraint(expr=   m.b296 + m.b304 + m.b311 >= 1)

m.c417 = Constraint(expr=   m.b296 + m.b304 + m.b308 >= 1)

m.c418 = Constraint(expr=   m.b296 + m.b304 + m.b305 >= 1)

m.c419 = Constraint(expr=   m.b296 + m.b301 + m.b311 >= 1)

m.c420 = Constraint(expr=   m.b296 + m.b301 + m.b308 >= 1)

m.c421 = Constraint(expr=   m.b296 + m.b301 + m.b305 >= 1)

m.c422 = Constraint(expr=   m.b296 + m.b298 + m.b311 >= 1)

m.c423 = Constraint(expr=   m.b296 + m.b298 + m.b308 >= 1)

m.c424 = Constraint(expr=   m.b296 + m.b298 + m.b305 >= 1)

m.c425 = Constraint(expr=   m.b295 + m.b310 >= 1)

m.c426 = Constraint(expr=   m.b295 + m.b308 + m.b311 >= 1)

m.c427 = Constraint(expr=   m.b295 + m.b307 >= 1)

m.c428 = Constraint(expr=   m.b295 + m.b305 >= 1)

m.c429 = Constraint(expr=   m.b295 + m.b304 + m.b311 >= 1)

m.c430 = Constraint(expr=   m.b295 + m.b304 + m.b308 >= 1)

m.c431 = Constraint(expr=   m.b295 + m.b304 + m.b305 >= 1)

m.c432 = Constraint(expr=   m.b295 + m.b301 + m.b311 >= 1)

m.c433 = Constraint(expr=   m.b295 + m.b301 + m.b308 >= 1)

m.c434 = Constraint(expr=   m.b295 + m.b301 + m.b305 >= 1)

m.c435 = Constraint(expr=   m.b294 + m.b310 >= 1)

m.c436 = Constraint(expr=   m.b294 + m.b308 + m.b311 >= 1)

m.c437 = Constraint(expr=   m.b294 + m.b307 >= 1)

m.c438 = Constraint(expr=   m.b294 + m.b305 >= 1)

m.c439 = Constraint(expr=   m.b294 + m.b304 + m.b311 >= 1)

m.c440 = Constraint(expr=   m.b294 + m.b304 + m.b308 >= 1)

m.c441 = Constraint(expr=   m.b294 + m.b304 + m.b305 >= 1)

m.c442 = Constraint(expr=   m.b294 + m.b301 + m.b311 >= 1)

m.c443 = Constraint(expr=   m.b294 + m.b301 + m.b308 >= 1)

m.c444 = Constraint(expr=   m.b294 + m.b301 + m.b305 >= 1)

m.c445 = Constraint(expr=   m.b294 + m.b298 + m.b311 >= 1)

m.c446 = Constraint(expr=   m.b294 + m.b298 + m.b308 >= 1)

m.c447 = Constraint(expr=   m.b294 + m.b298 + m.b305 >= 1)

m.c448 = Constraint(expr=   m.b297 - m.b298 >= 0)

m.c449 = Constraint(expr=   m.b299 - m.b300 >= 0)

m.c450 = Constraint(expr=   m.b300 - m.b301 >= 0)

m.c451 = Constraint(expr=   m.b302 - m.b303 >= 0)

m.c452 = Constraint(expr=   m.b303 - m.b304 >= 0)

m.c453 = Constraint(expr=   m.b306 - m.b307 >= 0)

m.c454 = Constraint(expr=   m.b307 - m.b308 >= 0)

m.c455 = Constraint(expr=   m.b309 - m.b310 >= 0)

m.c456 = Constraint(expr=   m.b310 - m.b311 >= 0)

m.c457 = Constraint(expr=   m.b312 - m.b313 >= 0)

m.c458 = Constraint(expr=   m.b313 - m.b314 >= 0)

m.c459 = Constraint(expr=   m.b314 - m.b315 >= 0)

m.c460 = Constraint(expr=   m.b316 - m.b317 >= 0)

m.c461 = Constraint(expr=   m.b317 - m.b318 >= 0)

m.c462 = Constraint(expr=   m.b322 - m.b323 >= 0)

m.c463 = Constraint(expr=   m.x155 - m.x156 >= 0)

m.c464 = Constraint(expr=   m.x156 - m.x157 >= 0)

m.c465 = Constraint(expr=   m.x157 - m.x158 >= 0)

m.c466 = Constraint(expr=   m.x121 - 0.1*m.b294 == 1.92)

m.c467 = Constraint(expr=   m.x122 - 0.193333333333333*m.b295 == 3.82)

m.c468 = Constraint(expr=   m.x123 - 0.226666666666667*m.b296 == 4.53333333333333)

m.c469 = Constraint(expr=   m.x124 - 0.286666666666667*m.b297 - 0.28*m.b298 == 5.39333333333333)

m.c470 = Constraint(expr=   m.x125 - 1.91333333333333*m.b299 - 1.91333333333333*m.b300 - 1.91333333333333*m.b301
                          == 36.3533333333333)

m.c471 = Constraint(expr=   m.x126 - 4.50666666666667*m.b302 - 4.51333333333333*m.b303 - 4.51333333333333*m.b304
                          == 85.7466666666667)

m.c472 = Constraint(expr=   m.x127 - 0.313333333333333*m.b305 == 6.28)

m.c473 = Constraint(expr=   m.x128 - 2.80666666666667*m.b306 - 2.81333333333333*m.b307 - 2.81333333333333*m.b308
                          == 53.4333333333333)

m.c474 = Constraint(expr=   m.x129 - 2.56*m.b309 - 2.56*m.b310 - 2.55333333333333*m.b311 == 48.6133333333333)

m.c475 = Constraint(expr=   m.x130 - 1.88666666666667*m.b312 - 1.88666666666667*m.b313 - 1.88666666666667*m.b314
                          - 1.88666666666667*m.b315 == 33.9533333333333)

m.c476 = Constraint(expr=   m.x131 - 2.84*m.b316 - 2.84*m.b317 - 2.84666666666667*m.b318 == 53.9666666666667)

m.c477 = Constraint(expr=   m.x132 - 3.85333333333333*m.b319 == 77.0533333333333)

m.c478 = Constraint(expr=   m.x133 - 1.24*m.b320 == 24.9066666666667)

m.c479 = Constraint(expr=   m.x134 - 1.81333333333333*m.b321 == 36.1866666666667)

m.c480 = Constraint(expr=   m.x135 - 2.96*m.b322 - 2.96666666666667*m.b323 == 56.3133333333333)

m.c481 = Constraint(expr= - m.x136 + m.x279 <= 0)

m.c482 = Constraint(expr= - m.x137 + m.x280 <= 0)

m.c483 = Constraint(expr= - m.x138 + m.x281 <= 0)

m.c484 = Constraint(expr= - m.x139 + m.x282 <= 0)

m.c485 = Constraint(expr= - m.x140 + m.x283 <= 0)

m.c486 = Constraint(expr= - m.x141 + m.x284 <= 0)

m.c487 = Constraint(expr= - m.x142 + m.x285 <= 0)

m.c488 = Constraint(expr= - m.x143 + m.x286 <= 0)

m.c489 = Constraint(expr= - m.x144 + m.x287 <= 0)

m.c490 = Constraint(expr= - m.x145 + m.x288 <= 0)

m.c491 = Constraint(expr= - m.x146 + m.x289 <= 0)

m.c492 = Constraint(expr= - m.x147 + m.x290 <= 0)

m.c493 = Constraint(expr= - m.x148 + m.x291 <= 0)

m.c494 = Constraint(expr= - m.x149 + m.x292 <= 0)

m.c495 = Constraint(expr= - m.x150 + m.x293 <= 0)
