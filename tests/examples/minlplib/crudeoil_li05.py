#  MINLP written by GAMS Convert at 04/21/18 13:51:21
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       1917      516      720      681        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        941      809      132        0        0        0        0        0
#  FX     32       16       16        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       6107     5723      384        0
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
m.x133 = Var(within=Reals,bounds=(0,290),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,340),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,350),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,340),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,350),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,290),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,490),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,290),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,490),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,840),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,850),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,870),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,840),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,850),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,870),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,870),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,870),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,870),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,870),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,390),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,400),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,510),initialize=0)
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
m.x322 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x323 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x324 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x325 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x326 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x327 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x328 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x329 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x330 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x331 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x332 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x333 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x334 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x335 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x336 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x337 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x338 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x339 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x340 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x341 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x342 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x343 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x344 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x345 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x346 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x347 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x348 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x349 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x350 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x351 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x352 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x353 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x354 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x355 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x356 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x357 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x358 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x359 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x360 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x361 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x362 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x363 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x364 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x365 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x366 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x367 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x368 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x369 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x370 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x371 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x372 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x373 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x374 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x375 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x376 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x377 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x378 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x379 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x380 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x381 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x382 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x383 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x384 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x385 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x386 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x387 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x388 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x389 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x390 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x391 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x392 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x393 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x394 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x395 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x396 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x397 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x398 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x399 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x400 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x401 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x402 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x403 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x404 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x405 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x406 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x407 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x408 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x409 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x410 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x411 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x412 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x413 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x414 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x415 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x416 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x417 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x418 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x419 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x420 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x421 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x422 = Var(within=Reals,bounds=(104,160),initialize=104)
m.x423 = Var(within=Reals,bounds=(104,160),initialize=104)
m.x424 = Var(within=Reals,bounds=(104,160),initialize=104)
m.x425 = Var(within=Reals,bounds=(104,160),initialize=104)
m.x426 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x427 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x428 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x429 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x430 = Var(within=Reals,bounds=(104,160),initialize=104)
m.x431 = Var(within=Reals,bounds=(104,160),initialize=104)
m.x432 = Var(within=Reals,bounds=(104,160),initialize=104)
m.x433 = Var(within=Reals,bounds=(104,160),initialize=104)
m.x434 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x435 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x436 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x437 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x438 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x439 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x440 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x441 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x442 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x443 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x444 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x445 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x446 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x447 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x448 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x449 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x450 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x451 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x452 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x453 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x454 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x455 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x456 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x457 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x458 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x459 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x460 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x461 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x462 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x463 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x464 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x465 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x466 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x467 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x468 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x469 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x470 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x471 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x472 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x473 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x474 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x475 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x476 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x477 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x478 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x479 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x480 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x481 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x482 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x483 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x484 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x485 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x486 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x487 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x488 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x489 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x490 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x491 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x492 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x493 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x494 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x495 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x496 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x497 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x498 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x499 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x500 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x501 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x502 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x503 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x504 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x505 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x506 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x507 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x508 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x509 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x510 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x511 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x512 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x513 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x514 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x515 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x516 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x517 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x518 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x519 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x520 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x521 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x522 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x523 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x524 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x525 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x526 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x527 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x528 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x529 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x530 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x531 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x532 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x533 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x534 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x535 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x536 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x537 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x538 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x539 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x540 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x541 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x542 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x543 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x544 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x545 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x546 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x547 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x548 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x549 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x550 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x551 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x552 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x553 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x554 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x555 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x556 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x557 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x558 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x559 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x560 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x561 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x562 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x563 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x564 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x565 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x566 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x567 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x568 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x569 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x570 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x571 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x572 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x573 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x574 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x575 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x576 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x577 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x578 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x579 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x580 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x581 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x582 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x583 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x584 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x585 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x586 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x587 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x588 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x589 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x590 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x591 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x592 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x593 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x594 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x595 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x596 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x597 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x598 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x599 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x600 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x601 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x602 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x603 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x604 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x605 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x606 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x607 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x608 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x609 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x610 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x611 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x612 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x613 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x614 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x615 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x616 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x617 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x618 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x619 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x620 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x621 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x622 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x623 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x624 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x625 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x626 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x627 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x628 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x629 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x630 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x631 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x632 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x633 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x634 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x635 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x636 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x637 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x638 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x639 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x640 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x641 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x642 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x643 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x644 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x645 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x646 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x647 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x648 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x649 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x650 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x651 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x652 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x653 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x654 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x655 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x656 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x657 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x658 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x659 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x660 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x661 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x662 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x663 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x664 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x665 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x666 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x667 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x668 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x669 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x670 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x671 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x672 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x673 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x674 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x675 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x676 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x677 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x678 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x679 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x680 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x681 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x682 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x683 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x684 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x685 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x686 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x687 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x688 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x689 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x690 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x691 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x692 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x693 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x694 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x695 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x696 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x697 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x698 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x699 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x700 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x701 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x702 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x703 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x704 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x705 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x706 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x707 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x708 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x709 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x710 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x711 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x712 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x713 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x714 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x715 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x716 = Var(within=Reals,bounds=(60,360),initialize=60)
m.x717 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x718 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x719 = Var(within=Reals,bounds=(60,410),initialize=60)
m.x720 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x721 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x722 = Var(within=Reals,bounds=(60,550),initialize=60)
m.x723 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x724 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x725 = Var(within=Reals,bounds=(110,960),initialize=110)
m.x726 = Var(within=Reals,bounds=(110,980),initialize=110)
m.x727 = Var(within=Reals,bounds=(110,980),initialize=110)
m.x728 = Var(within=Reals,bounds=(110,980),initialize=110)
m.x729 = Var(within=Reals,bounds=(110,980),initialize=110)
m.x730 = Var(within=Reals,bounds=(110,980),initialize=110)
m.x731 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x732 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x733 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x734 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x735 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x736 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x737 = Var(within=Reals,bounds=(60,460),initialize=60)
m.x738 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x739 = Var(within=Reals,bounds=(60,570),initialize=60)
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
m.x775 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x776 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x777 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x778 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x779 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x780 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x781 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x782 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x783 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x784 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x785 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x836 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x837 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x838 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x839 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x840 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x841 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x842 = Var(within=Reals,bounds=(0.138888888888889,0.142857142857143),initialize=0.138888888888889)
m.x843 = Var(within=Reals,bounds=(0.0146198830409357,0.142857142857143),initialize=0.0146198830409357)
m.x844 = Var(within=Reals,bounds=(0.0015389350569406,0.142857142857143),initialize=0.0015389350569406)
m.x845 = Var(within=Reals,bounds=(0.285714285714286,0.305555555555556),initialize=0.285714285714286)
m.x846 = Var(within=Reals,bounds=(0.0300751879699248,0.387755102040816),initialize=0.0300751879699248)
m.x847 = Var(within=Reals,bounds=(0.00316580925999209,0.387755102040816),initialize=0.00316580925999209)
m.x848 = Var(within=Reals,bounds=(0.277777777777778,0.285714285714286),initialize=0.277777777777778)
m.x849 = Var(within=Reals,bounds=(0.0292397660818713,0.923469387755102),initialize=0.0292397660818713)
m.x850 = Var(within=Reals,bounds=(0.00307787011388119,0.973242158465884),initialize=0.00307787011388119)
m.x851 = Var(within=Reals,bounds=(0.277777777777778,0.285714285714286),initialize=0.277777777777778)
m.x852 = Var(within=Reals,bounds=(0.0292397660818713,0.880952380952381),initialize=0.0292397660818713)
m.x853 = Var(within=Reals,bounds=(0.00307787011388119,0.880952380952381),initialize=0.00307787011388119)
m.x854 = Var(within=Reals,bounds=(0.25,0.268292682926829),initialize=0.25)
m.x855 = Var(within=Reals,bounds=(0.0263157894736842,0.831144465290807),initialize=0.0263157894736842)
m.x856 = Var(within=Reals,bounds=(0.00277008310249307,0.845714285714286),initialize=0.00277008310249307)
m.x857 = Var(within=Reals,bounds=(0.24390243902439,0.25),initialize=0.24390243902439)
m.x858 = Var(within=Reals,bounds=(0.0256739409499358,0.854838709677419),initialize=0.0256739409499358)
m.x859 = Var(within=Reals,bounds=(0.00270252009999324,0.854838709677419),initialize=0.00270252009999324)
m.x860 = Var(within=Reals,bounds=(0.24390243902439,0.25),initialize=0.24390243902439)
m.x861 = Var(within=Reals,bounds=(0.0256739409499358,0.25),initialize=0.0256739409499358)
m.x862 = Var(within=Reals,bounds=(0.00270252009999324,0.25),initialize=0.00270252009999324)
m.x863 = Var(within=Reals,bounds=(0.24390243902439,0.25),initialize=0.24390243902439)
m.x864 = Var(within=Reals,bounds=(0.0256739409499358,0.85),initialize=0.0256739409499358)
m.x865 = Var(within=Reals,bounds=(0.00270252009999324,0.85),initialize=0.00270252009999324)
m.x866 = Var(within=Reals,bounds=(0.285714285714286,0.545454545454545),initialize=0.285714285714286)
m.x867 = Var(within=Reals,bounds=(0.0300751879699248,0.853061224489796),initialize=0.0300751879699248)
m.x868 = Var(within=Reals,bounds=(0.00316580925999209,0.853061224489796),initialize=0.00316580925999209)
m.x869 = Var(within=Reals,bounds=(0.181818181818182,0.285714285714286),initialize=0.181818181818182)
m.x870 = Var(within=Reals,bounds=(0.0191387559808612,0.861751152073733),initialize=0.0191387559808612)
m.x871 = Var(within=Reals,bounds=(0.00201460589272224,0.861751152073733),initialize=0.00201460589272224)
m.x872 = Var(within=Reals,bounds=(0.0909090909090909,0.142857142857143),initialize=0.0909090909090909)
m.x873 = Var(within=Reals,bounds=(0.00956937799043062,0.142857142857143),initialize=0.00956937799043062)
m.x874 = Var(within=Reals,bounds=(0.00100730294636112,0.142857142857143),initialize=0.00100730294636112)
m.x875 = Var(within=Reals,bounds=(0.181818181818182,0.285714285714286),initialize=0.181818181818182)
m.x876 = Var(within=Reals,bounds=(0.0191387559808612,0.857142857142857),initialize=0.0191387559808612)
m.x877 = Var(within=Reals,bounds=(0.00201460589272224,0.857142857142857),initialize=0.00201460589272224)
m.x878 = Var(within=Reals,bounds=(0.210526315789474,0.21875),initialize=0.210526315789474)
m.x879 = Var(within=Reals,bounds=(0.0236305048335123,0.722782258064516),initialize=0.0236305048335123)
m.x880 = Var(within=Reals,bounds=(0.00265240360376159,0.734649122807018),initialize=0.00265240360376159)
m.x881 = Var(within=Reals,bounds=(0.260416666666667,0.263157894736842),initialize=0.260416666666667)
m.x882 = Var(within=Reals,bounds=(0.0292304421768707,0.774853801169591),initialize=0.0292304421768707)
m.x883 = Var(within=Reals,bounds=(0.00328096799944468,0.774853801169591),initialize=0.00328096799944468)
m.x884 = Var(within=Reals,bounds=(0.208333333333333,0.210526315789474),initialize=0.208333333333333)
m.x885 = Var(within=Reals,bounds=(0.0233843537414966,0.210526315789474),initialize=0.0233843537414966)
m.x886 = Var(within=Reals,bounds=(0.00262477439955574,0.210526315789474),initialize=0.00262477439955574)
m.x887 = Var(within=Reals,bounds=(0.3125,0.315789473684211),initialize=0.3125)
m.x888 = Var(within=Reals,bounds=(0.0350765306122449,0.784962406015038),initialize=0.0350765306122449)
m.x889 = Var(within=Reals,bounds=(0.00393716159933361,0.784962406015038),initialize=0.00393716159933361)
m.x890 = Var(within=Reals,bounds=(0.126582278481013,0.6),initialize=0.126582278481013)
m.x891 = Var(within=Reals,bounds=(0.0142082149315422,0.775925925925926),initialize=0.0142082149315422)
m.x892 = Var(within=Reals,bounds=(0.00159479963517311,0.775925925925926),initialize=0.00159479963517311)
m.x893 = Var(within=Reals,bounds=(0.135135135135135,0.636363636363636),initialize=0.135135135135135)
m.x894 = Var(within=Reals,bounds=(0.0151682294539437,0.796296296296296),initialize=0.0151682294539437)
m.x895 = Var(within=Reals,bounds=(0.0017025563672794,0.796296296296296),initialize=0.0017025563672794)
m.x896 = Var(within=Reals,bounds=(0.0510204081632653,0.166666666666667),initialize=0.0510204081632653)
m.x897 = Var(within=Reals,bounds=(0.00572678050812162,0.166666666666667),initialize=0.00572678050812162)
m.x898 = Var(within=Reals,bounds=(0.000642801893768753,0.166666666666667),initialize=0.000642801893768753)
m.x899 = Var(within=Reals,bounds=(0.0666666666666667,0.537037037037037),initialize=0.0666666666666667)
m.x900 = Var(within=Reals,bounds=(0.00748299319727891,0.738095238095238),initialize=0.00748299319727891)
m.x901 = Var(within=Reals,bounds=(0.000839927807857837,0.738095238095238),initialize=0.000839927807857837)
m.x902 = Var(within=Reals,bounds=(0.0350877192982456,0.25),initialize=0.0350877192982456)
m.x903 = Var(within=Reals,bounds=(0.00369344413665743,0.25),initialize=0.00369344413665743)
m.x904 = Var(within=Reals,bounds=(0.000388783593332361,0.25),initialize=0.000388783593332361)
m.x905 = Var(within=Reals,bounds=(0.0350877192982456,0.333333333333333),initialize=0.0350877192982456)
m.x906 = Var(within=Reals,bounds=(0.00369344413665743,0.357142857142857),initialize=0.00369344413665743)
m.x907 = Var(within=Reals,bounds=(0.000388783593332361,0.357142857142857),initialize=0.000388783593332361)
m.x908 = Var(within=Reals,bounds=(0.0512820512820513,0.894736842105263),initialize=0.0512820512820513)
m.x909 = Var(within=Reals,bounds=(0.00539811066126856,0.971904266389178),initialize=0.00539811066126856)
m.x910 = Var(within=Reals,bounds=(0.000568222174870374,0.971904266389178),initialize=0.000568222174870374)
m.x911 = Var(within=Reals,bounds=(0.0350877192982456,0.842105263157895),initialize=0.0350877192982456)
m.x912 = Var(within=Reals,bounds=(0.00369344413665743,0.875),initialize=0.00369344413665743)
m.x913 = Var(within=Reals,bounds=(0.000388783593332361,0.875),initialize=0.000388783593332361)
m.x914 = Var(within=Reals,bounds=(0.0350877192982456,0.25),initialize=0.0350877192982456)
m.x915 = Var(within=Reals,bounds=(0.00369344413665743,0.25),initialize=0.00369344413665743)
m.x916 = Var(within=Reals,bounds=(0.000388783593332361,0.25),initialize=0.000388783593332361)
m.x917 = Var(within=Reals,bounds=(0.0350877192982456,0.333333333333333),initialize=0.0350877192982456)
m.x918 = Var(within=Reals,bounds=(0.00369344413665743,0.357142857142857),initialize=0.00369344413665743)
m.x919 = Var(within=Reals,bounds=(0.000388783593332361,0.357142857142857),initialize=0.000388783593332361)
m.x920 = Var(within=Reals,bounds=(0.0512820512820513,0.894736842105263),initialize=0.0512820512820513)
m.x921 = Var(within=Reals,bounds=(0.00539811066126856,0.971904266389178),initialize=0.00539811066126856)
m.x922 = Var(within=Reals,bounds=(0.000568222174870374,0.971904266389178),initialize=0.000568222174870374)
m.x923 = Var(within=Reals,bounds=(0.0350877192982456,0.842105263157895),initialize=0.0350877192982456)
m.x924 = Var(within=Reals,bounds=(0.00369344413665743,0.875),initialize=0.00369344413665743)
m.x925 = Var(within=Reals,bounds=(0.000388783593332361,0.875),initialize=0.000388783593332361)
m.x926 = Var(within=Reals,bounds=(0.217391304347826,0.222222222222222),initialize=0.217391304347826)
m.x927 = Var(within=Reals,bounds=(0.022883295194508,0.222222222222222),initialize=0.022883295194508)
m.x928 = Var(within=Reals,bounds=(0.00240876791521137,0.222222222222222),initialize=0.00240876791521137)
m.x929 = Var(within=Reals,bounds=(0.222222222222222,0.239130434782609),initialize=0.222222222222222)
m.x930 = Var(within=Reals,bounds=(0.0233918128654971,0.333333333333333),initialize=0.0233918128654971)
m.x931 = Var(within=Reals,bounds=(0.00246229609110496,0.333333333333333),initialize=0.00246229609110496)
m.x932 = Var(within=Reals,bounds=(0.217391304347826,0.222222222222222),initialize=0.217391304347826)
m.x933 = Var(within=Reals,bounds=(0.022883295194508,0.916666666666667),initialize=0.022883295194508)
m.x934 = Var(within=Reals,bounds=(0.00240876791521137,0.970863683662851),initialize=0.00240876791521137)
m.x935 = Var(within=Reals,bounds=(0.326086956521739,0.333333333333333),initialize=0.326086956521739)
m.x936 = Var(within=Reals,bounds=(0.034324942791762,0.888888888888889),initialize=0.034324942791762)
m.x937 = Var(within=Reals,bounds=(0.00361315187281705,0.888888888888889),initialize=0.00361315187281705)
m.x938 = Var(within=Reals,bounds=(0,1500),initialize=0)
m.x939 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x940 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   1.5*m.x169 + 1.5*m.x170 + 1.5*m.x171 + 1.7*m.x172 + 1.7*m.x173 + 1.7*m.x174 + 1.5*m.x175
                        + 1.5*m.x176 + 1.5*m.x177 + 1.6*m.x178 + 1.6*m.x179 + 1.6*m.x180 + 1.45*m.x181 + 1.45*m.x182
                        + 1.45*m.x183 + 1.6*m.x184 + 1.6*m.x185 + 1.6*m.x186 + 1.55*m.x187 + 1.55*m.x188 + 1.55*m.x189
                        + 0.5*m.x190 + 0.5*m.x191 + 0.5*m.x192 + 1.45*m.x193 + 1.45*m.x194 + 1.45*m.x195 + 1.6*m.x196
                        + 1.6*m.x197 + 1.6*m.x198 + 1.55*m.x199 + 1.55*m.x200 + 1.55*m.x201 + 0.5*m.x202 + 0.5*m.x203
                        + 0.5*m.x204 + 1.45*m.x205 + 1.45*m.x206 + 1.45*m.x207 + 1.6*m.x208 + 1.6*m.x209 + 1.6*m.x210
                        + 1.55*m.x211 + 1.55*m.x212 + 1.55*m.x213 + 0.5*m.x214 + 0.5*m.x215 + 0.5*m.x216 + 1.45*m.x217
                        + 1.45*m.x218 + 1.45*m.x219 + 1.6*m.x220 + 1.6*m.x221 + 1.6*m.x222 + 1.55*m.x223 + 1.55*m.x224
                        + 1.55*m.x225 + 0.5*m.x226 + 0.5*m.x227 + 0.5*m.x228 + 1.45*m.x229 + 1.45*m.x230 + 1.45*m.x231
                        + 1.6*m.x232 + 1.6*m.x233 + 1.6*m.x234 + 1.55*m.x235 + 1.55*m.x236 + 1.55*m.x237 + 0.5*m.x238
                        + 0.5*m.x239 + 0.5*m.x240 + 1.45*m.x241 + 1.45*m.x242 + 1.45*m.x243 + 1.6*m.x244 + 1.6*m.x245
                        + 1.6*m.x246 + 1.55*m.x247 + 1.55*m.x248 + 1.55*m.x249 + 0.5*m.x250 + 0.5*m.x251 + 0.5*m.x252
                        + 1.45*m.x253 + 1.45*m.x254 + 1.45*m.x255 + 1.6*m.x256 + 1.6*m.x257 + 1.6*m.x258 + 1.55*m.x259
                        + 1.55*m.x260 + 1.55*m.x261 + 0.5*m.x262 + 0.5*m.x263 + 0.5*m.x264 + 1.45*m.x265 + 1.45*m.x266
                        + 1.45*m.x267 + 1.6*m.x268 + 1.6*m.x269 + 1.6*m.x270 + 1.55*m.x271 + 1.55*m.x272 + 1.55*m.x273
                        + 0.5*m.x274 + 0.5*m.x275 + 0.5*m.x276 + 1.5*m.x277 + 1.5*m.x278 + 1.5*m.x279 + 1.7*m.x280
                        + 1.7*m.x281 + 1.7*m.x282 + 1.5*m.x283 + 1.5*m.x284 + 1.5*m.x285 + 1.6*m.x286 + 1.6*m.x287
                        + 1.6*m.x288 + 1.5*m.x289 + 1.5*m.x290 + 1.5*m.x291 + 1.7*m.x292 + 1.7*m.x293 + 1.7*m.x294
                        + 1.5*m.x295 + 1.5*m.x296 + 1.5*m.x297 + 1.6*m.x298 + 1.6*m.x299 + 1.6*m.x300 + 1.5*m.x301
                        + 1.5*m.x302 + 1.5*m.x303 + 1.7*m.x304 + 1.7*m.x305 + 1.7*m.x306 + 1.5*m.x307 + 1.5*m.x308
                        + 1.5*m.x309 + 1.6*m.x310 + 1.6*m.x311 + 1.6*m.x312 - 10*m.x836 - 10*m.x837 - 10*m.x838
                        - 10*m.x839 - 10*m.x840 - 10*m.x841 - 4*m.x938 - m.x939 - m.x940, sense=maximize)

m.c1 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8 + m.b9 + m.b10 + m.b11 + m.b12 == 1)

m.c2 = Constraint(expr=   m.b13 + m.b14 + m.b15 + m.b16 + m.b17 + m.b18 + m.b19 + m.b20 + m.b21 + m.b22 + m.b23 + m.b24
                        == 1)

m.c3 = Constraint(expr=   m.b25 + m.b26 + m.b27 + m.b28 + m.b29 + m.b30 + m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36
                        == 1)

m.c4 = Constraint(expr=   m.b37 + m.b38 + m.b39 + m.b40 + m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 + m.b47 + m.b48
                        == 1)

m.c5 = Constraint(expr=   m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 + m.b55 + m.b56 + m.b57 + m.b58 + m.b59 + m.b60
                        == 1)

m.c6 = Constraint(expr=   m.b61 + m.b62 + m.b63 + m.b64 + m.b65 + m.b66 + m.b67 + m.b68 + m.b69 + m.b70 + m.b71 + m.b72
                        == 1)

m.c7 = Constraint(expr=   m.b73 + m.b74 + m.b75 + m.b76 + m.b77 + m.b78 + m.b79 + m.b80 + m.b81 + m.b82 + m.b83 + m.b84
                        == 1)

m.c8 = Constraint(expr=   m.b85 + m.b86 + m.b87 + m.b88 + m.b89 + m.b90 + m.b91 + m.b92 + m.b93 + m.b94 + m.b95 + m.b96
                        == 1)

m.c9 = Constraint(expr= - m.x322 - 1.25*m.x434 + 1.25*m.x530 <= 0)

m.c10 = Constraint(expr= - m.x323 - 1.25*m.x435 + 1.25*m.x531 <= 0)

m.c11 = Constraint(expr= - m.x324 - 1.25*m.x436 + 1.25*m.x532 <= 0)

m.c12 = Constraint(expr= - m.x325 - 1.25*m.x437 + 1.25*m.x533 <= 0)

m.c13 = Constraint(expr= - m.x326 - 1.25*m.x438 + 1.25*m.x534 <= 0)

m.c14 = Constraint(expr= - m.x327 - 1.25*m.x439 + 1.25*m.x535 <= 0)

m.c15 = Constraint(expr= - m.x328 - 1.25*m.x440 + 1.25*m.x536 <= 0)

m.c16 = Constraint(expr= - m.x329 - 1.25*m.x441 + 1.25*m.x537 <= 0)

m.c17 = Constraint(expr= - m.x330 - 1.25*m.x442 + 1.25*m.x538 <= 0)

m.c18 = Constraint(expr= - m.x331 - 1.25*m.x443 + 1.25*m.x539 <= 0)

m.c19 = Constraint(expr= - m.x332 - 1.25*m.x444 + 1.25*m.x540 <= 0)

m.c20 = Constraint(expr= - m.x333 - 1.25*m.x445 + 1.25*m.x541 <= 0)

m.c21 = Constraint(expr= - m.x334 - 1.25*m.x446 + 1.25*m.x542 <= 0)

m.c22 = Constraint(expr= - m.x335 - 1.25*m.x447 + 1.25*m.x543 <= 0)

m.c23 = Constraint(expr= - m.x336 - 1.25*m.x448 + 1.25*m.x544 <= 0)

m.c24 = Constraint(expr= - m.x337 - 1.25*m.x449 + 1.25*m.x545 <= 0)

m.c25 = Constraint(expr= - m.x338 - 1.25*m.x450 + 1.25*m.x546 <= 0)

m.c26 = Constraint(expr= - m.x339 - 1.25*m.x451 + 1.25*m.x547 <= 0)

m.c27 = Constraint(expr= - m.x340 - 1.25*m.x452 + 1.25*m.x548 <= 0)

m.c28 = Constraint(expr= - m.x341 - 1.25*m.x453 + 1.25*m.x549 <= 0)

m.c29 = Constraint(expr= - m.x342 - 1.25*m.x454 + 1.25*m.x550 <= 0)

m.c30 = Constraint(expr= - m.x343 - 1.25*m.x455 + 1.25*m.x551 <= 0)

m.c31 = Constraint(expr= - m.x344 - 1.25*m.x456 + 1.25*m.x552 <= 0)

m.c32 = Constraint(expr= - m.x345 - 1.25*m.x457 + 1.25*m.x553 <= 0)

m.c33 = Constraint(expr= - m.x346 - 1.25*m.x458 + 1.25*m.x554 <= 0)

m.c34 = Constraint(expr= - m.x347 - 1.25*m.x459 + 1.25*m.x555 <= 0)

m.c35 = Constraint(expr= - m.x348 - 1.25*m.x460 + 1.25*m.x556 <= 0)

m.c36 = Constraint(expr= - m.x349 - 1.25*m.x461 + 1.25*m.x557 <= 0)

m.c37 = Constraint(expr= - m.x350 - 1.25*m.x462 + 1.25*m.x558 <= 0)

m.c38 = Constraint(expr= - m.x351 - 1.25*m.x463 + 1.25*m.x559 <= 0)

m.c39 = Constraint(expr= - m.x352 - 1.25*m.x464 + 1.25*m.x560 <= 0)

m.c40 = Constraint(expr= - m.x353 - 1.25*m.x465 + 1.25*m.x561 <= 0)

m.c41 = Constraint(expr= - m.x354 - 1.25*m.x466 + 1.25*m.x562 <= 0)

m.c42 = Constraint(expr= - m.x355 - 1.25*m.x467 + 1.25*m.x563 <= 0)

m.c43 = Constraint(expr= - m.x356 - 1.25*m.x468 + 1.25*m.x564 <= 0)

m.c44 = Constraint(expr= - m.x357 - 1.25*m.x469 + 1.25*m.x565 <= 0)

