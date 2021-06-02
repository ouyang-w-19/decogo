#  MINLP written by GAMS Convert at 04/21/18 13:52:14
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       1057      527       50      480        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        897      777      120        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       3506     3427       79        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x221 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x222 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x223 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x224 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x225 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x226 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x227 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x228 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x229 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x230 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x231 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x232 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x233 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x234 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x235 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x236 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x237 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x238 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x239 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x240 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x241 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x242 = Var(within=Reals,bounds=(None,None),initialize=0)
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
m.b363 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b364 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b365 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b366 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b367 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b368 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b369 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b370 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b371 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b372 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b373 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b374 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b375 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b376 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b377 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b378 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b379 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b380 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b381 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b382 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b383 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b384 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b385 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b386 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b387 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b388 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b389 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b390 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b391 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b392 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b393 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b394 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b395 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b396 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b397 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b398 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b399 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b400 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b401 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b402 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x451 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x452 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x453 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x454 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x455 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x456 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x457 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x458 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x459 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x460 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x461 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x462 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x463 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x464 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x465 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x466 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x467 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x468 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x469 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x470 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x471 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x472 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x473 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x474 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x475 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x476 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x477 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x478 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x479 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x480 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x481 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x482 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x483 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x484 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x485 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x486 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x487 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x488 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x489 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x490 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x491 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x492 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x493 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x494 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x495 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x496 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x497 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x498 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x499 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x500 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x501 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x502 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x503 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x504 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x505 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x506 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x507 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x508 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x509 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x510 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x511 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x512 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x513 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x514 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x515 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x516 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x517 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x518 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x519 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x520 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x521 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x522 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x523 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x524 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x525 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x526 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x527 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x528 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x529 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x530 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x531 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x532 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x533 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x534 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x535 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x536 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x537 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x538 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x539 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x540 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x541 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x542 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x543 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x544 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x545 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x546 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x547 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x548 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x549 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x550 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x551 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x552 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x553 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x554 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x555 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x556 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x557 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x558 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x559 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x560 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x561 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x562 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x563 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x564 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x565 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x566 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x567 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x568 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x569 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x570 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x571 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x572 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x573 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x574 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x575 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x576 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x577 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x578 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x579 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x580 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x581 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x582 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x583 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x584 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x585 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x586 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x587 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x588 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x589 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x590 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x591 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x592 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x593 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x594 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x595 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x596 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x597 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x598 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x599 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x600 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x601 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x602 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x603 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x604 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x605 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x606 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x607 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x608 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x609 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x610 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x611 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x612 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x613 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x614 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x615 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x616 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x617 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x618 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x619 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x620 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x621 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x622 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x623 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x624 = Var(within=Reals,bounds=(0,None),initialize=0)
m.b625 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b626 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b627 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b628 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b629 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b630 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b631 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b632 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b633 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b634 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b635 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b636 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b637 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b638 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b639 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b640 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b641 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b642 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b643 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b644 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x645 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x646 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x647 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x648 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x649 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x650 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x651 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x652 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x653 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x654 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x655 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x656 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x657 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x658 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x659 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x660 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x661 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x662 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x663 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x664 = Var(within=Reals,bounds=(0,None),initialize=0)
m.b665 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b666 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b667 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b668 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b669 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b670 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b671 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b672 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b673 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b674 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b675 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b676 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b677 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b678 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b679 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b680 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b681 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b682 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b683 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b684 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b685 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b686 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b687 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b688 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b689 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b690 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b691 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b692 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b693 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b694 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b695 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b696 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b697 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b698 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b699 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b700 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b701 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b702 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b703 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b704 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b705 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b706 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b707 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b708 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b709 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b710 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b711 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b712 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b713 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b714 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b715 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b716 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b717 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b718 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b719 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b720 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b721 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b722 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b723 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b724 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x725 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x726 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x727 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x728 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x729 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x730 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x731 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x732 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x733 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x734 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x735 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x736 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x737 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x738 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x739 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x740 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x741 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x742 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x743 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x744 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x745 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x746 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x747 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x748 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x749 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x750 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x751 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x752 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x753 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x754 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x755 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x756 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x757 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x758 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x759 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x760 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x761 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x762 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x763 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x764 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x765 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x766 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x767 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x768 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x769 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x770 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x771 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x772 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x773 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x774 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x786 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x787 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x788 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x789 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x790 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x791 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x792 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x793 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x794 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x795 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x796 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x797 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x798 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x799 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x800 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x801 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x802 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x803 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x804 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x805 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x806 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x807 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x808 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x809 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x810 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x811 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x812 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x813 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x814 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x815 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x816 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x817 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x818 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x819 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x820 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x821 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x822 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x823 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x824 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x825 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x826 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x827 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x828 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x829 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x830 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x831 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x832 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x833 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x834 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x835 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x836 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x837 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x838 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x839 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x840 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x841 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x842 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x843 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x844 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x845 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x846 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x847 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x848 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x849 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x850 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x851 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x852 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x853 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x854 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x855 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x856 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x857 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x858 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x859 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x860 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x861 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x862 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x863 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x864 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x865 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x866 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x867 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x868 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x869 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x870 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x871 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x872 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x873 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x874 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x875 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x876 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x877 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x878 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x879 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x880 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x881 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x882 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x883 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x884 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x885 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x886 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x887 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x888 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x889 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x890 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x891 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x892 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x893 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x894 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x895 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x896 = Var(within=Reals,bounds=(0,1),initialize=0)

m.obj = Objective(expr=-min(m.x890,m.x891,m.x892,m.x893,m.x894,m.x895,m.x896), sense=minimize)

m.c1 = Constraint(expr=   m.x1 + m.x41 == 120)

m.c2 = Constraint(expr=   m.x2 - m.x41 + m.x42 - m.x243 == 0)

m.c3 = Constraint(expr=   m.x3 - m.x42 + m.x43 - m.x244 - m.x263 == 0)

m.c4 = Constraint(expr=   m.x4 - m.x43 + m.x44 - m.x245 - m.x264 == 0)

m.c5 = Constraint(expr=   m.x5 - m.x44 + m.x45 - m.x246 - m.x265 == 0)

m.c6 = Constraint(expr=   m.x6 - m.x45 + m.x46 - m.x247 - m.x266 == 0)

m.c7 = Constraint(expr=   m.x7 - m.x46 + m.x47 - m.x248 - m.x267 == 0)

m.c8 = Constraint(expr=   m.x8 - m.x47 + m.x48 - m.x249 - m.x268 == 0)

m.c9 = Constraint(expr=   m.x9 - m.x48 + m.x49 - m.x250 - m.x269 == 0)

m.c10 = Constraint(expr=   m.x10 - m.x49 + m.x50 - m.x251 - m.x270 == 0)

m.c11 = Constraint(expr=   m.x11 + m.x51 == 120)

m.c12 = Constraint(expr=   m.x12 - m.x51 + m.x52 - m.x253 == 0)

m.c13 = Constraint(expr=   m.x13 - m.x52 + m.x53 - m.x254 - m.x273 == 0)

m.c14 = Constraint(expr=   m.x14 - m.x53 + m.x54 - m.x255 - m.x274 == 0)

m.c15 = Constraint(expr=   m.x15 - m.x54 + m.x55 - m.x256 - m.x275 == 0)

m.c16 = Constraint(expr=   m.x16 - m.x55 + m.x56 - m.x257 - m.x276 == 0)

m.c17 = Constraint(expr=   m.x17 - m.x56 + m.x57 - m.x258 - m.x277 == 0)

m.c18 = Constraint(expr=   m.x18 - m.x57 + m.x58 - m.x259 - m.x278 == 0)

m.c19 = Constraint(expr=   m.x19 - m.x58 + m.x59 - m.x260 - m.x279 == 0)

m.c20 = Constraint(expr=   m.x20 - m.x59 + m.x60 - m.x261 - m.x280 == 0)

m.c21 = Constraint(expr=   m.x21 + m.x61 == 120)

m.c22 = Constraint(expr=   m.x22 - m.x61 + m.x62 - m.x283 == 0)

m.c23 = Constraint(expr=   m.x23 - m.x62 + m.x63 - m.x284 - m.x303 == 0)

m.c24 = Constraint(expr=   m.x24 - m.x63 + m.x64 - m.x285 - m.x304 == 0)

m.c25 = Constraint(expr=   m.x25 - m.x64 + m.x65 - m.x286 - m.x305 == 0)

m.c26 = Constraint(expr=   m.x26 - m.x65 + m.x66 - m.x287 - m.x306 == 0)

m.c27 = Constraint(expr=   m.x27 - m.x66 + m.x67 - m.x288 - m.x307 == 0)

m.c28 = Constraint(expr=   m.x28 - m.x67 + m.x68 - m.x289 - m.x308 == 0)

m.c29 = Constraint(expr=   m.x29 - m.x68 + m.x69 - m.x290 - m.x309 == 0)

m.c30 = Constraint(expr=   m.x30 - m.x69 + m.x70 - m.x291 - m.x310 == 0)

m.c31 = Constraint(expr=   m.x31 + m.x71 == 120)

m.c32 = Constraint(expr=   m.x32 - m.x71 + m.x72 - m.x293 == 0)

m.c33 = Constraint(expr=   m.x33 - m.x72 + m.x73 - m.x294 - m.x313 == 0)

m.c34 = Constraint(expr=   m.x34 - m.x73 + m.x74 - m.x295 - m.x314 == 0)

m.c35 = Constraint(expr=   m.x35 - m.x74 + m.x75 - m.x296 - m.x315 == 0)

m.c36 = Constraint(expr=   m.x36 - m.x75 + m.x76 - m.x297 - m.x316 == 0)

m.c37 = Constraint(expr=   m.x37 - m.x76 + m.x77 - m.x298 - m.x317 == 0)

m.c38 = Constraint(expr=   m.x38 - m.x77 + m.x78 - m.x299 - m.x318 == 0)

m.c39 = Constraint(expr=   m.x39 - m.x78 + m.x79 - m.x300 - m.x319 == 0)

m.c40 = Constraint(expr=   m.x40 - m.x79 + m.x80 - m.x301 - m.x320 == 0)

m.c41 = Constraint(expr= - m.x41 - m.x786 <= -72)

m.c42 = Constraint(expr= - m.x42 - m.x787 <= -72)

m.c43 = Constraint(expr= - m.x43 - m.x788 <= -72)

m.c44 = Constraint(expr= - m.x44 - m.x789 <= -72)

m.c45 = Constraint(expr= - m.x45 - m.x790 <= -72)

m.c46 = Constraint(expr= - m.x46 - m.x791 <= -72)

m.c47 = Constraint(expr= - m.x47 - m.x792 <= -72)

m.c48 = Constraint(expr= - m.x48 - m.x793 <= -72)

m.c49 = Constraint(expr= - m.x49 - m.x794 <= -72)

m.c50 = Constraint(expr= - m.x50 - m.x795 <= -72)

m.c51 = Constraint(expr= - m.x51 - m.x796 <= -72)

m.c52 = Constraint(expr= - m.x52 - m.x797 <= -72)

m.c53 = Constraint(expr= - m.x53 - m.x798 <= -72)

m.c54 = Constraint(expr= - m.x54 - m.x799 <= -72)

m.c55 = Constraint(expr= - m.x55 - m.x800 <= -72)

m.c56 = Constraint(expr= - m.x56 - m.x801 <= -72)

m.c57 = Constraint(expr= - m.x57 - m.x802 <= -72)

m.c58 = Constraint(expr= - m.x58 - m.x803 <= -72)

m.c59 = Constraint(expr= - m.x59 - m.x804 <= -72)

m.c60 = Constraint(expr= - m.x60 - m.x805 <= -72)

m.c61 = Constraint(expr= - m.x61 - m.x806 <= -72)

m.c62 = Constraint(expr= - m.x62 - m.x807 <= -72)

m.c63 = Constraint(expr= - m.x63 - m.x808 <= -72)

m.c64 = Constraint(expr= - m.x64 - m.x809 <= -72)

m.c65 = Constraint(expr= - m.x65 - m.x810 <= -72)

m.c66 = Constraint(expr= - m.x66 - m.x811 <= -72)

m.c67 = Constraint(expr= - m.x67 - m.x812 <= -72)

m.c68 = Constraint(expr= - m.x68 - m.x813 <= -72)

m.c69 = Constraint(expr= - m.x69 - m.x814 <= -72)

m.c70 = Constraint(expr= - m.x70 - m.x815 <= -72)

m.c71 = Constraint(expr= - m.x71 - m.x816 <= -72)

m.c72 = Constraint(expr= - m.x72 - m.x817 <= -72)

m.c73 = Constraint(expr= - m.x73 - m.x818 <= -72)

m.c74 = Constraint(expr= - m.x74 - m.x819 <= -72)

m.c75 = Constraint(expr= - m.x75 - m.x820 <= -72)

m.c76 = Constraint(expr= - m.x76 - m.x821 <= -72)

m.c77 = Constraint(expr= - m.x77 - m.x822 <= -72)

m.c78 = Constraint(expr= - m.x78 - m.x823 <= -72)

m.c79 = Constraint(expr= - m.x79 - m.x824 <= -72)

m.c80 = Constraint(expr= - m.x80 - m.x825 <= -72)

m.c81 = Constraint(expr=   m.x786 <= 72)

m.c82 = Constraint(expr=   m.x787 <= 72)

m.c83 = Constraint(expr=   m.x788 <= 72)

m.c84 = Constraint(expr=   m.x789 <= 72)

m.c85 = Constraint(expr=   m.x790 <= 72)

m.c86 = Constraint(expr=   m.x791 <= 72)

m.c87 = Constraint(expr=   m.x792 <= 72)

m.c88 = Constraint(expr=   m.x793 <= 72)

m.c89 = Constraint(expr=   m.x794 <= 72)

m.c90 = Constraint(expr=   m.x795 <= 72)

m.c91 = Constraint(expr=   m.x796 <= 72)

m.c92 = Constraint(expr=   m.x797 <= 72)

m.c93 = Constraint(expr=   m.x798 <= 72)

m.c94 = Constraint(expr=   m.x799 <= 72)

m.c95 = Constraint(expr=   m.x800 <= 72)

m.c96 = Constraint(expr=   m.x801 <= 72)

m.c97 = Constraint(expr=   m.x802 <= 72)

m.c98 = Constraint(expr=   m.x803 <= 72)

m.c99 = Constraint(expr=   m.x804 <= 72)

m.c100 = Constraint(expr=   m.x805 <= 72)

m.c101 = Constraint(expr=   m.x806 <= 72)

m.c102 = Constraint(expr=   m.x807 <= 72)

