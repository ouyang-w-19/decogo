#  MINLP written by GAMS Convert at 04/21/18 13:53:10
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        525      151       96      278        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        332      287       45        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1914     1360      554        0
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
m.x11 = Var(within=Reals,bounds=(0,275),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,275),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,275),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,525),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,525),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,400),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,375),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,375),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,375),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x32 = Var(within=Reals,bounds=(100,700),initialize=100)
m.x33 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x34 = Var(within=Reals,bounds=(50,400),initialize=50)
m.x35 = Var(within=Reals,bounds=(0,3.7),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,130),initialize=0)
m.x37 = Var(within=Reals,bounds=(6.4,10),initialize=6.4)
m.x38 = Var(within=Reals,bounds=(30,70),initialize=30)
m.x39 = Var(within=Reals,bounds=(70,100),initialize=70)
m.x40 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,3.7),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,3.7),initialize=0)
m.x45 = Var(within=Reals,bounds=(2,3.7),initialize=2)
m.x46 = Var(within=Reals,bounds=(0,3.7),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x48 = Var(within=Reals,bounds=(6.4,10),initialize=6.4)
m.x49 = Var(within=Reals,bounds=(30,70),initialize=30)
m.x50 = Var(within=Reals,bounds=(70,100),initialize=70)
m.x51 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,3.7),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,3.7),initialize=0)
m.x56 = Var(within=Reals,bounds=(1,3.7),initialize=1)
m.x57 = Var(within=Reals,bounds=(0,3.7),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x59 = Var(within=Reals,bounds=(6.4,10),initialize=6.4)
m.x60 = Var(within=Reals,bounds=(30,70),initialize=30)
m.x61 = Var(within=Reals,bounds=(70,100),initialize=70)
m.x62 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,3.7),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,3.7),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,3.7),initialize=0)
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
m.x114 = Var(within=Reals,bounds=(0,0.1243908),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,0.14364),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,0.1719096),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,0.16128),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,0.2058516),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,0.17388),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,0.1243908),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,0.14364),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,0.1719096),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,0.16128),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,0.2058516),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,0.17388),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,0.1243908),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,0.14364),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,0.1719096),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,0.16128),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,0.2058516),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,0.17388),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,0.1243908),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,0.14364),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,0.1719096),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,0.16128),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,0.2058516),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,0.17388),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,0.1243908),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,0.14364),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,0.1719096),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,0.16128),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,0.2058516),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,0.17388),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,0.1243908),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,0.14364),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,0.1719096),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,0.16128),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,0.2058516),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,0.17388),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,0.20396),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,0.21094),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,0.20396),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,0.21094),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,0.20396),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,0.21094),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,0.20396),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,0.21094),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,0.20396),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,0.21094),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,0.20396),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,0.21094),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,0.20396),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,0.21094),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,0.20396),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,0.21094),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,0.20396),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,0.21094),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,0.20396),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,0.21094),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,0.20396),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,0.21094),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,0.20396),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,0.21094),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,0.20396),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,0.21094),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,0.20396),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,0.21094),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,0.20396),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,0.21094),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,0.20396),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,0.21094),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,0.20396),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,0.21094),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,0.20396),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,0.21094),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,0.278825),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,0.279175),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,0.278825),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,0.279175),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,0.278825),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,0.279175),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,0.278825),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,0.279175),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,0.278825),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,0.279175),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,0.278825),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,0.279175),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,0.278825),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,0.279175),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,0.278825),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,0.279175),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,0.278825),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,0.279175),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,0.278825),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,0.279175),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,0.278825),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,0.279175),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,0.278825),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,0.279175),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,0.295792),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,0.26032),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,0.295792),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,0.26032),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,0.295792),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,0.26032),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,0.295792),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,0.26032),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,0.295792),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,0.26032),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,0.295792),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,0.26032),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,0.295792),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,0.26032),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,0.295792),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,0.26032),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,0.295792),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,0.26032),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,0.295792),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,0.26032),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,0.295792),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,0.26032),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,0.295792),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,0.26032),initialize=0)
m.x234 = Var(within=Reals,bounds=(-0.04293,0.0814608),initialize=0)
m.x235 = Var(within=Reals,bounds=(-0.1134,0.03024),initialize=0)
m.x236 = Var(within=Reals,bounds=(-0.04293,0.1289796),initialize=0)
m.x237 = Var(within=Reals,bounds=(-0.1134,0.04788),initialize=0)
m.x238 = Var(within=Reals,bounds=(-0.04293,0.1629216),initialize=0)
m.x239 = Var(within=Reals,bounds=(-0.1134,0.06048),initialize=0)
m.x240 = Var(within=Reals,bounds=(-0.0734256,0.1305344),initialize=0)
m.x241 = Var(within=Reals,bounds=(-0.0759384,0.1350016),initialize=0)
m.x242 = Var(within=Reals,bounds=(-0.0734256,0.1305344),initialize=0)
m.x243 = Var(within=Reals,bounds=(-0.0759384,0.1350016),initialize=0)
m.x244 = Var(within=Reals,bounds=(-0.0734256,0.1305344),initialize=0)
m.x245 = Var(within=Reals,bounds=(-0.0759384,0.1350016),initialize=0)
m.x246 = Var(within=Reals,bounds=(-0.211907,0.066918),initialize=0)
m.x247 = Var(within=Reals,bounds=(-0.212173,0.067002),initialize=0)
m.x248 = Var(within=Reals,bounds=(-0.211907,0.066918),initialize=0)
m.x249 = Var(within=Reals,bounds=(-0.212173,0.067002),initialize=0)
m.x250 = Var(within=Reals,bounds=(-0.211907,0.066918),initialize=0)
m.x251 = Var(within=Reals,bounds=(-0.212173,0.067002),initialize=0)
m.x252 = Var(within=Reals,bounds=(-0.2736076,0.0221844),initialize=0)
m.x253 = Var(within=Reals,bounds=(-0.240796,0.019524),initialize=0)
m.x254 = Var(within=Reals,bounds=(-0.2736076,0.0221844),initialize=0)
m.x255 = Var(within=Reals,bounds=(-0.240796,0.019524),initialize=0)
m.x256 = Var(within=Reals,bounds=(-0.2736076,0.0221844),initialize=0)
m.x257 = Var(within=Reals,bounds=(-0.240796,0.019524),initialize=0)
m.x258 = Var(within=Reals,bounds=(6.4,10),initialize=6.4)
m.x259 = Var(within=Reals,bounds=(6.4,10),initialize=6.4)
m.x260 = Var(within=Reals,bounds=(6.4,10),initialize=6.4)
m.x261 = Var(within=Reals,bounds=(33,65.52),initialize=33)
m.x262 = Var(within=Reals,bounds=(33,65.52),initialize=33)
m.x263 = Var(within=Reals,bounds=(33,65.52),initialize=33)
m.x264 = Var(within=Reals,bounds=(18,46),initialize=18)
m.x265 = Var(within=Reals,bounds=(18,46),initialize=18)
m.x266 = Var(within=Reals,bounds=(18,46),initialize=18)
m.x267 = Var(within=Reals,bounds=(83.6,99),initialize=83.6)
m.x268 = Var(within=Reals,bounds=(83.6,99),initialize=83.6)
m.x269 = Var(within=Reals,bounds=(83.6,99),initialize=83.6)
m.x270 = Var(within=Reals,bounds=(72,94),initialize=72)
m.x271 = Var(within=Reals,bounds=(72,94),initialize=72)
m.x272 = Var(within=Reals,bounds=(72,94),initialize=72)
m.x273 = Var(within=Reals,bounds=(10,130),initialize=10)
m.x274 = Var(within=Reals,bounds=(10,200),initialize=10)
m.x275 = Var(within=Reals,bounds=(10,250),initialize=10)
m.x276 = Var(within=Reals,bounds=(70,95),initialize=70)
m.x277 = Var(within=Reals,bounds=(70,95),initialize=70)
m.x278 = Var(within=Reals,bounds=(70,95),initialize=70)
m.x279 = Var(within=Reals,bounds=(18,36.8),initialize=18)
m.x280 = Var(within=Reals,bounds=(18,36.8),initialize=18)
m.x281 = Var(within=Reals,bounds=(18,36.8),initialize=18)
m.x282 = Var(within=Reals,bounds=(3.77,19),initialize=3.77)
m.x283 = Var(within=Reals,bounds=(3.77,19),initialize=3.77)
m.x284 = Var(within=Reals,bounds=(3.77,19),initialize=3.77)
m.x285 = Var(within=Reals,bounds=(10,50),initialize=10)
m.x286 = Var(within=Reals,bounds=(10,50),initialize=10)
m.x287 = Var(within=Reals,bounds=(10,50),initialize=10)
m.x288 = Var(within=Reals,bounds=(70,95),initialize=70)
m.x289 = Var(within=Reals,bounds=(70,95),initialize=70)
m.x290 = Var(within=Reals,bounds=(70,95),initialize=70)
m.x291 = Var(within=Reals,bounds=(-8,4),initialize=0)
m.x292 = Var(within=Reals,bounds=(-8,4),initialize=0)
m.x293 = Var(within=Reals,bounds=(-8,4),initialize=0)
m.x294 = Var(within=Reals,bounds=(-2,1),initialize=0)
m.x295 = Var(within=Reals,bounds=(-2,1),initialize=0)
m.x296 = Var(within=Reals,bounds=(-2,1),initialize=0)
m.x297 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x298 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x299 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x300 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x301 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x302 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x303 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x304 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x305 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x306 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x307 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x308 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x309 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x310 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x311 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x312 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x313 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x314 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x315 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x316 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x317 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x318 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x319 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x320 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x321 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x322 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x323 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x324 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x325 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x326 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x327 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x328 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x329 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x330 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x331 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x332 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=3*m.x1*m.x11 + 3*m.x1*m.x12 + 3*m.x1*m.x13 + 2*m.x2*m.x11 + 2*m.x2*m.x12 + 2*m.x2*m.x13 + 3.5*
                       m.x3*m.x17 + 3.5*m.x3*m.x18 + 3.5*m.x3*m.x19 + 2*m.x4*m.x14 + 2*m.x4*m.x15 + 2*m.x4*m.x16 + m.x5*
                       m.x14 + m.x5*m.x15 + m.x5*m.x16 + 3*m.x6*m.x11 + 3*m.x6*m.x12 + 3*m.x6*m.x13 + 0.7*m.x7*m.x14 + 
                       0.7*m.x7*m.x15 + 0.7*m.x7*m.x16 + 0.5*m.x8*m.x14 + 0.5*m.x8*m.x15 + 0.5*m.x8*m.x16 + 0.3*m.x9*
                       m.x17 + 0.3*m.x9*m.x18 + 0.3*m.x9*m.x19 + 2.5*m.x10*m.x17 + 2.5*m.x10*m.x18 + 2.5*m.x10*m.x19 - 
                       6.3*m.x11 - 5.5*m.x12 - 5*m.x13 - 6.3*m.x14 - 5.5*m.x15 - 5*m.x16 - 6.3*m.x17 - 5.5*m.x18 - 5*
                       m.x19 + 1.2*m.x20 + 2*m.x21 + 2.5*m.x22 + 4.2*m.x23 + 5*m.x24 + 5.5*m.x25 + 2.2*m.x26 + 3*m.x27
                        + 3.5*m.x28 - 0.8*m.x29 + 0.5*m.x31, sense=minimize)

