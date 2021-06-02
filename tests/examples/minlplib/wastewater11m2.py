#  NLP written by GAMS Convert at 04/21/18 13:55:06
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        252      244        0        8        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        304      304        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1105      881      224        0
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

m.obj = Objective(expr=   m.x98 + m.x99 + m.x100 + m.x101 + m.x102 + m.x103 + m.x104, sense=minimize)

m.c2 = Constraint(expr= - m.x50 - m.x62 - m.x63 - m.x64 - m.x65 - m.x66 - m.x67 - m.x68 == -80)

m.c3 = Constraint(expr= - m.x51 - m.x69 - m.x70 - m.x71 - m.x72 - m.x73 - m.x74 - m.x75 == -450)

m.c4 = Constraint(expr= - m.x52 - m.x76 - m.x77 - m.x78 - m.x79 - m.x80 - m.x81 - m.x82 == -230)

m.c5 = Constraint(expr= - m.x53 - m.x83 - m.x84 - m.x85 - m.x86 - m.x87 - m.x88 - m.x89 == -90)

m.c6 = Constraint(expr= - m.x54 - m.x90 - m.x91 - m.x92 - m.x93 - m.x94 - m.x95 - m.x96 == -330)

m.c7 = Constraint(expr= - m.x1 - m.x8 - m.x15 - m.x22 - m.x29 - m.x36 - m.x43 - m.x62 - m.x69 - m.x76 - m.x83 - m.x90
                        + m.x98 == 0)

m.c8 = Constraint(expr= - m.x2 - m.x9 - m.x16 - m.x23 - m.x30 - m.x37 - m.x44 - m.x63 - m.x70 - m.x77 - m.x84 - m.x91
                        + m.x99 == 0)

m.c9 = Constraint(expr= - m.x3 - m.x10 - m.x17 - m.x24 - m.x31 - m.x38 - m.x45 - m.x64 - m.x71 - m.x78 - m.x85 - m.x92
                        + m.x100 == 0)

m.c10 = Constraint(expr= - m.x4 - m.x11 - m.x18 - m.x25 - m.x32 - m.x39 - m.x46 - m.x65 - m.x72 - m.x79 - m.x86 - m.x93
                         + m.x101 == 0)

m.c11 = Constraint(expr= - m.x5 - m.x12 - m.x19 - m.x26 - m.x33 - m.x40 - m.x47 - m.x66 - m.x73 - m.x80 - m.x87 - m.x94
                         + m.x102 == 0)

m.c12 = Constraint(expr= - m.x6 - m.x13 - m.x20 - m.x27 - m.x34 - m.x41 - m.x48 - m.x67 - m.x74 - m.x81 - m.x88 - m.x95
                         + m.x103 == 0)

m.c13 = Constraint(expr= - m.x7 - m.x14 - m.x21 - m.x28 - m.x35 - m.x42 - m.x49 - m.x68 - m.x75 - m.x82 - m.x89 - m.x96
                         + m.x104 == 0)

m.c14 = Constraint(expr= - m.x1 - m.x2 - m.x3 - m.x4 - m.x5 - m.x6 - m.x7 - m.x55 + m.x98 == 0)

m.c15 = Constraint(expr= - m.x8 - m.x9 - m.x10 - m.x11 - m.x12 - m.x13 - m.x14 - m.x56 + m.x99 == 0)

m.c16 = Constraint(expr= - m.x15 - m.x16 - m.x17 - m.x18 - m.x19 - m.x20 - m.x21 - m.x57 + m.x100 == 0)

m.c17 = Constraint(expr= - m.x22 - m.x23 - m.x24 - m.x25 - m.x26 - m.x27 - m.x28 - m.x58 + m.x101 == 0)

m.c18 = Constraint(expr= - m.x29 - m.x30 - m.x31 - m.x32 - m.x33 - m.x34 - m.x35 - m.x59 + m.x102 == 0)

m.c19 = Constraint(expr= - m.x36 - m.x37 - m.x38 - m.x39 - m.x40 - m.x41 - m.x42 - m.x60 + m.x103 == 0)

m.c20 = Constraint(expr= - m.x43 - m.x44 - m.x45 - m.x46 - m.x47 - m.x48 - m.x49 - m.x61 + m.x104 == 0)

