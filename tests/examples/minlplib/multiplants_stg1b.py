#  MINLP written by GAMS Convert at 04/21/18 13:52:37
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        280      140       30      110        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        476      233      243        0        0        0        0        0
#  FX     82       82        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1920     1777      143        0


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
m.b217 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b218 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b219 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b220 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b221 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b222 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b223 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b224 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b225 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b226 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b227 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b228 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b229 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b230 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b231 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b232 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b233 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b234 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b235 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b236 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b237 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b238 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b239 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b240 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b241 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b242 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b243 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x255 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x258 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x262 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x263 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x264 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x265 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x266 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x267 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x268 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x269 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x270 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x271 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x272 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x273 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x274 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x275 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x276 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x277 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x278 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x279 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x280 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x281 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x282 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x283 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x284 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x285 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x286 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x287 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x289 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x290 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x291 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x292 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x293 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x294 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x295 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x296 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x297 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x298 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x299 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x300 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x301 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x302 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x303 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x304 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x305 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x306 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x307 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x309 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x311 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x312 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x313 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x314 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x315 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x316 = Var(within=Reals,bounds=(0,270000),initialize=0)
m.x317 = Var(within=Reals,bounds=(0,270000),initialize=0)
m.x318 = Var(within=Reals,bounds=(0,270000),initialize=0)
m.x319 = Var(within=Reals,bounds=(0,270000),initialize=0)
m.x320 = Var(within=Reals,bounds=(0,270000),initialize=0)
m.x321 = Var(within=Reals,bounds=(0,270000),initialize=0)
m.x322 = Var(within=Reals,bounds=(0,270000),initialize=0)
m.x323 = Var(within=Reals,bounds=(0,270000),initialize=0)
m.x324 = Var(within=Reals,bounds=(0,270000),initialize=0)
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
m.x361 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x362 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x363 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x364 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x365 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x366 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x367 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x368 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x369 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x370 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x371 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x372 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x373 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x374 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x375 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x376 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x377 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x378 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x379 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x380 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x381 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x382 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x383 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x384 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x385 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x386 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x387 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x388 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x389 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x390 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x391 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x392 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x393 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x394 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x395 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x396 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x397 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x398 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x399 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x400 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x401 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x402 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x403 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x404 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x405 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x406 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x407 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x408 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x409 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x410 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x411 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x412 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x413 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x414 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x415 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x416 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x417 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x418 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x419 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x420 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x421 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x422 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x423 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x424 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x425 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x426 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x427 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x428 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x429 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x430 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x431 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x432 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x433 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x434 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x435 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x436 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x437 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x438 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x439 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x440 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x441 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x442 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x443 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x444 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x445 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x446 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x447 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x448 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x449 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x450 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x451 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x452 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x453 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x454 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x455 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x456 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x457 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x458 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x459 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x460 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x461 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x462 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x463 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x464 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x465 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x466 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x467 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x468 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x469 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x470 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x471 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x472 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x473 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x474 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x475 = Var(within=Reals,bounds=(200,600),initialize=200)
m.x476 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x476, sense=maximize)

m.c1 = Constraint(expr=m.x476*m.x475 + (0.00203*m.x415 + 0.00203*m.x416)*(m.x464 - m.x463) + (0.00203*m.x416 + 0.00203*
                       m.x417)*(m.x465 - m.x464) + (0.00203*m.x417 + 0.00203*m.x418)*(m.x466 - m.x465) + (0.00203*m.x418
                        + 0.00203*m.x419)*(m.x467 - m.x466) + (0.00203*m.x419 + 0.00203*m.x420)*(m.x468 - m.x467) + (
                       0.00203*m.x420 + 0.00203*m.x421)*(m.x469 - m.x468) + (0.00203*m.x421 + 0.00203*m.x422)*(m.x470 - 
                       m.x469) + (0.00203*m.x422 + 0.00203*m.x423)*(m.x471 - m.x470) + (0.00203*m.x415 + 0.00203*m.x423)
                       *(m.x475 - m.x471) + (0.00203*m.x433 + 0.00203*m.x434)*(m.x464 - m.x463) + (0.00203*m.x434 + 
                       0.00203*m.x435)*(m.x465 - m.x464) + (0.00203*m.x435 + 0.00203*m.x436)*(m.x466 - m.x465) + (
                       0.00203*m.x436 + 0.00203*m.x437)*(m.x467 - m.x466) + (0.00203*m.x437 + 0.00203*m.x438)*(m.x468 - 
                       m.x467) + (0.00203*m.x438 + 0.00203*m.x439)*(m.x469 - m.x468) + (0.00203*m.x439 + 0.00203*m.x440)
                       *(m.x470 - m.x469) + (0.00203*m.x440 + 0.00203*m.x441)*(m.x471 - m.x470) + (0.00203*m.x433 + 
                       0.00203*m.x441)*(m.x475 - m.x471) + (0.00203*m.x451 + 0.00203*m.x452)*(m.x464 - m.x463) + (
                       0.00203*m.x452 + 0.00203*m.x453)*(m.x465 - m.x464) + (0.00203*m.x453 + 0.00203*m.x454)*(m.x466 - 
                       m.x465) + (0.00203*m.x454 + 0.00203*m.x455)*(m.x467 - m.x466) + (0.00203*m.x455 + 0.00203*m.x456)
                       *(m.x468 - m.x467) + (0.00203*m.x456 + 0.00203*m.x457)*(m.x469 - m.x468) + (0.00203*m.x457 + 
                       0.00203*m.x458)*(m.x470 - m.x469) + (0.00203*m.x458 + 0.00203*m.x459)*(m.x471 - m.x470) + (
                       0.00203*m.x451 + 0.00203*m.x459)*(m.x475 - m.x471) + 3800*m.b82 + 3800*m.b83 + 3800*m.b84
                        + 3800*m.b85 + 3800*m.b86 + 3800*m.b87 + 3800*m.b88 + 3800*m.b89 + 3800*m.b90 + 6080*m.b91
                        + 6080*m.b92 + 6080*m.b93 + 6080*m.b94 + 6080*m.b95 + 6080*m.b96 + 6080*m.b97 + 6080*m.b98
                        + 6080*m.b99 + 7500*m.b100 + 7500*m.b101 + 7500*m.b102 + 7500*m.b103 + 7500*m.b104 + 7500*m.b105
                        + 7500*m.b106 + 7500*m.b107 + 7500*m.b108 + 2250*m.b109 + 2250*m.b110 + 2250*m.b111
                        + 2250*m.b112 + 2250*m.b113 + 2250*m.b114 + 2250*m.b115 + 2250*m.b116 + 2250*m.b117
                        + 3080*m.b118 + 3080*m.b119 + 3080*m.b120 + 3080*m.b121 + 3080*m.b122 + 3080*m.b123
                        + 3080*m.b124 + 3080*m.b125 + 3080*m.b126 + 5390*m.b127 + 5390*m.b128 + 5390*m.b129
                        + 5390*m.b130 + 5390*m.b131 + 5390*m.b132 + 5390*m.b133 + 5390*m.b134 + 5390*m.b135
                        + 8360*m.b136 + 8360*m.b137 + 8360*m.b138 + 8360*m.b139 + 8360*m.b140 + 8360*m.b141
                        + 8360*m.b142 + 8360*m.b143 + 8360*m.b144 + 760*m.b145 + 760*m.b146 + 760*m.b147 + 760*m.b148
                        + 760*m.b149 + 760*m.b150 + 760*m.b151 + 760*m.b152 + 760*m.b153 + 1500*m.b154 + 1500*m.b155
                        + 1500*m.b156 + 1500*m.b157 + 1500*m.b158 + 1500*m.b159 + 1500*m.b160 + 1500*m.b161
                        + 1500*m.b162 + 3750*m.b163 + 3750*m.b164 + 3750*m.b165 + 3750*m.b166 + 3750*m.b167
                        + 3750*m.b168 + 3750*m.b169 + 3750*m.b170 + 3750*m.b171 + 4620*m.b172 + 4620*m.b173
                        + 4620*m.b174 + 4620*m.b175 + 4620*m.b176 + 4620*m.b177 + 4620*m.b178 + 4620*m.b179
                        + 4620*m.b180 + 770*m.b181 + 770*m.b182 + 770*m.b183 + 770*m.b184 + 770*m.b185 + 770*m.b186
                        + 770*m.b187 + 770*m.b188 + 770*m.b189 + 6840*m.b190 + 6840*m.b191 + 6840*m.b192 + 6840*m.b193
                        + 6840*m.b194 + 6840*m.b195 + 6840*m.b196 + 6840*m.b197 + 6840*m.b198 + 8360*m.b199
                        + 8360*m.b200 + 8360*m.b201 + 8360*m.b202 + 8360*m.b203 + 8360*m.b204 + 8360*m.b205
                        + 8360*m.b206 + 8360*m.b207 + 3750*m.b208 + 3750*m.b209 + 3750*m.b210 + 3750*m.b211
                        + 3750*m.b212 + 3750*m.b213 + 3750*m.b214 + 3750*m.b215 + 3750*m.b216 + 5250*m.b217
                        + 5250*m.b218 + 5250*m.b219 + 5250*m.b220 + 5250*m.b221 + 5250*m.b222 + 5250*m.b223
                        + 5250*m.b224 + 5250*m.b225 + 4620*m.b226 + 4620*m.b227 + 4620*m.b228 + 4620*m.b229
                        + 4620*m.b230 + 4620*m.b231 + 4620*m.b232 + 4620*m.b233 + 4620*m.b234 + 3080*m.b235
                        + 3080*m.b236 + 3080*m.b237 + 3080*m.b238 + 3080*m.b239 + 3080*m.b240 + 3080*m.b241
                        + 3080*m.b242 + 3080*m.b243 - 0.15*m.x460 - 0.4*m.x461 - 0.65*m.x462 + 0.1406*m.x472
                        + 0.1406*m.x473 + 0.1406*m.x474 == 0)

