#  MINLP written by GAMS Convert at 04/21/18 13:51:21
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       1199      480      371      348        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        730      602      128        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       4845     4376      469        0
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
m.b109 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b128 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x152 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,500),initialize=0)
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
m.x184 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,500),initialize=0)
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
m.x216 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x235 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x255 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x258 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x262 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x263 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x264 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x265 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x266 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x267 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x268 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x269 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x270 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x271 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x272 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x273 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x274 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x275 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x276 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x277 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x278 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x279 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x280 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x281 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x282 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x283 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x284 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x285 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x286 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x287 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,700),initialize=0)
m.x289 = Var(within=Reals,bounds=(0,700),initialize=0)
m.x290 = Var(within=Reals,bounds=(0,700),initialize=0)
m.x291 = Var(within=Reals,bounds=(0,700),initialize=0)
m.x292 = Var(within=Reals,bounds=(0,700),initialize=0)
m.x293 = Var(within=Reals,bounds=(0,700),initialize=0)
m.x294 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x295 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x296 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x297 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x298 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x299 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x300 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x301 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x302 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x303 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x304 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x305 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x306 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x307 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x309 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x311 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x312 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x313 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x314 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x315 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x316 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x317 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x318 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x319 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x320 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x321 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x322 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x323 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x324 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x325 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x326 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x327 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x328 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x329 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x330 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x331 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x332 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x333 = Var(within=Reals,bounds=(0,300),initialize=0)
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
m.x543 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x544 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x545 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x546 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x547 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x548 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x549 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x550 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x551 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x552 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x553 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x554 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x555 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x556 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x557 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x558 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x559 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x560 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x561 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x562 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x563 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x564 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x601 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x602 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x603 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x604 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x605 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x606 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x607 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x608 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x609 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x610 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x611 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x612 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x613 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x614 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x615 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x616 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x617 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x618 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x619 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x620 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x621 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x622 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x623 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x624 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x625 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x626 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x627 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x628 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x629 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x630 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x631 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x632 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x633 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x634 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x635 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x636 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x637 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x638 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x639 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x640 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x641 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x642 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x643 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x644 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x645 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x646 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x647 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x648 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x649 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x650 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x651 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x652 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x653 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x654 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x655 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x656 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x657 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x658 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x659 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x660 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x661 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x662 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x663 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x664 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x665 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x666 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x667 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x668 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x669 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x670 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x671 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x672 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x673 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x674 = Var(within=Reals,bounds=(12,12),initialize=12)
m.x675 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x676 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x677 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x678 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x679 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x680 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x681 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x682 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x683 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x684 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x685 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x686 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x687 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x688 = Var(within=Reals,bounds=(100,600),initialize=100)
m.x689 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x690 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x691 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x692 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x693 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x694 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x695 = Var(within=Reals,bounds=(100,600),initialize=100)
m.x696 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x697 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x698 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x699 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x700 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x701 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x702 = Var(within=Reals,bounds=(100,600),initialize=100)
m.x703 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x704 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x705 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x706 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x707 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x708 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x709 = Var(within=Reals,bounds=(150,650),initialize=150)
m.x710 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x711 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x712 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x713 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x714 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x715 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x716 = Var(within=Reals,bounds=(250,750),initialize=250)
m.x717 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x718 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x719 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x720 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x721 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x722 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x723 = Var(within=Reals,bounds=(150,650),initialize=150)
m.x724 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x725 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x726 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x727 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x728 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x729 = Var(within=Reals,bounds=(0,1000),initialize=0)

m.obj = Objective(expr=4*m.x675*m.x688 + 4*m.x676*m.x689 + 4*m.x677*m.x690 + 4*m.x678*m.x691 + 4*m.x679*m.x692 + 4*
                       m.x680*m.x693 + 4*m.x681*m.x694 + 4*m.x675*m.x695 + 4*m.x676*m.x696 + 4*m.x677*m.x697 + 4*m.x678*
                       m.x698 + 4*m.x679*m.x699 + 4*m.x680*m.x700 + 4*m.x681*m.x701 + 4*m.x675*m.x702 + 4*m.x676*m.x703
                        + 4*m.x677*m.x704 + 4*m.x678*m.x705 + 4*m.x679*m.x706 + 4*m.x680*m.x707 + 4*m.x681*m.x708 + 8*
                       m.x675*m.x709 + 8*m.x676*m.x710 + 8*m.x677*m.x711 + 8*m.x678*m.x712 + 8*m.x679*m.x713 + 8*m.x680*
                       m.x714 + 8*m.x681*m.x715 + 8*m.x675*m.x716 + 8*m.x676*m.x717 + 8*m.x677*m.x718 + 8*m.x678*m.x719
                        + 8*m.x679*m.x720 + 8*m.x680*m.x721 + 8*m.x681*m.x722 + 8*m.x675*m.x723 + 8*m.x676*m.x724 + 8*
                       m.x677*m.x725 + 8*m.x678*m.x726 + 8*m.x679*m.x727 + 8*m.x680*m.x728 + 8*m.x681*m.x729
                        + 50000*m.x141 + 50000*m.x142 + 5000*m.x682 + 5000*m.x683 + 5000*m.x684 + 10000*m.x685
                        + 10000*m.x686 + 10000*m.x687 - 100000, sense=minimize)

m.c2 = Constraint(expr=   m.x143 == 500)

m.c3 = Constraint(expr= - m.x143 + m.x144 + m.x335 == 0)

m.c4 = Constraint(expr= - m.x144 + m.x145 + m.x336 == 0)

m.c5 = Constraint(expr= - m.x145 + m.x146 + m.x337 == 0)

m.c6 = Constraint(expr= - m.x146 + m.x147 + m.x338 == 0)

m.c7 = Constraint(expr= - m.x147 + m.x148 + m.x339 == 0)

m.c8 = Constraint(expr= - m.x148 + m.x149 + m.x340 == 0)

m.c9 = Constraint(expr= - m.x149 + m.x150 + m.x341 == 0)

m.c10 = Constraint(expr=   m.x151 == 0)

m.c11 = Constraint(expr= - m.x151 + m.x152 - m.x335 + m.x342 + m.x349 == 0)

m.c12 = Constraint(expr= - m.x152 + m.x153 - m.x336 + m.x343 + m.x350 == 0)

m.c13 = Constraint(expr= - m.x153 + m.x154 - m.x337 + m.x344 + m.x351 == 0)

m.c14 = Constraint(expr= - m.x154 + m.x155 - m.x338 + m.x345 + m.x352 == 0)

m.c15 = Constraint(expr= - m.x155 + m.x156 - m.x339 + m.x346 + m.x353 == 0)

m.c16 = Constraint(expr= - m.x156 + m.x157 - m.x340 + m.x347 + m.x354 == 0)

m.c17 = Constraint(expr= - m.x157 + m.x158 - m.x341 + m.x348 + m.x355 == 0)

m.c18 = Constraint(expr=   m.x159 == 0)

m.c19 = Constraint(expr= - m.x159 + m.x160 - m.x342 + m.x356 == 0)

m.c20 = Constraint(expr= - m.x160 + m.x161 - m.x343 + m.x357 == 0)

m.c21 = Constraint(expr= - m.x161 + m.x162 - m.x344 + m.x358 == 0)

m.c22 = Constraint(expr= - m.x162 + m.x163 - m.x345 + m.x359 == 0)

m.c23 = Constraint(expr= - m.x163 + m.x164 - m.x346 + m.x360 == 0)

m.c24 = Constraint(expr= - m.x164 + m.x165 - m.x347 + m.x361 == 0)

m.c25 = Constraint(expr= - m.x165 + m.x166 - m.x348 + m.x362 == 0)

m.c26 = Constraint(expr=   m.x167 == 0)

m.c27 = Constraint(expr= - m.x167 + m.x168 - m.x349 + m.x363 + m.x370 == 0)

m.c28 = Constraint(expr= - m.x168 + m.x169 - m.x350 + m.x364 + m.x371 == 0)

m.c29 = Constraint(expr= - m.x169 + m.x170 - m.x351 + m.x365 + m.x372 == 0)

m.c30 = Constraint(expr= - m.x170 + m.x171 - m.x352 + m.x366 + m.x373 == 0)

m.c31 = Constraint(expr= - m.x171 + m.x172 - m.x353 + m.x367 + m.x374 == 0)

m.c32 = Constraint(expr= - m.x172 + m.x173 - m.x354 + m.x368 + m.x375 == 0)

m.c33 = Constraint(expr= - m.x173 + m.x174 - m.x355 + m.x369 + m.x376 == 0)

m.c34 = Constraint(expr=   m.x175 == 500)

m.c35 = Constraint(expr= - m.x175 + m.x176 + m.x377 == 0)

m.c36 = Constraint(expr= - m.x176 + m.x177 + m.x378 == 0)

m.c37 = Constraint(expr= - m.x177 + m.x178 + m.x379 == 0)

m.c38 = Constraint(expr= - m.x178 + m.x179 + m.x380 == 0)

m.c39 = Constraint(expr= - m.x179 + m.x180 + m.x381 == 0)

m.c40 = Constraint(expr= - m.x180 + m.x181 + m.x382 == 0)

m.c41 = Constraint(expr= - m.x181 + m.x182 + m.x383 == 0)

m.c42 = Constraint(expr=   m.x183 == 0)

m.c43 = Constraint(expr= - m.x183 + m.x184 - m.x377 + m.x384 + m.x391 == 0)

m.c44 = Constraint(expr= - m.x184 + m.x185 - m.x378 + m.x385 + m.x392 == 0)

m.c45 = Constraint(expr= - m.x185 + m.x186 - m.x379 + m.x386 + m.x393 == 0)

m.c46 = Constraint(expr= - m.x186 + m.x187 - m.x380 + m.x387 + m.x394 == 0)

m.c47 = Constraint(expr= - m.x187 + m.x188 - m.x381 + m.x388 + m.x395 == 0)

m.c48 = Constraint(expr= - m.x188 + m.x189 - m.x382 + m.x389 + m.x396 == 0)

m.c49 = Constraint(expr= - m.x189 + m.x190 - m.x383 + m.x390 + m.x397 == 0)

m.c50 = Constraint(expr=   m.x191 == 0)

m.c51 = Constraint(expr= - m.x191 + m.x192 - m.x384 + m.x398 + m.x405 == 0)

m.c52 = Constraint(expr= - m.x192 + m.x193 - m.x385 + m.x399 + m.x406 == 0)

m.c53 = Constraint(expr= - m.x193 + m.x194 - m.x386 + m.x400 + m.x407 == 0)

m.c54 = Constraint(expr= - m.x194 + m.x195 - m.x387 + m.x401 + m.x408 == 0)

m.c55 = Constraint(expr= - m.x195 + m.x196 - m.x388 + m.x402 + m.x409 == 0)

m.c56 = Constraint(expr= - m.x196 + m.x197 - m.x389 + m.x403 + m.x410 == 0)

m.c57 = Constraint(expr= - m.x197 + m.x198 - m.x390 + m.x404 + m.x411 == 0)

m.c58 = Constraint(expr=   m.x199 == 0)

m.c59 = Constraint(expr= - m.x199 + m.x200 - m.x391 + m.x412 == 0)

m.c60 = Constraint(expr= - m.x200 + m.x201 - m.x392 + m.x413 == 0)

m.c61 = Constraint(expr= - m.x201 + m.x202 - m.x393 + m.x414 == 0)

m.c62 = Constraint(expr= - m.x202 + m.x203 - m.x394 + m.x415 == 0)

m.c63 = Constraint(expr= - m.x203 + m.x204 - m.x395 + m.x416 == 0)

m.c64 = Constraint(expr= - m.x204 + m.x205 - m.x396 + m.x417 == 0)

m.c65 = Constraint(expr= - m.x205 + m.x206 - m.x397 + m.x418 == 0)

m.c66 = Constraint(expr=   m.x207 == 500)

m.c67 = Constraint(expr= - m.x207 + m.x208 + m.x419 == 0)

m.c68 = Constraint(expr= - m.x208 + m.x209 + m.x420 == 0)

m.c69 = Constraint(expr= - m.x209 + m.x210 + m.x421 == 0)

m.c70 = Constraint(expr= - m.x210 + m.x211 + m.x422 == 0)

m.c71 = Constraint(expr= - m.x211 + m.x212 + m.x423 == 0)

m.c72 = Constraint(expr= - m.x212 + m.x213 + m.x424 == 0)

m.c73 = Constraint(expr= - m.x213 + m.x214 + m.x425 == 0)

m.c74 = Constraint(expr=   m.x215 == 0)

m.c75 = Constraint(expr= - m.x215 + m.x216 - m.x419 + m.x426 + m.x433 + m.x440 == 0)

m.c76 = Constraint(expr= - m.x216 + m.x217 - m.x420 + m.x427 + m.x434 + m.x441 == 0)

m.c77 = Constraint(expr= - m.x217 + m.x218 - m.x421 + m.x428 + m.x435 + m.x442 == 0)

m.c78 = Constraint(expr= - m.x218 + m.x219 - m.x422 + m.x429 + m.x436 + m.x443 == 0)

m.c79 = Constraint(expr= - m.x219 + m.x220 - m.x423 + m.x430 + m.x437 + m.x444 == 0)

m.c80 = Constraint(expr= - m.x220 + m.x221 - m.x424 + m.x431 + m.x438 + m.x445 == 0)

m.c81 = Constraint(expr= - m.x221 + m.x222 - m.x425 + m.x432 + m.x439 + m.x446 == 0)

m.c82 = Constraint(expr=   m.x223 == 0)

m.c83 = Constraint(expr= - m.x223 + m.x224 - m.x426 + m.x447 == 0)

m.c84 = Constraint(expr= - m.x224 + m.x225 - m.x427 + m.x448 == 0)

m.c85 = Constraint(expr= - m.x225 + m.x226 - m.x428 + m.x449 == 0)

m.c86 = Constraint(expr= - m.x226 + m.x227 - m.x429 + m.x450 == 0)

m.c87 = Constraint(expr= - m.x227 + m.x228 - m.x430 + m.x451 == 0)

m.c88 = Constraint(expr= - m.x228 + m.x229 - m.x431 + m.x452 == 0)

m.c89 = Constraint(expr= - m.x229 + m.x230 - m.x432 + m.x453 == 0)

m.c90 = Constraint(expr=   m.x231 == 0)

m.c91 = Constraint(expr= - m.x231 + m.x232 - m.x433 + m.x454 + m.x461 == 0)

m.c92 = Constraint(expr= - m.x232 + m.x233 - m.x434 + m.x455 + m.x462 == 0)

m.c93 = Constraint(expr= - m.x233 + m.x234 - m.x435 + m.x456 + m.x463 == 0)

m.c94 = Constraint(expr= - m.x234 + m.x235 - m.x436 + m.x457 + m.x464 == 0)

m.c95 = Constraint(expr= - m.x235 + m.x236 - m.x437 + m.x458 + m.x465 == 0)

m.c96 = Constraint(expr= - m.x236 + m.x237 - m.x438 + m.x459 + m.x466 == 0)

m.c97 = Constraint(expr= - m.x237 + m.x238 - m.x439 + m.x460 + m.x467 == 0)

m.c98 = Constraint(expr=   m.x239 == 0)

m.c99 = Constraint(expr= - m.x239 + m.x240 - m.x440 + m.x468 == 0)

m.c100 = Constraint(expr= - m.x240 + m.x241 - m.x441 + m.x469 == 0)

m.c101 = Constraint(expr= - m.x241 + m.x242 - m.x442 + m.x470 == 0)

m.c102 = Constraint(expr= - m.x242 + m.x243 - m.x443 + m.x471 == 0)

m.c103 = Constraint(expr= - m.x243 + m.x244 - m.x444 + m.x472 == 0)

m.c104 = Constraint(expr= - m.x244 + m.x245 - m.x445 + m.x473 == 0)

m.c105 = Constraint(expr= - m.x245 + m.x246 - m.x446 + m.x474 == 0)

m.c106 = Constraint(expr=   m.x247 == 200)

m.c107 = Constraint(expr= - m.x247 + m.x248 + m.x475 + m.x482 == 0)

m.c108 = Constraint(expr= - m.x248 + m.x249 + m.x476 + m.x483 == 0)

m.c109 = Constraint(expr= - m.x249 + m.x250 + m.x477 + m.x484 == 0)

m.c110 = Constraint(expr= - m.x250 + m.x251 + m.x478 + m.x485 == 0)

m.c111 = Constraint(expr= - m.x251 + m.x252 + m.x479 + m.x486 == 0)

m.c112 = Constraint(expr= - m.x252 + m.x253 + m.x480 + m.x487 == 0)

m.c113 = Constraint(expr= - m.x253 + m.x254 + m.x481 + m.x488 == 0)

m.c114 = Constraint(expr=   m.x255 == 0)

m.c115 = Constraint(expr= - m.x255 + m.x256 - m.x475 + m.x489 == 0)

m.c116 = Constraint(expr= - m.x256 + m.x257 - m.x476 + m.x490 == 0)

m.c117 = Constraint(expr= - m.x257 + m.x258 - m.x477 + m.x491 == 0)

m.c118 = Constraint(expr= - m.x258 + m.x259 - m.x478 + m.x492 == 0)

m.c119 = Constraint(expr= - m.x259 + m.x260 - m.x479 + m.x493 == 0)

m.c120 = Constraint(expr= - m.x260 + m.x261 - m.x480 + m.x494 == 0)

m.c121 = Constraint(expr= - m.x261 + m.x262 - m.x481 + m.x495 == 0)

m.c122 = Constraint(expr=   m.x263 == 0)

m.c123 = Constraint(expr= - m.x263 + m.x264 - m.x482 + m.x496 + m.x503 == 0)

m.c124 = Constraint(expr= - m.x264 + m.x265 - m.x483 + m.x497 + m.x504 == 0)

m.c125 = Constraint(expr= - m.x265 + m.x266 - m.x484 + m.x498 + m.x505 == 0)

m.c126 = Constraint(expr= - m.x266 + m.x267 - m.x485 + m.x499 + m.x506 == 0)

m.c127 = Constraint(expr= - m.x267 + m.x268 - m.x486 + m.x500 + m.x507 == 0)

m.c128 = Constraint(expr= - m.x268 + m.x269 - m.x487 + m.x501 + m.x508 == 0)

m.c129 = Constraint(expr= - m.x269 + m.x270 - m.x488 + m.x502 + m.x509 == 0)

m.c130 = Constraint(expr=   m.x271 == 200)

m.c131 = Constraint(expr= - m.x271 + m.x272 + m.x510 + m.x517 + m.x524 == 0)

