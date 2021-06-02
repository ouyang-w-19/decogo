#  MINLP written by GAMS Convert at 04/21/18 13:51:21
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        925      277      342      306        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        534      396      138        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       3211     3021      190        0
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
m.b129 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b130 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b131 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b132 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b133 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b134 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b135 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b136 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b137 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b138 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x172 = Var(within=Reals,bounds=(0,700),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,700),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,700),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,700),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,700),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,700),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,700),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,700),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,700),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,700),initialize=0)
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
m.x200 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,800),initialize=0)
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
m.x228 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x235 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,600),initialize=0)
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
m.x270 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x271 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x272 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x273 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x274 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x275 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x276 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x277 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x278 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x279 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x280 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x281 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x282 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x283 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x284 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x285 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x286 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x287 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x289 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x290 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x291 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x292 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x293 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x294 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x295 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x296 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x297 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x298 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x299 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x300 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x301 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x302 = Var(within=Reals,bounds=(0,300),initialize=0)
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
m.x502 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x503 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x504 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x505 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x506 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x507 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x508 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x509 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x510 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x511 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x512 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x513 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x514 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x515 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x516 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x517 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x518 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x519 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x520 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x521 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x522 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x523 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x524 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x525 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x526 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x527 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x528 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x529 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x530 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x531 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x532 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x533 = Var(within=Reals,bounds=(15,15),initialize=15)

m.obj = Objective(expr=   3*m.x322 + 3*m.x323 + 3*m.x324 + 3*m.x325 + 3*m.x326 + 3*m.x327 + 3*m.x328 + 3*m.x329
                        + 3*m.x330 + 3*m.x331 + 3*m.x332 + 3*m.x333 + 3*m.x334 + 3*m.x335 + 3*m.x336 + 3*m.x337
                        + 3*m.x338 + 3*m.x339 + 5*m.x358 + 5*m.x359 + 5*m.x360 + 5*m.x361 + 5*m.x362 + 5*m.x363
                        + 5*m.x364 + 5*m.x365 + 5*m.x366 + 5*m.x367 + 5*m.x368 + 5*m.x369 + 5*m.x370 + 5*m.x371
                        + 5*m.x372 + 5*m.x373 + 5*m.x374 + 5*m.x375 + 5*m.x376 + 5*m.x377 + 5*m.x378 + 5*m.x379
                        + 5*m.x380 + 5*m.x381 + 6.5*m.x400 + 6.5*m.x401 + 6.5*m.x402 + 6.5*m.x403 + 6.5*m.x404
                        + 6.5*m.x405 + 6.5*m.x406 + 6.5*m.x407 + 6.5*m.x408 + 6.5*m.x409 + 6.5*m.x410 + 6.5*m.x411
                        + 6.5*m.x412 + 6.5*m.x413 + 6.5*m.x414 + 6.5*m.x415 + 6.5*m.x416 + 6.5*m.x417 + 6.5*m.x418
                        + 6.5*m.x419 + 6.5*m.x420 + 6.5*m.x421 + 6.5*m.x422 + 6.5*m.x423 + 3.1*m.x430 + 3.1*m.x431
                        + 3.1*m.x432 + 3.1*m.x433 + 3.1*m.x434 + 3.1*m.x435 + 7.5*m.x454 + 7.5*m.x455 + 7.5*m.x456
                        + 7.5*m.x457 + 7.5*m.x458 + 7.5*m.x459 + 7.5*m.x460 + 7.5*m.x461 + 7.5*m.x462 + 7.5*m.x463
                        + 7.5*m.x464 + 7.5*m.x465 + 7.5*m.x466 + 7.5*m.x467 + 7.5*m.x468 + 7.5*m.x469 + 7.5*m.x470
                        + 7.5*m.x471 + 3.17*m.x472 + 3.17*m.x473 + 3.17*m.x474 + 3.17*m.x475 + 3.17*m.x476 + 3.17*m.x477
                        + 4.83*m.x478 + 4.83*m.x479 + 4.83*m.x480 + 4.83*m.x481 + 4.83*m.x482 + 4.83*m.x483
                        + 4.83*m.x484 + 4.83*m.x485 + 4.83*m.x486 + 4.83*m.x487 + 4.83*m.x488 + 4.83*m.x489
                        + 6.33*m.x490 + 6.33*m.x491 + 6.33*m.x492 + 6.33*m.x493 + 6.33*m.x494 + 6.33*m.x495
                        + 6.33*m.x496 + 6.33*m.x497 + 6.33*m.x498 + 6.33*m.x499 + 6.33*m.x500 + 6.33*m.x501
                       , sense=maximize)

m.c2 = Constraint(expr=   m.x157 == 600)

m.c3 = Constraint(expr= - m.x157 + m.x158 + m.x304 == 0)

m.c4 = Constraint(expr= - m.x158 + m.x159 + m.x305 == 0)

m.c5 = Constraint(expr= - m.x159 + m.x160 + m.x306 == 0)

m.c6 = Constraint(expr= - m.x160 + m.x161 + m.x307 == 0)

m.c7 = Constraint(expr= - m.x161 + m.x162 + m.x308 == 0)

m.c8 = Constraint(expr= - m.x162 + m.x163 + m.x309 == 0)

m.c9 = Constraint(expr=   m.x164 == 100)

m.c10 = Constraint(expr= - m.x164 + m.x165 - m.x304 + m.x310 + m.x316 == 0)

m.c11 = Constraint(expr= - m.x165 + m.x166 - m.x305 + m.x311 + m.x317 == 0)

m.c12 = Constraint(expr= - m.x166 + m.x167 - m.x306 + m.x312 + m.x318 == 0)

m.c13 = Constraint(expr= - m.x167 + m.x168 - m.x307 + m.x313 + m.x319 == 0)

m.c14 = Constraint(expr= - m.x168 + m.x169 - m.x308 + m.x314 + m.x320 == 0)

m.c15 = Constraint(expr= - m.x169 + m.x170 - m.x309 + m.x315 + m.x321 == 0)

m.c16 = Constraint(expr=   m.x171 == 0)

m.c17 = Constraint(expr= - m.x171 + m.x172 - m.x310 + m.x322 == 0)

m.c18 = Constraint(expr= - m.x172 + m.x173 - m.x311 + m.x323 == 0)

m.c19 = Constraint(expr= - m.x173 + m.x174 - m.x312 + m.x324 == 0)

m.c20 = Constraint(expr= - m.x174 + m.x175 - m.x313 + m.x325 == 0)

m.c21 = Constraint(expr= - m.x175 + m.x176 - m.x314 + m.x326 == 0)

m.c22 = Constraint(expr= - m.x176 + m.x177 - m.x315 + m.x327 == 0)

m.c23 = Constraint(expr=   m.x178 == 0)

m.c24 = Constraint(expr= - m.x178 + m.x179 - m.x316 + m.x328 + m.x334 == 0)

m.c25 = Constraint(expr= - m.x179 + m.x180 - m.x317 + m.x329 + m.x335 == 0)

m.c26 = Constraint(expr= - m.x180 + m.x181 - m.x318 + m.x330 + m.x336 == 0)

m.c27 = Constraint(expr= - m.x181 + m.x182 - m.x319 + m.x331 + m.x337 == 0)

m.c28 = Constraint(expr= - m.x182 + m.x183 - m.x320 + m.x332 + m.x338 == 0)

m.c29 = Constraint(expr= - m.x183 + m.x184 - m.x321 + m.x333 + m.x339 == 0)

m.c30 = Constraint(expr=   m.x185 == 600)

m.c31 = Constraint(expr= - m.x185 + m.x186 + m.x340 == 0)

m.c32 = Constraint(expr= - m.x186 + m.x187 + m.x341 == 0)

m.c33 = Constraint(expr= - m.x187 + m.x188 + m.x342 == 0)

m.c34 = Constraint(expr= - m.x188 + m.x189 + m.x343 == 0)

m.c35 = Constraint(expr= - m.x189 + m.x190 + m.x344 == 0)

m.c36 = Constraint(expr= - m.x190 + m.x191 + m.x345 == 0)

m.c37 = Constraint(expr=   m.x192 == 500)

m.c38 = Constraint(expr= - m.x192 + m.x193 - m.x340 + m.x346 + m.x352 == 0)

m.c39 = Constraint(expr= - m.x193 + m.x194 - m.x341 + m.x347 + m.x353 == 0)

m.c40 = Constraint(expr= - m.x194 + m.x195 - m.x342 + m.x348 + m.x354 == 0)

m.c41 = Constraint(expr= - m.x195 + m.x196 - m.x343 + m.x349 + m.x355 == 0)

m.c42 = Constraint(expr= - m.x196 + m.x197 - m.x344 + m.x350 + m.x356 == 0)

m.c43 = Constraint(expr= - m.x197 + m.x198 - m.x345 + m.x351 + m.x357 == 0)

m.c44 = Constraint(expr=   m.x199 == 0)

m.c45 = Constraint(expr= - m.x199 + m.x200 - m.x346 + m.x358 + m.x364 == 0)

m.c46 = Constraint(expr= - m.x200 + m.x201 - m.x347 + m.x359 + m.x365 == 0)

m.c47 = Constraint(expr= - m.x201 + m.x202 - m.x348 + m.x360 + m.x366 == 0)

m.c48 = Constraint(expr= - m.x202 + m.x203 - m.x349 + m.x361 + m.x367 == 0)

m.c49 = Constraint(expr= - m.x203 + m.x204 - m.x350 + m.x362 + m.x368 == 0)

m.c50 = Constraint(expr= - m.x204 + m.x205 - m.x351 + m.x363 + m.x369 == 0)

m.c51 = Constraint(expr=   m.x206 == 0)

m.c52 = Constraint(expr= - m.x206 + m.x207 - m.x352 + m.x370 + m.x376 == 0)

m.c53 = Constraint(expr= - m.x207 + m.x208 - m.x353 + m.x371 + m.x377 == 0)

m.c54 = Constraint(expr= - m.x208 + m.x209 - m.x354 + m.x372 + m.x378 == 0)

m.c55 = Constraint(expr= - m.x209 + m.x210 - m.x355 + m.x373 + m.x379 == 0)

m.c56 = Constraint(expr= - m.x210 + m.x211 - m.x356 + m.x374 + m.x380 == 0)

m.c57 = Constraint(expr= - m.x211 + m.x212 - m.x357 + m.x375 + m.x381 == 0)

m.c58 = Constraint(expr=   m.x213 == 600)

m.c59 = Constraint(expr= - m.x213 + m.x214 + m.x382 == 0)

m.c60 = Constraint(expr= - m.x214 + m.x215 + m.x383 == 0)

m.c61 = Constraint(expr= - m.x215 + m.x216 + m.x384 == 0)

m.c62 = Constraint(expr= - m.x216 + m.x217 + m.x385 == 0)

m.c63 = Constraint(expr= - m.x217 + m.x218 + m.x386 == 0)

m.c64 = Constraint(expr= - m.x218 + m.x219 + m.x387 == 0)

m.c65 = Constraint(expr=   m.x220 == 400)

m.c66 = Constraint(expr= - m.x220 + m.x221 - m.x382 + m.x388 + m.x394 == 0)

m.c67 = Constraint(expr= - m.x221 + m.x222 - m.x383 + m.x389 + m.x395 == 0)

m.c68 = Constraint(expr= - m.x222 + m.x223 - m.x384 + m.x390 + m.x396 == 0)

m.c69 = Constraint(expr= - m.x223 + m.x224 - m.x385 + m.x391 + m.x397 == 0)

m.c70 = Constraint(expr= - m.x224 + m.x225 - m.x386 + m.x392 + m.x398 == 0)

m.c71 = Constraint(expr= - m.x225 + m.x226 - m.x387 + m.x393 + m.x399 == 0)

m.c72 = Constraint(expr=   m.x227 == 0)

m.c73 = Constraint(expr= - m.x227 + m.x228 - m.x388 + m.x400 + m.x406 == 0)

m.c74 = Constraint(expr= - m.x228 + m.x229 - m.x389 + m.x401 + m.x407 == 0)

m.c75 = Constraint(expr= - m.x229 + m.x230 - m.x390 + m.x402 + m.x408 == 0)

m.c76 = Constraint(expr= - m.x230 + m.x231 - m.x391 + m.x403 + m.x409 == 0)

m.c77 = Constraint(expr= - m.x231 + m.x232 - m.x392 + m.x404 + m.x410 == 0)

m.c78 = Constraint(expr= - m.x232 + m.x233 - m.x393 + m.x405 + m.x411 == 0)

m.c79 = Constraint(expr=   m.x234 == 0)

m.c80 = Constraint(expr= - m.x234 + m.x235 - m.x394 + m.x412 + m.x418 == 0)

m.c81 = Constraint(expr= - m.x235 + m.x236 - m.x395 + m.x413 + m.x419 == 0)

