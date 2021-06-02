#  MINLP written by GAMS Convert at 04/21/18 13:51:14
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        899      361      179      359        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        841      661      180        0        0        0        0        0
#  FX     19        1       18        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2812     2452      360        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x2 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x3 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x4 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x5 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x6 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x7 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x8 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x9 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x10 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x11 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x12 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x13 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x14 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x15 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x16 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x17 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x18 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x19 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x20 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x21 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x22 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x23 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x24 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x25 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x26 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x27 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x28 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x29 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x30 = Var(within=Reals,bounds=(0,1211.001),initialize=1211)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x156 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x235 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x255 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x309 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x311 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x312 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x313 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x314 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x315 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x316 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x317 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x318 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x319 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x320 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x321 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x322 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x323 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x324 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x325 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x326 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x327 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x328 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x329 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x330 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x331 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x332 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x333 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x334 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x335 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x336 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x337 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x338 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x339 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x340 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x341 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x342 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x343 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x344 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x345 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x346 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x347 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x348 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x349 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x350 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x351 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x352 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x353 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x354 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x355 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x356 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x357 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x358 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x359 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x360 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x361 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x362 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x363 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x364 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x365 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x366 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x367 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x368 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x369 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x370 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x371 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x372 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x373 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x374 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x375 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x376 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x377 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x378 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x379 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x380 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x381 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x382 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x383 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x384 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x385 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x386 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x387 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x388 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x389 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x390 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x391 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x392 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x393 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x394 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x395 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x396 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x397 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x398 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x399 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x400 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x401 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x402 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x403 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x404 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x405 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x406 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x407 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x408 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x409 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x410 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x411 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x412 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x413 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x414 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x415 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x416 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x417 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x418 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x419 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x420 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x421 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x422 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x423 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x424 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x425 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x426 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x427 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x428 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x429 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x430 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x431 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x432 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x433 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x434 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x435 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x436 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x437 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x438 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x439 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x440 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x441 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x442 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x443 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x444 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x445 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x446 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x447 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x448 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x449 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x450 = Var(within=Reals,bounds=(0,None),initialize=0)
m.b451 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b452 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b453 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b454 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b455 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b456 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b457 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b458 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b459 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b460 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b461 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b462 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b463 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b464 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b465 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b466 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b467 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b468 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b469 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b470 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b471 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b472 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b473 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b474 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b475 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b476 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b477 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b478 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b479 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b480 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b481 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b482 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b483 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b484 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b485 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b486 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b487 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b488 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b489 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b490 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b491 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b492 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b493 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b494 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b495 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b496 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b497 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b498 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b499 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b500 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b501 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b502 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b503 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b504 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b505 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b506 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b507 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b508 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b509 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b510 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b511 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b512 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b513 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b514 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b515 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b516 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b517 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b518 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b519 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b520 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b521 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b522 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b523 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b524 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b525 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b526 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b527 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b528 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b529 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b530 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b531 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b532 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b533 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b534 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b535 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b536 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b537 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b538 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b539 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b540 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b541 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b542 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b543 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b544 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b545 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b546 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b547 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b548 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b549 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b550 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b551 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b552 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b553 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b554 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b555 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b556 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b557 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b558 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b559 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b560 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b561 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b562 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b563 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b564 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b565 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b566 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b567 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b568 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b569 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b570 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b571 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b572 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b573 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b574 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b575 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b576 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b577 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b578 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b579 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b580 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b581 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b582 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b583 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b584 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b585 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b586 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b587 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b588 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b589 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b590 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b591 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b592 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b593 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b594 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b595 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b596 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b597 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b598 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b599 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b600 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b601 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b602 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b603 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b604 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b605 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b606 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b607 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b608 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b609 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b610 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b611 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b612 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b613 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b614 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b615 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b616 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b617 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b618 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b619 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b620 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b621 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b622 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b623 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b624 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b625 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b626 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b627 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b628 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b629 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b630 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x631 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x632 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x633 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x634 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x635 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x636 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x637 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x638 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x639 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x640 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x641 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x642 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x643 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x644 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x645 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x646 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x647 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x648 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x649 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x650 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x651 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x652 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x653 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x654 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x655 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x656 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x657 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x658 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x659 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x660 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x661 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x662 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x663 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x664 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x665 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x666 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x667 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x668 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x669 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x670 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x671 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x672 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x673 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x674 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x675 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x676 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x677 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x678 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x679 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x680 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x681 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x682 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x683 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x684 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x685 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x686 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x687 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x688 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x689 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x690 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x691 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x692 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x693 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x694 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x695 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x696 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x697 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x698 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x699 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x700 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x701 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x702 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x703 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x704 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x705 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x706 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x707 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x708 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x709 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x710 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x711 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x712 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x713 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x714 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x715 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x716 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x717 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x718 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x719 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x720 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x721 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x722 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x723 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x724 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x725 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x726 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x727 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x728 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x729 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x730 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x731 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x732 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x733 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x734 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x735 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x736 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x737 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x738 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x739 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x740 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x741 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x742 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x743 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x744 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x745 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x746 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x747 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x748 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x749 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x750 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x751 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x752 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x753 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x754 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x755 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x756 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x757 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x758 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x759 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x760 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x761 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x762 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x763 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x764 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x765 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x766 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x767 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x768 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x769 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x770 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x771 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x772 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x773 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x774 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x775 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x776 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x777 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x778 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x779 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x780 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x781 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x782 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x783 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x784 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x785 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x786 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x787 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x788 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x789 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x790 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x791 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x792 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x793 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x794 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x795 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x796 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x797 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x798 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x799 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x800 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x801 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x802 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x803 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x804 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x805 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x806 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x807 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x808 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x809 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x810 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x811 = Var(within=Reals,bounds=(1211,1211),initialize=1211)
m.x812 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x813 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x814 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x815 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x816 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x817 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x818 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x819 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x820 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x821 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x822 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x823 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x824 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x825 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x826 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x827 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x828 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x829 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x830 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x831 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x832 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x833 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x834 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x835 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x836 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x837 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x838 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x839 = Var(within=Reals,bounds=(None,None),initialize=1211)
m.x840 = Var(within=Reals,bounds=(None,None),initialize=1211)

m.obj = Objective(expr= - 300.544*m.x211 - 225.408*m.x212 - 150.272*m.x213 - 300.544*m.x214 - 225.408*m.x215
                        - 150.272*m.x216 - 300.544*m.x217 - 225.408*m.x218 - 150.272*m.x219 - 300.544*m.x220
                        - 225.408*m.x221 - 150.272*m.x222 - 300.544*m.x223 - 225.408*m.x224 - 150.272*m.x225
                        - 300.544*m.x226 - 225.408*m.x227 - 150.272*m.x228 - 300.544*m.x229 - 225.408*m.x230
                        - 150.272*m.x231 - 300.544*m.x232 - 225.408*m.x233 - 150.272*m.x234 - 300.544*m.x235
                        - 225.408*m.x236 - 150.272*m.x237 - 300.544*m.x238 - 225.408*m.x239 - 150.272*m.x240
                        - 300.544*m.x241 - 225.408*m.x242 - 150.272*m.x243 - 300.544*m.x244 - 225.408*m.x245
                        - 150.272*m.x246 - 300.544*m.x247 - 225.408*m.x248 - 150.272*m.x249 - 300.544*m.x250
                        - 225.408*m.x251 - 150.272*m.x252 - 300.544*m.x253 - 225.408*m.x254 - 150.272*m.x255
                        - 300.544*m.x256 - 225.408*m.x257 - 150.272*m.x258 - 300.544*m.x259 - 225.408*m.x260
                        - 150.272*m.x261 - 300.544*m.x262 - 225.408*m.x263 - 150.272*m.x264 - 300.544*m.x265
                        - 225.408*m.x266 - 150.272*m.x267 - 300.544*m.x268 - 225.408*m.x269 - 150.272*m.x270
                        - 300.544*m.x271 - 225.408*m.x272 - 150.272*m.x273 - 300.544*m.x274 - 225.408*m.x275
                        - 150.272*m.x276 - 300.544*m.x277 - 225.408*m.x278 - 150.272*m.x279 - 300.544*m.x280
                        - 225.408*m.x281 - 150.272*m.x282 - 300.544*m.x283 - 225.408*m.x284 - 150.272*m.x285
                        - 300.544*m.x286 - 225.408*m.x287 - 150.272*m.x288 - 300.544*m.x289 - 225.408*m.x290
                        - 150.272*m.x291 - 300.544*m.x292 - 225.408*m.x293 - 150.272*m.x294 - 300.544*m.x295
                        - 225.408*m.x296 - 150.272*m.x297 - 300.544*m.x298 - 225.408*m.x299 - 150.272*m.x300
                        - 2.66666666666667*m.x301 - 4*m.x302 - 5.33333333333333*m.x303 - 2.66666666666667*m.x304
                        - 4*m.x305 - 5.33333333333333*m.x306 - 2.66666666666667*m.x307 - 4*m.x308
                        - 5.33333333333333*m.x309 - 2.66666666666667*m.x310 - 4*m.x311 - 5.33333333333333*m.x312
                        - 2.66666666666667*m.x313 - 4*m.x314 - 5.33333333333333*m.x315 - 2.66666666666667*m.x316
                        - 4*m.x317 - 5.33333333333333*m.x318 - 2.66666666666667*m.x319 - 4*m.x320
                        - 5.33333333333333*m.x321 - 2.66666666666667*m.x322 - 4*m.x323 - 5.33333333333333*m.x324
                        - 2.66666666666667*m.x325 - 4*m.x326 - 5.33333333333333*m.x327 - 2.66666666666667*m.x328
                        - 4*m.x329 - 5.33333333333333*m.x330 - 2.66666666666667*m.x331 - 4*m.x332
                        - 5.33333333333333*m.x333 - 2.66666666666667*m.x334 - 4*m.x335 - 5.33333333333333*m.x336
                        - 2.66666666666667*m.x337 - 4*m.x338 - 5.33333333333333*m.x339 - 2.66666666666667*m.x340
                        - 4*m.x341 - 5.33333333333333*m.x342 - 2.66666666666667*m.x343 - 4*m.x344
                        - 5.33333333333333*m.x345 - 2.66666666666667*m.x346 - 4*m.x347 - 5.33333333333333*m.x348
                        - 2.66666666666667*m.x349 - 4*m.x350 - 5.33333333333333*m.x351 - 2.66666666666667*m.x352
                        - 4*m.x353 - 5.33333333333333*m.x354 - 2.66666666666667*m.x355 - 4*m.x356
                        - 5.33333333333333*m.x357 - 2.66666666666667*m.x358 - 4*m.x359 - 5.33333333333333*m.x360
                        - 2.66666666666667*m.x361 - 4*m.x362 - 5.33333333333333*m.x363 - 2.66666666666667*m.x364
                        - 4*m.x365 - 5.33333333333333*m.x366 - 2.66666666666667*m.x367 - 4*m.x368
                        - 5.33333333333333*m.x369 - 2.66666666666667*m.x370 - 4*m.x371 - 5.33333333333333*m.x372
                        - 2.66666666666667*m.x373 - 4*m.x374 - 5.33333333333333*m.x375 - 2.66666666666667*m.x376
                        - 4*m.x377 - 5.33333333333333*m.x378 - 2.66666666666667*m.x379 - 4*m.x380
                        - 5.33333333333333*m.x381 - 2.66666666666667*m.x382 - 4*m.x383 - 5.33333333333333*m.x384
                        - 2.66666666666667*m.x385 - 4*m.x386 - 5.33333333333333*m.x387 - 2.66666666666667*m.x388
                        - 4*m.x389 - 5.33333333333333*m.x390 + 1.33333333333333*m.x631 + m.x632 + m.x633
                        + 1.33333333333333*m.x634 + m.x635 + m.x636 + 1.33333333333333*m.x637 + m.x638 + m.x639
                        + 1.33333333333333*m.x640 + m.x641 + m.x642 + 1.33333333333333*m.x643 + m.x644 + m.x645
                        + 1.33333333333333*m.x646 + m.x647 + m.x648 + 1.33333333333333*m.x649 + m.x650 + m.x651
                        + 1.33333333333333*m.x652 + m.x653 + m.x654 + 1.33333333333333*m.x655 + m.x656 + m.x657
                        + 1.33333333333333*m.x658 + m.x659 + m.x660 + 1.33333333333333*m.x661 + m.x662 + m.x663
                        + 1.33333333333333*m.x664 + m.x665 + m.x666 + 1.33333333333333*m.x667 + m.x668 + m.x669
                        + 1.33333333333333*m.x670 + m.x671 + m.x672 + 1.33333333333333*m.x673 + m.x674 + m.x675
                        + 1.33333333333333*m.x676 + m.x677 + m.x678 + 1.33333333333333*m.x679 + m.x680 + m.x681
                        + 1.33333333333333*m.x682 + m.x683 + m.x684 + 1.33333333333333*m.x685 + m.x686 + m.x687
                        + 1.33333333333333*m.x688 + m.x689 + m.x690 + 1.33333333333333*m.x691 + m.x692 + m.x693
                        + 1.33333333333333*m.x694 + m.x695 + m.x696 + 1.33333333333333*m.x697 + m.x698 + m.x699
                        + 1.33333333333333*m.x700 + m.x701 + m.x702 + 1.33333333333333*m.x703 + m.x704 + m.x705
                        + 1.33333333333333*m.x706 + m.x707 + m.x708 + 1.33333333333333*m.x709 + m.x710 + m.x711
                        + 1.33333333333333*m.x712 + m.x713 + m.x714 + 1.33333333333333*m.x715 + m.x716 + m.x717
                        + 1.33333333333333*m.x718 + m.x719 + m.x720 + 1.33333333333333*m.x721 + m.x722 + m.x723
                        + 1.33333333333333*m.x724 + m.x725 + m.x726 + 1.33333333333333*m.x727 + m.x728 + m.x729
                        + 1.33333333333333*m.x730 + m.x731 + m.x732 + 1.33333333333333*m.x733 + m.x734 + m.x735
                        + 1.33333333333333*m.x736 + m.x737 + m.x738 + 1.33333333333333*m.x739 + m.x740 + m.x741
                        + 1.33333333333333*m.x742 + m.x743 + m.x744 + 1.33333333333333*m.x745 + m.x746 + m.x747
                        + 1.33333333333333*m.x748 + m.x749 + m.x750 + 1.33333333333333*m.x751 + m.x752 + m.x753
                        + 1.33333333333333*m.x754 + m.x755 + m.x756 + 1.33333333333333*m.x757 + m.x758 + m.x759
                        + 1.33333333333333*m.x760 + m.x761 + m.x762 + 1.33333333333333*m.x763 + m.x764 + m.x765
                        + 1.33333333333333*m.x766 + m.x767 + m.x768 + 1.33333333333333*m.x769 + m.x770 + m.x771
                        + 1.33333333333333*m.x772 + m.x773 + m.x774 + 1.33333333333333*m.x775 + m.x776 + m.x777
                        + 1.33333333333333*m.x778 + m.x779 + m.x780 + 1.33333333333333*m.x781 + m.x782 + m.x783
                        + 1.33333333333333*m.x784 + m.x785 + m.x786 + 1.33333333333333*m.x787 + m.x788 + m.x789
                        + 1.33333333333333*m.x790 + m.x791 + m.x792 + 1.33333333333333*m.x793 + m.x794 + m.x795
                        + 1.33333333333333*m.x796 + m.x797 + m.x798 + 1.33333333333333*m.x799 + m.x800 + m.x801
                        + 1.33333333333333*m.x802 + m.x803 + m.x804 + 1.33333333333333*m.x805 + m.x806 + m.x807
                        + 1.33333333333333*m.x808 + m.x809 + m.x810, sense=minimize)

