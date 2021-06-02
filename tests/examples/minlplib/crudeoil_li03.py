#  MINLP written by GAMS Convert at 04/21/18 13:51:21
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       2443      428      936     1079        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        965      833      132        0        0        0        0        0
#  FX     32       16       16        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       8169     7785      384        0
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
m.x157 = Var(within=Reals,bounds=(0,290),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,340),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,340),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,290),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,290),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,840),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,870),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,870),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,840),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,870),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,870),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,870),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,870),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,870),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,870),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,830),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,920),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,390),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,510),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,510),initialize=0)
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
m.x346 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x347 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x348 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x349 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x350 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x351 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x352 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x353 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x354 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x355 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x356 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x357 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x358 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x359 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x360 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x361 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x362 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x363 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x364 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x365 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x366 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x367 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x368 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x369 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x370 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x371 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x372 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x373 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x374 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x375 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x376 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x377 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x378 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x379 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x380 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x381 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x382 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x383 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x384 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x385 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x386 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x387 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x388 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x389 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x390 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x391 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x392 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x393 = Var(within=Reals,bounds=(0,190),initialize=0)
m.x394 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x395 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x396 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x397 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x398 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x399 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x400 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x401 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x402 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x403 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x404 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x405 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x406 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x407 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x408 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x409 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x410 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x411 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x412 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x413 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x414 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x415 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x416 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x417 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x418 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x419 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x420 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x421 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x422 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x423 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x424 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x425 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x426 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x427 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x428 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x429 = Var(within=Reals,bounds=(0,250),initialize=0)
m.x430 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x431 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x432 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x433 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x434 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x435 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x436 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x437 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x438 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x439 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x440 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x441 = Var(within=Reals,bounds=(0,240),initialize=0)
m.x442 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x443 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x444 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x445 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x446 = Var(within=Reals,bounds=(104,160),initialize=104)
m.x447 = Var(within=Reals,bounds=(104,160),initialize=104)
m.x448 = Var(within=Reals,bounds=(104,160),initialize=104)
m.x449 = Var(within=Reals,bounds=(104,160),initialize=104)
m.x450 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x451 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x452 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x453 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x454 = Var(within=Reals,bounds=(104,160),initialize=104)
m.x455 = Var(within=Reals,bounds=(104,160),initialize=104)
m.x456 = Var(within=Reals,bounds=(104,160),initialize=104)
m.x457 = Var(within=Reals,bounds=(104,160),initialize=104)
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
m.x716 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x717 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x718 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x719 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x720 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x721 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x722 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x723 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x724 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x725 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x726 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x727 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x728 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x729 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x730 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x731 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x732 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x733 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x734 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x735 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x736 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x737 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x738 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x739 = Var(within=Reals,bounds=(0,160),initialize=0)
m.x740 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x741 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x742 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x743 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x744 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x745 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x746 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x747 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x748 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x749 = Var(within=Reals,bounds=(110,980),initialize=110)
m.x750 = Var(within=Reals,bounds=(110,980),initialize=110)
m.x751 = Var(within=Reals,bounds=(110,980),initialize=110)
m.x752 = Var(within=Reals,bounds=(110,980),initialize=110)
m.x753 = Var(within=Reals,bounds=(110,980),initialize=110)
m.x754 = Var(within=Reals,bounds=(110,980),initialize=110)
m.x755 = Var(within=Reals,bounds=(60,890),initialize=60)
m.x756 = Var(within=Reals,bounds=(60,980),initialize=60)
m.x757 = Var(within=Reals,bounds=(60,980),initialize=60)
m.x758 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x759 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x760 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x761 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x762 = Var(within=Reals,bounds=(60,570),initialize=60)
m.x763 = Var(within=Reals,bounds=(60,570),initialize=60)
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
m.x836 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x837 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x838 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x839 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x840 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x841 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x842 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x843 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x844 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x845 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x846 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x847 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x848 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x849 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x850 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x851 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x852 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x853 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x854 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x855 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x856 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x857 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x858 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x859 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x860 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x861 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x862 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x863 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x864 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x865 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x866 = Var(within=Reals,bounds=(0.087719298245614,0.142857142857143),initialize=0.087719298245614)
m.x867 = Var(within=Reals,bounds=(0.00923361034164358,0.142857142857143),initialize=0.00923361034164358)
m.x868 = Var(within=Reals,bounds=(0.000971958983330903,0.142857142857143),initialize=0.000971958983330903)
m.x869 = Var(within=Reals,bounds=(0.175438596491228,0.305555555555556),initialize=0.175438596491228)
m.x870 = Var(within=Reals,bounds=(0.0184672206832872,0.387755102040816),initialize=0.0184672206832872)
m.x871 = Var(within=Reals,bounds=(0.00194391796666181,0.387755102040816),initialize=0.00194391796666181)
m.x872 = Var(within=Reals,bounds=(0.175438596491228,0.56140350877193),initialize=0.175438596491228)
m.x873 = Var(within=Reals,bounds=(0.0184672206832872,0.953007518796993),initialize=0.0184672206832872)
m.x874 = Var(within=Reals,bounds=(0.00194391796666181,0.973242158465884),initialize=0.00194391796666181)
m.x875 = Var(within=Reals,bounds=(0.175438596491228,0.56140350877193),initialize=0.175438596491228)
m.x876 = Var(within=Reals,bounds=(0.0184672206832872,0.880952380952381),initialize=0.0184672206832872)
m.x877 = Var(within=Reals,bounds=(0.00194391796666181,0.880952380952381),initialize=0.00194391796666181)
m.x878 = Var(within=Reals,bounds=(0.175438596491228,0.473684210526316),initialize=0.175438596491228)
m.x879 = Var(within=Reals,bounds=(0.0184672206832872,0.845714285714286),initialize=0.0184672206832872)
m.x880 = Var(within=Reals,bounds=(0.00194391796666181,0.845714285714286),initialize=0.00194391796666181)
m.x881 = Var(within=Reals,bounds=(0.175438596491228,0.473684210526316),initialize=0.175438596491228)
m.x882 = Var(within=Reals,bounds=(0.0184672206832872,0.854838709677419),initialize=0.0184672206832872)
m.x883 = Var(within=Reals,bounds=(0.00194391796666181,0.854838709677419),initialize=0.00194391796666181)
m.x884 = Var(within=Reals,bounds=(0.175438596491228,0.25),initialize=0.175438596491228)
m.x885 = Var(within=Reals,bounds=(0.0184672206832872,0.25),initialize=0.0184672206832872)
m.x886 = Var(within=Reals,bounds=(0.00194391796666181,0.25),initialize=0.00194391796666181)
m.x887 = Var(within=Reals,bounds=(0.175438596491228,0.473684210526316),initialize=0.175438596491228)
m.x888 = Var(within=Reals,bounds=(0.0184672206832872,0.85),initialize=0.0184672206832872)
m.x889 = Var(within=Reals,bounds=(0.00194391796666181,0.85),initialize=0.00194391796666181)
m.x890 = Var(within=Reals,bounds=(0.175438596491228,0.545454545454545),initialize=0.175438596491228)
m.x891 = Var(within=Reals,bounds=(0.0184672206832872,0.853061224489796),initialize=0.0184672206832872)
m.x892 = Var(within=Reals,bounds=(0.00194391796666181,0.853061224489796),initialize=0.00194391796666181)
m.x893 = Var(within=Reals,bounds=(0.175438596491228,0.56140350877193),initialize=0.175438596491228)
m.x894 = Var(within=Reals,bounds=(0.0184672206832872,0.861751152073733),initialize=0.0184672206832872)
m.x895 = Var(within=Reals,bounds=(0.00194391796666181,0.861751152073733),initialize=0.00194391796666181)
m.x896 = Var(within=Reals,bounds=(0.087719298245614,0.142857142857143),initialize=0.087719298245614)
m.x897 = Var(within=Reals,bounds=(0.00923361034164358,0.142857142857143),initialize=0.00923361034164358)
m.x898 = Var(within=Reals,bounds=(0.000971958983330903,0.142857142857143),initialize=0.000971958983330903)
m.x899 = Var(within=Reals,bounds=(0.175438596491228,0.56140350877193),initialize=0.175438596491228)
m.x900 = Var(within=Reals,bounds=(0.0184672206832872,0.857142857142857),initialize=0.0184672206832872)
m.x901 = Var(within=Reals,bounds=(0.00194391796666181,0.857142857142857),initialize=0.00194391796666181)
m.x902 = Var(within=Reals,bounds=(0.204081632653061,0.23469387755102),initialize=0.204081632653061)
m.x903 = Var(within=Reals,bounds=(0.0229071220324865,0.728439763001975),initialize=0.0229071220324865)
m.x904 = Var(within=Reals,bounds=(0.00257120757507501,0.734649122807018),initialize=0.00257120757507501)
m.x905 = Var(within=Reals,bounds=(0.255102040816327,0.285714285714286),initialize=0.255102040816327)
m.x906 = Var(within=Reals,bounds=(0.0286339025406081,0.774853801169591),initialize=0.0286339025406081)
m.x907 = Var(within=Reals,bounds=(0.00321400946884376,0.774853801169591),initialize=0.00321400946884376)
m.x908 = Var(within=Reals,bounds=(0.204081632653061,0.210526315789474),initialize=0.204081632653061)
m.x909 = Var(within=Reals,bounds=(0.0229071220324865,0.210526315789474),initialize=0.0229071220324865)
m.x910 = Var(within=Reals,bounds=(0.00257120757507501,0.210526315789474),initialize=0.00257120757507501)
m.x911 = Var(within=Reals,bounds=(0.306122448979592,0.336734693877551),initialize=0.306122448979592)
m.x912 = Var(within=Reals,bounds=(0.0343606830487297,0.784962406015038),initialize=0.0343606830487297)
m.x913 = Var(within=Reals,bounds=(0.00385681136261252,0.784962406015038),initialize=0.00385681136261252)
m.x914 = Var(within=Reals,bounds=(0.126582278481013,0.6),initialize=0.126582278481013)
m.x915 = Var(within=Reals,bounds=(0.0142082149315422,0.775925925925926),initialize=0.0142082149315422)
m.x916 = Var(within=Reals,bounds=(0.00159479963517311,0.775925925925926),initialize=0.00159479963517311)
m.x917 = Var(within=Reals,bounds=(0.135135135135135,0.636363636363636),initialize=0.135135135135135)
m.x918 = Var(within=Reals,bounds=(0.0151682294539437,0.796296296296296),initialize=0.0151682294539437)
m.x919 = Var(within=Reals,bounds=(0.0017025563672794,0.796296296296296),initialize=0.0017025563672794)
m.x920 = Var(within=Reals,bounds=(0.0510204081632653,0.166666666666667),initialize=0.0510204081632653)
m.x921 = Var(within=Reals,bounds=(0.00572678050812162,0.166666666666667),initialize=0.00572678050812162)
m.x922 = Var(within=Reals,bounds=(0.000642801893768753,0.166666666666667),initialize=0.000642801893768753)
m.x923 = Var(within=Reals,bounds=(0.0666666666666667,0.537037037037037),initialize=0.0666666666666667)
m.x924 = Var(within=Reals,bounds=(0.00748299319727891,0.738095238095238),initialize=0.00748299319727891)
m.x925 = Var(within=Reals,bounds=(0.000839927807857837,0.738095238095238),initialize=0.000839927807857837)
m.x926 = Var(within=Reals,bounds=(0.0224719101123595,0.25),initialize=0.0224719101123595)
m.x927 = Var(within=Reals,bounds=(0.00137583123136895,0.25),initialize=0.00137583123136895)
m.x928 = Var(within=Reals,bounds=(8.42345651858542E-5,0.25),initialize=8.42345651858542E-5)
m.x929 = Var(within=Reals,bounds=(0.0227272727272727,0.333333333333333),initialize=0.0227272727272727)
m.x930 = Var(within=Reals,bounds=(0.00139146567717996,0.357142857142857),initialize=0.00139146567717996)
m.x931 = Var(within=Reals,bounds=(8.51917761538753E-5,0.357142857142857),initialize=8.51917761538753E-5)
m.x932 = Var(within=Reals,bounds=(0.0512820512820513,0.896551724137931),initialize=0.0512820512820513)
m.x933 = Var(within=Reals,bounds=(0.00313971742543171,0.971904266389178),initialize=0.00313971742543171)
m.x934 = Var(within=Reals,bounds=(0.000192227597475411,0.971904266389178),initialize=0.000192227597475411)
m.x935 = Var(within=Reals,bounds=(0.0338983050847458,0.842105263157895),initialize=0.0338983050847458)
m.x936 = Var(within=Reals,bounds=(0.00207540643375994,0.875),initialize=0.00207540643375994)
m.x937 = Var(within=Reals,bounds=(0.000127065700026119,0.875),initialize=0.000127065700026119)
m.x938 = Var(within=Reals,bounds=(0.0350877192982456,0.25),initialize=0.0350877192982456)
m.x939 = Var(within=Reals,bounds=(0.00369344413665743,0.25),initialize=0.00369344413665743)
m.x940 = Var(within=Reals,bounds=(0.000388783593332361,0.25),initialize=0.000388783593332361)
m.x941 = Var(within=Reals,bounds=(0.0350877192982456,0.333333333333333),initialize=0.0350877192982456)
m.x942 = Var(within=Reals,bounds=(0.00369344413665743,0.357142857142857),initialize=0.00369344413665743)
m.x943 = Var(within=Reals,bounds=(0.000388783593332361,0.357142857142857),initialize=0.000388783593332361)
m.x944 = Var(within=Reals,bounds=(0.0512820512820513,0.894736842105263),initialize=0.0512820512820513)
m.x945 = Var(within=Reals,bounds=(0.00539811066126856,0.971904266389178),initialize=0.00539811066126856)
m.x946 = Var(within=Reals,bounds=(0.000568222174870374,0.971904266389178),initialize=0.000568222174870374)
m.x947 = Var(within=Reals,bounds=(0.0350877192982456,0.842105263157895),initialize=0.0350877192982456)
m.x948 = Var(within=Reals,bounds=(0.00369344413665743,0.875),initialize=0.00369344413665743)
m.x949 = Var(within=Reals,bounds=(0.000388783593332361,0.875),initialize=0.000388783593332361)
m.x950 = Var(within=Reals,bounds=(0.175438596491228,0.222222222222222),initialize=0.175438596491228)
m.x951 = Var(within=Reals,bounds=(0.0184672206832872,0.222222222222222),initialize=0.0184672206832872)
m.x952 = Var(within=Reals,bounds=(0.00194391796666181,0.222222222222222),initialize=0.00194391796666181)
m.x953 = Var(within=Reals,bounds=(0.175438596491228,0.239130434782609),initialize=0.175438596491228)
m.x954 = Var(within=Reals,bounds=(0.0184672206832872,0.333333333333333),initialize=0.0184672206832872)
m.x955 = Var(within=Reals,bounds=(0.00194391796666181,0.333333333333333),initialize=0.00194391796666181)
m.x956 = Var(within=Reals,bounds=(0.175438596491228,0.385964912280702),initialize=0.175438596491228)
m.x957 = Var(within=Reals,bounds=(0.0184672206832872,0.934210526315789),initialize=0.0184672206832872)
m.x958 = Var(within=Reals,bounds=(0.00194391796666181,0.970863683662851),initialize=0.00194391796666181)
m.x959 = Var(within=Reals,bounds=(0.263157894736842,0.473684210526316),initialize=0.263157894736842)
m.x960 = Var(within=Reals,bounds=(0.0277008310249307,0.888888888888889),initialize=0.0277008310249307)
m.x961 = Var(within=Reals,bounds=(0.00291587694999271,0.888888888888889),initialize=0.00291587694999271)
m.x962 = Var(within=Reals,bounds=(0,1500),initialize=0)
m.x963 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x964 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   1.5*m.x193 + 1.5*m.x194 + 1.5*m.x195 + 1.7*m.x196 + 1.7*m.x197 + 1.7*m.x198 + 1.5*m.x199
                        + 1.5*m.x200 + 1.5*m.x201 + 1.6*m.x202 + 1.6*m.x203 + 1.6*m.x204 + 1.45*m.x205 + 1.45*m.x206
                        + 1.45*m.x207 + 1.6*m.x208 + 1.6*m.x209 + 1.6*m.x210 + 1.55*m.x211 + 1.55*m.x212 + 1.55*m.x213
                        + 1.6*m.x214 + 1.6*m.x215 + 1.6*m.x216 + 1.45*m.x217 + 1.45*m.x218 + 1.45*m.x219 + 1.6*m.x220
                        + 1.6*m.x221 + 1.6*m.x222 + 1.55*m.x223 + 1.55*m.x224 + 1.55*m.x225 + 1.6*m.x226 + 1.6*m.x227
                        + 1.6*m.x228 + 1.45*m.x229 + 1.45*m.x230 + 1.45*m.x231 + 1.6*m.x232 + 1.6*m.x233 + 1.6*m.x234
                        + 1.55*m.x235 + 1.55*m.x236 + 1.55*m.x237 + 1.6*m.x238 + 1.6*m.x239 + 1.6*m.x240 + 1.45*m.x241
                        + 1.45*m.x242 + 1.45*m.x243 + 1.6*m.x244 + 1.6*m.x245 + 1.6*m.x246 + 1.55*m.x247 + 1.55*m.x248
                        + 1.55*m.x249 + 1.6*m.x250 + 1.6*m.x251 + 1.6*m.x252 + 1.45*m.x253 + 1.45*m.x254 + 1.45*m.x255
                        + 1.6*m.x256 + 1.6*m.x257 + 1.6*m.x258 + 1.55*m.x259 + 1.55*m.x260 + 1.55*m.x261 + 1.6*m.x262
                        + 1.6*m.x263 + 1.6*m.x264 + 1.45*m.x265 + 1.45*m.x266 + 1.45*m.x267 + 1.6*m.x268 + 1.6*m.x269
                        + 1.6*m.x270 + 1.55*m.x271 + 1.55*m.x272 + 1.55*m.x273 + 1.6*m.x274 + 1.6*m.x275 + 1.6*m.x276
                        + 1.45*m.x277 + 1.45*m.x278 + 1.45*m.x279 + 1.6*m.x280 + 1.6*m.x281 + 1.6*m.x282 + 1.55*m.x283
                        + 1.55*m.x284 + 1.55*m.x285 + 1.6*m.x286 + 1.6*m.x287 + 1.6*m.x288 + 1.45*m.x289 + 1.45*m.x290
                        + 1.45*m.x291 + 1.6*m.x292 + 1.6*m.x293 + 1.6*m.x294 + 1.55*m.x295 + 1.55*m.x296 + 1.55*m.x297
                        + 1.6*m.x298 + 1.6*m.x299 + 1.6*m.x300 + 1.5*m.x301 + 1.5*m.x302 + 1.5*m.x303 + 1.7*m.x304
                        + 1.7*m.x305 + 1.7*m.x306 + 1.5*m.x307 + 1.5*m.x308 + 1.5*m.x309 + 1.6*m.x310 + 1.6*m.x311
                        + 1.6*m.x312 + 1.5*m.x313 + 1.5*m.x314 + 1.5*m.x315 + 1.7*m.x316 + 1.7*m.x317 + 1.7*m.x318
                        + 1.5*m.x319 + 1.5*m.x320 + 1.5*m.x321 + 1.6*m.x322 + 1.6*m.x323 + 1.6*m.x324 + 1.5*m.x325
                        + 1.5*m.x326 + 1.5*m.x327 + 1.7*m.x328 + 1.7*m.x329 + 1.7*m.x330 + 1.5*m.x331 + 1.5*m.x332
                        + 1.5*m.x333 + 1.6*m.x334 + 1.6*m.x335 + 1.6*m.x336 - 10*m.x860 - 10*m.x861 - 10*m.x862
                        - 10*m.x863 - 10*m.x864 - 10*m.x865 - 4*m.x962 - m.x963 - m.x964, sense=maximize)

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

m.c25 = Constraint(expr=   m.b1 + m.b2 + m.b4 + m.b5 + m.b7 + m.b8 + m.b10 + m.b11 + m.x97 <= 2)

m.c26 = Constraint(expr=   m.b2 + m.b3 + m.b5 + m.b6 + m.b8 + m.b9 + m.b11 + m.b12 + m.x98 <= 2)

m.c27 = Constraint(expr=   m.b13 + m.b14 + m.b16 + m.b17 + m.b19 + m.b20 + m.b22 + m.b23 + m.x100 <= 2)

m.c28 = Constraint(expr=   m.b14 + m.b15 + m.b17 + m.b18 + m.b20 + m.b21 + m.b23 + m.b24 + m.x101 <= 2)

m.c29 = Constraint(expr=   m.b25 + m.b26 + m.b28 + m.b29 + m.b31 + m.b32 + m.b34 + m.b35 + m.x103 <= 2)

m.c30 = Constraint(expr=   m.b26 + m.b27 + m.b29 + m.b30 + m.b32 + m.b33 + m.b35 + m.b36 + m.x104 <= 2)

m.c31 = Constraint(expr=   m.b37 + m.b38 + m.b40 + m.b41 + m.b43 + m.b44 + m.b46 + m.b47 + m.x106 <= 2)

m.c32 = Constraint(expr=   m.b38 + m.b39 + m.b41 + m.b42 + m.b44 + m.b45 + m.b47 + m.b48 + m.x107 <= 2)

m.c33 = Constraint(expr=   m.b49 + m.b50 + m.b52 + m.b53 + m.b55 + m.b56 + m.b58 + m.b59 + m.x109 <= 2)

m.c34 = Constraint(expr=   m.b50 + m.b51 + m.b53 + m.b54 + m.b56 + m.b57 + m.b59 + m.b60 + m.x110 <= 2)

m.c35 = Constraint(expr=   m.b61 + m.b62 + m.b64 + m.b65 + m.b67 + m.b68 + m.b70 + m.b71 + m.x112 <= 2)

m.c36 = Constraint(expr=   m.b62 + m.b63 + m.b65 + m.b66 + m.b68 + m.b69 + m.b71 + m.b72 + m.x113 <= 2)

m.c37 = Constraint(expr=   m.b73 + m.b74 + m.b76 + m.b77 + m.b79 + m.b80 + m.b82 + m.b83 + m.x115 <= 2)

m.c38 = Constraint(expr=   m.b74 + m.b75 + m.b77 + m.b78 + m.b80 + m.b81 + m.b83 + m.b84 + m.x116 <= 2)

m.c39 = Constraint(expr=   m.b85 + m.b86 + m.b88 + m.b89 + m.b91 + m.b92 + m.b94 + m.b95 + m.x118 <= 2)

m.c40 = Constraint(expr=   m.b86 + m.b87 + m.b89 + m.b90 + m.b92 + m.b93 + m.b95 + m.b96 + m.x119 <= 2)

m.c41 = Constraint(expr= - m.b1 + m.b2 - m.b4 + m.b5 - m.b7 + m.b8 - m.b10 + m.b11 + m.x97 >= 0)

m.c42 = Constraint(expr= - m.b2 + m.b3 - m.b5 + m.b6 - m.b8 + m.b9 - m.b11 + m.b12 + m.x98 >= 0)

m.c43 = Constraint(expr= - m.b13 + m.b14 - m.b16 + m.b17 - m.b19 + m.b20 - m.b22 + m.b23 + m.x100 >= 0)

m.c44 = Constraint(expr= - m.b14 + m.b15 - m.b17 + m.b18 - m.b20 + m.b21 - m.b23 + m.b24 + m.x101 >= 0)

m.c45 = Constraint(expr= - m.b25 + m.b26 - m.b28 + m.b29 - m.b31 + m.b32 - m.b34 + m.b35 + m.x103 >= 0)

m.c46 = Constraint(expr= - m.b26 + m.b27 - m.b29 + m.b30 - m.b32 + m.b33 - m.b35 + m.b36 + m.x104 >= 0)

m.c47 = Constraint(expr= - m.b37 + m.b38 - m.b40 + m.b41 - m.b43 + m.b44 - m.b46 + m.b47 + m.x106 >= 0)

m.c48 = Constraint(expr= - m.b38 + m.b39 - m.b41 + m.b42 - m.b44 + m.b45 - m.b47 + m.b48 + m.x107 >= 0)

m.c49 = Constraint(expr= - m.b49 + m.b50 - m.b52 + m.b53 - m.b55 + m.b56 - m.b58 + m.b59 + m.x109 >= 0)

m.c50 = Constraint(expr= - m.b50 + m.b51 - m.b53 + m.b54 - m.b56 + m.b57 - m.b59 + m.b60 + m.x110 >= 0)

m.c51 = Constraint(expr= - m.b61 + m.b62 - m.b64 + m.b65 - m.b67 + m.b68 - m.b70 + m.b71 + m.x112 >= 0)

m.c52 = Constraint(expr= - m.b62 + m.b63 - m.b65 + m.b66 - m.b68 + m.b69 - m.b71 + m.b72 + m.x113 >= 0)

m.c53 = Constraint(expr= - m.b73 + m.b74 - m.b76 + m.b77 - m.b79 + m.b80 - m.b82 + m.b83 + m.x115 >= 0)

m.c54 = Constraint(expr= - m.b74 + m.b75 - m.b77 + m.b78 - m.b80 + m.b81 - m.b83 + m.b84 + m.x116 >= 0)

m.c55 = Constraint(expr= - m.b85 + m.b86 - m.b88 + m.b89 - m.b91 + m.b92 - m.b94 + m.b95 + m.x118 >= 0)

m.c56 = Constraint(expr= - m.b86 + m.b87 - m.b89 + m.b90 - m.b92 + m.b93 - m.b95 + m.b96 + m.x119 >= 0)

m.c57 = Constraint(expr= - m.b3 - m.b6 - m.b9 - m.b12 + m.x99 >= 0)

m.c58 = Constraint(expr= - m.b15 - m.b18 - m.b21 - m.b24 + m.x102 >= 0)

m.c59 = Constraint(expr= - m.b27 - m.b30 - m.b33 - m.b36 + m.x105 >= 0)

m.c60 = Constraint(expr= - m.b39 - m.b42 - m.b45 - m.b48 + m.x108 >= 0)

m.c61 = Constraint(expr= - m.b51 - m.b54 - m.b57 - m.b60 + m.x111 >= 0)

m.c62 = Constraint(expr= - m.b63 - m.b66 - m.b69 - m.b72 + m.x114 >= 0)

m.c63 = Constraint(expr= - m.b75 - m.b78 - m.b81 - m.b84 + m.x117 >= 0)

m.c64 = Constraint(expr= - m.b87 - m.b90 - m.b93 - m.b96 + m.x120 >= 0)

m.c65 = Constraint(expr=   m.x97 + m.x98 + m.x99 == 1)

m.c66 = Constraint(expr=   m.x100 + m.x101 + m.x102 == 1)

m.c67 = Constraint(expr=   m.x103 + m.x104 + m.x105 == 1)

m.c68 = Constraint(expr=   m.x106 + m.x107 + m.x108 == 1)

m.c69 = Constraint(expr=   m.x109 + m.x110 + m.x111 == 1)

m.c70 = Constraint(expr=   m.x112 + m.x113 + m.x114 == 1)

m.c71 = Constraint(expr=   m.x115 + m.x116 + m.x117 == 1)

m.c72 = Constraint(expr=   m.x118 + m.x119 + m.x120 == 1)

m.c73 = Constraint(expr= - m.x346 - 1.25*m.x458 + 1.25*m.x554 <= 0)

m.c74 = Constraint(expr= - m.x347 - 1.25*m.x459 + 1.25*m.x555 <= 0)

m.c75 = Constraint(expr= - m.x348 - 1.25*m.x460 + 1.25*m.x556 <= 0)

m.c76 = Constraint(expr= - m.x349 - 1.25*m.x461 + 1.25*m.x557 <= 0)

m.c77 = Constraint(expr= - m.x350 - 1.25*m.x462 + 1.25*m.x558 <= 0)

m.c78 = Constraint(expr= - m.x351 - 1.25*m.x463 + 1.25*m.x559 <= 0)

m.c79 = Constraint(expr= - m.x352 - 1.25*m.x464 + 1.25*m.x560 <= 0)

m.c80 = Constraint(expr= - m.x353 - 1.25*m.x465 + 1.25*m.x561 <= 0)

m.c81 = Constraint(expr= - m.x354 - 1.25*m.x466 + 1.25*m.x562 <= 0)

m.c82 = Constraint(expr= - m.x355 - 1.25*m.x467 + 1.25*m.x563 <= 0)

m.c83 = Constraint(expr= - m.x356 - 1.25*m.x468 + 1.25*m.x564 <= 0)

m.c84 = Constraint(expr= - m.x357 - 1.25*m.x469 + 1.25*m.x565 <= 0)

m.c85 = Constraint(expr= - m.x358 - 1.25*m.x470 + 1.25*m.x566 <= 0)

m.c86 = Constraint(expr= - m.x359 - 1.25*m.x471 + 1.25*m.x567 <= 0)

m.c87 = Constraint(expr= - m.x360 - 1.25*m.x472 + 1.25*m.x568 <= 0)

m.c88 = Constraint(expr= - m.x361 - 1.25*m.x473 + 1.25*m.x569 <= 0)

m.c89 = Constraint(expr= - m.x362 - 1.25*m.x474 + 1.25*m.x570 <= 0)

m.c90 = Constraint(expr= - m.x363 - 1.25*m.x475 + 1.25*m.x571 <= 0)

m.c91 = Constraint(expr= - m.x364 - 1.25*m.x476 + 1.25*m.x572 <= 0)

m.c92 = Constraint(expr= - m.x365 - 1.25*m.x477 + 1.25*m.x573 <= 0)

m.c93 = Constraint(expr= - m.x366 - 1.25*m.x478 + 1.25*m.x574 <= 0)

m.c94 = Constraint(expr= - m.x367 - 1.25*m.x479 + 1.25*m.x575 <= 0)

m.c95 = Constraint(expr= - m.x368 - 1.25*m.x480 + 1.25*m.x576 <= 0)

m.c96 = Constraint(expr= - m.x369 - 1.25*m.x481 + 1.25*m.x577 <= 0)

m.c97 = Constraint(expr= - m.x370 - 1.25*m.x482 + 1.25*m.x578 <= 0)

m.c98 = Constraint(expr= - m.x371 - 1.25*m.x483 + 1.25*m.x579 <= 0)

m.c99 = Constraint(expr= - m.x372 - 1.25*m.x484 + 1.25*m.x580 <= 0)

m.c100 = Constraint(expr= - m.x373 - 1.25*m.x485 + 1.25*m.x581 <= 0)

m.c101 = Constraint(expr= - m.x374 - 1.25*m.x486 + 1.25*m.x582 <= 0)

m.c102 = Constraint(expr= - m.x375 - 1.25*m.x487 + 1.25*m.x583 <= 0)

m.c103 = Constraint(expr= - m.x376 - 1.25*m.x488 + 1.25*m.x584 <= 0)

m.c104 = Constraint(expr= - m.x377 - 1.25*m.x489 + 1.25*m.x585 <= 0)

m.c105 = Constraint(expr= - m.x378 - 1.25*m.x490 + 1.25*m.x586 <= 0)

m.c106 = Constraint(expr= - m.x379 - 1.25*m.x491 + 1.25*m.x587 <= 0)

m.c107 = Constraint(expr= - m.x380 - 1.25*m.x492 + 1.25*m.x588 <= 0)

m.c108 = Constraint(expr= - m.x381 - 1.25*m.x493 + 1.25*m.x589 <= 0)

m.c109 = Constraint(expr= - m.x382 - 1.25*m.x494 + 1.25*m.x590 <= 0)

m.c110 = Constraint(expr= - m.x383 - 1.25*m.x495 + 1.25*m.x591 <= 0)

m.c111 = Constraint(expr= - m.x384 - 1.25*m.x496 + 1.25*m.x592 <= 0)

m.c112 = Constraint(expr= - m.x385 - 1.25*m.x497 + 1.25*m.x593 <= 0)

m.c113 = Constraint(expr= - m.x386 - 1.25*m.x498 + 1.25*m.x594 <= 0)

m.c114 = Constraint(expr= - m.x387 - 1.25*m.x499 + 1.25*m.x595 <= 0)

m.c115 = Constraint(expr= - m.x388 - 1.25*m.x500 + 1.25*m.x596 <= 0)

m.c116 = Constraint(expr= - m.x389 - 1.25*m.x501 + 1.25*m.x597 <= 0)

m.c117 = Constraint(expr= - m.x390 - 1.25*m.x502 + 1.25*m.x598 <= 0)

m.c118 = Constraint(expr= - m.x391 - 1.25*m.x503 + 1.25*m.x599 <= 0)

m.c119 = Constraint(expr= - m.x392 - 1.25*m.x504 + 1.25*m.x600 <= 0)

m.c120 = Constraint(expr= - m.x393 - 1.25*m.x505 + 1.25*m.x601 <= 0)

m.c121 = Constraint(expr= - m.x394 - 1.25*m.x506 + 1.25*m.x602 <= 0)

m.c122 = Constraint(expr= - m.x395 - 1.25*m.x507 + 1.25*m.x603 <= 0)

m.c123 = Constraint(expr= - m.x396 - 1.25*m.x508 + 1.25*m.x604 <= 0)

m.c124 = Constraint(expr= - m.x397 - 1.25*m.x509 + 1.25*m.x605 <= 0)

m.c125 = Constraint(expr= - m.x398 - 1.25*m.x510 + 1.25*m.x606 <= 0)

m.c126 = Constraint(expr= - m.x399 - 1.25*m.x511 + 1.25*m.x607 <= 0)

m.c127 = Constraint(expr= - m.x400 - 1.25*m.x512 + 1.25*m.x608 <= 0)

m.c128 = Constraint(expr= - m.x401 - 1.25*m.x513 + 1.25*m.x609 <= 0)

m.c129 = Constraint(expr= - m.x402 - 1.25*m.x514 + 1.25*m.x610 <= 0)

m.c130 = Constraint(expr= - m.x403 - 1.25*m.x515 + 1.25*m.x611 <= 0)

m.c131 = Constraint(expr= - m.x404 - 1.25*m.x516 + 1.25*m.x612 <= 0)

m.c132 = Constraint(expr= - m.x405 - 1.25*m.x517 + 1.25*m.x613 <= 0)

m.c133 = Constraint(expr= - m.x406 - 1.25*m.x518 + 1.25*m.x614 <= 0)

m.c134 = Constraint(expr= - m.x407 - 1.25*m.x519 + 1.25*m.x615 <= 0)

m.c135 = Constraint(expr= - m.x408 - 1.25*m.x520 + 1.25*m.x616 <= 0)

