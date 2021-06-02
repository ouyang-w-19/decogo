#  NLP written by GAMS Convert at 04/21/18 13:55:06
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         84       68        0       16        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        383      383        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1371      861      510        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x235 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x255 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x258 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x262 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x263 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x264 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x265 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x266 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x267 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x268 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x269 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x270 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x271 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x272 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x273 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x274 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x275 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x276 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x277 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x278 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x279 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x280 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x281 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x282 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x283 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x284 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x285 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x286 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x287 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x289 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x290 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x291 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x292 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x293 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x294 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x295 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x296 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x297 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x298 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x299 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x300 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x301 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x302 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x303 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x304 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x305 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x306 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x307 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x309 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x311 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x312 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x313 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x314 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x315 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x316 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x317 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x318 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x319 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x320 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x321 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x322 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x323 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x324 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x325 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x326 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x327 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x328 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x329 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x330 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x331 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x332 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x333 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x334 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x335 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x336 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x337 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x338 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x339 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x340 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x341 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x342 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x343 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x344 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x345 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x346 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x347 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x348 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x349 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x350 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x351 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x352 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x353 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x354 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x355 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x356 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x357 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x358 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x359 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x360 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x361 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x362 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x363 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x364 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x365 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x366 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x367 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x368 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x369 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x370 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x371 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x372 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x373 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x374 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x375 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x376 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x377 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x378 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x379 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x380 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x381 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x382 = Var(within=Reals,bounds=(0,1000000),initialize=0)

m.obj = Objective(expr=   m.x368 + m.x369 + m.x370 + m.x371 + m.x372 + m.x373 + m.x374 + m.x375 + m.x376 + m.x377
                        + m.x378 + m.x379 + m.x380 + m.x381 + m.x382, sense=minimize)

m.c2 = Constraint(expr= - m.x256 - m.x277 - m.x278 - m.x279 - m.x280 - m.x281 - m.x282 - m.x283 - m.x284 - m.x285
                        - m.x286 - m.x287 - m.x288 - m.x289 - m.x290 - m.x291 == -90)

m.c3 = Constraint(expr= - m.x257 - m.x292 - m.x293 - m.x294 - m.x295 - m.x296 - m.x297 - m.x298 - m.x299 - m.x300
                        - m.x301 - m.x302 - m.x303 - m.x304 - m.x305 - m.x306 == -50)

m.c4 = Constraint(expr= - m.x258 - m.x307 - m.x308 - m.x309 - m.x310 - m.x311 - m.x312 - m.x313 - m.x314 - m.x315
                        - m.x316 - m.x317 - m.x318 - m.x319 - m.x320 - m.x321 == -200)

m.c5 = Constraint(expr= - m.x259 - m.x322 - m.x323 - m.x324 - m.x325 - m.x326 - m.x327 - m.x328 - m.x329 - m.x330
                        - m.x331 - m.x332 - m.x333 - m.x334 - m.x335 - m.x336 == -240)

m.c6 = Constraint(expr= - m.x260 - m.x337 - m.x338 - m.x339 - m.x340 - m.x341 - m.x342 - m.x343 - m.x344 - m.x345
                        - m.x346 - m.x347 - m.x348 - m.x349 - m.x350 - m.x351 == -530)

m.c7 = Constraint(expr= - m.x261 - m.x352 - m.x353 - m.x354 - m.x355 - m.x356 - m.x357 - m.x358 - m.x359 - m.x360
                        - m.x361 - m.x362 - m.x363 - m.x364 - m.x365 - m.x366 == -70)

m.c8 = Constraint(expr= - m.x31 - m.x46 - m.x61 - m.x76 - m.x91 - m.x106 - m.x121 - m.x136 - m.x151 - m.x166 - m.x181
                        - m.x196 - m.x211 - m.x226 - m.x241 - m.x277 - m.x292 - m.x307 - m.x322 - m.x337 - m.x352
                        + m.x368 == 0)

m.c9 = Constraint(expr= - m.x32 - m.x47 - m.x62 - m.x77 - m.x92 - m.x107 - m.x122 - m.x137 - m.x152 - m.x167 - m.x182
                        - m.x197 - m.x212 - m.x227 - m.x242 - m.x278 - m.x293 - m.x308 - m.x323 - m.x338 - m.x353
                        + m.x369 == 0)