m.c1 = Constraint(expr=   m.b451 + m.b541 + m.b571 + m.b601 == 1)

m.c2 = Constraint(expr=   m.b452 + m.b542 + m.b572 + m.b602 == 1)

m.c3 = Constraint(expr=   m.b453 + m.b543 + m.b573 + m.b603 == 1)

m.c4 = Constraint(expr=   m.b454 + m.b544 + m.b574 + m.b604 == 1)

m.c5 = Constraint(expr=   m.b455 + m.b545 + m.b575 + m.b605 == 1)

m.c6 = Constraint(expr=   m.b456 + m.b546 + m.b576 + m.b606 == 1)

m.c7 = Constraint(expr=   m.b457 + m.b547 + m.b577 + m.b607 == 1)

m.c8 = Constraint(expr=   m.b458 + m.b548 + m.b578 + m.b608 == 1)

m.c9 = Constraint(expr=   m.b459 + m.b549 + m.b579 + m.b609 == 1)

m.c10 = Constraint(expr=   m.b460 + m.b550 + m.b580 + m.b610 == 1)

m.c11 = Constraint(expr=   m.b461 + m.b551 + m.b581 + m.b611 == 1)

m.c12 = Constraint(expr=   m.b462 + m.b552 + m.b582 + m.b612 == 1)

m.c13 = Constraint(expr=   m.b463 + m.b553 + m.b583 + m.b613 == 1)

m.c14 = Constraint(expr=   m.b464 + m.b554 + m.b584 + m.b614 == 1)

m.c15 = Constraint(expr=   m.b465 + m.b555 + m.b585 + m.b615 == 1)

m.c16 = Constraint(expr=   m.b466 + m.b556 + m.b586 + m.b616 == 1)

m.c17 = Constraint(expr=   m.b467 + m.b557 + m.b587 + m.b617 == 1)

m.c18 = Constraint(expr=   m.b468 + m.b558 + m.b588 + m.b618 == 1)

m.c19 = Constraint(expr=   m.b469 + m.b559 + m.b589 + m.b619 == 1)

m.c20 = Constraint(expr=   m.b470 + m.b560 + m.b590 + m.b620 == 1)

m.c21 = Constraint(expr=   m.b471 + m.b561 + m.b591 + m.b621 == 1)

m.c22 = Constraint(expr=   m.b472 + m.b562 + m.b592 + m.b622 == 1)

m.c23 = Constraint(expr=   m.b473 + m.b563 + m.b593 + m.b623 == 1)

m.c24 = Constraint(expr=   m.b474 + m.b564 + m.b594 + m.b624 == 1)

m.c25 = Constraint(expr=   m.b475 + m.b565 + m.b595 + m.b625 == 1)

m.c26 = Constraint(expr=   m.b476 + m.b566 + m.b596 + m.b626 == 1)

m.c27 = Constraint(expr=   m.b477 + m.b567 + m.b597 + m.b627 == 1)

m.c28 = Constraint(expr=   m.b478 + m.b568 + m.b598 + m.b628 == 1)

m.c29 = Constraint(expr=   m.b479 + m.b569 + m.b599 + m.b629 == 1)

m.c30 = Constraint(expr=   m.b480 + m.b570 + m.b600 + m.b630 == 1)

m.c31 = Constraint(expr=   m.x31 + m.x32 + m.x33 + m.x121 + m.x122 + m.x123 + m.b451 == 1)

m.c32 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x124 + m.x125 + m.x126 + m.b452 == 1)

m.c33 = Constraint(expr=   m.x37 + m.x38 + m.x39 + m.x127 + m.x128 + m.x129 + m.b453 == 1)

m.c34 = Constraint(expr=   m.x40 + m.x41 + m.x42 + m.x130 + m.x131 + m.x132 + m.b454 == 1)

m.c35 = Constraint(expr=   m.x43 + m.x44 + m.x45 + m.x133 + m.x134 + m.x135 + m.b455 == 1)

m.c36 = Constraint(expr=   m.x46 + m.x47 + m.x48 + m.x136 + m.x137 + m.x138 + m.b456 == 1)

m.c37 = Constraint(expr=   m.x49 + m.x50 + m.x51 + m.x139 + m.x140 + m.x141 + m.b457 == 1)

m.c38 = Constraint(expr=   m.x52 + m.x53 + m.x54 + m.x142 + m.x143 + m.x144 + m.b458 == 1)

m.c39 = Constraint(expr=   m.x55 + m.x56 + m.x57 + m.x145 + m.x146 + m.x147 + m.b459 == 1)

m.c40 = Constraint(expr=   m.x58 + m.x59 + m.x60 + m.x148 + m.x149 + m.x150 + m.b460 == 1)

m.c41 = Constraint(expr=   m.x61 + m.x62 + m.x63 + m.x151 + m.x152 + m.x153 + m.b461 == 1)

m.c42 = Constraint(expr=   m.x64 + m.x65 + m.x66 + m.x154 + m.x155 + m.x156 + m.b462 == 1)

m.c43 = Constraint(expr=   m.x67 + m.x68 + m.x69 + m.x157 + m.x158 + m.x159 + m.b463 == 1)

m.c44 = Constraint(expr=   m.x70 + m.x71 + m.x72 + m.x160 + m.x161 + m.x162 + m.b464 == 1)

m.c45 = Constraint(expr=   m.x73 + m.x74 + m.x75 + m.x163 + m.x164 + m.x165 + m.b465 == 1)

m.c46 = Constraint(expr=   m.x76 + m.x77 + m.x78 + m.x166 + m.x167 + m.x168 + m.b466 == 1)

m.c47 = Constraint(expr=   m.x79 + m.x80 + m.x81 + m.x169 + m.x170 + m.x171 + m.b467 == 1)

m.c48 = Constraint(expr=   m.x82 + m.x83 + m.x84 + m.x172 + m.x173 + m.x174 + m.b468 == 1)

m.c49 = Constraint(expr=   m.x85 + m.x86 + m.x87 + m.x175 + m.x176 + m.x177 + m.b469 == 1)

m.c50 = Constraint(expr=   m.x88 + m.x89 + m.x90 + m.x178 + m.x179 + m.x180 + m.b470 == 1)

m.c51 = Constraint(expr=   m.x91 + m.x92 + m.x93 + m.x181 + m.x182 + m.x183 + m.b471 == 1)

m.c52 = Constraint(expr=   m.x94 + m.x95 + m.x96 + m.x184 + m.x185 + m.x186 + m.b472 == 1)

m.c53 = Constraint(expr=   m.x97 + m.x98 + m.x99 + m.x187 + m.x188 + m.x189 + m.b473 == 1)

m.c54 = Constraint(expr=   m.x100 + m.x101 + m.x102 + m.x190 + m.x191 + m.x192 + m.b474 == 1)

m.c55 = Constraint(expr=   m.x103 + m.x104 + m.x105 + m.x193 + m.x194 + m.x195 + m.b475 == 1)

m.c56 = Constraint(expr=   m.x106 + m.x107 + m.x108 + m.x196 + m.x197 + m.x198 + m.b476 == 1)

m.c57 = Constraint(expr=   m.x109 + m.x110 + m.x111 + m.x199 + m.x200 + m.x201 + m.b477 == 1)

m.c58 = Constraint(expr=   m.x112 + m.x113 + m.x114 + m.x202 + m.x203 + m.x204 + m.b478 == 1)

m.c59 = Constraint(expr=   m.x115 + m.x116 + m.x117 + m.x205 + m.x206 + m.x207 + m.b479 == 1)

m.c60 = Constraint(expr=   m.x118 + m.x119 + m.x120 + m.x208 + m.x209 + m.x210 + m.b480 == 1)

m.c61 = Constraint(expr= - 3.16363636363636*m.x31 - 3.16363636363636*m.x32 - 3.16363636363636*m.x33
                         + 22.5454545454545*m.b541 + 9.09090909090909*m.b571 - m.x811 + m.x812 <= -33.8181818181818)

m.c62 = Constraint(expr= - 3.16363636363636*m.x34 - 3.16363636363636*m.x35 - 3.16363636363636*m.x36
                         + 22.5454545454545*m.b542 + 9.09090909090909*m.b572 - m.x812 + m.x813 <= -33.8181818181818)

m.c63 = Constraint(expr= - 3.16363636363636*m.x37 - 3.16363636363636*m.x38 - 3.16363636363636*m.x39
                         + 22.5454545454545*m.b543 + 9.09090909090909*m.b573 - m.x813 + m.x814 <= -33.8181818181818)

m.c64 = Constraint(expr= - 3.16363636363636*m.x40 - 3.16363636363636*m.x41 - 3.16363636363636*m.x42
                         + 22.5454545454545*m.b544 + 9.09090909090909*m.b574 - m.x814 + m.x815 <= -33.8181818181818)

m.c65 = Constraint(expr= - 3.16363636363636*m.x43 - 3.16363636363636*m.x44 - 3.16363636363636*m.x45
                         + 22.5454545454545*m.b545 + 9.09090909090909*m.b575 - m.x815 + m.x816 <= -33.8181818181818)

m.c66 = Constraint(expr= - 3.16363636363636*m.x46 - 3.16363636363636*m.x47 - 3.16363636363636*m.x48
                         + 22.5454545454545*m.b546 + 9.09090909090909*m.b576 - m.x816 + m.x817 <= -33.8181818181818)

m.c67 = Constraint(expr= - 3.16363636363636*m.x49 - 3.16363636363636*m.x50 - 3.16363636363636*m.x51
                         + 22.5454545454545*m.b547 + 9.09090909090909*m.b577 - m.x817 + m.x818 <= -33.8181818181818)

m.c68 = Constraint(expr= - 3.16363636363636*m.x52 - 3.16363636363636*m.x53 - 3.16363636363636*m.x54
                         + 22.5454545454545*m.b548 + 9.09090909090909*m.b578 - m.x818 + m.x819 <= -33.8181818181818)

m.c69 = Constraint(expr= - 3.16363636363636*m.x55 - 3.16363636363636*m.x56 - 3.16363636363636*m.x57
                         + 22.5454545454545*m.b549 + 9.09090909090909*m.b579 - m.x819 + m.x820 <= -33.8181818181818)

m.c70 = Constraint(expr= - 3.16363636363636*m.x58 - 3.16363636363636*m.x59 - 3.16363636363636*m.x60
                         + 22.5454545454545*m.b550 + 9.09090909090909*m.b580 - m.x820 + m.x821 <= -33.8181818181818)

m.c71 = Constraint(expr= - 3.16363636363636*m.x61 - 3.16363636363636*m.x62 - 3.16363636363636*m.x63
                         + 22.5454545454545*m.b551 + 9.09090909090909*m.b581 - m.x821 + m.x822 <= -33.8181818181818)

m.c72 = Constraint(expr= - 3.16363636363636*m.x64 - 3.16363636363636*m.x65 - 3.16363636363636*m.x66
                         + 22.5454545454545*m.b552 + 9.09090909090909*m.b582 - m.x822 + m.x823 <= -33.8181818181818)

m.c73 = Constraint(expr= - 3.16363636363636*m.x67 - 3.16363636363636*m.x68 - 3.16363636363636*m.x69
                         + 22.5454545454545*m.b553 + 9.09090909090909*m.b583 - m.x823 + m.x824 <= -33.8181818181818)

m.c74 = Constraint(expr= - 3.16363636363636*m.x70 - 3.16363636363636*m.x71 - 3.16363636363636*m.x72
                         + 22.5454545454545*m.b554 + 9.09090909090909*m.b584 - m.x824 + m.x825 <= -33.8181818181818)

m.c75 = Constraint(expr= - 3.16363636363636*m.x73 - 3.16363636363636*m.x74 - 3.16363636363636*m.x75
                         + 22.5454545454545*m.b555 + 9.09090909090909*m.b585 - m.x825 + m.x826 <= -33.8181818181818)

