#  MINLP written by GAMS Convert at 04/21/18 13:51:21
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        733      209      266      258        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        404      296      108        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2524     2384      140        0
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
m.x136 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,1000),initialize=0)
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
m.x164 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,1000),initialize=0)
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
m.x199 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,300),initialize=0)
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
m.x377 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x378 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x379 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x380 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x381 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x382 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x383 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x384 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x385 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x386 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x387 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x388 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x389 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x390 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x391 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x392 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x393 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x394 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x395 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x396 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x397 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x398 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x399 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x400 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x401 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x402 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x403 = Var(within=Reals,bounds=(10,10),initialize=10)

m.obj = Objective(expr=   m.x251 + m.x252 + m.x253 + m.x254 + m.x255 + m.x256 + m.x257 + m.x258 + m.x259 + m.x260
                        + m.x261 + m.x262 + m.x263 + m.x264 + m.x265 + m.x266 + m.x267 + m.x268 + 3*m.x293 + 3*m.x294
                        + 3*m.x295 + 3*m.x296 + 3*m.x297 + 3*m.x298 + 3*m.x299 + 3*m.x300 + 3*m.x301 + 3*m.x302
                        + 3*m.x303 + 3*m.x304 + 3*m.x305 + 3*m.x306 + 3*m.x307 + 3*m.x308 + 3*m.x309 + 3*m.x310
                        + 3*m.x311 + 3*m.x312 + 3*m.x313 + 3*m.x314 + 3*m.x315 + 3*m.x316 + 5*m.x335 + 5*m.x336
                        + 5*m.x337 + 5*m.x338 + 5*m.x339 + 5*m.x340 + 5*m.x341 + 5*m.x342 + 5*m.x343 + 5*m.x344
                        + 5*m.x345 + 5*m.x346 + 5*m.x347 + 5*m.x348 + 5*m.x349 + 5*m.x350 + 5*m.x351 + 5*m.x352
                        + 1.67*m.x353 + 1.67*m.x354 + 1.67*m.x355 + 1.67*m.x356 + 1.67*m.x357 + 1.67*m.x358 + 3*m.x359
                        + 3*m.x360 + 3*m.x361 + 3*m.x362 + 3*m.x363 + 3*m.x364 + 3*m.x365 + 3*m.x366 + 3*m.x367
                        + 3*m.x368 + 3*m.x369 + 3*m.x370 + 4.33*m.x371 + 4.33*m.x372 + 4.33*m.x373 + 4.33*m.x374
                        + 4.33*m.x375 + 4.33*m.x376, sense=maximize)

m.c2 = Constraint(expr=   m.x121 == 1000)

m.c3 = Constraint(expr= - m.x121 + m.x122 + m.x233 == 0)

m.c4 = Constraint(expr= - m.x122 + m.x123 + m.x234 == 0)

m.c5 = Constraint(expr= - m.x123 + m.x124 + m.x235 == 0)

m.c6 = Constraint(expr= - m.x124 + m.x125 + m.x236 == 0)

m.c7 = Constraint(expr= - m.x125 + m.x126 + m.x237 == 0)

m.c8 = Constraint(expr= - m.x126 + m.x127 + m.x238 == 0)

m.c9 = Constraint(expr=   m.x128 == 200)

m.c10 = Constraint(expr= - m.x128 + m.x129 - m.x233 + m.x239 + m.x245 == 0)

m.c11 = Constraint(expr= - m.x129 + m.x130 - m.x234 + m.x240 + m.x246 == 0)

m.c12 = Constraint(expr= - m.x130 + m.x131 - m.x235 + m.x241 + m.x247 == 0)

m.c13 = Constraint(expr= - m.x131 + m.x132 - m.x236 + m.x242 + m.x248 == 0)

m.c14 = Constraint(expr= - m.x132 + m.x133 - m.x237 + m.x243 + m.x249 == 0)

m.c15 = Constraint(expr= - m.x133 + m.x134 - m.x238 + m.x244 + m.x250 == 0)

m.c16 = Constraint(expr=   m.x135 == 0)

m.c17 = Constraint(expr= - m.x135 + m.x136 - m.x239 + m.x251 == 0)

m.c18 = Constraint(expr= - m.x136 + m.x137 - m.x240 + m.x252 == 0)

m.c19 = Constraint(expr= - m.x137 + m.x138 - m.x241 + m.x253 == 0)

m.c20 = Constraint(expr= - m.x138 + m.x139 - m.x242 + m.x254 == 0)

m.c21 = Constraint(expr= - m.x139 + m.x140 - m.x243 + m.x255 == 0)

m.c22 = Constraint(expr= - m.x140 + m.x141 - m.x244 + m.x256 == 0)

m.c23 = Constraint(expr=   m.x142 == 0)

m.c24 = Constraint(expr= - m.x142 + m.x143 - m.x245 + m.x257 + m.x263 == 0)

m.c25 = Constraint(expr= - m.x143 + m.x144 - m.x246 + m.x258 + m.x264 == 0)

m.c26 = Constraint(expr= - m.x144 + m.x145 - m.x247 + m.x259 + m.x265 == 0)

m.c27 = Constraint(expr= - m.x145 + m.x146 - m.x248 + m.x260 + m.x266 == 0)

m.c28 = Constraint(expr= - m.x146 + m.x147 - m.x249 + m.x261 + m.x267 == 0)

m.c29 = Constraint(expr= - m.x147 + m.x148 - m.x250 + m.x262 + m.x268 == 0)

m.c30 = Constraint(expr=   m.x149 == 1000)

m.c31 = Constraint(expr= - m.x149 + m.x150 + m.x269 == 0)

m.c32 = Constraint(expr= - m.x150 + m.x151 + m.x270 == 0)

m.c33 = Constraint(expr= - m.x151 + m.x152 + m.x271 == 0)

m.c34 = Constraint(expr= - m.x152 + m.x153 + m.x272 == 0)

m.c35 = Constraint(expr= - m.x153 + m.x154 + m.x273 == 0)

m.c36 = Constraint(expr= - m.x154 + m.x155 + m.x274 == 0)

m.c37 = Constraint(expr=   m.x156 == 500)

m.c38 = Constraint(expr= - m.x156 + m.x157 - m.x269 + m.x275 + m.x281 + m.x287 == 0)

m.c39 = Constraint(expr= - m.x157 + m.x158 - m.x270 + m.x276 + m.x282 + m.x288 == 0)

m.c40 = Constraint(expr= - m.x158 + m.x159 - m.x271 + m.x277 + m.x283 + m.x289 == 0)

m.c41 = Constraint(expr= - m.x159 + m.x160 - m.x272 + m.x278 + m.x284 + m.x290 == 0)

m.c42 = Constraint(expr= - m.x160 + m.x161 - m.x273 + m.x279 + m.x285 + m.x291 == 0)

m.c43 = Constraint(expr= - m.x161 + m.x162 - m.x274 + m.x280 + m.x286 + m.x292 == 0)

m.c44 = Constraint(expr=   m.x163 == 0)

m.c45 = Constraint(expr= - m.x163 + m.x164 - m.x275 + m.x293 == 0)

m.c46 = Constraint(expr= - m.x164 + m.x165 - m.x276 + m.x294 == 0)

m.c47 = Constraint(expr= - m.x165 + m.x166 - m.x277 + m.x295 == 0)

m.c48 = Constraint(expr= - m.x166 + m.x167 - m.x278 + m.x296 == 0)

m.c49 = Constraint(expr= - m.x167 + m.x168 - m.x279 + m.x297 == 0)

m.c50 = Constraint(expr= - m.x168 + m.x169 - m.x280 + m.x298 == 0)

m.c51 = Constraint(expr=   m.x170 == 0)

m.c52 = Constraint(expr= - m.x170 + m.x171 - m.x281 + m.x299 + m.x305 == 0)

m.c53 = Constraint(expr= - m.x171 + m.x172 - m.x282 + m.x300 + m.x306 == 0)

m.c54 = Constraint(expr= - m.x172 + m.x173 - m.x283 + m.x301 + m.x307 == 0)

m.c55 = Constraint(expr= - m.x173 + m.x174 - m.x284 + m.x302 + m.x308 == 0)

m.c56 = Constraint(expr= - m.x174 + m.x175 - m.x285 + m.x303 + m.x309 == 0)

m.c57 = Constraint(expr= - m.x175 + m.x176 - m.x286 + m.x304 + m.x310 == 0)

m.c58 = Constraint(expr=   m.x177 == 0)

m.c59 = Constraint(expr= - m.x177 + m.x178 - m.x287 + m.x311 == 0)

m.c60 = Constraint(expr= - m.x178 + m.x179 - m.x288 + m.x312 == 0)

m.c61 = Constraint(expr= - m.x179 + m.x180 - m.x289 + m.x313 == 0)

m.c62 = Constraint(expr= - m.x180 + m.x181 - m.x290 + m.x314 == 0)

m.c63 = Constraint(expr= - m.x181 + m.x182 - m.x291 + m.x315 == 0)

m.c64 = Constraint(expr= - m.x182 + m.x183 - m.x292 + m.x316 == 0)

m.c65 = Constraint(expr=   m.x184 == 1000)

m.c66 = Constraint(expr= - m.x184 + m.x185 + m.x317 == 0)

m.c67 = Constraint(expr= - m.x185 + m.x186 + m.x318 == 0)

m.c68 = Constraint(expr= - m.x186 + m.x187 + m.x319 == 0)

m.c69 = Constraint(expr= - m.x187 + m.x188 + m.x320 == 0)

m.c70 = Constraint(expr= - m.x188 + m.x189 + m.x321 == 0)

m.c71 = Constraint(expr= - m.x189 + m.x190 + m.x322 == 0)

m.c72 = Constraint(expr=   m.x191 == 700)

m.c73 = Constraint(expr= - m.x191 + m.x192 - m.x317 + m.x323 + m.x329 == 0)

m.c74 = Constraint(expr= - m.x192 + m.x193 - m.x318 + m.x324 + m.x330 == 0)

m.c75 = Constraint(expr= - m.x193 + m.x194 - m.x319 + m.x325 + m.x331 == 0)

m.c76 = Constraint(expr= - m.x194 + m.x195 - m.x320 + m.x326 + m.x332 == 0)

