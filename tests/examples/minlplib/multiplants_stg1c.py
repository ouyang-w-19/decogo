#  MINLP written by GAMS Convert at 04/21/18 13:52:37
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        270      132       31      107        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        477      225      252        0        0        0        0        0
#  FX     85       85        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1909     1798      111        0


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
m.b244 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b245 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b246 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b247 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b248 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b249 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b250 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b251 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b252 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x255 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x258 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x262 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x263 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x264 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x265 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x266 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x267 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x268 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x269 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x270 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x271 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x272 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x273 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x274 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x275 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x276 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x277 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x278 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x279 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x280 = Var(within=Reals,bounds=(0,240000),initialize=0)
m.x281 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x282 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x283 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x284 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x285 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x286 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x287 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x289 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x290 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x291 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x292 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x293 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x294 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x295 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x296 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x297 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x298 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x299 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x300 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x301 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x302 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x303 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x304 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x305 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x306 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x307 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,300000),initialize=0)
m.x309 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x311 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x312 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x313 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x314 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x315 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x316 = Var(within=Reals,bounds=(0,270000),initialize=0)
m.x317 = Var(within=Reals,bounds=(0,270000),initialize=0)
m.x318 = Var(within=Reals,bounds=(0,270000),initialize=0)
m.x319 = Var(within=Reals,bounds=(0,270000),initialize=0)
m.x320 = Var(within=Reals,bounds=(0,270000),initialize=0)
m.x321 = Var(within=Reals,bounds=(0,270000),initialize=0)
m.x322 = Var(within=Reals,bounds=(0,270000),initialize=0)
m.x323 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x324 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x325 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x326 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x327 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x328 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x329 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x330 = Var(within=Reals,bounds=(0,270000),initialize=0)
m.x331 = Var(within=Reals,bounds=(0,270000),initialize=0)
m.x332 = Var(within=Reals,bounds=(0,270000),initialize=0)
m.x333 = Var(within=Reals,bounds=(0,270000),initialize=0)
m.x334 = Var(within=Reals,bounds=(0,270000),initialize=0)
m.x335 = Var(within=Reals,bounds=(0,270000),initialize=0)
m.x336 = Var(within=Reals,bounds=(0,270000),initialize=0)
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
m.x406 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x407 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x408 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x409 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x410 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x411 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x412 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x413 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x414 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x415 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x416 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x417 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x418 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x419 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x420 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x421 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x422 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x423 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x424 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x425 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x426 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x427 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x428 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x429 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x430 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x431 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x432 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x433 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x434 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x435 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x436 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x437 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x438 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x439 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x440 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x441 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x442 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x443 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x444 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x445 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x446 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x447 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x448 = Var(within=Reals,bounds=(0,360000),initialize=0)
m.x449 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x450 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x451 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x452 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x453 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x454 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x455 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x456 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x457 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x458 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x459 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x460 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x461 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x462 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x463 = Var(within=Reals,bounds=(0,540000),initialize=0)
m.x464 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x465 = Var(within=Reals,bounds=(0,660000),initialize=0)
m.x466 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x467 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x468 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x469 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x470 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x471 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x472 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x473 = Var(within=Reals,bounds=(0,480000),initialize=0)
m.x474 = Var(within=Reals,bounds=(0,720000),initialize=0)
m.x475 = Var(within=Reals,bounds=(0,600000),initialize=0)
m.x476 = Var(within=Reals,bounds=(200,600),initialize=200)
m.x477 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x477, sense=maximize)