m.c10 = Constraint(expr= - m.x33 - m.x48 - m.x63 - m.x78 - m.x93 - m.x108 - m.x123 - m.x138 - m.x153 - m.x168 - m.x183
                         - m.x198 - m.x213 - m.x228 - m.x243 - m.x279 - m.x294 - m.x309 - m.x324 - m.x339 - m.x354
                         + m.x370 == 0)

m.c11 = Constraint(expr= - m.x34 - m.x49 - m.x64 - m.x79 - m.x94 - m.x109 - m.x124 - m.x139 - m.x154 - m.x169 - m.x184
                         - m.x199 - m.x214 - m.x229 - m.x244 - m.x280 - m.x295 - m.x310 - m.x325 - m.x340 - m.x355
                         + m.x371 == 0)

m.c12 = Constraint(expr= - m.x35 - m.x50 - m.x65 - m.x80 - m.x95 - m.x110 - m.x125 - m.x140 - m.x155 - m.x170 - m.x185
                         - m.x200 - m.x215 - m.x230 - m.x245 - m.x281 - m.x296 - m.x311 - m.x326 - m.x341 - m.x356
                         + m.x372 == 0)

m.c13 = Constraint(expr= - m.x36 - m.x51 - m.x66 - m.x81 - m.x96 - m.x111 - m.x126 - m.x141 - m.x156 - m.x171 - m.x186
                         - m.x201 - m.x216 - m.x231 - m.x246 - m.x282 - m.x297 - m.x312 - m.x327 - m.x342 - m.x357
                         + m.x373 == 0)

m.c14 = Constraint(expr= - m.x37 - m.x52 - m.x67 - m.x82 - m.x97 - m.x112 - m.x127 - m.x142 - m.x157 - m.x172 - m.x187
                         - m.x202 - m.x217 - m.x232 - m.x247 - m.x283 - m.x298 - m.x313 - m.x328 - m.x343 - m.x358
                         + m.x374 == 0)

m.c15 = Constraint(expr= - m.x38 - m.x53 - m.x68 - m.x83 - m.x98 - m.x113 - m.x128 - m.x143 - m.x158 - m.x173 - m.x188
                         - m.x203 - m.x218 - m.x233 - m.x248 - m.x284 - m.x299 - m.x314 - m.x329 - m.x344 - m.x359
                         + m.x375 == 0)

m.c16 = Constraint(expr= - m.x39 - m.x54 - m.x69 - m.x84 - m.x99 - m.x114 - m.x129 - m.x144 - m.x159 - m.x174 - m.x189
                         - m.x204 - m.x219 - m.x234 - m.x249 - m.x285 - m.x300 - m.x315 - m.x330 - m.x345 - m.x360
                         + m.x376 == 0)

m.c17 = Constraint(expr= - m.x40 - m.x55 - m.x70 - m.x85 - m.x100 - m.x115 - m.x130 - m.x145 - m.x160 - m.x175 - m.x190
                         - m.x205 - m.x220 - m.x235 - m.x250 - m.x286 - m.x301 - m.x316 - m.x331 - m.x346 - m.x361
                         + m.x377 == 0)

m.c18 = Constraint(expr= - m.x41 - m.x56 - m.x71 - m.x86 - m.x101 - m.x116 - m.x131 - m.x146 - m.x161 - m.x176 - m.x191
                         - m.x206 - m.x221 - m.x236 - m.x251 - m.x287 - m.x302 - m.x317 - m.x332 - m.x347 - m.x362
                         + m.x378 == 0)

m.c19 = Constraint(expr= - m.x42 - m.x57 - m.x72 - m.x87 - m.x102 - m.x117 - m.x132 - m.x147 - m.x162 - m.x177 - m.x192
                         - m.x207 - m.x222 - m.x237 - m.x252 - m.x288 - m.x303 - m.x318 - m.x333 - m.x348 - m.x363
                         + m.x379 == 0)

m.c20 = Constraint(expr= - m.x43 - m.x58 - m.x73 - m.x88 - m.x103 - m.x118 - m.x133 - m.x148 - m.x163 - m.x178 - m.x193
                         - m.x208 - m.x223 - m.x238 - m.x253 - m.x289 - m.x304 - m.x319 - m.x334 - m.x349 - m.x364
                         + m.x380 == 0)

m.c21 = Constraint(expr= - m.x44 - m.x59 - m.x74 - m.x89 - m.x104 - m.x119 - m.x134 - m.x149 - m.x164 - m.x179 - m.x194
                         - m.x209 - m.x224 - m.x239 - m.x254 - m.x290 - m.x305 - m.x320 - m.x335 - m.x350 - m.x365
                         + m.x381 == 0)