m.c2 = Constraint(expr=   m.b1 - m.b9 + m.b82 + m.b91 - m.b108 - m.b126 + m.x325 - m.x333 == 0)

m.c3 = Constraint(expr= - m.b1 + m.b2 + m.b83 + m.b92 - m.b100 - m.b118 - m.x325 + m.x326 == 0)

m.c4 = Constraint(expr= - m.b2 + m.b3 + m.b84 + m.b93 - m.b101 - m.b119 - m.x326 + m.x327 == 0)

m.c5 = Constraint(expr= - m.b3 + m.b4 + m.b85 + m.b94 - m.b102 - m.b120 - m.x327 + m.x328 == 0)

m.c6 = Constraint(expr= - m.b4 + m.b5 + m.b86 + m.b95 - m.b103 - m.b121 - m.x328 + m.x329 == 0)

m.c7 = Constraint(expr= - m.b5 + m.b6 + m.b87 + m.b96 - m.b104 - m.b122 - m.x329 + m.x330 == 0)

m.c8 = Constraint(expr= - m.b6 + m.b7 + m.b88 + m.b97 - m.b105 - m.b123 - m.x330 + m.x331 == 0)

m.c9 = Constraint(expr= - m.b7 + m.b8 + m.b89 + m.b98 - m.b106 - m.b124 - m.x331 + m.x332 == 0)

m.c10 = Constraint(expr= - m.b8 + m.b9 + m.b90 + m.b99 - m.b107 - m.b125 - m.x332 + m.x333 == 0)

m.c11 = Constraint(expr=   m.b28 - m.b36 - m.b90 + m.b100 + m.b109 - m.b135 + m.x334 - m.x342 == 0)

m.c12 = Constraint(expr= - m.b28 + m.b29 - m.b82 + m.b101 + m.b110 - m.b127 - m.x334 + m.x335 == 0)

m.c13 = Constraint(expr= - m.b29 + m.b30 - m.b83 + m.b102 + m.b111 - m.b128 - m.x335 + m.x336 == 0)

m.c14 = Constraint(expr= - m.b30 + m.b31 - m.b84 + m.b103 + m.b112 - m.b129 - m.x336 + m.x337 == 0)

m.c15 = Constraint(expr= - m.b31 + m.b32 - m.b85 + m.b104 + m.b113 - m.b130 - m.x337 + m.x338 == 0)

m.c16 = Constraint(expr= - m.b32 + m.b33 - m.b86 + m.b105 + m.b114 - m.b131 - m.x338 + m.x339 == 0)

m.c17 = Constraint(expr= - m.b33 + m.b34 - m.b87 + m.b106 + m.b115 - m.b132 - m.x339 + m.x340 == 0)

m.c18 = Constraint(expr= - m.b34 + m.b35 - m.b88 + m.b107 + m.b116 - m.b133 - m.x340 + m.x341 == 0)

m.c19 = Constraint(expr= - m.b35 + m.b36 - m.b89 + m.b108 + m.b117 - m.b134 - m.x341 + m.x342 == 0)

m.c20 = Constraint(expr=   m.b55 - m.b63 - m.b99 - m.b117 + m.b118 + m.b127 + m.x343 - m.x351 == 0)

