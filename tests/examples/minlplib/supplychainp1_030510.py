#  MINLP written by GAMS Convert at 04/21/18 13:54:26
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        836      121      165      550        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        446      376       70        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2331     2316       15        0
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
m.x71 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,14),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,13),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,14),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,13),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,14),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,13),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,13),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,14),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x235 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,109669.003926881),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,99699.094478983),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,109669.003926881),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,69789.3661352881),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,99699.094478983),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x255 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x258 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x262 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x263 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x264 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x265 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x266 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x267 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x268 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x269 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x270 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x271 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x272 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x273 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x274 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x275 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x276 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x277 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x278 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x279 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x280 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x281 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x282 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x283 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x284 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x285 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x286 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x287 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x289 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x290 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x291 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x292 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x293 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x294 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x295 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x296 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x297 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x298 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x299 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x300 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x301 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x302 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x303 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x304 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x305 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x306 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x307 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x309 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x311 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x312 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x313 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x314 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x315 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x316 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x317 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x318 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x319 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x320 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x321 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x322 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x323 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x324 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x325 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x326 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x327 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x328 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x329 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x330 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x331 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x332 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x333 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x334 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x335 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x336 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x337 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x338 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x339 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x340 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x341 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x342 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x343 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x344 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x345 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x346 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x347 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x348 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x349 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x350 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x351 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x352 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x353 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x354 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x355 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x356 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x357 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x358 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x359 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x360 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x361 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x362 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x363 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x364 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x365 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x366 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x367 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x368 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x369 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x370 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x371 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x372 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x373 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x374 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x375 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x376 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x377 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x378 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x379 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x380 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x381 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x382 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x383 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x384 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x385 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x386 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x387 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x388 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x389 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x390 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x391 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x392 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x393 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x394 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x395 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x396 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x397 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x398 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x399 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x400 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x401 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x402 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x403 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x404 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x405 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x406 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x407 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x408 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x409 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x410 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x411 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x412 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x413 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x414 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x415 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x416 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x417 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x418 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x419 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x420 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x421 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x422 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x423 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x424 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x425 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x426 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x427 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x428 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x429 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x430 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x431 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x432 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x433 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x434 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x435 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x436 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x437 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x438 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x439 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x440 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x441 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x442 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x443 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x444 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x445 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x446 = Var(within=Reals,bounds=(0,10),initialize=0)

m.obj = Objective(expr=88.85300006996*sqrt(1e-6 + m.x242) + 192.23073994166*sqrt(1e-6 + m.x243) + 127.63233374696*sqrt(
                       1e-6 + m.x244) + 419.48235478268*sqrt(1e-6 + m.x245) + 153.22284111554*sqrt(1e-6 + m.x246) + 
                       11812.8060023653*sqrt(1e-6 + m.x81) + 1350.11753695442*sqrt(1e-6 + m.x82) + 13367.9894872554*
                       sqrt(1e-6 + m.x83) + 22271.0227712868*sqrt(1e-6 + m.x84) + 3005.94387692899*sqrt(1e-6 + m.x85) + 
                       8081.13134168897*sqrt(1e-6 + m.x86) + 2725.40259637536*sqrt(1e-6 + m.x87) + 17834.6321864598*
                       sqrt(1e-6 + m.x88) + 11090.3708869987*sqrt(1e-6 + m.x89) + 34135.3450147183*sqrt(1e-6 + m.x90)
                        + 151717.47132*m.b16 + 158432.66708*m.b17 + 155503.75356*m.b18 + 153011.37904*m.b19
                        + 152922.12117*m.b20 + 31172.917964017*m.b21 + 50366.2988612629*m.b22 + 25232.3015865842*m.b23
                        + 13875.2777716691*m.b24 + 12894.0919466219*m.b25 + 104246.200740246*m.b26
                        + 23030.4692996671*m.b27 + 34080.9619919892*m.b28 + 23691.1338892398*m.b29
                        + 71485.9325093983*m.b30 + 20595.4230163802*m.b31 + 100964.014716159*m.b32
                        + 47584.642753328*m.b33 + 8366.15399075336*m.b34 + 12512.1539989574*m.b35
                        + 35986.4763418661*m.b36 + 46834.267934517*m.b37 + 35500.2352632821*m.b38
                        + 24409.7766590388*m.b39 + 48282.6225705813*m.b40 + 31041.4817687302*m.b41
                        + 53037.2328896265*m.b42 + 51459.7461120258*m.b43 + 22667.2580628975*m.b44
                        + 25228.9882448255*m.b45 + 37408.8375498868*m.b46 + 25200.7856772603*m.b47
                        + 36902.8071939517*m.b48 + 26504.6681149691*m.b49 + 49522.8366523017*m.b50
                        + 9271.93442865272*m.b51 + 144904.131180845*m.b52 + 24247.3790621604*m.b53
                        + 7667.40116108732*m.b54 + 22073.8762813933*m.b55 + 107488.43411253*m.b56
                        + 23226.4417178111*m.b57 + 34704.48655633*m.b58 + 25058.2307095212*m.b59
                        + 47407.2067673463*m.b60 + 21614.5566697948*m.b61 + 101949.658248026*m.b62
                        + 25381.2261639692*m.b63 + 8426.19414871674*m.b64 + 13579.8855675766*m.b65
                        + 107491.687838232*m.b66 + 43784.7477537411*m.b67 + 107221.380878763*m.b68
                        + 13362.229690641*m.b69 + 25676.6925875457*m.b70 + 102990.619769066*m.x92
                        + 112014.257406774*m.x93 + 69629.7741612624*m.x94 + 75188.2830958459*m.x95
                        + 69397.1006878894*m.x96 + 72244.2291996906*m.x97 + 95437.7441707133*m.x98
                        + 100567.408588663*m.x99 + 62917.1664376185*m.x100 + 66679.7204984856*m.x101
                        + 14622.9462763914*m.x102 + 15904.1519695865*m.x103 + 9886.26390520296*m.x104
                        + 10675.4792503432*m.x105 + 9853.2281616692*m.x106 + 10257.4728138851*m.x107
                        + 13550.5642055325*m.x108 + 14278.8907984572*m.x109 + 8933.18582549597*m.x110
                        + 9467.40560218483*m.x111 + 44327.8411949159*m.x112 + 48211.6742770128*m.x113
                        + 29969.1134821712*m.x114 + 32361.5323440562*m.x115 + 29868.9692865049*m.x116
                        + 31094.3921533217*m.x117 + 41077.0337831393*m.x118 + 43284.8751400703*m.x119
                        + 27079.9628988982*m.x120 + 28699.3909523596*m.x121 + 30184.9172999892*m.x122
                        + 32829.6023834465*m.x123 + 20407.3825304419*m.x124 + 22036.4933453672*m.x125
                        + 20339.1896254238*m.x126 + 21173.6378389006*m.x127 + 27971.289245079*m.x128
                        + 29474.7125333329*m.x129 + 18440.0236635879*m.x130 + 19542.7685875302*m.x131
                        + 21271.6426284951*m.x132 + 23135.381243417*m.x133 + 14381.3065265781*m.x134
                        + 15529.3588042406*m.x135 + 14333.2502377062*m.x136 + 14921.2950553433*m.x137
                        + 19711.6746342652*m.x138 + 20771.1535319299*m.x139 + 12994.8871330178*m.x140
                        + 13772.0035882117*m.x141 + 82797.4459378645*m.x142 + 90051.8362031746*m.x143
                        + 55977.5975201425*m.x144 + 60446.2602395074*m.x145 + 55790.5438896666*m.x146
                        + 58079.4413597721*m.x147 + 76725.4482119329*m.x148 + 80849.3491388033*m.x149
                        + 50581.1179538799*m.x150 + 53605.9552365516*m.x151 + 59289.988870794*m.x152
                        + 64484.7471537658*m.x153 + 40084.704260971*m.x154 + 43284.6455139573*m.x155
                        + 39950.7580076351*m.x156 + 41589.8025939957*m.x157 + 54941.9238608643*m.x158
                        + 57894.9864497985*m.x159 + 36220.3675075729*m.x160 + 38386.4073750364*m.x161
                        + 26393.5425520846*m.x162 + 28706.0421224286*m.x163 + 17844.1144575897*m.x164
                        + 19268.6009051908*m.x165 + 17784.4869183635*m.x166 + 18514.1243134581*m.x167
                        + 24457.9571177729*m.x168 + 25772.5430130386*m.x169 + 16123.8655845689*m.x170
                        + 17088.1002977174*m.x171 + 47652.7133364267*m.x172 + 51827.8587872032*m.x173
                        + 32216.9890347951*m.x174 + 34788.8546418922*m.x175 + 32109.3333827319*m.x176
                        + 33426.6708170444*m.x177 + 44158.0745376599*m.x178 + 46531.5181441627*m.x179
                        + 29111.1336441592*m.x180 + 30852.0291788918*m.x181 + 10750.8361993864*m.x182
                        + 11692.7826638619*m.x183 + 7268.41238829826*m.x184 + 7848.64599794667*m.x185
                        + 7244.12440551125*m.x186 + 7541.32634815041*m.x187 + 9962.41752034251*m.x188
                        + 10497.8855274179*m.x189 + 6567.70637963992*m.x190 + 6960.46644352166*m.x191
                        + 32254.3444976195*m.x192 + 35080.344745418*m.x193 + 21806.4783775906*m.x194
                        + 23547.2782919047*m.x195 + 21733.6102816178*m.x196 + 22625.266862135*m.x197
                        + 29888.9538237582*m.x198 + 31495.4492858181*m.x199 + 19704.2406934086*m.x200
                        + 20882.5879559287*m.x201 + 83994.6601779029*m.x202 + 91353.9456997037*m.x203
                        + 56787.0086815031*m.x204 + 61320.2862761332*m.x205 + 56597.2503387317*m.x206
                        + 58919.2442481556*m.x207 + 77834.864065673*m.x208 + 82018.3947656389*m.x209
                        + 51312.4984210611*m.x210 + 54381.0735053956*m.x211 + 64744.0715040064*m.x212
                        + 70416.6952997655*m.x213 + 43772.0938781904*m.x214 + 47266.3975412161*m.x215
                        + 43625.8259167885*m.x216 + 45415.6461194679*m.x217 + 59996.0282463086*m.x218
                        + 63220.7428913123*m.x219 + 39552.277011252*m.x220 + 41917.57076034*m.x221
                        + 31959.4592631882*m.x222 + 34759.6228133711*m.x223 + 21607.1127234856*m.x224
                        + 23331.9973805274*m.x225 + 21534.9108238314*m.x226 + 22418.4154371059*m.x227
                        + 29615.6941654856*m.x228 + 31207.5022482693*m.x229 + 19524.0947401527*m.x230
                        + 20691.6689668489*m.x231 + 54434.9183185422*m.x232 + 59204.2941980751*m.x233
                        + 36802.2940099374*m.x234 + 39740.2021466726*m.x235 + 36679.3161936436*m.x236
                        + 38184.1445783043*m.x237 + 50442.9026651909*m.x238 + 53154.1482545346*m.x239
                        + 33254.3956288975*m.x240 + 35243.0653099971*m.x241, sense=minimize)

