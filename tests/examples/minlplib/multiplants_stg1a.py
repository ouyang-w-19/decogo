#  MINLP written by GAMS Convert at 04/21/18 13:52:37
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        250      125       27       98        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        424      208      216        0        0        0        0        0
#  FX     73       73        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1689     1562      127        0


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
m.b193 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b194 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b195 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b196 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b197 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b198 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b199 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b200 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b201 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b202 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b203 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b204 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b205 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b206 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b207 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b208 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b209 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b210 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b211 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b212 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b213 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b214 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b215 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b216 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,200000),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,200000),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,200000),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,200000),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,200000),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,200000),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,200000),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,200000),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,225000),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,225000),initialize=0)
m.x235 = Var(within=Reals,bounds=(0,225000),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,225000),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,225000),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,225000),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,225000),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,225000),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,125000),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,125000),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,125000),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,125000),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,125000),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,125000),initialize=0)
m.x255 = Var(within=Reals,bounds=(0,125000),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,125000),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,150000),initialize=0)
m.x258 = Var(within=Reals,bounds=(0,150000),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,150000),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,150000),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,150000),initialize=0)
m.x262 = Var(within=Reals,bounds=(0,150000),initialize=0)
m.x263 = Var(within=Reals,bounds=(0,150000),initialize=0)
m.x264 = Var(within=Reals,bounds=(0,150000),initialize=0)
m.x265 = Var(within=Reals,bounds=(0,250000),initialize=0)
m.x266 = Var(within=Reals,bounds=(0,250000),initialize=0)
m.x267 = Var(within=Reals,bounds=(0,250000),initialize=0)
m.x268 = Var(within=Reals,bounds=(0,250000),initialize=0)
m.x269 = Var(within=Reals,bounds=(0,250000),initialize=0)
m.x270 = Var(within=Reals,bounds=(0,250000),initialize=0)
m.x271 = Var(within=Reals,bounds=(0,250000),initialize=0)
m.x272 = Var(within=Reals,bounds=(0,250000),initialize=0)
m.x273 = Var(within=Reals,bounds=(0,112500),initialize=0)
m.x274 = Var(within=Reals,bounds=(0,112500),initialize=0)
m.x275 = Var(within=Reals,bounds=(0,112500),initialize=0)
m.x276 = Var(within=Reals,bounds=(0,112500),initialize=0)
m.x277 = Var(within=Reals,bounds=(0,112500),initialize=0)
m.x278 = Var(within=Reals,bounds=(0,112500),initialize=0)
m.x279 = Var(within=Reals,bounds=(0,112500),initialize=0)
m.x280 = Var(within=Reals,bounds=(0,112500),initialize=0)
m.x281 = Var(within=Reals,bounds=(0,275000),initialize=0)
m.x282 = Var(within=Reals,bounds=(0,275000),initialize=0)
m.x283 = Var(within=Reals,bounds=(0,275000),initialize=0)
m.x284 = Var(within=Reals,bounds=(0,275000),initialize=0)
m.x285 = Var(within=Reals,bounds=(0,275000),initialize=0)
m.x286 = Var(within=Reals,bounds=(0,275000),initialize=0)
m.x287 = Var(within=Reals,bounds=(0,275000),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,275000),initialize=0)
m.x289 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x290 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x291 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x292 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x293 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x294 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x295 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x296 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x297 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x298 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x299 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x300 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x301 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x302 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x303 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x304 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x305 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x306 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x307 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x309 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x311 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x312 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x313 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x314 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x315 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x316 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x317 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x318 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x319 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x320 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x321 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x322 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x323 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x324 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x325 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x326 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x327 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x328 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x329 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x330 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x331 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x332 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x333 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x334 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x335 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x336 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x337 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x338 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x339 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x340 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x341 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x342 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x343 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x344 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x345 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x346 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x347 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x348 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x349 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x350 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x351 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x352 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x353 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x354 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x355 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x356 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x357 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x358 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x359 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x360 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x361 = Var(within=Reals,bounds=(0,200000),initialize=0)
m.x362 = Var(within=Reals,bounds=(0,200000),initialize=0)
m.x363 = Var(within=Reals,bounds=(0,200000),initialize=0)
m.x364 = Var(within=Reals,bounds=(0,200000),initialize=0)
m.x365 = Var(within=Reals,bounds=(0,200000),initialize=0)
m.x366 = Var(within=Reals,bounds=(0,200000),initialize=0)
m.x367 = Var(within=Reals,bounds=(0,200000),initialize=0)
m.x368 = Var(within=Reals,bounds=(0,200000),initialize=0)
m.x369 = Var(within=Reals,bounds=(0,225000),initialize=0)
m.x370 = Var(within=Reals,bounds=(0,225000),initialize=0)
m.x371 = Var(within=Reals,bounds=(0,225000),initialize=0)
m.x372 = Var(within=Reals,bounds=(0,225000),initialize=0)
m.x373 = Var(within=Reals,bounds=(0,225000),initialize=0)
m.x374 = Var(within=Reals,bounds=(0,225000),initialize=0)
m.x375 = Var(within=Reals,bounds=(0,225000),initialize=0)
m.x376 = Var(within=Reals,bounds=(0,225000),initialize=0)
m.x377 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x378 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x379 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x380 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x381 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x382 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x383 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x384 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x385 = Var(within=Reals,bounds=(0,150000),initialize=0)
m.x386 = Var(within=Reals,bounds=(0,150000),initialize=0)
m.x387 = Var(within=Reals,bounds=(0,150000),initialize=0)
m.x388 = Var(within=Reals,bounds=(0,150000),initialize=0)
m.x389 = Var(within=Reals,bounds=(0,150000),initialize=0)
m.x390 = Var(within=Reals,bounds=(0,150000),initialize=0)
m.x391 = Var(within=Reals,bounds=(0,150000),initialize=0)
m.x392 = Var(within=Reals,bounds=(0,150000),initialize=0)
m.x393 = Var(within=Reals,bounds=(0,250000),initialize=0)
m.x394 = Var(within=Reals,bounds=(0,250000),initialize=0)
m.x395 = Var(within=Reals,bounds=(0,250000),initialize=0)
m.x396 = Var(within=Reals,bounds=(0,250000),initialize=0)
m.x397 = Var(within=Reals,bounds=(0,250000),initialize=0)
m.x398 = Var(within=Reals,bounds=(0,250000),initialize=0)
m.x399 = Var(within=Reals,bounds=(0,250000),initialize=0)
m.x400 = Var(within=Reals,bounds=(0,250000),initialize=0)
m.x401 = Var(within=Reals,bounds=(0,275000),initialize=0)
m.x402 = Var(within=Reals,bounds=(0,275000),initialize=0)
m.x403 = Var(within=Reals,bounds=(0,275000),initialize=0)
m.x404 = Var(within=Reals,bounds=(0,275000),initialize=0)
m.x405 = Var(within=Reals,bounds=(0,275000),initialize=0)
m.x406 = Var(within=Reals,bounds=(0,275000),initialize=0)
m.x407 = Var(within=Reals,bounds=(0,275000),initialize=0)
m.x408 = Var(within=Reals,bounds=(0,275000),initialize=0)
m.x409 = Var(within=Reals,bounds=(0,225000),initialize=0)
m.x410 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x411 = Var(within=Reals,bounds=(0,275000),initialize=0)
m.x412 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x413 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x414 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x415 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x416 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x417 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x418 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x419 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x420 = Var(within=Reals,bounds=(0,200000),initialize=0)
m.x421 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x422 = Var(within=Reals,bounds=(0,250000),initialize=0)
m.x423 = Var(within=Reals,bounds=(100,250),initialize=100)
m.x424 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x424, sense=maximize)