m.c21 = Constraint(expr= - m.b55 + m.b56 - m.b91 - m.b109 + m.b119 + m.b128 - m.x343 + m.x344 == 0)

m.c22 = Constraint(expr= - m.b56 + m.b57 - m.b92 - m.b110 + m.b120 + m.b129 - m.x344 + m.x345 == 0)

m.c23 = Constraint(expr= - m.b57 + m.b58 - m.b93 - m.b111 + m.b121 + m.b130 - m.x345 + m.x346 == 0)

m.c24 = Constraint(expr= - m.b58 + m.b59 - m.b94 - m.b112 + m.b122 + m.b131 - m.x346 + m.x347 == 0)

m.c25 = Constraint(expr= - m.b59 + m.b60 - m.b95 - m.b113 + m.b123 + m.b132 - m.x347 + m.x348 == 0)

m.c26 = Constraint(expr= - m.b60 + m.b61 - m.b96 - m.b114 + m.b124 + m.b133 - m.x348 + m.x349 == 0)

m.c27 = Constraint(expr= - m.b61 + m.b62 - m.b97 - m.b115 + m.b125 + m.b134 - m.x349 + m.x350 == 0)

m.c28 = Constraint(expr= - m.b62 + m.b63 - m.b98 - m.b116 + m.b126 + m.b135 - m.x350 + m.x351 == 0)

m.c29 = Constraint(expr=   m.b10 - m.b18 + m.b136 + m.b145 - m.b162 - m.b180 + m.x352 - m.x360 == 0)

m.c30 = Constraint(expr= - m.b10 + m.b11 + m.b137 + m.b146 - m.b154 - m.b172 - m.x352 + m.x353 == 0)

m.c31 = Constraint(expr= - m.b11 + m.b12 + m.b138 + m.b147 - m.b155 - m.b173 - m.x353 + m.x354 == 0)

m.c32 = Constraint(expr= - m.b12 + m.b13 + m.b139 + m.b148 - m.b156 - m.b174 - m.x354 + m.x355 == 0)

m.c33 = Constraint(expr= - m.b13 + m.b14 + m.b140 + m.b149 - m.b157 - m.b175 - m.x355 + m.x356 == 0)

m.c34 = Constraint(expr= - m.b14 + m.b15 + m.b141 + m.b150 - m.b158 - m.b176 - m.x356 + m.x357 == 0)

m.c35 = Constraint(expr= - m.b15 + m.b16 + m.b142 + m.b151 - m.b159 - m.b177 - m.x357 + m.x358 == 0)

m.c36 = Constraint(expr= - m.b16 + m.b17 + m.b143 + m.b152 - m.b160 - m.b178 - m.x358 + m.x359 == 0)

m.c37 = Constraint(expr= - m.b17 + m.b18 + m.b144 + m.b153 - m.b161 - m.b179 - m.x359 + m.x360 == 0)

m.c38 = Constraint(expr=   m.b37 - m.b45 - m.b144 + m.b154 + m.b163 - m.b189 + m.x361 - m.x369 == 0)

m.c39 = Constraint(expr= - m.b37 + m.b38 - m.b136 + m.b155 + m.b164 - m.b181 - m.x361 + m.x362 == 0)

m.c40 = Constraint(expr= - m.b38 + m.b39 - m.b137 + m.b156 + m.b165 - m.b182 - m.x362 + m.x363 == 0)

m.c41 = Constraint(expr= - m.b39 + m.b40 - m.b138 + m.b157 + m.b166 - m.b183 - m.x363 + m.x364 == 0)

m.c42 = Constraint(expr= - m.b40 + m.b41 - m.b139 + m.b158 + m.b167 - m.b184 - m.x364 + m.x365 == 0)

m.c43 = Constraint(expr= - m.b41 + m.b42 - m.b140 + m.b159 + m.b168 - m.b185 - m.x365 + m.x366 == 0)

m.c44 = Constraint(expr= - m.b42 + m.b43 - m.b141 + m.b160 + m.b169 - m.b186 - m.x366 + m.x367 == 0)

m.c45 = Constraint(expr= - m.b43 + m.b44 - m.b142 + m.b161 + m.b170 - m.b187 - m.x367 + m.x368 == 0)

m.c46 = Constraint(expr= - m.b44 + m.b45 - m.b143 + m.b162 + m.b171 - m.b188 - m.x368 + m.x369 == 0)

m.c47 = Constraint(expr=   m.b64 - m.b72 - m.b153 - m.b171 + m.b172 + m.b181 + m.x370 - m.x378 == 0)

m.c48 = Constraint(expr= - m.b64 + m.b65 - m.b145 - m.b163 + m.b173 + m.b182 - m.x370 + m.x371 == 0)

m.c49 = Constraint(expr= - m.b65 + m.b66 - m.b146 - m.b164 + m.b174 + m.b183 - m.x371 + m.x372 == 0)

m.c50 = Constraint(expr= - m.b66 + m.b67 - m.b147 - m.b165 + m.b175 + m.b184 - m.x372 + m.x373 == 0)

m.c51 = Constraint(expr= - m.b67 + m.b68 - m.b148 - m.b166 + m.b176 + m.b185 - m.x373 + m.x374 == 0)

m.c52 = Constraint(expr= - m.b68 + m.b69 - m.b149 - m.b167 + m.b177 + m.b186 - m.x374 + m.x375 == 0)

m.c53 = Constraint(expr= - m.b69 + m.b70 - m.b150 - m.b168 + m.b178 + m.b187 - m.x375 + m.x376 == 0)

m.c54 = Constraint(expr= - m.b70 + m.b71 - m.b151 - m.b169 + m.b179 + m.b188 - m.x376 + m.x377 == 0)

m.c55 = Constraint(expr= - m.b71 + m.b72 - m.b152 - m.b170 + m.b180 + m.b189 - m.x377 + m.x378 == 0)

m.c56 = Constraint(expr=   m.b19 - m.b27 + m.b190 + m.b199 - m.b216 - m.b234 + m.x379 - m.x387 == 0)

m.c57 = Constraint(expr= - m.b19 + m.b20 + m.b191 + m.b200 - m.b208 - m.b226 - m.x379 + m.x380 == 0)

m.c58 = Constraint(expr= - m.b20 + m.b21 + m.b192 + m.b201 - m.b209 - m.b227 - m.x380 + m.x381 == 0)

m.c59 = Constraint(expr= - m.b21 + m.b22 + m.b193 + m.b202 - m.b210 - m.b228 - m.x381 + m.x382 == 0)

m.c60 = Constraint(expr= - m.b22 + m.b23 + m.b194 + m.b203 - m.b211 - m.b229 - m.x382 + m.x383 == 0)