m.c103 = Constraint(expr=   m.x808 <= 72)

m.c104 = Constraint(expr=   m.x809 <= 72)

m.c105 = Constraint(expr=   m.x810 <= 72)

m.c106 = Constraint(expr=   m.x811 <= 72)

m.c107 = Constraint(expr=   m.x812 <= 72)

m.c108 = Constraint(expr=   m.x813 <= 72)

m.c109 = Constraint(expr=   m.x814 <= 72)

m.c110 = Constraint(expr=   m.x815 <= 72)

m.c111 = Constraint(expr=   m.x816 <= 72)

m.c112 = Constraint(expr=   m.x817 <= 72)

m.c113 = Constraint(expr=   m.x818 <= 72)

m.c114 = Constraint(expr=   m.x819 <= 72)

m.c115 = Constraint(expr=   m.x820 <= 72)

m.c116 = Constraint(expr=   m.x821 <= 72)

m.c117 = Constraint(expr=   m.x822 <= 72)

m.c118 = Constraint(expr=   m.x823 <= 72)

m.c119 = Constraint(expr=   m.x824 <= 72)

m.c120 = Constraint(expr=   m.x825 <= 72)

m.c121 = Constraint(expr=   m.x1 + m.x81 == 80)

m.c122 = Constraint(expr=   m.x2 - m.x81 + m.x82 == 80)

m.c123 = Constraint(expr=   m.x3 - m.x82 + m.x83 == 80)

m.c124 = Constraint(expr=   m.x4 - m.x83 + m.x84 == 80)

m.c125 = Constraint(expr=   m.x5 - m.x84 + m.x85 == 80)

m.c126 = Constraint(expr=   m.x6 - m.x85 + m.x86 == 80)

m.c127 = Constraint(expr=   m.x7 - m.x86 + m.x87 == 80)

m.c128 = Constraint(expr=   m.x8 - m.x87 + m.x88 == 80)

m.c129 = Constraint(expr=   m.x9 - m.x88 + m.x89 == 80)

m.c130 = Constraint(expr=   m.x10 - m.x89 + m.x90 == 80)

m.c131 = Constraint(expr=   m.x11 + m.x91 == 80)

m.c132 = Constraint(expr=   m.x12 - m.x91 + m.x92 == 80)

m.c133 = Constraint(expr=   m.x13 - m.x92 + m.x93 == 80)

m.c134 = Constraint(expr=   m.x14 - m.x93 + m.x94 == 80)

m.c135 = Constraint(expr=   m.x15 - m.x94 + m.x95 == 80)

m.c136 = Constraint(expr=   m.x16 - m.x95 + m.x96 == 80)

m.c137 = Constraint(expr=   m.x17 - m.x96 + m.x97 == 80)

m.c138 = Constraint(expr=   m.x18 - m.x97 + m.x98 == 80)

m.c139 = Constraint(expr=   m.x19 - m.x98 + m.x99 == 80)

m.c140 = Constraint(expr=   m.x20 - m.x99 + m.x100 == 80)

m.c141 = Constraint(expr=   m.x21 + m.x101 == 80)

m.c142 = Constraint(expr=   m.x22 - m.x101 + m.x102 == 80)

m.c143 = Constraint(expr=   m.x23 - m.x102 + m.x103 == 80)

m.c144 = Constraint(expr=   m.x24 - m.x103 + m.x104 == 80)

m.c145 = Constraint(expr=   m.x25 - m.x104 + m.x105 == 80)

m.c146 = Constraint(expr=   m.x26 - m.x105 + m.x106 == 80)

m.c147 = Constraint(expr=   m.x27 - m.x106 + m.x107 == 80)

m.c148 = Constraint(expr=   m.x28 - m.x107 + m.x108 == 80)

m.c149 = Constraint(expr=   m.x29 - m.x108 + m.x109 == 80)

m.c150 = Constraint(expr=   m.x30 - m.x109 + m.x110 == 80)

m.c151 = Constraint(expr=   m.x31 + m.x111 == 80)

m.c152 = Constraint(expr=   m.x32 - m.x111 + m.x112 == 80)

m.c153 = Constraint(expr=   m.x33 - m.x112 + m.x113 == 80)

m.c154 = Constraint(expr=   m.x34 - m.x113 + m.x114 == 80)

m.c155 = Constraint(expr=   m.x35 - m.x114 + m.x115 == 80)

m.c156 = Constraint(expr=   m.x36 - m.x115 + m.x116 == 80)

m.c157 = Constraint(expr=   m.x37 - m.x116 + m.x117 == 80)

m.c158 = Constraint(expr=   m.x38 - m.x117 + m.x118 == 80)

m.c159 = Constraint(expr=   m.x39 - m.x118 + m.x119 == 80)

m.c160 = Constraint(expr=   m.x40 - m.x119 + m.x120 == 80)

m.c161 = Constraint(expr=   m.x41 + m.x61 <= 600)

m.c162 = Constraint(expr=   m.x42 + m.x62 <= 600)

m.c163 = Constraint(expr=   m.x43 + m.x63 <= 600)

m.c164 = Constraint(expr=   m.x44 + m.x64 <= 600)

m.c165 = Constraint(expr=   m.x45 + m.x65 <= 600)

m.c166 = Constraint(expr=   m.x46 + m.x66 <= 600)

m.c167 = Constraint(expr=   m.x47 + m.x67 <= 600)

m.c168 = Constraint(expr=   m.x48 + m.x68 <= 600)

m.c169 = Constraint(expr=   m.x49 + m.x69 <= 600)

m.c170 = Constraint(expr=   m.x50 + m.x70 <= 600)

m.c171 = Constraint(expr=   m.x51 + m.x71 <= 600)

m.c172 = Constraint(expr=   m.x52 + m.x72 <= 600)

m.c173 = Constraint(expr=   m.x53 + m.x73 <= 600)

m.c174 = Constraint(expr=   m.x54 + m.x74 <= 600)

m.c175 = Constraint(expr=   m.x55 + m.x75 <= 600)

m.c176 = Constraint(expr=   m.x56 + m.x76 <= 600)

m.c177 = Constraint(expr=   m.x57 + m.x77 <= 600)

m.c178 = Constraint(expr=   m.x58 + m.x78 <= 600)

m.c179 = Constraint(expr=   m.x59 + m.x79 <= 600)

m.c180 = Constraint(expr=   m.x60 + m.x80 <= 600)

m.c181 = Constraint(expr=   m.x141 - 1050*m.x243 - 950*m.x263 - 1050*m.x283 - 950*m.x303 == 0)

m.c182 = Constraint(expr=   m.x142 - 1050*m.x244 - 950*m.x264 - 1050*m.x284 - 950*m.x304 == 0)

m.c183 = Constraint(expr=   m.x143 - 1050*m.x245 - 950*m.x265 - 1050*m.x285 - 950*m.x305 == 0)

m.c184 = Constraint(expr=   m.x144 - 1050*m.x246 - 950*m.x266 - 1050*m.x286 - 950*m.x306 == 0)

m.c185 = Constraint(expr=   m.x145 - 1050*m.x247 - 950*m.x267 - 1050*m.x287 - 950*m.x307 == 0)

m.c186 = Constraint(expr=   m.x146 - 1050*m.x248 - 950*m.x268 - 1050*m.x288 - 950*m.x308 == 0)

m.c187 = Constraint(expr=   m.x147 - 1050*m.x249 - 950*m.x269 - 1050*m.x289 - 950*m.x309 == 0)

m.c188 = Constraint(expr=   m.x148 - 1050*m.x250 - 950*m.x270 - 1050*m.x290 - 950*m.x310 == 0)

m.c189 = Constraint(expr=   m.x149 - 1050*m.x251 - 950*m.x271 - 1050*m.x291 - 950*m.x311 == 0)

m.c190 = Constraint(expr=   m.x150 - 1050*m.x252 - 950*m.x272 - 1050*m.x292 - 950*m.x312 == 0)

m.c191 = Constraint(expr=   m.x151 - 1200*m.x253 - 900*m.x273 - 1200*m.x293 - 900*m.x313 == 0)

m.c192 = Constraint(expr=   m.x152 - 1200*m.x254 - 900*m.x274 - 1200*m.x294 - 900*m.x314 == 0)

m.c193 = Constraint(expr=   m.x153 - 1200*m.x255 - 900*m.x275 - 1200*m.x295 - 900*m.x315 == 0)

m.c194 = Constraint(expr=   m.x154 - 1200*m.x256 - 900*m.x276 - 1200*m.x296 - 900*m.x316 == 0)

m.c195 = Constraint(expr=   m.x155 - 1200*m.x257 - 900*m.x277 - 1200*m.x297 - 900*m.x317 == 0)

m.c196 = Constraint(expr=   m.x156 - 1200*m.x258 - 900*m.x278 - 1200*m.x298 - 900*m.x318 == 0)

m.c197 = Constraint(expr=   m.x157 - 1200*m.x259 - 900*m.x279 - 1200*m.x299 - 900*m.x319 == 0)

m.c198 = Constraint(expr=   m.x158 - 1200*m.x260 - 900*m.x280 - 1200*m.x300 - 900*m.x320 == 0)

m.c199 = Constraint(expr=   m.x159 - 1200*m.x261 - 900*m.x281 - 1200*m.x301 - 900*m.x321 == 0)

m.c200 = Constraint(expr=   m.x160 - 1200*m.x262 - 900*m.x282 - 1200*m.x302 - 900*m.x322 == 0)

m.c201 = Constraint(expr= - 10*m.x41 - 10*m.x61 + m.x161 - 11*m.x786 - 11*m.x806 == 0)

m.c202 = Constraint(expr= - 10*m.x42 - 10*m.x62 + m.x162 - 11*m.x787 - 11*m.x807 == 0)

m.c203 = Constraint(expr= - 10*m.x43 - 10*m.x63 + m.x163 - 11*m.x788 - 11*m.x808 == 0)

m.c204 = Constraint(expr= - 10*m.x44 - 10*m.x64 + m.x164 - 11*m.x789 - 11*m.x809 == 0)

m.c205 = Constraint(expr= - 10*m.x45 - 10*m.x65 + m.x165 - 11*m.x790 - 11*m.x810 == 0)

m.c206 = Constraint(expr= - 10*m.x46 - 10*m.x66 + m.x166 - 11*m.x791 - 11*m.x811 == 0)

m.c207 = Constraint(expr= - 10*m.x47 - 10*m.x67 + m.x167 - 11*m.x792 - 11*m.x812 == 0)

m.c208 = Constraint(expr= - 10*m.x48 - 10*m.x68 + m.x168 - 11*m.x793 - 11*m.x813 == 0)

m.c209 = Constraint(expr= - 10*m.x49 - 10*m.x69 + m.x169 - 11*m.x794 - 11*m.x814 == 0)

m.c210 = Constraint(expr= - 10*m.x50 - 10*m.x70 + m.x170 - 11*m.x795 - 11*m.x815 == 0)

m.c211 = Constraint(expr= - 10*m.x51 - 10*m.x71 + m.x171 - 11*m.x796 - 11*m.x816 == 0)

m.c212 = Constraint(expr= - 10*m.x52 - 10*m.x72 + m.x172 - 11*m.x797 - 11*m.x817 == 0)

m.c213 = Constraint(expr= - 10*m.x53 - 10*m.x73 + m.x173 - 11*m.x798 - 11*m.x818 == 0)

m.c214 = Constraint(expr= - 10*m.x54 - 10*m.x74 + m.x174 - 11*m.x799 - 11*m.x819 == 0)

m.c215 = Constraint(expr= - 10*m.x55 - 10*m.x75 + m.x175 - 11*m.x800 - 11*m.x820 == 0)

m.c216 = Constraint(expr= - 10*m.x56 - 10*m.x76 + m.x176 - 11*m.x801 - 11*m.x821 == 0)

m.c217 = Constraint(expr= - 10*m.x57 - 10*m.x77 + m.x177 - 11*m.x802 - 11*m.x822 == 0)

m.c218 = Constraint(expr= - 10*m.x58 - 10*m.x78 + m.x178 - 11*m.x803 - 11*m.x823 == 0)

m.c219 = Constraint(expr= - 10*m.x59 - 10*m.x79 + m.x179 - 11*m.x804 - 11*m.x824 == 0)

m.c220 = Constraint(expr= - 10*m.x60 - 10*m.x80 + m.x180 - 11*m.x805 - 11*m.x825 == 0)

m.c221 = Constraint(expr= - 5*m.x1 - 5*m.x21 + m.x181 == 0)

m.c222 = Constraint(expr= - 5*m.x2 - 5*m.x22 + m.x182 - 5*m.x243 - 5*m.x283 == 0)

m.c223 = Constraint(expr= - 5*m.x3 - 5*m.x23 + m.x183 - 5*m.x244 - 5*m.x263 - 5*m.x284 - 5*m.x303 == 0)

m.c224 = Constraint(expr= - 5*m.x4 - 5*m.x24 + m.x184 - 5*m.x245 - 5*m.x264 - 5*m.x285 - 5*m.x304 == 0)

m.c225 = Constraint(expr= - 5*m.x5 - 5*m.x25 + m.x185 - 5*m.x246 - 5*m.x265 - 5*m.x286 - 5*m.x305 == 0)

m.c226 = Constraint(expr= - 5*m.x6 - 5*m.x26 + m.x186 - 5*m.x247 - 5*m.x266 - 5*m.x287 - 5*m.x306 == 0)

m.c227 = Constraint(expr= - 5*m.x7 - 5*m.x27 + m.x187 - 5*m.x248 - 5*m.x267 - 5*m.x288 - 5*m.x307 == 0)

m.c228 = Constraint(expr= - 5*m.x8 - 5*m.x28 + m.x188 - 5*m.x249 - 5*m.x268 - 5*m.x289 - 5*m.x308 == 0)

m.c229 = Constraint(expr= - 5*m.x9 - 5*m.x29 + m.x189 - 5*m.x250 - 5*m.x269 - 5*m.x290 - 5*m.x309 == 0)

m.c230 = Constraint(expr= - 5*m.x10 - 5*m.x30 + m.x190 - 5*m.x251 - 5*m.x270 - 5*m.x291 - 5*m.x310 == 0)

m.c231 = Constraint(expr= - 5*m.x11 - 5*m.x31 + m.x191 == 0)

m.c232 = Constraint(expr= - 5*m.x12 - 5*m.x32 + m.x192 - 5*m.x253 - 5*m.x293 == 0)

m.c233 = Constraint(expr= - 5*m.x13 - 5*m.x33 + m.x193 - 5*m.x254 - 5*m.x273 - 5*m.x294 - 5*m.x313 == 0)

