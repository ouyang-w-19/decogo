#  MINLP written by GAMS Convert at 04/21/18 13:52:37
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        481      106      196      179        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        350      174      176        0        0        0        0        0
#  FX     49       49        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       4126     3908      218        0


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
m.x225 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x235 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x255 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x258 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x262 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x263 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x264 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x265 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x266 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x267 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x268 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x269 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x270 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x271 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x272 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x273 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x274 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x275 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x276 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x277 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x278 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x279 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x280 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x281 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x282 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x283 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x284 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x285 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x286 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x287 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x289 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x290 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x291 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x292 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x293 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x294 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x295 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x296 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x297 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x298 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x299 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x300 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x301 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x302 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x303 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x304 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x305 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x306 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x307 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x309 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x311 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x312 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x313 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x314 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x315 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x316 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x317 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x318 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x319 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x320 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x321 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x322 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x323 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x324 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x325 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x326 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x327 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x328 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x329 = Var(within=Reals,bounds=(150,None),initialize=150)
m.x330 = Var(within=Reals,bounds=(250,None),initialize=250)
m.x331 = Var(within=Reals,bounds=(500,None),initialize=500)
m.x332 = Var(within=Reals,bounds=(50,None),initialize=50)
m.x333 = Var(within=Reals,bounds=(0,None),initialize=1170)
m.x334 = Var(within=Reals,bounds=(0,None),initialize=1120)
m.x335 = Var(within=Reals,bounds=(0,None),initialize=1120)
m.x336 = Var(within=Reals,bounds=(0,None),initialize=1340)
m.x337 = Var(within=Reals,bounds=(0,None),initialize=1290)
m.x338 = Var(within=Reals,bounds=(0,None),initialize=1860)
m.x339 = Var(within=Reals,bounds=(0,None),initialize=1340)
m.x340 = Var(within=Reals,bounds=(0,None),initialize=1340)
m.x341 = Var(within=Reals,bounds=(0,None),initialize=1340)
m.x342 = Var(within=Reals,bounds=(0,None),initialize=1210)
m.x343 = Var(within=Reals,bounds=(0,None),initialize=1160)
m.x344 = Var(within=Reals,bounds=(0,None),initialize=1420)
m.x345 = Var(within=Reals,bounds=(26.7857142857143,600),initialize=26.7857142857143)
m.x346 = Var(within=Reals,bounds=(26.8817204301075,600),initialize=26.8817204301075)
m.x347 = Var(within=Reals,bounds=(74.6268656716418,600),initialize=74.6268656716418)
m.x348 = Var(within=Reals,bounds=(7.04225352112676,600),initialize=7.04225352112676)
m.x349 = Var(within=Reals,bounds=(200,600),initialize=200)
m.x350 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x350, sense=maximize)

m.c1 = Constraint(expr=m.x350*m.x349 + 0.00203*(m.x345**2*(m.x335 - m.x329) + (m.x349 - m.x345)**2*m.x329) + 0.00203*(
                       m.x346**2*(m.x338 - m.x330) + (m.x349 - m.x346)**2*m.x330) + 0.00203*(m.x347**2*(m.x341 - m.x331)
                        + (m.x349 - m.x347)**2*m.x331) + 0.00203*(m.x348**2*(m.x344 - m.x332) + (m.x349 - m.x348)**2*
                       m.x332) + 7600*m.b1 + 7600*m.b2 + 7600*m.b3 + 7600*m.b4 + 7600*m.b5 + 7600*m.b6 + 7600*m.b7
                        + 7600*m.b8 + 7600*m.b9 + 7600*m.b10 + 7600*m.b11 + 7600*m.b12 + 7500*m.b13 + 7500*m.b14
                        + 7500*m.b15 + 7500*m.b16 + 750*m.b17 + 750*m.b18 + 750*m.b19 + 750*m.b20 + 3000*m.b21
                        + 3000*m.b22 + 3000*m.b23 + 3000*m.b24 + 7700*m.b25 + 7700*m.b26 + 7700*m.b27 + 7700*m.b28
                        + 770*m.b29 + 770*m.b30 + 770*m.b31 + 770*m.b32 + 3080*m.b33 + 3080*m.b34 + 3080*m.b35
                        + 3080*m.b36 + 7600*m.b37 + 7600*m.b38 + 7600*m.b39 + 7600*m.b40 + 3040*m.b41 + 3040*m.b42
                        + 3040*m.b43 + 3040*m.b44 + 3040*m.b45 + 3040*m.b46 + 3040*m.b47 + 3040*m.b48 + 2280*m.b49
                        + 2280*m.b50 + 2280*m.b51 + 2280*m.b52 + 2280*m.b53 + 2280*m.b54 + 2280*m.b55 + 2280*m.b56
                        + 9120*m.b57 + 9120*m.b58 + 9120*m.b59 + 9120*m.b60 + 2250*m.b61 + 2250*m.b62 + 2250*m.b63
                        + 2250*m.b64 + 750*m.b65 + 750*m.b66 + 750*m.b67 + 750*m.b68 + 9000*m.b69 + 9000*m.b70
                        + 9000*m.b71 + 9000*m.b72 + 2310*m.b73 + 2310*m.b74 + 2310*m.b75 + 2310*m.b76 + 770*m.b77
                        + 770*m.b78 + 770*m.b79 + 770*m.b80 + 9240*m.b81 + 9240*m.b82 + 9240*m.b83 + 9240*m.b84
                        + 9120*m.b85 + 9120*m.b86 + 9120*m.b87 + 9120*m.b88 + 9120*m.b89 + 9120*m.b90 + 9120*m.b91
                        + 9120*m.b92 + 9120*m.b93 + 9120*m.b94 + 9120*m.b95 + 9120*m.b96 + 1520*m.b97 + 1520*m.b98
                        + 1520*m.b99 + 1520*m.b100 + 1520*m.b101 + 1520*m.b102 + 1520*m.b103 + 1520*m.b104 + 6080*m.b105
                        + 6080*m.b106 + 6080*m.b107 + 6080*m.b108 + 1500*m.b109 + 1500*m.b110 + 1500*m.b111
                        + 1500*m.b112 + 750*m.b113 + 750*m.b114 + 750*m.b115 + 750*m.b116 + 6000*m.b117 + 6000*m.b118
                        + 6000*m.b119 + 6000*m.b120 + 1540*m.b121 + 1540*m.b122 + 1540*m.b123 + 1540*m.b124 + 770*m.b125
                        + 770*m.b126 + 770*m.b127 + 770*m.b128 + 6160*m.b129 + 6160*m.b130 + 6160*m.b131 + 6160*m.b132
                        + 6080*m.b133 + 6080*m.b134 + 6080*m.b135 + 6080*m.b136 + 6080*m.b137 + 6080*m.b138
                        + 6080*m.b139 + 6080*m.b140 + 6080*m.b141 + 6080*m.b142 + 6080*m.b143 + 6080*m.b144 - 4*m.x185
                        - 4*m.x186 - 4*m.x187 - 4*m.x188 - 1.5*m.x197 - 1.5*m.x198 - 1.5*m.x199 - 1.5*m.x200
                        - 6.5*m.x209 - 6.5*m.x210 - 6.5*m.x211 - 6.5*m.x212 - 3*m.x221 - 3*m.x222 - 3*m.x223 - 3*m.x224
                        + 0.1218*m.x297 + 0.1218*m.x298 + 0.1218*m.x299 + 0.1218*m.x300 + 0.1218*m.x301 + 0.1218*m.x302
                        + 0.1218*m.x303 + 0.1218*m.x304 == 0)

m.c2 = Constraint(expr=   m.b1 + m.b5 + m.b9 - m.b16 - m.b28 - m.b40 + m.x225 - m.x228 == 0)

m.c3 = Constraint(expr=   m.b2 + m.b6 + m.b10 - m.b13 - m.b25 - m.b37 - m.x225 + m.x226 == 0)

m.c4 = Constraint(expr=   m.b3 + m.b7 + m.b11 - m.b14 - m.b26 - m.b38 - m.x226 + m.x227 == 0)

m.c5 = Constraint(expr=   m.b4 + m.b8 + m.b12 - m.b15 - m.b27 - m.b39 - m.x227 + m.x228 == 0)

m.c6 = Constraint(expr= - m.b4 + m.b13 + m.b17 + m.b21 - m.b32 - m.b44 + m.x229 - m.x232 == 0)

m.c7 = Constraint(expr= - m.b1 + m.b14 + m.b18 + m.b22 - m.b29 - m.b41 - m.x229 + m.x230 == 0)

m.c8 = Constraint(expr= - m.b2 + m.b15 + m.b19 + m.b23 - m.b30 - m.b42 - m.x230 + m.x231 == 0)

m.c9 = Constraint(expr= - m.b3 + m.b16 + m.b20 + m.b24 - m.b31 - m.b43 - m.x231 + m.x232 == 0)

m.c10 = Constraint(expr= - m.b8 - m.b20 + m.b25 + m.b29 + m.b33 - m.b48 + m.x233 - m.x236 == 0)

m.c11 = Constraint(expr= - m.b5 - m.b17 + m.b26 + m.b30 + m.b34 - m.b45 - m.x233 + m.x234 == 0)

m.c12 = Constraint(expr= - m.b6 - m.b18 + m.b27 + m.b31 + m.b35 - m.b46 - m.x234 + m.x235 == 0)

m.c13 = Constraint(expr= - m.b7 - m.b19 + m.b28 + m.b32 + m.b36 - m.b47 - m.x235 + m.x236 == 0)

m.c14 = Constraint(expr= - m.b12 - m.b24 - m.b36 + m.b37 + m.b41 + m.b45 + m.x237 - m.x240 == 0)

m.c15 = Constraint(expr= - m.b9 - m.b21 - m.b33 + m.b38 + m.b42 + m.b46 - m.x237 + m.x238 == 0)

m.c16 = Constraint(expr= - m.b10 - m.b22 - m.b34 + m.b39 + m.b43 + m.b47 - m.x238 + m.x239 == 0)

m.c17 = Constraint(expr= - m.b11 - m.b23 - m.b35 + m.b40 + m.b44 + m.b48 - m.x239 + m.x240 == 0)

m.c18 = Constraint(expr=   m.b49 + m.b53 + m.b57 - m.b64 - m.b76 - m.b88 + m.x241 - m.x244 == 0)

m.c19 = Constraint(expr=   m.b50 + m.b54 + m.b58 - m.b61 - m.b73 - m.b85 - m.x241 + m.x242 == 0)

m.c20 = Constraint(expr=   m.b51 + m.b55 + m.b59 - m.b62 - m.b74 - m.b86 - m.x242 + m.x243 == 0)

m.c21 = Constraint(expr=   m.b52 + m.b56 + m.b60 - m.b63 - m.b75 - m.b87 - m.x243 + m.x244 == 0)

m.c22 = Constraint(expr= - m.b52 + m.b61 + m.b65 + m.b69 - m.b80 - m.b92 + m.x245 - m.x248 == 0)

m.c23 = Constraint(expr= - m.b49 + m.b62 + m.b66 + m.b70 - m.b77 - m.b89 - m.x245 + m.x246 == 0)

m.c24 = Constraint(expr= - m.b50 + m.b63 + m.b67 + m.b71 - m.b78 - m.b90 - m.x246 + m.x247 == 0)

m.c25 = Constraint(expr= - m.b51 + m.b64 + m.b68 + m.b72 - m.b79 - m.b91 - m.x247 + m.x248 == 0)

m.c26 = Constraint(expr= - m.b56 - m.b68 + m.b73 + m.b77 + m.b81 - m.b96 + m.x249 - m.x252 == 0)

m.c27 = Constraint(expr= - m.b53 - m.b65 + m.b74 + m.b78 + m.b82 - m.b93 - m.x249 + m.x250 == 0)

m.c28 = Constraint(expr= - m.b54 - m.b66 + m.b75 + m.b79 + m.b83 - m.b94 - m.x250 + m.x251 == 0)

m.c29 = Constraint(expr= - m.b55 - m.b67 + m.b76 + m.b80 + m.b84 - m.b95 - m.x251 + m.x252 == 0)

m.c30 = Constraint(expr= - m.b60 - m.b72 - m.b84 + m.b85 + m.b89 + m.b93 + m.x253 - m.x256 == 0)

m.c31 = Constraint(expr= - m.b57 - m.b69 - m.b81 + m.b86 + m.b90 + m.b94 - m.x253 + m.x254 == 0)

m.c32 = Constraint(expr= - m.b58 - m.b70 - m.b82 + m.b87 + m.b91 + m.b95 - m.x254 + m.x255 == 0)

m.c33 = Constraint(expr= - m.b59 - m.b71 - m.b83 + m.b88 + m.b92 + m.b96 - m.x255 + m.x256 == 0)

m.c34 = Constraint(expr=   m.b97 + m.b101 + m.b105 - m.b112 - m.b124 - m.b136 + m.x257 - m.x260 == 0)

m.c35 = Constraint(expr=   m.b98 + m.b102 + m.b106 - m.b109 - m.b121 - m.b133 - m.x257 + m.x258 == 0)

m.c36 = Constraint(expr=   m.b99 + m.b103 + m.b107 - m.b110 - m.b122 - m.b134 - m.x258 + m.x259 == 0)

m.c37 = Constraint(expr=   m.b100 + m.b104 + m.b108 - m.b111 - m.b123 - m.b135 - m.x259 + m.x260 == 0)

m.c38 = Constraint(expr= - m.b100 + m.b109 + m.b113 + m.b117 - m.b128 - m.b140 + m.x261 - m.x264 == 0)