m.c61 = Constraint(expr= - m.b23 + m.b24 + m.b195 + m.b204 - m.b212 - m.b230 - m.x383 + m.x384 == 0)

m.c62 = Constraint(expr= - m.b24 + m.b25 + m.b196 + m.b205 - m.b213 - m.b231 - m.x384 + m.x385 == 0)

m.c63 = Constraint(expr= - m.b25 + m.b26 + m.b197 + m.b206 - m.b214 - m.b232 - m.x385 + m.x386 == 0)

m.c64 = Constraint(expr= - m.b26 + m.b27 + m.b198 + m.b207 - m.b215 - m.b233 - m.x386 + m.x387 == 0)

m.c65 = Constraint(expr=   m.b46 - m.b54 - m.b198 + m.b208 + m.b217 - m.b243 + m.x388 - m.x396 == 0)

m.c66 = Constraint(expr= - m.b46 + m.b47 - m.b190 + m.b209 + m.b218 - m.b235 - m.x388 + m.x389 == 0)

m.c67 = Constraint(expr= - m.b47 + m.b48 - m.b191 + m.b210 + m.b219 - m.b236 - m.x389 + m.x390 == 0)

m.c68 = Constraint(expr= - m.b48 + m.b49 - m.b192 + m.b211 + m.b220 - m.b237 - m.x390 + m.x391 == 0)

m.c69 = Constraint(expr= - m.b49 + m.b50 - m.b193 + m.b212 + m.b221 - m.b238 - m.x391 + m.x392 == 0)

m.c70 = Constraint(expr= - m.b50 + m.b51 - m.b194 + m.b213 + m.b222 - m.b239 - m.x392 + m.x393 == 0)

m.c71 = Constraint(expr= - m.b51 + m.b52 - m.b195 + m.b214 + m.b223 - m.b240 - m.x393 + m.x394 == 0)

m.c72 = Constraint(expr= - m.b52 + m.b53 - m.b196 + m.b215 + m.b224 - m.b241 - m.x394 + m.x395 == 0)

m.c73 = Constraint(expr= - m.b53 + m.b54 - m.b197 + m.b216 + m.b225 - m.b242 - m.x395 + m.x396 == 0)

m.c74 = Constraint(expr=   m.b73 - m.b81 - m.b207 - m.b225 + m.b226 + m.b235 + m.x397 - m.x405 == 0)

m.c75 = Constraint(expr= - m.b73 + m.b74 - m.b199 - m.b217 + m.b227 + m.b236 - m.x397 + m.x398 == 0)

m.c76 = Constraint(expr= - m.b74 + m.b75 - m.b200 - m.b218 + m.b228 + m.b237 - m.x398 + m.x399 == 0)

m.c77 = Constraint(expr= - m.b75 + m.b76 - m.b201 - m.b219 + m.b229 + m.b238 - m.x399 + m.x400 == 0)

m.c78 = Constraint(expr= - m.b76 + m.b77 - m.b202 - m.b220 + m.b230 + m.b239 - m.x400 + m.x401 == 0)

m.c79 = Constraint(expr= - m.b77 + m.b78 - m.b203 - m.b221 + m.b231 + m.b240 - m.x401 + m.x402 == 0)

m.c80 = Constraint(expr= - m.b78 + m.b79 - m.b204 - m.b222 + m.b232 + m.b241 - m.x402 + m.x403 == 0)

m.c81 = Constraint(expr= - m.b79 + m.b80 - m.b205 - m.b223 + m.b233 + m.b242 - m.x403 + m.x404 == 0)

m.c82 = Constraint(expr= - m.b80 + m.b81 - m.b206 - m.b224 + m.b234 + m.b243 - m.x404 + m.x405 == 0)

m.c83 = Constraint(expr= - m.x252 + m.x261 + m.x270 + m.x406 - m.x414 == 0)

m.c84 = Constraint(expr= - m.x244 + m.x253 + m.x262 - m.x406 + m.x407 == 0)

m.c85 = Constraint(expr= - m.x245 + m.x254 + m.x263 - m.x407 + m.x408 == 0)

m.c86 = Constraint(expr= - m.x246 + m.x255 + m.x264 - m.x408 + m.x409 == 0)

m.c87 = Constraint(expr= - m.x247 + m.x256 + m.x265 - m.x409 + m.x410 == 0)

m.c88 = Constraint(expr= - m.x248 + m.x257 + m.x266 - m.x410 + m.x411 == 0)

m.c89 = Constraint(expr= - m.x249 + m.x258 + m.x267 - m.x411 + m.x412 == 0)

m.c90 = Constraint(expr= - m.x250 + m.x259 + m.x268 - m.x412 + m.x413 == 0)

m.c91 = Constraint(expr= - m.x251 + m.x260 + m.x269 - m.x413 + m.x414 == 0)

m.c92 = Constraint(expr=m.x460/m.x475*(m.x475 - m.x471) - m.x261 - m.x270 + m.x415 - m.x423 == 0)

m.c93 = Constraint(expr=m.x460/m.x475*(m.x464 - m.x463) - m.x253 - m.x262 - m.x415 + m.x416 == 0)

m.c94 = Constraint(expr=m.x460/m.x475*(m.x465 - m.x464) - m.x254 - m.x263 - m.x416 + m.x417 == 0)

m.c95 = Constraint(expr=m.x460/m.x475*(m.x466 - m.x465) - m.x255 - m.x264 - m.x417 + m.x418 == 0)

m.c96 = Constraint(expr=m.x460/m.x475*(m.x467 - m.x466) - m.x256 - m.x265 - m.x418 + m.x419 == 0)

m.c97 = Constraint(expr=m.x460/m.x475*(m.x468 - m.x467) - m.x257 - m.x266 - m.x419 + m.x420 == 0)

m.c98 = Constraint(expr=m.x460/m.x475*(m.x469 - m.x468) - m.x258 - m.x267 - m.x420 + m.x421 == 0)

m.c99 = Constraint(expr=m.x460/m.x475*(m.x470 - m.x469) - m.x259 - m.x268 - m.x421 + m.x422 == 0)

m.c100 = Constraint(expr=m.x460/m.x475*(m.x471 - m.x470) - m.x260 - m.x269 - m.x422 + m.x423 == 0)

m.c101 = Constraint(expr= - m.x279 + m.x288 + m.x297 + m.x424 - m.x432 == 0)

m.c102 = Constraint(expr= - m.x271 + m.x280 + m.x289 - m.x424 + m.x425 == 0)

m.c103 = Constraint(expr= - m.x272 + m.x281 + m.x290 - m.x425 + m.x426 == 0)