m.c234 = Constraint(expr= - 5*m.x14 - 5*m.x34 + m.x194 - 5*m.x255 - 5*m.x274 - 5*m.x295 - 5*m.x314 == 0)

m.c235 = Constraint(expr= - 5*m.x15 - 5*m.x35 + m.x195 - 5*m.x256 - 5*m.x275 - 5*m.x296 - 5*m.x315 == 0)

m.c236 = Constraint(expr= - 5*m.x16 - 5*m.x36 + m.x196 - 5*m.x257 - 5*m.x276 - 5*m.x297 - 5*m.x316 == 0)

m.c237 = Constraint(expr= - 5*m.x17 - 5*m.x37 + m.x197 - 5*m.x258 - 5*m.x277 - 5*m.x298 - 5*m.x317 == 0)

m.c238 = Constraint(expr= - 5*m.x18 - 5*m.x38 + m.x198 - 5*m.x259 - 5*m.x278 - 5*m.x299 - 5*m.x318 == 0)

m.c239 = Constraint(expr= - 5*m.x19 - 5*m.x39 + m.x199 - 5*m.x260 - 5*m.x279 - 5*m.x300 - 5*m.x319 == 0)

m.c240 = Constraint(expr= - 5*m.x20 - 5*m.x40 + m.x200 - 5*m.x261 - 5*m.x280 - 5*m.x301 - 5*m.x320 == 0)

m.c241 = Constraint(expr= - 0.00625*m.x1 - 0.00625*m.x21 + m.x121 == 0)

m.c242 = Constraint(expr=-0.5*(m.x2/(80 + m.x81) + m.x22/(80 + m.x101)) + m.x122 == 0)

m.c243 = Constraint(expr=-0.5*(m.x3/(80 + m.x82) + m.x23/(80 + m.x102)) + m.x123 == 0)

m.c244 = Constraint(expr=-0.5*(m.x4/(80 + m.x83) + m.x24/(80 + m.x103)) + m.x124 == 0)

m.c245 = Constraint(expr=-0.5*(m.x5/(80 + m.x84) + m.x25/(80 + m.x104)) + m.x125 == 0)

m.c246 = Constraint(expr=-0.5*(m.x6/(80 + m.x85) + m.x26/(80 + m.x105)) + m.x126 == 0)

m.c247 = Constraint(expr=-0.5*(m.x7/(80 + m.x86) + m.x27/(80 + m.x106)) + m.x127 == 0)

m.c248 = Constraint(expr=-0.5*(m.x8/(80 + m.x87) + m.x28/(80 + m.x107)) + m.x128 == 0)

m.c249 = Constraint(expr=-0.5*(m.x9/(80 + m.x88) + m.x29/(80 + m.x108)) + m.x129 == 0)

m.c250 = Constraint(expr=-0.5*(m.x10/(80 + m.x89) + m.x30/(80 + m.x109)) + m.x130 == 0)

m.c251 = Constraint(expr= - 0.00625*m.x11 - 0.00625*m.x31 + m.x131 == 0)

m.c252 = Constraint(expr=-0.5*(m.x12/(80 + m.x91) + m.x32/(80 + m.x111)) + m.x132 == 0)

m.c253 = Constraint(expr=-0.5*(m.x13/(80 + m.x92) + m.x33/(80 + m.x112)) + m.x133 == 0)

m.c254 = Constraint(expr=-0.5*(m.x14/(80 + m.x93) + m.x34/(80 + m.x113)) + m.x134 == 0)

m.c255 = Constraint(expr=-0.5*(m.x15/(80 + m.x94) + m.x35/(80 + m.x114)) + m.x135 == 0)

m.c256 = Constraint(expr=-0.5*(m.x16/(80 + m.x95) + m.x36/(80 + m.x115)) + m.x136 == 0)

m.c257 = Constraint(expr=-0.5*(m.x17/(80 + m.x96) + m.x37/(80 + m.x116)) + m.x137 == 0)

m.c258 = Constraint(expr=-0.5*(m.x18/(80 + m.x97) + m.x38/(80 + m.x117)) + m.x138 == 0)

m.c259 = Constraint(expr=-0.5*(m.x19/(80 + m.x98) + m.x39/(80 + m.x118)) + m.x139 == 0)

m.c260 = Constraint(expr=-0.5*(m.x20/(80 + m.x99) + m.x40/(80 + m.x119)) + m.x140 == 0)

m.c261 = Constraint(expr=   m.x121 >= 0.6)

m.c262 = Constraint(expr=   m.x122 >= 0.6)

m.c263 = Constraint(expr=   m.x123 >= 0.6)

m.c264 = Constraint(expr=   m.x124 >= 0.6)

m.c265 = Constraint(expr=   m.x125 >= 0.6)

m.c266 = Constraint(expr=   m.x126 >= 0.6)

m.c267 = Constraint(expr=   m.x127 >= 0.6)

m.c268 = Constraint(expr=   m.x128 >= 0.6)

m.c269 = Constraint(expr=   m.x129 >= 0.6)

m.c270 = Constraint(expr=   m.x130 >= 0.6)

m.c271 = Constraint(expr=   m.x131 >= 0.6)

m.c272 = Constraint(expr=   m.x132 >= 0.6)

m.c273 = Constraint(expr=   m.x133 >= 0.6)

m.c274 = Constraint(expr=   m.x134 >= 0.6)

m.c275 = Constraint(expr=   m.x135 >= 0.6)

m.c276 = Constraint(expr=   m.x136 >= 0.6)

m.c277 = Constraint(expr=   m.x137 >= 0.6)

m.c278 = Constraint(expr=   m.x138 >= 0.6)

m.c279 = Constraint(expr=   m.x139 >= 0.6)

m.c280 = Constraint(expr=   m.x140 >= 0.6)

m.c281 = Constraint(expr= - 1500*m.x1 - 1500*m.x21 + m.x201 == 0)

m.c282 = Constraint(expr= - 1500*m.x2 - 1500*m.x22 + m.x202 == 0)

m.c283 = Constraint(expr= - 1500*m.x3 - 1500*m.x23 + m.x203 == 0)

m.c284 = Constraint(expr= - 1500*m.x4 - 1500*m.x24 + m.x204 == 0)

m.c285 = Constraint(expr= - 1500*m.x5 - 1500*m.x25 + m.x205 == 0)

m.c286 = Constraint(expr= - 1500*m.x6 - 1500*m.x26 + m.x206 == 0)

m.c287 = Constraint(expr= - 1500*m.x7 - 1500*m.x27 + m.x207 == 0)

m.c288 = Constraint(expr= - 1500*m.x8 - 1500*m.x28 + m.x208 == 0)

m.c289 = Constraint(expr= - 1500*m.x9 - 1500*m.x29 + m.x209 == 0)

m.c290 = Constraint(expr= - 1500*m.x10 - 1500*m.x30 + m.x210 == 0)

m.c291 = Constraint(expr= - 1500*m.x11 - 1500*m.x31 + m.x211 == 0)

m.c292 = Constraint(expr= - 1500*m.x12 - 1500*m.x32 + m.x212 == 0)

m.c293 = Constraint(expr= - 1500*m.x13 - 1500*m.x33 + m.x213 == 0)

m.c294 = Constraint(expr= - 1500*m.x14 - 1500*m.x34 + m.x214 == 0)

m.c295 = Constraint(expr= - 1500*m.x15 - 1500*m.x35 + m.x215 == 0)

m.c296 = Constraint(expr= - 1500*m.x16 - 1500*m.x36 + m.x216 == 0)

m.c297 = Constraint(expr= - 1500*m.x17 - 1500*m.x37 + m.x217 == 0)

m.c298 = Constraint(expr= - 1500*m.x18 - 1500*m.x38 + m.x218 == 0)

m.c299 = Constraint(expr= - 1500*m.x19 - 1500*m.x39 + m.x219 == 0)

m.c300 = Constraint(expr= - 1500*m.x20 - 1500*m.x40 + m.x220 == 0)

m.c301 = Constraint(expr=   m.x141 + m.x161 + m.x181 - m.x201 + m.x221 == 0)

m.c302 = Constraint(expr=   m.x142 + m.x162 + m.x182 - m.x202 + m.x222 == 0)

m.c303 = Constraint(expr=   m.x143 + m.x163 + m.x183 - m.x203 + m.x223 == 0)

m.c304 = Constraint(expr=   m.x144 + m.x164 + m.x184 - m.x204 + m.x224 == 0)

m.c305 = Constraint(expr=   m.x145 + m.x165 + m.x185 - m.x205 + m.x225 == 0)

m.c306 = Constraint(expr=   m.x146 + m.x166 + m.x186 - m.x206 + m.x226 == 0)

m.c307 = Constraint(expr=   m.x147 + m.x167 + m.x187 - m.x207 + m.x227 == 0)

m.c308 = Constraint(expr=   m.x148 + m.x168 + m.x188 - m.x208 + m.x228 == 0)

m.c309 = Constraint(expr=   m.x149 + m.x169 + m.x189 - m.x209 + m.x229 == 0)

m.c310 = Constraint(expr=   m.x150 + m.x170 + m.x190 - m.x210 + m.x230 == 0)

m.c311 = Constraint(expr=   m.x151 + m.x171 + m.x191 - m.x211 + m.x231 == 0)

m.c312 = Constraint(expr=   m.x152 + m.x172 + m.x192 - m.x212 + m.x232 == 0)

m.c313 = Constraint(expr=   m.x153 + m.x173 + m.x193 - m.x213 + m.x233 == 0)

m.c314 = Constraint(expr=   m.x154 + m.x174 + m.x194 - m.x214 + m.x234 == 0)

m.c315 = Constraint(expr=   m.x155 + m.x175 + m.x195 - m.x215 + m.x235 == 0)

m.c316 = Constraint(expr=   m.x156 + m.x176 + m.x196 - m.x216 + m.x236 == 0)

m.c317 = Constraint(expr=   m.x157 + m.x177 + m.x197 - m.x217 + m.x237 == 0)

m.c318 = Constraint(expr=   m.x158 + m.x178 + m.x198 - m.x218 + m.x238 == 0)

m.c319 = Constraint(expr=   m.x159 + m.x179 + m.x199 - m.x219 + m.x239 == 0)

m.c320 = Constraint(expr=   m.x160 + m.x180 + m.x200 - m.x220 + m.x240 == 0)

m.c321 = Constraint(expr=   m.x141 + m.x142 + m.x143 + m.x144 + m.x145 + m.x146 + m.x147 + m.x148 + m.x149 + m.x150
                          + m.x161 + m.x162 + m.x163 + m.x164 + m.x165 + m.x166 + m.x167 + m.x168 + m.x169 + m.x170
                          + m.x181 + m.x182 + m.x183 + m.x184 + m.x185 + m.x186 + m.x187 + m.x188 + m.x189 + m.x190
                          - m.x201 - m.x202 - m.x203 - m.x204 - m.x205 - m.x206 - m.x207 - m.x208 - m.x209 - m.x210
                          + m.x241 == 0)

m.c322 = Constraint(expr=   m.x151 + m.x152 + m.x153 + m.x154 + m.x155 + m.x156 + m.x157 + m.x158 + m.x159 + m.x160
                          + m.x171 + m.x172 + m.x173 + m.x174 + m.x175 + m.x176 + m.x177 + m.x178 + m.x179 + m.x180
                          + m.x191 + m.x192 + m.x193 + m.x194 + m.x195 + m.x196 + m.x197 + m.x198 + m.x199 + m.x200
                          - m.x211 - m.x212 - m.x213 - m.x214 - m.x215 - m.x216 - m.x217 - m.x218 - m.x219 - m.x220
                          + m.x242 == 0)

m.c323 = Constraint(expr=   m.x243 + m.x253 + m.x403 == 300)

m.c324 = Constraint(expr=   m.x244 + m.x254 - m.x403 + m.x404 == 0)

m.c325 = Constraint(expr=   m.x245 + m.x255 - m.x404 + m.x405 - m.x565 == 0)

m.c326 = Constraint(expr=   m.x246 + m.x256 - m.x405 + m.x406 - m.x566 == 0)

m.c327 = Constraint(expr=   m.x247 + m.x257 - m.x406 + m.x407 - m.x567 == 0)

m.c328 = Constraint(expr=   m.x248 + m.x258 - m.x407 + m.x408 - m.x568 == 0)

m.c329 = Constraint(expr=   m.x249 + m.x259 - m.x408 + m.x409 - m.x569 == 0)

m.c330 = Constraint(expr=   m.x250 + m.x260 - m.x409 + m.x410 - m.x570 == 0)

m.c331 = Constraint(expr=   m.x251 + m.x261 - m.x410 + m.x411 - m.x571 == 0)

m.c332 = Constraint(expr=   m.x252 + m.x262 - m.x411 + m.x412 - m.x572 == 0)

m.c333 = Constraint(expr=   m.x283 + m.x293 + m.x423 == 300)

m.c334 = Constraint(expr=   m.x284 + m.x294 - m.x423 + m.x424 == 0)

m.c335 = Constraint(expr=   m.x285 + m.x295 - m.x424 + m.x425 - m.x585 == 0)

m.c336 = Constraint(expr=   m.x286 + m.x296 - m.x425 + m.x426 - m.x586 == 0)

m.c337 = Constraint(expr=   m.x287 + m.x297 - m.x426 + m.x427 - m.x587 == 0)

m.c338 = Constraint(expr=   m.x288 + m.x298 - m.x427 + m.x428 - m.x588 == 0)

m.c339 = Constraint(expr=   m.x289 + m.x299 - m.x428 + m.x429 - m.x589 == 0)

m.c340 = Constraint(expr=   m.x290 + m.x300 - m.x429 + m.x430 - m.x590 == 0)

m.c341 = Constraint(expr=   m.x291 + m.x301 - m.x430 + m.x431 - m.x591 == 0)

m.c342 = Constraint(expr=   m.x292 + m.x302 - m.x431 + m.x432 - m.x592 == 0)

m.c343 = Constraint(expr=   m.x263 + m.x273 + m.x413 == 400)

m.c344 = Constraint(expr=   m.x264 + m.x274 - m.x413 + m.x414 - m.x575 == 0)

m.c345 = Constraint(expr=   m.x265 + m.x275 - m.x414 + m.x415 - m.x576 == 0)

m.c346 = Constraint(expr=   m.x266 + m.x276 - m.x415 + m.x416 - m.x577 == 0)

m.c347 = Constraint(expr=   m.x267 + m.x277 - m.x416 + m.x417 - m.x578 == 0)