m.c136 = Constraint(expr= - m.x409 - 1.25*m.x521 + 1.25*m.x617 <= 0)

m.c137 = Constraint(expr= - m.x410 - 1.25*m.x522 + 1.25*m.x618 <= 0)

m.c138 = Constraint(expr= - m.x411 - 1.25*m.x523 + 1.25*m.x619 <= 0)

m.c139 = Constraint(expr= - m.x412 - 1.25*m.x524 + 1.25*m.x620 <= 0)

m.c140 = Constraint(expr= - m.x413 - 1.25*m.x525 + 1.25*m.x621 <= 0)

m.c141 = Constraint(expr= - m.x414 - 1.25*m.x526 + 1.25*m.x622 <= 0)

m.c142 = Constraint(expr= - m.x415 - 1.25*m.x527 + 1.25*m.x623 <= 0)

m.c143 = Constraint(expr= - m.x416 - 1.25*m.x528 + 1.25*m.x624 <= 0)

m.c144 = Constraint(expr= - m.x417 - 1.25*m.x529 + 1.25*m.x625 <= 0)

m.c145 = Constraint(expr= - m.x418 - 1.25*m.x530 + 1.25*m.x626 <= 0)

m.c146 = Constraint(expr= - m.x419 - 1.25*m.x531 + 1.25*m.x627 <= 0)

m.c147 = Constraint(expr= - m.x420 - 1.25*m.x532 + 1.25*m.x628 <= 0)

m.c148 = Constraint(expr= - m.x421 - 1.25*m.x533 + 1.25*m.x629 <= 0)

m.c149 = Constraint(expr= - m.x422 - 1.25*m.x534 + 1.25*m.x630 <= 0)

m.c150 = Constraint(expr= - m.x423 - 1.25*m.x535 + 1.25*m.x631 <= 0)

m.c151 = Constraint(expr= - m.x424 - 1.25*m.x536 + 1.25*m.x632 <= 0)

m.c152 = Constraint(expr= - m.x425 - 1.25*m.x537 + 1.25*m.x633 <= 0)

m.c153 = Constraint(expr= - m.x426 - 1.25*m.x538 + 1.25*m.x634 <= 0)

m.c154 = Constraint(expr= - m.x427 - 1.25*m.x539 + 1.25*m.x635 <= 0)

m.c155 = Constraint(expr= - m.x428 - 1.25*m.x540 + 1.25*m.x636 <= 0)

m.c156 = Constraint(expr= - m.x429 - 1.25*m.x541 + 1.25*m.x637 <= 0)

m.c157 = Constraint(expr= - m.x430 - 1.25*m.x542 + 1.25*m.x638 <= 0)

m.c158 = Constraint(expr= - m.x431 - 1.25*m.x543 + 1.25*m.x639 <= 0)

m.c159 = Constraint(expr= - m.x432 - 1.25*m.x544 + 1.25*m.x640 <= 0)

m.c160 = Constraint(expr= - m.x433 - 1.25*m.x545 + 1.25*m.x641 <= 0)

m.c161 = Constraint(expr= - m.x434 - 1.25*m.x546 + 1.25*m.x642 <= 0)

m.c162 = Constraint(expr= - m.x435 - 1.25*m.x547 + 1.25*m.x643 <= 0)

m.c163 = Constraint(expr= - m.x436 - 1.25*m.x548 + 1.25*m.x644 <= 0)

m.c164 = Constraint(expr= - m.x437 - 1.25*m.x549 + 1.25*m.x645 <= 0)

m.c165 = Constraint(expr= - m.x438 - 1.25*m.x550 + 1.25*m.x646 <= 0)

m.c166 = Constraint(expr= - m.x439 - 1.25*m.x551 + 1.25*m.x647 <= 0)

m.c167 = Constraint(expr= - m.x440 - 1.25*m.x552 + 1.25*m.x648 <= 0)

m.c168 = Constraint(expr= - m.x441 - 1.25*m.x553 + 1.25*m.x649 <= 0)

m.c169 = Constraint(expr=   m.x346 + 50*m.x458 - 50*m.x554 <= 0)

m.c170 = Constraint(expr=   m.x347 + 50*m.x459 - 50*m.x555 <= 0)

m.c171 = Constraint(expr=   m.x348 + 50*m.x460 - 50*m.x556 <= 0)

m.c172 = Constraint(expr=   m.x349 + 50*m.x461 - 50*m.x557 <= 0)

m.c173 = Constraint(expr=   m.x350 + 50*m.x462 - 50*m.x558 <= 0)

m.c174 = Constraint(expr=   m.x351 + 50*m.x463 - 50*m.x559 <= 0)

m.c175 = Constraint(expr=   m.x352 + 50*m.x464 - 50*m.x560 <= 0)

m.c176 = Constraint(expr=   m.x353 + 50*m.x465 - 50*m.x561 <= 0)

m.c177 = Constraint(expr=   m.x354 + 50*m.x466 - 50*m.x562 <= 0)

m.c178 = Constraint(expr=   m.x355 + 50*m.x467 - 50*m.x563 <= 0)

m.c179 = Constraint(expr=   m.x356 + 50*m.x468 - 50*m.x564 <= 0)

m.c180 = Constraint(expr=   m.x357 + 50*m.x469 - 50*m.x565 <= 0)

m.c181 = Constraint(expr=   m.x358 + 50*m.x470 - 50*m.x566 <= 0)

m.c182 = Constraint(expr=   m.x359 + 50*m.x471 - 50*m.x567 <= 0)

m.c183 = Constraint(expr=   m.x360 + 50*m.x472 - 50*m.x568 <= 0)

m.c184 = Constraint(expr=   m.x361 + 50*m.x473 - 50*m.x569 <= 0)

m.c185 = Constraint(expr=   m.x362 + 50*m.x474 - 50*m.x570 <= 0)

m.c186 = Constraint(expr=   m.x363 + 50*m.x475 - 50*m.x571 <= 0)

m.c187 = Constraint(expr=   m.x364 + 50*m.x476 - 50*m.x572 <= 0)

m.c188 = Constraint(expr=   m.x365 + 50*m.x477 - 50*m.x573 <= 0)

m.c189 = Constraint(expr=   m.x366 + 50*m.x478 - 50*m.x574 <= 0)

m.c190 = Constraint(expr=   m.x367 + 50*m.x479 - 50*m.x575 <= 0)

m.c191 = Constraint(expr=   m.x368 + 50*m.x480 - 50*m.x576 <= 0)

m.c192 = Constraint(expr=   m.x369 + 50*m.x481 - 50*m.x577 <= 0)

m.c193 = Constraint(expr=   m.x370 + 50*m.x482 - 50*m.x578 <= 0)

m.c194 = Constraint(expr=   m.x371 + 50*m.x483 - 50*m.x579 <= 0)

m.c195 = Constraint(expr=   m.x372 + 50*m.x484 - 50*m.x580 <= 0)

m.c196 = Constraint(expr=   m.x373 + 50*m.x485 - 50*m.x581 <= 0)

m.c197 = Constraint(expr=   m.x374 + 50*m.x486 - 50*m.x582 <= 0)

m.c198 = Constraint(expr=   m.x375 + 50*m.x487 - 50*m.x583 <= 0)

m.c199 = Constraint(expr=   m.x376 + 50*m.x488 - 50*m.x584 <= 0)

m.c200 = Constraint(expr=   m.x377 + 50*m.x489 - 50*m.x585 <= 0)

m.c201 = Constraint(expr=   m.x378 + 50*m.x490 - 50*m.x586 <= 0)

m.c202 = Constraint(expr=   m.x379 + 50*m.x491 - 50*m.x587 <= 0)

m.c203 = Constraint(expr=   m.x380 + 50*m.x492 - 50*m.x588 <= 0)

m.c204 = Constraint(expr=   m.x381 + 50*m.x493 - 50*m.x589 <= 0)

m.c205 = Constraint(expr=   m.x382 + 50*m.x494 - 50*m.x590 <= 0)

m.c206 = Constraint(expr=   m.x383 + 50*m.x495 - 50*m.x591 <= 0)

m.c207 = Constraint(expr=   m.x384 + 50*m.x496 - 50*m.x592 <= 0)

m.c208 = Constraint(expr=   m.x385 + 50*m.x497 - 50*m.x593 <= 0)

m.c209 = Constraint(expr=   m.x386 + 50*m.x498 - 50*m.x594 <= 0)

m.c210 = Constraint(expr=   m.x387 + 50*m.x499 - 50*m.x595 <= 0)

m.c211 = Constraint(expr=   m.x388 + 50*m.x500 - 50*m.x596 <= 0)

m.c212 = Constraint(expr=   m.x389 + 50*m.x501 - 50*m.x597 <= 0)

m.c213 = Constraint(expr=   m.x390 + 50*m.x502 - 50*m.x598 <= 0)

m.c214 = Constraint(expr=   m.x391 + 50*m.x503 - 50*m.x599 <= 0)

m.c215 = Constraint(expr=   m.x392 + 50*m.x504 - 50*m.x600 <= 0)

m.c216 = Constraint(expr=   m.x393 + 50*m.x505 - 50*m.x601 <= 0)

m.c217 = Constraint(expr=   m.x394 + 50*m.x506 - 50*m.x602 <= 0)

m.c218 = Constraint(expr=   m.x395 + 50*m.x507 - 50*m.x603 <= 0)

m.c219 = Constraint(expr=   m.x396 + 50*m.x508 - 50*m.x604 <= 0)

m.c220 = Constraint(expr=   m.x397 + 50*m.x509 - 50*m.x605 <= 0)

m.c221 = Constraint(expr=   m.x398 + 50*m.x510 - 50*m.x606 <= 0)

m.c222 = Constraint(expr=   m.x399 + 50*m.x511 - 50*m.x607 <= 0)

m.c223 = Constraint(expr=   m.x400 + 50*m.x512 - 50*m.x608 <= 0)

m.c224 = Constraint(expr=   m.x401 + 50*m.x513 - 50*m.x609 <= 0)

m.c225 = Constraint(expr=   m.x402 + 50*m.x514 - 50*m.x610 <= 0)

m.c226 = Constraint(expr=   m.x403 + 50*m.x515 - 50*m.x611 <= 0)

m.c227 = Constraint(expr=   m.x404 + 50*m.x516 - 50*m.x612 <= 0)

m.c228 = Constraint(expr=   m.x405 + 50*m.x517 - 50*m.x613 <= 0)

m.c229 = Constraint(expr=   m.x406 + 50*m.x518 - 50*m.x614 <= 0)

m.c230 = Constraint(expr=   m.x407 + 50*m.x519 - 50*m.x615 <= 0)

m.c231 = Constraint(expr=   m.x408 + 50*m.x520 - 50*m.x616 <= 0)

m.c232 = Constraint(expr=   m.x409 + 50*m.x521 - 50*m.x617 <= 0)

m.c233 = Constraint(expr=   m.x410 + 50*m.x522 - 50*m.x618 <= 0)

m.c234 = Constraint(expr=   m.x411 + 50*m.x523 - 50*m.x619 <= 0)

m.c235 = Constraint(expr=   m.x412 + 50*m.x524 - 50*m.x620 <= 0)

m.c236 = Constraint(expr=   m.x413 + 50*m.x525 - 50*m.x621 <= 0)

m.c237 = Constraint(expr=   m.x414 + 50*m.x526 - 50*m.x622 <= 0)

m.c238 = Constraint(expr=   m.x415 + 50*m.x527 - 50*m.x623 <= 0)

m.c239 = Constraint(expr=   m.x416 + 50*m.x528 - 50*m.x624 <= 0)

m.c240 = Constraint(expr=   m.x417 + 50*m.x529 - 50*m.x625 <= 0)

m.c241 = Constraint(expr=   m.x418 + 50*m.x530 - 50*m.x626 <= 0)

m.c242 = Constraint(expr=   m.x419 + 50*m.x531 - 50*m.x627 <= 0)

m.c243 = Constraint(expr=   m.x420 + 50*m.x532 - 50*m.x628 <= 0)

m.c244 = Constraint(expr=   m.x421 + 50*m.x533 - 50*m.x629 <= 0)

m.c245 = Constraint(expr=   m.x422 + 50*m.x534 - 50*m.x630 <= 0)

m.c246 = Constraint(expr=   m.x423 + 50*m.x535 - 50*m.x631 <= 0)

m.c247 = Constraint(expr=   m.x424 + 50*m.x536 - 50*m.x632 <= 0)

m.c248 = Constraint(expr=   m.x425 + 50*m.x537 - 50*m.x633 <= 0)

m.c249 = Constraint(expr=   m.x426 + 50*m.x538 - 50*m.x634 <= 0)

m.c250 = Constraint(expr=   m.x427 + 50*m.x539 - 50*m.x635 <= 0)

m.c251 = Constraint(expr=   m.x428 + 50*m.x540 - 50*m.x636 <= 0)

m.c252 = Constraint(expr=   m.x429 + 50*m.x541 - 50*m.x637 <= 0)

m.c253 = Constraint(expr=   m.x430 + 50*m.x542 - 50*m.x638 <= 0)

m.c254 = Constraint(expr=   m.x431 + 50*m.x543 - 50*m.x639 <= 0)

m.c255 = Constraint(expr=   m.x432 + 50*m.x544 - 50*m.x640 <= 0)

m.c256 = Constraint(expr=   m.x433 + 50*m.x545 - 50*m.x641 <= 0)

m.c257 = Constraint(expr=   m.x434 + 50*m.x546 - 50*m.x642 <= 0)

m.c258 = Constraint(expr=   m.x435 + 50*m.x547 - 50*m.x643 <= 0)

m.c259 = Constraint(expr=   m.x436 + 50*m.x548 - 50*m.x644 <= 0)

m.c260 = Constraint(expr=   m.x437 + 50*m.x549 - 50*m.x645 <= 0)

m.c261 = Constraint(expr=   m.x438 + 50*m.x550 - 50*m.x646 <= 0)

m.c262 = Constraint(expr=   m.x439 + 50*m.x551 - 50*m.x647 <= 0)

m.c263 = Constraint(expr=   m.x440 + 50*m.x552 - 50*m.x648 <= 0)

m.c264 = Constraint(expr=   m.x441 + 50*m.x553 - 50*m.x649 <= 0)

m.c265 = Constraint(expr= - 10*m.b1 + m.x346 <= 0)

m.c266 = Constraint(expr= - 10*m.b2 + m.x347 <= 0)

m.c267 = Constraint(expr= - 10*m.b3 + m.x348 <= 0)

m.c268 = Constraint(expr= - 10*m.b4 + m.x349 <= 0)

m.c269 = Constraint(expr= - 10*m.b5 + m.x350 <= 0)

m.c270 = Constraint(expr= - 10*m.b6 + m.x351 <= 0)

m.c271 = Constraint(expr= - 10*m.b7 + m.x352 <= 0)

m.c272 = Constraint(expr= - 10*m.b8 + m.x353 <= 0)

m.c273 = Constraint(expr= - 10*m.b9 + m.x354 <= 0)

m.c274 = Constraint(expr= - 10*m.b10 + m.x355 <= 0)

m.c275 = Constraint(expr= - 10*m.b11 + m.x356 <= 0)

m.c276 = Constraint(expr= - 10*m.b12 + m.x357 <= 0)

m.c277 = Constraint(expr= - 250*m.b13 + m.x358 <= 0)

m.c278 = Constraint(expr= - 250*m.b14 + m.x359 <= 0)

m.c279 = Constraint(expr= - 250*m.b15 + m.x360 <= 0)

m.c280 = Constraint(expr= - 250*m.b16 + m.x361 <= 0)

m.c281 = Constraint(expr= - 250*m.b17 + m.x362 <= 0)

m.c282 = Constraint(expr= - 250*m.b18 + m.x363 <= 0)

m.c283 = Constraint(expr= - 250*m.b19 + m.x364 <= 0)

m.c284 = Constraint(expr= - 250*m.b20 + m.x365 <= 0)

m.c285 = Constraint(expr= - 250*m.b21 + m.x366 <= 0)

m.c286 = Constraint(expr= - 250*m.b22 + m.x367 <= 0)

m.c287 = Constraint(expr= - 250*m.b23 + m.x368 <= 0)

m.c288 = Constraint(expr= - 250*m.b24 + m.x369 <= 0)

m.c289 = Constraint(expr= - 300*m.b25 + m.x370 <= 0)

m.c290 = Constraint(expr= - 300*m.b26 + m.x371 <= 0)

m.c291 = Constraint(expr= - 300*m.b27 + m.x372 <= 0)

m.c292 = Constraint(expr= - 300*m.b28 + m.x373 <= 0)

m.c293 = Constraint(expr= - 300*m.b29 + m.x374 <= 0)

m.c294 = Constraint(expr= - 300*m.b30 + m.x375 <= 0)

m.c295 = Constraint(expr= - 300*m.b31 + m.x376 <= 0)

m.c296 = Constraint(expr= - 300*m.b32 + m.x377 <= 0)

m.c297 = Constraint(expr= - 300*m.b33 + m.x378 <= 0)

m.c298 = Constraint(expr= - 300*m.b34 + m.x379 <= 0)

m.c299 = Constraint(expr= - 300*m.b35 + m.x380 <= 0)

m.c300 = Constraint(expr= - 300*m.b36 + m.x381 <= 0)

m.c301 = Constraint(expr= - 190*m.b37 + m.x382 <= 0)

m.c302 = Constraint(expr= - 190*m.b38 + m.x383 <= 0)

m.c303 = Constraint(expr= - 190*m.b39 + m.x384 <= 0)

m.c304 = Constraint(expr= - 190*m.b40 + m.x385 <= 0)

m.c305 = Constraint(expr= - 190*m.b41 + m.x386 <= 0)

m.c306 = Constraint(expr= - 190*m.b42 + m.x387 <= 0)

m.c307 = Constraint(expr= - 190*m.b43 + m.x388 <= 0)

m.c308 = Constraint(expr= - 190*m.b44 + m.x389 <= 0)

m.c309 = Constraint(expr= - 190*m.b45 + m.x390 <= 0)

m.c310 = Constraint(expr= - 190*m.b46 + m.x391 <= 0)

m.c311 = Constraint(expr= - 190*m.b47 + m.x392 <= 0)

m.c312 = Constraint(expr= - 190*m.b48 + m.x393 <= 0)

m.c313 = Constraint(expr=   m.x394 <= 0)

m.c314 = Constraint(expr= - 10*m.b50 + m.x395 <= 0)

m.c315 = Constraint(expr= - 10*m.b51 + m.x396 <= 0)

m.c316 = Constraint(expr=   m.x397 <= 0)

m.c317 = Constraint(expr= - 10*m.b53 + m.x398 <= 0)

m.c318 = Constraint(expr= - 10*m.b54 + m.x399 <= 0)

m.c319 = Constraint(expr=   m.x400 <= 0)

m.c320 = Constraint(expr= - 10*m.b56 + m.x401 <= 0)

m.c321 = Constraint(expr= - 10*m.b57 + m.x402 <= 0)

m.c322 = Constraint(expr=   m.x403 <= 0)

m.c323 = Constraint(expr= - 10*m.b59 + m.x404 <= 0)

m.c324 = Constraint(expr= - 10*m.b60 + m.x405 <= 0)

m.c325 = Constraint(expr=   m.x406 <= 0)

m.c326 = Constraint(expr= - 250*m.b62 + m.x407 <= 0)

m.c327 = Constraint(expr= - 250*m.b63 + m.x408 <= 0)

m.c328 = Constraint(expr=   m.x409 <= 0)

m.c329 = Constraint(expr= - 250*m.b65 + m.x410 <= 0)

m.c330 = Constraint(expr= - 250*m.b66 + m.x411 <= 0)

m.c331 = Constraint(expr=   m.x412 <= 0)

m.c332 = Constraint(expr= - 250*m.b68 + m.x413 <= 0)

m.c333 = Constraint(expr= - 250*m.b69 + m.x414 <= 0)

m.c334 = Constraint(expr=   m.x415 <= 0)

m.c335 = Constraint(expr= - 250*m.b71 + m.x416 <= 0)

m.c336 = Constraint(expr= - 250*m.b72 + m.x417 <= 0)

m.c337 = Constraint(expr=   m.x418 <= 0)

m.c338 = Constraint(expr= - 250*m.b74 + m.x419 <= 0)

m.c339 = Constraint(expr= - 250*m.b75 + m.x420 <= 0)

m.c340 = Constraint(expr=   m.x421 <= 0)

m.c341 = Constraint(expr= - 250*m.b77 + m.x422 <= 0)

m.c342 = Constraint(expr= - 250*m.b78 + m.x423 <= 0)

m.c343 = Constraint(expr=   m.x424 <= 0)

m.c344 = Constraint(expr= - 250*m.b80 + m.x425 <= 0)

m.c345 = Constraint(expr= - 250*m.b81 + m.x426 <= 0)

m.c346 = Constraint(expr=   m.x427 <= 0)

m.c347 = Constraint(expr= - 250*m.b83 + m.x428 <= 0)

m.c348 = Constraint(expr= - 250*m.b84 + m.x429 <= 0)

m.c349 = Constraint(expr=   m.x430 <= 0)

m.c350 = Constraint(expr= - 240*m.b86 + m.x431 <= 0)

m.c351 = Constraint(expr= - 240*m.b87 + m.x432 <= 0)

m.c352 = Constraint(expr=   m.x433 <= 0)

m.c353 = Constraint(expr= - 240*m.b89 + m.x434 <= 0)

m.c354 = Constraint(expr= - 240*m.b90 + m.x435 <= 0)

m.c355 = Constraint(expr=   m.x436 <= 0)

m.c356 = Constraint(expr= - 240*m.b92 + m.x437 <= 0)

m.c357 = Constraint(expr= - 240*m.b93 + m.x438 <= 0)

m.c358 = Constraint(expr=   m.x439 <= 0)

m.c359 = Constraint(expr= - 240*m.b95 + m.x440 <= 0)

m.c360 = Constraint(expr= - 240*m.b96 + m.x441 <= 0)

m.c361 = Constraint(expr=   m.x346 + m.x347 + m.x348 + m.x349 + m.x350 + m.x351 + m.x352 + m.x353 + m.x354 + m.x355
                          + m.x356 + m.x357 == 10)

m.c362 = Constraint(expr=   m.x358 + m.x359 + m.x360 + m.x361 + m.x362 + m.x363 + m.x364 + m.x365 + m.x366 + m.x367
                          + m.x368 + m.x369 == 250)

m.c363 = Constraint(expr=   m.x370 + m.x371 + m.x372 + m.x373 + m.x374 + m.x375 + m.x376 + m.x377 + m.x378 + m.x379
                          + m.x380 + m.x381 == 300)

m.c364 = Constraint(expr=   m.x382 + m.x383 + m.x384 + m.x385 + m.x386 + m.x387 + m.x388 + m.x389 + m.x390 + m.x391
                          + m.x392 + m.x393 == 190)

m.c365 = Constraint(expr=   m.x394 + m.x395 + m.x396 + m.x397 + m.x398 + m.x399 + m.x400 + m.x401 + m.x402 + m.x403
                          + m.x404 + m.x405 == 10)

m.c366 = Constraint(expr=   m.x406 + m.x407 + m.x408 + m.x409 + m.x410 + m.x411 + m.x412 + m.x413 + m.x414 + m.x415
                          + m.x416 + m.x417 == 250)

m.c367 = Constraint(expr=   m.x418 + m.x419 + m.x420 + m.x421 + m.x422 + m.x423 + m.x424 + m.x425 + m.x426 + m.x427
                          + m.x428 + m.x429 == 250)

m.c368 = Constraint(expr=   m.x430 + m.x431 + m.x432 + m.x433 + m.x434 + m.x435 + m.x436 + m.x437 + m.x438 + m.x439
                          + m.x440 + m.x441 == 240)

m.c369 = Constraint(expr=   160*m.b1 + m.x442 - m.x458 <= 160)

m.c370 = Constraint(expr=   160*m.b2 + m.x442 - m.x459 <= 160)

m.c371 = Constraint(expr=   160*m.b3 + m.x442 - m.x460 <= 160)

m.c372 = Constraint(expr=   160*m.b4 + m.x442 - m.x461 <= 160)

m.c373 = Constraint(expr=   160*m.b5 + m.x442 - m.x462 <= 160)

m.c374 = Constraint(expr=   160*m.b6 + m.x442 - m.x463 <= 160)

m.c375 = Constraint(expr=   160*m.b7 + m.x442 - m.x464 <= 160)

m.c376 = Constraint(expr=   160*m.b8 + m.x442 - m.x465 <= 160)

m.c377 = Constraint(expr=   160*m.b9 + m.x442 - m.x466 <= 160)

m.c378 = Constraint(expr=   160*m.b10 + m.x442 - m.x467 <= 160)

m.c379 = Constraint(expr=   160*m.b11 + m.x442 - m.x468 <= 160)

m.c380 = Constraint(expr=   160*m.b12 + m.x442 - m.x469 <= 160)

m.c381 = Constraint(expr=   160*m.b13 + m.x443 - m.x470 <= 160)

m.c382 = Constraint(expr=   160*m.b14 + m.x443 - m.x471 <= 160)

m.c383 = Constraint(expr=   160*m.b15 + m.x443 - m.x472 <= 160)

m.c384 = Constraint(expr=   160*m.b16 + m.x443 - m.x473 <= 160)

m.c385 = Constraint(expr=   160*m.b17 + m.x443 - m.x474 <= 160)

m.c386 = Constraint(expr=   160*m.b18 + m.x443 - m.x475 <= 160)

m.c387 = Constraint(expr=   160*m.b19 + m.x443 - m.x476 <= 160)

m.c388 = Constraint(expr=   160*m.b20 + m.x443 - m.x477 <= 160)

m.c389 = Constraint(expr=   160*m.b21 + m.x443 - m.x478 <= 160)

m.c390 = Constraint(expr=   160*m.b22 + m.x443 - m.x479 <= 160)

m.c391 = Constraint(expr=   160*m.b23 + m.x443 - m.x480 <= 160)

m.c392 = Constraint(expr=   160*m.b24 + m.x443 - m.x481 <= 160)

m.c393 = Constraint(expr=   160*m.b25 + m.x444 - m.x482 <= 160)

m.c394 = Constraint(expr=   160*m.b26 + m.x444 - m.x483 <= 160)

m.c395 = Constraint(expr=   160*m.b27 + m.x444 - m.x484 <= 160)

m.c396 = Constraint(expr=   160*m.b28 + m.x444 - m.x485 <= 160)

m.c397 = Constraint(expr=   160*m.b29 + m.x444 - m.x486 <= 160)

m.c398 = Constraint(expr=   160*m.b30 + m.x444 - m.x487 <= 160)

m.c399 = Constraint(expr=   160*m.b31 + m.x444 - m.x488 <= 160)

m.c400 = Constraint(expr=   160*m.b32 + m.x444 - m.x489 <= 160)

m.c401 = Constraint(expr=   160*m.b33 + m.x444 - m.x490 <= 160)

m.c402 = Constraint(expr=   160*m.b34 + m.x444 - m.x491 <= 160)

m.c403 = Constraint(expr=   160*m.b35 + m.x444 - m.x492 <= 160)

m.c404 = Constraint(expr=   160*m.b36 + m.x444 - m.x493 <= 160)

m.c405 = Constraint(expr=   160*m.b37 + m.x445 - m.x494 <= 160)

m.c406 = Constraint(expr=   160*m.b38 + m.x445 - m.x495 <= 160)

m.c407 = Constraint(expr=   160*m.b39 + m.x445 - m.x496 <= 160)

m.c408 = Constraint(expr=   160*m.b40 + m.x445 - m.x497 <= 160)

m.c409 = Constraint(expr=   160*m.b41 + m.x445 - m.x498 <= 160)

m.c410 = Constraint(expr=   160*m.b42 + m.x445 - m.x499 <= 160)

m.c411 = Constraint(expr=   160*m.b43 + m.x445 - m.x500 <= 160)

m.c412 = Constraint(expr=   160*m.b44 + m.x445 - m.x501 <= 160)

m.c413 = Constraint(expr=   160*m.b45 + m.x445 - m.x502 <= 160)

m.c414 = Constraint(expr=   160*m.b46 + m.x445 - m.x503 <= 160)

m.c415 = Constraint(expr=   160*m.b47 + m.x445 - m.x504 <= 160)

m.c416 = Constraint(expr=   160*m.b48 + m.x445 - m.x505 <= 160)

m.c417 = Constraint(expr=   160*m.b49 + m.x446 - m.x506 <= 160)

m.c418 = Constraint(expr=   160*m.b50 + m.x446 - m.x507 <= 160)

m.c419 = Constraint(expr=   160*m.b51 + m.x446 - m.x508 <= 160)

m.c420 = Constraint(expr=   160*m.b52 + m.x446 - m.x509 <= 160)

m.c421 = Constraint(expr=   160*m.b53 + m.x446 - m.x510 <= 160)

m.c422 = Constraint(expr=   160*m.b54 + m.x446 - m.x511 <= 160)

m.c423 = Constraint(expr=   160*m.b55 + m.x446 - m.x512 <= 160)

m.c424 = Constraint(expr=   160*m.b56 + m.x446 - m.x513 <= 160)

m.c425 = Constraint(expr=   160*m.b57 + m.x446 - m.x514 <= 160)

m.c426 = Constraint(expr=   160*m.b58 + m.x446 - m.x515 <= 160)

m.c427 = Constraint(expr=   160*m.b59 + m.x446 - m.x516 <= 160)

m.c428 = Constraint(expr=   160*m.b60 + m.x446 - m.x517 <= 160)

m.c429 = Constraint(expr=   160*m.b61 + m.x447 - m.x518 <= 160)

m.c430 = Constraint(expr=   160*m.b62 + m.x447 - m.x519 <= 160)

m.c431 = Constraint(expr=   160*m.b63 + m.x447 - m.x520 <= 160)

m.c432 = Constraint(expr=   160*m.b64 + m.x447 - m.x521 <= 160)

m.c433 = Constraint(expr=   160*m.b65 + m.x447 - m.x522 <= 160)

m.c434 = Constraint(expr=   160*m.b66 + m.x447 - m.x523 <= 160)

m.c435 = Constraint(expr=   160*m.b67 + m.x447 - m.x524 <= 160)

m.c436 = Constraint(expr=   160*m.b68 + m.x447 - m.x525 <= 160)

m.c437 = Constraint(expr=   160*m.b69 + m.x447 - m.x526 <= 160)

m.c438 = Constraint(expr=   160*m.b70 + m.x447 - m.x527 <= 160)

m.c439 = Constraint(expr=   160*m.b71 + m.x447 - m.x528 <= 160)

m.c440 = Constraint(expr=   160*m.b72 + m.x447 - m.x529 <= 160)

m.c441 = Constraint(expr=   160*m.b73 + m.x448 - m.x530 <= 160)

m.c442 = Constraint(expr=   160*m.b74 + m.x448 - m.x531 <= 160)

m.c443 = Constraint(expr=   160*m.b75 + m.x448 - m.x532 <= 160)

m.c444 = Constraint(expr=   160*m.b76 + m.x448 - m.x533 <= 160)

m.c445 = Constraint(expr=   160*m.b77 + m.x448 - m.x534 <= 160)

m.c446 = Constraint(expr=   160*m.b78 + m.x448 - m.x535 <= 160)

m.c447 = Constraint(expr=   160*m.b79 + m.x448 - m.x536 <= 160)

m.c448 = Constraint(expr=   160*m.b80 + m.x448 - m.x537 <= 160)

m.c449 = Constraint(expr=   160*m.b81 + m.x448 - m.x538 <= 160)

m.c450 = Constraint(expr=   160*m.b82 + m.x448 - m.x539 <= 160)

m.c451 = Constraint(expr=   160*m.b83 + m.x448 - m.x540 <= 160)

m.c452 = Constraint(expr=   160*m.b84 + m.x448 - m.x541 <= 160)

m.c453 = Constraint(expr=   160*m.b85 + m.x449 - m.x542 <= 160)

m.c454 = Constraint(expr=   160*m.b86 + m.x449 - m.x543 <= 160)

m.c455 = Constraint(expr=   160*m.b87 + m.x449 - m.x544 <= 160)

m.c456 = Constraint(expr=   160*m.b88 + m.x449 - m.x545 <= 160)

m.c457 = Constraint(expr=   160*m.b89 + m.x449 - m.x546 <= 160)

m.c458 = Constraint(expr=   160*m.b90 + m.x449 - m.x547 <= 160)

m.c459 = Constraint(expr=   160*m.b91 + m.x449 - m.x548 <= 160)

m.c460 = Constraint(expr=   160*m.b92 + m.x449 - m.x549 <= 160)

m.c461 = Constraint(expr=   160*m.b93 + m.x449 - m.x550 <= 160)

m.c462 = Constraint(expr=   160*m.b94 + m.x449 - m.x551 <= 160)

m.c463 = Constraint(expr=   160*m.b95 + m.x449 - m.x552 <= 160)

m.c464 = Constraint(expr=   160*m.b96 + m.x449 - m.x553 <= 160)

m.c465 = Constraint(expr= - 160*m.b1 + m.x450 - m.x554 >= -160)

m.c466 = Constraint(expr= - 160*m.b2 + m.x450 - m.x555 >= -160)

m.c467 = Constraint(expr= - 160*m.b3 + m.x450 - m.x556 >= -160)

m.c468 = Constraint(expr= - 160*m.b4 + m.x450 - m.x557 >= -160)

m.c469 = Constraint(expr= - 160*m.b5 + m.x450 - m.x558 >= -160)

m.c470 = Constraint(expr= - 160*m.b6 + m.x450 - m.x559 >= -160)

m.c471 = Constraint(expr= - 160*m.b7 + m.x450 - m.x560 >= -160)

m.c472 = Constraint(expr= - 160*m.b8 + m.x450 - m.x561 >= -160)

m.c473 = Constraint(expr= - 160*m.b9 + m.x450 - m.x562 >= -160)

m.c474 = Constraint(expr= - 160*m.b10 + m.x450 - m.x563 >= -160)

m.c475 = Constraint(expr= - 160*m.b11 + m.x450 - m.x564 >= -160)

m.c476 = Constraint(expr= - 160*m.b12 + m.x450 - m.x565 >= -160)

m.c477 = Constraint(expr= - 160*m.b13 + m.x451 - m.x566 >= -160)

m.c478 = Constraint(expr= - 160*m.b14 + m.x451 - m.x567 >= -160)

m.c479 = Constraint(expr= - 160*m.b15 + m.x451 - m.x568 >= -160)

m.c480 = Constraint(expr= - 160*m.b16 + m.x451 - m.x569 >= -160)