m.c104 = Constraint(expr= - m.x273 + m.x282 + m.x291 - m.x426 + m.x427 == 0)

m.c105 = Constraint(expr= - m.x274 + m.x283 + m.x292 - m.x427 + m.x428 == 0)

m.c106 = Constraint(expr= - m.x275 + m.x284 + m.x293 - m.x428 + m.x429 == 0)

m.c107 = Constraint(expr= - m.x276 + m.x285 + m.x294 - m.x429 + m.x430 == 0)

m.c108 = Constraint(expr= - m.x277 + m.x286 + m.x295 - m.x430 + m.x431 == 0)

m.c109 = Constraint(expr= - m.x278 + m.x287 + m.x296 - m.x431 + m.x432 == 0)

m.c110 = Constraint(expr=m.x461/m.x475*(m.x475 - m.x471) - m.x288 - m.x297 + m.x433 - m.x441 == 0)

m.c111 = Constraint(expr=m.x461/m.x475*(m.x464 - m.x463) - m.x280 - m.x289 - m.x433 + m.x434 == 0)

m.c112 = Constraint(expr=m.x461/m.x475*(m.x465 - m.x464) - m.x281 - m.x290 - m.x434 + m.x435 == 0)

m.c113 = Constraint(expr=m.x461/m.x475*(m.x466 - m.x465) - m.x282 - m.x291 - m.x435 + m.x436 == 0)

m.c114 = Constraint(expr=m.x461/m.x475*(m.x467 - m.x466) - m.x283 - m.x292 - m.x436 + m.x437 == 0)

m.c115 = Constraint(expr=m.x461/m.x475*(m.x468 - m.x467) - m.x284 - m.x293 - m.x437 + m.x438 == 0)

m.c116 = Constraint(expr=m.x461/m.x475*(m.x469 - m.x468) - m.x285 - m.x294 - m.x438 + m.x439 == 0)

m.c117 = Constraint(expr=m.x461/m.x475*(m.x470 - m.x469) - m.x286 - m.x295 - m.x439 + m.x440 == 0)

m.c118 = Constraint(expr=m.x461/m.x475*(m.x471 - m.x470) - m.x287 - m.x296 - m.x440 + m.x441 == 0)

m.c119 = Constraint(expr= - m.x306 + m.x315 + m.x324 + m.x442 - m.x450 == 0)

m.c120 = Constraint(expr= - m.x298 + m.x307 + m.x316 - m.x442 + m.x443 == 0)

m.c121 = Constraint(expr= - m.x299 + m.x308 + m.x317 - m.x443 + m.x444 == 0)

m.c122 = Constraint(expr= - m.x300 + m.x309 + m.x318 - m.x444 + m.x445 == 0)

m.c123 = Constraint(expr= - m.x301 + m.x310 + m.x319 - m.x445 + m.x446 == 0)

m.c124 = Constraint(expr= - m.x302 + m.x311 + m.x320 - m.x446 + m.x447 == 0)

m.c125 = Constraint(expr= - m.x303 + m.x312 + m.x321 - m.x447 + m.x448 == 0)

m.c126 = Constraint(expr= - m.x304 + m.x313 + m.x322 - m.x448 + m.x449 == 0)

m.c127 = Constraint(expr= - m.x305 + m.x314 + m.x323 - m.x449 + m.x450 == 0)

m.c128 = Constraint(expr=m.x462/m.x475*(m.x475 - m.x471) - m.x315 - m.x324 + m.x451 - m.x459 == 0)

m.c129 = Constraint(expr=m.x462/m.x475*(m.x464 - m.x463) - m.x307 - m.x316 - m.x451 + m.x452 == 0)

m.c130 = Constraint(expr=m.x462/m.x475*(m.x465 - m.x464) - m.x308 - m.x317 - m.x452 + m.x453 == 0)

m.c131 = Constraint(expr=m.x462/m.x475*(m.x466 - m.x465) - m.x309 - m.x318 - m.x453 + m.x454 == 0)

m.c132 = Constraint(expr=m.x462/m.x475*(m.x467 - m.x466) - m.x310 - m.x319 - m.x454 + m.x455 == 0)

m.c133 = Constraint(expr=m.x462/m.x475*(m.x468 - m.x467) - m.x311 - m.x320 - m.x455 + m.x456 == 0)

m.c134 = Constraint(expr=m.x462/m.x475*(m.x469 - m.x468) - m.x312 - m.x321 - m.x456 + m.x457 == 0)

m.c135 = Constraint(expr=m.x462/m.x475*(m.x470 - m.x469) - m.x313 - m.x322 - m.x457 + m.x458 == 0)

m.c136 = Constraint(expr=m.x462/m.x475*(m.x471 - m.x470) - m.x314 - m.x323 - m.x458 + m.x459 == 0)

m.c137 = Constraint(expr=   m.b1 + m.b28 + m.b55 + m.b82 + m.b91 + m.b100 + m.b109 + m.b118 + m.b127 + m.x325 + m.x334
                          + m.x343 == 1)

m.c138 = Constraint(expr=   m.b10 + m.b37 + m.b64 + m.b136 + m.b145 + m.b154 + m.b163 + m.b172 + m.b181 + m.x352
                          + m.x361 + m.x370 == 1)

m.c139 = Constraint(expr=   m.b19 + m.b46 + m.b73 + m.b190 + m.b199 + m.b208 + m.b217 + m.b226 + m.b235 + m.x379
                          + m.x388 + m.x397 == 1)

m.c140 = Constraint(expr= - 5*m.b82 - 8*m.b91 - 10*m.b100 - 3*m.b109 - 4*m.b118 - 7*m.b127 - 0.00125*m.x244
                          - 0.000833333333333333*m.x271 - 0.001*m.x298 - m.x463 + m.x464 >= 0)

m.c141 = Constraint(expr= - 5*m.b83 - 8*m.b92 - 10*m.b101 - 3*m.b110 - 4*m.b119 - 7*m.b128 - 0.00125*m.x245
                          - 0.000833333333333333*m.x272 - 0.001*m.x299 - m.x464 + m.x465 >= 0)

m.c142 = Constraint(expr= - 5*m.b84 - 8*m.b93 - 10*m.b102 - 3*m.b111 - 4*m.b120 - 7*m.b129 - 0.00125*m.x246
                          - 0.000833333333333333*m.x273 - 0.001*m.x300 - m.x465 + m.x466 >= 0)

m.c143 = Constraint(expr= - 5*m.b85 - 8*m.b94 - 10*m.b103 - 3*m.b112 - 4*m.b121 - 7*m.b130 - 0.00125*m.x247
                          - 0.000833333333333333*m.x274 - 0.001*m.x301 - m.x466 + m.x467 >= 0)

