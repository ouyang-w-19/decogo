#  MINLP written by GAMS Convert at 04/21/18 13:51:21
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        566      168      227      171        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        311      231       80        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1933     1826      107        0
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
m.b49 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b50 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b51 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b52 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b53 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b54 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b55 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b56 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b57 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b58 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b59 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b60 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x105 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,1000),initialize=0)
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
m.x137 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,500),initialize=0)
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
m.x252 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x255 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x258 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x262 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x263 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x264 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x265 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x266 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x267 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x268 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x269 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x270 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x271 = Var(within=Reals,bounds=(8,8),initialize=8)
m.x272 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x273 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x274 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x275 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x276 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x277 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x278 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x279 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x280 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x281 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x282 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x283 = Var(within=Reals,bounds=(125,625),initialize=125)
m.x284 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x285 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x286 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x287 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x289 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x290 = Var(within=Reals,bounds=(375,875),initialize=375)
m.x291 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x292 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x293 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x294 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x295 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x296 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x297 = Var(within=Reals,bounds=(250,750),initialize=250)
m.x298 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x299 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x300 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x301 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x302 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x303 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x304 = Var(within=Reals,bounds=(250,750),initialize=250)
m.x305 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x306 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x307 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x309 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,1000),initialize=0)

m.obj = Objective(expr=8*m.x272*m.x283 + 8*m.x273*m.x284 + 8*m.x274*m.x285 + 8*m.x275*m.x286 + 8*m.x276*m.x287 + 8*
                       m.x277*m.x288 + 8*m.x278*m.x289 + 8*m.x272*m.x290 + 8*m.x273*m.x291 + 8*m.x274*m.x292 + 8*m.x275*
                       m.x293 + 8*m.x276*m.x294 + 8*m.x277*m.x295 + 8*m.x278*m.x296 + 5*m.x272*m.x297 + 5*m.x273*m.x298
                        + 5*m.x274*m.x299 + 5*m.x275*m.x300 + 5*m.x276*m.x301 + 5*m.x277*m.x302 + 5*m.x278*m.x303 + 5*
                       m.x272*m.x304 + 5*m.x273*m.x305 + 5*m.x274*m.x306 + 5*m.x275*m.x307 + 5*m.x276*m.x308 + 5*m.x277*
                       m.x309 + 5*m.x278*m.x310 + 50000*m.x87 + 5000*m.x279 + 5000*m.x280 + 8000*m.x281 + 8000*m.x282
                        - 50000, sense=minimize)

m.c2 = Constraint(expr=   m.x88 == 1000)

m.c3 = Constraint(expr= - m.x88 + m.x89 + m.x168 == 0)

m.c4 = Constraint(expr= - m.x89 + m.x90 + m.x169 == 0)

m.c5 = Constraint(expr= - m.x90 + m.x91 + m.x170 == 0)

m.c6 = Constraint(expr= - m.x91 + m.x92 + m.x171 == 0)

m.c7 = Constraint(expr= - m.x92 + m.x93 + m.x172 == 0)

m.c8 = Constraint(expr= - m.x93 + m.x94 + m.x173 == 0)

m.c9 = Constraint(expr= - m.x94 + m.x95 + m.x174 == 0)

m.c10 = Constraint(expr=   m.x96 == 250)

m.c11 = Constraint(expr= - m.x96 + m.x97 - m.x168 + m.x175 + m.x182 == 0)

m.c12 = Constraint(expr= - m.x97 + m.x98 - m.x169 + m.x176 + m.x183 == 0)

m.c13 = Constraint(expr= - m.x98 + m.x99 - m.x170 + m.x177 + m.x184 == 0)

m.c14 = Constraint(expr= - m.x99 + m.x100 - m.x171 + m.x178 + m.x185 == 0)

m.c15 = Constraint(expr= - m.x100 + m.x101 - m.x172 + m.x179 + m.x186 == 0)

m.c16 = Constraint(expr= - m.x101 + m.x102 - m.x173 + m.x180 + m.x187 == 0)

m.c17 = Constraint(expr= - m.x102 + m.x103 - m.x174 + m.x181 + m.x188 == 0)

m.c18 = Constraint(expr=   m.x104 == 0)

m.c19 = Constraint(expr= - m.x104 + m.x105 - m.x175 + m.x189 == 0)

m.c20 = Constraint(expr= - m.x105 + m.x106 - m.x176 + m.x190 == 0)

m.c21 = Constraint(expr= - m.x106 + m.x107 - m.x177 + m.x191 == 0)

m.c22 = Constraint(expr= - m.x107 + m.x108 - m.x178 + m.x192 == 0)

m.c23 = Constraint(expr= - m.x108 + m.x109 - m.x179 + m.x193 == 0)

m.c24 = Constraint(expr= - m.x109 + m.x110 - m.x180 + m.x194 == 0)

m.c25 = Constraint(expr= - m.x110 + m.x111 - m.x181 + m.x195 == 0)

m.c26 = Constraint(expr=   m.x112 == 0)

m.c27 = Constraint(expr= - m.x112 + m.x113 - m.x182 + m.x196 == 0)

m.c28 = Constraint(expr= - m.x113 + m.x114 - m.x183 + m.x197 == 0)

m.c29 = Constraint(expr= - m.x114 + m.x115 - m.x184 + m.x198 == 0)

m.c30 = Constraint(expr= - m.x115 + m.x116 - m.x185 + m.x199 == 0)

m.c31 = Constraint(expr= - m.x116 + m.x117 - m.x186 + m.x200 == 0)

m.c32 = Constraint(expr= - m.x117 + m.x118 - m.x187 + m.x201 == 0)

m.c33 = Constraint(expr= - m.x118 + m.x119 - m.x188 + m.x202 == 0)

m.c34 = Constraint(expr=   m.x120 == 1000)

m.c35 = Constraint(expr= - m.x120 + m.x121 + m.x203 == 0)

m.c36 = Constraint(expr= - m.x121 + m.x122 + m.x204 == 0)

m.c37 = Constraint(expr= - m.x122 + m.x123 + m.x205 == 0)

m.c38 = Constraint(expr= - m.x123 + m.x124 + m.x206 == 0)

m.c39 = Constraint(expr= - m.x124 + m.x125 + m.x207 == 0)

m.c40 = Constraint(expr= - m.x125 + m.x126 + m.x208 == 0)

m.c41 = Constraint(expr= - m.x126 + m.x127 + m.x209 == 0)

m.c42 = Constraint(expr=   m.x128 == 750)

m.c43 = Constraint(expr= - m.x128 + m.x129 - m.x203 + m.x210 + m.x217 == 0)

m.c44 = Constraint(expr= - m.x129 + m.x130 - m.x204 + m.x211 + m.x218 == 0)

m.c45 = Constraint(expr= - m.x130 + m.x131 - m.x205 + m.x212 + m.x219 == 0)

m.c46 = Constraint(expr= - m.x131 + m.x132 - m.x206 + m.x213 + m.x220 == 0)

m.c47 = Constraint(expr= - m.x132 + m.x133 - m.x207 + m.x214 + m.x221 == 0)

m.c48 = Constraint(expr= - m.x133 + m.x134 - m.x208 + m.x215 + m.x222 == 0)

m.c49 = Constraint(expr= - m.x134 + m.x135 - m.x209 + m.x216 + m.x223 == 0)

m.c50 = Constraint(expr=   m.x136 == 0)

m.c51 = Constraint(expr= - m.x136 + m.x137 - m.x210 + m.x224 == 0)

m.c52 = Constraint(expr= - m.x137 + m.x138 - m.x211 + m.x225 == 0)

m.c53 = Constraint(expr= - m.x138 + m.x139 - m.x212 + m.x226 == 0)

m.c54 = Constraint(expr= - m.x139 + m.x140 - m.x213 + m.x227 == 0)

m.c55 = Constraint(expr= - m.x140 + m.x141 - m.x214 + m.x228 == 0)

m.c56 = Constraint(expr= - m.x141 + m.x142 - m.x215 + m.x229 == 0)