m.c21 = Constraint(expr= - m.x50 - m.x51 - m.x52 - m.x53 - m.x54 - m.x55 - m.x56 - m.x57 - m.x58 - m.x59 - m.x60 - m.x61
                         + m.x97 == 0)

m.c22 = Constraint(expr= - m.x154 - m.x166 - m.x167 - m.x168 - m.x169 - m.x170 - m.x171 - m.x172 == -960)

m.c23 = Constraint(expr= - m.x155 - m.x173 - m.x174 - m.x175 - m.x176 - m.x177 - m.x178 - m.x179 == -22500)

m.c24 = Constraint(expr= - m.x156 - m.x180 - m.x181 - m.x182 - m.x183 - m.x184 - m.x185 - m.x186 == -115000)

m.c25 = Constraint(expr= - m.x157 - m.x187 - m.x188 - m.x189 - m.x190 - m.x191 - m.x192 - m.x193 == -36000)

m.c26 = Constraint(expr= - m.x158 - m.x194 - m.x195 - m.x196 - m.x197 - m.x198 - m.x199 - m.x200 == -39600)

m.c27 = Constraint(expr= - m.x166 + 960*m.x269 == 0)

m.c28 = Constraint(expr= - m.x167 + 960*m.x270 == 0)

m.c29 = Constraint(expr= - m.x168 + 960*m.x271 == 0)

m.c30 = Constraint(expr= - m.x169 + 960*m.x272 == 0)

m.c31 = Constraint(expr= - m.x170 + 960*m.x273 == 0)

m.c32 = Constraint(expr= - m.x171 + 960*m.x274 == 0)

m.c33 = Constraint(expr= - m.x172 + 960*m.x275 == 0)

m.c34 = Constraint(expr= - m.x173 + 22500*m.x276 == 0)

m.c35 = Constraint(expr= - m.x174 + 22500*m.x277 == 0)

m.c36 = Constraint(expr= - m.x175 + 22500*m.x278 == 0)

m.c37 = Constraint(expr= - m.x176 + 22500*m.x279 == 0)

m.c38 = Constraint(expr= - m.x177 + 22500*m.x280 == 0)

m.c39 = Constraint(expr= - m.x178 + 22500*m.x281 == 0)

m.c40 = Constraint(expr= - m.x179 + 22500*m.x282 == 0)

m.c41 = Constraint(expr= - m.x180 + 115000*m.x283 == 0)

m.c42 = Constraint(expr= - m.x181 + 115000*m.x284 == 0)

m.c43 = Constraint(expr= - m.x182 + 115000*m.x285 == 0)

m.c44 = Constraint(expr= - m.x183 + 115000*m.x286 == 0)

m.c45 = Constraint(expr= - m.x184 + 115000*m.x287 == 0)

m.c46 = Constraint(expr= - m.x185 + 115000*m.x288 == 0)

m.c47 = Constraint(expr= - m.x186 + 115000*m.x289 == 0)

m.c48 = Constraint(expr= - m.x187 + 36000*m.x290 == 0)

m.c49 = Constraint(expr= - m.x188 + 36000*m.x291 == 0)

m.c50 = Constraint(expr= - m.x189 + 36000*m.x292 == 0)

m.c51 = Constraint(expr= - m.x190 + 36000*m.x293 == 0)

m.c52 = Constraint(expr= - m.x191 + 36000*m.x294 == 0)

m.c53 = Constraint(expr= - m.x192 + 36000*m.x295 == 0)

m.c54 = Constraint(expr= - m.x193 + 36000*m.x296 == 0)

m.c55 = Constraint(expr= - m.x194 + 39600*m.x297 == 0)

m.c56 = Constraint(expr= - m.x195 + 39600*m.x298 == 0)

m.c57 = Constraint(expr= - m.x196 + 39600*m.x299 == 0)

m.c58 = Constraint(expr= - m.x197 + 39600*m.x300 == 0)

m.c59 = Constraint(expr= - m.x198 + 39600*m.x301 == 0)

m.c60 = Constraint(expr= - m.x199 + 39600*m.x302 == 0)

m.c61 = Constraint(expr= - m.x200 + 39600*m.x303 == 0)

m.c62 = Constraint(expr= - m.x154 + 960*m.x257 == 0)

m.c63 = Constraint(expr= - m.x155 + 22500*m.x258 == 0)

m.c64 = Constraint(expr= - m.x156 + 115000*m.x259 == 0)