m.c22 = Constraint(expr= - m.x45 - m.x60 - m.x75 - m.x90 - m.x105 - m.x120 - m.x135 - m.x150 - m.x165 - m.x180 - m.x195
                         - m.x210 - m.x225 - m.x240 - m.x255 - m.x291 - m.x306 - m.x321 - m.x336 - m.x351 - m.x366
                         + m.x382 == 0)

m.c23 = Constraint(expr= - m.x31 - m.x32 - m.x33 - m.x34 - m.x35 - m.x36 - m.x37 - m.x38 - m.x39 - m.x40 - m.x41 - m.x42
                         - m.x43 - m.x44 - m.x45 - m.x262 + m.x368 == 0)

m.c24 = Constraint(expr= - m.x46 - m.x47 - m.x48 - m.x49 - m.x50 - m.x51 - m.x52 - m.x53 - m.x54 - m.x55 - m.x56 - m.x57
                         - m.x58 - m.x59 - m.x60 - m.x263 + m.x369 == 0)

m.c25 = Constraint(expr= - m.x61 - m.x62 - m.x63 - m.x64 - m.x65 - m.x66 - m.x67 - m.x68 - m.x69 - m.x70 - m.x71 - m.x72
                         - m.x73 - m.x74 - m.x75 - m.x264 + m.x370 == 0)

m.c26 = Constraint(expr= - m.x76 - m.x77 - m.x78 - m.x79 - m.x80 - m.x81 - m.x82 - m.x83 - m.x84 - m.x85 - m.x86 - m.x87
                         - m.x88 - m.x89 - m.x90 - m.x265 + m.x371 == 0)

m.c27 = Constraint(expr= - m.x91 - m.x92 - m.x93 - m.x94 - m.x95 - m.x96 - m.x97 - m.x98 - m.x99 - m.x100 - m.x101
                         - m.x102 - m.x103 - m.x104 - m.x105 - m.x266 + m.x372 == 0)

m.c28 = Constraint(expr= - m.x106 - m.x107 - m.x108 - m.x109 - m.x110 - m.x111 - m.x112 - m.x113 - m.x114 - m.x115
                         - m.x116 - m.x117 - m.x118 - m.x119 - m.x120 - m.x267 + m.x373 == 0)

m.c29 = Constraint(expr= - m.x121 - m.x122 - m.x123 - m.x124 - m.x125 - m.x126 - m.x127 - m.x128 - m.x129 - m.x130
                         - m.x131 - m.x132 - m.x133 - m.x134 - m.x135 - m.x268 + m.x374 == 0)

m.c30 = Constraint(expr= - m.x136 - m.x137 - m.x138 - m.x139 - m.x140 - m.x141 - m.x142 - m.x143 - m.x144 - m.x145
                         - m.x146 - m.x147 - m.x148 - m.x149 - m.x150 - m.x269 + m.x375 == 0)

m.c31 = Constraint(expr= - m.x151 - m.x152 - m.x153 - m.x154 - m.x155 - m.x156 - m.x157 - m.x158 - m.x159 - m.x160
                         - m.x161 - m.x162 - m.x163 - m.x164 - m.x165 - m.x270 + m.x376 == 0)

m.c32 = Constraint(expr= - m.x166 - m.x167 - m.x168 - m.x169 - m.x170 - m.x171 - m.x172 - m.x173 - m.x174 - m.x175
                         - m.x176 - m.x177 - m.x178 - m.x179 - m.x180 - m.x271 + m.x377 == 0)

m.c33 = Constraint(expr= - m.x181 - m.x182 - m.x183 - m.x184 - m.x185 - m.x186 - m.x187 - m.x188 - m.x189 - m.x190
                         - m.x191 - m.x192 - m.x193 - m.x194 - m.x195 - m.x272 + m.x378 == 0)

m.c34 = Constraint(expr= - m.x196 - m.x197 - m.x198 - m.x199 - m.x200 - m.x201 - m.x202 - m.x203 - m.x204 - m.x205
                         - m.x206 - m.x207 - m.x208 - m.x209 - m.x210 - m.x273 + m.x379 == 0)

m.c35 = Constraint(expr= - m.x211 - m.x212 - m.x213 - m.x214 - m.x215 - m.x216 - m.x217 - m.x218 - m.x219 - m.x220
                         - m.x221 - m.x222 - m.x223 - m.x224 - m.x225 - m.x274 + m.x380 == 0)