m.c1 = Constraint(expr=m.x477*m.x476 + (0.00203*m.x428 + 0.00203*m.x429)*(m.x467 - m.x466) + (0.00203*m.x429 + 0.00203*
                       m.x430)*(m.x468 - m.x467) + (0.00203*m.x430 + 0.00203*m.x431)*(m.x469 - m.x468) + (0.00203*m.x431
                        + 0.00203*m.x432)*(m.x470 - m.x469) + (0.00203*m.x432 + 0.00203*m.x433)*(m.x471 - m.x470) + (
                       0.00203*m.x433 + 0.00203*m.x434)*(m.x472 - m.x471) + (0.00203*m.x428 + 0.00203*m.x434)*(m.x476 - 
                       m.x472) + (0.00203*m.x442 + 0.00203*m.x443)*(m.x467 - m.x466) + (0.00203*m.x443 + 0.00203*m.x444)
                       *(m.x468 - m.x467) + (0.00203*m.x444 + 0.00203*m.x445)*(m.x469 - m.x468) + (0.00203*m.x445 + 
                       0.00203*m.x446)*(m.x470 - m.x469) + (0.00203*m.x446 + 0.00203*m.x447)*(m.x471 - m.x470) + (
                       0.00203*m.x447 + 0.00203*m.x448)*(m.x472 - m.x471) + (0.00203*m.x442 + 0.00203*m.x448)*(m.x476 - 
                       m.x472) + (0.00203*m.x456 + 0.00203*m.x457)*(m.x467 - m.x466) + (0.00203*m.x457 + 0.00203*m.x458)
                       *(m.x468 - m.x467) + (0.00203*m.x458 + 0.00203*m.x459)*(m.x469 - m.x468) + (0.00203*m.x459 + 
                       0.00203*m.x460)*(m.x470 - m.x469) + (0.00203*m.x460 + 0.00203*m.x461)*(m.x471 - m.x470) + (
                       0.00203*m.x461 + 0.00203*m.x462)*(m.x472 - m.x471) + (0.00203*m.x456 + 0.00203*m.x462)*(m.x476 - 
                       m.x472) + 3800*m.b85 + 3800*m.b86 + 3800*m.b87 + 3800*m.b88 + 3800*m.b89 + 3800*m.b90
                        + 3800*m.b91 + 6080*m.b92 + 6080*m.b93 + 6080*m.b94 + 6080*m.b95 + 6080*m.b96 + 6080*m.b97
                        + 6080*m.b98 + 7500*m.b99 + 7500*m.b100 + 7500*m.b101 + 7500*m.b102 + 7500*m.b103 + 7500*m.b104
                        + 7500*m.b105 + 2250*m.b106 + 2250*m.b107 + 2250*m.b108 + 2250*m.b109 + 2250*m.b110
                        + 2250*m.b111 + 2250*m.b112 + 3080*m.b113 + 3080*m.b114 + 3080*m.b115 + 3080*m.b116
                        + 3080*m.b117 + 3080*m.b118 + 3080*m.b119 + 5390*m.b120 + 5390*m.b121 + 5390*m.b122
                        + 5390*m.b123 + 5390*m.b124 + 5390*m.b125 + 5390*m.b126 + 6840*m.b127 + 6840*m.b128
                        + 6840*m.b129 + 6840*m.b130 + 6840*m.b131 + 6840*m.b132 + 6840*m.b133 + 8360*m.b134
                        + 8360*m.b135 + 8360*m.b136 + 8360*m.b137 + 8360*m.b138 + 8360*m.b139 + 8360*m.b140
                        + 3750*m.b141 + 3750*m.b142 + 3750*m.b143 + 3750*m.b144 + 3750*m.b145 + 3750*m.b146
                        + 3750*m.b147 + 5250*m.b148 + 5250*m.b149 + 5250*m.b150 + 5250*m.b151 + 5250*m.b152
                        + 5250*m.b153 + 5250*m.b154 + 4620*m.b155 + 4620*m.b156 + 4620*m.b157 + 4620*m.b158
                        + 4620*m.b159 + 4620*m.b160 + 4620*m.b161 + 3080*m.b162 + 3080*m.b163 + 3080*m.b164
                        + 3080*m.b165 + 3080*m.b166 + 3080*m.b167 + 3080*m.b168 + 8360*m.b169 + 8360*m.b170
                        + 8360*m.b171 + 8360*m.b172 + 8360*m.b173 + 8360*m.b174 + 8360*m.b175 + 760*m.b176 + 760*m.b177
                        + 760*m.b178 + 760*m.b179 + 760*m.b180 + 760*m.b181 + 760*m.b182 + 1500*m.b183 + 1500*m.b184
                        + 1500*m.b185 + 1500*m.b186 + 1500*m.b187 + 1500*m.b188 + 1500*m.b189 + 3750*m.b190
                        + 3750*m.b191 + 3750*m.b192 + 3750*m.b193 + 3750*m.b194 + 3750*m.b195 + 3750*m.b196
                        + 4620*m.b197 + 4620*m.b198 + 4620*m.b199 + 4620*m.b200 + 4620*m.b201 + 4620*m.b202
                        + 4620*m.b203 + 770*m.b204 + 770*m.b205 + 770*m.b206 + 770*m.b207 + 770*m.b208 + 770*m.b209
                        + 770*m.b210 + 6840*m.b211 + 6840*m.b212 + 6840*m.b213 + 6840*m.b214 + 6840*m.b215 + 6840*m.b216
                        + 6840*m.b217 + 8360*m.b218 + 8360*m.b219 + 8360*m.b220 + 8360*m.b221 + 8360*m.b222
                        + 8360*m.b223 + 8360*m.b224 + 3750*m.b225 + 3750*m.b226 + 3750*m.b227 + 3750*m.b228
                        + 3750*m.b229 + 3750*m.b230 + 3750*m.b231 + 5250*m.b232 + 5250*m.b233 + 5250*m.b234
                        + 5250*m.b235 + 5250*m.b236 + 5250*m.b237 + 5250*m.b238 + 4620*m.b239 + 4620*m.b240
                        + 4620*m.b241 + 4620*m.b242 + 4620*m.b243 + 4620*m.b244 + 4620*m.b245 + 3080*m.b246
                        + 3080*m.b247 + 3080*m.b248 + 3080*m.b249 + 3080*m.b250 + 3080*m.b251 + 3080*m.b252
                        - 0.15*m.x463 - 0.4*m.x464 - 0.65*m.x465 + 0.1406*m.x473 + 0.1406*m.x474 + 0.1406*m.x475 == 0)

m.c2 = Constraint(expr=   m.b1 - m.b7 + m.b85 + m.b92 - m.b105 - m.b119 + m.x337 - m.x343 == 0)

m.c3 = Constraint(expr= - m.b1 + m.b2 + m.b86 + m.b93 - m.b99 - m.b113 - m.x337 + m.x338 == 0)

m.c4 = Constraint(expr= - m.b2 + m.b3 + m.b87 + m.b94 - m.b100 - m.b114 - m.x338 + m.x339 == 0)

m.c5 = Constraint(expr= - m.b3 + m.b4 + m.b88 + m.b95 - m.b101 - m.b115 - m.x339 + m.x340 == 0)

m.c6 = Constraint(expr= - m.b4 + m.b5 + m.b89 + m.b96 - m.b102 - m.b116 - m.x340 + m.x341 == 0)

m.c7 = Constraint(expr= - m.b5 + m.b6 + m.b90 + m.b97 - m.b103 - m.b117 - m.x341 + m.x342 == 0)

m.c8 = Constraint(expr= - m.b6 + m.b7 + m.b91 + m.b98 - m.b104 - m.b118 - m.x342 + m.x343 == 0)

m.c9 = Constraint(expr=   m.b29 - m.b35 - m.b91 + m.b99 + m.b106 - m.b126 + m.x344 - m.x350 == 0)

m.c10 = Constraint(expr= - m.b29 + m.b30 - m.b85 + m.b100 + m.b107 - m.b120 - m.x344 + m.x345 == 0)

m.c11 = Constraint(expr= - m.b30 + m.b31 - m.b86 + m.b101 + m.b108 - m.b121 - m.x345 + m.x346 == 0)

m.c12 = Constraint(expr= - m.b31 + m.b32 - m.b87 + m.b102 + m.b109 - m.b122 - m.x346 + m.x347 == 0)

m.c13 = Constraint(expr= - m.b32 + m.b33 - m.b88 + m.b103 + m.b110 - m.b123 - m.x347 + m.x348 == 0)

m.c14 = Constraint(expr= - m.b33 + m.b34 - m.b89 + m.b104 + m.b111 - m.b124 - m.x348 + m.x349 == 0)

m.c15 = Constraint(expr= - m.b34 + m.b35 - m.b90 + m.b105 + m.b112 - m.b125 - m.x349 + m.x350 == 0)

m.c16 = Constraint(expr=   m.b57 - m.b63 - m.b98 - m.b112 + m.b113 + m.b120 + m.x351 - m.x357 == 0)

m.c17 = Constraint(expr= - m.b57 + m.b58 - m.b92 - m.b106 + m.b114 + m.b121 - m.x351 + m.x352 == 0)

m.c18 = Constraint(expr= - m.b58 + m.b59 - m.b93 - m.b107 + m.b115 + m.b122 - m.x352 + m.x353 == 0)

m.c19 = Constraint(expr= - m.b59 + m.b60 - m.b94 - m.b108 + m.b116 + m.b123 - m.x353 + m.x354 == 0)

m.c20 = Constraint(expr= - m.b60 + m.b61 - m.b95 - m.b109 + m.b117 + m.b124 - m.x354 + m.x355 == 0)