m.c39 = Constraint(expr= - m.b97 + m.b110 + m.b114 + m.b118 - m.b125 - m.b137 - m.x261 + m.x262 == 0)

m.c40 = Constraint(expr= - m.b98 + m.b111 + m.b115 + m.b119 - m.b126 - m.b138 - m.x262 + m.x263 == 0)

m.c41 = Constraint(expr= - m.b99 + m.b112 + m.b116 + m.b120 - m.b127 - m.b139 - m.x263 + m.x264 == 0)

m.c42 = Constraint(expr= - m.b104 - m.b116 + m.b121 + m.b125 + m.b129 - m.b144 + m.x265 - m.x268 == 0)

m.c43 = Constraint(expr= - m.b101 - m.b113 + m.b122 + m.b126 + m.b130 - m.b141 - m.x265 + m.x266 == 0)

m.c44 = Constraint(expr= - m.b102 - m.b114 + m.b123 + m.b127 + m.b131 - m.b142 - m.x266 + m.x267 == 0)

m.c45 = Constraint(expr= - m.b103 - m.b115 + m.b124 + m.b128 + m.b132 - m.b143 - m.x267 + m.x268 == 0)

m.c46 = Constraint(expr= - m.b108 - m.b120 - m.b132 + m.b133 + m.b137 + m.b141 + m.x269 - m.x272 == 0)

m.c47 = Constraint(expr= - m.b105 - m.b117 - m.b129 + m.b134 + m.b138 + m.b142 - m.x269 + m.x270 == 0)

m.c48 = Constraint(expr= - m.b106 - m.b118 - m.b130 + m.b135 + m.b139 + m.b143 - m.x270 + m.x271 == 0)

m.c49 = Constraint(expr= - m.b107 - m.b119 - m.b131 + m.b136 + m.b140 + m.b144 - m.x271 + m.x272 == 0)

m.c50 = Constraint(expr=   m.b1 + m.b5 + m.b9 + m.b13 + m.b17 + m.b21 + m.b25 + m.b29 + m.b33 + m.b37 + m.b41 + m.b45
                         + m.x225 + m.x229 + m.x233 + m.x237 == 1)

m.c51 = Constraint(expr=   m.b49 + m.b53 + m.b57 + m.b61 + m.b65 + m.b69 + m.b73 + m.b77 + m.b81 + m.b85 + m.b89 + m.b93
                         + m.x241 + m.x245 + m.x249 + m.x253 == 1)

m.c52 = Constraint(expr=   m.b97 + m.b101 + m.b105 + m.b109 + m.b113 + m.b117 + m.b121 + m.b125 + m.b129 + m.b133
                         + m.b137 + m.b141 + m.x257 + m.x261 + m.x265 + m.x269 == 1)

m.c53 = Constraint(expr= - 10*m.b1 - 10*m.b5 - 10*m.b9 - 10*m.b13 - m.b17 - 4*m.b21 - 10*m.b25 - m.b29 - 4*m.b33
                         - 10*m.b37 - 4*m.b41 - 4*m.b45 - 0.000854700854700855*m.x177 - 0.000746268656716418*m.x189
                         - 0.000746268656716418*m.x201 - 0.000826446280991736*m.x213 - m.x273 + m.x276 >= 0)

m.c54 = Constraint(expr= - 10*m.b2 - 10*m.b6 - 10*m.b10 - 10*m.b14 - m.b18 - 4*m.b22 - 10*m.b26 - m.b30 - 4*m.b34
                         - 10*m.b38 - 4*m.b42 - 4*m.b46 - 0.000854700854700855*m.x178 - 0.000746268656716418*m.x190
                         - 0.000746268656716418*m.x202 - 0.000826446280991736*m.x214 - m.x276 + m.x279 >= 0)

m.c55 = Constraint(expr= - 10*m.b3 - 10*m.b7 - 10*m.b11 - 10*m.b15 - m.b19 - 4*m.b23 - 10*m.b27 - m.b31 - 4*m.b35
                         - 10*m.b39 - 4*m.b43 - 4*m.b47 - 0.000854700854700855*m.x179 - 0.000746268656716418*m.x191
                         - 0.000746268656716418*m.x203 - 0.000826446280991736*m.x215 - m.x279 + m.x282 >= 0)

m.c56 = Constraint(expr= - 10*m.b4 - 10*m.b8 - 10*m.b12 - 10*m.b16 - m.b20 - 4*m.b24 - 10*m.b28 - m.b32 - 4*m.b36
                         - 10*m.b40 - 4*m.b44 - 4*m.b48 - 0.000854700854700855*m.x180 - 0.000746268656716418*m.x192
                         - 0.000746268656716418*m.x204 - 0.000826446280991736*m.x216 + m.x273 - m.x282 + m.x349 >= 0)

m.c57 = Constraint(expr= - 3*m.b49 - 3*m.b53 - 12*m.b57 - 3*m.b61 - m.b65 - 12*m.b69 - 3*m.b73 - m.b77 - 12*m.b81
                         - 12*m.b85 - 12*m.b89 - 12*m.b93 - 0.000892857142857143*m.x181 - 0.000775193798449612*m.x193
                         - 0.000746268656716418*m.x205 - 0.000862068965517241*m.x217 - m.x274 + m.x277 >= 0)

m.c58 = Constraint(expr= - 3*m.b50 - 3*m.b54 - 12*m.b58 - 3*m.b62 - m.b66 - 12*m.b70 - 3*m.b74 - m.b78 - 12*m.b82
                         - 12*m.b86 - 12*m.b90 - 12*m.b94 - 0.000892857142857143*m.x182 - 0.000775193798449612*m.x194
                         - 0.000746268656716418*m.x206 - 0.000862068965517241*m.x218 - m.x277 + m.x280 >= 0)

m.c59 = Constraint(expr= - 3*m.b51 - 3*m.b55 - 12*m.b59 - 3*m.b63 - m.b67 - 12*m.b71 - 3*m.b75 - m.b79 - 12*m.b83
                         - 12*m.b87 - 12*m.b91 - 12*m.b95 - 0.000892857142857143*m.x183 - 0.000775193798449612*m.x195
                         - 0.000746268656716418*m.x207 - 0.000862068965517241*m.x219 - m.x280 + m.x283 >= 0)

m.c60 = Constraint(expr= - 3*m.b52 - 3*m.b56 - 12*m.b60 - 3*m.b64 - m.b68 - 12*m.b72 - 3*m.b76 - m.b80 - 12*m.b84
                         - 12*m.b88 - 12*m.b92 - 12*m.b96 - 0.000892857142857143*m.x184 - 0.000775193798449612*m.x196
                         - 0.000746268656716418*m.x208 - 0.000862068965517241*m.x220 + m.x274 - m.x283 + m.x349 >= 0)

m.c61 = Constraint(expr= - 2*m.b97 - 2*m.b101 - 8*m.b105 - 2*m.b109 - m.b113 - 8*m.b117 - 2*m.b121 - m.b125 - 8*m.b129
                         - 8*m.b133 - 8*m.b137 - 8*m.b141 - 0.000892857142857143*m.x185 - 0.000537634408602151*m.x197
                         - 0.000746268656716418*m.x209 - 0.000704225352112676*m.x221 - m.x275 + m.x278 >= 0)

m.c62 = Constraint(expr= - 2*m.b98 - 2*m.b102 - 8*m.b106 - 2*m.b110 - m.b114 - 8*m.b118 - 2*m.b122 - m.b126 - 8*m.b130
                         - 8*m.b134 - 8*m.b138 - 8*m.b142 - 0.000892857142857143*m.x186 - 0.000537634408602151*m.x198
                         - 0.000746268656716418*m.x210 - 0.000704225352112676*m.x222 - m.x278 + m.x281 >= 0)

m.c63 = Constraint(expr= - 2*m.b99 - 2*m.b103 - 8*m.b107 - 2*m.b111 - m.b115 - 8*m.b119 - 2*m.b123 - m.b127 - 8*m.b131
                         - 8*m.b135 - 8*m.b139 - 8*m.b143 - 0.000892857142857143*m.x187 - 0.000537634408602151*m.x199
                         - 0.000746268656716418*m.x211 - 0.000704225352112676*m.x223 - m.x281 + m.x284 >= 0)

m.c64 = Constraint(expr= - 2*m.b100 - 2*m.b104 - 8*m.b108 - 2*m.b112 - m.b116 - 8*m.b120 - 2*m.b124 - m.b128 - 8*m.b132
                         - 8*m.b136 - 8*m.b140 - 8*m.b144 - 0.000892857142857143*m.x188 - 0.000537634408602151*m.x200
                         - 0.000746268656716418*m.x212 - 0.000704225352112676*m.x224 + m.x275 - m.x284 + m.x349 >= 0)

m.c65 = Constraint(expr= - 10*m.b1 - 10*m.b5 - 10*m.b9 - 10*m.b13 - m.b17 - 4*m.b21 - 10*m.b25 - m.b29 - 4*m.b33
                         - 10*m.b37 - 4*m.b41 - 4*m.b45 + m.x276 - m.x285 == 0)

m.c66 = Constraint(expr= - 10*m.b2 - 10*m.b6 - 10*m.b10 - 10*m.b14 - m.b18 - 4*m.b22 - 10*m.b26 - m.b30 - 4*m.b34
                         - 10*m.b38 - 4*m.b42 - 4*m.b46 + m.x279 - m.x288 == 0)

m.c67 = Constraint(expr= - 10*m.b3 - 10*m.b7 - 10*m.b11 - 10*m.b15 - m.b19 - 4*m.b23 - 10*m.b27 - m.b31 - 4*m.b35
                         - 10*m.b39 - 4*m.b43 - 4*m.b47 + m.x282 - m.x291 == 0)

m.c68 = Constraint(expr= - 10*m.b4 - 10*m.b8 - 10*m.b12 - 10*m.b16 - m.b20 - 4*m.b24 - 10*m.b28 - m.b32 - 4*m.b36
                         - 10*m.b40 - 4*m.b44 - 4*m.b48 + m.x273 - m.x294 + m.x349 == 0)

m.c69 = Constraint(expr= - 3*m.b49 - 3*m.b53 - 12*m.b57 - 3*m.b61 - m.b65 - 12*m.b69 - 3*m.b73 - m.b77 - 12*m.b81
                         - 12*m.b85 - 12*m.b89 - 12*m.b93 + m.x277 - m.x286 == 0)

m.c70 = Constraint(expr= - 3*m.b50 - 3*m.b54 - 12*m.b58 - 3*m.b62 - m.b66 - 12*m.b70 - 3*m.b74 - m.b78 - 12*m.b82
                         - 12*m.b86 - 12*m.b90 - 12*m.b94 + m.x280 - m.x289 == 0)

m.c71 = Constraint(expr= - 3*m.b51 - 3*m.b55 - 12*m.b59 - 3*m.b63 - m.b67 - 12*m.b71 - 3*m.b75 - m.b79 - 12*m.b83
                         - 12*m.b87 - 12*m.b91 - 12*m.b95 + m.x283 - m.x292 == 0)

m.c72 = Constraint(expr= - 3*m.b52 - 3*m.b56 - 12*m.b60 - 3*m.b64 - m.b68 - 12*m.b72 - 3*m.b76 - m.b80 - 12*m.b84
                         - 12*m.b88 - 12*m.b92 - 12*m.b96 + m.x274 - m.x295 + m.x349 == 0)

m.c73 = Constraint(expr= - 2*m.b97 - 2*m.b101 - 8*m.b105 - 2*m.b109 - m.b113 - 8*m.b117 - 2*m.b121 - m.b125 - 8*m.b129
                         - 8*m.b133 - 8*m.b137 - 8*m.b141 + m.x278 - m.x287 == 0)

m.c74 = Constraint(expr= - 2*m.b98 - 2*m.b102 - 8*m.b106 - 2*m.b110 - m.b114 - 8*m.b118 - 2*m.b122 - m.b126 - 8*m.b130
                         - 8*m.b134 - 8*m.b138 - 8*m.b142 + m.x281 - m.x290 == 0)

m.c75 = Constraint(expr= - 2*m.b99 - 2*m.b103 - 8*m.b107 - 2*m.b111 - m.b115 - 8*m.b119 - 2*m.b123 - m.b127 - 8*m.b131
                         - 8*m.b135 - 8*m.b139 - 8*m.b143 + m.x284 - m.x293 == 0)

m.c76 = Constraint(expr= - 2*m.b100 - 2*m.b104 - 8*m.b108 - 2*m.b112 - m.b116 - 8*m.b120 - 2*m.b124 - m.b128 - 8*m.b132
                         - 8*m.b136 - 8*m.b140 - 8*m.b144 + m.x275 - m.x296 + m.x349 == 0)

m.c77 = Constraint(expr=   m.x282 - m.x349 <= 0)

m.c78 = Constraint(expr=   m.x283 - m.x349 <= 0)

m.c79 = Constraint(expr=   m.x284 - m.x349 <= 0)

m.c80 = Constraint(expr= - 702000*m.b1 - 702000*m.b5 - 702000*m.b9 + m.x177 <= 0)

m.c81 = Constraint(expr= - 702000*m.b2 - 702000*m.b6 - 702000*m.b10 + m.x178 <= 0)

m.c82 = Constraint(expr= - 702000*m.b3 - 702000*m.b7 - 702000*m.b11 + m.x179 <= 0)

m.c83 = Constraint(expr= - 702000*m.b4 - 702000*m.b8 - 702000*m.b12 + m.x180 <= 0)