m.c2 = Constraint(expr=   m.b1 + m.b6 + m.b11 - m.b16 == 0)

m.c3 = Constraint(expr=   m.b2 + m.b7 + m.b12 - m.b17 == 0)

m.c4 = Constraint(expr=   m.b3 + m.b8 + m.b13 - m.b18 == 0)

m.c5 = Constraint(expr=   m.b4 + m.b9 + m.b14 - m.b19 == 0)

m.c6 = Constraint(expr=   m.b5 + m.b10 + m.b15 - m.b20 == 0)

m.c7 = Constraint(expr= - m.b16 + m.b21 <= 0)

m.c8 = Constraint(expr= - m.b16 + m.b22 <= 0)

m.c9 = Constraint(expr= - m.b16 + m.b23 <= 0)

m.c10 = Constraint(expr= - m.b16 + m.b24 <= 0)

m.c11 = Constraint(expr= - m.b16 + m.b25 <= 0)

m.c12 = Constraint(expr= - m.b16 + m.b26 <= 0)

m.c13 = Constraint(expr= - m.b16 + m.b27 <= 0)

m.c14 = Constraint(expr= - m.b16 + m.b28 <= 0)

m.c15 = Constraint(expr= - m.b16 + m.b29 <= 0)

m.c16 = Constraint(expr= - m.b16 + m.b30 <= 0)

m.c17 = Constraint(expr= - m.b17 + m.b31 <= 0)

m.c18 = Constraint(expr= - m.b17 + m.b32 <= 0)

m.c19 = Constraint(expr= - m.b17 + m.b33 <= 0)

m.c20 = Constraint(expr= - m.b17 + m.b34 <= 0)

m.c21 = Constraint(expr= - m.b17 + m.b35 <= 0)

m.c22 = Constraint(expr= - m.b17 + m.b36 <= 0)

m.c23 = Constraint(expr= - m.b17 + m.b37 <= 0)

m.c24 = Constraint(expr= - m.b17 + m.b38 <= 0)

m.c25 = Constraint(expr= - m.b17 + m.b39 <= 0)

m.c26 = Constraint(expr= - m.b17 + m.b40 <= 0)

m.c27 = Constraint(expr= - m.b18 + m.b41 <= 0)

m.c28 = Constraint(expr= - m.b18 + m.b42 <= 0)

m.c29 = Constraint(expr= - m.b18 + m.b43 <= 0)

m.c30 = Constraint(expr= - m.b18 + m.b44 <= 0)

m.c31 = Constraint(expr= - m.b18 + m.b45 <= 0)

m.c32 = Constraint(expr= - m.b18 + m.b46 <= 0)

m.c33 = Constraint(expr= - m.b18 + m.b47 <= 0)

m.c34 = Constraint(expr= - m.b18 + m.b48 <= 0)

m.c35 = Constraint(expr= - m.b18 + m.b49 <= 0)

m.c36 = Constraint(expr= - m.b18 + m.b50 <= 0)

m.c37 = Constraint(expr= - m.b19 + m.b51 <= 0)

m.c38 = Constraint(expr= - m.b19 + m.b52 <= 0)

m.c39 = Constraint(expr= - m.b19 + m.b53 <= 0)

m.c40 = Constraint(expr= - m.b19 + m.b54 <= 0)

m.c41 = Constraint(expr= - m.b19 + m.b55 <= 0)

m.c42 = Constraint(expr= - m.b19 + m.b56 <= 0)

m.c43 = Constraint(expr= - m.b19 + m.b57 <= 0)

m.c44 = Constraint(expr= - m.b19 + m.b58 <= 0)

m.c45 = Constraint(expr= - m.b19 + m.b59 <= 0)

m.c46 = Constraint(expr= - m.b19 + m.b60 <= 0)

m.c47 = Constraint(expr= - m.b20 + m.b61 <= 0)

m.c48 = Constraint(expr= - m.b20 + m.b62 <= 0)

m.c49 = Constraint(expr= - m.b20 + m.b63 <= 0)

m.c50 = Constraint(expr= - m.b20 + m.b64 <= 0)

m.c51 = Constraint(expr= - m.b20 + m.b65 <= 0)

m.c52 = Constraint(expr= - m.b20 + m.b66 <= 0)

m.c53 = Constraint(expr= - m.b20 + m.b67 <= 0)

m.c54 = Constraint(expr= - m.b20 + m.b68 <= 0)

m.c55 = Constraint(expr= - m.b20 + m.b69 <= 0)

m.c56 = Constraint(expr= - m.b20 + m.b70 <= 0)

m.c57 = Constraint(expr=   m.b21 + m.b31 + m.b41 + m.b51 + m.b61 == 1)

m.c58 = Constraint(expr=   m.b22 + m.b32 + m.b42 + m.b52 + m.b62 == 1)

m.c59 = Constraint(expr=   m.b23 + m.b33 + m.b43 + m.b53 + m.b63 == 1)

m.c60 = Constraint(expr=   m.b24 + m.b34 + m.b44 + m.b54 + m.b64 == 1)

m.c61 = Constraint(expr=   m.b25 + m.b35 + m.b45 + m.b55 + m.b65 == 1)

m.c62 = Constraint(expr=   m.b26 + m.b36 + m.b46 + m.b56 + m.b66 == 1)

m.c63 = Constraint(expr=   m.b27 + m.b37 + m.b47 + m.b57 + m.b67 == 1)

m.c64 = Constraint(expr=   m.b28 + m.b38 + m.b48 + m.b58 + m.b68 == 1)

m.c65 = Constraint(expr=   m.b29 + m.b39 + m.b49 + m.b59 + m.b69 == 1)

m.c66 = Constraint(expr=   m.b30 + m.b40 + m.b50 + m.b60 + m.b70 == 1)

m.c67 = Constraint(expr= - 11*m.b1 - 8*m.b6 - 7*m.b11 + m.x71 + m.x76 >= 0)

m.c68 = Constraint(expr= - 6*m.b2 - 7*m.b7 - 10*m.b12 + m.x72 + m.x77 >= 0)

m.c69 = Constraint(expr= - 10*m.b3 - 6*m.b8 - 11*m.b13 + m.x73 + m.x78 >= 0)

m.c70 = Constraint(expr= - 7*m.b4 - 6*m.b9 - 7*m.b14 + m.x74 + m.x79 >= 0)

m.c71 = Constraint(expr= - 7*m.b5 - 4*m.b10 - 10*m.b15 + m.x75 + m.x80 >= 0)

m.c72 = Constraint(expr= - 3*m.b21 - 2*m.b31 - 3*m.b41 - m.b51 - 2*m.b61 + m.x81 - m.x347 - m.x357 - m.x367 - m.x377
                         - m.x387 >= 0)

m.c73 = Constraint(expr= - m.b22 - 2*m.b32 - m.b42 - 3*m.b52 - 2*m.b62 + m.x82 - m.x348 - m.x358 - m.x368 - m.x378
                         - m.x388 >= 0)

m.c74 = Constraint(expr= - m.b23 - 2*m.b33 - 2*m.b43 - m.b53 - m.b63 + m.x83 - m.x349 - m.x359 - m.x369 - m.x379
                         - m.x389 >= 0)

m.c75 = Constraint(expr= - 2*m.b24 - m.b34 - 3*m.b44 - m.b54 - m.b64 + m.x84 - m.x350 - m.x360 - m.x370 - m.x380
                         - m.x390 >= 0)

m.c76 = Constraint(expr= - m.b25 - m.b35 - 2*m.b45 - 2*m.b55 - m.b65 + m.x85 - m.x351 - m.x361 - m.x371 - m.x381
                         - m.x391 >= 0)

m.c77 = Constraint(expr= - 3*m.b26 - m.b36 - m.b46 - 3*m.b56 - 3*m.b66 + m.x86 - m.x352 - m.x362 - m.x372 - m.x382
                         - m.x392 >= 0)

m.c78 = Constraint(expr= - m.b27 - 2*m.b37 - m.b47 - m.b57 - 2*m.b67 + m.x87 - m.x353 - m.x363 - m.x373 - m.x383
                         - m.x393 >= 0)

m.c79 = Constraint(expr= - m.b28 - m.b38 - m.b48 - m.b58 - 3*m.b68 + m.x88 - m.x354 - m.x364 - m.x374 - m.x384 - m.x394
                         >= 0)

m.c80 = Constraint(expr= - 2*m.b29 - 2*m.b39 - 2*m.b49 - 2*m.b59 - m.b69 + m.x89 - m.x355 - m.x365 - m.x375 - m.x385
                         - m.x395 >= 0)

m.c81 = Constraint(expr= - 3*m.b30 - 2*m.b40 - 2*m.b50 - 2*m.b60 - m.b70 + m.x90 - m.x356 - m.x366 - m.x376 - m.x386
                         - m.x396 >= 0)

m.c82 = Constraint(expr= - m.b1 + m.x92 <= 0)

m.c83 = Constraint(expr= - m.b1 + m.x93 <= 0)

m.c84 = Constraint(expr= - m.b1 + m.x94 <= 0)

m.c85 = Constraint(expr= - m.b1 + m.x95 <= 0)

m.c86 = Constraint(expr= - m.b1 + m.x96 <= 0)

m.c87 = Constraint(expr= - m.b1 + m.x97 <= 0)

m.c88 = Constraint(expr= - m.b1 + m.x98 <= 0)

m.c89 = Constraint(expr= - m.b1 + m.x99 <= 0)

m.c90 = Constraint(expr= - m.b1 + m.x100 <= 0)

m.c91 = Constraint(expr= - m.b1 + m.x101 <= 0)

m.c92 = Constraint(expr= - m.b2 + m.x102 <= 0)

m.c93 = Constraint(expr= - m.b2 + m.x103 <= 0)

m.c94 = Constraint(expr= - m.b2 + m.x104 <= 0)

m.c95 = Constraint(expr= - m.b2 + m.x105 <= 0)

m.c96 = Constraint(expr= - m.b2 + m.x106 <= 0)

m.c97 = Constraint(expr= - m.b2 + m.x107 <= 0)

m.c98 = Constraint(expr= - m.b2 + m.x108 <= 0)

m.c99 = Constraint(expr= - m.b2 + m.x109 <= 0)

m.c100 = Constraint(expr= - m.b2 + m.x110 <= 0)

m.c101 = Constraint(expr= - m.b2 + m.x111 <= 0)