m.c21 = Constraint(expr= - m.b61 + m.b62 - m.b96 - m.b110 + m.b118 + m.b125 - m.x355 + m.x356 == 0)

m.c22 = Constraint(expr= - m.b62 + m.b63 - m.b97 - m.b111 + m.b119 + m.b126 - m.x356 + m.x357 == 0)

m.c23 = Constraint(expr=   m.b8 - m.b14 + m.b127 + m.b134 - m.b147 - m.b161 + m.x358 - m.x364 == 0)

m.c24 = Constraint(expr= - m.b8 + m.b9 + m.b128 + m.b135 - m.b141 - m.b155 - m.x358 + m.x359 == 0)

m.c25 = Constraint(expr= - m.b9 + m.b10 + m.b129 + m.b136 - m.b142 - m.b156 - m.x359 + m.x360 == 0)

m.c26 = Constraint(expr= - m.b10 + m.b11 + m.b130 + m.b137 - m.b143 - m.b157 - m.x360 + m.x361 == 0)

m.c27 = Constraint(expr= - m.b11 + m.b12 + m.b131 + m.b138 - m.b144 - m.b158 - m.x361 + m.x362 == 0)

m.c28 = Constraint(expr= - m.b12 + m.b13 + m.b132 + m.b139 - m.b145 - m.b159 - m.x362 + m.x363 == 0)

m.c29 = Constraint(expr= - m.b13 + m.b14 + m.b133 + m.b140 - m.b146 - m.b160 - m.x363 + m.x364 == 0)

m.c30 = Constraint(expr=   m.b36 - m.b42 - m.b133 + m.b141 + m.b148 - m.b168 + m.x365 - m.x371 == 0)

m.c31 = Constraint(expr= - m.b36 + m.b37 - m.b127 + m.b142 + m.b149 - m.b162 - m.x365 + m.x366 == 0)

m.c32 = Constraint(expr= - m.b37 + m.b38 - m.b128 + m.b143 + m.b150 - m.b163 - m.x366 + m.x367 == 0)

m.c33 = Constraint(expr= - m.b38 + m.b39 - m.b129 + m.b144 + m.b151 - m.b164 - m.x367 + m.x368 == 0)

m.c34 = Constraint(expr= - m.b39 + m.b40 - m.b130 + m.b145 + m.b152 - m.b165 - m.x368 + m.x369 == 0)

m.c35 = Constraint(expr= - m.b40 + m.b41 - m.b131 + m.b146 + m.b153 - m.b166 - m.x369 + m.x370 == 0)

m.c36 = Constraint(expr= - m.b41 + m.b42 - m.b132 + m.b147 + m.b154 - m.b167 - m.x370 + m.x371 == 0)

m.c37 = Constraint(expr=   m.b64 - m.b70 - m.b140 - m.b154 + m.b155 + m.b162 + m.x372 - m.x378 == 0)

m.c38 = Constraint(expr= - m.b64 + m.b65 - m.b134 - m.b148 + m.b156 + m.b163 - m.x372 + m.x373 == 0)

m.c39 = Constraint(expr= - m.b65 + m.b66 - m.b135 - m.b149 + m.b157 + m.b164 - m.x373 + m.x374 == 0)

m.c40 = Constraint(expr= - m.b66 + m.b67 - m.b136 - m.b150 + m.b158 + m.b165 - m.x374 + m.x375 == 0)

m.c41 = Constraint(expr= - m.b67 + m.b68 - m.b137 - m.b151 + m.b159 + m.b166 - m.x375 + m.x376 == 0)

m.c42 = Constraint(expr= - m.b68 + m.b69 - m.b138 - m.b152 + m.b160 + m.b167 - m.x376 + m.x377 == 0)

m.c43 = Constraint(expr= - m.b69 + m.b70 - m.b139 - m.b153 + m.b161 + m.b168 - m.x377 + m.x378 == 0)

m.c44 = Constraint(expr=   m.b15 - m.b21 + m.b169 + m.b176 - m.b189 - m.b203 + m.x379 - m.x385 == 0)

m.c45 = Constraint(expr= - m.b15 + m.b16 + m.b170 + m.b177 - m.b183 - m.b197 - m.x379 + m.x380 == 0)

m.c46 = Constraint(expr= - m.b16 + m.b17 + m.b171 + m.b178 - m.b184 - m.b198 - m.x380 + m.x381 == 0)

m.c47 = Constraint(expr= - m.b17 + m.b18 + m.b172 + m.b179 - m.b185 - m.b199 - m.x381 + m.x382 == 0)

m.c48 = Constraint(expr= - m.b18 + m.b19 + m.b173 + m.b180 - m.b186 - m.b200 - m.x382 + m.x383 == 0)

m.c49 = Constraint(expr= - m.b19 + m.b20 + m.b174 + m.b181 - m.b187 - m.b201 - m.x383 + m.x384 == 0)

m.c50 = Constraint(expr= - m.b20 + m.b21 + m.b175 + m.b182 - m.b188 - m.b202 - m.x384 + m.x385 == 0)

m.c51 = Constraint(expr=   m.b43 - m.b49 - m.b175 + m.b183 + m.b190 - m.b210 + m.x386 - m.x392 == 0)

m.c52 = Constraint(expr= - m.b43 + m.b44 - m.b169 + m.b184 + m.b191 - m.b204 - m.x386 + m.x387 == 0)

m.c53 = Constraint(expr= - m.b44 + m.b45 - m.b170 + m.b185 + m.b192 - m.b205 - m.x387 + m.x388 == 0)

m.c54 = Constraint(expr= - m.b45 + m.b46 - m.b171 + m.b186 + m.b193 - m.b206 - m.x388 + m.x389 == 0)

m.c55 = Constraint(expr= - m.b46 + m.b47 - m.b172 + m.b187 + m.b194 - m.b207 - m.x389 + m.x390 == 0)

m.c56 = Constraint(expr= - m.b47 + m.b48 - m.b173 + m.b188 + m.b195 - m.b208 - m.x390 + m.x391 == 0)

m.c57 = Constraint(expr= - m.b48 + m.b49 - m.b174 + m.b189 + m.b196 - m.b209 - m.x391 + m.x392 == 0)

m.c58 = Constraint(expr=   m.b71 - m.b77 - m.b182 - m.b196 + m.b197 + m.b204 + m.x393 - m.x399 == 0)

m.c59 = Constraint(expr= - m.b71 + m.b72 - m.b176 - m.b190 + m.b198 + m.b205 - m.x393 + m.x394 == 0)

