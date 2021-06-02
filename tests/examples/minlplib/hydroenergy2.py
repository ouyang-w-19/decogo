#  MINLP written by GAMS Convert at 04/21/18 13:52:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        857      193      288      376        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        577      385      192        0        0        0        0        0
#  FX      4        4        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2497     2233      264        0
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
m.b139 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b140 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b141 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b142 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b143 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b144 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b145 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b146 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b147 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b148 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b149 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b150 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b151 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b152 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b153 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b154 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b155 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b156 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b157 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b158 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b159 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b160 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b161 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b162 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b163 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b164 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b165 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b166 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b167 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b168 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b169 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b170 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b171 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b172 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b173 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b174 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b175 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b176 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b177 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b178 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b179 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b180 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b181 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b182 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b183 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b184 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b185 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b186 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b187 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b188 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b189 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b190 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b191 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b192 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x235 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x255 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x258 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x262 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x263 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x264 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x265 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x266 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x267 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x268 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x269 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x270 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x271 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x272 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x273 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x274 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x275 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x276 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x277 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x278 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x279 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x280 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x281 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x282 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x283 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x284 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x285 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x286 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x287 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,185.99),initialize=0)
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
m.x385 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x386 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x387 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x388 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x389 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x390 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x391 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x392 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x393 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x394 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x395 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x396 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x397 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x398 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x399 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x400 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x401 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x402 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x403 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x404 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x405 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x406 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x407 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x408 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x409 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x410 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x411 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x412 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x413 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x414 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x415 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x416 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x417 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x418 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x419 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x420 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x421 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x422 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x423 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x424 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x425 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x426 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x427 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x428 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x429 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x430 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x431 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x432 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x433 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x434 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x435 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x436 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x437 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x438 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x439 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x440 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x441 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x442 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x443 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x444 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x445 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x446 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x447 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x448 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x449 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x450 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x451 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x452 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x453 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x454 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x455 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x456 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x457 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x458 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x459 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x460 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x461 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x462 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x463 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x464 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x465 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x466 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x467 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x468 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x469 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x470 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x471 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x472 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x473 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x474 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x475 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x476 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x477 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x478 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x479 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x480 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x481 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x482 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x483 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x484 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x485 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x486 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x487 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x488 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x489 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x490 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x491 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x492 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x493 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x494 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x495 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x496 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x497 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x498 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x499 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x500 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x501 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x502 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x503 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x504 = Var(within=Reals,bounds=(10.35,10.35),initialize=10.35)
m.x505 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x506 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x507 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x508 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x509 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x510 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x511 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x512 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x513 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x514 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x515 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x516 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x517 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x518 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x519 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x520 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x521 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x522 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x523 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x524 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x525 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x526 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x527 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x528 = Var(within=Reals,bounds=(10.64,10.64),initialize=10.64)
m.x529 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x530 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x531 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x532 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x533 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x534 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x535 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x536 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x537 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x538 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x539 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x540 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x541 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x542 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x543 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x544 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x545 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x546 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x547 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x548 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x549 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x550 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x551 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x552 = Var(within=Reals,bounds=(78,78),initialize=78)
m.x553 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x554 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x555 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x556 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x557 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x558 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x559 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x560 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x561 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x562 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x563 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x564 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x565 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x566 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x567 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x568 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x569 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x570 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x571 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x572 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x573 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x574 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x575 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x576 = Var(within=Reals,bounds=(9.6,9.6),initialize=9.6)

m.obj = Objective(expr= - 470.2*m.b97 - 470.2*m.b98 - 470.2*m.b99 - 470.2*m.b100 - 470.2*m.b101 - 470.2*m.b102
                        - 470.2*m.b103 - 470.2*m.b104 - 470.2*m.b105 - 470.2*m.b106 - 470.2*m.b107 - 470.2*m.b108
                        - 470.2*m.b109 - 470.2*m.b110 - 470.2*m.b111 - 470.2*m.b112 - 470.2*m.b113 - 470.2*m.b114
                        - 470.2*m.b115 - 470.2*m.b116 - 470.2*m.b117 - 470.2*m.b118 - 470.2*m.b119 - 470.2*m.b120
                        - 592.85*m.b121 - 592.85*m.b122 - 592.85*m.b123 - 592.85*m.b124 - 592.85*m.b125 - 592.85*m.b126
                        - 592.85*m.b127 - 592.85*m.b128 - 592.85*m.b129 - 592.85*m.b130 - 592.85*m.b131 - 592.85*m.b132
                        - 592.85*m.b133 - 592.85*m.b134 - 592.85*m.b135 - 592.85*m.b136 - 592.85*m.b137 - 592.85*m.b138
                        - 592.85*m.b139 - 592.85*m.b140 - 592.85*m.b141 - 592.85*m.b142 - 592.85*m.b143 - 592.85*m.b144
                        - 150*m.b145 - 150*m.b146 - 150*m.b147 - 150*m.b148 - 150*m.b149 - 150*m.b150 - 150*m.b151
                        - 150*m.b152 - 150*m.b153 - 150*m.b154 - 150*m.b155 - 150*m.b156 - 150*m.b157 - 150*m.b158
                        - 150*m.b159 - 150*m.b160 - 150*m.b161 - 150*m.b162 - 150*m.b163 - 150*m.b164 - 150*m.b165
                        - 150*m.b166 - 150*m.b167 - 150*m.b168 - 464.975*m.b169 - 464.975*m.b170 - 464.975*m.b171
                        - 464.975*m.b172 - 464.975*m.b173 - 464.975*m.b174 - 464.975*m.b175 - 464.975*m.b176
                        - 464.975*m.b177 - 464.975*m.b178 - 464.975*m.b179 - 464.975*m.b180 - 464.975*m.b181
                        - 464.975*m.b182 - 464.975*m.b183 - 464.975*m.b184 - 464.975*m.b185 - 464.975*m.b186
                        - 464.975*m.b187 - 464.975*m.b188 - 464.975*m.b189 - 464.975*m.b190 - 464.975*m.b191
                        - 464.975*m.b192 + 50.4*m.x193 + 46.287*m.x194 + 44.187*m.x195 + 44.787*m.x196 + 45.477*m.x197
                        + 47.523*m.x198 + 58.359*m.x199 + 68.487*m.x200 + 87.441*m.x201 + 91.395*m.x202 + 93.846*m.x203
                        + 94.995*m.x204 + 86.187*m.x205 + 92.295*m.x206 + 93.495*m.x207 + 92.259*m.x208 + 93.795*m.x209
                        + 103.254*m.x210 + 103.359*m.x211 + 100.623*m.x212 + 95.418*m.x213 + 92.136*m.x214
                        + 82.305*m.x215 + 68.946*m.x216 + 50.4*m.x217 + 46.287*m.x218 + 44.187*m.x219 + 44.787*m.x220
                        + 45.477*m.x221 + 47.523*m.x222 + 58.359*m.x223 + 68.487*m.x224 + 87.441*m.x225 + 91.395*m.x226
                        + 93.846*m.x227 + 94.995*m.x228 + 86.187*m.x229 + 92.295*m.x230 + 93.495*m.x231 + 92.259*m.x232
                        + 93.795*m.x233 + 103.254*m.x234 + 103.359*m.x235 + 100.623*m.x236 + 95.418*m.x237
                        + 92.136*m.x238 + 82.305*m.x239 + 68.946*m.x240 + 50.4*m.x241 + 46.287*m.x242 + 44.187*m.x243
                        + 44.787*m.x244 + 45.477*m.x245 + 47.523*m.x246 + 58.359*m.x247 + 68.487*m.x248 + 87.441*m.x249
                        + 91.395*m.x250 + 93.846*m.x251 + 94.995*m.x252 + 86.187*m.x253 + 92.295*m.x254 + 93.495*m.x255
                        + 92.259*m.x256 + 93.795*m.x257 + 103.254*m.x258 + 103.359*m.x259 + 100.623*m.x260
                        + 95.418*m.x261 + 92.136*m.x262 + 82.305*m.x263 + 68.946*m.x264 + 50.4*m.x265 + 46.287*m.x266
                        + 44.187*m.x267 + 44.787*m.x268 + 45.477*m.x269 + 47.523*m.x270 + 58.359*m.x271 + 68.487*m.x272
                        + 87.441*m.x273 + 91.395*m.x274 + 93.846*m.x275 + 94.995*m.x276 + 86.187*m.x277 + 92.295*m.x278
                        + 93.495*m.x279 + 92.259*m.x280 + 93.795*m.x281 + 103.254*m.x282 + 103.359*m.x283
                        + 100.623*m.x284 + 95.418*m.x285 + 92.136*m.x286 + 82.305*m.x287 + 68.946*m.x288
                       , sense=maximize)

m.c2 = Constraint(expr=   m.x289 + m.x385 + m.x481 == 10.4208)

m.c3 = Constraint(expr=   m.x290 + m.x386 - m.x481 + m.x482 == 0.0708)

m.c4 = Constraint(expr=   m.x291 + m.x387 - m.x482 + m.x483 == 0.0708)

m.c5 = Constraint(expr=   m.x292 + m.x388 - m.x483 + m.x484 == 0.0708)

m.c6 = Constraint(expr=   m.x293 + m.x389 - m.x484 + m.x485 == 0.0708)

m.c7 = Constraint(expr=   m.x294 + m.x390 - m.x485 + m.x486 == 0.0708)

m.c8 = Constraint(expr=   m.x295 + m.x391 - m.x486 + m.x487 == 0.7374)

m.c9 = Constraint(expr=   m.x296 + m.x392 - m.x487 + m.x488 == 0.7374)

m.c10 = Constraint(expr=   m.x297 + m.x393 - m.x488 + m.x489 == 0.7374)

m.c11 = Constraint(expr=   m.x298 + m.x394 - m.x489 + m.x490 == 0.7374)

m.c12 = Constraint(expr=   m.x299 + m.x395 - m.x490 + m.x491 == 0.7374)

m.c13 = Constraint(expr=   m.x300 + m.x396 - m.x491 + m.x492 == 0.7374)

m.c14 = Constraint(expr=   m.x301 + m.x397 - m.x492 + m.x493 == 0.7374)

m.c15 = Constraint(expr=   m.x302 + m.x398 - m.x493 + m.x494 == 0.7374)

m.c16 = Constraint(expr=   m.x303 + m.x399 - m.x494 + m.x495 == 0.7374)

m.c17 = Constraint(expr=   m.x304 + m.x400 - m.x495 + m.x496 == 0.7374)

m.c18 = Constraint(expr=   m.x305 + m.x401 - m.x496 + m.x497 == 0.7374)

m.c19 = Constraint(expr=   m.x306 + m.x402 - m.x497 + m.x498 == 0.7374)

m.c20 = Constraint(expr=   m.x307 + m.x403 - m.x498 + m.x499 == 0.7374)

m.c21 = Constraint(expr=   m.x308 + m.x404 - m.x499 + m.x500 == 0.7374)

m.c22 = Constraint(expr=   m.x309 + m.x405 - m.x500 + m.x501 == 0.7374)

m.c23 = Constraint(expr=   m.x310 + m.x406 - m.x501 + m.x502 == 0.7374)

m.c24 = Constraint(expr=   m.x311 + m.x407 - m.x502 + m.x503 == 0.7374)

m.c25 = Constraint(expr=   m.x312 + m.x408 - m.x503 + m.x504 == 0.7374)

m.c26 = Constraint(expr= - m.x289 + m.x313 - m.x385 + m.x409 + m.x505 == 10.7948)

m.c27 = Constraint(expr= - m.x290 + m.x314 - m.x386 + m.x410 - m.x505 + m.x506 == 0.1548)

m.c28 = Constraint(expr= - m.x291 + m.x315 - m.x387 + m.x411 - m.x506 + m.x507 == 0.1548)

m.c29 = Constraint(expr= - m.x292 + m.x316 - m.x388 + m.x412 - m.x507 + m.x508 == 0.1548)

m.c30 = Constraint(expr= - m.x293 + m.x317 - m.x389 + m.x413 - m.x508 + m.x509 == 0.1548)

m.c31 = Constraint(expr= - m.x294 + m.x318 - m.x390 + m.x414 - m.x509 + m.x510 == 0.1548)

m.c32 = Constraint(expr= - m.x295 + m.x319 - m.x391 + m.x415 - m.x510 + m.x511 == 0.1548)