m.c102 = Constraint(expr= - m.b3 + m.x112 <= 0)

m.c103 = Constraint(expr= - m.b3 + m.x113 <= 0)

m.c104 = Constraint(expr= - m.b3 + m.x114 <= 0)

m.c105 = Constraint(expr= - m.b3 + m.x115 <= 0)

m.c106 = Constraint(expr= - m.b3 + m.x116 <= 0)

m.c107 = Constraint(expr= - m.b3 + m.x117 <= 0)

m.c108 = Constraint(expr= - m.b3 + m.x118 <= 0)

m.c109 = Constraint(expr= - m.b3 + m.x119 <= 0)

m.c110 = Constraint(expr= - m.b3 + m.x120 <= 0)

m.c111 = Constraint(expr= - m.b3 + m.x121 <= 0)

m.c112 = Constraint(expr= - m.b4 + m.x122 <= 0)

m.c113 = Constraint(expr= - m.b4 + m.x123 <= 0)

m.c114 = Constraint(expr= - m.b4 + m.x124 <= 0)

m.c115 = Constraint(expr= - m.b4 + m.x125 <= 0)

m.c116 = Constraint(expr= - m.b4 + m.x126 <= 0)

m.c117 = Constraint(expr= - m.b4 + m.x127 <= 0)

m.c118 = Constraint(expr= - m.b4 + m.x128 <= 0)

m.c119 = Constraint(expr= - m.b4 + m.x129 <= 0)

m.c120 = Constraint(expr= - m.b4 + m.x130 <= 0)

m.c121 = Constraint(expr= - m.b4 + m.x131 <= 0)

m.c122 = Constraint(expr= - m.b5 + m.x132 <= 0)

m.c123 = Constraint(expr= - m.b5 + m.x133 <= 0)

m.c124 = Constraint(expr= - m.b5 + m.x134 <= 0)

m.c125 = Constraint(expr= - m.b5 + m.x135 <= 0)

m.c126 = Constraint(expr= - m.b5 + m.x136 <= 0)

m.c127 = Constraint(expr= - m.b5 + m.x137 <= 0)

m.c128 = Constraint(expr= - m.b5 + m.x138 <= 0)

m.c129 = Constraint(expr= - m.b5 + m.x139 <= 0)

m.c130 = Constraint(expr= - m.b5 + m.x140 <= 0)

m.c131 = Constraint(expr= - m.b5 + m.x141 <= 0)

m.c132 = Constraint(expr= - m.b6 + m.x142 <= 0)

m.c133 = Constraint(expr= - m.b6 + m.x143 <= 0)

m.c134 = Constraint(expr= - m.b6 + m.x144 <= 0)

m.c135 = Constraint(expr= - m.b6 + m.x145 <= 0)

m.c136 = Constraint(expr= - m.b6 + m.x146 <= 0)

m.c137 = Constraint(expr= - m.b6 + m.x147 <= 0)

m.c138 = Constraint(expr= - m.b6 + m.x148 <= 0)

m.c139 = Constraint(expr= - m.b6 + m.x149 <= 0)

m.c140 = Constraint(expr= - m.b6 + m.x150 <= 0)

m.c141 = Constraint(expr= - m.b6 + m.x151 <= 0)

m.c142 = Constraint(expr= - m.b7 + m.x152 <= 0)

m.c143 = Constraint(expr= - m.b7 + m.x153 <= 0)

m.c144 = Constraint(expr= - m.b7 + m.x154 <= 0)

m.c145 = Constraint(expr= - m.b7 + m.x155 <= 0)

m.c146 = Constraint(expr= - m.b7 + m.x156 <= 0)

m.c147 = Constraint(expr= - m.b7 + m.x157 <= 0)

m.c148 = Constraint(expr= - m.b7 + m.x158 <= 0)

m.c149 = Constraint(expr= - m.b7 + m.x159 <= 0)

m.c150 = Constraint(expr= - m.b7 + m.x160 <= 0)

m.c151 = Constraint(expr= - m.b7 + m.x161 <= 0)

m.c152 = Constraint(expr= - m.b8 + m.x162 <= 0)

m.c153 = Constraint(expr= - m.b8 + m.x163 <= 0)

m.c154 = Constraint(expr= - m.b8 + m.x164 <= 0)

m.c155 = Constraint(expr= - m.b8 + m.x165 <= 0)

m.c156 = Constraint(expr= - m.b8 + m.x166 <= 0)

m.c157 = Constraint(expr= - m.b8 + m.x167 <= 0)

m.c158 = Constraint(expr= - m.b8 + m.x168 <= 0)

m.c159 = Constraint(expr= - m.b8 + m.x169 <= 0)

m.c160 = Constraint(expr= - m.b8 + m.x170 <= 0)

m.c161 = Constraint(expr= - m.b8 + m.x171 <= 0)

m.c162 = Constraint(expr= - m.b9 + m.x172 <= 0)

m.c163 = Constraint(expr= - m.b9 + m.x173 <= 0)

m.c164 = Constraint(expr= - m.b9 + m.x174 <= 0)

m.c165 = Constraint(expr= - m.b9 + m.x175 <= 0)

m.c166 = Constraint(expr= - m.b9 + m.x176 <= 0)

m.c167 = Constraint(expr= - m.b9 + m.x177 <= 0)

m.c168 = Constraint(expr= - m.b9 + m.x178 <= 0)

m.c169 = Constraint(expr= - m.b9 + m.x179 <= 0)

m.c170 = Constraint(expr= - m.b9 + m.x180 <= 0)

m.c171 = Constraint(expr= - m.b9 + m.x181 <= 0)

m.c172 = Constraint(expr= - m.b10 + m.x182 <= 0)

m.c173 = Constraint(expr= - m.b10 + m.x183 <= 0)

m.c174 = Constraint(expr= - m.b10 + m.x184 <= 0)

m.c175 = Constraint(expr= - m.b10 + m.x185 <= 0)

m.c176 = Constraint(expr= - m.b10 + m.x186 <= 0)

m.c177 = Constraint(expr= - m.b10 + m.x187 <= 0)

m.c178 = Constraint(expr= - m.b10 + m.x188 <= 0)

m.c179 = Constraint(expr= - m.b10 + m.x189 <= 0)

m.c180 = Constraint(expr= - m.b10 + m.x190 <= 0)

m.c181 = Constraint(expr= - m.b10 + m.x191 <= 0)

m.c182 = Constraint(expr= - m.b11 + m.x192 <= 0)

m.c183 = Constraint(expr= - m.b11 + m.x193 <= 0)

m.c184 = Constraint(expr= - m.b11 + m.x194 <= 0)

m.c185 = Constraint(expr= - m.b11 + m.x195 <= 0)

m.c186 = Constraint(expr= - m.b11 + m.x196 <= 0)

m.c187 = Constraint(expr= - m.b11 + m.x197 <= 0)

m.c188 = Constraint(expr= - m.b11 + m.x198 <= 0)

m.c189 = Constraint(expr= - m.b11 + m.x199 <= 0)

m.c190 = Constraint(expr= - m.b11 + m.x200 <= 0)

m.c191 = Constraint(expr= - m.b11 + m.x201 <= 0)

m.c192 = Constraint(expr= - m.b12 + m.x202 <= 0)

m.c193 = Constraint(expr= - m.b12 + m.x203 <= 0)

m.c194 = Constraint(expr= - m.b12 + m.x204 <= 0)

m.c195 = Constraint(expr= - m.b12 + m.x205 <= 0)

m.c196 = Constraint(expr= - m.b12 + m.x206 <= 0)

m.c197 = Constraint(expr= - m.b12 + m.x207 <= 0)

m.c198 = Constraint(expr= - m.b12 + m.x208 <= 0)

m.c199 = Constraint(expr= - m.b12 + m.x209 <= 0)

m.c200 = Constraint(expr= - m.b12 + m.x210 <= 0)

m.c201 = Constraint(expr= - m.b12 + m.x211 <= 0)

m.c202 = Constraint(expr= - m.b13 + m.x212 <= 0)

m.c203 = Constraint(expr= - m.b13 + m.x213 <= 0)

m.c204 = Constraint(expr= - m.b13 + m.x214 <= 0)

m.c205 = Constraint(expr= - m.b13 + m.x215 <= 0)

m.c206 = Constraint(expr= - m.b13 + m.x216 <= 0)

m.c207 = Constraint(expr= - m.b13 + m.x217 <= 0)

m.c208 = Constraint(expr= - m.b13 + m.x218 <= 0)

m.c209 = Constraint(expr= - m.b13 + m.x219 <= 0)

m.c210 = Constraint(expr= - m.b13 + m.x220 <= 0)

m.c211 = Constraint(expr= - m.b13 + m.x221 <= 0)

m.c212 = Constraint(expr= - m.b14 + m.x222 <= 0)

m.c213 = Constraint(expr= - m.b14 + m.x223 <= 0)

m.c214 = Constraint(expr= - m.b14 + m.x224 <= 0)

m.c215 = Constraint(expr= - m.b14 + m.x225 <= 0)

m.c216 = Constraint(expr= - m.b14 + m.x226 <= 0)

m.c217 = Constraint(expr= - m.b14 + m.x227 <= 0)

m.c218 = Constraint(expr= - m.b14 + m.x228 <= 0)

m.c219 = Constraint(expr= - m.b14 + m.x229 <= 0)

m.c220 = Constraint(expr= - m.b14 + m.x230 <= 0)

m.c221 = Constraint(expr= - m.b14 + m.x231 <= 0)

m.c222 = Constraint(expr= - m.b15 + m.x232 <= 0)

m.c223 = Constraint(expr= - m.b15 + m.x233 <= 0)

m.c224 = Constraint(expr= - m.b15 + m.x234 <= 0)

m.c225 = Constraint(expr= - m.b15 + m.x235 <= 0)

m.c226 = Constraint(expr= - m.b15 + m.x236 <= 0)

m.c227 = Constraint(expr= - m.b15 + m.x237 <= 0)

m.c228 = Constraint(expr= - m.b15 + m.x238 <= 0)

m.c229 = Constraint(expr= - m.b15 + m.x239 <= 0)

m.c230 = Constraint(expr= - m.b15 + m.x240 <= 0)

m.c231 = Constraint(expr= - m.b15 + m.x241 <= 0)

m.c232 = Constraint(expr= - m.b21 + m.x92 <= 0)

m.c233 = Constraint(expr= - m.b22 + m.x93 <= 0)

m.c234 = Constraint(expr= - m.b23 + m.x94 <= 0)

m.c235 = Constraint(expr= - m.b24 + m.x95 <= 0)

m.c236 = Constraint(expr= - m.b25 + m.x96 <= 0)

m.c237 = Constraint(expr= - m.b26 + m.x97 <= 0)