m.c2 = Constraint(expr=m.x1*m.x11 + m.x1*m.x12 + m.x1*m.x13 <= 75)

m.c3 = Constraint(expr=m.x2*m.x11 + m.x2*m.x12 + m.x2*m.x13 <= 50)

m.c4 = Constraint(expr=m.x3*m.x17 + m.x3*m.x18 + m.x3*m.x19 <= 75)

m.c5 = Constraint(expr=m.x4*m.x14 + m.x4*m.x15 + m.x4*m.x16 <= 75)

m.c6 = Constraint(expr=m.x5*m.x14 + m.x5*m.x15 + m.x5*m.x16 <= 300)

m.c7 = Constraint(expr=m.x6*m.x11 + m.x6*m.x12 + m.x6*m.x13 <= 150)

m.c8 = Constraint(expr=m.x7*m.x14 + m.x7*m.x15 + m.x7*m.x16 <= 50)

m.c9 = Constraint(expr=m.x8*m.x14 + m.x8*m.x15 + m.x8*m.x16 <= 100)

m.c10 = Constraint(expr=m.x9*m.x17 + m.x9*m.x18 + m.x9*m.x19 <= 200)

m.c11 = Constraint(expr=m.x10*m.x17 + m.x10*m.x18 + m.x10*m.x19 <= 100)

m.c12 = Constraint(expr=   m.x20 + m.x21 + m.x22 <= 5)

m.c13 = Constraint(expr=   m.x23 + m.x24 + m.x25 <= 10)

m.c14 = Constraint(expr=   m.x26 + m.x27 + m.x28 <= 10)

m.c15 = Constraint(expr=   m.x29 + m.x30 + m.x31 <= 100)

m.c16 = Constraint(expr=-(m.x8*m.x14 + m.x8*m.x15 + m.x8*m.x16) <= -10)

m.c17 = Constraint(expr=-(m.x9*m.x17 + m.x9*m.x18 + m.x9*m.x19) <= -20)

m.c18 = Constraint(expr=-(m.x10*m.x17 + m.x10*m.x18 + m.x10*m.x19) <= -10)

m.c19 = Constraint(expr=   m.x11 + m.x12 + m.x13 <= 400)

m.c20 = Constraint(expr=   m.x14 + m.x15 + m.x16 <= 575)

m.c21 = Constraint(expr=   m.x17 + m.x18 + m.x19 <= 500)

m.c22 = Constraint(expr=   m.x1 + m.x2 + m.x6 == 1)

m.c23 = Constraint(expr=   m.x4 + m.x5 + m.x7 + m.x8 == 1)

m.c24 = Constraint(expr=   m.x3 + m.x9 + m.x10 == 1)

m.c25 = Constraint(expr=m.x1*m.x11 + m.x2*m.x11 + m.x6*m.x11 - m.x11 == 0)

m.c26 = Constraint(expr=m.x1*m.x12 + m.x2*m.x12 + m.x6*m.x12 - m.x12 == 0)

m.c27 = Constraint(expr=m.x1*m.x13 + m.x2*m.x13 + m.x6*m.x13 - m.x13 == 0)

m.c28 = Constraint(expr=m.x4*m.x14 + m.x5*m.x14 + m.x7*m.x14 + m.x8*m.x14 - m.x14 == 0)

m.c29 = Constraint(expr=m.x4*m.x15 + m.x5*m.x15 + m.x7*m.x15 + m.x8*m.x15 - m.x15 == 0)

m.c30 = Constraint(expr=m.x4*m.x16 + m.x5*m.x16 + m.x7*m.x16 + m.x8*m.x16 - m.x16 == 0)

m.c31 = Constraint(expr=m.x3*m.x17 + m.x9*m.x17 + m.x10*m.x17 - m.x17 == 0)

m.c32 = Constraint(expr=m.x3*m.x18 + m.x9*m.x18 + m.x10*m.x18 - m.x18 == 0)

m.c33 = Constraint(expr=m.x3*m.x19 + m.x9*m.x19 + m.x10*m.x19 - m.x19 == 0)

m.c34 = Constraint(expr= - m.x11 - m.x14 - m.x17 - m.x20 - m.x23 - m.x26 - m.x29 + m.x32 == 0)

m.c35 = Constraint(expr= - m.x12 - m.x15 - m.x18 - m.x21 - m.x24 - m.x27 - m.x30 + m.x33 == 0)

m.c36 = Constraint(expr= - m.x13 - m.x16 - m.x19 - m.x22 - m.x25 - m.x28 - m.x31 + m.x34 == 0)

m.c37 = Constraint(expr=m.x35*m.x32 - 18.15*m.x20 - 15.66*m.x23 - 15.66*m.x26 - 34.73*m.x29 == 0)

m.c38 = Constraint(expr=m.x36*m.x32 - (50*m.x4*m.x14 + 100*m.x5*m.x14 + 15*m.x6*m.x11 + 200*m.x7*m.x14 + 400*m.x8*m.x14
                         + 700*m.x9*m.x17 + 10*m.x10*m.x17) == 0)

m.c39 = Constraint(expr=m.x38*m.x32 - (100*m.x1*m.x11 + 100*m.x2*m.x11 + 50*m.x3*m.x17 + 100*m.x4*m.x14 + 70*m.x5*m.x14
                         + 60*m.x6*m.x11 + 85*m.x7*m.x14 + 45*m.x8*m.x14 + 15*m.x9*m.x17 + 30*m.x10*m.x17) - 100*m.x20
                         - 95*m.x23 - 70*m.x26 - 100*m.x29 == 0)

m.c40 = Constraint(expr=m.x39*m.x32 - (100*m.x1*m.x11 + 100*m.x2*m.x11 + 95*m.x3*m.x17 + 100*m.x4*m.x14 + 100*m.x5*m.x14
                         + 85*m.x6*m.x11 + 100*m.x7*m.x14 + 80*m.x8*m.x14 + 60*m.x9*m.x17 + 70*m.x10*m.x17) - 100*m.x20
                         - 100*m.x23 - 100*m.x26 - 100*m.x29 == 0)

m.c41 = Constraint(expr=m.x40*m.x32 - (7.5*m.x5*m.x14 + 3.2*m.x6*m.x11 + 10*m.x7*m.x14 + 35*m.x8*m.x14 + 65*m.x9*m.x17
                         + 60*m.x10*m.x17) == 0)

m.c42 = Constraint(expr=m.x41*m.x32 - (2*m.x5*m.x14 + m.x7*m.x14 + 3*m.x8*m.x14 + 4*m.x9*m.x17 + 5*m.x10*m.x17) == 0)

m.c43 = Constraint(expr=m.x42*m.x32 - (37*m.x5*m.x14 + 12*m.x6*m.x11 + 60*m.x7*m.x14 + 20*m.x8*m.x14 + 15*m.x9*m.x17 + 3
                        *m.x10*m.x17) == 0)

m.c44 = Constraint(expr=m.x43*m.x32 - 18.15*m.x20 == 0)

m.c45 = Constraint(expr=m.x44*m.x32 - 15.66*m.x23 == 0)

m.c46 = Constraint(expr=m.x45*m.x32 - 34.73*m.x29 == 0)

m.c47 = Constraint(expr=m.x46*m.x33 - 18.15*m.x21 - 15.66*m.x24 - 15.66*m.x27 - 34.73*m.x30 == 0)

m.c48 = Constraint(expr=m.x47*m.x33 - (50*m.x4*m.x15 + 100*m.x5*m.x15 + 15*m.x6*m.x12 + 200*m.x7*m.x15 + 400*m.x8*m.x15
                         + 700*m.x9*m.x18 + 10*m.x10*m.x18) == 0)

m.c49 = Constraint(expr=m.x49*m.x33 - (100*m.x1*m.x12 + 100*m.x2*m.x12 + 50*m.x3*m.x18 + 100*m.x4*m.x15 + 70*m.x5*m.x15
                         + 60*m.x6*m.x12 + 85*m.x7*m.x15 + 45*m.x8*m.x15 + 15*m.x9*m.x18 + 30*m.x10*m.x18) - 100*m.x21
                         - 95*m.x24 - 70*m.x27 - 100*m.x30 == 0)

m.c50 = Constraint(expr=m.x50*m.x33 - (100*m.x1*m.x12 + 100*m.x2*m.x12 + 95*m.x3*m.x18 + 100*m.x4*m.x15 + 100*m.x5*m.x15
                         + 85*m.x6*m.x12 + 100*m.x7*m.x15 + 80*m.x8*m.x15 + 60*m.x9*m.x18 + 70*m.x10*m.x18) - 100*m.x21
                         - 100*m.x24 - 100*m.x27 - 100*m.x30 == 0)

m.c51 = Constraint(expr=m.x51*m.x33 - (7.5*m.x5*m.x15 + 3.2*m.x6*m.x12 + 10*m.x7*m.x15 + 35*m.x8*m.x15 + 65*m.x9*m.x18
                         + 60*m.x10*m.x18) == 0)

m.c52 = Constraint(expr=m.x52*m.x33 - (2*m.x5*m.x15 + m.x7*m.x15 + 3*m.x8*m.x15 + 4*m.x9*m.x18 + 5*m.x10*m.x18) == 0)

m.c53 = Constraint(expr=m.x53*m.x33 - (37*m.x5*m.x15 + 12*m.x6*m.x12 + 60*m.x7*m.x15 + 20*m.x8*m.x15 + 15*m.x9*m.x18 + 3
                        *m.x10*m.x18) == 0)