m.c33 = Constraint(expr= - m.x296 + m.x320 - m.x392 + m.x416 - m.x511 + m.x512 == 0.1548)

m.c34 = Constraint(expr= - m.x297 + m.x321 - m.x393 + m.x417 - m.x512 + m.x513 == 0.1548)

m.c35 = Constraint(expr= - m.x298 + m.x322 - m.x394 + m.x418 - m.x513 + m.x514 == 0.1548)

m.c36 = Constraint(expr= - m.x299 + m.x323 - m.x395 + m.x419 - m.x514 + m.x515 == 0.1548)

m.c37 = Constraint(expr= - m.x300 + m.x324 - m.x396 + m.x420 - m.x515 + m.x516 == 0.1548)

m.c38 = Constraint(expr= - m.x301 + m.x325 - m.x397 + m.x421 - m.x516 + m.x517 == 0.1548)

m.c39 = Constraint(expr= - m.x302 + m.x326 - m.x398 + m.x422 - m.x517 + m.x518 == 0.1548)

m.c40 = Constraint(expr= - m.x303 + m.x327 - m.x399 + m.x423 - m.x518 + m.x519 == 0.1548)

m.c41 = Constraint(expr= - m.x304 + m.x328 - m.x400 + m.x424 - m.x519 + m.x520 == 0.1548)

m.c42 = Constraint(expr= - m.x305 + m.x329 - m.x401 + m.x425 - m.x520 + m.x521 == 0.1548)

m.c43 = Constraint(expr= - m.x306 + m.x330 - m.x402 + m.x426 - m.x521 + m.x522 == 0.1548)

m.c44 = Constraint(expr= - m.x307 + m.x331 - m.x403 + m.x427 - m.x522 + m.x523 == 0.1548)

m.c45 = Constraint(expr= - m.x308 + m.x332 - m.x404 + m.x428 - m.x523 + m.x524 == 0.1548)

m.c46 = Constraint(expr= - m.x309 + m.x333 - m.x405 + m.x429 - m.x524 + m.x525 == 0.1548)

m.c47 = Constraint(expr= - m.x310 + m.x334 - m.x406 + m.x430 - m.x525 + m.x526 == 0.1548)

m.c48 = Constraint(expr= - m.x311 + m.x335 - m.x407 + m.x431 - m.x526 + m.x527 == 0.1548)

m.c49 = Constraint(expr= - m.x312 + m.x336 - m.x408 + m.x432 - m.x527 + m.x528 == 0.1548)

m.c50 = Constraint(expr=   m.x337 + m.x433 + m.x529 == 78.0108)

m.c51 = Constraint(expr=   m.x338 + m.x434 - m.x529 + m.x530 == 0.0108)

m.c52 = Constraint(expr=   m.x339 + m.x435 - m.x530 + m.x531 == 0.0108)

m.c53 = Constraint(expr=   m.x340 + m.x436 - m.x531 + m.x532 == 0.0108)

m.c54 = Constraint(expr=   m.x341 + m.x437 - m.x532 + m.x533 == 0.0108)

m.c55 = Constraint(expr=   m.x342 + m.x438 - m.x533 + m.x534 == 0.0108)

m.c56 = Constraint(expr=   m.x343 + m.x439 - m.x534 + m.x535 == 0.0108)

m.c57 = Constraint(expr=   m.x344 + m.x440 - m.x535 + m.x536 == 0.0108)

m.c58 = Constraint(expr=   m.x345 + m.x441 - m.x536 + m.x537 == 0.0108)

m.c59 = Constraint(expr=   m.x346 + m.x442 - m.x537 + m.x538 == 0.0108)

m.c60 = Constraint(expr=   m.x347 + m.x443 - m.x538 + m.x539 == 0.0108)

m.c61 = Constraint(expr=   m.x348 + m.x444 - m.x539 + m.x540 == 0.0108)

m.c62 = Constraint(expr=   m.x349 + m.x445 - m.x540 + m.x541 == 0.0108)

m.c63 = Constraint(expr=   m.x350 + m.x446 - m.x541 + m.x542 == 0.0108)

m.c64 = Constraint(expr=   m.x351 + m.x447 - m.x542 + m.x543 == 0.0108)

m.c65 = Constraint(expr=   m.x352 + m.x448 - m.x543 + m.x544 == 0.0108)

m.c66 = Constraint(expr=   m.x353 + m.x449 - m.x544 + m.x545 == 0.0108)

m.c67 = Constraint(expr=   m.x354 + m.x450 - m.x545 + m.x546 == 0.0108)

m.c68 = Constraint(expr=   m.x355 + m.x451 - m.x546 + m.x547 == 0.0108)

m.c69 = Constraint(expr=   m.x356 + m.x452 - m.x547 + m.x548 == 0.0108)

m.c70 = Constraint(expr=   m.x357 + m.x453 - m.x548 + m.x549 == 0.0108)

m.c71 = Constraint(expr=   m.x358 + m.x454 - m.x549 + m.x550 == 0.0108)

m.c72 = Constraint(expr=   m.x359 + m.x455 - m.x550 + m.x551 == 0.0108)

m.c73 = Constraint(expr=   m.x360 + m.x456 - m.x551 + m.x552 == 0.0108)

m.c74 = Constraint(expr= - m.x313 - m.x337 + m.x361 - m.x409 - m.x433 + m.x457 + m.x553 == 9.7115)

m.c75 = Constraint(expr= - m.x314 - m.x338 + m.x362 - m.x410 - m.x434 + m.x458 - m.x553 + m.x554 == 0.1115)

m.c76 = Constraint(expr= - m.x315 - m.x339 + m.x363 - m.x411 - m.x435 + m.x459 - m.x554 + m.x555 == 0.1115)

m.c77 = Constraint(expr= - m.x316 - m.x340 + m.x364 - m.x412 - m.x436 + m.x460 - m.x555 + m.x556 == 0.1115)

m.c78 = Constraint(expr= - m.x317 - m.x341 + m.x365 - m.x413 - m.x437 + m.x461 - m.x556 + m.x557 == 0.1115)

m.c79 = Constraint(expr= - m.x318 - m.x342 + m.x366 - m.x414 - m.x438 + m.x462 - m.x557 + m.x558 == 0.1115)

m.c80 = Constraint(expr= - m.x319 - m.x343 + m.x367 - m.x415 - m.x439 + m.x463 - m.x558 + m.x559 == 0.1115)

m.c81 = Constraint(expr= - m.x320 - m.x344 + m.x368 - m.x416 - m.x440 + m.x464 - m.x559 + m.x560 == 0.1115)

m.c82 = Constraint(expr= - m.x321 - m.x345 + m.x369 - m.x417 - m.x441 + m.x465 - m.x560 + m.x561 == 0.1115)

m.c83 = Constraint(expr= - m.x322 - m.x346 + m.x370 - m.x418 - m.x442 + m.x466 - m.x561 + m.x562 == 0.1115)

m.c84 = Constraint(expr= - m.x323 - m.x347 + m.x371 - m.x419 - m.x443 + m.x467 - m.x562 + m.x563 == 0.1115)

m.c85 = Constraint(expr= - m.x324 - m.x348 + m.x372 - m.x420 - m.x444 + m.x468 - m.x563 + m.x564 == 0.1115)

m.c86 = Constraint(expr= - m.x325 - m.x349 + m.x373 - m.x421 - m.x445 + m.x469 - m.x564 + m.x565 == 0.1115)

m.c87 = Constraint(expr= - m.x326 - m.x350 + m.x374 - m.x422 - m.x446 + m.x470 - m.x565 + m.x566 == 0.1115)

m.c88 = Constraint(expr= - m.x327 - m.x351 + m.x375 - m.x423 - m.x447 + m.x471 - m.x566 + m.x567 == 0.1115)

m.c89 = Constraint(expr= - m.x328 - m.x352 + m.x376 - m.x424 - m.x448 + m.x472 - m.x567 + m.x568 == 0.1115)

m.c90 = Constraint(expr= - m.x329 - m.x353 + m.x377 - m.x425 - m.x449 + m.x473 - m.x568 + m.x569 == 0.1115)

m.c91 = Constraint(expr= - m.x330 - m.x354 + m.x378 - m.x426 - m.x450 + m.x474 - m.x569 + m.x570 == 0.1115)

m.c92 = Constraint(expr= - m.x331 - m.x355 + m.x379 - m.x427 - m.x451 + m.x475 - m.x570 + m.x571 == 0.1115)

m.c93 = Constraint(expr= - m.x332 - m.x356 + m.x380 - m.x428 - m.x452 + m.x476 - m.x571 + m.x572 == 0.1115)

m.c94 = Constraint(expr= - m.x333 - m.x357 + m.x381 - m.x429 - m.x453 + m.x477 - m.x572 + m.x573 == 0.1115)

m.c95 = Constraint(expr= - m.x334 - m.x358 + m.x382 - m.x430 - m.x454 + m.x478 - m.x573 + m.x574 == 0.1115)

m.c96 = Constraint(expr= - m.x335 - m.x359 + m.x383 - m.x431 - m.x455 + m.x479 - m.x574 + m.x575 == 0.1115)

m.c97 = Constraint(expr= - m.x336 - m.x360 + m.x384 - m.x432 - m.x456 + m.x480 - m.x575 + m.x576 == 0.1115)

m.c98 = Constraint(expr= - 4.1202*m.b1 + m.x385 <= 0)

m.c99 = Constraint(expr= - 4.1202*m.b2 + m.x386 <= 0)

m.c100 = Constraint(expr= - 4.1202*m.b3 + m.x387 <= 0)

m.c101 = Constraint(expr= - 4.1202*m.b4 + m.x388 <= 0)

m.c102 = Constraint(expr= - 4.1202*m.b5 + m.x389 <= 0)

m.c103 = Constraint(expr= - 4.1202*m.b6 + m.x390 <= 0)

m.c104 = Constraint(expr= - 4.1202*m.b7 + m.x391 <= 0)

m.c105 = Constraint(expr= - 4.1202*m.b8 + m.x392 <= 0)

m.c106 = Constraint(expr= - 4.1202*m.b9 + m.x393 <= 0)

m.c107 = Constraint(expr= - 4.1202*m.b10 + m.x394 <= 0)

m.c108 = Constraint(expr= - 4.1202*m.b11 + m.x395 <= 0)

m.c109 = Constraint(expr= - 4.1202*m.b12 + m.x396 <= 0)

m.c110 = Constraint(expr= - 4.1202*m.b13 + m.x397 <= 0)

m.c111 = Constraint(expr= - 4.1202*m.b14 + m.x398 <= 0)

m.c112 = Constraint(expr= - 4.1202*m.b15 + m.x399 <= 0)

m.c113 = Constraint(expr= - 4.1202*m.b16 + m.x400 <= 0)

m.c114 = Constraint(expr= - 4.1202*m.b17 + m.x401 <= 0)

m.c115 = Constraint(expr= - 4.1202*m.b18 + m.x402 <= 0)

m.c116 = Constraint(expr= - 4.1202*m.b19 + m.x403 <= 0)

m.c117 = Constraint(expr= - 4.1202*m.b20 + m.x404 <= 0)

m.c118 = Constraint(expr= - 4.1202*m.b21 + m.x405 <= 0)

m.c119 = Constraint(expr= - 4.1202*m.b22 + m.x406 <= 0)

m.c120 = Constraint(expr= - 4.1202*m.b23 + m.x407 <= 0)

m.c121 = Constraint(expr= - 4.1202*m.b24 + m.x408 <= 0)

m.c122 = Constraint(expr= - 3.888*m.b25 + m.x409 <= 0)

m.c123 = Constraint(expr= - 3.888*m.b26 + m.x410 <= 0)

m.c124 = Constraint(expr= - 3.888*m.b27 + m.x411 <= 0)

m.c125 = Constraint(expr= - 3.888*m.b28 + m.x412 <= 0)

m.c126 = Constraint(expr= - 3.888*m.b29 + m.x413 <= 0)

m.c127 = Constraint(expr= - 3.888*m.b30 + m.x414 <= 0)

m.c128 = Constraint(expr= - 3.888*m.b31 + m.x415 <= 0)

m.c129 = Constraint(expr= - 3.888*m.b32 + m.x416 <= 0)

m.c130 = Constraint(expr= - 3.888*m.b33 + m.x417 <= 0)