m.c238 = Constraint(expr= - m.b27 + m.x98 <= 0)

m.c239 = Constraint(expr= - m.b28 + m.x99 <= 0)

m.c240 = Constraint(expr= - m.b29 + m.x100 <= 0)

m.c241 = Constraint(expr= - m.b30 + m.x101 <= 0)

m.c242 = Constraint(expr= - m.b31 + m.x102 <= 0)

m.c243 = Constraint(expr= - m.b32 + m.x103 <= 0)

m.c244 = Constraint(expr= - m.b33 + m.x104 <= 0)

m.c245 = Constraint(expr= - m.b34 + m.x105 <= 0)

m.c246 = Constraint(expr= - m.b35 + m.x106 <= 0)

m.c247 = Constraint(expr= - m.b36 + m.x107 <= 0)

m.c248 = Constraint(expr= - m.b37 + m.x108 <= 0)

m.c249 = Constraint(expr= - m.b38 + m.x109 <= 0)

m.c250 = Constraint(expr= - m.b39 + m.x110 <= 0)

m.c251 = Constraint(expr= - m.b40 + m.x111 <= 0)

m.c252 = Constraint(expr= - m.b41 + m.x112 <= 0)

m.c253 = Constraint(expr= - m.b42 + m.x113 <= 0)

m.c254 = Constraint(expr= - m.b43 + m.x114 <= 0)

m.c255 = Constraint(expr= - m.b44 + m.x115 <= 0)

m.c256 = Constraint(expr= - m.b45 + m.x116 <= 0)

m.c257 = Constraint(expr= - m.b46 + m.x117 <= 0)

m.c258 = Constraint(expr= - m.b47 + m.x118 <= 0)

m.c259 = Constraint(expr= - m.b48 + m.x119 <= 0)

m.c260 = Constraint(expr= - m.b49 + m.x120 <= 0)

m.c261 = Constraint(expr= - m.b50 + m.x121 <= 0)

m.c262 = Constraint(expr= - m.b51 + m.x122 <= 0)

m.c263 = Constraint(expr= - m.b52 + m.x123 <= 0)

m.c264 = Constraint(expr= - m.b53 + m.x124 <= 0)

m.c265 = Constraint(expr= - m.b54 + m.x125 <= 0)

m.c266 = Constraint(expr= - m.b55 + m.x126 <= 0)

m.c267 = Constraint(expr= - m.b56 + m.x127 <= 0)

m.c268 = Constraint(expr= - m.b57 + m.x128 <= 0)

m.c269 = Constraint(expr= - m.b58 + m.x129 <= 0)

m.c270 = Constraint(expr= - m.b59 + m.x130 <= 0)

m.c271 = Constraint(expr= - m.b60 + m.x131 <= 0)

m.c272 = Constraint(expr= - m.b61 + m.x132 <= 0)

m.c273 = Constraint(expr= - m.b62 + m.x133 <= 0)

m.c274 = Constraint(expr= - m.b63 + m.x134 <= 0)

m.c275 = Constraint(expr= - m.b64 + m.x135 <= 0)

m.c276 = Constraint(expr= - m.b65 + m.x136 <= 0)

m.c277 = Constraint(expr= - m.b66 + m.x137 <= 0)

m.c278 = Constraint(expr= - m.b67 + m.x138 <= 0)

m.c279 = Constraint(expr= - m.b68 + m.x139 <= 0)

m.c280 = Constraint(expr= - m.b69 + m.x140 <= 0)

m.c281 = Constraint(expr= - m.b70 + m.x141 <= 0)

m.c282 = Constraint(expr= - m.b21 + m.x142 <= 0)

m.c283 = Constraint(expr= - m.b22 + m.x143 <= 0)

m.c284 = Constraint(expr= - m.b23 + m.x144 <= 0)

m.c285 = Constraint(expr= - m.b24 + m.x145 <= 0)

m.c286 = Constraint(expr= - m.b25 + m.x146 <= 0)

m.c287 = Constraint(expr= - m.b26 + m.x147 <= 0)

m.c288 = Constraint(expr= - m.b27 + m.x148 <= 0)

m.c289 = Constraint(expr= - m.b28 + m.x149 <= 0)

m.c290 = Constraint(expr= - m.b29 + m.x150 <= 0)

m.c291 = Constraint(expr= - m.b30 + m.x151 <= 0)

m.c292 = Constraint(expr= - m.b31 + m.x152 <= 0)

m.c293 = Constraint(expr= - m.b32 + m.x153 <= 0)

m.c294 = Constraint(expr= - m.b33 + m.x154 <= 0)

m.c295 = Constraint(expr= - m.b34 + m.x155 <= 0)

m.c296 = Constraint(expr= - m.b35 + m.x156 <= 0)

m.c297 = Constraint(expr= - m.b36 + m.x157 <= 0)

m.c298 = Constraint(expr= - m.b37 + m.x158 <= 0)

m.c299 = Constraint(expr= - m.b38 + m.x159 <= 0)

m.c300 = Constraint(expr= - m.b39 + m.x160 <= 0)

m.c301 = Constraint(expr= - m.b40 + m.x161 <= 0)

m.c302 = Constraint(expr= - m.b41 + m.x162 <= 0)

m.c303 = Constraint(expr= - m.b42 + m.x163 <= 0)

m.c304 = Constraint(expr= - m.b43 + m.x164 <= 0)

m.c305 = Constraint(expr= - m.b44 + m.x165 <= 0)

m.c306 = Constraint(expr= - m.b45 + m.x166 <= 0)

m.c307 = Constraint(expr= - m.b46 + m.x167 <= 0)

m.c308 = Constraint(expr= - m.b47 + m.x168 <= 0)

m.c309 = Constraint(expr= - m.b48 + m.x169 <= 0)

m.c310 = Constraint(expr= - m.b49 + m.x170 <= 0)

m.c311 = Constraint(expr= - m.b50 + m.x171 <= 0)

m.c312 = Constraint(expr= - m.b51 + m.x172 <= 0)

m.c313 = Constraint(expr= - m.b52 + m.x173 <= 0)

m.c314 = Constraint(expr= - m.b53 + m.x174 <= 0)

m.c315 = Constraint(expr= - m.b54 + m.x175 <= 0)

m.c316 = Constraint(expr= - m.b55 + m.x176 <= 0)

m.c317 = Constraint(expr= - m.b56 + m.x177 <= 0)

m.c318 = Constraint(expr= - m.b57 + m.x178 <= 0)

m.c319 = Constraint(expr= - m.b58 + m.x179 <= 0)

m.c320 = Constraint(expr= - m.b59 + m.x180 <= 0)

m.c321 = Constraint(expr= - m.b60 + m.x181 <= 0)

m.c322 = Constraint(expr= - m.b61 + m.x182 <= 0)

m.c323 = Constraint(expr= - m.b62 + m.x183 <= 0)

m.c324 = Constraint(expr= - m.b63 + m.x184 <= 0)

m.c325 = Constraint(expr= - m.b64 + m.x185 <= 0)

m.c326 = Constraint(expr= - m.b65 + m.x186 <= 0)

m.c327 = Constraint(expr= - m.b66 + m.x187 <= 0)

m.c328 = Constraint(expr= - m.b67 + m.x188 <= 0)

m.c329 = Constraint(expr= - m.b68 + m.x189 <= 0)

m.c330 = Constraint(expr= - m.b69 + m.x190 <= 0)

m.c331 = Constraint(expr= - m.b70 + m.x191 <= 0)

m.c332 = Constraint(expr= - m.b21 + m.x192 <= 0)

m.c333 = Constraint(expr= - m.b22 + m.x193 <= 0)

m.c334 = Constraint(expr= - m.b23 + m.x194 <= 0)

m.c335 = Constraint(expr= - m.b24 + m.x195 <= 0)

m.c336 = Constraint(expr= - m.b25 + m.x196 <= 0)

m.c337 = Constraint(expr= - m.b26 + m.x197 <= 0)

m.c338 = Constraint(expr= - m.b27 + m.x198 <= 0)

m.c339 = Constraint(expr= - m.b28 + m.x199 <= 0)

m.c340 = Constraint(expr= - m.b29 + m.x200 <= 0)

m.c341 = Constraint(expr= - m.b30 + m.x201 <= 0)

m.c342 = Constraint(expr= - m.b31 + m.x202 <= 0)

m.c343 = Constraint(expr= - m.b32 + m.x203 <= 0)

m.c344 = Constraint(expr= - m.b33 + m.x204 <= 0)

m.c345 = Constraint(expr= - m.b34 + m.x205 <= 0)

m.c346 = Constraint(expr= - m.b35 + m.x206 <= 0)

m.c347 = Constraint(expr= - m.b36 + m.x207 <= 0)

m.c348 = Constraint(expr= - m.b37 + m.x208 <= 0)

m.c349 = Constraint(expr= - m.b38 + m.x209 <= 0)

m.c350 = Constraint(expr= - m.b39 + m.x210 <= 0)

m.c351 = Constraint(expr= - m.b40 + m.x211 <= 0)

m.c352 = Constraint(expr= - m.b41 + m.x212 <= 0)

m.c353 = Constraint(expr= - m.b42 + m.x213 <= 0)

m.c354 = Constraint(expr= - m.b43 + m.x214 <= 0)

m.c355 = Constraint(expr= - m.b44 + m.x215 <= 0)

m.c356 = Constraint(expr= - m.b45 + m.x216 <= 0)

m.c357 = Constraint(expr= - m.b46 + m.x217 <= 0)

m.c358 = Constraint(expr= - m.b47 + m.x218 <= 0)

m.c359 = Constraint(expr= - m.b48 + m.x219 <= 0)

m.c360 = Constraint(expr= - m.b49 + m.x220 <= 0)

m.c361 = Constraint(expr= - m.b50 + m.x221 <= 0)

m.c362 = Constraint(expr= - m.b51 + m.x222 <= 0)

m.c363 = Constraint(expr= - m.b52 + m.x223 <= 0)

m.c364 = Constraint(expr= - m.b53 + m.x224 <= 0)

m.c365 = Constraint(expr= - m.b54 + m.x225 <= 0)

m.c366 = Constraint(expr= - m.b55 + m.x226 <= 0)

m.c367 = Constraint(expr= - m.b56 + m.x227 <= 0)

m.c368 = Constraint(expr= - m.b57 + m.x228 <= 0)

m.c369 = Constraint(expr= - m.b58 + m.x229 <= 0)

m.c370 = Constraint(expr= - m.b59 + m.x230 <= 0)

m.c371 = Constraint(expr= - m.b60 + m.x231 <= 0)

m.c372 = Constraint(expr= - m.b61 + m.x232 <= 0)

m.c373 = Constraint(expr= - m.b62 + m.x233 <= 0)