m.c1 = Constraint(expr=m.x424*m.x423 + (0.00203*m.x369 + 0.00203*m.x370)*(m.x413 - m.x412) + (0.00203*m.x370 + 0.00203*
                       m.x371)*(m.x414 - m.x413) + (0.00203*m.x371 + 0.00203*m.x372)*(m.x415 - m.x414) + (0.00203*m.x372
                        + 0.00203*m.x373)*(m.x416 - m.x415) + (0.00203*m.x373 + 0.00203*m.x374)*(m.x417 - m.x416) + (
                       0.00203*m.x374 + 0.00203*m.x375)*(m.x418 - m.x417) + (0.00203*m.x375 + 0.00203*m.x376)*(m.x419 - 
                       m.x418) + (0.00203*m.x369 + 0.00203*m.x376)*(m.x423 - m.x419) + (0.00203*m.x385 + 0.00203*m.x386)
                       *(m.x413 - m.x412) + (0.00203*m.x386 + 0.00203*m.x387)*(m.x414 - m.x413) + (0.00203*m.x387 + 
                       0.00203*m.x388)*(m.x415 - m.x414) + (0.00203*m.x388 + 0.00203*m.x389)*(m.x416 - m.x415) + (
                       0.00203*m.x389 + 0.00203*m.x390)*(m.x417 - m.x416) + (0.00203*m.x390 + 0.00203*m.x391)*(m.x418 - 
                       m.x417) + (0.00203*m.x391 + 0.00203*m.x392)*(m.x419 - m.x418) + (0.00203*m.x385 + 0.00203*m.x392)
                       *(m.x423 - m.x419) + (0.00203*m.x401 + 0.00203*m.x402)*(m.x413 - m.x412) + (0.00203*m.x402 + 
                       0.00203*m.x403)*(m.x414 - m.x413) + (0.00203*m.x403 + 0.00203*m.x404)*(m.x415 - m.x414) + (
                       0.00203*m.x404 + 0.00203*m.x405)*(m.x416 - m.x415) + (0.00203*m.x405 + 0.00203*m.x406)*(m.x417 - 
                       m.x416) + (0.00203*m.x406 + 0.00203*m.x407)*(m.x418 - m.x417) + (0.00203*m.x407 + 0.00203*m.x408)
                       *(m.x419 - m.x418) + (0.00203*m.x401 + 0.00203*m.x408)*(m.x423 - m.x419) + 3800*m.b73
                        + 3800*m.b74 + 3800*m.b75 + 3800*m.b76 + 3800*m.b77 + 3800*m.b78 + 3800*m.b79 + 3800*m.b80
                        + 6080*m.b81 + 6080*m.b82 + 6080*m.b83 + 6080*m.b84 + 6080*m.b85 + 6080*m.b86 + 6080*m.b87
                        + 6080*m.b88 + 7500*m.b89 + 7500*m.b90 + 7500*m.b91 + 7500*m.b92 + 7500*m.b93 + 7500*m.b94
                        + 7500*m.b95 + 7500*m.b96 + 2250*m.b97 + 2250*m.b98 + 2250*m.b99 + 2250*m.b100 + 2250*m.b101
                        + 2250*m.b102 + 2250*m.b103 + 2250*m.b104 + 3080*m.b105 + 3080*m.b106 + 3080*m.b107
                        + 3080*m.b108 + 3080*m.b109 + 3080*m.b110 + 3080*m.b111 + 3080*m.b112 + 5390*m.b113
                        + 5390*m.b114 + 5390*m.b115 + 5390*m.b116 + 5390*m.b117 + 5390*m.b118 + 5390*m.b119
                        + 5390*m.b120 + 6840*m.b121 + 6840*m.b122 + 6840*m.b123 + 6840*m.b124 + 6840*m.b125
                        + 6840*m.b126 + 6840*m.b127 + 6840*m.b128 + 8360*m.b129 + 8360*m.b130 + 8360*m.b131
                        + 8360*m.b132 + 8360*m.b133 + 8360*m.b134 + 8360*m.b135 + 8360*m.b136 + 3750*m.b137
                        + 3750*m.b138 + 3750*m.b139 + 3750*m.b140 + 3750*m.b141 + 3750*m.b142 + 3750*m.b143
                        + 3750*m.b144 + 5250*m.b145 + 5250*m.b146 + 5250*m.b147 + 5250*m.b148 + 5250*m.b149
                        + 5250*m.b150 + 5250*m.b151 + 5250*m.b152 + 4620*m.b153 + 4620*m.b154 + 4620*m.b155
                        + 4620*m.b156 + 4620*m.b157 + 4620*m.b158 + 4620*m.b159 + 4620*m.b160 + 3080*m.b161
                        + 3080*m.b162 + 3080*m.b163 + 3080*m.b164 + 3080*m.b165 + 3080*m.b166 + 3080*m.b167
                        + 3080*m.b168 + 8360*m.b169 + 8360*m.b170 + 8360*m.b171 + 8360*m.b172 + 8360*m.b173
                        + 8360*m.b174 + 8360*m.b175 + 8360*m.b176 + 760*m.b177 + 760*m.b178 + 760*m.b179 + 760*m.b180
                        + 760*m.b181 + 760*m.b182 + 760*m.b183 + 760*m.b184 + 1500*m.b185 + 1500*m.b186 + 1500*m.b187
                        + 1500*m.b188 + 1500*m.b189 + 1500*m.b190 + 1500*m.b191 + 1500*m.b192 + 3750*m.b193
                        + 3750*m.b194 + 3750*m.b195 + 3750*m.b196 + 3750*m.b197 + 3750*m.b198 + 3750*m.b199
                        + 3750*m.b200 + 4620*m.b201 + 4620*m.b202 + 4620*m.b203 + 4620*m.b204 + 4620*m.b205
                        + 4620*m.b206 + 4620*m.b207 + 4620*m.b208 + 770*m.b209 + 770*m.b210 + 770*m.b211 + 770*m.b212
                        + 770*m.b213 + 770*m.b214 + 770*m.b215 + 770*m.b216 - 0.15*m.x409 - 0.4*m.x410 - 0.65*m.x411
                        + 0.1406*m.x420 + 0.1406*m.x421 + 0.1406*m.x422 == 0)