m.c131 = Constraint(expr= - 3.888*m.b34 + m.x418 <= 0)

m.c132 = Constraint(expr= - 3.888*m.b35 + m.x419 <= 0)

m.c133 = Constraint(expr= - 3.888*m.b36 + m.x420 <= 0)

m.c134 = Constraint(expr= - 3.888*m.b37 + m.x421 <= 0)

m.c135 = Constraint(expr= - 3.888*m.b38 + m.x422 <= 0)

m.c136 = Constraint(expr= - 3.888*m.b39 + m.x423 <= 0)

m.c137 = Constraint(expr= - 3.888*m.b40 + m.x424 <= 0)

m.c138 = Constraint(expr= - 3.888*m.b41 + m.x425 <= 0)

m.c139 = Constraint(expr= - 3.888*m.b42 + m.x426 <= 0)

m.c140 = Constraint(expr= - 3.888*m.b43 + m.x427 <= 0)

m.c141 = Constraint(expr= - 3.888*m.b44 + m.x428 <= 0)

m.c142 = Constraint(expr= - 3.888*m.b45 + m.x429 <= 0)

m.c143 = Constraint(expr= - 3.888*m.b46 + m.x430 <= 0)

m.c144 = Constraint(expr= - 3.888*m.b47 + m.x431 <= 0)

m.c145 = Constraint(expr= - 3.888*m.b48 + m.x432 <= 0)

m.c146 = Constraint(expr= - 0.05904*m.b49 + m.x433 <= 0)

m.c147 = Constraint(expr= - 0.05904*m.b50 + m.x434 <= 0)

m.c148 = Constraint(expr= - 0.05904*m.b51 + m.x435 <= 0)

m.c149 = Constraint(expr= - 0.05904*m.b52 + m.x436 <= 0)

m.c150 = Constraint(expr= - 0.05904*m.b53 + m.x437 <= 0)

m.c151 = Constraint(expr= - 0.05904*m.b54 + m.x438 <= 0)

m.c152 = Constraint(expr= - 0.05904*m.b55 + m.x439 <= 0)

m.c153 = Constraint(expr= - 0.05904*m.b56 + m.x440 <= 0)

m.c154 = Constraint(expr= - 0.05904*m.b57 + m.x441 <= 0)

m.c155 = Constraint(expr= - 0.05904*m.b58 + m.x442 <= 0)

m.c156 = Constraint(expr= - 0.05904*m.b59 + m.x443 <= 0)

m.c157 = Constraint(expr= - 0.05904*m.b60 + m.x444 <= 0)

m.c158 = Constraint(expr= - 0.05904*m.b61 + m.x445 <= 0)

m.c159 = Constraint(expr= - 0.05904*m.b62 + m.x446 <= 0)

m.c160 = Constraint(expr= - 0.05904*m.b63 + m.x447 <= 0)

m.c161 = Constraint(expr= - 0.05904*m.b64 + m.x448 <= 0)

m.c162 = Constraint(expr= - 0.05904*m.b65 + m.x449 <= 0)

m.c163 = Constraint(expr= - 0.05904*m.b66 + m.x450 <= 0)

m.c164 = Constraint(expr= - 0.05904*m.b67 + m.x451 <= 0)

m.c165 = Constraint(expr= - 0.05904*m.b68 + m.x452 <= 0)

m.c166 = Constraint(expr= - 0.05904*m.b69 + m.x453 <= 0)

m.c167 = Constraint(expr= - 0.05904*m.b70 + m.x454 <= 0)

m.c168 = Constraint(expr= - 0.05904*m.b71 + m.x455 <= 0)

m.c169 = Constraint(expr= - 0.05904*m.b72 + m.x456 <= 0)

m.c170 = Constraint(expr= - 3.24*m.b73 + m.x457 <= 0)

m.c171 = Constraint(expr= - 3.24*m.b74 + m.x458 <= 0)

m.c172 = Constraint(expr= - 3.24*m.b75 + m.x459 <= 0)

m.c173 = Constraint(expr= - 3.24*m.b76 + m.x460 <= 0)

m.c174 = Constraint(expr= - 3.24*m.b77 + m.x461 <= 0)

m.c175 = Constraint(expr= - 3.24*m.b78 + m.x462 <= 0)

m.c176 = Constraint(expr= - 3.24*m.b79 + m.x463 <= 0)

m.c177 = Constraint(expr= - 3.24*m.b80 + m.x464 <= 0)

m.c178 = Constraint(expr= - 3.24*m.b81 + m.x465 <= 0)

m.c179 = Constraint(expr= - 3.24*m.b82 + m.x466 <= 0)

m.c180 = Constraint(expr= - 3.24*m.b83 + m.x467 <= 0)

m.c181 = Constraint(expr= - 3.24*m.b84 + m.x468 <= 0)

m.c182 = Constraint(expr= - 3.24*m.b85 + m.x469 <= 0)

m.c183 = Constraint(expr= - 3.24*m.b86 + m.x470 <= 0)

m.c184 = Constraint(expr= - 3.24*m.b87 + m.x471 <= 0)

m.c185 = Constraint(expr= - 3.24*m.b88 + m.x472 <= 0)

m.c186 = Constraint(expr= - 3.24*m.b89 + m.x473 <= 0)

m.c187 = Constraint(expr= - 3.24*m.b90 + m.x474 <= 0)

m.c188 = Constraint(expr= - 3.24*m.b91 + m.x475 <= 0)

m.c189 = Constraint(expr= - 3.24*m.b92 + m.x476 <= 0)

m.c190 = Constraint(expr= - 3.24*m.b93 + m.x477 <= 0)

m.c191 = Constraint(expr= - 3.24*m.b94 + m.x478 <= 0)

m.c192 = Constraint(expr= - 3.24*m.b95 + m.x479 <= 0)

m.c193 = Constraint(expr= - 3.24*m.b96 + m.x480 <= 0)

m.c194 = Constraint(expr= - 0.605268*m.b1 + m.x385 >= 0)

m.c195 = Constraint(expr= - 0.605268*m.b2 + m.x386 >= 0)

m.c196 = Constraint(expr= - 0.605268*m.b3 + m.x387 >= 0)

m.c197 = Constraint(expr= - 0.605268*m.b4 + m.x388 >= 0)

m.c198 = Constraint(expr= - 0.605268*m.b5 + m.x389 >= 0)

m.c199 = Constraint(expr= - 0.605268*m.b6 + m.x390 >= 0)

m.c200 = Constraint(expr= - 0.605268*m.b7 + m.x391 >= 0)

m.c201 = Constraint(expr= - 0.605268*m.b8 + m.x392 >= 0)

m.c202 = Constraint(expr= - 0.605268*m.b9 + m.x393 >= 0)

m.c203 = Constraint(expr= - 0.605268*m.b10 + m.x394 >= 0)

m.c204 = Constraint(expr= - 0.605268*m.b11 + m.x395 >= 0)

m.c205 = Constraint(expr= - 0.605268*m.b12 + m.x396 >= 0)

m.c206 = Constraint(expr= - 0.605268*m.b13 + m.x397 >= 0)

m.c207 = Constraint(expr= - 0.605268*m.b14 + m.x398 >= 0)

m.c208 = Constraint(expr= - 0.605268*m.b15 + m.x399 >= 0)

m.c209 = Constraint(expr= - 0.605268*m.b16 + m.x400 >= 0)

m.c210 = Constraint(expr= - 0.605268*m.b17 + m.x401 >= 0)

m.c211 = Constraint(expr= - 0.605268*m.b18 + m.x402 >= 0)

m.c212 = Constraint(expr= - 0.605268*m.b19 + m.x403 >= 0)

m.c213 = Constraint(expr= - 0.605268*m.b20 + m.x404 >= 0)

m.c214 = Constraint(expr= - 0.605268*m.b21 + m.x405 >= 0)

m.c215 = Constraint(expr= - 0.605268*m.b22 + m.x406 >= 0)

m.c216 = Constraint(expr= - 0.605268*m.b23 + m.x407 >= 0)

m.c217 = Constraint(expr= - 0.605268*m.b24 + m.x408 >= 0)

m.c218 = Constraint(expr= - 0.37692*m.b25 + m.x409 >= 0)

m.c219 = Constraint(expr= - 0.37692*m.b26 + m.x410 >= 0)

m.c220 = Constraint(expr= - 0.37692*m.b27 + m.x411 >= 0)

m.c221 = Constraint(expr= - 0.37692*m.b28 + m.x412 >= 0)

m.c222 = Constraint(expr= - 0.37692*m.b29 + m.x413 >= 0)

m.c223 = Constraint(expr= - 0.37692*m.b30 + m.x414 >= 0)

m.c224 = Constraint(expr= - 0.37692*m.b31 + m.x415 >= 0)

m.c225 = Constraint(expr= - 0.37692*m.b32 + m.x416 >= 0)

m.c226 = Constraint(expr= - 0.37692*m.b33 + m.x417 >= 0)

m.c227 = Constraint(expr= - 0.37692*m.b34 + m.x418 >= 0)

m.c228 = Constraint(expr= - 0.37692*m.b35 + m.x419 >= 0)

m.c229 = Constraint(expr= - 0.37692*m.b36 + m.x420 >= 0)

m.c230 = Constraint(expr= - 0.37692*m.b37 + m.x421 >= 0)

m.c231 = Constraint(expr= - 0.37692*m.b38 + m.x422 >= 0)

m.c232 = Constraint(expr= - 0.37692*m.b39 + m.x423 >= 0)

m.c233 = Constraint(expr= - 0.37692*m.b40 + m.x424 >= 0)

m.c234 = Constraint(expr= - 0.37692*m.b41 + m.x425 >= 0)

m.c235 = Constraint(expr= - 0.37692*m.b42 + m.x426 >= 0)

m.c236 = Constraint(expr= - 0.37692*m.b43 + m.x427 >= 0)

m.c237 = Constraint(expr= - 0.37692*m.b44 + m.x428 >= 0)

m.c238 = Constraint(expr= - 0.37692*m.b45 + m.x429 >= 0)

m.c239 = Constraint(expr= - 0.37692*m.b46 + m.x430 >= 0)

m.c240 = Constraint(expr= - 0.37692*m.b47 + m.x431 >= 0)

m.c241 = Constraint(expr= - 0.37692*m.b48 + m.x432 >= 0)

m.c242 = Constraint(expr= - 0.0108*m.b49 + m.x433 >= 0)

m.c243 = Constraint(expr= - 0.0108*m.b50 + m.x434 >= 0)

m.c244 = Constraint(expr= - 0.0108*m.b51 + m.x435 >= 0)

m.c245 = Constraint(expr= - 0.0108*m.b52 + m.x436 >= 0)

m.c246 = Constraint(expr= - 0.0108*m.b53 + m.x437 >= 0)

m.c247 = Constraint(expr= - 0.0108*m.b54 + m.x438 >= 0)

m.c248 = Constraint(expr= - 0.0108*m.b55 + m.x439 >= 0)

m.c249 = Constraint(expr= - 0.0108*m.b56 + m.x440 >= 0)

m.c250 = Constraint(expr= - 0.0108*m.b57 + m.x441 >= 0)

m.c251 = Constraint(expr= - 0.0108*m.b58 + m.x442 >= 0)

m.c252 = Constraint(expr= - 0.0108*m.b59 + m.x443 >= 0)

m.c253 = Constraint(expr= - 0.0108*m.b60 + m.x444 >= 0)

m.c254 = Constraint(expr= - 0.0108*m.b61 + m.x445 >= 0)

m.c255 = Constraint(expr= - 0.0108*m.b62 + m.x446 >= 0)

m.c256 = Constraint(expr= - 0.0108*m.b63 + m.x447 >= 0)

m.c257 = Constraint(expr= - 0.0108*m.b64 + m.x448 >= 0)

m.c258 = Constraint(expr= - 0.0108*m.b65 + m.x449 >= 0)

m.c259 = Constraint(expr= - 0.0108*m.b66 + m.x450 >= 0)

m.c260 = Constraint(expr= - 0.0108*m.b67 + m.x451 >= 0)

m.c261 = Constraint(expr= - 0.0108*m.b68 + m.x452 >= 0)

m.c262 = Constraint(expr= - 0.0108*m.b69 + m.x453 >= 0)

m.c263 = Constraint(expr= - 0.0108*m.b70 + m.x454 >= 0)

