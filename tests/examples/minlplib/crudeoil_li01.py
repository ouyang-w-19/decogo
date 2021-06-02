#  MINLP written by GAMS Convert at 04/21/18 13:51:20
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        696      177      207      312        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        345      297       48        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2022     1910      112        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b15 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b18 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b19 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b21 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b23 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b24 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b25 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b26 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b27 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b28 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b29 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b30 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b31 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b32 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b33 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b34 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b35 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b36 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b38 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b39 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b40 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b41 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b42 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b43 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b44 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b45 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b46 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b47 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b48 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,560),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,650),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,650),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,650),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,650),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,650),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,840),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,850),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,850),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,560),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,650),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,650),initialize=0)
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
m.x105 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,340),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,340),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,340),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,340),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,340),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,340),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,340),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,340),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x235 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x255 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,72),initialize=0)
m.x257 = Var(within=Reals,bounds=(50,610),initialize=50)
m.x258 = Var(within=Reals,bounds=(50,700),initialize=50)
m.x259 = Var(within=Reals,bounds=(50,700),initialize=50)
m.x260 = Var(within=Reals,bounds=(50,700),initialize=50)
m.x261 = Var(within=Reals,bounds=(50,700),initialize=50)
m.x262 = Var(within=Reals,bounds=(50,700),initialize=50)
m.x263 = Var(within=Reals,bounds=(50,700),initialize=50)
m.x264 = Var(within=Reals,bounds=(50,700),initialize=50)
m.x265 = Var(within=Reals,bounds=(50,890),initialize=50)
m.x266 = Var(within=Reals,bounds=(50,900),initialize=50)
m.x267 = Var(within=Reals,bounds=(50,900),initialize=50)
m.x268 = Var(within=Reals,bounds=(50,900),initialize=50)
m.x269 = Var(within=Reals,bounds=(50,610),initialize=50)
m.x270 = Var(within=Reals,bounds=(50,700),initialize=50)
m.x271 = Var(within=Reals,bounds=(50,700),initialize=50)
m.x272 = Var(within=Reals,bounds=(50,700),initialize=50)
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
m.x305 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x306 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x307 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x309 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x311 = Var(within=Reals,bounds=(0.645161290322581,0.833333333333333),initialize=0.645161290322581)
m.x312 = Var(within=Reals,bounds=(0.0460829493087558,0.952380952380952),initialize=0.0460829493087558)
m.x313 = Var(within=Reals,bounds=(0.0032916392363397,0.952380952380952),initialize=0.0032916392363397)
m.x314 = Var(within=Reals,bounds=(0.000235117088309978,0.952380952380952),initialize=0.000235117088309978)
m.x315 = Var(within=Reals,bounds=(0.166666666666667,0.354838709677419),initialize=0.166666666666667)
m.x316 = Var(within=Reals,bounds=(0.0119047619047619,0.444444444444444),initialize=0.0119047619047619)
m.x317 = Var(within=Reals,bounds=(0.000850340136054422,0.444444444444444),initialize=0.000850340136054422)
m.x318 = Var(within=Reals,bounds=(6.07385811467444E-5,0.444444444444444),initialize=6.07385811467444E-5)
m.x319 = Var(within=Reals,bounds=(0.166666666666667,0.6875),initialize=0.166666666666667)
m.x320 = Var(within=Reals,bounds=(0.0119047619047619,0.914529914529915),initialize=0.0119047619047619)
m.x321 = Var(within=Reals,bounds=(0.000850340136054422,0.914529914529915),initialize=0.000850340136054422)
m.x322 = Var(within=Reals,bounds=(6.07385811467444E-5,0.914529914529915),initialize=6.07385811467444E-5)
m.x323 = Var(within=Reals,bounds=(0.3125,0.833333333333333),initialize=0.3125)
m.x324 = Var(within=Reals,bounds=(0.0223214285714286,0.952380952380952),initialize=0.0223214285714286)
m.x325 = Var(within=Reals,bounds=(0.00159438775510204,0.952380952380952),initialize=0.00159438775510204)
m.x326 = Var(within=Reals,bounds=(0.000113884839650146,0.952380952380952),initialize=0.000113884839650146)
m.x327 = Var(within=Reals,bounds=(0.0909090909090909,0.661016949152542),initialize=0.0909090909090909)
m.x328 = Var(within=Reals,bounds=(0.00505050505050505,0.897435897435897),initialize=0.00505050505050505)
m.x329 = Var(within=Reals,bounds=(0.000280583613916947,0.897435897435897),initialize=0.000280583613916947)
m.x330 = Var(within=Reals,bounds=(1.55879785509415E-5,0.897435897435897),initialize=1.55879785509415E-5)
m.x331 = Var(within=Reals,bounds=(0.338983050847458,0.909090909090909),initialize=0.338983050847458)
m.x332 = Var(within=Reals,bounds=(0.0188323917137476,0.971428571428571),initialize=0.0188323917137476)
m.x333 = Var(within=Reals,bounds=(0.00104624398409709,0.971428571428571),initialize=0.00104624398409709)
m.x334 = Var(within=Reals,bounds=(5.81246657831718E-5,0.971428571428571),initialize=5.81246657831718E-5)
m.x335 = Var(within=Reals,bounds=(0.419354838709677,0.716666666666667),initialize=0.419354838709677)
m.x336 = Var(within=Reals,bounds=(0.0299539170506912,0.919047619047619),initialize=0.0299539170506912)
m.x337 = Var(within=Reals,bounds=(0.0021395655036208,0.919047619047619),initialize=0.0021395655036208)
m.x338 = Var(within=Reals,bounds=(0.000152826107401486,0.919047619047619),initialize=0.000152826107401486)
m.x339 = Var(within=Reals,bounds=(0.283333333333333,0.580645161290323),initialize=0.283333333333333)
m.x340 = Var(within=Reals,bounds=(0.0202380952380952,0.638888888888889),initialize=0.0202380952380952)
m.x341 = Var(within=Reals,bounds=(0.00144557823129252,0.638888888888889),initialize=0.00144557823129252)
m.x342 = Var(within=Reals,bounds=(0.000103255587949465,0.638888888888889),initialize=0.000103255587949465)
m.x343 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x344 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   3*m.x65 + 3*m.x66 + 3*m.x67 + 3*m.x68 + 4.5*m.x69 + 4.5*m.x70 + 4.5*m.x71 + 4.5*m.x72
                        + 5*m.x73 + 5*m.x74 + 5*m.x75 + 5*m.x76 + 6*m.x77 + 6*m.x78 + 6*m.x79 + 6*m.x80 + 5*m.x81
                        + 5*m.x82 + 5*m.x83 + 5*m.x84 + 6*m.x85 + 6*m.x86 + 6*m.x87 + 6*m.x88 + 3*m.x89 + 3*m.x90
                        + 3*m.x91 + 3*m.x92 + 4.5*m.x93 + 4.5*m.x94 + 4.5*m.x95 + 4.5*m.x96 - 5*m.x305 - 5*m.x306
                        - 5*m.x307 - 5*m.x308 - 5*m.x309 - 5*m.x310 - 1.8*m.x343 - m.x344, sense=maximize)

m.c1 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8 == 1)

m.c2 = Constraint(expr=   m.b9 + m.b10 + m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 == 1)

m.c3 = Constraint(expr=   m.b17 + m.b18 + m.b19 + m.b20 + m.b21 + m.b22 + m.b23 + m.b24 == 1)

m.c4 = Constraint(expr=   m.b25 + m.b26 + m.b27 + m.b28 + m.b29 + m.b30 + m.b31 + m.b32 == 1)

m.c5 = Constraint(expr= - m.x105 - 1.25*m.x145 + 1.25*m.x177 <= 0)

m.c6 = Constraint(expr= - m.x106 - 1.25*m.x146 + 1.25*m.x178 <= 0)

m.c7 = Constraint(expr= - m.x107 - 1.25*m.x147 + 1.25*m.x179 <= 0)

m.c8 = Constraint(expr= - m.x108 - 1.25*m.x148 + 1.25*m.x180 <= 0)

m.c9 = Constraint(expr= - m.x109 - 1.25*m.x149 + 1.25*m.x181 <= 0)

m.c10 = Constraint(expr= - m.x110 - 1.25*m.x150 + 1.25*m.x182 <= 0)

m.c11 = Constraint(expr= - m.x111 - 1.25*m.x151 + 1.25*m.x183 <= 0)

m.c12 = Constraint(expr= - m.x112 - 1.25*m.x152 + 1.25*m.x184 <= 0)

m.c13 = Constraint(expr= - m.x113 - 1.25*m.x153 + 1.25*m.x185 <= 0)

m.c14 = Constraint(expr= - m.x114 - 1.25*m.x154 + 1.25*m.x186 <= 0)

m.c15 = Constraint(expr= - m.x115 - 1.25*m.x155 + 1.25*m.x187 <= 0)

m.c16 = Constraint(expr= - m.x116 - 1.25*m.x156 + 1.25*m.x188 <= 0)

m.c17 = Constraint(expr= - m.x117 - 1.25*m.x157 + 1.25*m.x189 <= 0)

m.c18 = Constraint(expr= - m.x118 - 1.25*m.x158 + 1.25*m.x190 <= 0)

m.c19 = Constraint(expr= - m.x119 - 1.25*m.x159 + 1.25*m.x191 <= 0)

m.c20 = Constraint(expr= - m.x120 - 1.25*m.x160 + 1.25*m.x192 <= 0)

m.c21 = Constraint(expr= - m.x121 - 1.25*m.x161 + 1.25*m.x193 <= 0)