m.c54 = Constraint(expr=m.x54*m.x33 - 18.15*m.x21 == 0)

m.c55 = Constraint(expr=m.x55*m.x33 - 15.66*m.x24 == 0)

m.c56 = Constraint(expr=m.x56*m.x33 - 34.73*m.x30 == 0)

m.c57 = Constraint(expr=m.x57*m.x34 - 18.15*m.x22 - 15.66*m.x25 - 15.66*m.x28 - 34.73*m.x31 == 0)

m.c58 = Constraint(expr=m.x58*m.x34 - (50*m.x4*m.x16 + 100*m.x5*m.x16 + 15*m.x6*m.x13 + 200*m.x7*m.x16 + 400*m.x8*m.x16
                         + 700*m.x9*m.x19 + 10*m.x10*m.x19) == 0)

m.c59 = Constraint(expr=m.x60*m.x34 - (100*m.x1*m.x13 + 100*m.x2*m.x13 + 50*m.x3*m.x19 + 100*m.x4*m.x16 + 70*m.x5*m.x16
                         + 60*m.x6*m.x13 + 85*m.x7*m.x16 + 45*m.x8*m.x16 + 15*m.x9*m.x19 + 30*m.x10*m.x19) - 100*m.x22
                         - 95*m.x25 - 70*m.x28 - 100*m.x31 == 0)

m.c60 = Constraint(expr=m.x61*m.x34 - (100*m.x1*m.x13 + 100*m.x2*m.x13 + 95*m.x3*m.x19 + 100*m.x4*m.x16 + 100*m.x5*m.x16
                         + 85*m.x6*m.x13 + 100*m.x7*m.x16 + 80*m.x8*m.x16 + 60*m.x9*m.x19 + 70*m.x10*m.x19) - 100*m.x22
                         - 100*m.x25 - 100*m.x28 - 100*m.x31 == 0)

m.c61 = Constraint(expr=m.x62*m.x34 - (7.5*m.x5*m.x16 + 3.2*m.x6*m.x13 + 10*m.x7*m.x16 + 35*m.x8*m.x16 + 65*m.x9*m.x19
                         + 60*m.x10*m.x19) == 0)

m.c62 = Constraint(expr=m.x63*m.x34 - (2*m.x5*m.x16 + m.x7*m.x16 + 3*m.x8*m.x16 + 4*m.x9*m.x19 + 5*m.x10*m.x19) == 0)

m.c63 = Constraint(expr=m.x64*m.x34 - (37*m.x5*m.x16 + 12*m.x6*m.x13 + 60*m.x7*m.x16 + 20*m.x8*m.x16 + 15*m.x9*m.x19 + 3
                        *m.x10*m.x19) == 0)

m.c64 = Constraint(expr=m.x65*m.x34 - 18.15*m.x22 == 0)

m.c65 = Constraint(expr=m.x66*m.x34 - 15.66*m.x25 == 0)

m.c66 = Constraint(expr=m.x67*m.x34 - 34.73*m.x31 == 0)

m.c67 = Constraint(expr=m.x37**1.25*m.x32 - (166.989461022824*m.x1*m.x11 + 44.9545980014895*m.x2*m.x11 + 
                        12.2050524378911*m.x3*m.x17 + 17.7827941003892*m.x4*m.x14 + 15.5884572681199*m.x5*m.x14 + 
                        4.61688063363795*m.x6*m.x11 + 18.2284698685036*m.x7*m.x14 + 13.8760966290575*m.x8*m.x14 + 
                        2.5279828213557*m.x9*m.x17 + 12.2050524378911*m.x10*m.x17) - 15.1566541273553*m.x20
                         - 8.80731581347371*m.x23 - 3.4610247518095*m.x26 - 50.3685901711814*m.x29 == 0)

m.c68 = Constraint(expr=m.x48**1.25*m.x33 - (166.989461022824*m.x1*m.x12 + 44.9545980014895*m.x2*m.x12 + 
                        12.2050524378911*m.x3*m.x18 + 17.7827941003892*m.x4*m.x15 + 15.5884572681199*m.x5*m.x15 + 
                        4.61688063363795*m.x6*m.x12 + 18.2284698685036*m.x7*m.x15 + 13.8760966290575*m.x8*m.x15 + 
                        2.5279828213557*m.x9*m.x18 + 12.2050524378911*m.x10*m.x18) - 15.1566541273553*m.x21
                         - 8.80731581347371*m.x24 - 3.4610247518095*m.x27 - 50.3685901711814*m.x30 == 0)

m.c69 = Constraint(expr=m.x59**1.25*m.x34 - (166.989461022824*m.x1*m.x13 + 44.9545980014895*m.x2*m.x13 + 
                        12.2050524378911*m.x3*m.x19 + 17.7827941003892*m.x4*m.x16 + 15.5884572681199*m.x5*m.x16 + 
                        4.61688063363795*m.x6*m.x13 + 18.2284698685036*m.x7*m.x16 + 13.8760966290575*m.x8*m.x16 + 
                        2.5279828213557*m.x9*m.x19 + 12.2050524378911*m.x10*m.x19) - 15.1566541273553*m.x22
                         - 8.80731581347371*m.x25 - 3.4610247518095*m.x28 - 50.3685901711814*m.x31 == 0)

m.c70 = Constraint(expr=-53.54*(0.444*exp((-1.26152) + 0.0006197*m.x36 + 0.22239*m.x41 + 0.02655*m.x285 - 0.003376*
                        m.x288) + 0.556*exp((-1.76845) - 0.096047*m.x35 + 0.000337*m.x36 + 0.222318*m.x41 + 0.011882*
                        m.x285 + 0.011251*m.x288)) + m.x318 == 0)

m.c71 = Constraint(expr=-53.54*(0.444*exp((-1.26152) + 0.0006197*m.x47 + 0.22239*m.x52 + 0.02655*m.x286 - 0.003376*
                        m.x289) + 0.556*exp((-1.76845) - 0.096047*m.x46 + 0.000337*m.x47 + 0.222318*m.x52 + 0.011882*
                        m.x286 + 0.011251*m.x289)) + m.x319 == 0)

m.c72 = Constraint(expr=-53.54*(0.444*exp((-1.26152) + 0.0006197*m.x58 + 0.22239*m.x63 + 0.02655*m.x287 - 0.003376*
                        m.x290) + 0.556*exp((-1.76845) - 0.096047*m.x57 + 0.000337*m.x58 + 0.222318*m.x63 + 0.011882*
                        m.x287 + 0.011251*m.x290)) + m.x320 == 0)

m.c73 = Constraint(expr=-9.7*(0.444*exp(1.07807 + 0.0462131*m.x43 - 0.007166*m.x285 - 0.010226*m.x288) + 0.556*exp(
                        1.36651 - 0.031352*m.x42 + 0.0462131*m.x43 - 0.007166*m.x285 - 0.010226*m.x288)) + m.x321 == 0)

m.c74 = Constraint(expr=-9.7*(0.444*exp(1.07807 + 0.0462131*m.x54 - 0.007166*m.x286 - 0.010226*m.x289) + 0.556*exp(
                        1.36651 - 0.031352*m.x53 + 0.0462131*m.x54 - 0.007166*m.x286 - 0.010226*m.x289)) + m.x322 == 0)

m.c75 = Constraint(expr=-9.7*(0.444*exp(1.07807 + 0.0462131*m.x65 - 0.007166*m.x287 - 0.010226*m.x290) + 0.556*exp(
                        1.36651 - 0.031352*m.x64 + 0.0462131*m.x65 - 0.007166*m.x287 - 0.010226*m.x290)) + m.x323 == 0)

m.c76 = Constraint(expr=-4.44*(0.444*exp(0.751747 + 0.0002631*m.x36 + 0.039786*m.x37 - 0.009594*m.x43 + 0.31658*m.x44 + 
                        0.24925*m.x45 - 0.005525*m.x285 - 0.012172*m.x288) + 0.556*exp(1.09751 + 0.0002627*m.x36 - 
                        0.05598*m.x43 + 0.3164665*m.x44 + 0.2493259*m.x45 - 0.005548*m.x285 - 0.012157*m.x288)) + m.x324
                         == 0)

m.c77 = Constraint(expr=-4.44*(0.444*exp(0.751747 + 0.0002631*m.x47 + 0.039786*m.x48 - 0.009594*m.x54 + 0.31658*m.x55 + 
                        0.24925*m.x56 - 0.005525*m.x286 - 0.012172*m.x289) + 0.556*exp(1.09751 + 0.0002627*m.x47 - 
                        0.05598*m.x54 + 0.3164665*m.x55 + 0.2493259*m.x56 - 0.005548*m.x286 - 0.012157*m.x289)) + m.x325
                         == 0)

m.c78 = Constraint(expr=-4.44*(0.444*exp(0.751747 + 0.0002631*m.x58 + 0.039786*m.x59 - 0.009594*m.x65 + 0.31658*m.x66 + 
                        0.24925*m.x67 - 0.005525*m.x287 - 0.012172*m.x290) + 0.556*exp(1.09751 + 0.0002627*m.x58 - 
                        0.05598*m.x65 + 0.3164665*m.x66 + 0.2493259*m.x67 - 0.005548*m.x287 - 0.012157*m.x290)) + m.x326
                         == 0)

m.c79 = Constraint(expr=-9.38*(0.444*exp(1.34704 + 0.0001552*m.x36 - 0.007253*m.x38 + 0.028235*m.x42 - 0.004005*m.x285
                         - 0.014866*m.x288) + 0.556*exp(0.694224 - 0.060771*m.x35 - 0.007311*m.x38 + 0.043696*m.x42 - 
                        0.004005*m.x285 - 0.008052*m.x288)) + m.x327 == 0)

m.c80 = Constraint(expr=-9.38*(0.444*exp(1.34704 + 0.0001552*m.x47 - 0.007253*m.x49 + 0.028235*m.x53 - 0.004005*m.x286
                         - 0.014866*m.x289) + 0.556*exp(0.694224 - 0.060771*m.x46 - 0.007311*m.x49 + 0.043696*m.x53 - 
                        0.004005*m.x286 - 0.008052*m.x289)) + m.x328 == 0)

m.c81 = Constraint(expr=-9.38*(0.444*exp(1.34704 + 0.0001552*m.x58 - 0.007253*m.x60 + 0.028235*m.x64 - 0.004005*m.x287
                         - 0.014866*m.x290) + 0.556*exp(0.694224 - 0.060771*m.x57 - 0.007311*m.x60 + 0.043696*m.x64 - 
                        0.004005*m.x287 - 0.008052*m.x290)) + m.x329 == 0)