m.c57 = Constraint(expr= - m.x142 + m.x143 - m.x216 + m.x230 == 0)

m.c58 = Constraint(expr=   m.x144 == 0)

m.c59 = Constraint(expr= - m.x144 + m.x145 - m.x217 + m.x231 == 0)

m.c60 = Constraint(expr= - m.x145 + m.x146 - m.x218 + m.x232 == 0)

m.c61 = Constraint(expr= - m.x146 + m.x147 - m.x219 + m.x233 == 0)

m.c62 = Constraint(expr= - m.x147 + m.x148 - m.x220 + m.x234 == 0)

m.c63 = Constraint(expr= - m.x148 + m.x149 - m.x221 + m.x235 == 0)

m.c64 = Constraint(expr= - m.x149 + m.x150 - m.x222 + m.x236 == 0)

m.c65 = Constraint(expr= - m.x150 + m.x151 - m.x223 + m.x237 == 0)

m.c66 = Constraint(expr=   m.x152 == 500)

m.c67 = Constraint(expr= - m.x152 + m.x153 + m.x238 == 0)

m.c68 = Constraint(expr= - m.x153 + m.x154 + m.x239 == 0)

m.c69 = Constraint(expr= - m.x154 + m.x155 + m.x240 == 0)

m.c70 = Constraint(expr= - m.x155 + m.x156 + m.x241 == 0)

m.c71 = Constraint(expr= - m.x156 + m.x157 + m.x242 == 0)

m.c72 = Constraint(expr= - m.x157 + m.x158 + m.x243 == 0)

m.c73 = Constraint(expr= - m.x158 + m.x159 + m.x244 == 0)

m.c74 = Constraint(expr=   m.x160 == 500)

m.c75 = Constraint(expr= - m.x160 + m.x161 + m.x245 == 0)

m.c76 = Constraint(expr= - m.x161 + m.x162 + m.x246 == 0)

m.c77 = Constraint(expr= - m.x162 + m.x163 + m.x247 == 0)

m.c78 = Constraint(expr= - m.x163 + m.x164 + m.x248 == 0)

m.c79 = Constraint(expr= - m.x164 + m.x165 + m.x249 == 0)

m.c80 = Constraint(expr= - m.x165 + m.x166 + m.x250 == 0)

m.c81 = Constraint(expr= - m.x166 + m.x167 + m.x251 == 0)

m.c82 = Constraint(expr=   m.x97 <= 1000)

m.c83 = Constraint(expr=   m.x98 <= 1000)

m.c84 = Constraint(expr=   m.x99 <= 1000)

m.c85 = Constraint(expr=   m.x100 <= 1000)

m.c86 = Constraint(expr=   m.x101 <= 1000)

m.c87 = Constraint(expr=   m.x102 <= 1000)

m.c88 = Constraint(expr=   m.x103 <= 1000)

m.c89 = Constraint(expr=   m.x129 <= 1000)

m.c90 = Constraint(expr=   m.x130 <= 1000)

m.c91 = Constraint(expr=   m.x131 <= 1000)

m.c92 = Constraint(expr=   m.x132 <= 1000)

m.c93 = Constraint(expr=   m.x133 <= 1000)

m.c94 = Constraint(expr=   m.x134 <= 1000)

m.c95 = Constraint(expr=   m.x135 <= 1000)

m.c96 = Constraint(expr=   m.x105 + m.x137 + m.x153 <= 1000)

m.c97 = Constraint(expr=   m.x106 + m.x138 + m.x154 <= 1000)

m.c98 = Constraint(expr=   m.x107 + m.x139 + m.x155 <= 1000)

m.c99 = Constraint(expr=   m.x108 + m.x140 + m.x156 <= 1000)

m.c100 = Constraint(expr=   m.x109 + m.x141 + m.x157 <= 1000)

m.c101 = Constraint(expr=   m.x110 + m.x142 + m.x158 <= 1000)

m.c102 = Constraint(expr=   m.x111 + m.x143 + m.x159 <= 1000)

m.c103 = Constraint(expr=   m.x113 + m.x145 + m.x161 <= 1000)

m.c104 = Constraint(expr=   m.x114 + m.x146 + m.x162 <= 1000)

m.c105 = Constraint(expr=   m.x115 + m.x147 + m.x163 <= 1000)

m.c106 = Constraint(expr=   m.x116 + m.x148 + m.x164 <= 1000)

m.c107 = Constraint(expr=   m.x117 + m.x149 + m.x165 <= 1000)

m.c108 = Constraint(expr=   m.x118 + m.x150 + m.x166 <= 1000)

m.c109 = Constraint(expr=   m.x119 + m.x151 + m.x167 <= 1000)

m.c110 = Constraint(expr=   m.x97 >= 0)

m.c111 = Constraint(expr=   m.x98 >= 0)

m.c112 = Constraint(expr=   m.x99 >= 0)

m.c113 = Constraint(expr=   m.x100 >= 0)

m.c114 = Constraint(expr=   m.x101 >= 0)

m.c115 = Constraint(expr=   m.x102 >= 0)

m.c116 = Constraint(expr=   m.x103 >= 0)

m.c117 = Constraint(expr=   m.x129 >= 0)

m.c118 = Constraint(expr=   m.x130 >= 0)

m.c119 = Constraint(expr=   m.x131 >= 0)

m.c120 = Constraint(expr=   m.x132 >= 0)

m.c121 = Constraint(expr=   m.x133 >= 0)

m.c122 = Constraint(expr=   m.x134 >= 0)

m.c123 = Constraint(expr=   m.x135 >= 0)

m.c124 = Constraint(expr=   m.x105 + m.x137 + m.x153 >= 0)

m.c125 = Constraint(expr=   m.x106 + m.x138 + m.x154 >= 0)

m.c126 = Constraint(expr=   m.x107 + m.x139 + m.x155 >= 0)

m.c127 = Constraint(expr=   m.x108 + m.x140 + m.x156 >= 0)

m.c128 = Constraint(expr=   m.x109 + m.x141 + m.x157 >= 0)

m.c129 = Constraint(expr=   m.x110 + m.x142 + m.x158 >= 0)

m.c130 = Constraint(expr=   m.x111 + m.x143 + m.x159 >= 0)

m.c131 = Constraint(expr=   m.x113 + m.x145 + m.x161 >= 0)

m.c132 = Constraint(expr=   m.x114 + m.x146 + m.x162 >= 0)

m.c133 = Constraint(expr=   m.x115 + m.x147 + m.x163 >= 0)

m.c134 = Constraint(expr=   m.x116 + m.x148 + m.x164 >= 0)

m.c135 = Constraint(expr=   m.x117 + m.x149 + m.x165 >= 0)

m.c136 = Constraint(expr=   m.x118 + m.x150 + m.x166 >= 0)

m.c137 = Constraint(expr=   m.x119 + m.x151 + m.x167 >= 0)

m.c138 = Constraint(expr= - 0.015*m.x105 + 0.035*m.x137 - 0.005*m.x153 <= 0)

m.c139 = Constraint(expr= - 0.015*m.x106 + 0.035*m.x138 - 0.005*m.x154 <= 0)

m.c140 = Constraint(expr= - 0.015*m.x107 + 0.035*m.x139 - 0.005*m.x155 <= 0)

m.c141 = Constraint(expr= - 0.015*m.x108 + 0.035*m.x140 - 0.005*m.x156 <= 0)

m.c142 = Constraint(expr= - 0.015*m.x109 + 0.035*m.x141 - 0.005*m.x157 <= 0)

m.c143 = Constraint(expr= - 0.015*m.x110 + 0.035*m.x142 - 0.005*m.x158 <= 0)

m.c144 = Constraint(expr= - 0.015*m.x111 + 0.035*m.x143 - 0.005*m.x159 <= 0)

m.c145 = Constraint(expr= - 0.045*m.x113 + 0.005*m.x145 - 0.005*m.x161 <= 0)

m.c146 = Constraint(expr= - 0.045*m.x114 + 0.005*m.x146 - 0.005*m.x162 <= 0)