m.c77 = Constraint(expr= - m.x195 + m.x196 - m.x321 + m.x327 + m.x333 == 0)

m.c78 = Constraint(expr= - m.x196 + m.x197 - m.x322 + m.x328 + m.x334 == 0)

m.c79 = Constraint(expr=   m.x198 == 0)

m.c80 = Constraint(expr= - m.x198 + m.x199 - m.x323 + m.x335 + m.x341 == 0)

m.c81 = Constraint(expr= - m.x199 + m.x200 - m.x324 + m.x336 + m.x342 == 0)

m.c82 = Constraint(expr= - m.x200 + m.x201 - m.x325 + m.x337 + m.x343 == 0)

m.c83 = Constraint(expr= - m.x201 + m.x202 - m.x326 + m.x338 + m.x344 == 0)

m.c84 = Constraint(expr= - m.x202 + m.x203 - m.x327 + m.x339 + m.x345 == 0)

m.c85 = Constraint(expr= - m.x203 + m.x204 - m.x328 + m.x340 + m.x346 == 0)

m.c86 = Constraint(expr=   m.x205 == 0)

m.c87 = Constraint(expr= - m.x205 + m.x206 - m.x329 + m.x347 == 0)

m.c88 = Constraint(expr= - m.x206 + m.x207 - m.x330 + m.x348 == 0)

m.c89 = Constraint(expr= - m.x207 + m.x208 - m.x331 + m.x349 == 0)

m.c90 = Constraint(expr= - m.x208 + m.x209 - m.x332 + m.x350 == 0)

m.c91 = Constraint(expr= - m.x209 + m.x210 - m.x333 + m.x351 == 0)

m.c92 = Constraint(expr= - m.x210 + m.x211 - m.x334 + m.x352 == 0)

m.c93 = Constraint(expr=   m.x212 == 300)

m.c94 = Constraint(expr= - m.x212 + m.x213 + m.x353 == 0)

m.c95 = Constraint(expr= - m.x213 + m.x214 + m.x354 == 0)

m.c96 = Constraint(expr= - m.x214 + m.x215 + m.x355 == 0)

m.c97 = Constraint(expr= - m.x215 + m.x216 + m.x356 == 0)

m.c98 = Constraint(expr= - m.x216 + m.x217 + m.x357 == 0)

m.c99 = Constraint(expr= - m.x217 + m.x218 + m.x358 == 0)

m.c100 = Constraint(expr=   m.x219 == 500)

m.c101 = Constraint(expr= - m.x219 + m.x220 + m.x359 + m.x365 == 0)

m.c102 = Constraint(expr= - m.x220 + m.x221 + m.x360 + m.x366 == 0)

m.c103 = Constraint(expr= - m.x221 + m.x222 + m.x361 + m.x367 == 0)

m.c104 = Constraint(expr= - m.x222 + m.x223 + m.x362 + m.x368 == 0)

m.c105 = Constraint(expr= - m.x223 + m.x224 + m.x363 + m.x369 == 0)

m.c106 = Constraint(expr= - m.x224 + m.x225 + m.x364 + m.x370 == 0)

m.c107 = Constraint(expr=   m.x226 == 300)

m.c108 = Constraint(expr= - m.x226 + m.x227 + m.x371 == 0)

m.c109 = Constraint(expr= - m.x227 + m.x228 + m.x372 == 0)

m.c110 = Constraint(expr= - m.x228 + m.x229 + m.x373 == 0)

m.c111 = Constraint(expr= - m.x229 + m.x230 + m.x374 == 0)

m.c112 = Constraint(expr= - m.x230 + m.x231 + m.x375 == 0)

m.c113 = Constraint(expr= - m.x231 + m.x232 + m.x376 == 0)

m.c114 = Constraint(expr=   m.x129 <= 1000)

m.c115 = Constraint(expr=   m.x130 <= 1000)

m.c116 = Constraint(expr=   m.x131 <= 1000)

m.c117 = Constraint(expr=   m.x132 <= 1000)

m.c118 = Constraint(expr=   m.x133 <= 1000)

m.c119 = Constraint(expr=   m.x134 <= 1000)

m.c120 = Constraint(expr=   m.x157 <= 1000)

m.c121 = Constraint(expr=   m.x158 <= 1000)

m.c122 = Constraint(expr=   m.x159 <= 1000)

m.c123 = Constraint(expr=   m.x160 <= 1000)

m.c124 = Constraint(expr=   m.x161 <= 1000)

m.c125 = Constraint(expr=   m.x162 <= 1000)

m.c126 = Constraint(expr=   m.x192 <= 1000)

m.c127 = Constraint(expr=   m.x193 <= 1000)

m.c128 = Constraint(expr=   m.x194 <= 1000)

m.c129 = Constraint(expr=   m.x195 <= 1000)

m.c130 = Constraint(expr=   m.x196 <= 1000)

m.c131 = Constraint(expr=   m.x197 <= 1000)

m.c132 = Constraint(expr=   m.x136 + m.x164 + m.x213 <= 1000)

m.c133 = Constraint(expr=   m.x137 + m.x165 + m.x214 <= 1000)

m.c134 = Constraint(expr=   m.x138 + m.x166 + m.x215 <= 1000)

m.c135 = Constraint(expr=   m.x139 + m.x167 + m.x216 <= 1000)

m.c136 = Constraint(expr=   m.x140 + m.x168 + m.x217 <= 1000)

m.c137 = Constraint(expr=   m.x141 + m.x169 + m.x218 <= 1000)

m.c138 = Constraint(expr=   m.x143 + m.x171 + m.x199 + m.x220 <= 1000)

m.c139 = Constraint(expr=   m.x144 + m.x172 + m.x200 + m.x221 <= 1000)

m.c140 = Constraint(expr=   m.x145 + m.x173 + m.x201 + m.x222 <= 1000)

m.c141 = Constraint(expr=   m.x146 + m.x174 + m.x202 + m.x223 <= 1000)

m.c142 = Constraint(expr=   m.x147 + m.x175 + m.x203 + m.x224 <= 1000)

m.c143 = Constraint(expr=   m.x148 + m.x176 + m.x204 + m.x225 <= 1000)

m.c144 = Constraint(expr=   m.x178 + m.x206 + m.x227 <= 1000)

m.c145 = Constraint(expr=   m.x179 + m.x207 + m.x228 <= 1000)

m.c146 = Constraint(expr=   m.x180 + m.x208 + m.x229 <= 1000)

m.c147 = Constraint(expr=   m.x181 + m.x209 + m.x230 <= 1000)

m.c148 = Constraint(expr=   m.x182 + m.x210 + m.x231 <= 1000)

m.c149 = Constraint(expr=   m.x183 + m.x211 + m.x232 <= 1000)

m.c150 = Constraint(expr=   m.x129 >= 0)

m.c151 = Constraint(expr=   m.x130 >= 0)

m.c152 = Constraint(expr=   m.x131 >= 0)

m.c153 = Constraint(expr=   m.x132 >= 0)

m.c154 = Constraint(expr=   m.x133 >= 0)

m.c155 = Constraint(expr=   m.x134 >= 0)

m.c156 = Constraint(expr=   m.x157 >= 0)

m.c157 = Constraint(expr=   m.x158 >= 0)

m.c158 = Constraint(expr=   m.x159 >= 0)

m.c159 = Constraint(expr=   m.x160 >= 0)

m.c160 = Constraint(expr=   m.x161 >= 0)

m.c161 = Constraint(expr=   m.x162 >= 0)

m.c162 = Constraint(expr=   m.x192 >= 0)

m.c163 = Constraint(expr=   m.x193 >= 0)

m.c164 = Constraint(expr=   m.x194 >= 0)

m.c165 = Constraint(expr=   m.x195 >= 0)

m.c166 = Constraint(expr=   m.x196 >= 0)

m.c167 = Constraint(expr=   m.x197 >= 0)

m.c168 = Constraint(expr=   m.x136 + m.x164 + m.x213 >= 0)

m.c169 = Constraint(expr=   m.x137 + m.x165 + m.x214 >= 0)

m.c170 = Constraint(expr=   m.x138 + m.x166 + m.x215 >= 0)

m.c171 = Constraint(expr=   m.x139 + m.x167 + m.x216 >= 0)

m.c172 = Constraint(expr=   m.x140 + m.x168 + m.x217 >= 0)

m.c173 = Constraint(expr=   m.x141 + m.x169 + m.x218 >= 0)

m.c174 = Constraint(expr=   m.x143 + m.x171 + m.x199 + m.x220 >= 0)

m.c175 = Constraint(expr=   m.x144 + m.x172 + m.x200 + m.x221 >= 0)

m.c176 = Constraint(expr=   m.x145 + m.x173 + m.x201 + m.x222 >= 0)

m.c177 = Constraint(expr=   m.x146 + m.x174 + m.x202 + m.x223 >= 0)

m.c178 = Constraint(expr=   m.x147 + m.x175 + m.x203 + m.x224 >= 0)

m.c179 = Constraint(expr=   m.x148 + m.x176 + m.x204 + m.x225 >= 0)

m.c180 = Constraint(expr=   m.x178 + m.x206 + m.x227 >= 0)

m.c181 = Constraint(expr=   m.x179 + m.x207 + m.x228 >= 0)

m.c182 = Constraint(expr=   m.x180 + m.x208 + m.x229 >= 0)

m.c183 = Constraint(expr=   m.x181 + m.x209 + m.x230 >= 0)

m.c184 = Constraint(expr=   m.x182 + m.x210 + m.x231 >= 0)

m.c185 = Constraint(expr=   m.x183 + m.x211 + m.x232 >= 0)

m.c186 = Constraint(expr= - 0.01*m.x136 + 0.01*m.x164 - 0.0033*m.x213 <= 0)

m.c187 = Constraint(expr= - 0.01*m.x137 + 0.01*m.x165 - 0.0033*m.x214 <= 0)

m.c188 = Constraint(expr= - 0.01*m.x138 + 0.01*m.x166 - 0.0033*m.x215 <= 0)

m.c189 = Constraint(expr= - 0.01*m.x139 + 0.01*m.x167 - 0.0033*m.x216 <= 0)

m.c190 = Constraint(expr= - 0.01*m.x140 + 0.01*m.x168 - 0.0033*m.x217 <= 0)