m.c84 = Constraint(expr= - 672000*m.b49 - 672000*m.b53 - 672000*m.b57 + m.x181 <= 0)

m.c85 = Constraint(expr= - 672000*m.b50 - 672000*m.b54 - 672000*m.b58 + m.x182 <= 0)

m.c86 = Constraint(expr= - 672000*m.b51 - 672000*m.b55 - 672000*m.b59 + m.x183 <= 0)

m.c87 = Constraint(expr= - 672000*m.b52 - 672000*m.b56 - 672000*m.b60 + m.x184 <= 0)

m.c88 = Constraint(expr= - 672000*m.b97 - 672000*m.b101 - 672000*m.b105 + m.x185 <= 0)

m.c89 = Constraint(expr= - 672000*m.b98 - 672000*m.b102 - 672000*m.b106 + m.x186 <= 0)

m.c90 = Constraint(expr= - 672000*m.b99 - 672000*m.b103 - 672000*m.b107 + m.x187 <= 0)

m.c91 = Constraint(expr= - 672000*m.b100 - 672000*m.b104 - 672000*m.b108 + m.x188 <= 0)

m.c92 = Constraint(expr= - 804000*m.b13 - 804000*m.b17 - 804000*m.b21 + m.x189 <= 0)

m.c93 = Constraint(expr= - 804000*m.b14 - 804000*m.b18 - 804000*m.b22 + m.x190 <= 0)

m.c94 = Constraint(expr= - 804000*m.b15 - 804000*m.b19 - 804000*m.b23 + m.x191 <= 0)

m.c95 = Constraint(expr= - 804000*m.b16 - 804000*m.b20 - 804000*m.b24 + m.x192 <= 0)

m.c96 = Constraint(expr= - 774000*m.b61 - 774000*m.b65 - 774000*m.b69 + m.x193 <= 0)

m.c97 = Constraint(expr= - 774000*m.b62 - 774000*m.b66 - 774000*m.b70 + m.x194 <= 0)

m.c98 = Constraint(expr= - 774000*m.b63 - 774000*m.b67 - 774000*m.b71 + m.x195 <= 0)

m.c99 = Constraint(expr= - 774000*m.b64 - 774000*m.b68 - 774000*m.b72 + m.x196 <= 0)

m.c100 = Constraint(expr= - 1116000*m.b109 - 1116000*m.b113 - 1116000*m.b117 + m.x197 <= 0)

m.c101 = Constraint(expr= - 1116000*m.b110 - 1116000*m.b114 - 1116000*m.b118 + m.x198 <= 0)

m.c102 = Constraint(expr= - 1116000*m.b111 - 1116000*m.b115 - 1116000*m.b119 + m.x199 <= 0)

m.c103 = Constraint(expr= - 1116000*m.b112 - 1116000*m.b116 - 1116000*m.b120 + m.x200 <= 0)

m.c104 = Constraint(expr= - 804000*m.b25 - 804000*m.b29 - 804000*m.b33 + m.x201 <= 0)

m.c105 = Constraint(expr= - 804000*m.b26 - 804000*m.b30 - 804000*m.b34 + m.x202 <= 0)

m.c106 = Constraint(expr= - 804000*m.b27 - 804000*m.b31 - 804000*m.b35 + m.x203 <= 0)

m.c107 = Constraint(expr= - 804000*m.b28 - 804000*m.b32 - 804000*m.b36 + m.x204 <= 0)

m.c108 = Constraint(expr= - 804000*m.b73 - 804000*m.b77 - 804000*m.b81 + m.x205 <= 0)

m.c109 = Constraint(expr= - 804000*m.b74 - 804000*m.b78 - 804000*m.b82 + m.x206 <= 0)

m.c110 = Constraint(expr= - 804000*m.b75 - 804000*m.b79 - 804000*m.b83 + m.x207 <= 0)

m.c111 = Constraint(expr= - 804000*m.b76 - 804000*m.b80 - 804000*m.b84 + m.x208 <= 0)

m.c112 = Constraint(expr= - 804000*m.b121 - 804000*m.b125 - 804000*m.b129 + m.x209 <= 0)

m.c113 = Constraint(expr= - 804000*m.b122 - 804000*m.b126 - 804000*m.b130 + m.x210 <= 0)

m.c114 = Constraint(expr= - 804000*m.b123 - 804000*m.b127 - 804000*m.b131 + m.x211 <= 0)

m.c115 = Constraint(expr= - 804000*m.b124 - 804000*m.b128 - 804000*m.b132 + m.x212 <= 0)

m.c116 = Constraint(expr= - 726000*m.b37 - 726000*m.b41 - 726000*m.b45 + m.x213 <= 0)

m.c117 = Constraint(expr= - 726000*m.b38 - 726000*m.b42 - 726000*m.b46 + m.x214 <= 0)

m.c118 = Constraint(expr= - 726000*m.b39 - 726000*m.b43 - 726000*m.b47 + m.x215 <= 0)

m.c119 = Constraint(expr= - 726000*m.b40 - 726000*m.b44 - 726000*m.b48 + m.x216 <= 0)

m.c120 = Constraint(expr= - 696000*m.b85 - 696000*m.b89 - 696000*m.b93 + m.x217 <= 0)

m.c121 = Constraint(expr= - 696000*m.b86 - 696000*m.b90 - 696000*m.b94 + m.x218 <= 0)

m.c122 = Constraint(expr= - 696000*m.b87 - 696000*m.b91 - 696000*m.b95 + m.x219 <= 0)

m.c123 = Constraint(expr= - 696000*m.b88 - 696000*m.b92 - 696000*m.b96 + m.x220 <= 0)

m.c124 = Constraint(expr= - 852000*m.b133 - 852000*m.b137 - 852000*m.b141 + m.x221 <= 0)

m.c125 = Constraint(expr= - 852000*m.b134 - 852000*m.b138 - 852000*m.b142 + m.x222 <= 0)

m.c126 = Constraint(expr= - 852000*m.b135 - 852000*m.b139 - 852000*m.b143 + m.x223 <= 0)

m.c127 = Constraint(expr= - 852000*m.b136 - 852000*m.b140 - 852000*m.b144 + m.x224 <= 0)

m.c128 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8 + m.b9 + m.b10 + m.b11 + m.b12 == 1)

m.c129 = Constraint(expr=   m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 + m.b55 + m.b56 + m.b57 + m.b58 + m.b59
                          + m.b60 == 1)

m.c130 = Constraint(expr=   m.b97 + m.b98 + m.b99 + m.b100 + m.b101 + m.b102 + m.b103 + m.b104 + m.b105 + m.b106
                          + m.b107 + m.b108 == 1)

m.c131 = Constraint(expr=   m.b13 + m.b14 + m.b15 + m.b16 + m.b17 + m.b18 + m.b19 + m.b20 + m.b21 + m.b22 + m.b23
                          + m.b24 == 1)

m.c132 = Constraint(expr=   m.b61 + m.b62 + m.b63 + m.b64 + m.b65 + m.b66 + m.b67 + m.b68 + m.b69 + m.b70 + m.b71
                          + m.b72 == 1)

m.c133 = Constraint(expr=   m.b109 + m.b110 + m.b111 + m.b112 + m.b113 + m.b114 + m.b115 + m.b116 + m.b117 + m.b118
                          + m.b119 + m.b120 == 1)

m.c134 = Constraint(expr=   m.b25 + m.b26 + m.b27 + m.b28 + m.b29 + m.b30 + m.b31 + m.b32 + m.b33 + m.b34 + m.b35
                          + m.b36 == 1)

m.c135 = Constraint(expr=   m.b73 + m.b74 + m.b75 + m.b76 + m.b77 + m.b78 + m.b79 + m.b80 + m.b81 + m.b82 + m.b83
                          + m.b84 == 1)

m.c136 = Constraint(expr=   m.b121 + m.b122 + m.b123 + m.b124 + m.b125 + m.b126 + m.b127 + m.b128 + m.b129 + m.b130
                          + m.b131 + m.b132 == 1)

m.c137 = Constraint(expr=   m.b37 + m.b38 + m.b39 + m.b40 + m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 + m.b47
                          + m.b48 == 1)

m.c138 = Constraint(expr=   m.b85 + m.b86 + m.b87 + m.b88 + m.b89 + m.b90 + m.b91 + m.b92 + m.b93 + m.b94 + m.b95
                          + m.b96 == 1)

m.c139 = Constraint(expr=   m.b133 + m.b134 + m.b135 + m.b136 + m.b137 + m.b138 + m.b139 + m.b140 + m.b141 + m.b142
                          + m.b143 + m.b144 == 1)

m.c140 = Constraint(expr=   m.b1 + m.b5 + m.b9 == 1)

m.c141 = Constraint(expr=m.x329*m.x349 - m.x185 - m.x186 - m.x187 - m.x188 == 0)

m.c142 = Constraint(expr=m.x330*m.x349 - m.x197 - m.x198 - m.x199 - m.x200 == 0)

m.c143 = Constraint(expr=m.x331*m.x349 - m.x209 - m.x210 - m.x211 - m.x212 == 0)

m.c144 = Constraint(expr=m.x332*m.x349 - m.x221 - m.x222 - m.x223 - m.x224 == 0)

m.c145 = Constraint(expr=   m.x177 + m.x178 + m.x179 + m.x180 - m.x181 - m.x182 - m.x183 - m.x184 == 0)

m.c146 = Constraint(expr=   m.x181 + m.x182 + m.x183 + m.x184 - m.x185 - m.x186 - m.x187 - m.x188 == 0)

m.c147 = Constraint(expr=   m.x189 + m.x190 + m.x191 + m.x192 - m.x193 - m.x194 - m.x195 - m.x196 == 0)

m.c148 = Constraint(expr=   m.x193 + m.x194 + m.x195 + m.x196 - m.x197 - m.x198 - m.x199 - m.x200 == 0)

m.c149 = Constraint(expr=   m.x201 + m.x202 + m.x203 + m.x204 - m.x205 - m.x206 - m.x207 - m.x208 == 0)

m.c150 = Constraint(expr=   m.x205 + m.x206 + m.x207 + m.x208 - m.x209 - m.x210 - m.x211 - m.x212 == 0)

m.c151 = Constraint(expr=   m.x213 + m.x214 + m.x215 + m.x216 - m.x217 - m.x218 - m.x219 - m.x220 == 0)

m.c152 = Constraint(expr=   m.x217 + m.x218 + m.x219 + m.x220 - m.x221 - m.x222 - m.x223 - m.x224 == 0)

m.c153 = Constraint(expr=   600*m.b1 + 600*m.b5 + 600*m.b9 - m.x273 + m.x305 <= 600)

m.c154 = Constraint(expr=   600*m.b1 + 600*m.b2 + 600*m.b5 + 600*m.b6 + 600*m.b9 + 600*m.b10 - m.x276 + m.x305 <= 600)

m.c155 = Constraint(expr=   600*m.b1 + 600*m.b2 + 600*m.b3 + 600*m.b5 + 600*m.b6 + 600*m.b7 + 600*m.b9 + 600*m.b10
                          + 600*m.b11 - m.x279 + m.x305 <= 600)

m.c156 = Constraint(expr=   600*m.b1 + 600*m.b2 + 600*m.b3 + 600*m.b4 + 600*m.b5 + 600*m.b6 + 600*m.b7 + 600*m.b8
                          + 600*m.b9 + 600*m.b10 + 600*m.b11 + 600*m.b12 - m.x282 + m.x305 <= 600)

m.c157 = Constraint(expr=   600*m.b49 + 600*m.b53 + 600*m.b57 - m.x274 + m.x306 <= 600)

m.c158 = Constraint(expr=   600*m.b49 + 600*m.b50 + 600*m.b53 + 600*m.b54 + 600*m.b57 + 600*m.b58 - m.x277 + m.x306
                          <= 600)

m.c159 = Constraint(expr=   600*m.b49 + 600*m.b50 + 600*m.b51 + 600*m.b53 + 600*m.b54 + 600*m.b55 + 600*m.b57
                          + 600*m.b58 + 600*m.b59 - m.x280 + m.x306 <= 600)

m.c160 = Constraint(expr=   600*m.b49 + 600*m.b50 + 600*m.b51 + 600*m.b52 + 600*m.b53 + 600*m.b54 + 600*m.b55
                          + 600*m.b56 + 600*m.b57 + 600*m.b58 + 600*m.b59 + 600*m.b60 - m.x283 + m.x306 <= 600)

m.c161 = Constraint(expr=   600*m.b97 + 600*m.b101 + 600*m.b105 - m.x275 + m.x307 <= 600)

m.c162 = Constraint(expr=   600*m.b97 + 600*m.b98 + 600*m.b101 + 600*m.b102 + 600*m.b105 + 600*m.b106 - m.x278 + m.x307
                          <= 600)

m.c163 = Constraint(expr=   600*m.b97 + 600*m.b98 + 600*m.b99 + 600*m.b101 + 600*m.b102 + 600*m.b103 + 600*m.b105
                          + 600*m.b106 + 600*m.b107 - m.x281 + m.x307 <= 600)

m.c164 = Constraint(expr=   600*m.b97 + 600*m.b98 + 600*m.b99 + 600*m.b100 + 600*m.b101 + 600*m.b102 + 600*m.b103
                          + 600*m.b104 + 600*m.b105 + 600*m.b106 + 600*m.b107 + 600*m.b108 - m.x284 + m.x307 <= 600)

m.c165 = Constraint(expr=   600*m.b13 + 600*m.b17 + 600*m.b21 - m.x273 + m.x308 <= 600)