m.c147 = Constraint(expr= - 0.045*m.x115 + 0.005*m.x147 - 0.005*m.x163 <= 0)

m.c148 = Constraint(expr= - 0.045*m.x116 + 0.005*m.x148 - 0.005*m.x164 <= 0)

m.c149 = Constraint(expr= - 0.045*m.x117 + 0.005*m.x149 - 0.005*m.x165 <= 0)

m.c150 = Constraint(expr= - 0.045*m.x118 + 0.005*m.x150 - 0.005*m.x166 <= 0)

m.c151 = Constraint(expr= - 0.045*m.x119 + 0.005*m.x151 - 0.005*m.x167 <= 0)

m.c152 = Constraint(expr= - 0.005*m.x105 + 0.045*m.x137 + 0.005*m.x153 >= 0)

m.c153 = Constraint(expr= - 0.005*m.x106 + 0.045*m.x138 + 0.005*m.x154 >= 0)

m.c154 = Constraint(expr= - 0.005*m.x107 + 0.045*m.x139 + 0.005*m.x155 >= 0)

m.c155 = Constraint(expr= - 0.005*m.x108 + 0.045*m.x140 + 0.005*m.x156 >= 0)

m.c156 = Constraint(expr= - 0.005*m.x109 + 0.045*m.x141 + 0.005*m.x157 >= 0)

m.c157 = Constraint(expr= - 0.005*m.x110 + 0.045*m.x142 + 0.005*m.x158 >= 0)

m.c158 = Constraint(expr= - 0.005*m.x111 + 0.045*m.x143 + 0.005*m.x159 >= 0)

m.c159 = Constraint(expr= - 0.035*m.x113 + 0.015*m.x145 + 0.005*m.x161 >= 0)

m.c160 = Constraint(expr= - 0.035*m.x114 + 0.015*m.x146 + 0.005*m.x162 >= 0)

m.c161 = Constraint(expr= - 0.035*m.x115 + 0.015*m.x147 + 0.005*m.x163 >= 0)

m.c162 = Constraint(expr= - 0.035*m.x116 + 0.015*m.x148 + 0.005*m.x164 >= 0)

m.c163 = Constraint(expr= - 0.035*m.x117 + 0.015*m.x149 + 0.005*m.x165 >= 0)

m.c164 = Constraint(expr= - 0.035*m.x118 + 0.015*m.x150 + 0.005*m.x166 >= 0)

m.c165 = Constraint(expr= - 0.035*m.x119 + 0.015*m.x151 + 0.005*m.x167 >= 0)

m.c166 = Constraint(expr=   m.b15 + m.b43 <= 1)

m.c167 = Constraint(expr=   m.b16 + m.b44 <= 1)

m.c168 = Constraint(expr=   m.b17 + m.b45 <= 1)

m.c169 = Constraint(expr=   m.b18 + m.b46 <= 1)

m.c170 = Constraint(expr=   m.b19 + m.b47 <= 1)

m.c171 = Constraint(expr=   m.b20 + m.b48 <= 1)

m.c172 = Constraint(expr=   m.b21 + m.b49 <= 1)

m.c173 = Constraint(expr=   m.b29 + m.b43 <= 1)

m.c174 = Constraint(expr=   m.b30 + m.b44 <= 1)

m.c175 = Constraint(expr=   m.b31 + m.b45 <= 1)

m.c176 = Constraint(expr=   m.b32 + m.b46 <= 1)

m.c177 = Constraint(expr=   m.b33 + m.b47 <= 1)

m.c178 = Constraint(expr=   m.b34 + m.b48 <= 1)

m.c179 = Constraint(expr=   m.b35 + m.b49 <= 1)

m.c180 = Constraint(expr=   m.b22 + m.b50 <= 1)

m.c181 = Constraint(expr=   m.b23 + m.b51 <= 1)

m.c182 = Constraint(expr=   m.b24 + m.b52 <= 1)

m.c183 = Constraint(expr=   m.b25 + m.b53 <= 1)

m.c184 = Constraint(expr=   m.b26 + m.b54 <= 1)

m.c185 = Constraint(expr=   m.b27 + m.b55 <= 1)

m.c186 = Constraint(expr=   m.b28 + m.b56 <= 1)

m.c187 = Constraint(expr=   m.b36 + m.b50 <= 1)

m.c188 = Constraint(expr=   m.b37 + m.b51 <= 1)

m.c189 = Constraint(expr=   m.b38 + m.b52 <= 1)

m.c190 = Constraint(expr=   m.b39 + m.b53 <= 1)

m.c191 = Constraint(expr=   m.b40 + m.b54 <= 1)

m.c192 = Constraint(expr=   m.b41 + m.b55 <= 1)

m.c193 = Constraint(expr=   m.b42 + m.b56 <= 1)

m.c194 = Constraint(expr=   m.x95 == 0)

m.c195 = Constraint(expr=   m.x127 == 0)

m.c196 = Constraint(expr=   m.x189 + m.x190 + m.x191 + m.x192 + m.x193 + m.x194 + m.x195 + m.x224 + m.x225 + m.x226
                          + m.x227 + m.x228 + m.x229 + m.x230 + m.x238 + m.x239 + m.x240 + m.x241 + m.x242 + m.x243
                          + m.x244 == 1000)

m.c197 = Constraint(expr=   m.x196 + m.x197 + m.x198 + m.x199 + m.x200 + m.x201 + m.x202 + m.x231 + m.x232 + m.x233
                          + m.x234 + m.x235 + m.x236 + m.x237 + m.x245 + m.x246 + m.x247 + m.x248 + m.x249 + m.x250
                          + m.x251 == 1000)

m.c198 = Constraint(expr=   m.b57 + m.b58 + m.b60 + m.b62 + m.b64 + m.b66 == 1)

m.c199 = Constraint(expr=   m.b59 + m.b61 + m.b63 + m.b65 + m.b67 + m.b68 == 1)

m.c200 = Constraint(expr=   m.b69 + m.b70 + m.b72 + m.b74 + m.b76 + m.b78 == 1)

m.c201 = Constraint(expr=   m.b71 + m.b73 + m.b75 + m.b77 + m.b79 + m.b80 == 1)

m.c202 = Constraint(expr=   m.b1 + m.b8 <= 1)

m.c203 = Constraint(expr=   m.b2 + m.b9 <= 1)

m.c204 = Constraint(expr=   m.b3 + m.b10 <= 1)

m.c205 = Constraint(expr=   m.b4 + m.b11 <= 1)

m.c206 = Constraint(expr=   m.b5 + m.b12 <= 1)

m.c207 = Constraint(expr=   m.b6 + m.b13 <= 1)

m.c208 = Constraint(expr=   m.b7 + m.b14 <= 1)

m.c209 = Constraint(expr=   m.b43 + m.b50 == 1)

m.c210 = Constraint(expr=   m.b44 + m.b51 == 1)

m.c211 = Constraint(expr=   m.b45 + m.b52 == 1)

m.c212 = Constraint(expr=   m.b46 + m.b53 == 1)

m.c213 = Constraint(expr=   m.b47 + m.b54 == 1)

m.c214 = Constraint(expr=   m.b48 + m.b55 == 1)

m.c215 = Constraint(expr=   m.b49 + m.b56 == 1)

m.c216 = Constraint(expr=   m.b1 - m.b57 <= 0)

m.c217 = Constraint(expr=   m.b2 - m.b57 - m.b58 <= 0)

m.c218 = Constraint(expr=   m.b3 - m.b57 - m.b58 - m.b60 <= 0)

m.c219 = Constraint(expr=   m.b4 - m.b57 - m.b58 - m.b60 - m.b62 <= 0)

m.c220 = Constraint(expr=   m.b5 - m.b57 - m.b58 - m.b60 - m.b62 - m.b64 <= 0)

m.c221 = Constraint(expr=   m.b6 - m.b57 - m.b58 - m.b60 - m.b62 - m.b64 - m.b66 <= 0)