m.c82 = Constraint(expr=-10*(1.75021*m.x41 - 0.603184*m.x37*m.x41 - 0.0402619*m.x43*m.x41 + 0.0738116*m.x37*m.x37*m.x41
                         + 0.0116427*m.x37*m.x43*m.x41 - 0.00255327*m.x37*m.x37*m.x37*m.x41 - 0.0010494*m.x37*m.x37*
                        m.x43*m.x41) + m.x330 == 0)

m.c83 = Constraint(expr=-10*(1.75021*m.x52 - 0.603184*m.x48*m.x52 - 0.0402619*m.x54*m.x52 + 0.0738116*m.x48*m.x48*m.x52
                         + 0.0116427*m.x48*m.x54*m.x52 - 0.00255327*m.x48*m.x48*m.x48*m.x52 - 0.0010494*m.x48*m.x48*
                        m.x54*m.x52) + m.x331 == 0)

m.c84 = Constraint(expr=-10*(1.75021*m.x63 - 0.603184*m.x59*m.x63 - 0.0402619*m.x65*m.x63 + 0.0738116*m.x59*m.x59*m.x63
                         + 0.0116427*m.x59*m.x65*m.x63 - 0.00255327*m.x59*m.x59*m.x59*m.x63 - 0.0010494*m.x59*m.x59*
                        m.x65*m.x63) + m.x332 == 0)

m.c85 = Constraint(expr=   0.003355*m.x297 + m.x318 + m.x321 + m.x324 + m.x327 + m.x330 <= 95)

m.c86 = Constraint(expr=   0.003355*m.x298 + m.x319 + m.x322 + m.x325 + m.x328 + m.x331 <= 95)

m.c87 = Constraint(expr=   0.003355*m.x299 + m.x320 + m.x323 + m.x326 + m.x329 + m.x332 <= 95)

m.c88 = Constraint(expr= - m.x276 + m.x288 == 0)

m.c89 = Constraint(expr= - m.x277 + m.x289 == 0)

m.c90 = Constraint(expr= - m.x278 + m.x290 == 0)

m.c91 = Constraint(expr=   40*m.b72 + m.x285 <= 50)

m.c92 = Constraint(expr=   40*m.b73 + m.x286 <= 50)

m.c93 = Constraint(expr=   40*m.b74 + m.x287 <= 50)

m.c94 = Constraint(expr=   10*m.b72 - m.x285 <= 0)

m.c95 = Constraint(expr=   10*m.b73 - m.x286 <= 0)

m.c96 = Constraint(expr=   10*m.b74 - m.x287 <= 0)

m.c97 = Constraint(expr= - m.x40 - 50*m.b72 + m.x285 <= 0)

m.c98 = Constraint(expr= - m.x51 - 50*m.b73 + m.x286 <= 0)

m.c99 = Constraint(expr= - m.x62 - 50*m.b74 + m.x287 <= 0)

m.c100 = Constraint(expr=   m.x40 - 50*m.b72 - m.x285 <= 0)

m.c101 = Constraint(expr=   m.x51 - 50*m.b73 - m.x286 <= 0)

m.c102 = Constraint(expr=   m.x62 - 50*m.b74 - m.x287 <= 0)

m.c103 = Constraint(expr=-1340*(0.738*exp((-0.497032) + 0.0006921*m.x36 - 6.63e-7*m.x36**2 - 0.000119*m.x279**2 + 
                         0.0083632*m.x279 + 0.0003665*m.x282**2 - 0.002774*m.x282 + 0.0018571*m.x35 + 0.0090744*m.x37 + 
                         0.000931*m.x38 + 0.000846*m.x276)*m.x312 + 0.262*exp(0.179906 + 0.007097*m.x279 - 7.995e-5*
                         m.x279**2 + 0.0003665*m.x282**2 - 0.00276*m.x282 - 0.00913*m.x35 + 0.000252*m.x36 - 0.01397*
                         m.x37 + 0.000931*m.x38 - 0.00401*m.x276)*m.x313) + m.x309 == 0)

m.c104 = Constraint(expr=-1340*(0.738*exp((-0.497032) + 0.0006921*m.x47 - 6.63e-7*m.x47**2 - 0.000119*m.x280**2 + 
                         0.0083632*m.x280 + 0.0003665*m.x283**2 - 0.002774*m.x283 + 0.0018571*m.x46 + 0.0090744*m.x48 + 
                         0.000931*m.x49 + 0.000846*m.x277)*m.x314 + 0.262*exp(0.179906 + 0.007097*m.x280 - 7.995e-5*
                         m.x280**2 + 0.0003665*m.x283**2 - 0.00276*m.x283 - 0.00913*m.x46 + 0.000252*m.x47 - 0.01397*
                         m.x48 + 0.000931*m.x49 - 0.00401*m.x277)*m.x315) + m.x310 == 0)

m.c105 = Constraint(expr=-1340*(0.738*exp((-0.497032) + 0.0006921*m.x58 - 6.63e-7*m.x58**2 - 0.000119*m.x281**2 + 
                         0.0083632*m.x281 + 0.0003665*m.x284**2 - 0.002774*m.x284 + 0.0018571*m.x57 + 0.0090744*m.x59 + 
                         0.000931*m.x60 + 0.000846*m.x278)*m.x316 + 0.262*exp(0.179906 + 0.007097*m.x281 - 7.995e-5*
                         m.x281**2 + 0.0003665*m.x284**2 - 0.00276*m.x284 - 0.00913*m.x57 + 0.000252*m.x58 - 0.01397*
                         m.x59 + 0.000931*m.x60 - 0.00401*m.x278)*m.x317) + m.x311 == 0)

m.c106 = Constraint(expr=   m.x309 <= 1400)

m.c107 = Constraint(expr=   m.x310 <= 1400)

m.c108 = Constraint(expr=   m.x311 <= 1400)

m.c109 = Constraint(expr= - m.x234 - m.x240 - m.x246 + m.x312 == 1)

m.c110 = Constraint(expr= - m.x235 - m.x241 - m.x247 + m.x313 == 1)

m.c111 = Constraint(expr= - m.x236 - m.x242 - m.x248 + m.x314 == 1)

m.c112 = Constraint(expr= - m.x237 - m.x243 - m.x249 + m.x315 == 1)

m.c113 = Constraint(expr= - m.x238 - m.x244 - m.x250 + m.x316 == 1)

m.c114 = Constraint(expr= - m.x239 - m.x245 - m.x251 + m.x317 == 1)

m.c115 = Constraint(expr=   120*m.b96 + m.x273 <= 130)

m.c116 = Constraint(expr=   190*m.b97 + m.x274 <= 200)

m.c117 = Constraint(expr=   240*m.b98 + m.x275 <= 250)

m.c118 = Constraint(expr= - 10*m.b96 + m.x273 >= 0)

m.c119 = Constraint(expr= - 10*m.b97 + m.x274 >= 0)

m.c120 = Constraint(expr= - 10*m.b98 + m.x275 >= 0)

m.c121 = Constraint(expr= - m.x36 - 130*m.b96 + 130*m.b99 + m.x273 <= 130)

m.c122 = Constraint(expr= - m.x47 - 200*m.b97 + 200*m.b100 + m.x274 <= 200)

m.c123 = Constraint(expr= - m.x58 - 250*m.b98 + 250*m.b101 + m.x275 <= 250)

m.c124 = Constraint(expr= - m.x36 + 130*m.b96 - 130*m.b99 + m.x273 >= -130)

m.c125 = Constraint(expr= - m.x47 + 200*m.b97 - 200*m.b100 + m.x274 >= -200)

m.c126 = Constraint(expr= - m.x58 + 250*m.b98 - 250*m.b101 + m.x275 >= -250)

m.c127 = Constraint(expr=   320*m.b99 + m.x273 <= 450)

m.c128 = Constraint(expr=   250*m.b100 + m.x274 <= 450)

m.c129 = Constraint(expr=   200*m.b101 + m.x275 <= 450)

m.c130 = Constraint(expr=   450*m.b99 + m.x273 >= 450)

m.c131 = Constraint(expr=   450*m.b100 + m.x274 >= 450)

m.c132 = Constraint(expr=   450*m.b101 + m.x275 >= 450)

m.c133 = Constraint(expr= - 5*m.b69 + m.x276 <= 95)

m.c134 = Constraint(expr= - 5*m.b70 + m.x277 <= 95)

m.c135 = Constraint(expr= - 5*m.b71 + m.x278 <= 95)

m.c136 = Constraint(expr= - 25*m.b69 - m.x276 <= -95)

m.c137 = Constraint(expr= - 25*m.b70 - m.x277 <= -95)

m.c138 = Constraint(expr= - 25*m.b71 - m.x278 <= -95)

m.c139 = Constraint(expr= - m.x39 + 30*m.b69 + m.x276 <= 30)

m.c140 = Constraint(expr= - m.x50 + 30*m.b70 + m.x277 <= 30)

m.c141 = Constraint(expr= - m.x61 + 30*m.b71 + m.x278 <= 30)

m.c142 = Constraint(expr=   m.x39 + 30*m.b69 - m.x276 <= 30)

m.c143 = Constraint(expr=   m.x50 + 30*m.b70 - m.x277 <= 30)

m.c144 = Constraint(expr=   m.x61 + 30*m.b71 - m.x278 <= 30)

m.c145 = Constraint(expr=   32*m.b102 + m.x279 <= 50)

m.c146 = Constraint(expr=   32*m.b103 + m.x280 <= 50)

m.c147 = Constraint(expr=   32*m.b104 + m.x281 <= 50)

m.c148 = Constraint(expr= - 18*m.b102 + m.x279 >= 0)

m.c149 = Constraint(expr= - 18*m.b103 + m.x280 >= 0)

m.c150 = Constraint(expr= - 18*m.b104 + m.x281 >= 0)

m.c151 = Constraint(expr= - m.x40 - 50*m.b102 + 50*m.b105 + m.x279 <= 50)

m.c152 = Constraint(expr= - m.x51 - 50*m.b103 + 50*m.b106 + m.x280 <= 50)

m.c153 = Constraint(expr= - m.x62 - 50*m.b104 + 50*m.b107 + m.x281 <= 50)

m.c154 = Constraint(expr= - m.x40 + 50*m.b102 - 50*m.b105 + m.x279 >= -50)

