#  NLP written by GAMS Convert at 04/21/18 13:54:05
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        253      253        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        308      308        0        0        0        0        0        0
#  FX      4        4        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1307      404      903        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,None),initialize=0.02)
m.x3 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0.0384)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0.0564)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0.0736)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0.09)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0.1056)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0.1204)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0.1344)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0.1476)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0.16)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0.1716)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0.1824)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0.1924)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0.2016)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0.21)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0.2176)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0.2244)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0.2304)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0.2356)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0.24)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0.2436)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0.2464)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=0.2484)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0.2496)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0.25)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0.2496)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0.2484)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0.2464)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=0.2436)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=0.24)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=0.2356)
m.x34 = Var(within=Reals,bounds=(0,None),initialize=0.2304)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=0.2244)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=0.2176)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=0.21)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=0.2016)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=0.1924)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=0.1824)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=0.1716)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0.16)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0.1476)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=0.1344)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=0.1204)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0.1056)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=0.09)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=0.0736)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0.0564)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0.0384)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=0.0196)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x55 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x56 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x57 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x58 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x59 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x60 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x61 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x62 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x63 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x64 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x65 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x66 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x67 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x68 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x69 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x70 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x71 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x72 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x73 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x74 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x75 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x76 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x77 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x78 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x79 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x80 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x81 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x82 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x83 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x84 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x85 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x86 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x87 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x88 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x89 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x90 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x91 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x92 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x93 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x94 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x95 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x96 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x97 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x98 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x99 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x100 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x101 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x102 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x103 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x104 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x105 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x156 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x157 = Var(within=Reals,bounds=(0.6,1),initialize=0.984)
m.x158 = Var(within=Reals,bounds=(0.6,1),initialize=0.976)
m.x159 = Var(within=Reals,bounds=(0.6,1),initialize=0.968)
m.x160 = Var(within=Reals,bounds=(0.6,1),initialize=0.96)
m.x161 = Var(within=Reals,bounds=(0.6,1),initialize=0.952)
m.x162 = Var(within=Reals,bounds=(0.6,1),initialize=0.944)
m.x163 = Var(within=Reals,bounds=(0.6,1),initialize=0.936)
m.x164 = Var(within=Reals,bounds=(0.6,1),initialize=0.928)
m.x165 = Var(within=Reals,bounds=(0.6,1),initialize=0.92)
m.x166 = Var(within=Reals,bounds=(0.6,1),initialize=0.912)
m.x167 = Var(within=Reals,bounds=(0.6,1),initialize=0.904)
m.x168 = Var(within=Reals,bounds=(0.6,1),initialize=0.896)
m.x169 = Var(within=Reals,bounds=(0.6,1),initialize=0.888)
m.x170 = Var(within=Reals,bounds=(0.6,1),initialize=0.88)
m.x171 = Var(within=Reals,bounds=(0.6,1),initialize=0.872)
m.x172 = Var(within=Reals,bounds=(0.6,1),initialize=0.864)
m.x173 = Var(within=Reals,bounds=(0.6,1),initialize=0.856)
m.x174 = Var(within=Reals,bounds=(0.6,1),initialize=0.848)
m.x175 = Var(within=Reals,bounds=(0.6,1),initialize=0.84)
m.x176 = Var(within=Reals,bounds=(0.6,1),initialize=0.832)
m.x177 = Var(within=Reals,bounds=(0.6,1),initialize=0.824)
m.x178 = Var(within=Reals,bounds=(0.6,1),initialize=0.816)
m.x179 = Var(within=Reals,bounds=(0.6,1),initialize=0.808)
m.x180 = Var(within=Reals,bounds=(0.6,1),initialize=0.8)
m.x181 = Var(within=Reals,bounds=(0.6,1),initialize=0.792)
m.x182 = Var(within=Reals,bounds=(0.6,1),initialize=0.784)
m.x183 = Var(within=Reals,bounds=(0.6,1),initialize=0.776)
m.x184 = Var(within=Reals,bounds=(0.6,1),initialize=0.768)
m.x185 = Var(within=Reals,bounds=(0.6,1),initialize=0.76)
m.x186 = Var(within=Reals,bounds=(0.6,1),initialize=0.752)
m.x187 = Var(within=Reals,bounds=(0.6,1),initialize=0.744)
m.x188 = Var(within=Reals,bounds=(0.6,1),initialize=0.736)
m.x189 = Var(within=Reals,bounds=(0.6,1),initialize=0.728)
m.x190 = Var(within=Reals,bounds=(0.6,1),initialize=0.72)
m.x191 = Var(within=Reals,bounds=(0.6,1),initialize=0.712)
m.x192 = Var(within=Reals,bounds=(0.6,1),initialize=0.704)
m.x193 = Var(within=Reals,bounds=(0.6,1),initialize=0.696)
m.x194 = Var(within=Reals,bounds=(0.6,1),initialize=0.688)
m.x195 = Var(within=Reals,bounds=(0.6,1),initialize=0.68)
m.x196 = Var(within=Reals,bounds=(0.6,1),initialize=0.672)
m.x197 = Var(within=Reals,bounds=(0.6,1),initialize=0.664)
m.x198 = Var(within=Reals,bounds=(0.6,1),initialize=0.656)
m.x199 = Var(within=Reals,bounds=(0.6,1),initialize=0.648)
m.x200 = Var(within=Reals,bounds=(0.6,1),initialize=0.64)
m.x201 = Var(within=Reals,bounds=(0.6,1),initialize=0.632)
m.x202 = Var(within=Reals,bounds=(0.6,1),initialize=0.624)
m.x203 = Var(within=Reals,bounds=(0.6,1),initialize=0.616)
m.x204 = Var(within=Reals,bounds=(0.6,1),initialize=0.608)
m.x205 = Var(within=Reals,bounds=(0.6,1),initialize=0.6)
m.x206 = Var(within=Reals,bounds=(0.6,0.6),initialize=0.6)
m.x207 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x208 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x209 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x210 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x211 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x212 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x213 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x214 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x215 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x216 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x217 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x218 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x219 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x220 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x221 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x222 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x223 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x224 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x225 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x226 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x227 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x228 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x229 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x230 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x231 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x232 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x233 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x234 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x235 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x236 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x237 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x238 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x239 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x240 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x241 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x242 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x243 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x244 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x245 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x246 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x247 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x248 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x249 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x250 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x251 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x252 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x253 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x254 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x255 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x256 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x257 = Var(within=Reals,bounds=(0,3.5),initialize=1.75)
m.x258 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x262 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x263 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x264 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x265 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x266 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x267 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x268 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x269 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x270 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x271 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x272 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x273 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x274 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x275 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x276 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x277 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x278 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x279 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x280 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x281 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x282 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x283 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x284 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x285 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x286 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x287 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x289 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x290 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x291 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x292 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x293 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x294 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x295 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x296 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x297 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x298 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x299 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x300 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x301 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x302 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x303 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x304 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x305 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x306 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x307 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr= - m.x104, sense=minimize)

