#  MINLP written by GAMS Convert at 04/21/18 13:54:17
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        379        1      378        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        379        1      378        0


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
m.b253 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b254 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b255 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b256 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b257 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b258 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b259 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b260 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b261 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b262 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b263 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b264 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b265 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b266 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b267 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b268 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b269 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b270 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b271 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b272 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b273 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b274 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b275 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b276 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b277 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b278 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b279 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b280 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b281 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b282 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b283 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b284 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b285 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b286 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b287 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b288 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b289 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b290 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.b326 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b327 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b328 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b329 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b330 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b331 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b332 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b333 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b334 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b335 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b336 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b337 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b338 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b339 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b340 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b341 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b342 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b343 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b344 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b345 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b346 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b347 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b348 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b349 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b350 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b351 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b352 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b353 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b354 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b355 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b356 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b357 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b358 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b359 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b360 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b361 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b362 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b363 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b364 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b365 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b366 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b367 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b368 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b369 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b370 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b371 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b372 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b373 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b374 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b375 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b376 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b377 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b378 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x379 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x379, sense=maximize)

m.c1 = Constraint(expr=(-2*m.b1*m.b206) - 2*m.b1 + 2*m.b206 + 2*m.b1*m.b209 - 2*m.b209 + 2*m.b1*m.b250 + 2*m.b1*m.b262
                        + 2*m.b2*m.b130 - 2*m.b2 - 2*m.b130 + 2*m.b2*m.b219 + 2*m.b219 + 2*m.b2*m.b258 - 2*m.b2*m.b273
                        + 2*m.b3*m.b107 - 2*m.b3 - 2*m.b107 + 2*m.b3*m.b253 + 2*m.b3*m.b258 - 2*m.b3*m.b280 + 2*m.b4*
                       m.b6 - 2*m.b4 - 4*m.b6 + 2*m.b4*m.b8 - 2*m.b8 + 2*m.b4*m.b264 - 2*m.b4*m.b295 + 2*m.b5*m.b88 - 2*
                       m.b5 - 2*m.b88 + 2*m.b5*m.b132 - 2*m.b132 + 2*m.b5*m.b253 - 2*m.b5*m.b287 + 2*m.b6*m.b70 - 2*
                       m.b70 + 2*m.b6*m.b108 - 2*m.b108 + 2*m.b6*m.b132 + 2*m.b7*m.b59 - 2*m.b7 - 2*m.b59 - 2*m.b7*
                       m.b197 + 2*m.b197 + 2*m.b7*m.b298 + 2*m.b7*m.b299 + 2*m.b8*m.b255 + 2*m.b8*m.b280 - 2*m.b8*m.b310
                        + 2*m.b9*m.b54 - 4*m.b9 - 2*m.b54 + 2*m.b9*m.b108 + 2*m.b9*m.b267 + 2*m.b9*m.b287 + 2*m.b10*
                       m.b59 - 2*m.b10 + 2*m.b10*m.b77 - 2*m.b77 - 2*m.b10*m.b229 + 2*m.b229 + 2*m.b10*m.b307 + 2*m.b11*
                       m.b77 - 2*m.b11 + 2*m.b11*m.b93 - 2*m.b93 + 2*m.b11*m.b115 - 2*m.b115 - 2*m.b11*m.b314 + 2*m.b12*
                       m.b15 - 2*m.b12 - 2*m.b15 + 2*m.b12*m.b244 - 2*m.b244 - 2*m.b13*m.b56 - 2*m.b13 - 2*m.b56 + 2*
                       m.b13*m.b90 - 2*m.b90 + 2*m.b13*m.b221 - 2*m.b221 + 2*m.b13*m.b224 + 2*m.b224 + 2*m.b14*m.b93 - 2
                       *m.b14 + 2*m.b14*m.b116 - 4*m.b116 + 2*m.b14*m.b140 - 4*m.b140 - 2*m.b14*m.b320 + 2*m.b15*m.b16
                        - 2*m.b16 - 2*m.b15*m.b63 - 2*m.b63 + 2*m.b15*m.b81 - 4*m.b81 + 2*m.b16*m.b19 - 2*m.b19 + 2*
                       m.b17*m.b116 - 2*m.b17 + 2*m.b17*m.b142 - 4*m.b142 + 2*m.b17*m.b167 - 4*m.b167 - 2*m.b17*m.b324
                        + 2*m.b18*m.b27 - 2*m.b18 - 2*m.b27 + 2*m.b18*m.b34 - 4*m.b34 - 2*m.b18*m.b93 + 2*m.b18*m.b142
                        + 2*m.b19*m.b20 - 2*m.b20 - 2*m.b19*m.b48 - 2*m.b48 + 2*m.b19*m.b102 - 4*m.b102 + 2*m.b20*m.b23
                        - 2*m.b23 + 2*m.b21*m.b142 - 4*m.b21 + 2*m.b21*m.b169 - 4*m.b169 + 2*m.b21*m.b198 - 4*m.b198 + 2
                       *m.b21*m.b324 + 2*m.b22*m.b34 - 2*m.b22 + 2*m.b22*m.b44 - 4*m.b44 - 2*m.b22*m.b77 + 2*m.b22*
                       m.b169 + 2*m.b23*m.b24 - 2*m.b24 - 2*m.b23*m.b35 - 2*m.b35 + 2*m.b23*m.b125 - 4*m.b125 + 2*m.b24*
                       m.b28 - 2*m.b28 + 2*m.b25*m.b169 - 4*m.b25 + 2*m.b25*m.b200 - 4*m.b200 + 2*m.b25*m.b230 - 4*
                       m.b230 + 2*m.b25*m.b320 + 2*m.b26*m.b44 - 2*m.b26 - 2*m.b26*m.b59 + 2*m.b26*m.b61 - 4*m.b61 + 2*
                       m.b26*m.b200 + 2*m.b27*m.b234 - 4*m.b234 + 2*m.b27*m.b321 - 2*m.b27*m.b325 + 2*m.b28*m.b29 - 2*
                       m.b29 + 2*m.b28*m.b150 - 4*m.b150 - 2*m.b28*m.b337 + 2*m.b29*m.b36 - 4*m.b36 + 2*m.b30*m.b31 - 2*
                       m.b30 - 2*m.b31 + 2*m.b30*m.b73 - 2*m.b73 + 2*m.b30*m.b137 - 4*m.b137 - 2*m.b30*m.b281 + 2*m.b31*
                       m.b57 - 2*m.b57 + 2*m.b31*m.b305 - 2*m.b31*m.b347 + 2*m.b32*m.b200 - 2*m.b32 + 2*m.b32*m.b232 - 2
                       *m.b232 - 2*m.b32*m.b245 + 2*m.b32*m.b314 + 2*m.b33*m.b61 - 2*m.b33 + 2*m.b33*m.b79 - 4*m.b79 + 2
                       *m.b33*m.b232 - 2*m.b33*m.b299 + 2*m.b34*m.b96 - 4*m.b96 + 2*m.b34*m.b315 + 2*m.b35*m.b49 - 4*
                       m.b49 + 2*m.b35*m.b62 - 4*m.b62 + 2*m.b35*m.b335 + 2*m.b36*m.b37 - 2*m.b37 + 2*m.b36*m.b242 - 2*
                       m.b242 + 2*m.b36*m.b337 + 2*m.b37*m.b49 + 2*m.b38*m.b85 - 2*m.b38 - 4*m.b85 + 2*m.b38*m.b251 + 2*
                       m.b38*m.b293 - 2*m.b38*m.b351 + 2*m.b39*m.b54 - 2*m.b39 + 2*m.b39*m.b130 - 2*m.b39*m.b255 + 2*
                       m.b39*m.b346 + 2*m.b40*m.b42 - 4*m.b40 - 4*m.b42 + 2*m.b40*m.b268 + 2*m.b40*m.b282 + 2*m.b40*
                       m.b341 + 2*m.b41*m.b76 + 2*m.b41 - 4*m.b76 - 2*m.b41*m.b195 + 2*m.b195 - 2*m.b41*m.b197 - 2*m.b41
                       *m.b245 + 2*m.b42*m.b197 + 2*m.b42*m.b245 + 2*m.b42*m.b305 + 2*m.b43*m.b79 - 2*m.b43 + 2*m.b43*
                       m.b95 - 4*m.b95 - 2*m.b43*m.b233 - 2*m.b233 + 2*m.b43*m.b299 + 2*m.b44*m.b308 + 2*m.b44*m.b325 - 
                       2*m.b45*m.b46 - 2*m.b45 + 2*m.b46 + 2*m.b45*m.b246 + 2*m.b45*m.b250 + 2*m.b45*m.b325 + 2*m.b46*
                       m.b80 - 4*m.b80 - 2*m.b46*m.b335 - 2*m.b46*m.b354 + 2*m.b47*m.b48 - 2*m.b47 + 2*m.b47*m.b337 - 2*
                       m.b47*m.b343 + 2*m.b47*m.b344 + 2*m.b48*m.b64 - 4*m.b64 + 2*m.b48*m.b80 + 2*m.b49*m.b50 - 2*m.b50
                        + 2*m.b49*m.b210 - 4*m.b210 + 2*m.b50*m.b64 + 2*m.b51*m.b301 - 2*m.b51 + 2*m.b51*m.b302 + 2*
                       m.b52*m.b67 - 2*m.b52 - 4*m.b67 + 2*m.b52*m.b249 + 2*m.b52*m.b301 - 2*m.b52*m.b356 - 2*m.b53*
                       m.b184 + 2*m.b53 - 2*m.b184 + 2*m.b53*m.b217 - 2*m.b217 - 2*m.b53*m.b251 - 2*m.b53*m.b323 + 2*
                       m.b54*m.b129 - 2*m.b129 - 2*m.b54*m.b358 + 2*m.b55*m.b56 - 4*m.b55 + 2*m.b55*m.b134 - 2*m.b134 + 
                       2*m.b55*m.b264 + 2*m.b55*m.b358 + 2*m.b56*m.b110 - 2*m.b110 + 2*m.b56*m.b188 - 4*m.b188 + 2*m.b57
                       *m.b259 + 2*m.b57*m.b275 - 2*m.b57*m.b348 + 2*m.b58*m.b274 - 4*m.b58 + 2*m.b58*m.b289 + 2*m.b58*
                       m.b334 + 2*m.b58*m.b348 + 2*m.b59*m.b60 - 2*m.b60 + 2*m.b60*m.b95 + 2*m.b60*m.b119 - 4*m.b119 - 2
                       *m.b60*m.b201 - 2*m.b201 + 2*m.b61*m.b300 + 2*m.b61*m.b321 + 2*m.b62*m.b63 + 2*m.b62*m.b100 - 2*
                       m.b100 + 2*m.b62*m.b343 + 2*m.b63*m.b82 - 2*m.b82 + 2*m.b63*m.b101 - 4*m.b101 + 2*m.b64*m.b65 - 2
                       *m.b65 + 2*m.b64*m.b243 - 4*m.b243 + 2*m.b65*m.b82 + 2*m.b66*m.b67 - 2*m.b66 + 2*m.b66*m.b293 + 2
                       *m.b67*m.b153 - 2*m.b153 + 2*m.b67*m.b357 - 2*m.b68*m.b183 + 2*m.b68 - 2*m.b183 - 2*m.b68*m.b249
                        - 2*m.b68*m.b301 + 2*m.b68*m.b302 + 2*m.b69*m.b186 + 2*m.b69 - 2*m.b186 - 2*m.b69*m.b249 - 2*
                       m.b69*m.b272 - 2*m.b69*m.b318 + 2*m.b70*m.b156 - 2*m.b156 + 2*m.b70*m.b323 - 2*m.b70*m.b361 + 2*
                       m.b71*m.b319 - 2*m.b71 - 2*m.b71*m.b328 + 2*m.b71*m.b358 + 2*m.b71*m.b361 + 2*m.b72*m.b73 - 2*
                       m.b72 - 2*m.b72*m.b74 + 2*m.b74 + 2*m.b72*m.b110 + 2*m.b72*m.b297 + 2*m.b73*m.b76 - 2*m.b73*
                       m.b139 + 4*m.b139 + 2*m.b74*m.b76 - 2*m.b74*m.b113 + 4*m.b113 - 2*m.b74*m.b363 - 2*m.b75*m.b259
                        + 2*m.b75 + 2*m.b75*m.b269 - 2*m.b75*m.b341 - 2*m.b75*m.b342 + 2*m.b76*m.b342 + 2*m.b77*m.b78 - 
                       2*m.b78 + 2*m.b78*m.b119 + 2*m.b78*m.b145 - 4*m.b145 - 2*m.b78*m.b170 - 2*m.b170 + 2*m.b79*m.b292
                        + 2*m.b79*m.b315 + 2*m.b80*m.b81 + 2*m.b80*m.b122 - 2*m.b122 + 2*m.b81*m.b103 - 2*m.b103 + 2*
                       m.b81*m.b123 - 4*m.b123 + 2*m.b82*m.b83 - 2*m.b83 - 2*m.b82*m.b262 + 2*m.b83*m.b103 + 2*m.b84*
                       m.b85 - 2*m.b84 + 2*m.b84*m.b212 + 2*m.b212 + 2*m.b85*m.b352 + 2*m.b85*m.b355 - 2*m.b86*m.b214 + 
                       2*m.b86 - 2*m.b214 - 2*m.b86*m.b251 - 2*m.b86*m.b293 + 2*m.b86*m.b294 + 2*m.b87*m.b156 - 2*m.b87
                        + 2*m.b87*m.b214 - 2*m.b87*m.b304 + 2*m.b87*m.b339 + 2*m.b88*m.b186 + 2*m.b88*m.b318 - 2*m.b88*
                       m.b365 + 2*m.b89*m.b189 - 2*m.b89 + 2*m.b189 - 2*m.b89*m.b333 + 2*m.b89*m.b361 + 2*m.b89*m.b365
                        + 2*m.b90*m.b136 - 2*m.b136 - 2*m.b90*m.b226 + 2*m.b226 + 2*m.b90*m.b274 - 2*m.b91*m.b92 + 4*
                       m.b91 + 2*m.b92 - 2*m.b91*m.b268 - 2*m.b91*m.b269 - 2*m.b91*m.b334 + 2*m.b92*m.b307 - 2*m.b92*
                       m.b320 - 2*m.b92*m.b367 + 2*m.b93*m.b94 - 2*m.b94 - 2*m.b94*m.b143 - 2*m.b143 + 2*m.b94*m.b145 + 
                       2*m.b94*m.b172 - 4*m.b172 + 2*m.b95*m.b97 - 4*m.b97 + 2*m.b95*m.b308 + 2*m.b96*m.b99 - 4*m.b99 + 
                       2*m.b96*m.b237 - 4*m.b237 + 2*m.b96*m.b270 + 2*m.b97*m.b99 + 2*m.b97*m.b172 + 2*m.b97*m.b291 - 2*
                       m.b98*m.b100 + 2*m.b98 + 2*m.b98*m.b205 - 4*m.b205 - 2*m.b98*m.b248 - 2*m.b98*m.b321 + 2*m.b99*
                       m.b100 + 2*m.b99*m.b248 + 2*m.b100*m.b149 - 4*m.b149 + 2*m.b101*m.b102 + 2*m.b101*m.b148 - 2*
                       m.b148 + 2*m.b101*m.b336 + 2*m.b102*m.b126 - 2*m.b126 + 2*m.b102*m.b149 + 2*m.b103*m.b104 - 2*
                       m.b104 - 2*m.b103*m.b124 + 2*m.b124 + 2*m.b104*m.b126 - 2*m.b105*m.b284 + 2*m.b105 + 2*m.b105*
                       m.b286 - 2*m.b105*m.b345 - 2*m.b105*m.b368 + 2*m.b106*m.b129 - 2*m.b106 + 2*m.b106*m.b286 - 2*
                       m.b106*m.b295 + 2*m.b106*m.b345 + 2*m.b107*m.b217 + 2*m.b107*m.b311 - 2*m.b107*m.b369 - 2*m.b108*
                       m.b160 + 2*m.b160 + 2*m.b108*m.b257 - 2*m.b109*m.b134 - 2*m.b109 + 2*m.b109*m.b160 + 2*m.b109*
                       m.b365 + 2*m.b109*m.b369 - 2*m.b110*m.b112 + 2*m.b112 + 2*m.b110*m.b266 + 2*m.b111*m.b162 - 2*
                       m.b111 - 2*m.b162 - 2*m.b111*m.b193 + 2*m.b193 + 2*m.b111*m.b268 + 2*m.b111*m.b281 + 2*m.b112*
                       m.b193 - 2*m.b112*m.b334 - 2*m.b112*m.b370 - 2*m.b113*m.b114 + 2*m.b114 - 2*m.b113*m.b274 - 2*
                       m.b113*m.b275 + 2*m.b114*m.b115 - 2*m.b114*m.b324 - 2*m.b114*m.b371 + 2*m.b115*m.b141 - 2*m.b141
                        - 2*m.b115*m.b269 + 2*m.b116*m.b118 - 4*m.b118 + 2*m.b116*m.b234 + 2*m.b117*m.b118 - 4*m.b117 + 
                       2*m.b117*m.b141 + 2*m.b117*m.b234 + 2*m.b117*m.b290 + 2*m.b118*m.b172 + 2*m.b118*m.b203 - 4*
                       m.b203 + 2*m.b119*m.b120 - 4*m.b120 + 2*m.b119*m.b300 + 2*m.b120*m.b175 + 2*m.b175 + 2*m.b120*
                       m.b203 + 2*m.b120*m.b364 - 2*m.b121*m.b122 + 2*m.b121 + 2*m.b121*m.b174 - 4*m.b174 - 2*m.b121*
                       m.b206 - 2*m.b121*m.b315 + 2*m.b122*m.b178 - 4*m.b178 + 2*m.b122*m.b364 + 2*m.b123*m.b125 + 2*
                       m.b123*m.b177 - 2*m.b177 + 2*m.b123*m.b344 + 2*m.b124*m.b151 - 4*m.b151 - 2*m.b124*m.b247 - 2*
                       m.b124*m.b254 + 2*m.b125*m.b151 + 2*m.b125*m.b178 + 2*m.b126*m.b127 - 2*m.b127 - 2*m.b126*m.b209
                        + 2*m.b127*m.b151 - 2*m.b128*m.b277 + 2*m.b128 + 2*m.b128*m.b279 - 2*m.b128*m.b339 - 2*m.b128*
                       m.b372 - 2*m.b129*m.b131 + 2*m.b131 + 2*m.b129*m.b285 - 2*m.b130*m.b158 - 2*m.b158 + 2*m.b130*
                       m.b304 + 2*m.b131*m.b158 - 2*m.b131*m.b369 - 2*m.b131*m.b373 - 2*m.b132*m.b135 - 2*m.b135 + 2*
                       m.b132*m.b252 + 2*m.b133*m.b135 - 4*m.b133 + 2*m.b133*m.b158 + 2*m.b133*m.b333 + 2*m.b133*m.b369
                        + 2*m.b134*m.b137 + 2*m.b134*m.b313 + 2*m.b135*m.b137 + 2*m.b135*m.b296 + 2*m.b136*m.b257 + 2*
                       m.b136*m.b328 - 2*m.b136*m.b353 + 2*m.b137*m.b353 - 2*m.b138*m.b163 - 2*m.b138 + 2*m.b163 + 2*
                       m.b138*m.b259 + 2*m.b138*m.b288 + 2*m.b138*m.b313 - 2*m.b139*m.b226 - 2*m.b139*m.b282 - 2*m.b139*
                       m.b329 + 2*m.b140*m.b168 - 2*m.b168 + 2*m.b140*m.b269 + 2*m.b140*m.b329 + 2*m.b141*m.b143 - 2*
                       m.b141*m.b307 + 2*m.b142*m.b144 - 4*m.b144 + 2*m.b143*m.b144 + 2*m.b143*m.b168 + 2*m.b144*m.b203
                        + 2*m.b144*m.b236 - 4*m.b236 + 2*m.b145*m.b146 - 4*m.b146 + 2*m.b145*m.b292 + 2*m.b146*m.b147 + 
                       2*m.b147 + 2*m.b146*m.b236 + 2*m.b146*m.b360 - 2*m.b147*m.b148 - 2*m.b147*m.b176 + 2*m.b176 - 2*
                       m.b147*m.b308 + 2*m.b148*m.b208 - 2*m.b208 + 2*m.b148*m.b360 + 2*m.b149*m.b150 + 2*m.b149*m.b207
                        - 2*m.b207 + 2*m.b150*m.b179 - 4*m.b179 + 2*m.b150*m.b208 + 2*m.b151*m.b152 - 2*m.b152 + 2*
                       m.b152*m.b179 + 2*m.b153*m.b155 - 4*m.b155 - 2*m.b154*m.b271 + 2*m.b154 + 2*m.b154*m.b326 - 2*
                       m.b154*m.b330 - 2*m.b154*m.b331 + 2*m.b155*m.b271 + 2*m.b155*m.b331 + 2*m.b155*m.b338 - 2*m.b156*
                       m.b157 + 2*m.b157 + 2*m.b156*m.b278 + 2*m.b157*m.b187 - 2*m.b187 - 2*m.b157*m.b365 - 2*m.b157*
                       m.b375 + 2*m.b158*m.b159 - 4*m.b159 + 2*m.b159*m.b161 - 2*m.b161 + 2*m.b159*m.b187 + 2*m.b159*
                       m.b328 - 2*m.b160*m.b296 - 2*m.b160*m.b370 - 2*m.b161*m.b253 + 2*m.b161*m.b288 + 2*m.b161*m.b370
                        + 2*m.b162*m.b252 + 2*m.b162*m.b333 - 2*m.b162*m.b347 - 2*m.b163*m.b195 + 2*m.b163*m.b353 - 2*
                       m.b163*m.b374 - 2*m.b164*m.b165 + 2*m.b164 - 2*m.b165 - 2*m.b164*m.b193 + 2*m.b164*m.b227 - 2*
                       m.b227 - 2*m.b164*m.b289 + 2*m.b165*m.b167 + 2*m.b165*m.b320 + 2*m.b165*m.b374 - 2*m.b166*m.b199
                        + 2*m.b166 - 2*m.b199 - 2*m.b166*m.b289 - 2*m.b166*m.b290 + 2*m.b166*m.b348 + 2*m.b167*m.b199 + 
                       2*m.b167*m.b275 + 2*m.b168*m.b170 - 2*m.b168*m.b298 + 2*m.b169*m.b171 - 4*m.b171 + 2*m.b170*
                       m.b171 + 2*m.b170*m.b199 + 2*m.b171*m.b173 - 2*m.b173 + 2*m.b171*m.b236 + 2*m.b172*m.b174 + 2*
                       m.b173*m.b174 + 2*m.b173*m.b202 - 4*m.b202 - 2*m.b173*m.b246 + 2*m.b174*m.b354 - 2*m.b175*m.b177
                        - 2*m.b175*m.b250 - 2*m.b175*m.b300 - 2*m.b176*m.b241 - 2*m.b241 - 2*m.b176*m.b247 + 2*m.b176*
                       m.b270 + 2*m.b177*m.b241 + 2*m.b177*m.b354 + 2*m.b178*m.b240 - 4*m.b240 + 2*m.b178*m.b242 + 2*
                       m.b179*m.b262 + 2*m.b179*m.b376 - 2*m.b180*m.b284 + 2*m.b180 - 2*m.b180*m.b372 - 2*m.b181*m.b182
                        + 4*m.b181 - 2*m.b182 - 2*m.b181*m.b276 - 2*m.b181*m.b326 - 2*m.b181*m.b327 + 2*m.b182*m.b184 + 
                       2*m.b182*m.b339 + 2*m.b182*m.b372 + 2*m.b183*m.b185 - 4*m.b185 + 2*m.b183*m.b332 + 2*m.b183*
                       m.b357 + 2*m.b184*m.b185 + 2*m.b184*m.b276 + 2*m.b185*m.b303 + 2*m.b185*m.b375 + 2*m.b186*m.b332
                        - 2*m.b186*m.b362 + 2*m.b187*m.b188 - 2*m.b187*m.b265 + 2*m.b188*m.b190 - 2*m.b190 + 2*m.b188*
                       m.b218 - 2*m.b218 - 2*m.b189*m.b267 - 2*m.b189*m.b288 - 2*m.b189*m.b366 - 2*m.b190*m.b258 + 2*
                       m.b190*m.b281 + 2*m.b190*m.b366 - 2*m.b191*m.b194 + 2*m.b191 - 2*m.b194 - 2*m.b191*m.b268 - 2*
                       m.b191*m.b296 + 2*m.b191*m.b297 + 2*m.b192*m.b194 - 2*m.b192 - 2*m.b192*m.b313 + 2*m.b192*m.b341
                        + 2*m.b192*m.b366 - 2*m.b193*m.b371 + 2*m.b194*m.b195 + 2*m.b194*m.b371 - 2*m.b195*m.b196 - 2*
                       m.b196 + 2*m.b196*m.b198 + 2*m.b196*m.b314 + 2*m.b196*m.b371 - 2*m.b197*m.b231 - 2*m.b231 + 2*
                       m.b198*m.b231 + 2*m.b198*m.b282 + 2*m.b199*m.b201 + 2*m.b200*m.b202 + 2*m.b201*m.b202 + 2*m.b201*
                       m.b231 + 2*m.b202*m.b204 - 4*m.b204 + 2*m.b203*m.b205 + 2*m.b204*m.b205 + 2*m.b204*m.b235 - 4*
                       m.b235 + 2*m.b204*m.b246 + 2*m.b205*m.b350 + 2*m.b206*m.b261 - 2*m.b206*m.b263 + 2*m.b207*m.b263
                        - 2*m.b207*m.b291 + 2*m.b207*m.b350 + 2*m.b208*m.b210 - 2*m.b208*m.b250 + 2*m.b209*m.b244 + 2*
                       m.b209*m.b247 + 2*m.b210*m.b244 + 2*m.b210*m.b263 - 2*m.b211*m.b294 + 2*m.b211 - 2*m.b211*m.b368
                        - 2*m.b212*m.b213 - 2*m.b213 - 2*m.b212*m.b283 - 2*m.b212*m.b322 + 2*m.b213*m.b215 - 2*m.b215 + 
                       2*m.b213*m.b345 + 2*m.b213*m.b368 + 2*m.b214*m.b216 - 4*m.b216 + 2*m.b214*m.b352 + 2*m.b215*
                       m.b216 - 2*m.b215*m.b255 + 2*m.b215*m.b283 + 2*m.b216*m.b295 + 2*m.b216*m.b373 + 2*m.b217*m.b340
                        - 2*m.b217*m.b359 + 2*m.b218*m.b220 - 4*m.b220 - 2*m.b218*m.b273 + 2*m.b218*m.b362 - 2*m.b219*
                       m.b221 - 2*m.b219*m.b264 - 2*m.b219*m.b266 + 2*m.b220*m.b221 + 2*m.b220*m.b312 + 2*m.b220*m.b319
                        + 2*m.b221*m.b223 - 2*m.b223 - 2*m.b222*m.b225 + 2*m.b222 - 2*m.b225 - 2*m.b222*m.b257 + 2*
                       m.b222*m.b260 - 2*m.b222*m.b333 + 2*m.b223*m.b225 - 2*m.b223*m.b319 + 2*m.b223*m.b363 - 2*m.b224*
                       m.b227 - 2*m.b224*m.b274 - 2*m.b224*m.b288 + 2*m.b225*m.b227 + 2*m.b225*m.b334 + 2*m.b226*m.b363
                        - 2*m.b226*m.b367 + 2*m.b227*m.b367 + 2*m.b228*m.b229 - 2*m.b228 + 2*m.b228*m.b230 - 2*m.b228*
                       m.b305 + 2*m.b228*m.b367 - 2*m.b229*m.b348 - 2*m.b229*m.b349 + 2*m.b230*m.b289 + 2*m.b230*m.b349
                        + 2*m.b231*m.b233 + 2*m.b232*m.b235 - 2*m.b232*m.b349 + 2*m.b233*m.b235 + 2*m.b233*m.b349 + 2*
                       m.b234*m.b237 + 2*m.b235*m.b237 + 2*m.b236*m.b238 - 4*m.b238 + 2*m.b237*m.b238 + 2*m.b238*m.b239
                        - 2*m.b239 + 2*m.b238*m.b261 + 2*m.b239*m.b240 - 2*m.b239*m.b321 + 2*m.b239*m.b343 + 2*m.b240*
                       m.b254 + 2*m.b240*m.b291 + 2*m.b241*m.b242 + 2*m.b241*m.b243 - 2*m.b242*m.b377 + 2*m.b243*m.b254
                        + 2*m.b243*m.b377 - 2*m.b244*m.b378 + 2*m.b245*m.b290 - 2*m.b246*m.b270 + 2*m.b247*m.b248 - 2*
                       m.b248*m.b254 + 2*m.b249*m.b278 + 2*m.b251*m.b285 - 2*m.b252*m.b253 - 2*m.b252*m.b313 + 2*m.b255*
                       m.b256 + 2*m.b256*m.b271 - 2*m.b256*m.b331 - 2*m.b256*m.b332 - 2*m.b257*m.b258 - 2*m.b259*m.b260
                        + 2*m.b260*m.b296 - 2*m.b260*m.b306 - 2*m.b261*m.b325 - 2*m.b261*m.b344 - 2*m.b262*m.b263 - 2*
                       m.b264*m.b265 + 2*m.b265*m.b295 + 2*m.b265*m.b323 + 2*m.b266*m.b267 - 2*m.b266*m.b297 - 2*m.b267*
                       m.b312 - 2*m.b270*m.b336 - 2*m.b271*m.b272 + 2*m.b272*m.b310 + 2*m.b272*m.b331 + 2*m.b273*m.b303
                        + 2*m.b273*m.b318 - 2*m.b275*m.b307 + 2*m.b276*m.b277 - 2*m.b276*m.b279 + 2*m.b277*m.b322 - 2*
                       m.b277*m.b338 - 2*m.b278*m.b279 - 2*m.b278*m.b311 + 2*m.b279*m.b317 + 2*m.b280*m.b311 - 2*m.b280*
                       m.b312 - 2*m.b281*m.b319 - 2*m.b282*m.b298 + 2*m.b283*m.b284 - 2*m.b283*m.b286 + 2*m.b284*m.b316
                        - 2*m.b285*m.b286 - 2*m.b285*m.b304 - 2*m.b287*m.b303 + 2*m.b287*m.b304 - 2*m.b290*m.b299 - 2*
                       m.b291*m.b292 - 2*m.b292*m.b364 - 2*m.b293*m.b316 + 2*m.b294*m.b309 - 2*m.b294*m.b352 - 2*m.b297*
                       m.b328 + 2*m.b298*m.b342 - 2*m.b300*m.b360 - 2*m.b301*m.b309 - 2*m.b302*m.b355 - 2*m.b302*m.b357
                        - 2*m.b303*m.b317 - 2*m.b305*m.b306 + 2*m.b306*m.b347 + 2*m.b306*m.b374 - 2*m.b308*m.b354 + 2*
                       m.b310*m.b356 - 2*m.b310*m.b375 - 2*m.b311*m.b332 + 2*m.b312*m.b359 - 2*m.b314*m.b342 - 2*m.b315*
                       m.b350 + 2*m.b317*m.b351 - 2*m.b317*m.b373 - 2*m.b318*m.b340 - 2*m.b323*m.b346 + 2*m.b324*m.b329
                        + 2*m.b327*m.b368 - 2*m.b329*m.b374 + 2*m.b330*m.b372 + 2*m.b335*m.b336 - 2*m.b335*m.b337 - 2*
                       m.b336*m.b360 - 2*m.b339*m.b340 + 2*m.b340*m.b356 - 2*m.b341*m.b353 - 2*m.b343*m.b350 - 2*m.b344*
                       m.b364 - 2*m.b345*m.b346 + 2*m.b346*m.b351 + 2*m.b347*m.b370 - 2*m.b351*m.b352 - 2*m.b356*m.b357
                        - 2*m.b358*m.b359 + 2*m.b359*m.b373 - 2*m.b361*m.b362 + 2*m.b362*m.b375 - 2*m.b363*m.b366 - 2*
                       m.b376*m.b377 + 2*m.b377*m.b378 + m.x379 <= 0)