m.c82 = Constraint(expr= - m.x236 + m.x237 - m.x396 + m.x414 + m.x420 == 0)

m.c83 = Constraint(expr= - m.x237 + m.x238 - m.x397 + m.x415 + m.x421 == 0)

m.c84 = Constraint(expr= - m.x238 + m.x239 - m.x398 + m.x416 + m.x422 == 0)

m.c85 = Constraint(expr= - m.x239 + m.x240 - m.x399 + m.x417 + m.x423 == 0)

m.c86 = Constraint(expr=   m.x241 == 600)

m.c87 = Constraint(expr= - m.x241 + m.x242 + m.x424 == 0)

m.c88 = Constraint(expr= - m.x242 + m.x243 + m.x425 == 0)

m.c89 = Constraint(expr= - m.x243 + m.x244 + m.x426 == 0)

m.c90 = Constraint(expr= - m.x244 + m.x245 + m.x427 == 0)

m.c91 = Constraint(expr= - m.x245 + m.x246 + m.x428 == 0)

m.c92 = Constraint(expr= - m.x246 + m.x247 + m.x429 == 0)

m.c93 = Constraint(expr=   m.x248 == 0)

m.c94 = Constraint(expr= - m.x248 + m.x249 - m.x424 + m.x430 == 0)

m.c95 = Constraint(expr= - m.x249 + m.x250 - m.x425 + m.x431 == 0)

m.c96 = Constraint(expr= - m.x250 + m.x251 - m.x426 + m.x432 == 0)

m.c97 = Constraint(expr= - m.x251 + m.x252 - m.x427 + m.x433 == 0)

m.c98 = Constraint(expr= - m.x252 + m.x253 - m.x428 + m.x434 == 0)

m.c99 = Constraint(expr= - m.x253 + m.x254 - m.x429 + m.x435 == 0)

m.c100 = Constraint(expr=   m.x255 == 300)

m.c101 = Constraint(expr= - m.x255 + m.x256 + m.x436 + m.x442 == 0)

m.c102 = Constraint(expr= - m.x256 + m.x257 + m.x437 + m.x443 == 0)

m.c103 = Constraint(expr= - m.x257 + m.x258 + m.x438 + m.x444 == 0)

m.c104 = Constraint(expr= - m.x258 + m.x259 + m.x439 + m.x445 == 0)

m.c105 = Constraint(expr= - m.x259 + m.x260 + m.x440 + m.x446 == 0)

m.c106 = Constraint(expr= - m.x260 + m.x261 + m.x441 + m.x447 == 0)

m.c107 = Constraint(expr=   m.x262 == 600)

m.c108 = Constraint(expr= - m.x262 + m.x263 + m.x448 == 0)

m.c109 = Constraint(expr= - m.x263 + m.x264 + m.x449 == 0)

m.c110 = Constraint(expr= - m.x264 + m.x265 + m.x450 == 0)

m.c111 = Constraint(expr= - m.x265 + m.x266 + m.x451 == 0)

m.c112 = Constraint(expr= - m.x266 + m.x267 + m.x452 == 0)

m.c113 = Constraint(expr= - m.x267 + m.x268 + m.x453 == 0)

m.c114 = Constraint(expr=   m.x269 == 0)

m.c115 = Constraint(expr= - m.x269 + m.x270 - m.x436 + m.x454 + m.x460 == 0)

m.c116 = Constraint(expr= - m.x270 + m.x271 - m.x437 + m.x455 + m.x461 == 0)

m.c117 = Constraint(expr= - m.x271 + m.x272 - m.x438 + m.x456 + m.x462 == 0)

m.c118 = Constraint(expr= - m.x272 + m.x273 - m.x439 + m.x457 + m.x463 == 0)

m.c119 = Constraint(expr= - m.x273 + m.x274 - m.x440 + m.x458 + m.x464 == 0)

m.c120 = Constraint(expr= - m.x274 + m.x275 - m.x441 + m.x459 + m.x465 == 0)

m.c121 = Constraint(expr=   m.x276 == 300)

m.c122 = Constraint(expr= - m.x276 + m.x277 - m.x442 - m.x448 + m.x466 == 0)

m.c123 = Constraint(expr= - m.x277 + m.x278 - m.x443 - m.x449 + m.x467 == 0)

m.c124 = Constraint(expr= - m.x278 + m.x279 - m.x444 - m.x450 + m.x468 == 0)

m.c125 = Constraint(expr= - m.x279 + m.x280 - m.x445 - m.x451 + m.x469 == 0)

m.c126 = Constraint(expr= - m.x280 + m.x281 - m.x446 - m.x452 + m.x470 == 0)

m.c127 = Constraint(expr= - m.x281 + m.x282 - m.x447 - m.x453 + m.x471 == 0)

m.c128 = Constraint(expr=   m.x283 == 50)

m.c129 = Constraint(expr= - m.x283 + m.x284 + m.x472 == 0)

m.c130 = Constraint(expr= - m.x284 + m.x285 + m.x473 == 0)

m.c131 = Constraint(expr= - m.x285 + m.x286 + m.x474 == 0)

m.c132 = Constraint(expr= - m.x286 + m.x287 + m.x475 == 0)

m.c133 = Constraint(expr= - m.x287 + m.x288 + m.x476 == 0)

m.c134 = Constraint(expr= - m.x288 + m.x289 + m.x477 == 0)

m.c135 = Constraint(expr=   m.x290 == 300)

m.c136 = Constraint(expr= - m.x290 + m.x291 + m.x478 + m.x484 == 0)

m.c137 = Constraint(expr= - m.x291 + m.x292 + m.x479 + m.x485 == 0)

m.c138 = Constraint(expr= - m.x292 + m.x293 + m.x480 + m.x486 == 0)

m.c139 = Constraint(expr= - m.x293 + m.x294 + m.x481 + m.x487 == 0)

m.c140 = Constraint(expr= - m.x294 + m.x295 + m.x482 + m.x488 == 0)

m.c141 = Constraint(expr= - m.x295 + m.x296 + m.x483 + m.x489 == 0)

m.c142 = Constraint(expr=   m.x297 == 300)

m.c143 = Constraint(expr= - m.x297 + m.x298 + m.x490 + m.x496 == 0)

m.c144 = Constraint(expr= - m.x298 + m.x299 + m.x491 + m.x497 == 0)

m.c145 = Constraint(expr= - m.x299 + m.x300 + m.x492 + m.x498 == 0)

m.c146 = Constraint(expr= - m.x300 + m.x301 + m.x493 + m.x499 == 0)

m.c147 = Constraint(expr= - m.x301 + m.x302 + m.x494 + m.x500 == 0)

m.c148 = Constraint(expr= - m.x302 + m.x303 + m.x495 + m.x501 == 0)

m.c149 = Constraint(expr=   m.x242 <= 900)

m.c150 = Constraint(expr=   m.x243 <= 900)

m.c151 = Constraint(expr=   m.x244 <= 900)

m.c152 = Constraint(expr=   m.x245 <= 900)

m.c153 = Constraint(expr=   m.x246 <= 900)

m.c154 = Constraint(expr=   m.x247 <= 900)

m.c155 = Constraint(expr=   m.x165 <= 1100)

m.c156 = Constraint(expr=   m.x166 <= 1100)

m.c157 = Constraint(expr=   m.x167 <= 1100)

m.c158 = Constraint(expr=   m.x168 <= 1100)

m.c159 = Constraint(expr=   m.x169 <= 1100)

m.c160 = Constraint(expr=   m.x170 <= 1100)

m.c161 = Constraint(expr=   m.x193 <= 1100)

m.c162 = Constraint(expr=   m.x194 <= 1100)

m.c163 = Constraint(expr=   m.x195 <= 1100)

m.c164 = Constraint(expr=   m.x196 <= 1100)

m.c165 = Constraint(expr=   m.x197 <= 1100)

m.c166 = Constraint(expr=   m.x198 <= 1100)

m.c167 = Constraint(expr=   m.x221 <= 1100)

m.c168 = Constraint(expr=   m.x222 <= 1100)

m.c169 = Constraint(expr=   m.x223 <= 1100)

m.c170 = Constraint(expr=   m.x224 <= 1100)

m.c171 = Constraint(expr=   m.x225 <= 1100)

m.c172 = Constraint(expr=   m.x226 <= 1100)

m.c173 = Constraint(expr=   m.x256 <= 900)

m.c174 = Constraint(expr=   m.x257 <= 900)

m.c175 = Constraint(expr=   m.x258 <= 900)

m.c176 = Constraint(expr=   m.x259 <= 900)

m.c177 = Constraint(expr=   m.x260 <= 900)

m.c178 = Constraint(expr=   m.x261 <= 900)

m.c179 = Constraint(expr=   m.x263 <= 900)

m.c180 = Constraint(expr=   m.x264 <= 900)

m.c181 = Constraint(expr=   m.x265 <= 900)

m.c182 = Constraint(expr=   m.x266 <= 900)

m.c183 = Constraint(expr=   m.x267 <= 900)

m.c184 = Constraint(expr=   m.x268 <= 900)

m.c185 = Constraint(expr=   m.x172 + m.x249 + m.x284 <= 800)

m.c186 = Constraint(expr=   m.x173 + m.x250 + m.x285 <= 800)

m.c187 = Constraint(expr=   m.x174 + m.x251 + m.x286 <= 800)

m.c188 = Constraint(expr=   m.x175 + m.x252 + m.x287 <= 800)

m.c189 = Constraint(expr=   m.x176 + m.x253 + m.x288 <= 800)

m.c190 = Constraint(expr=   m.x177 + m.x254 + m.x289 <= 800)

m.c191 = Constraint(expr=   m.x179 + m.x200 + m.x228 + m.x291 <= 800)

m.c192 = Constraint(expr=   m.x180 + m.x201 + m.x229 + m.x292 <= 800)

m.c193 = Constraint(expr=   m.x181 + m.x202 + m.x230 + m.x293 <= 800)

m.c194 = Constraint(expr=   m.x182 + m.x203 + m.x231 + m.x294 <= 800)

m.c195 = Constraint(expr=   m.x183 + m.x204 + m.x232 + m.x295 <= 800)

m.c196 = Constraint(expr=   m.x184 + m.x205 + m.x233 + m.x296 <= 800)

m.c197 = Constraint(expr=   m.x207 + m.x235 + m.x270 + m.x298 <= 800)

m.c198 = Constraint(expr=   m.x208 + m.x236 + m.x271 + m.x299 <= 800)

m.c199 = Constraint(expr=   m.x209 + m.x237 + m.x272 + m.x300 <= 800)

m.c200 = Constraint(expr=   m.x210 + m.x238 + m.x273 + m.x301 <= 800)

m.c201 = Constraint(expr=   m.x211 + m.x239 + m.x274 + m.x302 <= 800)

m.c202 = Constraint(expr=   m.x212 + m.x240 + m.x275 + m.x303 <= 800)

m.c203 = Constraint(expr=   m.x277 <= 800)

m.c204 = Constraint(expr=   m.x278 <= 800)

m.c205 = Constraint(expr=   m.x279 <= 800)

m.c206 = Constraint(expr=   m.x280 <= 800)

m.c207 = Constraint(expr=   m.x281 <= 800)

m.c208 = Constraint(expr=   m.x282 <= 800)

m.c209 = Constraint(expr=   m.x242 >= 100)

m.c210 = Constraint(expr=   m.x243 >= 100)

m.c211 = Constraint(expr=   m.x244 >= 100)

m.c212 = Constraint(expr=   m.x245 >= 100)

m.c213 = Constraint(expr=   m.x246 >= 100)

m.c214 = Constraint(expr=   m.x247 >= 100)

m.c215 = Constraint(expr=   m.x165 >= 100)

m.c216 = Constraint(expr=   m.x166 >= 100)

m.c217 = Constraint(expr=   m.x167 >= 100)

m.c218 = Constraint(expr=   m.x168 >= 100)

m.c219 = Constraint(expr=   m.x169 >= 100)

m.c220 = Constraint(expr=   m.x170 >= 100)

m.c221 = Constraint(expr=   m.x193 >= 100)

m.c222 = Constraint(expr=   m.x194 >= 100)

m.c223 = Constraint(expr=   m.x195 >= 100)

m.c224 = Constraint(expr=   m.x196 >= 100)

m.c225 = Constraint(expr=   m.x197 >= 100)

m.c226 = Constraint(expr=   m.x198 >= 100)

m.c227 = Constraint(expr=   m.x221 >= 100)

m.c228 = Constraint(expr=   m.x222 >= 100)

m.c229 = Constraint(expr=   m.x223 >= 100)

m.c230 = Constraint(expr=   m.x224 >= 100)

m.c231 = Constraint(expr=   m.x225 >= 100)

m.c232 = Constraint(expr=   m.x226 >= 100)

m.c233 = Constraint(expr=   m.x256 >= 100)

m.c234 = Constraint(expr=   m.x257 >= 100)

m.c235 = Constraint(expr=   m.x258 >= 100)

