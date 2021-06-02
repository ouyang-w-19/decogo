#  MINLP written by GAMS Convert at 04/21/18 13:51:21
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       3506      436     1513     1557        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#       1178      998      180        0        0        0        0        0
#  FX     96       48       48        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#      11630    11246      384        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b6 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b9 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b12 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b15 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b18 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b19 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b21 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b23 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b24 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b25 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b26 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b27 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b28 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b29 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b30 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b31 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b32 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b33 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b34 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b35 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b36 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b38 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b39 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b40 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b41 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b42 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b43 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b44 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b45 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b46 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b47 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b48 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b49 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b50 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b51 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b52 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b53 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b54 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b55 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b56 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b57 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b58 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b59 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b60 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b61 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b62 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b63 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b64 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b65 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b66 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b67 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b68 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b69 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b70 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b71 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b72 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b73 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b74 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b75 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b76 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b77 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b78 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b79 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b80 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b81 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b82 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b83 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b84 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b85 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b86 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b87 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b88 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b89 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b90 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b91 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b92 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b93 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b94 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b95 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b96 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b97 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b98 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b99 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b100 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b101 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b102 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b103 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b104 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b105 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b106 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b109 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b112 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b115 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b118 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b121 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b124 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b127 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b128 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b129 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b130 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b131 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b132 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b133 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b134 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b135 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b136 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b137 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b138 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b139 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b140 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b141 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b142 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b143 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b144 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x217 = Var(within=Reals,bounds=(0,340),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,340),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,340),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,290),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,290),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,840),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,870),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,870),initialize=0)
m.x235 = Var(within=Reals,bounds=(0,840),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,870),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,870),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,870),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,870),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,870),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,870),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,390),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,920),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,920),initialize=0)
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
m.x406 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x407 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x408 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x409 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x410 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x411 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x412 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x413 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x414 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x415 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x416 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x417 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x418 = Var(within=Reals,bounds=(0,350),initialize=0)
m.x419 = Var(within=Reals,bounds=(0,350),initialize=0)
m.x420 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x421 = Var(within=Reals,bounds=(0,350),initialize=0)
m.x422 = Var(within=Reals,bounds=(0,350),initialize=0)
m.x423 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x424 = Var(within=Reals,bounds=(0,350),initialize=0)
m.x425 = Var(within=Reals,bounds=(0,350),initialize=0)
m.x426 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x427 = Var(within=Reals,bounds=(0,350),initialize=0)
m.x428 = Var(within=Reals,bounds=(0,350),initialize=0)
m.x429 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x430 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x431 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x432 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x433 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x434 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x435 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x436 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x437 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x438 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x439 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x440 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x441 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x442 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x443 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x444 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x445 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x446 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x447 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x448 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x449 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x450 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x451 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x452 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x453 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x454 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x455 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x456 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x457 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x458 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x459 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x460 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x461 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x462 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x463 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x464 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x465 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x466 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x467 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x468 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x469 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x470 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x471 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x472 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x473 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x474 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x475 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x476 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x477 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x478 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x479 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x480 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x481 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x482 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x483 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x484 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x485 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x486 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x487 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x488 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x489 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x490 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x491 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x492 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x493 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x494 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x495 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x496 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x497 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x498 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x499 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x500 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x501 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x502 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x503 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x504 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x505 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x506 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x507 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x508 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x509 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x510 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x511 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x512 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x513 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x514 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x515 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x516 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x517 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x518 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x519 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x520 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x521 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x522 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x523 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x524 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x525 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x526 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x527 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x528 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x529 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x530 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x531 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x532 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x533 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x534 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x535 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x536 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x537 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x538 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x539 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x540 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x541 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x542 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x543 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x544 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x545 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x546 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x547 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x548 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x549 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x550 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x551 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x552 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x553 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x554 = Var(within=Reals,bounds=(120,336),initialize=120)
m.x555 = Var(within=Reals,bounds=(120,336),initialize=120)
m.x556 = Var(within=Reals,bounds=(120,336),initialize=120)
m.x557 = Var(within=Reals,bounds=(120,336),initialize=120)
m.x558 = Var(within=Reals,bounds=(216,336),initialize=216)
m.x559 = Var(within=Reals,bounds=(216,336),initialize=216)
m.x560 = Var(within=Reals,bounds=(216,336),initialize=216)
m.x561 = Var(within=Reals,bounds=(216,336),initialize=216)
m.x562 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x563 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x564 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x565 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x566 = Var(within=Reals,bounds=(120,336),initialize=120)
m.x567 = Var(within=Reals,bounds=(120,336),initialize=120)
m.x568 = Var(within=Reals,bounds=(120,336),initialize=120)
m.x569 = Var(within=Reals,bounds=(120,336),initialize=120)
m.x570 = Var(within=Reals,bounds=(216,336),initialize=216)
m.x571 = Var(within=Reals,bounds=(216,336),initialize=216)
m.x572 = Var(within=Reals,bounds=(216,336),initialize=216)
m.x573 = Var(within=Reals,bounds=(216,336),initialize=216)
m.x574 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x575 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x576 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x577 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x578 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x579 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x580 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x581 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x582 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x583 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x584 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x585 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x586 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x587 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x588 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x589 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x590 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x591 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x592 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x593 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x594 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x595 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x596 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x597 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x598 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x599 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x600 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x601 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x602 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x603 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x604 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x605 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x606 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x607 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x608 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x609 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x610 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x611 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x612 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x613 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x614 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x615 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x616 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x617 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x618 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x619 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x620 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x621 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x622 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x623 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x624 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x625 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x626 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x627 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x628 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x629 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x630 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x631 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x632 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x633 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x634 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x635 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x636 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x637 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x638 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x639 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x640 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x641 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x642 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x643 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x644 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x645 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x646 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x647 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x648 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x649 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x650 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x651 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x652 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x653 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x654 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x655 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x656 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x657 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x658 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x659 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x660 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x661 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x662 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x663 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x664 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x665 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x666 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x667 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x668 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x669 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x670 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x671 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x672 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x673 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x674 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x675 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x676 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x677 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x678 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x679 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x680 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x681 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x682 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x683 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x684 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x685 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x686 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x687 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x688 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x689 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x690 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x691 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x692 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x693 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x694 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x695 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x696 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x697 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x698 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x699 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x700 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x701 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x702 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x703 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x704 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x705 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x706 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x707 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x708 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x709 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x710 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x711 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x712 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x713 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x714 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x715 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x716 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x717 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x718 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x719 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x720 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x721 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x722 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x723 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x724 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x725 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x726 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x727 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x728 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x729 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x730 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x731 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x732 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x733 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x734 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x735 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x736 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x737 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x738 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x739 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x740 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x741 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x742 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x743 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x744 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x745 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x746 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x747 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x748 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x749 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x750 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x751 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x752 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x753 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x754 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x755 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x756 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x757 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x758 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x759 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x760 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x761 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x762 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x763 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x764 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x765 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x766 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x767 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x768 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x769 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x770 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x771 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x772 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x773 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x774 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x775 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x776 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x777 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x778 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x779 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x780 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x781 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x782 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x783 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x784 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x785 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x786 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x787 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x788 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x789 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x790 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x791 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x792 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x793 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x794 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x795 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x796 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x797 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x798 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x799 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x800 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x801 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x802 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x803 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x804 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x805 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x806 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x807 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x808 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x809 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x810 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x811 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x812 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x813 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x814 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x815 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x816 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x817 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x818 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x819 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x820 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x821 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x822 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x823 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x824 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x825 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x826 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x827 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x828 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x829 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x830 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x831 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x832 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x833 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x834 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x835 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x836 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x837 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x838 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x839 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x840 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x841 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x842 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x843 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x844 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x845 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x846 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x847 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x848 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x849 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x850 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x851 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x852 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x853 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x854 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x855 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x856 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x857 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x858 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x859 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x860 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x861 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x862 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x863 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x864 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x865 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x866 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x867 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x868 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x869 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x870 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x871 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x872 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x873 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x874 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x875 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x876 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x877 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x878 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x879 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x880 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x881 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x882 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x883 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x884 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x885 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x886 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x887 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x888 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x889 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x890 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x891 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x892 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x893 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x894 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x895 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x896 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x897 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x898 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x899 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x900 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x901 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x902 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x903 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x904 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x905 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x906 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x907 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x908 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x909 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x910 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x911 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x912 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x913 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x914 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x915 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x916 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x917 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x918 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x919 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x920 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x921 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x922 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x923 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x924 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x925 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x926 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x927 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x928 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x929 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x930 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x931 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x932 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x933 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x934 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x935 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x936 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x937 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x938 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x939 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x940 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x941 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x942 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x943 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x944 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x945 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x946 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x947 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x948 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x949 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x950 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x951 = Var(within=Reals,bounds=(0,336),initialize=0)
m.x952 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x953 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x954 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x955 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x956 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x957 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x958 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x959 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x960 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x961 = Var(within=Reals,bounds=(110,980),initialize=110)
m.x962 = Var(within=Reals,bounds=(110,980),initialize=110)
m.x963 = Var(within=Reals,bounds=(110,980),initialize=110)
m.x964 = Var(within=Reals,bounds=(110,980),initialize=110)
m.x965 = Var(within=Reals,bounds=(110,980),initialize=110)
m.x966 = Var(within=Reals,bounds=(110,980),initialize=110)
m.x967 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x968 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x969 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x970 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x971 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x972 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x973 = Var(within=Reals,bounds=(60,980),initialize=60)
m.x974 = Var(within=Reals,bounds=(60,980),initialize=60)
m.x975 = Var(within=Reals,bounds=(60,980),initialize=60)
m.x976 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x977 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x978 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x979 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x980 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x981 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x982 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x983 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x984 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x985 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x986 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x987 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x988 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x989 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x990 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x991 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x992 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x993 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x994 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x995 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x996 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x997 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x998 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x999 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1000 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1001 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1002 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1003 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1004 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1005 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1006 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1007 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1008 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1009 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1010 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1011 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1012 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1013 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1014 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1015 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1016 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1017 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1018 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1019 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1020 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1021 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1022 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1023 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1024 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1025 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1026 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1027 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1028 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1029 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1030 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1031 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1032 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1033 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1034 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1035 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1036 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1037 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1038 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1039 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1040 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1041 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1042 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1043 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1044 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1045 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1046 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1047 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1048 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1049 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1050 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1051 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1052 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1053 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1054 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1055 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1056 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1057 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1058 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1059 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1060 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1061 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1062 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1063 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1064 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1065 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1066 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1067 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1068 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1069 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1070 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1071 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1072 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1073 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1074 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1075 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1076 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1077 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1078 = Var(within=Reals,bounds=(0.175438596491228,0.25),initialize=0.175438596491228)
m.x1079 = Var(within=Reals,bounds=(0.0184672206832872,0.25),initialize=0.0184672206832872)
m.x1080 = Var(within=Reals,bounds=(0.00194391796666181,0.25),initialize=0.00194391796666181)
m.x1081 = Var(within=Reals,bounds=(0.175438596491228,0.473684210526316),initialize=0.175438596491228)
m.x1082 = Var(within=Reals,bounds=(0.0184672206832872,0.87557603686636),initialize=0.0184672206832872)
m.x1083 = Var(within=Reals,bounds=(0.00194391796666181,0.87557603686636),initialize=0.00194391796666181)
m.x1084 = Var(within=Reals,bounds=(0.175438596491228,0.473684210526316),initialize=0.175438596491228)
m.x1085 = Var(within=Reals,bounds=(0.0184672206832872,0.944598337950138),initialize=0.0184672206832872)
m.x1086 = Var(within=Reals,bounds=(0.00194391796666181,0.981184668989547),initialize=0.00194391796666181)
m.x1087 = Var(within=Reals,bounds=(0.175438596491228,0.473684210526316),initialize=0.175438596491228)
m.x1088 = Var(within=Reals,bounds=(0.0184672206832872,0.826923076923077),initialize=0.0184672206832872)
m.x1089 = Var(within=Reals,bounds=(0.00194391796666181,0.826923076923077),initialize=0.00194391796666181)
m.x1090 = Var(within=Reals,bounds=(0.175438596491228,0.473684210526316),initialize=0.175438596491228)
m.x1091 = Var(within=Reals,bounds=(0.0184672206832872,0.892857142857143),initialize=0.0184672206832872)
m.x1092 = Var(within=Reals,bounds=(0.00194391796666181,0.892857142857143),initialize=0.00194391796666181)
m.x1093 = Var(within=Reals,bounds=(0.175438596491228,0.473684210526316),initialize=0.175438596491228)
m.x1094 = Var(within=Reals,bounds=(0.0184672206832872,0.938080495356037),initialize=0.0184672206832872)
m.x1095 = Var(within=Reals,bounds=(0.00194391796666181,0.966501240694789),initialize=0.00194391796666181)
m.x1096 = Var(within=Reals,bounds=(0.175438596491228,0.473684210526316),initialize=0.175438596491228)
m.x1097 = Var(within=Reals,bounds=(0.0184672206832872,0.82),initialize=0.0184672206832872)
m.x1098 = Var(within=Reals,bounds=(0.00194391796666181,0.82),initialize=0.00194391796666181)
m.x1099 = Var(within=Reals,bounds=(0.175438596491228,0.473684210526316),initialize=0.175438596491228)
m.x1100 = Var(within=Reals,bounds=(0.0184672206832872,0.854838709677419),initialize=0.0184672206832872)
m.x1101 = Var(within=Reals,bounds=(0.00194391796666181,0.854838709677419),initialize=0.00194391796666181)
m.x1102 = Var(within=Reals,bounds=(0.175438596491228,0.56140350877193),initialize=0.175438596491228)
m.x1103 = Var(within=Reals,bounds=(0.0184672206832872,0.897959183673469),initialize=0.0184672206832872)
m.x1104 = Var(within=Reals,bounds=(0.00194391796666181,0.897959183673469),initialize=0.00194391796666181)
m.x1105 = Var(within=Reals,bounds=(0.175438596491228,0.56140350877193),initialize=0.175438596491228)
m.x1106 = Var(within=Reals,bounds=(0.0184672206832872,0.948400412796698),initialize=0.0184672206832872)
m.x1107 = Var(within=Reals,bounds=(0.00194391796666181,0.968096419709323),initialize=0.00194391796666181)
m.x1108 = Var(within=Reals,bounds=(0.087719298245614,0.444444444444444),initialize=0.087719298245614)
m.x1109 = Var(within=Reals,bounds=(0.00923361034164358,0.794285714285714),initialize=0.00923361034164358)
m.x1110 = Var(within=Reals,bounds=(0.000971958983330903,0.794285714285714),initialize=0.000971958983330903)
m.x1111 = Var(within=Reals,bounds=(0.175438596491228,0.56140350877193),initialize=0.175438596491228)
m.x1112 = Var(within=Reals,bounds=(0.0184672206832872,0.861751152073733),initialize=0.0184672206832872)
m.x1113 = Var(within=Reals,bounds=(0.00194391796666181,0.861751152073733),initialize=0.00194391796666181)
m.x1114 = Var(within=Reals,bounds=(0.204081632653061,0.23469387755102),initialize=0.204081632653061)
m.x1115 = Var(within=Reals,bounds=(0.0229071220324865,0.799562682215743),initialize=0.0229071220324865)
m.x1116 = Var(within=Reals,bounds=(0.00257120757507501,0.80584082156611),initialize=0.00257120757507501)
m.x1117 = Var(within=Reals,bounds=(0.255102040816327,0.285714285714286),initialize=0.255102040816327)
m.x1118 = Var(within=Reals,bounds=(0.0286339025406081,0.85969387755102),initialize=0.0286339025406081)
m.x1119 = Var(within=Reals,bounds=(0.00321400946884376,0.920109413318242),initialize=0.00321400946884376)
m.x1120 = Var(within=Reals,bounds=(0.204081632653061,0.23469387755102),initialize=0.204081632653061)
m.x1121 = Var(within=Reals,bounds=(0.0229071220324865,0.710526315789474),initialize=0.0229071220324865)
m.x1122 = Var(within=Reals,bounds=(0.00257120757507501,0.710526315789474),initialize=0.00257120757507501)
m.x1123 = Var(within=Reals,bounds=(0.306122448979592,0.336734693877551),initialize=0.306122448979592)
m.x1124 = Var(within=Reals,bounds=(0.0343606830487297,0.79093567251462),initialize=0.0343606830487297)
m.x1125 = Var(within=Reals,bounds=(0.00385681136261252,0.79093567251462),initialize=0.00385681136261252)
m.x1126 = Var(within=Reals,bounds=(0.076530612244898,0.631147540983607),initialize=0.076530612244898)
m.x1127 = Var(within=Reals,bounds=(0.00859017076218242,0.815548780487805),initialize=0.00859017076218242)
m.x1128 = Var(within=Reals,bounds=(0.000964202840653129,0.815548780487805),initialize=0.000964202840653129)
m.x1129 = Var(within=Reals,bounds=(0.076530612244898,0.7),initialize=0.076530612244898)
m.x1130 = Var(within=Reals,bounds=(0.00859017076218242,0.918682795698925),initialize=0.00859017076218242)
m.x1131 = Var(within=Reals,bounds=(0.000964202840653129,0.918682795698925),initialize=0.000964202840653129)
m.x1132 = Var(within=Reals,bounds=(0.076530612244898,0.540816326530612),initialize=0.076530612244898)
m.x1133 = Var(within=Reals,bounds=(0.00859017076218242,0.725),initialize=0.00859017076218242)
m.x1134 = Var(within=Reals,bounds=(0.000964202840653129,0.725),initialize=0.000964202840653129)
m.x1135 = Var(within=Reals,bounds=(0.076530612244898,0.590909090909091),initialize=0.076530612244898)
m.x1136 = Var(within=Reals,bounds=(0.00859017076218242,0.770833333333333),initialize=0.00859017076218242)
m.x1137 = Var(within=Reals,bounds=(0.000964202840653129,0.770833333333333),initialize=0.000964202840653129)
m.x1138 = Var(within=Reals,bounds=(0.0350877192982456,0.25),initialize=0.0350877192982456)
m.x1139 = Var(within=Reals,bounds=(0.00369344413665743,0.25),initialize=0.00369344413665743)
m.x1140 = Var(within=Reals,bounds=(0.000388783593332361,0.25),initialize=0.000388783593332361)
m.x1141 = Var(within=Reals,bounds=(0.0350877192982456,0.823529411764706),initialize=0.0350877192982456)
m.x1142 = Var(within=Reals,bounds=(0.00369344413665743,0.87557603686636),initialize=0.00369344413665743)
m.x1143 = Var(within=Reals,bounds=(0.000388783593332361,0.87557603686636),initialize=0.000388783593332361)
m.x1144 = Var(within=Reals,bounds=(0.037037037037037,0.894736842105263),initialize=0.037037037037037)
m.x1145 = Var(within=Reals,bounds=(0.00389863547758285,0.981184668989547),initialize=0.00389863547758285)
m.x1146 = Var(within=Reals,bounds=(0.000410382681850826,0.981184668989547),initialize=0.000410382681850826)
m.x1147 = Var(within=Reals,bounds=(0.0350877192982456,0.785714285714286),initialize=0.0350877192982456)
m.x1148 = Var(within=Reals,bounds=(0.00369344413665743,0.826923076923077),initialize=0.00369344413665743)
m.x1149 = Var(within=Reals,bounds=(0.000388783593332361,0.826923076923077),initialize=0.000388783593332361)
m.x1150 = Var(within=Reals,bounds=(0.0350877192982456,0.25),initialize=0.0350877192982456)
m.x1151 = Var(within=Reals,bounds=(0.00369344413665743,0.25),initialize=0.00369344413665743)
m.x1152 = Var(within=Reals,bounds=(0.000388783593332361,0.25),initialize=0.000388783593332361)
m.x1153 = Var(within=Reals,bounds=(0.0350877192982456,0.823529411764706),initialize=0.0350877192982456)
m.x1154 = Var(within=Reals,bounds=(0.00369344413665743,0.87557603686636),initialize=0.00369344413665743)
m.x1155 = Var(within=Reals,bounds=(0.000388783593332361,0.87557603686636),initialize=0.000388783593332361)
m.x1156 = Var(within=Reals,bounds=(0.037037037037037,0.894736842105263),initialize=0.037037037037037)
m.x1157 = Var(within=Reals,bounds=(0.00389863547758285,0.981184668989547),initialize=0.00389863547758285)
m.x1158 = Var(within=Reals,bounds=(0.000410382681850826,0.981184668989547),initialize=0.000410382681850826)
m.x1159 = Var(within=Reals,bounds=(0.0350877192982456,0.785714285714286),initialize=0.0350877192982456)
m.x1160 = Var(within=Reals,bounds=(0.00369344413665743,0.826923076923077),initialize=0.00369344413665743)
m.x1161 = Var(within=Reals,bounds=(0.000388783593332361,0.826923076923077),initialize=0.000388783593332361)
m.x1162 = Var(within=Reals,bounds=(0.102040816326531,0.222222222222222),initialize=0.102040816326531)
m.x1163 = Var(within=Reals,bounds=(0.00624739691795085,0.222222222222222),initialize=0.00624739691795085)
m.x1164 = Var(within=Reals,bounds=(0.000382493688854134,0.222222222222222),initialize=0.000382493688854134)
m.x1165 = Var(within=Reals,bounds=(0.102040816326531,0.507042253521127),initialize=0.102040816326531)
m.x1166 = Var(within=Reals,bounds=(0.00624739691795085,0.870967741935484),initialize=0.00624739691795085)
m.x1167 = Var(within=Reals,bounds=(0.000382493688854134,0.870967741935484),initialize=0.000382493688854134)
m.x1168 = Var(within=Reals,bounds=(0.10989010989011,0.642857142857143),initialize=0.10989010989011)
m.x1169 = Var(within=Reals,bounds=(0.00672796591163938,0.967532467532467),initialize=0.00672796591163938)
m.x1170 = Var(within=Reals,bounds=(0.000411916280304452,0.980487804878049),initialize=0.000411916280304452)
m.x1171 = Var(within=Reals,bounds=(0.153061224489796,0.538461538461538),initialize=0.153061224489796)
m.x1172 = Var(within=Reals,bounds=(0.00937109537692628,0.846153846153846),initialize=0.00937109537692628)
m.x1173 = Var(within=Reals,bounds=(0.000573740533281201,0.846153846153846),initialize=0.000573740533281201)
m.x1174 = Var(within=Reals,bounds=(0,1500),initialize=0)
m.x1175 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1176 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1177 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   1.5*m.x253 + 1.5*m.x254 + 1.5*m.x255 + 1.7*m.x256 + 1.7*m.x257 + 1.7*m.x258 + 1.5*m.x259
                        + 1.5*m.x260 + 1.5*m.x261 + 1.6*m.x262 + 1.6*m.x263 + 1.6*m.x264 + 1.45*m.x265 + 1.45*m.x266
                        + 1.45*m.x267 + 1.6*m.x268 + 1.6*m.x269 + 1.6*m.x270 + 1.55*m.x271 + 1.55*m.x272 + 1.55*m.x273
                        + 1.6*m.x274 + 1.6*m.x275 + 1.6*m.x276 + 1.45*m.x277 + 1.45*m.x278 + 1.45*m.x279 + 1.6*m.x280
                        + 1.6*m.x281 + 1.6*m.x282 + 1.55*m.x283 + 1.55*m.x284 + 1.55*m.x285 + 1.6*m.x286 + 1.6*m.x287
                        + 1.6*m.x288 + 1.45*m.x289 + 1.45*m.x290 + 1.45*m.x291 + 1.6*m.x292 + 1.6*m.x293 + 1.6*m.x294
                        + 1.55*m.x295 + 1.55*m.x296 + 1.55*m.x297 + 1.6*m.x298 + 1.6*m.x299 + 1.6*m.x300 + 1.45*m.x301
                        + 1.45*m.x302 + 1.45*m.x303 + 1.6*m.x304 + 1.6*m.x305 + 1.6*m.x306 + 1.55*m.x307 + 1.55*m.x308
                        + 1.55*m.x309 + 1.6*m.x310 + 1.6*m.x311 + 1.6*m.x312 + 1.45*m.x313 + 1.45*m.x314 + 1.45*m.x315
                        + 1.6*m.x316 + 1.6*m.x317 + 1.6*m.x318 + 1.55*m.x319 + 1.55*m.x320 + 1.55*m.x321 + 1.6*m.x322
                        + 1.6*m.x323 + 1.6*m.x324 + 1.45*m.x325 + 1.45*m.x326 + 1.45*m.x327 + 1.6*m.x328 + 1.6*m.x329
                        + 1.6*m.x330 + 1.55*m.x331 + 1.55*m.x332 + 1.55*m.x333 + 1.6*m.x334 + 1.6*m.x335 + 1.6*m.x336
                        + 1.45*m.x337 + 1.45*m.x338 + 1.45*m.x339 + 1.6*m.x340 + 1.6*m.x341 + 1.6*m.x342 + 1.55*m.x343
                        + 1.55*m.x344 + 1.55*m.x345 + 1.6*m.x346 + 1.6*m.x347 + 1.6*m.x348 + 1.45*m.x349 + 1.45*m.x350
                        + 1.45*m.x351 + 1.6*m.x352 + 1.6*m.x353 + 1.6*m.x354 + 1.55*m.x355 + 1.55*m.x356 + 1.55*m.x357
                        + 1.6*m.x358 + 1.6*m.x359 + 1.6*m.x360 + 1.5*m.x361 + 1.5*m.x362 + 1.5*m.x363 + 1.7*m.x364
                        + 1.7*m.x365 + 1.7*m.x366 + 1.5*m.x367 + 1.5*m.x368 + 1.5*m.x369 + 1.6*m.x370 + 1.6*m.x371
                        + 1.6*m.x372 + 1.5*m.x373 + 1.5*m.x374 + 1.5*m.x375 + 1.7*m.x376 + 1.7*m.x377 + 1.7*m.x378
                        + 1.5*m.x379 + 1.5*m.x380 + 1.5*m.x381 + 1.6*m.x382 + 1.6*m.x383 + 1.6*m.x384 + 1.5*m.x385
                        + 1.5*m.x386 + 1.5*m.x387 + 1.7*m.x388 + 1.7*m.x389 + 1.7*m.x390 + 1.5*m.x391 + 1.5*m.x392
                        + 1.5*m.x393 + 1.6*m.x394 + 1.6*m.x395 + 1.6*m.x396 - 10*m.x1072 - 10*m.x1073 - 10*m.x1074
                        - 10*m.x1075 - 10*m.x1076 - 10*m.x1077 - 0.84*m.x1174 - m.x1175 - m.x1176 - m.x1177
                       , sense=maximize)

m.c1 = Constraint(expr=   m.b1 + m.b4 + m.b7 + m.b10 <= 1)

m.c2 = Constraint(expr=   m.b2 + m.b5 + m.b8 + m.b11 <= 1)

m.c3 = Constraint(expr=   m.b3 + m.b6 + m.b9 + m.b12 <= 1)

m.c4 = Constraint(expr=   m.b13 + m.b16 + m.b19 + m.b22 <= 1)

m.c5 = Constraint(expr=   m.b14 + m.b17 + m.b20 + m.b23 <= 1)

m.c6 = Constraint(expr=   m.b15 + m.b18 + m.b21 + m.b24 <= 1)

m.c7 = Constraint(expr=   m.b25 + m.b28 + m.b31 + m.b34 <= 1)

m.c8 = Constraint(expr=   m.b26 + m.b29 + m.b32 + m.b35 <= 1)

m.c9 = Constraint(expr=   m.b27 + m.b30 + m.b33 + m.b36 <= 1)

m.c10 = Constraint(expr=   m.b37 + m.b40 + m.b43 + m.b46 <= 1)

m.c11 = Constraint(expr=   m.b38 + m.b41 + m.b44 + m.b47 <= 1)

m.c12 = Constraint(expr=   m.b39 + m.b42 + m.b45 + m.b48 <= 1)

m.c13 = Constraint(expr=   m.b49 + m.b52 + m.b55 + m.b58 <= 1)

m.c14 = Constraint(expr=   m.b50 + m.b53 + m.b56 + m.b59 <= 1)

m.c15 = Constraint(expr=   m.b51 + m.b54 + m.b57 + m.b60 <= 1)

m.c16 = Constraint(expr=   m.b61 + m.b64 + m.b67 + m.b70 <= 1)

m.c17 = Constraint(expr=   m.b62 + m.b65 + m.b68 + m.b71 <= 1)

m.c18 = Constraint(expr=   m.b63 + m.b66 + m.b69 + m.b72 <= 1)

m.c19 = Constraint(expr=   m.b73 + m.b76 + m.b79 + m.b82 <= 1)

m.c20 = Constraint(expr=   m.b74 + m.b77 + m.b80 + m.b83 <= 1)

m.c21 = Constraint(expr=   m.b75 + m.b78 + m.b81 + m.b84 <= 1)

m.c22 = Constraint(expr=   m.b85 + m.b88 + m.b91 + m.b94 <= 1)

m.c23 = Constraint(expr=   m.b86 + m.b89 + m.b92 + m.b95 <= 1)

m.c24 = Constraint(expr=   m.b87 + m.b90 + m.b93 + m.b96 <= 1)

m.c25 = Constraint(expr=   m.b97 + m.b100 + m.b103 + m.b106 <= 1)

m.c26 = Constraint(expr=   m.b98 + m.b101 + m.b104 + m.b107 <= 1)

m.c27 = Constraint(expr=   m.b99 + m.b102 + m.b105 + m.b108 <= 1)

m.c28 = Constraint(expr=   m.b109 + m.b112 + m.b115 + m.b118 <= 1)

m.c29 = Constraint(expr=   m.b110 + m.b113 + m.b116 + m.b119 <= 1)

m.c30 = Constraint(expr=   m.b111 + m.b114 + m.b117 + m.b120 <= 1)

m.c31 = Constraint(expr=   m.b121 + m.b124 + m.b127 + m.b130 <= 1)

m.c32 = Constraint(expr=   m.b122 + m.b125 + m.b128 + m.b131 <= 1)

m.c33 = Constraint(expr=   m.b123 + m.b126 + m.b129 + m.b132 <= 1)

m.c34 = Constraint(expr=   m.b133 + m.b136 + m.b139 + m.b142 <= 1)

m.c35 = Constraint(expr=   m.b134 + m.b137 + m.b140 + m.b143 <= 1)

m.c36 = Constraint(expr=   m.b135 + m.b138 + m.b141 + m.b144 <= 1)

m.c37 = Constraint(expr=   m.b1 + m.b2 + m.b4 + m.b5 + m.b7 + m.b8 + m.b10 + m.b11 + m.x145 <= 2)

m.c38 = Constraint(expr=   m.b2 + m.b3 + m.b5 + m.b6 + m.b8 + m.b9 + m.b11 + m.b12 + m.x146 <= 2)

m.c39 = Constraint(expr=   m.b13 + m.b14 + m.b16 + m.b17 + m.b19 + m.b20 + m.b22 + m.b23 + m.x148 <= 2)

m.c40 = Constraint(expr=   m.b14 + m.b15 + m.b17 + m.b18 + m.b20 + m.b21 + m.b23 + m.b24 + m.x149 <= 2)

m.c41 = Constraint(expr=   m.b25 + m.b26 + m.b28 + m.b29 + m.b31 + m.b32 + m.b34 + m.b35 + m.x151 <= 2)

m.c42 = Constraint(expr=   m.b26 + m.b27 + m.b29 + m.b30 + m.b32 + m.b33 + m.b35 + m.b36 + m.x152 <= 2)

m.c43 = Constraint(expr=   m.b37 + m.b38 + m.b40 + m.b41 + m.b43 + m.b44 + m.b46 + m.b47 + m.x154 <= 2)

m.c44 = Constraint(expr=   m.b38 + m.b39 + m.b41 + m.b42 + m.b44 + m.b45 + m.b47 + m.b48 + m.x155 <= 2)

m.c45 = Constraint(expr=   m.b49 + m.b50 + m.b52 + m.b53 + m.b55 + m.b56 + m.b58 + m.b59 + m.x157 <= 2)

m.c46 = Constraint(expr=   m.b50 + m.b51 + m.b53 + m.b54 + m.b56 + m.b57 + m.b59 + m.b60 + m.x158 <= 2)

m.c47 = Constraint(expr=   m.b61 + m.b62 + m.b64 + m.b65 + m.b67 + m.b68 + m.b70 + m.b71 + m.x160 <= 2)

m.c48 = Constraint(expr=   m.b62 + m.b63 + m.b65 + m.b66 + m.b68 + m.b69 + m.b71 + m.b72 + m.x161 <= 2)

m.c49 = Constraint(expr=   m.b73 + m.b74 + m.b76 + m.b77 + m.b79 + m.b80 + m.b82 + m.b83 + m.x163 <= 2)

m.c50 = Constraint(expr=   m.b74 + m.b75 + m.b77 + m.b78 + m.b80 + m.b81 + m.b83 + m.b84 + m.x164 <= 2)

m.c51 = Constraint(expr=   m.b85 + m.b86 + m.b88 + m.b89 + m.b91 + m.b92 + m.b94 + m.b95 + m.x166 <= 2)

m.c52 = Constraint(expr=   m.b86 + m.b87 + m.b89 + m.b90 + m.b92 + m.b93 + m.b95 + m.b96 + m.x167 <= 2)

m.c53 = Constraint(expr=   m.b97 + m.b98 + m.b100 + m.b101 + m.b103 + m.b104 + m.b106 + m.b107 + m.x169 <= 2)

m.c54 = Constraint(expr=   m.b98 + m.b99 + m.b101 + m.b102 + m.b104 + m.b105 + m.b107 + m.b108 + m.x170 <= 2)

m.c55 = Constraint(expr=   m.b109 + m.b110 + m.b112 + m.b113 + m.b115 + m.b116 + m.b118 + m.b119 + m.x172 <= 2)

m.c56 = Constraint(expr=   m.b110 + m.b111 + m.b113 + m.b114 + m.b116 + m.b117 + m.b119 + m.b120 + m.x173 <= 2)

m.c57 = Constraint(expr=   m.b121 + m.b122 + m.b124 + m.b125 + m.b127 + m.b128 + m.b130 + m.b131 + m.x175 <= 2)

m.c58 = Constraint(expr=   m.b122 + m.b123 + m.b125 + m.b126 + m.b128 + m.b129 + m.b131 + m.b132 + m.x176 <= 2)

m.c59 = Constraint(expr=   m.b133 + m.b134 + m.b136 + m.b137 + m.b139 + m.b140 + m.b142 + m.b143 + m.x178 <= 2)

m.c60 = Constraint(expr=   m.b134 + m.b135 + m.b137 + m.b138 + m.b140 + m.b141 + m.b143 + m.b144 + m.x179 <= 2)

m.c61 = Constraint(expr= - m.b1 + m.b2 - m.b4 + m.b5 - m.b7 + m.b8 - m.b10 + m.b11 + m.x145 >= 0)

m.c62 = Constraint(expr= - m.b2 + m.b3 - m.b5 + m.b6 - m.b8 + m.b9 - m.b11 + m.b12 + m.x146 >= 0)

m.c63 = Constraint(expr= - m.b13 + m.b14 - m.b16 + m.b17 - m.b19 + m.b20 - m.b22 + m.b23 + m.x148 >= 0)

m.c64 = Constraint(expr= - m.b14 + m.b15 - m.b17 + m.b18 - m.b20 + m.b21 - m.b23 + m.b24 + m.x149 >= 0)

m.c65 = Constraint(expr= - m.b25 + m.b26 - m.b28 + m.b29 - m.b31 + m.b32 - m.b34 + m.b35 + m.x151 >= 0)

m.c66 = Constraint(expr= - m.b26 + m.b27 - m.b29 + m.b30 - m.b32 + m.b33 - m.b35 + m.b36 + m.x152 >= 0)

m.c67 = Constraint(expr= - m.b37 + m.b38 - m.b40 + m.b41 - m.b43 + m.b44 - m.b46 + m.b47 + m.x154 >= 0)

m.c68 = Constraint(expr= - m.b38 + m.b39 - m.b41 + m.b42 - m.b44 + m.b45 - m.b47 + m.b48 + m.x155 >= 0)

m.c69 = Constraint(expr= - m.b49 + m.b50 - m.b52 + m.b53 - m.b55 + m.b56 - m.b58 + m.b59 + m.x157 >= 0)

m.c70 = Constraint(expr= - m.b50 + m.b51 - m.b53 + m.b54 - m.b56 + m.b57 - m.b59 + m.b60 + m.x158 >= 0)

m.c71 = Constraint(expr= - m.b61 + m.b62 - m.b64 + m.b65 - m.b67 + m.b68 - m.b70 + m.b71 + m.x160 >= 0)

m.c72 = Constraint(expr= - m.b62 + m.b63 - m.b65 + m.b66 - m.b68 + m.b69 - m.b71 + m.b72 + m.x161 >= 0)

m.c73 = Constraint(expr= - m.b73 + m.b74 - m.b76 + m.b77 - m.b79 + m.b80 - m.b82 + m.b83 + m.x163 >= 0)

m.c74 = Constraint(expr= - m.b74 + m.b75 - m.b77 + m.b78 - m.b80 + m.b81 - m.b83 + m.b84 + m.x164 >= 0)

m.c75 = Constraint(expr= - m.b85 + m.b86 - m.b88 + m.b89 - m.b91 + m.b92 - m.b94 + m.b95 + m.x166 >= 0)

m.c76 = Constraint(expr= - m.b86 + m.b87 - m.b89 + m.b90 - m.b92 + m.b93 - m.b95 + m.b96 + m.x167 >= 0)

m.c77 = Constraint(expr= - m.b97 + m.b98 - m.b100 + m.b101 - m.b103 + m.b104 - m.b106 + m.b107 + m.x169 >= 0)

m.c78 = Constraint(expr= - m.b98 + m.b99 - m.b101 + m.b102 - m.b104 + m.b105 - m.b107 + m.b108 + m.x170 >= 0)

m.c79 = Constraint(expr= - m.b109 + m.b110 - m.b112 + m.b113 - m.b115 + m.b116 - m.b118 + m.b119 + m.x172 >= 0)

m.c80 = Constraint(expr= - m.b110 + m.b111 - m.b113 + m.b114 - m.b116 + m.b117 - m.b119 + m.b120 + m.x173 >= 0)

m.c81 = Constraint(expr= - m.b121 + m.b122 - m.b124 + m.b125 - m.b127 + m.b128 - m.b130 + m.b131 + m.x175 >= 0)

m.c82 = Constraint(expr= - m.b122 + m.b123 - m.b125 + m.b126 - m.b128 + m.b129 - m.b131 + m.b132 + m.x176 >= 0)

m.c83 = Constraint(expr= - m.b133 + m.b134 - m.b136 + m.b137 - m.b139 + m.b140 - m.b142 + m.b143 + m.x178 >= 0)

m.c84 = Constraint(expr= - m.b134 + m.b135 - m.b137 + m.b138 - m.b140 + m.b141 - m.b143 + m.b144 + m.x179 >= 0)

m.c85 = Constraint(expr= - m.b3 - m.b6 - m.b9 - m.b12 + m.x147 >= 0)

m.c86 = Constraint(expr= - m.b15 - m.b18 - m.b21 - m.b24 + m.x150 >= 0)

m.c87 = Constraint(expr= - m.b27 - m.b30 - m.b33 - m.b36 + m.x153 >= 0)

m.c88 = Constraint(expr= - m.b39 - m.b42 - m.b45 - m.b48 + m.x156 >= 0)

m.c89 = Constraint(expr= - m.b51 - m.b54 - m.b57 - m.b60 + m.x159 >= 0)

m.c90 = Constraint(expr= - m.b63 - m.b66 - m.b69 - m.b72 + m.x162 >= 0)

m.c91 = Constraint(expr= - m.b75 - m.b78 - m.b81 - m.b84 + m.x165 >= 0)

m.c92 = Constraint(expr= - m.b87 - m.b90 - m.b93 - m.b96 + m.x168 >= 0)

m.c93 = Constraint(expr= - m.b99 - m.b102 - m.b105 - m.b108 + m.x171 >= 0)

m.c94 = Constraint(expr= - m.b111 - m.b114 - m.b117 - m.b120 + m.x174 >= 0)

m.c95 = Constraint(expr= - m.b123 - m.b126 - m.b129 - m.b132 + m.x177 >= 0)

m.c96 = Constraint(expr= - m.b135 - m.b138 - m.b141 - m.b144 + m.x180 >= 0)

m.c97 = Constraint(expr=   m.x145 + m.x146 + m.x147 == 1)

m.c98 = Constraint(expr=   m.x148 + m.x149 + m.x150 == 1)

m.c99 = Constraint(expr=   m.x151 + m.x152 + m.x153 == 1)

m.c100 = Constraint(expr=   m.x154 + m.x155 + m.x156 == 1)

m.c101 = Constraint(expr=   m.x157 + m.x158 + m.x159 == 1)

m.c102 = Constraint(expr=   m.x160 + m.x161 + m.x162 == 1)

m.c103 = Constraint(expr=   m.x163 + m.x164 + m.x165 == 1)

m.c104 = Constraint(expr=   m.x166 + m.x167 + m.x168 == 1)

m.c105 = Constraint(expr=   m.x169 + m.x170 + m.x171 == 1)

m.c106 = Constraint(expr=   m.x172 + m.x173 + m.x174 == 1)

m.c107 = Constraint(expr=   m.x175 + m.x176 + m.x177 == 1)

m.c108 = Constraint(expr=   m.x178 + m.x179 + m.x180 == 1)

m.c109 = Constraint(expr= - m.x406 - 1.25*m.x574 + 1.25*m.x718 <= 0)

m.c110 = Constraint(expr= - m.x407 - 1.25*m.x575 + 1.25*m.x719 <= 0)

m.c111 = Constraint(expr= - m.x408 - 1.25*m.x576 + 1.25*m.x720 <= 0)

m.c112 = Constraint(expr= - m.x409 - 1.25*m.x577 + 1.25*m.x721 <= 0)

m.c113 = Constraint(expr= - m.x410 - 1.25*m.x578 + 1.25*m.x722 <= 0)

m.c114 = Constraint(expr= - m.x411 - 1.25*m.x579 + 1.25*m.x723 <= 0)

m.c115 = Constraint(expr= - m.x412 - 1.25*m.x580 + 1.25*m.x724 <= 0)

m.c116 = Constraint(expr= - m.x413 - 1.25*m.x581 + 1.25*m.x725 <= 0)

m.c117 = Constraint(expr= - m.x414 - 1.25*m.x582 + 1.25*m.x726 <= 0)

m.c118 = Constraint(expr= - m.x415 - 1.25*m.x583 + 1.25*m.x727 <= 0)

m.c119 = Constraint(expr= - m.x416 - 1.25*m.x584 + 1.25*m.x728 <= 0)

m.c120 = Constraint(expr= - m.x417 - 1.25*m.x585 + 1.25*m.x729 <= 0)

m.c121 = Constraint(expr= - m.x418 - 1.25*m.x586 + 1.25*m.x730 <= 0)

m.c122 = Constraint(expr= - m.x419 - 1.25*m.x587 + 1.25*m.x731 <= 0)

m.c123 = Constraint(expr= - m.x420 - 1.25*m.x588 + 1.25*m.x732 <= 0)

m.c124 = Constraint(expr= - m.x421 - 1.25*m.x589 + 1.25*m.x733 <= 0)

m.c125 = Constraint(expr= - m.x422 - 1.25*m.x590 + 1.25*m.x734 <= 0)

m.c126 = Constraint(expr= - m.x423 - 1.25*m.x591 + 1.25*m.x735 <= 0)

m.c127 = Constraint(expr= - m.x424 - 1.25*m.x592 + 1.25*m.x736 <= 0)

m.c128 = Constraint(expr= - m.x425 - 1.25*m.x593 + 1.25*m.x737 <= 0)

m.c129 = Constraint(expr= - m.x426 - 1.25*m.x594 + 1.25*m.x738 <= 0)

m.c130 = Constraint(expr= - m.x427 - 1.25*m.x595 + 1.25*m.x739 <= 0)

m.c131 = Constraint(expr= - m.x428 - 1.25*m.x596 + 1.25*m.x740 <= 0)

m.c132 = Constraint(expr= - m.x429 - 1.25*m.x597 + 1.25*m.x741 <= 0)

m.c133 = Constraint(expr= - m.x430 - 1.25*m.x598 + 1.25*m.x742 <= 0)

m.c134 = Constraint(expr= - m.x431 - 1.25*m.x599 + 1.25*m.x743 <= 0)

m.c135 = Constraint(expr= - m.x432 - 1.25*m.x600 + 1.25*m.x744 <= 0)

m.c136 = Constraint(expr= - m.x433 - 1.25*m.x601 + 1.25*m.x745 <= 0)

m.c137 = Constraint(expr= - m.x434 - 1.25*m.x602 + 1.25*m.x746 <= 0)

m.c138 = Constraint(expr= - m.x435 - 1.25*m.x603 + 1.25*m.x747 <= 0)

m.c139 = Constraint(expr= - m.x436 - 1.25*m.x604 + 1.25*m.x748 <= 0)

m.c140 = Constraint(expr= - m.x437 - 1.25*m.x605 + 1.25*m.x749 <= 0)

m.c141 = Constraint(expr= - m.x438 - 1.25*m.x606 + 1.25*m.x750 <= 0)

m.c142 = Constraint(expr= - m.x439 - 1.25*m.x607 + 1.25*m.x751 <= 0)

m.c143 = Constraint(expr= - m.x440 - 1.25*m.x608 + 1.25*m.x752 <= 0)

m.c144 = Constraint(expr= - m.x441 - 1.25*m.x609 + 1.25*m.x753 <= 0)

m.c145 = Constraint(expr= - m.x442 - 1.25*m.x610 + 1.25*m.x754 <= 0)

m.c146 = Constraint(expr= - m.x443 - 1.25*m.x611 + 1.25*m.x755 <= 0)

m.c147 = Constraint(expr= - m.x444 - 1.25*m.x612 + 1.25*m.x756 <= 0)

m.c148 = Constraint(expr= - m.x445 - 1.25*m.x613 + 1.25*m.x757 <= 0)

m.c149 = Constraint(expr= - m.x446 - 1.25*m.x614 + 1.25*m.x758 <= 0)

m.c150 = Constraint(expr= - m.x447 - 1.25*m.x615 + 1.25*m.x759 <= 0)

m.c151 = Constraint(expr= - m.x448 - 1.25*m.x616 + 1.25*m.x760 <= 0)

m.c152 = Constraint(expr= - m.x449 - 1.25*m.x617 + 1.25*m.x761 <= 0)

m.c153 = Constraint(expr= - m.x450 - 1.25*m.x618 + 1.25*m.x762 <= 0)

m.c154 = Constraint(expr= - m.x451 - 1.25*m.x619 + 1.25*m.x763 <= 0)

m.c155 = Constraint(expr= - m.x452 - 1.25*m.x620 + 1.25*m.x764 <= 0)

m.c156 = Constraint(expr= - m.x453 - 1.25*m.x621 + 1.25*m.x765 <= 0)

m.c157 = Constraint(expr= - m.x454 - 1.25*m.x622 + 1.25*m.x766 <= 0)

m.c158 = Constraint(expr= - m.x455 - 1.25*m.x623 + 1.25*m.x767 <= 0)

m.c159 = Constraint(expr= - m.x456 - 1.25*m.x624 + 1.25*m.x768 <= 0)

m.c160 = Constraint(expr= - m.x457 - 1.25*m.x625 + 1.25*m.x769 <= 0)

m.c161 = Constraint(expr= - m.x458 - 1.25*m.x626 + 1.25*m.x770 <= 0)

m.c162 = Constraint(expr= - m.x459 - 1.25*m.x627 + 1.25*m.x771 <= 0)

m.c163 = Constraint(expr= - m.x460 - 1.25*m.x628 + 1.25*m.x772 <= 0)

m.c164 = Constraint(expr= - m.x461 - 1.25*m.x629 + 1.25*m.x773 <= 0)

m.c165 = Constraint(expr= - m.x462 - 1.25*m.x630 + 1.25*m.x774 <= 0)

m.c166 = Constraint(expr= - m.x463 - 1.25*m.x631 + 1.25*m.x775 <= 0)

m.c167 = Constraint(expr= - m.x464 - 1.25*m.x632 + 1.25*m.x776 <= 0)

m.c168 = Constraint(expr= - m.x465 - 1.25*m.x633 + 1.25*m.x777 <= 0)

m.c169 = Constraint(expr= - m.x466 - 1.25*m.x634 + 1.25*m.x778 <= 0)

m.c170 = Constraint(expr= - m.x467 - 1.25*m.x635 + 1.25*m.x779 <= 0)

m.c171 = Constraint(expr= - m.x468 - 1.25*m.x636 + 1.25*m.x780 <= 0)

m.c172 = Constraint(expr= - m.x469 - 1.25*m.x637 + 1.25*m.x781 <= 0)

m.c173 = Constraint(expr= - m.x470 - 1.25*m.x638 + 1.25*m.x782 <= 0)

m.c174 = Constraint(expr= - m.x471 - 1.25*m.x639 + 1.25*m.x783 <= 0)

m.c175 = Constraint(expr= - m.x472 - 1.25*m.x640 + 1.25*m.x784 <= 0)

m.c176 = Constraint(expr= - m.x473 - 1.25*m.x641 + 1.25*m.x785 <= 0)

m.c177 = Constraint(expr= - m.x474 - 1.25*m.x642 + 1.25*m.x786 <= 0)

m.c178 = Constraint(expr= - m.x475 - 1.25*m.x643 + 1.25*m.x787 <= 0)

m.c179 = Constraint(expr= - m.x476 - 1.25*m.x644 + 1.25*m.x788 <= 0)

m.c180 = Constraint(expr= - m.x477 - 1.25*m.x645 + 1.25*m.x789 <= 0)

m.c181 = Constraint(expr= - m.x478 - 1.25*m.x646 + 1.25*m.x790 <= 0)

m.c182 = Constraint(expr= - m.x479 - 1.25*m.x647 + 1.25*m.x791 <= 0)

m.c183 = Constraint(expr= - m.x480 - 1.25*m.x648 + 1.25*m.x792 <= 0)

m.c184 = Constraint(expr= - m.x481 - 1.25*m.x649 + 1.25*m.x793 <= 0)

m.c185 = Constraint(expr= - m.x482 - 1.25*m.x650 + 1.25*m.x794 <= 0)

m.c186 = Constraint(expr= - m.x483 - 1.25*m.x651 + 1.25*m.x795 <= 0)

m.c187 = Constraint(expr= - m.x484 - 1.25*m.x652 + 1.25*m.x796 <= 0)

m.c188 = Constraint(expr= - m.x485 - 1.25*m.x653 + 1.25*m.x797 <= 0)

m.c189 = Constraint(expr= - m.x486 - 1.25*m.x654 + 1.25*m.x798 <= 0)

m.c190 = Constraint(expr= - m.x487 - 1.25*m.x655 + 1.25*m.x799 <= 0)

m.c191 = Constraint(expr= - m.x488 - 1.25*m.x656 + 1.25*m.x800 <= 0)

m.c192 = Constraint(expr= - m.x489 - 1.25*m.x657 + 1.25*m.x801 <= 0)

m.c193 = Constraint(expr= - m.x490 - 1.25*m.x658 + 1.25*m.x802 <= 0)

m.c194 = Constraint(expr= - m.x491 - 1.25*m.x659 + 1.25*m.x803 <= 0)

m.c195 = Constraint(expr= - m.x492 - 1.25*m.x660 + 1.25*m.x804 <= 0)

m.c196 = Constraint(expr= - m.x493 - 1.25*m.x661 + 1.25*m.x805 <= 0)

m.c197 = Constraint(expr= - m.x494 - 1.25*m.x662 + 1.25*m.x806 <= 0)

m.c198 = Constraint(expr= - m.x495 - 1.25*m.x663 + 1.25*m.x807 <= 0)

m.c199 = Constraint(expr= - m.x496 - 1.25*m.x664 + 1.25*m.x808 <= 0)

m.c200 = Constraint(expr= - m.x497 - 1.25*m.x665 + 1.25*m.x809 <= 0)

m.c201 = Constraint(expr= - m.x498 - 1.25*m.x666 + 1.25*m.x810 <= 0)

m.c202 = Constraint(expr= - m.x499 - 1.25*m.x667 + 1.25*m.x811 <= 0)

m.c203 = Constraint(expr= - m.x500 - 1.25*m.x668 + 1.25*m.x812 <= 0)

m.c204 = Constraint(expr= - m.x501 - 1.25*m.x669 + 1.25*m.x813 <= 0)

m.c205 = Constraint(expr= - m.x502 - 1.25*m.x670 + 1.25*m.x814 <= 0)

m.c206 = Constraint(expr= - m.x503 - 1.25*m.x671 + 1.25*m.x815 <= 0)

m.c207 = Constraint(expr= - m.x504 - 1.25*m.x672 + 1.25*m.x816 <= 0)

m.c208 = Constraint(expr= - m.x505 - 1.25*m.x673 + 1.25*m.x817 <= 0)

m.c209 = Constraint(expr= - m.x506 - 1.25*m.x674 + 1.25*m.x818 <= 0)

m.c210 = Constraint(expr= - m.x507 - 1.25*m.x675 + 1.25*m.x819 <= 0)

m.c211 = Constraint(expr= - m.x508 - 1.25*m.x676 + 1.25*m.x820 <= 0)

m.c212 = Constraint(expr= - m.x509 - 1.25*m.x677 + 1.25*m.x821 <= 0)

m.c213 = Constraint(expr= - m.x510 - 1.25*m.x678 + 1.25*m.x822 <= 0)

m.c214 = Constraint(expr= - m.x511 - 1.25*m.x679 + 1.25*m.x823 <= 0)

m.c215 = Constraint(expr= - m.x512 - 1.25*m.x680 + 1.25*m.x824 <= 0)

m.c216 = Constraint(expr= - m.x513 - 1.25*m.x681 + 1.25*m.x825 <= 0)

m.c217 = Constraint(expr= - m.x514 - 1.25*m.x682 + 1.25*m.x826 <= 0)

m.c218 = Constraint(expr= - m.x515 - 1.25*m.x683 + 1.25*m.x827 <= 0)

m.c219 = Constraint(expr= - m.x516 - 1.25*m.x684 + 1.25*m.x828 <= 0)

m.c220 = Constraint(expr= - m.x517 - 1.25*m.x685 + 1.25*m.x829 <= 0)

m.c221 = Constraint(expr= - m.x518 - 1.25*m.x686 + 1.25*m.x830 <= 0)

m.c222 = Constraint(expr= - m.x519 - 1.25*m.x687 + 1.25*m.x831 <= 0)

m.c223 = Constraint(expr= - m.x520 - 1.25*m.x688 + 1.25*m.x832 <= 0)

m.c224 = Constraint(expr= - m.x521 - 1.25*m.x689 + 1.25*m.x833 <= 0)

m.c225 = Constraint(expr= - m.x522 - 1.25*m.x690 + 1.25*m.x834 <= 0)

m.c226 = Constraint(expr= - m.x523 - 1.25*m.x691 + 1.25*m.x835 <= 0)

m.c227 = Constraint(expr= - m.x524 - 1.25*m.x692 + 1.25*m.x836 <= 0)

m.c228 = Constraint(expr= - m.x525 - 1.25*m.x693 + 1.25*m.x837 <= 0)

m.c229 = Constraint(expr= - m.x526 - 1.25*m.x694 + 1.25*m.x838 <= 0)

m.c230 = Constraint(expr= - m.x527 - 1.25*m.x695 + 1.25*m.x839 <= 0)

m.c231 = Constraint(expr= - m.x528 - 1.25*m.x696 + 1.25*m.x840 <= 0)

m.c232 = Constraint(expr= - m.x529 - 1.25*m.x697 + 1.25*m.x841 <= 0)

m.c233 = Constraint(expr= - m.x530 - 1.25*m.x698 + 1.25*m.x842 <= 0)

m.c234 = Constraint(expr= - m.x531 - 1.25*m.x699 + 1.25*m.x843 <= 0)

m.c235 = Constraint(expr= - m.x532 - 1.25*m.x700 + 1.25*m.x844 <= 0)

m.c236 = Constraint(expr= - m.x533 - 1.25*m.x701 + 1.25*m.x845 <= 0)

m.c237 = Constraint(expr= - m.x534 - 1.25*m.x702 + 1.25*m.x846 <= 0)

m.c238 = Constraint(expr= - m.x535 - 1.25*m.x703 + 1.25*m.x847 <= 0)

m.c239 = Constraint(expr= - m.x536 - 1.25*m.x704 + 1.25*m.x848 <= 0)

m.c240 = Constraint(expr= - m.x537 - 1.25*m.x705 + 1.25*m.x849 <= 0)

m.c241 = Constraint(expr= - m.x538 - 1.25*m.x706 + 1.25*m.x850 <= 0)

m.c242 = Constraint(expr= - m.x539 - 1.25*m.x707 + 1.25*m.x851 <= 0)

m.c243 = Constraint(expr= - m.x540 - 1.25*m.x708 + 1.25*m.x852 <= 0)

m.c244 = Constraint(expr= - m.x541 - 1.25*m.x709 + 1.25*m.x853 <= 0)

m.c245 = Constraint(expr= - m.x542 - 1.25*m.x710 + 1.25*m.x854 <= 0)

m.c246 = Constraint(expr= - m.x543 - 1.25*m.x711 + 1.25*m.x855 <= 0)

m.c247 = Constraint(expr= - m.x544 - 1.25*m.x712 + 1.25*m.x856 <= 0)

m.c248 = Constraint(expr= - m.x545 - 1.25*m.x713 + 1.25*m.x857 <= 0)

m.c249 = Constraint(expr= - m.x546 - 1.25*m.x714 + 1.25*m.x858 <= 0)

m.c250 = Constraint(expr= - m.x547 - 1.25*m.x715 + 1.25*m.x859 <= 0)

m.c251 = Constraint(expr= - m.x548 - 1.25*m.x716 + 1.25*m.x860 <= 0)

m.c252 = Constraint(expr= - m.x549 - 1.25*m.x717 + 1.25*m.x861 <= 0)

m.c253 = Constraint(expr=   m.x406 + 50*m.x574 - 50*m.x718 <= 0)

m.c254 = Constraint(expr=   m.x407 + 50*m.x575 - 50*m.x719 <= 0)

m.c255 = Constraint(expr=   m.x408 + 50*m.x576 - 50*m.x720 <= 0)

m.c256 = Constraint(expr=   m.x409 + 50*m.x577 - 50*m.x721 <= 0)

m.c257 = Constraint(expr=   m.x410 + 50*m.x578 - 50*m.x722 <= 0)

m.c258 = Constraint(expr=   m.x411 + 50*m.x579 - 50*m.x723 <= 0)

m.c259 = Constraint(expr=   m.x412 + 50*m.x580 - 50*m.x724 <= 0)

m.c260 = Constraint(expr=   m.x413 + 50*m.x581 - 50*m.x725 <= 0)

m.c261 = Constraint(expr=   m.x414 + 50*m.x582 - 50*m.x726 <= 0)

m.c262 = Constraint(expr=   m.x415 + 50*m.x583 - 50*m.x727 <= 0)

m.c263 = Constraint(expr=   m.x416 + 50*m.x584 - 50*m.x728 <= 0)

m.c264 = Constraint(expr=   m.x417 + 50*m.x585 - 50*m.x729 <= 0)

m.c265 = Constraint(expr=   m.x418 + 50*m.x586 - 50*m.x730 <= 0)

m.c266 = Constraint(expr=   m.x419 + 50*m.x587 - 50*m.x731 <= 0)

m.c267 = Constraint(expr=   m.x420 + 50*m.x588 - 50*m.x732 <= 0)

m.c268 = Constraint(expr=   m.x421 + 50*m.x589 - 50*m.x733 <= 0)

m.c269 = Constraint(expr=   m.x422 + 50*m.x590 - 50*m.x734 <= 0)

m.c270 = Constraint(expr=   m.x423 + 50*m.x591 - 50*m.x735 <= 0)

m.c271 = Constraint(expr=   m.x424 + 50*m.x592 - 50*m.x736 <= 0)

m.c272 = Constraint(expr=   m.x425 + 50*m.x593 - 50*m.x737 <= 0)

m.c273 = Constraint(expr=   m.x426 + 50*m.x594 - 50*m.x738 <= 0)

m.c274 = Constraint(expr=   m.x427 + 50*m.x595 - 50*m.x739 <= 0)

m.c275 = Constraint(expr=   m.x428 + 50*m.x596 - 50*m.x740 <= 0)

m.c276 = Constraint(expr=   m.x429 + 50*m.x597 - 50*m.x741 <= 0)

m.c277 = Constraint(expr=   m.x430 + 50*m.x598 - 50*m.x742 <= 0)

m.c278 = Constraint(expr=   m.x431 + 50*m.x599 - 50*m.x743 <= 0)

m.c279 = Constraint(expr=   m.x432 + 50*m.x600 - 50*m.x744 <= 0)

m.c280 = Constraint(expr=   m.x433 + 50*m.x601 - 50*m.x745 <= 0)

m.c281 = Constraint(expr=   m.x434 + 50*m.x602 - 50*m.x746 <= 0)

m.c282 = Constraint(expr=   m.x435 + 50*m.x603 - 50*m.x747 <= 0)

m.c283 = Constraint(expr=   m.x436 + 50*m.x604 - 50*m.x748 <= 0)

m.c284 = Constraint(expr=   m.x437 + 50*m.x605 - 50*m.x749 <= 0)

m.c285 = Constraint(expr=   m.x438 + 50*m.x606 - 50*m.x750 <= 0)

m.c286 = Constraint(expr=   m.x439 + 50*m.x607 - 50*m.x751 <= 0)

m.c287 = Constraint(expr=   m.x440 + 50*m.x608 - 50*m.x752 <= 0)

m.c288 = Constraint(expr=   m.x441 + 50*m.x609 - 50*m.x753 <= 0)

m.c289 = Constraint(expr=   m.x442 + 50*m.x610 - 50*m.x754 <= 0)

m.c290 = Constraint(expr=   m.x443 + 50*m.x611 - 50*m.x755 <= 0)

m.c291 = Constraint(expr=   m.x444 + 50*m.x612 - 50*m.x756 <= 0)

m.c292 = Constraint(expr=   m.x445 + 50*m.x613 - 50*m.x757 <= 0)

m.c293 = Constraint(expr=   m.x446 + 50*m.x614 - 50*m.x758 <= 0)

m.c294 = Constraint(expr=   m.x447 + 50*m.x615 - 50*m.x759 <= 0)

m.c295 = Constraint(expr=   m.x448 + 50*m.x616 - 50*m.x760 <= 0)

m.c296 = Constraint(expr=   m.x449 + 50*m.x617 - 50*m.x761 <= 0)

m.c297 = Constraint(expr=   m.x450 + 50*m.x618 - 50*m.x762 <= 0)

m.c298 = Constraint(expr=   m.x451 + 50*m.x619 - 50*m.x763 <= 0)

m.c299 = Constraint(expr=   m.x452 + 50*m.x620 - 50*m.x764 <= 0)

m.c300 = Constraint(expr=   m.x453 + 50*m.x621 - 50*m.x765 <= 0)

m.c301 = Constraint(expr=   m.x454 + 50*m.x622 - 50*m.x766 <= 0)

m.c302 = Constraint(expr=   m.x455 + 50*m.x623 - 50*m.x767 <= 0)

m.c303 = Constraint(expr=   m.x456 + 50*m.x624 - 50*m.x768 <= 0)

m.c304 = Constraint(expr=   m.x457 + 50*m.x625 - 50*m.x769 <= 0)

m.c305 = Constraint(expr=   m.x458 + 50*m.x626 - 50*m.x770 <= 0)

m.c306 = Constraint(expr=   m.x459 + 50*m.x627 - 50*m.x771 <= 0)

m.c307 = Constraint(expr=   m.x460 + 50*m.x628 - 50*m.x772 <= 0)

m.c308 = Constraint(expr=   m.x461 + 50*m.x629 - 50*m.x773 <= 0)

m.c309 = Constraint(expr=   m.x462 + 50*m.x630 - 50*m.x774 <= 0)

m.c310 = Constraint(expr=   m.x463 + 50*m.x631 - 50*m.x775 <= 0)

m.c311 = Constraint(expr=   m.x464 + 50*m.x632 - 50*m.x776 <= 0)

m.c312 = Constraint(expr=   m.x465 + 50*m.x633 - 50*m.x777 <= 0)

m.c313 = Constraint(expr=   m.x466 + 50*m.x634 - 50*m.x778 <= 0)

m.c314 = Constraint(expr=   m.x467 + 50*m.x635 - 50*m.x779 <= 0)

m.c315 = Constraint(expr=   m.x468 + 50*m.x636 - 50*m.x780 <= 0)

m.c316 = Constraint(expr=   m.x469 + 50*m.x637 - 50*m.x781 <= 0)

m.c317 = Constraint(expr=   m.x470 + 50*m.x638 - 50*m.x782 <= 0)

m.c318 = Constraint(expr=   m.x471 + 50*m.x639 - 50*m.x783 <= 0)

m.c319 = Constraint(expr=   m.x472 + 50*m.x640 - 50*m.x784 <= 0)

m.c320 = Constraint(expr=   m.x473 + 50*m.x641 - 50*m.x785 <= 0)

m.c321 = Constraint(expr=   m.x474 + 50*m.x642 - 50*m.x786 <= 0)

m.c322 = Constraint(expr=   m.x475 + 50*m.x643 - 50*m.x787 <= 0)

m.c323 = Constraint(expr=   m.x476 + 50*m.x644 - 50*m.x788 <= 0)

m.c324 = Constraint(expr=   m.x477 + 50*m.x645 - 50*m.x789 <= 0)

m.c325 = Constraint(expr=   m.x478 + 50*m.x646 - 50*m.x790 <= 0)

m.c326 = Constraint(expr=   m.x479 + 50*m.x647 - 50*m.x791 <= 0)

m.c327 = Constraint(expr=   m.x480 + 50*m.x648 - 50*m.x792 <= 0)

m.c328 = Constraint(expr=   m.x481 + 50*m.x649 - 50*m.x793 <= 0)

m.c329 = Constraint(expr=   m.x482 + 50*m.x650 - 50*m.x794 <= 0)

m.c330 = Constraint(expr=   m.x483 + 50*m.x651 - 50*m.x795 <= 0)

m.c331 = Constraint(expr=   m.x484 + 50*m.x652 - 50*m.x796 <= 0)

m.c332 = Constraint(expr=   m.x485 + 50*m.x653 - 50*m.x797 <= 0)

m.c333 = Constraint(expr=   m.x486 + 50*m.x654 - 50*m.x798 <= 0)

m.c334 = Constraint(expr=   m.x487 + 50*m.x655 - 50*m.x799 <= 0)

m.c335 = Constraint(expr=   m.x488 + 50*m.x656 - 50*m.x800 <= 0)

m.c336 = Constraint(expr=   m.x489 + 50*m.x657 - 50*m.x801 <= 0)

m.c337 = Constraint(expr=   m.x490 + 50*m.x658 - 50*m.x802 <= 0)

m.c338 = Constraint(expr=   m.x491 + 50*m.x659 - 50*m.x803 <= 0)

m.c339 = Constraint(expr=   m.x492 + 50*m.x660 - 50*m.x804 <= 0)

m.c340 = Constraint(expr=   m.x493 + 50*m.x661 - 50*m.x805 <= 0)

m.c341 = Constraint(expr=   m.x494 + 50*m.x662 - 50*m.x806 <= 0)

m.c342 = Constraint(expr=   m.x495 + 50*m.x663 - 50*m.x807 <= 0)

m.c343 = Constraint(expr=   m.x496 + 50*m.x664 - 50*m.x808 <= 0)

m.c344 = Constraint(expr=   m.x497 + 50*m.x665 - 50*m.x809 <= 0)

m.c345 = Constraint(expr=   m.x498 + 50*m.x666 - 50*m.x810 <= 0)

m.c346 = Constraint(expr=   m.x499 + 50*m.x667 - 50*m.x811 <= 0)

m.c347 = Constraint(expr=   m.x500 + 50*m.x668 - 50*m.x812 <= 0)

m.c348 = Constraint(expr=   m.x501 + 50*m.x669 - 50*m.x813 <= 0)

m.c349 = Constraint(expr=   m.x502 + 50*m.x670 - 50*m.x814 <= 0)

m.c350 = Constraint(expr=   m.x503 + 50*m.x671 - 50*m.x815 <= 0)

m.c351 = Constraint(expr=   m.x504 + 50*m.x672 - 50*m.x816 <= 0)

m.c352 = Constraint(expr=   m.x505 + 50*m.x673 - 50*m.x817 <= 0)

m.c353 = Constraint(expr=   m.x506 + 50*m.x674 - 50*m.x818 <= 0)

m.c354 = Constraint(expr=   m.x507 + 50*m.x675 - 50*m.x819 <= 0)

m.c355 = Constraint(expr=   m.x508 + 50*m.x676 - 50*m.x820 <= 0)

m.c356 = Constraint(expr=   m.x509 + 50*m.x677 - 50*m.x821 <= 0)

m.c357 = Constraint(expr=   m.x510 + 50*m.x678 - 50*m.x822 <= 0)

m.c358 = Constraint(expr=   m.x511 + 50*m.x679 - 50*m.x823 <= 0)

m.c359 = Constraint(expr=   m.x512 + 50*m.x680 - 50*m.x824 <= 0)

m.c360 = Constraint(expr=   m.x513 + 50*m.x681 - 50*m.x825 <= 0)

m.c361 = Constraint(expr=   m.x514 + 50*m.x682 - 50*m.x826 <= 0)

m.c362 = Constraint(expr=   m.x515 + 50*m.x683 - 50*m.x827 <= 0)

m.c363 = Constraint(expr=   m.x516 + 50*m.x684 - 50*m.x828 <= 0)

m.c364 = Constraint(expr=   m.x517 + 50*m.x685 - 50*m.x829 <= 0)

m.c365 = Constraint(expr=   m.x518 + 50*m.x686 - 50*m.x830 <= 0)

m.c366 = Constraint(expr=   m.x519 + 50*m.x687 - 50*m.x831 <= 0)

m.c367 = Constraint(expr=   m.x520 + 50*m.x688 - 50*m.x832 <= 0)

m.c368 = Constraint(expr=   m.x521 + 50*m.x689 - 50*m.x833 <= 0)

m.c369 = Constraint(expr=   m.x522 + 50*m.x690 - 50*m.x834 <= 0)

m.c370 = Constraint(expr=   m.x523 + 50*m.x691 - 50*m.x835 <= 0)

m.c371 = Constraint(expr=   m.x524 + 50*m.x692 - 50*m.x836 <= 0)

m.c372 = Constraint(expr=   m.x525 + 50*m.x693 - 50*m.x837 <= 0)

m.c373 = Constraint(expr=   m.x526 + 50*m.x694 - 50*m.x838 <= 0)

m.c374 = Constraint(expr=   m.x527 + 50*m.x695 - 50*m.x839 <= 0)

m.c375 = Constraint(expr=   m.x528 + 50*m.x696 - 50*m.x840 <= 0)

m.c376 = Constraint(expr=   m.x529 + 50*m.x697 - 50*m.x841 <= 0)

m.c377 = Constraint(expr=   m.x530 + 50*m.x698 - 50*m.x842 <= 0)

m.c378 = Constraint(expr=   m.x531 + 50*m.x699 - 50*m.x843 <= 0)

m.c379 = Constraint(expr=   m.x532 + 50*m.x700 - 50*m.x844 <= 0)

m.c380 = Constraint(expr=   m.x533 + 50*m.x701 - 50*m.x845 <= 0)

m.c381 = Constraint(expr=   m.x534 + 50*m.x702 - 50*m.x846 <= 0)

m.c382 = Constraint(expr=   m.x535 + 50*m.x703 - 50*m.x847 <= 0)

m.c383 = Constraint(expr=   m.x536 + 50*m.x704 - 50*m.x848 <= 0)

m.c384 = Constraint(expr=   m.x537 + 50*m.x705 - 50*m.x849 <= 0)

m.c385 = Constraint(expr=   m.x538 + 50*m.x706 - 50*m.x850 <= 0)

m.c386 = Constraint(expr=   m.x539 + 50*m.x707 - 50*m.x851 <= 0)

m.c387 = Constraint(expr=   m.x540 + 50*m.x708 - 50*m.x852 <= 0)

m.c388 = Constraint(expr=   m.x541 + 50*m.x709 - 50*m.x853 <= 0)

m.c389 = Constraint(expr=   m.x542 + 50*m.x710 - 50*m.x854 <= 0)

m.c390 = Constraint(expr=   m.x543 + 50*m.x711 - 50*m.x855 <= 0)

m.c391 = Constraint(expr=   m.x544 + 50*m.x712 - 50*m.x856 <= 0)

m.c392 = Constraint(expr=   m.x545 + 50*m.x713 - 50*m.x857 <= 0)

m.c393 = Constraint(expr=   m.x546 + 50*m.x714 - 50*m.x858 <= 0)

m.c394 = Constraint(expr=   m.x547 + 50*m.x715 - 50*m.x859 <= 0)

m.c395 = Constraint(expr=   m.x548 + 50*m.x716 - 50*m.x860 <= 0)

m.c396 = Constraint(expr=   m.x549 + 50*m.x717 - 50*m.x861 <= 0)

m.c397 = Constraint(expr= - 10*m.b1 + m.x406 <= 0)

m.c398 = Constraint(expr= - 10*m.b2 + m.x407 <= 0)

m.c399 = Constraint(expr=   m.x408 <= 0)

m.c400 = Constraint(expr= - 10*m.b4 + m.x409 <= 0)

m.c401 = Constraint(expr= - 10*m.b5 + m.x410 <= 0)

m.c402 = Constraint(expr=   m.x411 <= 0)

m.c403 = Constraint(expr= - 10*m.b7 + m.x412 <= 0)

m.c404 = Constraint(expr= - 10*m.b8 + m.x413 <= 0)

m.c405 = Constraint(expr=   m.x414 <= 0)

m.c406 = Constraint(expr= - 10*m.b10 + m.x415 <= 0)

m.c407 = Constraint(expr= - 10*m.b11 + m.x416 <= 0)

m.c408 = Constraint(expr=   m.x417 <= 0)

m.c409 = Constraint(expr= - 350*m.b13 + m.x418 <= 0)

m.c410 = Constraint(expr= - 350*m.b14 + m.x419 <= 0)

m.c411 = Constraint(expr=   m.x420 <= 0)

m.c412 = Constraint(expr= - 350*m.b16 + m.x421 <= 0)

m.c413 = Constraint(expr= - 350*m.b17 + m.x422 <= 0)

m.c414 = Constraint(expr=   m.x423 <= 0)

m.c415 = Constraint(expr= - 350*m.b19 + m.x424 <= 0)

m.c416 = Constraint(expr= - 350*m.b20 + m.x425 <= 0)

m.c417 = Constraint(expr=   m.x426 <= 0)

m.c418 = Constraint(expr= - 350*m.b22 + m.x427 <= 0)

m.c419 = Constraint(expr= - 350*m.b23 + m.x428 <= 0)

m.c420 = Constraint(expr=   m.x429 <= 0)

m.c421 = Constraint(expr= - 200*m.b25 + m.x430 <= 0)

m.c422 = Constraint(expr= - 200*m.b26 + m.x431 <= 0)

m.c423 = Constraint(expr=   m.x432 <= 0)

m.c424 = Constraint(expr= - 200*m.b28 + m.x433 <= 0)

m.c425 = Constraint(expr= - 200*m.b29 + m.x434 <= 0)

m.c426 = Constraint(expr=   m.x435 <= 0)

m.c427 = Constraint(expr= - 200*m.b31 + m.x436 <= 0)

m.c428 = Constraint(expr= - 200*m.b32 + m.x437 <= 0)

m.c429 = Constraint(expr=   m.x438 <= 0)

m.c430 = Constraint(expr= - 200*m.b34 + m.x439 <= 0)

m.c431 = Constraint(expr= - 200*m.b35 + m.x440 <= 0)

m.c432 = Constraint(expr=   m.x441 <= 0)

m.c433 = Constraint(expr= - 300*m.b37 + m.x442 <= 0)

m.c434 = Constraint(expr= - 300*m.b38 + m.x443 <= 0)

m.c435 = Constraint(expr=   m.x444 <= 0)

m.c436 = Constraint(expr= - 300*m.b40 + m.x445 <= 0)

m.c437 = Constraint(expr= - 300*m.b41 + m.x446 <= 0)

m.c438 = Constraint(expr=   m.x447 <= 0)

m.c439 = Constraint(expr= - 300*m.b43 + m.x448 <= 0)

m.c440 = Constraint(expr= - 300*m.b44 + m.x449 <= 0)

m.c441 = Constraint(expr=   m.x450 <= 0)

m.c442 = Constraint(expr= - 300*m.b46 + m.x451 <= 0)

m.c443 = Constraint(expr= - 300*m.b47 + m.x452 <= 0)

m.c444 = Constraint(expr=   m.x453 <= 0)

m.c445 = Constraint(expr=   m.x454 <= 0)

m.c446 = Constraint(expr= - 10*m.b50 + m.x455 <= 0)

m.c447 = Constraint(expr= - 10*m.b51 + m.x456 <= 0)

m.c448 = Constraint(expr=   m.x457 <= 0)

m.c449 = Constraint(expr= - 10*m.b53 + m.x458 <= 0)

m.c450 = Constraint(expr= - 10*m.b54 + m.x459 <= 0)

m.c451 = Constraint(expr=   m.x460 <= 0)

m.c452 = Constraint(expr= - 10*m.b56 + m.x461 <= 0)

m.c453 = Constraint(expr= - 10*m.b57 + m.x462 <= 0)

m.c454 = Constraint(expr=   m.x463 <= 0)

m.c455 = Constraint(expr= - 10*m.b59 + m.x464 <= 0)

m.c456 = Constraint(expr= - 10*m.b60 + m.x465 <= 0)

m.c457 = Constraint(expr=   m.x466 <= 0)

m.c458 = Constraint(expr= - 200*m.b62 + m.x467 <= 0)

m.c459 = Constraint(expr= - 200*m.b63 + m.x468 <= 0)

m.c460 = Constraint(expr=   m.x469 <= 0)

m.c461 = Constraint(expr= - 200*m.b65 + m.x470 <= 0)

m.c462 = Constraint(expr= - 200*m.b66 + m.x471 <= 0)

m.c463 = Constraint(expr=   m.x472 <= 0)

m.c464 = Constraint(expr= - 200*m.b68 + m.x473 <= 0)

m.c465 = Constraint(expr= - 200*m.b69 + m.x474 <= 0)

m.c466 = Constraint(expr=   m.x475 <= 0)

m.c467 = Constraint(expr= - 200*m.b71 + m.x476 <= 0)

m.c468 = Constraint(expr= - 200*m.b72 + m.x477 <= 0)

m.c469 = Constraint(expr=   m.x478 <= 0)

m.c470 = Constraint(expr= - 250*m.b74 + m.x479 <= 0)

m.c471 = Constraint(expr= - 250*m.b75 + m.x480 <= 0)

m.c472 = Constraint(expr=   m.x481 <= 0)

m.c473 = Constraint(expr= - 250*m.b77 + m.x482 <= 0)

m.c474 = Constraint(expr= - 250*m.b78 + m.x483 <= 0)

m.c475 = Constraint(expr=   m.x484 <= 0)

m.c476 = Constraint(expr= - 250*m.b80 + m.x485 <= 0)

m.c477 = Constraint(expr= - 250*m.b81 + m.x486 <= 0)

m.c478 = Constraint(expr=   m.x487 <= 0)

m.c479 = Constraint(expr= - 250*m.b83 + m.x488 <= 0)

m.c480 = Constraint(expr= - 250*m.b84 + m.x489 <= 0)

m.c481 = Constraint(expr=   m.x490 <= 0)

m.c482 = Constraint(expr= - 240*m.b86 + m.x491 <= 0)

m.c483 = Constraint(expr= - 240*m.b87 + m.x492 <= 0)

m.c484 = Constraint(expr=   m.x493 <= 0)

m.c485 = Constraint(expr= - 240*m.b89 + m.x494 <= 0)

m.c486 = Constraint(expr= - 240*m.b90 + m.x495 <= 0)

m.c487 = Constraint(expr=   m.x496 <= 0)

m.c488 = Constraint(expr= - 240*m.b92 + m.x497 <= 0)

m.c489 = Constraint(expr= - 240*m.b93 + m.x498 <= 0)

m.c490 = Constraint(expr=   m.x499 <= 0)

m.c491 = Constraint(expr= - 240*m.b95 + m.x500 <= 0)

m.c492 = Constraint(expr= - 240*m.b96 + m.x501 <= 0)

m.c493 = Constraint(expr=   m.x502 <= 0)

m.c494 = Constraint(expr= - 10*m.b98 + m.x503 <= 0)

m.c495 = Constraint(expr= - 10*m.b99 + m.x504 <= 0)

m.c496 = Constraint(expr=   m.x505 <= 0)

m.c497 = Constraint(expr= - 10*m.b101 + m.x506 <= 0)

m.c498 = Constraint(expr= - 10*m.b102 + m.x507 <= 0)

m.c499 = Constraint(expr=   m.x508 <= 0)

m.c500 = Constraint(expr= - 10*m.b104 + m.x509 <= 0)

m.c501 = Constraint(expr= - 10*m.b105 + m.x510 <= 0)

m.c502 = Constraint(expr=   m.x511 <= 0)

m.c503 = Constraint(expr= - 10*m.b107 + m.x512 <= 0)

m.c504 = Constraint(expr= - 10*m.b108 + m.x513 <= 0)

m.c505 = Constraint(expr=   m.x514 <= 0)

m.c506 = Constraint(expr= - 250*m.b110 + m.x515 <= 0)

m.c507 = Constraint(expr= - 250*m.b111 + m.x516 <= 0)

m.c508 = Constraint(expr=   m.x517 <= 0)

m.c509 = Constraint(expr= - 250*m.b113 + m.x518 <= 0)

m.c510 = Constraint(expr= - 250*m.b114 + m.x519 <= 0)

m.c511 = Constraint(expr=   m.x520 <= 0)

m.c512 = Constraint(expr= - 250*m.b116 + m.x521 <= 0)

m.c513 = Constraint(expr= - 250*m.b117 + m.x522 <= 0)

m.c514 = Constraint(expr=   m.x523 <= 0)

m.c515 = Constraint(expr= - 250*m.b119 + m.x524 <= 0)

m.c516 = Constraint(expr= - 250*m.b120 + m.x525 <= 0)

m.c517 = Constraint(expr=   m.x526 <= 0)

m.c518 = Constraint(expr= - 250*m.b122 + m.x527 <= 0)

m.c519 = Constraint(expr= - 250*m.b123 + m.x528 <= 0)

m.c520 = Constraint(expr=   m.x529 <= 0)

m.c521 = Constraint(expr= - 250*m.b125 + m.x530 <= 0)

m.c522 = Constraint(expr= - 250*m.b126 + m.x531 <= 0)

m.c523 = Constraint(expr=   m.x532 <= 0)

m.c524 = Constraint(expr= - 250*m.b128 + m.x533 <= 0)

m.c525 = Constraint(expr= - 250*m.b129 + m.x534 <= 0)

m.c526 = Constraint(expr=   m.x535 <= 0)

m.c527 = Constraint(expr= - 250*m.b131 + m.x536 <= 0)

m.c528 = Constraint(expr= - 250*m.b132 + m.x537 <= 0)

m.c529 = Constraint(expr=   m.x538 <= 0)

m.c530 = Constraint(expr= - 190*m.b134 + m.x539 <= 0)

m.c531 = Constraint(expr= - 190*m.b135 + m.x540 <= 0)

m.c532 = Constraint(expr=   m.x541 <= 0)

m.c533 = Constraint(expr= - 190*m.b137 + m.x542 <= 0)

m.c534 = Constraint(expr= - 190*m.b138 + m.x543 <= 0)

m.c535 = Constraint(expr=   m.x544 <= 0)

m.c536 = Constraint(expr= - 190*m.b140 + m.x545 <= 0)

m.c537 = Constraint(expr= - 190*m.b141 + m.x546 <= 0)

m.c538 = Constraint(expr=   m.x547 <= 0)

m.c539 = Constraint(expr= - 190*m.b143 + m.x548 <= 0)

m.c540 = Constraint(expr= - 190*m.b144 + m.x549 <= 0)

m.c541 = Constraint(expr=   m.x406 + m.x407 + m.x408 + m.x409 + m.x410 + m.x411 + m.x412 + m.x413 + m.x414 + m.x415
                          + m.x416 + m.x417 == 10)

m.c542 = Constraint(expr=   m.x418 + m.x419 + m.x420 + m.x421 + m.x422 + m.x423 + m.x424 + m.x425 + m.x426 + m.x427
                          + m.x428 + m.x429 == 350)

m.c543 = Constraint(expr=   m.x430 + m.x431 + m.x432 + m.x433 + m.x434 + m.x435 + m.x436 + m.x437 + m.x438 + m.x439
                          + m.x440 + m.x441 == 200)

m.c544 = Constraint(expr=   m.x442 + m.x443 + m.x444 + m.x445 + m.x446 + m.x447 + m.x448 + m.x449 + m.x450 + m.x451
                          + m.x452 + m.x453 == 300)

m.c545 = Constraint(expr=   m.x454 + m.x455 + m.x456 + m.x457 + m.x458 + m.x459 + m.x460 + m.x461 + m.x462 + m.x463
                          + m.x464 + m.x465 == 10)

m.c546 = Constraint(expr=   m.x466 + m.x467 + m.x468 + m.x469 + m.x470 + m.x471 + m.x472 + m.x473 + m.x474 + m.x475
                          + m.x476 + m.x477 == 200)

m.c547 = Constraint(expr=   m.x478 + m.x479 + m.x480 + m.x481 + m.x482 + m.x483 + m.x484 + m.x485 + m.x486 + m.x487
                          + m.x488 + m.x489 == 250)

m.c548 = Constraint(expr=   m.x490 + m.x491 + m.x492 + m.x493 + m.x494 + m.x495 + m.x496 + m.x497 + m.x498 + m.x499
                          + m.x500 + m.x501 == 240)

m.c549 = Constraint(expr=   m.x502 + m.x503 + m.x504 + m.x505 + m.x506 + m.x507 + m.x508 + m.x509 + m.x510 + m.x511
                          + m.x512 + m.x513 == 10)

m.c550 = Constraint(expr=   m.x514 + m.x515 + m.x516 + m.x517 + m.x518 + m.x519 + m.x520 + m.x521 + m.x522 + m.x523
                          + m.x524 + m.x525 == 250)

m.c551 = Constraint(expr=   m.x526 + m.x527 + m.x528 + m.x529 + m.x530 + m.x531 + m.x532 + m.x533 + m.x534 + m.x535
                          + m.x536 + m.x537 == 250)

m.c552 = Constraint(expr=   m.x538 + m.x539 + m.x540 + m.x541 + m.x542 + m.x543 + m.x544 + m.x545 + m.x546 + m.x547
                          + m.x548 + m.x549 == 190)

m.c553 = Constraint(expr=   336*m.b1 + m.x550 - m.x574 <= 336)

m.c554 = Constraint(expr=   336*m.b2 + m.x550 - m.x575 <= 336)

m.c555 = Constraint(expr=   336*m.b3 + m.x550 - m.x576 <= 336)

m.c556 = Constraint(expr=   336*m.b4 + m.x550 - m.x577 <= 336)

m.c557 = Constraint(expr=   336*m.b5 + m.x550 - m.x578 <= 336)

m.c558 = Constraint(expr=   336*m.b6 + m.x550 - m.x579 <= 336)

m.c559 = Constraint(expr=   336*m.b7 + m.x550 - m.x580 <= 336)

m.c560 = Constraint(expr=   336*m.b8 + m.x550 - m.x581 <= 336)

m.c561 = Constraint(expr=   336*m.b9 + m.x550 - m.x582 <= 336)

m.c562 = Constraint(expr=   336*m.b10 + m.x550 - m.x583 <= 336)

m.c563 = Constraint(expr=   336*m.b11 + m.x550 - m.x584 <= 336)

m.c564 = Constraint(expr=   336*m.b12 + m.x550 - m.x585 <= 336)

m.c565 = Constraint(expr=   336*m.b13 + m.x551 - m.x586 <= 336)

m.c566 = Constraint(expr=   336*m.b14 + m.x551 - m.x587 <= 336)

m.c567 = Constraint(expr=   336*m.b15 + m.x551 - m.x588 <= 336)

m.c568 = Constraint(expr=   336*m.b16 + m.x551 - m.x589 <= 336)

m.c569 = Constraint(expr=   336*m.b17 + m.x551 - m.x590 <= 336)

m.c570 = Constraint(expr=   336*m.b18 + m.x551 - m.x591 <= 336)

m.c571 = Constraint(expr=   336*m.b19 + m.x551 - m.x592 <= 336)

m.c572 = Constraint(expr=   336*m.b20 + m.x551 - m.x593 <= 336)

m.c573 = Constraint(expr=   336*m.b21 + m.x551 - m.x594 <= 336)

m.c574 = Constraint(expr=   336*m.b22 + m.x551 - m.x595 <= 336)

m.c575 = Constraint(expr=   336*m.b23 + m.x551 - m.x596 <= 336)

m.c576 = Constraint(expr=   336*m.b24 + m.x551 - m.x597 <= 336)

m.c577 = Constraint(expr=   336*m.b25 + m.x552 - m.x598 <= 336)

m.c578 = Constraint(expr=   336*m.b26 + m.x552 - m.x599 <= 336)

m.c579 = Constraint(expr=   336*m.b27 + m.x552 - m.x600 <= 336)

m.c580 = Constraint(expr=   336*m.b28 + m.x552 - m.x601 <= 336)

m.c581 = Constraint(expr=   336*m.b29 + m.x552 - m.x602 <= 336)

m.c582 = Constraint(expr=   336*m.b30 + m.x552 - m.x603 <= 336)

m.c583 = Constraint(expr=   336*m.b31 + m.x552 - m.x604 <= 336)

m.c584 = Constraint(expr=   336*m.b32 + m.x552 - m.x605 <= 336)

m.c585 = Constraint(expr=   336*m.b33 + m.x552 - m.x606 <= 336)

m.c586 = Constraint(expr=   336*m.b34 + m.x552 - m.x607 <= 336)

m.c587 = Constraint(expr=   336*m.b35 + m.x552 - m.x608 <= 336)

m.c588 = Constraint(expr=   336*m.b36 + m.x552 - m.x609 <= 336)

m.c589 = Constraint(expr=   336*m.b37 + m.x553 - m.x610 <= 336)

m.c590 = Constraint(expr=   336*m.b38 + m.x553 - m.x611 <= 336)

m.c591 = Constraint(expr=   336*m.b39 + m.x553 - m.x612 <= 336)

m.c592 = Constraint(expr=   336*m.b40 + m.x553 - m.x613 <= 336)

m.c593 = Constraint(expr=   336*m.b41 + m.x553 - m.x614 <= 336)

m.c594 = Constraint(expr=   336*m.b42 + m.x553 - m.x615 <= 336)

m.c595 = Constraint(expr=   336*m.b43 + m.x553 - m.x616 <= 336)

m.c596 = Constraint(expr=   336*m.b44 + m.x553 - m.x617 <= 336)

m.c597 = Constraint(expr=   336*m.b45 + m.x553 - m.x618 <= 336)

m.c598 = Constraint(expr=   336*m.b46 + m.x553 - m.x619 <= 336)

m.c599 = Constraint(expr=   336*m.b47 + m.x553 - m.x620 <= 336)

m.c600 = Constraint(expr=   336*m.b48 + m.x553 - m.x621 <= 336)

m.c601 = Constraint(expr=   336*m.b49 + m.x554 - m.x622 <= 336)

m.c602 = Constraint(expr=   336*m.b50 + m.x554 - m.x623 <= 336)

m.c603 = Constraint(expr=   336*m.b51 + m.x554 - m.x624 <= 336)

m.c604 = Constraint(expr=   336*m.b52 + m.x554 - m.x625 <= 336)

m.c605 = Constraint(expr=   336*m.b53 + m.x554 - m.x626 <= 336)

m.c606 = Constraint(expr=   336*m.b54 + m.x554 - m.x627 <= 336)

m.c607 = Constraint(expr=   336*m.b55 + m.x554 - m.x628 <= 336)

m.c608 = Constraint(expr=   336*m.b56 + m.x554 - m.x629 <= 336)

m.c609 = Constraint(expr=   336*m.b57 + m.x554 - m.x630 <= 336)

m.c610 = Constraint(expr=   336*m.b58 + m.x554 - m.x631 <= 336)

m.c611 = Constraint(expr=   336*m.b59 + m.x554 - m.x632 <= 336)

m.c612 = Constraint(expr=   336*m.b60 + m.x554 - m.x633 <= 336)

m.c613 = Constraint(expr=   336*m.b61 + m.x555 - m.x634 <= 336)

m.c614 = Constraint(expr=   336*m.b62 + m.x555 - m.x635 <= 336)

m.c615 = Constraint(expr=   336*m.b63 + m.x555 - m.x636 <= 336)

m.c616 = Constraint(expr=   336*m.b64 + m.x555 - m.x637 <= 336)

m.c617 = Constraint(expr=   336*m.b65 + m.x555 - m.x638 <= 336)

m.c618 = Constraint(expr=   336*m.b66 + m.x555 - m.x639 <= 336)

m.c619 = Constraint(expr=   336*m.b67 + m.x555 - m.x640 <= 336)

m.c620 = Constraint(expr=   336*m.b68 + m.x555 - m.x641 <= 336)

m.c621 = Constraint(expr=   336*m.b69 + m.x555 - m.x642 <= 336)

m.c622 = Constraint(expr=   336*m.b70 + m.x555 - m.x643 <= 336)

m.c623 = Constraint(expr=   336*m.b71 + m.x555 - m.x644 <= 336)

m.c624 = Constraint(expr=   336*m.b72 + m.x555 - m.x645 <= 336)

m.c625 = Constraint(expr=   336*m.b73 + m.x556 - m.x646 <= 336)

m.c626 = Constraint(expr=   336*m.b74 + m.x556 - m.x647 <= 336)

m.c627 = Constraint(expr=   336*m.b75 + m.x556 - m.x648 <= 336)

m.c628 = Constraint(expr=   336*m.b76 + m.x556 - m.x649 <= 336)

m.c629 = Constraint(expr=   336*m.b77 + m.x556 - m.x650 <= 336)

m.c630 = Constraint(expr=   336*m.b78 + m.x556 - m.x651 <= 336)

m.c631 = Constraint(expr=   336*m.b79 + m.x556 - m.x652 <= 336)

m.c632 = Constraint(expr=   336*m.b80 + m.x556 - m.x653 <= 336)

m.c633 = Constraint(expr=   336*m.b81 + m.x556 - m.x654 <= 336)

m.c634 = Constraint(expr=   336*m.b82 + m.x556 - m.x655 <= 336)

m.c635 = Constraint(expr=   336*m.b83 + m.x556 - m.x656 <= 336)

m.c636 = Constraint(expr=   336*m.b84 + m.x556 - m.x657 <= 336)

m.c637 = Constraint(expr=   336*m.b85 + m.x557 - m.x658 <= 336)

m.c638 = Constraint(expr=   336*m.b86 + m.x557 - m.x659 <= 336)

m.c639 = Constraint(expr=   336*m.b87 + m.x557 - m.x660 <= 336)

m.c640 = Constraint(expr=   336*m.b88 + m.x557 - m.x661 <= 336)

m.c641 = Constraint(expr=   336*m.b89 + m.x557 - m.x662 <= 336)

m.c642 = Constraint(expr=   336*m.b90 + m.x557 - m.x663 <= 336)

m.c643 = Constraint(expr=   336*m.b91 + m.x557 - m.x664 <= 336)

m.c644 = Constraint(expr=   336*m.b92 + m.x557 - m.x665 <= 336)

m.c645 = Constraint(expr=   336*m.b93 + m.x557 - m.x666 <= 336)

m.c646 = Constraint(expr=   336*m.b94 + m.x557 - m.x667 <= 336)

m.c647 = Constraint(expr=   336*m.b95 + m.x557 - m.x668 <= 336)

m.c648 = Constraint(expr=   336*m.b96 + m.x557 - m.x669 <= 336)

m.c649 = Constraint(expr=   336*m.b97 + m.x558 - m.x670 <= 336)

m.c650 = Constraint(expr=   336*m.b98 + m.x558 - m.x671 <= 336)

m.c651 = Constraint(expr=   336*m.b99 + m.x558 - m.x672 <= 336)

m.c652 = Constraint(expr=   336*m.b100 + m.x558 - m.x673 <= 336)

m.c653 = Constraint(expr=   336*m.b101 + m.x558 - m.x674 <= 336)

m.c654 = Constraint(expr=   336*m.b102 + m.x558 - m.x675 <= 336)

m.c655 = Constraint(expr=   336*m.b103 + m.x558 - m.x676 <= 336)

m.c656 = Constraint(expr=   336*m.b104 + m.x558 - m.x677 <= 336)

m.c657 = Constraint(expr=   336*m.b105 + m.x558 - m.x678 <= 336)

m.c658 = Constraint(expr=   336*m.b106 + m.x558 - m.x679 <= 336)

m.c659 = Constraint(expr=   336*m.b107 + m.x558 - m.x680 <= 336)

m.c660 = Constraint(expr=   336*m.b108 + m.x558 - m.x681 <= 336)

m.c661 = Constraint(expr=   336*m.b109 + m.x559 - m.x682 <= 336)

m.c662 = Constraint(expr=   336*m.b110 + m.x559 - m.x683 <= 336)

m.c663 = Constraint(expr=   336*m.b111 + m.x559 - m.x684 <= 336)

m.c664 = Constraint(expr=   336*m.b112 + m.x559 - m.x685 <= 336)

m.c665 = Constraint(expr=   336*m.b113 + m.x559 - m.x686 <= 336)

m.c666 = Constraint(expr=   336*m.b114 + m.x559 - m.x687 <= 336)

m.c667 = Constraint(expr=   336*m.b115 + m.x559 - m.x688 <= 336)

m.c668 = Constraint(expr=   336*m.b116 + m.x559 - m.x689 <= 336)

m.c669 = Constraint(expr=   336*m.b117 + m.x559 - m.x690 <= 336)

m.c670 = Constraint(expr=   336*m.b118 + m.x559 - m.x691 <= 336)

m.c671 = Constraint(expr=   336*m.b119 + m.x559 - m.x692 <= 336)

m.c672 = Constraint(expr=   336*m.b120 + m.x559 - m.x693 <= 336)

m.c673 = Constraint(expr=   336*m.b121 + m.x560 - m.x694 <= 336)

m.c674 = Constraint(expr=   336*m.b122 + m.x560 - m.x695 <= 336)

m.c675 = Constraint(expr=   336*m.b123 + m.x560 - m.x696 <= 336)

m.c676 = Constraint(expr=   336*m.b124 + m.x560 - m.x697 <= 336)

m.c677 = Constraint(expr=   336*m.b125 + m.x560 - m.x698 <= 336)

m.c678 = Constraint(expr=   336*m.b126 + m.x560 - m.x699 <= 336)

m.c679 = Constraint(expr=   336*m.b127 + m.x560 - m.x700 <= 336)

m.c680 = Constraint(expr=   336*m.b128 + m.x560 - m.x701 <= 336)

m.c681 = Constraint(expr=   336*m.b129 + m.x560 - m.x702 <= 336)

m.c682 = Constraint(expr=   336*m.b130 + m.x560 - m.x703 <= 336)

m.c683 = Constraint(expr=   336*m.b131 + m.x560 - m.x704 <= 336)

m.c684 = Constraint(expr=   336*m.b132 + m.x560 - m.x705 <= 336)

m.c685 = Constraint(expr=   336*m.b133 + m.x561 - m.x706 <= 336)

m.c686 = Constraint(expr=   336*m.b134 + m.x561 - m.x707 <= 336)

m.c687 = Constraint(expr=   336*m.b135 + m.x561 - m.x708 <= 336)

m.c688 = Constraint(expr=   336*m.b136 + m.x561 - m.x709 <= 336)

m.c689 = Constraint(expr=   336*m.b137 + m.x561 - m.x710 <= 336)

m.c690 = Constraint(expr=   336*m.b138 + m.x561 - m.x711 <= 336)

m.c691 = Constraint(expr=   336*m.b139 + m.x561 - m.x712 <= 336)

m.c692 = Constraint(expr=   336*m.b140 + m.x561 - m.x713 <= 336)

m.c693 = Constraint(expr=   336*m.b141 + m.x561 - m.x714 <= 336)

m.c694 = Constraint(expr=   336*m.b142 + m.x561 - m.x715 <= 336)

m.c695 = Constraint(expr=   336*m.b143 + m.x561 - m.x716 <= 336)

m.c696 = Constraint(expr=   336*m.b144 + m.x561 - m.x717 <= 336)

m.c697 = Constraint(expr= - 336*m.b1 + m.x562 - m.x718 >= -336)

m.c698 = Constraint(expr= - 336*m.b2 + m.x562 - m.x719 >= -336)

m.c699 = Constraint(expr= - 336*m.b3 + m.x562 - m.x720 >= -336)

m.c700 = Constraint(expr= - 336*m.b4 + m.x562 - m.x721 >= -336)

m.c701 = Constraint(expr= - 336*m.b5 + m.x562 - m.x722 >= -336)

m.c702 = Constraint(expr= - 336*m.b6 + m.x562 - m.x723 >= -336)

m.c703 = Constraint(expr= - 336*m.b7 + m.x562 - m.x724 >= -336)

m.c704 = Constraint(expr= - 336*m.b8 + m.x562 - m.x725 >= -336)

m.c705 = Constraint(expr= - 336*m.b9 + m.x562 - m.x726 >= -336)

m.c706 = Constraint(expr= - 336*m.b10 + m.x562 - m.x727 >= -336)

m.c707 = Constraint(expr= - 336*m.b11 + m.x562 - m.x728 >= -336)

m.c708 = Constraint(expr= - 336*m.b12 + m.x562 - m.x729 >= -336)

m.c709 = Constraint(expr= - 336*m.b13 + m.x563 - m.x730 >= -336)

m.c710 = Constraint(expr= - 336*m.b14 + m.x563 - m.x731 >= -336)

m.c711 = Constraint(expr= - 336*m.b15 + m.x563 - m.x732 >= -336)

m.c712 = Constraint(expr= - 336*m.b16 + m.x563 - m.x733 >= -336)

m.c713 = Constraint(expr= - 336*m.b17 + m.x563 - m.x734 >= -336)

m.c714 = Constraint(expr= - 336*m.b18 + m.x563 - m.x735 >= -336)

m.c715 = Constraint(expr= - 336*m.b19 + m.x563 - m.x736 >= -336)

m.c716 = Constraint(expr= - 336*m.b20 + m.x563 - m.x737 >= -336)

m.c717 = Constraint(expr= - 336*m.b21 + m.x563 - m.x738 >= -336)

m.c718 = Constraint(expr= - 336*m.b22 + m.x563 - m.x739 >= -336)

m.c719 = Constraint(expr= - 336*m.b23 + m.x563 - m.x740 >= -336)

m.c720 = Constraint(expr= - 336*m.b24 + m.x563 - m.x741 >= -336)

m.c721 = Constraint(expr= - 336*m.b25 + m.x564 - m.x742 >= -336)

m.c722 = Constraint(expr= - 336*m.b26 + m.x564 - m.x743 >= -336)

m.c723 = Constraint(expr= - 336*m.b27 + m.x564 - m.x744 >= -336)

m.c724 = Constraint(expr= - 336*m.b28 + m.x564 - m.x745 >= -336)

m.c725 = Constraint(expr= - 336*m.b29 + m.x564 - m.x746 >= -336)

m.c726 = Constraint(expr= - 336*m.b30 + m.x564 - m.x747 >= -336)

m.c727 = Constraint(expr= - 336*m.b31 + m.x564 - m.x748 >= -336)

m.c728 = Constraint(expr= - 336*m.b32 + m.x564 - m.x749 >= -336)

m.c729 = Constraint(expr= - 336*m.b33 + m.x564 - m.x750 >= -336)

m.c730 = Constraint(expr= - 336*m.b34 + m.x564 - m.x751 >= -336)

m.c731 = Constraint(expr= - 336*m.b35 + m.x564 - m.x752 >= -336)

m.c732 = Constraint(expr= - 336*m.b36 + m.x564 - m.x753 >= -336)

m.c733 = Constraint(expr= - 336*m.b37 + m.x565 - m.x754 >= -336)

m.c734 = Constraint(expr= - 336*m.b38 + m.x565 - m.x755 >= -336)

m.c735 = Constraint(expr= - 336*m.b39 + m.x565 - m.x756 >= -336)

m.c736 = Constraint(expr= - 336*m.b40 + m.x565 - m.x757 >= -336)

m.c737 = Constraint(expr= - 336*m.b41 + m.x565 - m.x758 >= -336)

m.c738 = Constraint(expr= - 336*m.b42 + m.x565 - m.x759 >= -336)

m.c739 = Constraint(expr= - 336*m.b43 + m.x565 - m.x760 >= -336)

m.c740 = Constraint(expr= - 336*m.b44 + m.x565 - m.x761 >= -336)

m.c741 = Constraint(expr= - 336*m.b45 + m.x565 - m.x762 >= -336)

m.c742 = Constraint(expr= - 336*m.b46 + m.x565 - m.x763 >= -336)

m.c743 = Constraint(expr= - 336*m.b47 + m.x565 - m.x764 >= -336)

m.c744 = Constraint(expr= - 336*m.b48 + m.x565 - m.x765 >= -336)

m.c745 = Constraint(expr= - 336*m.b49 + m.x566 - m.x766 >= -336)

m.c746 = Constraint(expr= - 336*m.b50 + m.x566 - m.x767 >= -336)

m.c747 = Constraint(expr= - 336*m.b51 + m.x566 - m.x768 >= -336)

m.c748 = Constraint(expr= - 336*m.b52 + m.x566 - m.x769 >= -336)

m.c749 = Constraint(expr= - 336*m.b53 + m.x566 - m.x770 >= -336)

m.c750 = Constraint(expr= - 336*m.b54 + m.x566 - m.x771 >= -336)

m.c751 = Constraint(expr= - 336*m.b55 + m.x566 - m.x772 >= -336)

m.c752 = Constraint(expr= - 336*m.b56 + m.x566 - m.x773 >= -336)

m.c753 = Constraint(expr= - 336*m.b57 + m.x566 - m.x774 >= -336)

m.c754 = Constraint(expr= - 336*m.b58 + m.x566 - m.x775 >= -336)

m.c755 = Constraint(expr= - 336*m.b59 + m.x566 - m.x776 >= -336)

m.c756 = Constraint(expr= - 336*m.b60 + m.x566 - m.x777 >= -336)

m.c757 = Constraint(expr= - 336*m.b61 + m.x567 - m.x778 >= -336)

m.c758 = Constraint(expr= - 336*m.b62 + m.x567 - m.x779 >= -336)

m.c759 = Constraint(expr= - 336*m.b63 + m.x567 - m.x780 >= -336)

m.c760 = Constraint(expr= - 336*m.b64 + m.x567 - m.x781 >= -336)

m.c761 = Constraint(expr= - 336*m.b65 + m.x567 - m.x782 >= -336)

m.c762 = Constraint(expr= - 336*m.b66 + m.x567 - m.x783 >= -336)

m.c763 = Constraint(expr= - 336*m.b67 + m.x567 - m.x784 >= -336)

m.c764 = Constraint(expr= - 336*m.b68 + m.x567 - m.x785 >= -336)

m.c765 = Constraint(expr= - 336*m.b69 + m.x567 - m.x786 >= -336)

m.c766 = Constraint(expr= - 336*m.b70 + m.x567 - m.x787 >= -336)

m.c767 = Constraint(expr= - 336*m.b71 + m.x567 - m.x788 >= -336)

m.c768 = Constraint(expr= - 336*m.b72 + m.x567 - m.x789 >= -336)

m.c769 = Constraint(expr= - 336*m.b73 + m.x568 - m.x790 >= -336)

m.c770 = Constraint(expr= - 336*m.b74 + m.x568 - m.x791 >= -336)

m.c771 = Constraint(expr= - 336*m.b75 + m.x568 - m.x792 >= -336)

m.c772 = Constraint(expr= - 336*m.b76 + m.x568 - m.x793 >= -336)

m.c773 = Constraint(expr= - 336*m.b77 + m.x568 - m.x794 >= -336)

m.c774 = Constraint(expr= - 336*m.b78 + m.x568 - m.x795 >= -336)

m.c775 = Constraint(expr= - 336*m.b79 + m.x568 - m.x796 >= -336)

m.c776 = Constraint(expr= - 336*m.b80 + m.x568 - m.x797 >= -336)

m.c777 = Constraint(expr= - 336*m.b81 + m.x568 - m.x798 >= -336)

m.c778 = Constraint(expr= - 336*m.b82 + m.x568 - m.x799 >= -336)

m.c779 = Constraint(expr= - 336*m.b83 + m.x568 - m.x800 >= -336)

m.c780 = Constraint(expr= - 336*m.b84 + m.x568 - m.x801 >= -336)

m.c781 = Constraint(expr= - 336*m.b85 + m.x569 - m.x802 >= -336)

m.c782 = Constraint(expr= - 336*m.b86 + m.x569 - m.x803 >= -336)

m.c783 = Constraint(expr= - 336*m.b87 + m.x569 - m.x804 >= -336)

m.c784 = Constraint(expr= - 336*m.b88 + m.x569 - m.x805 >= -336)

m.c785 = Constraint(expr= - 336*m.b89 + m.x569 - m.x806 >= -336)

m.c786 = Constraint(expr= - 336*m.b90 + m.x569 - m.x807 >= -336)

m.c787 = Constraint(expr= - 336*m.b91 + m.x569 - m.x808 >= -336)

m.c788 = Constraint(expr= - 336*m.b92 + m.x569 - m.x809 >= -336)

m.c789 = Constraint(expr= - 336*m.b93 + m.x569 - m.x810 >= -336)

m.c790 = Constraint(expr= - 336*m.b94 + m.x569 - m.x811 >= -336)

m.c791 = Constraint(expr= - 336*m.b95 + m.x569 - m.x812 >= -336)

m.c792 = Constraint(expr= - 336*m.b96 + m.x569 - m.x813 >= -336)

m.c793 = Constraint(expr= - 336*m.b97 + m.x570 - m.x814 >= -336)

m.c794 = Constraint(expr= - 336*m.b98 + m.x570 - m.x815 >= -336)

m.c795 = Constraint(expr= - 336*m.b99 + m.x570 - m.x816 >= -336)

m.c796 = Constraint(expr= - 336*m.b100 + m.x570 - m.x817 >= -336)

m.c797 = Constraint(expr= - 336*m.b101 + m.x570 - m.x818 >= -336)

m.c798 = Constraint(expr= - 336*m.b102 + m.x570 - m.x819 >= -336)

m.c799 = Constraint(expr= - 336*m.b103 + m.x570 - m.x820 >= -336)

m.c800 = Constraint(expr= - 336*m.b104 + m.x570 - m.x821 >= -336)

m.c801 = Constraint(expr= - 336*m.b105 + m.x570 - m.x822 >= -336)

m.c802 = Constraint(expr= - 336*m.b106 + m.x570 - m.x823 >= -336)

m.c803 = Constraint(expr= - 336*m.b107 + m.x570 - m.x824 >= -336)

m.c804 = Constraint(expr= - 336*m.b108 + m.x570 - m.x825 >= -336)

m.c805 = Constraint(expr= - 336*m.b109 + m.x571 - m.x826 >= -336)

m.c806 = Constraint(expr= - 336*m.b110 + m.x571 - m.x827 >= -336)

m.c807 = Constraint(expr= - 336*m.b111 + m.x571 - m.x828 >= -336)

m.c808 = Constraint(expr= - 336*m.b112 + m.x571 - m.x829 >= -336)

m.c809 = Constraint(expr= - 336*m.b113 + m.x571 - m.x830 >= -336)

m.c810 = Constraint(expr= - 336*m.b114 + m.x571 - m.x831 >= -336)

m.c811 = Constraint(expr= - 336*m.b115 + m.x571 - m.x832 >= -336)

m.c812 = Constraint(expr= - 336*m.b116 + m.x571 - m.x833 >= -336)

m.c813 = Constraint(expr= - 336*m.b117 + m.x571 - m.x834 >= -336)

m.c814 = Constraint(expr= - 336*m.b118 + m.x571 - m.x835 >= -336)

m.c815 = Constraint(expr= - 336*m.b119 + m.x571 - m.x836 >= -336)

m.c816 = Constraint(expr= - 336*m.b120 + m.x571 - m.x837 >= -336)

m.c817 = Constraint(expr= - 336*m.b121 + m.x572 - m.x838 >= -336)

m.c818 = Constraint(expr= - 336*m.b122 + m.x572 - m.x839 >= -336)

m.c819 = Constraint(expr= - 336*m.b123 + m.x572 - m.x840 >= -336)

m.c820 = Constraint(expr= - 336*m.b124 + m.x572 - m.x841 >= -336)

m.c821 = Constraint(expr= - 336*m.b125 + m.x572 - m.x842 >= -336)

m.c822 = Constraint(expr= - 336*m.b126 + m.x572 - m.x843 >= -336)

m.c823 = Constraint(expr= - 336*m.b127 + m.x572 - m.x844 >= -336)

m.c824 = Constraint(expr= - 336*m.b128 + m.x572 - m.x845 >= -336)

m.c825 = Constraint(expr= - 336*m.b129 + m.x572 - m.x846 >= -336)

m.c826 = Constraint(expr= - 336*m.b130 + m.x572 - m.x847 >= -336)

m.c827 = Constraint(expr= - 336*m.b131 + m.x572 - m.x848 >= -336)

m.c828 = Constraint(expr= - 336*m.b132 + m.x572 - m.x849 >= -336)

m.c829 = Constraint(expr= - 336*m.b133 + m.x573 - m.x850 >= -336)

m.c830 = Constraint(expr= - 336*m.b134 + m.x573 - m.x851 >= -336)

m.c831 = Constraint(expr= - 336*m.b135 + m.x573 - m.x852 >= -336)

m.c832 = Constraint(expr= - 336*m.b136 + m.x573 - m.x853 >= -336)

m.c833 = Constraint(expr= - 336*m.b137 + m.x573 - m.x854 >= -336)

m.c834 = Constraint(expr= - 336*m.b138 + m.x573 - m.x855 >= -336)

m.c835 = Constraint(expr= - 336*m.b139 + m.x573 - m.x856 >= -336)

m.c836 = Constraint(expr= - 336*m.b140 + m.x573 - m.x857 >= -336)

m.c837 = Constraint(expr= - 336*m.b141 + m.x573 - m.x858 >= -336)

m.c838 = Constraint(expr= - 336*m.b142 + m.x573 - m.x859 >= -336)

m.c839 = Constraint(expr= - 336*m.b143 + m.x573 - m.x860 >= -336)

m.c840 = Constraint(expr= - 336*m.b144 + m.x573 - m.x861 >= -336)

m.c841 = Constraint(expr=   m.x551 - m.x562 >= 0)

m.c842 = Constraint(expr=   m.x552 - m.x563 >= 0)

m.c843 = Constraint(expr=   m.x553 - m.x564 >= 0)

m.c844 = Constraint(expr=   m.x554 - m.x565 >= 0)

m.c845 = Constraint(expr=   m.x555 - m.x566 >= 0)

m.c846 = Constraint(expr=   m.x556 - m.x567 >= 0)

m.c847 = Constraint(expr=   m.x557 - m.x568 >= 0)

m.c848 = Constraint(expr=   m.x558 - m.x569 >= 0)

m.c849 = Constraint(expr=   m.x559 - m.x570 >= 0)

m.c850 = Constraint(expr=   m.x560 - m.x571 >= 0)

m.c851 = Constraint(expr=   m.x561 - m.x572 >= 0)

m.c852 = Constraint(expr= - m.x952 + m.x976 + m.x979 + m.x982 + m.x985 == 0)

m.c853 = Constraint(expr= - m.x953 + m.x977 + m.x980 + m.x983 + m.x986 == 0)

m.c854 = Constraint(expr= - m.x954 + m.x978 + m.x981 + m.x984 + m.x987 == 0)

m.c855 = Constraint(expr= - m.x955 + m.x988 + m.x991 + m.x994 + m.x997 == 0)

m.c856 = Constraint(expr= - m.x956 + m.x989 + m.x992 + m.x995 + m.x998 == 0)

m.c857 = Constraint(expr= - m.x957 + m.x990 + m.x993 + m.x996 + m.x999 == 0)

m.c858 = Constraint(expr= - m.x958 + m.x1000 + m.x1003 + m.x1006 + m.x1009 == 0)

m.c859 = Constraint(expr= - m.x959 + m.x1001 + m.x1004 + m.x1007 + m.x1010 == 0)

m.c860 = Constraint(expr= - m.x960 + m.x1002 + m.x1005 + m.x1008 + m.x1011 == 0)

m.c861 = Constraint(expr= - m.x961 + m.x1012 + m.x1015 + m.x1018 + m.x1021 == 0)

m.c862 = Constraint(expr= - m.x962 + m.x1013 + m.x1016 + m.x1019 + m.x1022 == 0)

m.c863 = Constraint(expr= - m.x963 + m.x1014 + m.x1017 + m.x1020 + m.x1023 == 0)

m.c864 = Constraint(expr= - m.x964 + m.x1024 + m.x1027 + m.x1030 + m.x1033 == 0)

m.c865 = Constraint(expr= - m.x965 + m.x1025 + m.x1028 + m.x1031 + m.x1034 == 0)

m.c866 = Constraint(expr= - m.x966 + m.x1026 + m.x1029 + m.x1032 + m.x1035 == 0)

m.c867 = Constraint(expr= - m.x967 + m.x1036 + m.x1039 + m.x1042 + m.x1045 == 0)

m.c868 = Constraint(expr= - m.x968 + m.x1037 + m.x1040 + m.x1043 + m.x1046 == 0)

m.c869 = Constraint(expr= - m.x969 + m.x1038 + m.x1041 + m.x1044 + m.x1047 == 0)

m.c870 = Constraint(expr= - m.x970 + m.x1048 + m.x1051 + m.x1054 + m.x1057 == 0)

m.c871 = Constraint(expr= - m.x971 + m.x1049 + m.x1052 + m.x1055 + m.x1058 == 0)

m.c872 = Constraint(expr= - m.x972 + m.x1050 + m.x1053 + m.x1056 + m.x1059 == 0)

m.c873 = Constraint(expr= - m.x973 + m.x1060 + m.x1063 + m.x1066 + m.x1069 == 0)

m.c874 = Constraint(expr= - m.x974 + m.x1061 + m.x1064 + m.x1067 + m.x1070 == 0)

m.c875 = Constraint(expr= - m.x975 + m.x1062 + m.x1065 + m.x1068 + m.x1071 == 0)

m.c876 = Constraint(expr= - 0.25*m.x217 + m.x253 == 0)

m.c877 = Constraint(expr= - 0.25*m.x217 + m.x256 == 0)

m.c878 = Constraint(expr= - 0.25*m.x217 + m.x259 == 0)

m.c879 = Constraint(expr= - 0.25*m.x217 + m.x262 == 0)

m.c880 = Constraint(expr= - 0.25*m.x220 + m.x265 == 0)

m.c881 = Constraint(expr= - 0.25*m.x220 + m.x268 == 0)

m.c882 = Constraint(expr= - 0.25*m.x220 + m.x271 == 0)

m.c883 = Constraint(expr= - 0.25*m.x220 + m.x274 == 0)

m.c884 = Constraint(expr= - 0.25*m.x223 + m.x277 == 0)

m.c885 = Constraint(expr= - 0.25*m.x223 + m.x280 == 0)

m.c886 = Constraint(expr= - 0.25*m.x223 + m.x283 == 0)

m.c887 = Constraint(expr= - 0.25*m.x223 + m.x286 == 0)

m.c888 = Constraint(expr= - 0.285714285714286*m.x226 + m.x289 == 0)

m.c889 = Constraint(expr= - 0.285714285714286*m.x226 + m.x292 == 0)

m.c890 = Constraint(expr= - 0.142857142857143*m.x226 + m.x295 == 0)

m.c891 = Constraint(expr= - 0.285714285714286*m.x226 + m.x298 == 0)

m.c892 = Constraint(expr= - 0.285714285714286*m.x229 + m.x301 == 0)

m.c893 = Constraint(expr= - 0.285714285714286*m.x229 + m.x304 == 0)

m.c894 = Constraint(expr= - 0.142857142857143*m.x229 + m.x307 == 0)

m.c895 = Constraint(expr= - 0.285714285714286*m.x229 + m.x310 == 0)

m.c896 = Constraint(expr= - 0.210526315789474*m.x232 + m.x313 == 0)

m.c897 = Constraint(expr= - 0.263157894736842*m.x232 + m.x316 == 0)

m.c898 = Constraint(expr= - 0.210526315789474*m.x232 + m.x319 == 0)

m.c899 = Constraint(expr= - 0.315789473684211*m.x232 + m.x322 == 0)

m.c900 = Constraint(expr= - 0.210526315789474*m.x235 + m.x325 == 0)

m.c901 = Constraint(expr= - 0.263157894736842*m.x235 + m.x328 == 0)

m.c902 = Constraint(expr= - 0.210526315789474*m.x235 + m.x331 == 0)

m.c903 = Constraint(expr= - 0.315789473684211*m.x235 + m.x334 == 0)

m.c904 = Constraint(expr= - 0.25*m.x238 + m.x337 == 0)

m.c905 = Constraint(expr= - 0.25*m.x238 + m.x340 == 0)

m.c906 = Constraint(expr= - 0.25*m.x238 + m.x343 == 0)

m.c907 = Constraint(expr= - 0.25*m.x238 + m.x346 == 0)

m.c908 = Constraint(expr= - 0.25*m.x241 + m.x349 == 0)

m.c909 = Constraint(expr= - 0.25*m.x241 + m.x352 == 0)

m.c910 = Constraint(expr= - 0.25*m.x241 + m.x355 == 0)

m.c911 = Constraint(expr= - 0.25*m.x241 + m.x358 == 0)

m.c912 = Constraint(expr= - 0.25*m.x244 + m.x361 == 0)

m.c913 = Constraint(expr= - 0.25*m.x244 + m.x364 == 0)

m.c914 = Constraint(expr= - 0.25*m.x244 + m.x367 == 0)

m.c915 = Constraint(expr= - 0.25*m.x244 + m.x370 == 0)

m.c916 = Constraint(expr= - 0.25*m.x247 + m.x373 == 0)

m.c917 = Constraint(expr= - 0.25*m.x247 + m.x376 == 0)

m.c918 = Constraint(expr= - 0.25*m.x247 + m.x379 == 0)

m.c919 = Constraint(expr= - 0.25*m.x247 + m.x382 == 0)

m.c920 = Constraint(expr= - 0.222222222222222*m.x250 + m.x385 == 0)

m.c921 = Constraint(expr= - 0.222222222222222*m.x250 + m.x388 == 0)

m.c922 = Constraint(expr= - 0.222222222222222*m.x250 + m.x391 == 0)

m.c923 = Constraint(expr= - 0.333333333333333*m.x250 + m.x394 == 0)

m.c924 = Constraint(expr=   m.b1 + m.b181 <= 1)

m.c925 = Constraint(expr=   m.b2 + m.b182 <= 1)

m.c926 = Constraint(expr=   m.b3 + m.b183 <= 1)

m.c927 = Constraint(expr=   m.b4 + m.b208 <= 1)

m.c928 = Constraint(expr=   m.b5 + m.b209 <= 1)

m.c929 = Constraint(expr=   m.b6 + m.b210 <= 1)

m.c930 = Constraint(expr=   m.b7 + m.b211 <= 1)

m.c931 = Constraint(expr=   m.b8 + m.b212 <= 1)

m.c932 = Constraint(expr=   m.b9 + m.b213 <= 1)

m.c933 = Constraint(expr=   m.b10 + m.b214 <= 1)

m.c934 = Constraint(expr=   m.b11 + m.b215 <= 1)

m.c935 = Constraint(expr=   m.b12 + m.b216 <= 1)

m.c936 = Constraint(expr=   m.b13 + m.b181 <= 1)

m.c937 = Constraint(expr=   m.b14 + m.b182 <= 1)

m.c938 = Constraint(expr=   m.b15 + m.b183 <= 1)

m.c939 = Constraint(expr=   m.b16 + m.b208 <= 1)

m.c940 = Constraint(expr=   m.b17 + m.b209 <= 1)

m.c941 = Constraint(expr=   m.b18 + m.b210 <= 1)

m.c942 = Constraint(expr=   m.b19 + m.b211 <= 1)

m.c943 = Constraint(expr=   m.b20 + m.b212 <= 1)

m.c944 = Constraint(expr=   m.b21 + m.b213 <= 1)

m.c945 = Constraint(expr=   m.b22 + m.b214 <= 1)

m.c946 = Constraint(expr=   m.b23 + m.b215 <= 1)

m.c947 = Constraint(expr=   m.b24 + m.b216 <= 1)

m.c948 = Constraint(expr=   m.b25 + m.b181 <= 1)

m.c949 = Constraint(expr=   m.b26 + m.b182 <= 1)

m.c950 = Constraint(expr=   m.b27 + m.b183 <= 1)

m.c951 = Constraint(expr=   m.b28 + m.b208 <= 1)

m.c952 = Constraint(expr=   m.b29 + m.b209 <= 1)

m.c953 = Constraint(expr=   m.b30 + m.b210 <= 1)

m.c954 = Constraint(expr=   m.b31 + m.b211 <= 1)

m.c955 = Constraint(expr=   m.b32 + m.b212 <= 1)

m.c956 = Constraint(expr=   m.b33 + m.b213 <= 1)

m.c957 = Constraint(expr=   m.b34 + m.b214 <= 1)

m.c958 = Constraint(expr=   m.b35 + m.b215 <= 1)

m.c959 = Constraint(expr=   m.b36 + m.b216 <= 1)

m.c960 = Constraint(expr=   m.b37 + m.b184 <= 1)

m.c961 = Constraint(expr=   m.b38 + m.b185 <= 1)

m.c962 = Constraint(expr=   m.b39 + m.b186 <= 1)

m.c963 = Constraint(expr=   m.b37 + m.b187 <= 1)

m.c964 = Constraint(expr=   m.b38 + m.b188 <= 1)

m.c965 = Constraint(expr=   m.b39 + m.b189 <= 1)

m.c966 = Constraint(expr=   m.b40 + m.b190 <= 1)

m.c967 = Constraint(expr=   m.b41 + m.b191 <= 1)

m.c968 = Constraint(expr=   m.b42 + m.b192 <= 1)

m.c969 = Constraint(expr=   m.b40 + m.b193 <= 1)

m.c970 = Constraint(expr=   m.b41 + m.b194 <= 1)

m.c971 = Constraint(expr=   m.b42 + m.b195 <= 1)

m.c972 = Constraint(expr=   m.b43 + m.b196 <= 1)

m.c973 = Constraint(expr=   m.b44 + m.b197 <= 1)

m.c974 = Constraint(expr=   m.b45 + m.b198 <= 1)

m.c975 = Constraint(expr=   m.b43 + m.b199 <= 1)

m.c976 = Constraint(expr=   m.b44 + m.b200 <= 1)

m.c977 = Constraint(expr=   m.b45 + m.b201 <= 1)

m.c978 = Constraint(expr=   m.b46 + m.b202 <= 1)

m.c979 = Constraint(expr=   m.b47 + m.b203 <= 1)

m.c980 = Constraint(expr=   m.b48 + m.b204 <= 1)

m.c981 = Constraint(expr=   m.b46 + m.b205 <= 1)

m.c982 = Constraint(expr=   m.b47 + m.b206 <= 1)

m.c983 = Constraint(expr=   m.b48 + m.b207 <= 1)

m.c984 = Constraint(expr=   m.b49 + m.b184 <= 1)

m.c985 = Constraint(expr=   m.b50 + m.b185 <= 1)

m.c986 = Constraint(expr=   m.b51 + m.b186 <= 1)

m.c987 = Constraint(expr=   m.b49 + m.b187 <= 1)

m.c988 = Constraint(expr=   m.b50 + m.b188 <= 1)

m.c989 = Constraint(expr=   m.b51 + m.b189 <= 1)

m.c990 = Constraint(expr=   m.b52 + m.b190 <= 1)

m.c991 = Constraint(expr=   m.b53 + m.b191 <= 1)

m.c992 = Constraint(expr=   m.b54 + m.b192 <= 1)

m.c993 = Constraint(expr=   m.b52 + m.b193 <= 1)

m.c994 = Constraint(expr=   m.b53 + m.b194 <= 1)

m.c995 = Constraint(expr=   m.b54 + m.b195 <= 1)

m.c996 = Constraint(expr=   m.b55 + m.b196 <= 1)

m.c997 = Constraint(expr=   m.b56 + m.b197 <= 1)

m.c998 = Constraint(expr=   m.b57 + m.b198 <= 1)

m.c999 = Constraint(expr=   m.b55 + m.b199 <= 1)

m.c1000 = Constraint(expr=   m.b56 + m.b200 <= 1)

m.c1001 = Constraint(expr=   m.b57 + m.b201 <= 1)

m.c1002 = Constraint(expr=   m.b58 + m.b202 <= 1)

m.c1003 = Constraint(expr=   m.b59 + m.b203 <= 1)

m.c1004 = Constraint(expr=   m.b60 + m.b204 <= 1)

m.c1005 = Constraint(expr=   m.b58 + m.b205 <= 1)

m.c1006 = Constraint(expr=   m.b59 + m.b206 <= 1)

m.c1007 = Constraint(expr=   m.b60 + m.b207 <= 1)

m.c1008 = Constraint(expr=   m.b61 + m.b184 <= 1)

m.c1009 = Constraint(expr=   m.b62 + m.b185 <= 1)

m.c1010 = Constraint(expr=   m.b63 + m.b186 <= 1)

m.c1011 = Constraint(expr=   m.b61 + m.b187 <= 1)

m.c1012 = Constraint(expr=   m.b62 + m.b188 <= 1)

m.c1013 = Constraint(expr=   m.b63 + m.b189 <= 1)

m.c1014 = Constraint(expr=   m.b64 + m.b190 <= 1)

m.c1015 = Constraint(expr=   m.b65 + m.b191 <= 1)

m.c1016 = Constraint(expr=   m.b66 + m.b192 <= 1)

m.c1017 = Constraint(expr=   m.b64 + m.b193 <= 1)

m.c1018 = Constraint(expr=   m.b65 + m.b194 <= 1)

m.c1019 = Constraint(expr=   m.b66 + m.b195 <= 1)

m.c1020 = Constraint(expr=   m.b67 + m.b196 <= 1)

m.c1021 = Constraint(expr=   m.b68 + m.b197 <= 1)

m.c1022 = Constraint(expr=   m.b69 + m.b198 <= 1)

m.c1023 = Constraint(expr=   m.b67 + m.b199 <= 1)

m.c1024 = Constraint(expr=   m.b68 + m.b200 <= 1)

m.c1025 = Constraint(expr=   m.b69 + m.b201 <= 1)

m.c1026 = Constraint(expr=   m.b70 + m.b202 <= 1)

m.c1027 = Constraint(expr=   m.b71 + m.b203 <= 1)

m.c1028 = Constraint(expr=   m.b72 + m.b204 <= 1)

m.c1029 = Constraint(expr=   m.b70 + m.b205 <= 1)

m.c1030 = Constraint(expr=   m.b71 + m.b206 <= 1)

m.c1031 = Constraint(expr=   m.b72 + m.b207 <= 1)

m.c1032 = Constraint(expr=   m.b73 + m.b184 <= 1)

m.c1033 = Constraint(expr=   m.b74 + m.b185 <= 1)

m.c1034 = Constraint(expr=   m.b75 + m.b186 <= 1)

m.c1035 = Constraint(expr=   m.b73 + m.b187 <= 1)

m.c1036 = Constraint(expr=   m.b74 + m.b188 <= 1)

m.c1037 = Constraint(expr=   m.b75 + m.b189 <= 1)

m.c1038 = Constraint(expr=   m.b76 + m.b190 <= 1)

m.c1039 = Constraint(expr=   m.b77 + m.b191 <= 1)

m.c1040 = Constraint(expr=   m.b78 + m.b192 <= 1)

m.c1041 = Constraint(expr=   m.b76 + m.b193 <= 1)

m.c1042 = Constraint(expr=   m.b77 + m.b194 <= 1)

m.c1043 = Constraint(expr=   m.b78 + m.b195 <= 1)

m.c1044 = Constraint(expr=   m.b79 + m.b196 <= 1)

m.c1045 = Constraint(expr=   m.b80 + m.b197 <= 1)

m.c1046 = Constraint(expr=   m.b81 + m.b198 <= 1)

m.c1047 = Constraint(expr=   m.b79 + m.b199 <= 1)

m.c1048 = Constraint(expr=   m.b80 + m.b200 <= 1)

m.c1049 = Constraint(expr=   m.b81 + m.b201 <= 1)

m.c1050 = Constraint(expr=   m.b82 + m.b202 <= 1)

m.c1051 = Constraint(expr=   m.b83 + m.b203 <= 1)

m.c1052 = Constraint(expr=   m.b84 + m.b204 <= 1)

m.c1053 = Constraint(expr=   m.b82 + m.b205 <= 1)

m.c1054 = Constraint(expr=   m.b83 + m.b206 <= 1)

m.c1055 = Constraint(expr=   m.b84 + m.b207 <= 1)

m.c1056 = Constraint(expr=   m.b85 + m.b181 <= 1)

m.c1057 = Constraint(expr=   m.b86 + m.b182 <= 1)

m.c1058 = Constraint(expr=   m.b87 + m.b183 <= 1)

m.c1059 = Constraint(expr=   m.b88 + m.b208 <= 1)

m.c1060 = Constraint(expr=   m.b89 + m.b209 <= 1)

m.c1061 = Constraint(expr=   m.b90 + m.b210 <= 1)

m.c1062 = Constraint(expr=   m.b91 + m.b211 <= 1)

m.c1063 = Constraint(expr=   m.b92 + m.b212 <= 1)

m.c1064 = Constraint(expr=   m.b93 + m.b213 <= 1)

m.c1065 = Constraint(expr=   m.b94 + m.b214 <= 1)

m.c1066 = Constraint(expr=   m.b95 + m.b215 <= 1)

m.c1067 = Constraint(expr=   m.b96 + m.b216 <= 1)

m.c1068 = Constraint(expr=   m.b97 + m.b181 <= 1)

m.c1069 = Constraint(expr=   m.b98 + m.b182 <= 1)

m.c1070 = Constraint(expr=   m.b99 + m.b183 <= 1)

m.c1071 = Constraint(expr=   m.b100 + m.b208 <= 1)

m.c1072 = Constraint(expr=   m.b101 + m.b209 <= 1)

m.c1073 = Constraint(expr=   m.b102 + m.b210 <= 1)

m.c1074 = Constraint(expr=   m.b103 + m.b211 <= 1)

m.c1075 = Constraint(expr=   m.b104 + m.b212 <= 1)

m.c1076 = Constraint(expr=   m.b105 + m.b213 <= 1)

m.c1077 = Constraint(expr=   m.b106 + m.b214 <= 1)

m.c1078 = Constraint(expr=   m.b107 + m.b215 <= 1)

m.c1079 = Constraint(expr=   m.b108 + m.b216 <= 1)

m.c1080 = Constraint(expr=   m.b109 + m.b184 <= 1)

m.c1081 = Constraint(expr=   m.b110 + m.b185 <= 1)

m.c1082 = Constraint(expr=   m.b111 + m.b186 <= 1)

m.c1083 = Constraint(expr=   m.b109 + m.b187 <= 1)

m.c1084 = Constraint(expr=   m.b110 + m.b188 <= 1)

m.c1085 = Constraint(expr=   m.b111 + m.b189 <= 1)

m.c1086 = Constraint(expr=   m.b112 + m.b190 <= 1)

m.c1087 = Constraint(expr=   m.b113 + m.b191 <= 1)

m.c1088 = Constraint(expr=   m.b114 + m.b192 <= 1)

m.c1089 = Constraint(expr=   m.b112 + m.b193 <= 1)

m.c1090 = Constraint(expr=   m.b113 + m.b194 <= 1)

m.c1091 = Constraint(expr=   m.b114 + m.b195 <= 1)

m.c1092 = Constraint(expr=   m.b115 + m.b196 <= 1)

m.c1093 = Constraint(expr=   m.b116 + m.b197 <= 1)

m.c1094 = Constraint(expr=   m.b117 + m.b198 <= 1)

m.c1095 = Constraint(expr=   m.b115 + m.b199 <= 1)

m.c1096 = Constraint(expr=   m.b116 + m.b200 <= 1)

m.c1097 = Constraint(expr=   m.b117 + m.b201 <= 1)

m.c1098 = Constraint(expr=   m.b118 + m.b202 <= 1)

m.c1099 = Constraint(expr=   m.b119 + m.b203 <= 1)

m.c1100 = Constraint(expr=   m.b120 + m.b204 <= 1)

m.c1101 = Constraint(expr=   m.b118 + m.b205 <= 1)

m.c1102 = Constraint(expr=   m.b119 + m.b206 <= 1)

m.c1103 = Constraint(expr=   m.b120 + m.b207 <= 1)

m.c1104 = Constraint(expr=   m.b121 + m.b181 <= 1)

m.c1105 = Constraint(expr=   m.b122 + m.b182 <= 1)

m.c1106 = Constraint(expr=   m.b123 + m.b183 <= 1)

m.c1107 = Constraint(expr=   m.b124 + m.b208 <= 1)

m.c1108 = Constraint(expr=   m.b125 + m.b209 <= 1)

m.c1109 = Constraint(expr=   m.b126 + m.b210 <= 1)

m.c1110 = Constraint(expr=   m.b127 + m.b211 <= 1)

m.c1111 = Constraint(expr=   m.b128 + m.b212 <= 1)

m.c1112 = Constraint(expr=   m.b129 + m.b213 <= 1)

m.c1113 = Constraint(expr=   m.b130 + m.b214 <= 1)

m.c1114 = Constraint(expr=   m.b131 + m.b215 <= 1)

m.c1115 = Constraint(expr=   m.b132 + m.b216 <= 1)

m.c1116 = Constraint(expr=   m.b133 + m.b184 <= 1)

m.c1117 = Constraint(expr=   m.b134 + m.b185 <= 1)

m.c1118 = Constraint(expr=   m.b135 + m.b186 <= 1)

m.c1119 = Constraint(expr=   m.b133 + m.b187 <= 1)

m.c1120 = Constraint(expr=   m.b134 + m.b188 <= 1)

m.c1121 = Constraint(expr=   m.b135 + m.b189 <= 1)

m.c1122 = Constraint(expr=   m.b136 + m.b190 <= 1)

m.c1123 = Constraint(expr=   m.b137 + m.b191 <= 1)

m.c1124 = Constraint(expr=   m.b138 + m.b192 <= 1)

m.c1125 = Constraint(expr=   m.b136 + m.b193 <= 1)

m.c1126 = Constraint(expr=   m.b137 + m.b194 <= 1)

m.c1127 = Constraint(expr=   m.b138 + m.b195 <= 1)

m.c1128 = Constraint(expr=   m.b139 + m.b196 <= 1)

m.c1129 = Constraint(expr=   m.b140 + m.b197 <= 1)

m.c1130 = Constraint(expr=   m.b141 + m.b198 <= 1)

m.c1131 = Constraint(expr=   m.b139 + m.b199 <= 1)

m.c1132 = Constraint(expr=   m.b140 + m.b200 <= 1)

m.c1133 = Constraint(expr=   m.b141 + m.b201 <= 1)

m.c1134 = Constraint(expr=   m.b142 + m.b202 <= 1)

m.c1135 = Constraint(expr=   m.b143 + m.b203 <= 1)

m.c1136 = Constraint(expr=   m.b144 + m.b204 <= 1)

m.c1137 = Constraint(expr=   m.b142 + m.b205 <= 1)

m.c1138 = Constraint(expr=   m.b143 + m.b206 <= 1)

m.c1139 = Constraint(expr=   m.b144 + m.b207 <= 1)

m.c1140 = Constraint(expr=   m.b181 <= 2)

m.c1141 = Constraint(expr=   m.b182 <= 2)

m.c1142 = Constraint(expr=   m.b183 <= 2)

m.c1143 = Constraint(expr=   m.b184 + m.b187 <= 2)

m.c1144 = Constraint(expr=   m.b185 + m.b188 <= 2)

m.c1145 = Constraint(expr=   m.b186 + m.b189 <= 2)

m.c1146 = Constraint(expr=   m.b190 + m.b193 <= 2)

m.c1147 = Constraint(expr=   m.b191 + m.b194 <= 2)

m.c1148 = Constraint(expr=   m.b192 + m.b195 <= 2)

m.c1149 = Constraint(expr=   m.b196 + m.b199 <= 2)

m.c1150 = Constraint(expr=   m.b197 + m.b200 <= 2)

m.c1151 = Constraint(expr=   m.b198 + m.b201 <= 2)

m.c1152 = Constraint(expr=   m.b202 + m.b205 <= 2)

m.c1153 = Constraint(expr=   m.b203 + m.b206 <= 2)

m.c1154 = Constraint(expr=   m.b204 + m.b207 <= 2)

m.c1155 = Constraint(expr=   m.b208 <= 2)

m.c1156 = Constraint(expr=   m.b209 <= 2)

m.c1157 = Constraint(expr=   m.b210 <= 2)

m.c1158 = Constraint(expr=   m.b211 <= 2)

m.c1159 = Constraint(expr=   m.b212 <= 2)

m.c1160 = Constraint(expr=   m.b213 <= 2)

m.c1161 = Constraint(expr=   m.b214 <= 2)

m.c1162 = Constraint(expr=   m.b215 <= 2)

m.c1163 = Constraint(expr=   m.b216 <= 2)

m.c1164 = Constraint(expr=   m.b184 + m.b190 + m.b196 + m.b202 <= 2)

m.c1165 = Constraint(expr=   m.b185 + m.b191 + m.b197 + m.b203 <= 2)

m.c1166 = Constraint(expr=   m.b186 + m.b192 + m.b198 + m.b204 <= 2)

m.c1167 = Constraint(expr=   m.b187 + m.b193 + m.b199 + m.b205 <= 2)

m.c1168 = Constraint(expr=   m.b188 + m.b194 + m.b200 + m.b206 <= 2)

m.c1169 = Constraint(expr=   m.b189 + m.b195 + m.b201 + m.b207 <= 2)

m.c1170 = Constraint(expr=   m.b181 + m.b208 + m.b211 + m.b214 <= 2)

m.c1171 = Constraint(expr=   m.b182 + m.b209 + m.b212 + m.b215 <= 2)

m.c1172 = Constraint(expr=   m.b183 + m.b210 + m.b213 + m.b216 <= 2)

m.c1173 = Constraint(expr= - m.x217 - 2.5*m.x862 + 2.5*m.x898 <= 0)

m.c1174 = Constraint(expr= - m.x218 - 2.5*m.x863 + 2.5*m.x899 <= 0)

m.c1175 = Constraint(expr= - m.x219 - 2.5*m.x864 + 2.5*m.x900 <= 0)

m.c1176 = Constraint(expr= - m.x220 - 2.5*m.x865 + 2.5*m.x901 <= 0)

m.c1177 = Constraint(expr= - m.x221 - 2.5*m.x866 + 2.5*m.x902 <= 0)

m.c1178 = Constraint(expr= - m.x222 - 2.5*m.x867 + 2.5*m.x903 <= 0)

m.c1179 = Constraint(expr= - m.x223 - 2.5*m.x868 + 2.5*m.x904 <= 0)

m.c1180 = Constraint(expr= - m.x224 - 2.5*m.x869 + 2.5*m.x905 <= 0)

m.c1181 = Constraint(expr= - m.x225 - 2.5*m.x870 + 2.5*m.x906 <= 0)

m.c1182 = Constraint(expr= - m.x226 - 2.5*m.x871 + 2.5*m.x907 <= 0)

m.c1183 = Constraint(expr= - m.x227 - 2.5*m.x872 + 2.5*m.x908 <= 0)

m.c1184 = Constraint(expr= - m.x228 - 2.5*m.x873 + 2.5*m.x909 <= 0)

m.c1185 = Constraint(expr= - m.x229 - 2.5*m.x874 + 2.5*m.x910 <= 0)

m.c1186 = Constraint(expr= - m.x230 - 2.5*m.x875 + 2.5*m.x911 <= 0)

m.c1187 = Constraint(expr= - m.x231 - 2.5*m.x876 + 2.5*m.x912 <= 0)

m.c1188 = Constraint(expr= - m.x232 - 2.5*m.x877 + 2.5*m.x913 <= 0)

m.c1189 = Constraint(expr= - m.x233 - 2.5*m.x878 + 2.5*m.x914 <= 0)

m.c1190 = Constraint(expr= - m.x234 - 2.5*m.x879 + 2.5*m.x915 <= 0)

m.c1191 = Constraint(expr= - m.x235 - 2.5*m.x880 + 2.5*m.x916 <= 0)

m.c1192 = Constraint(expr= - m.x236 - 2.5*m.x881 + 2.5*m.x917 <= 0)

m.c1193 = Constraint(expr= - m.x237 - 2.5*m.x882 + 2.5*m.x918 <= 0)

m.c1194 = Constraint(expr= - m.x238 - 2.5*m.x883 + 2.5*m.x919 <= 0)

m.c1195 = Constraint(expr= - m.x239 - 2.5*m.x884 + 2.5*m.x920 <= 0)

m.c1196 = Constraint(expr= - m.x240 - 2.5*m.x885 + 2.5*m.x921 <= 0)

m.c1197 = Constraint(expr= - m.x241 - 2.5*m.x886 + 2.5*m.x922 <= 0)

m.c1198 = Constraint(expr= - m.x242 - 2.5*m.x887 + 2.5*m.x923 <= 0)

m.c1199 = Constraint(expr= - m.x243 - 2.5*m.x888 + 2.5*m.x924 <= 0)

m.c1200 = Constraint(expr= - m.x244 - 2.5*m.x889 + 2.5*m.x925 <= 0)

m.c1201 = Constraint(expr= - m.x245 - 2.5*m.x890 + 2.5*m.x926 <= 0)

m.c1202 = Constraint(expr= - m.x246 - 2.5*m.x891 + 2.5*m.x927 <= 0)

m.c1203 = Constraint(expr= - m.x247 - 2.5*m.x892 + 2.5*m.x928 <= 0)

m.c1204 = Constraint(expr= - m.x248 - 2.5*m.x893 + 2.5*m.x929 <= 0)

m.c1205 = Constraint(expr= - m.x249 - 2.5*m.x894 + 2.5*m.x930 <= 0)

m.c1206 = Constraint(expr= - m.x250 - 2.5*m.x895 + 2.5*m.x931 <= 0)

m.c1207 = Constraint(expr= - m.x251 - 2.5*m.x896 + 2.5*m.x932 <= 0)

m.c1208 = Constraint(expr= - m.x252 - 2.5*m.x897 + 2.5*m.x933 <= 0)

m.c1209 = Constraint(expr=   m.x217 + 5*m.x862 - 5*m.x898 <= 0)

m.c1210 = Constraint(expr=   m.x218 + 5*m.x863 - 5*m.x899 <= 0)

m.c1211 = Constraint(expr=   m.x219 + 5*m.x864 - 5*m.x900 <= 0)

m.c1212 = Constraint(expr=   m.x220 + 5*m.x865 - 5*m.x901 <= 0)

m.c1213 = Constraint(expr=   m.x221 + 5*m.x866 - 5*m.x902 <= 0)

m.c1214 = Constraint(expr=   m.x222 + 5*m.x867 - 5*m.x903 <= 0)

m.c1215 = Constraint(expr=   m.x223 + 5*m.x868 - 5*m.x904 <= 0)

m.c1216 = Constraint(expr=   m.x224 + 5*m.x869 - 5*m.x905 <= 0)

m.c1217 = Constraint(expr=   m.x225 + 5*m.x870 - 5*m.x906 <= 0)

m.c1218 = Constraint(expr=   m.x226 + 5*m.x871 - 5*m.x907 <= 0)

m.c1219 = Constraint(expr=   m.x227 + 5*m.x872 - 5*m.x908 <= 0)

m.c1220 = Constraint(expr=   m.x228 + 5*m.x873 - 5*m.x909 <= 0)

m.c1221 = Constraint(expr=   m.x229 + 5*m.x874 - 5*m.x910 <= 0)

m.c1222 = Constraint(expr=   m.x230 + 5*m.x875 - 5*m.x911 <= 0)

m.c1223 = Constraint(expr=   m.x231 + 5*m.x876 - 5*m.x912 <= 0)

m.c1224 = Constraint(expr=   m.x232 + 5*m.x877 - 5*m.x913 <= 0)

m.c1225 = Constraint(expr=   m.x233 + 5*m.x878 - 5*m.x914 <= 0)

m.c1226 = Constraint(expr=   m.x234 + 5*m.x879 - 5*m.x915 <= 0)

m.c1227 = Constraint(expr=   m.x235 + 5*m.x880 - 5*m.x916 <= 0)

m.c1228 = Constraint(expr=   m.x236 + 5*m.x881 - 5*m.x917 <= 0)

m.c1229 = Constraint(expr=   m.x237 + 5*m.x882 - 5*m.x918 <= 0)

m.c1230 = Constraint(expr=   m.x238 + 5*m.x883 - 5*m.x919 <= 0)

m.c1231 = Constraint(expr=   m.x239 + 5*m.x884 - 5*m.x920 <= 0)

m.c1232 = Constraint(expr=   m.x240 + 5*m.x885 - 5*m.x921 <= 0)

m.c1233 = Constraint(expr=   m.x241 + 5*m.x886 - 5*m.x922 <= 0)

m.c1234 = Constraint(expr=   m.x242 + 5*m.x887 - 5*m.x923 <= 0)

m.c1235 = Constraint(expr=   m.x243 + 5*m.x888 - 5*m.x924 <= 0)

m.c1236 = Constraint(expr=   m.x244 + 5*m.x889 - 5*m.x925 <= 0)

m.c1237 = Constraint(expr=   m.x245 + 5*m.x890 - 5*m.x926 <= 0)

m.c1238 = Constraint(expr=   m.x246 + 5*m.x891 - 5*m.x927 <= 0)

m.c1239 = Constraint(expr=   m.x247 + 5*m.x892 - 5*m.x928 <= 0)

m.c1240 = Constraint(expr=   m.x248 + 5*m.x893 - 5*m.x929 <= 0)

m.c1241 = Constraint(expr=   m.x249 + 5*m.x894 - 5*m.x930 <= 0)

m.c1242 = Constraint(expr=   m.x250 + 5*m.x895 - 5*m.x931 <= 0)

m.c1243 = Constraint(expr=   m.x251 + 5*m.x896 - 5*m.x932 <= 0)

m.c1244 = Constraint(expr=   m.x252 + 5*m.x897 - 5*m.x933 <= 0)

m.c1245 = Constraint(expr= - 340*m.b181 + m.x217 <= 0)

m.c1246 = Constraint(expr= - 510*m.b182 + m.x218 <= 0)

m.c1247 = Constraint(expr= - 510*m.b183 + m.x219 <= 0)

m.c1248 = Constraint(expr= - 340*m.b184 + m.x220 <= 0)

m.c1249 = Constraint(expr= - 510*m.b185 + m.x221 <= 0)

m.c1250 = Constraint(expr= - 510*m.b186 + m.x222 <= 0)

m.c1251 = Constraint(expr= - 340*m.b187 + m.x223 <= 0)

m.c1252 = Constraint(expr= - 510*m.b188 + m.x224 <= 0)

m.c1253 = Constraint(expr= - 510*m.b189 + m.x225 <= 0)

m.c1254 = Constraint(expr= - 290*m.b190 + m.x226 <= 0)

m.c1255 = Constraint(expr= - 510*m.b191 + m.x227 <= 0)

m.c1256 = Constraint(expr= - 510*m.b192 + m.x228 <= 0)

m.c1257 = Constraint(expr= - 290*m.b193 + m.x229 <= 0)

m.c1258 = Constraint(expr= - 510*m.b194 + m.x230 <= 0)

m.c1259 = Constraint(expr= - 510*m.b195 + m.x231 <= 0)

m.c1260 = Constraint(expr= - 840*m.b196 + m.x232 <= 0)

m.c1261 = Constraint(expr= - 870*m.b197 + m.x233 <= 0)

m.c1262 = Constraint(expr= - 870*m.b198 + m.x234 <= 0)

m.c1263 = Constraint(expr= - 840*m.b199 + m.x235 <= 0)

m.c1264 = Constraint(expr= - 870*m.b200 + m.x236 <= 0)

m.c1265 = Constraint(expr= - 870*m.b201 + m.x237 <= 0)

m.c1266 = Constraint(expr= - 190*m.b202 + m.x238 <= 0)

m.c1267 = Constraint(expr= - 870*m.b203 + m.x239 <= 0)

m.c1268 = Constraint(expr= - 870*m.b204 + m.x240 <= 0)

m.c1269 = Constraint(expr= - 190*m.b205 + m.x241 <= 0)

m.c1270 = Constraint(expr= - 870*m.b206 + m.x242 <= 0)

m.c1271 = Constraint(expr= - 870*m.b207 + m.x243 <= 0)

m.c1272 = Constraint(expr= - 20*m.b208 + m.x244 <= 0)

m.c1273 = Constraint(expr= - 510*m.b209 + m.x245 <= 0)

m.c1274 = Constraint(expr= - 510*m.b210 + m.x246 <= 0)

m.c1275 = Constraint(expr= - 20*m.b211 + m.x247 <= 0)

m.c1276 = Constraint(expr= - 510*m.b212 + m.x248 <= 0)

m.c1277 = Constraint(expr= - 510*m.b213 + m.x249 <= 0)

m.c1278 = Constraint(expr= - 390*m.b214 + m.x250 <= 0)

m.c1279 = Constraint(expr= - 920*m.b215 + m.x251 <= 0)

m.c1280 = Constraint(expr= - 920*m.b216 + m.x252 <= 0)

m.c1281 = Constraint(expr=   m.x217 - m.x253 - m.x256 - m.x259 - m.x262 == 0)

m.c1282 = Constraint(expr=   m.x218 - m.x254 - m.x257 - m.x260 - m.x263 == 0)

m.c1283 = Constraint(expr=   m.x219 - m.x255 - m.x258 - m.x261 - m.x264 == 0)

m.c1284 = Constraint(expr=   m.x220 - m.x265 - m.x268 - m.x271 - m.x274 == 0)

m.c1285 = Constraint(expr=   m.x221 - m.x266 - m.x269 - m.x272 - m.x275 == 0)

m.c1286 = Constraint(expr=   m.x222 - m.x267 - m.x270 - m.x273 - m.x276 == 0)

m.c1287 = Constraint(expr=   m.x223 - m.x277 - m.x280 - m.x283 - m.x286 == 0)

m.c1288 = Constraint(expr=   m.x224 - m.x278 - m.x281 - m.x284 - m.x287 == 0)

m.c1289 = Constraint(expr=   m.x225 - m.x279 - m.x282 - m.x285 - m.x288 == 0)

m.c1290 = Constraint(expr=   m.x226 - m.x289 - m.x292 - m.x295 - m.x298 == 0)

m.c1291 = Constraint(expr=   m.x227 - m.x290 - m.x293 - m.x296 - m.x299 == 0)

m.c1292 = Constraint(expr=   m.x228 - m.x291 - m.x294 - m.x297 - m.x300 == 0)

m.c1293 = Constraint(expr=   m.x229 - m.x301 - m.x304 - m.x307 - m.x310 == 0)

m.c1294 = Constraint(expr=   m.x230 - m.x302 - m.x305 - m.x308 - m.x311 == 0)

m.c1295 = Constraint(expr=   m.x231 - m.x303 - m.x306 - m.x309 - m.x312 == 0)

m.c1296 = Constraint(expr=   m.x232 - m.x313 - m.x316 - m.x319 - m.x322 == 0)

m.c1297 = Constraint(expr=   m.x233 - m.x314 - m.x317 - m.x320 - m.x323 == 0)

m.c1298 = Constraint(expr=   m.x234 - m.x315 - m.x318 - m.x321 - m.x324 == 0)

m.c1299 = Constraint(expr=   m.x235 - m.x325 - m.x328 - m.x331 - m.x334 == 0)

m.c1300 = Constraint(expr=   m.x236 - m.x326 - m.x329 - m.x332 - m.x335 == 0)

m.c1301 = Constraint(expr=   m.x237 - m.x327 - m.x330 - m.x333 - m.x336 == 0)

m.c1302 = Constraint(expr=   m.x238 - m.x337 - m.x340 - m.x343 - m.x346 == 0)

m.c1303 = Constraint(expr=   m.x239 - m.x338 - m.x341 - m.x344 - m.x347 == 0)

m.c1304 = Constraint(expr=   m.x240 - m.x339 - m.x342 - m.x345 - m.x348 == 0)

m.c1305 = Constraint(expr=   m.x241 - m.x349 - m.x352 - m.x355 - m.x358 == 0)

m.c1306 = Constraint(expr=   m.x242 - m.x350 - m.x353 - m.x356 - m.x359 == 0)

m.c1307 = Constraint(expr=   m.x243 - m.x351 - m.x354 - m.x357 - m.x360 == 0)

m.c1308 = Constraint(expr=   m.x244 - m.x361 - m.x364 - m.x367 - m.x370 == 0)

m.c1309 = Constraint(expr=   m.x245 - m.x362 - m.x365 - m.x368 - m.x371 == 0)

m.c1310 = Constraint(expr=   m.x246 - m.x363 - m.x366 - m.x369 - m.x372 == 0)

m.c1311 = Constraint(expr=   m.x247 - m.x373 - m.x376 - m.x379 - m.x382 == 0)

m.c1312 = Constraint(expr=   m.x248 - m.x374 - m.x377 - m.x380 - m.x383 == 0)

m.c1313 = Constraint(expr=   m.x249 - m.x375 - m.x378 - m.x381 - m.x384 == 0)

m.c1314 = Constraint(expr=   m.x250 - m.x385 - m.x388 - m.x391 - m.x394 == 0)

m.c1315 = Constraint(expr=   m.x251 - m.x386 - m.x389 - m.x392 - m.x395 == 0)

m.c1316 = Constraint(expr=   m.x252 - m.x387 - m.x390 - m.x393 - m.x396 == 0)

m.c1317 = Constraint(expr= - m.x220 - m.x226 - m.x232 - m.x238 + m.x397 == 0)

m.c1318 = Constraint(expr= - m.x221 - m.x227 - m.x233 - m.x239 + m.x398 == 0)

m.c1319 = Constraint(expr= - m.x222 - m.x228 - m.x234 - m.x240 + m.x399 == 0)

m.c1320 = Constraint(expr= - m.x223 - m.x229 - m.x235 - m.x241 + m.x400 == 0)

m.c1321 = Constraint(expr= - m.x224 - m.x230 - m.x236 - m.x242 + m.x401 == 0)

m.c1322 = Constraint(expr= - m.x225 - m.x231 - m.x237 - m.x243 + m.x402 == 0)

m.c1323 = Constraint(expr= - m.x217 - m.x244 - m.x247 - m.x250 + m.x403 == 0)

m.c1324 = Constraint(expr= - m.x218 - m.x245 - m.x248 - m.x251 + m.x404 == 0)

m.c1325 = Constraint(expr= - m.x219 - m.x246 - m.x249 - m.x252 + m.x405 == 0)

m.c1326 = Constraint(expr= - m.x397 - 2.5*m.x934 + 2.5*m.x943 <= 0)

m.c1327 = Constraint(expr= - m.x398 - 2.5*m.x935 + 2.5*m.x944 <= 0)

m.c1328 = Constraint(expr= - m.x399 - 2.5*m.x936 + 2.5*m.x945 <= 0)

m.c1329 = Constraint(expr= - m.x400 - 2.5*m.x937 + 2.5*m.x946 <= 0)

m.c1330 = Constraint(expr= - m.x401 - 2.5*m.x938 + 2.5*m.x947 <= 0)

m.c1331 = Constraint(expr= - m.x402 - 2.5*m.x939 + 2.5*m.x948 <= 0)

m.c1332 = Constraint(expr= - m.x403 - 2.5*m.x940 + 2.5*m.x949 <= 0)

m.c1333 = Constraint(expr= - m.x404 - 2.5*m.x941 + 2.5*m.x950 <= 0)

m.c1334 = Constraint(expr= - m.x405 - 2.5*m.x942 + 2.5*m.x951 <= 0)

m.c1335 = Constraint(expr=   m.x397 + 5*m.x934 - 5*m.x943 <= 0)

m.c1336 = Constraint(expr=   m.x398 + 5*m.x935 - 5*m.x944 <= 0)

m.c1337 = Constraint(expr=   m.x399 + 5*m.x936 - 5*m.x945 <= 0)

m.c1338 = Constraint(expr=   m.x400 + 5*m.x937 - 5*m.x946 <= 0)

m.c1339 = Constraint(expr=   m.x401 + 5*m.x938 - 5*m.x947 <= 0)

m.c1340 = Constraint(expr=   m.x402 + 5*m.x939 - 5*m.x948 <= 0)

m.c1341 = Constraint(expr=   m.x403 + 5*m.x940 - 5*m.x949 <= 0)

m.c1342 = Constraint(expr=   m.x404 + 5*m.x941 - 5*m.x950 <= 0)

m.c1343 = Constraint(expr=   m.x405 + 5*m.x942 - 5*m.x951 <= 0)

m.c1344 = Constraint(expr= - m.x265 - m.x289 - m.x313 - m.x337 + 0.1*m.x397 <= 0)

m.c1345 = Constraint(expr= - m.x266 - m.x290 - m.x314 - m.x338 + 0.1*m.x398 <= 0)

m.c1346 = Constraint(expr= - m.x267 - m.x291 - m.x315 - m.x339 + 0.1*m.x399 <= 0)

m.c1347 = Constraint(expr= - m.x268 - m.x292 - m.x316 - m.x340 + 0.1*m.x397 <= 0)

m.c1348 = Constraint(expr= - m.x269 - m.x293 - m.x317 - m.x341 + 0.1*m.x398 <= 0)

m.c1349 = Constraint(expr= - m.x270 - m.x294 - m.x318 - m.x342 + 0.1*m.x399 <= 0)

m.c1350 = Constraint(expr= - m.x271 - m.x295 - m.x319 - m.x343 + 0.1*m.x397 <= 0)

m.c1351 = Constraint(expr= - m.x272 - m.x296 - m.x320 - m.x344 + 0.1*m.x398 <= 0)

m.c1352 = Constraint(expr= - m.x273 - m.x297 - m.x321 - m.x345 + 0.1*m.x399 <= 0)

m.c1353 = Constraint(expr= - m.x274 - m.x298 - m.x322 - m.x346 + 0.1*m.x397 <= 0)

m.c1354 = Constraint(expr= - m.x275 - m.x299 - m.x323 - m.x347 + 0.1*m.x398 <= 0)

m.c1355 = Constraint(expr= - m.x276 - m.x300 - m.x324 - m.x348 + 0.1*m.x399 <= 0)

m.c1356 = Constraint(expr= - m.x277 - m.x301 - m.x325 - m.x349 + 0.1*m.x400 <= 0)

m.c1357 = Constraint(expr= - m.x278 - m.x302 - m.x326 - m.x350 + 0.1*m.x401 <= 0)

m.c1358 = Constraint(expr= - m.x279 - m.x303 - m.x327 - m.x351 + 0.1*m.x402 <= 0)

m.c1359 = Constraint(expr= - m.x280 - m.x304 - m.x328 - m.x352 + 0.1*m.x400 <= 0)

m.c1360 = Constraint(expr= - m.x281 - m.x305 - m.x329 - m.x353 + 0.1*m.x401 <= 0)

m.c1361 = Constraint(expr= - m.x282 - m.x306 - m.x330 - m.x354 + 0.1*m.x402 <= 0)

m.c1362 = Constraint(expr= - m.x283 - m.x307 - m.x331 - m.x355 + 0.1*m.x400 <= 0)

m.c1363 = Constraint(expr= - m.x284 - m.x308 - m.x332 - m.x356 + 0.1*m.x401 <= 0)

m.c1364 = Constraint(expr= - m.x285 - m.x309 - m.x333 - m.x357 + 0.1*m.x402 <= 0)

m.c1365 = Constraint(expr= - m.x286 - m.x310 - m.x334 - m.x358 + 0.1*m.x400 <= 0)

m.c1366 = Constraint(expr= - m.x287 - m.x311 - m.x335 - m.x359 + 0.1*m.x401 <= 0)

m.c1367 = Constraint(expr= - m.x288 - m.x312 - m.x336 - m.x360 + 0.1*m.x402 <= 0)

m.c1368 = Constraint(expr= - m.x253 - m.x361 - m.x373 - m.x385 + 0.1*m.x403 <= 0)

m.c1369 = Constraint(expr= - m.x254 - m.x362 - m.x374 - m.x386 + 0.1*m.x404 <= 0)

m.c1370 = Constraint(expr= - m.x255 - m.x363 - m.x375 - m.x387 + 0.1*m.x405 <= 0)

m.c1371 = Constraint(expr= - m.x256 - m.x364 - m.x376 - m.x388 + 0.1*m.x403 <= 0)

m.c1372 = Constraint(expr= - m.x257 - m.x365 - m.x377 - m.x389 + 0.1*m.x404 <= 0)

m.c1373 = Constraint(expr= - m.x258 - m.x366 - m.x378 - m.x390 + 0.1*m.x405 <= 0)

m.c1374 = Constraint(expr= - m.x259 - m.x367 - m.x379 - m.x391 + 0.1*m.x403 <= 0)

m.c1375 = Constraint(expr= - m.x260 - m.x368 - m.x380 - m.x392 + 0.1*m.x404 <= 0)

m.c1376 = Constraint(expr= - m.x261 - m.x369 - m.x381 - m.x393 + 0.1*m.x405 <= 0)

m.c1377 = Constraint(expr= - m.x262 - m.x370 - m.x382 - m.x394 + 0.1*m.x403 <= 0)

m.c1378 = Constraint(expr= - m.x263 - m.x371 - m.x383 - m.x395 + 0.1*m.x404 <= 0)

m.c1379 = Constraint(expr= - m.x264 - m.x372 - m.x384 - m.x396 + 0.1*m.x405 <= 0)

m.c1380 = Constraint(expr=   m.x265 + m.x289 + m.x313 + m.x337 - 0.9*m.x397 <= 0)

m.c1381 = Constraint(expr=   m.x266 + m.x290 + m.x314 + m.x338 - 0.9*m.x398 <= 0)

m.c1382 = Constraint(expr=   m.x267 + m.x291 + m.x315 + m.x339 - 0.9*m.x399 <= 0)

m.c1383 = Constraint(expr=   m.x268 + m.x292 + m.x316 + m.x340 - 0.9*m.x397 <= 0)

m.c1384 = Constraint(expr=   m.x269 + m.x293 + m.x317 + m.x341 - 0.9*m.x398 <= 0)

m.c1385 = Constraint(expr=   m.x270 + m.x294 + m.x318 + m.x342 - 0.9*m.x399 <= 0)

m.c1386 = Constraint(expr=   m.x271 + m.x295 + m.x319 + m.x343 - 0.9*m.x397 <= 0)

m.c1387 = Constraint(expr=   m.x272 + m.x296 + m.x320 + m.x344 - 0.9*m.x398 <= 0)

m.c1388 = Constraint(expr=   m.x273 + m.x297 + m.x321 + m.x345 - 0.9*m.x399 <= 0)

m.c1389 = Constraint(expr=   m.x274 + m.x298 + m.x322 + m.x346 - 0.9*m.x397 <= 0)

m.c1390 = Constraint(expr=   m.x275 + m.x299 + m.x323 + m.x347 - 0.9*m.x398 <= 0)

m.c1391 = Constraint(expr=   m.x276 + m.x300 + m.x324 + m.x348 - 0.9*m.x399 <= 0)

m.c1392 = Constraint(expr=   m.x277 + m.x301 + m.x325 + m.x349 - 0.9*m.x400 <= 0)

m.c1393 = Constraint(expr=   m.x278 + m.x302 + m.x326 + m.x350 - 0.9*m.x401 <= 0)

m.c1394 = Constraint(expr=   m.x279 + m.x303 + m.x327 + m.x351 - 0.9*m.x402 <= 0)

m.c1395 = Constraint(expr=   m.x280 + m.x304 + m.x328 + m.x352 - 0.9*m.x400 <= 0)

m.c1396 = Constraint(expr=   m.x281 + m.x305 + m.x329 + m.x353 - 0.9*m.x401 <= 0)

m.c1397 = Constraint(expr=   m.x282 + m.x306 + m.x330 + m.x354 - 0.9*m.x402 <= 0)

m.c1398 = Constraint(expr=   m.x283 + m.x307 + m.x331 + m.x355 - 0.9*m.x400 <= 0)

m.c1399 = Constraint(expr=   m.x284 + m.x308 + m.x332 + m.x356 - 0.9*m.x401 <= 0)

m.c1400 = Constraint(expr=   m.x285 + m.x309 + m.x333 + m.x357 - 0.9*m.x402 <= 0)

m.c1401 = Constraint(expr=   m.x286 + m.x310 + m.x334 + m.x358 - 0.9*m.x400 <= 0)

m.c1402 = Constraint(expr=   m.x287 + m.x311 + m.x335 + m.x359 - 0.9*m.x401 <= 0)

m.c1403 = Constraint(expr=   m.x288 + m.x312 + m.x336 + m.x360 - 0.9*m.x402 <= 0)

m.c1404 = Constraint(expr=   m.x253 + m.x361 + m.x373 + m.x385 - 0.9*m.x403 <= 0)

m.c1405 = Constraint(expr=   m.x254 + m.x362 + m.x374 + m.x386 - 0.9*m.x404 <= 0)

m.c1406 = Constraint(expr=   m.x255 + m.x363 + m.x375 + m.x387 - 0.9*m.x405 <= 0)

m.c1407 = Constraint(expr=   m.x256 + m.x364 + m.x376 + m.x388 - 0.9*m.x403 <= 0)

m.c1408 = Constraint(expr=   m.x257 + m.x365 + m.x377 + m.x389 - 0.9*m.x404 <= 0)

m.c1409 = Constraint(expr=   m.x258 + m.x366 + m.x378 + m.x390 - 0.9*m.x405 <= 0)

m.c1410 = Constraint(expr=   m.x259 + m.x367 + m.x379 + m.x391 - 0.9*m.x403 <= 0)

m.c1411 = Constraint(expr=   m.x260 + m.x368 + m.x380 + m.x392 - 0.9*m.x404 <= 0)

m.c1412 = Constraint(expr=   m.x261 + m.x369 + m.x381 + m.x393 - 0.9*m.x405 <= 0)

m.c1413 = Constraint(expr=   m.x262 + m.x370 + m.x382 + m.x394 - 0.9*m.x403 <= 0)

m.c1414 = Constraint(expr=   m.x263 + m.x371 + m.x383 + m.x395 - 0.9*m.x404 <= 0)

m.c1415 = Constraint(expr=   m.x264 + m.x372 + m.x384 + m.x396 - 0.9*m.x405 <= 0)

m.c1416 = Constraint(expr=   0.001*m.x220 + 0.001*m.x226 + 0.001*m.x232 + 0.001*m.x238 - 0.012*m.x265 - 0.013*m.x268
                           - 0.009*m.x271 - 0.015*m.x274 - 0.012*m.x289 - 0.013*m.x292 - 0.009*m.x295 - 0.015*m.x298
                           - 0.012*m.x313 - 0.013*m.x316 - 0.009*m.x319 - 0.015*m.x322 - 0.012*m.x337 - 0.013*m.x340
                           - 0.009*m.x343 - 0.015*m.x346 <= 0)

m.c1417 = Constraint(expr=   0.001*m.x221 + 0.001*m.x227 + 0.001*m.x233 + 0.001*m.x239 - 0.012*m.x266 - 0.013*m.x269
                           - 0.009*m.x272 - 0.015*m.x275 - 0.012*m.x290 - 0.013*m.x293 - 0.009*m.x296 - 0.015*m.x299
                           - 0.012*m.x314 - 0.013*m.x317 - 0.009*m.x320 - 0.015*m.x323 - 0.012*m.x338 - 0.013*m.x341
                           - 0.009*m.x344 - 0.015*m.x347 <= 0)

m.c1418 = Constraint(expr=   0.001*m.x222 + 0.001*m.x228 + 0.001*m.x234 + 0.001*m.x240 - 0.012*m.x267 - 0.013*m.x270
                           - 0.009*m.x273 - 0.015*m.x276 - 0.012*m.x291 - 0.013*m.x294 - 0.009*m.x297 - 0.015*m.x300
                           - 0.012*m.x315 - 0.013*m.x318 - 0.009*m.x321 - 0.015*m.x324 - 0.012*m.x339 - 0.013*m.x342
                           - 0.009*m.x345 - 0.015*m.x348 <= 0)

m.c1419 = Constraint(expr=   0.001*m.x223 + 0.001*m.x229 + 0.001*m.x235 + 0.001*m.x241 - 0.012*m.x277 - 0.013*m.x280
                           - 0.009*m.x283 - 0.015*m.x286 - 0.012*m.x301 - 0.013*m.x304 - 0.009*m.x307 - 0.015*m.x310
                           - 0.012*m.x325 - 0.013*m.x328 - 0.009*m.x331 - 0.015*m.x334 - 0.012*m.x349 - 0.013*m.x352
                           - 0.009*m.x355 - 0.015*m.x358 <= 0)

m.c1420 = Constraint(expr=   0.001*m.x224 + 0.001*m.x230 + 0.001*m.x236 + 0.001*m.x242 - 0.012*m.x278 - 0.013*m.x281
                           - 0.009*m.x284 - 0.015*m.x287 - 0.012*m.x302 - 0.013*m.x305 - 0.009*m.x308 - 0.015*m.x311
                           - 0.012*m.x326 - 0.013*m.x329 - 0.009*m.x332 - 0.015*m.x335 - 0.012*m.x350 - 0.013*m.x353
                           - 0.009*m.x356 - 0.015*m.x359 <= 0)

m.c1421 = Constraint(expr=   0.001*m.x225 + 0.001*m.x231 + 0.001*m.x237 + 0.001*m.x243 - 0.012*m.x279 - 0.013*m.x282
                           - 0.009*m.x285 - 0.015*m.x288 - 0.012*m.x303 - 0.013*m.x306 - 0.009*m.x309 - 0.015*m.x312
                           - 0.012*m.x327 - 0.013*m.x330 - 0.009*m.x333 - 0.015*m.x336 - 0.012*m.x351 - 0.013*m.x354
                           - 0.009*m.x357 - 0.015*m.x360 <= 0)

m.c1422 = Constraint(expr=   0.001*m.x217 + 0.001*m.x244 + 0.001*m.x247 + 0.001*m.x250 - 0.002*m.x253 - 0.0025*m.x256
                           - 0.0015*m.x259 - 0.006*m.x262 - 0.002*m.x361 - 0.0025*m.x364 - 0.0015*m.x367 - 0.006*m.x370
                           - 0.002*m.x373 - 0.0025*m.x376 - 0.0015*m.x379 - 0.006*m.x382 - 0.002*m.x385 - 0.0025*m.x388
                           - 0.0015*m.x391 - 0.006*m.x394 <= 0)

m.c1423 = Constraint(expr=   0.001*m.x218 + 0.001*m.x245 + 0.001*m.x248 + 0.001*m.x251 - 0.002*m.x254 - 0.0025*m.x257
                           - 0.0015*m.x260 - 0.006*m.x263 - 0.002*m.x362 - 0.0025*m.x365 - 0.0015*m.x368 - 0.006*m.x371
                           - 0.002*m.x374 - 0.0025*m.x377 - 0.0015*m.x380 - 0.006*m.x383 - 0.002*m.x386 - 0.0025*m.x389
                           - 0.0015*m.x392 - 0.006*m.x395 <= 0)

m.c1424 = Constraint(expr=   0.001*m.x219 + 0.001*m.x246 + 0.001*m.x249 + 0.001*m.x252 - 0.002*m.x255 - 0.0025*m.x258
                           - 0.0015*m.x261 - 0.006*m.x264 - 0.002*m.x363 - 0.0025*m.x366 - 0.0015*m.x369 - 0.006*m.x372
                           - 0.002*m.x375 - 0.0025*m.x378 - 0.0015*m.x381 - 0.006*m.x384 - 0.002*m.x387 - 0.0025*m.x390
                           - 0.0015*m.x393 - 0.006*m.x396 <= 0)

m.c1425 = Constraint(expr= - 0.0135*m.x220 - 0.0135*m.x226 - 0.0135*m.x232 - 0.0135*m.x238 + 0.012*m.x265 + 0.013*m.x268
                           + 0.009*m.x271 + 0.015*m.x274 + 0.012*m.x289 + 0.013*m.x292 + 0.009*m.x295 + 0.015*m.x298
                           + 0.012*m.x313 + 0.013*m.x316 + 0.009*m.x319 + 0.015*m.x322 + 0.012*m.x337 + 0.013*m.x340
                           + 0.009*m.x343 + 0.015*m.x346 <= 0)

m.c1426 = Constraint(expr= - 0.0135*m.x221 - 0.0135*m.x227 - 0.0135*m.x233 - 0.0135*m.x239 + 0.012*m.x266 + 0.013*m.x269
                           + 0.009*m.x272 + 0.015*m.x275 + 0.012*m.x290 + 0.013*m.x293 + 0.009*m.x296 + 0.015*m.x299
                           + 0.012*m.x314 + 0.013*m.x317 + 0.009*m.x320 + 0.015*m.x323 + 0.012*m.x338 + 0.013*m.x341
                           + 0.009*m.x344 + 0.015*m.x347 <= 0)

m.c1427 = Constraint(expr= - 0.0135*m.x222 - 0.0135*m.x228 - 0.0135*m.x234 - 0.0135*m.x240 + 0.012*m.x267 + 0.013*m.x270
                           + 0.009*m.x273 + 0.015*m.x276 + 0.012*m.x291 + 0.013*m.x294 + 0.009*m.x297 + 0.015*m.x300
                           + 0.012*m.x315 + 0.013*m.x318 + 0.009*m.x321 + 0.015*m.x324 + 0.012*m.x339 + 0.013*m.x342
                           + 0.009*m.x345 + 0.015*m.x348 <= 0)

m.c1428 = Constraint(expr= - 0.013*m.x223 - 0.013*m.x229 - 0.013*m.x235 - 0.013*m.x241 + 0.012*m.x277 + 0.013*m.x280
                           + 0.009*m.x283 + 0.015*m.x286 + 0.012*m.x301 + 0.013*m.x304 + 0.009*m.x307 + 0.015*m.x310
                           + 0.012*m.x325 + 0.013*m.x328 + 0.009*m.x331 + 0.015*m.x334 + 0.012*m.x349 + 0.013*m.x352
                           + 0.009*m.x355 + 0.015*m.x358 <= 0)

m.c1429 = Constraint(expr= - 0.013*m.x224 - 0.013*m.x230 - 0.013*m.x236 - 0.013*m.x242 + 0.012*m.x278 + 0.013*m.x281
                           + 0.009*m.x284 + 0.015*m.x287 + 0.012*m.x302 + 0.013*m.x305 + 0.009*m.x308 + 0.015*m.x311
                           + 0.012*m.x326 + 0.013*m.x329 + 0.009*m.x332 + 0.015*m.x335 + 0.012*m.x350 + 0.013*m.x353
                           + 0.009*m.x356 + 0.015*m.x359 <= 0)

m.c1430 = Constraint(expr= - 0.013*m.x225 - 0.013*m.x231 - 0.013*m.x237 - 0.013*m.x243 + 0.012*m.x279 + 0.013*m.x282
                           + 0.009*m.x285 + 0.015*m.x288 + 0.012*m.x303 + 0.013*m.x306 + 0.009*m.x309 + 0.015*m.x312
                           + 0.012*m.x327 + 0.013*m.x330 + 0.009*m.x333 + 0.015*m.x336 + 0.012*m.x351 + 0.013*m.x354
                           + 0.009*m.x357 + 0.015*m.x360 <= 0)

m.c1431 = Constraint(expr= - 0.004*m.x217 - 0.004*m.x244 - 0.004*m.x247 - 0.004*m.x250 + 0.002*m.x253 + 0.0025*m.x256
                           + 0.0015*m.x259 + 0.006*m.x262 + 0.002*m.x361 + 0.0025*m.x364 + 0.0015*m.x367 + 0.006*m.x370
                           + 0.002*m.x373 + 0.0025*m.x376 + 0.0015*m.x379 + 0.006*m.x382 + 0.002*m.x385 + 0.0025*m.x388
                           + 0.0015*m.x391 + 0.006*m.x394 <= 0)

m.c1432 = Constraint(expr= - 0.004*m.x218 - 0.004*m.x245 - 0.004*m.x248 - 0.004*m.x251 + 0.002*m.x254 + 0.0025*m.x257
                           + 0.0015*m.x260 + 0.006*m.x263 + 0.002*m.x362 + 0.0025*m.x365 + 0.0015*m.x368 + 0.006*m.x371
                           + 0.002*m.x374 + 0.0025*m.x377 + 0.0015*m.x380 + 0.006*m.x383 + 0.002*m.x386 + 0.0025*m.x389
                           + 0.0015*m.x392 + 0.006*m.x395 <= 0)

m.c1433 = Constraint(expr= - 0.004*m.x219 - 0.004*m.x246 - 0.004*m.x249 - 0.004*m.x252 + 0.002*m.x255 + 0.0025*m.x258
                           + 0.0015*m.x261 + 0.006*m.x264 + 0.002*m.x363 + 0.0025*m.x366 + 0.0015*m.x369 + 0.006*m.x372
                           + 0.002*m.x375 + 0.0025*m.x378 + 0.0015*m.x381 + 0.006*m.x384 + 0.002*m.x387 + 0.0025*m.x390
                           + 0.0015*m.x393 + 0.006*m.x396 <= 0)

m.c1434 = Constraint(expr=   m.x397 + m.x398 + m.x399 == 1000)

m.c1435 = Constraint(expr=   m.x400 + m.x401 + m.x402 == 1000)

m.c1436 = Constraint(expr=   m.x403 + m.x404 + m.x405 == 1000)

m.c1437 = Constraint(expr=   m.x575 - m.x718 >= 0)

m.c1438 = Constraint(expr=   m.x576 - m.x719 >= 0)

m.c1439 = Constraint(expr=   m.x578 - m.x721 >= 0)

m.c1440 = Constraint(expr=   m.x579 - m.x722 >= 0)

m.c1441 = Constraint(expr=   m.x581 - m.x724 >= 0)

m.c1442 = Constraint(expr=   m.x582 - m.x725 >= 0)

m.c1443 = Constraint(expr=   m.x584 - m.x727 >= 0)

m.c1444 = Constraint(expr=   m.x585 - m.x728 >= 0)

m.c1445 = Constraint(expr=   m.x587 - m.x730 >= 0)

m.c1446 = Constraint(expr=   m.x588 - m.x731 >= 0)

m.c1447 = Constraint(expr=   m.x590 - m.x733 >= 0)

m.c1448 = Constraint(expr=   m.x591 - m.x734 >= 0)

m.c1449 = Constraint(expr=   m.x593 - m.x736 >= 0)

m.c1450 = Constraint(expr=   m.x594 - m.x737 >= 0)

m.c1451 = Constraint(expr=   m.x596 - m.x739 >= 0)

m.c1452 = Constraint(expr=   m.x597 - m.x740 >= 0)

m.c1453 = Constraint(expr=   m.x599 - m.x742 >= 0)

m.c1454 = Constraint(expr=   m.x600 - m.x743 >= 0)

m.c1455 = Constraint(expr=   m.x602 - m.x745 >= 0)

m.c1456 = Constraint(expr=   m.x603 - m.x746 >= 0)

m.c1457 = Constraint(expr=   m.x605 - m.x748 >= 0)

m.c1458 = Constraint(expr=   m.x606 - m.x749 >= 0)

m.c1459 = Constraint(expr=   m.x608 - m.x751 >= 0)

m.c1460 = Constraint(expr=   m.x609 - m.x752 >= 0)

m.c1461 = Constraint(expr=   m.x611 - m.x754 >= 0)

m.c1462 = Constraint(expr=   m.x612 - m.x755 >= 0)

m.c1463 = Constraint(expr=   m.x614 - m.x757 >= 0)

m.c1464 = Constraint(expr=   m.x615 - m.x758 >= 0)

m.c1465 = Constraint(expr=   m.x617 - m.x760 >= 0)

m.c1466 = Constraint(expr=   m.x618 - m.x761 >= 0)

m.c1467 = Constraint(expr=   m.x620 - m.x763 >= 0)

m.c1468 = Constraint(expr=   m.x621 - m.x764 >= 0)

m.c1469 = Constraint(expr=   m.x623 - m.x766 >= 0)

m.c1470 = Constraint(expr=   m.x624 - m.x767 >= 0)

m.c1471 = Constraint(expr=   m.x626 - m.x769 >= 0)

m.c1472 = Constraint(expr=   m.x627 - m.x770 >= 0)

m.c1473 = Constraint(expr=   m.x629 - m.x772 >= 0)

m.c1474 = Constraint(expr=   m.x630 - m.x773 >= 0)

m.c1475 = Constraint(expr=   m.x632 - m.x775 >= 0)

m.c1476 = Constraint(expr=   m.x633 - m.x776 >= 0)

m.c1477 = Constraint(expr=   m.x635 - m.x778 >= 0)

m.c1478 = Constraint(expr=   m.x636 - m.x779 >= 0)

m.c1479 = Constraint(expr=   m.x638 - m.x781 >= 0)

m.c1480 = Constraint(expr=   m.x639 - m.x782 >= 0)

m.c1481 = Constraint(expr=   m.x641 - m.x784 >= 0)

m.c1482 = Constraint(expr=   m.x642 - m.x785 >= 0)

m.c1483 = Constraint(expr=   m.x644 - m.x787 >= 0)

m.c1484 = Constraint(expr=   m.x645 - m.x788 >= 0)

m.c1485 = Constraint(expr=   m.x647 - m.x790 >= 0)

m.c1486 = Constraint(expr=   m.x648 - m.x791 >= 0)

m.c1487 = Constraint(expr=   m.x650 - m.x793 >= 0)

m.c1488 = Constraint(expr=   m.x651 - m.x794 >= 0)

m.c1489 = Constraint(expr=   m.x653 - m.x796 >= 0)

m.c1490 = Constraint(expr=   m.x654 - m.x797 >= 0)

m.c1491 = Constraint(expr=   m.x656 - m.x799 >= 0)

m.c1492 = Constraint(expr=   m.x657 - m.x800 >= 0)

m.c1493 = Constraint(expr=   m.x659 - m.x802 >= 0)

m.c1494 = Constraint(expr=   m.x660 - m.x803 >= 0)

m.c1495 = Constraint(expr=   m.x662 - m.x805 >= 0)

m.c1496 = Constraint(expr=   m.x663 - m.x806 >= 0)

m.c1497 = Constraint(expr=   m.x665 - m.x808 >= 0)

m.c1498 = Constraint(expr=   m.x666 - m.x809 >= 0)

m.c1499 = Constraint(expr=   m.x668 - m.x811 >= 0)

m.c1500 = Constraint(expr=   m.x669 - m.x812 >= 0)

m.c1501 = Constraint(expr=   m.x671 - m.x814 >= 0)

m.c1502 = Constraint(expr=   m.x672 - m.x815 >= 0)

m.c1503 = Constraint(expr=   m.x674 - m.x817 >= 0)

m.c1504 = Constraint(expr=   m.x675 - m.x818 >= 0)

m.c1505 = Constraint(expr=   m.x677 - m.x820 >= 0)

m.c1506 = Constraint(expr=   m.x678 - m.x821 >= 0)

m.c1507 = Constraint(expr=   m.x680 - m.x823 >= 0)

m.c1508 = Constraint(expr=   m.x681 - m.x824 >= 0)

m.c1509 = Constraint(expr=   m.x683 - m.x826 >= 0)

m.c1510 = Constraint(expr=   m.x684 - m.x827 >= 0)

m.c1511 = Constraint(expr=   m.x686 - m.x829 >= 0)

m.c1512 = Constraint(expr=   m.x687 - m.x830 >= 0)

m.c1513 = Constraint(expr=   m.x689 - m.x832 >= 0)

m.c1514 = Constraint(expr=   m.x690 - m.x833 >= 0)

m.c1515 = Constraint(expr=   m.x692 - m.x835 >= 0)

m.c1516 = Constraint(expr=   m.x693 - m.x836 >= 0)

m.c1517 = Constraint(expr=   m.x695 - m.x838 >= 0)

m.c1518 = Constraint(expr=   m.x696 - m.x839 >= 0)

m.c1519 = Constraint(expr=   m.x698 - m.x841 >= 0)

m.c1520 = Constraint(expr=   m.x699 - m.x842 >= 0)

m.c1521 = Constraint(expr=   m.x701 - m.x844 >= 0)

m.c1522 = Constraint(expr=   m.x702 - m.x845 >= 0)

m.c1523 = Constraint(expr=   m.x704 - m.x847 >= 0)

m.c1524 = Constraint(expr=   m.x705 - m.x848 >= 0)

m.c1525 = Constraint(expr=   m.x707 - m.x850 >= 0)

m.c1526 = Constraint(expr=   m.x708 - m.x851 >= 0)

m.c1527 = Constraint(expr=   m.x710 - m.x853 >= 0)

m.c1528 = Constraint(expr=   m.x711 - m.x854 >= 0)

m.c1529 = Constraint(expr=   m.x713 - m.x856 >= 0)

m.c1530 = Constraint(expr=   m.x714 - m.x857 >= 0)

m.c1531 = Constraint(expr=   m.x716 - m.x859 >= 0)

m.c1532 = Constraint(expr=   m.x717 - m.x860 >= 0)

m.c1533 = Constraint(expr= - 336*m.b1 + m.x578 - m.x718 >= -336)

m.c1534 = Constraint(expr= - 336*m.b2 + m.x579 - m.x719 >= -336)

m.c1535 = Constraint(expr= - 336*m.b1 + m.x581 - m.x718 >= -336)

m.c1536 = Constraint(expr= - 336*m.b2 + m.x582 - m.x719 >= -336)

m.c1537 = Constraint(expr= - 336*m.b1 + m.x584 - m.x718 >= -336)

m.c1538 = Constraint(expr= - 336*m.b2 + m.x585 - m.x719 >= -336)

m.c1539 = Constraint(expr= - 336*m.b4 + m.x575 - m.x721 >= -336)

m.c1540 = Constraint(expr= - 336*m.b5 + m.x576 - m.x722 >= -336)

m.c1541 = Constraint(expr= - 336*m.b4 + m.x581 - m.x721 >= -336)

m.c1542 = Constraint(expr= - 336*m.b5 + m.x582 - m.x722 >= -336)

m.c1543 = Constraint(expr= - 336*m.b4 + m.x584 - m.x721 >= -336)

m.c1544 = Constraint(expr= - 336*m.b5 + m.x585 - m.x722 >= -336)

m.c1545 = Constraint(expr= - 336*m.b7 + m.x575 - m.x724 >= -336)

m.c1546 = Constraint(expr= - 336*m.b8 + m.x576 - m.x725 >= -336)

m.c1547 = Constraint(expr= - 336*m.b7 + m.x578 - m.x724 >= -336)

m.c1548 = Constraint(expr= - 336*m.b8 + m.x579 - m.x725 >= -336)

m.c1549 = Constraint(expr= - 336*m.b7 + m.x584 - m.x724 >= -336)

m.c1550 = Constraint(expr= - 336*m.b8 + m.x585 - m.x725 >= -336)

m.c1551 = Constraint(expr= - 336*m.b10 + m.x575 - m.x727 >= -336)

m.c1552 = Constraint(expr= - 336*m.b11 + m.x576 - m.x728 >= -336)

m.c1553 = Constraint(expr= - 336*m.b10 + m.x578 - m.x727 >= -336)

m.c1554 = Constraint(expr= - 336*m.b11 + m.x579 - m.x728 >= -336)

m.c1555 = Constraint(expr= - 336*m.b10 + m.x581 - m.x727 >= -336)

m.c1556 = Constraint(expr= - 336*m.b11 + m.x582 - m.x728 >= -336)

m.c1557 = Constraint(expr= - 336*m.b13 + m.x590 - m.x730 >= -336)

m.c1558 = Constraint(expr= - 336*m.b14 + m.x591 - m.x731 >= -336)

m.c1559 = Constraint(expr= - 336*m.b13 + m.x593 - m.x730 >= -336)

m.c1560 = Constraint(expr= - 336*m.b14 + m.x594 - m.x731 >= -336)

m.c1561 = Constraint(expr= - 336*m.b13 + m.x596 - m.x730 >= -336)

m.c1562 = Constraint(expr= - 336*m.b14 + m.x597 - m.x731 >= -336)

m.c1563 = Constraint(expr= - 336*m.b16 + m.x587 - m.x733 >= -336)

m.c1564 = Constraint(expr= - 336*m.b17 + m.x588 - m.x734 >= -336)

m.c1565 = Constraint(expr= - 336*m.b16 + m.x593 - m.x733 >= -336)

m.c1566 = Constraint(expr= - 336*m.b17 + m.x594 - m.x734 >= -336)

m.c1567 = Constraint(expr= - 336*m.b16 + m.x596 - m.x733 >= -336)

m.c1568 = Constraint(expr= - 336*m.b17 + m.x597 - m.x734 >= -336)

m.c1569 = Constraint(expr= - 336*m.b19 + m.x587 - m.x736 >= -336)

m.c1570 = Constraint(expr= - 336*m.b20 + m.x588 - m.x737 >= -336)

m.c1571 = Constraint(expr= - 336*m.b19 + m.x590 - m.x736 >= -336)

m.c1572 = Constraint(expr= - 336*m.b20 + m.x591 - m.x737 >= -336)

m.c1573 = Constraint(expr= - 336*m.b19 + m.x596 - m.x736 >= -336)

m.c1574 = Constraint(expr= - 336*m.b20 + m.x597 - m.x737 >= -336)

m.c1575 = Constraint(expr= - 336*m.b22 + m.x587 - m.x739 >= -336)

m.c1576 = Constraint(expr= - 336*m.b23 + m.x588 - m.x740 >= -336)

m.c1577 = Constraint(expr= - 336*m.b22 + m.x590 - m.x739 >= -336)

m.c1578 = Constraint(expr= - 336*m.b23 + m.x591 - m.x740 >= -336)

m.c1579 = Constraint(expr= - 336*m.b22 + m.x593 - m.x739 >= -336)

m.c1580 = Constraint(expr= - 336*m.b23 + m.x594 - m.x740 >= -336)

m.c1581 = Constraint(expr= - 336*m.b25 + m.x602 - m.x742 >= -336)

m.c1582 = Constraint(expr= - 336*m.b26 + m.x603 - m.x743 >= -336)

m.c1583 = Constraint(expr= - 336*m.b25 + m.x605 - m.x742 >= -336)

m.c1584 = Constraint(expr= - 336*m.b26 + m.x606 - m.x743 >= -336)

m.c1585 = Constraint(expr= - 336*m.b25 + m.x608 - m.x742 >= -336)

m.c1586 = Constraint(expr= - 336*m.b26 + m.x609 - m.x743 >= -336)

m.c1587 = Constraint(expr= - 336*m.b28 + m.x599 - m.x745 >= -336)

m.c1588 = Constraint(expr= - 336*m.b29 + m.x600 - m.x746 >= -336)

m.c1589 = Constraint(expr= - 336*m.b28 + m.x605 - m.x745 >= -336)

m.c1590 = Constraint(expr= - 336*m.b29 + m.x606 - m.x746 >= -336)

m.c1591 = Constraint(expr= - 336*m.b28 + m.x608 - m.x745 >= -336)

m.c1592 = Constraint(expr= - 336*m.b29 + m.x609 - m.x746 >= -336)

m.c1593 = Constraint(expr= - 336*m.b31 + m.x599 - m.x748 >= -336)

m.c1594 = Constraint(expr= - 336*m.b32 + m.x600 - m.x749 >= -336)

m.c1595 = Constraint(expr= - 336*m.b31 + m.x602 - m.x748 >= -336)

m.c1596 = Constraint(expr= - 336*m.b32 + m.x603 - m.x749 >= -336)

m.c1597 = Constraint(expr= - 336*m.b31 + m.x608 - m.x748 >= -336)

m.c1598 = Constraint(expr= - 336*m.b32 + m.x609 - m.x749 >= -336)

m.c1599 = Constraint(expr= - 336*m.b34 + m.x599 - m.x751 >= -336)

m.c1600 = Constraint(expr= - 336*m.b35 + m.x600 - m.x752 >= -336)

m.c1601 = Constraint(expr= - 336*m.b34 + m.x602 - m.x751 >= -336)

m.c1602 = Constraint(expr= - 336*m.b35 + m.x603 - m.x752 >= -336)

m.c1603 = Constraint(expr= - 336*m.b34 + m.x605 - m.x751 >= -336)

m.c1604 = Constraint(expr= - 336*m.b35 + m.x606 - m.x752 >= -336)

m.c1605 = Constraint(expr= - 336*m.b37 + m.x614 - m.x754 >= -336)

m.c1606 = Constraint(expr= - 336*m.b38 + m.x615 - m.x755 >= -336)

m.c1607 = Constraint(expr= - 336*m.b37 + m.x617 - m.x754 >= -336)

m.c1608 = Constraint(expr= - 336*m.b38 + m.x618 - m.x755 >= -336)

m.c1609 = Constraint(expr= - 336*m.b37 + m.x620 - m.x754 >= -336)

m.c1610 = Constraint(expr= - 336*m.b38 + m.x621 - m.x755 >= -336)

m.c1611 = Constraint(expr= - 336*m.b40 + m.x611 - m.x757 >= -336)

m.c1612 = Constraint(expr= - 336*m.b41 + m.x612 - m.x758 >= -336)

m.c1613 = Constraint(expr= - 336*m.b40 + m.x617 - m.x757 >= -336)

m.c1614 = Constraint(expr= - 336*m.b41 + m.x618 - m.x758 >= -336)

m.c1615 = Constraint(expr= - 336*m.b40 + m.x620 - m.x757 >= -336)

m.c1616 = Constraint(expr= - 336*m.b41 + m.x621 - m.x758 >= -336)

m.c1617 = Constraint(expr= - 336*m.b43 + m.x611 - m.x760 >= -336)

m.c1618 = Constraint(expr= - 336*m.b44 + m.x612 - m.x761 >= -336)

m.c1619 = Constraint(expr= - 336*m.b43 + m.x614 - m.x760 >= -336)

m.c1620 = Constraint(expr= - 336*m.b44 + m.x615 - m.x761 >= -336)

m.c1621 = Constraint(expr= - 336*m.b43 + m.x620 - m.x760 >= -336)

m.c1622 = Constraint(expr= - 336*m.b44 + m.x621 - m.x761 >= -336)

m.c1623 = Constraint(expr= - 336*m.b46 + m.x611 - m.x763 >= -336)

m.c1624 = Constraint(expr= - 336*m.b47 + m.x612 - m.x764 >= -336)

m.c1625 = Constraint(expr= - 336*m.b46 + m.x614 - m.x763 >= -336)

m.c1626 = Constraint(expr= - 336*m.b47 + m.x615 - m.x764 >= -336)

m.c1627 = Constraint(expr= - 336*m.b46 + m.x617 - m.x763 >= -336)

m.c1628 = Constraint(expr= - 336*m.b47 + m.x618 - m.x764 >= -336)

m.c1629 = Constraint(expr= - 336*m.b49 + m.x626 - m.x766 >= -336)

m.c1630 = Constraint(expr= - 336*m.b50 + m.x627 - m.x767 >= -336)

m.c1631 = Constraint(expr= - 336*m.b49 + m.x629 - m.x766 >= -336)

m.c1632 = Constraint(expr= - 336*m.b50 + m.x630 - m.x767 >= -336)

m.c1633 = Constraint(expr= - 336*m.b49 + m.x632 - m.x766 >= -336)

m.c1634 = Constraint(expr= - 336*m.b50 + m.x633 - m.x767 >= -336)

m.c1635 = Constraint(expr= - 336*m.b52 + m.x623 - m.x769 >= -336)

m.c1636 = Constraint(expr= - 336*m.b53 + m.x624 - m.x770 >= -336)

m.c1637 = Constraint(expr= - 336*m.b52 + m.x629 - m.x769 >= -336)

m.c1638 = Constraint(expr= - 336*m.b53 + m.x630 - m.x770 >= -336)

m.c1639 = Constraint(expr= - 336*m.b52 + m.x632 - m.x769 >= -336)

m.c1640 = Constraint(expr= - 336*m.b53 + m.x633 - m.x770 >= -336)

m.c1641 = Constraint(expr= - 336*m.b55 + m.x623 - m.x772 >= -336)

m.c1642 = Constraint(expr= - 336*m.b56 + m.x624 - m.x773 >= -336)

m.c1643 = Constraint(expr= - 336*m.b55 + m.x626 - m.x772 >= -336)

m.c1644 = Constraint(expr= - 336*m.b56 + m.x627 - m.x773 >= -336)

m.c1645 = Constraint(expr= - 336*m.b55 + m.x632 - m.x772 >= -336)

m.c1646 = Constraint(expr= - 336*m.b56 + m.x633 - m.x773 >= -336)

m.c1647 = Constraint(expr= - 336*m.b58 + m.x623 - m.x775 >= -336)

m.c1648 = Constraint(expr= - 336*m.b59 + m.x624 - m.x776 >= -336)

m.c1649 = Constraint(expr= - 336*m.b58 + m.x626 - m.x775 >= -336)

m.c1650 = Constraint(expr= - 336*m.b59 + m.x627 - m.x776 >= -336)

m.c1651 = Constraint(expr= - 336*m.b58 + m.x629 - m.x775 >= -336)

m.c1652 = Constraint(expr= - 336*m.b59 + m.x630 - m.x776 >= -336)

m.c1653 = Constraint(expr= - 336*m.b61 + m.x638 - m.x778 >= -336)

m.c1654 = Constraint(expr= - 336*m.b62 + m.x639 - m.x779 >= -336)

m.c1655 = Constraint(expr= - 336*m.b61 + m.x641 - m.x778 >= -336)

m.c1656 = Constraint(expr= - 336*m.b62 + m.x642 - m.x779 >= -336)

m.c1657 = Constraint(expr= - 336*m.b61 + m.x644 - m.x778 >= -336)

m.c1658 = Constraint(expr= - 336*m.b62 + m.x645 - m.x779 >= -336)

m.c1659 = Constraint(expr= - 336*m.b64 + m.x635 - m.x781 >= -336)

m.c1660 = Constraint(expr= - 336*m.b65 + m.x636 - m.x782 >= -336)

m.c1661 = Constraint(expr= - 336*m.b64 + m.x641 - m.x781 >= -336)

m.c1662 = Constraint(expr= - 336*m.b65 + m.x642 - m.x782 >= -336)

m.c1663 = Constraint(expr= - 336*m.b64 + m.x644 - m.x781 >= -336)

m.c1664 = Constraint(expr= - 336*m.b65 + m.x645 - m.x782 >= -336)

m.c1665 = Constraint(expr= - 336*m.b67 + m.x635 - m.x784 >= -336)

m.c1666 = Constraint(expr= - 336*m.b68 + m.x636 - m.x785 >= -336)

m.c1667 = Constraint(expr= - 336*m.b67 + m.x638 - m.x784 >= -336)

m.c1668 = Constraint(expr= - 336*m.b68 + m.x639 - m.x785 >= -336)

m.c1669 = Constraint(expr= - 336*m.b67 + m.x644 - m.x784 >= -336)

m.c1670 = Constraint(expr= - 336*m.b68 + m.x645 - m.x785 >= -336)

m.c1671 = Constraint(expr= - 336*m.b70 + m.x635 - m.x787 >= -336)

m.c1672 = Constraint(expr= - 336*m.b71 + m.x636 - m.x788 >= -336)

m.c1673 = Constraint(expr= - 336*m.b70 + m.x638 - m.x787 >= -336)

m.c1674 = Constraint(expr= - 336*m.b71 + m.x639 - m.x788 >= -336)

m.c1675 = Constraint(expr= - 336*m.b70 + m.x641 - m.x787 >= -336)

m.c1676 = Constraint(expr= - 336*m.b71 + m.x642 - m.x788 >= -336)

m.c1677 = Constraint(expr= - 336*m.b73 + m.x650 - m.x790 >= -336)

m.c1678 = Constraint(expr= - 336*m.b74 + m.x651 - m.x791 >= -336)

m.c1679 = Constraint(expr= - 336*m.b73 + m.x653 - m.x790 >= -336)

m.c1680 = Constraint(expr= - 336*m.b74 + m.x654 - m.x791 >= -336)

m.c1681 = Constraint(expr= - 336*m.b73 + m.x656 - m.x790 >= -336)

m.c1682 = Constraint(expr= - 336*m.b74 + m.x657 - m.x791 >= -336)

m.c1683 = Constraint(expr= - 336*m.b76 + m.x647 - m.x793 >= -336)

m.c1684 = Constraint(expr= - 336*m.b77 + m.x648 - m.x794 >= -336)

m.c1685 = Constraint(expr= - 336*m.b76 + m.x653 - m.x793 >= -336)

m.c1686 = Constraint(expr= - 336*m.b77 + m.x654 - m.x794 >= -336)

m.c1687 = Constraint(expr= - 336*m.b76 + m.x656 - m.x793 >= -336)

m.c1688 = Constraint(expr= - 336*m.b77 + m.x657 - m.x794 >= -336)

m.c1689 = Constraint(expr= - 336*m.b79 + m.x647 - m.x796 >= -336)

m.c1690 = Constraint(expr= - 336*m.b80 + m.x648 - m.x797 >= -336)

m.c1691 = Constraint(expr= - 336*m.b79 + m.x650 - m.x796 >= -336)

m.c1692 = Constraint(expr= - 336*m.b80 + m.x651 - m.x797 >= -336)

m.c1693 = Constraint(expr= - 336*m.b79 + m.x656 - m.x796 >= -336)

m.c1694 = Constraint(expr= - 336*m.b80 + m.x657 - m.x797 >= -336)

m.c1695 = Constraint(expr= - 336*m.b82 + m.x647 - m.x799 >= -336)

m.c1696 = Constraint(expr= - 336*m.b83 + m.x648 - m.x800 >= -336)

m.c1697 = Constraint(expr= - 336*m.b82 + m.x650 - m.x799 >= -336)

m.c1698 = Constraint(expr= - 336*m.b83 + m.x651 - m.x800 >= -336)

m.c1699 = Constraint(expr= - 336*m.b82 + m.x653 - m.x799 >= -336)

m.c1700 = Constraint(expr= - 336*m.b83 + m.x654 - m.x800 >= -336)

m.c1701 = Constraint(expr= - 336*m.b85 + m.x662 - m.x802 >= -336)

m.c1702 = Constraint(expr= - 336*m.b86 + m.x663 - m.x803 >= -336)

m.c1703 = Constraint(expr= - 336*m.b85 + m.x665 - m.x802 >= -336)

m.c1704 = Constraint(expr= - 336*m.b86 + m.x666 - m.x803 >= -336)

m.c1705 = Constraint(expr= - 336*m.b85 + m.x668 - m.x802 >= -336)

m.c1706 = Constraint(expr= - 336*m.b86 + m.x669 - m.x803 >= -336)

m.c1707 = Constraint(expr= - 336*m.b88 + m.x659 - m.x805 >= -336)

m.c1708 = Constraint(expr= - 336*m.b89 + m.x660 - m.x806 >= -336)

m.c1709 = Constraint(expr= - 336*m.b88 + m.x665 - m.x805 >= -336)

m.c1710 = Constraint(expr= - 336*m.b89 + m.x666 - m.x806 >= -336)

m.c1711 = Constraint(expr= - 336*m.b88 + m.x668 - m.x805 >= -336)

m.c1712 = Constraint(expr= - 336*m.b89 + m.x669 - m.x806 >= -336)

m.c1713 = Constraint(expr= - 336*m.b91 + m.x659 - m.x808 >= -336)

m.c1714 = Constraint(expr= - 336*m.b92 + m.x660 - m.x809 >= -336)

m.c1715 = Constraint(expr= - 336*m.b91 + m.x662 - m.x808 >= -336)

m.c1716 = Constraint(expr= - 336*m.b92 + m.x663 - m.x809 >= -336)

m.c1717 = Constraint(expr= - 336*m.b91 + m.x668 - m.x808 >= -336)

m.c1718 = Constraint(expr= - 336*m.b92 + m.x669 - m.x809 >= -336)

m.c1719 = Constraint(expr= - 336*m.b94 + m.x659 - m.x811 >= -336)

m.c1720 = Constraint(expr= - 336*m.b95 + m.x660 - m.x812 >= -336)

m.c1721 = Constraint(expr= - 336*m.b94 + m.x662 - m.x811 >= -336)

m.c1722 = Constraint(expr= - 336*m.b95 + m.x663 - m.x812 >= -336)

m.c1723 = Constraint(expr= - 336*m.b94 + m.x665 - m.x811 >= -336)

m.c1724 = Constraint(expr= - 336*m.b95 + m.x666 - m.x812 >= -336)

m.c1725 = Constraint(expr= - 336*m.b97 + m.x674 - m.x814 >= -336)

m.c1726 = Constraint(expr= - 336*m.b98 + m.x675 - m.x815 >= -336)

m.c1727 = Constraint(expr= - 336*m.b97 + m.x677 - m.x814 >= -336)

m.c1728 = Constraint(expr= - 336*m.b98 + m.x678 - m.x815 >= -336)

m.c1729 = Constraint(expr= - 336*m.b97 + m.x680 - m.x814 >= -336)

m.c1730 = Constraint(expr= - 336*m.b98 + m.x681 - m.x815 >= -336)

m.c1731 = Constraint(expr= - 336*m.b100 + m.x671 - m.x817 >= -336)

m.c1732 = Constraint(expr= - 336*m.b101 + m.x672 - m.x818 >= -336)

m.c1733 = Constraint(expr= - 336*m.b100 + m.x677 - m.x817 >= -336)

m.c1734 = Constraint(expr= - 336*m.b101 + m.x678 - m.x818 >= -336)

m.c1735 = Constraint(expr= - 336*m.b100 + m.x680 - m.x817 >= -336)

m.c1736 = Constraint(expr= - 336*m.b101 + m.x681 - m.x818 >= -336)

m.c1737 = Constraint(expr= - 336*m.b103 + m.x671 - m.x820 >= -336)

m.c1738 = Constraint(expr= - 336*m.b104 + m.x672 - m.x821 >= -336)

m.c1739 = Constraint(expr= - 336*m.b103 + m.x674 - m.x820 >= -336)

m.c1740 = Constraint(expr= - 336*m.b104 + m.x675 - m.x821 >= -336)

m.c1741 = Constraint(expr= - 336*m.b103 + m.x680 - m.x820 >= -336)

m.c1742 = Constraint(expr= - 336*m.b104 + m.x681 - m.x821 >= -336)

m.c1743 = Constraint(expr= - 336*m.b106 + m.x671 - m.x823 >= -336)

m.c1744 = Constraint(expr= - 336*m.b107 + m.x672 - m.x824 >= -336)

m.c1745 = Constraint(expr= - 336*m.b106 + m.x674 - m.x823 >= -336)

m.c1746 = Constraint(expr= - 336*m.b107 + m.x675 - m.x824 >= -336)

m.c1747 = Constraint(expr= - 336*m.b106 + m.x677 - m.x823 >= -336)

m.c1748 = Constraint(expr= - 336*m.b107 + m.x678 - m.x824 >= -336)

m.c1749 = Constraint(expr= - 336*m.b109 + m.x686 - m.x826 >= -336)

m.c1750 = Constraint(expr= - 336*m.b110 + m.x687 - m.x827 >= -336)

m.c1751 = Constraint(expr= - 336*m.b109 + m.x689 - m.x826 >= -336)

m.c1752 = Constraint(expr= - 336*m.b110 + m.x690 - m.x827 >= -336)

m.c1753 = Constraint(expr= - 336*m.b109 + m.x692 - m.x826 >= -336)

m.c1754 = Constraint(expr= - 336*m.b110 + m.x693 - m.x827 >= -336)

m.c1755 = Constraint(expr= - 336*m.b112 + m.x683 - m.x829 >= -336)

m.c1756 = Constraint(expr= - 336*m.b113 + m.x684 - m.x830 >= -336)

m.c1757 = Constraint(expr= - 336*m.b112 + m.x689 - m.x829 >= -336)

m.c1758 = Constraint(expr= - 336*m.b113 + m.x690 - m.x830 >= -336)

m.c1759 = Constraint(expr= - 336*m.b112 + m.x692 - m.x829 >= -336)

m.c1760 = Constraint(expr= - 336*m.b113 + m.x693 - m.x830 >= -336)

m.c1761 = Constraint(expr= - 336*m.b115 + m.x683 - m.x832 >= -336)

m.c1762 = Constraint(expr= - 336*m.b116 + m.x684 - m.x833 >= -336)

m.c1763 = Constraint(expr= - 336*m.b115 + m.x686 - m.x832 >= -336)

m.c1764 = Constraint(expr= - 336*m.b116 + m.x687 - m.x833 >= -336)

m.c1765 = Constraint(expr= - 336*m.b115 + m.x692 - m.x832 >= -336)

m.c1766 = Constraint(expr= - 336*m.b116 + m.x693 - m.x833 >= -336)

m.c1767 = Constraint(expr= - 336*m.b118 + m.x683 - m.x835 >= -336)

m.c1768 = Constraint(expr= - 336*m.b119 + m.x684 - m.x836 >= -336)

m.c1769 = Constraint(expr= - 336*m.b118 + m.x686 - m.x835 >= -336)

m.c1770 = Constraint(expr= - 336*m.b119 + m.x687 - m.x836 >= -336)

m.c1771 = Constraint(expr= - 336*m.b118 + m.x689 - m.x835 >= -336)

m.c1772 = Constraint(expr= - 336*m.b119 + m.x690 - m.x836 >= -336)

m.c1773 = Constraint(expr= - 336*m.b121 + m.x698 - m.x838 >= -336)

m.c1774 = Constraint(expr= - 336*m.b122 + m.x699 - m.x839 >= -336)

m.c1775 = Constraint(expr= - 336*m.b121 + m.x701 - m.x838 >= -336)

m.c1776 = Constraint(expr= - 336*m.b122 + m.x702 - m.x839 >= -336)

m.c1777 = Constraint(expr= - 336*m.b121 + m.x704 - m.x838 >= -336)

m.c1778 = Constraint(expr= - 336*m.b122 + m.x705 - m.x839 >= -336)

m.c1779 = Constraint(expr= - 336*m.b124 + m.x695 - m.x841 >= -336)

m.c1780 = Constraint(expr= - 336*m.b125 + m.x696 - m.x842 >= -336)

m.c1781 = Constraint(expr= - 336*m.b124 + m.x701 - m.x841 >= -336)

m.c1782 = Constraint(expr= - 336*m.b125 + m.x702 - m.x842 >= -336)

m.c1783 = Constraint(expr= - 336*m.b124 + m.x704 - m.x841 >= -336)

m.c1784 = Constraint(expr= - 336*m.b125 + m.x705 - m.x842 >= -336)

m.c1785 = Constraint(expr= - 336*m.b127 + m.x695 - m.x844 >= -336)

m.c1786 = Constraint(expr= - 336*m.b128 + m.x696 - m.x845 >= -336)

m.c1787 = Constraint(expr= - 336*m.b127 + m.x698 - m.x844 >= -336)

m.c1788 = Constraint(expr= - 336*m.b128 + m.x699 - m.x845 >= -336)

m.c1789 = Constraint(expr= - 336*m.b127 + m.x704 - m.x844 >= -336)

m.c1790 = Constraint(expr= - 336*m.b128 + m.x705 - m.x845 >= -336)

m.c1791 = Constraint(expr= - 336*m.b130 + m.x695 - m.x847 >= -336)

m.c1792 = Constraint(expr= - 336*m.b131 + m.x696 - m.x848 >= -336)

m.c1793 = Constraint(expr= - 336*m.b130 + m.x698 - m.x847 >= -336)

m.c1794 = Constraint(expr= - 336*m.b131 + m.x699 - m.x848 >= -336)

m.c1795 = Constraint(expr= - 336*m.b130 + m.x701 - m.x847 >= -336)

m.c1796 = Constraint(expr= - 336*m.b131 + m.x702 - m.x848 >= -336)

m.c1797 = Constraint(expr= - 336*m.b133 + m.x710 - m.x850 >= -336)

m.c1798 = Constraint(expr= - 336*m.b134 + m.x711 - m.x851 >= -336)

m.c1799 = Constraint(expr= - 336*m.b133 + m.x713 - m.x850 >= -336)

m.c1800 = Constraint(expr= - 336*m.b134 + m.x714 - m.x851 >= -336)

m.c1801 = Constraint(expr= - 336*m.b133 + m.x716 - m.x850 >= -336)

m.c1802 = Constraint(expr= - 336*m.b134 + m.x717 - m.x851 >= -336)

m.c1803 = Constraint(expr= - 336*m.b136 + m.x707 - m.x853 >= -336)

m.c1804 = Constraint(expr= - 336*m.b137 + m.x708 - m.x854 >= -336)

m.c1805 = Constraint(expr= - 336*m.b136 + m.x713 - m.x853 >= -336)

m.c1806 = Constraint(expr= - 336*m.b137 + m.x714 - m.x854 >= -336)

m.c1807 = Constraint(expr= - 336*m.b136 + m.x716 - m.x853 >= -336)

m.c1808 = Constraint(expr= - 336*m.b137 + m.x717 - m.x854 >= -336)

m.c1809 = Constraint(expr= - 336*m.b139 + m.x707 - m.x856 >= -336)

m.c1810 = Constraint(expr= - 336*m.b140 + m.x708 - m.x857 >= -336)

m.c1811 = Constraint(expr= - 336*m.b139 + m.x710 - m.x856 >= -336)

m.c1812 = Constraint(expr= - 336*m.b140 + m.x711 - m.x857 >= -336)

m.c1813 = Constraint(expr= - 336*m.b139 + m.x716 - m.x856 >= -336)

m.c1814 = Constraint(expr= - 336*m.b140 + m.x717 - m.x857 >= -336)

m.c1815 = Constraint(expr= - 336*m.b142 + m.x707 - m.x859 >= -336)

m.c1816 = Constraint(expr= - 336*m.b143 + m.x708 - m.x860 >= -336)

m.c1817 = Constraint(expr= - 336*m.b142 + m.x710 - m.x859 >= -336)

m.c1818 = Constraint(expr= - 336*m.b143 + m.x711 - m.x860 >= -336)

m.c1819 = Constraint(expr= - 336*m.b142 + m.x713 - m.x859 >= -336)

m.c1820 = Constraint(expr= - 336*m.b143 + m.x714 - m.x860 >= -336)

m.c1821 = Constraint(expr= - 336*m.b1 + m.x587 - m.x718 >= -336)

m.c1822 = Constraint(expr= - 336*m.b2 + m.x588 - m.x719 >= -336)

m.c1823 = Constraint(expr= - 336*m.b4 + m.x590 - m.x721 >= -336)

m.c1824 = Constraint(expr= - 336*m.b5 + m.x591 - m.x722 >= -336)

m.c1825 = Constraint(expr= - 336*m.b7 + m.x593 - m.x724 >= -336)

m.c1826 = Constraint(expr= - 336*m.b8 + m.x594 - m.x725 >= -336)

m.c1827 = Constraint(expr= - 336*m.b10 + m.x596 - m.x727 >= -336)

m.c1828 = Constraint(expr= - 336*m.b11 + m.x597 - m.x728 >= -336)

m.c1829 = Constraint(expr= - 336*m.b1 + m.x599 - m.x718 >= -336)

m.c1830 = Constraint(expr= - 336*m.b2 + m.x600 - m.x719 >= -336)

m.c1831 = Constraint(expr= - 336*m.b4 + m.x602 - m.x721 >= -336)

m.c1832 = Constraint(expr= - 336*m.b5 + m.x603 - m.x722 >= -336)

m.c1833 = Constraint(expr= - 336*m.b7 + m.x605 - m.x724 >= -336)

m.c1834 = Constraint(expr= - 336*m.b8 + m.x606 - m.x725 >= -336)

m.c1835 = Constraint(expr= - 336*m.b10 + m.x608 - m.x727 >= -336)

m.c1836 = Constraint(expr= - 336*m.b11 + m.x609 - m.x728 >= -336)

m.c1837 = Constraint(expr= - 336*m.b1 + m.x659 - m.x718 >= -336)

m.c1838 = Constraint(expr= - 336*m.b2 + m.x660 - m.x719 >= -336)

m.c1839 = Constraint(expr= - 336*m.b4 + m.x662 - m.x721 >= -336)

m.c1840 = Constraint(expr= - 336*m.b5 + m.x663 - m.x722 >= -336)

m.c1841 = Constraint(expr= - 336*m.b7 + m.x665 - m.x724 >= -336)

m.c1842 = Constraint(expr= - 336*m.b8 + m.x666 - m.x725 >= -336)

m.c1843 = Constraint(expr= - 336*m.b10 + m.x668 - m.x727 >= -336)

m.c1844 = Constraint(expr= - 336*m.b11 + m.x669 - m.x728 >= -336)

m.c1845 = Constraint(expr= - 336*m.b1 + m.x671 - m.x718 >= -336)

m.c1846 = Constraint(expr= - 336*m.b2 + m.x672 - m.x719 >= -336)

m.c1847 = Constraint(expr= - 336*m.b4 + m.x674 - m.x721 >= -336)

m.c1848 = Constraint(expr= - 336*m.b5 + m.x675 - m.x722 >= -336)

m.c1849 = Constraint(expr= - 336*m.b7 + m.x677 - m.x724 >= -336)

m.c1850 = Constraint(expr= - 336*m.b8 + m.x678 - m.x725 >= -336)

m.c1851 = Constraint(expr= - 336*m.b10 + m.x680 - m.x727 >= -336)

m.c1852 = Constraint(expr= - 336*m.b11 + m.x681 - m.x728 >= -336)

m.c1853 = Constraint(expr= - 336*m.b1 + m.x695 - m.x718 >= -336)

m.c1854 = Constraint(expr= - 336*m.b2 + m.x696 - m.x719 >= -336)

m.c1855 = Constraint(expr= - 336*m.b4 + m.x698 - m.x721 >= -336)

m.c1856 = Constraint(expr= - 336*m.b5 + m.x699 - m.x722 >= -336)

m.c1857 = Constraint(expr= - 336*m.b7 + m.x701 - m.x724 >= -336)

m.c1858 = Constraint(expr= - 336*m.b8 + m.x702 - m.x725 >= -336)

m.c1859 = Constraint(expr= - 336*m.b10 + m.x704 - m.x727 >= -336)

m.c1860 = Constraint(expr= - 336*m.b11 + m.x705 - m.x728 >= -336)

m.c1861 = Constraint(expr= - 336*m.b13 + m.x575 - m.x730 >= -336)

m.c1862 = Constraint(expr= - 336*m.b14 + m.x576 - m.x731 >= -336)

m.c1863 = Constraint(expr= - 336*m.b16 + m.x578 - m.x733 >= -336)

m.c1864 = Constraint(expr= - 336*m.b17 + m.x579 - m.x734 >= -336)

m.c1865 = Constraint(expr= - 336*m.b19 + m.x581 - m.x736 >= -336)

m.c1866 = Constraint(expr= - 336*m.b20 + m.x582 - m.x737 >= -336)

m.c1867 = Constraint(expr= - 336*m.b22 + m.x584 - m.x739 >= -336)

m.c1868 = Constraint(expr= - 336*m.b23 + m.x585 - m.x740 >= -336)

m.c1869 = Constraint(expr= - 336*m.b13 + m.x599 - m.x730 >= -336)

m.c1870 = Constraint(expr= - 336*m.b14 + m.x600 - m.x731 >= -336)

m.c1871 = Constraint(expr= - 336*m.b16 + m.x602 - m.x733 >= -336)

m.c1872 = Constraint(expr= - 336*m.b17 + m.x603 - m.x734 >= -336)

m.c1873 = Constraint(expr= - 336*m.b19 + m.x605 - m.x736 >= -336)

m.c1874 = Constraint(expr= - 336*m.b20 + m.x606 - m.x737 >= -336)

m.c1875 = Constraint(expr= - 336*m.b22 + m.x608 - m.x739 >= -336)

m.c1876 = Constraint(expr= - 336*m.b23 + m.x609 - m.x740 >= -336)

m.c1877 = Constraint(expr= - 336*m.b13 + m.x659 - m.x730 >= -336)

m.c1878 = Constraint(expr= - 336*m.b14 + m.x660 - m.x731 >= -336)

m.c1879 = Constraint(expr= - 336*m.b16 + m.x662 - m.x733 >= -336)

m.c1880 = Constraint(expr= - 336*m.b17 + m.x663 - m.x734 >= -336)

m.c1881 = Constraint(expr= - 336*m.b19 + m.x665 - m.x736 >= -336)

m.c1882 = Constraint(expr= - 336*m.b20 + m.x666 - m.x737 >= -336)

m.c1883 = Constraint(expr= - 336*m.b22 + m.x668 - m.x739 >= -336)

m.c1884 = Constraint(expr= - 336*m.b23 + m.x669 - m.x740 >= -336)

m.c1885 = Constraint(expr= - 336*m.b13 + m.x671 - m.x730 >= -336)

m.c1886 = Constraint(expr= - 336*m.b14 + m.x672 - m.x731 >= -336)

m.c1887 = Constraint(expr= - 336*m.b16 + m.x674 - m.x733 >= -336)

m.c1888 = Constraint(expr= - 336*m.b17 + m.x675 - m.x734 >= -336)

m.c1889 = Constraint(expr= - 336*m.b19 + m.x677 - m.x736 >= -336)

m.c1890 = Constraint(expr= - 336*m.b20 + m.x678 - m.x737 >= -336)

m.c1891 = Constraint(expr= - 336*m.b22 + m.x680 - m.x739 >= -336)

m.c1892 = Constraint(expr= - 336*m.b23 + m.x681 - m.x740 >= -336)

m.c1893 = Constraint(expr= - 336*m.b13 + m.x695 - m.x730 >= -336)

m.c1894 = Constraint(expr= - 336*m.b14 + m.x696 - m.x731 >= -336)

m.c1895 = Constraint(expr= - 336*m.b16 + m.x698 - m.x733 >= -336)

m.c1896 = Constraint(expr= - 336*m.b17 + m.x699 - m.x734 >= -336)

m.c1897 = Constraint(expr= - 336*m.b19 + m.x701 - m.x736 >= -336)

m.c1898 = Constraint(expr= - 336*m.b20 + m.x702 - m.x737 >= -336)

m.c1899 = Constraint(expr= - 336*m.b22 + m.x704 - m.x739 >= -336)

m.c1900 = Constraint(expr= - 336*m.b23 + m.x705 - m.x740 >= -336)

m.c1901 = Constraint(expr= - 336*m.b25 + m.x575 - m.x742 >= -336)

m.c1902 = Constraint(expr= - 336*m.b26 + m.x576 - m.x743 >= -336)

m.c1903 = Constraint(expr= - 336*m.b28 + m.x578 - m.x745 >= -336)

m.c1904 = Constraint(expr= - 336*m.b29 + m.x579 - m.x746 >= -336)

m.c1905 = Constraint(expr= - 336*m.b31 + m.x581 - m.x748 >= -336)

m.c1906 = Constraint(expr= - 336*m.b32 + m.x582 - m.x749 >= -336)

m.c1907 = Constraint(expr= - 336*m.b34 + m.x584 - m.x751 >= -336)

m.c1908 = Constraint(expr= - 336*m.b35 + m.x585 - m.x752 >= -336)

m.c1909 = Constraint(expr= - 336*m.b25 + m.x587 - m.x742 >= -336)

m.c1910 = Constraint(expr= - 336*m.b26 + m.x588 - m.x743 >= -336)

m.c1911 = Constraint(expr= - 336*m.b28 + m.x590 - m.x745 >= -336)

m.c1912 = Constraint(expr= - 336*m.b29 + m.x591 - m.x746 >= -336)

m.c1913 = Constraint(expr= - 336*m.b31 + m.x593 - m.x748 >= -336)

m.c1914 = Constraint(expr= - 336*m.b32 + m.x594 - m.x749 >= -336)

m.c1915 = Constraint(expr= - 336*m.b34 + m.x596 - m.x751 >= -336)

m.c1916 = Constraint(expr= - 336*m.b35 + m.x597 - m.x752 >= -336)

m.c1917 = Constraint(expr= - 336*m.b25 + m.x659 - m.x742 >= -336)

m.c1918 = Constraint(expr= - 336*m.b26 + m.x660 - m.x743 >= -336)

m.c1919 = Constraint(expr= - 336*m.b28 + m.x662 - m.x745 >= -336)

m.c1920 = Constraint(expr= - 336*m.b29 + m.x663 - m.x746 >= -336)

m.c1921 = Constraint(expr= - 336*m.b31 + m.x665 - m.x748 >= -336)

m.c1922 = Constraint(expr= - 336*m.b32 + m.x666 - m.x749 >= -336)

m.c1923 = Constraint(expr= - 336*m.b34 + m.x668 - m.x751 >= -336)

m.c1924 = Constraint(expr= - 336*m.b35 + m.x669 - m.x752 >= -336)

m.c1925 = Constraint(expr= - 336*m.b25 + m.x671 - m.x742 >= -336)

m.c1926 = Constraint(expr= - 336*m.b26 + m.x672 - m.x743 >= -336)

m.c1927 = Constraint(expr= - 336*m.b28 + m.x674 - m.x745 >= -336)

m.c1928 = Constraint(expr= - 336*m.b29 + m.x675 - m.x746 >= -336)

m.c1929 = Constraint(expr= - 336*m.b31 + m.x677 - m.x748 >= -336)

m.c1930 = Constraint(expr= - 336*m.b32 + m.x678 - m.x749 >= -336)

m.c1931 = Constraint(expr= - 336*m.b34 + m.x680 - m.x751 >= -336)

m.c1932 = Constraint(expr= - 336*m.b35 + m.x681 - m.x752 >= -336)

m.c1933 = Constraint(expr= - 336*m.b25 + m.x695 - m.x742 >= -336)

m.c1934 = Constraint(expr= - 336*m.b26 + m.x696 - m.x743 >= -336)

m.c1935 = Constraint(expr= - 336*m.b28 + m.x698 - m.x745 >= -336)

m.c1936 = Constraint(expr= - 336*m.b29 + m.x699 - m.x746 >= -336)

m.c1937 = Constraint(expr= - 336*m.b31 + m.x701 - m.x748 >= -336)

m.c1938 = Constraint(expr= - 336*m.b32 + m.x702 - m.x749 >= -336)

m.c1939 = Constraint(expr= - 336*m.b34 + m.x704 - m.x751 >= -336)

m.c1940 = Constraint(expr= - 336*m.b35 + m.x705 - m.x752 >= -336)

m.c1941 = Constraint(expr= - 336*m.b37 + m.x623 - m.x754 >= -336)

m.c1942 = Constraint(expr= - 336*m.b38 + m.x624 - m.x755 >= -336)

m.c1943 = Constraint(expr= - 336*m.b40 + m.x626 - m.x757 >= -336)

m.c1944 = Constraint(expr= - 336*m.b41 + m.x627 - m.x758 >= -336)

m.c1945 = Constraint(expr= - 336*m.b43 + m.x629 - m.x760 >= -336)

m.c1946 = Constraint(expr= - 336*m.b44 + m.x630 - m.x761 >= -336)

m.c1947 = Constraint(expr= - 336*m.b46 + m.x632 - m.x763 >= -336)

m.c1948 = Constraint(expr= - 336*m.b47 + m.x633 - m.x764 >= -336)

m.c1949 = Constraint(expr= - 336*m.b37 + m.x635 - m.x754 >= -336)

m.c1950 = Constraint(expr= - 336*m.b38 + m.x636 - m.x755 >= -336)

m.c1951 = Constraint(expr= - 336*m.b40 + m.x638 - m.x757 >= -336)

m.c1952 = Constraint(expr= - 336*m.b41 + m.x639 - m.x758 >= -336)

m.c1953 = Constraint(expr= - 336*m.b43 + m.x641 - m.x760 >= -336)

m.c1954 = Constraint(expr= - 336*m.b44 + m.x642 - m.x761 >= -336)

m.c1955 = Constraint(expr= - 336*m.b46 + m.x644 - m.x763 >= -336)

m.c1956 = Constraint(expr= - 336*m.b47 + m.x645 - m.x764 >= -336)

m.c1957 = Constraint(expr= - 336*m.b37 + m.x647 - m.x754 >= -336)

m.c1958 = Constraint(expr= - 336*m.b38 + m.x648 - m.x755 >= -336)

m.c1959 = Constraint(expr= - 336*m.b40 + m.x650 - m.x757 >= -336)

m.c1960 = Constraint(expr= - 336*m.b41 + m.x651 - m.x758 >= -336)

m.c1961 = Constraint(expr= - 336*m.b43 + m.x653 - m.x760 >= -336)

m.c1962 = Constraint(expr= - 336*m.b44 + m.x654 - m.x761 >= -336)

m.c1963 = Constraint(expr= - 336*m.b46 + m.x656 - m.x763 >= -336)

m.c1964 = Constraint(expr= - 336*m.b47 + m.x657 - m.x764 >= -336)

m.c1965 = Constraint(expr= - 336*m.b37 + m.x683 - m.x754 >= -336)

m.c1966 = Constraint(expr= - 336*m.b38 + m.x684 - m.x755 >= -336)

m.c1967 = Constraint(expr= - 336*m.b40 + m.x686 - m.x757 >= -336)

m.c1968 = Constraint(expr= - 336*m.b41 + m.x687 - m.x758 >= -336)

m.c1969 = Constraint(expr= - 336*m.b43 + m.x689 - m.x760 >= -336)

m.c1970 = Constraint(expr= - 336*m.b44 + m.x690 - m.x761 >= -336)

m.c1971 = Constraint(expr= - 336*m.b46 + m.x692 - m.x763 >= -336)

m.c1972 = Constraint(expr= - 336*m.b47 + m.x693 - m.x764 >= -336)

m.c1973 = Constraint(expr= - 336*m.b37 + m.x707 - m.x754 >= -336)

m.c1974 = Constraint(expr= - 336*m.b38 + m.x708 - m.x755 >= -336)

m.c1975 = Constraint(expr= - 336*m.b40 + m.x710 - m.x757 >= -336)

m.c1976 = Constraint(expr= - 336*m.b41 + m.x711 - m.x758 >= -336)

m.c1977 = Constraint(expr= - 336*m.b43 + m.x713 - m.x760 >= -336)

m.c1978 = Constraint(expr= - 336*m.b44 + m.x714 - m.x761 >= -336)

m.c1979 = Constraint(expr= - 336*m.b46 + m.x716 - m.x763 >= -336)

m.c1980 = Constraint(expr= - 336*m.b47 + m.x717 - m.x764 >= -336)

m.c1981 = Constraint(expr= - 336*m.b49 + m.x611 - m.x766 >= -336)

m.c1982 = Constraint(expr= - 336*m.b50 + m.x612 - m.x767 >= -336)

m.c1983 = Constraint(expr= - 336*m.b52 + m.x614 - m.x769 >= -336)

m.c1984 = Constraint(expr= - 336*m.b53 + m.x615 - m.x770 >= -336)

m.c1985 = Constraint(expr= - 336*m.b55 + m.x617 - m.x772 >= -336)

m.c1986 = Constraint(expr= - 336*m.b56 + m.x618 - m.x773 >= -336)

m.c1987 = Constraint(expr= - 336*m.b58 + m.x620 - m.x775 >= -336)

m.c1988 = Constraint(expr= - 336*m.b59 + m.x621 - m.x776 >= -336)

m.c1989 = Constraint(expr= - 336*m.b49 + m.x635 - m.x766 >= -336)

m.c1990 = Constraint(expr= - 336*m.b50 + m.x636 - m.x767 >= -336)

m.c1991 = Constraint(expr= - 336*m.b52 + m.x638 - m.x769 >= -336)

m.c1992 = Constraint(expr= - 336*m.b53 + m.x639 - m.x770 >= -336)

m.c1993 = Constraint(expr= - 336*m.b55 + m.x641 - m.x772 >= -336)

m.c1994 = Constraint(expr= - 336*m.b56 + m.x642 - m.x773 >= -336)

m.c1995 = Constraint(expr= - 336*m.b58 + m.x644 - m.x775 >= -336)

m.c1996 = Constraint(expr= - 336*m.b59 + m.x645 - m.x776 >= -336)

m.c1997 = Constraint(expr= - 336*m.b49 + m.x647 - m.x766 >= -336)

m.c1998 = Constraint(expr= - 336*m.b50 + m.x648 - m.x767 >= -336)

m.c1999 = Constraint(expr= - 336*m.b52 + m.x650 - m.x769 >= -336)

m.c2000 = Constraint(expr= - 336*m.b53 + m.x651 - m.x770 >= -336)

m.c2001 = Constraint(expr= - 336*m.b55 + m.x653 - m.x772 >= -336)

m.c2002 = Constraint(expr= - 336*m.b56 + m.x654 - m.x773 >= -336)

m.c2003 = Constraint(expr= - 336*m.b58 + m.x656 - m.x775 >= -336)

m.c2004 = Constraint(expr= - 336*m.b59 + m.x657 - m.x776 >= -336)

m.c2005 = Constraint(expr= - 336*m.b49 + m.x683 - m.x766 >= -336)

m.c2006 = Constraint(expr= - 336*m.b50 + m.x684 - m.x767 >= -336)

m.c2007 = Constraint(expr= - 336*m.b52 + m.x686 - m.x769 >= -336)

m.c2008 = Constraint(expr= - 336*m.b53 + m.x687 - m.x770 >= -336)

m.c2009 = Constraint(expr= - 336*m.b55 + m.x689 - m.x772 >= -336)

m.c2010 = Constraint(expr= - 336*m.b56 + m.x690 - m.x773 >= -336)

m.c2011 = Constraint(expr= - 336*m.b58 + m.x692 - m.x775 >= -336)

m.c2012 = Constraint(expr= - 336*m.b59 + m.x693 - m.x776 >= -336)

m.c2013 = Constraint(expr= - 336*m.b49 + m.x707 - m.x766 >= -336)

m.c2014 = Constraint(expr= - 336*m.b50 + m.x708 - m.x767 >= -336)

m.c2015 = Constraint(expr= - 336*m.b52 + m.x710 - m.x769 >= -336)

m.c2016 = Constraint(expr= - 336*m.b53 + m.x711 - m.x770 >= -336)

m.c2017 = Constraint(expr= - 336*m.b55 + m.x713 - m.x772 >= -336)

m.c2018 = Constraint(expr= - 336*m.b56 + m.x714 - m.x773 >= -336)

m.c2019 = Constraint(expr= - 336*m.b58 + m.x716 - m.x775 >= -336)

m.c2020 = Constraint(expr= - 336*m.b59 + m.x717 - m.x776 >= -336)

m.c2021 = Constraint(expr= - 336*m.b61 + m.x611 - m.x778 >= -336)

m.c2022 = Constraint(expr= - 336*m.b62 + m.x612 - m.x779 >= -336)

m.c2023 = Constraint(expr= - 336*m.b64 + m.x614 - m.x781 >= -336)

m.c2024 = Constraint(expr= - 336*m.b65 + m.x615 - m.x782 >= -336)

m.c2025 = Constraint(expr= - 336*m.b67 + m.x617 - m.x784 >= -336)

m.c2026 = Constraint(expr= - 336*m.b68 + m.x618 - m.x785 >= -336)

m.c2027 = Constraint(expr= - 336*m.b70 + m.x620 - m.x787 >= -336)

m.c2028 = Constraint(expr= - 336*m.b71 + m.x621 - m.x788 >= -336)

m.c2029 = Constraint(expr= - 336*m.b61 + m.x623 - m.x778 >= -336)

m.c2030 = Constraint(expr= - 336*m.b62 + m.x624 - m.x779 >= -336)

m.c2031 = Constraint(expr= - 336*m.b64 + m.x626 - m.x781 >= -336)

m.c2032 = Constraint(expr= - 336*m.b65 + m.x627 - m.x782 >= -336)

m.c2033 = Constraint(expr= - 336*m.b67 + m.x629 - m.x784 >= -336)

m.c2034 = Constraint(expr= - 336*m.b68 + m.x630 - m.x785 >= -336)

m.c2035 = Constraint(expr= - 336*m.b70 + m.x632 - m.x787 >= -336)

m.c2036 = Constraint(expr= - 336*m.b71 + m.x633 - m.x788 >= -336)

m.c2037 = Constraint(expr= - 336*m.b61 + m.x647 - m.x778 >= -336)

m.c2038 = Constraint(expr= - 336*m.b62 + m.x648 - m.x779 >= -336)

m.c2039 = Constraint(expr= - 336*m.b64 + m.x650 - m.x781 >= -336)

m.c2040 = Constraint(expr= - 336*m.b65 + m.x651 - m.x782 >= -336)

m.c2041 = Constraint(expr= - 336*m.b67 + m.x653 - m.x784 >= -336)

m.c2042 = Constraint(expr= - 336*m.b68 + m.x654 - m.x785 >= -336)

m.c2043 = Constraint(expr= - 336*m.b70 + m.x656 - m.x787 >= -336)

m.c2044 = Constraint(expr= - 336*m.b71 + m.x657 - m.x788 >= -336)

m.c2045 = Constraint(expr= - 336*m.b61 + m.x683 - m.x778 >= -336)

m.c2046 = Constraint(expr= - 336*m.b62 + m.x684 - m.x779 >= -336)

m.c2047 = Constraint(expr= - 336*m.b64 + m.x686 - m.x781 >= -336)

m.c2048 = Constraint(expr= - 336*m.b65 + m.x687 - m.x782 >= -336)

m.c2049 = Constraint(expr= - 336*m.b67 + m.x689 - m.x784 >= -336)

m.c2050 = Constraint(expr= - 336*m.b68 + m.x690 - m.x785 >= -336)

m.c2051 = Constraint(expr= - 336*m.b70 + m.x692 - m.x787 >= -336)

m.c2052 = Constraint(expr= - 336*m.b71 + m.x693 - m.x788 >= -336)

m.c2053 = Constraint(expr= - 336*m.b61 + m.x707 - m.x778 >= -336)

m.c2054 = Constraint(expr= - 336*m.b62 + m.x708 - m.x779 >= -336)

m.c2055 = Constraint(expr= - 336*m.b64 + m.x710 - m.x781 >= -336)

m.c2056 = Constraint(expr= - 336*m.b65 + m.x711 - m.x782 >= -336)

m.c2057 = Constraint(expr= - 336*m.b67 + m.x713 - m.x784 >= -336)

m.c2058 = Constraint(expr= - 336*m.b68 + m.x714 - m.x785 >= -336)

m.c2059 = Constraint(expr= - 336*m.b70 + m.x716 - m.x787 >= -336)

m.c2060 = Constraint(expr= - 336*m.b71 + m.x717 - m.x788 >= -336)

m.c2061 = Constraint(expr= - 336*m.b73 + m.x611 - m.x790 >= -336)

m.c2062 = Constraint(expr= - 336*m.b74 + m.x612 - m.x791 >= -336)

m.c2063 = Constraint(expr= - 336*m.b76 + m.x614 - m.x793 >= -336)

m.c2064 = Constraint(expr= - 336*m.b77 + m.x615 - m.x794 >= -336)

m.c2065 = Constraint(expr= - 336*m.b79 + m.x617 - m.x796 >= -336)

m.c2066 = Constraint(expr= - 336*m.b80 + m.x618 - m.x797 >= -336)

m.c2067 = Constraint(expr= - 336*m.b82 + m.x620 - m.x799 >= -336)

m.c2068 = Constraint(expr= - 336*m.b83 + m.x621 - m.x800 >= -336)

m.c2069 = Constraint(expr= - 336*m.b73 + m.x623 - m.x790 >= -336)

m.c2070 = Constraint(expr= - 336*m.b74 + m.x624 - m.x791 >= -336)

m.c2071 = Constraint(expr= - 336*m.b76 + m.x626 - m.x793 >= -336)

m.c2072 = Constraint(expr= - 336*m.b77 + m.x627 - m.x794 >= -336)

m.c2073 = Constraint(expr= - 336*m.b79 + m.x629 - m.x796 >= -336)

m.c2074 = Constraint(expr= - 336*m.b80 + m.x630 - m.x797 >= -336)

m.c2075 = Constraint(expr= - 336*m.b82 + m.x632 - m.x799 >= -336)

m.c2076 = Constraint(expr= - 336*m.b83 + m.x633 - m.x800 >= -336)

m.c2077 = Constraint(expr= - 336*m.b73 + m.x635 - m.x790 >= -336)

m.c2078 = Constraint(expr= - 336*m.b74 + m.x636 - m.x791 >= -336)

m.c2079 = Constraint(expr= - 336*m.b76 + m.x638 - m.x793 >= -336)

m.c2080 = Constraint(expr= - 336*m.b77 + m.x639 - m.x794 >= -336)

m.c2081 = Constraint(expr= - 336*m.b79 + m.x641 - m.x796 >= -336)

m.c2082 = Constraint(expr= - 336*m.b80 + m.x642 - m.x797 >= -336)

m.c2083 = Constraint(expr= - 336*m.b82 + m.x644 - m.x799 >= -336)

m.c2084 = Constraint(expr= - 336*m.b83 + m.x645 - m.x800 >= -336)

m.c2085 = Constraint(expr= - 336*m.b73 + m.x683 - m.x790 >= -336)

m.c2086 = Constraint(expr= - 336*m.b74 + m.x684 - m.x791 >= -336)

m.c2087 = Constraint(expr= - 336*m.b76 + m.x686 - m.x793 >= -336)

m.c2088 = Constraint(expr= - 336*m.b77 + m.x687 - m.x794 >= -336)

m.c2089 = Constraint(expr= - 336*m.b79 + m.x689 - m.x796 >= -336)

m.c2090 = Constraint(expr= - 336*m.b80 + m.x690 - m.x797 >= -336)

m.c2091 = Constraint(expr= - 336*m.b82 + m.x692 - m.x799 >= -336)

m.c2092 = Constraint(expr= - 336*m.b83 + m.x693 - m.x800 >= -336)

m.c2093 = Constraint(expr= - 336*m.b73 + m.x707 - m.x790 >= -336)

m.c2094 = Constraint(expr= - 336*m.b74 + m.x708 - m.x791 >= -336)

m.c2095 = Constraint(expr= - 336*m.b76 + m.x710 - m.x793 >= -336)

m.c2096 = Constraint(expr= - 336*m.b77 + m.x711 - m.x794 >= -336)

m.c2097 = Constraint(expr= - 336*m.b79 + m.x713 - m.x796 >= -336)

m.c2098 = Constraint(expr= - 336*m.b80 + m.x714 - m.x797 >= -336)

m.c2099 = Constraint(expr= - 336*m.b82 + m.x716 - m.x799 >= -336)

m.c2100 = Constraint(expr= - 336*m.b83 + m.x717 - m.x800 >= -336)

m.c2101 = Constraint(expr= - 336*m.b85 + m.x575 - m.x802 >= -336)

m.c2102 = Constraint(expr= - 336*m.b86 + m.x576 - m.x803 >= -336)

m.c2103 = Constraint(expr= - 336*m.b88 + m.x578 - m.x805 >= -336)

m.c2104 = Constraint(expr= - 336*m.b89 + m.x579 - m.x806 >= -336)

m.c2105 = Constraint(expr= - 336*m.b91 + m.x581 - m.x808 >= -336)

m.c2106 = Constraint(expr= - 336*m.b92 + m.x582 - m.x809 >= -336)

m.c2107 = Constraint(expr= - 336*m.b94 + m.x584 - m.x811 >= -336)

m.c2108 = Constraint(expr= - 336*m.b95 + m.x585 - m.x812 >= -336)

m.c2109 = Constraint(expr= - 336*m.b85 + m.x587 - m.x802 >= -336)

m.c2110 = Constraint(expr= - 336*m.b86 + m.x588 - m.x803 >= -336)

m.c2111 = Constraint(expr= - 336*m.b88 + m.x590 - m.x805 >= -336)

m.c2112 = Constraint(expr= - 336*m.b89 + m.x591 - m.x806 >= -336)

m.c2113 = Constraint(expr= - 336*m.b91 + m.x593 - m.x808 >= -336)

m.c2114 = Constraint(expr= - 336*m.b92 + m.x594 - m.x809 >= -336)

m.c2115 = Constraint(expr= - 336*m.b94 + m.x596 - m.x811 >= -336)

m.c2116 = Constraint(expr= - 336*m.b95 + m.x597 - m.x812 >= -336)

m.c2117 = Constraint(expr= - 336*m.b85 + m.x599 - m.x802 >= -336)

m.c2118 = Constraint(expr= - 336*m.b86 + m.x600 - m.x803 >= -336)

m.c2119 = Constraint(expr= - 336*m.b88 + m.x602 - m.x805 >= -336)

m.c2120 = Constraint(expr= - 336*m.b89 + m.x603 - m.x806 >= -336)

m.c2121 = Constraint(expr= - 336*m.b91 + m.x605 - m.x808 >= -336)

m.c2122 = Constraint(expr= - 336*m.b92 + m.x606 - m.x809 >= -336)

m.c2123 = Constraint(expr= - 336*m.b94 + m.x608 - m.x811 >= -336)

m.c2124 = Constraint(expr= - 336*m.b95 + m.x609 - m.x812 >= -336)

m.c2125 = Constraint(expr= - 336*m.b85 + m.x671 - m.x802 >= -336)

m.c2126 = Constraint(expr= - 336*m.b86 + m.x672 - m.x803 >= -336)

m.c2127 = Constraint(expr= - 336*m.b88 + m.x674 - m.x805 >= -336)

m.c2128 = Constraint(expr= - 336*m.b89 + m.x675 - m.x806 >= -336)

m.c2129 = Constraint(expr= - 336*m.b91 + m.x677 - m.x808 >= -336)

m.c2130 = Constraint(expr= - 336*m.b92 + m.x678 - m.x809 >= -336)

m.c2131 = Constraint(expr= - 336*m.b94 + m.x680 - m.x811 >= -336)

m.c2132 = Constraint(expr= - 336*m.b95 + m.x681 - m.x812 >= -336)

m.c2133 = Constraint(expr= - 336*m.b85 + m.x695 - m.x802 >= -336)

m.c2134 = Constraint(expr= - 336*m.b86 + m.x696 - m.x803 >= -336)

m.c2135 = Constraint(expr= - 336*m.b88 + m.x698 - m.x805 >= -336)

m.c2136 = Constraint(expr= - 336*m.b89 + m.x699 - m.x806 >= -336)

m.c2137 = Constraint(expr= - 336*m.b91 + m.x701 - m.x808 >= -336)

m.c2138 = Constraint(expr= - 336*m.b92 + m.x702 - m.x809 >= -336)

m.c2139 = Constraint(expr= - 336*m.b94 + m.x704 - m.x811 >= -336)

m.c2140 = Constraint(expr= - 336*m.b95 + m.x705 - m.x812 >= -336)

m.c2141 = Constraint(expr= - 336*m.b97 + m.x575 - m.x814 >= -336)

m.c2142 = Constraint(expr= - 336*m.b98 + m.x576 - m.x815 >= -336)

m.c2143 = Constraint(expr= - 336*m.b100 + m.x578 - m.x817 >= -336)

m.c2144 = Constraint(expr= - 336*m.b101 + m.x579 - m.x818 >= -336)

m.c2145 = Constraint(expr= - 336*m.b103 + m.x581 - m.x820 >= -336)

m.c2146 = Constraint(expr= - 336*m.b104 + m.x582 - m.x821 >= -336)

m.c2147 = Constraint(expr= - 336*m.b106 + m.x584 - m.x823 >= -336)

m.c2148 = Constraint(expr= - 336*m.b107 + m.x585 - m.x824 >= -336)

m.c2149 = Constraint(expr= - 336*m.b97 + m.x587 - m.x814 >= -336)

m.c2150 = Constraint(expr= - 336*m.b98 + m.x588 - m.x815 >= -336)

m.c2151 = Constraint(expr= - 336*m.b100 + m.x590 - m.x817 >= -336)

m.c2152 = Constraint(expr= - 336*m.b101 + m.x591 - m.x818 >= -336)

m.c2153 = Constraint(expr= - 336*m.b103 + m.x593 - m.x820 >= -336)

m.c2154 = Constraint(expr= - 336*m.b104 + m.x594 - m.x821 >= -336)

m.c2155 = Constraint(expr= - 336*m.b106 + m.x596 - m.x823 >= -336)

m.c2156 = Constraint(expr= - 336*m.b107 + m.x597 - m.x824 >= -336)

m.c2157 = Constraint(expr= - 336*m.b97 + m.x599 - m.x814 >= -336)

m.c2158 = Constraint(expr= - 336*m.b98 + m.x600 - m.x815 >= -336)

m.c2159 = Constraint(expr= - 336*m.b100 + m.x602 - m.x817 >= -336)

m.c2160 = Constraint(expr= - 336*m.b101 + m.x603 - m.x818 >= -336)

m.c2161 = Constraint(expr= - 336*m.b103 + m.x605 - m.x820 >= -336)

m.c2162 = Constraint(expr= - 336*m.b104 + m.x606 - m.x821 >= -336)

m.c2163 = Constraint(expr= - 336*m.b106 + m.x608 - m.x823 >= -336)

m.c2164 = Constraint(expr= - 336*m.b107 + m.x609 - m.x824 >= -336)

m.c2165 = Constraint(expr= - 336*m.b97 + m.x659 - m.x814 >= -336)

m.c2166 = Constraint(expr= - 336*m.b98 + m.x660 - m.x815 >= -336)

m.c2167 = Constraint(expr= - 336*m.b100 + m.x662 - m.x817 >= -336)

m.c2168 = Constraint(expr= - 336*m.b101 + m.x663 - m.x818 >= -336)

m.c2169 = Constraint(expr= - 336*m.b103 + m.x665 - m.x820 >= -336)

m.c2170 = Constraint(expr= - 336*m.b104 + m.x666 - m.x821 >= -336)

m.c2171 = Constraint(expr= - 336*m.b106 + m.x668 - m.x823 >= -336)

m.c2172 = Constraint(expr= - 336*m.b107 + m.x669 - m.x824 >= -336)

m.c2173 = Constraint(expr= - 336*m.b97 + m.x695 - m.x814 >= -336)

m.c2174 = Constraint(expr= - 336*m.b98 + m.x696 - m.x815 >= -336)

m.c2175 = Constraint(expr= - 336*m.b100 + m.x698 - m.x817 >= -336)

m.c2176 = Constraint(expr= - 336*m.b101 + m.x699 - m.x818 >= -336)

m.c2177 = Constraint(expr= - 336*m.b103 + m.x701 - m.x820 >= -336)

m.c2178 = Constraint(expr= - 336*m.b104 + m.x702 - m.x821 >= -336)

m.c2179 = Constraint(expr= - 336*m.b106 + m.x704 - m.x823 >= -336)

m.c2180 = Constraint(expr= - 336*m.b107 + m.x705 - m.x824 >= -336)

m.c2181 = Constraint(expr= - 336*m.b109 + m.x611 - m.x826 >= -336)

m.c2182 = Constraint(expr= - 336*m.b110 + m.x612 - m.x827 >= -336)

m.c2183 = Constraint(expr= - 336*m.b112 + m.x614 - m.x829 >= -336)

m.c2184 = Constraint(expr= - 336*m.b113 + m.x615 - m.x830 >= -336)

m.c2185 = Constraint(expr= - 336*m.b115 + m.x617 - m.x832 >= -336)

m.c2186 = Constraint(expr= - 336*m.b116 + m.x618 - m.x833 >= -336)

m.c2187 = Constraint(expr= - 336*m.b118 + m.x620 - m.x835 >= -336)

m.c2188 = Constraint(expr= - 336*m.b119 + m.x621 - m.x836 >= -336)

m.c2189 = Constraint(expr= - 336*m.b109 + m.x623 - m.x826 >= -336)

m.c2190 = Constraint(expr= - 336*m.b110 + m.x624 - m.x827 >= -336)

m.c2191 = Constraint(expr= - 336*m.b112 + m.x626 - m.x829 >= -336)

m.c2192 = Constraint(expr= - 336*m.b113 + m.x627 - m.x830 >= -336)

m.c2193 = Constraint(expr= - 336*m.b115 + m.x629 - m.x832 >= -336)

m.c2194 = Constraint(expr= - 336*m.b116 + m.x630 - m.x833 >= -336)

m.c2195 = Constraint(expr= - 336*m.b118 + m.x632 - m.x835 >= -336)

m.c2196 = Constraint(expr= - 336*m.b119 + m.x633 - m.x836 >= -336)

m.c2197 = Constraint(expr= - 336*m.b109 + m.x635 - m.x826 >= -336)

m.c2198 = Constraint(expr= - 336*m.b110 + m.x636 - m.x827 >= -336)

m.c2199 = Constraint(expr= - 336*m.b112 + m.x638 - m.x829 >= -336)

m.c2200 = Constraint(expr= - 336*m.b113 + m.x639 - m.x830 >= -336)

m.c2201 = Constraint(expr= - 336*m.b115 + m.x641 - m.x832 >= -336)

m.c2202 = Constraint(expr= - 336*m.b116 + m.x642 - m.x833 >= -336)

m.c2203 = Constraint(expr= - 336*m.b118 + m.x644 - m.x835 >= -336)

m.c2204 = Constraint(expr= - 336*m.b119 + m.x645 - m.x836 >= -336)

m.c2205 = Constraint(expr= - 336*m.b109 + m.x647 - m.x826 >= -336)

m.c2206 = Constraint(expr= - 336*m.b110 + m.x648 - m.x827 >= -336)

m.c2207 = Constraint(expr= - 336*m.b112 + m.x650 - m.x829 >= -336)

m.c2208 = Constraint(expr= - 336*m.b113 + m.x651 - m.x830 >= -336)

m.c2209 = Constraint(expr= - 336*m.b115 + m.x653 - m.x832 >= -336)

m.c2210 = Constraint(expr= - 336*m.b116 + m.x654 - m.x833 >= -336)

m.c2211 = Constraint(expr= - 336*m.b118 + m.x656 - m.x835 >= -336)

m.c2212 = Constraint(expr= - 336*m.b119 + m.x657 - m.x836 >= -336)

m.c2213 = Constraint(expr= - 336*m.b109 + m.x707 - m.x826 >= -336)

m.c2214 = Constraint(expr= - 336*m.b110 + m.x708 - m.x827 >= -336)

m.c2215 = Constraint(expr= - 336*m.b112 + m.x710 - m.x829 >= -336)

m.c2216 = Constraint(expr= - 336*m.b113 + m.x711 - m.x830 >= -336)

m.c2217 = Constraint(expr= - 336*m.b115 + m.x713 - m.x832 >= -336)

m.c2218 = Constraint(expr= - 336*m.b116 + m.x714 - m.x833 >= -336)

m.c2219 = Constraint(expr= - 336*m.b118 + m.x716 - m.x835 >= -336)

m.c2220 = Constraint(expr= - 336*m.b119 + m.x717 - m.x836 >= -336)

m.c2221 = Constraint(expr= - 336*m.b121 + m.x575 - m.x838 >= -336)

m.c2222 = Constraint(expr= - 336*m.b122 + m.x576 - m.x839 >= -336)

m.c2223 = Constraint(expr= - 336*m.b124 + m.x578 - m.x841 >= -336)

m.c2224 = Constraint(expr= - 336*m.b125 + m.x579 - m.x842 >= -336)

m.c2225 = Constraint(expr= - 336*m.b127 + m.x581 - m.x844 >= -336)

m.c2226 = Constraint(expr= - 336*m.b128 + m.x582 - m.x845 >= -336)

m.c2227 = Constraint(expr= - 336*m.b130 + m.x584 - m.x847 >= -336)

m.c2228 = Constraint(expr= - 336*m.b131 + m.x585 - m.x848 >= -336)

m.c2229 = Constraint(expr= - 336*m.b121 + m.x587 - m.x838 >= -336)

m.c2230 = Constraint(expr= - 336*m.b122 + m.x588 - m.x839 >= -336)

m.c2231 = Constraint(expr= - 336*m.b124 + m.x590 - m.x841 >= -336)

m.c2232 = Constraint(expr= - 336*m.b125 + m.x591 - m.x842 >= -336)

m.c2233 = Constraint(expr= - 336*m.b127 + m.x593 - m.x844 >= -336)

m.c2234 = Constraint(expr= - 336*m.b128 + m.x594 - m.x845 >= -336)

m.c2235 = Constraint(expr= - 336*m.b130 + m.x596 - m.x847 >= -336)

m.c2236 = Constraint(expr= - 336*m.b131 + m.x597 - m.x848 >= -336)

m.c2237 = Constraint(expr= - 336*m.b121 + m.x599 - m.x838 >= -336)

m.c2238 = Constraint(expr= - 336*m.b122 + m.x600 - m.x839 >= -336)

m.c2239 = Constraint(expr= - 336*m.b124 + m.x602 - m.x841 >= -336)

m.c2240 = Constraint(expr= - 336*m.b125 + m.x603 - m.x842 >= -336)

m.c2241 = Constraint(expr= - 336*m.b127 + m.x605 - m.x844 >= -336)

m.c2242 = Constraint(expr= - 336*m.b128 + m.x606 - m.x845 >= -336)

m.c2243 = Constraint(expr= - 336*m.b130 + m.x608 - m.x847 >= -336)

m.c2244 = Constraint(expr= - 336*m.b131 + m.x609 - m.x848 >= -336)

m.c2245 = Constraint(expr= - 336*m.b121 + m.x659 - m.x838 >= -336)

m.c2246 = Constraint(expr= - 336*m.b122 + m.x660 - m.x839 >= -336)

m.c2247 = Constraint(expr= - 336*m.b124 + m.x662 - m.x841 >= -336)

m.c2248 = Constraint(expr= - 336*m.b125 + m.x663 - m.x842 >= -336)

m.c2249 = Constraint(expr= - 336*m.b127 + m.x665 - m.x844 >= -336)

m.c2250 = Constraint(expr= - 336*m.b128 + m.x666 - m.x845 >= -336)

m.c2251 = Constraint(expr= - 336*m.b130 + m.x668 - m.x847 >= -336)

m.c2252 = Constraint(expr= - 336*m.b131 + m.x669 - m.x848 >= -336)

m.c2253 = Constraint(expr= - 336*m.b121 + m.x671 - m.x838 >= -336)

m.c2254 = Constraint(expr= - 336*m.b122 + m.x672 - m.x839 >= -336)

m.c2255 = Constraint(expr= - 336*m.b124 + m.x674 - m.x841 >= -336)

m.c2256 = Constraint(expr= - 336*m.b125 + m.x675 - m.x842 >= -336)

m.c2257 = Constraint(expr= - 336*m.b127 + m.x677 - m.x844 >= -336)

m.c2258 = Constraint(expr= - 336*m.b128 + m.x678 - m.x845 >= -336)

m.c2259 = Constraint(expr= - 336*m.b130 + m.x680 - m.x847 >= -336)

m.c2260 = Constraint(expr= - 336*m.b131 + m.x681 - m.x848 >= -336)

m.c2261 = Constraint(expr= - 336*m.b133 + m.x611 - m.x850 >= -336)

m.c2262 = Constraint(expr= - 336*m.b134 + m.x612 - m.x851 >= -336)

m.c2263 = Constraint(expr= - 336*m.b136 + m.x614 - m.x853 >= -336)

m.c2264 = Constraint(expr= - 336*m.b137 + m.x615 - m.x854 >= -336)

m.c2265 = Constraint(expr= - 336*m.b139 + m.x617 - m.x856 >= -336)

m.c2266 = Constraint(expr= - 336*m.b140 + m.x618 - m.x857 >= -336)

m.c2267 = Constraint(expr= - 336*m.b142 + m.x620 - m.x859 >= -336)

m.c2268 = Constraint(expr= - 336*m.b143 + m.x621 - m.x860 >= -336)

m.c2269 = Constraint(expr= - 336*m.b133 + m.x623 - m.x850 >= -336)

m.c2270 = Constraint(expr= - 336*m.b134 + m.x624 - m.x851 >= -336)

m.c2271 = Constraint(expr= - 336*m.b136 + m.x626 - m.x853 >= -336)

m.c2272 = Constraint(expr= - 336*m.b137 + m.x627 - m.x854 >= -336)

m.c2273 = Constraint(expr= - 336*m.b139 + m.x629 - m.x856 >= -336)

m.c2274 = Constraint(expr= - 336*m.b140 + m.x630 - m.x857 >= -336)

m.c2275 = Constraint(expr= - 336*m.b142 + m.x632 - m.x859 >= -336)

m.c2276 = Constraint(expr= - 336*m.b143 + m.x633 - m.x860 >= -336)

m.c2277 = Constraint(expr= - 336*m.b133 + m.x635 - m.x850 >= -336)

m.c2278 = Constraint(expr= - 336*m.b134 + m.x636 - m.x851 >= -336)

m.c2279 = Constraint(expr= - 336*m.b136 + m.x638 - m.x853 >= -336)

m.c2280 = Constraint(expr= - 336*m.b137 + m.x639 - m.x854 >= -336)

m.c2281 = Constraint(expr= - 336*m.b139 + m.x641 - m.x856 >= -336)

m.c2282 = Constraint(expr= - 336*m.b140 + m.x642 - m.x857 >= -336)

m.c2283 = Constraint(expr= - 336*m.b142 + m.x644 - m.x859 >= -336)

m.c2284 = Constraint(expr= - 336*m.b143 + m.x645 - m.x860 >= -336)

m.c2285 = Constraint(expr= - 336*m.b133 + m.x647 - m.x850 >= -336)

m.c2286 = Constraint(expr= - 336*m.b134 + m.x648 - m.x851 >= -336)

m.c2287 = Constraint(expr= - 336*m.b136 + m.x650 - m.x853 >= -336)

m.c2288 = Constraint(expr= - 336*m.b137 + m.x651 - m.x854 >= -336)

m.c2289 = Constraint(expr= - 336*m.b139 + m.x653 - m.x856 >= -336)

m.c2290 = Constraint(expr= - 336*m.b140 + m.x654 - m.x857 >= -336)

m.c2291 = Constraint(expr= - 336*m.b142 + m.x656 - m.x859 >= -336)

m.c2292 = Constraint(expr= - 336*m.b143 + m.x657 - m.x860 >= -336)

m.c2293 = Constraint(expr= - 336*m.b133 + m.x683 - m.x850 >= -336)

m.c2294 = Constraint(expr= - 336*m.b134 + m.x684 - m.x851 >= -336)

m.c2295 = Constraint(expr= - 336*m.b136 + m.x686 - m.x853 >= -336)

m.c2296 = Constraint(expr= - 336*m.b137 + m.x687 - m.x854 >= -336)

m.c2297 = Constraint(expr= - 336*m.b139 + m.x689 - m.x856 >= -336)

m.c2298 = Constraint(expr= - 336*m.b140 + m.x690 - m.x857 >= -336)

m.c2299 = Constraint(expr= - 336*m.b142 + m.x692 - m.x859 >= -336)

m.c2300 = Constraint(expr= - 336*m.b143 + m.x693 - m.x860 >= -336)

m.c2301 = Constraint(expr=   336*m.b1 + 336*m.b2 + m.x575 - m.x718 <= 672)

m.c2302 = Constraint(expr=   336*m.b2 + 336*m.b3 + m.x576 - m.x719 <= 672)

m.c2303 = Constraint(expr=   336*m.b1 + 336*m.b5 + m.x578 - m.x718 <= 672)

m.c2304 = Constraint(expr=   336*m.b2 + 336*m.b6 + m.x579 - m.x719 <= 672)

m.c2305 = Constraint(expr=   336*m.b1 + 336*m.b8 + m.x581 - m.x718 <= 672)

m.c2306 = Constraint(expr=   336*m.b2 + 336*m.b9 + m.x582 - m.x719 <= 672)

m.c2307 = Constraint(expr=   336*m.b1 + 336*m.b11 + m.x584 - m.x718 <= 672)

m.c2308 = Constraint(expr=   336*m.b2 + 336*m.b12 + m.x585 - m.x719 <= 672)

m.c2309 = Constraint(expr=   336*m.b2 + 336*m.b4 + m.x575 - m.x721 <= 672)

m.c2310 = Constraint(expr=   336*m.b3 + 336*m.b5 + m.x576 - m.x722 <= 672)

m.c2311 = Constraint(expr=   336*m.b4 + 336*m.b5 + m.x578 - m.x721 <= 672)

m.c2312 = Constraint(expr=   336*m.b5 + 336*m.b6 + m.x579 - m.x722 <= 672)

m.c2313 = Constraint(expr=   336*m.b4 + 336*m.b8 + m.x581 - m.x721 <= 672)

m.c2314 = Constraint(expr=   336*m.b5 + 336*m.b9 + m.x582 - m.x722 <= 672)

m.c2315 = Constraint(expr=   336*m.b4 + 336*m.b11 + m.x584 - m.x721 <= 672)

m.c2316 = Constraint(expr=   336*m.b5 + 336*m.b12 + m.x585 - m.x722 <= 672)

m.c2317 = Constraint(expr=   336*m.b2 + 336*m.b7 + m.x575 - m.x724 <= 672)

m.c2318 = Constraint(expr=   336*m.b3 + 336*m.b8 + m.x576 - m.x725 <= 672)

m.c2319 = Constraint(expr=   336*m.b5 + 336*m.b7 + m.x578 - m.x724 <= 672)

m.c2320 = Constraint(expr=   336*m.b6 + 336*m.b8 + m.x579 - m.x725 <= 672)

m.c2321 = Constraint(expr=   336*m.b7 + 336*m.b8 + m.x581 - m.x724 <= 672)

m.c2322 = Constraint(expr=   336*m.b8 + 336*m.b9 + m.x582 - m.x725 <= 672)

m.c2323 = Constraint(expr=   336*m.b7 + 336*m.b11 + m.x584 - m.x724 <= 672)

m.c2324 = Constraint(expr=   336*m.b8 + 336*m.b12 + m.x585 - m.x725 <= 672)

m.c2325 = Constraint(expr=   336*m.b2 + 336*m.b10 + m.x575 - m.x727 <= 672)

m.c2326 = Constraint(expr=   336*m.b3 + 336*m.b11 + m.x576 - m.x728 <= 672)

m.c2327 = Constraint(expr=   336*m.b5 + 336*m.b10 + m.x578 - m.x727 <= 672)

m.c2328 = Constraint(expr=   336*m.b6 + 336*m.b11 + m.x579 - m.x728 <= 672)

m.c2329 = Constraint(expr=   336*m.b8 + 336*m.b10 + m.x581 - m.x727 <= 672)

m.c2330 = Constraint(expr=   336*m.b9 + 336*m.b11 + m.x582 - m.x728 <= 672)

m.c2331 = Constraint(expr=   336*m.b10 + 336*m.b11 + m.x584 - m.x727 <= 672)

m.c2332 = Constraint(expr=   336*m.b11 + 336*m.b12 + m.x585 - m.x728 <= 672)

m.c2333 = Constraint(expr=   336*m.b13 + 336*m.b14 + m.x587 - m.x730 <= 672)

m.c2334 = Constraint(expr=   336*m.b14 + 336*m.b15 + m.x588 - m.x731 <= 672)

m.c2335 = Constraint(expr=   336*m.b13 + 336*m.b17 + m.x590 - m.x730 <= 672)

m.c2336 = Constraint(expr=   336*m.b14 + 336*m.b18 + m.x591 - m.x731 <= 672)

m.c2337 = Constraint(expr=   336*m.b13 + 336*m.b20 + m.x593 - m.x730 <= 672)

m.c2338 = Constraint(expr=   336*m.b14 + 336*m.b21 + m.x594 - m.x731 <= 672)

m.c2339 = Constraint(expr=   336*m.b13 + 336*m.b23 + m.x596 - m.x730 <= 672)

m.c2340 = Constraint(expr=   336*m.b14 + 336*m.b24 + m.x597 - m.x731 <= 672)

m.c2341 = Constraint(expr=   336*m.b14 + 336*m.b16 + m.x587 - m.x733 <= 672)

m.c2342 = Constraint(expr=   336*m.b15 + 336*m.b17 + m.x588 - m.x734 <= 672)

m.c2343 = Constraint(expr=   336*m.b16 + 336*m.b17 + m.x590 - m.x733 <= 672)

m.c2344 = Constraint(expr=   336*m.b17 + 336*m.b18 + m.x591 - m.x734 <= 672)

m.c2345 = Constraint(expr=   336*m.b16 + 336*m.b20 + m.x593 - m.x733 <= 672)

m.c2346 = Constraint(expr=   336*m.b17 + 336*m.b21 + m.x594 - m.x734 <= 672)

m.c2347 = Constraint(expr=   336*m.b16 + 336*m.b23 + m.x596 - m.x733 <= 672)

m.c2348 = Constraint(expr=   336*m.b17 + 336*m.b24 + m.x597 - m.x734 <= 672)

m.c2349 = Constraint(expr=   336*m.b14 + 336*m.b19 + m.x587 - m.x736 <= 672)

m.c2350 = Constraint(expr=   336*m.b15 + 336*m.b20 + m.x588 - m.x737 <= 672)

m.c2351 = Constraint(expr=   336*m.b17 + 336*m.b19 + m.x590 - m.x736 <= 672)

m.c2352 = Constraint(expr=   336*m.b18 + 336*m.b20 + m.x591 - m.x737 <= 672)

m.c2353 = Constraint(expr=   336*m.b19 + 336*m.b20 + m.x593 - m.x736 <= 672)

m.c2354 = Constraint(expr=   336*m.b20 + 336*m.b21 + m.x594 - m.x737 <= 672)

m.c2355 = Constraint(expr=   336*m.b19 + 336*m.b23 + m.x596 - m.x736 <= 672)

m.c2356 = Constraint(expr=   336*m.b20 + 336*m.b24 + m.x597 - m.x737 <= 672)

m.c2357 = Constraint(expr=   336*m.b14 + 336*m.b22 + m.x587 - m.x739 <= 672)

m.c2358 = Constraint(expr=   336*m.b15 + 336*m.b23 + m.x588 - m.x740 <= 672)

m.c2359 = Constraint(expr=   336*m.b17 + 336*m.b22 + m.x590 - m.x739 <= 672)

m.c2360 = Constraint(expr=   336*m.b18 + 336*m.b23 + m.x591 - m.x740 <= 672)

m.c2361 = Constraint(expr=   336*m.b20 + 336*m.b22 + m.x593 - m.x739 <= 672)

m.c2362 = Constraint(expr=   336*m.b21 + 336*m.b23 + m.x594 - m.x740 <= 672)

m.c2363 = Constraint(expr=   336*m.b22 + 336*m.b23 + m.x596 - m.x739 <= 672)

m.c2364 = Constraint(expr=   336*m.b23 + 336*m.b24 + m.x597 - m.x740 <= 672)

m.c2365 = Constraint(expr=   336*m.b25 + 336*m.b26 + m.x599 - m.x742 <= 672)

m.c2366 = Constraint(expr=   336*m.b26 + 336*m.b27 + m.x600 - m.x743 <= 672)

m.c2367 = Constraint(expr=   336*m.b25 + 336*m.b29 + m.x602 - m.x742 <= 672)

m.c2368 = Constraint(expr=   336*m.b26 + 336*m.b30 + m.x603 - m.x743 <= 672)

m.c2369 = Constraint(expr=   336*m.b25 + 336*m.b32 + m.x605 - m.x742 <= 672)

m.c2370 = Constraint(expr=   336*m.b26 + 336*m.b33 + m.x606 - m.x743 <= 672)

m.c2371 = Constraint(expr=   336*m.b25 + 336*m.b35 + m.x608 - m.x742 <= 672)

m.c2372 = Constraint(expr=   336*m.b26 + 336*m.b36 + m.x609 - m.x743 <= 672)

m.c2373 = Constraint(expr=   336*m.b26 + 336*m.b28 + m.x599 - m.x745 <= 672)

m.c2374 = Constraint(expr=   336*m.b27 + 336*m.b29 + m.x600 - m.x746 <= 672)

m.c2375 = Constraint(expr=   336*m.b28 + 336*m.b29 + m.x602 - m.x745 <= 672)

m.c2376 = Constraint(expr=   336*m.b29 + 336*m.b30 + m.x603 - m.x746 <= 672)

m.c2377 = Constraint(expr=   336*m.b28 + 336*m.b32 + m.x605 - m.x745 <= 672)

m.c2378 = Constraint(expr=   336*m.b29 + 336*m.b33 + m.x606 - m.x746 <= 672)

m.c2379 = Constraint(expr=   336*m.b28 + 336*m.b35 + m.x608 - m.x745 <= 672)

m.c2380 = Constraint(expr=   336*m.b29 + 336*m.b36 + m.x609 - m.x746 <= 672)

m.c2381 = Constraint(expr=   336*m.b26 + 336*m.b31 + m.x599 - m.x748 <= 672)

m.c2382 = Constraint(expr=   336*m.b27 + 336*m.b32 + m.x600 - m.x749 <= 672)

m.c2383 = Constraint(expr=   336*m.b29 + 336*m.b31 + m.x602 - m.x748 <= 672)

m.c2384 = Constraint(expr=   336*m.b30 + 336*m.b32 + m.x603 - m.x749 <= 672)

m.c2385 = Constraint(expr=   336*m.b31 + 336*m.b32 + m.x605 - m.x748 <= 672)

m.c2386 = Constraint(expr=   336*m.b32 + 336*m.b33 + m.x606 - m.x749 <= 672)

m.c2387 = Constraint(expr=   336*m.b31 + 336*m.b35 + m.x608 - m.x748 <= 672)

m.c2388 = Constraint(expr=   336*m.b32 + 336*m.b36 + m.x609 - m.x749 <= 672)

m.c2389 = Constraint(expr=   336*m.b26 + 336*m.b34 + m.x599 - m.x751 <= 672)

m.c2390 = Constraint(expr=   336*m.b27 + 336*m.b35 + m.x600 - m.x752 <= 672)

m.c2391 = Constraint(expr=   336*m.b29 + 336*m.b34 + m.x602 - m.x751 <= 672)

m.c2392 = Constraint(expr=   336*m.b30 + 336*m.b35 + m.x603 - m.x752 <= 672)

m.c2393 = Constraint(expr=   336*m.b32 + 336*m.b34 + m.x605 - m.x751 <= 672)

m.c2394 = Constraint(expr=   336*m.b33 + 336*m.b35 + m.x606 - m.x752 <= 672)

m.c2395 = Constraint(expr=   336*m.b34 + 336*m.b35 + m.x608 - m.x751 <= 672)

m.c2396 = Constraint(expr=   336*m.b35 + 336*m.b36 + m.x609 - m.x752 <= 672)

m.c2397 = Constraint(expr=   336*m.b37 + 336*m.b38 + m.x611 - m.x754 <= 672)

m.c2398 = Constraint(expr=   336*m.b38 + 336*m.b39 + m.x612 - m.x755 <= 672)

m.c2399 = Constraint(expr=   336*m.b37 + 336*m.b41 + m.x614 - m.x754 <= 672)

m.c2400 = Constraint(expr=   336*m.b38 + 336*m.b42 + m.x615 - m.x755 <= 672)

m.c2401 = Constraint(expr=   336*m.b37 + 336*m.b44 + m.x617 - m.x754 <= 672)

m.c2402 = Constraint(expr=   336*m.b38 + 336*m.b45 + m.x618 - m.x755 <= 672)

m.c2403 = Constraint(expr=   336*m.b37 + 336*m.b47 + m.x620 - m.x754 <= 672)

m.c2404 = Constraint(expr=   336*m.b38 + 336*m.b48 + m.x621 - m.x755 <= 672)

m.c2405 = Constraint(expr=   336*m.b38 + 336*m.b40 + m.x611 - m.x757 <= 672)

m.c2406 = Constraint(expr=   336*m.b39 + 336*m.b41 + m.x612 - m.x758 <= 672)

m.c2407 = Constraint(expr=   336*m.b40 + 336*m.b41 + m.x614 - m.x757 <= 672)

m.c2408 = Constraint(expr=   336*m.b41 + 336*m.b42 + m.x615 - m.x758 <= 672)

m.c2409 = Constraint(expr=   336*m.b40 + 336*m.b44 + m.x617 - m.x757 <= 672)

m.c2410 = Constraint(expr=   336*m.b41 + 336*m.b45 + m.x618 - m.x758 <= 672)

m.c2411 = Constraint(expr=   336*m.b40 + 336*m.b47 + m.x620 - m.x757 <= 672)

m.c2412 = Constraint(expr=   336*m.b41 + 336*m.b48 + m.x621 - m.x758 <= 672)

m.c2413 = Constraint(expr=   336*m.b38 + 336*m.b43 + m.x611 - m.x760 <= 672)

m.c2414 = Constraint(expr=   336*m.b39 + 336*m.b44 + m.x612 - m.x761 <= 672)

m.c2415 = Constraint(expr=   336*m.b41 + 336*m.b43 + m.x614 - m.x760 <= 672)

m.c2416 = Constraint(expr=   336*m.b42 + 336*m.b44 + m.x615 - m.x761 <= 672)

m.c2417 = Constraint(expr=   336*m.b43 + 336*m.b44 + m.x617 - m.x760 <= 672)

m.c2418 = Constraint(expr=   336*m.b44 + 336*m.b45 + m.x618 - m.x761 <= 672)

m.c2419 = Constraint(expr=   336*m.b43 + 336*m.b47 + m.x620 - m.x760 <= 672)

m.c2420 = Constraint(expr=   336*m.b44 + 336*m.b48 + m.x621 - m.x761 <= 672)

m.c2421 = Constraint(expr=   336*m.b38 + 336*m.b46 + m.x611 - m.x763 <= 672)

m.c2422 = Constraint(expr=   336*m.b39 + 336*m.b47 + m.x612 - m.x764 <= 672)

m.c2423 = Constraint(expr=   336*m.b41 + 336*m.b46 + m.x614 - m.x763 <= 672)

m.c2424 = Constraint(expr=   336*m.b42 + 336*m.b47 + m.x615 - m.x764 <= 672)

m.c2425 = Constraint(expr=   336*m.b44 + 336*m.b46 + m.x617 - m.x763 <= 672)

m.c2426 = Constraint(expr=   336*m.b45 + 336*m.b47 + m.x618 - m.x764 <= 672)

m.c2427 = Constraint(expr=   336*m.b46 + 336*m.b47 + m.x620 - m.x763 <= 672)

m.c2428 = Constraint(expr=   336*m.b47 + 336*m.b48 + m.x621 - m.x764 <= 672)

m.c2429 = Constraint(expr=   336*m.b49 + 336*m.b50 + m.x623 - m.x766 <= 672)

m.c2430 = Constraint(expr=   336*m.b50 + 336*m.b51 + m.x624 - m.x767 <= 672)

m.c2431 = Constraint(expr=   336*m.b49 + 336*m.b53 + m.x626 - m.x766 <= 672)

m.c2432 = Constraint(expr=   336*m.b50 + 336*m.b54 + m.x627 - m.x767 <= 672)

m.c2433 = Constraint(expr=   336*m.b49 + 336*m.b56 + m.x629 - m.x766 <= 672)

m.c2434 = Constraint(expr=   336*m.b50 + 336*m.b57 + m.x630 - m.x767 <= 672)

m.c2435 = Constraint(expr=   336*m.b49 + 336*m.b59 + m.x632 - m.x766 <= 672)

m.c2436 = Constraint(expr=   336*m.b50 + 336*m.b60 + m.x633 - m.x767 <= 672)

m.c2437 = Constraint(expr=   336*m.b50 + 336*m.b52 + m.x623 - m.x769 <= 672)

m.c2438 = Constraint(expr=   336*m.b51 + 336*m.b53 + m.x624 - m.x770 <= 672)

m.c2439 = Constraint(expr=   336*m.b52 + 336*m.b53 + m.x626 - m.x769 <= 672)

m.c2440 = Constraint(expr=   336*m.b53 + 336*m.b54 + m.x627 - m.x770 <= 672)

m.c2441 = Constraint(expr=   336*m.b52 + 336*m.b56 + m.x629 - m.x769 <= 672)

m.c2442 = Constraint(expr=   336*m.b53 + 336*m.b57 + m.x630 - m.x770 <= 672)

m.c2443 = Constraint(expr=   336*m.b52 + 336*m.b59 + m.x632 - m.x769 <= 672)

m.c2444 = Constraint(expr=   336*m.b53 + 336*m.b60 + m.x633 - m.x770 <= 672)

m.c2445 = Constraint(expr=   336*m.b50 + 336*m.b55 + m.x623 - m.x772 <= 672)

m.c2446 = Constraint(expr=   336*m.b51 + 336*m.b56 + m.x624 - m.x773 <= 672)

m.c2447 = Constraint(expr=   336*m.b53 + 336*m.b55 + m.x626 - m.x772 <= 672)

m.c2448 = Constraint(expr=   336*m.b54 + 336*m.b56 + m.x627 - m.x773 <= 672)

m.c2449 = Constraint(expr=   336*m.b55 + 336*m.b56 + m.x629 - m.x772 <= 672)

m.c2450 = Constraint(expr=   336*m.b56 + 336*m.b57 + m.x630 - m.x773 <= 672)

m.c2451 = Constraint(expr=   336*m.b55 + 336*m.b59 + m.x632 - m.x772 <= 672)

m.c2452 = Constraint(expr=   336*m.b56 + 336*m.b60 + m.x633 - m.x773 <= 672)

m.c2453 = Constraint(expr=   336*m.b50 + 336*m.b58 + m.x623 - m.x775 <= 672)

m.c2454 = Constraint(expr=   336*m.b51 + 336*m.b59 + m.x624 - m.x776 <= 672)

m.c2455 = Constraint(expr=   336*m.b53 + 336*m.b58 + m.x626 - m.x775 <= 672)

m.c2456 = Constraint(expr=   336*m.b54 + 336*m.b59 + m.x627 - m.x776 <= 672)

m.c2457 = Constraint(expr=   336*m.b56 + 336*m.b58 + m.x629 - m.x775 <= 672)

m.c2458 = Constraint(expr=   336*m.b57 + 336*m.b59 + m.x630 - m.x776 <= 672)

m.c2459 = Constraint(expr=   336*m.b58 + 336*m.b59 + m.x632 - m.x775 <= 672)

m.c2460 = Constraint(expr=   336*m.b59 + 336*m.b60 + m.x633 - m.x776 <= 672)

m.c2461 = Constraint(expr=   336*m.b61 + 336*m.b62 + m.x635 - m.x778 <= 672)

m.c2462 = Constraint(expr=   336*m.b62 + 336*m.b63 + m.x636 - m.x779 <= 672)

m.c2463 = Constraint(expr=   336*m.b61 + 336*m.b65 + m.x638 - m.x778 <= 672)

m.c2464 = Constraint(expr=   336*m.b62 + 336*m.b66 + m.x639 - m.x779 <= 672)

m.c2465 = Constraint(expr=   336*m.b61 + 336*m.b68 + m.x641 - m.x778 <= 672)

m.c2466 = Constraint(expr=   336*m.b62 + 336*m.b69 + m.x642 - m.x779 <= 672)

m.c2467 = Constraint(expr=   336*m.b61 + 336*m.b71 + m.x644 - m.x778 <= 672)

m.c2468 = Constraint(expr=   336*m.b62 + 336*m.b72 + m.x645 - m.x779 <= 672)

m.c2469 = Constraint(expr=   336*m.b62 + 336*m.b64 + m.x635 - m.x781 <= 672)

m.c2470 = Constraint(expr=   336*m.b63 + 336*m.b65 + m.x636 - m.x782 <= 672)

m.c2471 = Constraint(expr=   336*m.b64 + 336*m.b65 + m.x638 - m.x781 <= 672)

m.c2472 = Constraint(expr=   336*m.b65 + 336*m.b66 + m.x639 - m.x782 <= 672)

m.c2473 = Constraint(expr=   336*m.b64 + 336*m.b68 + m.x641 - m.x781 <= 672)

m.c2474 = Constraint(expr=   336*m.b65 + 336*m.b69 + m.x642 - m.x782 <= 672)

m.c2475 = Constraint(expr=   336*m.b64 + 336*m.b71 + m.x644 - m.x781 <= 672)

m.c2476 = Constraint(expr=   336*m.b65 + 336*m.b72 + m.x645 - m.x782 <= 672)

m.c2477 = Constraint(expr=   336*m.b62 + 336*m.b67 + m.x635 - m.x784 <= 672)

m.c2478 = Constraint(expr=   336*m.b63 + 336*m.b68 + m.x636 - m.x785 <= 672)

m.c2479 = Constraint(expr=   336*m.b65 + 336*m.b67 + m.x638 - m.x784 <= 672)

m.c2480 = Constraint(expr=   336*m.b66 + 336*m.b68 + m.x639 - m.x785 <= 672)

m.c2481 = Constraint(expr=   336*m.b67 + 336*m.b68 + m.x641 - m.x784 <= 672)

m.c2482 = Constraint(expr=   336*m.b68 + 336*m.b69 + m.x642 - m.x785 <= 672)

m.c2483 = Constraint(expr=   336*m.b67 + 336*m.b71 + m.x644 - m.x784 <= 672)

m.c2484 = Constraint(expr=   336*m.b68 + 336*m.b72 + m.x645 - m.x785 <= 672)

m.c2485 = Constraint(expr=   336*m.b62 + 336*m.b70 + m.x635 - m.x787 <= 672)

m.c2486 = Constraint(expr=   336*m.b63 + 336*m.b71 + m.x636 - m.x788 <= 672)

m.c2487 = Constraint(expr=   336*m.b65 + 336*m.b70 + m.x638 - m.x787 <= 672)

m.c2488 = Constraint(expr=   336*m.b66 + 336*m.b71 + m.x639 - m.x788 <= 672)

m.c2489 = Constraint(expr=   336*m.b68 + 336*m.b70 + m.x641 - m.x787 <= 672)

m.c2490 = Constraint(expr=   336*m.b69 + 336*m.b71 + m.x642 - m.x788 <= 672)

m.c2491 = Constraint(expr=   336*m.b70 + 336*m.b71 + m.x644 - m.x787 <= 672)

m.c2492 = Constraint(expr=   336*m.b71 + 336*m.b72 + m.x645 - m.x788 <= 672)

m.c2493 = Constraint(expr=   336*m.b73 + 336*m.b74 + m.x647 - m.x790 <= 672)

m.c2494 = Constraint(expr=   336*m.b74 + 336*m.b75 + m.x648 - m.x791 <= 672)

m.c2495 = Constraint(expr=   336*m.b73 + 336*m.b77 + m.x650 - m.x790 <= 672)

m.c2496 = Constraint(expr=   336*m.b74 + 336*m.b78 + m.x651 - m.x791 <= 672)

m.c2497 = Constraint(expr=   336*m.b73 + 336*m.b80 + m.x653 - m.x790 <= 672)

m.c2498 = Constraint(expr=   336*m.b74 + 336*m.b81 + m.x654 - m.x791 <= 672)

m.c2499 = Constraint(expr=   336*m.b73 + 336*m.b83 + m.x656 - m.x790 <= 672)

m.c2500 = Constraint(expr=   336*m.b74 + 336*m.b84 + m.x657 - m.x791 <= 672)

m.c2501 = Constraint(expr=   336*m.b74 + 336*m.b76 + m.x647 - m.x793 <= 672)

m.c2502 = Constraint(expr=   336*m.b75 + 336*m.b77 + m.x648 - m.x794 <= 672)

m.c2503 = Constraint(expr=   336*m.b76 + 336*m.b77 + m.x650 - m.x793 <= 672)

m.c2504 = Constraint(expr=   336*m.b77 + 336*m.b78 + m.x651 - m.x794 <= 672)

m.c2505 = Constraint(expr=   336*m.b76 + 336*m.b80 + m.x653 - m.x793 <= 672)

m.c2506 = Constraint(expr=   336*m.b77 + 336*m.b81 + m.x654 - m.x794 <= 672)

m.c2507 = Constraint(expr=   336*m.b76 + 336*m.b83 + m.x656 - m.x793 <= 672)

m.c2508 = Constraint(expr=   336*m.b77 + 336*m.b84 + m.x657 - m.x794 <= 672)

m.c2509 = Constraint(expr=   336*m.b74 + 336*m.b79 + m.x647 - m.x796 <= 672)

m.c2510 = Constraint(expr=   336*m.b75 + 336*m.b80 + m.x648 - m.x797 <= 672)

m.c2511 = Constraint(expr=   336*m.b77 + 336*m.b79 + m.x650 - m.x796 <= 672)

m.c2512 = Constraint(expr=   336*m.b78 + 336*m.b80 + m.x651 - m.x797 <= 672)

m.c2513 = Constraint(expr=   336*m.b79 + 336*m.b80 + m.x653 - m.x796 <= 672)

m.c2514 = Constraint(expr=   336*m.b80 + 336*m.b81 + m.x654 - m.x797 <= 672)

m.c2515 = Constraint(expr=   336*m.b79 + 336*m.b83 + m.x656 - m.x796 <= 672)

m.c2516 = Constraint(expr=   336*m.b80 + 336*m.b84 + m.x657 - m.x797 <= 672)

m.c2517 = Constraint(expr=   336*m.b74 + 336*m.b82 + m.x647 - m.x799 <= 672)

m.c2518 = Constraint(expr=   336*m.b75 + 336*m.b83 + m.x648 - m.x800 <= 672)

m.c2519 = Constraint(expr=   336*m.b77 + 336*m.b82 + m.x650 - m.x799 <= 672)

m.c2520 = Constraint(expr=   336*m.b78 + 336*m.b83 + m.x651 - m.x800 <= 672)

m.c2521 = Constraint(expr=   336*m.b80 + 336*m.b82 + m.x653 - m.x799 <= 672)

m.c2522 = Constraint(expr=   336*m.b81 + 336*m.b83 + m.x654 - m.x800 <= 672)

m.c2523 = Constraint(expr=   336*m.b82 + 336*m.b83 + m.x656 - m.x799 <= 672)

m.c2524 = Constraint(expr=   336*m.b83 + 336*m.b84 + m.x657 - m.x800 <= 672)

m.c2525 = Constraint(expr=   336*m.b85 + 336*m.b86 + m.x659 - m.x802 <= 672)

m.c2526 = Constraint(expr=   336*m.b86 + 336*m.b87 + m.x660 - m.x803 <= 672)

m.c2527 = Constraint(expr=   336*m.b85 + 336*m.b89 + m.x662 - m.x802 <= 672)

m.c2528 = Constraint(expr=   336*m.b86 + 336*m.b90 + m.x663 - m.x803 <= 672)

m.c2529 = Constraint(expr=   336*m.b85 + 336*m.b92 + m.x665 - m.x802 <= 672)

m.c2530 = Constraint(expr=   336*m.b86 + 336*m.b93 + m.x666 - m.x803 <= 672)

m.c2531 = Constraint(expr=   336*m.b85 + 336*m.b95 + m.x668 - m.x802 <= 672)

m.c2532 = Constraint(expr=   336*m.b86 + 336*m.b96 + m.x669 - m.x803 <= 672)

m.c2533 = Constraint(expr=   336*m.b86 + 336*m.b88 + m.x659 - m.x805 <= 672)

m.c2534 = Constraint(expr=   336*m.b87 + 336*m.b89 + m.x660 - m.x806 <= 672)

m.c2535 = Constraint(expr=   336*m.b88 + 336*m.b89 + m.x662 - m.x805 <= 672)

m.c2536 = Constraint(expr=   336*m.b89 + 336*m.b90 + m.x663 - m.x806 <= 672)

m.c2537 = Constraint(expr=   336*m.b88 + 336*m.b92 + m.x665 - m.x805 <= 672)

m.c2538 = Constraint(expr=   336*m.b89 + 336*m.b93 + m.x666 - m.x806 <= 672)

m.c2539 = Constraint(expr=   336*m.b88 + 336*m.b95 + m.x668 - m.x805 <= 672)

m.c2540 = Constraint(expr=   336*m.b89 + 336*m.b96 + m.x669 - m.x806 <= 672)

m.c2541 = Constraint(expr=   336*m.b86 + 336*m.b91 + m.x659 - m.x808 <= 672)

m.c2542 = Constraint(expr=   336*m.b87 + 336*m.b92 + m.x660 - m.x809 <= 672)

m.c2543 = Constraint(expr=   336*m.b89 + 336*m.b91 + m.x662 - m.x808 <= 672)

m.c2544 = Constraint(expr=   336*m.b90 + 336*m.b92 + m.x663 - m.x809 <= 672)

m.c2545 = Constraint(expr=   336*m.b91 + 336*m.b92 + m.x665 - m.x808 <= 672)

m.c2546 = Constraint(expr=   336*m.b92 + 336*m.b93 + m.x666 - m.x809 <= 672)

m.c2547 = Constraint(expr=   336*m.b91 + 336*m.b95 + m.x668 - m.x808 <= 672)

m.c2548 = Constraint(expr=   336*m.b92 + 336*m.b96 + m.x669 - m.x809 <= 672)

m.c2549 = Constraint(expr=   336*m.b86 + 336*m.b94 + m.x659 - m.x811 <= 672)

m.c2550 = Constraint(expr=   336*m.b87 + 336*m.b95 + m.x660 - m.x812 <= 672)

m.c2551 = Constraint(expr=   336*m.b89 + 336*m.b94 + m.x662 - m.x811 <= 672)

m.c2552 = Constraint(expr=   336*m.b90 + 336*m.b95 + m.x663 - m.x812 <= 672)

m.c2553 = Constraint(expr=   336*m.b92 + 336*m.b94 + m.x665 - m.x811 <= 672)

m.c2554 = Constraint(expr=   336*m.b93 + 336*m.b95 + m.x666 - m.x812 <= 672)

m.c2555 = Constraint(expr=   336*m.b94 + 336*m.b95 + m.x668 - m.x811 <= 672)

m.c2556 = Constraint(expr=   336*m.b95 + 336*m.b96 + m.x669 - m.x812 <= 672)

m.c2557 = Constraint(expr=   336*m.b97 + 336*m.b98 + m.x671 - m.x814 <= 672)

m.c2558 = Constraint(expr=   336*m.b98 + 336*m.b99 + m.x672 - m.x815 <= 672)

m.c2559 = Constraint(expr=   336*m.b97 + 336*m.b101 + m.x674 - m.x814 <= 672)

m.c2560 = Constraint(expr=   336*m.b98 + 336*m.b102 + m.x675 - m.x815 <= 672)

m.c2561 = Constraint(expr=   336*m.b97 + 336*m.b104 + m.x677 - m.x814 <= 672)

m.c2562 = Constraint(expr=   336*m.b98 + 336*m.b105 + m.x678 - m.x815 <= 672)

m.c2563 = Constraint(expr=   336*m.b97 + 336*m.b107 + m.x680 - m.x814 <= 672)

m.c2564 = Constraint(expr=   336*m.b98 + 336*m.b108 + m.x681 - m.x815 <= 672)

m.c2565 = Constraint(expr=   336*m.b98 + 336*m.b100 + m.x671 - m.x817 <= 672)

m.c2566 = Constraint(expr=   336*m.b99 + 336*m.b101 + m.x672 - m.x818 <= 672)

m.c2567 = Constraint(expr=   336*m.b100 + 336*m.b101 + m.x674 - m.x817 <= 672)

m.c2568 = Constraint(expr=   336*m.b101 + 336*m.b102 + m.x675 - m.x818 <= 672)

m.c2569 = Constraint(expr=   336*m.b100 + 336*m.b104 + m.x677 - m.x817 <= 672)

m.c2570 = Constraint(expr=   336*m.b101 + 336*m.b105 + m.x678 - m.x818 <= 672)

m.c2571 = Constraint(expr=   336*m.b100 + 336*m.b107 + m.x680 - m.x817 <= 672)

m.c2572 = Constraint(expr=   336*m.b101 + 336*m.b108 + m.x681 - m.x818 <= 672)

m.c2573 = Constraint(expr=   336*m.b98 + 336*m.b103 + m.x671 - m.x820 <= 672)

m.c2574 = Constraint(expr=   336*m.b99 + 336*m.b104 + m.x672 - m.x821 <= 672)

m.c2575 = Constraint(expr=   336*m.b101 + 336*m.b103 + m.x674 - m.x820 <= 672)

m.c2576 = Constraint(expr=   336*m.b102 + 336*m.b104 + m.x675 - m.x821 <= 672)

m.c2577 = Constraint(expr=   336*m.b103 + 336*m.b104 + m.x677 - m.x820 <= 672)

m.c2578 = Constraint(expr=   336*m.b104 + 336*m.b105 + m.x678 - m.x821 <= 672)

m.c2579 = Constraint(expr=   336*m.b103 + 336*m.b107 + m.x680 - m.x820 <= 672)

m.c2580 = Constraint(expr=   336*m.b104 + 336*m.b108 + m.x681 - m.x821 <= 672)

m.c2581 = Constraint(expr=   336*m.b98 + 336*m.b106 + m.x671 - m.x823 <= 672)

m.c2582 = Constraint(expr=   336*m.b99 + 336*m.b107 + m.x672 - m.x824 <= 672)

m.c2583 = Constraint(expr=   336*m.b101 + 336*m.b106 + m.x674 - m.x823 <= 672)

m.c2584 = Constraint(expr=   336*m.b102 + 336*m.b107 + m.x675 - m.x824 <= 672)

m.c2585 = Constraint(expr=   336*m.b104 + 336*m.b106 + m.x677 - m.x823 <= 672)

m.c2586 = Constraint(expr=   336*m.b105 + 336*m.b107 + m.x678 - m.x824 <= 672)

m.c2587 = Constraint(expr=   336*m.b106 + 336*m.b107 + m.x680 - m.x823 <= 672)

m.c2588 = Constraint(expr=   336*m.b107 + 336*m.b108 + m.x681 - m.x824 <= 672)

m.c2589 = Constraint(expr=   336*m.b109 + 336*m.b110 + m.x683 - m.x826 <= 672)

m.c2590 = Constraint(expr=   336*m.b110 + 336*m.b111 + m.x684 - m.x827 <= 672)

m.c2591 = Constraint(expr=   336*m.b109 + 336*m.b113 + m.x686 - m.x826 <= 672)

m.c2592 = Constraint(expr=   336*m.b110 + 336*m.b114 + m.x687 - m.x827 <= 672)

m.c2593 = Constraint(expr=   336*m.b109 + 336*m.b116 + m.x689 - m.x826 <= 672)

m.c2594 = Constraint(expr=   336*m.b110 + 336*m.b117 + m.x690 - m.x827 <= 672)

m.c2595 = Constraint(expr=   336*m.b109 + 336*m.b119 + m.x692 - m.x826 <= 672)

m.c2596 = Constraint(expr=   336*m.b110 + 336*m.b120 + m.x693 - m.x827 <= 672)

m.c2597 = Constraint(expr=   336*m.b110 + 336*m.b112 + m.x683 - m.x829 <= 672)

m.c2598 = Constraint(expr=   336*m.b111 + 336*m.b113 + m.x684 - m.x830 <= 672)

m.c2599 = Constraint(expr=   336*m.b112 + 336*m.b113 + m.x686 - m.x829 <= 672)

m.c2600 = Constraint(expr=   336*m.b113 + 336*m.b114 + m.x687 - m.x830 <= 672)

m.c2601 = Constraint(expr=   336*m.b112 + 336*m.b116 + m.x689 - m.x829 <= 672)

m.c2602 = Constraint(expr=   336*m.b113 + 336*m.b117 + m.x690 - m.x830 <= 672)

m.c2603 = Constraint(expr=   336*m.b112 + 336*m.b119 + m.x692 - m.x829 <= 672)

m.c2604 = Constraint(expr=   336*m.b113 + 336*m.b120 + m.x693 - m.x830 <= 672)

m.c2605 = Constraint(expr=   336*m.b110 + 336*m.b115 + m.x683 - m.x832 <= 672)

m.c2606 = Constraint(expr=   336*m.b111 + 336*m.b116 + m.x684 - m.x833 <= 672)

m.c2607 = Constraint(expr=   336*m.b113 + 336*m.b115 + m.x686 - m.x832 <= 672)

m.c2608 = Constraint(expr=   336*m.b114 + 336*m.b116 + m.x687 - m.x833 <= 672)

m.c2609 = Constraint(expr=   336*m.b115 + 336*m.b116 + m.x689 - m.x832 <= 672)

m.c2610 = Constraint(expr=   336*m.b116 + 336*m.b117 + m.x690 - m.x833 <= 672)

m.c2611 = Constraint(expr=   336*m.b115 + 336*m.b119 + m.x692 - m.x832 <= 672)

m.c2612 = Constraint(expr=   336*m.b116 + 336*m.b120 + m.x693 - m.x833 <= 672)

m.c2613 = Constraint(expr=   336*m.b110 + 336*m.b118 + m.x683 - m.x835 <= 672)

m.c2614 = Constraint(expr=   336*m.b111 + 336*m.b119 + m.x684 - m.x836 <= 672)

m.c2615 = Constraint(expr=   336*m.b113 + 336*m.b118 + m.x686 - m.x835 <= 672)

m.c2616 = Constraint(expr=   336*m.b114 + 336*m.b119 + m.x687 - m.x836 <= 672)

m.c2617 = Constraint(expr=   336*m.b116 + 336*m.b118 + m.x689 - m.x835 <= 672)

m.c2618 = Constraint(expr=   336*m.b117 + 336*m.b119 + m.x690 - m.x836 <= 672)

m.c2619 = Constraint(expr=   336*m.b118 + 336*m.b119 + m.x692 - m.x835 <= 672)

m.c2620 = Constraint(expr=   336*m.b119 + 336*m.b120 + m.x693 - m.x836 <= 672)

m.c2621 = Constraint(expr=   336*m.b121 + 336*m.b122 + m.x695 - m.x838 <= 672)

m.c2622 = Constraint(expr=   336*m.b122 + 336*m.b123 + m.x696 - m.x839 <= 672)

m.c2623 = Constraint(expr=   336*m.b121 + 336*m.b125 + m.x698 - m.x838 <= 672)

m.c2624 = Constraint(expr=   336*m.b122 + 336*m.b126 + m.x699 - m.x839 <= 672)

m.c2625 = Constraint(expr=   336*m.b121 + 336*m.b128 + m.x701 - m.x838 <= 672)

m.c2626 = Constraint(expr=   336*m.b122 + 336*m.b129 + m.x702 - m.x839 <= 672)

m.c2627 = Constraint(expr=   336*m.b121 + 336*m.b131 + m.x704 - m.x838 <= 672)

m.c2628 = Constraint(expr=   336*m.b122 + 336*m.b132 + m.x705 - m.x839 <= 672)

m.c2629 = Constraint(expr=   336*m.b122 + 336*m.b124 + m.x695 - m.x841 <= 672)

m.c2630 = Constraint(expr=   336*m.b123 + 336*m.b125 + m.x696 - m.x842 <= 672)

m.c2631 = Constraint(expr=   336*m.b124 + 336*m.b125 + m.x698 - m.x841 <= 672)

m.c2632 = Constraint(expr=   336*m.b125 + 336*m.b126 + m.x699 - m.x842 <= 672)

m.c2633 = Constraint(expr=   336*m.b124 + 336*m.b128 + m.x701 - m.x841 <= 672)

m.c2634 = Constraint(expr=   336*m.b125 + 336*m.b129 + m.x702 - m.x842 <= 672)

m.c2635 = Constraint(expr=   336*m.b124 + 336*m.b131 + m.x704 - m.x841 <= 672)

m.c2636 = Constraint(expr=   336*m.b125 + 336*m.b132 + m.x705 - m.x842 <= 672)

m.c2637 = Constraint(expr=   336*m.b122 + 336*m.b127 + m.x695 - m.x844 <= 672)

m.c2638 = Constraint(expr=   336*m.b123 + 336*m.b128 + m.x696 - m.x845 <= 672)

m.c2639 = Constraint(expr=   336*m.b125 + 336*m.b127 + m.x698 - m.x844 <= 672)

m.c2640 = Constraint(expr=   336*m.b126 + 336*m.b128 + m.x699 - m.x845 <= 672)

m.c2641 = Constraint(expr=   336*m.b127 + 336*m.b128 + m.x701 - m.x844 <= 672)

m.c2642 = Constraint(expr=   336*m.b128 + 336*m.b129 + m.x702 - m.x845 <= 672)

m.c2643 = Constraint(expr=   336*m.b127 + 336*m.b131 + m.x704 - m.x844 <= 672)

m.c2644 = Constraint(expr=   336*m.b128 + 336*m.b132 + m.x705 - m.x845 <= 672)

m.c2645 = Constraint(expr=   336*m.b122 + 336*m.b130 + m.x695 - m.x847 <= 672)

m.c2646 = Constraint(expr=   336*m.b123 + 336*m.b131 + m.x696 - m.x848 <= 672)

m.c2647 = Constraint(expr=   336*m.b125 + 336*m.b130 + m.x698 - m.x847 <= 672)

m.c2648 = Constraint(expr=   336*m.b126 + 336*m.b131 + m.x699 - m.x848 <= 672)

m.c2649 = Constraint(expr=   336*m.b128 + 336*m.b130 + m.x701 - m.x847 <= 672)

m.c2650 = Constraint(expr=   336*m.b129 + 336*m.b131 + m.x702 - m.x848 <= 672)

m.c2651 = Constraint(expr=   336*m.b130 + 336*m.b131 + m.x704 - m.x847 <= 672)

m.c2652 = Constraint(expr=   336*m.b131 + 336*m.b132 + m.x705 - m.x848 <= 672)

m.c2653 = Constraint(expr=   336*m.b133 + 336*m.b134 + m.x707 - m.x850 <= 672)

m.c2654 = Constraint(expr=   336*m.b134 + 336*m.b135 + m.x708 - m.x851 <= 672)

m.c2655 = Constraint(expr=   336*m.b133 + 336*m.b137 + m.x710 - m.x850 <= 672)

m.c2656 = Constraint(expr=   336*m.b134 + 336*m.b138 + m.x711 - m.x851 <= 672)

m.c2657 = Constraint(expr=   336*m.b133 + 336*m.b140 + m.x713 - m.x850 <= 672)

m.c2658 = Constraint(expr=   336*m.b134 + 336*m.b141 + m.x714 - m.x851 <= 672)

m.c2659 = Constraint(expr=   336*m.b133 + 336*m.b143 + m.x716 - m.x850 <= 672)

m.c2660 = Constraint(expr=   336*m.b134 + 336*m.b144 + m.x717 - m.x851 <= 672)

m.c2661 = Constraint(expr=   336*m.b134 + 336*m.b136 + m.x707 - m.x853 <= 672)

m.c2662 = Constraint(expr=   336*m.b135 + 336*m.b137 + m.x708 - m.x854 <= 672)

m.c2663 = Constraint(expr=   336*m.b136 + 336*m.b137 + m.x710 - m.x853 <= 672)

m.c2664 = Constraint(expr=   336*m.b137 + 336*m.b138 + m.x711 - m.x854 <= 672)

m.c2665 = Constraint(expr=   336*m.b136 + 336*m.b140 + m.x713 - m.x853 <= 672)

m.c2666 = Constraint(expr=   336*m.b137 + 336*m.b141 + m.x714 - m.x854 <= 672)

m.c2667 = Constraint(expr=   336*m.b136 + 336*m.b143 + m.x716 - m.x853 <= 672)

m.c2668 = Constraint(expr=   336*m.b137 + 336*m.b144 + m.x717 - m.x854 <= 672)

m.c2669 = Constraint(expr=   336*m.b134 + 336*m.b139 + m.x707 - m.x856 <= 672)

m.c2670 = Constraint(expr=   336*m.b135 + 336*m.b140 + m.x708 - m.x857 <= 672)

m.c2671 = Constraint(expr=   336*m.b137 + 336*m.b139 + m.x710 - m.x856 <= 672)

m.c2672 = Constraint(expr=   336*m.b138 + 336*m.b140 + m.x711 - m.x857 <= 672)

m.c2673 = Constraint(expr=   336*m.b139 + 336*m.b140 + m.x713 - m.x856 <= 672)

m.c2674 = Constraint(expr=   336*m.b140 + 336*m.b141 + m.x714 - m.x857 <= 672)

m.c2675 = Constraint(expr=   336*m.b139 + 336*m.b143 + m.x716 - m.x856 <= 672)

m.c2676 = Constraint(expr=   336*m.b140 + 336*m.b144 + m.x717 - m.x857 <= 672)

m.c2677 = Constraint(expr=   336*m.b134 + 336*m.b142 + m.x707 - m.x859 <= 672)

m.c2678 = Constraint(expr=   336*m.b135 + 336*m.b143 + m.x708 - m.x860 <= 672)

m.c2679 = Constraint(expr=   336*m.b137 + 336*m.b142 + m.x710 - m.x859 <= 672)

m.c2680 = Constraint(expr=   336*m.b138 + 336*m.b143 + m.x711 - m.x860 <= 672)

m.c2681 = Constraint(expr=   336*m.b140 + 336*m.b142 + m.x713 - m.x859 <= 672)

m.c2682 = Constraint(expr=   336*m.b141 + 336*m.b143 + m.x714 - m.x860 <= 672)

m.c2683 = Constraint(expr=   336*m.b142 + 336*m.b143 + m.x716 - m.x859 <= 672)

m.c2684 = Constraint(expr=   336*m.b143 + 336*m.b144 + m.x717 - m.x860 <= 672)

m.c2685 = Constraint(expr=   m.x863 - m.x898 >= 0)

m.c2686 = Constraint(expr=   m.x864 - m.x899 >= 0)

m.c2687 = Constraint(expr=   m.x866 - m.x901 >= 0)

m.c2688 = Constraint(expr=   m.x867 - m.x902 >= 0)

m.c2689 = Constraint(expr=   m.x869 - m.x904 >= 0)

m.c2690 = Constraint(expr=   m.x870 - m.x905 >= 0)

m.c2691 = Constraint(expr=   m.x872 - m.x907 >= 0)

m.c2692 = Constraint(expr=   m.x873 - m.x908 >= 0)

m.c2693 = Constraint(expr=   m.x875 - m.x910 >= 0)

m.c2694 = Constraint(expr=   m.x876 - m.x911 >= 0)

m.c2695 = Constraint(expr=   m.x878 - m.x913 >= 0)

m.c2696 = Constraint(expr=   m.x879 - m.x914 >= 0)

m.c2697 = Constraint(expr=   m.x881 - m.x916 >= 0)

m.c2698 = Constraint(expr=   m.x882 - m.x917 >= 0)

m.c2699 = Constraint(expr=   m.x884 - m.x919 >= 0)

m.c2700 = Constraint(expr=   m.x885 - m.x920 >= 0)

m.c2701 = Constraint(expr=   m.x887 - m.x922 >= 0)

m.c2702 = Constraint(expr=   m.x888 - m.x923 >= 0)

m.c2703 = Constraint(expr=   m.x890 - m.x925 >= 0)

m.c2704 = Constraint(expr=   m.x891 - m.x926 >= 0)

m.c2705 = Constraint(expr=   m.x893 - m.x928 >= 0)

m.c2706 = Constraint(expr=   m.x894 - m.x929 >= 0)

m.c2707 = Constraint(expr=   m.x896 - m.x931 >= 0)

m.c2708 = Constraint(expr=   m.x897 - m.x932 >= 0)

m.c2709 = Constraint(expr= - 336*m.b181 + m.x575 - m.x898 >= -336)

m.c2710 = Constraint(expr= - 336*m.b182 + m.x576 - m.x899 >= -336)

m.c2711 = Constraint(expr= - 336*m.b208 + m.x578 - m.x925 >= -336)

m.c2712 = Constraint(expr= - 336*m.b209 + m.x579 - m.x926 >= -336)

m.c2713 = Constraint(expr= - 336*m.b211 + m.x581 - m.x928 >= -336)

m.c2714 = Constraint(expr= - 336*m.b212 + m.x582 - m.x929 >= -336)

m.c2715 = Constraint(expr= - 336*m.b214 + m.x584 - m.x931 >= -336)

m.c2716 = Constraint(expr= - 336*m.b215 + m.x585 - m.x932 >= -336)

m.c2717 = Constraint(expr= - 336*m.b181 + m.x587 - m.x898 >= -336)

m.c2718 = Constraint(expr= - 336*m.b182 + m.x588 - m.x899 >= -336)

m.c2719 = Constraint(expr= - 336*m.b208 + m.x590 - m.x925 >= -336)

m.c2720 = Constraint(expr= - 336*m.b209 + m.x591 - m.x926 >= -336)

m.c2721 = Constraint(expr= - 336*m.b211 + m.x593 - m.x928 >= -336)

m.c2722 = Constraint(expr= - 336*m.b212 + m.x594 - m.x929 >= -336)

m.c2723 = Constraint(expr= - 336*m.b214 + m.x596 - m.x931 >= -336)

m.c2724 = Constraint(expr= - 336*m.b215 + m.x597 - m.x932 >= -336)

m.c2725 = Constraint(expr= - 336*m.b181 + m.x599 - m.x898 >= -336)

m.c2726 = Constraint(expr= - 336*m.b182 + m.x600 - m.x899 >= -336)

m.c2727 = Constraint(expr= - 336*m.b208 + m.x602 - m.x925 >= -336)

m.c2728 = Constraint(expr= - 336*m.b209 + m.x603 - m.x926 >= -336)

m.c2729 = Constraint(expr= - 336*m.b211 + m.x605 - m.x928 >= -336)

m.c2730 = Constraint(expr= - 336*m.b212 + m.x606 - m.x929 >= -336)

m.c2731 = Constraint(expr= - 336*m.b214 + m.x608 - m.x931 >= -336)

m.c2732 = Constraint(expr= - 336*m.b215 + m.x609 - m.x932 >= -336)

m.c2733 = Constraint(expr= - 336*m.b184 + m.x611 - m.x901 >= -336)

m.c2734 = Constraint(expr= - 336*m.b185 + m.x612 - m.x902 >= -336)

m.c2735 = Constraint(expr= - 336*m.b187 + m.x611 - m.x904 >= -336)

m.c2736 = Constraint(expr= - 336*m.b188 + m.x612 - m.x905 >= -336)

m.c2737 = Constraint(expr= - 336*m.b190 + m.x614 - m.x907 >= -336)

m.c2738 = Constraint(expr= - 336*m.b191 + m.x615 - m.x908 >= -336)

m.c2739 = Constraint(expr= - 336*m.b193 + m.x614 - m.x910 >= -336)

m.c2740 = Constraint(expr= - 336*m.b194 + m.x615 - m.x911 >= -336)

m.c2741 = Constraint(expr= - 336*m.b196 + m.x617 - m.x913 >= -336)

m.c2742 = Constraint(expr= - 336*m.b197 + m.x618 - m.x914 >= -336)

m.c2743 = Constraint(expr= - 336*m.b199 + m.x617 - m.x916 >= -336)

m.c2744 = Constraint(expr= - 336*m.b200 + m.x618 - m.x917 >= -336)

m.c2745 = Constraint(expr= - 336*m.b202 + m.x620 - m.x919 >= -336)

m.c2746 = Constraint(expr= - 336*m.b203 + m.x621 - m.x920 >= -336)

m.c2747 = Constraint(expr= - 336*m.b205 + m.x620 - m.x922 >= -336)

m.c2748 = Constraint(expr= - 336*m.b206 + m.x621 - m.x923 >= -336)

m.c2749 = Constraint(expr= - 336*m.b184 + m.x623 - m.x901 >= -336)

m.c2750 = Constraint(expr= - 336*m.b185 + m.x624 - m.x902 >= -336)

m.c2751 = Constraint(expr= - 336*m.b187 + m.x623 - m.x904 >= -336)

m.c2752 = Constraint(expr= - 336*m.b188 + m.x624 - m.x905 >= -336)

m.c2753 = Constraint(expr= - 336*m.b190 + m.x626 - m.x907 >= -336)

m.c2754 = Constraint(expr= - 336*m.b191 + m.x627 - m.x908 >= -336)

m.c2755 = Constraint(expr= - 336*m.b193 + m.x626 - m.x910 >= -336)

m.c2756 = Constraint(expr= - 336*m.b194 + m.x627 - m.x911 >= -336)

m.c2757 = Constraint(expr= - 336*m.b196 + m.x629 - m.x913 >= -336)

m.c2758 = Constraint(expr= - 336*m.b197 + m.x630 - m.x914 >= -336)

m.c2759 = Constraint(expr= - 336*m.b199 + m.x629 - m.x916 >= -336)

m.c2760 = Constraint(expr= - 336*m.b200 + m.x630 - m.x917 >= -336)

m.c2761 = Constraint(expr= - 336*m.b202 + m.x632 - m.x919 >= -336)

m.c2762 = Constraint(expr= - 336*m.b203 + m.x633 - m.x920 >= -336)

m.c2763 = Constraint(expr= - 336*m.b205 + m.x632 - m.x922 >= -336)

m.c2764 = Constraint(expr= - 336*m.b206 + m.x633 - m.x923 >= -336)

m.c2765 = Constraint(expr= - 336*m.b184 + m.x635 - m.x901 >= -336)

m.c2766 = Constraint(expr= - 336*m.b185 + m.x636 - m.x902 >= -336)

m.c2767 = Constraint(expr= - 336*m.b187 + m.x635 - m.x904 >= -336)

m.c2768 = Constraint(expr= - 336*m.b188 + m.x636 - m.x905 >= -336)

m.c2769 = Constraint(expr= - 336*m.b190 + m.x638 - m.x907 >= -336)

m.c2770 = Constraint(expr= - 336*m.b191 + m.x639 - m.x908 >= -336)

m.c2771 = Constraint(expr= - 336*m.b193 + m.x638 - m.x910 >= -336)

m.c2772 = Constraint(expr= - 336*m.b194 + m.x639 - m.x911 >= -336)

m.c2773 = Constraint(expr= - 336*m.b196 + m.x641 - m.x913 >= -336)

m.c2774 = Constraint(expr= - 336*m.b197 + m.x642 - m.x914 >= -336)

m.c2775 = Constraint(expr= - 336*m.b199 + m.x641 - m.x916 >= -336)

m.c2776 = Constraint(expr= - 336*m.b200 + m.x642 - m.x917 >= -336)

m.c2777 = Constraint(expr= - 336*m.b202 + m.x644 - m.x919 >= -336)

m.c2778 = Constraint(expr= - 336*m.b203 + m.x645 - m.x920 >= -336)

m.c2779 = Constraint(expr= - 336*m.b205 + m.x644 - m.x922 >= -336)

m.c2780 = Constraint(expr= - 336*m.b206 + m.x645 - m.x923 >= -336)

m.c2781 = Constraint(expr= - 336*m.b184 + m.x647 - m.x901 >= -336)

m.c2782 = Constraint(expr= - 336*m.b185 + m.x648 - m.x902 >= -336)

m.c2783 = Constraint(expr= - 336*m.b187 + m.x647 - m.x904 >= -336)

m.c2784 = Constraint(expr= - 336*m.b188 + m.x648 - m.x905 >= -336)

m.c2785 = Constraint(expr= - 336*m.b190 + m.x650 - m.x907 >= -336)

m.c2786 = Constraint(expr= - 336*m.b191 + m.x651 - m.x908 >= -336)

m.c2787 = Constraint(expr= - 336*m.b193 + m.x650 - m.x910 >= -336)

m.c2788 = Constraint(expr= - 336*m.b194 + m.x651 - m.x911 >= -336)

m.c2789 = Constraint(expr= - 336*m.b196 + m.x653 - m.x913 >= -336)

m.c2790 = Constraint(expr= - 336*m.b197 + m.x654 - m.x914 >= -336)

m.c2791 = Constraint(expr= - 336*m.b199 + m.x653 - m.x916 >= -336)

m.c2792 = Constraint(expr= - 336*m.b200 + m.x654 - m.x917 >= -336)

m.c2793 = Constraint(expr= - 336*m.b202 + m.x656 - m.x919 >= -336)

m.c2794 = Constraint(expr= - 336*m.b203 + m.x657 - m.x920 >= -336)

m.c2795 = Constraint(expr= - 336*m.b205 + m.x656 - m.x922 >= -336)

m.c2796 = Constraint(expr= - 336*m.b206 + m.x657 - m.x923 >= -336)

m.c2797 = Constraint(expr= - 336*m.b181 + m.x659 - m.x898 >= -336)

m.c2798 = Constraint(expr= - 336*m.b182 + m.x660 - m.x899 >= -336)

m.c2799 = Constraint(expr= - 336*m.b208 + m.x662 - m.x925 >= -336)

m.c2800 = Constraint(expr= - 336*m.b209 + m.x663 - m.x926 >= -336)

m.c2801 = Constraint(expr= - 336*m.b211 + m.x665 - m.x928 >= -336)

m.c2802 = Constraint(expr= - 336*m.b212 + m.x666 - m.x929 >= -336)

m.c2803 = Constraint(expr= - 336*m.b214 + m.x668 - m.x931 >= -336)

m.c2804 = Constraint(expr= - 336*m.b215 + m.x669 - m.x932 >= -336)

m.c2805 = Constraint(expr= - 336*m.b181 + m.x671 - m.x898 >= -336)

m.c2806 = Constraint(expr= - 336*m.b182 + m.x672 - m.x899 >= -336)

m.c2807 = Constraint(expr= - 336*m.b208 + m.x674 - m.x925 >= -336)

m.c2808 = Constraint(expr= - 336*m.b209 + m.x675 - m.x926 >= -336)

m.c2809 = Constraint(expr= - 336*m.b211 + m.x677 - m.x928 >= -336)

m.c2810 = Constraint(expr= - 336*m.b212 + m.x678 - m.x929 >= -336)

m.c2811 = Constraint(expr= - 336*m.b214 + m.x680 - m.x931 >= -336)

m.c2812 = Constraint(expr= - 336*m.b215 + m.x681 - m.x932 >= -336)

m.c2813 = Constraint(expr= - 336*m.b184 + m.x683 - m.x901 >= -336)

m.c2814 = Constraint(expr= - 336*m.b185 + m.x684 - m.x902 >= -336)

m.c2815 = Constraint(expr= - 336*m.b187 + m.x683 - m.x904 >= -336)

m.c2816 = Constraint(expr= - 336*m.b188 + m.x684 - m.x905 >= -336)

m.c2817 = Constraint(expr= - 336*m.b190 + m.x686 - m.x907 >= -336)

m.c2818 = Constraint(expr= - 336*m.b191 + m.x687 - m.x908 >= -336)

m.c2819 = Constraint(expr= - 336*m.b193 + m.x686 - m.x910 >= -336)

m.c2820 = Constraint(expr= - 336*m.b194 + m.x687 - m.x911 >= -336)

m.c2821 = Constraint(expr= - 336*m.b196 + m.x689 - m.x913 >= -336)

m.c2822 = Constraint(expr= - 336*m.b197 + m.x690 - m.x914 >= -336)

m.c2823 = Constraint(expr= - 336*m.b199 + m.x689 - m.x916 >= -336)

m.c2824 = Constraint(expr= - 336*m.b200 + m.x690 - m.x917 >= -336)

m.c2825 = Constraint(expr= - 336*m.b202 + m.x692 - m.x919 >= -336)

m.c2826 = Constraint(expr= - 336*m.b203 + m.x693 - m.x920 >= -336)

m.c2827 = Constraint(expr= - 336*m.b205 + m.x692 - m.x922 >= -336)

m.c2828 = Constraint(expr= - 336*m.b206 + m.x693 - m.x923 >= -336)

m.c2829 = Constraint(expr= - 336*m.b181 + m.x695 - m.x898 >= -336)

m.c2830 = Constraint(expr= - 336*m.b182 + m.x696 - m.x899 >= -336)

m.c2831 = Constraint(expr= - 336*m.b208 + m.x698 - m.x925 >= -336)

m.c2832 = Constraint(expr= - 336*m.b209 + m.x699 - m.x926 >= -336)

m.c2833 = Constraint(expr= - 336*m.b211 + m.x701 - m.x928 >= -336)

m.c2834 = Constraint(expr= - 336*m.b212 + m.x702 - m.x929 >= -336)

m.c2835 = Constraint(expr= - 336*m.b214 + m.x704 - m.x931 >= -336)

m.c2836 = Constraint(expr= - 336*m.b215 + m.x705 - m.x932 >= -336)

m.c2837 = Constraint(expr= - 336*m.b184 + m.x707 - m.x901 >= -336)

m.c2838 = Constraint(expr= - 336*m.b185 + m.x708 - m.x902 >= -336)

m.c2839 = Constraint(expr= - 336*m.b187 + m.x707 - m.x904 >= -336)

m.c2840 = Constraint(expr= - 336*m.b188 + m.x708 - m.x905 >= -336)

m.c2841 = Constraint(expr= - 336*m.b190 + m.x710 - m.x907 >= -336)

m.c2842 = Constraint(expr= - 336*m.b191 + m.x711 - m.x908 >= -336)

m.c2843 = Constraint(expr= - 336*m.b193 + m.x710 - m.x910 >= -336)

m.c2844 = Constraint(expr= - 336*m.b194 + m.x711 - m.x911 >= -336)

m.c2845 = Constraint(expr= - 336*m.b196 + m.x713 - m.x913 >= -336)

m.c2846 = Constraint(expr= - 336*m.b197 + m.x714 - m.x914 >= -336)

m.c2847 = Constraint(expr= - 336*m.b199 + m.x713 - m.x916 >= -336)

m.c2848 = Constraint(expr= - 336*m.b200 + m.x714 - m.x917 >= -336)

m.c2849 = Constraint(expr= - 336*m.b202 + m.x716 - m.x919 >= -336)

m.c2850 = Constraint(expr= - 336*m.b203 + m.x717 - m.x920 >= -336)

m.c2851 = Constraint(expr= - 336*m.b205 + m.x716 - m.x922 >= -336)

m.c2852 = Constraint(expr= - 336*m.b206 + m.x717 - m.x923 >= -336)

m.c2853 = Constraint(expr= - 344*m.b1 - m.x718 + m.x863 >= -336)

m.c2854 = Constraint(expr= - 344*m.b2 - m.x719 + m.x864 >= -336)

m.c2855 = Constraint(expr= - 344*m.b4 - m.x721 + m.x890 >= -336)

m.c2856 = Constraint(expr= - 344*m.b5 - m.x722 + m.x891 >= -336)

m.c2857 = Constraint(expr= - 344*m.b7 - m.x724 + m.x893 >= -336)

m.c2858 = Constraint(expr= - 344*m.b8 - m.x725 + m.x894 >= -336)

m.c2859 = Constraint(expr= - 344*m.b10 - m.x727 + m.x896 >= -336)

m.c2860 = Constraint(expr= - 344*m.b11 - m.x728 + m.x897 >= -336)

m.c2861 = Constraint(expr= - 344*m.b13 - m.x730 + m.x863 >= -336)

m.c2862 = Constraint(expr= - 344*m.b14 - m.x731 + m.x864 >= -336)

m.c2863 = Constraint(expr= - 344*m.b16 - m.x733 + m.x890 >= -336)

m.c2864 = Constraint(expr= - 344*m.b17 - m.x734 + m.x891 >= -336)

m.c2865 = Constraint(expr= - 344*m.b19 - m.x736 + m.x893 >= -336)

m.c2866 = Constraint(expr= - 344*m.b20 - m.x737 + m.x894 >= -336)

m.c2867 = Constraint(expr= - 344*m.b22 - m.x739 + m.x896 >= -336)

m.c2868 = Constraint(expr= - 344*m.b23 - m.x740 + m.x897 >= -336)

m.c2869 = Constraint(expr= - 344*m.b25 - m.x742 + m.x863 >= -336)

m.c2870 = Constraint(expr= - 344*m.b26 - m.x743 + m.x864 >= -336)

m.c2871 = Constraint(expr= - 344*m.b28 - m.x745 + m.x890 >= -336)

m.c2872 = Constraint(expr= - 344*m.b29 - m.x746 + m.x891 >= -336)

m.c2873 = Constraint(expr= - 344*m.b31 - m.x748 + m.x893 >= -336)

m.c2874 = Constraint(expr= - 344*m.b32 - m.x749 + m.x894 >= -336)

m.c2875 = Constraint(expr= - 344*m.b34 - m.x751 + m.x896 >= -336)

m.c2876 = Constraint(expr= - 344*m.b35 - m.x752 + m.x897 >= -336)

m.c2877 = Constraint(expr= - 344*m.b37 - m.x754 + m.x866 >= -336)

m.c2878 = Constraint(expr= - 344*m.b38 - m.x755 + m.x867 >= -336)

m.c2879 = Constraint(expr= - 344*m.b37 - m.x754 + m.x869 >= -336)

m.c2880 = Constraint(expr= - 344*m.b38 - m.x755 + m.x870 >= -336)

m.c2881 = Constraint(expr= - 344*m.b40 - m.x757 + m.x872 >= -336)

m.c2882 = Constraint(expr= - 344*m.b41 - m.x758 + m.x873 >= -336)

m.c2883 = Constraint(expr= - 344*m.b40 - m.x757 + m.x875 >= -336)

m.c2884 = Constraint(expr= - 344*m.b41 - m.x758 + m.x876 >= -336)

m.c2885 = Constraint(expr= - 344*m.b43 - m.x760 + m.x878 >= -336)

m.c2886 = Constraint(expr= - 344*m.b44 - m.x761 + m.x879 >= -336)

m.c2887 = Constraint(expr= - 344*m.b43 - m.x760 + m.x881 >= -336)

m.c2888 = Constraint(expr= - 344*m.b44 - m.x761 + m.x882 >= -336)

m.c2889 = Constraint(expr= - 344*m.b46 - m.x763 + m.x884 >= -336)

m.c2890 = Constraint(expr= - 344*m.b47 - m.x764 + m.x885 >= -336)

m.c2891 = Constraint(expr= - 344*m.b46 - m.x763 + m.x887 >= -336)

m.c2892 = Constraint(expr= - 344*m.b47 - m.x764 + m.x888 >= -336)

m.c2893 = Constraint(expr= - 344*m.b49 - m.x766 + m.x866 >= -336)

m.c2894 = Constraint(expr= - 344*m.b50 - m.x767 + m.x867 >= -336)

m.c2895 = Constraint(expr= - 344*m.b49 - m.x766 + m.x869 >= -336)

m.c2896 = Constraint(expr= - 344*m.b50 - m.x767 + m.x870 >= -336)

m.c2897 = Constraint(expr= - 344*m.b52 - m.x769 + m.x872 >= -336)

m.c2898 = Constraint(expr= - 344*m.b53 - m.x770 + m.x873 >= -336)

m.c2899 = Constraint(expr= - 344*m.b52 - m.x769 + m.x875 >= -336)

m.c2900 = Constraint(expr= - 344*m.b53 - m.x770 + m.x876 >= -336)

m.c2901 = Constraint(expr= - 344*m.b55 - m.x772 + m.x878 >= -336)

m.c2902 = Constraint(expr= - 344*m.b56 - m.x773 + m.x879 >= -336)

m.c2903 = Constraint(expr= - 344*m.b55 - m.x772 + m.x881 >= -336)

m.c2904 = Constraint(expr= - 344*m.b56 - m.x773 + m.x882 >= -336)

m.c2905 = Constraint(expr= - 344*m.b58 - m.x775 + m.x884 >= -336)

m.c2906 = Constraint(expr= - 344*m.b59 - m.x776 + m.x885 >= -336)

m.c2907 = Constraint(expr= - 344*m.b58 - m.x775 + m.x887 >= -336)

m.c2908 = Constraint(expr= - 344*m.b59 - m.x776 + m.x888 >= -336)

m.c2909 = Constraint(expr= - 344*m.b61 - m.x778 + m.x866 >= -336)

m.c2910 = Constraint(expr= - 344*m.b62 - m.x779 + m.x867 >= -336)

m.c2911 = Constraint(expr= - 344*m.b61 - m.x778 + m.x869 >= -336)

m.c2912 = Constraint(expr= - 344*m.b62 - m.x779 + m.x870 >= -336)

m.c2913 = Constraint(expr= - 344*m.b64 - m.x781 + m.x872 >= -336)

m.c2914 = Constraint(expr= - 344*m.b65 - m.x782 + m.x873 >= -336)

m.c2915 = Constraint(expr= - 344*m.b64 - m.x781 + m.x875 >= -336)

m.c2916 = Constraint(expr= - 344*m.b65 - m.x782 + m.x876 >= -336)

m.c2917 = Constraint(expr= - 344*m.b67 - m.x784 + m.x878 >= -336)

m.c2918 = Constraint(expr= - 344*m.b68 - m.x785 + m.x879 >= -336)

m.c2919 = Constraint(expr= - 344*m.b67 - m.x784 + m.x881 >= -336)

m.c2920 = Constraint(expr= - 344*m.b68 - m.x785 + m.x882 >= -336)

m.c2921 = Constraint(expr= - 344*m.b70 - m.x787 + m.x884 >= -336)

m.c2922 = Constraint(expr= - 344*m.b71 - m.x788 + m.x885 >= -336)

m.c2923 = Constraint(expr= - 344*m.b70 - m.x787 + m.x887 >= -336)

m.c2924 = Constraint(expr= - 344*m.b71 - m.x788 + m.x888 >= -336)

m.c2925 = Constraint(expr= - 344*m.b73 - m.x790 + m.x866 >= -336)

m.c2926 = Constraint(expr= - 344*m.b74 - m.x791 + m.x867 >= -336)

m.c2927 = Constraint(expr= - 344*m.b73 - m.x790 + m.x869 >= -336)

m.c2928 = Constraint(expr= - 344*m.b74 - m.x791 + m.x870 >= -336)

m.c2929 = Constraint(expr= - 344*m.b76 - m.x793 + m.x872 >= -336)

m.c2930 = Constraint(expr= - 344*m.b77 - m.x794 + m.x873 >= -336)

m.c2931 = Constraint(expr= - 344*m.b76 - m.x793 + m.x875 >= -336)

m.c2932 = Constraint(expr= - 344*m.b77 - m.x794 + m.x876 >= -336)

m.c2933 = Constraint(expr= - 344*m.b79 - m.x796 + m.x878 >= -336)

m.c2934 = Constraint(expr= - 344*m.b80 - m.x797 + m.x879 >= -336)

m.c2935 = Constraint(expr= - 344*m.b79 - m.x796 + m.x881 >= -336)

m.c2936 = Constraint(expr= - 344*m.b80 - m.x797 + m.x882 >= -336)

m.c2937 = Constraint(expr= - 344*m.b82 - m.x799 + m.x884 >= -336)

m.c2938 = Constraint(expr= - 344*m.b83 - m.x800 + m.x885 >= -336)

m.c2939 = Constraint(expr= - 344*m.b82 - m.x799 + m.x887 >= -336)

m.c2940 = Constraint(expr= - 344*m.b83 - m.x800 + m.x888 >= -336)

m.c2941 = Constraint(expr= - 344*m.b85 - m.x802 + m.x863 >= -336)

m.c2942 = Constraint(expr= - 344*m.b86 - m.x803 + m.x864 >= -336)

m.c2943 = Constraint(expr= - 344*m.b88 - m.x805 + m.x890 >= -336)

m.c2944 = Constraint(expr= - 344*m.b89 - m.x806 + m.x891 >= -336)

m.c2945 = Constraint(expr= - 344*m.b91 - m.x808 + m.x893 >= -336)

m.c2946 = Constraint(expr= - 344*m.b92 - m.x809 + m.x894 >= -336)

m.c2947 = Constraint(expr= - 344*m.b94 - m.x811 + m.x896 >= -336)

m.c2948 = Constraint(expr= - 344*m.b95 - m.x812 + m.x897 >= -336)

m.c2949 = Constraint(expr= - 344*m.b97 - m.x814 + m.x863 >= -336)

m.c2950 = Constraint(expr= - 344*m.b98 - m.x815 + m.x864 >= -336)

m.c2951 = Constraint(expr= - 344*m.b100 - m.x817 + m.x890 >= -336)

m.c2952 = Constraint(expr= - 344*m.b101 - m.x818 + m.x891 >= -336)

m.c2953 = Constraint(expr= - 344*m.b103 - m.x820 + m.x893 >= -336)

m.c2954 = Constraint(expr= - 344*m.b104 - m.x821 + m.x894 >= -336)

m.c2955 = Constraint(expr= - 344*m.b106 - m.x823 + m.x896 >= -336)

m.c2956 = Constraint(expr= - 344*m.b107 - m.x824 + m.x897 >= -336)

m.c2957 = Constraint(expr= - 344*m.b109 - m.x826 + m.x866 >= -336)

m.c2958 = Constraint(expr= - 344*m.b110 - m.x827 + m.x867 >= -336)

m.c2959 = Constraint(expr= - 344*m.b109 - m.x826 + m.x869 >= -336)

m.c2960 = Constraint(expr= - 344*m.b110 - m.x827 + m.x870 >= -336)

m.c2961 = Constraint(expr= - 344*m.b112 - m.x829 + m.x872 >= -336)

m.c2962 = Constraint(expr= - 344*m.b113 - m.x830 + m.x873 >= -336)

m.c2963 = Constraint(expr= - 344*m.b112 - m.x829 + m.x875 >= -336)

m.c2964 = Constraint(expr= - 344*m.b113 - m.x830 + m.x876 >= -336)

m.c2965 = Constraint(expr= - 344*m.b115 - m.x832 + m.x878 >= -336)

m.c2966 = Constraint(expr= - 344*m.b116 - m.x833 + m.x879 >= -336)

m.c2967 = Constraint(expr= - 344*m.b115 - m.x832 + m.x881 >= -336)

m.c2968 = Constraint(expr= - 344*m.b116 - m.x833 + m.x882 >= -336)

m.c2969 = Constraint(expr= - 344*m.b118 - m.x835 + m.x884 >= -336)

m.c2970 = Constraint(expr= - 344*m.b119 - m.x836 + m.x885 >= -336)

m.c2971 = Constraint(expr= - 344*m.b118 - m.x835 + m.x887 >= -336)

m.c2972 = Constraint(expr= - 344*m.b119 - m.x836 + m.x888 >= -336)

m.c2973 = Constraint(expr= - 344*m.b121 - m.x838 + m.x863 >= -336)

m.c2974 = Constraint(expr= - 344*m.b122 - m.x839 + m.x864 >= -336)

m.c2975 = Constraint(expr= - 344*m.b124 - m.x841 + m.x890 >= -336)

m.c2976 = Constraint(expr= - 344*m.b125 - m.x842 + m.x891 >= -336)

m.c2977 = Constraint(expr= - 344*m.b127 - m.x844 + m.x893 >= -336)

m.c2978 = Constraint(expr= - 344*m.b128 - m.x845 + m.x894 >= -336)

m.c2979 = Constraint(expr= - 344*m.b130 - m.x847 + m.x896 >= -336)

m.c2980 = Constraint(expr= - 344*m.b131 - m.x848 + m.x897 >= -336)

m.c2981 = Constraint(expr= - 344*m.b133 - m.x850 + m.x866 >= -336)

m.c2982 = Constraint(expr= - 344*m.b134 - m.x851 + m.x867 >= -336)

m.c2983 = Constraint(expr= - 344*m.b133 - m.x850 + m.x869 >= -336)

m.c2984 = Constraint(expr= - 344*m.b134 - m.x851 + m.x870 >= -336)

m.c2985 = Constraint(expr= - 344*m.b136 - m.x853 + m.x872 >= -336)

m.c2986 = Constraint(expr= - 344*m.b137 - m.x854 + m.x873 >= -336)

m.c2987 = Constraint(expr= - 344*m.b136 - m.x853 + m.x875 >= -336)

m.c2988 = Constraint(expr= - 344*m.b137 - m.x854 + m.x876 >= -336)

m.c2989 = Constraint(expr= - 344*m.b139 - m.x856 + m.x878 >= -336)

m.c2990 = Constraint(expr= - 344*m.b140 - m.x857 + m.x879 >= -336)

m.c2991 = Constraint(expr= - 344*m.b139 - m.x856 + m.x881 >= -336)

m.c2992 = Constraint(expr= - 344*m.b140 - m.x857 + m.x882 >= -336)

m.c2993 = Constraint(expr= - 344*m.b142 - m.x859 + m.x884 >= -336)

m.c2994 = Constraint(expr= - 344*m.b143 - m.x860 + m.x885 >= -336)

m.c2995 = Constraint(expr= - 344*m.b142 - m.x859 + m.x887 >= -336)

m.c2996 = Constraint(expr= - 344*m.b143 - m.x860 + m.x888 >= -336)

m.c2997 = Constraint(expr= - 336*m.b187 + m.x866 - m.x904 >= -336)

m.c2998 = Constraint(expr= - 336*m.b188 + m.x867 - m.x905 >= -336)

m.c2999 = Constraint(expr= - 336*m.b184 + m.x869 - m.x901 >= -336)

m.c3000 = Constraint(expr= - 336*m.b185 + m.x870 - m.x902 >= -336)

m.c3001 = Constraint(expr= - 336*m.b193 + m.x872 - m.x910 >= -336)

m.c3002 = Constraint(expr= - 336*m.b194 + m.x873 - m.x911 >= -336)

m.c3003 = Constraint(expr= - 336*m.b190 + m.x875 - m.x907 >= -336)

m.c3004 = Constraint(expr= - 336*m.b191 + m.x876 - m.x908 >= -336)

m.c3005 = Constraint(expr= - 336*m.b199 + m.x878 - m.x916 >= -336)

m.c3006 = Constraint(expr= - 336*m.b200 + m.x879 - m.x917 >= -336)

m.c3007 = Constraint(expr= - 336*m.b196 + m.x881 - m.x913 >= -336)

m.c3008 = Constraint(expr= - 336*m.b197 + m.x882 - m.x914 >= -336)

m.c3009 = Constraint(expr= - 336*m.b205 + m.x884 - m.x922 >= -336)

m.c3010 = Constraint(expr= - 336*m.b206 + m.x885 - m.x923 >= -336)

m.c3011 = Constraint(expr= - 336*m.b202 + m.x887 - m.x919 >= -336)

m.c3012 = Constraint(expr= - 336*m.b203 + m.x888 - m.x920 >= -336)

m.c3013 = Constraint(expr=   m.x935 - m.x943 >= 0)

m.c3014 = Constraint(expr=   m.x936 - m.x944 >= 0)

m.c3015 = Constraint(expr=   m.x938 - m.x946 >= 0)

m.c3016 = Constraint(expr=   m.x939 - m.x947 >= 0)

m.c3017 = Constraint(expr=   m.x941 - m.x949 >= 0)

m.c3018 = Constraint(expr=   m.x942 - m.x950 >= 0)

m.c3019 = Constraint(expr= - 336*m.b181 - m.x862 + m.x940 >= -336)

m.c3020 = Constraint(expr= - 336*m.b182 - m.x863 + m.x941 >= -336)

m.c3021 = Constraint(expr= - 336*m.b183 - m.x864 + m.x942 >= -336)

m.c3022 = Constraint(expr= - 336*m.b184 - m.x865 + m.x934 >= -336)

m.c3023 = Constraint(expr= - 336*m.b185 - m.x866 + m.x935 >= -336)

m.c3024 = Constraint(expr= - 336*m.b186 - m.x867 + m.x936 >= -336)

m.c3025 = Constraint(expr= - 336*m.b187 - m.x868 + m.x937 >= -336)

m.c3026 = Constraint(expr= - 336*m.b188 - m.x869 + m.x938 >= -336)

m.c3027 = Constraint(expr= - 336*m.b189 - m.x870 + m.x939 >= -336)

m.c3028 = Constraint(expr= - 336*m.b190 - m.x871 + m.x934 >= -336)

m.c3029 = Constraint(expr= - 336*m.b191 - m.x872 + m.x935 >= -336)

m.c3030 = Constraint(expr= - 336*m.b192 - m.x873 + m.x936 >= -336)

m.c3031 = Constraint(expr= - 336*m.b193 - m.x874 + m.x937 >= -336)

m.c3032 = Constraint(expr= - 336*m.b194 - m.x875 + m.x938 >= -336)

m.c3033 = Constraint(expr= - 336*m.b195 - m.x876 + m.x939 >= -336)

m.c3034 = Constraint(expr= - 336*m.b196 - m.x877 + m.x934 >= -336)

m.c3035 = Constraint(expr= - 336*m.b197 - m.x878 + m.x935 >= -336)

m.c3036 = Constraint(expr= - 336*m.b198 - m.x879 + m.x936 >= -336)

m.c3037 = Constraint(expr= - 336*m.b199 - m.x880 + m.x937 >= -336)

m.c3038 = Constraint(expr= - 336*m.b200 - m.x881 + m.x938 >= -336)

m.c3039 = Constraint(expr= - 336*m.b201 - m.x882 + m.x939 >= -336)

m.c3040 = Constraint(expr= - 336*m.b202 - m.x883 + m.x934 >= -336)

m.c3041 = Constraint(expr= - 336*m.b203 - m.x884 + m.x935 >= -336)

m.c3042 = Constraint(expr= - 336*m.b204 - m.x885 + m.x936 >= -336)

m.c3043 = Constraint(expr= - 336*m.b205 - m.x886 + m.x937 >= -336)

m.c3044 = Constraint(expr= - 336*m.b206 - m.x887 + m.x938 >= -336)

m.c3045 = Constraint(expr= - 336*m.b207 - m.x888 + m.x939 >= -336)

m.c3046 = Constraint(expr= - 336*m.b208 - m.x889 + m.x940 >= -336)

m.c3047 = Constraint(expr= - 336*m.b209 - m.x890 + m.x941 >= -336)

m.c3048 = Constraint(expr= - 336*m.b210 - m.x891 + m.x942 >= -336)

m.c3049 = Constraint(expr= - 336*m.b211 - m.x892 + m.x940 >= -336)

m.c3050 = Constraint(expr= - 336*m.b212 - m.x893 + m.x941 >= -336)

m.c3051 = Constraint(expr= - 336*m.b213 - m.x894 + m.x942 >= -336)

m.c3052 = Constraint(expr= - 336*m.b214 - m.x895 + m.x940 >= -336)

m.c3053 = Constraint(expr= - 336*m.b215 - m.x896 + m.x941 >= -336)

m.c3054 = Constraint(expr= - 336*m.b216 - m.x897 + m.x942 >= -336)

m.c3055 = Constraint(expr=   336*m.b181 - m.x862 + m.x940 <= 336)

m.c3056 = Constraint(expr=   336*m.b182 - m.x863 + m.x941 <= 336)

m.c3057 = Constraint(expr=   336*m.b183 - m.x864 + m.x942 <= 336)

m.c3058 = Constraint(expr=   336*m.b184 - m.x865 + m.x934 <= 336)

m.c3059 = Constraint(expr=   336*m.b185 - m.x866 + m.x935 <= 336)

m.c3060 = Constraint(expr=   336*m.b186 - m.x867 + m.x936 <= 336)

m.c3061 = Constraint(expr=   336*m.b187 - m.x868 + m.x937 <= 336)

m.c3062 = Constraint(expr=   336*m.b188 - m.x869 + m.x938 <= 336)

m.c3063 = Constraint(expr=   336*m.b189 - m.x870 + m.x939 <= 336)

m.c3064 = Constraint(expr=   336*m.b190 - m.x871 + m.x934 <= 336)

m.c3065 = Constraint(expr=   336*m.b191 - m.x872 + m.x935 <= 336)

m.c3066 = Constraint(expr=   336*m.b192 - m.x873 + m.x936 <= 336)

m.c3067 = Constraint(expr=   336*m.b193 - m.x874 + m.x937 <= 336)

m.c3068 = Constraint(expr=   336*m.b194 - m.x875 + m.x938 <= 336)

m.c3069 = Constraint(expr=   336*m.b195 - m.x876 + m.x939 <= 336)

m.c3070 = Constraint(expr=   336*m.b196 - m.x877 + m.x934 <= 336)

m.c3071 = Constraint(expr=   336*m.b197 - m.x878 + m.x935 <= 336)

m.c3072 = Constraint(expr=   336*m.b198 - m.x879 + m.x936 <= 336)

m.c3073 = Constraint(expr=   336*m.b199 - m.x880 + m.x937 <= 336)

m.c3074 = Constraint(expr=   336*m.b200 - m.x881 + m.x938 <= 336)

m.c3075 = Constraint(expr=   336*m.b201 - m.x882 + m.x939 <= 336)

m.c3076 = Constraint(expr=   336*m.b202 - m.x883 + m.x934 <= 336)

m.c3077 = Constraint(expr=   336*m.b203 - m.x884 + m.x935 <= 336)

m.c3078 = Constraint(expr=   336*m.b204 - m.x885 + m.x936 <= 336)

m.c3079 = Constraint(expr=   336*m.b205 - m.x886 + m.x937 <= 336)

m.c3080 = Constraint(expr=   336*m.b206 - m.x887 + m.x938 <= 336)

m.c3081 = Constraint(expr=   336*m.b207 - m.x888 + m.x939 <= 336)

m.c3082 = Constraint(expr=   336*m.b208 - m.x889 + m.x940 <= 336)

m.c3083 = Constraint(expr=   336*m.b209 - m.x890 + m.x941 <= 336)

m.c3084 = Constraint(expr=   336*m.b210 - m.x891 + m.x942 <= 336)

m.c3085 = Constraint(expr=   336*m.b211 - m.x892 + m.x940 <= 336)

m.c3086 = Constraint(expr=   336*m.b212 - m.x893 + m.x941 <= 336)

m.c3087 = Constraint(expr=   336*m.b213 - m.x894 + m.x942 <= 336)

m.c3088 = Constraint(expr=   336*m.b214 - m.x895 + m.x940 <= 336)

m.c3089 = Constraint(expr=   336*m.b215 - m.x896 + m.x941 <= 336)

m.c3090 = Constraint(expr=   336*m.b216 - m.x897 + m.x942 <= 336)

m.c3091 = Constraint(expr= - 336*m.b181 - m.x898 + m.x949 >= -336)

m.c3092 = Constraint(expr= - 336*m.b182 - m.x899 + m.x950 >= -336)

m.c3093 = Constraint(expr= - 336*m.b183 - m.x900 + m.x951 >= -336)

m.c3094 = Constraint(expr= - 336*m.b184 - m.x901 + m.x943 >= -336)

m.c3095 = Constraint(expr= - 336*m.b185 - m.x902 + m.x944 >= -336)

m.c3096 = Constraint(expr= - 336*m.b186 - m.x903 + m.x945 >= -336)

m.c3097 = Constraint(expr= - 336*m.b187 - m.x904 + m.x946 >= -336)

m.c3098 = Constraint(expr= - 336*m.b188 - m.x905 + m.x947 >= -336)

m.c3099 = Constraint(expr= - 336*m.b189 - m.x906 + m.x948 >= -336)

m.c3100 = Constraint(expr= - 336*m.b190 - m.x907 + m.x943 >= -336)

m.c3101 = Constraint(expr= - 336*m.b191 - m.x908 + m.x944 >= -336)

m.c3102 = Constraint(expr= - 336*m.b192 - m.x909 + m.x945 >= -336)

m.c3103 = Constraint(expr= - 336*m.b193 - m.x910 + m.x946 >= -336)

m.c3104 = Constraint(expr= - 336*m.b194 - m.x911 + m.x947 >= -336)

m.c3105 = Constraint(expr= - 336*m.b195 - m.x912 + m.x948 >= -336)

m.c3106 = Constraint(expr= - 336*m.b196 - m.x913 + m.x943 >= -336)

m.c3107 = Constraint(expr= - 336*m.b197 - m.x914 + m.x944 >= -336)

m.c3108 = Constraint(expr= - 336*m.b198 - m.x915 + m.x945 >= -336)

m.c3109 = Constraint(expr= - 336*m.b199 - m.x916 + m.x946 >= -336)

m.c3110 = Constraint(expr= - 336*m.b200 - m.x917 + m.x947 >= -336)

m.c3111 = Constraint(expr= - 336*m.b201 - m.x918 + m.x948 >= -336)

m.c3112 = Constraint(expr= - 336*m.b202 - m.x919 + m.x943 >= -336)

m.c3113 = Constraint(expr= - 336*m.b203 - m.x920 + m.x944 >= -336)

m.c3114 = Constraint(expr= - 336*m.b204 - m.x921 + m.x945 >= -336)

m.c3115 = Constraint(expr= - 336*m.b205 - m.x922 + m.x946 >= -336)

m.c3116 = Constraint(expr= - 336*m.b206 - m.x923 + m.x947 >= -336)

m.c3117 = Constraint(expr= - 336*m.b207 - m.x924 + m.x948 >= -336)

m.c3118 = Constraint(expr= - 336*m.b208 - m.x925 + m.x949 >= -336)

m.c3119 = Constraint(expr= - 336*m.b209 - m.x926 + m.x950 >= -336)

m.c3120 = Constraint(expr= - 336*m.b210 - m.x927 + m.x951 >= -336)

m.c3121 = Constraint(expr= - 336*m.b211 - m.x928 + m.x949 >= -336)

m.c3122 = Constraint(expr= - 336*m.b212 - m.x929 + m.x950 >= -336)

m.c3123 = Constraint(expr= - 336*m.b213 - m.x930 + m.x951 >= -336)

m.c3124 = Constraint(expr= - 336*m.b214 - m.x931 + m.x949 >= -336)

m.c3125 = Constraint(expr= - 336*m.b215 - m.x932 + m.x950 >= -336)

m.c3126 = Constraint(expr= - 336*m.b216 - m.x933 + m.x951 >= -336)

m.c3127 = Constraint(expr=   336*m.b181 - m.x898 + m.x949 <= 336)

m.c3128 = Constraint(expr=   336*m.b182 - m.x899 + m.x950 <= 336)

m.c3129 = Constraint(expr=   336*m.b183 - m.x900 + m.x951 <= 336)

m.c3130 = Constraint(expr=   336*m.b184 - m.x901 + m.x943 <= 336)

m.c3131 = Constraint(expr=   336*m.b185 - m.x902 + m.x944 <= 336)

m.c3132 = Constraint(expr=   336*m.b186 - m.x903 + m.x945 <= 336)

m.c3133 = Constraint(expr=   336*m.b187 - m.x904 + m.x946 <= 336)

m.c3134 = Constraint(expr=   336*m.b188 - m.x905 + m.x947 <= 336)

m.c3135 = Constraint(expr=   336*m.b189 - m.x906 + m.x948 <= 336)

m.c3136 = Constraint(expr=   336*m.b190 - m.x907 + m.x943 <= 336)

m.c3137 = Constraint(expr=   336*m.b191 - m.x908 + m.x944 <= 336)

m.c3138 = Constraint(expr=   336*m.b192 - m.x909 + m.x945 <= 336)

m.c3139 = Constraint(expr=   336*m.b193 - m.x910 + m.x946 <= 336)

m.c3140 = Constraint(expr=   336*m.b194 - m.x911 + m.x947 <= 336)

m.c3141 = Constraint(expr=   336*m.b195 - m.x912 + m.x948 <= 336)

m.c3142 = Constraint(expr=   336*m.b196 - m.x913 + m.x943 <= 336)

m.c3143 = Constraint(expr=   336*m.b197 - m.x914 + m.x944 <= 336)

m.c3144 = Constraint(expr=   336*m.b198 - m.x915 + m.x945 <= 336)

m.c3145 = Constraint(expr=   336*m.b199 - m.x916 + m.x946 <= 336)

m.c3146 = Constraint(expr=   336*m.b200 - m.x917 + m.x947 <= 336)

m.c3147 = Constraint(expr=   336*m.b201 - m.x918 + m.x948 <= 336)

m.c3148 = Constraint(expr=   336*m.b202 - m.x919 + m.x943 <= 336)

m.c3149 = Constraint(expr=   336*m.b203 - m.x920 + m.x944 <= 336)

m.c3150 = Constraint(expr=   336*m.b204 - m.x921 + m.x945 <= 336)

m.c3151 = Constraint(expr=   336*m.b205 - m.x922 + m.x946 <= 336)

m.c3152 = Constraint(expr=   336*m.b206 - m.x923 + m.x947 <= 336)

m.c3153 = Constraint(expr=   336*m.b207 - m.x924 + m.x948 <= 336)

m.c3154 = Constraint(expr=   336*m.b208 - m.x925 + m.x949 <= 336)

m.c3155 = Constraint(expr=   336*m.b209 - m.x926 + m.x950 <= 336)

m.c3156 = Constraint(expr=   336*m.b210 - m.x927 + m.x951 <= 336)

m.c3157 = Constraint(expr=   336*m.b211 - m.x928 + m.x949 <= 336)

m.c3158 = Constraint(expr=   336*m.b212 - m.x929 + m.x950 <= 336)

m.c3159 = Constraint(expr=   336*m.b213 - m.x930 + m.x951 <= 336)

m.c3160 = Constraint(expr=   336*m.b214 - m.x931 + m.x949 <= 336)

m.c3161 = Constraint(expr=   336*m.b215 - m.x932 + m.x950 <= 336)

m.c3162 = Constraint(expr=   336*m.b216 - m.x933 + m.x951 <= 336)

m.c3163 = Constraint(expr=   m.x254 - m.x976 + m.x977 == 0)

m.c3164 = Constraint(expr=   m.x255 - m.x977 + m.x978 == 0)

m.c3165 = Constraint(expr=   m.x257 - m.x407 - m.x527 - m.x979 + m.x980 == 0)

m.c3166 = Constraint(expr=   m.x258 - m.x408 - m.x528 - m.x980 + m.x981 == 0)

m.c3167 = Constraint(expr=   m.x260 - m.x419 - m.x491 - m.x503 - m.x982 + m.x983 == 0)

m.c3168 = Constraint(expr=   m.x261 - m.x420 - m.x492 - m.x504 - m.x983 + m.x984 == 0)

m.c3169 = Constraint(expr=   m.x263 - m.x431 - m.x985 + m.x986 == 0)

m.c3170 = Constraint(expr=   m.x264 - m.x432 - m.x986 + m.x987 == 0)

m.c3171 = Constraint(expr=   m.x266 + m.x278 - m.x443 - m.x455 - m.x988 + m.x989 == 0)

m.c3172 = Constraint(expr=   m.x267 + m.x279 - m.x444 - m.x456 - m.x989 + m.x990 == 0)

m.c3173 = Constraint(expr=   m.x269 + m.x281 - m.x467 - m.x515 - m.x991 + m.x992 == 0)

m.c3174 = Constraint(expr=   m.x270 + m.x282 - m.x468 - m.x516 - m.x992 + m.x993 == 0)

m.c3175 = Constraint(expr=   m.x272 + m.x284 - m.x539 - m.x994 + m.x995 == 0)

m.c3176 = Constraint(expr=   m.x273 + m.x285 - m.x540 - m.x995 + m.x996 == 0)

m.c3177 = Constraint(expr=   m.x275 + m.x287 - m.x479 - m.x997 + m.x998 == 0)

m.c3178 = Constraint(expr=   m.x276 + m.x288 - m.x480 - m.x998 + m.x999 == 0)

m.c3179 = Constraint(expr=   m.x290 + m.x302 - m.x446 - m.x458 - m.x1000 + m.x1001 == 0)

m.c3180 = Constraint(expr=   m.x291 + m.x303 - m.x447 - m.x459 - m.x1001 + m.x1002 == 0)

m.c3181 = Constraint(expr=   m.x293 + m.x305 - m.x470 - m.x518 - m.x1003 + m.x1004 == 0)

m.c3182 = Constraint(expr=   m.x294 + m.x306 - m.x471 - m.x519 - m.x1004 + m.x1005 == 0)

m.c3183 = Constraint(expr=   m.x296 + m.x308 - m.x542 - m.x1006 + m.x1007 == 0)

m.c3184 = Constraint(expr=   m.x297 + m.x309 - m.x543 - m.x1007 + m.x1008 == 0)

m.c3185 = Constraint(expr=   m.x299 + m.x311 - m.x482 - m.x1009 + m.x1010 == 0)

m.c3186 = Constraint(expr=   m.x300 + m.x312 - m.x483 - m.x1010 + m.x1011 == 0)

m.c3187 = Constraint(expr=   m.x314 + m.x326 - m.x449 - m.x461 - m.x1012 + m.x1013 == 0)

m.c3188 = Constraint(expr=   m.x315 + m.x327 - m.x450 - m.x462 - m.x1013 + m.x1014 == 0)

m.c3189 = Constraint(expr=   m.x317 + m.x329 - m.x473 - m.x521 - m.x1015 + m.x1016 == 0)

m.c3190 = Constraint(expr=   m.x318 + m.x330 - m.x474 - m.x522 - m.x1016 + m.x1017 == 0)

m.c3191 = Constraint(expr=   m.x320 + m.x332 - m.x545 - m.x1018 + m.x1019 == 0)

m.c3192 = Constraint(expr=   m.x321 + m.x333 - m.x546 - m.x1019 + m.x1020 == 0)

m.c3193 = Constraint(expr=   m.x323 + m.x335 - m.x485 - m.x1021 + m.x1022 == 0)

m.c3194 = Constraint(expr=   m.x324 + m.x336 - m.x486 - m.x1022 + m.x1023 == 0)

m.c3195 = Constraint(expr=   m.x338 + m.x350 - m.x452 - m.x464 - m.x1024 + m.x1025 == 0)

m.c3196 = Constraint(expr=   m.x339 + m.x351 - m.x453 - m.x465 - m.x1025 + m.x1026 == 0)

m.c3197 = Constraint(expr=   m.x341 + m.x353 - m.x476 - m.x524 - m.x1027 + m.x1028 == 0)

m.c3198 = Constraint(expr=   m.x342 + m.x354 - m.x477 - m.x525 - m.x1028 + m.x1029 == 0)

m.c3199 = Constraint(expr=   m.x344 + m.x356 - m.x548 - m.x1030 + m.x1031 == 0)

m.c3200 = Constraint(expr=   m.x345 + m.x357 - m.x549 - m.x1031 + m.x1032 == 0)

m.c3201 = Constraint(expr=   m.x347 + m.x359 - m.x488 - m.x1033 + m.x1034 == 0)

m.c3202 = Constraint(expr=   m.x348 + m.x360 - m.x489 - m.x1034 + m.x1035 == 0)

m.c3203 = Constraint(expr=   m.x362 - m.x1036 + m.x1037 == 0)

m.c3204 = Constraint(expr=   m.x363 - m.x1037 + m.x1038 == 0)

m.c3205 = Constraint(expr=   m.x365 - m.x410 - m.x530 - m.x1039 + m.x1040 == 0)

m.c3206 = Constraint(expr=   m.x366 - m.x411 - m.x531 - m.x1040 + m.x1041 == 0)

m.c3207 = Constraint(expr=   m.x368 - m.x422 - m.x494 - m.x506 - m.x1042 + m.x1043 == 0)

m.c3208 = Constraint(expr=   m.x369 - m.x423 - m.x495 - m.x507 - m.x1043 + m.x1044 == 0)

m.c3209 = Constraint(expr=   m.x371 - m.x434 - m.x1045 + m.x1046 == 0)

m.c3210 = Constraint(expr=   m.x372 - m.x435 - m.x1046 + m.x1047 == 0)

m.c3211 = Constraint(expr=   m.x374 - m.x1048 + m.x1049 == 0)

m.c3212 = Constraint(expr=   m.x375 - m.x1049 + m.x1050 == 0)

m.c3213 = Constraint(expr=   m.x377 - m.x413 - m.x533 - m.x1051 + m.x1052 == 0)

m.c3214 = Constraint(expr=   m.x378 - m.x414 - m.x534 - m.x1052 + m.x1053 == 0)

m.c3215 = Constraint(expr=   m.x380 - m.x425 - m.x497 - m.x509 - m.x1054 + m.x1055 == 0)

m.c3216 = Constraint(expr=   m.x381 - m.x426 - m.x498 - m.x510 - m.x1055 + m.x1056 == 0)

m.c3217 = Constraint(expr=   m.x383 - m.x437 - m.x1057 + m.x1058 == 0)

m.c3218 = Constraint(expr=   m.x384 - m.x438 - m.x1058 + m.x1059 == 0)

m.c3219 = Constraint(expr=   m.x386 - m.x1060 + m.x1061 == 0)

m.c3220 = Constraint(expr=   m.x387 - m.x1061 + m.x1062 == 0)

m.c3221 = Constraint(expr=   m.x389 - m.x416 - m.x536 - m.x1063 + m.x1064 == 0)

m.c3222 = Constraint(expr=   m.x390 - m.x417 - m.x537 - m.x1064 + m.x1065 == 0)

m.c3223 = Constraint(expr=   m.x392 - m.x428 - m.x500 - m.x512 - m.x1066 + m.x1067 == 0)

m.c3224 = Constraint(expr=   m.x393 - m.x429 - m.x501 - m.x513 - m.x1067 + m.x1068 == 0)

m.c3225 = Constraint(expr=   m.x395 - m.x440 - m.x1069 + m.x1070 == 0)

m.c3226 = Constraint(expr=   m.x396 - m.x441 - m.x1070 + m.x1071 == 0)

m.c3227 = Constraint(expr=   m.x253 + m.x976 == 100)

m.c3228 = Constraint(expr=   m.x256 - m.x406 - m.x526 + m.x979 == 100)

m.c3229 = Constraint(expr=   m.x259 - m.x418 - m.x490 - m.x502 + m.x982 == 100)

m.c3230 = Constraint(expr=   m.x262 - m.x430 + m.x985 == 100)

m.c3231 = Constraint(expr=   m.x265 + m.x277 - m.x442 - m.x454 + m.x988 == 100)

m.c3232 = Constraint(expr=   m.x268 + m.x280 - m.x466 - m.x514 + m.x991 == 100)

m.c3233 = Constraint(expr=   m.x271 + m.x283 - m.x538 + m.x994 == 100)

m.c3234 = Constraint(expr=   m.x274 + m.x286 - m.x478 + m.x997 == 100)

m.c3235 = Constraint(expr=   m.x289 + m.x301 - m.x445 - m.x457 + m.x1000 == 100)

m.c3236 = Constraint(expr=   m.x292 + m.x304 - m.x469 - m.x517 + m.x1003 == 100)

m.c3237 = Constraint(expr=   m.x295 + m.x307 - m.x541 + m.x1006 == 50)

m.c3238 = Constraint(expr=   m.x298 + m.x310 - m.x481 + m.x1009 == 100)

m.c3239 = Constraint(expr=   m.x313 + m.x325 - m.x448 - m.x460 + m.x1012 == 200)

m.c3240 = Constraint(expr=   m.x316 + m.x328 - m.x472 - m.x520 + m.x1015 == 250)

m.c3241 = Constraint(expr=   m.x319 + m.x331 - m.x544 + m.x1018 == 200)

m.c3242 = Constraint(expr=   m.x322 + m.x334 - m.x484 + m.x1021 == 300)

m.c3243 = Constraint(expr=   m.x337 + m.x349 - m.x451 - m.x463 + m.x1024 == 75)

m.c3244 = Constraint(expr=   m.x340 + m.x352 - m.x475 - m.x523 + m.x1027 == 75)

m.c3245 = Constraint(expr=   m.x343 + m.x355 - m.x547 + m.x1030 == 75)

m.c3246 = Constraint(expr=   m.x346 + m.x358 - m.x487 + m.x1033 == 75)

m.c3247 = Constraint(expr=   m.x361 + m.x1036 == 20)

m.c3248 = Constraint(expr=   m.x364 - m.x409 - m.x529 + m.x1039 == 20)

m.c3249 = Constraint(expr=   m.x367 - m.x421 - m.x493 - m.x505 + m.x1042 == 20)

m.c3250 = Constraint(expr=   m.x370 - m.x433 + m.x1045 == 20)

m.c3251 = Constraint(expr=   m.x373 + m.x1048 == 20)

m.c3252 = Constraint(expr=   m.x376 - m.x412 - m.x532 + m.x1051 == 20)

m.c3253 = Constraint(expr=   m.x379 - m.x424 - m.x496 - m.x508 + m.x1054 == 20)

m.c3254 = Constraint(expr=   m.x382 - m.x436 + m.x1057 == 20)

m.c3255 = Constraint(expr=   m.x385 + m.x1060 == 100)

m.c3256 = Constraint(expr=   m.x388 - m.x415 - m.x535 + m.x1063 == 100)

m.c3257 = Constraint(expr=   m.x391 - m.x427 - m.x499 - m.x511 + m.x1066 == 100)

m.c3258 = Constraint(expr=   m.x394 - m.x439 + m.x1069 == 150)

m.c3259 = Constraint(expr= - m.x934 - m.x935 - m.x936 + m.x943 + m.x944 + m.x945 == 336)

m.c3260 = Constraint(expr= - m.x937 - m.x938 - m.x939 + m.x946 + m.x947 + m.x948 == 336)

m.c3261 = Constraint(expr= - m.x940 - m.x941 - m.x942 + m.x949 + m.x950 + m.x951 == 336)

m.c3262 = Constraint(expr= - m.b181 + m.b182 + m.x1076 >= 0)

m.c3263 = Constraint(expr= - m.b182 + m.b183 + m.x1077 >= 0)

m.c3264 = Constraint(expr= - m.b184 + m.b185 + m.x1072 >= 0)

m.c3265 = Constraint(expr= - m.b185 + m.b186 + m.x1073 >= 0)

m.c3266 = Constraint(expr= - m.b187 + m.b188 + m.x1074 >= 0)

m.c3267 = Constraint(expr= - m.b188 + m.b189 + m.x1075 >= 0)

m.c3268 = Constraint(expr= - m.b190 + m.b191 + m.x1072 >= 0)

m.c3269 = Constraint(expr= - m.b191 + m.b192 + m.x1073 >= 0)

m.c3270 = Constraint(expr= - m.b193 + m.b194 + m.x1074 >= 0)

m.c3271 = Constraint(expr= - m.b194 + m.b195 + m.x1075 >= 0)

m.c3272 = Constraint(expr= - m.b196 + m.b197 + m.x1072 >= 0)

m.c3273 = Constraint(expr= - m.b197 + m.b198 + m.x1073 >= 0)

m.c3274 = Constraint(expr= - m.b199 + m.b200 + m.x1074 >= 0)

m.c3275 = Constraint(expr= - m.b200 + m.b201 + m.x1075 >= 0)

m.c3276 = Constraint(expr= - m.b202 + m.b203 + m.x1072 >= 0)

m.c3277 = Constraint(expr= - m.b203 + m.b204 + m.x1073 >= 0)

m.c3278 = Constraint(expr= - m.b205 + m.b206 + m.x1074 >= 0)

m.c3279 = Constraint(expr= - m.b206 + m.b207 + m.x1075 >= 0)

m.c3280 = Constraint(expr= - m.b208 + m.b209 + m.x1076 >= 0)

m.c3281 = Constraint(expr= - m.b209 + m.b210 + m.x1077 >= 0)

m.c3282 = Constraint(expr= - m.b211 + m.b212 + m.x1076 >= 0)

m.c3283 = Constraint(expr= - m.b212 + m.b213 + m.x1077 >= 0)

m.c3284 = Constraint(expr= - m.b214 + m.b215 + m.x1076 >= 0)

m.c3285 = Constraint(expr= - m.b215 + m.b216 + m.x1077 >= 0)

m.c3286 = Constraint(expr=   m.b181 - m.b182 + m.x1076 >= 0)

m.c3287 = Constraint(expr=   m.b182 - m.b183 + m.x1077 >= 0)

m.c3288 = Constraint(expr=   m.b184 - m.b185 + m.x1072 >= 0)

m.c3289 = Constraint(expr=   m.b185 - m.b186 + m.x1073 >= 0)

m.c3290 = Constraint(expr=   m.b187 - m.b188 + m.x1074 >= 0)

m.c3291 = Constraint(expr=   m.b188 - m.b189 + m.x1075 >= 0)

m.c3292 = Constraint(expr=   m.b190 - m.b191 + m.x1072 >= 0)

m.c3293 = Constraint(expr=   m.b191 - m.b192 + m.x1073 >= 0)

m.c3294 = Constraint(expr=   m.b193 - m.b194 + m.x1074 >= 0)

m.c3295 = Constraint(expr=   m.b194 - m.b195 + m.x1075 >= 0)

m.c3296 = Constraint(expr=   m.b196 - m.b197 + m.x1072 >= 0)

m.c3297 = Constraint(expr=   m.b197 - m.b198 + m.x1073 >= 0)

m.c3298 = Constraint(expr=   m.b199 - m.b200 + m.x1074 >= 0)

m.c3299 = Constraint(expr=   m.b200 - m.b201 + m.x1075 >= 0)

m.c3300 = Constraint(expr=   m.b202 - m.b203 + m.x1072 >= 0)

m.c3301 = Constraint(expr=   m.b203 - m.b204 + m.x1073 >= 0)

m.c3302 = Constraint(expr=   m.b205 - m.b206 + m.x1074 >= 0)

m.c3303 = Constraint(expr=   m.b206 - m.b207 + m.x1075 >= 0)

m.c3304 = Constraint(expr=   m.b208 - m.b209 + m.x1076 >= 0)

m.c3305 = Constraint(expr=   m.b209 - m.b210 + m.x1077 >= 0)

m.c3306 = Constraint(expr=   m.b211 - m.b212 + m.x1076 >= 0)

m.c3307 = Constraint(expr=   m.b212 - m.b213 + m.x1077 >= 0)

m.c3308 = Constraint(expr=   m.b214 - m.b215 + m.x1076 >= 0)

m.c3309 = Constraint(expr=   m.b215 - m.b216 + m.x1077 >= 0)

m.c3310 = Constraint(expr=   0.25*m.x952 + 0.25*m.x953 + 0.25*m.x954 + 0.25*m.x955 + 0.25*m.x956 + 0.25*m.x957
                           + 0.25*m.x958 + 0.25*m.x959 + 0.25*m.x960 + 0.25*m.x961 + 0.25*m.x962 + 0.25*m.x963
                           + 0.25*m.x964 + 0.25*m.x965 + 0.25*m.x966 + 0.25*m.x967 + 0.25*m.x968 + 0.25*m.x969
                           + 0.25*m.x970 + 0.25*m.x971 + 0.25*m.x972 + 0.25*m.x973 + 0.25*m.x974 + 0.25*m.x975 + m.x1174
                           >= 747.5)

m.c3311 = Constraint(expr= - 3.125*m.x565 + m.x1175 >= -75)

m.c3312 = Constraint(expr= - 3.125*m.x569 + m.x1176 >= -450)

m.c3313 = Constraint(expr= - 3.125*m.x573 + m.x1177 >= -750)

m.c3315 = Constraint(expr=-m.x1078*m.x218 + m.x254 == 0)

m.c3316 = Constraint(expr=-m.x1079*m.x219 + m.x255 == 0)

m.c3317 = Constraint(expr=-m.x1081*m.x218 + m.x257 == 0)

m.c3318 = Constraint(expr=-m.x1082*m.x219 + m.x258 == 0)

m.c3319 = Constraint(expr=-m.x1084*m.x218 + m.x260 == 0)

m.c3320 = Constraint(expr=-m.x1085*m.x219 + m.x261 == 0)

m.c3321 = Constraint(expr=-m.x1087*m.x218 + m.x263 == 0)

m.c3322 = Constraint(expr=-m.x1088*m.x219 + m.x264 == 0)

m.c3323 = Constraint(expr=-m.x1090*m.x221 + m.x266 == 0)

m.c3324 = Constraint(expr=-m.x1091*m.x222 + m.x267 == 0)

m.c3325 = Constraint(expr=-m.x1093*m.x221 + m.x269 == 0)

m.c3326 = Constraint(expr=-m.x1094*m.x222 + m.x270 == 0)

m.c3327 = Constraint(expr=-m.x1096*m.x221 + m.x272 == 0)

m.c3328 = Constraint(expr=-m.x1097*m.x222 + m.x273 == 0)

m.c3329 = Constraint(expr=-m.x1099*m.x221 + m.x275 == 0)

m.c3330 = Constraint(expr=-m.x1100*m.x222 + m.x276 == 0)

m.c3331 = Constraint(expr=-m.x1090*m.x224 + m.x278 == 0)

m.c3332 = Constraint(expr=-m.x1091*m.x225 + m.x279 == 0)

m.c3333 = Constraint(expr=-m.x1093*m.x224 + m.x281 == 0)

m.c3334 = Constraint(expr=-m.x1094*m.x225 + m.x282 == 0)

m.c3335 = Constraint(expr=-m.x1096*m.x224 + m.x284 == 0)

m.c3336 = Constraint(expr=-m.x1097*m.x225 + m.x285 == 0)

m.c3337 = Constraint(expr=-m.x1099*m.x224 + m.x287 == 0)

m.c3338 = Constraint(expr=-m.x1100*m.x225 + m.x288 == 0)

m.c3339 = Constraint(expr=-m.x1102*m.x227 + m.x290 == 0)

m.c3340 = Constraint(expr=-m.x1103*m.x228 + m.x291 == 0)

m.c3341 = Constraint(expr=-m.x1105*m.x227 + m.x293 == 0)

m.c3342 = Constraint(expr=-m.x1106*m.x228 + m.x294 == 0)

m.c3343 = Constraint(expr=-m.x1108*m.x227 + m.x296 == 0)

m.c3344 = Constraint(expr=-m.x1109*m.x228 + m.x297 == 0)

m.c3345 = Constraint(expr=-m.x1111*m.x227 + m.x299 == 0)

m.c3346 = Constraint(expr=-m.x1112*m.x228 + m.x300 == 0)

m.c3347 = Constraint(expr=-m.x1102*m.x230 + m.x302 == 0)

m.c3348 = Constraint(expr=-m.x1103*m.x231 + m.x303 == 0)

m.c3349 = Constraint(expr=-m.x1105*m.x230 + m.x305 == 0)

m.c3350 = Constraint(expr=-m.x1106*m.x231 + m.x306 == 0)

m.c3351 = Constraint(expr=-m.x1108*m.x230 + m.x308 == 0)

m.c3352 = Constraint(expr=-m.x1109*m.x231 + m.x309 == 0)

m.c3353 = Constraint(expr=-m.x1111*m.x230 + m.x311 == 0)

m.c3354 = Constraint(expr=-m.x1112*m.x231 + m.x312 == 0)

m.c3355 = Constraint(expr=-m.x1114*m.x233 + m.x314 == 0)

m.c3356 = Constraint(expr=-m.x1115*m.x234 + m.x315 == 0)

m.c3357 = Constraint(expr=-m.x1117*m.x233 + m.x317 == 0)

m.c3358 = Constraint(expr=-m.x1118*m.x234 + m.x318 == 0)

m.c3359 = Constraint(expr=-m.x1120*m.x233 + m.x320 == 0)

m.c3360 = Constraint(expr=-m.x1121*m.x234 + m.x321 == 0)

m.c3361 = Constraint(expr=-m.x1123*m.x233 + m.x323 == 0)

m.c3362 = Constraint(expr=-m.x1124*m.x234 + m.x324 == 0)

m.c3363 = Constraint(expr=-m.x1114*m.x236 + m.x326 == 0)

m.c3364 = Constraint(expr=-m.x1115*m.x237 + m.x327 == 0)

m.c3365 = Constraint(expr=-m.x1117*m.x236 + m.x329 == 0)

m.c3366 = Constraint(expr=-m.x1118*m.x237 + m.x330 == 0)

m.c3367 = Constraint(expr=-m.x1120*m.x236 + m.x332 == 0)

m.c3368 = Constraint(expr=-m.x1121*m.x237 + m.x333 == 0)

m.c3369 = Constraint(expr=-m.x1123*m.x236 + m.x335 == 0)

m.c3370 = Constraint(expr=-m.x1124*m.x237 + m.x336 == 0)

m.c3371 = Constraint(expr=-m.x1126*m.x239 + m.x338 == 0)

m.c3372 = Constraint(expr=-m.x1127*m.x240 + m.x339 == 0)

m.c3373 = Constraint(expr=-m.x1129*m.x239 + m.x341 == 0)

m.c3374 = Constraint(expr=-m.x1130*m.x240 + m.x342 == 0)

m.c3375 = Constraint(expr=-m.x1132*m.x239 + m.x344 == 0)

m.c3376 = Constraint(expr=-m.x1133*m.x240 + m.x345 == 0)

m.c3377 = Constraint(expr=-m.x1135*m.x239 + m.x347 == 0)

m.c3378 = Constraint(expr=-m.x1136*m.x240 + m.x348 == 0)

m.c3379 = Constraint(expr=-m.x1126*m.x242 + m.x350 == 0)

m.c3380 = Constraint(expr=-m.x1127*m.x243 + m.x351 == 0)

m.c3381 = Constraint(expr=-m.x1129*m.x242 + m.x353 == 0)

m.c3382 = Constraint(expr=-m.x1130*m.x243 + m.x354 == 0)

m.c3383 = Constraint(expr=-m.x1132*m.x242 + m.x356 == 0)

m.c3384 = Constraint(expr=-m.x1133*m.x243 + m.x357 == 0)

m.c3385 = Constraint(expr=-m.x1135*m.x242 + m.x359 == 0)

m.c3386 = Constraint(expr=-m.x1136*m.x243 + m.x360 == 0)

m.c3387 = Constraint(expr=-m.x1138*m.x245 + m.x362 == 0)

m.c3388 = Constraint(expr=-m.x1139*m.x246 + m.x363 == 0)

m.c3389 = Constraint(expr=-m.x1141*m.x245 + m.x365 == 0)

m.c3390 = Constraint(expr=-m.x1142*m.x246 + m.x366 == 0)

m.c3391 = Constraint(expr=-m.x1144*m.x245 + m.x368 == 0)

m.c3392 = Constraint(expr=-m.x1145*m.x246 + m.x369 == 0)

m.c3393 = Constraint(expr=-m.x1147*m.x245 + m.x371 == 0)

m.c3394 = Constraint(expr=-m.x1148*m.x246 + m.x372 == 0)

m.c3395 = Constraint(expr=-m.x1150*m.x248 + m.x374 == 0)

m.c3396 = Constraint(expr=-m.x1151*m.x249 + m.x375 == 0)

m.c3397 = Constraint(expr=-m.x1153*m.x248 + m.x377 == 0)

m.c3398 = Constraint(expr=-m.x1154*m.x249 + m.x378 == 0)

m.c3399 = Constraint(expr=-m.x1156*m.x248 + m.x380 == 0)

m.c3400 = Constraint(expr=-m.x1157*m.x249 + m.x381 == 0)

m.c3401 = Constraint(expr=-m.x1159*m.x248 + m.x383 == 0)

m.c3402 = Constraint(expr=-m.x1160*m.x249 + m.x384 == 0)

m.c3403 = Constraint(expr=-m.x1162*m.x251 + m.x386 == 0)

m.c3404 = Constraint(expr=-m.x1163*m.x252 + m.x387 == 0)

m.c3405 = Constraint(expr=-m.x1165*m.x251 + m.x389 == 0)

m.c3406 = Constraint(expr=-m.x1166*m.x252 + m.x390 == 0)

m.c3407 = Constraint(expr=-m.x1168*m.x251 + m.x392 == 0)

m.c3408 = Constraint(expr=-m.x1169*m.x252 + m.x393 == 0)

m.c3409 = Constraint(expr=-m.x1171*m.x251 + m.x395 == 0)

m.c3410 = Constraint(expr=-m.x1172*m.x252 + m.x396 == 0)

m.c3411 = Constraint(expr=-m.x1078*m.x952 + m.x976 == 0)

m.c3412 = Constraint(expr=-m.x1079*m.x953 + m.x977 == 0)

m.c3413 = Constraint(expr=-m.x1080*m.x954 + m.x978 == 0)

m.c3414 = Constraint(expr=-m.x1081*m.x952 + m.x979 == 0)

m.c3415 = Constraint(expr=-m.x1082*m.x953 + m.x980 == 0)

m.c3416 = Constraint(expr=-m.x1083*m.x954 + m.x981 == 0)

m.c3417 = Constraint(expr=-m.x1084*m.x952 + m.x982 == 0)

m.c3418 = Constraint(expr=-m.x1085*m.x953 + m.x983 == 0)

m.c3419 = Constraint(expr=-m.x1086*m.x954 + m.x984 == 0)

m.c3420 = Constraint(expr=-m.x1087*m.x952 + m.x985 == 0)

m.c3421 = Constraint(expr=-m.x1088*m.x953 + m.x986 == 0)

m.c3422 = Constraint(expr=-m.x1089*m.x954 + m.x987 == 0)

m.c3423 = Constraint(expr=-m.x1090*m.x955 + m.x988 == 0)

m.c3424 = Constraint(expr=-m.x1091*m.x956 + m.x989 == 0)

m.c3425 = Constraint(expr=-m.x1092*m.x957 + m.x990 == 0)

m.c3426 = Constraint(expr=-m.x1093*m.x955 + m.x991 == 0)

m.c3427 = Constraint(expr=-m.x1094*m.x956 + m.x992 == 0)

m.c3428 = Constraint(expr=-m.x1095*m.x957 + m.x993 == 0)

m.c3429 = Constraint(expr=-m.x1096*m.x955 + m.x994 == 0)

m.c3430 = Constraint(expr=-m.x1097*m.x956 + m.x995 == 0)

m.c3431 = Constraint(expr=-m.x1098*m.x957 + m.x996 == 0)

m.c3432 = Constraint(expr=-m.x1099*m.x955 + m.x997 == 0)

m.c3433 = Constraint(expr=-m.x1100*m.x956 + m.x998 == 0)

m.c3434 = Constraint(expr=-m.x1101*m.x957 + m.x999 == 0)

m.c3435 = Constraint(expr=-m.x1102*m.x958 + m.x1000 == 0)

m.c3436 = Constraint(expr=-m.x1103*m.x959 + m.x1001 == 0)

m.c3437 = Constraint(expr=-m.x1104*m.x960 + m.x1002 == 0)

m.c3438 = Constraint(expr=-m.x1105*m.x958 + m.x1003 == 0)

m.c3439 = Constraint(expr=-m.x1106*m.x959 + m.x1004 == 0)

m.c3440 = Constraint(expr=-m.x1107*m.x960 + m.x1005 == 0)

m.c3441 = Constraint(expr=-m.x1108*m.x958 + m.x1006 == 0)

m.c3442 = Constraint(expr=-m.x1109*m.x959 + m.x1007 == 0)

m.c3443 = Constraint(expr=-m.x1110*m.x960 + m.x1008 == 0)

m.c3444 = Constraint(expr=-m.x1111*m.x958 + m.x1009 == 0)

m.c3445 = Constraint(expr=-m.x1112*m.x959 + m.x1010 == 0)

m.c3446 = Constraint(expr=-m.x1113*m.x960 + m.x1011 == 0)

m.c3447 = Constraint(expr=-m.x1114*m.x961 + m.x1012 == 0)

m.c3448 = Constraint(expr=-m.x1115*m.x962 + m.x1013 == 0)

m.c3449 = Constraint(expr=-m.x1116*m.x963 + m.x1014 == 0)

m.c3450 = Constraint(expr=-m.x1117*m.x961 + m.x1015 == 0)

m.c3451 = Constraint(expr=-m.x1118*m.x962 + m.x1016 == 0)

m.c3452 = Constraint(expr=-m.x1119*m.x963 + m.x1017 == 0)

m.c3453 = Constraint(expr=-m.x1120*m.x961 + m.x1018 == 0)

m.c3454 = Constraint(expr=-m.x1121*m.x962 + m.x1019 == 0)

m.c3455 = Constraint(expr=-m.x1122*m.x963 + m.x1020 == 0)

m.c3456 = Constraint(expr=-m.x1123*m.x961 + m.x1021 == 0)

m.c3457 = Constraint(expr=-m.x1124*m.x962 + m.x1022 == 0)

m.c3458 = Constraint(expr=-m.x1125*m.x963 + m.x1023 == 0)

m.c3459 = Constraint(expr=-m.x1126*m.x964 + m.x1024 == 0)

m.c3460 = Constraint(expr=-m.x1127*m.x965 + m.x1025 == 0)

m.c3461 = Constraint(expr=-m.x1128*m.x966 + m.x1026 == 0)

m.c3462 = Constraint(expr=-m.x1129*m.x964 + m.x1027 == 0)

m.c3463 = Constraint(expr=-m.x1130*m.x965 + m.x1028 == 0)

m.c3464 = Constraint(expr=-m.x1131*m.x966 + m.x1029 == 0)

m.c3465 = Constraint(expr=-m.x1132*m.x964 + m.x1030 == 0)

m.c3466 = Constraint(expr=-m.x1133*m.x965 + m.x1031 == 0)

m.c3467 = Constraint(expr=-m.x1134*m.x966 + m.x1032 == 0)

m.c3468 = Constraint(expr=-m.x1135*m.x964 + m.x1033 == 0)

m.c3469 = Constraint(expr=-m.x1136*m.x965 + m.x1034 == 0)

m.c3470 = Constraint(expr=-m.x1137*m.x966 + m.x1035 == 0)

m.c3471 = Constraint(expr=-m.x1138*m.x967 + m.x1036 == 0)

m.c3472 = Constraint(expr=-m.x1139*m.x968 + m.x1037 == 0)

m.c3473 = Constraint(expr=-m.x1140*m.x969 + m.x1038 == 0)

m.c3474 = Constraint(expr=-m.x1141*m.x967 + m.x1039 == 0)

m.c3475 = Constraint(expr=-m.x1142*m.x968 + m.x1040 == 0)

m.c3476 = Constraint(expr=-m.x1143*m.x969 + m.x1041 == 0)

m.c3477 = Constraint(expr=-m.x1144*m.x967 + m.x1042 == 0)

m.c3478 = Constraint(expr=-m.x1145*m.x968 + m.x1043 == 0)

m.c3479 = Constraint(expr=-m.x1146*m.x969 + m.x1044 == 0)

m.c3480 = Constraint(expr=-m.x1147*m.x967 + m.x1045 == 0)

m.c3481 = Constraint(expr=-m.x1148*m.x968 + m.x1046 == 0)

m.c3482 = Constraint(expr=-m.x1149*m.x969 + m.x1047 == 0)

m.c3483 = Constraint(expr=-m.x1150*m.x970 + m.x1048 == 0)

m.c3484 = Constraint(expr=-m.x1151*m.x971 + m.x1049 == 0)

m.c3485 = Constraint(expr=-m.x1152*m.x972 + m.x1050 == 0)

m.c3486 = Constraint(expr=-m.x1153*m.x970 + m.x1051 == 0)

m.c3487 = Constraint(expr=-m.x1154*m.x971 + m.x1052 == 0)

m.c3488 = Constraint(expr=-m.x1155*m.x972 + m.x1053 == 0)

m.c3489 = Constraint(expr=-m.x1156*m.x970 + m.x1054 == 0)

m.c3490 = Constraint(expr=-m.x1157*m.x971 + m.x1055 == 0)

m.c3491 = Constraint(expr=-m.x1158*m.x972 + m.x1056 == 0)

m.c3492 = Constraint(expr=-m.x1159*m.x970 + m.x1057 == 0)

m.c3493 = Constraint(expr=-m.x1160*m.x971 + m.x1058 == 0)

m.c3494 = Constraint(expr=-m.x1161*m.x972 + m.x1059 == 0)

m.c3495 = Constraint(expr=-m.x1162*m.x973 + m.x1060 == 0)

m.c3496 = Constraint(expr=-m.x1163*m.x974 + m.x1061 == 0)

m.c3497 = Constraint(expr=-m.x1164*m.x975 + m.x1062 == 0)

m.c3498 = Constraint(expr=-m.x1165*m.x973 + m.x1063 == 0)

m.c3499 = Constraint(expr=-m.x1166*m.x974 + m.x1064 == 0)

m.c3500 = Constraint(expr=-m.x1167*m.x975 + m.x1065 == 0)

m.c3501 = Constraint(expr=-m.x1168*m.x973 + m.x1066 == 0)

m.c3502 = Constraint(expr=-m.x1169*m.x974 + m.x1067 == 0)

m.c3503 = Constraint(expr=-m.x1170*m.x975 + m.x1068 == 0)

m.c3504 = Constraint(expr=-m.x1171*m.x973 + m.x1069 == 0)

m.c3505 = Constraint(expr=-m.x1172*m.x974 + m.x1070 == 0)

m.c3506 = Constraint(expr=-m.x1173*m.x975 + m.x1071 == 0)
