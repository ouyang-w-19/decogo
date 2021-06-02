#  MINLP written by GAMS Convert at 04/21/18 13:54:10
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       2235      106     2110       19        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        356      294       62        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       8025     7890      135        0
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
m.b324 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b325 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b326 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b327 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b328 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b329 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b330 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b331 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b332 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b333 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b334 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b335 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b336 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b337 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b338 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b339 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b340 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b341 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b342 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b343 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b344 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b345 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b346 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b347 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b348 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b349 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b350 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b351 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b352 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b353 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b354 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b355 = Var(within=Binary,bounds=(0,1),initialize=0)

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

m.c320 = Constraint(expr=   m.b312 + m.b313 >= 1)

m.c321 = Constraint(expr=   m.b309 + m.b314 >= 1)

m.c322 = Constraint(expr=   m.b308 + m.b315 >= 1)

m.c323 = Constraint(expr=   m.b307 + m.b318 >= 1)

m.c324 = Constraint(expr=   m.b306 + m.b313 >= 1)

m.c325 = Constraint(expr=   m.b306 + m.b311 + m.b314 >= 1)

m.c326 = Constraint(expr=   m.b306 + m.b309 + m.b316 >= 1)

m.c327 = Constraint(expr=   m.b306 + m.b308 + m.b317 >= 1)

m.c328 = Constraint(expr=   m.b306 + m.b307 >= 1)

m.c329 = Constraint(expr=   m.b305 + m.b313 >= 1)

m.c330 = Constraint(expr=   m.b305 + m.b312 + m.b314 >= 1)

m.c331 = Constraint(expr=   m.b305 + m.b311 + m.b315 >= 1)

m.c332 = Constraint(expr=   m.b305 + m.b310 + m.b316 >= 1)

m.c333 = Constraint(expr=   m.b305 + m.b309 + m.b317 >= 1)

m.c334 = Constraint(expr=   m.b305 + m.b308 + m.b318 >= 1)

m.c335 = Constraint(expr=   m.b305 + m.b307 >= 1)

m.c336 = Constraint(expr=   m.b304 + m.b315 >= 1)

m.c337 = Constraint(expr=   m.b304 + m.b312 + m.b316 >= 1)

m.c338 = Constraint(expr=   m.b304 + m.b311 + m.b317 >= 1)

m.c339 = Constraint(expr=   m.b304 + m.b310 + m.b318 >= 1)

m.c340 = Constraint(expr=   m.b304 + m.b309 >= 1)

m.c341 = Constraint(expr=   m.b303 + m.b318 >= 1)

m.c342 = Constraint(expr=   m.b303 + m.b312 >= 1)

m.c343 = Constraint(expr=   m.b302 + m.b313 >= 1)

m.c344 = Constraint(expr=   m.b302 + m.b312 + m.b314 >= 1)

m.c345 = Constraint(expr=   m.b302 + m.b310 + m.b315 >= 1)

m.c346 = Constraint(expr=   m.b302 + m.b309 + m.b316 >= 1)

m.c347 = Constraint(expr=   m.b302 + m.b308 + m.b318 >= 1)

m.c348 = Constraint(expr=   m.b302 + m.b307 >= 1)

m.c349 = Constraint(expr=   m.b302 + m.b306 + m.b314 >= 1)

m.c350 = Constraint(expr=   m.b302 + m.b306 + m.b312 + m.b315 >= 1)

m.c351 = Constraint(expr=   m.b302 + m.b306 + m.b311 + m.b316 >= 1)

m.c352 = Constraint(expr=   m.b302 + m.b306 + m.b310 + m.b317 >= 1)

m.c353 = Constraint(expr=   m.b302 + m.b306 + m.b309 + m.b318 >= 1)

m.c354 = Constraint(expr=   m.b302 + m.b306 + m.b308 >= 1)

m.c355 = Constraint(expr=   m.b302 + m.b305 + m.b316 >= 1)

m.c356 = Constraint(expr=   m.b302 + m.b305 + m.b312 + m.b317 >= 1)

m.c357 = Constraint(expr=   m.b302 + m.b305 + m.b311 + m.b318 >= 1)

m.c358 = Constraint(expr=   m.b302 + m.b305 + m.b310 >= 1)

m.c359 = Constraint(expr=   m.b302 + m.b304 + m.b318 >= 1)

m.c360 = Constraint(expr=   m.b302 + m.b304 + m.b312 >= 1)

m.c361 = Constraint(expr=   m.b302 + m.b303 >= 1)

m.c362 = Constraint(expr=   m.b301 + m.b315 >= 1)

m.c363 = Constraint(expr=   m.b301 + m.b312 + m.b316 >= 1)

m.c364 = Constraint(expr=   m.b301 + m.b311 + m.b317 >= 1)

m.c365 = Constraint(expr=   m.b301 + m.b310 + m.b318 >= 1)

m.c366 = Constraint(expr=   m.b301 + m.b309 >= 1)

m.c367 = Constraint(expr=   m.b301 + m.b306 + m.b317 >= 1)

m.c368 = Constraint(expr=   m.b301 + m.b306 + m.b312 + m.b318 >= 1)

m.c369 = Constraint(expr=   m.b301 + m.b306 + m.b311 >= 1)

m.c370 = Constraint(expr=   m.b301 + m.b305 + m.b318 >= 1)

m.c371 = Constraint(expr=   m.b301 + m.b305 + m.b312 >= 1)

m.c372 = Constraint(expr=   m.b301 + m.b304 >= 1)

m.c373 = Constraint(expr=   m.b300 + m.b318 >= 1)

m.c374 = Constraint(expr=   m.b300 + m.b312 >= 1)

m.c375 = Constraint(expr=   m.b300 + m.b306 >= 1)

m.c376 = Constraint(expr=   m.b299 + m.b313 >= 1)

m.c377 = Constraint(expr=   m.b299 + m.b312 + m.b314 >= 1)

m.c378 = Constraint(expr=   m.b299 + m.b311 + m.b315 >= 1)

m.c379 = Constraint(expr=   m.b299 + m.b310 + m.b316 >= 1)

m.c380 = Constraint(expr=   m.b299 + m.b309 + m.b317 >= 1)

m.c381 = Constraint(expr=   m.b299 + m.b308 + m.b318 >= 1)

m.c382 = Constraint(expr=   m.b299 + m.b307 >= 1)

m.c383 = Constraint(expr=   m.b299 + m.b306 + m.b314 >= 1)

m.c384 = Constraint(expr=   m.b299 + m.b306 + m.b312 + m.b315 >= 1)

m.c385 = Constraint(expr=   m.b299 + m.b306 + m.b311 + m.b316 >= 1)

m.c386 = Constraint(expr=   m.b299 + m.b306 + m.b310 + m.b317 >= 1)

m.c387 = Constraint(expr=   m.b299 + m.b306 + m.b309 + m.b318 >= 1)

m.c388 = Constraint(expr=   m.b299 + m.b306 + m.b308 >= 1)

m.c389 = Constraint(expr=   m.b299 + m.b305 + m.b316 >= 1)

m.c390 = Constraint(expr=   m.b299 + m.b305 + m.b312 + m.b317 >= 1)

m.c391 = Constraint(expr=   m.b299 + m.b305 + m.b311 + m.b318 >= 1)

m.c392 = Constraint(expr=   m.b299 + m.b305 + m.b310 >= 1)

m.c393 = Constraint(expr=   m.b299 + m.b304 + m.b318 >= 1)

m.c394 = Constraint(expr=   m.b299 + m.b304 + m.b312 >= 1)

m.c395 = Constraint(expr=   m.b299 + m.b303 >= 1)

m.c396 = Constraint(expr=   m.b299 + m.b302 + m.b315 >= 1)

m.c397 = Constraint(expr=   m.b299 + m.b302 + m.b312 + m.b316 >= 1)

m.c398 = Constraint(expr=   m.b299 + m.b302 + m.b311 + m.b317 >= 1)

m.c399 = Constraint(expr=   m.b299 + m.b302 + m.b310 + m.b318 >= 1)

m.c400 = Constraint(expr=   m.b299 + m.b302 + m.b309 >= 1)

m.c401 = Constraint(expr=   m.b299 + m.b302 + m.b306 + m.b316 >= 1)

m.c402 = Constraint(expr=   m.b299 + m.b302 + m.b306 + m.b312 + m.b318 >= 1)

m.c403 = Constraint(expr=   m.b299 + m.b302 + m.b306 + m.b310 >= 1)

m.c404 = Constraint(expr=   m.b299 + m.b302 + m.b305 + m.b318 >= 1)

m.c405 = Constraint(expr=   m.b299 + m.b302 + m.b305 + m.b312 >= 1)

m.c406 = Constraint(expr=   m.b299 + m.b302 + m.b304 >= 1)

m.c407 = Constraint(expr=   m.b299 + m.b301 + m.b318 >= 1)

m.c408 = Constraint(expr=   m.b299 + m.b301 + m.b312 >= 1)

m.c409 = Constraint(expr=   m.b299 + m.b301 + m.b306 >= 1)

m.c410 = Constraint(expr=   m.b299 + m.b300 >= 1)

m.c411 = Constraint(expr=   m.b298 + m.b315 >= 1)

m.c412 = Constraint(expr=   m.b298 + m.b312 + m.b316 >= 1)

m.c413 = Constraint(expr=   m.b298 + m.b311 + m.b317 >= 1)

m.c414 = Constraint(expr=   m.b298 + m.b310 + m.b318 >= 1)

m.c415 = Constraint(expr=   m.b298 + m.b309 >= 1)

m.c416 = Constraint(expr=   m.b298 + m.b306 + m.b317 >= 1)

m.c417 = Constraint(expr=   m.b298 + m.b306 + m.b312 + m.b318 >= 1)

m.c418 = Constraint(expr=   m.b298 + m.b306 + m.b310 >= 1)

m.c419 = Constraint(expr=   m.b298 + m.b305 + m.b318 >= 1)

m.c420 = Constraint(expr=   m.b298 + m.b305 + m.b312 >= 1)

m.c421 = Constraint(expr=   m.b298 + m.b304 >= 1)

m.c422 = Constraint(expr=   m.b298 + m.b302 + m.b318 >= 1)

m.c423 = Constraint(expr=   m.b298 + m.b302 + m.b311 >= 1)

m.c424 = Constraint(expr=   m.b298 + m.b302 + m.b306 >= 1)

m.c425 = Constraint(expr=   m.b298 + m.b301 >= 1)

m.c426 = Constraint(expr=   m.b297 + m.b318 >= 1)

m.c427 = Constraint(expr=   m.b297 + m.b312 >= 1)

m.c428 = Constraint(expr=   m.b297 + m.b306 >= 1)

m.c429 = Constraint(expr=   m.b297 + m.b302 >= 1)

m.c430 = Constraint(expr=   m.b296 + m.b313 >= 1)

m.c431 = Constraint(expr=   m.b296 + m.b311 + m.b314 >= 1)

m.c432 = Constraint(expr=   m.b296 + m.b310 + m.b315 >= 1)

m.c433 = Constraint(expr=   m.b296 + m.b309 + m.b316 >= 1)

m.c434 = Constraint(expr=   m.b296 + m.b308 + m.b318 >= 1)

m.c435 = Constraint(expr=   m.b296 + m.b307 >= 1)

m.c436 = Constraint(expr=   m.b296 + m.b306 + m.b314 >= 1)

m.c437 = Constraint(expr=   m.b296 + m.b306 + m.b312 + m.b315 >= 1)

m.c438 = Constraint(expr=   m.b296 + m.b306 + m.b311 + m.b316 >= 1)

m.c439 = Constraint(expr=   m.b296 + m.b306 + m.b310 + m.b317 >= 1)

m.c440 = Constraint(expr=   m.b296 + m.b306 + m.b309 + m.b318 >= 1)

m.c441 = Constraint(expr=   m.b296 + m.b306 + m.b308 >= 1)

m.c442 = Constraint(expr=   m.b296 + m.b305 + m.b316 >= 1)

m.c443 = Constraint(expr=   m.b296 + m.b305 + m.b312 + m.b317 >= 1)

m.c444 = Constraint(expr=   m.b296 + m.b305 + m.b311 + m.b318 >= 1)

m.c445 = Constraint(expr=   m.b296 + m.b305 + m.b310 >= 1)

m.c446 = Constraint(expr=   m.b296 + m.b304 + m.b318 >= 1)

m.c447 = Constraint(expr=   m.b296 + m.b304 + m.b311 >= 1)

m.c448 = Constraint(expr=   m.b296 + m.b303 >= 1)

m.c449 = Constraint(expr=   m.b296 + m.b302 + m.b315 >= 1)

m.c450 = Constraint(expr=   m.b296 + m.b302 + m.b312 + m.b316 >= 1)

m.c451 = Constraint(expr=   m.b296 + m.b302 + m.b311 + m.b317 >= 1)

m.c452 = Constraint(expr=   m.b296 + m.b302 + m.b310 + m.b318 >= 1)

m.c453 = Constraint(expr=   m.b296 + m.b302 + m.b309 >= 1)

m.c454 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b316 >= 1)

m.c455 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b312 + m.b317 >= 1)

m.c456 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b311 + m.b318 >= 1)

m.c457 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b310 >= 1)

m.c458 = Constraint(expr=   m.b296 + m.b302 + m.b305 + m.b318 >= 1)

m.c459 = Constraint(expr=   m.b296 + m.b302 + m.b305 + m.b312 >= 1)

m.c460 = Constraint(expr=   m.b296 + m.b302 + m.b304 >= 1)

m.c461 = Constraint(expr=   m.b296 + m.b301 + m.b318 >= 1)

m.c462 = Constraint(expr=   m.b296 + m.b301 + m.b312 >= 1)

m.c463 = Constraint(expr=   m.b296 + m.b301 + m.b306 >= 1)

m.c464 = Constraint(expr=   m.b296 + m.b300 >= 1)

m.c465 = Constraint(expr=   m.b296 + m.b299 + m.b315 >= 1)

m.c466 = Constraint(expr=   m.b296 + m.b299 + m.b312 + m.b316 >= 1)

m.c467 = Constraint(expr=   m.b296 + m.b299 + m.b311 + m.b317 >= 1)

m.c468 = Constraint(expr=   m.b296 + m.b299 + m.b310 + m.b318 >= 1)

m.c469 = Constraint(expr=   m.b296 + m.b299 + m.b309 >= 1)

m.c470 = Constraint(expr=   m.b296 + m.b299 + m.b306 + m.b316 >= 1)

m.c471 = Constraint(expr=   m.b296 + m.b299 + m.b306 + m.b312 + m.b318 >= 1)

m.c472 = Constraint(expr=   m.b296 + m.b299 + m.b306 + m.b311 >= 1)

m.c473 = Constraint(expr=   m.b296 + m.b299 + m.b305 + m.b318 >= 1)

m.c474 = Constraint(expr=   m.b296 + m.b299 + m.b305 + m.b312 >= 1)

m.c475 = Constraint(expr=   m.b296 + m.b299 + m.b304 >= 1)

m.c476 = Constraint(expr=   m.b296 + m.b299 + m.b302 + m.b317 >= 1)

m.c477 = Constraint(expr=   m.b296 + m.b299 + m.b302 + m.b312 + m.b318 >= 1)

m.c478 = Constraint(expr=   m.b296 + m.b299 + m.b302 + m.b311 >= 1)

m.c479 = Constraint(expr=   m.b296 + m.b299 + m.b302 + m.b306 >= 1)

m.c480 = Constraint(expr=   m.b296 + m.b299 + m.b301 >= 1)

m.c481 = Constraint(expr=   m.b296 + m.b298 + m.b318 >= 1)

m.c482 = Constraint(expr=   m.b296 + m.b298 + m.b312 >= 1)

m.c483 = Constraint(expr=   m.b296 + m.b298 + m.b306 >= 1)

m.c484 = Constraint(expr=   m.b296 + m.b298 + m.b302 >= 1)

m.c485 = Constraint(expr=   m.b296 + m.b297 >= 1)

m.c486 = Constraint(expr=   m.b295 + m.b315 >= 1)

m.c487 = Constraint(expr=   m.b295 + m.b312 + m.b316 >= 1)

m.c488 = Constraint(expr=   m.b295 + m.b311 + m.b317 >= 1)

m.c489 = Constraint(expr=   m.b295 + m.b310 + m.b318 >= 1)

m.c490 = Constraint(expr=   m.b295 + m.b309 >= 1)

m.c491 = Constraint(expr=   m.b295 + m.b306 + m.b317 >= 1)

m.c492 = Constraint(expr=   m.b295 + m.b306 + m.b312 + m.b318 >= 1)

m.c493 = Constraint(expr=   m.b295 + m.b306 + m.b311 >= 1)

m.c494 = Constraint(expr=   m.b295 + m.b305 + m.b318 >= 1)

m.c495 = Constraint(expr=   m.b295 + m.b305 + m.b312 >= 1)

m.c496 = Constraint(expr=   m.b295 + m.b304 >= 1)

m.c497 = Constraint(expr=   m.b295 + m.b302 + m.b318 >= 1)

m.c498 = Constraint(expr=   m.b295 + m.b302 + m.b312 >= 1)

m.c499 = Constraint(expr=   m.b295 + m.b302 + m.b306 >= 1)

m.c500 = Constraint(expr=   m.b295 + m.b301 >= 1)

m.c501 = Constraint(expr=   m.b295 + m.b299 + m.b318 >= 1)

m.c502 = Constraint(expr=   m.b295 + m.b299 + m.b312 >= 1)

m.c503 = Constraint(expr=   m.b295 + m.b299 + m.b306 >= 1)

m.c504 = Constraint(expr=   m.b295 + m.b299 + m.b302 >= 1)

m.c505 = Constraint(expr=   m.b295 + m.b298 >= 1)

m.c506 = Constraint(expr=   m.b294 + m.b318 >= 1)

m.c507 = Constraint(expr=   m.b294 + m.b312 >= 1)

m.c508 = Constraint(expr=   m.b294 + m.b306 >= 1)

m.c509 = Constraint(expr=   m.b294 + m.b302 >= 1)

m.c510 = Constraint(expr=   m.b294 + m.b299 >= 1)

m.c511 = Constraint(expr=   m.b318 + m.b327 >= 1)

m.c512 = Constraint(expr=   m.b318 + m.b325 + m.b328 >= 1)

m.c513 = Constraint(expr=   m.b318 + m.b324 + m.b329 >= 1)

m.c514 = Constraint(expr=   m.b318 + m.b323 + m.b330 >= 1)

m.c515 = Constraint(expr=   m.b318 + m.b322 >= 1)

m.c516 = Constraint(expr=   m.b318 + m.b321 + m.b328 >= 1)

m.c517 = Constraint(expr=   m.b318 + m.b321 + m.b326 + m.b329 >= 1)

m.c518 = Constraint(expr=   m.b318 + m.b321 + m.b324 + m.b331 >= 1)

m.c519 = Constraint(expr=   m.b318 + m.b321 + m.b323 >= 1)

m.c520 = Constraint(expr=   m.b318 + m.b320 + m.b330 >= 1)

m.c521 = Constraint(expr=   m.b318 + m.b320 + m.b326 + m.b331 >= 1)

m.c522 = Constraint(expr=   m.b318 + m.b320 + m.b325 >= 1)

m.c523 = Constraint(expr=   m.b318 + m.b319 >= 1)

m.c524 = Constraint(expr=   m.b317 + m.b327 >= 1)

m.c525 = Constraint(expr=   m.b317 + m.b325 + m.b328 >= 1)

m.c526 = Constraint(expr=   m.b317 + m.b324 + m.b329 >= 1)

m.c527 = Constraint(expr=   m.b317 + m.b323 + m.b330 >= 1)

m.c528 = Constraint(expr=   m.b317 + m.b322 >= 1)

m.c529 = Constraint(expr=   m.b317 + m.b321 + m.b328 >= 1)

m.c530 = Constraint(expr=   m.b317 + m.b321 + m.b326 + m.b329 >= 1)

m.c531 = Constraint(expr=   m.b317 + m.b321 + m.b325 + m.b330 >= 1)

m.c532 = Constraint(expr=   m.b317 + m.b321 + m.b324 + m.b331 >= 1)

m.c533 = Constraint(expr=   m.b317 + m.b321 + m.b323 >= 1)

m.c534 = Constraint(expr=   m.b317 + m.b320 + m.b330 >= 1)

m.c535 = Constraint(expr=   m.b317 + m.b320 + m.b326 + m.b331 >= 1)

m.c536 = Constraint(expr=   m.b317 + m.b320 + m.b325 >= 1)

m.c537 = Constraint(expr=   m.b317 + m.b319 >= 1)

m.c538 = Constraint(expr=   m.b316 + m.b327 >= 1)

m.c539 = Constraint(expr=   m.b316 + m.b326 + m.b328 >= 1)

m.c540 = Constraint(expr=   m.b316 + m.b325 + m.b329 >= 1)

m.c541 = Constraint(expr=   m.b316 + m.b324 + m.b330 >= 1)

m.c542 = Constraint(expr=   m.b316 + m.b323 + m.b331 >= 1)

m.c543 = Constraint(expr=   m.b316 + m.b322 >= 1)

m.c544 = Constraint(expr=   m.b316 + m.b321 + m.b329 >= 1)

m.c545 = Constraint(expr=   m.b316 + m.b321 + m.b326 + m.b330 >= 1)

m.c546 = Constraint(expr=   m.b316 + m.b321 + m.b325 + m.b331 >= 1)

m.c547 = Constraint(expr=   m.b316 + m.b321 + m.b324 >= 1)

m.c548 = Constraint(expr=   m.b316 + m.b320 + m.b331 >= 1)

m.c549 = Constraint(expr=   m.b316 + m.b320 + m.b326 >= 1)

m.c550 = Constraint(expr=   m.b316 + m.b319 >= 1)

m.c551 = Constraint(expr=   m.b315 + m.b328 >= 1)

m.c552 = Constraint(expr=   m.b315 + m.b326 + m.b329 >= 1)

m.c553 = Constraint(expr=   m.b315 + m.b325 + m.b330 >= 1)

m.c554 = Constraint(expr=   m.b315 + m.b324 + m.b331 >= 1)

m.c555 = Constraint(expr=   m.b315 + m.b323 >= 1)

m.c556 = Constraint(expr=   m.b315 + m.b321 + m.b330 >= 1)

m.c557 = Constraint(expr=   m.b315 + m.b321 + m.b326 + m.b331 >= 1)

m.c558 = Constraint(expr=   m.b315 + m.b321 + m.b325 >= 1)

m.c559 = Constraint(expr=   m.b315 + m.b320 >= 1)

m.c560 = Constraint(expr=   m.b314 + m.b329 >= 1)

m.c561 = Constraint(expr=   m.b314 + m.b326 + m.b330 >= 1)

m.c562 = Constraint(expr=   m.b314 + m.b325 + m.b331 >= 1)

m.c563 = Constraint(expr=   m.b314 + m.b324 >= 1)

m.c564 = Constraint(expr=   m.b314 + m.b321 + m.b331 >= 1)

m.c565 = Constraint(expr=   m.b314 + m.b321 + m.b326 >= 1)

m.c566 = Constraint(expr=   m.b314 + m.b320 >= 1)

m.c567 = Constraint(expr=   m.b313 + m.b331 >= 1)

m.c568 = Constraint(expr=   m.b313 + m.b326 >= 1)

m.c569 = Constraint(expr=   m.b313 + m.b321 >= 1)

m.c570 = Constraint(expr=   m.b312 + m.b327 >= 1)

m.c571 = Constraint(expr=   m.b312 + m.b325 + m.b328 >= 1)

m.c572 = Constraint(expr=   m.b312 + m.b324 + m.b329 >= 1)

m.c573 = Constraint(expr=   m.b312 + m.b322 >= 1)

m.c574 = Constraint(expr=   m.b312 + m.b321 + m.b328 >= 1)

m.c575 = Constraint(expr=   m.b312 + m.b321 + m.b326 + m.b329 >= 1)

m.c576 = Constraint(expr=   m.b312 + m.b321 + m.b324 + m.b331 >= 1)

m.c577 = Constraint(expr=   m.b312 + m.b321 + m.b323 >= 1)

m.c578 = Constraint(expr=   m.b312 + m.b320 + m.b330 >= 1)

m.c579 = Constraint(expr=   m.b312 + m.b320 + m.b326 + m.b331 >= 1)

m.c580 = Constraint(expr=   m.b312 + m.b320 + m.b325 >= 1)

m.c581 = Constraint(expr=   m.b312 + m.b319 >= 1)

m.c582 = Constraint(expr=   m.b312 + m.b318 + m.b327 >= 1)

m.c583 = Constraint(expr=   m.b312 + m.b318 + m.b325 + m.b328 >= 1)

m.c584 = Constraint(expr=   m.b312 + m.b318 + m.b324 + m.b329 >= 1)

m.c585 = Constraint(expr=   m.b312 + m.b318 + m.b323 + m.b331 >= 1)

m.c586 = Constraint(expr=   m.b312 + m.b318 + m.b322 >= 1)