m.c132 = Constraint(expr= - m.x272 + m.x273 + m.x511 + m.x518 + m.x525 == 0)

m.c133 = Constraint(expr= - m.x273 + m.x274 + m.x512 + m.x519 + m.x526 == 0)

m.c134 = Constraint(expr= - m.x274 + m.x275 + m.x513 + m.x520 + m.x527 == 0)

m.c135 = Constraint(expr= - m.x275 + m.x276 + m.x514 + m.x521 + m.x528 == 0)

m.c136 = Constraint(expr= - m.x276 + m.x277 + m.x515 + m.x522 + m.x529 == 0)

m.c137 = Constraint(expr= - m.x277 + m.x278 + m.x516 + m.x523 + m.x530 == 0)

m.c138 = Constraint(expr=   m.x279 == 0)

m.c139 = Constraint(expr= - m.x279 + m.x280 - m.x510 + m.x531 == 0)

m.c140 = Constraint(expr= - m.x280 + m.x281 - m.x511 + m.x532 == 0)

m.c141 = Constraint(expr= - m.x281 + m.x282 - m.x512 + m.x533 == 0)

m.c142 = Constraint(expr= - m.x282 + m.x283 - m.x513 + m.x534 == 0)

m.c143 = Constraint(expr= - m.x283 + m.x284 - m.x514 + m.x535 == 0)

m.c144 = Constraint(expr= - m.x284 + m.x285 - m.x515 + m.x536 == 0)

m.c145 = Constraint(expr= - m.x285 + m.x286 - m.x516 + m.x537 == 0)

m.c146 = Constraint(expr=   m.x287 == 500)

m.c147 = Constraint(expr= - m.x287 + m.x288 - m.x517 + m.x538 + m.x545 == 0)

m.c148 = Constraint(expr= - m.x288 + m.x289 - m.x518 + m.x539 + m.x546 == 0)

m.c149 = Constraint(expr= - m.x289 + m.x290 - m.x519 + m.x540 + m.x547 == 0)

m.c150 = Constraint(expr= - m.x290 + m.x291 - m.x520 + m.x541 + m.x548 == 0)

m.c151 = Constraint(expr= - m.x291 + m.x292 - m.x521 + m.x542 + m.x549 == 0)

m.c152 = Constraint(expr= - m.x292 + m.x293 - m.x522 + m.x543 + m.x550 == 0)

m.c153 = Constraint(expr= - m.x293 + m.x294 - m.x523 + m.x544 + m.x551 == 0)

m.c154 = Constraint(expr=   m.x295 == 0)

m.c155 = Constraint(expr= - m.x295 + m.x296 - m.x524 + m.x552 == 0)

m.c156 = Constraint(expr= - m.x296 + m.x297 - m.x525 + m.x553 == 0)

m.c157 = Constraint(expr= - m.x297 + m.x298 - m.x526 + m.x554 == 0)

m.c158 = Constraint(expr= - m.x298 + m.x299 - m.x527 + m.x555 == 0)

m.c159 = Constraint(expr= - m.x299 + m.x300 - m.x528 + m.x556 == 0)

m.c160 = Constraint(expr= - m.x300 + m.x301 - m.x529 + m.x557 == 0)

m.c161 = Constraint(expr= - m.x301 + m.x302 - m.x530 + m.x558 == 0)

m.c162 = Constraint(expr=   m.x303 == 200)

m.c163 = Constraint(expr= - m.x303 + m.x304 + m.x559 + m.x566 == 0)

m.c164 = Constraint(expr= - m.x304 + m.x305 + m.x560 + m.x567 == 0)

m.c165 = Constraint(expr= - m.x305 + m.x306 + m.x561 + m.x568 == 0)

m.c166 = Constraint(expr= - m.x306 + m.x307 + m.x562 + m.x569 == 0)

m.c167 = Constraint(expr= - m.x307 + m.x308 + m.x563 + m.x570 == 0)

m.c168 = Constraint(expr= - m.x308 + m.x309 + m.x564 + m.x571 == 0)

m.c169 = Constraint(expr= - m.x309 + m.x310 + m.x565 + m.x572 == 0)

m.c170 = Constraint(expr=   m.x311 == 0)

m.c171 = Constraint(expr= - m.x311 + m.x312 - m.x559 + m.x573 + m.x580 == 0)

m.c172 = Constraint(expr= - m.x312 + m.x313 - m.x560 + m.x574 + m.x581 == 0)

m.c173 = Constraint(expr= - m.x313 + m.x314 - m.x561 + m.x575 + m.x582 == 0)

m.c174 = Constraint(expr= - m.x314 + m.x315 - m.x562 + m.x576 + m.x583 == 0)

m.c175 = Constraint(expr= - m.x315 + m.x316 - m.x563 + m.x577 + m.x584 == 0)

m.c176 = Constraint(expr= - m.x316 + m.x317 - m.x564 + m.x578 + m.x585 == 0)

m.c177 = Constraint(expr= - m.x317 + m.x318 - m.x565 + m.x579 + m.x586 == 0)

m.c178 = Constraint(expr=   m.x319 == 300)

m.c179 = Constraint(expr= - m.x319 + m.x320 - m.x566 + m.x587 == 0)

m.c180 = Constraint(expr= - m.x320 + m.x321 - m.x567 + m.x588 == 0)

m.c181 = Constraint(expr= - m.x321 + m.x322 - m.x568 + m.x589 == 0)

m.c182 = Constraint(expr= - m.x322 + m.x323 - m.x569 + m.x590 == 0)

m.c183 = Constraint(expr= - m.x323 + m.x324 - m.x570 + m.x591 == 0)

m.c184 = Constraint(expr= - m.x324 + m.x325 - m.x571 + m.x592 == 0)

m.c185 = Constraint(expr= - m.x325 + m.x326 - m.x572 + m.x593 == 0)

m.c186 = Constraint(expr=   m.x327 == 300)

m.c187 = Constraint(expr= - m.x327 + m.x328 + m.x594 == 0)

m.c188 = Constraint(expr= - m.x328 + m.x329 + m.x595 == 0)

m.c189 = Constraint(expr= - m.x329 + m.x330 + m.x596 == 0)

m.c190 = Constraint(expr= - m.x330 + m.x331 + m.x597 == 0)

m.c191 = Constraint(expr= - m.x331 + m.x332 + m.x598 == 0)

m.c192 = Constraint(expr= - m.x332 + m.x333 + m.x599 == 0)

m.c193 = Constraint(expr= - m.x333 + m.x334 + m.x600 == 0)

m.c194 = Constraint(expr=   m.x152 + m.x248 <= 1000)

m.c195 = Constraint(expr=   m.x153 + m.x249 <= 1000)

m.c196 = Constraint(expr=   m.x154 + m.x250 <= 1000)

m.c197 = Constraint(expr=   m.x155 + m.x251 <= 1000)

m.c198 = Constraint(expr=   m.x156 + m.x252 <= 1000)

m.c199 = Constraint(expr=   m.x157 + m.x253 <= 1000)

m.c200 = Constraint(expr=   m.x158 + m.x254 <= 1000)

m.c201 = Constraint(expr=   m.x216 + m.x272 <= 1000)

m.c202 = Constraint(expr=   m.x217 + m.x273 <= 1000)

m.c203 = Constraint(expr=   m.x218 + m.x274 <= 1000)

m.c204 = Constraint(expr=   m.x219 + m.x275 <= 1000)

m.c205 = Constraint(expr=   m.x220 + m.x276 <= 1000)

m.c206 = Constraint(expr=   m.x221 + m.x277 <= 1000)

m.c207 = Constraint(expr=   m.x222 + m.x278 <= 1000)

m.c208 = Constraint(expr=   m.x184 + m.x304 <= 1000)

m.c209 = Constraint(expr=   m.x185 + m.x305 <= 1000)

m.c210 = Constraint(expr=   m.x186 + m.x306 <= 1000)

m.c211 = Constraint(expr=   m.x187 + m.x307 <= 1000)

m.c212 = Constraint(expr=   m.x188 + m.x308 <= 1000)

m.c213 = Constraint(expr=   m.x189 + m.x309 <= 1000)

m.c214 = Constraint(expr=   m.x190 + m.x310 <= 1000)

m.c215 = Constraint(expr=   m.x160 + m.x224 + m.x256 + m.x280 + m.x328 <= 1000)

m.c216 = Constraint(expr=   m.x161 + m.x225 + m.x257 + m.x281 + m.x329 <= 1000)

m.c217 = Constraint(expr=   m.x162 + m.x226 + m.x258 + m.x282 + m.x330 <= 1000)

m.c218 = Constraint(expr=   m.x163 + m.x227 + m.x259 + m.x283 + m.x331 <= 1000)

m.c219 = Constraint(expr=   m.x164 + m.x228 + m.x260 + m.x284 + m.x332 <= 1000)

m.c220 = Constraint(expr=   m.x165 + m.x229 + m.x261 + m.x285 + m.x333 <= 1000)

m.c221 = Constraint(expr=   m.x166 + m.x230 + m.x262 + m.x286 + m.x334 <= 1000)

m.c222 = Constraint(expr=   m.x168 + m.x192 + m.x232 + m.x264 + m.x288 + m.x312 <= 1000)

m.c223 = Constraint(expr=   m.x169 + m.x193 + m.x233 + m.x265 + m.x289 + m.x313 <= 1000)

m.c224 = Constraint(expr=   m.x170 + m.x194 + m.x234 + m.x266 + m.x290 + m.x314 <= 1000)

m.c225 = Constraint(expr=   m.x171 + m.x195 + m.x235 + m.x267 + m.x291 + m.x315 <= 1000)

m.c226 = Constraint(expr=   m.x172 + m.x196 + m.x236 + m.x268 + m.x292 + m.x316 <= 1000)

m.c227 = Constraint(expr=   m.x173 + m.x197 + m.x237 + m.x269 + m.x293 + m.x317 <= 1000)

m.c228 = Constraint(expr=   m.x174 + m.x198 + m.x238 + m.x270 + m.x294 + m.x318 <= 1000)

m.c229 = Constraint(expr=   m.x200 + m.x240 + m.x296 + m.x320 <= 1000)

m.c230 = Constraint(expr=   m.x201 + m.x241 + m.x297 + m.x321 <= 1000)

m.c231 = Constraint(expr=   m.x202 + m.x242 + m.x298 + m.x322 <= 1000)

m.c232 = Constraint(expr=   m.x203 + m.x243 + m.x299 + m.x323 <= 1000)

m.c233 = Constraint(expr=   m.x204 + m.x244 + m.x300 + m.x324 <= 1000)

m.c234 = Constraint(expr=   m.x205 + m.x245 + m.x301 + m.x325 <= 1000)

m.c235 = Constraint(expr=   m.x206 + m.x246 + m.x302 + m.x326 <= 1000)

m.c236 = Constraint(expr=   m.x152 + m.x248 >= 0)

m.c237 = Constraint(expr=   m.x153 + m.x249 >= 0)

m.c238 = Constraint(expr=   m.x154 + m.x250 >= 0)

m.c239 = Constraint(expr=   m.x155 + m.x251 >= 0)

m.c240 = Constraint(expr=   m.x156 + m.x252 >= 0)

m.c241 = Constraint(expr=   m.x157 + m.x253 >= 0)

m.c242 = Constraint(expr=   m.x158 + m.x254 >= 0)

m.c243 = Constraint(expr=   m.x216 + m.x272 >= 0)

m.c244 = Constraint(expr=   m.x217 + m.x273 >= 0)

m.c245 = Constraint(expr=   m.x218 + m.x274 >= 0)

m.c246 = Constraint(expr=   m.x219 + m.x275 >= 0)

m.c247 = Constraint(expr=   m.x220 + m.x276 >= 0)

m.c248 = Constraint(expr=   m.x221 + m.x277 >= 0)

m.c249 = Constraint(expr=   m.x222 + m.x278 >= 0)

m.c250 = Constraint(expr=   m.x184 + m.x304 >= 0)

m.c251 = Constraint(expr=   m.x185 + m.x305 >= 0)

m.c252 = Constraint(expr=   m.x186 + m.x306 >= 0)

m.c253 = Constraint(expr=   m.x187 + m.x307 >= 0)

m.c254 = Constraint(expr=   m.x188 + m.x308 >= 0)

m.c255 = Constraint(expr=   m.x189 + m.x309 >= 0)

m.c256 = Constraint(expr=   m.x190 + m.x310 >= 0)

m.c257 = Constraint(expr=   m.x160 + m.x224 + m.x256 + m.x280 + m.x328 >= 0)

m.c258 = Constraint(expr=   m.x161 + m.x225 + m.x257 + m.x281 + m.x329 >= 0)

m.c259 = Constraint(expr=   m.x162 + m.x226 + m.x258 + m.x282 + m.x330 >= 0)

m.c260 = Constraint(expr=   m.x163 + m.x227 + m.x259 + m.x283 + m.x331 >= 0)

m.c261 = Constraint(expr=   m.x164 + m.x228 + m.x260 + m.x284 + m.x332 >= 0)

m.c262 = Constraint(expr=   m.x165 + m.x229 + m.x261 + m.x285 + m.x333 >= 0)

m.c263 = Constraint(expr=   m.x166 + m.x230 + m.x262 + m.x286 + m.x334 >= 0)

m.c264 = Constraint(expr=   m.x168 + m.x192 + m.x232 + m.x264 + m.x288 + m.x312 >= 0)

m.c265 = Constraint(expr=   m.x169 + m.x193 + m.x233 + m.x265 + m.x289 + m.x313 >= 0)

m.c266 = Constraint(expr=   m.x170 + m.x194 + m.x234 + m.x266 + m.x290 + m.x314 >= 0)

m.c267 = Constraint(expr=   m.x171 + m.x195 + m.x235 + m.x267 + m.x291 + m.x315 >= 0)

m.c268 = Constraint(expr=   m.x172 + m.x196 + m.x236 + m.x268 + m.x292 + m.x316 >= 0)

m.c269 = Constraint(expr=   m.x173 + m.x197 + m.x237 + m.x269 + m.x293 + m.x317 >= 0)

m.c270 = Constraint(expr=   m.x174 + m.x198 + m.x238 + m.x270 + m.x294 + m.x318 >= 0)

m.c271 = Constraint(expr=   m.x200 + m.x240 + m.x296 + m.x320 >= 0)

m.c272 = Constraint(expr=   m.x201 + m.x241 + m.x297 + m.x321 >= 0)

m.c273 = Constraint(expr=   m.x202 + m.x242 + m.x298 + m.x322 >= 0)

m.c274 = Constraint(expr=   m.x203 + m.x243 + m.x299 + m.x323 >= 0)

m.c275 = Constraint(expr=   m.x204 + m.x244 + m.x300 + m.x324 >= 0)

m.c276 = Constraint(expr=   m.x205 + m.x245 + m.x301 + m.x325 >= 0)

m.c277 = Constraint(expr=   m.x206 + m.x246 + m.x302 + m.x326 >= 0)

m.c278 = Constraint(expr= - 0.02*m.x152 - 0.01*m.x248 <= 0)

m.c279 = Constraint(expr= - 0.02*m.x153 - 0.01*m.x249 <= 0)

m.c280 = Constraint(expr= - 0.02*m.x154 - 0.01*m.x250 <= 0)

m.c281 = Constraint(expr= - 0.02*m.x155 - 0.01*m.x251 <= 0)

m.c282 = Constraint(expr= - 0.02*m.x156 - 0.01*m.x252 <= 0)

m.c283 = Constraint(expr= - 0.02*m.x157 - 0.01*m.x253 <= 0)

m.c284 = Constraint(expr= - 0.02*m.x158 - 0.01*m.x254 <= 0)

m.c285 = Constraint(expr= - 0.01*m.x272 <= 0)

m.c286 = Constraint(expr= - 0.01*m.x273 <= 0)

m.c287 = Constraint(expr= - 0.01*m.x274 <= 0)

m.c288 = Constraint(expr= - 0.01*m.x275 <= 0)

m.c289 = Constraint(expr= - 0.01*m.x276 <= 0)

m.c290 = Constraint(expr= - 0.01*m.x277 <= 0)

m.c291 = Constraint(expr= - 0.01*m.x278 <= 0)

m.c292 = Constraint(expr= - 0.00499999999999999*m.x184 - 0.01*m.x304 <= 0)

m.c293 = Constraint(expr= - 0.00499999999999999*m.x185 - 0.01*m.x305 <= 0)

m.c294 = Constraint(expr= - 0.00499999999999999*m.x186 - 0.01*m.x306 <= 0)

m.c295 = Constraint(expr= - 0.00499999999999999*m.x187 - 0.01*m.x307 <= 0)

m.c296 = Constraint(expr= - 0.00499999999999999*m.x188 - 0.01*m.x308 <= 0)

m.c297 = Constraint(expr= - 0.00499999999999999*m.x189 - 0.01*m.x309 <= 0)

m.c298 = Constraint(expr= - 0.00499999999999999*m.x190 - 0.01*m.x310 <= 0)

m.c299 = Constraint(expr= - 0.025*m.x160 + 0.025*m.x224 - 0.015*m.x256 + 0.015*m.x280 - 0.005*m.x328 <= 0)

m.c300 = Constraint(expr= - 0.025*m.x161 + 0.025*m.x225 - 0.015*m.x257 + 0.015*m.x281 - 0.005*m.x329 <= 0)

m.c301 = Constraint(expr= - 0.025*m.x162 + 0.025*m.x226 - 0.015*m.x258 + 0.015*m.x282 - 0.005*m.x330 <= 0)

m.c302 = Constraint(expr= - 0.025*m.x163 + 0.025*m.x227 - 0.015*m.x259 + 0.015*m.x283 - 0.005*m.x331 <= 0)

m.c303 = Constraint(expr= - 0.025*m.x164 + 0.025*m.x228 - 0.015*m.x260 + 0.015*m.x284 - 0.005*m.x332 <= 0)

m.c304 = Constraint(expr= - 0.025*m.x165 + 0.025*m.x229 - 0.015*m.x261 + 0.015*m.x285 - 0.005*m.x333 <= 0)

m.c305 = Constraint(expr= - 0.025*m.x166 + 0.025*m.x230 - 0.015*m.x262 + 0.015*m.x286 - 0.005*m.x334 <= 0)

m.c306 = Constraint(expr= - 0.055*m.x168 + 0.02*m.x192 - 0.005*m.x232 - 0.045*m.x264 - 0.015*m.x288 + 0.015*m.x312 <= 0)