m.c36 = Constraint(expr= - m.x226 - m.x227 - m.x228 - m.x229 - m.x230 - m.x231 - m.x232 - m.x233 - m.x234 - m.x235
                         - m.x236 - m.x237 - m.x238 - m.x239 - m.x240 - m.x275 + m.x381 == 0)

m.c37 = Constraint(expr= - m.x241 - m.x242 - m.x243 - m.x244 - m.x245 - m.x246 - m.x247 - m.x248 - m.x249 - m.x250
                         - m.x251 - m.x252 - m.x253 - m.x254 - m.x255 - m.x276 + m.x382 == 0)

m.c38 = Constraint(expr= - m.x256 - m.x257 - m.x258 - m.x259 - m.x260 - m.x261 - m.x262 - m.x263 - m.x264 - m.x265
                         - m.x266 - m.x267 - m.x268 - m.x269 - m.x270 - m.x271 - m.x272 - m.x273 - m.x274 - m.x275
                         - m.x276 + m.x367 == 0)

m.c39 = Constraint(expr=m.x31*m.x16 + m.x46*m.x17 + m.x61*m.x18 + m.x76*m.x19 + m.x91*m.x20 + m.x106*m.x21 + m.x121*
                        m.x22 + m.x136*m.x23 + m.x151*m.x24 + m.x166*m.x25 + m.x181*m.x26 + m.x196*m.x27 + m.x211*m.x28
                         + m.x226*m.x29 + m.x241*m.x30 - m.x368*m.x1 + 12*m.x277 + 350*m.x292 + 500*m.x307 + 400*m.x322
                         + 50*m.x337 + 140*m.x352 == 0)

m.c40 = Constraint(expr=m.x32*m.x16 + m.x47*m.x17 + m.x62*m.x18 + m.x77*m.x19 + m.x92*m.x20 + m.x107*m.x21 + m.x122*
                        m.x22 + m.x137*m.x23 + m.x152*m.x24 + m.x167*m.x25 + m.x182*m.x26 + m.x197*m.x27 + m.x212*m.x28
                         + m.x227*m.x29 + m.x242*m.x30 - m.x369*m.x2 + 12*m.x278 + 350*m.x293 + 500*m.x308 + 400*m.x323
                         + 50*m.x338 + 140*m.x353 == 0)

m.c41 = Constraint(expr=m.x33*m.x16 + m.x48*m.x17 + m.x63*m.x18 + m.x78*m.x19 + m.x93*m.x20 + m.x108*m.x21 + m.x123*
                        m.x22 + m.x138*m.x23 + m.x153*m.x24 + m.x168*m.x25 + m.x183*m.x26 + m.x198*m.x27 + m.x213*m.x28
                         + m.x228*m.x29 + m.x243*m.x30 - m.x370*m.x3 + 12*m.x279 + 350*m.x294 + 500*m.x309 + 400*m.x324
                         + 50*m.x339 + 140*m.x354 == 0)

m.c42 = Constraint(expr=m.x34*m.x16 + m.x49*m.x17 + m.x64*m.x18 + m.x79*m.x19 + m.x94*m.x20 + m.x109*m.x21 + m.x124*
                        m.x22 + m.x139*m.x23 + m.x154*m.x24 + m.x169*m.x25 + m.x184*m.x26 + m.x199*m.x27 + m.x214*m.x28
                         + m.x229*m.x29 + m.x244*m.x30 - m.x371*m.x4 + 12*m.x280 + 350*m.x295 + 500*m.x310 + 400*m.x325
                         + 50*m.x340 + 140*m.x355 == 0)

m.c43 = Constraint(expr=m.x35*m.x16 + m.x50*m.x17 + m.x65*m.x18 + m.x80*m.x19 + m.x95*m.x20 + m.x110*m.x21 + m.x125*
                        m.x22 + m.x140*m.x23 + m.x155*m.x24 + m.x170*m.x25 + m.x185*m.x26 + m.x200*m.x27 + m.x215*m.x28
                         + m.x230*m.x29 + m.x245*m.x30 - m.x372*m.x5 + 12*m.x281 + 350*m.x296 + 500*m.x311 + 400*m.x326
                         + 50*m.x341 + 140*m.x356 == 0)

m.c44 = Constraint(expr=m.x36*m.x16 + m.x51*m.x17 + m.x66*m.x18 + m.x81*m.x19 + m.x96*m.x20 + m.x111*m.x21 + m.x126*
                        m.x22 + m.x141*m.x23 + m.x156*m.x24 + m.x171*m.x25 + m.x186*m.x26 + m.x201*m.x27 + m.x216*m.x28
                         + m.x231*m.x29 + m.x246*m.x30 - m.x373*m.x6 + 12*m.x282 + 350*m.x297 + 500*m.x312 + 400*m.x327
                         + 50*m.x342 + 140*m.x357 == 0)