m.c481 = Constraint(expr= - 160*m.b17 + m.x451 - m.x570 >= -160)

m.c482 = Constraint(expr= - 160*m.b18 + m.x451 - m.x571 >= -160)

m.c483 = Constraint(expr= - 160*m.b19 + m.x451 - m.x572 >= -160)

m.c484 = Constraint(expr= - 160*m.b20 + m.x451 - m.x573 >= -160)

m.c485 = Constraint(expr= - 160*m.b21 + m.x451 - m.x574 >= -160)

m.c486 = Constraint(expr= - 160*m.b22 + m.x451 - m.x575 >= -160)

m.c487 = Constraint(expr= - 160*m.b23 + m.x451 - m.x576 >= -160)

m.c488 = Constraint(expr= - 160*m.b24 + m.x451 - m.x577 >= -160)

m.c489 = Constraint(expr= - 160*m.b25 + m.x452 - m.x578 >= -160)

m.c490 = Constraint(expr= - 160*m.b26 + m.x452 - m.x579 >= -160)

m.c491 = Constraint(expr= - 160*m.b27 + m.x452 - m.x580 >= -160)

m.c492 = Constraint(expr= - 160*m.b28 + m.x452 - m.x581 >= -160)

m.c493 = Constraint(expr= - 160*m.b29 + m.x452 - m.x582 >= -160)

m.c494 = Constraint(expr= - 160*m.b30 + m.x452 - m.x583 >= -160)

m.c495 = Constraint(expr= - 160*m.b31 + m.x452 - m.x584 >= -160)

m.c496 = Constraint(expr= - 160*m.b32 + m.x452 - m.x585 >= -160)

m.c497 = Constraint(expr= - 160*m.b33 + m.x452 - m.x586 >= -160)

m.c498 = Constraint(expr= - 160*m.b34 + m.x452 - m.x587 >= -160)

m.c499 = Constraint(expr= - 160*m.b35 + m.x452 - m.x588 >= -160)

m.c500 = Constraint(expr= - 160*m.b36 + m.x452 - m.x589 >= -160)

m.c501 = Constraint(expr= - 160*m.b37 + m.x453 - m.x590 >= -160)

m.c502 = Constraint(expr= - 160*m.b38 + m.x453 - m.x591 >= -160)

m.c503 = Constraint(expr= - 160*m.b39 + m.x453 - m.x592 >= -160)

m.c504 = Constraint(expr= - 160*m.b40 + m.x453 - m.x593 >= -160)

m.c505 = Constraint(expr= - 160*m.b41 + m.x453 - m.x594 >= -160)

m.c506 = Constraint(expr= - 160*m.b42 + m.x453 - m.x595 >= -160)

m.c507 = Constraint(expr= - 160*m.b43 + m.x453 - m.x596 >= -160)

m.c508 = Constraint(expr= - 160*m.b44 + m.x453 - m.x597 >= -160)

m.c509 = Constraint(expr= - 160*m.b45 + m.x453 - m.x598 >= -160)

m.c510 = Constraint(expr= - 160*m.b46 + m.x453 - m.x599 >= -160)

m.c511 = Constraint(expr= - 160*m.b47 + m.x453 - m.x600 >= -160)

m.c512 = Constraint(expr= - 160*m.b48 + m.x453 - m.x601 >= -160)

m.c513 = Constraint(expr= - 160*m.b49 + m.x454 - m.x602 >= -160)

m.c514 = Constraint(expr= - 160*m.b50 + m.x454 - m.x603 >= -160)

m.c515 = Constraint(expr= - 160*m.b51 + m.x454 - m.x604 >= -160)

m.c516 = Constraint(expr= - 160*m.b52 + m.x454 - m.x605 >= -160)

m.c517 = Constraint(expr= - 160*m.b53 + m.x454 - m.x606 >= -160)

m.c518 = Constraint(expr= - 160*m.b54 + m.x454 - m.x607 >= -160)

m.c519 = Constraint(expr= - 160*m.b55 + m.x454 - m.x608 >= -160)

m.c520 = Constraint(expr= - 160*m.b56 + m.x454 - m.x609 >= -160)

m.c521 = Constraint(expr= - 160*m.b57 + m.x454 - m.x610 >= -160)

m.c522 = Constraint(expr= - 160*m.b58 + m.x454 - m.x611 >= -160)

m.c523 = Constraint(expr= - 160*m.b59 + m.x454 - m.x612 >= -160)

m.c524 = Constraint(expr= - 160*m.b60 + m.x454 - m.x613 >= -160)

m.c525 = Constraint(expr= - 160*m.b61 + m.x455 - m.x614 >= -160)

m.c526 = Constraint(expr= - 160*m.b62 + m.x455 - m.x615 >= -160)

m.c527 = Constraint(expr= - 160*m.b63 + m.x455 - m.x616 >= -160)

m.c528 = Constraint(expr= - 160*m.b64 + m.x455 - m.x617 >= -160)

m.c529 = Constraint(expr= - 160*m.b65 + m.x455 - m.x618 >= -160)

m.c530 = Constraint(expr= - 160*m.b66 + m.x455 - m.x619 >= -160)

m.c531 = Constraint(expr= - 160*m.b67 + m.x455 - m.x620 >= -160)

m.c532 = Constraint(expr= - 160*m.b68 + m.x455 - m.x621 >= -160)

m.c533 = Constraint(expr= - 160*m.b69 + m.x455 - m.x622 >= -160)

m.c534 = Constraint(expr= - 160*m.b70 + m.x455 - m.x623 >= -160)

m.c535 = Constraint(expr= - 160*m.b71 + m.x455 - m.x624 >= -160)

m.c536 = Constraint(expr= - 160*m.b72 + m.x455 - m.x625 >= -160)

m.c537 = Constraint(expr= - 160*m.b73 + m.x456 - m.x626 >= -160)

m.c538 = Constraint(expr= - 160*m.b74 + m.x456 - m.x627 >= -160)

m.c539 = Constraint(expr= - 160*m.b75 + m.x456 - m.x628 >= -160)

m.c540 = Constraint(expr= - 160*m.b76 + m.x456 - m.x629 >= -160)

m.c541 = Constraint(expr= - 160*m.b77 + m.x456 - m.x630 >= -160)

m.c542 = Constraint(expr= - 160*m.b78 + m.x456 - m.x631 >= -160)

m.c543 = Constraint(expr= - 160*m.b79 + m.x456 - m.x632 >= -160)

m.c544 = Constraint(expr= - 160*m.b80 + m.x456 - m.x633 >= -160)

m.c545 = Constraint(expr= - 160*m.b81 + m.x456 - m.x634 >= -160)

m.c546 = Constraint(expr= - 160*m.b82 + m.x456 - m.x635 >= -160)

m.c547 = Constraint(expr= - 160*m.b83 + m.x456 - m.x636 >= -160)

m.c548 = Constraint(expr= - 160*m.b84 + m.x456 - m.x637 >= -160)

m.c549 = Constraint(expr= - 160*m.b85 + m.x457 - m.x638 >= -160)

m.c550 = Constraint(expr= - 160*m.b86 + m.x457 - m.x639 >= -160)

m.c551 = Constraint(expr= - 160*m.b87 + m.x457 - m.x640 >= -160)

m.c552 = Constraint(expr= - 160*m.b88 + m.x457 - m.x641 >= -160)

m.c553 = Constraint(expr= - 160*m.b89 + m.x457 - m.x642 >= -160)

m.c554 = Constraint(expr= - 160*m.b90 + m.x457 - m.x643 >= -160)

m.c555 = Constraint(expr= - 160*m.b91 + m.x457 - m.x644 >= -160)

m.c556 = Constraint(expr= - 160*m.b92 + m.x457 - m.x645 >= -160)

m.c557 = Constraint(expr= - 160*m.b93 + m.x457 - m.x646 >= -160)

m.c558 = Constraint(expr= - 160*m.b94 + m.x457 - m.x647 >= -160)

m.c559 = Constraint(expr= - 160*m.b95 + m.x457 - m.x648 >= -160)

m.c560 = Constraint(expr= - 160*m.b96 + m.x457 - m.x649 >= -160)

m.c561 = Constraint(expr=   m.x443 - m.x450 >= 0)

m.c562 = Constraint(expr=   m.x444 - m.x451 >= 0)

m.c563 = Constraint(expr=   m.x445 - m.x452 >= 0)

m.c564 = Constraint(expr=   m.x446 - m.x453 >= 0)

m.c565 = Constraint(expr=   m.x447 - m.x454 >= 0)

m.c566 = Constraint(expr=   m.x448 - m.x455 >= 0)

m.c567 = Constraint(expr=   m.x449 - m.x456 >= 0)

m.c568 = Constraint(expr= - m.x740 + m.x764 + m.x767 + m.x770 + m.x773 == 0)

m.c569 = Constraint(expr= - m.x741 + m.x765 + m.x768 + m.x771 + m.x774 == 0)

m.c570 = Constraint(expr= - m.x742 + m.x766 + m.x769 + m.x772 + m.x775 == 0)

m.c571 = Constraint(expr= - m.x743 + m.x776 + m.x779 + m.x782 + m.x785 == 0)

m.c572 = Constraint(expr= - m.x744 + m.x777 + m.x780 + m.x783 + m.x786 == 0)

m.c573 = Constraint(expr= - m.x745 + m.x778 + m.x781 + m.x784 + m.x787 == 0)

m.c574 = Constraint(expr= - m.x746 + m.x788 + m.x791 + m.x794 + m.x797 == 0)

m.c575 = Constraint(expr= - m.x747 + m.x789 + m.x792 + m.x795 + m.x798 == 0)

m.c576 = Constraint(expr= - m.x748 + m.x790 + m.x793 + m.x796 + m.x799 == 0)

m.c577 = Constraint(expr= - m.x749 + m.x800 + m.x803 + m.x806 + m.x809 == 0)

m.c578 = Constraint(expr= - m.x750 + m.x801 + m.x804 + m.x807 + m.x810 == 0)

m.c579 = Constraint(expr= - m.x751 + m.x802 + m.x805 + m.x808 + m.x811 == 0)

m.c580 = Constraint(expr= - m.x752 + m.x812 + m.x815 + m.x818 + m.x821 == 0)

m.c581 = Constraint(expr= - m.x753 + m.x813 + m.x816 + m.x819 + m.x822 == 0)

m.c582 = Constraint(expr= - m.x754 + m.x814 + m.x817 + m.x820 + m.x823 == 0)

m.c583 = Constraint(expr= - m.x755 + m.x824 + m.x827 + m.x830 + m.x833 == 0)

m.c584 = Constraint(expr= - m.x756 + m.x825 + m.x828 + m.x831 + m.x834 == 0)

m.c585 = Constraint(expr= - m.x757 + m.x826 + m.x829 + m.x832 + m.x835 == 0)

m.c586 = Constraint(expr= - m.x758 + m.x836 + m.x839 + m.x842 + m.x845 == 0)

m.c587 = Constraint(expr= - m.x759 + m.x837 + m.x840 + m.x843 + m.x846 == 0)

m.c588 = Constraint(expr= - m.x760 + m.x838 + m.x841 + m.x844 + m.x847 == 0)

m.c589 = Constraint(expr= - m.x761 + m.x848 + m.x851 + m.x854 + m.x857 == 0)

m.c590 = Constraint(expr= - m.x762 + m.x849 + m.x852 + m.x855 + m.x858 == 0)

m.c591 = Constraint(expr= - m.x763 + m.x850 + m.x853 + m.x856 + m.x859 == 0)

m.c592 = Constraint(expr= - 0.142857142857143*m.x157 + m.x193 == 0)

m.c593 = Constraint(expr= - 0.285714285714286*m.x157 + m.x196 == 0)

m.c594 = Constraint(expr= - 0.285714285714286*m.x157 + m.x199 == 0)

m.c595 = Constraint(expr= - 0.285714285714286*m.x157 + m.x202 == 0)

m.c596 = Constraint(expr= - 0.25*m.x160 + m.x205 == 0)

m.c597 = Constraint(expr= - 0.25*m.x160 + m.x208 == 0)

m.c598 = Constraint(expr= - 0.25*m.x160 + m.x211 == 0)

m.c599 = Constraint(expr= - 0.25*m.x160 + m.x214 == 0)

m.c600 = Constraint(expr= - 0.25*m.x163 + m.x217 == 0)

m.c601 = Constraint(expr= - 0.25*m.x163 + m.x220 == 0)

m.c602 = Constraint(expr= - 0.25*m.x163 + m.x223 == 0)

m.c603 = Constraint(expr= - 0.25*m.x163 + m.x226 == 0)

m.c604 = Constraint(expr= - 0.285714285714286*m.x166 + m.x229 == 0)

m.c605 = Constraint(expr= - 0.285714285714286*m.x166 + m.x232 == 0)

m.c606 = Constraint(expr= - 0.142857142857143*m.x166 + m.x235 == 0)

m.c607 = Constraint(expr= - 0.285714285714286*m.x166 + m.x238 == 0)

m.c608 = Constraint(expr= - 0.285714285714286*m.x169 + m.x241 == 0)

m.c609 = Constraint(expr= - 0.285714285714286*m.x169 + m.x244 == 0)

m.c610 = Constraint(expr= - 0.142857142857143*m.x169 + m.x247 == 0)

m.c611 = Constraint(expr= - 0.285714285714286*m.x169 + m.x250 == 0)

m.c612 = Constraint(expr= - 0.210526315789474*m.x172 + m.x253 == 0)

m.c613 = Constraint(expr= - 0.263157894736842*m.x172 + m.x256 == 0)

m.c614 = Constraint(expr= - 0.210526315789474*m.x172 + m.x259 == 0)

m.c615 = Constraint(expr= - 0.315789473684211*m.x172 + m.x262 == 0)

m.c616 = Constraint(expr= - 0.210526315789474*m.x175 + m.x265 == 0)

m.c617 = Constraint(expr= - 0.263157894736842*m.x175 + m.x268 == 0)

m.c618 = Constraint(expr= - 0.210526315789474*m.x175 + m.x271 == 0)

m.c619 = Constraint(expr= - 0.315789473684211*m.x175 + m.x274 == 0)

m.c620 = Constraint(expr= - 0.333333333333333*m.x178 + m.x277 == 0)

m.c621 = Constraint(expr= - 0.333333333333333*m.x178 + m.x280 == 0)

m.c622 = Constraint(expr= - 0.166666666666667*m.x178 + m.x283 == 0)

m.c623 = Constraint(expr= - 0.166666666666667*m.x178 + m.x286 == 0)

m.c624 = Constraint(expr= - 0.333333333333333*m.x181 + m.x289 == 0)

m.c625 = Constraint(expr= - 0.333333333333333*m.x181 + m.x292 == 0)

m.c626 = Constraint(expr= - 0.166666666666667*m.x181 + m.x295 == 0)

m.c627 = Constraint(expr= - 0.166666666666667*m.x181 + m.x298 == 0)

m.c628 = Constraint(expr= - 0.25*m.x184 + m.x301 == 0)

m.c629 = Constraint(expr= - 0.25*m.x184 + m.x304 == 0)

m.c630 = Constraint(expr= - 0.25*m.x184 + m.x307 == 0)

m.c631 = Constraint(expr= - 0.25*m.x184 + m.x310 == 0)

m.c632 = Constraint(expr= - 0.25*m.x187 + m.x313 == 0)

m.c633 = Constraint(expr= - 0.25*m.x187 + m.x316 == 0)

m.c634 = Constraint(expr= - 0.25*m.x187 + m.x319 == 0)

m.c635 = Constraint(expr= - 0.25*m.x187 + m.x322 == 0)

m.c636 = Constraint(expr= - 0.222222222222222*m.x190 + m.x325 == 0)

m.c637 = Constraint(expr= - 0.222222222222222*m.x190 + m.x328 == 0)

m.c638 = Constraint(expr= - 0.222222222222222*m.x190 + m.x331 == 0)

m.c639 = Constraint(expr= - 0.333333333333333*m.x190 + m.x334 == 0)

m.c640 = Constraint(expr=   m.b1 + m.b121 <= 1)

m.c641 = Constraint(expr=   m.b2 + m.b122 <= 1)

m.c642 = Constraint(expr=   m.b3 + m.b123 <= 1)

m.c643 = Constraint(expr=   m.b4 + m.b148 <= 1)

m.c644 = Constraint(expr=   m.b5 + m.b149 <= 1)

m.c645 = Constraint(expr=   m.b6 + m.b150 <= 1)

m.c646 = Constraint(expr=   m.b7 + m.b151 <= 1)

m.c647 = Constraint(expr=   m.b8 + m.b152 <= 1)

m.c648 = Constraint(expr=   m.b9 + m.b153 <= 1)

m.c649 = Constraint(expr=   m.b10 + m.b154 <= 1)

m.c650 = Constraint(expr=   m.b11 + m.b155 <= 1)

m.c651 = Constraint(expr=   m.b12 + m.b156 <= 1)

m.c652 = Constraint(expr=   m.b13 + m.b121 <= 1)

m.c653 = Constraint(expr=   m.b14 + m.b122 <= 1)

m.c654 = Constraint(expr=   m.b15 + m.b123 <= 1)

m.c655 = Constraint(expr=   m.b16 + m.b148 <= 1)

m.c656 = Constraint(expr=   m.b17 + m.b149 <= 1)

m.c657 = Constraint(expr=   m.b18 + m.b150 <= 1)

m.c658 = Constraint(expr=   m.b19 + m.b151 <= 1)

m.c659 = Constraint(expr=   m.b20 + m.b152 <= 1)

m.c660 = Constraint(expr=   m.b21 + m.b153 <= 1)

m.c661 = Constraint(expr=   m.b22 + m.b154 <= 1)

m.c662 = Constraint(expr=   m.b23 + m.b155 <= 1)

m.c663 = Constraint(expr=   m.b24 + m.b156 <= 1)

m.c664 = Constraint(expr=   m.b25 + m.b121 <= 1)

m.c665 = Constraint(expr=   m.b26 + m.b122 <= 1)

m.c666 = Constraint(expr=   m.b27 + m.b123 <= 1)

m.c667 = Constraint(expr=   m.b28 + m.b148 <= 1)

m.c668 = Constraint(expr=   m.b29 + m.b149 <= 1)

m.c669 = Constraint(expr=   m.b30 + m.b150 <= 1)

m.c670 = Constraint(expr=   m.b31 + m.b151 <= 1)

m.c671 = Constraint(expr=   m.b32 + m.b152 <= 1)

m.c672 = Constraint(expr=   m.b33 + m.b153 <= 1)

m.c673 = Constraint(expr=   m.b34 + m.b154 <= 1)

m.c674 = Constraint(expr=   m.b35 + m.b155 <= 1)

m.c675 = Constraint(expr=   m.b36 + m.b156 <= 1)

m.c676 = Constraint(expr=   m.b37 + m.b124 <= 1)

m.c677 = Constraint(expr=   m.b38 + m.b125 <= 1)

m.c678 = Constraint(expr=   m.b39 + m.b126 <= 1)

m.c679 = Constraint(expr=   m.b37 + m.b127 <= 1)

m.c680 = Constraint(expr=   m.b38 + m.b128 <= 1)

m.c681 = Constraint(expr=   m.b39 + m.b129 <= 1)

m.c682 = Constraint(expr=   m.b40 + m.b130 <= 1)

m.c683 = Constraint(expr=   m.b41 + m.b131 <= 1)

m.c684 = Constraint(expr=   m.b42 + m.b132 <= 1)

m.c685 = Constraint(expr=   m.b40 + m.b133 <= 1)

m.c686 = Constraint(expr=   m.b41 + m.b134 <= 1)

m.c687 = Constraint(expr=   m.b42 + m.b135 <= 1)

m.c688 = Constraint(expr=   m.b43 + m.b136 <= 1)

m.c689 = Constraint(expr=   m.b44 + m.b137 <= 1)

m.c690 = Constraint(expr=   m.b45 + m.b138 <= 1)

m.c691 = Constraint(expr=   m.b43 + m.b139 <= 1)

m.c692 = Constraint(expr=   m.b44 + m.b140 <= 1)

m.c693 = Constraint(expr=   m.b45 + m.b141 <= 1)

m.c694 = Constraint(expr=   m.b46 + m.b142 <= 1)

m.c695 = Constraint(expr=   m.b47 + m.b143 <= 1)

m.c696 = Constraint(expr=   m.b48 + m.b144 <= 1)

m.c697 = Constraint(expr=   m.b46 + m.b145 <= 1)

m.c698 = Constraint(expr=   m.b47 + m.b146 <= 1)

m.c699 = Constraint(expr=   m.b48 + m.b147 <= 1)

m.c700 = Constraint(expr=   m.b49 + m.b124 <= 1)

m.c701 = Constraint(expr=   m.b50 + m.b125 <= 1)

m.c702 = Constraint(expr=   m.b51 + m.b126 <= 1)

m.c703 = Constraint(expr=   m.b49 + m.b127 <= 1)

m.c704 = Constraint(expr=   m.b50 + m.b128 <= 1)

m.c705 = Constraint(expr=   m.b51 + m.b129 <= 1)

m.c706 = Constraint(expr=   m.b52 + m.b130 <= 1)

m.c707 = Constraint(expr=   m.b53 + m.b131 <= 1)

m.c708 = Constraint(expr=   m.b54 + m.b132 <= 1)

m.c709 = Constraint(expr=   m.b52 + m.b133 <= 1)

m.c710 = Constraint(expr=   m.b53 + m.b134 <= 1)

m.c711 = Constraint(expr=   m.b54 + m.b135 <= 1)

m.c712 = Constraint(expr=   m.b55 + m.b136 <= 1)

m.c713 = Constraint(expr=   m.b56 + m.b137 <= 1)

m.c714 = Constraint(expr=   m.b57 + m.b138 <= 1)

m.c715 = Constraint(expr=   m.b55 + m.b139 <= 1)

m.c716 = Constraint(expr=   m.b56 + m.b140 <= 1)

m.c717 = Constraint(expr=   m.b57 + m.b141 <= 1)

m.c718 = Constraint(expr=   m.b58 + m.b142 <= 1)

m.c719 = Constraint(expr=   m.b59 + m.b143 <= 1)

m.c720 = Constraint(expr=   m.b60 + m.b144 <= 1)

m.c721 = Constraint(expr=   m.b58 + m.b145 <= 1)

m.c722 = Constraint(expr=   m.b59 + m.b146 <= 1)

m.c723 = Constraint(expr=   m.b60 + m.b147 <= 1)

m.c724 = Constraint(expr=   m.b61 + m.b124 <= 1)

m.c725 = Constraint(expr=   m.b62 + m.b125 <= 1)

m.c726 = Constraint(expr=   m.b63 + m.b126 <= 1)

m.c727 = Constraint(expr=   m.b61 + m.b127 <= 1)

m.c728 = Constraint(expr=   m.b62 + m.b128 <= 1)

m.c729 = Constraint(expr=   m.b63 + m.b129 <= 1)

m.c730 = Constraint(expr=   m.b64 + m.b130 <= 1)

m.c731 = Constraint(expr=   m.b65 + m.b131 <= 1)

m.c732 = Constraint(expr=   m.b66 + m.b132 <= 1)

m.c733 = Constraint(expr=   m.b64 + m.b133 <= 1)

m.c734 = Constraint(expr=   m.b65 + m.b134 <= 1)

m.c735 = Constraint(expr=   m.b66 + m.b135 <= 1)

m.c736 = Constraint(expr=   m.b67 + m.b136 <= 1)

m.c737 = Constraint(expr=   m.b68 + m.b137 <= 1)

m.c738 = Constraint(expr=   m.b69 + m.b138 <= 1)

m.c739 = Constraint(expr=   m.b67 + m.b139 <= 1)

m.c740 = Constraint(expr=   m.b68 + m.b140 <= 1)

m.c741 = Constraint(expr=   m.b69 + m.b141 <= 1)

m.c742 = Constraint(expr=   m.b70 + m.b142 <= 1)

m.c743 = Constraint(expr=   m.b71 + m.b143 <= 1)

m.c744 = Constraint(expr=   m.b72 + m.b144 <= 1)

m.c745 = Constraint(expr=   m.b70 + m.b145 <= 1)

m.c746 = Constraint(expr=   m.b71 + m.b146 <= 1)

m.c747 = Constraint(expr=   m.b72 + m.b147 <= 1)

m.c748 = Constraint(expr=   m.b73 + m.b121 <= 1)

m.c749 = Constraint(expr=   m.b74 + m.b122 <= 1)

m.c750 = Constraint(expr=   m.b75 + m.b123 <= 1)

m.c751 = Constraint(expr=   m.b76 + m.b148 <= 1)

m.c752 = Constraint(expr=   m.b77 + m.b149 <= 1)

m.c753 = Constraint(expr=   m.b78 + m.b150 <= 1)

m.c754 = Constraint(expr=   m.b79 + m.b151 <= 1)

m.c755 = Constraint(expr=   m.b80 + m.b152 <= 1)

m.c756 = Constraint(expr=   m.b81 + m.b153 <= 1)

m.c757 = Constraint(expr=   m.b82 + m.b154 <= 1)

m.c758 = Constraint(expr=   m.b83 + m.b155 <= 1)

m.c759 = Constraint(expr=   m.b84 + m.b156 <= 1)

m.c760 = Constraint(expr=   m.b85 + m.b124 <= 1)

m.c761 = Constraint(expr=   m.b86 + m.b125 <= 1)

m.c762 = Constraint(expr=   m.b87 + m.b126 <= 1)

m.c763 = Constraint(expr=   m.b85 + m.b127 <= 1)

m.c764 = Constraint(expr=   m.b86 + m.b128 <= 1)

m.c765 = Constraint(expr=   m.b87 + m.b129 <= 1)

m.c766 = Constraint(expr=   m.b88 + m.b130 <= 1)

m.c767 = Constraint(expr=   m.b89 + m.b131 <= 1)

m.c768 = Constraint(expr=   m.b90 + m.b132 <= 1)

m.c769 = Constraint(expr=   m.b88 + m.b133 <= 1)

m.c770 = Constraint(expr=   m.b89 + m.b134 <= 1)

m.c771 = Constraint(expr=   m.b90 + m.b135 <= 1)

m.c772 = Constraint(expr=   m.b91 + m.b136 <= 1)

m.c773 = Constraint(expr=   m.b92 + m.b137 <= 1)

m.c774 = Constraint(expr=   m.b93 + m.b138 <= 1)

m.c775 = Constraint(expr=   m.b91 + m.b139 <= 1)

m.c776 = Constraint(expr=   m.b92 + m.b140 <= 1)

m.c777 = Constraint(expr=   m.b93 + m.b141 <= 1)

m.c778 = Constraint(expr=   m.b94 + m.b142 <= 1)

m.c779 = Constraint(expr=   m.b95 + m.b143 <= 1)

m.c780 = Constraint(expr=   m.b96 + m.b144 <= 1)

m.c781 = Constraint(expr=   m.b94 + m.b145 <= 1)

m.c782 = Constraint(expr=   m.b95 + m.b146 <= 1)

m.c783 = Constraint(expr=   m.b96 + m.b147 <= 1)

m.c784 = Constraint(expr=   m.b121 <= 2)

m.c785 = Constraint(expr=   m.b122 <= 2)

m.c786 = Constraint(expr=   m.b123 <= 2)

m.c787 = Constraint(expr=   m.b124 + m.b127 <= 2)

m.c788 = Constraint(expr=   m.b125 + m.b128 <= 2)

m.c789 = Constraint(expr=   m.b126 + m.b129 <= 2)

m.c790 = Constraint(expr=   m.b130 + m.b133 <= 2)

m.c791 = Constraint(expr=   m.b131 + m.b134 <= 2)

m.c792 = Constraint(expr=   m.b132 + m.b135 <= 2)

m.c793 = Constraint(expr=   m.b136 + m.b139 <= 2)

m.c794 = Constraint(expr=   m.b137 + m.b140 <= 2)

m.c795 = Constraint(expr=   m.b138 + m.b141 <= 2)

m.c796 = Constraint(expr=   m.b142 + m.b145 <= 2)

m.c797 = Constraint(expr=   m.b143 + m.b146 <= 2)

m.c798 = Constraint(expr=   m.b144 + m.b147 <= 2)

m.c799 = Constraint(expr=   m.b148 <= 2)

m.c800 = Constraint(expr=   m.b149 <= 2)

m.c801 = Constraint(expr=   m.b150 <= 2)

m.c802 = Constraint(expr=   m.b151 <= 2)

m.c803 = Constraint(expr=   m.b152 <= 2)

m.c804 = Constraint(expr=   m.b153 <= 2)

m.c805 = Constraint(expr=   m.b154 <= 2)

m.c806 = Constraint(expr=   m.b155 <= 2)

m.c807 = Constraint(expr=   m.b156 <= 2)

m.c808 = Constraint(expr=   m.b124 + m.b130 + m.b136 + m.b142 <= 2)

m.c809 = Constraint(expr=   m.b125 + m.b131 + m.b137 + m.b143 <= 2)

m.c810 = Constraint(expr=   m.b126 + m.b132 + m.b138 + m.b144 <= 2)

m.c811 = Constraint(expr=   m.b127 + m.b133 + m.b139 + m.b145 <= 2)

m.c812 = Constraint(expr=   m.b128 + m.b134 + m.b140 + m.b146 <= 2)

m.c813 = Constraint(expr=   m.b129 + m.b135 + m.b141 + m.b147 <= 2)

m.c814 = Constraint(expr=   m.b121 + m.b148 + m.b151 + m.b154 <= 2)

m.c815 = Constraint(expr=   m.b122 + m.b149 + m.b152 + m.b155 <= 2)

m.c816 = Constraint(expr=   m.b123 + m.b150 + m.b153 + m.b156 <= 2)

m.c817 = Constraint(expr= - m.x157 - 2.5*m.x650 + 2.5*m.x686 <= 0)

m.c818 = Constraint(expr= - m.x158 - 2.5*m.x651 + 2.5*m.x687 <= 0)

m.c819 = Constraint(expr= - m.x159 - 2.5*m.x652 + 2.5*m.x688 <= 0)

m.c820 = Constraint(expr= - m.x160 - 2.5*m.x653 + 2.5*m.x689 <= 0)

m.c821 = Constraint(expr= - m.x161 - 2.5*m.x654 + 2.5*m.x690 <= 0)

m.c822 = Constraint(expr= - m.x162 - 2.5*m.x655 + 2.5*m.x691 <= 0)

m.c823 = Constraint(expr= - m.x163 - 2.5*m.x656 + 2.5*m.x692 <= 0)

m.c824 = Constraint(expr= - m.x164 - 2.5*m.x657 + 2.5*m.x693 <= 0)

m.c825 = Constraint(expr= - m.x165 - 2.5*m.x658 + 2.5*m.x694 <= 0)

m.c826 = Constraint(expr= - m.x166 - 2.5*m.x659 + 2.5*m.x695 <= 0)

m.c827 = Constraint(expr= - m.x167 - 2.5*m.x660 + 2.5*m.x696 <= 0)

m.c828 = Constraint(expr= - m.x168 - 2.5*m.x661 + 2.5*m.x697 <= 0)

m.c829 = Constraint(expr= - m.x169 - 2.5*m.x662 + 2.5*m.x698 <= 0)

m.c830 = Constraint(expr= - m.x170 - 2.5*m.x663 + 2.5*m.x699 <= 0)

m.c831 = Constraint(expr= - m.x171 - 2.5*m.x664 + 2.5*m.x700 <= 0)

m.c832 = Constraint(expr= - m.x172 - 2.5*m.x665 + 2.5*m.x701 <= 0)

m.c833 = Constraint(expr= - m.x173 - 2.5*m.x666 + 2.5*m.x702 <= 0)

m.c834 = Constraint(expr= - m.x174 - 2.5*m.x667 + 2.5*m.x703 <= 0)

m.c835 = Constraint(expr= - m.x175 - 2.5*m.x668 + 2.5*m.x704 <= 0)

m.c836 = Constraint(expr= - m.x176 - 2.5*m.x669 + 2.5*m.x705 <= 0)

m.c837 = Constraint(expr= - m.x177 - 2.5*m.x670 + 2.5*m.x706 <= 0)

m.c838 = Constraint(expr= - m.x178 - 2.5*m.x671 + 2.5*m.x707 <= 0)

m.c839 = Constraint(expr= - m.x179 - 2.5*m.x672 + 2.5*m.x708 <= 0)

m.c840 = Constraint(expr= - m.x180 - 2.5*m.x673 + 2.5*m.x709 <= 0)

m.c841 = Constraint(expr= - m.x181 - 2.5*m.x674 + 2.5*m.x710 <= 0)

m.c842 = Constraint(expr= - m.x182 - 2.5*m.x675 + 2.5*m.x711 <= 0)

m.c843 = Constraint(expr= - m.x183 - 2.5*m.x676 + 2.5*m.x712 <= 0)

m.c844 = Constraint(expr= - m.x184 - 2.5*m.x677 + 2.5*m.x713 <= 0)

m.c845 = Constraint(expr= - m.x185 - 2.5*m.x678 + 2.5*m.x714 <= 0)

m.c846 = Constraint(expr= - m.x186 - 2.5*m.x679 + 2.5*m.x715 <= 0)

m.c847 = Constraint(expr= - m.x187 - 2.5*m.x680 + 2.5*m.x716 <= 0)

m.c848 = Constraint(expr= - m.x188 - 2.5*m.x681 + 2.5*m.x717 <= 0)

m.c849 = Constraint(expr= - m.x189 - 2.5*m.x682 + 2.5*m.x718 <= 0)

m.c850 = Constraint(expr= - m.x190 - 2.5*m.x683 + 2.5*m.x719 <= 0)

m.c851 = Constraint(expr= - m.x191 - 2.5*m.x684 + 2.5*m.x720 <= 0)

m.c852 = Constraint(expr= - m.x192 - 2.5*m.x685 + 2.5*m.x721 <= 0)

m.c853 = Constraint(expr=   m.x157 + 5.625*m.x650 - 5.625*m.x686 <= 0)

m.c854 = Constraint(expr=   m.x158 + 5.625*m.x651 - 5.625*m.x687 <= 0)

m.c855 = Constraint(expr=   m.x159 + 5.625*m.x652 - 5.625*m.x688 <= 0)

m.c856 = Constraint(expr=   m.x160 + 5.625*m.x653 - 5.625*m.x689 <= 0)

m.c857 = Constraint(expr=   m.x161 + 5.625*m.x654 - 5.625*m.x690 <= 0)

m.c858 = Constraint(expr=   m.x162 + 5.625*m.x655 - 5.625*m.x691 <= 0)