m.c45 = Constraint(expr= - m.x358 - 1.25*m.x470 + 1.25*m.x566 <= 0)

m.c46 = Constraint(expr= - m.x359 - 1.25*m.x471 + 1.25*m.x567 <= 0)

m.c47 = Constraint(expr= - m.x360 - 1.25*m.x472 + 1.25*m.x568 <= 0)

m.c48 = Constraint(expr= - m.x361 - 1.25*m.x473 + 1.25*m.x569 <= 0)

m.c49 = Constraint(expr= - m.x362 - 1.25*m.x474 + 1.25*m.x570 <= 0)

m.c50 = Constraint(expr= - m.x363 - 1.25*m.x475 + 1.25*m.x571 <= 0)

m.c51 = Constraint(expr= - m.x364 - 1.25*m.x476 + 1.25*m.x572 <= 0)

m.c52 = Constraint(expr= - m.x365 - 1.25*m.x477 + 1.25*m.x573 <= 0)

m.c53 = Constraint(expr= - m.x366 - 1.25*m.x478 + 1.25*m.x574 <= 0)

m.c54 = Constraint(expr= - m.x367 - 1.25*m.x479 + 1.25*m.x575 <= 0)

m.c55 = Constraint(expr= - m.x368 - 1.25*m.x480 + 1.25*m.x576 <= 0)

m.c56 = Constraint(expr= - m.x369 - 1.25*m.x481 + 1.25*m.x577 <= 0)

m.c57 = Constraint(expr= - m.x370 - 1.25*m.x482 + 1.25*m.x578 <= 0)

m.c58 = Constraint(expr= - m.x371 - 1.25*m.x483 + 1.25*m.x579 <= 0)

m.c59 = Constraint(expr= - m.x372 - 1.25*m.x484 + 1.25*m.x580 <= 0)

m.c60 = Constraint(expr= - m.x373 - 1.25*m.x485 + 1.25*m.x581 <= 0)

m.c61 = Constraint(expr= - m.x374 - 1.25*m.x486 + 1.25*m.x582 <= 0)

m.c62 = Constraint(expr= - m.x375 - 1.25*m.x487 + 1.25*m.x583 <= 0)

m.c63 = Constraint(expr= - m.x376 - 1.25*m.x488 + 1.25*m.x584 <= 0)

m.c64 = Constraint(expr= - m.x377 - 1.25*m.x489 + 1.25*m.x585 <= 0)

m.c65 = Constraint(expr= - m.x378 - 1.25*m.x490 + 1.25*m.x586 <= 0)

m.c66 = Constraint(expr= - m.x379 - 1.25*m.x491 + 1.25*m.x587 <= 0)

m.c67 = Constraint(expr= - m.x380 - 1.25*m.x492 + 1.25*m.x588 <= 0)

m.c68 = Constraint(expr= - m.x381 - 1.25*m.x493 + 1.25*m.x589 <= 0)

m.c69 = Constraint(expr= - m.x382 - 1.25*m.x494 + 1.25*m.x590 <= 0)

m.c70 = Constraint(expr= - m.x383 - 1.25*m.x495 + 1.25*m.x591 <= 0)

m.c71 = Constraint(expr= - m.x384 - 1.25*m.x496 + 1.25*m.x592 <= 0)

m.c72 = Constraint(expr= - m.x385 - 1.25*m.x497 + 1.25*m.x593 <= 0)

m.c73 = Constraint(expr= - m.x386 - 1.25*m.x498 + 1.25*m.x594 <= 0)

m.c74 = Constraint(expr= - m.x387 - 1.25*m.x499 + 1.25*m.x595 <= 0)

m.c75 = Constraint(expr= - m.x388 - 1.25*m.x500 + 1.25*m.x596 <= 0)

m.c76 = Constraint(expr= - m.x389 - 1.25*m.x501 + 1.25*m.x597 <= 0)

m.c77 = Constraint(expr= - m.x390 - 1.25*m.x502 + 1.25*m.x598 <= 0)

m.c78 = Constraint(expr= - m.x391 - 1.25*m.x503 + 1.25*m.x599 <= 0)

m.c79 = Constraint(expr= - m.x392 - 1.25*m.x504 + 1.25*m.x600 <= 0)

m.c80 = Constraint(expr= - m.x393 - 1.25*m.x505 + 1.25*m.x601 <= 0)

m.c81 = Constraint(expr= - m.x394 - 1.25*m.x506 + 1.25*m.x602 <= 0)

m.c82 = Constraint(expr= - m.x395 - 1.25*m.x507 + 1.25*m.x603 <= 0)

m.c83 = Constraint(expr= - m.x396 - 1.25*m.x508 + 1.25*m.x604 <= 0)

m.c84 = Constraint(expr= - m.x397 - 1.25*m.x509 + 1.25*m.x605 <= 0)

m.c85 = Constraint(expr= - m.x398 - 1.25*m.x510 + 1.25*m.x606 <= 0)

m.c86 = Constraint(expr= - m.x399 - 1.25*m.x511 + 1.25*m.x607 <= 0)

m.c87 = Constraint(expr= - m.x400 - 1.25*m.x512 + 1.25*m.x608 <= 0)

m.c88 = Constraint(expr= - m.x401 - 1.25*m.x513 + 1.25*m.x609 <= 0)

m.c89 = Constraint(expr= - m.x402 - 1.25*m.x514 + 1.25*m.x610 <= 0)

m.c90 = Constraint(expr= - m.x403 - 1.25*m.x515 + 1.25*m.x611 <= 0)

m.c91 = Constraint(expr= - m.x404 - 1.25*m.x516 + 1.25*m.x612 <= 0)

m.c92 = Constraint(expr= - m.x405 - 1.25*m.x517 + 1.25*m.x613 <= 0)

m.c93 = Constraint(expr= - m.x406 - 1.25*m.x518 + 1.25*m.x614 <= 0)

m.c94 = Constraint(expr= - m.x407 - 1.25*m.x519 + 1.25*m.x615 <= 0)

m.c95 = Constraint(expr= - m.x408 - 1.25*m.x520 + 1.25*m.x616 <= 0)

m.c96 = Constraint(expr= - m.x409 - 1.25*m.x521 + 1.25*m.x617 <= 0)

m.c97 = Constraint(expr= - m.x410 - 1.25*m.x522 + 1.25*m.x618 <= 0)

m.c98 = Constraint(expr= - m.x411 - 1.25*m.x523 + 1.25*m.x619 <= 0)

m.c99 = Constraint(expr= - m.x412 - 1.25*m.x524 + 1.25*m.x620 <= 0)

m.c100 = Constraint(expr= - m.x413 - 1.25*m.x525 + 1.25*m.x621 <= 0)

m.c101 = Constraint(expr= - m.x414 - 1.25*m.x526 + 1.25*m.x622 <= 0)

m.c102 = Constraint(expr= - m.x415 - 1.25*m.x527 + 1.25*m.x623 <= 0)

m.c103 = Constraint(expr= - m.x416 - 1.25*m.x528 + 1.25*m.x624 <= 0)

m.c104 = Constraint(expr= - m.x417 - 1.25*m.x529 + 1.25*m.x625 <= 0)

m.c105 = Constraint(expr=   m.x322 + 50*m.x434 - 50*m.x530 <= 0)

m.c106 = Constraint(expr=   m.x323 + 50*m.x435 - 50*m.x531 <= 0)

m.c107 = Constraint(expr=   m.x324 + 50*m.x436 - 50*m.x532 <= 0)

m.c108 = Constraint(expr=   m.x325 + 50*m.x437 - 50*m.x533 <= 0)

m.c109 = Constraint(expr=   m.x326 + 50*m.x438 - 50*m.x534 <= 0)

m.c110 = Constraint(expr=   m.x327 + 50*m.x439 - 50*m.x535 <= 0)

m.c111 = Constraint(expr=   m.x328 + 50*m.x440 - 50*m.x536 <= 0)

m.c112 = Constraint(expr=   m.x329 + 50*m.x441 - 50*m.x537 <= 0)

m.c113 = Constraint(expr=   m.x330 + 50*m.x442 - 50*m.x538 <= 0)

m.c114 = Constraint(expr=   m.x331 + 50*m.x443 - 50*m.x539 <= 0)

m.c115 = Constraint(expr=   m.x332 + 50*m.x444 - 50*m.x540 <= 0)

m.c116 = Constraint(expr=   m.x333 + 50*m.x445 - 50*m.x541 <= 0)

m.c117 = Constraint(expr=   m.x334 + 50*m.x446 - 50*m.x542 <= 0)

m.c118 = Constraint(expr=   m.x335 + 50*m.x447 - 50*m.x543 <= 0)

m.c119 = Constraint(expr=   m.x336 + 50*m.x448 - 50*m.x544 <= 0)

m.c120 = Constraint(expr=   m.x337 + 50*m.x449 - 50*m.x545 <= 0)

m.c121 = Constraint(expr=   m.x338 + 50*m.x450 - 50*m.x546 <= 0)

m.c122 = Constraint(expr=   m.x339 + 50*m.x451 - 50*m.x547 <= 0)

m.c123 = Constraint(expr=   m.x340 + 50*m.x452 - 50*m.x548 <= 0)

m.c124 = Constraint(expr=   m.x341 + 50*m.x453 - 50*m.x549 <= 0)

m.c125 = Constraint(expr=   m.x342 + 50*m.x454 - 50*m.x550 <= 0)

m.c126 = Constraint(expr=   m.x343 + 50*m.x455 - 50*m.x551 <= 0)

m.c127 = Constraint(expr=   m.x344 + 50*m.x456 - 50*m.x552 <= 0)

m.c128 = Constraint(expr=   m.x345 + 50*m.x457 - 50*m.x553 <= 0)

m.c129 = Constraint(expr=   m.x346 + 50*m.x458 - 50*m.x554 <= 0)

m.c130 = Constraint(expr=   m.x347 + 50*m.x459 - 50*m.x555 <= 0)

m.c131 = Constraint(expr=   m.x348 + 50*m.x460 - 50*m.x556 <= 0)

m.c132 = Constraint(expr=   m.x349 + 50*m.x461 - 50*m.x557 <= 0)

m.c133 = Constraint(expr=   m.x350 + 50*m.x462 - 50*m.x558 <= 0)

m.c134 = Constraint(expr=   m.x351 + 50*m.x463 - 50*m.x559 <= 0)

m.c135 = Constraint(expr=   m.x352 + 50*m.x464 - 50*m.x560 <= 0)

m.c136 = Constraint(expr=   m.x353 + 50*m.x465 - 50*m.x561 <= 0)

m.c137 = Constraint(expr=   m.x354 + 50*m.x466 - 50*m.x562 <= 0)

m.c138 = Constraint(expr=   m.x355 + 50*m.x467 - 50*m.x563 <= 0)

m.c139 = Constraint(expr=   m.x356 + 50*m.x468 - 50*m.x564 <= 0)

m.c140 = Constraint(expr=   m.x357 + 50*m.x469 - 50*m.x565 <= 0)

m.c141 = Constraint(expr=   m.x358 + 50*m.x470 - 50*m.x566 <= 0)

m.c142 = Constraint(expr=   m.x359 + 50*m.x471 - 50*m.x567 <= 0)

m.c143 = Constraint(expr=   m.x360 + 50*m.x472 - 50*m.x568 <= 0)

m.c144 = Constraint(expr=   m.x361 + 50*m.x473 - 50*m.x569 <= 0)

m.c145 = Constraint(expr=   m.x362 + 50*m.x474 - 50*m.x570 <= 0)

m.c146 = Constraint(expr=   m.x363 + 50*m.x475 - 50*m.x571 <= 0)

m.c147 = Constraint(expr=   m.x364 + 50*m.x476 - 50*m.x572 <= 0)

m.c148 = Constraint(expr=   m.x365 + 50*m.x477 - 50*m.x573 <= 0)

m.c149 = Constraint(expr=   m.x366 + 50*m.x478 - 50*m.x574 <= 0)

m.c150 = Constraint(expr=   m.x367 + 50*m.x479 - 50*m.x575 <= 0)

m.c151 = Constraint(expr=   m.x368 + 50*m.x480 - 50*m.x576 <= 0)

m.c152 = Constraint(expr=   m.x369 + 50*m.x481 - 50*m.x577 <= 0)

m.c153 = Constraint(expr=   m.x370 + 50*m.x482 - 50*m.x578 <= 0)

m.c154 = Constraint(expr=   m.x371 + 50*m.x483 - 50*m.x579 <= 0)

m.c155 = Constraint(expr=   m.x372 + 50*m.x484 - 50*m.x580 <= 0)

m.c156 = Constraint(expr=   m.x373 + 50*m.x485 - 50*m.x581 <= 0)

m.c157 = Constraint(expr=   m.x374 + 50*m.x486 - 50*m.x582 <= 0)

m.c158 = Constraint(expr=   m.x375 + 50*m.x487 - 50*m.x583 <= 0)

m.c159 = Constraint(expr=   m.x376 + 50*m.x488 - 50*m.x584 <= 0)

m.c160 = Constraint(expr=   m.x377 + 50*m.x489 - 50*m.x585 <= 0)

m.c161 = Constraint(expr=   m.x378 + 50*m.x490 - 50*m.x586 <= 0)

m.c162 = Constraint(expr=   m.x379 + 50*m.x491 - 50*m.x587 <= 0)

m.c163 = Constraint(expr=   m.x380 + 50*m.x492 - 50*m.x588 <= 0)

m.c164 = Constraint(expr=   m.x381 + 50*m.x493 - 50*m.x589 <= 0)

m.c165 = Constraint(expr=   m.x382 + 50*m.x494 - 50*m.x590 <= 0)

m.c166 = Constraint(expr=   m.x383 + 50*m.x495 - 50*m.x591 <= 0)

m.c167 = Constraint(expr=   m.x384 + 50*m.x496 - 50*m.x592 <= 0)

m.c168 = Constraint(expr=   m.x385 + 50*m.x497 - 50*m.x593 <= 0)

m.c169 = Constraint(expr=   m.x386 + 50*m.x498 - 50*m.x594 <= 0)

m.c170 = Constraint(expr=   m.x387 + 50*m.x499 - 50*m.x595 <= 0)

m.c171 = Constraint(expr=   m.x388 + 50*m.x500 - 50*m.x596 <= 0)

m.c172 = Constraint(expr=   m.x389 + 50*m.x501 - 50*m.x597 <= 0)

m.c173 = Constraint(expr=   m.x390 + 50*m.x502 - 50*m.x598 <= 0)

m.c174 = Constraint(expr=   m.x391 + 50*m.x503 - 50*m.x599 <= 0)

m.c175 = Constraint(expr=   m.x392 + 50*m.x504 - 50*m.x600 <= 0)

m.c176 = Constraint(expr=   m.x393 + 50*m.x505 - 50*m.x601 <= 0)

m.c177 = Constraint(expr=   m.x394 + 50*m.x506 - 50*m.x602 <= 0)

m.c178 = Constraint(expr=   m.x395 + 50*m.x507 - 50*m.x603 <= 0)

m.c179 = Constraint(expr=   m.x396 + 50*m.x508 - 50*m.x604 <= 0)

m.c180 = Constraint(expr=   m.x397 + 50*m.x509 - 50*m.x605 <= 0)

m.c181 = Constraint(expr=   m.x398 + 50*m.x510 - 50*m.x606 <= 0)

m.c182 = Constraint(expr=   m.x399 + 50*m.x511 - 50*m.x607 <= 0)

m.c183 = Constraint(expr=   m.x400 + 50*m.x512 - 50*m.x608 <= 0)

m.c184 = Constraint(expr=   m.x401 + 50*m.x513 - 50*m.x609 <= 0)

m.c185 = Constraint(expr=   m.x402 + 50*m.x514 - 50*m.x610 <= 0)

m.c186 = Constraint(expr=   m.x403 + 50*m.x515 - 50*m.x611 <= 0)

m.c187 = Constraint(expr=   m.x404 + 50*m.x516 - 50*m.x612 <= 0)

m.c188 = Constraint(expr=   m.x405 + 50*m.x517 - 50*m.x613 <= 0)

m.c189 = Constraint(expr=   m.x406 + 50*m.x518 - 50*m.x614 <= 0)

m.c190 = Constraint(expr=   m.x407 + 50*m.x519 - 50*m.x615 <= 0)

m.c191 = Constraint(expr=   m.x408 + 50*m.x520 - 50*m.x616 <= 0)

m.c192 = Constraint(expr=   m.x409 + 50*m.x521 - 50*m.x617 <= 0)

m.c193 = Constraint(expr=   m.x410 + 50*m.x522 - 50*m.x618 <= 0)

m.c194 = Constraint(expr=   m.x411 + 50*m.x523 - 50*m.x619 <= 0)

m.c195 = Constraint(expr=   m.x412 + 50*m.x524 - 50*m.x620 <= 0)

m.c196 = Constraint(expr=   m.x413 + 50*m.x525 - 50*m.x621 <= 0)

m.c197 = Constraint(expr=   m.x414 + 50*m.x526 - 50*m.x622 <= 0)

m.c198 = Constraint(expr=   m.x415 + 50*m.x527 - 50*m.x623 <= 0)

m.c199 = Constraint(expr=   m.x416 + 50*m.x528 - 50*m.x624 <= 0)

m.c200 = Constraint(expr=   m.x417 + 50*m.x529 - 50*m.x625 <= 0)

m.c201 = Constraint(expr= - 10*m.b1 + m.x322 == 0)

m.c202 = Constraint(expr= - 10*m.b2 + m.x323 == 0)

m.c203 = Constraint(expr= - 10*m.b3 + m.x324 == 0)

m.c204 = Constraint(expr= - 10*m.b4 + m.x325 == 0)

m.c205 = Constraint(expr= - 10*m.b5 + m.x326 == 0)

m.c206 = Constraint(expr= - 10*m.b6 + m.x327 == 0)

m.c207 = Constraint(expr= - 10*m.b7 + m.x328 == 0)

m.c208 = Constraint(expr= - 10*m.b8 + m.x329 == 0)

m.c209 = Constraint(expr= - 10*m.b9 + m.x330 == 0)

m.c210 = Constraint(expr= - 10*m.b10 + m.x331 == 0)

m.c211 = Constraint(expr= - 10*m.b11 + m.x332 == 0)

m.c212 = Constraint(expr= - 10*m.b12 + m.x333 == 0)

m.c213 = Constraint(expr= - 250*m.b13 + m.x334 == 0)

m.c214 = Constraint(expr= - 250*m.b14 + m.x335 == 0)

m.c215 = Constraint(expr= - 250*m.b15 + m.x336 == 0)

m.c216 = Constraint(expr= - 250*m.b16 + m.x337 == 0)

m.c217 = Constraint(expr= - 250*m.b17 + m.x338 == 0)

m.c218 = Constraint(expr= - 250*m.b18 + m.x339 == 0)

m.c219 = Constraint(expr= - 250*m.b19 + m.x340 == 0)

m.c220 = Constraint(expr= - 250*m.b20 + m.x341 == 0)

m.c221 = Constraint(expr= - 250*m.b21 + m.x342 == 0)

m.c222 = Constraint(expr= - 250*m.b22 + m.x343 == 0)

m.c223 = Constraint(expr= - 250*m.b23 + m.x344 == 0)

m.c224 = Constraint(expr= - 250*m.b24 + m.x345 == 0)

m.c225 = Constraint(expr= - 300*m.b25 + m.x346 == 0)

m.c226 = Constraint(expr= - 300*m.b26 + m.x347 == 0)

m.c227 = Constraint(expr= - 300*m.b27 + m.x348 == 0)

m.c228 = Constraint(expr= - 300*m.b28 + m.x349 == 0)

m.c229 = Constraint(expr= - 300*m.b29 + m.x350 == 0)

m.c230 = Constraint(expr= - 300*m.b30 + m.x351 == 0)

m.c231 = Constraint(expr= - 300*m.b31 + m.x352 == 0)

m.c232 = Constraint(expr= - 300*m.b32 + m.x353 == 0)

m.c233 = Constraint(expr= - 300*m.b33 + m.x354 == 0)

m.c234 = Constraint(expr= - 300*m.b34 + m.x355 == 0)

m.c235 = Constraint(expr= - 300*m.b35 + m.x356 == 0)

m.c236 = Constraint(expr= - 300*m.b36 + m.x357 == 0)

m.c237 = Constraint(expr= - 190*m.b37 + m.x358 == 0)

m.c238 = Constraint(expr= - 190*m.b38 + m.x359 == 0)

m.c239 = Constraint(expr= - 190*m.b39 + m.x360 == 0)

m.c240 = Constraint(expr= - 190*m.b40 + m.x361 == 0)

m.c241 = Constraint(expr= - 190*m.b41 + m.x362 == 0)

m.c242 = Constraint(expr= - 190*m.b42 + m.x363 == 0)

m.c243 = Constraint(expr= - 190*m.b43 + m.x364 == 0)

m.c244 = Constraint(expr= - 190*m.b44 + m.x365 == 0)

m.c245 = Constraint(expr= - 190*m.b45 + m.x366 == 0)

m.c246 = Constraint(expr= - 190*m.b46 + m.x367 == 0)

m.c247 = Constraint(expr= - 190*m.b47 + m.x368 == 0)

m.c248 = Constraint(expr= - 190*m.b48 + m.x369 == 0)

m.c249 = Constraint(expr= - 10*m.b49 + m.x370 == 0)

m.c250 = Constraint(expr= - 10*m.b50 + m.x371 == 0)

m.c251 = Constraint(expr= - 10*m.b51 + m.x372 == 0)

m.c252 = Constraint(expr= - 10*m.b52 + m.x373 == 0)

m.c253 = Constraint(expr= - 10*m.b53 + m.x374 == 0)

m.c254 = Constraint(expr= - 10*m.b54 + m.x375 == 0)

m.c255 = Constraint(expr= - 10*m.b55 + m.x376 == 0)

m.c256 = Constraint(expr= - 10*m.b56 + m.x377 == 0)

m.c257 = Constraint(expr= - 10*m.b57 + m.x378 == 0)

m.c258 = Constraint(expr= - 10*m.b58 + m.x379 == 0)

m.c259 = Constraint(expr= - 10*m.b59 + m.x380 == 0)

m.c260 = Constraint(expr= - 10*m.b60 + m.x381 == 0)

m.c261 = Constraint(expr= - 250*m.b61 + m.x382 == 0)

m.c262 = Constraint(expr= - 250*m.b62 + m.x383 == 0)

m.c263 = Constraint(expr= - 250*m.b63 + m.x384 == 0)

m.c264 = Constraint(expr= - 250*m.b64 + m.x385 == 0)

m.c265 = Constraint(expr= - 250*m.b65 + m.x386 == 0)

m.c266 = Constraint(expr= - 250*m.b66 + m.x387 == 0)

m.c267 = Constraint(expr= - 250*m.b67 + m.x388 == 0)

m.c268 = Constraint(expr= - 250*m.b68 + m.x389 == 0)

m.c269 = Constraint(expr= - 250*m.b69 + m.x390 == 0)

m.c270 = Constraint(expr= - 250*m.b70 + m.x391 == 0)

m.c271 = Constraint(expr= - 250*m.b71 + m.x392 == 0)

m.c272 = Constraint(expr= - 250*m.b72 + m.x393 == 0)

m.c273 = Constraint(expr= - 250*m.b73 + m.x394 == 0)

m.c274 = Constraint(expr= - 250*m.b74 + m.x395 == 0)

m.c275 = Constraint(expr= - 250*m.b75 + m.x396 == 0)

m.c276 = Constraint(expr= - 250*m.b76 + m.x397 == 0)

m.c277 = Constraint(expr= - 250*m.b77 + m.x398 == 0)

m.c278 = Constraint(expr= - 250*m.b78 + m.x399 == 0)

m.c279 = Constraint(expr= - 250*m.b79 + m.x400 == 0)

m.c280 = Constraint(expr= - 250*m.b80 + m.x401 == 0)

m.c281 = Constraint(expr= - 250*m.b81 + m.x402 == 0)

m.c282 = Constraint(expr= - 250*m.b82 + m.x403 == 0)

m.c283 = Constraint(expr= - 250*m.b83 + m.x404 == 0)

m.c284 = Constraint(expr= - 250*m.b84 + m.x405 == 0)

m.c285 = Constraint(expr= - 240*m.b85 + m.x406 == 0)

m.c286 = Constraint(expr= - 240*m.b86 + m.x407 == 0)

m.c287 = Constraint(expr= - 240*m.b87 + m.x408 == 0)

m.c288 = Constraint(expr= - 240*m.b88 + m.x409 == 0)

m.c289 = Constraint(expr= - 240*m.b89 + m.x410 == 0)

m.c290 = Constraint(expr= - 240*m.b90 + m.x411 == 0)

m.c291 = Constraint(expr= - 240*m.b91 + m.x412 == 0)

m.c292 = Constraint(expr= - 240*m.b92 + m.x413 == 0)

m.c293 = Constraint(expr= - 240*m.b93 + m.x414 == 0)

m.c294 = Constraint(expr= - 240*m.b94 + m.x415 == 0)

m.c295 = Constraint(expr= - 240*m.b95 + m.x416 == 0)

m.c296 = Constraint(expr= - 240*m.b96 + m.x417 == 0)

m.c297 = Constraint(expr=   160*m.b1 + m.x418 - m.x434 <= 160)

m.c298 = Constraint(expr=   160*m.b2 + m.x418 - m.x435 <= 160)

m.c299 = Constraint(expr=   160*m.b3 + m.x418 - m.x436 <= 160)

m.c300 = Constraint(expr=   160*m.b4 + m.x418 - m.x437 <= 160)

m.c301 = Constraint(expr=   160*m.b5 + m.x418 - m.x438 <= 160)

m.c302 = Constraint(expr=   160*m.b6 + m.x418 - m.x439 <= 160)

m.c303 = Constraint(expr=   160*m.b7 + m.x418 - m.x440 <= 160)

m.c304 = Constraint(expr=   160*m.b8 + m.x418 - m.x441 <= 160)

m.c305 = Constraint(expr=   160*m.b9 + m.x418 - m.x442 <= 160)

m.c306 = Constraint(expr=   160*m.b10 + m.x418 - m.x443 <= 160)

m.c307 = Constraint(expr=   160*m.b11 + m.x418 - m.x444 <= 160)

m.c308 = Constraint(expr=   160*m.b12 + m.x418 - m.x445 <= 160)

m.c309 = Constraint(expr=   160*m.b13 + m.x419 - m.x446 <= 160)

m.c310 = Constraint(expr=   160*m.b14 + m.x419 - m.x447 <= 160)

m.c311 = Constraint(expr=   160*m.b15 + m.x419 - m.x448 <= 160)

m.c312 = Constraint(expr=   160*m.b16 + m.x419 - m.x449 <= 160)

m.c313 = Constraint(expr=   160*m.b17 + m.x419 - m.x450 <= 160)

m.c314 = Constraint(expr=   160*m.b18 + m.x419 - m.x451 <= 160)

m.c315 = Constraint(expr=   160*m.b19 + m.x419 - m.x452 <= 160)

m.c316 = Constraint(expr=   160*m.b20 + m.x419 - m.x453 <= 160)

m.c317 = Constraint(expr=   160*m.b21 + m.x419 - m.x454 <= 160)

m.c318 = Constraint(expr=   160*m.b22 + m.x419 - m.x455 <= 160)

m.c319 = Constraint(expr=   160*m.b23 + m.x419 - m.x456 <= 160)