m.c166 = Constraint(expr=   600*m.b13 + 600*m.b14 + 600*m.b17 + 600*m.b18 + 600*m.b21 + 600*m.b22 - m.x276 + m.x308
                          <= 600)

m.c167 = Constraint(expr=   600*m.b13 + 600*m.b14 + 600*m.b15 + 600*m.b17 + 600*m.b18 + 600*m.b19 + 600*m.b21
                          + 600*m.b22 + 600*m.b23 - m.x279 + m.x308 <= 600)

m.c168 = Constraint(expr=   600*m.b13 + 600*m.b14 + 600*m.b15 + 600*m.b16 + 600*m.b17 + 600*m.b18 + 600*m.b19
                          + 600*m.b20 + 600*m.b21 + 600*m.b22 + 600*m.b23 + 600*m.b24 - m.x282 + m.x308 <= 600)

m.c169 = Constraint(expr=   600*m.b61 + 600*m.b65 + 600*m.b69 - m.x274 + m.x309 <= 600)

m.c170 = Constraint(expr=   600*m.b61 + 600*m.b62 + 600*m.b65 + 600*m.b66 + 600*m.b69 + 600*m.b70 - m.x277 + m.x309
                          <= 600)

m.c171 = Constraint(expr=   600*m.b61 + 600*m.b62 + 600*m.b63 + 600*m.b65 + 600*m.b66 + 600*m.b67 + 600*m.b69
                          + 600*m.b70 + 600*m.b71 - m.x280 + m.x309 <= 600)

m.c172 = Constraint(expr=   600*m.b61 + 600*m.b62 + 600*m.b63 + 600*m.b64 + 600*m.b65 + 600*m.b66 + 600*m.b67
                          + 600*m.b68 + 600*m.b69 + 600*m.b70 + 600*m.b71 + 600*m.b72 - m.x283 + m.x309 <= 600)

m.c173 = Constraint(expr=   600*m.b109 + 600*m.b113 + 600*m.b117 - m.x275 + m.x310 <= 600)

m.c174 = Constraint(expr=   600*m.b109 + 600*m.b110 + 600*m.b113 + 600*m.b114 + 600*m.b117 + 600*m.b118 - m.x278
                          + m.x310 <= 600)

m.c175 = Constraint(expr=   600*m.b109 + 600*m.b110 + 600*m.b111 + 600*m.b113 + 600*m.b114 + 600*m.b115 + 600*m.b117
                          + 600*m.b118 + 600*m.b119 - m.x281 + m.x310 <= 600)

m.c176 = Constraint(expr=   600*m.b109 + 600*m.b110 + 600*m.b111 + 600*m.b112 + 600*m.b113 + 600*m.b114 + 600*m.b115
                          + 600*m.b116 + 600*m.b117 + 600*m.b118 + 600*m.b119 + 600*m.b120 - m.x284 + m.x310 <= 600)

m.c177 = Constraint(expr=   600*m.b25 + 600*m.b29 + 600*m.b33 - m.x273 + m.x311 <= 600)

m.c178 = Constraint(expr=   600*m.b25 + 600*m.b26 + 600*m.b29 + 600*m.b30 + 600*m.b33 + 600*m.b34 - m.x276 + m.x311
                          <= 600)

m.c179 = Constraint(expr=   600*m.b25 + 600*m.b26 + 600*m.b27 + 600*m.b29 + 600*m.b30 + 600*m.b31 + 600*m.b33
                          + 600*m.b34 + 600*m.b35 - m.x279 + m.x311 <= 600)

m.c180 = Constraint(expr=   600*m.b25 + 600*m.b26 + 600*m.b27 + 600*m.b28 + 600*m.b29 + 600*m.b30 + 600*m.b31
                          + 600*m.b32 + 600*m.b33 + 600*m.b34 + 600*m.b35 + 600*m.b36 - m.x282 + m.x311 <= 600)

m.c181 = Constraint(expr=   600*m.b73 + 600*m.b77 + 600*m.b81 - m.x274 + m.x312 <= 600)

m.c182 = Constraint(expr=   600*m.b73 + 600*m.b74 + 600*m.b77 + 600*m.b78 + 600*m.b81 + 600*m.b82 - m.x277 + m.x312
                          <= 600)

m.c183 = Constraint(expr=   600*m.b73 + 600*m.b74 + 600*m.b75 + 600*m.b77 + 600*m.b78 + 600*m.b79 + 600*m.b81
                          + 600*m.b82 + 600*m.b83 - m.x280 + m.x312 <= 600)

m.c184 = Constraint(expr=   600*m.b73 + 600*m.b74 + 600*m.b75 + 600*m.b76 + 600*m.b77 + 600*m.b78 + 600*m.b79
                          + 600*m.b80 + 600*m.b81 + 600*m.b82 + 600*m.b83 + 600*m.b84 - m.x283 + m.x312 <= 600)

m.c185 = Constraint(expr=   600*m.b121 + 600*m.b125 + 600*m.b129 - m.x275 + m.x313 <= 600)

m.c186 = Constraint(expr=   600*m.b121 + 600*m.b122 + 600*m.b125 + 600*m.b126 + 600*m.b129 + 600*m.b130 - m.x278
                          + m.x313 <= 600)

m.c187 = Constraint(expr=   600*m.b121 + 600*m.b122 + 600*m.b123 + 600*m.b125 + 600*m.b126 + 600*m.b127 + 600*m.b129
                          + 600*m.b130 + 600*m.b131 - m.x281 + m.x313 <= 600)

m.c188 = Constraint(expr=   600*m.b121 + 600*m.b122 + 600*m.b123 + 600*m.b124 + 600*m.b125 + 600*m.b126 + 600*m.b127
                          + 600*m.b128 + 600*m.b129 + 600*m.b130 + 600*m.b131 + 600*m.b132 - m.x284 + m.x313 <= 600)

m.c189 = Constraint(expr=   600*m.b37 + 600*m.b41 + 600*m.b45 - m.x273 + m.x314 <= 600)

m.c190 = Constraint(expr=   600*m.b37 + 600*m.b38 + 600*m.b41 + 600*m.b42 + 600*m.b45 + 600*m.b46 - m.x276 + m.x314
                          <= 600)

m.c191 = Constraint(expr=   600*m.b37 + 600*m.b38 + 600*m.b39 + 600*m.b41 + 600*m.b42 + 600*m.b43 + 600*m.b45
                          + 600*m.b46 + 600*m.b47 - m.x279 + m.x314 <= 600)

m.c192 = Constraint(expr=   600*m.b37 + 600*m.b38 + 600*m.b39 + 600*m.b40 + 600*m.b41 + 600*m.b42 + 600*m.b43
                          + 600*m.b44 + 600*m.b45 + 600*m.b46 + 600*m.b47 + 600*m.b48 - m.x282 + m.x314 <= 600)

m.c193 = Constraint(expr=   600*m.b85 + 600*m.b89 + 600*m.b93 - m.x274 + m.x315 <= 600)

m.c194 = Constraint(expr=   600*m.b85 + 600*m.b86 + 600*m.b89 + 600*m.b90 + 600*m.b93 + 600*m.b94 - m.x277 + m.x315
                          <= 600)

m.c195 = Constraint(expr=   600*m.b85 + 600*m.b86 + 600*m.b87 + 600*m.b89 + 600*m.b90 + 600*m.b91 + 600*m.b93
                          + 600*m.b94 + 600*m.b95 - m.x280 + m.x315 <= 600)

m.c196 = Constraint(expr=   600*m.b85 + 600*m.b86 + 600*m.b87 + 600*m.b88 + 600*m.b89 + 600*m.b90 + 600*m.b91
                          + 600*m.b92 + 600*m.b93 + 600*m.b94 + 600*m.b95 + 600*m.b96 - m.x283 + m.x315 <= 600)

m.c197 = Constraint(expr=   600*m.b133 + 600*m.b137 + 600*m.b141 - m.x275 + m.x316 <= 600)

m.c198 = Constraint(expr=   600*m.b133 + 600*m.b134 + 600*m.b137 + 600*m.b138 + 600*m.b141 + 600*m.b142 - m.x278
                          + m.x316 <= 600)

m.c199 = Constraint(expr=   600*m.b133 + 600*m.b134 + 600*m.b135 + 600*m.b137 + 600*m.b138 + 600*m.b139 + 600*m.b141
                          + 600*m.b142 + 600*m.b143 - m.x281 + m.x316 <= 600)

m.c200 = Constraint(expr=   600*m.b133 + 600*m.b134 + 600*m.b135 + 600*m.b136 + 600*m.b137 + 600*m.b138 + 600*m.b139
                          + 600*m.b140 + 600*m.b141 + 600*m.b142 + 600*m.b143 + 600*m.b144 - m.x284 + m.x316 <= 600)

m.c201 = Constraint(expr= - 600*m.b1 - 600*m.b2 - 600*m.b3 - 600*m.b4 - 600*m.b5 - 600*m.b6 - 600*m.b7 - 600*m.b8
                          - 600*m.b9 - 600*m.b10 - 600*m.b11 - 600*m.b12 - m.x273 + m.x305 >= -600)

m.c202 = Constraint(expr= - 600*m.b2 - 600*m.b3 - 600*m.b4 - 600*m.b6 - 600*m.b7 - 600*m.b8 - 600*m.b10 - 600*m.b11
                          - 600*m.b12 - m.x276 + m.x305 >= -600)

m.c203 = Constraint(expr= - 600*m.b3 - 600*m.b4 - 600*m.b7 - 600*m.b8 - 600*m.b11 - 600*m.b12 - m.x279 + m.x305 >= -600)

m.c204 = Constraint(expr= - 600*m.b4 - 600*m.b8 - 600*m.b12 - m.x282 + m.x305 >= -600)

m.c205 = Constraint(expr= - 600*m.b49 - 600*m.b50 - 600*m.b51 - 600*m.b52 - 600*m.b53 - 600*m.b54 - 600*m.b55
                          - 600*m.b56 - 600*m.b57 - 600*m.b58 - 600*m.b59 - 600*m.b60 - m.x274 + m.x306 >= -600)

m.c206 = Constraint(expr= - 600*m.b50 - 600*m.b51 - 600*m.b52 - 600*m.b54 - 600*m.b55 - 600*m.b56 - 600*m.b58
                          - 600*m.b59 - 600*m.b60 - m.x277 + m.x306 >= -600)

m.c207 = Constraint(expr= - 600*m.b51 - 600*m.b52 - 600*m.b55 - 600*m.b56 - 600*m.b59 - 600*m.b60 - m.x280 + m.x306
                          >= -600)

m.c208 = Constraint(expr= - 600*m.b52 - 600*m.b56 - 600*m.b60 - m.x283 + m.x306 >= -600)

m.c209 = Constraint(expr= - 600*m.b97 - 600*m.b98 - 600*m.b99 - 600*m.b100 - 600*m.b101 - 600*m.b102 - 600*m.b103
                          - 600*m.b104 - 600*m.b105 - 600*m.b106 - 600*m.b107 - 600*m.b108 - m.x275 + m.x307 >= -600)

m.c210 = Constraint(expr= - 600*m.b98 - 600*m.b99 - 600*m.b100 - 600*m.b102 - 600*m.b103 - 600*m.b104 - 600*m.b106
                          - 600*m.b107 - 600*m.b108 - m.x278 + m.x307 >= -600)

m.c211 = Constraint(expr= - 600*m.b99 - 600*m.b100 - 600*m.b103 - 600*m.b104 - 600*m.b107 - 600*m.b108 - m.x281 + m.x307
                          >= -600)

m.c212 = Constraint(expr= - 600*m.b100 - 600*m.b104 - 600*m.b108 - m.x284 + m.x307 >= -600)

m.c213 = Constraint(expr= - 600*m.b13 - 600*m.b14 - 600*m.b15 - 600*m.b16 - 600*m.b17 - 600*m.b18 - 600*m.b19
                          - 600*m.b20 - 600*m.b21 - 600*m.b22 - 600*m.b23 - 600*m.b24 - m.x273 + m.x308 >= -600)

m.c214 = Constraint(expr= - 600*m.b14 - 600*m.b15 - 600*m.b16 - 600*m.b18 - 600*m.b19 - 600*m.b20 - 600*m.b22
                          - 600*m.b23 - 600*m.b24 - m.x276 + m.x308 >= -600)

m.c215 = Constraint(expr= - 600*m.b15 - 600*m.b16 - 600*m.b19 - 600*m.b20 - 600*m.b23 - 600*m.b24 - m.x279 + m.x308
                          >= -600)

m.c216 = Constraint(expr= - 600*m.b16 - 600*m.b20 - 600*m.b24 - m.x282 + m.x308 >= -600)

m.c217 = Constraint(expr= - 600*m.b61 - 600*m.b62 - 600*m.b63 - 600*m.b64 - 600*m.b65 - 600*m.b66 - 600*m.b67
                          - 600*m.b68 - 600*m.b69 - 600*m.b70 - 600*m.b71 - 600*m.b72 - m.x274 + m.x309 >= -600)

m.c218 = Constraint(expr= - 600*m.b62 - 600*m.b63 - 600*m.b64 - 600*m.b66 - 600*m.b67 - 600*m.b68 - 600*m.b70
                          - 600*m.b71 - 600*m.b72 - m.x277 + m.x309 >= -600)

m.c219 = Constraint(expr= - 600*m.b63 - 600*m.b64 - 600*m.b67 - 600*m.b68 - 600*m.b71 - 600*m.b72 - m.x280 + m.x309
                          >= -600)