m.c348 = Constraint(expr=   m.x268 + m.x278 - m.x417 + m.x418 - m.x579 == 0)

m.c349 = Constraint(expr=   m.x269 + m.x279 - m.x418 + m.x419 - m.x580 == 0)

m.c350 = Constraint(expr=   m.x270 + m.x280 - m.x419 + m.x420 - m.x581 == 0)

m.c351 = Constraint(expr=   m.x271 + m.x281 - m.x420 + m.x421 - m.x582 == 0)

m.c352 = Constraint(expr=   m.x272 + m.x282 - m.x421 + m.x422 - m.x583 == 0)

m.c353 = Constraint(expr=   m.x303 + m.x313 + m.x433 == 400)

m.c354 = Constraint(expr=   m.x304 + m.x314 - m.x433 + m.x434 - m.x595 == 0)

m.c355 = Constraint(expr=   m.x305 + m.x315 - m.x434 + m.x435 - m.x596 == 0)

m.c356 = Constraint(expr=   m.x306 + m.x316 - m.x435 + m.x436 - m.x597 == 0)

m.c357 = Constraint(expr=   m.x307 + m.x317 - m.x436 + m.x437 - m.x598 == 0)

m.c358 = Constraint(expr=   m.x308 + m.x318 - m.x437 + m.x438 - m.x599 == 0)

m.c359 = Constraint(expr=   m.x309 + m.x319 - m.x438 + m.x439 - m.x600 == 0)

m.c360 = Constraint(expr=   m.x310 + m.x320 - m.x439 + m.x440 - m.x601 == 0)

m.c361 = Constraint(expr=   m.x311 + m.x321 - m.x440 + m.x441 - m.x602 == 0)

m.c362 = Constraint(expr=   m.x312 + m.x322 - m.x441 + m.x442 - m.x603 == 0)

m.c363 = Constraint(expr= - m.x403 - m.x826 <= -180)

m.c364 = Constraint(expr= - m.x404 - m.x827 <= -180)

m.c365 = Constraint(expr= - m.x405 - m.x828 <= -180)

m.c366 = Constraint(expr= - m.x406 - m.x829 <= -180)

m.c367 = Constraint(expr= - m.x407 - m.x830 <= -180)

m.c368 = Constraint(expr= - m.x408 - m.x831 <= -180)

m.c369 = Constraint(expr= - m.x409 - m.x832 <= -180)

m.c370 = Constraint(expr= - m.x410 - m.x833 <= -180)

m.c371 = Constraint(expr= - m.x411 - m.x834 <= -180)

m.c372 = Constraint(expr= - m.x412 - m.x835 <= -180)

m.c373 = Constraint(expr= - m.x413 - m.x836 <= -180)

m.c374 = Constraint(expr= - m.x414 - m.x837 <= -180)

m.c375 = Constraint(expr= - m.x415 - m.x838 <= -180)

m.c376 = Constraint(expr= - m.x416 - m.x839 <= -180)

m.c377 = Constraint(expr= - m.x417 - m.x840 <= -180)

m.c378 = Constraint(expr= - m.x418 - m.x841 <= -180)

m.c379 = Constraint(expr= - m.x419 - m.x842 <= -180)

m.c380 = Constraint(expr= - m.x420 - m.x843 <= -180)

m.c381 = Constraint(expr= - m.x421 - m.x844 <= -180)

m.c382 = Constraint(expr= - m.x422 - m.x845 <= -180)

m.c383 = Constraint(expr= - m.x423 - m.x846 <= -180)

m.c384 = Constraint(expr= - m.x424 - m.x847 <= -180)

m.c385 = Constraint(expr= - m.x425 - m.x848 <= -180)

m.c386 = Constraint(expr= - m.x426 - m.x849 <= -180)

m.c387 = Constraint(expr= - m.x427 - m.x850 <= -180)

m.c388 = Constraint(expr= - m.x428 - m.x851 <= -180)

m.c389 = Constraint(expr= - m.x429 - m.x852 <= -180)

m.c390 = Constraint(expr= - m.x430 - m.x853 <= -180)

m.c391 = Constraint(expr= - m.x431 - m.x854 <= -180)

m.c392 = Constraint(expr= - m.x432 - m.x855 <= -180)

m.c393 = Constraint(expr= - m.x433 - m.x856 <= -180)

m.c394 = Constraint(expr= - m.x434 - m.x857 <= -180)

m.c395 = Constraint(expr= - m.x435 - m.x858 <= -180)

m.c396 = Constraint(expr= - m.x436 - m.x859 <= -180)

m.c397 = Constraint(expr= - m.x437 - m.x860 <= -180)

m.c398 = Constraint(expr= - m.x438 - m.x861 <= -180)

m.c399 = Constraint(expr= - m.x439 - m.x862 <= -180)

m.c400 = Constraint(expr= - m.x440 - m.x863 <= -180)

m.c401 = Constraint(expr= - m.x441 - m.x864 <= -180)

m.c402 = Constraint(expr= - m.x442 - m.x865 <= -180)

m.c403 = Constraint(expr=   m.x826 <= 180)

m.c404 = Constraint(expr=   m.x827 <= 180)

m.c405 = Constraint(expr=   m.x828 <= 180)

m.c406 = Constraint(expr=   m.x829 <= 180)

m.c407 = Constraint(expr=   m.x830 <= 180)

m.c408 = Constraint(expr=   m.x831 <= 180)

m.c409 = Constraint(expr=   m.x832 <= 180)

m.c410 = Constraint(expr=   m.x833 <= 180)

m.c411 = Constraint(expr=   m.x834 <= 180)

m.c412 = Constraint(expr=   m.x835 <= 180)

m.c413 = Constraint(expr=   m.x836 <= 180)

m.c414 = Constraint(expr=   m.x837 <= 180)

m.c415 = Constraint(expr=   m.x838 <= 180)

m.c416 = Constraint(expr=   m.x839 <= 180)

m.c417 = Constraint(expr=   m.x840 <= 180)

m.c418 = Constraint(expr=   m.x841 <= 180)

m.c419 = Constraint(expr=   m.x842 <= 180)

m.c420 = Constraint(expr=   m.x843 <= 180)

m.c421 = Constraint(expr=   m.x844 <= 180)

m.c422 = Constraint(expr=   m.x845 <= 180)

m.c423 = Constraint(expr=   m.x846 <= 180)

m.c424 = Constraint(expr=   m.x847 <= 180)

m.c425 = Constraint(expr=   m.x848 <= 180)

m.c426 = Constraint(expr=   m.x849 <= 180)

m.c427 = Constraint(expr=   m.x850 <= 180)

m.c428 = Constraint(expr=   m.x851 <= 180)

m.c429 = Constraint(expr=   m.x852 <= 180)

m.c430 = Constraint(expr=   m.x853 <= 180)

m.c431 = Constraint(expr=   m.x854 <= 180)

m.c432 = Constraint(expr=   m.x855 <= 180)

m.c433 = Constraint(expr=   m.x856 <= 180)

m.c434 = Constraint(expr=   m.x857 <= 180)

m.c435 = Constraint(expr=   m.x858 <= 180)

m.c436 = Constraint(expr=   m.x859 <= 180)

m.c437 = Constraint(expr=   m.x860 <= 180)

m.c438 = Constraint(expr=   m.x861 <= 180)

m.c439 = Constraint(expr=   m.x862 <= 180)

m.c440 = Constraint(expr=   m.x863 <= 180)

m.c441 = Constraint(expr=   m.x864 <= 180)

m.c442 = Constraint(expr=   m.x865 <= 180)

m.c443 = Constraint(expr=   m.x403 + m.x423 <= 2000)

m.c444 = Constraint(expr=   m.x404 + m.x424 <= 2000)

m.c445 = Constraint(expr=   m.x405 + m.x425 <= 2000)

m.c446 = Constraint(expr=   m.x406 + m.x426 <= 2000)

m.c447 = Constraint(expr=   m.x407 + m.x427 <= 2000)

m.c448 = Constraint(expr=   m.x408 + m.x428 <= 2000)

m.c449 = Constraint(expr=   m.x409 + m.x429 <= 2000)

m.c450 = Constraint(expr=   m.x410 + m.x430 <= 2000)

m.c451 = Constraint(expr=   m.x411 + m.x431 <= 2000)

m.c452 = Constraint(expr=   m.x412 + m.x432 <= 2000)

m.c453 = Constraint(expr=   m.x413 + m.x433 <= 4000)

m.c454 = Constraint(expr=   m.x414 + m.x434 <= 4000)

m.c455 = Constraint(expr=   m.x415 + m.x435 <= 4000)

m.c456 = Constraint(expr=   m.x416 + m.x436 <= 4000)

m.c457 = Constraint(expr=   m.x417 + m.x437 <= 4000)

m.c458 = Constraint(expr=   m.x418 + m.x438 <= 4000)

m.c459 = Constraint(expr=   m.x419 + m.x439 <= 4000)

m.c460 = Constraint(expr=   m.x420 + m.x440 <= 4000)

m.c461 = Constraint(expr=   m.x421 + m.x441 <= 4000)

m.c462 = Constraint(expr=   m.x422 + m.x442 <= 4000)

m.c463 = Constraint(expr= - m.x243 - m.x283 + m.x323 == 0)

m.c464 = Constraint(expr= - m.x244 - m.x284 + m.x324 == 0)

m.c465 = Constraint(expr= - m.x245 - m.x285 + m.x325 == 0)

m.c466 = Constraint(expr= - m.x246 - m.x286 + m.x326 == 0)

m.c467 = Constraint(expr= - m.x247 - m.x287 + m.x327 == 0)

m.c468 = Constraint(expr= - m.x248 - m.x288 + m.x328 == 0)

m.c469 = Constraint(expr= - m.x249 - m.x289 + m.x329 == 0)

m.c470 = Constraint(expr= - m.x250 - m.x290 + m.x330 == 0)

m.c471 = Constraint(expr= - m.x251 - m.x291 + m.x331 == 0)

m.c472 = Constraint(expr= - m.x252 - m.x292 + m.x332 == 0)

m.c473 = Constraint(expr= - m.x253 - m.x293 + m.x333 == 0)

m.c474 = Constraint(expr= - m.x254 - m.x294 + m.x334 == 0)

m.c475 = Constraint(expr= - m.x255 - m.x295 + m.x335 == 0)

m.c476 = Constraint(expr= - m.x256 - m.x296 + m.x336 == 0)

m.c477 = Constraint(expr= - m.x257 - m.x297 + m.x337 == 0)

m.c478 = Constraint(expr= - m.x258 - m.x298 + m.x338 == 0)

m.c479 = Constraint(expr= - m.x259 - m.x299 + m.x339 == 0)

m.c480 = Constraint(expr= - m.x260 - m.x300 + m.x340 == 0)

m.c481 = Constraint(expr= - m.x261 - m.x301 + m.x341 == 0)

m.c482 = Constraint(expr= - m.x262 - m.x302 + m.x342 == 0)

m.c483 = Constraint(expr= - m.x263 - m.x303 + m.x343 == 0)

m.c484 = Constraint(expr= - m.x264 - m.x304 + m.x344 == 0)

m.c485 = Constraint(expr= - m.x265 - m.x305 + m.x345 == 0)

m.c486 = Constraint(expr= - m.x266 - m.x306 + m.x346 == 0)

m.c487 = Constraint(expr= - m.x267 - m.x307 + m.x347 == 0)

m.c488 = Constraint(expr= - m.x268 - m.x308 + m.x348 == 0)

m.c489 = Constraint(expr= - m.x269 - m.x309 + m.x349 == 0)

m.c490 = Constraint(expr= - m.x270 - m.x310 + m.x350 == 0)

m.c491 = Constraint(expr= - m.x271 - m.x311 + m.x351 == 0)

m.c492 = Constraint(expr= - m.x272 - m.x312 + m.x352 == 0)

m.c493 = Constraint(expr= - m.x273 - m.x313 + m.x353 == 0)

m.c494 = Constraint(expr= - m.x274 - m.x314 + m.x354 == 0)

m.c495 = Constraint(expr= - m.x275 - m.x315 + m.x355 == 0)

m.c496 = Constraint(expr= - m.x276 - m.x316 + m.x356 == 0)

m.c497 = Constraint(expr= - m.x277 - m.x317 + m.x357 == 0)

m.c498 = Constraint(expr= - m.x278 - m.x318 + m.x358 == 0)

m.c499 = Constraint(expr= - m.x279 - m.x319 + m.x359 == 0)

m.c500 = Constraint(expr= - m.x280 - m.x320 + m.x360 == 0)

m.c501 = Constraint(expr= - m.x281 - m.x321 + m.x361 == 0)

m.c502 = Constraint(expr= - m.x282 - m.x322 + m.x362 == 0)

m.c503 = Constraint(expr= - m.x323 + m.b363 <= 0)

m.c504 = Constraint(expr= - m.x324 + m.b364 <= 0)

m.c505 = Constraint(expr= - m.x325 + m.b365 <= 0)

m.c506 = Constraint(expr= - m.x326 + m.b366 <= 0)

m.c507 = Constraint(expr= - m.x327 + m.b367 <= 0)

m.c508 = Constraint(expr= - m.x328 + m.b368 <= 0)

m.c509 = Constraint(expr= - m.x329 + m.b369 <= 0)

m.c510 = Constraint(expr= - m.x330 + m.b370 <= 0)

m.c511 = Constraint(expr= - m.x331 + m.b371 <= 0)

m.c512 = Constraint(expr= - m.x332 + m.b372 <= 0)

m.c513 = Constraint(expr= - m.x333 + m.b373 <= 0)

m.c514 = Constraint(expr= - m.x334 + m.b374 <= 0)

m.c515 = Constraint(expr= - m.x335 + m.b375 <= 0)

m.c516 = Constraint(expr= - m.x336 + m.b376 <= 0)

m.c517 = Constraint(expr= - m.x337 + m.b377 <= 0)

m.c518 = Constraint(expr= - m.x338 + m.b378 <= 0)

m.c519 = Constraint(expr= - m.x339 + m.b379 <= 0)

m.c520 = Constraint(expr= - m.x340 + m.b380 <= 0)

m.c521 = Constraint(expr= - m.x341 + m.b381 <= 0)

m.c522 = Constraint(expr= - m.x342 + m.b382 <= 0)

m.c523 = Constraint(expr= - m.x343 + m.b383 <= 0)

m.c524 = Constraint(expr= - m.x344 + m.b384 <= 0)

m.c525 = Constraint(expr= - m.x345 + m.b385 <= 0)

m.c526 = Constraint(expr= - m.x346 + m.b386 <= 0)