m.c320 = Constraint(expr=   160*m.b24 + m.x419 - m.x457 <= 160)

m.c321 = Constraint(expr=   160*m.b25 + m.x420 - m.x458 <= 160)

m.c322 = Constraint(expr=   160*m.b26 + m.x420 - m.x459 <= 160)

m.c323 = Constraint(expr=   160*m.b27 + m.x420 - m.x460 <= 160)

m.c324 = Constraint(expr=   160*m.b28 + m.x420 - m.x461 <= 160)

m.c325 = Constraint(expr=   160*m.b29 + m.x420 - m.x462 <= 160)

m.c326 = Constraint(expr=   160*m.b30 + m.x420 - m.x463 <= 160)

m.c327 = Constraint(expr=   160*m.b31 + m.x420 - m.x464 <= 160)

m.c328 = Constraint(expr=   160*m.b32 + m.x420 - m.x465 <= 160)

m.c329 = Constraint(expr=   160*m.b33 + m.x420 - m.x466 <= 160)

m.c330 = Constraint(expr=   160*m.b34 + m.x420 - m.x467 <= 160)

m.c331 = Constraint(expr=   160*m.b35 + m.x420 - m.x468 <= 160)

m.c332 = Constraint(expr=   160*m.b36 + m.x420 - m.x469 <= 160)

m.c333 = Constraint(expr=   160*m.b37 + m.x421 - m.x470 <= 160)

m.c334 = Constraint(expr=   160*m.b38 + m.x421 - m.x471 <= 160)

m.c335 = Constraint(expr=   160*m.b39 + m.x421 - m.x472 <= 160)

m.c336 = Constraint(expr=   160*m.b40 + m.x421 - m.x473 <= 160)

m.c337 = Constraint(expr=   160*m.b41 + m.x421 - m.x474 <= 160)

m.c338 = Constraint(expr=   160*m.b42 + m.x421 - m.x475 <= 160)

m.c339 = Constraint(expr=   160*m.b43 + m.x421 - m.x476 <= 160)

m.c340 = Constraint(expr=   160*m.b44 + m.x421 - m.x477 <= 160)

m.c341 = Constraint(expr=   160*m.b45 + m.x421 - m.x478 <= 160)

m.c342 = Constraint(expr=   160*m.b46 + m.x421 - m.x479 <= 160)

m.c343 = Constraint(expr=   160*m.b47 + m.x421 - m.x480 <= 160)

m.c344 = Constraint(expr=   160*m.b48 + m.x421 - m.x481 <= 160)

m.c345 = Constraint(expr=   160*m.b49 + m.x422 - m.x482 <= 160)

m.c346 = Constraint(expr=   160*m.b50 + m.x422 - m.x483 <= 160)

m.c347 = Constraint(expr=   160*m.b51 + m.x422 - m.x484 <= 160)

m.c348 = Constraint(expr=   160*m.b52 + m.x422 - m.x485 <= 160)

m.c349 = Constraint(expr=   160*m.b53 + m.x422 - m.x486 <= 160)

m.c350 = Constraint(expr=   160*m.b54 + m.x422 - m.x487 <= 160)

m.c351 = Constraint(expr=   160*m.b55 + m.x422 - m.x488 <= 160)

m.c352 = Constraint(expr=   160*m.b56 + m.x422 - m.x489 <= 160)

m.c353 = Constraint(expr=   160*m.b57 + m.x422 - m.x490 <= 160)

m.c354 = Constraint(expr=   160*m.b58 + m.x422 - m.x491 <= 160)

m.c355 = Constraint(expr=   160*m.b59 + m.x422 - m.x492 <= 160)

m.c356 = Constraint(expr=   160*m.b60 + m.x422 - m.x493 <= 160)

m.c357 = Constraint(expr=   160*m.b61 + m.x423 - m.x494 <= 160)

m.c358 = Constraint(expr=   160*m.b62 + m.x423 - m.x495 <= 160)

m.c359 = Constraint(expr=   160*m.b63 + m.x423 - m.x496 <= 160)

m.c360 = Constraint(expr=   160*m.b64 + m.x423 - m.x497 <= 160)

m.c361 = Constraint(expr=   160*m.b65 + m.x423 - m.x498 <= 160)

m.c362 = Constraint(expr=   160*m.b66 + m.x423 - m.x499 <= 160)

m.c363 = Constraint(expr=   160*m.b67 + m.x423 - m.x500 <= 160)

m.c364 = Constraint(expr=   160*m.b68 + m.x423 - m.x501 <= 160)

m.c365 = Constraint(expr=   160*m.b69 + m.x423 - m.x502 <= 160)

m.c366 = Constraint(expr=   160*m.b70 + m.x423 - m.x503 <= 160)

m.c367 = Constraint(expr=   160*m.b71 + m.x423 - m.x504 <= 160)

m.c368 = Constraint(expr=   160*m.b72 + m.x423 - m.x505 <= 160)

m.c369 = Constraint(expr=   160*m.b73 + m.x424 - m.x506 <= 160)

m.c370 = Constraint(expr=   160*m.b74 + m.x424 - m.x507 <= 160)

m.c371 = Constraint(expr=   160*m.b75 + m.x424 - m.x508 <= 160)

m.c372 = Constraint(expr=   160*m.b76 + m.x424 - m.x509 <= 160)

m.c373 = Constraint(expr=   160*m.b77 + m.x424 - m.x510 <= 160)

m.c374 = Constraint(expr=   160*m.b78 + m.x424 - m.x511 <= 160)

m.c375 = Constraint(expr=   160*m.b79 + m.x424 - m.x512 <= 160)

m.c376 = Constraint(expr=   160*m.b80 + m.x424 - m.x513 <= 160)

m.c377 = Constraint(expr=   160*m.b81 + m.x424 - m.x514 <= 160)

m.c378 = Constraint(expr=   160*m.b82 + m.x424 - m.x515 <= 160)

m.c379 = Constraint(expr=   160*m.b83 + m.x424 - m.x516 <= 160)

m.c380 = Constraint(expr=   160*m.b84 + m.x424 - m.x517 <= 160)

m.c381 = Constraint(expr=   160*m.b85 + m.x425 - m.x518 <= 160)

m.c382 = Constraint(expr=   160*m.b86 + m.x425 - m.x519 <= 160)

m.c383 = Constraint(expr=   160*m.b87 + m.x425 - m.x520 <= 160)

m.c384 = Constraint(expr=   160*m.b88 + m.x425 - m.x521 <= 160)

m.c385 = Constraint(expr=   160*m.b89 + m.x425 - m.x522 <= 160)

m.c386 = Constraint(expr=   160*m.b90 + m.x425 - m.x523 <= 160)

m.c387 = Constraint(expr=   160*m.b91 + m.x425 - m.x524 <= 160)

m.c388 = Constraint(expr=   160*m.b92 + m.x425 - m.x525 <= 160)

m.c389 = Constraint(expr=   160*m.b93 + m.x425 - m.x526 <= 160)

m.c390 = Constraint(expr=   160*m.b94 + m.x425 - m.x527 <= 160)

m.c391 = Constraint(expr=   160*m.b95 + m.x425 - m.x528 <= 160)

m.c392 = Constraint(expr=   160*m.b96 + m.x425 - m.x529 <= 160)

m.c393 = Constraint(expr= - 160*m.b1 + m.x426 - m.x530 >= -160)

m.c394 = Constraint(expr= - 160*m.b2 + m.x426 - m.x531 >= -160)

m.c395 = Constraint(expr= - 160*m.b3 + m.x426 - m.x532 >= -160)

m.c396 = Constraint(expr= - 160*m.b4 + m.x426 - m.x533 >= -160)

m.c397 = Constraint(expr= - 160*m.b5 + m.x426 - m.x534 >= -160)

m.c398 = Constraint(expr= - 160*m.b6 + m.x426 - m.x535 >= -160)

m.c399 = Constraint(expr= - 160*m.b7 + m.x426 - m.x536 >= -160)

m.c400 = Constraint(expr= - 160*m.b8 + m.x426 - m.x537 >= -160)

m.c401 = Constraint(expr= - 160*m.b9 + m.x426 - m.x538 >= -160)

m.c402 = Constraint(expr= - 160*m.b10 + m.x426 - m.x539 >= -160)

m.c403 = Constraint(expr= - 160*m.b11 + m.x426 - m.x540 >= -160)

m.c404 = Constraint(expr= - 160*m.b12 + m.x426 - m.x541 >= -160)

m.c405 = Constraint(expr= - 160*m.b13 + m.x427 - m.x542 >= -160)

m.c406 = Constraint(expr= - 160*m.b14 + m.x427 - m.x543 >= -160)

m.c407 = Constraint(expr= - 160*m.b15 + m.x427 - m.x544 >= -160)

m.c408 = Constraint(expr= - 160*m.b16 + m.x427 - m.x545 >= -160)

m.c409 = Constraint(expr= - 160*m.b17 + m.x427 - m.x546 >= -160)

m.c410 = Constraint(expr= - 160*m.b18 + m.x427 - m.x547 >= -160)

m.c411 = Constraint(expr= - 160*m.b19 + m.x427 - m.x548 >= -160)

m.c412 = Constraint(expr= - 160*m.b20 + m.x427 - m.x549 >= -160)

m.c413 = Constraint(expr= - 160*m.b21 + m.x427 - m.x550 >= -160)

m.c414 = Constraint(expr= - 160*m.b22 + m.x427 - m.x551 >= -160)

m.c415 = Constraint(expr= - 160*m.b23 + m.x427 - m.x552 >= -160)

m.c416 = Constraint(expr= - 160*m.b24 + m.x427 - m.x553 >= -160)

m.c417 = Constraint(expr= - 160*m.b25 + m.x428 - m.x554 >= -160)

m.c418 = Constraint(expr= - 160*m.b26 + m.x428 - m.x555 >= -160)

m.c419 = Constraint(expr= - 160*m.b27 + m.x428 - m.x556 >= -160)

m.c420 = Constraint(expr= - 160*m.b28 + m.x428 - m.x557 >= -160)

m.c421 = Constraint(expr= - 160*m.b29 + m.x428 - m.x558 >= -160)

m.c422 = Constraint(expr= - 160*m.b30 + m.x428 - m.x559 >= -160)

m.c423 = Constraint(expr= - 160*m.b31 + m.x428 - m.x560 >= -160)

m.c424 = Constraint(expr= - 160*m.b32 + m.x428 - m.x561 >= -160)

m.c425 = Constraint(expr= - 160*m.b33 + m.x428 - m.x562 >= -160)

m.c426 = Constraint(expr= - 160*m.b34 + m.x428 - m.x563 >= -160)

m.c427 = Constraint(expr= - 160*m.b35 + m.x428 - m.x564 >= -160)

m.c428 = Constraint(expr= - 160*m.b36 + m.x428 - m.x565 >= -160)

m.c429 = Constraint(expr= - 160*m.b37 + m.x429 - m.x566 >= -160)

m.c430 = Constraint(expr= - 160*m.b38 + m.x429 - m.x567 >= -160)

m.c431 = Constraint(expr= - 160*m.b39 + m.x429 - m.x568 >= -160)

m.c432 = Constraint(expr= - 160*m.b40 + m.x429 - m.x569 >= -160)

m.c433 = Constraint(expr= - 160*m.b41 + m.x429 - m.x570 >= -160)

m.c434 = Constraint(expr= - 160*m.b42 + m.x429 - m.x571 >= -160)

m.c435 = Constraint(expr= - 160*m.b43 + m.x429 - m.x572 >= -160)

m.c436 = Constraint(expr= - 160*m.b44 + m.x429 - m.x573 >= -160)

m.c437 = Constraint(expr= - 160*m.b45 + m.x429 - m.x574 >= -160)

m.c438 = Constraint(expr= - 160*m.b46 + m.x429 - m.x575 >= -160)

m.c439 = Constraint(expr= - 160*m.b47 + m.x429 - m.x576 >= -160)

m.c440 = Constraint(expr= - 160*m.b48 + m.x429 - m.x577 >= -160)

m.c441 = Constraint(expr= - 160*m.b49 + m.x430 - m.x578 >= -160)

m.c442 = Constraint(expr= - 160*m.b50 + m.x430 - m.x579 >= -160)

m.c443 = Constraint(expr= - 160*m.b51 + m.x430 - m.x580 >= -160)

m.c444 = Constraint(expr= - 160*m.b52 + m.x430 - m.x581 >= -160)

m.c445 = Constraint(expr= - 160*m.b53 + m.x430 - m.x582 >= -160)

m.c446 = Constraint(expr= - 160*m.b54 + m.x430 - m.x583 >= -160)

m.c447 = Constraint(expr= - 160*m.b55 + m.x430 - m.x584 >= -160)

m.c448 = Constraint(expr= - 160*m.b56 + m.x430 - m.x585 >= -160)

m.c449 = Constraint(expr= - 160*m.b57 + m.x430 - m.x586 >= -160)

m.c450 = Constraint(expr= - 160*m.b58 + m.x430 - m.x587 >= -160)

m.c451 = Constraint(expr= - 160*m.b59 + m.x430 - m.x588 >= -160)

m.c452 = Constraint(expr= - 160*m.b60 + m.x430 - m.x589 >= -160)

m.c453 = Constraint(expr= - 160*m.b61 + m.x431 - m.x590 >= -160)

m.c454 = Constraint(expr= - 160*m.b62 + m.x431 - m.x591 >= -160)

m.c455 = Constraint(expr= - 160*m.b63 + m.x431 - m.x592 >= -160)

m.c456 = Constraint(expr= - 160*m.b64 + m.x431 - m.x593 >= -160)

m.c457 = Constraint(expr= - 160*m.b65 + m.x431 - m.x594 >= -160)

m.c458 = Constraint(expr= - 160*m.b66 + m.x431 - m.x595 >= -160)

m.c459 = Constraint(expr= - 160*m.b67 + m.x431 - m.x596 >= -160)

m.c460 = Constraint(expr= - 160*m.b68 + m.x431 - m.x597 >= -160)

m.c461 = Constraint(expr= - 160*m.b69 + m.x431 - m.x598 >= -160)

m.c462 = Constraint(expr= - 160*m.b70 + m.x431 - m.x599 >= -160)

m.c463 = Constraint(expr= - 160*m.b71 + m.x431 - m.x600 >= -160)

m.c464 = Constraint(expr= - 160*m.b72 + m.x431 - m.x601 >= -160)

m.c465 = Constraint(expr= - 160*m.b73 + m.x432 - m.x602 >= -160)

m.c466 = Constraint(expr= - 160*m.b74 + m.x432 - m.x603 >= -160)

m.c467 = Constraint(expr= - 160*m.b75 + m.x432 - m.x604 >= -160)

m.c468 = Constraint(expr= - 160*m.b76 + m.x432 - m.x605 >= -160)

m.c469 = Constraint(expr= - 160*m.b77 + m.x432 - m.x606 >= -160)

m.c470 = Constraint(expr= - 160*m.b78 + m.x432 - m.x607 >= -160)

m.c471 = Constraint(expr= - 160*m.b79 + m.x432 - m.x608 >= -160)

m.c472 = Constraint(expr= - 160*m.b80 + m.x432 - m.x609 >= -160)

m.c473 = Constraint(expr= - 160*m.b81 + m.x432 - m.x610 >= -160)

m.c474 = Constraint(expr= - 160*m.b82 + m.x432 - m.x611 >= -160)

m.c475 = Constraint(expr= - 160*m.b83 + m.x432 - m.x612 >= -160)

m.c476 = Constraint(expr= - 160*m.b84 + m.x432 - m.x613 >= -160)

m.c477 = Constraint(expr= - 160*m.b85 + m.x433 - m.x614 >= -160)

m.c478 = Constraint(expr= - 160*m.b86 + m.x433 - m.x615 >= -160)

m.c479 = Constraint(expr= - 160*m.b87 + m.x433 - m.x616 >= -160)

m.c480 = Constraint(expr= - 160*m.b88 + m.x433 - m.x617 >= -160)

m.c481 = Constraint(expr= - 160*m.b89 + m.x433 - m.x618 >= -160)

m.c482 = Constraint(expr= - 160*m.b90 + m.x433 - m.x619 >= -160)

m.c483 = Constraint(expr= - 160*m.b91 + m.x433 - m.x620 >= -160)

m.c484 = Constraint(expr= - 160*m.b92 + m.x433 - m.x621 >= -160)

m.c485 = Constraint(expr= - 160*m.b93 + m.x433 - m.x622 >= -160)

m.c486 = Constraint(expr= - 160*m.b94 + m.x433 - m.x623 >= -160)

m.c487 = Constraint(expr= - 160*m.b95 + m.x433 - m.x624 >= -160)

m.c488 = Constraint(expr= - 160*m.b96 + m.x433 - m.x625 >= -160)

m.c489 = Constraint(expr=   m.x419 - m.x426 >= 0)

m.c490 = Constraint(expr=   m.x420 - m.x427 >= 0)

m.c491 = Constraint(expr=   m.x421 - m.x428 >= 0)

m.c492 = Constraint(expr=   m.x422 - m.x429 >= 0)

m.c493 = Constraint(expr=   m.x423 - m.x430 >= 0)

m.c494 = Constraint(expr=   m.x424 - m.x431 >= 0)

m.c495 = Constraint(expr=   m.x425 - m.x432 >= 0)

m.c496 = Constraint(expr= - m.x716 + m.x740 + m.x743 + m.x746 + m.x749 == 0)

m.c497 = Constraint(expr= - m.x717 + m.x741 + m.x744 + m.x747 + m.x750 == 0)

m.c498 = Constraint(expr= - m.x718 + m.x742 + m.x745 + m.x748 + m.x751 == 0)

m.c499 = Constraint(expr= - m.x719 + m.x752 + m.x755 + m.x758 + m.x761 == 0)

m.c500 = Constraint(expr= - m.x720 + m.x753 + m.x756 + m.x759 + m.x762 == 0)

m.c501 = Constraint(expr= - m.x721 + m.x754 + m.x757 + m.x760 + m.x763 == 0)

m.c502 = Constraint(expr= - m.x722 + m.x764 + m.x767 + m.x770 + m.x773 == 0)

m.c503 = Constraint(expr= - m.x723 + m.x765 + m.x768 + m.x771 + m.x774 == 0)

m.c504 = Constraint(expr= - m.x724 + m.x766 + m.x769 + m.x772 + m.x775 == 0)

m.c505 = Constraint(expr= - m.x725 + m.x776 + m.x779 + m.x782 + m.x785 == 0)

m.c506 = Constraint(expr= - m.x726 + m.x777 + m.x780 + m.x783 + m.x786 == 0)

m.c507 = Constraint(expr= - m.x727 + m.x778 + m.x781 + m.x784 + m.x787 == 0)

m.c508 = Constraint(expr= - m.x728 + m.x788 + m.x791 + m.x794 + m.x797 == 0)

m.c509 = Constraint(expr= - m.x729 + m.x789 + m.x792 + m.x795 + m.x798 == 0)

m.c510 = Constraint(expr= - m.x730 + m.x790 + m.x793 + m.x796 + m.x799 == 0)

m.c511 = Constraint(expr= - m.x731 + m.x800 + m.x803 + m.x806 + m.x809 == 0)

m.c512 = Constraint(expr= - m.x732 + m.x801 + m.x804 + m.x807 + m.x810 == 0)

m.c513 = Constraint(expr= - m.x733 + m.x802 + m.x805 + m.x808 + m.x811 == 0)

m.c514 = Constraint(expr= - m.x734 + m.x812 + m.x815 + m.x818 + m.x821 == 0)

m.c515 = Constraint(expr= - m.x735 + m.x813 + m.x816 + m.x819 + m.x822 == 0)

m.c516 = Constraint(expr= - m.x736 + m.x814 + m.x817 + m.x820 + m.x823 == 0)

m.c517 = Constraint(expr= - m.x737 + m.x824 + m.x827 + m.x830 + m.x833 == 0)

m.c518 = Constraint(expr= - m.x738 + m.x825 + m.x828 + m.x831 + m.x834 == 0)

m.c519 = Constraint(expr= - m.x739 + m.x826 + m.x829 + m.x832 + m.x835 == 0)

m.c520 = Constraint(expr= - 0.142857142857143*m.x133 + m.x169 == 0)

m.c521 = Constraint(expr= - 0.285714285714286*m.x133 + m.x172 == 0)

m.c522 = Constraint(expr= - 0.285714285714286*m.x133 + m.x175 == 0)

m.c523 = Constraint(expr= - 0.285714285714286*m.x133 + m.x178 == 0)

m.c524 = Constraint(expr= - 0.25*m.x136 + m.x181 == 0)

m.c525 = Constraint(expr= - 0.25*m.x136 + m.x184 == 0)

m.c526 = Constraint(expr= - 0.25*m.x136 + m.x187 == 0)

m.c527 = Constraint(expr= - 0.25*m.x136 + m.x190 == 0)

m.c528 = Constraint(expr= - 0.25*m.x139 + m.x193 == 0)

m.c529 = Constraint(expr= - 0.25*m.x139 + m.x196 == 0)

m.c530 = Constraint(expr= - 0.25*m.x139 + m.x199 == 0)

m.c531 = Constraint(expr= - 0.25*m.x139 + m.x202 == 0)

m.c532 = Constraint(expr= - 0.285714285714286*m.x142 + m.x205 == 0)

m.c533 = Constraint(expr= - 0.285714285714286*m.x142 + m.x208 == 0)

m.c534 = Constraint(expr= - 0.142857142857143*m.x142 + m.x211 == 0)

m.c535 = Constraint(expr= - 0.285714285714286*m.x142 + m.x214 == 0)

m.c536 = Constraint(expr= - 0.285714285714286*m.x145 + m.x217 == 0)

m.c537 = Constraint(expr= - 0.285714285714286*m.x145 + m.x220 == 0)

m.c538 = Constraint(expr= - 0.142857142857143*m.x145 + m.x223 == 0)

m.c539 = Constraint(expr= - 0.285714285714286*m.x145 + m.x226 == 0)

m.c540 = Constraint(expr= - 0.210526315789474*m.x148 + m.x229 == 0)

m.c541 = Constraint(expr= - 0.263157894736842*m.x148 + m.x232 == 0)

m.c542 = Constraint(expr= - 0.210526315789474*m.x148 + m.x235 == 0)

m.c543 = Constraint(expr= - 0.315789473684211*m.x148 + m.x238 == 0)

m.c544 = Constraint(expr= - 0.210526315789474*m.x151 + m.x241 == 0)

m.c545 = Constraint(expr= - 0.263157894736842*m.x151 + m.x244 == 0)

m.c546 = Constraint(expr= - 0.210526315789474*m.x151 + m.x247 == 0)

m.c547 = Constraint(expr= - 0.315789473684211*m.x151 + m.x250 == 0)

m.c548 = Constraint(expr= - 0.333333333333333*m.x154 + m.x253 == 0)

m.c549 = Constraint(expr= - 0.333333333333333*m.x154 + m.x256 == 0)

m.c550 = Constraint(expr= - 0.166666666666667*m.x154 + m.x259 == 0)

m.c551 = Constraint(expr= - 0.166666666666667*m.x154 + m.x262 == 0)

m.c552 = Constraint(expr= - 0.333333333333333*m.x157 + m.x265 == 0)

m.c553 = Constraint(expr= - 0.333333333333333*m.x157 + m.x268 == 0)

m.c554 = Constraint(expr= - 0.166666666666667*m.x157 + m.x271 == 0)

m.c555 = Constraint(expr= - 0.166666666666667*m.x157 + m.x274 == 0)

m.c556 = Constraint(expr= - 0.25*m.x160 + m.x277 == 0)

m.c557 = Constraint(expr= - 0.25*m.x160 + m.x280 == 0)

m.c558 = Constraint(expr= - 0.25*m.x160 + m.x283 == 0)

m.c559 = Constraint(expr= - 0.25*m.x160 + m.x286 == 0)

m.c560 = Constraint(expr= - 0.25*m.x163 + m.x289 == 0)

m.c561 = Constraint(expr= - 0.25*m.x163 + m.x292 == 0)

m.c562 = Constraint(expr= - 0.25*m.x163 + m.x295 == 0)

m.c563 = Constraint(expr= - 0.25*m.x163 + m.x298 == 0)

m.c564 = Constraint(expr= - 0.222222222222222*m.x166 + m.x301 == 0)

m.c565 = Constraint(expr= - 0.222222222222222*m.x166 + m.x304 == 0)

m.c566 = Constraint(expr= - 0.222222222222222*m.x166 + m.x307 == 0)

m.c567 = Constraint(expr= - 0.333333333333333*m.x166 + m.x310 == 0)

m.c568 = Constraint(expr=   m.b1 + m.b97 <= 1)

m.c569 = Constraint(expr=   m.b2 + m.b98 <= 1)

m.c570 = Constraint(expr=   m.b3 + m.b99 <= 1)

m.c571 = Constraint(expr=   m.b4 + m.b124 <= 1)

m.c572 = Constraint(expr=   m.b5 + m.b125 <= 1)

m.c573 = Constraint(expr=   m.b6 + m.b126 <= 1)

m.c574 = Constraint(expr=   m.b7 + m.b127 <= 1)

m.c575 = Constraint(expr=   m.b8 + m.b128 <= 1)

m.c576 = Constraint(expr=   m.b9 + m.b129 <= 1)

m.c577 = Constraint(expr=   m.b10 + m.b130 <= 1)

m.c578 = Constraint(expr=   m.b11 + m.b131 <= 1)

m.c579 = Constraint(expr=   m.b12 + m.b132 <= 1)

m.c580 = Constraint(expr=   m.b13 + m.b97 <= 1)

m.c581 = Constraint(expr=   m.b14 + m.b98 <= 1)

m.c582 = Constraint(expr=   m.b15 + m.b99 <= 1)

m.c583 = Constraint(expr=   m.b16 + m.b124 <= 1)

m.c584 = Constraint(expr=   m.b17 + m.b125 <= 1)

m.c585 = Constraint(expr=   m.b18 + m.b126 <= 1)

m.c586 = Constraint(expr=   m.b19 + m.b127 <= 1)

m.c587 = Constraint(expr=   m.b20 + m.b128 <= 1)

m.c588 = Constraint(expr=   m.b21 + m.b129 <= 1)

m.c589 = Constraint(expr=   m.b22 + m.b130 <= 1)

m.c590 = Constraint(expr=   m.b23 + m.b131 <= 1)

m.c591 = Constraint(expr=   m.b24 + m.b132 <= 1)

m.c592 = Constraint(expr=   m.b25 + m.b97 <= 1)

m.c593 = Constraint(expr=   m.b26 + m.b98 <= 1)

m.c594 = Constraint(expr=   m.b27 + m.b99 <= 1)

m.c595 = Constraint(expr=   m.b28 + m.b124 <= 1)

m.c596 = Constraint(expr=   m.b29 + m.b125 <= 1)

m.c597 = Constraint(expr=   m.b30 + m.b126 <= 1)

m.c598 = Constraint(expr=   m.b31 + m.b127 <= 1)

m.c599 = Constraint(expr=   m.b32 + m.b128 <= 1)

m.c600 = Constraint(expr=   m.b33 + m.b129 <= 1)

m.c601 = Constraint(expr=   m.b34 + m.b130 <= 1)

m.c602 = Constraint(expr=   m.b35 + m.b131 <= 1)

m.c603 = Constraint(expr=   m.b36 + m.b132 <= 1)

m.c604 = Constraint(expr=   m.b37 + m.b100 <= 1)

m.c605 = Constraint(expr=   m.b38 + m.b101 <= 1)