m.c374 = Constraint(expr= - m.b63 + m.x234 <= 0)

m.c375 = Constraint(expr= - m.b64 + m.x235 <= 0)

m.c376 = Constraint(expr= - m.b65 + m.x236 <= 0)

m.c377 = Constraint(expr= - m.b66 + m.x237 <= 0)

m.c378 = Constraint(expr= - m.b67 + m.x238 <= 0)

m.c379 = Constraint(expr= - m.b68 + m.x239 <= 0)

m.c380 = Constraint(expr= - m.b69 + m.x240 <= 0)

m.c381 = Constraint(expr= - m.b70 + m.x241 <= 0)

m.c382 = Constraint(expr= - m.b1 - m.b21 + m.x92 >= -1)

m.c383 = Constraint(expr= - m.b1 - m.b22 + m.x93 >= -1)

m.c384 = Constraint(expr= - m.b1 - m.b23 + m.x94 >= -1)

m.c385 = Constraint(expr= - m.b1 - m.b24 + m.x95 >= -1)

m.c386 = Constraint(expr= - m.b1 - m.b25 + m.x96 >= -1)

m.c387 = Constraint(expr= - m.b1 - m.b26 + m.x97 >= -1)

m.c388 = Constraint(expr= - m.b1 - m.b27 + m.x98 >= -1)

m.c389 = Constraint(expr= - m.b1 - m.b28 + m.x99 >= -1)

m.c390 = Constraint(expr= - m.b1 - m.b29 + m.x100 >= -1)

m.c391 = Constraint(expr= - m.b1 - m.b30 + m.x101 >= -1)

m.c392 = Constraint(expr= - m.b2 - m.b31 + m.x102 >= -1)

m.c393 = Constraint(expr= - m.b2 - m.b32 + m.x103 >= -1)

m.c394 = Constraint(expr= - m.b2 - m.b33 + m.x104 >= -1)

m.c395 = Constraint(expr= - m.b2 - m.b34 + m.x105 >= -1)

m.c396 = Constraint(expr= - m.b2 - m.b35 + m.x106 >= -1)

m.c397 = Constraint(expr= - m.b2 - m.b36 + m.x107 >= -1)

m.c398 = Constraint(expr= - m.b2 - m.b37 + m.x108 >= -1)

m.c399 = Constraint(expr= - m.b2 - m.b38 + m.x109 >= -1)

m.c400 = Constraint(expr= - m.b2 - m.b39 + m.x110 >= -1)

m.c401 = Constraint(expr= - m.b2 - m.b40 + m.x111 >= -1)

m.c402 = Constraint(expr= - m.b3 - m.b41 + m.x112 >= -1)

m.c403 = Constraint(expr= - m.b3 - m.b42 + m.x113 >= -1)

m.c404 = Constraint(expr= - m.b3 - m.b43 + m.x114 >= -1)

m.c405 = Constraint(expr= - m.b3 - m.b44 + m.x115 >= -1)

m.c406 = Constraint(expr= - m.b3 - m.b45 + m.x116 >= -1)

m.c407 = Constraint(expr= - m.b3 - m.b46 + m.x117 >= -1)

m.c408 = Constraint(expr= - m.b3 - m.b47 + m.x118 >= -1)

m.c409 = Constraint(expr= - m.b3 - m.b48 + m.x119 >= -1)

m.c410 = Constraint(expr= - m.b3 - m.b49 + m.x120 >= -1)

m.c411 = Constraint(expr= - m.b3 - m.b50 + m.x121 >= -1)

m.c412 = Constraint(expr= - m.b4 - m.b51 + m.x122 >= -1)

m.c413 = Constraint(expr= - m.b4 - m.b52 + m.x123 >= -1)

m.c414 = Constraint(expr= - m.b4 - m.b53 + m.x124 >= -1)

m.c415 = Constraint(expr= - m.b4 - m.b54 + m.x125 >= -1)

m.c416 = Constraint(expr= - m.b4 - m.b55 + m.x126 >= -1)

m.c417 = Constraint(expr= - m.b4 - m.b56 + m.x127 >= -1)

m.c418 = Constraint(expr= - m.b4 - m.b57 + m.x128 >= -1)

m.c419 = Constraint(expr= - m.b4 - m.b58 + m.x129 >= -1)

m.c420 = Constraint(expr= - m.b4 - m.b59 + m.x130 >= -1)

m.c421 = Constraint(expr= - m.b4 - m.b60 + m.x131 >= -1)

m.c422 = Constraint(expr= - m.b5 - m.b61 + m.x132 >= -1)

m.c423 = Constraint(expr= - m.b5 - m.b62 + m.x133 >= -1)

m.c424 = Constraint(expr= - m.b5 - m.b63 + m.x134 >= -1)

m.c425 = Constraint(expr= - m.b5 - m.b64 + m.x135 >= -1)

m.c426 = Constraint(expr= - m.b5 - m.b65 + m.x136 >= -1)

m.c427 = Constraint(expr= - m.b5 - m.b66 + m.x137 >= -1)

m.c428 = Constraint(expr= - m.b5 - m.b67 + m.x138 >= -1)

m.c429 = Constraint(expr= - m.b5 - m.b68 + m.x139 >= -1)

m.c430 = Constraint(expr= - m.b5 - m.b69 + m.x140 >= -1)

m.c431 = Constraint(expr= - m.b5 - m.b70 + m.x141 >= -1)

m.c432 = Constraint(expr= - m.b6 - m.b21 + m.x142 >= -1)

m.c433 = Constraint(expr= - m.b6 - m.b22 + m.x143 >= -1)

m.c434 = Constraint(expr= - m.b6 - m.b23 + m.x144 >= -1)

m.c435 = Constraint(expr= - m.b6 - m.b24 + m.x145 >= -1)

m.c436 = Constraint(expr= - m.b6 - m.b25 + m.x146 >= -1)

m.c437 = Constraint(expr= - m.b6 - m.b26 + m.x147 >= -1)

m.c438 = Constraint(expr= - m.b6 - m.b27 + m.x148 >= -1)

m.c439 = Constraint(expr= - m.b6 - m.b28 + m.x149 >= -1)

m.c440 = Constraint(expr= - m.b6 - m.b29 + m.x150 >= -1)

m.c441 = Constraint(expr= - m.b6 - m.b30 + m.x151 >= -1)

m.c442 = Constraint(expr= - m.b7 - m.b31 + m.x152 >= -1)

m.c443 = Constraint(expr= - m.b7 - m.b32 + m.x153 >= -1)

m.c444 = Constraint(expr= - m.b7 - m.b33 + m.x154 >= -1)

m.c445 = Constraint(expr= - m.b7 - m.b34 + m.x155 >= -1)

m.c446 = Constraint(expr= - m.b7 - m.b35 + m.x156 >= -1)

m.c447 = Constraint(expr= - m.b7 - m.b36 + m.x157 >= -1)

m.c448 = Constraint(expr= - m.b7 - m.b37 + m.x158 >= -1)

m.c449 = Constraint(expr= - m.b7 - m.b38 + m.x159 >= -1)

m.c450 = Constraint(expr= - m.b7 - m.b39 + m.x160 >= -1)

m.c451 = Constraint(expr= - m.b7 - m.b40 + m.x161 >= -1)

m.c452 = Constraint(expr= - m.b8 - m.b41 + m.x162 >= -1)

m.c453 = Constraint(expr= - m.b8 - m.b42 + m.x163 >= -1)

m.c454 = Constraint(expr= - m.b8 - m.b43 + m.x164 >= -1)

m.c455 = Constraint(expr= - m.b8 - m.b44 + m.x165 >= -1)

m.c456 = Constraint(expr= - m.b8 - m.b45 + m.x166 >= -1)

m.c457 = Constraint(expr= - m.b8 - m.b46 + m.x167 >= -1)

m.c458 = Constraint(expr= - m.b8 - m.b47 + m.x168 >= -1)

m.c459 = Constraint(expr= - m.b8 - m.b48 + m.x169 >= -1)

m.c460 = Constraint(expr= - m.b8 - m.b49 + m.x170 >= -1)

m.c461 = Constraint(expr= - m.b8 - m.b50 + m.x171 >= -1)

m.c462 = Constraint(expr= - m.b9 - m.b51 + m.x172 >= -1)

m.c463 = Constraint(expr= - m.b9 - m.b52 + m.x173 >= -1)

m.c464 = Constraint(expr= - m.b9 - m.b53 + m.x174 >= -1)

m.c465 = Constraint(expr= - m.b9 - m.b54 + m.x175 >= -1)

m.c466 = Constraint(expr= - m.b9 - m.b55 + m.x176 >= -1)

m.c467 = Constraint(expr= - m.b9 - m.b56 + m.x177 >= -1)

m.c468 = Constraint(expr= - m.b9 - m.b57 + m.x178 >= -1)

m.c469 = Constraint(expr= - m.b9 - m.b58 + m.x179 >= -1)

m.c470 = Constraint(expr= - m.b9 - m.b59 + m.x180 >= -1)

m.c471 = Constraint(expr= - m.b9 - m.b60 + m.x181 >= -1)

m.c472 = Constraint(expr= - m.b10 - m.b61 + m.x182 >= -1)

m.c473 = Constraint(expr= - m.b10 - m.b62 + m.x183 >= -1)

m.c474 = Constraint(expr= - m.b10 - m.b63 + m.x184 >= -1)

m.c475 = Constraint(expr= - m.b10 - m.b64 + m.x185 >= -1)

m.c476 = Constraint(expr= - m.b10 - m.b65 + m.x186 >= -1)

m.c477 = Constraint(expr= - m.b10 - m.b66 + m.x187 >= -1)

m.c478 = Constraint(expr= - m.b10 - m.b67 + m.x188 >= -1)

m.c479 = Constraint(expr= - m.b10 - m.b68 + m.x189 >= -1)

m.c480 = Constraint(expr= - m.b10 - m.b69 + m.x190 >= -1)

m.c481 = Constraint(expr= - m.b10 - m.b70 + m.x191 >= -1)

m.c482 = Constraint(expr= - m.b11 - m.b21 + m.x192 >= -1)

m.c483 = Constraint(expr= - m.b11 - m.b22 + m.x193 >= -1)

m.c484 = Constraint(expr= - m.b11 - m.b23 + m.x194 >= -1)

m.c485 = Constraint(expr= - m.b11 - m.b24 + m.x195 >= -1)

m.c486 = Constraint(expr= - m.b11 - m.b25 + m.x196 >= -1)

m.c487 = Constraint(expr= - m.b11 - m.b26 + m.x197 >= -1)

m.c488 = Constraint(expr= - m.b11 - m.b27 + m.x198 >= -1)

m.c489 = Constraint(expr= - m.b11 - m.b28 + m.x199 >= -1)