m.c76 = Constraint(expr= - 3.16363636363636*m.x76 - 3.16363636363636*m.x77 - 3.16363636363636*m.x78
                         + 22.5454545454545*m.b556 + 9.09090909090909*m.b586 - m.x826 + m.x827 <= -33.8181818181818)

m.c77 = Constraint(expr= - 3.16363636363636*m.x79 - 3.16363636363636*m.x80 - 3.16363636363636*m.x81
                         + 22.5454545454545*m.b557 + 9.09090909090909*m.b587 - m.x827 + m.x828 <= -33.8181818181818)

m.c78 = Constraint(expr= - 3.16363636363636*m.x82 - 3.16363636363636*m.x83 - 3.16363636363636*m.x84
                         + 22.5454545454545*m.b558 + 9.09090909090909*m.b588 - m.x828 + m.x829 <= -33.8181818181818)

m.c79 = Constraint(expr= - 3.16363636363636*m.x85 - 3.16363636363636*m.x86 - 3.16363636363636*m.x87
                         + 22.5454545454545*m.b559 + 9.09090909090909*m.b589 - m.x829 + m.x830 <= -33.8181818181818)

m.c80 = Constraint(expr= - 3.16363636363636*m.x88 - 3.16363636363636*m.x89 - 3.16363636363636*m.x90
                         + 22.5454545454545*m.b560 + 9.09090909090909*m.b590 - m.x830 + m.x831 <= -33.8181818181818)

m.c81 = Constraint(expr= - 3.16363636363636*m.x91 - 3.16363636363636*m.x92 - 3.16363636363636*m.x93
                         + 22.5454545454545*m.b561 + 9.09090909090909*m.b591 - m.x831 + m.x832 <= -33.8181818181818)

m.c82 = Constraint(expr= - 3.16363636363636*m.x94 - 3.16363636363636*m.x95 - 3.16363636363636*m.x96
                         + 22.5454545454545*m.b562 + 9.09090909090909*m.b592 - m.x832 + m.x833 <= -33.8181818181818)

m.c83 = Constraint(expr= - 3.16363636363636*m.x97 - 3.16363636363636*m.x98 - 3.16363636363636*m.x99
                         + 22.5454545454545*m.b563 + 9.09090909090909*m.b593 - m.x833 + m.x834 <= -33.8181818181818)

m.c84 = Constraint(expr= - 3.16363636363636*m.x100 - 3.16363636363636*m.x101 - 3.16363636363636*m.x102
                         + 22.5454545454545*m.b564 + 9.09090909090909*m.b594 - m.x834 + m.x835 <= -33.8181818181818)

m.c85 = Constraint(expr= - 3.16363636363636*m.x103 - 3.16363636363636*m.x104 - 3.16363636363636*m.x105
                         + 22.5454545454545*m.b565 + 9.09090909090909*m.b595 - m.x835 + m.x836 <= -33.8181818181818)

m.c86 = Constraint(expr= - 3.16363636363636*m.x106 - 3.16363636363636*m.x107 - 3.16363636363636*m.x108
                         + 22.5454545454545*m.b566 + 9.09090909090909*m.b596 - m.x836 + m.x837 <= -33.8181818181818)

m.c87 = Constraint(expr= - 3.16363636363636*m.x109 - 3.16363636363636*m.x110 - 3.16363636363636*m.x111
                         + 22.5454545454545*m.b567 + 9.09090909090909*m.b597 - m.x837 + m.x838 <= -33.8181818181818)

m.c88 = Constraint(expr= - 3.16363636363636*m.x112 - 3.16363636363636*m.x113 - 3.16363636363636*m.x114
                         + 22.5454545454545*m.b568 + 9.09090909090909*m.b598 - m.x838 + m.x839 <= -33.8181818181818)

m.c89 = Constraint(expr= - 3.16363636363636*m.x115 - 3.16363636363636*m.x116 - 3.16363636363636*m.x117
                         + 22.5454545454545*m.b569 + 9.09090909090909*m.b599 - m.x839 + m.x840 <= -33.8181818181818)

m.c90 = Constraint(expr=-6.353*(0.001 + m.x1)**0.172*m.b541 + m.x211 <= 0)

m.c91 = Constraint(expr=-6.353*(0.001 + m.x2)**0.172*m.b542 + m.x214 <= 0)

m.c92 = Constraint(expr=-6.353*(0.001 + m.x3)**0.172*m.b543 + m.x217 <= 0)

m.c93 = Constraint(expr=-6.353*(0.001 + m.x4)**0.172*m.b544 + m.x220 <= 0)

m.c94 = Constraint(expr=-6.353*(0.001 + m.x5)**0.172*m.b545 + m.x223 <= 0)

m.c95 = Constraint(expr=-6.353*(0.001 + m.x6)**0.172*m.b546 + m.x226 <= 0)

m.c96 = Constraint(expr=-6.353*(0.001 + m.x7)**0.172*m.b547 + m.x229 <= 0)

m.c97 = Constraint(expr=-6.353*(0.001 + m.x8)**0.172*m.b548 + m.x232 <= 0)

m.c98 = Constraint(expr=-6.353*(0.001 + m.x9)**0.172*m.b549 + m.x235 <= 0)

m.c99 = Constraint(expr=-6.353*(0.001 + m.x10)**0.172*m.b550 + m.x238 <= 0)

m.c100 = Constraint(expr=-6.353*(0.001 + m.x11)**0.172*m.b551 + m.x241 <= 0)

m.c101 = Constraint(expr=-6.353*(0.001 + m.x12)**0.172*m.b552 + m.x244 <= 0)

m.c102 = Constraint(expr=-6.353*(0.001 + m.x13)**0.172*m.b553 + m.x247 <= 0)

m.c103 = Constraint(expr=-6.353*(0.001 + m.x14)**0.172*m.b554 + m.x250 <= 0)

m.c104 = Constraint(expr=-6.353*(0.001 + m.x15)**0.172*m.b555 + m.x253 <= 0)

m.c105 = Constraint(expr=-6.353*(0.001 + m.x16)**0.172*m.b556 + m.x256 <= 0)

m.c106 = Constraint(expr=-6.353*(0.001 + m.x17)**0.172*m.b557 + m.x259 <= 0)

m.c107 = Constraint(expr=-6.353*(0.001 + m.x18)**0.172*m.b558 + m.x262 <= 0)

m.c108 = Constraint(expr=-6.353*(0.001 + m.x19)**0.172*m.b559 + m.x265 <= 0)

m.c109 = Constraint(expr=-6.353*(0.001 + m.x20)**0.172*m.b560 + m.x268 <= 0)

m.c110 = Constraint(expr=-6.353*(0.001 + m.x21)**0.172*m.b561 + m.x271 <= 0)

m.c111 = Constraint(expr=-6.353*(0.001 + m.x22)**0.172*m.b562 + m.x274 <= 0)

m.c112 = Constraint(expr=-6.353*(0.001 + m.x23)**0.172*m.b563 + m.x277 <= 0)

m.c113 = Constraint(expr=-6.353*(0.001 + m.x24)**0.172*m.b564 + m.x280 <= 0)

m.c114 = Constraint(expr=-6.353*(0.001 + m.x25)**0.172*m.b565 + m.x283 <= 0)

m.c115 = Constraint(expr=-6.353*(0.001 + m.x26)**0.172*m.b566 + m.x286 <= 0)

m.c116 = Constraint(expr=-6.353*(0.001 + m.x27)**0.172*m.b567 + m.x289 <= 0)

m.c117 = Constraint(expr=-6.353*(0.001 + m.x28)**0.172*m.b568 + m.x292 <= 0)

m.c118 = Constraint(expr=-6.353*(0.001 + m.x29)**0.172*m.b569 + m.x295 <= 0)

m.c119 = Constraint(expr=-6.353*(0.001 + m.x30)**0.172*m.b570 + m.x298 <= 0)

m.c120 = Constraint(expr=-6.353*(0.001 + m.x1)**0.172*m.b571 + m.x212 <= 0)

m.c121 = Constraint(expr=-6.353*(0.001 + m.x2)**0.172*m.b572 + m.x215 <= 0)

m.c122 = Constraint(expr=-6.353*(0.001 + m.x3)**0.172*m.b573 + m.x218 <= 0)

m.c123 = Constraint(expr=-6.353*(0.001 + m.x4)**0.172*m.b574 + m.x221 <= 0)

m.c124 = Constraint(expr=-6.353*(0.001 + m.x5)**0.172*m.b575 + m.x224 <= 0)

m.c125 = Constraint(expr=-6.353*(0.001 + m.x6)**0.172*m.b576 + m.x227 <= 0)

m.c126 = Constraint(expr=-6.353*(0.001 + m.x7)**0.172*m.b577 + m.x230 <= 0)

m.c127 = Constraint(expr=-6.353*(0.001 + m.x8)**0.172*m.b578 + m.x233 <= 0)

m.c128 = Constraint(expr=-6.353*(0.001 + m.x9)**0.172*m.b579 + m.x236 <= 0)

m.c129 = Constraint(expr=-6.353*(0.001 + m.x10)**0.172*m.b580 + m.x239 <= 0)

m.c130 = Constraint(expr=-6.353*(0.001 + m.x11)**0.172*m.b581 + m.x242 <= 0)

m.c131 = Constraint(expr=-6.353*(0.001 + m.x12)**0.172*m.b582 + m.x245 <= 0)

m.c132 = Constraint(expr=-6.353*(0.001 + m.x13)**0.172*m.b583 + m.x248 <= 0)

m.c133 = Constraint(expr=-6.353*(0.001 + m.x14)**0.172*m.b584 + m.x251 <= 0)

m.c134 = Constraint(expr=-6.353*(0.001 + m.x15)**0.172*m.b585 + m.x254 <= 0)

m.c135 = Constraint(expr=-6.353*(0.001 + m.x16)**0.172*m.b586 + m.x257 <= 0)

m.c136 = Constraint(expr=-6.353*(0.001 + m.x17)**0.172*m.b587 + m.x260 <= 0)

m.c137 = Constraint(expr=-6.353*(0.001 + m.x18)**0.172*m.b588 + m.x263 <= 0)

m.c138 = Constraint(expr=-6.353*(0.001 + m.x19)**0.172*m.b589 + m.x266 <= 0)

m.c139 = Constraint(expr=-6.353*(0.001 + m.x20)**0.172*m.b590 + m.x269 <= 0)

m.c140 = Constraint(expr=-6.353*(0.001 + m.x21)**0.172*m.b591 + m.x272 <= 0)

m.c141 = Constraint(expr=-6.353*(0.001 + m.x22)**0.172*m.b592 + m.x275 <= 0)

m.c142 = Constraint(expr=-6.353*(0.001 + m.x23)**0.172*m.b593 + m.x278 <= 0)

m.c143 = Constraint(expr=-6.353*(0.001 + m.x24)**0.172*m.b594 + m.x281 <= 0)

m.c144 = Constraint(expr=-6.353*(0.001 + m.x25)**0.172*m.b595 + m.x284 <= 0)

m.c145 = Constraint(expr=-6.353*(0.001 + m.x26)**0.172*m.b596 + m.x287 <= 0)

m.c146 = Constraint(expr=-6.353*(0.001 + m.x27)**0.172*m.b597 + m.x290 <= 0)

m.c147 = Constraint(expr=-6.353*(0.001 + m.x28)**0.172*m.b598 + m.x293 <= 0)

m.c148 = Constraint(expr=-6.353*(0.001 + m.x29)**0.172*m.b599 + m.x296 <= 0)

m.c149 = Constraint(expr=-6.353*(0.001 + m.x30)**0.172*m.b600 + m.x299 <= 0)

m.c150 = Constraint(expr=-6.353*(0.001 + m.x1)**0.172*m.b601 + m.x213 <= 0)

m.c151 = Constraint(expr=-6.353*(0.001 + m.x2)**0.172*m.b602 + m.x216 <= 0)

m.c152 = Constraint(expr=-6.353*(0.001 + m.x3)**0.172*m.b603 + m.x219 <= 0)

m.c153 = Constraint(expr=-6.353*(0.001 + m.x4)**0.172*m.b604 + m.x222 <= 0)

m.c154 = Constraint(expr=-6.353*(0.001 + m.x5)**0.172*m.b605 + m.x225 <= 0)

m.c155 = Constraint(expr=-6.353*(0.001 + m.x6)**0.172*m.b606 + m.x228 <= 0)

m.c156 = Constraint(expr=-6.353*(0.001 + m.x7)**0.172*m.b607 + m.x231 <= 0)

m.c157 = Constraint(expr=-6.353*(0.001 + m.x8)**0.172*m.b608 + m.x234 <= 0)

m.c158 = Constraint(expr=-6.353*(0.001 + m.x9)**0.172*m.b609 + m.x237 <= 0)

m.c159 = Constraint(expr=-6.353*(0.001 + m.x10)**0.172*m.b610 + m.x240 <= 0)

m.c160 = Constraint(expr=-6.353*(0.001 + m.x11)**0.172*m.b611 + m.x243 <= 0)

m.c161 = Constraint(expr=-6.353*(0.001 + m.x12)**0.172*m.b612 + m.x246 <= 0)

m.c162 = Constraint(expr=-6.353*(0.001 + m.x13)**0.172*m.b613 + m.x249 <= 0)

m.c163 = Constraint(expr=-6.353*(0.001 + m.x14)**0.172*m.b614 + m.x252 <= 0)

m.c164 = Constraint(expr=-6.353*(0.001 + m.x15)**0.172*m.b615 + m.x255 <= 0)

m.c165 = Constraint(expr=-6.353*(0.001 + m.x16)**0.172*m.b616 + m.x258 <= 0)

m.c166 = Constraint(expr=-6.353*(0.001 + m.x17)**0.172*m.b617 + m.x261 <= 0)