m.c606 = Constraint(expr=   m.b39 + m.b102 <= 1)

m.c607 = Constraint(expr=   m.b37 + m.b103 <= 1)

m.c608 = Constraint(expr=   m.b38 + m.b104 <= 1)

m.c609 = Constraint(expr=   m.b39 + m.b105 <= 1)

m.c610 = Constraint(expr=   m.b40 + m.b106 <= 1)

m.c611 = Constraint(expr=   m.b41 + m.b107 <= 1)

m.c612 = Constraint(expr=   m.b42 + m.b108 <= 1)

m.c613 = Constraint(expr=   m.b40 + m.b109 <= 1)

m.c614 = Constraint(expr=   m.b41 + m.b110 <= 1)

m.c615 = Constraint(expr=   m.b42 + m.b111 <= 1)

m.c616 = Constraint(expr=   m.b43 + m.b112 <= 1)

m.c617 = Constraint(expr=   m.b44 + m.b113 <= 1)

m.c618 = Constraint(expr=   m.b45 + m.b114 <= 1)

m.c619 = Constraint(expr=   m.b43 + m.b115 <= 1)

m.c620 = Constraint(expr=   m.b44 + m.b116 <= 1)

m.c621 = Constraint(expr=   m.b45 + m.b117 <= 1)

m.c622 = Constraint(expr=   m.b46 + m.b118 <= 1)

m.c623 = Constraint(expr=   m.b47 + m.b119 <= 1)

m.c624 = Constraint(expr=   m.b48 + m.b120 <= 1)

m.c625 = Constraint(expr=   m.b46 + m.b121 <= 1)

m.c626 = Constraint(expr=   m.b47 + m.b122 <= 1)

m.c627 = Constraint(expr=   m.b48 + m.b123 <= 1)

m.c628 = Constraint(expr=   m.b49 + m.b100 <= 1)

m.c629 = Constraint(expr=   m.b50 + m.b101 <= 1)

m.c630 = Constraint(expr=   m.b51 + m.b102 <= 1)

m.c631 = Constraint(expr=   m.b49 + m.b103 <= 1)

m.c632 = Constraint(expr=   m.b50 + m.b104 <= 1)

m.c633 = Constraint(expr=   m.b51 + m.b105 <= 1)

m.c634 = Constraint(expr=   m.b52 + m.b106 <= 1)

m.c635 = Constraint(expr=   m.b53 + m.b107 <= 1)

m.c636 = Constraint(expr=   m.b54 + m.b108 <= 1)

m.c637 = Constraint(expr=   m.b52 + m.b109 <= 1)

m.c638 = Constraint(expr=   m.b53 + m.b110 <= 1)

m.c639 = Constraint(expr=   m.b54 + m.b111 <= 1)

m.c640 = Constraint(expr=   m.b55 + m.b112 <= 1)

m.c641 = Constraint(expr=   m.b56 + m.b113 <= 1)

m.c642 = Constraint(expr=   m.b57 + m.b114 <= 1)

m.c643 = Constraint(expr=   m.b55 + m.b115 <= 1)

m.c644 = Constraint(expr=   m.b56 + m.b116 <= 1)

m.c645 = Constraint(expr=   m.b57 + m.b117 <= 1)

m.c646 = Constraint(expr=   m.b58 + m.b118 <= 1)

m.c647 = Constraint(expr=   m.b59 + m.b119 <= 1)

m.c648 = Constraint(expr=   m.b60 + m.b120 <= 1)

m.c649 = Constraint(expr=   m.b58 + m.b121 <= 1)

m.c650 = Constraint(expr=   m.b59 + m.b122 <= 1)

m.c651 = Constraint(expr=   m.b60 + m.b123 <= 1)

m.c652 = Constraint(expr=   m.b61 + m.b100 <= 1)

m.c653 = Constraint(expr=   m.b62 + m.b101 <= 1)

m.c654 = Constraint(expr=   m.b63 + m.b102 <= 1)

m.c655 = Constraint(expr=   m.b61 + m.b103 <= 1)

m.c656 = Constraint(expr=   m.b62 + m.b104 <= 1)

m.c657 = Constraint(expr=   m.b63 + m.b105 <= 1)

m.c658 = Constraint(expr=   m.b64 + m.b106 <= 1)

m.c659 = Constraint(expr=   m.b65 + m.b107 <= 1)

m.c660 = Constraint(expr=   m.b66 + m.b108 <= 1)

m.c661 = Constraint(expr=   m.b64 + m.b109 <= 1)

m.c662 = Constraint(expr=   m.b65 + m.b110 <= 1)

m.c663 = Constraint(expr=   m.b66 + m.b111 <= 1)

m.c664 = Constraint(expr=   m.b67 + m.b112 <= 1)

m.c665 = Constraint(expr=   m.b68 + m.b113 <= 1)

m.c666 = Constraint(expr=   m.b69 + m.b114 <= 1)

m.c667 = Constraint(expr=   m.b67 + m.b115 <= 1)

m.c668 = Constraint(expr=   m.b68 + m.b116 <= 1)

m.c669 = Constraint(expr=   m.b69 + m.b117 <= 1)

m.c670 = Constraint(expr=   m.b70 + m.b118 <= 1)

m.c671 = Constraint(expr=   m.b71 + m.b119 <= 1)

m.c672 = Constraint(expr=   m.b72 + m.b120 <= 1)

m.c673 = Constraint(expr=   m.b70 + m.b121 <= 1)

m.c674 = Constraint(expr=   m.b71 + m.b122 <= 1)

m.c675 = Constraint(expr=   m.b72 + m.b123 <= 1)

m.c676 = Constraint(expr=   m.b73 + m.b97 <= 1)

m.c677 = Constraint(expr=   m.b74 + m.b98 <= 1)

m.c678 = Constraint(expr=   m.b75 + m.b99 <= 1)

m.c679 = Constraint(expr=   m.b76 + m.b124 <= 1)

m.c680 = Constraint(expr=   m.b77 + m.b125 <= 1)

m.c681 = Constraint(expr=   m.b78 + m.b126 <= 1)

m.c682 = Constraint(expr=   m.b79 + m.b127 <= 1)

m.c683 = Constraint(expr=   m.b80 + m.b128 <= 1)

m.c684 = Constraint(expr=   m.b81 + m.b129 <= 1)

m.c685 = Constraint(expr=   m.b82 + m.b130 <= 1)

m.c686 = Constraint(expr=   m.b83 + m.b131 <= 1)

m.c687 = Constraint(expr=   m.b84 + m.b132 <= 1)

m.c688 = Constraint(expr=   m.b85 + m.b100 <= 1)

m.c689 = Constraint(expr=   m.b86 + m.b101 <= 1)

m.c690 = Constraint(expr=   m.b87 + m.b102 <= 1)

m.c691 = Constraint(expr=   m.b85 + m.b103 <= 1)

m.c692 = Constraint(expr=   m.b86 + m.b104 <= 1)

m.c693 = Constraint(expr=   m.b87 + m.b105 <= 1)

m.c694 = Constraint(expr=   m.b88 + m.b106 <= 1)

m.c695 = Constraint(expr=   m.b89 + m.b107 <= 1)

m.c696 = Constraint(expr=   m.b90 + m.b108 <= 1)

m.c697 = Constraint(expr=   m.b88 + m.b109 <= 1)

m.c698 = Constraint(expr=   m.b89 + m.b110 <= 1)

m.c699 = Constraint(expr=   m.b90 + m.b111 <= 1)

m.c700 = Constraint(expr=   m.b91 + m.b112 <= 1)

m.c701 = Constraint(expr=   m.b92 + m.b113 <= 1)

m.c702 = Constraint(expr=   m.b93 + m.b114 <= 1)

m.c703 = Constraint(expr=   m.b91 + m.b115 <= 1)

m.c704 = Constraint(expr=   m.b92 + m.b116 <= 1)

m.c705 = Constraint(expr=   m.b93 + m.b117 <= 1)

m.c706 = Constraint(expr=   m.b94 + m.b118 <= 1)

m.c707 = Constraint(expr=   m.b95 + m.b119 <= 1)

m.c708 = Constraint(expr=   m.b96 + m.b120 <= 1)

m.c709 = Constraint(expr=   m.b94 + m.b121 <= 1)

m.c710 = Constraint(expr=   m.b95 + m.b122 <= 1)

m.c711 = Constraint(expr=   m.b96 + m.b123 <= 1)

m.c712 = Constraint(expr=   m.b97 <= 2)

m.c713 = Constraint(expr=   m.b98 <= 2)

m.c714 = Constraint(expr=   m.b99 <= 2)

m.c715 = Constraint(expr=   m.b100 + m.b103 <= 2)

m.c716 = Constraint(expr=   m.b101 + m.b104 <= 2)

m.c717 = Constraint(expr=   m.b102 + m.b105 <= 2)

m.c718 = Constraint(expr=   m.b106 + m.b109 <= 2)

m.c719 = Constraint(expr=   m.b107 + m.b110 <= 2)

m.c720 = Constraint(expr=   m.b108 + m.b111 <= 2)

m.c721 = Constraint(expr=   m.b112 + m.b115 <= 2)

m.c722 = Constraint(expr=   m.b113 + m.b116 <= 2)

m.c723 = Constraint(expr=   m.b114 + m.b117 <= 2)

m.c724 = Constraint(expr=   m.b118 + m.b121 <= 2)

m.c725 = Constraint(expr=   m.b119 + m.b122 <= 2)

m.c726 = Constraint(expr=   m.b120 + m.b123 <= 2)

m.c727 = Constraint(expr=   m.b124 <= 2)

m.c728 = Constraint(expr=   m.b125 <= 2)

m.c729 = Constraint(expr=   m.b126 <= 2)

m.c730 = Constraint(expr=   m.b127 <= 2)

m.c731 = Constraint(expr=   m.b128 <= 2)

m.c732 = Constraint(expr=   m.b129 <= 2)

m.c733 = Constraint(expr=   m.b130 <= 2)

m.c734 = Constraint(expr=   m.b131 <= 2)

m.c735 = Constraint(expr=   m.b132 <= 2)

m.c736 = Constraint(expr=   m.b100 + m.b106 + m.b112 + m.b118 <= 2)

m.c737 = Constraint(expr=   m.b101 + m.b107 + m.b113 + m.b119 <= 2)

m.c738 = Constraint(expr=   m.b102 + m.b108 + m.b114 + m.b120 <= 2)

m.c739 = Constraint(expr=   m.b103 + m.b109 + m.b115 + m.b121 <= 2)

m.c740 = Constraint(expr=   m.b104 + m.b110 + m.b116 + m.b122 <= 2)

m.c741 = Constraint(expr=   m.b105 + m.b111 + m.b117 + m.b123 <= 2)

m.c742 = Constraint(expr=   m.b97 + m.b124 + m.b127 + m.b130 <= 2)

m.c743 = Constraint(expr=   m.b98 + m.b125 + m.b128 + m.b131 <= 2)

m.c744 = Constraint(expr=   m.b99 + m.b126 + m.b129 + m.b132 <= 2)

m.c745 = Constraint(expr= - m.x133 - 2.5*m.x626 + 2.5*m.x662 <= 0)

m.c746 = Constraint(expr= - m.x134 - 2.5*m.x627 + 2.5*m.x663 <= 0)

m.c747 = Constraint(expr= - m.x135 - 2.5*m.x628 + 2.5*m.x664 <= 0)

m.c748 = Constraint(expr= - m.x136 - 2.5*m.x629 + 2.5*m.x665 <= 0)

m.c749 = Constraint(expr= - m.x137 - 2.5*m.x630 + 2.5*m.x666 <= 0)

m.c750 = Constraint(expr= - m.x138 - 2.5*m.x631 + 2.5*m.x667 <= 0)

m.c751 = Constraint(expr= - m.x139 - 2.5*m.x632 + 2.5*m.x668 <= 0)

m.c752 = Constraint(expr= - m.x140 - 2.5*m.x633 + 2.5*m.x669 <= 0)

m.c753 = Constraint(expr= - m.x141 - 2.5*m.x634 + 2.5*m.x670 <= 0)

m.c754 = Constraint(expr= - m.x142 - 2.5*m.x635 + 2.5*m.x671 <= 0)

m.c755 = Constraint(expr= - m.x143 - 2.5*m.x636 + 2.5*m.x672 <= 0)

m.c756 = Constraint(expr= - m.x144 - 2.5*m.x637 + 2.5*m.x673 <= 0)

m.c757 = Constraint(expr= - m.x145 - 2.5*m.x638 + 2.5*m.x674 <= 0)

m.c758 = Constraint(expr= - m.x146 - 2.5*m.x639 + 2.5*m.x675 <= 0)

m.c759 = Constraint(expr= - m.x147 - 2.5*m.x640 + 2.5*m.x676 <= 0)

m.c760 = Constraint(expr= - m.x148 - 2.5*m.x641 + 2.5*m.x677 <= 0)

m.c761 = Constraint(expr= - m.x149 - 2.5*m.x642 + 2.5*m.x678 <= 0)

m.c762 = Constraint(expr= - m.x150 - 2.5*m.x643 + 2.5*m.x679 <= 0)

m.c763 = Constraint(expr= - m.x151 - 2.5*m.x644 + 2.5*m.x680 <= 0)

m.c764 = Constraint(expr= - m.x152 - 2.5*m.x645 + 2.5*m.x681 <= 0)

m.c765 = Constraint(expr= - m.x153 - 2.5*m.x646 + 2.5*m.x682 <= 0)

m.c766 = Constraint(expr= - m.x154 - 2.5*m.x647 + 2.5*m.x683 <= 0)

m.c767 = Constraint(expr= - m.x155 - 2.5*m.x648 + 2.5*m.x684 <= 0)

m.c768 = Constraint(expr= - m.x156 - 2.5*m.x649 + 2.5*m.x685 <= 0)

m.c769 = Constraint(expr= - m.x157 - 2.5*m.x650 + 2.5*m.x686 <= 0)

m.c770 = Constraint(expr= - m.x158 - 2.5*m.x651 + 2.5*m.x687 <= 0)

m.c771 = Constraint(expr= - m.x159 - 2.5*m.x652 + 2.5*m.x688 <= 0)

m.c772 = Constraint(expr= - m.x160 - 2.5*m.x653 + 2.5*m.x689 <= 0)

m.c773 = Constraint(expr= - m.x161 - 2.5*m.x654 + 2.5*m.x690 <= 0)

m.c774 = Constraint(expr= - m.x162 - 2.5*m.x655 + 2.5*m.x691 <= 0)

m.c775 = Constraint(expr= - m.x163 - 2.5*m.x656 + 2.5*m.x692 <= 0)

m.c776 = Constraint(expr= - m.x164 - 2.5*m.x657 + 2.5*m.x693 <= 0)

m.c777 = Constraint(expr= - m.x165 - 2.5*m.x658 + 2.5*m.x694 <= 0)

m.c778 = Constraint(expr= - m.x166 - 2.5*m.x659 + 2.5*m.x695 <= 0)

m.c779 = Constraint(expr= - m.x167 - 2.5*m.x660 + 2.5*m.x696 <= 0)

m.c780 = Constraint(expr= - m.x168 - 2.5*m.x661 + 2.5*m.x697 <= 0)

m.c781 = Constraint(expr=   m.x133 + 5.625*m.x626 - 5.625*m.x662 <= 0)

m.c782 = Constraint(expr=   m.x134 + 5.625*m.x627 - 5.625*m.x663 <= 0)

m.c783 = Constraint(expr=   m.x135 + 5.625*m.x628 - 5.625*m.x664 <= 0)

m.c784 = Constraint(expr=   m.x136 + 5.625*m.x629 - 5.625*m.x665 <= 0)

m.c785 = Constraint(expr=   m.x137 + 5.625*m.x630 - 5.625*m.x666 <= 0)

m.c786 = Constraint(expr=   m.x138 + 5.625*m.x631 - 5.625*m.x667 <= 0)

m.c787 = Constraint(expr=   m.x139 + 5.625*m.x632 - 5.625*m.x668 <= 0)

m.c788 = Constraint(expr=   m.x140 + 5.625*m.x633 - 5.625*m.x669 <= 0)

m.c789 = Constraint(expr=   m.x141 + 5.625*m.x634 - 5.625*m.x670 <= 0)

m.c790 = Constraint(expr=   m.x142 + 5.625*m.x635 - 5.625*m.x671 <= 0)

m.c791 = Constraint(expr=   m.x143 + 5.625*m.x636 - 5.625*m.x672 <= 0)

m.c792 = Constraint(expr=   m.x144 + 5.625*m.x637 - 5.625*m.x673 <= 0)

m.c793 = Constraint(expr=   m.x145 + 5.625*m.x638 - 5.625*m.x674 <= 0)

m.c794 = Constraint(expr=   m.x146 + 5.625*m.x639 - 5.625*m.x675 <= 0)

m.c795 = Constraint(expr=   m.x147 + 5.625*m.x640 - 5.625*m.x676 <= 0)

m.c796 = Constraint(expr=   m.x148 + 5.625*m.x641 - 5.625*m.x677 <= 0)

m.c797 = Constraint(expr=   m.x149 + 5.625*m.x642 - 5.625*m.x678 <= 0)

m.c798 = Constraint(expr=   m.x150 + 5.625*m.x643 - 5.625*m.x679 <= 0)

m.c799 = Constraint(expr=   m.x151 + 5.625*m.x644 - 5.625*m.x680 <= 0)

m.c800 = Constraint(expr=   m.x152 + 5.625*m.x645 - 5.625*m.x681 <= 0)

m.c801 = Constraint(expr=   m.x153 + 5.625*m.x646 - 5.625*m.x682 <= 0)

m.c802 = Constraint(expr=   m.x154 + 5.625*m.x647 - 5.625*m.x683 <= 0)

m.c803 = Constraint(expr=   m.x155 + 5.625*m.x648 - 5.625*m.x684 <= 0)

m.c804 = Constraint(expr=   m.x156 + 5.625*m.x649 - 5.625*m.x685 <= 0)

m.c805 = Constraint(expr=   m.x157 + 5.625*m.x650 - 5.625*m.x686 <= 0)

m.c806 = Constraint(expr=   m.x158 + 5.625*m.x651 - 5.625*m.x687 <= 0)

m.c807 = Constraint(expr=   m.x159 + 5.625*m.x652 - 5.625*m.x688 <= 0)

m.c808 = Constraint(expr=   m.x160 + 5.625*m.x653 - 5.625*m.x689 <= 0)

m.c809 = Constraint(expr=   m.x161 + 5.625*m.x654 - 5.625*m.x690 <= 0)

m.c810 = Constraint(expr=   m.x162 + 5.625*m.x655 - 5.625*m.x691 <= 0)

m.c811 = Constraint(expr=   m.x163 + 5.625*m.x656 - 5.625*m.x692 <= 0)

m.c812 = Constraint(expr=   m.x164 + 5.625*m.x657 - 5.625*m.x693 <= 0)

m.c813 = Constraint(expr=   m.x165 + 5.625*m.x658 - 5.625*m.x694 <= 0)

m.c814 = Constraint(expr=   m.x166 + 5.625*m.x659 - 5.625*m.x695 <= 0)

m.c815 = Constraint(expr=   m.x167 + 5.625*m.x660 - 5.625*m.x696 <= 0)

m.c816 = Constraint(expr=   m.x168 + 5.625*m.x661 - 5.625*m.x697 <= 0)

m.c817 = Constraint(expr= - 290*m.b97 + m.x133 <= 0)

m.c818 = Constraint(expr= - 300*m.b98 + m.x134 <= 0)

m.c819 = Constraint(expr= - 510*m.b99 + m.x135 <= 0)

m.c820 = Constraint(expr= - 340*m.b100 + m.x136 <= 0)

m.c821 = Constraint(expr= - 350*m.b101 + m.x137 <= 0)

m.c822 = Constraint(expr= - 510*m.b102 + m.x138 <= 0)

m.c823 = Constraint(expr= - 340*m.b103 + m.x139 <= 0)

m.c824 = Constraint(expr= - 350*m.b104 + m.x140 <= 0)

m.c825 = Constraint(expr= - 510*m.b105 + m.x141 <= 0)

m.c826 = Constraint(expr= - 290*m.b106 + m.x142 <= 0)

m.c827 = Constraint(expr= - 490*m.b107 + m.x143 <= 0)

m.c828 = Constraint(expr= - 510*m.b108 + m.x144 <= 0)

m.c829 = Constraint(expr= - 290*m.b109 + m.x145 <= 0)

m.c830 = Constraint(expr= - 490*m.b110 + m.x146 <= 0)

m.c831 = Constraint(expr= - 510*m.b111 + m.x147 <= 0)

m.c832 = Constraint(expr= - 840*m.b112 + m.x148 <= 0)

m.c833 = Constraint(expr= - 850*m.b113 + m.x149 <= 0)

m.c834 = Constraint(expr= - 870*m.b114 + m.x150 <= 0)

m.c835 = Constraint(expr= - 840*m.b115 + m.x151 <= 0)

m.c836 = Constraint(expr= - 850*m.b116 + m.x152 <= 0)

m.c837 = Constraint(expr= - 870*m.b117 + m.x153 <= 0)

m.c838 = Constraint(expr= - 190*m.b118 + m.x154 <= 0)

m.c839 = Constraint(expr= - 870*m.b119 + m.x155 <= 0)

m.c840 = Constraint(expr= - 870*m.b120 + m.x156 <= 0)

m.c841 = Constraint(expr= - 190*m.b121 + m.x157 <= 0)

m.c842 = Constraint(expr= - 870*m.b122 + m.x158 <= 0)

m.c843 = Constraint(expr= - 870*m.b123 + m.x159 <= 0)

m.c844 = Constraint(expr= - 20*m.b124 + m.x160 <= 0)

m.c845 = Constraint(expr= - 510*m.b125 + m.x161 <= 0)

m.c846 = Constraint(expr= - 510*m.b126 + m.x162 <= 0)

m.c847 = Constraint(expr= - 20*m.b127 + m.x163 <= 0)

m.c848 = Constraint(expr= - 510*m.b128 + m.x164 <= 0)

m.c849 = Constraint(expr= - 510*m.b129 + m.x165 <= 0)

m.c850 = Constraint(expr= - 390*m.b130 + m.x166 <= 0)

m.c851 = Constraint(expr= - 400*m.b131 + m.x167 <= 0)

m.c852 = Constraint(expr= - 510*m.b132 + m.x168 <= 0)

m.c853 = Constraint(expr=   m.x133 - m.x169 - m.x172 - m.x175 - m.x178 == 0)

m.c854 = Constraint(expr=   m.x134 - m.x170 - m.x173 - m.x176 - m.x179 == 0)

m.c855 = Constraint(expr=   m.x135 - m.x171 - m.x174 - m.x177 - m.x180 == 0)

m.c856 = Constraint(expr=   m.x136 - m.x181 - m.x184 - m.x187 - m.x190 == 0)

m.c857 = Constraint(expr=   m.x137 - m.x182 - m.x185 - m.x188 - m.x191 == 0)

m.c858 = Constraint(expr=   m.x138 - m.x183 - m.x186 - m.x189 - m.x192 == 0)

m.c859 = Constraint(expr=   m.x139 - m.x193 - m.x196 - m.x199 - m.x202 == 0)

m.c860 = Constraint(expr=   m.x140 - m.x194 - m.x197 - m.x200 - m.x203 == 0)

m.c861 = Constraint(expr=   m.x141 - m.x195 - m.x198 - m.x201 - m.x204 == 0)

m.c862 = Constraint(expr=   m.x142 - m.x205 - m.x208 - m.x211 - m.x214 == 0)

m.c863 = Constraint(expr=   m.x143 - m.x206 - m.x209 - m.x212 - m.x215 == 0)

m.c864 = Constraint(expr=   m.x144 - m.x207 - m.x210 - m.x213 - m.x216 == 0)

m.c865 = Constraint(expr=   m.x145 - m.x217 - m.x220 - m.x223 - m.x226 == 0)

m.c866 = Constraint(expr=   m.x146 - m.x218 - m.x221 - m.x224 - m.x227 == 0)

m.c867 = Constraint(expr=   m.x147 - m.x219 - m.x222 - m.x225 - m.x228 == 0)

m.c868 = Constraint(expr=   m.x148 - m.x229 - m.x232 - m.x235 - m.x238 == 0)

m.c869 = Constraint(expr=   m.x149 - m.x230 - m.x233 - m.x236 - m.x239 == 0)

m.c870 = Constraint(expr=   m.x150 - m.x231 - m.x234 - m.x237 - m.x240 == 0)

m.c871 = Constraint(expr=   m.x151 - m.x241 - m.x244 - m.x247 - m.x250 == 0)

m.c872 = Constraint(expr=   m.x152 - m.x242 - m.x245 - m.x248 - m.x251 == 0)

m.c873 = Constraint(expr=   m.x153 - m.x243 - m.x246 - m.x249 - m.x252 == 0)

m.c874 = Constraint(expr=   m.x154 - m.x253 - m.x256 - m.x259 - m.x262 == 0)

m.c875 = Constraint(expr=   m.x155 - m.x254 - m.x257 - m.x260 - m.x263 == 0)

m.c876 = Constraint(expr=   m.x156 - m.x255 - m.x258 - m.x261 - m.x264 == 0)

m.c877 = Constraint(expr=   m.x157 - m.x265 - m.x268 - m.x271 - m.x274 == 0)

m.c878 = Constraint(expr=   m.x158 - m.x266 - m.x269 - m.x272 - m.x275 == 0)

m.c879 = Constraint(expr=   m.x159 - m.x267 - m.x270 - m.x273 - m.x276 == 0)

m.c880 = Constraint(expr=   m.x160 - m.x277 - m.x280 - m.x283 - m.x286 == 0)

m.c881 = Constraint(expr=   m.x161 - m.x278 - m.x281 - m.x284 - m.x287 == 0)

m.c882 = Constraint(expr=   m.x162 - m.x279 - m.x282 - m.x285 - m.x288 == 0)

m.c883 = Constraint(expr=   m.x163 - m.x289 - m.x292 - m.x295 - m.x298 == 0)

m.c884 = Constraint(expr=   m.x164 - m.x290 - m.x293 - m.x296 - m.x299 == 0)

m.c885 = Constraint(expr=   m.x165 - m.x291 - m.x294 - m.x297 - m.x300 == 0)

m.c886 = Constraint(expr=   m.x166 - m.x301 - m.x304 - m.x307 - m.x310 == 0)

m.c887 = Constraint(expr=   m.x167 - m.x302 - m.x305 - m.x308 - m.x311 == 0)

m.c888 = Constraint(expr=   m.x168 - m.x303 - m.x306 - m.x309 - m.x312 == 0)

m.c889 = Constraint(expr= - m.x136 - m.x142 - m.x148 - m.x154 + m.x313 == 0)

m.c890 = Constraint(expr= - m.x137 - m.x143 - m.x149 - m.x155 + m.x314 == 0)

m.c891 = Constraint(expr= - m.x138 - m.x144 - m.x150 - m.x156 + m.x315 == 0)

m.c892 = Constraint(expr= - m.x139 - m.x145 - m.x151 - m.x157 + m.x316 == 0)

m.c893 = Constraint(expr= - m.x140 - m.x146 - m.x152 - m.x158 + m.x317 == 0)

m.c894 = Constraint(expr= - m.x141 - m.x147 - m.x153 - m.x159 + m.x318 == 0)

m.c895 = Constraint(expr= - m.x133 - m.x160 - m.x163 - m.x166 + m.x319 == 0)