m.c155 = Constraint(expr= - m.x51 + 50*m.b103 - 50*m.b106 + m.x280 >= -50)

m.c156 = Constraint(expr= - m.x62 + 50*m.b104 - 50*m.b107 + m.x281 >= -50)

m.c157 = Constraint(expr= - 13.2*m.b105 + m.x279 <= 36.8)

m.c158 = Constraint(expr= - 13.2*m.b106 + m.x280 <= 36.8)

m.c159 = Constraint(expr= - 13.2*m.b107 + m.x281 <= 36.8)

m.c160 = Constraint(expr=   36.8*m.b105 + m.x279 >= 36.8)

m.c161 = Constraint(expr=   36.8*m.b106 + m.x280 >= 36.8)

m.c162 = Constraint(expr=   36.8*m.b107 + m.x281 >= 36.8)

m.c163 = Constraint(expr=   21.23*m.b108 + m.x282 <= 25)

m.c164 = Constraint(expr=   21.23*m.b109 + m.x283 <= 25)

m.c165 = Constraint(expr=   21.23*m.b110 + m.x284 <= 25)

m.c166 = Constraint(expr= - 3.77*m.b108 + m.x282 >= 0)

m.c167 = Constraint(expr= - 3.77*m.b109 + m.x283 >= 0)

m.c168 = Constraint(expr= - 3.77*m.b110 + m.x284 >= 0)

m.c169 = Constraint(expr= - m.x42 - 25*m.b108 + 25*m.b111 + m.x282 <= 25)

m.c170 = Constraint(expr= - m.x53 - 25*m.b109 + 25*m.b112 + m.x283 <= 25)

m.c171 = Constraint(expr= - m.x64 - 25*m.b110 + 25*m.b113 + m.x284 <= 25)

m.c172 = Constraint(expr= - m.x42 + 25*m.b108 - 25*m.b111 + m.x282 >= -25)

m.c173 = Constraint(expr= - m.x53 + 25*m.b109 - 25*m.b112 + m.x283 >= -25)

m.c174 = Constraint(expr= - m.x64 + 25*m.b110 - 25*m.b113 + m.x284 >= -25)

m.c175 = Constraint(expr= - 6*m.b111 + m.x282 <= 19)

m.c176 = Constraint(expr= - 6*m.b112 + m.x283 <= 19)

m.c177 = Constraint(expr= - 6*m.b113 + m.x284 <= 19)

m.c178 = Constraint(expr=   19*m.b111 + m.x282 >= 19)

m.c179 = Constraint(expr=   19*m.b112 + m.x283 >= 19)

m.c180 = Constraint(expr=   19*m.b113 + m.x284 >= 19)

m.c181 = Constraint(expr=   0.1243908*m.b96 + m.x138 + m.x144 <= 0.1243908)

m.c182 = Constraint(expr=   0.14364*m.b96 + m.x139 + m.x145 <= 0.14364)

m.c183 = Constraint(expr=   0.1719096*m.b97 + m.x140 + m.x146 <= 0.1719096)

m.c184 = Constraint(expr=   0.16128*m.b97 + m.x141 + m.x147 <= 0.16128)

m.c185 = Constraint(expr=   0.2058516*m.b98 + m.x142 + m.x148 <= 0.2058516)

m.c186 = Constraint(expr=   0.17388*m.b98 + m.x143 + m.x149 <= 0.17388)

m.c187 = Constraint(expr= - 0.1243908*m.b96 + 0.1243908*m.b99 + m.x126 + m.x132 <= 0.1243908)

m.c188 = Constraint(expr= - 0.14364*m.b96 + 0.14364*m.b99 + m.x127 + m.x133 <= 0.14364)

m.c189 = Constraint(expr= - 0.1719096*m.b97 + 0.1719096*m.b100 + m.x128 + m.x134 <= 0.1719096)

m.c190 = Constraint(expr= - 0.16128*m.b97 + 0.16128*m.b100 + m.x129 + m.x135 <= 0.16128)

m.c191 = Constraint(expr= - 0.2058516*m.b98 + 0.2058516*m.b101 + m.x130 + m.x136 <= 0.2058516)

m.c192 = Constraint(expr= - 0.17388*m.b98 + 0.17388*m.b101 + m.x131 + m.x137 <= 0.17388)

m.c193 = Constraint(expr= - 0.1243908*m.b99 + m.x114 + m.x120 <= 0)

m.c194 = Constraint(expr= - 0.14364*m.b99 + m.x115 + m.x121 <= 0)

m.c195 = Constraint(expr= - 0.1719096*m.b100 + m.x116 + m.x122 <= 0)

m.c196 = Constraint(expr= - 0.16128*m.b100 + m.x117 + m.x123 <= 0)

m.c197 = Constraint(expr= - 0.2058516*m.b101 + m.x118 + m.x124 <= 0)

m.c198 = Constraint(expr= - 0.17388*m.b101 + m.x119 + m.x125 <= 0)

m.c199 = Constraint(expr= - 0.00067884*m.x36 + m.x138 - m.x144 + m.x234 == -0.0067884)

m.c200 = Constraint(expr= - 0.000252*m.x36 + m.x139 - m.x145 + m.x235 == -0.00252)

m.c201 = Constraint(expr= - 0.00067884*m.x47 + m.x140 - m.x146 + m.x236 == -0.0067884)

m.c202 = Constraint(expr= - 0.000252*m.x47 + m.x141 - m.x147 + m.x237 == -0.00252)

m.c203 = Constraint(expr= - 0.00067884*m.x58 + m.x142 - m.x148 + m.x238 == -0.0067884)

m.c204 = Constraint(expr= - 0.000252*m.x58 + m.x143 - m.x149 + m.x239 == -0.00252)

m.c205 = Constraint(expr=   m.x126 - m.x132 + m.x234 == 0)

m.c206 = Constraint(expr=   m.x127 - m.x133 + m.x235 == 0)

m.c207 = Constraint(expr=   m.x128 - m.x134 + m.x236 == 0)

m.c208 = Constraint(expr=   m.x129 - m.x135 + m.x237 == 0)

m.c209 = Constraint(expr=   m.x130 - m.x136 + m.x238 == 0)

m.c210 = Constraint(expr=   m.x131 - m.x137 + m.x239 == 0)

m.c211 = Constraint(expr= - 9.53999999999999E-5*m.x36 + m.x114 - m.x120 + m.x234 == -0.04293)

m.c212 = Constraint(expr= - 0.000252*m.x36 + m.x115 - m.x121 + m.x235 == -0.1134)

m.c213 = Constraint(expr= - 9.53999999999999E-5*m.x47 + m.x116 - m.x122 + m.x236 == -0.04293)

m.c214 = Constraint(expr= - 0.000252*m.x47 + m.x117 - m.x123 + m.x237 == -0.1134)

m.c215 = Constraint(expr= - 9.53999999999999E-5*m.x58 + m.x118 - m.x124 + m.x238 == -0.04293)

m.c216 = Constraint(expr= - 0.000252*m.x58 + m.x119 - m.x125 + m.x239 == -0.1134)

m.c217 = Constraint(expr=   0.20396*m.b72 + m.x174 + m.x180 <= 0.20396)

m.c218 = Constraint(expr=   0.21094*m.b72 + m.x175 + m.x181 <= 0.21094)

m.c219 = Constraint(expr=   0.20396*m.b73 + m.x176 + m.x182 <= 0.20396)

m.c220 = Constraint(expr=   0.21094*m.b73 + m.x177 + m.x183 <= 0.21094)

m.c221 = Constraint(expr=   0.20396*m.b74 + m.x178 + m.x184 <= 0.20396)

m.c222 = Constraint(expr=   0.21094*m.b74 + m.x179 + m.x185 <= 0.21094)

m.c223 = Constraint(expr= - 0.20396*m.b72 + 0.20396*m.b102 + m.x162 + m.x168 <= 0.20396)

m.c224 = Constraint(expr= - 0.21094*m.b72 + 0.21094*m.b102 + m.x163 + m.x169 <= 0.21094)

m.c225 = Constraint(expr= - 0.20396*m.b73 + 0.20396*m.b103 + m.x164 + m.x170 <= 0.20396)

m.c226 = Constraint(expr= - 0.21094*m.b73 + 0.21094*m.b103 + m.x165 + m.x171 <= 0.21094)

m.c227 = Constraint(expr= - 0.20396*m.b74 + 0.20396*m.b104 + m.x166 + m.x172 <= 0.20396)

m.c228 = Constraint(expr= - 0.21094*m.b74 + 0.21094*m.b104 + m.x167 + m.x173 <= 0.21094)

m.c229 = Constraint(expr= - 0.20396*m.b102 + m.x150 + m.x156 <= 0)

m.c230 = Constraint(expr= - 0.21094*m.b102 + m.x151 + m.x157 <= 0)

m.c231 = Constraint(expr= - 0.20396*m.b103 + m.x152 + m.x158 <= 0)

m.c232 = Constraint(expr= - 0.21094*m.b103 + m.x153 + m.x159 <= 0)

m.c233 = Constraint(expr= - 0.20396*m.b104 + m.x154 + m.x160 <= 0)

m.c234 = Constraint(expr= - 0.21094*m.b104 + m.x155 + m.x161 <= 0)

m.c235 = Constraint(expr=   m.x174 - m.x180 + m.x240 == -0.0326336)

m.c236 = Constraint(expr=   m.x175 - m.x181 + m.x241 == -0.0337504)

m.c237 = Constraint(expr=   m.x176 - m.x182 + m.x242 == -0.0326336)

m.c238 = Constraint(expr=   m.x177 - m.x183 + m.x243 == -0.0337504)

m.c239 = Constraint(expr=   m.x178 - m.x184 + m.x244 == -0.0326336)

m.c240 = Constraint(expr=   m.x179 - m.x185 + m.x245 == -0.0337504)

m.c241 = Constraint(expr= - 0.0040792*m.x40 + m.x162 - m.x168 + m.x240 == -0.0734256)

m.c242 = Constraint(expr= - 0.0042188*m.x40 + m.x163 - m.x169 + m.x241 == -0.0759384)

m.c243 = Constraint(expr= - 0.0040792*m.x51 + m.x164 - m.x170 + m.x242 == -0.0734256)

m.c244 = Constraint(expr= - 0.0042188*m.x51 + m.x165 - m.x171 + m.x243 == -0.0759384)

m.c245 = Constraint(expr= - 0.0040792*m.x62 + m.x166 - m.x172 + m.x244 == -0.0734256)