m.c587 = Constraint(expr=   m.b312 + m.b318 + m.b321 + m.b328 >= 1)

m.c588 = Constraint(expr=   m.b312 + m.b318 + m.b321 + m.b326 + m.b329 >= 1)

m.c589 = Constraint(expr=   m.b312 + m.b318 + m.b321 + m.b325 + m.b330 >= 1)

m.c590 = Constraint(expr=   m.b312 + m.b318 + m.b321 + m.b324 + m.b331 >= 1)

m.c591 = Constraint(expr=   m.b312 + m.b318 + m.b321 + m.b323 >= 1)

m.c592 = Constraint(expr=   m.b312 + m.b318 + m.b320 + m.b330 >= 1)

m.c593 = Constraint(expr=   m.b312 + m.b318 + m.b320 + m.b326 + m.b331 >= 1)

m.c594 = Constraint(expr=   m.b312 + m.b318 + m.b320 + m.b325 >= 1)

m.c595 = Constraint(expr=   m.b312 + m.b318 + m.b319 >= 1)

m.c596 = Constraint(expr=   m.b312 + m.b317 + m.b327 >= 1)

m.c597 = Constraint(expr=   m.b312 + m.b317 + m.b326 + m.b328 >= 1)

m.c598 = Constraint(expr=   m.b312 + m.b317 + m.b325 + m.b329 >= 1)

m.c599 = Constraint(expr=   m.b312 + m.b317 + m.b324 + m.b330 >= 1)

m.c600 = Constraint(expr=   m.b312 + m.b317 + m.b323 + m.b331 >= 1)

m.c601 = Constraint(expr=   m.b312 + m.b317 + m.b322 >= 1)

m.c602 = Constraint(expr=   m.b312 + m.b317 + m.b321 + m.b329 >= 1)

m.c603 = Constraint(expr=   m.b312 + m.b317 + m.b321 + m.b326 + m.b330 >= 1)

m.c604 = Constraint(expr=   m.b312 + m.b317 + m.b321 + m.b325 + m.b331 >= 1)

m.c605 = Constraint(expr=   m.b312 + m.b317 + m.b321 + m.b324 >= 1)

m.c606 = Constraint(expr=   m.b312 + m.b317 + m.b320 + m.b331 >= 1)

m.c607 = Constraint(expr=   m.b312 + m.b317 + m.b320 + m.b326 >= 1)

m.c608 = Constraint(expr=   m.b312 + m.b317 + m.b319 >= 1)

m.c609 = Constraint(expr=   m.b312 + m.b316 + m.b328 >= 1)

m.c610 = Constraint(expr=   m.b312 + m.b316 + m.b326 + m.b329 >= 1)

m.c611 = Constraint(expr=   m.b312 + m.b316 + m.b325 + m.b330 >= 1)

m.c612 = Constraint(expr=   m.b312 + m.b316 + m.b324 + m.b331 >= 1)

m.c613 = Constraint(expr=   m.b312 + m.b316 + m.b323 >= 1)

m.c614 = Constraint(expr=   m.b312 + m.b316 + m.b321 + m.b330 >= 1)

m.c615 = Constraint(expr=   m.b312 + m.b316 + m.b321 + m.b326 + m.b331 >= 1)

m.c616 = Constraint(expr=   m.b312 + m.b316 + m.b321 + m.b325 >= 1)

m.c617 = Constraint(expr=   m.b312 + m.b316 + m.b320 >= 1)

m.c618 = Constraint(expr=   m.b312 + m.b315 + m.b329 >= 1)

m.c619 = Constraint(expr=   m.b312 + m.b315 + m.b326 + m.b330 >= 1)

m.c620 = Constraint(expr=   m.b312 + m.b315 + m.b325 + m.b331 >= 1)

m.c621 = Constraint(expr=   m.b312 + m.b315 + m.b324 >= 1)

m.c622 = Constraint(expr=   m.b312 + m.b315 + m.b321 + m.b331 >= 1)

m.c623 = Constraint(expr=   m.b312 + m.b315 + m.b321 + m.b326 >= 1)

m.c624 = Constraint(expr=   m.b312 + m.b315 + m.b320 >= 1)

m.c625 = Constraint(expr=   m.b312 + m.b314 + m.b330 >= 1)

m.c626 = Constraint(expr=   m.b312 + m.b314 + m.b326 + m.b331 >= 1)

m.c627 = Constraint(expr=   m.b312 + m.b314 + m.b325 >= 1)

m.c628 = Constraint(expr=   m.b312 + m.b314 + m.b321 >= 1)

m.c629 = Constraint(expr=   m.b311 + m.b327 >= 1)

m.c630 = Constraint(expr=   m.b311 + m.b325 + m.b328 >= 1)

m.c631 = Constraint(expr=   m.b311 + m.b324 + m.b329 >= 1)

m.c632 = Constraint(expr=   m.b311 + m.b323 + m.b330 >= 1)

m.c633 = Constraint(expr=   m.b311 + m.b322 >= 1)

m.c634 = Constraint(expr=   m.b311 + m.b321 + m.b328 >= 1)

m.c635 = Constraint(expr=   m.b311 + m.b321 + m.b326 + m.b329 >= 1)

m.c636 = Constraint(expr=   m.b311 + m.b321 + m.b325 + m.b330 >= 1)

m.c637 = Constraint(expr=   m.b311 + m.b321 + m.b324 + m.b331 >= 1)

m.c638 = Constraint(expr=   m.b311 + m.b321 + m.b323 >= 1)

m.c639 = Constraint(expr=   m.b311 + m.b320 + m.b330 >= 1)

m.c640 = Constraint(expr=   m.b311 + m.b320 + m.b326 + m.b331 >= 1)

m.c641 = Constraint(expr=   m.b311 + m.b320 + m.b325 >= 1)

m.c642 = Constraint(expr=   m.b311 + m.b319 >= 1)

m.c643 = Constraint(expr=   m.b311 + m.b318 + m.b327 >= 1)

m.c644 = Constraint(expr=   m.b311 + m.b318 + m.b326 + m.b328 >= 1)

m.c645 = Constraint(expr=   m.b311 + m.b318 + m.b325 + m.b329 >= 1)

m.c646 = Constraint(expr=   m.b311 + m.b318 + m.b324 + m.b330 >= 1)

m.c647 = Constraint(expr=   m.b311 + m.b318 + m.b323 + m.b331 >= 1)

m.c648 = Constraint(expr=   m.b311 + m.b318 + m.b322 >= 1)

m.c649 = Constraint(expr=   m.b311 + m.b318 + m.b321 + m.b329 >= 1)

m.c650 = Constraint(expr=   m.b311 + m.b318 + m.b321 + m.b326 + m.b330 >= 1)

m.c651 = Constraint(expr=   m.b311 + m.b318 + m.b321 + m.b325 + m.b331 >= 1)

m.c652 = Constraint(expr=   m.b311 + m.b318 + m.b321 + m.b324 >= 1)

m.c653 = Constraint(expr=   m.b311 + m.b318 + m.b320 + m.b331 >= 1)

m.c654 = Constraint(expr=   m.b311 + m.b318 + m.b320 + m.b326 >= 1)

m.c655 = Constraint(expr=   m.b311 + m.b318 + m.b319 >= 1)

m.c656 = Constraint(expr=   m.b311 + m.b317 + m.b328 >= 1)

m.c657 = Constraint(expr=   m.b311 + m.b317 + m.b326 + m.b329 >= 1)

m.c658 = Constraint(expr=   m.b311 + m.b317 + m.b325 + m.b330 >= 1)

m.c659 = Constraint(expr=   m.b311 + m.b317 + m.b324 + m.b331 >= 1)

m.c660 = Constraint(expr=   m.b311 + m.b317 + m.b323 >= 1)

m.c661 = Constraint(expr=   m.b311 + m.b317 + m.b321 + m.b330 >= 1)

m.c662 = Constraint(expr=   m.b311 + m.b317 + m.b321 + m.b326 + m.b331 >= 1)

m.c663 = Constraint(expr=   m.b311 + m.b317 + m.b321 + m.b325 >= 1)

m.c664 = Constraint(expr=   m.b311 + m.b317 + m.b320 >= 1)

m.c665 = Constraint(expr=   m.b311 + m.b316 + m.b329 >= 1)

m.c666 = Constraint(expr=   m.b311 + m.b316 + m.b326 + m.b330 >= 1)

m.c667 = Constraint(expr=   m.b311 + m.b316 + m.b325 + m.b331 >= 1)

m.c668 = Constraint(expr=   m.b311 + m.b316 + m.b324 >= 1)

m.c669 = Constraint(expr=   m.b311 + m.b316 + m.b321 + m.b331 >= 1)

m.c670 = Constraint(expr=   m.b311 + m.b316 + m.b321 + m.b326 >= 1)

m.c671 = Constraint(expr=   m.b311 + m.b316 + m.b320 >= 1)

m.c672 = Constraint(expr=   m.b311 + m.b315 + m.b329 >= 1)

m.c673 = Constraint(expr=   m.b311 + m.b315 + m.b326 + m.b331 >= 1)

m.c674 = Constraint(expr=   m.b311 + m.b315 + m.b325 >= 1)

m.c675 = Constraint(expr=   m.b311 + m.b315 + m.b321 >= 1)

m.c676 = Constraint(expr=   m.b311 + m.b314 + m.b330 >= 1)

m.c677 = Constraint(expr=   m.b311 + m.b314 + m.b326 + m.b331 >= 1)

m.c678 = Constraint(expr=   m.b311 + m.b314 + m.b325 >= 1)

m.c679 = Constraint(expr=   m.b311 + m.b314 + m.b321 >= 1)

m.c680 = Constraint(expr=   m.b310 + m.b327 >= 1)

m.c681 = Constraint(expr=   m.b310 + m.b326 + m.b328 >= 1)

m.c682 = Constraint(expr=   m.b310 + m.b325 + m.b329 >= 1)

m.c683 = Constraint(expr=   m.b310 + m.b324 + m.b330 >= 1)

m.c684 = Constraint(expr=   m.b310 + m.b323 + m.b331 >= 1)

m.c685 = Constraint(expr=   m.b310 + m.b322 >= 1)

m.c686 = Constraint(expr=   m.b310 + m.b321 + m.b329 >= 1)

m.c687 = Constraint(expr=   m.b310 + m.b321 + m.b326 + m.b330 >= 1)

m.c688 = Constraint(expr=   m.b310 + m.b321 + m.b325 + m.b331 >= 1)

m.c689 = Constraint(expr=   m.b310 + m.b321 + m.b324 >= 1)

m.c690 = Constraint(expr=   m.b310 + m.b320 + m.b331 >= 1)

m.c691 = Constraint(expr=   m.b310 + m.b320 + m.b326 >= 1)

m.c692 = Constraint(expr=   m.b310 + m.b319 >= 1)

m.c693 = Constraint(expr=   m.b310 + m.b318 + m.b328 >= 1)

m.c694 = Constraint(expr=   m.b310 + m.b318 + m.b326 + m.b329 >= 1)

m.c695 = Constraint(expr=   m.b310 + m.b318 + m.b325 + m.b330 >= 1)

m.c696 = Constraint(expr=   m.b310 + m.b318 + m.b324 + m.b331 >= 1)

m.c697 = Constraint(expr=   m.b310 + m.b318 + m.b323 >= 1)

m.c698 = Constraint(expr=   m.b310 + m.b318 + m.b321 + m.b330 >= 1)

m.c699 = Constraint(expr=   m.b310 + m.b318 + m.b321 + m.b326 + m.b331 >= 1)

m.c700 = Constraint(expr=   m.b310 + m.b318 + m.b321 + m.b325 >= 1)

m.c701 = Constraint(expr=   m.b310 + m.b318 + m.b320 >= 1)

m.c702 = Constraint(expr=   m.b310 + m.b317 + m.b329 >= 1)

m.c703 = Constraint(expr=   m.b310 + m.b317 + m.b326 + m.b330 >= 1)

m.c704 = Constraint(expr=   m.b310 + m.b317 + m.b325 + m.b331 >= 1)

m.c705 = Constraint(expr=   m.b310 + m.b317 + m.b324 >= 1)

m.c706 = Constraint(expr=   m.b310 + m.b317 + m.b321 + m.b331 >= 1)

m.c707 = Constraint(expr=   m.b310 + m.b317 + m.b321 + m.b326 >= 1)

m.c708 = Constraint(expr=   m.b310 + m.b317 + m.b320 >= 1)

m.c709 = Constraint(expr=   m.b310 + m.b316 + m.b329 >= 1)

m.c710 = Constraint(expr=   m.b310 + m.b316 + m.b326 + m.b330 >= 1)

m.c711 = Constraint(expr=   m.b310 + m.b316 + m.b325 + m.b331 >= 1)

m.c712 = Constraint(expr=   m.b310 + m.b316 + m.b324 >= 1)

m.c713 = Constraint(expr=   m.b310 + m.b316 + m.b321 + m.b331 >= 1)

m.c714 = Constraint(expr=   m.b310 + m.b316 + m.b321 + m.b326 >= 1)

m.c715 = Constraint(expr=   m.b310 + m.b316 + m.b320 >= 1)

m.c716 = Constraint(expr=   m.b310 + m.b315 + m.b330 >= 1)

m.c717 = Constraint(expr=   m.b310 + m.b315 + m.b326 + m.b331 >= 1)

m.c718 = Constraint(expr=   m.b310 + m.b315 + m.b325 >= 1)

m.c719 = Constraint(expr=   m.b310 + m.b315 + m.b321 >= 1)

m.c720 = Constraint(expr=   m.b310 + m.b314 + m.b331 >= 1)

m.c721 = Constraint(expr=   m.b310 + m.b314 + m.b326 >= 1)

m.c722 = Constraint(expr=   m.b310 + m.b314 + m.b321 >= 1)

m.c723 = Constraint(expr=   m.b309 + m.b328 >= 1)

m.c724 = Constraint(expr=   m.b309 + m.b326 + m.b329 >= 1)

m.c725 = Constraint(expr=   m.b309 + m.b325 + m.b330 >= 1)

m.c726 = Constraint(expr=   m.b309 + m.b324 + m.b331 >= 1)

m.c727 = Constraint(expr=   m.b309 + m.b323 >= 1)

m.c728 = Constraint(expr=   m.b309 + m.b321 + m.b330 >= 1)

m.c729 = Constraint(expr=   m.b309 + m.b321 + m.b326 + m.b331 >= 1)

m.c730 = Constraint(expr=   m.b309 + m.b321 + m.b325 >= 1)

m.c731 = Constraint(expr=   m.b309 + m.b320 >= 1)

m.c732 = Constraint(expr=   m.b309 + m.b318 + m.b329 >= 1)

m.c733 = Constraint(expr=   m.b309 + m.b318 + m.b326 + m.b330 >= 1)

m.c734 = Constraint(expr=   m.b309 + m.b318 + m.b325 + m.b331 >= 1)

m.c735 = Constraint(expr=   m.b309 + m.b318 + m.b324 >= 1)

m.c736 = Constraint(expr=   m.b309 + m.b318 + m.b321 + m.b331 >= 1)

m.c737 = Constraint(expr=   m.b309 + m.b318 + m.b321 + m.b326 >= 1)

m.c738 = Constraint(expr=   m.b309 + m.b318 + m.b320 >= 1)

m.c739 = Constraint(expr=   m.b309 + m.b317 + m.b329 >= 1)

m.c740 = Constraint(expr=   m.b309 + m.b317 + m.b326 + m.b330 >= 1)

m.c741 = Constraint(expr=   m.b309 + m.b317 + m.b325 >= 1)

m.c742 = Constraint(expr=   m.b309 + m.b317 + m.b321 + m.b331 >= 1)

m.c743 = Constraint(expr=   m.b309 + m.b317 + m.b321 + m.b326 >= 1)

m.c744 = Constraint(expr=   m.b309 + m.b317 + m.b320 >= 1)

m.c745 = Constraint(expr=   m.b309 + m.b316 + m.b330 >= 1)

m.c746 = Constraint(expr=   m.b309 + m.b316 + m.b326 + m.b331 >= 1)

m.c747 = Constraint(expr=   m.b309 + m.b316 + m.b325 >= 1)

m.c748 = Constraint(expr=   m.b309 + m.b316 + m.b321 >= 1)

m.c749 = Constraint(expr=   m.b309 + m.b315 + m.b331 >= 1)

m.c750 = Constraint(expr=   m.b309 + m.b315 + m.b326 >= 1)

m.c751 = Constraint(expr=   m.b309 + m.b315 + m.b321 >= 1)

m.c752 = Constraint(expr=   m.b308 + m.b329 >= 1)

m.c753 = Constraint(expr=   m.b308 + m.b326 + m.b330 >= 1)

m.c754 = Constraint(expr=   m.b308 + m.b325 + m.b331 >= 1)

m.c755 = Constraint(expr=   m.b308 + m.b324 >= 1)

m.c756 = Constraint(expr=   m.b308 + m.b321 + m.b331 >= 1)

m.c757 = Constraint(expr=   m.b308 + m.b321 + m.b326 >= 1)

m.c758 = Constraint(expr=   m.b308 + m.b320 >= 1)

m.c759 = Constraint(expr=   m.b308 + m.b318 + m.b329 >= 1)

m.c760 = Constraint(expr=   m.b308 + m.b318 + m.b326 + m.b331 >= 1)

m.c761 = Constraint(expr=   m.b308 + m.b318 + m.b325 >= 1)

m.c762 = Constraint(expr=   m.b308 + m.b318 + m.b321 >= 1)

m.c763 = Constraint(expr=   m.b308 + m.b317 + m.b330 >= 1)

m.c764 = Constraint(expr=   m.b308 + m.b317 + m.b326 + m.b331 >= 1)

m.c765 = Constraint(expr=   m.b308 + m.b317 + m.b325 >= 1)

m.c766 = Constraint(expr=   m.b308 + m.b317 + m.b321 >= 1)

m.c767 = Constraint(expr=   m.b308 + m.b316 + m.b331 >= 1)

m.c768 = Constraint(expr=   m.b308 + m.b316 + m.b326 >= 1)

m.c769 = Constraint(expr=   m.b308 + m.b316 + m.b321 >= 1)

m.c770 = Constraint(expr=   m.b307 + m.b331 >= 1)

m.c771 = Constraint(expr=   m.b307 + m.b326 >= 1)

m.c772 = Constraint(expr=   m.b307 + m.b321 >= 1)

m.c773 = Constraint(expr=   m.b306 + m.b327 >= 1)

m.c774 = Constraint(expr=   m.b306 + m.b325 + m.b328 >= 1)

m.c775 = Constraint(expr=   m.b306 + m.b324 + m.b329 >= 1)

m.c776 = Constraint(expr=   m.b306 + m.b323 + m.b330 >= 1)

m.c777 = Constraint(expr=   m.b306 + m.b322 >= 1)

m.c778 = Constraint(expr=   m.b306 + m.b321 + m.b328 >= 1)

m.c779 = Constraint(expr=   m.b306 + m.b321 + m.b326 + m.b329 >= 1)

m.c780 = Constraint(expr=   m.b306 + m.b321 + m.b325 + m.b330 >= 1)

m.c781 = Constraint(expr=   m.b306 + m.b321 + m.b324 + m.b331 >= 1)

m.c782 = Constraint(expr=   m.b306 + m.b321 + m.b323 >= 1)

m.c783 = Constraint(expr=   m.b306 + m.b320 + m.b330 >= 1)

m.c784 = Constraint(expr=   m.b306 + m.b320 + m.b326 + m.b331 >= 1)

m.c785 = Constraint(expr=   m.b306 + m.b320 + m.b325 >= 1)

m.c786 = Constraint(expr=   m.b306 + m.b319 >= 1)

m.c787 = Constraint(expr=   m.b306 + m.b318 + m.b327 >= 1)

m.c788 = Constraint(expr=   m.b306 + m.b318 + m.b326 + m.b328 >= 1)

m.c789 = Constraint(expr=   m.b306 + m.b318 + m.b325 + m.b329 >= 1)

m.c790 = Constraint(expr=   m.b306 + m.b318 + m.b324 + m.b330 >= 1)

m.c791 = Constraint(expr=   m.b306 + m.b318 + m.b323 + m.b331 >= 1)

m.c792 = Constraint(expr=   m.b306 + m.b318 + m.b322 >= 1)

m.c793 = Constraint(expr=   m.b306 + m.b318 + m.b321 + m.b329 >= 1)

m.c794 = Constraint(expr=   m.b306 + m.b318 + m.b321 + m.b326 + m.b330 >= 1)

m.c795 = Constraint(expr=   m.b306 + m.b318 + m.b321 + m.b325 + m.b331 >= 1)

m.c796 = Constraint(expr=   m.b306 + m.b318 + m.b321 + m.b324 >= 1)

m.c797 = Constraint(expr=   m.b306 + m.b318 + m.b320 + m.b331 >= 1)

m.c798 = Constraint(expr=   m.b306 + m.b318 + m.b320 + m.b326 >= 1)

m.c799 = Constraint(expr=   m.b306 + m.b318 + m.b319 >= 1)

m.c800 = Constraint(expr=   m.b306 + m.b317 + m.b328 >= 1)

m.c801 = Constraint(expr=   m.b306 + m.b317 + m.b325 + m.b329 >= 1)

m.c802 = Constraint(expr=   m.b306 + m.b317 + m.b324 + m.b331 >= 1)

m.c803 = Constraint(expr=   m.b306 + m.b317 + m.b323 >= 1)

m.c804 = Constraint(expr=   m.b306 + m.b317 + m.b321 + m.b329 >= 1)

m.c805 = Constraint(expr=   m.b306 + m.b317 + m.b321 + m.b326 + m.b330 >= 1)

m.c806 = Constraint(expr=   m.b306 + m.b317 + m.b321 + m.b325 + m.b331 >= 1)

m.c807 = Constraint(expr=   m.b306 + m.b317 + m.b321 + m.b324 >= 1)

m.c808 = Constraint(expr=   m.b306 + m.b317 + m.b320 + m.b331 >= 1)

m.c809 = Constraint(expr=   m.b306 + m.b317 + m.b320 + m.b326 >= 1)

m.c810 = Constraint(expr=   m.b306 + m.b317 + m.b319 >= 1)

m.c811 = Constraint(expr=   m.b306 + m.b316 + m.b328 >= 1)

m.c812 = Constraint(expr=   m.b306 + m.b316 + m.b326 + m.b329 >= 1)

m.c813 = Constraint(expr=   m.b306 + m.b316 + m.b325 + m.b330 >= 1)

m.c814 = Constraint(expr=   m.b306 + m.b316 + m.b324 + m.b331 >= 1)

m.c815 = Constraint(expr=   m.b306 + m.b316 + m.b323 >= 1)

m.c816 = Constraint(expr=   m.b306 + m.b316 + m.b321 + m.b330 >= 1)

m.c817 = Constraint(expr=   m.b306 + m.b316 + m.b321 + m.b326 + m.b331 >= 1)

m.c818 = Constraint(expr=   m.b306 + m.b316 + m.b321 + m.b325 >= 1)

m.c819 = Constraint(expr=   m.b306 + m.b316 + m.b320 >= 1)

m.c820 = Constraint(expr=   m.b306 + m.b315 + m.b329 >= 1)

m.c821 = Constraint(expr=   m.b306 + m.b315 + m.b326 + m.b330 >= 1)

m.c822 = Constraint(expr=   m.b306 + m.b315 + m.b325 + m.b331 >= 1)

m.c823 = Constraint(expr=   m.b306 + m.b315 + m.b324 >= 1)

m.c824 = Constraint(expr=   m.b306 + m.b315 + m.b321 + m.b331 >= 1)

m.c825 = Constraint(expr=   m.b306 + m.b315 + m.b321 + m.b326 >= 1)

m.c826 = Constraint(expr=   m.b306 + m.b315 + m.b320 >= 1)

m.c827 = Constraint(expr=   m.b306 + m.b314 + m.b330 >= 1)

m.c828 = Constraint(expr=   m.b306 + m.b314 + m.b326 + m.b331 >= 1)

m.c829 = Constraint(expr=   m.b306 + m.b314 + m.b325 >= 1)

m.c830 = Constraint(expr=   m.b306 + m.b314 + m.b321 >= 1)

m.c831 = Constraint(expr=   m.b306 + m.b312 + m.b327 >= 1)

m.c832 = Constraint(expr=   m.b306 + m.b312 + m.b326 + m.b328 >= 1)

m.c833 = Constraint(expr=   m.b306 + m.b312 + m.b325 + m.b329 >= 1)

m.c834 = Constraint(expr=   m.b306 + m.b312 + m.b324 + m.b330 >= 1)

m.c835 = Constraint(expr=   m.b306 + m.b312 + m.b323 + m.b331 >= 1)

m.c836 = Constraint(expr=   m.b306 + m.b312 + m.b322 >= 1)

m.c837 = Constraint(expr=   m.b306 + m.b312 + m.b321 + m.b329 >= 1)

m.c838 = Constraint(expr=   m.b306 + m.b312 + m.b321 + m.b326 + m.b330 >= 1)

