#  MINLP written by GAMS Convert at 04/21/18 13:54:17
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        631        1      630        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        631        1      630        0


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
m.b379 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b380 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b381 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b382 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b383 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b384 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b385 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b386 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b387 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b388 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b389 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b390 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b391 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b392 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b393 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b394 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b395 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b396 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b397 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b398 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b399 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b400 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b401 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b402 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b403 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b404 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b405 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b406 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b407 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b408 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b409 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b410 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b411 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b412 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b413 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b414 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b415 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b416 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b417 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b418 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b419 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b420 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b421 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b422 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b423 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b424 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b425 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b426 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b427 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b428 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b429 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b430 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b431 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b432 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b433 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b434 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b435 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b436 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b437 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b438 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b439 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b440 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b441 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b442 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b443 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b444 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b445 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b446 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b447 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b448 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b449 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b450 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b451 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b452 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b453 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b454 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b455 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b456 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b457 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b458 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b459 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b460 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b461 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b462 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b463 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b464 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b465 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b466 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b467 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b468 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b469 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b470 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b471 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b472 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b473 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b474 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b475 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b476 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b477 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b478 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b479 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b480 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b481 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b482 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b483 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b484 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b485 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b486 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b487 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b488 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b489 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b490 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b491 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b492 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b493 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b494 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b495 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b496 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b497 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b498 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b499 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b500 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b501 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b502 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b503 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b504 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b505 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b506 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b507 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b508 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b509 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b510 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b511 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b512 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b513 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b514 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b515 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b516 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b517 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b518 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b519 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b520 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b521 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b522 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b523 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b524 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b525 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b526 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b527 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b528 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b529 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b530 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b531 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b532 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b533 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b534 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b535 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b536 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b537 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b538 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b539 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b540 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b541 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b542 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b543 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b544 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b545 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b546 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b547 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b548 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b549 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b550 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b551 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b552 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b553 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b554 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b555 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b556 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b557 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b558 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b559 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b560 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b561 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b562 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b563 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b564 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b565 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b566 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b567 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b568 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b569 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b570 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b571 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b572 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b573 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b574 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b575 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b576 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b577 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b578 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b579 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b580 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b581 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b582 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b583 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b584 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b585 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b586 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b587 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b588 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b589 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b590 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b591 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b592 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b593 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b594 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b595 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b596 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b597 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b598 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b599 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b600 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b601 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b602 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b603 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b604 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b605 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b606 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b607 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b608 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b609 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b610 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b611 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b612 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b613 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b614 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b615 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b616 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b617 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b618 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b619 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b620 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b621 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b622 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b623 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b624 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b625 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b626 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b627 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b628 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b629 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b630 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x631 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x631, sense=maximize)

