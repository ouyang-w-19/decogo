#  MINLP written by GAMS Convert at 04/21/18 13:51:20
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       5005      252     2886     1867        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#       1298     1058      240        0        0        0        0        0
#  FX    303      168      135        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#      15763    15655      108        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b3 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b8 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b9 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b10 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b12 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b13 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b14 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b15 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b18 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b19 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b20 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b21 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b23 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b24 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b25 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b26 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b27 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b28 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b29 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b30 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b31 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b32 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b33 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b34 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b35 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b36 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b38 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b39 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b40 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b41 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b42 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b43 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b44 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b45 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b46 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b47 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b48 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b49 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b50 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b51 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b52 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b53 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b54 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b55 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b56 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b57 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b58 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b59 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b60 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b61 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b62 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b63 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b64 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b65 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b66 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b67 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b68 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b69 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b70 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b71 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b72 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b73 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b74 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b75 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b76 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b77 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b78 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b79 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b80 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b81 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b82 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b83 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b84 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b85 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b86 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b87 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b88 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b89 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b90 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b91 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b92 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b93 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b94 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b95 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b96 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b97 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b98 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b99 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b100 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b101 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b102 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b103 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b104 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b105 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b106 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b109 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b110 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b111 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b114 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b115 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b116 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b119 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b120 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b121 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b122 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b124 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b125 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b126 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b127 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b128 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b129 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b130 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b131 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b132 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b133 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b134 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b135 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b136 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b137 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b138 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b139 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b140 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b141 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b142 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b143 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b144 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b145 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b146 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b147 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b148 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b149 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b150 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b151 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b152 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b153 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b154 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b155 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b156 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b157 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b158 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b159 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b160 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b161 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b162 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b163 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b164 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b165 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b166 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b167 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b168 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b169 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b170 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b171 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b172 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b173 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b174 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b175 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b176 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b177 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b178 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b179 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b180 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b181 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b182 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b183 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b184 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b185 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b186 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b187 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b188 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b189 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b190 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b191 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b192 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b193 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b194 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b195 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b196 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b197 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b198 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b199 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b200 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b201 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b202 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b203 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b204 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b205 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x242 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x255 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x258 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x262 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x263 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x264 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x265 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x266 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x267 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x268 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x269 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x270 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x271 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x272 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x273 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x274 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x275 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x276 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x277 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x278 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x279 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x280 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x281 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x282 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x283 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x284 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x285 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x286 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x287 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x289 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x290 = Var(within=Reals,bounds=(0,1),initialize=0)
m.b291 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b292 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b293 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b294 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b295 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b296 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b297 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b298 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b299 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b300 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b301 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b302 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b303 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b304 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b305 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b306 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b307 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b308 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b309 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b310 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b311 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b312 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b313 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b314 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b315 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b316 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b317 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b318 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b319 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b320 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b321 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b322 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b323 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b324 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b325 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x326 = Var(within=Reals,bounds=(0,5000),initialize=0)
m.x327 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x328 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x329 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x330 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x331 = Var(within=Reals,bounds=(0,6000),initialize=0)
m.x332 = Var(within=Reals,bounds=(0,14500),initialize=0)
m.x333 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x334 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x335 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x336 = Var(within=Reals,bounds=(0,7000),initialize=0)
m.x337 = Var(within=Reals,bounds=(0,7000),initialize=0)
m.x338 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x339 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x340 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x341 = Var(within=Reals,bounds=(0,8000),initialize=0)
m.x342 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x343 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x344 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x345 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x346 = Var(within=Reals,bounds=(0,8000),initialize=0)
m.x347 = Var(within=Reals,bounds=(0,35000),initialize=0)
m.x348 = Var(within=Reals,bounds=(0,35000),initialize=0)
m.x349 = Var(within=Reals,bounds=(0,35000),initialize=0)
m.x350 = Var(within=Reals,bounds=(0,35000),initialize=0)
m.x351 = Var(within=Reals,bounds=(0,20000),initialize=0)
m.x352 = Var(within=Reals,bounds=(0,35000),initialize=0)
m.x353 = Var(within=Reals,bounds=(0,35000),initialize=0)
m.x354 = Var(within=Reals,bounds=(0,35000),initialize=0)
m.x355 = Var(within=Reals,bounds=(0,35000),initialize=0)
m.x356 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x357 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x358 = Var(within=Reals,bounds=(0,35000),initialize=0)
m.x359 = Var(within=Reals,bounds=(0,35000),initialize=0)
m.x360 = Var(within=Reals,bounds=(0,35000),initialize=0)
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
m.x416 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x417 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x418 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x419 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x420 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x421 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x422 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x423 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x424 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x425 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x426 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x427 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x428 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x429 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x430 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x431 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x432 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x433 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x434 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x435 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x436 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x437 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x438 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x439 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x440 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x441 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x442 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x443 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x444 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x445 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x446 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x447 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x448 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x449 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x450 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x451 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x452 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x453 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x454 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x455 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x456 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x457 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x458 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x459 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x460 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x461 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x462 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x463 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x464 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x465 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x466 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x467 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x468 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x469 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x470 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x471 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x472 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x473 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x474 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x475 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x476 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x477 = Var(within=Reals,bounds=(0,5000),initialize=0)
m.x478 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x479 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x480 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x481 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x482 = Var(within=Reals,bounds=(0,5000),initialize=0)
m.x483 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x484 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x485 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x486 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x487 = Var(within=Reals,bounds=(0,5000),initialize=0)
m.x488 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x489 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x490 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x491 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x492 = Var(within=Reals,bounds=(0,5000),initialize=0)
m.x493 = Var(within=Reals,bounds=(0,5000),initialize=0)
m.x494 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x495 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x496 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x497 = Var(within=Reals,bounds=(0,5000),initialize=0)
m.x498 = Var(within=Reals,bounds=(0,5000),initialize=0)
m.x499 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x500 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x501 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x502 = Var(within=Reals,bounds=(0,5000),initialize=0)
m.x503 = Var(within=Reals,bounds=(0,5000),initialize=0)
m.x504 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x505 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x506 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x507 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x508 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x509 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x510 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x511 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x512 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x513 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x514 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x515 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x516 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x517 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x518 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x519 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x520 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x521 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x522 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x523 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x524 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x525 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x526 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x527 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x528 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x529 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x530 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x531 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x532 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x533 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x534 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x535 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x536 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x537 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x538 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x539 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x540 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x541 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x542 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x543 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x544 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x545 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x546 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x547 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x548 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x549 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x550 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x551 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x552 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x553 = Var(within=Reals,bounds=(0,5000),initialize=0)
m.x554 = Var(within=Reals,bounds=(0,5000),initialize=0)
m.x555 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x556 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x557 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x558 = Var(within=Reals,bounds=(0,5000),initialize=0)
m.x559 = Var(within=Reals,bounds=(0,5000),initialize=0)
m.x560 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x561 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x562 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x563 = Var(within=Reals,bounds=(0,5000),initialize=0)
m.x564 = Var(within=Reals,bounds=(0,5000),initialize=0)
m.x565 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x566 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x567 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x568 = Var(within=Reals,bounds=(0,3500),initialize=0)
m.x569 = Var(within=Reals,bounds=(0,3500),initialize=0)
m.x570 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x571 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x572 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x573 = Var(within=Reals,bounds=(0,3500),initialize=0)
m.x574 = Var(within=Reals,bounds=(0,3500),initialize=0)
m.x575 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x576 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x577 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x578 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x579 = Var(within=Reals,bounds=(0,3500),initialize=0)
m.x580 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x581 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x582 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x583 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x584 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x585 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x586 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x587 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x588 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x589 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x590 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x591 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x592 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x593 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x594 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x595 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x596 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x597 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x598 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x599 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x600 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x601 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x602 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x603 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x604 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x605 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x606 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x607 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x608 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x609 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x610 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x611 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x612 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x613 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x614 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x615 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x616 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x617 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x618 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x619 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x620 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x621 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x622 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x623 = Var(within=Reals,bounds=(1,7),initialize=1)
m.x624 = Var(within=Reals,bounds=(1,7),initialize=1)
m.x625 = Var(within=Reals,bounds=(2,7),initialize=2)
m.x626 = Var(within=Reals,bounds=(2,7),initialize=2)
m.x627 = Var(within=Reals,bounds=(2,7),initialize=2)
m.x628 = Var(within=Reals,bounds=(2,7),initialize=2)
m.x629 = Var(within=Reals,bounds=(3,7),initialize=3)
m.x630 = Var(within=Reals,bounds=(4,7),initialize=4)
m.x631 = Var(within=Reals,bounds=(4,7),initialize=4)
m.x632 = Var(within=Reals,bounds=(4,7),initialize=4)
m.x633 = Var(within=Reals,bounds=(4,7),initialize=4)
m.x634 = Var(within=Reals,bounds=(5,7),initialize=5)
m.x635 = Var(within=Reals,bounds=(5,7),initialize=5)
m.x636 = Var(within=Reals,bounds=(6,7),initialize=6)
m.x637 = Var(within=Reals,bounds=(6,7),initialize=6)
m.x638 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x639 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x640 = Var(within=Reals,bounds=(1,7),initialize=1)
m.x641 = Var(within=Reals,bounds=(1,7),initialize=1)
m.x642 = Var(within=Reals,bounds=(2,7),initialize=2)
m.x643 = Var(within=Reals,bounds=(2,7),initialize=2)
m.x644 = Var(within=Reals,bounds=(2,7),initialize=2)
m.x645 = Var(within=Reals,bounds=(2,7),initialize=2)
m.x646 = Var(within=Reals,bounds=(3,7),initialize=3)
m.x647 = Var(within=Reals,bounds=(4,7),initialize=4)
m.x648 = Var(within=Reals,bounds=(4,7),initialize=4)
m.x649 = Var(within=Reals,bounds=(4,7),initialize=4)
m.x650 = Var(within=Reals,bounds=(4,7),initialize=4)
m.x651 = Var(within=Reals,bounds=(5,7),initialize=5)
m.x652 = Var(within=Reals,bounds=(5,7),initialize=5)
m.x653 = Var(within=Reals,bounds=(6,7),initialize=6)
m.x654 = Var(within=Reals,bounds=(6,7),initialize=6)
m.x655 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x656 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x657 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x658 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x659 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x660 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x661 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x662 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x663 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x664 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x665 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x666 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x667 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x668 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x669 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x670 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x671 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x672 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x673 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x674 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x675 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x676 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x677 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x678 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x679 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x680 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x681 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x682 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x683 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x684 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x685 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x686 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x687 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x688 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x689 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x690 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x691 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x692 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x693 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x694 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x695 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x696 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x697 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x698 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x699 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x700 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x701 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x702 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x703 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x704 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x705 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x706 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x707 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x708 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x709 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x710 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x711 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x712 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x713 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x714 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x715 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x716 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x717 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x718 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x719 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x720 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x721 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x722 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x723 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x724 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x725 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x726 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x727 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x728 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x729 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x730 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x731 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x732 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x733 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x734 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x735 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x736 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x737 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x738 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x739 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x740 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x741 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x742 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x743 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x744 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x745 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x746 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x747 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x748 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x749 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x750 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x751 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x752 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x753 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x754 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x755 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x756 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x757 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x758 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x759 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x760 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x761 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x762 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x763 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x764 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x765 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x766 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x767 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x768 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x769 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x770 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x771 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x772 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x773 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x774 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x775 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x776 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x777 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x778 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x779 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x780 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x781 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x782 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x783 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x784 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x785 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x786 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x787 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x788 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x789 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x790 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x791 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x792 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x793 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x794 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x795 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x796 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x797 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x798 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x799 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x800 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x801 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x802 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x803 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x804 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x805 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x806 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x807 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x808 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x809 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x810 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x811 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x812 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x813 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x814 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x815 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x816 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x817 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x818 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x819 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x820 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x821 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x822 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x823 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x824 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x825 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x826 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x827 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x828 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x829 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x830 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x831 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x832 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x833 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x834 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x835 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x836 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x837 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x838 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x839 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x840 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x841 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x842 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x843 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x844 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x845 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x846 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x847 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x848 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x849 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x850 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x851 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x852 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x853 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x854 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x855 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x856 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x857 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x858 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x859 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x860 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x861 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x862 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x863 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x864 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x865 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x866 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x867 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x868 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x869 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x870 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x871 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x872 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x873 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x874 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x875 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x876 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x877 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x878 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x879 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x880 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x881 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x882 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x883 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x884 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x885 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x886 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x887 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x888 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x889 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x890 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x891 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x892 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x893 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x894 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x895 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x896 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x897 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x898 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x899 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x900 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x901 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x902 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x903 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x904 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x905 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x906 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x907 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x908 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x909 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x910 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x911 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x912 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x913 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x914 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x915 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x916 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x917 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x918 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x919 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x920 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x921 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x922 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x923 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x924 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x925 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x926 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x927 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x928 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x929 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x930 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x931 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x932 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x933 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x934 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x935 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x936 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x937 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x938 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x939 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x940 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x941 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x942 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x943 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x944 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x945 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x946 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x947 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x948 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x949 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x950 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x951 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x952 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x953 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x954 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x955 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x956 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x957 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x958 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x959 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x960 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x961 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x962 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x963 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x964 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x965 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x966 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x967 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x968 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x969 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x970 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x971 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x972 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x973 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x974 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x975 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x976 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x977 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x978 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x979 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x980 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x981 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x982 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x983 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x984 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x985 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x986 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x987 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x988 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x989 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x990 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x991 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x992 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x993 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x994 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x995 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x996 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x997 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x998 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x999 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1000 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1001 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1002 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1003 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1004 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1005 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1006 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1007 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1008 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1009 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1010 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1011 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1012 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1013 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1014 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1015 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1016 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1017 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1018 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1019 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1020 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1021 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1022 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1023 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1024 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1025 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1026 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1027 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1028 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1029 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1030 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1031 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1032 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1033 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1034 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1035 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1036 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1037 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1038 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1039 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1040 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1041 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1042 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1043 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1044 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1045 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1046 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1047 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1048 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1049 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1050 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1051 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1052 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1053 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1054 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1055 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1056 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1057 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1058 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1059 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1060 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1061 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1062 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1063 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1064 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1065 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1066 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1067 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1068 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1069 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1070 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1071 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1072 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1073 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1074 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1075 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1076 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1077 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1078 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1079 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1080 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1081 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1082 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1083 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1084 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1085 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1086 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1087 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1088 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1089 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1090 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1091 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1092 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1093 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1094 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1095 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1096 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1097 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1098 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1099 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1100 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1101 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1102 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1103 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1104 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1105 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1106 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1107 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1108 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1109 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1110 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1111 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1112 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1113 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1114 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1115 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1116 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1117 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1118 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1119 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1120 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1121 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1122 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1123 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1124 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1125 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1126 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1127 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1128 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1129 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1130 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1131 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1132 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1133 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1134 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1135 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1136 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1137 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1138 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1139 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1140 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1141 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1142 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1143 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1144 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1145 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1146 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1147 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1148 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1149 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1150 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1151 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1152 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1153 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1154 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1155 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1156 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1157 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1158 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1159 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1160 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1161 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1162 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1163 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1164 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x1165 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x1166 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x1167 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x1168 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x1169 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x1170 = Var(within=Reals,bounds=(0,14500),initialize=0)
m.x1171 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x1172 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x1173 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x1174 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x1175 = Var(within=Reals,bounds=(0,7000),initialize=0)
m.x1176 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x1177 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x1178 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x1179 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x1180 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x1181 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x1182 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x1183 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x1184 = Var(within=Reals,bounds=(0,25000),initialize=0)
m.x1185 = Var(within=Reals,bounds=(0,40000),initialize=0)
m.x1186 = Var(within=Reals,bounds=(0,40000),initialize=0)
m.x1187 = Var(within=Reals,bounds=(0,40000),initialize=0)
m.x1188 = Var(within=Reals,bounds=(0,40000),initialize=0)
m.x1189 = Var(within=Reals,bounds=(0,40000),initialize=0)
m.x1190 = Var(within=Reals,bounds=(0,40000),initialize=0)
m.x1191 = Var(within=Reals,bounds=(0,40000),initialize=0)
m.x1192 = Var(within=Reals,bounds=(0,40000),initialize=0)
m.x1193 = Var(within=Reals,bounds=(0,40000),initialize=0)
m.x1194 = Var(within=Reals,bounds=(0,40000),initialize=0)
m.x1195 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x1196 = Var(within=Reals,bounds=(0,40000),initialize=0)
m.x1197 = Var(within=Reals,bounds=(0,40000),initialize=0)
m.x1198 = Var(within=Reals,bounds=(0,40000),initialize=0)
m.x1199 = Var(within=Reals,bounds=(0,40000),initialize=0)
m.x1200 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1201 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1202 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1203 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1204 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1205 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1206 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1207 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1208 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1209 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1210 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1211 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1212 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1213 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1214 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1215 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1216 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1217 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1218 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1219 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1220 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1221 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1222 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1223 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1224 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1225 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1226 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1227 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1228 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1229 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1230 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1231 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1232 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1233 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1234 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1235 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1236 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1237 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1238 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1239 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1240 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1241 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1242 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1243 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1244 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1245 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1246 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1247 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1248 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1249 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1250 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1251 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1252 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1253 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1254 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1255 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1256 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1257 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1258 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1259 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1260 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1261 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1262 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1263 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1264 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1265 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1266 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1267 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1268 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1269 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1270 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1271 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1272 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1273 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1274 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1275 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1276 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1277 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1278 = Var(within=Reals,bounds=(0.5,0.5),initialize=0.5)
m.x1279 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1280 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1281 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1282 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1283 = Var(within=Reals,bounds=(0.25,0.25),initialize=0.25)
m.x1284 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1285 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1286 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1287 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1288 = Var(within=Reals,bounds=(0.25,0.25),initialize=0.25)
m.x1289 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1290 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1291 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1292 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x1293 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1294 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1295 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1296 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x1297 = Var(within=Reals,bounds=(1,1),initialize=1)

m.obj = Objective(expr=   2130*m.x361 + 2130*m.x362 + 2130*m.x363 + 2130*m.x364 + 2130*m.x365 + 2574*m.x366
                        + 2574*m.x367 + 2574*m.x368 + 2574*m.x369 + 2574*m.x370 + 2418*m.x371 + 2418*m.x372
                        + 2418*m.x373 + 2418*m.x374 + 2418*m.x375 + 2130*m.x376 + 2130*m.x377 + 2130*m.x378
                        + 2130*m.x379 + 2130*m.x380 + 2130*m.x381 + 2130*m.x382 + 2130*m.x383 + 2130*m.x384
                        + 2130*m.x385 + 2574*m.x386 + 2574*m.x387 + 2574*m.x388 + 2574*m.x389 + 2574*m.x390
                        + 2150*m.x391 + 2150*m.x392 + 2150*m.x393 + 2150*m.x394 + 2150*m.x395 + 2671*m.x396
                        + 2671*m.x397 + 2671*m.x398 + 2671*m.x399 + 2671*m.x400 + 2418*m.x401 + 2418*m.x402
                        + 2418*m.x403 + 2418*m.x404 + 2418*m.x405 - 1130*m.x416 - 1130*m.x417 - 1130*m.x418
                        - 1130*m.x419 - 1130*m.x420 - 1130*m.x421 - 1130*m.x422 - 1130*m.x423 - 1130*m.x424
                        - 1130*m.x425 - 1130*m.x426 - 1130*m.x427 - 1130*m.x428 - 1130*m.x429 - 1130*m.x430
                        - 1130*m.x431 - 1130*m.x432 - 1130*m.x433 - 1130*m.x434 - 1130*m.x435 - 1130*m.x436
                        - 1130*m.x437 - 1130*m.x438 - 1130*m.x439 - 1130*m.x440 - 1130*m.x441 - 1130*m.x442
                        - 1130*m.x443 - 1130*m.x444 - 1130*m.x445 - 1130*m.x446 - 1130*m.x447 - 1130*m.x448
                        - 1130*m.x449 - 1130*m.x450 - 1130*m.x451 - 1130*m.x452 - 1130*m.x453 - 1130*m.x454
                        - 1130*m.x455 - 1130*m.x456 - 1130*m.x457 - 1130*m.x458 - 1130*m.x459 - 1130*m.x460
                        - 1130*m.x461 - 1130*m.x462 - 1130*m.x463 - 1130*m.x464 - 1130*m.x465 - 1130*m.x466
                        - 1130*m.x467 - 1130*m.x468 - 1130*m.x469 - 1130*m.x470 - 1130*m.x471 - 1130*m.x472
                        - 1130*m.x473 - 1130*m.x474 - 1130*m.x475 - 1130*m.x476 - 1130*m.x477 - 1130*m.x478
                        - 1130*m.x479 - 1130*m.x480 - 1130*m.x481 - 1130*m.x482 - 1130*m.x483 - 1130*m.x484
                        - 1130*m.x485 - 1130*m.x486 - 1130*m.x487 - 1130*m.x488 - 1130*m.x489 - 1130*m.x490
                        - 1130*m.x491 - 1130*m.x492 - 1130*m.x493 - 1130*m.x494 - 1130*m.x495 - 1130*m.x496
                        - 1130*m.x497 - 1130*m.x498 - 1130*m.x499 - 1130*m.x500 - 1130*m.x501 - 1130*m.x502
                        - 1130*m.x503 - 1130*m.x504 - 1130*m.x505 - 1130*m.x506 - 1130*m.x507 - 1130*m.x508
                        - 1130*m.x509 - 1130*m.x510 - 1130*m.x511 - 1130*m.x512 - 1130*m.x513 - 1130*m.x514
                        - 1130*m.x515 - 1130*m.x516 - 1130*m.x517 - 1130*m.x518 - 1130*m.x519 - 1130*m.x520
                        - 1130*m.x521 - 1130*m.x522 - 1130*m.x523 - 1130*m.x524 - 1130*m.x525 - 1130*m.x526
                        - 1130*m.x527 - 1130*m.x528 - 1130*m.x529 - 1130*m.x530 - 1130*m.x531 - 1130*m.x532
                        - 1130*m.x533 - 1130*m.x534 - 1130*m.x535 - 1130*m.x536 - 1130*m.x537 - 1130*m.x538
                        - 1130*m.x539 - 1130*m.x540 - 1130*m.x541 - 1130*m.x542 - 1130*m.x543 - 1130*m.x544
                        - 1130*m.x545 - 1130*m.x546 - 1130*m.x547 - 1130*m.x548 - 1130*m.x549 - 1130*m.x550
                        - 1574*m.x551 - 1574*m.x552 - 1574*m.x553 - 1574*m.x554 - 1574*m.x555 - 1574*m.x556
                        - 1574*m.x557 - 1574*m.x558 - 1574*m.x559 - 1574*m.x560 - 1671*m.x561 - 1671*m.x562
                        - 1671*m.x563 - 1671*m.x564 - 1671*m.x565 - 1574*m.x566 - 1574*m.x567 - 1574*m.x568
                        - 1574*m.x569 - 1574*m.x570 - 1574*m.x571 - 1574*m.x572 - 1574*m.x573 - 1574*m.x574
                        - 1574*m.x575 - 1150*m.x576 - 1150*m.x577 - 1150*m.x578 - 1150*m.x579 - 1150*m.x580
                        - 1130*m.x581 - 1130*m.x582 - 1130*m.x583 - 1130*m.x584 - 1130*m.x585 - 1130*m.x586
                        - 1130*m.x587 - 1130*m.x588 - 1130*m.x589 - 1130*m.x590 - 1130*m.x591 - 1130*m.x592
                        - 1130*m.x593 - 1130*m.x594 - 1130*m.x595 - 1130*m.x596 - 1130*m.x597 - 1130*m.x598
                        - 1130*m.x599 - 1130*m.x600 - 1130*m.x601 - 1130*m.x602 - 1130*m.x603 - 1130*m.x604
                        - 1130*m.x605 - 1130*m.x606 - 1130*m.x607 - 1130*m.x608 - 1130*m.x609 - 1130*m.x610
                        - 1150*m.x611 - 1150*m.x612 - 1150*m.x613 - 1150*m.x614 - 1150*m.x615 - 1622.5*m.x616
                        - 1622.5*m.x617 - 1622.5*m.x618 - 1622.5*m.x619 - 1622.5*m.x620 + 2000*m.x621 + 2000*m.x622
                        + 2000*m.x623 + 2000*m.x624 + 2000*m.x625 + 2000*m.x626 + 2000*m.x627 + 2000*m.x628
                        + 2000*m.x629 + 2000*m.x630 + 2000*m.x631 + 2000*m.x632 + 2000*m.x633 + 2000*m.x634
                        + 2000*m.x635 + 2000*m.x636 + 2000*m.x637 - 7000*m.x638 - 7000*m.x639 - 7000*m.x640
                        - 7000*m.x641 - 7000*m.x642 - 7000*m.x643 - 7000*m.x644 - 7000*m.x645 - 7000*m.x646
                        - 7000*m.x647 - 7000*m.x648 - 7000*m.x649 - 7000*m.x650 - 7000*m.x651 - 7000*m.x652
                        - 7000*m.x653 - 7000*m.x654 - 0.0583333333333333*m.x1165 - 0.0583333333333333*m.x1166
                        - 0.0583333333333333*m.x1167 - 0.0583333333333333*m.x1168 - 0.0583333333333333*m.x1169
                        - 0.0583333333333333*m.x1170 - 0.0583333333333333*m.x1171 - 0.0583333333333333*m.x1172
                        - 0.0583333333333333*m.x1173 - 0.0583333333333333*m.x1174 - 0.0583333333333333*m.x1175
                        - 0.0583333333333333*m.x1176 - 0.0583333333333333*m.x1177 - 0.0583333333333333*m.x1178
                        - 0.0583333333333333*m.x1179 - 0.0583333333333333*m.x1180 - 0.0583333333333333*m.x1181
                        - 0.0583333333333333*m.x1182 - 0.0583333333333333*m.x1183 - 0.0583333333333333*m.x1184
                        - 0.0583333333333333*m.x1185 - 0.0583333333333333*m.x1186 - 0.0583333333333333*m.x1187
                        - 0.0583333333333333*m.x1188 - 0.0583333333333333*m.x1189 - 0.0583333333333333*m.x1190
                        - 0.0583333333333333*m.x1191 - 0.0583333333333333*m.x1192 - 0.0583333333333333*m.x1193
                        - 0.0583333333333333*m.x1194 - 0.0583333333333333*m.x1195 - 0.0583333333333333*m.x1196
                        - 0.0583333333333333*m.x1197 - 0.0583333333333333*m.x1198 - 0.0583333333333333*m.x1199
                        - 1000*m.x1245 - 1000*m.x1246 - 1000*m.x1247 - 1000*m.x1248 - 1000*m.x1249 - 1000*m.x1250
                        - 1000*m.x1251 - 1000*m.x1252 + 251266.666666667, sense=maximize)

m.c1 = Constraint(expr=   m.b1 + m.b6 + m.b11 <= 1)

m.c2 = Constraint(expr=   m.b2 + m.b7 + m.b12 <= 1)

m.c3 = Constraint(expr=   m.b3 + m.b8 + m.b13 <= 1)

m.c4 = Constraint(expr=   m.b4 + m.b9 + m.b14 <= 1)

m.c5 = Constraint(expr=   m.b5 + m.b10 + m.b15 <= 1)

m.c6 = Constraint(expr=   m.b16 + m.b21 + m.b26 <= 1)

m.c7 = Constraint(expr=   m.b17 + m.b22 + m.b27 <= 1)

m.c8 = Constraint(expr=   m.b18 + m.b23 + m.b28 <= 1)

m.c9 = Constraint(expr=   m.b19 + m.b24 + m.b29 <= 1)

m.c10 = Constraint(expr=   m.b20 + m.b25 + m.b30 <= 1)

m.c11 = Constraint(expr=   m.b31 + m.b36 + m.b41 <= 1)

m.c12 = Constraint(expr=   m.b32 + m.b37 + m.b42 <= 1)

m.c13 = Constraint(expr=   m.b33 + m.b38 + m.b43 <= 1)

m.c14 = Constraint(expr=   m.b34 + m.b39 + m.b44 <= 1)

m.c15 = Constraint(expr=   m.b35 + m.b40 + m.b45 <= 1)

m.c16 = Constraint(expr=   m.b46 + m.b51 + m.b56 <= 1)

m.c17 = Constraint(expr=   m.b47 + m.b52 + m.b57 <= 1)

m.c18 = Constraint(expr=   m.b48 + m.b53 + m.b58 <= 1)

m.c19 = Constraint(expr=   m.b49 + m.b54 + m.b59 <= 1)

m.c20 = Constraint(expr=   m.b50 + m.b55 + m.b60 <= 1)

m.c21 = Constraint(expr=   m.b61 + m.b66 + m.b71 <= 1)

m.c22 = Constraint(expr=   m.b62 + m.b67 + m.b72 <= 1)

m.c23 = Constraint(expr=   m.b63 + m.b68 + m.b73 <= 1)

m.c24 = Constraint(expr=   m.b64 + m.b69 + m.b74 <= 1)

m.c25 = Constraint(expr=   m.b65 + m.b70 + m.b75 <= 1)

m.c26 = Constraint(expr=   m.b76 + m.b81 + m.b86 <= 1)

m.c27 = Constraint(expr=   m.b77 + m.b82 + m.b87 <= 1)

m.c28 = Constraint(expr=   m.b78 + m.b83 + m.b88 <= 1)

m.c29 = Constraint(expr=   m.b79 + m.b84 + m.b89 <= 1)

m.c30 = Constraint(expr=   m.b80 + m.b85 + m.b90 <= 1)

m.c31 = Constraint(expr=   m.b91 + m.b96 + m.b101 <= 1)

m.c32 = Constraint(expr=   m.b92 + m.b97 + m.b102 <= 1)

m.c33 = Constraint(expr=   m.b93 + m.b98 + m.b103 <= 1)

m.c34 = Constraint(expr=   m.b94 + m.b99 + m.b104 <= 1)

m.c35 = Constraint(expr=   m.b95 + m.b100 + m.b105 <= 1)

m.c36 = Constraint(expr=   m.b106 + m.b111 + m.b116 <= 1)

m.c37 = Constraint(expr=   m.b107 + m.b112 + m.b117 <= 1)

m.c38 = Constraint(expr=   m.b108 + m.b113 + m.b118 <= 1)

m.c39 = Constraint(expr=   m.b109 + m.b114 + m.b119 <= 1)

m.c40 = Constraint(expr=   m.b110 + m.b115 + m.b120 <= 1)

m.c41 = Constraint(expr=   m.b121 + m.b126 + m.b131 <= 1)

m.c42 = Constraint(expr=   m.b122 + m.b127 + m.b132 <= 1)

m.c43 = Constraint(expr=   m.b123 + m.b128 + m.b133 <= 1)

m.c44 = Constraint(expr=   m.b124 + m.b129 + m.b134 <= 1)

m.c45 = Constraint(expr=   m.b125 + m.b130 + m.b135 <= 1)

m.c46 = Constraint(expr=   m.b136 + m.b141 <= 1)

m.c47 = Constraint(expr=   m.b137 + m.b142 <= 1)

m.c48 = Constraint(expr=   m.b138 + m.b143 <= 1)

m.c49 = Constraint(expr=   m.b139 + m.b144 <= 1)

m.c50 = Constraint(expr=   m.b140 + m.b145 <= 1)

m.c51 = Constraint(expr=   m.b146 <= 1)

m.c52 = Constraint(expr=   m.b147 <= 1)

m.c53 = Constraint(expr=   m.b148 <= 1)

m.c54 = Constraint(expr=   m.b149 <= 1)

m.c55 = Constraint(expr=   m.b150 <= 1)

m.c56 = Constraint(expr=   m.b151 + m.b156 <= 1)

m.c57 = Constraint(expr=   m.b152 + m.b157 <= 1)

m.c58 = Constraint(expr=   m.b153 + m.b158 <= 1)

m.c59 = Constraint(expr=   m.b154 + m.b159 <= 1)

m.c60 = Constraint(expr=   m.b155 + m.b160 <= 1)

m.c61 = Constraint(expr=   m.b161 <= 1)

m.c62 = Constraint(expr=   m.b162 <= 1)

m.c63 = Constraint(expr=   m.b163 <= 1)

m.c64 = Constraint(expr=   m.b164 <= 1)

m.c65 = Constraint(expr=   m.b165 <= 1)

m.c66 = Constraint(expr=   m.b166 + m.b171 + m.b176 <= 1)

m.c67 = Constraint(expr=   m.b167 + m.b172 + m.b177 <= 1)

m.c68 = Constraint(expr=   m.b168 + m.b173 + m.b178 <= 1)

m.c69 = Constraint(expr=   m.b169 + m.b174 + m.b179 <= 1)

m.c70 = Constraint(expr=   m.b170 + m.b175 + m.b180 <= 1)

m.c71 = Constraint(expr=   m.b181 + m.b186 + m.b191 <= 1)

m.c72 = Constraint(expr=   m.b182 + m.b187 + m.b192 <= 1)

m.c73 = Constraint(expr=   m.b183 + m.b188 + m.b193 <= 1)

m.c74 = Constraint(expr=   m.b184 + m.b189 + m.b194 <= 1)

m.c75 = Constraint(expr=   m.b185 + m.b190 + m.b195 <= 1)

m.c76 = Constraint(expr=   m.b196 <= 1)

m.c77 = Constraint(expr=   m.b197 <= 1)

m.c78 = Constraint(expr=   m.b198 <= 1)

m.c79 = Constraint(expr=   m.b199 <= 1)

m.c80 = Constraint(expr=   m.b200 <= 1)

m.c81 = Constraint(expr=   m.b201 <= 1)

m.c82 = Constraint(expr=   m.b202 <= 1)

m.c83 = Constraint(expr=   m.b203 <= 1)

m.c84 = Constraint(expr=   m.b204 <= 1)

m.c85 = Constraint(expr=   m.b205 <= 1)

m.c86 = Constraint(expr=   m.b1 + m.b6 + m.b11 + m.b16 + m.b21 + m.b26 + m.b31 + m.b36 + m.b41 + m.b46 + m.b51 + m.b56
                         + m.b61 + m.b66 + m.b71 + m.b76 + m.b81 + m.b86 + m.b91 + m.b96 + m.b101 + m.b106 + m.b111
                         + m.b116 + m.b121 + m.b126 + m.b131 + m.b136 + m.b141 + m.b146 + m.b151 + m.b156 + m.b161
                         + m.b166 + m.b171 + m.b176 + m.b181 + m.b186 + m.b191 + m.b196 + m.b201 <= 4)

m.c87 = Constraint(expr=   m.b2 + m.b7 + m.b12 + m.b17 + m.b22 + m.b27 + m.b32 + m.b37 + m.b42 + m.b47 + m.b52 + m.b57
                         + m.b62 + m.b67 + m.b72 + m.b77 + m.b82 + m.b87 + m.b92 + m.b97 + m.b102 + m.b107 + m.b112
                         + m.b117 + m.b122 + m.b127 + m.b132 + m.b137 + m.b142 + m.b147 + m.b152 + m.b157 + m.b162
                         + m.b167 + m.b172 + m.b177 + m.b182 + m.b187 + m.b192 + m.b197 + m.b202 <= 4)

m.c88 = Constraint(expr=   m.b3 + m.b8 + m.b13 + m.b18 + m.b23 + m.b28 + m.b33 + m.b38 + m.b43 + m.b48 + m.b53 + m.b58
                         + m.b63 + m.b68 + m.b73 + m.b78 + m.b83 + m.b88 + m.b93 + m.b98 + m.b103 + m.b108 + m.b113
                         + m.b118 + m.b123 + m.b128 + m.b133 + m.b138 + m.b143 + m.b148 + m.b153 + m.b158 + m.b163
                         + m.b168 + m.b173 + m.b178 + m.b183 + m.b188 + m.b193 + m.b198 + m.b203 <= 4)

m.c89 = Constraint(expr=   m.b4 + m.b9 + m.b14 + m.b19 + m.b24 + m.b29 + m.b34 + m.b39 + m.b44 + m.b49 + m.b54 + m.b59
                         + m.b64 + m.b69 + m.b74 + m.b79 + m.b84 + m.b89 + m.b94 + m.b99 + m.b104 + m.b109 + m.b114
                         + m.b119 + m.b124 + m.b129 + m.b134 + m.b139 + m.b144 + m.b149 + m.b154 + m.b159 + m.b164
                         + m.b169 + m.b174 + m.b179 + m.b184 + m.b189 + m.b194 + m.b199 + m.b204 <= 4)

m.c90 = Constraint(expr=   m.b5 + m.b10 + m.b15 + m.b20 + m.b25 + m.b30 + m.b35 + m.b40 + m.b45 + m.b50 + m.b55 + m.b60
                         + m.b65 + m.b70 + m.b75 + m.b80 + m.b85 + m.b90 + m.b95 + m.b100 + m.b105 + m.b110 + m.b115
                         + m.b120 + m.b125 + m.b130 + m.b135 + m.b140 + m.b145 + m.b150 + m.b155 + m.b160 + m.b165
                         + m.b170 + m.b175 + m.b180 + m.b185 + m.b190 + m.b195 + m.b200 + m.b205 <= 4)

m.c91 = Constraint(expr=   m.b1 + m.b2 + m.b6 + m.b7 + m.b11 + m.b12 + m.x206 <= 2)

m.c92 = Constraint(expr=   m.b2 + m.b3 + m.b7 + m.b8 + m.b12 + m.b13 + m.x207 <= 2)

m.c93 = Constraint(expr=   m.b3 + m.b4 + m.b8 + m.b9 + m.b13 + m.b14 + m.x208 <= 2)

m.c94 = Constraint(expr=   m.b4 + m.b5 + m.b9 + m.b10 + m.b14 + m.b15 + m.x209 <= 2)

m.c95 = Constraint(expr=   m.b16 + m.b17 + m.b21 + m.b22 + m.b26 + m.b27 + m.x211 <= 2)

m.c96 = Constraint(expr=   m.b17 + m.b18 + m.b22 + m.b23 + m.b27 + m.b28 + m.x212 <= 2)

m.c97 = Constraint(expr=   m.b18 + m.b19 + m.b23 + m.b24 + m.b28 + m.b29 + m.x213 <= 2)

m.c98 = Constraint(expr=   m.b19 + m.b20 + m.b24 + m.b25 + m.b29 + m.b30 + m.x214 <= 2)

m.c99 = Constraint(expr=   m.b31 + m.b32 + m.b36 + m.b37 + m.b41 + m.b42 + m.x216 <= 2)

m.c100 = Constraint(expr=   m.b32 + m.b33 + m.b37 + m.b38 + m.b42 + m.b43 + m.x217 <= 2)

m.c101 = Constraint(expr=   m.b33 + m.b34 + m.b38 + m.b39 + m.b43 + m.b44 + m.x218 <= 2)

m.c102 = Constraint(expr=   m.b34 + m.b35 + m.b39 + m.b40 + m.b44 + m.b45 + m.x219 <= 2)

m.c103 = Constraint(expr=   m.b46 + m.b47 + m.b51 + m.b52 + m.b56 + m.b57 + m.x221 <= 2)

m.c104 = Constraint(expr=   m.b47 + m.b48 + m.b52 + m.b53 + m.b57 + m.b58 + m.x222 <= 2)

m.c105 = Constraint(expr=   m.b48 + m.b49 + m.b53 + m.b54 + m.b58 + m.b59 + m.x223 <= 2)

m.c106 = Constraint(expr=   m.b49 + m.b50 + m.b54 + m.b55 + m.b59 + m.b60 + m.x224 <= 2)

m.c107 = Constraint(expr=   m.b61 + m.b62 + m.b66 + m.b67 + m.b71 + m.b72 + m.x226 <= 2)

m.c108 = Constraint(expr=   m.b62 + m.b63 + m.b67 + m.b68 + m.b72 + m.b73 + m.x227 <= 2)

m.c109 = Constraint(expr=   m.b63 + m.b64 + m.b68 + m.b69 + m.b73 + m.b74 + m.x228 <= 2)

m.c110 = Constraint(expr=   m.b64 + m.b65 + m.b69 + m.b70 + m.b74 + m.b75 + m.x229 <= 2)

m.c111 = Constraint(expr=   m.b76 + m.b77 + m.b81 + m.b82 + m.b86 + m.b87 + m.x231 <= 2)

m.c112 = Constraint(expr=   m.b77 + m.b78 + m.b82 + m.b83 + m.b87 + m.b88 + m.x232 <= 2)

m.c113 = Constraint(expr=   m.b78 + m.b79 + m.b83 + m.b84 + m.b88 + m.b89 + m.x233 <= 2)

m.c114 = Constraint(expr=   m.b79 + m.b80 + m.b84 + m.b85 + m.b89 + m.b90 + m.x234 <= 2)

m.c115 = Constraint(expr=   m.b91 + m.b92 + m.b96 + m.b97 + m.b101 + m.b102 + m.x236 <= 2)

m.c116 = Constraint(expr=   m.b92 + m.b93 + m.b97 + m.b98 + m.b102 + m.b103 + m.x237 <= 2)

m.c117 = Constraint(expr=   m.b93 + m.b94 + m.b98 + m.b99 + m.b103 + m.b104 + m.x238 <= 2)

m.c118 = Constraint(expr=   m.b94 + m.b95 + m.b99 + m.b100 + m.b104 + m.b105 + m.x239 <= 2)

m.c119 = Constraint(expr=   m.b106 + m.b107 + m.b111 + m.b112 + m.b116 + m.b117 + m.x241 <= 2)

m.c120 = Constraint(expr=   m.b107 + m.b108 + m.b112 + m.b113 + m.b117 + m.b118 + m.x242 <= 2)

m.c121 = Constraint(expr=   m.b108 + m.b109 + m.b113 + m.b114 + m.b118 + m.b119 + m.x243 <= 2)

m.c122 = Constraint(expr=   m.b109 + m.b110 + m.b114 + m.b115 + m.b119 + m.b120 + m.x244 <= 2)

m.c123 = Constraint(expr=   m.b121 + m.b122 + m.b126 + m.b127 + m.b131 + m.b132 + m.x246 <= 2)

m.c124 = Constraint(expr=   m.b122 + m.b123 + m.b127 + m.b128 + m.b132 + m.b133 + m.x247 <= 2)

m.c125 = Constraint(expr=   m.b123 + m.b124 + m.b128 + m.b129 + m.b133 + m.b134 + m.x248 <= 2)

m.c126 = Constraint(expr=   m.b124 + m.b125 + m.b129 + m.b130 + m.b134 + m.b135 + m.x249 <= 2)

m.c127 = Constraint(expr=   m.b136 + m.b137 + m.b141 + m.b142 + m.x251 <= 2)

m.c128 = Constraint(expr=   m.b137 + m.b138 + m.b142 + m.b143 + m.x252 <= 2)

m.c129 = Constraint(expr=   m.b138 + m.b139 + m.b143 + m.b144 + m.x253 <= 2)

m.c130 = Constraint(expr=   m.b139 + m.b140 + m.b144 + m.b145 + m.x254 <= 2)

m.c131 = Constraint(expr=   m.b146 + m.b147 + m.x256 <= 2)

m.c132 = Constraint(expr=   m.b147 + m.b148 + m.x257 <= 2)

m.c133 = Constraint(expr=   m.b148 + m.b149 + m.x258 <= 2)

m.c134 = Constraint(expr=   m.b149 + m.b150 + m.x259 <= 2)

m.c135 = Constraint(expr=   m.b151 + m.b152 + m.b156 + m.b157 + m.x261 <= 2)

m.c136 = Constraint(expr=   m.b152 + m.b153 + m.b157 + m.b158 + m.x262 <= 2)

m.c137 = Constraint(expr=   m.b153 + m.b154 + m.b158 + m.b159 + m.x263 <= 2)

m.c138 = Constraint(expr=   m.b154 + m.b155 + m.b159 + m.b160 + m.x264 <= 2)

m.c139 = Constraint(expr=   m.b161 + m.b162 + m.x266 <= 2)

m.c140 = Constraint(expr=   m.b162 + m.b163 + m.x267 <= 2)

m.c141 = Constraint(expr=   m.b163 + m.b164 + m.x268 <= 2)

m.c142 = Constraint(expr=   m.b164 + m.b165 + m.x269 <= 2)

m.c143 = Constraint(expr=   m.b166 + m.b167 + m.b171 + m.b172 + m.b176 + m.b177 + m.x271 <= 2)

m.c144 = Constraint(expr=   m.b167 + m.b168 + m.b172 + m.b173 + m.b177 + m.b178 + m.x272 <= 2)

m.c145 = Constraint(expr=   m.b168 + m.b169 + m.b173 + m.b174 + m.b178 + m.b179 + m.x273 <= 2)

m.c146 = Constraint(expr=   m.b169 + m.b170 + m.b174 + m.b175 + m.b179 + m.b180 + m.x274 <= 2)

m.c147 = Constraint(expr=   m.b181 + m.b182 + m.b186 + m.b187 + m.b191 + m.b192 + m.x276 <= 2)

m.c148 = Constraint(expr=   m.b182 + m.b183 + m.b187 + m.b188 + m.b192 + m.b193 + m.x277 <= 2)

m.c149 = Constraint(expr=   m.b183 + m.b184 + m.b188 + m.b189 + m.b193 + m.b194 + m.x278 <= 2)

m.c150 = Constraint(expr=   m.b184 + m.b185 + m.b189 + m.b190 + m.b194 + m.b195 + m.x279 <= 2)

m.c151 = Constraint(expr=   m.b196 + m.b197 + m.x281 <= 2)

m.c152 = Constraint(expr=   m.b197 + m.b198 + m.x282 <= 2)

m.c153 = Constraint(expr=   m.b198 + m.b199 + m.x283 <= 2)

m.c154 = Constraint(expr=   m.b199 + m.b200 + m.x284 <= 2)

m.c155 = Constraint(expr=   m.b201 + m.b202 + m.x286 <= 2)

m.c156 = Constraint(expr=   m.b202 + m.b203 + m.x287 <= 2)

m.c157 = Constraint(expr=   m.b203 + m.b204 + m.x288 <= 2)

m.c158 = Constraint(expr=   m.b204 + m.b205 + m.x289 <= 2)

m.c159 = Constraint(expr= - m.b1 + m.b2 - m.b6 + m.b7 - m.b11 + m.b12 + m.x206 >= 0)

m.c160 = Constraint(expr= - m.b2 + m.b3 - m.b7 + m.b8 - m.b12 + m.b13 + m.x207 >= 0)

m.c161 = Constraint(expr= - m.b3 + m.b4 - m.b8 + m.b9 - m.b13 + m.b14 + m.x208 >= 0)

m.c162 = Constraint(expr= - m.b4 + m.b5 - m.b9 + m.b10 - m.b14 + m.b15 + m.x209 >= 0)

m.c163 = Constraint(expr= - m.b16 + m.b17 - m.b21 + m.b22 - m.b26 + m.b27 + m.x211 >= 0)

m.c164 = Constraint(expr= - m.b17 + m.b18 - m.b22 + m.b23 - m.b27 + m.b28 + m.x212 >= 0)

m.c165 = Constraint(expr= - m.b18 + m.b19 - m.b23 + m.b24 - m.b28 + m.b29 + m.x213 >= 0)

m.c166 = Constraint(expr= - m.b19 + m.b20 - m.b24 + m.b25 - m.b29 + m.b30 + m.x214 >= 0)

m.c167 = Constraint(expr= - m.b31 + m.b32 - m.b36 + m.b37 - m.b41 + m.b42 + m.x216 >= 0)

m.c168 = Constraint(expr= - m.b32 + m.b33 - m.b37 + m.b38 - m.b42 + m.b43 + m.x217 >= 0)

m.c169 = Constraint(expr= - m.b33 + m.b34 - m.b38 + m.b39 - m.b43 + m.b44 + m.x218 >= 0)

m.c170 = Constraint(expr= - m.b34 + m.b35 - m.b39 + m.b40 - m.b44 + m.b45 + m.x219 >= 0)

m.c171 = Constraint(expr= - m.b46 + m.b47 - m.b51 + m.b52 - m.b56 + m.b57 + m.x221 >= 0)

m.c172 = Constraint(expr= - m.b47 + m.b48 - m.b52 + m.b53 - m.b57 + m.b58 + m.x222 >= 0)

m.c173 = Constraint(expr= - m.b48 + m.b49 - m.b53 + m.b54 - m.b58 + m.b59 + m.x223 >= 0)

m.c174 = Constraint(expr= - m.b49 + m.b50 - m.b54 + m.b55 - m.b59 + m.b60 + m.x224 >= 0)

m.c175 = Constraint(expr= - m.b61 + m.b62 - m.b66 + m.b67 - m.b71 + m.b72 + m.x226 >= 0)

m.c176 = Constraint(expr= - m.b62 + m.b63 - m.b67 + m.b68 - m.b72 + m.b73 + m.x227 >= 0)

m.c177 = Constraint(expr= - m.b63 + m.b64 - m.b68 + m.b69 - m.b73 + m.b74 + m.x228 >= 0)

m.c178 = Constraint(expr= - m.b64 + m.b65 - m.b69 + m.b70 - m.b74 + m.b75 + m.x229 >= 0)

m.c179 = Constraint(expr= - m.b76 + m.b77 - m.b81 + m.b82 - m.b86 + m.b87 + m.x231 >= 0)

m.c180 = Constraint(expr= - m.b77 + m.b78 - m.b82 + m.b83 - m.b87 + m.b88 + m.x232 >= 0)

m.c181 = Constraint(expr= - m.b78 + m.b79 - m.b83 + m.b84 - m.b88 + m.b89 + m.x233 >= 0)

m.c182 = Constraint(expr= - m.b79 + m.b80 - m.b84 + m.b85 - m.b89 + m.b90 + m.x234 >= 0)

m.c183 = Constraint(expr= - m.b91 + m.b92 - m.b96 + m.b97 - m.b101 + m.b102 + m.x236 >= 0)

m.c184 = Constraint(expr= - m.b92 + m.b93 - m.b97 + m.b98 - m.b102 + m.b103 + m.x237 >= 0)

m.c185 = Constraint(expr= - m.b93 + m.b94 - m.b98 + m.b99 - m.b103 + m.b104 + m.x238 >= 0)

m.c186 = Constraint(expr= - m.b94 + m.b95 - m.b99 + m.b100 - m.b104 + m.b105 + m.x239 >= 0)

m.c187 = Constraint(expr= - m.b106 + m.b107 - m.b111 + m.b112 - m.b116 + m.b117 + m.x241 >= 0)

m.c188 = Constraint(expr= - m.b107 + m.b108 - m.b112 + m.b113 - m.b117 + m.b118 + m.x242 >= 0)

m.c189 = Constraint(expr= - m.b108 + m.b109 - m.b113 + m.b114 - m.b118 + m.b119 + m.x243 >= 0)

m.c190 = Constraint(expr= - m.b109 + m.b110 - m.b114 + m.b115 - m.b119 + m.b120 + m.x244 >= 0)

m.c191 = Constraint(expr= - m.b121 + m.b122 - m.b126 + m.b127 - m.b131 + m.b132 + m.x246 >= 0)

m.c192 = Constraint(expr= - m.b122 + m.b123 - m.b127 + m.b128 - m.b132 + m.b133 + m.x247 >= 0)

m.c193 = Constraint(expr= - m.b123 + m.b124 - m.b128 + m.b129 - m.b133 + m.b134 + m.x248 >= 0)

m.c194 = Constraint(expr= - m.b124 + m.b125 - m.b129 + m.b130 - m.b134 + m.b135 + m.x249 >= 0)

m.c195 = Constraint(expr= - m.b136 + m.b137 - m.b141 + m.b142 + m.x251 >= 0)

m.c196 = Constraint(expr= - m.b137 + m.b138 - m.b142 + m.b143 + m.x252 >= 0)

m.c197 = Constraint(expr= - m.b138 + m.b139 - m.b143 + m.b144 + m.x253 >= 0)

m.c198 = Constraint(expr= - m.b139 + m.b140 - m.b144 + m.b145 + m.x254 >= 0)

m.c199 = Constraint(expr= - m.b146 + m.b147 + m.x256 >= 0)

m.c200 = Constraint(expr= - m.b147 + m.b148 + m.x257 >= 0)

m.c201 = Constraint(expr= - m.b148 + m.b149 + m.x258 >= 0)

m.c202 = Constraint(expr= - m.b149 + m.b150 + m.x259 >= 0)

m.c203 = Constraint(expr= - m.b151 + m.b152 - m.b156 + m.b157 + m.x261 >= 0)

m.c204 = Constraint(expr= - m.b152 + m.b153 - m.b157 + m.b158 + m.x262 >= 0)

m.c205 = Constraint(expr= - m.b153 + m.b154 - m.b158 + m.b159 + m.x263 >= 0)

m.c206 = Constraint(expr= - m.b154 + m.b155 - m.b159 + m.b160 + m.x264 >= 0)

m.c207 = Constraint(expr= - m.b161 + m.b162 + m.x266 >= 0)

m.c208 = Constraint(expr= - m.b162 + m.b163 + m.x267 >= 0)

m.c209 = Constraint(expr= - m.b163 + m.b164 + m.x268 >= 0)

m.c210 = Constraint(expr= - m.b164 + m.b165 + m.x269 >= 0)

m.c211 = Constraint(expr= - m.b166 + m.b167 - m.b171 + m.b172 - m.b176 + m.b177 + m.x271 >= 0)

m.c212 = Constraint(expr= - m.b167 + m.b168 - m.b172 + m.b173 - m.b177 + m.b178 + m.x272 >= 0)

m.c213 = Constraint(expr= - m.b168 + m.b169 - m.b173 + m.b174 - m.b178 + m.b179 + m.x273 >= 0)

m.c214 = Constraint(expr= - m.b169 + m.b170 - m.b174 + m.b175 - m.b179 + m.b180 + m.x274 >= 0)

m.c215 = Constraint(expr= - m.b181 + m.b182 - m.b186 + m.b187 - m.b191 + m.b192 + m.x276 >= 0)

m.c216 = Constraint(expr= - m.b182 + m.b183 - m.b187 + m.b188 - m.b192 + m.b193 + m.x277 >= 0)

m.c217 = Constraint(expr= - m.b183 + m.b184 - m.b188 + m.b189 - m.b193 + m.b194 + m.x278 >= 0)

m.c218 = Constraint(expr= - m.b184 + m.b185 - m.b189 + m.b190 - m.b194 + m.b195 + m.x279 >= 0)

m.c219 = Constraint(expr= - m.b196 + m.b197 + m.x281 >= 0)

m.c220 = Constraint(expr= - m.b197 + m.b198 + m.x282 >= 0)

m.c221 = Constraint(expr= - m.b198 + m.b199 + m.x283 >= 0)

m.c222 = Constraint(expr= - m.b199 + m.b200 + m.x284 >= 0)

m.c223 = Constraint(expr= - m.b201 + m.b202 + m.x286 >= 0)

m.c224 = Constraint(expr= - m.b202 + m.b203 + m.x287 >= 0)

m.c225 = Constraint(expr= - m.b203 + m.b204 + m.x288 >= 0)

m.c226 = Constraint(expr= - m.b204 + m.b205 + m.x289 >= 0)

m.c227 = Constraint(expr= - m.b5 - m.b10 - m.b15 + m.x210 >= 0)

m.c228 = Constraint(expr= - m.b20 - m.b25 - m.b30 + m.x215 >= 0)

m.c229 = Constraint(expr= - m.b35 - m.b40 - m.b45 + m.x220 >= 0)

m.c230 = Constraint(expr= - m.b50 - m.b55 - m.b60 + m.x225 >= 0)

m.c231 = Constraint(expr= - m.b65 - m.b70 - m.b75 + m.x230 >= 0)

m.c232 = Constraint(expr= - m.b80 - m.b85 - m.b90 + m.x235 >= 0)

m.c233 = Constraint(expr= - m.b95 - m.b100 - m.b105 + m.x240 >= 0)

m.c234 = Constraint(expr= - m.b110 - m.b115 - m.b120 + m.x245 >= 0)

m.c235 = Constraint(expr= - m.b125 - m.b130 - m.b135 + m.x250 >= 0)

m.c236 = Constraint(expr= - m.b140 - m.b145 + m.x255 >= 0)

m.c237 = Constraint(expr= - m.b150 + m.x260 >= 0)

m.c238 = Constraint(expr= - m.b155 - m.b160 + m.x265 >= 0)

m.c239 = Constraint(expr= - m.b165 + m.x270 >= 0)

m.c240 = Constraint(expr= - m.b170 - m.b175 - m.b180 + m.x275 >= 0)

m.c241 = Constraint(expr= - m.b185 - m.b190 - m.b195 + m.x280 >= 0)

m.c242 = Constraint(expr= - m.b200 + m.x285 >= 0)

m.c243 = Constraint(expr= - m.b205 + m.x290 >= 0)

m.c244 = Constraint(expr=   m.x206 + m.x207 + m.x208 + m.x209 + m.x210 == 1)

m.c245 = Constraint(expr=   m.x211 + m.x212 + m.x213 + m.x214 + m.x215 == 1)

m.c246 = Constraint(expr=   m.x216 + m.x217 + m.x218 + m.x219 + m.x220 == 1)

m.c247 = Constraint(expr=   m.x221 + m.x222 + m.x223 + m.x224 + m.x225 == 1)

m.c248 = Constraint(expr=   m.x226 + m.x227 + m.x228 + m.x229 + m.x230 == 1)

m.c249 = Constraint(expr=   m.x231 + m.x232 + m.x233 + m.x234 + m.x235 == 1)

m.c250 = Constraint(expr=   m.x236 + m.x237 + m.x238 + m.x239 + m.x240 == 1)

m.c251 = Constraint(expr=   m.x241 + m.x242 + m.x243 + m.x244 + m.x245 == 1)

m.c252 = Constraint(expr=   m.x246 + m.x247 + m.x248 + m.x249 + m.x250 == 1)

m.c253 = Constraint(expr=   m.x251 + m.x252 + m.x253 + m.x254 + m.x255 == 1)

m.c254 = Constraint(expr=   m.x256 + m.x257 + m.x258 + m.x259 + m.x260 == 1)

m.c255 = Constraint(expr=   m.x261 + m.x262 + m.x263 + m.x264 + m.x265 == 1)

m.c256 = Constraint(expr=   m.x266 + m.x267 + m.x268 + m.x269 + m.x270 == 1)

m.c257 = Constraint(expr=   m.x271 + m.x272 + m.x273 + m.x274 + m.x275 == 1)

m.c258 = Constraint(expr=   m.x276 + m.x277 + m.x278 + m.x279 + m.x280 == 1)

m.c259 = Constraint(expr=   m.x281 + m.x282 + m.x283 + m.x284 + m.x285 == 1)

m.c260 = Constraint(expr=   m.x286 + m.x287 + m.x288 + m.x289 + m.x290 == 1)

m.c261 = Constraint(expr=   m.x416 + 5000*m.x655 - 5000*m.x860 <= 0)

m.c262 = Constraint(expr=   m.x417 + 5000*m.x656 - 5000*m.x861 <= 0)

m.c263 = Constraint(expr=   m.x418 + 5000*m.x657 - 5000*m.x862 <= 0)

m.c264 = Constraint(expr=   m.x419 + 5000*m.x658 - 5000*m.x863 <= 0)

m.c265 = Constraint(expr=   m.x420 + 5000*m.x659 - 5000*m.x864 <= 0)

m.c266 = Constraint(expr=   m.x421 + 5000*m.x660 - 5000*m.x865 <= 0)

m.c267 = Constraint(expr=   m.x422 + 5000*m.x661 - 5000*m.x866 <= 0)

m.c268 = Constraint(expr=   m.x423 + 5000*m.x662 - 5000*m.x867 <= 0)

m.c269 = Constraint(expr=   m.x424 + 5000*m.x663 - 5000*m.x868 <= 0)

m.c270 = Constraint(expr=   m.x425 + 5000*m.x664 - 5000*m.x869 <= 0)

m.c271 = Constraint(expr=   m.x426 + 5000*m.x665 - 5000*m.x870 <= 0)

m.c272 = Constraint(expr=   m.x427 + 5000*m.x666 - 5000*m.x871 <= 0)

m.c273 = Constraint(expr=   m.x428 + 5000*m.x667 - 5000*m.x872 <= 0)

m.c274 = Constraint(expr=   m.x429 + 5000*m.x668 - 5000*m.x873 <= 0)

m.c275 = Constraint(expr=   m.x430 + 5000*m.x669 - 5000*m.x874 <= 0)

m.c276 = Constraint(expr=   m.x431 + 5000*m.x670 - 5000*m.x875 <= 0)

m.c277 = Constraint(expr=   m.x432 + 5000*m.x671 - 5000*m.x876 <= 0)

m.c278 = Constraint(expr=   m.x433 + 5000*m.x672 - 5000*m.x877 <= 0)

m.c279 = Constraint(expr=   m.x434 + 5000*m.x673 - 5000*m.x878 <= 0)

m.c280 = Constraint(expr=   m.x435 + 5000*m.x674 - 5000*m.x879 <= 0)

m.c281 = Constraint(expr=   m.x436 + 5000*m.x675 - 5000*m.x880 <= 0)

m.c282 = Constraint(expr=   m.x437 + 5000*m.x676 - 5000*m.x881 <= 0)

m.c283 = Constraint(expr=   m.x438 + 5000*m.x677 - 5000*m.x882 <= 0)

m.c284 = Constraint(expr=   m.x439 + 5000*m.x678 - 5000*m.x883 <= 0)

m.c285 = Constraint(expr=   m.x440 + 5000*m.x679 - 5000*m.x884 <= 0)

m.c286 = Constraint(expr=   m.x441 + 5000*m.x680 - 5000*m.x885 <= 0)

m.c287 = Constraint(expr=   m.x442 + 5000*m.x681 - 5000*m.x886 <= 0)

m.c288 = Constraint(expr=   m.x443 + 5000*m.x682 - 5000*m.x887 <= 0)

m.c289 = Constraint(expr=   m.x444 + 5000*m.x683 - 5000*m.x888 <= 0)

m.c290 = Constraint(expr=   m.x445 + 5000*m.x684 - 5000*m.x889 <= 0)

m.c291 = Constraint(expr=   m.x446 + 5000*m.x685 - 5000*m.x890 <= 0)

m.c292 = Constraint(expr=   m.x447 + 5000*m.x686 - 5000*m.x891 <= 0)

m.c293 = Constraint(expr=   m.x448 + 5000*m.x687 - 5000*m.x892 <= 0)

m.c294 = Constraint(expr=   m.x449 + 5000*m.x688 - 5000*m.x893 <= 0)

m.c295 = Constraint(expr=   m.x450 + 5000*m.x689 - 5000*m.x894 <= 0)

m.c296 = Constraint(expr=   m.x451 + 5000*m.x690 - 5000*m.x895 <= 0)

m.c297 = Constraint(expr=   m.x452 + 5000*m.x691 - 5000*m.x896 <= 0)

m.c298 = Constraint(expr=   m.x453 + 5000*m.x692 - 5000*m.x897 <= 0)

m.c299 = Constraint(expr=   m.x454 + 5000*m.x693 - 5000*m.x898 <= 0)

m.c300 = Constraint(expr=   m.x455 + 5000*m.x694 - 5000*m.x899 <= 0)

m.c301 = Constraint(expr=   m.x456 + 5000*m.x695 - 5000*m.x900 <= 0)

m.c302 = Constraint(expr=   m.x457 + 5000*m.x696 - 5000*m.x901 <= 0)

m.c303 = Constraint(expr=   m.x458 + 5000*m.x697 - 5000*m.x902 <= 0)

m.c304 = Constraint(expr=   m.x459 + 5000*m.x698 - 5000*m.x903 <= 0)

m.c305 = Constraint(expr=   m.x460 + 5000*m.x699 - 5000*m.x904 <= 0)

m.c306 = Constraint(expr=   m.x461 + 5000*m.x700 - 5000*m.x905 <= 0)

m.c307 = Constraint(expr=   m.x462 + 5000*m.x701 - 5000*m.x906 <= 0)

m.c308 = Constraint(expr=   m.x463 + 5000*m.x702 - 5000*m.x907 <= 0)

m.c309 = Constraint(expr=   m.x464 + 5000*m.x703 - 5000*m.x908 <= 0)

m.c310 = Constraint(expr=   m.x465 + 5000*m.x704 - 5000*m.x909 <= 0)

m.c311 = Constraint(expr=   m.x466 + 5000*m.x705 - 5000*m.x910 <= 0)

m.c312 = Constraint(expr=   m.x467 + 5000*m.x706 - 5000*m.x911 <= 0)

m.c313 = Constraint(expr=   m.x468 + 5000*m.x707 - 5000*m.x912 <= 0)

m.c314 = Constraint(expr=   m.x469 + 5000*m.x708 - 5000*m.x913 <= 0)

m.c315 = Constraint(expr=   m.x470 + 5000*m.x709 - 5000*m.x914 <= 0)

m.c316 = Constraint(expr=   m.x471 + 5000*m.x710 - 5000*m.x915 <= 0)

m.c317 = Constraint(expr=   m.x472 + 5000*m.x711 - 5000*m.x916 <= 0)

m.c318 = Constraint(expr=   m.x473 + 5000*m.x712 - 5000*m.x917 <= 0)

m.c319 = Constraint(expr=   m.x474 + 5000*m.x713 - 5000*m.x918 <= 0)

m.c320 = Constraint(expr=   m.x475 + 5000*m.x714 - 5000*m.x919 <= 0)

m.c321 = Constraint(expr=   m.x476 + 5000*m.x715 - 5000*m.x920 <= 0)

m.c322 = Constraint(expr=   m.x477 + 5000*m.x716 - 5000*m.x921 <= 0)

m.c323 = Constraint(expr=   m.x478 + 5000*m.x717 - 5000*m.x922 <= 0)

m.c324 = Constraint(expr=   m.x479 + 5000*m.x718 - 5000*m.x923 <= 0)

m.c325 = Constraint(expr=   m.x480 + 5000*m.x719 - 5000*m.x924 <= 0)

m.c326 = Constraint(expr=   m.x481 + 5000*m.x720 - 5000*m.x925 <= 0)

m.c327 = Constraint(expr=   m.x482 + 5000*m.x721 - 5000*m.x926 <= 0)

m.c328 = Constraint(expr=   m.x483 + 5000*m.x722 - 5000*m.x927 <= 0)

m.c329 = Constraint(expr=   m.x484 + 5000*m.x723 - 5000*m.x928 <= 0)

m.c330 = Constraint(expr=   m.x485 + 5000*m.x724 - 5000*m.x929 <= 0)

m.c331 = Constraint(expr=   m.x486 + 5000*m.x725 - 5000*m.x930 <= 0)

m.c332 = Constraint(expr=   m.x487 + 5000*m.x726 - 5000*m.x931 <= 0)

m.c333 = Constraint(expr=   m.x488 + 5000*m.x727 - 5000*m.x932 <= 0)

m.c334 = Constraint(expr=   m.x489 + 5000*m.x728 - 5000*m.x933 <= 0)

m.c335 = Constraint(expr=   m.x490 + 5000*m.x729 - 5000*m.x934 <= 0)

m.c336 = Constraint(expr=   m.x491 + 5000*m.x730 - 5000*m.x935 <= 0)

m.c337 = Constraint(expr=   m.x492 + 5000*m.x731 - 5000*m.x936 <= 0)

m.c338 = Constraint(expr=   m.x493 + 5000*m.x732 - 5000*m.x937 <= 0)

m.c339 = Constraint(expr=   m.x494 + 5000*m.x733 - 5000*m.x938 <= 0)

m.c340 = Constraint(expr=   m.x495 + 5000*m.x734 - 5000*m.x939 <= 0)

m.c341 = Constraint(expr=   m.x496 + 5000*m.x735 - 5000*m.x940 <= 0)

m.c342 = Constraint(expr=   m.x497 + 5000*m.x736 - 5000*m.x941 <= 0)

m.c343 = Constraint(expr=   m.x498 + 5000*m.x737 - 5000*m.x942 <= 0)

m.c344 = Constraint(expr=   m.x499 + 5000*m.x738 - 5000*m.x943 <= 0)

m.c345 = Constraint(expr=   m.x500 + 5000*m.x739 - 5000*m.x944 <= 0)

m.c346 = Constraint(expr=   m.x501 + 5000*m.x740 - 5000*m.x945 <= 0)

m.c347 = Constraint(expr=   m.x502 + 5000*m.x741 - 5000*m.x946 <= 0)

m.c348 = Constraint(expr=   m.x503 + 5000*m.x742 - 5000*m.x947 <= 0)

m.c349 = Constraint(expr=   m.x504 + 5000*m.x743 - 5000*m.x948 <= 0)

m.c350 = Constraint(expr=   m.x505 + 5000*m.x744 - 5000*m.x949 <= 0)

m.c351 = Constraint(expr=   m.x506 + 5000*m.x745 - 5000*m.x950 <= 0)

m.c352 = Constraint(expr=   m.x507 + 5000*m.x746 - 5000*m.x951 <= 0)

m.c353 = Constraint(expr=   m.x508 + 5000*m.x747 - 5000*m.x952 <= 0)

m.c354 = Constraint(expr=   m.x509 + 5000*m.x748 - 5000*m.x953 <= 0)

m.c355 = Constraint(expr=   m.x510 + 5000*m.x749 - 5000*m.x954 <= 0)

m.c356 = Constraint(expr=   m.x511 + 5000*m.x750 - 5000*m.x955 <= 0)

m.c357 = Constraint(expr=   m.x512 + 5000*m.x751 - 5000*m.x956 <= 0)

m.c358 = Constraint(expr=   m.x513 + 5000*m.x752 - 5000*m.x957 <= 0)

m.c359 = Constraint(expr=   m.x514 + 5000*m.x753 - 5000*m.x958 <= 0)

m.c360 = Constraint(expr=   m.x515 + 5000*m.x754 - 5000*m.x959 <= 0)

m.c361 = Constraint(expr=   m.x516 + 5000*m.x755 - 5000*m.x960 <= 0)

m.c362 = Constraint(expr=   m.x517 + 5000*m.x756 - 5000*m.x961 <= 0)

m.c363 = Constraint(expr=   m.x518 + 5000*m.x757 - 5000*m.x962 <= 0)

m.c364 = Constraint(expr=   m.x519 + 5000*m.x758 - 5000*m.x963 <= 0)

m.c365 = Constraint(expr=   m.x520 + 5000*m.x759 - 5000*m.x964 <= 0)

m.c366 = Constraint(expr=   m.x521 + 5000*m.x760 - 5000*m.x965 <= 0)

m.c367 = Constraint(expr=   m.x522 + 5000*m.x761 - 5000*m.x966 <= 0)

m.c368 = Constraint(expr=   m.x523 + 5000*m.x762 - 5000*m.x967 <= 0)

m.c369 = Constraint(expr=   m.x524 + 5000*m.x763 - 5000*m.x968 <= 0)

m.c370 = Constraint(expr=   m.x525 + 5000*m.x764 - 5000*m.x969 <= 0)

m.c371 = Constraint(expr=   m.x526 + 5000*m.x765 - 5000*m.x970 <= 0)

m.c372 = Constraint(expr=   m.x527 + 5000*m.x766 - 5000*m.x971 <= 0)

m.c373 = Constraint(expr=   m.x528 + 5000*m.x767 - 5000*m.x972 <= 0)

m.c374 = Constraint(expr=   m.x529 + 5000*m.x768 - 5000*m.x973 <= 0)

m.c375 = Constraint(expr=   m.x530 + 5000*m.x769 - 5000*m.x974 <= 0)

m.c376 = Constraint(expr=   m.x531 + 5000*m.x770 - 5000*m.x975 <= 0)

m.c377 = Constraint(expr=   m.x532 + 5000*m.x771 - 5000*m.x976 <= 0)

m.c378 = Constraint(expr=   m.x533 + 5000*m.x772 - 5000*m.x977 <= 0)

m.c379 = Constraint(expr=   m.x534 + 5000*m.x773 - 5000*m.x978 <= 0)

m.c380 = Constraint(expr=   m.x535 + 5000*m.x774 - 5000*m.x979 <= 0)

m.c381 = Constraint(expr=   m.x536 + 5000*m.x775 - 5000*m.x980 <= 0)

m.c382 = Constraint(expr=   m.x537 + 5000*m.x776 - 5000*m.x981 <= 0)

m.c383 = Constraint(expr=   m.x538 + 5000*m.x777 - 5000*m.x982 <= 0)

m.c384 = Constraint(expr=   m.x539 + 5000*m.x778 - 5000*m.x983 <= 0)

m.c385 = Constraint(expr=   m.x540 + 5000*m.x779 - 5000*m.x984 <= 0)

m.c386 = Constraint(expr=   m.x541 + 5000*m.x780 - 5000*m.x985 <= 0)

m.c387 = Constraint(expr=   m.x542 + 5000*m.x781 - 5000*m.x986 <= 0)

m.c388 = Constraint(expr=   m.x543 + 5000*m.x782 - 5000*m.x987 <= 0)

m.c389 = Constraint(expr=   m.x544 + 5000*m.x783 - 5000*m.x988 <= 0)

m.c390 = Constraint(expr=   m.x545 + 5000*m.x784 - 5000*m.x989 <= 0)

m.c391 = Constraint(expr=   m.x546 + 5000*m.x785 - 5000*m.x990 <= 0)

m.c392 = Constraint(expr=   m.x547 + 5000*m.x786 - 5000*m.x991 <= 0)

m.c393 = Constraint(expr=   m.x548 + 5000*m.x787 - 5000*m.x992 <= 0)

m.c394 = Constraint(expr=   m.x549 + 5000*m.x788 - 5000*m.x993 <= 0)

m.c395 = Constraint(expr=   m.x550 + 5000*m.x789 - 5000*m.x994 <= 0)

m.c396 = Constraint(expr=   m.x551 + 5000*m.x790 - 5000*m.x995 <= 0)

m.c397 = Constraint(expr=   m.x552 + 5000*m.x791 - 5000*m.x996 <= 0)

m.c398 = Constraint(expr=   m.x553 + 5000*m.x792 - 5000*m.x997 <= 0)

m.c399 = Constraint(expr=   m.x554 + 5000*m.x793 - 5000*m.x998 <= 0)

m.c400 = Constraint(expr=   m.x555 + 5000*m.x794 - 5000*m.x999 <= 0)

m.c401 = Constraint(expr=   m.x556 + 5000*m.x795 - 5000*m.x1000 <= 0)

m.c402 = Constraint(expr=   m.x557 + 5000*m.x796 - 5000*m.x1001 <= 0)

m.c403 = Constraint(expr=   m.x558 + 5000*m.x797 - 5000*m.x1002 <= 0)

m.c404 = Constraint(expr=   m.x559 + 5000*m.x798 - 5000*m.x1003 <= 0)

m.c405 = Constraint(expr=   m.x560 + 5000*m.x799 - 5000*m.x1004 <= 0)

m.c406 = Constraint(expr=   m.x561 + 5000*m.x800 - 5000*m.x1005 <= 0)

m.c407 = Constraint(expr=   m.x562 + 5000*m.x801 - 5000*m.x1006 <= 0)

m.c408 = Constraint(expr=   m.x563 + 5000*m.x802 - 5000*m.x1007 <= 0)

m.c409 = Constraint(expr=   m.x564 + 5000*m.x803 - 5000*m.x1008 <= 0)

m.c410 = Constraint(expr=   m.x565 + 5000*m.x804 - 5000*m.x1009 <= 0)

m.c411 = Constraint(expr=   m.x566 + 5000*m.x805 - 5000*m.x1010 <= 0)

m.c412 = Constraint(expr=   m.x567 + 5000*m.x806 - 5000*m.x1011 <= 0)

m.c413 = Constraint(expr=   m.x568 + 5000*m.x807 - 5000*m.x1012 <= 0)

m.c414 = Constraint(expr=   m.x569 + 5000*m.x808 - 5000*m.x1013 <= 0)

m.c415 = Constraint(expr=   m.x570 + 5000*m.x809 - 5000*m.x1014 <= 0)

m.c416 = Constraint(expr=   m.x571 + 5000*m.x810 - 5000*m.x1015 <= 0)

m.c417 = Constraint(expr=   m.x572 + 5000*m.x811 - 5000*m.x1016 <= 0)

m.c418 = Constraint(expr=   m.x573 + 5000*m.x812 - 5000*m.x1017 <= 0)

m.c419 = Constraint(expr=   m.x574 + 5000*m.x813 - 5000*m.x1018 <= 0)

m.c420 = Constraint(expr=   m.x575 + 5000*m.x814 - 5000*m.x1019 <= 0)

m.c421 = Constraint(expr=   m.x576 + 5000*m.x815 - 5000*m.x1020 <= 0)

m.c422 = Constraint(expr=   m.x577 + 5000*m.x816 - 5000*m.x1021 <= 0)

m.c423 = Constraint(expr=   m.x578 + 5000*m.x817 - 5000*m.x1022 <= 0)

m.c424 = Constraint(expr=   m.x579 + 5000*m.x818 - 5000*m.x1023 <= 0)

m.c425 = Constraint(expr=   m.x580 + 5000*m.x819 - 5000*m.x1024 <= 0)

m.c426 = Constraint(expr=   m.x581 + 5000*m.x820 - 5000*m.x1025 <= 0)

m.c427 = Constraint(expr=   m.x582 + 5000*m.x821 - 5000*m.x1026 <= 0)

m.c428 = Constraint(expr=   m.x583 + 5000*m.x822 - 5000*m.x1027 <= 0)

m.c429 = Constraint(expr=   m.x584 + 5000*m.x823 - 5000*m.x1028 <= 0)

m.c430 = Constraint(expr=   m.x585 + 5000*m.x824 - 5000*m.x1029 <= 0)

m.c431 = Constraint(expr=   m.x586 + 5000*m.x825 - 5000*m.x1030 <= 0)

m.c432 = Constraint(expr=   m.x587 + 5000*m.x826 - 5000*m.x1031 <= 0)

m.c433 = Constraint(expr=   m.x588 + 5000*m.x827 - 5000*m.x1032 <= 0)

m.c434 = Constraint(expr=   m.x589 + 5000*m.x828 - 5000*m.x1033 <= 0)

m.c435 = Constraint(expr=   m.x590 + 5000*m.x829 - 5000*m.x1034 <= 0)

m.c436 = Constraint(expr=   m.x591 + 5000*m.x830 - 5000*m.x1035 <= 0)

m.c437 = Constraint(expr=   m.x592 + 5000*m.x831 - 5000*m.x1036 <= 0)

m.c438 = Constraint(expr=   m.x593 + 5000*m.x832 - 5000*m.x1037 <= 0)

m.c439 = Constraint(expr=   m.x594 + 5000*m.x833 - 5000*m.x1038 <= 0)

m.c440 = Constraint(expr=   m.x595 + 5000*m.x834 - 5000*m.x1039 <= 0)

m.c441 = Constraint(expr=   m.x596 + 5000*m.x835 - 5000*m.x1040 <= 0)

m.c442 = Constraint(expr=   m.x597 + 5000*m.x836 - 5000*m.x1041 <= 0)

m.c443 = Constraint(expr=   m.x598 + 5000*m.x837 - 5000*m.x1042 <= 0)

m.c444 = Constraint(expr=   m.x599 + 5000*m.x838 - 5000*m.x1043 <= 0)

m.c445 = Constraint(expr=   m.x600 + 5000*m.x839 - 5000*m.x1044 <= 0)

m.c446 = Constraint(expr=   m.x601 + 5000*m.x840 - 5000*m.x1045 <= 0)

m.c447 = Constraint(expr=   m.x602 + 5000*m.x841 - 5000*m.x1046 <= 0)

m.c448 = Constraint(expr=   m.x603 + 5000*m.x842 - 5000*m.x1047 <= 0)

m.c449 = Constraint(expr=   m.x604 + 5000*m.x843 - 5000*m.x1048 <= 0)

m.c450 = Constraint(expr=   m.x605 + 5000*m.x844 - 5000*m.x1049 <= 0)

m.c451 = Constraint(expr=   m.x606 + 5000*m.x845 - 5000*m.x1050 <= 0)

m.c452 = Constraint(expr=   m.x607 + 5000*m.x846 - 5000*m.x1051 <= 0)

m.c453 = Constraint(expr=   m.x608 + 5000*m.x847 - 5000*m.x1052 <= 0)

m.c454 = Constraint(expr=   m.x609 + 5000*m.x848 - 5000*m.x1053 <= 0)

m.c455 = Constraint(expr=   m.x610 + 5000*m.x849 - 5000*m.x1054 <= 0)

m.c456 = Constraint(expr=   m.x611 + 5000*m.x850 - 5000*m.x1055 <= 0)

m.c457 = Constraint(expr=   m.x612 + 5000*m.x851 - 5000*m.x1056 <= 0)

m.c458 = Constraint(expr=   m.x613 + 5000*m.x852 - 5000*m.x1057 <= 0)

m.c459 = Constraint(expr=   m.x614 + 5000*m.x853 - 5000*m.x1058 <= 0)

m.c460 = Constraint(expr=   m.x615 + 5000*m.x854 - 5000*m.x1059 <= 0)

m.c461 = Constraint(expr=   m.x616 + 5000*m.x855 - 5000*m.x1060 <= 0)

m.c462 = Constraint(expr=   m.x617 + 5000*m.x856 - 5000*m.x1061 <= 0)

m.c463 = Constraint(expr=   m.x618 + 5000*m.x857 - 5000*m.x1062 <= 0)

m.c464 = Constraint(expr=   m.x619 + 5000*m.x858 - 5000*m.x1063 <= 0)

m.c465 = Constraint(expr=   m.x620 + 5000*m.x859 - 5000*m.x1064 <= 0)

m.c466 = Constraint(expr= - 3000*m.b1 + m.x416 <= 0)

m.c467 = Constraint(expr=   m.x417 <= 0)

m.c468 = Constraint(expr=   m.x418 <= 0)

m.c469 = Constraint(expr=   m.x419 <= 0)

m.c470 = Constraint(expr=   m.x420 <= 0)

m.c471 = Constraint(expr= - 3000*m.b6 + m.x421 <= 0)

m.c472 = Constraint(expr=   m.x422 <= 0)

m.c473 = Constraint(expr=   m.x423 <= 0)

m.c474 = Constraint(expr=   m.x424 <= 0)

m.c475 = Constraint(expr=   m.x425 <= 0)

m.c476 = Constraint(expr= - 3000*m.b11 + m.x426 <= 0)

m.c477 = Constraint(expr=   m.x427 <= 0)

m.c478 = Constraint(expr=   m.x428 <= 0)

m.c479 = Constraint(expr=   m.x429 <= 0)

m.c480 = Constraint(expr=   m.x430 <= 0)

m.c481 = Constraint(expr= - 3000*m.b16 + m.x431 <= 0)

m.c482 = Constraint(expr= - 3000*m.b17 + m.x432 <= 0)

m.c483 = Constraint(expr=   m.x433 <= 0)

m.c484 = Constraint(expr=   m.x434 <= 0)

m.c485 = Constraint(expr=   m.x435 <= 0)

m.c486 = Constraint(expr= - 3000*m.b21 + m.x436 <= 0)

m.c487 = Constraint(expr= - 3000*m.b22 + m.x437 <= 0)

m.c488 = Constraint(expr=   m.x438 <= 0)

m.c489 = Constraint(expr=   m.x439 <= 0)

m.c490 = Constraint(expr=   m.x440 <= 0)

m.c491 = Constraint(expr= - 3000*m.b26 + m.x441 <= 0)

m.c492 = Constraint(expr= - 3000*m.b27 + m.x442 <= 0)

m.c493 = Constraint(expr=   m.x443 <= 0)

m.c494 = Constraint(expr=   m.x444 <= 0)

m.c495 = Constraint(expr=   m.x445 <= 0)

m.c496 = Constraint(expr= - 3000*m.b31 + m.x446 <= 0)

m.c497 = Constraint(expr= - 3000*m.b32 + m.x447 <= 0)

m.c498 = Constraint(expr=   m.x448 <= 0)

m.c499 = Constraint(expr=   m.x449 <= 0)

m.c500 = Constraint(expr=   m.x450 <= 0)

m.c501 = Constraint(expr= - 3000*m.b36 + m.x451 <= 0)

m.c502 = Constraint(expr= - 3000*m.b37 + m.x452 <= 0)

m.c503 = Constraint(expr=   m.x453 <= 0)

m.c504 = Constraint(expr=   m.x454 <= 0)

m.c505 = Constraint(expr=   m.x455 <= 0)

m.c506 = Constraint(expr= - 3000*m.b41 + m.x456 <= 0)

m.c507 = Constraint(expr= - 3000*m.b42 + m.x457 <= 0)

m.c508 = Constraint(expr=   m.x458 <= 0)

m.c509 = Constraint(expr=   m.x459 <= 0)

m.c510 = Constraint(expr=   m.x460 <= 0)

m.c511 = Constraint(expr= - 3000*m.b46 + m.x461 <= 0)

m.c512 = Constraint(expr= - 3000*m.b47 + m.x462 <= 0)

m.c513 = Constraint(expr=   m.x463 <= 0)

m.c514 = Constraint(expr=   m.x464 <= 0)

m.c515 = Constraint(expr=   m.x465 <= 0)

m.c516 = Constraint(expr= - 3000*m.b51 + m.x466 <= 0)

m.c517 = Constraint(expr= - 3000*m.b52 + m.x467 <= 0)

m.c518 = Constraint(expr=   m.x468 <= 0)

m.c519 = Constraint(expr=   m.x469 <= 0)

m.c520 = Constraint(expr=   m.x470 <= 0)

m.c521 = Constraint(expr= - 3000*m.b56 + m.x471 <= 0)

m.c522 = Constraint(expr= - 3000*m.b57 + m.x472 <= 0)

m.c523 = Constraint(expr=   m.x473 <= 0)

m.c524 = Constraint(expr=   m.x474 <= 0)

m.c525 = Constraint(expr=   m.x475 <= 0)

m.c526 = Constraint(expr=   m.x476 <= 0)

m.c527 = Constraint(expr= - 5000*m.b62 + m.x477 <= 0)

m.c528 = Constraint(expr=   m.x478 <= 0)

m.c529 = Constraint(expr=   m.x479 <= 0)

m.c530 = Constraint(expr=   m.x480 <= 0)

m.c531 = Constraint(expr=   m.x481 <= 0)

m.c532 = Constraint(expr= - 5000*m.b67 + m.x482 <= 0)

m.c533 = Constraint(expr=   m.x483 <= 0)

m.c534 = Constraint(expr=   m.x484 <= 0)

m.c535 = Constraint(expr=   m.x485 <= 0)

m.c536 = Constraint(expr=   m.x486 <= 0)

m.c537 = Constraint(expr= - 5000*m.b72 + m.x487 <= 0)

m.c538 = Constraint(expr=   m.x488 <= 0)

m.c539 = Constraint(expr=   m.x489 <= 0)

m.c540 = Constraint(expr=   m.x490 <= 0)

m.c541 = Constraint(expr=   m.x491 <= 0)

m.c542 = Constraint(expr= - 5000*m.b77 + m.x492 <= 0)

m.c543 = Constraint(expr= - 5000*m.b78 + m.x493 <= 0)

m.c544 = Constraint(expr=   m.x494 <= 0)

m.c545 = Constraint(expr=   m.x495 <= 0)

m.c546 = Constraint(expr=   m.x496 <= 0)

m.c547 = Constraint(expr= - 5000*m.b82 + m.x497 <= 0)

m.c548 = Constraint(expr= - 5000*m.b83 + m.x498 <= 0)

m.c549 = Constraint(expr=   m.x499 <= 0)

m.c550 = Constraint(expr=   m.x500 <= 0)

m.c551 = Constraint(expr=   m.x501 <= 0)

m.c552 = Constraint(expr= - 5000*m.b87 + m.x502 <= 0)

m.c553 = Constraint(expr= - 5000*m.b88 + m.x503 <= 0)

m.c554 = Constraint(expr=   m.x504 <= 0)

m.c555 = Constraint(expr=   m.x505 <= 0)

m.c556 = Constraint(expr=   m.x506 <= 0)

m.c557 = Constraint(expr= - 3000*m.b92 + m.x507 <= 0)

m.c558 = Constraint(expr= - 3000*m.b93 + m.x508 <= 0)

m.c559 = Constraint(expr=   m.x509 <= 0)

m.c560 = Constraint(expr=   m.x510 <= 0)

m.c561 = Constraint(expr=   m.x511 <= 0)

m.c562 = Constraint(expr= - 3000*m.b97 + m.x512 <= 0)

m.c563 = Constraint(expr= - 3000*m.b98 + m.x513 <= 0)

m.c564 = Constraint(expr=   m.x514 <= 0)

m.c565 = Constraint(expr=   m.x515 <= 0)

m.c566 = Constraint(expr=   m.x516 <= 0)

m.c567 = Constraint(expr= - 3000*m.b102 + m.x517 <= 0)

m.c568 = Constraint(expr= - 3000*m.b103 + m.x518 <= 0)

m.c569 = Constraint(expr=   m.x519 <= 0)

m.c570 = Constraint(expr=   m.x520 <= 0)

m.c571 = Constraint(expr=   m.x521 <= 0)

m.c572 = Constraint(expr= - 3000*m.b107 + m.x522 <= 0)

m.c573 = Constraint(expr= - 3000*m.b108 + m.x523 <= 0)

m.c574 = Constraint(expr=   m.x524 <= 0)

m.c575 = Constraint(expr=   m.x525 <= 0)

m.c576 = Constraint(expr=   m.x526 <= 0)

m.c577 = Constraint(expr= - 3000*m.b112 + m.x527 <= 0)

m.c578 = Constraint(expr= - 3000*m.b113 + m.x528 <= 0)

m.c579 = Constraint(expr=   m.x529 <= 0)

m.c580 = Constraint(expr=   m.x530 <= 0)

m.c581 = Constraint(expr=   m.x531 <= 0)

m.c582 = Constraint(expr= - 3000*m.b117 + m.x532 <= 0)

m.c583 = Constraint(expr= - 3000*m.b118 + m.x533 <= 0)

m.c584 = Constraint(expr=   m.x534 <= 0)

m.c585 = Constraint(expr=   m.x535 <= 0)

m.c586 = Constraint(expr=   m.x536 <= 0)

m.c587 = Constraint(expr=   m.x537 <= 0)

m.c588 = Constraint(expr= - 3000*m.b123 + m.x538 <= 0)

m.c589 = Constraint(expr=   m.x539 <= 0)

m.c590 = Constraint(expr=   m.x540 <= 0)

m.c591 = Constraint(expr=   m.x541 <= 0)

m.c592 = Constraint(expr=   m.x542 <= 0)

m.c593 = Constraint(expr= - 3000*m.b128 + m.x543 <= 0)

m.c594 = Constraint(expr=   m.x544 <= 0)

m.c595 = Constraint(expr=   m.x545 <= 0)

m.c596 = Constraint(expr=   m.x546 <= 0)

m.c597 = Constraint(expr=   m.x547 <= 0)

m.c598 = Constraint(expr= - 3000*m.b133 + m.x548 <= 0)

m.c599 = Constraint(expr=   m.x549 <= 0)

m.c600 = Constraint(expr=   m.x550 <= 0)

m.c601 = Constraint(expr=   m.x551 <= 0)

m.c602 = Constraint(expr=   m.x552 <= 0)

m.c603 = Constraint(expr= - 5000*m.b138 + m.x553 <= 0)

m.c604 = Constraint(expr= - 5000*m.b139 + m.x554 <= 0)

m.c605 = Constraint(expr=   m.x555 <= 0)

m.c606 = Constraint(expr=   m.x556 <= 0)

m.c607 = Constraint(expr=   m.x557 <= 0)

m.c608 = Constraint(expr= - 5000*m.b143 + m.x558 <= 0)

m.c609 = Constraint(expr= - 5000*m.b144 + m.x559 <= 0)

m.c610 = Constraint(expr=   m.x560 <= 0)

m.c611 = Constraint(expr=   m.x561 <= 0)

m.c612 = Constraint(expr=   m.x562 <= 0)

m.c613 = Constraint(expr= - 5000*m.b148 + m.x563 <= 0)

m.c614 = Constraint(expr= - 5000*m.b149 + m.x564 <= 0)

m.c615 = Constraint(expr=   m.x565 <= 0)

m.c616 = Constraint(expr=   m.x566 <= 0)

m.c617 = Constraint(expr=   m.x567 <= 0)

m.c618 = Constraint(expr= - 3500*m.b153 + m.x568 <= 0)

m.c619 = Constraint(expr= - 3500*m.b154 + m.x569 <= 0)

m.c620 = Constraint(expr=   m.x570 <= 0)

m.c621 = Constraint(expr=   m.x571 <= 0)

m.c622 = Constraint(expr=   m.x572 <= 0)

m.c623 = Constraint(expr= - 3500*m.b158 + m.x573 <= 0)

m.c624 = Constraint(expr= - 3500*m.b159 + m.x574 <= 0)

m.c625 = Constraint(expr=   m.x575 <= 0)

m.c626 = Constraint(expr=   m.x576 <= 0)

m.c627 = Constraint(expr=   m.x577 <= 0)

m.c628 = Constraint(expr=   m.x578 <= 0)

m.c629 = Constraint(expr= - 3500*m.b164 + m.x579 <= 0)

m.c630 = Constraint(expr=   m.x580 <= 0)

m.c631 = Constraint(expr=   m.x581 <= 0)

m.c632 = Constraint(expr=   m.x582 <= 0)

m.c633 = Constraint(expr=   m.x583 <= 0)

m.c634 = Constraint(expr= - 3000*m.b169 + m.x584 <= 0)

m.c635 = Constraint(expr= - 3000*m.b170 + m.x585 <= 0)

m.c636 = Constraint(expr=   m.x586 <= 0)

m.c637 = Constraint(expr=   m.x587 <= 0)

m.c638 = Constraint(expr=   m.x588 <= 0)

m.c639 = Constraint(expr= - 3000*m.b174 + m.x589 <= 0)

m.c640 = Constraint(expr= - 3000*m.b175 + m.x590 <= 0)

m.c641 = Constraint(expr=   m.x591 <= 0)

m.c642 = Constraint(expr=   m.x592 <= 0)

m.c643 = Constraint(expr=   m.x593 <= 0)

m.c644 = Constraint(expr= - 3000*m.b179 + m.x594 <= 0)

m.c645 = Constraint(expr= - 3000*m.b180 + m.x595 <= 0)

m.c646 = Constraint(expr=   m.x596 <= 0)

m.c647 = Constraint(expr=   m.x597 <= 0)

m.c648 = Constraint(expr=   m.x598 <= 0)

m.c649 = Constraint(expr= - 3000*m.b184 + m.x599 <= 0)

m.c650 = Constraint(expr= - 3000*m.b185 + m.x600 <= 0)

m.c651 = Constraint(expr=   m.x601 <= 0)

m.c652 = Constraint(expr=   m.x602 <= 0)

m.c653 = Constraint(expr=   m.x603 <= 0)

m.c654 = Constraint(expr= - 3000*m.b189 + m.x604 <= 0)

m.c655 = Constraint(expr= - 3000*m.b190 + m.x605 <= 0)

m.c656 = Constraint(expr=   m.x606 <= 0)

m.c657 = Constraint(expr=   m.x607 <= 0)

m.c658 = Constraint(expr=   m.x608 <= 0)

m.c659 = Constraint(expr= - 3000*m.b194 + m.x609 <= 0)

m.c660 = Constraint(expr= - 3000*m.b195 + m.x610 <= 0)

m.c661 = Constraint(expr=   m.x611 <= 0)

m.c662 = Constraint(expr=   m.x612 <= 0)

m.c663 = Constraint(expr=   m.x613 <= 0)

m.c664 = Constraint(expr=   m.x614 <= 0)

m.c665 = Constraint(expr= - 3000*m.b200 + m.x615 <= 0)

m.c666 = Constraint(expr=   m.x616 <= 0)

m.c667 = Constraint(expr=   m.x617 <= 0)

m.c668 = Constraint(expr=   m.x618 <= 0)

m.c669 = Constraint(expr=   m.x619 <= 0)

m.c670 = Constraint(expr= - 3000*m.b205 + m.x620 <= 0)

m.c671 = Constraint(expr=   m.x416 + m.x417 + m.x418 + m.x419 + m.x420 + m.x421 + m.x422 + m.x423 + m.x424 + m.x425
                          + m.x426 + m.x427 + m.x428 + m.x429 + m.x430 == 3000)

m.c672 = Constraint(expr=   m.x431 + m.x432 + m.x433 + m.x434 + m.x435 + m.x436 + m.x437 + m.x438 + m.x439 + m.x440
                          + m.x441 + m.x442 + m.x443 + m.x444 + m.x445 == 3000)

m.c673 = Constraint(expr=   m.x446 + m.x447 + m.x448 + m.x449 + m.x450 + m.x451 + m.x452 + m.x453 + m.x454 + m.x455
                          + m.x456 + m.x457 + m.x458 + m.x459 + m.x460 == 3000)

m.c674 = Constraint(expr=   m.x461 + m.x462 + m.x463 + m.x464 + m.x465 + m.x466 + m.x467 + m.x468 + m.x469 + m.x470
                          + m.x471 + m.x472 + m.x473 + m.x474 + m.x475 == 3000)

m.c675 = Constraint(expr=   m.x476 + m.x477 + m.x478 + m.x479 + m.x480 + m.x481 + m.x482 + m.x483 + m.x484 + m.x485
                          + m.x486 + m.x487 + m.x488 + m.x489 + m.x490 == 5000)

m.c676 = Constraint(expr=   m.x491 + m.x492 + m.x493 + m.x494 + m.x495 + m.x496 + m.x497 + m.x498 + m.x499 + m.x500
                          + m.x501 + m.x502 + m.x503 + m.x504 + m.x505 == 5000)

m.c677 = Constraint(expr=   m.x506 + m.x507 + m.x508 + m.x509 + m.x510 + m.x511 + m.x512 + m.x513 + m.x514 + m.x515
                          + m.x516 + m.x517 + m.x518 + m.x519 + m.x520 == 3000)

m.c678 = Constraint(expr=   m.x521 + m.x522 + m.x523 + m.x524 + m.x525 + m.x526 + m.x527 + m.x528 + m.x529 + m.x530
                          + m.x531 + m.x532 + m.x533 + m.x534 + m.x535 == 3000)

m.c679 = Constraint(expr=   m.x536 + m.x537 + m.x538 + m.x539 + m.x540 + m.x541 + m.x542 + m.x543 + m.x544 + m.x545
                          + m.x546 + m.x547 + m.x548 + m.x549 + m.x550 == 3000)

m.c680 = Constraint(expr=   m.x551 + m.x552 + m.x553 + m.x554 + m.x555 + m.x556 + m.x557 + m.x558 + m.x559 + m.x560
                          == 5000)

m.c681 = Constraint(expr=   m.x561 + m.x562 + m.x563 + m.x564 + m.x565 == 5000)

m.c682 = Constraint(expr=   m.x566 + m.x567 + m.x568 + m.x569 + m.x570 + m.x571 + m.x572 + m.x573 + m.x574 + m.x575
                          == 3500)

m.c683 = Constraint(expr=   m.x576 + m.x577 + m.x578 + m.x579 + m.x580 == 3500)

m.c684 = Constraint(expr=   m.x581 + m.x582 + m.x583 + m.x584 + m.x585 + m.x586 + m.x587 + m.x588 + m.x589 + m.x590
                          + m.x591 + m.x592 + m.x593 + m.x594 + m.x595 == 3000)

m.c685 = Constraint(expr=   m.x596 + m.x597 + m.x598 + m.x599 + m.x600 + m.x601 + m.x602 + m.x603 + m.x604 + m.x605
                          + m.x606 + m.x607 + m.x608 + m.x609 + m.x610 == 3000)

m.c686 = Constraint(expr=   m.x611 + m.x612 + m.x613 + m.x614 + m.x615 == 3000)

m.c687 = Constraint(expr=   m.x616 + m.x617 + m.x618 + m.x619 + m.x620 == 3000)

m.c688 = Constraint(expr=   7*m.b1 + m.x621 - m.x655 <= 7)

m.c689 = Constraint(expr=   7*m.b2 + m.x621 - m.x656 <= 7)

m.c690 = Constraint(expr=   7*m.b3 + m.x621 - m.x657 <= 7)

m.c691 = Constraint(expr=   7*m.b4 + m.x621 - m.x658 <= 7)

m.c692 = Constraint(expr=   7*m.b5 + m.x621 - m.x659 <= 7)

m.c693 = Constraint(expr=   7*m.b6 + m.x621 - m.x660 <= 7)

m.c694 = Constraint(expr=   7*m.b7 + m.x621 - m.x661 <= 7)

m.c695 = Constraint(expr=   7*m.b8 + m.x621 - m.x662 <= 7)

m.c696 = Constraint(expr=   7*m.b9 + m.x621 - m.x663 <= 7)

m.c697 = Constraint(expr=   7*m.b10 + m.x621 - m.x664 <= 7)

m.c698 = Constraint(expr=   7*m.b11 + m.x621 - m.x665 <= 7)

m.c699 = Constraint(expr=   7*m.b12 + m.x621 - m.x666 <= 7)

m.c700 = Constraint(expr=   7*m.b13 + m.x621 - m.x667 <= 7)

m.c701 = Constraint(expr=   7*m.b14 + m.x621 - m.x668 <= 7)

m.c702 = Constraint(expr=   7*m.b15 + m.x621 - m.x669 <= 7)

m.c703 = Constraint(expr=   7*m.b16 + m.x622 - m.x670 <= 7)

m.c704 = Constraint(expr=   7*m.b17 + m.x622 - m.x671 <= 7)

m.c705 = Constraint(expr=   7*m.b18 + m.x622 - m.x672 <= 7)

m.c706 = Constraint(expr=   7*m.b19 + m.x622 - m.x673 <= 7)

m.c707 = Constraint(expr=   7*m.b20 + m.x622 - m.x674 <= 7)

m.c708 = Constraint(expr=   7*m.b21 + m.x622 - m.x675 <= 7)

m.c709 = Constraint(expr=   7*m.b22 + m.x622 - m.x676 <= 7)

m.c710 = Constraint(expr=   7*m.b23 + m.x622 - m.x677 <= 7)

m.c711 = Constraint(expr=   7*m.b24 + m.x622 - m.x678 <= 7)

m.c712 = Constraint(expr=   7*m.b25 + m.x622 - m.x679 <= 7)

m.c713 = Constraint(expr=   7*m.b26 + m.x622 - m.x680 <= 7)

m.c714 = Constraint(expr=   7*m.b27 + m.x622 - m.x681 <= 7)

m.c715 = Constraint(expr=   7*m.b28 + m.x622 - m.x682 <= 7)

m.c716 = Constraint(expr=   7*m.b29 + m.x622 - m.x683 <= 7)

m.c717 = Constraint(expr=   7*m.b30 + m.x622 - m.x684 <= 7)

m.c718 = Constraint(expr=   7*m.b31 + m.x623 - m.x685 <= 7)

m.c719 = Constraint(expr=   7*m.b32 + m.x623 - m.x686 <= 7)

m.c720 = Constraint(expr=   7*m.b33 + m.x623 - m.x687 <= 7)

m.c721 = Constraint(expr=   7*m.b34 + m.x623 - m.x688 <= 7)

m.c722 = Constraint(expr=   7*m.b35 + m.x623 - m.x689 <= 7)

m.c723 = Constraint(expr=   7*m.b36 + m.x623 - m.x690 <= 7)

m.c724 = Constraint(expr=   7*m.b37 + m.x623 - m.x691 <= 7)

m.c725 = Constraint(expr=   7*m.b38 + m.x623 - m.x692 <= 7)

m.c726 = Constraint(expr=   7*m.b39 + m.x623 - m.x693 <= 7)

m.c727 = Constraint(expr=   7*m.b40 + m.x623 - m.x694 <= 7)

m.c728 = Constraint(expr=   7*m.b41 + m.x623 - m.x695 <= 7)

m.c729 = Constraint(expr=   7*m.b42 + m.x623 - m.x696 <= 7)

m.c730 = Constraint(expr=   7*m.b43 + m.x623 - m.x697 <= 7)

m.c731 = Constraint(expr=   7*m.b44 + m.x623 - m.x698 <= 7)

m.c732 = Constraint(expr=   7*m.b45 + m.x623 - m.x699 <= 7)

m.c733 = Constraint(expr=   7*m.b46 + m.x624 - m.x700 <= 7)

m.c734 = Constraint(expr=   7*m.b47 + m.x624 - m.x701 <= 7)

m.c735 = Constraint(expr=   7*m.b48 + m.x624 - m.x702 <= 7)

m.c736 = Constraint(expr=   7*m.b49 + m.x624 - m.x703 <= 7)

m.c737 = Constraint(expr=   7*m.b50 + m.x624 - m.x704 <= 7)

m.c738 = Constraint(expr=   7*m.b51 + m.x624 - m.x705 <= 7)

m.c739 = Constraint(expr=   7*m.b52 + m.x624 - m.x706 <= 7)

m.c740 = Constraint(expr=   7*m.b53 + m.x624 - m.x707 <= 7)

m.c741 = Constraint(expr=   7*m.b54 + m.x624 - m.x708 <= 7)

m.c742 = Constraint(expr=   7*m.b55 + m.x624 - m.x709 <= 7)

m.c743 = Constraint(expr=   7*m.b56 + m.x624 - m.x710 <= 7)

m.c744 = Constraint(expr=   7*m.b57 + m.x624 - m.x711 <= 7)

m.c745 = Constraint(expr=   7*m.b58 + m.x624 - m.x712 <= 7)

m.c746 = Constraint(expr=   7*m.b59 + m.x624 - m.x713 <= 7)

m.c747 = Constraint(expr=   7*m.b60 + m.x624 - m.x714 <= 7)

m.c748 = Constraint(expr=   7*m.b61 + m.x625 - m.x715 <= 7)

m.c749 = Constraint(expr=   7*m.b62 + m.x625 - m.x716 <= 7)

m.c750 = Constraint(expr=   7*m.b63 + m.x625 - m.x717 <= 7)

m.c751 = Constraint(expr=   7*m.b64 + m.x625 - m.x718 <= 7)

m.c752 = Constraint(expr=   7*m.b65 + m.x625 - m.x719 <= 7)

m.c753 = Constraint(expr=   7*m.b66 + m.x625 - m.x720 <= 7)

m.c754 = Constraint(expr=   7*m.b67 + m.x625 - m.x721 <= 7)

m.c755 = Constraint(expr=   7*m.b68 + m.x625 - m.x722 <= 7)

m.c756 = Constraint(expr=   7*m.b69 + m.x625 - m.x723 <= 7)

m.c757 = Constraint(expr=   7*m.b70 + m.x625 - m.x724 <= 7)

m.c758 = Constraint(expr=   7*m.b71 + m.x625 - m.x725 <= 7)

m.c759 = Constraint(expr=   7*m.b72 + m.x625 - m.x726 <= 7)

m.c760 = Constraint(expr=   7*m.b73 + m.x625 - m.x727 <= 7)

m.c761 = Constraint(expr=   7*m.b74 + m.x625 - m.x728 <= 7)

m.c762 = Constraint(expr=   7*m.b75 + m.x625 - m.x729 <= 7)

m.c763 = Constraint(expr=   7*m.b76 + m.x626 - m.x730 <= 7)

m.c764 = Constraint(expr=   7*m.b77 + m.x626 - m.x731 <= 7)

m.c765 = Constraint(expr=   7*m.b78 + m.x626 - m.x732 <= 7)

m.c766 = Constraint(expr=   7*m.b79 + m.x626 - m.x733 <= 7)

m.c767 = Constraint(expr=   7*m.b80 + m.x626 - m.x734 <= 7)

m.c768 = Constraint(expr=   7*m.b81 + m.x626 - m.x735 <= 7)

m.c769 = Constraint(expr=   7*m.b82 + m.x626 - m.x736 <= 7)

m.c770 = Constraint(expr=   7*m.b83 + m.x626 - m.x737 <= 7)

m.c771 = Constraint(expr=   7*m.b84 + m.x626 - m.x738 <= 7)

m.c772 = Constraint(expr=   7*m.b85 + m.x626 - m.x739 <= 7)

m.c773 = Constraint(expr=   7*m.b86 + m.x626 - m.x740 <= 7)

m.c774 = Constraint(expr=   7*m.b87 + m.x626 - m.x741 <= 7)

m.c775 = Constraint(expr=   7*m.b88 + m.x626 - m.x742 <= 7)

m.c776 = Constraint(expr=   7*m.b89 + m.x626 - m.x743 <= 7)

m.c777 = Constraint(expr=   7*m.b90 + m.x626 - m.x744 <= 7)

m.c778 = Constraint(expr=   7*m.b91 + m.x627 - m.x745 <= 7)

m.c779 = Constraint(expr=   7*m.b92 + m.x627 - m.x746 <= 7)

m.c780 = Constraint(expr=   7*m.b93 + m.x627 - m.x747 <= 7)

m.c781 = Constraint(expr=   7*m.b94 + m.x627 - m.x748 <= 7)

m.c782 = Constraint(expr=   7*m.b95 + m.x627 - m.x749 <= 7)

m.c783 = Constraint(expr=   7*m.b96 + m.x627 - m.x750 <= 7)

m.c784 = Constraint(expr=   7*m.b97 + m.x627 - m.x751 <= 7)

m.c785 = Constraint(expr=   7*m.b98 + m.x627 - m.x752 <= 7)

m.c786 = Constraint(expr=   7*m.b99 + m.x627 - m.x753 <= 7)

m.c787 = Constraint(expr=   7*m.b100 + m.x627 - m.x754 <= 7)

m.c788 = Constraint(expr=   7*m.b101 + m.x627 - m.x755 <= 7)

m.c789 = Constraint(expr=   7*m.b102 + m.x627 - m.x756 <= 7)

m.c790 = Constraint(expr=   7*m.b103 + m.x627 - m.x757 <= 7)

m.c791 = Constraint(expr=   7*m.b104 + m.x627 - m.x758 <= 7)

m.c792 = Constraint(expr=   7*m.b105 + m.x627 - m.x759 <= 7)

m.c793 = Constraint(expr=   7*m.b106 + m.x628 - m.x760 <= 7)

m.c794 = Constraint(expr=   7*m.b107 + m.x628 - m.x761 <= 7)

m.c795 = Constraint(expr=   7*m.b108 + m.x628 - m.x762 <= 7)

m.c796 = Constraint(expr=   7*m.b109 + m.x628 - m.x763 <= 7)

m.c797 = Constraint(expr=   7*m.b110 + m.x628 - m.x764 <= 7)

m.c798 = Constraint(expr=   7*m.b111 + m.x628 - m.x765 <= 7)

m.c799 = Constraint(expr=   7*m.b112 + m.x628 - m.x766 <= 7)

m.c800 = Constraint(expr=   7*m.b113 + m.x628 - m.x767 <= 7)

m.c801 = Constraint(expr=   7*m.b114 + m.x628 - m.x768 <= 7)

m.c802 = Constraint(expr=   7*m.b115 + m.x628 - m.x769 <= 7)

m.c803 = Constraint(expr=   7*m.b116 + m.x628 - m.x770 <= 7)

m.c804 = Constraint(expr=   7*m.b117 + m.x628 - m.x771 <= 7)

m.c805 = Constraint(expr=   7*m.b118 + m.x628 - m.x772 <= 7)

m.c806 = Constraint(expr=   7*m.b119 + m.x628 - m.x773 <= 7)

m.c807 = Constraint(expr=   7*m.b120 + m.x628 - m.x774 <= 7)

m.c808 = Constraint(expr=   7*m.b121 + m.x629 - m.x775 <= 7)

m.c809 = Constraint(expr=   7*m.b122 + m.x629 - m.x776 <= 7)

m.c810 = Constraint(expr=   7*m.b123 + m.x629 - m.x777 <= 7)

m.c811 = Constraint(expr=   7*m.b124 + m.x629 - m.x778 <= 7)

m.c812 = Constraint(expr=   7*m.b125 + m.x629 - m.x779 <= 7)

m.c813 = Constraint(expr=   7*m.b126 + m.x629 - m.x780 <= 7)

m.c814 = Constraint(expr=   7*m.b127 + m.x629 - m.x781 <= 7)

m.c815 = Constraint(expr=   7*m.b128 + m.x629 - m.x782 <= 7)

m.c816 = Constraint(expr=   7*m.b129 + m.x629 - m.x783 <= 7)

m.c817 = Constraint(expr=   7*m.b130 + m.x629 - m.x784 <= 7)

m.c818 = Constraint(expr=   7*m.b131 + m.x629 - m.x785 <= 7)

m.c819 = Constraint(expr=   7*m.b132 + m.x629 - m.x786 <= 7)

m.c820 = Constraint(expr=   7*m.b133 + m.x629 - m.x787 <= 7)

m.c821 = Constraint(expr=   7*m.b134 + m.x629 - m.x788 <= 7)

m.c822 = Constraint(expr=   7*m.b135 + m.x629 - m.x789 <= 7)

m.c823 = Constraint(expr=   7*m.b136 + m.x630 - m.x790 <= 7)

m.c824 = Constraint(expr=   7*m.b137 + m.x630 - m.x791 <= 7)

m.c825 = Constraint(expr=   7*m.b138 + m.x630 - m.x792 <= 7)

m.c826 = Constraint(expr=   7*m.b139 + m.x630 - m.x793 <= 7)

m.c827 = Constraint(expr=   7*m.b140 + m.x630 - m.x794 <= 7)

m.c828 = Constraint(expr=   7*m.b141 + m.x630 - m.x795 <= 7)

m.c829 = Constraint(expr=   7*m.b142 + m.x630 - m.x796 <= 7)

m.c830 = Constraint(expr=   7*m.b143 + m.x630 - m.x797 <= 7)

m.c831 = Constraint(expr=   7*m.b144 + m.x630 - m.x798 <= 7)

m.c832 = Constraint(expr=   7*m.b145 + m.x630 - m.x799 <= 7)

m.c833 = Constraint(expr=   7*m.b146 + m.x631 - m.x800 <= 7)

m.c834 = Constraint(expr=   7*m.b147 + m.x631 - m.x801 <= 7)

m.c835 = Constraint(expr=   7*m.b148 + m.x631 - m.x802 <= 7)

m.c836 = Constraint(expr=   7*m.b149 + m.x631 - m.x803 <= 7)

m.c837 = Constraint(expr=   7*m.b150 + m.x631 - m.x804 <= 7)

m.c838 = Constraint(expr=   7*m.b151 + m.x632 - m.x805 <= 7)

m.c839 = Constraint(expr=   7*m.b152 + m.x632 - m.x806 <= 7)

m.c840 = Constraint(expr=   7*m.b153 + m.x632 - m.x807 <= 7)

m.c841 = Constraint(expr=   7*m.b154 + m.x632 - m.x808 <= 7)

m.c842 = Constraint(expr=   7*m.b155 + m.x632 - m.x809 <= 7)

m.c843 = Constraint(expr=   7*m.b156 + m.x632 - m.x810 <= 7)

m.c844 = Constraint(expr=   7*m.b157 + m.x632 - m.x811 <= 7)

m.c845 = Constraint(expr=   7*m.b158 + m.x632 - m.x812 <= 7)

m.c846 = Constraint(expr=   7*m.b159 + m.x632 - m.x813 <= 7)

m.c847 = Constraint(expr=   7*m.b160 + m.x632 - m.x814 <= 7)

m.c848 = Constraint(expr=   7*m.b161 + m.x633 - m.x815 <= 7)

m.c849 = Constraint(expr=   7*m.b162 + m.x633 - m.x816 <= 7)

m.c850 = Constraint(expr=   7*m.b163 + m.x633 - m.x817 <= 7)

m.c851 = Constraint(expr=   7*m.b164 + m.x633 - m.x818 <= 7)

m.c852 = Constraint(expr=   7*m.b165 + m.x633 - m.x819 <= 7)

m.c853 = Constraint(expr=   7*m.b166 + m.x634 - m.x820 <= 7)

m.c854 = Constraint(expr=   7*m.b167 + m.x634 - m.x821 <= 7)

m.c855 = Constraint(expr=   7*m.b168 + m.x634 - m.x822 <= 7)

m.c856 = Constraint(expr=   7*m.b169 + m.x634 - m.x823 <= 7)

m.c857 = Constraint(expr=   7*m.b170 + m.x634 - m.x824 <= 7)

m.c858 = Constraint(expr=   7*m.b171 + m.x634 - m.x825 <= 7)

m.c859 = Constraint(expr=   7*m.b172 + m.x634 - m.x826 <= 7)

m.c860 = Constraint(expr=   7*m.b173 + m.x634 - m.x827 <= 7)

m.c861 = Constraint(expr=   7*m.b174 + m.x634 - m.x828 <= 7)

m.c862 = Constraint(expr=   7*m.b175 + m.x634 - m.x829 <= 7)

m.c863 = Constraint(expr=   7*m.b176 + m.x634 - m.x830 <= 7)

m.c864 = Constraint(expr=   7*m.b177 + m.x634 - m.x831 <= 7)

m.c865 = Constraint(expr=   7*m.b178 + m.x634 - m.x832 <= 7)

m.c866 = Constraint(expr=   7*m.b179 + m.x634 - m.x833 <= 7)

m.c867 = Constraint(expr=   7*m.b180 + m.x634 - m.x834 <= 7)

m.c868 = Constraint(expr=   7*m.b181 + m.x635 - m.x835 <= 7)

m.c869 = Constraint(expr=   7*m.b182 + m.x635 - m.x836 <= 7)

m.c870 = Constraint(expr=   7*m.b183 + m.x635 - m.x837 <= 7)

m.c871 = Constraint(expr=   7*m.b184 + m.x635 - m.x838 <= 7)

m.c872 = Constraint(expr=   7*m.b185 + m.x635 - m.x839 <= 7)

m.c873 = Constraint(expr=   7*m.b186 + m.x635 - m.x840 <= 7)

m.c874 = Constraint(expr=   7*m.b187 + m.x635 - m.x841 <= 7)

m.c875 = Constraint(expr=   7*m.b188 + m.x635 - m.x842 <= 7)

m.c876 = Constraint(expr=   7*m.b189 + m.x635 - m.x843 <= 7)

m.c877 = Constraint(expr=   7*m.b190 + m.x635 - m.x844 <= 7)

m.c878 = Constraint(expr=   7*m.b191 + m.x635 - m.x845 <= 7)

m.c879 = Constraint(expr=   7*m.b192 + m.x635 - m.x846 <= 7)

m.c880 = Constraint(expr=   7*m.b193 + m.x635 - m.x847 <= 7)

m.c881 = Constraint(expr=   7*m.b194 + m.x635 - m.x848 <= 7)

m.c882 = Constraint(expr=   7*m.b195 + m.x635 - m.x849 <= 7)

m.c883 = Constraint(expr=   7*m.b196 + m.x636 - m.x850 <= 7)

m.c884 = Constraint(expr=   7*m.b197 + m.x636 - m.x851 <= 7)

m.c885 = Constraint(expr=   7*m.b198 + m.x636 - m.x852 <= 7)

m.c886 = Constraint(expr=   7*m.b199 + m.x636 - m.x853 <= 7)

m.c887 = Constraint(expr=   7*m.b200 + m.x636 - m.x854 <= 7)

m.c888 = Constraint(expr=   7*m.b201 + m.x637 - m.x855 <= 7)

m.c889 = Constraint(expr=   7*m.b202 + m.x637 - m.x856 <= 7)

m.c890 = Constraint(expr=   7*m.b203 + m.x637 - m.x857 <= 7)

m.c891 = Constraint(expr=   7*m.b204 + m.x637 - m.x858 <= 7)

m.c892 = Constraint(expr=   7*m.b205 + m.x637 - m.x859 <= 7)

m.c893 = Constraint(expr= - 7*m.b1 + m.x638 - m.x860 >= -7)

m.c894 = Constraint(expr= - 7*m.b2 + m.x638 - m.x861 >= -7)

m.c895 = Constraint(expr= - 7*m.b3 + m.x638 - m.x862 >= -7)

m.c896 = Constraint(expr= - 7*m.b4 + m.x638 - m.x863 >= -7)

m.c897 = Constraint(expr= - 7*m.b5 + m.x638 - m.x864 >= -7)

m.c898 = Constraint(expr= - 7*m.b6 + m.x638 - m.x865 >= -7)

m.c899 = Constraint(expr= - 7*m.b7 + m.x638 - m.x866 >= -7)

m.c900 = Constraint(expr= - 7*m.b8 + m.x638 - m.x867 >= -7)

m.c901 = Constraint(expr= - 7*m.b9 + m.x638 - m.x868 >= -7)

m.c902 = Constraint(expr= - 7*m.b10 + m.x638 - m.x869 >= -7)

m.c903 = Constraint(expr= - 7*m.b11 + m.x638 - m.x870 >= -7)

m.c904 = Constraint(expr= - 7*m.b12 + m.x638 - m.x871 >= -7)

m.c905 = Constraint(expr= - 7*m.b13 + m.x638 - m.x872 >= -7)

m.c906 = Constraint(expr= - 7*m.b14 + m.x638 - m.x873 >= -7)

m.c907 = Constraint(expr= - 7*m.b15 + m.x638 - m.x874 >= -7)

m.c908 = Constraint(expr= - 7*m.b16 + m.x639 - m.x875 >= -7)

m.c909 = Constraint(expr= - 7*m.b17 + m.x639 - m.x876 >= -7)

m.c910 = Constraint(expr= - 7*m.b18 + m.x639 - m.x877 >= -7)

m.c911 = Constraint(expr= - 7*m.b19 + m.x639 - m.x878 >= -7)

m.c912 = Constraint(expr= - 7*m.b20 + m.x639 - m.x879 >= -7)

m.c913 = Constraint(expr= - 7*m.b21 + m.x639 - m.x880 >= -7)

m.c914 = Constraint(expr= - 7*m.b22 + m.x639 - m.x881 >= -7)

m.c915 = Constraint(expr= - 7*m.b23 + m.x639 - m.x882 >= -7)

m.c916 = Constraint(expr= - 7*m.b24 + m.x639 - m.x883 >= -7)

m.c917 = Constraint(expr= - 7*m.b25 + m.x639 - m.x884 >= -7)

m.c918 = Constraint(expr= - 7*m.b26 + m.x639 - m.x885 >= -7)

m.c919 = Constraint(expr= - 7*m.b27 + m.x639 - m.x886 >= -7)

m.c920 = Constraint(expr= - 7*m.b28 + m.x639 - m.x887 >= -7)

m.c921 = Constraint(expr= - 7*m.b29 + m.x639 - m.x888 >= -7)

m.c922 = Constraint(expr= - 7*m.b30 + m.x639 - m.x889 >= -7)

m.c923 = Constraint(expr= - 7*m.b31 + m.x640 - m.x890 >= -7)

m.c924 = Constraint(expr= - 7*m.b32 + m.x640 - m.x891 >= -7)

m.c925 = Constraint(expr= - 7*m.b33 + m.x640 - m.x892 >= -7)

m.c926 = Constraint(expr= - 7*m.b34 + m.x640 - m.x893 >= -7)

m.c927 = Constraint(expr= - 7*m.b35 + m.x640 - m.x894 >= -7)

m.c928 = Constraint(expr= - 7*m.b36 + m.x640 - m.x895 >= -7)

m.c929 = Constraint(expr= - 7*m.b37 + m.x640 - m.x896 >= -7)

m.c930 = Constraint(expr= - 7*m.b38 + m.x640 - m.x897 >= -7)

m.c931 = Constraint(expr= - 7*m.b39 + m.x640 - m.x898 >= -7)

m.c932 = Constraint(expr= - 7*m.b40 + m.x640 - m.x899 >= -7)

m.c933 = Constraint(expr= - 7*m.b41 + m.x640 - m.x900 >= -7)

m.c934 = Constraint(expr= - 7*m.b42 + m.x640 - m.x901 >= -7)

m.c935 = Constraint(expr= - 7*m.b43 + m.x640 - m.x902 >= -7)

m.c936 = Constraint(expr= - 7*m.b44 + m.x640 - m.x903 >= -7)

m.c937 = Constraint(expr= - 7*m.b45 + m.x640 - m.x904 >= -7)

m.c938 = Constraint(expr= - 7*m.b46 + m.x641 - m.x905 >= -7)

m.c939 = Constraint(expr= - 7*m.b47 + m.x641 - m.x906 >= -7)

m.c940 = Constraint(expr= - 7*m.b48 + m.x641 - m.x907 >= -7)

m.c941 = Constraint(expr= - 7*m.b49 + m.x641 - m.x908 >= -7)

m.c942 = Constraint(expr= - 7*m.b50 + m.x641 - m.x909 >= -7)

m.c943 = Constraint(expr= - 7*m.b51 + m.x641 - m.x910 >= -7)

m.c944 = Constraint(expr= - 7*m.b52 + m.x641 - m.x911 >= -7)

m.c945 = Constraint(expr= - 7*m.b53 + m.x641 - m.x912 >= -7)

m.c946 = Constraint(expr= - 7*m.b54 + m.x641 - m.x913 >= -7)

m.c947 = Constraint(expr= - 7*m.b55 + m.x641 - m.x914 >= -7)

m.c948 = Constraint(expr= - 7*m.b56 + m.x641 - m.x915 >= -7)

m.c949 = Constraint(expr= - 7*m.b57 + m.x641 - m.x916 >= -7)

m.c950 = Constraint(expr= - 7*m.b58 + m.x641 - m.x917 >= -7)

m.c951 = Constraint(expr= - 7*m.b59 + m.x641 - m.x918 >= -7)

m.c952 = Constraint(expr= - 7*m.b60 + m.x641 - m.x919 >= -7)

m.c953 = Constraint(expr= - 7*m.b61 + m.x642 - m.x920 >= -7)

m.c954 = Constraint(expr= - 7*m.b62 + m.x642 - m.x921 >= -7)

m.c955 = Constraint(expr= - 7*m.b63 + m.x642 - m.x922 >= -7)

m.c956 = Constraint(expr= - 7*m.b64 + m.x642 - m.x923 >= -7)

m.c957 = Constraint(expr= - 7*m.b65 + m.x642 - m.x924 >= -7)

m.c958 = Constraint(expr= - 7*m.b66 + m.x642 - m.x925 >= -7)

m.c959 = Constraint(expr= - 7*m.b67 + m.x642 - m.x926 >= -7)

m.c960 = Constraint(expr= - 7*m.b68 + m.x642 - m.x927 >= -7)

m.c961 = Constraint(expr= - 7*m.b69 + m.x642 - m.x928 >= -7)

m.c962 = Constraint(expr= - 7*m.b70 + m.x642 - m.x929 >= -7)

m.c963 = Constraint(expr= - 7*m.b71 + m.x642 - m.x930 >= -7)

m.c964 = Constraint(expr= - 7*m.b72 + m.x642 - m.x931 >= -7)

m.c965 = Constraint(expr= - 7*m.b73 + m.x642 - m.x932 >= -7)

m.c966 = Constraint(expr= - 7*m.b74 + m.x642 - m.x933 >= -7)

m.c967 = Constraint(expr= - 7*m.b75 + m.x642 - m.x934 >= -7)

m.c968 = Constraint(expr= - 7*m.b76 + m.x643 - m.x935 >= -7)

m.c969 = Constraint(expr= - 7*m.b77 + m.x643 - m.x936 >= -7)

m.c970 = Constraint(expr= - 7*m.b78 + m.x643 - m.x937 >= -7)

m.c971 = Constraint(expr= - 7*m.b79 + m.x643 - m.x938 >= -7)

m.c972 = Constraint(expr= - 7*m.b80 + m.x643 - m.x939 >= -7)

m.c973 = Constraint(expr= - 7*m.b81 + m.x643 - m.x940 >= -7)

m.c974 = Constraint(expr= - 7*m.b82 + m.x643 - m.x941 >= -7)

m.c975 = Constraint(expr= - 7*m.b83 + m.x643 - m.x942 >= -7)

m.c976 = Constraint(expr= - 7*m.b84 + m.x643 - m.x943 >= -7)

m.c977 = Constraint(expr= - 7*m.b85 + m.x643 - m.x944 >= -7)

m.c978 = Constraint(expr= - 7*m.b86 + m.x643 - m.x945 >= -7)

m.c979 = Constraint(expr= - 7*m.b87 + m.x643 - m.x946 >= -7)

m.c980 = Constraint(expr= - 7*m.b88 + m.x643 - m.x947 >= -7)

m.c981 = Constraint(expr= - 7*m.b89 + m.x643 - m.x948 >= -7)

m.c982 = Constraint(expr= - 7*m.b90 + m.x643 - m.x949 >= -7)

m.c983 = Constraint(expr= - 7*m.b91 + m.x644 - m.x950 >= -7)

m.c984 = Constraint(expr= - 7*m.b92 + m.x644 - m.x951 >= -7)

m.c985 = Constraint(expr= - 7*m.b93 + m.x644 - m.x952 >= -7)

m.c986 = Constraint(expr= - 7*m.b94 + m.x644 - m.x953 >= -7)

m.c987 = Constraint(expr= - 7*m.b95 + m.x644 - m.x954 >= -7)

m.c988 = Constraint(expr= - 7*m.b96 + m.x644 - m.x955 >= -7)

m.c989 = Constraint(expr= - 7*m.b97 + m.x644 - m.x956 >= -7)

m.c990 = Constraint(expr= - 7*m.b98 + m.x644 - m.x957 >= -7)

m.c991 = Constraint(expr= - 7*m.b99 + m.x644 - m.x958 >= -7)

m.c992 = Constraint(expr= - 7*m.b100 + m.x644 - m.x959 >= -7)

m.c993 = Constraint(expr= - 7*m.b101 + m.x644 - m.x960 >= -7)

m.c994 = Constraint(expr= - 7*m.b102 + m.x644 - m.x961 >= -7)

m.c995 = Constraint(expr= - 7*m.b103 + m.x644 - m.x962 >= -7)

m.c996 = Constraint(expr= - 7*m.b104 + m.x644 - m.x963 >= -7)

m.c997 = Constraint(expr= - 7*m.b105 + m.x644 - m.x964 >= -7)

m.c998 = Constraint(expr= - 7*m.b106 + m.x645 - m.x965 >= -7)

m.c999 = Constraint(expr= - 7*m.b107 + m.x645 - m.x966 >= -7)

m.c1000 = Constraint(expr= - 7*m.b108 + m.x645 - m.x967 >= -7)

m.c1001 = Constraint(expr= - 7*m.b109 + m.x645 - m.x968 >= -7)

m.c1002 = Constraint(expr= - 7*m.b110 + m.x645 - m.x969 >= -7)

m.c1003 = Constraint(expr= - 7*m.b111 + m.x645 - m.x970 >= -7)

m.c1004 = Constraint(expr= - 7*m.b112 + m.x645 - m.x971 >= -7)

m.c1005 = Constraint(expr= - 7*m.b113 + m.x645 - m.x972 >= -7)

m.c1006 = Constraint(expr= - 7*m.b114 + m.x645 - m.x973 >= -7)

m.c1007 = Constraint(expr= - 7*m.b115 + m.x645 - m.x974 >= -7)

m.c1008 = Constraint(expr= - 7*m.b116 + m.x645 - m.x975 >= -7)

m.c1009 = Constraint(expr= - 7*m.b117 + m.x645 - m.x976 >= -7)

m.c1010 = Constraint(expr= - 7*m.b118 + m.x645 - m.x977 >= -7)

m.c1011 = Constraint(expr= - 7*m.b119 + m.x645 - m.x978 >= -7)

m.c1012 = Constraint(expr= - 7*m.b120 + m.x645 - m.x979 >= -7)

m.c1013 = Constraint(expr= - 7*m.b121 + m.x646 - m.x980 >= -7)

m.c1014 = Constraint(expr= - 7*m.b122 + m.x646 - m.x981 >= -7)

m.c1015 = Constraint(expr= - 7*m.b123 + m.x646 - m.x982 >= -7)

m.c1016 = Constraint(expr= - 7*m.b124 + m.x646 - m.x983 >= -7)

m.c1017 = Constraint(expr= - 7*m.b125 + m.x646 - m.x984 >= -7)

m.c1018 = Constraint(expr= - 7*m.b126 + m.x646 - m.x985 >= -7)

m.c1019 = Constraint(expr= - 7*m.b127 + m.x646 - m.x986 >= -7)

m.c1020 = Constraint(expr= - 7*m.b128 + m.x646 - m.x987 >= -7)

m.c1021 = Constraint(expr= - 7*m.b129 + m.x646 - m.x988 >= -7)

m.c1022 = Constraint(expr= - 7*m.b130 + m.x646 - m.x989 >= -7)

m.c1023 = Constraint(expr= - 7*m.b131 + m.x646 - m.x990 >= -7)

m.c1024 = Constraint(expr= - 7*m.b132 + m.x646 - m.x991 >= -7)

m.c1025 = Constraint(expr= - 7*m.b133 + m.x646 - m.x992 >= -7)

m.c1026 = Constraint(expr= - 7*m.b134 + m.x646 - m.x993 >= -7)

m.c1027 = Constraint(expr= - 7*m.b135 + m.x646 - m.x994 >= -7)

m.c1028 = Constraint(expr= - 7*m.b136 + m.x647 - m.x995 >= -7)

m.c1029 = Constraint(expr= - 7*m.b137 + m.x647 - m.x996 >= -7)

m.c1030 = Constraint(expr= - 7*m.b138 + m.x647 - m.x997 >= -7)

m.c1031 = Constraint(expr= - 7*m.b139 + m.x647 - m.x998 >= -7)

m.c1032 = Constraint(expr= - 7*m.b140 + m.x647 - m.x999 >= -7)

m.c1033 = Constraint(expr= - 7*m.b141 + m.x647 - m.x1000 >= -7)

m.c1034 = Constraint(expr= - 7*m.b142 + m.x647 - m.x1001 >= -7)

m.c1035 = Constraint(expr= - 7*m.b143 + m.x647 - m.x1002 >= -7)

m.c1036 = Constraint(expr= - 7*m.b144 + m.x647 - m.x1003 >= -7)

m.c1037 = Constraint(expr= - 7*m.b145 + m.x647 - m.x1004 >= -7)

m.c1038 = Constraint(expr= - 7*m.b146 + m.x648 - m.x1005 >= -7)

m.c1039 = Constraint(expr= - 7*m.b147 + m.x648 - m.x1006 >= -7)

m.c1040 = Constraint(expr= - 7*m.b148 + m.x648 - m.x1007 >= -7)

m.c1041 = Constraint(expr= - 7*m.b149 + m.x648 - m.x1008 >= -7)

m.c1042 = Constraint(expr= - 7*m.b150 + m.x648 - m.x1009 >= -7)

m.c1043 = Constraint(expr= - 7*m.b151 + m.x649 - m.x1010 >= -7)

m.c1044 = Constraint(expr= - 7*m.b152 + m.x649 - m.x1011 >= -7)

m.c1045 = Constraint(expr= - 7*m.b153 + m.x649 - m.x1012 >= -7)

m.c1046 = Constraint(expr= - 7*m.b154 + m.x649 - m.x1013 >= -7)

m.c1047 = Constraint(expr= - 7*m.b155 + m.x649 - m.x1014 >= -7)

m.c1048 = Constraint(expr= - 7*m.b156 + m.x649 - m.x1015 >= -7)

m.c1049 = Constraint(expr= - 7*m.b157 + m.x649 - m.x1016 >= -7)

m.c1050 = Constraint(expr= - 7*m.b158 + m.x649 - m.x1017 >= -7)

m.c1051 = Constraint(expr= - 7*m.b159 + m.x649 - m.x1018 >= -7)

m.c1052 = Constraint(expr= - 7*m.b160 + m.x649 - m.x1019 >= -7)

m.c1053 = Constraint(expr= - 7*m.b161 + m.x650 - m.x1020 >= -7)

m.c1054 = Constraint(expr= - 7*m.b162 + m.x650 - m.x1021 >= -7)

m.c1055 = Constraint(expr= - 7*m.b163 + m.x650 - m.x1022 >= -7)

m.c1056 = Constraint(expr= - 7*m.b164 + m.x650 - m.x1023 >= -7)

m.c1057 = Constraint(expr= - 7*m.b165 + m.x650 - m.x1024 >= -7)

m.c1058 = Constraint(expr= - 7*m.b166 + m.x651 - m.x1025 >= -7)

m.c1059 = Constraint(expr= - 7*m.b167 + m.x651 - m.x1026 >= -7)

m.c1060 = Constraint(expr= - 7*m.b168 + m.x651 - m.x1027 >= -7)

m.c1061 = Constraint(expr= - 7*m.b169 + m.x651 - m.x1028 >= -7)

m.c1062 = Constraint(expr= - 7*m.b170 + m.x651 - m.x1029 >= -7)

m.c1063 = Constraint(expr= - 7*m.b171 + m.x651 - m.x1030 >= -7)

m.c1064 = Constraint(expr= - 7*m.b172 + m.x651 - m.x1031 >= -7)

m.c1065 = Constraint(expr= - 7*m.b173 + m.x651 - m.x1032 >= -7)

m.c1066 = Constraint(expr= - 7*m.b174 + m.x651 - m.x1033 >= -7)

m.c1067 = Constraint(expr= - 7*m.b175 + m.x651 - m.x1034 >= -7)

m.c1068 = Constraint(expr= - 7*m.b176 + m.x651 - m.x1035 >= -7)

m.c1069 = Constraint(expr= - 7*m.b177 + m.x651 - m.x1036 >= -7)

m.c1070 = Constraint(expr= - 7*m.b178 + m.x651 - m.x1037 >= -7)

m.c1071 = Constraint(expr= - 7*m.b179 + m.x651 - m.x1038 >= -7)

m.c1072 = Constraint(expr= - 7*m.b180 + m.x651 - m.x1039 >= -7)

m.c1073 = Constraint(expr= - 7*m.b181 + m.x652 - m.x1040 >= -7)

m.c1074 = Constraint(expr= - 7*m.b182 + m.x652 - m.x1041 >= -7)

m.c1075 = Constraint(expr= - 7*m.b183 + m.x652 - m.x1042 >= -7)

m.c1076 = Constraint(expr= - 7*m.b184 + m.x652 - m.x1043 >= -7)

m.c1077 = Constraint(expr= - 7*m.b185 + m.x652 - m.x1044 >= -7)

m.c1078 = Constraint(expr= - 7*m.b186 + m.x652 - m.x1045 >= -7)

m.c1079 = Constraint(expr= - 7*m.b187 + m.x652 - m.x1046 >= -7)

m.c1080 = Constraint(expr= - 7*m.b188 + m.x652 - m.x1047 >= -7)

m.c1081 = Constraint(expr= - 7*m.b189 + m.x652 - m.x1048 >= -7)

m.c1082 = Constraint(expr= - 7*m.b190 + m.x652 - m.x1049 >= -7)

m.c1083 = Constraint(expr= - 7*m.b191 + m.x652 - m.x1050 >= -7)

m.c1084 = Constraint(expr= - 7*m.b192 + m.x652 - m.x1051 >= -7)

m.c1085 = Constraint(expr= - 7*m.b193 + m.x652 - m.x1052 >= -7)

m.c1086 = Constraint(expr= - 7*m.b194 + m.x652 - m.x1053 >= -7)

m.c1087 = Constraint(expr= - 7*m.b195 + m.x652 - m.x1054 >= -7)

m.c1088 = Constraint(expr= - 7*m.b196 + m.x653 - m.x1055 >= -7)

m.c1089 = Constraint(expr= - 7*m.b197 + m.x653 - m.x1056 >= -7)

m.c1090 = Constraint(expr= - 7*m.b198 + m.x653 - m.x1057 >= -7)

m.c1091 = Constraint(expr= - 7*m.b199 + m.x653 - m.x1058 >= -7)

m.c1092 = Constraint(expr= - 7*m.b200 + m.x653 - m.x1059 >= -7)

m.c1093 = Constraint(expr= - 7*m.b201 + m.x654 - m.x1060 >= -7)

m.c1094 = Constraint(expr= - 7*m.b202 + m.x654 - m.x1061 >= -7)

m.c1095 = Constraint(expr= - 7*m.b203 + m.x654 - m.x1062 >= -7)

m.c1096 = Constraint(expr= - 7*m.b204 + m.x654 - m.x1063 >= -7)

m.c1097 = Constraint(expr= - 7*m.b205 + m.x654 - m.x1064 >= -7)

m.c1098 = Constraint(expr= - m.x1165 + m.x1200 == 0)

m.c1099 = Constraint(expr= - m.x1166 + m.x1201 == 0)

m.c1100 = Constraint(expr= - m.x1167 + m.x1202 == 0)

m.c1101 = Constraint(expr= - m.x1168 + m.x1203 == 0)

m.c1102 = Constraint(expr= - m.x1169 + m.x1204 == 0)

m.c1103 = Constraint(expr= - m.x1170 + m.x1205 == 0)

m.c1104 = Constraint(expr= - m.x1171 + m.x1206 == 0)

m.c1105 = Constraint(expr= - m.x1172 + m.x1207 == 0)

m.c1106 = Constraint(expr= - m.x1173 + m.x1208 == 0)

m.c1107 = Constraint(expr= - m.x1174 + m.x1209 == 0)

m.c1108 = Constraint(expr= - m.x1175 + m.x1210 == 0)

m.c1109 = Constraint(expr= - m.x1176 + m.x1211 == 0)

m.c1110 = Constraint(expr= - m.x1177 + m.x1212 == 0)

m.c1111 = Constraint(expr= - m.x1178 + m.x1213 == 0)

m.c1112 = Constraint(expr= - m.x1179 + m.x1214 == 0)

m.c1113 = Constraint(expr= - m.x1180 + m.x1215 == 0)

m.c1114 = Constraint(expr= - m.x1181 + m.x1216 == 0)

m.c1115 = Constraint(expr= - m.x1182 + m.x1217 == 0)

m.c1116 = Constraint(expr= - m.x1183 + m.x1218 == 0)

m.c1117 = Constraint(expr= - m.x1184 + m.x1219 == 0)

m.c1118 = Constraint(expr= - m.x1185 + m.x1220 == 0)

m.c1119 = Constraint(expr= - m.x1186 + m.x1221 == 0)

m.c1120 = Constraint(expr= - m.x1187 + m.x1222 == 0)

m.c1121 = Constraint(expr= - m.x1188 + m.x1223 == 0)

m.c1122 = Constraint(expr= - m.x1189 + m.x1224 == 0)

m.c1123 = Constraint(expr= - m.x1190 + m.x1225 + m.x1230 + m.x1235 == 0)

m.c1124 = Constraint(expr= - m.x1191 + m.x1226 + m.x1231 + m.x1236 == 0)

m.c1125 = Constraint(expr= - m.x1192 + m.x1227 + m.x1232 + m.x1237 == 0)

m.c1126 = Constraint(expr= - m.x1193 + m.x1228 + m.x1233 + m.x1238 == 0)

m.c1127 = Constraint(expr= - m.x1194 + m.x1229 + m.x1234 + m.x1239 == 0)

m.c1128 = Constraint(expr= - m.x1195 + m.x1240 == 0)

m.c1129 = Constraint(expr= - m.x1196 + m.x1241 == 0)

m.c1130 = Constraint(expr= - m.x1197 + m.x1242 == 0)

m.c1131 = Constraint(expr= - m.x1198 + m.x1243 == 0)

m.c1132 = Constraint(expr= - m.x1199 + m.x1244 == 0)

m.c1133 = Constraint(expr=   m.x1165 - m.x1200 <= 0)

m.c1134 = Constraint(expr=   m.x1166 - m.x1201 <= 0)

m.c1135 = Constraint(expr=   m.x1167 - m.x1202 <= 0)

m.c1136 = Constraint(expr=   m.x1168 - m.x1203 <= 0)

m.c1137 = Constraint(expr=   m.x1169 - m.x1204 <= 0)

m.c1138 = Constraint(expr=   m.x1170 - m.x1205 <= 0)

m.c1139 = Constraint(expr=   m.x1171 - m.x1206 <= 0)

m.c1140 = Constraint(expr=   m.x1172 - m.x1207 <= 0)

m.c1141 = Constraint(expr=   m.x1173 - m.x1208 <= 0)

m.c1142 = Constraint(expr=   m.x1174 - m.x1209 <= 0)

m.c1143 = Constraint(expr=   m.x1175 - m.x1210 <= 0)

m.c1144 = Constraint(expr=   m.x1176 - m.x1211 <= 0)

m.c1145 = Constraint(expr=   m.x1177 - m.x1212 <= 0)

m.c1146 = Constraint(expr=   m.x1178 - m.x1213 <= 0)

m.c1147 = Constraint(expr=   m.x1179 - m.x1214 <= 0)

m.c1148 = Constraint(expr=   m.x1180 - m.x1215 <= 0)

m.c1149 = Constraint(expr=   m.x1181 - m.x1216 <= 0)

m.c1150 = Constraint(expr=   m.x1182 - m.x1217 <= 0)

m.c1151 = Constraint(expr=   m.x1183 - m.x1218 <= 0)

m.c1152 = Constraint(expr=   m.x1184 - m.x1219 <= 0)

m.c1153 = Constraint(expr=   m.x1185 - m.x1220 <= 0)

m.c1154 = Constraint(expr=   m.x1186 - m.x1221 <= 0)

m.c1155 = Constraint(expr=   m.x1187 - m.x1222 <= 0)

m.c1156 = Constraint(expr=   m.x1188 - m.x1223 <= 0)

m.c1157 = Constraint(expr=   m.x1189 - m.x1224 <= 0)

m.c1158 = Constraint(expr=   m.x1195 - m.x1240 <= 0)

m.c1159 = Constraint(expr=   m.x1196 - m.x1241 <= 0)

m.c1160 = Constraint(expr=   m.x1197 - m.x1242 <= 0)

m.c1161 = Constraint(expr=   m.x1198 - m.x1243 <= 0)

m.c1162 = Constraint(expr=   m.x1199 - m.x1244 <= 0)

m.c1163 = Constraint(expr= - m.x326 + m.x361 == 0)

m.c1164 = Constraint(expr= - m.x327 + m.x362 == 0)

m.c1165 = Constraint(expr= - m.x328 + m.x363 == 0)

m.c1166 = Constraint(expr= - m.x329 + m.x364 == 0)

m.c1167 = Constraint(expr= - m.x330 + m.x365 == 0)

m.c1168 = Constraint(expr= - m.x331 + m.x366 == 0)

m.c1169 = Constraint(expr= - m.x332 + m.x367 == 0)

m.c1170 = Constraint(expr= - m.x333 + m.x368 == 0)

m.c1171 = Constraint(expr= - m.x334 + m.x369 == 0)

m.c1172 = Constraint(expr= - m.x335 + m.x370 == 0)

m.c1173 = Constraint(expr= - m.x336 + m.x371 == 0)

m.c1174 = Constraint(expr= - m.x337 + m.x372 == 0)

m.c1175 = Constraint(expr= - m.x338 + m.x373 == 0)

m.c1176 = Constraint(expr= - m.x339 + m.x374 == 0)

m.c1177 = Constraint(expr= - m.x340 + m.x375 == 0)

m.c1178 = Constraint(expr= - m.x341 + m.x376 == 0)

m.c1179 = Constraint(expr= - m.x342 + m.x377 == 0)

m.c1180 = Constraint(expr= - m.x343 + m.x378 == 0)

m.c1181 = Constraint(expr= - m.x344 + m.x379 == 0)

m.c1182 = Constraint(expr= - m.x345 + m.x380 == 0)

m.c1183 = Constraint(expr= - m.x346 + m.x381 == 0)

m.c1184 = Constraint(expr= - m.x347 + m.x382 == 0)

m.c1185 = Constraint(expr= - m.x348 + m.x383 == 0)

m.c1186 = Constraint(expr= - m.x349 + m.x384 == 0)

m.c1187 = Constraint(expr= - m.x350 + m.x385 == 0)

m.c1188 = Constraint(expr= - 0.5*m.x351 + m.x386 == 0)

m.c1189 = Constraint(expr= - 0.5*m.x352 + m.x387 == 0)

m.c1190 = Constraint(expr= - 0.25*m.x351 + m.x391 == 0)

m.c1191 = Constraint(expr= - 0.25*m.x352 + m.x392 == 0)

m.c1192 = Constraint(expr= - 0.25*m.x351 + m.x396 == 0)

m.c1193 = Constraint(expr= - 0.25*m.x352 + m.x397 == 0)

m.c1194 = Constraint(expr= - m.x356 + m.x401 == 0)

m.c1195 = Constraint(expr= - m.x357 + m.x402 == 0)

m.c1196 = Constraint(expr= - m.x358 + m.x403 == 0)

m.c1197 = Constraint(expr= - m.x359 + m.x404 == 0)

m.c1198 = Constraint(expr= - m.x360 + m.x405 == 0)

m.c1199 = Constraint(expr=   m.b1 + m.b291 <= 1)

m.c1200 = Constraint(expr=   m.b2 + m.b292 <= 1)

m.c1201 = Constraint(expr=   m.b3 + m.b293 <= 1)

m.c1202 = Constraint(expr=   m.b4 + m.b294 <= 1)

m.c1203 = Constraint(expr=   m.b5 + m.b295 <= 1)

m.c1204 = Constraint(expr=   m.b6 + m.b306 <= 1)

m.c1205 = Constraint(expr=   m.b7 + m.b307 <= 1)

m.c1206 = Constraint(expr=   m.b8 + m.b308 <= 1)

m.c1207 = Constraint(expr=   m.b9 + m.b309 <= 1)

m.c1208 = Constraint(expr=   m.b10 + m.b310 <= 1)

m.c1209 = Constraint(expr=   m.b11 + m.b311 <= 1)

m.c1210 = Constraint(expr=   m.b12 + m.b312 <= 1)

m.c1211 = Constraint(expr=   m.b13 + m.b313 <= 1)

m.c1212 = Constraint(expr=   m.b14 + m.b314 <= 1)

m.c1213 = Constraint(expr=   m.b15 + m.b315 <= 1)

m.c1214 = Constraint(expr=   m.b16 + m.b291 <= 1)

m.c1215 = Constraint(expr=   m.b17 + m.b292 <= 1)

m.c1216 = Constraint(expr=   m.b18 + m.b293 <= 1)

m.c1217 = Constraint(expr=   m.b19 + m.b294 <= 1)

m.c1218 = Constraint(expr=   m.b20 + m.b295 <= 1)

m.c1219 = Constraint(expr=   m.b21 + m.b306 <= 1)

m.c1220 = Constraint(expr=   m.b22 + m.b307 <= 1)

m.c1221 = Constraint(expr=   m.b23 + m.b308 <= 1)

m.c1222 = Constraint(expr=   m.b24 + m.b309 <= 1)

m.c1223 = Constraint(expr=   m.b25 + m.b310 <= 1)

m.c1224 = Constraint(expr=   m.b26 + m.b311 <= 1)

m.c1225 = Constraint(expr=   m.b27 + m.b312 <= 1)

m.c1226 = Constraint(expr=   m.b28 + m.b313 <= 1)

m.c1227 = Constraint(expr=   m.b29 + m.b314 <= 1)

m.c1228 = Constraint(expr=   m.b30 + m.b315 <= 1)

m.c1229 = Constraint(expr=   m.b31 + m.b291 <= 1)

m.c1230 = Constraint(expr=   m.b32 + m.b292 <= 1)

m.c1231 = Constraint(expr=   m.b33 + m.b293 <= 1)

m.c1232 = Constraint(expr=   m.b34 + m.b294 <= 1)

m.c1233 = Constraint(expr=   m.b35 + m.b295 <= 1)

m.c1234 = Constraint(expr=   m.b36 + m.b306 <= 1)

m.c1235 = Constraint(expr=   m.b37 + m.b307 <= 1)

m.c1236 = Constraint(expr=   m.b38 + m.b308 <= 1)

m.c1237 = Constraint(expr=   m.b39 + m.b309 <= 1)

m.c1238 = Constraint(expr=   m.b40 + m.b310 <= 1)

m.c1239 = Constraint(expr=   m.b41 + m.b311 <= 1)

m.c1240 = Constraint(expr=   m.b42 + m.b312 <= 1)

m.c1241 = Constraint(expr=   m.b43 + m.b313 <= 1)

m.c1242 = Constraint(expr=   m.b44 + m.b314 <= 1)

m.c1243 = Constraint(expr=   m.b45 + m.b315 <= 1)

m.c1244 = Constraint(expr=   m.b46 + m.b291 <= 1)

m.c1245 = Constraint(expr=   m.b47 + m.b292 <= 1)

m.c1246 = Constraint(expr=   m.b48 + m.b293 <= 1)

m.c1247 = Constraint(expr=   m.b49 + m.b294 <= 1)

m.c1248 = Constraint(expr=   m.b50 + m.b295 <= 1)

m.c1249 = Constraint(expr=   m.b51 + m.b306 <= 1)

m.c1250 = Constraint(expr=   m.b52 + m.b307 <= 1)

m.c1251 = Constraint(expr=   m.b53 + m.b308 <= 1)

m.c1252 = Constraint(expr=   m.b54 + m.b309 <= 1)

m.c1253 = Constraint(expr=   m.b55 + m.b310 <= 1)

m.c1254 = Constraint(expr=   m.b56 + m.b311 <= 1)

m.c1255 = Constraint(expr=   m.b57 + m.b312 <= 1)

m.c1256 = Constraint(expr=   m.b58 + m.b313 <= 1)

m.c1257 = Constraint(expr=   m.b59 + m.b314 <= 1)

m.c1258 = Constraint(expr=   m.b60 + m.b315 <= 1)

m.c1259 = Constraint(expr=   m.b61 + m.b291 <= 1)

m.c1260 = Constraint(expr=   m.b62 + m.b292 <= 1)

m.c1261 = Constraint(expr=   m.b63 + m.b293 <= 1)

m.c1262 = Constraint(expr=   m.b64 + m.b294 <= 1)

m.c1263 = Constraint(expr=   m.b65 + m.b295 <= 1)

m.c1264 = Constraint(expr=   m.b66 + m.b306 <= 1)

m.c1265 = Constraint(expr=   m.b67 + m.b307 <= 1)

m.c1266 = Constraint(expr=   m.b68 + m.b308 <= 1)

m.c1267 = Constraint(expr=   m.b69 + m.b309 <= 1)

m.c1268 = Constraint(expr=   m.b70 + m.b310 <= 1)

m.c1269 = Constraint(expr=   m.b71 + m.b311 <= 1)

m.c1270 = Constraint(expr=   m.b72 + m.b312 <= 1)

m.c1271 = Constraint(expr=   m.b73 + m.b313 <= 1)

m.c1272 = Constraint(expr=   m.b74 + m.b314 <= 1)

m.c1273 = Constraint(expr=   m.b75 + m.b315 <= 1)

m.c1274 = Constraint(expr=   m.b76 + m.b291 <= 1)

m.c1275 = Constraint(expr=   m.b77 + m.b292 <= 1)

m.c1276 = Constraint(expr=   m.b78 + m.b293 <= 1)

m.c1277 = Constraint(expr=   m.b79 + m.b294 <= 1)

m.c1278 = Constraint(expr=   m.b80 + m.b295 <= 1)

m.c1279 = Constraint(expr=   m.b81 + m.b306 <= 1)

m.c1280 = Constraint(expr=   m.b82 + m.b307 <= 1)

m.c1281 = Constraint(expr=   m.b83 + m.b308 <= 1)

m.c1282 = Constraint(expr=   m.b84 + m.b309 <= 1)

m.c1283 = Constraint(expr=   m.b85 + m.b310 <= 1)

m.c1284 = Constraint(expr=   m.b86 + m.b311 <= 1)

m.c1285 = Constraint(expr=   m.b87 + m.b312 <= 1)

m.c1286 = Constraint(expr=   m.b88 + m.b313 <= 1)

m.c1287 = Constraint(expr=   m.b89 + m.b314 <= 1)

m.c1288 = Constraint(expr=   m.b90 + m.b315 <= 1)

m.c1289 = Constraint(expr=   m.b91 + m.b291 <= 1)

m.c1290 = Constraint(expr=   m.b92 + m.b292 <= 1)

m.c1291 = Constraint(expr=   m.b93 + m.b293 <= 1)

m.c1292 = Constraint(expr=   m.b94 + m.b294 <= 1)

m.c1293 = Constraint(expr=   m.b95 + m.b295 <= 1)

m.c1294 = Constraint(expr=   m.b96 + m.b306 <= 1)

m.c1295 = Constraint(expr=   m.b97 + m.b307 <= 1)

m.c1296 = Constraint(expr=   m.b98 + m.b308 <= 1)

m.c1297 = Constraint(expr=   m.b99 + m.b309 <= 1)

m.c1298 = Constraint(expr=   m.b100 + m.b310 <= 1)

m.c1299 = Constraint(expr=   m.b101 + m.b311 <= 1)

m.c1300 = Constraint(expr=   m.b102 + m.b312 <= 1)

m.c1301 = Constraint(expr=   m.b103 + m.b313 <= 1)

m.c1302 = Constraint(expr=   m.b104 + m.b314 <= 1)

m.c1303 = Constraint(expr=   m.b105 + m.b315 <= 1)

m.c1304 = Constraint(expr=   m.b106 + m.b291 <= 1)

m.c1305 = Constraint(expr=   m.b107 + m.b292 <= 1)

m.c1306 = Constraint(expr=   m.b108 + m.b293 <= 1)

m.c1307 = Constraint(expr=   m.b109 + m.b294 <= 1)

m.c1308 = Constraint(expr=   m.b110 + m.b295 <= 1)

m.c1309 = Constraint(expr=   m.b111 + m.b306 <= 1)

m.c1310 = Constraint(expr=   m.b112 + m.b307 <= 1)

m.c1311 = Constraint(expr=   m.b113 + m.b308 <= 1)

m.c1312 = Constraint(expr=   m.b114 + m.b309 <= 1)

m.c1313 = Constraint(expr=   m.b115 + m.b310 <= 1)

m.c1314 = Constraint(expr=   m.b116 + m.b311 <= 1)

m.c1315 = Constraint(expr=   m.b117 + m.b312 <= 1)

m.c1316 = Constraint(expr=   m.b118 + m.b313 <= 1)

m.c1317 = Constraint(expr=   m.b119 + m.b314 <= 1)

m.c1318 = Constraint(expr=   m.b120 + m.b315 <= 1)

m.c1319 = Constraint(expr=   m.b121 + m.b291 <= 1)

m.c1320 = Constraint(expr=   m.b122 + m.b292 <= 1)

m.c1321 = Constraint(expr=   m.b123 + m.b293 <= 1)

m.c1322 = Constraint(expr=   m.b124 + m.b294 <= 1)

m.c1323 = Constraint(expr=   m.b125 + m.b295 <= 1)

m.c1324 = Constraint(expr=   m.b126 + m.b306 <= 1)

m.c1325 = Constraint(expr=   m.b127 + m.b307 <= 1)

m.c1326 = Constraint(expr=   m.b128 + m.b308 <= 1)

m.c1327 = Constraint(expr=   m.b129 + m.b309 <= 1)

m.c1328 = Constraint(expr=   m.b130 + m.b310 <= 1)

m.c1329 = Constraint(expr=   m.b131 + m.b311 <= 1)

m.c1330 = Constraint(expr=   m.b132 + m.b312 <= 1)

m.c1331 = Constraint(expr=   m.b133 + m.b313 <= 1)

m.c1332 = Constraint(expr=   m.b134 + m.b314 <= 1)

m.c1333 = Constraint(expr=   m.b135 + m.b315 <= 1)

m.c1334 = Constraint(expr=   m.b136 + m.b296 <= 1)

m.c1335 = Constraint(expr=   m.b137 + m.b297 <= 1)

m.c1336 = Constraint(expr=   m.b138 + m.b298 <= 1)

m.c1337 = Constraint(expr=   m.b139 + m.b299 <= 1)

m.c1338 = Constraint(expr=   m.b140 + m.b300 <= 1)

m.c1339 = Constraint(expr=   m.b141 + m.b316 <= 1)

m.c1340 = Constraint(expr=   m.b142 + m.b317 <= 1)

m.c1341 = Constraint(expr=   m.b143 + m.b318 <= 1)

m.c1342 = Constraint(expr=   m.b144 + m.b319 <= 1)

m.c1343 = Constraint(expr=   m.b145 + m.b320 <= 1)

m.c1344 = Constraint(expr=   m.b146 + m.b316 <= 1)

m.c1345 = Constraint(expr=   m.b147 + m.b317 <= 1)

m.c1346 = Constraint(expr=   m.b148 + m.b318 <= 1)

m.c1347 = Constraint(expr=   m.b149 + m.b319 <= 1)

m.c1348 = Constraint(expr=   m.b150 + m.b320 <= 1)

m.c1349 = Constraint(expr=   m.b151 + m.b296 <= 1)

m.c1350 = Constraint(expr=   m.b152 + m.b297 <= 1)

m.c1351 = Constraint(expr=   m.b153 + m.b298 <= 1)

m.c1352 = Constraint(expr=   m.b154 + m.b299 <= 1)

m.c1353 = Constraint(expr=   m.b155 + m.b300 <= 1)

m.c1354 = Constraint(expr=   m.b156 + m.b316 <= 1)

m.c1355 = Constraint(expr=   m.b157 + m.b317 <= 1)

m.c1356 = Constraint(expr=   m.b158 + m.b318 <= 1)

m.c1357 = Constraint(expr=   m.b159 + m.b319 <= 1)

m.c1358 = Constraint(expr=   m.b160 + m.b320 <= 1)

m.c1359 = Constraint(expr=   m.b161 + m.b316 <= 1)

m.c1360 = Constraint(expr=   m.b162 + m.b317 <= 1)

m.c1361 = Constraint(expr=   m.b163 + m.b318 <= 1)

m.c1362 = Constraint(expr=   m.b164 + m.b319 <= 1)

m.c1363 = Constraint(expr=   m.b165 + m.b320 <= 1)

m.c1364 = Constraint(expr=   m.b166 + m.b291 <= 1)

m.c1365 = Constraint(expr=   m.b167 + m.b292 <= 1)

m.c1366 = Constraint(expr=   m.b168 + m.b293 <= 1)

m.c1367 = Constraint(expr=   m.b169 + m.b294 <= 1)

m.c1368 = Constraint(expr=   m.b170 + m.b295 <= 1)

m.c1369 = Constraint(expr=   m.b171 + m.b306 <= 1)

m.c1370 = Constraint(expr=   m.b172 + m.b307 <= 1)

m.c1371 = Constraint(expr=   m.b173 + m.b308 <= 1)

m.c1372 = Constraint(expr=   m.b174 + m.b309 <= 1)

m.c1373 = Constraint(expr=   m.b175 + m.b310 <= 1)

m.c1374 = Constraint(expr=   m.b176 + m.b311 <= 1)

m.c1375 = Constraint(expr=   m.b177 + m.b312 <= 1)

m.c1376 = Constraint(expr=   m.b178 + m.b313 <= 1)

m.c1377 = Constraint(expr=   m.b179 + m.b314 <= 1)

m.c1378 = Constraint(expr=   m.b180 + m.b315 <= 1)

m.c1379 = Constraint(expr=   m.b181 + m.b291 <= 1)

m.c1380 = Constraint(expr=   m.b182 + m.b292 <= 1)

m.c1381 = Constraint(expr=   m.b183 + m.b293 <= 1)

m.c1382 = Constraint(expr=   m.b184 + m.b294 <= 1)

m.c1383 = Constraint(expr=   m.b185 + m.b295 <= 1)

m.c1384 = Constraint(expr=   m.b186 + m.b306 <= 1)

m.c1385 = Constraint(expr=   m.b187 + m.b307 <= 1)

m.c1386 = Constraint(expr=   m.b188 + m.b308 <= 1)

m.c1387 = Constraint(expr=   m.b189 + m.b309 <= 1)

m.c1388 = Constraint(expr=   m.b190 + m.b310 <= 1)

m.c1389 = Constraint(expr=   m.b191 + m.b311 <= 1)

m.c1390 = Constraint(expr=   m.b192 + m.b312 <= 1)

m.c1391 = Constraint(expr=   m.b193 + m.b313 <= 1)

m.c1392 = Constraint(expr=   m.b194 + m.b314 <= 1)

m.c1393 = Constraint(expr=   m.b195 + m.b315 <= 1)

m.c1394 = Constraint(expr=   m.b196 + m.b316 <= 1)

m.c1395 = Constraint(expr=   m.b197 + m.b317 <= 1)

m.c1396 = Constraint(expr=   m.b198 + m.b318 <= 1)

m.c1397 = Constraint(expr=   m.b199 + m.b319 <= 1)

m.c1398 = Constraint(expr=   m.b200 + m.b320 <= 1)

m.c1399 = Constraint(expr=   m.b201 + m.b316 <= 1)

m.c1400 = Constraint(expr=   m.b202 + m.b317 <= 1)

m.c1401 = Constraint(expr=   m.b203 + m.b318 <= 1)

m.c1402 = Constraint(expr=   m.b204 + m.b319 <= 1)

m.c1403 = Constraint(expr=   m.b205 + m.b320 <= 1)

m.c1404 = Constraint(expr=   m.b291 <= 2)

m.c1405 = Constraint(expr=   m.b292 <= 2)

m.c1406 = Constraint(expr=   m.b293 <= 2)

m.c1407 = Constraint(expr=   m.b294 <= 2)

m.c1408 = Constraint(expr=   m.b295 <= 2)

m.c1409 = Constraint(expr=   m.b296 <= 2)

m.c1410 = Constraint(expr=   m.b297 <= 2)

m.c1411 = Constraint(expr=   m.b298 <= 2)

m.c1412 = Constraint(expr=   m.b299 <= 2)

m.c1413 = Constraint(expr=   m.b300 <= 2)

m.c1414 = Constraint(expr=   m.b301 <= 2)

m.c1415 = Constraint(expr=   m.b302 <= 2)

m.c1416 = Constraint(expr=   m.b303 <= 2)

m.c1417 = Constraint(expr=   m.b304 <= 2)

m.c1418 = Constraint(expr=   m.b305 <= 2)

m.c1419 = Constraint(expr=   m.b306 <= 2)

m.c1420 = Constraint(expr=   m.b307 <= 2)

m.c1421 = Constraint(expr=   m.b308 <= 2)

m.c1422 = Constraint(expr=   m.b309 <= 2)

m.c1423 = Constraint(expr=   m.b310 <= 2)

m.c1424 = Constraint(expr=   m.b311 <= 2)

m.c1425 = Constraint(expr=   m.b312 <= 2)

m.c1426 = Constraint(expr=   m.b313 <= 2)

m.c1427 = Constraint(expr=   m.b314 <= 2)

m.c1428 = Constraint(expr=   m.b315 <= 2)

m.c1429 = Constraint(expr=   m.b316 <= 2)

m.c1430 = Constraint(expr=   m.b317 <= 2)

m.c1431 = Constraint(expr=   m.b318 <= 2)

m.c1432 = Constraint(expr=   m.b319 <= 2)

m.c1433 = Constraint(expr=   m.b320 <= 2)

m.c1434 = Constraint(expr=   m.b321 <= 2)

m.c1435 = Constraint(expr=   m.b322 <= 2)

m.c1436 = Constraint(expr=   m.b323 <= 2)

m.c1437 = Constraint(expr=   m.b324 <= 2)

m.c1438 = Constraint(expr=   m.b325 <= 2)

m.c1439 = Constraint(expr=   m.b291 + m.b301 + m.b306 + m.b311 + m.b321 <= 2)

m.c1440 = Constraint(expr=   m.b292 + m.b302 + m.b307 + m.b312 + m.b322 <= 2)

m.c1441 = Constraint(expr=   m.b293 + m.b303 + m.b308 + m.b313 + m.b323 <= 2)

m.c1442 = Constraint(expr=   m.b294 + m.b304 + m.b309 + m.b314 + m.b324 <= 2)

m.c1443 = Constraint(expr=   m.b295 + m.b305 + m.b310 + m.b315 + m.b325 <= 2)

m.c1444 = Constraint(expr=   m.b296 + m.b316 <= 2)

m.c1445 = Constraint(expr=   m.b297 + m.b317 <= 2)

m.c1446 = Constraint(expr=   m.b298 + m.b318 <= 2)

m.c1447 = Constraint(expr=   m.b299 + m.b319 <= 2)

m.c1448 = Constraint(expr=   m.b300 + m.b320 <= 2)

m.c1449 = Constraint(expr=   m.x326 + 5000*m.x1075 - 5000*m.x1110 <= 0)

m.c1450 = Constraint(expr=   m.x327 + 5000*m.x1076 - 5000*m.x1111 <= 0)

m.c1451 = Constraint(expr=   m.x328 + 5000*m.x1077 - 5000*m.x1112 <= 0)

m.c1452 = Constraint(expr=   m.x329 + 5000*m.x1078 - 5000*m.x1113 <= 0)

m.c1453 = Constraint(expr=   m.x330 + 5000*m.x1079 - 5000*m.x1114 <= 0)

m.c1454 = Constraint(expr=   m.x331 + 5000*m.x1080 - 5000*m.x1115 <= 0)

m.c1455 = Constraint(expr=   m.x332 + 5000*m.x1081 - 5000*m.x1116 <= 0)

m.c1456 = Constraint(expr=   m.x333 + 5000*m.x1082 - 5000*m.x1117 <= 0)

m.c1457 = Constraint(expr=   m.x334 + 5000*m.x1083 - 5000*m.x1118 <= 0)

m.c1458 = Constraint(expr=   m.x335 + 5000*m.x1084 - 5000*m.x1119 <= 0)

m.c1459 = Constraint(expr=   m.x336 + 5000*m.x1085 - 5000*m.x1120 <= 0)

m.c1460 = Constraint(expr=   m.x337 + 5000*m.x1086 - 5000*m.x1121 <= 0)

m.c1461 = Constraint(expr=   m.x338 + 5000*m.x1087 - 5000*m.x1122 <= 0)

m.c1462 = Constraint(expr=   m.x339 + 5000*m.x1088 - 5000*m.x1123 <= 0)

m.c1463 = Constraint(expr=   m.x340 + 5000*m.x1089 - 5000*m.x1124 <= 0)

m.c1464 = Constraint(expr=   m.x341 + 5000*m.x1090 - 5000*m.x1125 <= 0)

m.c1465 = Constraint(expr=   m.x342 + 5000*m.x1091 - 5000*m.x1126 <= 0)

m.c1466 = Constraint(expr=   m.x343 + 5000*m.x1092 - 5000*m.x1127 <= 0)

m.c1467 = Constraint(expr=   m.x344 + 5000*m.x1093 - 5000*m.x1128 <= 0)

m.c1468 = Constraint(expr=   m.x345 + 5000*m.x1094 - 5000*m.x1129 <= 0)

m.c1469 = Constraint(expr=   m.x346 + 5000*m.x1095 - 5000*m.x1130 <= 0)

m.c1470 = Constraint(expr=   m.x347 + 5000*m.x1096 - 5000*m.x1131 <= 0)

m.c1471 = Constraint(expr=   m.x348 + 5000*m.x1097 - 5000*m.x1132 <= 0)

m.c1472 = Constraint(expr=   m.x349 + 5000*m.x1098 - 5000*m.x1133 <= 0)

m.c1473 = Constraint(expr=   m.x350 + 5000*m.x1099 - 5000*m.x1134 <= 0)

m.c1474 = Constraint(expr=   m.x351 + 5000*m.x1100 - 5000*m.x1135 <= 0)

m.c1475 = Constraint(expr=   m.x352 + 5000*m.x1101 - 5000*m.x1136 <= 0)

m.c1476 = Constraint(expr=   m.x353 + 5000*m.x1102 - 5000*m.x1137 <= 0)

m.c1477 = Constraint(expr=   m.x354 + 5000*m.x1103 - 5000*m.x1138 <= 0)

m.c1478 = Constraint(expr=   m.x355 + 5000*m.x1104 - 5000*m.x1139 <= 0)

m.c1479 = Constraint(expr=   m.x356 + 5000*m.x1105 - 5000*m.x1140 <= 0)

m.c1480 = Constraint(expr=   m.x357 + 5000*m.x1106 - 5000*m.x1141 <= 0)

m.c1481 = Constraint(expr=   m.x358 + 5000*m.x1107 - 5000*m.x1142 <= 0)

m.c1482 = Constraint(expr=   m.x359 + 5000*m.x1108 - 5000*m.x1143 <= 0)

m.c1483 = Constraint(expr=   m.x360 + 5000*m.x1109 - 5000*m.x1144 <= 0)

m.c1484 = Constraint(expr= - 5000*m.b291 + m.x326 <= 0)

m.c1485 = Constraint(expr= - 25000*m.b292 + m.x327 <= 0)

m.c1486 = Constraint(expr= - 25000*m.b293 + m.x328 <= 0)

m.c1487 = Constraint(expr= - 25000*m.b294 + m.x329 <= 0)

m.c1488 = Constraint(expr= - 25000*m.b295 + m.x330 <= 0)

m.c1489 = Constraint(expr= - 6000*m.b296 + m.x331 <= 0)

m.c1490 = Constraint(expr= - 14500*m.b297 + m.x332 <= 0)

m.c1491 = Constraint(expr= - 25000*m.b298 + m.x333 <= 0)

m.c1492 = Constraint(expr= - 25000*m.b299 + m.x334 <= 0)

m.c1493 = Constraint(expr= - 25000*m.b300 + m.x335 <= 0)

m.c1494 = Constraint(expr= - 7000*m.b301 + m.x336 <= 0)

m.c1495 = Constraint(expr= - 7000*m.b302 + m.x337 <= 0)

m.c1496 = Constraint(expr= - 25000*m.b303 + m.x338 <= 0)

m.c1497 = Constraint(expr= - 25000*m.b304 + m.x339 <= 0)

m.c1498 = Constraint(expr= - 25000*m.b305 + m.x340 <= 0)

m.c1499 = Constraint(expr= - 8000*m.b306 + m.x341 <= 0)

m.c1500 = Constraint(expr= - 25000*m.b307 + m.x342 <= 0)

m.c1501 = Constraint(expr= - 25000*m.b308 + m.x343 <= 0)

m.c1502 = Constraint(expr= - 25000*m.b309 + m.x344 <= 0)

m.c1503 = Constraint(expr= - 25000*m.b310 + m.x345 <= 0)

m.c1504 = Constraint(expr= - 8000*m.b311 + m.x346 <= 0)

m.c1505 = Constraint(expr= - 35000*m.b312 + m.x347 <= 0)

m.c1506 = Constraint(expr= - 35000*m.b313 + m.x348 <= 0)

m.c1507 = Constraint(expr= - 35000*m.b314 + m.x349 <= 0)

m.c1508 = Constraint(expr= - 35000*m.b315 + m.x350 <= 0)

m.c1509 = Constraint(expr= - 20000*m.b316 + m.x351 <= 0)

m.c1510 = Constraint(expr= - 35000*m.b317 + m.x352 <= 0)

m.c1511 = Constraint(expr= - 35000*m.b318 + m.x353 <= 0)

m.c1512 = Constraint(expr= - 35000*m.b319 + m.x354 <= 0)

m.c1513 = Constraint(expr= - 35000*m.b320 + m.x355 <= 0)

m.c1514 = Constraint(expr= - 10000*m.b321 + m.x356 <= 0)

m.c1515 = Constraint(expr= - 10000*m.b322 + m.x357 <= 0)

m.c1516 = Constraint(expr= - 35000*m.b323 + m.x358 <= 0)

m.c1517 = Constraint(expr= - 35000*m.b324 + m.x359 <= 0)

m.c1518 = Constraint(expr= - 35000*m.b325 + m.x360 <= 0)

m.c1519 = Constraint(expr=   m.x326 - m.x361 == 0)

m.c1520 = Constraint(expr=   m.x327 - m.x362 == 0)

m.c1521 = Constraint(expr=   m.x328 - m.x363 == 0)

m.c1522 = Constraint(expr=   m.x329 - m.x364 == 0)

m.c1523 = Constraint(expr=   m.x330 - m.x365 == 0)

m.c1524 = Constraint(expr=   m.x331 - m.x366 == 0)

m.c1525 = Constraint(expr=   m.x332 - m.x367 == 0)

m.c1526 = Constraint(expr=   m.x333 - m.x368 == 0)

m.c1527 = Constraint(expr=   m.x334 - m.x369 == 0)

m.c1528 = Constraint(expr=   m.x335 - m.x370 == 0)

m.c1529 = Constraint(expr=   m.x336 - m.x371 == 0)

m.c1530 = Constraint(expr=   m.x337 - m.x372 == 0)

m.c1531 = Constraint(expr=   m.x338 - m.x373 == 0)

m.c1532 = Constraint(expr=   m.x339 - m.x374 == 0)

m.c1533 = Constraint(expr=   m.x340 - m.x375 == 0)

m.c1534 = Constraint(expr=   m.x341 - m.x376 == 0)

m.c1535 = Constraint(expr=   m.x342 - m.x377 == 0)

m.c1536 = Constraint(expr=   m.x343 - m.x378 == 0)

m.c1537 = Constraint(expr=   m.x344 - m.x379 == 0)

m.c1538 = Constraint(expr=   m.x345 - m.x380 == 0)

m.c1539 = Constraint(expr=   m.x346 - m.x381 == 0)

m.c1540 = Constraint(expr=   m.x347 - m.x382 == 0)

m.c1541 = Constraint(expr=   m.x348 - m.x383 == 0)

m.c1542 = Constraint(expr=   m.x349 - m.x384 == 0)

m.c1543 = Constraint(expr=   m.x350 - m.x385 == 0)

m.c1544 = Constraint(expr=   m.x351 - m.x386 - m.x391 - m.x396 == 0)

m.c1545 = Constraint(expr=   m.x352 - m.x387 - m.x392 - m.x397 == 0)

m.c1546 = Constraint(expr=   m.x353 - m.x388 - m.x393 - m.x398 == 0)

m.c1547 = Constraint(expr=   m.x354 - m.x389 - m.x394 - m.x399 == 0)

m.c1548 = Constraint(expr=   m.x355 - m.x390 - m.x395 - m.x400 == 0)

m.c1549 = Constraint(expr=   m.x356 - m.x401 == 0)

m.c1550 = Constraint(expr=   m.x357 - m.x402 == 0)

m.c1551 = Constraint(expr=   m.x358 - m.x403 == 0)

m.c1552 = Constraint(expr=   m.x359 - m.x404 == 0)

m.c1553 = Constraint(expr=   m.x360 - m.x405 == 0)

m.c1554 = Constraint(expr= - m.x326 - m.x336 - m.x341 - m.x346 - m.x356 + m.x406 == 0)

m.c1555 = Constraint(expr= - m.x327 - m.x337 - m.x342 - m.x347 - m.x357 + m.x407 == 0)

m.c1556 = Constraint(expr= - m.x328 - m.x338 - m.x343 - m.x348 - m.x358 + m.x408 == 0)

m.c1557 = Constraint(expr= - m.x329 - m.x339 - m.x344 - m.x349 - m.x359 + m.x409 == 0)

m.c1558 = Constraint(expr= - m.x330 - m.x340 - m.x345 - m.x350 - m.x360 + m.x410 == 0)

m.c1559 = Constraint(expr= - m.x331 - m.x351 + m.x411 == 0)

m.c1560 = Constraint(expr= - m.x332 - m.x352 + m.x412 == 0)

m.c1561 = Constraint(expr= - m.x333 - m.x353 + m.x413 == 0)

m.c1562 = Constraint(expr= - m.x334 - m.x354 + m.x414 == 0)

m.c1563 = Constraint(expr= - m.x335 - m.x355 + m.x415 == 0)

m.c1564 = Constraint(expr= - m.x406 - 2000*m.x1145 + 2000*m.x1155 <= 0)

m.c1565 = Constraint(expr= - m.x407 - 2000*m.x1146 + 2000*m.x1156 <= 0)

m.c1566 = Constraint(expr= - m.x408 - 2000*m.x1147 + 2000*m.x1157 <= 0)

m.c1567 = Constraint(expr= - m.x409 - 2000*m.x1148 + 2000*m.x1158 <= 0)

m.c1568 = Constraint(expr= - m.x410 - 2000*m.x1149 + 2000*m.x1159 <= 0)

m.c1569 = Constraint(expr= - m.x411 - 1000*m.x1150 + 1000*m.x1160 <= 0)

m.c1570 = Constraint(expr= - m.x412 - 1000*m.x1151 + 1000*m.x1161 <= 0)

m.c1571 = Constraint(expr= - m.x413 - 1000*m.x1152 + 1000*m.x1162 <= 0)

m.c1572 = Constraint(expr= - m.x414 - 1000*m.x1153 + 1000*m.x1163 <= 0)

m.c1573 = Constraint(expr= - m.x415 - 1000*m.x1154 + 1000*m.x1164 <= 0)

m.c1574 = Constraint(expr=   m.x406 + 8000*m.x1145 - 8000*m.x1155 <= 0)

m.c1575 = Constraint(expr=   m.x407 + 8000*m.x1146 - 8000*m.x1156 <= 0)

m.c1576 = Constraint(expr=   m.x408 + 8000*m.x1147 - 8000*m.x1157 <= 0)

m.c1577 = Constraint(expr=   m.x409 + 8000*m.x1148 - 8000*m.x1158 <= 0)

m.c1578 = Constraint(expr=   m.x410 + 8000*m.x1149 - 8000*m.x1159 <= 0)

m.c1579 = Constraint(expr=   m.x411 + 3000*m.x1150 - 3000*m.x1160 <= 0)

m.c1580 = Constraint(expr=   m.x412 + 3000*m.x1151 - 3000*m.x1161 <= 0)

m.c1581 = Constraint(expr=   m.x413 + 3000*m.x1152 - 3000*m.x1162 <= 0)

m.c1582 = Constraint(expr=   m.x414 + 3000*m.x1153 - 3000*m.x1163 <= 0)

m.c1583 = Constraint(expr=   m.x415 + 3000*m.x1154 - 3000*m.x1164 <= 0)

m.c1584 = Constraint(expr= - m.x366 - m.x386 + 0.45*m.x411 <= 0)

m.c1585 = Constraint(expr= - m.x367 - m.x387 + 0.45*m.x412 <= 0)

m.c1586 = Constraint(expr= - m.x368 - m.x388 + 0.45*m.x413 <= 0)

m.c1587 = Constraint(expr= - m.x369 - m.x389 + 0.45*m.x414 <= 0)

m.c1588 = Constraint(expr= - m.x370 - m.x390 + 0.45*m.x415 <= 0)

m.c1589 = Constraint(expr=   m.x656 - m.x860 >= 0)

m.c1590 = Constraint(expr=   m.x657 - m.x861 >= 0)

m.c1591 = Constraint(expr=   m.x658 - m.x862 >= 0)

m.c1592 = Constraint(expr=   m.x659 - m.x863 >= 0)

m.c1593 = Constraint(expr=   m.x661 - m.x865 >= 0)

m.c1594 = Constraint(expr=   m.x662 - m.x866 >= 0)

m.c1595 = Constraint(expr=   m.x663 - m.x867 >= 0)

m.c1596 = Constraint(expr=   m.x664 - m.x868 >= 0)

m.c1597 = Constraint(expr=   m.x666 - m.x870 >= 0)

m.c1598 = Constraint(expr=   m.x667 - m.x871 >= 0)

m.c1599 = Constraint(expr=   m.x668 - m.x872 >= 0)

m.c1600 = Constraint(expr=   m.x669 - m.x873 >= 0)

m.c1601 = Constraint(expr=   m.x671 - m.x875 >= 0)

m.c1602 = Constraint(expr=   m.x672 - m.x876 >= 0)

m.c1603 = Constraint(expr=   m.x673 - m.x877 >= 0)

m.c1604 = Constraint(expr=   m.x674 - m.x878 >= 0)

m.c1605 = Constraint(expr=   m.x676 - m.x880 >= 0)

m.c1606 = Constraint(expr=   m.x677 - m.x881 >= 0)

m.c1607 = Constraint(expr=   m.x678 - m.x882 >= 0)

m.c1608 = Constraint(expr=   m.x679 - m.x883 >= 0)

m.c1609 = Constraint(expr=   m.x681 - m.x885 >= 0)

m.c1610 = Constraint(expr=   m.x682 - m.x886 >= 0)

m.c1611 = Constraint(expr=   m.x683 - m.x887 >= 0)

m.c1612 = Constraint(expr=   m.x684 - m.x888 >= 0)

m.c1613 = Constraint(expr=   m.x686 - m.x890 >= 0)

m.c1614 = Constraint(expr=   m.x687 - m.x891 >= 0)

m.c1615 = Constraint(expr=   m.x688 - m.x892 >= 0)

m.c1616 = Constraint(expr=   m.x689 - m.x893 >= 0)

m.c1617 = Constraint(expr=   m.x691 - m.x895 >= 0)

m.c1618 = Constraint(expr=   m.x692 - m.x896 >= 0)

m.c1619 = Constraint(expr=   m.x693 - m.x897 >= 0)

m.c1620 = Constraint(expr=   m.x694 - m.x898 >= 0)

m.c1621 = Constraint(expr=   m.x696 - m.x900 >= 0)

m.c1622 = Constraint(expr=   m.x697 - m.x901 >= 0)

m.c1623 = Constraint(expr=   m.x698 - m.x902 >= 0)

m.c1624 = Constraint(expr=   m.x699 - m.x903 >= 0)

m.c1625 = Constraint(expr=   m.x701 - m.x905 >= 0)

m.c1626 = Constraint(expr=   m.x702 - m.x906 >= 0)

m.c1627 = Constraint(expr=   m.x703 - m.x907 >= 0)

m.c1628 = Constraint(expr=   m.x704 - m.x908 >= 0)

m.c1629 = Constraint(expr=   m.x706 - m.x910 >= 0)

m.c1630 = Constraint(expr=   m.x707 - m.x911 >= 0)

m.c1631 = Constraint(expr=   m.x708 - m.x912 >= 0)

m.c1632 = Constraint(expr=   m.x709 - m.x913 >= 0)

m.c1633 = Constraint(expr=   m.x711 - m.x915 >= 0)

m.c1634 = Constraint(expr=   m.x712 - m.x916 >= 0)

m.c1635 = Constraint(expr=   m.x713 - m.x917 >= 0)

m.c1636 = Constraint(expr=   m.x714 - m.x918 >= 0)

m.c1637 = Constraint(expr=   m.x716 - m.x920 >= 0)

m.c1638 = Constraint(expr=   m.x717 - m.x921 >= 0)

m.c1639 = Constraint(expr=   m.x718 - m.x922 >= 0)

m.c1640 = Constraint(expr=   m.x719 - m.x923 >= 0)

m.c1641 = Constraint(expr=   m.x721 - m.x925 >= 0)

m.c1642 = Constraint(expr=   m.x722 - m.x926 >= 0)

m.c1643 = Constraint(expr=   m.x723 - m.x927 >= 0)

m.c1644 = Constraint(expr=   m.x724 - m.x928 >= 0)

m.c1645 = Constraint(expr=   m.x726 - m.x930 >= 0)

m.c1646 = Constraint(expr=   m.x727 - m.x931 >= 0)

m.c1647 = Constraint(expr=   m.x728 - m.x932 >= 0)

m.c1648 = Constraint(expr=   m.x729 - m.x933 >= 0)

m.c1649 = Constraint(expr=   m.x731 - m.x935 >= 0)

m.c1650 = Constraint(expr=   m.x732 - m.x936 >= 0)

m.c1651 = Constraint(expr=   m.x733 - m.x937 >= 0)

m.c1652 = Constraint(expr=   m.x734 - m.x938 >= 0)

m.c1653 = Constraint(expr=   m.x736 - m.x940 >= 0)

m.c1654 = Constraint(expr=   m.x737 - m.x941 >= 0)

m.c1655 = Constraint(expr=   m.x738 - m.x942 >= 0)

m.c1656 = Constraint(expr=   m.x739 - m.x943 >= 0)

m.c1657 = Constraint(expr=   m.x741 - m.x945 >= 0)

m.c1658 = Constraint(expr=   m.x742 - m.x946 >= 0)

m.c1659 = Constraint(expr=   m.x743 - m.x947 >= 0)

m.c1660 = Constraint(expr=   m.x744 - m.x948 >= 0)

m.c1661 = Constraint(expr=   m.x746 - m.x950 >= 0)

m.c1662 = Constraint(expr=   m.x747 - m.x951 >= 0)

m.c1663 = Constraint(expr=   m.x748 - m.x952 >= 0)

m.c1664 = Constraint(expr=   m.x749 - m.x953 >= 0)

m.c1665 = Constraint(expr=   m.x751 - m.x955 >= 0)

m.c1666 = Constraint(expr=   m.x752 - m.x956 >= 0)

m.c1667 = Constraint(expr=   m.x753 - m.x957 >= 0)

m.c1668 = Constraint(expr=   m.x754 - m.x958 >= 0)

m.c1669 = Constraint(expr=   m.x756 - m.x960 >= 0)

m.c1670 = Constraint(expr=   m.x757 - m.x961 >= 0)

m.c1671 = Constraint(expr=   m.x758 - m.x962 >= 0)

m.c1672 = Constraint(expr=   m.x759 - m.x963 >= 0)

m.c1673 = Constraint(expr=   m.x761 - m.x965 >= 0)

m.c1674 = Constraint(expr=   m.x762 - m.x966 >= 0)

m.c1675 = Constraint(expr=   m.x763 - m.x967 >= 0)

m.c1676 = Constraint(expr=   m.x764 - m.x968 >= 0)

m.c1677 = Constraint(expr=   m.x766 - m.x970 >= 0)

m.c1678 = Constraint(expr=   m.x767 - m.x971 >= 0)

m.c1679 = Constraint(expr=   m.x768 - m.x972 >= 0)

m.c1680 = Constraint(expr=   m.x769 - m.x973 >= 0)

m.c1681 = Constraint(expr=   m.x771 - m.x975 >= 0)

m.c1682 = Constraint(expr=   m.x772 - m.x976 >= 0)

m.c1683 = Constraint(expr=   m.x773 - m.x977 >= 0)

m.c1684 = Constraint(expr=   m.x774 - m.x978 >= 0)

m.c1685 = Constraint(expr=   m.x776 - m.x980 >= 0)

m.c1686 = Constraint(expr=   m.x777 - m.x981 >= 0)

m.c1687 = Constraint(expr=   m.x778 - m.x982 >= 0)

m.c1688 = Constraint(expr=   m.x779 - m.x983 >= 0)

m.c1689 = Constraint(expr=   m.x781 - m.x985 >= 0)

m.c1690 = Constraint(expr=   m.x782 - m.x986 >= 0)

m.c1691 = Constraint(expr=   m.x783 - m.x987 >= 0)

m.c1692 = Constraint(expr=   m.x784 - m.x988 >= 0)

m.c1693 = Constraint(expr=   m.x786 - m.x990 >= 0)

m.c1694 = Constraint(expr=   m.x787 - m.x991 >= 0)

m.c1695 = Constraint(expr=   m.x788 - m.x992 >= 0)

m.c1696 = Constraint(expr=   m.x789 - m.x993 >= 0)

m.c1697 = Constraint(expr=   m.x791 - m.x995 >= 0)

m.c1698 = Constraint(expr=   m.x792 - m.x996 >= 0)

m.c1699 = Constraint(expr=   m.x793 - m.x997 >= 0)

m.c1700 = Constraint(expr=   m.x794 - m.x998 >= 0)

m.c1701 = Constraint(expr=   m.x796 - m.x1000 >= 0)

m.c1702 = Constraint(expr=   m.x797 - m.x1001 >= 0)

m.c1703 = Constraint(expr=   m.x798 - m.x1002 >= 0)

m.c1704 = Constraint(expr=   m.x799 - m.x1003 >= 0)

m.c1705 = Constraint(expr=   m.x801 - m.x1005 >= 0)

m.c1706 = Constraint(expr=   m.x802 - m.x1006 >= 0)

m.c1707 = Constraint(expr=   m.x803 - m.x1007 >= 0)

m.c1708 = Constraint(expr=   m.x804 - m.x1008 >= 0)

m.c1709 = Constraint(expr=   m.x806 - m.x1010 >= 0)

m.c1710 = Constraint(expr=   m.x807 - m.x1011 >= 0)

m.c1711 = Constraint(expr=   m.x808 - m.x1012 >= 0)

m.c1712 = Constraint(expr=   m.x809 - m.x1013 >= 0)

m.c1713 = Constraint(expr=   m.x811 - m.x1015 >= 0)

m.c1714 = Constraint(expr=   m.x812 - m.x1016 >= 0)

m.c1715 = Constraint(expr=   m.x813 - m.x1017 >= 0)

m.c1716 = Constraint(expr=   m.x814 - m.x1018 >= 0)

m.c1717 = Constraint(expr=   m.x816 - m.x1020 >= 0)

m.c1718 = Constraint(expr=   m.x817 - m.x1021 >= 0)

m.c1719 = Constraint(expr=   m.x818 - m.x1022 >= 0)

m.c1720 = Constraint(expr=   m.x819 - m.x1023 >= 0)

m.c1721 = Constraint(expr=   m.x821 - m.x1025 >= 0)

m.c1722 = Constraint(expr=   m.x822 - m.x1026 >= 0)

m.c1723 = Constraint(expr=   m.x823 - m.x1027 >= 0)

m.c1724 = Constraint(expr=   m.x824 - m.x1028 >= 0)

m.c1725 = Constraint(expr=   m.x826 - m.x1030 >= 0)

m.c1726 = Constraint(expr=   m.x827 - m.x1031 >= 0)

m.c1727 = Constraint(expr=   m.x828 - m.x1032 >= 0)

m.c1728 = Constraint(expr=   m.x829 - m.x1033 >= 0)

m.c1729 = Constraint(expr=   m.x831 - m.x1035 >= 0)

m.c1730 = Constraint(expr=   m.x832 - m.x1036 >= 0)

m.c1731 = Constraint(expr=   m.x833 - m.x1037 >= 0)

m.c1732 = Constraint(expr=   m.x834 - m.x1038 >= 0)

m.c1733 = Constraint(expr=   m.x836 - m.x1040 >= 0)

m.c1734 = Constraint(expr=   m.x837 - m.x1041 >= 0)

m.c1735 = Constraint(expr=   m.x838 - m.x1042 >= 0)

m.c1736 = Constraint(expr=   m.x839 - m.x1043 >= 0)

m.c1737 = Constraint(expr=   m.x841 - m.x1045 >= 0)

m.c1738 = Constraint(expr=   m.x842 - m.x1046 >= 0)

m.c1739 = Constraint(expr=   m.x843 - m.x1047 >= 0)

m.c1740 = Constraint(expr=   m.x844 - m.x1048 >= 0)

m.c1741 = Constraint(expr=   m.x846 - m.x1050 >= 0)

m.c1742 = Constraint(expr=   m.x847 - m.x1051 >= 0)

m.c1743 = Constraint(expr=   m.x848 - m.x1052 >= 0)

m.c1744 = Constraint(expr=   m.x849 - m.x1053 >= 0)

m.c1745 = Constraint(expr=   m.x851 - m.x1055 >= 0)

m.c1746 = Constraint(expr=   m.x852 - m.x1056 >= 0)

m.c1747 = Constraint(expr=   m.x853 - m.x1057 >= 0)

m.c1748 = Constraint(expr=   m.x854 - m.x1058 >= 0)

m.c1749 = Constraint(expr=   m.x856 - m.x1060 >= 0)

m.c1750 = Constraint(expr=   m.x857 - m.x1061 >= 0)

m.c1751 = Constraint(expr=   m.x858 - m.x1062 >= 0)

m.c1752 = Constraint(expr=   m.x859 - m.x1063 >= 0)

m.c1753 = Constraint(expr= - 7*m.b1 + m.x661 - m.x860 >= -7)

m.c1754 = Constraint(expr= - 7*m.b2 + m.x662 - m.x861 >= -7)

m.c1755 = Constraint(expr= - 7*m.b3 + m.x663 - m.x862 >= -7)

m.c1756 = Constraint(expr= - 7*m.b4 + m.x664 - m.x863 >= -7)

m.c1757 = Constraint(expr= - 7*m.b1 + m.x666 - m.x860 >= -7)

m.c1758 = Constraint(expr= - 7*m.b2 + m.x667 - m.x861 >= -7)

m.c1759 = Constraint(expr= - 7*m.b3 + m.x668 - m.x862 >= -7)

m.c1760 = Constraint(expr= - 7*m.b4 + m.x669 - m.x863 >= -7)

m.c1761 = Constraint(expr= - 7*m.b6 + m.x656 - m.x865 >= -7)

m.c1762 = Constraint(expr= - 7*m.b7 + m.x657 - m.x866 >= -7)

m.c1763 = Constraint(expr= - 7*m.b8 + m.x658 - m.x867 >= -7)

m.c1764 = Constraint(expr= - 7*m.b9 + m.x659 - m.x868 >= -7)

m.c1765 = Constraint(expr= - 7*m.b6 + m.x666 - m.x865 >= -7)

m.c1766 = Constraint(expr= - 7*m.b7 + m.x667 - m.x866 >= -7)

m.c1767 = Constraint(expr= - 7*m.b8 + m.x668 - m.x867 >= -7)

m.c1768 = Constraint(expr= - 7*m.b9 + m.x669 - m.x868 >= -7)

m.c1769 = Constraint(expr= - 7*m.b11 + m.x656 - m.x870 >= -7)

m.c1770 = Constraint(expr= - 7*m.b12 + m.x657 - m.x871 >= -7)

m.c1771 = Constraint(expr= - 7*m.b13 + m.x658 - m.x872 >= -7)

m.c1772 = Constraint(expr= - 7*m.b14 + m.x659 - m.x873 >= -7)

m.c1773 = Constraint(expr= - 7*m.b11 + m.x661 - m.x870 >= -7)

m.c1774 = Constraint(expr= - 7*m.b12 + m.x662 - m.x871 >= -7)

m.c1775 = Constraint(expr= - 7*m.b13 + m.x663 - m.x872 >= -7)

m.c1776 = Constraint(expr= - 7*m.b14 + m.x664 - m.x873 >= -7)

m.c1777 = Constraint(expr= - 7*m.b16 + m.x676 - m.x875 >= -7)

m.c1778 = Constraint(expr= - 7*m.b17 + m.x677 - m.x876 >= -7)

m.c1779 = Constraint(expr= - 7*m.b18 + m.x678 - m.x877 >= -7)

m.c1780 = Constraint(expr= - 7*m.b19 + m.x679 - m.x878 >= -7)

m.c1781 = Constraint(expr= - 7*m.b16 + m.x681 - m.x875 >= -7)

m.c1782 = Constraint(expr= - 7*m.b17 + m.x682 - m.x876 >= -7)

m.c1783 = Constraint(expr= - 7*m.b18 + m.x683 - m.x877 >= -7)

m.c1784 = Constraint(expr= - 7*m.b19 + m.x684 - m.x878 >= -7)

m.c1785 = Constraint(expr= - 7*m.b21 + m.x671 - m.x880 >= -7)

m.c1786 = Constraint(expr= - 7*m.b22 + m.x672 - m.x881 >= -7)

m.c1787 = Constraint(expr= - 7*m.b23 + m.x673 - m.x882 >= -7)

m.c1788 = Constraint(expr= - 7*m.b24 + m.x674 - m.x883 >= -7)

m.c1789 = Constraint(expr= - 7*m.b21 + m.x681 - m.x880 >= -7)

m.c1790 = Constraint(expr= - 7*m.b22 + m.x682 - m.x881 >= -7)

m.c1791 = Constraint(expr= - 7*m.b23 + m.x683 - m.x882 >= -7)

m.c1792 = Constraint(expr= - 7*m.b24 + m.x684 - m.x883 >= -7)

m.c1793 = Constraint(expr= - 7*m.b26 + m.x671 - m.x885 >= -7)

m.c1794 = Constraint(expr= - 7*m.b27 + m.x672 - m.x886 >= -7)

m.c1795 = Constraint(expr= - 7*m.b28 + m.x673 - m.x887 >= -7)

m.c1796 = Constraint(expr= - 7*m.b29 + m.x674 - m.x888 >= -7)

m.c1797 = Constraint(expr= - 7*m.b26 + m.x676 - m.x885 >= -7)

m.c1798 = Constraint(expr= - 7*m.b27 + m.x677 - m.x886 >= -7)

m.c1799 = Constraint(expr= - 7*m.b28 + m.x678 - m.x887 >= -7)

m.c1800 = Constraint(expr= - 7*m.b29 + m.x679 - m.x888 >= -7)

m.c1801 = Constraint(expr= - 7*m.b31 + m.x691 - m.x890 >= -7)

m.c1802 = Constraint(expr= - 7*m.b32 + m.x692 - m.x891 >= -7)

m.c1803 = Constraint(expr= - 7*m.b33 + m.x693 - m.x892 >= -7)

m.c1804 = Constraint(expr= - 7*m.b34 + m.x694 - m.x893 >= -7)

m.c1805 = Constraint(expr= - 7*m.b31 + m.x696 - m.x890 >= -7)

m.c1806 = Constraint(expr= - 7*m.b32 + m.x697 - m.x891 >= -7)

m.c1807 = Constraint(expr= - 7*m.b33 + m.x698 - m.x892 >= -7)

m.c1808 = Constraint(expr= - 7*m.b34 + m.x699 - m.x893 >= -7)

m.c1809 = Constraint(expr= - 7*m.b36 + m.x686 - m.x895 >= -7)

m.c1810 = Constraint(expr= - 7*m.b37 + m.x687 - m.x896 >= -7)

m.c1811 = Constraint(expr= - 7*m.b38 + m.x688 - m.x897 >= -7)

m.c1812 = Constraint(expr= - 7*m.b39 + m.x689 - m.x898 >= -7)

m.c1813 = Constraint(expr= - 7*m.b36 + m.x696 - m.x895 >= -7)

m.c1814 = Constraint(expr= - 7*m.b37 + m.x697 - m.x896 >= -7)

m.c1815 = Constraint(expr= - 7*m.b38 + m.x698 - m.x897 >= -7)

m.c1816 = Constraint(expr= - 7*m.b39 + m.x699 - m.x898 >= -7)

m.c1817 = Constraint(expr= - 7*m.b41 + m.x686 - m.x900 >= -7)

m.c1818 = Constraint(expr= - 7*m.b42 + m.x687 - m.x901 >= -7)

m.c1819 = Constraint(expr= - 7*m.b43 + m.x688 - m.x902 >= -7)

m.c1820 = Constraint(expr= - 7*m.b44 + m.x689 - m.x903 >= -7)

m.c1821 = Constraint(expr= - 7*m.b41 + m.x691 - m.x900 >= -7)

m.c1822 = Constraint(expr= - 7*m.b42 + m.x692 - m.x901 >= -7)

m.c1823 = Constraint(expr= - 7*m.b43 + m.x693 - m.x902 >= -7)

m.c1824 = Constraint(expr= - 7*m.b44 + m.x694 - m.x903 >= -7)

m.c1825 = Constraint(expr= - 7*m.b46 + m.x706 - m.x905 >= -7)

m.c1826 = Constraint(expr= - 7*m.b47 + m.x707 - m.x906 >= -7)

m.c1827 = Constraint(expr= - 7*m.b48 + m.x708 - m.x907 >= -7)

m.c1828 = Constraint(expr= - 7*m.b49 + m.x709 - m.x908 >= -7)

m.c1829 = Constraint(expr= - 7*m.b46 + m.x711 - m.x905 >= -7)

m.c1830 = Constraint(expr= - 7*m.b47 + m.x712 - m.x906 >= -7)

m.c1831 = Constraint(expr= - 7*m.b48 + m.x713 - m.x907 >= -7)

m.c1832 = Constraint(expr= - 7*m.b49 + m.x714 - m.x908 >= -7)

m.c1833 = Constraint(expr= - 7*m.b51 + m.x701 - m.x910 >= -7)

m.c1834 = Constraint(expr= - 7*m.b52 + m.x702 - m.x911 >= -7)

m.c1835 = Constraint(expr= - 7*m.b53 + m.x703 - m.x912 >= -7)

m.c1836 = Constraint(expr= - 7*m.b54 + m.x704 - m.x913 >= -7)

m.c1837 = Constraint(expr= - 7*m.b51 + m.x711 - m.x910 >= -7)

m.c1838 = Constraint(expr= - 7*m.b52 + m.x712 - m.x911 >= -7)

m.c1839 = Constraint(expr= - 7*m.b53 + m.x713 - m.x912 >= -7)

m.c1840 = Constraint(expr= - 7*m.b54 + m.x714 - m.x913 >= -7)

m.c1841 = Constraint(expr= - 7*m.b56 + m.x701 - m.x915 >= -7)

m.c1842 = Constraint(expr= - 7*m.b57 + m.x702 - m.x916 >= -7)

m.c1843 = Constraint(expr= - 7*m.b58 + m.x703 - m.x917 >= -7)

m.c1844 = Constraint(expr= - 7*m.b59 + m.x704 - m.x918 >= -7)

m.c1845 = Constraint(expr= - 7*m.b56 + m.x706 - m.x915 >= -7)

m.c1846 = Constraint(expr= - 7*m.b57 + m.x707 - m.x916 >= -7)

m.c1847 = Constraint(expr= - 7*m.b58 + m.x708 - m.x917 >= -7)

m.c1848 = Constraint(expr= - 7*m.b59 + m.x709 - m.x918 >= -7)

m.c1849 = Constraint(expr= - 7*m.b61 + m.x721 - m.x920 >= -7)

m.c1850 = Constraint(expr= - 7*m.b62 + m.x722 - m.x921 >= -7)

m.c1851 = Constraint(expr= - 7*m.b63 + m.x723 - m.x922 >= -7)

m.c1852 = Constraint(expr= - 7*m.b64 + m.x724 - m.x923 >= -7)

m.c1853 = Constraint(expr= - 7*m.b61 + m.x726 - m.x920 >= -7)

m.c1854 = Constraint(expr= - 7*m.b62 + m.x727 - m.x921 >= -7)

m.c1855 = Constraint(expr= - 7*m.b63 + m.x728 - m.x922 >= -7)

m.c1856 = Constraint(expr= - 7*m.b64 + m.x729 - m.x923 >= -7)

m.c1857 = Constraint(expr= - 7*m.b66 + m.x716 - m.x925 >= -7)

m.c1858 = Constraint(expr= - 7*m.b67 + m.x717 - m.x926 >= -7)

m.c1859 = Constraint(expr= - 7*m.b68 + m.x718 - m.x927 >= -7)

m.c1860 = Constraint(expr= - 7*m.b69 + m.x719 - m.x928 >= -7)

m.c1861 = Constraint(expr= - 7*m.b66 + m.x726 - m.x925 >= -7)

m.c1862 = Constraint(expr= - 7*m.b67 + m.x727 - m.x926 >= -7)

m.c1863 = Constraint(expr= - 7*m.b68 + m.x728 - m.x927 >= -7)

m.c1864 = Constraint(expr= - 7*m.b69 + m.x729 - m.x928 >= -7)

m.c1865 = Constraint(expr= - 7*m.b71 + m.x716 - m.x930 >= -7)

m.c1866 = Constraint(expr= - 7*m.b72 + m.x717 - m.x931 >= -7)

m.c1867 = Constraint(expr= - 7*m.b73 + m.x718 - m.x932 >= -7)

m.c1868 = Constraint(expr= - 7*m.b74 + m.x719 - m.x933 >= -7)

m.c1869 = Constraint(expr= - 7*m.b71 + m.x721 - m.x930 >= -7)

m.c1870 = Constraint(expr= - 7*m.b72 + m.x722 - m.x931 >= -7)

m.c1871 = Constraint(expr= - 7*m.b73 + m.x723 - m.x932 >= -7)

m.c1872 = Constraint(expr= - 7*m.b74 + m.x724 - m.x933 >= -7)

m.c1873 = Constraint(expr= - 7*m.b76 + m.x736 - m.x935 >= -7)

m.c1874 = Constraint(expr= - 7*m.b77 + m.x737 - m.x936 >= -7)

m.c1875 = Constraint(expr= - 7*m.b78 + m.x738 - m.x937 >= -7)

m.c1876 = Constraint(expr= - 7*m.b79 + m.x739 - m.x938 >= -7)

m.c1877 = Constraint(expr= - 7*m.b76 + m.x741 - m.x935 >= -7)

m.c1878 = Constraint(expr= - 7*m.b77 + m.x742 - m.x936 >= -7)

m.c1879 = Constraint(expr= - 7*m.b78 + m.x743 - m.x937 >= -7)

m.c1880 = Constraint(expr= - 7*m.b79 + m.x744 - m.x938 >= -7)

m.c1881 = Constraint(expr= - 7*m.b81 + m.x731 - m.x940 >= -7)

m.c1882 = Constraint(expr= - 7*m.b82 + m.x732 - m.x941 >= -7)

m.c1883 = Constraint(expr= - 7*m.b83 + m.x733 - m.x942 >= -7)

m.c1884 = Constraint(expr= - 7*m.b84 + m.x734 - m.x943 >= -7)

m.c1885 = Constraint(expr= - 7*m.b81 + m.x741 - m.x940 >= -7)

m.c1886 = Constraint(expr= - 7*m.b82 + m.x742 - m.x941 >= -7)

m.c1887 = Constraint(expr= - 7*m.b83 + m.x743 - m.x942 >= -7)

m.c1888 = Constraint(expr= - 7*m.b84 + m.x744 - m.x943 >= -7)

m.c1889 = Constraint(expr= - 7*m.b86 + m.x731 - m.x945 >= -7)

m.c1890 = Constraint(expr= - 7*m.b87 + m.x732 - m.x946 >= -7)

m.c1891 = Constraint(expr= - 7*m.b88 + m.x733 - m.x947 >= -7)

m.c1892 = Constraint(expr= - 7*m.b89 + m.x734 - m.x948 >= -7)

m.c1893 = Constraint(expr= - 7*m.b86 + m.x736 - m.x945 >= -7)

m.c1894 = Constraint(expr= - 7*m.b87 + m.x737 - m.x946 >= -7)

m.c1895 = Constraint(expr= - 7*m.b88 + m.x738 - m.x947 >= -7)

m.c1896 = Constraint(expr= - 7*m.b89 + m.x739 - m.x948 >= -7)

m.c1897 = Constraint(expr= - 7*m.b91 + m.x751 - m.x950 >= -7)

m.c1898 = Constraint(expr= - 7*m.b92 + m.x752 - m.x951 >= -7)

m.c1899 = Constraint(expr= - 7*m.b93 + m.x753 - m.x952 >= -7)

m.c1900 = Constraint(expr= - 7*m.b94 + m.x754 - m.x953 >= -7)

m.c1901 = Constraint(expr= - 7*m.b91 + m.x756 - m.x950 >= -7)

m.c1902 = Constraint(expr= - 7*m.b92 + m.x757 - m.x951 >= -7)

m.c1903 = Constraint(expr= - 7*m.b93 + m.x758 - m.x952 >= -7)

m.c1904 = Constraint(expr= - 7*m.b94 + m.x759 - m.x953 >= -7)

m.c1905 = Constraint(expr= - 7*m.b96 + m.x746 - m.x955 >= -7)

m.c1906 = Constraint(expr= - 7*m.b97 + m.x747 - m.x956 >= -7)

m.c1907 = Constraint(expr= - 7*m.b98 + m.x748 - m.x957 >= -7)

m.c1908 = Constraint(expr= - 7*m.b99 + m.x749 - m.x958 >= -7)

m.c1909 = Constraint(expr= - 7*m.b96 + m.x756 - m.x955 >= -7)

m.c1910 = Constraint(expr= - 7*m.b97 + m.x757 - m.x956 >= -7)

m.c1911 = Constraint(expr= - 7*m.b98 + m.x758 - m.x957 >= -7)

m.c1912 = Constraint(expr= - 7*m.b99 + m.x759 - m.x958 >= -7)

m.c1913 = Constraint(expr= - 7*m.b101 + m.x746 - m.x960 >= -7)

m.c1914 = Constraint(expr= - 7*m.b102 + m.x747 - m.x961 >= -7)

m.c1915 = Constraint(expr= - 7*m.b103 + m.x748 - m.x962 >= -7)

m.c1916 = Constraint(expr= - 7*m.b104 + m.x749 - m.x963 >= -7)

m.c1917 = Constraint(expr= - 7*m.b101 + m.x751 - m.x960 >= -7)

m.c1918 = Constraint(expr= - 7*m.b102 + m.x752 - m.x961 >= -7)

m.c1919 = Constraint(expr= - 7*m.b103 + m.x753 - m.x962 >= -7)

m.c1920 = Constraint(expr= - 7*m.b104 + m.x754 - m.x963 >= -7)

m.c1921 = Constraint(expr= - 7*m.b106 + m.x766 - m.x965 >= -7)

m.c1922 = Constraint(expr= - 7*m.b107 + m.x767 - m.x966 >= -7)

m.c1923 = Constraint(expr= - 7*m.b108 + m.x768 - m.x967 >= -7)

m.c1924 = Constraint(expr= - 7*m.b109 + m.x769 - m.x968 >= -7)

m.c1925 = Constraint(expr= - 7*m.b106 + m.x771 - m.x965 >= -7)

m.c1926 = Constraint(expr= - 7*m.b107 + m.x772 - m.x966 >= -7)

m.c1927 = Constraint(expr= - 7*m.b108 + m.x773 - m.x967 >= -7)

m.c1928 = Constraint(expr= - 7*m.b109 + m.x774 - m.x968 >= -7)

m.c1929 = Constraint(expr= - 7*m.b111 + m.x761 - m.x970 >= -7)

m.c1930 = Constraint(expr= - 7*m.b112 + m.x762 - m.x971 >= -7)

m.c1931 = Constraint(expr= - 7*m.b113 + m.x763 - m.x972 >= -7)

m.c1932 = Constraint(expr= - 7*m.b114 + m.x764 - m.x973 >= -7)

m.c1933 = Constraint(expr= - 7*m.b111 + m.x771 - m.x970 >= -7)

m.c1934 = Constraint(expr= - 7*m.b112 + m.x772 - m.x971 >= -7)

m.c1935 = Constraint(expr= - 7*m.b113 + m.x773 - m.x972 >= -7)

m.c1936 = Constraint(expr= - 7*m.b114 + m.x774 - m.x973 >= -7)

m.c1937 = Constraint(expr= - 7*m.b116 + m.x761 - m.x975 >= -7)

m.c1938 = Constraint(expr= - 7*m.b117 + m.x762 - m.x976 >= -7)

m.c1939 = Constraint(expr= - 7*m.b118 + m.x763 - m.x977 >= -7)

m.c1940 = Constraint(expr= - 7*m.b119 + m.x764 - m.x978 >= -7)

m.c1941 = Constraint(expr= - 7*m.b116 + m.x766 - m.x975 >= -7)

m.c1942 = Constraint(expr= - 7*m.b117 + m.x767 - m.x976 >= -7)

m.c1943 = Constraint(expr= - 7*m.b118 + m.x768 - m.x977 >= -7)

m.c1944 = Constraint(expr= - 7*m.b119 + m.x769 - m.x978 >= -7)

m.c1945 = Constraint(expr= - 7*m.b121 + m.x781 - m.x980 >= -7)

m.c1946 = Constraint(expr= - 7*m.b122 + m.x782 - m.x981 >= -7)

m.c1947 = Constraint(expr= - 7*m.b123 + m.x783 - m.x982 >= -7)

m.c1948 = Constraint(expr= - 7*m.b124 + m.x784 - m.x983 >= -7)

m.c1949 = Constraint(expr= - 7*m.b121 + m.x786 - m.x980 >= -7)

m.c1950 = Constraint(expr= - 7*m.b122 + m.x787 - m.x981 >= -7)

m.c1951 = Constraint(expr= - 7*m.b123 + m.x788 - m.x982 >= -7)

m.c1952 = Constraint(expr= - 7*m.b124 + m.x789 - m.x983 >= -7)

m.c1953 = Constraint(expr= - 7*m.b126 + m.x776 - m.x985 >= -7)

m.c1954 = Constraint(expr= - 7*m.b127 + m.x777 - m.x986 >= -7)

m.c1955 = Constraint(expr= - 7*m.b128 + m.x778 - m.x987 >= -7)

m.c1956 = Constraint(expr= - 7*m.b129 + m.x779 - m.x988 >= -7)

m.c1957 = Constraint(expr= - 7*m.b126 + m.x786 - m.x985 >= -7)

m.c1958 = Constraint(expr= - 7*m.b127 + m.x787 - m.x986 >= -7)

m.c1959 = Constraint(expr= - 7*m.b128 + m.x788 - m.x987 >= -7)

m.c1960 = Constraint(expr= - 7*m.b129 + m.x789 - m.x988 >= -7)

m.c1961 = Constraint(expr= - 7*m.b131 + m.x776 - m.x990 >= -7)

m.c1962 = Constraint(expr= - 7*m.b132 + m.x777 - m.x991 >= -7)

m.c1963 = Constraint(expr= - 7*m.b133 + m.x778 - m.x992 >= -7)

m.c1964 = Constraint(expr= - 7*m.b134 + m.x779 - m.x993 >= -7)

m.c1965 = Constraint(expr= - 7*m.b131 + m.x781 - m.x990 >= -7)

m.c1966 = Constraint(expr= - 7*m.b132 + m.x782 - m.x991 >= -7)

m.c1967 = Constraint(expr= - 7*m.b133 + m.x783 - m.x992 >= -7)

m.c1968 = Constraint(expr= - 7*m.b134 + m.x784 - m.x993 >= -7)

m.c1969 = Constraint(expr= - 7*m.b136 + m.x796 - m.x995 >= -7)

m.c1970 = Constraint(expr= - 7*m.b137 + m.x797 - m.x996 >= -7)

m.c1971 = Constraint(expr= - 7*m.b138 + m.x798 - m.x997 >= -7)

m.c1972 = Constraint(expr= - 7*m.b139 + m.x799 - m.x998 >= -7)

m.c1973 = Constraint(expr= - 7*m.b141 + m.x791 - m.x1000 >= -7)

m.c1974 = Constraint(expr= - 7*m.b142 + m.x792 - m.x1001 >= -7)

m.c1975 = Constraint(expr= - 7*m.b143 + m.x793 - m.x1002 >= -7)

m.c1976 = Constraint(expr= - 7*m.b144 + m.x794 - m.x1003 >= -7)

m.c1977 = Constraint(expr= - 7*m.b151 + m.x811 - m.x1010 >= -7)

m.c1978 = Constraint(expr= - 7*m.b152 + m.x812 - m.x1011 >= -7)

m.c1979 = Constraint(expr= - 7*m.b153 + m.x813 - m.x1012 >= -7)

m.c1980 = Constraint(expr= - 7*m.b154 + m.x814 - m.x1013 >= -7)

m.c1981 = Constraint(expr= - 7*m.b156 + m.x806 - m.x1015 >= -7)

m.c1982 = Constraint(expr= - 7*m.b157 + m.x807 - m.x1016 >= -7)

m.c1983 = Constraint(expr= - 7*m.b158 + m.x808 - m.x1017 >= -7)

m.c1984 = Constraint(expr= - 7*m.b159 + m.x809 - m.x1018 >= -7)

m.c1985 = Constraint(expr= - 7*m.b166 + m.x826 - m.x1025 >= -7)

m.c1986 = Constraint(expr= - 7*m.b167 + m.x827 - m.x1026 >= -7)

m.c1987 = Constraint(expr= - 7*m.b168 + m.x828 - m.x1027 >= -7)

m.c1988 = Constraint(expr= - 7*m.b169 + m.x829 - m.x1028 >= -7)

m.c1989 = Constraint(expr= - 7*m.b166 + m.x831 - m.x1025 >= -7)

m.c1990 = Constraint(expr= - 7*m.b167 + m.x832 - m.x1026 >= -7)

m.c1991 = Constraint(expr= - 7*m.b168 + m.x833 - m.x1027 >= -7)

m.c1992 = Constraint(expr= - 7*m.b169 + m.x834 - m.x1028 >= -7)

m.c1993 = Constraint(expr= - 7*m.b171 + m.x821 - m.x1030 >= -7)

m.c1994 = Constraint(expr= - 7*m.b172 + m.x822 - m.x1031 >= -7)

m.c1995 = Constraint(expr= - 7*m.b173 + m.x823 - m.x1032 >= -7)

m.c1996 = Constraint(expr= - 7*m.b174 + m.x824 - m.x1033 >= -7)

m.c1997 = Constraint(expr= - 7*m.b171 + m.x831 - m.x1030 >= -7)

m.c1998 = Constraint(expr= - 7*m.b172 + m.x832 - m.x1031 >= -7)

m.c1999 = Constraint(expr= - 7*m.b173 + m.x833 - m.x1032 >= -7)

m.c2000 = Constraint(expr= - 7*m.b174 + m.x834 - m.x1033 >= -7)

m.c2001 = Constraint(expr= - 7*m.b176 + m.x821 - m.x1035 >= -7)

m.c2002 = Constraint(expr= - 7*m.b177 + m.x822 - m.x1036 >= -7)

m.c2003 = Constraint(expr= - 7*m.b178 + m.x823 - m.x1037 >= -7)

m.c2004 = Constraint(expr= - 7*m.b179 + m.x824 - m.x1038 >= -7)

m.c2005 = Constraint(expr= - 7*m.b176 + m.x826 - m.x1035 >= -7)

m.c2006 = Constraint(expr= - 7*m.b177 + m.x827 - m.x1036 >= -7)

m.c2007 = Constraint(expr= - 7*m.b178 + m.x828 - m.x1037 >= -7)

m.c2008 = Constraint(expr= - 7*m.b179 + m.x829 - m.x1038 >= -7)

m.c2009 = Constraint(expr= - 7*m.b181 + m.x841 - m.x1040 >= -7)

m.c2010 = Constraint(expr= - 7*m.b182 + m.x842 - m.x1041 >= -7)

m.c2011 = Constraint(expr= - 7*m.b183 + m.x843 - m.x1042 >= -7)

m.c2012 = Constraint(expr= - 7*m.b184 + m.x844 - m.x1043 >= -7)

m.c2013 = Constraint(expr= - 7*m.b181 + m.x846 - m.x1040 >= -7)

m.c2014 = Constraint(expr= - 7*m.b182 + m.x847 - m.x1041 >= -7)

m.c2015 = Constraint(expr= - 7*m.b183 + m.x848 - m.x1042 >= -7)

m.c2016 = Constraint(expr= - 7*m.b184 + m.x849 - m.x1043 >= -7)

m.c2017 = Constraint(expr= - 7*m.b186 + m.x836 - m.x1045 >= -7)

m.c2018 = Constraint(expr= - 7*m.b187 + m.x837 - m.x1046 >= -7)

m.c2019 = Constraint(expr= - 7*m.b188 + m.x838 - m.x1047 >= -7)

m.c2020 = Constraint(expr= - 7*m.b189 + m.x839 - m.x1048 >= -7)

m.c2021 = Constraint(expr= - 7*m.b186 + m.x846 - m.x1045 >= -7)

m.c2022 = Constraint(expr= - 7*m.b187 + m.x847 - m.x1046 >= -7)

m.c2023 = Constraint(expr= - 7*m.b188 + m.x848 - m.x1047 >= -7)

m.c2024 = Constraint(expr= - 7*m.b189 + m.x849 - m.x1048 >= -7)

m.c2025 = Constraint(expr= - 7*m.b191 + m.x836 - m.x1050 >= -7)

m.c2026 = Constraint(expr= - 7*m.b192 + m.x837 - m.x1051 >= -7)

m.c2027 = Constraint(expr= - 7*m.b193 + m.x838 - m.x1052 >= -7)

m.c2028 = Constraint(expr= - 7*m.b194 + m.x839 - m.x1053 >= -7)

m.c2029 = Constraint(expr= - 7*m.b191 + m.x841 - m.x1050 >= -7)

m.c2030 = Constraint(expr= - 7*m.b192 + m.x842 - m.x1051 >= -7)

m.c2031 = Constraint(expr= - 7*m.b193 + m.x843 - m.x1052 >= -7)

m.c2032 = Constraint(expr= - 7*m.b194 + m.x844 - m.x1053 >= -7)

m.c2033 = Constraint(expr= - 7*m.b1 + m.x671 - m.x860 >= -7)

m.c2034 = Constraint(expr= - 7*m.b2 + m.x672 - m.x861 >= -7)

m.c2035 = Constraint(expr= - 7*m.b3 + m.x673 - m.x862 >= -7)

m.c2036 = Constraint(expr= - 7*m.b4 + m.x674 - m.x863 >= -7)

m.c2037 = Constraint(expr= - 7*m.b6 + m.x676 - m.x865 >= -7)

m.c2038 = Constraint(expr= - 7*m.b7 + m.x677 - m.x866 >= -7)

m.c2039 = Constraint(expr= - 7*m.b8 + m.x678 - m.x867 >= -7)

m.c2040 = Constraint(expr= - 7*m.b9 + m.x679 - m.x868 >= -7)

m.c2041 = Constraint(expr= - 7*m.b11 + m.x681 - m.x870 >= -7)

m.c2042 = Constraint(expr= - 7*m.b12 + m.x682 - m.x871 >= -7)

m.c2043 = Constraint(expr= - 7*m.b13 + m.x683 - m.x872 >= -7)

m.c2044 = Constraint(expr= - 7*m.b14 + m.x684 - m.x873 >= -7)

m.c2045 = Constraint(expr= - 7*m.b1 + m.x686 - m.x860 >= -7)

m.c2046 = Constraint(expr= - 7*m.b2 + m.x687 - m.x861 >= -7)

m.c2047 = Constraint(expr= - 7*m.b3 + m.x688 - m.x862 >= -7)

m.c2048 = Constraint(expr= - 7*m.b4 + m.x689 - m.x863 >= -7)

m.c2049 = Constraint(expr= - 7*m.b6 + m.x691 - m.x865 >= -7)

m.c2050 = Constraint(expr= - 7*m.b7 + m.x692 - m.x866 >= -7)

m.c2051 = Constraint(expr= - 7*m.b8 + m.x693 - m.x867 >= -7)

m.c2052 = Constraint(expr= - 7*m.b9 + m.x694 - m.x868 >= -7)

m.c2053 = Constraint(expr= - 7*m.b11 + m.x696 - m.x870 >= -7)

m.c2054 = Constraint(expr= - 7*m.b12 + m.x697 - m.x871 >= -7)

m.c2055 = Constraint(expr= - 7*m.b13 + m.x698 - m.x872 >= -7)

m.c2056 = Constraint(expr= - 7*m.b14 + m.x699 - m.x873 >= -7)

m.c2057 = Constraint(expr= - 7*m.b1 + m.x701 - m.x860 >= -7)

m.c2058 = Constraint(expr= - 7*m.b2 + m.x702 - m.x861 >= -7)

m.c2059 = Constraint(expr= - 7*m.b3 + m.x703 - m.x862 >= -7)

m.c2060 = Constraint(expr= - 7*m.b4 + m.x704 - m.x863 >= -7)

m.c2061 = Constraint(expr= - 7*m.b6 + m.x706 - m.x865 >= -7)

m.c2062 = Constraint(expr= - 7*m.b7 + m.x707 - m.x866 >= -7)

m.c2063 = Constraint(expr= - 7*m.b8 + m.x708 - m.x867 >= -7)

m.c2064 = Constraint(expr= - 7*m.b9 + m.x709 - m.x868 >= -7)

m.c2065 = Constraint(expr= - 7*m.b11 + m.x711 - m.x870 >= -7)

m.c2066 = Constraint(expr= - 7*m.b12 + m.x712 - m.x871 >= -7)

m.c2067 = Constraint(expr= - 7*m.b13 + m.x713 - m.x872 >= -7)

m.c2068 = Constraint(expr= - 7*m.b14 + m.x714 - m.x873 >= -7)

m.c2069 = Constraint(expr= - 7*m.b1 + m.x716 - m.x860 >= -7)

m.c2070 = Constraint(expr= - 7*m.b2 + m.x717 - m.x861 >= -7)

m.c2071 = Constraint(expr= - 7*m.b3 + m.x718 - m.x862 >= -7)

m.c2072 = Constraint(expr= - 7*m.b4 + m.x719 - m.x863 >= -7)

m.c2073 = Constraint(expr= - 7*m.b6 + m.x721 - m.x865 >= -7)

m.c2074 = Constraint(expr= - 7*m.b7 + m.x722 - m.x866 >= -7)

m.c2075 = Constraint(expr= - 7*m.b8 + m.x723 - m.x867 >= -7)

m.c2076 = Constraint(expr= - 7*m.b9 + m.x724 - m.x868 >= -7)

m.c2077 = Constraint(expr= - 7*m.b11 + m.x726 - m.x870 >= -7)

m.c2078 = Constraint(expr= - 7*m.b12 + m.x727 - m.x871 >= -7)

m.c2079 = Constraint(expr= - 7*m.b13 + m.x728 - m.x872 >= -7)

m.c2080 = Constraint(expr= - 7*m.b14 + m.x729 - m.x873 >= -7)

m.c2081 = Constraint(expr= - 7*m.b1 + m.x731 - m.x860 >= -7)

m.c2082 = Constraint(expr= - 7*m.b2 + m.x732 - m.x861 >= -7)

m.c2083 = Constraint(expr= - 7*m.b3 + m.x733 - m.x862 >= -7)

m.c2084 = Constraint(expr= - 7*m.b4 + m.x734 - m.x863 >= -7)

m.c2085 = Constraint(expr= - 7*m.b6 + m.x736 - m.x865 >= -7)

m.c2086 = Constraint(expr= - 7*m.b7 + m.x737 - m.x866 >= -7)

m.c2087 = Constraint(expr= - 7*m.b8 + m.x738 - m.x867 >= -7)

m.c2088 = Constraint(expr= - 7*m.b9 + m.x739 - m.x868 >= -7)

m.c2089 = Constraint(expr= - 7*m.b11 + m.x741 - m.x870 >= -7)

m.c2090 = Constraint(expr= - 7*m.b12 + m.x742 - m.x871 >= -7)

m.c2091 = Constraint(expr= - 7*m.b13 + m.x743 - m.x872 >= -7)

m.c2092 = Constraint(expr= - 7*m.b14 + m.x744 - m.x873 >= -7)

m.c2093 = Constraint(expr= - 7*m.b1 + m.x746 - m.x860 >= -7)

m.c2094 = Constraint(expr= - 7*m.b2 + m.x747 - m.x861 >= -7)

m.c2095 = Constraint(expr= - 7*m.b3 + m.x748 - m.x862 >= -7)

m.c2096 = Constraint(expr= - 7*m.b4 + m.x749 - m.x863 >= -7)

m.c2097 = Constraint(expr= - 7*m.b6 + m.x751 - m.x865 >= -7)

m.c2098 = Constraint(expr= - 7*m.b7 + m.x752 - m.x866 >= -7)

m.c2099 = Constraint(expr= - 7*m.b8 + m.x753 - m.x867 >= -7)

m.c2100 = Constraint(expr= - 7*m.b9 + m.x754 - m.x868 >= -7)

m.c2101 = Constraint(expr= - 7*m.b11 + m.x756 - m.x870 >= -7)

m.c2102 = Constraint(expr= - 7*m.b12 + m.x757 - m.x871 >= -7)

m.c2103 = Constraint(expr= - 7*m.b13 + m.x758 - m.x872 >= -7)

m.c2104 = Constraint(expr= - 7*m.b14 + m.x759 - m.x873 >= -7)

m.c2105 = Constraint(expr= - 7*m.b1 + m.x761 - m.x860 >= -7)

m.c2106 = Constraint(expr= - 7*m.b2 + m.x762 - m.x861 >= -7)

m.c2107 = Constraint(expr= - 7*m.b3 + m.x763 - m.x862 >= -7)

m.c2108 = Constraint(expr= - 7*m.b4 + m.x764 - m.x863 >= -7)

m.c2109 = Constraint(expr= - 7*m.b6 + m.x766 - m.x865 >= -7)

m.c2110 = Constraint(expr= - 7*m.b7 + m.x767 - m.x866 >= -7)

m.c2111 = Constraint(expr= - 7*m.b8 + m.x768 - m.x867 >= -7)

m.c2112 = Constraint(expr= - 7*m.b9 + m.x769 - m.x868 >= -7)

m.c2113 = Constraint(expr= - 7*m.b11 + m.x771 - m.x870 >= -7)

m.c2114 = Constraint(expr= - 7*m.b12 + m.x772 - m.x871 >= -7)

m.c2115 = Constraint(expr= - 7*m.b13 + m.x773 - m.x872 >= -7)

m.c2116 = Constraint(expr= - 7*m.b14 + m.x774 - m.x873 >= -7)

m.c2117 = Constraint(expr= - 7*m.b1 + m.x776 - m.x860 >= -7)

m.c2118 = Constraint(expr= - 7*m.b2 + m.x777 - m.x861 >= -7)

m.c2119 = Constraint(expr= - 7*m.b3 + m.x778 - m.x862 >= -7)

m.c2120 = Constraint(expr= - 7*m.b4 + m.x779 - m.x863 >= -7)

m.c2121 = Constraint(expr= - 7*m.b6 + m.x781 - m.x865 >= -7)

m.c2122 = Constraint(expr= - 7*m.b7 + m.x782 - m.x866 >= -7)

m.c2123 = Constraint(expr= - 7*m.b8 + m.x783 - m.x867 >= -7)

m.c2124 = Constraint(expr= - 7*m.b9 + m.x784 - m.x868 >= -7)

m.c2125 = Constraint(expr= - 7*m.b11 + m.x786 - m.x870 >= -7)

m.c2126 = Constraint(expr= - 7*m.b12 + m.x787 - m.x871 >= -7)

m.c2127 = Constraint(expr= - 7*m.b13 + m.x788 - m.x872 >= -7)

m.c2128 = Constraint(expr= - 7*m.b14 + m.x789 - m.x873 >= -7)

m.c2129 = Constraint(expr= - 7*m.b1 + m.x821 - m.x860 >= -7)

m.c2130 = Constraint(expr= - 7*m.b2 + m.x822 - m.x861 >= -7)

m.c2131 = Constraint(expr= - 7*m.b3 + m.x823 - m.x862 >= -7)

m.c2132 = Constraint(expr= - 7*m.b4 + m.x824 - m.x863 >= -7)

m.c2133 = Constraint(expr= - 7*m.b6 + m.x826 - m.x865 >= -7)

m.c2134 = Constraint(expr= - 7*m.b7 + m.x827 - m.x866 >= -7)

m.c2135 = Constraint(expr= - 7*m.b8 + m.x828 - m.x867 >= -7)

m.c2136 = Constraint(expr= - 7*m.b9 + m.x829 - m.x868 >= -7)

m.c2137 = Constraint(expr= - 7*m.b11 + m.x831 - m.x870 >= -7)

m.c2138 = Constraint(expr= - 7*m.b12 + m.x832 - m.x871 >= -7)

m.c2139 = Constraint(expr= - 7*m.b13 + m.x833 - m.x872 >= -7)

m.c2140 = Constraint(expr= - 7*m.b14 + m.x834 - m.x873 >= -7)

m.c2141 = Constraint(expr= - 7*m.b1 + m.x836 - m.x860 >= -7)

m.c2142 = Constraint(expr= - 7*m.b2 + m.x837 - m.x861 >= -7)

m.c2143 = Constraint(expr= - 7*m.b3 + m.x838 - m.x862 >= -7)

m.c2144 = Constraint(expr= - 7*m.b4 + m.x839 - m.x863 >= -7)

m.c2145 = Constraint(expr= - 7*m.b6 + m.x841 - m.x865 >= -7)

m.c2146 = Constraint(expr= - 7*m.b7 + m.x842 - m.x866 >= -7)

m.c2147 = Constraint(expr= - 7*m.b8 + m.x843 - m.x867 >= -7)

m.c2148 = Constraint(expr= - 7*m.b9 + m.x844 - m.x868 >= -7)

m.c2149 = Constraint(expr= - 7*m.b11 + m.x846 - m.x870 >= -7)

m.c2150 = Constraint(expr= - 7*m.b12 + m.x847 - m.x871 >= -7)

m.c2151 = Constraint(expr= - 7*m.b13 + m.x848 - m.x872 >= -7)

m.c2152 = Constraint(expr= - 7*m.b14 + m.x849 - m.x873 >= -7)

m.c2153 = Constraint(expr= - 7*m.b16 + m.x656 - m.x875 >= -7)

m.c2154 = Constraint(expr= - 7*m.b17 + m.x657 - m.x876 >= -7)

m.c2155 = Constraint(expr= - 7*m.b18 + m.x658 - m.x877 >= -7)

m.c2156 = Constraint(expr= - 7*m.b19 + m.x659 - m.x878 >= -7)

m.c2157 = Constraint(expr= - 7*m.b21 + m.x661 - m.x880 >= -7)

m.c2158 = Constraint(expr= - 7*m.b22 + m.x662 - m.x881 >= -7)

m.c2159 = Constraint(expr= - 7*m.b23 + m.x663 - m.x882 >= -7)

m.c2160 = Constraint(expr= - 7*m.b24 + m.x664 - m.x883 >= -7)

m.c2161 = Constraint(expr= - 7*m.b26 + m.x666 - m.x885 >= -7)

m.c2162 = Constraint(expr= - 7*m.b27 + m.x667 - m.x886 >= -7)

m.c2163 = Constraint(expr= - 7*m.b28 + m.x668 - m.x887 >= -7)

m.c2164 = Constraint(expr= - 7*m.b29 + m.x669 - m.x888 >= -7)

m.c2165 = Constraint(expr= - 7*m.b16 + m.x686 - m.x875 >= -7)

m.c2166 = Constraint(expr= - 7*m.b17 + m.x687 - m.x876 >= -7)

m.c2167 = Constraint(expr= - 7*m.b18 + m.x688 - m.x877 >= -7)

m.c2168 = Constraint(expr= - 7*m.b19 + m.x689 - m.x878 >= -7)

m.c2169 = Constraint(expr= - 7*m.b21 + m.x691 - m.x880 >= -7)

m.c2170 = Constraint(expr= - 7*m.b22 + m.x692 - m.x881 >= -7)

m.c2171 = Constraint(expr= - 7*m.b23 + m.x693 - m.x882 >= -7)

m.c2172 = Constraint(expr= - 7*m.b24 + m.x694 - m.x883 >= -7)

m.c2173 = Constraint(expr= - 7*m.b26 + m.x696 - m.x885 >= -7)

m.c2174 = Constraint(expr= - 7*m.b27 + m.x697 - m.x886 >= -7)

m.c2175 = Constraint(expr= - 7*m.b28 + m.x698 - m.x887 >= -7)

m.c2176 = Constraint(expr= - 7*m.b29 + m.x699 - m.x888 >= -7)

m.c2177 = Constraint(expr= - 7*m.b16 + m.x701 - m.x875 >= -7)

m.c2178 = Constraint(expr= - 7*m.b17 + m.x702 - m.x876 >= -7)

m.c2179 = Constraint(expr= - 7*m.b18 + m.x703 - m.x877 >= -7)

m.c2180 = Constraint(expr= - 7*m.b19 + m.x704 - m.x878 >= -7)

m.c2181 = Constraint(expr= - 7*m.b21 + m.x706 - m.x880 >= -7)

m.c2182 = Constraint(expr= - 7*m.b22 + m.x707 - m.x881 >= -7)

m.c2183 = Constraint(expr= - 7*m.b23 + m.x708 - m.x882 >= -7)

m.c2184 = Constraint(expr= - 7*m.b24 + m.x709 - m.x883 >= -7)

m.c2185 = Constraint(expr= - 7*m.b26 + m.x711 - m.x885 >= -7)

m.c2186 = Constraint(expr= - 7*m.b27 + m.x712 - m.x886 >= -7)

m.c2187 = Constraint(expr= - 7*m.b28 + m.x713 - m.x887 >= -7)

m.c2188 = Constraint(expr= - 7*m.b29 + m.x714 - m.x888 >= -7)

m.c2189 = Constraint(expr= - 7*m.b16 + m.x716 - m.x875 >= -7)

m.c2190 = Constraint(expr= - 7*m.b17 + m.x717 - m.x876 >= -7)

m.c2191 = Constraint(expr= - 7*m.b18 + m.x718 - m.x877 >= -7)

m.c2192 = Constraint(expr= - 7*m.b19 + m.x719 - m.x878 >= -7)

m.c2193 = Constraint(expr= - 7*m.b21 + m.x721 - m.x880 >= -7)

m.c2194 = Constraint(expr= - 7*m.b22 + m.x722 - m.x881 >= -7)

m.c2195 = Constraint(expr= - 7*m.b23 + m.x723 - m.x882 >= -7)

m.c2196 = Constraint(expr= - 7*m.b24 + m.x724 - m.x883 >= -7)

m.c2197 = Constraint(expr= - 7*m.b26 + m.x726 - m.x885 >= -7)

m.c2198 = Constraint(expr= - 7*m.b27 + m.x727 - m.x886 >= -7)

m.c2199 = Constraint(expr= - 7*m.b28 + m.x728 - m.x887 >= -7)

m.c2200 = Constraint(expr= - 7*m.b29 + m.x729 - m.x888 >= -7)

m.c2201 = Constraint(expr= - 7*m.b16 + m.x731 - m.x875 >= -7)

m.c2202 = Constraint(expr= - 7*m.b17 + m.x732 - m.x876 >= -7)

m.c2203 = Constraint(expr= - 7*m.b18 + m.x733 - m.x877 >= -7)

m.c2204 = Constraint(expr= - 7*m.b19 + m.x734 - m.x878 >= -7)

m.c2205 = Constraint(expr= - 7*m.b21 + m.x736 - m.x880 >= -7)

m.c2206 = Constraint(expr= - 7*m.b22 + m.x737 - m.x881 >= -7)

m.c2207 = Constraint(expr= - 7*m.b23 + m.x738 - m.x882 >= -7)

m.c2208 = Constraint(expr= - 7*m.b24 + m.x739 - m.x883 >= -7)

m.c2209 = Constraint(expr= - 7*m.b26 + m.x741 - m.x885 >= -7)

m.c2210 = Constraint(expr= - 7*m.b27 + m.x742 - m.x886 >= -7)

m.c2211 = Constraint(expr= - 7*m.b28 + m.x743 - m.x887 >= -7)

m.c2212 = Constraint(expr= - 7*m.b29 + m.x744 - m.x888 >= -7)

m.c2213 = Constraint(expr= - 7*m.b16 + m.x746 - m.x875 >= -7)

m.c2214 = Constraint(expr= - 7*m.b17 + m.x747 - m.x876 >= -7)

m.c2215 = Constraint(expr= - 7*m.b18 + m.x748 - m.x877 >= -7)

m.c2216 = Constraint(expr= - 7*m.b19 + m.x749 - m.x878 >= -7)

m.c2217 = Constraint(expr= - 7*m.b21 + m.x751 - m.x880 >= -7)

m.c2218 = Constraint(expr= - 7*m.b22 + m.x752 - m.x881 >= -7)

m.c2219 = Constraint(expr= - 7*m.b23 + m.x753 - m.x882 >= -7)

m.c2220 = Constraint(expr= - 7*m.b24 + m.x754 - m.x883 >= -7)

m.c2221 = Constraint(expr= - 7*m.b26 + m.x756 - m.x885 >= -7)

m.c2222 = Constraint(expr= - 7*m.b27 + m.x757 - m.x886 >= -7)

m.c2223 = Constraint(expr= - 7*m.b28 + m.x758 - m.x887 >= -7)

m.c2224 = Constraint(expr= - 7*m.b29 + m.x759 - m.x888 >= -7)

m.c2225 = Constraint(expr= - 7*m.b16 + m.x761 - m.x875 >= -7)

m.c2226 = Constraint(expr= - 7*m.b17 + m.x762 - m.x876 >= -7)

m.c2227 = Constraint(expr= - 7*m.b18 + m.x763 - m.x877 >= -7)

m.c2228 = Constraint(expr= - 7*m.b19 + m.x764 - m.x878 >= -7)

m.c2229 = Constraint(expr= - 7*m.b21 + m.x766 - m.x880 >= -7)

m.c2230 = Constraint(expr= - 7*m.b22 + m.x767 - m.x881 >= -7)

m.c2231 = Constraint(expr= - 7*m.b23 + m.x768 - m.x882 >= -7)

m.c2232 = Constraint(expr= - 7*m.b24 + m.x769 - m.x883 >= -7)

m.c2233 = Constraint(expr= - 7*m.b26 + m.x771 - m.x885 >= -7)

m.c2234 = Constraint(expr= - 7*m.b27 + m.x772 - m.x886 >= -7)

m.c2235 = Constraint(expr= - 7*m.b28 + m.x773 - m.x887 >= -7)

m.c2236 = Constraint(expr= - 7*m.b29 + m.x774 - m.x888 >= -7)

m.c2237 = Constraint(expr= - 7*m.b16 + m.x776 - m.x875 >= -7)

m.c2238 = Constraint(expr= - 7*m.b17 + m.x777 - m.x876 >= -7)

m.c2239 = Constraint(expr= - 7*m.b18 + m.x778 - m.x877 >= -7)

m.c2240 = Constraint(expr= - 7*m.b19 + m.x779 - m.x878 >= -7)

m.c2241 = Constraint(expr= - 7*m.b21 + m.x781 - m.x880 >= -7)

m.c2242 = Constraint(expr= - 7*m.b22 + m.x782 - m.x881 >= -7)

m.c2243 = Constraint(expr= - 7*m.b23 + m.x783 - m.x882 >= -7)

m.c2244 = Constraint(expr= - 7*m.b24 + m.x784 - m.x883 >= -7)

m.c2245 = Constraint(expr= - 7*m.b26 + m.x786 - m.x885 >= -7)

m.c2246 = Constraint(expr= - 7*m.b27 + m.x787 - m.x886 >= -7)

m.c2247 = Constraint(expr= - 7*m.b28 + m.x788 - m.x887 >= -7)

m.c2248 = Constraint(expr= - 7*m.b29 + m.x789 - m.x888 >= -7)

m.c2249 = Constraint(expr= - 7*m.b16 + m.x821 - m.x875 >= -7)

m.c2250 = Constraint(expr= - 7*m.b17 + m.x822 - m.x876 >= -7)

m.c2251 = Constraint(expr= - 7*m.b18 + m.x823 - m.x877 >= -7)

m.c2252 = Constraint(expr= - 7*m.b19 + m.x824 - m.x878 >= -7)

m.c2253 = Constraint(expr= - 7*m.b21 + m.x826 - m.x880 >= -7)

m.c2254 = Constraint(expr= - 7*m.b22 + m.x827 - m.x881 >= -7)

m.c2255 = Constraint(expr= - 7*m.b23 + m.x828 - m.x882 >= -7)

m.c2256 = Constraint(expr= - 7*m.b24 + m.x829 - m.x883 >= -7)

m.c2257 = Constraint(expr= - 7*m.b26 + m.x831 - m.x885 >= -7)

m.c2258 = Constraint(expr= - 7*m.b27 + m.x832 - m.x886 >= -7)

m.c2259 = Constraint(expr= - 7*m.b28 + m.x833 - m.x887 >= -7)

m.c2260 = Constraint(expr= - 7*m.b29 + m.x834 - m.x888 >= -7)

m.c2261 = Constraint(expr= - 7*m.b16 + m.x836 - m.x875 >= -7)

m.c2262 = Constraint(expr= - 7*m.b17 + m.x837 - m.x876 >= -7)

m.c2263 = Constraint(expr= - 7*m.b18 + m.x838 - m.x877 >= -7)

m.c2264 = Constraint(expr= - 7*m.b19 + m.x839 - m.x878 >= -7)

m.c2265 = Constraint(expr= - 7*m.b21 + m.x841 - m.x880 >= -7)

m.c2266 = Constraint(expr= - 7*m.b22 + m.x842 - m.x881 >= -7)

m.c2267 = Constraint(expr= - 7*m.b23 + m.x843 - m.x882 >= -7)

m.c2268 = Constraint(expr= - 7*m.b24 + m.x844 - m.x883 >= -7)

m.c2269 = Constraint(expr= - 7*m.b26 + m.x846 - m.x885 >= -7)

m.c2270 = Constraint(expr= - 7*m.b27 + m.x847 - m.x886 >= -7)

m.c2271 = Constraint(expr= - 7*m.b28 + m.x848 - m.x887 >= -7)

m.c2272 = Constraint(expr= - 7*m.b29 + m.x849 - m.x888 >= -7)

m.c2273 = Constraint(expr= - 7*m.b31 + m.x656 - m.x890 >= -7)

m.c2274 = Constraint(expr= - 7*m.b32 + m.x657 - m.x891 >= -7)

m.c2275 = Constraint(expr= - 7*m.b33 + m.x658 - m.x892 >= -7)

m.c2276 = Constraint(expr= - 7*m.b34 + m.x659 - m.x893 >= -7)

m.c2277 = Constraint(expr= - 7*m.b36 + m.x661 - m.x895 >= -7)

m.c2278 = Constraint(expr= - 7*m.b37 + m.x662 - m.x896 >= -7)

m.c2279 = Constraint(expr= - 7*m.b38 + m.x663 - m.x897 >= -7)

m.c2280 = Constraint(expr= - 7*m.b39 + m.x664 - m.x898 >= -7)

m.c2281 = Constraint(expr= - 7*m.b41 + m.x666 - m.x900 >= -7)

m.c2282 = Constraint(expr= - 7*m.b42 + m.x667 - m.x901 >= -7)

m.c2283 = Constraint(expr= - 7*m.b43 + m.x668 - m.x902 >= -7)

m.c2284 = Constraint(expr= - 7*m.b44 + m.x669 - m.x903 >= -7)

m.c2285 = Constraint(expr= - 7*m.b31 + m.x671 - m.x890 >= -7)

m.c2286 = Constraint(expr= - 7*m.b32 + m.x672 - m.x891 >= -7)

m.c2287 = Constraint(expr= - 7*m.b33 + m.x673 - m.x892 >= -7)

m.c2288 = Constraint(expr= - 7*m.b34 + m.x674 - m.x893 >= -7)

m.c2289 = Constraint(expr= - 7*m.b36 + m.x676 - m.x895 >= -7)

m.c2290 = Constraint(expr= - 7*m.b37 + m.x677 - m.x896 >= -7)

m.c2291 = Constraint(expr= - 7*m.b38 + m.x678 - m.x897 >= -7)

m.c2292 = Constraint(expr= - 7*m.b39 + m.x679 - m.x898 >= -7)

m.c2293 = Constraint(expr= - 7*m.b41 + m.x681 - m.x900 >= -7)

m.c2294 = Constraint(expr= - 7*m.b42 + m.x682 - m.x901 >= -7)

m.c2295 = Constraint(expr= - 7*m.b43 + m.x683 - m.x902 >= -7)

m.c2296 = Constraint(expr= - 7*m.b44 + m.x684 - m.x903 >= -7)

m.c2297 = Constraint(expr= - 7*m.b31 + m.x701 - m.x890 >= -7)

m.c2298 = Constraint(expr= - 7*m.b32 + m.x702 - m.x891 >= -7)

m.c2299 = Constraint(expr= - 7*m.b33 + m.x703 - m.x892 >= -7)

m.c2300 = Constraint(expr= - 7*m.b34 + m.x704 - m.x893 >= -7)

m.c2301 = Constraint(expr= - 7*m.b36 + m.x706 - m.x895 >= -7)

m.c2302 = Constraint(expr= - 7*m.b37 + m.x707 - m.x896 >= -7)

m.c2303 = Constraint(expr= - 7*m.b38 + m.x708 - m.x897 >= -7)

m.c2304 = Constraint(expr= - 7*m.b39 + m.x709 - m.x898 >= -7)

m.c2305 = Constraint(expr= - 7*m.b41 + m.x711 - m.x900 >= -7)

m.c2306 = Constraint(expr= - 7*m.b42 + m.x712 - m.x901 >= -7)

m.c2307 = Constraint(expr= - 7*m.b43 + m.x713 - m.x902 >= -7)

m.c2308 = Constraint(expr= - 7*m.b44 + m.x714 - m.x903 >= -7)

m.c2309 = Constraint(expr= - 7*m.b31 + m.x716 - m.x890 >= -7)

m.c2310 = Constraint(expr= - 7*m.b32 + m.x717 - m.x891 >= -7)

m.c2311 = Constraint(expr= - 7*m.b33 + m.x718 - m.x892 >= -7)

m.c2312 = Constraint(expr= - 7*m.b34 + m.x719 - m.x893 >= -7)

m.c2313 = Constraint(expr= - 7*m.b36 + m.x721 - m.x895 >= -7)

m.c2314 = Constraint(expr= - 7*m.b37 + m.x722 - m.x896 >= -7)

m.c2315 = Constraint(expr= - 7*m.b38 + m.x723 - m.x897 >= -7)

m.c2316 = Constraint(expr= - 7*m.b39 + m.x724 - m.x898 >= -7)

m.c2317 = Constraint(expr= - 7*m.b41 + m.x726 - m.x900 >= -7)

m.c2318 = Constraint(expr= - 7*m.b42 + m.x727 - m.x901 >= -7)

m.c2319 = Constraint(expr= - 7*m.b43 + m.x728 - m.x902 >= -7)

m.c2320 = Constraint(expr= - 7*m.b44 + m.x729 - m.x903 >= -7)

m.c2321 = Constraint(expr= - 7*m.b31 + m.x731 - m.x890 >= -7)

m.c2322 = Constraint(expr= - 7*m.b32 + m.x732 - m.x891 >= -7)

m.c2323 = Constraint(expr= - 7*m.b33 + m.x733 - m.x892 >= -7)

m.c2324 = Constraint(expr= - 7*m.b34 + m.x734 - m.x893 >= -7)

m.c2325 = Constraint(expr= - 7*m.b36 + m.x736 - m.x895 >= -7)

m.c2326 = Constraint(expr= - 7*m.b37 + m.x737 - m.x896 >= -7)

m.c2327 = Constraint(expr= - 7*m.b38 + m.x738 - m.x897 >= -7)

m.c2328 = Constraint(expr= - 7*m.b39 + m.x739 - m.x898 >= -7)

m.c2329 = Constraint(expr= - 7*m.b41 + m.x741 - m.x900 >= -7)

m.c2330 = Constraint(expr= - 7*m.b42 + m.x742 - m.x901 >= -7)

m.c2331 = Constraint(expr= - 7*m.b43 + m.x743 - m.x902 >= -7)

m.c2332 = Constraint(expr= - 7*m.b44 + m.x744 - m.x903 >= -7)

m.c2333 = Constraint(expr= - 7*m.b31 + m.x746 - m.x890 >= -7)

m.c2334 = Constraint(expr= - 7*m.b32 + m.x747 - m.x891 >= -7)

m.c2335 = Constraint(expr= - 7*m.b33 + m.x748 - m.x892 >= -7)

m.c2336 = Constraint(expr= - 7*m.b34 + m.x749 - m.x893 >= -7)

m.c2337 = Constraint(expr= - 7*m.b36 + m.x751 - m.x895 >= -7)

m.c2338 = Constraint(expr= - 7*m.b37 + m.x752 - m.x896 >= -7)

m.c2339 = Constraint(expr= - 7*m.b38 + m.x753 - m.x897 >= -7)

m.c2340 = Constraint(expr= - 7*m.b39 + m.x754 - m.x898 >= -7)

m.c2341 = Constraint(expr= - 7*m.b41 + m.x756 - m.x900 >= -7)

m.c2342 = Constraint(expr= - 7*m.b42 + m.x757 - m.x901 >= -7)

m.c2343 = Constraint(expr= - 7*m.b43 + m.x758 - m.x902 >= -7)

m.c2344 = Constraint(expr= - 7*m.b44 + m.x759 - m.x903 >= -7)

m.c2345 = Constraint(expr= - 7*m.b31 + m.x761 - m.x890 >= -7)

m.c2346 = Constraint(expr= - 7*m.b32 + m.x762 - m.x891 >= -7)

m.c2347 = Constraint(expr= - 7*m.b33 + m.x763 - m.x892 >= -7)

m.c2348 = Constraint(expr= - 7*m.b34 + m.x764 - m.x893 >= -7)

m.c2349 = Constraint(expr= - 7*m.b36 + m.x766 - m.x895 >= -7)

m.c2350 = Constraint(expr= - 7*m.b37 + m.x767 - m.x896 >= -7)

m.c2351 = Constraint(expr= - 7*m.b38 + m.x768 - m.x897 >= -7)

m.c2352 = Constraint(expr= - 7*m.b39 + m.x769 - m.x898 >= -7)

m.c2353 = Constraint(expr= - 7*m.b41 + m.x771 - m.x900 >= -7)

m.c2354 = Constraint(expr= - 7*m.b42 + m.x772 - m.x901 >= -7)

m.c2355 = Constraint(expr= - 7*m.b43 + m.x773 - m.x902 >= -7)

m.c2356 = Constraint(expr= - 7*m.b44 + m.x774 - m.x903 >= -7)

m.c2357 = Constraint(expr= - 7*m.b31 + m.x776 - m.x890 >= -7)

m.c2358 = Constraint(expr= - 7*m.b32 + m.x777 - m.x891 >= -7)

m.c2359 = Constraint(expr= - 7*m.b33 + m.x778 - m.x892 >= -7)

m.c2360 = Constraint(expr= - 7*m.b34 + m.x779 - m.x893 >= -7)

m.c2361 = Constraint(expr= - 7*m.b36 + m.x781 - m.x895 >= -7)

m.c2362 = Constraint(expr= - 7*m.b37 + m.x782 - m.x896 >= -7)

m.c2363 = Constraint(expr= - 7*m.b38 + m.x783 - m.x897 >= -7)

m.c2364 = Constraint(expr= - 7*m.b39 + m.x784 - m.x898 >= -7)

m.c2365 = Constraint(expr= - 7*m.b41 + m.x786 - m.x900 >= -7)

m.c2366 = Constraint(expr= - 7*m.b42 + m.x787 - m.x901 >= -7)

m.c2367 = Constraint(expr= - 7*m.b43 + m.x788 - m.x902 >= -7)

m.c2368 = Constraint(expr= - 7*m.b44 + m.x789 - m.x903 >= -7)

m.c2369 = Constraint(expr= - 7*m.b31 + m.x821 - m.x890 >= -7)

m.c2370 = Constraint(expr= - 7*m.b32 + m.x822 - m.x891 >= -7)

m.c2371 = Constraint(expr= - 7*m.b33 + m.x823 - m.x892 >= -7)

m.c2372 = Constraint(expr= - 7*m.b34 + m.x824 - m.x893 >= -7)

m.c2373 = Constraint(expr= - 7*m.b36 + m.x826 - m.x895 >= -7)

m.c2374 = Constraint(expr= - 7*m.b37 + m.x827 - m.x896 >= -7)

m.c2375 = Constraint(expr= - 7*m.b38 + m.x828 - m.x897 >= -7)

m.c2376 = Constraint(expr= - 7*m.b39 + m.x829 - m.x898 >= -7)

m.c2377 = Constraint(expr= - 7*m.b41 + m.x831 - m.x900 >= -7)

m.c2378 = Constraint(expr= - 7*m.b42 + m.x832 - m.x901 >= -7)

m.c2379 = Constraint(expr= - 7*m.b43 + m.x833 - m.x902 >= -7)

m.c2380 = Constraint(expr= - 7*m.b44 + m.x834 - m.x903 >= -7)

m.c2381 = Constraint(expr= - 7*m.b31 + m.x836 - m.x890 >= -7)

m.c2382 = Constraint(expr= - 7*m.b32 + m.x837 - m.x891 >= -7)

m.c2383 = Constraint(expr= - 7*m.b33 + m.x838 - m.x892 >= -7)

m.c2384 = Constraint(expr= - 7*m.b34 + m.x839 - m.x893 >= -7)

m.c2385 = Constraint(expr= - 7*m.b36 + m.x841 - m.x895 >= -7)

m.c2386 = Constraint(expr= - 7*m.b37 + m.x842 - m.x896 >= -7)

m.c2387 = Constraint(expr= - 7*m.b38 + m.x843 - m.x897 >= -7)

m.c2388 = Constraint(expr= - 7*m.b39 + m.x844 - m.x898 >= -7)

m.c2389 = Constraint(expr= - 7*m.b41 + m.x846 - m.x900 >= -7)

m.c2390 = Constraint(expr= - 7*m.b42 + m.x847 - m.x901 >= -7)

m.c2391 = Constraint(expr= - 7*m.b43 + m.x848 - m.x902 >= -7)

m.c2392 = Constraint(expr= - 7*m.b44 + m.x849 - m.x903 >= -7)

m.c2393 = Constraint(expr= - 7*m.b46 + m.x656 - m.x905 >= -7)

m.c2394 = Constraint(expr= - 7*m.b47 + m.x657 - m.x906 >= -7)

m.c2395 = Constraint(expr= - 7*m.b48 + m.x658 - m.x907 >= -7)

m.c2396 = Constraint(expr= - 7*m.b49 + m.x659 - m.x908 >= -7)

m.c2397 = Constraint(expr= - 7*m.b51 + m.x661 - m.x910 >= -7)

m.c2398 = Constraint(expr= - 7*m.b52 + m.x662 - m.x911 >= -7)

m.c2399 = Constraint(expr= - 7*m.b53 + m.x663 - m.x912 >= -7)

m.c2400 = Constraint(expr= - 7*m.b54 + m.x664 - m.x913 >= -7)

m.c2401 = Constraint(expr= - 7*m.b56 + m.x666 - m.x915 >= -7)

m.c2402 = Constraint(expr= - 7*m.b57 + m.x667 - m.x916 >= -7)

m.c2403 = Constraint(expr= - 7*m.b58 + m.x668 - m.x917 >= -7)

m.c2404 = Constraint(expr= - 7*m.b59 + m.x669 - m.x918 >= -7)

m.c2405 = Constraint(expr= - 7*m.b46 + m.x671 - m.x905 >= -7)

m.c2406 = Constraint(expr= - 7*m.b47 + m.x672 - m.x906 >= -7)

m.c2407 = Constraint(expr= - 7*m.b48 + m.x673 - m.x907 >= -7)

m.c2408 = Constraint(expr= - 7*m.b49 + m.x674 - m.x908 >= -7)

m.c2409 = Constraint(expr= - 7*m.b51 + m.x676 - m.x910 >= -7)

m.c2410 = Constraint(expr= - 7*m.b52 + m.x677 - m.x911 >= -7)

m.c2411 = Constraint(expr= - 7*m.b53 + m.x678 - m.x912 >= -7)

m.c2412 = Constraint(expr= - 7*m.b54 + m.x679 - m.x913 >= -7)

m.c2413 = Constraint(expr= - 7*m.b56 + m.x681 - m.x915 >= -7)

m.c2414 = Constraint(expr= - 7*m.b57 + m.x682 - m.x916 >= -7)

m.c2415 = Constraint(expr= - 7*m.b58 + m.x683 - m.x917 >= -7)

m.c2416 = Constraint(expr= - 7*m.b59 + m.x684 - m.x918 >= -7)

m.c2417 = Constraint(expr= - 7*m.b46 + m.x686 - m.x905 >= -7)

m.c2418 = Constraint(expr= - 7*m.b47 + m.x687 - m.x906 >= -7)

m.c2419 = Constraint(expr= - 7*m.b48 + m.x688 - m.x907 >= -7)

m.c2420 = Constraint(expr= - 7*m.b49 + m.x689 - m.x908 >= -7)

m.c2421 = Constraint(expr= - 7*m.b51 + m.x691 - m.x910 >= -7)

m.c2422 = Constraint(expr= - 7*m.b52 + m.x692 - m.x911 >= -7)

m.c2423 = Constraint(expr= - 7*m.b53 + m.x693 - m.x912 >= -7)

m.c2424 = Constraint(expr= - 7*m.b54 + m.x694 - m.x913 >= -7)

m.c2425 = Constraint(expr= - 7*m.b56 + m.x696 - m.x915 >= -7)

m.c2426 = Constraint(expr= - 7*m.b57 + m.x697 - m.x916 >= -7)

m.c2427 = Constraint(expr= - 7*m.b58 + m.x698 - m.x917 >= -7)

m.c2428 = Constraint(expr= - 7*m.b59 + m.x699 - m.x918 >= -7)

m.c2429 = Constraint(expr= - 7*m.b46 + m.x716 - m.x905 >= -7)

m.c2430 = Constraint(expr= - 7*m.b47 + m.x717 - m.x906 >= -7)

m.c2431 = Constraint(expr= - 7*m.b48 + m.x718 - m.x907 >= -7)

m.c2432 = Constraint(expr= - 7*m.b49 + m.x719 - m.x908 >= -7)

m.c2433 = Constraint(expr= - 7*m.b51 + m.x721 - m.x910 >= -7)

m.c2434 = Constraint(expr= - 7*m.b52 + m.x722 - m.x911 >= -7)

m.c2435 = Constraint(expr= - 7*m.b53 + m.x723 - m.x912 >= -7)

m.c2436 = Constraint(expr= - 7*m.b54 + m.x724 - m.x913 >= -7)

m.c2437 = Constraint(expr= - 7*m.b56 + m.x726 - m.x915 >= -7)

m.c2438 = Constraint(expr= - 7*m.b57 + m.x727 - m.x916 >= -7)

m.c2439 = Constraint(expr= - 7*m.b58 + m.x728 - m.x917 >= -7)

m.c2440 = Constraint(expr= - 7*m.b59 + m.x729 - m.x918 >= -7)

m.c2441 = Constraint(expr= - 7*m.b46 + m.x731 - m.x905 >= -7)

m.c2442 = Constraint(expr= - 7*m.b47 + m.x732 - m.x906 >= -7)

m.c2443 = Constraint(expr= - 7*m.b48 + m.x733 - m.x907 >= -7)

m.c2444 = Constraint(expr= - 7*m.b49 + m.x734 - m.x908 >= -7)

m.c2445 = Constraint(expr= - 7*m.b51 + m.x736 - m.x910 >= -7)

m.c2446 = Constraint(expr= - 7*m.b52 + m.x737 - m.x911 >= -7)

m.c2447 = Constraint(expr= - 7*m.b53 + m.x738 - m.x912 >= -7)

m.c2448 = Constraint(expr= - 7*m.b54 + m.x739 - m.x913 >= -7)

m.c2449 = Constraint(expr= - 7*m.b56 + m.x741 - m.x915 >= -7)

m.c2450 = Constraint(expr= - 7*m.b57 + m.x742 - m.x916 >= -7)

m.c2451 = Constraint(expr= - 7*m.b58 + m.x743 - m.x917 >= -7)

m.c2452 = Constraint(expr= - 7*m.b59 + m.x744 - m.x918 >= -7)

m.c2453 = Constraint(expr= - 7*m.b46 + m.x746 - m.x905 >= -7)

m.c2454 = Constraint(expr= - 7*m.b47 + m.x747 - m.x906 >= -7)

m.c2455 = Constraint(expr= - 7*m.b48 + m.x748 - m.x907 >= -7)

m.c2456 = Constraint(expr= - 7*m.b49 + m.x749 - m.x908 >= -7)

m.c2457 = Constraint(expr= - 7*m.b51 + m.x751 - m.x910 >= -7)

m.c2458 = Constraint(expr= - 7*m.b52 + m.x752 - m.x911 >= -7)

m.c2459 = Constraint(expr= - 7*m.b53 + m.x753 - m.x912 >= -7)

m.c2460 = Constraint(expr= - 7*m.b54 + m.x754 - m.x913 >= -7)

m.c2461 = Constraint(expr= - 7*m.b56 + m.x756 - m.x915 >= -7)

m.c2462 = Constraint(expr= - 7*m.b57 + m.x757 - m.x916 >= -7)

m.c2463 = Constraint(expr= - 7*m.b58 + m.x758 - m.x917 >= -7)

m.c2464 = Constraint(expr= - 7*m.b59 + m.x759 - m.x918 >= -7)

m.c2465 = Constraint(expr= - 7*m.b46 + m.x761 - m.x905 >= -7)

m.c2466 = Constraint(expr= - 7*m.b47 + m.x762 - m.x906 >= -7)

m.c2467 = Constraint(expr= - 7*m.b48 + m.x763 - m.x907 >= -7)

m.c2468 = Constraint(expr= - 7*m.b49 + m.x764 - m.x908 >= -7)

m.c2469 = Constraint(expr= - 7*m.b51 + m.x766 - m.x910 >= -7)

m.c2470 = Constraint(expr= - 7*m.b52 + m.x767 - m.x911 >= -7)

m.c2471 = Constraint(expr= - 7*m.b53 + m.x768 - m.x912 >= -7)

m.c2472 = Constraint(expr= - 7*m.b54 + m.x769 - m.x913 >= -7)

m.c2473 = Constraint(expr= - 7*m.b56 + m.x771 - m.x915 >= -7)

m.c2474 = Constraint(expr= - 7*m.b57 + m.x772 - m.x916 >= -7)

m.c2475 = Constraint(expr= - 7*m.b58 + m.x773 - m.x917 >= -7)

m.c2476 = Constraint(expr= - 7*m.b59 + m.x774 - m.x918 >= -7)

m.c2477 = Constraint(expr= - 7*m.b46 + m.x776 - m.x905 >= -7)

m.c2478 = Constraint(expr= - 7*m.b47 + m.x777 - m.x906 >= -7)

m.c2479 = Constraint(expr= - 7*m.b48 + m.x778 - m.x907 >= -7)

m.c2480 = Constraint(expr= - 7*m.b49 + m.x779 - m.x908 >= -7)

m.c2481 = Constraint(expr= - 7*m.b51 + m.x781 - m.x910 >= -7)

m.c2482 = Constraint(expr= - 7*m.b52 + m.x782 - m.x911 >= -7)

m.c2483 = Constraint(expr= - 7*m.b53 + m.x783 - m.x912 >= -7)

m.c2484 = Constraint(expr= - 7*m.b54 + m.x784 - m.x913 >= -7)

m.c2485 = Constraint(expr= - 7*m.b56 + m.x786 - m.x915 >= -7)

m.c2486 = Constraint(expr= - 7*m.b57 + m.x787 - m.x916 >= -7)

m.c2487 = Constraint(expr= - 7*m.b58 + m.x788 - m.x917 >= -7)

m.c2488 = Constraint(expr= - 7*m.b59 + m.x789 - m.x918 >= -7)

m.c2489 = Constraint(expr= - 7*m.b46 + m.x821 - m.x905 >= -7)

m.c2490 = Constraint(expr= - 7*m.b47 + m.x822 - m.x906 >= -7)

m.c2491 = Constraint(expr= - 7*m.b48 + m.x823 - m.x907 >= -7)

m.c2492 = Constraint(expr= - 7*m.b49 + m.x824 - m.x908 >= -7)

m.c2493 = Constraint(expr= - 7*m.b51 + m.x826 - m.x910 >= -7)

m.c2494 = Constraint(expr= - 7*m.b52 + m.x827 - m.x911 >= -7)

m.c2495 = Constraint(expr= - 7*m.b53 + m.x828 - m.x912 >= -7)

m.c2496 = Constraint(expr= - 7*m.b54 + m.x829 - m.x913 >= -7)

m.c2497 = Constraint(expr= - 7*m.b56 + m.x831 - m.x915 >= -7)

m.c2498 = Constraint(expr= - 7*m.b57 + m.x832 - m.x916 >= -7)

m.c2499 = Constraint(expr= - 7*m.b58 + m.x833 - m.x917 >= -7)

m.c2500 = Constraint(expr= - 7*m.b59 + m.x834 - m.x918 >= -7)

m.c2501 = Constraint(expr= - 7*m.b46 + m.x836 - m.x905 >= -7)

m.c2502 = Constraint(expr= - 7*m.b47 + m.x837 - m.x906 >= -7)

m.c2503 = Constraint(expr= - 7*m.b48 + m.x838 - m.x907 >= -7)

m.c2504 = Constraint(expr= - 7*m.b49 + m.x839 - m.x908 >= -7)

m.c2505 = Constraint(expr= - 7*m.b51 + m.x841 - m.x910 >= -7)

m.c2506 = Constraint(expr= - 7*m.b52 + m.x842 - m.x911 >= -7)

m.c2507 = Constraint(expr= - 7*m.b53 + m.x843 - m.x912 >= -7)

m.c2508 = Constraint(expr= - 7*m.b54 + m.x844 - m.x913 >= -7)

m.c2509 = Constraint(expr= - 7*m.b56 + m.x846 - m.x915 >= -7)

m.c2510 = Constraint(expr= - 7*m.b57 + m.x847 - m.x916 >= -7)

m.c2511 = Constraint(expr= - 7*m.b58 + m.x848 - m.x917 >= -7)

m.c2512 = Constraint(expr= - 7*m.b59 + m.x849 - m.x918 >= -7)

m.c2513 = Constraint(expr= - 7*m.b61 + m.x656 - m.x920 >= -7)

m.c2514 = Constraint(expr= - 7*m.b62 + m.x657 - m.x921 >= -7)

m.c2515 = Constraint(expr= - 7*m.b63 + m.x658 - m.x922 >= -7)

m.c2516 = Constraint(expr= - 7*m.b64 + m.x659 - m.x923 >= -7)

m.c2517 = Constraint(expr= - 7*m.b66 + m.x661 - m.x925 >= -7)

m.c2518 = Constraint(expr= - 7*m.b67 + m.x662 - m.x926 >= -7)

m.c2519 = Constraint(expr= - 7*m.b68 + m.x663 - m.x927 >= -7)

m.c2520 = Constraint(expr= - 7*m.b69 + m.x664 - m.x928 >= -7)

m.c2521 = Constraint(expr= - 7*m.b71 + m.x666 - m.x930 >= -7)

m.c2522 = Constraint(expr= - 7*m.b72 + m.x667 - m.x931 >= -7)

m.c2523 = Constraint(expr= - 7*m.b73 + m.x668 - m.x932 >= -7)

m.c2524 = Constraint(expr= - 7*m.b74 + m.x669 - m.x933 >= -7)

m.c2525 = Constraint(expr= - 7*m.b61 + m.x671 - m.x920 >= -7)

m.c2526 = Constraint(expr= - 7*m.b62 + m.x672 - m.x921 >= -7)

m.c2527 = Constraint(expr= - 7*m.b63 + m.x673 - m.x922 >= -7)

m.c2528 = Constraint(expr= - 7*m.b64 + m.x674 - m.x923 >= -7)

m.c2529 = Constraint(expr= - 7*m.b66 + m.x676 - m.x925 >= -7)

m.c2530 = Constraint(expr= - 7*m.b67 + m.x677 - m.x926 >= -7)

m.c2531 = Constraint(expr= - 7*m.b68 + m.x678 - m.x927 >= -7)

m.c2532 = Constraint(expr= - 7*m.b69 + m.x679 - m.x928 >= -7)

m.c2533 = Constraint(expr= - 7*m.b71 + m.x681 - m.x930 >= -7)

m.c2534 = Constraint(expr= - 7*m.b72 + m.x682 - m.x931 >= -7)

m.c2535 = Constraint(expr= - 7*m.b73 + m.x683 - m.x932 >= -7)

m.c2536 = Constraint(expr= - 7*m.b74 + m.x684 - m.x933 >= -7)

m.c2537 = Constraint(expr= - 7*m.b61 + m.x686 - m.x920 >= -7)

m.c2538 = Constraint(expr= - 7*m.b62 + m.x687 - m.x921 >= -7)

m.c2539 = Constraint(expr= - 7*m.b63 + m.x688 - m.x922 >= -7)

m.c2540 = Constraint(expr= - 7*m.b64 + m.x689 - m.x923 >= -7)

m.c2541 = Constraint(expr= - 7*m.b66 + m.x691 - m.x925 >= -7)

m.c2542 = Constraint(expr= - 7*m.b67 + m.x692 - m.x926 >= -7)

m.c2543 = Constraint(expr= - 7*m.b68 + m.x693 - m.x927 >= -7)

m.c2544 = Constraint(expr= - 7*m.b69 + m.x694 - m.x928 >= -7)

m.c2545 = Constraint(expr= - 7*m.b71 + m.x696 - m.x930 >= -7)

m.c2546 = Constraint(expr= - 7*m.b72 + m.x697 - m.x931 >= -7)

m.c2547 = Constraint(expr= - 7*m.b73 + m.x698 - m.x932 >= -7)

m.c2548 = Constraint(expr= - 7*m.b74 + m.x699 - m.x933 >= -7)

m.c2549 = Constraint(expr= - 7*m.b61 + m.x701 - m.x920 >= -7)

m.c2550 = Constraint(expr= - 7*m.b62 + m.x702 - m.x921 >= -7)

m.c2551 = Constraint(expr= - 7*m.b63 + m.x703 - m.x922 >= -7)

m.c2552 = Constraint(expr= - 7*m.b64 + m.x704 - m.x923 >= -7)

m.c2553 = Constraint(expr= - 7*m.b66 + m.x706 - m.x925 >= -7)

m.c2554 = Constraint(expr= - 7*m.b67 + m.x707 - m.x926 >= -7)

m.c2555 = Constraint(expr= - 7*m.b68 + m.x708 - m.x927 >= -7)

m.c2556 = Constraint(expr= - 7*m.b69 + m.x709 - m.x928 >= -7)

m.c2557 = Constraint(expr= - 7*m.b71 + m.x711 - m.x930 >= -7)

m.c2558 = Constraint(expr= - 7*m.b72 + m.x712 - m.x931 >= -7)

m.c2559 = Constraint(expr= - 7*m.b73 + m.x713 - m.x932 >= -7)

m.c2560 = Constraint(expr= - 7*m.b74 + m.x714 - m.x933 >= -7)

m.c2561 = Constraint(expr= - 7*m.b61 + m.x731 - m.x920 >= -7)

m.c2562 = Constraint(expr= - 7*m.b62 + m.x732 - m.x921 >= -7)

m.c2563 = Constraint(expr= - 7*m.b63 + m.x733 - m.x922 >= -7)

m.c2564 = Constraint(expr= - 7*m.b64 + m.x734 - m.x923 >= -7)

m.c2565 = Constraint(expr= - 7*m.b66 + m.x736 - m.x925 >= -7)

m.c2566 = Constraint(expr= - 7*m.b67 + m.x737 - m.x926 >= -7)

m.c2567 = Constraint(expr= - 7*m.b68 + m.x738 - m.x927 >= -7)

m.c2568 = Constraint(expr= - 7*m.b69 + m.x739 - m.x928 >= -7)

m.c2569 = Constraint(expr= - 7*m.b71 + m.x741 - m.x930 >= -7)

m.c2570 = Constraint(expr= - 7*m.b72 + m.x742 - m.x931 >= -7)

m.c2571 = Constraint(expr= - 7*m.b73 + m.x743 - m.x932 >= -7)

m.c2572 = Constraint(expr= - 7*m.b74 + m.x744 - m.x933 >= -7)

m.c2573 = Constraint(expr= - 7*m.b61 + m.x746 - m.x920 >= -7)

m.c2574 = Constraint(expr= - 7*m.b62 + m.x747 - m.x921 >= -7)

m.c2575 = Constraint(expr= - 7*m.b63 + m.x748 - m.x922 >= -7)

m.c2576 = Constraint(expr= - 7*m.b64 + m.x749 - m.x923 >= -7)

m.c2577 = Constraint(expr= - 7*m.b66 + m.x751 - m.x925 >= -7)

m.c2578 = Constraint(expr= - 7*m.b67 + m.x752 - m.x926 >= -7)

m.c2579 = Constraint(expr= - 7*m.b68 + m.x753 - m.x927 >= -7)

m.c2580 = Constraint(expr= - 7*m.b69 + m.x754 - m.x928 >= -7)

m.c2581 = Constraint(expr= - 7*m.b71 + m.x756 - m.x930 >= -7)

m.c2582 = Constraint(expr= - 7*m.b72 + m.x757 - m.x931 >= -7)

m.c2583 = Constraint(expr= - 7*m.b73 + m.x758 - m.x932 >= -7)

m.c2584 = Constraint(expr= - 7*m.b74 + m.x759 - m.x933 >= -7)

m.c2585 = Constraint(expr= - 7*m.b61 + m.x761 - m.x920 >= -7)

m.c2586 = Constraint(expr= - 7*m.b62 + m.x762 - m.x921 >= -7)

m.c2587 = Constraint(expr= - 7*m.b63 + m.x763 - m.x922 >= -7)

m.c2588 = Constraint(expr= - 7*m.b64 + m.x764 - m.x923 >= -7)

m.c2589 = Constraint(expr= - 7*m.b66 + m.x766 - m.x925 >= -7)

m.c2590 = Constraint(expr= - 7*m.b67 + m.x767 - m.x926 >= -7)

m.c2591 = Constraint(expr= - 7*m.b68 + m.x768 - m.x927 >= -7)

m.c2592 = Constraint(expr= - 7*m.b69 + m.x769 - m.x928 >= -7)

m.c2593 = Constraint(expr= - 7*m.b71 + m.x771 - m.x930 >= -7)

m.c2594 = Constraint(expr= - 7*m.b72 + m.x772 - m.x931 >= -7)

m.c2595 = Constraint(expr= - 7*m.b73 + m.x773 - m.x932 >= -7)

m.c2596 = Constraint(expr= - 7*m.b74 + m.x774 - m.x933 >= -7)

m.c2597 = Constraint(expr= - 7*m.b61 + m.x776 - m.x920 >= -7)

m.c2598 = Constraint(expr= - 7*m.b62 + m.x777 - m.x921 >= -7)

m.c2599 = Constraint(expr= - 7*m.b63 + m.x778 - m.x922 >= -7)

m.c2600 = Constraint(expr= - 7*m.b64 + m.x779 - m.x923 >= -7)

m.c2601 = Constraint(expr= - 7*m.b66 + m.x781 - m.x925 >= -7)

m.c2602 = Constraint(expr= - 7*m.b67 + m.x782 - m.x926 >= -7)

m.c2603 = Constraint(expr= - 7*m.b68 + m.x783 - m.x927 >= -7)

m.c2604 = Constraint(expr= - 7*m.b69 + m.x784 - m.x928 >= -7)

m.c2605 = Constraint(expr= - 7*m.b71 + m.x786 - m.x930 >= -7)

m.c2606 = Constraint(expr= - 7*m.b72 + m.x787 - m.x931 >= -7)

m.c2607 = Constraint(expr= - 7*m.b73 + m.x788 - m.x932 >= -7)

m.c2608 = Constraint(expr= - 7*m.b74 + m.x789 - m.x933 >= -7)

m.c2609 = Constraint(expr= - 7*m.b61 + m.x821 - m.x920 >= -7)

m.c2610 = Constraint(expr= - 7*m.b62 + m.x822 - m.x921 >= -7)

m.c2611 = Constraint(expr= - 7*m.b63 + m.x823 - m.x922 >= -7)

m.c2612 = Constraint(expr= - 7*m.b64 + m.x824 - m.x923 >= -7)

m.c2613 = Constraint(expr= - 7*m.b66 + m.x826 - m.x925 >= -7)

m.c2614 = Constraint(expr= - 7*m.b67 + m.x827 - m.x926 >= -7)

m.c2615 = Constraint(expr= - 7*m.b68 + m.x828 - m.x927 >= -7)

m.c2616 = Constraint(expr= - 7*m.b69 + m.x829 - m.x928 >= -7)

m.c2617 = Constraint(expr= - 7*m.b71 + m.x831 - m.x930 >= -7)

m.c2618 = Constraint(expr= - 7*m.b72 + m.x832 - m.x931 >= -7)

m.c2619 = Constraint(expr= - 7*m.b73 + m.x833 - m.x932 >= -7)

m.c2620 = Constraint(expr= - 7*m.b74 + m.x834 - m.x933 >= -7)

m.c2621 = Constraint(expr= - 7*m.b61 + m.x836 - m.x920 >= -7)

m.c2622 = Constraint(expr= - 7*m.b62 + m.x837 - m.x921 >= -7)

m.c2623 = Constraint(expr= - 7*m.b63 + m.x838 - m.x922 >= -7)

m.c2624 = Constraint(expr= - 7*m.b64 + m.x839 - m.x923 >= -7)

m.c2625 = Constraint(expr= - 7*m.b66 + m.x841 - m.x925 >= -7)

m.c2626 = Constraint(expr= - 7*m.b67 + m.x842 - m.x926 >= -7)

m.c2627 = Constraint(expr= - 7*m.b68 + m.x843 - m.x927 >= -7)

m.c2628 = Constraint(expr= - 7*m.b69 + m.x844 - m.x928 >= -7)

m.c2629 = Constraint(expr= - 7*m.b71 + m.x846 - m.x930 >= -7)

m.c2630 = Constraint(expr= - 7*m.b72 + m.x847 - m.x931 >= -7)

m.c2631 = Constraint(expr= - 7*m.b73 + m.x848 - m.x932 >= -7)

m.c2632 = Constraint(expr= - 7*m.b74 + m.x849 - m.x933 >= -7)

m.c2633 = Constraint(expr= - 7*m.b76 + m.x656 - m.x935 >= -7)

m.c2634 = Constraint(expr= - 7*m.b77 + m.x657 - m.x936 >= -7)

m.c2635 = Constraint(expr= - 7*m.b78 + m.x658 - m.x937 >= -7)

m.c2636 = Constraint(expr= - 7*m.b79 + m.x659 - m.x938 >= -7)

m.c2637 = Constraint(expr= - 7*m.b81 + m.x661 - m.x940 >= -7)

m.c2638 = Constraint(expr= - 7*m.b82 + m.x662 - m.x941 >= -7)

m.c2639 = Constraint(expr= - 7*m.b83 + m.x663 - m.x942 >= -7)

m.c2640 = Constraint(expr= - 7*m.b84 + m.x664 - m.x943 >= -7)

m.c2641 = Constraint(expr= - 7*m.b86 + m.x666 - m.x945 >= -7)

m.c2642 = Constraint(expr= - 7*m.b87 + m.x667 - m.x946 >= -7)

m.c2643 = Constraint(expr= - 7*m.b88 + m.x668 - m.x947 >= -7)

m.c2644 = Constraint(expr= - 7*m.b89 + m.x669 - m.x948 >= -7)

m.c2645 = Constraint(expr= - 7*m.b76 + m.x671 - m.x935 >= -7)

m.c2646 = Constraint(expr= - 7*m.b77 + m.x672 - m.x936 >= -7)

m.c2647 = Constraint(expr= - 7*m.b78 + m.x673 - m.x937 >= -7)

m.c2648 = Constraint(expr= - 7*m.b79 + m.x674 - m.x938 >= -7)

m.c2649 = Constraint(expr= - 7*m.b81 + m.x676 - m.x940 >= -7)

m.c2650 = Constraint(expr= - 7*m.b82 + m.x677 - m.x941 >= -7)

m.c2651 = Constraint(expr= - 7*m.b83 + m.x678 - m.x942 >= -7)

m.c2652 = Constraint(expr= - 7*m.b84 + m.x679 - m.x943 >= -7)

m.c2653 = Constraint(expr= - 7*m.b86 + m.x681 - m.x945 >= -7)

m.c2654 = Constraint(expr= - 7*m.b87 + m.x682 - m.x946 >= -7)

m.c2655 = Constraint(expr= - 7*m.b88 + m.x683 - m.x947 >= -7)

m.c2656 = Constraint(expr= - 7*m.b89 + m.x684 - m.x948 >= -7)

m.c2657 = Constraint(expr= - 7*m.b76 + m.x686 - m.x935 >= -7)

m.c2658 = Constraint(expr= - 7*m.b77 + m.x687 - m.x936 >= -7)

m.c2659 = Constraint(expr= - 7*m.b78 + m.x688 - m.x937 >= -7)

m.c2660 = Constraint(expr= - 7*m.b79 + m.x689 - m.x938 >= -7)

m.c2661 = Constraint(expr= - 7*m.b81 + m.x691 - m.x940 >= -7)

m.c2662 = Constraint(expr= - 7*m.b82 + m.x692 - m.x941 >= -7)

m.c2663 = Constraint(expr= - 7*m.b83 + m.x693 - m.x942 >= -7)

m.c2664 = Constraint(expr= - 7*m.b84 + m.x694 - m.x943 >= -7)

m.c2665 = Constraint(expr= - 7*m.b86 + m.x696 - m.x945 >= -7)

m.c2666 = Constraint(expr= - 7*m.b87 + m.x697 - m.x946 >= -7)

m.c2667 = Constraint(expr= - 7*m.b88 + m.x698 - m.x947 >= -7)

m.c2668 = Constraint(expr= - 7*m.b89 + m.x699 - m.x948 >= -7)

m.c2669 = Constraint(expr= - 7*m.b76 + m.x701 - m.x935 >= -7)

m.c2670 = Constraint(expr= - 7*m.b77 + m.x702 - m.x936 >= -7)

m.c2671 = Constraint(expr= - 7*m.b78 + m.x703 - m.x937 >= -7)

m.c2672 = Constraint(expr= - 7*m.b79 + m.x704 - m.x938 >= -7)

m.c2673 = Constraint(expr= - 7*m.b81 + m.x706 - m.x940 >= -7)

m.c2674 = Constraint(expr= - 7*m.b82 + m.x707 - m.x941 >= -7)

m.c2675 = Constraint(expr= - 7*m.b83 + m.x708 - m.x942 >= -7)

m.c2676 = Constraint(expr= - 7*m.b84 + m.x709 - m.x943 >= -7)

m.c2677 = Constraint(expr= - 7*m.b86 + m.x711 - m.x945 >= -7)

m.c2678 = Constraint(expr= - 7*m.b87 + m.x712 - m.x946 >= -7)

m.c2679 = Constraint(expr= - 7*m.b88 + m.x713 - m.x947 >= -7)

m.c2680 = Constraint(expr= - 7*m.b89 + m.x714 - m.x948 >= -7)

m.c2681 = Constraint(expr= - 7*m.b76 + m.x716 - m.x935 >= -7)

m.c2682 = Constraint(expr= - 7*m.b77 + m.x717 - m.x936 >= -7)

m.c2683 = Constraint(expr= - 7*m.b78 + m.x718 - m.x937 >= -7)

m.c2684 = Constraint(expr= - 7*m.b79 + m.x719 - m.x938 >= -7)

m.c2685 = Constraint(expr= - 7*m.b81 + m.x721 - m.x940 >= -7)

m.c2686 = Constraint(expr= - 7*m.b82 + m.x722 - m.x941 >= -7)

m.c2687 = Constraint(expr= - 7*m.b83 + m.x723 - m.x942 >= -7)

m.c2688 = Constraint(expr= - 7*m.b84 + m.x724 - m.x943 >= -7)

m.c2689 = Constraint(expr= - 7*m.b86 + m.x726 - m.x945 >= -7)

m.c2690 = Constraint(expr= - 7*m.b87 + m.x727 - m.x946 >= -7)

m.c2691 = Constraint(expr= - 7*m.b88 + m.x728 - m.x947 >= -7)

m.c2692 = Constraint(expr= - 7*m.b89 + m.x729 - m.x948 >= -7)

m.c2693 = Constraint(expr= - 7*m.b76 + m.x746 - m.x935 >= -7)

m.c2694 = Constraint(expr= - 7*m.b77 + m.x747 - m.x936 >= -7)

m.c2695 = Constraint(expr= - 7*m.b78 + m.x748 - m.x937 >= -7)

m.c2696 = Constraint(expr= - 7*m.b79 + m.x749 - m.x938 >= -7)

m.c2697 = Constraint(expr= - 7*m.b81 + m.x751 - m.x940 >= -7)

m.c2698 = Constraint(expr= - 7*m.b82 + m.x752 - m.x941 >= -7)

m.c2699 = Constraint(expr= - 7*m.b83 + m.x753 - m.x942 >= -7)

m.c2700 = Constraint(expr= - 7*m.b84 + m.x754 - m.x943 >= -7)

m.c2701 = Constraint(expr= - 7*m.b86 + m.x756 - m.x945 >= -7)

m.c2702 = Constraint(expr= - 7*m.b87 + m.x757 - m.x946 >= -7)

m.c2703 = Constraint(expr= - 7*m.b88 + m.x758 - m.x947 >= -7)

m.c2704 = Constraint(expr= - 7*m.b89 + m.x759 - m.x948 >= -7)

m.c2705 = Constraint(expr= - 7*m.b76 + m.x761 - m.x935 >= -7)

m.c2706 = Constraint(expr= - 7*m.b77 + m.x762 - m.x936 >= -7)

m.c2707 = Constraint(expr= - 7*m.b78 + m.x763 - m.x937 >= -7)

m.c2708 = Constraint(expr= - 7*m.b79 + m.x764 - m.x938 >= -7)

m.c2709 = Constraint(expr= - 7*m.b81 + m.x766 - m.x940 >= -7)

m.c2710 = Constraint(expr= - 7*m.b82 + m.x767 - m.x941 >= -7)

m.c2711 = Constraint(expr= - 7*m.b83 + m.x768 - m.x942 >= -7)

m.c2712 = Constraint(expr= - 7*m.b84 + m.x769 - m.x943 >= -7)

m.c2713 = Constraint(expr= - 7*m.b86 + m.x771 - m.x945 >= -7)

m.c2714 = Constraint(expr= - 7*m.b87 + m.x772 - m.x946 >= -7)

m.c2715 = Constraint(expr= - 7*m.b88 + m.x773 - m.x947 >= -7)

m.c2716 = Constraint(expr= - 7*m.b89 + m.x774 - m.x948 >= -7)

m.c2717 = Constraint(expr= - 7*m.b76 + m.x776 - m.x935 >= -7)

m.c2718 = Constraint(expr= - 7*m.b77 + m.x777 - m.x936 >= -7)

m.c2719 = Constraint(expr= - 7*m.b78 + m.x778 - m.x937 >= -7)

m.c2720 = Constraint(expr= - 7*m.b79 + m.x779 - m.x938 >= -7)

m.c2721 = Constraint(expr= - 7*m.b81 + m.x781 - m.x940 >= -7)

m.c2722 = Constraint(expr= - 7*m.b82 + m.x782 - m.x941 >= -7)

m.c2723 = Constraint(expr= - 7*m.b83 + m.x783 - m.x942 >= -7)

m.c2724 = Constraint(expr= - 7*m.b84 + m.x784 - m.x943 >= -7)

m.c2725 = Constraint(expr= - 7*m.b86 + m.x786 - m.x945 >= -7)

m.c2726 = Constraint(expr= - 7*m.b87 + m.x787 - m.x946 >= -7)

m.c2727 = Constraint(expr= - 7*m.b88 + m.x788 - m.x947 >= -7)

m.c2728 = Constraint(expr= - 7*m.b89 + m.x789 - m.x948 >= -7)

m.c2729 = Constraint(expr= - 7*m.b76 + m.x821 - m.x935 >= -7)

m.c2730 = Constraint(expr= - 7*m.b77 + m.x822 - m.x936 >= -7)

m.c2731 = Constraint(expr= - 7*m.b78 + m.x823 - m.x937 >= -7)

m.c2732 = Constraint(expr= - 7*m.b79 + m.x824 - m.x938 >= -7)

m.c2733 = Constraint(expr= - 7*m.b81 + m.x826 - m.x940 >= -7)

m.c2734 = Constraint(expr= - 7*m.b82 + m.x827 - m.x941 >= -7)

m.c2735 = Constraint(expr= - 7*m.b83 + m.x828 - m.x942 >= -7)

m.c2736 = Constraint(expr= - 7*m.b84 + m.x829 - m.x943 >= -7)

m.c2737 = Constraint(expr= - 7*m.b86 + m.x831 - m.x945 >= -7)

m.c2738 = Constraint(expr= - 7*m.b87 + m.x832 - m.x946 >= -7)

m.c2739 = Constraint(expr= - 7*m.b88 + m.x833 - m.x947 >= -7)

m.c2740 = Constraint(expr= - 7*m.b89 + m.x834 - m.x948 >= -7)

m.c2741 = Constraint(expr= - 7*m.b76 + m.x836 - m.x935 >= -7)

m.c2742 = Constraint(expr= - 7*m.b77 + m.x837 - m.x936 >= -7)

m.c2743 = Constraint(expr= - 7*m.b78 + m.x838 - m.x937 >= -7)

m.c2744 = Constraint(expr= - 7*m.b79 + m.x839 - m.x938 >= -7)

m.c2745 = Constraint(expr= - 7*m.b81 + m.x841 - m.x940 >= -7)

m.c2746 = Constraint(expr= - 7*m.b82 + m.x842 - m.x941 >= -7)

m.c2747 = Constraint(expr= - 7*m.b83 + m.x843 - m.x942 >= -7)

m.c2748 = Constraint(expr= - 7*m.b84 + m.x844 - m.x943 >= -7)

m.c2749 = Constraint(expr= - 7*m.b86 + m.x846 - m.x945 >= -7)

m.c2750 = Constraint(expr= - 7*m.b87 + m.x847 - m.x946 >= -7)

m.c2751 = Constraint(expr= - 7*m.b88 + m.x848 - m.x947 >= -7)

m.c2752 = Constraint(expr= - 7*m.b89 + m.x849 - m.x948 >= -7)

m.c2753 = Constraint(expr= - 7*m.b91 + m.x656 - m.x950 >= -7)

m.c2754 = Constraint(expr= - 7*m.b92 + m.x657 - m.x951 >= -7)

m.c2755 = Constraint(expr= - 7*m.b93 + m.x658 - m.x952 >= -7)

m.c2756 = Constraint(expr= - 7*m.b94 + m.x659 - m.x953 >= -7)

m.c2757 = Constraint(expr= - 7*m.b96 + m.x661 - m.x955 >= -7)

m.c2758 = Constraint(expr= - 7*m.b97 + m.x662 - m.x956 >= -7)

m.c2759 = Constraint(expr= - 7*m.b98 + m.x663 - m.x957 >= -7)

m.c2760 = Constraint(expr= - 7*m.b99 + m.x664 - m.x958 >= -7)

m.c2761 = Constraint(expr= - 7*m.b101 + m.x666 - m.x960 >= -7)

m.c2762 = Constraint(expr= - 7*m.b102 + m.x667 - m.x961 >= -7)

m.c2763 = Constraint(expr= - 7*m.b103 + m.x668 - m.x962 >= -7)

m.c2764 = Constraint(expr= - 7*m.b104 + m.x669 - m.x963 >= -7)

m.c2765 = Constraint(expr= - 7*m.b91 + m.x671 - m.x950 >= -7)

m.c2766 = Constraint(expr= - 7*m.b92 + m.x672 - m.x951 >= -7)

m.c2767 = Constraint(expr= - 7*m.b93 + m.x673 - m.x952 >= -7)

m.c2768 = Constraint(expr= - 7*m.b94 + m.x674 - m.x953 >= -7)

m.c2769 = Constraint(expr= - 7*m.b96 + m.x676 - m.x955 >= -7)

m.c2770 = Constraint(expr= - 7*m.b97 + m.x677 - m.x956 >= -7)

m.c2771 = Constraint(expr= - 7*m.b98 + m.x678 - m.x957 >= -7)

m.c2772 = Constraint(expr= - 7*m.b99 + m.x679 - m.x958 >= -7)

m.c2773 = Constraint(expr= - 7*m.b101 + m.x681 - m.x960 >= -7)

m.c2774 = Constraint(expr= - 7*m.b102 + m.x682 - m.x961 >= -7)

m.c2775 = Constraint(expr= - 7*m.b103 + m.x683 - m.x962 >= -7)

m.c2776 = Constraint(expr= - 7*m.b104 + m.x684 - m.x963 >= -7)

m.c2777 = Constraint(expr= - 7*m.b91 + m.x686 - m.x950 >= -7)

m.c2778 = Constraint(expr= - 7*m.b92 + m.x687 - m.x951 >= -7)

m.c2779 = Constraint(expr= - 7*m.b93 + m.x688 - m.x952 >= -7)

m.c2780 = Constraint(expr= - 7*m.b94 + m.x689 - m.x953 >= -7)

m.c2781 = Constraint(expr= - 7*m.b96 + m.x691 - m.x955 >= -7)

m.c2782 = Constraint(expr= - 7*m.b97 + m.x692 - m.x956 >= -7)

m.c2783 = Constraint(expr= - 7*m.b98 + m.x693 - m.x957 >= -7)

m.c2784 = Constraint(expr= - 7*m.b99 + m.x694 - m.x958 >= -7)

m.c2785 = Constraint(expr= - 7*m.b101 + m.x696 - m.x960 >= -7)

m.c2786 = Constraint(expr= - 7*m.b102 + m.x697 - m.x961 >= -7)

m.c2787 = Constraint(expr= - 7*m.b103 + m.x698 - m.x962 >= -7)

m.c2788 = Constraint(expr= - 7*m.b104 + m.x699 - m.x963 >= -7)

m.c2789 = Constraint(expr= - 7*m.b91 + m.x701 - m.x950 >= -7)

m.c2790 = Constraint(expr= - 7*m.b92 + m.x702 - m.x951 >= -7)

m.c2791 = Constraint(expr= - 7*m.b93 + m.x703 - m.x952 >= -7)

m.c2792 = Constraint(expr= - 7*m.b94 + m.x704 - m.x953 >= -7)

m.c2793 = Constraint(expr= - 7*m.b96 + m.x706 - m.x955 >= -7)

m.c2794 = Constraint(expr= - 7*m.b97 + m.x707 - m.x956 >= -7)

m.c2795 = Constraint(expr= - 7*m.b98 + m.x708 - m.x957 >= -7)

m.c2796 = Constraint(expr= - 7*m.b99 + m.x709 - m.x958 >= -7)

m.c2797 = Constraint(expr= - 7*m.b101 + m.x711 - m.x960 >= -7)

m.c2798 = Constraint(expr= - 7*m.b102 + m.x712 - m.x961 >= -7)

m.c2799 = Constraint(expr= - 7*m.b103 + m.x713 - m.x962 >= -7)

m.c2800 = Constraint(expr= - 7*m.b104 + m.x714 - m.x963 >= -7)

m.c2801 = Constraint(expr= - 7*m.b91 + m.x716 - m.x950 >= -7)

m.c2802 = Constraint(expr= - 7*m.b92 + m.x717 - m.x951 >= -7)

m.c2803 = Constraint(expr= - 7*m.b93 + m.x718 - m.x952 >= -7)

m.c2804 = Constraint(expr= - 7*m.b94 + m.x719 - m.x953 >= -7)

m.c2805 = Constraint(expr= - 7*m.b96 + m.x721 - m.x955 >= -7)

m.c2806 = Constraint(expr= - 7*m.b97 + m.x722 - m.x956 >= -7)

m.c2807 = Constraint(expr= - 7*m.b98 + m.x723 - m.x957 >= -7)

m.c2808 = Constraint(expr= - 7*m.b99 + m.x724 - m.x958 >= -7)

m.c2809 = Constraint(expr= - 7*m.b101 + m.x726 - m.x960 >= -7)

m.c2810 = Constraint(expr= - 7*m.b102 + m.x727 - m.x961 >= -7)

m.c2811 = Constraint(expr= - 7*m.b103 + m.x728 - m.x962 >= -7)

m.c2812 = Constraint(expr= - 7*m.b104 + m.x729 - m.x963 >= -7)

m.c2813 = Constraint(expr= - 7*m.b91 + m.x731 - m.x950 >= -7)

m.c2814 = Constraint(expr= - 7*m.b92 + m.x732 - m.x951 >= -7)

m.c2815 = Constraint(expr= - 7*m.b93 + m.x733 - m.x952 >= -7)

m.c2816 = Constraint(expr= - 7*m.b94 + m.x734 - m.x953 >= -7)

m.c2817 = Constraint(expr= - 7*m.b96 + m.x736 - m.x955 >= -7)

m.c2818 = Constraint(expr= - 7*m.b97 + m.x737 - m.x956 >= -7)

m.c2819 = Constraint(expr= - 7*m.b98 + m.x738 - m.x957 >= -7)

m.c2820 = Constraint(expr= - 7*m.b99 + m.x739 - m.x958 >= -7)

m.c2821 = Constraint(expr= - 7*m.b101 + m.x741 - m.x960 >= -7)

m.c2822 = Constraint(expr= - 7*m.b102 + m.x742 - m.x961 >= -7)

m.c2823 = Constraint(expr= - 7*m.b103 + m.x743 - m.x962 >= -7)

m.c2824 = Constraint(expr= - 7*m.b104 + m.x744 - m.x963 >= -7)

m.c2825 = Constraint(expr= - 7*m.b91 + m.x761 - m.x950 >= -7)

m.c2826 = Constraint(expr= - 7*m.b92 + m.x762 - m.x951 >= -7)

m.c2827 = Constraint(expr= - 7*m.b93 + m.x763 - m.x952 >= -7)

m.c2828 = Constraint(expr= - 7*m.b94 + m.x764 - m.x953 >= -7)

m.c2829 = Constraint(expr= - 7*m.b96 + m.x766 - m.x955 >= -7)

m.c2830 = Constraint(expr= - 7*m.b97 + m.x767 - m.x956 >= -7)

m.c2831 = Constraint(expr= - 7*m.b98 + m.x768 - m.x957 >= -7)

m.c2832 = Constraint(expr= - 7*m.b99 + m.x769 - m.x958 >= -7)

m.c2833 = Constraint(expr= - 7*m.b101 + m.x771 - m.x960 >= -7)

m.c2834 = Constraint(expr= - 7*m.b102 + m.x772 - m.x961 >= -7)

m.c2835 = Constraint(expr= - 7*m.b103 + m.x773 - m.x962 >= -7)

m.c2836 = Constraint(expr= - 7*m.b104 + m.x774 - m.x963 >= -7)

m.c2837 = Constraint(expr= - 7*m.b91 + m.x776 - m.x950 >= -7)

m.c2838 = Constraint(expr= - 7*m.b92 + m.x777 - m.x951 >= -7)

m.c2839 = Constraint(expr= - 7*m.b93 + m.x778 - m.x952 >= -7)

m.c2840 = Constraint(expr= - 7*m.b94 + m.x779 - m.x953 >= -7)

m.c2841 = Constraint(expr= - 7*m.b96 + m.x781 - m.x955 >= -7)

m.c2842 = Constraint(expr= - 7*m.b97 + m.x782 - m.x956 >= -7)

m.c2843 = Constraint(expr= - 7*m.b98 + m.x783 - m.x957 >= -7)

m.c2844 = Constraint(expr= - 7*m.b99 + m.x784 - m.x958 >= -7)

m.c2845 = Constraint(expr= - 7*m.b101 + m.x786 - m.x960 >= -7)

m.c2846 = Constraint(expr= - 7*m.b102 + m.x787 - m.x961 >= -7)

m.c2847 = Constraint(expr= - 7*m.b103 + m.x788 - m.x962 >= -7)

m.c2848 = Constraint(expr= - 7*m.b104 + m.x789 - m.x963 >= -7)

m.c2849 = Constraint(expr= - 7*m.b91 + m.x821 - m.x950 >= -7)

m.c2850 = Constraint(expr= - 7*m.b92 + m.x822 - m.x951 >= -7)

m.c2851 = Constraint(expr= - 7*m.b93 + m.x823 - m.x952 >= -7)

m.c2852 = Constraint(expr= - 7*m.b94 + m.x824 - m.x953 >= -7)

m.c2853 = Constraint(expr= - 7*m.b96 + m.x826 - m.x955 >= -7)

m.c2854 = Constraint(expr= - 7*m.b97 + m.x827 - m.x956 >= -7)

m.c2855 = Constraint(expr= - 7*m.b98 + m.x828 - m.x957 >= -7)

m.c2856 = Constraint(expr= - 7*m.b99 + m.x829 - m.x958 >= -7)

m.c2857 = Constraint(expr= - 7*m.b101 + m.x831 - m.x960 >= -7)

m.c2858 = Constraint(expr= - 7*m.b102 + m.x832 - m.x961 >= -7)

m.c2859 = Constraint(expr= - 7*m.b103 + m.x833 - m.x962 >= -7)

m.c2860 = Constraint(expr= - 7*m.b104 + m.x834 - m.x963 >= -7)

m.c2861 = Constraint(expr= - 7*m.b91 + m.x836 - m.x950 >= -7)

m.c2862 = Constraint(expr= - 7*m.b92 + m.x837 - m.x951 >= -7)

m.c2863 = Constraint(expr= - 7*m.b93 + m.x838 - m.x952 >= -7)

m.c2864 = Constraint(expr= - 7*m.b94 + m.x839 - m.x953 >= -7)

m.c2865 = Constraint(expr= - 7*m.b96 + m.x841 - m.x955 >= -7)

m.c2866 = Constraint(expr= - 7*m.b97 + m.x842 - m.x956 >= -7)

m.c2867 = Constraint(expr= - 7*m.b98 + m.x843 - m.x957 >= -7)

m.c2868 = Constraint(expr= - 7*m.b99 + m.x844 - m.x958 >= -7)

m.c2869 = Constraint(expr= - 7*m.b101 + m.x846 - m.x960 >= -7)

m.c2870 = Constraint(expr= - 7*m.b102 + m.x847 - m.x961 >= -7)

m.c2871 = Constraint(expr= - 7*m.b103 + m.x848 - m.x962 >= -7)

m.c2872 = Constraint(expr= - 7*m.b104 + m.x849 - m.x963 >= -7)

m.c2873 = Constraint(expr= - 7*m.b106 + m.x656 - m.x965 >= -7)

m.c2874 = Constraint(expr= - 7*m.b107 + m.x657 - m.x966 >= -7)

m.c2875 = Constraint(expr= - 7*m.b108 + m.x658 - m.x967 >= -7)

m.c2876 = Constraint(expr= - 7*m.b109 + m.x659 - m.x968 >= -7)

m.c2877 = Constraint(expr= - 7*m.b111 + m.x661 - m.x970 >= -7)

m.c2878 = Constraint(expr= - 7*m.b112 + m.x662 - m.x971 >= -7)

m.c2879 = Constraint(expr= - 7*m.b113 + m.x663 - m.x972 >= -7)

m.c2880 = Constraint(expr= - 7*m.b114 + m.x664 - m.x973 >= -7)

m.c2881 = Constraint(expr= - 7*m.b116 + m.x666 - m.x975 >= -7)

m.c2882 = Constraint(expr= - 7*m.b117 + m.x667 - m.x976 >= -7)

m.c2883 = Constraint(expr= - 7*m.b118 + m.x668 - m.x977 >= -7)

m.c2884 = Constraint(expr= - 7*m.b119 + m.x669 - m.x978 >= -7)

m.c2885 = Constraint(expr= - 7*m.b106 + m.x671 - m.x965 >= -7)

m.c2886 = Constraint(expr= - 7*m.b107 + m.x672 - m.x966 >= -7)

m.c2887 = Constraint(expr= - 7*m.b108 + m.x673 - m.x967 >= -7)

m.c2888 = Constraint(expr= - 7*m.b109 + m.x674 - m.x968 >= -7)

m.c2889 = Constraint(expr= - 7*m.b111 + m.x676 - m.x970 >= -7)

m.c2890 = Constraint(expr= - 7*m.b112 + m.x677 - m.x971 >= -7)

m.c2891 = Constraint(expr= - 7*m.b113 + m.x678 - m.x972 >= -7)

m.c2892 = Constraint(expr= - 7*m.b114 + m.x679 - m.x973 >= -7)

m.c2893 = Constraint(expr= - 7*m.b116 + m.x681 - m.x975 >= -7)

m.c2894 = Constraint(expr= - 7*m.b117 + m.x682 - m.x976 >= -7)

m.c2895 = Constraint(expr= - 7*m.b118 + m.x683 - m.x977 >= -7)

m.c2896 = Constraint(expr= - 7*m.b119 + m.x684 - m.x978 >= -7)

m.c2897 = Constraint(expr= - 7*m.b106 + m.x686 - m.x965 >= -7)

m.c2898 = Constraint(expr= - 7*m.b107 + m.x687 - m.x966 >= -7)

m.c2899 = Constraint(expr= - 7*m.b108 + m.x688 - m.x967 >= -7)

m.c2900 = Constraint(expr= - 7*m.b109 + m.x689 - m.x968 >= -7)

m.c2901 = Constraint(expr= - 7*m.b111 + m.x691 - m.x970 >= -7)

m.c2902 = Constraint(expr= - 7*m.b112 + m.x692 - m.x971 >= -7)

m.c2903 = Constraint(expr= - 7*m.b113 + m.x693 - m.x972 >= -7)

m.c2904 = Constraint(expr= - 7*m.b114 + m.x694 - m.x973 >= -7)

m.c2905 = Constraint(expr= - 7*m.b116 + m.x696 - m.x975 >= -7)

m.c2906 = Constraint(expr= - 7*m.b117 + m.x697 - m.x976 >= -7)

m.c2907 = Constraint(expr= - 7*m.b118 + m.x698 - m.x977 >= -7)

m.c2908 = Constraint(expr= - 7*m.b119 + m.x699 - m.x978 >= -7)

m.c2909 = Constraint(expr= - 7*m.b106 + m.x701 - m.x965 >= -7)

m.c2910 = Constraint(expr= - 7*m.b107 + m.x702 - m.x966 >= -7)

m.c2911 = Constraint(expr= - 7*m.b108 + m.x703 - m.x967 >= -7)

m.c2912 = Constraint(expr= - 7*m.b109 + m.x704 - m.x968 >= -7)

m.c2913 = Constraint(expr= - 7*m.b111 + m.x706 - m.x970 >= -7)

m.c2914 = Constraint(expr= - 7*m.b112 + m.x707 - m.x971 >= -7)

m.c2915 = Constraint(expr= - 7*m.b113 + m.x708 - m.x972 >= -7)

m.c2916 = Constraint(expr= - 7*m.b114 + m.x709 - m.x973 >= -7)

m.c2917 = Constraint(expr= - 7*m.b116 + m.x711 - m.x975 >= -7)

m.c2918 = Constraint(expr= - 7*m.b117 + m.x712 - m.x976 >= -7)

m.c2919 = Constraint(expr= - 7*m.b118 + m.x713 - m.x977 >= -7)

m.c2920 = Constraint(expr= - 7*m.b119 + m.x714 - m.x978 >= -7)

m.c2921 = Constraint(expr= - 7*m.b106 + m.x716 - m.x965 >= -7)

m.c2922 = Constraint(expr= - 7*m.b107 + m.x717 - m.x966 >= -7)

m.c2923 = Constraint(expr= - 7*m.b108 + m.x718 - m.x967 >= -7)

m.c2924 = Constraint(expr= - 7*m.b109 + m.x719 - m.x968 >= -7)

m.c2925 = Constraint(expr= - 7*m.b111 + m.x721 - m.x970 >= -7)

m.c2926 = Constraint(expr= - 7*m.b112 + m.x722 - m.x971 >= -7)

m.c2927 = Constraint(expr= - 7*m.b113 + m.x723 - m.x972 >= -7)

m.c2928 = Constraint(expr= - 7*m.b114 + m.x724 - m.x973 >= -7)

m.c2929 = Constraint(expr= - 7*m.b116 + m.x726 - m.x975 >= -7)

m.c2930 = Constraint(expr= - 7*m.b117 + m.x727 - m.x976 >= -7)

m.c2931 = Constraint(expr= - 7*m.b118 + m.x728 - m.x977 >= -7)

m.c2932 = Constraint(expr= - 7*m.b119 + m.x729 - m.x978 >= -7)

m.c2933 = Constraint(expr= - 7*m.b106 + m.x731 - m.x965 >= -7)

m.c2934 = Constraint(expr= - 7*m.b107 + m.x732 - m.x966 >= -7)

m.c2935 = Constraint(expr= - 7*m.b108 + m.x733 - m.x967 >= -7)

m.c2936 = Constraint(expr= - 7*m.b109 + m.x734 - m.x968 >= -7)

m.c2937 = Constraint(expr= - 7*m.b111 + m.x736 - m.x970 >= -7)

m.c2938 = Constraint(expr= - 7*m.b112 + m.x737 - m.x971 >= -7)

m.c2939 = Constraint(expr= - 7*m.b113 + m.x738 - m.x972 >= -7)

m.c2940 = Constraint(expr= - 7*m.b114 + m.x739 - m.x973 >= -7)

m.c2941 = Constraint(expr= - 7*m.b116 + m.x741 - m.x975 >= -7)

m.c2942 = Constraint(expr= - 7*m.b117 + m.x742 - m.x976 >= -7)

m.c2943 = Constraint(expr= - 7*m.b118 + m.x743 - m.x977 >= -7)

m.c2944 = Constraint(expr= - 7*m.b119 + m.x744 - m.x978 >= -7)

m.c2945 = Constraint(expr= - 7*m.b106 + m.x746 - m.x965 >= -7)

m.c2946 = Constraint(expr= - 7*m.b107 + m.x747 - m.x966 >= -7)

m.c2947 = Constraint(expr= - 7*m.b108 + m.x748 - m.x967 >= -7)

m.c2948 = Constraint(expr= - 7*m.b109 + m.x749 - m.x968 >= -7)

m.c2949 = Constraint(expr= - 7*m.b111 + m.x751 - m.x970 >= -7)

m.c2950 = Constraint(expr= - 7*m.b112 + m.x752 - m.x971 >= -7)

m.c2951 = Constraint(expr= - 7*m.b113 + m.x753 - m.x972 >= -7)

m.c2952 = Constraint(expr= - 7*m.b114 + m.x754 - m.x973 >= -7)

m.c2953 = Constraint(expr= - 7*m.b116 + m.x756 - m.x975 >= -7)

m.c2954 = Constraint(expr= - 7*m.b117 + m.x757 - m.x976 >= -7)

m.c2955 = Constraint(expr= - 7*m.b118 + m.x758 - m.x977 >= -7)

m.c2956 = Constraint(expr= - 7*m.b119 + m.x759 - m.x978 >= -7)

m.c2957 = Constraint(expr= - 7*m.b106 + m.x776 - m.x965 >= -7)

m.c2958 = Constraint(expr= - 7*m.b107 + m.x777 - m.x966 >= -7)

m.c2959 = Constraint(expr= - 7*m.b108 + m.x778 - m.x967 >= -7)

m.c2960 = Constraint(expr= - 7*m.b109 + m.x779 - m.x968 >= -7)

m.c2961 = Constraint(expr= - 7*m.b111 + m.x781 - m.x970 >= -7)

m.c2962 = Constraint(expr= - 7*m.b112 + m.x782 - m.x971 >= -7)

m.c2963 = Constraint(expr= - 7*m.b113 + m.x783 - m.x972 >= -7)

m.c2964 = Constraint(expr= - 7*m.b114 + m.x784 - m.x973 >= -7)

m.c2965 = Constraint(expr= - 7*m.b116 + m.x786 - m.x975 >= -7)

m.c2966 = Constraint(expr= - 7*m.b117 + m.x787 - m.x976 >= -7)

m.c2967 = Constraint(expr= - 7*m.b118 + m.x788 - m.x977 >= -7)

m.c2968 = Constraint(expr= - 7*m.b119 + m.x789 - m.x978 >= -7)

m.c2969 = Constraint(expr= - 7*m.b106 + m.x821 - m.x965 >= -7)

m.c2970 = Constraint(expr= - 7*m.b107 + m.x822 - m.x966 >= -7)

m.c2971 = Constraint(expr= - 7*m.b108 + m.x823 - m.x967 >= -7)

m.c2972 = Constraint(expr= - 7*m.b109 + m.x824 - m.x968 >= -7)

m.c2973 = Constraint(expr= - 7*m.b111 + m.x826 - m.x970 >= -7)

m.c2974 = Constraint(expr= - 7*m.b112 + m.x827 - m.x971 >= -7)

m.c2975 = Constraint(expr= - 7*m.b113 + m.x828 - m.x972 >= -7)

m.c2976 = Constraint(expr= - 7*m.b114 + m.x829 - m.x973 >= -7)

m.c2977 = Constraint(expr= - 7*m.b116 + m.x831 - m.x975 >= -7)

m.c2978 = Constraint(expr= - 7*m.b117 + m.x832 - m.x976 >= -7)

m.c2979 = Constraint(expr= - 7*m.b118 + m.x833 - m.x977 >= -7)

m.c2980 = Constraint(expr= - 7*m.b119 + m.x834 - m.x978 >= -7)

m.c2981 = Constraint(expr= - 7*m.b106 + m.x836 - m.x965 >= -7)

m.c2982 = Constraint(expr= - 7*m.b107 + m.x837 - m.x966 >= -7)

m.c2983 = Constraint(expr= - 7*m.b108 + m.x838 - m.x967 >= -7)

m.c2984 = Constraint(expr= - 7*m.b109 + m.x839 - m.x968 >= -7)

m.c2985 = Constraint(expr= - 7*m.b111 + m.x841 - m.x970 >= -7)

m.c2986 = Constraint(expr= - 7*m.b112 + m.x842 - m.x971 >= -7)

m.c2987 = Constraint(expr= - 7*m.b113 + m.x843 - m.x972 >= -7)

m.c2988 = Constraint(expr= - 7*m.b114 + m.x844 - m.x973 >= -7)

m.c2989 = Constraint(expr= - 7*m.b116 + m.x846 - m.x975 >= -7)

m.c2990 = Constraint(expr= - 7*m.b117 + m.x847 - m.x976 >= -7)

m.c2991 = Constraint(expr= - 7*m.b118 + m.x848 - m.x977 >= -7)

m.c2992 = Constraint(expr= - 7*m.b119 + m.x849 - m.x978 >= -7)

m.c2993 = Constraint(expr= - 7*m.b121 + m.x656 - m.x980 >= -7)

m.c2994 = Constraint(expr= - 7*m.b122 + m.x657 - m.x981 >= -7)

m.c2995 = Constraint(expr= - 7*m.b123 + m.x658 - m.x982 >= -7)

m.c2996 = Constraint(expr= - 7*m.b124 + m.x659 - m.x983 >= -7)

m.c2997 = Constraint(expr= - 7*m.b126 + m.x661 - m.x985 >= -7)

m.c2998 = Constraint(expr= - 7*m.b127 + m.x662 - m.x986 >= -7)

m.c2999 = Constraint(expr= - 7*m.b128 + m.x663 - m.x987 >= -7)

m.c3000 = Constraint(expr= - 7*m.b129 + m.x664 - m.x988 >= -7)

m.c3001 = Constraint(expr= - 7*m.b131 + m.x666 - m.x990 >= -7)

m.c3002 = Constraint(expr= - 7*m.b132 + m.x667 - m.x991 >= -7)

m.c3003 = Constraint(expr= - 7*m.b133 + m.x668 - m.x992 >= -7)

m.c3004 = Constraint(expr= - 7*m.b134 + m.x669 - m.x993 >= -7)

m.c3005 = Constraint(expr= - 7*m.b121 + m.x671 - m.x980 >= -7)

m.c3006 = Constraint(expr= - 7*m.b122 + m.x672 - m.x981 >= -7)

m.c3007 = Constraint(expr= - 7*m.b123 + m.x673 - m.x982 >= -7)

m.c3008 = Constraint(expr= - 7*m.b124 + m.x674 - m.x983 >= -7)

m.c3009 = Constraint(expr= - 7*m.b126 + m.x676 - m.x985 >= -7)

m.c3010 = Constraint(expr= - 7*m.b127 + m.x677 - m.x986 >= -7)

m.c3011 = Constraint(expr= - 7*m.b128 + m.x678 - m.x987 >= -7)

m.c3012 = Constraint(expr= - 7*m.b129 + m.x679 - m.x988 >= -7)

m.c3013 = Constraint(expr= - 7*m.b131 + m.x681 - m.x990 >= -7)

m.c3014 = Constraint(expr= - 7*m.b132 + m.x682 - m.x991 >= -7)

m.c3015 = Constraint(expr= - 7*m.b133 + m.x683 - m.x992 >= -7)

m.c3016 = Constraint(expr= - 7*m.b134 + m.x684 - m.x993 >= -7)

m.c3017 = Constraint(expr= - 7*m.b121 + m.x686 - m.x980 >= -7)

m.c3018 = Constraint(expr= - 7*m.b122 + m.x687 - m.x981 >= -7)

m.c3019 = Constraint(expr= - 7*m.b123 + m.x688 - m.x982 >= -7)

m.c3020 = Constraint(expr= - 7*m.b124 + m.x689 - m.x983 >= -7)

m.c3021 = Constraint(expr= - 7*m.b126 + m.x691 - m.x985 >= -7)

m.c3022 = Constraint(expr= - 7*m.b127 + m.x692 - m.x986 >= -7)

m.c3023 = Constraint(expr= - 7*m.b128 + m.x693 - m.x987 >= -7)

m.c3024 = Constraint(expr= - 7*m.b129 + m.x694 - m.x988 >= -7)

m.c3025 = Constraint(expr= - 7*m.b131 + m.x696 - m.x990 >= -7)

m.c3026 = Constraint(expr= - 7*m.b132 + m.x697 - m.x991 >= -7)

m.c3027 = Constraint(expr= - 7*m.b133 + m.x698 - m.x992 >= -7)

m.c3028 = Constraint(expr= - 7*m.b134 + m.x699 - m.x993 >= -7)

m.c3029 = Constraint(expr= - 7*m.b121 + m.x701 - m.x980 >= -7)

m.c3030 = Constraint(expr= - 7*m.b122 + m.x702 - m.x981 >= -7)

m.c3031 = Constraint(expr= - 7*m.b123 + m.x703 - m.x982 >= -7)

m.c3032 = Constraint(expr= - 7*m.b124 + m.x704 - m.x983 >= -7)

m.c3033 = Constraint(expr= - 7*m.b126 + m.x706 - m.x985 >= -7)

m.c3034 = Constraint(expr= - 7*m.b127 + m.x707 - m.x986 >= -7)

m.c3035 = Constraint(expr= - 7*m.b128 + m.x708 - m.x987 >= -7)

m.c3036 = Constraint(expr= - 7*m.b129 + m.x709 - m.x988 >= -7)

m.c3037 = Constraint(expr= - 7*m.b131 + m.x711 - m.x990 >= -7)

m.c3038 = Constraint(expr= - 7*m.b132 + m.x712 - m.x991 >= -7)

m.c3039 = Constraint(expr= - 7*m.b133 + m.x713 - m.x992 >= -7)

m.c3040 = Constraint(expr= - 7*m.b134 + m.x714 - m.x993 >= -7)

m.c3041 = Constraint(expr= - 7*m.b121 + m.x716 - m.x980 >= -7)

m.c3042 = Constraint(expr= - 7*m.b122 + m.x717 - m.x981 >= -7)

m.c3043 = Constraint(expr= - 7*m.b123 + m.x718 - m.x982 >= -7)

m.c3044 = Constraint(expr= - 7*m.b124 + m.x719 - m.x983 >= -7)

m.c3045 = Constraint(expr= - 7*m.b126 + m.x721 - m.x985 >= -7)

m.c3046 = Constraint(expr= - 7*m.b127 + m.x722 - m.x986 >= -7)

m.c3047 = Constraint(expr= - 7*m.b128 + m.x723 - m.x987 >= -7)

m.c3048 = Constraint(expr= - 7*m.b129 + m.x724 - m.x988 >= -7)

m.c3049 = Constraint(expr= - 7*m.b131 + m.x726 - m.x990 >= -7)

m.c3050 = Constraint(expr= - 7*m.b132 + m.x727 - m.x991 >= -7)

m.c3051 = Constraint(expr= - 7*m.b133 + m.x728 - m.x992 >= -7)

m.c3052 = Constraint(expr= - 7*m.b134 + m.x729 - m.x993 >= -7)

m.c3053 = Constraint(expr= - 7*m.b121 + m.x731 - m.x980 >= -7)

m.c3054 = Constraint(expr= - 7*m.b122 + m.x732 - m.x981 >= -7)

m.c3055 = Constraint(expr= - 7*m.b123 + m.x733 - m.x982 >= -7)

m.c3056 = Constraint(expr= - 7*m.b124 + m.x734 - m.x983 >= -7)

m.c3057 = Constraint(expr= - 7*m.b126 + m.x736 - m.x985 >= -7)

m.c3058 = Constraint(expr= - 7*m.b127 + m.x737 - m.x986 >= -7)

m.c3059 = Constraint(expr= - 7*m.b128 + m.x738 - m.x987 >= -7)

m.c3060 = Constraint(expr= - 7*m.b129 + m.x739 - m.x988 >= -7)

m.c3061 = Constraint(expr= - 7*m.b131 + m.x741 - m.x990 >= -7)

m.c3062 = Constraint(expr= - 7*m.b132 + m.x742 - m.x991 >= -7)

m.c3063 = Constraint(expr= - 7*m.b133 + m.x743 - m.x992 >= -7)

m.c3064 = Constraint(expr= - 7*m.b134 + m.x744 - m.x993 >= -7)

m.c3065 = Constraint(expr= - 7*m.b121 + m.x746 - m.x980 >= -7)

m.c3066 = Constraint(expr= - 7*m.b122 + m.x747 - m.x981 >= -7)

m.c3067 = Constraint(expr= - 7*m.b123 + m.x748 - m.x982 >= -7)

m.c3068 = Constraint(expr= - 7*m.b124 + m.x749 - m.x983 >= -7)

m.c3069 = Constraint(expr= - 7*m.b126 + m.x751 - m.x985 >= -7)

m.c3070 = Constraint(expr= - 7*m.b127 + m.x752 - m.x986 >= -7)

m.c3071 = Constraint(expr= - 7*m.b128 + m.x753 - m.x987 >= -7)

m.c3072 = Constraint(expr= - 7*m.b129 + m.x754 - m.x988 >= -7)

m.c3073 = Constraint(expr= - 7*m.b131 + m.x756 - m.x990 >= -7)

m.c3074 = Constraint(expr= - 7*m.b132 + m.x757 - m.x991 >= -7)

m.c3075 = Constraint(expr= - 7*m.b133 + m.x758 - m.x992 >= -7)

m.c3076 = Constraint(expr= - 7*m.b134 + m.x759 - m.x993 >= -7)

m.c3077 = Constraint(expr= - 7*m.b121 + m.x761 - m.x980 >= -7)

m.c3078 = Constraint(expr= - 7*m.b122 + m.x762 - m.x981 >= -7)

m.c3079 = Constraint(expr= - 7*m.b123 + m.x763 - m.x982 >= -7)

m.c3080 = Constraint(expr= - 7*m.b124 + m.x764 - m.x983 >= -7)

m.c3081 = Constraint(expr= - 7*m.b126 + m.x766 - m.x985 >= -7)

m.c3082 = Constraint(expr= - 7*m.b127 + m.x767 - m.x986 >= -7)

m.c3083 = Constraint(expr= - 7*m.b128 + m.x768 - m.x987 >= -7)

m.c3084 = Constraint(expr= - 7*m.b129 + m.x769 - m.x988 >= -7)

m.c3085 = Constraint(expr= - 7*m.b131 + m.x771 - m.x990 >= -7)

m.c3086 = Constraint(expr= - 7*m.b132 + m.x772 - m.x991 >= -7)

m.c3087 = Constraint(expr= - 7*m.b133 + m.x773 - m.x992 >= -7)

m.c3088 = Constraint(expr= - 7*m.b134 + m.x774 - m.x993 >= -7)

m.c3089 = Constraint(expr= - 7*m.b121 + m.x821 - m.x980 >= -7)

m.c3090 = Constraint(expr= - 7*m.b122 + m.x822 - m.x981 >= -7)

m.c3091 = Constraint(expr= - 7*m.b123 + m.x823 - m.x982 >= -7)

m.c3092 = Constraint(expr= - 7*m.b124 + m.x824 - m.x983 >= -7)

m.c3093 = Constraint(expr= - 7*m.b126 + m.x826 - m.x985 >= -7)

m.c3094 = Constraint(expr= - 7*m.b127 + m.x827 - m.x986 >= -7)

m.c3095 = Constraint(expr= - 7*m.b128 + m.x828 - m.x987 >= -7)

m.c3096 = Constraint(expr= - 7*m.b129 + m.x829 - m.x988 >= -7)

m.c3097 = Constraint(expr= - 7*m.b131 + m.x831 - m.x990 >= -7)

m.c3098 = Constraint(expr= - 7*m.b132 + m.x832 - m.x991 >= -7)

m.c3099 = Constraint(expr= - 7*m.b133 + m.x833 - m.x992 >= -7)

m.c3100 = Constraint(expr= - 7*m.b134 + m.x834 - m.x993 >= -7)

m.c3101 = Constraint(expr= - 7*m.b121 + m.x836 - m.x980 >= -7)

m.c3102 = Constraint(expr= - 7*m.b122 + m.x837 - m.x981 >= -7)

m.c3103 = Constraint(expr= - 7*m.b123 + m.x838 - m.x982 >= -7)

m.c3104 = Constraint(expr= - 7*m.b124 + m.x839 - m.x983 >= -7)

m.c3105 = Constraint(expr= - 7*m.b126 + m.x841 - m.x985 >= -7)

m.c3106 = Constraint(expr= - 7*m.b127 + m.x842 - m.x986 >= -7)

m.c3107 = Constraint(expr= - 7*m.b128 + m.x843 - m.x987 >= -7)

m.c3108 = Constraint(expr= - 7*m.b129 + m.x844 - m.x988 >= -7)

m.c3109 = Constraint(expr= - 7*m.b131 + m.x846 - m.x990 >= -7)

m.c3110 = Constraint(expr= - 7*m.b132 + m.x847 - m.x991 >= -7)

m.c3111 = Constraint(expr= - 7*m.b133 + m.x848 - m.x992 >= -7)

m.c3112 = Constraint(expr= - 7*m.b134 + m.x849 - m.x993 >= -7)

m.c3113 = Constraint(expr= - 7*m.b141 + m.x801 - m.x1000 >= -7)

m.c3114 = Constraint(expr= - 7*m.b142 + m.x802 - m.x1001 >= -7)

m.c3115 = Constraint(expr= - 7*m.b143 + m.x803 - m.x1002 >= -7)

m.c3116 = Constraint(expr= - 7*m.b144 + m.x804 - m.x1003 >= -7)

m.c3117 = Constraint(expr= - 7*m.b136 + m.x806 - m.x995 >= -7)

m.c3118 = Constraint(expr= - 7*m.b137 + m.x807 - m.x996 >= -7)

m.c3119 = Constraint(expr= - 7*m.b138 + m.x808 - m.x997 >= -7)

m.c3120 = Constraint(expr= - 7*m.b139 + m.x809 - m.x998 >= -7)

m.c3121 = Constraint(expr= - 7*m.b141 + m.x811 - m.x1000 >= -7)

m.c3122 = Constraint(expr= - 7*m.b142 + m.x812 - m.x1001 >= -7)

m.c3123 = Constraint(expr= - 7*m.b143 + m.x813 - m.x1002 >= -7)

m.c3124 = Constraint(expr= - 7*m.b144 + m.x814 - m.x1003 >= -7)

m.c3125 = Constraint(expr= - 7*m.b141 + m.x816 - m.x1000 >= -7)

m.c3126 = Constraint(expr= - 7*m.b142 + m.x817 - m.x1001 >= -7)

m.c3127 = Constraint(expr= - 7*m.b143 + m.x818 - m.x1002 >= -7)

m.c3128 = Constraint(expr= - 7*m.b144 + m.x819 - m.x1003 >= -7)

m.c3129 = Constraint(expr= - 7*m.b141 + m.x851 - m.x1000 >= -7)

m.c3130 = Constraint(expr= - 7*m.b142 + m.x852 - m.x1001 >= -7)

m.c3131 = Constraint(expr= - 7*m.b143 + m.x853 - m.x1002 >= -7)

m.c3132 = Constraint(expr= - 7*m.b144 + m.x854 - m.x1003 >= -7)

m.c3133 = Constraint(expr= - 7*m.b141 + m.x856 - m.x1000 >= -7)

m.c3134 = Constraint(expr= - 7*m.b142 + m.x857 - m.x1001 >= -7)

m.c3135 = Constraint(expr= - 7*m.b143 + m.x858 - m.x1002 >= -7)

m.c3136 = Constraint(expr= - 7*m.b144 + m.x859 - m.x1003 >= -7)

m.c3137 = Constraint(expr= - 7*m.b146 + m.x796 - m.x1005 >= -7)

m.c3138 = Constraint(expr= - 7*m.b147 + m.x797 - m.x1006 >= -7)

m.c3139 = Constraint(expr= - 7*m.b148 + m.x798 - m.x1007 >= -7)

m.c3140 = Constraint(expr= - 7*m.b149 + m.x799 - m.x1008 >= -7)

m.c3141 = Constraint(expr= - 7*m.b146 + m.x811 - m.x1005 >= -7)

m.c3142 = Constraint(expr= - 7*m.b147 + m.x812 - m.x1006 >= -7)

m.c3143 = Constraint(expr= - 7*m.b148 + m.x813 - m.x1007 >= -7)

m.c3144 = Constraint(expr= - 7*m.b149 + m.x814 - m.x1008 >= -7)

m.c3145 = Constraint(expr= - 7*m.b146 + m.x816 - m.x1005 >= -7)

m.c3146 = Constraint(expr= - 7*m.b147 + m.x817 - m.x1006 >= -7)

m.c3147 = Constraint(expr= - 7*m.b148 + m.x818 - m.x1007 >= -7)

m.c3148 = Constraint(expr= - 7*m.b149 + m.x819 - m.x1008 >= -7)

m.c3149 = Constraint(expr= - 7*m.b146 + m.x851 - m.x1005 >= -7)

m.c3150 = Constraint(expr= - 7*m.b147 + m.x852 - m.x1006 >= -7)

m.c3151 = Constraint(expr= - 7*m.b148 + m.x853 - m.x1007 >= -7)

m.c3152 = Constraint(expr= - 7*m.b149 + m.x854 - m.x1008 >= -7)

m.c3153 = Constraint(expr= - 7*m.b146 + m.x856 - m.x1005 >= -7)

m.c3154 = Constraint(expr= - 7*m.b147 + m.x857 - m.x1006 >= -7)

m.c3155 = Constraint(expr= - 7*m.b148 + m.x858 - m.x1007 >= -7)

m.c3156 = Constraint(expr= - 7*m.b149 + m.x859 - m.x1008 >= -7)

m.c3157 = Constraint(expr= - 7*m.b151 + m.x791 - m.x1010 >= -7)

m.c3158 = Constraint(expr= - 7*m.b152 + m.x792 - m.x1011 >= -7)

m.c3159 = Constraint(expr= - 7*m.b153 + m.x793 - m.x1012 >= -7)

m.c3160 = Constraint(expr= - 7*m.b154 + m.x794 - m.x1013 >= -7)

m.c3161 = Constraint(expr= - 7*m.b156 + m.x796 - m.x1015 >= -7)

m.c3162 = Constraint(expr= - 7*m.b157 + m.x797 - m.x1016 >= -7)

m.c3163 = Constraint(expr= - 7*m.b158 + m.x798 - m.x1017 >= -7)

m.c3164 = Constraint(expr= - 7*m.b159 + m.x799 - m.x1018 >= -7)

m.c3165 = Constraint(expr= - 7*m.b156 + m.x801 - m.x1015 >= -7)

m.c3166 = Constraint(expr= - 7*m.b157 + m.x802 - m.x1016 >= -7)

m.c3167 = Constraint(expr= - 7*m.b158 + m.x803 - m.x1017 >= -7)

m.c3168 = Constraint(expr= - 7*m.b159 + m.x804 - m.x1018 >= -7)

m.c3169 = Constraint(expr= - 7*m.b156 + m.x816 - m.x1015 >= -7)

m.c3170 = Constraint(expr= - 7*m.b157 + m.x817 - m.x1016 >= -7)

m.c3171 = Constraint(expr= - 7*m.b158 + m.x818 - m.x1017 >= -7)

m.c3172 = Constraint(expr= - 7*m.b159 + m.x819 - m.x1018 >= -7)

m.c3173 = Constraint(expr= - 7*m.b156 + m.x851 - m.x1015 >= -7)

m.c3174 = Constraint(expr= - 7*m.b157 + m.x852 - m.x1016 >= -7)

m.c3175 = Constraint(expr= - 7*m.b158 + m.x853 - m.x1017 >= -7)

m.c3176 = Constraint(expr= - 7*m.b159 + m.x854 - m.x1018 >= -7)

m.c3177 = Constraint(expr= - 7*m.b156 + m.x856 - m.x1015 >= -7)

m.c3178 = Constraint(expr= - 7*m.b157 + m.x857 - m.x1016 >= -7)

m.c3179 = Constraint(expr= - 7*m.b158 + m.x858 - m.x1017 >= -7)

m.c3180 = Constraint(expr= - 7*m.b159 + m.x859 - m.x1018 >= -7)

m.c3181 = Constraint(expr= - 7*m.b161 + m.x796 - m.x1020 >= -7)

m.c3182 = Constraint(expr= - 7*m.b162 + m.x797 - m.x1021 >= -7)

m.c3183 = Constraint(expr= - 7*m.b163 + m.x798 - m.x1022 >= -7)

m.c3184 = Constraint(expr= - 7*m.b164 + m.x799 - m.x1023 >= -7)

m.c3185 = Constraint(expr= - 7*m.b161 + m.x801 - m.x1020 >= -7)

m.c3186 = Constraint(expr= - 7*m.b162 + m.x802 - m.x1021 >= -7)

m.c3187 = Constraint(expr= - 7*m.b163 + m.x803 - m.x1022 >= -7)

m.c3188 = Constraint(expr= - 7*m.b164 + m.x804 - m.x1023 >= -7)

m.c3189 = Constraint(expr= - 7*m.b161 + m.x811 - m.x1020 >= -7)

m.c3190 = Constraint(expr= - 7*m.b162 + m.x812 - m.x1021 >= -7)

m.c3191 = Constraint(expr= - 7*m.b163 + m.x813 - m.x1022 >= -7)

m.c3192 = Constraint(expr= - 7*m.b164 + m.x814 - m.x1023 >= -7)

m.c3193 = Constraint(expr= - 7*m.b161 + m.x851 - m.x1020 >= -7)

m.c3194 = Constraint(expr= - 7*m.b162 + m.x852 - m.x1021 >= -7)

m.c3195 = Constraint(expr= - 7*m.b163 + m.x853 - m.x1022 >= -7)

m.c3196 = Constraint(expr= - 7*m.b164 + m.x854 - m.x1023 >= -7)

m.c3197 = Constraint(expr= - 7*m.b161 + m.x856 - m.x1020 >= -7)

m.c3198 = Constraint(expr= - 7*m.b162 + m.x857 - m.x1021 >= -7)

m.c3199 = Constraint(expr= - 7*m.b163 + m.x858 - m.x1022 >= -7)

m.c3200 = Constraint(expr= - 7*m.b164 + m.x859 - m.x1023 >= -7)

m.c3201 = Constraint(expr= - 7*m.b166 + m.x656 - m.x1025 >= -7)

m.c3202 = Constraint(expr= - 7*m.b167 + m.x657 - m.x1026 >= -7)

m.c3203 = Constraint(expr= - 7*m.b168 + m.x658 - m.x1027 >= -7)

m.c3204 = Constraint(expr= - 7*m.b169 + m.x659 - m.x1028 >= -7)

m.c3205 = Constraint(expr= - 7*m.b171 + m.x661 - m.x1030 >= -7)

m.c3206 = Constraint(expr= - 7*m.b172 + m.x662 - m.x1031 >= -7)

m.c3207 = Constraint(expr= - 7*m.b173 + m.x663 - m.x1032 >= -7)

m.c3208 = Constraint(expr= - 7*m.b174 + m.x664 - m.x1033 >= -7)

m.c3209 = Constraint(expr= - 7*m.b176 + m.x666 - m.x1035 >= -7)

m.c3210 = Constraint(expr= - 7*m.b177 + m.x667 - m.x1036 >= -7)

m.c3211 = Constraint(expr= - 7*m.b178 + m.x668 - m.x1037 >= -7)

m.c3212 = Constraint(expr= - 7*m.b179 + m.x669 - m.x1038 >= -7)

m.c3213 = Constraint(expr= - 7*m.b166 + m.x671 - m.x1025 >= -7)

m.c3214 = Constraint(expr= - 7*m.b167 + m.x672 - m.x1026 >= -7)

m.c3215 = Constraint(expr= - 7*m.b168 + m.x673 - m.x1027 >= -7)

m.c3216 = Constraint(expr= - 7*m.b169 + m.x674 - m.x1028 >= -7)

m.c3217 = Constraint(expr= - 7*m.b171 + m.x676 - m.x1030 >= -7)

m.c3218 = Constraint(expr= - 7*m.b172 + m.x677 - m.x1031 >= -7)

m.c3219 = Constraint(expr= - 7*m.b173 + m.x678 - m.x1032 >= -7)

m.c3220 = Constraint(expr= - 7*m.b174 + m.x679 - m.x1033 >= -7)

m.c3221 = Constraint(expr= - 7*m.b176 + m.x681 - m.x1035 >= -7)

m.c3222 = Constraint(expr= - 7*m.b177 + m.x682 - m.x1036 >= -7)

m.c3223 = Constraint(expr= - 7*m.b178 + m.x683 - m.x1037 >= -7)

m.c3224 = Constraint(expr= - 7*m.b179 + m.x684 - m.x1038 >= -7)

m.c3225 = Constraint(expr= - 7*m.b166 + m.x686 - m.x1025 >= -7)

m.c3226 = Constraint(expr= - 7*m.b167 + m.x687 - m.x1026 >= -7)

m.c3227 = Constraint(expr= - 7*m.b168 + m.x688 - m.x1027 >= -7)

m.c3228 = Constraint(expr= - 7*m.b169 + m.x689 - m.x1028 >= -7)

m.c3229 = Constraint(expr= - 7*m.b171 + m.x691 - m.x1030 >= -7)

m.c3230 = Constraint(expr= - 7*m.b172 + m.x692 - m.x1031 >= -7)

m.c3231 = Constraint(expr= - 7*m.b173 + m.x693 - m.x1032 >= -7)

m.c3232 = Constraint(expr= - 7*m.b174 + m.x694 - m.x1033 >= -7)

m.c3233 = Constraint(expr= - 7*m.b176 + m.x696 - m.x1035 >= -7)

m.c3234 = Constraint(expr= - 7*m.b177 + m.x697 - m.x1036 >= -7)

m.c3235 = Constraint(expr= - 7*m.b178 + m.x698 - m.x1037 >= -7)

m.c3236 = Constraint(expr= - 7*m.b179 + m.x699 - m.x1038 >= -7)

m.c3237 = Constraint(expr= - 7*m.b166 + m.x701 - m.x1025 >= -7)

m.c3238 = Constraint(expr= - 7*m.b167 + m.x702 - m.x1026 >= -7)

m.c3239 = Constraint(expr= - 7*m.b168 + m.x703 - m.x1027 >= -7)

m.c3240 = Constraint(expr= - 7*m.b169 + m.x704 - m.x1028 >= -7)

m.c3241 = Constraint(expr= - 7*m.b171 + m.x706 - m.x1030 >= -7)

m.c3242 = Constraint(expr= - 7*m.b172 + m.x707 - m.x1031 >= -7)

m.c3243 = Constraint(expr= - 7*m.b173 + m.x708 - m.x1032 >= -7)

m.c3244 = Constraint(expr= - 7*m.b174 + m.x709 - m.x1033 >= -7)

m.c3245 = Constraint(expr= - 7*m.b176 + m.x711 - m.x1035 >= -7)

m.c3246 = Constraint(expr= - 7*m.b177 + m.x712 - m.x1036 >= -7)

m.c3247 = Constraint(expr= - 7*m.b178 + m.x713 - m.x1037 >= -7)

m.c3248 = Constraint(expr= - 7*m.b179 + m.x714 - m.x1038 >= -7)

m.c3249 = Constraint(expr= - 7*m.b166 + m.x716 - m.x1025 >= -7)

m.c3250 = Constraint(expr= - 7*m.b167 + m.x717 - m.x1026 >= -7)

m.c3251 = Constraint(expr= - 7*m.b168 + m.x718 - m.x1027 >= -7)

m.c3252 = Constraint(expr= - 7*m.b169 + m.x719 - m.x1028 >= -7)

m.c3253 = Constraint(expr= - 7*m.b171 + m.x721 - m.x1030 >= -7)

m.c3254 = Constraint(expr= - 7*m.b172 + m.x722 - m.x1031 >= -7)

m.c3255 = Constraint(expr= - 7*m.b173 + m.x723 - m.x1032 >= -7)

m.c3256 = Constraint(expr= - 7*m.b174 + m.x724 - m.x1033 >= -7)

m.c3257 = Constraint(expr= - 7*m.b176 + m.x726 - m.x1035 >= -7)

m.c3258 = Constraint(expr= - 7*m.b177 + m.x727 - m.x1036 >= -7)

m.c3259 = Constraint(expr= - 7*m.b178 + m.x728 - m.x1037 >= -7)

m.c3260 = Constraint(expr= - 7*m.b179 + m.x729 - m.x1038 >= -7)

m.c3261 = Constraint(expr= - 7*m.b166 + m.x731 - m.x1025 >= -7)

m.c3262 = Constraint(expr= - 7*m.b167 + m.x732 - m.x1026 >= -7)

m.c3263 = Constraint(expr= - 7*m.b168 + m.x733 - m.x1027 >= -7)

m.c3264 = Constraint(expr= - 7*m.b169 + m.x734 - m.x1028 >= -7)

m.c3265 = Constraint(expr= - 7*m.b171 + m.x736 - m.x1030 >= -7)

m.c3266 = Constraint(expr= - 7*m.b172 + m.x737 - m.x1031 >= -7)

m.c3267 = Constraint(expr= - 7*m.b173 + m.x738 - m.x1032 >= -7)

m.c3268 = Constraint(expr= - 7*m.b174 + m.x739 - m.x1033 >= -7)

m.c3269 = Constraint(expr= - 7*m.b176 + m.x741 - m.x1035 >= -7)

m.c3270 = Constraint(expr= - 7*m.b177 + m.x742 - m.x1036 >= -7)

m.c3271 = Constraint(expr= - 7*m.b178 + m.x743 - m.x1037 >= -7)

m.c3272 = Constraint(expr= - 7*m.b179 + m.x744 - m.x1038 >= -7)

m.c3273 = Constraint(expr= - 7*m.b166 + m.x746 - m.x1025 >= -7)

m.c3274 = Constraint(expr= - 7*m.b167 + m.x747 - m.x1026 >= -7)

m.c3275 = Constraint(expr= - 7*m.b168 + m.x748 - m.x1027 >= -7)

m.c3276 = Constraint(expr= - 7*m.b169 + m.x749 - m.x1028 >= -7)

m.c3277 = Constraint(expr= - 7*m.b171 + m.x751 - m.x1030 >= -7)

m.c3278 = Constraint(expr= - 7*m.b172 + m.x752 - m.x1031 >= -7)

m.c3279 = Constraint(expr= - 7*m.b173 + m.x753 - m.x1032 >= -7)

m.c3280 = Constraint(expr= - 7*m.b174 + m.x754 - m.x1033 >= -7)

m.c3281 = Constraint(expr= - 7*m.b176 + m.x756 - m.x1035 >= -7)

m.c3282 = Constraint(expr= - 7*m.b177 + m.x757 - m.x1036 >= -7)

m.c3283 = Constraint(expr= - 7*m.b178 + m.x758 - m.x1037 >= -7)

m.c3284 = Constraint(expr= - 7*m.b179 + m.x759 - m.x1038 >= -7)

m.c3285 = Constraint(expr= - 7*m.b166 + m.x761 - m.x1025 >= -7)

m.c3286 = Constraint(expr= - 7*m.b167 + m.x762 - m.x1026 >= -7)

m.c3287 = Constraint(expr= - 7*m.b168 + m.x763 - m.x1027 >= -7)

m.c3288 = Constraint(expr= - 7*m.b169 + m.x764 - m.x1028 >= -7)

m.c3289 = Constraint(expr= - 7*m.b171 + m.x766 - m.x1030 >= -7)

m.c3290 = Constraint(expr= - 7*m.b172 + m.x767 - m.x1031 >= -7)

m.c3291 = Constraint(expr= - 7*m.b173 + m.x768 - m.x1032 >= -7)

m.c3292 = Constraint(expr= - 7*m.b174 + m.x769 - m.x1033 >= -7)

m.c3293 = Constraint(expr= - 7*m.b176 + m.x771 - m.x1035 >= -7)

m.c3294 = Constraint(expr= - 7*m.b177 + m.x772 - m.x1036 >= -7)

m.c3295 = Constraint(expr= - 7*m.b178 + m.x773 - m.x1037 >= -7)

m.c3296 = Constraint(expr= - 7*m.b179 + m.x774 - m.x1038 >= -7)

m.c3297 = Constraint(expr= - 7*m.b166 + m.x776 - m.x1025 >= -7)

m.c3298 = Constraint(expr= - 7*m.b167 + m.x777 - m.x1026 >= -7)

m.c3299 = Constraint(expr= - 7*m.b168 + m.x778 - m.x1027 >= -7)

m.c3300 = Constraint(expr= - 7*m.b169 + m.x779 - m.x1028 >= -7)

m.c3301 = Constraint(expr= - 7*m.b171 + m.x781 - m.x1030 >= -7)

m.c3302 = Constraint(expr= - 7*m.b172 + m.x782 - m.x1031 >= -7)

m.c3303 = Constraint(expr= - 7*m.b173 + m.x783 - m.x1032 >= -7)

m.c3304 = Constraint(expr= - 7*m.b174 + m.x784 - m.x1033 >= -7)

m.c3305 = Constraint(expr= - 7*m.b176 + m.x786 - m.x1035 >= -7)

m.c3306 = Constraint(expr= - 7*m.b177 + m.x787 - m.x1036 >= -7)

m.c3307 = Constraint(expr= - 7*m.b178 + m.x788 - m.x1037 >= -7)

m.c3308 = Constraint(expr= - 7*m.b179 + m.x789 - m.x1038 >= -7)

m.c3309 = Constraint(expr= - 7*m.b166 + m.x836 - m.x1025 >= -7)

m.c3310 = Constraint(expr= - 7*m.b167 + m.x837 - m.x1026 >= -7)

m.c3311 = Constraint(expr= - 7*m.b168 + m.x838 - m.x1027 >= -7)

m.c3312 = Constraint(expr= - 7*m.b169 + m.x839 - m.x1028 >= -7)

m.c3313 = Constraint(expr= - 7*m.b171 + m.x841 - m.x1030 >= -7)

m.c3314 = Constraint(expr= - 7*m.b172 + m.x842 - m.x1031 >= -7)

m.c3315 = Constraint(expr= - 7*m.b173 + m.x843 - m.x1032 >= -7)

m.c3316 = Constraint(expr= - 7*m.b174 + m.x844 - m.x1033 >= -7)

m.c3317 = Constraint(expr= - 7*m.b176 + m.x846 - m.x1035 >= -7)

m.c3318 = Constraint(expr= - 7*m.b177 + m.x847 - m.x1036 >= -7)

m.c3319 = Constraint(expr= - 7*m.b178 + m.x848 - m.x1037 >= -7)

m.c3320 = Constraint(expr= - 7*m.b179 + m.x849 - m.x1038 >= -7)

m.c3321 = Constraint(expr= - 7*m.b181 + m.x656 - m.x1040 >= -7)

m.c3322 = Constraint(expr= - 7*m.b182 + m.x657 - m.x1041 >= -7)

m.c3323 = Constraint(expr= - 7*m.b183 + m.x658 - m.x1042 >= -7)

m.c3324 = Constraint(expr= - 7*m.b184 + m.x659 - m.x1043 >= -7)

m.c3325 = Constraint(expr= - 7*m.b186 + m.x661 - m.x1045 >= -7)

m.c3326 = Constraint(expr= - 7*m.b187 + m.x662 - m.x1046 >= -7)

m.c3327 = Constraint(expr= - 7*m.b188 + m.x663 - m.x1047 >= -7)

m.c3328 = Constraint(expr= - 7*m.b189 + m.x664 - m.x1048 >= -7)

m.c3329 = Constraint(expr= - 7*m.b191 + m.x666 - m.x1050 >= -7)

m.c3330 = Constraint(expr= - 7*m.b192 + m.x667 - m.x1051 >= -7)

m.c3331 = Constraint(expr= - 7*m.b193 + m.x668 - m.x1052 >= -7)

m.c3332 = Constraint(expr= - 7*m.b194 + m.x669 - m.x1053 >= -7)

m.c3333 = Constraint(expr= - 7*m.b181 + m.x671 - m.x1040 >= -7)

m.c3334 = Constraint(expr= - 7*m.b182 + m.x672 - m.x1041 >= -7)

m.c3335 = Constraint(expr= - 7*m.b183 + m.x673 - m.x1042 >= -7)

m.c3336 = Constraint(expr= - 7*m.b184 + m.x674 - m.x1043 >= -7)

m.c3337 = Constraint(expr= - 7*m.b186 + m.x676 - m.x1045 >= -7)

m.c3338 = Constraint(expr= - 7*m.b187 + m.x677 - m.x1046 >= -7)

m.c3339 = Constraint(expr= - 7*m.b188 + m.x678 - m.x1047 >= -7)

m.c3340 = Constraint(expr= - 7*m.b189 + m.x679 - m.x1048 >= -7)

m.c3341 = Constraint(expr= - 7*m.b191 + m.x681 - m.x1050 >= -7)

m.c3342 = Constraint(expr= - 7*m.b192 + m.x682 - m.x1051 >= -7)

m.c3343 = Constraint(expr= - 7*m.b193 + m.x683 - m.x1052 >= -7)

m.c3344 = Constraint(expr= - 7*m.b194 + m.x684 - m.x1053 >= -7)

m.c3345 = Constraint(expr= - 7*m.b181 + m.x686 - m.x1040 >= -7)

m.c3346 = Constraint(expr= - 7*m.b182 + m.x687 - m.x1041 >= -7)

m.c3347 = Constraint(expr= - 7*m.b183 + m.x688 - m.x1042 >= -7)

m.c3348 = Constraint(expr= - 7*m.b184 + m.x689 - m.x1043 >= -7)

m.c3349 = Constraint(expr= - 7*m.b186 + m.x691 - m.x1045 >= -7)

m.c3350 = Constraint(expr= - 7*m.b187 + m.x692 - m.x1046 >= -7)

m.c3351 = Constraint(expr= - 7*m.b188 + m.x693 - m.x1047 >= -7)

m.c3352 = Constraint(expr= - 7*m.b189 + m.x694 - m.x1048 >= -7)

m.c3353 = Constraint(expr= - 7*m.b191 + m.x696 - m.x1050 >= -7)

m.c3354 = Constraint(expr= - 7*m.b192 + m.x697 - m.x1051 >= -7)

m.c3355 = Constraint(expr= - 7*m.b193 + m.x698 - m.x1052 >= -7)

m.c3356 = Constraint(expr= - 7*m.b194 + m.x699 - m.x1053 >= -7)

m.c3357 = Constraint(expr= - 7*m.b181 + m.x701 - m.x1040 >= -7)

m.c3358 = Constraint(expr= - 7*m.b182 + m.x702 - m.x1041 >= -7)

m.c3359 = Constraint(expr= - 7*m.b183 + m.x703 - m.x1042 >= -7)

m.c3360 = Constraint(expr= - 7*m.b184 + m.x704 - m.x1043 >= -7)

m.c3361 = Constraint(expr= - 7*m.b186 + m.x706 - m.x1045 >= -7)

m.c3362 = Constraint(expr= - 7*m.b187 + m.x707 - m.x1046 >= -7)

m.c3363 = Constraint(expr= - 7*m.b188 + m.x708 - m.x1047 >= -7)

m.c3364 = Constraint(expr= - 7*m.b189 + m.x709 - m.x1048 >= -7)

m.c3365 = Constraint(expr= - 7*m.b191 + m.x711 - m.x1050 >= -7)

m.c3366 = Constraint(expr= - 7*m.b192 + m.x712 - m.x1051 >= -7)

m.c3367 = Constraint(expr= - 7*m.b193 + m.x713 - m.x1052 >= -7)

m.c3368 = Constraint(expr= - 7*m.b194 + m.x714 - m.x1053 >= -7)

m.c3369 = Constraint(expr= - 7*m.b181 + m.x716 - m.x1040 >= -7)

m.c3370 = Constraint(expr= - 7*m.b182 + m.x717 - m.x1041 >= -7)

m.c3371 = Constraint(expr= - 7*m.b183 + m.x718 - m.x1042 >= -7)

m.c3372 = Constraint(expr= - 7*m.b184 + m.x719 - m.x1043 >= -7)

m.c3373 = Constraint(expr= - 7*m.b186 + m.x721 - m.x1045 >= -7)

m.c3374 = Constraint(expr= - 7*m.b187 + m.x722 - m.x1046 >= -7)

m.c3375 = Constraint(expr= - 7*m.b188 + m.x723 - m.x1047 >= -7)

m.c3376 = Constraint(expr= - 7*m.b189 + m.x724 - m.x1048 >= -7)

m.c3377 = Constraint(expr= - 7*m.b191 + m.x726 - m.x1050 >= -7)

m.c3378 = Constraint(expr= - 7*m.b192 + m.x727 - m.x1051 >= -7)

m.c3379 = Constraint(expr= - 7*m.b193 + m.x728 - m.x1052 >= -7)

m.c3380 = Constraint(expr= - 7*m.b194 + m.x729 - m.x1053 >= -7)

m.c3381 = Constraint(expr= - 7*m.b181 + m.x731 - m.x1040 >= -7)

m.c3382 = Constraint(expr= - 7*m.b182 + m.x732 - m.x1041 >= -7)

m.c3383 = Constraint(expr= - 7*m.b183 + m.x733 - m.x1042 >= -7)

m.c3384 = Constraint(expr= - 7*m.b184 + m.x734 - m.x1043 >= -7)

m.c3385 = Constraint(expr= - 7*m.b186 + m.x736 - m.x1045 >= -7)

m.c3386 = Constraint(expr= - 7*m.b187 + m.x737 - m.x1046 >= -7)

m.c3387 = Constraint(expr= - 7*m.b188 + m.x738 - m.x1047 >= -7)

m.c3388 = Constraint(expr= - 7*m.b189 + m.x739 - m.x1048 >= -7)

m.c3389 = Constraint(expr= - 7*m.b191 + m.x741 - m.x1050 >= -7)

m.c3390 = Constraint(expr= - 7*m.b192 + m.x742 - m.x1051 >= -7)

m.c3391 = Constraint(expr= - 7*m.b193 + m.x743 - m.x1052 >= -7)

m.c3392 = Constraint(expr= - 7*m.b194 + m.x744 - m.x1053 >= -7)

m.c3393 = Constraint(expr= - 7*m.b181 + m.x746 - m.x1040 >= -7)

m.c3394 = Constraint(expr= - 7*m.b182 + m.x747 - m.x1041 >= -7)

m.c3395 = Constraint(expr= - 7*m.b183 + m.x748 - m.x1042 >= -7)

m.c3396 = Constraint(expr= - 7*m.b184 + m.x749 - m.x1043 >= -7)

m.c3397 = Constraint(expr= - 7*m.b186 + m.x751 - m.x1045 >= -7)

m.c3398 = Constraint(expr= - 7*m.b187 + m.x752 - m.x1046 >= -7)

m.c3399 = Constraint(expr= - 7*m.b188 + m.x753 - m.x1047 >= -7)

m.c3400 = Constraint(expr= - 7*m.b189 + m.x754 - m.x1048 >= -7)

m.c3401 = Constraint(expr= - 7*m.b191 + m.x756 - m.x1050 >= -7)

m.c3402 = Constraint(expr= - 7*m.b192 + m.x757 - m.x1051 >= -7)

m.c3403 = Constraint(expr= - 7*m.b193 + m.x758 - m.x1052 >= -7)

m.c3404 = Constraint(expr= - 7*m.b194 + m.x759 - m.x1053 >= -7)

m.c3405 = Constraint(expr= - 7*m.b181 + m.x761 - m.x1040 >= -7)

m.c3406 = Constraint(expr= - 7*m.b182 + m.x762 - m.x1041 >= -7)

m.c3407 = Constraint(expr= - 7*m.b183 + m.x763 - m.x1042 >= -7)

m.c3408 = Constraint(expr= - 7*m.b184 + m.x764 - m.x1043 >= -7)

m.c3409 = Constraint(expr= - 7*m.b186 + m.x766 - m.x1045 >= -7)

m.c3410 = Constraint(expr= - 7*m.b187 + m.x767 - m.x1046 >= -7)

m.c3411 = Constraint(expr= - 7*m.b188 + m.x768 - m.x1047 >= -7)

m.c3412 = Constraint(expr= - 7*m.b189 + m.x769 - m.x1048 >= -7)

m.c3413 = Constraint(expr= - 7*m.b191 + m.x771 - m.x1050 >= -7)

m.c3414 = Constraint(expr= - 7*m.b192 + m.x772 - m.x1051 >= -7)

m.c3415 = Constraint(expr= - 7*m.b193 + m.x773 - m.x1052 >= -7)

m.c3416 = Constraint(expr= - 7*m.b194 + m.x774 - m.x1053 >= -7)

m.c3417 = Constraint(expr= - 7*m.b181 + m.x776 - m.x1040 >= -7)

m.c3418 = Constraint(expr= - 7*m.b182 + m.x777 - m.x1041 >= -7)

m.c3419 = Constraint(expr= - 7*m.b183 + m.x778 - m.x1042 >= -7)

m.c3420 = Constraint(expr= - 7*m.b184 + m.x779 - m.x1043 >= -7)

m.c3421 = Constraint(expr= - 7*m.b186 + m.x781 - m.x1045 >= -7)

m.c3422 = Constraint(expr= - 7*m.b187 + m.x782 - m.x1046 >= -7)

m.c3423 = Constraint(expr= - 7*m.b188 + m.x783 - m.x1047 >= -7)

m.c3424 = Constraint(expr= - 7*m.b189 + m.x784 - m.x1048 >= -7)

m.c3425 = Constraint(expr= - 7*m.b191 + m.x786 - m.x1050 >= -7)

m.c3426 = Constraint(expr= - 7*m.b192 + m.x787 - m.x1051 >= -7)

m.c3427 = Constraint(expr= - 7*m.b193 + m.x788 - m.x1052 >= -7)

m.c3428 = Constraint(expr= - 7*m.b194 + m.x789 - m.x1053 >= -7)

m.c3429 = Constraint(expr= - 7*m.b181 + m.x821 - m.x1040 >= -7)

m.c3430 = Constraint(expr= - 7*m.b182 + m.x822 - m.x1041 >= -7)

m.c3431 = Constraint(expr= - 7*m.b183 + m.x823 - m.x1042 >= -7)

m.c3432 = Constraint(expr= - 7*m.b184 + m.x824 - m.x1043 >= -7)

m.c3433 = Constraint(expr= - 7*m.b186 + m.x826 - m.x1045 >= -7)

m.c3434 = Constraint(expr= - 7*m.b187 + m.x827 - m.x1046 >= -7)

m.c3435 = Constraint(expr= - 7*m.b188 + m.x828 - m.x1047 >= -7)

m.c3436 = Constraint(expr= - 7*m.b189 + m.x829 - m.x1048 >= -7)

m.c3437 = Constraint(expr= - 7*m.b191 + m.x831 - m.x1050 >= -7)

m.c3438 = Constraint(expr= - 7*m.b192 + m.x832 - m.x1051 >= -7)

m.c3439 = Constraint(expr= - 7*m.b193 + m.x833 - m.x1052 >= -7)

m.c3440 = Constraint(expr= - 7*m.b194 + m.x834 - m.x1053 >= -7)

m.c3441 = Constraint(expr= - 7*m.b196 + m.x796 - m.x1055 >= -7)

m.c3442 = Constraint(expr= - 7*m.b197 + m.x797 - m.x1056 >= -7)

m.c3443 = Constraint(expr= - 7*m.b198 + m.x798 - m.x1057 >= -7)

m.c3444 = Constraint(expr= - 7*m.b199 + m.x799 - m.x1058 >= -7)

m.c3445 = Constraint(expr= - 7*m.b196 + m.x801 - m.x1055 >= -7)

m.c3446 = Constraint(expr= - 7*m.b197 + m.x802 - m.x1056 >= -7)

m.c3447 = Constraint(expr= - 7*m.b198 + m.x803 - m.x1057 >= -7)

m.c3448 = Constraint(expr= - 7*m.b199 + m.x804 - m.x1058 >= -7)

m.c3449 = Constraint(expr= - 7*m.b196 + m.x811 - m.x1055 >= -7)

m.c3450 = Constraint(expr= - 7*m.b197 + m.x812 - m.x1056 >= -7)

m.c3451 = Constraint(expr= - 7*m.b198 + m.x813 - m.x1057 >= -7)

m.c3452 = Constraint(expr= - 7*m.b199 + m.x814 - m.x1058 >= -7)

m.c3453 = Constraint(expr= - 7*m.b196 + m.x816 - m.x1055 >= -7)

m.c3454 = Constraint(expr= - 7*m.b197 + m.x817 - m.x1056 >= -7)

m.c3455 = Constraint(expr= - 7*m.b198 + m.x818 - m.x1057 >= -7)

m.c3456 = Constraint(expr= - 7*m.b199 + m.x819 - m.x1058 >= -7)

m.c3457 = Constraint(expr= - 7*m.b196 + m.x856 - m.x1055 >= -7)

m.c3458 = Constraint(expr= - 7*m.b197 + m.x857 - m.x1056 >= -7)

m.c3459 = Constraint(expr= - 7*m.b198 + m.x858 - m.x1057 >= -7)

m.c3460 = Constraint(expr= - 7*m.b199 + m.x859 - m.x1058 >= -7)

m.c3461 = Constraint(expr= - 7*m.b201 + m.x796 - m.x1060 >= -7)

m.c3462 = Constraint(expr= - 7*m.b202 + m.x797 - m.x1061 >= -7)

m.c3463 = Constraint(expr= - 7*m.b203 + m.x798 - m.x1062 >= -7)

m.c3464 = Constraint(expr= - 7*m.b204 + m.x799 - m.x1063 >= -7)

m.c3465 = Constraint(expr= - 7*m.b201 + m.x801 - m.x1060 >= -7)

m.c3466 = Constraint(expr= - 7*m.b202 + m.x802 - m.x1061 >= -7)

m.c3467 = Constraint(expr= - 7*m.b203 + m.x803 - m.x1062 >= -7)

m.c3468 = Constraint(expr= - 7*m.b204 + m.x804 - m.x1063 >= -7)

m.c3469 = Constraint(expr= - 7*m.b201 + m.x811 - m.x1060 >= -7)

m.c3470 = Constraint(expr= - 7*m.b202 + m.x812 - m.x1061 >= -7)

m.c3471 = Constraint(expr= - 7*m.b203 + m.x813 - m.x1062 >= -7)

m.c3472 = Constraint(expr= - 7*m.b204 + m.x814 - m.x1063 >= -7)

m.c3473 = Constraint(expr= - 7*m.b201 + m.x816 - m.x1060 >= -7)

m.c3474 = Constraint(expr= - 7*m.b202 + m.x817 - m.x1061 >= -7)

m.c3475 = Constraint(expr= - 7*m.b203 + m.x818 - m.x1062 >= -7)

m.c3476 = Constraint(expr= - 7*m.b204 + m.x819 - m.x1063 >= -7)

m.c3477 = Constraint(expr= - 7*m.b201 + m.x851 - m.x1060 >= -7)

m.c3478 = Constraint(expr= - 7*m.b202 + m.x852 - m.x1061 >= -7)

m.c3479 = Constraint(expr= - 7*m.b203 + m.x853 - m.x1062 >= -7)

m.c3480 = Constraint(expr= - 7*m.b204 + m.x854 - m.x1063 >= -7)

m.c3481 = Constraint(expr=   7*m.b1 + 7*m.b2 + m.x656 - m.x860 <= 14)

m.c3482 = Constraint(expr=   7*m.b2 + 7*m.b3 + m.x657 - m.x861 <= 14)

m.c3483 = Constraint(expr=   7*m.b3 + 7*m.b4 + m.x658 - m.x862 <= 14)

m.c3484 = Constraint(expr=   7*m.b4 + 7*m.b5 + m.x659 - m.x863 <= 14)

m.c3485 = Constraint(expr=   7*m.b1 + 7*m.b7 + m.x661 - m.x860 <= 14)

m.c3486 = Constraint(expr=   7*m.b2 + 7*m.b8 + m.x662 - m.x861 <= 14)

m.c3487 = Constraint(expr=   7*m.b3 + 7*m.b9 + m.x663 - m.x862 <= 14)

m.c3488 = Constraint(expr=   7*m.b4 + 7*m.b10 + m.x664 - m.x863 <= 14)

m.c3489 = Constraint(expr=   7*m.b1 + 7*m.b12 + m.x666 - m.x860 <= 14)

m.c3490 = Constraint(expr=   7*m.b2 + 7*m.b13 + m.x667 - m.x861 <= 14)

m.c3491 = Constraint(expr=   7*m.b3 + 7*m.b14 + m.x668 - m.x862 <= 14)

m.c3492 = Constraint(expr=   7*m.b4 + 7*m.b15 + m.x669 - m.x863 <= 14)

m.c3493 = Constraint(expr=   7*m.b2 + 7*m.b6 + m.x656 - m.x865 <= 14)

m.c3494 = Constraint(expr=   7*m.b3 + 7*m.b7 + m.x657 - m.x866 <= 14)

m.c3495 = Constraint(expr=   7*m.b4 + 7*m.b8 + m.x658 - m.x867 <= 14)

m.c3496 = Constraint(expr=   7*m.b5 + 7*m.b9 + m.x659 - m.x868 <= 14)

m.c3497 = Constraint(expr=   7*m.b6 + 7*m.b7 + m.x661 - m.x865 <= 14)

m.c3498 = Constraint(expr=   7*m.b7 + 7*m.b8 + m.x662 - m.x866 <= 14)

m.c3499 = Constraint(expr=   7*m.b8 + 7*m.b9 + m.x663 - m.x867 <= 14)

m.c3500 = Constraint(expr=   7*m.b9 + 7*m.b10 + m.x664 - m.x868 <= 14)

m.c3501 = Constraint(expr=   7*m.b6 + 7*m.b12 + m.x666 - m.x865 <= 14)

m.c3502 = Constraint(expr=   7*m.b7 + 7*m.b13 + m.x667 - m.x866 <= 14)

m.c3503 = Constraint(expr=   7*m.b8 + 7*m.b14 + m.x668 - m.x867 <= 14)

m.c3504 = Constraint(expr=   7*m.b9 + 7*m.b15 + m.x669 - m.x868 <= 14)

m.c3505 = Constraint(expr=   7*m.b2 + 7*m.b11 + m.x656 - m.x870 <= 14)

m.c3506 = Constraint(expr=   7*m.b3 + 7*m.b12 + m.x657 - m.x871 <= 14)

m.c3507 = Constraint(expr=   7*m.b4 + 7*m.b13 + m.x658 - m.x872 <= 14)

m.c3508 = Constraint(expr=   7*m.b5 + 7*m.b14 + m.x659 - m.x873 <= 14)

m.c3509 = Constraint(expr=   7*m.b7 + 7*m.b11 + m.x661 - m.x870 <= 14)

m.c3510 = Constraint(expr=   7*m.b8 + 7*m.b12 + m.x662 - m.x871 <= 14)

m.c3511 = Constraint(expr=   7*m.b9 + 7*m.b13 + m.x663 - m.x872 <= 14)

m.c3512 = Constraint(expr=   7*m.b10 + 7*m.b14 + m.x664 - m.x873 <= 14)

m.c3513 = Constraint(expr=   7*m.b11 + 7*m.b12 + m.x666 - m.x870 <= 14)

m.c3514 = Constraint(expr=   7*m.b12 + 7*m.b13 + m.x667 - m.x871 <= 14)

m.c3515 = Constraint(expr=   7*m.b13 + 7*m.b14 + m.x668 - m.x872 <= 14)

m.c3516 = Constraint(expr=   7*m.b14 + 7*m.b15 + m.x669 - m.x873 <= 14)

m.c3517 = Constraint(expr=   7*m.b16 + 7*m.b17 + m.x671 - m.x875 <= 14)

m.c3518 = Constraint(expr=   7*m.b17 + 7*m.b18 + m.x672 - m.x876 <= 14)

m.c3519 = Constraint(expr=   7*m.b18 + 7*m.b19 + m.x673 - m.x877 <= 14)

m.c3520 = Constraint(expr=   7*m.b19 + 7*m.b20 + m.x674 - m.x878 <= 14)

m.c3521 = Constraint(expr=   7*m.b16 + 7*m.b22 + m.x676 - m.x875 <= 14)

m.c3522 = Constraint(expr=   7*m.b17 + 7*m.b23 + m.x677 - m.x876 <= 14)

m.c3523 = Constraint(expr=   7*m.b18 + 7*m.b24 + m.x678 - m.x877 <= 14)

m.c3524 = Constraint(expr=   7*m.b19 + 7*m.b25 + m.x679 - m.x878 <= 14)

m.c3525 = Constraint(expr=   7*m.b16 + 7*m.b27 + m.x681 - m.x875 <= 14)

m.c3526 = Constraint(expr=   7*m.b17 + 7*m.b28 + m.x682 - m.x876 <= 14)

m.c3527 = Constraint(expr=   7*m.b18 + 7*m.b29 + m.x683 - m.x877 <= 14)

m.c3528 = Constraint(expr=   7*m.b19 + 7*m.b30 + m.x684 - m.x878 <= 14)

m.c3529 = Constraint(expr=   7*m.b17 + 7*m.b21 + m.x671 - m.x880 <= 14)

m.c3530 = Constraint(expr=   7*m.b18 + 7*m.b22 + m.x672 - m.x881 <= 14)

m.c3531 = Constraint(expr=   7*m.b19 + 7*m.b23 + m.x673 - m.x882 <= 14)

m.c3532 = Constraint(expr=   7*m.b20 + 7*m.b24 + m.x674 - m.x883 <= 14)

m.c3533 = Constraint(expr=   7*m.b21 + 7*m.b22 + m.x676 - m.x880 <= 14)

m.c3534 = Constraint(expr=   7*m.b22 + 7*m.b23 + m.x677 - m.x881 <= 14)

m.c3535 = Constraint(expr=   7*m.b23 + 7*m.b24 + m.x678 - m.x882 <= 14)

m.c3536 = Constraint(expr=   7*m.b24 + 7*m.b25 + m.x679 - m.x883 <= 14)

m.c3537 = Constraint(expr=   7*m.b21 + 7*m.b27 + m.x681 - m.x880 <= 14)

m.c3538 = Constraint(expr=   7*m.b22 + 7*m.b28 + m.x682 - m.x881 <= 14)

m.c3539 = Constraint(expr=   7*m.b23 + 7*m.b29 + m.x683 - m.x882 <= 14)

m.c3540 = Constraint(expr=   7*m.b24 + 7*m.b30 + m.x684 - m.x883 <= 14)

m.c3541 = Constraint(expr=   7*m.b17 + 7*m.b26 + m.x671 - m.x885 <= 14)

m.c3542 = Constraint(expr=   7*m.b18 + 7*m.b27 + m.x672 - m.x886 <= 14)

m.c3543 = Constraint(expr=   7*m.b19 + 7*m.b28 + m.x673 - m.x887 <= 14)

m.c3544 = Constraint(expr=   7*m.b20 + 7*m.b29 + m.x674 - m.x888 <= 14)

m.c3545 = Constraint(expr=   7*m.b22 + 7*m.b26 + m.x676 - m.x885 <= 14)

m.c3546 = Constraint(expr=   7*m.b23 + 7*m.b27 + m.x677 - m.x886 <= 14)

m.c3547 = Constraint(expr=   7*m.b24 + 7*m.b28 + m.x678 - m.x887 <= 14)

m.c3548 = Constraint(expr=   7*m.b25 + 7*m.b29 + m.x679 - m.x888 <= 14)

m.c3549 = Constraint(expr=   7*m.b26 + 7*m.b27 + m.x681 - m.x885 <= 14)

m.c3550 = Constraint(expr=   7*m.b27 + 7*m.b28 + m.x682 - m.x886 <= 14)

m.c3551 = Constraint(expr=   7*m.b28 + 7*m.b29 + m.x683 - m.x887 <= 14)

m.c3552 = Constraint(expr=   7*m.b29 + 7*m.b30 + m.x684 - m.x888 <= 14)

m.c3553 = Constraint(expr=   7*m.b31 + 7*m.b32 + m.x686 - m.x890 <= 14)

m.c3554 = Constraint(expr=   7*m.b32 + 7*m.b33 + m.x687 - m.x891 <= 14)

m.c3555 = Constraint(expr=   7*m.b33 + 7*m.b34 + m.x688 - m.x892 <= 14)

m.c3556 = Constraint(expr=   7*m.b34 + 7*m.b35 + m.x689 - m.x893 <= 14)

m.c3557 = Constraint(expr=   7*m.b31 + 7*m.b37 + m.x691 - m.x890 <= 14)

m.c3558 = Constraint(expr=   7*m.b32 + 7*m.b38 + m.x692 - m.x891 <= 14)

m.c3559 = Constraint(expr=   7*m.b33 + 7*m.b39 + m.x693 - m.x892 <= 14)

m.c3560 = Constraint(expr=   7*m.b34 + 7*m.b40 + m.x694 - m.x893 <= 14)

m.c3561 = Constraint(expr=   7*m.b31 + 7*m.b42 + m.x696 - m.x890 <= 14)

m.c3562 = Constraint(expr=   7*m.b32 + 7*m.b43 + m.x697 - m.x891 <= 14)

m.c3563 = Constraint(expr=   7*m.b33 + 7*m.b44 + m.x698 - m.x892 <= 14)

m.c3564 = Constraint(expr=   7*m.b34 + 7*m.b45 + m.x699 - m.x893 <= 14)

m.c3565 = Constraint(expr=   7*m.b32 + 7*m.b36 + m.x686 - m.x895 <= 14)

m.c3566 = Constraint(expr=   7*m.b33 + 7*m.b37 + m.x687 - m.x896 <= 14)

m.c3567 = Constraint(expr=   7*m.b34 + 7*m.b38 + m.x688 - m.x897 <= 14)

m.c3568 = Constraint(expr=   7*m.b35 + 7*m.b39 + m.x689 - m.x898 <= 14)

m.c3569 = Constraint(expr=   7*m.b36 + 7*m.b37 + m.x691 - m.x895 <= 14)

m.c3570 = Constraint(expr=   7*m.b37 + 7*m.b38 + m.x692 - m.x896 <= 14)

m.c3571 = Constraint(expr=   7*m.b38 + 7*m.b39 + m.x693 - m.x897 <= 14)

m.c3572 = Constraint(expr=   7*m.b39 + 7*m.b40 + m.x694 - m.x898 <= 14)

m.c3573 = Constraint(expr=   7*m.b36 + 7*m.b42 + m.x696 - m.x895 <= 14)

m.c3574 = Constraint(expr=   7*m.b37 + 7*m.b43 + m.x697 - m.x896 <= 14)

m.c3575 = Constraint(expr=   7*m.b38 + 7*m.b44 + m.x698 - m.x897 <= 14)

m.c3576 = Constraint(expr=   7*m.b39 + 7*m.b45 + m.x699 - m.x898 <= 14)

m.c3577 = Constraint(expr=   7*m.b32 + 7*m.b41 + m.x686 - m.x900 <= 14)

m.c3578 = Constraint(expr=   7*m.b33 + 7*m.b42 + m.x687 - m.x901 <= 14)

m.c3579 = Constraint(expr=   7*m.b34 + 7*m.b43 + m.x688 - m.x902 <= 14)

m.c3580 = Constraint(expr=   7*m.b35 + 7*m.b44 + m.x689 - m.x903 <= 14)

m.c3581 = Constraint(expr=   7*m.b37 + 7*m.b41 + m.x691 - m.x900 <= 14)

m.c3582 = Constraint(expr=   7*m.b38 + 7*m.b42 + m.x692 - m.x901 <= 14)

m.c3583 = Constraint(expr=   7*m.b39 + 7*m.b43 + m.x693 - m.x902 <= 14)

m.c3584 = Constraint(expr=   7*m.b40 + 7*m.b44 + m.x694 - m.x903 <= 14)

m.c3585 = Constraint(expr=   7*m.b41 + 7*m.b42 + m.x696 - m.x900 <= 14)

m.c3586 = Constraint(expr=   7*m.b42 + 7*m.b43 + m.x697 - m.x901 <= 14)

m.c3587 = Constraint(expr=   7*m.b43 + 7*m.b44 + m.x698 - m.x902 <= 14)

m.c3588 = Constraint(expr=   7*m.b44 + 7*m.b45 + m.x699 - m.x903 <= 14)

m.c3589 = Constraint(expr=   7*m.b46 + 7*m.b47 + m.x701 - m.x905 <= 14)

m.c3590 = Constraint(expr=   7*m.b47 + 7*m.b48 + m.x702 - m.x906 <= 14)

m.c3591 = Constraint(expr=   7*m.b48 + 7*m.b49 + m.x703 - m.x907 <= 14)

m.c3592 = Constraint(expr=   7*m.b49 + 7*m.b50 + m.x704 - m.x908 <= 14)

m.c3593 = Constraint(expr=   7*m.b46 + 7*m.b52 + m.x706 - m.x905 <= 14)

m.c3594 = Constraint(expr=   7*m.b47 + 7*m.b53 + m.x707 - m.x906 <= 14)

m.c3595 = Constraint(expr=   7*m.b48 + 7*m.b54 + m.x708 - m.x907 <= 14)

m.c3596 = Constraint(expr=   7*m.b49 + 7*m.b55 + m.x709 - m.x908 <= 14)

m.c3597 = Constraint(expr=   7*m.b46 + 7*m.b57 + m.x711 - m.x905 <= 14)

m.c3598 = Constraint(expr=   7*m.b47 + 7*m.b58 + m.x712 - m.x906 <= 14)

m.c3599 = Constraint(expr=   7*m.b48 + 7*m.b59 + m.x713 - m.x907 <= 14)

m.c3600 = Constraint(expr=   7*m.b49 + 7*m.b60 + m.x714 - m.x908 <= 14)

m.c3601 = Constraint(expr=   7*m.b47 + 7*m.b51 + m.x701 - m.x910 <= 14)

m.c3602 = Constraint(expr=   7*m.b48 + 7*m.b52 + m.x702 - m.x911 <= 14)

m.c3603 = Constraint(expr=   7*m.b49 + 7*m.b53 + m.x703 - m.x912 <= 14)

m.c3604 = Constraint(expr=   7*m.b50 + 7*m.b54 + m.x704 - m.x913 <= 14)

m.c3605 = Constraint(expr=   7*m.b51 + 7*m.b52 + m.x706 - m.x910 <= 14)

m.c3606 = Constraint(expr=   7*m.b52 + 7*m.b53 + m.x707 - m.x911 <= 14)

m.c3607 = Constraint(expr=   7*m.b53 + 7*m.b54 + m.x708 - m.x912 <= 14)

m.c3608 = Constraint(expr=   7*m.b54 + 7*m.b55 + m.x709 - m.x913 <= 14)

m.c3609 = Constraint(expr=   7*m.b51 + 7*m.b57 + m.x711 - m.x910 <= 14)

m.c3610 = Constraint(expr=   7*m.b52 + 7*m.b58 + m.x712 - m.x911 <= 14)

m.c3611 = Constraint(expr=   7*m.b53 + 7*m.b59 + m.x713 - m.x912 <= 14)

m.c3612 = Constraint(expr=   7*m.b54 + 7*m.b60 + m.x714 - m.x913 <= 14)

m.c3613 = Constraint(expr=   7*m.b47 + 7*m.b56 + m.x701 - m.x915 <= 14)

m.c3614 = Constraint(expr=   7*m.b48 + 7*m.b57 + m.x702 - m.x916 <= 14)

m.c3615 = Constraint(expr=   7*m.b49 + 7*m.b58 + m.x703 - m.x917 <= 14)

m.c3616 = Constraint(expr=   7*m.b50 + 7*m.b59 + m.x704 - m.x918 <= 14)

m.c3617 = Constraint(expr=   7*m.b52 + 7*m.b56 + m.x706 - m.x915 <= 14)

m.c3618 = Constraint(expr=   7*m.b53 + 7*m.b57 + m.x707 - m.x916 <= 14)

m.c3619 = Constraint(expr=   7*m.b54 + 7*m.b58 + m.x708 - m.x917 <= 14)

m.c3620 = Constraint(expr=   7*m.b55 + 7*m.b59 + m.x709 - m.x918 <= 14)

m.c3621 = Constraint(expr=   7*m.b56 + 7*m.b57 + m.x711 - m.x915 <= 14)

m.c3622 = Constraint(expr=   7*m.b57 + 7*m.b58 + m.x712 - m.x916 <= 14)

m.c3623 = Constraint(expr=   7*m.b58 + 7*m.b59 + m.x713 - m.x917 <= 14)

m.c3624 = Constraint(expr=   7*m.b59 + 7*m.b60 + m.x714 - m.x918 <= 14)

m.c3625 = Constraint(expr=   7*m.b61 + 7*m.b62 + m.x716 - m.x920 <= 14)

m.c3626 = Constraint(expr=   7*m.b62 + 7*m.b63 + m.x717 - m.x921 <= 14)

m.c3627 = Constraint(expr=   7*m.b63 + 7*m.b64 + m.x718 - m.x922 <= 14)

m.c3628 = Constraint(expr=   7*m.b64 + 7*m.b65 + m.x719 - m.x923 <= 14)

m.c3629 = Constraint(expr=   7*m.b61 + 7*m.b67 + m.x721 - m.x920 <= 14)

m.c3630 = Constraint(expr=   7*m.b62 + 7*m.b68 + m.x722 - m.x921 <= 14)

m.c3631 = Constraint(expr=   7*m.b63 + 7*m.b69 + m.x723 - m.x922 <= 14)

m.c3632 = Constraint(expr=   7*m.b64 + 7*m.b70 + m.x724 - m.x923 <= 14)

m.c3633 = Constraint(expr=   7*m.b61 + 7*m.b72 + m.x726 - m.x920 <= 14)

m.c3634 = Constraint(expr=   7*m.b62 + 7*m.b73 + m.x727 - m.x921 <= 14)

m.c3635 = Constraint(expr=   7*m.b63 + 7*m.b74 + m.x728 - m.x922 <= 14)

m.c3636 = Constraint(expr=   7*m.b64 + 7*m.b75 + m.x729 - m.x923 <= 14)

m.c3637 = Constraint(expr=   7*m.b62 + 7*m.b66 + m.x716 - m.x925 <= 14)

m.c3638 = Constraint(expr=   7*m.b63 + 7*m.b67 + m.x717 - m.x926 <= 14)

m.c3639 = Constraint(expr=   7*m.b64 + 7*m.b68 + m.x718 - m.x927 <= 14)

m.c3640 = Constraint(expr=   7*m.b65 + 7*m.b69 + m.x719 - m.x928 <= 14)

m.c3641 = Constraint(expr=   7*m.b66 + 7*m.b67 + m.x721 - m.x925 <= 14)

m.c3642 = Constraint(expr=   7*m.b67 + 7*m.b68 + m.x722 - m.x926 <= 14)

m.c3643 = Constraint(expr=   7*m.b68 + 7*m.b69 + m.x723 - m.x927 <= 14)

m.c3644 = Constraint(expr=   7*m.b69 + 7*m.b70 + m.x724 - m.x928 <= 14)

m.c3645 = Constraint(expr=   7*m.b66 + 7*m.b72 + m.x726 - m.x925 <= 14)

m.c3646 = Constraint(expr=   7*m.b67 + 7*m.b73 + m.x727 - m.x926 <= 14)

m.c3647 = Constraint(expr=   7*m.b68 + 7*m.b74 + m.x728 - m.x927 <= 14)

m.c3648 = Constraint(expr=   7*m.b69 + 7*m.b75 + m.x729 - m.x928 <= 14)

m.c3649 = Constraint(expr=   7*m.b62 + 7*m.b71 + m.x716 - m.x930 <= 14)

m.c3650 = Constraint(expr=   7*m.b63 + 7*m.b72 + m.x717 - m.x931 <= 14)

m.c3651 = Constraint(expr=   7*m.b64 + 7*m.b73 + m.x718 - m.x932 <= 14)

m.c3652 = Constraint(expr=   7*m.b65 + 7*m.b74 + m.x719 - m.x933 <= 14)

m.c3653 = Constraint(expr=   7*m.b67 + 7*m.b71 + m.x721 - m.x930 <= 14)

m.c3654 = Constraint(expr=   7*m.b68 + 7*m.b72 + m.x722 - m.x931 <= 14)

m.c3655 = Constraint(expr=   7*m.b69 + 7*m.b73 + m.x723 - m.x932 <= 14)

m.c3656 = Constraint(expr=   7*m.b70 + 7*m.b74 + m.x724 - m.x933 <= 14)

m.c3657 = Constraint(expr=   7*m.b71 + 7*m.b72 + m.x726 - m.x930 <= 14)

m.c3658 = Constraint(expr=   7*m.b72 + 7*m.b73 + m.x727 - m.x931 <= 14)

m.c3659 = Constraint(expr=   7*m.b73 + 7*m.b74 + m.x728 - m.x932 <= 14)

m.c3660 = Constraint(expr=   7*m.b74 + 7*m.b75 + m.x729 - m.x933 <= 14)

m.c3661 = Constraint(expr=   7*m.b76 + 7*m.b77 + m.x731 - m.x935 <= 14)

m.c3662 = Constraint(expr=   7*m.b77 + 7*m.b78 + m.x732 - m.x936 <= 14)

m.c3663 = Constraint(expr=   7*m.b78 + 7*m.b79 + m.x733 - m.x937 <= 14)

m.c3664 = Constraint(expr=   7*m.b79 + 7*m.b80 + m.x734 - m.x938 <= 14)

m.c3665 = Constraint(expr=   7*m.b76 + 7*m.b82 + m.x736 - m.x935 <= 14)

m.c3666 = Constraint(expr=   7*m.b77 + 7*m.b83 + m.x737 - m.x936 <= 14)

m.c3667 = Constraint(expr=   7*m.b78 + 7*m.b84 + m.x738 - m.x937 <= 14)

m.c3668 = Constraint(expr=   7*m.b79 + 7*m.b85 + m.x739 - m.x938 <= 14)

m.c3669 = Constraint(expr=   7*m.b76 + 7*m.b87 + m.x741 - m.x935 <= 14)

m.c3670 = Constraint(expr=   7*m.b77 + 7*m.b88 + m.x742 - m.x936 <= 14)

m.c3671 = Constraint(expr=   7*m.b78 + 7*m.b89 + m.x743 - m.x937 <= 14)

m.c3672 = Constraint(expr=   7*m.b79 + 7*m.b90 + m.x744 - m.x938 <= 14)

m.c3673 = Constraint(expr=   7*m.b77 + 7*m.b81 + m.x731 - m.x940 <= 14)

m.c3674 = Constraint(expr=   7*m.b78 + 7*m.b82 + m.x732 - m.x941 <= 14)

m.c3675 = Constraint(expr=   7*m.b79 + 7*m.b83 + m.x733 - m.x942 <= 14)

m.c3676 = Constraint(expr=   7*m.b80 + 7*m.b84 + m.x734 - m.x943 <= 14)

m.c3677 = Constraint(expr=   7*m.b81 + 7*m.b82 + m.x736 - m.x940 <= 14)

m.c3678 = Constraint(expr=   7*m.b82 + 7*m.b83 + m.x737 - m.x941 <= 14)

m.c3679 = Constraint(expr=   7*m.b83 + 7*m.b84 + m.x738 - m.x942 <= 14)

m.c3680 = Constraint(expr=   7*m.b84 + 7*m.b85 + m.x739 - m.x943 <= 14)

m.c3681 = Constraint(expr=   7*m.b81 + 7*m.b87 + m.x741 - m.x940 <= 14)

m.c3682 = Constraint(expr=   7*m.b82 + 7*m.b88 + m.x742 - m.x941 <= 14)

m.c3683 = Constraint(expr=   7*m.b83 + 7*m.b89 + m.x743 - m.x942 <= 14)

m.c3684 = Constraint(expr=   7*m.b84 + 7*m.b90 + m.x744 - m.x943 <= 14)

m.c3685 = Constraint(expr=   7*m.b77 + 7*m.b86 + m.x731 - m.x945 <= 14)

m.c3686 = Constraint(expr=   7*m.b78 + 7*m.b87 + m.x732 - m.x946 <= 14)

m.c3687 = Constraint(expr=   7*m.b79 + 7*m.b88 + m.x733 - m.x947 <= 14)

m.c3688 = Constraint(expr=   7*m.b80 + 7*m.b89 + m.x734 - m.x948 <= 14)

m.c3689 = Constraint(expr=   7*m.b82 + 7*m.b86 + m.x736 - m.x945 <= 14)

m.c3690 = Constraint(expr=   7*m.b83 + 7*m.b87 + m.x737 - m.x946 <= 14)

m.c3691 = Constraint(expr=   7*m.b84 + 7*m.b88 + m.x738 - m.x947 <= 14)

m.c3692 = Constraint(expr=   7*m.b85 + 7*m.b89 + m.x739 - m.x948 <= 14)

m.c3693 = Constraint(expr=   7*m.b86 + 7*m.b87 + m.x741 - m.x945 <= 14)

m.c3694 = Constraint(expr=   7*m.b87 + 7*m.b88 + m.x742 - m.x946 <= 14)

m.c3695 = Constraint(expr=   7*m.b88 + 7*m.b89 + m.x743 - m.x947 <= 14)

m.c3696 = Constraint(expr=   7*m.b89 + 7*m.b90 + m.x744 - m.x948 <= 14)

m.c3697 = Constraint(expr=   7*m.b91 + 7*m.b92 + m.x746 - m.x950 <= 14)

m.c3698 = Constraint(expr=   7*m.b92 + 7*m.b93 + m.x747 - m.x951 <= 14)

m.c3699 = Constraint(expr=   7*m.b93 + 7*m.b94 + m.x748 - m.x952 <= 14)

m.c3700 = Constraint(expr=   7*m.b94 + 7*m.b95 + m.x749 - m.x953 <= 14)

m.c3701 = Constraint(expr=   7*m.b91 + 7*m.b97 + m.x751 - m.x950 <= 14)

m.c3702 = Constraint(expr=   7*m.b92 + 7*m.b98 + m.x752 - m.x951 <= 14)

m.c3703 = Constraint(expr=   7*m.b93 + 7*m.b99 + m.x753 - m.x952 <= 14)

m.c3704 = Constraint(expr=   7*m.b94 + 7*m.b100 + m.x754 - m.x953 <= 14)

m.c3705 = Constraint(expr=   7*m.b91 + 7*m.b102 + m.x756 - m.x950 <= 14)

m.c3706 = Constraint(expr=   7*m.b92 + 7*m.b103 + m.x757 - m.x951 <= 14)

m.c3707 = Constraint(expr=   7*m.b93 + 7*m.b104 + m.x758 - m.x952 <= 14)

m.c3708 = Constraint(expr=   7*m.b94 + 7*m.b105 + m.x759 - m.x953 <= 14)

m.c3709 = Constraint(expr=   7*m.b92 + 7*m.b96 + m.x746 - m.x955 <= 14)

m.c3710 = Constraint(expr=   7*m.b93 + 7*m.b97 + m.x747 - m.x956 <= 14)

m.c3711 = Constraint(expr=   7*m.b94 + 7*m.b98 + m.x748 - m.x957 <= 14)

m.c3712 = Constraint(expr=   7*m.b95 + 7*m.b99 + m.x749 - m.x958 <= 14)

m.c3713 = Constraint(expr=   7*m.b96 + 7*m.b97 + m.x751 - m.x955 <= 14)

m.c3714 = Constraint(expr=   7*m.b97 + 7*m.b98 + m.x752 - m.x956 <= 14)

m.c3715 = Constraint(expr=   7*m.b98 + 7*m.b99 + m.x753 - m.x957 <= 14)

m.c3716 = Constraint(expr=   7*m.b99 + 7*m.b100 + m.x754 - m.x958 <= 14)

m.c3717 = Constraint(expr=   7*m.b96 + 7*m.b102 + m.x756 - m.x955 <= 14)

m.c3718 = Constraint(expr=   7*m.b97 + 7*m.b103 + m.x757 - m.x956 <= 14)

m.c3719 = Constraint(expr=   7*m.b98 + 7*m.b104 + m.x758 - m.x957 <= 14)

m.c3720 = Constraint(expr=   7*m.b99 + 7*m.b105 + m.x759 - m.x958 <= 14)

m.c3721 = Constraint(expr=   7*m.b92 + 7*m.b101 + m.x746 - m.x960 <= 14)

m.c3722 = Constraint(expr=   7*m.b93 + 7*m.b102 + m.x747 - m.x961 <= 14)

m.c3723 = Constraint(expr=   7*m.b94 + 7*m.b103 + m.x748 - m.x962 <= 14)

m.c3724 = Constraint(expr=   7*m.b95 + 7*m.b104 + m.x749 - m.x963 <= 14)

m.c3725 = Constraint(expr=   7*m.b97 + 7*m.b101 + m.x751 - m.x960 <= 14)

m.c3726 = Constraint(expr=   7*m.b98 + 7*m.b102 + m.x752 - m.x961 <= 14)

m.c3727 = Constraint(expr=   7*m.b99 + 7*m.b103 + m.x753 - m.x962 <= 14)

m.c3728 = Constraint(expr=   7*m.b100 + 7*m.b104 + m.x754 - m.x963 <= 14)

m.c3729 = Constraint(expr=   7*m.b101 + 7*m.b102 + m.x756 - m.x960 <= 14)

m.c3730 = Constraint(expr=   7*m.b102 + 7*m.b103 + m.x757 - m.x961 <= 14)

m.c3731 = Constraint(expr=   7*m.b103 + 7*m.b104 + m.x758 - m.x962 <= 14)

m.c3732 = Constraint(expr=   7*m.b104 + 7*m.b105 + m.x759 - m.x963 <= 14)

m.c3733 = Constraint(expr=   7*m.b106 + 7*m.b107 + m.x761 - m.x965 <= 14)

m.c3734 = Constraint(expr=   7*m.b107 + 7*m.b108 + m.x762 - m.x966 <= 14)

m.c3735 = Constraint(expr=   7*m.b108 + 7*m.b109 + m.x763 - m.x967 <= 14)

m.c3736 = Constraint(expr=   7*m.b109 + 7*m.b110 + m.x764 - m.x968 <= 14)

m.c3737 = Constraint(expr=   7*m.b106 + 7*m.b112 + m.x766 - m.x965 <= 14)

m.c3738 = Constraint(expr=   7*m.b107 + 7*m.b113 + m.x767 - m.x966 <= 14)

m.c3739 = Constraint(expr=   7*m.b108 + 7*m.b114 + m.x768 - m.x967 <= 14)

m.c3740 = Constraint(expr=   7*m.b109 + 7*m.b115 + m.x769 - m.x968 <= 14)

m.c3741 = Constraint(expr=   7*m.b106 + 7*m.b117 + m.x771 - m.x965 <= 14)

m.c3742 = Constraint(expr=   7*m.b107 + 7*m.b118 + m.x772 - m.x966 <= 14)

m.c3743 = Constraint(expr=   7*m.b108 + 7*m.b119 + m.x773 - m.x967 <= 14)

m.c3744 = Constraint(expr=   7*m.b109 + 7*m.b120 + m.x774 - m.x968 <= 14)

m.c3745 = Constraint(expr=   7*m.b107 + 7*m.b111 + m.x761 - m.x970 <= 14)

m.c3746 = Constraint(expr=   7*m.b108 + 7*m.b112 + m.x762 - m.x971 <= 14)

m.c3747 = Constraint(expr=   7*m.b109 + 7*m.b113 + m.x763 - m.x972 <= 14)

m.c3748 = Constraint(expr=   7*m.b110 + 7*m.b114 + m.x764 - m.x973 <= 14)

m.c3749 = Constraint(expr=   7*m.b111 + 7*m.b112 + m.x766 - m.x970 <= 14)

m.c3750 = Constraint(expr=   7*m.b112 + 7*m.b113 + m.x767 - m.x971 <= 14)

m.c3751 = Constraint(expr=   7*m.b113 + 7*m.b114 + m.x768 - m.x972 <= 14)

m.c3752 = Constraint(expr=   7*m.b114 + 7*m.b115 + m.x769 - m.x973 <= 14)

m.c3753 = Constraint(expr=   7*m.b111 + 7*m.b117 + m.x771 - m.x970 <= 14)

m.c3754 = Constraint(expr=   7*m.b112 + 7*m.b118 + m.x772 - m.x971 <= 14)

m.c3755 = Constraint(expr=   7*m.b113 + 7*m.b119 + m.x773 - m.x972 <= 14)

m.c3756 = Constraint(expr=   7*m.b114 + 7*m.b120 + m.x774 - m.x973 <= 14)

m.c3757 = Constraint(expr=   7*m.b107 + 7*m.b116 + m.x761 - m.x975 <= 14)

m.c3758 = Constraint(expr=   7*m.b108 + 7*m.b117 + m.x762 - m.x976 <= 14)

m.c3759 = Constraint(expr=   7*m.b109 + 7*m.b118 + m.x763 - m.x977 <= 14)

m.c3760 = Constraint(expr=   7*m.b110 + 7*m.b119 + m.x764 - m.x978 <= 14)

m.c3761 = Constraint(expr=   7*m.b112 + 7*m.b116 + m.x766 - m.x975 <= 14)

m.c3762 = Constraint(expr=   7*m.b113 + 7*m.b117 + m.x767 - m.x976 <= 14)

m.c3763 = Constraint(expr=   7*m.b114 + 7*m.b118 + m.x768 - m.x977 <= 14)

m.c3764 = Constraint(expr=   7*m.b115 + 7*m.b119 + m.x769 - m.x978 <= 14)

m.c3765 = Constraint(expr=   7*m.b116 + 7*m.b117 + m.x771 - m.x975 <= 14)

m.c3766 = Constraint(expr=   7*m.b117 + 7*m.b118 + m.x772 - m.x976 <= 14)

m.c3767 = Constraint(expr=   7*m.b118 + 7*m.b119 + m.x773 - m.x977 <= 14)

m.c3768 = Constraint(expr=   7*m.b119 + 7*m.b120 + m.x774 - m.x978 <= 14)

m.c3769 = Constraint(expr=   7*m.b121 + 7*m.b122 + m.x776 - m.x980 <= 14)

m.c3770 = Constraint(expr=   7*m.b122 + 7*m.b123 + m.x777 - m.x981 <= 14)

m.c3771 = Constraint(expr=   7*m.b123 + 7*m.b124 + m.x778 - m.x982 <= 14)

m.c3772 = Constraint(expr=   7*m.b124 + 7*m.b125 + m.x779 - m.x983 <= 14)

m.c3773 = Constraint(expr=   7*m.b121 + 7*m.b127 + m.x781 - m.x980 <= 14)

m.c3774 = Constraint(expr=   7*m.b122 + 7*m.b128 + m.x782 - m.x981 <= 14)

m.c3775 = Constraint(expr=   7*m.b123 + 7*m.b129 + m.x783 - m.x982 <= 14)

m.c3776 = Constraint(expr=   7*m.b124 + 7*m.b130 + m.x784 - m.x983 <= 14)

m.c3777 = Constraint(expr=   7*m.b121 + 7*m.b132 + m.x786 - m.x980 <= 14)

m.c3778 = Constraint(expr=   7*m.b122 + 7*m.b133 + m.x787 - m.x981 <= 14)

m.c3779 = Constraint(expr=   7*m.b123 + 7*m.b134 + m.x788 - m.x982 <= 14)

m.c3780 = Constraint(expr=   7*m.b124 + 7*m.b135 + m.x789 - m.x983 <= 14)

m.c3781 = Constraint(expr=   7*m.b122 + 7*m.b126 + m.x776 - m.x985 <= 14)

m.c3782 = Constraint(expr=   7*m.b123 + 7*m.b127 + m.x777 - m.x986 <= 14)

m.c3783 = Constraint(expr=   7*m.b124 + 7*m.b128 + m.x778 - m.x987 <= 14)

m.c3784 = Constraint(expr=   7*m.b125 + 7*m.b129 + m.x779 - m.x988 <= 14)

m.c3785 = Constraint(expr=   7*m.b126 + 7*m.b127 + m.x781 - m.x985 <= 14)

m.c3786 = Constraint(expr=   7*m.b127 + 7*m.b128 + m.x782 - m.x986 <= 14)

m.c3787 = Constraint(expr=   7*m.b128 + 7*m.b129 + m.x783 - m.x987 <= 14)

m.c3788 = Constraint(expr=   7*m.b129 + 7*m.b130 + m.x784 - m.x988 <= 14)

m.c3789 = Constraint(expr=   7*m.b126 + 7*m.b132 + m.x786 - m.x985 <= 14)

m.c3790 = Constraint(expr=   7*m.b127 + 7*m.b133 + m.x787 - m.x986 <= 14)

m.c3791 = Constraint(expr=   7*m.b128 + 7*m.b134 + m.x788 - m.x987 <= 14)

m.c3792 = Constraint(expr=   7*m.b129 + 7*m.b135 + m.x789 - m.x988 <= 14)

m.c3793 = Constraint(expr=   7*m.b122 + 7*m.b131 + m.x776 - m.x990 <= 14)

m.c3794 = Constraint(expr=   7*m.b123 + 7*m.b132 + m.x777 - m.x991 <= 14)

m.c3795 = Constraint(expr=   7*m.b124 + 7*m.b133 + m.x778 - m.x992 <= 14)

m.c3796 = Constraint(expr=   7*m.b125 + 7*m.b134 + m.x779 - m.x993 <= 14)

m.c3797 = Constraint(expr=   7*m.b127 + 7*m.b131 + m.x781 - m.x990 <= 14)

m.c3798 = Constraint(expr=   7*m.b128 + 7*m.b132 + m.x782 - m.x991 <= 14)

m.c3799 = Constraint(expr=   7*m.b129 + 7*m.b133 + m.x783 - m.x992 <= 14)

m.c3800 = Constraint(expr=   7*m.b130 + 7*m.b134 + m.x784 - m.x993 <= 14)

m.c3801 = Constraint(expr=   7*m.b131 + 7*m.b132 + m.x786 - m.x990 <= 14)

m.c3802 = Constraint(expr=   7*m.b132 + 7*m.b133 + m.x787 - m.x991 <= 14)

m.c3803 = Constraint(expr=   7*m.b133 + 7*m.b134 + m.x788 - m.x992 <= 14)

m.c3804 = Constraint(expr=   7*m.b134 + 7*m.b135 + m.x789 - m.x993 <= 14)

m.c3805 = Constraint(expr=   7*m.b136 + 7*m.b137 + m.x791 - m.x995 <= 14)

m.c3806 = Constraint(expr=   7*m.b137 + 7*m.b138 + m.x792 - m.x996 <= 14)

m.c3807 = Constraint(expr=   7*m.b138 + 7*m.b139 + m.x793 - m.x997 <= 14)

m.c3808 = Constraint(expr=   7*m.b139 + 7*m.b140 + m.x794 - m.x998 <= 14)

m.c3809 = Constraint(expr=   7*m.b136 + 7*m.b142 + m.x796 - m.x995 <= 14)

m.c3810 = Constraint(expr=   7*m.b137 + 7*m.b143 + m.x797 - m.x996 <= 14)

m.c3811 = Constraint(expr=   7*m.b138 + 7*m.b144 + m.x798 - m.x997 <= 14)

m.c3812 = Constraint(expr=   7*m.b139 + 7*m.b145 + m.x799 - m.x998 <= 14)

m.c3813 = Constraint(expr=   7*m.b137 + 7*m.b141 + m.x791 - m.x1000 <= 14)

m.c3814 = Constraint(expr=   7*m.b138 + 7*m.b142 + m.x792 - m.x1001 <= 14)

m.c3815 = Constraint(expr=   7*m.b139 + 7*m.b143 + m.x793 - m.x1002 <= 14)

m.c3816 = Constraint(expr=   7*m.b140 + 7*m.b144 + m.x794 - m.x1003 <= 14)

m.c3817 = Constraint(expr=   7*m.b141 + 7*m.b142 + m.x796 - m.x1000 <= 14)

m.c3818 = Constraint(expr=   7*m.b142 + 7*m.b143 + m.x797 - m.x1001 <= 14)

m.c3819 = Constraint(expr=   7*m.b143 + 7*m.b144 + m.x798 - m.x1002 <= 14)

m.c3820 = Constraint(expr=   7*m.b144 + 7*m.b145 + m.x799 - m.x1003 <= 14)

m.c3821 = Constraint(expr=   7*m.b146 + 7*m.b147 + m.x801 - m.x1005 <= 14)

m.c3822 = Constraint(expr=   7*m.b147 + 7*m.b148 + m.x802 - m.x1006 <= 14)

m.c3823 = Constraint(expr=   7*m.b148 + 7*m.b149 + m.x803 - m.x1007 <= 14)

m.c3824 = Constraint(expr=   7*m.b149 + 7*m.b150 + m.x804 - m.x1008 <= 14)

m.c3825 = Constraint(expr=   7*m.b151 + 7*m.b152 + m.x806 - m.x1010 <= 14)

m.c3826 = Constraint(expr=   7*m.b152 + 7*m.b153 + m.x807 - m.x1011 <= 14)

m.c3827 = Constraint(expr=   7*m.b153 + 7*m.b154 + m.x808 - m.x1012 <= 14)

m.c3828 = Constraint(expr=   7*m.b154 + 7*m.b155 + m.x809 - m.x1013 <= 14)

m.c3829 = Constraint(expr=   7*m.b151 + 7*m.b157 + m.x811 - m.x1010 <= 14)

m.c3830 = Constraint(expr=   7*m.b152 + 7*m.b158 + m.x812 - m.x1011 <= 14)

m.c3831 = Constraint(expr=   7*m.b153 + 7*m.b159 + m.x813 - m.x1012 <= 14)

m.c3832 = Constraint(expr=   7*m.b154 + 7*m.b160 + m.x814 - m.x1013 <= 14)

m.c3833 = Constraint(expr=   7*m.b152 + 7*m.b156 + m.x806 - m.x1015 <= 14)

m.c3834 = Constraint(expr=   7*m.b153 + 7*m.b157 + m.x807 - m.x1016 <= 14)

m.c3835 = Constraint(expr=   7*m.b154 + 7*m.b158 + m.x808 - m.x1017 <= 14)

m.c3836 = Constraint(expr=   7*m.b155 + 7*m.b159 + m.x809 - m.x1018 <= 14)

m.c3837 = Constraint(expr=   7*m.b156 + 7*m.b157 + m.x811 - m.x1015 <= 14)

m.c3838 = Constraint(expr=   7*m.b157 + 7*m.b158 + m.x812 - m.x1016 <= 14)

m.c3839 = Constraint(expr=   7*m.b158 + 7*m.b159 + m.x813 - m.x1017 <= 14)

m.c3840 = Constraint(expr=   7*m.b159 + 7*m.b160 + m.x814 - m.x1018 <= 14)

m.c3841 = Constraint(expr=   7*m.b161 + 7*m.b162 + m.x816 - m.x1020 <= 14)

m.c3842 = Constraint(expr=   7*m.b162 + 7*m.b163 + m.x817 - m.x1021 <= 14)

m.c3843 = Constraint(expr=   7*m.b163 + 7*m.b164 + m.x818 - m.x1022 <= 14)

m.c3844 = Constraint(expr=   7*m.b164 + 7*m.b165 + m.x819 - m.x1023 <= 14)

m.c3845 = Constraint(expr=   7*m.b166 + 7*m.b167 + m.x821 - m.x1025 <= 14)

m.c3846 = Constraint(expr=   7*m.b167 + 7*m.b168 + m.x822 - m.x1026 <= 14)

m.c3847 = Constraint(expr=   7*m.b168 + 7*m.b169 + m.x823 - m.x1027 <= 14)

m.c3848 = Constraint(expr=   7*m.b169 + 7*m.b170 + m.x824 - m.x1028 <= 14)

m.c3849 = Constraint(expr=   7*m.b166 + 7*m.b172 + m.x826 - m.x1025 <= 14)

m.c3850 = Constraint(expr=   7*m.b167 + 7*m.b173 + m.x827 - m.x1026 <= 14)

m.c3851 = Constraint(expr=   7*m.b168 + 7*m.b174 + m.x828 - m.x1027 <= 14)

m.c3852 = Constraint(expr=   7*m.b169 + 7*m.b175 + m.x829 - m.x1028 <= 14)

m.c3853 = Constraint(expr=   7*m.b166 + 7*m.b177 + m.x831 - m.x1025 <= 14)

m.c3854 = Constraint(expr=   7*m.b167 + 7*m.b178 + m.x832 - m.x1026 <= 14)

m.c3855 = Constraint(expr=   7*m.b168 + 7*m.b179 + m.x833 - m.x1027 <= 14)

m.c3856 = Constraint(expr=   7*m.b169 + 7*m.b180 + m.x834 - m.x1028 <= 14)

m.c3857 = Constraint(expr=   7*m.b167 + 7*m.b171 + m.x821 - m.x1030 <= 14)

m.c3858 = Constraint(expr=   7*m.b168 + 7*m.b172 + m.x822 - m.x1031 <= 14)

m.c3859 = Constraint(expr=   7*m.b169 + 7*m.b173 + m.x823 - m.x1032 <= 14)

m.c3860 = Constraint(expr=   7*m.b170 + 7*m.b174 + m.x824 - m.x1033 <= 14)

m.c3861 = Constraint(expr=   7*m.b171 + 7*m.b172 + m.x826 - m.x1030 <= 14)

m.c3862 = Constraint(expr=   7*m.b172 + 7*m.b173 + m.x827 - m.x1031 <= 14)

m.c3863 = Constraint(expr=   7*m.b173 + 7*m.b174 + m.x828 - m.x1032 <= 14)

m.c3864 = Constraint(expr=   7*m.b174 + 7*m.b175 + m.x829 - m.x1033 <= 14)

m.c3865 = Constraint(expr=   7*m.b171 + 7*m.b177 + m.x831 - m.x1030 <= 14)

m.c3866 = Constraint(expr=   7*m.b172 + 7*m.b178 + m.x832 - m.x1031 <= 14)

m.c3867 = Constraint(expr=   7*m.b173 + 7*m.b179 + m.x833 - m.x1032 <= 14)

m.c3868 = Constraint(expr=   7*m.b174 + 7*m.b180 + m.x834 - m.x1033 <= 14)

m.c3869 = Constraint(expr=   7*m.b167 + 7*m.b176 + m.x821 - m.x1035 <= 14)

m.c3870 = Constraint(expr=   7*m.b168 + 7*m.b177 + m.x822 - m.x1036 <= 14)

m.c3871 = Constraint(expr=   7*m.b169 + 7*m.b178 + m.x823 - m.x1037 <= 14)

m.c3872 = Constraint(expr=   7*m.b170 + 7*m.b179 + m.x824 - m.x1038 <= 14)

m.c3873 = Constraint(expr=   7*m.b172 + 7*m.b176 + m.x826 - m.x1035 <= 14)

m.c3874 = Constraint(expr=   7*m.b173 + 7*m.b177 + m.x827 - m.x1036 <= 14)

m.c3875 = Constraint(expr=   7*m.b174 + 7*m.b178 + m.x828 - m.x1037 <= 14)

m.c3876 = Constraint(expr=   7*m.b175 + 7*m.b179 + m.x829 - m.x1038 <= 14)

m.c3877 = Constraint(expr=   7*m.b176 + 7*m.b177 + m.x831 - m.x1035 <= 14)

m.c3878 = Constraint(expr=   7*m.b177 + 7*m.b178 + m.x832 - m.x1036 <= 14)

m.c3879 = Constraint(expr=   7*m.b178 + 7*m.b179 + m.x833 - m.x1037 <= 14)

m.c3880 = Constraint(expr=   7*m.b179 + 7*m.b180 + m.x834 - m.x1038 <= 14)

m.c3881 = Constraint(expr=   7*m.b181 + 7*m.b182 + m.x836 - m.x1040 <= 14)

m.c3882 = Constraint(expr=   7*m.b182 + 7*m.b183 + m.x837 - m.x1041 <= 14)

m.c3883 = Constraint(expr=   7*m.b183 + 7*m.b184 + m.x838 - m.x1042 <= 14)

m.c3884 = Constraint(expr=   7*m.b184 + 7*m.b185 + m.x839 - m.x1043 <= 14)

m.c3885 = Constraint(expr=   7*m.b181 + 7*m.b187 + m.x841 - m.x1040 <= 14)

m.c3886 = Constraint(expr=   7*m.b182 + 7*m.b188 + m.x842 - m.x1041 <= 14)

m.c3887 = Constraint(expr=   7*m.b183 + 7*m.b189 + m.x843 - m.x1042 <= 14)

m.c3888 = Constraint(expr=   7*m.b184 + 7*m.b190 + m.x844 - m.x1043 <= 14)

m.c3889 = Constraint(expr=   7*m.b181 + 7*m.b192 + m.x846 - m.x1040 <= 14)

m.c3890 = Constraint(expr=   7*m.b182 + 7*m.b193 + m.x847 - m.x1041 <= 14)

m.c3891 = Constraint(expr=   7*m.b183 + 7*m.b194 + m.x848 - m.x1042 <= 14)

m.c3892 = Constraint(expr=   7*m.b184 + 7*m.b195 + m.x849 - m.x1043 <= 14)

m.c3893 = Constraint(expr=   7*m.b182 + 7*m.b186 + m.x836 - m.x1045 <= 14)

m.c3894 = Constraint(expr=   7*m.b183 + 7*m.b187 + m.x837 - m.x1046 <= 14)

m.c3895 = Constraint(expr=   7*m.b184 + 7*m.b188 + m.x838 - m.x1047 <= 14)

m.c3896 = Constraint(expr=   7*m.b185 + 7*m.b189 + m.x839 - m.x1048 <= 14)

m.c3897 = Constraint(expr=   7*m.b186 + 7*m.b187 + m.x841 - m.x1045 <= 14)

m.c3898 = Constraint(expr=   7*m.b187 + 7*m.b188 + m.x842 - m.x1046 <= 14)

m.c3899 = Constraint(expr=   7*m.b188 + 7*m.b189 + m.x843 - m.x1047 <= 14)

m.c3900 = Constraint(expr=   7*m.b189 + 7*m.b190 + m.x844 - m.x1048 <= 14)

m.c3901 = Constraint(expr=   7*m.b186 + 7*m.b192 + m.x846 - m.x1045 <= 14)

m.c3902 = Constraint(expr=   7*m.b187 + 7*m.b193 + m.x847 - m.x1046 <= 14)

m.c3903 = Constraint(expr=   7*m.b188 + 7*m.b194 + m.x848 - m.x1047 <= 14)

m.c3904 = Constraint(expr=   7*m.b189 + 7*m.b195 + m.x849 - m.x1048 <= 14)

m.c3905 = Constraint(expr=   7*m.b182 + 7*m.b191 + m.x836 - m.x1050 <= 14)

m.c3906 = Constraint(expr=   7*m.b183 + 7*m.b192 + m.x837 - m.x1051 <= 14)

m.c3907 = Constraint(expr=   7*m.b184 + 7*m.b193 + m.x838 - m.x1052 <= 14)

m.c3908 = Constraint(expr=   7*m.b185 + 7*m.b194 + m.x839 - m.x1053 <= 14)

m.c3909 = Constraint(expr=   7*m.b187 + 7*m.b191 + m.x841 - m.x1050 <= 14)

m.c3910 = Constraint(expr=   7*m.b188 + 7*m.b192 + m.x842 - m.x1051 <= 14)

m.c3911 = Constraint(expr=   7*m.b189 + 7*m.b193 + m.x843 - m.x1052 <= 14)

m.c3912 = Constraint(expr=   7*m.b190 + 7*m.b194 + m.x844 - m.x1053 <= 14)

m.c3913 = Constraint(expr=   7*m.b191 + 7*m.b192 + m.x846 - m.x1050 <= 14)

m.c3914 = Constraint(expr=   7*m.b192 + 7*m.b193 + m.x847 - m.x1051 <= 14)

m.c3915 = Constraint(expr=   7*m.b193 + 7*m.b194 + m.x848 - m.x1052 <= 14)

m.c3916 = Constraint(expr=   7*m.b194 + 7*m.b195 + m.x849 - m.x1053 <= 14)

m.c3917 = Constraint(expr=   7*m.b196 + 7*m.b197 + m.x851 - m.x1055 <= 14)

m.c3918 = Constraint(expr=   7*m.b197 + 7*m.b198 + m.x852 - m.x1056 <= 14)

m.c3919 = Constraint(expr=   7*m.b198 + 7*m.b199 + m.x853 - m.x1057 <= 14)

m.c3920 = Constraint(expr=   7*m.b199 + 7*m.b200 + m.x854 - m.x1058 <= 14)

m.c3921 = Constraint(expr=   7*m.b201 + 7*m.b202 + m.x856 - m.x1060 <= 14)

m.c3922 = Constraint(expr=   7*m.b202 + 7*m.b203 + m.x857 - m.x1061 <= 14)

m.c3923 = Constraint(expr=   7*m.b203 + 7*m.b204 + m.x858 - m.x1062 <= 14)

m.c3924 = Constraint(expr=   7*m.b204 + 7*m.b205 + m.x859 - m.x1063 <= 14)

m.c3925 = Constraint(expr= - m.x1065 + m.x1070 >= 0)

m.c3926 = Constraint(expr= - m.x1066 + m.x1071 >= 0)

m.c3927 = Constraint(expr= - m.x1067 + m.x1072 >= 0)

m.c3928 = Constraint(expr= - m.x1068 + m.x1073 >= 0)

m.c3929 = Constraint(expr= - m.x1069 + m.x1074 >= 0)

m.c3930 = Constraint(expr=   m.x1066 - m.x1070 >= 0)

m.c3931 = Constraint(expr=   m.x1067 - m.x1071 >= 0)

m.c3932 = Constraint(expr=   m.x1068 - m.x1072 >= 0)

m.c3933 = Constraint(expr=   m.x1069 - m.x1073 >= 0)

m.c3934 = Constraint(expr=   7*m.b1 - m.x655 + m.x1065 <= 7)

m.c3935 = Constraint(expr=   7*m.b2 - m.x656 + m.x1066 <= 7)

m.c3936 = Constraint(expr=   7*m.b3 - m.x657 + m.x1067 <= 7)

m.c3937 = Constraint(expr=   7*m.b4 - m.x658 + m.x1068 <= 7)

m.c3938 = Constraint(expr=   7*m.b5 - m.x659 + m.x1069 <= 7)

m.c3939 = Constraint(expr=   7*m.b6 - m.x660 + m.x1065 <= 7)

m.c3940 = Constraint(expr=   7*m.b7 - m.x661 + m.x1066 <= 7)

m.c3941 = Constraint(expr=   7*m.b8 - m.x662 + m.x1067 <= 7)

m.c3942 = Constraint(expr=   7*m.b9 - m.x663 + m.x1068 <= 7)

m.c3943 = Constraint(expr=   7*m.b10 - m.x664 + m.x1069 <= 7)

m.c3944 = Constraint(expr=   7*m.b11 - m.x665 + m.x1065 <= 7)

m.c3945 = Constraint(expr=   7*m.b12 - m.x666 + m.x1066 <= 7)

m.c3946 = Constraint(expr=   7*m.b13 - m.x667 + m.x1067 <= 7)

m.c3947 = Constraint(expr=   7*m.b14 - m.x668 + m.x1068 <= 7)

m.c3948 = Constraint(expr=   7*m.b15 - m.x669 + m.x1069 <= 7)

m.c3949 = Constraint(expr=   7*m.b16 - m.x670 + m.x1065 <= 7)

m.c3950 = Constraint(expr=   7*m.b17 - m.x671 + m.x1066 <= 7)

m.c3951 = Constraint(expr=   7*m.b18 - m.x672 + m.x1067 <= 7)

m.c3952 = Constraint(expr=   7*m.b19 - m.x673 + m.x1068 <= 7)

m.c3953 = Constraint(expr=   7*m.b20 - m.x674 + m.x1069 <= 7)

m.c3954 = Constraint(expr=   7*m.b21 - m.x675 + m.x1065 <= 7)

m.c3955 = Constraint(expr=   7*m.b22 - m.x676 + m.x1066 <= 7)

m.c3956 = Constraint(expr=   7*m.b23 - m.x677 + m.x1067 <= 7)

m.c3957 = Constraint(expr=   7*m.b24 - m.x678 + m.x1068 <= 7)

m.c3958 = Constraint(expr=   7*m.b25 - m.x679 + m.x1069 <= 7)

m.c3959 = Constraint(expr=   7*m.b26 - m.x680 + m.x1065 <= 7)

m.c3960 = Constraint(expr=   7*m.b27 - m.x681 + m.x1066 <= 7)

m.c3961 = Constraint(expr=   7*m.b28 - m.x682 + m.x1067 <= 7)

m.c3962 = Constraint(expr=   7*m.b29 - m.x683 + m.x1068 <= 7)

m.c3963 = Constraint(expr=   7*m.b30 - m.x684 + m.x1069 <= 7)

m.c3964 = Constraint(expr=   7*m.b31 - m.x685 + m.x1065 <= 7)

m.c3965 = Constraint(expr=   7*m.b32 - m.x686 + m.x1066 <= 7)

m.c3966 = Constraint(expr=   7*m.b33 - m.x687 + m.x1067 <= 7)

m.c3967 = Constraint(expr=   7*m.b34 - m.x688 + m.x1068 <= 7)

m.c3968 = Constraint(expr=   7*m.b35 - m.x689 + m.x1069 <= 7)

m.c3969 = Constraint(expr=   7*m.b36 - m.x690 + m.x1065 <= 7)

m.c3970 = Constraint(expr=   7*m.b37 - m.x691 + m.x1066 <= 7)

m.c3971 = Constraint(expr=   7*m.b38 - m.x692 + m.x1067 <= 7)

m.c3972 = Constraint(expr=   7*m.b39 - m.x693 + m.x1068 <= 7)

m.c3973 = Constraint(expr=   7*m.b40 - m.x694 + m.x1069 <= 7)

m.c3974 = Constraint(expr=   7*m.b41 - m.x695 + m.x1065 <= 7)

m.c3975 = Constraint(expr=   7*m.b42 - m.x696 + m.x1066 <= 7)

m.c3976 = Constraint(expr=   7*m.b43 - m.x697 + m.x1067 <= 7)

m.c3977 = Constraint(expr=   7*m.b44 - m.x698 + m.x1068 <= 7)

m.c3978 = Constraint(expr=   7*m.b45 - m.x699 + m.x1069 <= 7)

m.c3979 = Constraint(expr=   7*m.b46 - m.x700 + m.x1065 <= 7)

m.c3980 = Constraint(expr=   7*m.b47 - m.x701 + m.x1066 <= 7)

m.c3981 = Constraint(expr=   7*m.b48 - m.x702 + m.x1067 <= 7)

m.c3982 = Constraint(expr=   7*m.b49 - m.x703 + m.x1068 <= 7)

m.c3983 = Constraint(expr=   7*m.b50 - m.x704 + m.x1069 <= 7)

m.c3984 = Constraint(expr=   7*m.b51 - m.x705 + m.x1065 <= 7)

m.c3985 = Constraint(expr=   7*m.b52 - m.x706 + m.x1066 <= 7)

m.c3986 = Constraint(expr=   7*m.b53 - m.x707 + m.x1067 <= 7)

m.c3987 = Constraint(expr=   7*m.b54 - m.x708 + m.x1068 <= 7)

m.c3988 = Constraint(expr=   7*m.b55 - m.x709 + m.x1069 <= 7)

m.c3989 = Constraint(expr=   7*m.b56 - m.x710 + m.x1065 <= 7)

m.c3990 = Constraint(expr=   7*m.b57 - m.x711 + m.x1066 <= 7)

m.c3991 = Constraint(expr=   7*m.b58 - m.x712 + m.x1067 <= 7)

m.c3992 = Constraint(expr=   7*m.b59 - m.x713 + m.x1068 <= 7)

m.c3993 = Constraint(expr=   7*m.b60 - m.x714 + m.x1069 <= 7)

m.c3994 = Constraint(expr=   7*m.b61 - m.x715 + m.x1065 <= 7)

m.c3995 = Constraint(expr=   7*m.b62 - m.x716 + m.x1066 <= 7)

m.c3996 = Constraint(expr=   7*m.b63 - m.x717 + m.x1067 <= 7)

m.c3997 = Constraint(expr=   7*m.b64 - m.x718 + m.x1068 <= 7)

m.c3998 = Constraint(expr=   7*m.b65 - m.x719 + m.x1069 <= 7)

m.c3999 = Constraint(expr=   7*m.b66 - m.x720 + m.x1065 <= 7)

m.c4000 = Constraint(expr=   7*m.b67 - m.x721 + m.x1066 <= 7)

m.c4001 = Constraint(expr=   7*m.b68 - m.x722 + m.x1067 <= 7)

m.c4002 = Constraint(expr=   7*m.b69 - m.x723 + m.x1068 <= 7)

m.c4003 = Constraint(expr=   7*m.b70 - m.x724 + m.x1069 <= 7)

m.c4004 = Constraint(expr=   7*m.b71 - m.x725 + m.x1065 <= 7)

m.c4005 = Constraint(expr=   7*m.b72 - m.x726 + m.x1066 <= 7)

m.c4006 = Constraint(expr=   7*m.b73 - m.x727 + m.x1067 <= 7)

m.c4007 = Constraint(expr=   7*m.b74 - m.x728 + m.x1068 <= 7)

m.c4008 = Constraint(expr=   7*m.b75 - m.x729 + m.x1069 <= 7)

m.c4009 = Constraint(expr=   7*m.b76 - m.x730 + m.x1065 <= 7)

m.c4010 = Constraint(expr=   7*m.b77 - m.x731 + m.x1066 <= 7)

m.c4011 = Constraint(expr=   7*m.b78 - m.x732 + m.x1067 <= 7)

m.c4012 = Constraint(expr=   7*m.b79 - m.x733 + m.x1068 <= 7)

m.c4013 = Constraint(expr=   7*m.b80 - m.x734 + m.x1069 <= 7)

m.c4014 = Constraint(expr=   7*m.b81 - m.x735 + m.x1065 <= 7)

m.c4015 = Constraint(expr=   7*m.b82 - m.x736 + m.x1066 <= 7)

m.c4016 = Constraint(expr=   7*m.b83 - m.x737 + m.x1067 <= 7)

m.c4017 = Constraint(expr=   7*m.b84 - m.x738 + m.x1068 <= 7)

m.c4018 = Constraint(expr=   7*m.b85 - m.x739 + m.x1069 <= 7)

m.c4019 = Constraint(expr=   7*m.b86 - m.x740 + m.x1065 <= 7)

m.c4020 = Constraint(expr=   7*m.b87 - m.x741 + m.x1066 <= 7)

m.c4021 = Constraint(expr=   7*m.b88 - m.x742 + m.x1067 <= 7)

m.c4022 = Constraint(expr=   7*m.b89 - m.x743 + m.x1068 <= 7)

m.c4023 = Constraint(expr=   7*m.b90 - m.x744 + m.x1069 <= 7)

m.c4024 = Constraint(expr=   7*m.b91 - m.x745 + m.x1065 <= 7)

m.c4025 = Constraint(expr=   7*m.b92 - m.x746 + m.x1066 <= 7)

m.c4026 = Constraint(expr=   7*m.b93 - m.x747 + m.x1067 <= 7)

m.c4027 = Constraint(expr=   7*m.b94 - m.x748 + m.x1068 <= 7)

m.c4028 = Constraint(expr=   7*m.b95 - m.x749 + m.x1069 <= 7)

m.c4029 = Constraint(expr=   7*m.b96 - m.x750 + m.x1065 <= 7)

m.c4030 = Constraint(expr=   7*m.b97 - m.x751 + m.x1066 <= 7)

m.c4031 = Constraint(expr=   7*m.b98 - m.x752 + m.x1067 <= 7)

m.c4032 = Constraint(expr=   7*m.b99 - m.x753 + m.x1068 <= 7)

m.c4033 = Constraint(expr=   7*m.b100 - m.x754 + m.x1069 <= 7)

m.c4034 = Constraint(expr=   7*m.b101 - m.x755 + m.x1065 <= 7)

m.c4035 = Constraint(expr=   7*m.b102 - m.x756 + m.x1066 <= 7)

m.c4036 = Constraint(expr=   7*m.b103 - m.x757 + m.x1067 <= 7)

m.c4037 = Constraint(expr=   7*m.b104 - m.x758 + m.x1068 <= 7)

m.c4038 = Constraint(expr=   7*m.b105 - m.x759 + m.x1069 <= 7)

m.c4039 = Constraint(expr=   7*m.b106 - m.x760 + m.x1065 <= 7)

m.c4040 = Constraint(expr=   7*m.b107 - m.x761 + m.x1066 <= 7)

m.c4041 = Constraint(expr=   7*m.b108 - m.x762 + m.x1067 <= 7)

m.c4042 = Constraint(expr=   7*m.b109 - m.x763 + m.x1068 <= 7)

m.c4043 = Constraint(expr=   7*m.b110 - m.x764 + m.x1069 <= 7)

m.c4044 = Constraint(expr=   7*m.b111 - m.x765 + m.x1065 <= 7)

m.c4045 = Constraint(expr=   7*m.b112 - m.x766 + m.x1066 <= 7)

m.c4046 = Constraint(expr=   7*m.b113 - m.x767 + m.x1067 <= 7)

m.c4047 = Constraint(expr=   7*m.b114 - m.x768 + m.x1068 <= 7)

m.c4048 = Constraint(expr=   7*m.b115 - m.x769 + m.x1069 <= 7)

m.c4049 = Constraint(expr=   7*m.b116 - m.x770 + m.x1065 <= 7)

m.c4050 = Constraint(expr=   7*m.b117 - m.x771 + m.x1066 <= 7)

m.c4051 = Constraint(expr=   7*m.b118 - m.x772 + m.x1067 <= 7)

m.c4052 = Constraint(expr=   7*m.b119 - m.x773 + m.x1068 <= 7)

m.c4053 = Constraint(expr=   7*m.b120 - m.x774 + m.x1069 <= 7)

m.c4054 = Constraint(expr=   7*m.b121 - m.x775 + m.x1065 <= 7)

m.c4055 = Constraint(expr=   7*m.b122 - m.x776 + m.x1066 <= 7)

m.c4056 = Constraint(expr=   7*m.b123 - m.x777 + m.x1067 <= 7)

m.c4057 = Constraint(expr=   7*m.b124 - m.x778 + m.x1068 <= 7)

m.c4058 = Constraint(expr=   7*m.b125 - m.x779 + m.x1069 <= 7)

m.c4059 = Constraint(expr=   7*m.b126 - m.x780 + m.x1065 <= 7)

m.c4060 = Constraint(expr=   7*m.b127 - m.x781 + m.x1066 <= 7)

m.c4061 = Constraint(expr=   7*m.b128 - m.x782 + m.x1067 <= 7)

m.c4062 = Constraint(expr=   7*m.b129 - m.x783 + m.x1068 <= 7)

m.c4063 = Constraint(expr=   7*m.b130 - m.x784 + m.x1069 <= 7)

m.c4064 = Constraint(expr=   7*m.b131 - m.x785 + m.x1065 <= 7)

m.c4065 = Constraint(expr=   7*m.b132 - m.x786 + m.x1066 <= 7)

m.c4066 = Constraint(expr=   7*m.b133 - m.x787 + m.x1067 <= 7)

m.c4067 = Constraint(expr=   7*m.b134 - m.x788 + m.x1068 <= 7)

m.c4068 = Constraint(expr=   7*m.b135 - m.x789 + m.x1069 <= 7)

m.c4069 = Constraint(expr=   7*m.b136 - m.x790 + m.x1065 <= 7)

m.c4070 = Constraint(expr=   7*m.b137 - m.x791 + m.x1066 <= 7)

m.c4071 = Constraint(expr=   7*m.b138 - m.x792 + m.x1067 <= 7)

m.c4072 = Constraint(expr=   7*m.b139 - m.x793 + m.x1068 <= 7)

m.c4073 = Constraint(expr=   7*m.b140 - m.x794 + m.x1069 <= 7)

m.c4074 = Constraint(expr=   7*m.b141 - m.x795 + m.x1065 <= 7)

m.c4075 = Constraint(expr=   7*m.b142 - m.x796 + m.x1066 <= 7)

m.c4076 = Constraint(expr=   7*m.b143 - m.x797 + m.x1067 <= 7)

m.c4077 = Constraint(expr=   7*m.b144 - m.x798 + m.x1068 <= 7)

m.c4078 = Constraint(expr=   7*m.b145 - m.x799 + m.x1069 <= 7)

m.c4079 = Constraint(expr=   7*m.b146 - m.x800 + m.x1065 <= 7)

m.c4080 = Constraint(expr=   7*m.b147 - m.x801 + m.x1066 <= 7)

m.c4081 = Constraint(expr=   7*m.b148 - m.x802 + m.x1067 <= 7)

m.c4082 = Constraint(expr=   7*m.b149 - m.x803 + m.x1068 <= 7)

m.c4083 = Constraint(expr=   7*m.b150 - m.x804 + m.x1069 <= 7)

m.c4084 = Constraint(expr=   7*m.b151 - m.x805 + m.x1065 <= 7)

m.c4085 = Constraint(expr=   7*m.b152 - m.x806 + m.x1066 <= 7)

m.c4086 = Constraint(expr=   7*m.b153 - m.x807 + m.x1067 <= 7)

m.c4087 = Constraint(expr=   7*m.b154 - m.x808 + m.x1068 <= 7)

m.c4088 = Constraint(expr=   7*m.b155 - m.x809 + m.x1069 <= 7)

m.c4089 = Constraint(expr=   7*m.b156 - m.x810 + m.x1065 <= 7)

m.c4090 = Constraint(expr=   7*m.b157 - m.x811 + m.x1066 <= 7)

m.c4091 = Constraint(expr=   7*m.b158 - m.x812 + m.x1067 <= 7)

m.c4092 = Constraint(expr=   7*m.b159 - m.x813 + m.x1068 <= 7)

m.c4093 = Constraint(expr=   7*m.b160 - m.x814 + m.x1069 <= 7)

m.c4094 = Constraint(expr=   7*m.b161 - m.x815 + m.x1065 <= 7)

m.c4095 = Constraint(expr=   7*m.b162 - m.x816 + m.x1066 <= 7)

m.c4096 = Constraint(expr=   7*m.b163 - m.x817 + m.x1067 <= 7)

m.c4097 = Constraint(expr=   7*m.b164 - m.x818 + m.x1068 <= 7)

m.c4098 = Constraint(expr=   7*m.b165 - m.x819 + m.x1069 <= 7)

m.c4099 = Constraint(expr=   7*m.b166 - m.x820 + m.x1065 <= 7)

m.c4100 = Constraint(expr=   7*m.b167 - m.x821 + m.x1066 <= 7)

m.c4101 = Constraint(expr=   7*m.b168 - m.x822 + m.x1067 <= 7)

m.c4102 = Constraint(expr=   7*m.b169 - m.x823 + m.x1068 <= 7)

m.c4103 = Constraint(expr=   7*m.b170 - m.x824 + m.x1069 <= 7)

m.c4104 = Constraint(expr=   7*m.b171 - m.x825 + m.x1065 <= 7)

m.c4105 = Constraint(expr=   7*m.b172 - m.x826 + m.x1066 <= 7)

m.c4106 = Constraint(expr=   7*m.b173 - m.x827 + m.x1067 <= 7)

m.c4107 = Constraint(expr=   7*m.b174 - m.x828 + m.x1068 <= 7)

m.c4108 = Constraint(expr=   7*m.b175 - m.x829 + m.x1069 <= 7)

m.c4109 = Constraint(expr=   7*m.b176 - m.x830 + m.x1065 <= 7)

m.c4110 = Constraint(expr=   7*m.b177 - m.x831 + m.x1066 <= 7)

m.c4111 = Constraint(expr=   7*m.b178 - m.x832 + m.x1067 <= 7)

m.c4112 = Constraint(expr=   7*m.b179 - m.x833 + m.x1068 <= 7)

m.c4113 = Constraint(expr=   7*m.b180 - m.x834 + m.x1069 <= 7)

m.c4114 = Constraint(expr=   7*m.b181 - m.x835 + m.x1065 <= 7)

m.c4115 = Constraint(expr=   7*m.b182 - m.x836 + m.x1066 <= 7)

m.c4116 = Constraint(expr=   7*m.b183 - m.x837 + m.x1067 <= 7)

m.c4117 = Constraint(expr=   7*m.b184 - m.x838 + m.x1068 <= 7)

m.c4118 = Constraint(expr=   7*m.b185 - m.x839 + m.x1069 <= 7)

m.c4119 = Constraint(expr=   7*m.b186 - m.x840 + m.x1065 <= 7)

m.c4120 = Constraint(expr=   7*m.b187 - m.x841 + m.x1066 <= 7)

m.c4121 = Constraint(expr=   7*m.b188 - m.x842 + m.x1067 <= 7)

m.c4122 = Constraint(expr=   7*m.b189 - m.x843 + m.x1068 <= 7)

m.c4123 = Constraint(expr=   7*m.b190 - m.x844 + m.x1069 <= 7)

m.c4124 = Constraint(expr=   7*m.b191 - m.x845 + m.x1065 <= 7)

m.c4125 = Constraint(expr=   7*m.b192 - m.x846 + m.x1066 <= 7)

m.c4126 = Constraint(expr=   7*m.b193 - m.x847 + m.x1067 <= 7)

m.c4127 = Constraint(expr=   7*m.b194 - m.x848 + m.x1068 <= 7)

m.c4128 = Constraint(expr=   7*m.b195 - m.x849 + m.x1069 <= 7)

m.c4129 = Constraint(expr=   7*m.b196 - m.x850 + m.x1065 <= 7)

m.c4130 = Constraint(expr=   7*m.b197 - m.x851 + m.x1066 <= 7)

m.c4131 = Constraint(expr=   7*m.b198 - m.x852 + m.x1067 <= 7)

m.c4132 = Constraint(expr=   7*m.b199 - m.x853 + m.x1068 <= 7)

m.c4133 = Constraint(expr=   7*m.b200 - m.x854 + m.x1069 <= 7)

m.c4134 = Constraint(expr=   7*m.b201 - m.x855 + m.x1065 <= 7)

m.c4135 = Constraint(expr=   7*m.b202 - m.x856 + m.x1066 <= 7)

m.c4136 = Constraint(expr=   7*m.b203 - m.x857 + m.x1067 <= 7)

m.c4137 = Constraint(expr=   7*m.b204 - m.x858 + m.x1068 <= 7)

m.c4138 = Constraint(expr=   7*m.b205 - m.x859 + m.x1069 <= 7)

m.c4139 = Constraint(expr= - 7*m.b1 - m.x860 + m.x1070 >= -7)

m.c4140 = Constraint(expr= - 7*m.b2 - m.x861 + m.x1071 >= -7)

m.c4141 = Constraint(expr= - 7*m.b3 - m.x862 + m.x1072 >= -7)

m.c4142 = Constraint(expr= - 7*m.b4 - m.x863 + m.x1073 >= -7)

m.c4143 = Constraint(expr= - 7*m.b5 - m.x864 + m.x1074 >= -7)

m.c4144 = Constraint(expr= - 7*m.b6 - m.x865 + m.x1070 >= -7)

m.c4145 = Constraint(expr= - 7*m.b7 - m.x866 + m.x1071 >= -7)

m.c4146 = Constraint(expr= - 7*m.b8 - m.x867 + m.x1072 >= -7)

m.c4147 = Constraint(expr= - 7*m.b9 - m.x868 + m.x1073 >= -7)

m.c4148 = Constraint(expr= - 7*m.b10 - m.x869 + m.x1074 >= -7)

m.c4149 = Constraint(expr= - 7*m.b11 - m.x870 + m.x1070 >= -7)

m.c4150 = Constraint(expr= - 7*m.b12 - m.x871 + m.x1071 >= -7)

m.c4151 = Constraint(expr= - 7*m.b13 - m.x872 + m.x1072 >= -7)

m.c4152 = Constraint(expr= - 7*m.b14 - m.x873 + m.x1073 >= -7)

m.c4153 = Constraint(expr= - 7*m.b15 - m.x874 + m.x1074 >= -7)

m.c4154 = Constraint(expr= - 7*m.b16 - m.x875 + m.x1070 >= -7)

m.c4155 = Constraint(expr= - 7*m.b17 - m.x876 + m.x1071 >= -7)

m.c4156 = Constraint(expr= - 7*m.b18 - m.x877 + m.x1072 >= -7)

m.c4157 = Constraint(expr= - 7*m.b19 - m.x878 + m.x1073 >= -7)

m.c4158 = Constraint(expr= - 7*m.b20 - m.x879 + m.x1074 >= -7)

m.c4159 = Constraint(expr= - 7*m.b21 - m.x880 + m.x1070 >= -7)

m.c4160 = Constraint(expr= - 7*m.b22 - m.x881 + m.x1071 >= -7)

m.c4161 = Constraint(expr= - 7*m.b23 - m.x882 + m.x1072 >= -7)

m.c4162 = Constraint(expr= - 7*m.b24 - m.x883 + m.x1073 >= -7)

m.c4163 = Constraint(expr= - 7*m.b25 - m.x884 + m.x1074 >= -7)

m.c4164 = Constraint(expr= - 7*m.b26 - m.x885 + m.x1070 >= -7)

m.c4165 = Constraint(expr= - 7*m.b27 - m.x886 + m.x1071 >= -7)

m.c4166 = Constraint(expr= - 7*m.b28 - m.x887 + m.x1072 >= -7)

m.c4167 = Constraint(expr= - 7*m.b29 - m.x888 + m.x1073 >= -7)

m.c4168 = Constraint(expr= - 7*m.b30 - m.x889 + m.x1074 >= -7)

m.c4169 = Constraint(expr= - 7*m.b31 - m.x890 + m.x1070 >= -7)

m.c4170 = Constraint(expr= - 7*m.b32 - m.x891 + m.x1071 >= -7)

m.c4171 = Constraint(expr= - 7*m.b33 - m.x892 + m.x1072 >= -7)

m.c4172 = Constraint(expr= - 7*m.b34 - m.x893 + m.x1073 >= -7)

m.c4173 = Constraint(expr= - 7*m.b35 - m.x894 + m.x1074 >= -7)

m.c4174 = Constraint(expr= - 7*m.b36 - m.x895 + m.x1070 >= -7)

m.c4175 = Constraint(expr= - 7*m.b37 - m.x896 + m.x1071 >= -7)

m.c4176 = Constraint(expr= - 7*m.b38 - m.x897 + m.x1072 >= -7)

m.c4177 = Constraint(expr= - 7*m.b39 - m.x898 + m.x1073 >= -7)

m.c4178 = Constraint(expr= - 7*m.b40 - m.x899 + m.x1074 >= -7)

m.c4179 = Constraint(expr= - 7*m.b41 - m.x900 + m.x1070 >= -7)

m.c4180 = Constraint(expr= - 7*m.b42 - m.x901 + m.x1071 >= -7)

m.c4181 = Constraint(expr= - 7*m.b43 - m.x902 + m.x1072 >= -7)

m.c4182 = Constraint(expr= - 7*m.b44 - m.x903 + m.x1073 >= -7)

m.c4183 = Constraint(expr= - 7*m.b45 - m.x904 + m.x1074 >= -7)

m.c4184 = Constraint(expr= - 7*m.b46 - m.x905 + m.x1070 >= -7)

m.c4185 = Constraint(expr= - 7*m.b47 - m.x906 + m.x1071 >= -7)

m.c4186 = Constraint(expr= - 7*m.b48 - m.x907 + m.x1072 >= -7)

m.c4187 = Constraint(expr= - 7*m.b49 - m.x908 + m.x1073 >= -7)

m.c4188 = Constraint(expr= - 7*m.b50 - m.x909 + m.x1074 >= -7)

m.c4189 = Constraint(expr= - 7*m.b51 - m.x910 + m.x1070 >= -7)

m.c4190 = Constraint(expr= - 7*m.b52 - m.x911 + m.x1071 >= -7)

m.c4191 = Constraint(expr= - 7*m.b53 - m.x912 + m.x1072 >= -7)

m.c4192 = Constraint(expr= - 7*m.b54 - m.x913 + m.x1073 >= -7)

m.c4193 = Constraint(expr= - 7*m.b55 - m.x914 + m.x1074 >= -7)

m.c4194 = Constraint(expr= - 7*m.b56 - m.x915 + m.x1070 >= -7)

m.c4195 = Constraint(expr= - 7*m.b57 - m.x916 + m.x1071 >= -7)

m.c4196 = Constraint(expr= - 7*m.b58 - m.x917 + m.x1072 >= -7)

m.c4197 = Constraint(expr= - 7*m.b59 - m.x918 + m.x1073 >= -7)

m.c4198 = Constraint(expr= - 7*m.b60 - m.x919 + m.x1074 >= -7)

m.c4199 = Constraint(expr= - 7*m.b61 - m.x920 + m.x1070 >= -7)

m.c4200 = Constraint(expr= - 7*m.b62 - m.x921 + m.x1071 >= -7)

m.c4201 = Constraint(expr= - 7*m.b63 - m.x922 + m.x1072 >= -7)

m.c4202 = Constraint(expr= - 7*m.b64 - m.x923 + m.x1073 >= -7)

m.c4203 = Constraint(expr= - 7*m.b65 - m.x924 + m.x1074 >= -7)

m.c4204 = Constraint(expr= - 7*m.b66 - m.x925 + m.x1070 >= -7)

m.c4205 = Constraint(expr= - 7*m.b67 - m.x926 + m.x1071 >= -7)

m.c4206 = Constraint(expr= - 7*m.b68 - m.x927 + m.x1072 >= -7)

m.c4207 = Constraint(expr= - 7*m.b69 - m.x928 + m.x1073 >= -7)

m.c4208 = Constraint(expr= - 7*m.b70 - m.x929 + m.x1074 >= -7)

m.c4209 = Constraint(expr= - 7*m.b71 - m.x930 + m.x1070 >= -7)

m.c4210 = Constraint(expr= - 7*m.b72 - m.x931 + m.x1071 >= -7)

m.c4211 = Constraint(expr= - 7*m.b73 - m.x932 + m.x1072 >= -7)

m.c4212 = Constraint(expr= - 7*m.b74 - m.x933 + m.x1073 >= -7)

m.c4213 = Constraint(expr= - 7*m.b75 - m.x934 + m.x1074 >= -7)

m.c4214 = Constraint(expr= - 7*m.b76 - m.x935 + m.x1070 >= -7)

m.c4215 = Constraint(expr= - 7*m.b77 - m.x936 + m.x1071 >= -7)

m.c4216 = Constraint(expr= - 7*m.b78 - m.x937 + m.x1072 >= -7)

m.c4217 = Constraint(expr= - 7*m.b79 - m.x938 + m.x1073 >= -7)

m.c4218 = Constraint(expr= - 7*m.b80 - m.x939 + m.x1074 >= -7)

m.c4219 = Constraint(expr= - 7*m.b81 - m.x940 + m.x1070 >= -7)

m.c4220 = Constraint(expr= - 7*m.b82 - m.x941 + m.x1071 >= -7)

m.c4221 = Constraint(expr= - 7*m.b83 - m.x942 + m.x1072 >= -7)

m.c4222 = Constraint(expr= - 7*m.b84 - m.x943 + m.x1073 >= -7)

m.c4223 = Constraint(expr= - 7*m.b85 - m.x944 + m.x1074 >= -7)

m.c4224 = Constraint(expr= - 7*m.b86 - m.x945 + m.x1070 >= -7)

m.c4225 = Constraint(expr= - 7*m.b87 - m.x946 + m.x1071 >= -7)

m.c4226 = Constraint(expr= - 7*m.b88 - m.x947 + m.x1072 >= -7)

m.c4227 = Constraint(expr= - 7*m.b89 - m.x948 + m.x1073 >= -7)

m.c4228 = Constraint(expr= - 7*m.b90 - m.x949 + m.x1074 >= -7)

m.c4229 = Constraint(expr= - 7*m.b91 - m.x950 + m.x1070 >= -7)

m.c4230 = Constraint(expr= - 7*m.b92 - m.x951 + m.x1071 >= -7)

m.c4231 = Constraint(expr= - 7*m.b93 - m.x952 + m.x1072 >= -7)

m.c4232 = Constraint(expr= - 7*m.b94 - m.x953 + m.x1073 >= -7)

m.c4233 = Constraint(expr= - 7*m.b95 - m.x954 + m.x1074 >= -7)

m.c4234 = Constraint(expr= - 7*m.b96 - m.x955 + m.x1070 >= -7)

m.c4235 = Constraint(expr= - 7*m.b97 - m.x956 + m.x1071 >= -7)

m.c4236 = Constraint(expr= - 7*m.b98 - m.x957 + m.x1072 >= -7)

m.c4237 = Constraint(expr= - 7*m.b99 - m.x958 + m.x1073 >= -7)

m.c4238 = Constraint(expr= - 7*m.b100 - m.x959 + m.x1074 >= -7)

m.c4239 = Constraint(expr= - 7*m.b101 - m.x960 + m.x1070 >= -7)

m.c4240 = Constraint(expr= - 7*m.b102 - m.x961 + m.x1071 >= -7)

m.c4241 = Constraint(expr= - 7*m.b103 - m.x962 + m.x1072 >= -7)

m.c4242 = Constraint(expr= - 7*m.b104 - m.x963 + m.x1073 >= -7)

m.c4243 = Constraint(expr= - 7*m.b105 - m.x964 + m.x1074 >= -7)

m.c4244 = Constraint(expr= - 7*m.b106 - m.x965 + m.x1070 >= -7)

m.c4245 = Constraint(expr= - 7*m.b107 - m.x966 + m.x1071 >= -7)

m.c4246 = Constraint(expr= - 7*m.b108 - m.x967 + m.x1072 >= -7)

m.c4247 = Constraint(expr= - 7*m.b109 - m.x968 + m.x1073 >= -7)

m.c4248 = Constraint(expr= - 7*m.b110 - m.x969 + m.x1074 >= -7)

m.c4249 = Constraint(expr= - 7*m.b111 - m.x970 + m.x1070 >= -7)

m.c4250 = Constraint(expr= - 7*m.b112 - m.x971 + m.x1071 >= -7)

m.c4251 = Constraint(expr= - 7*m.b113 - m.x972 + m.x1072 >= -7)

m.c4252 = Constraint(expr= - 7*m.b114 - m.x973 + m.x1073 >= -7)

m.c4253 = Constraint(expr= - 7*m.b115 - m.x974 + m.x1074 >= -7)

m.c4254 = Constraint(expr= - 7*m.b116 - m.x975 + m.x1070 >= -7)

m.c4255 = Constraint(expr= - 7*m.b117 - m.x976 + m.x1071 >= -7)

m.c4256 = Constraint(expr= - 7*m.b118 - m.x977 + m.x1072 >= -7)

m.c4257 = Constraint(expr= - 7*m.b119 - m.x978 + m.x1073 >= -7)

m.c4258 = Constraint(expr= - 7*m.b120 - m.x979 + m.x1074 >= -7)

m.c4259 = Constraint(expr= - 7*m.b121 - m.x980 + m.x1070 >= -7)

m.c4260 = Constraint(expr= - 7*m.b122 - m.x981 + m.x1071 >= -7)

m.c4261 = Constraint(expr= - 7*m.b123 - m.x982 + m.x1072 >= -7)

m.c4262 = Constraint(expr= - 7*m.b124 - m.x983 + m.x1073 >= -7)

m.c4263 = Constraint(expr= - 7*m.b125 - m.x984 + m.x1074 >= -7)

m.c4264 = Constraint(expr= - 7*m.b126 - m.x985 + m.x1070 >= -7)

m.c4265 = Constraint(expr= - 7*m.b127 - m.x986 + m.x1071 >= -7)

m.c4266 = Constraint(expr= - 7*m.b128 - m.x987 + m.x1072 >= -7)

m.c4267 = Constraint(expr= - 7*m.b129 - m.x988 + m.x1073 >= -7)

m.c4268 = Constraint(expr= - 7*m.b130 - m.x989 + m.x1074 >= -7)

m.c4269 = Constraint(expr= - 7*m.b131 - m.x990 + m.x1070 >= -7)

m.c4270 = Constraint(expr= - 7*m.b132 - m.x991 + m.x1071 >= -7)

m.c4271 = Constraint(expr= - 7*m.b133 - m.x992 + m.x1072 >= -7)

m.c4272 = Constraint(expr= - 7*m.b134 - m.x993 + m.x1073 >= -7)

m.c4273 = Constraint(expr= - 7*m.b135 - m.x994 + m.x1074 >= -7)

m.c4274 = Constraint(expr= - 7*m.b136 - m.x995 + m.x1070 >= -7)

m.c4275 = Constraint(expr= - 7*m.b137 - m.x996 + m.x1071 >= -7)

m.c4276 = Constraint(expr= - 7*m.b138 - m.x997 + m.x1072 >= -7)

m.c4277 = Constraint(expr= - 7*m.b139 - m.x998 + m.x1073 >= -7)

m.c4278 = Constraint(expr= - 7*m.b140 - m.x999 + m.x1074 >= -7)

m.c4279 = Constraint(expr= - 7*m.b141 - m.x1000 + m.x1070 >= -7)

m.c4280 = Constraint(expr= - 7*m.b142 - m.x1001 + m.x1071 >= -7)

m.c4281 = Constraint(expr= - 7*m.b143 - m.x1002 + m.x1072 >= -7)

m.c4282 = Constraint(expr= - 7*m.b144 - m.x1003 + m.x1073 >= -7)

m.c4283 = Constraint(expr= - 7*m.b145 - m.x1004 + m.x1074 >= -7)

m.c4284 = Constraint(expr= - 7*m.b146 - m.x1005 + m.x1070 >= -7)

m.c4285 = Constraint(expr= - 7*m.b147 - m.x1006 + m.x1071 >= -7)

m.c4286 = Constraint(expr= - 7*m.b148 - m.x1007 + m.x1072 >= -7)

m.c4287 = Constraint(expr= - 7*m.b149 - m.x1008 + m.x1073 >= -7)

m.c4288 = Constraint(expr= - 7*m.b150 - m.x1009 + m.x1074 >= -7)

m.c4289 = Constraint(expr= - 7*m.b151 - m.x1010 + m.x1070 >= -7)

m.c4290 = Constraint(expr= - 7*m.b152 - m.x1011 + m.x1071 >= -7)

m.c4291 = Constraint(expr= - 7*m.b153 - m.x1012 + m.x1072 >= -7)

m.c4292 = Constraint(expr= - 7*m.b154 - m.x1013 + m.x1073 >= -7)

m.c4293 = Constraint(expr= - 7*m.b155 - m.x1014 + m.x1074 >= -7)

m.c4294 = Constraint(expr= - 7*m.b156 - m.x1015 + m.x1070 >= -7)

m.c4295 = Constraint(expr= - 7*m.b157 - m.x1016 + m.x1071 >= -7)

m.c4296 = Constraint(expr= - 7*m.b158 - m.x1017 + m.x1072 >= -7)

m.c4297 = Constraint(expr= - 7*m.b159 - m.x1018 + m.x1073 >= -7)

m.c4298 = Constraint(expr= - 7*m.b160 - m.x1019 + m.x1074 >= -7)

m.c4299 = Constraint(expr= - 7*m.b161 - m.x1020 + m.x1070 >= -7)

m.c4300 = Constraint(expr= - 7*m.b162 - m.x1021 + m.x1071 >= -7)

m.c4301 = Constraint(expr= - 7*m.b163 - m.x1022 + m.x1072 >= -7)

m.c4302 = Constraint(expr= - 7*m.b164 - m.x1023 + m.x1073 >= -7)

m.c4303 = Constraint(expr= - 7*m.b165 - m.x1024 + m.x1074 >= -7)

m.c4304 = Constraint(expr= - 7*m.b166 - m.x1025 + m.x1070 >= -7)

m.c4305 = Constraint(expr= - 7*m.b167 - m.x1026 + m.x1071 >= -7)

m.c4306 = Constraint(expr= - 7*m.b168 - m.x1027 + m.x1072 >= -7)

m.c4307 = Constraint(expr= - 7*m.b169 - m.x1028 + m.x1073 >= -7)

m.c4308 = Constraint(expr= - 7*m.b170 - m.x1029 + m.x1074 >= -7)

m.c4309 = Constraint(expr= - 7*m.b171 - m.x1030 + m.x1070 >= -7)

m.c4310 = Constraint(expr= - 7*m.b172 - m.x1031 + m.x1071 >= -7)

m.c4311 = Constraint(expr= - 7*m.b173 - m.x1032 + m.x1072 >= -7)

m.c4312 = Constraint(expr= - 7*m.b174 - m.x1033 + m.x1073 >= -7)

m.c4313 = Constraint(expr= - 7*m.b175 - m.x1034 + m.x1074 >= -7)

m.c4314 = Constraint(expr= - 7*m.b176 - m.x1035 + m.x1070 >= -7)

m.c4315 = Constraint(expr= - 7*m.b177 - m.x1036 + m.x1071 >= -7)

m.c4316 = Constraint(expr= - 7*m.b178 - m.x1037 + m.x1072 >= -7)

m.c4317 = Constraint(expr= - 7*m.b179 - m.x1038 + m.x1073 >= -7)

m.c4318 = Constraint(expr= - 7*m.b180 - m.x1039 + m.x1074 >= -7)

m.c4319 = Constraint(expr= - 7*m.b181 - m.x1040 + m.x1070 >= -7)

m.c4320 = Constraint(expr= - 7*m.b182 - m.x1041 + m.x1071 >= -7)

m.c4321 = Constraint(expr= - 7*m.b183 - m.x1042 + m.x1072 >= -7)

m.c4322 = Constraint(expr= - 7*m.b184 - m.x1043 + m.x1073 >= -7)

m.c4323 = Constraint(expr= - 7*m.b185 - m.x1044 + m.x1074 >= -7)

m.c4324 = Constraint(expr= - 7*m.b186 - m.x1045 + m.x1070 >= -7)

m.c4325 = Constraint(expr= - 7*m.b187 - m.x1046 + m.x1071 >= -7)

m.c4326 = Constraint(expr= - 7*m.b188 - m.x1047 + m.x1072 >= -7)

m.c4327 = Constraint(expr= - 7*m.b189 - m.x1048 + m.x1073 >= -7)

m.c4328 = Constraint(expr= - 7*m.b190 - m.x1049 + m.x1074 >= -7)

m.c4329 = Constraint(expr= - 7*m.b191 - m.x1050 + m.x1070 >= -7)

m.c4330 = Constraint(expr= - 7*m.b192 - m.x1051 + m.x1071 >= -7)

m.c4331 = Constraint(expr= - 7*m.b193 - m.x1052 + m.x1072 >= -7)

m.c4332 = Constraint(expr= - 7*m.b194 - m.x1053 + m.x1073 >= -7)

m.c4333 = Constraint(expr= - 7*m.b195 - m.x1054 + m.x1074 >= -7)

m.c4334 = Constraint(expr= - 7*m.b196 - m.x1055 + m.x1070 >= -7)

m.c4335 = Constraint(expr= - 7*m.b197 - m.x1056 + m.x1071 >= -7)

m.c4336 = Constraint(expr= - 7*m.b198 - m.x1057 + m.x1072 >= -7)

m.c4337 = Constraint(expr= - 7*m.b199 - m.x1058 + m.x1073 >= -7)

m.c4338 = Constraint(expr= - 7*m.b200 - m.x1059 + m.x1074 >= -7)

m.c4339 = Constraint(expr= - 7*m.b201 - m.x1060 + m.x1070 >= -7)

m.c4340 = Constraint(expr= - 7*m.b202 - m.x1061 + m.x1071 >= -7)

m.c4341 = Constraint(expr= - 7*m.b203 - m.x1062 + m.x1072 >= -7)

m.c4342 = Constraint(expr= - 7*m.b204 - m.x1063 + m.x1073 >= -7)

m.c4343 = Constraint(expr= - 7*m.b205 - m.x1064 + m.x1074 >= -7)

m.c4344 = Constraint(expr=   m.x1076 - m.x1110 >= 0)

m.c4345 = Constraint(expr=   m.x1077 - m.x1111 >= 0)

m.c4346 = Constraint(expr=   m.x1078 - m.x1112 >= 0)

m.c4347 = Constraint(expr=   m.x1079 - m.x1113 >= 0)

m.c4348 = Constraint(expr=   m.x1081 - m.x1115 >= 0)

m.c4349 = Constraint(expr=   m.x1082 - m.x1116 >= 0)

m.c4350 = Constraint(expr=   m.x1083 - m.x1117 >= 0)

m.c4351 = Constraint(expr=   m.x1084 - m.x1118 >= 0)

m.c4352 = Constraint(expr=   m.x1086 - m.x1120 >= 0)

m.c4353 = Constraint(expr=   m.x1087 - m.x1121 >= 0)

m.c4354 = Constraint(expr=   m.x1088 - m.x1122 >= 0)

m.c4355 = Constraint(expr=   m.x1089 - m.x1123 >= 0)

m.c4356 = Constraint(expr=   m.x1091 - m.x1125 >= 0)

m.c4357 = Constraint(expr=   m.x1092 - m.x1126 >= 0)

m.c4358 = Constraint(expr=   m.x1093 - m.x1127 >= 0)

m.c4359 = Constraint(expr=   m.x1094 - m.x1128 >= 0)

m.c4360 = Constraint(expr=   m.x1096 - m.x1130 >= 0)

m.c4361 = Constraint(expr=   m.x1097 - m.x1131 >= 0)

m.c4362 = Constraint(expr=   m.x1098 - m.x1132 >= 0)

m.c4363 = Constraint(expr=   m.x1099 - m.x1133 >= 0)

m.c4364 = Constraint(expr=   m.x1101 - m.x1135 >= 0)

m.c4365 = Constraint(expr=   m.x1102 - m.x1136 >= 0)

m.c4366 = Constraint(expr=   m.x1103 - m.x1137 >= 0)

m.c4367 = Constraint(expr=   m.x1104 - m.x1138 >= 0)

m.c4368 = Constraint(expr=   m.x1106 - m.x1140 >= 0)

m.c4369 = Constraint(expr=   m.x1107 - m.x1141 >= 0)

m.c4370 = Constraint(expr=   m.x1108 - m.x1142 >= 0)

m.c4371 = Constraint(expr=   m.x1109 - m.x1143 >= 0)

m.c4372 = Constraint(expr= - 7*m.b291 + m.x656 - m.x1110 >= -7)

m.c4373 = Constraint(expr= - 7*m.b292 + m.x657 - m.x1111 >= -7)

m.c4374 = Constraint(expr= - 7*m.b293 + m.x658 - m.x1112 >= -7)

m.c4375 = Constraint(expr= - 7*m.b294 + m.x659 - m.x1113 >= -7)

m.c4376 = Constraint(expr= - 7*m.b306 + m.x661 - m.x1125 >= -7)

m.c4377 = Constraint(expr= - 7*m.b307 + m.x662 - m.x1126 >= -7)

m.c4378 = Constraint(expr= - 7*m.b308 + m.x663 - m.x1127 >= -7)

m.c4379 = Constraint(expr= - 7*m.b309 + m.x664 - m.x1128 >= -7)

m.c4380 = Constraint(expr= - 7*m.b311 + m.x666 - m.x1130 >= -7)

m.c4381 = Constraint(expr= - 7*m.b312 + m.x667 - m.x1131 >= -7)

m.c4382 = Constraint(expr= - 7*m.b313 + m.x668 - m.x1132 >= -7)

m.c4383 = Constraint(expr= - 7*m.b314 + m.x669 - m.x1133 >= -7)

m.c4384 = Constraint(expr= - 7*m.b291 + m.x671 - m.x1110 >= -7)

m.c4385 = Constraint(expr= - 7*m.b292 + m.x672 - m.x1111 >= -7)

m.c4386 = Constraint(expr= - 7*m.b293 + m.x673 - m.x1112 >= -7)

m.c4387 = Constraint(expr= - 7*m.b294 + m.x674 - m.x1113 >= -7)

m.c4388 = Constraint(expr= - 7*m.b306 + m.x676 - m.x1125 >= -7)

m.c4389 = Constraint(expr= - 7*m.b307 + m.x677 - m.x1126 >= -7)

m.c4390 = Constraint(expr= - 7*m.b308 + m.x678 - m.x1127 >= -7)

m.c4391 = Constraint(expr= - 7*m.b309 + m.x679 - m.x1128 >= -7)

m.c4392 = Constraint(expr= - 7*m.b311 + m.x681 - m.x1130 >= -7)

m.c4393 = Constraint(expr= - 7*m.b312 + m.x682 - m.x1131 >= -7)

m.c4394 = Constraint(expr= - 7*m.b313 + m.x683 - m.x1132 >= -7)

m.c4395 = Constraint(expr= - 7*m.b314 + m.x684 - m.x1133 >= -7)

m.c4396 = Constraint(expr= - 7*m.b291 + m.x686 - m.x1110 >= -7)

m.c4397 = Constraint(expr= - 7*m.b292 + m.x687 - m.x1111 >= -7)

m.c4398 = Constraint(expr= - 7*m.b293 + m.x688 - m.x1112 >= -7)

m.c4399 = Constraint(expr= - 7*m.b294 + m.x689 - m.x1113 >= -7)

m.c4400 = Constraint(expr= - 7*m.b306 + m.x691 - m.x1125 >= -7)

m.c4401 = Constraint(expr= - 7*m.b307 + m.x692 - m.x1126 >= -7)

m.c4402 = Constraint(expr= - 7*m.b308 + m.x693 - m.x1127 >= -7)

m.c4403 = Constraint(expr= - 7*m.b309 + m.x694 - m.x1128 >= -7)

m.c4404 = Constraint(expr= - 7*m.b311 + m.x696 - m.x1130 >= -7)

m.c4405 = Constraint(expr= - 7*m.b312 + m.x697 - m.x1131 >= -7)

m.c4406 = Constraint(expr= - 7*m.b313 + m.x698 - m.x1132 >= -7)

m.c4407 = Constraint(expr= - 7*m.b314 + m.x699 - m.x1133 >= -7)

m.c4408 = Constraint(expr= - 7*m.b291 + m.x701 - m.x1110 >= -7)

m.c4409 = Constraint(expr= - 7*m.b292 + m.x702 - m.x1111 >= -7)

m.c4410 = Constraint(expr= - 7*m.b293 + m.x703 - m.x1112 >= -7)

m.c4411 = Constraint(expr= - 7*m.b294 + m.x704 - m.x1113 >= -7)

m.c4412 = Constraint(expr= - 7*m.b306 + m.x706 - m.x1125 >= -7)

m.c4413 = Constraint(expr= - 7*m.b307 + m.x707 - m.x1126 >= -7)

m.c4414 = Constraint(expr= - 7*m.b308 + m.x708 - m.x1127 >= -7)

m.c4415 = Constraint(expr= - 7*m.b309 + m.x709 - m.x1128 >= -7)

m.c4416 = Constraint(expr= - 7*m.b311 + m.x711 - m.x1130 >= -7)

m.c4417 = Constraint(expr= - 7*m.b312 + m.x712 - m.x1131 >= -7)

m.c4418 = Constraint(expr= - 7*m.b313 + m.x713 - m.x1132 >= -7)

m.c4419 = Constraint(expr= - 7*m.b314 + m.x714 - m.x1133 >= -7)

m.c4420 = Constraint(expr= - 7*m.b291 + m.x716 - m.x1110 >= -7)

m.c4421 = Constraint(expr= - 7*m.b292 + m.x717 - m.x1111 >= -7)

m.c4422 = Constraint(expr= - 7*m.b293 + m.x718 - m.x1112 >= -7)

m.c4423 = Constraint(expr= - 7*m.b294 + m.x719 - m.x1113 >= -7)

m.c4424 = Constraint(expr= - 7*m.b306 + m.x721 - m.x1125 >= -7)

m.c4425 = Constraint(expr= - 7*m.b307 + m.x722 - m.x1126 >= -7)

m.c4426 = Constraint(expr= - 7*m.b308 + m.x723 - m.x1127 >= -7)

m.c4427 = Constraint(expr= - 7*m.b309 + m.x724 - m.x1128 >= -7)

m.c4428 = Constraint(expr= - 7*m.b311 + m.x726 - m.x1130 >= -7)

m.c4429 = Constraint(expr= - 7*m.b312 + m.x727 - m.x1131 >= -7)

m.c4430 = Constraint(expr= - 7*m.b313 + m.x728 - m.x1132 >= -7)

m.c4431 = Constraint(expr= - 7*m.b314 + m.x729 - m.x1133 >= -7)

m.c4432 = Constraint(expr= - 7*m.b291 + m.x731 - m.x1110 >= -7)

m.c4433 = Constraint(expr= - 7*m.b292 + m.x732 - m.x1111 >= -7)

m.c4434 = Constraint(expr= - 7*m.b293 + m.x733 - m.x1112 >= -7)

m.c4435 = Constraint(expr= - 7*m.b294 + m.x734 - m.x1113 >= -7)

m.c4436 = Constraint(expr= - 7*m.b306 + m.x736 - m.x1125 >= -7)

m.c4437 = Constraint(expr= - 7*m.b307 + m.x737 - m.x1126 >= -7)

m.c4438 = Constraint(expr= - 7*m.b308 + m.x738 - m.x1127 >= -7)

m.c4439 = Constraint(expr= - 7*m.b309 + m.x739 - m.x1128 >= -7)

m.c4440 = Constraint(expr= - 7*m.b311 + m.x741 - m.x1130 >= -7)

m.c4441 = Constraint(expr= - 7*m.b312 + m.x742 - m.x1131 >= -7)

m.c4442 = Constraint(expr= - 7*m.b313 + m.x743 - m.x1132 >= -7)

m.c4443 = Constraint(expr= - 7*m.b314 + m.x744 - m.x1133 >= -7)

m.c4444 = Constraint(expr= - 7*m.b291 + m.x746 - m.x1110 >= -7)

m.c4445 = Constraint(expr= - 7*m.b292 + m.x747 - m.x1111 >= -7)

m.c4446 = Constraint(expr= - 7*m.b293 + m.x748 - m.x1112 >= -7)

m.c4447 = Constraint(expr= - 7*m.b294 + m.x749 - m.x1113 >= -7)

m.c4448 = Constraint(expr= - 7*m.b306 + m.x751 - m.x1125 >= -7)

m.c4449 = Constraint(expr= - 7*m.b307 + m.x752 - m.x1126 >= -7)

m.c4450 = Constraint(expr= - 7*m.b308 + m.x753 - m.x1127 >= -7)

m.c4451 = Constraint(expr= - 7*m.b309 + m.x754 - m.x1128 >= -7)

m.c4452 = Constraint(expr= - 7*m.b311 + m.x756 - m.x1130 >= -7)

m.c4453 = Constraint(expr= - 7*m.b312 + m.x757 - m.x1131 >= -7)

m.c4454 = Constraint(expr= - 7*m.b313 + m.x758 - m.x1132 >= -7)

m.c4455 = Constraint(expr= - 7*m.b314 + m.x759 - m.x1133 >= -7)

m.c4456 = Constraint(expr= - 7*m.b291 + m.x761 - m.x1110 >= -7)

m.c4457 = Constraint(expr= - 7*m.b292 + m.x762 - m.x1111 >= -7)

m.c4458 = Constraint(expr= - 7*m.b293 + m.x763 - m.x1112 >= -7)

m.c4459 = Constraint(expr= - 7*m.b294 + m.x764 - m.x1113 >= -7)

m.c4460 = Constraint(expr= - 7*m.b306 + m.x766 - m.x1125 >= -7)

m.c4461 = Constraint(expr= - 7*m.b307 + m.x767 - m.x1126 >= -7)

m.c4462 = Constraint(expr= - 7*m.b308 + m.x768 - m.x1127 >= -7)

m.c4463 = Constraint(expr= - 7*m.b309 + m.x769 - m.x1128 >= -7)

m.c4464 = Constraint(expr= - 7*m.b311 + m.x771 - m.x1130 >= -7)

m.c4465 = Constraint(expr= - 7*m.b312 + m.x772 - m.x1131 >= -7)

m.c4466 = Constraint(expr= - 7*m.b313 + m.x773 - m.x1132 >= -7)

m.c4467 = Constraint(expr= - 7*m.b314 + m.x774 - m.x1133 >= -7)

m.c4468 = Constraint(expr= - 7*m.b291 + m.x776 - m.x1110 >= -7)

m.c4469 = Constraint(expr= - 7*m.b292 + m.x777 - m.x1111 >= -7)

m.c4470 = Constraint(expr= - 7*m.b293 + m.x778 - m.x1112 >= -7)

m.c4471 = Constraint(expr= - 7*m.b294 + m.x779 - m.x1113 >= -7)

m.c4472 = Constraint(expr= - 7*m.b306 + m.x781 - m.x1125 >= -7)

m.c4473 = Constraint(expr= - 7*m.b307 + m.x782 - m.x1126 >= -7)

m.c4474 = Constraint(expr= - 7*m.b308 + m.x783 - m.x1127 >= -7)

m.c4475 = Constraint(expr= - 7*m.b309 + m.x784 - m.x1128 >= -7)

m.c4476 = Constraint(expr= - 7*m.b311 + m.x786 - m.x1130 >= -7)

m.c4477 = Constraint(expr= - 7*m.b312 + m.x787 - m.x1131 >= -7)

m.c4478 = Constraint(expr= - 7*m.b313 + m.x788 - m.x1132 >= -7)

m.c4479 = Constraint(expr= - 7*m.b314 + m.x789 - m.x1133 >= -7)

m.c4480 = Constraint(expr= - 7*m.b296 + m.x791 - m.x1115 >= -7)

m.c4481 = Constraint(expr= - 7*m.b297 + m.x792 - m.x1116 >= -7)

m.c4482 = Constraint(expr= - 7*m.b298 + m.x793 - m.x1117 >= -7)

m.c4483 = Constraint(expr= - 7*m.b299 + m.x794 - m.x1118 >= -7)

m.c4484 = Constraint(expr= - 7*m.b316 + m.x796 - m.x1135 >= -7)

m.c4485 = Constraint(expr= - 7*m.b317 + m.x797 - m.x1136 >= -7)

m.c4486 = Constraint(expr= - 7*m.b318 + m.x798 - m.x1137 >= -7)

m.c4487 = Constraint(expr= - 7*m.b319 + m.x799 - m.x1138 >= -7)

m.c4488 = Constraint(expr= - 7*m.b316 + m.x801 - m.x1135 >= -7)

m.c4489 = Constraint(expr= - 7*m.b317 + m.x802 - m.x1136 >= -7)

m.c4490 = Constraint(expr= - 7*m.b318 + m.x803 - m.x1137 >= -7)

m.c4491 = Constraint(expr= - 7*m.b319 + m.x804 - m.x1138 >= -7)

m.c4492 = Constraint(expr= - 7*m.b296 + m.x806 - m.x1115 >= -7)

m.c4493 = Constraint(expr= - 7*m.b297 + m.x807 - m.x1116 >= -7)

m.c4494 = Constraint(expr= - 7*m.b298 + m.x808 - m.x1117 >= -7)

m.c4495 = Constraint(expr= - 7*m.b299 + m.x809 - m.x1118 >= -7)

m.c4496 = Constraint(expr= - 7*m.b316 + m.x811 - m.x1135 >= -7)

m.c4497 = Constraint(expr= - 7*m.b317 + m.x812 - m.x1136 >= -7)

m.c4498 = Constraint(expr= - 7*m.b318 + m.x813 - m.x1137 >= -7)

m.c4499 = Constraint(expr= - 7*m.b319 + m.x814 - m.x1138 >= -7)

m.c4500 = Constraint(expr= - 7*m.b316 + m.x816 - m.x1135 >= -7)

m.c4501 = Constraint(expr= - 7*m.b317 + m.x817 - m.x1136 >= -7)

m.c4502 = Constraint(expr= - 7*m.b318 + m.x818 - m.x1137 >= -7)

m.c4503 = Constraint(expr= - 7*m.b319 + m.x819 - m.x1138 >= -7)

m.c4504 = Constraint(expr= - 7*m.b291 + m.x821 - m.x1110 >= -7)

m.c4505 = Constraint(expr= - 7*m.b292 + m.x822 - m.x1111 >= -7)

m.c4506 = Constraint(expr= - 7*m.b293 + m.x823 - m.x1112 >= -7)

m.c4507 = Constraint(expr= - 7*m.b294 + m.x824 - m.x1113 >= -7)

m.c4508 = Constraint(expr= - 7*m.b306 + m.x826 - m.x1125 >= -7)

m.c4509 = Constraint(expr= - 7*m.b307 + m.x827 - m.x1126 >= -7)

m.c4510 = Constraint(expr= - 7*m.b308 + m.x828 - m.x1127 >= -7)

m.c4511 = Constraint(expr= - 7*m.b309 + m.x829 - m.x1128 >= -7)

m.c4512 = Constraint(expr= - 7*m.b311 + m.x831 - m.x1130 >= -7)

m.c4513 = Constraint(expr= - 7*m.b312 + m.x832 - m.x1131 >= -7)

m.c4514 = Constraint(expr= - 7*m.b313 + m.x833 - m.x1132 >= -7)

m.c4515 = Constraint(expr= - 7*m.b314 + m.x834 - m.x1133 >= -7)

m.c4516 = Constraint(expr= - 7*m.b291 + m.x836 - m.x1110 >= -7)

m.c4517 = Constraint(expr= - 7*m.b292 + m.x837 - m.x1111 >= -7)

m.c4518 = Constraint(expr= - 7*m.b293 + m.x838 - m.x1112 >= -7)

m.c4519 = Constraint(expr= - 7*m.b294 + m.x839 - m.x1113 >= -7)

m.c4520 = Constraint(expr= - 7*m.b306 + m.x841 - m.x1125 >= -7)

m.c4521 = Constraint(expr= - 7*m.b307 + m.x842 - m.x1126 >= -7)

m.c4522 = Constraint(expr= - 7*m.b308 + m.x843 - m.x1127 >= -7)

m.c4523 = Constraint(expr= - 7*m.b309 + m.x844 - m.x1128 >= -7)

m.c4524 = Constraint(expr= - 7*m.b311 + m.x846 - m.x1130 >= -7)

m.c4525 = Constraint(expr= - 7*m.b312 + m.x847 - m.x1131 >= -7)

m.c4526 = Constraint(expr= - 7*m.b313 + m.x848 - m.x1132 >= -7)

m.c4527 = Constraint(expr= - 7*m.b314 + m.x849 - m.x1133 >= -7)

m.c4528 = Constraint(expr= - 7*m.b316 + m.x851 - m.x1135 >= -7)

m.c4529 = Constraint(expr= - 7*m.b317 + m.x852 - m.x1136 >= -7)

m.c4530 = Constraint(expr= - 7*m.b318 + m.x853 - m.x1137 >= -7)

m.c4531 = Constraint(expr= - 7*m.b319 + m.x854 - m.x1138 >= -7)

m.c4532 = Constraint(expr= - 7*m.b316 + m.x856 - m.x1135 >= -7)

m.c4533 = Constraint(expr= - 7*m.b317 + m.x857 - m.x1136 >= -7)

m.c4534 = Constraint(expr= - 7*m.b318 + m.x858 - m.x1137 >= -7)

m.c4535 = Constraint(expr= - 7*m.b319 + m.x859 - m.x1138 >= -7)

m.c4536 = Constraint(expr= - 7*m.b1 - m.x860 + m.x1076 >= -7)

m.c4537 = Constraint(expr= - 7*m.b2 - m.x861 + m.x1077 >= -7)

m.c4538 = Constraint(expr= - 7*m.b3 - m.x862 + m.x1078 >= -7)

m.c4539 = Constraint(expr= - 7*m.b4 - m.x863 + m.x1079 >= -7)

m.c4540 = Constraint(expr= - 7*m.b6 - m.x865 + m.x1091 >= -7)

m.c4541 = Constraint(expr= - 7*m.b7 - m.x866 + m.x1092 >= -7)

m.c4542 = Constraint(expr= - 7*m.b8 - m.x867 + m.x1093 >= -7)

m.c4543 = Constraint(expr= - 7*m.b9 - m.x868 + m.x1094 >= -7)

m.c4544 = Constraint(expr= - 7*m.b11 - m.x870 + m.x1096 >= -7)

m.c4545 = Constraint(expr= - 7*m.b12 - m.x871 + m.x1097 >= -7)

m.c4546 = Constraint(expr= - 7*m.b13 - m.x872 + m.x1098 >= -7)

m.c4547 = Constraint(expr= - 7*m.b14 - m.x873 + m.x1099 >= -7)

m.c4548 = Constraint(expr= - 7*m.b16 - m.x875 + m.x1076 >= -7)

m.c4549 = Constraint(expr= - 7*m.b17 - m.x876 + m.x1077 >= -7)

m.c4550 = Constraint(expr= - 7*m.b18 - m.x877 + m.x1078 >= -7)

m.c4551 = Constraint(expr= - 7*m.b19 - m.x878 + m.x1079 >= -7)

m.c4552 = Constraint(expr= - 7*m.b21 - m.x880 + m.x1091 >= -7)

m.c4553 = Constraint(expr= - 7*m.b22 - m.x881 + m.x1092 >= -7)

m.c4554 = Constraint(expr= - 7*m.b23 - m.x882 + m.x1093 >= -7)

m.c4555 = Constraint(expr= - 7*m.b24 - m.x883 + m.x1094 >= -7)

m.c4556 = Constraint(expr= - 7*m.b26 - m.x885 + m.x1096 >= -7)

m.c4557 = Constraint(expr= - 7*m.b27 - m.x886 + m.x1097 >= -7)

m.c4558 = Constraint(expr= - 7*m.b28 - m.x887 + m.x1098 >= -7)

m.c4559 = Constraint(expr= - 7*m.b29 - m.x888 + m.x1099 >= -7)

m.c4560 = Constraint(expr= - 7*m.b31 - m.x890 + m.x1076 >= -7)

m.c4561 = Constraint(expr= - 7*m.b32 - m.x891 + m.x1077 >= -7)

m.c4562 = Constraint(expr= - 7*m.b33 - m.x892 + m.x1078 >= -7)

m.c4563 = Constraint(expr= - 7*m.b34 - m.x893 + m.x1079 >= -7)

m.c4564 = Constraint(expr= - 7*m.b36 - m.x895 + m.x1091 >= -7)

m.c4565 = Constraint(expr= - 7*m.b37 - m.x896 + m.x1092 >= -7)

m.c4566 = Constraint(expr= - 7*m.b38 - m.x897 + m.x1093 >= -7)

m.c4567 = Constraint(expr= - 7*m.b39 - m.x898 + m.x1094 >= -7)

m.c4568 = Constraint(expr= - 7*m.b41 - m.x900 + m.x1096 >= -7)

m.c4569 = Constraint(expr= - 7*m.b42 - m.x901 + m.x1097 >= -7)

m.c4570 = Constraint(expr= - 7*m.b43 - m.x902 + m.x1098 >= -7)

m.c4571 = Constraint(expr= - 7*m.b44 - m.x903 + m.x1099 >= -7)

m.c4572 = Constraint(expr= - 7*m.b46 - m.x905 + m.x1076 >= -7)

m.c4573 = Constraint(expr= - 7*m.b47 - m.x906 + m.x1077 >= -7)

m.c4574 = Constraint(expr= - 7*m.b48 - m.x907 + m.x1078 >= -7)

m.c4575 = Constraint(expr= - 7*m.b49 - m.x908 + m.x1079 >= -7)

m.c4576 = Constraint(expr= - 7*m.b51 - m.x910 + m.x1091 >= -7)

m.c4577 = Constraint(expr= - 7*m.b52 - m.x911 + m.x1092 >= -7)

m.c4578 = Constraint(expr= - 7*m.b53 - m.x912 + m.x1093 >= -7)

m.c4579 = Constraint(expr= - 7*m.b54 - m.x913 + m.x1094 >= -7)

m.c4580 = Constraint(expr= - 7*m.b56 - m.x915 + m.x1096 >= -7)

m.c4581 = Constraint(expr= - 7*m.b57 - m.x916 + m.x1097 >= -7)

m.c4582 = Constraint(expr= - 7*m.b58 - m.x917 + m.x1098 >= -7)

m.c4583 = Constraint(expr= - 7*m.b59 - m.x918 + m.x1099 >= -7)

m.c4584 = Constraint(expr= - 7*m.b61 - m.x920 + m.x1076 >= -7)

m.c4585 = Constraint(expr= - 7*m.b62 - m.x921 + m.x1077 >= -7)

m.c4586 = Constraint(expr= - 7*m.b63 - m.x922 + m.x1078 >= -7)

m.c4587 = Constraint(expr= - 7*m.b64 - m.x923 + m.x1079 >= -7)

m.c4588 = Constraint(expr= - 7*m.b66 - m.x925 + m.x1091 >= -7)

m.c4589 = Constraint(expr= - 7*m.b67 - m.x926 + m.x1092 >= -7)

m.c4590 = Constraint(expr= - 7*m.b68 - m.x927 + m.x1093 >= -7)

m.c4591 = Constraint(expr= - 7*m.b69 - m.x928 + m.x1094 >= -7)

m.c4592 = Constraint(expr= - 7*m.b71 - m.x930 + m.x1096 >= -7)

m.c4593 = Constraint(expr= - 7*m.b72 - m.x931 + m.x1097 >= -7)

m.c4594 = Constraint(expr= - 7*m.b73 - m.x932 + m.x1098 >= -7)

m.c4595 = Constraint(expr= - 7*m.b74 - m.x933 + m.x1099 >= -7)

m.c4596 = Constraint(expr= - 7*m.b76 - m.x935 + m.x1076 >= -7)

m.c4597 = Constraint(expr= - 7*m.b77 - m.x936 + m.x1077 >= -7)

m.c4598 = Constraint(expr= - 7*m.b78 - m.x937 + m.x1078 >= -7)

m.c4599 = Constraint(expr= - 7*m.b79 - m.x938 + m.x1079 >= -7)

m.c4600 = Constraint(expr= - 7*m.b81 - m.x940 + m.x1091 >= -7)

m.c4601 = Constraint(expr= - 7*m.b82 - m.x941 + m.x1092 >= -7)

m.c4602 = Constraint(expr= - 7*m.b83 - m.x942 + m.x1093 >= -7)

m.c4603 = Constraint(expr= - 7*m.b84 - m.x943 + m.x1094 >= -7)

m.c4604 = Constraint(expr= - 7*m.b86 - m.x945 + m.x1096 >= -7)

m.c4605 = Constraint(expr= - 7*m.b87 - m.x946 + m.x1097 >= -7)

m.c4606 = Constraint(expr= - 7*m.b88 - m.x947 + m.x1098 >= -7)

m.c4607 = Constraint(expr= - 7*m.b89 - m.x948 + m.x1099 >= -7)

m.c4608 = Constraint(expr= - 7*m.b91 - m.x950 + m.x1076 >= -7)

m.c4609 = Constraint(expr= - 7*m.b92 - m.x951 + m.x1077 >= -7)

m.c4610 = Constraint(expr= - 7*m.b93 - m.x952 + m.x1078 >= -7)

m.c4611 = Constraint(expr= - 7*m.b94 - m.x953 + m.x1079 >= -7)

m.c4612 = Constraint(expr= - 7*m.b96 - m.x955 + m.x1091 >= -7)

m.c4613 = Constraint(expr= - 7*m.b97 - m.x956 + m.x1092 >= -7)

m.c4614 = Constraint(expr= - 7*m.b98 - m.x957 + m.x1093 >= -7)

m.c4615 = Constraint(expr= - 7*m.b99 - m.x958 + m.x1094 >= -7)

m.c4616 = Constraint(expr= - 7*m.b101 - m.x960 + m.x1096 >= -7)

m.c4617 = Constraint(expr= - 7*m.b102 - m.x961 + m.x1097 >= -7)

m.c4618 = Constraint(expr= - 7*m.b103 - m.x962 + m.x1098 >= -7)

m.c4619 = Constraint(expr= - 7*m.b104 - m.x963 + m.x1099 >= -7)

m.c4620 = Constraint(expr= - 7*m.b106 - m.x965 + m.x1076 >= -7)

m.c4621 = Constraint(expr= - 7*m.b107 - m.x966 + m.x1077 >= -7)

m.c4622 = Constraint(expr= - 7*m.b108 - m.x967 + m.x1078 >= -7)

m.c4623 = Constraint(expr= - 7*m.b109 - m.x968 + m.x1079 >= -7)

m.c4624 = Constraint(expr= - 7*m.b111 - m.x970 + m.x1091 >= -7)

m.c4625 = Constraint(expr= - 7*m.b112 - m.x971 + m.x1092 >= -7)

m.c4626 = Constraint(expr= - 7*m.b113 - m.x972 + m.x1093 >= -7)

m.c4627 = Constraint(expr= - 7*m.b114 - m.x973 + m.x1094 >= -7)

m.c4628 = Constraint(expr= - 7*m.b116 - m.x975 + m.x1096 >= -7)

m.c4629 = Constraint(expr= - 7*m.b117 - m.x976 + m.x1097 >= -7)

m.c4630 = Constraint(expr= - 7*m.b118 - m.x977 + m.x1098 >= -7)

m.c4631 = Constraint(expr= - 7*m.b119 - m.x978 + m.x1099 >= -7)

m.c4632 = Constraint(expr= - 7*m.b121 - m.x980 + m.x1076 >= -7)

m.c4633 = Constraint(expr= - 7*m.b122 - m.x981 + m.x1077 >= -7)

m.c4634 = Constraint(expr= - 7*m.b123 - m.x982 + m.x1078 >= -7)

m.c4635 = Constraint(expr= - 7*m.b124 - m.x983 + m.x1079 >= -7)

m.c4636 = Constraint(expr= - 7*m.b126 - m.x985 + m.x1091 >= -7)

m.c4637 = Constraint(expr= - 7*m.b127 - m.x986 + m.x1092 >= -7)

m.c4638 = Constraint(expr= - 7*m.b128 - m.x987 + m.x1093 >= -7)

m.c4639 = Constraint(expr= - 7*m.b129 - m.x988 + m.x1094 >= -7)

m.c4640 = Constraint(expr= - 7*m.b131 - m.x990 + m.x1096 >= -7)

m.c4641 = Constraint(expr= - 7*m.b132 - m.x991 + m.x1097 >= -7)

m.c4642 = Constraint(expr= - 7*m.b133 - m.x992 + m.x1098 >= -7)

m.c4643 = Constraint(expr= - 7*m.b134 - m.x993 + m.x1099 >= -7)

m.c4644 = Constraint(expr= - 7*m.b136 - m.x995 + m.x1081 >= -7)

m.c4645 = Constraint(expr= - 7*m.b137 - m.x996 + m.x1082 >= -7)

m.c4646 = Constraint(expr= - 7*m.b138 - m.x997 + m.x1083 >= -7)

m.c4647 = Constraint(expr= - 7*m.b139 - m.x998 + m.x1084 >= -7)

m.c4648 = Constraint(expr= - 7*m.b141 - m.x1000 + m.x1101 >= -7)

m.c4649 = Constraint(expr= - 7*m.b142 - m.x1001 + m.x1102 >= -7)

m.c4650 = Constraint(expr= - 7*m.b143 - m.x1002 + m.x1103 >= -7)

m.c4651 = Constraint(expr= - 7*m.b144 - m.x1003 + m.x1104 >= -7)

m.c4652 = Constraint(expr= - 7*m.b146 - m.x1005 + m.x1101 >= -7)

m.c4653 = Constraint(expr= - 7*m.b147 - m.x1006 + m.x1102 >= -7)

m.c4654 = Constraint(expr= - 7*m.b148 - m.x1007 + m.x1103 >= -7)

m.c4655 = Constraint(expr= - 7*m.b149 - m.x1008 + m.x1104 >= -7)

m.c4656 = Constraint(expr= - 7*m.b151 - m.x1010 + m.x1081 >= -7)

m.c4657 = Constraint(expr= - 7*m.b152 - m.x1011 + m.x1082 >= -7)

m.c4658 = Constraint(expr= - 7*m.b153 - m.x1012 + m.x1083 >= -7)

m.c4659 = Constraint(expr= - 7*m.b154 - m.x1013 + m.x1084 >= -7)

m.c4660 = Constraint(expr= - 7*m.b156 - m.x1015 + m.x1101 >= -7)

m.c4661 = Constraint(expr= - 7*m.b157 - m.x1016 + m.x1102 >= -7)

m.c4662 = Constraint(expr= - 7*m.b158 - m.x1017 + m.x1103 >= -7)

m.c4663 = Constraint(expr= - 7*m.b159 - m.x1018 + m.x1104 >= -7)

m.c4664 = Constraint(expr= - 7*m.b161 - m.x1020 + m.x1101 >= -7)

m.c4665 = Constraint(expr= - 7*m.b162 - m.x1021 + m.x1102 >= -7)

m.c4666 = Constraint(expr= - 7*m.b163 - m.x1022 + m.x1103 >= -7)

m.c4667 = Constraint(expr= - 7*m.b164 - m.x1023 + m.x1104 >= -7)

m.c4668 = Constraint(expr= - 7*m.b166 - m.x1025 + m.x1076 >= -7)

m.c4669 = Constraint(expr= - 7*m.b167 - m.x1026 + m.x1077 >= -7)

m.c4670 = Constraint(expr= - 7*m.b168 - m.x1027 + m.x1078 >= -7)

m.c4671 = Constraint(expr= - 7*m.b169 - m.x1028 + m.x1079 >= -7)

m.c4672 = Constraint(expr= - 7*m.b171 - m.x1030 + m.x1091 >= -7)

m.c4673 = Constraint(expr= - 7*m.b172 - m.x1031 + m.x1092 >= -7)

m.c4674 = Constraint(expr= - 7*m.b173 - m.x1032 + m.x1093 >= -7)

m.c4675 = Constraint(expr= - 7*m.b174 - m.x1033 + m.x1094 >= -7)

m.c4676 = Constraint(expr= - 7*m.b176 - m.x1035 + m.x1096 >= -7)

m.c4677 = Constraint(expr= - 7*m.b177 - m.x1036 + m.x1097 >= -7)

m.c4678 = Constraint(expr= - 7*m.b178 - m.x1037 + m.x1098 >= -7)

m.c4679 = Constraint(expr= - 7*m.b179 - m.x1038 + m.x1099 >= -7)

m.c4680 = Constraint(expr= - 7*m.b181 - m.x1040 + m.x1076 >= -7)

m.c4681 = Constraint(expr= - 7*m.b182 - m.x1041 + m.x1077 >= -7)

m.c4682 = Constraint(expr= - 7*m.b183 - m.x1042 + m.x1078 >= -7)

m.c4683 = Constraint(expr= - 7*m.b184 - m.x1043 + m.x1079 >= -7)

m.c4684 = Constraint(expr= - 7*m.b186 - m.x1045 + m.x1091 >= -7)

m.c4685 = Constraint(expr= - 7*m.b187 - m.x1046 + m.x1092 >= -7)

m.c4686 = Constraint(expr= - 7*m.b188 - m.x1047 + m.x1093 >= -7)

m.c4687 = Constraint(expr= - 7*m.b189 - m.x1048 + m.x1094 >= -7)

m.c4688 = Constraint(expr= - 7*m.b191 - m.x1050 + m.x1096 >= -7)

m.c4689 = Constraint(expr= - 7*m.b192 - m.x1051 + m.x1097 >= -7)

m.c4690 = Constraint(expr= - 7*m.b193 - m.x1052 + m.x1098 >= -7)

m.c4691 = Constraint(expr= - 7*m.b194 - m.x1053 + m.x1099 >= -7)

m.c4692 = Constraint(expr= - 7*m.b196 - m.x1055 + m.x1101 >= -7)

m.c4693 = Constraint(expr= - 7*m.b197 - m.x1056 + m.x1102 >= -7)

m.c4694 = Constraint(expr= - 7*m.b198 - m.x1057 + m.x1103 >= -7)

m.c4695 = Constraint(expr= - 7*m.b199 - m.x1058 + m.x1104 >= -7)

m.c4696 = Constraint(expr= - 7*m.b201 - m.x1060 + m.x1101 >= -7)

m.c4697 = Constraint(expr= - 7*m.b202 - m.x1061 + m.x1102 >= -7)

m.c4698 = Constraint(expr= - 7*m.b203 - m.x1062 + m.x1103 >= -7)

m.c4699 = Constraint(expr= - 7*m.b204 - m.x1063 + m.x1104 >= -7)

m.c4700 = Constraint(expr=   m.x1146 - m.x1155 >= 0)

m.c4701 = Constraint(expr=   m.x1147 - m.x1156 >= 0)

m.c4702 = Constraint(expr=   m.x1148 - m.x1157 >= 0)

m.c4703 = Constraint(expr=   m.x1149 - m.x1158 >= 0)

m.c4704 = Constraint(expr=   m.x1151 - m.x1160 >= 0)

m.c4705 = Constraint(expr=   m.x1152 - m.x1161 >= 0)

m.c4706 = Constraint(expr=   m.x1153 - m.x1162 >= 0)

m.c4707 = Constraint(expr=   m.x1154 - m.x1163 >= 0)

m.c4708 = Constraint(expr= - 7*m.b291 - m.x1075 + m.x1145 >= -7)

m.c4709 = Constraint(expr= - 7*m.b292 - m.x1076 + m.x1146 >= -7)

m.c4710 = Constraint(expr= - 7*m.b293 - m.x1077 + m.x1147 >= -7)

m.c4711 = Constraint(expr= - 7*m.b294 - m.x1078 + m.x1148 >= -7)

m.c4712 = Constraint(expr= - 7*m.b295 - m.x1079 + m.x1149 >= -7)

m.c4713 = Constraint(expr= - 7*m.b296 - m.x1080 + m.x1150 >= -7)

m.c4714 = Constraint(expr= - 7*m.b297 - m.x1081 + m.x1151 >= -7)

m.c4715 = Constraint(expr= - 7*m.b298 - m.x1082 + m.x1152 >= -7)

m.c4716 = Constraint(expr= - 7*m.b299 - m.x1083 + m.x1153 >= -7)

m.c4717 = Constraint(expr= - 7*m.b300 - m.x1084 + m.x1154 >= -7)

m.c4718 = Constraint(expr= - 7*m.b301 - m.x1085 + m.x1145 >= -7)

m.c4719 = Constraint(expr= - 7*m.b302 - m.x1086 + m.x1146 >= -7)

m.c4720 = Constraint(expr= - 7*m.b303 - m.x1087 + m.x1147 >= -7)

m.c4721 = Constraint(expr= - 7*m.b304 - m.x1088 + m.x1148 >= -7)

m.c4722 = Constraint(expr= - 7*m.b305 - m.x1089 + m.x1149 >= -7)

m.c4723 = Constraint(expr= - 7*m.b306 - m.x1090 + m.x1145 >= -7)

m.c4724 = Constraint(expr= - 7*m.b307 - m.x1091 + m.x1146 >= -7)

m.c4725 = Constraint(expr= - 7*m.b308 - m.x1092 + m.x1147 >= -7)

m.c4726 = Constraint(expr= - 7*m.b309 - m.x1093 + m.x1148 >= -7)

m.c4727 = Constraint(expr= - 7*m.b310 - m.x1094 + m.x1149 >= -7)

m.c4728 = Constraint(expr= - 7*m.b311 - m.x1095 + m.x1145 >= -7)

m.c4729 = Constraint(expr= - 7*m.b312 - m.x1096 + m.x1146 >= -7)

m.c4730 = Constraint(expr= - 7*m.b313 - m.x1097 + m.x1147 >= -7)

m.c4731 = Constraint(expr= - 7*m.b314 - m.x1098 + m.x1148 >= -7)

m.c4732 = Constraint(expr= - 7*m.b315 - m.x1099 + m.x1149 >= -7)

m.c4733 = Constraint(expr= - 7*m.b316 - m.x1100 + m.x1150 >= -7)

m.c4734 = Constraint(expr= - 7*m.b317 - m.x1101 + m.x1151 >= -7)

m.c4735 = Constraint(expr= - 7*m.b318 - m.x1102 + m.x1152 >= -7)

m.c4736 = Constraint(expr= - 7*m.b319 - m.x1103 + m.x1153 >= -7)

m.c4737 = Constraint(expr= - 7*m.b320 - m.x1104 + m.x1154 >= -7)

m.c4738 = Constraint(expr= - 7*m.b321 - m.x1105 + m.x1145 >= -7)

m.c4739 = Constraint(expr= - 7*m.b322 - m.x1106 + m.x1146 >= -7)

m.c4740 = Constraint(expr= - 7*m.b323 - m.x1107 + m.x1147 >= -7)

m.c4741 = Constraint(expr= - 7*m.b324 - m.x1108 + m.x1148 >= -7)

m.c4742 = Constraint(expr= - 7*m.b325 - m.x1109 + m.x1149 >= -7)

m.c4743 = Constraint(expr=   7*m.b291 - m.x1075 + m.x1145 <= 7)

m.c4744 = Constraint(expr=   7*m.b292 - m.x1076 + m.x1146 <= 7)

m.c4745 = Constraint(expr=   7*m.b293 - m.x1077 + m.x1147 <= 7)

m.c4746 = Constraint(expr=   7*m.b294 - m.x1078 + m.x1148 <= 7)

m.c4747 = Constraint(expr=   7*m.b295 - m.x1079 + m.x1149 <= 7)

m.c4748 = Constraint(expr=   7*m.b296 - m.x1080 + m.x1150 <= 7)

m.c4749 = Constraint(expr=   7*m.b297 - m.x1081 + m.x1151 <= 7)

m.c4750 = Constraint(expr=   7*m.b298 - m.x1082 + m.x1152 <= 7)

m.c4751 = Constraint(expr=   7*m.b299 - m.x1083 + m.x1153 <= 7)

m.c4752 = Constraint(expr=   7*m.b300 - m.x1084 + m.x1154 <= 7)

m.c4753 = Constraint(expr=   7*m.b301 - m.x1085 + m.x1145 <= 7)

m.c4754 = Constraint(expr=   7*m.b302 - m.x1086 + m.x1146 <= 7)

m.c4755 = Constraint(expr=   7*m.b303 - m.x1087 + m.x1147 <= 7)

m.c4756 = Constraint(expr=   7*m.b304 - m.x1088 + m.x1148 <= 7)

m.c4757 = Constraint(expr=   7*m.b305 - m.x1089 + m.x1149 <= 7)

m.c4758 = Constraint(expr=   7*m.b306 - m.x1090 + m.x1145 <= 7)

m.c4759 = Constraint(expr=   7*m.b307 - m.x1091 + m.x1146 <= 7)

m.c4760 = Constraint(expr=   7*m.b308 - m.x1092 + m.x1147 <= 7)

m.c4761 = Constraint(expr=   7*m.b309 - m.x1093 + m.x1148 <= 7)

m.c4762 = Constraint(expr=   7*m.b310 - m.x1094 + m.x1149 <= 7)

m.c4763 = Constraint(expr=   7*m.b311 - m.x1095 + m.x1145 <= 7)

m.c4764 = Constraint(expr=   7*m.b312 - m.x1096 + m.x1146 <= 7)

m.c4765 = Constraint(expr=   7*m.b313 - m.x1097 + m.x1147 <= 7)

m.c4766 = Constraint(expr=   7*m.b314 - m.x1098 + m.x1148 <= 7)

m.c4767 = Constraint(expr=   7*m.b315 - m.x1099 + m.x1149 <= 7)

m.c4768 = Constraint(expr=   7*m.b316 - m.x1100 + m.x1150 <= 7)

m.c4769 = Constraint(expr=   7*m.b317 - m.x1101 + m.x1151 <= 7)

m.c4770 = Constraint(expr=   7*m.b318 - m.x1102 + m.x1152 <= 7)

m.c4771 = Constraint(expr=   7*m.b319 - m.x1103 + m.x1153 <= 7)

m.c4772 = Constraint(expr=   7*m.b320 - m.x1104 + m.x1154 <= 7)

m.c4773 = Constraint(expr=   7*m.b321 - m.x1105 + m.x1145 <= 7)

m.c4774 = Constraint(expr=   7*m.b322 - m.x1106 + m.x1146 <= 7)

m.c4775 = Constraint(expr=   7*m.b323 - m.x1107 + m.x1147 <= 7)

m.c4776 = Constraint(expr=   7*m.b324 - m.x1108 + m.x1148 <= 7)

m.c4777 = Constraint(expr=   7*m.b325 - m.x1109 + m.x1149 <= 7)

m.c4778 = Constraint(expr= - 7*m.b291 - m.x1110 + m.x1155 >= -7)

m.c4779 = Constraint(expr= - 7*m.b292 - m.x1111 + m.x1156 >= -7)

m.c4780 = Constraint(expr= - 7*m.b293 - m.x1112 + m.x1157 >= -7)

m.c4781 = Constraint(expr= - 7*m.b294 - m.x1113 + m.x1158 >= -7)

m.c4782 = Constraint(expr= - 7*m.b295 - m.x1114 + m.x1159 >= -7)

m.c4783 = Constraint(expr= - 7*m.b296 - m.x1115 + m.x1160 >= -7)

m.c4784 = Constraint(expr= - 7*m.b297 - m.x1116 + m.x1161 >= -7)

m.c4785 = Constraint(expr= - 7*m.b298 - m.x1117 + m.x1162 >= -7)

m.c4786 = Constraint(expr= - 7*m.b299 - m.x1118 + m.x1163 >= -7)

m.c4787 = Constraint(expr= - 7*m.b300 - m.x1119 + m.x1164 >= -7)

m.c4788 = Constraint(expr= - 7*m.b301 - m.x1120 + m.x1155 >= -7)

m.c4789 = Constraint(expr= - 7*m.b302 - m.x1121 + m.x1156 >= -7)

m.c4790 = Constraint(expr= - 7*m.b303 - m.x1122 + m.x1157 >= -7)

m.c4791 = Constraint(expr= - 7*m.b304 - m.x1123 + m.x1158 >= -7)

m.c4792 = Constraint(expr= - 7*m.b305 - m.x1124 + m.x1159 >= -7)

m.c4793 = Constraint(expr= - 7*m.b306 - m.x1125 + m.x1155 >= -7)

m.c4794 = Constraint(expr= - 7*m.b307 - m.x1126 + m.x1156 >= -7)

m.c4795 = Constraint(expr= - 7*m.b308 - m.x1127 + m.x1157 >= -7)

m.c4796 = Constraint(expr= - 7*m.b309 - m.x1128 + m.x1158 >= -7)

m.c4797 = Constraint(expr= - 7*m.b310 - m.x1129 + m.x1159 >= -7)

m.c4798 = Constraint(expr= - 7*m.b311 - m.x1130 + m.x1155 >= -7)

m.c4799 = Constraint(expr= - 7*m.b312 - m.x1131 + m.x1156 >= -7)

m.c4800 = Constraint(expr= - 7*m.b313 - m.x1132 + m.x1157 >= -7)

m.c4801 = Constraint(expr= - 7*m.b314 - m.x1133 + m.x1158 >= -7)

m.c4802 = Constraint(expr= - 7*m.b315 - m.x1134 + m.x1159 >= -7)

m.c4803 = Constraint(expr= - 7*m.b316 - m.x1135 + m.x1160 >= -7)

m.c4804 = Constraint(expr= - 7*m.b317 - m.x1136 + m.x1161 >= -7)

m.c4805 = Constraint(expr= - 7*m.b318 - m.x1137 + m.x1162 >= -7)

m.c4806 = Constraint(expr= - 7*m.b319 - m.x1138 + m.x1163 >= -7)

m.c4807 = Constraint(expr= - 7*m.b320 - m.x1139 + m.x1164 >= -7)

m.c4808 = Constraint(expr= - 7*m.b321 - m.x1140 + m.x1155 >= -7)

m.c4809 = Constraint(expr= - 7*m.b322 - m.x1141 + m.x1156 >= -7)

m.c4810 = Constraint(expr= - 7*m.b323 - m.x1142 + m.x1157 >= -7)

m.c4811 = Constraint(expr= - 7*m.b324 - m.x1143 + m.x1158 >= -7)

m.c4812 = Constraint(expr= - 7*m.b325 - m.x1144 + m.x1159 >= -7)

m.c4813 = Constraint(expr=   7*m.b291 - m.x1110 + m.x1155 <= 7)

m.c4814 = Constraint(expr=   7*m.b292 - m.x1111 + m.x1156 <= 7)

m.c4815 = Constraint(expr=   7*m.b293 - m.x1112 + m.x1157 <= 7)

m.c4816 = Constraint(expr=   7*m.b294 - m.x1113 + m.x1158 <= 7)

m.c4817 = Constraint(expr=   7*m.b295 - m.x1114 + m.x1159 <= 7)

m.c4818 = Constraint(expr=   7*m.b296 - m.x1115 + m.x1160 <= 7)

m.c4819 = Constraint(expr=   7*m.b297 - m.x1116 + m.x1161 <= 7)

m.c4820 = Constraint(expr=   7*m.b298 - m.x1117 + m.x1162 <= 7)

m.c4821 = Constraint(expr=   7*m.b299 - m.x1118 + m.x1163 <= 7)

m.c4822 = Constraint(expr=   7*m.b300 - m.x1119 + m.x1164 <= 7)

m.c4823 = Constraint(expr=   7*m.b301 - m.x1120 + m.x1155 <= 7)

m.c4824 = Constraint(expr=   7*m.b302 - m.x1121 + m.x1156 <= 7)

m.c4825 = Constraint(expr=   7*m.b303 - m.x1122 + m.x1157 <= 7)

m.c4826 = Constraint(expr=   7*m.b304 - m.x1123 + m.x1158 <= 7)

m.c4827 = Constraint(expr=   7*m.b305 - m.x1124 + m.x1159 <= 7)

m.c4828 = Constraint(expr=   7*m.b306 - m.x1125 + m.x1155 <= 7)

m.c4829 = Constraint(expr=   7*m.b307 - m.x1126 + m.x1156 <= 7)

m.c4830 = Constraint(expr=   7*m.b308 - m.x1127 + m.x1157 <= 7)

m.c4831 = Constraint(expr=   7*m.b309 - m.x1128 + m.x1158 <= 7)

m.c4832 = Constraint(expr=   7*m.b310 - m.x1129 + m.x1159 <= 7)

m.c4833 = Constraint(expr=   7*m.b311 - m.x1130 + m.x1155 <= 7)

m.c4834 = Constraint(expr=   7*m.b312 - m.x1131 + m.x1156 <= 7)

m.c4835 = Constraint(expr=   7*m.b313 - m.x1132 + m.x1157 <= 7)

m.c4836 = Constraint(expr=   7*m.b314 - m.x1133 + m.x1158 <= 7)

m.c4837 = Constraint(expr=   7*m.b315 - m.x1134 + m.x1159 <= 7)

m.c4838 = Constraint(expr=   7*m.b316 - m.x1135 + m.x1160 <= 7)

m.c4839 = Constraint(expr=   7*m.b317 - m.x1136 + m.x1161 <= 7)

m.c4840 = Constraint(expr=   7*m.b318 - m.x1137 + m.x1162 <= 7)

m.c4841 = Constraint(expr=   7*m.b319 - m.x1138 + m.x1163 <= 7)

m.c4842 = Constraint(expr=   7*m.b320 - m.x1139 + m.x1164 <= 7)

m.c4843 = Constraint(expr=   7*m.b321 - m.x1140 + m.x1155 <= 7)

m.c4844 = Constraint(expr=   7*m.b322 - m.x1141 + m.x1156 <= 7)

m.c4845 = Constraint(expr=   7*m.b323 - m.x1142 + m.x1157 <= 7)

m.c4846 = Constraint(expr=   7*m.b324 - m.x1143 + m.x1158 <= 7)

m.c4847 = Constraint(expr=   7*m.b325 - m.x1144 + m.x1159 <= 7)

m.c4848 = Constraint(expr=   m.x362 - m.x417 - m.x432 - m.x447 - m.x462 - m.x477 - m.x492 - m.x507 - m.x522 - m.x537
                           - m.x582 - m.x597 - m.x1200 + m.x1201 == 0)

m.c4849 = Constraint(expr=   m.x363 - m.x418 - m.x433 - m.x448 - m.x463 - m.x478 - m.x493 - m.x508 - m.x523 - m.x538
                           - m.x583 - m.x598 - m.x1201 + m.x1202 == 0)

m.c4850 = Constraint(expr=   m.x364 - m.x419 - m.x434 - m.x449 - m.x464 - m.x479 - m.x494 - m.x509 - m.x524 - m.x539
                           - m.x584 - m.x599 - m.x1202 + m.x1203 == 0)

m.c4851 = Constraint(expr=   m.x365 - m.x420 - m.x435 - m.x450 - m.x465 - m.x480 - m.x495 - m.x510 - m.x525 - m.x540
                           - m.x585 - m.x600 - m.x1203 + m.x1204 == 0)

m.c4852 = Constraint(expr=   m.x367 - m.x552 - m.x567 - m.x1205 + m.x1206 == 0)

m.c4853 = Constraint(expr=   m.x368 - m.x553 - m.x568 - m.x1206 + m.x1207 == 0)

m.c4854 = Constraint(expr=   m.x369 - m.x554 - m.x569 - m.x1207 + m.x1208 == 0)

m.c4855 = Constraint(expr=   m.x370 - m.x555 - m.x570 - m.x1208 + m.x1209 == 0)

m.c4856 = Constraint(expr=   m.x372 - m.x1210 + m.x1211 == 0)

m.c4857 = Constraint(expr=   m.x373 - m.x1211 + m.x1212 == 0)

m.c4858 = Constraint(expr=   m.x374 - m.x1212 + m.x1213 == 0)

m.c4859 = Constraint(expr=   m.x375 - m.x1213 + m.x1214 == 0)

m.c4860 = Constraint(expr=   m.x377 - m.x422 - m.x437 - m.x452 - m.x467 - m.x482 - m.x497 - m.x512 - m.x527 - m.x542
                           - m.x587 - m.x602 - m.x1215 + m.x1216 == 0)

m.c4861 = Constraint(expr=   m.x378 - m.x423 - m.x438 - m.x453 - m.x468 - m.x483 - m.x498 - m.x513 - m.x528 - m.x543
                           - m.x588 - m.x603 - m.x1216 + m.x1217 == 0)

m.c4862 = Constraint(expr=   m.x379 - m.x424 - m.x439 - m.x454 - m.x469 - m.x484 - m.x499 - m.x514 - m.x529 - m.x544
                           - m.x589 - m.x604 - m.x1217 + m.x1218 == 0)

m.c4863 = Constraint(expr=   m.x380 - m.x425 - m.x440 - m.x455 - m.x470 - m.x485 - m.x500 - m.x515 - m.x530 - m.x545
                           - m.x590 - m.x605 - m.x1218 + m.x1219 == 0)

m.c4864 = Constraint(expr=   m.x382 - m.x427 - m.x442 - m.x457 - m.x472 - m.x487 - m.x502 - m.x517 - m.x532 - m.x547
                           - m.x592 - m.x607 - m.x1220 + m.x1221 == 0)

m.c4865 = Constraint(expr=   m.x383 - m.x428 - m.x443 - m.x458 - m.x473 - m.x488 - m.x503 - m.x518 - m.x533 - m.x548
                           - m.x593 - m.x608 - m.x1221 + m.x1222 == 0)

m.c4866 = Constraint(expr=   m.x384 - m.x429 - m.x444 - m.x459 - m.x474 - m.x489 - m.x504 - m.x519 - m.x534 - m.x549
                           - m.x594 - m.x609 - m.x1222 + m.x1223 == 0)

m.c4867 = Constraint(expr=   m.x385 - m.x430 - m.x445 - m.x460 - m.x475 - m.x490 - m.x505 - m.x520 - m.x535 - m.x550
                           - m.x595 - m.x610 - m.x1223 + m.x1224 == 0)

m.c4868 = Constraint(expr=   m.x387 - m.x557 - m.x572 - 0.5*m.x617 - m.x1225 + m.x1226 == 0)

m.c4869 = Constraint(expr=   m.x388 - m.x558 - m.x573 - 0.5*m.x618 - m.x1226 + m.x1227 == 0)

m.c4870 = Constraint(expr=   m.x389 - m.x559 - m.x574 - 0.5*m.x619 - m.x1227 + m.x1228 == 0)

m.c4871 = Constraint(expr=   m.x390 - m.x560 - m.x575 - 0.5*m.x620 - m.x1228 + m.x1229 == 0)

m.c4872 = Constraint(expr=   m.x392 - m.x577 - m.x612 - m.x1230 + m.x1231 == 0)

m.c4873 = Constraint(expr=   m.x393 - m.x578 - m.x613 - m.x1231 + m.x1232 == 0)

m.c4874 = Constraint(expr=   m.x394 - m.x579 - m.x614 - m.x1232 + m.x1233 == 0)

m.c4875 = Constraint(expr=   m.x395 - m.x580 - m.x615 - m.x1233 + m.x1234 == 0)

m.c4876 = Constraint(expr=   m.x397 - m.x562 - 0.5*m.x617 - m.x1235 + m.x1236 == 0)

m.c4877 = Constraint(expr=   m.x398 - m.x563 - 0.5*m.x618 - m.x1236 + m.x1237 == 0)

m.c4878 = Constraint(expr=   m.x399 - m.x564 - 0.5*m.x619 - m.x1237 + m.x1238 == 0)

m.c4879 = Constraint(expr=   m.x400 - m.x565 - 0.5*m.x620 - m.x1238 + m.x1239 == 0)

m.c4880 = Constraint(expr=   m.x402 - m.x1240 + m.x1241 == 0)

m.c4881 = Constraint(expr=   m.x403 - m.x1241 + m.x1242 == 0)

m.c4882 = Constraint(expr=   m.x404 - m.x1242 + m.x1243 == 0)

m.c4883 = Constraint(expr=   m.x405 - m.x1243 + m.x1244 == 0)

m.c4884 = Constraint(expr=   m.x361 - m.x416 - m.x431 - m.x446 - m.x461 - m.x476 - m.x491 - m.x506 - m.x521 - m.x536
                           - m.x581 - m.x596 + m.x1200 == 5000)

m.c4885 = Constraint(expr=   m.x366 - m.x551 - m.x566 + m.x1205 == 6000)

m.c4886 = Constraint(expr=   m.x371 + m.x1210 == 7000)

m.c4887 = Constraint(expr=   m.x376 - m.x421 - m.x436 - m.x451 - m.x466 - m.x481 - m.x496 - m.x511 - m.x526 - m.x541
                           - m.x586 - m.x601 + m.x1215 == 8000)

m.c4888 = Constraint(expr=   m.x381 - m.x426 - m.x441 - m.x456 - m.x471 - m.x486 - m.x501 - m.x516 - m.x531 - m.x546
                           - m.x591 - m.x606 + m.x1220 == 8000)

m.c4889 = Constraint(expr=   m.x386 - m.x556 - m.x571 - 0.5*m.x616 + m.x1225 == 10000)

m.c4890 = Constraint(expr=   m.x391 - m.x576 - m.x611 + m.x1230 == 5000)

m.c4891 = Constraint(expr=   m.x396 - m.x561 - 0.5*m.x616 + m.x1235 == 5000)

m.c4892 = Constraint(expr=   m.x401 + m.x1240 == 10000)

m.c4893 = Constraint(expr= - m.x1145 - m.x1146 - m.x1147 - m.x1148 - m.x1149 + m.x1155 + m.x1156 + m.x1157 + m.x1158
                           + m.x1159 == 7)

m.c4894 = Constraint(expr= - m.x1150 - m.x1151 - m.x1152 - m.x1153 - m.x1154 + m.x1160 + m.x1161 + m.x1162 + m.x1163
                           + m.x1164 == 7)

m.c4895 = Constraint(expr= - m.b291 + m.b292 + m.x1245 >= 0)

m.c4896 = Constraint(expr= - m.b292 + m.b293 + m.x1246 >= 0)

m.c4897 = Constraint(expr= - m.b293 + m.b294 + m.x1247 >= 0)

m.c4898 = Constraint(expr= - m.b294 + m.b295 + m.x1248 >= 0)

m.c4899 = Constraint(expr= - m.b296 + m.b297 + m.x1249 >= 0)

m.c4900 = Constraint(expr= - m.b297 + m.b298 + m.x1250 >= 0)

m.c4901 = Constraint(expr= - m.b298 + m.b299 + m.x1251 >= 0)

m.c4902 = Constraint(expr= - m.b299 + m.b300 + m.x1252 >= 0)

m.c4903 = Constraint(expr= - m.b301 + m.b302 + m.x1245 >= 0)

m.c4904 = Constraint(expr= - m.b302 + m.b303 + m.x1246 >= 0)

m.c4905 = Constraint(expr= - m.b303 + m.b304 + m.x1247 >= 0)

m.c4906 = Constraint(expr= - m.b304 + m.b305 + m.x1248 >= 0)

m.c4907 = Constraint(expr= - m.b306 + m.b307 + m.x1245 >= 0)

m.c4908 = Constraint(expr= - m.b307 + m.b308 + m.x1246 >= 0)

m.c4909 = Constraint(expr= - m.b308 + m.b309 + m.x1247 >= 0)

m.c4910 = Constraint(expr= - m.b309 + m.b310 + m.x1248 >= 0)

m.c4911 = Constraint(expr= - m.b311 + m.b312 + m.x1245 >= 0)

m.c4912 = Constraint(expr= - m.b312 + m.b313 + m.x1246 >= 0)

m.c4913 = Constraint(expr= - m.b313 + m.b314 + m.x1247 >= 0)

m.c4914 = Constraint(expr= - m.b314 + m.b315 + m.x1248 >= 0)

m.c4915 = Constraint(expr= - m.b316 + m.b317 + m.x1249 >= 0)

m.c4916 = Constraint(expr= - m.b317 + m.b318 + m.x1250 >= 0)

m.c4917 = Constraint(expr= - m.b318 + m.b319 + m.x1251 >= 0)

m.c4918 = Constraint(expr= - m.b319 + m.b320 + m.x1252 >= 0)

m.c4919 = Constraint(expr= - m.b321 + m.b322 + m.x1245 >= 0)

m.c4920 = Constraint(expr= - m.b322 + m.b323 + m.x1246 >= 0)

m.c4921 = Constraint(expr= - m.b323 + m.b324 + m.x1247 >= 0)

m.c4922 = Constraint(expr= - m.b324 + m.b325 + m.x1248 >= 0)

m.c4923 = Constraint(expr=   m.b291 - m.b292 + m.x1245 >= 0)

m.c4924 = Constraint(expr=   m.b292 - m.b293 + m.x1246 >= 0)

m.c4925 = Constraint(expr=   m.b293 - m.b294 + m.x1247 >= 0)

m.c4926 = Constraint(expr=   m.b294 - m.b295 + m.x1248 >= 0)

m.c4927 = Constraint(expr=   m.b296 - m.b297 + m.x1249 >= 0)

m.c4928 = Constraint(expr=   m.b297 - m.b298 + m.x1250 >= 0)

m.c4929 = Constraint(expr=   m.b298 - m.b299 + m.x1251 >= 0)

m.c4930 = Constraint(expr=   m.b299 - m.b300 + m.x1252 >= 0)

m.c4931 = Constraint(expr=   m.b301 - m.b302 + m.x1245 >= 0)

m.c4932 = Constraint(expr=   m.b302 - m.b303 + m.x1246 >= 0)

m.c4933 = Constraint(expr=   m.b303 - m.b304 + m.x1247 >= 0)

m.c4934 = Constraint(expr=   m.b304 - m.b305 + m.x1248 >= 0)

m.c4935 = Constraint(expr=   m.b306 - m.b307 + m.x1245 >= 0)

m.c4936 = Constraint(expr=   m.b307 - m.b308 + m.x1246 >= 0)

m.c4937 = Constraint(expr=   m.b308 - m.b309 + m.x1247 >= 0)

m.c4938 = Constraint(expr=   m.b309 - m.b310 + m.x1248 >= 0)

m.c4939 = Constraint(expr=   m.b311 - m.b312 + m.x1245 >= 0)

m.c4940 = Constraint(expr=   m.b312 - m.b313 + m.x1246 >= 0)

m.c4941 = Constraint(expr=   m.b313 - m.b314 + m.x1247 >= 0)

m.c4942 = Constraint(expr=   m.b314 - m.b315 + m.x1248 >= 0)

m.c4943 = Constraint(expr=   m.b316 - m.b317 + m.x1249 >= 0)

m.c4944 = Constraint(expr=   m.b317 - m.b318 + m.x1250 >= 0)

m.c4945 = Constraint(expr=   m.b318 - m.b319 + m.x1251 >= 0)

m.c4946 = Constraint(expr=   m.b319 - m.b320 + m.x1252 >= 0)

m.c4947 = Constraint(expr=   m.b321 - m.b322 + m.x1245 >= 0)

m.c4948 = Constraint(expr=   m.b322 - m.b323 + m.x1246 >= 0)

m.c4949 = Constraint(expr=   m.b323 - m.b324 + m.x1247 >= 0)

m.c4950 = Constraint(expr=   m.b324 - m.b325 + m.x1248 >= 0)

m.c4952 = Constraint(expr=-m.x1279*m.x353 + m.x388 == 0)

m.c4953 = Constraint(expr=-m.x1280*m.x354 + m.x389 == 0)

m.c4954 = Constraint(expr=-m.x1281*m.x355 + m.x390 == 0)

m.c4955 = Constraint(expr=-m.x1284*m.x353 + m.x393 == 0)

m.c4956 = Constraint(expr=-m.x1285*m.x354 + m.x394 == 0)

m.c4957 = Constraint(expr=-m.x1286*m.x355 + m.x395 == 0)

m.c4958 = Constraint(expr=-m.x1289*m.x353 + m.x398 == 0)

m.c4959 = Constraint(expr=-m.x1290*m.x354 + m.x399 == 0)

m.c4960 = Constraint(expr=-m.x1291*m.x355 + m.x400 == 0)

m.c4961 = Constraint(expr=-m.x1253*m.x1165 + m.x1200 == 0)

m.c4962 = Constraint(expr=-m.x1254*m.x1166 + m.x1201 == 0)

m.c4963 = Constraint(expr=-m.x1255*m.x1167 + m.x1202 == 0)

m.c4964 = Constraint(expr=-m.x1256*m.x1168 + m.x1203 == 0)

m.c4965 = Constraint(expr=-m.x1257*m.x1169 + m.x1204 == 0)

m.c4966 = Constraint(expr=-m.x1258*m.x1170 + m.x1205 == 0)

m.c4967 = Constraint(expr=-m.x1259*m.x1171 + m.x1206 == 0)

m.c4968 = Constraint(expr=-m.x1260*m.x1172 + m.x1207 == 0)

m.c4969 = Constraint(expr=-m.x1261*m.x1173 + m.x1208 == 0)

m.c4970 = Constraint(expr=-m.x1262*m.x1174 + m.x1209 == 0)

m.c4971 = Constraint(expr=-m.x1263*m.x1175 + m.x1210 == 0)

m.c4972 = Constraint(expr=-m.x1264*m.x1176 + m.x1211 == 0)

m.c4973 = Constraint(expr=-m.x1265*m.x1177 + m.x1212 == 0)

m.c4974 = Constraint(expr=-m.x1266*m.x1178 + m.x1213 == 0)

m.c4975 = Constraint(expr=-m.x1267*m.x1179 + m.x1214 == 0)

m.c4976 = Constraint(expr=-m.x1268*m.x1180 + m.x1215 == 0)

m.c4977 = Constraint(expr=-m.x1269*m.x1181 + m.x1216 == 0)

m.c4978 = Constraint(expr=-m.x1270*m.x1182 + m.x1217 == 0)

m.c4979 = Constraint(expr=-m.x1271*m.x1183 + m.x1218 == 0)

m.c4980 = Constraint(expr=-m.x1272*m.x1184 + m.x1219 == 0)

m.c4981 = Constraint(expr=-m.x1273*m.x1185 + m.x1220 == 0)

m.c4982 = Constraint(expr=-m.x1274*m.x1186 + m.x1221 == 0)

m.c4983 = Constraint(expr=-m.x1275*m.x1187 + m.x1222 == 0)

m.c4984 = Constraint(expr=-m.x1276*m.x1188 + m.x1223 == 0)

m.c4985 = Constraint(expr=-m.x1277*m.x1189 + m.x1224 == 0)

m.c4986 = Constraint(expr=-m.x1278*m.x1190 + m.x1225 == 0)

m.c4987 = Constraint(expr=-m.x1279*m.x1191 + m.x1226 == 0)

m.c4988 = Constraint(expr=-m.x1280*m.x1192 + m.x1227 == 0)

m.c4989 = Constraint(expr=-m.x1281*m.x1193 + m.x1228 == 0)

m.c4990 = Constraint(expr=-m.x1282*m.x1194 + m.x1229 == 0)

m.c4991 = Constraint(expr=-m.x1283*m.x1190 + m.x1230 == 0)

m.c4992 = Constraint(expr=-m.x1284*m.x1191 + m.x1231 == 0)

m.c4993 = Constraint(expr=-m.x1285*m.x1192 + m.x1232 == 0)

m.c4994 = Constraint(expr=-m.x1286*m.x1193 + m.x1233 == 0)

m.c4995 = Constraint(expr=-m.x1287*m.x1194 + m.x1234 == 0)

m.c4996 = Constraint(expr=-m.x1288*m.x1190 + m.x1235 == 0)

m.c4997 = Constraint(expr=-m.x1289*m.x1191 + m.x1236 == 0)

m.c4998 = Constraint(expr=-m.x1290*m.x1192 + m.x1237 == 0)

m.c4999 = Constraint(expr=-m.x1291*m.x1193 + m.x1238 == 0)

m.c5000 = Constraint(expr=-m.x1292*m.x1194 + m.x1239 == 0)

m.c5001 = Constraint(expr=-m.x1293*m.x1195 + m.x1240 == 0)

m.c5002 = Constraint(expr=-m.x1294*m.x1196 + m.x1241 == 0)

m.c5003 = Constraint(expr=-m.x1295*m.x1197 + m.x1242 == 0)

m.c5004 = Constraint(expr=-m.x1296*m.x1198 + m.x1243 == 0)

m.c5005 = Constraint(expr=-m.x1297*m.x1199 + m.x1244 == 0)