m.c222 = Constraint(expr=   m.b7 - m.b57 - m.b58 - m.b60 - m.b62 - m.b64 - m.b66 <= 0)

m.c223 = Constraint(expr=   m.b8 <= 0)

m.c224 = Constraint(expr=   m.b9 - m.b59 <= 0)

m.c225 = Constraint(expr=   m.b10 - m.b59 - m.b61 <= 0)

m.c226 = Constraint(expr=   m.b11 - m.b59 - m.b61 - m.b63 <= 0)

m.c227 = Constraint(expr=   m.b12 - m.b59 - m.b61 - m.b63 - m.b65 <= 0)

m.c228 = Constraint(expr=   m.b13 - m.b59 - m.b61 - m.b63 - m.b65 - m.b67 <= 0)

m.c229 = Constraint(expr=   m.b14 - m.b59 - m.b61 - m.b63 - m.b65 - m.b67 - m.b68 <= 0)

m.c230 = Constraint(expr=   m.b1 - m.b69 - m.b70 - m.b72 - m.b74 - m.b76 - m.b78 <= 0)

m.c231 = Constraint(expr=   m.b2 - m.b70 - m.b72 - m.b74 - m.b76 - m.b78 <= 0)

m.c232 = Constraint(expr=   m.b3 - m.b72 - m.b74 - m.b76 - m.b78 <= 0)

m.c233 = Constraint(expr=   m.b4 - m.b74 - m.b76 - m.b78 <= 0)

m.c234 = Constraint(expr=   m.b5 - m.b76 - m.b78 <= 0)

m.c235 = Constraint(expr=   m.b6 - m.b78 <= 0)

m.c236 = Constraint(expr=   m.b7 <= 0)

m.c237 = Constraint(expr=   m.b8 - m.b71 - m.b73 - m.b75 - m.b77 - m.b79 - m.b80 <= 0)

m.c238 = Constraint(expr=   m.b9 - m.b71 - m.b73 - m.b75 - m.b77 - m.b79 - m.b80 <= 0)

m.c239 = Constraint(expr=   m.b10 - m.b73 - m.b75 - m.b77 - m.b79 - m.b80 <= 0)

m.c240 = Constraint(expr=   m.b11 - m.b75 - m.b77 - m.b79 - m.b80 <= 0)

m.c241 = Constraint(expr=   m.b12 - m.b77 - m.b79 - m.b80 <= 0)

m.c242 = Constraint(expr=   m.b13 - m.b79 - m.b80 <= 0)

m.c243 = Constraint(expr=   m.b14 - m.b80 <= 0)

m.c244 = Constraint(expr= - m.b43 - m.b51 + m.x81 >= -1)

m.c245 = Constraint(expr= - m.b44 - m.b52 + m.x82 >= -1)

m.c246 = Constraint(expr= - m.b45 - m.b53 + m.x83 >= -1)

m.c247 = Constraint(expr= - m.b46 - m.b54 + m.x84 >= -1)

m.c248 = Constraint(expr= - m.b47 - m.b55 + m.x85 >= -1)

m.c249 = Constraint(expr= - m.b48 - m.b56 + m.x86 >= -1)

m.c250 = Constraint(expr= - m.b44 - m.b50 + m.x81 >= -1)

m.c251 = Constraint(expr= - m.b45 - m.b51 + m.x82 >= -1)

m.c252 = Constraint(expr= - m.b46 - m.b52 + m.x83 >= -1)

m.c253 = Constraint(expr= - m.b47 - m.b53 + m.x84 >= -1)

m.c254 = Constraint(expr= - m.b48 - m.b54 + m.x85 >= -1)

m.c255 = Constraint(expr= - m.b49 - m.b55 + m.x86 >= -1)

m.c256 = Constraint(expr=   m.x81 + m.x82 + m.x83 + m.x84 + m.x85 + m.x86 - m.x87 == -1)

m.c257 = Constraint(expr= - 0.5*m.x96 - 0.5*m.x97 + m.x283 == 0)

m.c258 = Constraint(expr= - 0.5*m.x97 - 0.5*m.x98 + m.x284 == 0)

m.c259 = Constraint(expr= - 0.5*m.x98 - 0.5*m.x99 + m.x285 == 0)

m.c260 = Constraint(expr= - 0.5*m.x99 - 0.5*m.x100 + m.x286 == 0)

m.c261 = Constraint(expr= - 0.5*m.x100 - 0.5*m.x101 + m.x287 == 0)

m.c262 = Constraint(expr= - 0.5*m.x101 - 0.5*m.x102 + m.x288 == 0)

m.c263 = Constraint(expr= - 0.5*m.x102 - 0.5*m.x103 + m.x289 == 0)

m.c264 = Constraint(expr= - 0.5*m.x128 - 0.5*m.x129 + m.x290 == 0)

m.c265 = Constraint(expr= - 0.5*m.x129 - 0.5*m.x130 + m.x291 == 0)

m.c266 = Constraint(expr= - 0.5*m.x130 - 0.5*m.x131 + m.x292 == 0)

m.c267 = Constraint(expr= - 0.5*m.x131 - 0.5*m.x132 + m.x293 == 0)

m.c268 = Constraint(expr= - 0.5*m.x132 - 0.5*m.x133 + m.x294 == 0)

m.c269 = Constraint(expr= - 0.5*m.x133 - 0.5*m.x134 + m.x295 == 0)

m.c270 = Constraint(expr= - 0.5*m.x134 - 0.5*m.x135 + m.x296 == 0)

m.c271 = Constraint(expr= - 0.5*m.x104 - 0.5*m.x105 - 0.5*m.x136 - 0.5*m.x137 - 0.5*m.x152 - 0.5*m.x153 + m.x297 == 0)

m.c272 = Constraint(expr= - 0.5*m.x105 - 0.5*m.x106 - 0.5*m.x137 - 0.5*m.x138 - 0.5*m.x153 - 0.5*m.x154 + m.x298 == 0)

m.c273 = Constraint(expr= - 0.5*m.x106 - 0.5*m.x107 - 0.5*m.x138 - 0.5*m.x139 - 0.5*m.x154 - 0.5*m.x155 + m.x299 == 0)

m.c274 = Constraint(expr= - 0.5*m.x107 - 0.5*m.x108 - 0.5*m.x139 - 0.5*m.x140 - 0.5*m.x155 - 0.5*m.x156 + m.x300 == 0)

m.c275 = Constraint(expr= - 0.5*m.x108 - 0.5*m.x109 - 0.5*m.x140 - 0.5*m.x141 - 0.5*m.x156 - 0.5*m.x157 + m.x301 == 0)

m.c276 = Constraint(expr= - 0.5*m.x109 - 0.5*m.x110 - 0.5*m.x141 - 0.5*m.x142 - 0.5*m.x157 - 0.5*m.x158 + m.x302 == 0)

m.c277 = Constraint(expr= - 0.5*m.x110 - 0.5*m.x111 - 0.5*m.x142 - 0.5*m.x143 - 0.5*m.x158 - 0.5*m.x159 + m.x303 == 0)

m.c278 = Constraint(expr= - 0.5*m.x112 - 0.5*m.x113 - 0.5*m.x144 - 0.5*m.x145 - 0.5*m.x160 - 0.5*m.x161 + m.x304 == 0)

m.c279 = Constraint(expr= - 0.5*m.x113 - 0.5*m.x114 - 0.5*m.x145 - 0.5*m.x146 - 0.5*m.x161 - 0.5*m.x162 + m.x305 == 0)

m.c280 = Constraint(expr= - 0.5*m.x114 - 0.5*m.x115 - 0.5*m.x146 - 0.5*m.x147 - 0.5*m.x162 - 0.5*m.x163 + m.x306 == 0)

m.c281 = Constraint(expr= - 0.5*m.x115 - 0.5*m.x116 - 0.5*m.x147 - 0.5*m.x148 - 0.5*m.x163 - 0.5*m.x164 + m.x307 == 0)