m.c307 = Constraint(expr= - 0.055*m.x169 + 0.02*m.x193 - 0.005*m.x233 - 0.045*m.x265 - 0.015*m.x289 + 0.015*m.x313 <= 0)

m.c308 = Constraint(expr= - 0.055*m.x170 + 0.02*m.x194 - 0.005*m.x234 - 0.045*m.x266 - 0.015*m.x290 + 0.015*m.x314 <= 0)

m.c309 = Constraint(expr= - 0.055*m.x171 + 0.02*m.x195 - 0.005*m.x235 - 0.045*m.x267 - 0.015*m.x291 + 0.015*m.x315 <= 0)

m.c310 = Constraint(expr= - 0.055*m.x172 + 0.02*m.x196 - 0.005*m.x236 - 0.045*m.x268 - 0.015*m.x292 + 0.015*m.x316 <= 0)

m.c311 = Constraint(expr= - 0.055*m.x173 + 0.02*m.x197 - 0.005*m.x237 - 0.045*m.x269 - 0.015*m.x293 + 0.015*m.x317 <= 0)

m.c312 = Constraint(expr= - 0.055*m.x174 + 0.02*m.x198 - 0.005*m.x238 - 0.045*m.x270 - 0.015*m.x294 + 0.015*m.x318 <= 0)

m.c313 = Constraint(expr= - 0.025*m.x240 - 0.035*m.x296 - 0.005*m.x320 <= 0)

m.c314 = Constraint(expr= - 0.025*m.x241 - 0.035*m.x297 - 0.005*m.x321 <= 0)

m.c315 = Constraint(expr= - 0.025*m.x242 - 0.035*m.x298 - 0.005*m.x322 <= 0)

m.c316 = Constraint(expr= - 0.025*m.x243 - 0.035*m.x299 - 0.005*m.x323 <= 0)

m.c317 = Constraint(expr= - 0.025*m.x244 - 0.035*m.x300 - 0.005*m.x324 <= 0)

m.c318 = Constraint(expr= - 0.025*m.x245 - 0.035*m.x301 - 0.005*m.x325 <= 0)

m.c319 = Constraint(expr= - 0.025*m.x246 - 0.035*m.x302 - 0.005*m.x326 <= 0)

m.c320 = Constraint(expr=   0.01*m.x248 >= 0)

m.c321 = Constraint(expr=   0.01*m.x249 >= 0)

m.c322 = Constraint(expr=   0.01*m.x250 >= 0)

m.c323 = Constraint(expr=   0.01*m.x251 >= 0)

m.c324 = Constraint(expr=   0.01*m.x252 >= 0)

m.c325 = Constraint(expr=   0.01*m.x253 >= 0)

m.c326 = Constraint(expr=   0.01*m.x254 >= 0)

m.c327 = Constraint(expr=   0.02*m.x216 + 0.01*m.x272 >= 0)

m.c328 = Constraint(expr=   0.02*m.x217 + 0.01*m.x273 >= 0)

m.c329 = Constraint(expr=   0.02*m.x218 + 0.01*m.x274 >= 0)

m.c330 = Constraint(expr=   0.02*m.x219 + 0.01*m.x275 >= 0)

m.c331 = Constraint(expr=   0.02*m.x220 + 0.01*m.x276 >= 0)

m.c332 = Constraint(expr=   0.02*m.x221 + 0.01*m.x277 >= 0)

m.c333 = Constraint(expr=   0.02*m.x222 + 0.01*m.x278 >= 0)

m.c334 = Constraint(expr=   0.015*m.x184 + 0.01*m.x304 >= 0)

m.c335 = Constraint(expr=   0.015*m.x185 + 0.01*m.x305 >= 0)

m.c336 = Constraint(expr=   0.015*m.x186 + 0.01*m.x306 >= 0)

m.c337 = Constraint(expr=   0.015*m.x187 + 0.01*m.x307 >= 0)

m.c338 = Constraint(expr=   0.015*m.x188 + 0.01*m.x308 >= 0)

m.c339 = Constraint(expr=   0.015*m.x189 + 0.01*m.x309 >= 0)

m.c340 = Constraint(expr=   0.015*m.x190 + 0.01*m.x310 >= 0)

m.c341 = Constraint(expr= - 0.015*m.x160 + 0.035*m.x224 - 0.005*m.x256 + 0.025*m.x280 + 0.005*m.x328 >= 0)

m.c342 = Constraint(expr= - 0.015*m.x161 + 0.035*m.x225 - 0.005*m.x257 + 0.025*m.x281 + 0.005*m.x329 >= 0)

m.c343 = Constraint(expr= - 0.015*m.x162 + 0.035*m.x226 - 0.005*m.x258 + 0.025*m.x282 + 0.005*m.x330 >= 0)

m.c344 = Constraint(expr= - 0.015*m.x163 + 0.035*m.x227 - 0.005*m.x259 + 0.025*m.x283 + 0.005*m.x331 >= 0)

m.c345 = Constraint(expr= - 0.015*m.x164 + 0.035*m.x228 - 0.005*m.x260 + 0.025*m.x284 + 0.005*m.x332 >= 0)

m.c346 = Constraint(expr= - 0.015*m.x165 + 0.035*m.x229 - 0.005*m.x261 + 0.025*m.x285 + 0.005*m.x333 >= 0)

m.c347 = Constraint(expr= - 0.015*m.x166 + 0.035*m.x230 - 0.005*m.x262 + 0.025*m.x286 + 0.005*m.x334 >= 0)

m.c348 = Constraint(expr= - 0.035*m.x168 + 0.04*m.x192 + 0.015*m.x232 - 0.025*m.x264 + 0.005*m.x288 + 0.035*m.x312 >= 0)

m.c349 = Constraint(expr= - 0.035*m.x169 + 0.04*m.x193 + 0.015*m.x233 - 0.025*m.x265 + 0.005*m.x289 + 0.035*m.x313 >= 0)

m.c350 = Constraint(expr= - 0.035*m.x170 + 0.04*m.x194 + 0.015*m.x234 - 0.025*m.x266 + 0.005*m.x290 + 0.035*m.x314 >= 0)

m.c351 = Constraint(expr= - 0.035*m.x171 + 0.04*m.x195 + 0.015*m.x235 - 0.025*m.x267 + 0.005*m.x291 + 0.035*m.x315 >= 0)

m.c352 = Constraint(expr= - 0.035*m.x172 + 0.04*m.x196 + 0.015*m.x236 - 0.025*m.x268 + 0.005*m.x292 + 0.035*m.x316 >= 0)

m.c353 = Constraint(expr= - 0.035*m.x173 + 0.04*m.x197 + 0.015*m.x237 - 0.025*m.x269 + 0.005*m.x293 + 0.035*m.x317 >= 0)

m.c354 = Constraint(expr= - 0.035*m.x174 + 0.04*m.x198 + 0.015*m.x238 - 0.025*m.x270 + 0.005*m.x294 + 0.035*m.x318 >= 0)

m.c355 = Constraint(expr=   0.01*m.x200 - 0.015*m.x240 - 0.025*m.x296 + 0.005*m.x320 >= 0)

m.c356 = Constraint(expr=   0.01*m.x201 - 0.015*m.x241 - 0.025*m.x297 + 0.005*m.x321 >= 0)

m.c357 = Constraint(expr=   0.01*m.x202 - 0.015*m.x242 - 0.025*m.x298 + 0.005*m.x322 >= 0)

m.c358 = Constraint(expr=   0.01*m.x203 - 0.015*m.x243 - 0.025*m.x299 + 0.005*m.x323 >= 0)

m.c359 = Constraint(expr=   0.01*m.x204 - 0.015*m.x244 - 0.025*m.x300 + 0.005*m.x324 >= 0)

m.c360 = Constraint(expr=   0.01*m.x205 - 0.015*m.x245 - 0.025*m.x301 + 0.005*m.x325 >= 0)

m.c361 = Constraint(expr=   0.01*m.x206 - 0.015*m.x246 - 0.025*m.x302 + 0.005*m.x326 >= 0)

m.c362 = Constraint(expr=   m.b1 + m.b22 <= 1)

m.c363 = Constraint(expr=   m.b2 + m.b23 <= 1)

m.c364 = Constraint(expr=   m.b3 + m.b24 <= 1)

m.c365 = Constraint(expr=   m.b4 + m.b25 <= 1)

m.c366 = Constraint(expr=   m.b5 + m.b26 <= 1)

m.c367 = Constraint(expr=   m.b6 + m.b27 <= 1)

m.c368 = Constraint(expr=   m.b7 + m.b28 <= 1)

m.c369 = Constraint(expr=   m.b1 + m.b29 <= 1)

m.c370 = Constraint(expr=   m.b2 + m.b30 <= 1)

m.c371 = Constraint(expr=   m.b3 + m.b31 <= 1)

m.c372 = Constraint(expr=   m.b4 + m.b32 <= 1)

m.c373 = Constraint(expr=   m.b5 + m.b33 <= 1)

m.c374 = Constraint(expr=   m.b6 + m.b34 <= 1)

m.c375 = Constraint(expr=   m.b7 + m.b35 <= 1)

m.c376 = Constraint(expr=   m.b15 + m.b36 <= 1)

m.c377 = Constraint(expr=   m.b16 + m.b37 <= 1)

m.c378 = Constraint(expr=   m.b17 + m.b38 <= 1)

m.c379 = Constraint(expr=   m.b18 + m.b39 <= 1)

m.c380 = Constraint(expr=   m.b19 + m.b40 <= 1)

m.c381 = Constraint(expr=   m.b20 + m.b41 <= 1)

m.c382 = Constraint(expr=   m.b21 + m.b42 <= 1)

m.c383 = Constraint(expr=   m.b15 + m.b43 <= 1)

m.c384 = Constraint(expr=   m.b16 + m.b44 <= 1)

m.c385 = Constraint(expr=   m.b17 + m.b45 <= 1)

m.c386 = Constraint(expr=   m.b18 + m.b46 <= 1)

m.c387 = Constraint(expr=   m.b19 + m.b47 <= 1)

m.c388 = Constraint(expr=   m.b20 + m.b48 <= 1)

m.c389 = Constraint(expr=   m.b21 + m.b49 <= 1)

m.c390 = Constraint(expr=   m.b15 + m.b50 <= 1)

m.c391 = Constraint(expr=   m.b16 + m.b51 <= 1)

m.c392 = Constraint(expr=   m.b17 + m.b52 <= 1)

m.c393 = Constraint(expr=   m.b18 + m.b53 <= 1)

m.c394 = Constraint(expr=   m.b19 + m.b54 <= 1)

m.c395 = Constraint(expr=   m.b20 + m.b55 <= 1)

m.c396 = Constraint(expr=   m.b21 + m.b56 <= 1)

m.c397 = Constraint(expr=   m.b8 + m.b57 <= 1)

m.c398 = Constraint(expr=   m.b9 + m.b58 <= 1)

m.c399 = Constraint(expr=   m.b10 + m.b59 <= 1)

m.c400 = Constraint(expr=   m.b11 + m.b60 <= 1)

m.c401 = Constraint(expr=   m.b12 + m.b61 <= 1)

m.c402 = Constraint(expr=   m.b13 + m.b62 <= 1)

m.c403 = Constraint(expr=   m.b14 + m.b63 <= 1)

m.c404 = Constraint(expr=   m.b8 + m.b64 <= 1)

m.c405 = Constraint(expr=   m.b9 + m.b65 <= 1)

m.c406 = Constraint(expr=   m.b10 + m.b66 <= 1)

m.c407 = Constraint(expr=   m.b11 + m.b67 <= 1)

m.c408 = Constraint(expr=   m.b12 + m.b68 <= 1)

m.c409 = Constraint(expr=   m.b13 + m.b69 <= 1)

m.c410 = Constraint(expr=   m.b14 + m.b70 <= 1)

m.c411 = Constraint(expr=   m.b22 + m.b71 <= 1)

m.c412 = Constraint(expr=   m.b23 + m.b72 <= 1)

m.c413 = Constraint(expr=   m.b24 + m.b73 <= 1)

m.c414 = Constraint(expr=   m.b25 + m.b74 <= 1)

m.c415 = Constraint(expr=   m.b26 + m.b75 <= 1)

m.c416 = Constraint(expr=   m.b27 + m.b76 <= 1)

m.c417 = Constraint(expr=   m.b28 + m.b77 <= 1)

m.c418 = Constraint(expr=   m.b36 + m.b71 <= 1)

m.c419 = Constraint(expr=   m.b37 + m.b72 <= 1)

m.c420 = Constraint(expr=   m.b38 + m.b73 <= 1)

m.c421 = Constraint(expr=   m.b39 + m.b74 <= 1)

m.c422 = Constraint(expr=   m.b40 + m.b75 <= 1)

m.c423 = Constraint(expr=   m.b41 + m.b76 <= 1)

m.c424 = Constraint(expr=   m.b42 + m.b77 <= 1)

m.c425 = Constraint(expr=   m.b29 + m.b78 + m.b85 <= 1)

m.c426 = Constraint(expr=   m.b30 + m.b79 + m.b86 <= 1)

m.c427 = Constraint(expr=   m.b31 + m.b80 + m.b87 <= 1)

m.c428 = Constraint(expr=   m.b32 + m.b81 + m.b88 <= 1)

m.c429 = Constraint(expr=   m.b33 + m.b82 + m.b89 <= 1)

m.c430 = Constraint(expr=   m.b34 + m.b83 + m.b90 <= 1)

m.c431 = Constraint(expr=   m.b35 + m.b84 + m.b91 <= 1)

m.c432 = Constraint(expr=   m.b43 + m.b78 + m.b85 <= 1)

m.c433 = Constraint(expr=   m.b44 + m.b79 + m.b86 <= 1)

m.c434 = Constraint(expr=   m.b45 + m.b80 + m.b87 <= 1)

m.c435 = Constraint(expr=   m.b46 + m.b81 + m.b88 <= 1)

m.c436 = Constraint(expr=   m.b47 + m.b82 + m.b89 <= 1)

m.c437 = Constraint(expr=   m.b48 + m.b83 + m.b90 <= 1)

m.c438 = Constraint(expr=   m.b49 + m.b84 + m.b91 <= 1)

m.c439 = Constraint(expr=   m.b57 + m.b78 + m.b85 <= 1)

m.c440 = Constraint(expr=   m.b58 + m.b79 + m.b86 <= 1)

m.c441 = Constraint(expr=   m.b59 + m.b80 + m.b87 <= 1)

m.c442 = Constraint(expr=   m.b60 + m.b81 + m.b88 <= 1)

m.c443 = Constraint(expr=   m.b61 + m.b82 + m.b89 <= 1)

m.c444 = Constraint(expr=   m.b62 + m.b83 + m.b90 <= 1)

m.c445 = Constraint(expr=   m.b63 + m.b84 + m.b91 <= 1)

m.c446 = Constraint(expr=   m.b50 + m.b92 <= 1)

m.c447 = Constraint(expr=   m.b51 + m.b93 <= 1)

m.c448 = Constraint(expr=   m.b52 + m.b94 <= 1)

m.c449 = Constraint(expr=   m.b53 + m.b95 <= 1)

m.c450 = Constraint(expr=   m.b54 + m.b96 <= 1)

m.c451 = Constraint(expr=   m.b55 + m.b97 <= 1)

m.c452 = Constraint(expr=   m.b56 + m.b98 <= 1)

m.c453 = Constraint(expr=   m.b64 + m.b92 <= 1)

m.c454 = Constraint(expr=   m.b65 + m.b93 <= 1)

m.c455 = Constraint(expr=   m.b66 + m.b94 <= 1)

m.c456 = Constraint(expr=   m.b67 + m.b95 <= 1)

m.c457 = Constraint(expr=   m.b68 + m.b96 <= 1)

m.c458 = Constraint(expr=   m.b69 + m.b97 <= 1)

m.c459 = Constraint(expr=   m.b70 + m.b98 <= 1)

m.c460 = Constraint(expr=   m.x150 == 0)

m.c461 = Constraint(expr=   m.x182 == 0)

m.c462 = Constraint(expr=   m.x214 == 0)

m.c463 = Constraint(expr=   m.x356 + m.x357 + m.x358 + m.x359 + m.x360 + m.x361 + m.x362 + m.x447 + m.x448 + m.x449
                          + m.x450 + m.x451 + m.x452 + m.x453 + m.x489 + m.x490 + m.x491 + m.x492 + m.x493 + m.x494
                          + m.x495 + m.x531 + m.x532 + m.x533 + m.x534 + m.x535 + m.x536 + m.x537 + m.x594 + m.x595
                          + m.x596 + m.x597 + m.x598 + m.x599 + m.x600 == 500)

m.c464 = Constraint(expr=   m.x363 + m.x364 + m.x365 + m.x366 + m.x367 + m.x368 + m.x369 + m.x370 + m.x371 + m.x372
                          + m.x373 + m.x374 + m.x375 + m.x376 + m.x398 + m.x399 + m.x400 + m.x401 + m.x402 + m.x403
                          + m.x404 + m.x405 + m.x406 + m.x407 + m.x408 + m.x409 + m.x410 + m.x411 + m.x454 + m.x455
                          + m.x456 + m.x457 + m.x458 + m.x459 + m.x460 + m.x461 + m.x462 + m.x463 + m.x464 + m.x465
                          + m.x466 + m.x467 + m.x496 + m.x497 + m.x498 + m.x499 + m.x500 + m.x501 + m.x502 + m.x503
                          + m.x504 + m.x505 + m.x506 + m.x507 + m.x508 + m.x509 + m.x538 + m.x539 + m.x540 + m.x541
                          + m.x542 + m.x543 + m.x544 + m.x545 + m.x546 + m.x547 + m.x548 + m.x549 + m.x550 + m.x551
                          + m.x573 + m.x574 + m.x575 + m.x576 + m.x577 + m.x578 + m.x579 + m.x580 + m.x581 + m.x582
                          + m.x583 + m.x584 + m.x585 + m.x586 == 500)

m.c465 = Constraint(expr=   m.x412 + m.x413 + m.x414 + m.x415 + m.x416 + m.x417 + m.x418 + m.x468 + m.x469 + m.x470
                          + m.x471 + m.x472 + m.x473 + m.x474 + m.x552 + m.x553 + m.x554 + m.x555 + m.x556 + m.x557
                          + m.x558 + m.x587 + m.x588 + m.x589 + m.x590 + m.x591 + m.x592 + m.x593 == 500)

m.c466 = Constraint(expr=   m.b99 + m.b100 + m.b102 + m.b105 + m.b108 == 1)