m.c22 = Constraint(expr= - m.x122 - 1.25*m.x162 + 1.25*m.x194 <= 0)

m.c23 = Constraint(expr= - m.x123 - 1.25*m.x163 + 1.25*m.x195 <= 0)

m.c24 = Constraint(expr= - m.x124 - 1.25*m.x164 + 1.25*m.x196 <= 0)

m.c25 = Constraint(expr= - m.x125 - 1.25*m.x165 + 1.25*m.x197 <= 0)

m.c26 = Constraint(expr= - m.x126 - 1.25*m.x166 + 1.25*m.x198 <= 0)

m.c27 = Constraint(expr= - m.x127 - 1.25*m.x167 + 1.25*m.x199 <= 0)

m.c28 = Constraint(expr= - m.x128 - 1.25*m.x168 + 1.25*m.x200 <= 0)

m.c29 = Constraint(expr= - m.x129 - 1.25*m.x169 + 1.25*m.x201 <= 0)

m.c30 = Constraint(expr= - m.x130 - 1.25*m.x170 + 1.25*m.x202 <= 0)

m.c31 = Constraint(expr= - m.x131 - 1.25*m.x171 + 1.25*m.x203 <= 0)

m.c32 = Constraint(expr= - m.x132 - 1.25*m.x172 + 1.25*m.x204 <= 0)

m.c33 = Constraint(expr= - m.x133 - 1.25*m.x173 + 1.25*m.x205 <= 0)

m.c34 = Constraint(expr= - m.x134 - 1.25*m.x174 + 1.25*m.x206 <= 0)

m.c35 = Constraint(expr= - m.x135 - 1.25*m.x175 + 1.25*m.x207 <= 0)

m.c36 = Constraint(expr= - m.x136 - 1.25*m.x176 + 1.25*m.x208 <= 0)

m.c37 = Constraint(expr=   m.x105 + 50*m.x145 - 50*m.x177 <= 0)

m.c38 = Constraint(expr=   m.x106 + 50*m.x146 - 50*m.x178 <= 0)

m.c39 = Constraint(expr=   m.x107 + 50*m.x147 - 50*m.x179 <= 0)

m.c40 = Constraint(expr=   m.x108 + 50*m.x148 - 50*m.x180 <= 0)

m.c41 = Constraint(expr=   m.x109 + 50*m.x149 - 50*m.x181 <= 0)

m.c42 = Constraint(expr=   m.x110 + 50*m.x150 - 50*m.x182 <= 0)

m.c43 = Constraint(expr=   m.x111 + 50*m.x151 - 50*m.x183 <= 0)

m.c44 = Constraint(expr=   m.x112 + 50*m.x152 - 50*m.x184 <= 0)

m.c45 = Constraint(expr=   m.x113 + 50*m.x153 - 50*m.x185 <= 0)

m.c46 = Constraint(expr=   m.x114 + 50*m.x154 - 50*m.x186 <= 0)

m.c47 = Constraint(expr=   m.x115 + 50*m.x155 - 50*m.x187 <= 0)

m.c48 = Constraint(expr=   m.x116 + 50*m.x156 - 50*m.x188 <= 0)

m.c49 = Constraint(expr=   m.x117 + 50*m.x157 - 50*m.x189 <= 0)

m.c50 = Constraint(expr=   m.x118 + 50*m.x158 - 50*m.x190 <= 0)

m.c51 = Constraint(expr=   m.x119 + 50*m.x159 - 50*m.x191 <= 0)

m.c52 = Constraint(expr=   m.x120 + 50*m.x160 - 50*m.x192 <= 0)

m.c53 = Constraint(expr=   m.x121 + 50*m.x161 - 50*m.x193 <= 0)

m.c54 = Constraint(expr=   m.x122 + 50*m.x162 - 50*m.x194 <= 0)

m.c55 = Constraint(expr=   m.x123 + 50*m.x163 - 50*m.x195 <= 0)

m.c56 = Constraint(expr=   m.x124 + 50*m.x164 - 50*m.x196 <= 0)

m.c57 = Constraint(expr=   m.x125 + 50*m.x165 - 50*m.x197 <= 0)

m.c58 = Constraint(expr=   m.x126 + 50*m.x166 - 50*m.x198 <= 0)

m.c59 = Constraint(expr=   m.x127 + 50*m.x167 - 50*m.x199 <= 0)

m.c60 = Constraint(expr=   m.x128 + 50*m.x168 - 50*m.x200 <= 0)

m.c61 = Constraint(expr=   m.x129 + 50*m.x169 - 50*m.x201 <= 0)

m.c62 = Constraint(expr=   m.x130 + 50*m.x170 - 50*m.x202 <= 0)

m.c63 = Constraint(expr=   m.x131 + 50*m.x171 - 50*m.x203 <= 0)

m.c64 = Constraint(expr=   m.x132 + 50*m.x172 - 50*m.x204 <= 0)

m.c65 = Constraint(expr=   m.x133 + 50*m.x173 - 50*m.x205 <= 0)

m.c66 = Constraint(expr=   m.x134 + 50*m.x174 - 50*m.x206 <= 0)

m.c67 = Constraint(expr=   m.x135 + 50*m.x175 - 50*m.x207 <= 0)

m.c68 = Constraint(expr=   m.x136 + 50*m.x176 - 50*m.x208 <= 0)

m.c69 = Constraint(expr= - 10*m.b1 + m.x105 == 0)

m.c70 = Constraint(expr= - 10*m.b2 + m.x106 == 0)

m.c71 = Constraint(expr= - 10*m.b3 + m.x107 == 0)

m.c72 = Constraint(expr= - 10*m.b4 + m.x108 == 0)

m.c73 = Constraint(expr= - 10*m.b5 + m.x109 == 0)

m.c74 = Constraint(expr= - 10*m.b6 + m.x110 == 0)

m.c75 = Constraint(expr= - 10*m.b7 + m.x111 == 0)

m.c76 = Constraint(expr= - 10*m.b8 + m.x112 == 0)

m.c77 = Constraint(expr= - 300*m.b9 + m.x113 == 0)

m.c78 = Constraint(expr= - 300*m.b10 + m.x114 == 0)

m.c79 = Constraint(expr= - 300*m.b11 + m.x115 == 0)

m.c80 = Constraint(expr= - 300*m.b12 + m.x116 == 0)

m.c81 = Constraint(expr= - 300*m.b13 + m.x117 == 0)

m.c82 = Constraint(expr= - 300*m.b14 + m.x118 == 0)

m.c83 = Constraint(expr= - 300*m.b15 + m.x119 == 0)

m.c84 = Constraint(expr= - 300*m.b16 + m.x120 == 0)

m.c85 = Constraint(expr= - 300*m.b17 + m.x121 == 0)

m.c86 = Constraint(expr= - 300*m.b18 + m.x122 == 0)

m.c87 = Constraint(expr= - 300*m.b19 + m.x123 == 0)

m.c88 = Constraint(expr= - 300*m.b20 + m.x124 == 0)

m.c89 = Constraint(expr= - 300*m.b21 + m.x125 == 0)

m.c90 = Constraint(expr= - 300*m.b22 + m.x126 == 0)

m.c91 = Constraint(expr= - 300*m.b23 + m.x127 == 0)

m.c92 = Constraint(expr= - 300*m.b24 + m.x128 == 0)

m.c93 = Constraint(expr= - 340*m.b25 + m.x129 == 0)

m.c94 = Constraint(expr= - 340*m.b26 + m.x130 == 0)

m.c95 = Constraint(expr= - 340*m.b27 + m.x131 == 0)

m.c96 = Constraint(expr= - 340*m.b28 + m.x132 == 0)

m.c97 = Constraint(expr= - 340*m.b29 + m.x133 == 0)

m.c98 = Constraint(expr= - 340*m.b30 + m.x134 == 0)

m.c99 = Constraint(expr= - 340*m.b31 + m.x135 == 0)

m.c100 = Constraint(expr= - 340*m.b32 + m.x136 == 0)

m.c101 = Constraint(expr=   72*m.b1 + m.x137 - m.x145 <= 72)

m.c102 = Constraint(expr=   72*m.b2 + m.x137 - m.x146 <= 72)

m.c103 = Constraint(expr=   72*m.b3 + m.x137 - m.x147 <= 72)

m.c104 = Constraint(expr=   72*m.b4 + m.x137 - m.x148 <= 72)

m.c105 = Constraint(expr=   72*m.b5 + m.x137 - m.x149 <= 72)

m.c106 = Constraint(expr=   72*m.b6 + m.x137 - m.x150 <= 72)

m.c107 = Constraint(expr=   72*m.b7 + m.x137 - m.x151 <= 72)

m.c108 = Constraint(expr=   72*m.b8 + m.x137 - m.x152 <= 72)

m.c109 = Constraint(expr=   72*m.b9 + m.x138 - m.x153 <= 72)

m.c110 = Constraint(expr=   72*m.b10 + m.x138 - m.x154 <= 72)

m.c111 = Constraint(expr=   72*m.b11 + m.x138 - m.x155 <= 72)

m.c112 = Constraint(expr=   72*m.b12 + m.x138 - m.x156 <= 72)

m.c113 = Constraint(expr=   72*m.b13 + m.x138 - m.x157 <= 72)

m.c114 = Constraint(expr=   72*m.b14 + m.x138 - m.x158 <= 72)

m.c115 = Constraint(expr=   72*m.b15 + m.x138 - m.x159 <= 72)

m.c116 = Constraint(expr=   72*m.b16 + m.x138 - m.x160 <= 72)