m.c282 = Constraint(expr= - 0.5*m.x116 - 0.5*m.x117 - 0.5*m.x148 - 0.5*m.x149 - 0.5*m.x164 - 0.5*m.x165 + m.x308 == 0)

m.c283 = Constraint(expr= - 0.5*m.x117 - 0.5*m.x118 - 0.5*m.x149 - 0.5*m.x150 - 0.5*m.x165 - 0.5*m.x166 + m.x309 == 0)

m.c284 = Constraint(expr= - 0.5*m.x118 - 0.5*m.x119 - 0.5*m.x150 - 0.5*m.x151 - 0.5*m.x166 - 0.5*m.x167 + m.x310 == 0)

m.c285 = Constraint(expr= - 1000*m.b1 + m.x168 <= 0)

m.c286 = Constraint(expr= - 1000*m.b2 + m.x169 <= 0)

m.c287 = Constraint(expr= - 1000*m.b3 + m.x170 <= 0)

m.c288 = Constraint(expr= - 1000*m.b4 + m.x171 <= 0)

m.c289 = Constraint(expr= - 1000*m.b5 + m.x172 <= 0)

m.c290 = Constraint(expr= - 1000*m.b6 + m.x173 <= 0)

m.c291 = Constraint(expr= - 1000*m.b7 + m.x174 <= 0)

m.c292 = Constraint(expr= - 1000*m.b8 + m.x203 <= 0)

m.c293 = Constraint(expr= - 1000*m.b9 + m.x204 <= 0)

m.c294 = Constraint(expr= - 1000*m.b10 + m.x205 <= 0)

m.c295 = Constraint(expr= - 1000*m.b11 + m.x206 <= 0)

m.c296 = Constraint(expr= - 1000*m.b12 + m.x207 <= 0)

m.c297 = Constraint(expr= - 1000*m.b13 + m.x208 <= 0)

m.c298 = Constraint(expr= - 1000*m.b14 + m.x209 <= 0)

m.c299 = Constraint(expr= - 1000*m.b15 + m.x175 <= 0)

m.c300 = Constraint(expr= - 1000*m.b16 + m.x176 <= 0)

m.c301 = Constraint(expr= - 1000*m.b17 + m.x177 <= 0)

m.c302 = Constraint(expr= - 1000*m.b18 + m.x178 <= 0)

m.c303 = Constraint(expr= - 1000*m.b19 + m.x179 <= 0)

m.c304 = Constraint(expr= - 1000*m.b20 + m.x180 <= 0)

m.c305 = Constraint(expr= - 1000*m.b21 + m.x181 <= 0)

m.c306 = Constraint(expr= - 1000*m.b22 + m.x182 <= 0)

m.c307 = Constraint(expr= - 1000*m.b23 + m.x183 <= 0)

m.c308 = Constraint(expr= - 1000*m.b24 + m.x184 <= 0)

m.c309 = Constraint(expr= - 1000*m.b25 + m.x185 <= 0)

m.c310 = Constraint(expr= - 1000*m.b26 + m.x186 <= 0)

m.c311 = Constraint(expr= - 1000*m.b27 + m.x187 <= 0)

m.c312 = Constraint(expr= - 1000*m.b28 + m.x188 <= 0)

m.c313 = Constraint(expr= - 1000*m.b29 + m.x210 <= 0)

m.c314 = Constraint(expr= - 1000*m.b30 + m.x211 <= 0)

m.c315 = Constraint(expr= - 1000*m.b31 + m.x212 <= 0)

m.c316 = Constraint(expr= - 1000*m.b32 + m.x213 <= 0)

m.c317 = Constraint(expr= - 1000*m.b33 + m.x214 <= 0)

m.c318 = Constraint(expr= - 1000*m.b34 + m.x215 <= 0)

m.c319 = Constraint(expr= - 1000*m.b35 + m.x216 <= 0)

m.c320 = Constraint(expr= - 1000*m.b36 + m.x217 <= 0)

m.c321 = Constraint(expr= - 1000*m.b37 + m.x218 <= 0)

m.c322 = Constraint(expr= - 1000*m.b38 + m.x219 <= 0)

m.c323 = Constraint(expr= - 1000*m.b39 + m.x220 <= 0)

m.c324 = Constraint(expr= - 1000*m.b40 + m.x221 <= 0)

m.c325 = Constraint(expr= - 1000*m.b41 + m.x222 <= 0)

m.c326 = Constraint(expr= - 1000*m.b42 + m.x223 <= 0)

m.c327 = Constraint(expr= - 1000*m.b43 + m.x189 + m.x224 + m.x238 <= 0)

m.c328 = Constraint(expr= - 1000*m.b44 + m.x190 + m.x225 + m.x239 <= 0)

m.c329 = Constraint(expr= - 1000*m.b45 + m.x191 + m.x226 + m.x240 <= 0)

m.c330 = Constraint(expr= - 1000*m.b46 + m.x192 + m.x227 + m.x241 <= 0)

m.c331 = Constraint(expr= - 1000*m.b47 + m.x193 + m.x228 + m.x242 <= 0)

m.c332 = Constraint(expr= - 1000*m.b48 + m.x194 + m.x229 + m.x243 <= 0)

m.c333 = Constraint(expr= - 1000*m.b49 + m.x195 + m.x230 + m.x244 <= 0)

m.c334 = Constraint(expr= - 1000*m.b50 + m.x196 + m.x231 + m.x245 <= 0)

m.c335 = Constraint(expr= - 1000*m.b51 + m.x197 + m.x232 + m.x246 <= 0)

m.c336 = Constraint(expr= - 1000*m.b52 + m.x198 + m.x233 + m.x247 <= 0)

m.c337 = Constraint(expr= - 1000*m.b53 + m.x199 + m.x234 + m.x248 <= 0)

m.c338 = Constraint(expr= - 1000*m.b54 + m.x200 + m.x235 + m.x249 <= 0)

m.c339 = Constraint(expr= - 1000*m.b55 + m.x201 + m.x236 + m.x250 <= 0)

m.c340 = Constraint(expr= - 1000*m.b56 + m.x202 + m.x237 + m.x251 <= 0)

m.c341 = Constraint(expr= - m.b1 + m.x168 >= 0)

m.c342 = Constraint(expr= - m.b2 + m.x169 >= 0)

m.c343 = Constraint(expr= - m.b3 + m.x170 >= 0)

m.c344 = Constraint(expr= - m.b4 + m.x171 >= 0)

m.c345 = Constraint(expr= - m.b5 + m.x172 >= 0)

m.c346 = Constraint(expr= - m.b6 + m.x173 >= 0)

m.c347 = Constraint(expr= - m.b7 + m.x174 >= 0)

m.c348 = Constraint(expr= - m.b8 + m.x203 >= 0)

m.c349 = Constraint(expr= - m.b9 + m.x204 >= 0)

m.c350 = Constraint(expr= - m.b10 + m.x205 >= 0)

m.c351 = Constraint(expr= - m.b11 + m.x206 >= 0)

m.c352 = Constraint(expr= - m.b12 + m.x207 >= 0)

m.c353 = Constraint(expr= - m.b13 + m.x208 >= 0)

m.c354 = Constraint(expr= - m.b14 + m.x209 >= 0)

m.c355 = Constraint(expr= - m.b15 + m.x175 >= 0)

m.c356 = Constraint(expr= - m.b16 + m.x176 >= 0)

m.c357 = Constraint(expr= - m.b17 + m.x177 >= 0)

m.c358 = Constraint(expr= - m.b18 + m.x178 >= 0)

m.c359 = Constraint(expr= - m.b19 + m.x179 >= 0)

m.c360 = Constraint(expr= - m.b20 + m.x180 >= 0)

m.c361 = Constraint(expr= - m.b21 + m.x181 >= 0)

m.c362 = Constraint(expr= - m.b22 + m.x182 >= 0)

m.c363 = Constraint(expr= - m.b23 + m.x183 >= 0)

m.c364 = Constraint(expr= - m.b24 + m.x184 >= 0)

m.c365 = Constraint(expr= - m.b25 + m.x185 >= 0)