m.c467 = Constraint(expr=   m.b101 + m.b103 + m.b106 + m.b109 + m.b111 == 1)

m.c468 = Constraint(expr=   m.b104 + m.b107 + m.b110 + m.b112 + m.b113 == 1)

m.c469 = Constraint(expr=   m.b114 + m.b115 + m.b117 + m.b120 + m.b123 == 1)

m.c470 = Constraint(expr=   m.b116 + m.b118 + m.b121 + m.b124 + m.b126 == 1)

m.c471 = Constraint(expr=   m.b119 + m.b122 + m.b125 + m.b127 + m.b128 == 1)

m.c472 = Constraint(expr=   m.b1 + m.b8 + m.b15 <= 1)

m.c473 = Constraint(expr=   m.b2 + m.b9 + m.b16 <= 1)

m.c474 = Constraint(expr=   m.b3 + m.b10 + m.b17 <= 1)

m.c475 = Constraint(expr=   m.b4 + m.b11 + m.b18 <= 1)

m.c476 = Constraint(expr=   m.b5 + m.b12 + m.b19 <= 1)

m.c477 = Constraint(expr=   m.b6 + m.b13 + m.b20 <= 1)

m.c478 = Constraint(expr=   m.b7 + m.b14 + m.b21 <= 1)

m.c479 = Constraint(expr=   m.b71 + m.b78 == 1)

m.c480 = Constraint(expr=   m.b72 + m.b79 == 1)

m.c481 = Constraint(expr=   m.b73 + m.b80 == 1)

m.c482 = Constraint(expr=   m.b74 + m.b81 == 1)

m.c483 = Constraint(expr=   m.b75 + m.b82 == 1)

m.c484 = Constraint(expr=   m.b76 + m.b83 == 1)

m.c485 = Constraint(expr=   m.b77 + m.b84 == 1)

m.c486 = Constraint(expr=   m.b85 + m.b92 == 1)

m.c487 = Constraint(expr=   m.b86 + m.b93 == 1)

m.c488 = Constraint(expr=   m.b87 + m.b94 == 1)

m.c489 = Constraint(expr=   m.b88 + m.b95 == 1)

m.c490 = Constraint(expr=   m.b89 + m.b96 == 1)

m.c491 = Constraint(expr=   m.b90 + m.b97 == 1)

m.c492 = Constraint(expr=   m.b91 + m.b98 == 1)

m.c493 = Constraint(expr=   m.b1 - m.b99 <= 0)

m.c494 = Constraint(expr=   m.b2 - m.b99 - m.b100 <= 0)

m.c495 = Constraint(expr=   m.b3 - m.b99 - m.b100 - m.b102 <= 0)

m.c496 = Constraint(expr=   m.b4 - m.b99 - m.b100 - m.b102 - m.b105 <= 0)

m.c497 = Constraint(expr=   m.b5 - m.b99 - m.b100 - m.b102 - m.b105 - m.b108 <= 0)

m.c498 = Constraint(expr=   m.b6 - m.b99 - m.b100 - m.b102 - m.b105 - m.b108 <= 0)

m.c499 = Constraint(expr=   m.b7 - m.b99 - m.b100 - m.b102 - m.b105 - m.b108 <= 0)

m.c500 = Constraint(expr=   m.b8 <= 0)

m.c501 = Constraint(expr=   m.b9 - m.b101 <= 0)

m.c502 = Constraint(expr=   m.b10 - m.b101 - m.b103 <= 0)

m.c503 = Constraint(expr=   m.b11 - m.b101 - m.b103 - m.b106 <= 0)

m.c504 = Constraint(expr=   m.b12 - m.b101 - m.b103 - m.b106 - m.b109 <= 0)

m.c505 = Constraint(expr=   m.b13 - m.b101 - m.b103 - m.b106 - m.b109 - m.b111 <= 0)

m.c506 = Constraint(expr=   m.b14 - m.b101 - m.b103 - m.b106 - m.b109 - m.b111 <= 0)

m.c507 = Constraint(expr=   m.b15 <= 0)

m.c508 = Constraint(expr=   m.b16 <= 0)

m.c509 = Constraint(expr=   m.b17 - m.b104 <= 0)

m.c510 = Constraint(expr=   m.b18 - m.b104 - m.b107 <= 0)

m.c511 = Constraint(expr=   m.b19 - m.b104 - m.b107 - m.b110 <= 0)

m.c512 = Constraint(expr=   m.b20 - m.b104 - m.b107 - m.b110 - m.b112 <= 0)

m.c513 = Constraint(expr=   m.b21 - m.b104 - m.b107 - m.b110 - m.b112 - m.b113 <= 0)

m.c514 = Constraint(expr=   m.b1 - m.b114 - m.b115 - m.b117 - m.b120 - m.b123 <= 0)

m.c515 = Constraint(expr=   m.b2 - m.b115 - m.b117 - m.b120 - m.b123 <= 0)

m.c516 = Constraint(expr=   m.b3 - m.b117 - m.b120 - m.b123 <= 0)

m.c517 = Constraint(expr=   m.b4 - m.b120 - m.b123 <= 0)

m.c518 = Constraint(expr=   m.b5 - m.b123 <= 0)

m.c519 = Constraint(expr=   m.b6 <= 0)

m.c520 = Constraint(expr=   m.b7 <= 0)

m.c521 = Constraint(expr=   m.b8 - m.b116 - m.b118 - m.b121 - m.b124 - m.b126 <= 0)

m.c522 = Constraint(expr=   m.b9 - m.b116 - m.b118 - m.b121 - m.b124 - m.b126 <= 0)

m.c523 = Constraint(expr=   m.b10 - m.b118 - m.b121 - m.b124 - m.b126 <= 0)

m.c524 = Constraint(expr=   m.b11 - m.b121 - m.b124 - m.b126 <= 0)

m.c525 = Constraint(expr=   m.b12 - m.b124 - m.b126 <= 0)

m.c526 = Constraint(expr=   m.b13 - m.b126 <= 0)

m.c527 = Constraint(expr=   m.b14 <= 0)

m.c528 = Constraint(expr=   m.b15 - m.b119 - m.b122 - m.b125 - m.b127 - m.b128 <= 0)

m.c529 = Constraint(expr=   m.b16 - m.b119 - m.b122 - m.b125 - m.b127 - m.b128 <= 0)

m.c530 = Constraint(expr=   m.b17 - m.b119 - m.b122 - m.b125 - m.b127 - m.b128 <= 0)

m.c531 = Constraint(expr=   m.b18 - m.b122 - m.b125 - m.b127 - m.b128 <= 0)

m.c532 = Constraint(expr=   m.b19 - m.b125 - m.b127 - m.b128 <= 0)

m.c533 = Constraint(expr=   m.b20 - m.b127 - m.b128 <= 0)

m.c534 = Constraint(expr=   m.b21 - m.b128 <= 0)

m.c535 = Constraint(expr= - m.b71 - m.b79 + m.x129 >= -1)

m.c536 = Constraint(expr= - m.b72 - m.b80 + m.x130 >= -1)

m.c537 = Constraint(expr= - m.b73 - m.b81 + m.x131 >= -1)

m.c538 = Constraint(expr= - m.b74 - m.b82 + m.x132 >= -1)

m.c539 = Constraint(expr= - m.b75 - m.b83 + m.x133 >= -1)

m.c540 = Constraint(expr= - m.b76 - m.b84 + m.x134 >= -1)

m.c541 = Constraint(expr= - m.b85 - m.b93 + m.x135 >= -1)

m.c542 = Constraint(expr= - m.b86 - m.b94 + m.x136 >= -1)

m.c543 = Constraint(expr= - m.b87 - m.b95 + m.x137 >= -1)

m.c544 = Constraint(expr= - m.b88 - m.b96 + m.x138 >= -1)

m.c545 = Constraint(expr= - m.b89 - m.b97 + m.x139 >= -1)

m.c546 = Constraint(expr= - m.b90 - m.b98 + m.x140 >= -1)

m.c547 = Constraint(expr= - m.b72 - m.b78 + m.x129 >= -1)

m.c548 = Constraint(expr= - m.b73 - m.b79 + m.x130 >= -1)

m.c549 = Constraint(expr= - m.b74 - m.b80 + m.x131 >= -1)

m.c550 = Constraint(expr= - m.b75 - m.b81 + m.x132 >= -1)

m.c551 = Constraint(expr= - m.b76 - m.b82 + m.x133 >= -1)

m.c552 = Constraint(expr= - m.b77 - m.b83 + m.x134 >= -1)

m.c553 = Constraint(expr= - m.b86 - m.b92 + m.x135 >= -1)

m.c554 = Constraint(expr= - m.b87 - m.b93 + m.x136 >= -1)

m.c555 = Constraint(expr= - m.b88 - m.b94 + m.x137 >= -1)

m.c556 = Constraint(expr= - m.b89 - m.b95 + m.x138 >= -1)

m.c557 = Constraint(expr= - m.b90 - m.b96 + m.x139 >= -1)

m.c558 = Constraint(expr= - m.b91 - m.b97 + m.x140 >= -1)

m.c559 = Constraint(expr=   m.x129 + m.x130 + m.x131 + m.x132 + m.x133 + m.x134 - m.x141 == -1)

m.c560 = Constraint(expr=   m.x135 + m.x136 + m.x137 + m.x138 + m.x139 + m.x140 - m.x142 == -1)

m.c561 = Constraint(expr= - 0.5*m.x151 - 0.5*m.x152 - 0.5*m.x247 - 0.5*m.x248 + m.x688 == 0)

m.c562 = Constraint(expr= - 0.5*m.x152 - 0.5*m.x153 - 0.5*m.x248 - 0.5*m.x249 + m.x689 == 0)

m.c563 = Constraint(expr= - 0.5*m.x153 - 0.5*m.x154 - 0.5*m.x249 - 0.5*m.x250 + m.x690 == 0)

m.c564 = Constraint(expr= - 0.5*m.x154 - 0.5*m.x155 - 0.5*m.x250 - 0.5*m.x251 + m.x691 == 0)

m.c565 = Constraint(expr= - 0.5*m.x155 - 0.5*m.x156 - 0.5*m.x251 - 0.5*m.x252 + m.x692 == 0)

m.c566 = Constraint(expr= - 0.5*m.x156 - 0.5*m.x157 - 0.5*m.x252 - 0.5*m.x253 + m.x693 == 0)

m.c567 = Constraint(expr= - 0.5*m.x157 - 0.5*m.x158 - 0.5*m.x253 - 0.5*m.x254 + m.x694 == 0)

m.c568 = Constraint(expr= - 0.5*m.x215 - 0.5*m.x216 - 0.5*m.x271 - 0.5*m.x272 + m.x695 == 0)

m.c569 = Constraint(expr= - 0.5*m.x216 - 0.5*m.x217 - 0.5*m.x272 - 0.5*m.x273 + m.x696 == 0)

m.c570 = Constraint(expr= - 0.5*m.x217 - 0.5*m.x218 - 0.5*m.x273 - 0.5*m.x274 + m.x697 == 0)

m.c571 = Constraint(expr= - 0.5*m.x218 - 0.5*m.x219 - 0.5*m.x274 - 0.5*m.x275 + m.x698 == 0)

m.c572 = Constraint(expr= - 0.5*m.x219 - 0.5*m.x220 - 0.5*m.x275 - 0.5*m.x276 + m.x699 == 0)

m.c573 = Constraint(expr= - 0.5*m.x220 - 0.5*m.x221 - 0.5*m.x276 - 0.5*m.x277 + m.x700 == 0)

m.c574 = Constraint(expr= - 0.5*m.x221 - 0.5*m.x222 - 0.5*m.x277 - 0.5*m.x278 + m.x701 == 0)

m.c575 = Constraint(expr= - 0.5*m.x183 - 0.5*m.x184 - 0.5*m.x303 - 0.5*m.x304 + m.x702 == 0)

m.c576 = Constraint(expr= - 0.5*m.x184 - 0.5*m.x185 - 0.5*m.x304 - 0.5*m.x305 + m.x703 == 0)

m.c577 = Constraint(expr= - 0.5*m.x185 - 0.5*m.x186 - 0.5*m.x305 - 0.5*m.x306 + m.x704 == 0)

m.c578 = Constraint(expr= - 0.5*m.x186 - 0.5*m.x187 - 0.5*m.x306 - 0.5*m.x307 + m.x705 == 0)

m.c579 = Constraint(expr= - 0.5*m.x187 - 0.5*m.x188 - 0.5*m.x307 - 0.5*m.x308 + m.x706 == 0)

m.c580 = Constraint(expr= - 0.5*m.x188 - 0.5*m.x189 - 0.5*m.x308 - 0.5*m.x309 + m.x707 == 0)

m.c581 = Constraint(expr= - 0.5*m.x189 - 0.5*m.x190 - 0.5*m.x309 - 0.5*m.x310 + m.x708 == 0)

m.c582 = Constraint(expr= - 0.5*m.x159 - 0.5*m.x160 - 0.5*m.x223 - 0.5*m.x224 - 0.5*m.x255 - 0.5*m.x256 - 0.5*m.x279
                          - 0.5*m.x280 - 0.5*m.x327 - 0.5*m.x328 + m.x709 == 0)

m.c583 = Constraint(expr= - 0.5*m.x160 - 0.5*m.x161 - 0.5*m.x224 - 0.5*m.x225 - 0.5*m.x256 - 0.5*m.x257 - 0.5*m.x280
                          - 0.5*m.x281 - 0.5*m.x328 - 0.5*m.x329 + m.x710 == 0)

m.c584 = Constraint(expr= - 0.5*m.x161 - 0.5*m.x162 - 0.5*m.x225 - 0.5*m.x226 - 0.5*m.x257 - 0.5*m.x258 - 0.5*m.x281
                          - 0.5*m.x282 - 0.5*m.x329 - 0.5*m.x330 + m.x711 == 0)

m.c585 = Constraint(expr= - 0.5*m.x162 - 0.5*m.x163 - 0.5*m.x226 - 0.5*m.x227 - 0.5*m.x258 - 0.5*m.x259 - 0.5*m.x282
                          - 0.5*m.x283 - 0.5*m.x330 - 0.5*m.x331 + m.x712 == 0)

m.c586 = Constraint(expr= - 0.5*m.x163 - 0.5*m.x164 - 0.5*m.x227 - 0.5*m.x228 - 0.5*m.x259 - 0.5*m.x260 - 0.5*m.x283
                          - 0.5*m.x284 - 0.5*m.x331 - 0.5*m.x332 + m.x713 == 0)

m.c587 = Constraint(expr= - 0.5*m.x164 - 0.5*m.x165 - 0.5*m.x228 - 0.5*m.x229 - 0.5*m.x260 - 0.5*m.x261 - 0.5*m.x284
                          - 0.5*m.x285 - 0.5*m.x332 - 0.5*m.x333 + m.x714 == 0)

m.c588 = Constraint(expr= - 0.5*m.x165 - 0.5*m.x166 - 0.5*m.x229 - 0.5*m.x230 - 0.5*m.x261 - 0.5*m.x262 - 0.5*m.x285
                          - 0.5*m.x286 - 0.5*m.x333 - 0.5*m.x334 + m.x715 == 0)

m.c589 = Constraint(expr= - 0.5*m.x167 - 0.5*m.x168 - 0.5*m.x191 - 0.5*m.x192 - 0.5*m.x231 - 0.5*m.x232 - 0.5*m.x263
                          - 0.5*m.x264 - 0.5*m.x287 - 0.5*m.x288 - 0.5*m.x311 - 0.5*m.x312 + m.x716 == 0)

m.c590 = Constraint(expr= - 0.5*m.x168 - 0.5*m.x169 - 0.5*m.x192 - 0.5*m.x193 - 0.5*m.x232 - 0.5*m.x233 - 0.5*m.x264
                          - 0.5*m.x265 - 0.5*m.x288 - 0.5*m.x289 - 0.5*m.x312 - 0.5*m.x313 + m.x717 == 0)

m.c591 = Constraint(expr= - 0.5*m.x169 - 0.5*m.x170 - 0.5*m.x193 - 0.5*m.x194 - 0.5*m.x233 - 0.5*m.x234 - 0.5*m.x265
                          - 0.5*m.x266 - 0.5*m.x289 - 0.5*m.x290 - 0.5*m.x313 - 0.5*m.x314 + m.x718 == 0)

m.c592 = Constraint(expr= - 0.5*m.x170 - 0.5*m.x171 - 0.5*m.x194 - 0.5*m.x195 - 0.5*m.x234 - 0.5*m.x235 - 0.5*m.x266
                          - 0.5*m.x267 - 0.5*m.x290 - 0.5*m.x291 - 0.5*m.x314 - 0.5*m.x315 + m.x719 == 0)

m.c593 = Constraint(expr= - 0.5*m.x171 - 0.5*m.x172 - 0.5*m.x195 - 0.5*m.x196 - 0.5*m.x235 - 0.5*m.x236 - 0.5*m.x267
                          - 0.5*m.x268 - 0.5*m.x291 - 0.5*m.x292 - 0.5*m.x315 - 0.5*m.x316 + m.x720 == 0)

m.c594 = Constraint(expr= - 0.5*m.x172 - 0.5*m.x173 - 0.5*m.x196 - 0.5*m.x197 - 0.5*m.x236 - 0.5*m.x237 - 0.5*m.x268
                          - 0.5*m.x269 - 0.5*m.x292 - 0.5*m.x293 - 0.5*m.x316 - 0.5*m.x317 + m.x721 == 0)

m.c595 = Constraint(expr= - 0.5*m.x173 - 0.5*m.x174 - 0.5*m.x197 - 0.5*m.x198 - 0.5*m.x237 - 0.5*m.x238 - 0.5*m.x269
                          - 0.5*m.x270 - 0.5*m.x293 - 0.5*m.x294 - 0.5*m.x317 - 0.5*m.x318 + m.x722 == 0)

m.c596 = Constraint(expr= - 0.5*m.x199 - 0.5*m.x200 - 0.5*m.x239 - 0.5*m.x240 - 0.5*m.x295 - 0.5*m.x296 - 0.5*m.x319
                          - 0.5*m.x320 + m.x723 == 0)

m.c597 = Constraint(expr= - 0.5*m.x200 - 0.5*m.x201 - 0.5*m.x240 - 0.5*m.x241 - 0.5*m.x296 - 0.5*m.x297 - 0.5*m.x320
                          - 0.5*m.x321 + m.x724 == 0)

m.c598 = Constraint(expr= - 0.5*m.x201 - 0.5*m.x202 - 0.5*m.x241 - 0.5*m.x242 - 0.5*m.x297 - 0.5*m.x298 - 0.5*m.x321
                          - 0.5*m.x322 + m.x725 == 0)