m.c264 = Constraint(expr= - 0.0108*m.b71 + m.x455 >= 0)

m.c265 = Constraint(expr= - 0.0108*m.b72 + m.x456 >= 0)

m.c266 = Constraint(expr= - 0.376812*m.b73 + m.x457 >= 0)

m.c267 = Constraint(expr= - 0.376812*m.b74 + m.x458 >= 0)

m.c268 = Constraint(expr= - 0.376812*m.b75 + m.x459 >= 0)

m.c269 = Constraint(expr= - 0.376812*m.b76 + m.x460 >= 0)

m.c270 = Constraint(expr= - 0.376812*m.b77 + m.x461 >= 0)

m.c271 = Constraint(expr= - 0.376812*m.b78 + m.x462 >= 0)

m.c272 = Constraint(expr= - 0.376812*m.b79 + m.x463 >= 0)

m.c273 = Constraint(expr= - 0.376812*m.b80 + m.x464 >= 0)

m.c274 = Constraint(expr= - 0.376812*m.b81 + m.x465 >= 0)

m.c275 = Constraint(expr= - 0.376812*m.b82 + m.x466 >= 0)

m.c276 = Constraint(expr= - 0.376812*m.b83 + m.x467 >= 0)

m.c277 = Constraint(expr= - 0.376812*m.b84 + m.x468 >= 0)

m.c278 = Constraint(expr= - 0.376812*m.b85 + m.x469 >= 0)

m.c279 = Constraint(expr= - 0.376812*m.b86 + m.x470 >= 0)

m.c280 = Constraint(expr= - 0.376812*m.b87 + m.x471 >= 0)

m.c281 = Constraint(expr= - 0.376812*m.b88 + m.x472 >= 0)

m.c282 = Constraint(expr= - 0.376812*m.b89 + m.x473 >= 0)

m.c283 = Constraint(expr= - 0.376812*m.b90 + m.x474 >= 0)

m.c284 = Constraint(expr= - 0.376812*m.b91 + m.x475 >= 0)

m.c285 = Constraint(expr= - 0.376812*m.b92 + m.x476 >= 0)

m.c286 = Constraint(expr= - 0.376812*m.b93 + m.x477 >= 0)

m.c287 = Constraint(expr= - 0.376812*m.b94 + m.x478 >= 0)

m.c288 = Constraint(expr= - 0.376812*m.b95 + m.x479 >= 0)

m.c289 = Constraint(expr= - 0.376812*m.b96 + m.x480 >= 0)

m.c290 = Constraint(expr= - 28*m.b1 + m.x193 >= 0)

m.c291 = Constraint(expr= - 28*m.b2 + m.x194 >= 0)

m.c292 = Constraint(expr= - 28*m.b3 + m.x195 >= 0)

m.c293 = Constraint(expr= - 28*m.b4 + m.x196 >= 0)

m.c294 = Constraint(expr= - 28*m.b5 + m.x197 >= 0)

m.c295 = Constraint(expr= - 28*m.b6 + m.x198 >= 0)

m.c296 = Constraint(expr= - 28*m.b7 + m.x199 >= 0)

m.c297 = Constraint(expr= - 28*m.b8 + m.x200 >= 0)

m.c298 = Constraint(expr= - 28*m.b9 + m.x201 >= 0)

m.c299 = Constraint(expr= - 28*m.b10 + m.x202 >= 0)

m.c300 = Constraint(expr= - 28*m.b11 + m.x203 >= 0)

m.c301 = Constraint(expr= - 28*m.b12 + m.x204 >= 0)

m.c302 = Constraint(expr= - 28*m.b13 + m.x205 >= 0)

m.c303 = Constraint(expr= - 28*m.b14 + m.x206 >= 0)

m.c304 = Constraint(expr= - 28*m.b15 + m.x207 >= 0)

m.c305 = Constraint(expr= - 28*m.b16 + m.x208 >= 0)

m.c306 = Constraint(expr= - 28*m.b17 + m.x209 >= 0)

m.c307 = Constraint(expr= - 28*m.b18 + m.x210 >= 0)

m.c308 = Constraint(expr= - 28*m.b19 + m.x211 >= 0)

m.c309 = Constraint(expr= - 28*m.b20 + m.x212 >= 0)

m.c310 = Constraint(expr= - 28*m.b21 + m.x213 >= 0)

m.c311 = Constraint(expr= - 28*m.b22 + m.x214 >= 0)

m.c312 = Constraint(expr= - 28*m.b23 + m.x215 >= 0)

m.c313 = Constraint(expr= - 28*m.b24 + m.x216 >= 0)

m.c314 = Constraint(expr= - 29.99*m.b25 + m.x217 >= 0)

m.c315 = Constraint(expr= - 29.99*m.b26 + m.x218 >= 0)

m.c316 = Constraint(expr= - 29.99*m.b27 + m.x219 >= 0)

m.c317 = Constraint(expr= - 29.99*m.b28 + m.x220 >= 0)

m.c318 = Constraint(expr= - 29.99*m.b29 + m.x221 >= 0)

m.c319 = Constraint(expr= - 29.99*m.b30 + m.x222 >= 0)

m.c320 = Constraint(expr= - 29.99*m.b31 + m.x223 >= 0)

m.c321 = Constraint(expr= - 29.99*m.b32 + m.x224 >= 0)

m.c322 = Constraint(expr= - 29.99*m.b33 + m.x225 >= 0)

m.c323 = Constraint(expr= - 29.99*m.b34 + m.x226 >= 0)

m.c324 = Constraint(expr= - 29.99*m.b35 + m.x227 >= 0)

m.c325 = Constraint(expr= - 29.99*m.b36 + m.x228 >= 0)

m.c326 = Constraint(expr= - 29.99*m.b37 + m.x229 >= 0)

m.c327 = Constraint(expr= - 29.99*m.b38 + m.x230 >= 0)

m.c328 = Constraint(expr= - 29.99*m.b39 + m.x231 >= 0)

m.c329 = Constraint(expr= - 29.99*m.b40 + m.x232 >= 0)

m.c330 = Constraint(expr= - 29.99*m.b41 + m.x233 >= 0)

m.c331 = Constraint(expr= - 29.99*m.b42 + m.x234 >= 0)

m.c332 = Constraint(expr= - 29.99*m.b43 + m.x235 >= 0)

m.c333 = Constraint(expr= - 29.99*m.b44 + m.x236 >= 0)

m.c334 = Constraint(expr= - 29.99*m.b45 + m.x237 >= 0)

m.c335 = Constraint(expr= - 29.99*m.b46 + m.x238 >= 0)

m.c336 = Constraint(expr= - 29.99*m.b47 + m.x239 >= 0)

m.c337 = Constraint(expr= - 29.99*m.b48 + m.x240 >= 0)

m.c338 = Constraint(expr= - 10.67*m.b49 + m.x241 >= 0)

m.c339 = Constraint(expr= - 10.67*m.b50 + m.x242 >= 0)

m.c340 = Constraint(expr= - 10.67*m.b51 + m.x243 >= 0)

m.c341 = Constraint(expr= - 10.67*m.b52 + m.x244 >= 0)

m.c342 = Constraint(expr= - 10.67*m.b53 + m.x245 >= 0)

m.c343 = Constraint(expr= - 10.67*m.b54 + m.x246 >= 0)

m.c344 = Constraint(expr= - 10.67*m.b55 + m.x247 >= 0)

m.c345 = Constraint(expr= - 10.67*m.b56 + m.x248 >= 0)

m.c346 = Constraint(expr= - 10.67*m.b57 + m.x249 >= 0)

m.c347 = Constraint(expr= - 10.67*m.b58 + m.x250 >= 0)

m.c348 = Constraint(expr= - 10.67*m.b59 + m.x251 >= 0)

m.c349 = Constraint(expr= - 10.67*m.b60 + m.x252 >= 0)

m.c350 = Constraint(expr= - 10.67*m.b61 + m.x253 >= 0)

m.c351 = Constraint(expr= - 10.67*m.b62 + m.x254 >= 0)

m.c352 = Constraint(expr= - 10.67*m.b63 + m.x255 >= 0)

m.c353 = Constraint(expr= - 10.67*m.b64 + m.x256 >= 0)

m.c354 = Constraint(expr= - 10.67*m.b65 + m.x257 >= 0)

m.c355 = Constraint(expr= - 10.67*m.b66 + m.x258 >= 0)

m.c356 = Constraint(expr= - 10.67*m.b67 + m.x259 >= 0)

m.c357 = Constraint(expr= - 10.67*m.b68 + m.x260 >= 0)

m.c358 = Constraint(expr= - 10.67*m.b69 + m.x261 >= 0)

m.c359 = Constraint(expr= - 10.67*m.b70 + m.x262 >= 0)

m.c360 = Constraint(expr= - 10.67*m.b71 + m.x263 >= 0)

m.c361 = Constraint(expr= - 10.67*m.b72 + m.x264 >= 0)

m.c362 = Constraint(expr= - 24.99*m.b73 + m.x265 >= 0)

m.c363 = Constraint(expr= - 24.99*m.b74 + m.x266 >= 0)

m.c364 = Constraint(expr= - 24.99*m.b75 + m.x267 >= 0)

m.c365 = Constraint(expr= - 24.99*m.b76 + m.x268 >= 0)

m.c366 = Constraint(expr= - 24.99*m.b77 + m.x269 >= 0)

m.c367 = Constraint(expr= - 24.99*m.b78 + m.x270 >= 0)

m.c368 = Constraint(expr= - 24.99*m.b79 + m.x271 >= 0)

m.c369 = Constraint(expr= - 24.99*m.b80 + m.x272 >= 0)

m.c370 = Constraint(expr= - 24.99*m.b81 + m.x273 >= 0)

m.c371 = Constraint(expr= - 24.99*m.b82 + m.x274 >= 0)

m.c372 = Constraint(expr= - 24.99*m.b83 + m.x275 >= 0)

m.c373 = Constraint(expr= - 24.99*m.b84 + m.x276 >= 0)

m.c374 = Constraint(expr= - 24.99*m.b85 + m.x277 >= 0)

m.c375 = Constraint(expr= - 24.99*m.b86 + m.x278 >= 0)

m.c376 = Constraint(expr= - 24.99*m.b87 + m.x279 >= 0)

m.c377 = Constraint(expr= - 24.99*m.b88 + m.x280 >= 0)

m.c378 = Constraint(expr= - 24.99*m.b89 + m.x281 >= 0)

m.c379 = Constraint(expr= - 24.99*m.b90 + m.x282 >= 0)

m.c380 = Constraint(expr= - 24.99*m.b91 + m.x283 >= 0)

m.c381 = Constraint(expr= - 24.99*m.b92 + m.x284 >= 0)

m.c382 = Constraint(expr= - 24.99*m.b93 + m.x285 >= 0)

m.c383 = Constraint(expr= - 24.99*m.b94 + m.x286 >= 0)

m.c384 = Constraint(expr= - 24.99*m.b95 + m.x287 >= 0)

m.c385 = Constraint(expr= - 24.99*m.b96 + m.x288 >= 0)

m.c386 = Constraint(expr= - 188.08*m.b1 + m.x193 <= 0)

m.c387 = Constraint(expr= - 188.08*m.b2 + m.x194 <= 0)

m.c388 = Constraint(expr= - 188.08*m.b3 + m.x195 <= 0)

m.c389 = Constraint(expr= - 188.08*m.b4 + m.x196 <= 0)

m.c390 = Constraint(expr= - 188.08*m.b5 + m.x197 <= 0)

m.c391 = Constraint(expr= - 188.08*m.b6 + m.x198 <= 0)

m.c392 = Constraint(expr= - 188.08*m.b7 + m.x199 <= 0)

m.c393 = Constraint(expr= - 188.08*m.b8 + m.x200 <= 0)

m.c394 = Constraint(expr= - 188.08*m.b9 + m.x201 <= 0)

m.c395 = Constraint(expr= - 188.08*m.b10 + m.x202 <= 0)

m.c396 = Constraint(expr= - 188.08*m.b11 + m.x203 <= 0)

m.c397 = Constraint(expr= - 188.08*m.b12 + m.x204 <= 0)

m.c398 = Constraint(expr= - 188.08*m.b13 + m.x205 <= 0)

m.c399 = Constraint(expr= - 188.08*m.b14 + m.x206 <= 0)