m.c117 = Constraint(expr=   72*m.b17 + m.x139 - m.x161 <= 72)

m.c118 = Constraint(expr=   72*m.b18 + m.x139 - m.x162 <= 72)

m.c119 = Constraint(expr=   72*m.b19 + m.x139 - m.x163 <= 72)

m.c120 = Constraint(expr=   72*m.b20 + m.x139 - m.x164 <= 72)

m.c121 = Constraint(expr=   72*m.b21 + m.x139 - m.x165 <= 72)

m.c122 = Constraint(expr=   72*m.b22 + m.x139 - m.x166 <= 72)

m.c123 = Constraint(expr=   72*m.b23 + m.x139 - m.x167 <= 72)

m.c124 = Constraint(expr=   72*m.b24 + m.x139 - m.x168 <= 72)

m.c125 = Constraint(expr=   72*m.b25 + m.x140 - m.x169 <= 72)

m.c126 = Constraint(expr=   72*m.b26 + m.x140 - m.x170 <= 72)

m.c127 = Constraint(expr=   72*m.b27 + m.x140 - m.x171 <= 72)

m.c128 = Constraint(expr=   72*m.b28 + m.x140 - m.x172 <= 72)

m.c129 = Constraint(expr=   72*m.b29 + m.x140 - m.x173 <= 72)

m.c130 = Constraint(expr=   72*m.b30 + m.x140 - m.x174 <= 72)

m.c131 = Constraint(expr=   72*m.b31 + m.x140 - m.x175 <= 72)

m.c132 = Constraint(expr=   72*m.b32 + m.x140 - m.x176 <= 72)

m.c133 = Constraint(expr= - 72*m.b1 + m.x141 - m.x177 >= -72)

m.c134 = Constraint(expr= - 72*m.b2 + m.x141 - m.x178 >= -72)

m.c135 = Constraint(expr= - 72*m.b3 + m.x141 - m.x179 >= -72)

m.c136 = Constraint(expr= - 72*m.b4 + m.x141 - m.x180 >= -72)

m.c137 = Constraint(expr= - 72*m.b5 + m.x141 - m.x181 >= -72)

m.c138 = Constraint(expr= - 72*m.b6 + m.x141 - m.x182 >= -72)

m.c139 = Constraint(expr= - 72*m.b7 + m.x141 - m.x183 >= -72)

m.c140 = Constraint(expr= - 72*m.b8 + m.x141 - m.x184 >= -72)

m.c141 = Constraint(expr= - 72*m.b9 + m.x142 - m.x185 >= -72)

m.c142 = Constraint(expr= - 72*m.b10 + m.x142 - m.x186 >= -72)

m.c143 = Constraint(expr= - 72*m.b11 + m.x142 - m.x187 >= -72)

m.c144 = Constraint(expr= - 72*m.b12 + m.x142 - m.x188 >= -72)

m.c145 = Constraint(expr= - 72*m.b13 + m.x142 - m.x189 >= -72)

m.c146 = Constraint(expr= - 72*m.b14 + m.x142 - m.x190 >= -72)

m.c147 = Constraint(expr= - 72*m.b15 + m.x142 - m.x191 >= -72)

m.c148 = Constraint(expr= - 72*m.b16 + m.x142 - m.x192 >= -72)

m.c149 = Constraint(expr= - 72*m.b17 + m.x143 - m.x193 >= -72)

m.c150 = Constraint(expr= - 72*m.b18 + m.x143 - m.x194 >= -72)

m.c151 = Constraint(expr= - 72*m.b19 + m.x143 - m.x195 >= -72)

m.c152 = Constraint(expr= - 72*m.b20 + m.x143 - m.x196 >= -72)

m.c153 = Constraint(expr= - 72*m.b21 + m.x143 - m.x197 >= -72)

m.c154 = Constraint(expr= - 72*m.b22 + m.x143 - m.x198 >= -72)

m.c155 = Constraint(expr= - 72*m.b23 + m.x143 - m.x199 >= -72)

m.c156 = Constraint(expr= - 72*m.b24 + m.x143 - m.x200 >= -72)

m.c157 = Constraint(expr= - 72*m.b25 + m.x144 - m.x201 >= -72)

m.c158 = Constraint(expr= - 72*m.b26 + m.x144 - m.x202 >= -72)

m.c159 = Constraint(expr= - 72*m.b27 + m.x144 - m.x203 >= -72)

m.c160 = Constraint(expr= - 72*m.b28 + m.x144 - m.x204 >= -72)

m.c161 = Constraint(expr= - 72*m.b29 + m.x144 - m.x205 >= -72)

m.c162 = Constraint(expr= - 72*m.b30 + m.x144 - m.x206 >= -72)

m.c163 = Constraint(expr= - 72*m.b31 + m.x144 - m.x207 >= -72)

m.c164 = Constraint(expr= - 72*m.b32 + m.x144 - m.x208 >= -72)

m.c165 = Constraint(expr=   m.x138 - m.x141 >= 0)

m.c166 = Constraint(expr=   m.x139 - m.x142 >= 0)

m.c167 = Constraint(expr=   m.x140 - m.x143 >= 0)

m.c168 = Constraint(expr= - m.x257 + m.x273 + m.x277 == 0)

m.c169 = Constraint(expr= - m.x258 + m.x274 + m.x278 == 0)

m.c170 = Constraint(expr= - m.x259 + m.x275 + m.x279 == 0)

m.c171 = Constraint(expr= - m.x260 + m.x276 + m.x280 == 0)

m.c172 = Constraint(expr= - m.x261 + m.x281 + m.x285 == 0)

m.c173 = Constraint(expr= - m.x262 + m.x282 + m.x286 == 0)

m.c174 = Constraint(expr= - m.x263 + m.x283 + m.x287 == 0)

m.c175 = Constraint(expr= - m.x264 + m.x284 + m.x288 == 0)

m.c176 = Constraint(expr= - m.x265 + m.x289 + m.x293 == 0)

m.c177 = Constraint(expr= - m.x266 + m.x290 + m.x294 == 0)

m.c178 = Constraint(expr= - m.x267 + m.x291 + m.x295 == 0)

m.c179 = Constraint(expr= - m.x268 + m.x292 + m.x296 == 0)

m.c180 = Constraint(expr= - m.x269 + m.x297 + m.x301 == 0)

m.c181 = Constraint(expr= - m.x270 + m.x298 + m.x302 == 0)

m.c182 = Constraint(expr= - m.x271 + m.x299 + m.x303 == 0)

m.c183 = Constraint(expr= - m.x272 + m.x300 + m.x304 == 0)

m.c184 = Constraint(expr=   0.2*m.x257 - m.x273 <= 0)

m.c185 = Constraint(expr=   0.2*m.x258 - m.x274 <= 0)

m.c186 = Constraint(expr=   0.2*m.x259 - m.x275 <= 0)

m.c187 = Constraint(expr=   0.2*m.x260 - m.x276 <= 0)

m.c188 = Constraint(expr=   0.2*m.x257 - m.x277 <= 0)

m.c189 = Constraint(expr=   0.2*m.x258 - m.x278 <= 0)

m.c190 = Constraint(expr=   0.2*m.x259 - m.x279 <= 0)

m.c191 = Constraint(expr=   0.2*m.x260 - m.x280 <= 0)

m.c192 = Constraint(expr=   0.2*m.x261 - m.x281 <= 0)

m.c193 = Constraint(expr=   0.2*m.x262 - m.x282 <= 0)

m.c194 = Constraint(expr=   0.2*m.x263 - m.x283 <= 0)

m.c195 = Constraint(expr=   0.2*m.x264 - m.x284 <= 0)

m.c196 = Constraint(expr=   0.2*m.x261 - m.x285 <= 0)

m.c197 = Constraint(expr=   0.2*m.x262 - m.x286 <= 0)

m.c198 = Constraint(expr=   0.2*m.x263 - m.x287 <= 0)

m.c199 = Constraint(expr=   0.2*m.x264 - m.x288 <= 0)

m.c200 = Constraint(expr=   0.2*m.x269 - m.x297 <= 0)

m.c201 = Constraint(expr=   0.2*m.x270 - m.x298 <= 0)

m.c202 = Constraint(expr=   0.2*m.x271 - m.x299 <= 0)

m.c203 = Constraint(expr=   0.2*m.x272 - m.x300 <= 0)

m.c204 = Constraint(expr=   0.2*m.x269 - m.x301 <= 0)

m.c205 = Constraint(expr=   0.2*m.x270 - m.x302 <= 0)

m.c206 = Constraint(expr=   0.2*m.x271 - m.x303 <= 0)

m.c207 = Constraint(expr=   0.2*m.x272 - m.x304 <= 0)

m.c208 = Constraint(expr= - 0.8*m.x257 + m.x273 <= 0)

m.c209 = Constraint(expr= - 0.8*m.x258 + m.x274 <= 0)

m.c210 = Constraint(expr= - 0.8*m.x259 + m.x275 <= 0)

m.c211 = Constraint(expr= - 0.8*m.x260 + m.x276 <= 0)

m.c212 = Constraint(expr= - 0.8*m.x257 + m.x277 <= 0)

m.c213 = Constraint(expr= - 0.8*m.x258 + m.x278 <= 0)

m.c214 = Constraint(expr= - 0.8*m.x259 + m.x279 <= 0)

m.c215 = Constraint(expr= - 0.8*m.x260 + m.x280 <= 0)

m.c216 = Constraint(expr= - 0.8*m.x261 + m.x281 <= 0)