m.c191 = Constraint(expr= - 0.01*m.x141 + 0.01*m.x169 - 0.0033*m.x218 <= 0)

m.c192 = Constraint(expr=   0.002*m.x136 - 0.018*m.x164 - 0.0047*m.x213 <= 0)

m.c193 = Constraint(expr=   0.002*m.x137 - 0.018*m.x165 - 0.0047*m.x214 <= 0)

m.c194 = Constraint(expr=   0.002*m.x138 - 0.018*m.x166 - 0.0047*m.x215 <= 0)

m.c195 = Constraint(expr=   0.002*m.x139 - 0.018*m.x167 - 0.0047*m.x216 <= 0)

m.c196 = Constraint(expr=   0.002*m.x140 - 0.018*m.x168 - 0.0047*m.x217 <= 0)

m.c197 = Constraint(expr=   0.002*m.x141 - 0.018*m.x169 - 0.0047*m.x218 <= 0)

m.c198 = Constraint(expr= - 0.025*m.x143 - 0.005*m.x171 + 0.015*m.x199 - 0.005*m.x220 <= 0)

m.c199 = Constraint(expr= - 0.025*m.x144 - 0.005*m.x172 + 0.015*m.x200 - 0.005*m.x221 <= 0)

m.c200 = Constraint(expr= - 0.025*m.x145 - 0.005*m.x173 + 0.015*m.x201 - 0.005*m.x222 <= 0)

m.c201 = Constraint(expr= - 0.025*m.x146 - 0.005*m.x174 + 0.015*m.x202 - 0.005*m.x223 <= 0)

m.c202 = Constraint(expr= - 0.025*m.x147 - 0.005*m.x175 + 0.015*m.x203 - 0.005*m.x224 <= 0)

m.c203 = Constraint(expr= - 0.025*m.x148 - 0.005*m.x176 + 0.015*m.x204 - 0.005*m.x225 <= 0)

m.c204 = Constraint(expr=   0.013*m.x143 - 0.007*m.x171 - 0.017*m.x199 - 0.004*m.x220 <= 0)

m.c205 = Constraint(expr=   0.013*m.x144 - 0.007*m.x172 - 0.017*m.x200 - 0.004*m.x221 <= 0)

m.c206 = Constraint(expr=   0.013*m.x145 - 0.007*m.x173 - 0.017*m.x201 - 0.004*m.x222 <= 0)

m.c207 = Constraint(expr=   0.013*m.x146 - 0.007*m.x174 - 0.017*m.x202 - 0.004*m.x223 <= 0)

m.c208 = Constraint(expr=   0.013*m.x147 - 0.007*m.x175 - 0.017*m.x203 - 0.004*m.x224 <= 0)

m.c209 = Constraint(expr=   0.013*m.x148 - 0.007*m.x176 - 0.017*m.x204 - 0.004*m.x225 <= 0)

m.c210 = Constraint(expr= - 0.018*m.x178 + 0.002*m.x206 - 0.0047*m.x227 <= 0)

m.c211 = Constraint(expr= - 0.018*m.x179 + 0.002*m.x207 - 0.0047*m.x228 <= 0)

m.c212 = Constraint(expr= - 0.018*m.x180 + 0.002*m.x208 - 0.0047*m.x229 <= 0)

m.c213 = Constraint(expr= - 0.018*m.x181 + 0.002*m.x209 - 0.0047*m.x230 <= 0)

m.c214 = Constraint(expr= - 0.018*m.x182 + 0.002*m.x210 - 0.0047*m.x231 <= 0)

m.c215 = Constraint(expr= - 0.018*m.x183 + 0.002*m.x211 - 0.0047*m.x232 <= 0)

m.c216 = Constraint(expr=   0.002*m.x178 - 0.008*m.x206 - 0.0047*m.x227 <= 0)

m.c217 = Constraint(expr=   0.002*m.x179 - 0.008*m.x207 - 0.0047*m.x228 <= 0)

m.c218 = Constraint(expr=   0.002*m.x180 - 0.008*m.x208 - 0.0047*m.x229 <= 0)

m.c219 = Constraint(expr=   0.002*m.x181 - 0.008*m.x209 - 0.0047*m.x230 <= 0)

m.c220 = Constraint(expr=   0.002*m.x182 - 0.008*m.x210 - 0.0047*m.x231 <= 0)

m.c221 = Constraint(expr=   0.002*m.x183 - 0.008*m.x211 - 0.0047*m.x232 <= 0)

m.c222 = Constraint(expr=   0.02*m.x164 + 0.0067*m.x213 >= 0)

m.c223 = Constraint(expr=   0.02*m.x165 + 0.0067*m.x214 >= 0)

m.c224 = Constraint(expr=   0.02*m.x166 + 0.0067*m.x215 >= 0)

m.c225 = Constraint(expr=   0.02*m.x167 + 0.0067*m.x216 >= 0)

m.c226 = Constraint(expr=   0.02*m.x168 + 0.0067*m.x217 >= 0)

m.c227 = Constraint(expr=   0.02*m.x169 + 0.0067*m.x218 >= 0)

m.c228 = Constraint(expr=   0.01*m.x136 - 0.01*m.x164 + 0.0033*m.x213 >= 0)

m.c229 = Constraint(expr=   0.01*m.x137 - 0.01*m.x165 + 0.0033*m.x214 >= 0)

m.c230 = Constraint(expr=   0.01*m.x138 - 0.01*m.x166 + 0.0033*m.x215 >= 0)

m.c231 = Constraint(expr=   0.01*m.x139 - 0.01*m.x167 + 0.0033*m.x216 >= 0)

m.c232 = Constraint(expr=   0.01*m.x140 - 0.01*m.x168 + 0.0033*m.x217 >= 0)

m.c233 = Constraint(expr=   0.01*m.x141 - 0.01*m.x169 + 0.0033*m.x218 >= 0)

m.c234 = Constraint(expr= - 0.015*m.x143 + 0.005*m.x171 + 0.025*m.x199 + 0.005*m.x220 >= 0)

m.c235 = Constraint(expr= - 0.015*m.x144 + 0.005*m.x172 + 0.025*m.x200 + 0.005*m.x221 >= 0)

m.c236 = Constraint(expr= - 0.015*m.x145 + 0.005*m.x173 + 0.025*m.x201 + 0.005*m.x222 >= 0)

m.c237 = Constraint(expr= - 0.015*m.x146 + 0.005*m.x174 + 0.025*m.x202 + 0.005*m.x223 >= 0)

m.c238 = Constraint(expr= - 0.015*m.x147 + 0.005*m.x175 + 0.025*m.x203 + 0.005*m.x224 >= 0)

m.c239 = Constraint(expr= - 0.015*m.x148 + 0.005*m.x176 + 0.025*m.x204 + 0.005*m.x225 >= 0)

m.c240 = Constraint(expr=   0.022*m.x143 + 0.002*m.x171 - 0.008*m.x199 + 0.005*m.x220 >= 0)

m.c241 = Constraint(expr=   0.022*m.x144 + 0.002*m.x172 - 0.008*m.x200 + 0.005*m.x221 >= 0)

m.c242 = Constraint(expr=   0.022*m.x145 + 0.002*m.x173 - 0.008*m.x201 + 0.005*m.x222 >= 0)

m.c243 = Constraint(expr=   0.022*m.x146 + 0.002*m.x174 - 0.008*m.x202 + 0.005*m.x223 >= 0)

m.c244 = Constraint(expr=   0.022*m.x147 + 0.002*m.x175 - 0.008*m.x203 + 0.005*m.x224 >= 0)

m.c245 = Constraint(expr=   0.022*m.x148 + 0.002*m.x176 - 0.008*m.x204 + 0.005*m.x225 >= 0)

m.c246 = Constraint(expr= - 0.01*m.x178 + 0.01*m.x206 + 0.0033*m.x227 >= 0)

m.c247 = Constraint(expr= - 0.01*m.x179 + 0.01*m.x207 + 0.0033*m.x228 >= 0)

m.c248 = Constraint(expr= - 0.01*m.x180 + 0.01*m.x208 + 0.0033*m.x229 >= 0)

m.c249 = Constraint(expr= - 0.01*m.x181 + 0.01*m.x209 + 0.0033*m.x230 >= 0)

m.c250 = Constraint(expr= - 0.01*m.x182 + 0.01*m.x210 + 0.0033*m.x231 >= 0)

m.c251 = Constraint(expr= - 0.01*m.x183 + 0.01*m.x211 + 0.0033*m.x232 >= 0)

m.c252 = Constraint(expr=   0.01*m.x178 + 0.0033*m.x227 >= 0)

m.c253 = Constraint(expr=   0.01*m.x179 + 0.0033*m.x228 >= 0)

m.c254 = Constraint(expr=   0.01*m.x180 + 0.0033*m.x229 >= 0)

m.c255 = Constraint(expr=   0.01*m.x181 + 0.0033*m.x230 >= 0)

m.c256 = Constraint(expr=   0.01*m.x182 + 0.0033*m.x231 >= 0)

m.c257 = Constraint(expr=   0.01*m.x183 + 0.0033*m.x232 >= 0)

m.c258 = Constraint(expr=   m.b19 + m.b61 <= 1)

m.c259 = Constraint(expr=   m.b20 + m.b62 <= 1)

m.c260 = Constraint(expr=   m.b21 + m.b63 <= 1)

m.c261 = Constraint(expr=   m.b22 + m.b64 <= 1)

m.c262 = Constraint(expr=   m.b23 + m.b65 <= 1)

m.c263 = Constraint(expr=   m.b24 + m.b66 <= 1)

m.c264 = Constraint(expr=   m.b31 + m.b61 <= 1)

m.c265 = Constraint(expr=   m.b32 + m.b62 <= 1)

m.c266 = Constraint(expr=   m.b33 + m.b63 <= 1)

m.c267 = Constraint(expr=   m.b34 + m.b64 <= 1)

m.c268 = Constraint(expr=   m.b35 + m.b65 <= 1)

m.c269 = Constraint(expr=   m.b36 + m.b66 <= 1)

m.c270 = Constraint(expr=   m.b25 + m.b67 + m.b73 <= 1)

m.c271 = Constraint(expr=   m.b26 + m.b68 + m.b74 <= 1)