m.c400 = Constraint(expr= - 188.08*m.b15 + m.x207 <= 0)

m.c401 = Constraint(expr= - 188.08*m.b16 + m.x208 <= 0)

m.c402 = Constraint(expr= - 188.08*m.b17 + m.x209 <= 0)

m.c403 = Constraint(expr= - 188.08*m.b18 + m.x210 <= 0)

m.c404 = Constraint(expr= - 188.08*m.b19 + m.x211 <= 0)

m.c405 = Constraint(expr= - 188.08*m.b20 + m.x212 <= 0)

m.c406 = Constraint(expr= - 188.08*m.b21 + m.x213 <= 0)

m.c407 = Constraint(expr= - 188.08*m.b22 + m.x214 <= 0)

m.c408 = Constraint(expr= - 188.08*m.b23 + m.x215 <= 0)

m.c409 = Constraint(expr= - 188.08*m.b24 + m.x216 <= 0)

m.c410 = Constraint(expr= - 237.14*m.b25 + m.x217 <= 0)

m.c411 = Constraint(expr= - 237.14*m.b26 + m.x218 <= 0)

m.c412 = Constraint(expr= - 237.14*m.b27 + m.x219 <= 0)

m.c413 = Constraint(expr= - 237.14*m.b28 + m.x220 <= 0)

m.c414 = Constraint(expr= - 237.14*m.b29 + m.x221 <= 0)

m.c415 = Constraint(expr= - 237.14*m.b30 + m.x222 <= 0)

m.c416 = Constraint(expr= - 237.14*m.b31 + m.x223 <= 0)

m.c417 = Constraint(expr= - 237.14*m.b32 + m.x224 <= 0)

m.c418 = Constraint(expr= - 237.14*m.b33 + m.x225 <= 0)

m.c419 = Constraint(expr= - 237.14*m.b34 + m.x226 <= 0)

m.c420 = Constraint(expr= - 237.14*m.b35 + m.x227 <= 0)

m.c421 = Constraint(expr= - 237.14*m.b36 + m.x228 <= 0)

m.c422 = Constraint(expr= - 237.14*m.b37 + m.x229 <= 0)

m.c423 = Constraint(expr= - 237.14*m.b38 + m.x230 <= 0)

m.c424 = Constraint(expr= - 237.14*m.b39 + m.x231 <= 0)

m.c425 = Constraint(expr= - 237.14*m.b40 + m.x232 <= 0)

m.c426 = Constraint(expr= - 237.14*m.b41 + m.x233 <= 0)

m.c427 = Constraint(expr= - 237.14*m.b42 + m.x234 <= 0)

m.c428 = Constraint(expr= - 237.14*m.b43 + m.x235 <= 0)

m.c429 = Constraint(expr= - 237.14*m.b44 + m.x236 <= 0)

m.c430 = Constraint(expr= - 237.14*m.b45 + m.x237 <= 0)

m.c431 = Constraint(expr= - 237.14*m.b46 + m.x238 <= 0)

m.c432 = Constraint(expr= - 237.14*m.b47 + m.x239 <= 0)

m.c433 = Constraint(expr= - 237.14*m.b48 + m.x240 <= 0)

m.c434 = Constraint(expr= - 60*m.b49 + m.x241 <= 0)

m.c435 = Constraint(expr= - 60*m.b50 + m.x242 <= 0)

m.c436 = Constraint(expr= - 60*m.b51 + m.x243 <= 0)

m.c437 = Constraint(expr= - 60*m.b52 + m.x244 <= 0)

m.c438 = Constraint(expr= - 60*m.b53 + m.x245 <= 0)

m.c439 = Constraint(expr= - 60*m.b54 + m.x246 <= 0)

m.c440 = Constraint(expr= - 60*m.b55 + m.x247 <= 0)

m.c441 = Constraint(expr= - 60*m.b56 + m.x248 <= 0)

m.c442 = Constraint(expr= - 60*m.b57 + m.x249 <= 0)

m.c443 = Constraint(expr= - 60*m.b58 + m.x250 <= 0)

m.c444 = Constraint(expr= - 60*m.b59 + m.x251 <= 0)

m.c445 = Constraint(expr= - 60*m.b60 + m.x252 <= 0)

m.c446 = Constraint(expr= - 60*m.b61 + m.x253 <= 0)

m.c447 = Constraint(expr= - 60*m.b62 + m.x254 <= 0)

m.c448 = Constraint(expr= - 60*m.b63 + m.x255 <= 0)

m.c449 = Constraint(expr= - 60*m.b64 + m.x256 <= 0)

m.c450 = Constraint(expr= - 60*m.b65 + m.x257 <= 0)

m.c451 = Constraint(expr= - 60*m.b66 + m.x258 <= 0)

m.c452 = Constraint(expr= - 60*m.b67 + m.x259 <= 0)

m.c453 = Constraint(expr= - 60*m.b68 + m.x260 <= 0)

m.c454 = Constraint(expr= - 60*m.b69 + m.x261 <= 0)

m.c455 = Constraint(expr= - 60*m.b70 + m.x262 <= 0)

m.c456 = Constraint(expr= - 60*m.b71 + m.x263 <= 0)

m.c457 = Constraint(expr= - 60*m.b72 + m.x264 <= 0)

m.c458 = Constraint(expr= - 185.99*m.b73 + m.x265 <= 0)

m.c459 = Constraint(expr= - 185.99*m.b74 + m.x266 <= 0)

m.c460 = Constraint(expr= - 185.99*m.b75 + m.x267 <= 0)

m.c461 = Constraint(expr= - 185.99*m.b76 + m.x268 <= 0)

m.c462 = Constraint(expr= - 185.99*m.b77 + m.x269 <= 0)

m.c463 = Constraint(expr= - 185.99*m.b78 + m.x270 <= 0)

m.c464 = Constraint(expr= - 185.99*m.b79 + m.x271 <= 0)

m.c465 = Constraint(expr= - 185.99*m.b80 + m.x272 <= 0)

m.c466 = Constraint(expr= - 185.99*m.b81 + m.x273 <= 0)

m.c467 = Constraint(expr= - 185.99*m.b82 + m.x274 <= 0)

m.c468 = Constraint(expr= - 185.99*m.b83 + m.x275 <= 0)

m.c469 = Constraint(expr= - 185.99*m.b84 + m.x276 <= 0)

m.c470 = Constraint(expr= - 185.99*m.b85 + m.x277 <= 0)

m.c471 = Constraint(expr= - 185.99*m.b86 + m.x278 <= 0)

m.c472 = Constraint(expr= - 185.99*m.b87 + m.x279 <= 0)

m.c473 = Constraint(expr= - 185.99*m.b88 + m.x280 <= 0)

m.c474 = Constraint(expr= - 185.99*m.b89 + m.x281 <= 0)

m.c475 = Constraint(expr= - 185.99*m.b90 + m.x282 <= 0)

m.c476 = Constraint(expr= - 185.99*m.b91 + m.x283 <= 0)

m.c477 = Constraint(expr= - 185.99*m.b92 + m.x284 <= 0)

m.c478 = Constraint(expr= - 185.99*m.b93 + m.x285 <= 0)

m.c479 = Constraint(expr= - 185.99*m.b94 + m.x286 <= 0)

m.c480 = Constraint(expr= - 185.99*m.b95 + m.x287 <= 0)

m.c481 = Constraint(expr= - 185.99*m.b96 + m.x288 <= 0)

m.c482 = Constraint(expr=   m.x385 - m.x386 <= 2.0601)

m.c483 = Constraint(expr=   m.x386 - m.x387 <= 2.0601)

m.c484 = Constraint(expr=   m.x387 - m.x388 <= 2.0601)

m.c485 = Constraint(expr=   m.x388 - m.x389 <= 2.0601)

m.c486 = Constraint(expr=   m.x389 - m.x390 <= 2.0601)

m.c487 = Constraint(expr=   m.x390 - m.x391 <= 2.0601)

m.c488 = Constraint(expr=   m.x391 - m.x392 <= 2.0601)

m.c489 = Constraint(expr=   m.x392 - m.x393 <= 2.0601)

m.c490 = Constraint(expr=   m.x393 - m.x394 <= 2.0601)

m.c491 = Constraint(expr=   m.x394 - m.x395 <= 2.0601)

m.c492 = Constraint(expr=   m.x395 - m.x396 <= 2.0601)

m.c493 = Constraint(expr=   m.x396 - m.x397 <= 2.0601)

m.c494 = Constraint(expr=   m.x397 - m.x398 <= 2.0601)

m.c495 = Constraint(expr=   m.x398 - m.x399 <= 2.0601)

m.c496 = Constraint(expr=   m.x399 - m.x400 <= 2.0601)

m.c497 = Constraint(expr=   m.x400 - m.x401 <= 2.0601)

m.c498 = Constraint(expr=   m.x401 - m.x402 <= 2.0601)

m.c499 = Constraint(expr=   m.x402 - m.x403 <= 2.0601)

m.c500 = Constraint(expr=   m.x403 - m.x404 <= 2.0601)

m.c501 = Constraint(expr=   m.x404 - m.x405 <= 2.0601)

m.c502 = Constraint(expr=   m.x405 - m.x406 <= 2.0601)

m.c503 = Constraint(expr=   m.x406 - m.x407 <= 2.0601)

m.c504 = Constraint(expr=   m.x407 - m.x408 <= 2.0601)

m.c505 = Constraint(expr=   m.x409 - m.x410 <= 1.944)

m.c506 = Constraint(expr=   m.x410 - m.x411 <= 1.944)

m.c507 = Constraint(expr=   m.x411 - m.x412 <= 1.944)

m.c508 = Constraint(expr=   m.x412 - m.x413 <= 1.944)

m.c509 = Constraint(expr=   m.x413 - m.x414 <= 1.944)

m.c510 = Constraint(expr=   m.x414 - m.x415 <= 1.944)

m.c511 = Constraint(expr=   m.x415 - m.x416 <= 1.944)

m.c512 = Constraint(expr=   m.x416 - m.x417 <= 1.944)

m.c513 = Constraint(expr=   m.x417 - m.x418 <= 1.944)

m.c514 = Constraint(expr=   m.x418 - m.x419 <= 1.944)

m.c515 = Constraint(expr=   m.x419 - m.x420 <= 1.944)

m.c516 = Constraint(expr=   m.x420 - m.x421 <= 1.944)

m.c517 = Constraint(expr=   m.x421 - m.x422 <= 1.944)

m.c518 = Constraint(expr=   m.x422 - m.x423 <= 1.944)

m.c519 = Constraint(expr=   m.x423 - m.x424 <= 1.944)

m.c520 = Constraint(expr=   m.x424 - m.x425 <= 1.944)

m.c521 = Constraint(expr=   m.x425 - m.x426 <= 1.944)

m.c522 = Constraint(expr=   m.x426 - m.x427 <= 1.944)

m.c523 = Constraint(expr=   m.x427 - m.x428 <= 1.944)

m.c524 = Constraint(expr=   m.x428 - m.x429 <= 1.944)

m.c525 = Constraint(expr=   m.x429 - m.x430 <= 1.944)

m.c526 = Constraint(expr=   m.x430 - m.x431 <= 1.944)

m.c527 = Constraint(expr=   m.x431 - m.x432 <= 1.944)

m.c528 = Constraint(expr=   m.x433 - m.x434 <= 0.02952)

m.c529 = Constraint(expr=   m.x434 - m.x435 <= 0.02952)

m.c530 = Constraint(expr=   m.x435 - m.x436 <= 0.02952)

m.c531 = Constraint(expr=   m.x436 - m.x437 <= 0.02952)

m.c532 = Constraint(expr=   m.x437 - m.x438 <= 0.02952)

m.c533 = Constraint(expr=   m.x438 - m.x439 <= 0.02952)

m.c534 = Constraint(expr=   m.x439 - m.x440 <= 0.02952)

m.c535 = Constraint(expr=   m.x440 - m.x441 <= 0.02952)

m.c536 = Constraint(expr=   m.x441 - m.x442 <= 0.02952)

m.c537 = Constraint(expr=   m.x442 - m.x443 <= 0.02952)

m.c538 = Constraint(expr=   m.x443 - m.x444 <= 0.02952)

m.c539 = Constraint(expr=   m.x444 - m.x445 <= 0.02952)