m.c60 = Constraint(expr= - m.b72 + m.b73 - m.b177 - m.b191 + m.b199 + m.b206 - m.x394 + m.x395 == 0)

m.c61 = Constraint(expr= - m.b73 + m.b74 - m.b178 - m.b192 + m.b200 + m.b207 - m.x395 + m.x396 == 0)

m.c62 = Constraint(expr= - m.b74 + m.b75 - m.b179 - m.b193 + m.b201 + m.b208 - m.x396 + m.x397 == 0)

m.c63 = Constraint(expr= - m.b75 + m.b76 - m.b180 - m.b194 + m.b202 + m.b209 - m.x397 + m.x398 == 0)

m.c64 = Constraint(expr= - m.b76 + m.b77 - m.b181 - m.b195 + m.b203 + m.b210 - m.x398 + m.x399 == 0)

m.c65 = Constraint(expr=   m.b22 - m.b28 + m.b211 + m.b218 - m.b231 - m.b245 + m.x400 - m.x406 == 0)

m.c66 = Constraint(expr= - m.b22 + m.b23 + m.b212 + m.b219 - m.b225 - m.b239 - m.x400 + m.x401 == 0)

m.c67 = Constraint(expr= - m.b23 + m.b24 + m.b213 + m.b220 - m.b226 - m.b240 - m.x401 + m.x402 == 0)

m.c68 = Constraint(expr= - m.b24 + m.b25 + m.b214 + m.b221 - m.b227 - m.b241 - m.x402 + m.x403 == 0)

m.c69 = Constraint(expr= - m.b25 + m.b26 + m.b215 + m.b222 - m.b228 - m.b242 - m.x403 + m.x404 == 0)

m.c70 = Constraint(expr= - m.b26 + m.b27 + m.b216 + m.b223 - m.b229 - m.b243 - m.x404 + m.x405 == 0)

m.c71 = Constraint(expr= - m.b27 + m.b28 + m.b217 + m.b224 - m.b230 - m.b244 - m.x405 + m.x406 == 0)

m.c72 = Constraint(expr=   m.b50 - m.b56 - m.b217 + m.b225 + m.b232 - m.b252 + m.x407 - m.x413 == 0)

m.c73 = Constraint(expr= - m.b50 + m.b51 - m.b211 + m.b226 + m.b233 - m.b246 - m.x407 + m.x408 == 0)

m.c74 = Constraint(expr= - m.b51 + m.b52 - m.b212 + m.b227 + m.b234 - m.b247 - m.x408 + m.x409 == 0)

m.c75 = Constraint(expr= - m.b52 + m.b53 - m.b213 + m.b228 + m.b235 - m.b248 - m.x409 + m.x410 == 0)

m.c76 = Constraint(expr= - m.b53 + m.b54 - m.b214 + m.b229 + m.b236 - m.b249 - m.x410 + m.x411 == 0)

m.c77 = Constraint(expr= - m.b54 + m.b55 - m.b215 + m.b230 + m.b237 - m.b250 - m.x411 + m.x412 == 0)

m.c78 = Constraint(expr= - m.b55 + m.b56 - m.b216 + m.b231 + m.b238 - m.b251 - m.x412 + m.x413 == 0)

m.c79 = Constraint(expr=   m.b78 - m.b84 - m.b224 - m.b238 + m.b239 + m.b246 + m.x414 - m.x420 == 0)

m.c80 = Constraint(expr= - m.b78 + m.b79 - m.b218 - m.b232 + m.b240 + m.b247 - m.x414 + m.x415 == 0)

m.c81 = Constraint(expr= - m.b79 + m.b80 - m.b219 - m.b233 + m.b241 + m.b248 - m.x415 + m.x416 == 0)

m.c82 = Constraint(expr= - m.b80 + m.b81 - m.b220 - m.b234 + m.b242 + m.b249 - m.x416 + m.x417 == 0)

m.c83 = Constraint(expr= - m.b81 + m.b82 - m.b221 - m.b235 + m.b243 + m.b250 - m.x417 + m.x418 == 0)

m.c84 = Constraint(expr= - m.b82 + m.b83 - m.b222 - m.b236 + m.b244 + m.b251 - m.x418 + m.x419 == 0)

m.c85 = Constraint(expr= - m.b83 + m.b84 - m.b223 - m.b237 + m.b245 + m.b252 - m.x419 + m.x420 == 0)

m.c86 = Constraint(expr= - m.x259 - m.x266 + m.x273 + m.x280 + m.x421 - m.x427 == 0)

m.c87 = Constraint(expr= - m.x253 - m.x260 + m.x267 + m.x274 - m.x421 + m.x422 == 0)

m.c88 = Constraint(expr= - m.x254 - m.x261 + m.x268 + m.x275 - m.x422 + m.x423 == 0)

m.c89 = Constraint(expr= - m.x255 - m.x262 + m.x269 + m.x276 - m.x423 + m.x424 == 0)

m.c90 = Constraint(expr= - m.x256 - m.x263 + m.x270 + m.x277 - m.x424 + m.x425 == 0)

m.c91 = Constraint(expr= - m.x257 - m.x264 + m.x271 + m.x278 - m.x425 + m.x426 == 0)

m.c92 = Constraint(expr= - m.x258 - m.x265 + m.x272 + m.x279 - m.x426 + m.x427 == 0)

m.c93 = Constraint(expr=m.x463/m.x476*(m.x476 - m.x472) - m.x273 - m.x280 + m.x428 - m.x434 == 0)

m.c94 = Constraint(expr=m.x463/m.x476*(m.x467 - m.x466) - m.x267 - m.x274 - m.x428 + m.x429 == 0)

m.c95 = Constraint(expr=m.x463/m.x476*(m.x468 - m.x467) - m.x268 - m.x275 - m.x429 + m.x430 == 0)

m.c96 = Constraint(expr=m.x463/m.x476*(m.x469 - m.x468) - m.x269 - m.x276 - m.x430 + m.x431 == 0)

m.c97 = Constraint(expr=m.x463/m.x476*(m.x470 - m.x469) - m.x270 - m.x277 - m.x431 + m.x432 == 0)

m.c98 = Constraint(expr=m.x463/m.x476*(m.x471 - m.x470) - m.x271 - m.x278 - m.x432 + m.x433 == 0)

m.c99 = Constraint(expr=m.x463/m.x476*(m.x472 - m.x471) - m.x272 - m.x279 - m.x433 + m.x434 == 0)

m.c100 = Constraint(expr= - m.x287 - m.x294 + m.x301 + m.x308 + m.x435 - m.x441 == 0)