m.c272 = Constraint(expr=   m.b27 + m.b69 + m.b75 <= 1)

m.c273 = Constraint(expr=   m.b28 + m.b70 + m.b76 <= 1)

m.c274 = Constraint(expr=   m.b29 + m.b71 + m.b77 <= 1)

m.c275 = Constraint(expr=   m.b30 + m.b72 + m.b78 <= 1)

m.c276 = Constraint(expr=   m.b37 + m.b67 + m.b73 <= 1)

m.c277 = Constraint(expr=   m.b38 + m.b68 + m.b74 <= 1)

m.c278 = Constraint(expr=   m.b39 + m.b69 + m.b75 <= 1)

m.c279 = Constraint(expr=   m.b40 + m.b70 + m.b76 <= 1)

m.c280 = Constraint(expr=   m.b41 + m.b71 + m.b77 <= 1)

m.c281 = Constraint(expr=   m.b42 + m.b72 + m.b78 <= 1)

m.c282 = Constraint(expr=   m.b49 + m.b67 + m.b73 <= 1)

m.c283 = Constraint(expr=   m.b50 + m.b68 + m.b74 <= 1)

m.c284 = Constraint(expr=   m.b51 + m.b69 + m.b75 <= 1)

m.c285 = Constraint(expr=   m.b52 + m.b70 + m.b76 <= 1)

m.c286 = Constraint(expr=   m.b53 + m.b71 + m.b77 <= 1)

m.c287 = Constraint(expr=   m.b54 + m.b72 + m.b78 <= 1)

m.c288 = Constraint(expr=   m.b43 + m.b79 <= 1)

m.c289 = Constraint(expr=   m.b44 + m.b80 <= 1)

m.c290 = Constraint(expr=   m.b45 + m.b81 <= 1)

m.c291 = Constraint(expr=   m.b46 + m.b82 <= 1)

m.c292 = Constraint(expr=   m.b47 + m.b83 <= 1)

m.c293 = Constraint(expr=   m.b48 + m.b84 <= 1)

m.c294 = Constraint(expr=   m.b55 + m.b79 <= 1)

m.c295 = Constraint(expr=   m.b56 + m.b80 <= 1)

m.c296 = Constraint(expr=   m.b57 + m.b81 <= 1)

m.c297 = Constraint(expr=   m.b58 + m.b82 <= 1)

m.c298 = Constraint(expr=   m.b59 + m.b83 <= 1)

m.c299 = Constraint(expr=   m.b60 + m.b84 <= 1)

m.c300 = Constraint(expr=   m.x127 == 0)

m.c301 = Constraint(expr=   m.x155 == 0)

m.c302 = Constraint(expr=   m.x190 == 0)

m.c303 = Constraint(expr=   m.x251 + m.x252 + m.x253 + m.x254 + m.x255 + m.x256 + m.x293 + m.x294 + m.x295 + m.x296
                          + m.x297 + m.x298 + m.x353 + m.x354 + m.x355 + m.x356 + m.x357 + m.x358 == 1000)

m.c304 = Constraint(expr=   m.x257 + m.x258 + m.x259 + m.x260 + m.x261 + m.x262 + m.x263 + m.x264 + m.x265 + m.x266
                          + m.x267 + m.x268 + m.x299 + m.x300 + m.x301 + m.x302 + m.x303 + m.x304 + m.x305 + m.x306
                          + m.x307 + m.x308 + m.x309 + m.x310 + m.x335 + m.x336 + m.x337 + m.x338 + m.x339 + m.x340
                          + m.x341 + m.x342 + m.x343 + m.x344 + m.x345 + m.x346 + m.x359 + m.x360 + m.x361 + m.x362
                          + m.x363 + m.x364 + m.x365 + m.x366 + m.x367 + m.x368 + m.x369 + m.x370 == 1000)

m.c305 = Constraint(expr=   m.x311 + m.x312 + m.x313 + m.x314 + m.x315 + m.x316 + m.x347 + m.x348 + m.x349 + m.x350
                          + m.x351 + m.x352 + m.x371 + m.x372 + m.x373 + m.x374 + m.x375 + m.x376 == 1000)

m.c306 = Constraint(expr=   m.b85 + m.b86 + m.b88 + m.b91 == 1)

m.c307 = Constraint(expr=   m.b87 + m.b89 + m.b92 + m.b94 == 1)

m.c308 = Constraint(expr=   m.b90 + m.b93 + m.b95 + m.b96 == 1)

m.c309 = Constraint(expr=   m.b97 + m.b98 + m.b100 + m.b103 == 1)

m.c310 = Constraint(expr=   m.b99 + m.b101 + m.b104 + m.b106 == 1)

m.c311 = Constraint(expr=   m.b102 + m.b105 + m.b107 + m.b108 == 1)

m.c312 = Constraint(expr=   m.b1 + m.b7 + m.b13 <= 1)

m.c313 = Constraint(expr=   m.b2 + m.b8 + m.b14 <= 1)

m.c314 = Constraint(expr=   m.b3 + m.b9 + m.b15 <= 1)

m.c315 = Constraint(expr=   m.b4 + m.b10 + m.b16 <= 1)

m.c316 = Constraint(expr=   m.b5 + m.b11 + m.b17 <= 1)

m.c317 = Constraint(expr=   m.b6 + m.b12 + m.b18 <= 1)

m.c318 = Constraint(expr=   m.b61 + m.b67 == 1)

m.c319 = Constraint(expr=   m.b62 + m.b68 == 1)

m.c320 = Constraint(expr=   m.b63 + m.b69 == 1)

m.c321 = Constraint(expr=   m.b64 + m.b70 == 1)

m.c322 = Constraint(expr=   m.b65 + m.b71 == 1)

m.c323 = Constraint(expr=   m.b66 + m.b72 == 1)

m.c324 = Constraint(expr=   m.b73 + m.b79 == 1)

m.c325 = Constraint(expr=   m.b74 + m.b80 == 1)

m.c326 = Constraint(expr=   m.b75 + m.b81 == 1)

m.c327 = Constraint(expr=   m.b76 + m.b82 == 1)

m.c328 = Constraint(expr=   m.b77 + m.b83 == 1)

m.c329 = Constraint(expr=   m.b78 + m.b84 == 1)

m.c330 = Constraint(expr=   m.b1 - m.b85 <= 0)

m.c331 = Constraint(expr=   m.b2 - m.b85 - m.b86 <= 0)

m.c332 = Constraint(expr=   m.b3 - m.b85 - m.b86 - m.b88 <= 0)

m.c333 = Constraint(expr=   m.b4 - m.b85 - m.b86 - m.b88 - m.b91 <= 0)

m.c334 = Constraint(expr=   m.b5 - m.b85 - m.b86 - m.b88 - m.b91 <= 0)

m.c335 = Constraint(expr=   m.b6 - m.b85 - m.b86 - m.b88 - m.b91 <= 0)

m.c336 = Constraint(expr=   m.b7 <= 0)

m.c337 = Constraint(expr=   m.b8 - m.b87 <= 0)

m.c338 = Constraint(expr=   m.b9 - m.b87 - m.b89 <= 0)

m.c339 = Constraint(expr=   m.b10 - m.b87 - m.b89 - m.b92 <= 0)

m.c340 = Constraint(expr=   m.b11 - m.b87 - m.b89 - m.b92 - m.b94 <= 0)

m.c341 = Constraint(expr=   m.b12 - m.b87 - m.b89 - m.b92 - m.b94 <= 0)

m.c342 = Constraint(expr=   m.b13 <= 0)

m.c343 = Constraint(expr=   m.b14 <= 0)

m.c344 = Constraint(expr=   m.b15 - m.b90 <= 0)

m.c345 = Constraint(expr=   m.b16 - m.b90 - m.b93 <= 0)

m.c346 = Constraint(expr=   m.b17 - m.b90 - m.b93 - m.b95 <= 0)

m.c347 = Constraint(expr=   m.b18 - m.b90 - m.b93 - m.b95 - m.b96 <= 0)

m.c348 = Constraint(expr=   m.b1 - m.b97 - m.b98 - m.b100 - m.b103 <= 0)

m.c349 = Constraint(expr=   m.b2 - m.b98 - m.b100 - m.b103 <= 0)

m.c350 = Constraint(expr=   m.b3 - m.b100 - m.b103 <= 0)

m.c351 = Constraint(expr=   m.b4 - m.b103 <= 0)

m.c352 = Constraint(expr=   m.b5 <= 0)

m.c353 = Constraint(expr=   m.b6 <= 0)

m.c354 = Constraint(expr=   m.b7 - m.b99 - m.b101 - m.b104 - m.b106 <= 0)

m.c355 = Constraint(expr=   m.b8 - m.b99 - m.b101 - m.b104 - m.b106 <= 0)

m.c356 = Constraint(expr=   m.b9 - m.b101 - m.b104 - m.b106 <= 0)

m.c357 = Constraint(expr=   m.b10 - m.b104 - m.b106 <= 0)

m.c358 = Constraint(expr=   m.b11 - m.b106 <= 0)

m.c359 = Constraint(expr=   m.b12 <= 0)

m.c360 = Constraint(expr=   m.b13 - m.b102 - m.b105 - m.b107 - m.b108 <= 0)

m.c361 = Constraint(expr=   m.b14 - m.b102 - m.b105 - m.b107 - m.b108 <= 0)

m.c362 = Constraint(expr=   m.b15 - m.b102 - m.b105 - m.b107 - m.b108 <= 0)

m.c363 = Constraint(expr=   m.b16 - m.b105 - m.b107 - m.b108 <= 0)

m.c364 = Constraint(expr=   m.b17 - m.b107 - m.b108 <= 0)

m.c365 = Constraint(expr=   m.b18 - m.b108 <= 0)

m.c366 = Constraint(expr= - m.b61 - m.b68 + m.x109 >= -1)

m.c367 = Constraint(expr= - m.b62 - m.b69 + m.x110 >= -1)

m.c368 = Constraint(expr= - m.b63 - m.b70 + m.x111 >= -1)

m.c369 = Constraint(expr= - m.b64 - m.b71 + m.x112 >= -1)

m.c370 = Constraint(expr= - m.b65 - m.b72 + m.x113 >= -1)