m.c1 = Constraint(expr=-310*m.x3**2*exp(500 - 500*m.x54) + m.x258 == 0)

m.c2 = Constraint(expr=-310*m.x4**2*exp(500 - 500*m.x55) + m.x259 == 0)

m.c3 = Constraint(expr=-310*m.x5**2*exp(500 - 500*m.x56) + m.x260 == 0)

m.c4 = Constraint(expr=-310*m.x6**2*exp(500 - 500*m.x57) + m.x261 == 0)

m.c5 = Constraint(expr=-310*m.x7**2*exp(500 - 500*m.x58) + m.x262 == 0)

m.c6 = Constraint(expr=-310*m.x8**2*exp(500 - 500*m.x59) + m.x263 == 0)

m.c7 = Constraint(expr=-310*m.x9**2*exp(500 - 500*m.x60) + m.x264 == 0)

m.c8 = Constraint(expr=-310*m.x10**2*exp(500 - 500*m.x61) + m.x265 == 0)

m.c9 = Constraint(expr=-310*m.x11**2*exp(500 - 500*m.x62) + m.x266 == 0)

m.c10 = Constraint(expr=-310*m.x12**2*exp(500 - 500*m.x63) + m.x267 == 0)

m.c11 = Constraint(expr=-310*m.x13**2*exp(500 - 500*m.x64) + m.x268 == 0)

m.c12 = Constraint(expr=-310*m.x14**2*exp(500 - 500*m.x65) + m.x269 == 0)

m.c13 = Constraint(expr=-310*m.x15**2*exp(500 - 500*m.x66) + m.x270 == 0)

m.c14 = Constraint(expr=-310*m.x16**2*exp(500 - 500*m.x67) + m.x271 == 0)

m.c15 = Constraint(expr=-310*m.x17**2*exp(500 - 500*m.x68) + m.x272 == 0)

m.c16 = Constraint(expr=-310*m.x18**2*exp(500 - 500*m.x69) + m.x273 == 0)

m.c17 = Constraint(expr=-310*m.x19**2*exp(500 - 500*m.x70) + m.x274 == 0)

m.c18 = Constraint(expr=-310*m.x20**2*exp(500 - 500*m.x71) + m.x275 == 0)

m.c19 = Constraint(expr=-310*m.x21**2*exp(500 - 500*m.x72) + m.x276 == 0)

m.c20 = Constraint(expr=-310*m.x22**2*exp(500 - 500*m.x73) + m.x277 == 0)

m.c21 = Constraint(expr=-310*m.x23**2*exp(500 - 500*m.x74) + m.x278 == 0)

m.c22 = Constraint(expr=-310*m.x24**2*exp(500 - 500*m.x75) + m.x279 == 0)

m.c23 = Constraint(expr=-310*m.x25**2*exp(500 - 500*m.x76) + m.x280 == 0)

m.c24 = Constraint(expr=-310*m.x26**2*exp(500 - 500*m.x77) + m.x281 == 0)

m.c25 = Constraint(expr=-310*m.x27**2*exp(500 - 500*m.x78) + m.x282 == 0)

m.c26 = Constraint(expr=-310*m.x28**2*exp(500 - 500*m.x79) + m.x283 == 0)

m.c27 = Constraint(expr=-310*m.x29**2*exp(500 - 500*m.x80) + m.x284 == 0)

m.c28 = Constraint(expr=-310*m.x30**2*exp(500 - 500*m.x81) + m.x285 == 0)

m.c29 = Constraint(expr=-310*m.x31**2*exp(500 - 500*m.x82) + m.x286 == 0)

m.c30 = Constraint(expr=-310*m.x32**2*exp(500 - 500*m.x83) + m.x287 == 0)

m.c31 = Constraint(expr=-310*m.x33**2*exp(500 - 500*m.x84) + m.x288 == 0)