m.c236 = Constraint(expr=   m.x259 >= 100)

m.c237 = Constraint(expr=   m.x260 >= 100)

m.c238 = Constraint(expr=   m.x261 >= 100)

m.c239 = Constraint(expr=   m.x263 >= 100)

m.c240 = Constraint(expr=   m.x264 >= 100)

m.c241 = Constraint(expr=   m.x265 >= 100)

m.c242 = Constraint(expr=   m.x266 >= 100)

m.c243 = Constraint(expr=   m.x267 >= 100)

m.c244 = Constraint(expr=   m.x268 >= 100)

m.c245 = Constraint(expr=   m.x172 + m.x249 + m.x284 >= 0)

m.c246 = Constraint(expr=   m.x173 + m.x250 + m.x285 >= 0)

m.c247 = Constraint(expr=   m.x174 + m.x251 + m.x286 >= 0)

m.c248 = Constraint(expr=   m.x175 + m.x252 + m.x287 >= 0)

m.c249 = Constraint(expr=   m.x176 + m.x253 + m.x288 >= 0)

m.c250 = Constraint(expr=   m.x177 + m.x254 + m.x289 >= 0)

m.c251 = Constraint(expr=   m.x179 + m.x200 + m.x228 + m.x291 >= 0)

m.c252 = Constraint(expr=   m.x180 + m.x201 + m.x229 + m.x292 >= 0)

m.c253 = Constraint(expr=   m.x181 + m.x202 + m.x230 + m.x293 >= 0)

m.c254 = Constraint(expr=   m.x182 + m.x203 + m.x231 + m.x294 >= 0)

m.c255 = Constraint(expr=   m.x183 + m.x204 + m.x232 + m.x295 >= 0)

m.c256 = Constraint(expr=   m.x184 + m.x205 + m.x233 + m.x296 >= 0)

m.c257 = Constraint(expr=   m.x207 + m.x235 + m.x270 + m.x298 >= 0)

m.c258 = Constraint(expr=   m.x208 + m.x236 + m.x271 + m.x299 >= 0)

m.c259 = Constraint(expr=   m.x209 + m.x237 + m.x272 + m.x300 >= 0)

m.c260 = Constraint(expr=   m.x210 + m.x238 + m.x273 + m.x301 >= 0)

m.c261 = Constraint(expr=   m.x211 + m.x239 + m.x274 + m.x302 >= 0)

m.c262 = Constraint(expr=   m.x212 + m.x240 + m.x275 + m.x303 >= 0)

m.c263 = Constraint(expr=   m.x277 >= 0)

m.c264 = Constraint(expr=   m.x278 >= 0)

m.c265 = Constraint(expr=   m.x279 >= 0)

m.c266 = Constraint(expr=   m.x280 >= 0)

m.c267 = Constraint(expr=   m.x281 >= 0)

m.c268 = Constraint(expr=   m.x282 >= 0)

m.c269 = Constraint(expr= - 0.005*m.x172 - 0.004*m.x249 - 0.0033*m.x284 <= 0)

m.c270 = Constraint(expr= - 0.005*m.x173 - 0.004*m.x250 - 0.0033*m.x285 <= 0)

m.c271 = Constraint(expr= - 0.005*m.x174 - 0.004*m.x251 - 0.0033*m.x286 <= 0)

m.c272 = Constraint(expr= - 0.005*m.x175 - 0.004*m.x252 - 0.0033*m.x287 <= 0)

m.c273 = Constraint(expr= - 0.005*m.x176 - 0.004*m.x253 - 0.0033*m.x288 <= 0)

m.c274 = Constraint(expr= - 0.005*m.x177 - 0.004*m.x254 - 0.0033*m.x289 <= 0)

m.c275 = Constraint(expr= - 0.02*m.x179 + 0.015*m.x228 - 0.0017*m.x291 <= 0)

m.c276 = Constraint(expr= - 0.02*m.x180 + 0.015*m.x229 - 0.0017*m.x292 <= 0)

m.c277 = Constraint(expr= - 0.02*m.x181 + 0.015*m.x230 - 0.0017*m.x293 <= 0)

m.c278 = Constraint(expr= - 0.02*m.x182 + 0.015*m.x231 - 0.0017*m.x294 <= 0)

m.c279 = Constraint(expr= - 0.02*m.x183 + 0.015*m.x232 - 0.0017*m.x295 <= 0)

m.c280 = Constraint(expr= - 0.02*m.x184 + 0.015*m.x233 - 0.0017*m.x296 <= 0)

m.c281 = Constraint(expr= - 0.015*m.x207 + 0.01*m.x270 - 0.00170000000000001*m.x298 <= 0)

m.c282 = Constraint(expr= - 0.015*m.x208 + 0.01*m.x271 - 0.00170000000000001*m.x299 <= 0)

m.c283 = Constraint(expr= - 0.015*m.x209 + 0.01*m.x272 - 0.00170000000000001*m.x300 <= 0)

m.c284 = Constraint(expr= - 0.015*m.x210 + 0.01*m.x273 - 0.00170000000000001*m.x301 <= 0)

m.c285 = Constraint(expr= - 0.015*m.x211 + 0.01*m.x274 - 0.00170000000000001*m.x302 <= 0)

m.c286 = Constraint(expr= - 0.015*m.x212 + 0.01*m.x275 - 0.00170000000000001*m.x303 <= 0)

m.c287 = Constraint(expr=   0.001*m.x249 + 0.0017*m.x284 >= 0)

m.c288 = Constraint(expr=   0.001*m.x250 + 0.0017*m.x285 >= 0)

m.c289 = Constraint(expr=   0.001*m.x251 + 0.0017*m.x286 >= 0)

m.c290 = Constraint(expr=   0.001*m.x252 + 0.0017*m.x287 >= 0)

m.c291 = Constraint(expr=   0.001*m.x253 + 0.0017*m.x288 >= 0)

m.c292 = Constraint(expr=   0.001*m.x254 + 0.0017*m.x289 >= 0)

m.c293 = Constraint(expr= - 0.013*m.x179 + 0.00700000000000001*m.x200 + 0.022*m.x228 + 0.00530000000000001*m.x291 >= 0)

m.c294 = Constraint(expr= - 0.013*m.x180 + 0.00700000000000001*m.x201 + 0.022*m.x229 + 0.00530000000000001*m.x292 >= 0)

m.c295 = Constraint(expr= - 0.013*m.x181 + 0.00700000000000001*m.x202 + 0.022*m.x230 + 0.00530000000000001*m.x293 >= 0)

m.c296 = Constraint(expr= - 0.013*m.x182 + 0.00700000000000001*m.x203 + 0.022*m.x231 + 0.00530000000000001*m.x294 >= 0)

m.c297 = Constraint(expr= - 0.013*m.x183 + 0.00700000000000001*m.x204 + 0.022*m.x232 + 0.00530000000000001*m.x295 >= 0)

m.c298 = Constraint(expr= - 0.013*m.x184 + 0.00700000000000001*m.x205 + 0.022*m.x233 + 0.00530000000000001*m.x296 >= 0)

m.c299 = Constraint(expr= - 0.01*m.x207 + 0.005*m.x235 + 0.015*m.x270 + 0.0033*m.x298 >= 0)

m.c300 = Constraint(expr= - 0.01*m.x208 + 0.005*m.x236 + 0.015*m.x271 + 0.0033*m.x299 >= 0)

m.c301 = Constraint(expr= - 0.01*m.x209 + 0.005*m.x237 + 0.015*m.x272 + 0.0033*m.x300 >= 0)

m.c302 = Constraint(expr= - 0.01*m.x210 + 0.005*m.x238 + 0.015*m.x273 + 0.0033*m.x301 >= 0)

m.c303 = Constraint(expr= - 0.01*m.x211 + 0.005*m.x239 + 0.015*m.x274 + 0.0033*m.x302 >= 0)

m.c304 = Constraint(expr= - 0.01*m.x212 + 0.005*m.x240 + 0.015*m.x275 + 0.0033*m.x303 >= 0)

m.c305 = Constraint(expr=   m.b19 + m.b79 <= 1)

m.c306 = Constraint(expr=   m.b20 + m.b80 <= 1)

m.c307 = Constraint(expr=   m.b21 + m.b81 <= 1)

m.c308 = Constraint(expr=   m.b22 + m.b82 <= 1)

m.c309 = Constraint(expr=   m.b23 + m.b83 <= 1)

m.c310 = Constraint(expr=   m.b24 + m.b84 <= 1)

m.c311 = Constraint(expr=   m.b25 + m.b79 <= 1)

m.c312 = Constraint(expr=   m.b26 + m.b80 <= 1)

m.c313 = Constraint(expr=   m.b27 + m.b81 <= 1)

m.c314 = Constraint(expr=   m.b28 + m.b82 <= 1)

m.c315 = Constraint(expr=   m.b29 + m.b83 <= 1)

m.c316 = Constraint(expr=   m.b30 + m.b84 <= 1)

m.c317 = Constraint(expr=   m.b31 + m.b85 + m.b91 <= 1)

m.c318 = Constraint(expr=   m.b32 + m.b86 + m.b92 <= 1)

m.c319 = Constraint(expr=   m.b33 + m.b87 + m.b93 <= 1)

m.c320 = Constraint(expr=   m.b34 + m.b88 + m.b94 <= 1)

m.c321 = Constraint(expr=   m.b35 + m.b89 + m.b95 <= 1)

m.c322 = Constraint(expr=   m.b36 + m.b90 + m.b96 <= 1)

m.c323 = Constraint(expr=   m.b37 + m.b85 + m.b91 <= 1)

m.c324 = Constraint(expr=   m.b38 + m.b86 + m.b92 <= 1)

m.c325 = Constraint(expr=   m.b39 + m.b87 + m.b93 <= 1)

m.c326 = Constraint(expr=   m.b40 + m.b88 + m.b94 <= 1)

m.c327 = Constraint(expr=   m.b41 + m.b89 + m.b95 <= 1)

m.c328 = Constraint(expr=   m.b42 + m.b90 + m.b96 <= 1)

m.c329 = Constraint(expr=   m.b49 + m.b85 + m.b91 <= 1)

m.c330 = Constraint(expr=   m.b50 + m.b86 + m.b92 <= 1)

m.c331 = Constraint(expr=   m.b51 + m.b87 + m.b93 <= 1)

m.c332 = Constraint(expr=   m.b52 + m.b88 + m.b94 <= 1)

m.c333 = Constraint(expr=   m.b53 + m.b89 + m.b95 <= 1)

m.c334 = Constraint(expr=   m.b54 + m.b90 + m.b96 <= 1)

m.c335 = Constraint(expr=   m.b43 + m.b97 + m.b103 <= 1)

m.c336 = Constraint(expr=   m.b44 + m.b98 + m.b104 <= 1)

m.c337 = Constraint(expr=   m.b45 + m.b99 + m.b105 <= 1)

m.c338 = Constraint(expr=   m.b46 + m.b100 + m.b106 <= 1)

m.c339 = Constraint(expr=   m.b47 + m.b101 + m.b107 <= 1)

m.c340 = Constraint(expr=   m.b48 + m.b102 + m.b108 <= 1)

m.c341 = Constraint(expr=   m.b55 + m.b97 + m.b103 <= 1)

m.c342 = Constraint(expr=   m.b56 + m.b98 + m.b104 <= 1)

m.c343 = Constraint(expr=   m.b57 + m.b99 + m.b105 <= 1)

m.c344 = Constraint(expr=   m.b58 + m.b100 + m.b106 <= 1)

m.c345 = Constraint(expr=   m.b59 + m.b101 + m.b107 <= 1)

m.c346 = Constraint(expr=   m.b60 + m.b102 + m.b108 <= 1)

m.c347 = Constraint(expr=   m.b61 + m.b97 + m.b103 <= 1)

m.c348 = Constraint(expr=   m.b62 + m.b98 + m.b104 <= 1)

m.c349 = Constraint(expr=   m.b63 + m.b99 + m.b105 <= 1)

m.c350 = Constraint(expr=   m.b64 + m.b100 + m.b106 <= 1)

m.c351 = Constraint(expr=   m.b65 + m.b101 + m.b107 <= 1)

m.c352 = Constraint(expr=   m.b66 + m.b102 + m.b108 <= 1)

m.c353 = Constraint(expr=   m.x163 == 0)

m.c354 = Constraint(expr=   m.x191 == 0)

m.c355 = Constraint(expr=   m.x219 == 0)

m.c356 = Constraint(expr=   m.x322 + m.x323 + m.x324 + m.x325 + m.x326 + m.x327 + m.x430 + m.x431 + m.x432 + m.x433
                          + m.x434 + m.x435 + m.x472 + m.x473 + m.x474 + m.x475 + m.x476 + m.x477 == 600)