m.c371 = Constraint(expr= - m.b73 - m.b80 + m.x114 >= -1)

m.c372 = Constraint(expr= - m.b74 - m.b81 + m.x115 >= -1)

m.c373 = Constraint(expr= - m.b75 - m.b82 + m.x116 >= -1)

m.c374 = Constraint(expr= - m.b76 - m.b83 + m.x117 >= -1)

m.c375 = Constraint(expr= - m.b77 - m.b84 + m.x118 >= -1)

m.c376 = Constraint(expr= - m.b62 - m.b67 + m.x109 >= -1)

m.c377 = Constraint(expr= - m.b63 - m.b68 + m.x110 >= -1)

m.c378 = Constraint(expr= - m.b64 - m.b69 + m.x111 >= -1)

m.c379 = Constraint(expr= - m.b65 - m.b70 + m.x112 >= -1)

m.c380 = Constraint(expr= - m.b66 - m.b71 + m.x113 >= -1)

m.c381 = Constraint(expr= - m.b74 - m.b79 + m.x114 >= -1)

m.c382 = Constraint(expr= - m.b75 - m.b80 + m.x115 >= -1)

m.c383 = Constraint(expr= - m.b76 - m.b81 + m.x116 >= -1)

m.c384 = Constraint(expr= - m.b77 - m.b82 + m.x117 >= -1)

m.c385 = Constraint(expr= - m.b78 - m.b83 + m.x118 >= -1)

m.c386 = Constraint(expr=   m.x109 + m.x110 + m.x111 + m.x112 + m.x113 - m.x119 == -1)

m.c387 = Constraint(expr=   m.x114 + m.x115 + m.x116 + m.x117 + m.x118 - m.x120 == -1)

m.c388 = Constraint(expr= - 1000*m.b1 + m.x233 <= 0)

m.c389 = Constraint(expr= - 1000*m.b2 + m.x234 <= 0)

m.c390 = Constraint(expr= - 1000*m.b3 + m.x235 <= 0)

m.c391 = Constraint(expr= - 1000*m.b4 + m.x236 <= 0)

m.c392 = Constraint(expr= - 1000*m.b5 + m.x237 <= 0)

m.c393 = Constraint(expr= - 1000*m.b6 + m.x238 <= 0)

m.c394 = Constraint(expr= - 1000*m.b7 + m.x269 <= 0)

m.c395 = Constraint(expr= - 1000*m.b8 + m.x270 <= 0)

m.c396 = Constraint(expr= - 1000*m.b9 + m.x271 <= 0)

m.c397 = Constraint(expr= - 1000*m.b10 + m.x272 <= 0)

m.c398 = Constraint(expr= - 1000*m.b11 + m.x273 <= 0)

m.c399 = Constraint(expr= - 1000*m.b12 + m.x274 <= 0)

m.c400 = Constraint(expr= - 1000*m.b13 + m.x317 <= 0)

m.c401 = Constraint(expr= - 1000*m.b14 + m.x318 <= 0)

m.c402 = Constraint(expr= - 1000*m.b15 + m.x319 <= 0)

m.c403 = Constraint(expr= - 1000*m.b16 + m.x320 <= 0)

m.c404 = Constraint(expr= - 1000*m.b17 + m.x321 <= 0)

m.c405 = Constraint(expr= - 1000*m.b18 + m.x322 <= 0)

m.c406 = Constraint(expr= - 1000*m.b19 + m.x239 <= 0)

m.c407 = Constraint(expr= - 1000*m.b20 + m.x240 <= 0)

m.c408 = Constraint(expr= - 1000*m.b21 + m.x241 <= 0)

m.c409 = Constraint(expr= - 1000*m.b22 + m.x242 <= 0)

m.c410 = Constraint(expr= - 1000*m.b23 + m.x243 <= 0)

m.c411 = Constraint(expr= - 1000*m.b24 + m.x244 <= 0)

m.c412 = Constraint(expr= - 1000*m.b25 + m.x245 <= 0)

m.c413 = Constraint(expr= - 1000*m.b26 + m.x246 <= 0)

m.c414 = Constraint(expr= - 1000*m.b27 + m.x247 <= 0)

m.c415 = Constraint(expr= - 1000*m.b28 + m.x248 <= 0)

m.c416 = Constraint(expr= - 1000*m.b29 + m.x249 <= 0)

m.c417 = Constraint(expr= - 1000*m.b30 + m.x250 <= 0)

m.c418 = Constraint(expr= - 1000*m.b31 + m.x275 <= 0)

m.c419 = Constraint(expr= - 1000*m.b32 + m.x276 <= 0)

m.c420 = Constraint(expr= - 1000*m.b33 + m.x277 <= 0)

m.c421 = Constraint(expr= - 1000*m.b34 + m.x278 <= 0)

m.c422 = Constraint(expr= - 1000*m.b35 + m.x279 <= 0)

m.c423 = Constraint(expr= - 1000*m.b36 + m.x280 <= 0)

m.c424 = Constraint(expr= - 1000*m.b37 + m.x281 <= 0)

m.c425 = Constraint(expr= - 1000*m.b38 + m.x282 <= 0)

m.c426 = Constraint(expr= - 1000*m.b39 + m.x283 <= 0)

m.c427 = Constraint(expr= - 1000*m.b40 + m.x284 <= 0)

m.c428 = Constraint(expr= - 1000*m.b41 + m.x285 <= 0)

m.c429 = Constraint(expr= - 1000*m.b42 + m.x286 <= 0)

m.c430 = Constraint(expr= - 1000*m.b43 + m.x287 <= 0)

m.c431 = Constraint(expr= - 1000*m.b44 + m.x288 <= 0)

m.c432 = Constraint(expr= - 1000*m.b45 + m.x289 <= 0)

m.c433 = Constraint(expr= - 1000*m.b46 + m.x290 <= 0)

m.c434 = Constraint(expr= - 1000*m.b47 + m.x291 <= 0)

m.c435 = Constraint(expr= - 1000*m.b48 + m.x292 <= 0)

m.c436 = Constraint(expr= - 1000*m.b49 + m.x323 <= 0)

m.c437 = Constraint(expr= - 1000*m.b50 + m.x324 <= 0)

m.c438 = Constraint(expr= - 1000*m.b51 + m.x325 <= 0)

m.c439 = Constraint(expr= - 1000*m.b52 + m.x326 <= 0)

m.c440 = Constraint(expr= - 1000*m.b53 + m.x327 <= 0)

m.c441 = Constraint(expr= - 1000*m.b54 + m.x328 <= 0)

m.c442 = Constraint(expr= - 1000*m.b55 + m.x329 <= 0)

m.c443 = Constraint(expr= - 1000*m.b56 + m.x330 <= 0)

m.c444 = Constraint(expr= - 1000*m.b57 + m.x331 <= 0)

m.c445 = Constraint(expr= - 1000*m.b58 + m.x332 <= 0)

m.c446 = Constraint(expr= - 1000*m.b59 + m.x333 <= 0)

m.c447 = Constraint(expr= - 1000*m.b60 + m.x334 <= 0)

m.c448 = Constraint(expr= - 1000*m.b61 + m.x251 + m.x293 + m.x353 <= 0)

m.c449 = Constraint(expr= - 1000*m.b62 + m.x252 + m.x294 + m.x354 <= 0)

m.c450 = Constraint(expr= - 1000*m.b63 + m.x253 + m.x295 + m.x355 <= 0)

m.c451 = Constraint(expr= - 1000*m.b64 + m.x254 + m.x296 + m.x356 <= 0)

m.c452 = Constraint(expr= - 1000*m.b65 + m.x255 + m.x297 + m.x357 <= 0)

m.c453 = Constraint(expr= - 1000*m.b66 + m.x256 + m.x298 + m.x358 <= 0)

m.c454 = Constraint(expr= - 1000*m.b67 + m.x257 + m.x299 + m.x335 + m.x359 <= 0)

m.c455 = Constraint(expr= - 1000*m.b68 + m.x258 + m.x300 + m.x336 + m.x360 <= 0)

m.c456 = Constraint(expr= - 1000*m.b69 + m.x259 + m.x301 + m.x337 + m.x361 <= 0)

m.c457 = Constraint(expr= - 1000*m.b70 + m.x260 + m.x302 + m.x338 + m.x362 <= 0)

m.c458 = Constraint(expr= - 1000*m.b71 + m.x261 + m.x303 + m.x339 + m.x363 <= 0)

m.c459 = Constraint(expr= - 1000*m.b72 + m.x262 + m.x304 + m.x340 + m.x364 <= 0)

m.c460 = Constraint(expr= - 1000*m.b73 + m.x263 + m.x305 + m.x341 + m.x365 <= 0)

m.c461 = Constraint(expr= - 1000*m.b74 + m.x264 + m.x306 + m.x342 + m.x366 <= 0)

m.c462 = Constraint(expr= - 1000*m.b75 + m.x265 + m.x307 + m.x343 + m.x367 <= 0)

m.c463 = Constraint(expr= - 1000*m.b76 + m.x266 + m.x308 + m.x344 + m.x368 <= 0)

m.c464 = Constraint(expr= - 1000*m.b77 + m.x267 + m.x309 + m.x345 + m.x369 <= 0)

m.c465 = Constraint(expr= - 1000*m.b78 + m.x268 + m.x310 + m.x346 + m.x370 <= 0)

m.c466 = Constraint(expr= - 1000*m.b79 + m.x311 + m.x347 + m.x371 <= 0)

m.c467 = Constraint(expr= - 1000*m.b80 + m.x312 + m.x348 + m.x372 <= 0)

m.c468 = Constraint(expr= - 1000*m.b81 + m.x313 + m.x349 + m.x373 <= 0)

m.c469 = Constraint(expr= - 1000*m.b82 + m.x314 + m.x350 + m.x374 <= 0)

m.c470 = Constraint(expr= - 1000*m.b83 + m.x315 + m.x351 + m.x375 <= 0)

m.c471 = Constraint(expr= - 1000*m.b84 + m.x316 + m.x352 + m.x376 <= 0)

m.c472 = Constraint(expr= - m.b1 + m.x233 >= 0)

m.c473 = Constraint(expr= - m.b2 + m.x234 >= 0)

m.c474 = Constraint(expr= - m.b3 + m.x235 >= 0)