m.c167 = Constraint(expr=-6.353*(0.001 + m.x18)**0.172*m.b618 + m.x264 <= 0)

m.c168 = Constraint(expr=-6.353*(0.001 + m.x19)**0.172*m.b619 + m.x267 <= 0)

m.c169 = Constraint(expr=-6.353*(0.001 + m.x20)**0.172*m.b620 + m.x270 <= 0)

m.c170 = Constraint(expr=-6.353*(0.001 + m.x21)**0.172*m.b621 + m.x273 <= 0)

m.c171 = Constraint(expr=-6.353*(0.001 + m.x22)**0.172*m.b622 + m.x276 <= 0)

m.c172 = Constraint(expr=-6.353*(0.001 + m.x23)**0.172*m.b623 + m.x279 <= 0)

m.c173 = Constraint(expr=-6.353*(0.001 + m.x24)**0.172*m.b624 + m.x282 <= 0)

m.c174 = Constraint(expr=-6.353*(0.001 + m.x25)**0.172*m.b625 + m.x285 <= 0)

m.c175 = Constraint(expr=-6.353*(0.001 + m.x26)**0.172*m.b626 + m.x288 <= 0)

m.c176 = Constraint(expr=-6.353*(0.001 + m.x27)**0.172*m.b627 + m.x291 <= 0)

m.c177 = Constraint(expr=-6.353*(0.001 + m.x28)**0.172*m.b628 + m.x294 <= 0)

m.c178 = Constraint(expr=-6.353*(0.001 + m.x29)**0.172*m.b629 + m.x297 <= 0)

m.c179 = Constraint(expr=-6.353*(0.001 + m.x30)**0.172*m.b630 + m.x300 <= 0)

m.c180 = Constraint(expr=-0.32*(0.001 + m.x1)**0.617*m.b541 + m.x301 <= 0)

m.c181 = Constraint(expr=-0.32*(0.001 + m.x2)**0.617*m.b542 + m.x304 <= 0)

m.c182 = Constraint(expr=-0.32*(0.001 + m.x3)**0.617*m.b543 + m.x307 <= 0)

m.c183 = Constraint(expr=-0.32*(0.001 + m.x4)**0.617*m.b544 + m.x310 <= 0)

m.c184 = Constraint(expr=-0.32*(0.001 + m.x5)**0.617*m.b545 + m.x313 <= 0)

m.c185 = Constraint(expr=-0.32*(0.001 + m.x6)**0.617*m.b546 + m.x316 <= 0)

m.c186 = Constraint(expr=-0.32*(0.001 + m.x7)**0.617*m.b547 + m.x319 <= 0)

m.c187 = Constraint(expr=-0.32*(0.001 + m.x8)**0.617*m.b548 + m.x322 <= 0)

m.c188 = Constraint(expr=-0.32*(0.001 + m.x9)**0.617*m.b549 + m.x325 <= 0)

m.c189 = Constraint(expr=-0.32*(0.001 + m.x10)**0.617*m.b550 + m.x328 <= 0)

m.c190 = Constraint(expr=-0.32*(0.001 + m.x11)**0.617*m.b551 + m.x331 <= 0)

m.c191 = Constraint(expr=-0.32*(0.001 + m.x12)**0.617*m.b552 + m.x334 <= 0)

m.c192 = Constraint(expr=-0.32*(0.001 + m.x13)**0.617*m.b553 + m.x337 <= 0)

m.c193 = Constraint(expr=-0.32*(0.001 + m.x14)**0.617*m.b554 + m.x340 <= 0)

m.c194 = Constraint(expr=-0.32*(0.001 + m.x15)**0.617*m.b555 + m.x343 <= 0)

m.c195 = Constraint(expr=-0.32*(0.001 + m.x16)**0.617*m.b556 + m.x346 <= 0)

m.c196 = Constraint(expr=-0.32*(0.001 + m.x17)**0.617*m.b557 + m.x349 <= 0)

m.c197 = Constraint(expr=-0.32*(0.001 + m.x18)**0.617*m.b558 + m.x352 <= 0)

m.c198 = Constraint(expr=-0.32*(0.001 + m.x19)**0.617*m.b559 + m.x355 <= 0)

m.c199 = Constraint(expr=-0.32*(0.001 + m.x20)**0.617*m.b560 + m.x358 <= 0)

m.c200 = Constraint(expr=-0.32*(0.001 + m.x21)**0.617*m.b561 + m.x361 <= 0)

m.c201 = Constraint(expr=-0.32*(0.001 + m.x22)**0.617*m.b562 + m.x364 <= 0)

m.c202 = Constraint(expr=-0.32*(0.001 + m.x23)**0.617*m.b563 + m.x367 <= 0)

m.c203 = Constraint(expr=-0.32*(0.001 + m.x24)**0.617*m.b564 + m.x370 <= 0)

m.c204 = Constraint(expr=-0.32*(0.001 + m.x25)**0.617*m.b565 + m.x373 <= 0)

m.c205 = Constraint(expr=-0.32*(0.001 + m.x26)**0.617*m.b566 + m.x376 <= 0)

m.c206 = Constraint(expr=-0.32*(0.001 + m.x27)**0.617*m.b567 + m.x379 <= 0)

m.c207 = Constraint(expr=-0.32*(0.001 + m.x28)**0.617*m.b568 + m.x382 <= 0)

m.c208 = Constraint(expr=-0.32*(0.001 + m.x29)**0.617*m.b569 + m.x385 <= 0)

m.c209 = Constraint(expr=-0.32*(0.001 + m.x30)**0.617*m.b570 + m.x388 <= 0)

m.c210 = Constraint(expr=-0.32*(0.001 + m.x1)**0.617*m.b571 + m.x302 <= 0)

m.c211 = Constraint(expr=-0.32*(0.001 + m.x2)**0.617*m.b572 + m.x305 <= 0)

m.c212 = Constraint(expr=-0.32*(0.001 + m.x3)**0.617*m.b573 + m.x308 <= 0)

m.c213 = Constraint(expr=-0.32*(0.001 + m.x4)**0.617*m.b574 + m.x311 <= 0)

m.c214 = Constraint(expr=-0.32*(0.001 + m.x5)**0.617*m.b575 + m.x314 <= 0)

m.c215 = Constraint(expr=-0.32*(0.001 + m.x6)**0.617*m.b576 + m.x317 <= 0)

m.c216 = Constraint(expr=-0.32*(0.001 + m.x7)**0.617*m.b577 + m.x320 <= 0)

m.c217 = Constraint(expr=-0.32*(0.001 + m.x8)**0.617*m.b578 + m.x323 <= 0)

m.c218 = Constraint(expr=-0.32*(0.001 + m.x9)**0.617*m.b579 + m.x326 <= 0)

m.c219 = Constraint(expr=-0.32*(0.001 + m.x10)**0.617*m.b580 + m.x329 <= 0)

m.c220 = Constraint(expr=-0.32*(0.001 + m.x11)**0.617*m.b581 + m.x332 <= 0)

m.c221 = Constraint(expr=-0.32*(0.001 + m.x12)**0.617*m.b582 + m.x335 <= 0)

m.c222 = Constraint(expr=-0.32*(0.001 + m.x13)**0.617*m.b583 + m.x338 <= 0)

m.c223 = Constraint(expr=-0.32*(0.001 + m.x14)**0.617*m.b584 + m.x341 <= 0)

m.c224 = Constraint(expr=-0.32*(0.001 + m.x15)**0.617*m.b585 + m.x344 <= 0)

m.c225 = Constraint(expr=-0.32*(0.001 + m.x16)**0.617*m.b586 + m.x347 <= 0)

m.c226 = Constraint(expr=-0.32*(0.001 + m.x17)**0.617*m.b587 + m.x350 <= 0)

m.c227 = Constraint(expr=-0.32*(0.001 + m.x18)**0.617*m.b588 + m.x353 <= 0)

m.c228 = Constraint(expr=-0.32*(0.001 + m.x19)**0.617*m.b589 + m.x356 <= 0)

m.c229 = Constraint(expr=-0.32*(0.001 + m.x20)**0.617*m.b590 + m.x359 <= 0)

m.c230 = Constraint(expr=-0.32*(0.001 + m.x21)**0.617*m.b591 + m.x362 <= 0)

m.c231 = Constraint(expr=-0.32*(0.001 + m.x22)**0.617*m.b592 + m.x365 <= 0)

m.c232 = Constraint(expr=-0.32*(0.001 + m.x23)**0.617*m.b593 + m.x368 <= 0)

m.c233 = Constraint(expr=-0.32*(0.001 + m.x24)**0.617*m.b594 + m.x371 <= 0)

m.c234 = Constraint(expr=-0.32*(0.001 + m.x25)**0.617*m.b595 + m.x374 <= 0)

m.c235 = Constraint(expr=-0.32*(0.001 + m.x26)**0.617*m.b596 + m.x377 <= 0)

m.c236 = Constraint(expr=-0.32*(0.001 + m.x27)**0.617*m.b597 + m.x380 <= 0)

m.c237 = Constraint(expr=-0.32*(0.001 + m.x28)**0.617*m.b598 + m.x383 <= 0)

m.c238 = Constraint(expr=-0.32*(0.001 + m.x29)**0.617*m.b599 + m.x386 <= 0)

m.c239 = Constraint(expr=-0.32*(0.001 + m.x30)**0.617*m.b600 + m.x389 <= 0)

m.c240 = Constraint(expr=-0.32*(0.001 + m.x1)**0.617*m.b601 + m.x303 <= 0)

m.c241 = Constraint(expr=-0.32*(0.001 + m.x2)**0.617*m.b602 + m.x306 <= 0)

m.c242 = Constraint(expr=-0.32*(0.001 + m.x3)**0.617*m.b603 + m.x309 <= 0)

m.c243 = Constraint(expr=-0.32*(0.001 + m.x4)**0.617*m.b604 + m.x312 <= 0)

m.c244 = Constraint(expr=-0.32*(0.001 + m.x5)**0.617*m.b605 + m.x315 <= 0)

m.c245 = Constraint(expr=-0.32*(0.001 + m.x6)**0.617*m.b606 + m.x318 <= 0)

m.c246 = Constraint(expr=-0.32*(0.001 + m.x7)**0.617*m.b607 + m.x321 <= 0)

m.c247 = Constraint(expr=-0.32*(0.001 + m.x8)**0.617*m.b608 + m.x324 <= 0)

m.c248 = Constraint(expr=-0.32*(0.001 + m.x9)**0.617*m.b609 + m.x327 <= 0)

m.c249 = Constraint(expr=-0.32*(0.001 + m.x10)**0.617*m.b610 + m.x330 <= 0)

m.c250 = Constraint(expr=-0.32*(0.001 + m.x11)**0.617*m.b611 + m.x333 <= 0)

m.c251 = Constraint(expr=-0.32*(0.001 + m.x12)**0.617*m.b612 + m.x336 <= 0)

m.c252 = Constraint(expr=-0.32*(0.001 + m.x13)**0.617*m.b613 + m.x339 <= 0)

m.c253 = Constraint(expr=-0.32*(0.001 + m.x14)**0.617*m.b614 + m.x342 <= 0)

m.c254 = Constraint(expr=-0.32*(0.001 + m.x15)**0.617*m.b615 + m.x345 <= 0)

m.c255 = Constraint(expr=-0.32*(0.001 + m.x16)**0.617*m.b616 + m.x348 <= 0)

m.c256 = Constraint(expr=-0.32*(0.001 + m.x17)**0.617*m.b617 + m.x351 <= 0)

m.c257 = Constraint(expr=-0.32*(0.001 + m.x18)**0.617*m.b618 + m.x354 <= 0)

m.c258 = Constraint(expr=-0.32*(0.001 + m.x19)**0.617*m.b619 + m.x357 <= 0)

m.c259 = Constraint(expr=-0.32*(0.001 + m.x20)**0.617*m.b620 + m.x360 <= 0)

m.c260 = Constraint(expr=-0.32*(0.001 + m.x21)**0.617*m.b621 + m.x363 <= 0)

m.c261 = Constraint(expr=-0.32*(0.001 + m.x22)**0.617*m.b622 + m.x366 <= 0)

m.c262 = Constraint(expr=-0.32*(0.001 + m.x23)**0.617*m.b623 + m.x369 <= 0)

m.c263 = Constraint(expr=-0.32*(0.001 + m.x24)**0.617*m.b624 + m.x372 <= 0)

m.c264 = Constraint(expr=-0.32*(0.001 + m.x25)**0.617*m.b625 + m.x375 <= 0)

m.c265 = Constraint(expr=-0.32*(0.001 + m.x26)**0.617*m.b626 + m.x378 <= 0)

m.c266 = Constraint(expr=-0.32*(0.001 + m.x27)**0.617*m.b627 + m.x381 <= 0)

m.c267 = Constraint(expr=-0.32*(0.001 + m.x28)**0.617*m.b628 + m.x384 <= 0)

m.c268 = Constraint(expr=-0.32*(0.001 + m.x29)**0.617*m.b629 + m.x387 <= 0)

m.c269 = Constraint(expr=-0.32*(0.001 + m.x30)**0.617*m.b630 + m.x390 <= 0)

m.c270 = Constraint(expr=   m.x31 + m.x121 - m.b541 <= 0)

m.c271 = Constraint(expr=   m.x34 + m.x124 - m.b542 <= 0)

m.c272 = Constraint(expr=   m.x37 + m.x127 - m.b543 <= 0)

m.c273 = Constraint(expr=   m.x40 + m.x130 - m.b544 <= 0)

m.c274 = Constraint(expr=   m.x43 + m.x133 - m.b545 <= 0)

m.c275 = Constraint(expr=   m.x46 + m.x136 - m.b546 <= 0)