m.c839 = Constraint(expr=   m.b306 + m.b312 + m.b321 + m.b325 + m.b331 >= 1)

m.c840 = Constraint(expr=   m.b306 + m.b312 + m.b321 + m.b324 >= 1)

m.c841 = Constraint(expr=   m.b306 + m.b312 + m.b320 + m.b331 >= 1)

m.c842 = Constraint(expr=   m.b306 + m.b312 + m.b320 + m.b326 >= 1)

m.c843 = Constraint(expr=   m.b306 + m.b312 + m.b319 >= 1)

m.c844 = Constraint(expr=   m.b306 + m.b312 + m.b318 + m.b328 >= 1)

m.c845 = Constraint(expr=   m.b306 + m.b312 + m.b318 + m.b326 + m.b329 >= 1)

m.c846 = Constraint(expr=   m.b306 + m.b312 + m.b318 + m.b325 + m.b330 >= 1)

m.c847 = Constraint(expr=   m.b306 + m.b312 + m.b318 + m.b324 + m.b331 >= 1)

m.c848 = Constraint(expr=   m.b306 + m.b312 + m.b318 + m.b323 >= 1)

m.c849 = Constraint(expr=   m.b306 + m.b312 + m.b318 + m.b321 + m.b330 >= 1)

m.c850 = Constraint(expr=   m.b306 + m.b312 + m.b318 + m.b321 + m.b326 + m.b331 >= 1)

m.c851 = Constraint(expr=   m.b306 + m.b312 + m.b318 + m.b321 + m.b325 >= 1)

m.c852 = Constraint(expr=   m.b306 + m.b312 + m.b318 + m.b320 >= 1)

m.c853 = Constraint(expr=   m.b306 + m.b312 + m.b317 + m.b328 >= 1)

m.c854 = Constraint(expr=   m.b306 + m.b312 + m.b317 + m.b326 + m.b329 >= 1)

m.c855 = Constraint(expr=   m.b306 + m.b312 + m.b317 + m.b325 + m.b330 >= 1)

m.c856 = Constraint(expr=   m.b306 + m.b312 + m.b317 + m.b324 + m.b331 >= 1)

m.c857 = Constraint(expr=   m.b306 + m.b312 + m.b317 + m.b323 >= 1)

m.c858 = Constraint(expr=   m.b306 + m.b312 + m.b317 + m.b321 + m.b330 >= 1)

m.c859 = Constraint(expr=   m.b306 + m.b312 + m.b317 + m.b321 + m.b326 + m.b331 >= 1)

m.c860 = Constraint(expr=   m.b306 + m.b312 + m.b317 + m.b321 + m.b325 >= 1)

m.c861 = Constraint(expr=   m.b306 + m.b312 + m.b317 + m.b320 >= 1)

m.c862 = Constraint(expr=   m.b306 + m.b312 + m.b316 + m.b329 >= 1)

m.c863 = Constraint(expr=   m.b306 + m.b312 + m.b316 + m.b326 + m.b330 >= 1)

m.c864 = Constraint(expr=   m.b306 + m.b312 + m.b316 + m.b325 + m.b331 >= 1)

m.c865 = Constraint(expr=   m.b306 + m.b312 + m.b316 + m.b324 >= 1)

m.c866 = Constraint(expr=   m.b306 + m.b312 + m.b316 + m.b321 + m.b331 >= 1)

m.c867 = Constraint(expr=   m.b306 + m.b312 + m.b316 + m.b321 + m.b326 >= 1)

m.c868 = Constraint(expr=   m.b306 + m.b312 + m.b316 + m.b320 >= 1)

m.c869 = Constraint(expr=   m.b306 + m.b312 + m.b315 + m.b330 >= 1)

m.c870 = Constraint(expr=   m.b306 + m.b312 + m.b315 + m.b326 + m.b331 >= 1)

m.c871 = Constraint(expr=   m.b306 + m.b312 + m.b315 + m.b325 >= 1)

m.c872 = Constraint(expr=   m.b306 + m.b312 + m.b315 + m.b321 >= 1)

m.c873 = Constraint(expr=   m.b306 + m.b312 + m.b314 + m.b331 >= 1)

m.c874 = Constraint(expr=   m.b306 + m.b312 + m.b314 + m.b326 >= 1)

m.c875 = Constraint(expr=   m.b306 + m.b312 + m.b314 + m.b321 >= 1)

m.c876 = Constraint(expr=   m.b306 + m.b311 + m.b327 >= 1)

m.c877 = Constraint(expr=   m.b306 + m.b311 + m.b326 + m.b328 >= 1)

m.c878 = Constraint(expr=   m.b306 + m.b311 + m.b325 + m.b329 >= 1)

m.c879 = Constraint(expr=   m.b306 + m.b311 + m.b324 + m.b331 >= 1)

m.c880 = Constraint(expr=   m.b306 + m.b311 + m.b323 >= 1)

m.c881 = Constraint(expr=   m.b306 + m.b311 + m.b321 + m.b329 >= 1)

m.c882 = Constraint(expr=   m.b306 + m.b311 + m.b321 + m.b326 + m.b330 >= 1)

m.c883 = Constraint(expr=   m.b306 + m.b311 + m.b321 + m.b325 + m.b331 >= 1)

m.c884 = Constraint(expr=   m.b306 + m.b311 + m.b321 + m.b324 >= 1)

m.c885 = Constraint(expr=   m.b306 + m.b311 + m.b320 >= 1)

m.c886 = Constraint(expr=   m.b306 + m.b311 + m.b318 + m.b328 >= 1)

m.c887 = Constraint(expr=   m.b306 + m.b311 + m.b318 + m.b326 + m.b329 >= 1)

m.c888 = Constraint(expr=   m.b306 + m.b311 + m.b318 + m.b325 + m.b330 >= 1)

m.c889 = Constraint(expr=   m.b306 + m.b311 + m.b318 + m.b324 + m.b331 >= 1)

m.c890 = Constraint(expr=   m.b306 + m.b311 + m.b318 + m.b323 >= 1)

m.c891 = Constraint(expr=   m.b306 + m.b311 + m.b318 + m.b321 + m.b330 >= 1)

m.c892 = Constraint(expr=   m.b306 + m.b311 + m.b318 + m.b321 + m.b326 + m.b331 >= 1)

m.c893 = Constraint(expr=   m.b306 + m.b311 + m.b318 + m.b321 + m.b325 >= 1)

m.c894 = Constraint(expr=   m.b306 + m.b311 + m.b318 + m.b320 >= 1)

m.c895 = Constraint(expr=   m.b306 + m.b311 + m.b317 + m.b329 >= 1)

m.c896 = Constraint(expr=   m.b306 + m.b311 + m.b317 + m.b326 + m.b330 >= 1)

m.c897 = Constraint(expr=   m.b306 + m.b311 + m.b317 + m.b325 + m.b331 >= 1)

m.c898 = Constraint(expr=   m.b306 + m.b311 + m.b317 + m.b324 >= 1)

m.c899 = Constraint(expr=   m.b306 + m.b311 + m.b317 + m.b321 + m.b331 >= 1)

m.c900 = Constraint(expr=   m.b306 + m.b311 + m.b317 + m.b321 + m.b326 >= 1)

m.c901 = Constraint(expr=   m.b306 + m.b311 + m.b317 + m.b320 >= 1)

m.c902 = Constraint(expr=   m.b306 + m.b311 + m.b316 + m.b330 >= 1)

m.c903 = Constraint(expr=   m.b306 + m.b311 + m.b316 + m.b326 + m.b331 >= 1)

m.c904 = Constraint(expr=   m.b306 + m.b311 + m.b316 + m.b325 >= 1)

m.c905 = Constraint(expr=   m.b306 + m.b311 + m.b316 + m.b321 >= 1)

m.c906 = Constraint(expr=   m.b306 + m.b311 + m.b315 + m.b331 >= 1)

m.c907 = Constraint(expr=   m.b306 + m.b311 + m.b315 + m.b326 >= 1)

m.c908 = Constraint(expr=   m.b306 + m.b311 + m.b315 + m.b321 >= 1)

m.c909 = Constraint(expr=   m.b306 + m.b310 + m.b328 >= 1)

m.c910 = Constraint(expr=   m.b306 + m.b310 + m.b326 + m.b329 >= 1)

m.c911 = Constraint(expr=   m.b306 + m.b310 + m.b325 + m.b330 >= 1)

m.c912 = Constraint(expr=   m.b306 + m.b310 + m.b324 + m.b331 >= 1)

m.c913 = Constraint(expr=   m.b306 + m.b310 + m.b323 >= 1)

m.c914 = Constraint(expr=   m.b306 + m.b310 + m.b321 + m.b330 >= 1)

m.c915 = Constraint(expr=   m.b306 + m.b310 + m.b321 + m.b326 + m.b331 >= 1)

m.c916 = Constraint(expr=   m.b306 + m.b310 + m.b321 + m.b325 >= 1)

m.c917 = Constraint(expr=   m.b306 + m.b310 + m.b320 >= 1)

m.c918 = Constraint(expr=   m.b306 + m.b310 + m.b318 + m.b329 >= 1)

m.c919 = Constraint(expr=   m.b306 + m.b310 + m.b318 + m.b326 + m.b330 >= 1)

m.c920 = Constraint(expr=   m.b306 + m.b310 + m.b318 + m.b325 + m.b331 >= 1)

m.c921 = Constraint(expr=   m.b306 + m.b310 + m.b318 + m.b324 >= 1)

m.c922 = Constraint(expr=   m.b306 + m.b310 + m.b318 + m.b321 + m.b331 >= 1)

m.c923 = Constraint(expr=   m.b306 + m.b310 + m.b318 + m.b321 + m.b326 >= 1)

m.c924 = Constraint(expr=   m.b306 + m.b310 + m.b318 + m.b320 >= 1)

m.c925 = Constraint(expr=   m.b306 + m.b310 + m.b317 + m.b330 >= 1)

m.c926 = Constraint(expr=   m.b306 + m.b310 + m.b317 + m.b326 + m.b331 >= 1)

m.c927 = Constraint(expr=   m.b306 + m.b310 + m.b317 + m.b325 >= 1)

m.c928 = Constraint(expr=   m.b306 + m.b310 + m.b317 + m.b321 >= 1)

m.c929 = Constraint(expr=   m.b306 + m.b310 + m.b316 + m.b331 >= 1)

m.c930 = Constraint(expr=   m.b306 + m.b310 + m.b316 + m.b326 >= 1)

m.c931 = Constraint(expr=   m.b306 + m.b310 + m.b316 + m.b321 >= 1)

m.c932 = Constraint(expr=   m.b306 + m.b310 + m.b315 + m.b331 >= 1)

m.c933 = Constraint(expr=   m.b306 + m.b310 + m.b315 + m.b326 >= 1)

m.c934 = Constraint(expr=   m.b306 + m.b310 + m.b315 + m.b321 >= 1)

m.c935 = Constraint(expr=   m.b306 + m.b309 + m.b329 >= 1)

m.c936 = Constraint(expr=   m.b306 + m.b309 + m.b326 + m.b330 >= 1)

m.c937 = Constraint(expr=   m.b306 + m.b309 + m.b325 + m.b331 >= 1)

m.c938 = Constraint(expr=   m.b306 + m.b309 + m.b324 >= 1)

m.c939 = Constraint(expr=   m.b306 + m.b309 + m.b321 + m.b331 >= 1)

m.c940 = Constraint(expr=   m.b306 + m.b309 + m.b321 + m.b326 >= 1)

m.c941 = Constraint(expr=   m.b306 + m.b309 + m.b320 >= 1)

m.c942 = Constraint(expr=   m.b306 + m.b309 + m.b318 + m.b330 >= 1)

m.c943 = Constraint(expr=   m.b306 + m.b309 + m.b318 + m.b326 + m.b331 >= 1)

m.c944 = Constraint(expr=   m.b306 + m.b309 + m.b318 + m.b325 >= 1)

m.c945 = Constraint(expr=   m.b306 + m.b309 + m.b318 + m.b321 >= 1)

m.c946 = Constraint(expr=   m.b306 + m.b309 + m.b317 + m.b331 >= 1)

m.c947 = Constraint(expr=   m.b306 + m.b309 + m.b317 + m.b326 >= 1)

m.c948 = Constraint(expr=   m.b306 + m.b309 + m.b317 + m.b321 >= 1)

m.c949 = Constraint(expr=   m.b306 + m.b308 + m.b330 >= 1)

m.c950 = Constraint(expr=   m.b306 + m.b308 + m.b326 + m.b331 >= 1)

m.c951 = Constraint(expr=   m.b306 + m.b308 + m.b325 >= 1)

m.c952 = Constraint(expr=   m.b306 + m.b308 + m.b321 >= 1)

m.c953 = Constraint(expr=   m.b306 + m.b308 + m.b318 + m.b331 >= 1)

m.c954 = Constraint(expr=   m.b306 + m.b308 + m.b318 + m.b326 >= 1)

m.c955 = Constraint(expr=   m.b306 + m.b308 + m.b318 + m.b321 >= 1)

m.c956 = Constraint(expr=   m.b305 + m.b327 >= 1)

m.c957 = Constraint(expr=   m.b305 + m.b326 + m.b328 >= 1)

m.c958 = Constraint(expr=   m.b305 + m.b325 + m.b329 >= 1)

m.c959 = Constraint(expr=   m.b305 + m.b324 + m.b330 >= 1)

m.c960 = Constraint(expr=   m.b305 + m.b323 + m.b331 >= 1)

m.c961 = Constraint(expr=   m.b305 + m.b322 >= 1)

m.c962 = Constraint(expr=   m.b305 + m.b321 + m.b329 >= 1)

m.c963 = Constraint(expr=   m.b305 + m.b321 + m.b326 + m.b330 >= 1)

m.c964 = Constraint(expr=   m.b305 + m.b321 + m.b325 + m.b331 >= 1)

m.c965 = Constraint(expr=   m.b305 + m.b321 + m.b324 >= 1)

m.c966 = Constraint(expr=   m.b305 + m.b320 + m.b331 >= 1)

m.c967 = Constraint(expr=   m.b305 + m.b320 + m.b326 >= 1)

m.c968 = Constraint(expr=   m.b305 + m.b319 >= 1)

m.c969 = Constraint(expr=   m.b305 + m.b318 + m.b328 >= 1)

m.c970 = Constraint(expr=   m.b305 + m.b318 + m.b326 + m.b329 >= 1)

m.c971 = Constraint(expr=   m.b305 + m.b318 + m.b325 + m.b330 >= 1)

m.c972 = Constraint(expr=   m.b305 + m.b318 + m.b324 + m.b331 >= 1)

m.c973 = Constraint(expr=   m.b305 + m.b318 + m.b323 >= 1)

m.c974 = Constraint(expr=   m.b305 + m.b318 + m.b321 + m.b330 >= 1)

m.c975 = Constraint(expr=   m.b305 + m.b318 + m.b321 + m.b326 + m.b331 >= 1)

m.c976 = Constraint(expr=   m.b305 + m.b318 + m.b321 + m.b325 >= 1)

m.c977 = Constraint(expr=   m.b305 + m.b318 + m.b320 >= 1)

m.c978 = Constraint(expr=   m.b305 + m.b317 + m.b329 >= 1)

m.c979 = Constraint(expr=   m.b305 + m.b317 + m.b326 + m.b330 >= 1)

m.c980 = Constraint(expr=   m.b305 + m.b317 + m.b325 + m.b331 >= 1)

m.c981 = Constraint(expr=   m.b305 + m.b317 + m.b324 >= 1)

m.c982 = Constraint(expr=   m.b305 + m.b317 + m.b321 + m.b331 >= 1)

m.c983 = Constraint(expr=   m.b305 + m.b317 + m.b321 + m.b326 >= 1)

m.c984 = Constraint(expr=   m.b305 + m.b317 + m.b320 >= 1)

m.c985 = Constraint(expr=   m.b305 + m.b316 + m.b330 >= 1)

m.c986 = Constraint(expr=   m.b305 + m.b316 + m.b326 + m.b331 >= 1)

m.c987 = Constraint(expr=   m.b305 + m.b316 + m.b325 >= 1)

m.c988 = Constraint(expr=   m.b305 + m.b316 + m.b321 >= 1)

m.c989 = Constraint(expr=   m.b305 + m.b315 + m.b331 >= 1)

m.c990 = Constraint(expr=   m.b305 + m.b315 + m.b326 >= 1)

m.c991 = Constraint(expr=   m.b305 + m.b315 + m.b321 >= 1)

m.c992 = Constraint(expr=   m.b305 + m.b314 + m.b331 >= 1)

m.c993 = Constraint(expr=   m.b305 + m.b314 + m.b326 >= 1)

m.c994 = Constraint(expr=   m.b305 + m.b314 + m.b321 >= 1)

m.c995 = Constraint(expr=   m.b305 + m.b312 + m.b328 >= 1)

m.c996 = Constraint(expr=   m.b305 + m.b312 + m.b326 + m.b329 >= 1)

m.c997 = Constraint(expr=   m.b305 + m.b312 + m.b325 + m.b330 >= 1)

m.c998 = Constraint(expr=   m.b305 + m.b312 + m.b324 + m.b331 >= 1)

m.c999 = Constraint(expr=   m.b305 + m.b312 + m.b323 >= 1)

m.c1000 = Constraint(expr=   m.b305 + m.b312 + m.b321 + m.b330 >= 1)

m.c1001 = Constraint(expr=   m.b305 + m.b312 + m.b321 + m.b326 + m.b331 >= 1)

m.c1002 = Constraint(expr=   m.b305 + m.b312 + m.b321 + m.b325 >= 1)

m.c1003 = Constraint(expr=   m.b305 + m.b312 + m.b320 >= 1)

m.c1004 = Constraint(expr=   m.b305 + m.b312 + m.b318 + m.b329 >= 1)

m.c1005 = Constraint(expr=   m.b305 + m.b312 + m.b318 + m.b326 + m.b330 >= 1)

m.c1006 = Constraint(expr=   m.b305 + m.b312 + m.b318 + m.b325 + m.b331 >= 1)

m.c1007 = Constraint(expr=   m.b305 + m.b312 + m.b318 + m.b324 >= 1)

m.c1008 = Constraint(expr=   m.b305 + m.b312 + m.b318 + m.b321 + m.b331 >= 1)

m.c1009 = Constraint(expr=   m.b305 + m.b312 + m.b318 + m.b321 + m.b326 >= 1)

m.c1010 = Constraint(expr=   m.b305 + m.b312 + m.b318 + m.b320 >= 1)

m.c1011 = Constraint(expr=   m.b305 + m.b312 + m.b317 + m.b330 >= 1)

m.c1012 = Constraint(expr=   m.b305 + m.b312 + m.b317 + m.b326 + m.b331 >= 1)

m.c1013 = Constraint(expr=   m.b305 + m.b312 + m.b317 + m.b325 >= 1)

m.c1014 = Constraint(expr=   m.b305 + m.b312 + m.b317 + m.b321 >= 1)

m.c1015 = Constraint(expr=   m.b305 + m.b312 + m.b316 + m.b331 >= 1)

m.c1016 = Constraint(expr=   m.b305 + m.b312 + m.b316 + m.b326 >= 1)

m.c1017 = Constraint(expr=   m.b305 + m.b312 + m.b316 + m.b321 >= 1)

m.c1018 = Constraint(expr=   m.b305 + m.b312 + m.b315 + m.b331 >= 1)

m.c1019 = Constraint(expr=   m.b305 + m.b312 + m.b315 + m.b326 >= 1)

m.c1020 = Constraint(expr=   m.b305 + m.b312 + m.b315 + m.b321 >= 1)

m.c1021 = Constraint(expr=   m.b305 + m.b311 + m.b329 >= 1)

m.c1022 = Constraint(expr=   m.b305 + m.b311 + m.b326 + m.b330 >= 1)

m.c1023 = Constraint(expr=   m.b305 + m.b311 + m.b325 + m.b331 >= 1)

m.c1024 = Constraint(expr=   m.b305 + m.b311 + m.b324 >= 1)

m.c1025 = Constraint(expr=   m.b305 + m.b311 + m.b321 + m.b331 >= 1)

m.c1026 = Constraint(expr=   m.b305 + m.b311 + m.b321 + m.b326 >= 1)

m.c1027 = Constraint(expr=   m.b305 + m.b311 + m.b320 >= 1)

m.c1028 = Constraint(expr=   m.b305 + m.b311 + m.b318 + m.b330 >= 1)

m.c1029 = Constraint(expr=   m.b305 + m.b311 + m.b318 + m.b326 + m.b331 >= 1)

m.c1030 = Constraint(expr=   m.b305 + m.b311 + m.b318 + m.b325 >= 1)

m.c1031 = Constraint(expr=   m.b305 + m.b311 + m.b318 + m.b321 >= 1)

m.c1032 = Constraint(expr=   m.b305 + m.b311 + m.b317 + m.b331 >= 1)

m.c1033 = Constraint(expr=   m.b305 + m.b311 + m.b317 + m.b325 >= 1)

m.c1034 = Constraint(expr=   m.b305 + m.b311 + m.b317 + m.b321 >= 1)

m.c1035 = Constraint(expr=   m.b305 + m.b311 + m.b316 + m.b331 >= 1)

m.c1036 = Constraint(expr=   m.b305 + m.b311 + m.b316 + m.b326 >= 1)

m.c1037 = Constraint(expr=   m.b305 + m.b311 + m.b316 + m.b321 >= 1)

m.c1038 = Constraint(expr=   m.b305 + m.b310 + m.b330 >= 1)

m.c1039 = Constraint(expr=   m.b305 + m.b310 + m.b326 + m.b331 >= 1)

m.c1040 = Constraint(expr=   m.b305 + m.b310 + m.b325 >= 1)

m.c1041 = Constraint(expr=   m.b305 + m.b310 + m.b321 >= 1)

m.c1042 = Constraint(expr=   m.b305 + m.b310 + m.b318 + m.b331 >= 1)

m.c1043 = Constraint(expr=   m.b305 + m.b310 + m.b318 + m.b325 >= 1)

m.c1044 = Constraint(expr=   m.b305 + m.b310 + m.b318 + m.b321 >= 1)

m.c1045 = Constraint(expr=   m.b305 + m.b310 + m.b317 + m.b331 >= 1)

m.c1046 = Constraint(expr=   m.b305 + m.b310 + m.b317 + m.b326 >= 1)

m.c1047 = Constraint(expr=   m.b305 + m.b310 + m.b317 + m.b321 >= 1)

m.c1048 = Constraint(expr=   m.b305 + m.b309 + m.b330 >= 1)

m.c1049 = Constraint(expr=   m.b305 + m.b309 + m.b326 + m.b331 >= 1)

m.c1050 = Constraint(expr=   m.b305 + m.b309 + m.b325 >= 1)

m.c1051 = Constraint(expr=   m.b305 + m.b309 + m.b321 >= 1)

m.c1052 = Constraint(expr=   m.b305 + m.b309 + m.b318 + m.b331 >= 1)

m.c1053 = Constraint(expr=   m.b305 + m.b309 + m.b318 + m.b326 >= 1)

m.c1054 = Constraint(expr=   m.b305 + m.b309 + m.b318 + m.b321 >= 1)

m.c1055 = Constraint(expr=   m.b305 + m.b308 + m.b331 >= 1)

m.c1056 = Constraint(expr=   m.b305 + m.b308 + m.b326 >= 1)

m.c1057 = Constraint(expr=   m.b305 + m.b308 + m.b321 >= 1)

m.c1058 = Constraint(expr=   m.b304 + m.b329 >= 1)

m.c1059 = Constraint(expr=   m.b304 + m.b326 + m.b330 >= 1)

m.c1060 = Constraint(expr=   m.b304 + m.b325 + m.b331 >= 1)

m.c1061 = Constraint(expr=   m.b304 + m.b324 >= 1)

m.c1062 = Constraint(expr=   m.b304 + m.b321 + m.b331 >= 1)

m.c1063 = Constraint(expr=   m.b304 + m.b321 + m.b326 >= 1)

m.c1064 = Constraint(expr=   m.b304 + m.b320 >= 1)

m.c1065 = Constraint(expr=   m.b304 + m.b318 + m.b330 >= 1)

m.c1066 = Constraint(expr=   m.b304 + m.b318 + m.b326 + m.b331 >= 1)

m.c1067 = Constraint(expr=   m.b304 + m.b318 + m.b325 >= 1)

m.c1068 = Constraint(expr=   m.b304 + m.b318 + m.b321 >= 1)

m.c1069 = Constraint(expr=   m.b304 + m.b317 + m.b330 >= 1)

m.c1070 = Constraint(expr=   m.b304 + m.b317 + m.b326 + m.b331 >= 1)

m.c1071 = Constraint(expr=   m.b304 + m.b317 + m.b325 >= 1)

m.c1072 = Constraint(expr=   m.b304 + m.b317 + m.b321 >= 1)

m.c1073 = Constraint(expr=   m.b304 + m.b316 + m.b331 >= 1)

m.c1074 = Constraint(expr=   m.b304 + m.b316 + m.b326 >= 1)