m.c475 = Constraint(expr= - m.b4 + m.x236 >= 0)

m.c476 = Constraint(expr= - m.b5 + m.x237 >= 0)

m.c477 = Constraint(expr= - m.b6 + m.x238 >= 0)

m.c478 = Constraint(expr= - m.b7 + m.x269 >= 0)

m.c479 = Constraint(expr= - m.b8 + m.x270 >= 0)

m.c480 = Constraint(expr= - m.b9 + m.x271 >= 0)

m.c481 = Constraint(expr= - m.b10 + m.x272 >= 0)

m.c482 = Constraint(expr= - m.b11 + m.x273 >= 0)

m.c483 = Constraint(expr= - m.b12 + m.x274 >= 0)

m.c484 = Constraint(expr= - m.b13 + m.x317 >= 0)

m.c485 = Constraint(expr= - m.b14 + m.x318 >= 0)

m.c486 = Constraint(expr= - m.b15 + m.x319 >= 0)

m.c487 = Constraint(expr= - m.b16 + m.x320 >= 0)

m.c488 = Constraint(expr= - m.b17 + m.x321 >= 0)

m.c489 = Constraint(expr= - m.b18 + m.x322 >= 0)

m.c490 = Constraint(expr= - m.b19 + m.x239 >= 0)

m.c491 = Constraint(expr= - m.b20 + m.x240 >= 0)

m.c492 = Constraint(expr= - m.b21 + m.x241 >= 0)

m.c493 = Constraint(expr= - m.b22 + m.x242 >= 0)

m.c494 = Constraint(expr= - m.b23 + m.x243 >= 0)

m.c495 = Constraint(expr= - m.b24 + m.x244 >= 0)

m.c496 = Constraint(expr= - m.b25 + m.x245 >= 0)

m.c497 = Constraint(expr= - m.b26 + m.x246 >= 0)

m.c498 = Constraint(expr= - m.b27 + m.x247 >= 0)

m.c499 = Constraint(expr= - m.b28 + m.x248 >= 0)

m.c500 = Constraint(expr= - m.b29 + m.x249 >= 0)

m.c501 = Constraint(expr= - m.b30 + m.x250 >= 0)

m.c502 = Constraint(expr= - m.b31 + m.x275 >= 0)

m.c503 = Constraint(expr= - m.b32 + m.x276 >= 0)

m.c504 = Constraint(expr= - m.b33 + m.x277 >= 0)

m.c505 = Constraint(expr= - m.b34 + m.x278 >= 0)

m.c506 = Constraint(expr= - m.b35 + m.x279 >= 0)

m.c507 = Constraint(expr= - m.b36 + m.x280 >= 0)

m.c508 = Constraint(expr= - m.b37 + m.x281 >= 0)

m.c509 = Constraint(expr= - m.b38 + m.x282 >= 0)

m.c510 = Constraint(expr= - m.b39 + m.x283 >= 0)

m.c511 = Constraint(expr= - m.b40 + m.x284 >= 0)

m.c512 = Constraint(expr= - m.b41 + m.x285 >= 0)

m.c513 = Constraint(expr= - m.b42 + m.x286 >= 0)

m.c514 = Constraint(expr= - m.b43 + m.x287 >= 0)

m.c515 = Constraint(expr= - m.b44 + m.x288 >= 0)

m.c516 = Constraint(expr= - m.b45 + m.x289 >= 0)

m.c517 = Constraint(expr= - m.b46 + m.x290 >= 0)

m.c518 = Constraint(expr= - m.b47 + m.x291 >= 0)

m.c519 = Constraint(expr= - m.b48 + m.x292 >= 0)

m.c520 = Constraint(expr= - m.b49 + m.x323 >= 0)

m.c521 = Constraint(expr= - m.b50 + m.x324 >= 0)

m.c522 = Constraint(expr= - m.b51 + m.x325 >= 0)

m.c523 = Constraint(expr= - m.b52 + m.x326 >= 0)

m.c524 = Constraint(expr= - m.b53 + m.x327 >= 0)

m.c525 = Constraint(expr= - m.b54 + m.x328 >= 0)

m.c526 = Constraint(expr= - m.b55 + m.x329 >= 0)

m.c527 = Constraint(expr= - m.b56 + m.x330 >= 0)

m.c528 = Constraint(expr= - m.b57 + m.x331 >= 0)

m.c529 = Constraint(expr= - m.b58 + m.x332 >= 0)

m.c530 = Constraint(expr= - m.b59 + m.x333 >= 0)

m.c531 = Constraint(expr= - m.b60 + m.x334 >= 0)

m.c532 = Constraint(expr= - m.b61 + m.x251 + m.x293 + m.x353 >= 0)

m.c533 = Constraint(expr= - m.b62 + m.x252 + m.x294 + m.x354 >= 0)

m.c534 = Constraint(expr= - m.b63 + m.x253 + m.x295 + m.x355 >= 0)

m.c535 = Constraint(expr= - m.b64 + m.x254 + m.x296 + m.x356 >= 0)

m.c536 = Constraint(expr= - m.b65 + m.x255 + m.x297 + m.x357 >= 0)

m.c537 = Constraint(expr= - m.b66 + m.x256 + m.x298 + m.x358 >= 0)

m.c538 = Constraint(expr= - m.b67 + m.x257 + m.x299 + m.x335 + m.x359 >= 0)

m.c539 = Constraint(expr= - m.b68 + m.x258 + m.x300 + m.x336 + m.x360 >= 0)

m.c540 = Constraint(expr= - m.b69 + m.x259 + m.x301 + m.x337 + m.x361 >= 0)

m.c541 = Constraint(expr= - m.b70 + m.x260 + m.x302 + m.x338 + m.x362 >= 0)

m.c542 = Constraint(expr= - m.b71 + m.x261 + m.x303 + m.x339 + m.x363 >= 0)

m.c543 = Constraint(expr= - m.b72 + m.x262 + m.x304 + m.x340 + m.x364 >= 0)

m.c544 = Constraint(expr= - m.b73 + m.x263 + m.x305 + m.x341 + m.x365 >= 0)

m.c545 = Constraint(expr= - m.b74 + m.x264 + m.x306 + m.x342 + m.x366 >= 0)

m.c546 = Constraint(expr= - m.b75 + m.x265 + m.x307 + m.x343 + m.x367 >= 0)

m.c547 = Constraint(expr= - m.b76 + m.x266 + m.x308 + m.x344 + m.x368 >= 0)

m.c548 = Constraint(expr= - m.b77 + m.x267 + m.x309 + m.x345 + m.x369 >= 0)

m.c549 = Constraint(expr= - m.b78 + m.x268 + m.x310 + m.x346 + m.x370 >= 0)

m.c550 = Constraint(expr= - m.b79 + m.x311 + m.x347 + m.x371 >= 0)

m.c551 = Constraint(expr= - m.b80 + m.x312 + m.x348 + m.x372 >= 0)

m.c552 = Constraint(expr= - m.b81 + m.x313 + m.x349 + m.x373 >= 0)

m.c553 = Constraint(expr= - m.b82 + m.x314 + m.x350 + m.x374 >= 0)

m.c554 = Constraint(expr= - m.b83 + m.x315 + m.x351 + m.x375 >= 0)

m.c555 = Constraint(expr= - m.b84 + m.x316 + m.x352 + m.x376 >= 0)

m.c556 = Constraint(expr= - 0.002*m.x233 - m.x397 + m.x398 >= 0)

m.c557 = Constraint(expr= - 0.002*m.x234 - m.x398 + m.x399 >= 0)

m.c558 = Constraint(expr= - 0.002*m.x235 - m.x399 + m.x400 >= 0)

m.c559 = Constraint(expr= - 0.002*m.x236 - m.x400 + m.x401 >= 0)

m.c560 = Constraint(expr= - 0.002*m.x237 - m.x401 + m.x402 >= 0)

m.c561 = Constraint(expr= - 0.002*m.x238 - m.x402 + m.x403 >= 0)

m.c562 = Constraint(expr= - 0.002*m.x269 - m.x397 + m.x398 >= 0)

m.c563 = Constraint(expr= - 0.002*m.x270 - m.x398 + m.x399 >= 0)

m.c564 = Constraint(expr= - 0.002*m.x271 - m.x399 + m.x400 >= 0)

m.c565 = Constraint(expr= - 0.002*m.x272 - m.x400 + m.x401 >= 0)

m.c566 = Constraint(expr= - 0.002*m.x273 - m.x401 + m.x402 >= 0)

m.c567 = Constraint(expr= - 0.002*m.x274 - m.x402 + m.x403 >= 0)

m.c568 = Constraint(expr= - 0.002*m.x317 - m.x397 + m.x398 >= 0)

m.c569 = Constraint(expr= - 0.002*m.x318 - m.x398 + m.x399 >= 0)

m.c570 = Constraint(expr= - 0.002*m.x319 - m.x399 + m.x400 >= 0)

m.c571 = Constraint(expr= - 0.002*m.x320 - m.x400 + m.x401 >= 0)

m.c572 = Constraint(expr= - 0.002*m.x321 - m.x401 + m.x402 >= 0)

m.c573 = Constraint(expr= - 0.002*m.x322 - m.x402 + m.x403 >= 0)

m.c574 = Constraint(expr= - 0.002*m.x239 - m.x397 + m.x398 >= 0)

m.c575 = Constraint(expr= - 0.002*m.x240 - m.x398 + m.x399 >= 0)

m.c576 = Constraint(expr= - 0.002*m.x241 - m.x399 + m.x400 >= 0)

m.c577 = Constraint(expr= - 0.002*m.x242 - m.x400 + m.x401 >= 0)

m.c578 = Constraint(expr= - 0.002*m.x243 - m.x401 + m.x402 >= 0)

m.c579 = Constraint(expr= - 0.002*m.x244 - m.x402 + m.x403 >= 0)

m.c580 = Constraint(expr= - 0.002*m.x245 - m.x397 + m.x398 >= 0)

m.c581 = Constraint(expr= - 0.002*m.x246 - m.x398 + m.x399 >= 0)

m.c582 = Constraint(expr= - 0.002*m.x247 - m.x399 + m.x400 >= 0)

m.c583 = Constraint(expr= - 0.002*m.x248 - m.x400 + m.x401 >= 0)