m.c2 = Constraint(expr=   m.b1 - m.b8 + m.b73 + m.b81 - m.b96 - m.b112 + m.x289 - m.x296 == 0)

m.c3 = Constraint(expr= - m.b1 + m.b2 + m.b74 + m.b82 - m.b89 - m.b105 - m.x289 + m.x290 == 0)

m.c4 = Constraint(expr= - m.b2 + m.b3 + m.b75 + m.b83 - m.b90 - m.b106 - m.x290 + m.x291 == 0)

m.c5 = Constraint(expr= - m.b3 + m.b4 + m.b76 + m.b84 - m.b91 - m.b107 - m.x291 + m.x292 == 0)

m.c6 = Constraint(expr= - m.b4 + m.b5 + m.b77 + m.b85 - m.b92 - m.b108 - m.x292 + m.x293 == 0)

m.c7 = Constraint(expr= - m.b5 + m.b6 + m.b78 + m.b86 - m.b93 - m.b109 - m.x293 + m.x294 == 0)

m.c8 = Constraint(expr= - m.b6 + m.b7 + m.b79 + m.b87 - m.b94 - m.b110 - m.x294 + m.x295 == 0)

m.c9 = Constraint(expr= - m.b7 + m.b8 + m.b80 + m.b88 - m.b95 - m.b111 - m.x295 + m.x296 == 0)

m.c10 = Constraint(expr=   m.b25 - m.b32 - m.b80 + m.b89 + m.b97 - m.b120 + m.x297 - m.x304 == 0)

m.c11 = Constraint(expr= - m.b25 + m.b26 - m.b73 + m.b90 + m.b98 - m.b113 - m.x297 + m.x298 == 0)

m.c12 = Constraint(expr= - m.b26 + m.b27 - m.b74 + m.b91 + m.b99 - m.b114 - m.x298 + m.x299 == 0)

m.c13 = Constraint(expr= - m.b27 + m.b28 - m.b75 + m.b92 + m.b100 - m.b115 - m.x299 + m.x300 == 0)

m.c14 = Constraint(expr= - m.b28 + m.b29 - m.b76 + m.b93 + m.b101 - m.b116 - m.x300 + m.x301 == 0)

m.c15 = Constraint(expr= - m.b29 + m.b30 - m.b77 + m.b94 + m.b102 - m.b117 - m.x301 + m.x302 == 0)

m.c16 = Constraint(expr= - m.b30 + m.b31 - m.b78 + m.b95 + m.b103 - m.b118 - m.x302 + m.x303 == 0)

m.c17 = Constraint(expr= - m.b31 + m.b32 - m.b79 + m.b96 + m.b104 - m.b119 - m.x303 + m.x304 == 0)

m.c18 = Constraint(expr=   m.b49 - m.b56 - m.b88 - m.b104 + m.b105 + m.b113 + m.x305 - m.x312 == 0)

m.c19 = Constraint(expr= - m.b49 + m.b50 - m.b81 - m.b97 + m.b106 + m.b114 - m.x305 + m.x306 == 0)

m.c20 = Constraint(expr= - m.b50 + m.b51 - m.b82 - m.b98 + m.b107 + m.b115 - m.x306 + m.x307 == 0)

m.c21 = Constraint(expr= - m.b51 + m.b52 - m.b83 - m.b99 + m.b108 + m.b116 - m.x307 + m.x308 == 0)

m.c22 = Constraint(expr= - m.b52 + m.b53 - m.b84 - m.b100 + m.b109 + m.b117 - m.x308 + m.x309 == 0)

m.c23 = Constraint(expr= - m.b53 + m.b54 - m.b85 - m.b101 + m.b110 + m.b118 - m.x309 + m.x310 == 0)

m.c24 = Constraint(expr= - m.b54 + m.b55 - m.b86 - m.b102 + m.b111 + m.b119 - m.x310 + m.x311 == 0)

m.c25 = Constraint(expr= - m.b55 + m.b56 - m.b87 - m.b103 + m.b112 + m.b120 - m.x311 + m.x312 == 0)

m.c26 = Constraint(expr=   m.b9 - m.b16 + m.b121 + m.b129 - m.b144 - m.b160 + m.x313 - m.x320 == 0)

m.c27 = Constraint(expr= - m.b9 + m.b10 + m.b122 + m.b130 - m.b137 - m.b153 - m.x313 + m.x314 == 0)

m.c28 = Constraint(expr= - m.b10 + m.b11 + m.b123 + m.b131 - m.b138 - m.b154 - m.x314 + m.x315 == 0)

m.c29 = Constraint(expr= - m.b11 + m.b12 + m.b124 + m.b132 - m.b139 - m.b155 - m.x315 + m.x316 == 0)

m.c30 = Constraint(expr= - m.b12 + m.b13 + m.b125 + m.b133 - m.b140 - m.b156 - m.x316 + m.x317 == 0)

m.c31 = Constraint(expr= - m.b13 + m.b14 + m.b126 + m.b134 - m.b141 - m.b157 - m.x317 + m.x318 == 0)

m.c32 = Constraint(expr= - m.b14 + m.b15 + m.b127 + m.b135 - m.b142 - m.b158 - m.x318 + m.x319 == 0)

m.c33 = Constraint(expr= - m.b15 + m.b16 + m.b128 + m.b136 - m.b143 - m.b159 - m.x319 + m.x320 == 0)

m.c34 = Constraint(expr=   m.b33 - m.b40 - m.b128 + m.b137 + m.b145 - m.b168 + m.x321 - m.x328 == 0)