m.c896 = Constraint(expr= - m.x134 - m.x161 - m.x164 - m.x167 + m.x320 == 0)

m.c897 = Constraint(expr= - m.x135 - m.x162 - m.x165 - m.x168 + m.x321 == 0)

m.c898 = Constraint(expr= - m.x313 - 2.5*m.x698 + 2.5*m.x707 <= 0)

m.c899 = Constraint(expr= - m.x314 - 2.5*m.x699 + 2.5*m.x708 <= 0)

m.c900 = Constraint(expr= - m.x315 - 2.5*m.x700 + 2.5*m.x709 <= 0)

m.c901 = Constraint(expr= - m.x316 - 2.5*m.x701 + 2.5*m.x710 <= 0)

m.c902 = Constraint(expr= - m.x317 - 2.5*m.x702 + 2.5*m.x711 <= 0)

m.c903 = Constraint(expr= - m.x318 - 2.5*m.x703 + 2.5*m.x712 <= 0)

m.c904 = Constraint(expr= - m.x319 - 2.5*m.x704 + 2.5*m.x713 <= 0)

m.c905 = Constraint(expr= - m.x320 - 2.5*m.x705 + 2.5*m.x714 <= 0)

m.c906 = Constraint(expr= - m.x321 - 2.5*m.x706 + 2.5*m.x715 <= 0)

m.c907 = Constraint(expr=   m.x313 + 5.625*m.x698 - 5.625*m.x707 <= 0)

m.c908 = Constraint(expr=   m.x314 + 5.625*m.x699 - 5.625*m.x708 <= 0)

m.c909 = Constraint(expr=   m.x315 + 5.625*m.x700 - 5.625*m.x709 <= 0)

m.c910 = Constraint(expr=   m.x316 + 5.625*m.x701 - 5.625*m.x710 <= 0)

m.c911 = Constraint(expr=   m.x317 + 5.625*m.x702 - 5.625*m.x711 <= 0)

m.c912 = Constraint(expr=   m.x318 + 5.625*m.x703 - 5.625*m.x712 <= 0)

m.c913 = Constraint(expr=   m.x319 + 5.625*m.x704 - 5.625*m.x713 <= 0)

m.c914 = Constraint(expr=   m.x320 + 5.625*m.x705 - 5.625*m.x714 <= 0)

m.c915 = Constraint(expr=   m.x321 + 5.625*m.x706 - 5.625*m.x715 <= 0)

m.c916 = Constraint(expr=   0.001*m.x136 + 0.001*m.x142 + 0.001*m.x148 + 0.001*m.x154 - 0.012*m.x181 - 0.013*m.x184
                          - 0.009*m.x187 - 0.015*m.x190 - 0.012*m.x205 - 0.013*m.x208 - 0.009*m.x211 - 0.015*m.x214
                          - 0.012*m.x229 - 0.013*m.x232 - 0.009*m.x235 - 0.015*m.x238 - 0.012*m.x253 - 0.013*m.x256
                          - 0.009*m.x259 - 0.015*m.x262 <= 0)

m.c917 = Constraint(expr=   0.001*m.x137 + 0.001*m.x143 + 0.001*m.x149 + 0.001*m.x155 - 0.012*m.x182 - 0.013*m.x185
                          - 0.009*m.x188 - 0.015*m.x191 - 0.012*m.x206 - 0.013*m.x209 - 0.009*m.x212 - 0.015*m.x215
                          - 0.012*m.x230 - 0.013*m.x233 - 0.009*m.x236 - 0.015*m.x239 - 0.012*m.x254 - 0.013*m.x257
                          - 0.009*m.x260 - 0.015*m.x263 <= 0)

m.c918 = Constraint(expr=   0.001*m.x138 + 0.001*m.x144 + 0.001*m.x150 + 0.001*m.x156 - 0.012*m.x183 - 0.013*m.x186
                          - 0.009*m.x189 - 0.015*m.x192 - 0.012*m.x207 - 0.013*m.x210 - 0.009*m.x213 - 0.015*m.x216
                          - 0.012*m.x231 - 0.013*m.x234 - 0.009*m.x237 - 0.015*m.x240 - 0.012*m.x255 - 0.013*m.x258
                          - 0.009*m.x261 - 0.015*m.x264 <= 0)

m.c919 = Constraint(expr=   0.001*m.x139 + 0.001*m.x145 + 0.001*m.x151 + 0.001*m.x157 - 0.012*m.x193 - 0.013*m.x196
                          - 0.009*m.x199 - 0.015*m.x202 - 0.012*m.x217 - 0.013*m.x220 - 0.009*m.x223 - 0.015*m.x226
                          - 0.012*m.x241 - 0.013*m.x244 - 0.009*m.x247 - 0.015*m.x250 - 0.012*m.x265 - 0.013*m.x268
                          - 0.009*m.x271 - 0.015*m.x274 <= 0)

m.c920 = Constraint(expr=   0.001*m.x140 + 0.001*m.x146 + 0.001*m.x152 + 0.001*m.x158 - 0.012*m.x194 - 0.013*m.x197
                          - 0.009*m.x200 - 0.015*m.x203 - 0.012*m.x218 - 0.013*m.x221 - 0.009*m.x224 - 0.015*m.x227
                          - 0.012*m.x242 - 0.013*m.x245 - 0.009*m.x248 - 0.015*m.x251 - 0.012*m.x266 - 0.013*m.x269
                          - 0.009*m.x272 - 0.015*m.x275 <= 0)

m.c921 = Constraint(expr=   0.001*m.x141 + 0.001*m.x147 + 0.001*m.x153 + 0.001*m.x159 - 0.012*m.x195 - 0.013*m.x198
                          - 0.009*m.x201 - 0.015*m.x204 - 0.012*m.x219 - 0.013*m.x222 - 0.009*m.x225 - 0.015*m.x228
                          - 0.012*m.x243 - 0.013*m.x246 - 0.009*m.x249 - 0.015*m.x252 - 0.012*m.x267 - 0.013*m.x270
                          - 0.009*m.x273 - 0.015*m.x276 <= 0)

m.c922 = Constraint(expr=   0.001*m.x133 + 0.001*m.x160 + 0.001*m.x163 + 0.001*m.x166 - 0.002*m.x169 - 0.0025*m.x172
                          - 0.0015*m.x175 - 0.006*m.x178 - 0.002*m.x277 - 0.0025*m.x280 - 0.0015*m.x283 - 0.006*m.x286
                          - 0.002*m.x289 - 0.0025*m.x292 - 0.0015*m.x295 - 0.006*m.x298 - 0.002*m.x301 - 0.0025*m.x304
                          - 0.0015*m.x307 - 0.006*m.x310 <= 0)

m.c923 = Constraint(expr=   0.001*m.x134 + 0.001*m.x161 + 0.001*m.x164 + 0.001*m.x167 - 0.002*m.x170 - 0.0025*m.x173
                          - 0.0015*m.x176 - 0.006*m.x179 - 0.002*m.x278 - 0.0025*m.x281 - 0.0015*m.x284 - 0.006*m.x287
                          - 0.002*m.x290 - 0.0025*m.x293 - 0.0015*m.x296 - 0.006*m.x299 - 0.002*m.x302 - 0.0025*m.x305
                          - 0.0015*m.x308 - 0.006*m.x311 <= 0)

m.c924 = Constraint(expr=   0.001*m.x135 + 0.001*m.x162 + 0.001*m.x165 + 0.001*m.x168 - 0.002*m.x171 - 0.0025*m.x174
                          - 0.0015*m.x177 - 0.006*m.x180 - 0.002*m.x279 - 0.0025*m.x282 - 0.0015*m.x285 - 0.006*m.x288
                          - 0.002*m.x291 - 0.0025*m.x294 - 0.0015*m.x297 - 0.006*m.x300 - 0.002*m.x303 - 0.0025*m.x306
                          - 0.0015*m.x309 - 0.006*m.x312 <= 0)

m.c925 = Constraint(expr= - 0.013*m.x136 - 0.013*m.x142 - 0.013*m.x148 - 0.013*m.x154 + 0.012*m.x181 + 0.013*m.x184
                          + 0.009*m.x187 + 0.015*m.x190 + 0.012*m.x205 + 0.013*m.x208 + 0.009*m.x211 + 0.015*m.x214
                          + 0.012*m.x229 + 0.013*m.x232 + 0.009*m.x235 + 0.015*m.x238 + 0.012*m.x253 + 0.013*m.x256
                          + 0.009*m.x259 + 0.015*m.x262 <= 0)

m.c926 = Constraint(expr= - 0.013*m.x137 - 0.013*m.x143 - 0.013*m.x149 - 0.013*m.x155 + 0.012*m.x182 + 0.013*m.x185
                          + 0.009*m.x188 + 0.015*m.x191 + 0.012*m.x206 + 0.013*m.x209 + 0.009*m.x212 + 0.015*m.x215
                          + 0.012*m.x230 + 0.013*m.x233 + 0.009*m.x236 + 0.015*m.x239 + 0.012*m.x254 + 0.013*m.x257
                          + 0.009*m.x260 + 0.015*m.x263 <= 0)

m.c927 = Constraint(expr= - 0.013*m.x138 - 0.013*m.x144 - 0.013*m.x150 - 0.013*m.x156 + 0.012*m.x183 + 0.013*m.x186
                          + 0.009*m.x189 + 0.015*m.x192 + 0.012*m.x207 + 0.013*m.x210 + 0.009*m.x213 + 0.015*m.x216
                          + 0.012*m.x231 + 0.013*m.x234 + 0.009*m.x237 + 0.015*m.x240 + 0.012*m.x255 + 0.013*m.x258
                          + 0.009*m.x261 + 0.015*m.x264 <= 0)

m.c928 = Constraint(expr= - 0.0125*m.x139 - 0.0125*m.x145 - 0.0125*m.x151 - 0.0125*m.x157 + 0.012*m.x193 + 0.013*m.x196
                          + 0.009*m.x199 + 0.015*m.x202 + 0.012*m.x217 + 0.013*m.x220 + 0.009*m.x223 + 0.015*m.x226
                          + 0.012*m.x241 + 0.013*m.x244 + 0.009*m.x247 + 0.015*m.x250 + 0.012*m.x265 + 0.013*m.x268
                          + 0.009*m.x271 + 0.015*m.x274 <= 0)

m.c929 = Constraint(expr= - 0.0125*m.x140 - 0.0125*m.x146 - 0.0125*m.x152 - 0.0125*m.x158 + 0.012*m.x194 + 0.013*m.x197
                          + 0.009*m.x200 + 0.015*m.x203 + 0.012*m.x218 + 0.013*m.x221 + 0.009*m.x224 + 0.015*m.x227
                          + 0.012*m.x242 + 0.013*m.x245 + 0.009*m.x248 + 0.015*m.x251 + 0.012*m.x266 + 0.013*m.x269
                          + 0.009*m.x272 + 0.015*m.x275 <= 0)

m.c930 = Constraint(expr= - 0.0125*m.x141 - 0.0125*m.x147 - 0.0125*m.x153 - 0.0125*m.x159 + 0.012*m.x195 + 0.013*m.x198
                          + 0.009*m.x201 + 0.015*m.x204 + 0.012*m.x219 + 0.013*m.x222 + 0.009*m.x225 + 0.015*m.x228
                          + 0.012*m.x243 + 0.013*m.x246 + 0.009*m.x249 + 0.015*m.x252 + 0.012*m.x267 + 0.013*m.x270
                          + 0.009*m.x273 + 0.015*m.x276 <= 0)

m.c931 = Constraint(expr= - 0.0035*m.x133 - 0.0035*m.x160 - 0.0035*m.x163 - 0.0035*m.x166 + 0.002*m.x169 + 0.0025*m.x172
                          + 0.0015*m.x175 + 0.006*m.x178 + 0.002*m.x277 + 0.0025*m.x280 + 0.0015*m.x283 + 0.006*m.x286
                          + 0.002*m.x289 + 0.0025*m.x292 + 0.0015*m.x295 + 0.006*m.x298 + 0.002*m.x301 + 0.0025*m.x304
                          + 0.0015*m.x307 + 0.006*m.x310 <= 0)

m.c932 = Constraint(expr= - 0.0035*m.x134 - 0.0035*m.x161 - 0.0035*m.x164 - 0.0035*m.x167 + 0.002*m.x170 + 0.0025*m.x173
                          + 0.0015*m.x176 + 0.006*m.x179 + 0.002*m.x278 + 0.0025*m.x281 + 0.0015*m.x284 + 0.006*m.x287
                          + 0.002*m.x290 + 0.0025*m.x293 + 0.0015*m.x296 + 0.006*m.x299 + 0.002*m.x302 + 0.0025*m.x305
                          + 0.0015*m.x308 + 0.006*m.x311 <= 0)

m.c933 = Constraint(expr= - 0.0035*m.x135 - 0.0035*m.x162 - 0.0035*m.x165 - 0.0035*m.x168 + 0.002*m.x171 + 0.0025*m.x174
                          + 0.0015*m.x177 + 0.006*m.x180 + 0.002*m.x279 + 0.0025*m.x282 + 0.0015*m.x285 + 0.006*m.x288
                          + 0.002*m.x291 + 0.0025*m.x294 + 0.0015*m.x297 + 0.006*m.x300 + 0.002*m.x303 + 0.0025*m.x306
                          + 0.0015*m.x309 + 0.006*m.x312 <= 0)

m.c934 = Constraint(expr=   m.x313 + m.x314 + m.x315 == 750)

m.c935 = Constraint(expr=   m.x316 + m.x317 + m.x318 == 750)

m.c936 = Constraint(expr=   m.x319 + m.x320 + m.x321 == 750)

m.c937 = Constraint(expr=   m.x435 - m.x530 >= 0)

m.c938 = Constraint(expr=   m.x436 - m.x531 >= 0)

m.c939 = Constraint(expr=   m.x438 - m.x533 >= 0)

m.c940 = Constraint(expr=   m.x439 - m.x534 >= 0)

m.c941 = Constraint(expr=   m.x441 - m.x536 >= 0)

m.c942 = Constraint(expr=   m.x442 - m.x537 >= 0)

m.c943 = Constraint(expr=   m.x444 - m.x539 >= 0)

m.c944 = Constraint(expr=   m.x445 - m.x540 >= 0)

m.c945 = Constraint(expr=   m.x447 - m.x542 >= 0)

m.c946 = Constraint(expr=   m.x448 - m.x543 >= 0)

m.c947 = Constraint(expr=   m.x450 - m.x545 >= 0)

m.c948 = Constraint(expr=   m.x451 - m.x546 >= 0)

m.c949 = Constraint(expr=   m.x453 - m.x548 >= 0)

m.c950 = Constraint(expr=   m.x454 - m.x549 >= 0)

m.c951 = Constraint(expr=   m.x456 - m.x551 >= 0)

m.c952 = Constraint(expr=   m.x457 - m.x552 >= 0)

m.c953 = Constraint(expr=   m.x459 - m.x554 >= 0)

m.c954 = Constraint(expr=   m.x460 - m.x555 >= 0)

m.c955 = Constraint(expr=   m.x462 - m.x557 >= 0)

m.c956 = Constraint(expr=   m.x463 - m.x558 >= 0)

m.c957 = Constraint(expr=   m.x465 - m.x560 >= 0)

m.c958 = Constraint(expr=   m.x466 - m.x561 >= 0)

m.c959 = Constraint(expr=   m.x468 - m.x563 >= 0)

m.c960 = Constraint(expr=   m.x469 - m.x564 >= 0)

m.c961 = Constraint(expr=   m.x471 - m.x566 >= 0)

m.c962 = Constraint(expr=   m.x472 - m.x567 >= 0)

m.c963 = Constraint(expr=   m.x474 - m.x569 >= 0)

m.c964 = Constraint(expr=   m.x475 - m.x570 >= 0)

m.c965 = Constraint(expr=   m.x477 - m.x572 >= 0)

m.c966 = Constraint(expr=   m.x478 - m.x573 >= 0)

m.c967 = Constraint(expr=   m.x480 - m.x575 >= 0)

m.c968 = Constraint(expr=   m.x481 - m.x576 >= 0)

m.c969 = Constraint(expr=   m.x483 - m.x578 >= 0)

m.c970 = Constraint(expr=   m.x484 - m.x579 >= 0)

m.c971 = Constraint(expr=   m.x486 - m.x581 >= 0)

m.c972 = Constraint(expr=   m.x487 - m.x582 >= 0)

m.c973 = Constraint(expr=   m.x489 - m.x584 >= 0)

m.c974 = Constraint(expr=   m.x490 - m.x585 >= 0)

m.c975 = Constraint(expr=   m.x492 - m.x587 >= 0)

m.c976 = Constraint(expr=   m.x493 - m.x588 >= 0)

m.c977 = Constraint(expr=   m.x495 - m.x590 >= 0)

m.c978 = Constraint(expr=   m.x496 - m.x591 >= 0)

m.c979 = Constraint(expr=   m.x498 - m.x593 >= 0)

m.c980 = Constraint(expr=   m.x499 - m.x594 >= 0)

m.c981 = Constraint(expr=   m.x501 - m.x596 >= 0)

m.c982 = Constraint(expr=   m.x502 - m.x597 >= 0)

m.c983 = Constraint(expr=   m.x504 - m.x599 >= 0)

m.c984 = Constraint(expr=   m.x505 - m.x600 >= 0)

m.c985 = Constraint(expr=   m.x507 - m.x602 >= 0)

m.c986 = Constraint(expr=   m.x508 - m.x603 >= 0)

m.c987 = Constraint(expr=   m.x510 - m.x605 >= 0)

m.c988 = Constraint(expr=   m.x511 - m.x606 >= 0)

m.c989 = Constraint(expr=   m.x513 - m.x608 >= 0)

m.c990 = Constraint(expr=   m.x514 - m.x609 >= 0)

m.c991 = Constraint(expr=   m.x516 - m.x611 >= 0)

m.c992 = Constraint(expr=   m.x517 - m.x612 >= 0)

m.c993 = Constraint(expr=   m.x519 - m.x614 >= 0)

m.c994 = Constraint(expr=   m.x520 - m.x615 >= 0)

m.c995 = Constraint(expr=   m.x522 - m.x617 >= 0)

m.c996 = Constraint(expr=   m.x523 - m.x618 >= 0)

m.c997 = Constraint(expr=   m.x525 - m.x620 >= 0)

m.c998 = Constraint(expr=   m.x526 - m.x621 >= 0)

m.c999 = Constraint(expr=   m.x528 - m.x623 >= 0)

m.c1000 = Constraint(expr=   m.x529 - m.x624 >= 0)

m.c1001 = Constraint(expr= - 160*m.b1 + m.x447 - m.x530 >= -160)

m.c1002 = Constraint(expr= - 160*m.b2 + m.x448 - m.x531 >= -160)

m.c1003 = Constraint(expr= - 160*m.b4 + m.x450 - m.x533 >= -160)

m.c1004 = Constraint(expr= - 160*m.b5 + m.x451 - m.x534 >= -160)

m.c1005 = Constraint(expr= - 160*m.b7 + m.x453 - m.x536 >= -160)

m.c1006 = Constraint(expr= - 160*m.b8 + m.x454 - m.x537 >= -160)

m.c1007 = Constraint(expr= - 160*m.b10 + m.x456 - m.x539 >= -160)

m.c1008 = Constraint(expr= - 160*m.b11 + m.x457 - m.x540 >= -160)

m.c1009 = Constraint(expr= - 160*m.b1 + m.x459 - m.x530 >= -160)

m.c1010 = Constraint(expr= - 160*m.b2 + m.x460 - m.x531 >= -160)

m.c1011 = Constraint(expr= - 160*m.b4 + m.x462 - m.x533 >= -160)

m.c1012 = Constraint(expr= - 160*m.b5 + m.x463 - m.x534 >= -160)

m.c1013 = Constraint(expr= - 160*m.b7 + m.x465 - m.x536 >= -160)

m.c1014 = Constraint(expr= - 160*m.b8 + m.x466 - m.x537 >= -160)

m.c1015 = Constraint(expr= - 160*m.b10 + m.x468 - m.x539 >= -160)

m.c1016 = Constraint(expr= - 160*m.b11 + m.x469 - m.x540 >= -160)

m.c1017 = Constraint(expr= - 160*m.b1 + m.x507 - m.x530 >= -160)

m.c1018 = Constraint(expr= - 160*m.b2 + m.x508 - m.x531 >= -160)

m.c1019 = Constraint(expr= - 160*m.b4 + m.x510 - m.x533 >= -160)

m.c1020 = Constraint(expr= - 160*m.b5 + m.x511 - m.x534 >= -160)

m.c1021 = Constraint(expr= - 160*m.b7 + m.x513 - m.x536 >= -160)

m.c1022 = Constraint(expr= - 160*m.b8 + m.x514 - m.x537 >= -160)

m.c1023 = Constraint(expr= - 160*m.b10 + m.x516 - m.x539 >= -160)

m.c1024 = Constraint(expr= - 160*m.b11 + m.x517 - m.x540 >= -160)

m.c1025 = Constraint(expr= - 160*m.b13 + m.x435 - m.x542 >= -160)

m.c1026 = Constraint(expr= - 160*m.b14 + m.x436 - m.x543 >= -160)

m.c1027 = Constraint(expr= - 160*m.b16 + m.x438 - m.x545 >= -160)

m.c1028 = Constraint(expr= - 160*m.b17 + m.x439 - m.x546 >= -160)

m.c1029 = Constraint(expr= - 160*m.b19 + m.x441 - m.x548 >= -160)

m.c1030 = Constraint(expr= - 160*m.b20 + m.x442 - m.x549 >= -160)

m.c1031 = Constraint(expr= - 160*m.b22 + m.x444 - m.x551 >= -160)

m.c1032 = Constraint(expr= - 160*m.b23 + m.x445 - m.x552 >= -160)

m.c1033 = Constraint(expr= - 160*m.b13 + m.x459 - m.x542 >= -160)

m.c1034 = Constraint(expr= - 160*m.b14 + m.x460 - m.x543 >= -160)

m.c1035 = Constraint(expr= - 160*m.b16 + m.x462 - m.x545 >= -160)

m.c1036 = Constraint(expr= - 160*m.b17 + m.x463 - m.x546 >= -160)

m.c1037 = Constraint(expr= - 160*m.b19 + m.x465 - m.x548 >= -160)

m.c1038 = Constraint(expr= - 160*m.b20 + m.x466 - m.x549 >= -160)

m.c1039 = Constraint(expr= - 160*m.b22 + m.x468 - m.x551 >= -160)

m.c1040 = Constraint(expr= - 160*m.b23 + m.x469 - m.x552 >= -160)

m.c1041 = Constraint(expr= - 160*m.b13 + m.x507 - m.x542 >= -160)

m.c1042 = Constraint(expr= - 160*m.b14 + m.x508 - m.x543 >= -160)

m.c1043 = Constraint(expr= - 160*m.b16 + m.x510 - m.x545 >= -160)

m.c1044 = Constraint(expr= - 160*m.b17 + m.x511 - m.x546 >= -160)

m.c1045 = Constraint(expr= - 160*m.b19 + m.x513 - m.x548 >= -160)

m.c1046 = Constraint(expr= - 160*m.b20 + m.x514 - m.x549 >= -160)

m.c1047 = Constraint(expr= - 160*m.b22 + m.x516 - m.x551 >= -160)

m.c1048 = Constraint(expr= - 160*m.b23 + m.x517 - m.x552 >= -160)

m.c1049 = Constraint(expr= - 160*m.b25 + m.x435 - m.x554 >= -160)

m.c1050 = Constraint(expr= - 160*m.b26 + m.x436 - m.x555 >= -160)

m.c1051 = Constraint(expr= - 160*m.b28 + m.x438 - m.x557 >= -160)

m.c1052 = Constraint(expr= - 160*m.b29 + m.x439 - m.x558 >= -160)

m.c1053 = Constraint(expr= - 160*m.b31 + m.x441 - m.x560 >= -160)

m.c1054 = Constraint(expr= - 160*m.b32 + m.x442 - m.x561 >= -160)

m.c1055 = Constraint(expr= - 160*m.b34 + m.x444 - m.x563 >= -160)

m.c1056 = Constraint(expr= - 160*m.b35 + m.x445 - m.x564 >= -160)

m.c1057 = Constraint(expr= - 160*m.b25 + m.x447 - m.x554 >= -160)

m.c1058 = Constraint(expr= - 160*m.b26 + m.x448 - m.x555 >= -160)

m.c1059 = Constraint(expr= - 160*m.b28 + m.x450 - m.x557 >= -160)

m.c1060 = Constraint(expr= - 160*m.b29 + m.x451 - m.x558 >= -160)

m.c1061 = Constraint(expr= - 160*m.b31 + m.x453 - m.x560 >= -160)

m.c1062 = Constraint(expr= - 160*m.b32 + m.x454 - m.x561 >= -160)

m.c1063 = Constraint(expr= - 160*m.b34 + m.x456 - m.x563 >= -160)

m.c1064 = Constraint(expr= - 160*m.b35 + m.x457 - m.x564 >= -160)

m.c1065 = Constraint(expr= - 160*m.b25 + m.x507 - m.x554 >= -160)

m.c1066 = Constraint(expr= - 160*m.b26 + m.x508 - m.x555 >= -160)

m.c1067 = Constraint(expr= - 160*m.b28 + m.x510 - m.x557 >= -160)

m.c1068 = Constraint(expr= - 160*m.b29 + m.x511 - m.x558 >= -160)

m.c1069 = Constraint(expr= - 160*m.b31 + m.x513 - m.x560 >= -160)

m.c1070 = Constraint(expr= - 160*m.b32 + m.x514 - m.x561 >= -160)

m.c1071 = Constraint(expr= - 160*m.b34 + m.x516 - m.x563 >= -160)

m.c1072 = Constraint(expr= - 160*m.b35 + m.x517 - m.x564 >= -160)

m.c1073 = Constraint(expr= - 160*m.b37 + m.x483 - m.x566 >= -160)

m.c1074 = Constraint(expr= - 160*m.b38 + m.x484 - m.x567 >= -160)

m.c1075 = Constraint(expr= - 160*m.b40 + m.x486 - m.x569 >= -160)

m.c1076 = Constraint(expr= - 160*m.b41 + m.x487 - m.x570 >= -160)

m.c1077 = Constraint(expr= - 160*m.b43 + m.x489 - m.x572 >= -160)

m.c1078 = Constraint(expr= - 160*m.b44 + m.x490 - m.x573 >= -160)

m.c1079 = Constraint(expr= - 160*m.b46 + m.x492 - m.x575 >= -160)

m.c1080 = Constraint(expr= - 160*m.b47 + m.x493 - m.x576 >= -160)

m.c1081 = Constraint(expr= - 160*m.b37 + m.x495 - m.x566 >= -160)

m.c1082 = Constraint(expr= - 160*m.b38 + m.x496 - m.x567 >= -160)

m.c1083 = Constraint(expr= - 160*m.b40 + m.x498 - m.x569 >= -160)

m.c1084 = Constraint(expr= - 160*m.b41 + m.x499 - m.x570 >= -160)

m.c1085 = Constraint(expr= - 160*m.b43 + m.x501 - m.x572 >= -160)

m.c1086 = Constraint(expr= - 160*m.b44 + m.x502 - m.x573 >= -160)

m.c1087 = Constraint(expr= - 160*m.b46 + m.x504 - m.x575 >= -160)

m.c1088 = Constraint(expr= - 160*m.b47 + m.x505 - m.x576 >= -160)