m.c599 = Constraint(expr= - 0.5*m.x202 - 0.5*m.x203 - 0.5*m.x242 - 0.5*m.x243 - 0.5*m.x298 - 0.5*m.x299 - 0.5*m.x322
                          - 0.5*m.x323 + m.x726 == 0)

m.c600 = Constraint(expr= - 0.5*m.x203 - 0.5*m.x204 - 0.5*m.x243 - 0.5*m.x244 - 0.5*m.x299 - 0.5*m.x300 - 0.5*m.x323
                          - 0.5*m.x324 + m.x727 == 0)

m.c601 = Constraint(expr= - 0.5*m.x204 - 0.5*m.x205 - 0.5*m.x244 - 0.5*m.x245 - 0.5*m.x300 - 0.5*m.x301 - 0.5*m.x324
                          - 0.5*m.x325 + m.x728 == 0)

m.c602 = Constraint(expr= - 0.5*m.x205 - 0.5*m.x206 - 0.5*m.x245 - 0.5*m.x246 - 0.5*m.x301 - 0.5*m.x302 - 0.5*m.x325
                          - 0.5*m.x326 + m.x729 == 0)

m.c603 = Constraint(expr= - 500*m.b1 + m.x335 <= 0)

m.c604 = Constraint(expr= - 500*m.b2 + m.x336 <= 0)

m.c605 = Constraint(expr= - 500*m.b3 + m.x337 <= 0)

m.c606 = Constraint(expr= - 500*m.b4 + m.x338 <= 0)

m.c607 = Constraint(expr= - 500*m.b5 + m.x339 <= 0)

m.c608 = Constraint(expr= - 500*m.b6 + m.x340 <= 0)

m.c609 = Constraint(expr= - 500*m.b7 + m.x341 <= 0)

m.c610 = Constraint(expr= - 500*m.b8 + m.x377 <= 0)

m.c611 = Constraint(expr= - 500*m.b9 + m.x378 <= 0)

m.c612 = Constraint(expr= - 500*m.b10 + m.x379 <= 0)

m.c613 = Constraint(expr= - 500*m.b11 + m.x380 <= 0)

m.c614 = Constraint(expr= - 500*m.b12 + m.x381 <= 0)

m.c615 = Constraint(expr= - 500*m.b13 + m.x382 <= 0)

m.c616 = Constraint(expr= - 500*m.b14 + m.x383 <= 0)

m.c617 = Constraint(expr= - 500*m.b15 + m.x419 <= 0)

m.c618 = Constraint(expr= - 500*m.b16 + m.x420 <= 0)

m.c619 = Constraint(expr= - 500*m.b17 + m.x421 <= 0)

m.c620 = Constraint(expr= - 500*m.b18 + m.x422 <= 0)

m.c621 = Constraint(expr= - 500*m.b19 + m.x423 <= 0)

m.c622 = Constraint(expr= - 500*m.b20 + m.x424 <= 0)

m.c623 = Constraint(expr= - 500*m.b21 + m.x425 <= 0)

m.c624 = Constraint(expr= - 1000*m.b22 + m.x342 + m.x475 <= 0)

m.c625 = Constraint(expr= - 1000*m.b23 + m.x343 + m.x476 <= 0)

m.c626 = Constraint(expr= - 1000*m.b24 + m.x344 + m.x477 <= 0)

m.c627 = Constraint(expr= - 1000*m.b25 + m.x345 + m.x478 <= 0)

m.c628 = Constraint(expr= - 1000*m.b26 + m.x346 + m.x479 <= 0)

m.c629 = Constraint(expr= - 1000*m.b27 + m.x347 + m.x480 <= 0)

m.c630 = Constraint(expr= - 1000*m.b28 + m.x348 + m.x481 <= 0)

m.c631 = Constraint(expr= - 1000*m.b29 + m.x349 + m.x482 <= 0)

m.c632 = Constraint(expr= - 1000*m.b30 + m.x350 + m.x483 <= 0)

m.c633 = Constraint(expr= - 1000*m.b31 + m.x351 + m.x484 <= 0)

m.c634 = Constraint(expr= - 1000*m.b32 + m.x352 + m.x485 <= 0)

m.c635 = Constraint(expr= - 1000*m.b33 + m.x353 + m.x486 <= 0)

m.c636 = Constraint(expr= - 1000*m.b34 + m.x354 + m.x487 <= 0)

m.c637 = Constraint(expr= - 1000*m.b35 + m.x355 + m.x488 <= 0)

m.c638 = Constraint(expr= - 1000*m.b36 + m.x426 + m.x510 <= 0)

m.c639 = Constraint(expr= - 1000*m.b37 + m.x427 + m.x511 <= 0)

m.c640 = Constraint(expr= - 1000*m.b38 + m.x428 + m.x512 <= 0)

m.c641 = Constraint(expr= - 1000*m.b39 + m.x429 + m.x513 <= 0)

m.c642 = Constraint(expr= - 1000*m.b40 + m.x430 + m.x514 <= 0)

m.c643 = Constraint(expr= - 1000*m.b41 + m.x431 + m.x515 <= 0)

m.c644 = Constraint(expr= - 1000*m.b42 + m.x432 + m.x516 <= 0)

m.c645 = Constraint(expr= - 1000*m.b43 + m.x433 + m.x517 <= 0)

m.c646 = Constraint(expr= - 1000*m.b44 + m.x434 + m.x518 <= 0)

m.c647 = Constraint(expr= - 1000*m.b45 + m.x435 + m.x519 <= 0)

m.c648 = Constraint(expr= - 1000*m.b46 + m.x436 + m.x520 <= 0)

m.c649 = Constraint(expr= - 1000*m.b47 + m.x437 + m.x521 <= 0)

m.c650 = Constraint(expr= - 1000*m.b48 + m.x438 + m.x522 <= 0)

m.c651 = Constraint(expr= - 1000*m.b49 + m.x439 + m.x523 <= 0)

m.c652 = Constraint(expr= - 1000*m.b50 + m.x440 + m.x524 <= 0)

m.c653 = Constraint(expr= - 1000*m.b51 + m.x441 + m.x525 <= 0)

m.c654 = Constraint(expr= - 1000*m.b52 + m.x442 + m.x526 <= 0)

m.c655 = Constraint(expr= - 1000*m.b53 + m.x443 + m.x527 <= 0)

m.c656 = Constraint(expr= - 1000*m.b54 + m.x444 + m.x528 <= 0)

m.c657 = Constraint(expr= - 1000*m.b55 + m.x445 + m.x529 <= 0)

m.c658 = Constraint(expr= - 1000*m.b56 + m.x446 + m.x530 <= 0)

m.c659 = Constraint(expr= - 1000*m.b57 + m.x384 + m.x559 <= 0)

m.c660 = Constraint(expr= - 1000*m.b58 + m.x385 + m.x560 <= 0)

m.c661 = Constraint(expr= - 1000*m.b59 + m.x386 + m.x561 <= 0)

m.c662 = Constraint(expr= - 1000*m.b60 + m.x387 + m.x562 <= 0)

m.c663 = Constraint(expr= - 1000*m.b61 + m.x388 + m.x563 <= 0)

m.c664 = Constraint(expr= - 1000*m.b62 + m.x389 + m.x564 <= 0)

m.c665 = Constraint(expr= - 1000*m.b63 + m.x390 + m.x565 <= 0)

m.c666 = Constraint(expr= - 1000*m.b64 + m.x391 + m.x566 <= 0)

m.c667 = Constraint(expr= - 1000*m.b65 + m.x392 + m.x567 <= 0)

m.c668 = Constraint(expr= - 1000*m.b66 + m.x393 + m.x568 <= 0)

m.c669 = Constraint(expr= - 1000*m.b67 + m.x394 + m.x569 <= 0)

m.c670 = Constraint(expr= - 1000*m.b68 + m.x395 + m.x570 <= 0)

m.c671 = Constraint(expr= - 1000*m.b69 + m.x396 + m.x571 <= 0)

m.c672 = Constraint(expr= - 1000*m.b70 + m.x397 + m.x572 <= 0)

m.c673 = Constraint(expr= - 1000*m.b71 + m.x356 + m.x447 + m.x489 + m.x531 + m.x594 <= 0)

m.c674 = Constraint(expr= - 1000*m.b72 + m.x357 + m.x448 + m.x490 + m.x532 + m.x595 <= 0)

m.c675 = Constraint(expr= - 1000*m.b73 + m.x358 + m.x449 + m.x491 + m.x533 + m.x596 <= 0)

m.c676 = Constraint(expr= - 1000*m.b74 + m.x359 + m.x450 + m.x492 + m.x534 + m.x597 <= 0)

m.c677 = Constraint(expr= - 1000*m.b75 + m.x360 + m.x451 + m.x493 + m.x535 + m.x598 <= 0)

m.c678 = Constraint(expr= - 1000*m.b76 + m.x361 + m.x452 + m.x494 + m.x536 + m.x599 <= 0)

m.c679 = Constraint(expr= - 1000*m.b77 + m.x362 + m.x453 + m.x495 + m.x537 + m.x600 <= 0)

m.c680 = Constraint(expr= - 1000*m.b78 + m.x363 + m.x398 + m.x454 + m.x496 + m.x538 + m.x573 <= 0)

m.c681 = Constraint(expr= - 1000*m.b79 + m.x364 + m.x399 + m.x455 + m.x497 + m.x539 + m.x574 <= 0)

m.c682 = Constraint(expr= - 1000*m.b80 + m.x365 + m.x400 + m.x456 + m.x498 + m.x540 + m.x575 <= 0)

m.c683 = Constraint(expr= - 1000*m.b81 + m.x366 + m.x401 + m.x457 + m.x499 + m.x541 + m.x576 <= 0)

m.c684 = Constraint(expr= - 1000*m.b82 + m.x367 + m.x402 + m.x458 + m.x500 + m.x542 + m.x577 <= 0)

m.c685 = Constraint(expr= - 1000*m.b83 + m.x368 + m.x403 + m.x459 + m.x501 + m.x543 + m.x578 <= 0)

m.c686 = Constraint(expr= - 1000*m.b84 + m.x369 + m.x404 + m.x460 + m.x502 + m.x544 + m.x579 <= 0)

m.c687 = Constraint(expr= - 1000*m.b85 + m.x370 + m.x405 + m.x461 + m.x503 + m.x545 + m.x580 <= 0)

m.c688 = Constraint(expr= - 1000*m.b86 + m.x371 + m.x406 + m.x462 + m.x504 + m.x546 + m.x581 <= 0)

m.c689 = Constraint(expr= - 1000*m.b87 + m.x372 + m.x407 + m.x463 + m.x505 + m.x547 + m.x582 <= 0)

m.c690 = Constraint(expr= - 1000*m.b88 + m.x373 + m.x408 + m.x464 + m.x506 + m.x548 + m.x583 <= 0)

m.c691 = Constraint(expr= - 1000*m.b89 + m.x374 + m.x409 + m.x465 + m.x507 + m.x549 + m.x584 <= 0)

m.c692 = Constraint(expr= - 1000*m.b90 + m.x375 + m.x410 + m.x466 + m.x508 + m.x550 + m.x585 <= 0)

m.c693 = Constraint(expr= - 1000*m.b91 + m.x376 + m.x411 + m.x467 + m.x509 + m.x551 + m.x586 <= 0)

m.c694 = Constraint(expr= - 1000*m.b92 + m.x412 + m.x468 + m.x552 + m.x587 <= 0)

m.c695 = Constraint(expr= - 1000*m.b93 + m.x413 + m.x469 + m.x553 + m.x588 <= 0)

m.c696 = Constraint(expr= - 1000*m.b94 + m.x414 + m.x470 + m.x554 + m.x589 <= 0)

m.c697 = Constraint(expr= - 1000*m.b95 + m.x415 + m.x471 + m.x555 + m.x590 <= 0)

m.c698 = Constraint(expr= - 1000*m.b96 + m.x416 + m.x472 + m.x556 + m.x591 <= 0)

m.c699 = Constraint(expr= - 1000*m.b97 + m.x417 + m.x473 + m.x557 + m.x592 <= 0)

m.c700 = Constraint(expr= - 1000*m.b98 + m.x418 + m.x474 + m.x558 + m.x593 <= 0)

m.c701 = Constraint(expr= - m.b1 + m.x335 >= 0)

m.c702 = Constraint(expr= - m.b2 + m.x336 >= 0)

m.c703 = Constraint(expr= - m.b3 + m.x337 >= 0)

m.c704 = Constraint(expr= - m.b4 + m.x338 >= 0)

m.c705 = Constraint(expr= - m.b5 + m.x339 >= 0)

m.c706 = Constraint(expr= - m.b6 + m.x340 >= 0)

m.c707 = Constraint(expr= - m.b7 + m.x341 >= 0)

m.c708 = Constraint(expr= - m.b8 + m.x377 >= 0)

m.c709 = Constraint(expr= - m.b9 + m.x378 >= 0)

m.c710 = Constraint(expr= - m.b10 + m.x379 >= 0)

m.c711 = Constraint(expr= - m.b11 + m.x380 >= 0)

m.c712 = Constraint(expr= - m.b12 + m.x381 >= 0)

m.c713 = Constraint(expr= - m.b13 + m.x382 >= 0)

m.c714 = Constraint(expr= - m.b14 + m.x383 >= 0)

m.c715 = Constraint(expr= - m.b15 + m.x419 >= 0)

m.c716 = Constraint(expr= - m.b16 + m.x420 >= 0)

m.c717 = Constraint(expr= - m.b17 + m.x421 >= 0)

m.c718 = Constraint(expr= - m.b18 + m.x422 >= 0)

m.c719 = Constraint(expr= - m.b19 + m.x423 >= 0)

m.c720 = Constraint(expr= - m.b20 + m.x424 >= 0)

m.c721 = Constraint(expr= - m.b21 + m.x425 >= 0)

m.c722 = Constraint(expr= - m.b22 + m.x342 + m.x475 >= 0)

m.c723 = Constraint(expr= - m.b23 + m.x343 + m.x476 >= 0)

m.c724 = Constraint(expr= - m.b24 + m.x344 + m.x477 >= 0)

m.c725 = Constraint(expr= - m.b25 + m.x345 + m.x478 >= 0)

m.c726 = Constraint(expr= - m.b26 + m.x346 + m.x479 >= 0)

m.c727 = Constraint(expr= - m.b27 + m.x347 + m.x480 >= 0)

m.c728 = Constraint(expr= - m.b28 + m.x348 + m.x481 >= 0)

m.c729 = Constraint(expr= - m.b29 + m.x349 + m.x482 >= 0)

m.c730 = Constraint(expr= - m.b30 + m.x350 + m.x483 >= 0)

m.c731 = Constraint(expr= - m.b31 + m.x351 + m.x484 >= 0)

m.c732 = Constraint(expr= - m.b32 + m.x352 + m.x485 >= 0)

m.c733 = Constraint(expr= - m.b33 + m.x353 + m.x486 >= 0)

m.c734 = Constraint(expr= - m.b34 + m.x354 + m.x487 >= 0)

m.c735 = Constraint(expr= - m.b35 + m.x355 + m.x488 >= 0)

m.c736 = Constraint(expr= - m.b36 + m.x426 + m.x510 >= 0)

m.c737 = Constraint(expr= - m.b37 + m.x427 + m.x511 >= 0)

m.c738 = Constraint(expr= - m.b38 + m.x428 + m.x512 >= 0)

m.c739 = Constraint(expr= - m.b39 + m.x429 + m.x513 >= 0)

m.c740 = Constraint(expr= - m.b40 + m.x430 + m.x514 >= 0)

m.c741 = Constraint(expr= - m.b41 + m.x431 + m.x515 >= 0)

m.c742 = Constraint(expr= - m.b42 + m.x432 + m.x516 >= 0)

m.c743 = Constraint(expr= - m.b43 + m.x433 + m.x517 >= 0)

m.c744 = Constraint(expr= - m.b44 + m.x434 + m.x518 >= 0)

m.c745 = Constraint(expr= - m.b45 + m.x435 + m.x519 >= 0)

m.c746 = Constraint(expr= - m.b46 + m.x436 + m.x520 >= 0)

m.c747 = Constraint(expr= - m.b47 + m.x437 + m.x521 >= 0)

m.c748 = Constraint(expr= - m.b48 + m.x438 + m.x522 >= 0)

m.c749 = Constraint(expr= - m.b49 + m.x439 + m.x523 >= 0)

m.c750 = Constraint(expr= - m.b50 + m.x440 + m.x524 >= 0)

m.c751 = Constraint(expr= - m.b51 + m.x441 + m.x525 >= 0)

m.c752 = Constraint(expr= - m.b52 + m.x442 + m.x526 >= 0)

m.c753 = Constraint(expr= - m.b53 + m.x443 + m.x527 >= 0)

m.c754 = Constraint(expr= - m.b54 + m.x444 + m.x528 >= 0)

m.c755 = Constraint(expr= - m.b55 + m.x445 + m.x529 >= 0)

m.c756 = Constraint(expr= - m.b56 + m.x446 + m.x530 >= 0)

m.c757 = Constraint(expr= - m.b57 + m.x384 + m.x559 >= 0)

m.c758 = Constraint(expr= - m.b58 + m.x385 + m.x560 >= 0)

m.c759 = Constraint(expr= - m.b59 + m.x386 + m.x561 >= 0)

m.c760 = Constraint(expr= - m.b60 + m.x387 + m.x562 >= 0)

m.c761 = Constraint(expr= - m.b61 + m.x388 + m.x563 >= 0)

m.c762 = Constraint(expr= - m.b62 + m.x389 + m.x564 >= 0)

m.c763 = Constraint(expr= - m.b63 + m.x390 + m.x565 >= 0)

m.c764 = Constraint(expr= - m.b64 + m.x391 + m.x566 >= 0)

m.c765 = Constraint(expr= - m.b65 + m.x392 + m.x567 >= 0)

m.c766 = Constraint(expr= - m.b66 + m.x393 + m.x568 >= 0)

m.c767 = Constraint(expr= - m.b67 + m.x394 + m.x569 >= 0)

m.c768 = Constraint(expr= - m.b68 + m.x395 + m.x570 >= 0)

m.c769 = Constraint(expr= - m.b69 + m.x396 + m.x571 >= 0)

m.c770 = Constraint(expr= - m.b70 + m.x397 + m.x572 >= 0)

m.c771 = Constraint(expr= - m.b71 + m.x356 + m.x447 + m.x489 + m.x531 + m.x594 >= 0)