m.c1075 = Constraint(expr=   m.b304 + m.b316 + m.b321 >= 1)

m.c1076 = Constraint(expr=   m.b304 + m.b312 + m.b330 >= 1)

m.c1077 = Constraint(expr=   m.b304 + m.b312 + m.b326 + m.b331 >= 1)

m.c1078 = Constraint(expr=   m.b304 + m.b312 + m.b325 >= 1)

m.c1079 = Constraint(expr=   m.b304 + m.b312 + m.b321 >= 1)

m.c1080 = Constraint(expr=   m.b304 + m.b312 + m.b318 + m.b331 >= 1)

m.c1081 = Constraint(expr=   m.b304 + m.b312 + m.b318 + m.b325 >= 1)

m.c1082 = Constraint(expr=   m.b304 + m.b312 + m.b318 + m.b321 >= 1)

m.c1083 = Constraint(expr=   m.b304 + m.b312 + m.b317 + m.b331 >= 1)

m.c1084 = Constraint(expr=   m.b304 + m.b312 + m.b317 + m.b326 >= 1)

m.c1085 = Constraint(expr=   m.b304 + m.b312 + m.b317 + m.b321 >= 1)

m.c1086 = Constraint(expr=   m.b304 + m.b311 + m.b330 >= 1)

m.c1087 = Constraint(expr=   m.b304 + m.b311 + m.b326 + m.b331 >= 1)

m.c1088 = Constraint(expr=   m.b304 + m.b311 + m.b325 >= 1)

m.c1089 = Constraint(expr=   m.b304 + m.b311 + m.b321 >= 1)

m.c1090 = Constraint(expr=   m.b304 + m.b311 + m.b318 + m.b331 >= 1)

m.c1091 = Constraint(expr=   m.b304 + m.b311 + m.b318 + m.b326 >= 1)

m.c1092 = Constraint(expr=   m.b304 + m.b311 + m.b318 + m.b321 >= 1)

m.c1093 = Constraint(expr=   m.b304 + m.b310 + m.b331 >= 1)

m.c1094 = Constraint(expr=   m.b304 + m.b310 + m.b326 >= 1)

m.c1095 = Constraint(expr=   m.b304 + m.b310 + m.b321 >= 1)

m.c1096 = Constraint(expr=   m.b303 + m.b331 >= 1)

m.c1097 = Constraint(expr=   m.b303 + m.b326 >= 1)

m.c1098 = Constraint(expr=   m.b303 + m.b321 >= 1)

m.c1099 = Constraint(expr=   m.b302 + m.b327 >= 1)

m.c1100 = Constraint(expr=   m.b302 + m.b326 + m.b328 >= 1)

m.c1101 = Constraint(expr=   m.b302 + m.b325 + m.b329 >= 1)

m.c1102 = Constraint(expr=   m.b302 + m.b324 + m.b330 >= 1)

m.c1103 = Constraint(expr=   m.b302 + m.b323 + m.b331 >= 1)

m.c1104 = Constraint(expr=   m.b302 + m.b322 >= 1)

m.c1105 = Constraint(expr=   m.b302 + m.b321 + m.b329 >= 1)

m.c1106 = Constraint(expr=   m.b302 + m.b321 + m.b326 + m.b330 >= 1)

m.c1107 = Constraint(expr=   m.b302 + m.b321 + m.b325 + m.b331 >= 1)

m.c1108 = Constraint(expr=   m.b302 + m.b321 + m.b324 >= 1)

m.c1109 = Constraint(expr=   m.b302 + m.b320 + m.b331 >= 1)

m.c1110 = Constraint(expr=   m.b302 + m.b320 + m.b326 >= 1)

m.c1111 = Constraint(expr=   m.b302 + m.b319 >= 1)

m.c1112 = Constraint(expr=   m.b302 + m.b318 + m.b328 >= 1)

m.c1113 = Constraint(expr=   m.b302 + m.b318 + m.b326 + m.b329 >= 1)

m.c1114 = Constraint(expr=   m.b302 + m.b318 + m.b324 + m.b331 >= 1)

m.c1115 = Constraint(expr=   m.b302 + m.b318 + m.b323 >= 1)

m.c1116 = Constraint(expr=   m.b302 + m.b318 + m.b321 + m.b329 >= 1)

m.c1117 = Constraint(expr=   m.b302 + m.b318 + m.b321 + m.b326 + m.b330 >= 1)

m.c1118 = Constraint(expr=   m.b302 + m.b318 + m.b321 + m.b325 + m.b331 >= 1)

m.c1119 = Constraint(expr=   m.b302 + m.b318 + m.b321 + m.b324 >= 1)

m.c1120 = Constraint(expr=   m.b302 + m.b318 + m.b320 >= 1)

m.c1121 = Constraint(expr=   m.b302 + m.b317 + m.b328 >= 1)

m.c1122 = Constraint(expr=   m.b302 + m.b317 + m.b326 + m.b329 >= 1)

m.c1123 = Constraint(expr=   m.b302 + m.b317 + m.b325 + m.b330 >= 1)

m.c1124 = Constraint(expr=   m.b302 + m.b317 + m.b324 + m.b331 >= 1)

m.c1125 = Constraint(expr=   m.b302 + m.b317 + m.b323 >= 1)

m.c1126 = Constraint(expr=   m.b302 + m.b317 + m.b321 + m.b330 >= 1)

m.c1127 = Constraint(expr=   m.b302 + m.b317 + m.b321 + m.b326 + m.b331 >= 1)

m.c1128 = Constraint(expr=   m.b302 + m.b317 + m.b321 + m.b325 >= 1)

m.c1129 = Constraint(expr=   m.b302 + m.b317 + m.b320 >= 1)

m.c1130 = Constraint(expr=   m.b302 + m.b316 + m.b329 >= 1)

m.c1131 = Constraint(expr=   m.b302 + m.b316 + m.b326 + m.b330 >= 1)

m.c1132 = Constraint(expr=   m.b302 + m.b316 + m.b325 + m.b331 >= 1)

m.c1133 = Constraint(expr=   m.b302 + m.b316 + m.b324 >= 1)

m.c1134 = Constraint(expr=   m.b302 + m.b316 + m.b321 + m.b331 >= 1)

m.c1135 = Constraint(expr=   m.b302 + m.b316 + m.b321 + m.b326 >= 1)

m.c1136 = Constraint(expr=   m.b302 + m.b316 + m.b320 >= 1)

m.c1137 = Constraint(expr=   m.b302 + m.b315 + m.b330 >= 1)

m.c1138 = Constraint(expr=   m.b302 + m.b315 + m.b326 + m.b331 >= 1)

m.c1139 = Constraint(expr=   m.b302 + m.b315 + m.b325 >= 1)

m.c1140 = Constraint(expr=   m.b302 + m.b315 + m.b321 >= 1)

m.c1141 = Constraint(expr=   m.b302 + m.b314 + m.b331 >= 1)

m.c1142 = Constraint(expr=   m.b302 + m.b314 + m.b326 >= 1)

m.c1143 = Constraint(expr=   m.b302 + m.b314 + m.b321 >= 1)

m.c1144 = Constraint(expr=   m.b302 + m.b312 + m.b328 >= 1)

m.c1145 = Constraint(expr=   m.b302 + m.b312 + m.b325 + m.b329 >= 1)

m.c1146 = Constraint(expr=   m.b302 + m.b312 + m.b324 + m.b330 >= 1)

m.c1147 = Constraint(expr=   m.b302 + m.b312 + m.b323 + m.b331 >= 1)

m.c1148 = Constraint(expr=   m.b302 + m.b312 + m.b322 >= 1)

m.c1149 = Constraint(expr=   m.b302 + m.b312 + m.b321 + m.b329 >= 1)

m.c1150 = Constraint(expr=   m.b302 + m.b312 + m.b321 + m.b326 + m.b330 >= 1)

m.c1151 = Constraint(expr=   m.b302 + m.b312 + m.b321 + m.b325 >= 1)

m.c1152 = Constraint(expr=   m.b302 + m.b312 + m.b320 >= 1)

m.c1153 = Constraint(expr=   m.b302 + m.b312 + m.b318 + m.b328 >= 1)

m.c1154 = Constraint(expr=   m.b302 + m.b312 + m.b318 + m.b326 + m.b329 >= 1)

m.c1155 = Constraint(expr=   m.b302 + m.b312 + m.b318 + m.b325 + m.b330 >= 1)

m.c1156 = Constraint(expr=   m.b302 + m.b312 + m.b318 + m.b324 + m.b331 >= 1)

m.c1157 = Constraint(expr=   m.b302 + m.b312 + m.b318 + m.b323 >= 1)

m.c1158 = Constraint(expr=   m.b302 + m.b312 + m.b318 + m.b321 + m.b330 >= 1)

m.c1159 = Constraint(expr=   m.b302 + m.b312 + m.b318 + m.b321 + m.b326 + m.b331 >= 1)

m.c1160 = Constraint(expr=   m.b302 + m.b312 + m.b318 + m.b321 + m.b325 >= 1)

m.c1161 = Constraint(expr=   m.b302 + m.b312 + m.b318 + m.b320 >= 1)

m.c1162 = Constraint(expr=   m.b302 + m.b312 + m.b317 + m.b329 >= 1)

m.c1163 = Constraint(expr=   m.b302 + m.b312 + m.b317 + m.b326 + m.b330 >= 1)

m.c1164 = Constraint(expr=   m.b302 + m.b312 + m.b317 + m.b325 + m.b331 >= 1)

m.c1165 = Constraint(expr=   m.b302 + m.b312 + m.b317 + m.b324 >= 1)

m.c1166 = Constraint(expr=   m.b302 + m.b312 + m.b317 + m.b321 + m.b331 >= 1)

m.c1167 = Constraint(expr=   m.b302 + m.b312 + m.b317 + m.b321 + m.b326 >= 1)

m.c1168 = Constraint(expr=   m.b302 + m.b312 + m.b317 + m.b320 >= 1)

m.c1169 = Constraint(expr=   m.b302 + m.b312 + m.b316 + m.b330 >= 1)

m.c1170 = Constraint(expr=   m.b302 + m.b312 + m.b316 + m.b326 + m.b331 >= 1)

m.c1171 = Constraint(expr=   m.b302 + m.b312 + m.b316 + m.b325 >= 1)

m.c1172 = Constraint(expr=   m.b302 + m.b312 + m.b316 + m.b321 >= 1)

m.c1173 = Constraint(expr=   m.b302 + m.b312 + m.b315 + m.b331 >= 1)

m.c1174 = Constraint(expr=   m.b302 + m.b312 + m.b315 + m.b326 >= 1)

m.c1175 = Constraint(expr=   m.b302 + m.b312 + m.b315 + m.b321 >= 1)

m.c1176 = Constraint(expr=   m.b302 + m.b311 + m.b328 >= 1)

m.c1177 = Constraint(expr=   m.b302 + m.b311 + m.b326 + m.b329 >= 1)

m.c1178 = Constraint(expr=   m.b302 + m.b311 + m.b325 + m.b330 >= 1)

m.c1179 = Constraint(expr=   m.b302 + m.b311 + m.b324 + m.b331 >= 1)

m.c1180 = Constraint(expr=   m.b302 + m.b311 + m.b323 >= 1)

m.c1181 = Constraint(expr=   m.b302 + m.b311 + m.b321 + m.b330 >= 1)

m.c1182 = Constraint(expr=   m.b302 + m.b311 + m.b321 + m.b326 + m.b331 >= 1)

m.c1183 = Constraint(expr=   m.b302 + m.b311 + m.b321 + m.b325 >= 1)

m.c1184 = Constraint(expr=   m.b302 + m.b311 + m.b320 >= 1)

m.c1185 = Constraint(expr=   m.b302 + m.b311 + m.b318 + m.b329 >= 1)

m.c1186 = Constraint(expr=   m.b302 + m.b311 + m.b318 + m.b326 + m.b330 >= 1)

m.c1187 = Constraint(expr=   m.b302 + m.b311 + m.b318 + m.b325 + m.b331 >= 1)

m.c1188 = Constraint(expr=   m.b302 + m.b311 + m.b318 + m.b324 >= 1)

m.c1189 = Constraint(expr=   m.b302 + m.b311 + m.b318 + m.b321 + m.b331 >= 1)

m.c1190 = Constraint(expr=   m.b302 + m.b311 + m.b318 + m.b321 + m.b326 >= 1)

m.c1191 = Constraint(expr=   m.b302 + m.b311 + m.b318 + m.b320 >= 1)

m.c1192 = Constraint(expr=   m.b302 + m.b311 + m.b317 + m.b330 >= 1)

m.c1193 = Constraint(expr=   m.b302 + m.b311 + m.b317 + m.b326 + m.b331 >= 1)

m.c1194 = Constraint(expr=   m.b302 + m.b311 + m.b317 + m.b325 >= 1)

m.c1195 = Constraint(expr=   m.b302 + m.b311 + m.b317 + m.b321 >= 1)

m.c1196 = Constraint(expr=   m.b302 + m.b311 + m.b316 + m.b331 >= 1)

m.c1197 = Constraint(expr=   m.b302 + m.b311 + m.b316 + m.b326 >= 1)

m.c1198 = Constraint(expr=   m.b302 + m.b311 + m.b316 + m.b321 >= 1)

m.c1199 = Constraint(expr=   m.b302 + m.b311 + m.b315 + m.b331 >= 1)

m.c1200 = Constraint(expr=   m.b302 + m.b311 + m.b315 + m.b326 >= 1)

m.c1201 = Constraint(expr=   m.b302 + m.b311 + m.b315 + m.b321 >= 1)

m.c1202 = Constraint(expr=   m.b302 + m.b310 + m.b329 >= 1)

m.c1203 = Constraint(expr=   m.b302 + m.b310 + m.b326 + m.b330 >= 1)

m.c1204 = Constraint(expr=   m.b302 + m.b310 + m.b325 + m.b331 >= 1)

m.c1205 = Constraint(expr=   m.b302 + m.b310 + m.b324 >= 1)

m.c1206 = Constraint(expr=   m.b302 + m.b310 + m.b321 + m.b331 >= 1)

m.c1207 = Constraint(expr=   m.b302 + m.b310 + m.b321 + m.b326 >= 1)

m.c1208 = Constraint(expr=   m.b302 + m.b310 + m.b320 >= 1)

m.c1209 = Constraint(expr=   m.b302 + m.b310 + m.b318 + m.b330 >= 1)

m.c1210 = Constraint(expr=   m.b302 + m.b310 + m.b318 + m.b326 + m.b331 >= 1)

m.c1211 = Constraint(expr=   m.b302 + m.b310 + m.b318 + m.b325 >= 1)

m.c1212 = Constraint(expr=   m.b302 + m.b310 + m.b318 + m.b321 >= 1)

m.c1213 = Constraint(expr=   m.b302 + m.b310 + m.b317 + m.b331 >= 1)

m.c1214 = Constraint(expr=   m.b302 + m.b310 + m.b317 + m.b326 >= 1)

m.c1215 = Constraint(expr=   m.b302 + m.b310 + m.b317 + m.b321 >= 1)

m.c1216 = Constraint(expr=   m.b302 + m.b310 + m.b316 + m.b331 >= 1)

m.c1217 = Constraint(expr=   m.b302 + m.b310 + m.b316 + m.b326 >= 1)

m.c1218 = Constraint(expr=   m.b302 + m.b310 + m.b316 + m.b321 >= 1)

m.c1219 = Constraint(expr=   m.b302 + m.b309 + m.b330 >= 1)

m.c1220 = Constraint(expr=   m.b302 + m.b309 + m.b326 + m.b331 >= 1)

m.c1221 = Constraint(expr=   m.b302 + m.b309 + m.b325 >= 1)

m.c1222 = Constraint(expr=   m.b302 + m.b309 + m.b321 >= 1)

m.c1223 = Constraint(expr=   m.b302 + m.b309 + m.b318 + m.b331 >= 1)

m.c1224 = Constraint(expr=   m.b302 + m.b309 + m.b318 + m.b326 >= 1)

m.c1225 = Constraint(expr=   m.b302 + m.b309 + m.b318 + m.b321 >= 1)

m.c1226 = Constraint(expr=   m.b302 + m.b309 + m.b317 + m.b331 >= 1)

m.c1227 = Constraint(expr=   m.b302 + m.b309 + m.b317 + m.b326 >= 1)

m.c1228 = Constraint(expr=   m.b302 + m.b309 + m.b317 + m.b321 >= 1)

m.c1229 = Constraint(expr=   m.b302 + m.b308 + m.b331 >= 1)

m.c1230 = Constraint(expr=   m.b302 + m.b308 + m.b326 >= 1)

m.c1231 = Constraint(expr=   m.b302 + m.b308 + m.b321 >= 1)

m.c1232 = Constraint(expr=   m.b302 + m.b306 + m.b328 >= 1)

m.c1233 = Constraint(expr=   m.b302 + m.b306 + m.b326 + m.b329 >= 1)

m.c1234 = Constraint(expr=   m.b302 + m.b306 + m.b325 + m.b330 >= 1)

m.c1235 = Constraint(expr=   m.b302 + m.b306 + m.b324 + m.b331 >= 1)

m.c1236 = Constraint(expr=   m.b302 + m.b306 + m.b323 >= 1)

m.c1237 = Constraint(expr=   m.b302 + m.b306 + m.b321 + m.b330 >= 1)

m.c1238 = Constraint(expr=   m.b302 + m.b306 + m.b321 + m.b326 + m.b331 >= 1)

m.c1239 = Constraint(expr=   m.b302 + m.b306 + m.b321 + m.b325 >= 1)

m.c1240 = Constraint(expr=   m.b302 + m.b306 + m.b320 >= 1)

m.c1241 = Constraint(expr=   m.b302 + m.b306 + m.b318 + m.b329 >= 1)

m.c1242 = Constraint(expr=   m.b302 + m.b306 + m.b318 + m.b326 + m.b330 >= 1)

m.c1243 = Constraint(expr=   m.b302 + m.b306 + m.b318 + m.b325 + m.b331 >= 1)

m.c1244 = Constraint(expr=   m.b302 + m.b306 + m.b318 + m.b324 >= 1)

m.c1245 = Constraint(expr=   m.b302 + m.b306 + m.b318 + m.b321 + m.b331 >= 1)

m.c1246 = Constraint(expr=   m.b302 + m.b306 + m.b318 + m.b321 + m.b326 >= 1)

m.c1247 = Constraint(expr=   m.b302 + m.b306 + m.b318 + m.b320 >= 1)

m.c1248 = Constraint(expr=   m.b302 + m.b306 + m.b317 + m.b329 >= 1)

m.c1249 = Constraint(expr=   m.b302 + m.b306 + m.b317 + m.b326 + m.b330 >= 1)

m.c1250 = Constraint(expr=   m.b302 + m.b306 + m.b317 + m.b325 + m.b331 >= 1)

m.c1251 = Constraint(expr=   m.b302 + m.b306 + m.b317 + m.b324 >= 1)

m.c1252 = Constraint(expr=   m.b302 + m.b306 + m.b317 + m.b321 + m.b331 >= 1)

m.c1253 = Constraint(expr=   m.b302 + m.b306 + m.b317 + m.b321 + m.b326 >= 1)

m.c1254 = Constraint(expr=   m.b302 + m.b306 + m.b317 + m.b320 >= 1)

m.c1255 = Constraint(expr=   m.b302 + m.b306 + m.b316 + m.b330 >= 1)

m.c1256 = Constraint(expr=   m.b302 + m.b306 + m.b316 + m.b326 + m.b331 >= 1)

m.c1257 = Constraint(expr=   m.b302 + m.b306 + m.b316 + m.b325 >= 1)

m.c1258 = Constraint(expr=   m.b302 + m.b306 + m.b316 + m.b321 >= 1)

m.c1259 = Constraint(expr=   m.b302 + m.b306 + m.b315 + m.b331 >= 1)

m.c1260 = Constraint(expr=   m.b302 + m.b306 + m.b315 + m.b326 >= 1)

m.c1261 = Constraint(expr=   m.b302 + m.b306 + m.b315 + m.b321 >= 1)

m.c1262 = Constraint(expr=   m.b302 + m.b306 + m.b312 + m.b329 >= 1)

m.c1263 = Constraint(expr=   m.b302 + m.b306 + m.b312 + m.b326 + m.b330 >= 1)

m.c1264 = Constraint(expr=   m.b302 + m.b306 + m.b312 + m.b325 + m.b331 >= 1)

m.c1265 = Constraint(expr=   m.b302 + m.b306 + m.b312 + m.b324 >= 1)

m.c1266 = Constraint(expr=   m.b302 + m.b306 + m.b312 + m.b321 + m.b331 >= 1)

m.c1267 = Constraint(expr=   m.b302 + m.b306 + m.b312 + m.b321 + m.b326 >= 1)

m.c1268 = Constraint(expr=   m.b302 + m.b306 + m.b312 + m.b320 >= 1)

m.c1269 = Constraint(expr=   m.b302 + m.b306 + m.b312 + m.b318 + m.b330 >= 1)

m.c1270 = Constraint(expr=   m.b302 + m.b306 + m.b312 + m.b318 + m.b326 + m.b331 >= 1)

m.c1271 = Constraint(expr=   m.b302 + m.b306 + m.b312 + m.b318 + m.b325 >= 1)

m.c1272 = Constraint(expr=   m.b302 + m.b306 + m.b312 + m.b318 + m.b321 >= 1)

m.c1273 = Constraint(expr=   m.b302 + m.b306 + m.b312 + m.b317 + m.b330 >= 1)

m.c1274 = Constraint(expr=   m.b302 + m.b306 + m.b312 + m.b317 + m.b326 + m.b331 >= 1)

m.c1275 = Constraint(expr=   m.b302 + m.b306 + m.b312 + m.b317 + m.b325 >= 1)

m.c1276 = Constraint(expr=   m.b302 + m.b306 + m.b312 + m.b317 + m.b321 >= 1)

m.c1277 = Constraint(expr=   m.b302 + m.b306 + m.b312 + m.b316 + m.b331 >= 1)

m.c1278 = Constraint(expr=   m.b302 + m.b306 + m.b312 + m.b316 + m.b326 >= 1)

m.c1279 = Constraint(expr=   m.b302 + m.b306 + m.b312 + m.b316 + m.b321 >= 1)

m.c1280 = Constraint(expr=   m.b302 + m.b306 + m.b311 + m.b329 >= 1)

m.c1281 = Constraint(expr=   m.b302 + m.b306 + m.b311 + m.b326 + m.b330 >= 1)

m.c1282 = Constraint(expr=   m.b302 + m.b306 + m.b311 + m.b325 + m.b331 >= 1)

m.c1283 = Constraint(expr=   m.b302 + m.b306 + m.b311 + m.b324 >= 1)

m.c1284 = Constraint(expr=   m.b302 + m.b306 + m.b311 + m.b321 + m.b331 >= 1)

m.c1285 = Constraint(expr=   m.b302 + m.b306 + m.b311 + m.b321 + m.b326 >= 1)

m.c1286 = Constraint(expr=   m.b302 + m.b306 + m.b311 + m.b320 >= 1)

m.c1287 = Constraint(expr=   m.b302 + m.b306 + m.b311 + m.b318 + m.b330 >= 1)

m.c1288 = Constraint(expr=   m.b302 + m.b306 + m.b311 + m.b318 + m.b326 + m.b331 >= 1)

m.c1289 = Constraint(expr=   m.b302 + m.b306 + m.b311 + m.b318 + m.b325 >= 1)

m.c1290 = Constraint(expr=   m.b302 + m.b306 + m.b311 + m.b318 + m.b321 >= 1)

m.c1291 = Constraint(expr=   m.b302 + m.b306 + m.b311 + m.b317 + m.b331 >= 1)

m.c1292 = Constraint(expr=   m.b302 + m.b306 + m.b311 + m.b317 + m.b326 >= 1)

m.c1293 = Constraint(expr=   m.b302 + m.b306 + m.b311 + m.b317 + m.b321 >= 1)

m.c1294 = Constraint(expr=   m.b302 + m.b306 + m.b310 + m.b330 >= 1)

m.c1295 = Constraint(expr=   m.b302 + m.b306 + m.b310 + m.b326 + m.b331 >= 1)

m.c1296 = Constraint(expr=   m.b302 + m.b306 + m.b310 + m.b325 >= 1)

m.c1297 = Constraint(expr=   m.b302 + m.b306 + m.b310 + m.b321 >= 1)

m.c1298 = Constraint(expr=   m.b302 + m.b306 + m.b310 + m.b318 + m.b331 >= 1)

m.c1299 = Constraint(expr=   m.b302 + m.b306 + m.b310 + m.b318 + m.b326 >= 1)

m.c1300 = Constraint(expr=   m.b302 + m.b306 + m.b310 + m.b318 + m.b321 >= 1)

m.c1301 = Constraint(expr=   m.b302 + m.b306 + m.b309 + m.b331 >= 1)

m.c1302 = Constraint(expr=   m.b302 + m.b306 + m.b309 + m.b326 >= 1)

m.c1303 = Constraint(expr=   m.b302 + m.b306 + m.b309 + m.b321 >= 1)