m.c1089 = Constraint(expr= - 160*m.b37 + m.x519 - m.x566 >= -160)

m.c1090 = Constraint(expr= - 160*m.b38 + m.x520 - m.x567 >= -160)

m.c1091 = Constraint(expr= - 160*m.b40 + m.x522 - m.x569 >= -160)

m.c1092 = Constraint(expr= - 160*m.b41 + m.x523 - m.x570 >= -160)

m.c1093 = Constraint(expr= - 160*m.b43 + m.x525 - m.x572 >= -160)

m.c1094 = Constraint(expr= - 160*m.b44 + m.x526 - m.x573 >= -160)

m.c1095 = Constraint(expr= - 160*m.b46 + m.x528 - m.x575 >= -160)

m.c1096 = Constraint(expr= - 160*m.b47 + m.x529 - m.x576 >= -160)

m.c1097 = Constraint(expr= - 160*m.b49 + m.x471 - m.x578 >= -160)

m.c1098 = Constraint(expr= - 160*m.b50 + m.x472 - m.x579 >= -160)

m.c1099 = Constraint(expr= - 160*m.b52 + m.x474 - m.x581 >= -160)

m.c1100 = Constraint(expr= - 160*m.b53 + m.x475 - m.x582 >= -160)

m.c1101 = Constraint(expr= - 160*m.b55 + m.x477 - m.x584 >= -160)

m.c1102 = Constraint(expr= - 160*m.b56 + m.x478 - m.x585 >= -160)

m.c1103 = Constraint(expr= - 160*m.b58 + m.x480 - m.x587 >= -160)

m.c1104 = Constraint(expr= - 160*m.b59 + m.x481 - m.x588 >= -160)

m.c1105 = Constraint(expr= - 160*m.b49 + m.x495 - m.x578 >= -160)

m.c1106 = Constraint(expr= - 160*m.b50 + m.x496 - m.x579 >= -160)

m.c1107 = Constraint(expr= - 160*m.b52 + m.x498 - m.x581 >= -160)

m.c1108 = Constraint(expr= - 160*m.b53 + m.x499 - m.x582 >= -160)

m.c1109 = Constraint(expr= - 160*m.b55 + m.x501 - m.x584 >= -160)

m.c1110 = Constraint(expr= - 160*m.b56 + m.x502 - m.x585 >= -160)

m.c1111 = Constraint(expr= - 160*m.b58 + m.x504 - m.x587 >= -160)

m.c1112 = Constraint(expr= - 160*m.b59 + m.x505 - m.x588 >= -160)

m.c1113 = Constraint(expr= - 160*m.b49 + m.x519 - m.x578 >= -160)

m.c1114 = Constraint(expr= - 160*m.b50 + m.x520 - m.x579 >= -160)

m.c1115 = Constraint(expr= - 160*m.b52 + m.x522 - m.x581 >= -160)

m.c1116 = Constraint(expr= - 160*m.b53 + m.x523 - m.x582 >= -160)

m.c1117 = Constraint(expr= - 160*m.b55 + m.x525 - m.x584 >= -160)

m.c1118 = Constraint(expr= - 160*m.b56 + m.x526 - m.x585 >= -160)

m.c1119 = Constraint(expr= - 160*m.b58 + m.x528 - m.x587 >= -160)

m.c1120 = Constraint(expr= - 160*m.b59 + m.x529 - m.x588 >= -160)

m.c1121 = Constraint(expr= - 160*m.b61 + m.x471 - m.x590 >= -160)

m.c1122 = Constraint(expr= - 160*m.b62 + m.x472 - m.x591 >= -160)

m.c1123 = Constraint(expr= - 160*m.b64 + m.x474 - m.x593 >= -160)

m.c1124 = Constraint(expr= - 160*m.b65 + m.x475 - m.x594 >= -160)

m.c1125 = Constraint(expr= - 160*m.b67 + m.x477 - m.x596 >= -160)

m.c1126 = Constraint(expr= - 160*m.b68 + m.x478 - m.x597 >= -160)

m.c1127 = Constraint(expr= - 160*m.b70 + m.x480 - m.x599 >= -160)

m.c1128 = Constraint(expr= - 160*m.b71 + m.x481 - m.x600 >= -160)

m.c1129 = Constraint(expr= - 160*m.b61 + m.x483 - m.x590 >= -160)

m.c1130 = Constraint(expr= - 160*m.b62 + m.x484 - m.x591 >= -160)

m.c1131 = Constraint(expr= - 160*m.b64 + m.x486 - m.x593 >= -160)

m.c1132 = Constraint(expr= - 160*m.b65 + m.x487 - m.x594 >= -160)

m.c1133 = Constraint(expr= - 160*m.b67 + m.x489 - m.x596 >= -160)

m.c1134 = Constraint(expr= - 160*m.b68 + m.x490 - m.x597 >= -160)

m.c1135 = Constraint(expr= - 160*m.b70 + m.x492 - m.x599 >= -160)

m.c1136 = Constraint(expr= - 160*m.b71 + m.x493 - m.x600 >= -160)

m.c1137 = Constraint(expr= - 160*m.b61 + m.x519 - m.x590 >= -160)

m.c1138 = Constraint(expr= - 160*m.b62 + m.x520 - m.x591 >= -160)

m.c1139 = Constraint(expr= - 160*m.b64 + m.x522 - m.x593 >= -160)

m.c1140 = Constraint(expr= - 160*m.b65 + m.x523 - m.x594 >= -160)

m.c1141 = Constraint(expr= - 160*m.b67 + m.x525 - m.x596 >= -160)

m.c1142 = Constraint(expr= - 160*m.b68 + m.x526 - m.x597 >= -160)

m.c1143 = Constraint(expr= - 160*m.b70 + m.x528 - m.x599 >= -160)

m.c1144 = Constraint(expr= - 160*m.b71 + m.x529 - m.x600 >= -160)

m.c1145 = Constraint(expr= - 160*m.b73 + m.x435 - m.x602 >= -160)

m.c1146 = Constraint(expr= - 160*m.b74 + m.x436 - m.x603 >= -160)

m.c1147 = Constraint(expr= - 160*m.b76 + m.x438 - m.x605 >= -160)

m.c1148 = Constraint(expr= - 160*m.b77 + m.x439 - m.x606 >= -160)

m.c1149 = Constraint(expr= - 160*m.b79 + m.x441 - m.x608 >= -160)

m.c1150 = Constraint(expr= - 160*m.b80 + m.x442 - m.x609 >= -160)

m.c1151 = Constraint(expr= - 160*m.b82 + m.x444 - m.x611 >= -160)

m.c1152 = Constraint(expr= - 160*m.b83 + m.x445 - m.x612 >= -160)

m.c1153 = Constraint(expr= - 160*m.b73 + m.x447 - m.x602 >= -160)

m.c1154 = Constraint(expr= - 160*m.b74 + m.x448 - m.x603 >= -160)

m.c1155 = Constraint(expr= - 160*m.b76 + m.x450 - m.x605 >= -160)

m.c1156 = Constraint(expr= - 160*m.b77 + m.x451 - m.x606 >= -160)

m.c1157 = Constraint(expr= - 160*m.b79 + m.x453 - m.x608 >= -160)

m.c1158 = Constraint(expr= - 160*m.b80 + m.x454 - m.x609 >= -160)

m.c1159 = Constraint(expr= - 160*m.b82 + m.x456 - m.x611 >= -160)

m.c1160 = Constraint(expr= - 160*m.b83 + m.x457 - m.x612 >= -160)

m.c1161 = Constraint(expr= - 160*m.b73 + m.x459 - m.x602 >= -160)

m.c1162 = Constraint(expr= - 160*m.b74 + m.x460 - m.x603 >= -160)

m.c1163 = Constraint(expr= - 160*m.b76 + m.x462 - m.x605 >= -160)

m.c1164 = Constraint(expr= - 160*m.b77 + m.x463 - m.x606 >= -160)

m.c1165 = Constraint(expr= - 160*m.b79 + m.x465 - m.x608 >= -160)

m.c1166 = Constraint(expr= - 160*m.b80 + m.x466 - m.x609 >= -160)

m.c1167 = Constraint(expr= - 160*m.b82 + m.x468 - m.x611 >= -160)

m.c1168 = Constraint(expr= - 160*m.b83 + m.x469 - m.x612 >= -160)

m.c1169 = Constraint(expr= - 160*m.b85 + m.x471 - m.x614 >= -160)

m.c1170 = Constraint(expr= - 160*m.b86 + m.x472 - m.x615 >= -160)

m.c1171 = Constraint(expr= - 160*m.b88 + m.x474 - m.x617 >= -160)

m.c1172 = Constraint(expr= - 160*m.b89 + m.x475 - m.x618 >= -160)

m.c1173 = Constraint(expr= - 160*m.b91 + m.x477 - m.x620 >= -160)

m.c1174 = Constraint(expr= - 160*m.b92 + m.x478 - m.x621 >= -160)

m.c1175 = Constraint(expr= - 160*m.b94 + m.x480 - m.x623 >= -160)

m.c1176 = Constraint(expr= - 160*m.b95 + m.x481 - m.x624 >= -160)

m.c1177 = Constraint(expr= - 160*m.b85 + m.x483 - m.x614 >= -160)

m.c1178 = Constraint(expr= - 160*m.b86 + m.x484 - m.x615 >= -160)

m.c1179 = Constraint(expr= - 160*m.b88 + m.x486 - m.x617 >= -160)

m.c1180 = Constraint(expr= - 160*m.b89 + m.x487 - m.x618 >= -160)

m.c1181 = Constraint(expr= - 160*m.b91 + m.x489 - m.x620 >= -160)

m.c1182 = Constraint(expr= - 160*m.b92 + m.x490 - m.x621 >= -160)

m.c1183 = Constraint(expr= - 160*m.b94 + m.x492 - m.x623 >= -160)

m.c1184 = Constraint(expr= - 160*m.b95 + m.x493 - m.x624 >= -160)

m.c1185 = Constraint(expr= - 160*m.b85 + m.x495 - m.x614 >= -160)

m.c1186 = Constraint(expr= - 160*m.b86 + m.x496 - m.x615 >= -160)

m.c1187 = Constraint(expr= - 160*m.b88 + m.x498 - m.x617 >= -160)

m.c1188 = Constraint(expr= - 160*m.b89 + m.x499 - m.x618 >= -160)

m.c1189 = Constraint(expr= - 160*m.b91 + m.x501 - m.x620 >= -160)

m.c1190 = Constraint(expr= - 160*m.b92 + m.x502 - m.x621 >= -160)

m.c1191 = Constraint(expr= - 160*m.b94 + m.x504 - m.x623 >= -160)

m.c1192 = Constraint(expr= - 160*m.b95 + m.x505 - m.x624 >= -160)

m.c1193 = Constraint(expr=   m.x627 - m.x662 >= 0)

m.c1194 = Constraint(expr=   m.x628 - m.x663 >= 0)

m.c1195 = Constraint(expr=   m.x630 - m.x665 >= 0)

m.c1196 = Constraint(expr=   m.x631 - m.x666 >= 0)

m.c1197 = Constraint(expr=   m.x633 - m.x668 >= 0)

m.c1198 = Constraint(expr=   m.x634 - m.x669 >= 0)

m.c1199 = Constraint(expr=   m.x636 - m.x671 >= 0)

m.c1200 = Constraint(expr=   m.x637 - m.x672 >= 0)

m.c1201 = Constraint(expr=   m.x639 - m.x674 >= 0)

m.c1202 = Constraint(expr=   m.x640 - m.x675 >= 0)

m.c1203 = Constraint(expr=   m.x642 - m.x677 >= 0)

m.c1204 = Constraint(expr=   m.x643 - m.x678 >= 0)

m.c1205 = Constraint(expr=   m.x645 - m.x680 >= 0)

m.c1206 = Constraint(expr=   m.x646 - m.x681 >= 0)

m.c1207 = Constraint(expr=   m.x648 - m.x683 >= 0)

m.c1208 = Constraint(expr=   m.x649 - m.x684 >= 0)

m.c1209 = Constraint(expr=   m.x651 - m.x686 >= 0)

m.c1210 = Constraint(expr=   m.x652 - m.x687 >= 0)

m.c1211 = Constraint(expr=   m.x654 - m.x689 >= 0)

m.c1212 = Constraint(expr=   m.x655 - m.x690 >= 0)

m.c1213 = Constraint(expr=   m.x657 - m.x692 >= 0)

m.c1214 = Constraint(expr=   m.x658 - m.x693 >= 0)

m.c1215 = Constraint(expr=   m.x660 - m.x695 >= 0)

m.c1216 = Constraint(expr=   m.x661 - m.x696 >= 0)

m.c1217 = Constraint(expr= - 160*m.b97 + m.x435 - m.x662 >= -160)

m.c1218 = Constraint(expr= - 160*m.b98 + m.x436 - m.x663 >= -160)

m.c1219 = Constraint(expr= - 160*m.b124 + m.x438 - m.x689 >= -160)

m.c1220 = Constraint(expr= - 160*m.b125 + m.x439 - m.x690 >= -160)

m.c1221 = Constraint(expr= - 160*m.b127 + m.x441 - m.x692 >= -160)

m.c1222 = Constraint(expr= - 160*m.b128 + m.x442 - m.x693 >= -160)

m.c1223 = Constraint(expr= - 160*m.b130 + m.x444 - m.x695 >= -160)

m.c1224 = Constraint(expr= - 160*m.b131 + m.x445 - m.x696 >= -160)

m.c1225 = Constraint(expr= - 160*m.b97 + m.x447 - m.x662 >= -160)

m.c1226 = Constraint(expr= - 160*m.b98 + m.x448 - m.x663 >= -160)

m.c1227 = Constraint(expr= - 160*m.b124 + m.x450 - m.x689 >= -160)

m.c1228 = Constraint(expr= - 160*m.b125 + m.x451 - m.x690 >= -160)

m.c1229 = Constraint(expr= - 160*m.b127 + m.x453 - m.x692 >= -160)

m.c1230 = Constraint(expr= - 160*m.b128 + m.x454 - m.x693 >= -160)

m.c1231 = Constraint(expr= - 160*m.b130 + m.x456 - m.x695 >= -160)

m.c1232 = Constraint(expr= - 160*m.b131 + m.x457 - m.x696 >= -160)

m.c1233 = Constraint(expr= - 160*m.b97 + m.x459 - m.x662 >= -160)

m.c1234 = Constraint(expr= - 160*m.b98 + m.x460 - m.x663 >= -160)

m.c1235 = Constraint(expr= - 160*m.b124 + m.x462 - m.x689 >= -160)

m.c1236 = Constraint(expr= - 160*m.b125 + m.x463 - m.x690 >= -160)

m.c1237 = Constraint(expr= - 160*m.b127 + m.x465 - m.x692 >= -160)

m.c1238 = Constraint(expr= - 160*m.b128 + m.x466 - m.x693 >= -160)

m.c1239 = Constraint(expr= - 160*m.b130 + m.x468 - m.x695 >= -160)

m.c1240 = Constraint(expr= - 160*m.b131 + m.x469 - m.x696 >= -160)

m.c1241 = Constraint(expr= - 160*m.b100 + m.x471 - m.x665 >= -160)

m.c1242 = Constraint(expr= - 160*m.b101 + m.x472 - m.x666 >= -160)

m.c1243 = Constraint(expr= - 160*m.b103 + m.x471 - m.x668 >= -160)

m.c1244 = Constraint(expr= - 160*m.b104 + m.x472 - m.x669 >= -160)

m.c1245 = Constraint(expr= - 160*m.b106 + m.x474 - m.x671 >= -160)

m.c1246 = Constraint(expr= - 160*m.b107 + m.x475 - m.x672 >= -160)

m.c1247 = Constraint(expr= - 160*m.b109 + m.x474 - m.x674 >= -160)

m.c1248 = Constraint(expr= - 160*m.b110 + m.x475 - m.x675 >= -160)

m.c1249 = Constraint(expr= - 160*m.b112 + m.x477 - m.x677 >= -160)

m.c1250 = Constraint(expr= - 160*m.b113 + m.x478 - m.x678 >= -160)

m.c1251 = Constraint(expr= - 160*m.b115 + m.x477 - m.x680 >= -160)

m.c1252 = Constraint(expr= - 160*m.b116 + m.x478 - m.x681 >= -160)

m.c1253 = Constraint(expr= - 160*m.b118 + m.x480 - m.x683 >= -160)

m.c1254 = Constraint(expr= - 160*m.b119 + m.x481 - m.x684 >= -160)

m.c1255 = Constraint(expr= - 160*m.b121 + m.x480 - m.x686 >= -160)

m.c1256 = Constraint(expr= - 160*m.b122 + m.x481 - m.x687 >= -160)

m.c1257 = Constraint(expr= - 160*m.b100 + m.x483 - m.x665 >= -160)

m.c1258 = Constraint(expr= - 160*m.b101 + m.x484 - m.x666 >= -160)

m.c1259 = Constraint(expr= - 160*m.b103 + m.x483 - m.x668 >= -160)

m.c1260 = Constraint(expr= - 160*m.b104 + m.x484 - m.x669 >= -160)

m.c1261 = Constraint(expr= - 160*m.b106 + m.x486 - m.x671 >= -160)

m.c1262 = Constraint(expr= - 160*m.b107 + m.x487 - m.x672 >= -160)

m.c1263 = Constraint(expr= - 160*m.b109 + m.x486 - m.x674 >= -160)

m.c1264 = Constraint(expr= - 160*m.b110 + m.x487 - m.x675 >= -160)

m.c1265 = Constraint(expr= - 160*m.b112 + m.x489 - m.x677 >= -160)

m.c1266 = Constraint(expr= - 160*m.b113 + m.x490 - m.x678 >= -160)

m.c1267 = Constraint(expr= - 160*m.b115 + m.x489 - m.x680 >= -160)

m.c1268 = Constraint(expr= - 160*m.b116 + m.x490 - m.x681 >= -160)

m.c1269 = Constraint(expr= - 160*m.b118 + m.x492 - m.x683 >= -160)

m.c1270 = Constraint(expr= - 160*m.b119 + m.x493 - m.x684 >= -160)

m.c1271 = Constraint(expr= - 160*m.b121 + m.x492 - m.x686 >= -160)

m.c1272 = Constraint(expr= - 160*m.b122 + m.x493 - m.x687 >= -160)

m.c1273 = Constraint(expr= - 160*m.b100 + m.x495 - m.x665 >= -160)

m.c1274 = Constraint(expr= - 160*m.b101 + m.x496 - m.x666 >= -160)

m.c1275 = Constraint(expr= - 160*m.b103 + m.x495 - m.x668 >= -160)

m.c1276 = Constraint(expr= - 160*m.b104 + m.x496 - m.x669 >= -160)

m.c1277 = Constraint(expr= - 160*m.b106 + m.x498 - m.x671 >= -160)

m.c1278 = Constraint(expr= - 160*m.b107 + m.x499 - m.x672 >= -160)

m.c1279 = Constraint(expr= - 160*m.b109 + m.x498 - m.x674 >= -160)

m.c1280 = Constraint(expr= - 160*m.b110 + m.x499 - m.x675 >= -160)

m.c1281 = Constraint(expr= - 160*m.b112 + m.x501 - m.x677 >= -160)

m.c1282 = Constraint(expr= - 160*m.b113 + m.x502 - m.x678 >= -160)

m.c1283 = Constraint(expr= - 160*m.b115 + m.x501 - m.x680 >= -160)

m.c1284 = Constraint(expr= - 160*m.b116 + m.x502 - m.x681 >= -160)

m.c1285 = Constraint(expr= - 160*m.b118 + m.x504 - m.x683 >= -160)

m.c1286 = Constraint(expr= - 160*m.b119 + m.x505 - m.x684 >= -160)

m.c1287 = Constraint(expr= - 160*m.b121 + m.x504 - m.x686 >= -160)

m.c1288 = Constraint(expr= - 160*m.b122 + m.x505 - m.x687 >= -160)

m.c1289 = Constraint(expr= - 160*m.b97 + m.x507 - m.x662 >= -160)

m.c1290 = Constraint(expr= - 160*m.b98 + m.x508 - m.x663 >= -160)

m.c1291 = Constraint(expr= - 160*m.b124 + m.x510 - m.x689 >= -160)

m.c1292 = Constraint(expr= - 160*m.b125 + m.x511 - m.x690 >= -160)

m.c1293 = Constraint(expr= - 160*m.b127 + m.x513 - m.x692 >= -160)

m.c1294 = Constraint(expr= - 160*m.b128 + m.x514 - m.x693 >= -160)

m.c1295 = Constraint(expr= - 160*m.b130 + m.x516 - m.x695 >= -160)

m.c1296 = Constraint(expr= - 160*m.b131 + m.x517 - m.x696 >= -160)

m.c1297 = Constraint(expr= - 160*m.b100 + m.x519 - m.x665 >= -160)

m.c1298 = Constraint(expr= - 160*m.b101 + m.x520 - m.x666 >= -160)

m.c1299 = Constraint(expr= - 160*m.b103 + m.x519 - m.x668 >= -160)

m.c1300 = Constraint(expr= - 160*m.b104 + m.x520 - m.x669 >= -160)

m.c1301 = Constraint(expr= - 160*m.b106 + m.x522 - m.x671 >= -160)

m.c1302 = Constraint(expr= - 160*m.b107 + m.x523 - m.x672 >= -160)

m.c1303 = Constraint(expr= - 160*m.b109 + m.x522 - m.x674 >= -160)

m.c1304 = Constraint(expr= - 160*m.b110 + m.x523 - m.x675 >= -160)

m.c1305 = Constraint(expr= - 160*m.b112 + m.x525 - m.x677 >= -160)

m.c1306 = Constraint(expr= - 160*m.b113 + m.x526 - m.x678 >= -160)

m.c1307 = Constraint(expr= - 160*m.b115 + m.x525 - m.x680 >= -160)

m.c1308 = Constraint(expr= - 160*m.b116 + m.x526 - m.x681 >= -160)

m.c1309 = Constraint(expr= - 160*m.b118 + m.x528 - m.x683 >= -160)

m.c1310 = Constraint(expr= - 160*m.b119 + m.x529 - m.x684 >= -160)

m.c1311 = Constraint(expr= - 160*m.b121 + m.x528 - m.x686 >= -160)

m.c1312 = Constraint(expr= - 160*m.b122 + m.x529 - m.x687 >= -160)

m.c1313 = Constraint(expr= - 168*m.b1 - m.x530 + m.x627 >= -160)

m.c1314 = Constraint(expr= - 168*m.b2 - m.x531 + m.x628 >= -160)

m.c1315 = Constraint(expr= - 168*m.b4 - m.x533 + m.x654 >= -160)

m.c1316 = Constraint(expr= - 168*m.b5 - m.x534 + m.x655 >= -160)

m.c1317 = Constraint(expr= - 168*m.b7 - m.x536 + m.x657 >= -160)

m.c1318 = Constraint(expr= - 168*m.b8 - m.x537 + m.x658 >= -160)

m.c1319 = Constraint(expr= - 168*m.b10 - m.x539 + m.x660 >= -160)

m.c1320 = Constraint(expr= - 168*m.b11 - m.x540 + m.x661 >= -160)

m.c1321 = Constraint(expr= - 168*m.b13 - m.x542 + m.x627 >= -160)

m.c1322 = Constraint(expr= - 168*m.b14 - m.x543 + m.x628 >= -160)

m.c1323 = Constraint(expr= - 168*m.b16 - m.x545 + m.x654 >= -160)

m.c1324 = Constraint(expr= - 168*m.b17 - m.x546 + m.x655 >= -160)

m.c1325 = Constraint(expr= - 168*m.b19 - m.x548 + m.x657 >= -160)

m.c1326 = Constraint(expr= - 168*m.b20 - m.x549 + m.x658 >= -160)

m.c1327 = Constraint(expr= - 168*m.b22 - m.x551 + m.x660 >= -160)

m.c1328 = Constraint(expr= - 168*m.b23 - m.x552 + m.x661 >= -160)

m.c1329 = Constraint(expr= - 168*m.b25 - m.x554 + m.x627 >= -160)

m.c1330 = Constraint(expr= - 168*m.b26 - m.x555 + m.x628 >= -160)

m.c1331 = Constraint(expr= - 168*m.b28 - m.x557 + m.x654 >= -160)

m.c1332 = Constraint(expr= - 168*m.b29 - m.x558 + m.x655 >= -160)

m.c1333 = Constraint(expr= - 168*m.b31 - m.x560 + m.x657 >= -160)

m.c1334 = Constraint(expr= - 168*m.b32 - m.x561 + m.x658 >= -160)

m.c1335 = Constraint(expr= - 168*m.b34 - m.x563 + m.x660 >= -160)

m.c1336 = Constraint(expr= - 168*m.b35 - m.x564 + m.x661 >= -160)

m.c1337 = Constraint(expr= - 168*m.b37 - m.x566 + m.x630 >= -160)

m.c1338 = Constraint(expr= - 168*m.b38 - m.x567 + m.x631 >= -160)

m.c1339 = Constraint(expr= - 168*m.b37 - m.x566 + m.x633 >= -160)

m.c1340 = Constraint(expr= - 168*m.b38 - m.x567 + m.x634 >= -160)

m.c1341 = Constraint(expr= - 168*m.b40 - m.x569 + m.x636 >= -160)

m.c1342 = Constraint(expr= - 168*m.b41 - m.x570 + m.x637 >= -160)

m.c1343 = Constraint(expr= - 168*m.b40 - m.x569 + m.x639 >= -160)

m.c1344 = Constraint(expr= - 168*m.b41 - m.x570 + m.x640 >= -160)

m.c1345 = Constraint(expr= - 168*m.b43 - m.x572 + m.x642 >= -160)

m.c1346 = Constraint(expr= - 168*m.b44 - m.x573 + m.x643 >= -160)

m.c1347 = Constraint(expr= - 168*m.b43 - m.x572 + m.x645 >= -160)

m.c1348 = Constraint(expr= - 168*m.b44 - m.x573 + m.x646 >= -160)

m.c1349 = Constraint(expr= - 168*m.b46 - m.x575 + m.x648 >= -160)

m.c1350 = Constraint(expr= - 168*m.b47 - m.x576 + m.x649 >= -160)

m.c1351 = Constraint(expr= - 168*m.b46 - m.x575 + m.x651 >= -160)

m.c1352 = Constraint(expr= - 168*m.b47 - m.x576 + m.x652 >= -160)

m.c1353 = Constraint(expr= - 168*m.b49 - m.x578 + m.x630 >= -160)

m.c1354 = Constraint(expr= - 168*m.b50 - m.x579 + m.x631 >= -160)

m.c1355 = Constraint(expr= - 168*m.b49 - m.x578 + m.x633 >= -160)

m.c1356 = Constraint(expr= - 168*m.b50 - m.x579 + m.x634 >= -160)

m.c1357 = Constraint(expr= - 168*m.b52 - m.x581 + m.x636 >= -160)

m.c1358 = Constraint(expr= - 168*m.b53 - m.x582 + m.x637 >= -160)

m.c1359 = Constraint(expr= - 168*m.b52 - m.x581 + m.x639 >= -160)

m.c1360 = Constraint(expr= - 168*m.b53 - m.x582 + m.x640 >= -160)

m.c1361 = Constraint(expr= - 168*m.b55 - m.x584 + m.x642 >= -160)

m.c1362 = Constraint(expr= - 168*m.b56 - m.x585 + m.x643 >= -160)