m.c1 = Constraint(expr=(-2*m.b1*m.b259) - 2*m.b1 + 2*m.b259 + 2*m.b1*m.b293 - 2*m.b293 + 2*m.b1*m.b392 + 2*m.b1*m.b403
                        + 2*m.b2*m.b61 - 2*m.b2 - 2*m.b61 + 2*m.b2*m.b356 + 2*m.b356 + 2*m.b2*m.b402 - 2*m.b2*m.b439 + 2
                       *m.b3*m.b83 - 2*m.b3 - 2*m.b83 + 2*m.b3*m.b211 - 2*m.b211 + 2*m.b3*m.b313 + 2*m.b313 - 2*m.b3*
                       m.b450 + 2*m.b4*m.b106 - 2*m.b4 - 2*m.b106 - 2*m.b4*m.b181 + 2*m.b181 + 2*m.b4*m.b410 + 2*m.b4*
                       m.b411 + 2*m.b5*m.b359 - 2*m.b5 - 2*m.b359 + 2*m.b5*m.b361 + 2*m.b361 + 2*m.b5*m.b413 - 2*m.b5*
                       m.b498 + 2*m.b6*m.b66 - 2*m.b6 - 2*m.b66 - 2*m.b6*m.b368 + 4*m.b368 + 2*m.b6*m.b492 + 2*m.b6*
                       m.b493 + 2*m.b7*m.b127 - 2*m.b7 - 2*m.b127 - 2*m.b7*m.b209 + 2*m.b209 + 2*m.b7*m.b402 + 2*m.b7*
                       m.b420 - 2*m.b8*m.b37 - 2*m.b8 + 2*m.b37 + 2*m.b8*m.b66 + 2*m.b8*m.b87 - 2*m.b87 + 2*m.b8*m.b501
                        + 2*m.b9*m.b154 - 2*m.b9 - 4*m.b154 + 2*m.b9*m.b211 - 2*m.b9*m.b242 + 2*m.b242 + 2*m.b9*m.b430
                        + 2*m.b10*m.b87 - 2*m.b10 + 2*m.b10*m.b110 - 2*m.b110 - 2*m.b10*m.b512 + 2*m.b10*m.b513 + 2*
                       m.b11*m.b110 - 2*m.b11 + 2*m.b11*m.b131 - 2*m.b131 - 2*m.b11*m.b522 + 2*m.b11*m.b523 + 2*m.b12*
                       m.b20 - 2*m.b12 - 2*m.b20 + 2*m.b12*m.b296 - 4*m.b296 + 2*m.b13*m.b26 - 2*m.b13 - 2*m.b26 + 2*
                       m.b13*m.b442 + 2*m.b14*m.b131 - 2*m.b14 + 2*m.b14*m.b162 - 4*m.b162 + 2*m.b14*m.b189 - 4*m.b189
                        - 2*m.b14*m.b532 + 2*m.b15*m.b107 - 2*m.b15 - 2*m.b107 + 2*m.b15*m.b185 - 2*m.b185 - 2*m.b15*
                       m.b276 + 2*m.b276 + 2*m.b15*m.b401 + 2*m.b16*m.b162 - 2*m.b16 + 2*m.b16*m.b190 - 4*m.b190 + 2*
                       m.b16*m.b218 - 4*m.b218 - 2*m.b16*m.b543 + 2*m.b17*m.b31 - 2*m.b17 - 2*m.b31 + 2*m.b17*m.b525 + 2
                       *m.b18*m.b190 - 4*m.b18 + 2*m.b18*m.b220 - 4*m.b220 + 2*m.b18*m.b250 - 4*m.b250 + 2*m.b18*m.b543
                        + 2*m.b19*m.b68 - 2*m.b19 - 4*m.b68 - 2*m.b19*m.b110 + 2*m.b19*m.b220 + 2*m.b19*m.b533 + 2*m.b20
                       *m.b21 - 2*m.b21 - 2*m.b20*m.b53 - 2*m.b53 + 2*m.b20*m.b114 - 4*m.b114 + 2*m.b21*m.b43 - 2*m.b43
                        + 2*m.b22*m.b220 - 4*m.b22 + 2*m.b22*m.b252 - 4*m.b252 + 2*m.b22*m.b284 - 4*m.b284 + 2*m.b22*
                       m.b532 + 2*m.b23*m.b40 - 2*m.b23 - 2*m.b40 - 2*m.b23*m.b87 + 2*m.b23*m.b89 - 4*m.b89 + 2*m.b23*
                       m.b252 + 2*m.b24*m.b25 - 2*m.b24 - 2*m.b25 - 2*m.b24*m.b42 - 2*m.b42 + 2*m.b24*m.b139 - 4*m.b139
                        + 2*m.b24*m.b545 + 2*m.b25*m.b54 - 4*m.b54 - 2*m.b26*m.b263 + 2*m.b263 + 2*m.b26*m.b393 + 2*
                       m.b26*m.b535 - 2*m.b27*m.b352 + 2*m.b27 + 2*m.b352 - 2*m.b27*m.b417 + 2*m.b27*m.b461 - 2*m.b27*
                       m.b566 + 2*m.b28*m.b252 - 4*m.b28 + 2*m.b28*m.b286 - 4*m.b286 + 2*m.b28*m.b324 - 4*m.b324 + 2*
                       m.b28*m.b522 + 2*m.b29*m.b51 - 2*m.b29 - 4*m.b51 - 2*m.b29*m.b66 + 2*m.b29*m.b112 - 4*m.b112 + 2*
                       m.b29*m.b286 - 2*m.b30*m.b31 - 2*m.b30 + 2*m.b30*m.b52 - 2*m.b52 + 2*m.b30*m.b73 - 4*m.b73 + 2*
                       m.b30*m.b557 + 2*m.b31*m.b32 - 2*m.b32 + 2*m.b31*m.b170 - 4*m.b170 + 2*m.b32*m.b73 - 2*m.b33*
                       m.b298 - 2*m.b33 + 2*m.b298 + 2*m.b33*m.b390 + 2*m.b33*m.b443 + 2*m.b33*m.b526 + 2*m.b34*m.b46 + 
                       2*m.b34 + 2*m.b46 - 2*m.b34*m.b57 + 4*m.b57 - 2*m.b34*m.b345 - 2*m.b345 - 2*m.b34*m.b405 + 2*
                       m.b35*m.b36 - 2*m.b35 - 2*m.b36 + 2*m.b35*m.b62 - 2*m.b62 + 2*m.b35*m.b158 - 4*m.b158 - 2*m.b35*
                       m.b451 + 2*m.b36*m.b63 - 2*m.b63 + 2*m.b36*m.b108 - 2*m.b108 - 2*m.b36*m.b246 - 2*m.b246 + 2*
                       m.b37*m.b49 - 2*m.b49 - 2*m.b37*m.b109 + 2*m.b109 - 2*m.b37*m.b386 + 2*m.b38*m.b286 - 4*m.b38 + 2
                       *m.b38*m.b326 - 4*m.b326 + 2*m.b38*m.b369 - 4*m.b369 + 2*m.b38*m.b512 + 2*m.b39*m.b68 - 2*m.b39
                        + 2*m.b39*m.b133 - 4*m.b133 + 2*m.b39*m.b326 - 2*m.b39*m.b493 + 2*m.b40*m.b328 - 4*m.b328 + 2*
                       m.b40*m.b514 - 2*m.b40*m.b544 + 2*m.b41*m.b42 - 2*m.b41 + 2*m.b41*m.b559 - 2*m.b41*m.b568 + 2*
                       m.b41*m.b569 + 2*m.b42*m.b71 - 4*m.b71 + 2*m.b42*m.b92 - 4*m.b92 + 2*m.b43*m.b44 - 2*m.b44 + 2*
                       m.b43*m.b198 - 4*m.b198 - 2*m.b43*m.b559 + 2*m.b44*m.b92 + 2*m.b45*m.b47 + 2*m.b45 - 4*m.b47 - 2*
                       m.b45*m.b78 + 4*m.b78 - 2*m.b45*m.b302 - 2*m.b302 - 2*m.b45*m.b398 - 2*m.b46*m.b406 - 2*m.b46*
                       m.b583 - 2*m.b46*m.b584 + 2*m.b47*m.b233 - 4*m.b233 + 2*m.b47*m.b416 + 2*m.b47*m.b584 + 2*m.b48*
                       m.b150 - 2*m.b48 - 2*m.b150 + 2*m.b48*m.b207 - 4*m.b207 - 2*m.b48*m.b237 + 2*m.b237 + 2*m.b48*
                       m.b397 + 2*m.b49*m.b326 + 2*m.b49*m.b371 - 2*m.b371 - 2*m.b49*m.b385 + 2*m.b50*m.b89 - 4*m.b50 + 
                       2*m.b50*m.b164 - 4*m.b164 + 2*m.b50*m.b371 + 2*m.b50*m.b493 + 2*m.b51*m.b134 - 4*m.b134 + 2*m.b51
                       *m.b502 + 2*m.b51*m.b534 + 2*m.b52*m.b53 + 2*m.b52*m.b137 - 2*m.b137 - 2*m.b52*m.b578 + 2*m.b53*
                       m.b90 - 4*m.b90 + 2*m.b53*m.b115 - 4*m.b115 + 2*m.b54*m.b55 - 2*m.b55 + 2*m.b54*m.b382 - 2*m.b382
                        + 2*m.b54*m.b559 + 2*m.b55*m.b115 + 2*m.b56*m.b58 + 2*m.b56 - 4*m.b58 - 2*m.b56*m.b98 + 4*m.b98
                        - 2*m.b56*m.b395 - 2*m.b56*m.b436 - 2*m.b57*m.b416 - 2*m.b57*m.b574 - 2*m.b57*m.b575 + 2*m.b58*
                       m.b426 + 2*m.b58*m.b575 + 2*m.b58*m.b583 + 2*m.b59*m.b60 - 2*m.b59 - 2*m.b60 + 2*m.b59*m.b238 - 4
                       *m.b238 - 2*m.b59*m.b268 + 2*m.b268 + 2*m.b59*m.b506 + 2*m.b60*m.b240 + 2*m.b240 - 2*m.b60*m.b351
                        + 2*m.b351 + 2*m.b60*m.b399 - 2*m.b61*m.b274 + 2*m.b274 + 2*m.b61*m.b529 + 2*m.b61*m.b593 + 2*
                       m.b62*m.b64 - 4*m.b64 + 2*m.b62*m.b107 - 2*m.b62*m.b321 + 4*m.b321 + 2*m.b63*m.b65 - 4*m.b65 + 2*
                       m.b63*m.b366 - 2*m.b366 - 2*m.b63*m.b491 + 2*m.b64*m.b65 + 2*m.b64*m.b386 + 2*m.b64*m.b567 + 2*
                       m.b65*m.b323 + 2*m.b323 + 2*m.b65*m.b385 + 2*m.b66*m.b67 - 2*m.b67 + 2*m.b67*m.b112 + 2*m.b67*
                       m.b193 - 4*m.b193 - 2*m.b67*m.b372 - 2*m.b372 + 2*m.b68*m.b494 + 2*m.b68*m.b544 - 2*m.b69*m.b70
                        - 2*m.b69 + 2*m.b70 + 2*m.b69*m.b387 + 2*m.b69*m.b392 + 2*m.b69*m.b544 + 2*m.b70*m.b113 - 4*
                       m.b113 - 2*m.b70*m.b557 - 2*m.b70*m.b595 + 2*m.b71*m.b72 - 2*m.b72 + 2*m.b71*m.b167 - 2*m.b167 + 
                       2*m.b71*m.b578 + 2*m.b72*m.b113 + 2*m.b72*m.b140 - 4*m.b140 - 2*m.b72*m.b525 + 2*m.b73*m.b74 - 2*
                       m.b74 + 2*m.b73*m.b336 - 2*m.b336 + 2*m.b74*m.b140 - 2*m.b75*m.b142 + 4*m.b75 + 2*m.b142 - 2*
                       m.b75*m.b394 - 2*m.b75*m.b504 - 2*m.b75*m.b592 - 2*m.b76*m.b117 + 2*m.b76 + 2*m.b117 - 2*m.b76*
                       m.b338 - 2*m.b338 - 2*m.b76*m.b496 + 2*m.b76*m.b592 + 2*m.b77*m.b232 - 2*m.b77 - 2*m.b232 - 2*
                       m.b77*m.b405 + 2*m.b77*m.b444 + 2*m.b77*m.b592 - 2*m.b78*m.b426 - 2*m.b78*m.b564 - 2*m.b78*m.b565
                        + 2*m.b79*m.b437 - 4*m.b79 + 2*m.b79*m.b446 + 2*m.b79*m.b565 + 2*m.b79*m.b574 + 2*m.b80*m.b81 - 
                       2*m.b80 - 2*m.b81 + 2*m.b80*m.b269 - 4*m.b269 - 2*m.b80*m.b305 + 2*m.b305 + 2*m.b80*m.b518 + 2*
                       m.b81*m.b208 + 2*m.b208 + 2*m.b81*m.b407 - 2*m.b81*m.b596 - 2*m.b82*m.b155 + 2*m.b82 - 2*m.b155
                        - 2*m.b82*m.b418 + 2*m.b82*m.b507 - 2*m.b82*m.b585 + 2*m.b83*m.b155 - 2*m.b83*m.b311 + 2*m.b311
                        + 2*m.b83*m.b540 + 2*m.b84*m.b155 - 4*m.b84 + 2*m.b84*m.b157 - 2*m.b157 + 2*m.b84*m.b418 + 2*
                       m.b84*m.b541 - 2*m.b85*m.b86 - 2*m.b85 + 2*m.b86 + 2*m.b85*m.b366 + 2*m.b85*m.b440 + 2*m.b85*
                       m.b577 - 2*m.b86*m.b368 + 2*m.b86*m.b492 - 2*m.b86*m.b597 + 2*m.b87*m.b88 - 2*m.b88 + 2*m.b88*
                       m.b133 + 2*m.b88*m.b223 - 4*m.b223 - 2*m.b88*m.b327 - 2*m.b327 + 2*m.b89*m.b376 + 2*m.b376 + 2*
                       m.b89*m.b481 + 2*m.b90*m.b91 - 4*m.b91 + 2*m.b90*m.b196 - 2*m.b196 + 2*m.b90*m.b568 + 2*m.b91*
                       m.b138 - 4*m.b138 + 2*m.b91*m.b171 - 2*m.b171 + 2*m.b91*m.b525 + 2*m.b92*m.b93 - 2*m.b93 + 2*
                       m.b92*m.b294 - 4*m.b294 + 2*m.b93*m.b171 + 2*m.b94*m.b201 - 2*m.b94 - 2*m.b201 + 2*m.b94*m.b425
                        + 2*m.b94*m.b485 - 2*m.b94*m.b599 - 2*m.b95*m.b204 + 2*m.b95 - 2*m.b204 + 2*m.b95*m.b265 - 4*
                       m.b265 - 2*m.b95*m.b300 - 2*m.b300 - 2*m.b95*m.b504 + 2*m.b96*m.b265 - 2*m.b96 - 2*m.b96*m.b398
                        + 2*m.b96*m.b457 + 2*m.b96*m.b588 + 2*m.b97*m.b233 - 2*m.b97 + 2*m.b97*m.b516 + 2*m.b97*m.b562
                        - 2*m.b97*m.b564 - 2*m.b98*m.b121 - 2*m.b121 - 2*m.b98*m.b437 - 2*m.b98*m.b554 + 2*m.b99*m.b448
                        - 4*m.b99 + 2*m.b99*m.b459 + 2*m.b99*m.b554 + 2*m.b99*m.b564 - 2*m.b100*m.b437 + 2*m.b100 - 2*
                       m.b100*m.b438 + 2*m.b100*m.b565 - 2*m.b100*m.b596 - 2*m.b101*m.b426 - 2*m.b101 + 2*m.b101*m.b449
                        + 2*m.b101*m.b554 + 2*m.b101*m.b596 + 2*m.b102*m.b103 - 2*m.b102 - 4*m.b103 + 2*m.b102*m.b306 - 
                       4*m.b306 - 2*m.b102*m.b349 + 2*m.b349 + 2*m.b102*m.b528 + 2*m.b103*m.b180 + 2*m.b180 + 2*m.b103*
                       m.b417 + 2*m.b103*m.b596 + 2*m.b104*m.b106 - 2*m.b104 + 2*m.b104*m.b181 - 2*m.b104*m.b272 + 2*
                       m.b272 + 2*m.b104*m.b399 - 2*m.b105*m.b182 + 2*m.b105 - 2*m.b182 - 2*m.b105*m.b427 + 2*m.b105*
                       m.b497 - 2*m.b105*m.b576 + 2*m.b106*m.b182 - 2*m.b106*m.b354 + 2*m.b354 + 2*m.b107*m.b278 - 2*
                       m.b278 - 2*m.b107*m.b319 + 4*m.b319 - 2*m.b108*m.b109 + 2*m.b108*m.b431 + 2*m.b108*m.b478 + 2*
                       m.b109*m.b501 - 2*m.b109*m.b601 + 2*m.b110*m.b111 - 2*m.b111 + 2*m.b111*m.b164 + 2*m.b111*m.b255
                        - 4*m.b255 - 2*m.b111*m.b287 - 2*m.b287 + 2*m.b112*m.b467 + 2*m.b112*m.b524 + 2*m.b113*m.b114 + 
                       2*m.b113*m.b228 - 2*m.b228 + 2*m.b114*m.b168 - 4*m.b168 + 2*m.b114*m.b199 - 2*m.b199 + 2*m.b115*
                       m.b116 - 2*m.b116 + 2*m.b115*m.b337 - 4*m.b337 + 2*m.b116*m.b199 + 2*m.b117*m.b471 - 2*m.b117*
                       m.b535 - 2*m.b117*m.b603 + 2*m.b118*m.b120 + 2*m.b118 - 2*m.b120 - 2*m.b118*m.b174 + 2*m.b174 - 2
                       *m.b118*m.b393 - 2*m.b118*m.b471 - 2*m.b119*m.b176 + 2*m.b119 - 2*m.b176 + 2*m.b119*m.b301 - 4*
                       m.b301 - 2*m.b119*m.b496 - 2*m.b119*m.b536 + 2*m.b120*m.b301 - 2*m.b120*m.b395 + 2*m.b120*m.b581
                        + 2*m.b121*m.b123 - 4*m.b123 + 2*m.b121*m.b301 + 2*m.b121*m.b573 - 2*m.b122*m.b446 + 4*m.b122 - 
                       2*m.b122*m.b448 - 2*m.b122*m.b547 - 2*m.b122*m.b548 + 2*m.b123*m.b460 + 2*m.b123*m.b472 + 2*
                       m.b123*m.b548 - 2*m.b124*m.b351 + 2*m.b124 - 2*m.b124*m.b448 - 2*m.b124*m.b449 + 2*m.b124*m.b575
                        + 2*m.b125*m.b351 - 2*m.b125 - 2*m.b125*m.b416 + 2*m.b125*m.b461 + 2*m.b125*m.b548 + 2*m.b126*
                       m.b127 - 2*m.b126 - 2*m.b126*m.b309 + 2*m.b309 + 2*m.b126*m.b407 + 2*m.b126*m.b450 + 2*m.b127*
                       m.b210 - 2*m.b210 - 2*m.b127*m.b605 + 2*m.b128*m.b184 - 2*m.b128 + 2*m.b184 + 2*m.b128*m.b210 - 2
                       *m.b128*m.b315 + 2*m.b315 + 2*m.b128*m.b593 - 2*m.b129*m.b281 - 2*m.b129 + 2*m.b281 + 2*m.b129*
                       m.b440 + 2*m.b129*m.b510 + 2*m.b129*m.b542 - 2*m.b130*m.b465 + 2*m.b130 - 2*m.b130*m.b512 + 2*
                       m.b130*m.b513 - 2*m.b130*m.b607 + 2*m.b131*m.b132 - 2*m.b132 - 2*m.b131*m.b534 + 2*m.b132*m.b193
                        - 2*m.b132*m.b253 - 2*m.b253 + 2*m.b132*m.b288 - 4*m.b288 + 2*m.b133*m.b135 - 4*m.b135 + 2*
                       m.b133*m.b514 + 2*m.b134*m.b136 - 4*m.b136 + 2*m.b134*m.b331 - 4*m.b331 + 2*m.b134*m.b434 + 2*
                       m.b135*m.b136 + 2*m.b135*m.b288 + 2*m.b135*m.b466 + 2*m.b136*m.b137 + 2*m.b136*m.b389 + 2*m.b137*
                       m.b197 - 4*m.b197 - 2*m.b137*m.b415 + 2*m.b138*m.b139 + 2*m.b138*m.b260 - 2*m.b260 + 2*m.b138*
                       m.b558 + 2*m.b139*m.b197 + 2*m.b139*m.b230 - 2*m.b230 + 2*m.b140*m.b141 - 2*m.b141 + 2*m.b140*
                       m.b383 - 4*m.b383 + 2*m.b141*m.b230 + 2*m.b142*m.b458 - 2*m.b142*m.b526 - 2*m.b142*m.b608 - 2*
                       m.b143*m.b144 + 2*m.b143 + 2*m.b144 + 2*m.b143*m.b145 - 4*m.b145 - 2*m.b143*m.b390 - 2*m.b143*
                       m.b485 + 2*m.b144*m.b344 - 4*m.b344 - 2*m.b144*m.b546 - 2*m.b144*m.b582 + 2*m.b145*m.b344 + 2*
                       m.b145*m.b395 + 2*m.b145*m.b572 - 2*m.b146*m.b147 + 4*m.b146 + 2*m.b147 - 2*m.b146*m.b459 - 2*
                       m.b146*m.b460 - 2*m.b146*m.b537 + 2*m.b147*m.b149 - 2*m.b149 - 2*m.b147*m.b349 - 2*m.b147*m.b609
                        - 2*m.b148*m.b307 + 2*m.b148 + 2*m.b307 - 2*m.b148*m.b460 - 2*m.b148*m.b461 + 2*m.b148*m.b584 + 
                       2*m.b149*m.b307 - 2*m.b149*m.b406 + 2*m.b149*m.b473 - 2*m.b150*m.b152 + 2*m.b152 + 2*m.b150*
                       m.b396 + 2*m.b150*m.b438 - 2*m.b151*m.b506 + 4*m.b151 - 2*m.b151*m.b507 - 2*m.b151*m.b604 - 2*
                       m.b151*m.b605 - 2*m.b152*m.b497 + 2*m.b152*m.b605 - 2*m.b152*m.b610 + 2*m.b153*m.b154 - 2*m.b153
                        - 2*m.b153*m.b352 + 2*m.b153*m.b417 + 2*m.b153*m.b439 + 2*m.b154*m.b243 - 2*m.b243 + 2*m.b154*
                       m.b605 + 2*m.b155*m.b156 - 2*m.b156 + 2*m.b156*m.b243 - 2*m.b156*m.b358 + 2*m.b358 + 2*m.b156*
                       m.b509 + 2*m.b157*m.b158 - 2*m.b157*m.b183 - 2*m.b183 + 2*m.b157*m.b278 + 2*m.b158*m.b160 - 2*
                       m.b160 + 2*m.b158*m.b509 - 2*m.b159*m.b247 - 2*m.b159 + 2*m.b247 + 2*m.b159*m.b431 + 2*m.b159*
                       m.b499 + 2*m.b159*m.b531 + 2*m.b160*m.b245 - 2*m.b245 + 2*m.b160*m.b247 - 2*m.b160*m.b363 + 2*
                       m.b363 - 2*m.b161*m.b453 + 2*m.b161 - 2*m.b161*m.b522 + 2*m.b161*m.b523 - 2*m.b161*m.b611 + 2*
                       m.b162*m.b163 - 2*m.b163 + 2*m.b162*m.b328 - 2*m.b163*m.b221 - 2*m.b221 + 2*m.b163*m.b223 + 2*
                       m.b163*m.b330 - 4*m.b330 + 2*m.b164*m.b165 - 4*m.b165 + 2*m.b164*m.b502 + 2*m.b165*m.b290 + 2*
                       m.b290 + 2*m.b165*m.b330 + 2*m.b165*m.b602 - 2*m.b166*m.b167 + 2*m.b166 + 2*m.b166*m.b289 - 2*
                       m.b289 - 2*m.b166*m.b389 - 2*m.b166*m.b524 + 2*m.b167*m.b229 - 4*m.b229 + 2*m.b167*m.b602 + 2*
                       m.b168*m.b170 + 2*m.b168*m.b291 - 2*m.b291 + 2*m.b168*m.b569 - 2*m.b169*m.b199 + 2*m.b169 + 2*
                       m.b169*m.b262 - 4*m.b262 - 2*m.b169*m.b381 - 2*m.b381 - 2*m.b169*m.b388 + 2*m.b170*m.b229 + 2*
                       m.b170*m.b262 + 2*m.b171*m.b172 - 2*m.b172 - 2*m.b171*m.b403 + 2*m.b172*m.b262 - 2*m.b173*m.b340
                        + 2*m.b173 + 2*m.b340 + 2*m.b173*m.b445 - 2*m.b173*m.b515 - 2*m.b173*m.b612 + 2*m.b174*m.b177 - 
                       2*m.b177 - 2*m.b174*m.b553 - 2*m.b174*m.b573 + 2*m.b175*m.b177 - 4*m.b175 + 2*m.b175*m.b398 + 2*
                       m.b175*m.b496 + 2*m.b175*m.b563 + 2*m.b176*m.b233 + 2*m.b176*m.b537 + 2*m.b176*m.b587 - 2*m.b177*
                       m.b472 + 2*m.b177*m.b537 - 2*m.b178*m.b270 + 2*m.b178 + 2*m.b270 + 2*m.b178*m.b348 - 4*m.b348 - 2
                       *m.b178*m.b473 - 2*m.b178*m.b584 + 2*m.b179*m.b270 - 4*m.b179 + 2*m.b179*m.b416 + 2*m.b179*m.b486
                        + 2*m.b179*m.b538 - 2*m.b180*m.b354 - 2*m.b180*m.b518 - 2*m.b180*m.b519 - 2*m.b181*m.b462 - 2*
                       m.b181*m.b615 + 2*m.b182*m.b183 + 2*m.b182*m.b594 + 2*m.b183*m.b498 + 2*m.b183*m.b615 - 2*m.b184*
                       m.b430 - 2*m.b184*m.b490 - 2*m.b184*m.b606 - 2*m.b185*m.b216 + 2*m.b216 + 2*m.b185*m.b421 + 2*
                       m.b185*m.b490 + 2*m.b186*m.b216 - 2*m.b186 + 2*m.b186*m.b279 - 2*m.b279 - 2*m.b186*m.b567 + 2*
                       m.b186*m.b606 - 2*m.b187*m.b188 + 2*m.b187 + 2*m.b188 - 2*m.b187*m.b363 - 2*m.b187*m.b412 + 2*
                       m.b187*m.b441 + 2*m.b188*m.b189 - 2*m.b188*m.b532 - 2*m.b188*m.b617 + 2*m.b189*m.b219 - 2*m.b219
                        + 2*m.b189*m.b433 + 2*m.b190*m.b192 - 4*m.b192 + 2*m.b190*m.b534 + 2*m.b191*m.b192 - 4*m.b191 + 
                       2*m.b191*m.b219 + 2*m.b191*m.b328 + 2*m.b191*m.b480 + 2*m.b192*m.b255 + 2*m.b192*m.b375 - 4*
                       m.b375 + 2*m.b193*m.b194 - 4*m.b194 + 2*m.b193*m.b494 + 2*m.b194*m.b258 + 2*m.b258 + 2*m.b194*
                       m.b375 + 2*m.b194*m.b598 - 2*m.b195*m.b196 + 2*m.b195 + 2*m.b195*m.b257 - 4*m.b257 - 2*m.b195*
                       m.b414 - 2*m.b195*m.b514 + 2*m.b196*m.b261 - 2*m.b261 + 2*m.b196*m.b598 + 2*m.b197*m.b198 + 2*
                       m.b197*m.b334 - 2*m.b334 + 2*m.b198*m.b261 + 2*m.b198*m.b295 - 4*m.b295 + 2*m.b199*m.b200 - 2*
                       m.b200 + 2*m.b200*m.b295 + 2*m.b201*m.b579 - 2*m.b202*m.b435 - 2*m.b202 + 2*m.b202*m.b442 + 2*
                       m.b202*m.b553 + 2*m.b202*m.b579 + 2*m.b203*m.b205 - 4*m.b203 - 2*m.b205 + 2*m.b203*m.b405 + 2*
                       m.b203*m.b504 + 2*m.b203*m.b553 + 2*m.b204*m.b343 - 2*m.b343 + 2*m.b204*m.b527 + 2*m.b204*m.b583
                        - 2*m.b205*m.b459 + 2*m.b205*m.b527 + 2*m.b205*m.b562 - 2*m.b206*m.b239 + 2*m.b206 + 2*m.b239 + 
                       2*m.b206*m.b304 - 4*m.b304 - 2*m.b206*m.b486 - 2*m.b206*m.b575 + 2*m.b207*m.b239 + 2*m.b207*
                       m.b426 + 2*m.b207*m.b549 - 2*m.b208*m.b311 - 2*m.b208*m.b528 - 2*m.b208*m.b529 - 2*m.b209*m.b474
                        + 2*m.b209*m.b540 - 2*m.b209*m.b620 + 2*m.b210*m.b212 - 4*m.b212 - 2*m.b210*m.b439 + 2*m.b211*
                       m.b401 - 2*m.b211*m.b489 + 2*m.b212*m.b358 + 2*m.b212*m.b489 + 2*m.b212*m.b620 + 2*m.b213*m.b215
                        - 2*m.b213 - 2*m.b215 + 2*m.b213*m.b489 - 2*m.b213*m.b530 + 2*m.b213*m.b600 + 2*m.b214*m.b412 - 
                       2*m.b214 + 2*m.b214*m.b477 + 2*m.b214*m.b510 - 2*m.b214*m.b511 + 2*m.b215*m.b317 - 2*m.b317 + 2*
                       m.b215*m.b511 - 2*m.b215*m.b577 - 2*m.b216*m.b321 - 2*m.b216*m.b617 - 2*m.b217*m.b319 + 2*m.b217
                        - 2*m.b217*m.b421 + 2*m.b217*m.b433 - 2*m.b217*m.b551 + 2*m.b218*m.b251 - 2*m.b251 + 2*m.b218*
                       m.b441 + 2*m.b218*m.b551 + 2*m.b219*m.b221 - 2*m.b219*m.b523 + 2*m.b220*m.b222 - 4*m.b222 + 2*
                       m.b221*m.b222 + 2*m.b221*m.b251 + 2*m.b222*m.b224 - 2*m.b224 + 2*m.b222*m.b288 + 2*m.b223*m.b225
                        - 4*m.b225 + 2*m.b223*m.b481 + 2*m.b224*m.b225 + 2*m.b224*m.b329 - 4*m.b329 - 2*m.b224*m.b387 + 
                       2*m.b225*m.b226 + 2*m.b226 + 2*m.b225*m.b595 - 2*m.b226*m.b228 - 2*m.b226*m.b259 - 2*m.b226*
                       m.b502 - 2*m.b227*m.b258 + 2*m.b227 - 2*m.b227*m.b292 - 2*m.b292 - 2*m.b227*m.b388 + 2*m.b227*
                       m.b434 + 2*m.b228*m.b292 + 2*m.b228*m.b595 + 2*m.b229*m.b379 - 4*m.b379 + 2*m.b229*m.b382 - 2*
                       m.b230*m.b293 + 2*m.b230*m.b622 - 2*m.b231*m.b424 - 2*m.b231 + 2*m.b231*m.b454 + 2*m.b231*m.b546
                        + 2*m.b231*m.b570 + 2*m.b232*m.b234 - 2*m.b234 - 2*m.b232*m.b516 + 2*m.b232*m.b574 + 2*m.b233*
                       m.b235 - 4*m.b235 + 2*m.b234*m.b235 + 2*m.b234*m.b447 - 2*m.b234*m.b517 + 2*m.b235*m.b236 - 2*
                       m.b236 + 2*m.b235*m.b406 + 2*m.b236*m.b238 + 2*m.b236*m.b268 - 2*m.b236*m.b505 + 2*m.b237*m.b267
                        - 4*m.b267 - 2*m.b237*m.b565 - 2*m.b237*m.b566 + 2*m.b238*m.b437 + 2*m.b238*m.b566 - 2*m.b239*
                       m.b408 - 2*m.b239*m.b619 - 2*m.b240*m.b271 + 2*m.b271 - 2*m.b240*m.b274 - 2*m.b240*m.b540 + 2*
                       m.b241*m.b274 - 2*m.b241 - 2*m.b241*m.b462 + 2*m.b241*m.b528 + 2*m.b241*m.b619 - 2*m.b242*m.b487
                        + 2*m.b242*m.b529 - 2*m.b242*m.b625 + 2*m.b243*m.b244 - 4*m.b244 - 2*m.b243*m.b450 + 2*m.b244*
                       m.b315 + 2*m.b244*m.b476 + 2*m.b244*m.b625 + 2*m.b245*m.b246 + 2*m.b245*m.b476 - 2*m.b245*m.b541
                        + 2*m.b246*m.b360 - 2*m.b360 + 2*m.b246*m.b500 - 2*m.b247*m.b282 + 4*m.b282 - 2*m.b247*m.b611 - 
                       2*m.b248*m.b249 + 4*m.b248 - 2*m.b249 - 2*m.b248*m.b281 - 2*m.b248*m.b431 - 2*m.b248*m.b433 + 2*
                       m.b249*m.b250 + 2*m.b249*m.b543 + 2*m.b249*m.b611 + 2*m.b250*m.b285 - 2*m.b285 + 2*m.b250*m.b452
                        + 2*m.b251*m.b253 - 2*m.b251*m.b513 + 2*m.b252*m.b254 - 4*m.b254 + 2*m.b253*m.b254 + 2*m.b253*
                       m.b285 + 2*m.b254*m.b256 - 4*m.b256 + 2*m.b254*m.b330 + 2*m.b255*m.b257 + 2*m.b255*m.b467 + 2*
                       m.b256*m.b257 + 2*m.b256*m.b374 - 4*m.b374 + 2*m.b256*m.b387 + 2*m.b257*m.b591 - 2*m.b258*m.b260
                        - 2*m.b258*m.b494 - 2*m.b259*m.b335 - 2*m.b335 + 2*m.b259*m.b423 + 2*m.b260*m.b335 + 2*m.b260*
                       m.b591 + 2*m.b261*m.b336 - 2*m.b261*m.b392 + 2*m.b262*m.b627 + 2*m.b263*m.b536 - 2*m.b263*m.b570
                        - 2*m.b263*m.b572 + 2*m.b264*m.b435 - 4*m.b264 + 2*m.b264*m.b468 + 2*m.b264*m.b536 + 2*m.b264*
                       m.b561 + 2*m.b265*m.b266 - 2*m.b266 + 2*m.b265*m.b564 + 2*m.b266*m.b436 - 2*m.b266*m.b505 + 2*
                       m.b266*m.b618 + 2*m.b267*m.b269 + 2*m.b267*m.b505 + 2*m.b267*m.b618 - 2*m.b268*m.b554 - 2*m.b268*
                       m.b556 + 2*m.b269*m.b448 + 2*m.b269*m.b556 - 2*m.b270*m.b400 - 2*m.b270*m.b614 + 2*m.b271*m.b273
                        - 4*m.b273 - 2*m.b271*m.b449 - 2*m.b271*m.b539 - 2*m.b272*m.b308 + 2*m.b308 + 2*m.b272*m.b397 - 
                       2*m.b272*m.b589 + 2*m.b273*m.b474 + 2*m.b273*m.b589 + 2*m.b273*m.b614 - 2*m.b274*m.b626 + 2*
                       m.b275*m.b276 - 4*m.b275 + 2*m.b275*m.b277 - 2*m.b277 + 2*m.b275*m.b521 + 2*m.b275*m.b615 - 2*
                       m.b276*m.b279 - 2*m.b276*m.b594 + 2*m.b277*m.b279 - 2*m.b277*m.b410 + 2*m.b277*m.b463 - 2*m.b278*
                       m.b280 - 2*m.b280 + 2*m.b278*m.b429 + 2*m.b279*m.b280 + 2*m.b280*m.b491 + 2*m.b280*m.b577 + 2*
                       m.b281*m.b600 - 2*m.b281*m.b607 - 2*m.b282*m.b283 - 2*m.b283 - 2*m.b282*m.b440 - 2*m.b282*m.b441
                        + 2*m.b283*m.b284 + 2*m.b283*m.b532 + 2*m.b283*m.b607 + 2*m.b284*m.b325 - 2*m.b325 + 2*m.b284*
                       m.b464 + 2*m.b285*m.b287 - 2*m.b285*m.b501 + 2*m.b286*m.b373 - 2*m.b373 + 2*m.b287*m.b325 + 2*
                       m.b287*m.b373 + 2*m.b288*m.b289 + 2*m.b289*m.b586 - 2*m.b289*m.b629 - 2*m.b290*m.b291 - 2*m.b290*
                       m.b392 - 2*m.b290*m.b481 + 2*m.b291*m.b380 - 2*m.b380 + 2*m.b291*m.b586 + 2*m.b292*m.b294 + 2*
                       m.b292*m.b382 + 2*m.b293*m.b296 + 2*m.b293*m.b388 + 2*m.b294*m.b296 + 2*m.b294*m.b380 + 2*m.b295*
                       m.b297 - 2*m.b297 + 2*m.b295*m.b403 + 2*m.b296*m.b297 + 2*m.b298*m.b300 - 2*m.b298*m.b579 - 2*
                       m.b298*m.b581 + 2*m.b299*m.b300 - 4*m.b299 + 2*m.b299*m.b444 + 2*m.b299*m.b482 + 2*m.b299*m.b552
                        + 2*m.b300*m.b628 + 2*m.b301*m.b303 - 4*m.b303 + 2*m.b302*m.b303 + 2*m.b302*m.b587 + 2*m.b302*
                       m.b628 + 2*m.b303*m.b505 + 2*m.b303*m.b613 + 2*m.b304*m.b306 + 2*m.b304*m.b517 + 2*m.b304*m.b613
                        - 2*m.b305*m.b548 + 2*m.b305*m.b549 - 2*m.b305*m.b550 + 2*m.b306*m.b460 + 2*m.b306*m.b550 - 2*
                       m.b307*m.b397 - 2*m.b307*m.b610 + 2*m.b308*m.b310 - 4*m.b310 - 2*m.b308*m.b438 - 2*m.b308*m.b550
                        + 2*m.b309*m.b400 - 2*m.b309*m.b555 - 2*m.b309*m.b585 + 2*m.b310*m.b487 + 2*m.b310*m.b585 + 2*
                       m.b310*m.b610 + 2*m.b311*m.b475 - 2*m.b311*m.b621 + 2*m.b312*m.b418 - 2*m.b312 + 2*m.b312*m.b462
                        + 2*m.b312*m.b507 - 2*m.b312*m.b508 - 2*m.b313*m.b316 - 2*m.b316 - 2*m.b313*m.b418 - 2*m.b313*
                       m.b419 + 2*m.b314*m.b316 - 4*m.b314 + 2*m.b314*m.b508 + 2*m.b314*m.b541 + 2*m.b314*m.b620 - 2*
                       m.b315*m.b317 - 2*m.b315*m.b531 + 2*m.b316*m.b317 + 2*m.b316*m.b451 + 2*m.b317*m.b318 - 2*m.b318
                        + 2*m.b318*m.b320 - 2*m.b320 - 2*m.b318*m.b542 + 2*m.b318*m.b567 - 2*m.b319*m.b600 - 2*m.b319*
                       m.b601 - 2*m.b320*m.b432 + 2*m.b320*m.b479 + 2*m.b320*m.b601 - 2*m.b321*m.b322 - 2*m.b322 - 2*
                       m.b321*m.b452 + 2*m.b322*m.b324 + 2*m.b322*m.b522 + 2*m.b322*m.b601 - 2*m.b323*m.b370 - 2*m.b370
                        - 2*m.b323*m.b478 - 2*m.b323*m.b480 + 2*m.b324*m.b370 + 2*m.b324*m.b478 + 2*m.b325*m.b327 - 2*
                       m.b325*m.b492 + 2*m.b326*m.b329 + 2*m.b327*m.b329 + 2*m.b327*m.b370 + 2*m.b328*m.b331 + 2*m.b329*
                       m.b331 + 2*m.b330*m.b332 - 4*m.b332 + 2*m.b331*m.b332 + 2*m.b332*m.b333 - 2*m.b333 + 2*m.b332*
                       m.b415 + 2*m.b333*m.b334 - 2*m.b333*m.b524 + 2*m.b333*m.b578 + 2*m.b334*m.b404 - 2*m.b334*m.b466
                        + 2*m.b335*m.b336 + 2*m.b335*m.b337 - 2*m.b336*m.b384 + 2*m.b384 + 2*m.b337*m.b384 + 2*m.b337*
                       m.b404 + 2*m.b338*m.b341 - 4*m.b341 + 2*m.b338*m.b483 + 2*m.b338*m.b495 + 2*m.b339*m.b341 - 2*
                       m.b339 - 2*m.b339*m.b456 + 2*m.b339*m.b560 + 2*m.b339*m.b599 + 2*m.b340*m.b342 - 2*m.b342 - 2*
                       m.b340*m.b391 - 2*m.b340*m.b588 + 2*m.b341*m.b342 + 2*m.b341*m.b457 - 2*m.b342*m.b516 + 2*m.b342*
                       m.b624 + 2*m.b343*m.b345 + 2*m.b343*m.b435 - 2*m.b343*m.b592 + 2*m.b344*m.b346 - 4*m.b346 + 2*
                       m.b344*m.b547 + 2*m.b345*m.b346 + 2*m.b345*m.b624 + 2*m.b346*m.b517 + 2*m.b346*m.b609 + 2*m.b347*
                       m.b348 + 2*m.b347 - 2*m.b347*m.b472 - 2*m.b347*m.b527 - 2*m.b347*m.b538 + 2*m.b348*m.b350 - 4*
                       m.b350 + 2*m.b348*m.b609 + 2*m.b349*m.b538 - 2*m.b349*m.b539 + 2*m.b350*m.b406 + 2*m.b350*m.b438
                        + 2*m.b350*m.b539 - 2*m.b351*m.b604 + 2*m.b352*m.b408 - 2*m.b352*m.b576 + 2*m.b353*m.b497 - 4*
                       m.b353 + 2*m.b353*m.b555 + 2*m.b353*m.b576 + 2*m.b353*m.b604 + 2*m.b354*m.b488 - 2*m.b354*m.b616
                        + 2*m.b355*m.b357 - 2*m.b355 - 4*m.b357 - 2*m.b355*m.b411 + 2*m.b355*m.b520 + 2*m.b355*m.b616 - 
                       2*m.b356*m.b359 - 2*m.b356*m.b427 - 2*m.b356*m.b429 + 2*m.b357*m.b359 + 2*m.b357*m.b530 + 2*
                       m.b357*m.b625 - 2*m.b358*m.b360 - 2*m.b358*m.b542 + 2*m.b359*m.b360 + 2*m.b360*m.b362 - 2*m.b362
                        - 2*m.b361*m.b364 - 2*m.b364 - 2*m.b361*m.b440 - 2*m.b361*m.b463 + 2*m.b362*m.b363 + 2*m.b362*
                       m.b364 - 2*m.b362*m.b531 - 2*m.b363*m.b597 + 2*m.b364*m.b365 + 2*m.b365 + 2*m.b364*m.b597 - 2*
                       m.b365*m.b367 - 2*m.b367 - 2*m.b365*m.b464 - 2*m.b365*m.b511 - 2*m.b366*m.b368 + 2*m.b366*m.b369
                        + 2*m.b367*m.b369 + 2*m.b367*m.b512 + 2*m.b367*m.b597 - 2*m.b368*m.b590 + 2*m.b369*m.b590 + 2*
                       m.b370*m.b372 + 2*m.b371*m.b374 - 2*m.b371*m.b590 + 2*m.b372*m.b374 + 2*m.b372*m.b590 + 2*m.b373*
                       m.b375 - 2*m.b373*m.b629 + 2*m.b374*m.b629 + 2*m.b375*m.b377 - 4*m.b377 - 2*m.b376*m.b378 - 2*
                       m.b378 - 2*m.b376*m.b415 - 2*m.b376*m.b533 + 2*m.b377*m.b378 + 2*m.b377*m.b423 + 2*m.b377*m.b629
                        + 2*m.b378*m.b379 + 2*m.b378*m.b568 + 2*m.b379*m.b381 + 2*m.b379*m.b466 + 2*m.b380*m.b383 - 2*
                       m.b380*m.b414 + 2*m.b381*m.b383 + 2*m.b381*m.b414 - 2*m.b382*m.b623 + 2*m.b383*m.b623 - 2*m.b384*
                       m.b627 - 2*m.b384*m.b630 - 2*m.b385*m.b386 + 2*m.b385*m.b480 + 2*m.b386*m.b479 - 2*m.b387*m.b434
                        + 2*m.b388*m.b389 - 2*m.b389*m.b404 - 2*m.b390*m.b391 + 2*m.b390*m.b496 + 2*m.b391*m.b455 + 2*
                       m.b391*m.b515 - 2*m.b393*m.b394 + 2*m.b393*m.b504 + 2*m.b394*m.b469 + 2*m.b394*m.b503 + 2*m.b395*
                       m.b446 - 2*m.b396*m.b397 + 2*m.b396*m.b462 - 2*m.b396*m.b540 + 2*m.b398*m.b459 - 2*m.b399*m.b400
                        - 2*m.b399*m.b529 + 2*m.b400*m.b486 - 2*m.b401*m.b402 - 2*m.b401*m.b510 - 2*m.b402*m.b476 - 2*
                       m.b403*m.b404 + 2*m.b405*m.b472 - 2*m.b407*m.b408 - 2*m.b407*m.b519 + 2*m.b408*m.b473 - 2*m.b409*
                       m.b410 + 2*m.b409*m.b411 - 2*m.b409*m.b499 + 2*m.b409*m.b531 + 2*m.b410*m.b427 - 2*m.b411*m.b498
                        - 2*m.b412*m.b413 + 2*m.b412*m.b453 + 2*m.b413*m.b499 - 2*m.b413*m.b500 + 2*m.b414*m.b415 - 2*
                       m.b417*m.b507 + 2*m.b419*m.b420 - 2*m.b419*m.b490 + 2*m.b419*m.b542 - 2*m.b420*m.b508 - 2*m.b420*
                       m.b509 - 2*m.b421*m.b422 + 2*m.b421*m.b465 + 2*m.b422*m.b451 + 2*m.b422*m.b490 - 2*m.b422*m.b491
                        - 2*m.b423*m.b544 - 2*m.b423*m.b569 + 2*m.b424*m.b425 + 2*m.b424*m.b516 - 2*m.b424*m.b587 - 2*
                       m.b425*m.b552 - 2*m.b425*m.b553 + 2*m.b427*m.b428 + 2*m.b428*m.b519 - 2*m.b428*m.b589 - 2*m.b428*
                       m.b593 + 2*m.b429*m.b430 - 2*m.b429*m.b477 - 2*m.b430*m.b521 - 2*m.b431*m.b432 + 2*m.b432*m.b463
                        + 2*m.b432*m.b477 - 2*m.b433*m.b523 - 2*m.b434*m.b558 - 2*m.b435*m.b580 + 2*m.b436*m.b580 - 2*
                       m.b436*m.b628 + 2*m.b439*m.b487 - 2*m.b441*m.b513 - 2*m.b442*m.b443 - 2*m.b442*m.b445 - 2*m.b444*
                       m.b445 - 2*m.b444*m.b571 + 2*m.b445*m.b563 - 2*m.b446*m.b447 + 2*m.b447*m.b571 - 2*m.b447*m.b624
                        + 2*m.b449*m.b555 + 2*m.b450*m.b474 - 2*m.b451*m.b489 + 2*m.b452*m.b453 - 2*m.b452*m.b501 - 2*
                       m.b453*m.b567 - 2*m.b454*m.b455 + 2*m.b454*m.b456 - 2*m.b454*m.b458 - 2*m.b457*m.b458 - 2*m.b457*
                       m.b562 + 2*m.b458*m.b572 - 2*m.b461*m.b528 - 2*m.b463*m.b476 + 2*m.b464*m.b465 - 2*m.b464*m.b492
                        - 2*m.b465*m.b577 - 2*m.b466*m.b467 - 2*m.b467*m.b602 - 2*m.b468*m.b469 + 2*m.b468*m.b470 - 2*
                       m.b468*m.b471 - 2*m.b470*m.b552 + 2*m.b471*m.b581 - 2*m.b473*m.b518 - 2*m.b474*m.b475 + 2*m.b475*
                       m.b518 - 2*m.b475*m.b619 - 2*m.b477*m.b509 - 2*m.b478*m.b479 - 2*m.b479*m.b500 - 2*m.b480*m.b493
                        - 2*m.b481*m.b598 - 2*m.b482*m.b483 + 2*m.b482*m.b484 - 2*m.b482*m.b485 - 2*m.b484*m.b561 + 2*
                       m.b485*m.b588 - 2*m.b486*m.b506 - 2*m.b487*m.b488 + 2*m.b488*m.b506 - 2*m.b488*m.b614 + 2*m.b491*
                       m.b607 - 2*m.b494*m.b595 - 2*m.b495*m.b570 - 2*m.b497*m.b520 + 2*m.b498*m.b606 - 2*m.b499*m.b530
                        + 2*m.b500*m.b611 - 2*m.b502*m.b591 - 2*m.b503*m.b579 + 2*m.b508*m.b621 - 2*m.b510*m.b541 + 2*
                       m.b511*m.b617 - 2*m.b514*m.b586 - 2*m.b517*m.b549 + 2*m.b519*m.b520 - 2*m.b520*m.b521 + 2*m.b521*
                       m.b626 + 2*m.b524*m.b533 - 2*m.b525*m.b545 - 2*m.b527*m.b618 + 2*m.b530*m.b594 - 2*m.b533*m.b534
                        - 2*m.b536*m.b628 - 2*m.b537*m.b613 - 2*m.b538*m.b613 + 2*m.b539*m.b604 - 2*m.b543*m.b551 + 2*
                       m.b546*m.b560 - 2*m.b546*m.b624 + 2*m.b547*m.b582 - 2*m.b547*m.b609 - 2*m.b549*m.b618 + 2*m.b550*
                       m.b610 + 2*m.b551*m.b617 + 2*m.b552*m.b603 - 2*m.b555*m.b556 + 2*m.b556*m.b614 + 2*m.b557*m.b558
                        - 2*m.b557*m.b559 - 2*m.b558*m.b598 - 2*m.b560*m.b561 - 2*m.b560*m.b563 + 2*m.b561*m.b608 - 2*
                       m.b562*m.b563 + 2*m.b566*m.b619 - 2*m.b568*m.b591 - 2*m.b569*m.b602 + 2*m.b570*m.b612 - 2*m.b571*
                       m.b572 + 2*m.b571*m.b573 - 2*m.b573*m.b574 + 2*m.b576*m.b616 - 2*m.b578*m.b586 - 2*m.b580*m.b581
                        + 2*m.b580*m.b582 - 2*m.b582*m.b583 + 2*m.b585*m.b621 - 2*m.b587*m.b588 + 2*m.b589*m.b626 - 2*
                       m.b593*m.b594 - 2*m.b600*m.b606 - 2*m.b615*m.b616 - 2*m.b620*m.b621 - 2*m.b622*m.b623 + 2*m.b623*
                       m.b630 - 2*m.b625*m.b626 + m.x631 <= 0)