m.c217 = Constraint(expr= - 0.8*m.x262 + m.x282 <= 0)

m.c218 = Constraint(expr= - 0.8*m.x263 + m.x283 <= 0)

m.c219 = Constraint(expr= - 0.8*m.x264 + m.x284 <= 0)

m.c220 = Constraint(expr= - 0.8*m.x261 + m.x285 <= 0)

m.c221 = Constraint(expr= - 0.8*m.x262 + m.x286 <= 0)

m.c222 = Constraint(expr= - 0.8*m.x263 + m.x287 <= 0)

m.c223 = Constraint(expr= - 0.8*m.x264 + m.x288 <= 0)

m.c224 = Constraint(expr= - 0.8*m.x269 + m.x297 <= 0)

m.c225 = Constraint(expr= - 0.8*m.x270 + m.x298 <= 0)

m.c226 = Constraint(expr= - 0.8*m.x271 + m.x299 <= 0)

m.c227 = Constraint(expr= - 0.8*m.x272 + m.x300 <= 0)

m.c228 = Constraint(expr= - 0.8*m.x269 + m.x301 <= 0)

m.c229 = Constraint(expr= - 0.8*m.x270 + m.x302 <= 0)

m.c230 = Constraint(expr= - 0.8*m.x271 + m.x303 <= 0)

m.c231 = Constraint(expr= - 0.8*m.x272 + m.x304 <= 0)

m.c232 = Constraint(expr= - 0.666666666666667*m.x49 + m.x65 == 0)

m.c233 = Constraint(expr= - 0.333333333333333*m.x49 + m.x69 == 0)

m.c234 = Constraint(expr= - 0.333333333333333*m.x53 + m.x73 == 0)

m.c235 = Constraint(expr= - 0.666666666666667*m.x53 + m.x77 == 0)

m.c236 = Constraint(expr= - 0.2*m.x57 + m.x81 == 0)

m.c237 = Constraint(expr= - 0.8*m.x57 + m.x85 == 0)

m.c238 = Constraint(expr= - 0.433333333333333*m.x61 + m.x89 == 0)

m.c239 = Constraint(expr= - 0.566666666666667*m.x61 + m.x93 == 0)

m.c240 = Constraint(expr=   m.b1 + m.b33 <= 1)

m.c241 = Constraint(expr=   m.b2 + m.b34 <= 1)

m.c242 = Constraint(expr=   m.b3 + m.b35 <= 1)

m.c243 = Constraint(expr=   m.b4 + m.b36 <= 1)

m.c244 = Constraint(expr=   m.b5 + m.b45 <= 1)

m.c245 = Constraint(expr=   m.b6 + m.b46 <= 1)

m.c246 = Constraint(expr=   m.b7 + m.b47 <= 1)

m.c247 = Constraint(expr=   m.b8 + m.b48 <= 1)

m.c248 = Constraint(expr=   m.b9 + m.b33 <= 1)

m.c249 = Constraint(expr=   m.b10 + m.b34 <= 1)

m.c250 = Constraint(expr=   m.b11 + m.b35 <= 1)

m.c251 = Constraint(expr=   m.b12 + m.b36 <= 1)

m.c252 = Constraint(expr=   m.b13 + m.b45 <= 1)

m.c253 = Constraint(expr=   m.b14 + m.b46 <= 1)

m.c254 = Constraint(expr=   m.b15 + m.b47 <= 1)

m.c255 = Constraint(expr=   m.b16 + m.b48 <= 1)

m.c256 = Constraint(expr=   m.b17 + m.b37 <= 1)

m.c257 = Constraint(expr=   m.b18 + m.b38 <= 1)

m.c258 = Constraint(expr=   m.b19 + m.b39 <= 1)

m.c259 = Constraint(expr=   m.b20 + m.b40 <= 1)

m.c260 = Constraint(expr=   m.b21 + m.b41 <= 1)

m.c261 = Constraint(expr=   m.b22 + m.b42 <= 1)

m.c262 = Constraint(expr=   m.b23 + m.b43 <= 1)

m.c263 = Constraint(expr=   m.b24 + m.b44 <= 1)

m.c264 = Constraint(expr=   m.b25 + m.b37 <= 1)

m.c265 = Constraint(expr=   m.b26 + m.b38 <= 1)

m.c266 = Constraint(expr=   m.b27 + m.b39 <= 1)

m.c267 = Constraint(expr=   m.b28 + m.b40 <= 1)

m.c268 = Constraint(expr=   m.b29 + m.b41 <= 1)

m.c269 = Constraint(expr=   m.b30 + m.b42 <= 1)

m.c270 = Constraint(expr=   m.b31 + m.b43 <= 1)

m.c271 = Constraint(expr=   m.b32 + m.b44 <= 1)

m.c272 = Constraint(expr=   m.b33 <= 2)

m.c273 = Constraint(expr=   m.b34 <= 2)

m.c274 = Constraint(expr=   m.b35 <= 2)

m.c275 = Constraint(expr=   m.b36 <= 2)

m.c276 = Constraint(expr=   m.b37 <= 2)

m.c277 = Constraint(expr=   m.b38 <= 2)

m.c278 = Constraint(expr=   m.b39 <= 2)

m.c279 = Constraint(expr=   m.b40 <= 2)

m.c280 = Constraint(expr=   m.b41 <= 2)

m.c281 = Constraint(expr=   m.b42 <= 2)

m.c282 = Constraint(expr=   m.b43 <= 2)

m.c283 = Constraint(expr=   m.b44 <= 2)

m.c284 = Constraint(expr=   m.b45 <= 2)

m.c285 = Constraint(expr=   m.b46 <= 2)

m.c286 = Constraint(expr=   m.b47 <= 2)

m.c287 = Constraint(expr=   m.b48 <= 2)

m.c288 = Constraint(expr=   m.b33 + m.b45 <= 2)

m.c289 = Constraint(expr=   m.b34 + m.b46 <= 2)

m.c290 = Constraint(expr=   m.b35 + m.b47 <= 2)

m.c291 = Constraint(expr=   m.b36 + m.b48 <= 2)

m.c292 = Constraint(expr=   m.b37 + m.b41 <= 2)

m.c293 = Constraint(expr=   m.b38 + m.b42 <= 2)

m.c294 = Constraint(expr=   m.b39 + m.b43 <= 2)

m.c295 = Constraint(expr=   m.b40 + m.b44 <= 2)

m.c296 = Constraint(expr=   m.x49 + 12.5*m.x209 - 12.5*m.x225 <= 0)

m.c297 = Constraint(expr=   m.x50 + 12.5*m.x210 - 12.5*m.x226 <= 0)

m.c298 = Constraint(expr=   m.x51 + 12.5*m.x211 - 12.5*m.x227 <= 0)

m.c299 = Constraint(expr=   m.x52 + 12.5*m.x212 - 12.5*m.x228 <= 0)

m.c300 = Constraint(expr=   m.x53 + 12.5*m.x213 - 12.5*m.x229 <= 0)

m.c301 = Constraint(expr=   m.x54 + 12.5*m.x214 - 12.5*m.x230 <= 0)

m.c302 = Constraint(expr=   m.x55 + 12.5*m.x215 - 12.5*m.x231 <= 0)

m.c303 = Constraint(expr=   m.x56 + 12.5*m.x216 - 12.5*m.x232 <= 0)

m.c304 = Constraint(expr=   m.x57 + 12.5*m.x217 - 12.5*m.x233 <= 0)

m.c305 = Constraint(expr=   m.x58 + 12.5*m.x218 - 12.5*m.x234 <= 0)

m.c306 = Constraint(expr=   m.x59 + 12.5*m.x219 - 12.5*m.x235 <= 0)

m.c307 = Constraint(expr=   m.x60 + 12.5*m.x220 - 12.5*m.x236 <= 0)

m.c308 = Constraint(expr=   m.x61 + 12.5*m.x221 - 12.5*m.x237 <= 0)

m.c309 = Constraint(expr=   m.x62 + 12.5*m.x222 - 12.5*m.x238 <= 0)

m.c310 = Constraint(expr=   m.x63 + 12.5*m.x223 - 12.5*m.x239 <= 0)

m.c311 = Constraint(expr=   m.x64 + 12.5*m.x224 - 12.5*m.x240 <= 0)

m.c312 = Constraint(expr= - 250*m.b33 + m.x49 <= 0)

m.c313 = Constraint(expr= - 560*m.b34 + m.x50 <= 0)

m.c314 = Constraint(expr= - 650*m.b35 + m.x51 <= 0)

m.c315 = Constraint(expr= - 650*m.b36 + m.x52 <= 0)

m.c316 = Constraint(expr= - 250*m.b37 + m.x53 <= 0)

m.c317 = Constraint(expr= - 650*m.b38 + m.x54 <= 0)

m.c318 = Constraint(expr= - 650*m.b39 + m.x55 <= 0)

m.c319 = Constraint(expr= - 650*m.b40 + m.x56 <= 0)

m.c320 = Constraint(expr= - 200*m.b41 + m.x57 <= 0)

m.c321 = Constraint(expr= - 840*m.b42 + m.x58 <= 0)

m.c322 = Constraint(expr= - 850*m.b43 + m.x59 <= 0)

m.c323 = Constraint(expr= - 850*m.b44 + m.x60 <= 0)

m.c324 = Constraint(expr= - 250*m.b45 + m.x61 <= 0)

m.c325 = Constraint(expr= - 560*m.b46 + m.x62 <= 0)

m.c326 = Constraint(expr= - 650*m.b47 + m.x63 <= 0)