m.c1363 = Constraint(expr= - 168*m.b55 - m.x584 + m.x645 >= -160)

m.c1364 = Constraint(expr= - 168*m.b56 - m.x585 + m.x646 >= -160)

m.c1365 = Constraint(expr= - 168*m.b58 - m.x587 + m.x648 >= -160)

m.c1366 = Constraint(expr= - 168*m.b59 - m.x588 + m.x649 >= -160)

m.c1367 = Constraint(expr= - 168*m.b58 - m.x587 + m.x651 >= -160)

m.c1368 = Constraint(expr= - 168*m.b59 - m.x588 + m.x652 >= -160)

m.c1369 = Constraint(expr= - 168*m.b61 - m.x590 + m.x630 >= -160)

m.c1370 = Constraint(expr= - 168*m.b62 - m.x591 + m.x631 >= -160)

m.c1371 = Constraint(expr= - 168*m.b61 - m.x590 + m.x633 >= -160)

m.c1372 = Constraint(expr= - 168*m.b62 - m.x591 + m.x634 >= -160)

m.c1373 = Constraint(expr= - 168*m.b64 - m.x593 + m.x636 >= -160)

m.c1374 = Constraint(expr= - 168*m.b65 - m.x594 + m.x637 >= -160)

m.c1375 = Constraint(expr= - 168*m.b64 - m.x593 + m.x639 >= -160)

m.c1376 = Constraint(expr= - 168*m.b65 - m.x594 + m.x640 >= -160)

m.c1377 = Constraint(expr= - 168*m.b67 - m.x596 + m.x642 >= -160)

m.c1378 = Constraint(expr= - 168*m.b68 - m.x597 + m.x643 >= -160)

m.c1379 = Constraint(expr= - 168*m.b67 - m.x596 + m.x645 >= -160)

m.c1380 = Constraint(expr= - 168*m.b68 - m.x597 + m.x646 >= -160)

m.c1381 = Constraint(expr= - 168*m.b70 - m.x599 + m.x648 >= -160)

m.c1382 = Constraint(expr= - 168*m.b71 - m.x600 + m.x649 >= -160)

m.c1383 = Constraint(expr= - 168*m.b70 - m.x599 + m.x651 >= -160)

m.c1384 = Constraint(expr= - 168*m.b71 - m.x600 + m.x652 >= -160)

m.c1385 = Constraint(expr= - 168*m.b73 - m.x602 + m.x627 >= -160)

m.c1386 = Constraint(expr= - 168*m.b74 - m.x603 + m.x628 >= -160)

m.c1387 = Constraint(expr= - 168*m.b76 - m.x605 + m.x654 >= -160)

m.c1388 = Constraint(expr= - 168*m.b77 - m.x606 + m.x655 >= -160)

m.c1389 = Constraint(expr= - 168*m.b79 - m.x608 + m.x657 >= -160)

m.c1390 = Constraint(expr= - 168*m.b80 - m.x609 + m.x658 >= -160)

m.c1391 = Constraint(expr= - 168*m.b82 - m.x611 + m.x660 >= -160)

m.c1392 = Constraint(expr= - 168*m.b83 - m.x612 + m.x661 >= -160)

m.c1393 = Constraint(expr= - 168*m.b85 - m.x614 + m.x630 >= -160)

m.c1394 = Constraint(expr= - 168*m.b86 - m.x615 + m.x631 >= -160)

m.c1395 = Constraint(expr= - 168*m.b85 - m.x614 + m.x633 >= -160)

m.c1396 = Constraint(expr= - 168*m.b86 - m.x615 + m.x634 >= -160)

m.c1397 = Constraint(expr= - 168*m.b88 - m.x617 + m.x636 >= -160)

m.c1398 = Constraint(expr= - 168*m.b89 - m.x618 + m.x637 >= -160)

m.c1399 = Constraint(expr= - 168*m.b88 - m.x617 + m.x639 >= -160)

m.c1400 = Constraint(expr= - 168*m.b89 - m.x618 + m.x640 >= -160)

m.c1401 = Constraint(expr= - 168*m.b91 - m.x620 + m.x642 >= -160)

m.c1402 = Constraint(expr= - 168*m.b92 - m.x621 + m.x643 >= -160)

m.c1403 = Constraint(expr= - 168*m.b91 - m.x620 + m.x645 >= -160)

m.c1404 = Constraint(expr= - 168*m.b92 - m.x621 + m.x646 >= -160)

m.c1405 = Constraint(expr= - 168*m.b94 - m.x623 + m.x648 >= -160)

m.c1406 = Constraint(expr= - 168*m.b95 - m.x624 + m.x649 >= -160)

m.c1407 = Constraint(expr= - 168*m.b94 - m.x623 + m.x651 >= -160)

m.c1408 = Constraint(expr= - 168*m.b95 - m.x624 + m.x652 >= -160)

m.c1409 = Constraint(expr= - 160*m.b103 + m.x630 - m.x668 >= -160)

m.c1410 = Constraint(expr= - 160*m.b104 + m.x631 - m.x669 >= -160)

m.c1411 = Constraint(expr= - 160*m.b100 + m.x633 - m.x665 >= -160)

m.c1412 = Constraint(expr= - 160*m.b101 + m.x634 - m.x666 >= -160)

m.c1413 = Constraint(expr= - 160*m.b109 + m.x636 - m.x674 >= -160)

m.c1414 = Constraint(expr= - 160*m.b110 + m.x637 - m.x675 >= -160)

m.c1415 = Constraint(expr= - 160*m.b106 + m.x639 - m.x671 >= -160)

m.c1416 = Constraint(expr= - 160*m.b107 + m.x640 - m.x672 >= -160)

m.c1417 = Constraint(expr= - 160*m.b115 + m.x642 - m.x680 >= -160)

m.c1418 = Constraint(expr= - 160*m.b116 + m.x643 - m.x681 >= -160)

m.c1419 = Constraint(expr= - 160*m.b112 + m.x645 - m.x677 >= -160)

m.c1420 = Constraint(expr= - 160*m.b113 + m.x646 - m.x678 >= -160)

m.c1421 = Constraint(expr= - 160*m.b121 + m.x648 - m.x686 >= -160)

m.c1422 = Constraint(expr= - 160*m.b122 + m.x649 - m.x687 >= -160)

m.c1423 = Constraint(expr= - 160*m.b118 + m.x651 - m.x683 >= -160)

m.c1424 = Constraint(expr= - 160*m.b119 + m.x652 - m.x684 >= -160)

m.c1425 = Constraint(expr=   m.x699 - m.x707 >= 0)

m.c1426 = Constraint(expr=   m.x700 - m.x708 >= 0)

m.c1427 = Constraint(expr=   m.x702 - m.x710 >= 0)

m.c1428 = Constraint(expr=   m.x703 - m.x711 >= 0)

m.c1429 = Constraint(expr=   m.x705 - m.x713 >= 0)

m.c1430 = Constraint(expr=   m.x706 - m.x714 >= 0)

m.c1431 = Constraint(expr= - 160*m.b97 - m.x626 + m.x704 >= -160)

m.c1432 = Constraint(expr= - 160*m.b98 - m.x627 + m.x705 >= -160)

m.c1433 = Constraint(expr= - 160*m.b99 - m.x628 + m.x706 >= -160)

m.c1434 = Constraint(expr= - 160*m.b100 - m.x629 + m.x698 >= -160)

m.c1435 = Constraint(expr= - 160*m.b101 - m.x630 + m.x699 >= -160)

m.c1436 = Constraint(expr= - 160*m.b102 - m.x631 + m.x700 >= -160)

m.c1437 = Constraint(expr= - 160*m.b103 - m.x632 + m.x701 >= -160)

m.c1438 = Constraint(expr= - 160*m.b104 - m.x633 + m.x702 >= -160)

m.c1439 = Constraint(expr= - 160*m.b105 - m.x634 + m.x703 >= -160)

m.c1440 = Constraint(expr= - 160*m.b106 - m.x635 + m.x698 >= -160)

m.c1441 = Constraint(expr= - 160*m.b107 - m.x636 + m.x699 >= -160)

m.c1442 = Constraint(expr= - 160*m.b108 - m.x637 + m.x700 >= -160)

m.c1443 = Constraint(expr= - 160*m.b109 - m.x638 + m.x701 >= -160)

m.c1444 = Constraint(expr= - 160*m.b110 - m.x639 + m.x702 >= -160)

m.c1445 = Constraint(expr= - 160*m.b111 - m.x640 + m.x703 >= -160)

m.c1446 = Constraint(expr= - 160*m.b112 - m.x641 + m.x698 >= -160)

m.c1447 = Constraint(expr= - 160*m.b113 - m.x642 + m.x699 >= -160)

m.c1448 = Constraint(expr= - 160*m.b114 - m.x643 + m.x700 >= -160)

m.c1449 = Constraint(expr= - 160*m.b115 - m.x644 + m.x701 >= -160)

m.c1450 = Constraint(expr= - 160*m.b116 - m.x645 + m.x702 >= -160)

m.c1451 = Constraint(expr= - 160*m.b117 - m.x646 + m.x703 >= -160)

m.c1452 = Constraint(expr= - 160*m.b118 - m.x647 + m.x698 >= -160)

m.c1453 = Constraint(expr= - 160*m.b119 - m.x648 + m.x699 >= -160)

m.c1454 = Constraint(expr= - 160*m.b120 - m.x649 + m.x700 >= -160)

m.c1455 = Constraint(expr= - 160*m.b121 - m.x650 + m.x701 >= -160)

m.c1456 = Constraint(expr= - 160*m.b122 - m.x651 + m.x702 >= -160)

m.c1457 = Constraint(expr= - 160*m.b123 - m.x652 + m.x703 >= -160)

m.c1458 = Constraint(expr= - 160*m.b124 - m.x653 + m.x704 >= -160)

m.c1459 = Constraint(expr= - 160*m.b125 - m.x654 + m.x705 >= -160)

m.c1460 = Constraint(expr= - 160*m.b126 - m.x655 + m.x706 >= -160)

m.c1461 = Constraint(expr= - 160*m.b127 - m.x656 + m.x704 >= -160)

m.c1462 = Constraint(expr= - 160*m.b128 - m.x657 + m.x705 >= -160)

m.c1463 = Constraint(expr= - 160*m.b129 - m.x658 + m.x706 >= -160)

m.c1464 = Constraint(expr= - 160*m.b130 - m.x659 + m.x704 >= -160)

m.c1465 = Constraint(expr= - 160*m.b131 - m.x660 + m.x705 >= -160)

m.c1466 = Constraint(expr= - 160*m.b132 - m.x661 + m.x706 >= -160)

m.c1467 = Constraint(expr=   160*m.b97 - m.x626 + m.x704 <= 160)

m.c1468 = Constraint(expr=   160*m.b98 - m.x627 + m.x705 <= 160)

m.c1469 = Constraint(expr=   160*m.b99 - m.x628 + m.x706 <= 160)

m.c1470 = Constraint(expr=   160*m.b100 - m.x629 + m.x698 <= 160)

m.c1471 = Constraint(expr=   160*m.b101 - m.x630 + m.x699 <= 160)

m.c1472 = Constraint(expr=   160*m.b102 - m.x631 + m.x700 <= 160)

m.c1473 = Constraint(expr=   160*m.b103 - m.x632 + m.x701 <= 160)

m.c1474 = Constraint(expr=   160*m.b104 - m.x633 + m.x702 <= 160)

m.c1475 = Constraint(expr=   160*m.b105 - m.x634 + m.x703 <= 160)

m.c1476 = Constraint(expr=   160*m.b106 - m.x635 + m.x698 <= 160)

m.c1477 = Constraint(expr=   160*m.b107 - m.x636 + m.x699 <= 160)

m.c1478 = Constraint(expr=   160*m.b108 - m.x637 + m.x700 <= 160)

m.c1479 = Constraint(expr=   160*m.b109 - m.x638 + m.x701 <= 160)

m.c1480 = Constraint(expr=   160*m.b110 - m.x639 + m.x702 <= 160)

m.c1481 = Constraint(expr=   160*m.b111 - m.x640 + m.x703 <= 160)

m.c1482 = Constraint(expr=   160*m.b112 - m.x641 + m.x698 <= 160)

m.c1483 = Constraint(expr=   160*m.b113 - m.x642 + m.x699 <= 160)

m.c1484 = Constraint(expr=   160*m.b114 - m.x643 + m.x700 <= 160)

m.c1485 = Constraint(expr=   160*m.b115 - m.x644 + m.x701 <= 160)

m.c1486 = Constraint(expr=   160*m.b116 - m.x645 + m.x702 <= 160)

m.c1487 = Constraint(expr=   160*m.b117 - m.x646 + m.x703 <= 160)

m.c1488 = Constraint(expr=   160*m.b118 - m.x647 + m.x698 <= 160)

m.c1489 = Constraint(expr=   160*m.b119 - m.x648 + m.x699 <= 160)

m.c1490 = Constraint(expr=   160*m.b120 - m.x649 + m.x700 <= 160)

m.c1491 = Constraint(expr=   160*m.b121 - m.x650 + m.x701 <= 160)

m.c1492 = Constraint(expr=   160*m.b122 - m.x651 + m.x702 <= 160)

m.c1493 = Constraint(expr=   160*m.b123 - m.x652 + m.x703 <= 160)

m.c1494 = Constraint(expr=   160*m.b124 - m.x653 + m.x704 <= 160)

m.c1495 = Constraint(expr=   160*m.b125 - m.x654 + m.x705 <= 160)

m.c1496 = Constraint(expr=   160*m.b126 - m.x655 + m.x706 <= 160)

m.c1497 = Constraint(expr=   160*m.b127 - m.x656 + m.x704 <= 160)

m.c1498 = Constraint(expr=   160*m.b128 - m.x657 + m.x705 <= 160)

m.c1499 = Constraint(expr=   160*m.b129 - m.x658 + m.x706 <= 160)

m.c1500 = Constraint(expr=   160*m.b130 - m.x659 + m.x704 <= 160)

m.c1501 = Constraint(expr=   160*m.b131 - m.x660 + m.x705 <= 160)

m.c1502 = Constraint(expr=   160*m.b132 - m.x661 + m.x706 <= 160)

m.c1503 = Constraint(expr= - 160*m.b97 - m.x662 + m.x713 >= -160)

m.c1504 = Constraint(expr= - 160*m.b98 - m.x663 + m.x714 >= -160)

m.c1505 = Constraint(expr= - 160*m.b99 - m.x664 + m.x715 >= -160)

m.c1506 = Constraint(expr= - 160*m.b100 - m.x665 + m.x707 >= -160)

m.c1507 = Constraint(expr= - 160*m.b101 - m.x666 + m.x708 >= -160)

m.c1508 = Constraint(expr= - 160*m.b102 - m.x667 + m.x709 >= -160)

m.c1509 = Constraint(expr= - 160*m.b103 - m.x668 + m.x710 >= -160)

m.c1510 = Constraint(expr= - 160*m.b104 - m.x669 + m.x711 >= -160)

m.c1511 = Constraint(expr= - 160*m.b105 - m.x670 + m.x712 >= -160)

m.c1512 = Constraint(expr= - 160*m.b106 - m.x671 + m.x707 >= -160)

m.c1513 = Constraint(expr= - 160*m.b107 - m.x672 + m.x708 >= -160)

m.c1514 = Constraint(expr= - 160*m.b108 - m.x673 + m.x709 >= -160)

m.c1515 = Constraint(expr= - 160*m.b109 - m.x674 + m.x710 >= -160)

m.c1516 = Constraint(expr= - 160*m.b110 - m.x675 + m.x711 >= -160)

m.c1517 = Constraint(expr= - 160*m.b111 - m.x676 + m.x712 >= -160)

m.c1518 = Constraint(expr= - 160*m.b112 - m.x677 + m.x707 >= -160)

m.c1519 = Constraint(expr= - 160*m.b113 - m.x678 + m.x708 >= -160)

m.c1520 = Constraint(expr= - 160*m.b114 - m.x679 + m.x709 >= -160)

m.c1521 = Constraint(expr= - 160*m.b115 - m.x680 + m.x710 >= -160)

m.c1522 = Constraint(expr= - 160*m.b116 - m.x681 + m.x711 >= -160)

m.c1523 = Constraint(expr= - 160*m.b117 - m.x682 + m.x712 >= -160)

m.c1524 = Constraint(expr= - 160*m.b118 - m.x683 + m.x707 >= -160)

m.c1525 = Constraint(expr= - 160*m.b119 - m.x684 + m.x708 >= -160)

m.c1526 = Constraint(expr= - 160*m.b120 - m.x685 + m.x709 >= -160)

m.c1527 = Constraint(expr= - 160*m.b121 - m.x686 + m.x710 >= -160)

m.c1528 = Constraint(expr= - 160*m.b122 - m.x687 + m.x711 >= -160)

m.c1529 = Constraint(expr= - 160*m.b123 - m.x688 + m.x712 >= -160)

m.c1530 = Constraint(expr= - 160*m.b124 - m.x689 + m.x713 >= -160)

m.c1531 = Constraint(expr= - 160*m.b125 - m.x690 + m.x714 >= -160)

m.c1532 = Constraint(expr= - 160*m.b126 - m.x691 + m.x715 >= -160)

m.c1533 = Constraint(expr= - 160*m.b127 - m.x692 + m.x713 >= -160)

m.c1534 = Constraint(expr= - 160*m.b128 - m.x693 + m.x714 >= -160)

m.c1535 = Constraint(expr= - 160*m.b129 - m.x694 + m.x715 >= -160)

m.c1536 = Constraint(expr= - 160*m.b130 - m.x695 + m.x713 >= -160)

m.c1537 = Constraint(expr= - 160*m.b131 - m.x696 + m.x714 >= -160)

m.c1538 = Constraint(expr= - 160*m.b132 - m.x697 + m.x715 >= -160)

m.c1539 = Constraint(expr=   160*m.b97 - m.x662 + m.x713 <= 160)

m.c1540 = Constraint(expr=   160*m.b98 - m.x663 + m.x714 <= 160)

m.c1541 = Constraint(expr=   160*m.b99 - m.x664 + m.x715 <= 160)

m.c1542 = Constraint(expr=   160*m.b100 - m.x665 + m.x707 <= 160)

m.c1543 = Constraint(expr=   160*m.b101 - m.x666 + m.x708 <= 160)

m.c1544 = Constraint(expr=   160*m.b102 - m.x667 + m.x709 <= 160)

m.c1545 = Constraint(expr=   160*m.b103 - m.x668 + m.x710 <= 160)

m.c1546 = Constraint(expr=   160*m.b104 - m.x669 + m.x711 <= 160)

m.c1547 = Constraint(expr=   160*m.b105 - m.x670 + m.x712 <= 160)

m.c1548 = Constraint(expr=   160*m.b106 - m.x671 + m.x707 <= 160)

m.c1549 = Constraint(expr=   160*m.b107 - m.x672 + m.x708 <= 160)

m.c1550 = Constraint(expr=   160*m.b108 - m.x673 + m.x709 <= 160)

m.c1551 = Constraint(expr=   160*m.b109 - m.x674 + m.x710 <= 160)

m.c1552 = Constraint(expr=   160*m.b110 - m.x675 + m.x711 <= 160)

m.c1553 = Constraint(expr=   160*m.b111 - m.x676 + m.x712 <= 160)

m.c1554 = Constraint(expr=   160*m.b112 - m.x677 + m.x707 <= 160)

m.c1555 = Constraint(expr=   160*m.b113 - m.x678 + m.x708 <= 160)

m.c1556 = Constraint(expr=   160*m.b114 - m.x679 + m.x709 <= 160)

m.c1557 = Constraint(expr=   160*m.b115 - m.x680 + m.x710 <= 160)

m.c1558 = Constraint(expr=   160*m.b116 - m.x681 + m.x711 <= 160)

m.c1559 = Constraint(expr=   160*m.b117 - m.x682 + m.x712 <= 160)

m.c1560 = Constraint(expr=   160*m.b118 - m.x683 + m.x707 <= 160)

m.c1561 = Constraint(expr=   160*m.b119 - m.x684 + m.x708 <= 160)

m.c1562 = Constraint(expr=   160*m.b120 - m.x685 + m.x709 <= 160)

m.c1563 = Constraint(expr=   160*m.b121 - m.x686 + m.x710 <= 160)

m.c1564 = Constraint(expr=   160*m.b122 - m.x687 + m.x711 <= 160)

m.c1565 = Constraint(expr=   160*m.b123 - m.x688 + m.x712 <= 160)

m.c1566 = Constraint(expr=   160*m.b124 - m.x689 + m.x713 <= 160)

m.c1567 = Constraint(expr=   160*m.b125 - m.x690 + m.x714 <= 160)

m.c1568 = Constraint(expr=   160*m.b126 - m.x691 + m.x715 <= 160)

m.c1569 = Constraint(expr=   160*m.b127 - m.x692 + m.x713 <= 160)

m.c1570 = Constraint(expr=   160*m.b128 - m.x693 + m.x714 <= 160)

m.c1571 = Constraint(expr=   160*m.b129 - m.x694 + m.x715 <= 160)

m.c1572 = Constraint(expr=   160*m.b130 - m.x695 + m.x713 <= 160)

m.c1573 = Constraint(expr=   160*m.b131 - m.x696 + m.x714 <= 160)

m.c1574 = Constraint(expr=   160*m.b132 - m.x697 + m.x715 <= 160)

m.c1575 = Constraint(expr=   m.x170 - m.x740 + m.x741 == 0)

m.c1576 = Constraint(expr=   m.x171 - m.x741 + m.x742 == 0)

m.c1577 = Constraint(expr=   m.x173 - m.x323 - m.x743 + m.x744 == 0)

m.c1578 = Constraint(expr=   m.x174 - m.x324 - m.x744 + m.x745 == 0)

m.c1579 = Constraint(expr=   m.x176 - m.x335 - m.x395 - m.x746 + m.x747 == 0)

m.c1580 = Constraint(expr=   m.x177 - m.x336 - m.x396 - m.x747 + m.x748 == 0)

m.c1581 = Constraint(expr=   m.x179 - m.x347 - m.x749 + m.x750 == 0)

m.c1582 = Constraint(expr=   m.x180 - m.x348 - m.x750 + m.x751 == 0)

m.c1583 = Constraint(expr=   m.x182 + m.x194 - m.x359 - m.x371 - m.x752 + m.x753 == 0)

m.c1584 = Constraint(expr=   m.x183 + m.x195 - m.x360 - m.x372 - m.x753 + m.x754 == 0)

m.c1585 = Constraint(expr=   m.x185 + m.x197 - m.x383 - m.x755 + m.x756 == 0)

m.c1586 = Constraint(expr=   m.x186 + m.x198 - m.x384 - m.x756 + m.x757 == 0)

m.c1587 = Constraint(expr=   m.x188 + m.x200 - m.x758 + m.x759 == 0)

m.c1588 = Constraint(expr=   m.x189 + m.x201 - m.x759 + m.x760 == 0)

m.c1589 = Constraint(expr=   m.x191 + m.x203 - m.x407 - m.x761 + m.x762 == 0)

m.c1590 = Constraint(expr=   m.x192 + m.x204 - m.x408 - m.x762 + m.x763 == 0)

m.c1591 = Constraint(expr=   m.x206 + m.x218 - m.x362 - m.x374 - m.x764 + m.x765 == 0)

m.c1592 = Constraint(expr=   m.x207 + m.x219 - m.x363 - m.x375 - m.x765 + m.x766 == 0)

m.c1593 = Constraint(expr=   m.x209 + m.x221 - m.x386 - m.x767 + m.x768 == 0)

m.c1594 = Constraint(expr=   m.x210 + m.x222 - m.x387 - m.x768 + m.x769 == 0)

m.c1595 = Constraint(expr=   m.x212 + m.x224 - m.x770 + m.x771 == 0)

m.c1596 = Constraint(expr=   m.x213 + m.x225 - m.x771 + m.x772 == 0)

m.c1597 = Constraint(expr=   m.x215 + m.x227 - m.x410 - m.x773 + m.x774 == 0)

m.c1598 = Constraint(expr=   m.x216 + m.x228 - m.x411 - m.x774 + m.x775 == 0)

m.c1599 = Constraint(expr=   m.x230 + m.x242 - m.x365 - m.x377 - m.x776 + m.x777 == 0)

m.c1600 = Constraint(expr=   m.x231 + m.x243 - m.x366 - m.x378 - m.x777 + m.x778 == 0)

m.c1601 = Constraint(expr=   m.x233 + m.x245 - m.x389 - m.x779 + m.x780 == 0)

m.c1602 = Constraint(expr=   m.x234 + m.x246 - m.x390 - m.x780 + m.x781 == 0)

m.c1603 = Constraint(expr=   m.x236 + m.x248 - m.x782 + m.x783 == 0)

m.c1604 = Constraint(expr=   m.x237 + m.x249 - m.x783 + m.x784 == 0)

m.c1605 = Constraint(expr=   m.x239 + m.x251 - m.x413 - m.x785 + m.x786 == 0)

m.c1606 = Constraint(expr=   m.x240 + m.x252 - m.x414 - m.x786 + m.x787 == 0)

m.c1607 = Constraint(expr=   m.x254 + m.x266 - m.x368 - m.x380 - m.x788 + m.x789 == 0)

m.c1608 = Constraint(expr=   m.x255 + m.x267 - m.x369 - m.x381 - m.x789 + m.x790 == 0)

m.c1609 = Constraint(expr=   m.x257 + m.x269 - m.x392 - m.x791 + m.x792 == 0)

m.c1610 = Constraint(expr=   m.x258 + m.x270 - m.x393 - m.x792 + m.x793 == 0)

m.c1611 = Constraint(expr=   m.x260 + m.x272 - m.x794 + m.x795 == 0)

m.c1612 = Constraint(expr=   m.x261 + m.x273 - m.x795 + m.x796 == 0)

m.c1613 = Constraint(expr=   m.x263 + m.x275 - m.x416 - m.x797 + m.x798 == 0)

m.c1614 = Constraint(expr=   m.x264 + m.x276 - m.x417 - m.x798 + m.x799 == 0)

m.c1615 = Constraint(expr=   m.x278 - m.x800 + m.x801 == 0)

m.c1616 = Constraint(expr=   m.x279 - m.x801 + m.x802 == 0)

m.c1617 = Constraint(expr=   m.x281 - m.x326 - m.x803 + m.x804 == 0)

m.c1618 = Constraint(expr=   m.x282 - m.x327 - m.x804 + m.x805 == 0)

m.c1619 = Constraint(expr=   m.x284 - m.x338 - m.x398 - m.x806 + m.x807 == 0)

m.c1620 = Constraint(expr=   m.x285 - m.x339 - m.x399 - m.x807 + m.x808 == 0)

m.c1621 = Constraint(expr=   m.x287 - m.x350 - m.x809 + m.x810 == 0)

m.c1622 = Constraint(expr=   m.x288 - m.x351 - m.x810 + m.x811 == 0)

m.c1623 = Constraint(expr=   m.x290 - m.x812 + m.x813 == 0)

m.c1624 = Constraint(expr=   m.x291 - m.x813 + m.x814 == 0)

m.c1625 = Constraint(expr=   m.x293 - m.x329 - m.x815 + m.x816 == 0)

m.c1626 = Constraint(expr=   m.x294 - m.x330 - m.x816 + m.x817 == 0)

m.c1627 = Constraint(expr=   m.x296 - m.x341 - m.x401 - m.x818 + m.x819 == 0)