m.c101 = Constraint(expr= - m.x281 - m.x288 + m.x295 + m.x302 - m.x435 + m.x436 == 0)

m.c102 = Constraint(expr= - m.x282 - m.x289 + m.x296 + m.x303 - m.x436 + m.x437 == 0)

m.c103 = Constraint(expr= - m.x283 - m.x290 + m.x297 + m.x304 - m.x437 + m.x438 == 0)

m.c104 = Constraint(expr= - m.x284 - m.x291 + m.x298 + m.x305 - m.x438 + m.x439 == 0)

m.c105 = Constraint(expr= - m.x285 - m.x292 + m.x299 + m.x306 - m.x439 + m.x440 == 0)

m.c106 = Constraint(expr= - m.x286 - m.x293 + m.x300 + m.x307 - m.x440 + m.x441 == 0)

m.c107 = Constraint(expr=m.x464/m.x476*(m.x476 - m.x472) - m.x301 - m.x308 + m.x442 - m.x448 == 0)

m.c108 = Constraint(expr=m.x464/m.x476*(m.x467 - m.x466) - m.x295 - m.x302 - m.x442 + m.x443 == 0)

m.c109 = Constraint(expr=m.x464/m.x476*(m.x468 - m.x467) - m.x296 - m.x303 - m.x443 + m.x444 == 0)

m.c110 = Constraint(expr=m.x464/m.x476*(m.x469 - m.x468) - m.x297 - m.x304 - m.x444 + m.x445 == 0)

m.c111 = Constraint(expr=m.x464/m.x476*(m.x470 - m.x469) - m.x298 - m.x305 - m.x445 + m.x446 == 0)

m.c112 = Constraint(expr=m.x464/m.x476*(m.x471 - m.x470) - m.x299 - m.x306 - m.x446 + m.x447 == 0)

m.c113 = Constraint(expr=m.x464/m.x476*(m.x472 - m.x471) - m.x300 - m.x307 - m.x447 + m.x448 == 0)

m.c114 = Constraint(expr= - m.x315 - m.x322 + m.x329 + m.x336 + m.x449 - m.x455 == 0)

m.c115 = Constraint(expr= - m.x309 - m.x316 + m.x323 + m.x330 - m.x449 + m.x450 == 0)

m.c116 = Constraint(expr= - m.x310 - m.x317 + m.x324 + m.x331 - m.x450 + m.x451 == 0)

m.c117 = Constraint(expr= - m.x311 - m.x318 + m.x325 + m.x332 - m.x451 + m.x452 == 0)

m.c118 = Constraint(expr= - m.x312 - m.x319 + m.x326 + m.x333 - m.x452 + m.x453 == 0)

m.c119 = Constraint(expr= - m.x313 - m.x320 + m.x327 + m.x334 - m.x453 + m.x454 == 0)

m.c120 = Constraint(expr= - m.x314 - m.x321 + m.x328 + m.x335 - m.x454 + m.x455 == 0)

m.c121 = Constraint(expr=m.x465/m.x476*(m.x476 - m.x472) - m.x329 - m.x336 + m.x456 - m.x462 == 0)

m.c122 = Constraint(expr=m.x465/m.x476*(m.x467 - m.x466) - m.x323 - m.x330 - m.x456 + m.x457 == 0)

m.c123 = Constraint(expr=m.x465/m.x476*(m.x468 - m.x467) - m.x324 - m.x331 - m.x457 + m.x458 == 0)

m.c124 = Constraint(expr=m.x465/m.x476*(m.x469 - m.x468) - m.x325 - m.x332 - m.x458 + m.x459 == 0)

m.c125 = Constraint(expr=m.x465/m.x476*(m.x470 - m.x469) - m.x326 - m.x333 - m.x459 + m.x460 == 0)

m.c126 = Constraint(expr=m.x465/m.x476*(m.x471 - m.x470) - m.x327 - m.x334 - m.x460 + m.x461 == 0)

m.c127 = Constraint(expr=m.x465/m.x476*(m.x472 - m.x471) - m.x328 - m.x335 - m.x461 + m.x462 == 0)

m.c128 = Constraint(expr=   m.b1 + m.b29 + m.b57 + m.b85 + m.b92 + m.b99 + m.b106 + m.b113 + m.b120 + m.x337 + m.x344
                          + m.x351 == 1)

m.c129 = Constraint(expr=   m.b8 + m.b36 + m.b64 + m.b127 + m.b134 + m.b141 + m.b148 + m.b155 + m.b162 + m.x358 + m.x365
                          + m.x372 == 1)

m.c130 = Constraint(expr=   m.b15 + m.b43 + m.b71 + m.b169 + m.b176 + m.b183 + m.b190 + m.b197 + m.b204 + m.x379
                          + m.x386 + m.x393 == 1)

m.c131 = Constraint(expr=   m.b22 + m.b50 + m.b78 + m.b211 + m.b218 + m.b225 + m.b232 + m.b239 + m.b246 + m.x400
                          + m.x407 + m.x414 == 1)

m.c132 = Constraint(expr= - 5*m.b85 - 8*m.b92 - 10*m.b99 - 3*m.b106 - 4*m.b113 - 7*m.b120 - 0.00125*m.x253
                          - 0.000833333333333333*m.x281 - 0.001*m.x309 - m.x466 + m.x467 >= 0)

m.c133 = Constraint(expr= - 5*m.b86 - 8*m.b93 - 10*m.b100 - 3*m.b107 - 4*m.b114 - 7*m.b121 - 0.00125*m.x254
                          - 0.000833333333333333*m.x282 - 0.001*m.x310 - m.x467 + m.x468 >= 0)

m.c134 = Constraint(expr= - 5*m.b87 - 8*m.b94 - 10*m.b101 - 3*m.b108 - 4*m.b115 - 7*m.b122 - 0.00125*m.x255
                          - 0.000833333333333333*m.x283 - 0.001*m.x311 - m.x468 + m.x469 >= 0)

m.c135 = Constraint(expr= - 5*m.b88 - 8*m.b95 - 10*m.b102 - 3*m.b109 - 4*m.b116 - 7*m.b123 - 0.00125*m.x256
                          - 0.000833333333333333*m.x284 - 0.001*m.x312 - m.x469 + m.x470 >= 0)

m.c136 = Constraint(expr= - 5*m.b89 - 8*m.b96 - 10*m.b103 - 3*m.b110 - 4*m.b117 - 7*m.b124 - 0.00125*m.x257
                          - 0.000833333333333333*m.x285 - 0.001*m.x313 - m.x470 + m.x471 >= 0)