m.c540 = Constraint(expr=   m.x445 - m.x446 <= 0.02952)

m.c541 = Constraint(expr=   m.x446 - m.x447 <= 0.02952)

m.c542 = Constraint(expr=   m.x447 - m.x448 <= 0.02952)

m.c543 = Constraint(expr=   m.x448 - m.x449 <= 0.02952)

m.c544 = Constraint(expr=   m.x449 - m.x450 <= 0.02952)

m.c545 = Constraint(expr=   m.x450 - m.x451 <= 0.02952)

m.c546 = Constraint(expr=   m.x451 - m.x452 <= 0.02952)

m.c547 = Constraint(expr=   m.x452 - m.x453 <= 0.02952)

m.c548 = Constraint(expr=   m.x453 - m.x454 <= 0.02952)

m.c549 = Constraint(expr=   m.x454 - m.x455 <= 0.02952)

m.c550 = Constraint(expr=   m.x455 - m.x456 <= 0.02952)

m.c551 = Constraint(expr=   m.x457 - m.x458 <= 1.62)

m.c552 = Constraint(expr=   m.x458 - m.x459 <= 1.62)

m.c553 = Constraint(expr=   m.x459 - m.x460 <= 1.62)

m.c554 = Constraint(expr=   m.x460 - m.x461 <= 1.62)

m.c555 = Constraint(expr=   m.x461 - m.x462 <= 1.62)

m.c556 = Constraint(expr=   m.x462 - m.x463 <= 1.62)

m.c557 = Constraint(expr=   m.x463 - m.x464 <= 1.62)

m.c558 = Constraint(expr=   m.x464 - m.x465 <= 1.62)

m.c559 = Constraint(expr=   m.x465 - m.x466 <= 1.62)

m.c560 = Constraint(expr=   m.x466 - m.x467 <= 1.62)

m.c561 = Constraint(expr=   m.x467 - m.x468 <= 1.62)

m.c562 = Constraint(expr=   m.x468 - m.x469 <= 1.62)

m.c563 = Constraint(expr=   m.x469 - m.x470 <= 1.62)

m.c564 = Constraint(expr=   m.x470 - m.x471 <= 1.62)

m.c565 = Constraint(expr=   m.x471 - m.x472 <= 1.62)

m.c566 = Constraint(expr=   m.x472 - m.x473 <= 1.62)

m.c567 = Constraint(expr=   m.x473 - m.x474 <= 1.62)

m.c568 = Constraint(expr=   m.x474 - m.x475 <= 1.62)

m.c569 = Constraint(expr=   m.x475 - m.x476 <= 1.62)

m.c570 = Constraint(expr=   m.x476 - m.x477 <= 1.62)

m.c571 = Constraint(expr=   m.x477 - m.x478 <= 1.62)

m.c572 = Constraint(expr=   m.x478 - m.x479 <= 1.62)

m.c573 = Constraint(expr=   m.x479 - m.x480 <= 1.62)

m.c574 = Constraint(expr= - m.x385 + m.x386 <= 2.0601)

m.c575 = Constraint(expr= - m.x386 + m.x387 <= 2.0601)

m.c576 = Constraint(expr= - m.x387 + m.x388 <= 2.0601)

m.c577 = Constraint(expr= - m.x388 + m.x389 <= 2.0601)

m.c578 = Constraint(expr= - m.x389 + m.x390 <= 2.0601)

m.c579 = Constraint(expr= - m.x390 + m.x391 <= 2.0601)

m.c580 = Constraint(expr= - m.x391 + m.x392 <= 2.0601)

m.c581 = Constraint(expr= - m.x392 + m.x393 <= 2.0601)

m.c582 = Constraint(expr= - m.x393 + m.x394 <= 2.0601)

m.c583 = Constraint(expr= - m.x394 + m.x395 <= 2.0601)

m.c584 = Constraint(expr= - m.x395 + m.x396 <= 2.0601)

m.c585 = Constraint(expr= - m.x396 + m.x397 <= 2.0601)

m.c586 = Constraint(expr= - m.x397 + m.x398 <= 2.0601)

m.c587 = Constraint(expr= - m.x398 + m.x399 <= 2.0601)

m.c588 = Constraint(expr= - m.x399 + m.x400 <= 2.0601)

m.c589 = Constraint(expr= - m.x400 + m.x401 <= 2.0601)

m.c590 = Constraint(expr= - m.x401 + m.x402 <= 2.0601)

m.c591 = Constraint(expr= - m.x402 + m.x403 <= 2.0601)

m.c592 = Constraint(expr= - m.x403 + m.x404 <= 2.0601)

m.c593 = Constraint(expr= - m.x404 + m.x405 <= 2.0601)

m.c594 = Constraint(expr= - m.x405 + m.x406 <= 2.0601)

m.c595 = Constraint(expr= - m.x406 + m.x407 <= 2.0601)

m.c596 = Constraint(expr= - m.x407 + m.x408 <= 2.0601)

m.c597 = Constraint(expr= - m.x409 + m.x410 <= 1.944)

m.c598 = Constraint(expr= - m.x410 + m.x411 <= 1.944)

m.c599 = Constraint(expr= - m.x411 + m.x412 <= 1.944)

m.c600 = Constraint(expr= - m.x412 + m.x413 <= 1.944)

m.c601 = Constraint(expr= - m.x413 + m.x414 <= 1.944)

m.c602 = Constraint(expr= - m.x414 + m.x415 <= 1.944)

m.c603 = Constraint(expr= - m.x415 + m.x416 <= 1.944)

m.c604 = Constraint(expr= - m.x416 + m.x417 <= 1.944)

m.c605 = Constraint(expr= - m.x417 + m.x418 <= 1.944)

m.c606 = Constraint(expr= - m.x418 + m.x419 <= 1.944)

m.c607 = Constraint(expr= - m.x419 + m.x420 <= 1.944)

m.c608 = Constraint(expr= - m.x420 + m.x421 <= 1.944)

m.c609 = Constraint(expr= - m.x421 + m.x422 <= 1.944)

m.c610 = Constraint(expr= - m.x422 + m.x423 <= 1.944)

m.c611 = Constraint(expr= - m.x423 + m.x424 <= 1.944)

m.c612 = Constraint(expr= - m.x424 + m.x425 <= 1.944)

m.c613 = Constraint(expr= - m.x425 + m.x426 <= 1.944)

m.c614 = Constraint(expr= - m.x426 + m.x427 <= 1.944)

m.c615 = Constraint(expr= - m.x427 + m.x428 <= 1.944)

m.c616 = Constraint(expr= - m.x428 + m.x429 <= 1.944)

m.c617 = Constraint(expr= - m.x429 + m.x430 <= 1.944)

m.c618 = Constraint(expr= - m.x430 + m.x431 <= 1.944)

m.c619 = Constraint(expr= - m.x431 + m.x432 <= 1.944)

m.c620 = Constraint(expr= - m.x433 + m.x434 <= 0.02952)

m.c621 = Constraint(expr= - m.x434 + m.x435 <= 0.02952)

m.c622 = Constraint(expr= - m.x435 + m.x436 <= 0.02952)

m.c623 = Constraint(expr= - m.x436 + m.x437 <= 0.02952)

m.c624 = Constraint(expr= - m.x437 + m.x438 <= 0.02952)

m.c625 = Constraint(expr= - m.x438 + m.x439 <= 0.02952)

m.c626 = Constraint(expr= - m.x439 + m.x440 <= 0.02952)

m.c627 = Constraint(expr= - m.x440 + m.x441 <= 0.02952)

m.c628 = Constraint(expr= - m.x441 + m.x442 <= 0.02952)

m.c629 = Constraint(expr= - m.x442 + m.x443 <= 0.02952)

m.c630 = Constraint(expr= - m.x443 + m.x444 <= 0.02952)

m.c631 = Constraint(expr= - m.x444 + m.x445 <= 0.02952)

m.c632 = Constraint(expr= - m.x445 + m.x446 <= 0.02952)

m.c633 = Constraint(expr= - m.x446 + m.x447 <= 0.02952)

m.c634 = Constraint(expr= - m.x447 + m.x448 <= 0.02952)

m.c635 = Constraint(expr= - m.x448 + m.x449 <= 0.02952)

m.c636 = Constraint(expr= - m.x449 + m.x450 <= 0.02952)

m.c637 = Constraint(expr= - m.x450 + m.x451 <= 0.02952)

m.c638 = Constraint(expr= - m.x451 + m.x452 <= 0.02952)

m.c639 = Constraint(expr= - m.x452 + m.x453 <= 0.02952)

m.c640 = Constraint(expr= - m.x453 + m.x454 <= 0.02952)

m.c641 = Constraint(expr= - m.x454 + m.x455 <= 0.02952)

m.c642 = Constraint(expr= - m.x455 + m.x456 <= 0.02952)

m.c643 = Constraint(expr= - m.x457 + m.x458 <= 1.62)

m.c644 = Constraint(expr= - m.x458 + m.x459 <= 1.62)

m.c645 = Constraint(expr= - m.x459 + m.x460 <= 1.62)

m.c646 = Constraint(expr= - m.x460 + m.x461 <= 1.62)

m.c647 = Constraint(expr= - m.x461 + m.x462 <= 1.62)

m.c648 = Constraint(expr= - m.x462 + m.x463 <= 1.62)

m.c649 = Constraint(expr= - m.x463 + m.x464 <= 1.62)

m.c650 = Constraint(expr= - m.x464 + m.x465 <= 1.62)

m.c651 = Constraint(expr= - m.x465 + m.x466 <= 1.62)

m.c652 = Constraint(expr= - m.x466 + m.x467 <= 1.62)

m.c653 = Constraint(expr= - m.x467 + m.x468 <= 1.62)

m.c654 = Constraint(expr= - m.x468 + m.x469 <= 1.62)

m.c655 = Constraint(expr= - m.x469 + m.x470 <= 1.62)

m.c656 = Constraint(expr= - m.x470 + m.x471 <= 1.62)

m.c657 = Constraint(expr= - m.x471 + m.x472 <= 1.62)

m.c658 = Constraint(expr= - m.x472 + m.x473 <= 1.62)

m.c659 = Constraint(expr= - m.x473 + m.x474 <= 1.62)

m.c660 = Constraint(expr= - m.x474 + m.x475 <= 1.62)

m.c661 = Constraint(expr= - m.x475 + m.x476 <= 1.62)

m.c662 = Constraint(expr= - m.x476 + m.x477 <= 1.62)

m.c663 = Constraint(expr= - m.x477 + m.x478 <= 1.62)

m.c664 = Constraint(expr= - m.x478 + m.x479 <= 1.62)

m.c665 = Constraint(expr= - m.x479 + m.x480 <= 1.62)

m.c666 = Constraint(expr= - m.b1 + m.b97 >= 0)

m.c667 = Constraint(expr=   m.b1 - m.b2 + m.b98 >= 0)

m.c668 = Constraint(expr=   m.b2 - m.b3 + m.b99 >= 0)

m.c669 = Constraint(expr=   m.b3 - m.b4 + m.b100 >= 0)

m.c670 = Constraint(expr=   m.b4 - m.b5 + m.b101 >= 0)

m.c671 = Constraint(expr=   m.b5 - m.b6 + m.b102 >= 0)

m.c672 = Constraint(expr=   m.b6 - m.b7 + m.b103 >= 0)

m.c673 = Constraint(expr=   m.b7 - m.b8 + m.b104 >= 0)

m.c674 = Constraint(expr=   m.b8 - m.b9 + m.b105 >= 0)

m.c675 = Constraint(expr=   m.b9 - m.b10 + m.b106 >= 0)

m.c676 = Constraint(expr=   m.b10 - m.b11 + m.b107 >= 0)

m.c677 = Constraint(expr=   m.b11 - m.b12 + m.b108 >= 0)

m.c678 = Constraint(expr=   m.b12 - m.b13 + m.b109 >= 0)

m.c679 = Constraint(expr=   m.b13 - m.b14 + m.b110 >= 0)

m.c680 = Constraint(expr=   m.b14 - m.b15 + m.b111 >= 0)

m.c681 = Constraint(expr=   m.b15 - m.b16 + m.b112 >= 0)

m.c682 = Constraint(expr=   m.b16 - m.b17 + m.b113 >= 0)

m.c683 = Constraint(expr=   m.b17 - m.b18 + m.b114 >= 0)