m.c772 = Constraint(expr= - m.b72 + m.x357 + m.x448 + m.x490 + m.x532 + m.x595 >= 0)

m.c773 = Constraint(expr= - m.b73 + m.x358 + m.x449 + m.x491 + m.x533 + m.x596 >= 0)

m.c774 = Constraint(expr= - m.b74 + m.x359 + m.x450 + m.x492 + m.x534 + m.x597 >= 0)

m.c775 = Constraint(expr= - m.b75 + m.x360 + m.x451 + m.x493 + m.x535 + m.x598 >= 0)

m.c776 = Constraint(expr= - m.b76 + m.x361 + m.x452 + m.x494 + m.x536 + m.x599 >= 0)

m.c777 = Constraint(expr= - m.b77 + m.x362 + m.x453 + m.x495 + m.x537 + m.x600 >= 0)

m.c778 = Constraint(expr= - m.b78 + m.x363 + m.x398 + m.x454 + m.x496 + m.x538 + m.x573 >= 0)

m.c779 = Constraint(expr= - m.b79 + m.x364 + m.x399 + m.x455 + m.x497 + m.x539 + m.x574 >= 0)

m.c780 = Constraint(expr= - m.b80 + m.x365 + m.x400 + m.x456 + m.x498 + m.x540 + m.x575 >= 0)

m.c781 = Constraint(expr= - m.b81 + m.x366 + m.x401 + m.x457 + m.x499 + m.x541 + m.x576 >= 0)

m.c782 = Constraint(expr= - m.b82 + m.x367 + m.x402 + m.x458 + m.x500 + m.x542 + m.x577 >= 0)

m.c783 = Constraint(expr= - m.b83 + m.x368 + m.x403 + m.x459 + m.x501 + m.x543 + m.x578 >= 0)

m.c784 = Constraint(expr= - m.b84 + m.x369 + m.x404 + m.x460 + m.x502 + m.x544 + m.x579 >= 0)

m.c785 = Constraint(expr= - m.b85 + m.x370 + m.x405 + m.x461 + m.x503 + m.x545 + m.x580 >= 0)

m.c786 = Constraint(expr= - m.b86 + m.x371 + m.x406 + m.x462 + m.x504 + m.x546 + m.x581 >= 0)

m.c787 = Constraint(expr= - m.b87 + m.x372 + m.x407 + m.x463 + m.x505 + m.x547 + m.x582 >= 0)

m.c788 = Constraint(expr= - m.b88 + m.x373 + m.x408 + m.x464 + m.x506 + m.x548 + m.x583 >= 0)

m.c789 = Constraint(expr= - m.b89 + m.x374 + m.x409 + m.x465 + m.x507 + m.x549 + m.x584 >= 0)

m.c790 = Constraint(expr= - m.b90 + m.x375 + m.x410 + m.x466 + m.x508 + m.x550 + m.x585 >= 0)

m.c791 = Constraint(expr= - m.b91 + m.x376 + m.x411 + m.x467 + m.x509 + m.x551 + m.x586 >= 0)

m.c792 = Constraint(expr= - m.b92 + m.x412 + m.x468 + m.x552 + m.x587 >= 0)

m.c793 = Constraint(expr= - m.b93 + m.x413 + m.x469 + m.x553 + m.x588 >= 0)

m.c794 = Constraint(expr= - m.b94 + m.x414 + m.x470 + m.x554 + m.x589 >= 0)

m.c795 = Constraint(expr= - m.b95 + m.x415 + m.x471 + m.x555 + m.x590 >= 0)

m.c796 = Constraint(expr= - m.b96 + m.x416 + m.x472 + m.x556 + m.x591 >= 0)

m.c797 = Constraint(expr= - m.b97 + m.x417 + m.x473 + m.x557 + m.x592 >= 0)

m.c798 = Constraint(expr= - m.b98 + m.x418 + m.x474 + m.x558 + m.x593 >= 0)

m.c799 = Constraint(expr= - 0.002*m.x335 - m.x667 + m.x668 >= 0)

m.c800 = Constraint(expr= - 0.002*m.x336 - m.x668 + m.x669 >= 0)

m.c801 = Constraint(expr= - 0.002*m.x337 - m.x669 + m.x670 >= 0)

m.c802 = Constraint(expr= - 0.002*m.x338 - m.x670 + m.x671 >= 0)

m.c803 = Constraint(expr= - 0.002*m.x339 - m.x671 + m.x672 >= 0)

m.c804 = Constraint(expr= - 0.002*m.x340 - m.x672 + m.x673 >= 0)

m.c805 = Constraint(expr= - 0.002*m.x341 - m.x673 + m.x674 >= 0)

m.c806 = Constraint(expr= - 0.002*m.x377 - m.x667 + m.x668 >= 0)

m.c807 = Constraint(expr= - 0.002*m.x378 - m.x668 + m.x669 >= 0)

m.c808 = Constraint(expr= - 0.002*m.x379 - m.x669 + m.x670 >= 0)

m.c809 = Constraint(expr= - 0.002*m.x380 - m.x670 + m.x671 >= 0)

m.c810 = Constraint(expr= - 0.002*m.x381 - m.x671 + m.x672 >= 0)

m.c811 = Constraint(expr= - 0.002*m.x382 - m.x672 + m.x673 >= 0)

m.c812 = Constraint(expr= - 0.002*m.x383 - m.x673 + m.x674 >= 0)

m.c813 = Constraint(expr= - 0.002*m.x419 - m.x667 + m.x668 >= 0)

m.c814 = Constraint(expr= - 0.002*m.x420 - m.x668 + m.x669 >= 0)

m.c815 = Constraint(expr= - 0.002*m.x421 - m.x669 + m.x670 >= 0)

m.c816 = Constraint(expr= - 0.002*m.x422 - m.x670 + m.x671 >= 0)

m.c817 = Constraint(expr= - 0.002*m.x423 - m.x671 + m.x672 >= 0)

m.c818 = Constraint(expr= - 0.002*m.x424 - m.x672 + m.x673 >= 0)

m.c819 = Constraint(expr= - 0.002*m.x425 - m.x673 + m.x674 >= 0)

m.c820 = Constraint(expr= - 0.002*m.x342 - 0.002*m.x475 - m.x667 + m.x668 >= 0)

m.c821 = Constraint(expr= - 0.002*m.x343 - 0.002*m.x476 - m.x668 + m.x669 >= 0)

m.c822 = Constraint(expr= - 0.002*m.x344 - 0.002*m.x477 - m.x669 + m.x670 >= 0)

m.c823 = Constraint(expr= - 0.002*m.x345 - 0.002*m.x478 - m.x670 + m.x671 >= 0)

m.c824 = Constraint(expr= - 0.002*m.x346 - 0.002*m.x479 - m.x671 + m.x672 >= 0)

m.c825 = Constraint(expr= - 0.002*m.x347 - 0.002*m.x480 - m.x672 + m.x673 >= 0)

m.c826 = Constraint(expr= - 0.002*m.x348 - 0.002*m.x481 - m.x673 + m.x674 >= 0)

m.c827 = Constraint(expr= - 0.002*m.x349 - 0.002*m.x482 - m.x667 + m.x668 >= 0)

m.c828 = Constraint(expr= - 0.002*m.x350 - 0.002*m.x483 - m.x668 + m.x669 >= 0)

m.c829 = Constraint(expr= - 0.002*m.x351 - 0.002*m.x484 - m.x669 + m.x670 >= 0)

m.c830 = Constraint(expr= - 0.002*m.x352 - 0.002*m.x485 - m.x670 + m.x671 >= 0)

m.c831 = Constraint(expr= - 0.002*m.x353 - 0.002*m.x486 - m.x671 + m.x672 >= 0)

m.c832 = Constraint(expr= - 0.002*m.x354 - 0.002*m.x487 - m.x672 + m.x673 >= 0)

m.c833 = Constraint(expr= - 0.002*m.x355 - 0.002*m.x488 - m.x673 + m.x674 >= 0)

m.c834 = Constraint(expr= - 0.002*m.x426 - 0.002*m.x510 - m.x667 + m.x668 >= 0)

m.c835 = Constraint(expr= - 0.002*m.x427 - 0.002*m.x511 - m.x668 + m.x669 >= 0)

m.c836 = Constraint(expr= - 0.002*m.x428 - 0.002*m.x512 - m.x669 + m.x670 >= 0)

m.c837 = Constraint(expr= - 0.002*m.x429 - 0.002*m.x513 - m.x670 + m.x671 >= 0)

m.c838 = Constraint(expr= - 0.002*m.x430 - 0.002*m.x514 - m.x671 + m.x672 >= 0)

m.c839 = Constraint(expr= - 0.002*m.x431 - 0.002*m.x515 - m.x672 + m.x673 >= 0)

m.c840 = Constraint(expr= - 0.002*m.x432 - 0.002*m.x516 - m.x673 + m.x674 >= 0)

m.c841 = Constraint(expr= - 0.002*m.x433 - 0.002*m.x517 - m.x667 + m.x668 >= 0)

m.c842 = Constraint(expr= - 0.002*m.x434 - 0.002*m.x518 - m.x668 + m.x669 >= 0)

m.c843 = Constraint(expr= - 0.002*m.x435 - 0.002*m.x519 - m.x669 + m.x670 >= 0)

m.c844 = Constraint(expr= - 0.002*m.x436 - 0.002*m.x520 - m.x670 + m.x671 >= 0)

m.c845 = Constraint(expr= - 0.002*m.x437 - 0.002*m.x521 - m.x671 + m.x672 >= 0)

m.c846 = Constraint(expr= - 0.002*m.x438 - 0.002*m.x522 - m.x672 + m.x673 >= 0)

m.c847 = Constraint(expr= - 0.002*m.x439 - 0.002*m.x523 - m.x673 + m.x674 >= 0)

m.c848 = Constraint(expr= - 0.002*m.x440 - 0.002*m.x524 - m.x667 + m.x668 >= 0)

m.c849 = Constraint(expr= - 0.002*m.x441 - 0.002*m.x525 - m.x668 + m.x669 >= 0)

m.c850 = Constraint(expr= - 0.002*m.x442 - 0.002*m.x526 - m.x669 + m.x670 >= 0)

m.c851 = Constraint(expr= - 0.002*m.x443 - 0.002*m.x527 - m.x670 + m.x671 >= 0)

m.c852 = Constraint(expr= - 0.002*m.x444 - 0.002*m.x528 - m.x671 + m.x672 >= 0)

m.c853 = Constraint(expr= - 0.002*m.x445 - 0.002*m.x529 - m.x672 + m.x673 >= 0)

m.c854 = Constraint(expr= - 0.002*m.x446 - 0.002*m.x530 - m.x673 + m.x674 >= 0)

m.c855 = Constraint(expr= - 0.002*m.x384 - 0.002*m.x559 - m.x667 + m.x668 >= 0)

m.c856 = Constraint(expr= - 0.002*m.x385 - 0.002*m.x560 - m.x668 + m.x669 >= 0)

m.c857 = Constraint(expr= - 0.002*m.x386 - 0.002*m.x561 - m.x669 + m.x670 >= 0)

m.c858 = Constraint(expr= - 0.002*m.x387 - 0.002*m.x562 - m.x670 + m.x671 >= 0)

m.c859 = Constraint(expr= - 0.002*m.x388 - 0.002*m.x563 - m.x671 + m.x672 >= 0)

m.c860 = Constraint(expr= - 0.002*m.x389 - 0.002*m.x564 - m.x672 + m.x673 >= 0)

m.c861 = Constraint(expr= - 0.002*m.x390 - 0.002*m.x565 - m.x673 + m.x674 >= 0)

m.c862 = Constraint(expr= - 0.002*m.x391 - 0.002*m.x566 - m.x667 + m.x668 >= 0)

m.c863 = Constraint(expr= - 0.002*m.x392 - 0.002*m.x567 - m.x668 + m.x669 >= 0)

m.c864 = Constraint(expr= - 0.002*m.x393 - 0.002*m.x568 - m.x669 + m.x670 >= 0)

m.c865 = Constraint(expr= - 0.002*m.x394 - 0.002*m.x569 - m.x670 + m.x671 >= 0)

m.c866 = Constraint(expr= - 0.002*m.x395 - 0.002*m.x570 - m.x671 + m.x672 >= 0)

m.c867 = Constraint(expr= - 0.002*m.x396 - 0.002*m.x571 - m.x672 + m.x673 >= 0)

m.c868 = Constraint(expr= - 0.002*m.x397 - 0.002*m.x572 - m.x673 + m.x674 >= 0)

m.c869 = Constraint(expr= - 0.002*m.x363 - 0.002*m.x370 - 0.002*m.x398 - 0.002*m.x405 - 0.002*m.x454 - 0.002*m.x461
                          - 0.002*m.x496 - 0.002*m.x503 - 0.002*m.x538 - 0.002*m.x545 - 0.002*m.x573 - 0.002*m.x580
                          - m.x667 + m.x668 >= 0)

m.c870 = Constraint(expr= - 0.002*m.x364 - 0.002*m.x371 - 0.002*m.x399 - 0.002*m.x406 - 0.002*m.x455 - 0.002*m.x462
                          - 0.002*m.x497 - 0.002*m.x504 - 0.002*m.x539 - 0.002*m.x546 - 0.002*m.x574 - 0.002*m.x581
                          - m.x668 + m.x669 >= 0)

m.c871 = Constraint(expr= - 0.002*m.x365 - 0.002*m.x372 - 0.002*m.x400 - 0.002*m.x407 - 0.002*m.x456 - 0.002*m.x463
                          - 0.002*m.x498 - 0.002*m.x505 - 0.002*m.x540 - 0.002*m.x547 - 0.002*m.x575 - 0.002*m.x582
                          - m.x669 + m.x670 >= 0)

m.c872 = Constraint(expr= - 0.002*m.x366 - 0.002*m.x373 - 0.002*m.x401 - 0.002*m.x408 - 0.002*m.x457 - 0.002*m.x464
                          - 0.002*m.x499 - 0.002*m.x506 - 0.002*m.x541 - 0.002*m.x548 - 0.002*m.x576 - 0.002*m.x583
                          - m.x670 + m.x671 >= 0)

m.c873 = Constraint(expr= - 0.002*m.x367 - 0.002*m.x374 - 0.002*m.x402 - 0.002*m.x409 - 0.002*m.x458 - 0.002*m.x465
                          - 0.002*m.x500 - 0.002*m.x507 - 0.002*m.x542 - 0.002*m.x549 - 0.002*m.x577 - 0.002*m.x584
                          - m.x671 + m.x672 >= 0)

m.c874 = Constraint(expr= - 0.002*m.x368 - 0.002*m.x375 - 0.002*m.x403 - 0.002*m.x410 - 0.002*m.x459 - 0.002*m.x466
                          - 0.002*m.x501 - 0.002*m.x508 - 0.002*m.x543 - 0.002*m.x550 - 0.002*m.x578 - 0.002*m.x585
                          - m.x672 + m.x673 >= 0)

m.c875 = Constraint(expr= - 0.002*m.x369 - 0.002*m.x376 - 0.002*m.x404 - 0.002*m.x411 - 0.002*m.x460 - 0.002*m.x467
                          - 0.002*m.x502 - 0.002*m.x509 - 0.002*m.x544 - 0.002*m.x551 - 0.002*m.x579 - 0.002*m.x586
                          - m.x673 + m.x674 >= 0)

m.c876 = Constraint(expr= - 0.002*m.x356 - 0.002*m.x363 - 0.002*m.x398 - 0.002*m.x447 - 0.002*m.x454 - 0.002*m.x489
                          - 0.002*m.x496 - 0.002*m.x531 - 0.002*m.x538 - 0.002*m.x573 - 0.002*m.x594 - m.x667 + m.x668
                          >= 0)

m.c877 = Constraint(expr= - 0.002*m.x357 - 0.002*m.x364 - 0.002*m.x399 - 0.002*m.x448 - 0.002*m.x455 - 0.002*m.x490
                          - 0.002*m.x497 - 0.002*m.x532 - 0.002*m.x539 - 0.002*m.x574 - 0.002*m.x595 - m.x668 + m.x669
                          >= 0)

m.c878 = Constraint(expr= - 0.002*m.x358 - 0.002*m.x365 - 0.002*m.x400 - 0.002*m.x449 - 0.002*m.x456 - 0.002*m.x491
                          - 0.002*m.x498 - 0.002*m.x533 - 0.002*m.x540 - 0.002*m.x575 - 0.002*m.x596 - m.x669 + m.x670
                          >= 0)

m.c879 = Constraint(expr= - 0.002*m.x359 - 0.002*m.x366 - 0.002*m.x401 - 0.002*m.x450 - 0.002*m.x457 - 0.002*m.x492
                          - 0.002*m.x499 - 0.002*m.x534 - 0.002*m.x541 - 0.002*m.x576 - 0.002*m.x597 - m.x670 + m.x671
                          >= 0)

m.c880 = Constraint(expr= - 0.002*m.x360 - 0.002*m.x367 - 0.002*m.x402 - 0.002*m.x451 - 0.002*m.x458 - 0.002*m.x493
                          - 0.002*m.x500 - 0.002*m.x535 - 0.002*m.x542 - 0.002*m.x577 - 0.002*m.x598 - m.x671 + m.x672
                          >= 0)

m.c881 = Constraint(expr= - 0.002*m.x361 - 0.002*m.x368 - 0.002*m.x403 - 0.002*m.x452 - 0.002*m.x459 - 0.002*m.x494
                          - 0.002*m.x501 - 0.002*m.x536 - 0.002*m.x543 - 0.002*m.x578 - 0.002*m.x599 - m.x672 + m.x673
                          >= 0)

m.c882 = Constraint(expr= - 0.002*m.x362 - 0.002*m.x369 - 0.002*m.x404 - 0.002*m.x453 - 0.002*m.x460 - 0.002*m.x495
                          - 0.002*m.x502 - 0.002*m.x537 - 0.002*m.x544 - 0.002*m.x579 - 0.002*m.x600 - m.x673 + m.x674
                          >= 0)

m.c883 = Constraint(expr= - 0.002*m.x370 - 0.002*m.x405 - 0.002*m.x412 - 0.002*m.x461 - 0.002*m.x468 - 0.002*m.x503
                          - 0.002*m.x545 - 0.002*m.x552 - 0.002*m.x580 - 0.002*m.x587 - m.x667 + m.x668 >= 0)