m.c35 = Constraint(expr= - m.b33 + m.b34 - m.b121 + m.b138 + m.b146 - m.b161 - m.x321 + m.x322 == 0)

m.c36 = Constraint(expr= - m.b34 + m.b35 - m.b122 + m.b139 + m.b147 - m.b162 - m.x322 + m.x323 == 0)

m.c37 = Constraint(expr= - m.b35 + m.b36 - m.b123 + m.b140 + m.b148 - m.b163 - m.x323 + m.x324 == 0)

m.c38 = Constraint(expr= - m.b36 + m.b37 - m.b124 + m.b141 + m.b149 - m.b164 - m.x324 + m.x325 == 0)

m.c39 = Constraint(expr= - m.b37 + m.b38 - m.b125 + m.b142 + m.b150 - m.b165 - m.x325 + m.x326 == 0)

m.c40 = Constraint(expr= - m.b38 + m.b39 - m.b126 + m.b143 + m.b151 - m.b166 - m.x326 + m.x327 == 0)

m.c41 = Constraint(expr= - m.b39 + m.b40 - m.b127 + m.b144 + m.b152 - m.b167 - m.x327 + m.x328 == 0)

m.c42 = Constraint(expr=   m.b57 - m.b64 - m.b136 - m.b152 + m.b153 + m.b161 + m.x329 - m.x336 == 0)

m.c43 = Constraint(expr= - m.b57 + m.b58 - m.b129 - m.b145 + m.b154 + m.b162 - m.x329 + m.x330 == 0)

m.c44 = Constraint(expr= - m.b58 + m.b59 - m.b130 - m.b146 + m.b155 + m.b163 - m.x330 + m.x331 == 0)

m.c45 = Constraint(expr= - m.b59 + m.b60 - m.b131 - m.b147 + m.b156 + m.b164 - m.x331 + m.x332 == 0)

m.c46 = Constraint(expr= - m.b60 + m.b61 - m.b132 - m.b148 + m.b157 + m.b165 - m.x332 + m.x333 == 0)

m.c47 = Constraint(expr= - m.b61 + m.b62 - m.b133 - m.b149 + m.b158 + m.b166 - m.x333 + m.x334 == 0)

m.c48 = Constraint(expr= - m.b62 + m.b63 - m.b134 - m.b150 + m.b159 + m.b167 - m.x334 + m.x335 == 0)

m.c49 = Constraint(expr= - m.b63 + m.b64 - m.b135 - m.b151 + m.b160 + m.b168 - m.x335 + m.x336 == 0)

m.c50 = Constraint(expr=   m.b17 - m.b24 + m.b169 + m.b177 - m.b192 - m.b208 + m.x337 - m.x344 == 0)

m.c51 = Constraint(expr= - m.b17 + m.b18 + m.b170 + m.b178 - m.b185 - m.b201 - m.x337 + m.x338 == 0)

m.c52 = Constraint(expr= - m.b18 + m.b19 + m.b171 + m.b179 - m.b186 - m.b202 - m.x338 + m.x339 == 0)

m.c53 = Constraint(expr= - m.b19 + m.b20 + m.b172 + m.b180 - m.b187 - m.b203 - m.x339 + m.x340 == 0)

m.c54 = Constraint(expr= - m.b20 + m.b21 + m.b173 + m.b181 - m.b188 - m.b204 - m.x340 + m.x341 == 0)

m.c55 = Constraint(expr= - m.b21 + m.b22 + m.b174 + m.b182 - m.b189 - m.b205 - m.x341 + m.x342 == 0)

m.c56 = Constraint(expr= - m.b22 + m.b23 + m.b175 + m.b183 - m.b190 - m.b206 - m.x342 + m.x343 == 0)

m.c57 = Constraint(expr= - m.b23 + m.b24 + m.b176 + m.b184 - m.b191 - m.b207 - m.x343 + m.x344 == 0)

m.c58 = Constraint(expr=   m.b41 - m.b48 - m.b176 + m.b185 + m.b193 - m.b216 + m.x345 - m.x352 == 0)

m.c59 = Constraint(expr= - m.b41 + m.b42 - m.b169 + m.b186 + m.b194 - m.b209 - m.x345 + m.x346 == 0)

m.c60 = Constraint(expr= - m.b42 + m.b43 - m.b170 + m.b187 + m.b195 - m.b210 - m.x346 + m.x347 == 0)

m.c61 = Constraint(expr= - m.b43 + m.b44 - m.b171 + m.b188 + m.b196 - m.b211 - m.x347 + m.x348 == 0)

m.c62 = Constraint(expr= - m.b44 + m.b45 - m.b172 + m.b189 + m.b197 - m.b212 - m.x348 + m.x349 == 0)

m.c63 = Constraint(expr= - m.b45 + m.b46 - m.b173 + m.b190 + m.b198 - m.b213 - m.x349 + m.x350 == 0)

m.c64 = Constraint(expr= - m.b46 + m.b47 - m.b174 + m.b191 + m.b199 - m.b214 - m.x350 + m.x351 == 0)

m.c65 = Constraint(expr= - m.b47 + m.b48 - m.b175 + m.b192 + m.b200 - m.b215 - m.x351 + m.x352 == 0)

m.c66 = Constraint(expr=   m.b65 - m.b72 - m.b184 - m.b200 + m.b201 + m.b209 + m.x353 - m.x360 == 0)

m.c67 = Constraint(expr= - m.b65 + m.b66 - m.b177 - m.b193 + m.b202 + m.b210 - m.x353 + m.x354 == 0)

m.c68 = Constraint(expr= - m.b66 + m.b67 - m.b178 - m.b194 + m.b203 + m.b211 - m.x354 + m.x355 == 0)

m.c69 = Constraint(expr= - m.b67 + m.b68 - m.b179 - m.b195 + m.b204 + m.b212 - m.x355 + m.x356 == 0)

m.c70 = Constraint(expr= - m.b68 + m.b69 - m.b180 - m.b196 + m.b205 + m.b213 - m.x356 + m.x357 == 0)

m.c71 = Constraint(expr= - m.b69 + m.b70 - m.b181 - m.b197 + m.b206 + m.b214 - m.x357 + m.x358 == 0)

m.c72 = Constraint(expr= - m.b70 + m.b71 - m.b182 - m.b198 + m.b207 + m.b215 - m.x358 + m.x359 == 0)

m.c73 = Constraint(expr= - m.b71 + m.b72 - m.b183 - m.b199 + m.b208 + m.b216 - m.x359 + m.x360 == 0)