m.c45 = Constraint(expr=m.x37*m.x16 + m.x52*m.x17 + m.x67*m.x18 + m.x82*m.x19 + m.x97*m.x20 + m.x112*m.x21 + m.x127*
                        m.x22 + m.x142*m.x23 + m.x157*m.x24 + m.x172*m.x25 + m.x187*m.x26 + m.x202*m.x27 + m.x217*m.x28
                         + m.x232*m.x29 + m.x247*m.x30 - m.x374*m.x7 + 12*m.x283 + 350*m.x298 + 500*m.x313 + 400*m.x328
                         + 50*m.x343 + 140*m.x358 == 0)

m.c46 = Constraint(expr=m.x38*m.x16 + m.x53*m.x17 + m.x68*m.x18 + m.x83*m.x19 + m.x98*m.x20 + m.x113*m.x21 + m.x128*
                        m.x22 + m.x143*m.x23 + m.x158*m.x24 + m.x173*m.x25 + m.x188*m.x26 + m.x203*m.x27 + m.x218*m.x28
                         + m.x233*m.x29 + m.x248*m.x30 - m.x375*m.x8 + 12*m.x284 + 350*m.x299 + 500*m.x314 + 400*m.x329
                         + 50*m.x344 + 140*m.x359 == 0)

m.c47 = Constraint(expr=m.x39*m.x16 + m.x54*m.x17 + m.x69*m.x18 + m.x84*m.x19 + m.x99*m.x20 + m.x114*m.x21 + m.x129*
                        m.x22 + m.x144*m.x23 + m.x159*m.x24 + m.x174*m.x25 + m.x189*m.x26 + m.x204*m.x27 + m.x219*m.x28
                         + m.x234*m.x29 + m.x249*m.x30 - m.x376*m.x9 + 12*m.x285 + 350*m.x300 + 500*m.x315 + 400*m.x330
                         + 50*m.x345 + 140*m.x360 == 0)

m.c48 = Constraint(expr=m.x40*m.x16 + m.x55*m.x17 + m.x70*m.x18 + m.x85*m.x19 + m.x100*m.x20 + m.x115*m.x21 + m.x130*
                        m.x22 + m.x145*m.x23 + m.x160*m.x24 + m.x175*m.x25 + m.x190*m.x26 + m.x205*m.x27 + m.x220*m.x28
                         + m.x235*m.x29 + m.x250*m.x30 - m.x377*m.x10 + 12*m.x286 + 350*m.x301 + 500*m.x316 + 400*m.x331
                         + 50*m.x346 + 140*m.x361 == 0)

m.c49 = Constraint(expr=m.x41*m.x16 + m.x56*m.x17 + m.x71*m.x18 + m.x86*m.x19 + m.x101*m.x20 + m.x116*m.x21 + m.x131*
                        m.x22 + m.x146*m.x23 + m.x161*m.x24 + m.x176*m.x25 + m.x191*m.x26 + m.x206*m.x27 + m.x221*m.x28
                         + m.x236*m.x29 + m.x251*m.x30 - m.x378*m.x11 + 12*m.x287 + 350*m.x302 + 500*m.x317 + 400*m.x332
                         + 50*m.x347 + 140*m.x362 == 0)

m.c50 = Constraint(expr=m.x42*m.x16 + m.x57*m.x17 + m.x72*m.x18 + m.x87*m.x19 + m.x102*m.x20 + m.x117*m.x21 + m.x132*
                        m.x22 + m.x147*m.x23 + m.x162*m.x24 + m.x177*m.x25 + m.x192*m.x26 + m.x207*m.x27 + m.x222*m.x28
                         + m.x237*m.x29 + m.x252*m.x30 - m.x379*m.x12 + 12*m.x288 + 350*m.x303 + 500*m.x318 + 400*m.x333
                         + 50*m.x348 + 140*m.x363 == 0)

m.c51 = Constraint(expr=m.x43*m.x16 + m.x58*m.x17 + m.x73*m.x18 + m.x88*m.x19 + m.x103*m.x20 + m.x118*m.x21 + m.x133*
                        m.x22 + m.x148*m.x23 + m.x163*m.x24 + m.x178*m.x25 + m.x193*m.x26 + m.x208*m.x27 + m.x223*m.x28
                         + m.x238*m.x29 + m.x253*m.x30 - m.x380*m.x13 + 12*m.x289 + 350*m.x304 + 500*m.x319 + 400*m.x334
                         + 50*m.x349 + 140*m.x364 == 0)