m.c137 = Constraint(expr= - 5*m.b90 - 8*m.b97 - 10*m.b104 - 3*m.b111 - 4*m.b118 - 7*m.b125 - 0.00125*m.x258
                          - 0.000833333333333333*m.x286 - 0.001*m.x314 - m.x471 + m.x472 >= 0)

m.c138 = Constraint(expr= - 5*m.b91 - 8*m.b98 - 10*m.b105 - 3*m.b112 - 4*m.b119 - 7*m.b126 - 0.00125*m.x259
                          - 0.000833333333333333*m.x287 - 0.001*m.x315 - m.x472 + m.x476 >= 0)

m.c139 = Constraint(expr= - 9*m.b127 - 11*m.b134 - 5*m.b141 - 7*m.b148 - 6*m.b155 - 4*m.b162 - 0.0025*m.x260
                          - 0.002*m.x288 - 0.00222222222222222*m.x316 - m.x466 + m.x467 >= 0)

m.c140 = Constraint(expr= - 9*m.b128 - 11*m.b135 - 5*m.b142 - 7*m.b149 - 6*m.b156 - 4*m.b163 - 0.0025*m.x261
                          - 0.002*m.x289 - 0.00222222222222222*m.x317 - m.x467 + m.x468 >= 0)

m.c141 = Constraint(expr= - 9*m.b129 - 11*m.b136 - 5*m.b143 - 7*m.b150 - 6*m.b157 - 4*m.b164 - 0.0025*m.x262
                          - 0.002*m.x290 - 0.00222222222222222*m.x318 - m.x468 + m.x469 >= 0)

m.c142 = Constraint(expr= - 9*m.b130 - 11*m.b137 - 5*m.b144 - 7*m.b151 - 6*m.b158 - 4*m.b165 - 0.0025*m.x263
                          - 0.002*m.x291 - 0.00222222222222222*m.x319 - m.x469 + m.x470 >= 0)

m.c143 = Constraint(expr= - 9*m.b131 - 11*m.b138 - 5*m.b145 - 7*m.b152 - 6*m.b159 - 4*m.b166 - 0.0025*m.x264
                          - 0.002*m.x292 - 0.00222222222222222*m.x320 - m.x470 + m.x471 >= 0)

m.c144 = Constraint(expr= - 9*m.b132 - 11*m.b139 - 5*m.b146 - 7*m.b153 - 6*m.b160 - 4*m.b167 - 0.0025*m.x265
                          - 0.002*m.x293 - 0.00222222222222222*m.x321 - m.x471 + m.x472 >= 0)

m.c145 = Constraint(expr= - 9*m.b133 - 11*m.b140 - 5*m.b147 - 7*m.b154 - 6*m.b161 - 4*m.b168 - 0.0025*m.x266
                          - 0.002*m.x294 - 0.00222222222222222*m.x322 - m.x472 + m.x476 >= 0)

m.c146 = Constraint(expr= - 11*m.b169 - m.b176 - 2*m.b183 - 5*m.b190 - 6*m.b197 - m.b204 - 0.00111111111111111*m.x267
                          - 0.00166666666666667*m.x295 - 0.000909090909090909*m.x323 - m.x466 + m.x467 >= 0)

m.c147 = Constraint(expr= - 11*m.b170 - m.b177 - 2*m.b184 - 5*m.b191 - 6*m.b198 - m.b205 - 0.00111111111111111*m.x268
                          - 0.00166666666666667*m.x296 - 0.000909090909090909*m.x324 - m.x467 + m.x468 >= 0)

m.c148 = Constraint(expr= - 11*m.b171 - m.b178 - 2*m.b185 - 5*m.b192 - 6*m.b199 - m.b206 - 0.00111111111111111*m.x269
                          - 0.00166666666666667*m.x297 - 0.000909090909090909*m.x325 - m.x468 + m.x469 >= 0)

m.c149 = Constraint(expr= - 11*m.b172 - m.b179 - 2*m.b186 - 5*m.b193 - 6*m.b200 - m.b207 - 0.00111111111111111*m.x270
                          - 0.00166666666666667*m.x298 - 0.000909090909090909*m.x326 - m.x469 + m.x470 >= 0)

m.c150 = Constraint(expr= - 11*m.b173 - m.b180 - 2*m.b187 - 5*m.b194 - 6*m.b201 - m.b208 - 0.00111111111111111*m.x271
                          - 0.00166666666666667*m.x299 - 0.000909090909090909*m.x327 - m.x470 + m.x471 >= 0)

m.c151 = Constraint(expr= - 11*m.b174 - m.b181 - 2*m.b188 - 5*m.b195 - 6*m.b202 - m.b209 - 0.00111111111111111*m.x272
                          - 0.00166666666666667*m.x300 - 0.000909090909090909*m.x328 - m.x471 + m.x472 >= 0)

m.c152 = Constraint(expr= - 11*m.b175 - m.b182 - 2*m.b189 - 5*m.b196 - 6*m.b203 - m.b210 - 0.00111111111111111*m.x273
                          - 0.00166666666666667*m.x301 - 0.000909090909090909*m.x329 - m.x472 + m.x476 >= 0)

m.c153 = Constraint(expr= - 9*m.b211 - 11*m.b218 - 5*m.b225 - 7*m.b232 - 6*m.b239 - 4*m.b246 - 0.0025*m.x274
                          - 0.002*m.x302 - 0.00222222222222222*m.x330 - m.x466 + m.x467 >= 0)

m.c154 = Constraint(expr= - 9*m.b212 - 11*m.b219 - 5*m.b226 - 7*m.b233 - 6*m.b240 - 4*m.b247 - 0.0025*m.x275
                          - 0.002*m.x303 - 0.00222222222222222*m.x331 - m.x467 + m.x468 >= 0)

m.c155 = Constraint(expr= - 9*m.b213 - 11*m.b220 - 5*m.b227 - 7*m.b234 - 6*m.b241 - 4*m.b248 - 0.0025*m.x276
                          - 0.002*m.x304 - 0.00222222222222222*m.x332 - m.x468 + m.x469 >= 0)

m.c156 = Constraint(expr= - 9*m.b214 - 11*m.b221 - 5*m.b228 - 7*m.b235 - 6*m.b242 - 4*m.b249 - 0.0025*m.x277
                          - 0.002*m.x305 - 0.00222222222222222*m.x333 - m.x469 + m.x470 >= 0)