m.c276 = Constraint(expr=   m.x49 + m.x139 - m.b547 <= 0)

m.c277 = Constraint(expr=   m.x52 + m.x142 - m.b548 <= 0)

m.c278 = Constraint(expr=   m.x55 + m.x145 - m.b549 <= 0)

m.c279 = Constraint(expr=   m.x58 + m.x148 - m.b550 <= 0)

m.c280 = Constraint(expr=   m.x61 + m.x151 - m.b551 <= 0)

m.c281 = Constraint(expr=   m.x64 + m.x154 - m.b552 <= 0)

m.c282 = Constraint(expr=   m.x67 + m.x157 - m.b553 <= 0)

m.c283 = Constraint(expr=   m.x70 + m.x160 - m.b554 <= 0)

m.c284 = Constraint(expr=   m.x73 + m.x163 - m.b555 <= 0)

m.c285 = Constraint(expr=   m.x76 + m.x166 - m.b556 <= 0)

m.c286 = Constraint(expr=   m.x79 + m.x169 - m.b557 <= 0)

m.c287 = Constraint(expr=   m.x82 + m.x172 - m.b558 <= 0)

m.c288 = Constraint(expr=   m.x85 + m.x175 - m.b559 <= 0)

m.c289 = Constraint(expr=   m.x88 + m.x178 - m.b560 <= 0)

m.c290 = Constraint(expr=   m.x91 + m.x181 - m.b561 <= 0)

m.c291 = Constraint(expr=   m.x94 + m.x184 - m.b562 <= 0)

m.c292 = Constraint(expr=   m.x97 + m.x187 - m.b563 <= 0)

m.c293 = Constraint(expr=   m.x100 + m.x190 - m.b564 <= 0)

m.c294 = Constraint(expr=   m.x103 + m.x193 - m.b565 <= 0)

m.c295 = Constraint(expr=   m.x106 + m.x196 - m.b566 <= 0)

m.c296 = Constraint(expr=   m.x109 + m.x199 - m.b567 <= 0)

m.c297 = Constraint(expr=   m.x112 + m.x202 - m.b568 <= 0)

m.c298 = Constraint(expr=   m.x115 + m.x205 - m.b569 <= 0)

m.c299 = Constraint(expr=   m.x118 + m.x208 - m.b570 <= 0)

m.c300 = Constraint(expr=   m.x32 + m.x122 - m.b571 <= 0)

m.c301 = Constraint(expr=   m.x35 + m.x125 - m.b572 <= 0)

m.c302 = Constraint(expr=   m.x38 + m.x128 - m.b573 <= 0)

m.c303 = Constraint(expr=   m.x41 + m.x131 - m.b574 <= 0)

m.c304 = Constraint(expr=   m.x44 + m.x134 - m.b575 <= 0)

m.c305 = Constraint(expr=   m.x47 + m.x137 - m.b576 <= 0)

m.c306 = Constraint(expr=   m.x50 + m.x140 - m.b577 <= 0)

m.c307 = Constraint(expr=   m.x53 + m.x143 - m.b578 <= 0)

m.c308 = Constraint(expr=   m.x56 + m.x146 - m.b579 <= 0)

m.c309 = Constraint(expr=   m.x59 + m.x149 - m.b580 <= 0)

m.c310 = Constraint(expr=   m.x62 + m.x152 - m.b581 <= 0)

m.c311 = Constraint(expr=   m.x65 + m.x155 - m.b582 <= 0)

m.c312 = Constraint(expr=   m.x68 + m.x158 - m.b583 <= 0)

m.c313 = Constraint(expr=   m.x71 + m.x161 - m.b584 <= 0)

m.c314 = Constraint(expr=   m.x74 + m.x164 - m.b585 <= 0)

m.c315 = Constraint(expr=   m.x77 + m.x167 - m.b586 <= 0)

m.c316 = Constraint(expr=   m.x80 + m.x170 - m.b587 <= 0)

m.c317 = Constraint(expr=   m.x83 + m.x173 - m.b588 <= 0)

m.c318 = Constraint(expr=   m.x86 + m.x176 - m.b589 <= 0)

m.c319 = Constraint(expr=   m.x89 + m.x179 - m.b590 <= 0)

m.c320 = Constraint(expr=   m.x92 + m.x182 - m.b591 <= 0)

m.c321 = Constraint(expr=   m.x95 + m.x185 - m.b592 <= 0)

m.c322 = Constraint(expr=   m.x98 + m.x188 - m.b593 <= 0)

m.c323 = Constraint(expr=   m.x101 + m.x191 - m.b594 <= 0)

m.c324 = Constraint(expr=   m.x104 + m.x194 - m.b595 <= 0)

m.c325 = Constraint(expr=   m.x107 + m.x197 - m.b596 <= 0)

m.c326 = Constraint(expr=   m.x110 + m.x200 - m.b597 <= 0)

m.c327 = Constraint(expr=   m.x113 + m.x203 - m.b598 <= 0)

m.c328 = Constraint(expr=   m.x116 + m.x206 - m.b599 <= 0)

m.c329 = Constraint(expr=   m.x119 + m.x209 - m.b600 <= 0)

m.c330 = Constraint(expr=   m.x33 + m.x123 - m.b601 <= 0)

m.c331 = Constraint(expr=   m.x36 + m.x126 - m.b602 <= 0)

m.c332 = Constraint(expr=   m.x39 + m.x129 - m.b603 <= 0)

m.c333 = Constraint(expr=   m.x42 + m.x132 - m.b604 <= 0)

m.c334 = Constraint(expr=   m.x45 + m.x135 - m.b605 <= 0)

m.c335 = Constraint(expr=   m.x48 + m.x138 - m.b606 <= 0)

m.c336 = Constraint(expr=   m.x51 + m.x141 - m.b607 <= 0)

m.c337 = Constraint(expr=   m.x54 + m.x144 - m.b608 <= 0)

m.c338 = Constraint(expr=   m.x57 + m.x147 - m.b609 <= 0)

m.c339 = Constraint(expr=   m.x60 + m.x150 - m.b610 <= 0)

m.c340 = Constraint(expr=   m.x63 + m.x153 - m.b611 <= 0)

m.c341 = Constraint(expr=   m.x66 + m.x156 - m.b612 <= 0)

m.c342 = Constraint(expr=   m.x69 + m.x159 - m.b613 <= 0)

m.c343 = Constraint(expr=   m.x72 + m.x162 - m.b614 <= 0)

m.c344 = Constraint(expr=   m.x75 + m.x165 - m.b615 <= 0)

m.c345 = Constraint(expr=   m.x78 + m.x168 - m.b616 <= 0)

m.c346 = Constraint(expr=   m.x81 + m.x171 - m.b617 <= 0)

m.c347 = Constraint(expr=   m.x84 + m.x174 - m.b618 <= 0)

m.c348 = Constraint(expr=   m.x87 + m.x177 - m.b619 <= 0)

m.c349 = Constraint(expr=   m.x90 + m.x180 - m.b620 <= 0)

m.c350 = Constraint(expr=   m.x93 + m.x183 - m.b621 <= 0)

m.c351 = Constraint(expr=   m.x96 + m.x186 - m.b622 <= 0)

m.c352 = Constraint(expr=   m.x99 + m.x189 - m.b623 <= 0)

m.c353 = Constraint(expr=   m.x102 + m.x192 - m.b624 <= 0)

m.c354 = Constraint(expr=   m.x105 + m.x195 - m.b625 <= 0)

m.c355 = Constraint(expr=   m.x108 + m.x198 - m.b626 <= 0)

m.c356 = Constraint(expr=   m.x111 + m.x201 - m.b627 <= 0)

m.c357 = Constraint(expr=   m.x114 + m.x204 - m.b628 <= 0)

m.c358 = Constraint(expr=   m.x117 + m.x207 - m.b629 <= 0)

m.c359 = Constraint(expr=   m.x120 + m.x210 - m.b630 <= 0)

m.c360 = Constraint(expr= - 200*m.b481 + m.x811 >= 0)

m.c361 = Constraint(expr= - 200*m.b482 + m.x812 >= 0)

m.c362 = Constraint(expr= - 200*m.b483 + m.x813 >= 0)

m.c363 = Constraint(expr= - 200*m.b484 + m.x814 >= 0)

m.c364 = Constraint(expr= - 200*m.b485 + m.x815 >= 0)

m.c365 = Constraint(expr= - 200*m.b486 + m.x816 >= 0)

m.c366 = Constraint(expr= - 200*m.b487 + m.x817 >= 0)

m.c367 = Constraint(expr= - 200*m.b488 + m.x818 >= 0)

m.c368 = Constraint(expr= - 200*m.b489 + m.x819 >= 0)

m.c369 = Constraint(expr= - 200*m.b490 + m.x820 >= 0)

m.c370 = Constraint(expr= - 200*m.b491 + m.x821 >= 0)

m.c371 = Constraint(expr= - 200*m.b492 + m.x822 >= 0)

m.c372 = Constraint(expr= - 200*m.b493 + m.x823 >= 0)

m.c373 = Constraint(expr= - 200*m.b494 + m.x824 >= 0)

m.c374 = Constraint(expr= - 200*m.b495 + m.x825 >= 0)

m.c375 = Constraint(expr= - 200*m.b496 + m.x826 >= 0)

m.c376 = Constraint(expr= - 200*m.b497 + m.x827 >= 0)

m.c377 = Constraint(expr= - 200*m.b498 + m.x828 >= 0)

m.c378 = Constraint(expr= - 200*m.b499 + m.x829 >= 0)

m.c379 = Constraint(expr= - 200*m.b500 + m.x830 >= 0)

m.c380 = Constraint(expr= - 200*m.b501 + m.x831 >= 0)

m.c381 = Constraint(expr= - 200*m.b502 + m.x832 >= 0)

m.c382 = Constraint(expr= - 200*m.b503 + m.x833 >= 0)

m.c383 = Constraint(expr= - 200*m.b504 + m.x834 >= 0)

m.c384 = Constraint(expr= - 200*m.b505 + m.x835 >= 0)

m.c385 = Constraint(expr= - 200*m.b506 + m.x836 >= 0)

m.c386 = Constraint(expr= - 200*m.b507 + m.x837 >= 0)

m.c387 = Constraint(expr= - 200*m.b508 + m.x838 >= 0)

m.c388 = Constraint(expr= - 200*m.b509 + m.x839 >= 0)

m.c389 = Constraint(expr= - 200*m.b510 + m.x840 >= 0)

m.c390 = Constraint(expr= - 200*m.b511 + m.x811 >= 0)

m.c391 = Constraint(expr= - 200*m.b512 + m.x812 >= 0)

m.c392 = Constraint(expr= - 200*m.b513 + m.x813 >= 0)

m.c393 = Constraint(expr= - 200*m.b514 + m.x814 >= 0)

m.c394 = Constraint(expr= - 200*m.b515 + m.x815 >= 0)

m.c395 = Constraint(expr= - 200*m.b516 + m.x816 >= 0)

m.c396 = Constraint(expr= - 200*m.b517 + m.x817 >= 0)

m.c397 = Constraint(expr= - 200*m.b518 + m.x818 >= 0)

m.c398 = Constraint(expr= - 200*m.b519 + m.x819 >= 0)

m.c399 = Constraint(expr= - 200*m.b520 + m.x820 >= 0)

m.c400 = Constraint(expr= - 200*m.b521 + m.x821 >= 0)

m.c401 = Constraint(expr= - 200*m.b522 + m.x822 >= 0)

m.c402 = Constraint(expr= - 200*m.b523 + m.x823 >= 0)

m.c403 = Constraint(expr= - 200*m.b524 + m.x824 >= 0)

m.c404 = Constraint(expr= - 200*m.b525 + m.x825 >= 0)

m.c405 = Constraint(expr= - 200*m.b526 + m.x826 >= 0)

m.c406 = Constraint(expr= - 200*m.b527 + m.x827 >= 0)

m.c407 = Constraint(expr= - 200*m.b528 + m.x828 >= 0)

m.c408 = Constraint(expr= - 200*m.b529 + m.x829 >= 0)

m.c409 = Constraint(expr= - 200*m.b530 + m.x830 >= 0)

m.c410 = Constraint(expr= - 200*m.b531 + m.x831 >= 0)

m.c411 = Constraint(expr= - 200*m.b532 + m.x832 >= 0)

m.c412 = Constraint(expr= - 200*m.b533 + m.x833 >= 0)

m.c413 = Constraint(expr= - 200*m.b534 + m.x834 >= 0)

m.c414 = Constraint(expr= - 200*m.b535 + m.x835 >= 0)

m.c415 = Constraint(expr= - 200*m.b536 + m.x836 >= 0)

m.c416 = Constraint(expr= - 200*m.b537 + m.x837 >= 0)

m.c417 = Constraint(expr= - 200*m.b538 + m.x838 >= 0)

m.c418 = Constraint(expr= - 200*m.b539 + m.x839 >= 0)

m.c419 = Constraint(expr= - 200*m.b540 + m.x840 >= 0)

m.c420 = Constraint(expr= - m.x391 + m.b481 == 0)

m.c421 = Constraint(expr= - m.x392 + m.b482 == 0)

m.c422 = Constraint(expr= - m.x393 + m.b483 == 0)

m.c423 = Constraint(expr= - m.x394 + m.b484 == 0)

m.c424 = Constraint(expr= - m.x395 + m.b485 == 0)

m.c425 = Constraint(expr= - m.x396 + m.b486 == 0)

m.c426 = Constraint(expr= - m.x397 + m.b487 == 0)

m.c427 = Constraint(expr= - m.x398 + m.b488 == 0)

m.c428 = Constraint(expr= - m.x399 + m.b489 == 0)

m.c429 = Constraint(expr= - m.x400 + m.b490 == 0)

m.c430 = Constraint(expr= - m.x401 + m.b491 == 0)