m.c32 = Constraint(expr=-310*m.x34**2*exp(500 - 500*m.x85) + m.x289 == 0)

m.c33 = Constraint(expr=-310*m.x35**2*exp(500 - 500*m.x86) + m.x290 == 0)

m.c34 = Constraint(expr=-310*m.x36**2*exp(500 - 500*m.x87) + m.x291 == 0)

m.c35 = Constraint(expr=-310*m.x37**2*exp(500 - 500*m.x88) + m.x292 == 0)

m.c36 = Constraint(expr=-310*m.x38**2*exp(500 - 500*m.x89) + m.x293 == 0)

m.c37 = Constraint(expr=-310*m.x39**2*exp(500 - 500*m.x90) + m.x294 == 0)

m.c38 = Constraint(expr=-310*m.x40**2*exp(500 - 500*m.x91) + m.x295 == 0)

m.c39 = Constraint(expr=-310*m.x41**2*exp(500 - 500*m.x92) + m.x296 == 0)

m.c40 = Constraint(expr=-310*m.x42**2*exp(500 - 500*m.x93) + m.x297 == 0)

m.c41 = Constraint(expr=-310*m.x43**2*exp(500 - 500*m.x94) + m.x298 == 0)

m.c42 = Constraint(expr=-310*m.x44**2*exp(500 - 500*m.x95) + m.x299 == 0)

m.c43 = Constraint(expr=-310*m.x45**2*exp(500 - 500*m.x96) + m.x300 == 0)

m.c44 = Constraint(expr=-310*m.x46**2*exp(500 - 500*m.x97) + m.x301 == 0)

m.c45 = Constraint(expr=-310*m.x47**2*exp(500 - 500*m.x98) + m.x302 == 0)

m.c46 = Constraint(expr=-310*m.x48**2*exp(500 - 500*m.x99) + m.x303 == 0)

m.c47 = Constraint(expr=-310*m.x49**2*exp(500 - 500*m.x100) + m.x304 == 0)

m.c48 = Constraint(expr=-310*m.x50**2*exp(500 - 500*m.x101) + m.x305 == 0)

m.c49 = Constraint(expr=-310*m.x51**2*exp(500 - 500*m.x102) + m.x306 == 0)

m.c50 = Constraint(expr=-310*m.x52**2*exp(500 - 500*m.x103) + m.x307 == 0)

m.c51 = Constraint(expr=-310*m.x53**2*exp(500 - 500*m.x104) + m.x308 == 0)

m.c52 = Constraint(expr=-(1/m.x54)**2 + m.x105 == 0)

m.c53 = Constraint(expr=-(1/m.x55)**2 + m.x106 == 0)

m.c54 = Constraint(expr=-(1/m.x56)**2 + m.x107 == 0)

m.c55 = Constraint(expr=-(1/m.x57)**2 + m.x108 == 0)

m.c56 = Constraint(expr=-(1/m.x58)**2 + m.x109 == 0)

m.c57 = Constraint(expr=-(1/m.x59)**2 + m.x110 == 0)

m.c58 = Constraint(expr=-(1/m.x60)**2 + m.x111 == 0)

m.c59 = Constraint(expr=-(1/m.x61)**2 + m.x112 == 0)

m.c60 = Constraint(expr=-(1/m.x62)**2 + m.x113 == 0)

m.c61 = Constraint(expr=-(1/m.x63)**2 + m.x114 == 0)

m.c62 = Constraint(expr=-(1/m.x64)**2 + m.x115 == 0)

m.c63 = Constraint(expr=-(1/m.x65)**2 + m.x116 == 0)

m.c64 = Constraint(expr=-(1/m.x66)**2 + m.x117 == 0)

m.c65 = Constraint(expr=-(1/m.x67)**2 + m.x118 == 0)

m.c66 = Constraint(expr=-(1/m.x68)**2 + m.x119 == 0)

m.c67 = Constraint(expr=-(1/m.x69)**2 + m.x120 == 0)

m.c68 = Constraint(expr=-(1/m.x70)**2 + m.x121 == 0)

m.c69 = Constraint(expr=-(1/m.x71)**2 + m.x122 == 0)

m.c70 = Constraint(expr=-(1/m.x72)**2 + m.x123 == 0)

m.c71 = Constraint(expr=-(1/m.x73)**2 + m.x124 == 0)

m.c72 = Constraint(expr=-(1/m.x74)**2 + m.x125 == 0)

m.c73 = Constraint(expr=-(1/m.x75)**2 + m.x126 == 0)

m.c74 = Constraint(expr=-(1/m.x76)**2 + m.x127 == 0)

m.c75 = Constraint(expr=-(1/m.x77)**2 + m.x128 == 0)

m.c76 = Constraint(expr=-(1/m.x78)**2 + m.x129 == 0)

m.c77 = Constraint(expr=-(1/m.x79)**2 + m.x130 == 0)

m.c78 = Constraint(expr=-(1/m.x80)**2 + m.x131 == 0)

m.c79 = Constraint(expr=-(1/m.x81)**2 + m.x132 == 0)

m.c80 = Constraint(expr=-(1/m.x82)**2 + m.x133 == 0)

m.c81 = Constraint(expr=-(1/m.x83)**2 + m.x134 == 0)

m.c82 = Constraint(expr=-(1/m.x84)**2 + m.x135 == 0)

m.c83 = Constraint(expr=-(1/m.x85)**2 + m.x136 == 0)

m.c84 = Constraint(expr=-(1/m.x86)**2 + m.x137 == 0)