m.c490 = Constraint(expr= - m.b11 - m.b29 + m.x200 >= -1)

m.c491 = Constraint(expr= - m.b11 - m.b30 + m.x201 >= -1)

m.c492 = Constraint(expr= - m.b12 - m.b31 + m.x202 >= -1)

m.c493 = Constraint(expr= - m.b12 - m.b32 + m.x203 >= -1)

m.c494 = Constraint(expr= - m.b12 - m.b33 + m.x204 >= -1)

m.c495 = Constraint(expr= - m.b12 - m.b34 + m.x205 >= -1)

m.c496 = Constraint(expr= - m.b12 - m.b35 + m.x206 >= -1)

m.c497 = Constraint(expr= - m.b12 - m.b36 + m.x207 >= -1)

m.c498 = Constraint(expr= - m.b12 - m.b37 + m.x208 >= -1)

m.c499 = Constraint(expr= - m.b12 - m.b38 + m.x209 >= -1)

m.c500 = Constraint(expr= - m.b12 - m.b39 + m.x210 >= -1)

m.c501 = Constraint(expr= - m.b12 - m.b40 + m.x211 >= -1)

m.c502 = Constraint(expr= - m.b13 - m.b41 + m.x212 >= -1)

m.c503 = Constraint(expr= - m.b13 - m.b42 + m.x213 >= -1)

m.c504 = Constraint(expr= - m.b13 - m.b43 + m.x214 >= -1)

m.c505 = Constraint(expr= - m.b13 - m.b44 + m.x215 >= -1)

m.c506 = Constraint(expr= - m.b13 - m.b45 + m.x216 >= -1)

m.c507 = Constraint(expr= - m.b13 - m.b46 + m.x217 >= -1)

m.c508 = Constraint(expr= - m.b13 - m.b47 + m.x218 >= -1)

m.c509 = Constraint(expr= - m.b13 - m.b48 + m.x219 >= -1)

m.c510 = Constraint(expr= - m.b13 - m.b49 + m.x220 >= -1)

m.c511 = Constraint(expr= - m.b13 - m.b50 + m.x221 >= -1)

m.c512 = Constraint(expr= - m.b14 - m.b51 + m.x222 >= -1)

m.c513 = Constraint(expr= - m.b14 - m.b52 + m.x223 >= -1)

m.c514 = Constraint(expr= - m.b14 - m.b53 + m.x224 >= -1)

m.c515 = Constraint(expr= - m.b14 - m.b54 + m.x225 >= -1)

m.c516 = Constraint(expr= - m.b14 - m.b55 + m.x226 >= -1)

m.c517 = Constraint(expr= - m.b14 - m.b56 + m.x227 >= -1)

m.c518 = Constraint(expr= - m.b14 - m.b57 + m.x228 >= -1)

m.c519 = Constraint(expr= - m.b14 - m.b58 + m.x229 >= -1)

m.c520 = Constraint(expr= - m.b14 - m.b59 + m.x230 >= -1)

m.c521 = Constraint(expr= - m.b14 - m.b60 + m.x231 >= -1)

m.c522 = Constraint(expr= - m.b15 - m.b61 + m.x232 >= -1)

m.c523 = Constraint(expr= - m.b15 - m.b62 + m.x233 >= -1)

m.c524 = Constraint(expr= - m.b15 - m.b63 + m.x234 >= -1)

m.c525 = Constraint(expr= - m.b15 - m.b64 + m.x235 >= -1)

m.c526 = Constraint(expr= - m.b15 - m.b65 + m.x236 >= -1)

m.c527 = Constraint(expr= - m.b15 - m.b66 + m.x237 >= -1)

m.c528 = Constraint(expr= - m.b15 - m.b67 + m.x238 >= -1)

m.c529 = Constraint(expr= - m.b15 - m.b68 + m.x239 >= -1)

m.c530 = Constraint(expr= - m.b15 - m.b69 + m.x240 >= -1)

m.c531 = Constraint(expr= - m.b15 - m.b70 + m.x241 >= -1)

m.c532 = Constraint(expr= - m.x71 + m.x347 + m.x397 == 0)

m.c533 = Constraint(expr= - m.x71 + m.x348 + m.x398 == 0)

m.c534 = Constraint(expr= - m.x71 + m.x349 + m.x399 == 0)

m.c535 = Constraint(expr= - m.x71 + m.x350 + m.x400 == 0)

m.c536 = Constraint(expr= - m.x71 + m.x351 + m.x401 == 0)

m.c537 = Constraint(expr= - m.x71 + m.x352 + m.x402 == 0)

m.c538 = Constraint(expr= - m.x71 + m.x353 + m.x403 == 0)

m.c539 = Constraint(expr= - m.x71 + m.x354 + m.x404 == 0)

m.c540 = Constraint(expr= - m.x71 + m.x355 + m.x405 == 0)

m.c541 = Constraint(expr= - m.x71 + m.x356 + m.x406 == 0)

m.c542 = Constraint(expr= - m.x72 + m.x357 + m.x407 == 0)

m.c543 = Constraint(expr= - m.x72 + m.x358 + m.x408 == 0)

m.c544 = Constraint(expr= - m.x72 + m.x359 + m.x409 == 0)

m.c545 = Constraint(expr= - m.x72 + m.x360 + m.x410 == 0)

m.c546 = Constraint(expr= - m.x72 + m.x361 + m.x411 == 0)

m.c547 = Constraint(expr= - m.x72 + m.x362 + m.x412 == 0)

m.c548 = Constraint(expr= - m.x72 + m.x363 + m.x413 == 0)

m.c549 = Constraint(expr= - m.x72 + m.x364 + m.x414 == 0)

m.c550 = Constraint(expr= - m.x72 + m.x365 + m.x415 == 0)

m.c551 = Constraint(expr= - m.x72 + m.x366 + m.x416 == 0)

m.c552 = Constraint(expr= - m.x73 + m.x367 + m.x417 == 0)

m.c553 = Constraint(expr= - m.x73 + m.x368 + m.x418 == 0)

m.c554 = Constraint(expr= - m.x73 + m.x369 + m.x419 == 0)

m.c555 = Constraint(expr= - m.x73 + m.x370 + m.x420 == 0)

m.c556 = Constraint(expr= - m.x73 + m.x371 + m.x421 == 0)

m.c557 = Constraint(expr= - m.x73 + m.x372 + m.x422 == 0)

m.c558 = Constraint(expr= - m.x73 + m.x373 + m.x423 == 0)

m.c559 = Constraint(expr= - m.x73 + m.x374 + m.x424 == 0)

m.c560 = Constraint(expr= - m.x73 + m.x375 + m.x425 == 0)

m.c561 = Constraint(expr= - m.x73 + m.x376 + m.x426 == 0)

m.c562 = Constraint(expr= - m.x74 + m.x377 + m.x427 == 0)

m.c563 = Constraint(expr= - m.x74 + m.x378 + m.x428 == 0)

m.c564 = Constraint(expr= - m.x74 + m.x379 + m.x429 == 0)

m.c565 = Constraint(expr= - m.x74 + m.x380 + m.x430 == 0)

m.c566 = Constraint(expr= - m.x74 + m.x381 + m.x431 == 0)

m.c567 = Constraint(expr= - m.x74 + m.x382 + m.x432 == 0)

m.c568 = Constraint(expr= - m.x74 + m.x383 + m.x433 == 0)

m.c569 = Constraint(expr= - m.x74 + m.x384 + m.x434 == 0)

m.c570 = Constraint(expr= - m.x74 + m.x385 + m.x435 == 0)

m.c571 = Constraint(expr= - m.x74 + m.x386 + m.x436 == 0)

m.c572 = Constraint(expr= - m.x75 + m.x387 + m.x437 == 0)

m.c573 = Constraint(expr= - m.x75 + m.x388 + m.x438 == 0)

m.c574 = Constraint(expr= - m.x75 + m.x389 + m.x439 == 0)

m.c575 = Constraint(expr= - m.x75 + m.x390 + m.x440 == 0)

m.c576 = Constraint(expr= - m.x75 + m.x391 + m.x441 == 0)

m.c577 = Constraint(expr= - m.x75 + m.x392 + m.x442 == 0)

m.c578 = Constraint(expr= - m.x75 + m.x393 + m.x443 == 0)

m.c579 = Constraint(expr= - m.x75 + m.x394 + m.x444 == 0)

m.c580 = Constraint(expr= - m.x75 + m.x395 + m.x445 == 0)

m.c581 = Constraint(expr= - m.x75 + m.x396 + m.x446 == 0)

m.c582 = Constraint(expr= - 11*m.b21 + m.x347 <= 0)

m.c583 = Constraint(expr= - 11*m.b22 + m.x348 <= 0)

m.c584 = Constraint(expr= - 11*m.b23 + m.x349 <= 0)

m.c585 = Constraint(expr= - 11*m.b24 + m.x350 <= 0)

m.c586 = Constraint(expr= - 11*m.b25 + m.x351 <= 0)

m.c587 = Constraint(expr= - 11*m.b26 + m.x352 <= 0)

m.c588 = Constraint(expr= - 11*m.b27 + m.x353 <= 0)

m.c589 = Constraint(expr= - 11*m.b28 + m.x354 <= 0)

m.c590 = Constraint(expr= - 11*m.b29 + m.x355 <= 0)

m.c591 = Constraint(expr= - 11*m.b30 + m.x356 <= 0)

m.c592 = Constraint(expr= - 10*m.b31 + m.x357 <= 0)

m.c593 = Constraint(expr= - 10*m.b32 + m.x358 <= 0)

m.c594 = Constraint(expr= - 10*m.b33 + m.x359 <= 0)

m.c595 = Constraint(expr= - 10*m.b34 + m.x360 <= 0)

m.c596 = Constraint(expr= - 10*m.b35 + m.x361 <= 0)

m.c597 = Constraint(expr= - 10*m.b36 + m.x362 <= 0)

m.c598 = Constraint(expr= - 10*m.b37 + m.x363 <= 0)

m.c599 = Constraint(expr= - 10*m.b38 + m.x364 <= 0)

m.c600 = Constraint(expr= - 10*m.b39 + m.x365 <= 0)

m.c601 = Constraint(expr= - 10*m.b40 + m.x366 <= 0)

m.c602 = Constraint(expr= - 11*m.b41 + m.x367 <= 0)

m.c603 = Constraint(expr= - 11*m.b42 + m.x368 <= 0)

m.c604 = Constraint(expr= - 11*m.b43 + m.x369 <= 0)

m.c605 = Constraint(expr= - 11*m.b44 + m.x370 <= 0)

m.c606 = Constraint(expr= - 11*m.b45 + m.x371 <= 0)

m.c607 = Constraint(expr= - 11*m.b46 + m.x372 <= 0)