m.c431 = Constraint(expr= - m.x402 + m.b492 == 0)

m.c432 = Constraint(expr= - m.x403 + m.b493 == 0)

m.c433 = Constraint(expr= - m.x404 + m.b494 == 0)

m.c434 = Constraint(expr= - m.x405 + m.b495 == 0)

m.c435 = Constraint(expr= - m.x406 + m.b496 == 0)

m.c436 = Constraint(expr= - m.x407 + m.b497 == 0)

m.c437 = Constraint(expr= - m.x408 + m.b498 == 0)

m.c438 = Constraint(expr= - m.x409 + m.b499 == 0)

m.c439 = Constraint(expr= - m.x410 + m.b500 == 0)

m.c440 = Constraint(expr= - m.x411 + m.b501 == 0)

m.c441 = Constraint(expr= - m.x412 + m.b502 == 0)

m.c442 = Constraint(expr= - m.x413 + m.b503 == 0)

m.c443 = Constraint(expr= - m.x414 + m.b504 == 0)

m.c444 = Constraint(expr= - m.x415 + m.b505 == 0)

m.c445 = Constraint(expr= - m.x416 + m.b506 == 0)

m.c446 = Constraint(expr= - m.x417 + m.b507 == 0)

m.c447 = Constraint(expr= - m.x418 + m.b508 == 0)

m.c448 = Constraint(expr= - m.x419 + m.b509 == 0)

m.c449 = Constraint(expr= - m.x420 + m.b510 == 0)

m.c450 = Constraint(expr= - m.x421 + m.b511 == 0)

m.c451 = Constraint(expr= - m.x422 + m.b512 == 0)

m.c452 = Constraint(expr= - m.x423 + m.b513 == 0)

m.c453 = Constraint(expr= - m.x424 + m.b514 == 0)

m.c454 = Constraint(expr= - m.x425 + m.b515 == 0)

m.c455 = Constraint(expr= - m.x426 + m.b516 == 0)

m.c456 = Constraint(expr= - m.x427 + m.b517 == 0)

m.c457 = Constraint(expr= - m.x428 + m.b518 == 0)

m.c458 = Constraint(expr= - m.x429 + m.b519 == 0)

m.c459 = Constraint(expr= - m.x430 + m.b520 == 0)

m.c460 = Constraint(expr= - m.x431 + m.b521 == 0)

m.c461 = Constraint(expr= - m.x432 + m.b522 == 0)

m.c462 = Constraint(expr= - m.x433 + m.b523 == 0)

m.c463 = Constraint(expr= - m.x434 + m.b524 == 0)

m.c464 = Constraint(expr= - m.x435 + m.b525 == 0)

m.c465 = Constraint(expr= - m.x436 + m.b526 == 0)

m.c466 = Constraint(expr= - m.x437 + m.b527 == 0)

m.c467 = Constraint(expr= - m.x438 + m.b528 == 0)

m.c468 = Constraint(expr= - m.x439 + m.b529 == 0)

m.c469 = Constraint(expr= - m.x440 + m.b530 == 0)

m.c470 = Constraint(expr= - m.x441 + m.b531 == 0)

m.c471 = Constraint(expr= - m.x442 + m.b532 == 0)

m.c472 = Constraint(expr= - m.x443 + m.b533 == 0)

m.c473 = Constraint(expr= - m.x444 + m.b534 == 0)

m.c474 = Constraint(expr= - m.x445 + m.b535 == 0)

m.c475 = Constraint(expr= - m.x446 + m.b536 == 0)

m.c476 = Constraint(expr= - m.x447 + m.b537 == 0)

m.c477 = Constraint(expr= - m.x448 + m.b538 == 0)

m.c478 = Constraint(expr= - m.x449 + m.b539 == 0)

m.c479 = Constraint(expr= - m.x450 + m.b540 == 0)

m.c480 = Constraint(expr=   200*m.b451 + m.x811 >= 200)

m.c481 = Constraint(expr=   200*m.b452 + m.x812 >= 200)

m.c482 = Constraint(expr=   200*m.b453 + m.x813 >= 200)

m.c483 = Constraint(expr=   200*m.b454 + m.x814 >= 200)

m.c484 = Constraint(expr=   200*m.b455 + m.x815 >= 200)

m.c485 = Constraint(expr=   200*m.b456 + m.x816 >= 200)

m.c486 = Constraint(expr=   200*m.b457 + m.x817 >= 200)

m.c487 = Constraint(expr=   200*m.b458 + m.x818 >= 200)

m.c488 = Constraint(expr=   200*m.b459 + m.x819 >= 200)

m.c489 = Constraint(expr=   200*m.b460 + m.x820 >= 200)

m.c490 = Constraint(expr=   200*m.b461 + m.x821 >= 200)

m.c491 = Constraint(expr=   200*m.b462 + m.x822 >= 200)

m.c492 = Constraint(expr=   200*m.b463 + m.x823 >= 200)

m.c493 = Constraint(expr=   200*m.b464 + m.x824 >= 200)

m.c494 = Constraint(expr=   200*m.b465 + m.x825 >= 200)

m.c495 = Constraint(expr=   200*m.b466 + m.x826 >= 200)

m.c496 = Constraint(expr=   200*m.b467 + m.x827 >= 200)

m.c497 = Constraint(expr=   200*m.b468 + m.x828 >= 200)

m.c498 = Constraint(expr=   200*m.b469 + m.x829 >= 200)

m.c499 = Constraint(expr=   200*m.b470 + m.x830 >= 200)

m.c500 = Constraint(expr=   200*m.b471 + m.x831 >= 200)

m.c501 = Constraint(expr=   200*m.b472 + m.x832 >= 200)

m.c502 = Constraint(expr=   200*m.b473 + m.x833 >= 200)

m.c503 = Constraint(expr=   200*m.b474 + m.x834 >= 200)

m.c504 = Constraint(expr=   200*m.b475 + m.x835 >= 200)

m.c505 = Constraint(expr=   200*m.b476 + m.x836 >= 200)

m.c506 = Constraint(expr=   200*m.b477 + m.x837 >= 200)

m.c507 = Constraint(expr=   200*m.b478 + m.x838 >= 200)

m.c508 = Constraint(expr=   200*m.b479 + m.x839 >= 200)

m.c509 = Constraint(expr=   200*m.b480 + m.x840 >= 200)

m.c510 = Constraint(expr= - 1011*m.b451 - m.x811 >= -1211)

m.c511 = Constraint(expr= - 980.345454545454*m.b452 - m.x812 >= -1180.34545454545)

m.c512 = Constraint(expr= - 949.690909090909*m.b453 - m.x813 >= -1149.69090909091)

m.c513 = Constraint(expr= - 919.036363636363*m.b454 - m.x814 >= -1119.03636363636)

m.c514 = Constraint(expr= - 888.381818181818*m.b455 - m.x815 >= -1088.38181818182)

m.c515 = Constraint(expr= - 857.727272727272*m.b456 - m.x816 >= -1057.72727272727)

m.c516 = Constraint(expr= - 827.072727272727*m.b457 - m.x817 >= -1027.07272727273)

m.c517 = Constraint(expr= - 796.418181818181*m.b458 - m.x818 >= -996.418181818181)

m.c518 = Constraint(expr= - 765.763636363636*m.b459 - m.x819 >= -965.763636363636)

m.c519 = Constraint(expr= - 735.10909090909*m.b460 - m.x820 >= -935.10909090909)

m.c520 = Constraint(expr= - 704.454545454545*m.b461 - m.x821 >= -904.454545454545)

m.c521 = Constraint(expr= - 673.8*m.b462 - m.x822 >= -873.8)

m.c522 = Constraint(expr= - 643.145454545454*m.b463 - m.x823 >= -843.145454545454)

m.c523 = Constraint(expr= - 612.490909090909*m.b464 - m.x824 >= -812.490909090909)

m.c524 = Constraint(expr= - 581.836363636363*m.b465 - m.x825 >= -781.836363636363)

m.c525 = Constraint(expr= - 551.181818181818*m.b466 - m.x826 >= -751.181818181818)

m.c526 = Constraint(expr= - 520.527272727272*m.b467 - m.x827 >= -720.527272727272)

m.c527 = Constraint(expr= - 489.872727272727*m.b468 - m.x828 >= -689.872727272727)

m.c528 = Constraint(expr= - 459.218181818182*m.b469 - m.x829 >= -659.218181818182)

m.c529 = Constraint(expr= - 428.563636363636*m.b470 - m.x830 >= -628.563636363636)

m.c530 = Constraint(expr= - 397.909090909091*m.b471 - m.x831 >= -597.909090909091)

m.c531 = Constraint(expr= - 367.254545454545*m.b472 - m.x832 >= -567.254545454545)

m.c532 = Constraint(expr= - 336.6*m.b473 - m.x833 >= -536.6)

m.c533 = Constraint(expr= - 305.945454545454*m.b474 - m.x834 >= -505.945454545454)

m.c534 = Constraint(expr= - 275.290909090909*m.b475 - m.x835 >= -475.290909090909)

m.c535 = Constraint(expr= - 244.636363636364*m.b476 - m.x836 >= -444.636363636364)

m.c536 = Constraint(expr= - 213.981818181818*m.b477 - m.x837 >= -413.981818181818)

m.c537 = Constraint(expr= - 183.327272727273*m.b478 - m.x838 >= -383.327272727273)

m.c538 = Constraint(expr= - 152.672727272727*m.b479 - m.x839 >= -352.672727272727)

m.c539 = Constraint(expr= - 122.018181818182*m.b480 - m.x840 >= -322.018181818182)

m.c540 = Constraint(expr=   m.x1 - m.x811 <= 0)

m.c541 = Constraint(expr=   m.x2 - m.x812 <= 0)

m.c542 = Constraint(expr=   m.x3 - m.x813 <= 0)

m.c543 = Constraint(expr=   m.x4 - m.x814 <= 0)

m.c544 = Constraint(expr=   m.x5 - m.x815 <= 0)

m.c545 = Constraint(expr=   m.x6 - m.x816 <= 0)

m.c546 = Constraint(expr=   m.x7 - m.x817 <= 0)

m.c547 = Constraint(expr=   m.x8 - m.x818 <= 0)

m.c548 = Constraint(expr=   m.x9 - m.x819 <= 0)

m.c549 = Constraint(expr=   m.x10 - m.x820 <= 0)

m.c550 = Constraint(expr=   m.x11 - m.x821 <= 0)

m.c551 = Constraint(expr=   m.x12 - m.x822 <= 0)

m.c552 = Constraint(expr=   m.x13 - m.x823 <= 0)

m.c553 = Constraint(expr=   m.x14 - m.x824 <= 0)

m.c554 = Constraint(expr=   m.x15 - m.x825 <= 0)

m.c555 = Constraint(expr=   m.x16 - m.x826 <= 0)

m.c556 = Constraint(expr=   m.x17 - m.x827 <= 0)

m.c557 = Constraint(expr=   m.x18 - m.x828 <= 0)

m.c558 = Constraint(expr=   m.x19 - m.x829 <= 0)

m.c559 = Constraint(expr=   m.x20 - m.x830 <= 0)

m.c560 = Constraint(expr=   m.x21 - m.x831 <= 0)

m.c561 = Constraint(expr=   m.x22 - m.x832 <= 0)

m.c562 = Constraint(expr=   m.x23 - m.x833 <= 0)

m.c563 = Constraint(expr=   m.x24 - m.x834 <= 0)

m.c564 = Constraint(expr=   m.x25 - m.x835 <= 0)

m.c565 = Constraint(expr=   m.x26 - m.x836 <= 0)

m.c566 = Constraint(expr=   m.x27 - m.x837 <= 0)

m.c567 = Constraint(expr=   m.x28 - m.x838 <= 0)

m.c568 = Constraint(expr=   m.x29 - m.x839 <= 0)

m.c569 = Constraint(expr=   m.x30 - m.x840 <= 0)

m.c570 = Constraint(expr=   m.x1 + 1211*m.b451 <= 1211)

m.c571 = Constraint(expr=   m.x2 + 1180.34545454545*m.b452 <= 1180.34545454545)

m.c572 = Constraint(expr=   m.x3 + 1149.69090909091*m.b453 <= 1149.69090909091)

m.c573 = Constraint(expr=   m.x4 + 1119.03636363636*m.b454 <= 1119.03636363636)

m.c574 = Constraint(expr=   m.x5 + 1088.38181818182*m.b455 <= 1088.38181818182)

m.c575 = Constraint(expr=   m.x6 + 1057.72727272727*m.b456 <= 1057.72727272727)

m.c576 = Constraint(expr=   m.x7 + 1027.07272727273*m.b457 <= 1027.07272727273)

m.c577 = Constraint(expr=   m.x8 + 996.418181818181*m.b458 <= 996.418181818181)

m.c578 = Constraint(expr=   m.x9 + 965.763636363636*m.b459 <= 965.763636363636)

m.c579 = Constraint(expr=   m.x10 + 935.10909090909*m.b460 <= 935.10909090909)

m.c580 = Constraint(expr=   m.x11 + 904.454545454545*m.b461 <= 904.454545454545)

m.c581 = Constraint(expr=   m.x12 + 873.8*m.b462 <= 873.8)

m.c582 = Constraint(expr=   m.x13 + 843.145454545454*m.b463 <= 843.145454545454)

m.c583 = Constraint(expr=   m.x14 + 812.490909090909*m.b464 <= 812.490909090909)

m.c584 = Constraint(expr=   m.x15 + 781.836363636363*m.b465 <= 781.836363636363)

m.c585 = Constraint(expr=   m.x16 + 751.181818181818*m.b466 <= 751.181818181818)

m.c586 = Constraint(expr=   m.x17 + 720.527272727272*m.b467 <= 720.527272727272)