m.c74 = Constraint(expr= - m.x224 - m.x232 + m.x240 + m.x361 - m.x368 == 0)

m.c75 = Constraint(expr= - m.x217 - m.x225 + m.x233 - m.x361 + m.x362 == 0)

m.c76 = Constraint(expr= - m.x218 - m.x226 + m.x234 - m.x362 + m.x363 == 0)

m.c77 = Constraint(expr= - m.x219 - m.x227 + m.x235 - m.x363 + m.x364 == 0)

m.c78 = Constraint(expr= - m.x220 - m.x228 + m.x236 - m.x364 + m.x365 == 0)

m.c79 = Constraint(expr= - m.x221 - m.x229 + m.x237 - m.x365 + m.x366 == 0)

m.c80 = Constraint(expr= - m.x222 - m.x230 + m.x238 - m.x366 + m.x367 == 0)

m.c81 = Constraint(expr= - m.x223 - m.x231 + m.x239 - m.x367 + m.x368 == 0)

m.c82 = Constraint(expr=m.x409/m.x423*(m.x423 - m.x419) - m.x240 + m.x369 - m.x376 == 0)

m.c83 = Constraint(expr=m.x409/m.x423*(m.x413 - m.x412) - m.x233 - m.x369 + m.x370 == 0)

m.c84 = Constraint(expr=m.x409/m.x423*(m.x414 - m.x413) - m.x234 - m.x370 + m.x371 == 0)

m.c85 = Constraint(expr=m.x409/m.x423*(m.x415 - m.x414) - m.x235 - m.x371 + m.x372 == 0)

m.c86 = Constraint(expr=m.x409/m.x423*(m.x416 - m.x415) - m.x236 - m.x372 + m.x373 == 0)

m.c87 = Constraint(expr=m.x409/m.x423*(m.x417 - m.x416) - m.x237 - m.x373 + m.x374 == 0)

m.c88 = Constraint(expr=m.x409/m.x423*(m.x418 - m.x417) - m.x238 - m.x374 + m.x375 == 0)

m.c89 = Constraint(expr=m.x409/m.x423*(m.x419 - m.x418) - m.x239 - m.x375 + m.x376 == 0)

m.c90 = Constraint(expr= - m.x248 - m.x256 + m.x264 + m.x377 - m.x384 == 0)

m.c91 = Constraint(expr= - m.x241 - m.x249 + m.x257 - m.x377 + m.x378 == 0)

m.c92 = Constraint(expr= - m.x242 - m.x250 + m.x258 - m.x378 + m.x379 == 0)

m.c93 = Constraint(expr= - m.x243 - m.x251 + m.x259 - m.x379 + m.x380 == 0)

m.c94 = Constraint(expr= - m.x244 - m.x252 + m.x260 - m.x380 + m.x381 == 0)

m.c95 = Constraint(expr= - m.x245 - m.x253 + m.x261 - m.x381 + m.x382 == 0)

m.c96 = Constraint(expr= - m.x246 - m.x254 + m.x262 - m.x382 + m.x383 == 0)

m.c97 = Constraint(expr= - m.x247 - m.x255 + m.x263 - m.x383 + m.x384 == 0)

m.c98 = Constraint(expr=m.x410/m.x423*(m.x423 - m.x419) - m.x264 + m.x385 - m.x392 == 0)

m.c99 = Constraint(expr=m.x410/m.x423*(m.x413 - m.x412) - m.x257 - m.x385 + m.x386 == 0)

m.c100 = Constraint(expr=m.x410/m.x423*(m.x414 - m.x413) - m.x258 - m.x386 + m.x387 == 0)

m.c101 = Constraint(expr=m.x410/m.x423*(m.x415 - m.x414) - m.x259 - m.x387 + m.x388 == 0)

m.c102 = Constraint(expr=m.x410/m.x423*(m.x416 - m.x415) - m.x260 - m.x388 + m.x389 == 0)

m.c103 = Constraint(expr=m.x410/m.x423*(m.x417 - m.x416) - m.x261 - m.x389 + m.x390 == 0)

m.c104 = Constraint(expr=m.x410/m.x423*(m.x418 - m.x417) - m.x262 - m.x390 + m.x391 == 0)

m.c105 = Constraint(expr=m.x410/m.x423*(m.x419 - m.x418) - m.x263 - m.x391 + m.x392 == 0)

m.c106 = Constraint(expr= - m.x272 - m.x280 + m.x288 + m.x393 - m.x400 == 0)

m.c107 = Constraint(expr= - m.x265 - m.x273 + m.x281 - m.x393 + m.x394 == 0)

m.c108 = Constraint(expr= - m.x266 - m.x274 + m.x282 - m.x394 + m.x395 == 0)

m.c109 = Constraint(expr= - m.x267 - m.x275 + m.x283 - m.x395 + m.x396 == 0)

m.c110 = Constraint(expr= - m.x268 - m.x276 + m.x284 - m.x396 + m.x397 == 0)

m.c111 = Constraint(expr= - m.x269 - m.x277 + m.x285 - m.x397 + m.x398 == 0)

m.c112 = Constraint(expr= - m.x270 - m.x278 + m.x286 - m.x398 + m.x399 == 0)

m.c113 = Constraint(expr= - m.x271 - m.x279 + m.x287 - m.x399 + m.x400 == 0)

m.c114 = Constraint(expr=m.x411/m.x423*(m.x423 - m.x419) - m.x288 + m.x401 - m.x408 == 0)

m.c115 = Constraint(expr=m.x411/m.x423*(m.x413 - m.x412) - m.x281 - m.x401 + m.x402 == 0)

m.c116 = Constraint(expr=m.x411/m.x423*(m.x414 - m.x413) - m.x282 - m.x402 + m.x403 == 0)

m.c117 = Constraint(expr=m.x411/m.x423*(m.x415 - m.x414) - m.x283 - m.x403 + m.x404 == 0)

m.c118 = Constraint(expr=m.x411/m.x423*(m.x416 - m.x415) - m.x284 - m.x404 + m.x405 == 0)

m.c119 = Constraint(expr=m.x411/m.x423*(m.x417 - m.x416) - m.x285 - m.x405 + m.x406 == 0)

m.c120 = Constraint(expr=m.x411/m.x423*(m.x418 - m.x417) - m.x286 - m.x406 + m.x407 == 0)

m.c121 = Constraint(expr=m.x411/m.x423*(m.x419 - m.x418) - m.x287 - m.x407 + m.x408 == 0)