m.c157 = Constraint(expr= - 9*m.b215 - 11*m.b222 - 5*m.b229 - 7*m.b236 - 6*m.b243 - 4*m.b250 - 0.0025*m.x278
                          - 0.002*m.x306 - 0.00222222222222222*m.x334 - m.x470 + m.x471 >= 0)

m.c158 = Constraint(expr= - 9*m.b216 - 11*m.b223 - 5*m.b230 - 7*m.b237 - 6*m.b244 - 4*m.b251 - 0.0025*m.x279
                          - 0.002*m.x307 - 0.00222222222222222*m.x335 - m.x471 + m.x472 >= 0)

m.c159 = Constraint(expr= - 9*m.b217 - 11*m.b224 - 5*m.b231 - 7*m.b238 - 6*m.b245 - 4*m.b252 - 0.0025*m.x280
                          - 0.002*m.x308 - 0.00222222222222222*m.x336 - m.x472 + m.x476 >= 0)

m.c160 = Constraint(expr= - 480000*m.b1 + m.x253 <= 0)

m.c161 = Constraint(expr= - 480000*m.b2 + m.x254 <= 0)

m.c162 = Constraint(expr= - 480000*m.b3 + m.x255 <= 0)

m.c163 = Constraint(expr= - 480000*m.b4 + m.x256 <= 0)

m.c164 = Constraint(expr= - 480000*m.b5 + m.x257 <= 0)

m.c165 = Constraint(expr= - 480000*m.b6 + m.x258 <= 0)

m.c166 = Constraint(expr= - 480000*m.b7 + m.x259 <= 0)

m.c167 = Constraint(expr= - 240000*m.b8 + m.x260 <= 0)

m.c168 = Constraint(expr= - 240000*m.b9 + m.x261 <= 0)

m.c169 = Constraint(expr= - 240000*m.b10 + m.x262 <= 0)

m.c170 = Constraint(expr= - 240000*m.b11 + m.x263 <= 0)

m.c171 = Constraint(expr= - 240000*m.b12 + m.x264 <= 0)

m.c172 = Constraint(expr= - 240000*m.b13 + m.x265 <= 0)

m.c173 = Constraint(expr= - 240000*m.b14 + m.x266 <= 0)

m.c174 = Constraint(expr= - 540000*m.b15 + m.x267 <= 0)

m.c175 = Constraint(expr= - 540000*m.b16 + m.x268 <= 0)

m.c176 = Constraint(expr= - 540000*m.b17 + m.x269 <= 0)

m.c177 = Constraint(expr= - 540000*m.b18 + m.x270 <= 0)

m.c178 = Constraint(expr= - 540000*m.b19 + m.x271 <= 0)

m.c179 = Constraint(expr= - 540000*m.b20 + m.x272 <= 0)

m.c180 = Constraint(expr= - 540000*m.b21 + m.x273 <= 0)

m.c181 = Constraint(expr= - 240000*m.b22 + m.x274 <= 0)

m.c182 = Constraint(expr= - 240000*m.b23 + m.x275 <= 0)

m.c183 = Constraint(expr= - 240000*m.b24 + m.x276 <= 0)

m.c184 = Constraint(expr= - 240000*m.b25 + m.x277 <= 0)

m.c185 = Constraint(expr= - 240000*m.b26 + m.x278 <= 0)

m.c186 = Constraint(expr= - 240000*m.b27 + m.x279 <= 0)

m.c187 = Constraint(expr= - 240000*m.b28 + m.x280 <= 0)

m.c188 = Constraint(expr= - 720000*m.b29 + m.x281 <= 0)

m.c189 = Constraint(expr= - 720000*m.b30 + m.x282 <= 0)

m.c190 = Constraint(expr= - 720000*m.b31 + m.x283 <= 0)

m.c191 = Constraint(expr= - 720000*m.b32 + m.x284 <= 0)

m.c192 = Constraint(expr= - 720000*m.b33 + m.x285 <= 0)

m.c193 = Constraint(expr= - 720000*m.b34 + m.x286 <= 0)

m.c194 = Constraint(expr= - 720000*m.b35 + m.x287 <= 0)

m.c195 = Constraint(expr= - 300000*m.b36 + m.x288 <= 0)

m.c196 = Constraint(expr= - 300000*m.b37 + m.x289 <= 0)

m.c197 = Constraint(expr= - 300000*m.b38 + m.x290 <= 0)

m.c198 = Constraint(expr= - 300000*m.b39 + m.x291 <= 0)

m.c199 = Constraint(expr= - 300000*m.b40 + m.x292 <= 0)

m.c200 = Constraint(expr= - 300000*m.b41 + m.x293 <= 0)

m.c201 = Constraint(expr= - 300000*m.b42 + m.x294 <= 0)

m.c202 = Constraint(expr= - 360000*m.b43 + m.x295 <= 0)

m.c203 = Constraint(expr= - 360000*m.b44 + m.x296 <= 0)

m.c204 = Constraint(expr= - 360000*m.b45 + m.x297 <= 0)

m.c205 = Constraint(expr= - 360000*m.b46 + m.x298 <= 0)

m.c206 = Constraint(expr= - 360000*m.b47 + m.x299 <= 0)

m.c207 = Constraint(expr= - 360000*m.b48 + m.x300 <= 0)

m.c208 = Constraint(expr= - 360000*m.b49 + m.x301 <= 0)

m.c209 = Constraint(expr= - 300000*m.b50 + m.x302 <= 0)

m.c210 = Constraint(expr= - 300000*m.b51 + m.x303 <= 0)

m.c211 = Constraint(expr= - 300000*m.b52 + m.x304 <= 0)

m.c212 = Constraint(expr= - 300000*m.b53 + m.x305 <= 0)

m.c213 = Constraint(expr= - 300000*m.b54 + m.x306 <= 0)

m.c214 = Constraint(expr= - 300000*m.b55 + m.x307 <= 0)

m.c215 = Constraint(expr= - 300000*m.b56 + m.x308 <= 0)

m.c216 = Constraint(expr= - 600000*m.b57 + m.x309 <= 0)

m.c217 = Constraint(expr= - 600000*m.b58 + m.x310 <= 0)

m.c218 = Constraint(expr= - 600000*m.b59 + m.x311 <= 0)

m.c219 = Constraint(expr= - 600000*m.b60 + m.x312 <= 0)

m.c220 = Constraint(expr= - 600000*m.b61 + m.x313 <= 0)

m.c221 = Constraint(expr= - 600000*m.b62 + m.x314 <= 0)

m.c222 = Constraint(expr= - 600000*m.b63 + m.x315 <= 0)