m.c85 = Constraint(expr=-(1/m.x87)**2 + m.x138 == 0)

m.c86 = Constraint(expr=-(1/m.x88)**2 + m.x139 == 0)

m.c87 = Constraint(expr=-(1/m.x89)**2 + m.x140 == 0)

m.c88 = Constraint(expr=-(1/m.x90)**2 + m.x141 == 0)

m.c89 = Constraint(expr=-(1/m.x91)**2 + m.x142 == 0)

m.c90 = Constraint(expr=-(1/m.x92)**2 + m.x143 == 0)

m.c91 = Constraint(expr=-(1/m.x93)**2 + m.x144 == 0)

m.c92 = Constraint(expr=-(1/m.x94)**2 + m.x145 == 0)

m.c93 = Constraint(expr=-(1/m.x95)**2 + m.x146 == 0)

m.c94 = Constraint(expr=-(1/m.x96)**2 + m.x147 == 0)

m.c95 = Constraint(expr=-(1/m.x97)**2 + m.x148 == 0)

m.c96 = Constraint(expr=-(1/m.x98)**2 + m.x149 == 0)

m.c97 = Constraint(expr=-(1/m.x99)**2 + m.x150 == 0)

m.c98 = Constraint(expr=-(1/m.x100)**2 + m.x151 == 0)

m.c99 = Constraint(expr=-(1/m.x101)**2 + m.x152 == 0)

m.c100 = Constraint(expr=-(1/m.x102)**2 + m.x153 == 0)

m.c101 = Constraint(expr=-(1/m.x103)**2 + m.x154 == 0)

m.c102 = Constraint(expr=-(1/m.x104)**2 + m.x155 == 0)

m.c104 = Constraint(expr=-0.5*m.x2*(m.x3 + m.x4) - m.x54 + m.x55 == 0)

m.c105 = Constraint(expr=-0.5*m.x2*(m.x4 + m.x5) - m.x55 + m.x56 == 0)

m.c106 = Constraint(expr=-0.5*m.x2*(m.x5 + m.x6) - m.x56 + m.x57 == 0)

m.c107 = Constraint(expr=-0.5*m.x2*(m.x6 + m.x7) - m.x57 + m.x58 == 0)

m.c108 = Constraint(expr=-0.5*m.x2*(m.x7 + m.x8) - m.x58 + m.x59 == 0)

m.c109 = Constraint(expr=-0.5*m.x2*(m.x8 + m.x9) - m.x59 + m.x60 == 0)

m.c110 = Constraint(expr=-0.5*m.x2*(m.x9 + m.x10) - m.x60 + m.x61 == 0)

m.c111 = Constraint(expr=-0.5*m.x2*(m.x10 + m.x11) - m.x61 + m.x62 == 0)

m.c112 = Constraint(expr=-0.5*m.x2*(m.x11 + m.x12) - m.x62 + m.x63 == 0)

m.c113 = Constraint(expr=-0.5*m.x2*(m.x12 + m.x13) - m.x63 + m.x64 == 0)

m.c114 = Constraint(expr=-0.5*m.x2*(m.x13 + m.x14) - m.x64 + m.x65 == 0)

m.c115 = Constraint(expr=-0.5*m.x2*(m.x14 + m.x15) - m.x65 + m.x66 == 0)

m.c116 = Constraint(expr=-0.5*m.x2*(m.x15 + m.x16) - m.x66 + m.x67 == 0)

m.c117 = Constraint(expr=-0.5*m.x2*(m.x16 + m.x17) - m.x67 + m.x68 == 0)

m.c118 = Constraint(expr=-0.5*m.x2*(m.x17 + m.x18) - m.x68 + m.x69 == 0)

m.c119 = Constraint(expr=-0.5*m.x2*(m.x18 + m.x19) - m.x69 + m.x70 == 0)

m.c120 = Constraint(expr=-0.5*m.x2*(m.x19 + m.x20) - m.x70 + m.x71 == 0)

m.c121 = Constraint(expr=-0.5*m.x2*(m.x20 + m.x21) - m.x71 + m.x72 == 0)

m.c122 = Constraint(expr=-0.5*m.x2*(m.x21 + m.x22) - m.x72 + m.x73 == 0)

m.c123 = Constraint(expr=-0.5*m.x2*(m.x22 + m.x23) - m.x73 + m.x74 == 0)

m.c124 = Constraint(expr=-0.5*m.x2*(m.x23 + m.x24) - m.x74 + m.x75 == 0)

m.c125 = Constraint(expr=-0.5*m.x2*(m.x24 + m.x25) - m.x75 + m.x76 == 0)

m.c126 = Constraint(expr=-0.5*m.x2*(m.x25 + m.x26) - m.x76 + m.x77 == 0)

m.c127 = Constraint(expr=-0.5*m.x2*(m.x26 + m.x27) - m.x77 + m.x78 == 0)

m.c128 = Constraint(expr=-0.5*m.x2*(m.x27 + m.x28) - m.x78 + m.x79 == 0)

m.c129 = Constraint(expr=-0.5*m.x2*(m.x28 + m.x29) - m.x79 + m.x80 == 0)

m.c130 = Constraint(expr=-0.5*m.x2*(m.x29 + m.x30) - m.x80 + m.x81 == 0)

m.c131 = Constraint(expr=-0.5*m.x2*(m.x30 + m.x31) - m.x81 + m.x82 == 0)