m.c859 = Constraint(expr=   m.x163 + 5.625*m.x656 - 5.625*m.x692 <= 0)

m.c860 = Constraint(expr=   m.x164 + 5.625*m.x657 - 5.625*m.x693 <= 0)

m.c861 = Constraint(expr=   m.x165 + 5.625*m.x658 - 5.625*m.x694 <= 0)

m.c862 = Constraint(expr=   m.x166 + 5.625*m.x659 - 5.625*m.x695 <= 0)

m.c863 = Constraint(expr=   m.x167 + 5.625*m.x660 - 5.625*m.x696 <= 0)

m.c864 = Constraint(expr=   m.x168 + 5.625*m.x661 - 5.625*m.x697 <= 0)

m.c865 = Constraint(expr=   m.x169 + 5.625*m.x662 - 5.625*m.x698 <= 0)

m.c866 = Constraint(expr=   m.x170 + 5.625*m.x663 - 5.625*m.x699 <= 0)

m.c867 = Constraint(expr=   m.x171 + 5.625*m.x664 - 5.625*m.x700 <= 0)

m.c868 = Constraint(expr=   m.x172 + 5.625*m.x665 - 5.625*m.x701 <= 0)

m.c869 = Constraint(expr=   m.x173 + 5.625*m.x666 - 5.625*m.x702 <= 0)

m.c870 = Constraint(expr=   m.x174 + 5.625*m.x667 - 5.625*m.x703 <= 0)

m.c871 = Constraint(expr=   m.x175 + 5.625*m.x668 - 5.625*m.x704 <= 0)

m.c872 = Constraint(expr=   m.x176 + 5.625*m.x669 - 5.625*m.x705 <= 0)

m.c873 = Constraint(expr=   m.x177 + 5.625*m.x670 - 5.625*m.x706 <= 0)

m.c874 = Constraint(expr=   m.x178 + 5.625*m.x671 - 5.625*m.x707 <= 0)

m.c875 = Constraint(expr=   m.x179 + 5.625*m.x672 - 5.625*m.x708 <= 0)

m.c876 = Constraint(expr=   m.x180 + 5.625*m.x673 - 5.625*m.x709 <= 0)

m.c877 = Constraint(expr=   m.x181 + 5.625*m.x674 - 5.625*m.x710 <= 0)

m.c878 = Constraint(expr=   m.x182 + 5.625*m.x675 - 5.625*m.x711 <= 0)

m.c879 = Constraint(expr=   m.x183 + 5.625*m.x676 - 5.625*m.x712 <= 0)

m.c880 = Constraint(expr=   m.x184 + 5.625*m.x677 - 5.625*m.x713 <= 0)

m.c881 = Constraint(expr=   m.x185 + 5.625*m.x678 - 5.625*m.x714 <= 0)

m.c882 = Constraint(expr=   m.x186 + 5.625*m.x679 - 5.625*m.x715 <= 0)

m.c883 = Constraint(expr=   m.x187 + 5.625*m.x680 - 5.625*m.x716 <= 0)

m.c884 = Constraint(expr=   m.x188 + 5.625*m.x681 - 5.625*m.x717 <= 0)

m.c885 = Constraint(expr=   m.x189 + 5.625*m.x682 - 5.625*m.x718 <= 0)

m.c886 = Constraint(expr=   m.x190 + 5.625*m.x683 - 5.625*m.x719 <= 0)

m.c887 = Constraint(expr=   m.x191 + 5.625*m.x684 - 5.625*m.x720 <= 0)

m.c888 = Constraint(expr=   m.x192 + 5.625*m.x685 - 5.625*m.x721 <= 0)

m.c889 = Constraint(expr= - 290*m.b121 + m.x157 <= 0)

m.c890 = Constraint(expr= - 510*m.b122 + m.x158 <= 0)

m.c891 = Constraint(expr= - 510*m.b123 + m.x159 <= 0)

m.c892 = Constraint(expr= - 340*m.b124 + m.x160 <= 0)

m.c893 = Constraint(expr= - 510*m.b125 + m.x161 <= 0)

m.c894 = Constraint(expr= - 510*m.b126 + m.x162 <= 0)

m.c895 = Constraint(expr= - 340*m.b127 + m.x163 <= 0)

m.c896 = Constraint(expr= - 510*m.b128 + m.x164 <= 0)

m.c897 = Constraint(expr= - 510*m.b129 + m.x165 <= 0)

m.c898 = Constraint(expr= - 290*m.b130 + m.x166 <= 0)

m.c899 = Constraint(expr= - 510*m.b131 + m.x167 <= 0)

m.c900 = Constraint(expr= - 510*m.b132 + m.x168 <= 0)

m.c901 = Constraint(expr= - 290*m.b133 + m.x169 <= 0)

m.c902 = Constraint(expr= - 510*m.b134 + m.x170 <= 0)

m.c903 = Constraint(expr= - 510*m.b135 + m.x171 <= 0)

m.c904 = Constraint(expr= - 840*m.b136 + m.x172 <= 0)

m.c905 = Constraint(expr= - 870*m.b137 + m.x173 <= 0)

m.c906 = Constraint(expr= - 870*m.b138 + m.x174 <= 0)

m.c907 = Constraint(expr= - 840*m.b139 + m.x175 <= 0)

m.c908 = Constraint(expr= - 870*m.b140 + m.x176 <= 0)

m.c909 = Constraint(expr= - 870*m.b141 + m.x177 <= 0)

m.c910 = Constraint(expr= - 190*m.b142 + m.x178 <= 0)

m.c911 = Constraint(expr= - 870*m.b143 + m.x179 <= 0)

m.c912 = Constraint(expr= - 870*m.b144 + m.x180 <= 0)

m.c913 = Constraint(expr= - 190*m.b145 + m.x181 <= 0)

m.c914 = Constraint(expr= - 870*m.b146 + m.x182 <= 0)

m.c915 = Constraint(expr= - 870*m.b147 + m.x183 <= 0)

m.c916 = Constraint(expr= - 20*m.b148 + m.x184 <= 0)

m.c917 = Constraint(expr= - 830*m.b149 + m.x185 <= 0)

m.c918 = Constraint(expr= - 920*m.b150 + m.x186 <= 0)

m.c919 = Constraint(expr= - 20*m.b151 + m.x187 <= 0)

m.c920 = Constraint(expr= - 510*m.b152 + m.x188 <= 0)

m.c921 = Constraint(expr= - 510*m.b153 + m.x189 <= 0)

m.c922 = Constraint(expr= - 390*m.b154 + m.x190 <= 0)

m.c923 = Constraint(expr= - 510*m.b155 + m.x191 <= 0)

m.c924 = Constraint(expr= - 510*m.b156 + m.x192 <= 0)

m.c925 = Constraint(expr=   m.x157 - m.x193 - m.x196 - m.x199 - m.x202 == 0)

m.c926 = Constraint(expr=   m.x158 - m.x194 - m.x197 - m.x200 - m.x203 == 0)

m.c927 = Constraint(expr=   m.x159 - m.x195 - m.x198 - m.x201 - m.x204 == 0)

m.c928 = Constraint(expr=   m.x160 - m.x205 - m.x208 - m.x211 - m.x214 == 0)

m.c929 = Constraint(expr=   m.x161 - m.x206 - m.x209 - m.x212 - m.x215 == 0)

m.c930 = Constraint(expr=   m.x162 - m.x207 - m.x210 - m.x213 - m.x216 == 0)

m.c931 = Constraint(expr=   m.x163 - m.x217 - m.x220 - m.x223 - m.x226 == 0)

m.c932 = Constraint(expr=   m.x164 - m.x218 - m.x221 - m.x224 - m.x227 == 0)

m.c933 = Constraint(expr=   m.x165 - m.x219 - m.x222 - m.x225 - m.x228 == 0)

m.c934 = Constraint(expr=   m.x166 - m.x229 - m.x232 - m.x235 - m.x238 == 0)

m.c935 = Constraint(expr=   m.x167 - m.x230 - m.x233 - m.x236 - m.x239 == 0)

m.c936 = Constraint(expr=   m.x168 - m.x231 - m.x234 - m.x237 - m.x240 == 0)

m.c937 = Constraint(expr=   m.x169 - m.x241 - m.x244 - m.x247 - m.x250 == 0)

m.c938 = Constraint(expr=   m.x170 - m.x242 - m.x245 - m.x248 - m.x251 == 0)

m.c939 = Constraint(expr=   m.x171 - m.x243 - m.x246 - m.x249 - m.x252 == 0)

m.c940 = Constraint(expr=   m.x172 - m.x253 - m.x256 - m.x259 - m.x262 == 0)

m.c941 = Constraint(expr=   m.x173 - m.x254 - m.x257 - m.x260 - m.x263 == 0)

m.c942 = Constraint(expr=   m.x174 - m.x255 - m.x258 - m.x261 - m.x264 == 0)

m.c943 = Constraint(expr=   m.x175 - m.x265 - m.x268 - m.x271 - m.x274 == 0)

m.c944 = Constraint(expr=   m.x176 - m.x266 - m.x269 - m.x272 - m.x275 == 0)

m.c945 = Constraint(expr=   m.x177 - m.x267 - m.x270 - m.x273 - m.x276 == 0)

m.c946 = Constraint(expr=   m.x178 - m.x277 - m.x280 - m.x283 - m.x286 == 0)

m.c947 = Constraint(expr=   m.x179 - m.x278 - m.x281 - m.x284 - m.x287 == 0)

m.c948 = Constraint(expr=   m.x180 - m.x279 - m.x282 - m.x285 - m.x288 == 0)

m.c949 = Constraint(expr=   m.x181 - m.x289 - m.x292 - m.x295 - m.x298 == 0)

m.c950 = Constraint(expr=   m.x182 - m.x290 - m.x293 - m.x296 - m.x299 == 0)

m.c951 = Constraint(expr=   m.x183 - m.x291 - m.x294 - m.x297 - m.x300 == 0)

m.c952 = Constraint(expr=   m.x184 - m.x301 - m.x304 - m.x307 - m.x310 == 0)

m.c953 = Constraint(expr=   m.x185 - m.x302 - m.x305 - m.x308 - m.x311 == 0)

m.c954 = Constraint(expr=   m.x186 - m.x303 - m.x306 - m.x309 - m.x312 == 0)

m.c955 = Constraint(expr=   m.x187 - m.x313 - m.x316 - m.x319 - m.x322 == 0)

m.c956 = Constraint(expr=   m.x188 - m.x314 - m.x317 - m.x320 - m.x323 == 0)

m.c957 = Constraint(expr=   m.x189 - m.x315 - m.x318 - m.x321 - m.x324 == 0)

m.c958 = Constraint(expr=   m.x190 - m.x325 - m.x328 - m.x331 - m.x334 == 0)

m.c959 = Constraint(expr=   m.x191 - m.x326 - m.x329 - m.x332 - m.x335 == 0)

m.c960 = Constraint(expr=   m.x192 - m.x327 - m.x330 - m.x333 - m.x336 == 0)

m.c961 = Constraint(expr= - m.x160 - m.x166 - m.x172 - m.x178 + m.x337 == 0)

m.c962 = Constraint(expr= - m.x161 - m.x167 - m.x173 - m.x179 + m.x338 == 0)

m.c963 = Constraint(expr= - m.x162 - m.x168 - m.x174 - m.x180 + m.x339 == 0)

m.c964 = Constraint(expr= - m.x163 - m.x169 - m.x175 - m.x181 + m.x340 == 0)

m.c965 = Constraint(expr= - m.x164 - m.x170 - m.x176 - m.x182 + m.x341 == 0)

m.c966 = Constraint(expr= - m.x165 - m.x171 - m.x177 - m.x183 + m.x342 == 0)

m.c967 = Constraint(expr= - m.x157 - m.x184 - m.x187 - m.x190 + m.x343 == 0)

m.c968 = Constraint(expr= - m.x158 - m.x185 - m.x188 - m.x191 + m.x344 == 0)

m.c969 = Constraint(expr= - m.x159 - m.x186 - m.x189 - m.x192 + m.x345 == 0)

m.c970 = Constraint(expr= - m.x337 - 2.5*m.x722 + 2.5*m.x731 <= 0)

m.c971 = Constraint(expr= - m.x338 - 2.5*m.x723 + 2.5*m.x732 <= 0)

m.c972 = Constraint(expr= - m.x339 - 2.5*m.x724 + 2.5*m.x733 <= 0)

m.c973 = Constraint(expr= - m.x340 - 2.5*m.x725 + 2.5*m.x734 <= 0)

m.c974 = Constraint(expr= - m.x341 - 2.5*m.x726 + 2.5*m.x735 <= 0)

m.c975 = Constraint(expr= - m.x342 - 2.5*m.x727 + 2.5*m.x736 <= 0)

m.c976 = Constraint(expr= - m.x343 - 2.5*m.x728 + 2.5*m.x737 <= 0)

m.c977 = Constraint(expr= - m.x344 - 2.5*m.x729 + 2.5*m.x738 <= 0)

m.c978 = Constraint(expr= - m.x345 - 2.5*m.x730 + 2.5*m.x739 <= 0)

m.c979 = Constraint(expr=   m.x337 + 5.625*m.x722 - 5.625*m.x731 <= 0)

m.c980 = Constraint(expr=   m.x338 + 5.625*m.x723 - 5.625*m.x732 <= 0)

m.c981 = Constraint(expr=   m.x339 + 5.625*m.x724 - 5.625*m.x733 <= 0)

m.c982 = Constraint(expr=   m.x340 + 5.625*m.x725 - 5.625*m.x734 <= 0)

m.c983 = Constraint(expr=   m.x341 + 5.625*m.x726 - 5.625*m.x735 <= 0)

m.c984 = Constraint(expr=   m.x342 + 5.625*m.x727 - 5.625*m.x736 <= 0)

m.c985 = Constraint(expr=   m.x343 + 5.625*m.x728 - 5.625*m.x737 <= 0)

m.c986 = Constraint(expr=   m.x344 + 5.625*m.x729 - 5.625*m.x738 <= 0)

m.c987 = Constraint(expr=   m.x345 + 5.625*m.x730 - 5.625*m.x739 <= 0)

m.c988 = Constraint(expr= - m.x193 - m.x301 - m.x313 - m.x325 + 0.15*m.x343 <= 0)

m.c989 = Constraint(expr= - m.x194 - m.x302 - m.x314 - m.x326 + 0.15*m.x344 <= 0)

m.c990 = Constraint(expr= - m.x195 - m.x303 - m.x315 - m.x327 + 0.15*m.x345 <= 0)

m.c991 = Constraint(expr=   m.x193 + m.x301 + m.x313 + m.x325 - 0.85*m.x343 <= 0)

m.c992 = Constraint(expr=   m.x194 + m.x302 + m.x314 + m.x326 - 0.85*m.x344 <= 0)

m.c993 = Constraint(expr=   m.x195 + m.x303 + m.x315 + m.x327 - 0.85*m.x345 <= 0)

m.c994 = Constraint(expr=   0.001*m.x160 + 0.001*m.x166 + 0.001*m.x172 + 0.001*m.x178 - 0.012*m.x205 - 0.013*m.x208
                          - 0.009*m.x211 - 0.015*m.x214 - 0.012*m.x229 - 0.013*m.x232 - 0.009*m.x235 - 0.015*m.x238
                          - 0.012*m.x253 - 0.013*m.x256 - 0.009*m.x259 - 0.015*m.x262 - 0.012*m.x277 - 0.013*m.x280
                          - 0.009*m.x283 - 0.015*m.x286 <= 0)

m.c995 = Constraint(expr=   0.001*m.x161 + 0.001*m.x167 + 0.001*m.x173 + 0.001*m.x179 - 0.012*m.x206 - 0.013*m.x209
                          - 0.009*m.x212 - 0.015*m.x215 - 0.012*m.x230 - 0.013*m.x233 - 0.009*m.x236 - 0.015*m.x239
                          - 0.012*m.x254 - 0.013*m.x257 - 0.009*m.x260 - 0.015*m.x263 - 0.012*m.x278 - 0.013*m.x281
                          - 0.009*m.x284 - 0.015*m.x287 <= 0)

m.c996 = Constraint(expr=   0.001*m.x162 + 0.001*m.x168 + 0.001*m.x174 + 0.001*m.x180 - 0.012*m.x207 - 0.013*m.x210
                          - 0.009*m.x213 - 0.015*m.x216 - 0.012*m.x231 - 0.013*m.x234 - 0.009*m.x237 - 0.015*m.x240
                          - 0.012*m.x255 - 0.013*m.x258 - 0.009*m.x261 - 0.015*m.x264 - 0.012*m.x279 - 0.013*m.x282
                          - 0.009*m.x285 - 0.015*m.x288 <= 0)

m.c997 = Constraint(expr=   0.001*m.x163 + 0.001*m.x169 + 0.001*m.x175 + 0.001*m.x181 - 0.012*m.x217 - 0.013*m.x220
                          - 0.009*m.x223 - 0.015*m.x226 - 0.012*m.x241 - 0.013*m.x244 - 0.009*m.x247 - 0.015*m.x250
                          - 0.012*m.x265 - 0.013*m.x268 - 0.009*m.x271 - 0.015*m.x274 - 0.012*m.x289 - 0.013*m.x292
                          - 0.009*m.x295 - 0.015*m.x298 <= 0)

m.c998 = Constraint(expr=   0.001*m.x164 + 0.001*m.x170 + 0.001*m.x176 + 0.001*m.x182 - 0.012*m.x218 - 0.013*m.x221
                          - 0.009*m.x224 - 0.015*m.x227 - 0.012*m.x242 - 0.013*m.x245 - 0.009*m.x248 - 0.015*m.x251
                          - 0.012*m.x266 - 0.013*m.x269 - 0.009*m.x272 - 0.015*m.x275 - 0.012*m.x290 - 0.013*m.x293
                          - 0.009*m.x296 - 0.015*m.x299 <= 0)

m.c999 = Constraint(expr=   0.001*m.x165 + 0.001*m.x171 + 0.001*m.x177 + 0.001*m.x183 - 0.012*m.x219 - 0.013*m.x222
                          - 0.009*m.x225 - 0.015*m.x228 - 0.012*m.x243 - 0.013*m.x246 - 0.009*m.x249 - 0.015*m.x252
                          - 0.012*m.x267 - 0.013*m.x270 - 0.009*m.x273 - 0.015*m.x276 - 0.012*m.x291 - 0.013*m.x294
                          - 0.009*m.x297 - 0.015*m.x300 <= 0)

m.c1000 = Constraint(expr=   0.001*m.x157 + 0.001*m.x184 + 0.001*m.x187 + 0.001*m.x190 - 0.002*m.x193 - 0.0025*m.x196
                           - 0.0015*m.x199 - 0.006*m.x202 - 0.002*m.x301 - 0.0025*m.x304 - 0.0015*m.x307 - 0.006*m.x310
                           - 0.002*m.x313 - 0.0025*m.x316 - 0.0015*m.x319 - 0.006*m.x322 - 0.002*m.x325 - 0.0025*m.x328
                           - 0.0015*m.x331 - 0.006*m.x334 <= 0)

m.c1001 = Constraint(expr=   0.001*m.x158 + 0.001*m.x185 + 0.001*m.x188 + 0.001*m.x191 - 0.002*m.x194 - 0.0025*m.x197
                           - 0.0015*m.x200 - 0.006*m.x203 - 0.002*m.x302 - 0.0025*m.x305 - 0.0015*m.x308 - 0.006*m.x311
                           - 0.002*m.x314 - 0.0025*m.x317 - 0.0015*m.x320 - 0.006*m.x323 - 0.002*m.x326 - 0.0025*m.x329
                           - 0.0015*m.x332 - 0.006*m.x335 <= 0)

m.c1002 = Constraint(expr=   0.001*m.x159 + 0.001*m.x186 + 0.001*m.x189 + 0.001*m.x192 - 0.002*m.x195 - 0.0025*m.x198
                           - 0.0015*m.x201 - 0.006*m.x204 - 0.002*m.x303 - 0.0025*m.x306 - 0.0015*m.x309 - 0.006*m.x312
                           - 0.002*m.x315 - 0.0025*m.x318 - 0.0015*m.x321 - 0.006*m.x324 - 0.002*m.x327 - 0.0025*m.x330
                           - 0.0015*m.x333 - 0.006*m.x336 <= 0)

m.c1003 = Constraint(expr= - 0.013*m.x160 - 0.013*m.x166 - 0.013*m.x172 - 0.013*m.x178 + 0.012*m.x205 + 0.013*m.x208
                           + 0.009*m.x211 + 0.015*m.x214 + 0.012*m.x229 + 0.013*m.x232 + 0.009*m.x235 + 0.015*m.x238
                           + 0.012*m.x253 + 0.013*m.x256 + 0.009*m.x259 + 0.015*m.x262 + 0.012*m.x277 + 0.013*m.x280
                           + 0.009*m.x283 + 0.015*m.x286 <= 0)

m.c1004 = Constraint(expr= - 0.013*m.x161 - 0.013*m.x167 - 0.013*m.x173 - 0.013*m.x179 + 0.012*m.x206 + 0.013*m.x209
                           + 0.009*m.x212 + 0.015*m.x215 + 0.012*m.x230 + 0.013*m.x233 + 0.009*m.x236 + 0.015*m.x239
                           + 0.012*m.x254 + 0.013*m.x257 + 0.009*m.x260 + 0.015*m.x263 + 0.012*m.x278 + 0.013*m.x281
                           + 0.009*m.x284 + 0.015*m.x287 <= 0)

m.c1005 = Constraint(expr= - 0.013*m.x162 - 0.013*m.x168 - 0.013*m.x174 - 0.013*m.x180 + 0.012*m.x207 + 0.013*m.x210
                           + 0.009*m.x213 + 0.015*m.x216 + 0.012*m.x231 + 0.013*m.x234 + 0.009*m.x237 + 0.015*m.x240
                           + 0.012*m.x255 + 0.013*m.x258 + 0.009*m.x261 + 0.015*m.x264 + 0.012*m.x279 + 0.013*m.x282
                           + 0.009*m.x285 + 0.015*m.x288 <= 0)

m.c1006 = Constraint(expr= - 0.0125*m.x163 - 0.0125*m.x169 - 0.0125*m.x175 - 0.0125*m.x181 + 0.012*m.x217 + 0.013*m.x220
                           + 0.009*m.x223 + 0.015*m.x226 + 0.012*m.x241 + 0.013*m.x244 + 0.009*m.x247 + 0.015*m.x250
                           + 0.012*m.x265 + 0.013*m.x268 + 0.009*m.x271 + 0.015*m.x274 + 0.012*m.x289 + 0.013*m.x292
                           + 0.009*m.x295 + 0.015*m.x298 <= 0)

m.c1007 = Constraint(expr= - 0.0125*m.x164 - 0.0125*m.x170 - 0.0125*m.x176 - 0.0125*m.x182 + 0.012*m.x218 + 0.013*m.x221
                           + 0.009*m.x224 + 0.015*m.x227 + 0.012*m.x242 + 0.013*m.x245 + 0.009*m.x248 + 0.015*m.x251
                           + 0.012*m.x266 + 0.013*m.x269 + 0.009*m.x272 + 0.015*m.x275 + 0.012*m.x290 + 0.013*m.x293
                           + 0.009*m.x296 + 0.015*m.x299 <= 0)

m.c1008 = Constraint(expr= - 0.0125*m.x165 - 0.0125*m.x171 - 0.0125*m.x177 - 0.0125*m.x183 + 0.012*m.x219 + 0.013*m.x222
                           + 0.009*m.x225 + 0.015*m.x228 + 0.012*m.x243 + 0.013*m.x246 + 0.009*m.x249 + 0.015*m.x252
                           + 0.012*m.x267 + 0.013*m.x270 + 0.009*m.x273 + 0.015*m.x276 + 0.012*m.x291 + 0.013*m.x294
                           + 0.009*m.x297 + 0.015*m.x300 <= 0)

m.c1009 = Constraint(expr= - 0.0035*m.x157 - 0.0035*m.x184 - 0.0035*m.x187 - 0.0035*m.x190 + 0.002*m.x193
                           + 0.0025*m.x196 + 0.0015*m.x199 + 0.006*m.x202 + 0.002*m.x301 + 0.0025*m.x304 + 0.0015*m.x307
                           + 0.006*m.x310 + 0.002*m.x313 + 0.0025*m.x316 + 0.0015*m.x319 + 0.006*m.x322 + 0.002*m.x325
                           + 0.0025*m.x328 + 0.0015*m.x331 + 0.006*m.x334 <= 0)

m.c1010 = Constraint(expr= - 0.0035*m.x158 - 0.0035*m.x185 - 0.0035*m.x188 - 0.0035*m.x191 + 0.002*m.x194
                           + 0.0025*m.x197 + 0.0015*m.x200 + 0.006*m.x203 + 0.002*m.x302 + 0.0025*m.x305 + 0.0015*m.x308
                           + 0.006*m.x311 + 0.002*m.x314 + 0.0025*m.x317 + 0.0015*m.x320 + 0.006*m.x323 + 0.002*m.x326
                           + 0.0025*m.x329 + 0.0015*m.x332 + 0.006*m.x335 <= 0)

m.c1011 = Constraint(expr= - 0.0035*m.x159 - 0.0035*m.x186 - 0.0035*m.x189 - 0.0035*m.x192 + 0.002*m.x195
                           + 0.0025*m.x198 + 0.0015*m.x201 + 0.006*m.x204 + 0.002*m.x303 + 0.0025*m.x306 + 0.0015*m.x309
                           + 0.006*m.x312 + 0.002*m.x315 + 0.0025*m.x318 + 0.0015*m.x321 + 0.006*m.x324 + 0.002*m.x327
                           + 0.0025*m.x330 + 0.0015*m.x333 + 0.006*m.x336 <= 0)

m.c1012 = Constraint(expr=   m.x337 + m.x338 + m.x339 == 750)

m.c1013 = Constraint(expr=   m.x340 + m.x341 + m.x342 == 750)

m.c1014 = Constraint(expr=   m.x343 + m.x344 + m.x345 == 750)

m.c1015 = Constraint(expr=   m.x459 - m.x554 >= 0)

m.c1016 = Constraint(expr=   m.x460 - m.x555 >= 0)

m.c1017 = Constraint(expr=   m.x462 - m.x557 >= 0)

m.c1018 = Constraint(expr=   m.x463 - m.x558 >= 0)

m.c1019 = Constraint(expr=   m.x465 - m.x560 >= 0)

m.c1020 = Constraint(expr=   m.x466 - m.x561 >= 0)

m.c1021 = Constraint(expr=   m.x468 - m.x563 >= 0)

m.c1022 = Constraint(expr=   m.x469 - m.x564 >= 0)

m.c1023 = Constraint(expr=   m.x471 - m.x566 >= 0)

m.c1024 = Constraint(expr=   m.x472 - m.x567 >= 0)

m.c1025 = Constraint(expr=   m.x474 - m.x569 >= 0)

m.c1026 = Constraint(expr=   m.x475 - m.x570 >= 0)

m.c1027 = Constraint(expr=   m.x477 - m.x572 >= 0)

m.c1028 = Constraint(expr=   m.x478 - m.x573 >= 0)

m.c1029 = Constraint(expr=   m.x480 - m.x575 >= 0)

m.c1030 = Constraint(expr=   m.x481 - m.x576 >= 0)

m.c1031 = Constraint(expr=   m.x483 - m.x578 >= 0)

m.c1032 = Constraint(expr=   m.x484 - m.x579 >= 0)

m.c1033 = Constraint(expr=   m.x486 - m.x581 >= 0)

m.c1034 = Constraint(expr=   m.x487 - m.x582 >= 0)

m.c1035 = Constraint(expr=   m.x489 - m.x584 >= 0)

m.c1036 = Constraint(expr=   m.x490 - m.x585 >= 0)

m.c1037 = Constraint(expr=   m.x492 - m.x587 >= 0)

m.c1038 = Constraint(expr=   m.x493 - m.x588 >= 0)

m.c1039 = Constraint(expr=   m.x495 - m.x590 >= 0)

m.c1040 = Constraint(expr=   m.x496 - m.x591 >= 0)

m.c1041 = Constraint(expr=   m.x498 - m.x593 >= 0)

m.c1042 = Constraint(expr=   m.x499 - m.x594 >= 0)

m.c1043 = Constraint(expr=   m.x501 - m.x596 >= 0)

m.c1044 = Constraint(expr=   m.x502 - m.x597 >= 0)

m.c1045 = Constraint(expr=   m.x504 - m.x599 >= 0)

m.c1046 = Constraint(expr=   m.x505 - m.x600 >= 0)

m.c1047 = Constraint(expr=   m.x507 - m.x602 >= 0)

m.c1048 = Constraint(expr=   m.x508 - m.x603 >= 0)

m.c1049 = Constraint(expr=   m.x510 - m.x605 >= 0)

m.c1050 = Constraint(expr=   m.x511 - m.x606 >= 0)

m.c1051 = Constraint(expr=   m.x513 - m.x608 >= 0)

m.c1052 = Constraint(expr=   m.x514 - m.x609 >= 0)

m.c1053 = Constraint(expr=   m.x516 - m.x611 >= 0)

m.c1054 = Constraint(expr=   m.x517 - m.x612 >= 0)

m.c1055 = Constraint(expr=   m.x519 - m.x614 >= 0)

m.c1056 = Constraint(expr=   m.x520 - m.x615 >= 0)

m.c1057 = Constraint(expr=   m.x522 - m.x617 >= 0)

m.c1058 = Constraint(expr=   m.x523 - m.x618 >= 0)

m.c1059 = Constraint(expr=   m.x525 - m.x620 >= 0)

m.c1060 = Constraint(expr=   m.x526 - m.x621 >= 0)

m.c1061 = Constraint(expr=   m.x528 - m.x623 >= 0)

m.c1062 = Constraint(expr=   m.x529 - m.x624 >= 0)

m.c1063 = Constraint(expr=   m.x531 - m.x626 >= 0)

m.c1064 = Constraint(expr=   m.x532 - m.x627 >= 0)

m.c1065 = Constraint(expr=   m.x534 - m.x629 >= 0)

m.c1066 = Constraint(expr=   m.x535 - m.x630 >= 0)

m.c1067 = Constraint(expr=   m.x537 - m.x632 >= 0)

m.c1068 = Constraint(expr=   m.x538 - m.x633 >= 0)

m.c1069 = Constraint(expr=   m.x540 - m.x635 >= 0)

m.c1070 = Constraint(expr=   m.x541 - m.x636 >= 0)

m.c1071 = Constraint(expr=   m.x543 - m.x638 >= 0)

m.c1072 = Constraint(expr=   m.x544 - m.x639 >= 0)

m.c1073 = Constraint(expr=   m.x546 - m.x641 >= 0)

m.c1074 = Constraint(expr=   m.x547 - m.x642 >= 0)

m.c1075 = Constraint(expr=   m.x549 - m.x644 >= 0)

m.c1076 = Constraint(expr=   m.x550 - m.x645 >= 0)

m.c1077 = Constraint(expr=   m.x552 - m.x647 >= 0)

m.c1078 = Constraint(expr=   m.x553 - m.x648 >= 0)

m.c1079 = Constraint(expr= - 160*m.b1 + m.x462 - m.x554 >= -160)

m.c1080 = Constraint(expr= - 160*m.b2 + m.x463 - m.x555 >= -160)

m.c1081 = Constraint(expr= - 160*m.b1 + m.x465 - m.x554 >= -160)

m.c1082 = Constraint(expr= - 160*m.b2 + m.x466 - m.x555 >= -160)

m.c1083 = Constraint(expr= - 160*m.b1 + m.x468 - m.x554 >= -160)

m.c1084 = Constraint(expr= - 160*m.b2 + m.x469 - m.x555 >= -160)

m.c1085 = Constraint(expr= - 160*m.b4 + m.x459 - m.x557 >= -160)

m.c1086 = Constraint(expr= - 160*m.b5 + m.x460 - m.x558 >= -160)

m.c1087 = Constraint(expr= - 160*m.b4 + m.x465 - m.x557 >= -160)

m.c1088 = Constraint(expr= - 160*m.b5 + m.x466 - m.x558 >= -160)

m.c1089 = Constraint(expr= - 160*m.b4 + m.x468 - m.x557 >= -160)

m.c1090 = Constraint(expr= - 160*m.b5 + m.x469 - m.x558 >= -160)

m.c1091 = Constraint(expr= - 160*m.b7 + m.x459 - m.x560 >= -160)

m.c1092 = Constraint(expr= - 160*m.b8 + m.x460 - m.x561 >= -160)

m.c1093 = Constraint(expr= - 160*m.b7 + m.x462 - m.x560 >= -160)

m.c1094 = Constraint(expr= - 160*m.b8 + m.x463 - m.x561 >= -160)

m.c1095 = Constraint(expr= - 160*m.b7 + m.x468 - m.x560 >= -160)

m.c1096 = Constraint(expr= - 160*m.b8 + m.x469 - m.x561 >= -160)

m.c1097 = Constraint(expr= - 160*m.b10 + m.x459 - m.x563 >= -160)

m.c1098 = Constraint(expr= - 160*m.b11 + m.x460 - m.x564 >= -160)

m.c1099 = Constraint(expr= - 160*m.b10 + m.x462 - m.x563 >= -160)

m.c1100 = Constraint(expr= - 160*m.b11 + m.x463 - m.x564 >= -160)

m.c1101 = Constraint(expr= - 160*m.b10 + m.x465 - m.x563 >= -160)

m.c1102 = Constraint(expr= - 160*m.b11 + m.x466 - m.x564 >= -160)

m.c1103 = Constraint(expr= - 160*m.b13 + m.x474 - m.x566 >= -160)

m.c1104 = Constraint(expr= - 160*m.b14 + m.x475 - m.x567 >= -160)

m.c1105 = Constraint(expr= - 160*m.b13 + m.x477 - m.x566 >= -160)

m.c1106 = Constraint(expr= - 160*m.b14 + m.x478 - m.x567 >= -160)

m.c1107 = Constraint(expr= - 160*m.b13 + m.x480 - m.x566 >= -160)

m.c1108 = Constraint(expr= - 160*m.b14 + m.x481 - m.x567 >= -160)

m.c1109 = Constraint(expr= - 160*m.b16 + m.x471 - m.x569 >= -160)

m.c1110 = Constraint(expr= - 160*m.b17 + m.x472 - m.x570 >= -160)

m.c1111 = Constraint(expr= - 160*m.b16 + m.x477 - m.x569 >= -160)

m.c1112 = Constraint(expr= - 160*m.b17 + m.x478 - m.x570 >= -160)