m.c357 = Constraint(expr=   m.x328 + m.x329 + m.x330 + m.x331 + m.x332 + m.x333 + m.x334 + m.x335 + m.x336 + m.x337
                          + m.x338 + m.x339 + m.x358 + m.x359 + m.x360 + m.x361 + m.x362 + m.x363 + m.x364 + m.x365
                          + m.x366 + m.x367 + m.x368 + m.x369 + m.x400 + m.x401 + m.x402 + m.x403 + m.x404 + m.x405
                          + m.x406 + m.x407 + m.x408 + m.x409 + m.x410 + m.x411 + m.x478 + m.x479 + m.x480 + m.x481
                          + m.x482 + m.x483 + m.x484 + m.x485 + m.x486 + m.x487 + m.x488 + m.x489 == 600)

m.c358 = Constraint(expr=   m.x370 + m.x371 + m.x372 + m.x373 + m.x374 + m.x375 + m.x376 + m.x377 + m.x378 + m.x379
                          + m.x380 + m.x381 + m.x412 + m.x413 + m.x414 + m.x415 + m.x416 + m.x417 + m.x418 + m.x419
                          + m.x420 + m.x421 + m.x422 + m.x423 + m.x454 + m.x455 + m.x456 + m.x457 + m.x458 + m.x459
                          + m.x460 + m.x461 + m.x462 + m.x463 + m.x464 + m.x465 + m.x490 + m.x491 + m.x492 + m.x493
                          + m.x494 + m.x495 + m.x496 + m.x497 + m.x498 + m.x499 + m.x500 + m.x501 == 600)

m.c359 = Constraint(expr=   m.x466 + m.x467 + m.x468 + m.x469 + m.x470 + m.x471 == 600)

m.c360 = Constraint(expr=   m.b115 + m.b116 + m.b118 + m.b121 == 1)

m.c361 = Constraint(expr=   m.b117 + m.b119 + m.b122 + m.b124 == 1)

m.c362 = Constraint(expr=   m.b120 + m.b123 + m.b125 + m.b126 == 1)

m.c363 = Constraint(expr=   m.b127 + m.b128 + m.b130 + m.b133 == 1)

m.c364 = Constraint(expr=   m.b129 + m.b131 + m.b134 + m.b136 == 1)

m.c365 = Constraint(expr=   m.b132 + m.b135 + m.b137 + m.b138 == 1)

m.c366 = Constraint(expr=   m.b1 + m.b7 + m.b13 <= 1)

m.c367 = Constraint(expr=   m.b2 + m.b8 + m.b14 <= 1)

m.c368 = Constraint(expr=   m.b3 + m.b9 + m.b15 <= 1)

m.c369 = Constraint(expr=   m.b4 + m.b10 + m.b16 <= 1)

m.c370 = Constraint(expr=   m.b5 + m.b11 + m.b17 <= 1)

m.c371 = Constraint(expr=   m.b6 + m.b12 + m.b18 <= 1)

m.c372 = Constraint(expr=   m.b79 + m.b85 == 1)

m.c373 = Constraint(expr=   m.b80 + m.b86 == 1)

m.c374 = Constraint(expr=   m.b81 + m.b87 == 1)

m.c375 = Constraint(expr=   m.b82 + m.b88 == 1)

m.c376 = Constraint(expr=   m.b83 + m.b89 == 1)

m.c377 = Constraint(expr=   m.b84 + m.b90 == 1)

m.c378 = Constraint(expr=   m.b91 + m.b97 == 1)

m.c379 = Constraint(expr=   m.b92 + m.b98 == 1)

m.c380 = Constraint(expr=   m.b93 + m.b99 == 1)

m.c381 = Constraint(expr=   m.b94 + m.b100 == 1)

m.c382 = Constraint(expr=   m.b95 + m.b101 == 1)

m.c383 = Constraint(expr=   m.b96 + m.b102 == 1)

m.c384 = Constraint(expr=   m.b103 + m.b109 == 1)

m.c385 = Constraint(expr=   m.b104 + m.b110 == 1)

m.c386 = Constraint(expr=   m.b105 + m.b111 == 1)

m.c387 = Constraint(expr=   m.b106 + m.b112 == 1)

m.c388 = Constraint(expr=   m.b107 + m.b113 == 1)

m.c389 = Constraint(expr=   m.b108 + m.b114 == 1)

m.c390 = Constraint(expr=   m.b1 - m.b115 <= 0)

m.c391 = Constraint(expr=   m.b2 - m.b115 - m.b116 <= 0)

m.c392 = Constraint(expr=   m.b3 - m.b115 - m.b116 - m.b118 <= 0)

m.c393 = Constraint(expr=   m.b4 - m.b115 - m.b116 - m.b118 - m.b121 <= 0)

m.c394 = Constraint(expr=   m.b5 - m.b115 - m.b116 - m.b118 - m.b121 <= 0)

m.c395 = Constraint(expr=   m.b6 - m.b115 - m.b116 - m.b118 - m.b121 <= 0)

m.c396 = Constraint(expr=   m.b7 <= 0)

m.c397 = Constraint(expr=   m.b8 - m.b117 <= 0)

m.c398 = Constraint(expr=   m.b9 - m.b117 - m.b119 <= 0)

m.c399 = Constraint(expr=   m.b10 - m.b117 - m.b119 - m.b122 <= 0)

m.c400 = Constraint(expr=   m.b11 - m.b117 - m.b119 - m.b122 - m.b124 <= 0)

m.c401 = Constraint(expr=   m.b12 - m.b117 - m.b119 - m.b122 - m.b124 <= 0)

m.c402 = Constraint(expr=   m.b13 <= 0)

m.c403 = Constraint(expr=   m.b14 <= 0)

m.c404 = Constraint(expr=   m.b15 - m.b120 <= 0)

m.c405 = Constraint(expr=   m.b16 - m.b120 - m.b123 <= 0)

m.c406 = Constraint(expr=   m.b17 - m.b120 - m.b123 - m.b125 <= 0)

m.c407 = Constraint(expr=   m.b18 - m.b120 - m.b123 - m.b125 - m.b126 <= 0)

m.c408 = Constraint(expr=   m.b1 - m.b127 - m.b128 - m.b130 - m.b133 <= 0)

m.c409 = Constraint(expr=   m.b2 - m.b128 - m.b130 - m.b133 <= 0)

m.c410 = Constraint(expr=   m.b3 - m.b130 - m.b133 <= 0)

m.c411 = Constraint(expr=   m.b4 - m.b133 <= 0)

m.c412 = Constraint(expr=   m.b5 <= 0)

m.c413 = Constraint(expr=   m.b6 <= 0)

m.c414 = Constraint(expr=   m.b7 - m.b129 - m.b131 - m.b134 - m.b136 <= 0)

m.c415 = Constraint(expr=   m.b8 - m.b129 - m.b131 - m.b134 - m.b136 <= 0)

m.c416 = Constraint(expr=   m.b9 - m.b131 - m.b134 - m.b136 <= 0)

m.c417 = Constraint(expr=   m.b10 - m.b134 - m.b136 <= 0)

m.c418 = Constraint(expr=   m.b11 - m.b136 <= 0)

m.c419 = Constraint(expr=   m.b12 <= 0)

m.c420 = Constraint(expr=   m.b13 - m.b132 - m.b135 - m.b137 - m.b138 <= 0)

m.c421 = Constraint(expr=   m.b14 - m.b132 - m.b135 - m.b137 - m.b138 <= 0)

m.c422 = Constraint(expr=   m.b15 - m.b132 - m.b135 - m.b137 - m.b138 <= 0)

m.c423 = Constraint(expr=   m.b16 - m.b135 - m.b137 - m.b138 <= 0)

m.c424 = Constraint(expr=   m.b17 - m.b137 - m.b138 <= 0)

m.c425 = Constraint(expr=   m.b18 - m.b138 <= 0)

m.c426 = Constraint(expr= - m.b79 - m.b86 + m.x139 >= -1)

m.c427 = Constraint(expr= - m.b80 - m.b87 + m.x140 >= -1)

m.c428 = Constraint(expr= - m.b81 - m.b88 + m.x141 >= -1)

m.c429 = Constraint(expr= - m.b82 - m.b89 + m.x142 >= -1)

m.c430 = Constraint(expr= - m.b83 - m.b90 + m.x143 >= -1)

m.c431 = Constraint(expr= - m.b91 - m.b98 + m.x144 >= -1)

m.c432 = Constraint(expr= - m.b92 - m.b99 + m.x145 >= -1)

m.c433 = Constraint(expr= - m.b93 - m.b100 + m.x146 >= -1)

m.c434 = Constraint(expr= - m.b94 - m.b101 + m.x147 >= -1)

m.c435 = Constraint(expr= - m.b95 - m.b102 + m.x148 >= -1)

m.c436 = Constraint(expr= - m.b103 - m.b110 + m.x149 >= -1)

m.c437 = Constraint(expr= - m.b104 - m.b111 + m.x150 >= -1)

m.c438 = Constraint(expr= - m.b105 - m.b112 + m.x151 >= -1)

m.c439 = Constraint(expr= - m.b106 - m.b113 + m.x152 >= -1)

m.c440 = Constraint(expr= - m.b107 - m.b114 + m.x153 >= -1)

m.c441 = Constraint(expr= - m.b80 - m.b85 + m.x139 >= -1)

m.c442 = Constraint(expr= - m.b81 - m.b86 + m.x140 >= -1)

m.c443 = Constraint(expr= - m.b82 - m.b87 + m.x141 >= -1)

m.c444 = Constraint(expr= - m.b83 - m.b88 + m.x142 >= -1)

m.c445 = Constraint(expr= - m.b84 - m.b89 + m.x143 >= -1)

m.c446 = Constraint(expr= - m.b92 - m.b97 + m.x144 >= -1)

m.c447 = Constraint(expr= - m.b93 - m.b98 + m.x145 >= -1)

m.c448 = Constraint(expr= - m.b94 - m.b99 + m.x146 >= -1)

m.c449 = Constraint(expr= - m.b95 - m.b100 + m.x147 >= -1)

m.c450 = Constraint(expr= - m.b96 - m.b101 + m.x148 >= -1)

m.c451 = Constraint(expr= - m.b104 - m.b109 + m.x149 >= -1)

m.c452 = Constraint(expr= - m.b105 - m.b110 + m.x150 >= -1)

m.c453 = Constraint(expr= - m.b106 - m.b111 + m.x151 >= -1)

m.c454 = Constraint(expr= - m.b107 - m.b112 + m.x152 >= -1)

m.c455 = Constraint(expr= - m.b108 - m.b113 + m.x153 >= -1)

m.c456 = Constraint(expr=   m.x139 + m.x140 + m.x141 + m.x142 + m.x143 - m.x154 == -1)

m.c457 = Constraint(expr=   m.x144 + m.x145 + m.x146 + m.x147 + m.x148 - m.x155 == -1)

m.c458 = Constraint(expr=   m.x149 + m.x150 + m.x151 + m.x152 + m.x153 - m.x156 == -1)

m.c459 = Constraint(expr= - 600*m.b1 + m.x304 <= 0)

m.c460 = Constraint(expr= - 600*m.b2 + m.x305 <= 0)

m.c461 = Constraint(expr= - 600*m.b3 + m.x306 <= 0)

m.c462 = Constraint(expr= - 600*m.b4 + m.x307 <= 0)

m.c463 = Constraint(expr= - 600*m.b5 + m.x308 <= 0)

m.c464 = Constraint(expr= - 600*m.b6 + m.x309 <= 0)

m.c465 = Constraint(expr= - 600*m.b7 + m.x340 <= 0)

m.c466 = Constraint(expr= - 600*m.b8 + m.x341 <= 0)

m.c467 = Constraint(expr= - 600*m.b9 + m.x342 <= 0)

m.c468 = Constraint(expr= - 600*m.b10 + m.x343 <= 0)

m.c469 = Constraint(expr= - 600*m.b11 + m.x344 <= 0)

m.c470 = Constraint(expr= - 600*m.b12 + m.x345 <= 0)

m.c471 = Constraint(expr= - 600*m.b13 + m.x382 <= 0)

m.c472 = Constraint(expr= - 600*m.b14 + m.x383 <= 0)

m.c473 = Constraint(expr= - 600*m.b15 + m.x384 <= 0)

m.c474 = Constraint(expr= - 600*m.b16 + m.x385 <= 0)

m.c475 = Constraint(expr= - 600*m.b17 + m.x386 <= 0)

m.c476 = Constraint(expr= - 600*m.b18 + m.x387 <= 0)

m.c477 = Constraint(expr= - 900*m.b19 + m.x424 <= 0)

m.c478 = Constraint(expr= - 900*m.b20 + m.x425 <= 0)

m.c479 = Constraint(expr= - 900*m.b21 + m.x426 <= 0)

m.c480 = Constraint(expr= - 900*m.b22 + m.x427 <= 0)

m.c481 = Constraint(expr= - 900*m.b23 + m.x428 <= 0)