m.c223 = Constraint(expr= - 270000*m.b64 + m.x316 <= 0)

m.c224 = Constraint(expr= - 270000*m.b65 + m.x317 <= 0)

m.c225 = Constraint(expr= - 270000*m.b66 + m.x318 <= 0)

m.c226 = Constraint(expr= - 270000*m.b67 + m.x319 <= 0)

m.c227 = Constraint(expr= - 270000*m.b68 + m.x320 <= 0)

m.c228 = Constraint(expr= - 270000*m.b69 + m.x321 <= 0)

m.c229 = Constraint(expr= - 270000*m.b70 + m.x322 <= 0)

m.c230 = Constraint(expr= - 660000*m.b71 + m.x323 <= 0)

m.c231 = Constraint(expr= - 660000*m.b72 + m.x324 <= 0)

m.c232 = Constraint(expr= - 660000*m.b73 + m.x325 <= 0)

m.c233 = Constraint(expr= - 660000*m.b74 + m.x326 <= 0)

m.c234 = Constraint(expr= - 660000*m.b75 + m.x327 <= 0)

m.c235 = Constraint(expr= - 660000*m.b76 + m.x328 <= 0)

m.c236 = Constraint(expr= - 660000*m.b77 + m.x329 <= 0)

m.c237 = Constraint(expr= - 270000*m.b78 + m.x330 <= 0)

m.c238 = Constraint(expr= - 270000*m.b79 + m.x331 <= 0)

m.c239 = Constraint(expr= - 270000*m.b80 + m.x332 <= 0)

m.c240 = Constraint(expr= - 270000*m.b81 + m.x333 <= 0)

m.c241 = Constraint(expr= - 270000*m.b82 + m.x334 <= 0)

m.c242 = Constraint(expr= - 270000*m.b83 + m.x335 <= 0)

m.c243 = Constraint(expr= - 270000*m.b84 + m.x336 <= 0)

m.c244 = Constraint(expr=   m.x463 - 50*m.x476 >= 0)

m.c245 = Constraint(expr=   m.x464 - 100*m.x476 >= 0)

m.c246 = Constraint(expr=   m.x465 - 250*m.x476 >= 0)

m.c247 = Constraint(expr=   m.x421 - m.x473 <= 0)

m.c248 = Constraint(expr=   m.x422 - m.x473 <= 0)

m.c249 = Constraint(expr=   m.x423 - m.x473 <= 0)

m.c250 = Constraint(expr=   m.x424 - m.x473 <= 0)

m.c251 = Constraint(expr=   m.x425 - m.x473 <= 0)

m.c252 = Constraint(expr=   m.x426 - m.x473 <= 0)

m.c253 = Constraint(expr=   m.x427 - m.x473 <= 0)

m.c254 = Constraint(expr=   m.x435 - m.x474 <= 0)

m.c255 = Constraint(expr=   m.x436 - m.x474 <= 0)

m.c256 = Constraint(expr=   m.x437 - m.x474 <= 0)

m.c257 = Constraint(expr=   m.x438 - m.x474 <= 0)

m.c258 = Constraint(expr=   m.x439 - m.x474 <= 0)

m.c259 = Constraint(expr=   m.x440 - m.x474 <= 0)

m.c260 = Constraint(expr=   m.x441 - m.x474 <= 0)

m.c261 = Constraint(expr=   m.x449 - m.x475 <= 0)

m.c262 = Constraint(expr=   m.x450 - m.x475 <= 0)

m.c263 = Constraint(expr=   m.x451 - m.x475 <= 0)

m.c264 = Constraint(expr=   m.x452 - m.x475 <= 0)

m.c265 = Constraint(expr=   m.x453 - m.x475 <= 0)

m.c266 = Constraint(expr=   m.x454 - m.x475 <= 0)

m.c267 = Constraint(expr=   m.x455 - m.x475 <= 0)

m.c268 = Constraint(expr=   m.b85 + m.b86 + m.b87 + m.b88 + m.b89 + m.b90 + m.b91 + m.b92 + m.b93 + m.b94 + m.b95
                          + m.b96 + m.b97 + m.b98 + m.b99 + m.b100 + m.b101 + m.b102 + m.b103 + m.b104 + m.b105 + m.b106
                          + m.b107 + m.b108 + m.b109 + m.b110 + m.b111 + m.b112 + m.b113 + m.b114 + m.b115 + m.b116
                          + m.b117 + m.b118 + m.b119 + m.b120 + m.b121 + m.b122 + m.b123 + m.b124 + m.b125 + m.b126
                          + m.b127 + m.b128 + m.b129 + m.b130 + m.b131 + m.b132 + m.b133 + m.b134 + m.b135 + m.b136
                          + m.b137 + m.b138 + m.b139 + m.b140 + m.b141 + m.b142 + m.b143 + m.b144 + m.b145 + m.b146
                          + m.b147 + m.b148 + m.b149 + m.b150 + m.b151 + m.b152 + m.b153 + m.b154 + m.b155 + m.b156
                          + m.b157 + m.b158 + m.b159 + m.b160 + m.b161 + m.b162 + m.b163 + m.b164 + m.b165 + m.b166
                          + m.b167 + m.b168 <= 3)

m.c269 = Constraint(expr=   m.b169 + m.b170 + m.b171 + m.b172 + m.b173 + m.b174 + m.b175 + m.b176 + m.b177 + m.b178
                          + m.b179 + m.b180 + m.b181 + m.b182 + m.b183 + m.b184 + m.b185 + m.b186 + m.b187 + m.b188
                          + m.b189 + m.b190 + m.b191 + m.b192 + m.b193 + m.b194 + m.b195 + m.b196 + m.b197 + m.b198
                          + m.b199 + m.b200 + m.b201 + m.b202 + m.b203 + m.b204 + m.b205 + m.b206 + m.b207 + m.b208
                          + m.b209 + m.b210 + m.b211 + m.b212 + m.b213 + m.b214 + m.b215 + m.b216 + m.b217 + m.b218
                          + m.b219 + m.b220 + m.b221 + m.b222 + m.b223 + m.b224 + m.b225 + m.b226 + m.b227 + m.b228
                          + m.b229 + m.b230 + m.b231 + m.b232 + m.b233 + m.b234 + m.b235 + m.b236 + m.b237 + m.b238
                          + m.b239 + m.b240 + m.b241 + m.b242 + m.b243 + m.b244 + m.b245 + m.b246 + m.b247 + m.b248
                          + m.b249 + m.b250 + m.b251 + m.b252 <= 3)

m.c270 = Constraint(expr=   m.b1 + m.b8 == 1)