m.c608 = Constraint(expr= - 11*m.b47 + m.x373 <= 0)

m.c609 = Constraint(expr= - 11*m.b48 + m.x374 <= 0)

m.c610 = Constraint(expr= - 11*m.b49 + m.x375 <= 0)

m.c611 = Constraint(expr= - 11*m.b50 + m.x376 <= 0)

m.c612 = Constraint(expr= - 7*m.b51 + m.x377 <= 0)

m.c613 = Constraint(expr= - 7*m.b52 + m.x378 <= 0)

m.c614 = Constraint(expr= - 7*m.b53 + m.x379 <= 0)

m.c615 = Constraint(expr= - 7*m.b54 + m.x380 <= 0)

m.c616 = Constraint(expr= - 7*m.b55 + m.x381 <= 0)

m.c617 = Constraint(expr= - 7*m.b56 + m.x382 <= 0)

m.c618 = Constraint(expr= - 7*m.b57 + m.x383 <= 0)

m.c619 = Constraint(expr= - 7*m.b58 + m.x384 <= 0)

m.c620 = Constraint(expr= - 7*m.b59 + m.x385 <= 0)

m.c621 = Constraint(expr= - 7*m.b60 + m.x386 <= 0)

m.c622 = Constraint(expr= - 10*m.b61 + m.x387 <= 0)

m.c623 = Constraint(expr= - 10*m.b62 + m.x388 <= 0)

m.c624 = Constraint(expr= - 10*m.b63 + m.x389 <= 0)

m.c625 = Constraint(expr= - 10*m.b64 + m.x390 <= 0)

m.c626 = Constraint(expr= - 10*m.b65 + m.x391 <= 0)

m.c627 = Constraint(expr= - 10*m.b66 + m.x392 <= 0)

m.c628 = Constraint(expr= - 10*m.b67 + m.x393 <= 0)

m.c629 = Constraint(expr= - 10*m.b68 + m.x394 <= 0)

m.c630 = Constraint(expr= - 10*m.b69 + m.x395 <= 0)

m.c631 = Constraint(expr= - 10*m.b70 + m.x396 <= 0)

m.c632 = Constraint(expr=   11*m.b21 + m.x397 <= 11)

m.c633 = Constraint(expr=   11*m.b22 + m.x398 <= 11)

m.c634 = Constraint(expr=   11*m.b23 + m.x399 <= 11)

m.c635 = Constraint(expr=   11*m.b24 + m.x400 <= 11)

m.c636 = Constraint(expr=   11*m.b25 + m.x401 <= 11)

m.c637 = Constraint(expr=   11*m.b26 + m.x402 <= 11)

m.c638 = Constraint(expr=   11*m.b27 + m.x403 <= 11)

m.c639 = Constraint(expr=   11*m.b28 + m.x404 <= 11)

m.c640 = Constraint(expr=   11*m.b29 + m.x405 <= 11)

m.c641 = Constraint(expr=   11*m.b30 + m.x406 <= 11)

m.c642 = Constraint(expr=   10*m.b31 + m.x407 <= 10)

m.c643 = Constraint(expr=   10*m.b32 + m.x408 <= 10)

m.c644 = Constraint(expr=   10*m.b33 + m.x409 <= 10)

m.c645 = Constraint(expr=   10*m.b34 + m.x410 <= 10)

m.c646 = Constraint(expr=   10*m.b35 + m.x411 <= 10)

m.c647 = Constraint(expr=   10*m.b36 + m.x412 <= 10)

m.c648 = Constraint(expr=   10*m.b37 + m.x413 <= 10)

m.c649 = Constraint(expr=   10*m.b38 + m.x414 <= 10)

m.c650 = Constraint(expr=   10*m.b39 + m.x415 <= 10)

m.c651 = Constraint(expr=   10*m.b40 + m.x416 <= 10)

m.c652 = Constraint(expr=   11*m.b41 + m.x417 <= 11)

m.c653 = Constraint(expr=   11*m.b42 + m.x418 <= 11)

m.c654 = Constraint(expr=   11*m.b43 + m.x419 <= 11)

m.c655 = Constraint(expr=   11*m.b44 + m.x420 <= 11)

m.c656 = Constraint(expr=   11*m.b45 + m.x421 <= 11)

m.c657 = Constraint(expr=   11*m.b46 + m.x422 <= 11)

m.c658 = Constraint(expr=   11*m.b47 + m.x423 <= 11)

m.c659 = Constraint(expr=   11*m.b48 + m.x424 <= 11)

m.c660 = Constraint(expr=   11*m.b49 + m.x425 <= 11)

m.c661 = Constraint(expr=   11*m.b50 + m.x426 <= 11)

m.c662 = Constraint(expr=   7*m.b51 + m.x427 <= 7)

m.c663 = Constraint(expr=   7*m.b52 + m.x428 <= 7)

m.c664 = Constraint(expr=   7*m.b53 + m.x429 <= 7)

m.c665 = Constraint(expr=   7*m.b54 + m.x430 <= 7)

m.c666 = Constraint(expr=   7*m.b55 + m.x431 <= 7)

m.c667 = Constraint(expr=   7*m.b56 + m.x432 <= 7)

m.c668 = Constraint(expr=   7*m.b57 + m.x433 <= 7)

m.c669 = Constraint(expr=   7*m.b58 + m.x434 <= 7)

m.c670 = Constraint(expr=   7*m.b59 + m.x435 <= 7)

m.c671 = Constraint(expr=   7*m.b60 + m.x436 <= 7)

m.c672 = Constraint(expr=   10*m.b61 + m.x437 <= 10)

m.c673 = Constraint(expr=   10*m.b62 + m.x438 <= 10)

m.c674 = Constraint(expr=   10*m.b63 + m.x439 <= 10)

m.c675 = Constraint(expr=   10*m.b64 + m.x440 <= 10)

m.c676 = Constraint(expr=   10*m.b65 + m.x441 <= 10)

m.c677 = Constraint(expr=   10*m.b66 + m.x442 <= 10)

m.c678 = Constraint(expr=   10*m.b67 + m.x443 <= 10)

m.c679 = Constraint(expr=   10*m.b68 + m.x444 <= 10)

m.c680 = Constraint(expr=   10*m.b69 + m.x445 <= 10)

m.c681 = Constraint(expr=   10*m.b70 + m.x446 <= 10)

m.c682 = Constraint(expr= - m.x76 + m.x247 + m.x297 == 0)

m.c683 = Constraint(expr= - m.x76 + m.x248 + m.x298 == 0)

m.c684 = Constraint(expr= - m.x76 + m.x249 + m.x299 == 0)

m.c685 = Constraint(expr= - m.x76 + m.x250 + m.x300 == 0)

m.c686 = Constraint(expr= - m.x76 + m.x251 + m.x301 == 0)

m.c687 = Constraint(expr= - m.x76 + m.x252 + m.x302 == 0)

m.c688 = Constraint(expr= - m.x76 + m.x253 + m.x303 == 0)

m.c689 = Constraint(expr= - m.x76 + m.x254 + m.x304 == 0)

m.c690 = Constraint(expr= - m.x76 + m.x255 + m.x305 == 0)

m.c691 = Constraint(expr= - m.x76 + m.x256 + m.x306 == 0)

m.c692 = Constraint(expr= - m.x77 + m.x257 + m.x307 == 0)

m.c693 = Constraint(expr= - m.x77 + m.x258 + m.x308 == 0)

m.c694 = Constraint(expr= - m.x77 + m.x259 + m.x309 == 0)

m.c695 = Constraint(expr= - m.x77 + m.x260 + m.x310 == 0)

m.c696 = Constraint(expr= - m.x77 + m.x261 + m.x311 == 0)

m.c697 = Constraint(expr= - m.x77 + m.x262 + m.x312 == 0)

m.c698 = Constraint(expr= - m.x77 + m.x263 + m.x313 == 0)

m.c699 = Constraint(expr= - m.x77 + m.x264 + m.x314 == 0)

m.c700 = Constraint(expr= - m.x77 + m.x265 + m.x315 == 0)

m.c701 = Constraint(expr= - m.x77 + m.x266 + m.x316 == 0)

m.c702 = Constraint(expr= - m.x78 + m.x267 + m.x317 == 0)

m.c703 = Constraint(expr= - m.x78 + m.x268 + m.x318 == 0)

m.c704 = Constraint(expr= - m.x78 + m.x269 + m.x319 == 0)

m.c705 = Constraint(expr= - m.x78 + m.x270 + m.x320 == 0)

m.c706 = Constraint(expr= - m.x78 + m.x271 + m.x321 == 0)

m.c707 = Constraint(expr= - m.x78 + m.x272 + m.x322 == 0)

m.c708 = Constraint(expr= - m.x78 + m.x273 + m.x323 == 0)

m.c709 = Constraint(expr= - m.x78 + m.x274 + m.x324 == 0)

m.c710 = Constraint(expr= - m.x78 + m.x275 + m.x325 == 0)

m.c711 = Constraint(expr= - m.x78 + m.x276 + m.x326 == 0)

m.c712 = Constraint(expr= - m.x79 + m.x277 + m.x327 == 0)

m.c713 = Constraint(expr= - m.x79 + m.x278 + m.x328 == 0)

m.c714 = Constraint(expr= - m.x79 + m.x279 + m.x329 == 0)

m.c715 = Constraint(expr= - m.x79 + m.x280 + m.x330 == 0)

m.c716 = Constraint(expr= - m.x79 + m.x281 + m.x331 == 0)

m.c717 = Constraint(expr= - m.x79 + m.x282 + m.x332 == 0)

m.c718 = Constraint(expr= - m.x79 + m.x283 + m.x333 == 0)

m.c719 = Constraint(expr= - m.x79 + m.x284 + m.x334 == 0)

m.c720 = Constraint(expr= - m.x79 + m.x285 + m.x335 == 0)

m.c721 = Constraint(expr= - m.x79 + m.x286 + m.x336 == 0)

m.c722 = Constraint(expr= - m.x80 + m.x287 + m.x337 == 0)

m.c723 = Constraint(expr= - m.x80 + m.x288 + m.x338 == 0)

m.c724 = Constraint(expr= - m.x80 + m.x289 + m.x339 == 0)

m.c725 = Constraint(expr= - m.x80 + m.x290 + m.x340 == 0)

m.c726 = Constraint(expr= - m.x80 + m.x291 + m.x341 == 0)

m.c727 = Constraint(expr= - m.x80 + m.x292 + m.x342 == 0)

m.c728 = Constraint(expr= - m.x80 + m.x293 + m.x343 == 0)

m.c729 = Constraint(expr= - m.x80 + m.x294 + m.x344 == 0)

m.c730 = Constraint(expr= - m.x80 + m.x295 + m.x345 == 0)