m.c65 = Constraint(expr= - m.x157 + 36000*m.x260 == 0)

m.c66 = Constraint(expr= - m.x158 + 39600*m.x261 == 0)

m.c67 = Constraint(expr= - m.x62 + 80*m.x269 == 0)

m.c68 = Constraint(expr= - m.x63 + 80*m.x270 == 0)

m.c69 = Constraint(expr= - m.x64 + 80*m.x271 == 0)

m.c70 = Constraint(expr= - m.x65 + 80*m.x272 == 0)

m.c71 = Constraint(expr= - m.x66 + 80*m.x273 == 0)

m.c72 = Constraint(expr= - m.x67 + 80*m.x274 == 0)

m.c73 = Constraint(expr= - m.x68 + 80*m.x275 == 0)

m.c74 = Constraint(expr= - m.x69 + 450*m.x276 == 0)

m.c75 = Constraint(expr= - m.x70 + 450*m.x277 == 0)

m.c76 = Constraint(expr= - m.x71 + 450*m.x278 == 0)

m.c77 = Constraint(expr= - m.x72 + 450*m.x279 == 0)

m.c78 = Constraint(expr= - m.x73 + 450*m.x280 == 0)

m.c79 = Constraint(expr= - m.x74 + 450*m.x281 == 0)

m.c80 = Constraint(expr= - m.x75 + 450*m.x282 == 0)

m.c81 = Constraint(expr= - m.x76 + 230*m.x283 == 0)

m.c82 = Constraint(expr= - m.x77 + 230*m.x284 == 0)

m.c83 = Constraint(expr= - m.x78 + 230*m.x285 == 0)

m.c84 = Constraint(expr= - m.x79 + 230*m.x286 == 0)

m.c85 = Constraint(expr= - m.x80 + 230*m.x287 == 0)

m.c86 = Constraint(expr= - m.x81 + 230*m.x288 == 0)

m.c87 = Constraint(expr= - m.x82 + 230*m.x289 == 0)

m.c88 = Constraint(expr= - m.x83 + 90*m.x290 == 0)

m.c89 = Constraint(expr= - m.x84 + 90*m.x291 == 0)

m.c90 = Constraint(expr= - m.x85 + 90*m.x292 == 0)

m.c91 = Constraint(expr= - m.x86 + 90*m.x293 == 0)

m.c92 = Constraint(expr= - m.x87 + 90*m.x294 == 0)

m.c93 = Constraint(expr= - m.x88 + 90*m.x295 == 0)

m.c94 = Constraint(expr= - m.x89 + 90*m.x296 == 0)

m.c95 = Constraint(expr= - m.x90 + 330*m.x297 == 0)

m.c96 = Constraint(expr= - m.x91 + 330*m.x298 == 0)

m.c97 = Constraint(expr= - m.x92 + 330*m.x299 == 0)

m.c98 = Constraint(expr= - m.x93 + 330*m.x300 == 0)

m.c99 = Constraint(expr= - m.x94 + 330*m.x301 == 0)

m.c100 = Constraint(expr= - m.x95 + 330*m.x302 == 0)

m.c101 = Constraint(expr= - m.x96 + 330*m.x303 == 0)

m.c102 = Constraint(expr= - m.x50 + 80*m.x257 == 0)

m.c103 = Constraint(expr= - m.x51 + 450*m.x258 == 0)

m.c104 = Constraint(expr= - m.x52 + 230*m.x259 == 0)

m.c105 = Constraint(expr= - m.x53 + 90*m.x260 == 0)

m.c106 = Constraint(expr= - m.x54 + 330*m.x261 == 0)

m.c107 = Constraint(expr=   m.x257 + m.x269 + m.x270 + m.x271 + m.x272 + m.x273 + m.x274 + m.x275 == 1)

m.c108 = Constraint(expr=   m.x258 + m.x276 + m.x277 + m.x278 + m.x279 + m.x280 + m.x281 + m.x282 == 1)

m.c109 = Constraint(expr=   m.x259 + m.x283 + m.x284 + m.x285 + m.x286 + m.x287 + m.x288 + m.x289 == 1)

m.c110 = Constraint(expr=   m.x260 + m.x290 + m.x291 + m.x292 + m.x293 + m.x294 + m.x295 + m.x296 == 1)