m.c527 = Constraint(expr= - m.x347 + m.b387 <= 0)

m.c528 = Constraint(expr= - m.x348 + m.b388 <= 0)

m.c529 = Constraint(expr= - m.x349 + m.b389 <= 0)

m.c530 = Constraint(expr= - m.x350 + m.b390 <= 0)

m.c531 = Constraint(expr= - m.x351 + m.b391 <= 0)

m.c532 = Constraint(expr= - m.x352 + m.b392 <= 0)

m.c533 = Constraint(expr= - m.x353 + m.b393 <= 0)

m.c534 = Constraint(expr= - m.x354 + m.b394 <= 0)

m.c535 = Constraint(expr= - m.x355 + m.b395 <= 0)

m.c536 = Constraint(expr= - m.x356 + m.b396 <= 0)

m.c537 = Constraint(expr= - m.x357 + m.b397 <= 0)

m.c538 = Constraint(expr= - m.x358 + m.b398 <= 0)

m.c539 = Constraint(expr= - m.x359 + m.b399 <= 0)

m.c540 = Constraint(expr= - m.x360 + m.b400 <= 0)

m.c541 = Constraint(expr= - m.x361 + m.b401 <= 0)

m.c542 = Constraint(expr= - m.x362 + m.b402 <= 0)

m.c543 = Constraint(expr=   m.x323 - 300*m.b363 <= 0)

m.c544 = Constraint(expr=   m.x324 - 300*m.b364 <= 0)

m.c545 = Constraint(expr=   m.x325 - 300*m.b365 <= 0)

m.c546 = Constraint(expr=   m.x326 - 300*m.b366 <= 0)

m.c547 = Constraint(expr=   m.x327 - 300*m.b367 <= 0)

m.c548 = Constraint(expr=   m.x328 - 300*m.b368 <= 0)

m.c549 = Constraint(expr=   m.x329 - 300*m.b369 <= 0)

m.c550 = Constraint(expr=   m.x330 - 300*m.b370 <= 0)

m.c551 = Constraint(expr=   m.x331 - 300*m.b371 <= 0)

m.c552 = Constraint(expr=   m.x332 - 300*m.b372 <= 0)

m.c553 = Constraint(expr=   m.x333 - 300*m.b373 <= 0)

m.c554 = Constraint(expr=   m.x334 - 300*m.b374 <= 0)

m.c555 = Constraint(expr=   m.x335 - 300*m.b375 <= 0)

m.c556 = Constraint(expr=   m.x336 - 300*m.b376 <= 0)

m.c557 = Constraint(expr=   m.x337 - 300*m.b377 <= 0)

m.c558 = Constraint(expr=   m.x338 - 300*m.b378 <= 0)

m.c559 = Constraint(expr=   m.x339 - 300*m.b379 <= 0)

m.c560 = Constraint(expr=   m.x340 - 300*m.b380 <= 0)

m.c561 = Constraint(expr=   m.x341 - 300*m.b381 <= 0)

m.c562 = Constraint(expr=   m.x342 - 300*m.b382 <= 0)

m.c563 = Constraint(expr=   m.x343 - 400*m.b383 <= 0)

m.c564 = Constraint(expr=   m.x344 - 400*m.b384 <= 0)

m.c565 = Constraint(expr=   m.x345 - 400*m.b385 <= 0)

m.c566 = Constraint(expr=   m.x346 - 400*m.b386 <= 0)

m.c567 = Constraint(expr=   m.x347 - 400*m.b387 <= 0)

m.c568 = Constraint(expr=   m.x348 - 400*m.b388 <= 0)

m.c569 = Constraint(expr=   m.x349 - 400*m.b389 <= 0)

m.c570 = Constraint(expr=   m.x350 - 400*m.b390 <= 0)

m.c571 = Constraint(expr=   m.x351 - 400*m.b391 <= 0)

m.c572 = Constraint(expr=   m.x352 - 400*m.b392 <= 0)

m.c573 = Constraint(expr=   m.x353 - 400*m.b393 <= 0)

m.c574 = Constraint(expr=   m.x354 - 400*m.b394 <= 0)

m.c575 = Constraint(expr=   m.x355 - 400*m.b395 <= 0)

m.c576 = Constraint(expr=   m.x356 - 400*m.b396 <= 0)

m.c577 = Constraint(expr=   m.x357 - 400*m.b397 <= 0)

m.c578 = Constraint(expr=   m.x358 - 400*m.b398 <= 0)

m.c579 = Constraint(expr=   m.x359 - 400*m.b399 <= 0)

m.c580 = Constraint(expr=   m.x360 - 400*m.b400 <= 0)

m.c581 = Constraint(expr=   m.x361 - 400*m.b401 <= 0)

m.c582 = Constraint(expr=   m.x362 - 400*m.b402 <= 0)

m.c583 = Constraint(expr=   m.b363 <= 1)

m.c584 = Constraint(expr=   m.b364 <= 1)

m.c585 = Constraint(expr=   m.b365 <= 1)

m.c586 = Constraint(expr=   m.b366 <= 1)

m.c587 = Constraint(expr=   m.b367 <= 1)

m.c588 = Constraint(expr=   m.b368 <= 1)

m.c589 = Constraint(expr=   m.b369 <= 1)

m.c590 = Constraint(expr=   m.b370 <= 1)

m.c591 = Constraint(expr=   m.b371 <= 1)

m.c592 = Constraint(expr=   m.b372 <= 1)

m.c593 = Constraint(expr=   m.b373 <= 1)

m.c594 = Constraint(expr=   m.b374 <= 1)

m.c595 = Constraint(expr=   m.b375 <= 1)

m.c596 = Constraint(expr=   m.b376 <= 1)

m.c597 = Constraint(expr=   m.b377 <= 1)

m.c598 = Constraint(expr=   m.b378 <= 1)

m.c599 = Constraint(expr=   m.b379 <= 1)

m.c600 = Constraint(expr=   m.b380 <= 1)

m.c601 = Constraint(expr=   m.b381 <= 1)

m.c602 = Constraint(expr=   m.b382 <= 1)

m.c603 = Constraint(expr=   m.b383 <= 1)

m.c604 = Constraint(expr=   m.b384 <= 1)

m.c605 = Constraint(expr=   m.b385 <= 1)

m.c606 = Constraint(expr=   m.b386 <= 1)

m.c607 = Constraint(expr=   m.b387 <= 1)

m.c608 = Constraint(expr=   m.b388 <= 1)

m.c609 = Constraint(expr=   m.b389 <= 1)

m.c610 = Constraint(expr=   m.b390 <= 1)

m.c611 = Constraint(expr=   m.b391 <= 1)

m.c612 = Constraint(expr=   m.b392 <= 1)

m.c613 = Constraint(expr=   m.b393 <= 1)

m.c614 = Constraint(expr=   m.b394 <= 1)

m.c615 = Constraint(expr=   m.b395 <= 1)

m.c616 = Constraint(expr=   m.b396 <= 1)

m.c617 = Constraint(expr=   m.b397 <= 1)

m.c618 = Constraint(expr=   m.b398 <= 1)

m.c619 = Constraint(expr=   m.b399 <= 1)

m.c620 = Constraint(expr=   m.b400 <= 1)

m.c621 = Constraint(expr=   m.b401 <= 1)

m.c622 = Constraint(expr=   m.b402 <= 1)

m.c623 = Constraint(expr=   300*m.b363 + 300*m.b373 <= 600)

m.c624 = Constraint(expr=   300*m.b364 + 300*m.b374 <= 600)

m.c625 = Constraint(expr=   300*m.b365 + 300*m.b375 <= 600)

m.c626 = Constraint(expr=   300*m.b366 + 300*m.b376 <= 600)

m.c627 = Constraint(expr=   300*m.b367 + 300*m.b377 <= 600)

m.c628 = Constraint(expr=   300*m.b368 + 300*m.b378 <= 600)

m.c629 = Constraint(expr=   300*m.b369 + 300*m.b379 <= 600)

m.c630 = Constraint(expr=   300*m.b370 + 300*m.b380 <= 600)

m.c631 = Constraint(expr=   300*m.b371 + 300*m.b381 <= 600)

m.c632 = Constraint(expr=   300*m.b372 + 300*m.b382 <= 600)

m.c633 = Constraint(expr=   400*m.b383 + 400*m.b393 <= 800)

m.c634 = Constraint(expr=   400*m.b384 + 400*m.b394 <= 800)

m.c635 = Constraint(expr=   400*m.b385 + 400*m.b395 <= 800)

m.c636 = Constraint(expr=   400*m.b386 + 400*m.b396 <= 800)

m.c637 = Constraint(expr=   400*m.b387 + 400*m.b397 <= 800)

m.c638 = Constraint(expr=   400*m.b388 + 400*m.b398 <= 800)

m.c639 = Constraint(expr=   400*m.b389 + 400*m.b399 <= 800)

m.c640 = Constraint(expr=   400*m.b390 + 400*m.b400 <= 800)

m.c641 = Constraint(expr=   400*m.b391 + 400*m.b401 <= 800)

m.c642 = Constraint(expr=   400*m.b392 + 400*m.b402 <= 800)

m.c643 = Constraint(expr=   m.x443 - 700*m.x565 - 700*m.x585 == 0)

m.c644 = Constraint(expr=   m.x444 - 700*m.x566 - 700*m.x586 == 0)

m.c645 = Constraint(expr=   m.x445 - 700*m.x567 - 700*m.x587 == 0)

m.c646 = Constraint(expr=   m.x446 - 700*m.x568 - 700*m.x588 == 0)

m.c647 = Constraint(expr=   m.x447 - 700*m.x569 - 700*m.x589 == 0)

m.c648 = Constraint(expr=   m.x448 - 700*m.x570 - 700*m.x590 == 0)

m.c649 = Constraint(expr=   m.x449 - 700*m.x571 - 700*m.x591 == 0)

m.c650 = Constraint(expr=   m.x450 - 700*m.x572 - 700*m.x592 == 0)

m.c651 = Constraint(expr=   m.x451 - 700*m.x573 - 700*m.x593 == 0)

m.c652 = Constraint(expr=   m.x452 - 700*m.x574 - 700*m.x594 == 0)

m.c653 = Constraint(expr=   m.x453 - 600*m.x575 - 600*m.x595 == 0)

m.c654 = Constraint(expr=   m.x454 - 600*m.x576 - 600*m.x596 == 0)

m.c655 = Constraint(expr=   m.x455 - 600*m.x577 - 600*m.x597 == 0)

m.c656 = Constraint(expr=   m.x456 - 600*m.x578 - 600*m.x598 == 0)

m.c657 = Constraint(expr=   m.x457 - 600*m.x579 - 600*m.x599 == 0)

m.c658 = Constraint(expr=   m.x458 - 600*m.x580 - 600*m.x600 == 0)

m.c659 = Constraint(expr=   m.x459 - 600*m.x581 - 600*m.x601 == 0)

m.c660 = Constraint(expr=   m.x460 - 600*m.x582 - 600*m.x602 == 0)

m.c661 = Constraint(expr=   m.x461 - 600*m.x583 - 600*m.x603 == 0)

m.c662 = Constraint(expr=   m.x462 - 600*m.x584 - 600*m.x604 == 0)

m.c663 = Constraint(expr= - 4*m.x403 - 4*m.x423 + m.x463 - 5*m.x826 - 5*m.x846 == 0)

m.c664 = Constraint(expr= - 4*m.x404 - 4*m.x424 + m.x464 - 5*m.x827 - 5*m.x847 == 0)

m.c665 = Constraint(expr= - 4*m.x405 - 4*m.x425 + m.x465 - 5*m.x828 - 5*m.x848 == 0)

m.c666 = Constraint(expr= - 4*m.x406 - 4*m.x426 + m.x466 - 5*m.x829 - 5*m.x849 == 0)

m.c667 = Constraint(expr= - 4*m.x407 - 4*m.x427 + m.x467 - 5*m.x830 - 5*m.x850 == 0)

m.c668 = Constraint(expr= - 4*m.x408 - 4*m.x428 + m.x468 - 5*m.x831 - 5*m.x851 == 0)

m.c669 = Constraint(expr= - 4*m.x409 - 4*m.x429 + m.x469 - 5*m.x832 - 5*m.x852 == 0)

m.c670 = Constraint(expr= - 4*m.x410 - 4*m.x430 + m.x470 - 5*m.x833 - 5*m.x853 == 0)

m.c671 = Constraint(expr= - 4*m.x411 - 4*m.x431 + m.x471 - 5*m.x834 - 5*m.x854 == 0)

m.c672 = Constraint(expr= - 4*m.x412 - 4*m.x432 + m.x472 - 5*m.x835 - 5*m.x855 == 0)

m.c673 = Constraint(expr= - 2*m.x413 - 2*m.x433 + m.x473 - 3*m.x836 - 3*m.x856 == 0)

m.c674 = Constraint(expr= - 2*m.x414 - 2*m.x434 + m.x474 - 3*m.x837 - 3*m.x857 == 0)

m.c675 = Constraint(expr= - 2*m.x415 - 2*m.x435 + m.x475 - 3*m.x838 - 3*m.x858 == 0)

m.c676 = Constraint(expr= - 2*m.x416 - 2*m.x436 + m.x476 - 3*m.x839 - 3*m.x859 == 0)

m.c677 = Constraint(expr= - 2*m.x417 - 2*m.x437 + m.x477 - 3*m.x840 - 3*m.x860 == 0)

m.c678 = Constraint(expr= - 2*m.x418 - 2*m.x438 + m.x478 - 3*m.x841 - 3*m.x861 == 0)

m.c679 = Constraint(expr= - 2*m.x419 - 2*m.x439 + m.x479 - 3*m.x842 - 3*m.x862 == 0)

m.c680 = Constraint(expr= - 2*m.x420 - 2*m.x440 + m.x480 - 3*m.x843 - 3*m.x863 == 0)

m.c681 = Constraint(expr= - 2*m.x421 - 2*m.x441 + m.x481 - 3*m.x844 - 3*m.x864 == 0)

m.c682 = Constraint(expr= - 2*m.x422 - 2*m.x442 + m.x482 - 3*m.x845 - 3*m.x865 == 0)

m.c683 = Constraint(expr= - 2*m.x243 - 2*m.x253 - 2*m.x283 - 2*m.x293 + m.x483 == 0)

m.c684 = Constraint(expr= - 2*m.x244 - 2*m.x254 - 2*m.x284 - 2*m.x294 + m.x484 == 0)

m.c685 = Constraint(expr= - 2*m.x245 - 2*m.x255 - 2*m.x285 - 2*m.x295 + m.x485 - 2*m.x565 - 2*m.x585 == 0)