m.c327 = Constraint(expr= - 650*m.b48 + m.x64 <= 0)

m.c328 = Constraint(expr=   m.x49 - m.x65 - m.x69 == 0)

m.c329 = Constraint(expr=   m.x50 - m.x66 - m.x70 == 0)

m.c330 = Constraint(expr=   m.x51 - m.x67 - m.x71 == 0)

m.c331 = Constraint(expr=   m.x52 - m.x68 - m.x72 == 0)

m.c332 = Constraint(expr=   m.x53 - m.x73 - m.x77 == 0)

m.c333 = Constraint(expr=   m.x54 - m.x74 - m.x78 == 0)

m.c334 = Constraint(expr=   m.x55 - m.x75 - m.x79 == 0)

m.c335 = Constraint(expr=   m.x56 - m.x76 - m.x80 == 0)

m.c336 = Constraint(expr=   m.x57 - m.x81 - m.x85 == 0)

m.c337 = Constraint(expr=   m.x58 - m.x82 - m.x86 == 0)

m.c338 = Constraint(expr=   m.x59 - m.x83 - m.x87 == 0)

m.c339 = Constraint(expr=   m.x60 - m.x84 - m.x88 == 0)

m.c340 = Constraint(expr=   m.x61 - m.x89 - m.x93 == 0)

m.c341 = Constraint(expr=   m.x62 - m.x90 - m.x94 == 0)

m.c342 = Constraint(expr=   m.x63 - m.x91 - m.x95 == 0)

m.c343 = Constraint(expr=   m.x64 - m.x92 - m.x96 == 0)

m.c344 = Constraint(expr= - m.x49 - m.x61 + m.x97 == 0)

m.c345 = Constraint(expr= - m.x50 - m.x62 + m.x98 == 0)

m.c346 = Constraint(expr= - m.x51 - m.x63 + m.x99 == 0)

m.c347 = Constraint(expr= - m.x52 - m.x64 + m.x100 == 0)

m.c348 = Constraint(expr= - m.x53 - m.x57 + m.x101 == 0)

m.c349 = Constraint(expr= - m.x54 - m.x58 + m.x102 == 0)

m.c350 = Constraint(expr= - m.x55 - m.x59 + m.x103 == 0)

m.c351 = Constraint(expr= - m.x56 - m.x60 + m.x104 == 0)

m.c352 = Constraint(expr= - m.x97 - 6.25*m.x241 + 6.25*m.x249 <= 0)

m.c353 = Constraint(expr= - m.x98 - 6.25*m.x242 + 6.25*m.x250 <= 0)

m.c354 = Constraint(expr= - m.x99 - 6.25*m.x243 + 6.25*m.x251 <= 0)

m.c355 = Constraint(expr= - m.x100 - 6.25*m.x244 + 6.25*m.x252 <= 0)

m.c356 = Constraint(expr= - m.x101 - 6.25*m.x245 + 6.25*m.x253 <= 0)

m.c357 = Constraint(expr= - m.x102 - 6.25*m.x246 + 6.25*m.x254 <= 0)

m.c358 = Constraint(expr= - m.x103 - 6.25*m.x247 + 6.25*m.x255 <= 0)

m.c359 = Constraint(expr= - m.x104 - 6.25*m.x248 + 6.25*m.x256 <= 0)

m.c360 = Constraint(expr=   m.x97 + 12.5*m.x241 - 12.5*m.x249 <= 0)

m.c361 = Constraint(expr=   m.x98 + 12.5*m.x242 - 12.5*m.x250 <= 0)

m.c362 = Constraint(expr=   m.x99 + 12.5*m.x243 - 12.5*m.x251 <= 0)

m.c363 = Constraint(expr=   m.x100 + 12.5*m.x244 - 12.5*m.x252 <= 0)

m.c364 = Constraint(expr=   m.x101 + 12.5*m.x245 - 12.5*m.x253 <= 0)

m.c365 = Constraint(expr=   m.x102 + 12.5*m.x246 - 12.5*m.x254 <= 0)

m.c366 = Constraint(expr=   m.x103 + 12.5*m.x247 - 12.5*m.x255 <= 0)

m.c367 = Constraint(expr=   m.x104 + 12.5*m.x248 - 12.5*m.x256 <= 0)

m.c368 = Constraint(expr= - m.x65 - m.x89 + 0.3*m.x97 <= 0)

m.c369 = Constraint(expr= - m.x66 - m.x90 + 0.3*m.x98 <= 0)

m.c370 = Constraint(expr= - m.x67 - m.x91 + 0.3*m.x99 <= 0)

m.c371 = Constraint(expr= - m.x68 - m.x92 + 0.3*m.x100 <= 0)

m.c372 = Constraint(expr= - m.x69 - m.x93 + 0.3*m.x97 <= 0)

m.c373 = Constraint(expr= - m.x70 - m.x94 + 0.3*m.x98 <= 0)

m.c374 = Constraint(expr= - m.x71 - m.x95 + 0.3*m.x99 <= 0)

m.c375 = Constraint(expr= - m.x72 - m.x96 + 0.3*m.x100 <= 0)

m.c376 = Constraint(expr=   m.x65 + m.x89 - 0.7*m.x97 <= 0)

m.c377 = Constraint(expr=   m.x66 + m.x90 - 0.7*m.x98 <= 0)

m.c378 = Constraint(expr=   m.x67 + m.x91 - 0.7*m.x99 <= 0)

m.c379 = Constraint(expr=   m.x68 + m.x92 - 0.7*m.x100 <= 0)

m.c380 = Constraint(expr=   m.x69 + m.x93 - 0.7*m.x97 <= 0)

m.c381 = Constraint(expr=   m.x70 + m.x94 - 0.7*m.x98 <= 0)

m.c382 = Constraint(expr=   m.x71 + m.x95 - 0.7*m.x99 <= 0)

m.c383 = Constraint(expr=   m.x72 + m.x96 - 0.7*m.x100 <= 0)

m.c384 = Constraint(expr=   0.0045*m.x49 + 0.0045*m.x61 - 0.005*m.x65 - 0.006*m.x69 - 0.005*m.x89 - 0.006*m.x93 <= 0)

m.c385 = Constraint(expr=   0.0045*m.x50 + 0.0045*m.x62 - 0.005*m.x66 - 0.006*m.x70 - 0.005*m.x90 - 0.006*m.x94 <= 0)

m.c386 = Constraint(expr=   0.0045*m.x51 + 0.0045*m.x63 - 0.005*m.x67 - 0.006*m.x71 - 0.005*m.x91 - 0.006*m.x95 <= 0)

m.c387 = Constraint(expr=   0.0045*m.x52 + 0.0045*m.x64 - 0.005*m.x68 - 0.006*m.x72 - 0.005*m.x92 - 0.006*m.x96 <= 0)

m.c388 = Constraint(expr=   0.014*m.x53 + 0.014*m.x57 - 0.0165*m.x73 - 0.0145*m.x77 - 0.0165*m.x81 - 0.0145*m.x85 <= 0)

m.c389 = Constraint(expr=   0.014*m.x54 + 0.014*m.x58 - 0.0165*m.x74 - 0.0145*m.x78 - 0.0165*m.x82 - 0.0145*m.x86 <= 0)

m.c390 = Constraint(expr=   0.014*m.x55 + 0.014*m.x59 - 0.0165*m.x75 - 0.0145*m.x79 - 0.0165*m.x83 - 0.0145*m.x87 <= 0)

m.c391 = Constraint(expr=   0.014*m.x56 + 0.014*m.x60 - 0.0165*m.x76 - 0.0145*m.x80 - 0.0165*m.x84 - 0.0145*m.x88 <= 0)

m.c392 = Constraint(expr= - 0.006*m.x49 - 0.006*m.x61 + 0.005*m.x65 + 0.006*m.x69 + 0.005*m.x89 + 0.006*m.x93 <= 0)

m.c393 = Constraint(expr= - 0.006*m.x50 - 0.006*m.x62 + 0.005*m.x66 + 0.006*m.x70 + 0.005*m.x90 + 0.006*m.x94 <= 0)

m.c394 = Constraint(expr= - 0.006*m.x51 - 0.006*m.x63 + 0.005*m.x67 + 0.006*m.x71 + 0.005*m.x91 + 0.006*m.x95 <= 0)

m.c395 = Constraint(expr= - 0.006*m.x52 - 0.006*m.x64 + 0.005*m.x68 + 0.006*m.x72 + 0.005*m.x92 + 0.006*m.x96 <= 0)

m.c396 = Constraint(expr= - 0.0153*m.x53 - 0.0153*m.x57 + 0.0165*m.x73 + 0.0145*m.x77 + 0.0165*m.x81 + 0.0145*m.x85
                          <= 0)

m.c397 = Constraint(expr= - 0.0153*m.x54 - 0.0153*m.x58 + 0.0165*m.x74 + 0.0145*m.x78 + 0.0165*m.x82 + 0.0145*m.x86
                          <= 0)

m.c398 = Constraint(expr= - 0.0153*m.x55 - 0.0153*m.x59 + 0.0165*m.x75 + 0.0145*m.x79 + 0.0165*m.x83 + 0.0145*m.x87
                          <= 0)

m.c399 = Constraint(expr= - 0.0153*m.x56 - 0.0153*m.x60 + 0.0165*m.x76 + 0.0145*m.x80 + 0.0165*m.x84 + 0.0145*m.x88
                          <= 0)

m.c400 = Constraint(expr=   m.x97 + m.x98 + m.x99 + m.x100 == 550)