m.c1304 = Constraint(expr=   m.b302 + m.b305 + m.b329 >= 1)

m.c1305 = Constraint(expr=   m.b302 + m.b305 + m.b326 + m.b330 >= 1)

m.c1306 = Constraint(expr=   m.b302 + m.b305 + m.b325 + m.b331 >= 1)

m.c1307 = Constraint(expr=   m.b302 + m.b305 + m.b324 >= 1)

m.c1308 = Constraint(expr=   m.b302 + m.b305 + m.b321 + m.b331 >= 1)

m.c1309 = Constraint(expr=   m.b302 + m.b305 + m.b321 + m.b326 >= 1)

m.c1310 = Constraint(expr=   m.b302 + m.b305 + m.b320 >= 1)

m.c1311 = Constraint(expr=   m.b302 + m.b305 + m.b318 + m.b330 >= 1)

m.c1312 = Constraint(expr=   m.b302 + m.b305 + m.b318 + m.b326 + m.b331 >= 1)

m.c1313 = Constraint(expr=   m.b302 + m.b305 + m.b318 + m.b325 >= 1)

m.c1314 = Constraint(expr=   m.b302 + m.b305 + m.b318 + m.b321 >= 1)

m.c1315 = Constraint(expr=   m.b302 + m.b305 + m.b317 + m.b331 >= 1)

m.c1316 = Constraint(expr=   m.b302 + m.b305 + m.b317 + m.b326 >= 1)

m.c1317 = Constraint(expr=   m.b302 + m.b305 + m.b317 + m.b321 >= 1)

m.c1318 = Constraint(expr=   m.b302 + m.b305 + m.b312 + m.b330 >= 1)

m.c1319 = Constraint(expr=   m.b302 + m.b305 + m.b312 + m.b326 + m.b331 >= 1)

m.c1320 = Constraint(expr=   m.b302 + m.b305 + m.b312 + m.b325 >= 1)

m.c1321 = Constraint(expr=   m.b302 + m.b305 + m.b312 + m.b321 >= 1)

m.c1322 = Constraint(expr=   m.b302 + m.b305 + m.b312 + m.b318 + m.b331 >= 1)

m.c1323 = Constraint(expr=   m.b302 + m.b305 + m.b312 + m.b318 + m.b326 >= 1)

m.c1324 = Constraint(expr=   m.b302 + m.b305 + m.b312 + m.b318 + m.b321 >= 1)

m.c1325 = Constraint(expr=   m.b302 + m.b305 + m.b311 + m.b331 >= 1)

m.c1326 = Constraint(expr=   m.b302 + m.b305 + m.b311 + m.b326 >= 1)

m.c1327 = Constraint(expr=   m.b302 + m.b305 + m.b311 + m.b321 >= 1)

m.c1328 = Constraint(expr=   m.b302 + m.b304 + m.b331 >= 1)

m.c1329 = Constraint(expr=   m.b302 + m.b304 + m.b326 >= 1)

m.c1330 = Constraint(expr=   m.b302 + m.b304 + m.b321 >= 1)

m.c1331 = Constraint(expr=   m.b301 + m.b329 >= 1)

m.c1332 = Constraint(expr=   m.b301 + m.b326 + m.b330 >= 1)

m.c1333 = Constraint(expr=   m.b301 + m.b325 + m.b331 >= 1)

m.c1334 = Constraint(expr=   m.b301 + m.b324 >= 1)

m.c1335 = Constraint(expr=   m.b301 + m.b321 + m.b331 >= 1)

m.c1336 = Constraint(expr=   m.b301 + m.b321 + m.b326 >= 1)

m.c1337 = Constraint(expr=   m.b301 + m.b320 >= 1)

m.c1338 = Constraint(expr=   m.b301 + m.b318 + m.b330 >= 1)

m.c1339 = Constraint(expr=   m.b301 + m.b318 + m.b326 + m.b331 >= 1)

m.c1340 = Constraint(expr=   m.b301 + m.b318 + m.b325 >= 1)

m.c1341 = Constraint(expr=   m.b301 + m.b318 + m.b321 >= 1)

m.c1342 = Constraint(expr=   m.b301 + m.b317 + m.b330 >= 1)

m.c1343 = Constraint(expr=   m.b301 + m.b317 + m.b326 + m.b331 >= 1)

m.c1344 = Constraint(expr=   m.b301 + m.b317 + m.b325 >= 1)

m.c1345 = Constraint(expr=   m.b301 + m.b317 + m.b321 >= 1)

m.c1346 = Constraint(expr=   m.b301 + m.b316 + m.b331 >= 1)

m.c1347 = Constraint(expr=   m.b301 + m.b316 + m.b326 >= 1)

m.c1348 = Constraint(expr=   m.b301 + m.b316 + m.b321 >= 1)

m.c1349 = Constraint(expr=   m.b301 + m.b312 + m.b330 >= 1)

m.c1350 = Constraint(expr=   m.b301 + m.b312 + m.b326 + m.b331 >= 1)

m.c1351 = Constraint(expr=   m.b301 + m.b312 + m.b325 >= 1)

m.c1352 = Constraint(expr=   m.b301 + m.b312 + m.b321 >= 1)

m.c1353 = Constraint(expr=   m.b301 + m.b312 + m.b318 + m.b331 >= 1)

m.c1354 = Constraint(expr=   m.b301 + m.b312 + m.b318 + m.b325 >= 1)

m.c1355 = Constraint(expr=   m.b301 + m.b312 + m.b318 + m.b321 >= 1)

m.c1356 = Constraint(expr=   m.b301 + m.b312 + m.b317 + m.b331 >= 1)

m.c1357 = Constraint(expr=   m.b301 + m.b312 + m.b317 + m.b326 >= 1)

m.c1358 = Constraint(expr=   m.b301 + m.b312 + m.b317 + m.b321 >= 1)

m.c1359 = Constraint(expr=   m.b301 + m.b311 + m.b330 >= 1)

m.c1360 = Constraint(expr=   m.b301 + m.b311 + m.b326 + m.b331 >= 1)

m.c1361 = Constraint(expr=   m.b301 + m.b311 + m.b325 >= 1)

m.c1362 = Constraint(expr=   m.b301 + m.b311 + m.b321 >= 1)

m.c1363 = Constraint(expr=   m.b301 + m.b311 + m.b318 + m.b331 >= 1)

m.c1364 = Constraint(expr=   m.b301 + m.b311 + m.b318 + m.b326 >= 1)

m.c1365 = Constraint(expr=   m.b301 + m.b311 + m.b318 + m.b321 >= 1)

m.c1366 = Constraint(expr=   m.b301 + m.b310 + m.b331 >= 1)

m.c1367 = Constraint(expr=   m.b301 + m.b310 + m.b326 >= 1)

m.c1368 = Constraint(expr=   m.b301 + m.b310 + m.b321 >= 1)

m.c1369 = Constraint(expr=   m.b301 + m.b306 + m.b330 >= 1)

m.c1370 = Constraint(expr=   m.b301 + m.b306 + m.b326 + m.b331 >= 1)

m.c1371 = Constraint(expr=   m.b301 + m.b306 + m.b325 >= 1)

m.c1372 = Constraint(expr=   m.b301 + m.b306 + m.b321 >= 1)

m.c1373 = Constraint(expr=   m.b301 + m.b306 + m.b318 + m.b331 >= 1)

m.c1374 = Constraint(expr=   m.b301 + m.b306 + m.b318 + m.b326 >= 1)

m.c1375 = Constraint(expr=   m.b301 + m.b306 + m.b318 + m.b321 >= 1)

m.c1376 = Constraint(expr=   m.b301 + m.b306 + m.b312 + m.b331 >= 1)

m.c1377 = Constraint(expr=   m.b301 + m.b306 + m.b312 + m.b326 >= 1)

m.c1378 = Constraint(expr=   m.b301 + m.b306 + m.b312 + m.b321 >= 1)

m.c1379 = Constraint(expr=   m.b301 + m.b305 + m.b331 >= 1)

m.c1380 = Constraint(expr=   m.b301 + m.b305 + m.b326 >= 1)

m.c1381 = Constraint(expr=   m.b301 + m.b305 + m.b321 >= 1)

m.c1382 = Constraint(expr=   m.b300 + m.b331 >= 1)

m.c1383 = Constraint(expr=   m.b300 + m.b326 >= 1)

m.c1384 = Constraint(expr=   m.b300 + m.b321 >= 1)

m.c1385 = Constraint(expr=   m.b299 + m.b327 >= 1)

m.c1386 = Constraint(expr=   m.b299 + m.b326 + m.b328 >= 1)

m.c1387 = Constraint(expr=   m.b299 + m.b325 + m.b329 >= 1)

m.c1388 = Constraint(expr=   m.b299 + m.b324 + m.b330 >= 1)

m.c1389 = Constraint(expr=   m.b299 + m.b323 + m.b331 >= 1)

m.c1390 = Constraint(expr=   m.b299 + m.b322 >= 1)

m.c1391 = Constraint(expr=   m.b299 + m.b321 + m.b329 >= 1)

m.c1392 = Constraint(expr=   m.b299 + m.b321 + m.b326 + m.b330 >= 1)

m.c1393 = Constraint(expr=   m.b299 + m.b321 + m.b325 + m.b331 >= 1)

m.c1394 = Constraint(expr=   m.b299 + m.b321 + m.b324 >= 1)

m.c1395 = Constraint(expr=   m.b299 + m.b320 + m.b331 >= 1)

m.c1396 = Constraint(expr=   m.b299 + m.b320 + m.b326 >= 1)

m.c1397 = Constraint(expr=   m.b299 + m.b319 >= 1)

m.c1398 = Constraint(expr=   m.b299 + m.b318 + m.b328 >= 1)

m.c1399 = Constraint(expr=   m.b299 + m.b318 + m.b326 + m.b329 >= 1)

m.c1400 = Constraint(expr=   m.b299 + m.b318 + m.b325 + m.b330 >= 1)

m.c1401 = Constraint(expr=   m.b299 + m.b318 + m.b324 + m.b331 >= 1)

m.c1402 = Constraint(expr=   m.b299 + m.b318 + m.b323 >= 1)

m.c1403 = Constraint(expr=   m.b299 + m.b318 + m.b321 + m.b330 >= 1)

m.c1404 = Constraint(expr=   m.b299 + m.b318 + m.b321 + m.b326 + m.b331 >= 1)

m.c1405 = Constraint(expr=   m.b299 + m.b318 + m.b321 + m.b325 >= 1)

m.c1406 = Constraint(expr=   m.b299 + m.b318 + m.b320 >= 1)

m.c1407 = Constraint(expr=   m.b299 + m.b317 + m.b328 >= 1)

m.c1408 = Constraint(expr=   m.b299 + m.b317 + m.b326 + m.b329 >= 1)

m.c1409 = Constraint(expr=   m.b299 + m.b317 + m.b325 + m.b330 >= 1)

m.c1410 = Constraint(expr=   m.b299 + m.b317 + m.b324 >= 1)

m.c1411 = Constraint(expr=   m.b299 + m.b317 + m.b321 + m.b330 >= 1)

m.c1412 = Constraint(expr=   m.b299 + m.b317 + m.b321 + m.b326 + m.b331 >= 1)

m.c1413 = Constraint(expr=   m.b299 + m.b317 + m.b321 + m.b325 >= 1)

m.c1414 = Constraint(expr=   m.b299 + m.b317 + m.b320 >= 1)

m.c1415 = Constraint(expr=   m.b299 + m.b316 + m.b329 >= 1)

m.c1416 = Constraint(expr=   m.b299 + m.b316 + m.b326 + m.b330 >= 1)

m.c1417 = Constraint(expr=   m.b299 + m.b316 + m.b325 + m.b331 >= 1)

m.c1418 = Constraint(expr=   m.b299 + m.b316 + m.b324 >= 1)

m.c1419 = Constraint(expr=   m.b299 + m.b316 + m.b321 + m.b331 >= 1)

m.c1420 = Constraint(expr=   m.b299 + m.b316 + m.b321 + m.b326 >= 1)

m.c1421 = Constraint(expr=   m.b299 + m.b316 + m.b320 >= 1)

m.c1422 = Constraint(expr=   m.b299 + m.b315 + m.b330 >= 1)

m.c1423 = Constraint(expr=   m.b299 + m.b315 + m.b326 + m.b331 >= 1)

m.c1424 = Constraint(expr=   m.b299 + m.b315 + m.b325 >= 1)

m.c1425 = Constraint(expr=   m.b299 + m.b315 + m.b321 >= 1)

m.c1426 = Constraint(expr=   m.b299 + m.b314 + m.b331 >= 1)

m.c1427 = Constraint(expr=   m.b299 + m.b314 + m.b326 >= 1)

m.c1428 = Constraint(expr=   m.b299 + m.b314 + m.b321 >= 1)

m.c1429 = Constraint(expr=   m.b299 + m.b312 + m.b328 >= 1)

m.c1430 = Constraint(expr=   m.b299 + m.b312 + m.b326 + m.b329 >= 1)

m.c1431 = Constraint(expr=   m.b299 + m.b312 + m.b325 + m.b330 >= 1)

m.c1432 = Constraint(expr=   m.b299 + m.b312 + m.b324 + m.b331 >= 1)

m.c1433 = Constraint(expr=   m.b299 + m.b312 + m.b323 >= 1)

m.c1434 = Constraint(expr=   m.b299 + m.b312 + m.b321 + m.b330 >= 1)

m.c1435 = Constraint(expr=   m.b299 + m.b312 + m.b321 + m.b326 + m.b331 >= 1)

m.c1436 = Constraint(expr=   m.b299 + m.b312 + m.b321 + m.b325 >= 1)

m.c1437 = Constraint(expr=   m.b299 + m.b312 + m.b320 >= 1)

m.c1438 = Constraint(expr=   m.b299 + m.b312 + m.b318 + m.b329 >= 1)

m.c1439 = Constraint(expr=   m.b299 + m.b312 + m.b318 + m.b325 + m.b331 >= 1)

m.c1440 = Constraint(expr=   m.b299 + m.b312 + m.b318 + m.b324 >= 1)

m.c1441 = Constraint(expr=   m.b299 + m.b312 + m.b318 + m.b321 + m.b331 >= 1)

m.c1442 = Constraint(expr=   m.b299 + m.b312 + m.b318 + m.b321 + m.b325 >= 1)

m.c1443 = Constraint(expr=   m.b299 + m.b312 + m.b318 + m.b320 >= 1)

m.c1444 = Constraint(expr=   m.b299 + m.b312 + m.b317 + m.b329 >= 1)

m.c1445 = Constraint(expr=   m.b299 + m.b312 + m.b317 + m.b326 + m.b330 >= 1)

m.c1446 = Constraint(expr=   m.b299 + m.b312 + m.b317 + m.b325 + m.b331 >= 1)

m.c1447 = Constraint(expr=   m.b299 + m.b312 + m.b317 + m.b324 >= 1)

m.c1448 = Constraint(expr=   m.b299 + m.b312 + m.b317 + m.b321 + m.b331 >= 1)

m.c1449 = Constraint(expr=   m.b299 + m.b312 + m.b317 + m.b321 + m.b326 >= 1)

m.c1450 = Constraint(expr=   m.b299 + m.b312 + m.b317 + m.b320 >= 1)

m.c1451 = Constraint(expr=   m.b299 + m.b312 + m.b316 + m.b330 >= 1)

m.c1452 = Constraint(expr=   m.b299 + m.b312 + m.b316 + m.b326 + m.b331 >= 1)

m.c1453 = Constraint(expr=   m.b299 + m.b312 + m.b316 + m.b325 >= 1)

m.c1454 = Constraint(expr=   m.b299 + m.b312 + m.b316 + m.b321 >= 1)

m.c1455 = Constraint(expr=   m.b299 + m.b312 + m.b315 + m.b331 >= 1)

m.c1456 = Constraint(expr=   m.b299 + m.b312 + m.b315 + m.b326 >= 1)

m.c1457 = Constraint(expr=   m.b299 + m.b312 + m.b315 + m.b321 >= 1)

m.c1458 = Constraint(expr=   m.b299 + m.b311 + m.b328 >= 1)

m.c1459 = Constraint(expr=   m.b299 + m.b311 + m.b326 + m.b329 >= 1)

m.c1460 = Constraint(expr=   m.b299 + m.b311 + m.b325 + m.b330 >= 1)

m.c1461 = Constraint(expr=   m.b299 + m.b311 + m.b324 + m.b331 >= 1)

m.c1462 = Constraint(expr=   m.b299 + m.b311 + m.b323 >= 1)

m.c1463 = Constraint(expr=   m.b299 + m.b311 + m.b321 + m.b330 >= 1)

m.c1464 = Constraint(expr=   m.b299 + m.b311 + m.b321 + m.b326 + m.b331 >= 1)

m.c1465 = Constraint(expr=   m.b299 + m.b311 + m.b321 + m.b325 >= 1)

m.c1466 = Constraint(expr=   m.b299 + m.b311 + m.b320 >= 1)

m.c1467 = Constraint(expr=   m.b299 + m.b311 + m.b318 + m.b329 >= 1)

m.c1468 = Constraint(expr=   m.b299 + m.b311 + m.b318 + m.b326 + m.b330 >= 1)

m.c1469 = Constraint(expr=   m.b299 + m.b311 + m.b318 + m.b325 + m.b331 >= 1)

m.c1470 = Constraint(expr=   m.b299 + m.b311 + m.b318 + m.b324 >= 1)

m.c1471 = Constraint(expr=   m.b299 + m.b311 + m.b318 + m.b321 + m.b331 >= 1)

m.c1472 = Constraint(expr=   m.b299 + m.b311 + m.b318 + m.b321 + m.b326 >= 1)

m.c1473 = Constraint(expr=   m.b299 + m.b311 + m.b318 + m.b320 >= 1)

m.c1474 = Constraint(expr=   m.b299 + m.b311 + m.b317 + m.b330 >= 1)

m.c1475 = Constraint(expr=   m.b299 + m.b311 + m.b317 + m.b326 + m.b331 >= 1)

m.c1476 = Constraint(expr=   m.b299 + m.b311 + m.b317 + m.b325 >= 1)

m.c1477 = Constraint(expr=   m.b299 + m.b311 + m.b317 + m.b321 >= 1)

m.c1478 = Constraint(expr=   m.b299 + m.b311 + m.b316 + m.b331 >= 1)

m.c1479 = Constraint(expr=   m.b299 + m.b311 + m.b316 + m.b326 >= 1)

m.c1480 = Constraint(expr=   m.b299 + m.b311 + m.b316 + m.b321 >= 1)

m.c1481 = Constraint(expr=   m.b299 + m.b310 + m.b329 >= 1)

m.c1482 = Constraint(expr=   m.b299 + m.b310 + m.b326 + m.b330 >= 1)

m.c1483 = Constraint(expr=   m.b299 + m.b310 + m.b325 + m.b331 >= 1)

m.c1484 = Constraint(expr=   m.b299 + m.b310 + m.b324 >= 1)

m.c1485 = Constraint(expr=   m.b299 + m.b310 + m.b321 + m.b331 >= 1)

m.c1486 = Constraint(expr=   m.b299 + m.b310 + m.b321 + m.b326 >= 1)

m.c1487 = Constraint(expr=   m.b299 + m.b310 + m.b320 >= 1)

m.c1488 = Constraint(expr=   m.b299 + m.b310 + m.b318 + m.b330 >= 1)

m.c1489 = Constraint(expr=   m.b299 + m.b310 + m.b318 + m.b326 + m.b331 >= 1)

m.c1490 = Constraint(expr=   m.b299 + m.b310 + m.b318 + m.b325 >= 1)

m.c1491 = Constraint(expr=   m.b299 + m.b310 + m.b318 + m.b321 >= 1)

m.c1492 = Constraint(expr=   m.b299 + m.b310 + m.b317 + m.b331 >= 1)

m.c1493 = Constraint(expr=   m.b299 + m.b310 + m.b317 + m.b326 >= 1)

m.c1494 = Constraint(expr=   m.b299 + m.b310 + m.b317 + m.b321 >= 1)

m.c1495 = Constraint(expr=   m.b299 + m.b309 + m.b330 >= 1)

m.c1496 = Constraint(expr=   m.b299 + m.b309 + m.b326 + m.b331 >= 1)

m.c1497 = Constraint(expr=   m.b299 + m.b309 + m.b325 >= 1)

m.c1498 = Constraint(expr=   m.b299 + m.b309 + m.b321 >= 1)

m.c1499 = Constraint(expr=   m.b299 + m.b309 + m.b318 + m.b331 >= 1)

m.c1500 = Constraint(expr=   m.b299 + m.b309 + m.b318 + m.b326 >= 1)

m.c1501 = Constraint(expr=   m.b299 + m.b309 + m.b318 + m.b321 >= 1)

m.c1502 = Constraint(expr=   m.b299 + m.b308 + m.b331 >= 1)

m.c1503 = Constraint(expr=   m.b299 + m.b308 + m.b326 >= 1)

m.c1504 = Constraint(expr=   m.b299 + m.b308 + m.b321 >= 1)

m.c1505 = Constraint(expr=   m.b299 + m.b306 + m.b328 >= 1)

m.c1506 = Constraint(expr=   m.b299 + m.b306 + m.b326 + m.b329 >= 1)

m.c1507 = Constraint(expr=   m.b299 + m.b306 + m.b325 + m.b330 >= 1)

m.c1508 = Constraint(expr=   m.b299 + m.b306 + m.b324 + m.b331 >= 1)

m.c1509 = Constraint(expr=   m.b299 + m.b306 + m.b323 >= 1)

m.c1510 = Constraint(expr=   m.b299 + m.b306 + m.b321 + m.b330 >= 1)

m.c1511 = Constraint(expr=   m.b299 + m.b306 + m.b321 + m.b326 + m.b331 >= 1)

m.c1512 = Constraint(expr=   m.b299 + m.b306 + m.b321 + m.b325 >= 1)

m.c1513 = Constraint(expr=   m.b299 + m.b306 + m.b320 >= 1)

m.c1514 = Constraint(expr=   m.b299 + m.b306 + m.b318 + m.b329 >= 1)

m.c1515 = Constraint(expr=   m.b299 + m.b306 + m.b318 + m.b326 + m.b330 >= 1)

m.c1516 = Constraint(expr=   m.b299 + m.b306 + m.b318 + m.b325 + m.b331 >= 1)

m.c1517 = Constraint(expr=   m.b299 + m.b306 + m.b318 + m.b324 >= 1)

m.c1518 = Constraint(expr=   m.b299 + m.b306 + m.b318 + m.b321 + m.b331 >= 1)

m.c1519 = Constraint(expr=   m.b299 + m.b306 + m.b318 + m.b321 + m.b326 >= 1)

m.c1520 = Constraint(expr=   m.b299 + m.b306 + m.b318 + m.b320 >= 1)

m.c1521 = Constraint(expr=   m.b299 + m.b306 + m.b317 + m.b330 >= 1)

m.c1522 = Constraint(expr=   m.b299 + m.b306 + m.b317 + m.b326 + m.b331 >= 1)

m.c1523 = Constraint(expr=   m.b299 + m.b306 + m.b317 + m.b325 >= 1)

m.c1524 = Constraint(expr=   m.b299 + m.b306 + m.b317 + m.b321 >= 1)

m.c1525 = Constraint(expr=   m.b299 + m.b306 + m.b316 + m.b330 >= 1)

m.c1526 = Constraint(expr=   m.b299 + m.b306 + m.b316 + m.b326 + m.b331 >= 1)

m.c1527 = Constraint(expr=   m.b299 + m.b306 + m.b316 + m.b325 >= 1)

m.c1528 = Constraint(expr=   m.b299 + m.b306 + m.b316 + m.b321 >= 1)

m.c1529 = Constraint(expr=   m.b299 + m.b306 + m.b315 + m.b331 >= 1)

m.c1530 = Constraint(expr=   m.b299 + m.b306 + m.b315 + m.b326 >= 1)

m.c1531 = Constraint(expr=   m.b299 + m.b306 + m.b315 + m.b321 >= 1)

m.c1532 = Constraint(expr=   m.b299 + m.b306 + m.b312 + m.b329 >= 1)

m.c1533 = Constraint(expr=   m.b299 + m.b306 + m.b312 + m.b326 + m.b330 >= 1)

m.c1534 = Constraint(expr=   m.b299 + m.b306 + m.b312 + m.b325 + m.b331 >= 1)

m.c1535 = Constraint(expr=   m.b299 + m.b306 + m.b312 + m.b324 >= 1)

m.c1536 = Constraint(expr=   m.b299 + m.b306 + m.b312 + m.b321 + m.b331 >= 1)

m.c1537 = Constraint(expr=   m.b299 + m.b306 + m.b312 + m.b321 + m.b326 >= 1)

m.c1538 = Constraint(expr=   m.b299 + m.b306 + m.b312 + m.b320 >= 1)

m.c1539 = Constraint(expr=   m.b299 + m.b306 + m.b312 + m.b318 + m.b330 >= 1)