m.c366 = Constraint(expr= - m.b26 + m.x186 >= 0)

m.c367 = Constraint(expr= - m.b27 + m.x187 >= 0)

m.c368 = Constraint(expr= - m.b28 + m.x188 >= 0)

m.c369 = Constraint(expr= - m.b29 + m.x210 >= 0)

m.c370 = Constraint(expr= - m.b30 + m.x211 >= 0)

m.c371 = Constraint(expr= - m.b31 + m.x212 >= 0)

m.c372 = Constraint(expr= - m.b32 + m.x213 >= 0)

m.c373 = Constraint(expr= - m.b33 + m.x214 >= 0)

m.c374 = Constraint(expr= - m.b34 + m.x215 >= 0)

m.c375 = Constraint(expr= - m.b35 + m.x216 >= 0)

m.c376 = Constraint(expr= - m.b36 + m.x217 >= 0)

m.c377 = Constraint(expr= - m.b37 + m.x218 >= 0)

m.c378 = Constraint(expr= - m.b38 + m.x219 >= 0)

m.c379 = Constraint(expr= - m.b39 + m.x220 >= 0)

m.c380 = Constraint(expr= - m.b40 + m.x221 >= 0)

m.c381 = Constraint(expr= - m.b41 + m.x222 >= 0)

m.c382 = Constraint(expr= - m.b42 + m.x223 >= 0)

m.c383 = Constraint(expr= - m.b43 + m.x189 + m.x224 + m.x238 >= 0)

m.c384 = Constraint(expr= - m.b44 + m.x190 + m.x225 + m.x239 >= 0)

m.c385 = Constraint(expr= - m.b45 + m.x191 + m.x226 + m.x240 >= 0)

m.c386 = Constraint(expr= - m.b46 + m.x192 + m.x227 + m.x241 >= 0)

m.c387 = Constraint(expr= - m.b47 + m.x193 + m.x228 + m.x242 >= 0)

m.c388 = Constraint(expr= - m.b48 + m.x194 + m.x229 + m.x243 >= 0)

m.c389 = Constraint(expr= - m.b49 + m.x195 + m.x230 + m.x244 >= 0)

m.c390 = Constraint(expr= - m.b50 + m.x196 + m.x231 + m.x245 >= 0)

m.c391 = Constraint(expr= - m.b51 + m.x197 + m.x232 + m.x246 >= 0)

m.c392 = Constraint(expr= - m.b52 + m.x198 + m.x233 + m.x247 >= 0)

m.c393 = Constraint(expr= - m.b53 + m.x199 + m.x234 + m.x248 >= 0)

m.c394 = Constraint(expr= - m.b54 + m.x200 + m.x235 + m.x249 >= 0)

m.c395 = Constraint(expr= - m.b55 + m.x201 + m.x236 + m.x250 >= 0)

m.c396 = Constraint(expr= - m.b56 + m.x202 + m.x237 + m.x251 >= 0)

m.c397 = Constraint(expr= - 0.002*m.x168 - m.x264 + m.x265 >= 0)

m.c398 = Constraint(expr= - 0.002*m.x169 - m.x265 + m.x266 >= 0)

m.c399 = Constraint(expr= - 0.002*m.x170 - m.x266 + m.x267 >= 0)

m.c400 = Constraint(expr= - 0.002*m.x171 - m.x267 + m.x268 >= 0)

m.c401 = Constraint(expr= - 0.002*m.x172 - m.x268 + m.x269 >= 0)

m.c402 = Constraint(expr= - 0.002*m.x173 - m.x269 + m.x270 >= 0)

m.c403 = Constraint(expr= - 0.002*m.x174 - m.x270 + m.x271 >= 0)

m.c404 = Constraint(expr= - 0.002*m.x203 - m.x264 + m.x265 >= 0)

m.c405 = Constraint(expr= - 0.002*m.x204 - m.x265 + m.x266 >= 0)

m.c406 = Constraint(expr= - 0.002*m.x205 - m.x266 + m.x267 >= 0)

m.c407 = Constraint(expr= - 0.002*m.x206 - m.x267 + m.x268 >= 0)

m.c408 = Constraint(expr= - 0.002*m.x207 - m.x268 + m.x269 >= 0)

m.c409 = Constraint(expr= - 0.002*m.x208 - m.x269 + m.x270 >= 0)

m.c410 = Constraint(expr= - 0.002*m.x209 - m.x270 + m.x271 >= 0)

m.c411 = Constraint(expr= - 0.002*m.x175 - m.x264 + m.x265 >= 0)

m.c412 = Constraint(expr= - 0.002*m.x176 - m.x265 + m.x266 >= 0)

m.c413 = Constraint(expr= - 0.002*m.x177 - m.x266 + m.x267 >= 0)

m.c414 = Constraint(expr= - 0.002*m.x178 - m.x267 + m.x268 >= 0)

m.c415 = Constraint(expr= - 0.002*m.x179 - m.x268 + m.x269 >= 0)

m.c416 = Constraint(expr= - 0.002*m.x180 - m.x269 + m.x270 >= 0)

m.c417 = Constraint(expr= - 0.002*m.x181 - m.x270 + m.x271 >= 0)

m.c418 = Constraint(expr= - 0.002*m.x182 - m.x264 + m.x265 >= 0)

m.c419 = Constraint(expr= - 0.002*m.x183 - m.x265 + m.x266 >= 0)

m.c420 = Constraint(expr= - 0.002*m.x184 - m.x266 + m.x267 >= 0)

m.c421 = Constraint(expr= - 0.002*m.x185 - m.x267 + m.x268 >= 0)

m.c422 = Constraint(expr= - 0.002*m.x186 - m.x268 + m.x269 >= 0)

m.c423 = Constraint(expr= - 0.002*m.x187 - m.x269 + m.x270 >= 0)

m.c424 = Constraint(expr= - 0.002*m.x188 - m.x270 + m.x271 >= 0)

m.c425 = Constraint(expr= - 0.002*m.x210 - m.x264 + m.x265 >= 0)

m.c426 = Constraint(expr= - 0.002*m.x211 - m.x265 + m.x266 >= 0)

m.c427 = Constraint(expr= - 0.002*m.x212 - m.x266 + m.x267 >= 0)

m.c428 = Constraint(expr= - 0.002*m.x213 - m.x267 + m.x268 >= 0)

m.c429 = Constraint(expr= - 0.002*m.x214 - m.x268 + m.x269 >= 0)

m.c430 = Constraint(expr= - 0.002*m.x215 - m.x269 + m.x270 >= 0)

m.c431 = Constraint(expr= - 0.002*m.x216 - m.x270 + m.x271 >= 0)

m.c432 = Constraint(expr= - 0.002*m.x217 - m.x264 + m.x265 >= 0)

m.c433 = Constraint(expr= - 0.002*m.x218 - m.x265 + m.x266 >= 0)

m.c434 = Constraint(expr= - 0.002*m.x219 - m.x266 + m.x267 >= 0)

m.c435 = Constraint(expr= - 0.002*m.x220 - m.x267 + m.x268 >= 0)

m.c436 = Constraint(expr= - 0.002*m.x221 - m.x268 + m.x269 >= 0)

m.c437 = Constraint(expr= - 0.002*m.x222 - m.x269 + m.x270 >= 0)

m.c438 = Constraint(expr= - 0.002*m.x223 - m.x270 + m.x271 >= 0)

m.c439 = Constraint(expr= - 0.002*m.x189 - 0.002*m.x196 - 0.002*m.x224 - 0.002*m.x231 - 0.002*m.x238 - 0.002*m.x245
                          - m.x264 + m.x265 >= 0)

m.c440 = Constraint(expr= - 0.002*m.x190 - 0.002*m.x197 - 0.002*m.x225 - 0.002*m.x232 - 0.002*m.x239 - 0.002*m.x246
                          - m.x265 + m.x266 >= 0)

m.c441 = Constraint(expr= - 0.002*m.x191 - 0.002*m.x198 - 0.002*m.x226 - 0.002*m.x233 - 0.002*m.x240 - 0.002*m.x247
                          - m.x266 + m.x267 >= 0)