m.c144 = Constraint(expr= - 5*m.b86 - 8*m.b95 - 10*m.b104 - 3*m.b113 - 4*m.b122 - 7*m.b131 - 0.00125*m.x248
                          - 0.000833333333333333*m.x275 - 0.001*m.x302 - m.x467 + m.x468 >= 0)

m.c145 = Constraint(expr= - 5*m.b87 - 8*m.b96 - 10*m.b105 - 3*m.b114 - 4*m.b123 - 7*m.b132 - 0.00125*m.x249
                          - 0.000833333333333333*m.x276 - 0.001*m.x303 - m.x468 + m.x469 >= 0)

m.c146 = Constraint(expr= - 5*m.b88 - 8*m.b97 - 10*m.b106 - 3*m.b115 - 4*m.b124 - 7*m.b133 - 0.00125*m.x250
                          - 0.000833333333333333*m.x277 - 0.001*m.x304 - m.x469 + m.x470 >= 0)

m.c147 = Constraint(expr= - 5*m.b89 - 8*m.b98 - 10*m.b107 - 3*m.b116 - 4*m.b125 - 7*m.b134 - 0.00125*m.x251
                          - 0.000833333333333333*m.x278 - 0.001*m.x305 - m.x470 + m.x471 >= 0)

m.c148 = Constraint(expr= - 5*m.b90 - 8*m.b99 - 10*m.b108 - 3*m.b117 - 4*m.b126 - 7*m.b135 - 0.00125*m.x252
                          - 0.000833333333333333*m.x279 - 0.001*m.x306 - m.x471 + m.x475 >= 0)

m.c149 = Constraint(expr= - 11*m.b136 - m.b145 - 2*m.b154 - 5*m.b163 - 6*m.b172 - m.b181 - 0.00111111111111111*m.x253
                          - 0.00166666666666667*m.x280 - 0.000909090909090909*m.x307 - m.x463 + m.x464 >= 0)

m.c150 = Constraint(expr= - 11*m.b137 - m.b146 - 2*m.b155 - 5*m.b164 - 6*m.b173 - m.b182 - 0.00111111111111111*m.x254
                          - 0.00166666666666667*m.x281 - 0.000909090909090909*m.x308 - m.x464 + m.x465 >= 0)

m.c151 = Constraint(expr= - 11*m.b138 - m.b147 - 2*m.b156 - 5*m.b165 - 6*m.b174 - m.b183 - 0.00111111111111111*m.x255
                          - 0.00166666666666667*m.x282 - 0.000909090909090909*m.x309 - m.x465 + m.x466 >= 0)

m.c152 = Constraint(expr= - 11*m.b139 - m.b148 - 2*m.b157 - 5*m.b166 - 6*m.b175 - m.b184 - 0.00111111111111111*m.x256
                          - 0.00166666666666667*m.x283 - 0.000909090909090909*m.x310 - m.x466 + m.x467 >= 0)

m.c153 = Constraint(expr= - 11*m.b140 - m.b149 - 2*m.b158 - 5*m.b167 - 6*m.b176 - m.b185 - 0.00111111111111111*m.x257
                          - 0.00166666666666667*m.x284 - 0.000909090909090909*m.x311 - m.x467 + m.x468 >= 0)

m.c154 = Constraint(expr= - 11*m.b141 - m.b150 - 2*m.b159 - 5*m.b168 - 6*m.b177 - m.b186 - 0.00111111111111111*m.x258
                          - 0.00166666666666667*m.x285 - 0.000909090909090909*m.x312 - m.x468 + m.x469 >= 0)

m.c155 = Constraint(expr= - 11*m.b142 - m.b151 - 2*m.b160 - 5*m.b169 - 6*m.b178 - m.b187 - 0.00111111111111111*m.x259
                          - 0.00166666666666667*m.x286 - 0.000909090909090909*m.x313 - m.x469 + m.x470 >= 0)

m.c156 = Constraint(expr= - 11*m.b143 - m.b152 - 2*m.b161 - 5*m.b170 - 6*m.b179 - m.b188 - 0.00111111111111111*m.x260
                          - 0.00166666666666667*m.x287 - 0.000909090909090909*m.x314 - m.x470 + m.x471 >= 0)

m.c157 = Constraint(expr= - 11*m.b144 - m.b153 - 2*m.b162 - 5*m.b171 - 6*m.b180 - m.b189 - 0.00111111111111111*m.x261
                          - 0.00166666666666667*m.x288 - 0.000909090909090909*m.x315 - m.x471 + m.x475 >= 0)

m.c158 = Constraint(expr= - 9*m.b190 - 11*m.b199 - 5*m.b208 - 7*m.b217 - 6*m.b226 - 4*m.b235 - 0.0025*m.x262
                          - 0.002*m.x289 - 0.00222222222222222*m.x316 - m.x463 + m.x464 >= 0)

m.c159 = Constraint(expr= - 9*m.b191 - 11*m.b200 - 5*m.b209 - 7*m.b218 - 6*m.b227 - 4*m.b236 - 0.0025*m.x263
                          - 0.002*m.x290 - 0.00222222222222222*m.x317 - m.x464 + m.x465 >= 0)

m.c160 = Constraint(expr= - 9*m.b192 - 11*m.b201 - 5*m.b210 - 7*m.b219 - 6*m.b228 - 4*m.b237 - 0.0025*m.x264
                          - 0.002*m.x291 - 0.00222222222222222*m.x318 - m.x465 + m.x466 >= 0)

m.c161 = Constraint(expr= - 9*m.b193 - 11*m.b202 - 5*m.b211 - 7*m.b220 - 6*m.b229 - 4*m.b238 - 0.0025*m.x265
                          - 0.002*m.x292 - 0.00222222222222222*m.x319 - m.x466 + m.x467 >= 0)

m.c162 = Constraint(expr= - 9*m.b194 - 11*m.b203 - 5*m.b212 - 7*m.b221 - 6*m.b230 - 4*m.b239 - 0.0025*m.x266
                          - 0.002*m.x293 - 0.00222222222222222*m.x320 - m.x467 + m.x468 >= 0)

m.c163 = Constraint(expr= - 9*m.b195 - 11*m.b204 - 5*m.b213 - 7*m.b222 - 6*m.b231 - 4*m.b240 - 0.0025*m.x267
                          - 0.002*m.x294 - 0.00222222222222222*m.x321 - m.x468 + m.x469 >= 0)