m.c401 = Constraint(expr=   m.x101 + m.x102 + m.x103 + m.x104 == 550)

m.c402 = Constraint(expr=   m.x146 - m.x177 >= 0)

m.c403 = Constraint(expr=   m.x147 - m.x178 >= 0)

m.c404 = Constraint(expr=   m.x148 - m.x179 >= 0)

m.c405 = Constraint(expr=   m.x150 - m.x181 >= 0)

m.c406 = Constraint(expr=   m.x151 - m.x182 >= 0)

m.c407 = Constraint(expr=   m.x152 - m.x183 >= 0)

m.c408 = Constraint(expr=   m.x154 - m.x185 >= 0)

m.c409 = Constraint(expr=   m.x155 - m.x186 >= 0)

m.c410 = Constraint(expr=   m.x156 - m.x187 >= 0)

m.c411 = Constraint(expr=   m.x158 - m.x189 >= 0)

m.c412 = Constraint(expr=   m.x159 - m.x190 >= 0)

m.c413 = Constraint(expr=   m.x160 - m.x191 >= 0)

m.c414 = Constraint(expr=   m.x162 - m.x193 >= 0)

m.c415 = Constraint(expr=   m.x163 - m.x194 >= 0)

m.c416 = Constraint(expr=   m.x164 - m.x195 >= 0)

m.c417 = Constraint(expr=   m.x166 - m.x197 >= 0)

m.c418 = Constraint(expr=   m.x167 - m.x198 >= 0)

m.c419 = Constraint(expr=   m.x168 - m.x199 >= 0)

m.c420 = Constraint(expr=   m.x170 - m.x201 >= 0)

m.c421 = Constraint(expr=   m.x171 - m.x202 >= 0)

m.c422 = Constraint(expr=   m.x172 - m.x203 >= 0)

m.c423 = Constraint(expr=   m.x174 - m.x205 >= 0)

m.c424 = Constraint(expr=   m.x175 - m.x206 >= 0)

m.c425 = Constraint(expr=   m.x176 - m.x207 >= 0)

m.c426 = Constraint(expr= - 72*m.b1 + m.x154 - m.x177 >= -72)

m.c427 = Constraint(expr= - 72*m.b2 + m.x155 - m.x178 >= -72)

m.c428 = Constraint(expr= - 72*m.b3 + m.x156 - m.x179 >= -72)

m.c429 = Constraint(expr= - 72*m.b5 + m.x158 - m.x181 >= -72)

m.c430 = Constraint(expr= - 72*m.b6 + m.x159 - m.x182 >= -72)

m.c431 = Constraint(expr= - 72*m.b7 + m.x160 - m.x183 >= -72)

m.c432 = Constraint(expr= - 72*m.b9 + m.x146 - m.x185 >= -72)

m.c433 = Constraint(expr= - 72*m.b10 + m.x147 - m.x186 >= -72)

m.c434 = Constraint(expr= - 72*m.b11 + m.x148 - m.x187 >= -72)

m.c435 = Constraint(expr= - 72*m.b13 + m.x150 - m.x189 >= -72)

m.c436 = Constraint(expr= - 72*m.b14 + m.x151 - m.x190 >= -72)

m.c437 = Constraint(expr= - 72*m.b15 + m.x152 - m.x191 >= -72)

m.c438 = Constraint(expr= - 72*m.b17 + m.x170 - m.x193 >= -72)

m.c439 = Constraint(expr= - 72*m.b18 + m.x171 - m.x194 >= -72)

m.c440 = Constraint(expr= - 72*m.b19 + m.x172 - m.x195 >= -72)

m.c441 = Constraint(expr= - 72*m.b21 + m.x174 - m.x197 >= -72)

m.c442 = Constraint(expr= - 72*m.b22 + m.x175 - m.x198 >= -72)

m.c443 = Constraint(expr= - 72*m.b23 + m.x176 - m.x199 >= -72)

m.c444 = Constraint(expr= - 72*m.b25 + m.x162 - m.x201 >= -72)

m.c445 = Constraint(expr= - 72*m.b26 + m.x163 - m.x202 >= -72)

m.c446 = Constraint(expr= - 72*m.b27 + m.x164 - m.x203 >= -72)

m.c447 = Constraint(expr= - 72*m.b29 + m.x166 - m.x205 >= -72)

m.c448 = Constraint(expr= - 72*m.b30 + m.x167 - m.x206 >= -72)

m.c449 = Constraint(expr= - 72*m.b31 + m.x168 - m.x207 >= -72)

m.c450 = Constraint(expr=   m.x210 - m.x225 >= 0)

m.c451 = Constraint(expr=   m.x211 - m.x226 >= 0)

m.c452 = Constraint(expr=   m.x212 - m.x227 >= 0)

m.c453 = Constraint(expr=   m.x214 - m.x229 >= 0)

m.c454 = Constraint(expr=   m.x215 - m.x230 >= 0)

m.c455 = Constraint(expr=   m.x216 - m.x231 >= 0)

m.c456 = Constraint(expr=   m.x218 - m.x233 >= 0)

m.c457 = Constraint(expr=   m.x219 - m.x234 >= 0)

m.c458 = Constraint(expr=   m.x220 - m.x235 >= 0)

m.c459 = Constraint(expr=   m.x222 - m.x237 >= 0)

m.c460 = Constraint(expr=   m.x223 - m.x238 >= 0)

m.c461 = Constraint(expr=   m.x224 - m.x239 >= 0)

m.c462 = Constraint(expr= - 72*m.b33 + m.x146 - m.x225 >= -72)

m.c463 = Constraint(expr= - 72*m.b34 + m.x147 - m.x226 >= -72)

m.c464 = Constraint(expr= - 72*m.b35 + m.x148 - m.x227 >= -72)

m.c465 = Constraint(expr= - 72*m.b45 + m.x150 - m.x237 >= -72)

m.c466 = Constraint(expr= - 72*m.b46 + m.x151 - m.x238 >= -72)

m.c467 = Constraint(expr= - 72*m.b47 + m.x152 - m.x239 >= -72)

m.c468 = Constraint(expr= - 72*m.b33 + m.x154 - m.x225 >= -72)

m.c469 = Constraint(expr= - 72*m.b34 + m.x155 - m.x226 >= -72)

m.c470 = Constraint(expr= - 72*m.b35 + m.x156 - m.x227 >= -72)

m.c471 = Constraint(expr= - 72*m.b45 + m.x158 - m.x237 >= -72)

m.c472 = Constraint(expr= - 72*m.b46 + m.x159 - m.x238 >= -72)

m.c473 = Constraint(expr= - 72*m.b47 + m.x160 - m.x239 >= -72)

m.c474 = Constraint(expr= - 72*m.b37 + m.x162 - m.x229 >= -72)

m.c475 = Constraint(expr= - 72*m.b38 + m.x163 - m.x230 >= -72)

m.c476 = Constraint(expr= - 72*m.b39 + m.x164 - m.x231 >= -72)

m.c477 = Constraint(expr= - 72*m.b41 + m.x166 - m.x233 >= -72)

m.c478 = Constraint(expr= - 72*m.b42 + m.x167 - m.x234 >= -72)

m.c479 = Constraint(expr= - 72*m.b43 + m.x168 - m.x235 >= -72)

m.c480 = Constraint(expr= - 72*m.b37 + m.x170 - m.x229 >= -72)

m.c481 = Constraint(expr= - 72*m.b38 + m.x171 - m.x230 >= -72)

m.c482 = Constraint(expr= - 72*m.b39 + m.x172 - m.x231 >= -72)

m.c483 = Constraint(expr= - 72*m.b41 + m.x174 - m.x233 >= -72)

m.c484 = Constraint(expr= - 72*m.b42 + m.x175 - m.x234 >= -72)

m.c485 = Constraint(expr= - 72*m.b43 + m.x176 - m.x235 >= -72)

m.c486 = Constraint(expr= - 80*m.b1 - m.x177 + m.x210 >= -72)

m.c487 = Constraint(expr= - 80*m.b2 - m.x178 + m.x211 >= -72)

m.c488 = Constraint(expr= - 80*m.b3 - m.x179 + m.x212 >= -72)

m.c489 = Constraint(expr= - 80*m.b5 - m.x181 + m.x222 >= -72)

m.c490 = Constraint(expr= - 80*m.b6 - m.x182 + m.x223 >= -72)

m.c491 = Constraint(expr= - 80*m.b7 - m.x183 + m.x224 >= -72)

m.c492 = Constraint(expr= - 80*m.b9 - m.x185 + m.x210 >= -72)

m.c493 = Constraint(expr= - 80*m.b10 - m.x186 + m.x211 >= -72)

m.c494 = Constraint(expr= - 80*m.b11 - m.x187 + m.x212 >= -72)

m.c495 = Constraint(expr= - 80*m.b13 - m.x189 + m.x222 >= -72)

m.c496 = Constraint(expr= - 80*m.b14 - m.x190 + m.x223 >= -72)

m.c497 = Constraint(expr= - 80*m.b15 - m.x191 + m.x224 >= -72)

m.c498 = Constraint(expr= - 80*m.b17 - m.x193 + m.x214 >= -72)

m.c499 = Constraint(expr= - 80*m.b18 - m.x194 + m.x215 >= -72)

m.c500 = Constraint(expr= - 80*m.b19 - m.x195 + m.x216 >= -72)

m.c501 = Constraint(expr= - 80*m.b21 - m.x197 + m.x218 >= -72)

m.c502 = Constraint(expr= - 80*m.b22 - m.x198 + m.x219 >= -72)