m.c1113 = Constraint(expr= - 160*m.b16 + m.x480 - m.x569 >= -160)

m.c1114 = Constraint(expr= - 160*m.b17 + m.x481 - m.x570 >= -160)

m.c1115 = Constraint(expr= - 160*m.b19 + m.x471 - m.x572 >= -160)

m.c1116 = Constraint(expr= - 160*m.b20 + m.x472 - m.x573 >= -160)

m.c1117 = Constraint(expr= - 160*m.b19 + m.x474 - m.x572 >= -160)

m.c1118 = Constraint(expr= - 160*m.b20 + m.x475 - m.x573 >= -160)

m.c1119 = Constraint(expr= - 160*m.b19 + m.x480 - m.x572 >= -160)

m.c1120 = Constraint(expr= - 160*m.b20 + m.x481 - m.x573 >= -160)

m.c1121 = Constraint(expr= - 160*m.b22 + m.x471 - m.x575 >= -160)

m.c1122 = Constraint(expr= - 160*m.b23 + m.x472 - m.x576 >= -160)

m.c1123 = Constraint(expr= - 160*m.b22 + m.x474 - m.x575 >= -160)

m.c1124 = Constraint(expr= - 160*m.b23 + m.x475 - m.x576 >= -160)

m.c1125 = Constraint(expr= - 160*m.b22 + m.x477 - m.x575 >= -160)

m.c1126 = Constraint(expr= - 160*m.b23 + m.x478 - m.x576 >= -160)

m.c1127 = Constraint(expr= - 160*m.b25 + m.x486 - m.x578 >= -160)

m.c1128 = Constraint(expr= - 160*m.b26 + m.x487 - m.x579 >= -160)

m.c1129 = Constraint(expr= - 160*m.b25 + m.x489 - m.x578 >= -160)

m.c1130 = Constraint(expr= - 160*m.b26 + m.x490 - m.x579 >= -160)

m.c1131 = Constraint(expr= - 160*m.b25 + m.x492 - m.x578 >= -160)

m.c1132 = Constraint(expr= - 160*m.b26 + m.x493 - m.x579 >= -160)

m.c1133 = Constraint(expr= - 160*m.b28 + m.x483 - m.x581 >= -160)

m.c1134 = Constraint(expr= - 160*m.b29 + m.x484 - m.x582 >= -160)

m.c1135 = Constraint(expr= - 160*m.b28 + m.x489 - m.x581 >= -160)

m.c1136 = Constraint(expr= - 160*m.b29 + m.x490 - m.x582 >= -160)

m.c1137 = Constraint(expr= - 160*m.b28 + m.x492 - m.x581 >= -160)

m.c1138 = Constraint(expr= - 160*m.b29 + m.x493 - m.x582 >= -160)

m.c1139 = Constraint(expr= - 160*m.b31 + m.x483 - m.x584 >= -160)

m.c1140 = Constraint(expr= - 160*m.b32 + m.x484 - m.x585 >= -160)

m.c1141 = Constraint(expr= - 160*m.b31 + m.x486 - m.x584 >= -160)

m.c1142 = Constraint(expr= - 160*m.b32 + m.x487 - m.x585 >= -160)

m.c1143 = Constraint(expr= - 160*m.b31 + m.x492 - m.x584 >= -160)

m.c1144 = Constraint(expr= - 160*m.b32 + m.x493 - m.x585 >= -160)

m.c1145 = Constraint(expr= - 160*m.b34 + m.x483 - m.x587 >= -160)

m.c1146 = Constraint(expr= - 160*m.b35 + m.x484 - m.x588 >= -160)

m.c1147 = Constraint(expr= - 160*m.b34 + m.x486 - m.x587 >= -160)

m.c1148 = Constraint(expr= - 160*m.b35 + m.x487 - m.x588 >= -160)

m.c1149 = Constraint(expr= - 160*m.b34 + m.x489 - m.x587 >= -160)

m.c1150 = Constraint(expr= - 160*m.b35 + m.x490 - m.x588 >= -160)

m.c1151 = Constraint(expr= - 160*m.b37 + m.x498 - m.x590 >= -160)

m.c1152 = Constraint(expr= - 160*m.b38 + m.x499 - m.x591 >= -160)

m.c1153 = Constraint(expr= - 160*m.b37 + m.x501 - m.x590 >= -160)

m.c1154 = Constraint(expr= - 160*m.b38 + m.x502 - m.x591 >= -160)

m.c1155 = Constraint(expr= - 160*m.b37 + m.x504 - m.x590 >= -160)

m.c1156 = Constraint(expr= - 160*m.b38 + m.x505 - m.x591 >= -160)

m.c1157 = Constraint(expr= - 160*m.b40 + m.x495 - m.x593 >= -160)

m.c1158 = Constraint(expr= - 160*m.b41 + m.x496 - m.x594 >= -160)

m.c1159 = Constraint(expr= - 160*m.b40 + m.x501 - m.x593 >= -160)

m.c1160 = Constraint(expr= - 160*m.b41 + m.x502 - m.x594 >= -160)

m.c1161 = Constraint(expr= - 160*m.b40 + m.x504 - m.x593 >= -160)

m.c1162 = Constraint(expr= - 160*m.b41 + m.x505 - m.x594 >= -160)

m.c1163 = Constraint(expr= - 160*m.b43 + m.x495 - m.x596 >= -160)

m.c1164 = Constraint(expr= - 160*m.b44 + m.x496 - m.x597 >= -160)

m.c1165 = Constraint(expr= - 160*m.b43 + m.x498 - m.x596 >= -160)

m.c1166 = Constraint(expr= - 160*m.b44 + m.x499 - m.x597 >= -160)

m.c1167 = Constraint(expr= - 160*m.b43 + m.x504 - m.x596 >= -160)

m.c1168 = Constraint(expr= - 160*m.b44 + m.x505 - m.x597 >= -160)

m.c1169 = Constraint(expr= - 160*m.b46 + m.x495 - m.x599 >= -160)

m.c1170 = Constraint(expr= - 160*m.b47 + m.x496 - m.x600 >= -160)

m.c1171 = Constraint(expr= - 160*m.b46 + m.x498 - m.x599 >= -160)

m.c1172 = Constraint(expr= - 160*m.b47 + m.x499 - m.x600 >= -160)

m.c1173 = Constraint(expr= - 160*m.b46 + m.x501 - m.x599 >= -160)

m.c1174 = Constraint(expr= - 160*m.b47 + m.x502 - m.x600 >= -160)

m.c1175 = Constraint(expr= - 160*m.b49 + m.x510 - m.x602 >= -160)

m.c1176 = Constraint(expr= - 160*m.b50 + m.x511 - m.x603 >= -160)

m.c1177 = Constraint(expr= - 160*m.b49 + m.x513 - m.x602 >= -160)

m.c1178 = Constraint(expr= - 160*m.b50 + m.x514 - m.x603 >= -160)

m.c1179 = Constraint(expr= - 160*m.b49 + m.x516 - m.x602 >= -160)

m.c1180 = Constraint(expr= - 160*m.b50 + m.x517 - m.x603 >= -160)

m.c1181 = Constraint(expr= - 160*m.b52 + m.x507 - m.x605 >= -160)

m.c1182 = Constraint(expr= - 160*m.b53 + m.x508 - m.x606 >= -160)

m.c1183 = Constraint(expr= - 160*m.b52 + m.x513 - m.x605 >= -160)

m.c1184 = Constraint(expr= - 160*m.b53 + m.x514 - m.x606 >= -160)

m.c1185 = Constraint(expr= - 160*m.b52 + m.x516 - m.x605 >= -160)

m.c1186 = Constraint(expr= - 160*m.b53 + m.x517 - m.x606 >= -160)

m.c1187 = Constraint(expr= - 160*m.b55 + m.x507 - m.x608 >= -160)

m.c1188 = Constraint(expr= - 160*m.b56 + m.x508 - m.x609 >= -160)

m.c1189 = Constraint(expr= - 160*m.b55 + m.x510 - m.x608 >= -160)

m.c1190 = Constraint(expr= - 160*m.b56 + m.x511 - m.x609 >= -160)

m.c1191 = Constraint(expr= - 160*m.b55 + m.x516 - m.x608 >= -160)

m.c1192 = Constraint(expr= - 160*m.b56 + m.x517 - m.x609 >= -160)

m.c1193 = Constraint(expr= - 160*m.b58 + m.x507 - m.x611 >= -160)

m.c1194 = Constraint(expr= - 160*m.b59 + m.x508 - m.x612 >= -160)

m.c1195 = Constraint(expr= - 160*m.b58 + m.x510 - m.x611 >= -160)

m.c1196 = Constraint(expr= - 160*m.b59 + m.x511 - m.x612 >= -160)

m.c1197 = Constraint(expr= - 160*m.b58 + m.x513 - m.x611 >= -160)

m.c1198 = Constraint(expr= - 160*m.b59 + m.x514 - m.x612 >= -160)

m.c1199 = Constraint(expr= - 160*m.b61 + m.x522 - m.x614 >= -160)

m.c1200 = Constraint(expr= - 160*m.b62 + m.x523 - m.x615 >= -160)

m.c1201 = Constraint(expr= - 160*m.b61 + m.x525 - m.x614 >= -160)

m.c1202 = Constraint(expr= - 160*m.b62 + m.x526 - m.x615 >= -160)

m.c1203 = Constraint(expr= - 160*m.b61 + m.x528 - m.x614 >= -160)

m.c1204 = Constraint(expr= - 160*m.b62 + m.x529 - m.x615 >= -160)

m.c1205 = Constraint(expr= - 160*m.b64 + m.x519 - m.x617 >= -160)

m.c1206 = Constraint(expr= - 160*m.b65 + m.x520 - m.x618 >= -160)

m.c1207 = Constraint(expr= - 160*m.b64 + m.x525 - m.x617 >= -160)

m.c1208 = Constraint(expr= - 160*m.b65 + m.x526 - m.x618 >= -160)

m.c1209 = Constraint(expr= - 160*m.b64 + m.x528 - m.x617 >= -160)

m.c1210 = Constraint(expr= - 160*m.b65 + m.x529 - m.x618 >= -160)

m.c1211 = Constraint(expr= - 160*m.b67 + m.x519 - m.x620 >= -160)

m.c1212 = Constraint(expr= - 160*m.b68 + m.x520 - m.x621 >= -160)

m.c1213 = Constraint(expr= - 160*m.b67 + m.x522 - m.x620 >= -160)

m.c1214 = Constraint(expr= - 160*m.b68 + m.x523 - m.x621 >= -160)

m.c1215 = Constraint(expr= - 160*m.b67 + m.x528 - m.x620 >= -160)

m.c1216 = Constraint(expr= - 160*m.b68 + m.x529 - m.x621 >= -160)

m.c1217 = Constraint(expr= - 160*m.b70 + m.x519 - m.x623 >= -160)

m.c1218 = Constraint(expr= - 160*m.b71 + m.x520 - m.x624 >= -160)

m.c1219 = Constraint(expr= - 160*m.b70 + m.x522 - m.x623 >= -160)

m.c1220 = Constraint(expr= - 160*m.b71 + m.x523 - m.x624 >= -160)

m.c1221 = Constraint(expr= - 160*m.b70 + m.x525 - m.x623 >= -160)

m.c1222 = Constraint(expr= - 160*m.b71 + m.x526 - m.x624 >= -160)

m.c1223 = Constraint(expr= - 160*m.b73 + m.x534 - m.x626 >= -160)

m.c1224 = Constraint(expr= - 160*m.b74 + m.x535 - m.x627 >= -160)

m.c1225 = Constraint(expr= - 160*m.b73 + m.x537 - m.x626 >= -160)

m.c1226 = Constraint(expr= - 160*m.b74 + m.x538 - m.x627 >= -160)

m.c1227 = Constraint(expr= - 160*m.b73 + m.x540 - m.x626 >= -160)

m.c1228 = Constraint(expr= - 160*m.b74 + m.x541 - m.x627 >= -160)

m.c1229 = Constraint(expr= - 160*m.b76 + m.x531 - m.x629 >= -160)

m.c1230 = Constraint(expr= - 160*m.b77 + m.x532 - m.x630 >= -160)

m.c1231 = Constraint(expr= - 160*m.b76 + m.x537 - m.x629 >= -160)

m.c1232 = Constraint(expr= - 160*m.b77 + m.x538 - m.x630 >= -160)

m.c1233 = Constraint(expr= - 160*m.b76 + m.x540 - m.x629 >= -160)

m.c1234 = Constraint(expr= - 160*m.b77 + m.x541 - m.x630 >= -160)

m.c1235 = Constraint(expr= - 160*m.b79 + m.x531 - m.x632 >= -160)

m.c1236 = Constraint(expr= - 160*m.b80 + m.x532 - m.x633 >= -160)

m.c1237 = Constraint(expr= - 160*m.b79 + m.x534 - m.x632 >= -160)

m.c1238 = Constraint(expr= - 160*m.b80 + m.x535 - m.x633 >= -160)

m.c1239 = Constraint(expr= - 160*m.b79 + m.x540 - m.x632 >= -160)

m.c1240 = Constraint(expr= - 160*m.b80 + m.x541 - m.x633 >= -160)

m.c1241 = Constraint(expr= - 160*m.b82 + m.x531 - m.x635 >= -160)

m.c1242 = Constraint(expr= - 160*m.b83 + m.x532 - m.x636 >= -160)

m.c1243 = Constraint(expr= - 160*m.b82 + m.x534 - m.x635 >= -160)

m.c1244 = Constraint(expr= - 160*m.b83 + m.x535 - m.x636 >= -160)

m.c1245 = Constraint(expr= - 160*m.b82 + m.x537 - m.x635 >= -160)

m.c1246 = Constraint(expr= - 160*m.b83 + m.x538 - m.x636 >= -160)

m.c1247 = Constraint(expr= - 160*m.b85 + m.x546 - m.x638 >= -160)

m.c1248 = Constraint(expr= - 160*m.b86 + m.x547 - m.x639 >= -160)

m.c1249 = Constraint(expr= - 160*m.b85 + m.x549 - m.x638 >= -160)

m.c1250 = Constraint(expr= - 160*m.b86 + m.x550 - m.x639 >= -160)

m.c1251 = Constraint(expr= - 160*m.b85 + m.x552 - m.x638 >= -160)

m.c1252 = Constraint(expr= - 160*m.b86 + m.x553 - m.x639 >= -160)

m.c1253 = Constraint(expr= - 160*m.b88 + m.x543 - m.x641 >= -160)

m.c1254 = Constraint(expr= - 160*m.b89 + m.x544 - m.x642 >= -160)

m.c1255 = Constraint(expr= - 160*m.b88 + m.x549 - m.x641 >= -160)

m.c1256 = Constraint(expr= - 160*m.b89 + m.x550 - m.x642 >= -160)

m.c1257 = Constraint(expr= - 160*m.b88 + m.x552 - m.x641 >= -160)

m.c1258 = Constraint(expr= - 160*m.b89 + m.x553 - m.x642 >= -160)

m.c1259 = Constraint(expr= - 160*m.b91 + m.x543 - m.x644 >= -160)

m.c1260 = Constraint(expr= - 160*m.b92 + m.x544 - m.x645 >= -160)

m.c1261 = Constraint(expr= - 160*m.b91 + m.x546 - m.x644 >= -160)

m.c1262 = Constraint(expr= - 160*m.b92 + m.x547 - m.x645 >= -160)

m.c1263 = Constraint(expr= - 160*m.b91 + m.x552 - m.x644 >= -160)

m.c1264 = Constraint(expr= - 160*m.b92 + m.x553 - m.x645 >= -160)

m.c1265 = Constraint(expr= - 160*m.b94 + m.x543 - m.x647 >= -160)

m.c1266 = Constraint(expr= - 160*m.b95 + m.x544 - m.x648 >= -160)

m.c1267 = Constraint(expr= - 160*m.b94 + m.x546 - m.x647 >= -160)

m.c1268 = Constraint(expr= - 160*m.b95 + m.x547 - m.x648 >= -160)

m.c1269 = Constraint(expr= - 160*m.b94 + m.x549 - m.x647 >= -160)

m.c1270 = Constraint(expr= - 160*m.b95 + m.x550 - m.x648 >= -160)

m.c1271 = Constraint(expr= - 160*m.b1 + m.x471 - m.x554 >= -160)

m.c1272 = Constraint(expr= - 160*m.b2 + m.x472 - m.x555 >= -160)

m.c1273 = Constraint(expr= - 160*m.b4 + m.x474 - m.x557 >= -160)

m.c1274 = Constraint(expr= - 160*m.b5 + m.x475 - m.x558 >= -160)

m.c1275 = Constraint(expr= - 160*m.b7 + m.x477 - m.x560 >= -160)

m.c1276 = Constraint(expr= - 160*m.b8 + m.x478 - m.x561 >= -160)

m.c1277 = Constraint(expr= - 160*m.b10 + m.x480 - m.x563 >= -160)

m.c1278 = Constraint(expr= - 160*m.b11 + m.x481 - m.x564 >= -160)

m.c1279 = Constraint(expr= - 160*m.b1 + m.x483 - m.x554 >= -160)

m.c1280 = Constraint(expr= - 160*m.b2 + m.x484 - m.x555 >= -160)

m.c1281 = Constraint(expr= - 160*m.b4 + m.x486 - m.x557 >= -160)

m.c1282 = Constraint(expr= - 160*m.b5 + m.x487 - m.x558 >= -160)

m.c1283 = Constraint(expr= - 160*m.b7 + m.x489 - m.x560 >= -160)

m.c1284 = Constraint(expr= - 160*m.b8 + m.x490 - m.x561 >= -160)

m.c1285 = Constraint(expr= - 160*m.b10 + m.x492 - m.x563 >= -160)

m.c1286 = Constraint(expr= - 160*m.b11 + m.x493 - m.x564 >= -160)

m.c1287 = Constraint(expr= - 160*m.b1 + m.x531 - m.x554 >= -160)

m.c1288 = Constraint(expr= - 160*m.b2 + m.x532 - m.x555 >= -160)

m.c1289 = Constraint(expr= - 160*m.b4 + m.x534 - m.x557 >= -160)

m.c1290 = Constraint(expr= - 160*m.b5 + m.x535 - m.x558 >= -160)

m.c1291 = Constraint(expr= - 160*m.b7 + m.x537 - m.x560 >= -160)

m.c1292 = Constraint(expr= - 160*m.b8 + m.x538 - m.x561 >= -160)

m.c1293 = Constraint(expr= - 160*m.b10 + m.x540 - m.x563 >= -160)

m.c1294 = Constraint(expr= - 160*m.b11 + m.x541 - m.x564 >= -160)

m.c1295 = Constraint(expr= - 160*m.b13 + m.x459 - m.x566 >= -160)

m.c1296 = Constraint(expr= - 160*m.b14 + m.x460 - m.x567 >= -160)

m.c1297 = Constraint(expr= - 160*m.b16 + m.x462 - m.x569 >= -160)

m.c1298 = Constraint(expr= - 160*m.b17 + m.x463 - m.x570 >= -160)

m.c1299 = Constraint(expr= - 160*m.b19 + m.x465 - m.x572 >= -160)

m.c1300 = Constraint(expr= - 160*m.b20 + m.x466 - m.x573 >= -160)

m.c1301 = Constraint(expr= - 160*m.b22 + m.x468 - m.x575 >= -160)

m.c1302 = Constraint(expr= - 160*m.b23 + m.x469 - m.x576 >= -160)

m.c1303 = Constraint(expr= - 160*m.b13 + m.x483 - m.x566 >= -160)

m.c1304 = Constraint(expr= - 160*m.b14 + m.x484 - m.x567 >= -160)

m.c1305 = Constraint(expr= - 160*m.b16 + m.x486 - m.x569 >= -160)

m.c1306 = Constraint(expr= - 160*m.b17 + m.x487 - m.x570 >= -160)

m.c1307 = Constraint(expr= - 160*m.b19 + m.x489 - m.x572 >= -160)

m.c1308 = Constraint(expr= - 160*m.b20 + m.x490 - m.x573 >= -160)

m.c1309 = Constraint(expr= - 160*m.b22 + m.x492 - m.x575 >= -160)

m.c1310 = Constraint(expr= - 160*m.b23 + m.x493 - m.x576 >= -160)

m.c1311 = Constraint(expr= - 160*m.b13 + m.x531 - m.x566 >= -160)

m.c1312 = Constraint(expr= - 160*m.b14 + m.x532 - m.x567 >= -160)

m.c1313 = Constraint(expr= - 160*m.b16 + m.x534 - m.x569 >= -160)

m.c1314 = Constraint(expr= - 160*m.b17 + m.x535 - m.x570 >= -160)

m.c1315 = Constraint(expr= - 160*m.b19 + m.x537 - m.x572 >= -160)

m.c1316 = Constraint(expr= - 160*m.b20 + m.x538 - m.x573 >= -160)

m.c1317 = Constraint(expr= - 160*m.b22 + m.x540 - m.x575 >= -160)

m.c1318 = Constraint(expr= - 160*m.b23 + m.x541 - m.x576 >= -160)

m.c1319 = Constraint(expr= - 160*m.b25 + m.x459 - m.x578 >= -160)

m.c1320 = Constraint(expr= - 160*m.b26 + m.x460 - m.x579 >= -160)

m.c1321 = Constraint(expr= - 160*m.b28 + m.x462 - m.x581 >= -160)

m.c1322 = Constraint(expr= - 160*m.b29 + m.x463 - m.x582 >= -160)

m.c1323 = Constraint(expr= - 160*m.b31 + m.x465 - m.x584 >= -160)

m.c1324 = Constraint(expr= - 160*m.b32 + m.x466 - m.x585 >= -160)

m.c1325 = Constraint(expr= - 160*m.b34 + m.x468 - m.x587 >= -160)

m.c1326 = Constraint(expr= - 160*m.b35 + m.x469 - m.x588 >= -160)

m.c1327 = Constraint(expr= - 160*m.b25 + m.x471 - m.x578 >= -160)

m.c1328 = Constraint(expr= - 160*m.b26 + m.x472 - m.x579 >= -160)

m.c1329 = Constraint(expr= - 160*m.b28 + m.x474 - m.x581 >= -160)

m.c1330 = Constraint(expr= - 160*m.b29 + m.x475 - m.x582 >= -160)

m.c1331 = Constraint(expr= - 160*m.b31 + m.x477 - m.x584 >= -160)

m.c1332 = Constraint(expr= - 160*m.b32 + m.x478 - m.x585 >= -160)

m.c1333 = Constraint(expr= - 160*m.b34 + m.x480 - m.x587 >= -160)

m.c1334 = Constraint(expr= - 160*m.b35 + m.x481 - m.x588 >= -160)

m.c1335 = Constraint(expr= - 160*m.b25 + m.x531 - m.x578 >= -160)

m.c1336 = Constraint(expr= - 160*m.b26 + m.x532 - m.x579 >= -160)

m.c1337 = Constraint(expr= - 160*m.b28 + m.x534 - m.x581 >= -160)

m.c1338 = Constraint(expr= - 160*m.b29 + m.x535 - m.x582 >= -160)

m.c1339 = Constraint(expr= - 160*m.b31 + m.x537 - m.x584 >= -160)

m.c1340 = Constraint(expr= - 160*m.b32 + m.x538 - m.x585 >= -160)

m.c1341 = Constraint(expr= - 160*m.b34 + m.x540 - m.x587 >= -160)

m.c1342 = Constraint(expr= - 160*m.b35 + m.x541 - m.x588 >= -160)

m.c1343 = Constraint(expr= - 160*m.b37 + m.x507 - m.x590 >= -160)

m.c1344 = Constraint(expr= - 160*m.b38 + m.x508 - m.x591 >= -160)

m.c1345 = Constraint(expr= - 160*m.b40 + m.x510 - m.x593 >= -160)

m.c1346 = Constraint(expr= - 160*m.b41 + m.x511 - m.x594 >= -160)

m.c1347 = Constraint(expr= - 160*m.b43 + m.x513 - m.x596 >= -160)

m.c1348 = Constraint(expr= - 160*m.b44 + m.x514 - m.x597 >= -160)

m.c1349 = Constraint(expr= - 160*m.b46 + m.x516 - m.x599 >= -160)

m.c1350 = Constraint(expr= - 160*m.b47 + m.x517 - m.x600 >= -160)

m.c1351 = Constraint(expr= - 160*m.b37 + m.x519 - m.x590 >= -160)

m.c1352 = Constraint(expr= - 160*m.b38 + m.x520 - m.x591 >= -160)

m.c1353 = Constraint(expr= - 160*m.b40 + m.x522 - m.x593 >= -160)

m.c1354 = Constraint(expr= - 160*m.b41 + m.x523 - m.x594 >= -160)

m.c1355 = Constraint(expr= - 160*m.b43 + m.x525 - m.x596 >= -160)

m.c1356 = Constraint(expr= - 160*m.b44 + m.x526 - m.x597 >= -160)

m.c1357 = Constraint(expr= - 160*m.b46 + m.x528 - m.x599 >= -160)

m.c1358 = Constraint(expr= - 160*m.b47 + m.x529 - m.x600 >= -160)

m.c1359 = Constraint(expr= - 160*m.b37 + m.x543 - m.x590 >= -160)

m.c1360 = Constraint(expr= - 160*m.b38 + m.x544 - m.x591 >= -160)

m.c1361 = Constraint(expr= - 160*m.b40 + m.x546 - m.x593 >= -160)

m.c1362 = Constraint(expr= - 160*m.b41 + m.x547 - m.x594 >= -160)

m.c1363 = Constraint(expr= - 160*m.b43 + m.x549 - m.x596 >= -160)

m.c1364 = Constraint(expr= - 160*m.b44 + m.x550 - m.x597 >= -160)

m.c1365 = Constraint(expr= - 160*m.b46 + m.x552 - m.x599 >= -160)

m.c1366 = Constraint(expr= - 160*m.b47 + m.x553 - m.x600 >= -160)

m.c1367 = Constraint(expr= - 160*m.b49 + m.x495 - m.x602 >= -160)

m.c1368 = Constraint(expr= - 160*m.b50 + m.x496 - m.x603 >= -160)

m.c1369 = Constraint(expr= - 160*m.b52 + m.x498 - m.x605 >= -160)

m.c1370 = Constraint(expr= - 160*m.b53 + m.x499 - m.x606 >= -160)

m.c1371 = Constraint(expr= - 160*m.b55 + m.x501 - m.x608 >= -160)

m.c1372 = Constraint(expr= - 160*m.b56 + m.x502 - m.x609 >= -160)

m.c1373 = Constraint(expr= - 160*m.b58 + m.x504 - m.x611 >= -160)

m.c1374 = Constraint(expr= - 160*m.b59 + m.x505 - m.x612 >= -160)

m.c1375 = Constraint(expr= - 160*m.b49 + m.x519 - m.x602 >= -160)

m.c1376 = Constraint(expr= - 160*m.b50 + m.x520 - m.x603 >= -160)

m.c1377 = Constraint(expr= - 160*m.b52 + m.x522 - m.x605 >= -160)

m.c1378 = Constraint(expr= - 160*m.b53 + m.x523 - m.x606 >= -160)

m.c1379 = Constraint(expr= - 160*m.b55 + m.x525 - m.x608 >= -160)

m.c1380 = Constraint(expr= - 160*m.b56 + m.x526 - m.x609 >= -160)

m.c1381 = Constraint(expr= - 160*m.b58 + m.x528 - m.x611 >= -160)

m.c1382 = Constraint(expr= - 160*m.b59 + m.x529 - m.x612 >= -160)

m.c1383 = Constraint(expr= - 160*m.b49 + m.x543 - m.x602 >= -160)

m.c1384 = Constraint(expr= - 160*m.b50 + m.x544 - m.x603 >= -160)

m.c1385 = Constraint(expr= - 160*m.b52 + m.x546 - m.x605 >= -160)

m.c1386 = Constraint(expr= - 160*m.b53 + m.x547 - m.x606 >= -160)

m.c1387 = Constraint(expr= - 160*m.b55 + m.x549 - m.x608 >= -160)

m.c1388 = Constraint(expr= - 160*m.b56 + m.x550 - m.x609 >= -160)

m.c1389 = Constraint(expr= - 160*m.b58 + m.x552 - m.x611 >= -160)

m.c1390 = Constraint(expr= - 160*m.b59 + m.x553 - m.x612 >= -160)

m.c1391 = Constraint(expr= - 160*m.b61 + m.x495 - m.x614 >= -160)

m.c1392 = Constraint(expr= - 160*m.b62 + m.x496 - m.x615 >= -160)

m.c1393 = Constraint(expr= - 160*m.b64 + m.x498 - m.x617 >= -160)

m.c1394 = Constraint(expr= - 160*m.b65 + m.x499 - m.x618 >= -160)

m.c1395 = Constraint(expr= - 160*m.b67 + m.x501 - m.x620 >= -160)

m.c1396 = Constraint(expr= - 160*m.b68 + m.x502 - m.x621 >= -160)

m.c1397 = Constraint(expr= - 160*m.b70 + m.x504 - m.x623 >= -160)

m.c1398 = Constraint(expr= - 160*m.b71 + m.x505 - m.x624 >= -160)

m.c1399 = Constraint(expr= - 160*m.b61 + m.x507 - m.x614 >= -160)

m.c1400 = Constraint(expr= - 160*m.b62 + m.x508 - m.x615 >= -160)

m.c1401 = Constraint(expr= - 160*m.b64 + m.x510 - m.x617 >= -160)

m.c1402 = Constraint(expr= - 160*m.b65 + m.x511 - m.x618 >= -160)

m.c1403 = Constraint(expr= - 160*m.b67 + m.x513 - m.x620 >= -160)

m.c1404 = Constraint(expr= - 160*m.b68 + m.x514 - m.x621 >= -160)

m.c1405 = Constraint(expr= - 160*m.b70 + m.x516 - m.x623 >= -160)

m.c1406 = Constraint(expr= - 160*m.b71 + m.x517 - m.x624 >= -160)

m.c1407 = Constraint(expr= - 160*m.b61 + m.x543 - m.x614 >= -160)

m.c1408 = Constraint(expr= - 160*m.b62 + m.x544 - m.x615 >= -160)

m.c1409 = Constraint(expr= - 160*m.b64 + m.x546 - m.x617 >= -160)

m.c1410 = Constraint(expr= - 160*m.b65 + m.x547 - m.x618 >= -160)

m.c1411 = Constraint(expr= - 160*m.b67 + m.x549 - m.x620 >= -160)

m.c1412 = Constraint(expr= - 160*m.b68 + m.x550 - m.x621 >= -160)

m.c1413 = Constraint(expr= - 160*m.b70 + m.x552 - m.x623 >= -160)

m.c1414 = Constraint(expr= - 160*m.b71 + m.x553 - m.x624 >= -160)

m.c1415 = Constraint(expr= - 160*m.b73 + m.x459 - m.x626 >= -160)

m.c1416 = Constraint(expr= - 160*m.b74 + m.x460 - m.x627 >= -160)

m.c1417 = Constraint(expr= - 160*m.b76 + m.x462 - m.x629 >= -160)

m.c1418 = Constraint(expr= - 160*m.b77 + m.x463 - m.x630 >= -160)

m.c1419 = Constraint(expr= - 160*m.b79 + m.x465 - m.x632 >= -160)

m.c1420 = Constraint(expr= - 160*m.b80 + m.x466 - m.x633 >= -160)

m.c1421 = Constraint(expr= - 160*m.b82 + m.x468 - m.x635 >= -160)

m.c1422 = Constraint(expr= - 160*m.b83 + m.x469 - m.x636 >= -160)

m.c1423 = Constraint(expr= - 160*m.b73 + m.x471 - m.x626 >= -160)

m.c1424 = Constraint(expr= - 160*m.b74 + m.x472 - m.x627 >= -160)

m.c1425 = Constraint(expr= - 160*m.b76 + m.x474 - m.x629 >= -160)

m.c1426 = Constraint(expr= - 160*m.b77 + m.x475 - m.x630 >= -160)

m.c1427 = Constraint(expr= - 160*m.b79 + m.x477 - m.x632 >= -160)

m.c1428 = Constraint(expr= - 160*m.b80 + m.x478 - m.x633 >= -160)

m.c1429 = Constraint(expr= - 160*m.b82 + m.x480 - m.x635 >= -160)

m.c1430 = Constraint(expr= - 160*m.b83 + m.x481 - m.x636 >= -160)

m.c1431 = Constraint(expr= - 160*m.b73 + m.x483 - m.x626 >= -160)

m.c1432 = Constraint(expr= - 160*m.b74 + m.x484 - m.x627 >= -160)

m.c1433 = Constraint(expr= - 160*m.b76 + m.x486 - m.x629 >= -160)

m.c1434 = Constraint(expr= - 160*m.b77 + m.x487 - m.x630 >= -160)

m.c1435 = Constraint(expr= - 160*m.b79 + m.x489 - m.x632 >= -160)

m.c1436 = Constraint(expr= - 160*m.b80 + m.x490 - m.x633 >= -160)

m.c1437 = Constraint(expr= - 160*m.b82 + m.x492 - m.x635 >= -160)

m.c1438 = Constraint(expr= - 160*m.b83 + m.x493 - m.x636 >= -160)

m.c1439 = Constraint(expr= - 160*m.b85 + m.x495 - m.x638 >= -160)

m.c1440 = Constraint(expr= - 160*m.b86 + m.x496 - m.x639 >= -160)

m.c1441 = Constraint(expr= - 160*m.b88 + m.x498 - m.x641 >= -160)

m.c1442 = Constraint(expr= - 160*m.b89 + m.x499 - m.x642 >= -160)

m.c1443 = Constraint(expr= - 160*m.b91 + m.x501 - m.x644 >= -160)

m.c1444 = Constraint(expr= - 160*m.b92 + m.x502 - m.x645 >= -160)

m.c1445 = Constraint(expr= - 160*m.b94 + m.x504 - m.x647 >= -160)

m.c1446 = Constraint(expr= - 160*m.b95 + m.x505 - m.x648 >= -160)

m.c1447 = Constraint(expr= - 160*m.b85 + m.x507 - m.x638 >= -160)

m.c1448 = Constraint(expr= - 160*m.b86 + m.x508 - m.x639 >= -160)

m.c1449 = Constraint(expr= - 160*m.b88 + m.x510 - m.x641 >= -160)

m.c1450 = Constraint(expr= - 160*m.b89 + m.x511 - m.x642 >= -160)

m.c1451 = Constraint(expr= - 160*m.b91 + m.x513 - m.x644 >= -160)

m.c1452 = Constraint(expr= - 160*m.b92 + m.x514 - m.x645 >= -160)