m.c111 = Constraint(expr=   m.x261 + m.x297 + m.x298 + m.x299 + m.x300 + m.x301 + m.x302 + m.x303 == 1)

m.c112 = Constraint(expr= - 400*m.x98 + m.x105 + m.x112 + m.x119 + m.x126 + m.x133 + m.x140 + m.x147 + m.x166 + m.x173
                          + m.x180 + m.x187 + m.x194 <= 0)

m.c113 = Constraint(expr= - 100*m.x99 + m.x106 + m.x113 + m.x120 + m.x127 + m.x134 + m.x141 + m.x148 + m.x167 + m.x174
                          + m.x181 + m.x188 + m.x195 <= 0)

m.c114 = Constraint(expr= - 50*m.x100 + m.x107 + m.x114 + m.x121 + m.x128 + m.x135 + m.x142 + m.x149 + m.x168 + m.x175
                          + m.x182 + m.x189 + m.x196 <= 0)

m.c115 = Constraint(expr= - 570*m.x101 + m.x108 + m.x115 + m.x122 + m.x129 + m.x136 + m.x143 + m.x150 + m.x169 + m.x176
                          + m.x183 + m.x190 + m.x197 <= 0)

m.c116 = Constraint(expr= - 100*m.x102 + m.x109 + m.x116 + m.x123 + m.x130 + m.x137 + m.x144 + m.x151 + m.x170 + m.x177
                          + m.x184 + m.x191 + m.x198 <= 0)

m.c117 = Constraint(expr= - 30*m.x103 + m.x110 + m.x117 + m.x124 + m.x131 + m.x138 + m.x145 + m.x152 + m.x171 + m.x178
                          + m.x185 + m.x192 + m.x199 <= 0)

m.c118 = Constraint(expr= - 640*m.x104 + m.x111 + m.x118 + m.x125 + m.x132 + m.x139 + m.x146 + m.x153 + m.x172 + m.x179
                          + m.x186 + m.x193 + m.x200 <= 0)

m.c119 = Constraint(expr=   0.9*m.x105 + 0.9*m.x112 + 0.9*m.x119 + 0.9*m.x126 + 0.9*m.x133 + 0.9*m.x140 + 0.9*m.x147
                          + 0.9*m.x166 + 0.9*m.x173 + 0.9*m.x180 + 0.9*m.x187 + 0.9*m.x194 - m.x201 == 0)

m.c120 = Constraint(expr=   0.6*m.x106 + 0.6*m.x113 + 0.6*m.x120 + 0.6*m.x127 + 0.6*m.x134 + 0.6*m.x141 + 0.6*m.x148
                          + 0.6*m.x167 + 0.6*m.x174 + 0.6*m.x181 + 0.6*m.x188 + 0.6*m.x195 - m.x202 == 0)

m.c121 = Constraint(expr=   0.15*m.x107 + 0.15*m.x114 + 0.15*m.x121 + 0.15*m.x128 + 0.15*m.x135 + 0.15*m.x142
                          + 0.15*m.x149 + 0.15*m.x168 + 0.15*m.x175 + 0.15*m.x182 + 0.15*m.x189 + 0.15*m.x196 - m.x203
                          == 0)

m.c122 = Constraint(expr=   0.26*m.x108 + 0.26*m.x115 + 0.26*m.x122 + 0.26*m.x129 + 0.26*m.x136 + 0.26*m.x143
                          + 0.26*m.x150 + 0.26*m.x169 + 0.26*m.x176 + 0.26*m.x183 + 0.26*m.x190 + 0.26*m.x197 - m.x204
                          == 0)

m.c123 = Constraint(expr=   0.1*m.x109 + 0.1*m.x116 + 0.1*m.x123 + 0.1*m.x130 + 0.1*m.x137 + 0.1*m.x144 + 0.1*m.x151
                          + 0.1*m.x170 + 0.1*m.x177 + 0.1*m.x184 + 0.1*m.x191 + 0.1*m.x198 - m.x205 == 0)

m.c124 = Constraint(expr=   0.4*m.x110 + 0.4*m.x117 + 0.4*m.x124 + 0.4*m.x131 + 0.4*m.x138 + 0.4*m.x145 + 0.4*m.x152
                          + 0.4*m.x171 + 0.4*m.x178 + 0.4*m.x185 + 0.4*m.x192 + 0.4*m.x199 - m.x206 == 0)