m.c686 = Constraint(expr= - 2*m.x246 - 2*m.x256 - 2*m.x286 - 2*m.x296 + m.x486 - 2*m.x566 - 2*m.x586 == 0)

m.c687 = Constraint(expr= - 2*m.x247 - 2*m.x257 - 2*m.x287 - 2*m.x297 + m.x487 - 2*m.x567 - 2*m.x587 == 0)

m.c688 = Constraint(expr= - 2*m.x248 - 2*m.x258 - 2*m.x288 - 2*m.x298 + m.x488 - 2*m.x568 - 2*m.x588 == 0)

m.c689 = Constraint(expr= - 2*m.x249 - 2*m.x259 - 2*m.x289 - 2*m.x299 + m.x489 - 2*m.x569 - 2*m.x589 == 0)

m.c690 = Constraint(expr= - 2*m.x250 - 2*m.x260 - 2*m.x290 - 2*m.x300 + m.x490 - 2*m.x570 - 2*m.x590 == 0)

m.c691 = Constraint(expr= - 2*m.x251 - 2*m.x261 - 2*m.x291 - 2*m.x301 + m.x491 - 2*m.x571 - 2*m.x591 == 0)

m.c692 = Constraint(expr= - 2*m.x252 - 2*m.x262 - 2*m.x292 - 2*m.x302 + m.x492 - 2*m.x572 - 2*m.x592 == 0)

m.c693 = Constraint(expr= - m.x263 - m.x273 - m.x303 - m.x313 + m.x493 == 0)

m.c694 = Constraint(expr= - m.x264 - m.x274 - m.x304 - m.x314 + m.x494 - m.x575 - m.x595 == 0)

m.c695 = Constraint(expr= - m.x265 - m.x275 - m.x305 - m.x315 + m.x495 - m.x576 - m.x596 == 0)

m.c696 = Constraint(expr= - m.x266 - m.x276 - m.x306 - m.x316 + m.x496 - m.x577 - m.x597 == 0)

m.c697 = Constraint(expr= - m.x267 - m.x277 - m.x307 - m.x317 + m.x497 - m.x578 - m.x598 == 0)

m.c698 = Constraint(expr= - m.x268 - m.x278 - m.x308 - m.x318 + m.x498 - m.x579 - m.x599 == 0)

m.c699 = Constraint(expr= - m.x269 - m.x279 - m.x309 - m.x319 + m.x499 - m.x580 - m.x600 == 0)

m.c700 = Constraint(expr= - m.x270 - m.x280 - m.x310 - m.x320 + m.x500 - m.x581 - m.x601 == 0)

m.c701 = Constraint(expr= - m.x271 - m.x281 - m.x311 - m.x321 + m.x501 - m.x582 - m.x602 == 0)

m.c702 = Constraint(expr= - m.x272 - m.x282 - m.x312 - m.x322 + m.x502 - m.x583 - m.x603 == 0)

m.c703 = Constraint(expr= - 10*m.x323 - 13*m.x333 - 2500*m.b363 - 3000*m.b373 + m.x503 == 0)

m.c704 = Constraint(expr= - 10*m.x324 - 13*m.x334 - 2500*m.b364 - 3000*m.b374 + m.x504 == 0)

m.c705 = Constraint(expr= - 10*m.x325 - 13*m.x335 - 2500*m.b365 - 3000*m.b375 + m.x505 == 0)

m.c706 = Constraint(expr= - 10*m.x326 - 13*m.x336 - 2500*m.b366 - 3000*m.b376 + m.x506 == 0)

m.c707 = Constraint(expr= - 10*m.x327 - 13*m.x337 - 2500*m.b367 - 3000*m.b377 + m.x507 == 0)

m.c708 = Constraint(expr= - 10*m.x328 - 13*m.x338 - 2500*m.b368 - 3000*m.b378 + m.x508 == 0)

m.c709 = Constraint(expr= - 10*m.x329 - 13*m.x339 - 2500*m.b369 - 3000*m.b379 + m.x509 == 0)

m.c710 = Constraint(expr= - 10*m.x330 - 13*m.x340 - 2500*m.b370 - 3000*m.b380 + m.x510 == 0)

m.c711 = Constraint(expr= - 10*m.x331 - 13*m.x341 - 2500*m.b371 - 3000*m.b381 + m.x511 == 0)

m.c712 = Constraint(expr= - 10*m.x332 - 13*m.x342 - 2500*m.b372 - 3000*m.b382 + m.x512 == 0)

m.c713 = Constraint(expr= - 25*m.x343 - 22*m.x353 - 6000*m.b383 - 5000*m.b393 + m.x513 == 0)

m.c714 = Constraint(expr= - 25*m.x344 - 22*m.x354 - 6000*m.b384 - 5000*m.b394 + m.x514 == 0)

m.c715 = Constraint(expr= - 25*m.x345 - 22*m.x355 - 6000*m.b385 - 5000*m.b395 + m.x515 == 0)

m.c716 = Constraint(expr= - 25*m.x346 - 22*m.x356 - 6000*m.b386 - 5000*m.b396 + m.x516 == 0)

m.c717 = Constraint(expr= - 25*m.x347 - 22*m.x357 - 6000*m.b387 - 5000*m.b397 + m.x517 == 0)

m.c718 = Constraint(expr= - 25*m.x348 - 22*m.x358 - 6000*m.b388 - 5000*m.b398 + m.x518 == 0)

m.c719 = Constraint(expr= - 25*m.x349 - 22*m.x359 - 6000*m.b389 - 5000*m.b399 + m.x519 == 0)

m.c720 = Constraint(expr= - 25*m.x350 - 22*m.x360 - 6000*m.b390 - 5000*m.b400 + m.x520 == 0)

m.c721 = Constraint(expr= - 25*m.x351 - 22*m.x361 - 6000*m.b391 - 5000*m.b401 + m.x521 == 0)

m.c722 = Constraint(expr= - 25*m.x352 - 22*m.x362 - 6000*m.b392 - 5000*m.b402 + m.x522 == 0)

m.c723 = Constraint(expr= - 1050*m.x243 - 1200*m.x253 - 1050*m.x283 - 1200*m.x293 + m.x523 == 0)

m.c724 = Constraint(expr= - 1050*m.x244 - 1200*m.x254 - 1050*m.x284 - 1200*m.x294 + m.x524 == 0)

m.c725 = Constraint(expr= - 1050*m.x245 - 1200*m.x255 - 1050*m.x285 - 1200*m.x295 + m.x525 == 0)

m.c726 = Constraint(expr= - 1050*m.x246 - 1200*m.x256 - 1050*m.x286 - 1200*m.x296 + m.x526 == 0)

m.c727 = Constraint(expr= - 1050*m.x247 - 1200*m.x257 - 1050*m.x287 - 1200*m.x297 + m.x527 == 0)

m.c728 = Constraint(expr= - 1050*m.x248 - 1200*m.x258 - 1050*m.x288 - 1200*m.x298 + m.x528 == 0)

m.c729 = Constraint(expr= - 1050*m.x249 - 1200*m.x259 - 1050*m.x289 - 1200*m.x299 + m.x529 == 0)

m.c730 = Constraint(expr= - 1050*m.x250 - 1200*m.x260 - 1050*m.x290 - 1200*m.x300 + m.x530 == 0)

m.c731 = Constraint(expr= - 1050*m.x251 - 1200*m.x261 - 1050*m.x291 - 1200*m.x301 + m.x531 == 0)

m.c732 = Constraint(expr= - 1050*m.x252 - 1200*m.x262 - 1050*m.x292 - 1200*m.x302 + m.x532 == 0)

m.c733 = Constraint(expr= - 950*m.x263 - 900*m.x273 - 950*m.x303 - 900*m.x313 + m.x533 == 0)

m.c734 = Constraint(expr= - 950*m.x264 - 900*m.x274 - 950*m.x304 - 900*m.x314 + m.x534 == 0)

m.c735 = Constraint(expr= - 950*m.x265 - 900*m.x275 - 950*m.x305 - 900*m.x315 + m.x535 == 0)

m.c736 = Constraint(expr= - 950*m.x266 - 900*m.x276 - 950*m.x306 - 900*m.x316 + m.x536 == 0)

m.c737 = Constraint(expr= - 950*m.x267 - 900*m.x277 - 950*m.x307 - 900*m.x317 + m.x537 == 0)

m.c738 = Constraint(expr= - 950*m.x268 - 900*m.x278 - 950*m.x308 - 900*m.x318 + m.x538 == 0)

m.c739 = Constraint(expr= - 950*m.x269 - 900*m.x279 - 950*m.x309 - 900*m.x319 + m.x539 == 0)

m.c740 = Constraint(expr= - 950*m.x270 - 900*m.x280 - 950*m.x310 - 900*m.x320 + m.x540 == 0)

m.c741 = Constraint(expr= - 950*m.x271 - 900*m.x281 - 950*m.x311 - 900*m.x321 + m.x541 == 0)

m.c742 = Constraint(expr= - 950*m.x272 - 900*m.x282 - 950*m.x312 - 900*m.x322 + m.x542 == 0)

m.c743 = Constraint(expr=   m.x443 + m.x463 + m.x483 + m.x503 - m.x523 + m.x543 == 0)

m.c744 = Constraint(expr=   m.x444 + m.x464 + m.x484 + m.x504 - m.x524 + m.x544 == 0)

m.c745 = Constraint(expr=   m.x445 + m.x465 + m.x485 + m.x505 - m.x525 + m.x545 == 0)

m.c746 = Constraint(expr=   m.x446 + m.x466 + m.x486 + m.x506 - m.x526 + m.x546 == 0)

m.c747 = Constraint(expr=   m.x447 + m.x467 + m.x487 + m.x507 - m.x527 + m.x547 == 0)

m.c748 = Constraint(expr=   m.x448 + m.x468 + m.x488 + m.x508 - m.x528 + m.x548 == 0)

m.c749 = Constraint(expr=   m.x449 + m.x469 + m.x489 + m.x509 - m.x529 + m.x549 == 0)

m.c750 = Constraint(expr=   m.x450 + m.x470 + m.x490 + m.x510 - m.x530 + m.x550 == 0)

m.c751 = Constraint(expr=   m.x451 + m.x471 + m.x491 + m.x511 - m.x531 + m.x551 == 0)

m.c752 = Constraint(expr=   m.x452 + m.x472 + m.x492 + m.x512 - m.x532 + m.x552 == 0)

m.c753 = Constraint(expr=   m.x453 + m.x473 + m.x493 + m.x513 - m.x533 + m.x553 == 0)

m.c754 = Constraint(expr=   m.x454 + m.x474 + m.x494 + m.x514 - m.x534 + m.x554 == 0)

m.c755 = Constraint(expr=   m.x455 + m.x475 + m.x495 + m.x515 - m.x535 + m.x555 == 0)

m.c756 = Constraint(expr=   m.x456 + m.x476 + m.x496 + m.x516 - m.x536 + m.x556 == 0)

m.c757 = Constraint(expr=   m.x457 + m.x477 + m.x497 + m.x517 - m.x537 + m.x557 == 0)

m.c758 = Constraint(expr=   m.x458 + m.x478 + m.x498 + m.x518 - m.x538 + m.x558 == 0)

m.c759 = Constraint(expr=   m.x459 + m.x479 + m.x499 + m.x519 - m.x539 + m.x559 == 0)

m.c760 = Constraint(expr=   m.x460 + m.x480 + m.x500 + m.x520 - m.x540 + m.x560 == 0)

m.c761 = Constraint(expr=   m.x461 + m.x481 + m.x501 + m.x521 - m.x541 + m.x561 == 0)

m.c762 = Constraint(expr=   m.x462 + m.x482 + m.x502 + m.x522 - m.x542 + m.x562 == 0)

m.c763 = Constraint(expr=   m.x443 + m.x444 + m.x445 + m.x446 + m.x447 + m.x448 + m.x449 + m.x450 + m.x451 + m.x452
                          + m.x463 + m.x464 + m.x465 + m.x466 + m.x467 + m.x468 + m.x469 + m.x470 + m.x471 + m.x472
                          + m.x483 + m.x484 + m.x485 + m.x486 + m.x487 + m.x488 + m.x489 + m.x490 + m.x491 + m.x492
                          + m.x503 + m.x504 + m.x505 + m.x506 + m.x507 + m.x508 + m.x509 + m.x510 + m.x511 + m.x512
                          - m.x523 - m.x524 - m.x525 - m.x526 - m.x527 - m.x528 - m.x529 - m.x530 - m.x531 - m.x532
                          + m.x563 == 0)

m.c764 = Constraint(expr=   m.x453 + m.x454 + m.x455 + m.x456 + m.x457 + m.x458 + m.x459 + m.x460 + m.x461 + m.x462
                          + m.x473 + m.x474 + m.x475 + m.x476 + m.x477 + m.x478 + m.x479 + m.x480 + m.x481 + m.x482
                          + m.x493 + m.x494 + m.x495 + m.x496 + m.x497 + m.x498 + m.x499 + m.x500 + m.x501 + m.x502
                          + m.x513 + m.x514 + m.x515 + m.x516 + m.x517 + m.x518 + m.x519 + m.x520 + m.x521 + m.x522
                          - m.x533 - m.x534 - m.x535 - m.x536 - m.x537 - m.x538 - m.x539 - m.x540 - m.x541 - m.x542
                          + m.x564 == 0)

m.c765 = Constraint(expr=   m.x565 + m.x575 + m.x645 == 500)

m.c766 = Constraint(expr=   m.x566 + m.x576 - m.x645 + m.x646 - 400*m.b665 == 0)

m.c767 = Constraint(expr=   m.x567 + m.x577 - m.x646 + m.x647 - 400*m.b666 == 0)

m.c768 = Constraint(expr=   m.x568 + m.x578 - m.x647 + m.x648 - 400*m.b667 == 0)

m.c769 = Constraint(expr=   m.x569 + m.x579 - m.x648 + m.x649 - 400*m.b668 == 0)

m.c770 = Constraint(expr=   m.x570 + m.x580 - m.x649 + m.x650 - 400*m.b669 == 0)

m.c771 = Constraint(expr=   m.x571 + m.x581 - m.x650 + m.x651 - 400*m.b670 == 0)

m.c772 = Constraint(expr=   m.x572 + m.x582 - m.x651 + m.x652 - 400*m.b671 == 0)

m.c773 = Constraint(expr=   m.x573 + m.x583 - m.x652 + m.x653 - 400*m.b672 == 0)