m.c684 = Constraint(expr=   m.b18 - m.b19 + m.b115 >= 0)

m.c685 = Constraint(expr=   m.b19 - m.b20 + m.b116 >= 0)

m.c686 = Constraint(expr=   m.b20 - m.b21 + m.b117 >= 0)

m.c687 = Constraint(expr=   m.b21 - m.b22 + m.b118 >= 0)

m.c688 = Constraint(expr=   m.b22 - m.b23 + m.b119 >= 0)

m.c689 = Constraint(expr=   m.b23 - m.b24 + m.b120 >= 0)

m.c690 = Constraint(expr= - m.b25 + m.b121 >= 0)

m.c691 = Constraint(expr=   m.b25 - m.b26 + m.b122 >= 0)

m.c692 = Constraint(expr=   m.b26 - m.b27 + m.b123 >= 0)

m.c693 = Constraint(expr=   m.b27 - m.b28 + m.b124 >= 0)

m.c694 = Constraint(expr=   m.b28 - m.b29 + m.b125 >= 0)

m.c695 = Constraint(expr=   m.b29 - m.b30 + m.b126 >= 0)

m.c696 = Constraint(expr=   m.b30 - m.b31 + m.b127 >= 0)

m.c697 = Constraint(expr=   m.b31 - m.b32 + m.b128 >= 0)

m.c698 = Constraint(expr=   m.b32 - m.b33 + m.b129 >= 0)

m.c699 = Constraint(expr=   m.b33 - m.b34 + m.b130 >= 0)

m.c700 = Constraint(expr=   m.b34 - m.b35 + m.b131 >= 0)

m.c701 = Constraint(expr=   m.b35 - m.b36 + m.b132 >= 0)

m.c702 = Constraint(expr=   m.b36 - m.b37 + m.b133 >= 0)

m.c703 = Constraint(expr=   m.b37 - m.b38 + m.b134 >= 0)

m.c704 = Constraint(expr=   m.b38 - m.b39 + m.b135 >= 0)

m.c705 = Constraint(expr=   m.b39 - m.b40 + m.b136 >= 0)

m.c706 = Constraint(expr=   m.b40 - m.b41 + m.b137 >= 0)

m.c707 = Constraint(expr=   m.b41 - m.b42 + m.b138 >= 0)

m.c708 = Constraint(expr=   m.b42 - m.b43 + m.b139 >= 0)

m.c709 = Constraint(expr=   m.b43 - m.b44 + m.b140 >= 0)

m.c710 = Constraint(expr=   m.b44 - m.b45 + m.b141 >= 0)

m.c711 = Constraint(expr=   m.b45 - m.b46 + m.b142 >= 0)

m.c712 = Constraint(expr=   m.b46 - m.b47 + m.b143 >= 0)

m.c713 = Constraint(expr=   m.b47 - m.b48 + m.b144 >= 0)

m.c714 = Constraint(expr= - m.b49 + m.b145 >= 0)

m.c715 = Constraint(expr=   m.b49 - m.b50 + m.b146 >= 0)

m.c716 = Constraint(expr=   m.b50 - m.b51 + m.b147 >= 0)

m.c717 = Constraint(expr=   m.b51 - m.b52 + m.b148 >= 0)

m.c718 = Constraint(expr=   m.b52 - m.b53 + m.b149 >= 0)

m.c719 = Constraint(expr=   m.b53 - m.b54 + m.b150 >= 0)

m.c720 = Constraint(expr=   m.b54 - m.b55 + m.b151 >= 0)

m.c721 = Constraint(expr=   m.b55 - m.b56 + m.b152 >= 0)

m.c722 = Constraint(expr=   m.b56 - m.b57 + m.b153 >= 0)

m.c723 = Constraint(expr=   m.b57 - m.b58 + m.b154 >= 0)

m.c724 = Constraint(expr=   m.b58 - m.b59 + m.b155 >= 0)

m.c725 = Constraint(expr=   m.b59 - m.b60 + m.b156 >= 0)

m.c726 = Constraint(expr=   m.b60 - m.b61 + m.b157 >= 0)

m.c727 = Constraint(expr=   m.b61 - m.b62 + m.b158 >= 0)

m.c728 = Constraint(expr=   m.b62 - m.b63 + m.b159 >= 0)

m.c729 = Constraint(expr=   m.b63 - m.b64 + m.b160 >= 0)

m.c730 = Constraint(expr=   m.b64 - m.b65 + m.b161 >= 0)

m.c731 = Constraint(expr=   m.b65 - m.b66 + m.b162 >= 0)

m.c732 = Constraint(expr=   m.b66 - m.b67 + m.b163 >= 0)

m.c733 = Constraint(expr=   m.b67 - m.b68 + m.b164 >= 0)

m.c734 = Constraint(expr=   m.b68 - m.b69 + m.b165 >= 0)

m.c735 = Constraint(expr=   m.b69 - m.b70 + m.b166 >= 0)

m.c736 = Constraint(expr=   m.b70 - m.b71 + m.b167 >= 0)

m.c737 = Constraint(expr=   m.b71 - m.b72 + m.b168 >= 0)

m.c738 = Constraint(expr= - m.b73 + m.b169 >= 0)

m.c739 = Constraint(expr=   m.b73 - m.b74 + m.b170 >= 0)

m.c740 = Constraint(expr=   m.b74 - m.b75 + m.b171 >= 0)

m.c741 = Constraint(expr=   m.b75 - m.b76 + m.b172 >= 0)

m.c742 = Constraint(expr=   m.b76 - m.b77 + m.b173 >= 0)

m.c743 = Constraint(expr=   m.b77 - m.b78 + m.b174 >= 0)

m.c744 = Constraint(expr=   m.b78 - m.b79 + m.b175 >= 0)

m.c745 = Constraint(expr=   m.b79 - m.b80 + m.b176 >= 0)

m.c746 = Constraint(expr=   m.b80 - m.b81 + m.b177 >= 0)

m.c747 = Constraint(expr=   m.b81 - m.b82 + m.b178 >= 0)

m.c748 = Constraint(expr=   m.b82 - m.b83 + m.b179 >= 0)

m.c749 = Constraint(expr=   m.b83 - m.b84 + m.b180 >= 0)

m.c750 = Constraint(expr=   m.b84 - m.b85 + m.b181 >= 0)

m.c751 = Constraint(expr=   m.b85 - m.b86 + m.b182 >= 0)

m.c752 = Constraint(expr=   m.b86 - m.b87 + m.b183 >= 0)

m.c753 = Constraint(expr=   m.b87 - m.b88 + m.b184 >= 0)

m.c754 = Constraint(expr=   m.b88 - m.b89 + m.b185 >= 0)

m.c755 = Constraint(expr=   m.b89 - m.b90 + m.b186 >= 0)

m.c756 = Constraint(expr=   m.b90 - m.b91 + m.b187 >= 0)

m.c757 = Constraint(expr=   m.b91 - m.b92 + m.b188 >= 0)

m.c758 = Constraint(expr=   m.b92 - m.b93 + m.b189 >= 0)

m.c759 = Constraint(expr=   m.b93 - m.b94 + m.b190 >= 0)

m.c760 = Constraint(expr=   m.b94 - m.b95 + m.b191 >= 0)

m.c761 = Constraint(expr=   m.b95 - m.b96 + m.b192 >= 0)

m.c762 = Constraint(expr=-(0.5061084326298*m.x385*m.x481 + 50.09702*m.x385 - 0.5580651303227*m.x505*m.x385) + m.x193
                          == 0)

m.c763 = Constraint(expr=-(0.5061084326298*m.x386*m.x482 + 50.09702*m.x386 - 0.5580651303227*m.x506*m.x386) + m.x194
                          == 0)

m.c764 = Constraint(expr=-(0.5061084326298*m.x387*m.x483 + 50.09702*m.x387 - 0.5580651303227*m.x507*m.x387) + m.x195
                          == 0)

m.c765 = Constraint(expr=-(0.5061084326298*m.x388*m.x484 + 50.09702*m.x388 - 0.5580651303227*m.x508*m.x388) + m.x196
                          == 0)

m.c766 = Constraint(expr=-(0.5061084326298*m.x389*m.x485 + 50.09702*m.x389 - 0.5580651303227*m.x509*m.x389) + m.x197
                          == 0)

m.c767 = Constraint(expr=-(0.5061084326298*m.x390*m.x486 + 50.09702*m.x390 - 0.5580651303227*m.x510*m.x390) + m.x198
                          == 0)

m.c768 = Constraint(expr=-(0.5061084326298*m.x391*m.x487 + 50.09702*m.x391 - 0.5580651303227*m.x511*m.x391) + m.x199
                          == 0)

m.c769 = Constraint(expr=-(0.5061084326298*m.x392*m.x488 + 50.09702*m.x392 - 0.5580651303227*m.x512*m.x392) + m.x200
                          == 0)

m.c770 = Constraint(expr=-(0.5061084326298*m.x393*m.x489 + 50.09702*m.x393 - 0.5580651303227*m.x513*m.x393) + m.x201
                          == 0)

m.c771 = Constraint(expr=-(0.5061084326298*m.x394*m.x490 + 50.09702*m.x394 - 0.5580651303227*m.x514*m.x394) + m.x202
                          == 0)

m.c772 = Constraint(expr=-(0.5061084326298*m.x395*m.x491 + 50.09702*m.x395 - 0.5580651303227*m.x515*m.x395) + m.x203
                          == 0)

m.c773 = Constraint(expr=-(0.5061084326298*m.x396*m.x492 + 50.09702*m.x396 - 0.5580651303227*m.x516*m.x396) + m.x204
                          == 0)

m.c774 = Constraint(expr=-(0.5061084326298*m.x397*m.x493 + 50.09702*m.x397 - 0.5580651303227*m.x517*m.x397) + m.x205
                          == 0)

m.c775 = Constraint(expr=-(0.5061084326298*m.x398*m.x494 + 50.09702*m.x398 - 0.5580651303227*m.x518*m.x398) + m.x206
                          == 0)

m.c776 = Constraint(expr=-(0.5061084326298*m.x399*m.x495 + 50.09702*m.x399 - 0.5580651303227*m.x519*m.x399) + m.x207
                          == 0)

m.c777 = Constraint(expr=-(0.5061084326298*m.x400*m.x496 + 50.09702*m.x400 - 0.5580651303227*m.x520*m.x400) + m.x208
                          == 0)

m.c778 = Constraint(expr=-(0.5061084326298*m.x401*m.x497 + 50.09702*m.x401 - 0.5580651303227*m.x521*m.x401) + m.x209
                          == 0)

m.c779 = Constraint(expr=-(0.5061084326298*m.x402*m.x498 + 50.09702*m.x402 - 0.5580651303227*m.x522*m.x402) + m.x210
                          == 0)

m.c780 = Constraint(expr=-(0.5061084326298*m.x403*m.x499 + 50.09702*m.x403 - 0.5580651303227*m.x523*m.x403) + m.x211
                          == 0)

m.c781 = Constraint(expr=-(0.5061084326298*m.x404*m.x500 + 50.09702*m.x404 - 0.5580651303227*m.x524*m.x404) + m.x212
                          == 0)

m.c782 = Constraint(expr=-(0.5061084326298*m.x405*m.x501 + 50.09702*m.x405 - 0.5580651303227*m.x525*m.x405) + m.x213
                          == 0)

m.c783 = Constraint(expr=-(0.5061084326298*m.x406*m.x502 + 50.09702*m.x406 - 0.5580651303227*m.x526*m.x406) + m.x214
                          == 0)

m.c784 = Constraint(expr=-(0.5061084326298*m.x407*m.x503 + 50.09702*m.x407 - 0.5580651303227*m.x527*m.x407) + m.x215
                          == 0)

m.c785 = Constraint(expr=-(0.5061084326298*m.x408*m.x504 + 50.09702*m.x408 - 0.5580651303227*m.x528*m.x408) + m.x216
                          == 0)

m.c786 = Constraint(expr=-(0.5623466695665*m.x409*m.x505 + 78.54163*m.x409 - 0.5499405370095*m.x553*m.x409) + m.x217
                          == 0)

m.c787 = Constraint(expr=-(0.5623466695665*m.x410*m.x506 + 78.54163*m.x410 - 0.5499405370095*m.x554*m.x410) + m.x218
                          == 0)