m.c164 = Constraint(expr= - 9*m.b196 - 11*m.b205 - 5*m.b214 - 7*m.b223 - 6*m.b232 - 4*m.b241 - 0.0025*m.x268
                          - 0.002*m.x295 - 0.00222222222222222*m.x322 - m.x469 + m.x470 >= 0)

m.c165 = Constraint(expr= - 9*m.b197 - 11*m.b206 - 5*m.b215 - 7*m.b224 - 6*m.b233 - 4*m.b242 - 0.0025*m.x269
                          - 0.002*m.x296 - 0.00222222222222222*m.x323 - m.x470 + m.x471 >= 0)

m.c166 = Constraint(expr= - 9*m.b198 - 11*m.b207 - 5*m.b216 - 7*m.b225 - 6*m.b234 - 4*m.b243 - 0.0025*m.x270
                          - 0.002*m.x297 - 0.00222222222222222*m.x324 - m.x471 + m.x475 >= 0)

m.c167 = Constraint(expr= - 480000*m.b1 + m.x244 <= 0)

m.c168 = Constraint(expr= - 480000*m.b2 + m.x245 <= 0)

m.c169 = Constraint(expr= - 480000*m.b3 + m.x246 <= 0)

m.c170 = Constraint(expr= - 480000*m.b4 + m.x247 <= 0)

m.c171 = Constraint(expr= - 480000*m.b5 + m.x248 <= 0)

m.c172 = Constraint(expr= - 480000*m.b6 + m.x249 <= 0)

m.c173 = Constraint(expr= - 480000*m.b7 + m.x250 <= 0)

m.c174 = Constraint(expr= - 480000*m.b8 + m.x251 <= 0)

m.c175 = Constraint(expr= - 480000*m.b9 + m.x252 <= 0)

m.c176 = Constraint(expr= - 540000*m.b10 + m.x253 <= 0)

m.c177 = Constraint(expr= - 540000*m.b11 + m.x254 <= 0)

m.c178 = Constraint(expr= - 540000*m.b12 + m.x255 <= 0)

m.c179 = Constraint(expr= - 540000*m.b13 + m.x256 <= 0)

m.c180 = Constraint(expr= - 540000*m.b14 + m.x257 <= 0)

m.c181 = Constraint(expr= - 540000*m.b15 + m.x258 <= 0)

m.c182 = Constraint(expr= - 540000*m.b16 + m.x259 <= 0)

m.c183 = Constraint(expr= - 540000*m.b17 + m.x260 <= 0)

m.c184 = Constraint(expr= - 540000*m.b18 + m.x261 <= 0)

m.c185 = Constraint(expr= - 240000*m.b19 + m.x262 <= 0)

m.c186 = Constraint(expr= - 240000*m.b20 + m.x263 <= 0)

m.c187 = Constraint(expr= - 240000*m.b21 + m.x264 <= 0)

m.c188 = Constraint(expr= - 240000*m.b22 + m.x265 <= 0)

m.c189 = Constraint(expr= - 240000*m.b23 + m.x266 <= 0)

m.c190 = Constraint(expr= - 240000*m.b24 + m.x267 <= 0)

m.c191 = Constraint(expr= - 240000*m.b25 + m.x268 <= 0)

m.c192 = Constraint(expr= - 240000*m.b26 + m.x269 <= 0)

m.c193 = Constraint(expr= - 240000*m.b27 + m.x270 <= 0)

m.c194 = Constraint(expr= - 720000*m.b28 + m.x271 <= 0)

m.c195 = Constraint(expr= - 720000*m.b29 + m.x272 <= 0)

m.c196 = Constraint(expr= - 720000*m.b30 + m.x273 <= 0)

m.c197 = Constraint(expr= - 720000*m.b31 + m.x274 <= 0)

m.c198 = Constraint(expr= - 720000*m.b32 + m.x275 <= 0)

m.c199 = Constraint(expr= - 720000*m.b33 + m.x276 <= 0)

m.c200 = Constraint(expr= - 720000*m.b34 + m.x277 <= 0)

m.c201 = Constraint(expr= - 720000*m.b35 + m.x278 <= 0)

m.c202 = Constraint(expr= - 720000*m.b36 + m.x279 <= 0)

m.c203 = Constraint(expr= - 360000*m.b37 + m.x280 <= 0)

m.c204 = Constraint(expr= - 360000*m.b38 + m.x281 <= 0)

m.c205 = Constraint(expr= - 360000*m.b39 + m.x282 <= 0)

m.c206 = Constraint(expr= - 360000*m.b40 + m.x283 <= 0)

m.c207 = Constraint(expr= - 360000*m.b41 + m.x284 <= 0)

m.c208 = Constraint(expr= - 360000*m.b42 + m.x285 <= 0)

m.c209 = Constraint(expr= - 360000*m.b43 + m.x286 <= 0)

m.c210 = Constraint(expr= - 360000*m.b44 + m.x287 <= 0)

m.c211 = Constraint(expr= - 360000*m.b45 + m.x288 <= 0)

m.c212 = Constraint(expr= - 300000*m.b46 + m.x289 <= 0)

m.c213 = Constraint(expr= - 300000*m.b47 + m.x290 <= 0)

m.c214 = Constraint(expr= - 300000*m.b48 + m.x291 <= 0)

m.c215 = Constraint(expr= - 300000*m.b49 + m.x292 <= 0)

m.c216 = Constraint(expr= - 300000*m.b50 + m.x293 <= 0)

m.c217 = Constraint(expr= - 300000*m.b51 + m.x294 <= 0)

m.c218 = Constraint(expr= - 300000*m.b52 + m.x295 <= 0)

m.c219 = Constraint(expr= - 300000*m.b53 + m.x296 <= 0)

m.c220 = Constraint(expr= - 300000*m.b54 + m.x297 <= 0)

m.c221 = Constraint(expr= - 600000*m.b55 + m.x298 <= 0)

m.c222 = Constraint(expr= - 600000*m.b56 + m.x299 <= 0)

m.c223 = Constraint(expr= - 600000*m.b57 + m.x300 <= 0)

m.c224 = Constraint(expr= - 600000*m.b58 + m.x301 <= 0)

m.c225 = Constraint(expr= - 600000*m.b59 + m.x302 <= 0)

m.c226 = Constraint(expr= - 600000*m.b60 + m.x303 <= 0)

m.c227 = Constraint(expr= - 600000*m.b61 + m.x304 <= 0)

m.c228 = Constraint(expr= - 600000*m.b62 + m.x305 <= 0)

m.c229 = Constraint(expr= - 600000*m.b63 + m.x306 <= 0)

m.c230 = Constraint(expr= - 660000*m.b64 + m.x307 <= 0)