m.c122 = Constraint(expr=   m.b1 + m.b25 + m.b49 + m.b73 + m.b81 + m.b89 + m.b97 + m.b105 + m.b113 + m.x289 + m.x297
                          + m.x305 == 1)

m.c123 = Constraint(expr=   m.b9 + m.b33 + m.b57 + m.b121 + m.b129 + m.b137 + m.b145 + m.b153 + m.b161 + m.x313 + m.x321
                          + m.x329 == 1)

m.c124 = Constraint(expr=   m.b17 + m.b41 + m.b65 + m.b169 + m.b177 + m.b185 + m.b193 + m.b201 + m.b209 + m.x337
                          + m.x345 + m.x353 == 1)

m.c125 = Constraint(expr= - 5*m.b73 - 8*m.b81 - 10*m.b89 - 3*m.b97 - 4*m.b105 - 7*m.b113 - 0.00125*m.x217
                          - 0.000833333333333333*m.x241 - 0.001*m.x265 - m.x412 + m.x413 >= 0)

m.c126 = Constraint(expr= - 5*m.b74 - 8*m.b82 - 10*m.b90 - 3*m.b98 - 4*m.b106 - 7*m.b114 - 0.00125*m.x218
                          - 0.000833333333333333*m.x242 - 0.001*m.x266 - m.x413 + m.x414 >= 0)

m.c127 = Constraint(expr= - 5*m.b75 - 8*m.b83 - 10*m.b91 - 3*m.b99 - 4*m.b107 - 7*m.b115 - 0.00125*m.x219
                          - 0.000833333333333333*m.x243 - 0.001*m.x267 - m.x414 + m.x415 >= 0)

m.c128 = Constraint(expr= - 5*m.b76 - 8*m.b84 - 10*m.b92 - 3*m.b100 - 4*m.b108 - 7*m.b116 - 0.00125*m.x220
                          - 0.000833333333333333*m.x244 - 0.001*m.x268 - m.x415 + m.x416 >= 0)

m.c129 = Constraint(expr= - 5*m.b77 - 8*m.b85 - 10*m.b93 - 3*m.b101 - 4*m.b109 - 7*m.b117 - 0.00125*m.x221
                          - 0.000833333333333333*m.x245 - 0.001*m.x269 - m.x416 + m.x417 >= 0)

m.c130 = Constraint(expr= - 5*m.b78 - 8*m.b86 - 10*m.b94 - 3*m.b102 - 4*m.b110 - 7*m.b118 - 0.00125*m.x222
                          - 0.000833333333333333*m.x246 - 0.001*m.x270 - m.x417 + m.x418 >= 0)

m.c131 = Constraint(expr= - 5*m.b79 - 8*m.b87 - 10*m.b95 - 3*m.b103 - 4*m.b111 - 7*m.b119 - 0.00125*m.x223
                          - 0.000833333333333333*m.x247 - 0.001*m.x271 - m.x418 + m.x419 >= 0)

m.c132 = Constraint(expr= - 5*m.b80 - 8*m.b88 - 10*m.b96 - 3*m.b104 - 4*m.b112 - 7*m.b120 - 0.00125*m.x224
                          - 0.000833333333333333*m.x248 - 0.001*m.x272 - m.x419 + m.x423 >= 0)

m.c133 = Constraint(expr= - 9*m.b121 - 11*m.b129 - 5*m.b137 - 7*m.b145 - 6*m.b153 - 4*m.b161 - 0.0025*m.x225
                          - 0.002*m.x249 - 0.00222222222222222*m.x273 - m.x412 + m.x413 >= 0)

m.c134 = Constraint(expr= - 9*m.b122 - 11*m.b130 - 5*m.b138 - 7*m.b146 - 6*m.b154 - 4*m.b162 - 0.0025*m.x226
                          - 0.002*m.x250 - 0.00222222222222222*m.x274 - m.x413 + m.x414 >= 0)

m.c135 = Constraint(expr= - 9*m.b123 - 11*m.b131 - 5*m.b139 - 7*m.b147 - 6*m.b155 - 4*m.b163 - 0.0025*m.x227
                          - 0.002*m.x251 - 0.00222222222222222*m.x275 - m.x414 + m.x415 >= 0)

m.c136 = Constraint(expr= - 9*m.b124 - 11*m.b132 - 5*m.b140 - 7*m.b148 - 6*m.b156 - 4*m.b164 - 0.0025*m.x228
                          - 0.002*m.x252 - 0.00222222222222222*m.x276 - m.x415 + m.x416 >= 0)

m.c137 = Constraint(expr= - 9*m.b125 - 11*m.b133 - 5*m.b141 - 7*m.b149 - 6*m.b157 - 4*m.b165 - 0.0025*m.x229
                          - 0.002*m.x253 - 0.00222222222222222*m.x277 - m.x416 + m.x417 >= 0)

m.c138 = Constraint(expr= - 9*m.b126 - 11*m.b134 - 5*m.b142 - 7*m.b150 - 6*m.b158 - 4*m.b166 - 0.0025*m.x230
                          - 0.002*m.x254 - 0.00222222222222222*m.x278 - m.x417 + m.x418 >= 0)

m.c139 = Constraint(expr= - 9*m.b127 - 11*m.b135 - 5*m.b143 - 7*m.b151 - 6*m.b159 - 4*m.b167 - 0.0025*m.x231
                          - 0.002*m.x255 - 0.00222222222222222*m.x279 - m.x418 + m.x419 >= 0)

m.c140 = Constraint(expr= - 9*m.b128 - 11*m.b136 - 5*m.b144 - 7*m.b152 - 6*m.b160 - 4*m.b168 - 0.0025*m.x232
                          - 0.002*m.x256 - 0.00222222222222222*m.x280 - m.x419 + m.x423 >= 0)

m.c141 = Constraint(expr= - 11*m.b169 - m.b177 - 2*m.b185 - 5*m.b193 - 6*m.b201 - m.b209 - 0.00111111111111111*m.x233
                          - 0.00166666666666667*m.x257 - 0.000909090909090909*m.x281 - m.x412 + m.x413 >= 0)

m.c142 = Constraint(expr= - 11*m.b170 - m.b178 - 2*m.b186 - 5*m.b194 - 6*m.b202 - m.b210 - 0.00111111111111111*m.x234
                          - 0.00166666666666667*m.x258 - 0.000909090909090909*m.x282 - m.x413 + m.x414 >= 0)