m.c442 = Constraint(expr= - 0.002*m.x192 - 0.002*m.x199 - 0.002*m.x227 - 0.002*m.x234 - 0.002*m.x241 - 0.002*m.x248
                          - m.x267 + m.x268 >= 0)

m.c443 = Constraint(expr= - 0.002*m.x193 - 0.002*m.x200 - 0.002*m.x228 - 0.002*m.x235 - 0.002*m.x242 - 0.002*m.x249
                          - m.x268 + m.x269 >= 0)

m.c444 = Constraint(expr= - 0.002*m.x194 - 0.002*m.x201 - 0.002*m.x229 - 0.002*m.x236 - 0.002*m.x243 - 0.002*m.x250
                          - m.x269 + m.x270 >= 0)

m.c445 = Constraint(expr= - 0.002*m.x195 - 0.002*m.x202 - 0.002*m.x230 - 0.002*m.x237 - 0.002*m.x244 - 0.002*m.x251
                          - m.x270 + m.x271 >= 0)

m.c446 = Constraint(expr= - 0.02*m.x189 - 0.02*m.x196 - 0.02*m.x224 - 0.02*m.x231 - 0.02*m.x238 - 0.02*m.x245 - m.x264
                          + m.x265 <= 0)

m.c447 = Constraint(expr= - 0.02*m.x190 - 0.02*m.x197 - 0.02*m.x225 - 0.02*m.x232 - 0.02*m.x239 - 0.02*m.x246 - m.x265
                          + m.x266 <= 0)

m.c448 = Constraint(expr= - 0.02*m.x191 - 0.02*m.x198 - 0.02*m.x226 - 0.02*m.x233 - 0.02*m.x240 - 0.02*m.x247 - m.x266
                          + m.x267 <= 0)

m.c449 = Constraint(expr= - 0.02*m.x192 - 0.02*m.x199 - 0.02*m.x227 - 0.02*m.x234 - 0.02*m.x241 - 0.02*m.x248 - m.x267
                          + m.x268 <= 0)

m.c450 = Constraint(expr= - 0.02*m.x193 - 0.02*m.x200 - 0.02*m.x228 - 0.02*m.x235 - 0.02*m.x242 - 0.02*m.x249 - m.x268
                          + m.x269 <= 0)

m.c451 = Constraint(expr= - 0.02*m.x194 - 0.02*m.x201 - 0.02*m.x229 - 0.02*m.x236 - 0.02*m.x243 - 0.02*m.x250 - m.x269
                          + m.x270 <= 0)

m.c452 = Constraint(expr= - 0.02*m.x195 - 0.02*m.x202 - 0.02*m.x230 - 0.02*m.x237 - 0.02*m.x244 - 0.02*m.x251 - m.x270
                          + m.x271 <= 0)

m.c453 = Constraint(expr=   m.x264 >= 0)

m.c454 = Constraint(expr= - 4*m.b59 + m.x265 >= 0)

m.c455 = Constraint(expr= - 4*m.b61 + m.x266 >= 0)

m.c456 = Constraint(expr= - 4*m.b63 + m.x267 >= 0)

m.c457 = Constraint(expr= - 4*m.b65 + m.x268 >= 0)

m.c458 = Constraint(expr= - 4*m.b67 + m.x269 >= 0)

m.c459 = Constraint(expr= - 4*m.b68 + m.x270 >= 0)

m.c460 = Constraint(expr= - 2*m.b69 + m.x265 >= 0)

m.c461 = Constraint(expr= - 2*m.b70 - 6*m.b71 + m.x266 >= 0)

m.c462 = Constraint(expr= - 2*m.b72 - 6*m.b73 + m.x267 >= 0)

m.c463 = Constraint(expr= - 2*m.b74 - 6*m.b75 + m.x268 >= 0)

m.c464 = Constraint(expr= - 2*m.b76 - 6*m.b77 + m.x269 >= 0)

m.c465 = Constraint(expr= - 2*m.b78 - 6*m.b79 + m.x270 >= 0)

m.c466 = Constraint(expr= - 6*m.b80 + m.x271 >= 0)

m.c467 = Constraint(expr=   m.b57 + 2*m.b58 + 3*m.b60 + 4*m.b62 + 5*m.b64 + 6*m.b66 - 2*m.b69 - 3*m.b70 - 4*m.b72
                          - 5*m.b74 - 6*m.b76 - 7*m.b78 <= -1)

m.c468 = Constraint(expr=   2*m.b59 + 3*m.b61 + 4*m.b63 + 5*m.b65 + 6*m.b67 + 7*m.b68 - 3*m.b71 - 4*m.b73 - 5*m.b75
                          - 6*m.b77 - 7*m.b79 - 8*m.b80 <= -1)

m.c469 = Constraint(expr= - 2*m.b59 - 3*m.b61 - 4*m.b63 - 5*m.b65 - 6*m.b67 - 7*m.b68 + 2*m.b69 + 3*m.b70 + 4*m.b72
                          + 5*m.b74 + 6*m.b76 + 7*m.b78 <= 0)

m.c470 = Constraint(expr= - 8*m.b57 - m.x264 + m.x279 >= -8)

m.c471 = Constraint(expr= - 8*m.b58 - m.x265 + m.x279 >= -8)

m.c472 = Constraint(expr= - 8*m.b60 - m.x266 + m.x279 >= -8)

m.c473 = Constraint(expr= - 8*m.b62 - m.x267 + m.x279 >= -8)

m.c474 = Constraint(expr= - 8*m.b64 - m.x268 + m.x279 >= -8)

m.c475 = Constraint(expr= - 8*m.b66 - m.x269 + m.x279 >= -8)

m.c476 = Constraint(expr= - 4*m.b59 - m.x265 + m.x280 >= -8)

m.c477 = Constraint(expr= - 4*m.b61 - m.x266 + m.x280 >= -8)

m.c478 = Constraint(expr= - 4*m.b63 - m.x267 + m.x280 >= -8)

m.c479 = Constraint(expr= - 4*m.b65 - m.x268 + m.x280 >= -8)

m.c480 = Constraint(expr= - 4*m.b67 - m.x269 + m.x280 >= -8)

m.c481 = Constraint(expr= - 4*m.b68 - m.x270 + m.x280 >= -8)

m.c482 = Constraint(expr= - 6*m.b57 - 6*m.b69 + m.x264 - m.x265 + m.x281 >= -12)

m.c483 = Constraint(expr= - 6*m.b57 - 6*m.b70 + m.x264 - m.x266 + m.x281 >= -12)

m.c484 = Constraint(expr= - 6*m.b57 - 6*m.b72 + m.x264 - m.x267 + m.x281 >= -12)

m.c485 = Constraint(expr= - 6*m.b57 - 6*m.b74 + m.x264 - m.x268 + m.x281 >= -12)

m.c486 = Constraint(expr= - 6*m.b57 - 6*m.b76 + m.x264 - m.x269 + m.x281 >= -12)

m.c487 = Constraint(expr= - 6*m.b57 - 6*m.b78 + m.x264 - m.x270 + m.x281 >= -12)

m.c488 = Constraint(expr= - 6*m.b58 - 6*m.b70 + m.x265 - m.x266 + m.x281 >= -12)

m.c489 = Constraint(expr= - 6*m.b58 - 6*m.b72 + m.x265 - m.x267 + m.x281 >= -12)

m.c490 = Constraint(expr= - 6*m.b58 - 6*m.b74 + m.x265 - m.x268 + m.x281 >= -12)

m.c491 = Constraint(expr= - 6*m.b58 - 6*m.b76 + m.x265 - m.x269 + m.x281 >= -12)

m.c492 = Constraint(expr= - 6*m.b58 - 6*m.b78 + m.x265 - m.x270 + m.x281 >= -12)

m.c493 = Constraint(expr= - 6*m.b60 - 6*m.b72 + m.x266 - m.x267 + m.x281 >= -12)