m.c220 = Constraint(expr= - 600*m.b64 - 600*m.b68 - 600*m.b72 - m.x283 + m.x309 >= -600)

m.c221 = Constraint(expr= - 600*m.b109 - 600*m.b110 - 600*m.b111 - 600*m.b112 - 600*m.b113 - 600*m.b114 - 600*m.b115
                          - 600*m.b116 - 600*m.b117 - 600*m.b118 - 600*m.b119 - 600*m.b120 - m.x275 + m.x310 >= -600)

m.c222 = Constraint(expr= - 600*m.b110 - 600*m.b111 - 600*m.b112 - 600*m.b114 - 600*m.b115 - 600*m.b116 - 600*m.b118
                          - 600*m.b119 - 600*m.b120 - m.x278 + m.x310 >= -600)

m.c223 = Constraint(expr= - 600*m.b111 - 600*m.b112 - 600*m.b115 - 600*m.b116 - 600*m.b119 - 600*m.b120 - m.x281
                          + m.x310 >= -600)

m.c224 = Constraint(expr= - 600*m.b112 - 600*m.b116 - 600*m.b120 - m.x284 + m.x310 >= -600)

m.c225 = Constraint(expr= - 600*m.b25 - 600*m.b26 - 600*m.b27 - 600*m.b28 - 600*m.b29 - 600*m.b30 - 600*m.b31
                          - 600*m.b32 - 600*m.b33 - 600*m.b34 - 600*m.b35 - 600*m.b36 - m.x273 + m.x311 >= -600)

m.c226 = Constraint(expr= - 600*m.b26 - 600*m.b27 - 600*m.b28 - 600*m.b30 - 600*m.b31 - 600*m.b32 - 600*m.b34
                          - 600*m.b35 - 600*m.b36 - m.x276 + m.x311 >= -600)

m.c227 = Constraint(expr= - 600*m.b27 - 600*m.b28 - 600*m.b31 - 600*m.b32 - 600*m.b35 - 600*m.b36 - m.x279 + m.x311
                          >= -600)

m.c228 = Constraint(expr= - 600*m.b28 - 600*m.b32 - 600*m.b36 - m.x282 + m.x311 >= -600)

m.c229 = Constraint(expr= - 600*m.b73 - 600*m.b74 - 600*m.b75 - 600*m.b76 - 600*m.b77 - 600*m.b78 - 600*m.b79
                          - 600*m.b80 - 600*m.b81 - 600*m.b82 - 600*m.b83 - 600*m.b84 - m.x274 + m.x312 >= -600)

m.c230 = Constraint(expr= - 600*m.b74 - 600*m.b75 - 600*m.b76 - 600*m.b78 - 600*m.b79 - 600*m.b80 - 600*m.b82
                          - 600*m.b83 - 600*m.b84 - m.x277 + m.x312 >= -600)

m.c231 = Constraint(expr= - 600*m.b75 - 600*m.b76 - 600*m.b79 - 600*m.b80 - 600*m.b83 - 600*m.b84 - m.x280 + m.x312
                          >= -600)

m.c232 = Constraint(expr= - 600*m.b76 - 600*m.b80 - 600*m.b84 - m.x283 + m.x312 >= -600)

m.c233 = Constraint(expr= - 600*m.b121 - 600*m.b122 - 600*m.b123 - 600*m.b124 - 600*m.b125 - 600*m.b126 - 600*m.b127
                          - 600*m.b128 - 600*m.b129 - 600*m.b130 - 600*m.b131 - 600*m.b132 - m.x275 + m.x313 >= -600)

m.c234 = Constraint(expr= - 600*m.b122 - 600*m.b123 - 600*m.b124 - 600*m.b126 - 600*m.b127 - 600*m.b128 - 600*m.b130
                          - 600*m.b131 - 600*m.b132 - m.x278 + m.x313 >= -600)

m.c235 = Constraint(expr= - 600*m.b123 - 600*m.b124 - 600*m.b127 - 600*m.b128 - 600*m.b131 - 600*m.b132 - m.x281
                          + m.x313 >= -600)

m.c236 = Constraint(expr= - 600*m.b124 - 600*m.b128 - 600*m.b132 - m.x284 + m.x313 >= -600)

m.c237 = Constraint(expr= - 600*m.b37 - 600*m.b38 - 600*m.b39 - 600*m.b40 - 600*m.b41 - 600*m.b42 - 600*m.b43
                          - 600*m.b44 - 600*m.b45 - 600*m.b46 - 600*m.b47 - 600*m.b48 - m.x273 + m.x314 >= -600)

m.c238 = Constraint(expr= - 600*m.b38 - 600*m.b39 - 600*m.b40 - 600*m.b42 - 600*m.b43 - 600*m.b44 - 600*m.b46
                          - 600*m.b47 - 600*m.b48 - m.x276 + m.x314 >= -600)

m.c239 = Constraint(expr= - 600*m.b39 - 600*m.b40 - 600*m.b43 - 600*m.b44 - 600*m.b47 - 600*m.b48 - m.x279 + m.x314
                          >= -600)

m.c240 = Constraint(expr= - 600*m.b40 - 600*m.b44 - 600*m.b48 - m.x282 + m.x314 >= -600)

m.c241 = Constraint(expr= - 600*m.b85 - 600*m.b86 - 600*m.b87 - 600*m.b88 - 600*m.b89 - 600*m.b90 - 600*m.b91
                          - 600*m.b92 - 600*m.b93 - 600*m.b94 - 600*m.b95 - 600*m.b96 - m.x274 + m.x315 >= -600)

m.c242 = Constraint(expr= - 600*m.b86 - 600*m.b87 - 600*m.b88 - 600*m.b90 - 600*m.b91 - 600*m.b92 - 600*m.b94
                          - 600*m.b95 - 600*m.b96 - m.x277 + m.x315 >= -600)

m.c243 = Constraint(expr= - 600*m.b87 - 600*m.b88 - 600*m.b91 - 600*m.b92 - 600*m.b95 - 600*m.b96 - m.x280 + m.x315
                          >= -600)

m.c244 = Constraint(expr= - 600*m.b88 - 600*m.b92 - 600*m.b96 - m.x283 + m.x315 >= -600)

m.c245 = Constraint(expr= - 600*m.b133 - 600*m.b134 - 600*m.b135 - 600*m.b136 - 600*m.b137 - 600*m.b138 - 600*m.b139
                          - 600*m.b140 - 600*m.b141 - 600*m.b142 - 600*m.b143 - 600*m.b144 - m.x275 + m.x316 >= -600)

m.c246 = Constraint(expr= - 600*m.b134 - 600*m.b135 - 600*m.b136 - 600*m.b138 - 600*m.b139 - 600*m.b140 - 600*m.b142
                          - 600*m.b143 - 600*m.b144 - m.x278 + m.x316 >= -600)

m.c247 = Constraint(expr= - 600*m.b135 - 600*m.b136 - 600*m.b139 - 600*m.b140 - 600*m.b143 - 600*m.b144 - m.x281
                          + m.x316 >= -600)

m.c248 = Constraint(expr= - 600*m.b136 - 600*m.b140 - 600*m.b144 - m.x284 + m.x316 >= -600)

m.c249 = Constraint(expr=   600*m.b1 + 600*m.b5 + 600*m.b9 - m.x285 + m.x317 <= 600)

m.c250 = Constraint(expr=   600*m.b1 + 600*m.b2 + 600*m.b5 + 600*m.b6 + 600*m.b9 + 600*m.b10 - m.x288 + m.x317 <= 600)

m.c251 = Constraint(expr=   600*m.b1 + 600*m.b2 + 600*m.b3 + 600*m.b5 + 600*m.b6 + 600*m.b7 + 600*m.b9 + 600*m.b10
                          + 600*m.b11 - m.x291 + m.x317 <= 600)

m.c252 = Constraint(expr=   600*m.b1 + 600*m.b2 + 600*m.b3 + 600*m.b4 + 600*m.b5 + 600*m.b6 + 600*m.b7 + 600*m.b8
                          + 600*m.b9 + 600*m.b10 + 600*m.b11 + 600*m.b12 - m.x294 + m.x317 <= 600)

m.c253 = Constraint(expr=   600*m.b49 + 600*m.b53 + 600*m.b57 - m.x286 + m.x318 <= 600)

m.c254 = Constraint(expr=   600*m.b49 + 600*m.b50 + 600*m.b53 + 600*m.b54 + 600*m.b57 + 600*m.b58 - m.x289 + m.x318
                          <= 600)

m.c255 = Constraint(expr=   600*m.b49 + 600*m.b50 + 600*m.b51 + 600*m.b53 + 600*m.b54 + 600*m.b55 + 600*m.b57
                          + 600*m.b58 + 600*m.b59 - m.x292 + m.x318 <= 600)

m.c256 = Constraint(expr=   600*m.b49 + 600*m.b50 + 600*m.b51 + 600*m.b52 + 600*m.b53 + 600*m.b54 + 600*m.b55
                          + 600*m.b56 + 600*m.b57 + 600*m.b58 + 600*m.b59 + 600*m.b60 - m.x295 + m.x318 <= 600)

m.c257 = Constraint(expr=   600*m.b97 + 600*m.b101 + 600*m.b105 - m.x287 + m.x319 <= 600)

m.c258 = Constraint(expr=   600*m.b97 + 600*m.b98 + 600*m.b101 + 600*m.b102 + 600*m.b105 + 600*m.b106 - m.x290 + m.x319
                          <= 600)

m.c259 = Constraint(expr=   600*m.b97 + 600*m.b98 + 600*m.b99 + 600*m.b101 + 600*m.b102 + 600*m.b103 + 600*m.b105
                          + 600*m.b106 + 600*m.b107 - m.x293 + m.x319 <= 600)

m.c260 = Constraint(expr=   600*m.b97 + 600*m.b98 + 600*m.b99 + 600*m.b100 + 600*m.b101 + 600*m.b102 + 600*m.b103
                          + 600*m.b104 + 600*m.b105 + 600*m.b106 + 600*m.b107 + 600*m.b108 - m.x296 + m.x319 <= 600)

m.c261 = Constraint(expr=   600*m.b13 + 600*m.b17 + 600*m.b21 - m.x285 + m.x320 <= 600)

m.c262 = Constraint(expr=   600*m.b13 + 600*m.b14 + 600*m.b17 + 600*m.b18 + 600*m.b21 + 600*m.b22 - m.x288 + m.x320
                          <= 600)

m.c263 = Constraint(expr=   600*m.b13 + 600*m.b14 + 600*m.b15 + 600*m.b17 + 600*m.b18 + 600*m.b19 + 600*m.b21
                          + 600*m.b22 + 600*m.b23 - m.x291 + m.x320 <= 600)

m.c264 = Constraint(expr=   600*m.b13 + 600*m.b14 + 600*m.b15 + 600*m.b16 + 600*m.b17 + 600*m.b18 + 600*m.b19
                          + 600*m.b20 + 600*m.b21 + 600*m.b22 + 600*m.b23 + 600*m.b24 - m.x294 + m.x320 <= 600)

m.c265 = Constraint(expr=   600*m.b61 + 600*m.b65 + 600*m.b69 - m.x286 + m.x321 <= 600)

m.c266 = Constraint(expr=   600*m.b61 + 600*m.b62 + 600*m.b65 + 600*m.b66 + 600*m.b69 + 600*m.b70 - m.x289 + m.x321
                          <= 600)

m.c267 = Constraint(expr=   600*m.b61 + 600*m.b62 + 600*m.b63 + 600*m.b65 + 600*m.b66 + 600*m.b67 + 600*m.b69
                          + 600*m.b70 + 600*m.b71 - m.x292 + m.x321 <= 600)

m.c268 = Constraint(expr=   600*m.b61 + 600*m.b62 + 600*m.b63 + 600*m.b64 + 600*m.b65 + 600*m.b66 + 600*m.b67
                          + 600*m.b68 + 600*m.b69 + 600*m.b70 + 600*m.b71 + 600*m.b72 - m.x295 + m.x321 <= 600)

m.c269 = Constraint(expr=   600*m.b109 + 600*m.b113 + 600*m.b117 - m.x287 + m.x322 <= 600)

m.c270 = Constraint(expr=   600*m.b109 + 600*m.b110 + 600*m.b113 + 600*m.b114 + 600*m.b117 + 600*m.b118 - m.x290
                          + m.x322 <= 600)

m.c271 = Constraint(expr=   600*m.b109 + 600*m.b110 + 600*m.b111 + 600*m.b113 + 600*m.b114 + 600*m.b115 + 600*m.b117
                          + 600*m.b118 + 600*m.b119 - m.x293 + m.x322 <= 600)

m.c272 = Constraint(expr=   600*m.b109 + 600*m.b110 + 600*m.b111 + 600*m.b112 + 600*m.b113 + 600*m.b114 + 600*m.b115
                          + 600*m.b116 + 600*m.b117 + 600*m.b118 + 600*m.b119 + 600*m.b120 - m.x296 + m.x322 <= 600)

m.c273 = Constraint(expr=   600*m.b25 + 600*m.b29 + 600*m.b33 - m.x285 + m.x323 <= 600)

m.c274 = Constraint(expr=   600*m.b25 + 600*m.b26 + 600*m.b29 + 600*m.b30 + 600*m.b33 + 600*m.b34 - m.x288 + m.x323
                          <= 600)

m.c275 = Constraint(expr=   600*m.b25 + 600*m.b26 + 600*m.b27 + 600*m.b29 + 600*m.b30 + 600*m.b31 + 600*m.b33
                          + 600*m.b34 + 600*m.b35 - m.x291 + m.x323 <= 600)