m.c1453 = Constraint(expr= - 160*m.b94 + m.x516 - m.x647 >= -160)

m.c1454 = Constraint(expr= - 160*m.b95 + m.x517 - m.x648 >= -160)

m.c1455 = Constraint(expr= - 160*m.b85 + m.x519 - m.x638 >= -160)

m.c1456 = Constraint(expr= - 160*m.b86 + m.x520 - m.x639 >= -160)

m.c1457 = Constraint(expr= - 160*m.b88 + m.x522 - m.x641 >= -160)

m.c1458 = Constraint(expr= - 160*m.b89 + m.x523 - m.x642 >= -160)

m.c1459 = Constraint(expr= - 160*m.b91 + m.x525 - m.x644 >= -160)

m.c1460 = Constraint(expr= - 160*m.b92 + m.x526 - m.x645 >= -160)

m.c1461 = Constraint(expr= - 160*m.b94 + m.x528 - m.x647 >= -160)

m.c1462 = Constraint(expr= - 160*m.b95 + m.x529 - m.x648 >= -160)

m.c1463 = Constraint(expr=   160*m.b1 + 160*m.b2 + m.x459 - m.x554 <= 320)

m.c1464 = Constraint(expr=   160*m.b2 + 160*m.b3 + m.x460 - m.x555 <= 320)

m.c1465 = Constraint(expr=   160*m.b1 + 160*m.b5 + m.x462 - m.x554 <= 320)

m.c1466 = Constraint(expr=   160*m.b2 + 160*m.b6 + m.x463 - m.x555 <= 320)

m.c1467 = Constraint(expr=   160*m.b1 + 160*m.b8 + m.x465 - m.x554 <= 320)

m.c1468 = Constraint(expr=   160*m.b2 + 160*m.b9 + m.x466 - m.x555 <= 320)

m.c1469 = Constraint(expr=   160*m.b1 + 160*m.b11 + m.x468 - m.x554 <= 320)

m.c1470 = Constraint(expr=   160*m.b2 + 160*m.b12 + m.x469 - m.x555 <= 320)

m.c1471 = Constraint(expr=   160*m.b2 + 160*m.b4 + m.x459 - m.x557 <= 320)

m.c1472 = Constraint(expr=   160*m.b3 + 160*m.b5 + m.x460 - m.x558 <= 320)

m.c1473 = Constraint(expr=   160*m.b4 + 160*m.b5 + m.x462 - m.x557 <= 320)

m.c1474 = Constraint(expr=   160*m.b5 + 160*m.b6 + m.x463 - m.x558 <= 320)

m.c1475 = Constraint(expr=   160*m.b4 + 160*m.b8 + m.x465 - m.x557 <= 320)

m.c1476 = Constraint(expr=   160*m.b5 + 160*m.b9 + m.x466 - m.x558 <= 320)

m.c1477 = Constraint(expr=   160*m.b4 + 160*m.b11 + m.x468 - m.x557 <= 320)

m.c1478 = Constraint(expr=   160*m.b5 + 160*m.b12 + m.x469 - m.x558 <= 320)

m.c1479 = Constraint(expr=   160*m.b2 + 160*m.b7 + m.x459 - m.x560 <= 320)

m.c1480 = Constraint(expr=   160*m.b3 + 160*m.b8 + m.x460 - m.x561 <= 320)

m.c1481 = Constraint(expr=   160*m.b5 + 160*m.b7 + m.x462 - m.x560 <= 320)

m.c1482 = Constraint(expr=   160*m.b6 + 160*m.b8 + m.x463 - m.x561 <= 320)

m.c1483 = Constraint(expr=   160*m.b7 + 160*m.b8 + m.x465 - m.x560 <= 320)

m.c1484 = Constraint(expr=   160*m.b8 + 160*m.b9 + m.x466 - m.x561 <= 320)

m.c1485 = Constraint(expr=   160*m.b7 + 160*m.b11 + m.x468 - m.x560 <= 320)

m.c1486 = Constraint(expr=   160*m.b8 + 160*m.b12 + m.x469 - m.x561 <= 320)

m.c1487 = Constraint(expr=   160*m.b2 + 160*m.b10 + m.x459 - m.x563 <= 320)

m.c1488 = Constraint(expr=   160*m.b3 + 160*m.b11 + m.x460 - m.x564 <= 320)

m.c1489 = Constraint(expr=   160*m.b5 + 160*m.b10 + m.x462 - m.x563 <= 320)

m.c1490 = Constraint(expr=   160*m.b6 + 160*m.b11 + m.x463 - m.x564 <= 320)

m.c1491 = Constraint(expr=   160*m.b8 + 160*m.b10 + m.x465 - m.x563 <= 320)

m.c1492 = Constraint(expr=   160*m.b9 + 160*m.b11 + m.x466 - m.x564 <= 320)

m.c1493 = Constraint(expr=   160*m.b10 + 160*m.b11 + m.x468 - m.x563 <= 320)

m.c1494 = Constraint(expr=   160*m.b11 + 160*m.b12 + m.x469 - m.x564 <= 320)

m.c1495 = Constraint(expr=   160*m.b13 + 160*m.b14 + m.x471 - m.x566 <= 320)

m.c1496 = Constraint(expr=   160*m.b14 + 160*m.b15 + m.x472 - m.x567 <= 320)

m.c1497 = Constraint(expr=   160*m.b13 + 160*m.b17 + m.x474 - m.x566 <= 320)

m.c1498 = Constraint(expr=   160*m.b14 + 160*m.b18 + m.x475 - m.x567 <= 320)

m.c1499 = Constraint(expr=   160*m.b13 + 160*m.b20 + m.x477 - m.x566 <= 320)

m.c1500 = Constraint(expr=   160*m.b14 + 160*m.b21 + m.x478 - m.x567 <= 320)

m.c1501 = Constraint(expr=   160*m.b13 + 160*m.b23 + m.x480 - m.x566 <= 320)

m.c1502 = Constraint(expr=   160*m.b14 + 160*m.b24 + m.x481 - m.x567 <= 320)

m.c1503 = Constraint(expr=   160*m.b14 + 160*m.b16 + m.x471 - m.x569 <= 320)

m.c1504 = Constraint(expr=   160*m.b15 + 160*m.b17 + m.x472 - m.x570 <= 320)

m.c1505 = Constraint(expr=   160*m.b16 + 160*m.b17 + m.x474 - m.x569 <= 320)

m.c1506 = Constraint(expr=   160*m.b17 + 160*m.b18 + m.x475 - m.x570 <= 320)

m.c1507 = Constraint(expr=   160*m.b16 + 160*m.b20 + m.x477 - m.x569 <= 320)

m.c1508 = Constraint(expr=   160*m.b17 + 160*m.b21 + m.x478 - m.x570 <= 320)

m.c1509 = Constraint(expr=   160*m.b16 + 160*m.b23 + m.x480 - m.x569 <= 320)

m.c1510 = Constraint(expr=   160*m.b17 + 160*m.b24 + m.x481 - m.x570 <= 320)

m.c1511 = Constraint(expr=   160*m.b14 + 160*m.b19 + m.x471 - m.x572 <= 320)

m.c1512 = Constraint(expr=   160*m.b15 + 160*m.b20 + m.x472 - m.x573 <= 320)

m.c1513 = Constraint(expr=   160*m.b17 + 160*m.b19 + m.x474 - m.x572 <= 320)

m.c1514 = Constraint(expr=   160*m.b18 + 160*m.b20 + m.x475 - m.x573 <= 320)

m.c1515 = Constraint(expr=   160*m.b19 + 160*m.b20 + m.x477 - m.x572 <= 320)

m.c1516 = Constraint(expr=   160*m.b20 + 160*m.b21 + m.x478 - m.x573 <= 320)

m.c1517 = Constraint(expr=   160*m.b19 + 160*m.b23 + m.x480 - m.x572 <= 320)

m.c1518 = Constraint(expr=   160*m.b20 + 160*m.b24 + m.x481 - m.x573 <= 320)

m.c1519 = Constraint(expr=   160*m.b14 + 160*m.b22 + m.x471 - m.x575 <= 320)

m.c1520 = Constraint(expr=   160*m.b15 + 160*m.b23 + m.x472 - m.x576 <= 320)

m.c1521 = Constraint(expr=   160*m.b17 + 160*m.b22 + m.x474 - m.x575 <= 320)

m.c1522 = Constraint(expr=   160*m.b18 + 160*m.b23 + m.x475 - m.x576 <= 320)

m.c1523 = Constraint(expr=   160*m.b20 + 160*m.b22 + m.x477 - m.x575 <= 320)

m.c1524 = Constraint(expr=   160*m.b21 + 160*m.b23 + m.x478 - m.x576 <= 320)

m.c1525 = Constraint(expr=   160*m.b22 + 160*m.b23 + m.x480 - m.x575 <= 320)

m.c1526 = Constraint(expr=   160*m.b23 + 160*m.b24 + m.x481 - m.x576 <= 320)

m.c1527 = Constraint(expr=   160*m.b25 + 160*m.b26 + m.x483 - m.x578 <= 320)

m.c1528 = Constraint(expr=   160*m.b26 + 160*m.b27 + m.x484 - m.x579 <= 320)

m.c1529 = Constraint(expr=   160*m.b25 + 160*m.b29 + m.x486 - m.x578 <= 320)

m.c1530 = Constraint(expr=   160*m.b26 + 160*m.b30 + m.x487 - m.x579 <= 320)

m.c1531 = Constraint(expr=   160*m.b25 + 160*m.b32 + m.x489 - m.x578 <= 320)

m.c1532 = Constraint(expr=   160*m.b26 + 160*m.b33 + m.x490 - m.x579 <= 320)

m.c1533 = Constraint(expr=   160*m.b25 + 160*m.b35 + m.x492 - m.x578 <= 320)

m.c1534 = Constraint(expr=   160*m.b26 + 160*m.b36 + m.x493 - m.x579 <= 320)

m.c1535 = Constraint(expr=   160*m.b26 + 160*m.b28 + m.x483 - m.x581 <= 320)

m.c1536 = Constraint(expr=   160*m.b27 + 160*m.b29 + m.x484 - m.x582 <= 320)

m.c1537 = Constraint(expr=   160*m.b28 + 160*m.b29 + m.x486 - m.x581 <= 320)

m.c1538 = Constraint(expr=   160*m.b29 + 160*m.b30 + m.x487 - m.x582 <= 320)

m.c1539 = Constraint(expr=   160*m.b28 + 160*m.b32 + m.x489 - m.x581 <= 320)

m.c1540 = Constraint(expr=   160*m.b29 + 160*m.b33 + m.x490 - m.x582 <= 320)

m.c1541 = Constraint(expr=   160*m.b28 + 160*m.b35 + m.x492 - m.x581 <= 320)

m.c1542 = Constraint(expr=   160*m.b29 + 160*m.b36 + m.x493 - m.x582 <= 320)

m.c1543 = Constraint(expr=   160*m.b26 + 160*m.b31 + m.x483 - m.x584 <= 320)

m.c1544 = Constraint(expr=   160*m.b27 + 160*m.b32 + m.x484 - m.x585 <= 320)

m.c1545 = Constraint(expr=   160*m.b29 + 160*m.b31 + m.x486 - m.x584 <= 320)

m.c1546 = Constraint(expr=   160*m.b30 + 160*m.b32 + m.x487 - m.x585 <= 320)

m.c1547 = Constraint(expr=   160*m.b31 + 160*m.b32 + m.x489 - m.x584 <= 320)

m.c1548 = Constraint(expr=   160*m.b32 + 160*m.b33 + m.x490 - m.x585 <= 320)

m.c1549 = Constraint(expr=   160*m.b31 + 160*m.b35 + m.x492 - m.x584 <= 320)

m.c1550 = Constraint(expr=   160*m.b32 + 160*m.b36 + m.x493 - m.x585 <= 320)

m.c1551 = Constraint(expr=   160*m.b26 + 160*m.b34 + m.x483 - m.x587 <= 320)

m.c1552 = Constraint(expr=   160*m.b27 + 160*m.b35 + m.x484 - m.x588 <= 320)

m.c1553 = Constraint(expr=   160*m.b29 + 160*m.b34 + m.x486 - m.x587 <= 320)

m.c1554 = Constraint(expr=   160*m.b30 + 160*m.b35 + m.x487 - m.x588 <= 320)

m.c1555 = Constraint(expr=   160*m.b32 + 160*m.b34 + m.x489 - m.x587 <= 320)

m.c1556 = Constraint(expr=   160*m.b33 + 160*m.b35 + m.x490 - m.x588 <= 320)

m.c1557 = Constraint(expr=   160*m.b34 + 160*m.b35 + m.x492 - m.x587 <= 320)

m.c1558 = Constraint(expr=   160*m.b35 + 160*m.b36 + m.x493 - m.x588 <= 320)

m.c1559 = Constraint(expr=   160*m.b37 + 160*m.b38 + m.x495 - m.x590 <= 320)

m.c1560 = Constraint(expr=   160*m.b38 + 160*m.b39 + m.x496 - m.x591 <= 320)

m.c1561 = Constraint(expr=   160*m.b37 + 160*m.b41 + m.x498 - m.x590 <= 320)

m.c1562 = Constraint(expr=   160*m.b38 + 160*m.b42 + m.x499 - m.x591 <= 320)

m.c1563 = Constraint(expr=   160*m.b37 + 160*m.b44 + m.x501 - m.x590 <= 320)

m.c1564 = Constraint(expr=   160*m.b38 + 160*m.b45 + m.x502 - m.x591 <= 320)

m.c1565 = Constraint(expr=   160*m.b37 + 160*m.b47 + m.x504 - m.x590 <= 320)

m.c1566 = Constraint(expr=   160*m.b38 + 160*m.b48 + m.x505 - m.x591 <= 320)

m.c1567 = Constraint(expr=   160*m.b38 + 160*m.b40 + m.x495 - m.x593 <= 320)

m.c1568 = Constraint(expr=   160*m.b39 + 160*m.b41 + m.x496 - m.x594 <= 320)

m.c1569 = Constraint(expr=   160*m.b40 + 160*m.b41 + m.x498 - m.x593 <= 320)

m.c1570 = Constraint(expr=   160*m.b41 + 160*m.b42 + m.x499 - m.x594 <= 320)

m.c1571 = Constraint(expr=   160*m.b40 + 160*m.b44 + m.x501 - m.x593 <= 320)

m.c1572 = Constraint(expr=   160*m.b41 + 160*m.b45 + m.x502 - m.x594 <= 320)

m.c1573 = Constraint(expr=   160*m.b40 + 160*m.b47 + m.x504 - m.x593 <= 320)

m.c1574 = Constraint(expr=   160*m.b41 + 160*m.b48 + m.x505 - m.x594 <= 320)

m.c1575 = Constraint(expr=   160*m.b38 + 160*m.b43 + m.x495 - m.x596 <= 320)

m.c1576 = Constraint(expr=   160*m.b39 + 160*m.b44 + m.x496 - m.x597 <= 320)

m.c1577 = Constraint(expr=   160*m.b41 + 160*m.b43 + m.x498 - m.x596 <= 320)

m.c1578 = Constraint(expr=   160*m.b42 + 160*m.b44 + m.x499 - m.x597 <= 320)

m.c1579 = Constraint(expr=   160*m.b43 + 160*m.b44 + m.x501 - m.x596 <= 320)

m.c1580 = Constraint(expr=   160*m.b44 + 160*m.b45 + m.x502 - m.x597 <= 320)

m.c1581 = Constraint(expr=   160*m.b43 + 160*m.b47 + m.x504 - m.x596 <= 320)

m.c1582 = Constraint(expr=   160*m.b44 + 160*m.b48 + m.x505 - m.x597 <= 320)

m.c1583 = Constraint(expr=   160*m.b38 + 160*m.b46 + m.x495 - m.x599 <= 320)

m.c1584 = Constraint(expr=   160*m.b39 + 160*m.b47 + m.x496 - m.x600 <= 320)

m.c1585 = Constraint(expr=   160*m.b41 + 160*m.b46 + m.x498 - m.x599 <= 320)

m.c1586 = Constraint(expr=   160*m.b42 + 160*m.b47 + m.x499 - m.x600 <= 320)

m.c1587 = Constraint(expr=   160*m.b44 + 160*m.b46 + m.x501 - m.x599 <= 320)

m.c1588 = Constraint(expr=   160*m.b45 + 160*m.b47 + m.x502 - m.x600 <= 320)

m.c1589 = Constraint(expr=   160*m.b46 + 160*m.b47 + m.x504 - m.x599 <= 320)

m.c1590 = Constraint(expr=   160*m.b47 + 160*m.b48 + m.x505 - m.x600 <= 320)

m.c1591 = Constraint(expr=   160*m.b49 + 160*m.b50 + m.x507 - m.x602 <= 320)

m.c1592 = Constraint(expr=   160*m.b50 + 160*m.b51 + m.x508 - m.x603 <= 320)

m.c1593 = Constraint(expr=   160*m.b49 + 160*m.b53 + m.x510 - m.x602 <= 320)

m.c1594 = Constraint(expr=   160*m.b50 + 160*m.b54 + m.x511 - m.x603 <= 320)

m.c1595 = Constraint(expr=   160*m.b49 + 160*m.b56 + m.x513 - m.x602 <= 320)

m.c1596 = Constraint(expr=   160*m.b50 + 160*m.b57 + m.x514 - m.x603 <= 320)

m.c1597 = Constraint(expr=   160*m.b49 + 160*m.b59 + m.x516 - m.x602 <= 320)

m.c1598 = Constraint(expr=   160*m.b50 + 160*m.b60 + m.x517 - m.x603 <= 320)

m.c1599 = Constraint(expr=   160*m.b50 + 160*m.b52 + m.x507 - m.x605 <= 320)

m.c1600 = Constraint(expr=   160*m.b51 + 160*m.b53 + m.x508 - m.x606 <= 320)

m.c1601 = Constraint(expr=   160*m.b52 + 160*m.b53 + m.x510 - m.x605 <= 320)

m.c1602 = Constraint(expr=   160*m.b53 + 160*m.b54 + m.x511 - m.x606 <= 320)

m.c1603 = Constraint(expr=   160*m.b52 + 160*m.b56 + m.x513 - m.x605 <= 320)

m.c1604 = Constraint(expr=   160*m.b53 + 160*m.b57 + m.x514 - m.x606 <= 320)

m.c1605 = Constraint(expr=   160*m.b52 + 160*m.b59 + m.x516 - m.x605 <= 320)

m.c1606 = Constraint(expr=   160*m.b53 + 160*m.b60 + m.x517 - m.x606 <= 320)

m.c1607 = Constraint(expr=   160*m.b50 + 160*m.b55 + m.x507 - m.x608 <= 320)

m.c1608 = Constraint(expr=   160*m.b51 + 160*m.b56 + m.x508 - m.x609 <= 320)

m.c1609 = Constraint(expr=   160*m.b53 + 160*m.b55 + m.x510 - m.x608 <= 320)

m.c1610 = Constraint(expr=   160*m.b54 + 160*m.b56 + m.x511 - m.x609 <= 320)

m.c1611 = Constraint(expr=   160*m.b55 + 160*m.b56 + m.x513 - m.x608 <= 320)

m.c1612 = Constraint(expr=   160*m.b56 + 160*m.b57 + m.x514 - m.x609 <= 320)

m.c1613 = Constraint(expr=   160*m.b55 + 160*m.b59 + m.x516 - m.x608 <= 320)

m.c1614 = Constraint(expr=   160*m.b56 + 160*m.b60 + m.x517 - m.x609 <= 320)

m.c1615 = Constraint(expr=   160*m.b50 + 160*m.b58 + m.x507 - m.x611 <= 320)

m.c1616 = Constraint(expr=   160*m.b51 + 160*m.b59 + m.x508 - m.x612 <= 320)

m.c1617 = Constraint(expr=   160*m.b53 + 160*m.b58 + m.x510 - m.x611 <= 320)

m.c1618 = Constraint(expr=   160*m.b54 + 160*m.b59 + m.x511 - m.x612 <= 320)

m.c1619 = Constraint(expr=   160*m.b56 + 160*m.b58 + m.x513 - m.x611 <= 320)

m.c1620 = Constraint(expr=   160*m.b57 + 160*m.b59 + m.x514 - m.x612 <= 320)

m.c1621 = Constraint(expr=   160*m.b58 + 160*m.b59 + m.x516 - m.x611 <= 320)

m.c1622 = Constraint(expr=   160*m.b59 + 160*m.b60 + m.x517 - m.x612 <= 320)

m.c1623 = Constraint(expr=   160*m.b61 + 160*m.b62 + m.x519 - m.x614 <= 320)

m.c1624 = Constraint(expr=   160*m.b62 + 160*m.b63 + m.x520 - m.x615 <= 320)

m.c1625 = Constraint(expr=   160*m.b61 + 160*m.b65 + m.x522 - m.x614 <= 320)

m.c1626 = Constraint(expr=   160*m.b62 + 160*m.b66 + m.x523 - m.x615 <= 320)

m.c1627 = Constraint(expr=   160*m.b61 + 160*m.b68 + m.x525 - m.x614 <= 320)

m.c1628 = Constraint(expr=   160*m.b62 + 160*m.b69 + m.x526 - m.x615 <= 320)

m.c1629 = Constraint(expr=   160*m.b61 + 160*m.b71 + m.x528 - m.x614 <= 320)

m.c1630 = Constraint(expr=   160*m.b62 + 160*m.b72 + m.x529 - m.x615 <= 320)

m.c1631 = Constraint(expr=   160*m.b62 + 160*m.b64 + m.x519 - m.x617 <= 320)

m.c1632 = Constraint(expr=   160*m.b63 + 160*m.b65 + m.x520 - m.x618 <= 320)

m.c1633 = Constraint(expr=   160*m.b64 + 160*m.b65 + m.x522 - m.x617 <= 320)

m.c1634 = Constraint(expr=   160*m.b65 + 160*m.b66 + m.x523 - m.x618 <= 320)

m.c1635 = Constraint(expr=   160*m.b64 + 160*m.b68 + m.x525 - m.x617 <= 320)

m.c1636 = Constraint(expr=   160*m.b65 + 160*m.b69 + m.x526 - m.x618 <= 320)

m.c1637 = Constraint(expr=   160*m.b64 + 160*m.b71 + m.x528 - m.x617 <= 320)

m.c1638 = Constraint(expr=   160*m.b65 + 160*m.b72 + m.x529 - m.x618 <= 320)

m.c1639 = Constraint(expr=   160*m.b62 + 160*m.b67 + m.x519 - m.x620 <= 320)

m.c1640 = Constraint(expr=   160*m.b63 + 160*m.b68 + m.x520 - m.x621 <= 320)

m.c1641 = Constraint(expr=   160*m.b65 + 160*m.b67 + m.x522 - m.x620 <= 320)

m.c1642 = Constraint(expr=   160*m.b66 + 160*m.b68 + m.x523 - m.x621 <= 320)

m.c1643 = Constraint(expr=   160*m.b67 + 160*m.b68 + m.x525 - m.x620 <= 320)

m.c1644 = Constraint(expr=   160*m.b68 + 160*m.b69 + m.x526 - m.x621 <= 320)

m.c1645 = Constraint(expr=   160*m.b67 + 160*m.b71 + m.x528 - m.x620 <= 320)

m.c1646 = Constraint(expr=   160*m.b68 + 160*m.b72 + m.x529 - m.x621 <= 320)

m.c1647 = Constraint(expr=   160*m.b62 + 160*m.b70 + m.x519 - m.x623 <= 320)

m.c1648 = Constraint(expr=   160*m.b63 + 160*m.b71 + m.x520 - m.x624 <= 320)

m.c1649 = Constraint(expr=   160*m.b65 + 160*m.b70 + m.x522 - m.x623 <= 320)

m.c1650 = Constraint(expr=   160*m.b66 + 160*m.b71 + m.x523 - m.x624 <= 320)

m.c1651 = Constraint(expr=   160*m.b68 + 160*m.b70 + m.x525 - m.x623 <= 320)

m.c1652 = Constraint(expr=   160*m.b69 + 160*m.b71 + m.x526 - m.x624 <= 320)

m.c1653 = Constraint(expr=   160*m.b70 + 160*m.b71 + m.x528 - m.x623 <= 320)

m.c1654 = Constraint(expr=   160*m.b71 + 160*m.b72 + m.x529 - m.x624 <= 320)

m.c1655 = Constraint(expr=   160*m.b73 + 160*m.b74 + m.x531 - m.x626 <= 320)

m.c1656 = Constraint(expr=   160*m.b74 + 160*m.b75 + m.x532 - m.x627 <= 320)

m.c1657 = Constraint(expr=   160*m.b73 + 160*m.b77 + m.x534 - m.x626 <= 320)

m.c1658 = Constraint(expr=   160*m.b74 + 160*m.b78 + m.x535 - m.x627 <= 320)

m.c1659 = Constraint(expr=   160*m.b73 + 160*m.b80 + m.x537 - m.x626 <= 320)

m.c1660 = Constraint(expr=   160*m.b74 + 160*m.b81 + m.x538 - m.x627 <= 320)

m.c1661 = Constraint(expr=   160*m.b73 + 160*m.b83 + m.x540 - m.x626 <= 320)

m.c1662 = Constraint(expr=   160*m.b74 + 160*m.b84 + m.x541 - m.x627 <= 320)

m.c1663 = Constraint(expr=   160*m.b74 + 160*m.b76 + m.x531 - m.x629 <= 320)

m.c1664 = Constraint(expr=   160*m.b75 + 160*m.b77 + m.x532 - m.x630 <= 320)

m.c1665 = Constraint(expr=   160*m.b76 + 160*m.b77 + m.x534 - m.x629 <= 320)

m.c1666 = Constraint(expr=   160*m.b77 + 160*m.b78 + m.x535 - m.x630 <= 320)

m.c1667 = Constraint(expr=   160*m.b76 + 160*m.b80 + m.x537 - m.x629 <= 320)

m.c1668 = Constraint(expr=   160*m.b77 + 160*m.b81 + m.x538 - m.x630 <= 320)

m.c1669 = Constraint(expr=   160*m.b76 + 160*m.b83 + m.x540 - m.x629 <= 320)

m.c1670 = Constraint(expr=   160*m.b77 + 160*m.b84 + m.x541 - m.x630 <= 320)

m.c1671 = Constraint(expr=   160*m.b74 + 160*m.b79 + m.x531 - m.x632 <= 320)

m.c1672 = Constraint(expr=   160*m.b75 + 160*m.b80 + m.x532 - m.x633 <= 320)

m.c1673 = Constraint(expr=   160*m.b77 + 160*m.b79 + m.x534 - m.x632 <= 320)

m.c1674 = Constraint(expr=   160*m.b78 + 160*m.b80 + m.x535 - m.x633 <= 320)

m.c1675 = Constraint(expr=   160*m.b79 + 160*m.b80 + m.x537 - m.x632 <= 320)

m.c1676 = Constraint(expr=   160*m.b80 + 160*m.b81 + m.x538 - m.x633 <= 320)

m.c1677 = Constraint(expr=   160*m.b79 + 160*m.b83 + m.x540 - m.x632 <= 320)

m.c1678 = Constraint(expr=   160*m.b80 + 160*m.b84 + m.x541 - m.x633 <= 320)

m.c1679 = Constraint(expr=   160*m.b74 + 160*m.b82 + m.x531 - m.x635 <= 320)

m.c1680 = Constraint(expr=   160*m.b75 + 160*m.b83 + m.x532 - m.x636 <= 320)

m.c1681 = Constraint(expr=   160*m.b77 + 160*m.b82 + m.x534 - m.x635 <= 320)

m.c1682 = Constraint(expr=   160*m.b78 + 160*m.b83 + m.x535 - m.x636 <= 320)

m.c1683 = Constraint(expr=   160*m.b80 + 160*m.b82 + m.x537 - m.x635 <= 320)

m.c1684 = Constraint(expr=   160*m.b81 + 160*m.b83 + m.x538 - m.x636 <= 320)

m.c1685 = Constraint(expr=   160*m.b82 + 160*m.b83 + m.x540 - m.x635 <= 320)

m.c1686 = Constraint(expr=   160*m.b83 + 160*m.b84 + m.x541 - m.x636 <= 320)

m.c1687 = Constraint(expr=   160*m.b85 + 160*m.b86 + m.x543 - m.x638 <= 320)

m.c1688 = Constraint(expr=   160*m.b86 + 160*m.b87 + m.x544 - m.x639 <= 320)

m.c1689 = Constraint(expr=   160*m.b85 + 160*m.b89 + m.x546 - m.x638 <= 320)

m.c1690 = Constraint(expr=   160*m.b86 + 160*m.b90 + m.x547 - m.x639 <= 320)

m.c1691 = Constraint(expr=   160*m.b85 + 160*m.b92 + m.x549 - m.x638 <= 320)

m.c1692 = Constraint(expr=   160*m.b86 + 160*m.b93 + m.x550 - m.x639 <= 320)

m.c1693 = Constraint(expr=   160*m.b85 + 160*m.b95 + m.x552 - m.x638 <= 320)

m.c1694 = Constraint(expr=   160*m.b86 + 160*m.b96 + m.x553 - m.x639 <= 320)

m.c1695 = Constraint(expr=   160*m.b86 + 160*m.b88 + m.x543 - m.x641 <= 320)

m.c1696 = Constraint(expr=   160*m.b87 + 160*m.b89 + m.x544 - m.x642 <= 320)

m.c1697 = Constraint(expr=   160*m.b88 + 160*m.b89 + m.x546 - m.x641 <= 320)

m.c1698 = Constraint(expr=   160*m.b89 + 160*m.b90 + m.x547 - m.x642 <= 320)

m.c1699 = Constraint(expr=   160*m.b88 + 160*m.b92 + m.x549 - m.x641 <= 320)

m.c1700 = Constraint(expr=   160*m.b89 + 160*m.b93 + m.x550 - m.x642 <= 320)

m.c1701 = Constraint(expr=   160*m.b88 + 160*m.b95 + m.x552 - m.x641 <= 320)

m.c1702 = Constraint(expr=   160*m.b89 + 160*m.b96 + m.x553 - m.x642 <= 320)

m.c1703 = Constraint(expr=   160*m.b86 + 160*m.b91 + m.x543 - m.x644 <= 320)

m.c1704 = Constraint(expr=   160*m.b87 + 160*m.b92 + m.x544 - m.x645 <= 320)

m.c1705 = Constraint(expr=   160*m.b89 + 160*m.b91 + m.x546 - m.x644 <= 320)

m.c1706 = Constraint(expr=   160*m.b90 + 160*m.b92 + m.x547 - m.x645 <= 320)

m.c1707 = Constraint(expr=   160*m.b91 + 160*m.b92 + m.x549 - m.x644 <= 320)

m.c1708 = Constraint(expr=   160*m.b92 + 160*m.b93 + m.x550 - m.x645 <= 320)

m.c1709 = Constraint(expr=   160*m.b91 + 160*m.b95 + m.x552 - m.x644 <= 320)

m.c1710 = Constraint(expr=   160*m.b92 + 160*m.b96 + m.x553 - m.x645 <= 320)

m.c1711 = Constraint(expr=   160*m.b86 + 160*m.b94 + m.x543 - m.x647 <= 320)

m.c1712 = Constraint(expr=   160*m.b87 + 160*m.b95 + m.x544 - m.x648 <= 320)

m.c1713 = Constraint(expr=   160*m.b89 + 160*m.b94 + m.x546 - m.x647 <= 320)

m.c1714 = Constraint(expr=   160*m.b90 + 160*m.b95 + m.x547 - m.x648 <= 320)

m.c1715 = Constraint(expr=   160*m.b92 + 160*m.b94 + m.x549 - m.x647 <= 320)

m.c1716 = Constraint(expr=   160*m.b93 + 160*m.b95 + m.x550 - m.x648 <= 320)

m.c1717 = Constraint(expr=   160*m.b94 + 160*m.b95 + m.x552 - m.x647 <= 320)

m.c1718 = Constraint(expr=   160*m.b95 + 160*m.b96 + m.x553 - m.x648 <= 320)

m.c1719 = Constraint(expr=   m.x651 - m.x686 >= 0)

m.c1720 = Constraint(expr=   m.x652 - m.x687 >= 0)

m.c1721 = Constraint(expr=   m.x654 - m.x689 >= 0)

m.c1722 = Constraint(expr=   m.x655 - m.x690 >= 0)

m.c1723 = Constraint(expr=   m.x657 - m.x692 >= 0)

m.c1724 = Constraint(expr=   m.x658 - m.x693 >= 0)

m.c1725 = Constraint(expr=   m.x660 - m.x695 >= 0)

m.c1726 = Constraint(expr=   m.x661 - m.x696 >= 0)

m.c1727 = Constraint(expr=   m.x663 - m.x698 >= 0)

m.c1728 = Constraint(expr=   m.x664 - m.x699 >= 0)

m.c1729 = Constraint(expr=   m.x666 - m.x701 >= 0)

m.c1730 = Constraint(expr=   m.x667 - m.x702 >= 0)

m.c1731 = Constraint(expr=   m.x669 - m.x704 >= 0)

m.c1732 = Constraint(expr=   m.x670 - m.x705 >= 0)

m.c1733 = Constraint(expr=   m.x672 - m.x707 >= 0)

m.c1734 = Constraint(expr=   m.x673 - m.x708 >= 0)

m.c1735 = Constraint(expr=   m.x675 - m.x710 >= 0)

m.c1736 = Constraint(expr=   m.x676 - m.x711 >= 0)

m.c1737 = Constraint(expr=   m.x678 - m.x713 >= 0)

m.c1738 = Constraint(expr=   m.x679 - m.x714 >= 0)

m.c1739 = Constraint(expr=   m.x681 - m.x716 >= 0)

m.c1740 = Constraint(expr=   m.x682 - m.x717 >= 0)

m.c1741 = Constraint(expr=   m.x684 - m.x719 >= 0)

m.c1742 = Constraint(expr=   m.x685 - m.x720 >= 0)

m.c1743 = Constraint(expr= - 160*m.b121 + m.x459 - m.x686 >= -160)

m.c1744 = Constraint(expr= - 160*m.b122 + m.x460 - m.x687 >= -160)

m.c1745 = Constraint(expr= - 160*m.b148 + m.x462 - m.x713 >= -160)

m.c1746 = Constraint(expr= - 160*m.b149 + m.x463 - m.x714 >= -160)

m.c1747 = Constraint(expr= - 160*m.b151 + m.x465 - m.x716 >= -160)

m.c1748 = Constraint(expr= - 160*m.b152 + m.x466 - m.x717 >= -160)