m.c884 = Constraint(expr= - 0.002*m.x371 - 0.002*m.x406 - 0.002*m.x413 - 0.002*m.x462 - 0.002*m.x469 - 0.002*m.x504
                          - 0.002*m.x546 - 0.002*m.x553 - 0.002*m.x581 - 0.002*m.x588 - m.x668 + m.x669 >= 0)

m.c885 = Constraint(expr= - 0.002*m.x372 - 0.002*m.x407 - 0.002*m.x414 - 0.002*m.x463 - 0.002*m.x470 - 0.002*m.x505
                          - 0.002*m.x547 - 0.002*m.x554 - 0.002*m.x582 - 0.002*m.x589 - m.x669 + m.x670 >= 0)

m.c886 = Constraint(expr= - 0.002*m.x373 - 0.002*m.x408 - 0.002*m.x415 - 0.002*m.x464 - 0.002*m.x471 - 0.002*m.x506
                          - 0.002*m.x548 - 0.002*m.x555 - 0.002*m.x583 - 0.002*m.x590 - m.x670 + m.x671 >= 0)

m.c887 = Constraint(expr= - 0.002*m.x374 - 0.002*m.x409 - 0.002*m.x416 - 0.002*m.x465 - 0.002*m.x472 - 0.002*m.x507
                          - 0.002*m.x549 - 0.002*m.x556 - 0.002*m.x584 - 0.002*m.x591 - m.x671 + m.x672 >= 0)

m.c888 = Constraint(expr= - 0.002*m.x375 - 0.002*m.x410 - 0.002*m.x417 - 0.002*m.x466 - 0.002*m.x473 - 0.002*m.x508
                          - 0.002*m.x550 - 0.002*m.x557 - 0.002*m.x585 - 0.002*m.x592 - m.x672 + m.x673 >= 0)

m.c889 = Constraint(expr= - 0.002*m.x376 - 0.002*m.x411 - 0.002*m.x418 - 0.002*m.x467 - 0.002*m.x474 - 0.002*m.x509
                          - 0.002*m.x551 - 0.002*m.x558 - 0.002*m.x586 - 0.002*m.x593 - m.x673 + m.x674 >= 0)

m.c890 = Constraint(expr= - 0.02*m.x356 - 0.02*m.x363 - 0.02*m.x398 - 0.02*m.x447 - 0.02*m.x454 - 0.02*m.x489
                          - 0.02*m.x496 - 0.02*m.x531 - 0.02*m.x538 - 0.02*m.x573 - 0.02*m.x594 - m.x667 + m.x668 <= 0)

m.c891 = Constraint(expr= - 0.02*m.x357 - 0.02*m.x364 - 0.02*m.x399 - 0.02*m.x448 - 0.02*m.x455 - 0.02*m.x490
                          - 0.02*m.x497 - 0.02*m.x532 - 0.02*m.x539 - 0.02*m.x574 - 0.02*m.x595 - m.x668 + m.x669 <= 0)

m.c892 = Constraint(expr= - 0.02*m.x358 - 0.02*m.x365 - 0.02*m.x400 - 0.02*m.x449 - 0.02*m.x456 - 0.02*m.x491
                          - 0.02*m.x498 - 0.02*m.x533 - 0.02*m.x540 - 0.02*m.x575 - 0.02*m.x596 - m.x669 + m.x670 <= 0)

m.c893 = Constraint(expr= - 0.02*m.x359 - 0.02*m.x366 - 0.02*m.x401 - 0.02*m.x450 - 0.02*m.x457 - 0.02*m.x492
                          - 0.02*m.x499 - 0.02*m.x534 - 0.02*m.x541 - 0.02*m.x576 - 0.02*m.x597 - m.x670 + m.x671 <= 0)

m.c894 = Constraint(expr= - 0.02*m.x360 - 0.02*m.x367 - 0.02*m.x402 - 0.02*m.x451 - 0.02*m.x458 - 0.02*m.x493
                          - 0.02*m.x500 - 0.02*m.x535 - 0.02*m.x542 - 0.02*m.x577 - 0.02*m.x598 - m.x671 + m.x672 <= 0)

m.c895 = Constraint(expr= - 0.02*m.x361 - 0.02*m.x368 - 0.02*m.x403 - 0.02*m.x452 - 0.02*m.x459 - 0.02*m.x494
                          - 0.02*m.x501 - 0.02*m.x536 - 0.02*m.x543 - 0.02*m.x578 - 0.02*m.x599 - m.x672 + m.x673 <= 0)

m.c896 = Constraint(expr= - 0.02*m.x362 - 0.02*m.x369 - 0.02*m.x404 - 0.02*m.x453 - 0.02*m.x460 - 0.02*m.x495
                          - 0.02*m.x502 - 0.02*m.x537 - 0.02*m.x544 - 0.02*m.x579 - 0.02*m.x600 - m.x673 + m.x674 <= 0)

m.c897 = Constraint(expr= - 0.02*m.x370 - 0.02*m.x405 - 0.02*m.x412 - 0.02*m.x461 - 0.02*m.x468 - 0.02*m.x503
                          - 0.02*m.x545 - 0.02*m.x552 - 0.02*m.x580 - 0.02*m.x587 - m.x667 + m.x668 <= 0)

m.c898 = Constraint(expr= - 0.02*m.x371 - 0.02*m.x406 - 0.02*m.x413 - 0.02*m.x462 - 0.02*m.x469 - 0.02*m.x504
                          - 0.02*m.x546 - 0.02*m.x553 - 0.02*m.x581 - 0.02*m.x588 - m.x668 + m.x669 <= 0)

m.c899 = Constraint(expr= - 0.02*m.x372 - 0.02*m.x407 - 0.02*m.x414 - 0.02*m.x463 - 0.02*m.x470 - 0.02*m.x505
                          - 0.02*m.x547 - 0.02*m.x554 - 0.02*m.x582 - 0.02*m.x589 - m.x669 + m.x670 <= 0)

m.c900 = Constraint(expr= - 0.02*m.x373 - 0.02*m.x408 - 0.02*m.x415 - 0.02*m.x464 - 0.02*m.x471 - 0.02*m.x506
                          - 0.02*m.x548 - 0.02*m.x555 - 0.02*m.x583 - 0.02*m.x590 - m.x670 + m.x671 <= 0)

m.c901 = Constraint(expr= - 0.02*m.x374 - 0.02*m.x409 - 0.02*m.x416 - 0.02*m.x465 - 0.02*m.x472 - 0.02*m.x507
                          - 0.02*m.x549 - 0.02*m.x556 - 0.02*m.x584 - 0.02*m.x591 - m.x671 + m.x672 <= 0)

m.c902 = Constraint(expr= - 0.02*m.x375 - 0.02*m.x410 - 0.02*m.x417 - 0.02*m.x466 - 0.02*m.x473 - 0.02*m.x508
                          - 0.02*m.x550 - 0.02*m.x557 - 0.02*m.x585 - 0.02*m.x592 - m.x672 + m.x673 <= 0)

m.c903 = Constraint(expr= - 0.02*m.x376 - 0.02*m.x411 - 0.02*m.x418 - 0.02*m.x467 - 0.02*m.x474 - 0.02*m.x509
                          - 0.02*m.x551 - 0.02*m.x558 - 0.02*m.x586 - 0.02*m.x593 - m.x673 + m.x674 <= 0)

m.c904 = Constraint(expr=   m.x667 >= 0)

m.c905 = Constraint(expr= - 4*m.b101 + m.x668 >= 0)

m.c906 = Constraint(expr= - 4*m.b103 - 8*m.b104 + m.x669 >= 0)

m.c907 = Constraint(expr= - 4*m.b106 - 8*m.b107 + m.x670 >= 0)

m.c908 = Constraint(expr= - 4*m.b109 - 8*m.b110 + m.x671 >= 0)

m.c909 = Constraint(expr= - 4*m.b111 - 8*m.b112 + m.x672 >= 0)

m.c910 = Constraint(expr= - 8*m.b113 + m.x673 >= 0)

m.c911 = Constraint(expr= - m.b114 + m.x668 >= 0)

m.c912 = Constraint(expr= - m.b115 - 5*m.b116 + m.x669 >= 0)

m.c913 = Constraint(expr= - m.b117 - 5*m.b118 - 9*m.b119 + m.x670 >= 0)

m.c914 = Constraint(expr= - m.b120 - 5*m.b121 - 9*m.b122 + m.x671 >= 0)

m.c915 = Constraint(expr= - m.b123 - 5*m.b124 - 9*m.b125 + m.x672 >= 0)

m.c916 = Constraint(expr= - 5*m.b126 - 9*m.b127 + m.x673 >= 0)

m.c917 = Constraint(expr= - 9*m.b128 + m.x674 >= 0)

m.c918 = Constraint(expr=   m.b99 + 2*m.b100 + 3*m.b102 + 4*m.b105 + 5*m.b108 - 2*m.b114 - 3*m.b115 - 4*m.b117
                          - 5*m.b120 - 6*m.b123 <= -1)

m.c919 = Constraint(expr=   2*m.b101 + 3*m.b103 + 4*m.b106 + 5*m.b109 + 6*m.b111 - 3*m.b116 - 4*m.b118 - 5*m.b121
                          - 6*m.b124 - 7*m.b126 <= -1)

m.c920 = Constraint(expr=   3*m.b104 + 4*m.b107 + 5*m.b110 + 6*m.b112 + 7*m.b113 - 4*m.b119 - 5*m.b122 - 6*m.b125
                          - 7*m.b127 - 8*m.b128 <= -1)

m.c921 = Constraint(expr= - 2*m.b101 - 3*m.b103 - 4*m.b106 - 5*m.b109 - 6*m.b111 + 2*m.b114 + 3*m.b115 + 4*m.b117
                          + 5*m.b120 + 6*m.b123 <= 0)

m.c922 = Constraint(expr= - 3*m.b104 - 4*m.b107 - 5*m.b110 - 6*m.b112 - 7*m.b113 + 3*m.b116 + 4*m.b118 + 5*m.b121
                          + 6*m.b124 + 7*m.b126 <= 0)

m.c923 = Constraint(expr= - 12*m.b99 - m.x667 + m.x682 >= -12)

m.c924 = Constraint(expr= - 12*m.b100 - m.x668 + m.x682 >= -12)

m.c925 = Constraint(expr= - 12*m.b102 - m.x669 + m.x682 >= -12)

m.c926 = Constraint(expr= - 12*m.b105 - m.x670 + m.x682 >= -12)

m.c927 = Constraint(expr= - 12*m.b108 - m.x671 + m.x682 >= -12)

m.c928 = Constraint(expr= - 8*m.b101 - m.x668 + m.x683 >= -12)

m.c929 = Constraint(expr= - 8*m.b103 - m.x669 + m.x683 >= -12)

m.c930 = Constraint(expr= - 8*m.b106 - m.x670 + m.x683 >= -12)

m.c931 = Constraint(expr= - 8*m.b109 - m.x671 + m.x683 >= -12)

m.c932 = Constraint(expr= - 8*m.b111 - m.x672 + m.x683 >= -12)

m.c933 = Constraint(expr= - 4*m.b104 - m.x669 + m.x684 >= -12)

m.c934 = Constraint(expr= - 4*m.b107 - m.x670 + m.x684 >= -12)

m.c935 = Constraint(expr= - 4*m.b110 - m.x671 + m.x684 >= -12)

m.c936 = Constraint(expr= - 4*m.b112 - m.x672 + m.x684 >= -12)

m.c937 = Constraint(expr= - 4*m.b113 - m.x673 + m.x684 >= -12)

m.c938 = Constraint(expr= - 11*m.b99 - 11*m.b114 + m.x667 - m.x668 + m.x685 >= -22)

m.c939 = Constraint(expr= - 11*m.b99 - 11*m.b115 + m.x667 - m.x669 + m.x685 >= -22)

m.c940 = Constraint(expr= - 11*m.b99 - 11*m.b117 + m.x667 - m.x670 + m.x685 >= -22)

m.c941 = Constraint(expr= - 11*m.b99 - 11*m.b120 + m.x667 - m.x671 + m.x685 >= -22)

m.c942 = Constraint(expr= - 11*m.b99 - 11*m.b123 + m.x667 - m.x672 + m.x685 >= -22)

m.c943 = Constraint(expr= - 11*m.b100 - 11*m.b115 + m.x668 - m.x669 + m.x685 >= -22)

m.c944 = Constraint(expr= - 11*m.b100 - 11*m.b117 + m.x668 - m.x670 + m.x685 >= -22)

m.c945 = Constraint(expr= - 11*m.b100 - 11*m.b120 + m.x668 - m.x671 + m.x685 >= -22)

m.c946 = Constraint(expr= - 11*m.b100 - 11*m.b123 + m.x668 - m.x672 + m.x685 >= -22)

m.c947 = Constraint(expr= - 11*m.b102 - 11*m.b117 + m.x669 - m.x670 + m.x685 >= -22)

m.c948 = Constraint(expr= - 11*m.b102 - 11*m.b120 + m.x669 - m.x671 + m.x685 >= -22)

m.c949 = Constraint(expr= - 11*m.b102 - 11*m.b123 + m.x669 - m.x672 + m.x685 >= -22)

m.c950 = Constraint(expr= - 11*m.b105 - 11*m.b120 + m.x670 - m.x671 + m.x685 >= -22)

m.c951 = Constraint(expr= - 11*m.b105 - 11*m.b123 + m.x670 - m.x672 + m.x685 >= -22)

m.c952 = Constraint(expr= - 11*m.b108 - 11*m.b123 + m.x671 - m.x672 + m.x685 >= -22)

m.c953 = Constraint(expr= - 11*m.b101 - 11*m.b116 + m.x668 - m.x669 + m.x686 >= -22)

m.c954 = Constraint(expr= - 11*m.b101 - 11*m.b118 + m.x668 - m.x670 + m.x686 >= -22)

m.c955 = Constraint(expr= - 11*m.b101 - 11*m.b121 + m.x668 - m.x671 + m.x686 >= -22)

m.c956 = Constraint(expr= - 11*m.b101 - 11*m.b124 + m.x668 - m.x672 + m.x686 >= -22)

m.c957 = Constraint(expr= - 11*m.b101 - 11*m.b126 + m.x668 - m.x673 + m.x686 >= -22)

m.c958 = Constraint(expr= - 11*m.b103 - 11*m.b118 + m.x669 - m.x670 + m.x686 >= -22)

m.c959 = Constraint(expr= - 11*m.b103 - 11*m.b121 + m.x669 - m.x671 + m.x686 >= -22)

m.c960 = Constraint(expr= - 11*m.b103 - 11*m.b124 + m.x669 - m.x672 + m.x686 >= -22)

m.c961 = Constraint(expr= - 11*m.b103 - 11*m.b126 + m.x669 - m.x673 + m.x686 >= -22)

m.c962 = Constraint(expr= - 11*m.b106 - 11*m.b121 + m.x670 - m.x671 + m.x686 >= -22)

m.c963 = Constraint(expr= - 11*m.b106 - 11*m.b124 + m.x670 - m.x672 + m.x686 >= -22)

m.c964 = Constraint(expr= - 11*m.b106 - 11*m.b126 + m.x670 - m.x673 + m.x686 >= -22)

m.c965 = Constraint(expr= - 11*m.b109 - 11*m.b124 + m.x671 - m.x672 + m.x686 >= -22)

m.c966 = Constraint(expr= - 11*m.b109 - 11*m.b126 + m.x671 - m.x673 + m.x686 >= -22)

m.c967 = Constraint(expr= - 11*m.b111 - 11*m.b126 + m.x672 - m.x673 + m.x686 >= -22)

m.c968 = Constraint(expr= - 11*m.b104 - 11*m.b119 + m.x669 - m.x670 + m.x687 >= -22)

m.c969 = Constraint(expr= - 11*m.b104 - 11*m.b122 + m.x669 - m.x671 + m.x687 >= -22)

m.c970 = Constraint(expr= - 11*m.b104 - 11*m.b125 + m.x669 - m.x672 + m.x687 >= -22)

m.c971 = Constraint(expr= - 11*m.b104 - 11*m.b127 + m.x669 - m.x673 + m.x687 >= -22)

m.c972 = Constraint(expr= - 11*m.b104 - 11*m.b128 + m.x669 - m.x674 + m.x687 >= -22)

m.c973 = Constraint(expr= - 11*m.b107 - 11*m.b122 + m.x670 - m.x671 + m.x687 >= -22)

m.c974 = Constraint(expr= - 11*m.b107 - 11*m.b125 + m.x670 - m.x672 + m.x687 >= -22)

m.c975 = Constraint(expr= - 11*m.b107 - 11*m.b127 + m.x670 - m.x673 + m.x687 >= -22)

m.c976 = Constraint(expr= - 11*m.b107 - 11*m.b128 + m.x670 - m.x674 + m.x687 >= -22)

m.c977 = Constraint(expr= - 11*m.b110 - 11*m.b125 + m.x671 - m.x672 + m.x687 >= -22)

m.c978 = Constraint(expr= - 11*m.b110 - 11*m.b127 + m.x671 - m.x673 + m.x687 >= -22)

m.c979 = Constraint(expr= - 11*m.b110 - 11*m.b128 + m.x671 - m.x674 + m.x687 >= -22)

m.c980 = Constraint(expr= - 11*m.b112 - 11*m.b127 + m.x672 - m.x673 + m.x687 >= -22)

m.c981 = Constraint(expr= - 11*m.b112 - 11*m.b128 + m.x672 - m.x674 + m.x687 >= -22)

m.c982 = Constraint(expr= - 11*m.b113 - 11*m.b128 + m.x673 - m.x674 + m.x687 >= -22)

m.c983 = Constraint(expr=   m.x667 - m.x668 + m.x675 == 0)

m.c984 = Constraint(expr=   m.x668 - m.x669 + m.x676 == 0)

m.c985 = Constraint(expr=   m.x669 - m.x670 + m.x677 == 0)

m.c986 = Constraint(expr=   m.x670 - m.x671 + m.x678 == 0)

m.c987 = Constraint(expr=   m.x671 - m.x672 + m.x679 == 0)

m.c988 = Constraint(expr=   m.x672 - m.x673 + m.x680 == 0)

m.c989 = Constraint(expr=   m.x673 - m.x674 + m.x681 == 0)

m.c990 = Constraint(expr=-m.x601*m.x152 + m.x343 == 0)

m.c991 = Constraint(expr=-m.x602*m.x153 + m.x344 == 0)

m.c992 = Constraint(expr=-m.x603*m.x154 + m.x345 == 0)

m.c993 = Constraint(expr=-m.x604*m.x155 + m.x346 == 0)

m.c994 = Constraint(expr=-m.x605*m.x156 + m.x347 == 0)