m.c132 = Constraint(expr=-0.5*m.x2*(m.x31 + m.x32) - m.x82 + m.x83 == 0)

m.c133 = Constraint(expr=-0.5*m.x2*(m.x32 + m.x33) - m.x83 + m.x84 == 0)

m.c134 = Constraint(expr=-0.5*m.x2*(m.x33 + m.x34) - m.x84 + m.x85 == 0)

m.c135 = Constraint(expr=-0.5*m.x2*(m.x34 + m.x35) - m.x85 + m.x86 == 0)

m.c136 = Constraint(expr=-0.5*m.x2*(m.x35 + m.x36) - m.x86 + m.x87 == 0)

m.c137 = Constraint(expr=-0.5*m.x2*(m.x36 + m.x37) - m.x87 + m.x88 == 0)

m.c138 = Constraint(expr=-0.5*m.x2*(m.x37 + m.x38) - m.x88 + m.x89 == 0)

m.c139 = Constraint(expr=-0.5*m.x2*(m.x38 + m.x39) - m.x89 + m.x90 == 0)

m.c140 = Constraint(expr=-0.5*m.x2*(m.x39 + m.x40) - m.x90 + m.x91 == 0)

m.c141 = Constraint(expr=-0.5*m.x2*(m.x40 + m.x41) - m.x91 + m.x92 == 0)

m.c142 = Constraint(expr=-0.5*m.x2*(m.x41 + m.x42) - m.x92 + m.x93 == 0)

m.c143 = Constraint(expr=-0.5*m.x2*(m.x42 + m.x43) - m.x93 + m.x94 == 0)

m.c144 = Constraint(expr=-0.5*m.x2*(m.x43 + m.x44) - m.x94 + m.x95 == 0)

m.c145 = Constraint(expr=-0.5*m.x2*(m.x44 + m.x45) - m.x95 + m.x96 == 0)

m.c146 = Constraint(expr=-0.5*m.x2*(m.x45 + m.x46) - m.x96 + m.x97 == 0)

m.c147 = Constraint(expr=-0.5*m.x2*(m.x46 + m.x47) - m.x97 + m.x98 == 0)

m.c148 = Constraint(expr=-0.5*m.x2*(m.x47 + m.x48) - m.x98 + m.x99 == 0)

m.c149 = Constraint(expr=-0.5*m.x2*(m.x48 + m.x49) - m.x99 + m.x100 == 0)

m.c150 = Constraint(expr=-0.5*m.x2*(m.x49 + m.x50) - m.x100 + m.x101 == 0)

m.c151 = Constraint(expr=-0.5*m.x2*(m.x50 + m.x51) - m.x101 + m.x102 == 0)

m.c152 = Constraint(expr=-0.5*m.x2*(m.x51 + m.x52) - m.x102 + m.x103 == 0)

m.c153 = Constraint(expr=-0.5*m.x2*(m.x52 + m.x53) - m.x103 + m.x104 == 0)

m.c154 = Constraint(expr=-0.5*((m.x208 - m.x157*m.x106 - m.x259)/m.x157 + (m.x207 - m.x156*m.x105 - m.x258)/m.x156)*m.x2
                          - m.x3 + m.x4 == 0)

m.c155 = Constraint(expr=-0.5*((m.x209 - m.x158*m.x107 - m.x260)/m.x158 + (m.x208 - m.x157*m.x106 - m.x259)/m.x157)*m.x2
                          - m.x4 + m.x5 == 0)

m.c156 = Constraint(expr=-0.5*((m.x210 - m.x159*m.x108 - m.x261)/m.x159 + (m.x209 - m.x158*m.x107 - m.x260)/m.x158)*m.x2
                          - m.x5 + m.x6 == 0)

m.c157 = Constraint(expr=-0.5*((m.x211 - m.x160*m.x109 - m.x262)/m.x160 + (m.x210 - m.x159*m.x108 - m.x261)/m.x159)*m.x2
                          - m.x6 + m.x7 == 0)

m.c158 = Constraint(expr=-0.5*((m.x212 - m.x161*m.x110 - m.x263)/m.x161 + (m.x211 - m.x160*m.x109 - m.x262)/m.x160)*m.x2
                          - m.x7 + m.x8 == 0)

m.c159 = Constraint(expr=-0.5*((m.x213 - m.x162*m.x111 - m.x264)/m.x162 + (m.x212 - m.x161*m.x110 - m.x263)/m.x161)*m.x2
                          - m.x8 + m.x9 == 0)

m.c160 = Constraint(expr=-0.5*((m.x214 - m.x163*m.x112 - m.x265)/m.x163 + (m.x213 - m.x162*m.x111 - m.x264)/m.x162)*m.x2
                          - m.x9 + m.x10 == 0)

m.c161 = Constraint(expr=-0.5*((m.x215 - m.x164*m.x113 - m.x266)/m.x164 + (m.x214 - m.x163*m.x112 - m.x265)/m.x163)*m.x2
                          - m.x10 + m.x11 == 0)

m.c162 = Constraint(expr=-0.5*((m.x216 - m.x165*m.x114 - m.x267)/m.x165 + (m.x215 - m.x164*m.x113 - m.x266)/m.x164)*m.x2
                          - m.x11 + m.x12 == 0)

m.c163 = Constraint(expr=-0.5*((m.x217 - m.x166*m.x115 - m.x268)/m.x166 + (m.x216 - m.x165*m.x114 - m.x267)/m.x165)*m.x2
                          - m.x12 + m.x13 == 0)