m.c143 = Constraint(expr= - 11*m.b171 - m.b179 - 2*m.b187 - 5*m.b195 - 6*m.b203 - m.b211 - 0.00111111111111111*m.x235
                          - 0.00166666666666667*m.x259 - 0.000909090909090909*m.x283 - m.x414 + m.x415 >= 0)

m.c144 = Constraint(expr= - 11*m.b172 - m.b180 - 2*m.b188 - 5*m.b196 - 6*m.b204 - m.b212 - 0.00111111111111111*m.x236
                          - 0.00166666666666667*m.x260 - 0.000909090909090909*m.x284 - m.x415 + m.x416 >= 0)

m.c145 = Constraint(expr= - 11*m.b173 - m.b181 - 2*m.b189 - 5*m.b197 - 6*m.b205 - m.b213 - 0.00111111111111111*m.x237
                          - 0.00166666666666667*m.x261 - 0.000909090909090909*m.x285 - m.x416 + m.x417 >= 0)

m.c146 = Constraint(expr= - 11*m.b174 - m.b182 - 2*m.b190 - 5*m.b198 - 6*m.b206 - m.b214 - 0.00111111111111111*m.x238
                          - 0.00166666666666667*m.x262 - 0.000909090909090909*m.x286 - m.x417 + m.x418 >= 0)

m.c147 = Constraint(expr= - 11*m.b175 - m.b183 - 2*m.b191 - 5*m.b199 - 6*m.b207 - m.b215 - 0.00111111111111111*m.x239
                          - 0.00166666666666667*m.x263 - 0.000909090909090909*m.x287 - m.x418 + m.x419 >= 0)

m.c148 = Constraint(expr= - 11*m.b176 - m.b184 - 2*m.b192 - 5*m.b200 - 6*m.b208 - m.b216 - 0.00111111111111111*m.x240
                          - 0.00166666666666667*m.x264 - 0.000909090909090909*m.x288 - m.x419 + m.x423 >= 0)

m.c149 = Constraint(expr= - 200000*m.b1 + m.x217 <= 0)

m.c150 = Constraint(expr= - 200000*m.b2 + m.x218 <= 0)

m.c151 = Constraint(expr= - 200000*m.b3 + m.x219 <= 0)

m.c152 = Constraint(expr= - 200000*m.b4 + m.x220 <= 0)

m.c153 = Constraint(expr= - 200000*m.b5 + m.x221 <= 0)

m.c154 = Constraint(expr= - 200000*m.b6 + m.x222 <= 0)

m.c155 = Constraint(expr= - 200000*m.b7 + m.x223 <= 0)

m.c156 = Constraint(expr= - 200000*m.b8 + m.x224 <= 0)

m.c157 = Constraint(expr= - 100000*m.b9 + m.x225 <= 0)

m.c158 = Constraint(expr= - 100000*m.b10 + m.x226 <= 0)

m.c159 = Constraint(expr= - 100000*m.b11 + m.x227 <= 0)

m.c160 = Constraint(expr= - 100000*m.b12 + m.x228 <= 0)

m.c161 = Constraint(expr= - 100000*m.b13 + m.x229 <= 0)

m.c162 = Constraint(expr= - 100000*m.b14 + m.x230 <= 0)

m.c163 = Constraint(expr= - 100000*m.b15 + m.x231 <= 0)

m.c164 = Constraint(expr= - 100000*m.b16 + m.x232 <= 0)

m.c165 = Constraint(expr= - 225000*m.b17 + m.x233 <= 0)

m.c166 = Constraint(expr= - 225000*m.b18 + m.x234 <= 0)

m.c167 = Constraint(expr= - 225000*m.b19 + m.x235 <= 0)

m.c168 = Constraint(expr= - 225000*m.b20 + m.x236 <= 0)

m.c169 = Constraint(expr= - 225000*m.b21 + m.x237 <= 0)

m.c170 = Constraint(expr= - 225000*m.b22 + m.x238 <= 0)

m.c171 = Constraint(expr= - 225000*m.b23 + m.x239 <= 0)

m.c172 = Constraint(expr= - 225000*m.b24 + m.x240 <= 0)

m.c173 = Constraint(expr= - 300000*m.b25 + m.x241 <= 0)

m.c174 = Constraint(expr= - 300000*m.b26 + m.x242 <= 0)

m.c175 = Constraint(expr= - 300000*m.b27 + m.x243 <= 0)

m.c176 = Constraint(expr= - 300000*m.b28 + m.x244 <= 0)

m.c177 = Constraint(expr= - 300000*m.b29 + m.x245 <= 0)

m.c178 = Constraint(expr= - 300000*m.b30 + m.x246 <= 0)

m.c179 = Constraint(expr= - 300000*m.b31 + m.x247 <= 0)

m.c180 = Constraint(expr= - 300000*m.b32 + m.x248 <= 0)

m.c181 = Constraint(expr= - 125000*m.b33 + m.x249 <= 0)

m.c182 = Constraint(expr= - 125000*m.b34 + m.x250 <= 0)

m.c183 = Constraint(expr= - 125000*m.b35 + m.x251 <= 0)

m.c184 = Constraint(expr= - 125000*m.b36 + m.x252 <= 0)

m.c185 = Constraint(expr= - 125000*m.b37 + m.x253 <= 0)

m.c186 = Constraint(expr= - 125000*m.b38 + m.x254 <= 0)

m.c187 = Constraint(expr= - 125000*m.b39 + m.x255 <= 0)

m.c188 = Constraint(expr= - 125000*m.b40 + m.x256 <= 0)

m.c189 = Constraint(expr= - 150000*m.b41 + m.x257 <= 0)

m.c190 = Constraint(expr= - 150000*m.b42 + m.x258 <= 0)

m.c191 = Constraint(expr= - 150000*m.b43 + m.x259 <= 0)

m.c192 = Constraint(expr= - 150000*m.b44 + m.x260 <= 0)

m.c193 = Constraint(expr= - 150000*m.b45 + m.x261 <= 0)

m.c194 = Constraint(expr= - 150000*m.b46 + m.x262 <= 0)

m.c195 = Constraint(expr= - 150000*m.b47 + m.x263 <= 0)

m.c196 = Constraint(expr= - 150000*m.b48 + m.x264 <= 0)

m.c197 = Constraint(expr= - 250000*m.b49 + m.x265 <= 0)

m.c198 = Constraint(expr= - 250000*m.b50 + m.x266 <= 0)

m.c199 = Constraint(expr= - 250000*m.b51 + m.x267 <= 0)