m.c482 = Constraint(expr= - 900*m.b24 + m.x429 <= 0)

m.c483 = Constraint(expr= - 1100*m.b25 + m.x310 <= 0)

m.c484 = Constraint(expr= - 1100*m.b26 + m.x311 <= 0)

m.c485 = Constraint(expr= - 1100*m.b27 + m.x312 <= 0)

m.c486 = Constraint(expr= - 1100*m.b28 + m.x313 <= 0)

m.c487 = Constraint(expr= - 1100*m.b29 + m.x314 <= 0)

m.c488 = Constraint(expr= - 1100*m.b30 + m.x315 <= 0)

m.c489 = Constraint(expr= - 1100*m.b31 + m.x316 <= 0)

m.c490 = Constraint(expr= - 1100*m.b32 + m.x317 <= 0)

m.c491 = Constraint(expr= - 1100*m.b33 + m.x318 <= 0)

m.c492 = Constraint(expr= - 1100*m.b34 + m.x319 <= 0)

m.c493 = Constraint(expr= - 1100*m.b35 + m.x320 <= 0)

m.c494 = Constraint(expr= - 1100*m.b36 + m.x321 <= 0)

m.c495 = Constraint(expr= - 1100*m.b37 + m.x346 <= 0)

m.c496 = Constraint(expr= - 1100*m.b38 + m.x347 <= 0)

m.c497 = Constraint(expr= - 1100*m.b39 + m.x348 <= 0)

m.c498 = Constraint(expr= - 1100*m.b40 + m.x349 <= 0)

m.c499 = Constraint(expr= - 1100*m.b41 + m.x350 <= 0)

m.c500 = Constraint(expr= - 1100*m.b42 + m.x351 <= 0)

m.c501 = Constraint(expr= - 1100*m.b43 + m.x352 <= 0)

m.c502 = Constraint(expr= - 1100*m.b44 + m.x353 <= 0)

m.c503 = Constraint(expr= - 1100*m.b45 + m.x354 <= 0)

m.c504 = Constraint(expr= - 1100*m.b46 + m.x355 <= 0)

m.c505 = Constraint(expr= - 1100*m.b47 + m.x356 <= 0)

m.c506 = Constraint(expr= - 1100*m.b48 + m.x357 <= 0)

m.c507 = Constraint(expr= - 1100*m.b49 + m.x388 <= 0)

m.c508 = Constraint(expr= - 1100*m.b50 + m.x389 <= 0)

m.c509 = Constraint(expr= - 1100*m.b51 + m.x390 <= 0)

m.c510 = Constraint(expr= - 1100*m.b52 + m.x391 <= 0)

m.c511 = Constraint(expr= - 1100*m.b53 + m.x392 <= 0)

m.c512 = Constraint(expr= - 1100*m.b54 + m.x393 <= 0)

m.c513 = Constraint(expr= - 1100*m.b55 + m.x394 <= 0)

m.c514 = Constraint(expr= - 1100*m.b56 + m.x395 <= 0)

m.c515 = Constraint(expr= - 1100*m.b57 + m.x396 <= 0)

m.c516 = Constraint(expr= - 1100*m.b58 + m.x397 <= 0)

m.c517 = Constraint(expr= - 1100*m.b59 + m.x398 <= 0)

m.c518 = Constraint(expr= - 1100*m.b60 + m.x399 <= 0)

m.c519 = Constraint(expr= - 900*m.b61 + m.x436 <= 0)

m.c520 = Constraint(expr= - 900*m.b62 + m.x437 <= 0)

m.c521 = Constraint(expr= - 900*m.b63 + m.x438 <= 0)

m.c522 = Constraint(expr= - 900*m.b64 + m.x439 <= 0)

m.c523 = Constraint(expr= - 900*m.b65 + m.x440 <= 0)

m.c524 = Constraint(expr= - 900*m.b66 + m.x441 <= 0)

m.c525 = Constraint(expr= - 900*m.b67 + m.x442 <= 0)

m.c526 = Constraint(expr= - 900*m.b68 + m.x443 <= 0)

m.c527 = Constraint(expr= - 900*m.b69 + m.x444 <= 0)

m.c528 = Constraint(expr= - 900*m.b70 + m.x445 <= 0)

m.c529 = Constraint(expr= - 900*m.b71 + m.x446 <= 0)

m.c530 = Constraint(expr= - 900*m.b72 + m.x447 <= 0)

m.c531 = Constraint(expr= - 900*m.b73 + m.x448 <= 0)

m.c532 = Constraint(expr= - 900*m.b74 + m.x449 <= 0)

m.c533 = Constraint(expr= - 900*m.b75 + m.x450 <= 0)

m.c534 = Constraint(expr= - 900*m.b76 + m.x451 <= 0)

m.c535 = Constraint(expr= - 900*m.b77 + m.x452 <= 0)

m.c536 = Constraint(expr= - 900*m.b78 + m.x453 <= 0)

m.c537 = Constraint(expr= - 800*m.b79 + m.x322 + m.x430 + m.x472 <= 0)

m.c538 = Constraint(expr= - 800*m.b80 + m.x323 + m.x431 + m.x473 <= 0)

m.c539 = Constraint(expr= - 800*m.b81 + m.x324 + m.x432 + m.x474 <= 0)

m.c540 = Constraint(expr= - 800*m.b82 + m.x325 + m.x433 + m.x475 <= 0)

m.c541 = Constraint(expr= - 800*m.b83 + m.x326 + m.x434 + m.x476 <= 0)

m.c542 = Constraint(expr= - 800*m.b84 + m.x327 + m.x435 + m.x477 <= 0)

m.c543 = Constraint(expr= - 800*m.b85 + m.x328 + m.x358 + m.x400 + m.x478 <= 0)

m.c544 = Constraint(expr= - 800*m.b86 + m.x329 + m.x359 + m.x401 + m.x479 <= 0)

m.c545 = Constraint(expr= - 800*m.b87 + m.x330 + m.x360 + m.x402 + m.x480 <= 0)

m.c546 = Constraint(expr= - 800*m.b88 + m.x331 + m.x361 + m.x403 + m.x481 <= 0)

m.c547 = Constraint(expr= - 800*m.b89 + m.x332 + m.x362 + m.x404 + m.x482 <= 0)

m.c548 = Constraint(expr= - 800*m.b90 + m.x333 + m.x363 + m.x405 + m.x483 <= 0)

m.c549 = Constraint(expr= - 800*m.b91 + m.x334 + m.x364 + m.x406 + m.x484 <= 0)

m.c550 = Constraint(expr= - 800*m.b92 + m.x335 + m.x365 + m.x407 + m.x485 <= 0)

m.c551 = Constraint(expr= - 800*m.b93 + m.x336 + m.x366 + m.x408 + m.x486 <= 0)

m.c552 = Constraint(expr= - 800*m.b94 + m.x337 + m.x367 + m.x409 + m.x487 <= 0)

m.c553 = Constraint(expr= - 800*m.b95 + m.x338 + m.x368 + m.x410 + m.x488 <= 0)

m.c554 = Constraint(expr= - 800*m.b96 + m.x339 + m.x369 + m.x411 + m.x489 <= 0)

m.c555 = Constraint(expr= - 800*m.b97 + m.x370 + m.x412 + m.x454 + m.x490 <= 0)

m.c556 = Constraint(expr= - 800*m.b98 + m.x371 + m.x413 + m.x455 + m.x491 <= 0)

m.c557 = Constraint(expr= - 800*m.b99 + m.x372 + m.x414 + m.x456 + m.x492 <= 0)

m.c558 = Constraint(expr= - 800*m.b100 + m.x373 + m.x415 + m.x457 + m.x493 <= 0)

m.c559 = Constraint(expr= - 800*m.b101 + m.x374 + m.x416 + m.x458 + m.x494 <= 0)

m.c560 = Constraint(expr= - 800*m.b102 + m.x375 + m.x417 + m.x459 + m.x495 <= 0)

m.c561 = Constraint(expr= - 800*m.b103 + m.x376 + m.x418 + m.x460 + m.x496 <= 0)

m.c562 = Constraint(expr= - 800*m.b104 + m.x377 + m.x419 + m.x461 + m.x497 <= 0)

m.c563 = Constraint(expr= - 800*m.b105 + m.x378 + m.x420 + m.x462 + m.x498 <= 0)

m.c564 = Constraint(expr= - 800*m.b106 + m.x379 + m.x421 + m.x463 + m.x499 <= 0)

m.c565 = Constraint(expr= - 800*m.b107 + m.x380 + m.x422 + m.x464 + m.x500 <= 0)

m.c566 = Constraint(expr= - 800*m.b108 + m.x381 + m.x423 + m.x465 + m.x501 <= 0)

m.c567 = Constraint(expr= - 800*m.b109 + m.x466 <= 0)

m.c568 = Constraint(expr= - 800*m.b110 + m.x467 <= 0)

m.c569 = Constraint(expr= - 800*m.b111 + m.x468 <= 0)

m.c570 = Constraint(expr= - 800*m.b112 + m.x469 <= 0)

m.c571 = Constraint(expr= - 800*m.b113 + m.x470 <= 0)

m.c572 = Constraint(expr= - 800*m.b114 + m.x471 <= 0)

m.c573 = Constraint(expr= - m.b1 + m.x304 >= 0)

m.c574 = Constraint(expr= - m.b2 + m.x305 >= 0)

m.c575 = Constraint(expr= - m.b3 + m.x306 >= 0)

m.c576 = Constraint(expr= - m.b4 + m.x307 >= 0)

m.c577 = Constraint(expr= - m.b5 + m.x308 >= 0)

m.c578 = Constraint(expr= - m.b6 + m.x309 >= 0)

m.c579 = Constraint(expr= - m.b7 + m.x340 >= 0)

m.c580 = Constraint(expr= - m.b8 + m.x341 >= 0)

m.c581 = Constraint(expr= - m.b9 + m.x342 >= 0)

m.c582 = Constraint(expr= - m.b10 + m.x343 >= 0)

m.c583 = Constraint(expr= - m.b11 + m.x344 >= 0)

m.c584 = Constraint(expr= - m.b12 + m.x345 >= 0)

m.c585 = Constraint(expr= - m.b13 + m.x382 >= 0)

m.c586 = Constraint(expr= - m.b14 + m.x383 >= 0)

m.c587 = Constraint(expr= - m.b15 + m.x384 >= 0)

m.c588 = Constraint(expr= - m.b16 + m.x385 >= 0)

m.c589 = Constraint(expr= - m.b17 + m.x386 >= 0)

m.c590 = Constraint(expr= - m.b18 + m.x387 >= 0)

m.c591 = Constraint(expr= - m.b19 + m.x424 >= 0)

m.c592 = Constraint(expr= - m.b20 + m.x425 >= 0)

m.c593 = Constraint(expr= - m.b21 + m.x426 >= 0)

m.c594 = Constraint(expr= - m.b22 + m.x427 >= 0)

m.c595 = Constraint(expr= - m.b23 + m.x428 >= 0)

m.c596 = Constraint(expr= - m.b24 + m.x429 >= 0)

m.c597 = Constraint(expr= - m.b25 + m.x310 >= 0)

m.c598 = Constraint(expr= - m.b26 + m.x311 >= 0)

m.c599 = Constraint(expr= - m.b27 + m.x312 >= 0)

m.c600 = Constraint(expr= - m.b28 + m.x313 >= 0)

m.c601 = Constraint(expr= - m.b29 + m.x314 >= 0)

m.c602 = Constraint(expr= - m.b30 + m.x315 >= 0)

m.c603 = Constraint(expr= - m.b31 + m.x316 >= 0)

m.c604 = Constraint(expr= - m.b32 + m.x317 >= 0)

m.c605 = Constraint(expr= - m.b33 + m.x318 >= 0)

m.c606 = Constraint(expr= - m.b34 + m.x319 >= 0)

m.c607 = Constraint(expr= - m.b35 + m.x320 >= 0)

m.c608 = Constraint(expr= - m.b36 + m.x321 >= 0)

m.c609 = Constraint(expr= - m.b37 + m.x346 >= 0)

m.c610 = Constraint(expr= - m.b38 + m.x347 >= 0)

m.c611 = Constraint(expr= - m.b39 + m.x348 >= 0)

m.c612 = Constraint(expr= - m.b40 + m.x349 >= 0)

m.c613 = Constraint(expr= - m.b41 + m.x350 >= 0)

m.c614 = Constraint(expr= - m.b42 + m.x351 >= 0)

m.c615 = Constraint(expr= - m.b43 + m.x352 >= 0)

m.c616 = Constraint(expr= - m.b44 + m.x353 >= 0)

m.c617 = Constraint(expr= - m.b45 + m.x354 >= 0)

m.c618 = Constraint(expr= - m.b46 + m.x355 >= 0)

m.c619 = Constraint(expr= - m.b47 + m.x356 >= 0)

m.c620 = Constraint(expr= - m.b48 + m.x357 >= 0)