m.c231 = Constraint(expr= - 660000*m.b65 + m.x308 <= 0)

m.c232 = Constraint(expr= - 660000*m.b66 + m.x309 <= 0)

m.c233 = Constraint(expr= - 660000*m.b67 + m.x310 <= 0)

m.c234 = Constraint(expr= - 660000*m.b68 + m.x311 <= 0)

m.c235 = Constraint(expr= - 660000*m.b69 + m.x312 <= 0)

m.c236 = Constraint(expr= - 660000*m.b70 + m.x313 <= 0)

m.c237 = Constraint(expr= - 660000*m.b71 + m.x314 <= 0)

m.c238 = Constraint(expr= - 660000*m.b72 + m.x315 <= 0)

m.c239 = Constraint(expr= - 270000*m.b73 + m.x316 <= 0)

m.c240 = Constraint(expr= - 270000*m.b74 + m.x317 <= 0)

m.c241 = Constraint(expr= - 270000*m.b75 + m.x318 <= 0)

m.c242 = Constraint(expr= - 270000*m.b76 + m.x319 <= 0)

m.c243 = Constraint(expr= - 270000*m.b77 + m.x320 <= 0)

m.c244 = Constraint(expr= - 270000*m.b78 + m.x321 <= 0)

m.c245 = Constraint(expr= - 270000*m.b79 + m.x322 <= 0)

m.c246 = Constraint(expr= - 270000*m.b80 + m.x323 <= 0)

m.c247 = Constraint(expr= - 270000*m.b81 + m.x324 <= 0)

m.c248 = Constraint(expr=   m.x460 - 50*m.x475 >= 0)

m.c249 = Constraint(expr=   m.x461 - 100*m.x475 >= 0)

m.c250 = Constraint(expr=   m.x462 - 250*m.x475 >= 0)

m.c251 = Constraint(expr=   m.x406 - m.x472 <= 0)

m.c252 = Constraint(expr=   m.x407 - m.x472 <= 0)

m.c253 = Constraint(expr=   m.x408 - m.x472 <= 0)

m.c254 = Constraint(expr=   m.x409 - m.x472 <= 0)

m.c255 = Constraint(expr=   m.x410 - m.x472 <= 0)

m.c256 = Constraint(expr=   m.x411 - m.x472 <= 0)

m.c257 = Constraint(expr=   m.x412 - m.x472 <= 0)

m.c258 = Constraint(expr=   m.x413 - m.x472 <= 0)

m.c259 = Constraint(expr=   m.x414 - m.x472 <= 0)

m.c260 = Constraint(expr=   m.x424 - m.x473 <= 0)

m.c261 = Constraint(expr=   m.x425 - m.x473 <= 0)

m.c262 = Constraint(expr=   m.x426 - m.x473 <= 0)

m.c263 = Constraint(expr=   m.x427 - m.x473 <= 0)

m.c264 = Constraint(expr=   m.x428 - m.x473 <= 0)

m.c265 = Constraint(expr=   m.x429 - m.x473 <= 0)

m.c266 = Constraint(expr=   m.x430 - m.x473 <= 0)

m.c267 = Constraint(expr=   m.x431 - m.x473 <= 0)

m.c268 = Constraint(expr=   m.x432 - m.x473 <= 0)

m.c269 = Constraint(expr=   m.x442 - m.x474 <= 0)

m.c270 = Constraint(expr=   m.x443 - m.x474 <= 0)

m.c271 = Constraint(expr=   m.x444 - m.x474 <= 0)

m.c272 = Constraint(expr=   m.x445 - m.x474 <= 0)

m.c273 = Constraint(expr=   m.x446 - m.x474 <= 0)

m.c274 = Constraint(expr=   m.x447 - m.x474 <= 0)

m.c275 = Constraint(expr=   m.x448 - m.x474 <= 0)

m.c276 = Constraint(expr=   m.x449 - m.x474 <= 0)

m.c277 = Constraint(expr=   m.x450 - m.x474 <= 0)

m.c278 = Constraint(expr=   m.b82 + m.b83 + m.b84 + m.b85 + m.b86 + m.b87 + m.b88 + m.b89 + m.b90 + m.b91 + m.b92
                          + m.b93 + m.b94 + m.b95 + m.b96 + m.b97 + m.b98 + m.b99 + m.b100 + m.b101 + m.b102 + m.b103
                          + m.b104 + m.b105 + m.b106 + m.b107 + m.b108 + m.b109 + m.b110 + m.b111 + m.b112 + m.b113
                          + m.b114 + m.b115 + m.b116 + m.b117 + m.b118 + m.b119 + m.b120 + m.b121 + m.b122 + m.b123
                          + m.b124 + m.b125 + m.b126 + m.b127 + m.b128 + m.b129 + m.b130 + m.b131 + m.b132 + m.b133
                          + m.b134 + m.b135 <= 3)

m.c279 = Constraint(expr=   m.b136 + m.b137 + m.b138 + m.b139 + m.b140 + m.b141 + m.b142 + m.b143 + m.b144 + m.b145
                          + m.b146 + m.b147 + m.b148 + m.b149 + m.b150 + m.b151 + m.b152 + m.b153 + m.b154 + m.b155
                          + m.b156 + m.b157 + m.b158 + m.b159 + m.b160 + m.b161 + m.b162 + m.b163 + m.b164 + m.b165
                          + m.b166 + m.b167 + m.b168 + m.b169 + m.b170 + m.b171 + m.b172 + m.b173 + m.b174 + m.b175
                          + m.b176 + m.b177 + m.b178 + m.b179 + m.b180 + m.b181 + m.b182 + m.b183 + m.b184 + m.b185
                          + m.b186 + m.b187 + m.b188 + m.b189 + m.b190 + m.b191 + m.b192 + m.b193 + m.b194 + m.b195
                          + m.b196 + m.b197 + m.b198 + m.b199 + m.b200 + m.b201 + m.b202 + m.b203 + m.b204 + m.b205
                          + m.b206 + m.b207 + m.b208 + m.b209 + m.b210 + m.b211 + m.b212 + m.b213 + m.b214 + m.b215
                          + m.b216 + m.b217 + m.b218 + m.b219 + m.b220 + m.b221 + m.b222 + m.b223 + m.b224 + m.b225
                          + m.b226 + m.b227 + m.b228 + m.b229 + m.b230 + m.b231 + m.b232 + m.b233 + m.b234 + m.b235
                          + m.b236 + m.b237 + m.b238 + m.b239 + m.b240 + m.b241 + m.b242 + m.b243 <= 3)

m.c280 = Constraint(expr=   m.b1 == 1)