m.c587 = Constraint(expr=   m.x18 + 689.872727272727*m.b468 <= 689.872727272727)

m.c588 = Constraint(expr=   m.x19 + 659.218181818182*m.b469 <= 659.218181818182)

m.c589 = Constraint(expr=   m.x20 + 628.563636363636*m.b470 <= 628.563636363636)

m.c590 = Constraint(expr=   m.x21 + 597.909090909091*m.b471 <= 597.909090909091)

m.c591 = Constraint(expr=   m.x22 + 567.254545454545*m.b472 <= 567.254545454545)

m.c592 = Constraint(expr=   m.x23 + 536.6*m.b473 <= 536.6)

m.c593 = Constraint(expr=   m.x24 + 505.945454545454*m.b474 <= 505.945454545454)

m.c594 = Constraint(expr=   m.x25 + 475.290909090909*m.b475 <= 475.290909090909)

m.c595 = Constraint(expr=   m.x26 + 444.636363636364*m.b476 <= 444.636363636364)

m.c596 = Constraint(expr=   m.x27 + 413.981818181818*m.b477 <= 413.981818181818)

m.c597 = Constraint(expr=   m.x28 + 383.327272727273*m.b478 <= 383.327272727273)

m.c598 = Constraint(expr=   m.x29 + 352.672727272727*m.b479 <= 352.672727272727)

m.c599 = Constraint(expr=   m.x30 + 322.018181818182*m.b480 <= 322.018181818182)

m.c600 = Constraint(expr=   m.x1 + 1211*m.b451 - m.x811 >= 0)

m.c601 = Constraint(expr=   m.x2 + 1180.34545454545*m.b452 - m.x812 >= 0)

m.c602 = Constraint(expr=   m.x3 + 1149.69090909091*m.b453 - m.x813 >= 0)

m.c603 = Constraint(expr=   m.x4 + 1119.03636363636*m.b454 - m.x814 >= 0)

m.c604 = Constraint(expr=   m.x5 + 1088.38181818182*m.b455 - m.x815 >= 0)

m.c605 = Constraint(expr=   m.x6 + 1057.72727272727*m.b456 - m.x816 >= 0)

m.c606 = Constraint(expr=   m.x7 + 1027.07272727273*m.b457 - m.x817 >= 0)

m.c607 = Constraint(expr=   m.x8 + 996.418181818181*m.b458 - m.x818 >= 0)

m.c608 = Constraint(expr=   m.x9 + 965.763636363636*m.b459 - m.x819 >= 0)

m.c609 = Constraint(expr=   m.x10 + 935.10909090909*m.b460 - m.x820 >= 0)

m.c610 = Constraint(expr=   m.x11 + 904.454545454545*m.b461 - m.x821 >= 0)

m.c611 = Constraint(expr=   m.x12 + 873.8*m.b462 - m.x822 >= 0)

m.c612 = Constraint(expr=   m.x13 + 843.145454545454*m.b463 - m.x823 >= 0)

m.c613 = Constraint(expr=   m.x14 + 812.490909090909*m.b464 - m.x824 >= 0)

m.c614 = Constraint(expr=   m.x15 + 781.836363636363*m.b465 - m.x825 >= 0)

m.c615 = Constraint(expr=   m.x16 + 751.181818181818*m.b466 - m.x826 >= 0)

m.c616 = Constraint(expr=   m.x17 + 720.527272727272*m.b467 - m.x827 >= 0)

m.c617 = Constraint(expr=   m.x18 + 689.872727272727*m.b468 - m.x828 >= 0)

m.c618 = Constraint(expr=   m.x19 + 659.218181818182*m.b469 - m.x829 >= 0)

m.c619 = Constraint(expr=   m.x20 + 628.563636363636*m.b470 - m.x830 >= 0)

m.c620 = Constraint(expr=   m.x21 + 597.909090909091*m.b471 - m.x831 >= 0)

m.c621 = Constraint(expr=   m.x22 + 567.254545454545*m.b472 - m.x832 >= 0)

m.c622 = Constraint(expr=   m.x23 + 536.6*m.b473 - m.x833 >= 0)

m.c623 = Constraint(expr=   m.x24 + 505.945454545454*m.b474 - m.x834 >= 0)

m.c624 = Constraint(expr=   m.x25 + 475.290909090909*m.b475 - m.x835 >= 0)

m.c625 = Constraint(expr=   m.x26 + 444.636363636364*m.b476 - m.x836 >= 0)

m.c626 = Constraint(expr=   m.x27 + 413.981818181818*m.b477 - m.x837 >= 0)

m.c627 = Constraint(expr=   m.x28 + 383.327272727273*m.b478 - m.x838 >= 0)

m.c628 = Constraint(expr=   m.x29 + 352.672727272727*m.b479 - m.x839 >= 0)

m.c629 = Constraint(expr=   m.x30 + 322.018181818182*m.b480 - m.x840 >= 0)

m.c630 = Constraint(expr= - 81.9*m.x31 + m.x631 == 0)

m.c631 = Constraint(expr= - 81.9*m.x34 + m.x634 == 0)

m.c632 = Constraint(expr= - 81.9*m.x37 + m.x637 == 0)

m.c633 = Constraint(expr= - 81.9*m.x40 + m.x640 == 0)

m.c634 = Constraint(expr= - 81.9*m.x43 + m.x643 == 0)

m.c635 = Constraint(expr= - 81.9*m.x46 + m.x646 == 0)

m.c636 = Constraint(expr= - 81.9*m.x49 + m.x649 == 0)

m.c637 = Constraint(expr= - 81.9*m.x52 + m.x652 == 0)

m.c638 = Constraint(expr= - 81.9*m.x55 + m.x655 == 0)

m.c639 = Constraint(expr= - 81.9*m.x58 + m.x658 == 0)

m.c640 = Constraint(expr= - 81.9*m.x61 + m.x661 == 0)

m.c641 = Constraint(expr= - 81.9*m.x64 + m.x664 == 0)

m.c642 = Constraint(expr= - 81.9*m.x67 + m.x667 == 0)

m.c643 = Constraint(expr= - 81.9*m.x70 + m.x670 == 0)

m.c644 = Constraint(expr= - 81.9*m.x73 + m.x673 == 0)

m.c645 = Constraint(expr= - 81.9*m.x76 + m.x676 == 0)

m.c646 = Constraint(expr= - 81.9*m.x79 + m.x679 == 0)

m.c647 = Constraint(expr= - 81.9*m.x82 + m.x682 == 0)

m.c648 = Constraint(expr= - 81.9*m.x85 + m.x685 == 0)

m.c649 = Constraint(expr= - 81.9*m.x88 + m.x688 == 0)

m.c650 = Constraint(expr= - 81.9*m.x91 + m.x691 == 0)

m.c651 = Constraint(expr= - 81.9*m.x94 + m.x694 == 0)

m.c652 = Constraint(expr= - 81.9*m.x97 + m.x697 == 0)

m.c653 = Constraint(expr= - 81.9*m.x100 + m.x700 == 0)

m.c654 = Constraint(expr= - 81.9*m.x103 + m.x703 == 0)

m.c655 = Constraint(expr= - 81.9*m.x106 + m.x706 == 0)

m.c656 = Constraint(expr= - 81.9*m.x109 + m.x709 == 0)

m.c657 = Constraint(expr= - 81.9*m.x112 + m.x712 == 0)

m.c658 = Constraint(expr= - 81.9*m.x115 + m.x715 == 0)

m.c659 = Constraint(expr= - 81.9*m.x118 + m.x718 == 0)

m.c660 = Constraint(expr= - 81.9*m.x32 + m.x632 == 0)

m.c661 = Constraint(expr= - 81.9*m.x35 + m.x635 == 0)

m.c662 = Constraint(expr= - 81.9*m.x38 + m.x638 == 0)

m.c663 = Constraint(expr= - 81.9*m.x41 + m.x641 == 0)

m.c664 = Constraint(expr= - 81.9*m.x44 + m.x644 == 0)

m.c665 = Constraint(expr= - 81.9*m.x47 + m.x647 == 0)

m.c666 = Constraint(expr= - 81.9*m.x50 + m.x650 == 0)

m.c667 = Constraint(expr= - 81.9*m.x53 + m.x653 == 0)

m.c668 = Constraint(expr= - 81.9*m.x56 + m.x656 == 0)

m.c669 = Constraint(expr= - 81.9*m.x59 + m.x659 == 0)

m.c670 = Constraint(expr= - 81.9*m.x62 + m.x662 == 0)

m.c671 = Constraint(expr= - 81.9*m.x65 + m.x665 == 0)

m.c672 = Constraint(expr= - 81.9*m.x68 + m.x668 == 0)

m.c673 = Constraint(expr= - 81.9*m.x71 + m.x671 == 0)

m.c674 = Constraint(expr= - 81.9*m.x74 + m.x674 == 0)

m.c675 = Constraint(expr= - 81.9*m.x77 + m.x677 == 0)

m.c676 = Constraint(expr= - 81.9*m.x80 + m.x680 == 0)

m.c677 = Constraint(expr= - 81.9*m.x83 + m.x683 == 0)

m.c678 = Constraint(expr= - 81.9*m.x86 + m.x686 == 0)

m.c679 = Constraint(expr= - 81.9*m.x89 + m.x689 == 0)

m.c680 = Constraint(expr= - 81.9*m.x92 + m.x692 == 0)

m.c681 = Constraint(expr= - 81.9*m.x95 + m.x695 == 0)

m.c682 = Constraint(expr= - 81.9*m.x98 + m.x698 == 0)

m.c683 = Constraint(expr= - 81.9*m.x101 + m.x701 == 0)

m.c684 = Constraint(expr= - 81.9*m.x104 + m.x704 == 0)

m.c685 = Constraint(expr= - 81.9*m.x107 + m.x707 == 0)

m.c686 = Constraint(expr= - 81.9*m.x110 + m.x710 == 0)

m.c687 = Constraint(expr= - 81.9*m.x113 + m.x713 == 0)

m.c688 = Constraint(expr= - 81.9*m.x116 + m.x716 == 0)

m.c689 = Constraint(expr= - 81.9*m.x119 + m.x719 == 0)

m.c690 = Constraint(expr= - 81.9*m.x33 + m.x633 == 0)

m.c691 = Constraint(expr= - 81.9*m.x36 + m.x636 == 0)

m.c692 = Constraint(expr= - 81.9*m.x39 + m.x639 == 0)

m.c693 = Constraint(expr= - 81.9*m.x42 + m.x642 == 0)

m.c694 = Constraint(expr= - 81.9*m.x45 + m.x645 == 0)

m.c695 = Constraint(expr= - 81.9*m.x48 + m.x648 == 0)

m.c696 = Constraint(expr= - 81.9*m.x51 + m.x651 == 0)

m.c697 = Constraint(expr= - 81.9*m.x54 + m.x654 == 0)

m.c698 = Constraint(expr= - 81.9*m.x57 + m.x657 == 0)

m.c699 = Constraint(expr= - 81.9*m.x60 + m.x660 == 0)

m.c700 = Constraint(expr= - 81.9*m.x63 + m.x663 == 0)

m.c701 = Constraint(expr= - 81.9*m.x66 + m.x666 == 0)

m.c702 = Constraint(expr= - 81.9*m.x69 + m.x669 == 0)

m.c703 = Constraint(expr= - 81.9*m.x72 + m.x672 == 0)

m.c704 = Constraint(expr= - 81.9*m.x75 + m.x675 == 0)

m.c705 = Constraint(expr= - 81.9*m.x78 + m.x678 == 0)

m.c706 = Constraint(expr= - 81.9*m.x81 + m.x681 == 0)

m.c707 = Constraint(expr= - 81.9*m.x84 + m.x684 == 0)

m.c708 = Constraint(expr= - 81.9*m.x87 + m.x687 == 0)

m.c709 = Constraint(expr= - 81.9*m.x90 + m.x690 == 0)

m.c710 = Constraint(expr= - 81.9*m.x93 + m.x693 == 0)

m.c711 = Constraint(expr= - 81.9*m.x96 + m.x696 == 0)

m.c712 = Constraint(expr= - 81.9*m.x99 + m.x699 == 0)

m.c713 = Constraint(expr= - 81.9*m.x102 + m.x702 == 0)

m.c714 = Constraint(expr= - 81.9*m.x105 + m.x705 == 0)

m.c715 = Constraint(expr= - 81.9*m.x108 + m.x708 == 0)

m.c716 = Constraint(expr= - 81.9*m.x111 + m.x711 == 0)

m.c717 = Constraint(expr= - 81.9*m.x114 + m.x714 == 0)

m.c718 = Constraint(expr= - 81.9*m.x117 + m.x717 == 0)

m.c719 = Constraint(expr= - 81.9*m.x120 + m.x720 == 0)

m.c720 = Constraint(expr= - 136.62*m.x121 + m.x721 == 0)

m.c721 = Constraint(expr= - 136.62*m.x124 + m.x724 == 0)

m.c722 = Constraint(expr= - 136.62*m.x127 + m.x727 == 0)

m.c723 = Constraint(expr= - 136.62*m.x130 + m.x730 == 0)

m.c724 = Constraint(expr= - 136.62*m.x133 + m.x733 == 0)

m.c725 = Constraint(expr= - 136.62*m.x136 + m.x736 == 0)

m.c726 = Constraint(expr= - 136.62*m.x139 + m.x739 == 0)

m.c727 = Constraint(expr= - 136.62*m.x142 + m.x742 == 0)

m.c728 = Constraint(expr= - 136.62*m.x145 + m.x745 == 0)

m.c729 = Constraint(expr= - 136.62*m.x148 + m.x748 == 0)

m.c730 = Constraint(expr= - 136.62*m.x151 + m.x751 == 0)

m.c731 = Constraint(expr= - 136.62*m.x154 + m.x754 == 0)