m.c584 = Constraint(expr= - 0.002*m.x249 - m.x401 + m.x402 >= 0)

m.c585 = Constraint(expr= - 0.002*m.x250 - m.x402 + m.x403 >= 0)

m.c586 = Constraint(expr= - 0.002*m.x275 - m.x397 + m.x398 >= 0)

m.c587 = Constraint(expr= - 0.002*m.x276 - m.x398 + m.x399 >= 0)

m.c588 = Constraint(expr= - 0.002*m.x277 - m.x399 + m.x400 >= 0)

m.c589 = Constraint(expr= - 0.002*m.x278 - m.x400 + m.x401 >= 0)

m.c590 = Constraint(expr= - 0.002*m.x279 - m.x401 + m.x402 >= 0)

m.c591 = Constraint(expr= - 0.002*m.x280 - m.x402 + m.x403 >= 0)

m.c592 = Constraint(expr= - 0.002*m.x281 - m.x397 + m.x398 >= 0)

m.c593 = Constraint(expr= - 0.002*m.x282 - m.x398 + m.x399 >= 0)

m.c594 = Constraint(expr= - 0.002*m.x283 - m.x399 + m.x400 >= 0)

m.c595 = Constraint(expr= - 0.002*m.x284 - m.x400 + m.x401 >= 0)

m.c596 = Constraint(expr= - 0.002*m.x285 - m.x401 + m.x402 >= 0)

m.c597 = Constraint(expr= - 0.002*m.x286 - m.x402 + m.x403 >= 0)

m.c598 = Constraint(expr= - 0.002*m.x287 - m.x397 + m.x398 >= 0)

m.c599 = Constraint(expr= - 0.002*m.x288 - m.x398 + m.x399 >= 0)

m.c600 = Constraint(expr= - 0.002*m.x289 - m.x399 + m.x400 >= 0)

m.c601 = Constraint(expr= - 0.002*m.x290 - m.x400 + m.x401 >= 0)

m.c602 = Constraint(expr= - 0.002*m.x291 - m.x401 + m.x402 >= 0)

m.c603 = Constraint(expr= - 0.002*m.x292 - m.x402 + m.x403 >= 0)

m.c604 = Constraint(expr= - 0.002*m.x323 - m.x397 + m.x398 >= 0)

m.c605 = Constraint(expr= - 0.002*m.x324 - m.x398 + m.x399 >= 0)

m.c606 = Constraint(expr= - 0.002*m.x325 - m.x399 + m.x400 >= 0)

m.c607 = Constraint(expr= - 0.002*m.x326 - m.x400 + m.x401 >= 0)

m.c608 = Constraint(expr= - 0.002*m.x327 - m.x401 + m.x402 >= 0)

m.c609 = Constraint(expr= - 0.002*m.x328 - m.x402 + m.x403 >= 0)

m.c610 = Constraint(expr= - 0.002*m.x329 - m.x397 + m.x398 >= 0)

m.c611 = Constraint(expr= - 0.002*m.x330 - m.x398 + m.x399 >= 0)

m.c612 = Constraint(expr= - 0.002*m.x331 - m.x399 + m.x400 >= 0)

m.c613 = Constraint(expr= - 0.002*m.x332 - m.x400 + m.x401 >= 0)

m.c614 = Constraint(expr= - 0.002*m.x333 - m.x401 + m.x402 >= 0)

m.c615 = Constraint(expr= - 0.002*m.x334 - m.x402 + m.x403 >= 0)

m.c616 = Constraint(expr= - 0.002*m.x257 - 0.002*m.x263 - 0.002*m.x299 - 0.002*m.x305 - 0.002*m.x335 - 0.002*m.x341
                          - 0.002*m.x359 - 0.002*m.x365 - m.x397 + m.x398 >= 0)

m.c617 = Constraint(expr= - 0.002*m.x258 - 0.002*m.x264 - 0.002*m.x300 - 0.002*m.x306 - 0.002*m.x336 - 0.002*m.x342
                          - 0.002*m.x360 - 0.002*m.x366 - m.x398 + m.x399 >= 0)

m.c618 = Constraint(expr= - 0.002*m.x259 - 0.002*m.x265 - 0.002*m.x301 - 0.002*m.x307 - 0.002*m.x337 - 0.002*m.x343
                          - 0.002*m.x361 - 0.002*m.x367 - m.x399 + m.x400 >= 0)

m.c619 = Constraint(expr= - 0.002*m.x260 - 0.002*m.x266 - 0.002*m.x302 - 0.002*m.x308 - 0.002*m.x338 - 0.002*m.x344
                          - 0.002*m.x362 - 0.002*m.x368 - m.x400 + m.x401 >= 0)

m.c620 = Constraint(expr= - 0.002*m.x261 - 0.002*m.x267 - 0.002*m.x303 - 0.002*m.x309 - 0.002*m.x339 - 0.002*m.x345
                          - 0.002*m.x363 - 0.002*m.x369 - m.x401 + m.x402 >= 0)

m.c621 = Constraint(expr= - 0.002*m.x262 - 0.002*m.x268 - 0.002*m.x304 - 0.002*m.x310 - 0.002*m.x340 - 0.002*m.x346
                          - 0.002*m.x364 - 0.002*m.x370 - m.x402 + m.x403 >= 0)

m.c622 = Constraint(expr= - 0.002*m.x251 - 0.002*m.x257 - 0.002*m.x293 - 0.002*m.x299 - 0.002*m.x335 - 0.002*m.x353
                          - 0.002*m.x359 - m.x397 + m.x398 >= 0)

m.c623 = Constraint(expr= - 0.002*m.x252 - 0.002*m.x258 - 0.002*m.x294 - 0.002*m.x300 - 0.002*m.x336 - 0.002*m.x354
                          - 0.002*m.x360 - m.x398 + m.x399 >= 0)

m.c624 = Constraint(expr= - 0.002*m.x253 - 0.002*m.x259 - 0.002*m.x295 - 0.002*m.x301 - 0.002*m.x337 - 0.002*m.x355
                          - 0.002*m.x361 - m.x399 + m.x400 >= 0)

m.c625 = Constraint(expr= - 0.002*m.x254 - 0.002*m.x260 - 0.002*m.x296 - 0.002*m.x302 - 0.002*m.x338 - 0.002*m.x356
                          - 0.002*m.x362 - m.x400 + m.x401 >= 0)

m.c626 = Constraint(expr= - 0.002*m.x255 - 0.002*m.x261 - 0.002*m.x297 - 0.002*m.x303 - 0.002*m.x339 - 0.002*m.x357
                          - 0.002*m.x363 - m.x401 + m.x402 >= 0)

m.c627 = Constraint(expr= - 0.002*m.x256 - 0.002*m.x262 - 0.002*m.x298 - 0.002*m.x304 - 0.002*m.x340 - 0.002*m.x358
                          - 0.002*m.x364 - m.x402 + m.x403 >= 0)

m.c628 = Constraint(expr= - 0.002*m.x263 - 0.002*m.x305 - 0.002*m.x311 - 0.002*m.x341 - 0.002*m.x347 - 0.002*m.x365
                          - 0.002*m.x371 - m.x397 + m.x398 >= 0)

m.c629 = Constraint(expr= - 0.002*m.x264 - 0.002*m.x306 - 0.002*m.x312 - 0.002*m.x342 - 0.002*m.x348 - 0.002*m.x366
                          - 0.002*m.x372 - m.x398 + m.x399 >= 0)

m.c630 = Constraint(expr= - 0.002*m.x265 - 0.002*m.x307 - 0.002*m.x313 - 0.002*m.x343 - 0.002*m.x349 - 0.002*m.x367
                          - 0.002*m.x373 - m.x399 + m.x400 >= 0)

m.c631 = Constraint(expr= - 0.002*m.x266 - 0.002*m.x308 - 0.002*m.x314 - 0.002*m.x344 - 0.002*m.x350 - 0.002*m.x368
                          - 0.002*m.x374 - m.x400 + m.x401 >= 0)

m.c632 = Constraint(expr= - 0.002*m.x267 - 0.002*m.x309 - 0.002*m.x315 - 0.002*m.x345 - 0.002*m.x351 - 0.002*m.x369
                          - 0.002*m.x375 - m.x401 + m.x402 >= 0)

m.c633 = Constraint(expr= - 0.002*m.x268 - 0.002*m.x310 - 0.002*m.x316 - 0.002*m.x346 - 0.002*m.x352 - 0.002*m.x370
                          - 0.002*m.x376 - m.x402 + m.x403 >= 0)

m.c634 = Constraint(expr= - 0.02*m.x251 - 0.02*m.x257 - 0.02*m.x293 - 0.02*m.x299 - 0.02*m.x335 - 0.02*m.x353
                          - 0.02*m.x359 - m.x397 + m.x398 <= 0)

m.c635 = Constraint(expr= - 0.02*m.x252 - 0.02*m.x258 - 0.02*m.x294 - 0.02*m.x300 - 0.02*m.x336 - 0.02*m.x354
                          - 0.02*m.x360 - m.x398 + m.x399 <= 0)

m.c636 = Constraint(expr= - 0.02*m.x253 - 0.02*m.x259 - 0.02*m.x295 - 0.02*m.x301 - 0.02*m.x337 - 0.02*m.x355
                          - 0.02*m.x361 - m.x399 + m.x400 <= 0)

m.c637 = Constraint(expr= - 0.02*m.x254 - 0.02*m.x260 - 0.02*m.x296 - 0.02*m.x302 - 0.02*m.x338 - 0.02*m.x356
                          - 0.02*m.x362 - m.x400 + m.x401 <= 0)

m.c638 = Constraint(expr= - 0.02*m.x255 - 0.02*m.x261 - 0.02*m.x297 - 0.02*m.x303 - 0.02*m.x339 - 0.02*m.x357
                          - 0.02*m.x363 - m.x401 + m.x402 <= 0)

m.c639 = Constraint(expr= - 0.02*m.x256 - 0.02*m.x262 - 0.02*m.x298 - 0.02*m.x304 - 0.02*m.x340 - 0.02*m.x358
                          - 0.02*m.x364 - m.x402 + m.x403 <= 0)