m.c164 = Constraint(expr=-0.5*((m.x218 - m.x167*m.x116 - m.x269)/m.x167 + (m.x217 - m.x166*m.x115 - m.x268)/m.x166)*m.x2
                          - m.x13 + m.x14 == 0)

m.c165 = Constraint(expr=-0.5*((m.x219 - m.x168*m.x117 - m.x270)/m.x168 + (m.x218 - m.x167*m.x116 - m.x269)/m.x167)*m.x2
                          - m.x14 + m.x15 == 0)

m.c166 = Constraint(expr=-0.5*((m.x220 - m.x169*m.x118 - m.x271)/m.x169 + (m.x219 - m.x168*m.x117 - m.x270)/m.x168)*m.x2
                          - m.x15 + m.x16 == 0)

m.c167 = Constraint(expr=-0.5*((m.x221 - m.x170*m.x119 - m.x272)/m.x170 + (m.x220 - m.x169*m.x118 - m.x271)/m.x169)*m.x2
                          - m.x16 + m.x17 == 0)

m.c168 = Constraint(expr=-0.5*((m.x222 - m.x171*m.x120 - m.x273)/m.x171 + (m.x221 - m.x170*m.x119 - m.x272)/m.x170)*m.x2
                          - m.x17 + m.x18 == 0)

m.c169 = Constraint(expr=-0.5*((m.x223 - m.x172*m.x121 - m.x274)/m.x172 + (m.x222 - m.x171*m.x120 - m.x273)/m.x171)*m.x2
                          - m.x18 + m.x19 == 0)

m.c170 = Constraint(expr=-0.5*((m.x224 - m.x173*m.x122 - m.x275)/m.x173 + (m.x223 - m.x172*m.x121 - m.x274)/m.x172)*m.x2
                          - m.x19 + m.x20 == 0)

m.c171 = Constraint(expr=-0.5*((m.x225 - m.x174*m.x123 - m.x276)/m.x174 + (m.x224 - m.x173*m.x122 - m.x275)/m.x173)*m.x2
                          - m.x20 + m.x21 == 0)

m.c172 = Constraint(expr=-0.5*((m.x226 - m.x175*m.x124 - m.x277)/m.x175 + (m.x225 - m.x174*m.x123 - m.x276)/m.x174)*m.x2
                          - m.x21 + m.x22 == 0)

m.c173 = Constraint(expr=-0.5*((m.x227 - m.x176*m.x125 - m.x278)/m.x176 + (m.x226 - m.x175*m.x124 - m.x277)/m.x175)*m.x2
                          - m.x22 + m.x23 == 0)

m.c174 = Constraint(expr=-0.5*((m.x228 - m.x177*m.x126 - m.x279)/m.x177 + (m.x227 - m.x176*m.x125 - m.x278)/m.x176)*m.x2
                          - m.x23 + m.x24 == 0)

m.c175 = Constraint(expr=-0.5*((m.x229 - m.x178*m.x127 - m.x280)/m.x178 + (m.x228 - m.x177*m.x126 - m.x279)/m.x177)*m.x2
                          - m.x24 + m.x25 == 0)

m.c176 = Constraint(expr=-0.5*((m.x230 - m.x179*m.x128 - m.x281)/m.x179 + (m.x229 - m.x178*m.x127 - m.x280)/m.x178)*m.x2
                          - m.x25 + m.x26 == 0)

m.c177 = Constraint(expr=-0.5*((m.x231 - m.x180*m.x129 - m.x282)/m.x180 + (m.x230 - m.x179*m.x128 - m.x281)/m.x179)*m.x2
                          - m.x26 + m.x27 == 0)

m.c178 = Constraint(expr=-0.5*((m.x232 - m.x181*m.x130 - m.x283)/m.x181 + (m.x231 - m.x180*m.x129 - m.x282)/m.x180)*m.x2
                          - m.x27 + m.x28 == 0)

m.c179 = Constraint(expr=-0.5*((m.x233 - m.x182*m.x131 - m.x284)/m.x182 + (m.x232 - m.x181*m.x130 - m.x283)/m.x181)*m.x2
                          - m.x28 + m.x29 == 0)

m.c180 = Constraint(expr=-0.5*((m.x234 - m.x183*m.x132 - m.x285)/m.x183 + (m.x233 - m.x182*m.x131 - m.x284)/m.x182)*m.x2
                          - m.x29 + m.x30 == 0)

m.c181 = Constraint(expr=-0.5*((m.x235 - m.x184*m.x133 - m.x286)/m.x184 + (m.x234 - m.x183*m.x132 - m.x285)/m.x183)*m.x2
                          - m.x30 + m.x31 == 0)

m.c182 = Constraint(expr=-0.5*((m.x236 - m.x185*m.x134 - m.x287)/m.x185 + (m.x235 - m.x184*m.x133 - m.x286)/m.x184)*m.x2
                          - m.x31 + m.x32 == 0)

m.c183 = Constraint(expr=-0.5*((m.x237 - m.x186*m.x135 - m.x288)/m.x186 + (m.x236 - m.x185*m.x134 - m.x287)/m.x185)*m.x2
                          - m.x32 + m.x33 == 0)

m.c184 = Constraint(expr=-0.5*((m.x238 - m.x187*m.x136 - m.x289)/m.x187 + (m.x237 - m.x186*m.x135 - m.x288)/m.x186)*m.x2
                          - m.x33 + m.x34 == 0)