m.c995 = Constraint(expr=-m.x606*m.x157 + m.x348 == 0)

m.c996 = Constraint(expr=-m.x607*m.x152 + m.x350 == 0)

m.c997 = Constraint(expr=-m.x608*m.x153 + m.x351 == 0)

m.c998 = Constraint(expr=-m.x609*m.x154 + m.x352 == 0)

m.c999 = Constraint(expr=-m.x610*m.x155 + m.x353 == 0)

m.c1000 = Constraint(expr=-m.x611*m.x156 + m.x354 == 0)

m.c1001 = Constraint(expr=-m.x612*m.x157 + m.x355 == 0)

m.c1002 = Constraint(expr=-m.x643*m.x160 + m.x357 == 0)

m.c1003 = Constraint(expr=-m.x644*m.x161 + m.x358 == 0)

m.c1004 = Constraint(expr=-m.x645*m.x162 + m.x359 == 0)

m.c1005 = Constraint(expr=-m.x646*m.x163 + m.x360 == 0)

m.c1006 = Constraint(expr=-m.x647*m.x164 + m.x361 == 0)

m.c1007 = Constraint(expr=-m.x648*m.x165 + m.x362 == 0)

m.c1008 = Constraint(expr=-m.x649*m.x168 + m.x364 == 0)

m.c1009 = Constraint(expr=-m.x650*m.x169 + m.x365 == 0)

m.c1010 = Constraint(expr=-m.x651*m.x170 + m.x366 == 0)

m.c1011 = Constraint(expr=-m.x652*m.x171 + m.x367 == 0)

m.c1012 = Constraint(expr=-m.x653*m.x172 + m.x368 == 0)

m.c1013 = Constraint(expr=-m.x654*m.x173 + m.x369 == 0)

m.c1014 = Constraint(expr=-m.x655*m.x168 + m.x371 == 0)

m.c1015 = Constraint(expr=-m.x656*m.x169 + m.x372 == 0)

m.c1016 = Constraint(expr=-m.x657*m.x170 + m.x373 == 0)

m.c1017 = Constraint(expr=-m.x658*m.x171 + m.x374 == 0)

m.c1018 = Constraint(expr=-m.x659*m.x172 + m.x375 == 0)

m.c1019 = Constraint(expr=-m.x660*m.x173 + m.x376 == 0)

m.c1020 = Constraint(expr=-m.x631*m.x184 + m.x385 == 0)

m.c1021 = Constraint(expr=-m.x632*m.x185 + m.x386 == 0)

m.c1022 = Constraint(expr=-m.x633*m.x186 + m.x387 == 0)

m.c1023 = Constraint(expr=-m.x634*m.x187 + m.x388 == 0)

m.c1024 = Constraint(expr=-m.x635*m.x188 + m.x389 == 0)

m.c1025 = Constraint(expr=-m.x636*m.x189 + m.x390 == 0)

m.c1026 = Constraint(expr=-m.x637*m.x184 + m.x392 == 0)

m.c1027 = Constraint(expr=-m.x638*m.x185 + m.x393 == 0)

m.c1028 = Constraint(expr=-m.x639*m.x186 + m.x394 == 0)

m.c1029 = Constraint(expr=-m.x640*m.x187 + m.x395 == 0)

m.c1030 = Constraint(expr=-m.x641*m.x188 + m.x396 == 0)

m.c1031 = Constraint(expr=-m.x642*m.x189 + m.x397 == 0)

m.c1032 = Constraint(expr=-m.x649*m.x192 + m.x399 == 0)

m.c1033 = Constraint(expr=-m.x650*m.x193 + m.x400 == 0)

m.c1034 = Constraint(expr=-m.x651*m.x194 + m.x401 == 0)

m.c1035 = Constraint(expr=-m.x652*m.x195 + m.x402 == 0)

m.c1036 = Constraint(expr=-m.x653*m.x196 + m.x403 == 0)

m.c1037 = Constraint(expr=-m.x654*m.x197 + m.x404 == 0)

m.c1038 = Constraint(expr=-m.x655*m.x192 + m.x406 == 0)

m.c1039 = Constraint(expr=-m.x656*m.x193 + m.x407 == 0)

m.c1040 = Constraint(expr=-m.x657*m.x194 + m.x408 == 0)

m.c1041 = Constraint(expr=-m.x658*m.x195 + m.x409 == 0)

m.c1042 = Constraint(expr=-m.x659*m.x196 + m.x410 == 0)

m.c1043 = Constraint(expr=-m.x660*m.x197 + m.x411 == 0)

m.c1044 = Constraint(expr=-m.x661*m.x200 + m.x413 == 0)

m.c1045 = Constraint(expr=-m.x662*m.x201 + m.x414 == 0)

m.c1046 = Constraint(expr=-m.x663*m.x202 + m.x415 == 0)

m.c1047 = Constraint(expr=-m.x664*m.x203 + m.x416 == 0)

m.c1048 = Constraint(expr=-m.x665*m.x204 + m.x417 == 0)

m.c1049 = Constraint(expr=-m.x666*m.x205 + m.x418 == 0)

m.c1050 = Constraint(expr=-m.x613*m.x216 + m.x427 == 0)

m.c1051 = Constraint(expr=-m.x614*m.x217 + m.x428 == 0)

m.c1052 = Constraint(expr=-m.x615*m.x218 + m.x429 == 0)

m.c1053 = Constraint(expr=-m.x616*m.x219 + m.x430 == 0)

m.c1054 = Constraint(expr=-m.x617*m.x220 + m.x431 == 0)

m.c1055 = Constraint(expr=-m.x618*m.x221 + m.x432 == 0)

m.c1056 = Constraint(expr=-m.x619*m.x216 + m.x434 == 0)

m.c1057 = Constraint(expr=-m.x620*m.x217 + m.x435 == 0)

m.c1058 = Constraint(expr=-m.x621*m.x218 + m.x436 == 0)

m.c1059 = Constraint(expr=-m.x622*m.x219 + m.x437 == 0)

m.c1060 = Constraint(expr=-m.x623*m.x220 + m.x438 == 0)

m.c1061 = Constraint(expr=-m.x624*m.x221 + m.x439 == 0)

m.c1062 = Constraint(expr=-m.x625*m.x216 + m.x441 == 0)

m.c1063 = Constraint(expr=-m.x626*m.x217 + m.x442 == 0)

m.c1064 = Constraint(expr=-m.x627*m.x218 + m.x443 == 0)

m.c1065 = Constraint(expr=-m.x628*m.x219 + m.x444 == 0)

m.c1066 = Constraint(expr=-m.x629*m.x220 + m.x445 == 0)

m.c1067 = Constraint(expr=-m.x630*m.x221 + m.x446 == 0)

m.c1068 = Constraint(expr=-m.x643*m.x224 + m.x448 == 0)

m.c1069 = Constraint(expr=-m.x644*m.x225 + m.x449 == 0)

m.c1070 = Constraint(expr=-m.x645*m.x226 + m.x450 == 0)

m.c1071 = Constraint(expr=-m.x646*m.x227 + m.x451 == 0)

m.c1072 = Constraint(expr=-m.x647*m.x228 + m.x452 == 0)

m.c1073 = Constraint(expr=-m.x648*m.x229 + m.x453 == 0)

m.c1074 = Constraint(expr=-m.x649*m.x232 + m.x455 == 0)

m.c1075 = Constraint(expr=-m.x650*m.x233 + m.x456 == 0)

m.c1076 = Constraint(expr=-m.x651*m.x234 + m.x457 == 0)

m.c1077 = Constraint(expr=-m.x652*m.x235 + m.x458 == 0)

m.c1078 = Constraint(expr=-m.x653*m.x236 + m.x459 == 0)

m.c1079 = Constraint(expr=-m.x654*m.x237 + m.x460 == 0)

m.c1080 = Constraint(expr=-m.x655*m.x232 + m.x462 == 0)

m.c1081 = Constraint(expr=-m.x656*m.x233 + m.x463 == 0)

m.c1082 = Constraint(expr=-m.x657*m.x234 + m.x464 == 0)

m.c1083 = Constraint(expr=-m.x658*m.x235 + m.x465 == 0)

m.c1084 = Constraint(expr=-m.x659*m.x236 + m.x466 == 0)

m.c1085 = Constraint(expr=-m.x660*m.x237 + m.x467 == 0)

m.c1086 = Constraint(expr=-m.x661*m.x240 + m.x469 == 0)

m.c1087 = Constraint(expr=-m.x662*m.x241 + m.x470 == 0)

m.c1088 = Constraint(expr=-m.x663*m.x242 + m.x471 == 0)

m.c1089 = Constraint(expr=-m.x664*m.x243 + m.x472 == 0)

m.c1090 = Constraint(expr=-m.x665*m.x244 + m.x473 == 0)

m.c1091 = Constraint(expr=-m.x666*m.x245 + m.x474 == 0)

m.c1092 = Constraint(expr=-m.x601*m.x248 + m.x476 == 0)

m.c1093 = Constraint(expr=-m.x602*m.x249 + m.x477 == 0)

m.c1094 = Constraint(expr=-m.x603*m.x250 + m.x478 == 0)

m.c1095 = Constraint(expr=-m.x604*m.x251 + m.x479 == 0)

m.c1096 = Constraint(expr=-m.x605*m.x252 + m.x480 == 0)

m.c1097 = Constraint(expr=-m.x606*m.x253 + m.x481 == 0)

m.c1098 = Constraint(expr=-m.x607*m.x248 + m.x483 == 0)

m.c1099 = Constraint(expr=-m.x608*m.x249 + m.x484 == 0)

m.c1100 = Constraint(expr=-m.x609*m.x250 + m.x485 == 0)

m.c1101 = Constraint(expr=-m.x610*m.x251 + m.x486 == 0)

m.c1102 = Constraint(expr=-m.x611*m.x252 + m.x487 == 0)

m.c1103 = Constraint(expr=-m.x612*m.x253 + m.x488 == 0)

m.c1104 = Constraint(expr=-m.x643*m.x256 + m.x490 == 0)

m.c1105 = Constraint(expr=-m.x644*m.x257 + m.x491 == 0)

m.c1106 = Constraint(expr=-m.x645*m.x258 + m.x492 == 0)

m.c1107 = Constraint(expr=-m.x646*m.x259 + m.x493 == 0)

m.c1108 = Constraint(expr=-m.x647*m.x260 + m.x494 == 0)

m.c1109 = Constraint(expr=-m.x648*m.x261 + m.x495 == 0)

m.c1110 = Constraint(expr=-m.x649*m.x264 + m.x497 == 0)

m.c1111 = Constraint(expr=-m.x650*m.x265 + m.x498 == 0)

m.c1112 = Constraint(expr=-m.x651*m.x266 + m.x499 == 0)

m.c1113 = Constraint(expr=-m.x652*m.x267 + m.x500 == 0)

m.c1114 = Constraint(expr=-m.x653*m.x268 + m.x501 == 0)

m.c1115 = Constraint(expr=-m.x654*m.x269 + m.x502 == 0)

m.c1116 = Constraint(expr=-m.x655*m.x264 + m.x504 == 0)

m.c1117 = Constraint(expr=-m.x656*m.x265 + m.x505 == 0)

m.c1118 = Constraint(expr=-m.x657*m.x266 + m.x506 == 0)

m.c1119 = Constraint(expr=-m.x658*m.x267 + m.x507 == 0)

m.c1120 = Constraint(expr=-m.x659*m.x268 + m.x508 == 0)

m.c1121 = Constraint(expr=-m.x660*m.x269 + m.x509 == 0)

m.c1122 = Constraint(expr=-m.x613*m.x272 + m.x511 == 0)

m.c1123 = Constraint(expr=-m.x614*m.x273 + m.x512 == 0)

m.c1124 = Constraint(expr=-m.x615*m.x274 + m.x513 == 0)

m.c1125 = Constraint(expr=-m.x616*m.x275 + m.x514 == 0)

m.c1126 = Constraint(expr=-m.x617*m.x276 + m.x515 == 0)

m.c1127 = Constraint(expr=-m.x618*m.x277 + m.x516 == 0)

m.c1128 = Constraint(expr=-m.x619*m.x272 + m.x518 == 0)

m.c1129 = Constraint(expr=-m.x620*m.x273 + m.x519 == 0)

m.c1130 = Constraint(expr=-m.x621*m.x274 + m.x520 == 0)

m.c1131 = Constraint(expr=-m.x622*m.x275 + m.x521 == 0)

m.c1132 = Constraint(expr=-m.x623*m.x276 + m.x522 == 0)

m.c1133 = Constraint(expr=-m.x624*m.x277 + m.x523 == 0)

m.c1134 = Constraint(expr=-m.x625*m.x272 + m.x525 == 0)

m.c1135 = Constraint(expr=-m.x626*m.x273 + m.x526 == 0)

m.c1136 = Constraint(expr=-m.x627*m.x274 + m.x527 == 0)

m.c1137 = Constraint(expr=-m.x628*m.x275 + m.x528 == 0)

m.c1138 = Constraint(expr=-m.x629*m.x276 + m.x529 == 0)

m.c1139 = Constraint(expr=-m.x630*m.x277 + m.x530 == 0)

m.c1140 = Constraint(expr=-m.x643*m.x280 + m.x532 == 0)

m.c1141 = Constraint(expr=-m.x644*m.x281 + m.x533 == 0)

m.c1142 = Constraint(expr=-m.x645*m.x282 + m.x534 == 0)

m.c1143 = Constraint(expr=-m.x646*m.x283 + m.x535 == 0)

m.c1144 = Constraint(expr=-m.x647*m.x284 + m.x536 == 0)

m.c1145 = Constraint(expr=-m.x648*m.x285 + m.x537 == 0)

m.c1146 = Constraint(expr=-m.x649*m.x288 + m.x539 == 0)

m.c1147 = Constraint(expr=-m.x650*m.x289 + m.x540 == 0)

m.c1148 = Constraint(expr=-m.x651*m.x290 + m.x541 == 0)

m.c1149 = Constraint(expr=-m.x652*m.x291 + m.x542 == 0)

m.c1150 = Constraint(expr=-m.x653*m.x292 + m.x543 == 0)

m.c1151 = Constraint(expr=-m.x654*m.x293 + m.x544 == 0)

m.c1152 = Constraint(expr=-m.x655*m.x288 + m.x546 == 0)

m.c1153 = Constraint(expr=-m.x656*m.x289 + m.x547 == 0)

m.c1154 = Constraint(expr=-m.x657*m.x290 + m.x548 == 0)

m.c1155 = Constraint(expr=-m.x658*m.x291 + m.x549 == 0)

m.c1156 = Constraint(expr=-m.x659*m.x292 + m.x550 == 0)

m.c1157 = Constraint(expr=-m.x660*m.x293 + m.x551 == 0)

m.c1158 = Constraint(expr=-m.x661*m.x296 + m.x553 == 0)

m.c1159 = Constraint(expr=-m.x662*m.x297 + m.x554 == 0)

m.c1160 = Constraint(expr=-m.x663*m.x298 + m.x555 == 0)

m.c1161 = Constraint(expr=-m.x664*m.x299 + m.x556 == 0)

m.c1162 = Constraint(expr=-m.x665*m.x300 + m.x557 == 0)

m.c1163 = Constraint(expr=-m.x666*m.x301 + m.x558 == 0)

m.c1164 = Constraint(expr=-m.x631*m.x304 + m.x560 == 0)

m.c1165 = Constraint(expr=-m.x632*m.x305 + m.x561 == 0)

m.c1166 = Constraint(expr=-m.x633*m.x306 + m.x562 == 0)

m.c1167 = Constraint(expr=-m.x634*m.x307 + m.x563 == 0)

m.c1168 = Constraint(expr=-m.x635*m.x308 + m.x564 == 0)

m.c1169 = Constraint(expr=-m.x636*m.x309 + m.x565 == 0)

m.c1170 = Constraint(expr=-m.x637*m.x304 + m.x567 == 0)

m.c1171 = Constraint(expr=-m.x638*m.x305 + m.x568 == 0)

m.c1172 = Constraint(expr=-m.x639*m.x306 + m.x569 == 0)

m.c1173 = Constraint(expr=-m.x640*m.x307 + m.x570 == 0)

m.c1174 = Constraint(expr=-m.x641*m.x308 + m.x571 == 0)

m.c1175 = Constraint(expr=-m.x642*m.x309 + m.x572 == 0)

m.c1176 = Constraint(expr=-m.x649*m.x312 + m.x574 == 0)

m.c1177 = Constraint(expr=-m.x650*m.x313 + m.x575 == 0)

m.c1178 = Constraint(expr=-m.x651*m.x314 + m.x576 == 0)

m.c1179 = Constraint(expr=-m.x652*m.x315 + m.x577 == 0)

m.c1180 = Constraint(expr=-m.x653*m.x316 + m.x578 == 0)

m.c1181 = Constraint(expr=-m.x654*m.x317 + m.x579 == 0)

m.c1182 = Constraint(expr=-m.x655*m.x312 + m.x581 == 0)

m.c1183 = Constraint(expr=-m.x656*m.x313 + m.x582 == 0)

m.c1184 = Constraint(expr=-m.x657*m.x314 + m.x583 == 0)

m.c1185 = Constraint(expr=-m.x658*m.x315 + m.x584 == 0)

m.c1186 = Constraint(expr=-m.x659*m.x316 + m.x585 == 0)

m.c1187 = Constraint(expr=-m.x660*m.x317 + m.x586 == 0)

m.c1188 = Constraint(expr=-m.x661*m.x320 + m.x588 == 0)

m.c1189 = Constraint(expr=-m.x662*m.x321 + m.x589 == 0)

m.c1190 = Constraint(expr=-m.x663*m.x322 + m.x590 == 0)

m.c1191 = Constraint(expr=-m.x664*m.x323 + m.x591 == 0)

m.c1192 = Constraint(expr=-m.x665*m.x324 + m.x592 == 0)

m.c1193 = Constraint(expr=-m.x666*m.x325 + m.x593 == 0)

m.c1194 = Constraint(expr=-m.x643*m.x328 + m.x595 == 0)

m.c1195 = Constraint(expr=-m.x644*m.x329 + m.x596 == 0)

m.c1196 = Constraint(expr=-m.x645*m.x330 + m.x597 == 0)

m.c1197 = Constraint(expr=-m.x646*m.x331 + m.x598 == 0)

m.c1198 = Constraint(expr=-m.x647*m.x332 + m.x599 == 0)

m.c1199 = Constraint(expr=-m.x648*m.x333 + m.x600 == 0)