m.c503 = Constraint(expr= - 80*m.b23 - m.x199 + m.x220 >= -72)

m.c504 = Constraint(expr= - 80*m.b25 - m.x201 + m.x214 >= -72)

m.c505 = Constraint(expr= - 80*m.b26 - m.x202 + m.x215 >= -72)

m.c506 = Constraint(expr= - 80*m.b27 - m.x203 + m.x216 >= -72)

m.c507 = Constraint(expr= - 80*m.b29 - m.x205 + m.x218 >= -72)

m.c508 = Constraint(expr= - 80*m.b30 - m.x206 + m.x219 >= -72)

m.c509 = Constraint(expr= - 80*m.b31 - m.x207 + m.x220 >= -72)

m.c510 = Constraint(expr=   m.x242 - m.x249 >= 0)

m.c511 = Constraint(expr=   m.x243 - m.x250 >= 0)

m.c512 = Constraint(expr=   m.x244 - m.x251 >= 0)

m.c513 = Constraint(expr=   m.x246 - m.x253 >= 0)

m.c514 = Constraint(expr=   m.x247 - m.x254 >= 0)

m.c515 = Constraint(expr=   m.x248 - m.x255 >= 0)

m.c516 = Constraint(expr= - 72*m.b33 - m.x209 + m.x241 >= -72)

m.c517 = Constraint(expr= - 72*m.b34 - m.x210 + m.x242 >= -72)

m.c518 = Constraint(expr= - 72*m.b35 - m.x211 + m.x243 >= -72)

m.c519 = Constraint(expr= - 72*m.b36 - m.x212 + m.x244 >= -72)

m.c520 = Constraint(expr= - 72*m.b37 - m.x213 + m.x245 >= -72)

m.c521 = Constraint(expr= - 72*m.b38 - m.x214 + m.x246 >= -72)

m.c522 = Constraint(expr= - 72*m.b39 - m.x215 + m.x247 >= -72)

m.c523 = Constraint(expr= - 72*m.b40 - m.x216 + m.x248 >= -72)

m.c524 = Constraint(expr= - 72*m.b41 - m.x217 + m.x245 >= -72)

m.c525 = Constraint(expr= - 72*m.b42 - m.x218 + m.x246 >= -72)

m.c526 = Constraint(expr= - 72*m.b43 - m.x219 + m.x247 >= -72)

m.c527 = Constraint(expr= - 72*m.b44 - m.x220 + m.x248 >= -72)

m.c528 = Constraint(expr= - 72*m.b45 - m.x221 + m.x241 >= -72)

m.c529 = Constraint(expr= - 72*m.b46 - m.x222 + m.x242 >= -72)

m.c530 = Constraint(expr= - 72*m.b47 - m.x223 + m.x243 >= -72)

m.c531 = Constraint(expr= - 72*m.b48 - m.x224 + m.x244 >= -72)

m.c532 = Constraint(expr=   72*m.b33 - m.x209 + m.x241 <= 72)

m.c533 = Constraint(expr=   72*m.b34 - m.x210 + m.x242 <= 72)

m.c534 = Constraint(expr=   72*m.b35 - m.x211 + m.x243 <= 72)

m.c535 = Constraint(expr=   72*m.b36 - m.x212 + m.x244 <= 72)

m.c536 = Constraint(expr=   72*m.b37 - m.x213 + m.x245 <= 72)

m.c537 = Constraint(expr=   72*m.b38 - m.x214 + m.x246 <= 72)

m.c538 = Constraint(expr=   72*m.b39 - m.x215 + m.x247 <= 72)

m.c539 = Constraint(expr=   72*m.b40 - m.x216 + m.x248 <= 72)

m.c540 = Constraint(expr=   72*m.b41 - m.x217 + m.x245 <= 72)

m.c541 = Constraint(expr=   72*m.b42 - m.x218 + m.x246 <= 72)

m.c542 = Constraint(expr=   72*m.b43 - m.x219 + m.x247 <= 72)

m.c543 = Constraint(expr=   72*m.b44 - m.x220 + m.x248 <= 72)

m.c544 = Constraint(expr=   72*m.b45 - m.x221 + m.x241 <= 72)

m.c545 = Constraint(expr=   72*m.b46 - m.x222 + m.x242 <= 72)

m.c546 = Constraint(expr=   72*m.b47 - m.x223 + m.x243 <= 72)

m.c547 = Constraint(expr=   72*m.b48 - m.x224 + m.x244 <= 72)

m.c548 = Constraint(expr= - 72*m.b33 - m.x225 + m.x249 >= -72)

m.c549 = Constraint(expr= - 72*m.b34 - m.x226 + m.x250 >= -72)

m.c550 = Constraint(expr= - 72*m.b35 - m.x227 + m.x251 >= -72)

m.c551 = Constraint(expr= - 72*m.b36 - m.x228 + m.x252 >= -72)

m.c552 = Constraint(expr= - 72*m.b37 - m.x229 + m.x253 >= -72)

m.c553 = Constraint(expr= - 72*m.b38 - m.x230 + m.x254 >= -72)

m.c554 = Constraint(expr= - 72*m.b39 - m.x231 + m.x255 >= -72)

m.c555 = Constraint(expr= - 72*m.b40 - m.x232 + m.x256 >= -72)

m.c556 = Constraint(expr= - 72*m.b41 - m.x233 + m.x253 >= -72)

m.c557 = Constraint(expr= - 72*m.b42 - m.x234 + m.x254 >= -72)

m.c558 = Constraint(expr= - 72*m.b43 - m.x235 + m.x255 >= -72)

m.c559 = Constraint(expr= - 72*m.b44 - m.x236 + m.x256 >= -72)

m.c560 = Constraint(expr= - 72*m.b45 - m.x237 + m.x249 >= -72)

m.c561 = Constraint(expr= - 72*m.b46 - m.x238 + m.x250 >= -72)

m.c562 = Constraint(expr= - 72*m.b47 - m.x239 + m.x251 >= -72)

m.c563 = Constraint(expr= - 72*m.b48 - m.x240 + m.x252 >= -72)

m.c564 = Constraint(expr=   72*m.b33 - m.x225 + m.x249 <= 72)

m.c565 = Constraint(expr=   72*m.b34 - m.x226 + m.x250 <= 72)

m.c566 = Constraint(expr=   72*m.b35 - m.x227 + m.x251 <= 72)

m.c567 = Constraint(expr=   72*m.b36 - m.x228 + m.x252 <= 72)

m.c568 = Constraint(expr=   72*m.b37 - m.x229 + m.x253 <= 72)

m.c569 = Constraint(expr=   72*m.b38 - m.x230 + m.x254 <= 72)

m.c570 = Constraint(expr=   72*m.b39 - m.x231 + m.x255 <= 72)

m.c571 = Constraint(expr=   72*m.b40 - m.x232 + m.x256 <= 72)

m.c572 = Constraint(expr=   72*m.b41 - m.x233 + m.x253 <= 72)

m.c573 = Constraint(expr=   72*m.b42 - m.x234 + m.x254 <= 72)

m.c574 = Constraint(expr=   72*m.b43 - m.x235 + m.x255 <= 72)

m.c575 = Constraint(expr=   72*m.b44 - m.x236 + m.x256 <= 72)

m.c576 = Constraint(expr=   72*m.b45 - m.x237 + m.x249 <= 72)

m.c577 = Constraint(expr=   72*m.b46 - m.x238 + m.x250 <= 72)

m.c578 = Constraint(expr=   72*m.b47 - m.x239 + m.x251 <= 72)

m.c579 = Constraint(expr=   72*m.b48 - m.x240 + m.x252 <= 72)

m.c580 = Constraint(expr=   m.x66 - m.x114 - m.x273 + m.x274 == 0)

m.c581 = Constraint(expr=   m.x67 - m.x115 - m.x274 + m.x275 == 0)

m.c582 = Constraint(expr=   m.x68 - m.x116 - m.x275 + m.x276 == 0)

m.c583 = Constraint(expr=   m.x70 - m.x106 - m.x277 + m.x278 == 0)

m.c584 = Constraint(expr=   m.x71 - m.x107 - m.x278 + m.x279 == 0)

m.c585 = Constraint(expr=   m.x72 - m.x108 - m.x279 + m.x280 == 0)

m.c586 = Constraint(expr=   m.x74 - m.x130 - m.x281 + m.x282 == 0)

m.c587 = Constraint(expr=   m.x75 - m.x131 - m.x282 + m.x283 == 0)

m.c588 = Constraint(expr=   m.x76 - m.x132 - m.x283 + m.x284 == 0)

m.c589 = Constraint(expr=   m.x78 - m.x122 - m.x285 + m.x286 == 0)

m.c590 = Constraint(expr=   m.x79 - m.x123 - m.x286 + m.x287 == 0)

m.c591 = Constraint(expr=   m.x80 - m.x124 - m.x287 + m.x288 == 0)

m.c592 = Constraint(expr=   m.x82 - m.x134 - m.x289 + m.x290 == 0)

m.c593 = Constraint(expr=   m.x83 - m.x135 - m.x290 + m.x291 == 0)

m.c594 = Constraint(expr=   m.x84 - m.x136 - m.x291 + m.x292 == 0)

m.c595 = Constraint(expr=   m.x86 - m.x126 - m.x293 + m.x294 == 0)

m.c596 = Constraint(expr=   m.x87 - m.x127 - m.x294 + m.x295 == 0)

m.c597 = Constraint(expr=   m.x88 - m.x128 - m.x295 + m.x296 == 0)