m.c1540 = Constraint(expr=   m.b299 + m.b306 + m.b312 + m.b318 + m.b326 + m.b331 >= 1)

m.c1541 = Constraint(expr=   m.b299 + m.b306 + m.b312 + m.b318 + m.b325 >= 1)

m.c1542 = Constraint(expr=   m.b299 + m.b306 + m.b312 + m.b318 + m.b321 >= 1)

m.c1543 = Constraint(expr=   m.b299 + m.b306 + m.b312 + m.b317 + m.b330 >= 1)

m.c1544 = Constraint(expr=   m.b299 + m.b306 + m.b312 + m.b317 + m.b326 + m.b331 >= 1)

m.c1545 = Constraint(expr=   m.b299 + m.b306 + m.b312 + m.b317 + m.b325 >= 1)

m.c1546 = Constraint(expr=   m.b299 + m.b306 + m.b312 + m.b317 + m.b321 >= 1)

m.c1547 = Constraint(expr=   m.b299 + m.b306 + m.b312 + m.b316 + m.b331 >= 1)

m.c1548 = Constraint(expr=   m.b299 + m.b306 + m.b312 + m.b316 + m.b326 >= 1)

m.c1549 = Constraint(expr=   m.b299 + m.b306 + m.b312 + m.b316 + m.b321 >= 1)

m.c1550 = Constraint(expr=   m.b299 + m.b306 + m.b311 + m.b330 >= 1)

m.c1551 = Constraint(expr=   m.b299 + m.b306 + m.b311 + m.b325 >= 1)

m.c1552 = Constraint(expr=   m.b299 + m.b306 + m.b311 + m.b321 >= 1)

m.c1553 = Constraint(expr=   m.b299 + m.b306 + m.b311 + m.b318 + m.b330 >= 1)

m.c1554 = Constraint(expr=   m.b299 + m.b306 + m.b311 + m.b318 + m.b326 + m.b331 >= 1)

m.c1555 = Constraint(expr=   m.b299 + m.b306 + m.b311 + m.b318 + m.b325 >= 1)

m.c1556 = Constraint(expr=   m.b299 + m.b306 + m.b311 + m.b318 + m.b321 >= 1)

m.c1557 = Constraint(expr=   m.b299 + m.b306 + m.b311 + m.b317 + m.b331 >= 1)

m.c1558 = Constraint(expr=   m.b299 + m.b306 + m.b311 + m.b317 + m.b326 >= 1)

m.c1559 = Constraint(expr=   m.b299 + m.b306 + m.b311 + m.b317 + m.b321 >= 1)

m.c1560 = Constraint(expr=   m.b299 + m.b306 + m.b310 + m.b330 >= 1)

m.c1561 = Constraint(expr=   m.b299 + m.b306 + m.b310 + m.b326 + m.b331 >= 1)

m.c1562 = Constraint(expr=   m.b299 + m.b306 + m.b310 + m.b325 >= 1)

m.c1563 = Constraint(expr=   m.b299 + m.b306 + m.b310 + m.b321 >= 1)

m.c1564 = Constraint(expr=   m.b299 + m.b306 + m.b310 + m.b318 + m.b331 >= 1)

m.c1565 = Constraint(expr=   m.b299 + m.b306 + m.b310 + m.b318 + m.b326 >= 1)

m.c1566 = Constraint(expr=   m.b299 + m.b306 + m.b310 + m.b318 + m.b321 >= 1)

m.c1567 = Constraint(expr=   m.b299 + m.b306 + m.b309 + m.b331 >= 1)

m.c1568 = Constraint(expr=   m.b299 + m.b306 + m.b309 + m.b326 >= 1)

m.c1569 = Constraint(expr=   m.b299 + m.b306 + m.b309 + m.b321 >= 1)

m.c1570 = Constraint(expr=   m.b299 + m.b305 + m.b329 >= 1)

m.c1571 = Constraint(expr=   m.b299 + m.b305 + m.b326 + m.b330 >= 1)

m.c1572 = Constraint(expr=   m.b299 + m.b305 + m.b325 + m.b331 >= 1)

m.c1573 = Constraint(expr=   m.b299 + m.b305 + m.b324 >= 1)

m.c1574 = Constraint(expr=   m.b299 + m.b305 + m.b321 + m.b331 >= 1)

m.c1575 = Constraint(expr=   m.b299 + m.b305 + m.b321 + m.b326 >= 1)

m.c1576 = Constraint(expr=   m.b299 + m.b305 + m.b320 >= 1)

m.c1577 = Constraint(expr=   m.b299 + m.b305 + m.b318 + m.b330 >= 1)

m.c1578 = Constraint(expr=   m.b299 + m.b305 + m.b318 + m.b326 + m.b331 >= 1)

m.c1579 = Constraint(expr=   m.b299 + m.b305 + m.b318 + m.b325 >= 1)

m.c1580 = Constraint(expr=   m.b299 + m.b305 + m.b318 + m.b321 >= 1)

m.c1581 = Constraint(expr=   m.b299 + m.b305 + m.b317 + m.b331 >= 1)

m.c1582 = Constraint(expr=   m.b299 + m.b305 + m.b317 + m.b326 >= 1)

m.c1583 = Constraint(expr=   m.b299 + m.b305 + m.b317 + m.b321 >= 1)

m.c1584 = Constraint(expr=   m.b299 + m.b305 + m.b312 + m.b330 >= 1)

m.c1585 = Constraint(expr=   m.b299 + m.b305 + m.b312 + m.b326 + m.b331 >= 1)

m.c1586 = Constraint(expr=   m.b299 + m.b305 + m.b312 + m.b325 >= 1)

m.c1587 = Constraint(expr=   m.b299 + m.b305 + m.b312 + m.b321 >= 1)

m.c1588 = Constraint(expr=   m.b299 + m.b305 + m.b312 + m.b318 + m.b331 >= 1)

m.c1589 = Constraint(expr=   m.b299 + m.b305 + m.b312 + m.b318 + m.b326 >= 1)

m.c1590 = Constraint(expr=   m.b299 + m.b305 + m.b312 + m.b318 + m.b321 >= 1)

m.c1591 = Constraint(expr=   m.b299 + m.b305 + m.b311 + m.b331 >= 1)

m.c1592 = Constraint(expr=   m.b299 + m.b305 + m.b311 + m.b326 >= 1)

m.c1593 = Constraint(expr=   m.b299 + m.b305 + m.b311 + m.b321 >= 1)

m.c1594 = Constraint(expr=   m.b299 + m.b304 + m.b331 >= 1)

m.c1595 = Constraint(expr=   m.b299 + m.b304 + m.b326 >= 1)

m.c1596 = Constraint(expr=   m.b299 + m.b304 + m.b321 >= 1)

m.c1597 = Constraint(expr=   m.b299 + m.b302 + m.b329 >= 1)

m.c1598 = Constraint(expr=   m.b299 + m.b302 + m.b326 + m.b330 >= 1)

m.c1599 = Constraint(expr=   m.b299 + m.b302 + m.b325 + m.b331 >= 1)

m.c1600 = Constraint(expr=   m.b299 + m.b302 + m.b324 >= 1)

m.c1601 = Constraint(expr=   m.b299 + m.b302 + m.b321 + m.b331 >= 1)

m.c1602 = Constraint(expr=   m.b299 + m.b302 + m.b321 + m.b326 >= 1)

m.c1603 = Constraint(expr=   m.b299 + m.b302 + m.b320 >= 1)

m.c1604 = Constraint(expr=   m.b299 + m.b302 + m.b318 + m.b330 >= 1)

m.c1605 = Constraint(expr=   m.b299 + m.b302 + m.b318 + m.b326 + m.b331 >= 1)

m.c1606 = Constraint(expr=   m.b299 + m.b302 + m.b318 + m.b325 >= 1)

m.c1607 = Constraint(expr=   m.b299 + m.b302 + m.b318 + m.b321 >= 1)

m.c1608 = Constraint(expr=   m.b299 + m.b302 + m.b317 + m.b330 >= 1)

m.c1609 = Constraint(expr=   m.b299 + m.b302 + m.b317 + m.b326 + m.b331 >= 1)

m.c1610 = Constraint(expr=   m.b299 + m.b302 + m.b317 + m.b325 >= 1)

m.c1611 = Constraint(expr=   m.b299 + m.b302 + m.b317 + m.b321 >= 1)

m.c1612 = Constraint(expr=   m.b299 + m.b302 + m.b316 + m.b331 >= 1)

m.c1613 = Constraint(expr=   m.b299 + m.b302 + m.b316 + m.b326 >= 1)

m.c1614 = Constraint(expr=   m.b299 + m.b302 + m.b316 + m.b321 >= 1)

m.c1615 = Constraint(expr=   m.b299 + m.b302 + m.b312 + m.b330 >= 1)

m.c1616 = Constraint(expr=   m.b299 + m.b302 + m.b312 + m.b326 + m.b331 >= 1)

m.c1617 = Constraint(expr=   m.b299 + m.b302 + m.b312 + m.b325 >= 1)

m.c1618 = Constraint(expr=   m.b299 + m.b302 + m.b312 + m.b321 >= 1)

m.c1619 = Constraint(expr=   m.b299 + m.b302 + m.b312 + m.b318 + m.b330 >= 1)

m.c1620 = Constraint(expr=   m.b299 + m.b302 + m.b312 + m.b318 + m.b326 + m.b331 >= 1)

m.c1621 = Constraint(expr=   m.b299 + m.b302 + m.b312 + m.b318 + m.b325 >= 1)

m.c1622 = Constraint(expr=   m.b299 + m.b302 + m.b312 + m.b318 + m.b321 >= 1)

m.c1623 = Constraint(expr=   m.b299 + m.b302 + m.b312 + m.b317 + m.b331 >= 1)

m.c1624 = Constraint(expr=   m.b299 + m.b302 + m.b312 + m.b317 + m.b326 >= 1)

m.c1625 = Constraint(expr=   m.b299 + m.b302 + m.b312 + m.b317 + m.b321 >= 1)

m.c1626 = Constraint(expr=   m.b299 + m.b302 + m.b311 + m.b330 >= 1)

m.c1627 = Constraint(expr=   m.b299 + m.b302 + m.b311 + m.b326 + m.b331 >= 1)

m.c1628 = Constraint(expr=   m.b299 + m.b302 + m.b311 + m.b325 >= 1)

m.c1629 = Constraint(expr=   m.b299 + m.b302 + m.b311 + m.b321 >= 1)

m.c1630 = Constraint(expr=   m.b299 + m.b302 + m.b311 + m.b318 + m.b331 >= 1)

m.c1631 = Constraint(expr=   m.b299 + m.b302 + m.b311 + m.b318 + m.b326 >= 1)

m.c1632 = Constraint(expr=   m.b299 + m.b302 + m.b311 + m.b318 + m.b321 >= 1)

m.c1633 = Constraint(expr=   m.b299 + m.b302 + m.b310 + m.b331 >= 1)

m.c1634 = Constraint(expr=   m.b299 + m.b302 + m.b310 + m.b326 >= 1)

m.c1635 = Constraint(expr=   m.b299 + m.b302 + m.b310 + m.b321 >= 1)

m.c1636 = Constraint(expr=   m.b299 + m.b302 + m.b306 + m.b330 >= 1)

m.c1637 = Constraint(expr=   m.b299 + m.b302 + m.b306 + m.b326 + m.b331 >= 1)

m.c1638 = Constraint(expr=   m.b299 + m.b302 + m.b306 + m.b325 >= 1)

m.c1639 = Constraint(expr=   m.b299 + m.b302 + m.b306 + m.b321 >= 1)

m.c1640 = Constraint(expr=   m.b299 + m.b302 + m.b306 + m.b318 + m.b331 >= 1)

m.c1641 = Constraint(expr=   m.b299 + m.b302 + m.b306 + m.b318 + m.b326 >= 1)

m.c1642 = Constraint(expr=   m.b299 + m.b302 + m.b306 + m.b318 + m.b321 >= 1)

m.c1643 = Constraint(expr=   m.b299 + m.b302 + m.b306 + m.b317 + m.b331 >= 1)

m.c1644 = Constraint(expr=   m.b299 + m.b302 + m.b306 + m.b317 + m.b326 >= 1)

m.c1645 = Constraint(expr=   m.b299 + m.b302 + m.b306 + m.b317 + m.b321 >= 1)

m.c1646 = Constraint(expr=   m.b299 + m.b302 + m.b306 + m.b312 + m.b331 >= 1)

m.c1647 = Constraint(expr=   m.b299 + m.b302 + m.b306 + m.b312 + m.b326 >= 1)

m.c1648 = Constraint(expr=   m.b299 + m.b302 + m.b306 + m.b312 + m.b321 >= 1)

m.c1649 = Constraint(expr=   m.b299 + m.b302 + m.b306 + m.b311 + m.b331 >= 1)

m.c1650 = Constraint(expr=   m.b299 + m.b302 + m.b306 + m.b311 + m.b326 >= 1)

m.c1651 = Constraint(expr=   m.b299 + m.b302 + m.b306 + m.b311 + m.b321 >= 1)

m.c1652 = Constraint(expr=   m.b299 + m.b302 + m.b305 + m.b331 >= 1)

m.c1653 = Constraint(expr=   m.b299 + m.b302 + m.b305 + m.b326 >= 1)

m.c1654 = Constraint(expr=   m.b299 + m.b302 + m.b305 + m.b321 >= 1)

m.c1655 = Constraint(expr=   m.b299 + m.b301 + m.b331 >= 1)

m.c1656 = Constraint(expr=   m.b299 + m.b301 + m.b326 >= 1)

m.c1657 = Constraint(expr=   m.b299 + m.b301 + m.b321 >= 1)

m.c1658 = Constraint(expr=   m.b298 + m.b329 >= 1)

m.c1659 = Constraint(expr=   m.b298 + m.b326 + m.b330 >= 1)

m.c1660 = Constraint(expr=   m.b298 + m.b325 + m.b331 >= 1)

m.c1661 = Constraint(expr=   m.b298 + m.b324 >= 1)

m.c1662 = Constraint(expr=   m.b298 + m.b321 + m.b331 >= 1)

m.c1663 = Constraint(expr=   m.b298 + m.b321 + m.b326 >= 1)

m.c1664 = Constraint(expr=   m.b298 + m.b320 >= 1)

m.c1665 = Constraint(expr=   m.b298 + m.b318 + m.b330 >= 1)

m.c1666 = Constraint(expr=   m.b298 + m.b318 + m.b326 + m.b331 >= 1)

m.c1667 = Constraint(expr=   m.b298 + m.b318 + m.b325 >= 1)

m.c1668 = Constraint(expr=   m.b298 + m.b318 + m.b321 >= 1)

m.c1669 = Constraint(expr=   m.b298 + m.b317 + m.b330 >= 1)

m.c1670 = Constraint(expr=   m.b298 + m.b317 + m.b326 + m.b331 >= 1)

m.c1671 = Constraint(expr=   m.b298 + m.b317 + m.b325 >= 1)

m.c1672 = Constraint(expr=   m.b298 + m.b317 + m.b321 >= 1)

m.c1673 = Constraint(expr=   m.b298 + m.b316 + m.b331 >= 1)

m.c1674 = Constraint(expr=   m.b298 + m.b316 + m.b326 >= 1)

m.c1675 = Constraint(expr=   m.b298 + m.b316 + m.b321 >= 1)

m.c1676 = Constraint(expr=   m.b298 + m.b312 + m.b330 >= 1)

m.c1677 = Constraint(expr=   m.b298 + m.b312 + m.b325 + m.b331 >= 1)

m.c1678 = Constraint(expr=   m.b298 + m.b312 + m.b324 >= 1)

m.c1679 = Constraint(expr=   m.b298 + m.b312 + m.b321 >= 1)

m.c1680 = Constraint(expr=   m.b298 + m.b312 + m.b318 + m.b330 >= 1)

m.c1681 = Constraint(expr=   m.b298 + m.b312 + m.b318 + m.b326 + m.b331 >= 1)

m.c1682 = Constraint(expr=   m.b298 + m.b312 + m.b318 + m.b325 >= 1)

m.c1683 = Constraint(expr=   m.b298 + m.b312 + m.b318 + m.b321 >= 1)

m.c1684 = Constraint(expr=   m.b298 + m.b312 + m.b317 + m.b331 >= 1)

m.c1685 = Constraint(expr=   m.b298 + m.b312 + m.b317 + m.b326 >= 1)

m.c1686 = Constraint(expr=   m.b298 + m.b312 + m.b317 + m.b321 >= 1)

m.c1687 = Constraint(expr=   m.b298 + m.b311 + m.b330 >= 1)

m.c1688 = Constraint(expr=   m.b298 + m.b311 + m.b326 + m.b331 >= 1)

m.c1689 = Constraint(expr=   m.b298 + m.b311 + m.b325 >= 1)

m.c1690 = Constraint(expr=   m.b298 + m.b311 + m.b321 >= 1)

m.c1691 = Constraint(expr=   m.b298 + m.b311 + m.b318 + m.b331 >= 1)

m.c1692 = Constraint(expr=   m.b298 + m.b311 + m.b318 + m.b326 >= 1)

m.c1693 = Constraint(expr=   m.b298 + m.b311 + m.b318 + m.b321 >= 1)

m.c1694 = Constraint(expr=   m.b298 + m.b310 + m.b331 >= 1)

m.c1695 = Constraint(expr=   m.b298 + m.b310 + m.b326 >= 1)

m.c1696 = Constraint(expr=   m.b298 + m.b310 + m.b321 >= 1)

m.c1697 = Constraint(expr=   m.b298 + m.b306 + m.b330 >= 1)

m.c1698 = Constraint(expr=   m.b298 + m.b306 + m.b326 + m.b331 >= 1)

m.c1699 = Constraint(expr=   m.b298 + m.b306 + m.b325 >= 1)

m.c1700 = Constraint(expr=   m.b298 + m.b306 + m.b321 >= 1)

m.c1701 = Constraint(expr=   m.b298 + m.b306 + m.b318 + m.b331 >= 1)

m.c1702 = Constraint(expr=   m.b298 + m.b306 + m.b318 + m.b326 >= 1)

m.c1703 = Constraint(expr=   m.b298 + m.b306 + m.b318 + m.b321 >= 1)

m.c1704 = Constraint(expr=   m.b298 + m.b306 + m.b312 + m.b331 >= 1)

m.c1705 = Constraint(expr=   m.b298 + m.b306 + m.b312 + m.b326 >= 1)

m.c1706 = Constraint(expr=   m.b298 + m.b306 + m.b312 + m.b321 >= 1)

m.c1707 = Constraint(expr=   m.b298 + m.b306 + m.b311 + m.b331 >= 1)

m.c1708 = Constraint(expr=   m.b298 + m.b306 + m.b311 + m.b326 >= 1)

m.c1709 = Constraint(expr=   m.b298 + m.b306 + m.b311 + m.b321 >= 1)

m.c1710 = Constraint(expr=   m.b298 + m.b305 + m.b331 >= 1)

m.c1711 = Constraint(expr=   m.b298 + m.b305 + m.b326 >= 1)

m.c1712 = Constraint(expr=   m.b298 + m.b305 + m.b321 >= 1)

m.c1713 = Constraint(expr=   m.b298 + m.b302 + m.b331 >= 1)

m.c1714 = Constraint(expr=   m.b298 + m.b302 + m.b326 >= 1)

m.c1715 = Constraint(expr=   m.b298 + m.b302 + m.b321 >= 1)

m.c1716 = Constraint(expr=   m.b298 + m.b302 + m.b312 + m.b331 >= 1)

m.c1717 = Constraint(expr=   m.b298 + m.b302 + m.b312 + m.b326 >= 1)

m.c1718 = Constraint(expr=   m.b298 + m.b302 + m.b312 + m.b321 >= 1)

m.c1719 = Constraint(expr=   m.b297 + m.b331 >= 1)

m.c1720 = Constraint(expr=   m.b297 + m.b326 >= 1)

m.c1721 = Constraint(expr=   m.b297 + m.b321 >= 1)

m.c1722 = Constraint(expr=   m.b296 + m.b327 >= 1)

m.c1723 = Constraint(expr=   m.b296 + m.b326 + m.b328 >= 1)

m.c1724 = Constraint(expr=   m.b296 + m.b325 + m.b329 >= 1)

m.c1725 = Constraint(expr=   m.b296 + m.b324 + m.b330 >= 1)

m.c1726 = Constraint(expr=   m.b296 + m.b323 + m.b331 >= 1)

m.c1727 = Constraint(expr=   m.b296 + m.b322 >= 1)

m.c1728 = Constraint(expr=   m.b296 + m.b321 + m.b329 >= 1)

m.c1729 = Constraint(expr=   m.b296 + m.b321 + m.b326 + m.b330 >= 1)

m.c1730 = Constraint(expr=   m.b296 + m.b321 + m.b324 >= 1)

m.c1731 = Constraint(expr=   m.b296 + m.b320 + m.b331 >= 1)

m.c1732 = Constraint(expr=   m.b296 + m.b320 + m.b326 >= 1)

m.c1733 = Constraint(expr=   m.b296 + m.b319 >= 1)

m.c1734 = Constraint(expr=   m.b296 + m.b318 + m.b328 >= 1)

m.c1735 = Constraint(expr=   m.b296 + m.b318 + m.b325 + m.b329 >= 1)

m.c1736 = Constraint(expr=   m.b296 + m.b318 + m.b324 + m.b331 >= 1)

m.c1737 = Constraint(expr=   m.b296 + m.b318 + m.b323 >= 1)

m.c1738 = Constraint(expr=   m.b296 + m.b318 + m.b321 + m.b329 >= 1)

m.c1739 = Constraint(expr=   m.b296 + m.b318 + m.b321 + m.b326 + m.b330 >= 1)

m.c1740 = Constraint(expr=   m.b296 + m.b318 + m.b321 + m.b325 + m.b331 >= 1)

m.c1741 = Constraint(expr=   m.b296 + m.b318 + m.b321 + m.b324 >= 1)

m.c1742 = Constraint(expr=   m.b296 + m.b318 + m.b320 >= 1)

m.c1743 = Constraint(expr=   m.b296 + m.b317 + m.b328 >= 1)

m.c1744 = Constraint(expr=   m.b296 + m.b317 + m.b326 + m.b329 >= 1)

m.c1745 = Constraint(expr=   m.b296 + m.b317 + m.b325 + m.b330 >= 1)

m.c1746 = Constraint(expr=   m.b296 + m.b317 + m.b324 + m.b331 >= 1)

m.c1747 = Constraint(expr=   m.b296 + m.b317 + m.b323 >= 1)

m.c1748 = Constraint(expr=   m.b296 + m.b317 + m.b321 + m.b330 >= 1)

m.c1749 = Constraint(expr=   m.b296 + m.b317 + m.b321 + m.b326 + m.b331 >= 1)

m.c1750 = Constraint(expr=   m.b296 + m.b317 + m.b321 + m.b325 >= 1)

m.c1751 = Constraint(expr=   m.b296 + m.b317 + m.b320 >= 1)

m.c1752 = Constraint(expr=   m.b296 + m.b316 + m.b329 >= 1)

m.c1753 = Constraint(expr=   m.b296 + m.b316 + m.b326 + m.b330 >= 1)

m.c1754 = Constraint(expr=   m.b296 + m.b316 + m.b325 + m.b331 >= 1)

m.c1755 = Constraint(expr=   m.b296 + m.b316 + m.b324 >= 1)

m.c1756 = Constraint(expr=   m.b296 + m.b316 + m.b321 + m.b331 >= 1)

m.c1757 = Constraint(expr=   m.b296 + m.b316 + m.b321 + m.b326 >= 1)

m.c1758 = Constraint(expr=   m.b296 + m.b316 + m.b320 >= 1)

m.c1759 = Constraint(expr=   m.b296 + m.b315 + m.b330 >= 1)

m.c1760 = Constraint(expr=   m.b296 + m.b315 + m.b326 + m.b331 >= 1)

m.c1761 = Constraint(expr=   m.b296 + m.b315 + m.b325 >= 1)

m.c1762 = Constraint(expr=   m.b296 + m.b315 + m.b321 >= 1)

m.c1763 = Constraint(expr=   m.b296 + m.b314 + m.b331 >= 1)

m.c1764 = Constraint(expr=   m.b296 + m.b314 + m.b326 >= 1)

m.c1765 = Constraint(expr=   m.b296 + m.b314 + m.b321 >= 1)

m.c1766 = Constraint(expr=   m.b296 + m.b312 + m.b328 >= 1)

m.c1767 = Constraint(expr=   m.b296 + m.b312 + m.b325 + m.b329 >= 1)

m.c1768 = Constraint(expr=   m.b296 + m.b312 + m.b324 + m.b330 >= 1)

m.c1769 = Constraint(expr=   m.b296 + m.b312 + m.b323 >= 1)

m.c1770 = Constraint(expr=   m.b296 + m.b312 + m.b321 + m.b329 >= 1)

m.c1771 = Constraint(expr=   m.b296 + m.b312 + m.b321 + m.b326 + m.b330 >= 1)