m.c276 = Constraint(expr=   600*m.b25 + 600*m.b26 + 600*m.b27 + 600*m.b28 + 600*m.b29 + 600*m.b30 + 600*m.b31
                          + 600*m.b32 + 600*m.b33 + 600*m.b34 + 600*m.b35 + 600*m.b36 - m.x294 + m.x323 <= 600)

m.c277 = Constraint(expr=   600*m.b73 + 600*m.b77 + 600*m.b81 - m.x286 + m.x324 <= 600)

m.c278 = Constraint(expr=   600*m.b73 + 600*m.b74 + 600*m.b77 + 600*m.b78 + 600*m.b81 + 600*m.b82 - m.x289 + m.x324
                          <= 600)

m.c279 = Constraint(expr=   600*m.b73 + 600*m.b74 + 600*m.b75 + 600*m.b77 + 600*m.b78 + 600*m.b79 + 600*m.b81
                          + 600*m.b82 + 600*m.b83 - m.x292 + m.x324 <= 600)

m.c280 = Constraint(expr=   600*m.b73 + 600*m.b74 + 600*m.b75 + 600*m.b76 + 600*m.b77 + 600*m.b78 + 600*m.b79
                          + 600*m.b80 + 600*m.b81 + 600*m.b82 + 600*m.b83 + 600*m.b84 - m.x295 + m.x324 <= 600)

m.c281 = Constraint(expr=   600*m.b121 + 600*m.b125 + 600*m.b129 - m.x287 + m.x325 <= 600)

m.c282 = Constraint(expr=   600*m.b121 + 600*m.b122 + 600*m.b125 + 600*m.b126 + 600*m.b129 + 600*m.b130 - m.x290
                          + m.x325 <= 600)

m.c283 = Constraint(expr=   600*m.b121 + 600*m.b122 + 600*m.b123 + 600*m.b125 + 600*m.b126 + 600*m.b127 + 600*m.b129
                          + 600*m.b130 + 600*m.b131 - m.x293 + m.x325 <= 600)

m.c284 = Constraint(expr=   600*m.b121 + 600*m.b122 + 600*m.b123 + 600*m.b124 + 600*m.b125 + 600*m.b126 + 600*m.b127
                          + 600*m.b128 + 600*m.b129 + 600*m.b130 + 600*m.b131 + 600*m.b132 - m.x296 + m.x325 <= 600)

m.c285 = Constraint(expr=   600*m.b37 + 600*m.b41 + 600*m.b45 - m.x285 + m.x326 <= 600)

m.c286 = Constraint(expr=   600*m.b37 + 600*m.b38 + 600*m.b41 + 600*m.b42 + 600*m.b45 + 600*m.b46 - m.x288 + m.x326
                          <= 600)

m.c287 = Constraint(expr=   600*m.b37 + 600*m.b38 + 600*m.b39 + 600*m.b41 + 600*m.b42 + 600*m.b43 + 600*m.b45
                          + 600*m.b46 + 600*m.b47 - m.x291 + m.x326 <= 600)

m.c288 = Constraint(expr=   600*m.b37 + 600*m.b38 + 600*m.b39 + 600*m.b40 + 600*m.b41 + 600*m.b42 + 600*m.b43
                          + 600*m.b44 + 600*m.b45 + 600*m.b46 + 600*m.b47 + 600*m.b48 - m.x294 + m.x326 <= 600)

m.c289 = Constraint(expr=   600*m.b85 + 600*m.b89 + 600*m.b93 - m.x286 + m.x327 <= 600)

m.c290 = Constraint(expr=   600*m.b85 + 600*m.b86 + 600*m.b89 + 600*m.b90 + 600*m.b93 + 600*m.b94 - m.x289 + m.x327
                          <= 600)

m.c291 = Constraint(expr=   600*m.b85 + 600*m.b86 + 600*m.b87 + 600*m.b89 + 600*m.b90 + 600*m.b91 + 600*m.b93
                          + 600*m.b94 + 600*m.b95 - m.x292 + m.x327 <= 600)

m.c292 = Constraint(expr=   600*m.b85 + 600*m.b86 + 600*m.b87 + 600*m.b88 + 600*m.b89 + 600*m.b90 + 600*m.b91
                          + 600*m.b92 + 600*m.b93 + 600*m.b94 + 600*m.b95 + 600*m.b96 - m.x295 + m.x327 <= 600)

m.c293 = Constraint(expr=   600*m.b133 + 600*m.b137 + 600*m.b141 - m.x287 + m.x328 <= 600)

m.c294 = Constraint(expr=   600*m.b133 + 600*m.b134 + 600*m.b137 + 600*m.b138 + 600*m.b141 + 600*m.b142 - m.x290
                          + m.x328 <= 600)

m.c295 = Constraint(expr=   600*m.b133 + 600*m.b134 + 600*m.b135 + 600*m.b137 + 600*m.b138 + 600*m.b139 + 600*m.b141
                          + 600*m.b142 + 600*m.b143 - m.x293 + m.x328 <= 600)

m.c296 = Constraint(expr=   600*m.b133 + 600*m.b134 + 600*m.b135 + 600*m.b136 + 600*m.b137 + 600*m.b138 + 600*m.b139
                          + 600*m.b140 + 600*m.b141 + 600*m.b142 + 600*m.b143 + 600*m.b144 - m.x296 + m.x328 <= 600)

m.c297 = Constraint(expr= - 600*m.b1 - 600*m.b2 - 600*m.b3 - 600*m.b4 - 600*m.b5 - 600*m.b6 - 600*m.b7 - 600*m.b8
                          - 600*m.b9 - 600*m.b10 - 600*m.b11 - 600*m.b12 - m.x285 + m.x317 >= -600)

m.c298 = Constraint(expr= - 600*m.b2 - 600*m.b3 - 600*m.b4 - 600*m.b6 - 600*m.b7 - 600*m.b8 - 600*m.b10 - 600*m.b11
                          - 600*m.b12 - m.x288 + m.x317 >= -600)

m.c299 = Constraint(expr= - 600*m.b3 - 600*m.b4 - 600*m.b7 - 600*m.b8 - 600*m.b11 - 600*m.b12 - m.x291 + m.x317 >= -600)

m.c300 = Constraint(expr= - 600*m.b4 - 600*m.b8 - 600*m.b12 - m.x294 + m.x317 >= -600)

m.c301 = Constraint(expr= - 600*m.b49 - 600*m.b50 - 600*m.b51 - 600*m.b52 - 600*m.b53 - 600*m.b54 - 600*m.b55
                          - 600*m.b56 - 600*m.b57 - 600*m.b58 - 600*m.b59 - 600*m.b60 - m.x286 + m.x318 >= -600)

m.c302 = Constraint(expr= - 600*m.b50 - 600*m.b51 - 600*m.b52 - 600*m.b54 - 600*m.b55 - 600*m.b56 - 600*m.b58
                          - 600*m.b59 - 600*m.b60 - m.x289 + m.x318 >= -600)

m.c303 = Constraint(expr= - 600*m.b51 - 600*m.b52 - 600*m.b55 - 600*m.b56 - 600*m.b59 - 600*m.b60 - m.x292 + m.x318
                          >= -600)

m.c304 = Constraint(expr= - 600*m.b52 - 600*m.b56 - 600*m.b60 - m.x295 + m.x318 >= -600)

m.c305 = Constraint(expr= - 600*m.b97 - 600*m.b98 - 600*m.b99 - 600*m.b100 - 600*m.b101 - 600*m.b102 - 600*m.b103
                          - 600*m.b104 - 600*m.b105 - 600*m.b106 - 600*m.b107 - 600*m.b108 - m.x287 + m.x319 >= -600)

m.c306 = Constraint(expr= - 600*m.b98 - 600*m.b99 - 600*m.b100 - 600*m.b102 - 600*m.b103 - 600*m.b104 - 600*m.b106
                          - 600*m.b107 - 600*m.b108 - m.x290 + m.x319 >= -600)

m.c307 = Constraint(expr= - 600*m.b99 - 600*m.b100 - 600*m.b103 - 600*m.b104 - 600*m.b107 - 600*m.b108 - m.x293 + m.x319
                          >= -600)

m.c308 = Constraint(expr= - 600*m.b100 - 600*m.b104 - 600*m.b108 - m.x296 + m.x319 >= -600)

m.c309 = Constraint(expr= - 600*m.b13 - 600*m.b14 - 600*m.b15 - 600*m.b16 - 600*m.b17 - 600*m.b18 - 600*m.b19
                          - 600*m.b20 - 600*m.b21 - 600*m.b22 - 600*m.b23 - 600*m.b24 - m.x285 + m.x320 >= -600)

m.c310 = Constraint(expr= - 600*m.b14 - 600*m.b15 - 600*m.b16 - 600*m.b18 - 600*m.b19 - 600*m.b20 - 600*m.b22
                          - 600*m.b23 - 600*m.b24 - m.x288 + m.x320 >= -600)

m.c311 = Constraint(expr= - 600*m.b15 - 600*m.b16 - 600*m.b19 - 600*m.b20 - 600*m.b23 - 600*m.b24 - m.x291 + m.x320
                          >= -600)

m.c312 = Constraint(expr= - 600*m.b16 - 600*m.b20 - 600*m.b24 - m.x294 + m.x320 >= -600)

m.c313 = Constraint(expr= - 600*m.b61 - 600*m.b62 - 600*m.b63 - 600*m.b64 - 600*m.b65 - 600*m.b66 - 600*m.b67
                          - 600*m.b68 - 600*m.b69 - 600*m.b70 - 600*m.b71 - 600*m.b72 - m.x286 + m.x321 >= -600)

m.c314 = Constraint(expr= - 600*m.b62 - 600*m.b63 - 600*m.b64 - 600*m.b66 - 600*m.b67 - 600*m.b68 - 600*m.b70
                          - 600*m.b71 - 600*m.b72 - m.x289 + m.x321 >= -600)

m.c315 = Constraint(expr= - 600*m.b63 - 600*m.b64 - 600*m.b67 - 600*m.b68 - 600*m.b71 - 600*m.b72 - m.x292 + m.x321
                          >= -600)

m.c316 = Constraint(expr= - 600*m.b64 - 600*m.b68 - 600*m.b72 - m.x295 + m.x321 >= -600)

m.c317 = Constraint(expr= - 600*m.b109 - 600*m.b110 - 600*m.b111 - 600*m.b112 - 600*m.b113 - 600*m.b114 - 600*m.b115
                          - 600*m.b116 - 600*m.b117 - 600*m.b118 - 600*m.b119 - 600*m.b120 - m.x287 + m.x322 >= -600)

m.c318 = Constraint(expr= - 600*m.b110 - 600*m.b111 - 600*m.b112 - 600*m.b114 - 600*m.b115 - 600*m.b116 - 600*m.b118
                          - 600*m.b119 - 600*m.b120 - m.x290 + m.x322 >= -600)

m.c319 = Constraint(expr= - 600*m.b111 - 600*m.b112 - 600*m.b115 - 600*m.b116 - 600*m.b119 - 600*m.b120 - m.x293
                          + m.x322 >= -600)

m.c320 = Constraint(expr= - 600*m.b112 - 600*m.b116 - 600*m.b120 - m.x296 + m.x322 >= -600)

m.c321 = Constraint(expr= - 600*m.b25 - 600*m.b26 - 600*m.b27 - 600*m.b28 - 600*m.b29 - 600*m.b30 - 600*m.b31
                          - 600*m.b32 - 600*m.b33 - 600*m.b34 - 600*m.b35 - 600*m.b36 - m.x285 + m.x323 >= -600)

m.c322 = Constraint(expr= - 600*m.b26 - 600*m.b27 - 600*m.b28 - 600*m.b30 - 600*m.b31 - 600*m.b32 - 600*m.b34
                          - 600*m.b35 - 600*m.b36 - m.x288 + m.x323 >= -600)

m.c323 = Constraint(expr= - 600*m.b27 - 600*m.b28 - 600*m.b31 - 600*m.b32 - 600*m.b35 - 600*m.b36 - m.x291 + m.x323
                          >= -600)

m.c324 = Constraint(expr= - 600*m.b28 - 600*m.b32 - 600*m.b36 - m.x294 + m.x323 >= -600)

m.c325 = Constraint(expr= - 600*m.b73 - 600*m.b74 - 600*m.b75 - 600*m.b76 - 600*m.b77 - 600*m.b78 - 600*m.b79
                          - 600*m.b80 - 600*m.b81 - 600*m.b82 - 600*m.b83 - 600*m.b84 - m.x286 + m.x324 >= -600)

m.c326 = Constraint(expr= - 600*m.b74 - 600*m.b75 - 600*m.b76 - 600*m.b78 - 600*m.b79 - 600*m.b80 - 600*m.b82
                          - 600*m.b83 - 600*m.b84 - m.x289 + m.x324 >= -600)

m.c327 = Constraint(expr= - 600*m.b75 - 600*m.b76 - 600*m.b79 - 600*m.b80 - 600*m.b83 - 600*m.b84 - m.x292 + m.x324
                          >= -600)

m.c328 = Constraint(expr= - 600*m.b76 - 600*m.b80 - 600*m.b84 - m.x295 + m.x324 >= -600)

m.c329 = Constraint(expr= - 600*m.b121 - 600*m.b122 - 600*m.b123 - 600*m.b124 - 600*m.b125 - 600*m.b126 - 600*m.b127
                          - 600*m.b128 - 600*m.b129 - 600*m.b130 - 600*m.b131 - 600*m.b132 - m.x287 + m.x325 >= -600)