m.c1749 = Constraint(expr= - 160*m.b154 + m.x468 - m.x719 >= -160)

m.c1750 = Constraint(expr= - 160*m.b155 + m.x469 - m.x720 >= -160)

m.c1751 = Constraint(expr= - 160*m.b121 + m.x471 - m.x686 >= -160)

m.c1752 = Constraint(expr= - 160*m.b122 + m.x472 - m.x687 >= -160)

m.c1753 = Constraint(expr= - 160*m.b148 + m.x474 - m.x713 >= -160)

m.c1754 = Constraint(expr= - 160*m.b149 + m.x475 - m.x714 >= -160)

m.c1755 = Constraint(expr= - 160*m.b151 + m.x477 - m.x716 >= -160)

m.c1756 = Constraint(expr= - 160*m.b152 + m.x478 - m.x717 >= -160)

m.c1757 = Constraint(expr= - 160*m.b154 + m.x480 - m.x719 >= -160)

m.c1758 = Constraint(expr= - 160*m.b155 + m.x481 - m.x720 >= -160)

m.c1759 = Constraint(expr= - 160*m.b121 + m.x483 - m.x686 >= -160)

m.c1760 = Constraint(expr= - 160*m.b122 + m.x484 - m.x687 >= -160)

m.c1761 = Constraint(expr= - 160*m.b148 + m.x486 - m.x713 >= -160)

m.c1762 = Constraint(expr= - 160*m.b149 + m.x487 - m.x714 >= -160)

m.c1763 = Constraint(expr= - 160*m.b151 + m.x489 - m.x716 >= -160)

m.c1764 = Constraint(expr= - 160*m.b152 + m.x490 - m.x717 >= -160)

m.c1765 = Constraint(expr= - 160*m.b154 + m.x492 - m.x719 >= -160)

m.c1766 = Constraint(expr= - 160*m.b155 + m.x493 - m.x720 >= -160)

m.c1767 = Constraint(expr= - 160*m.b124 + m.x495 - m.x689 >= -160)

m.c1768 = Constraint(expr= - 160*m.b125 + m.x496 - m.x690 >= -160)

m.c1769 = Constraint(expr= - 160*m.b127 + m.x495 - m.x692 >= -160)

m.c1770 = Constraint(expr= - 160*m.b128 + m.x496 - m.x693 >= -160)

m.c1771 = Constraint(expr= - 160*m.b130 + m.x498 - m.x695 >= -160)

m.c1772 = Constraint(expr= - 160*m.b131 + m.x499 - m.x696 >= -160)

m.c1773 = Constraint(expr= - 160*m.b133 + m.x498 - m.x698 >= -160)

m.c1774 = Constraint(expr= - 160*m.b134 + m.x499 - m.x699 >= -160)

m.c1775 = Constraint(expr= - 160*m.b136 + m.x501 - m.x701 >= -160)

m.c1776 = Constraint(expr= - 160*m.b137 + m.x502 - m.x702 >= -160)

m.c1777 = Constraint(expr= - 160*m.b139 + m.x501 - m.x704 >= -160)

m.c1778 = Constraint(expr= - 160*m.b140 + m.x502 - m.x705 >= -160)

m.c1779 = Constraint(expr= - 160*m.b142 + m.x504 - m.x707 >= -160)

m.c1780 = Constraint(expr= - 160*m.b143 + m.x505 - m.x708 >= -160)

m.c1781 = Constraint(expr= - 160*m.b145 + m.x504 - m.x710 >= -160)

m.c1782 = Constraint(expr= - 160*m.b146 + m.x505 - m.x711 >= -160)

m.c1783 = Constraint(expr= - 160*m.b124 + m.x507 - m.x689 >= -160)

m.c1784 = Constraint(expr= - 160*m.b125 + m.x508 - m.x690 >= -160)

m.c1785 = Constraint(expr= - 160*m.b127 + m.x507 - m.x692 >= -160)

m.c1786 = Constraint(expr= - 160*m.b128 + m.x508 - m.x693 >= -160)

m.c1787 = Constraint(expr= - 160*m.b130 + m.x510 - m.x695 >= -160)

m.c1788 = Constraint(expr= - 160*m.b131 + m.x511 - m.x696 >= -160)

m.c1789 = Constraint(expr= - 160*m.b133 + m.x510 - m.x698 >= -160)

m.c1790 = Constraint(expr= - 160*m.b134 + m.x511 - m.x699 >= -160)

m.c1791 = Constraint(expr= - 160*m.b136 + m.x513 - m.x701 >= -160)

m.c1792 = Constraint(expr= - 160*m.b137 + m.x514 - m.x702 >= -160)

m.c1793 = Constraint(expr= - 160*m.b139 + m.x513 - m.x704 >= -160)

m.c1794 = Constraint(expr= - 160*m.b140 + m.x514 - m.x705 >= -160)

m.c1795 = Constraint(expr= - 160*m.b142 + m.x516 - m.x707 >= -160)

m.c1796 = Constraint(expr= - 160*m.b143 + m.x517 - m.x708 >= -160)

m.c1797 = Constraint(expr= - 160*m.b145 + m.x516 - m.x710 >= -160)

m.c1798 = Constraint(expr= - 160*m.b146 + m.x517 - m.x711 >= -160)

m.c1799 = Constraint(expr= - 160*m.b124 + m.x519 - m.x689 >= -160)

m.c1800 = Constraint(expr= - 160*m.b125 + m.x520 - m.x690 >= -160)

m.c1801 = Constraint(expr= - 160*m.b127 + m.x519 - m.x692 >= -160)

m.c1802 = Constraint(expr= - 160*m.b128 + m.x520 - m.x693 >= -160)

m.c1803 = Constraint(expr= - 160*m.b130 + m.x522 - m.x695 >= -160)

m.c1804 = Constraint(expr= - 160*m.b131 + m.x523 - m.x696 >= -160)

m.c1805 = Constraint(expr= - 160*m.b133 + m.x522 - m.x698 >= -160)

m.c1806 = Constraint(expr= - 160*m.b134 + m.x523 - m.x699 >= -160)

m.c1807 = Constraint(expr= - 160*m.b136 + m.x525 - m.x701 >= -160)

m.c1808 = Constraint(expr= - 160*m.b137 + m.x526 - m.x702 >= -160)

m.c1809 = Constraint(expr= - 160*m.b139 + m.x525 - m.x704 >= -160)

m.c1810 = Constraint(expr= - 160*m.b140 + m.x526 - m.x705 >= -160)

m.c1811 = Constraint(expr= - 160*m.b142 + m.x528 - m.x707 >= -160)

m.c1812 = Constraint(expr= - 160*m.b143 + m.x529 - m.x708 >= -160)

m.c1813 = Constraint(expr= - 160*m.b145 + m.x528 - m.x710 >= -160)

m.c1814 = Constraint(expr= - 160*m.b146 + m.x529 - m.x711 >= -160)

m.c1815 = Constraint(expr= - 160*m.b121 + m.x531 - m.x686 >= -160)

m.c1816 = Constraint(expr= - 160*m.b122 + m.x532 - m.x687 >= -160)

m.c1817 = Constraint(expr= - 160*m.b148 + m.x534 - m.x713 >= -160)

m.c1818 = Constraint(expr= - 160*m.b149 + m.x535 - m.x714 >= -160)

m.c1819 = Constraint(expr= - 160*m.b151 + m.x537 - m.x716 >= -160)

m.c1820 = Constraint(expr= - 160*m.b152 + m.x538 - m.x717 >= -160)

m.c1821 = Constraint(expr= - 160*m.b154 + m.x540 - m.x719 >= -160)

m.c1822 = Constraint(expr= - 160*m.b155 + m.x541 - m.x720 >= -160)

m.c1823 = Constraint(expr= - 160*m.b124 + m.x543 - m.x689 >= -160)

m.c1824 = Constraint(expr= - 160*m.b125 + m.x544 - m.x690 >= -160)

m.c1825 = Constraint(expr= - 160*m.b127 + m.x543 - m.x692 >= -160)

m.c1826 = Constraint(expr= - 160*m.b128 + m.x544 - m.x693 >= -160)

m.c1827 = Constraint(expr= - 160*m.b130 + m.x546 - m.x695 >= -160)

m.c1828 = Constraint(expr= - 160*m.b131 + m.x547 - m.x696 >= -160)

m.c1829 = Constraint(expr= - 160*m.b133 + m.x546 - m.x698 >= -160)

m.c1830 = Constraint(expr= - 160*m.b134 + m.x547 - m.x699 >= -160)

m.c1831 = Constraint(expr= - 160*m.b136 + m.x549 - m.x701 >= -160)

m.c1832 = Constraint(expr= - 160*m.b137 + m.x550 - m.x702 >= -160)

m.c1833 = Constraint(expr= - 160*m.b139 + m.x549 - m.x704 >= -160)

m.c1834 = Constraint(expr= - 160*m.b140 + m.x550 - m.x705 >= -160)

m.c1835 = Constraint(expr= - 160*m.b142 + m.x552 - m.x707 >= -160)

m.c1836 = Constraint(expr= - 160*m.b143 + m.x553 - m.x708 >= -160)

m.c1837 = Constraint(expr= - 160*m.b145 + m.x552 - m.x710 >= -160)

m.c1838 = Constraint(expr= - 160*m.b146 + m.x553 - m.x711 >= -160)

m.c1839 = Constraint(expr= - 168*m.b1 - m.x554 + m.x651 >= -160)

m.c1840 = Constraint(expr= - 168*m.b2 - m.x555 + m.x652 >= -160)

m.c1841 = Constraint(expr= - 168*m.b4 - m.x557 + m.x678 >= -160)

m.c1842 = Constraint(expr= - 168*m.b5 - m.x558 + m.x679 >= -160)

m.c1843 = Constraint(expr= - 168*m.b7 - m.x560 + m.x681 >= -160)

m.c1844 = Constraint(expr= - 168*m.b8 - m.x561 + m.x682 >= -160)

m.c1845 = Constraint(expr= - 168*m.b10 - m.x563 + m.x684 >= -160)

m.c1846 = Constraint(expr= - 168*m.b11 - m.x564 + m.x685 >= -160)

m.c1847 = Constraint(expr= - 168*m.b13 - m.x566 + m.x651 >= -160)

m.c1848 = Constraint(expr= - 168*m.b14 - m.x567 + m.x652 >= -160)

m.c1849 = Constraint(expr= - 168*m.b16 - m.x569 + m.x678 >= -160)

m.c1850 = Constraint(expr= - 168*m.b17 - m.x570 + m.x679 >= -160)

m.c1851 = Constraint(expr= - 168*m.b19 - m.x572 + m.x681 >= -160)

m.c1852 = Constraint(expr= - 168*m.b20 - m.x573 + m.x682 >= -160)

m.c1853 = Constraint(expr= - 168*m.b22 - m.x575 + m.x684 >= -160)

m.c1854 = Constraint(expr= - 168*m.b23 - m.x576 + m.x685 >= -160)

m.c1855 = Constraint(expr= - 168*m.b25 - m.x578 + m.x651 >= -160)

m.c1856 = Constraint(expr= - 168*m.b26 - m.x579 + m.x652 >= -160)

m.c1857 = Constraint(expr= - 168*m.b28 - m.x581 + m.x678 >= -160)

m.c1858 = Constraint(expr= - 168*m.b29 - m.x582 + m.x679 >= -160)

m.c1859 = Constraint(expr= - 168*m.b31 - m.x584 + m.x681 >= -160)

m.c1860 = Constraint(expr= - 168*m.b32 - m.x585 + m.x682 >= -160)

m.c1861 = Constraint(expr= - 168*m.b34 - m.x587 + m.x684 >= -160)

m.c1862 = Constraint(expr= - 168*m.b35 - m.x588 + m.x685 >= -160)

m.c1863 = Constraint(expr= - 168*m.b37 - m.x590 + m.x654 >= -160)

m.c1864 = Constraint(expr= - 168*m.b38 - m.x591 + m.x655 >= -160)

m.c1865 = Constraint(expr= - 168*m.b37 - m.x590 + m.x657 >= -160)

m.c1866 = Constraint(expr= - 168*m.b38 - m.x591 + m.x658 >= -160)

m.c1867 = Constraint(expr= - 168*m.b40 - m.x593 + m.x660 >= -160)

m.c1868 = Constraint(expr= - 168*m.b41 - m.x594 + m.x661 >= -160)

m.c1869 = Constraint(expr= - 168*m.b40 - m.x593 + m.x663 >= -160)

m.c1870 = Constraint(expr= - 168*m.b41 - m.x594 + m.x664 >= -160)

m.c1871 = Constraint(expr= - 168*m.b43 - m.x596 + m.x666 >= -160)

m.c1872 = Constraint(expr= - 168*m.b44 - m.x597 + m.x667 >= -160)

m.c1873 = Constraint(expr= - 168*m.b43 - m.x596 + m.x669 >= -160)

m.c1874 = Constraint(expr= - 168*m.b44 - m.x597 + m.x670 >= -160)

m.c1875 = Constraint(expr= - 168*m.b46 - m.x599 + m.x672 >= -160)

m.c1876 = Constraint(expr= - 168*m.b47 - m.x600 + m.x673 >= -160)

m.c1877 = Constraint(expr= - 168*m.b46 - m.x599 + m.x675 >= -160)

m.c1878 = Constraint(expr= - 168*m.b47 - m.x600 + m.x676 >= -160)

m.c1879 = Constraint(expr= - 168*m.b49 - m.x602 + m.x654 >= -160)

m.c1880 = Constraint(expr= - 168*m.b50 - m.x603 + m.x655 >= -160)

m.c1881 = Constraint(expr= - 168*m.b49 - m.x602 + m.x657 >= -160)

m.c1882 = Constraint(expr= - 168*m.b50 - m.x603 + m.x658 >= -160)

m.c1883 = Constraint(expr= - 168*m.b52 - m.x605 + m.x660 >= -160)

m.c1884 = Constraint(expr= - 168*m.b53 - m.x606 + m.x661 >= -160)

m.c1885 = Constraint(expr= - 168*m.b52 - m.x605 + m.x663 >= -160)

m.c1886 = Constraint(expr= - 168*m.b53 - m.x606 + m.x664 >= -160)

m.c1887 = Constraint(expr= - 168*m.b55 - m.x608 + m.x666 >= -160)

m.c1888 = Constraint(expr= - 168*m.b56 - m.x609 + m.x667 >= -160)

m.c1889 = Constraint(expr= - 168*m.b55 - m.x608 + m.x669 >= -160)

m.c1890 = Constraint(expr= - 168*m.b56 - m.x609 + m.x670 >= -160)

m.c1891 = Constraint(expr= - 168*m.b58 - m.x611 + m.x672 >= -160)

m.c1892 = Constraint(expr= - 168*m.b59 - m.x612 + m.x673 >= -160)

m.c1893 = Constraint(expr= - 168*m.b58 - m.x611 + m.x675 >= -160)

m.c1894 = Constraint(expr= - 168*m.b59 - m.x612 + m.x676 >= -160)

m.c1895 = Constraint(expr= - 168*m.b61 - m.x614 + m.x654 >= -160)

m.c1896 = Constraint(expr= - 168*m.b62 - m.x615 + m.x655 >= -160)

m.c1897 = Constraint(expr= - 168*m.b61 - m.x614 + m.x657 >= -160)

m.c1898 = Constraint(expr= - 168*m.b62 - m.x615 + m.x658 >= -160)

m.c1899 = Constraint(expr= - 168*m.b64 - m.x617 + m.x660 >= -160)

m.c1900 = Constraint(expr= - 168*m.b65 - m.x618 + m.x661 >= -160)

m.c1901 = Constraint(expr= - 168*m.b64 - m.x617 + m.x663 >= -160)

m.c1902 = Constraint(expr= - 168*m.b65 - m.x618 + m.x664 >= -160)

m.c1903 = Constraint(expr= - 168*m.b67 - m.x620 + m.x666 >= -160)

m.c1904 = Constraint(expr= - 168*m.b68 - m.x621 + m.x667 >= -160)

m.c1905 = Constraint(expr= - 168*m.b67 - m.x620 + m.x669 >= -160)

m.c1906 = Constraint(expr= - 168*m.b68 - m.x621 + m.x670 >= -160)

m.c1907 = Constraint(expr= - 168*m.b70 - m.x623 + m.x672 >= -160)

m.c1908 = Constraint(expr= - 168*m.b71 - m.x624 + m.x673 >= -160)

m.c1909 = Constraint(expr= - 168*m.b70 - m.x623 + m.x675 >= -160)

m.c1910 = Constraint(expr= - 168*m.b71 - m.x624 + m.x676 >= -160)

m.c1911 = Constraint(expr= - 168*m.b73 - m.x626 + m.x651 >= -160)

m.c1912 = Constraint(expr= - 168*m.b74 - m.x627 + m.x652 >= -160)

m.c1913 = Constraint(expr= - 168*m.b76 - m.x629 + m.x678 >= -160)

m.c1914 = Constraint(expr= - 168*m.b77 - m.x630 + m.x679 >= -160)

m.c1915 = Constraint(expr= - 168*m.b79 - m.x632 + m.x681 >= -160)

m.c1916 = Constraint(expr= - 168*m.b80 - m.x633 + m.x682 >= -160)

m.c1917 = Constraint(expr= - 168*m.b82 - m.x635 + m.x684 >= -160)

m.c1918 = Constraint(expr= - 168*m.b83 - m.x636 + m.x685 >= -160)

m.c1919 = Constraint(expr= - 168*m.b85 - m.x638 + m.x654 >= -160)

m.c1920 = Constraint(expr= - 168*m.b86 - m.x639 + m.x655 >= -160)

m.c1921 = Constraint(expr= - 168*m.b85 - m.x638 + m.x657 >= -160)

m.c1922 = Constraint(expr= - 168*m.b86 - m.x639 + m.x658 >= -160)

m.c1923 = Constraint(expr= - 168*m.b88 - m.x641 + m.x660 >= -160)

m.c1924 = Constraint(expr= - 168*m.b89 - m.x642 + m.x661 >= -160)

m.c1925 = Constraint(expr= - 168*m.b88 - m.x641 + m.x663 >= -160)

m.c1926 = Constraint(expr= - 168*m.b89 - m.x642 + m.x664 >= -160)

m.c1927 = Constraint(expr= - 168*m.b91 - m.x644 + m.x666 >= -160)

m.c1928 = Constraint(expr= - 168*m.b92 - m.x645 + m.x667 >= -160)

m.c1929 = Constraint(expr= - 168*m.b91 - m.x644 + m.x669 >= -160)

m.c1930 = Constraint(expr= - 168*m.b92 - m.x645 + m.x670 >= -160)

m.c1931 = Constraint(expr= - 168*m.b94 - m.x647 + m.x672 >= -160)

m.c1932 = Constraint(expr= - 168*m.b95 - m.x648 + m.x673 >= -160)

m.c1933 = Constraint(expr= - 168*m.b94 - m.x647 + m.x675 >= -160)

m.c1934 = Constraint(expr= - 168*m.b95 - m.x648 + m.x676 >= -160)

m.c1935 = Constraint(expr= - 160*m.b127 + m.x654 - m.x692 >= -160)

m.c1936 = Constraint(expr= - 160*m.b128 + m.x655 - m.x693 >= -160)

m.c1937 = Constraint(expr= - 160*m.b124 + m.x657 - m.x689 >= -160)

m.c1938 = Constraint(expr= - 160*m.b125 + m.x658 - m.x690 >= -160)

m.c1939 = Constraint(expr= - 160*m.b133 + m.x660 - m.x698 >= -160)

m.c1940 = Constraint(expr= - 160*m.b134 + m.x661 - m.x699 >= -160)

m.c1941 = Constraint(expr= - 160*m.b130 + m.x663 - m.x695 >= -160)

m.c1942 = Constraint(expr= - 160*m.b131 + m.x664 - m.x696 >= -160)

m.c1943 = Constraint(expr= - 160*m.b139 + m.x666 - m.x704 >= -160)

m.c1944 = Constraint(expr= - 160*m.b140 + m.x667 - m.x705 >= -160)

m.c1945 = Constraint(expr= - 160*m.b136 + m.x669 - m.x701 >= -160)

m.c1946 = Constraint(expr= - 160*m.b137 + m.x670 - m.x702 >= -160)

m.c1947 = Constraint(expr= - 160*m.b145 + m.x672 - m.x710 >= -160)

m.c1948 = Constraint(expr= - 160*m.b146 + m.x673 - m.x711 >= -160)

m.c1949 = Constraint(expr= - 160*m.b142 + m.x675 - m.x707 >= -160)

m.c1950 = Constraint(expr= - 160*m.b143 + m.x676 - m.x708 >= -160)

m.c1951 = Constraint(expr=   m.x723 - m.x731 >= 0)

m.c1952 = Constraint(expr=   m.x724 - m.x732 >= 0)

m.c1953 = Constraint(expr=   m.x726 - m.x734 >= 0)

m.c1954 = Constraint(expr=   m.x727 - m.x735 >= 0)

m.c1955 = Constraint(expr=   m.x729 - m.x737 >= 0)

m.c1956 = Constraint(expr=   m.x730 - m.x738 >= 0)

m.c1957 = Constraint(expr= - 160*m.b121 - m.x650 + m.x728 >= -160)

m.c1958 = Constraint(expr= - 160*m.b122 - m.x651 + m.x729 >= -160)

m.c1959 = Constraint(expr= - 160*m.b123 - m.x652 + m.x730 >= -160)

m.c1960 = Constraint(expr= - 160*m.b124 - m.x653 + m.x722 >= -160)

m.c1961 = Constraint(expr= - 160*m.b125 - m.x654 + m.x723 >= -160)

m.c1962 = Constraint(expr= - 160*m.b126 - m.x655 + m.x724 >= -160)

m.c1963 = Constraint(expr= - 160*m.b127 - m.x656 + m.x725 >= -160)

m.c1964 = Constraint(expr= - 160*m.b128 - m.x657 + m.x726 >= -160)

m.c1965 = Constraint(expr= - 160*m.b129 - m.x658 + m.x727 >= -160)

m.c1966 = Constraint(expr= - 160*m.b130 - m.x659 + m.x722 >= -160)

m.c1967 = Constraint(expr= - 160*m.b131 - m.x660 + m.x723 >= -160)

m.c1968 = Constraint(expr= - 160*m.b132 - m.x661 + m.x724 >= -160)

m.c1969 = Constraint(expr= - 160*m.b133 - m.x662 + m.x725 >= -160)

m.c1970 = Constraint(expr= - 160*m.b134 - m.x663 + m.x726 >= -160)

m.c1971 = Constraint(expr= - 160*m.b135 - m.x664 + m.x727 >= -160)

m.c1972 = Constraint(expr= - 160*m.b136 - m.x665 + m.x722 >= -160)

m.c1973 = Constraint(expr= - 160*m.b137 - m.x666 + m.x723 >= -160)

m.c1974 = Constraint(expr= - 160*m.b138 - m.x667 + m.x724 >= -160)

m.c1975 = Constraint(expr= - 160*m.b139 - m.x668 + m.x725 >= -160)

m.c1976 = Constraint(expr= - 160*m.b140 - m.x669 + m.x726 >= -160)

m.c1977 = Constraint(expr= - 160*m.b141 - m.x670 + m.x727 >= -160)

m.c1978 = Constraint(expr= - 160*m.b142 - m.x671 + m.x722 >= -160)

m.c1979 = Constraint(expr= - 160*m.b143 - m.x672 + m.x723 >= -160)

m.c1980 = Constraint(expr= - 160*m.b144 - m.x673 + m.x724 >= -160)

m.c1981 = Constraint(expr= - 160*m.b145 - m.x674 + m.x725 >= -160)

m.c1982 = Constraint(expr= - 160*m.b146 - m.x675 + m.x726 >= -160)

m.c1983 = Constraint(expr= - 160*m.b147 - m.x676 + m.x727 >= -160)

m.c1984 = Constraint(expr= - 160*m.b148 - m.x677 + m.x728 >= -160)

m.c1985 = Constraint(expr= - 160*m.b149 - m.x678 + m.x729 >= -160)

m.c1986 = Constraint(expr= - 160*m.b150 - m.x679 + m.x730 >= -160)

m.c1987 = Constraint(expr= - 160*m.b151 - m.x680 + m.x728 >= -160)

m.c1988 = Constraint(expr= - 160*m.b152 - m.x681 + m.x729 >= -160)

m.c1989 = Constraint(expr= - 160*m.b153 - m.x682 + m.x730 >= -160)

m.c1990 = Constraint(expr= - 160*m.b154 - m.x683 + m.x728 >= -160)

m.c1991 = Constraint(expr= - 160*m.b155 - m.x684 + m.x729 >= -160)

m.c1992 = Constraint(expr= - 160*m.b156 - m.x685 + m.x730 >= -160)

m.c1993 = Constraint(expr=   160*m.b121 - m.x650 + m.x728 <= 160)

m.c1994 = Constraint(expr=   160*m.b122 - m.x651 + m.x729 <= 160)

m.c1995 = Constraint(expr=   160*m.b123 - m.x652 + m.x730 <= 160)

m.c1996 = Constraint(expr=   160*m.b124 - m.x653 + m.x722 <= 160)

m.c1997 = Constraint(expr=   160*m.b125 - m.x654 + m.x723 <= 160)

m.c1998 = Constraint(expr=   160*m.b126 - m.x655 + m.x724 <= 160)

m.c1999 = Constraint(expr=   160*m.b127 - m.x656 + m.x725 <= 160)

m.c2000 = Constraint(expr=   160*m.b128 - m.x657 + m.x726 <= 160)

m.c2001 = Constraint(expr=   160*m.b129 - m.x658 + m.x727 <= 160)

m.c2002 = Constraint(expr=   160*m.b130 - m.x659 + m.x722 <= 160)

m.c2003 = Constraint(expr=   160*m.b131 - m.x660 + m.x723 <= 160)

m.c2004 = Constraint(expr=   160*m.b132 - m.x661 + m.x724 <= 160)

m.c2005 = Constraint(expr=   160*m.b133 - m.x662 + m.x725 <= 160)

m.c2006 = Constraint(expr=   160*m.b134 - m.x663 + m.x726 <= 160)

m.c2007 = Constraint(expr=   160*m.b135 - m.x664 + m.x727 <= 160)

m.c2008 = Constraint(expr=   160*m.b136 - m.x665 + m.x722 <= 160)

m.c2009 = Constraint(expr=   160*m.b137 - m.x666 + m.x723 <= 160)

m.c2010 = Constraint(expr=   160*m.b138 - m.x667 + m.x724 <= 160)

m.c2011 = Constraint(expr=   160*m.b139 - m.x668 + m.x725 <= 160)

m.c2012 = Constraint(expr=   160*m.b140 - m.x669 + m.x726 <= 160)

m.c2013 = Constraint(expr=   160*m.b141 - m.x670 + m.x727 <= 160)

m.c2014 = Constraint(expr=   160*m.b142 - m.x671 + m.x722 <= 160)

m.c2015 = Constraint(expr=   160*m.b143 - m.x672 + m.x723 <= 160)

m.c2016 = Constraint(expr=   160*m.b144 - m.x673 + m.x724 <= 160)

m.c2017 = Constraint(expr=   160*m.b145 - m.x674 + m.x725 <= 160)

m.c2018 = Constraint(expr=   160*m.b146 - m.x675 + m.x726 <= 160)

m.c2019 = Constraint(expr=   160*m.b147 - m.x676 + m.x727 <= 160)

m.c2020 = Constraint(expr=   160*m.b148 - m.x677 + m.x728 <= 160)

m.c2021 = Constraint(expr=   160*m.b149 - m.x678 + m.x729 <= 160)

m.c2022 = Constraint(expr=   160*m.b150 - m.x679 + m.x730 <= 160)

m.c2023 = Constraint(expr=   160*m.b151 - m.x680 + m.x728 <= 160)

m.c2024 = Constraint(expr=   160*m.b152 - m.x681 + m.x729 <= 160)

m.c2025 = Constraint(expr=   160*m.b153 - m.x682 + m.x730 <= 160)

m.c2026 = Constraint(expr=   160*m.b154 - m.x683 + m.x728 <= 160)

m.c2027 = Constraint(expr=   160*m.b155 - m.x684 + m.x729 <= 160)

m.c2028 = Constraint(expr=   160*m.b156 - m.x685 + m.x730 <= 160)

m.c2029 = Constraint(expr= - 160*m.b121 - m.x686 + m.x737 >= -160)

m.c2030 = Constraint(expr= - 160*m.b122 - m.x687 + m.x738 >= -160)

m.c2031 = Constraint(expr= - 160*m.b123 - m.x688 + m.x739 >= -160)

m.c2032 = Constraint(expr= - 160*m.b124 - m.x689 + m.x731 >= -160)

m.c2033 = Constraint(expr= - 160*m.b125 - m.x690 + m.x732 >= -160)

m.c2034 = Constraint(expr= - 160*m.b126 - m.x691 + m.x733 >= -160)

m.c2035 = Constraint(expr= - 160*m.b127 - m.x692 + m.x734 >= -160)

m.c2036 = Constraint(expr= - 160*m.b128 - m.x693 + m.x735 >= -160)

m.c2037 = Constraint(expr= - 160*m.b129 - m.x694 + m.x736 >= -160)

m.c2038 = Constraint(expr= - 160*m.b130 - m.x695 + m.x731 >= -160)

m.c2039 = Constraint(expr= - 160*m.b131 - m.x696 + m.x732 >= -160)

m.c2040 = Constraint(expr= - 160*m.b132 - m.x697 + m.x733 >= -160)

m.c2041 = Constraint(expr= - 160*m.b133 - m.x698 + m.x734 >= -160)

m.c2042 = Constraint(expr= - 160*m.b134 - m.x699 + m.x735 >= -160)

m.c2043 = Constraint(expr= - 160*m.b135 - m.x700 + m.x736 >= -160)

m.c2044 = Constraint(expr= - 160*m.b136 - m.x701 + m.x731 >= -160)

m.c2045 = Constraint(expr= - 160*m.b137 - m.x702 + m.x732 >= -160)

m.c2046 = Constraint(expr= - 160*m.b138 - m.x703 + m.x733 >= -160)

m.c2047 = Constraint(expr= - 160*m.b139 - m.x704 + m.x734 >= -160)

m.c2048 = Constraint(expr= - 160*m.b140 - m.x705 + m.x735 >= -160)

m.c2049 = Constraint(expr= - 160*m.b141 - m.x706 + m.x736 >= -160)

m.c2050 = Constraint(expr= - 160*m.b142 - m.x707 + m.x731 >= -160)

m.c2051 = Constraint(expr= - 160*m.b143 - m.x708 + m.x732 >= -160)

m.c2052 = Constraint(expr= - 160*m.b144 - m.x709 + m.x733 >= -160)

m.c2053 = Constraint(expr= - 160*m.b145 - m.x710 + m.x734 >= -160)

m.c2054 = Constraint(expr= - 160*m.b146 - m.x711 + m.x735 >= -160)

m.c2055 = Constraint(expr= - 160*m.b147 - m.x712 + m.x736 >= -160)

m.c2056 = Constraint(expr= - 160*m.b148 - m.x713 + m.x737 >= -160)

m.c2057 = Constraint(expr= - 160*m.b149 - m.x714 + m.x738 >= -160)

m.c2058 = Constraint(expr= - 160*m.b150 - m.x715 + m.x739 >= -160)

m.c2059 = Constraint(expr= - 160*m.b151 - m.x716 + m.x737 >= -160)

m.c2060 = Constraint(expr= - 160*m.b152 - m.x717 + m.x738 >= -160)

m.c2061 = Constraint(expr= - 160*m.b153 - m.x718 + m.x739 >= -160)

m.c2062 = Constraint(expr= - 160*m.b154 - m.x719 + m.x737 >= -160)

m.c2063 = Constraint(expr= - 160*m.b155 - m.x720 + m.x738 >= -160)

m.c2064 = Constraint(expr= - 160*m.b156 - m.x721 + m.x739 >= -160)

m.c2065 = Constraint(expr=   160*m.b121 - m.x686 + m.x737 <= 160)

m.c2066 = Constraint(expr=   160*m.b122 - m.x687 + m.x738 <= 160)

m.c2067 = Constraint(expr=   160*m.b123 - m.x688 + m.x739 <= 160)

m.c2068 = Constraint(expr=   160*m.b124 - m.x689 + m.x731 <= 160)

m.c2069 = Constraint(expr=   160*m.b125 - m.x690 + m.x732 <= 160)

m.c2070 = Constraint(expr=   160*m.b126 - m.x691 + m.x733 <= 160)

m.c2071 = Constraint(expr=   160*m.b127 - m.x692 + m.x734 <= 160)

m.c2072 = Constraint(expr=   160*m.b128 - m.x693 + m.x735 <= 160)

m.c2073 = Constraint(expr=   160*m.b129 - m.x694 + m.x736 <= 160)

m.c2074 = Constraint(expr=   160*m.b130 - m.x695 + m.x731 <= 160)

m.c2075 = Constraint(expr=   160*m.b131 - m.x696 + m.x732 <= 160)

m.c2076 = Constraint(expr=   160*m.b132 - m.x697 + m.x733 <= 160)

m.c2077 = Constraint(expr=   160*m.b133 - m.x698 + m.x734 <= 160)

m.c2078 = Constraint(expr=   160*m.b134 - m.x699 + m.x735 <= 160)

m.c2079 = Constraint(expr=   160*m.b135 - m.x700 + m.x736 <= 160)

m.c2080 = Constraint(expr=   160*m.b136 - m.x701 + m.x731 <= 160)

m.c2081 = Constraint(expr=   160*m.b137 - m.x702 + m.x732 <= 160)

m.c2082 = Constraint(expr=   160*m.b138 - m.x703 + m.x733 <= 160)

m.c2083 = Constraint(expr=   160*m.b139 - m.x704 + m.x734 <= 160)

m.c2084 = Constraint(expr=   160*m.b140 - m.x705 + m.x735 <= 160)

m.c2085 = Constraint(expr=   160*m.b141 - m.x706 + m.x736 <= 160)

m.c2086 = Constraint(expr=   160*m.b142 - m.x707 + m.x731 <= 160)

m.c2087 = Constraint(expr=   160*m.b143 - m.x708 + m.x732 <= 160)

m.c2088 = Constraint(expr=   160*m.b144 - m.x709 + m.x733 <= 160)

m.c2089 = Constraint(expr=   160*m.b145 - m.x710 + m.x734 <= 160)

m.c2090 = Constraint(expr=   160*m.b146 - m.x711 + m.x735 <= 160)