m.c598 = Constraint(expr=   m.x90 - m.x118 - m.x297 + m.x298 == 0)

m.c599 = Constraint(expr=   m.x91 - m.x119 - m.x298 + m.x299 == 0)

m.c600 = Constraint(expr=   m.x92 - m.x120 - m.x299 + m.x300 == 0)

m.c601 = Constraint(expr=   m.x94 - m.x110 - m.x301 + m.x302 == 0)

m.c602 = Constraint(expr=   m.x95 - m.x111 - m.x302 + m.x303 == 0)

m.c603 = Constraint(expr=   m.x96 - m.x112 - m.x303 + m.x304 == 0)

m.c604 = Constraint(expr=   m.x65 - m.x113 + m.x273 == 200)

m.c605 = Constraint(expr=   m.x69 - m.x105 + m.x277 == 100)

m.c606 = Constraint(expr=   m.x73 - m.x129 + m.x281 == 100)

m.c607 = Constraint(expr=   m.x77 - m.x121 + m.x285 == 200)

m.c608 = Constraint(expr=   m.x81 - m.x133 + m.x289 == 50)

m.c609 = Constraint(expr=   m.x85 - m.x125 + m.x293 == 200)

m.c610 = Constraint(expr=   m.x89 - m.x117 + m.x297 == 130)

m.c611 = Constraint(expr=   m.x93 - m.x109 + m.x301 == 170)

m.c612 = Constraint(expr= - m.x241 - m.x242 - m.x243 - m.x244 + m.x249 + m.x250 + m.x251 + m.x252 == 72)

m.c613 = Constraint(expr= - m.x245 - m.x246 - m.x247 - m.x248 + m.x253 + m.x254 + m.x255 + m.x256 == 72)

m.c614 = Constraint(expr= - m.b33 + m.b34 + m.x305 >= 0)

m.c615 = Constraint(expr= - m.b34 + m.b35 + m.x306 >= 0)

m.c616 = Constraint(expr= - m.b35 + m.b36 + m.x307 >= 0)

m.c617 = Constraint(expr= - m.b37 + m.b38 + m.x308 >= 0)

m.c618 = Constraint(expr= - m.b38 + m.b39 + m.x309 >= 0)

m.c619 = Constraint(expr= - m.b39 + m.b40 + m.x310 >= 0)

m.c620 = Constraint(expr= - m.b41 + m.b42 + m.x308 >= 0)

m.c621 = Constraint(expr= - m.b42 + m.b43 + m.x309 >= 0)

m.c622 = Constraint(expr= - m.b43 + m.b44 + m.x310 >= 0)

m.c623 = Constraint(expr= - m.b45 + m.b46 + m.x305 >= 0)

m.c624 = Constraint(expr= - m.b46 + m.b47 + m.x306 >= 0)

m.c625 = Constraint(expr= - m.b47 + m.b48 + m.x307 >= 0)

m.c626 = Constraint(expr=   m.b33 - m.b34 + m.x305 >= 0)

m.c627 = Constraint(expr=   m.b34 - m.b35 + m.x306 >= 0)

m.c628 = Constraint(expr=   m.b35 - m.b36 + m.x307 >= 0)

m.c629 = Constraint(expr=   m.b37 - m.b38 + m.x308 >= 0)

m.c630 = Constraint(expr=   m.b38 - m.b39 + m.x309 >= 0)

m.c631 = Constraint(expr=   m.b39 - m.b40 + m.x310 >= 0)

m.c632 = Constraint(expr=   m.b41 - m.b42 + m.x308 >= 0)

m.c633 = Constraint(expr=   m.b42 - m.b43 + m.x309 >= 0)

m.c634 = Constraint(expr=   m.b43 - m.b44 + m.x310 >= 0)

m.c635 = Constraint(expr=   m.b45 - m.b46 + m.x305 >= 0)

m.c636 = Constraint(expr=   m.b46 - m.b47 + m.x306 >= 0)

m.c637 = Constraint(expr=   m.b47 - m.b48 + m.x307 >= 0)

m.c638 = Constraint(expr=   0.2*m.x257 + 0.2*m.x258 + 0.2*m.x259 + 0.2*m.x260 + 0.2*m.x261 + 0.2*m.x262 + 0.2*m.x263
                          + 0.2*m.x264 + 0.2*m.x265 + 0.2*m.x266 + 0.2*m.x267 + 0.2*m.x268 + 0.2*m.x269 + 0.2*m.x270
                          + 0.2*m.x271 + 0.2*m.x272 + m.x343 >= 970)

m.c639 = Constraint(expr= - 12.5*m.x144 + m.x344 >= -400)

m.c641 = Constraint(expr=-m.x311*m.x50 + m.x66 == 0)

m.c642 = Constraint(expr=-m.x312*m.x51 + m.x67 == 0)

m.c643 = Constraint(expr=-m.x313*m.x52 + m.x68 == 0)

m.c644 = Constraint(expr=-m.x315*m.x50 + m.x70 == 0)

m.c645 = Constraint(expr=-m.x316*m.x51 + m.x71 == 0)

m.c646 = Constraint(expr=-m.x317*m.x52 + m.x72 == 0)

m.c647 = Constraint(expr=-m.x319*m.x54 + m.x74 == 0)

m.c648 = Constraint(expr=-m.x320*m.x55 + m.x75 == 0)

m.c649 = Constraint(expr=-m.x321*m.x56 + m.x76 == 0)

m.c650 = Constraint(expr=-m.x323*m.x54 + m.x78 == 0)

m.c651 = Constraint(expr=-m.x324*m.x55 + m.x79 == 0)

m.c652 = Constraint(expr=-m.x325*m.x56 + m.x80 == 0)

m.c653 = Constraint(expr=-m.x327*m.x58 + m.x82 == 0)

m.c654 = Constraint(expr=-m.x328*m.x59 + m.x83 == 0)

m.c655 = Constraint(expr=-m.x329*m.x60 + m.x84 == 0)

m.c656 = Constraint(expr=-m.x331*m.x58 + m.x86 == 0)

m.c657 = Constraint(expr=-m.x332*m.x59 + m.x87 == 0)

m.c658 = Constraint(expr=-m.x333*m.x60 + m.x88 == 0)

m.c659 = Constraint(expr=-m.x335*m.x62 + m.x90 == 0)

m.c660 = Constraint(expr=-m.x336*m.x63 + m.x91 == 0)

m.c661 = Constraint(expr=-m.x337*m.x64 + m.x92 == 0)

m.c662 = Constraint(expr=-m.x339*m.x62 + m.x94 == 0)

m.c663 = Constraint(expr=-m.x340*m.x63 + m.x95 == 0)

m.c664 = Constraint(expr=-m.x341*m.x64 + m.x96 == 0)

m.c665 = Constraint(expr=-m.x311*m.x257 + m.x273 == 0)

m.c666 = Constraint(expr=-m.x312*m.x258 + m.x274 == 0)

m.c667 = Constraint(expr=-m.x313*m.x259 + m.x275 == 0)

m.c668 = Constraint(expr=-m.x314*m.x260 + m.x276 == 0)

m.c669 = Constraint(expr=-m.x315*m.x257 + m.x277 == 0)

m.c670 = Constraint(expr=-m.x316*m.x258 + m.x278 == 0)

m.c671 = Constraint(expr=-m.x317*m.x259 + m.x279 == 0)

m.c672 = Constraint(expr=-m.x318*m.x260 + m.x280 == 0)

m.c673 = Constraint(expr=-m.x319*m.x261 + m.x281 == 0)

m.c674 = Constraint(expr=-m.x320*m.x262 + m.x282 == 0)

m.c675 = Constraint(expr=-m.x321*m.x263 + m.x283 == 0)

m.c676 = Constraint(expr=-m.x322*m.x264 + m.x284 == 0)

m.c677 = Constraint(expr=-m.x323*m.x261 + m.x285 == 0)

m.c678 = Constraint(expr=-m.x324*m.x262 + m.x286 == 0)

m.c679 = Constraint(expr=-m.x325*m.x263 + m.x287 == 0)

m.c680 = Constraint(expr=-m.x326*m.x264 + m.x288 == 0)

m.c681 = Constraint(expr=-m.x327*m.x265 + m.x289 == 0)

m.c682 = Constraint(expr=-m.x328*m.x266 + m.x290 == 0)

m.c683 = Constraint(expr=-m.x329*m.x267 + m.x291 == 0)

m.c684 = Constraint(expr=-m.x330*m.x268 + m.x292 == 0)

m.c685 = Constraint(expr=-m.x331*m.x265 + m.x293 == 0)

m.c686 = Constraint(expr=-m.x332*m.x266 + m.x294 == 0)

m.c687 = Constraint(expr=-m.x333*m.x267 + m.x295 == 0)

m.c688 = Constraint(expr=-m.x334*m.x268 + m.x296 == 0)

m.c689 = Constraint(expr=-m.x335*m.x269 + m.x297 == 0)

m.c690 = Constraint(expr=-m.x336*m.x270 + m.x298 == 0)

m.c691 = Constraint(expr=-m.x337*m.x271 + m.x299 == 0)

m.c692 = Constraint(expr=-m.x338*m.x272 + m.x300 == 0)

m.c693 = Constraint(expr=-m.x339*m.x269 + m.x301 == 0)

m.c694 = Constraint(expr=-m.x340*m.x270 + m.x302 == 0)

m.c695 = Constraint(expr=-m.x341*m.x271 + m.x303 == 0)

m.c696 = Constraint(expr=-m.x342*m.x272 + m.x304 == 0)