m.c621 = Constraint(expr= - m.b49 + m.x388 >= 0)

m.c622 = Constraint(expr= - m.b50 + m.x389 >= 0)

m.c623 = Constraint(expr= - m.b51 + m.x390 >= 0)

m.c624 = Constraint(expr= - m.b52 + m.x391 >= 0)

m.c625 = Constraint(expr= - m.b53 + m.x392 >= 0)

m.c626 = Constraint(expr= - m.b54 + m.x393 >= 0)

m.c627 = Constraint(expr= - m.b55 + m.x394 >= 0)

m.c628 = Constraint(expr= - m.b56 + m.x395 >= 0)

m.c629 = Constraint(expr= - m.b57 + m.x396 >= 0)

m.c630 = Constraint(expr= - m.b58 + m.x397 >= 0)

m.c631 = Constraint(expr= - m.b59 + m.x398 >= 0)

m.c632 = Constraint(expr= - m.b60 + m.x399 >= 0)

m.c633 = Constraint(expr= - m.b61 + m.x436 >= 0)

m.c634 = Constraint(expr= - m.b62 + m.x437 >= 0)

m.c635 = Constraint(expr= - m.b63 + m.x438 >= 0)

m.c636 = Constraint(expr= - m.b64 + m.x439 >= 0)

m.c637 = Constraint(expr= - m.b65 + m.x440 >= 0)

m.c638 = Constraint(expr= - m.b66 + m.x441 >= 0)

m.c639 = Constraint(expr= - m.b67 + m.x442 >= 0)

m.c640 = Constraint(expr= - m.b68 + m.x443 >= 0)

m.c641 = Constraint(expr= - m.b69 + m.x444 >= 0)

m.c642 = Constraint(expr= - m.b70 + m.x445 >= 0)

m.c643 = Constraint(expr= - m.b71 + m.x446 >= 0)

m.c644 = Constraint(expr= - m.b72 + m.x447 >= 0)

m.c645 = Constraint(expr= - m.b73 + m.x448 >= 0)

m.c646 = Constraint(expr= - m.b74 + m.x449 >= 0)

m.c647 = Constraint(expr= - m.b75 + m.x450 >= 0)

m.c648 = Constraint(expr= - m.b76 + m.x451 >= 0)

m.c649 = Constraint(expr= - m.b77 + m.x452 >= 0)

m.c650 = Constraint(expr= - m.b78 + m.x453 >= 0)

m.c651 = Constraint(expr= - m.b79 + m.x322 + m.x430 + m.x472 >= 0)

m.c652 = Constraint(expr= - m.b80 + m.x323 + m.x431 + m.x473 >= 0)

m.c653 = Constraint(expr= - m.b81 + m.x324 + m.x432 + m.x474 >= 0)

m.c654 = Constraint(expr= - m.b82 + m.x325 + m.x433 + m.x475 >= 0)

m.c655 = Constraint(expr= - m.b83 + m.x326 + m.x434 + m.x476 >= 0)

m.c656 = Constraint(expr= - m.b84 + m.x327 + m.x435 + m.x477 >= 0)

m.c657 = Constraint(expr= - m.b85 + m.x328 + m.x358 + m.x400 + m.x478 >= 0)

m.c658 = Constraint(expr= - m.b86 + m.x329 + m.x359 + m.x401 + m.x479 >= 0)

m.c659 = Constraint(expr= - m.b87 + m.x330 + m.x360 + m.x402 + m.x480 >= 0)

m.c660 = Constraint(expr= - m.b88 + m.x331 + m.x361 + m.x403 + m.x481 >= 0)

m.c661 = Constraint(expr= - m.b89 + m.x332 + m.x362 + m.x404 + m.x482 >= 0)

m.c662 = Constraint(expr= - m.b90 + m.x333 + m.x363 + m.x405 + m.x483 >= 0)

m.c663 = Constraint(expr= - m.b91 + m.x334 + m.x364 + m.x406 + m.x484 >= 0)

m.c664 = Constraint(expr= - m.b92 + m.x335 + m.x365 + m.x407 + m.x485 >= 0)

m.c665 = Constraint(expr= - m.b93 + m.x336 + m.x366 + m.x408 + m.x486 >= 0)

m.c666 = Constraint(expr= - m.b94 + m.x337 + m.x367 + m.x409 + m.x487 >= 0)

m.c667 = Constraint(expr= - m.b95 + m.x338 + m.x368 + m.x410 + m.x488 >= 0)

m.c668 = Constraint(expr= - m.b96 + m.x339 + m.x369 + m.x411 + m.x489 >= 0)

m.c669 = Constraint(expr= - m.b97 + m.x370 + m.x412 + m.x454 + m.x490 >= 0)

m.c670 = Constraint(expr= - m.b98 + m.x371 + m.x413 + m.x455 + m.x491 >= 0)

m.c671 = Constraint(expr= - m.b99 + m.x372 + m.x414 + m.x456 + m.x492 >= 0)

m.c672 = Constraint(expr= - m.b100 + m.x373 + m.x415 + m.x457 + m.x493 >= 0)

m.c673 = Constraint(expr= - m.b101 + m.x374 + m.x416 + m.x458 + m.x494 >= 0)

m.c674 = Constraint(expr= - m.b102 + m.x375 + m.x417 + m.x459 + m.x495 >= 0)

m.c675 = Constraint(expr= - m.b103 + m.x376 + m.x418 + m.x460 + m.x496 >= 0)

m.c676 = Constraint(expr= - m.b104 + m.x377 + m.x419 + m.x461 + m.x497 >= 0)

m.c677 = Constraint(expr= - m.b105 + m.x378 + m.x420 + m.x462 + m.x498 >= 0)

m.c678 = Constraint(expr= - m.b106 + m.x379 + m.x421 + m.x463 + m.x499 >= 0)

m.c679 = Constraint(expr= - m.b107 + m.x380 + m.x422 + m.x464 + m.x500 >= 0)

m.c680 = Constraint(expr= - m.b108 + m.x381 + m.x423 + m.x465 + m.x501 >= 0)

m.c681 = Constraint(expr= - m.b109 + m.x466 >= 0)

m.c682 = Constraint(expr= - m.b110 + m.x467 >= 0)

m.c683 = Constraint(expr= - m.b111 + m.x468 >= 0)

m.c684 = Constraint(expr= - m.b112 + m.x469 >= 0)

m.c685 = Constraint(expr= - m.b113 + m.x470 >= 0)

m.c686 = Constraint(expr= - m.b114 + m.x471 >= 0)

m.c687 = Constraint(expr= - 0.002*m.x304 - m.x527 + m.x528 >= 0)

m.c688 = Constraint(expr= - 0.002*m.x305 - m.x528 + m.x529 >= 0)

m.c689 = Constraint(expr= - 0.002*m.x306 - m.x529 + m.x530 >= 0)

m.c690 = Constraint(expr= - 0.002*m.x307 - m.x530 + m.x531 >= 0)

m.c691 = Constraint(expr= - 0.002*m.x308 - m.x531 + m.x532 >= 0)

m.c692 = Constraint(expr= - 0.002*m.x309 - m.x532 + m.x533 >= 0)

m.c693 = Constraint(expr= - 0.002*m.x340 - m.x527 + m.x528 >= 0)

m.c694 = Constraint(expr= - 0.002*m.x341 - m.x528 + m.x529 >= 0)

m.c695 = Constraint(expr= - 0.002*m.x342 - m.x529 + m.x530 >= 0)

m.c696 = Constraint(expr= - 0.002*m.x343 - m.x530 + m.x531 >= 0)

m.c697 = Constraint(expr= - 0.002*m.x344 - m.x531 + m.x532 >= 0)

m.c698 = Constraint(expr= - 0.002*m.x345 - m.x532 + m.x533 >= 0)

m.c699 = Constraint(expr= - 0.002*m.x382 - m.x527 + m.x528 >= 0)

m.c700 = Constraint(expr= - 0.002*m.x383 - m.x528 + m.x529 >= 0)

m.c701 = Constraint(expr= - 0.002*m.x384 - m.x529 + m.x530 >= 0)

m.c702 = Constraint(expr= - 0.002*m.x385 - m.x530 + m.x531 >= 0)

m.c703 = Constraint(expr= - 0.002*m.x386 - m.x531 + m.x532 >= 0)

m.c704 = Constraint(expr= - 0.002*m.x387 - m.x532 + m.x533 >= 0)

m.c705 = Constraint(expr= - 0.002*m.x424 - m.x527 + m.x528 >= 0)

m.c706 = Constraint(expr= - 0.002*m.x425 - m.x528 + m.x529 >= 0)

m.c707 = Constraint(expr= - 0.002*m.x426 - m.x529 + m.x530 >= 0)

m.c708 = Constraint(expr= - 0.002*m.x427 - m.x530 + m.x531 >= 0)

m.c709 = Constraint(expr= - 0.002*m.x428 - m.x531 + m.x532 >= 0)

m.c710 = Constraint(expr= - 0.002*m.x429 - m.x532 + m.x533 >= 0)

m.c711 = Constraint(expr= - 0.002*m.x310 - m.x527 + m.x528 >= 0)

m.c712 = Constraint(expr= - 0.002*m.x311 - m.x528 + m.x529 >= 0)

m.c713 = Constraint(expr= - 0.002*m.x312 - m.x529 + m.x530 >= 0)

m.c714 = Constraint(expr= - 0.002*m.x313 - m.x530 + m.x531 >= 0)

m.c715 = Constraint(expr= - 0.002*m.x314 - m.x531 + m.x532 >= 0)

m.c716 = Constraint(expr= - 0.002*m.x315 - m.x532 + m.x533 >= 0)

m.c717 = Constraint(expr= - 0.002*m.x316 - m.x527 + m.x528 >= 0)

m.c718 = Constraint(expr= - 0.002*m.x317 - m.x528 + m.x529 >= 0)

m.c719 = Constraint(expr= - 0.002*m.x318 - m.x529 + m.x530 >= 0)

m.c720 = Constraint(expr= - 0.002*m.x319 - m.x530 + m.x531 >= 0)

m.c721 = Constraint(expr= - 0.002*m.x320 - m.x531 + m.x532 >= 0)

m.c722 = Constraint(expr= - 0.002*m.x321 - m.x532 + m.x533 >= 0)

m.c723 = Constraint(expr= - 0.002*m.x346 - m.x527 + m.x528 >= 0)

m.c724 = Constraint(expr= - 0.002*m.x347 - m.x528 + m.x529 >= 0)

m.c725 = Constraint(expr= - 0.002*m.x348 - m.x529 + m.x530 >= 0)

m.c726 = Constraint(expr= - 0.002*m.x349 - m.x530 + m.x531 >= 0)

m.c727 = Constraint(expr= - 0.002*m.x350 - m.x531 + m.x532 >= 0)

m.c728 = Constraint(expr= - 0.002*m.x351 - m.x532 + m.x533 >= 0)

m.c729 = Constraint(expr= - 0.002*m.x352 - m.x527 + m.x528 >= 0)

m.c730 = Constraint(expr= - 0.002*m.x353 - m.x528 + m.x529 >= 0)

m.c731 = Constraint(expr= - 0.002*m.x354 - m.x529 + m.x530 >= 0)

m.c732 = Constraint(expr= - 0.002*m.x355 - m.x530 + m.x531 >= 0)

m.c733 = Constraint(expr= - 0.002*m.x356 - m.x531 + m.x532 >= 0)

m.c734 = Constraint(expr= - 0.002*m.x357 - m.x532 + m.x533 >= 0)

m.c735 = Constraint(expr= - 0.002*m.x388 - m.x527 + m.x528 >= 0)

m.c736 = Constraint(expr= - 0.002*m.x389 - m.x528 + m.x529 >= 0)

m.c737 = Constraint(expr= - 0.002*m.x390 - m.x529 + m.x530 >= 0)

m.c738 = Constraint(expr= - 0.002*m.x391 - m.x530 + m.x531 >= 0)

m.c739 = Constraint(expr= - 0.002*m.x392 - m.x531 + m.x532 >= 0)

m.c740 = Constraint(expr= - 0.002*m.x393 - m.x532 + m.x533 >= 0)

m.c741 = Constraint(expr= - 0.002*m.x394 - m.x527 + m.x528 >= 0)

m.c742 = Constraint(expr= - 0.002*m.x395 - m.x528 + m.x529 >= 0)

m.c743 = Constraint(expr= - 0.002*m.x396 - m.x529 + m.x530 >= 0)

m.c744 = Constraint(expr= - 0.002*m.x397 - m.x530 + m.x531 >= 0)

m.c745 = Constraint(expr= - 0.002*m.x398 - m.x531 + m.x532 >= 0)

m.c746 = Constraint(expr= - 0.002*m.x399 - m.x532 + m.x533 >= 0)

m.c747 = Constraint(expr= - 0.002*m.x436 - m.x527 + m.x528 >= 0)