m.c494 = Constraint(expr= - 6*m.b60 - 6*m.b74 + m.x266 - m.x268 + m.x281 >= -12)

m.c495 = Constraint(expr= - 6*m.b60 - 6*m.b76 + m.x266 - m.x269 + m.x281 >= -12)

m.c496 = Constraint(expr= - 6*m.b60 - 6*m.b78 + m.x266 - m.x270 + m.x281 >= -12)

m.c497 = Constraint(expr= - 6*m.b62 - 6*m.b74 + m.x267 - m.x268 + m.x281 >= -12)

m.c498 = Constraint(expr= - 6*m.b62 - 6*m.b76 + m.x267 - m.x269 + m.x281 >= -12)

m.c499 = Constraint(expr= - 6*m.b62 - 6*m.b78 + m.x267 - m.x270 + m.x281 >= -12)

m.c500 = Constraint(expr= - 6*m.b64 - 6*m.b76 + m.x268 - m.x269 + m.x281 >= -12)

m.c501 = Constraint(expr= - 6*m.b64 - 6*m.b78 + m.x268 - m.x270 + m.x281 >= -12)

m.c502 = Constraint(expr= - 6*m.b66 - 6*m.b78 + m.x269 - m.x270 + m.x281 >= -12)

m.c503 = Constraint(expr= - 6*m.b59 - 6*m.b71 + m.x265 - m.x266 + m.x282 >= -12)

m.c504 = Constraint(expr= - 6*m.b59 - 6*m.b73 + m.x265 - m.x267 + m.x282 >= -12)

m.c505 = Constraint(expr= - 6*m.b59 - 6*m.b75 + m.x265 - m.x268 + m.x282 >= -12)

m.c506 = Constraint(expr= - 6*m.b59 - 6*m.b77 + m.x265 - m.x269 + m.x282 >= -12)

m.c507 = Constraint(expr= - 6*m.b59 - 6*m.b79 + m.x265 - m.x270 + m.x282 >= -12)

m.c508 = Constraint(expr= - 6*m.b59 - 6*m.b80 + m.x265 - m.x271 + m.x282 >= -12)

m.c509 = Constraint(expr= - 6*m.b61 - 6*m.b73 + m.x266 - m.x267 + m.x282 >= -12)

m.c510 = Constraint(expr= - 6*m.b61 - 6*m.b75 + m.x266 - m.x268 + m.x282 >= -12)

m.c511 = Constraint(expr= - 6*m.b61 - 6*m.b77 + m.x266 - m.x269 + m.x282 >= -12)

m.c512 = Constraint(expr= - 6*m.b61 - 6*m.b79 + m.x266 - m.x270 + m.x282 >= -12)

m.c513 = Constraint(expr= - 6*m.b61 - 6*m.b80 + m.x266 - m.x271 + m.x282 >= -12)

m.c514 = Constraint(expr= - 6*m.b63 - 6*m.b75 + m.x267 - m.x268 + m.x282 >= -12)

m.c515 = Constraint(expr= - 6*m.b63 - 6*m.b77 + m.x267 - m.x269 + m.x282 >= -12)

m.c516 = Constraint(expr= - 6*m.b63 - 6*m.b79 + m.x267 - m.x270 + m.x282 >= -12)

m.c517 = Constraint(expr= - 6*m.b63 - 6*m.b80 + m.x267 - m.x271 + m.x282 >= -12)

m.c518 = Constraint(expr= - 6*m.b65 - 6*m.b77 + m.x268 - m.x269 + m.x282 >= -12)

m.c519 = Constraint(expr= - 6*m.b65 - 6*m.b79 + m.x268 - m.x270 + m.x282 >= -12)

m.c520 = Constraint(expr= - 6*m.b65 - 6*m.b80 + m.x268 - m.x271 + m.x282 >= -12)

m.c521 = Constraint(expr= - 6*m.b67 - 6*m.b79 + m.x269 - m.x270 + m.x282 >= -12)

m.c522 = Constraint(expr= - 6*m.b67 - 6*m.b80 + m.x269 - m.x271 + m.x282 >= -12)

m.c523 = Constraint(expr= - 6*m.b68 - 6*m.b80 + m.x270 - m.x271 + m.x282 >= -12)

m.c524 = Constraint(expr=   m.x264 - m.x265 + m.x272 == 0)

m.c525 = Constraint(expr=   m.x265 - m.x266 + m.x273 == 0)

m.c526 = Constraint(expr=   m.x266 - m.x267 + m.x274 == 0)

m.c527 = Constraint(expr=   m.x267 - m.x268 + m.x275 == 0)

m.c528 = Constraint(expr=   m.x268 - m.x269 + m.x276 == 0)

m.c529 = Constraint(expr=   m.x269 - m.x270 + m.x277 == 0)

m.c530 = Constraint(expr=   m.x270 - m.x271 + m.x278 == 0)

m.c531 = Constraint(expr=-m.x252*m.x105 + m.x190 == 0)

m.c532 = Constraint(expr=-m.x253*m.x106 + m.x191 == 0)

m.c533 = Constraint(expr=-m.x254*m.x107 + m.x192 == 0)

m.c534 = Constraint(expr=-m.x255*m.x108 + m.x193 == 0)

m.c535 = Constraint(expr=-m.x256*m.x109 + m.x194 == 0)

m.c536 = Constraint(expr=-m.x257*m.x110 + m.x195 == 0)

m.c537 = Constraint(expr=-m.x258*m.x113 + m.x197 == 0)

m.c538 = Constraint(expr=-m.x259*m.x114 + m.x198 == 0)

m.c539 = Constraint(expr=-m.x260*m.x115 + m.x199 == 0)

m.c540 = Constraint(expr=-m.x261*m.x116 + m.x200 == 0)

m.c541 = Constraint(expr=-m.x262*m.x117 + m.x201 == 0)

m.c542 = Constraint(expr=-m.x263*m.x118 + m.x202 == 0)

m.c543 = Constraint(expr=-m.x252*m.x137 + m.x225 == 0)

m.c544 = Constraint(expr=-m.x253*m.x138 + m.x226 == 0)

m.c545 = Constraint(expr=-m.x254*m.x139 + m.x227 == 0)

m.c546 = Constraint(expr=-m.x255*m.x140 + m.x228 == 0)

m.c547 = Constraint(expr=-m.x256*m.x141 + m.x229 == 0)

m.c548 = Constraint(expr=-m.x257*m.x142 + m.x230 == 0)

m.c549 = Constraint(expr=-m.x258*m.x145 + m.x232 == 0)

m.c550 = Constraint(expr=-m.x259*m.x146 + m.x233 == 0)

m.c551 = Constraint(expr=-m.x260*m.x147 + m.x234 == 0)

m.c552 = Constraint(expr=-m.x261*m.x148 + m.x235 == 0)

m.c553 = Constraint(expr=-m.x262*m.x149 + m.x236 == 0)

m.c554 = Constraint(expr=-m.x263*m.x150 + m.x237 == 0)

m.c555 = Constraint(expr=-m.x252*m.x153 + m.x239 == 0)

m.c556 = Constraint(expr=-m.x253*m.x154 + m.x240 == 0)

m.c557 = Constraint(expr=-m.x254*m.x155 + m.x241 == 0)

m.c558 = Constraint(expr=-m.x255*m.x156 + m.x242 == 0)

m.c559 = Constraint(expr=-m.x256*m.x157 + m.x243 == 0)

m.c560 = Constraint(expr=-m.x257*m.x158 + m.x244 == 0)

m.c561 = Constraint(expr=-m.x258*m.x161 + m.x246 == 0)

m.c562 = Constraint(expr=-m.x259*m.x162 + m.x247 == 0)

m.c563 = Constraint(expr=-m.x260*m.x163 + m.x248 == 0)

m.c564 = Constraint(expr=-m.x261*m.x164 + m.x249 == 0)

m.c565 = Constraint(expr=-m.x262*m.x165 + m.x250 == 0)

m.c566 = Constraint(expr=-m.x263*m.x166 + m.x251 == 0)