m.c731 = Constraint(expr= - m.x80 + m.x296 + m.x346 == 0)

m.c732 = Constraint(expr= - 11*m.b21 + m.x247 <= 0)

m.c733 = Constraint(expr= - 11*m.b22 + m.x248 <= 0)

m.c734 = Constraint(expr= - 11*m.b23 + m.x249 <= 0)

m.c735 = Constraint(expr= - 11*m.b24 + m.x250 <= 0)

m.c736 = Constraint(expr= - 11*m.b25 + m.x251 <= 0)

m.c737 = Constraint(expr= - 11*m.b26 + m.x252 <= 0)

m.c738 = Constraint(expr= - 11*m.b27 + m.x253 <= 0)

m.c739 = Constraint(expr= - 11*m.b28 + m.x254 <= 0)

m.c740 = Constraint(expr= - 11*m.b29 + m.x255 <= 0)

m.c741 = Constraint(expr= - 11*m.b30 + m.x256 <= 0)

m.c742 = Constraint(expr= - 10*m.b31 + m.x257 <= 0)

m.c743 = Constraint(expr= - 10*m.b32 + m.x258 <= 0)

m.c744 = Constraint(expr= - 10*m.b33 + m.x259 <= 0)

m.c745 = Constraint(expr= - 10*m.b34 + m.x260 <= 0)

m.c746 = Constraint(expr= - 10*m.b35 + m.x261 <= 0)

m.c747 = Constraint(expr= - 10*m.b36 + m.x262 <= 0)

m.c748 = Constraint(expr= - 10*m.b37 + m.x263 <= 0)

m.c749 = Constraint(expr= - 10*m.b38 + m.x264 <= 0)

m.c750 = Constraint(expr= - 10*m.b39 + m.x265 <= 0)

m.c751 = Constraint(expr= - 10*m.b40 + m.x266 <= 0)

m.c752 = Constraint(expr= - 11*m.b41 + m.x267 <= 0)

m.c753 = Constraint(expr= - 11*m.b42 + m.x268 <= 0)

m.c754 = Constraint(expr= - 11*m.b43 + m.x269 <= 0)

m.c755 = Constraint(expr= - 11*m.b44 + m.x270 <= 0)

m.c756 = Constraint(expr= - 11*m.b45 + m.x271 <= 0)

m.c757 = Constraint(expr= - 11*m.b46 + m.x272 <= 0)

m.c758 = Constraint(expr= - 11*m.b47 + m.x273 <= 0)

m.c759 = Constraint(expr= - 11*m.b48 + m.x274 <= 0)

m.c760 = Constraint(expr= - 11*m.b49 + m.x275 <= 0)

m.c761 = Constraint(expr= - 11*m.b50 + m.x276 <= 0)

m.c762 = Constraint(expr= - 7*m.b51 + m.x277 <= 0)

m.c763 = Constraint(expr= - 7*m.b52 + m.x278 <= 0)

m.c764 = Constraint(expr= - 7*m.b53 + m.x279 <= 0)

m.c765 = Constraint(expr= - 7*m.b54 + m.x280 <= 0)

m.c766 = Constraint(expr= - 7*m.b55 + m.x281 <= 0)

m.c767 = Constraint(expr= - 7*m.b56 + m.x282 <= 0)

m.c768 = Constraint(expr= - 7*m.b57 + m.x283 <= 0)

m.c769 = Constraint(expr= - 7*m.b58 + m.x284 <= 0)

m.c770 = Constraint(expr= - 7*m.b59 + m.x285 <= 0)

m.c771 = Constraint(expr= - 7*m.b60 + m.x286 <= 0)

m.c772 = Constraint(expr= - 10*m.b61 + m.x287 <= 0)

m.c773 = Constraint(expr= - 10*m.b62 + m.x288 <= 0)

m.c774 = Constraint(expr= - 10*m.b63 + m.x289 <= 0)

m.c775 = Constraint(expr= - 10*m.b64 + m.x290 <= 0)

m.c776 = Constraint(expr= - 10*m.b65 + m.x291 <= 0)

m.c777 = Constraint(expr= - 10*m.b66 + m.x292 <= 0)

m.c778 = Constraint(expr= - 10*m.b67 + m.x293 <= 0)

m.c779 = Constraint(expr= - 10*m.b68 + m.x294 <= 0)

m.c780 = Constraint(expr= - 10*m.b69 + m.x295 <= 0)

m.c781 = Constraint(expr= - 10*m.b70 + m.x296 <= 0)

m.c782 = Constraint(expr=   11*m.b21 + m.x297 <= 11)

m.c783 = Constraint(expr=   11*m.b22 + m.x298 <= 11)

m.c784 = Constraint(expr=   11*m.b23 + m.x299 <= 11)

m.c785 = Constraint(expr=   11*m.b24 + m.x300 <= 11)

m.c786 = Constraint(expr=   11*m.b25 + m.x301 <= 11)

m.c787 = Constraint(expr=   11*m.b26 + m.x302 <= 11)

m.c788 = Constraint(expr=   11*m.b27 + m.x303 <= 11)

m.c789 = Constraint(expr=   11*m.b28 + m.x304 <= 11)

m.c790 = Constraint(expr=   11*m.b29 + m.x305 <= 11)

m.c791 = Constraint(expr=   11*m.b30 + m.x306 <= 11)

m.c792 = Constraint(expr=   10*m.b31 + m.x307 <= 10)

m.c793 = Constraint(expr=   10*m.b32 + m.x308 <= 10)

m.c794 = Constraint(expr=   10*m.b33 + m.x309 <= 10)

m.c795 = Constraint(expr=   10*m.b34 + m.x310 <= 10)

m.c796 = Constraint(expr=   10*m.b35 + m.x311 <= 10)

m.c797 = Constraint(expr=   10*m.b36 + m.x312 <= 10)

m.c798 = Constraint(expr=   10*m.b37 + m.x313 <= 10)

m.c799 = Constraint(expr=   10*m.b38 + m.x314 <= 10)

m.c800 = Constraint(expr=   10*m.b39 + m.x315 <= 10)

m.c801 = Constraint(expr=   10*m.b40 + m.x316 <= 10)

m.c802 = Constraint(expr=   11*m.b41 + m.x317 <= 11)

m.c803 = Constraint(expr=   11*m.b42 + m.x318 <= 11)

m.c804 = Constraint(expr=   11*m.b43 + m.x319 <= 11)

m.c805 = Constraint(expr=   11*m.b44 + m.x320 <= 11)

m.c806 = Constraint(expr=   11*m.b45 + m.x321 <= 11)

m.c807 = Constraint(expr=   11*m.b46 + m.x322 <= 11)

m.c808 = Constraint(expr=   11*m.b47 + m.x323 <= 11)

m.c809 = Constraint(expr=   11*m.b48 + m.x324 <= 11)

m.c810 = Constraint(expr=   11*m.b49 + m.x325 <= 11)

m.c811 = Constraint(expr=   11*m.b50 + m.x326 <= 11)

m.c812 = Constraint(expr=   7*m.b51 + m.x327 <= 7)

m.c813 = Constraint(expr=   7*m.b52 + m.x328 <= 7)

m.c814 = Constraint(expr=   7*m.b53 + m.x329 <= 7)

m.c815 = Constraint(expr=   7*m.b54 + m.x330 <= 7)

m.c816 = Constraint(expr=   7*m.b55 + m.x331 <= 7)

m.c817 = Constraint(expr=   7*m.b56 + m.x332 <= 7)

m.c818 = Constraint(expr=   7*m.b57 + m.x333 <= 7)

m.c819 = Constraint(expr=   7*m.b58 + m.x334 <= 7)

m.c820 = Constraint(expr=   7*m.b59 + m.x335 <= 7)

m.c821 = Constraint(expr=   7*m.b60 + m.x336 <= 7)

m.c822 = Constraint(expr=   10*m.b61 + m.x337 <= 10)

m.c823 = Constraint(expr=   10*m.b62 + m.x338 <= 10)

m.c824 = Constraint(expr=   10*m.b63 + m.x339 <= 10)

m.c825 = Constraint(expr=   10*m.b64 + m.x340 <= 10)

m.c826 = Constraint(expr=   10*m.b65 + m.x341 <= 10)

m.c827 = Constraint(expr=   10*m.b66 + m.x342 <= 10)

m.c828 = Constraint(expr=   10*m.b67 + m.x343 <= 10)

m.c829 = Constraint(expr=   10*m.b68 + m.x344 <= 10)

m.c830 = Constraint(expr=   10*m.b69 + m.x345 <= 10)

m.c831 = Constraint(expr=   10*m.b70 + m.x346 <= 10)

m.c832 = Constraint(expr=   m.x242 - 471.299114292143*m.x247 - 87.3644508144726*m.x248 - 1199.55883169351*m.x249
                          - 1455.32236178753*m.x250 - 59.9123555503718*m.x251 - 379.038814816129*m.x252
                          - 1209.04864109044*m.x253 - 1788.49473840444*m.x254 - 938.567397231442*m.x255
                          - 2381.30274221782*m.x256 == 0)

m.c833 = Constraint(expr=   m.x243 - 471.299114292143*m.x257 - 87.3644508144726*m.x258 - 1199.55883169351*m.x259
                          - 1455.32236178753*m.x260 - 59.9123555503718*m.x261 - 379.038814816129*m.x262
                          - 1209.04864109044*m.x263 - 1788.49473840444*m.x264 - 938.567397231442*m.x265
                          - 2381.30274221782*m.x266 == 0)

m.c834 = Constraint(expr=   m.x244 - 471.299114292143*m.x267 - 87.3644508144726*m.x268 - 1199.55883169351*m.x269
                          - 1455.32236178753*m.x270 - 59.9123555503718*m.x271 - 379.038814816129*m.x272
                          - 1209.04864109044*m.x273 - 1788.49473840444*m.x274 - 938.567397231442*m.x275
                          - 2381.30274221782*m.x276 == 0)

m.c835 = Constraint(expr=   m.x245 - 471.299114292143*m.x277 - 87.3644508144726*m.x278 - 1199.55883169351*m.x279
                          - 1455.32236178753*m.x280 - 59.9123555503718*m.x281 - 379.038814816129*m.x282
                          - 1209.04864109044*m.x283 - 1788.49473840444*m.x284 - 938.567397231442*m.x285
                          - 2381.30274221782*m.x286 == 0)

m.c836 = Constraint(expr=   m.x246 - 471.299114292143*m.x287 - 87.3644508144726*m.x288 - 1199.55883169351*m.x289
                          - 1455.32236178753*m.x290 - 59.9123555503718*m.x291 - 379.038814816129*m.x292
                          - 1209.04864109044*m.x293 - 1788.49473840444*m.x294 - 938.567397231442*m.x295
                          - 2381.30274221782*m.x296 == 0)