m.c1772 = Constraint(expr=   m.b296 + m.b312 + m.b321 + m.b325 + m.b331 >= 1)

m.c1773 = Constraint(expr=   m.b296 + m.b312 + m.b321 + m.b324 >= 1)

m.c1774 = Constraint(expr=   m.b296 + m.b312 + m.b320 >= 1)

m.c1775 = Constraint(expr=   m.b296 + m.b312 + m.b318 + m.b328 >= 1)

m.c1776 = Constraint(expr=   m.b296 + m.b312 + m.b318 + m.b326 + m.b329 >= 1)

m.c1777 = Constraint(expr=   m.b296 + m.b312 + m.b318 + m.b325 + m.b330 >= 1)

m.c1778 = Constraint(expr=   m.b296 + m.b312 + m.b318 + m.b324 + m.b331 >= 1)

m.c1779 = Constraint(expr=   m.b296 + m.b312 + m.b318 + m.b323 >= 1)

m.c1780 = Constraint(expr=   m.b296 + m.b312 + m.b318 + m.b321 + m.b330 >= 1)

m.c1781 = Constraint(expr=   m.b296 + m.b312 + m.b318 + m.b321 + m.b326 + m.b331 >= 1)

m.c1782 = Constraint(expr=   m.b296 + m.b312 + m.b318 + m.b321 + m.b325 >= 1)

m.c1783 = Constraint(expr=   m.b296 + m.b312 + m.b318 + m.b320 >= 1)

m.c1784 = Constraint(expr=   m.b296 + m.b312 + m.b317 + m.b329 >= 1)

m.c1785 = Constraint(expr=   m.b296 + m.b312 + m.b317 + m.b326 + m.b330 >= 1)

m.c1786 = Constraint(expr=   m.b296 + m.b312 + m.b317 + m.b325 + m.b331 >= 1)

m.c1787 = Constraint(expr=   m.b296 + m.b312 + m.b317 + m.b324 >= 1)

m.c1788 = Constraint(expr=   m.b296 + m.b312 + m.b317 + m.b321 + m.b331 >= 1)

m.c1789 = Constraint(expr=   m.b296 + m.b312 + m.b317 + m.b321 + m.b326 >= 1)

m.c1790 = Constraint(expr=   m.b296 + m.b312 + m.b317 + m.b320 >= 1)

m.c1791 = Constraint(expr=   m.b296 + m.b312 + m.b316 + m.b330 >= 1)

m.c1792 = Constraint(expr=   m.b296 + m.b312 + m.b316 + m.b326 + m.b331 >= 1)

m.c1793 = Constraint(expr=   m.b296 + m.b312 + m.b316 + m.b325 >= 1)

m.c1794 = Constraint(expr=   m.b296 + m.b312 + m.b316 + m.b321 >= 1)

m.c1795 = Constraint(expr=   m.b296 + m.b312 + m.b315 + m.b331 >= 1)

m.c1796 = Constraint(expr=   m.b296 + m.b312 + m.b315 + m.b326 >= 1)

m.c1797 = Constraint(expr=   m.b296 + m.b312 + m.b315 + m.b321 >= 1)

m.c1798 = Constraint(expr=   m.b296 + m.b312 + m.b314 + m.b331 >= 1)

m.c1799 = Constraint(expr=   m.b296 + m.b312 + m.b314 + m.b326 >= 1)

m.c1800 = Constraint(expr=   m.b296 + m.b312 + m.b314 + m.b321 >= 1)

m.c1801 = Constraint(expr=   m.b296 + m.b311 + m.b328 >= 1)

m.c1802 = Constraint(expr=   m.b296 + m.b311 + m.b326 + m.b329 >= 1)

m.c1803 = Constraint(expr=   m.b296 + m.b311 + m.b325 + m.b330 >= 1)

m.c1804 = Constraint(expr=   m.b296 + m.b311 + m.b324 + m.b331 >= 1)

m.c1805 = Constraint(expr=   m.b296 + m.b311 + m.b323 >= 1)

m.c1806 = Constraint(expr=   m.b296 + m.b311 + m.b321 + m.b330 >= 1)

m.c1807 = Constraint(expr=   m.b296 + m.b311 + m.b321 + m.b326 + m.b331 >= 1)

m.c1808 = Constraint(expr=   m.b296 + m.b311 + m.b321 + m.b325 >= 1)

m.c1809 = Constraint(expr=   m.b296 + m.b311 + m.b320 >= 1)

m.c1810 = Constraint(expr=   m.b296 + m.b311 + m.b318 + m.b329 >= 1)

m.c1811 = Constraint(expr=   m.b296 + m.b311 + m.b318 + m.b326 + m.b330 >= 1)

m.c1812 = Constraint(expr=   m.b296 + m.b311 + m.b318 + m.b325 + m.b331 >= 1)

m.c1813 = Constraint(expr=   m.b296 + m.b311 + m.b318 + m.b324 >= 1)

m.c1814 = Constraint(expr=   m.b296 + m.b311 + m.b318 + m.b321 + m.b331 >= 1)

m.c1815 = Constraint(expr=   m.b296 + m.b311 + m.b318 + m.b321 + m.b326 >= 1)

m.c1816 = Constraint(expr=   m.b296 + m.b311 + m.b318 + m.b320 >= 1)

m.c1817 = Constraint(expr=   m.b296 + m.b311 + m.b317 + m.b330 >= 1)

m.c1818 = Constraint(expr=   m.b296 + m.b311 + m.b317 + m.b326 + m.b331 >= 1)

m.c1819 = Constraint(expr=   m.b296 + m.b311 + m.b317 + m.b325 >= 1)

m.c1820 = Constraint(expr=   m.b296 + m.b311 + m.b317 + m.b321 >= 1)

m.c1821 = Constraint(expr=   m.b296 + m.b311 + m.b316 + m.b331 >= 1)

m.c1822 = Constraint(expr=   m.b296 + m.b311 + m.b316 + m.b326 >= 1)

m.c1823 = Constraint(expr=   m.b296 + m.b311 + m.b316 + m.b321 >= 1)

m.c1824 = Constraint(expr=   m.b296 + m.b311 + m.b315 + m.b331 >= 1)

m.c1825 = Constraint(expr=   m.b296 + m.b311 + m.b315 + m.b326 >= 1)

m.c1826 = Constraint(expr=   m.b296 + m.b311 + m.b315 + m.b321 >= 1)

m.c1827 = Constraint(expr=   m.b296 + m.b310 + m.b329 >= 1)

m.c1828 = Constraint(expr=   m.b296 + m.b310 + m.b326 + m.b330 >= 1)

m.c1829 = Constraint(expr=   m.b296 + m.b310 + m.b325 + m.b331 >= 1)

m.c1830 = Constraint(expr=   m.b296 + m.b310 + m.b324 >= 1)

m.c1831 = Constraint(expr=   m.b296 + m.b310 + m.b321 + m.b331 >= 1)

m.c1832 = Constraint(expr=   m.b296 + m.b310 + m.b321 + m.b326 >= 1)

m.c1833 = Constraint(expr=   m.b296 + m.b310 + m.b320 >= 1)

m.c1834 = Constraint(expr=   m.b296 + m.b310 + m.b318 + m.b330 >= 1)

m.c1835 = Constraint(expr=   m.b296 + m.b310 + m.b318 + m.b326 + m.b331 >= 1)

m.c1836 = Constraint(expr=   m.b296 + m.b310 + m.b318 + m.b325 >= 1)

m.c1837 = Constraint(expr=   m.b296 + m.b310 + m.b318 + m.b321 >= 1)

m.c1838 = Constraint(expr=   m.b296 + m.b310 + m.b317 + m.b331 >= 1)

m.c1839 = Constraint(expr=   m.b296 + m.b310 + m.b317 + m.b326 >= 1)

m.c1840 = Constraint(expr=   m.b296 + m.b310 + m.b317 + m.b321 >= 1)

m.c1841 = Constraint(expr=   m.b296 + m.b310 + m.b316 + m.b331 >= 1)

m.c1842 = Constraint(expr=   m.b296 + m.b310 + m.b316 + m.b326 >= 1)

m.c1843 = Constraint(expr=   m.b296 + m.b310 + m.b316 + m.b321 >= 1)

m.c1844 = Constraint(expr=   m.b296 + m.b309 + m.b330 >= 1)

m.c1845 = Constraint(expr=   m.b296 + m.b309 + m.b326 + m.b331 >= 1)

m.c1846 = Constraint(expr=   m.b296 + m.b309 + m.b325 >= 1)

m.c1847 = Constraint(expr=   m.b296 + m.b309 + m.b321 >= 1)

m.c1848 = Constraint(expr=   m.b296 + m.b309 + m.b318 + m.b331 >= 1)

m.c1849 = Constraint(expr=   m.b296 + m.b309 + m.b318 + m.b326 >= 1)

m.c1850 = Constraint(expr=   m.b296 + m.b309 + m.b318 + m.b321 >= 1)

m.c1851 = Constraint(expr=   m.b296 + m.b309 + m.b317 + m.b331 >= 1)

m.c1852 = Constraint(expr=   m.b296 + m.b309 + m.b317 + m.b326 >= 1)

m.c1853 = Constraint(expr=   m.b296 + m.b309 + m.b317 + m.b321 >= 1)

m.c1854 = Constraint(expr=   m.b296 + m.b308 + m.b331 >= 1)

m.c1855 = Constraint(expr=   m.b296 + m.b308 + m.b326 >= 1)

m.c1856 = Constraint(expr=   m.b296 + m.b308 + m.b321 >= 1)

m.c1857 = Constraint(expr=   m.b296 + m.b306 + m.b328 >= 1)

m.c1858 = Constraint(expr=   m.b296 + m.b306 + m.b326 + m.b329 >= 1)

m.c1859 = Constraint(expr=   m.b296 + m.b306 + m.b325 + m.b330 >= 1)

m.c1860 = Constraint(expr=   m.b296 + m.b306 + m.b324 + m.b331 >= 1)

m.c1861 = Constraint(expr=   m.b296 + m.b306 + m.b323 >= 1)

m.c1862 = Constraint(expr=   m.b296 + m.b306 + m.b321 + m.b330 >= 1)

m.c1863 = Constraint(expr=   m.b296 + m.b306 + m.b321 + m.b326 + m.b331 >= 1)

m.c1864 = Constraint(expr=   m.b296 + m.b306 + m.b321 + m.b325 >= 1)

m.c1865 = Constraint(expr=   m.b296 + m.b306 + m.b320 >= 1)

m.c1866 = Constraint(expr=   m.b296 + m.b306 + m.b318 + m.b329 >= 1)

m.c1867 = Constraint(expr=   m.b296 + m.b306 + m.b318 + m.b326 + m.b330 >= 1)

m.c1868 = Constraint(expr=   m.b296 + m.b306 + m.b318 + m.b325 + m.b331 >= 1)

m.c1869 = Constraint(expr=   m.b296 + m.b306 + m.b318 + m.b324 >= 1)

m.c1870 = Constraint(expr=   m.b296 + m.b306 + m.b318 + m.b321 + m.b331 >= 1)

m.c1871 = Constraint(expr=   m.b296 + m.b306 + m.b318 + m.b321 + m.b326 >= 1)

m.c1872 = Constraint(expr=   m.b296 + m.b306 + m.b318 + m.b320 >= 1)

m.c1873 = Constraint(expr=   m.b296 + m.b306 + m.b317 + m.b329 >= 1)

m.c1874 = Constraint(expr=   m.b296 + m.b306 + m.b317 + m.b326 + m.b330 >= 1)

m.c1875 = Constraint(expr=   m.b296 + m.b306 + m.b317 + m.b325 + m.b331 >= 1)

m.c1876 = Constraint(expr=   m.b296 + m.b306 + m.b317 + m.b324 >= 1)

m.c1877 = Constraint(expr=   m.b296 + m.b306 + m.b317 + m.b321 + m.b331 >= 1)

m.c1878 = Constraint(expr=   m.b296 + m.b306 + m.b317 + m.b321 + m.b326 >= 1)

m.c1879 = Constraint(expr=   m.b296 + m.b306 + m.b317 + m.b320 >= 1)

m.c1880 = Constraint(expr=   m.b296 + m.b306 + m.b316 + m.b330 >= 1)

m.c1881 = Constraint(expr=   m.b296 + m.b306 + m.b316 + m.b326 + m.b331 >= 1)

m.c1882 = Constraint(expr=   m.b296 + m.b306 + m.b316 + m.b325 >= 1)

m.c1883 = Constraint(expr=   m.b296 + m.b306 + m.b316 + m.b321 >= 1)

m.c1884 = Constraint(expr=   m.b296 + m.b306 + m.b315 + m.b331 >= 1)

m.c1885 = Constraint(expr=   m.b296 + m.b306 + m.b315 + m.b326 >= 1)

m.c1886 = Constraint(expr=   m.b296 + m.b306 + m.b315 + m.b321 >= 1)

m.c1887 = Constraint(expr=   m.b296 + m.b306 + m.b312 + m.b329 >= 1)

m.c1888 = Constraint(expr=   m.b296 + m.b306 + m.b312 + m.b326 + m.b330 >= 1)

m.c1889 = Constraint(expr=   m.b296 + m.b306 + m.b312 + m.b325 + m.b331 >= 1)

m.c1890 = Constraint(expr=   m.b296 + m.b306 + m.b312 + m.b324 >= 1)

m.c1891 = Constraint(expr=   m.b296 + m.b306 + m.b312 + m.b321 + m.b331 >= 1)

m.c1892 = Constraint(expr=   m.b296 + m.b306 + m.b312 + m.b321 + m.b326 >= 1)

m.c1893 = Constraint(expr=   m.b296 + m.b306 + m.b312 + m.b320 >= 1)

m.c1894 = Constraint(expr=   m.b296 + m.b306 + m.b312 + m.b318 + m.b329 >= 1)

m.c1895 = Constraint(expr=   m.b296 + m.b306 + m.b312 + m.b318 + m.b326 + m.b330 >= 1)

m.c1896 = Constraint(expr=   m.b296 + m.b306 + m.b312 + m.b318 + m.b325 >= 1)

m.c1897 = Constraint(expr=   m.b296 + m.b306 + m.b312 + m.b318 + m.b321 >= 1)

m.c1898 = Constraint(expr=   m.b296 + m.b306 + m.b312 + m.b317 + m.b330 >= 1)

m.c1899 = Constraint(expr=   m.b296 + m.b306 + m.b312 + m.b317 + m.b326 + m.b331 >= 1)

m.c1900 = Constraint(expr=   m.b296 + m.b306 + m.b312 + m.b317 + m.b325 >= 1)

m.c1901 = Constraint(expr=   m.b296 + m.b306 + m.b312 + m.b317 + m.b321 >= 1)

m.c1902 = Constraint(expr=   m.b296 + m.b306 + m.b312 + m.b316 + m.b331 >= 1)

m.c1903 = Constraint(expr=   m.b296 + m.b306 + m.b312 + m.b316 + m.b326 >= 1)

m.c1904 = Constraint(expr=   m.b296 + m.b306 + m.b312 + m.b316 + m.b321 >= 1)

m.c1905 = Constraint(expr=   m.b296 + m.b306 + m.b311 + m.b329 >= 1)

m.c1906 = Constraint(expr=   m.b296 + m.b306 + m.b311 + m.b326 + m.b330 >= 1)

m.c1907 = Constraint(expr=   m.b296 + m.b306 + m.b311 + m.b325 + m.b331 >= 1)

m.c1908 = Constraint(expr=   m.b296 + m.b306 + m.b311 + m.b324 >= 1)

m.c1909 = Constraint(expr=   m.b296 + m.b306 + m.b311 + m.b321 + m.b331 >= 1)

m.c1910 = Constraint(expr=   m.b296 + m.b306 + m.b311 + m.b321 + m.b326 >= 1)

m.c1911 = Constraint(expr=   m.b296 + m.b306 + m.b311 + m.b320 >= 1)

m.c1912 = Constraint(expr=   m.b296 + m.b306 + m.b311 + m.b318 + m.b330 >= 1)

m.c1913 = Constraint(expr=   m.b296 + m.b306 + m.b311 + m.b318 + m.b326 + m.b331 >= 1)

m.c1914 = Constraint(expr=   m.b296 + m.b306 + m.b311 + m.b318 + m.b325 >= 1)

m.c1915 = Constraint(expr=   m.b296 + m.b306 + m.b311 + m.b318 + m.b321 >= 1)

m.c1916 = Constraint(expr=   m.b296 + m.b306 + m.b311 + m.b317 + m.b331 >= 1)

m.c1917 = Constraint(expr=   m.b296 + m.b306 + m.b311 + m.b317 + m.b326 >= 1)

m.c1918 = Constraint(expr=   m.b296 + m.b306 + m.b311 + m.b317 + m.b321 >= 1)

m.c1919 = Constraint(expr=   m.b296 + m.b306 + m.b310 + m.b330 >= 1)

m.c1920 = Constraint(expr=   m.b296 + m.b306 + m.b310 + m.b326 + m.b331 >= 1)

m.c1921 = Constraint(expr=   m.b296 + m.b306 + m.b310 + m.b325 >= 1)

m.c1922 = Constraint(expr=   m.b296 + m.b306 + m.b310 + m.b321 >= 1)

m.c1923 = Constraint(expr=   m.b296 + m.b306 + m.b310 + m.b318 + m.b331 >= 1)

m.c1924 = Constraint(expr=   m.b296 + m.b306 + m.b310 + m.b318 + m.b326 >= 1)

m.c1925 = Constraint(expr=   m.b296 + m.b306 + m.b310 + m.b318 + m.b321 >= 1)

m.c1926 = Constraint(expr=   m.b296 + m.b306 + m.b309 + m.b331 >= 1)

m.c1927 = Constraint(expr=   m.b296 + m.b306 + m.b309 + m.b326 >= 1)

m.c1928 = Constraint(expr=   m.b296 + m.b306 + m.b309 + m.b321 >= 1)

m.c1929 = Constraint(expr=   m.b296 + m.b305 + m.b329 >= 1)

m.c1930 = Constraint(expr=   m.b296 + m.b305 + m.b326 + m.b330 >= 1)

m.c1931 = Constraint(expr=   m.b296 + m.b305 + m.b325 + m.b331 >= 1)

m.c1932 = Constraint(expr=   m.b296 + m.b305 + m.b324 >= 1)

m.c1933 = Constraint(expr=   m.b296 + m.b305 + m.b321 + m.b331 >= 1)

m.c1934 = Constraint(expr=   m.b296 + m.b305 + m.b321 + m.b326 >= 1)

m.c1935 = Constraint(expr=   m.b296 + m.b305 + m.b320 >= 1)

m.c1936 = Constraint(expr=   m.b296 + m.b305 + m.b318 + m.b330 >= 1)

m.c1937 = Constraint(expr=   m.b296 + m.b305 + m.b318 + m.b326 + m.b331 >= 1)

m.c1938 = Constraint(expr=   m.b296 + m.b305 + m.b318 + m.b325 >= 1)

m.c1939 = Constraint(expr=   m.b296 + m.b305 + m.b318 + m.b321 >= 1)

m.c1940 = Constraint(expr=   m.b296 + m.b305 + m.b317 + m.b331 >= 1)

m.c1941 = Constraint(expr=   m.b296 + m.b305 + m.b317 + m.b326 >= 1)

m.c1942 = Constraint(expr=   m.b296 + m.b305 + m.b317 + m.b321 >= 1)

m.c1943 = Constraint(expr=   m.b296 + m.b305 + m.b312 + m.b330 >= 1)

m.c1944 = Constraint(expr=   m.b296 + m.b305 + m.b312 + m.b326 + m.b331 >= 1)

m.c1945 = Constraint(expr=   m.b296 + m.b305 + m.b312 + m.b325 >= 1)

m.c1946 = Constraint(expr=   m.b296 + m.b305 + m.b312 + m.b321 >= 1)

m.c1947 = Constraint(expr=   m.b296 + m.b305 + m.b312 + m.b318 + m.b331 >= 1)

m.c1948 = Constraint(expr=   m.b296 + m.b305 + m.b312 + m.b318 + m.b326 >= 1)

m.c1949 = Constraint(expr=   m.b296 + m.b305 + m.b312 + m.b318 + m.b321 >= 1)

m.c1950 = Constraint(expr=   m.b296 + m.b305 + m.b311 + m.b331 >= 1)

m.c1951 = Constraint(expr=   m.b296 + m.b305 + m.b311 + m.b326 >= 1)

m.c1952 = Constraint(expr=   m.b296 + m.b305 + m.b311 + m.b321 >= 1)

m.c1953 = Constraint(expr=   m.b296 + m.b304 + m.b331 >= 1)

m.c1954 = Constraint(expr=   m.b296 + m.b304 + m.b326 >= 1)

m.c1955 = Constraint(expr=   m.b296 + m.b304 + m.b321 >= 1)

m.c1956 = Constraint(expr=   m.b296 + m.b304 + m.b312 + m.b331 >= 1)

m.c1957 = Constraint(expr=   m.b296 + m.b304 + m.b312 + m.b326 >= 1)

m.c1958 = Constraint(expr=   m.b296 + m.b304 + m.b312 + m.b321 >= 1)

m.c1959 = Constraint(expr=   m.b296 + m.b302 + m.b329 >= 1)

m.c1960 = Constraint(expr=   m.b296 + m.b302 + m.b325 + m.b330 >= 1)

m.c1961 = Constraint(expr=   m.b296 + m.b302 + m.b324 >= 1)

m.c1962 = Constraint(expr=   m.b296 + m.b302 + m.b321 + m.b330 >= 1)

m.c1963 = Constraint(expr=   m.b296 + m.b302 + m.b321 + m.b326 + m.b331 >= 1)

m.c1964 = Constraint(expr=   m.b296 + m.b302 + m.b321 + m.b325 >= 1)

m.c1965 = Constraint(expr=   m.b296 + m.b302 + m.b320 >= 1)

m.c1966 = Constraint(expr=   m.b296 + m.b302 + m.b318 + m.b329 >= 1)

m.c1967 = Constraint(expr=   m.b296 + m.b302 + m.b318 + m.b326 + m.b330 >= 1)

m.c1968 = Constraint(expr=   m.b296 + m.b302 + m.b318 + m.b325 + m.b331 >= 1)

m.c1969 = Constraint(expr=   m.b296 + m.b302 + m.b318 + m.b324 >= 1)

m.c1970 = Constraint(expr=   m.b296 + m.b302 + m.b318 + m.b321 + m.b331 >= 1)

m.c1971 = Constraint(expr=   m.b296 + m.b302 + m.b318 + m.b321 + m.b326 >= 1)

m.c1972 = Constraint(expr=   m.b296 + m.b302 + m.b318 + m.b320 >= 1)

m.c1973 = Constraint(expr=   m.b296 + m.b302 + m.b317 + m.b330 >= 1)

m.c1974 = Constraint(expr=   m.b296 + m.b302 + m.b317 + m.b326 + m.b331 >= 1)

m.c1975 = Constraint(expr=   m.b296 + m.b302 + m.b317 + m.b325 >= 1)

m.c1976 = Constraint(expr=   m.b296 + m.b302 + m.b317 + m.b321 >= 1)

m.c1977 = Constraint(expr=   m.b296 + m.b302 + m.b316 + m.b331 >= 1)

m.c1978 = Constraint(expr=   m.b296 + m.b302 + m.b316 + m.b326 >= 1)

m.c1979 = Constraint(expr=   m.b296 + m.b302 + m.b316 + m.b321 >= 1)

m.c1980 = Constraint(expr=   m.b296 + m.b302 + m.b312 + m.b329 >= 1)

m.c1981 = Constraint(expr=   m.b296 + m.b302 + m.b312 + m.b326 + m.b330 >= 1)

m.c1982 = Constraint(expr=   m.b296 + m.b302 + m.b312 + m.b325 + m.b331 >= 1)

m.c1983 = Constraint(expr=   m.b296 + m.b302 + m.b312 + m.b324 >= 1)

m.c1984 = Constraint(expr=   m.b296 + m.b302 + m.b312 + m.b321 + m.b331 >= 1)

m.c1985 = Constraint(expr=   m.b296 + m.b302 + m.b312 + m.b321 + m.b326 >= 1)

m.c1986 = Constraint(expr=   m.b296 + m.b302 + m.b312 + m.b320 >= 1)

m.c1987 = Constraint(expr=   m.b296 + m.b302 + m.b312 + m.b318 + m.b330 >= 1)

m.c1988 = Constraint(expr=   m.b296 + m.b302 + m.b312 + m.b318 + m.b326 + m.b331 >= 1)

m.c1989 = Constraint(expr=   m.b296 + m.b302 + m.b312 + m.b318 + m.b325 >= 1)

m.c1990 = Constraint(expr=   m.b296 + m.b302 + m.b312 + m.b318 + m.b321 >= 1)

m.c1991 = Constraint(expr=   m.b296 + m.b302 + m.b312 + m.b317 + m.b331 >= 1)

m.c1992 = Constraint(expr=   m.b296 + m.b302 + m.b312 + m.b317 + m.b326 >= 1)