m.c788 = Constraint(expr=-(0.5623466695665*m.x411*m.x507 + 78.54163*m.x411 - 0.5499405370095*m.x555*m.x411) + m.x219
                          == 0)

m.c789 = Constraint(expr=-(0.5623466695665*m.x412*m.x508 + 78.54163*m.x412 - 0.5499405370095*m.x556*m.x412) + m.x220
                          == 0)

m.c790 = Constraint(expr=-(0.5623466695665*m.x413*m.x509 + 78.54163*m.x413 - 0.5499405370095*m.x557*m.x413) + m.x221
                          == 0)

m.c791 = Constraint(expr=-(0.5623466695665*m.x414*m.x510 + 78.54163*m.x414 - 0.5499405370095*m.x558*m.x414) + m.x222
                          == 0)

m.c792 = Constraint(expr=-(0.5623466695665*m.x415*m.x511 + 78.54163*m.x415 - 0.5499405370095*m.x559*m.x415) + m.x223
                          == 0)

m.c793 = Constraint(expr=-(0.5623466695665*m.x416*m.x512 + 78.54163*m.x416 - 0.5499405370095*m.x560*m.x416) + m.x224
                          == 0)

m.c794 = Constraint(expr=-(0.5623466695665*m.x417*m.x513 + 78.54163*m.x417 - 0.5499405370095*m.x561*m.x417) + m.x225
                          == 0)

m.c795 = Constraint(expr=-(0.5623466695665*m.x418*m.x514 + 78.54163*m.x418 - 0.5499405370095*m.x562*m.x418) + m.x226
                          == 0)

m.c796 = Constraint(expr=-(0.5623466695665*m.x419*m.x515 + 78.54163*m.x419 - 0.5499405370095*m.x563*m.x419) + m.x227
                          == 0)

m.c797 = Constraint(expr=-(0.5623466695665*m.x420*m.x516 + 78.54163*m.x420 - 0.5499405370095*m.x564*m.x420) + m.x228
                          == 0)

m.c798 = Constraint(expr=-(0.5623466695665*m.x421*m.x517 + 78.54163*m.x421 - 0.5499405370095*m.x565*m.x421) + m.x229
                          == 0)

m.c799 = Constraint(expr=-(0.5623466695665*m.x422*m.x518 + 78.54163*m.x422 - 0.5499405370095*m.x566*m.x422) + m.x230
                          == 0)

m.c800 = Constraint(expr=-(0.5623466695665*m.x423*m.x519 + 78.54163*m.x423 - 0.5499405370095*m.x567*m.x423) + m.x231
                          == 0)

m.c801 = Constraint(expr=-(0.5623466695665*m.x424*m.x520 + 78.54163*m.x424 - 0.5499405370095*m.x568*m.x424) + m.x232
                          == 0)

m.c802 = Constraint(expr=-(0.5623466695665*m.x425*m.x521 + 78.54163*m.x425 - 0.5499405370095*m.x569*m.x425) + m.x233
                          == 0)

m.c803 = Constraint(expr=-(0.5623466695665*m.x426*m.x522 + 78.54163*m.x426 - 0.5499405370095*m.x570*m.x426) + m.x234
                          == 0)

m.c804 = Constraint(expr=-(0.5623466695665*m.x427*m.x523 + 78.54163*m.x427 - 0.5499405370095*m.x571*m.x427) + m.x235
                          == 0)

m.c805 = Constraint(expr=-(0.5623466695665*m.x428*m.x524 + 78.54163*m.x428 - 0.5499405370095*m.x572*m.x428) + m.x236
                          == 0)

m.c806 = Constraint(expr=-(0.5623466695665*m.x429*m.x525 + 78.54163*m.x429 - 0.5499405370095*m.x573*m.x429) + m.x237
                          == 0)

m.c807 = Constraint(expr=-(0.5623466695665*m.x430*m.x526 + 78.54163*m.x430 - 0.5499405370095*m.x574*m.x430) + m.x238
                          == 0)

m.c808 = Constraint(expr=-(0.5623466695665*m.x431*m.x527 + 78.54163*m.x431 - 0.5499405370095*m.x575*m.x431) + m.x239
                          == 0)

m.c809 = Constraint(expr=-(0.5623466695665*m.x432*m.x528 + 78.54163*m.x432 - 0.5499405370095*m.x576*m.x432) + m.x240
                          == 0)

m.c810 = Constraint(expr=-(1.0195418832074*m.x433*m.x529 + 989.1982*m.x433 - 0.4602295096966*m.x553*m.x433) + m.x241
                          == 0)

m.c811 = Constraint(expr=-(1.0195418832074*m.x434*m.x530 + 989.1982*m.x434 - 0.4602295096966*m.x554*m.x434) + m.x242
                          == 0)

m.c812 = Constraint(expr=-(1.0195418832074*m.x435*m.x531 + 989.1982*m.x435 - 0.4602295096966*m.x555*m.x435) + m.x243
                          == 0)

m.c813 = Constraint(expr=-(1.0195418832074*m.x436*m.x532 + 989.1982*m.x436 - 0.4602295096966*m.x556*m.x436) + m.x244
                          == 0)

m.c814 = Constraint(expr=-(1.0195418832074*m.x437*m.x533 + 989.1982*m.x437 - 0.4602295096966*m.x557*m.x437) + m.x245
                          == 0)

m.c815 = Constraint(expr=-(1.0195418832074*m.x438*m.x534 + 989.1982*m.x438 - 0.4602295096966*m.x558*m.x438) + m.x246
                          == 0)

m.c816 = Constraint(expr=-(1.0195418832074*m.x439*m.x535 + 989.1982*m.x439 - 0.4602295096966*m.x559*m.x439) + m.x247
                          == 0)

m.c817 = Constraint(expr=-(1.0195418832074*m.x440*m.x536 + 989.1982*m.x440 - 0.4602295096966*m.x560*m.x440) + m.x248
                          == 0)

m.c818 = Constraint(expr=-(1.0195418832074*m.x441*m.x537 + 989.1982*m.x441 - 0.4602295096966*m.x561*m.x441) + m.x249
                          == 0)

m.c819 = Constraint(expr=-(1.0195418832074*m.x442*m.x538 + 989.1982*m.x442 - 0.4602295096966*m.x562*m.x442) + m.x250
                          == 0)

m.c820 = Constraint(expr=-(1.0195418832074*m.x443*m.x539 + 989.1982*m.x443 - 0.4602295096966*m.x563*m.x443) + m.x251
                          == 0)

m.c821 = Constraint(expr=-(1.0195418832074*m.x444*m.x540 + 989.1982*m.x444 - 0.4602295096966*m.x564*m.x444) + m.x252
                          == 0)

m.c822 = Constraint(expr=-(1.0195418832074*m.x445*m.x541 + 989.1982*m.x445 - 0.4602295096966*m.x565*m.x445) + m.x253
                          == 0)

m.c823 = Constraint(expr=-(1.0195418832074*m.x446*m.x542 + 989.1982*m.x446 - 0.4602295096966*m.x566*m.x446) + m.x254
                          == 0)

m.c824 = Constraint(expr=-(1.0195418832074*m.x447*m.x543 + 989.1982*m.x447 - 0.4602295096966*m.x567*m.x447) + m.x255
                          == 0)

m.c825 = Constraint(expr=-(1.0195418832074*m.x448*m.x544 + 989.1982*m.x448 - 0.4602295096966*m.x568*m.x448) + m.x256
                          == 0)

m.c826 = Constraint(expr=-(1.0195418832074*m.x449*m.x545 + 989.1982*m.x449 - 0.4602295096966*m.x569*m.x449) + m.x257
                          == 0)

m.c827 = Constraint(expr=-(1.0195418832074*m.x450*m.x546 + 989.1982*m.x450 - 0.4602295096966*m.x570*m.x450) + m.x258
                          == 0)

m.c828 = Constraint(expr=-(1.0195418832074*m.x451*m.x547 + 989.1982*m.x451 - 0.4602295096966*m.x571*m.x451) + m.x259
                          == 0)

m.c829 = Constraint(expr=-(1.0195418832074*m.x452*m.x548 + 989.1982*m.x452 - 0.4602295096966*m.x572*m.x452) + m.x260
                          == 0)

m.c830 = Constraint(expr=-(1.0195418832074*m.x453*m.x549 + 989.1982*m.x453 - 0.4602295096966*m.x573*m.x453) + m.x261
                          == 0)

m.c831 = Constraint(expr=-(1.0195418832074*m.x454*m.x550 + 989.1982*m.x454 - 0.4602295096966*m.x574*m.x454) + m.x262
                          == 0)

m.c832 = Constraint(expr=-(1.0195418832074*m.x455*m.x551 + 989.1982*m.x455 - 0.4602295096966*m.x575*m.x455) + m.x263
                          == 0)

m.c833 = Constraint(expr=-(1.0195418832074*m.x456*m.x552 + 989.1982*m.x456 - 0.4602295096966*m.x576*m.x456) + m.x264
                          == 0)

m.c834 = Constraint(expr=-(0.5742413664547*m.x457*m.x553 + 67.34698*m.x457) + m.x265 == 0)

m.c835 = Constraint(expr=-(0.5742413664547*m.x458*m.x554 + 67.34698*m.x458) + m.x266 == 0)

m.c836 = Constraint(expr=-(0.5742413664547*m.x459*m.x555 + 67.34698*m.x459) + m.x267 == 0)

m.c837 = Constraint(expr=-(0.5742413664547*m.x460*m.x556 + 67.34698*m.x460) + m.x268 == 0)

m.c838 = Constraint(expr=-(0.5742413664547*m.x461*m.x557 + 67.34698*m.x461) + m.x269 == 0)

m.c839 = Constraint(expr=-(0.5742413664547*m.x462*m.x558 + 67.34698*m.x462) + m.x270 == 0)

m.c840 = Constraint(expr=-(0.5742413664547*m.x463*m.x559 + 67.34698*m.x463) + m.x271 == 0)

m.c841 = Constraint(expr=-(0.5742413664547*m.x464*m.x560 + 67.34698*m.x464) + m.x272 == 0)

m.c842 = Constraint(expr=-(0.5742413664547*m.x465*m.x561 + 67.34698*m.x465) + m.x273 == 0)

m.c843 = Constraint(expr=-(0.5742413664547*m.x466*m.x562 + 67.34698*m.x466) + m.x274 == 0)

m.c844 = Constraint(expr=-(0.5742413664547*m.x467*m.x563 + 67.34698*m.x467) + m.x275 == 0)

m.c845 = Constraint(expr=-(0.5742413664547*m.x468*m.x564 + 67.34698*m.x468) + m.x276 == 0)

m.c846 = Constraint(expr=-(0.5742413664547*m.x469*m.x565 + 67.34698*m.x469) + m.x277 == 0)

m.c847 = Constraint(expr=-(0.5742413664547*m.x470*m.x566 + 67.34698*m.x470) + m.x278 == 0)

m.c848 = Constraint(expr=-(0.5742413664547*m.x471*m.x567 + 67.34698*m.x471) + m.x279 == 0)

m.c849 = Constraint(expr=-(0.5742413664547*m.x472*m.x568 + 67.34698*m.x472) + m.x280 == 0)

m.c850 = Constraint(expr=-(0.5742413664547*m.x473*m.x569 + 67.34698*m.x473) + m.x281 == 0)

m.c851 = Constraint(expr=-(0.5742413664547*m.x474*m.x570 + 67.34698*m.x474) + m.x282 == 0)

m.c852 = Constraint(expr=-(0.5742413664547*m.x475*m.x571 + 67.34698*m.x475) + m.x283 == 0)

m.c853 = Constraint(expr=-(0.5742413664547*m.x476*m.x572 + 67.34698*m.x476) + m.x284 == 0)

m.c854 = Constraint(expr=-(0.5742413664547*m.x477*m.x573 + 67.34698*m.x477) + m.x285 == 0)

m.c855 = Constraint(expr=-(0.5742413664547*m.x478*m.x574 + 67.34698*m.x478) + m.x286 == 0)

m.c856 = Constraint(expr=-(0.5742413664547*m.x479*m.x575 + 67.34698*m.x479) + m.x287 == 0)

m.c857 = Constraint(expr=-(0.5742413664547*m.x480*m.x576 + 67.34698*m.x480) + m.x288 == 0)