m.c330 = Constraint(expr= - 600*m.b122 - 600*m.b123 - 600*m.b124 - 600*m.b126 - 600*m.b127 - 600*m.b128 - 600*m.b130
                          - 600*m.b131 - 600*m.b132 - m.x290 + m.x325 >= -600)

m.c331 = Constraint(expr= - 600*m.b123 - 600*m.b124 - 600*m.b127 - 600*m.b128 - 600*m.b131 - 600*m.b132 - m.x293
                          + m.x325 >= -600)

m.c332 = Constraint(expr= - 600*m.b124 - 600*m.b128 - 600*m.b132 - m.x296 + m.x325 >= -600)

m.c333 = Constraint(expr= - 600*m.b37 - 600*m.b38 - 600*m.b39 - 600*m.b40 - 600*m.b41 - 600*m.b42 - 600*m.b43
                          - 600*m.b44 - 600*m.b45 - 600*m.b46 - 600*m.b47 - 600*m.b48 - m.x285 + m.x326 >= -600)

m.c334 = Constraint(expr= - 600*m.b38 - 600*m.b39 - 600*m.b40 - 600*m.b42 - 600*m.b43 - 600*m.b44 - 600*m.b46
                          - 600*m.b47 - 600*m.b48 - m.x288 + m.x326 >= -600)

m.c335 = Constraint(expr= - 600*m.b39 - 600*m.b40 - 600*m.b43 - 600*m.b44 - 600*m.b47 - 600*m.b48 - m.x291 + m.x326
                          >= -600)

m.c336 = Constraint(expr= - 600*m.b40 - 600*m.b44 - 600*m.b48 - m.x294 + m.x326 >= -600)

m.c337 = Constraint(expr= - 600*m.b85 - 600*m.b86 - 600*m.b87 - 600*m.b88 - 600*m.b89 - 600*m.b90 - 600*m.b91
                          - 600*m.b92 - 600*m.b93 - 600*m.b94 - 600*m.b95 - 600*m.b96 - m.x286 + m.x327 >= -600)

m.c338 = Constraint(expr= - 600*m.b86 - 600*m.b87 - 600*m.b88 - 600*m.b90 - 600*m.b91 - 600*m.b92 - 600*m.b94
                          - 600*m.b95 - 600*m.b96 - m.x289 + m.x327 >= -600)

m.c339 = Constraint(expr= - 600*m.b87 - 600*m.b88 - 600*m.b91 - 600*m.b92 - 600*m.b95 - 600*m.b96 - m.x292 + m.x327
                          >= -600)

m.c340 = Constraint(expr= - 600*m.b88 - 600*m.b92 - 600*m.b96 - m.x295 + m.x327 >= -600)

m.c341 = Constraint(expr= - 600*m.b133 - 600*m.b134 - 600*m.b135 - 600*m.b136 - 600*m.b137 - 600*m.b138 - 600*m.b139
                          - 600*m.b140 - 600*m.b141 - 600*m.b142 - 600*m.b143 - 600*m.b144 - m.x287 + m.x328 >= -600)

m.c342 = Constraint(expr= - 600*m.b134 - 600*m.b135 - 600*m.b136 - 600*m.b138 - 600*m.b139 - 600*m.b140 - 600*m.b142
                          - 600*m.b143 - 600*m.b144 - m.x290 + m.x328 >= -600)

m.c343 = Constraint(expr= - 600*m.b135 - 600*m.b136 - 600*m.b139 - 600*m.b140 - 600*m.b143 - 600*m.b144 - m.x293
                          + m.x328 >= -600)

m.c344 = Constraint(expr= - 600*m.b136 - 600*m.b140 - 600*m.b144 - m.x296 + m.x328 >= -600)

m.c345 = Constraint(expr=-m.x333*(m.x317 - m.x305) + m.x177 + m.x178 + m.x179 + m.x180 == 0)

m.c346 = Constraint(expr=-m.x334*(m.x318 - m.x306) + m.x181 + m.x182 + m.x183 + m.x184 == 0)

m.c347 = Constraint(expr=-m.x335*(m.x319 - m.x307) + m.x185 + m.x186 + m.x187 + m.x188 == 0)

m.c348 = Constraint(expr=-m.x336*(m.x320 - m.x308) + m.x189 + m.x190 + m.x191 + m.x192 == 0)

m.c349 = Constraint(expr=-m.x337*(m.x321 - m.x309) + m.x193 + m.x194 + m.x195 + m.x196 == 0)

m.c350 = Constraint(expr=-m.x338*(m.x322 - m.x310) + m.x197 + m.x198 + m.x199 + m.x200 == 0)

m.c351 = Constraint(expr=-m.x339*(m.x323 - m.x311) + m.x201 + m.x202 + m.x203 + m.x204 == 0)

m.c352 = Constraint(expr=-m.x340*(m.x324 - m.x312) + m.x205 + m.x206 + m.x207 + m.x208 == 0)

m.c353 = Constraint(expr=-m.x341*(m.x325 - m.x313) + m.x209 + m.x210 + m.x211 + m.x212 == 0)

m.c354 = Constraint(expr=-m.x342*(m.x326 - m.x314) + m.x213 + m.x214 + m.x215 + m.x216 == 0)

m.c355 = Constraint(expr=-m.x343*(m.x327 - m.x315) + m.x217 + m.x218 + m.x219 + m.x220 == 0)

m.c356 = Constraint(expr=-m.x344*(m.x328 - m.x316) + m.x221 + m.x222 + m.x223 + m.x224 == 0)

m.c357 = Constraint(expr= - 1170*m.b1 - 1170*m.b2 - 1170*m.b3 - 1170*m.b4 - 1170*m.b5 - 1170*m.b6 - 1170*m.b7
                          - 1170*m.b8 - 1170*m.b9 - 1170*m.b10 - 1170*m.b11 - 1170*m.b12 + m.x333 <= 0)

m.c358 = Constraint(expr= - 1120*m.b49 - 1120*m.b50 - 1120*m.b51 - 1120*m.b52 - 1120*m.b53 - 1120*m.b54 - 1120*m.b55
                          - 1120*m.b56 - 1120*m.b57 - 1120*m.b58 - 1120*m.b59 - 1120*m.b60 + m.x334 <= 0)

m.c359 = Constraint(expr= - 1120*m.b97 - 1120*m.b98 - 1120*m.b99 - 1120*m.b100 - 1120*m.b101 - 1120*m.b102 - 1120*m.b103
                          - 1120*m.b104 - 1120*m.b105 - 1120*m.b106 - 1120*m.b107 - 1120*m.b108 + m.x335 <= 0)

m.c360 = Constraint(expr= - 1340*m.b13 - 1340*m.b14 - 1340*m.b15 - 1340*m.b16 - 1340*m.b17 - 1340*m.b18 - 1340*m.b19
                          - 1340*m.b20 - 1340*m.b21 - 1340*m.b22 - 1340*m.b23 - 1340*m.b24 + m.x336 <= 0)

m.c361 = Constraint(expr= - 1290*m.b61 - 1290*m.b62 - 1290*m.b63 - 1290*m.b64 - 1290*m.b65 - 1290*m.b66 - 1290*m.b67
                          - 1290*m.b68 - 1290*m.b69 - 1290*m.b70 - 1290*m.b71 - 1290*m.b72 + m.x337 <= 0)

m.c362 = Constraint(expr= - 1860*m.b109 - 1860*m.b110 - 1860*m.b111 - 1860*m.b112 - 1860*m.b113 - 1860*m.b114
                          - 1860*m.b115 - 1860*m.b116 - 1860*m.b117 - 1860*m.b118 - 1860*m.b119 - 1860*m.b120 + m.x338
                          <= 0)

m.c363 = Constraint(expr= - 1340*m.b25 - 1340*m.b26 - 1340*m.b27 - 1340*m.b28 - 1340*m.b29 - 1340*m.b30 - 1340*m.b31
                          - 1340*m.b32 - 1340*m.b33 - 1340*m.b34 - 1340*m.b35 - 1340*m.b36 + m.x339 <= 0)

m.c364 = Constraint(expr= - 1340*m.b73 - 1340*m.b74 - 1340*m.b75 - 1340*m.b76 - 1340*m.b77 - 1340*m.b78 - 1340*m.b79
                          - 1340*m.b80 - 1340*m.b81 - 1340*m.b82 - 1340*m.b83 - 1340*m.b84 + m.x340 <= 0)

m.c365 = Constraint(expr= - 1340*m.b121 - 1340*m.b122 - 1340*m.b123 - 1340*m.b124 - 1340*m.b125 - 1340*m.b126
                          - 1340*m.b127 - 1340*m.b128 - 1340*m.b129 - 1340*m.b130 - 1340*m.b131 - 1340*m.b132 + m.x341
                          <= 0)

m.c366 = Constraint(expr= - 1210*m.b37 - 1210*m.b38 - 1210*m.b39 - 1210*m.b40 - 1210*m.b41 - 1210*m.b42 - 1210*m.b43
                          - 1210*m.b44 - 1210*m.b45 - 1210*m.b46 - 1210*m.b47 - 1210*m.b48 + m.x342 <= 0)

m.c367 = Constraint(expr= - 1160*m.b85 - 1160*m.b86 - 1160*m.b87 - 1160*m.b88 - 1160*m.b89 - 1160*m.b90 - 1160*m.b91
                          - 1160*m.b92 - 1160*m.b93 - 1160*m.b94 - 1160*m.b95 - 1160*m.b96 + m.x343 <= 0)

m.c368 = Constraint(expr= - 1420*m.b133 - 1420*m.b134 - 1420*m.b135 - 1420*m.b136 - 1420*m.b137 - 1420*m.b138
                          - 1420*m.b139 - 1420*m.b140 - 1420*m.b141 - 1420*m.b142 - 1420*m.b143 - 1420*m.b144 + m.x344
                          <= 0)

m.c369 = Constraint(expr=   m.x307 - m.x319 + m.x345 == 0)

m.c370 = Constraint(expr=   m.x310 - m.x322 + m.x346 == 0)

m.c371 = Constraint(expr=   m.x313 - m.x325 + m.x347 == 0)

m.c372 = Constraint(expr=   m.x316 - m.x328 + m.x348 == 0)

m.c373 = Constraint(expr=   m.x345 - m.x349 <= 0)

m.c374 = Constraint(expr=   m.x346 - m.x349 <= 0)

m.c375 = Constraint(expr=   m.x347 - m.x349 <= 0)

m.c376 = Constraint(expr=   m.x348 - m.x349 <= 0)

m.c377 = Constraint(expr=   600*m.b145 + 600*m.b161 + m.x305 - m.x306 <= 600)

m.c378 = Constraint(expr=   600*m.b146 + 600*m.b162 + m.x306 - m.x307 <= 600)

m.c379 = Constraint(expr=   600*m.b147 + 600*m.b163 + m.x308 - m.x309 <= 600)

m.c380 = Constraint(expr=   600*m.b148 + 600*m.b164 + m.x309 - m.x310 <= 600)

m.c381 = Constraint(expr=   600*m.b149 + 600*m.b165 + m.x311 - m.x312 <= 600)

m.c382 = Constraint(expr=   600*m.b150 + 600*m.b166 + m.x312 - m.x313 <= 600)

m.c383 = Constraint(expr=   600*m.b151 + 600*m.b167 + m.x314 - m.x315 <= 600)

m.c384 = Constraint(expr=   600*m.b152 + 600*m.b168 + m.x315 - m.x316 <= 600)

m.c385 = Constraint(expr= - 600*m.b153 - 600*m.b169 + m.x305 - m.x306 >= -600)

m.c386 = Constraint(expr= - 600*m.b154 - 600*m.b170 + m.x306 - m.x307 >= -600)

m.c387 = Constraint(expr= - 600*m.b155 - 600*m.b171 + m.x308 - m.x309 >= -600)

m.c388 = Constraint(expr= - 600*m.b156 - 600*m.b172 + m.x309 - m.x310 >= -600)

m.c389 = Constraint(expr= - 600*m.b157 - 600*m.b173 + m.x311 - m.x312 >= -600)

m.c390 = Constraint(expr= - 600*m.b158 - 600*m.b174 + m.x312 - m.x313 >= -600)

m.c391 = Constraint(expr= - 600*m.b159 - 600*m.b175 + m.x314 - m.x315 >= -600)

m.c392 = Constraint(expr= - 600*m.b160 - 600*m.b176 + m.x315 - m.x316 >= -600)

m.c393 = Constraint(expr=   1200*m.b145 + 1200*m.b169 + m.x317 - m.x318 <= 1200)

m.c394 = Constraint(expr=   1200*m.b146 + 1200*m.b170 + m.x318 - m.x319 <= 1200)

m.c395 = Constraint(expr=   1200*m.b147 + 1200*m.b171 + m.x320 - m.x321 <= 1200)

m.c396 = Constraint(expr=   1200*m.b148 + 1200*m.b172 + m.x321 - m.x322 <= 1200)

m.c397 = Constraint(expr=   1200*m.b149 + 1200*m.b173 + m.x323 - m.x324 <= 1200)

m.c398 = Constraint(expr=   1200*m.b150 + 1200*m.b174 + m.x324 - m.x325 <= 1200)

m.c399 = Constraint(expr=   1200*m.b151 + 1200*m.b175 + m.x326 - m.x327 <= 1200)

m.c400 = Constraint(expr=   1200*m.b152 + 1200*m.b176 + m.x327 - m.x328 <= 1200)