m.c748 = Constraint(expr= - 0.002*m.x437 - m.x528 + m.x529 >= 0)

m.c749 = Constraint(expr= - 0.002*m.x438 - m.x529 + m.x530 >= 0)

m.c750 = Constraint(expr= - 0.002*m.x439 - m.x530 + m.x531 >= 0)

m.c751 = Constraint(expr= - 0.002*m.x440 - m.x531 + m.x532 >= 0)

m.c752 = Constraint(expr= - 0.002*m.x441 - m.x532 + m.x533 >= 0)

m.c753 = Constraint(expr= - 0.002*m.x442 - m.x527 + m.x528 >= 0)

m.c754 = Constraint(expr= - 0.002*m.x443 - m.x528 + m.x529 >= 0)

m.c755 = Constraint(expr= - 0.002*m.x444 - m.x529 + m.x530 >= 0)

m.c756 = Constraint(expr= - 0.002*m.x445 - m.x530 + m.x531 >= 0)

m.c757 = Constraint(expr= - 0.002*m.x446 - m.x531 + m.x532 >= 0)

m.c758 = Constraint(expr= - 0.002*m.x447 - m.x532 + m.x533 >= 0)

m.c759 = Constraint(expr= - 0.002*m.x448 - m.x527 + m.x528 >= 0)

m.c760 = Constraint(expr= - 0.002*m.x449 - m.x528 + m.x529 >= 0)

m.c761 = Constraint(expr= - 0.002*m.x450 - m.x529 + m.x530 >= 0)

m.c762 = Constraint(expr= - 0.002*m.x451 - m.x530 + m.x531 >= 0)

m.c763 = Constraint(expr= - 0.002*m.x452 - m.x531 + m.x532 >= 0)

m.c764 = Constraint(expr= - 0.002*m.x453 - m.x532 + m.x533 >= 0)

m.c765 = Constraint(expr= - 0.002*m.x328 - 0.002*m.x334 - 0.002*m.x358 - 0.002*m.x364 - 0.002*m.x400 - 0.002*m.x406
                          - 0.002*m.x478 - 0.002*m.x484 - m.x527 + m.x528 >= 0)

m.c766 = Constraint(expr= - 0.002*m.x329 - 0.002*m.x335 - 0.002*m.x359 - 0.002*m.x365 - 0.002*m.x401 - 0.002*m.x407
                          - 0.002*m.x479 - 0.002*m.x485 - m.x528 + m.x529 >= 0)

m.c767 = Constraint(expr= - 0.002*m.x330 - 0.002*m.x336 - 0.002*m.x360 - 0.002*m.x366 - 0.002*m.x402 - 0.002*m.x408
                          - 0.002*m.x480 - 0.002*m.x486 - m.x529 + m.x530 >= 0)

m.c768 = Constraint(expr= - 0.002*m.x331 - 0.002*m.x337 - 0.002*m.x361 - 0.002*m.x367 - 0.002*m.x403 - 0.002*m.x409
                          - 0.002*m.x481 - 0.002*m.x487 - m.x530 + m.x531 >= 0)

m.c769 = Constraint(expr= - 0.002*m.x332 - 0.002*m.x338 - 0.002*m.x362 - 0.002*m.x368 - 0.002*m.x404 - 0.002*m.x410
                          - 0.002*m.x482 - 0.002*m.x488 - m.x531 + m.x532 >= 0)

m.c770 = Constraint(expr= - 0.002*m.x333 - 0.002*m.x339 - 0.002*m.x363 - 0.002*m.x369 - 0.002*m.x405 - 0.002*m.x411
                          - 0.002*m.x483 - 0.002*m.x489 - m.x532 + m.x533 >= 0)

m.c771 = Constraint(expr= - 0.002*m.x370 - 0.002*m.x376 - 0.002*m.x412 - 0.002*m.x418 - 0.002*m.x454 - 0.002*m.x460
                          - 0.002*m.x490 - 0.002*m.x496 - m.x527 + m.x528 >= 0)

m.c772 = Constraint(expr= - 0.002*m.x371 - 0.002*m.x377 - 0.002*m.x413 - 0.002*m.x419 - 0.002*m.x455 - 0.002*m.x461
                          - 0.002*m.x491 - 0.002*m.x497 - m.x528 + m.x529 >= 0)

m.c773 = Constraint(expr= - 0.002*m.x372 - 0.002*m.x378 - 0.002*m.x414 - 0.002*m.x420 - 0.002*m.x456 - 0.002*m.x462
                          - 0.002*m.x492 - 0.002*m.x498 - m.x529 + m.x530 >= 0)

m.c774 = Constraint(expr= - 0.002*m.x373 - 0.002*m.x379 - 0.002*m.x415 - 0.002*m.x421 - 0.002*m.x457 - 0.002*m.x463
                          - 0.002*m.x493 - 0.002*m.x499 - m.x530 + m.x531 >= 0)

m.c775 = Constraint(expr= - 0.002*m.x374 - 0.002*m.x380 - 0.002*m.x416 - 0.002*m.x422 - 0.002*m.x458 - 0.002*m.x464
                          - 0.002*m.x494 - 0.002*m.x500 - m.x531 + m.x532 >= 0)

m.c776 = Constraint(expr= - 0.002*m.x375 - 0.002*m.x381 - 0.002*m.x417 - 0.002*m.x423 - 0.002*m.x459 - 0.002*m.x465
                          - 0.002*m.x495 - 0.002*m.x501 - m.x532 + m.x533 >= 0)

m.c777 = Constraint(expr= - 0.002*m.x322 - 0.002*m.x328 - 0.002*m.x358 - 0.002*m.x400 - 0.002*m.x430 - 0.002*m.x472
                          - 0.002*m.x478 - m.x527 + m.x528 >= 0)

m.c778 = Constraint(expr= - 0.002*m.x323 - 0.002*m.x329 - 0.002*m.x359 - 0.002*m.x401 - 0.002*m.x431 - 0.002*m.x473
                          - 0.002*m.x479 - m.x528 + m.x529 >= 0)

m.c779 = Constraint(expr= - 0.002*m.x324 - 0.002*m.x330 - 0.002*m.x360 - 0.002*m.x402 - 0.002*m.x432 - 0.002*m.x474
                          - 0.002*m.x480 - m.x529 + m.x530 >= 0)

m.c780 = Constraint(expr= - 0.002*m.x325 - 0.002*m.x331 - 0.002*m.x361 - 0.002*m.x403 - 0.002*m.x433 - 0.002*m.x475
                          - 0.002*m.x481 - m.x530 + m.x531 >= 0)

m.c781 = Constraint(expr= - 0.002*m.x326 - 0.002*m.x332 - 0.002*m.x362 - 0.002*m.x404 - 0.002*m.x434 - 0.002*m.x476
                          - 0.002*m.x482 - m.x531 + m.x532 >= 0)

m.c782 = Constraint(expr= - 0.002*m.x327 - 0.002*m.x333 - 0.002*m.x363 - 0.002*m.x405 - 0.002*m.x435 - 0.002*m.x477
                          - 0.002*m.x483 - m.x532 + m.x533 >= 0)

m.c783 = Constraint(expr= - 0.002*m.x334 - 0.002*m.x364 - 0.002*m.x370 - 0.002*m.x406 - 0.002*m.x412 - 0.002*m.x454
                          - 0.002*m.x484 - 0.002*m.x490 - m.x527 + m.x528 >= 0)

m.c784 = Constraint(expr= - 0.002*m.x335 - 0.002*m.x365 - 0.002*m.x371 - 0.002*m.x407 - 0.002*m.x413 - 0.002*m.x455
                          - 0.002*m.x485 - 0.002*m.x491 - m.x528 + m.x529 >= 0)

m.c785 = Constraint(expr= - 0.002*m.x336 - 0.002*m.x366 - 0.002*m.x372 - 0.002*m.x408 - 0.002*m.x414 - 0.002*m.x456
                          - 0.002*m.x486 - 0.002*m.x492 - m.x529 + m.x530 >= 0)

m.c786 = Constraint(expr= - 0.002*m.x337 - 0.002*m.x367 - 0.002*m.x373 - 0.002*m.x409 - 0.002*m.x415 - 0.002*m.x457
                          - 0.002*m.x487 - 0.002*m.x493 - m.x530 + m.x531 >= 0)

m.c787 = Constraint(expr= - 0.002*m.x338 - 0.002*m.x368 - 0.002*m.x374 - 0.002*m.x410 - 0.002*m.x416 - 0.002*m.x458
                          - 0.002*m.x488 - 0.002*m.x494 - m.x531 + m.x532 >= 0)

m.c788 = Constraint(expr= - 0.002*m.x339 - 0.002*m.x369 - 0.002*m.x375 - 0.002*m.x411 - 0.002*m.x417 - 0.002*m.x459
                          - 0.002*m.x489 - 0.002*m.x495 - m.x532 + m.x533 >= 0)

m.c789 = Constraint(expr= - 0.002*m.x376 - 0.002*m.x418 - 0.002*m.x460 - 0.002*m.x466 - 0.002*m.x496 - m.x527 + m.x528
                          >= 0)

m.c790 = Constraint(expr= - 0.002*m.x377 - 0.002*m.x419 - 0.002*m.x461 - 0.002*m.x467 - 0.002*m.x497 - m.x528 + m.x529
                          >= 0)

m.c791 = Constraint(expr= - 0.002*m.x378 - 0.002*m.x420 - 0.002*m.x462 - 0.002*m.x468 - 0.002*m.x498 - m.x529 + m.x530
                          >= 0)

m.c792 = Constraint(expr= - 0.002*m.x379 - 0.002*m.x421 - 0.002*m.x463 - 0.002*m.x469 - 0.002*m.x499 - m.x530 + m.x531
                          >= 0)

m.c793 = Constraint(expr= - 0.002*m.x380 - 0.002*m.x422 - 0.002*m.x464 - 0.002*m.x470 - 0.002*m.x500 - m.x531 + m.x532
                          >= 0)

m.c794 = Constraint(expr= - 0.002*m.x381 - 0.002*m.x423 - 0.002*m.x465 - 0.002*m.x471 - 0.002*m.x501 - m.x532 + m.x533
                          >= 0)

m.c795 = Constraint(expr= - 0.05*m.x322 - 0.05*m.x328 - 0.05*m.x358 - 0.05*m.x400 - 0.05*m.x430 - 0.05*m.x472
                          - 0.05*m.x478 - m.x527 + m.x528 <= 0)

m.c796 = Constraint(expr= - 0.05*m.x323 - 0.05*m.x329 - 0.05*m.x359 - 0.05*m.x401 - 0.05*m.x431 - 0.05*m.x473
                          - 0.05*m.x479 - m.x528 + m.x529 <= 0)

m.c797 = Constraint(expr= - 0.05*m.x324 - 0.05*m.x330 - 0.05*m.x360 - 0.05*m.x402 - 0.05*m.x432 - 0.05*m.x474
                          - 0.05*m.x480 - m.x529 + m.x530 <= 0)

m.c798 = Constraint(expr= - 0.05*m.x325 - 0.05*m.x331 - 0.05*m.x361 - 0.05*m.x403 - 0.05*m.x433 - 0.05*m.x475
                          - 0.05*m.x481 - m.x530 + m.x531 <= 0)

m.c799 = Constraint(expr= - 0.05*m.x326 - 0.05*m.x332 - 0.05*m.x362 - 0.05*m.x404 - 0.05*m.x434 - 0.05*m.x476
                          - 0.05*m.x482 - m.x531 + m.x532 <= 0)

m.c800 = Constraint(expr= - 0.05*m.x327 - 0.05*m.x333 - 0.05*m.x363 - 0.05*m.x405 - 0.05*m.x435 - 0.05*m.x477
                          - 0.05*m.x483 - m.x532 + m.x533 <= 0)

m.c801 = Constraint(expr= - 0.05*m.x334 - 0.05*m.x364 - 0.05*m.x370 - 0.05*m.x406 - 0.05*m.x412 - 0.05*m.x454
                          - 0.05*m.x484 - 0.05*m.x490 - m.x527 + m.x528 <= 0)

m.c802 = Constraint(expr= - 0.05*m.x335 - 0.05*m.x365 - 0.05*m.x371 - 0.05*m.x407 - 0.05*m.x413 - 0.05*m.x455
                          - 0.05*m.x485 - 0.05*m.x491 - m.x528 + m.x529 <= 0)

m.c803 = Constraint(expr= - 0.05*m.x336 - 0.05*m.x366 - 0.05*m.x372 - 0.05*m.x408 - 0.05*m.x414 - 0.05*m.x456
                          - 0.05*m.x486 - 0.05*m.x492 - m.x529 + m.x530 <= 0)

m.c804 = Constraint(expr= - 0.05*m.x337 - 0.05*m.x367 - 0.05*m.x373 - 0.05*m.x409 - 0.05*m.x415 - 0.05*m.x457
                          - 0.05*m.x487 - 0.05*m.x493 - m.x530 + m.x531 <= 0)