m.c185 = Constraint(expr=-0.5*((m.x239 - m.x188*m.x137 - m.x290)/m.x188 + (m.x238 - m.x187*m.x136 - m.x289)/m.x187)*m.x2
                          - m.x34 + m.x35 == 0)

m.c186 = Constraint(expr=-0.5*((m.x240 - m.x189*m.x138 - m.x291)/m.x189 + (m.x239 - m.x188*m.x137 - m.x290)/m.x188)*m.x2
                          - m.x35 + m.x36 == 0)

m.c187 = Constraint(expr=-0.5*((m.x241 - m.x190*m.x139 - m.x292)/m.x190 + (m.x240 - m.x189*m.x138 - m.x291)/m.x189)*m.x2
                          - m.x36 + m.x37 == 0)

m.c188 = Constraint(expr=-0.5*((m.x242 - m.x191*m.x140 - m.x293)/m.x191 + (m.x241 - m.x190*m.x139 - m.x292)/m.x190)*m.x2
                          - m.x37 + m.x38 == 0)

m.c189 = Constraint(expr=-0.5*((m.x243 - m.x192*m.x141 - m.x294)/m.x192 + (m.x242 - m.x191*m.x140 - m.x293)/m.x191)*m.x2
                          - m.x38 + m.x39 == 0)

m.c190 = Constraint(expr=-0.5*((m.x244 - m.x193*m.x142 - m.x295)/m.x193 + (m.x243 - m.x192*m.x141 - m.x294)/m.x192)*m.x2
                          - m.x39 + m.x40 == 0)

m.c191 = Constraint(expr=-0.5*((m.x245 - m.x194*m.x143 - m.x296)/m.x194 + (m.x244 - m.x193*m.x142 - m.x295)/m.x193)*m.x2
                          - m.x40 + m.x41 == 0)

m.c192 = Constraint(expr=-0.5*((m.x246 - m.x195*m.x144 - m.x297)/m.x195 + (m.x245 - m.x194*m.x143 - m.x296)/m.x194)*m.x2
                          - m.x41 + m.x42 == 0)

m.c193 = Constraint(expr=-0.5*((m.x247 - m.x196*m.x145 - m.x298)/m.x196 + (m.x246 - m.x195*m.x144 - m.x297)/m.x195)*m.x2
                          - m.x42 + m.x43 == 0)

m.c194 = Constraint(expr=-0.5*((m.x248 - m.x197*m.x146 - m.x299)/m.x197 + (m.x247 - m.x196*m.x145 - m.x298)/m.x196)*m.x2
                          - m.x43 + m.x44 == 0)

m.c195 = Constraint(expr=-0.5*((m.x249 - m.x198*m.x147 - m.x300)/m.x198 + (m.x248 - m.x197*m.x146 - m.x299)/m.x197)*m.x2
                          - m.x44 + m.x45 == 0)

m.c196 = Constraint(expr=-0.5*((m.x250 - m.x199*m.x148 - m.x301)/m.x199 + (m.x249 - m.x198*m.x147 - m.x300)/m.x198)*m.x2
                          - m.x45 + m.x46 == 0)

m.c197 = Constraint(expr=-0.5*((m.x251 - m.x200*m.x149 - m.x302)/m.x200 + (m.x250 - m.x199*m.x148 - m.x301)/m.x199)*m.x2
                          - m.x46 + m.x47 == 0)

m.c198 = Constraint(expr=-0.5*((m.x252 - m.x201*m.x150 - m.x303)/m.x201 + (m.x251 - m.x200*m.x149 - m.x302)/m.x200)*m.x2
                          - m.x47 + m.x48 == 0)

m.c199 = Constraint(expr=-0.5*((m.x253 - m.x202*m.x151 - m.x304)/m.x202 + (m.x252 - m.x201*m.x150 - m.x303)/m.x201)*m.x2
                          - m.x48 + m.x49 == 0)

m.c200 = Constraint(expr=-0.5*((m.x254 - m.x203*m.x152 - m.x305)/m.x203 + (m.x253 - m.x202*m.x151 - m.x304)/m.x202)*m.x2
                          - m.x49 + m.x50 == 0)

m.c201 = Constraint(expr=-0.5*((m.x255 - m.x204*m.x153 - m.x306)/m.x204 + (m.x254 - m.x203*m.x152 - m.x305)/m.x203)*m.x2
                          - m.x50 + m.x51 == 0)

m.c202 = Constraint(expr=-0.5*((m.x256 - m.x205*m.x154 - m.x307)/m.x205 + (m.x255 - m.x204*m.x153 - m.x306)/m.x204)*m.x2
                          - m.x51 + m.x52 == 0)

m.c203 = Constraint(expr=-0.5*((m.x257 - m.x206*m.x155 - m.x308)/m.x206 + (m.x256 - m.x205*m.x154 - m.x307)/m.x205)*m.x2
                          - m.x52 + m.x53 == 0)

m.c204 = Constraint(expr=m.x2*(m.x207 + m.x208) - m.x156 + m.x157 == 0)

m.c205 = Constraint(expr=m.x2*(m.x208 + m.x209) - m.x157 + m.x158 == 0)

m.c206 = Constraint(expr=m.x2*(m.x209 + m.x210) - m.x158 + m.x159 == 0)

m.c207 = Constraint(expr=m.x2*(m.x210 + m.x211) - m.x159 + m.x160 == 0)

m.c208 = Constraint(expr=m.x2*(m.x211 + m.x212) - m.x160 + m.x161 == 0)