m.c125 = Constraint(expr=   0.3*m.x111 + 0.3*m.x118 + 0.3*m.x125 + 0.3*m.x132 + 0.3*m.x139 + 0.3*m.x146 + 0.3*m.x153
                          + 0.3*m.x172 + 0.3*m.x179 + 0.3*m.x186 + 0.3*m.x193 + 0.3*m.x200 - m.x207 == 0)

m.c126 = Constraint(expr= - m.x105 - m.x106 - m.x107 - m.x108 - m.x109 - m.x110 - m.x111 - m.x159 + m.x201 == 0)

m.c127 = Constraint(expr= - m.x112 - m.x113 - m.x114 - m.x115 - m.x116 - m.x117 - m.x118 - m.x160 + m.x202 == 0)

m.c128 = Constraint(expr= - m.x119 - m.x120 - m.x121 - m.x122 - m.x123 - m.x124 - m.x125 - m.x161 + m.x203 == 0)

m.c129 = Constraint(expr= - m.x126 - m.x127 - m.x128 - m.x129 - m.x130 - m.x131 - m.x132 - m.x162 + m.x204 == 0)

m.c130 = Constraint(expr= - m.x133 - m.x134 - m.x135 - m.x136 - m.x137 - m.x138 - m.x139 - m.x163 + m.x205 == 0)

m.c131 = Constraint(expr= - m.x140 - m.x141 - m.x142 - m.x143 - m.x144 - m.x145 - m.x146 - m.x164 + m.x206 == 0)

m.c132 = Constraint(expr= - m.x147 - m.x148 - m.x149 - m.x150 - m.x151 - m.x152 - m.x153 - m.x165 + m.x207 == 0)

m.c133 = Constraint(expr=m.x201*m.x208 - m.x105 == 0)

m.c134 = Constraint(expr=m.x201*m.x209 - m.x106 == 0)

m.c135 = Constraint(expr=m.x201*m.x210 - m.x107 == 0)

m.c136 = Constraint(expr=m.x201*m.x211 - m.x108 == 0)

m.c137 = Constraint(expr=m.x201*m.x212 - m.x109 == 0)

m.c138 = Constraint(expr=m.x201*m.x213 - m.x110 == 0)

m.c139 = Constraint(expr=m.x201*m.x214 - m.x111 == 0)

m.c140 = Constraint(expr=m.x202*m.x215 - m.x112 == 0)

m.c141 = Constraint(expr=m.x202*m.x216 - m.x113 == 0)

m.c142 = Constraint(expr=m.x202*m.x217 - m.x114 == 0)

m.c143 = Constraint(expr=m.x202*m.x218 - m.x115 == 0)

m.c144 = Constraint(expr=m.x202*m.x219 - m.x116 == 0)

m.c145 = Constraint(expr=m.x202*m.x220 - m.x117 == 0)

m.c146 = Constraint(expr=m.x202*m.x221 - m.x118 == 0)

m.c147 = Constraint(expr=m.x203*m.x222 - m.x119 == 0)

m.c148 = Constraint(expr=m.x203*m.x223 - m.x120 == 0)

m.c149 = Constraint(expr=m.x203*m.x224 - m.x121 == 0)

m.c150 = Constraint(expr=m.x203*m.x225 - m.x122 == 0)

m.c151 = Constraint(expr=m.x203*m.x226 - m.x123 == 0)

m.c152 = Constraint(expr=m.x203*m.x227 - m.x124 == 0)

m.c153 = Constraint(expr=m.x203*m.x228 - m.x125 == 0)

m.c154 = Constraint(expr=m.x204*m.x229 - m.x126 == 0)

m.c155 = Constraint(expr=m.x204*m.x230 - m.x127 == 0)

m.c156 = Constraint(expr=m.x204*m.x231 - m.x128 == 0)

m.c157 = Constraint(expr=m.x204*m.x232 - m.x129 == 0)

m.c158 = Constraint(expr=m.x204*m.x233 - m.x130 == 0)

m.c159 = Constraint(expr=m.x204*m.x234 - m.x131 == 0)

m.c160 = Constraint(expr=m.x204*m.x235 - m.x132 == 0)

m.c161 = Constraint(expr=m.x205*m.x236 - m.x133 == 0)

m.c162 = Constraint(expr=m.x205*m.x237 - m.x134 == 0)