m.c401 = Constraint(expr= - 1200*m.b153 - 1200*m.b161 + m.x317 - m.x318 >= -1200)

m.c402 = Constraint(expr= - 1200*m.b154 - 1200*m.b162 + m.x318 - m.x319 >= -1200)

m.c403 = Constraint(expr= - 1200*m.b155 - 1200*m.b163 + m.x320 - m.x321 >= -1200)

m.c404 = Constraint(expr= - 1200*m.b156 - 1200*m.b164 + m.x321 - m.x322 >= -1200)

m.c405 = Constraint(expr= - 1200*m.b157 - 1200*m.b165 + m.x323 - m.x324 >= -1200)

m.c406 = Constraint(expr= - 1200*m.b158 - 1200*m.b166 + m.x324 - m.x325 >= -1200)

m.c407 = Constraint(expr= - 1200*m.b159 - 1200*m.b167 + m.x326 - m.x327 >= -1200)

m.c408 = Constraint(expr= - 1200*m.b160 - 1200*m.b168 + m.x327 - m.x328 >= -1200)

m.c409 = Constraint(expr= - 600*m.b145 - 600*m.b153 - 600*m.b161 - 600*m.b169 - m.x306 + m.x317 >= -600)

m.c410 = Constraint(expr= - 600*m.b146 - 600*m.b154 - 600*m.b162 - 600*m.b170 - m.x307 + m.x318 >= -600)

m.c411 = Constraint(expr= - 600*m.b147 - 600*m.b155 - 600*m.b163 - 600*m.b171 - m.x309 + m.x320 >= -600)

m.c412 = Constraint(expr= - 600*m.b148 - 600*m.b156 - 600*m.b164 - 600*m.b172 - m.x310 + m.x321 >= -600)

m.c413 = Constraint(expr= - 600*m.b149 - 600*m.b157 - 600*m.b165 - 600*m.b173 - m.x312 + m.x323 >= -600)

m.c414 = Constraint(expr= - 600*m.b150 - 600*m.b158 - 600*m.b166 - 600*m.b174 - m.x313 + m.x324 >= -600)

m.c415 = Constraint(expr= - 600*m.b151 - 600*m.b159 - 600*m.b167 - 600*m.b175 - m.x315 + m.x326 >= -600)

m.c416 = Constraint(expr= - 600*m.b152 - 600*m.b160 - 600*m.b168 - 600*m.b176 - m.x316 + m.x327 >= -600)

m.c417 = Constraint(expr= - 600*m.b145 - 600*m.b153 - 600*m.b161 - 600*m.b169 - m.x305 + m.x318 >= -600)

m.c418 = Constraint(expr= - 600*m.b146 - 600*m.b154 - 600*m.b162 - 600*m.b170 - m.x306 + m.x319 >= -600)

m.c419 = Constraint(expr= - 600*m.b147 - 600*m.b155 - 600*m.b163 - 600*m.b171 - m.x308 + m.x321 >= -600)

m.c420 = Constraint(expr= - 600*m.b148 - 600*m.b156 - 600*m.b164 - 600*m.b172 - m.x309 + m.x322 >= -600)

m.c421 = Constraint(expr= - 600*m.b149 - 600*m.b157 - 600*m.b165 - 600*m.b173 - m.x311 + m.x324 >= -600)

m.c422 = Constraint(expr= - 600*m.b150 - 600*m.b158 - 600*m.b166 - 600*m.b174 - m.x312 + m.x325 >= -600)

m.c423 = Constraint(expr= - 600*m.b151 - 600*m.b159 - 600*m.b167 - 600*m.b175 - m.x314 + m.x327 >= -600)

m.c424 = Constraint(expr= - 600*m.b152 - 600*m.b160 - 600*m.b168 - 600*m.b176 - m.x315 + m.x328 >= -600)

m.c425 = Constraint(expr=-(m.x306 - m.x305)*m.x333 - 672000*m.b145 + m.x297 >= -672000)

m.c426 = Constraint(expr=-(m.x307 - m.x306)*m.x334 - 672000*m.b146 + m.x298 >= -672000)

m.c427 = Constraint(expr=-(m.x309 - m.x308)*m.x336 - 774000*m.b147 + m.x299 >= -774000)

m.c428 = Constraint(expr=-(m.x310 - m.x309)*m.x337 - 774000*m.b148 + m.x300 >= -774000)

m.c429 = Constraint(expr=-(m.x312 - m.x311)*m.x339 - 804000*m.b149 + m.x301 >= -804000)

m.c430 = Constraint(expr=-(m.x313 - m.x312)*m.x340 - 804000*m.b150 + m.x302 >= -804000)

m.c431 = Constraint(expr=-(m.x315 - m.x314)*m.x342 - 696000*m.b151 + m.x303 >= -696000)

m.c432 = Constraint(expr=-(m.x316 - m.x315)*m.x343 - 696000*m.b152 + m.x304 >= -696000)

m.c433 = Constraint(expr=-(m.x318 - m.x317)*m.x334 - 672000*m.b145 + m.x297 >= -672000)

m.c434 = Constraint(expr=-(m.x319 - m.x318)*m.x335 - 672000*m.b146 + m.x298 >= -672000)

m.c435 = Constraint(expr=-(m.x321 - m.x320)*m.x337 - 774000*m.b147 + m.x299 >= -774000)

m.c436 = Constraint(expr=-(m.x322 - m.x321)*m.x338 - 774000*m.b148 + m.x300 >= -774000)

m.c437 = Constraint(expr=-(m.x324 - m.x323)*m.x340 - 804000*m.b149 + m.x301 >= -804000)

m.c438 = Constraint(expr=-(m.x325 - m.x324)*m.x341 - 804000*m.b150 + m.x302 >= -804000)

m.c439 = Constraint(expr=-(m.x327 - m.x326)*m.x343 - 696000*m.b151 + m.x303 >= -696000)

m.c440 = Constraint(expr=-(m.x328 - m.x327)*m.x344 - 696000*m.b152 + m.x304 >= -696000)

m.c441 = Constraint(expr=-(m.x305 - m.x306)*m.x334 - 672000*m.b153 + m.x297 >= -672000)

m.c442 = Constraint(expr=-(m.x306 - m.x307)*m.x335 - 672000*m.b154 + m.x298 >= -672000)

m.c443 = Constraint(expr=-(m.x308 - m.x309)*m.x337 - 774000*m.b155 + m.x299 >= -774000)

m.c444 = Constraint(expr=-(m.x309 - m.x310)*m.x338 - 774000*m.b156 + m.x300 >= -774000)

m.c445 = Constraint(expr=-(m.x311 - m.x312)*m.x340 - 804000*m.b157 + m.x301 >= -804000)

m.c446 = Constraint(expr=-(m.x312 - m.x313)*m.x341 - 804000*m.b158 + m.x302 >= -804000)

m.c447 = Constraint(expr=-(m.x314 - m.x315)*m.x343 - 696000*m.b159 + m.x303 >= -696000)

m.c448 = Constraint(expr=-(m.x315 - m.x316)*m.x344 - 696000*m.b160 + m.x304 >= -696000)

m.c449 = Constraint(expr=-(m.x317 - m.x318)*m.x333 - 672000*m.b153 + m.x297 >= -672000)

m.c450 = Constraint(expr=-(m.x318 - m.x319)*m.x334 - 672000*m.b154 + m.x298 >= -672000)

m.c451 = Constraint(expr=-(m.x320 - m.x321)*m.x336 - 774000*m.b155 + m.x299 >= -774000)

m.c452 = Constraint(expr=-(m.x321 - m.x322)*m.x337 - 774000*m.b156 + m.x300 >= -774000)

m.c453 = Constraint(expr=-(m.x323 - m.x324)*m.x339 - 804000*m.b157 + m.x301 >= -804000)

m.c454 = Constraint(expr=-(m.x324 - m.x325)*m.x340 - 804000*m.b158 + m.x302 >= -804000)

m.c455 = Constraint(expr=-(m.x326 - m.x327)*m.x342 - 696000*m.b159 + m.x303 >= -696000)

m.c456 = Constraint(expr=-(m.x327 - m.x328)*m.x343 - 696000*m.b160 + m.x304 >= -696000)

m.c457 = Constraint(expr=-(m.x334 - m.x333)*(m.x318 - m.x306) - 672000*m.b161 + m.x297 >= -672000)

m.c458 = Constraint(expr=-(m.x335 - m.x334)*(m.x319 - m.x307) - 672000*m.b162 + m.x298 >= -672000)

m.c459 = Constraint(expr=-(m.x337 - m.x336)*(m.x321 - m.x309) - 774000*m.b163 + m.x299 >= -774000)

m.c460 = Constraint(expr=-(m.x338 - m.x337)*(m.x322 - m.x310) - 774000*m.b164 + m.x300 >= -774000)

m.c461 = Constraint(expr=-(m.x340 - m.x339)*(m.x324 - m.x312) - 804000*m.b165 + m.x301 >= -804000)

m.c462 = Constraint(expr=-(m.x341 - m.x340)*(m.x325 - m.x313) - 804000*m.b166 + m.x302 >= -804000)

m.c463 = Constraint(expr=-(m.x343 - m.x342)*(m.x327 - m.x315) - 696000*m.b167 + m.x303 >= -696000)

m.c464 = Constraint(expr=-(m.x344 - m.x343)*(m.x328 - m.x316) - 696000*m.b168 + m.x304 >= -696000)

m.c465 = Constraint(expr=-(m.x333 - m.x334)*(m.x317 - m.x305) - 672000*m.b169 + m.x297 >= -672000)

m.c466 = Constraint(expr=-(m.x334 - m.x335)*(m.x318 - m.x306) - 672000*m.b170 + m.x298 >= -672000)

m.c467 = Constraint(expr=-(m.x336 - m.x337)*(m.x320 - m.x308) - 774000*m.b171 + m.x299 >= -774000)

m.c468 = Constraint(expr=-(m.x337 - m.x338)*(m.x321 - m.x309) - 774000*m.b172 + m.x300 >= -774000)

m.c469 = Constraint(expr=-(m.x339 - m.x340)*(m.x323 - m.x311) - 804000*m.b173 + m.x301 >= -804000)

m.c470 = Constraint(expr=-(m.x340 - m.x341)*(m.x324 - m.x312) - 804000*m.b174 + m.x302 >= -804000)

m.c471 = Constraint(expr=-(m.x342 - m.x343)*(m.x326 - m.x314) - 696000*m.b175 + m.x303 >= -696000)

m.c472 = Constraint(expr=-(m.x343 - m.x344)*(m.x327 - m.x315) - 696000*m.b176 + m.x304 >= -696000)

m.c473 = Constraint(expr=   672000*m.b145 + 672000*m.b153 + 672000*m.b161 + 672000*m.b169 - m.x177 - m.x178 - m.x179
                          - m.x180 + m.x297 >= 0)

m.c474 = Constraint(expr=   672000*m.b146 + 672000*m.b154 + 672000*m.b162 + 672000*m.b170 - m.x181 - m.x182 - m.x183
                          - m.x184 + m.x298 >= 0)

m.c475 = Constraint(expr=   774000*m.b147 + 774000*m.b155 + 774000*m.b163 + 774000*m.b171 - m.x189 - m.x190 - m.x191
                          - m.x192 + m.x299 >= 0)

m.c476 = Constraint(expr=   774000*m.b148 + 774000*m.b156 + 774000*m.b164 + 774000*m.b172 - m.x193 - m.x194 - m.x195
                          - m.x196 + m.x300 >= 0)

m.c477 = Constraint(expr=   804000*m.b149 + 804000*m.b157 + 804000*m.b165 + 804000*m.b173 - m.x201 - m.x202 - m.x203
                          - m.x204 + m.x301 >= 0)

m.c478 = Constraint(expr=   804000*m.b150 + 804000*m.b158 + 804000*m.b166 + 804000*m.b174 - m.x205 - m.x206 - m.x207
                          - m.x208 + m.x302 >= 0)

m.c479 = Constraint(expr=   696000*m.b151 + 696000*m.b159 + 696000*m.b167 + 696000*m.b175 - m.x213 - m.x214 - m.x215
                          - m.x216 + m.x303 >= 0)

m.c480 = Constraint(expr=   696000*m.b152 + 696000*m.b160 + 696000*m.b168 + 696000*m.b176 - m.x217 - m.x218 - m.x219
                          - m.x220 + m.x304 >= 0)

m.c481 = Constraint(expr=   2*m.b97 + 2*m.b98 + 2*m.b99 + 2*m.b100 + 2*m.b101 + 2*m.b102 + 2*m.b103 + 2*m.b104
                          + 8*m.b105 + 8*m.b106 + 8*m.b107 + 8*m.b108 + 2*m.b109 + 2*m.b110 + 2*m.b111 + 2*m.b112
                          + m.b113 + m.b114 + m.b115 + m.b116 + 8*m.b117 + 8*m.b118 + 8*m.b119 + 8*m.b120 + 2*m.b121
                          + 2*m.b122 + 2*m.b123 + 2*m.b124 + m.b125 + m.b126 + m.b127 + m.b128 + 8*m.b129 + 8*m.b130
                          + 8*m.b131 + 8*m.b132 + 8*m.b133 + 8*m.b134 + 8*m.b135 + 8*m.b136 + 8*m.b137 + 8*m.b138
                          + 8*m.b139 + 8*m.b140 + 8*m.b141 + 8*m.b142 + 8*m.b143 + 8*m.b144 + m.x345 + m.x346 + m.x347
                          + m.x348 - m.x349 == 0)