m.c774 = Constraint(expr=   m.x574 + m.x584 - m.x653 + m.x654 - 400*m.b673 == 0)

m.c775 = Constraint(expr=   m.x585 + m.x595 + m.x655 == 500)

m.c776 = Constraint(expr=   m.x586 + m.x596 - m.x655 + m.x656 - 400*m.b675 == 0)

m.c777 = Constraint(expr=   m.x587 + m.x597 - m.x656 + m.x657 - 400*m.b676 == 0)

m.c778 = Constraint(expr=   m.x588 + m.x598 - m.x657 + m.x658 - 400*m.b677 == 0)

m.c779 = Constraint(expr=   m.x589 + m.x599 - m.x658 + m.x659 - 400*m.b678 == 0)

m.c780 = Constraint(expr=   m.x590 + m.x600 - m.x659 + m.x660 - 400*m.b679 == 0)

m.c781 = Constraint(expr=   m.x591 + m.x601 - m.x660 + m.x661 - 400*m.b680 == 0)

m.c782 = Constraint(expr=   m.x592 + m.x602 - m.x661 + m.x662 - 400*m.b681 == 0)

m.c783 = Constraint(expr=   m.x593 + m.x603 - m.x662 + m.x663 - 400*m.b682 == 0)

m.c784 = Constraint(expr=   m.x594 + m.x604 - m.x663 + m.x664 - 400*m.b683 == 0)

m.c785 = Constraint(expr= - m.x645 - m.x866 <= -300)

m.c786 = Constraint(expr= - m.x646 - m.x867 <= -300)

m.c787 = Constraint(expr= - m.x647 - m.x868 <= -300)

m.c788 = Constraint(expr= - m.x648 - m.x869 <= -300)

m.c789 = Constraint(expr= - m.x649 - m.x870 <= -300)

m.c790 = Constraint(expr= - m.x650 - m.x871 <= -300)

m.c791 = Constraint(expr= - m.x651 - m.x872 <= -300)

m.c792 = Constraint(expr= - m.x652 - m.x873 <= -300)

m.c793 = Constraint(expr= - m.x653 - m.x874 <= -300)

m.c794 = Constraint(expr= - m.x654 - m.x875 <= -300)

m.c795 = Constraint(expr= - m.x655 - m.x876 <= -300)

m.c796 = Constraint(expr= - m.x656 - m.x877 <= -300)

m.c797 = Constraint(expr= - m.x657 - m.x878 <= -300)

m.c798 = Constraint(expr= - m.x658 - m.x879 <= -300)

m.c799 = Constraint(expr= - m.x659 - m.x880 <= -300)

m.c800 = Constraint(expr= - m.x660 - m.x881 <= -300)

m.c801 = Constraint(expr= - m.x661 - m.x882 <= -300)

m.c802 = Constraint(expr= - m.x662 - m.x883 <= -300)

m.c803 = Constraint(expr= - m.x663 - m.x884 <= -300)

m.c804 = Constraint(expr= - m.x664 - m.x885 <= -300)

m.c805 = Constraint(expr=   m.x866 <= 300)

m.c806 = Constraint(expr=   m.x867 <= 300)

m.c807 = Constraint(expr=   m.x868 <= 300)

m.c808 = Constraint(expr=   m.x869 <= 300)

m.c809 = Constraint(expr=   m.x870 <= 300)

m.c810 = Constraint(expr=   m.x871 <= 300)

m.c811 = Constraint(expr=   m.x872 <= 300)

m.c812 = Constraint(expr=   m.x873 <= 300)

m.c813 = Constraint(expr=   m.x874 <= 300)

m.c814 = Constraint(expr=   m.x875 <= 300)

m.c815 = Constraint(expr=   m.x876 <= 300)

m.c816 = Constraint(expr=   m.x877 <= 300)

m.c817 = Constraint(expr=   m.x878 <= 300)

m.c818 = Constraint(expr=   m.x879 <= 300)

m.c819 = Constraint(expr=   m.x880 <= 300)

m.c820 = Constraint(expr=   m.x881 <= 300)

m.c821 = Constraint(expr=   m.x882 <= 300)

m.c822 = Constraint(expr=   m.x883 <= 300)

m.c823 = Constraint(expr=   m.x884 <= 300)

m.c824 = Constraint(expr=   m.x885 <= 300)

m.c825 = Constraint(expr=   m.x645 + m.x655 <= 2200)

m.c826 = Constraint(expr=   m.x646 + m.x656 <= 2200)

m.c827 = Constraint(expr=   m.x647 + m.x657 <= 2200)

m.c828 = Constraint(expr=   m.x648 + m.x658 <= 2200)

m.c829 = Constraint(expr=   m.x649 + m.x659 <= 2200)

m.c830 = Constraint(expr=   m.x650 + m.x660 <= 2200)

m.c831 = Constraint(expr=   m.x651 + m.x661 <= 2200)

m.c832 = Constraint(expr=   m.x652 + m.x662 <= 2200)

m.c833 = Constraint(expr=   m.x653 + m.x663 <= 2200)

m.c834 = Constraint(expr=   m.x654 + m.x664 <= 2200)

m.c835 = Constraint(expr= - m.x565 - m.x585 + m.x605 == 0)

m.c836 = Constraint(expr= - m.x566 - m.x586 + m.x606 == 0)

m.c837 = Constraint(expr= - m.x567 - m.x587 + m.x607 == 0)

m.c838 = Constraint(expr= - m.x568 - m.x588 + m.x608 == 0)

m.c839 = Constraint(expr= - m.x569 - m.x589 + m.x609 == 0)

m.c840 = Constraint(expr= - m.x570 - m.x590 + m.x610 == 0)

m.c841 = Constraint(expr= - m.x571 - m.x591 + m.x611 == 0)

m.c842 = Constraint(expr= - m.x572 - m.x592 + m.x612 == 0)

m.c843 = Constraint(expr= - m.x573 - m.x593 + m.x613 == 0)

m.c844 = Constraint(expr= - m.x574 - m.x594 + m.x614 == 0)

m.c845 = Constraint(expr= - m.x575 - m.x595 + m.x615 == 0)

m.c846 = Constraint(expr= - m.x576 - m.x596 + m.x616 == 0)

m.c847 = Constraint(expr= - m.x577 - m.x597 + m.x617 == 0)

m.c848 = Constraint(expr= - m.x578 - m.x598 + m.x618 == 0)

m.c849 = Constraint(expr= - m.x579 - m.x599 + m.x619 == 0)

m.c850 = Constraint(expr= - m.x580 - m.x600 + m.x620 == 0)

m.c851 = Constraint(expr= - m.x581 - m.x601 + m.x621 == 0)

m.c852 = Constraint(expr= - m.x582 - m.x602 + m.x622 == 0)

m.c853 = Constraint(expr= - m.x583 - m.x603 + m.x623 == 0)

m.c854 = Constraint(expr= - m.x584 - m.x604 + m.x624 == 0)

m.c855 = Constraint(expr= - m.x605 + m.b625 <= 0)

m.c856 = Constraint(expr= - m.x606 + m.b626 <= 0)

m.c857 = Constraint(expr= - m.x607 + m.b627 <= 0)

m.c858 = Constraint(expr= - m.x608 + m.b628 <= 0)

m.c859 = Constraint(expr= - m.x609 + m.b629 <= 0)

m.c860 = Constraint(expr= - m.x610 + m.b630 <= 0)

m.c861 = Constraint(expr= - m.x611 + m.b631 <= 0)

m.c862 = Constraint(expr= - m.x612 + m.b632 <= 0)

m.c863 = Constraint(expr= - m.x613 + m.b633 <= 0)

m.c864 = Constraint(expr= - m.x614 + m.b634 <= 0)

m.c865 = Constraint(expr= - m.x615 + m.b635 <= 0)

m.c866 = Constraint(expr= - m.x616 + m.b636 <= 0)

m.c867 = Constraint(expr= - m.x617 + m.b637 <= 0)

m.c868 = Constraint(expr= - m.x618 + m.b638 <= 0)

m.c869 = Constraint(expr= - m.x619 + m.b639 <= 0)

m.c870 = Constraint(expr= - m.x620 + m.b640 <= 0)

m.c871 = Constraint(expr= - m.x621 + m.b641 <= 0)

m.c872 = Constraint(expr= - m.x622 + m.b642 <= 0)

m.c873 = Constraint(expr= - m.x623 + m.b643 <= 0)

m.c874 = Constraint(expr= - m.x624 + m.b644 <= 0)

m.c875 = Constraint(expr=   m.x605 - 500*m.b625 <= 0)

m.c876 = Constraint(expr=   m.x606 - 500*m.b626 <= 0)

m.c877 = Constraint(expr=   m.x607 - 500*m.b627 <= 0)

m.c878 = Constraint(expr=   m.x608 - 500*m.b628 <= 0)

m.c879 = Constraint(expr=   m.x609 - 500*m.b629 <= 0)

m.c880 = Constraint(expr=   m.x610 - 500*m.b630 <= 0)

m.c881 = Constraint(expr=   m.x611 - 500*m.b631 <= 0)

m.c882 = Constraint(expr=   m.x612 - 500*m.b632 <= 0)

m.c883 = Constraint(expr=   m.x613 - 500*m.b633 <= 0)

m.c884 = Constraint(expr=   m.x614 - 500*m.b634 <= 0)

m.c885 = Constraint(expr=   m.x615 - 500*m.b635 <= 0)

m.c886 = Constraint(expr=   m.x616 - 500*m.b636 <= 0)

m.c887 = Constraint(expr=   m.x617 - 500*m.b637 <= 0)

m.c888 = Constraint(expr=   m.x618 - 500*m.b638 <= 0)

m.c889 = Constraint(expr=   m.x619 - 500*m.b639 <= 0)

m.c890 = Constraint(expr=   m.x620 - 500*m.b640 <= 0)

m.c891 = Constraint(expr=   m.x621 - 500*m.b641 <= 0)

m.c892 = Constraint(expr=   m.x622 - 500*m.b642 <= 0)

m.c893 = Constraint(expr=   m.x623 - 500*m.b643 <= 0)

m.c894 = Constraint(expr=   m.x624 - 500*m.b644 <= 0)

m.c895 = Constraint(expr=   m.b625 <= 1)

m.c896 = Constraint(expr=   m.b626 <= 1)

m.c897 = Constraint(expr=   m.b627 <= 1)

m.c898 = Constraint(expr=   m.b628 <= 1)

m.c899 = Constraint(expr=   m.b629 <= 1)

m.c900 = Constraint(expr=   m.b630 <= 1)

m.c901 = Constraint(expr=   m.b631 <= 1)

m.c902 = Constraint(expr=   m.b632 <= 1)

m.c903 = Constraint(expr=   m.b633 <= 1)

m.c904 = Constraint(expr=   m.b634 <= 1)

m.c905 = Constraint(expr=   m.b635 <= 1)

m.c906 = Constraint(expr=   m.b636 <= 1)

m.c907 = Constraint(expr=   m.b637 <= 1)

m.c908 = Constraint(expr=   m.b638 <= 1)

m.c909 = Constraint(expr=   m.b639 <= 1)

m.c910 = Constraint(expr=   m.b640 <= 1)

m.c911 = Constraint(expr=   m.b641 <= 1)

m.c912 = Constraint(expr=   m.b642 <= 1)

m.c913 = Constraint(expr=   m.b643 <= 1)

m.c914 = Constraint(expr=   m.b644 <= 1)

m.c915 = Constraint(expr=   500*m.b625 + 500*m.b635 <= 1000)

m.c916 = Constraint(expr=   500*m.b626 + 500*m.b636 <= 1000)

m.c917 = Constraint(expr=   500*m.b627 + 500*m.b637 <= 1000)

m.c918 = Constraint(expr=   500*m.b628 + 500*m.b638 <= 1000)

m.c919 = Constraint(expr=   500*m.b629 + 500*m.b639 <= 1000)

m.c920 = Constraint(expr=   500*m.b630 + 500*m.b640 <= 1000)

m.c921 = Constraint(expr=   500*m.b631 + 500*m.b641 <= 1000)

m.c922 = Constraint(expr=   500*m.b632 + 500*m.b642 <= 1000)

m.c923 = Constraint(expr=   500*m.b633 + 500*m.b643 <= 1000)

m.c924 = Constraint(expr=   500*m.b634 + 500*m.b644 <= 1000)

m.c925 = Constraint(expr=   m.b685 + m.b695 == 1)

m.c926 = Constraint(expr=   m.b686 + m.b696 == 1)

m.c927 = Constraint(expr=   m.b687 + m.b697 == 1)

m.c928 = Constraint(expr=   m.b688 + m.b698 == 1)

m.c929 = Constraint(expr=   m.b689 + m.b699 == 1)

m.c930 = Constraint(expr=   m.b690 + m.b700 == 1)

m.c931 = Constraint(expr=   m.b691 + m.b701 == 1)

m.c932 = Constraint(expr=   m.b692 + m.b702 == 1)

m.c933 = Constraint(expr=   m.b693 + m.b703 == 1)

m.c934 = Constraint(expr=   m.b694 + m.b704 == 1)

m.c935 = Constraint(expr=   m.b665 - m.b685 <= 0)

m.c936 = Constraint(expr=   m.b666 - m.b686 <= 0)

m.c937 = Constraint(expr=   m.b667 - m.b687 <= 0)

m.c938 = Constraint(expr=   m.b668 - m.b688 <= 0)

m.c939 = Constraint(expr=   m.b669 - m.b689 <= 0)

m.c940 = Constraint(expr=   m.b670 - m.b690 <= 0)

m.c941 = Constraint(expr=   m.b671 - m.b691 <= 0)

m.c942 = Constraint(expr=   m.b672 - m.b692 <= 0)

m.c943 = Constraint(expr=   m.b673 - m.b693 <= 0)

m.c944 = Constraint(expr=   m.b674 - m.b694 <= 0)

m.c945 = Constraint(expr=   m.b675 - m.b695 <= 0)

m.c946 = Constraint(expr=   m.b676 - m.b696 <= 0)

m.c947 = Constraint(expr=   m.b677 - m.b697 <= 0)

m.c948 = Constraint(expr=   m.b678 - m.b698 <= 0)

m.c949 = Constraint(expr=   m.b679 - m.b699 <= 0)

m.c950 = Constraint(expr=   m.b680 - m.b700 <= 0)

m.c951 = Constraint(expr=   m.b681 - m.b701 <= 0)

m.c952 = Constraint(expr=   m.b682 - m.b702 <= 0)

m.c953 = Constraint(expr=   m.b683 - m.b703 <= 0)

m.c954 = Constraint(expr=   m.b684 - m.b704 <= 0)