m.c163 = Constraint(expr=m.x205*m.x238 - m.x135 == 0)

m.c164 = Constraint(expr=m.x205*m.x239 - m.x136 == 0)

m.c165 = Constraint(expr=m.x205*m.x240 - m.x137 == 0)

m.c166 = Constraint(expr=m.x205*m.x241 - m.x138 == 0)

m.c167 = Constraint(expr=m.x205*m.x242 - m.x139 == 0)

m.c168 = Constraint(expr=m.x206*m.x243 - m.x140 == 0)

m.c169 = Constraint(expr=m.x206*m.x244 - m.x141 == 0)

m.c170 = Constraint(expr=m.x206*m.x245 - m.x142 == 0)

m.c171 = Constraint(expr=m.x206*m.x246 - m.x143 == 0)

m.c172 = Constraint(expr=m.x206*m.x247 - m.x144 == 0)

m.c173 = Constraint(expr=m.x206*m.x248 - m.x145 == 0)

m.c174 = Constraint(expr=m.x206*m.x249 - m.x146 == 0)

m.c175 = Constraint(expr=m.x207*m.x250 - m.x147 == 0)

m.c176 = Constraint(expr=m.x207*m.x251 - m.x148 == 0)

m.c177 = Constraint(expr=m.x207*m.x252 - m.x149 == 0)

m.c178 = Constraint(expr=m.x207*m.x253 - m.x150 == 0)

m.c179 = Constraint(expr=m.x207*m.x254 - m.x151 == 0)

m.c180 = Constraint(expr=m.x207*m.x255 - m.x152 == 0)

m.c181 = Constraint(expr=m.x207*m.x256 - m.x153 == 0)

m.c182 = Constraint(expr=m.x201*m.x262 - m.x159 == 0)

m.c183 = Constraint(expr=m.x202*m.x263 - m.x160 == 0)

m.c184 = Constraint(expr=m.x203*m.x264 - m.x161 == 0)

m.c185 = Constraint(expr=m.x204*m.x265 - m.x162 == 0)

m.c186 = Constraint(expr=m.x205*m.x266 - m.x163 == 0)

m.c187 = Constraint(expr=m.x206*m.x267 - m.x164 == 0)

m.c188 = Constraint(expr=m.x207*m.x268 - m.x165 == 0)

m.c189 = Constraint(expr=m.x98*m.x208 - m.x1 == 0)

m.c190 = Constraint(expr=m.x98*m.x209 - m.x2 == 0)

m.c191 = Constraint(expr=m.x98*m.x210 - m.x3 == 0)

m.c192 = Constraint(expr=m.x98*m.x211 - m.x4 == 0)

m.c193 = Constraint(expr=m.x98*m.x212 - m.x5 == 0)

m.c194 = Constraint(expr=m.x98*m.x213 - m.x6 == 0)

m.c195 = Constraint(expr=m.x98*m.x214 - m.x7 == 0)

m.c196 = Constraint(expr=m.x99*m.x215 - m.x8 == 0)

m.c197 = Constraint(expr=m.x99*m.x216 - m.x9 == 0)

m.c198 = Constraint(expr=m.x99*m.x217 - m.x10 == 0)

m.c199 = Constraint(expr=m.x99*m.x218 - m.x11 == 0)

m.c200 = Constraint(expr=m.x99*m.x219 - m.x12 == 0)

m.c201 = Constraint(expr=m.x99*m.x220 - m.x13 == 0)

m.c202 = Constraint(expr=m.x99*m.x221 - m.x14 == 0)

m.c203 = Constraint(expr=m.x100*m.x222 - m.x15 == 0)

m.c204 = Constraint(expr=m.x100*m.x223 - m.x16 == 0)

m.c205 = Constraint(expr=m.x100*m.x224 - m.x17 == 0)

m.c206 = Constraint(expr=m.x100*m.x225 - m.x18 == 0)

m.c207 = Constraint(expr=m.x100*m.x226 - m.x19 == 0)

m.c208 = Constraint(expr=m.x100*m.x227 - m.x20 == 0)

m.c209 = Constraint(expr=m.x100*m.x228 - m.x21 == 0)

m.c210 = Constraint(expr=m.x101*m.x229 - m.x22 == 0)

m.c211 = Constraint(expr=m.x101*m.x230 - m.x23 == 0)