m.c1628 = Constraint(expr=   m.x297 - m.x342 - m.x402 - m.x819 + m.x820 == 0)

m.c1629 = Constraint(expr=   m.x299 - m.x353 - m.x821 + m.x822 == 0)

m.c1630 = Constraint(expr=   m.x300 - m.x354 - m.x822 + m.x823 == 0)

m.c1631 = Constraint(expr=   m.x302 - m.x824 + m.x825 == 0)

m.c1632 = Constraint(expr=   m.x303 - m.x825 + m.x826 == 0)

m.c1633 = Constraint(expr=   m.x305 - m.x332 - m.x827 + m.x828 == 0)

m.c1634 = Constraint(expr=   m.x306 - m.x333 - m.x828 + m.x829 == 0)

m.c1635 = Constraint(expr=   m.x308 - m.x344 - m.x404 - m.x830 + m.x831 == 0)

m.c1636 = Constraint(expr=   m.x309 - m.x345 - m.x405 - m.x831 + m.x832 == 0)

m.c1637 = Constraint(expr=   m.x311 - m.x356 - m.x833 + m.x834 == 0)

m.c1638 = Constraint(expr=   m.x312 - m.x357 - m.x834 + m.x835 == 0)

m.c1639 = Constraint(expr=   m.x169 + m.x740 == 50)

m.c1640 = Constraint(expr=   m.x172 - m.x322 + m.x743 == 100)

m.c1641 = Constraint(expr=   m.x175 - m.x334 - m.x394 + m.x746 == 100)

m.c1642 = Constraint(expr=   m.x178 - m.x346 + m.x749 == 100)

m.c1643 = Constraint(expr=   m.x181 + m.x193 - m.x358 - m.x370 + m.x752 == 100)

m.c1644 = Constraint(expr=   m.x184 + m.x196 - m.x382 + m.x755 == 100)

m.c1645 = Constraint(expr=   m.x187 + m.x199 + m.x758 == 100)

m.c1646 = Constraint(expr=   m.x190 + m.x202 - m.x406 + m.x761 == 100)

m.c1647 = Constraint(expr=   m.x205 + m.x217 - m.x361 - m.x373 + m.x764 == 100)

m.c1648 = Constraint(expr=   m.x208 + m.x220 - m.x385 + m.x767 == 100)

m.c1649 = Constraint(expr=   m.x211 + m.x223 + m.x770 == 50)

m.c1650 = Constraint(expr=   m.x214 + m.x226 - m.x409 + m.x773 == 100)

m.c1651 = Constraint(expr=   m.x229 + m.x241 - m.x364 - m.x376 + m.x776 == 200)

m.c1652 = Constraint(expr=   m.x232 + m.x244 - m.x388 + m.x779 == 250)

m.c1653 = Constraint(expr=   m.x235 + m.x247 + m.x782 == 200)

m.c1654 = Constraint(expr=   m.x238 + m.x250 - m.x412 + m.x785 == 300)

m.c1655 = Constraint(expr=   m.x253 + m.x265 - m.x367 - m.x379 + m.x788 == 100)

m.c1656 = Constraint(expr=   m.x256 + m.x268 - m.x391 + m.x791 == 100)

m.c1657 = Constraint(expr=   m.x259 + m.x271 + m.x794 == 50)

m.c1658 = Constraint(expr=   m.x262 + m.x274 - m.x415 + m.x797 == 50)

m.c1659 = Constraint(expr=   m.x277 + m.x800 == 20)

m.c1660 = Constraint(expr=   m.x280 - m.x325 + m.x803 == 20)

m.c1661 = Constraint(expr=   m.x283 - m.x337 - m.x397 + m.x806 == 20)

m.c1662 = Constraint(expr=   m.x286 - m.x349 + m.x809 == 20)

m.c1663 = Constraint(expr=   m.x289 + m.x812 == 20)

m.c1664 = Constraint(expr=   m.x292 - m.x328 + m.x815 == 20)

m.c1665 = Constraint(expr=   m.x295 - m.x340 - m.x400 + m.x818 == 20)

m.c1666 = Constraint(expr=   m.x298 - m.x352 + m.x821 == 20)

m.c1667 = Constraint(expr=   m.x301 + m.x824 == 100)

m.c1668 = Constraint(expr=   m.x304 - m.x331 + m.x827 == 100)

m.c1669 = Constraint(expr=   m.x307 - m.x343 - m.x403 + m.x830 == 100)

m.c1670 = Constraint(expr=   m.x310 - m.x355 + m.x833 == 150)

m.c1671 = Constraint(expr= - m.x698 - m.x699 - m.x700 + m.x707 + m.x708 + m.x709 == 160)

m.c1672 = Constraint(expr= - m.x701 - m.x702 - m.x703 + m.x710 + m.x711 + m.x712 == 160)

m.c1673 = Constraint(expr= - m.x704 - m.x705 - m.x706 + m.x713 + m.x714 + m.x715 == 160)

m.c1674 = Constraint(expr= - m.b97 + m.b98 + m.x840 >= 0)

m.c1675 = Constraint(expr= - m.b98 + m.b99 + m.x841 >= 0)

m.c1676 = Constraint(expr= - m.b100 + m.b101 + m.x836 >= 0)

m.c1677 = Constraint(expr= - m.b101 + m.b102 + m.x837 >= 0)

m.c1678 = Constraint(expr= - m.b103 + m.b104 + m.x838 >= 0)

m.c1679 = Constraint(expr= - m.b104 + m.b105 + m.x839 >= 0)

m.c1680 = Constraint(expr= - m.b106 + m.b107 + m.x836 >= 0)

m.c1681 = Constraint(expr= - m.b107 + m.b108 + m.x837 >= 0)

m.c1682 = Constraint(expr= - m.b109 + m.b110 + m.x838 >= 0)

m.c1683 = Constraint(expr= - m.b110 + m.b111 + m.x839 >= 0)

m.c1684 = Constraint(expr= - m.b112 + m.b113 + m.x836 >= 0)

m.c1685 = Constraint(expr= - m.b113 + m.b114 + m.x837 >= 0)

m.c1686 = Constraint(expr= - m.b115 + m.b116 + m.x838 >= 0)

m.c1687 = Constraint(expr= - m.b116 + m.b117 + m.x839 >= 0)

m.c1688 = Constraint(expr= - m.b118 + m.b119 + m.x836 >= 0)

m.c1689 = Constraint(expr= - m.b119 + m.b120 + m.x837 >= 0)

m.c1690 = Constraint(expr= - m.b121 + m.b122 + m.x838 >= 0)

m.c1691 = Constraint(expr= - m.b122 + m.b123 + m.x839 >= 0)

m.c1692 = Constraint(expr= - m.b124 + m.b125 + m.x840 >= 0)

m.c1693 = Constraint(expr= - m.b125 + m.b126 + m.x841 >= 0)

m.c1694 = Constraint(expr= - m.b127 + m.b128 + m.x840 >= 0)

m.c1695 = Constraint(expr= - m.b128 + m.b129 + m.x841 >= 0)

m.c1696 = Constraint(expr= - m.b130 + m.b131 + m.x840 >= 0)

m.c1697 = Constraint(expr= - m.b131 + m.b132 + m.x841 >= 0)

m.c1698 = Constraint(expr=   m.b97 - m.b98 + m.x840 >= 0)

m.c1699 = Constraint(expr=   m.b98 - m.b99 + m.x841 >= 0)

m.c1700 = Constraint(expr=   m.b100 - m.b101 + m.x836 >= 0)

m.c1701 = Constraint(expr=   m.b101 - m.b102 + m.x837 >= 0)

m.c1702 = Constraint(expr=   m.b103 - m.b104 + m.x838 >= 0)

m.c1703 = Constraint(expr=   m.b104 - m.b105 + m.x839 >= 0)

m.c1704 = Constraint(expr=   m.b106 - m.b107 + m.x836 >= 0)

m.c1705 = Constraint(expr=   m.b107 - m.b108 + m.x837 >= 0)

m.c1706 = Constraint(expr=   m.b109 - m.b110 + m.x838 >= 0)

m.c1707 = Constraint(expr=   m.b110 - m.b111 + m.x839 >= 0)

m.c1708 = Constraint(expr=   m.b112 - m.b113 + m.x836 >= 0)

m.c1709 = Constraint(expr=   m.b113 - m.b114 + m.x837 >= 0)

m.c1710 = Constraint(expr=   m.b115 - m.b116 + m.x838 >= 0)

m.c1711 = Constraint(expr=   m.b116 - m.b117 + m.x839 >= 0)

m.c1712 = Constraint(expr=   m.b118 - m.b119 + m.x836 >= 0)

m.c1713 = Constraint(expr=   m.b119 - m.b120 + m.x837 >= 0)

m.c1714 = Constraint(expr=   m.b121 - m.b122 + m.x838 >= 0)

m.c1715 = Constraint(expr=   m.b122 - m.b123 + m.x839 >= 0)

m.c1716 = Constraint(expr=   m.b124 - m.b125 + m.x840 >= 0)

m.c1717 = Constraint(expr=   m.b125 - m.b126 + m.x841 >= 0)

m.c1718 = Constraint(expr=   m.b127 - m.b128 + m.x840 >= 0)

m.c1719 = Constraint(expr=   m.b128 - m.b129 + m.x841 >= 0)

m.c1720 = Constraint(expr=   m.b130 - m.b131 + m.x840 >= 0)

m.c1721 = Constraint(expr=   m.b131 - m.b132 + m.x841 >= 0)

m.c1722 = Constraint(expr=   0.25*m.x716 + 0.25*m.x717 + 0.25*m.x718 + 0.25*m.x719 + 0.25*m.x720 + 0.25*m.x721
                           + 0.25*m.x722 + 0.25*m.x723 + 0.25*m.x724 + 0.25*m.x725 + 0.25*m.x726 + 0.25*m.x727
                           + 0.25*m.x728 + 0.25*m.x729 + 0.25*m.x730 + 0.25*m.x731 + 0.25*m.x732 + 0.25*m.x733
                           + 0.25*m.x734 + 0.25*m.x735 + 0.25*m.x736 + 0.25*m.x737 + 0.25*m.x738 + 0.25*m.x739 + m.x938
                           >= 760)

m.c1723 = Constraint(expr= - 3.125*m.x429 + m.x939 >= -75)

m.c1724 = Constraint(expr= - 3.125*m.x433 + m.x940 >= -400)

m.c1726 = Constraint(expr=-m.x842*m.x134 + m.x170 == 0)

m.c1727 = Constraint(expr=-m.x843*m.x135 + m.x171 == 0)

m.c1728 = Constraint(expr=-m.x845*m.x134 + m.x173 == 0)

m.c1729 = Constraint(expr=-m.x846*m.x135 + m.x174 == 0)

m.c1730 = Constraint(expr=-m.x848*m.x134 + m.x176 == 0)

m.c1731 = Constraint(expr=-m.x849*m.x135 + m.x177 == 0)

m.c1732 = Constraint(expr=-m.x851*m.x134 + m.x179 == 0)

m.c1733 = Constraint(expr=-m.x852*m.x135 + m.x180 == 0)

m.c1734 = Constraint(expr=-m.x854*m.x137 + m.x182 == 0)

m.c1735 = Constraint(expr=-m.x855*m.x138 + m.x183 == 0)

m.c1736 = Constraint(expr=-m.x857*m.x137 + m.x185 == 0)

m.c1737 = Constraint(expr=-m.x858*m.x138 + m.x186 == 0)

m.c1738 = Constraint(expr=-m.x860*m.x137 + m.x188 == 0)

m.c1739 = Constraint(expr=-m.x861*m.x138 + m.x189 == 0)

m.c1740 = Constraint(expr=-m.x863*m.x137 + m.x191 == 0)

m.c1741 = Constraint(expr=-m.x864*m.x138 + m.x192 == 0)

m.c1742 = Constraint(expr=-m.x854*m.x140 + m.x194 == 0)

m.c1743 = Constraint(expr=-m.x855*m.x141 + m.x195 == 0)

m.c1744 = Constraint(expr=-m.x857*m.x140 + m.x197 == 0)

m.c1745 = Constraint(expr=-m.x858*m.x141 + m.x198 == 0)

m.c1746 = Constraint(expr=-m.x860*m.x140 + m.x200 == 0)

m.c1747 = Constraint(expr=-m.x861*m.x141 + m.x201 == 0)

m.c1748 = Constraint(expr=-m.x863*m.x140 + m.x203 == 0)

m.c1749 = Constraint(expr=-m.x864*m.x141 + m.x204 == 0)

m.c1750 = Constraint(expr=-m.x866*m.x143 + m.x206 == 0)

m.c1751 = Constraint(expr=-m.x867*m.x144 + m.x207 == 0)

m.c1752 = Constraint(expr=-m.x869*m.x143 + m.x209 == 0)

m.c1753 = Constraint(expr=-m.x870*m.x144 + m.x210 == 0)

m.c1754 = Constraint(expr=-m.x872*m.x143 + m.x212 == 0)

m.c1755 = Constraint(expr=-m.x873*m.x144 + m.x213 == 0)

m.c1756 = Constraint(expr=-m.x875*m.x143 + m.x215 == 0)

m.c1757 = Constraint(expr=-m.x876*m.x144 + m.x216 == 0)

m.c1758 = Constraint(expr=-m.x866*m.x146 + m.x218 == 0)

m.c1759 = Constraint(expr=-m.x867*m.x147 + m.x219 == 0)

m.c1760 = Constraint(expr=-m.x869*m.x146 + m.x221 == 0)

m.c1761 = Constraint(expr=-m.x870*m.x147 + m.x222 == 0)

m.c1762 = Constraint(expr=-m.x872*m.x146 + m.x224 == 0)

m.c1763 = Constraint(expr=-m.x873*m.x147 + m.x225 == 0)

m.c1764 = Constraint(expr=-m.x875*m.x146 + m.x227 == 0)

m.c1765 = Constraint(expr=-m.x876*m.x147 + m.x228 == 0)

m.c1766 = Constraint(expr=-m.x878*m.x149 + m.x230 == 0)

m.c1767 = Constraint(expr=-m.x879*m.x150 + m.x231 == 0)

m.c1768 = Constraint(expr=-m.x881*m.x149 + m.x233 == 0)

m.c1769 = Constraint(expr=-m.x882*m.x150 + m.x234 == 0)

m.c1770 = Constraint(expr=-m.x884*m.x149 + m.x236 == 0)

m.c1771 = Constraint(expr=-m.x885*m.x150 + m.x237 == 0)

m.c1772 = Constraint(expr=-m.x887*m.x149 + m.x239 == 0)

m.c1773 = Constraint(expr=-m.x888*m.x150 + m.x240 == 0)

m.c1774 = Constraint(expr=-m.x878*m.x152 + m.x242 == 0)

m.c1775 = Constraint(expr=-m.x879*m.x153 + m.x243 == 0)

m.c1776 = Constraint(expr=-m.x881*m.x152 + m.x245 == 0)

m.c1777 = Constraint(expr=-m.x882*m.x153 + m.x246 == 0)

m.c1778 = Constraint(expr=-m.x884*m.x152 + m.x248 == 0)

m.c1779 = Constraint(expr=-m.x885*m.x153 + m.x249 == 0)

m.c1780 = Constraint(expr=-m.x887*m.x152 + m.x251 == 0)

m.c1781 = Constraint(expr=-m.x888*m.x153 + m.x252 == 0)

m.c1782 = Constraint(expr=-m.x890*m.x155 + m.x254 == 0)

m.c1783 = Constraint(expr=-m.x891*m.x156 + m.x255 == 0)

m.c1784 = Constraint(expr=-m.x893*m.x155 + m.x257 == 0)

m.c1785 = Constraint(expr=-m.x894*m.x156 + m.x258 == 0)

m.c1786 = Constraint(expr=-m.x896*m.x155 + m.x260 == 0)

m.c1787 = Constraint(expr=-m.x897*m.x156 + m.x261 == 0)

m.c1788 = Constraint(expr=-m.x899*m.x155 + m.x263 == 0)

m.c1789 = Constraint(expr=-m.x900*m.x156 + m.x264 == 0)

m.c1790 = Constraint(expr=-m.x890*m.x158 + m.x266 == 0)

m.c1791 = Constraint(expr=-m.x891*m.x159 + m.x267 == 0)

m.c1792 = Constraint(expr=-m.x893*m.x158 + m.x269 == 0)

m.c1793 = Constraint(expr=-m.x894*m.x159 + m.x270 == 0)

m.c1794 = Constraint(expr=-m.x896*m.x158 + m.x272 == 0)

m.c1795 = Constraint(expr=-m.x897*m.x159 + m.x273 == 0)

m.c1796 = Constraint(expr=-m.x899*m.x158 + m.x275 == 0)

m.c1797 = Constraint(expr=-m.x900*m.x159 + m.x276 == 0)

m.c1798 = Constraint(expr=-m.x902*m.x161 + m.x278 == 0)

m.c1799 = Constraint(expr=-m.x903*m.x162 + m.x279 == 0)

m.c1800 = Constraint(expr=-m.x905*m.x161 + m.x281 == 0)

m.c1801 = Constraint(expr=-m.x906*m.x162 + m.x282 == 0)

m.c1802 = Constraint(expr=-m.x908*m.x161 + m.x284 == 0)

m.c1803 = Constraint(expr=-m.x909*m.x162 + m.x285 == 0)

m.c1804 = Constraint(expr=-m.x911*m.x161 + m.x287 == 0)

m.c1805 = Constraint(expr=-m.x912*m.x162 + m.x288 == 0)

m.c1806 = Constraint(expr=-m.x914*m.x164 + m.x290 == 0)

m.c1807 = Constraint(expr=-m.x915*m.x165 + m.x291 == 0)

m.c1808 = Constraint(expr=-m.x917*m.x164 + m.x293 == 0)

m.c1809 = Constraint(expr=-m.x918*m.x165 + m.x294 == 0)

m.c1810 = Constraint(expr=-m.x920*m.x164 + m.x296 == 0)

m.c1811 = Constraint(expr=-m.x921*m.x165 + m.x297 == 0)

m.c1812 = Constraint(expr=-m.x923*m.x164 + m.x299 == 0)

m.c1813 = Constraint(expr=-m.x924*m.x165 + m.x300 == 0)

m.c1814 = Constraint(expr=-m.x926*m.x167 + m.x302 == 0)

m.c1815 = Constraint(expr=-m.x927*m.x168 + m.x303 == 0)

m.c1816 = Constraint(expr=-m.x929*m.x167 + m.x305 == 0)

m.c1817 = Constraint(expr=-m.x930*m.x168 + m.x306 == 0)

m.c1818 = Constraint(expr=-m.x932*m.x167 + m.x308 == 0)

m.c1819 = Constraint(expr=-m.x933*m.x168 + m.x309 == 0)

m.c1820 = Constraint(expr=-m.x935*m.x167 + m.x311 == 0)

m.c1821 = Constraint(expr=-m.x936*m.x168 + m.x312 == 0)

m.c1822 = Constraint(expr=-m.x842*m.x716 + m.x740 == 0)

m.c1823 = Constraint(expr=-m.x843*m.x717 + m.x741 == 0)

m.c1824 = Constraint(expr=-m.x844*m.x718 + m.x742 == 0)

m.c1825 = Constraint(expr=-m.x845*m.x716 + m.x743 == 0)

m.c1826 = Constraint(expr=-m.x846*m.x717 + m.x744 == 0)

m.c1827 = Constraint(expr=-m.x847*m.x718 + m.x745 == 0)

m.c1828 = Constraint(expr=-m.x848*m.x716 + m.x746 == 0)

m.c1829 = Constraint(expr=-m.x849*m.x717 + m.x747 == 0)

m.c1830 = Constraint(expr=-m.x850*m.x718 + m.x748 == 0)

m.c1831 = Constraint(expr=-m.x851*m.x716 + m.x749 == 0)

m.c1832 = Constraint(expr=-m.x852*m.x717 + m.x750 == 0)

m.c1833 = Constraint(expr=-m.x853*m.x718 + m.x751 == 0)

m.c1834 = Constraint(expr=-m.x854*m.x719 + m.x752 == 0)

m.c1835 = Constraint(expr=-m.x855*m.x720 + m.x753 == 0)

m.c1836 = Constraint(expr=-m.x856*m.x721 + m.x754 == 0)

m.c1837 = Constraint(expr=-m.x857*m.x719 + m.x755 == 0)

m.c1838 = Constraint(expr=-m.x858*m.x720 + m.x756 == 0)

m.c1839 = Constraint(expr=-m.x859*m.x721 + m.x757 == 0)

m.c1840 = Constraint(expr=-m.x860*m.x719 + m.x758 == 0)

m.c1841 = Constraint(expr=-m.x861*m.x720 + m.x759 == 0)

m.c1842 = Constraint(expr=-m.x862*m.x721 + m.x760 == 0)

m.c1843 = Constraint(expr=-m.x863*m.x719 + m.x761 == 0)

m.c1844 = Constraint(expr=-m.x864*m.x720 + m.x762 == 0)

m.c1845 = Constraint(expr=-m.x865*m.x721 + m.x763 == 0)

m.c1846 = Constraint(expr=-m.x866*m.x722 + m.x764 == 0)

m.c1847 = Constraint(expr=-m.x867*m.x723 + m.x765 == 0)

m.c1848 = Constraint(expr=-m.x868*m.x724 + m.x766 == 0)

m.c1849 = Constraint(expr=-m.x869*m.x722 + m.x767 == 0)

m.c1850 = Constraint(expr=-m.x870*m.x723 + m.x768 == 0)

m.c1851 = Constraint(expr=-m.x871*m.x724 + m.x769 == 0)

m.c1852 = Constraint(expr=-m.x872*m.x722 + m.x770 == 0)

m.c1853 = Constraint(expr=-m.x873*m.x723 + m.x771 == 0)

m.c1854 = Constraint(expr=-m.x874*m.x724 + m.x772 == 0)

m.c1855 = Constraint(expr=-m.x875*m.x722 + m.x773 == 0)

m.c1856 = Constraint(expr=-m.x876*m.x723 + m.x774 == 0)

m.c1857 = Constraint(expr=-m.x877*m.x724 + m.x775 == 0)

m.c1858 = Constraint(expr=-m.x878*m.x725 + m.x776 == 0)

m.c1859 = Constraint(expr=-m.x879*m.x726 + m.x777 == 0)

m.c1860 = Constraint(expr=-m.x880*m.x727 + m.x778 == 0)

m.c1861 = Constraint(expr=-m.x881*m.x725 + m.x779 == 0)

m.c1862 = Constraint(expr=-m.x882*m.x726 + m.x780 == 0)

m.c1863 = Constraint(expr=-m.x883*m.x727 + m.x781 == 0)

m.c1864 = Constraint(expr=-m.x884*m.x725 + m.x782 == 0)

m.c1865 = Constraint(expr=-m.x885*m.x726 + m.x783 == 0)

m.c1866 = Constraint(expr=-m.x886*m.x727 + m.x784 == 0)

m.c1867 = Constraint(expr=-m.x887*m.x725 + m.x785 == 0)

m.c1868 = Constraint(expr=-m.x888*m.x726 + m.x786 == 0)

m.c1869 = Constraint(expr=-m.x889*m.x727 + m.x787 == 0)

m.c1870 = Constraint(expr=-m.x890*m.x728 + m.x788 == 0)

m.c1871 = Constraint(expr=-m.x891*m.x729 + m.x789 == 0)

m.c1872 = Constraint(expr=-m.x892*m.x730 + m.x790 == 0)

m.c1873 = Constraint(expr=-m.x893*m.x728 + m.x791 == 0)

m.c1874 = Constraint(expr=-m.x894*m.x729 + m.x792 == 0)

m.c1875 = Constraint(expr=-m.x895*m.x730 + m.x793 == 0)

m.c1876 = Constraint(expr=-m.x896*m.x728 + m.x794 == 0)

m.c1877 = Constraint(expr=-m.x897*m.x729 + m.x795 == 0)

m.c1878 = Constraint(expr=-m.x898*m.x730 + m.x796 == 0)

m.c1879 = Constraint(expr=-m.x899*m.x728 + m.x797 == 0)

m.c1880 = Constraint(expr=-m.x900*m.x729 + m.x798 == 0)

m.c1881 = Constraint(expr=-m.x901*m.x730 + m.x799 == 0)

m.c1882 = Constraint(expr=-m.x902*m.x731 + m.x800 == 0)

m.c1883 = Constraint(expr=-m.x903*m.x732 + m.x801 == 0)

m.c1884 = Constraint(expr=-m.x904*m.x733 + m.x802 == 0)

m.c1885 = Constraint(expr=-m.x905*m.x731 + m.x803 == 0)

m.c1886 = Constraint(expr=-m.x906*m.x732 + m.x804 == 0)

m.c1887 = Constraint(expr=-m.x907*m.x733 + m.x805 == 0)

m.c1888 = Constraint(expr=-m.x908*m.x731 + m.x806 == 0)

m.c1889 = Constraint(expr=-m.x909*m.x732 + m.x807 == 0)

m.c1890 = Constraint(expr=-m.x910*m.x733 + m.x808 == 0)

m.c1891 = Constraint(expr=-m.x911*m.x731 + m.x809 == 0)

m.c1892 = Constraint(expr=-m.x912*m.x732 + m.x810 == 0)

m.c1893 = Constraint(expr=-m.x913*m.x733 + m.x811 == 0)

m.c1894 = Constraint(expr=-m.x914*m.x734 + m.x812 == 0)

m.c1895 = Constraint(expr=-m.x915*m.x735 + m.x813 == 0)

m.c1896 = Constraint(expr=-m.x916*m.x736 + m.x814 == 0)

m.c1897 = Constraint(expr=-m.x917*m.x734 + m.x815 == 0)

m.c1898 = Constraint(expr=-m.x918*m.x735 + m.x816 == 0)

m.c1899 = Constraint(expr=-m.x919*m.x736 + m.x817 == 0)

m.c1900 = Constraint(expr=-m.x920*m.x734 + m.x818 == 0)

m.c1901 = Constraint(expr=-m.x921*m.x735 + m.x819 == 0)

m.c1902 = Constraint(expr=-m.x922*m.x736 + m.x820 == 0)

m.c1903 = Constraint(expr=-m.x923*m.x734 + m.x821 == 0)

m.c1904 = Constraint(expr=-m.x924*m.x735 + m.x822 == 0)

m.c1905 = Constraint(expr=-m.x925*m.x736 + m.x823 == 0)

m.c1906 = Constraint(expr=-m.x926*m.x737 + m.x824 == 0)

m.c1907 = Constraint(expr=-m.x927*m.x738 + m.x825 == 0)

m.c1908 = Constraint(expr=-m.x928*m.x739 + m.x826 == 0)

m.c1909 = Constraint(expr=-m.x929*m.x737 + m.x827 == 0)

m.c1910 = Constraint(expr=-m.x930*m.x738 + m.x828 == 0)

m.c1911 = Constraint(expr=-m.x931*m.x739 + m.x829 == 0)

m.c1912 = Constraint(expr=-m.x932*m.x737 + m.x830 == 0)

m.c1913 = Constraint(expr=-m.x933*m.x738 + m.x831 == 0)

m.c1914 = Constraint(expr=-m.x934*m.x739 + m.x832 == 0)

m.c1915 = Constraint(expr=-m.x935*m.x737 + m.x833 == 0)

m.c1916 = Constraint(expr=-m.x936*m.x738 + m.x834 == 0)

m.c1917 = Constraint(expr=-m.x937*m.x739 + m.x835 == 0)