m.c52 = Constraint(expr=m.x44*m.x16 + m.x59*m.x17 + m.x74*m.x18 + m.x89*m.x19 + m.x104*m.x20 + m.x119*m.x21 + m.x134*
                        m.x22 + m.x149*m.x23 + m.x164*m.x24 + m.x179*m.x25 + m.x194*m.x26 + m.x209*m.x27 + m.x224*m.x28
                         + m.x239*m.x29 + m.x254*m.x30 - m.x381*m.x14 + 12*m.x290 + 350*m.x305 + 500*m.x320 + 400*m.x335
                         + 50*m.x350 + 140*m.x365 == 0)

m.c53 = Constraint(expr=m.x45*m.x16 + m.x60*m.x17 + m.x75*m.x18 + m.x90*m.x19 + m.x105*m.x20 + m.x120*m.x21 + m.x135*
                        m.x22 + m.x150*m.x23 + m.x165*m.x24 + m.x180*m.x25 + m.x195*m.x26 + m.x210*m.x27 + m.x225*m.x28
                         + m.x240*m.x29 + m.x255*m.x30 - m.x382*m.x15 + 12*m.x291 + 350*m.x306 + 500*m.x321 + 400*m.x336
                         + 50*m.x351 + 140*m.x366 == 0)

m.c54 = Constraint(expr=   m.x1 <= 300)

m.c55 = Constraint(expr=   m.x2 <= 10)

m.c56 = Constraint(expr=   m.x3 <= 500)

m.c57 = Constraint(expr=   m.x4 <= 570)

m.c58 = Constraint(expr=   m.x5 <= 100)

m.c59 = Constraint(expr=   m.x6 <= 300)

m.c60 = Constraint(expr=   m.x7 <= 200)

m.c61 = Constraint(expr=   m.x8 <= 47)

m.c62 = Constraint(expr=   m.x9 <= 200)

m.c63 = Constraint(expr=   m.x10 <= 250)

m.c64 = Constraint(expr=   m.x11 <= 136)

m.c65 = Constraint(expr=   m.x12 <= 50)

m.c66 = Constraint(expr=   m.x13 <= 100)

m.c67 = Constraint(expr=   m.x14 <= 270)

m.c68 = Constraint(expr=   m.x15 <= 10)

m.c69 = Constraint(expr= - 0.05*m.x1 + m.x16 == 0)

m.c70 = Constraint(expr= - 0.8*m.x2 + m.x17 == 0)

m.c71 = Constraint(expr= - 0.15*m.x3 + m.x18 == 0)

m.c72 = Constraint(expr= - 0.26*m.x4 + m.x19 == 0)

m.c73 = Constraint(expr= - 0.9*m.x5 + m.x20 == 0)

m.c74 = Constraint(expr= - 0.4*m.x6 + m.x21 == 0)

m.c75 = Constraint(expr= - 0.33*m.x7 + m.x22 == 0)

m.c76 = Constraint(expr= - 0.3*m.x8 + m.x23 == 0)

m.c77 = Constraint(expr= - 0.5*m.x9 + m.x24 == 0)

m.c78 = Constraint(expr= - 0.5*m.x10 + m.x25 == 0)

m.c79 = Constraint(expr= - 0.7*m.x11 + m.x26 == 0)

m.c80 = Constraint(expr= - 0.12*m.x12 + m.x27 == 0)

m.c81 = Constraint(expr= - 0.15*m.x13 + m.x28 == 0)

m.c82 = Constraint(expr= - 0.26*m.x14 + m.x29 == 0)

m.c83 = Constraint(expr= - 0.55*m.x15 + m.x30 == 0)

m.c84 = Constraint(expr=m.x262*m.x16 + m.x263*m.x17 + m.x264*m.x18 + m.x265*m.x19 + m.x266*m.x20 + m.x267*m.x21 + m.x268
                        *m.x22 + m.x269*m.x23 + m.x270*m.x24 + m.x271*m.x25 + m.x272*m.x26 + m.x273*m.x27 + m.x274*m.x28
                         + m.x275*m.x29 + m.x276*m.x30 + 12*m.x256 + 350*m.x257 + 500*m.x258 + 400*m.x259 + 50*m.x260
                         + 140*m.x261 - 4*m.x367 <= 0)