m.c212 = Constraint(expr=m.x101*m.x231 - m.x24 == 0)

m.c213 = Constraint(expr=m.x101*m.x232 - m.x25 == 0)

m.c214 = Constraint(expr=m.x101*m.x233 - m.x26 == 0)

m.c215 = Constraint(expr=m.x101*m.x234 - m.x27 == 0)

m.c216 = Constraint(expr=m.x101*m.x235 - m.x28 == 0)

m.c217 = Constraint(expr=m.x102*m.x236 - m.x29 == 0)

m.c218 = Constraint(expr=m.x102*m.x237 - m.x30 == 0)

m.c219 = Constraint(expr=m.x102*m.x238 - m.x31 == 0)

m.c220 = Constraint(expr=m.x102*m.x239 - m.x32 == 0)

m.c221 = Constraint(expr=m.x102*m.x240 - m.x33 == 0)

m.c222 = Constraint(expr=m.x102*m.x241 - m.x34 == 0)

m.c223 = Constraint(expr=m.x102*m.x242 - m.x35 == 0)

m.c224 = Constraint(expr=m.x103*m.x243 - m.x36 == 0)

m.c225 = Constraint(expr=m.x103*m.x244 - m.x37 == 0)

m.c226 = Constraint(expr=m.x103*m.x245 - m.x38 == 0)

m.c227 = Constraint(expr=m.x103*m.x246 - m.x39 == 0)

m.c228 = Constraint(expr=m.x103*m.x247 - m.x40 == 0)

m.c229 = Constraint(expr=m.x103*m.x248 - m.x41 == 0)

m.c230 = Constraint(expr=m.x103*m.x249 - m.x42 == 0)

m.c231 = Constraint(expr=m.x104*m.x250 - m.x43 == 0)

m.c232 = Constraint(expr=m.x104*m.x251 - m.x44 == 0)

m.c233 = Constraint(expr=m.x104*m.x252 - m.x45 == 0)

m.c234 = Constraint(expr=m.x104*m.x253 - m.x46 == 0)

m.c235 = Constraint(expr=m.x104*m.x254 - m.x47 == 0)

m.c236 = Constraint(expr=m.x104*m.x255 - m.x48 == 0)

m.c237 = Constraint(expr=m.x104*m.x256 - m.x49 == 0)

m.c238 = Constraint(expr=m.x98*m.x262 - m.x55 == 0)

m.c239 = Constraint(expr=m.x99*m.x263 - m.x56 == 0)

m.c240 = Constraint(expr=m.x100*m.x264 - m.x57 == 0)

m.c241 = Constraint(expr=m.x101*m.x265 - m.x58 == 0)

m.c242 = Constraint(expr=m.x102*m.x266 - m.x59 == 0)

m.c243 = Constraint(expr=m.x103*m.x267 - m.x60 == 0)

m.c244 = Constraint(expr=m.x104*m.x268 - m.x61 == 0)

m.c245 = Constraint(expr=   m.x208 + m.x209 + m.x210 + m.x211 + m.x212 + m.x213 + m.x214 + m.x262 == 1)

m.c246 = Constraint(expr=   m.x215 + m.x216 + m.x217 + m.x218 + m.x219 + m.x220 + m.x221 + m.x263 == 1)

m.c247 = Constraint(expr=   m.x222 + m.x223 + m.x224 + m.x225 + m.x226 + m.x227 + m.x228 + m.x264 == 1)

m.c248 = Constraint(expr=   m.x229 + m.x230 + m.x231 + m.x232 + m.x233 + m.x234 + m.x235 + m.x265 == 1)

m.c249 = Constraint(expr=   m.x236 + m.x237 + m.x238 + m.x239 + m.x240 + m.x241 + m.x242 + m.x266 == 1)

m.c250 = Constraint(expr=   m.x243 + m.x244 + m.x245 + m.x246 + m.x247 + m.x248 + m.x249 + m.x267 == 1)

m.c251 = Constraint(expr=   m.x250 + m.x251 + m.x252 + m.x253 + m.x254 + m.x255 + m.x256 + m.x268 == 1)

m.c252 = Constraint(expr= - 4*m.x97 + m.x154 + m.x155 + m.x156 + m.x157 + m.x158 + m.x159 + m.x160 + m.x161 + m.x162
                          + m.x163 + m.x164 + m.x165 <= 0)