m.c805 = Constraint(expr= - 0.05*m.x338 - 0.05*m.x368 - 0.05*m.x374 - 0.05*m.x410 - 0.05*m.x416 - 0.05*m.x458
                          - 0.05*m.x488 - 0.05*m.x494 - m.x531 + m.x532 <= 0)

m.c806 = Constraint(expr= - 0.05*m.x339 - 0.05*m.x369 - 0.05*m.x375 - 0.05*m.x411 - 0.05*m.x417 - 0.05*m.x459
                          - 0.05*m.x489 - 0.05*m.x495 - m.x532 + m.x533 <= 0)

m.c807 = Constraint(expr= - 0.05*m.x376 - 0.05*m.x418 - 0.05*m.x460 - 0.05*m.x466 - 0.05*m.x496 - m.x527 + m.x528 <= 0)

m.c808 = Constraint(expr= - 0.05*m.x377 - 0.05*m.x419 - 0.05*m.x461 - 0.05*m.x467 - 0.05*m.x497 - m.x528 + m.x529 <= 0)

m.c809 = Constraint(expr= - 0.05*m.x378 - 0.05*m.x420 - 0.05*m.x462 - 0.05*m.x468 - 0.05*m.x498 - m.x529 + m.x530 <= 0)

m.c810 = Constraint(expr= - 0.05*m.x379 - 0.05*m.x421 - 0.05*m.x463 - 0.05*m.x469 - 0.05*m.x499 - m.x530 + m.x531 <= 0)

m.c811 = Constraint(expr= - 0.05*m.x380 - 0.05*m.x422 - 0.05*m.x464 - 0.05*m.x470 - 0.05*m.x500 - m.x531 + m.x532 <= 0)

m.c812 = Constraint(expr= - 0.05*m.x381 - 0.05*m.x423 - 0.05*m.x465 - 0.05*m.x471 - 0.05*m.x501 - m.x532 + m.x533 <= 0)

m.c813 = Constraint(expr=   m.x527 >= 0)

m.c814 = Constraint(expr= - 5*m.b117 + m.x528 >= 0)

m.c815 = Constraint(expr= - 5*m.b119 - 10*m.b120 + m.x529 >= 0)

m.c816 = Constraint(expr= - 5*m.b122 - 10*m.b123 + m.x530 >= 0)

m.c817 = Constraint(expr= - 5*m.b124 - 10*m.b125 + m.x531 >= 0)

m.c818 = Constraint(expr= - 10*m.b126 + m.x532 >= 0)

m.c819 = Constraint(expr= - 1.2*m.b127 + m.x528 >= 0)

m.c820 = Constraint(expr= - 1.2*m.b128 - 6.2*m.b129 + m.x529 >= 0)

m.c821 = Constraint(expr= - 1.2*m.b130 - 6.2*m.b131 - 11.2*m.b132 + m.x530 >= 0)

m.c822 = Constraint(expr= - 1.2*m.b133 - 6.2*m.b134 - 11.2*m.b135 + m.x531 >= 0)

m.c823 = Constraint(expr= - 6.2*m.b136 - 11.2*m.b137 + m.x532 >= 0)

m.c824 = Constraint(expr= - 11.2*m.b138 + m.x533 >= 0)

m.c825 = Constraint(expr=   m.b115 + 2*m.b116 + 3*m.b118 + 4*m.b121 - 2*m.b127 - 3*m.b128 - 4*m.b130 - 5*m.b133 <= -1)

m.c826 = Constraint(expr=   2*m.b117 + 3*m.b119 + 4*m.b122 + 5*m.b124 - 3*m.b129 - 4*m.b131 - 5*m.b134 - 6*m.b136 <= -1)

m.c827 = Constraint(expr=   3*m.b120 + 4*m.b123 + 5*m.b125 + 6*m.b126 - 4*m.b132 - 5*m.b135 - 6*m.b137 - 7*m.b138 <= -1)

m.c828 = Constraint(expr= - 2*m.b117 - 3*m.b119 - 4*m.b122 - 5*m.b124 + 2*m.b127 + 3*m.b128 + 4*m.b130 + 5*m.b133 <= 0)

m.c829 = Constraint(expr= - 3*m.b120 - 4*m.b123 - 5*m.b125 - 6*m.b126 + 3*m.b129 + 4*m.b131 + 5*m.b134 + 6*m.b136 <= 0)

m.c830 = Constraint(expr=   m.x154 + m.x155 + m.x156 <= 7)

m.c831 = Constraint(expr=-m.x502*m.x172 + m.x323 == 0)

m.c832 = Constraint(expr=-m.x503*m.x173 + m.x324 == 0)

m.c833 = Constraint(expr=-m.x504*m.x174 + m.x325 == 0)

m.c834 = Constraint(expr=-m.x505*m.x175 + m.x326 == 0)

m.c835 = Constraint(expr=-m.x506*m.x176 + m.x327 == 0)

m.c836 = Constraint(expr=-m.x507*m.x179 + m.x329 == 0)

m.c837 = Constraint(expr=-m.x508*m.x180 + m.x330 == 0)

m.c838 = Constraint(expr=-m.x509*m.x181 + m.x331 == 0)

m.c839 = Constraint(expr=-m.x510*m.x182 + m.x332 == 0)

m.c840 = Constraint(expr=-m.x511*m.x183 + m.x333 == 0)

m.c841 = Constraint(expr=-m.x512*m.x179 + m.x335 == 0)

m.c842 = Constraint(expr=-m.x513*m.x180 + m.x336 == 0)

m.c843 = Constraint(expr=-m.x514*m.x181 + m.x337 == 0)

m.c844 = Constraint(expr=-m.x515*m.x182 + m.x338 == 0)

m.c845 = Constraint(expr=-m.x516*m.x183 + m.x339 == 0)

m.c846 = Constraint(expr=-m.x507*m.x200 + m.x359 == 0)

m.c847 = Constraint(expr=-m.x508*m.x201 + m.x360 == 0)

m.c848 = Constraint(expr=-m.x509*m.x202 + m.x361 == 0)

m.c849 = Constraint(expr=-m.x510*m.x203 + m.x362 == 0)

m.c850 = Constraint(expr=-m.x511*m.x204 + m.x363 == 0)

m.c851 = Constraint(expr=-m.x512*m.x200 + m.x365 == 0)

m.c852 = Constraint(expr=-m.x513*m.x201 + m.x366 == 0)

m.c853 = Constraint(expr=-m.x514*m.x202 + m.x367 == 0)

m.c854 = Constraint(expr=-m.x515*m.x203 + m.x368 == 0)

m.c855 = Constraint(expr=-m.x516*m.x204 + m.x369 == 0)

m.c856 = Constraint(expr=-m.x517*m.x207 + m.x371 == 0)

m.c857 = Constraint(expr=-m.x518*m.x208 + m.x372 == 0)

m.c858 = Constraint(expr=-m.x519*m.x209 + m.x373 == 0)

m.c859 = Constraint(expr=-m.x520*m.x210 + m.x374 == 0)

m.c860 = Constraint(expr=-m.x521*m.x211 + m.x375 == 0)

m.c861 = Constraint(expr=-m.x522*m.x207 + m.x377 == 0)

m.c862 = Constraint(expr=-m.x523*m.x208 + m.x378 == 0)

m.c863 = Constraint(expr=-m.x524*m.x209 + m.x379 == 0)

m.c864 = Constraint(expr=-m.x525*m.x210 + m.x380 == 0)

m.c865 = Constraint(expr=-m.x526*m.x211 + m.x381 == 0)

m.c866 = Constraint(expr=-m.x507*m.x228 + m.x401 == 0)

m.c867 = Constraint(expr=-m.x508*m.x229 + m.x402 == 0)

m.c868 = Constraint(expr=-m.x509*m.x230 + m.x403 == 0)

m.c869 = Constraint(expr=-m.x510*m.x231 + m.x404 == 0)

m.c870 = Constraint(expr=-m.x511*m.x232 + m.x405 == 0)

m.c871 = Constraint(expr=-m.x512*m.x228 + m.x407 == 0)

m.c872 = Constraint(expr=-m.x513*m.x229 + m.x408 == 0)

m.c873 = Constraint(expr=-m.x514*m.x230 + m.x409 == 0)

m.c874 = Constraint(expr=-m.x515*m.x231 + m.x410 == 0)

m.c875 = Constraint(expr=-m.x516*m.x232 + m.x411 == 0)

m.c876 = Constraint(expr=-m.x517*m.x235 + m.x413 == 0)

m.c877 = Constraint(expr=-m.x518*m.x236 + m.x414 == 0)

m.c878 = Constraint(expr=-m.x519*m.x237 + m.x415 == 0)

m.c879 = Constraint(expr=-m.x520*m.x238 + m.x416 == 0)

m.c880 = Constraint(expr=-m.x521*m.x239 + m.x417 == 0)

m.c881 = Constraint(expr=-m.x522*m.x235 + m.x419 == 0)

m.c882 = Constraint(expr=-m.x523*m.x236 + m.x420 == 0)

m.c883 = Constraint(expr=-m.x524*m.x237 + m.x421 == 0)

m.c884 = Constraint(expr=-m.x525*m.x238 + m.x422 == 0)

m.c885 = Constraint(expr=-m.x526*m.x239 + m.x423 == 0)

m.c886 = Constraint(expr=-m.x502*m.x249 + m.x431 == 0)

m.c887 = Constraint(expr=-m.x503*m.x250 + m.x432 == 0)

m.c888 = Constraint(expr=-m.x504*m.x251 + m.x433 == 0)

m.c889 = Constraint(expr=-m.x505*m.x252 + m.x434 == 0)

m.c890 = Constraint(expr=-m.x506*m.x253 + m.x435 == 0)

m.c891 = Constraint(expr=-m.x517*m.x270 + m.x455 == 0)

m.c892 = Constraint(expr=-m.x518*m.x271 + m.x456 == 0)

m.c893 = Constraint(expr=-m.x519*m.x272 + m.x457 == 0)

m.c894 = Constraint(expr=-m.x520*m.x273 + m.x458 == 0)

m.c895 = Constraint(expr=-m.x521*m.x274 + m.x459 == 0)

m.c896 = Constraint(expr=-m.x522*m.x270 + m.x461 == 0)

m.c897 = Constraint(expr=-m.x523*m.x271 + m.x462 == 0)

m.c898 = Constraint(expr=-m.x524*m.x272 + m.x463 == 0)

m.c899 = Constraint(expr=-m.x525*m.x273 + m.x464 == 0)

m.c900 = Constraint(expr=-m.x526*m.x274 + m.x465 == 0)

m.c901 = Constraint(expr=-m.x502*m.x284 + m.x473 == 0)

m.c902 = Constraint(expr=-m.x503*m.x285 + m.x474 == 0)

m.c903 = Constraint(expr=-m.x504*m.x286 + m.x475 == 0)

m.c904 = Constraint(expr=-m.x505*m.x287 + m.x476 == 0)

m.c905 = Constraint(expr=-m.x506*m.x288 + m.x477 == 0)

m.c906 = Constraint(expr=-m.x507*m.x291 + m.x479 == 0)

m.c907 = Constraint(expr=-m.x508*m.x292 + m.x480 == 0)

m.c908 = Constraint(expr=-m.x509*m.x293 + m.x481 == 0)

m.c909 = Constraint(expr=-m.x510*m.x294 + m.x482 == 0)

m.c910 = Constraint(expr=-m.x511*m.x295 + m.x483 == 0)

m.c911 = Constraint(expr=-m.x512*m.x291 + m.x485 == 0)

m.c912 = Constraint(expr=-m.x513*m.x292 + m.x486 == 0)

m.c913 = Constraint(expr=-m.x514*m.x293 + m.x487 == 0)

m.c914 = Constraint(expr=-m.x515*m.x294 + m.x488 == 0)

m.c915 = Constraint(expr=-m.x516*m.x295 + m.x489 == 0)

m.c916 = Constraint(expr=-m.x517*m.x298 + m.x491 == 0)

m.c917 = Constraint(expr=-m.x518*m.x299 + m.x492 == 0)

m.c918 = Constraint(expr=-m.x519*m.x300 + m.x493 == 0)

m.c919 = Constraint(expr=-m.x520*m.x301 + m.x494 == 0)

m.c920 = Constraint(expr=-m.x521*m.x302 + m.x495 == 0)

m.c921 = Constraint(expr=-m.x522*m.x298 + m.x497 == 0)

m.c922 = Constraint(expr=-m.x523*m.x299 + m.x498 == 0)

m.c923 = Constraint(expr=-m.x524*m.x300 + m.x499 == 0)

m.c924 = Constraint(expr=-m.x525*m.x301 + m.x500 == 0)

m.c925 = Constraint(expr=-m.x526*m.x302 + m.x501 == 0)