m.c246 = Constraint(expr= - 0.0042188*m.x62 + m.x167 - m.x173 + m.x245 == -0.0759384)

m.c247 = Constraint(expr=   m.x150 - m.x156 + m.x240 == 0)

m.c248 = Constraint(expr=   m.x151 - m.x157 + m.x241 == 0)

m.c249 = Constraint(expr=   m.x152 - m.x158 + m.x242 == 0)

m.c250 = Constraint(expr=   m.x153 - m.x159 + m.x243 == 0)

m.c251 = Constraint(expr=   m.x154 - m.x160 + m.x244 == 0)

m.c252 = Constraint(expr=   m.x155 - m.x161 + m.x245 == 0)

m.c253 = Constraint(expr=   0.278825*m.b111 + m.x198 + m.x204 <= 0.278825)

m.c254 = Constraint(expr=   0.279175*m.b111 + m.x199 + m.x205 <= 0.279175)

m.c255 = Constraint(expr=   0.278825*m.b112 + m.x200 + m.x206 <= 0.278825)

m.c256 = Constraint(expr=   0.279175*m.b112 + m.x201 + m.x207 <= 0.279175)

m.c257 = Constraint(expr=   0.278825*m.b113 + m.x202 + m.x208 <= 0.278825)

m.c258 = Constraint(expr=   0.279175*m.b113 + m.x203 + m.x209 <= 0.279175)

m.c259 = Constraint(expr= - 0.278825*m.b111 + m.x186 + m.x192 <= 0)

m.c260 = Constraint(expr= - 0.279175*m.b111 + m.x187 + m.x193 <= 0)

m.c261 = Constraint(expr= - 0.278825*m.b112 + m.x188 + m.x194 <= 0)

m.c262 = Constraint(expr= - 0.279175*m.b112 + m.x189 + m.x195 <= 0)

m.c263 = Constraint(expr= - 0.278825*m.b113 + m.x190 + m.x196 <= 0)

m.c264 = Constraint(expr= - 0.279175*m.b113 + m.x191 + m.x197 <= 0)

m.c265 = Constraint(expr=   m.x198 - m.x204 + m.x246 == 0)

m.c266 = Constraint(expr=   m.x199 - m.x205 + m.x247 == 0)

m.c267 = Constraint(expr=   m.x200 - m.x206 + m.x248 == 0)

m.c268 = Constraint(expr=   m.x201 - m.x207 + m.x249 == 0)

m.c269 = Constraint(expr=   m.x202 - m.x208 + m.x250 == 0)

m.c270 = Constraint(expr=   m.x203 - m.x209 + m.x251 == 0)

m.c271 = Constraint(expr= - 0.011153*m.x42 + m.x186 - m.x192 + m.x246 == -0.211907)

m.c272 = Constraint(expr= - 0.011167*m.x42 + m.x187 - m.x193 + m.x247 == -0.212173)

m.c273 = Constraint(expr= - 0.011153*m.x53 + m.x188 - m.x194 + m.x248 == -0.211907)

m.c274 = Constraint(expr= - 0.011167*m.x53 + m.x189 - m.x195 + m.x249 == -0.212173)

m.c275 = Constraint(expr= - 0.011153*m.x64 + m.x190 - m.x196 + m.x250 == -0.211907)

m.c276 = Constraint(expr= - 0.011167*m.x64 + m.x191 - m.x197 + m.x251 == -0.212173)

m.c277 = Constraint(expr=-907*(0.444*exp(2.77929 + 0.0001072*m.x261**2 - 0.01447*m.x261 + 0.0004087*m.x270**2 - 0.068624
                         *m.x270 - 0.0003481*m.x264*m.x270 + 0.0323712*m.x264 - 0.003641*m.x35 + 0.0005219*m.x36 + 
                         0.0289749*m.x37 - 0.002858*m.x42)*m.x303 + 0.556*exp(2.26558 + 0.000106*m.x261**2 - 0.013504*
                         m.x261 + 0.000408*m.x270**2 - 0.062327*m.x270 - 0.000287*m.x264*m.x270 + 0.0282042*m.x264 - 
                         0.003626*m.x35 - 5.4e-5*m.x36 + 0.043295*m.x37 - 0.002858*m.x42)*m.x304) + m.x297 == 0)

m.c278 = Constraint(expr=-907*(0.444*exp(2.77929 + 0.0001072*m.x262**2 - 0.01447*m.x262 + 0.0004087*m.x271**2 - 0.068624
                         *m.x271 - 0.0003481*m.x265*m.x271 + 0.0323712*m.x265 - 0.003641*m.x46 + 0.0005219*m.x47 + 
                         0.0289749*m.x48 - 0.002858*m.x53)*m.x305 + 0.556*exp(2.26558 + 0.000106*m.x262**2 - 0.013504*
                         m.x262 + 0.000408*m.x271**2 - 0.062327*m.x271 - 0.000287*m.x265*m.x271 + 0.0282042*m.x265 - 
                         0.003626*m.x46 - 5.4e-5*m.x47 + 0.043295*m.x48 - 0.002858*m.x53)*m.x306) + m.x298 == 0)

m.c279 = Constraint(expr=-907*(0.444*exp(2.77929 + 0.0001072*m.x263**2 - 0.01447*m.x263 + 0.0004087*m.x272**2 - 0.068624
                         *m.x272 - 0.0003481*m.x266*m.x272 + 0.0323712*m.x266 - 0.003641*m.x57 + 0.0005219*m.x58 + 
                         0.0289749*m.x59 - 0.002858*m.x64)*m.x307 + 0.556*exp(2.26558 + 0.000106*m.x263**2 - 0.013504*
                         m.x263 + 0.000408*m.x272**2 - 0.062327*m.x272 - 0.000287*m.x266*m.x272 + 0.0282042*m.x266 - 
                         0.003626*m.x57 - 5.4e-5*m.x58 + 0.043295*m.x59 - 0.002858*m.x64)*m.x308) + m.x299 == 0)

m.c280 = Constraint(expr=-1000*(0.0318*m.x258**2 - 0.3534*m.x258) + m.x300 == 1226.9)

m.c281 = Constraint(expr=-1000*(0.0318*m.x259**2 - 0.3534*m.x259) + m.x301 == 1226.9)

m.c282 = Constraint(expr=-1000*(0.0318*m.x260**2 - 0.3534*m.x260) + m.x302 == 1226.9)

m.c283 = Constraint(expr=   m.x297 + m.x300 <= 1700)

m.c284 = Constraint(expr=   m.x298 + m.x301 <= 1700)

m.c285 = Constraint(expr=   m.x299 + m.x302 <= 1700)

m.c286 = Constraint(expr=-((0.0323712 - 0.0003481*m.x270)*m.x291 + (-0.068624 - 0.0003481*m.x264 + 0.0008174*m.x270)*
                         m.x294) - m.x252 + m.x303 == 1)

m.c287 = Constraint(expr=-((0.0282042 - 0.000287*m.x270)*m.x291 + (-0.062327 - 0.000287*m.x264 + 0.000816*m.x270)*m.x294
                         ) - m.x253 + m.x304 == 1)

m.c288 = Constraint(expr=-((0.0323712 - 0.0003481*m.x271)*m.x292 + (-0.068624 - 0.0003481*m.x265 + 0.0008174*m.x271)*
                         m.x295) - m.x254 + m.x305 == 1)

m.c289 = Constraint(expr=-((0.0282042 - 0.000287*m.x271)*m.x292 + (-0.062327 - 0.000287*m.x265 + 0.000816*m.x271)*m.x295
                         ) - m.x255 + m.x306 == 1)

m.c290 = Constraint(expr=-((0.0323712 - 0.0003481*m.x272)*m.x293 + (-0.068624 - 0.0003481*m.x266 + 0.0008174*m.x272)*
                         m.x296) - m.x256 + m.x307 == 1)

m.c291 = Constraint(expr=-((0.0282042 - 0.000287*m.x272)*m.x293 + (-0.062327 - 0.000287*m.x266 + 0.000816*m.x272)*m.x296
                         ) - m.x257 + m.x308 == 1)

m.c292 = Constraint(expr=   28*m.b81 + m.x270 <= 100)

m.c293 = Constraint(expr=   28*m.b82 + m.x271 <= 100)

m.c294 = Constraint(expr=   28*m.b83 + m.x272 <= 100)

m.c295 = Constraint(expr= - 2*m.b81 + m.x270 >= 70)

m.c296 = Constraint(expr= - 2*m.b82 + m.x271 >= 70)

m.c297 = Constraint(expr= - 2*m.b83 + m.x272 >= 70)

m.c298 = Constraint(expr= - m.x39 - 30*m.b81 + 30*m.b93 + m.x270 <= 30)

m.c299 = Constraint(expr= - m.x50 - 30*m.b82 + 30*m.b94 + m.x271 <= 30)

m.c300 = Constraint(expr= - m.x61 - 30*m.b83 + 30*m.b95 + m.x272 <= 30)

m.c301 = Constraint(expr= - m.x39 + 30*m.b81 - 30*m.b93 + m.x270 >= -30)

m.c302 = Constraint(expr= - m.x50 + 30*m.b82 - 30*m.b94 + m.x271 >= -30)

m.c303 = Constraint(expr= - m.x61 + 30*m.b83 - 30*m.b95 + m.x272 >= -30)

m.c304 = Constraint(expr= - 16.4*m.b93 - m.x267 + m.x270 <= 0)

m.c305 = Constraint(expr= - 16.4*m.b94 - m.x268 + m.x271 <= 0)

m.c306 = Constraint(expr= - 16.4*m.b95 - m.x269 + m.x272 <= 0)

m.c307 = Constraint(expr=   29*m.b93 - m.x267 + m.x270 >= 0)

m.c308 = Constraint(expr=   29*m.b94 - m.x268 + m.x271 >= 0)

m.c309 = Constraint(expr=   29*m.b95 - m.x269 + m.x272 >= 0)

m.c310 = Constraint(expr= - m.x39 + 3*m.b81 + m.x294 <= -69)

m.c311 = Constraint(expr= - m.x50 + 3*m.b82 + m.x295 <= -69)

m.c312 = Constraint(expr= - m.x61 + 3*m.b83 + m.x296 <= -69)

m.c313 = Constraint(expr= - m.x39 - 30*m.b81 + m.x294 >= -102)

m.c314 = Constraint(expr= - m.x50 - 30*m.b82 + m.x295 >= -102)