m.c1993 = Constraint(expr=   m.b296 + m.b302 + m.b312 + m.b317 + m.b321 >= 1)

m.c1994 = Constraint(expr=   m.b296 + m.b302 + m.b311 + m.b330 >= 1)

m.c1995 = Constraint(expr=   m.b296 + m.b302 + m.b311 + m.b326 + m.b331 >= 1)

m.c1996 = Constraint(expr=   m.b296 + m.b302 + m.b311 + m.b325 >= 1)

m.c1997 = Constraint(expr=   m.b296 + m.b302 + m.b311 + m.b321 >= 1)

m.c1998 = Constraint(expr=   m.b296 + m.b302 + m.b311 + m.b318 + m.b331 >= 1)

m.c1999 = Constraint(expr=   m.b296 + m.b302 + m.b311 + m.b318 + m.b326 >= 1)

m.c2000 = Constraint(expr=   m.b296 + m.b302 + m.b311 + m.b318 + m.b321 >= 1)

m.c2001 = Constraint(expr=   m.b296 + m.b302 + m.b310 + m.b331 >= 1)

m.c2002 = Constraint(expr=   m.b296 + m.b302 + m.b310 + m.b326 >= 1)

m.c2003 = Constraint(expr=   m.b296 + m.b302 + m.b310 + m.b321 >= 1)

m.c2004 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b330 >= 1)

m.c2005 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b326 + m.b331 >= 1)

m.c2006 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b325 >= 1)

m.c2007 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b321 >= 1)

m.c2008 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b318 + m.b331 >= 1)

m.c2009 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b318 + m.b326 >= 1)

m.c2010 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b318 + m.b321 >= 1)

m.c2011 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b317 + m.b331 >= 1)

m.c2012 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b317 + m.b326 >= 1)

m.c2013 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b317 + m.b321 >= 1)

m.c2014 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b312 + m.b331 >= 1)

m.c2015 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b312 + m.b326 >= 1)

m.c2016 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b312 + m.b321 >= 1)

m.c2017 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b312 + m.b318 + m.b331 >= 1)

m.c2018 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b312 + m.b318 + m.b326 >= 1)

m.c2019 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b312 + m.b318 + m.b321 >= 1)

m.c2020 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b311 + m.b331 >= 1)

m.c2021 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b311 + m.b326 >= 1)

m.c2022 = Constraint(expr=   m.b296 + m.b302 + m.b306 + m.b311 + m.b321 >= 1)

m.c2023 = Constraint(expr=   m.b296 + m.b302 + m.b305 + m.b331 >= 1)

m.c2024 = Constraint(expr=   m.b296 + m.b302 + m.b305 + m.b326 >= 1)

m.c2025 = Constraint(expr=   m.b296 + m.b302 + m.b305 + m.b321 >= 1)

m.c2026 = Constraint(expr=   m.b296 + m.b301 + m.b331 >= 1)

m.c2027 = Constraint(expr=   m.b296 + m.b301 + m.b326 >= 1)

m.c2028 = Constraint(expr=   m.b296 + m.b301 + m.b321 >= 1)

m.c2029 = Constraint(expr=   m.b296 + m.b299 + m.b329 >= 1)

m.c2030 = Constraint(expr=   m.b296 + m.b299 + m.b326 + m.b330 >= 1)

m.c2031 = Constraint(expr=   m.b296 + m.b299 + m.b325 + m.b331 >= 1)

m.c2032 = Constraint(expr=   m.b296 + m.b299 + m.b324 >= 1)

m.c2033 = Constraint(expr=   m.b296 + m.b299 + m.b321 + m.b331 >= 1)

m.c2034 = Constraint(expr=   m.b296 + m.b299 + m.b321 + m.b326 >= 1)

m.c2035 = Constraint(expr=   m.b296 + m.b299 + m.b320 >= 1)

m.c2036 = Constraint(expr=   m.b296 + m.b299 + m.b318 + m.b330 >= 1)

m.c2037 = Constraint(expr=   m.b296 + m.b299 + m.b318 + m.b326 + m.b331 >= 1)

m.c2038 = Constraint(expr=   m.b296 + m.b299 + m.b318 + m.b325 >= 1)

m.c2039 = Constraint(expr=   m.b296 + m.b299 + m.b318 + m.b321 >= 1)

m.c2040 = Constraint(expr=   m.b296 + m.b299 + m.b317 + m.b330 >= 1)

m.c2041 = Constraint(expr=   m.b296 + m.b299 + m.b317 + m.b326 + m.b331 >= 1)

m.c2042 = Constraint(expr=   m.b296 + m.b299 + m.b317 + m.b325 >= 1)

m.c2043 = Constraint(expr=   m.b296 + m.b299 + m.b317 + m.b321 >= 1)

m.c2044 = Constraint(expr=   m.b296 + m.b299 + m.b316 + m.b331 >= 1)

m.c2045 = Constraint(expr=   m.b296 + m.b299 + m.b316 + m.b326 >= 1)

m.c2046 = Constraint(expr=   m.b296 + m.b299 + m.b316 + m.b321 >= 1)

m.c2047 = Constraint(expr=   m.b296 + m.b299 + m.b312 + m.b330 >= 1)

m.c2048 = Constraint(expr=   m.b296 + m.b299 + m.b312 + m.b326 + m.b331 >= 1)

m.c2049 = Constraint(expr=   m.b296 + m.b299 + m.b312 + m.b325 >= 1)

m.c2050 = Constraint(expr=   m.b296 + m.b299 + m.b312 + m.b321 >= 1)

m.c2051 = Constraint(expr=   m.b296 + m.b299 + m.b312 + m.b318 + m.b330 >= 1)

m.c2052 = Constraint(expr=   m.b296 + m.b299 + m.b312 + m.b318 + m.b326 + m.b331 >= 1)

m.c2053 = Constraint(expr=   m.b296 + m.b299 + m.b312 + m.b318 + m.b325 >= 1)

m.c2054 = Constraint(expr=   m.b296 + m.b299 + m.b312 + m.b318 + m.b321 >= 1)

m.c2055 = Constraint(expr=   m.b296 + m.b299 + m.b312 + m.b317 + m.b331 >= 1)

m.c2056 = Constraint(expr=   m.b296 + m.b299 + m.b312 + m.b317 + m.b326 >= 1)

m.c2057 = Constraint(expr=   m.b296 + m.b299 + m.b312 + m.b317 + m.b321 >= 1)

m.c2058 = Constraint(expr=   m.b296 + m.b299 + m.b311 + m.b330 >= 1)

m.c2059 = Constraint(expr=   m.b296 + m.b299 + m.b311 + m.b326 + m.b331 >= 1)

m.c2060 = Constraint(expr=   m.b296 + m.b299 + m.b311 + m.b325 >= 1)

m.c2061 = Constraint(expr=   m.b296 + m.b299 + m.b311 + m.b321 >= 1)

m.c2062 = Constraint(expr=   m.b296 + m.b299 + m.b311 + m.b318 + m.b331 >= 1)

m.c2063 = Constraint(expr=   m.b296 + m.b299 + m.b311 + m.b318 + m.b326 >= 1)

m.c2064 = Constraint(expr=   m.b296 + m.b299 + m.b311 + m.b318 + m.b321 >= 1)

m.c2065 = Constraint(expr=   m.b296 + m.b299 + m.b310 + m.b331 >= 1)

m.c2066 = Constraint(expr=   m.b296 + m.b299 + m.b310 + m.b326 >= 1)

m.c2067 = Constraint(expr=   m.b296 + m.b299 + m.b310 + m.b321 >= 1)

m.c2068 = Constraint(expr=   m.b296 + m.b299 + m.b306 + m.b330 >= 1)

m.c2069 = Constraint(expr=   m.b296 + m.b299 + m.b306 + m.b326 + m.b331 >= 1)

m.c2070 = Constraint(expr=   m.b296 + m.b299 + m.b306 + m.b325 >= 1)

m.c2071 = Constraint(expr=   m.b296 + m.b299 + m.b306 + m.b321 >= 1)

m.c2072 = Constraint(expr=   m.b296 + m.b299 + m.b306 + m.b318 + m.b331 >= 1)

m.c2073 = Constraint(expr=   m.b296 + m.b299 + m.b306 + m.b318 + m.b326 >= 1)

m.c2074 = Constraint(expr=   m.b296 + m.b299 + m.b306 + m.b318 + m.b321 >= 1)

m.c2075 = Constraint(expr=   m.b296 + m.b299 + m.b306 + m.b317 + m.b331 >= 1)

m.c2076 = Constraint(expr=   m.b296 + m.b299 + m.b306 + m.b317 + m.b326 >= 1)

m.c2077 = Constraint(expr=   m.b296 + m.b299 + m.b306 + m.b317 + m.b321 >= 1)

m.c2078 = Constraint(expr=   m.b296 + m.b299 + m.b306 + m.b312 + m.b331 >= 1)

m.c2079 = Constraint(expr=   m.b296 + m.b299 + m.b306 + m.b312 + m.b326 >= 1)

m.c2080 = Constraint(expr=   m.b296 + m.b299 + m.b306 + m.b312 + m.b321 >= 1)

m.c2081 = Constraint(expr=   m.b296 + m.b299 + m.b305 + m.b331 >= 1)

m.c2082 = Constraint(expr=   m.b296 + m.b299 + m.b305 + m.b326 >= 1)

m.c2083 = Constraint(expr=   m.b296 + m.b299 + m.b305 + m.b321 >= 1)

m.c2084 = Constraint(expr=   m.b296 + m.b299 + m.b302 + m.b331 >= 1)

m.c2085 = Constraint(expr=   m.b296 + m.b299 + m.b302 + m.b326 >= 1)

m.c2086 = Constraint(expr=   m.b296 + m.b299 + m.b302 + m.b321 >= 1)

m.c2087 = Constraint(expr=   m.b296 + m.b299 + m.b302 + m.b318 + m.b331 >= 1)

m.c2088 = Constraint(expr=   m.b296 + m.b299 + m.b302 + m.b318 + m.b326 >= 1)

m.c2089 = Constraint(expr=   m.b296 + m.b299 + m.b302 + m.b318 + m.b321 >= 1)

m.c2090 = Constraint(expr=   m.b296 + m.b299 + m.b302 + m.b312 + m.b331 >= 1)

m.c2091 = Constraint(expr=   m.b296 + m.b299 + m.b302 + m.b312 + m.b326 >= 1)

m.c2092 = Constraint(expr=   m.b296 + m.b299 + m.b302 + m.b312 + m.b321 >= 1)

m.c2093 = Constraint(expr=   m.b296 + m.b298 + m.b331 >= 1)

m.c2094 = Constraint(expr=   m.b296 + m.b298 + m.b326 >= 1)

m.c2095 = Constraint(expr=   m.b296 + m.b298 + m.b321 >= 1)

m.c2096 = Constraint(expr=   m.b295 + m.b329 >= 1)

m.c2097 = Constraint(expr=   m.b295 + m.b326 + m.b330 >= 1)

m.c2098 = Constraint(expr=   m.b295 + m.b325 + m.b331 >= 1)

m.c2099 = Constraint(expr=   m.b295 + m.b324 >= 1)

m.c2100 = Constraint(expr=   m.b295 + m.b321 + m.b331 >= 1)

m.c2101 = Constraint(expr=   m.b295 + m.b321 + m.b326 >= 1)

m.c2102 = Constraint(expr=   m.b295 + m.b320 >= 1)

m.c2103 = Constraint(expr=   m.b295 + m.b318 + m.b330 >= 1)

m.c2104 = Constraint(expr=   m.b295 + m.b318 + m.b326 + m.b331 >= 1)

m.c2105 = Constraint(expr=   m.b295 + m.b318 + m.b325 >= 1)

m.c2106 = Constraint(expr=   m.b295 + m.b318 + m.b321 >= 1)

m.c2107 = Constraint(expr=   m.b295 + m.b317 + m.b330 >= 1)

m.c2108 = Constraint(expr=   m.b295 + m.b317 + m.b326 + m.b331 >= 1)

m.c2109 = Constraint(expr=   m.b295 + m.b317 + m.b325 >= 1)

m.c2110 = Constraint(expr=   m.b295 + m.b317 + m.b321 >= 1)

m.c2111 = Constraint(expr=   m.b295 + m.b316 + m.b331 >= 1)

m.c2112 = Constraint(expr=   m.b295 + m.b316 + m.b326 >= 1)

m.c2113 = Constraint(expr=   m.b295 + m.b316 + m.b321 >= 1)

m.c2114 = Constraint(expr=   m.b295 + m.b312 + m.b330 >= 1)

m.c2115 = Constraint(expr=   m.b295 + m.b312 + m.b325 >= 1)

m.c2116 = Constraint(expr=   m.b295 + m.b312 + m.b321 >= 1)

m.c2117 = Constraint(expr=   m.b295 + m.b312 + m.b318 + m.b330 >= 1)

m.c2118 = Constraint(expr=   m.b295 + m.b312 + m.b318 + m.b326 + m.b331 >= 1)

m.c2119 = Constraint(expr=   m.b295 + m.b312 + m.b318 + m.b325 >= 1)

m.c2120 = Constraint(expr=   m.b295 + m.b312 + m.b318 + m.b321 >= 1)

m.c2121 = Constraint(expr=   m.b295 + m.b312 + m.b317 + m.b331 >= 1)

m.c2122 = Constraint(expr=   m.b295 + m.b312 + m.b317 + m.b326 >= 1)

m.c2123 = Constraint(expr=   m.b295 + m.b312 + m.b317 + m.b321 >= 1)

m.c2124 = Constraint(expr=   m.b295 + m.b311 + m.b330 >= 1)

m.c2125 = Constraint(expr=   m.b295 + m.b311 + m.b326 + m.b331 >= 1)

m.c2126 = Constraint(expr=   m.b295 + m.b311 + m.b325 >= 1)

m.c2127 = Constraint(expr=   m.b295 + m.b311 + m.b321 >= 1)

m.c2128 = Constraint(expr=   m.b295 + m.b311 + m.b318 + m.b331 >= 1)

m.c2129 = Constraint(expr=   m.b295 + m.b311 + m.b318 + m.b326 >= 1)

m.c2130 = Constraint(expr=   m.b295 + m.b311 + m.b318 + m.b321 >= 1)

m.c2131 = Constraint(expr=   m.b295 + m.b310 + m.b331 >= 1)

m.c2132 = Constraint(expr=   m.b295 + m.b310 + m.b326 >= 1)

m.c2133 = Constraint(expr=   m.b295 + m.b310 + m.b321 >= 1)

m.c2134 = Constraint(expr=   m.b295 + m.b306 + m.b330 >= 1)

m.c2135 = Constraint(expr=   m.b295 + m.b306 + m.b326 + m.b331 >= 1)

m.c2136 = Constraint(expr=   m.b295 + m.b306 + m.b325 >= 1)

m.c2137 = Constraint(expr=   m.b295 + m.b306 + m.b321 >= 1)

m.c2138 = Constraint(expr=   m.b295 + m.b306 + m.b318 + m.b331 >= 1)

m.c2139 = Constraint(expr=   m.b295 + m.b306 + m.b318 + m.b326 >= 1)

m.c2140 = Constraint(expr=   m.b295 + m.b306 + m.b318 + m.b321 >= 1)

m.c2141 = Constraint(expr=   m.b295 + m.b306 + m.b312 + m.b331 >= 1)

m.c2142 = Constraint(expr=   m.b295 + m.b306 + m.b312 + m.b326 >= 1)

m.c2143 = Constraint(expr=   m.b295 + m.b306 + m.b312 + m.b321 >= 1)

m.c2144 = Constraint(expr=   m.b295 + m.b305 + m.b331 >= 1)

m.c2145 = Constraint(expr=   m.b295 + m.b305 + m.b326 >= 1)

m.c2146 = Constraint(expr=   m.b295 + m.b305 + m.b321 >= 1)

m.c2147 = Constraint(expr=   m.b295 + m.b302 + m.b331 >= 1)

m.c2148 = Constraint(expr=   m.b295 + m.b302 + m.b326 >= 1)

m.c2149 = Constraint(expr=   m.b295 + m.b302 + m.b321 >= 1)

m.c2150 = Constraint(expr=   m.b295 + m.b299 + m.b331 >= 1)

m.c2151 = Constraint(expr=   m.b295 + m.b299 + m.b326 >= 1)

m.c2152 = Constraint(expr=   m.b295 + m.b299 + m.b321 >= 1)

m.c2153 = Constraint(expr=   m.b294 + m.b331 >= 1)

m.c2154 = Constraint(expr=   m.b294 + m.b326 >= 1)

m.c2155 = Constraint(expr=   m.b294 + m.b321 >= 1)

m.c2156 = Constraint(expr=   m.b294 - m.b295 >= 0)

m.c2157 = Constraint(expr=   m.b295 - m.b296 >= 0)

m.c2158 = Constraint(expr=   m.b297 - m.b298 >= 0)

m.c2159 = Constraint(expr=   m.b298 - m.b299 >= 0)

m.c2160 = Constraint(expr=   m.b300 - m.b301 >= 0)

m.c2161 = Constraint(expr=   m.b301 - m.b302 >= 0)

m.c2162 = Constraint(expr=   m.b303 - m.b304 >= 0)

m.c2163 = Constraint(expr=   m.b304 - m.b305 >= 0)

m.c2164 = Constraint(expr=   m.b305 - m.b306 >= 0)

m.c2165 = Constraint(expr=   m.b307 - m.b308 >= 0)

m.c2166 = Constraint(expr=   m.b308 - m.b309 >= 0)

m.c2167 = Constraint(expr=   m.b309 - m.b310 >= 0)

m.c2168 = Constraint(expr=   m.b310 - m.b311 >= 0)

m.c2169 = Constraint(expr=   m.b311 - m.b312 >= 0)

m.c2170 = Constraint(expr=   m.b313 - m.b314 >= 0)

m.c2171 = Constraint(expr=   m.b314 - m.b315 >= 0)

m.c2172 = Constraint(expr=   m.b315 - m.b316 >= 0)

m.c2173 = Constraint(expr=   m.b316 - m.b317 >= 0)

m.c2174 = Constraint(expr=   m.b317 - m.b318 >= 0)

m.c2175 = Constraint(expr=   m.b319 - m.b320 >= 0)

m.c2176 = Constraint(expr=   m.b320 - m.b321 >= 0)

m.c2177 = Constraint(expr=   m.b322 - m.b323 >= 0)

m.c2178 = Constraint(expr=   m.b323 - m.b324 >= 0)

m.c2179 = Constraint(expr=   m.b324 - m.b325 >= 0)

m.c2180 = Constraint(expr=   m.b325 - m.b326 >= 0)

m.c2181 = Constraint(expr=   m.b327 - m.b328 >= 0)

m.c2182 = Constraint(expr=   m.b328 - m.b329 >= 0)

m.c2183 = Constraint(expr=   m.b329 - m.b330 >= 0)

m.c2184 = Constraint(expr=   m.b330 - m.b331 >= 0)

m.c2185 = Constraint(expr=   m.b332 - m.b333 >= 0)

m.c2186 = Constraint(expr=   m.b333 - m.b334 >= 0)

m.c2187 = Constraint(expr=   m.b334 - m.b335 >= 0)

m.c2188 = Constraint(expr=   m.b335 - m.b336 >= 0)

m.c2189 = Constraint(expr=   m.b336 - m.b337 >= 0)

m.c2190 = Constraint(expr=   m.b338 - m.b339 >= 0)

m.c2191 = Constraint(expr=   m.b339 - m.b340 >= 0)

m.c2192 = Constraint(expr=   m.b340 - m.b341 >= 0)

m.c2193 = Constraint(expr=   m.b341 - m.b342 >= 0)

m.c2194 = Constraint(expr=   m.b343 - m.b344 >= 0)

m.c2195 = Constraint(expr=   m.b344 - m.b345 >= 0)

m.c2196 = Constraint(expr=   m.b346 - m.b347 >= 0)

m.c2197 = Constraint(expr=   m.b347 - m.b348 >= 0)

m.c2198 = Constraint(expr=   m.b349 - m.b350 >= 0)

m.c2199 = Constraint(expr=   m.b350 - m.b351 >= 0)

m.c2200 = Constraint(expr=   m.b352 - m.b353 >= 0)

m.c2201 = Constraint(expr=   m.b353 - m.b354 >= 0)

m.c2202 = Constraint(expr=   m.b354 - m.b355 >= 0)

m.c2203 = Constraint(expr=   m.x155 - m.x156 >= 0)

m.c2204 = Constraint(expr=   m.x156 - m.x157 >= 0)

m.c2205 = Constraint(expr=   m.x157 - m.x158 >= 0)

m.c2206 = Constraint(expr=   m.x121 - 0.1*m.b294 - 0.573333333333333*m.b295 - 0.1*m.b296 == 1.24666666666667)

m.c2207 = Constraint(expr=   m.x122 - 0.193333333333333*m.b297 - 1.14666666666667*m.b298 - 0.193333333333333*m.b299
                           == 2.48)

m.c2208 = Constraint(expr=   m.x123 - 0.226666666666667*m.b300 - 1.36*m.b301 - 0.226666666666667*m.b302
                           == 2.94666666666667)

m.c2209 = Constraint(expr=   m.x124 - 0.28*m.b303 - 1.42*m.b304 - 0.286666666666667*m.b305 - 0.28*m.b306
                           == 3.69333333333333)

m.c2210 = Constraint(expr=   m.x125 - 1.91333333333333*m.b307 - 7.65333333333333*m.b308 - 1.91333333333333*m.b309
                           - 1.91333333333333*m.b310 - 1.91333333333333*m.b311 - 1.91333333333333*m.b312
                           == 24.8733333333333)

m.c2211 = Constraint(expr=   m.x126 - 4.51333333333333*m.b313 - 18.0533333333333*m.b314 - 4.51333333333333*m.b315
                           - 4.50666666666667*m.b316 - 4.51333333333333*m.b317 - 4.51333333333333*m.b318
                           == 58.6666666666667)

m.c2212 = Constraint(expr=   m.x127 - 0.313333333333333*m.b319 - 1.88666666666667*m.b320 - 0.313333333333333*m.b321
                           == 4.08)

m.c2213 = Constraint(expr=   m.x128 - 2.81333333333333*m.b322 - 14.06*m.b323 - 2.80666666666667*m.b324
                           - 2.81333333333333*m.b325 - 2.81333333333333*m.b326 == 36.56)

m.c2214 = Constraint(expr=   m.x129 - 2.56*m.b327 - 12.7933333333333*m.b328 - 2.56*m.b329 - 2.56*m.b330
                           - 2.55333333333333*m.b331 == 33.26)

m.c2215 = Constraint(expr=   m.x130 - 1.88666666666667*m.b332 - 7.54666666666667*m.b333 - 1.88666666666667*m.b334
                           - 1.88666666666667*m.b335 - 1.88666666666667*m.b336 - 1.88666666666667*m.b337 == 24.52)

m.c2216 = Constraint(expr=   m.x131 - 2.84*m.b338 - 14.2*m.b339 - 2.84*m.b340 - 2.84*m.b341 - 2.84666666666667*m.b342
                           == 36.9266666666667)

m.c2217 = Constraint(expr=   m.x132 - 3.85333333333333*m.b343 - 23.1133333333333*m.b344 - 3.85333333333333*m.b345
                           == 50.0866666666667)

m.c2218 = Constraint(expr=   m.x133 - 1.24666666666667*m.b346 - 7.47333333333333*m.b347 - 1.24*m.b348
                           == 16.1866666666667)

m.c2219 = Constraint(expr=   m.x134 - 1.81333333333333*m.b349 - 10.8533333333333*m.b350 - 1.81333333333333*m.b351
                           == 23.52)

m.c2220 = Constraint(expr=   m.x135 - 2.96666666666667*m.b352 - 14.82*m.b353 - 2.96*m.b354 - 2.96666666666667*m.b355
                           == 38.5266666666667)

m.c2221 = Constraint(expr= - m.x136 + m.x279 <= 0)

m.c2222 = Constraint(expr= - m.x137 + m.x280 <= 0)

m.c2223 = Constraint(expr= - m.x138 + m.x281 <= 0)

m.c2224 = Constraint(expr= - m.x139 + m.x282 <= 0)

m.c2225 = Constraint(expr= - m.x140 + m.x283 <= 0)

m.c2226 = Constraint(expr= - m.x141 + m.x284 <= 0)

m.c2227 = Constraint(expr= - m.x142 + m.x285 <= 0)

m.c2228 = Constraint(expr= - m.x143 + m.x286 <= 0)

m.c2229 = Constraint(expr= - m.x144 + m.x287 <= 0)

m.c2230 = Constraint(expr= - m.x145 + m.x288 <= 0)

m.c2231 = Constraint(expr= - m.x146 + m.x289 <= 0)

m.c2232 = Constraint(expr= - m.x147 + m.x290 <= 0)

m.c2233 = Constraint(expr= - m.x148 + m.x291 <= 0)

m.c2234 = Constraint(expr= - m.x149 + m.x292 <= 0)

m.c2235 = Constraint(expr= - m.x150 + m.x293 <= 0)