m.c200 = Constraint(expr= - 250000*m.b52 + m.x268 <= 0)

m.c201 = Constraint(expr= - 250000*m.b53 + m.x269 <= 0)

m.c202 = Constraint(expr= - 250000*m.b54 + m.x270 <= 0)

m.c203 = Constraint(expr= - 250000*m.b55 + m.x271 <= 0)

m.c204 = Constraint(expr= - 250000*m.b56 + m.x272 <= 0)

m.c205 = Constraint(expr= - 112500*m.b57 + m.x273 <= 0)

m.c206 = Constraint(expr= - 112500*m.b58 + m.x274 <= 0)

m.c207 = Constraint(expr= - 112500*m.b59 + m.x275 <= 0)

m.c208 = Constraint(expr= - 112500*m.b60 + m.x276 <= 0)

m.c209 = Constraint(expr= - 112500*m.b61 + m.x277 <= 0)

m.c210 = Constraint(expr= - 112500*m.b62 + m.x278 <= 0)

m.c211 = Constraint(expr= - 112500*m.b63 + m.x279 <= 0)

m.c212 = Constraint(expr= - 112500*m.b64 + m.x280 <= 0)

m.c213 = Constraint(expr= - 275000*m.b65 + m.x281 <= 0)

m.c214 = Constraint(expr= - 275000*m.b66 + m.x282 <= 0)

m.c215 = Constraint(expr= - 275000*m.b67 + m.x283 <= 0)

m.c216 = Constraint(expr= - 275000*m.b68 + m.x284 <= 0)

m.c217 = Constraint(expr= - 275000*m.b69 + m.x285 <= 0)

m.c218 = Constraint(expr= - 275000*m.b70 + m.x286 <= 0)

m.c219 = Constraint(expr= - 275000*m.b71 + m.x287 <= 0)

m.c220 = Constraint(expr= - 275000*m.b72 + m.x288 <= 0)

m.c221 = Constraint(expr=   m.x409 - 50*m.x423 >= 0)

m.c222 = Constraint(expr=   m.x410 - 100*m.x423 >= 0)

m.c223 = Constraint(expr=   m.x411 - 250*m.x423 >= 0)

m.c224 = Constraint(expr=   m.x361 - m.x420 <= 0)

m.c225 = Constraint(expr=   m.x362 - m.x420 <= 0)

m.c226 = Constraint(expr=   m.x363 - m.x420 <= 0)

m.c227 = Constraint(expr=   m.x364 - m.x420 <= 0)

m.c228 = Constraint(expr=   m.x365 - m.x420 <= 0)

m.c229 = Constraint(expr=   m.x366 - m.x420 <= 0)

m.c230 = Constraint(expr=   m.x367 - m.x420 <= 0)

m.c231 = Constraint(expr=   m.x368 - m.x420 <= 0)

m.c232 = Constraint(expr=   m.x377 - m.x421 <= 0)

m.c233 = Constraint(expr=   m.x378 - m.x421 <= 0)

m.c234 = Constraint(expr=   m.x379 - m.x421 <= 0)

m.c235 = Constraint(expr=   m.x380 - m.x421 <= 0)

m.c236 = Constraint(expr=   m.x381 - m.x421 <= 0)

m.c237 = Constraint(expr=   m.x382 - m.x421 <= 0)

m.c238 = Constraint(expr=   m.x383 - m.x421 <= 0)

m.c239 = Constraint(expr=   m.x384 - m.x421 <= 0)

m.c240 = Constraint(expr=   m.x393 - m.x422 <= 0)

m.c241 = Constraint(expr=   m.x394 - m.x422 <= 0)

m.c242 = Constraint(expr=   m.x395 - m.x422 <= 0)

m.c243 = Constraint(expr=   m.x396 - m.x422 <= 0)

m.c244 = Constraint(expr=   m.x397 - m.x422 <= 0)

m.c245 = Constraint(expr=   m.x398 - m.x422 <= 0)

m.c246 = Constraint(expr=   m.x399 - m.x422 <= 0)

m.c247 = Constraint(expr=   m.x400 - m.x422 <= 0)

m.c248 = Constraint(expr=   m.b73 + m.b74 + m.b75 + m.b76 + m.b77 + m.b78 + m.b79 + m.b80 + m.b81 + m.b82 + m.b83
                          + m.b84 + m.b85 + m.b86 + m.b87 + m.b88 + m.b89 + m.b90 + m.b91 + m.b92 + m.b93 + m.b94
                          + m.b95 + m.b96 + m.b97 + m.b98 + m.b99 + m.b100 + m.b101 + m.b102 + m.b103 + m.b104 + m.b105
                          + m.b106 + m.b107 + m.b108 + m.b109 + m.b110 + m.b111 + m.b112 + m.b113 + m.b114 + m.b115
                          + m.b116 + m.b117 + m.b118 + m.b119 + m.b120 + m.b121 + m.b122 + m.b123 + m.b124 + m.b125
                          + m.b126 + m.b127 + m.b128 + m.b129 + m.b130 + m.b131 + m.b132 + m.b133 + m.b134 + m.b135
                          + m.b136 + m.b137 + m.b138 + m.b139 + m.b140 + m.b141 + m.b142 + m.b143 + m.b144 + m.b145
                          + m.b146 + m.b147 + m.b148 + m.b149 + m.b150 + m.b151 + m.b152 + m.b153 + m.b154 + m.b155
                          + m.b156 + m.b157 + m.b158 + m.b159 + m.b160 + m.b161 + m.b162 + m.b163 + m.b164 + m.b165
                          + m.b166 + m.b167 + m.b168 <= 3)

m.c249 = Constraint(expr=   m.b169 + m.b170 + m.b171 + m.b172 + m.b173 + m.b174 + m.b175 + m.b176 + m.b177 + m.b178
                          + m.b179 + m.b180 + m.b181 + m.b182 + m.b183 + m.b184 + m.b185 + m.b186 + m.b187 + m.b188
                          + m.b189 + m.b190 + m.b191 + m.b192 + m.b193 + m.b194 + m.b195 + m.b196 + m.b197 + m.b198
                          + m.b199 + m.b200 + m.b201 + m.b202 + m.b203 + m.b204 + m.b205 + m.b206 + m.b207 + m.b208
                          + m.b209 + m.b210 + m.b211 + m.b212 + m.b213 + m.b214 + m.b215 + m.b216 <= 3)

m.c250 = Constraint(expr=   m.b1 + m.b9 == 1)