m.c315 = Constraint(expr= - m.x61 - 30*m.b83 + m.x296 >= -102)

m.c316 = Constraint(expr=   2*m.b81 - 2*m.b93 + m.x294 >= -2)

m.c317 = Constraint(expr=   2*m.b82 - 2*m.b94 + m.x295 >= -2)

m.c318 = Constraint(expr=   2*m.b83 - 2*m.b95 + m.x296 >= -2)

m.c319 = Constraint(expr= - m.b81 + m.b93 + m.x294 <= 1)

m.c320 = Constraint(expr= - m.b82 + m.b94 + m.x295 <= 1)

m.c321 = Constraint(expr= - m.b83 + m.b95 + m.x296 <= 1)

m.c322 = Constraint(expr=   2*m.b81 + 2*m.b90 + m.x294 >= 0)

m.c323 = Constraint(expr=   2*m.b82 + 2*m.b91 + m.x295 >= 0)

m.c324 = Constraint(expr=   2*m.b83 + 2*m.b92 + m.x296 >= 0)

m.c325 = Constraint(expr= - m.b81 - m.b90 + m.x294 <= 0)

m.c326 = Constraint(expr= - m.b82 - m.b91 + m.x295 <= 0)

m.c327 = Constraint(expr= - m.b83 - m.b92 + m.x296 <= 0)

m.c328 = Constraint(expr= - m.x39 - 3*m.b90 + 3*m.b93 + m.x294 >= -97)

m.c329 = Constraint(expr= - m.x50 - 3*m.b91 + 3*m.b94 + m.x295 >= -97)

m.c330 = Constraint(expr= - m.x61 - 3*m.b92 + 3*m.b95 + m.x296 >= -97)

m.c331 = Constraint(expr= - m.x39 + 23*m.b90 - 23*m.b93 + m.x294 <= -71)

m.c332 = Constraint(expr= - m.x50 + 23*m.b91 - 23*m.b94 + m.x295 <= -71)

m.c333 = Constraint(expr= - m.x61 + 23*m.b92 - 23*m.b95 + m.x296 <= -71)

m.c334 = Constraint(expr=   15.4*m.b72 - 15.4*m.b90 + m.x267 <= 99)

m.c335 = Constraint(expr=   15.4*m.b73 - 15.4*m.b91 + m.x268 <= 99)

m.c336 = Constraint(expr=   15.4*m.b74 - 15.4*m.b92 + m.x269 <= 99)

m.c337 = Constraint(expr= - 3.85*m.b72 + 3.85*m.b90 + m.x267 >= 79.75)

m.c338 = Constraint(expr= - 3.85*m.b73 + 3.85*m.b91 + m.x268 >= 79.75)

m.c339 = Constraint(expr= - 3.85*m.b74 + 3.85*m.b92 + m.x269 >= 79.75)

m.c340 = Constraint(expr= - 0.385*m.x40 - 19.25*m.b72 - 19.25*m.b90 + m.x267 <= 79.75)

m.c341 = Constraint(expr= - 0.385*m.x51 - 19.25*m.b73 - 19.25*m.b91 + m.x268 <= 79.75)

m.c342 = Constraint(expr= - 0.385*m.x62 - 19.25*m.b74 - 19.25*m.b92 + m.x269 <= 79.75)

m.c343 = Constraint(expr= - 0.385*m.x40 + 19.25*m.b72 + 19.25*m.b90 + m.x267 >= 79.75)

m.c344 = Constraint(expr= - 0.385*m.x51 + 19.25*m.b73 + 19.25*m.b91 + m.x268 >= 79.75)

m.c345 = Constraint(expr= - 0.385*m.x62 + 19.25*m.b74 + 19.25*m.b92 + m.x269 >= 79.75)

m.c346 = Constraint(expr=   5*m.b90 + m.x267 <= 99)

m.c347 = Constraint(expr=   5*m.b91 + m.x268 <= 99)

m.c348 = Constraint(expr=   5*m.b92 + m.x269 <= 99)

m.c349 = Constraint(expr= - 14.25*m.b90 + m.x267 >= 79.75)

m.c350 = Constraint(expr= - 14.25*m.b91 + m.x268 >= 79.75)

m.c351 = Constraint(expr= - 14.25*m.b92 + m.x269 >= 79.75)

m.c352 = Constraint(expr=   m.x39 + 29*m.b93 - m.x267 >= 0)

m.c353 = Constraint(expr=   m.x50 + 29*m.b94 - m.x268 >= 0)

m.c354 = Constraint(expr=   m.x61 + 29*m.b95 - m.x269 >= 0)

m.c355 = Constraint(expr=   m.x39 + 16.4*m.b93 - m.x267 <= 16.4)

m.c356 = Constraint(expr=   m.x50 + 16.4*m.b94 - m.x268 <= 16.4)

m.c357 = Constraint(expr=   m.x61 + 16.4*m.b95 - m.x269 <= 16.4)

m.c358 = Constraint(expr=   32.52*m.b75 + m.x261 <= 65.52)

m.c359 = Constraint(expr=   32.52*m.b76 + m.x262 <= 65.52)

m.c360 = Constraint(expr=   32.52*m.b77 + m.x263 <= 65.52)

m.c361 = Constraint(expr=   m.x261 >= 33)

m.c362 = Constraint(expr=   m.x262 >= 33)

m.c363 = Constraint(expr=   m.x263 >= 33)

m.c364 = Constraint(expr= - m.x38 - 35.52*m.b75 + 35.52*m.b78 + m.x261 <= 35.52)

m.c365 = Constraint(expr= - m.x49 - 35.52*m.b76 + 35.52*m.b79 + m.x262 <= 35.52)

m.c366 = Constraint(expr= - m.x60 - 35.52*m.b77 + 35.52*m.b80 + m.x263 <= 35.52)

m.c367 = Constraint(expr= - m.x38 + 37*m.b75 - 37*m.b78 + m.x261 >= -37)

m.c368 = Constraint(expr= - m.x49 + 37*m.b76 - 37*m.b79 + m.x262 >= -37)

m.c369 = Constraint(expr= - m.x60 + 37*m.b77 - 37*m.b80 + m.x263 >= -37)

m.c370 = Constraint(expr=   m.x261 <= 65.52)

m.c371 = Constraint(expr=   m.x262 <= 65.52)

m.c372 = Constraint(expr=   m.x263 <= 65.52)

m.c373 = Constraint(expr=   32.52*m.b78 + m.x261 >= 65.52)

m.c374 = Constraint(expr=   32.52*m.b79 + m.x262 >= 65.52)

m.c375 = Constraint(expr=   32.52*m.b80 + m.x263 >= 65.52)

m.c376 = Constraint(expr=   0.295792*m.b75 + m.x222 + m.x228 <= 0.295792)

m.c377 = Constraint(expr=   0.26032*m.b75 + m.x223 + m.x229 <= 0.26032)

m.c378 = Constraint(expr=   0.295792*m.b76 + m.x224 + m.x230 <= 0.295792)

m.c379 = Constraint(expr=   0.26032*m.b76 + m.x225 + m.x231 <= 0.26032)

m.c380 = Constraint(expr=   0.295792*m.b77 + m.x226 + m.x232 <= 0.295792)

m.c381 = Constraint(expr=   0.26032*m.b77 + m.x227 + m.x233 <= 0.26032)

m.c382 = Constraint(expr= - 0.295792*m.b75 + m.x210 + m.x216 <= 0)

m.c383 = Constraint(expr= - 0.26032*m.b75 + m.x211 + m.x217 <= 0)

m.c384 = Constraint(expr= - 0.295792*m.b76 + m.x212 + m.x218 <= 0)

m.c385 = Constraint(expr= - 0.26032*m.b76 + m.x213 + m.x219 <= 0)

m.c386 = Constraint(expr= - 0.295792*m.b77 + m.x214 + m.x220 <= 0)

m.c387 = Constraint(expr= - 0.26032*m.b77 + m.x215 + m.x221 <= 0)

m.c388 = Constraint(expr=   0.0073948*m.x38 + m.x222 - m.x228 + m.x252 == 0.2440284)

m.c389 = Constraint(expr=   0.006508*m.x38 + m.x223 - m.x229 + m.x253 == 0.214764)

m.c390 = Constraint(expr=   0.0073948*m.x49 + m.x224 - m.x230 + m.x254 == 0.2440284)

m.c391 = Constraint(expr=   0.006508*m.x49 + m.x225 - m.x231 + m.x255 == 0.214764)

m.c392 = Constraint(expr=   0.0073948*m.x60 + m.x226 - m.x232 + m.x256 == 0.2440284)

m.c393 = Constraint(expr=   0.006508*m.x60 + m.x227 - m.x233 + m.x257 == 0.214764)

m.c394 = Constraint(expr=   m.x210 - m.x216 + m.x252 == 0)

m.c395 = Constraint(expr=   m.x211 - m.x217 + m.x253 == 0)

m.c396 = Constraint(expr=   m.x212 - m.x218 + m.x254 == 0)

m.c397 = Constraint(expr=   m.x213 - m.x219 + m.x255 == 0)

m.c398 = Constraint(expr=   m.x214 - m.x220 + m.x256 == 0)

m.c399 = Constraint(expr=   m.x215 - m.x221 + m.x257 == 0)

m.c400 = Constraint(expr=   12*m.b72 + m.x291 <= 4)

m.c401 = Constraint(expr=   12*m.b73 + m.x292 <= 4)

m.c402 = Constraint(expr=   12*m.b74 + m.x293 <= 4)

m.c403 = Constraint(expr=   m.x291 >= -8)

m.c404 = Constraint(expr=   m.x292 >= -8)

m.c405 = Constraint(expr=   m.x293 >= -8)

m.c406 = Constraint(expr= - m.x40 - 22*m.b72 + 22*m.b84 + m.x291 <= 4)

m.c407 = Constraint(expr= - m.x51 - 22*m.b73 + 22*m.b85 + m.x292 <= 4)

m.c408 = Constraint(expr= - m.x62 - 22*m.b74 + 22*m.b86 + m.x293 <= 4)

m.c409 = Constraint(expr= - m.x40 + 40*m.b72 - 40*m.b84 + m.x291 >= -58)

m.c410 = Constraint(expr= - m.x51 + 40*m.b73 - 40*m.b85 + m.x292 >= -58)

m.c411 = Constraint(expr= - m.x62 + 40*m.b74 - 40*m.b86 + m.x293 >= -58)

m.c412 = Constraint(expr= - 4*m.b84 + 4*m.b87 + m.x291 <= 4)