m.c955 = Constraint(expr= - m.b685 + m.b705 >= 0)

m.c956 = Constraint(expr=   m.b685 - m.b686 + m.b706 >= 0)

m.c957 = Constraint(expr=   m.b686 - m.b687 + m.b707 >= 0)

m.c958 = Constraint(expr=   m.b687 - m.b688 + m.b708 >= 0)

m.c959 = Constraint(expr=   m.b688 - m.b689 + m.b709 >= 0)

m.c960 = Constraint(expr=   m.b689 - m.b690 + m.b710 >= 0)

m.c961 = Constraint(expr=   m.b690 - m.b691 + m.b711 >= 0)

m.c962 = Constraint(expr=   m.b691 - m.b692 + m.b712 >= 0)

m.c963 = Constraint(expr=   m.b692 - m.b693 + m.b713 >= 0)

m.c964 = Constraint(expr=   m.b693 - m.b694 + m.b714 >= 0)

m.c965 = Constraint(expr= - m.b695 + m.b715 >= 0)

m.c966 = Constraint(expr=   m.b695 - m.b696 + m.b716 >= 0)

m.c967 = Constraint(expr=   m.b696 - m.b697 + m.b717 >= 0)

m.c968 = Constraint(expr=   m.b697 - m.b698 + m.b718 >= 0)

m.c969 = Constraint(expr=   m.b698 - m.b699 + m.b719 >= 0)

m.c970 = Constraint(expr=   m.b699 - m.b700 + m.b720 >= 0)

m.c971 = Constraint(expr=   m.b700 - m.b701 + m.b721 >= 0)

m.c972 = Constraint(expr=   m.b701 - m.b702 + m.b722 >= 0)

m.c973 = Constraint(expr=   m.b702 - m.b703 + m.b723 >= 0)

m.c974 = Constraint(expr=   m.b703 - m.b704 + m.b724 >= 0)

m.c975 = Constraint(expr= - 30400*m.b665 - 12800*m.b675 - 1600*m.b685 - 3200*m.b695 - 16000*m.b705 - 32000*m.b715
                          + m.x725 == 0)

m.c976 = Constraint(expr= - 30400*m.b666 - 12800*m.b676 - 1600*m.b686 - 3200*m.b696 - 16000*m.b706 - 32000*m.b716
                          + m.x726 == 0)

m.c977 = Constraint(expr= - 30400*m.b667 - 12800*m.b677 - 1600*m.b687 - 3200*m.b697 - 16000*m.b707 - 32000*m.b717
                          + m.x727 == 0)

m.c978 = Constraint(expr= - 30400*m.b668 - 12800*m.b678 - 1600*m.b688 - 3200*m.b698 - 16000*m.b708 - 32000*m.b718
                          + m.x728 == 0)

m.c979 = Constraint(expr= - 30400*m.b669 - 12800*m.b679 - 1600*m.b689 - 3200*m.b699 - 16000*m.b709 - 32000*m.b719
                          + m.x729 == 0)

m.c980 = Constraint(expr= - 30400*m.b670 - 12800*m.b680 - 1600*m.b690 - 3200*m.b700 - 16000*m.b710 - 32000*m.b720
                          + m.x730 == 0)

m.c981 = Constraint(expr= - 30400*m.b671 - 12800*m.b681 - 1600*m.b691 - 3200*m.b701 - 16000*m.b711 - 32000*m.b721
                          + m.x731 == 0)

m.c982 = Constraint(expr= - 30400*m.b672 - 12800*m.b682 - 1600*m.b692 - 3200*m.b702 - 16000*m.b712 - 32000*m.b722
                          + m.x732 == 0)

m.c983 = Constraint(expr= - 30400*m.b673 - 12800*m.b683 - 1600*m.b693 - 3200*m.b703 - 16000*m.b713 - 32000*m.b723
                          + m.x733 == 0)

m.c984 = Constraint(expr= - 30400*m.b674 - 12800*m.b684 - 1600*m.b694 - 3200*m.b704 - 16000*m.b714 - 32000*m.b724
                          + m.x734 == 0)

m.c985 = Constraint(expr= - m.x645 - m.x655 + m.x735 - 2*m.x866 - 2*m.x876 == 0)

m.c986 = Constraint(expr= - m.x646 - m.x656 + m.x736 - 2*m.x867 - 2*m.x877 == 0)

m.c987 = Constraint(expr= - m.x647 - m.x657 + m.x737 - 2*m.x868 - 2*m.x878 == 0)

m.c988 = Constraint(expr= - m.x648 - m.x658 + m.x738 - 2*m.x869 - 2*m.x879 == 0)

m.c989 = Constraint(expr= - m.x649 - m.x659 + m.x739 - 2*m.x870 - 2*m.x880 == 0)

m.c990 = Constraint(expr= - m.x650 - m.x660 + m.x740 - 2*m.x871 - 2*m.x881 == 0)

m.c991 = Constraint(expr= - m.x651 - m.x661 + m.x741 - 2*m.x872 - 2*m.x882 == 0)

m.c992 = Constraint(expr= - m.x652 - m.x662 + m.x742 - 2*m.x873 - 2*m.x883 == 0)

m.c993 = Constraint(expr= - m.x653 - m.x663 + m.x743 - 2*m.x874 - 2*m.x884 == 0)

m.c994 = Constraint(expr= - m.x654 - m.x664 + m.x744 - 2*m.x875 - 2*m.x885 == 0)

m.c995 = Constraint(expr= - m.x565 - m.x575 - m.x585 - m.x595 + m.x745 == 0)

m.c996 = Constraint(expr= - m.x566 - m.x576 - m.x586 - m.x596 - 400*m.b665 - 400*m.b675 + m.x746 == 0)

m.c997 = Constraint(expr= - m.x567 - m.x577 - m.x587 - m.x597 - 400*m.b666 - 400*m.b676 + m.x747 == 0)

m.c998 = Constraint(expr= - m.x568 - m.x578 - m.x588 - m.x598 - 400*m.b667 - 400*m.b677 + m.x748 == 0)

m.c999 = Constraint(expr= - m.x569 - m.x579 - m.x589 - m.x599 - 400*m.b668 - 400*m.b678 + m.x749 == 0)

m.c1000 = Constraint(expr= - m.x570 - m.x580 - m.x590 - m.x600 - 400*m.b669 - 400*m.b679 + m.x750 == 0)

m.c1001 = Constraint(expr= - m.x571 - m.x581 - m.x591 - m.x601 - 400*m.b670 - 400*m.b680 + m.x751 == 0)

m.c1002 = Constraint(expr= - m.x572 - m.x582 - m.x592 - m.x602 - 400*m.b671 - 400*m.b681 + m.x752 == 0)

m.c1003 = Constraint(expr= - m.x573 - m.x583 - m.x593 - m.x603 - 400*m.b672 - 400*m.b682 + m.x753 == 0)

m.c1004 = Constraint(expr= - m.x574 - m.x584 - m.x594 - m.x604 - 400*m.b673 - 400*m.b683 + m.x754 == 0)

m.c1005 = Constraint(expr= - 20*m.x605 - 10*m.x615 - 5000*m.b625 - 3000*m.b635 + m.x755 == 0)

m.c1006 = Constraint(expr= - 20*m.x606 - 10*m.x616 - 5000*m.b626 - 3000*m.b636 + m.x756 == 0)

m.c1007 = Constraint(expr= - 20*m.x607 - 10*m.x617 - 5000*m.b627 - 3000*m.b637 + m.x757 == 0)

m.c1008 = Constraint(expr= - 20*m.x608 - 10*m.x618 - 5000*m.b628 - 3000*m.b638 + m.x758 == 0)

m.c1009 = Constraint(expr= - 20*m.x609 - 10*m.x619 - 5000*m.b629 - 3000*m.b639 + m.x759 == 0)

m.c1010 = Constraint(expr= - 20*m.x610 - 10*m.x620 - 5000*m.b630 - 3000*m.b640 + m.x760 == 0)

m.c1011 = Constraint(expr= - 20*m.x611 - 10*m.x621 - 5000*m.b631 - 3000*m.b641 + m.x761 == 0)

m.c1012 = Constraint(expr= - 20*m.x612 - 10*m.x622 - 5000*m.b632 - 3000*m.b642 + m.x762 == 0)

m.c1013 = Constraint(expr= - 20*m.x613 - 10*m.x623 - 5000*m.b633 - 3000*m.b643 + m.x763 == 0)

m.c1014 = Constraint(expr= - 20*m.x614 - 10*m.x624 - 5000*m.b634 - 3000*m.b644 + m.x764 == 0)

m.c1015 = Constraint(expr= - 700*m.x565 - 600*m.x575 - 700*m.x585 - 600*m.x595 + m.x765 == 0)

m.c1016 = Constraint(expr= - 700*m.x566 - 600*m.x576 - 700*m.x586 - 600*m.x596 + m.x766 == 0)

m.c1017 = Constraint(expr= - 700*m.x567 - 600*m.x577 - 700*m.x587 - 600*m.x597 + m.x767 == 0)

m.c1018 = Constraint(expr= - 700*m.x568 - 600*m.x578 - 700*m.x588 - 600*m.x598 + m.x768 == 0)

m.c1019 = Constraint(expr= - 700*m.x569 - 600*m.x579 - 700*m.x589 - 600*m.x599 + m.x769 == 0)

m.c1020 = Constraint(expr= - 700*m.x570 - 600*m.x580 - 700*m.x590 - 600*m.x600 + m.x770 == 0)

m.c1021 = Constraint(expr= - 700*m.x571 - 600*m.x581 - 700*m.x591 - 600*m.x601 + m.x771 == 0)

m.c1022 = Constraint(expr= - 700*m.x572 - 600*m.x582 - 700*m.x592 - 600*m.x602 + m.x772 == 0)

m.c1023 = Constraint(expr= - 700*m.x573 - 600*m.x583 - 700*m.x593 - 600*m.x603 + m.x773 == 0)

m.c1024 = Constraint(expr= - 700*m.x574 - 600*m.x584 - 700*m.x594 - 600*m.x604 + m.x774 == 0)

m.c1025 = Constraint(expr=   m.x725 + m.x735 + m.x745 + m.x755 - m.x765 + m.x775 == 0)

m.c1026 = Constraint(expr=   m.x726 + m.x736 + m.x746 + m.x756 - m.x766 + m.x776 == 0)

m.c1027 = Constraint(expr=   m.x727 + m.x737 + m.x747 + m.x757 - m.x767 + m.x777 == 0)

m.c1028 = Constraint(expr=   m.x728 + m.x738 + m.x748 + m.x758 - m.x768 + m.x778 == 0)

m.c1029 = Constraint(expr=   m.x729 + m.x739 + m.x749 + m.x759 - m.x769 + m.x779 == 0)

m.c1030 = Constraint(expr=   m.x730 + m.x740 + m.x750 + m.x760 - m.x770 + m.x780 == 0)

m.c1031 = Constraint(expr=   m.x731 + m.x741 + m.x751 + m.x761 - m.x771 + m.x781 == 0)

m.c1032 = Constraint(expr=   m.x732 + m.x742 + m.x752 + m.x762 - m.x772 + m.x782 == 0)

m.c1033 = Constraint(expr=   m.x733 + m.x743 + m.x753 + m.x763 - m.x773 + m.x783 == 0)

m.c1034 = Constraint(expr=   m.x734 + m.x744 + m.x754 + m.x764 - m.x774 + m.x784 == 0)

m.c1035 = Constraint(expr=   m.x725 + m.x726 + m.x727 + m.x728 + m.x729 + m.x730 + m.x731 + m.x732 + m.x733 + m.x734
                           + m.x735 + m.x736 + m.x737 + m.x738 + m.x739 + m.x740 + m.x741 + m.x742 + m.x743 + m.x744
                           + m.x745 + m.x746 + m.x747 + m.x748 + m.x749 + m.x750 + m.x751 + m.x752 + m.x753 + m.x754
                           + m.x755 + m.x756 + m.x757 + m.x758 + m.x759 + m.x760 + m.x761 + m.x762 + m.x763 + m.x764
                           - m.x765 - m.x766 - m.x767 - m.x768 - m.x769 - m.x770 - m.x771 - m.x772 - m.x773 - m.x774
                           + m.x785 == 0)

m.c1036 = Constraint(expr= - m.x241 - m.x242 - m.x563 - m.x564 - m.x785 + m.x886 == 0)

m.c1037 = Constraint(expr= - 0.1*m.x121 - 0.1*m.x122 - 0.1*m.x123 - 0.1*m.x124 - 0.1*m.x125 - 0.1*m.x126 - 0.1*m.x127
                           - 0.1*m.x128 - 0.1*m.x129 - 0.1*m.x130 + m.x887 == 0)

m.c1038 = Constraint(expr= - 0.1*m.x131 - 0.1*m.x132 - 0.1*m.x133 - 0.1*m.x134 - 0.1*m.x135 - 0.1*m.x136 - 0.1*m.x137
                           - 0.1*m.x138 - 0.1*m.x139 - 0.1*m.x140 + m.x888 == 0)

m.c1039 = Constraint(expr=   m.x50 >= 120)

m.c1040 = Constraint(expr=   m.x60 >= 120)

m.c1041 = Constraint(expr=   m.x70 >= 120)

m.c1042 = Constraint(expr=   m.x80 >= 120)

m.c1043 = Constraint(expr=   m.x412 >= 300)

m.c1044 = Constraint(expr=   m.x422 >= 400)

m.c1045 = Constraint(expr=   m.x432 >= 300)

m.c1046 = Constraint(expr=   m.x442 >= 400)

m.c1047 = Constraint(expr=   m.x654 >= 500)

m.c1048 = Constraint(expr=   m.x664 >= 500)

m.c1049 = Constraint(expr=   m.x889 == 1)

m.c1050 = Constraint(expr= - 2.12407124984601E-6*m.x241 + m.x890 == -0.802287199921834)

m.c1051 = Constraint(expr= - 7.77033379799929E-7*m.x242 + m.x891 == 0.278519844655487)

m.c1052 = Constraint(expr= - 6.59485311283662E-7*m.x563 + m.x892 == 0.0177882973012542)

m.c1053 = Constraint(expr= - 9.57487552661815E-7*m.x564 + m.x893 == 0.015319800842589)

m.c1054 = Constraint(expr= - 1.95158888609161E-6*m.x785 + m.x894 == -3.04198453170649)

m.c1055 = Constraint(expr= - 2.5*m.x887 + m.x895 == -1.5)

m.c1056 = Constraint(expr= - 2.5*m.x888 + m.x896 == -1.5)