m.c209 = Constraint(expr=m.x2*(m.x212 + m.x213) - m.x161 + m.x162 == 0)

m.c210 = Constraint(expr=m.x2*(m.x213 + m.x214) - m.x162 + m.x163 == 0)

m.c211 = Constraint(expr=m.x2*(m.x214 + m.x215) - m.x163 + m.x164 == 0)

m.c212 = Constraint(expr=m.x2*(m.x215 + m.x216) - m.x164 + m.x165 == 0)

m.c213 = Constraint(expr=m.x2*(m.x216 + m.x217) - m.x165 + m.x166 == 0)

m.c214 = Constraint(expr=m.x2*(m.x217 + m.x218) - m.x166 + m.x167 == 0)

m.c215 = Constraint(expr=m.x2*(m.x218 + m.x219) - m.x167 + m.x168 == 0)

m.c216 = Constraint(expr=m.x2*(m.x219 + m.x220) - m.x168 + m.x169 == 0)

m.c217 = Constraint(expr=m.x2*(m.x220 + m.x221) - m.x169 + m.x170 == 0)

m.c218 = Constraint(expr=m.x2*(m.x221 + m.x222) - m.x170 + m.x171 == 0)

m.c219 = Constraint(expr=m.x2*(m.x222 + m.x223) - m.x171 + m.x172 == 0)

m.c220 = Constraint(expr=m.x2*(m.x223 + m.x224) - m.x172 + m.x173 == 0)

m.c221 = Constraint(expr=m.x2*(m.x224 + m.x225) - m.x173 + m.x174 == 0)

m.c222 = Constraint(expr=m.x2*(m.x225 + m.x226) - m.x174 + m.x175 == 0)

m.c223 = Constraint(expr=m.x2*(m.x226 + m.x227) - m.x175 + m.x176 == 0)

m.c224 = Constraint(expr=m.x2*(m.x227 + m.x228) - m.x176 + m.x177 == 0)

m.c225 = Constraint(expr=m.x2*(m.x228 + m.x229) - m.x177 + m.x178 == 0)

m.c226 = Constraint(expr=m.x2*(m.x229 + m.x230) - m.x178 + m.x179 == 0)

m.c227 = Constraint(expr=m.x2*(m.x230 + m.x231) - m.x179 + m.x180 == 0)

m.c228 = Constraint(expr=m.x2*(m.x231 + m.x232) - m.x180 + m.x181 == 0)

m.c229 = Constraint(expr=m.x2*(m.x232 + m.x233) - m.x181 + m.x182 == 0)

m.c230 = Constraint(expr=m.x2*(m.x233 + m.x234) - m.x182 + m.x183 == 0)

m.c231 = Constraint(expr=m.x2*(m.x234 + m.x235) - m.x183 + m.x184 == 0)

m.c232 = Constraint(expr=m.x2*(m.x235 + m.x236) - m.x184 + m.x185 == 0)

m.c233 = Constraint(expr=m.x2*(m.x236 + m.x237) - m.x185 + m.x186 == 0)

m.c234 = Constraint(expr=m.x2*(m.x237 + m.x238) - m.x186 + m.x187 == 0)

m.c235 = Constraint(expr=m.x2*(m.x238 + m.x239) - m.x187 + m.x188 == 0)

m.c236 = Constraint(expr=m.x2*(m.x239 + m.x240) - m.x188 + m.x189 == 0)

m.c237 = Constraint(expr=m.x2*(m.x240 + m.x241) - m.x189 + m.x190 == 0)

m.c238 = Constraint(expr=m.x2*(m.x241 + m.x242) - m.x190 + m.x191 == 0)

m.c239 = Constraint(expr=m.x2*(m.x242 + m.x243) - m.x191 + m.x192 == 0)

m.c240 = Constraint(expr=m.x2*(m.x243 + m.x244) - m.x192 + m.x193 == 0)

m.c241 = Constraint(expr=m.x2*(m.x244 + m.x245) - m.x193 + m.x194 == 0)

m.c242 = Constraint(expr=m.x2*(m.x245 + m.x246) - m.x194 + m.x195 == 0)

m.c243 = Constraint(expr=m.x2*(m.x246 + m.x247) - m.x195 + m.x196 == 0)

m.c244 = Constraint(expr=m.x2*(m.x247 + m.x248) - m.x196 + m.x197 == 0)

m.c245 = Constraint(expr=m.x2*(m.x248 + m.x249) - m.x197 + m.x198 == 0)

m.c246 = Constraint(expr=m.x2*(m.x249 + m.x250) - m.x198 + m.x199 == 0)

m.c247 = Constraint(expr=m.x2*(m.x250 + m.x251) - m.x199 + m.x200 == 0)

m.c248 = Constraint(expr=m.x2*(m.x251 + m.x252) - m.x200 + m.x201 == 0)

m.c249 = Constraint(expr=m.x2*(m.x252 + m.x253) - m.x201 + m.x202 == 0)

m.c250 = Constraint(expr=m.x2*(m.x253 + m.x254) - m.x202 + m.x203 == 0)

m.c251 = Constraint(expr=m.x2*(m.x254 + m.x255) - m.x203 + m.x204 == 0)

m.c252 = Constraint(expr=m.x2*(m.x255 + m.x256) - m.x204 + m.x205 == 0)

m.c253 = Constraint(expr=m.x2*(m.x256 + m.x257) - m.x205 + m.x206 == 0)