m.c413 = Constraint(expr= - 4*m.b85 + 4*m.b88 + m.x292 <= 4)

m.c414 = Constraint(expr= - 4*m.b86 + 4*m.b89 + m.x293 <= 4)

m.c415 = Constraint(expr=   8*m.b84 - 8*m.b87 + m.x291 >= -8)

m.c416 = Constraint(expr=   8*m.b85 - 8*m.b88 + m.x292 >= -8)

m.c417 = Constraint(expr=   8*m.b86 - 8*m.b89 + m.x293 >= -8)

m.c418 = Constraint(expr= - m.x40 - 50*m.b87 + m.x291 <= -46)

m.c419 = Constraint(expr= - m.x51 - 50*m.b88 + m.x292 <= -46)

m.c420 = Constraint(expr= - m.x62 - 50*m.b89 + m.x293 <= -46)

m.c421 = Constraint(expr= - m.x40 + 12*m.b87 + m.x291 >= -46)

m.c422 = Constraint(expr= - m.x51 + 12*m.b88 + m.x292 >= -46)

m.c423 = Constraint(expr= - m.x62 + 12*m.b89 + m.x293 >= -46)

m.c424 = Constraint(expr=   32*m.b84 + m.x264 <= 50)

m.c425 = Constraint(expr=   32*m.b85 + m.x265 <= 50)

m.c426 = Constraint(expr=   32*m.b86 + m.x266 <= 50)

m.c427 = Constraint(expr= - 18*m.b84 + m.x264 >= 0)

m.c428 = Constraint(expr= - 18*m.b85 + m.x265 >= 0)

m.c429 = Constraint(expr= - 18*m.b86 + m.x266 >= 0)

m.c430 = Constraint(expr= - m.x40 - 50*m.b84 + 50*m.b87 + m.x264 <= 50)

m.c431 = Constraint(expr= - m.x51 - 50*m.b85 + 50*m.b88 + m.x265 <= 50)

m.c432 = Constraint(expr= - m.x62 - 50*m.b86 + 50*m.b89 + m.x266 <= 50)

m.c433 = Constraint(expr= - m.x40 + 50*m.b84 - 50*m.b87 + m.x264 >= -50)

m.c434 = Constraint(expr= - m.x51 + 50*m.b85 - 50*m.b88 + m.x265 >= -50)

m.c435 = Constraint(expr= - m.x62 + 50*m.b86 - 50*m.b89 + m.x266 >= -50)

m.c436 = Constraint(expr= - 4*m.b87 + m.x264 <= 46)

m.c437 = Constraint(expr= - 4*m.b88 + m.x265 <= 46)

m.c438 = Constraint(expr= - 4*m.b89 + m.x266 <= 46)

m.c439 = Constraint(expr=   46*m.b87 + m.x264 >= 46)

m.c440 = Constraint(expr=   46*m.b88 + m.x265 >= 46)

m.c441 = Constraint(expr=   46*m.b89 + m.x266 >= 46)

m.c442 = Constraint(expr=   m.x35 - m.x43 - m.x44 - m.x45 >= 0)

m.c443 = Constraint(expr=   m.x46 - m.x54 - m.x55 - m.x56 >= 0)

m.c444 = Constraint(expr=   m.x57 - m.x65 - m.x66 - m.x67 >= 0)

m.c445 = Constraint(expr= - m.x39 - 25*m.b69 <= -95)

m.c446 = Constraint(expr= - m.x50 - 25*m.b70 <= -95)

m.c447 = Constraint(expr= - m.x61 - 25*m.b71 <= -95)

m.c448 = Constraint(expr=   m.x39 + 5*m.b69 <= 100)

m.c449 = Constraint(expr=   m.x50 + 5*m.b70 <= 100)

m.c450 = Constraint(expr=   m.x61 + 5*m.b71 <= 100)

m.c451 = Constraint(expr= - m.x40 - 10*m.b72 <= -10)

m.c452 = Constraint(expr= - m.x51 - 10*m.b73 <= -10)

m.c453 = Constraint(expr= - m.x62 - 10*m.b74 <= -10)

m.c454 = Constraint(expr=   m.x40 + 40*m.b72 <= 50)

m.c455 = Constraint(expr=   m.x51 + 40*m.b73 <= 50)

m.c456 = Constraint(expr=   m.x62 + 40*m.b74 <= 50)

m.c457 = Constraint(expr= - m.x38 - 3*m.b75 <= -33)

m.c458 = Constraint(expr= - m.x49 - 3*m.b76 <= -33)

m.c459 = Constraint(expr= - m.x60 - 3*m.b77 <= -33)

m.c460 = Constraint(expr=   m.x38 + 37*m.b75 <= 70)

m.c461 = Constraint(expr=   m.x49 + 37*m.b76 <= 70)

m.c462 = Constraint(expr=   m.x60 + 37*m.b77 <= 70)

m.c463 = Constraint(expr= - m.x38 - 35.52*m.b78 <= -65.52)

m.c464 = Constraint(expr= - m.x49 - 35.52*m.b79 <= -65.52)

m.c465 = Constraint(expr= - m.x60 - 35.52*m.b80 <= -65.52)

m.c466 = Constraint(expr=   m.x38 + 4.48*m.b78 <= 70)

m.c467 = Constraint(expr=   m.x49 + 4.48*m.b79 <= 70)

m.c468 = Constraint(expr=   m.x60 + 4.48*m.b80 <= 70)

m.c469 = Constraint(expr= - m.x39 - 2*m.b81 <= -72)

m.c470 = Constraint(expr= - m.x50 - 2*m.b82 <= -72)

m.c471 = Constraint(expr= - m.x61 - 2*m.b83 <= -72)

m.c472 = Constraint(expr=   m.x39 + 28*m.b81 <= 100)

m.c473 = Constraint(expr=   m.x50 + 28*m.b82 <= 100)

m.c474 = Constraint(expr=   m.x61 + 28*m.b83 <= 100)

m.c475 = Constraint(expr= - m.x40 - 18*m.b84 <= -18)

m.c476 = Constraint(expr= - m.x51 - 18*m.b85 <= -18)

m.c477 = Constraint(expr= - m.x62 - 18*m.b86 <= -18)

m.c478 = Constraint(expr=   m.x40 + 32*m.b84 <= 50)

m.c479 = Constraint(expr=   m.x51 + 32*m.b85 <= 50)

m.c480 = Constraint(expr=   m.x62 + 32*m.b86 <= 50)

m.c481 = Constraint(expr= - m.x40 - 46*m.b87 <= -46)

m.c482 = Constraint(expr= - m.x51 - 46*m.b88 <= -46)

m.c483 = Constraint(expr= - m.x62 - 46*m.b89 <= -46)

m.c484 = Constraint(expr=   m.x40 + 4*m.b87 <= 50)

m.c485 = Constraint(expr=   m.x51 + 4*m.b88 <= 50)

m.c486 = Constraint(expr=   m.x62 + 4*m.b89 <= 50)

m.c487 = Constraint(expr=   0.385*m.x40 - 5*m.b90 <= 14.25)

m.c488 = Constraint(expr=   0.385*m.x51 - 5*m.b91 <= 14.25)

m.c489 = Constraint(expr=   0.385*m.x62 - 5*m.b92 <= 14.25)

m.c490 = Constraint(expr=   0.385*m.x40 - 14.25*m.b90 >= 0)

m.c491 = Constraint(expr=   0.385*m.x51 - 14.25*m.b91 >= 0)

m.c492 = Constraint(expr=   0.385*m.x62 - 14.25*m.b92 >= 0)

m.c493 = Constraint(expr= - m.x36 - 10*m.b96 <= -10)

m.c494 = Constraint(expr= - m.x47 - 10*m.b97 <= -10)

m.c495 = Constraint(expr= - m.x58 - 10*m.b98 <= -10)

m.c496 = Constraint(expr=   m.x36 + 120*m.b96 <= 130)

m.c497 = Constraint(expr=   m.x47 + 190*m.b97 <= 200)

m.c498 = Constraint(expr=   m.x58 + 240*m.b98 <= 250)

m.c499 = Constraint(expr= - m.x36 - 450*m.b99 <= -450)

m.c500 = Constraint(expr= - m.x47 - 450*m.b100 <= -450)

m.c501 = Constraint(expr= - m.x58 - 450*m.b101 <= -450)

m.c502 = Constraint(expr=   m.x36 - 320*m.b99 <= 130)

m.c503 = Constraint(expr=   m.x47 - 250*m.b100 <= 200)

m.c504 = Constraint(expr=   m.x58 - 200*m.b101 <= 250)

m.c505 = Constraint(expr= - m.b84 + m.b102 == 0)

m.c506 = Constraint(expr= - m.b85 + m.b103 == 0)

m.c507 = Constraint(expr= - m.b86 + m.b104 == 0)

m.c508 = Constraint(expr= - m.x40 - 36.8*m.b105 <= -36.8)

m.c509 = Constraint(expr= - m.x51 - 36.8*m.b106 <= -36.8)

m.c510 = Constraint(expr= - m.x62 - 36.8*m.b107 <= -36.8)

m.c511 = Constraint(expr=   m.x40 + 13.2*m.b105 <= 50)

m.c512 = Constraint(expr=   m.x51 + 13.2*m.b106 <= 50)

m.c513 = Constraint(expr=   m.x62 + 13.2*m.b107 <= 50)

m.c514 = Constraint(expr= - m.x42 - 3.77*m.b108 <= -3.77)

m.c515 = Constraint(expr= - m.x53 - 3.77*m.b109 <= -3.77)

m.c516 = Constraint(expr= - m.x64 - 3.77*m.b110 <= -3.77)

m.c517 = Constraint(expr=   m.x42 + 21.23*m.b108 <= 25)

m.c518 = Constraint(expr=   m.x53 + 21.23*m.b109 <= 25)

m.c519 = Constraint(expr=   m.x64 + 21.23*m.b110 <= 25)

m.c520 = Constraint(expr= - m.x42 - 19*m.b111 <= -19)

m.c521 = Constraint(expr= - m.x53 - 19*m.b112 <= -19)

m.c522 = Constraint(expr= - m.x64 - 19*m.b113 <= -19)

m.c523 = Constraint(expr=   m.x42 + 6*m.b111 <= 25)

m.c524 = Constraint(expr=   m.x53 + 6*m.b112 <= 25)

m.c525 = Constraint(expr=   m.x64 + 6*m.b113 <= 25)