m.c2091 = Constraint(expr=   160*m.b147 - m.x712 + m.x736 <= 160)

m.c2092 = Constraint(expr=   160*m.b148 - m.x713 + m.x737 <= 160)

m.c2093 = Constraint(expr=   160*m.b149 - m.x714 + m.x738 <= 160)

m.c2094 = Constraint(expr=   160*m.b150 - m.x715 + m.x739 <= 160)

m.c2095 = Constraint(expr=   160*m.b151 - m.x716 + m.x737 <= 160)

m.c2096 = Constraint(expr=   160*m.b152 - m.x717 + m.x738 <= 160)

m.c2097 = Constraint(expr=   160*m.b153 - m.x718 + m.x739 <= 160)

m.c2098 = Constraint(expr=   160*m.b154 - m.x719 + m.x737 <= 160)

m.c2099 = Constraint(expr=   160*m.b155 - m.x720 + m.x738 <= 160)

m.c2100 = Constraint(expr=   160*m.b156 - m.x721 + m.x739 <= 160)

m.c2101 = Constraint(expr=   m.x194 - m.x764 + m.x765 == 0)

m.c2102 = Constraint(expr=   m.x195 - m.x765 + m.x766 == 0)

m.c2103 = Constraint(expr=   m.x197 - m.x347 - m.x767 + m.x768 == 0)

m.c2104 = Constraint(expr=   m.x198 - m.x348 - m.x768 + m.x769 == 0)

m.c2105 = Constraint(expr=   m.x200 - m.x359 - m.x419 - m.x770 + m.x771 == 0)

m.c2106 = Constraint(expr=   m.x201 - m.x360 - m.x420 - m.x771 + m.x772 == 0)

m.c2107 = Constraint(expr=   m.x203 - m.x371 - m.x773 + m.x774 == 0)

m.c2108 = Constraint(expr=   m.x204 - m.x372 - m.x774 + m.x775 == 0)

m.c2109 = Constraint(expr=   m.x206 + m.x218 - m.x383 - m.x395 - m.x776 + m.x777 == 0)

m.c2110 = Constraint(expr=   m.x207 + m.x219 - m.x384 - m.x396 - m.x777 + m.x778 == 0)

m.c2111 = Constraint(expr=   m.x209 + m.x221 - m.x407 - m.x779 + m.x780 == 0)

m.c2112 = Constraint(expr=   m.x210 + m.x222 - m.x408 - m.x780 + m.x781 == 0)

m.c2113 = Constraint(expr=   m.x212 + m.x224 - m.x782 + m.x783 == 0)

m.c2114 = Constraint(expr=   m.x213 + m.x225 - m.x783 + m.x784 == 0)

m.c2115 = Constraint(expr=   m.x215 + m.x227 - m.x431 - m.x785 + m.x786 == 0)

m.c2116 = Constraint(expr=   m.x216 + m.x228 - m.x432 - m.x786 + m.x787 == 0)

m.c2117 = Constraint(expr=   m.x230 + m.x242 - m.x386 - m.x398 - m.x788 + m.x789 == 0)

m.c2118 = Constraint(expr=   m.x231 + m.x243 - m.x387 - m.x399 - m.x789 + m.x790 == 0)

m.c2119 = Constraint(expr=   m.x233 + m.x245 - m.x410 - m.x791 + m.x792 == 0)

m.c2120 = Constraint(expr=   m.x234 + m.x246 - m.x411 - m.x792 + m.x793 == 0)

m.c2121 = Constraint(expr=   m.x236 + m.x248 - m.x794 + m.x795 == 0)

m.c2122 = Constraint(expr=   m.x237 + m.x249 - m.x795 + m.x796 == 0)

m.c2123 = Constraint(expr=   m.x239 + m.x251 - m.x434 - m.x797 + m.x798 == 0)

m.c2124 = Constraint(expr=   m.x240 + m.x252 - m.x435 - m.x798 + m.x799 == 0)

m.c2125 = Constraint(expr=   m.x254 + m.x266 - m.x389 - m.x401 - m.x800 + m.x801 == 0)

m.c2126 = Constraint(expr=   m.x255 + m.x267 - m.x390 - m.x402 - m.x801 + m.x802 == 0)

m.c2127 = Constraint(expr=   m.x257 + m.x269 - m.x413 - m.x803 + m.x804 == 0)

m.c2128 = Constraint(expr=   m.x258 + m.x270 - m.x414 - m.x804 + m.x805 == 0)

m.c2129 = Constraint(expr=   m.x260 + m.x272 - m.x806 + m.x807 == 0)

m.c2130 = Constraint(expr=   m.x261 + m.x273 - m.x807 + m.x808 == 0)

m.c2131 = Constraint(expr=   m.x263 + m.x275 - m.x437 - m.x809 + m.x810 == 0)

m.c2132 = Constraint(expr=   m.x264 + m.x276 - m.x438 - m.x810 + m.x811 == 0)

m.c2133 = Constraint(expr=   m.x278 + m.x290 - m.x392 - m.x404 - m.x812 + m.x813 == 0)

m.c2134 = Constraint(expr=   m.x279 + m.x291 - m.x393 - m.x405 - m.x813 + m.x814 == 0)

m.c2135 = Constraint(expr=   m.x281 + m.x293 - m.x416 - m.x815 + m.x816 == 0)

m.c2136 = Constraint(expr=   m.x282 + m.x294 - m.x417 - m.x816 + m.x817 == 0)

m.c2137 = Constraint(expr=   m.x284 + m.x296 - m.x818 + m.x819 == 0)

m.c2138 = Constraint(expr=   m.x285 + m.x297 - m.x819 + m.x820 == 0)

m.c2139 = Constraint(expr=   m.x287 + m.x299 - m.x440 - m.x821 + m.x822 == 0)

m.c2140 = Constraint(expr=   m.x288 + m.x300 - m.x441 - m.x822 + m.x823 == 0)

m.c2141 = Constraint(expr=   m.x302 - m.x824 + m.x825 == 0)

m.c2142 = Constraint(expr=   m.x303 - m.x825 + m.x826 == 0)

m.c2143 = Constraint(expr=   m.x305 - m.x350 - m.x827 + m.x828 == 0)

m.c2144 = Constraint(expr=   m.x306 - m.x351 - m.x828 + m.x829 == 0)

m.c2145 = Constraint(expr=   m.x308 - m.x362 - m.x422 - m.x830 + m.x831 == 0)

m.c2146 = Constraint(expr=   m.x309 - m.x363 - m.x423 - m.x831 + m.x832 == 0)

m.c2147 = Constraint(expr=   m.x311 - m.x374 - m.x833 + m.x834 == 0)

m.c2148 = Constraint(expr=   m.x312 - m.x375 - m.x834 + m.x835 == 0)

m.c2149 = Constraint(expr=   m.x314 - m.x836 + m.x837 == 0)

m.c2150 = Constraint(expr=   m.x315 - m.x837 + m.x838 == 0)

m.c2151 = Constraint(expr=   m.x317 - m.x353 - m.x839 + m.x840 == 0)

m.c2152 = Constraint(expr=   m.x318 - m.x354 - m.x840 + m.x841 == 0)

m.c2153 = Constraint(expr=   m.x320 - m.x365 - m.x425 - m.x842 + m.x843 == 0)

m.c2154 = Constraint(expr=   m.x321 - m.x366 - m.x426 - m.x843 + m.x844 == 0)

m.c2155 = Constraint(expr=   m.x323 - m.x377 - m.x845 + m.x846 == 0)

m.c2156 = Constraint(expr=   m.x324 - m.x378 - m.x846 + m.x847 == 0)

m.c2157 = Constraint(expr=   m.x326 - m.x848 + m.x849 == 0)

m.c2158 = Constraint(expr=   m.x327 - m.x849 + m.x850 == 0)

m.c2159 = Constraint(expr=   m.x329 - m.x356 - m.x851 + m.x852 == 0)

m.c2160 = Constraint(expr=   m.x330 - m.x357 - m.x852 + m.x853 == 0)

m.c2161 = Constraint(expr=   m.x332 - m.x368 - m.x428 - m.x854 + m.x855 == 0)

m.c2162 = Constraint(expr=   m.x333 - m.x369 - m.x429 - m.x855 + m.x856 == 0)

m.c2163 = Constraint(expr=   m.x335 - m.x380 - m.x857 + m.x858 == 0)

m.c2164 = Constraint(expr=   m.x336 - m.x381 - m.x858 + m.x859 == 0)

m.c2165 = Constraint(expr=   m.x193 + m.x764 == 50)

m.c2166 = Constraint(expr=   m.x196 - m.x346 + m.x767 == 100)

m.c2167 = Constraint(expr=   m.x199 - m.x358 - m.x418 + m.x770 == 100)

m.c2168 = Constraint(expr=   m.x202 - m.x370 + m.x773 == 100)

m.c2169 = Constraint(expr=   m.x205 + m.x217 - m.x382 - m.x394 + m.x776 == 100)

m.c2170 = Constraint(expr=   m.x208 + m.x220 - m.x406 + m.x779 == 100)

m.c2171 = Constraint(expr=   m.x211 + m.x223 + m.x782 == 100)

m.c2172 = Constraint(expr=   m.x214 + m.x226 - m.x430 + m.x785 == 100)

m.c2173 = Constraint(expr=   m.x229 + m.x241 - m.x385 - m.x397 + m.x788 == 100)

m.c2174 = Constraint(expr=   m.x232 + m.x244 - m.x409 + m.x791 == 100)

m.c2175 = Constraint(expr=   m.x235 + m.x247 + m.x794 == 50)

m.c2176 = Constraint(expr=   m.x238 + m.x250 - m.x433 + m.x797 == 100)

m.c2177 = Constraint(expr=   m.x253 + m.x265 - m.x388 - m.x400 + m.x800 == 200)

m.c2178 = Constraint(expr=   m.x256 + m.x268 - m.x412 + m.x803 == 250)

m.c2179 = Constraint(expr=   m.x259 + m.x271 + m.x806 == 200)

m.c2180 = Constraint(expr=   m.x262 + m.x274 - m.x436 + m.x809 == 300)

m.c2181 = Constraint(expr=   m.x277 + m.x289 - m.x391 - m.x403 + m.x812 == 100)

m.c2182 = Constraint(expr=   m.x280 + m.x292 - m.x415 + m.x815 == 100)

m.c2183 = Constraint(expr=   m.x283 + m.x295 + m.x818 == 50)

m.c2184 = Constraint(expr=   m.x286 + m.x298 - m.x439 + m.x821 == 50)

m.c2185 = Constraint(expr=   m.x301 + m.x824 == 20)

m.c2186 = Constraint(expr=   m.x304 - m.x349 + m.x827 == 20)

m.c2187 = Constraint(expr=   m.x307 - m.x361 - m.x421 + m.x830 == 20)

m.c2188 = Constraint(expr=   m.x310 - m.x373 + m.x833 == 20)

m.c2189 = Constraint(expr=   m.x313 + m.x836 == 20)

m.c2190 = Constraint(expr=   m.x316 - m.x352 + m.x839 == 20)

m.c2191 = Constraint(expr=   m.x319 - m.x364 - m.x424 + m.x842 == 20)

m.c2192 = Constraint(expr=   m.x322 - m.x376 + m.x845 == 20)

m.c2193 = Constraint(expr=   m.x325 + m.x848 == 100)

m.c2194 = Constraint(expr=   m.x328 - m.x355 + m.x851 == 100)

m.c2195 = Constraint(expr=   m.x331 - m.x367 - m.x427 + m.x854 == 100)

m.c2196 = Constraint(expr=   m.x334 - m.x379 + m.x857 == 150)

m.c2197 = Constraint(expr= - m.x722 - m.x723 - m.x724 + m.x731 + m.x732 + m.x733 == 160)

m.c2198 = Constraint(expr= - m.x725 - m.x726 - m.x727 + m.x734 + m.x735 + m.x736 == 160)

m.c2199 = Constraint(expr= - m.x728 - m.x729 - m.x730 + m.x737 + m.x738 + m.x739 == 160)

m.c2200 = Constraint(expr= - m.b121 + m.b122 + m.x864 >= 0)

m.c2201 = Constraint(expr= - m.b122 + m.b123 + m.x865 >= 0)

m.c2202 = Constraint(expr= - m.b124 + m.b125 + m.x860 >= 0)

m.c2203 = Constraint(expr= - m.b125 + m.b126 + m.x861 >= 0)

m.c2204 = Constraint(expr= - m.b127 + m.b128 + m.x862 >= 0)

m.c2205 = Constraint(expr= - m.b128 + m.b129 + m.x863 >= 0)

m.c2206 = Constraint(expr= - m.b130 + m.b131 + m.x860 >= 0)

m.c2207 = Constraint(expr= - m.b131 + m.b132 + m.x861 >= 0)

m.c2208 = Constraint(expr= - m.b133 + m.b134 + m.x862 >= 0)

m.c2209 = Constraint(expr= - m.b134 + m.b135 + m.x863 >= 0)

m.c2210 = Constraint(expr= - m.b136 + m.b137 + m.x860 >= 0)

m.c2211 = Constraint(expr= - m.b137 + m.b138 + m.x861 >= 0)

m.c2212 = Constraint(expr= - m.b139 + m.b140 + m.x862 >= 0)

m.c2213 = Constraint(expr= - m.b140 + m.b141 + m.x863 >= 0)

m.c2214 = Constraint(expr= - m.b142 + m.b143 + m.x860 >= 0)

m.c2215 = Constraint(expr= - m.b143 + m.b144 + m.x861 >= 0)

m.c2216 = Constraint(expr= - m.b145 + m.b146 + m.x862 >= 0)

m.c2217 = Constraint(expr= - m.b146 + m.b147 + m.x863 >= 0)

m.c2218 = Constraint(expr= - m.b148 + m.b149 + m.x864 >= 0)

m.c2219 = Constraint(expr= - m.b149 + m.b150 + m.x865 >= 0)

m.c2220 = Constraint(expr= - m.b151 + m.b152 + m.x864 >= 0)

m.c2221 = Constraint(expr= - m.b152 + m.b153 + m.x865 >= 0)

m.c2222 = Constraint(expr= - m.b154 + m.b155 + m.x864 >= 0)

m.c2223 = Constraint(expr= - m.b155 + m.b156 + m.x865 >= 0)

m.c2224 = Constraint(expr=   m.b121 - m.b122 + m.x864 >= 0)

m.c2225 = Constraint(expr=   m.b122 - m.b123 + m.x865 >= 0)

m.c2226 = Constraint(expr=   m.b124 - m.b125 + m.x860 >= 0)

m.c2227 = Constraint(expr=   m.b125 - m.b126 + m.x861 >= 0)

m.c2228 = Constraint(expr=   m.b127 - m.b128 + m.x862 >= 0)

m.c2229 = Constraint(expr=   m.b128 - m.b129 + m.x863 >= 0)

m.c2230 = Constraint(expr=   m.b130 - m.b131 + m.x860 >= 0)

m.c2231 = Constraint(expr=   m.b131 - m.b132 + m.x861 >= 0)

m.c2232 = Constraint(expr=   m.b133 - m.b134 + m.x862 >= 0)

m.c2233 = Constraint(expr=   m.b134 - m.b135 + m.x863 >= 0)

m.c2234 = Constraint(expr=   m.b136 - m.b137 + m.x860 >= 0)

m.c2235 = Constraint(expr=   m.b137 - m.b138 + m.x861 >= 0)

m.c2236 = Constraint(expr=   m.b139 - m.b140 + m.x862 >= 0)

m.c2237 = Constraint(expr=   m.b140 - m.b141 + m.x863 >= 0)

m.c2238 = Constraint(expr=   m.b142 - m.b143 + m.x860 >= 0)

m.c2239 = Constraint(expr=   m.b143 - m.b144 + m.x861 >= 0)

m.c2240 = Constraint(expr=   m.b145 - m.b146 + m.x862 >= 0)

m.c2241 = Constraint(expr=   m.b146 - m.b147 + m.x863 >= 0)

m.c2242 = Constraint(expr=   m.b148 - m.b149 + m.x864 >= 0)

m.c2243 = Constraint(expr=   m.b149 - m.b150 + m.x865 >= 0)

m.c2244 = Constraint(expr=   m.b151 - m.b152 + m.x864 >= 0)

m.c2245 = Constraint(expr=   m.b152 - m.b153 + m.x865 >= 0)

m.c2246 = Constraint(expr=   m.b154 - m.b155 + m.x864 >= 0)

m.c2247 = Constraint(expr=   m.b155 - m.b156 + m.x865 >= 0)

m.c2248 = Constraint(expr=   0.25*m.x740 + 0.25*m.x741 + 0.25*m.x742 + 0.25*m.x743 + 0.25*m.x744 + 0.25*m.x745
                           + 0.25*m.x746 + 0.25*m.x747 + 0.25*m.x748 + 0.25*m.x749 + 0.25*m.x750 + 0.25*m.x751
                           + 0.25*m.x752 + 0.25*m.x753 + 0.25*m.x754 + 0.25*m.x755 + 0.25*m.x756 + 0.25*m.x757
                           + 0.25*m.x758 + 0.25*m.x759 + 0.25*m.x760 + 0.25*m.x761 + 0.25*m.x762 + 0.25*m.x763 + m.x962
                           >= 760)

m.c2249 = Constraint(expr= - 3.125*m.x453 + m.x963 >= -75)

m.c2250 = Constraint(expr= - 3.125*m.x457 + m.x964 >= -400)

m.c2252 = Constraint(expr=-m.x866*m.x158 + m.x194 == 0)

m.c2253 = Constraint(expr=-m.x867*m.x159 + m.x195 == 0)

m.c2254 = Constraint(expr=-m.x869*m.x158 + m.x197 == 0)

m.c2255 = Constraint(expr=-m.x870*m.x159 + m.x198 == 0)

m.c2256 = Constraint(expr=-m.x872*m.x158 + m.x200 == 0)

m.c2257 = Constraint(expr=-m.x873*m.x159 + m.x201 == 0)

m.c2258 = Constraint(expr=-m.x875*m.x158 + m.x203 == 0)

m.c2259 = Constraint(expr=-m.x876*m.x159 + m.x204 == 0)

m.c2260 = Constraint(expr=-m.x878*m.x161 + m.x206 == 0)

m.c2261 = Constraint(expr=-m.x879*m.x162 + m.x207 == 0)

m.c2262 = Constraint(expr=-m.x881*m.x161 + m.x209 == 0)

m.c2263 = Constraint(expr=-m.x882*m.x162 + m.x210 == 0)

m.c2264 = Constraint(expr=-m.x884*m.x161 + m.x212 == 0)

m.c2265 = Constraint(expr=-m.x885*m.x162 + m.x213 == 0)

m.c2266 = Constraint(expr=-m.x887*m.x161 + m.x215 == 0)

m.c2267 = Constraint(expr=-m.x888*m.x162 + m.x216 == 0)

m.c2268 = Constraint(expr=-m.x878*m.x164 + m.x218 == 0)

m.c2269 = Constraint(expr=-m.x879*m.x165 + m.x219 == 0)

m.c2270 = Constraint(expr=-m.x881*m.x164 + m.x221 == 0)

m.c2271 = Constraint(expr=-m.x882*m.x165 + m.x222 == 0)

m.c2272 = Constraint(expr=-m.x884*m.x164 + m.x224 == 0)

m.c2273 = Constraint(expr=-m.x885*m.x165 + m.x225 == 0)

m.c2274 = Constraint(expr=-m.x887*m.x164 + m.x227 == 0)

m.c2275 = Constraint(expr=-m.x888*m.x165 + m.x228 == 0)

m.c2276 = Constraint(expr=-m.x890*m.x167 + m.x230 == 0)

m.c2277 = Constraint(expr=-m.x891*m.x168 + m.x231 == 0)

m.c2278 = Constraint(expr=-m.x893*m.x167 + m.x233 == 0)

m.c2279 = Constraint(expr=-m.x894*m.x168 + m.x234 == 0)

m.c2280 = Constraint(expr=-m.x896*m.x167 + m.x236 == 0)

m.c2281 = Constraint(expr=-m.x897*m.x168 + m.x237 == 0)

m.c2282 = Constraint(expr=-m.x899*m.x167 + m.x239 == 0)

m.c2283 = Constraint(expr=-m.x900*m.x168 + m.x240 == 0)

m.c2284 = Constraint(expr=-m.x890*m.x170 + m.x242 == 0)

m.c2285 = Constraint(expr=-m.x891*m.x171 + m.x243 == 0)

m.c2286 = Constraint(expr=-m.x893*m.x170 + m.x245 == 0)

m.c2287 = Constraint(expr=-m.x894*m.x171 + m.x246 == 0)

m.c2288 = Constraint(expr=-m.x896*m.x170 + m.x248 == 0)

m.c2289 = Constraint(expr=-m.x897*m.x171 + m.x249 == 0)

m.c2290 = Constraint(expr=-m.x899*m.x170 + m.x251 == 0)

m.c2291 = Constraint(expr=-m.x900*m.x171 + m.x252 == 0)

m.c2292 = Constraint(expr=-m.x902*m.x173 + m.x254 == 0)

m.c2293 = Constraint(expr=-m.x903*m.x174 + m.x255 == 0)

m.c2294 = Constraint(expr=-m.x905*m.x173 + m.x257 == 0)

m.c2295 = Constraint(expr=-m.x906*m.x174 + m.x258 == 0)

m.c2296 = Constraint(expr=-m.x908*m.x173 + m.x260 == 0)

m.c2297 = Constraint(expr=-m.x909*m.x174 + m.x261 == 0)

m.c2298 = Constraint(expr=-m.x911*m.x173 + m.x263 == 0)

m.c2299 = Constraint(expr=-m.x912*m.x174 + m.x264 == 0)

m.c2300 = Constraint(expr=-m.x902*m.x176 + m.x266 == 0)

m.c2301 = Constraint(expr=-m.x903*m.x177 + m.x267 == 0)

m.c2302 = Constraint(expr=-m.x905*m.x176 + m.x269 == 0)

m.c2303 = Constraint(expr=-m.x906*m.x177 + m.x270 == 0)

m.c2304 = Constraint(expr=-m.x908*m.x176 + m.x272 == 0)

m.c2305 = Constraint(expr=-m.x909*m.x177 + m.x273 == 0)

m.c2306 = Constraint(expr=-m.x911*m.x176 + m.x275 == 0)

m.c2307 = Constraint(expr=-m.x912*m.x177 + m.x276 == 0)

m.c2308 = Constraint(expr=-m.x914*m.x179 + m.x278 == 0)

m.c2309 = Constraint(expr=-m.x915*m.x180 + m.x279 == 0)

m.c2310 = Constraint(expr=-m.x917*m.x179 + m.x281 == 0)

m.c2311 = Constraint(expr=-m.x918*m.x180 + m.x282 == 0)

m.c2312 = Constraint(expr=-m.x920*m.x179 + m.x284 == 0)

m.c2313 = Constraint(expr=-m.x921*m.x180 + m.x285 == 0)

m.c2314 = Constraint(expr=-m.x923*m.x179 + m.x287 == 0)

m.c2315 = Constraint(expr=-m.x924*m.x180 + m.x288 == 0)

m.c2316 = Constraint(expr=-m.x914*m.x182 + m.x290 == 0)

m.c2317 = Constraint(expr=-m.x915*m.x183 + m.x291 == 0)

m.c2318 = Constraint(expr=-m.x917*m.x182 + m.x293 == 0)

m.c2319 = Constraint(expr=-m.x918*m.x183 + m.x294 == 0)

m.c2320 = Constraint(expr=-m.x920*m.x182 + m.x296 == 0)

m.c2321 = Constraint(expr=-m.x921*m.x183 + m.x297 == 0)

m.c2322 = Constraint(expr=-m.x923*m.x182 + m.x299 == 0)

m.c2323 = Constraint(expr=-m.x924*m.x183 + m.x300 == 0)

m.c2324 = Constraint(expr=-m.x926*m.x185 + m.x302 == 0)

m.c2325 = Constraint(expr=-m.x927*m.x186 + m.x303 == 0)

m.c2326 = Constraint(expr=-m.x929*m.x185 + m.x305 == 0)

m.c2327 = Constraint(expr=-m.x930*m.x186 + m.x306 == 0)

m.c2328 = Constraint(expr=-m.x932*m.x185 + m.x308 == 0)

m.c2329 = Constraint(expr=-m.x933*m.x186 + m.x309 == 0)

m.c2330 = Constraint(expr=-m.x935*m.x185 + m.x311 == 0)

m.c2331 = Constraint(expr=-m.x936*m.x186 + m.x312 == 0)

m.c2332 = Constraint(expr=-m.x938*m.x188 + m.x314 == 0)

m.c2333 = Constraint(expr=-m.x939*m.x189 + m.x315 == 0)

m.c2334 = Constraint(expr=-m.x941*m.x188 + m.x317 == 0)

m.c2335 = Constraint(expr=-m.x942*m.x189 + m.x318 == 0)

m.c2336 = Constraint(expr=-m.x944*m.x188 + m.x320 == 0)

m.c2337 = Constraint(expr=-m.x945*m.x189 + m.x321 == 0)

m.c2338 = Constraint(expr=-m.x947*m.x188 + m.x323 == 0)

m.c2339 = Constraint(expr=-m.x948*m.x189 + m.x324 == 0)

m.c2340 = Constraint(expr=-m.x950*m.x191 + m.x326 == 0)

m.c2341 = Constraint(expr=-m.x951*m.x192 + m.x327 == 0)

m.c2342 = Constraint(expr=-m.x953*m.x191 + m.x329 == 0)

m.c2343 = Constraint(expr=-m.x954*m.x192 + m.x330 == 0)

m.c2344 = Constraint(expr=-m.x956*m.x191 + m.x332 == 0)

m.c2345 = Constraint(expr=-m.x957*m.x192 + m.x333 == 0)

m.c2346 = Constraint(expr=-m.x959*m.x191 + m.x335 == 0)

m.c2347 = Constraint(expr=-m.x960*m.x192 + m.x336 == 0)

m.c2348 = Constraint(expr=-m.x866*m.x740 + m.x764 == 0)

m.c2349 = Constraint(expr=-m.x867*m.x741 + m.x765 == 0)

m.c2350 = Constraint(expr=-m.x868*m.x742 + m.x766 == 0)

m.c2351 = Constraint(expr=-m.x869*m.x740 + m.x767 == 0)

m.c2352 = Constraint(expr=-m.x870*m.x741 + m.x768 == 0)

m.c2353 = Constraint(expr=-m.x871*m.x742 + m.x769 == 0)

m.c2354 = Constraint(expr=-m.x872*m.x740 + m.x770 == 0)

m.c2355 = Constraint(expr=-m.x873*m.x741 + m.x771 == 0)

m.c2356 = Constraint(expr=-m.x874*m.x742 + m.x772 == 0)

m.c2357 = Constraint(expr=-m.x875*m.x740 + m.x773 == 0)

m.c2358 = Constraint(expr=-m.x876*m.x741 + m.x774 == 0)

m.c2359 = Constraint(expr=-m.x877*m.x742 + m.x775 == 0)

m.c2360 = Constraint(expr=-m.x878*m.x743 + m.x776 == 0)

m.c2361 = Constraint(expr=-m.x879*m.x744 + m.x777 == 0)

m.c2362 = Constraint(expr=-m.x880*m.x745 + m.x778 == 0)

m.c2363 = Constraint(expr=-m.x881*m.x743 + m.x779 == 0)

m.c2364 = Constraint(expr=-m.x882*m.x744 + m.x780 == 0)

m.c2365 = Constraint(expr=-m.x883*m.x745 + m.x781 == 0)

m.c2366 = Constraint(expr=-m.x884*m.x743 + m.x782 == 0)

m.c2367 = Constraint(expr=-m.x885*m.x744 + m.x783 == 0)

m.c2368 = Constraint(expr=-m.x886*m.x745 + m.x784 == 0)

m.c2369 = Constraint(expr=-m.x887*m.x743 + m.x785 == 0)

m.c2370 = Constraint(expr=-m.x888*m.x744 + m.x786 == 0)

m.c2371 = Constraint(expr=-m.x889*m.x745 + m.x787 == 0)

m.c2372 = Constraint(expr=-m.x890*m.x746 + m.x788 == 0)

m.c2373 = Constraint(expr=-m.x891*m.x747 + m.x789 == 0)

m.c2374 = Constraint(expr=-m.x892*m.x748 + m.x790 == 0)

m.c2375 = Constraint(expr=-m.x893*m.x746 + m.x791 == 0)

m.c2376 = Constraint(expr=-m.x894*m.x747 + m.x792 == 0)

m.c2377 = Constraint(expr=-m.x895*m.x748 + m.x793 == 0)

m.c2378 = Constraint(expr=-m.x896*m.x746 + m.x794 == 0)

m.c2379 = Constraint(expr=-m.x897*m.x747 + m.x795 == 0)

m.c2380 = Constraint(expr=-m.x898*m.x748 + m.x796 == 0)

m.c2381 = Constraint(expr=-m.x899*m.x746 + m.x797 == 0)

m.c2382 = Constraint(expr=-m.x900*m.x747 + m.x798 == 0)

m.c2383 = Constraint(expr=-m.x901*m.x748 + m.x799 == 0)

m.c2384 = Constraint(expr=-m.x902*m.x749 + m.x800 == 0)

m.c2385 = Constraint(expr=-m.x903*m.x750 + m.x801 == 0)

m.c2386 = Constraint(expr=-m.x904*m.x751 + m.x802 == 0)

m.c2387 = Constraint(expr=-m.x905*m.x749 + m.x803 == 0)

m.c2388 = Constraint(expr=-m.x906*m.x750 + m.x804 == 0)

m.c2389 = Constraint(expr=-m.x907*m.x751 + m.x805 == 0)

m.c2390 = Constraint(expr=-m.x908*m.x749 + m.x806 == 0)

m.c2391 = Constraint(expr=-m.x909*m.x750 + m.x807 == 0)

m.c2392 = Constraint(expr=-m.x910*m.x751 + m.x808 == 0)

m.c2393 = Constraint(expr=-m.x911*m.x749 + m.x809 == 0)

m.c2394 = Constraint(expr=-m.x912*m.x750 + m.x810 == 0)

m.c2395 = Constraint(expr=-m.x913*m.x751 + m.x811 == 0)

m.c2396 = Constraint(expr=-m.x914*m.x752 + m.x812 == 0)

m.c2397 = Constraint(expr=-m.x915*m.x753 + m.x813 == 0)

m.c2398 = Constraint(expr=-m.x916*m.x754 + m.x814 == 0)

m.c2399 = Constraint(expr=-m.x917*m.x752 + m.x815 == 0)

m.c2400 = Constraint(expr=-m.x918*m.x753 + m.x816 == 0)

m.c2401 = Constraint(expr=-m.x919*m.x754 + m.x817 == 0)

m.c2402 = Constraint(expr=-m.x920*m.x752 + m.x818 == 0)

m.c2403 = Constraint(expr=-m.x921*m.x753 + m.x819 == 0)

m.c2404 = Constraint(expr=-m.x922*m.x754 + m.x820 == 0)

m.c2405 = Constraint(expr=-m.x923*m.x752 + m.x821 == 0)

m.c2406 = Constraint(expr=-m.x924*m.x753 + m.x822 == 0)

m.c2407 = Constraint(expr=-m.x925*m.x754 + m.x823 == 0)

m.c2408 = Constraint(expr=-m.x926*m.x755 + m.x824 == 0)

m.c2409 = Constraint(expr=-m.x927*m.x756 + m.x825 == 0)

m.c2410 = Constraint(expr=-m.x928*m.x757 + m.x826 == 0)

m.c2411 = Constraint(expr=-m.x929*m.x755 + m.x827 == 0)

m.c2412 = Constraint(expr=-m.x930*m.x756 + m.x828 == 0)

m.c2413 = Constraint(expr=-m.x931*m.x757 + m.x829 == 0)

m.c2414 = Constraint(expr=-m.x932*m.x755 + m.x830 == 0)

m.c2415 = Constraint(expr=-m.x933*m.x756 + m.x831 == 0)

m.c2416 = Constraint(expr=-m.x934*m.x757 + m.x832 == 0)

m.c2417 = Constraint(expr=-m.x935*m.x755 + m.x833 == 0)

m.c2418 = Constraint(expr=-m.x936*m.x756 + m.x834 == 0)

m.c2419 = Constraint(expr=-m.x937*m.x757 + m.x835 == 0)

m.c2420 = Constraint(expr=-m.x938*m.x758 + m.x836 == 0)

m.c2421 = Constraint(expr=-m.x939*m.x759 + m.x837 == 0)

m.c2422 = Constraint(expr=-m.x940*m.x760 + m.x838 == 0)

m.c2423 = Constraint(expr=-m.x941*m.x758 + m.x839 == 0)

m.c2424 = Constraint(expr=-m.x942*m.x759 + m.x840 == 0)

m.c2425 = Constraint(expr=-m.x943*m.x760 + m.x841 == 0)

m.c2426 = Constraint(expr=-m.x944*m.x758 + m.x842 == 0)

m.c2427 = Constraint(expr=-m.x945*m.x759 + m.x843 == 0)

m.c2428 = Constraint(expr=-m.x946*m.x760 + m.x844 == 0)

m.c2429 = Constraint(expr=-m.x947*m.x758 + m.x845 == 0)

m.c2430 = Constraint(expr=-m.x948*m.x759 + m.x846 == 0)

m.c2431 = Constraint(expr=-m.x949*m.x760 + m.x847 == 0)

m.c2432 = Constraint(expr=-m.x950*m.x761 + m.x848 == 0)

m.c2433 = Constraint(expr=-m.x951*m.x762 + m.x849 == 0)

m.c2434 = Constraint(expr=-m.x952*m.x763 + m.x850 == 0)

m.c2435 = Constraint(expr=-m.x953*m.x761 + m.x851 == 0)

m.c2436 = Constraint(expr=-m.x954*m.x762 + m.x852 == 0)

m.c2437 = Constraint(expr=-m.x955*m.x763 + m.x853 == 0)

m.c2438 = Constraint(expr=-m.x956*m.x761 + m.x854 == 0)

m.c2439 = Constraint(expr=-m.x957*m.x762 + m.x855 == 0)

m.c2440 = Constraint(expr=-m.x958*m.x763 + m.x856 == 0)

m.c2441 = Constraint(expr=-m.x959*m.x761 + m.x857 == 0)

m.c2442 = Constraint(expr=-m.x960*m.x762 + m.x858 == 0)

m.c2443 = Constraint(expr=-m.x961*m.x763 + m.x859 == 0)