m.c732 = Constraint(expr= - 136.62*m.x157 + m.x757 == 0)

m.c733 = Constraint(expr= - 136.62*m.x160 + m.x760 == 0)

m.c734 = Constraint(expr= - 136.62*m.x163 + m.x763 == 0)

m.c735 = Constraint(expr= - 136.62*m.x166 + m.x766 == 0)

m.c736 = Constraint(expr= - 136.62*m.x169 + m.x769 == 0)

m.c737 = Constraint(expr= - 136.62*m.x172 + m.x772 == 0)

m.c738 = Constraint(expr= - 136.62*m.x175 + m.x775 == 0)

m.c739 = Constraint(expr= - 136.62*m.x178 + m.x778 == 0)

m.c740 = Constraint(expr= - 136.62*m.x181 + m.x781 == 0)

m.c741 = Constraint(expr= - 136.62*m.x184 + m.x784 == 0)

m.c742 = Constraint(expr= - 136.62*m.x187 + m.x787 == 0)

m.c743 = Constraint(expr= - 136.62*m.x190 + m.x790 == 0)

m.c744 = Constraint(expr= - 136.62*m.x193 + m.x793 == 0)

m.c745 = Constraint(expr= - 136.62*m.x196 + m.x796 == 0)

m.c746 = Constraint(expr= - 136.62*m.x199 + m.x799 == 0)

m.c747 = Constraint(expr= - 136.62*m.x202 + m.x802 == 0)

m.c748 = Constraint(expr= - 136.62*m.x205 + m.x805 == 0)

m.c749 = Constraint(expr= - 136.62*m.x208 + m.x808 == 0)

m.c750 = Constraint(expr= - 136.62*m.x122 + m.x722 == 0)

m.c751 = Constraint(expr= - 136.62*m.x125 + m.x725 == 0)

m.c752 = Constraint(expr= - 136.62*m.x128 + m.x728 == 0)

m.c753 = Constraint(expr= - 136.62*m.x131 + m.x731 == 0)

m.c754 = Constraint(expr= - 136.62*m.x134 + m.x734 == 0)

m.c755 = Constraint(expr= - 136.62*m.x137 + m.x737 == 0)

m.c756 = Constraint(expr= - 136.62*m.x140 + m.x740 == 0)

m.c757 = Constraint(expr= - 136.62*m.x143 + m.x743 == 0)

m.c758 = Constraint(expr= - 136.62*m.x146 + m.x746 == 0)

m.c759 = Constraint(expr= - 136.62*m.x149 + m.x749 == 0)

m.c760 = Constraint(expr= - 136.62*m.x152 + m.x752 == 0)

m.c761 = Constraint(expr= - 136.62*m.x155 + m.x755 == 0)

m.c762 = Constraint(expr= - 136.62*m.x158 + m.x758 == 0)

m.c763 = Constraint(expr= - 136.62*m.x161 + m.x761 == 0)

m.c764 = Constraint(expr= - 136.62*m.x164 + m.x764 == 0)

m.c765 = Constraint(expr= - 136.62*m.x167 + m.x767 == 0)

m.c766 = Constraint(expr= - 136.62*m.x170 + m.x770 == 0)

m.c767 = Constraint(expr= - 136.62*m.x173 + m.x773 == 0)

m.c768 = Constraint(expr= - 136.62*m.x176 + m.x776 == 0)

m.c769 = Constraint(expr= - 136.62*m.x179 + m.x779 == 0)

m.c770 = Constraint(expr= - 136.62*m.x182 + m.x782 == 0)

m.c771 = Constraint(expr= - 136.62*m.x185 + m.x785 == 0)

m.c772 = Constraint(expr= - 136.62*m.x188 + m.x788 == 0)

m.c773 = Constraint(expr= - 136.62*m.x191 + m.x791 == 0)

m.c774 = Constraint(expr= - 136.62*m.x194 + m.x794 == 0)

m.c775 = Constraint(expr= - 136.62*m.x197 + m.x797 == 0)

m.c776 = Constraint(expr= - 136.62*m.x200 + m.x800 == 0)

m.c777 = Constraint(expr= - 136.62*m.x203 + m.x803 == 0)

m.c778 = Constraint(expr= - 136.62*m.x206 + m.x806 == 0)

m.c779 = Constraint(expr= - 136.62*m.x209 + m.x809 == 0)

m.c780 = Constraint(expr= - 136.62*m.x123 + m.x723 == 0)

m.c781 = Constraint(expr= - 136.62*m.x126 + m.x726 == 0)

m.c782 = Constraint(expr= - 136.62*m.x129 + m.x729 == 0)

m.c783 = Constraint(expr= - 136.62*m.x132 + m.x732 == 0)

m.c784 = Constraint(expr= - 136.62*m.x135 + m.x735 == 0)

m.c785 = Constraint(expr= - 136.62*m.x138 + m.x738 == 0)

m.c786 = Constraint(expr= - 136.62*m.x141 + m.x741 == 0)

m.c787 = Constraint(expr= - 136.62*m.x144 + m.x744 == 0)

m.c788 = Constraint(expr= - 136.62*m.x147 + m.x747 == 0)

m.c789 = Constraint(expr= - 136.62*m.x150 + m.x750 == 0)

m.c790 = Constraint(expr= - 136.62*m.x153 + m.x753 == 0)

m.c791 = Constraint(expr= - 136.62*m.x156 + m.x756 == 0)

m.c792 = Constraint(expr= - 136.62*m.x159 + m.x759 == 0)

m.c793 = Constraint(expr= - 136.62*m.x162 + m.x762 == 0)

m.c794 = Constraint(expr= - 136.62*m.x165 + m.x765 == 0)

m.c795 = Constraint(expr= - 136.62*m.x168 + m.x768 == 0)

m.c796 = Constraint(expr= - 136.62*m.x171 + m.x771 == 0)

m.c797 = Constraint(expr= - 136.62*m.x174 + m.x774 == 0)

m.c798 = Constraint(expr= - 136.62*m.x177 + m.x777 == 0)

m.c799 = Constraint(expr= - 136.62*m.x180 + m.x780 == 0)

m.c800 = Constraint(expr= - 136.62*m.x183 + m.x783 == 0)

m.c801 = Constraint(expr= - 136.62*m.x186 + m.x786 == 0)

m.c802 = Constraint(expr= - 136.62*m.x189 + m.x789 == 0)

m.c803 = Constraint(expr= - 136.62*m.x192 + m.x792 == 0)

m.c804 = Constraint(expr= - 136.62*m.x195 + m.x795 == 0)

m.c805 = Constraint(expr= - 136.62*m.x198 + m.x798 == 0)

m.c806 = Constraint(expr= - 136.62*m.x201 + m.x801 == 0)

m.c807 = Constraint(expr= - 136.62*m.x204 + m.x804 == 0)

m.c808 = Constraint(expr= - 136.62*m.x207 + m.x807 == 0)

m.c809 = Constraint(expr= - 136.62*m.x210 + m.x810 == 0)

m.c811 = Constraint(expr= - m.b451 - m.b481 == -1)

m.c812 = Constraint(expr= - m.b452 - m.b482 == -1)

m.c813 = Constraint(expr= - m.b453 - m.b483 == -1)

m.c814 = Constraint(expr= - m.b454 - m.b484 == -1)

m.c815 = Constraint(expr= - m.b455 - m.b485 == -1)

m.c816 = Constraint(expr= - m.b456 - m.b486 == -1)

m.c817 = Constraint(expr= - m.b457 - m.b487 == -1)

m.c818 = Constraint(expr= - m.b458 - m.b488 == -1)

m.c819 = Constraint(expr= - m.b459 - m.b489 == -1)

m.c820 = Constraint(expr= - m.b460 - m.b490 == -1)

m.c821 = Constraint(expr= - m.b461 - m.b491 == -1)

m.c822 = Constraint(expr= - m.b462 - m.b492 == -1)

m.c823 = Constraint(expr= - m.b463 - m.b493 == -1)

m.c824 = Constraint(expr= - m.b464 - m.b494 == -1)

m.c825 = Constraint(expr= - m.b465 - m.b495 == -1)

m.c826 = Constraint(expr= - m.b466 - m.b496 == -1)

m.c827 = Constraint(expr= - m.b467 - m.b497 == -1)

m.c828 = Constraint(expr= - m.b468 - m.b498 == -1)

m.c829 = Constraint(expr= - m.b469 - m.b499 == -1)

m.c830 = Constraint(expr= - m.b470 - m.b500 == -1)

m.c831 = Constraint(expr= - m.b471 - m.b501 == -1)

m.c832 = Constraint(expr= - m.b472 - m.b502 == -1)

m.c833 = Constraint(expr= - m.b473 - m.b503 == -1)

m.c834 = Constraint(expr= - m.b474 - m.b504 == -1)

m.c835 = Constraint(expr= - m.b475 - m.b505 == -1)

m.c836 = Constraint(expr= - m.b476 - m.b506 == -1)

m.c837 = Constraint(expr= - m.b477 - m.b507 == -1)

m.c838 = Constraint(expr= - m.b478 - m.b508 == -1)

m.c839 = Constraint(expr= - m.b479 - m.b509 == -1)

m.c840 = Constraint(expr= - m.b480 - m.b510 == -1)

m.c841 = Constraint(expr= - m.b451 - m.b511 == -1)

m.c842 = Constraint(expr= - m.b452 - m.b512 == -1)

m.c843 = Constraint(expr= - m.b453 - m.b513 == -1)

m.c844 = Constraint(expr= - m.b454 - m.b514 == -1)

m.c845 = Constraint(expr= - m.b455 - m.b515 == -1)

m.c846 = Constraint(expr= - m.b456 - m.b516 == -1)

m.c847 = Constraint(expr= - m.b457 - m.b517 == -1)

m.c848 = Constraint(expr= - m.b458 - m.b518 == -1)

m.c849 = Constraint(expr= - m.b459 - m.b519 == -1)

m.c850 = Constraint(expr= - m.b460 - m.b520 == -1)

m.c851 = Constraint(expr= - m.b461 - m.b521 == -1)

m.c852 = Constraint(expr= - m.b462 - m.b522 == -1)

m.c853 = Constraint(expr= - m.b463 - m.b523 == -1)

m.c854 = Constraint(expr= - m.b464 - m.b524 == -1)

m.c855 = Constraint(expr= - m.b465 - m.b525 == -1)

m.c856 = Constraint(expr= - m.b466 - m.b526 == -1)

m.c857 = Constraint(expr= - m.b467 - m.b527 == -1)

m.c858 = Constraint(expr= - m.b468 - m.b528 == -1)

m.c859 = Constraint(expr= - m.b469 - m.b529 == -1)

m.c860 = Constraint(expr= - m.b470 - m.b530 == -1)

m.c861 = Constraint(expr= - m.b471 - m.b531 == -1)

m.c862 = Constraint(expr= - m.b472 - m.b532 == -1)

m.c863 = Constraint(expr= - m.b473 - m.b533 == -1)

m.c864 = Constraint(expr= - m.b474 - m.b534 == -1)

m.c865 = Constraint(expr= - m.b475 - m.b535 == -1)

m.c866 = Constraint(expr= - m.b476 - m.b536 == -1)

m.c867 = Constraint(expr= - m.b477 - m.b537 == -1)

m.c868 = Constraint(expr= - m.b478 - m.b538 == -1)

m.c869 = Constraint(expr= - m.b479 - m.b539 == -1)

m.c870 = Constraint(expr= - m.b480 - m.b540 == -1)

m.c871 = Constraint(expr= - m.b451 + m.b452 >= 0)

m.c872 = Constraint(expr= - m.b452 + m.b453 >= 0)

m.c873 = Constraint(expr= - m.b453 + m.b454 >= 0)

m.c874 = Constraint(expr= - m.b454 + m.b455 >= 0)

m.c875 = Constraint(expr= - m.b455 + m.b456 >= 0)

m.c876 = Constraint(expr= - m.b456 + m.b457 >= 0)

m.c877 = Constraint(expr= - m.b457 + m.b458 >= 0)

m.c878 = Constraint(expr= - m.b458 + m.b459 >= 0)

m.c879 = Constraint(expr= - m.b459 + m.b460 >= 0)

m.c880 = Constraint(expr= - m.b460 + m.b461 >= 0)

m.c881 = Constraint(expr= - m.b461 + m.b462 >= 0)

m.c882 = Constraint(expr= - m.b462 + m.b463 >= 0)

m.c883 = Constraint(expr= - m.b463 + m.b464 >= 0)

m.c884 = Constraint(expr= - m.b464 + m.b465 >= 0)

m.c885 = Constraint(expr= - m.b465 + m.b466 >= 0)

m.c886 = Constraint(expr= - m.b466 + m.b467 >= 0)

m.c887 = Constraint(expr= - m.b467 + m.b468 >= 0)

m.c888 = Constraint(expr= - m.b468 + m.b469 >= 0)

m.c889 = Constraint(expr= - m.b469 + m.b470 >= 0)

m.c890 = Constraint(expr= - m.b470 + m.b471 >= 0)

m.c891 = Constraint(expr= - m.b471 + m.b472 >= 0)

m.c892 = Constraint(expr= - m.b472 + m.b473 >= 0)

m.c893 = Constraint(expr= - m.b473 + m.b474 >= 0)

m.c894 = Constraint(expr= - m.b474 + m.b475 >= 0)

m.c895 = Constraint(expr= - m.b475 + m.b476 >= 0)

m.c896 = Constraint(expr= - m.b476 + m.b477 >= 0)

m.c897 = Constraint(expr= - m.b477 + m.b478 >= 0)

m.c898 = Constraint(expr= - m.b478 + m.b479 >= 0)

m.c899 = Constraint(expr= - m.b479 + m.b480 >= 0)