m.c640 = Constraint(expr= - 0.02*m.x263 - 0.02*m.x305 - 0.02*m.x311 - 0.02*m.x341 - 0.02*m.x347 - 0.02*m.x365
                          - 0.02*m.x371 - m.x397 + m.x398 <= 0)

m.c641 = Constraint(expr= - 0.02*m.x264 - 0.02*m.x306 - 0.02*m.x312 - 0.02*m.x342 - 0.02*m.x348 - 0.02*m.x366
                          - 0.02*m.x372 - m.x398 + m.x399 <= 0)

m.c642 = Constraint(expr= - 0.02*m.x265 - 0.02*m.x307 - 0.02*m.x313 - 0.02*m.x343 - 0.02*m.x349 - 0.02*m.x367
                          - 0.02*m.x373 - m.x399 + m.x400 <= 0)

m.c643 = Constraint(expr= - 0.02*m.x266 - 0.02*m.x308 - 0.02*m.x314 - 0.02*m.x344 - 0.02*m.x350 - 0.02*m.x368
                          - 0.02*m.x374 - m.x400 + m.x401 <= 0)

m.c644 = Constraint(expr= - 0.02*m.x267 - 0.02*m.x309 - 0.02*m.x315 - 0.02*m.x345 - 0.02*m.x351 - 0.02*m.x369
                          - 0.02*m.x375 - m.x401 + m.x402 <= 0)

m.c645 = Constraint(expr= - 0.02*m.x268 - 0.02*m.x310 - 0.02*m.x316 - 0.02*m.x346 - 0.02*m.x352 - 0.02*m.x370
                          - 0.02*m.x376 - m.x402 + m.x403 <= 0)

m.c646 = Constraint(expr=   m.x397 >= 0)

m.c647 = Constraint(expr= - 3*m.b87 + m.x398 >= 0)

m.c648 = Constraint(expr= - 3*m.b89 - 6*m.b90 + m.x399 >= 0)

m.c649 = Constraint(expr= - 3*m.b92 - 6*m.b93 + m.x400 >= 0)

m.c650 = Constraint(expr= - 3*m.b94 - 6*m.b95 + m.x401 >= 0)

m.c651 = Constraint(expr= - 6*m.b96 + m.x402 >= 0)

m.c652 = Constraint(expr= - 2*m.b97 + m.x398 >= 0)

m.c653 = Constraint(expr= - 2*m.b98 - 5*m.b99 + m.x399 >= 0)

m.c654 = Constraint(expr= - 2*m.b100 - 5*m.b101 - 8*m.b102 + m.x400 >= 0)

m.c655 = Constraint(expr= - 2*m.b103 - 5*m.b104 - 8*m.b105 + m.x401 >= 0)

m.c656 = Constraint(expr= - 5*m.b106 - 8*m.b107 + m.x402 >= 0)

m.c657 = Constraint(expr= - 8*m.b108 + m.x403 >= 0)

m.c658 = Constraint(expr=   m.b85 + 2*m.b86 + 3*m.b88 + 4*m.b91 - 2*m.b97 - 3*m.b98 - 4*m.b100 - 5*m.b103 <= -1)

m.c659 = Constraint(expr=   2*m.b87 + 3*m.b89 + 4*m.b92 + 5*m.b94 - 3*m.b99 - 4*m.b101 - 5*m.b104 - 6*m.b106 <= -1)

m.c660 = Constraint(expr=   3*m.b90 + 4*m.b93 + 5*m.b95 + 6*m.b96 - 4*m.b102 - 5*m.b105 - 6*m.b107 - 7*m.b108 <= -1)

m.c661 = Constraint(expr= - 2*m.b87 - 3*m.b89 - 4*m.b92 - 5*m.b94 + 2*m.b97 + 3*m.b98 + 4*m.b100 + 5*m.b103 <= 0)

m.c662 = Constraint(expr= - 3*m.b90 - 4*m.b93 - 5*m.b95 - 6*m.b96 + 3*m.b99 + 4*m.b101 + 5*m.b104 + 6*m.b106 <= 0)

m.c663 = Constraint(expr=   m.x119 + m.x120 <= 5)

m.c664 = Constraint(expr=-m.x377*m.x136 + m.x252 == 0)

m.c665 = Constraint(expr=-m.x378*m.x137 + m.x253 == 0)

m.c666 = Constraint(expr=-m.x379*m.x138 + m.x254 == 0)

m.c667 = Constraint(expr=-m.x380*m.x139 + m.x255 == 0)

m.c668 = Constraint(expr=-m.x381*m.x140 + m.x256 == 0)

m.c669 = Constraint(expr=-m.x382*m.x143 + m.x258 == 0)

m.c670 = Constraint(expr=-m.x383*m.x144 + m.x259 == 0)

m.c671 = Constraint(expr=-m.x384*m.x145 + m.x260 == 0)

m.c672 = Constraint(expr=-m.x385*m.x146 + m.x261 == 0)

m.c673 = Constraint(expr=-m.x386*m.x147 + m.x262 == 0)

m.c674 = Constraint(expr=-m.x387*m.x143 + m.x264 == 0)

m.c675 = Constraint(expr=-m.x388*m.x144 + m.x265 == 0)

m.c676 = Constraint(expr=-m.x389*m.x145 + m.x266 == 0)

m.c677 = Constraint(expr=-m.x390*m.x146 + m.x267 == 0)

m.c678 = Constraint(expr=-m.x391*m.x147 + m.x268 == 0)

m.c679 = Constraint(expr=-m.x377*m.x164 + m.x294 == 0)

m.c680 = Constraint(expr=-m.x378*m.x165 + m.x295 == 0)

m.c681 = Constraint(expr=-m.x379*m.x166 + m.x296 == 0)

m.c682 = Constraint(expr=-m.x380*m.x167 + m.x297 == 0)

m.c683 = Constraint(expr=-m.x381*m.x168 + m.x298 == 0)

m.c684 = Constraint(expr=-m.x382*m.x171 + m.x300 == 0)

m.c685 = Constraint(expr=-m.x383*m.x172 + m.x301 == 0)

m.c686 = Constraint(expr=-m.x384*m.x173 + m.x302 == 0)

m.c687 = Constraint(expr=-m.x385*m.x174 + m.x303 == 0)

m.c688 = Constraint(expr=-m.x386*m.x175 + m.x304 == 0)

m.c689 = Constraint(expr=-m.x387*m.x171 + m.x306 == 0)

m.c690 = Constraint(expr=-m.x388*m.x172 + m.x307 == 0)

m.c691 = Constraint(expr=-m.x389*m.x173 + m.x308 == 0)

m.c692 = Constraint(expr=-m.x390*m.x174 + m.x309 == 0)

m.c693 = Constraint(expr=-m.x391*m.x175 + m.x310 == 0)

m.c694 = Constraint(expr=-m.x392*m.x178 + m.x312 == 0)

m.c695 = Constraint(expr=-m.x393*m.x179 + m.x313 == 0)

m.c696 = Constraint(expr=-m.x394*m.x180 + m.x314 == 0)

m.c697 = Constraint(expr=-m.x395*m.x181 + m.x315 == 0)

m.c698 = Constraint(expr=-m.x396*m.x182 + m.x316 == 0)

m.c699 = Constraint(expr=-m.x382*m.x199 + m.x336 == 0)

m.c700 = Constraint(expr=-m.x383*m.x200 + m.x337 == 0)

m.c701 = Constraint(expr=-m.x384*m.x201 + m.x338 == 0)

m.c702 = Constraint(expr=-m.x385*m.x202 + m.x339 == 0)

m.c703 = Constraint(expr=-m.x386*m.x203 + m.x340 == 0)

m.c704 = Constraint(expr=-m.x387*m.x199 + m.x342 == 0)

m.c705 = Constraint(expr=-m.x388*m.x200 + m.x343 == 0)

m.c706 = Constraint(expr=-m.x389*m.x201 + m.x344 == 0)

m.c707 = Constraint(expr=-m.x390*m.x202 + m.x345 == 0)

m.c708 = Constraint(expr=-m.x391*m.x203 + m.x346 == 0)

m.c709 = Constraint(expr=-m.x392*m.x206 + m.x348 == 0)

m.c710 = Constraint(expr=-m.x393*m.x207 + m.x349 == 0)

m.c711 = Constraint(expr=-m.x394*m.x208 + m.x350 == 0)

m.c712 = Constraint(expr=-m.x395*m.x209 + m.x351 == 0)

m.c713 = Constraint(expr=-m.x396*m.x210 + m.x352 == 0)

m.c714 = Constraint(expr=-m.x377*m.x213 + m.x354 == 0)

m.c715 = Constraint(expr=-m.x378*m.x214 + m.x355 == 0)

m.c716 = Constraint(expr=-m.x379*m.x215 + m.x356 == 0)

m.c717 = Constraint(expr=-m.x380*m.x216 + m.x357 == 0)

m.c718 = Constraint(expr=-m.x381*m.x217 + m.x358 == 0)

m.c719 = Constraint(expr=-m.x382*m.x220 + m.x360 == 0)

m.c720 = Constraint(expr=-m.x383*m.x221 + m.x361 == 0)

m.c721 = Constraint(expr=-m.x384*m.x222 + m.x362 == 0)

m.c722 = Constraint(expr=-m.x385*m.x223 + m.x363 == 0)

m.c723 = Constraint(expr=-m.x386*m.x224 + m.x364 == 0)

m.c724 = Constraint(expr=-m.x387*m.x220 + m.x366 == 0)

m.c725 = Constraint(expr=-m.x388*m.x221 + m.x367 == 0)

m.c726 = Constraint(expr=-m.x389*m.x222 + m.x368 == 0)

m.c727 = Constraint(expr=-m.x390*m.x223 + m.x369 == 0)

m.c728 = Constraint(expr=-m.x391*m.x224 + m.x370 == 0)

m.c729 = Constraint(expr=-m.x392*m.x227 + m.x372 == 0)

m.c730 = Constraint(expr=-m.x393*m.x228 + m.x373 == 0)

m.c731 = Constraint(expr=-m.x394*m.x229 + m.x374 == 0)

m.c732 = Constraint(expr=-m.x395*m.x230 + m.x375 == 0)

m.c733 = Constraint(expr=-m.x396*m.x231 + m.x376 == 0)
