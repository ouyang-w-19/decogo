#  MINLP written by GAMS Convert at 04/21/18 13:54:17
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        862        1      861        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        862        1      861        0


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
m.b631 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b632 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b633 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b634 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b635 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b636 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b637 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b638 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b639 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b640 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b641 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b642 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b643 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b644 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b645 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b646 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b647 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b648 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b649 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b650 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b651 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b652 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b653 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b654 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b655 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b656 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b657 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b658 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b659 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b660 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b661 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b662 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b663 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b664 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b665 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b666 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b667 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b668 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b669 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b670 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b671 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b672 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b673 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b674 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b675 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b676 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b677 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b678 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b679 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b680 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b681 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b682 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b683 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b684 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b685 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b686 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b687 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b688 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b689 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b690 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b691 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b692 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b693 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b694 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b695 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b696 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b697 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b698 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b699 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b700 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b701 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b702 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b703 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b704 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b705 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b706 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b707 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b708 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b709 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b710 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b711 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b712 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b713 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b714 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b715 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b716 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b717 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b718 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b719 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b720 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b721 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b722 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b723 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b724 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b725 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b726 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b727 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b728 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b729 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b730 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b731 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b732 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b733 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b734 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b735 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b736 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b737 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b738 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b739 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b740 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b741 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b742 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b743 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b744 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b745 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b746 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b747 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b748 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b749 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b750 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b751 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b752 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b753 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b754 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b755 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b756 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b757 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b758 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b759 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b760 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b761 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b762 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b763 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b764 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b765 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b766 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b767 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b768 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b769 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b770 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b771 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b772 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b773 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b774 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b775 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b776 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b777 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b778 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b779 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b780 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b781 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b782 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b783 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b784 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b785 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b786 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b787 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b788 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b789 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b790 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b791 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b792 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b793 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b794 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b795 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b796 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b797 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b798 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b799 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b800 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b801 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b802 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b803 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b804 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b805 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b806 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b807 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b808 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b809 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b810 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b811 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b812 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b813 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b814 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b815 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b816 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b817 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b818 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b819 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b820 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b821 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b822 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b823 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b824 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b825 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b826 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b827 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b828 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b829 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b830 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b831 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b832 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b833 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b834 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b835 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b836 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b837 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b838 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b839 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b840 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b841 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b842 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b843 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b844 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b845 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b846 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b847 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b848 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b849 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b850 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b851 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b852 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b853 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b854 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b855 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b856 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b857 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b858 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b859 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b860 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b861 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x862 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x862, sense=maximize)

m.c1 = Constraint(expr=2*m.b1*m.b3 - 2*m.b1 - 4*m.b3 - 2*m.b1*m.b145 + 2*m.b145 + 2*m.b1*m.b193 - 4*m.b193 + 2*m.b1*
                       m.b537 + 2*m.b2*m.b376 - 2*m.b2 - 2*m.b376 - 2*m.b2*m.b522 + 2*m.b522 + 2*m.b2*m.b542 + 2*m.b2*
                       m.b558 + 2*m.b3*m.b547 + 2*m.b3*m.b548 + 2*m.b3*m.b568 + 2*m.b4*m.b75 - 2*m.b4 - 2*m.b75 + 2*m.b4
                       *m.b110 - 2*m.b110 + 2*m.b4*m.b344 - 2*m.b344 - 2*m.b4*m.b596 + 2*m.b5*m.b130 - 2*m.b5 - 2*m.b130
                        + 2*m.b5*m.b388 - 4*m.b388 - 2*m.b5*m.b607 + 2*m.b5*m.b608 + 2*m.b6*m.b110 - 2*m.b6 + 2*m.b6*
                       m.b153 - 2*m.b153 + 2*m.b6*m.b432 - 4*m.b432 - 2*m.b6*m.b619 + 2*m.b7*m.b130 - 2*m.b7 + 2*m.b7*
                       m.b174 - 2*m.b174 + 2*m.b7*m.b485 - 4*m.b485 - 2*m.b7*m.b630 + 2*m.b8*m.b94 - 2*m.b8 - 2*m.b94 + 
                       2*m.b8*m.b217 + 2*m.b217 - 2*m.b8*m.b610 + 2*m.b8*m.b611 + 2*m.b9*m.b115 - 2*m.b9 - 2*m.b115 + 2*
                       m.b9*m.b546 - 2*m.b9*m.b622 + 2*m.b9*m.b623 - 2*m.b10*m.b256 - 2*m.b10 + 2*m.b256 + 2*m.b10*
                       m.b326 - 2*m.b326 + 2*m.b10*m.b450 - 4*m.b450 + 2*m.b10*m.b603 - 2*m.b11*m.b109 - 2*m.b11 - 2*
                       m.b109 + 2*m.b11*m.b205 - 2*m.b205 + 2*m.b11*m.b533 + 2*m.b11*m.b699 - 2*m.b12*m.b76 - 2*m.b12 + 
                       2*m.b76 + 2*m.b12*m.b156 - 2*m.b156 + 2*m.b12*m.b308 - 4*m.b308 + 2*m.b12*m.b597 + 2*m.b13*m.b137
                        - 2*m.b13 - 2*m.b137 - 2*m.b13*m.b283 + 2*m.b283 + 2*m.b13*m.b320 + 2*m.b320 + 2*m.b13*m.b556 - 
                       2*m.b14*m.b286 - 2*m.b14 + 2*m.b286 + 2*m.b14*m.b287 - 2*m.b287 + 2*m.b14*m.b504 - 4*m.b504 + 2*
                       m.b14*m.b507 + 2*m.b507 + 2*m.b15*m.b244 - 2*m.b15 - 2*m.b244 + 2*m.b15*m.b305 - 2*m.b305 + 2*
                       m.b15*m.b540 - 2*m.b15*m.b685 + 2*m.b16*m.b160 - 2*m.b16 - 2*m.b160 - 2*m.b16*m.b317 + 2*m.b317
                        + 2*m.b16*m.b564 + 2*m.b16*m.b565 - 2*m.b17*m.b61 - 2*m.b17 + 2*m.b61 + 2*m.b17*m.b120 - 2*
                       m.b120 + 2*m.b17*m.b681 + 2*m.b17*m.b682 + 2*m.b18*m.b183 - 2*m.b18 - 2*m.b183 - 2*m.b18*m.b355
                        + 2*m.b355 + 2*m.b18*m.b555 + 2*m.b18*m.b578 + 2*m.b19*m.b142 - 2*m.b19 - 2*m.b142 - 2*m.b19*
                       m.b692 + 2*m.b19*m.b693 + 2*m.b19*m.b694 + 2*m.b20*m.b40 - 2*m.b20 - 2*m.b40 + 2*m.b20*m.b379 - 4
                       *m.b379 + 2*m.b21*m.b113 - 2*m.b21 - 2*m.b113 + 2*m.b21*m.b280 - 2*m.b280 - 2*m.b21*m.b661 + 2*
                       m.b21*m.b662 + 2*m.b22*m.b99 - 2*m.b22 - 2*m.b99 + 2*m.b22*m.b162 - 4*m.b162 - 2*m.b22*m.b706 + 2
                       *m.b22*m.b707 + 2*m.b23*m.b314 - 2*m.b23 - 2*m.b314 - 2*m.b23*m.b674 + 2*m.b23*m.b675 + 2*m.b23*
                       m.b676 + 2*m.b24*m.b120 - 2*m.b24 + 2*m.b24*m.b187 - 4*m.b187 - 2*m.b24*m.b716 + 2*m.b24*m.b717
                        + 2*m.b25*m.b351 - 2*m.b25 - 4*m.b351 - 2*m.b25*m.b687 + 2*m.b25*m.b688 + 2*m.b25*m.b689 + 2*
                       m.b26*m.b142 - 2*m.b26 + 2*m.b26*m.b225 - 4*m.b225 + 2*m.b26*m.b261 - 4*m.b261 - 2*m.b26*m.b725
                        + 2*m.b27*m.b82 - 2*m.b27 - 4*m.b82 - 2*m.b27*m.b120 + 2*m.b27*m.b225 + 2*m.b27*m.b726 + 2*m.b28
                       *m.b85 - 2*m.b28 - 2*m.b85 + 2*m.b28*m.b709 + 2*m.b29*m.b473 - 2*m.b29 - 2*m.b473 + 2*m.b29*
                       m.b710 + 2*m.b30*m.b213 - 2*m.b30 - 2*m.b213 + 2*m.b30*m.b396 - 2*m.b396 - 2*m.b30*m.b701 + 2*
                       m.b30*m.b702 + 2*m.b31*m.b162 - 2*m.b31 + 2*m.b31*m.b262 - 4*m.b262 + 2*m.b31*m.b291 - 4*m.b291
                        - 2*m.b31*m.b730 + 2*m.b32*m.b49 - 2*m.b32 - 2*m.b49 - 2*m.b32*m.b99 + 2*m.b32*m.b101 - 4*m.b101
                        + 2*m.b32*m.b262 + 2*m.b33*m.b105 - 2*m.b33 - 2*m.b105 + 2*m.b33*m.b719 + 2*m.b34*m.b606 - 2*
                       m.b34 + 2*m.b34*m.b720 + 2*m.b35*m.b111 + 2*m.b35 + 2*m.b111 - 2*m.b35*m.b178 + 4*m.b178 - 2*
                       m.b35*m.b490 - 2*m.b490 - 2*m.b35*m.b572 + 2*m.b36*m.b180 - 4*m.b36 - 2*m.b180 + 2*m.b36*m.b215
                        - 2*m.b215 + 2*m.b36*m.b442 - 2*m.b442 + 2*m.b36*m.b701 + 2*m.b37*m.b282 - 2*m.b37 - 4*m.b282 - 
                       2*m.b37*m.b398 + 2*m.b398 + 2*m.b37*m.b447 - 2*m.b447 + 2*m.b37*m.b590 + 2*m.b38*m.b187 - 4*m.b38
                        + 2*m.b38*m.b292 - 4*m.b292 + 2*m.b38*m.b331 - 4*m.b331 + 2*m.b38*m.b730 + 2*m.b39*m.b64 - 2*
                       m.b39 - 4*m.b64 + 2*m.b39*m.b122 - 4*m.b122 + 2*m.b39*m.b292 - 2*m.b39*m.b694 + 2*m.b40*m.b41 - 2
                       *m.b41 - 2*m.b40*m.b104 - 2*m.b104 + 2*m.b40*m.b233 - 4*m.b233 + 2*m.b41*m.b125 - 4*m.b125 + 2*
                       m.b42*m.b340 - 2*m.b42 - 2*m.b340 + 2*m.b42*m.b595 - 2*m.b43*m.b201 - 2*m.b43 + 2*m.b201 + 2*
                       m.b43*m.b271 - 2*m.b271 + 2*m.b43*m.b551 + 2*m.b43*m.b672 + 2*m.b44*m.b89 + 2*m.b44 + 2*m.b89 - 2
                       *m.b44*m.b211 + 4*m.b211 - 2*m.b44*m.b437 - 2*m.b437 - 2*m.b44*m.b561 + 2*m.b45*m.b181 - 4*m.b45
                        - 4*m.b181 + 2*m.b45*m.b252 - 2*m.b252 + 2*m.b45*m.b496 - 2*m.b496 + 2*m.b45*m.b687 + 2*m.b46*
                       m.b136 - 2*m.b46 + 2*m.b136 + 2*m.b46*m.b316 - 4*m.b316 - 2*m.b46*m.b444 + 2*m.b444 + 2*m.b46*
                       m.b703 + 2*m.b47*m.b225 - 4*m.b47 + 2*m.b47*m.b332 - 4*m.b332 + 2*m.b47*m.b367 - 4*m.b367 + 2*
                       m.b47*m.b725 + 2*m.b48*m.b82 - 2*m.b48 + 2*m.b48*m.b144 - 4*m.b144 + 2*m.b48*m.b332 - 2*m.b48*
                       m.b682 + 2*m.b49*m.b462 - 4*m.b462 + 2*m.b49*m.b708 - 2*m.b49*m.b731 + 2*m.b50*m.b83 - 2*m.b50 - 
                       4*m.b83 - 2*m.b50*m.b85 + 2*m.b50*m.b148 - 4*m.b148 + 2*m.b50*m.b749 + 2*m.b51*m.b52 - 2*m.b51 - 
                       2*m.b52 - 2*m.b51*m.b84 - 2*m.b84 + 2*m.b51*m.b525 - 2*m.b525 + 2*m.b51*m.b732 + 2*m.b52*m.b148
                        + 2*m.b53*m.b54 - 2*m.b53 - 2*m.b54 + 2*m.b53*m.b382 - 2*m.b382 + 2*m.b54*m.b150 - 2*m.b150 - 2*
                       m.b54*m.b582 + 2*m.b54*m.b763 - 2*m.b55*m.b240 - 2*m.b55 + 2*m.b240 + 2*m.b55*m.b301 - 2*m.b301
                        + 2*m.b55*m.b543 + 2*m.b55*m.b658 - 2*m.b56*m.b249 + 2*m.b56 + 4*m.b249 - 2*m.b56*m.b553 + 2*
                       m.b56*m.b575 - 2*m.b56*m.b631 + 2*m.b57*m.b214 - 4*m.b57 - 4*m.b214 + 2*m.b57*m.b280 + 2*m.b57*
                       m.b536 + 2*m.b57*m.b674 + 2*m.b58*m.b353 - 2*m.b58 - 4*m.b353 + 2*m.b58*m.b355 - 2*m.b58*m.b498
                        + 2*m.b498 + 2*m.b58*m.b591 + 2*m.b59*m.b60 - 2*m.b59 - 2*m.b60 + 2*m.b59*m.b116 - 2*m.b116 + 2*
                       m.b59*m.b220 - 4*m.b220 - 2*m.b59*m.b612 + 2*m.b60*m.b95 - 2*m.b95 + 2*m.b60*m.b140 - 2*m.b140 - 
                       2*m.b60*m.b288 - 2*m.b288 + 2*m.b61*m.b119 - 2*m.b119 - 2*m.b61*m.b529 - 2*m.b61*m.b781 + 2*m.b62
                       *m.b262 - 4*m.b62 + 2*m.b62*m.b368 - 4*m.b368 + 2*m.b62*m.b410 - 4*m.b410 + 2*m.b62*m.b716 + 2*
                       m.b63*m.b101 - 4*m.b63 + 2*m.b63*m.b164 - 4*m.b164 + 2*m.b63*m.b368 + 2*m.b63*m.b682 + 2*m.b64*
                       m.b190 - 4*m.b190 + 2*m.b64*m.b695 + 2*m.b64*m.b727 - 2*m.b65*m.b66 - 2*m.b65 + 2*m.b66 + 2*m.b65
                       *m.b532 + 2*m.b65*m.b547 + 2*m.b65*m.b728 + 2*m.b66*m.b103 - 4*m.b103 - 2*m.b66*m.b749 - 2*m.b66*
                       m.b782 + 2*m.b67*m.b68 - 2*m.b67 - 2*m.b68 + 2*m.b67*m.b751 - 2*m.b67*m.b761 + 2*m.b67*m.b762 - 2
                       *m.b68*m.b69 - 2*m.b69 + 2*m.b68*m.b103 + 2*m.b68*m.b168 - 4*m.b168 + 2*m.b69*m.b70 - 2*m.b70 + 2
                       *m.b69*m.b470 - 2*m.b470 + 2*m.b69*m.b736 + 2*m.b70*m.b168 + 2*m.b71*m.b72 - 2*m.b71 - 2*m.b72 + 
                       2*m.b71*m.b423 - 2*m.b423 + 2*m.b72*m.b170 - 2*m.b170 - 2*m.b72*m.b570 + 2*m.b72*m.b752 + 2*m.b73
                       *m.b538 - 2*m.b73 + 2*m.b73*m.b641 + 2*m.b73*m.b722 - 2*m.b73*m.b784 + 2*m.b74*m.b484 - 4*m.b74
                        - 2*m.b484 + 2*m.b74*m.b584 + 2*m.b74*m.b740 + 2*m.b74*m.b784 - 2*m.b75*m.b76 + 2*m.b75*m.b176
                        - 2*m.b176 + 2*m.b75*m.b583 - 2*m.b76*m.b175 - 2*m.b175 + 2*m.b76*m.b786 + 2*m.b77*m.b588 - 2*
                       m.b77 + 2*m.b77*m.b645 + 2*m.b77*m.b779 - 2*m.b77*m.b787 + 2*m.b78*m.b251 - 4*m.b78 - 4*m.b251 + 
                       2*m.b78*m.b314 + 2*m.b78*m.b531 + 2*m.b78*m.b661 + 2*m.b79*m.b317 - 2*m.b79 + 2*m.b79*m.b399 - 4*
                       m.b399 + 2*m.b79*m.b601 - 2*m.b79*m.b724 + 2*m.b80*m.b292 - 4*m.b80 + 2*m.b80*m.b412 - 2*m.b412
                        + 2*m.b80*m.b458 - 4*m.b458 + 2*m.b80*m.b706 + 2*m.b81*m.b122 - 4*m.b81 + 2*m.b81*m.b189 - 4*
                       m.b189 + 2*m.b81*m.b412 + 2*m.b81*m.b694 + 2*m.b82*m.b683 + 2*m.b82*m.b731 + 2*m.b83*m.b84 + 2*
                       m.b83*m.b761 + 2*m.b83*m.b773 + 2*m.b84*m.b123 - 4*m.b123 + 2*m.b84*m.b197 - 2*m.b197 + 2*m.b85*
                       m.b86 - 2*m.b86 + 2*m.b85*m.b418 - 2*m.b418 + 2*m.b86*m.b197 + 2*m.b87*m.b88 - 2*m.b87 - 2*m.b88
                        + 2*m.b87*m.b473 + 2*m.b88*m.b199 - 2*m.b199 + 2*m.b88*m.b474 + 2*m.b474 - 2*m.b88*m.b560 - 2*
                       m.b89*m.b438 + 2*m.b438 - 2*m.b89*m.b562 - 2*m.b89*m.b768 + 2*m.b90*m.b598 - 2*m.b90 + 2*m.b90*
                       m.b660 + 2*m.b90*m.b768 - 2*m.b90*m.b795 + 2*m.b91*m.b92 - 4*m.b91 - 2*m.b92 + 2*m.b91*m.b279 - 4
                       *m.b279 + 2*m.b91*m.b351 + 2*m.b91*m.b648 + 2*m.b92*m.b352 + 2*m.b352 + 2*m.b92*m.b535 - 2*m.b92*
                       m.b796 + 2*m.b93*m.b94 - 2*m.b93 + 2*m.b93*m.b283 + 2*m.b93*m.b445 - 4*m.b445 - 2*m.b93*m.b729 - 
                       2*m.b94*m.b797 + 2*m.b94*m.b798 + 2*m.b95*m.b97 - 4*m.b97 + 2*m.b95*m.b529 - 2*m.b95*m.b680 + 2*
                       m.b96*m.b97 - 4*m.b96 + 2*m.b96*m.b602 + 2*m.b96*m.b653 + 2*m.b96*m.b760 + 2*m.b97*m.b457 + 2*
                       m.b457 + 2*m.b97*m.b528 + 2*m.b98*m.b332 - 4*m.b98 + 2*m.b98*m.b460 - 2*m.b460 + 2*m.b98*m.b513
                        - 4*m.b513 + 2*m.b98*m.b692 + 2*m.b99*m.b100 - 4*m.b100 + 2*m.b99*m.b667 + 2*m.b100*m.b144 + 2*
                       m.b100*m.b227 - 4*m.b227 + 2*m.b100*m.b460 + 2*m.b101*m.b670 + 2*m.b101*m.b728 + 2*m.b102*m.b190
                        - 2*m.b102 + 2*m.b102*m.b467 + 2*m.b467 + 2*m.b102*m.b520 - 4*m.b520 - 2*m.b102*m.b762 + 2*
                       m.b103*m.b104 + 2*m.b103*m.b783 + 2*m.b104*m.b146 - 4*m.b146 + 2*m.b104*m.b234 - 2*m.b234 + 2*
                       m.b105*m.b106 - 2*m.b106 + 2*m.b105*m.b377 - 4*m.b377 - 2*m.b105*m.b751 + 2*m.b106*m.b234 + 2*
                       m.b107*m.b108 - 2*m.b107 - 2*m.b108 + 2*m.b107*m.b606 + 2*m.b108*m.b236 - 2*m.b236 + 2*m.b108*
                       m.b424 + 2*m.b424 - 2*m.b108*m.b549 + 2*m.b109*m.b431 - 4*m.b431 + 2*m.b109*m.b766 + 2*m.b109*
                       m.b804 + 2*m.b110*m.b573 - 2*m.b110*m.b767 - 2*m.b111*m.b574 - 2*m.b111*m.b757 - 2*m.b111*m.b758
                        + 2*m.b112*m.b310 - 4*m.b112 - 4*m.b310 + 2*m.b112*m.b609 + 2*m.b112*m.b673 + 2*m.b112*m.b758 - 
                       2*m.b113*m.b315 + 4*m.b315 + 2*m.b113*m.b530 + 2*m.b113*m.b621 + 2*m.b114*m.b115 - 2*m.b114 + 2*
                       m.b114*m.b499 - 4*m.b499 + 2*m.b114*m.b622 - 2*m.b114*m.b734 - 2*m.b115*m.b354 + 2*m.b354 + 2*
                       m.b115*m.b806 + 2*m.b116*m.b118 - 4*m.b118 + 2*m.b116*m.b221 - 2*m.b221 - 2*m.b116*m.b329 + 4*
                       m.b329 + 2*m.b117*m.b592 - 2*m.b117 + 2*m.b117*m.b636 + 2*m.b117*m.b771 - 2*m.b117*m.b789 + 2*
                       m.b118*m.b666 + 2*m.b118*m.b748 + 2*m.b118*m.b789 + 2*m.b119*m.b368 + 2*m.b119*m.b515 - 2*m.b515
                        - 2*m.b119*m.b528 + 2*m.b120*m.b121 - 4*m.b121 + 2*m.b121*m.b164 + 2*m.b121*m.b264 - 4*m.b264 + 
                       2*m.b121*m.b515 + 2*m.b122*m.b656 + 2*m.b122*m.b718 + 2*m.b123*m.b124 - 2*m.b124 + 2*m.b123*
                       m.b750 + 2*m.b123*m.b792 + 2*m.b124*m.b166 - 4*m.b166 + 2*m.b124*m.b269 - 2*m.b269 - 2*m.b124*
                       m.b719 + 2*m.b125*m.b126 - 2*m.b126 + 2*m.b125*m.b419 - 4*m.b419 + 2*m.b125*m.b751 + 2*m.b126*
                       m.b269 + 2*m.b127*m.b128 - 2*m.b127 - 4*m.b128 + 2*m.b127*m.b595 + 2*m.b128*m.b383 + 2*m.b383 + 2
                       *m.b128*m.b560 + 2*m.b128*m.b811 + 2*m.b129*m.b173 - 2*m.b129 - 2*m.b173 + 2*m.b129*m.b483 - 4*
                       m.b483 - 2*m.b129*m.b659 + 2*m.b129*m.b756 + 2*m.b130*m.b131 - 2*m.b131 - 2*m.b130*m.b390 + 2*
                       m.b390 + 2*m.b131*m.b391 - 2*m.b391 - 2*m.b131*m.b561 + 2*m.b131*m.b805 + 2*m.b132*m.b134 - 2*
                       m.b132 - 4*m.b134 - 2*m.b132*m.b248 - 2*m.b248 + 2*m.b132*m.b586 + 2*m.b132*m.b686 - 2*m.b133*
                       m.b588 + 2*m.b133 + 2*m.b133*m.b597 - 2*m.b133*m.b744 - 2*m.b133*m.b745 + 2*m.b134*m.b620 + 2*
                       m.b134*m.b745 + 2*m.b134*m.b795 + 2*m.b135*m.b137 - 2*m.b135 - 2*m.b135*m.b535 + 2*m.b135*m.b610
                        + 2*m.b135*m.b734 - 2*m.b136*m.b284 - 2*m.b284 - 2*m.b136*m.b576 - 2*m.b136*m.b770 + 2*m.b137*
                       m.b284 - 2*m.b137*m.b400 + 2*m.b400 + 2*m.b138*m.b219 - 4*m.b138 - 2*m.b219 + 2*m.b138*m.b284 + 2
                       *m.b138*m.b322 + 2*m.b322 + 2*m.b138*m.b576 + 2*m.b139*m.b141 - 2*m.b139 - 4*m.b141 + 2*m.b139*
                       m.b184 - 2*m.b184 - 2*m.b139*m.b365 + 4*m.b365 + 2*m.b139*m.b603 + 2*m.b140*m.b579 + 2*m.b140*
                       m.b625 - 2*m.b140*m.b781 + 2*m.b141*m.b529 + 2*m.b141*m.b739 + 2*m.b141*m.b781 + 2*m.b142*m.b143
                        - 2*m.b143 - 2*m.b142*m.b727 + 2*m.b143*m.b189 + 2*m.b143*m.b295 - 4*m.b295 - 2*m.b143*m.b516 - 
                       2*m.b516 + 2*m.b144*m.b638 + 2*m.b144*m.b708 + 2*m.b145*m.b415 - 2*m.b415 - 2*m.b145*m.b728 - 2*
                       m.b145*m.b783 + 2*m.b146*m.b147 - 2*m.b147 + 2*m.b146*m.b194 - 2*m.b194 + 2*m.b146*m.b762 + 2*
                       m.b147*m.b195 - 4*m.b195 + 2*m.b147*m.b299 - 2*m.b299 - 2*m.b147*m.b709 + 2*m.b148*m.b149 - 2*
                       m.b149 + 2*m.b148*m.b471 - 4*m.b471 + 2*m.b149*m.b299 + 2*m.b150*m.b151 - 4*m.b151 + 2*m.b151*
                       m.b341 + 2*m.b341 + 2*m.b151*m.b570 + 2*m.b151*m.b816 + 2*m.b152*m.b238 - 2*m.b152 - 4*m.b238 + 2
                       *m.b152*m.b428 - 2*m.b428 + 2*m.b152*m.b740 - 2*m.b152*m.b817 + 2*m.b153*m.b155 - 2*m.b155 - 2*
                       m.b153*m.b346 + 2*m.b346 + 2*m.b153*m.b643 + 2*m.b154*m.b155 - 2*m.b154 + 2*m.b154*m.b204 - 2*
                       m.b204 - 2*m.b154*m.b587 + 2*m.b154*m.b804 + 2*m.b155*m.b436 - 2*m.b436 - 2*m.b155*m.b553 + 2*
                       m.b156*m.b158 - 4*m.b158 - 2*m.b156*m.b210 - 2*m.b210 + 2*m.b156*m.b700 - 2*m.b157*m.b311 + 4*
                       m.b157 - 2*m.b311 - 2*m.b157*m.b597 - 2*m.b157*m.b598 - 2*m.b157*m.b738 + 2*m.b158*m.b632 + 2*
                       m.b158*m.b738 + 2*m.b158*m.b787 + 2*m.b159*m.b160 - 2*m.b159 - 2*m.b159*m.b530 + 2*m.b159*m.b600
                        + 2*m.b159*m.b729 + 2*m.b160*m.b318 - 2*m.b318 - 2*m.b160*m.b446 + 2*m.b446 - 2*m.b161*m.b614 + 
                       2*m.b161 - 2*m.b161*m.b692 + 2*m.b161*m.b693 - 2*m.b161*m.b819 + 2*m.b162*m.b163 - 2*m.b163 + 2*
                       m.b162*m.b462 + 2*m.b163*m.b227 + 2*m.b163*m.b334 - 4*m.b334 - 2*m.b163*m.b461 - 2*m.b461 + 2*
                       m.b164*m.b228 - 2*m.b228 + 2*m.b164*m.b695 + 2*m.b165*m.b373 + 2*m.b165 - 4*m.b373 - 2*m.b165*
                       m.b522 - 2*m.b165*m.b718 - 2*m.b165*m.b792 + 2*m.b166*m.b167 - 4*m.b167 + 2*m.b166*m.b231 - 2*
                       m.b231 + 2*m.b166*m.b773 + 2*m.b167*m.b232 - 4*m.b232 + 2*m.b167*m.b339 - 4*m.b339 + 2*m.b167*
                       m.b709 + 2*m.b168*m.b169 - 2*m.b169 + 2*m.b168*m.b526 - 4*m.b526 + 2*m.b169*m.b339 + 2*m.b170*
                       m.b171 - 4*m.b171 + 2*m.b171*m.b300 + 2*m.b300 + 2*m.b171*m.b582 + 2*m.b171*m.b821 + 2*m.b172*
                       m.b480 - 2*m.b172 - 2*m.b480 - 2*m.b172*m.b584 + 2*m.b172*m.b630 + 2*m.b172*m.b753 + 2*m.b173*
                       m.b175 - 2*m.b173*m.b484 + 2*m.b173*m.b805 + 2*m.b174*m.b177 - 4*m.b177 - 2*m.b174*m.b307 + 2*
                       m.b307 + 2*m.b174*m.b659 + 2*m.b175*m.b177 + 2*m.b175*m.b243 - 2*m.b243 + 2*m.b176*m.b209 - 2*
                       m.b209 + 2*m.b176*m.b305 - 2*m.b176*m.b489 - 2*m.b489 + 2*m.b177*m.b489 + 2*m.b177*m.b553 - 2*
                       m.b178*m.b179 + 2*m.b179 - 2*m.b178*m.b348 - 2*m.b348 - 2*m.b178*m.b609 + 2*m.b179*m.b181 - 2*
                       m.b179*m.b661 - 2*m.b179*m.b823 + 2*m.b180*m.b588 + 2*m.b180*m.b738 - 2*m.b180*m.b824 + 2*m.b181*
                       m.b598 + 2*m.b181*m.b824 + 2*m.b182*m.b183 - 4*m.b182 + 2*m.b182*m.b535 + 2*m.b182*m.b590 + 2*
                       m.b182*m.b724 + 2*m.b183*m.b356 - 2*m.b356 - 2*m.b183*m.b500 + 2*m.b500 + 2*m.b184*m.b324 - 2*
                       m.b324 - 2*m.b184*m.b453 + 2*m.b453 + 2*m.b184*m.b679 - 2*m.b185*m.b186 + 2*m.b185 + 2*m.b186 - 2
                       *m.b185*m.b566 + 2*m.b185*m.b604 - 2*m.b185*m.b760 - 2*m.b186*m.b706 + 2*m.b186*m.b707 - 2*m.b186
                       *m.b827 + 2*m.b187*m.b188 - 2*m.b188 + 2*m.b187*m.b727 + 2*m.b188*m.b264 + 2*m.b188*m.b371 - 4*
                       m.b371 - 2*m.b188*m.b413 - 2*m.b413 + 2*m.b189*m.b191 - 4*m.b191 + 2*m.b189*m.b683 + 2*m.b190*
                       m.b193 + 2*m.b190*m.b465 - 4*m.b465 + 2*m.b191*m.b193 + 2*m.b191*m.b371 + 2*m.b191*m.b655 - 2*
                       m.b192*m.b194 + 2*m.b192 + 2*m.b192*m.b336 - 4*m.b336 - 2*m.b192*m.b467 - 2*m.b192*m.b708 + 2*
                       m.b193*m.b194 + 2*m.b194*m.b268 - 4*m.b268 + 2*m.b195*m.b196 - 4*m.b196 + 2*m.b195*m.b267 - 2*
                       m.b267 + 2*m.b195*m.b783 + 2*m.b196*m.b268 + 2*m.b196*m.b378 - 4*m.b378 + 2*m.b196*m.b719 + 2*
                       m.b197*m.b198 - 2*m.b198 - 2*m.b197*m.b568 + 2*m.b198*m.b378 + 2*m.b199*m.b200 - 4*m.b200 + 2*
                       m.b200*m.b270 + 2*m.b270 + 2*m.b200*m.b381 - 2*m.b381 + 2*m.b200*m.b594 + 2*m.b201*m.b203 - 4*
                       m.b203 - 2*m.b201*m.b764 - 2*m.b201*m.b766 - 2*m.b202*m.b533 + 2*m.b202 + 2*m.b202*m.b538 - 2*
                       m.b202*m.b618 - 2*m.b202*m.b619 + 2*m.b203*m.b619 + 2*m.b203*m.b642 + 2*m.b203*m.b742 + 2*m.b204*
                       m.b206 - 2*m.b206 + 2*m.b204*m.b644 - 2*m.b204*m.b775 + 2*m.b205*m.b208 - 4*m.b208 - 2*m.b205*
                       m.b275 + 2*m.b275 + 2*m.b205*m.b643 + 2*m.b206*m.b208 + 2*m.b206*m.b273 - 2*m.b273 - 2*m.b206*
                       m.b777 + 2*m.b207*m.b210 + 2*m.b207 - 2*m.b207*m.b436 - 2*m.b207*m.b488 - 2*m.b488 - 2*m.b207*
                       m.b699 + 2*m.b208*m.b210 + 2*m.b208*m.b561 + 2*m.b209*m.b310 - 2*m.b209*m.b438 + 2*m.b209*m.b767
                        + 2*m.b210*m.b438 - 2*m.b211*m.b212 + 2*m.b212 - 2*m.b211*m.b392 - 2*m.b392 - 2*m.b211*m.b620 + 
                       2*m.b212*m.b214 - 2*m.b212*m.b674 - 2*m.b212*m.b829 + 2*m.b213*m.b574 + 2*m.b213*m.b745 - 2*
                       m.b213*m.b830 + 2*m.b214*m.b609 + 2*m.b214*m.b830 + 2*m.b215*m.b216 - 2*m.b216 - 2*m.b215*m.b498
                        + 2*m.b215*m.b633 + 2*m.b216*m.b500 + 2*m.b216*m.b663 - 2*m.b216*m.b831 - 2*m.b217*m.b501 - 2*
                       m.b501 - 2*m.b217*m.b545 - 2*m.b217*m.b678 - 2*m.b218*m.b449 - 2*m.b218 + 2*m.b449 + 2*m.b218*
                       m.b678 + 2*m.b218*m.b798 + 2*m.b218*m.b832 + 2*m.b219*m.b220 - 2*m.b219*m.b321 - 2*m.b321 + 2*
                       m.b219*m.b360 - 2*m.b360 + 2*m.b220*m.b222 - 2*m.b222 + 2*m.b220*m.b678 + 2*m.b221*m.b360 - 2*
                       m.b221*m.b406 + 2*m.b406 + 2*m.b221*m.b665 + 2*m.b222*m.b404 - 2*m.b404 + 2*m.b222*m.b406 - 2*
                       m.b222*m.b760 - 2*m.b223*m.b224 + 2*m.b223 + 2*m.b224 - 2*m.b223*m.b579 + 2*m.b223*m.b593 - 2*
                       m.b223*m.b748 - 2*m.b224*m.b716 + 2*m.b224*m.b717 - 2*m.b224*m.b834 + 2*m.b225*m.b226 - 2*m.b226
                        + 2*m.b226*m.b295 - 2*m.b226*m.b369 - 2*m.b369 + 2*m.b226*m.b414 - 4*m.b414 + 2*m.b227*m.b229 - 
                       4*m.b229 + 2*m.b227*m.b670 + 2*m.b228*m.b334 + 2*m.b228*m.b637 - 2*m.b228*m.b820 + 2*m.b229*
                       m.b414 + 2*m.b229*m.b669 + 2*m.b229*m.b820 - 2*m.b230*m.b231 + 2*m.b230 + 2*m.b230*m.b296 - 4*
                       m.b296 - 2*m.b230*m.b542 - 2*m.b230*m.b695 + 2*m.b231*m.b298 - 4*m.b298 + 2*m.b231*m.b820 + 2*
                       m.b232*m.b233 + 2*m.b232*m.b297 - 2*m.b297 + 2*m.b232*m.b792 + 2*m.b233*m.b298 + 2*m.b233*m.b420
                        - 4*m.b420 + 2*m.b234*m.b235 - 2*m.b235 - 2*m.b234*m.b558 + 2*m.b235*m.b420 + 2*m.b236*m.b237 - 
                       4*m.b237 + 2*m.b237*m.b422 - 2*m.b422 + 2*m.b237*m.b605 + 2*m.b237*m.b697 + 2*m.b238*m.b239 - 2*
                       m.b239 + 2*m.b238*m.b549 + 2*m.b238*m.b697 + 2*m.b239*m.b477 - 2*m.b477 + 2*m.b239*m.b629 - 2*
                       m.b239*m.b793 + 2*m.b240*m.b242 - 4*m.b242 - 2*m.b240*m.b774 - 2*m.b240*m.b776 - 2*m.b241*m.b302
                        + 4*m.b241 - 2*m.b302 - 2*m.b241*m.b538 - 2*m.b241*m.b540 - 2*m.b241*m.b607 + 2*m.b242*m.b607 + 
                       2*m.b242*m.b629 + 2*m.b242*m.b755 + 2*m.b243*m.b245 - 2*m.b245 + 2*m.b243*m.b630 - 2*m.b243*
                       m.b765 - 2*m.b244*m.b246 + 2*m.b246 + 2*m.b244*m.b247 - 4*m.b247 + 2*m.b244*m.b659 + 2*m.b245*
                       m.b247 + 2*m.b245*m.b304 - 2*m.b304 - 2*m.b245*m.b767 + 2*m.b246*m.b248 - 2*m.b246*m.b391 - 2*
                       m.b246*m.b435 - 2*m.b435 + 2*m.b247*m.b248 + 2*m.b247*m.b572 + 2*m.b248*m.b757 - 2*m.b249*m.b250
                        + 2*m.b250 - 2*m.b249*m.b439 - 2*m.b439 - 2*m.b249*m.b632 + 2*m.b250*m.b251 - 2*m.b250*m.b687 - 
                       2*m.b250*m.b835 + 2*m.b251*m.b620 + 2*m.b251*m.b836 + 2*m.b252*m.b254 - 2*m.b254 + 2*m.b252*
                       m.b647 - 2*m.b252*m.b724 - 2*m.b253*m.b397 + 2*m.b253 - 2*m.b397 - 2*m.b253*m.b446 - 2*m.b253*
                       m.b634 + 2*m.b253*m.b689 + 2*m.b254*m.b446 + 2*m.b254*m.b677 - 2*m.b254*m.b837 - 2*m.b255*m.b503
                        - 2*m.b255 + 2*m.b503 + 2*m.b255*m.b664 + 2*m.b255*m.b806 + 2*m.b255*m.b838 - 2*m.b256*m.b546 + 
                       2*m.b256*m.b799 - 2*m.b256*m.b826 - 2*m.b257*m.b364 - 2*m.b257 + 2*m.b364 + 2*m.b257*m.b602 + 2*
                       m.b257*m.b652 + 2*m.b257*m.b715 + 2*m.b258*m.b364 - 2*m.b258 + 2*m.b258*m.b451 - 2*m.b451 - 2*
                       m.b258*m.b771 + 2*m.b258*m.b826 - 2*m.b259*m.b260 + 4*m.b259 + 2*m.b260 - 2*m.b259*m.b592 - 2*
                       m.b259*m.b593 - 2*m.b259*m.b739 + 2*m.b260*m.b261 - 2*m.b260*m.b725 - 2*m.b260*m.b840 + 2*m.b261*
                       m.b593 + 2*m.b261*m.b841 + 2*m.b262*m.b263 - 2*m.b263 + 2*m.b263*m.b334 + 2*m.b263*m.b464 - 4*
                       m.b464 - 2*m.b263*m.b842 + 2*m.b264*m.b265 - 4*m.b265 + 2*m.b264*m.b656 + 2*m.b265*m.b266 + 2*
                       m.b266 + 2*m.b265*m.b464 + 2*m.b265*m.b815 - 2*m.b266*m.b267 - 2*m.b266*m.b547 - 2*m.b266*m.b683
                        + 2*m.b267*m.b338 - 4*m.b338 + 2*m.b267*m.b815 + 2*m.b268*m.b337 - 2*m.b337 + 2*m.b268*m.b525 - 
                       2*m.b269*m.b548 + 2*m.b269*m.b843 - 2*m.b270*m.b628 - 2*m.b270*m.b710 - 2*m.b270*m.b828 + 2*
                       m.b271*m.b605 + 2*m.b271*m.b752 - 2*m.b271*m.b785 + 2*m.b272*m.b596 - 4*m.b272 + 2*m.b272*m.b618
                        + 2*m.b272*m.b765 + 2*m.b272*m.b784 + 2*m.b273*m.b274 - 2*m.b274 + 2*m.b273*m.b619 - 2*m.b273*
                       m.b755 + 2*m.b274*m.b276 - 4*m.b276 + 2*m.b274*m.b345 - 2*m.b345 - 2*m.b274*m.b390 + 2*m.b275*
                       m.b277 - 2*m.b277 - 2*m.b275*m.b347 - 2*m.b347 - 2*m.b275*m.b733 + 2*m.b276*m.b277 + 2*m.b276*
                       m.b586 + 2*m.b276*m.b699 - 2*m.b277*m.b673 + 2*m.b277*m.b744 + 2*m.b278*m.b279 + 2*m.b278 - 2*
                       m.b278*m.b493 + 2*m.b493 - 2*m.b278*m.b701 - 2*m.b278*m.b846 + 2*m.b279*m.b632 + 2*m.b279*m.b796
                        + 2*m.b280*m.b282 - 2*m.b280*m.b729 - 2*m.b281*m.b400 + 2*m.b281 - 2*m.b281*m.b443 - 2*m.b443 - 
                       2*m.b281*m.b649 + 2*m.b281*m.b676 + 2*m.b282*m.b400 + 2*m.b282*m.b837 - 2*m.b283*m.b634 - 2*
                       m.b283*m.b847 + 2*m.b284*m.b285 - 2*m.b285 + 2*m.b285*m.b651 - 2*m.b285*m.b747 + 2*m.b285*m.b847
                        - 2*m.b286*m.b556 + 2*m.b286*m.b807 - 2*m.b286*m.b818 - 2*m.b287*m.b328 + 2*m.b328 + 2*m.b287*
                       m.b592 + 2*m.b287*m.b705 + 2*m.b288*m.b328 + 2*m.b288*m.b506 - 2*m.b506 + 2*m.b288*m.b818 - 2*
                       m.b289*m.b290 + 4*m.b289 + 2*m.b290 - 2*m.b289*m.b602 - 2*m.b289*m.b604 - 2*m.b289*m.b735 + 2*
                       m.b290*m.b291 - 2*m.b290*m.b730 - 2*m.b290*m.b849 + 2*m.b291*m.b411 - 2*m.b411 + 2*m.b291*m.b604
                        + 2*m.b292*m.b294 - 4*m.b294 + 2*m.b293*m.b294 - 4*m.b293 + 2*m.b293*m.b411 + 2*m.b293*m.b462 + 
                       2*m.b293*m.b654 + 2*m.b294*m.b371 + 2*m.b294*m.b519 - 4*m.b519 + 2*m.b295*m.b296 + 2*m.b295*
                       m.b638 + 2*m.b296*m.b519 + 2*m.b296*m.b810 + 2*m.b297*m.b375 - 4*m.b375 - 2*m.b297*m.b669 + 2*
                       m.b297*m.b810 + 2*m.b298*m.b374 - 2*m.b374 + 2*m.b298*m.b470 - 2*m.b299*m.b376 + 2*m.b299*m.b850
                        - 2*m.b300*m.b641 - 2*m.b300*m.b720 - 2*m.b300*m.b822 + 2*m.b301*m.b594 + 2*m.b301*m.b763 - 2*
                       m.b301*m.b774 + 2*m.b302*m.b303 - 4*m.b303 + 2*m.b302*m.b615 + 2*m.b302*m.b774 + 2*m.b303*m.b585
                        + 2*m.b303*m.b775 + 2*m.b303*m.b793 + 2*m.b304*m.b306 - 2*m.b306 + 2*m.b304*m.b607 - 2*m.b304*
                       m.b742 + 2*m.b305*m.b308 - 2*m.b305*m.b434 - 2*m.b434 + 2*m.b306*m.b308 - 2*m.b306*m.b346 + 2*
                       m.b306*m.b389 - 4*m.b389 + 2*m.b307*m.b309 - 2*m.b309 - 2*m.b307*m.b737 - 2*m.b307*m.b794 + 2*
                       m.b308*m.b309 + 2*m.b309*m.b311 - 2*m.b309*m.b660 + 2*m.b310*m.b312 - 4*m.b312 + 2*m.b310*m.b347
                        + 2*m.b311*m.b312 + 2*m.b311*m.b794 + 2*m.b312*m.b562 + 2*m.b312*m.b713 - 2*m.b313*m.b531 + 2*
                       m.b313 - 2*m.b313*m.b662 + 2*m.b313*m.b831 - 2*m.b313*m.b852 + 2*m.b314*m.b316 - 2*m.b314*m.b734
                        - 2*m.b315*m.b354 - 2*m.b315*m.b497 - 2*m.b497 - 2*m.b315*m.b663 + 2*m.b316*m.b354 + 2*m.b316*
                       m.b831 - 2*m.b317*m.b319 + 2*m.b319 - 2*m.b317*m.b649 + 2*m.b318*m.b321 - 2*m.b318*m.b590 + 2*
                       m.b318*m.b807 + 2*m.b319*m.b321 - 2*m.b319*m.b578 - 2*m.b319*m.b853 - 2*m.b320*m.b323 - 2*m.b323
                        - 2*m.b320*m.b576 - 2*m.b320*m.b577 + 2*m.b321*m.b323 - 2*m.b322*m.b325 - 2*m.b325 - 2*m.b322*
                       m.b565 - 2*m.b322*m.b652 + 2*m.b323*m.b325 + 2*m.b323*m.b635 - 2*m.b324*m.b327 - 2*m.b327 + 2*
                       m.b324*m.b577 + 2*m.b324*m.b747 + 2*m.b325*m.b327 + 2*m.b325*m.b814 + 2*m.b326*m.b505 + 2*m.b505
                        + 2*m.b326*m.b579 - 2*m.b326*m.b691 + 2*m.b327*m.b691 + 2*m.b327*m.b771 - 2*m.b328*m.b455 + 2*
                       m.b455 - 2*m.b328*m.b849 - 2*m.b329*m.b330 - 2*m.b330 - 2*m.b329*m.b453 - 2*m.b329*m.b613 + 2*
                       m.b330*m.b331 + 2*m.b330*m.b730 + 2*m.b330*m.b849 + 2*m.b331*m.b459 - 2*m.b459 + 2*m.b331*m.b613
                        + 2*m.b332*m.b333 - 4*m.b333 + 2*m.b333*m.b335 - 2*m.b335 + 2*m.b333*m.b414 + 2*m.b333*m.b842 + 
                       2*m.b334*m.b336 + 2*m.b335*m.b336 + 2*m.b335*m.b463 - 4*m.b463 - 2*m.b335*m.b532 + 2*m.b336*
                       m.b801 + 2*m.b337*m.b417 - 4*m.b417 - 2*m.b337*m.b655 + 2*m.b337*m.b801 + 2*m.b338*m.b416 - 4*
                       m.b416 + 2*m.b338*m.b418 + 2*m.b338*m.b525 + 2*m.b339*m.b548 + 2*m.b339*m.b854 - 2*m.b340*m.b341
                        + 2*m.b340*m.b657 + 2*m.b340*m.b721 - 2*m.b341*m.b658 - 2*m.b341*m.b817 + 2*m.b342*m.b343 - 2*
                       m.b342 - 4*m.b343 - 2*m.b342*m.b482 + 2*m.b482 + 2*m.b342*m.b626 + 2*m.b342*m.b764 + 2*m.b343*
                       m.b344 + 2*m.b343*m.b484 + 2*m.b343*m.b802 + 2*m.b344*m.b433 - 4*m.b433 - 2*m.b344*m.b571 - 2*
                       m.b345*m.b584 + 2*m.b345*m.b596 + 2*m.b345*m.b737 + 2*m.b346*m.b646 - 2*m.b346*m.b786 + 2*m.b347*
                       m.b348 + 2*m.b347*m.b573 + 2*m.b348*m.b646 + 2*m.b348*m.b846 - 2*m.b349*m.b350 + 2*m.b349 + 2*
                       m.b350 - 2*m.b349*m.b598 + 2*m.b349*m.b647 - 2*m.b349*m.b779 - 2*m.b350*m.b536 + 2*m.b350*m.b825
                        - 2*m.b350*m.b858 + 2*m.b351*m.b353 + 2*m.b351*m.b734 - 2*m.b352*m.b676 - 2*m.b352*m.b677 - 2*
                       m.b352*m.b797 + 2*m.b353*m.b797 + 2*m.b353*m.b825 - 2*m.b354*m.b853 - 2*m.b355*m.b663 - 2*m.b355*
                       m.b714 + 2*m.b356*m.b357 - 4*m.b357 - 2*m.b356*m.b600 + 2*m.b356*m.b799 + 2*m.b357*m.b359 - 2*
                       m.b359 + 2*m.b357*m.b714 + 2*m.b357*m.b747 - 2*m.b358*m.b361 + 4*m.b358 - 2*m.b361 - 2*m.b358*
                       m.b578 - 2*m.b358*m.b665 - 2*m.b358*m.b807 + 2*m.b359*m.b361 - 2*m.b359*m.b623 + 2*m.b359*m.b624
                        - 2*m.b360*m.b363 - 2*m.b363 + 2*m.b360*m.b563 + 2*m.b361*m.b363 + 2*m.b361*m.b808 + 2*m.b362*
                       m.b566 - 2*m.b362 + 2*m.b362*m.b612 + 2*m.b362*m.b679 - 2*m.b362*m.b680 + 2*m.b363*m.b680 + 2*
                       m.b363*m.b760 - 2*m.b364*m.b408 + 2*m.b408 - 2*m.b364*m.b840 - 2*m.b365*m.b366 - 2*m.b366 - 2*
                       m.b365*m.b406 - 2*m.b365*m.b625 + 2*m.b366*m.b367 + 2*m.b366*m.b725 + 2*m.b366*m.b840 + 2*m.b367*
                       m.b514 - 2*m.b514 + 2*m.b367*m.b625 + 2*m.b368*m.b370 - 4*m.b370 + 2*m.b369*m.b370 + 2*m.b369*
                       m.b514 + 2*m.b369*m.b841 + 2*m.b370*m.b372 - 4*m.b372 + 2*m.b370*m.b464 + 2*m.b371*m.b373 + 2*
                       m.b372*m.b373 + 2*m.b372*m.b518 - 4*m.b518 + 2*m.b372*m.b532 + 2*m.b373*m.b791 + 2*m.b374*m.b469
                        - 2*m.b469 - 2*m.b374*m.b637 + 2*m.b374*m.b791 + 2*m.b375*m.b377 + 2*m.b375*m.b468 - 4*m.b468 + 
                       2*m.b375*m.b470 + 2*m.b376*m.b379 + 2*m.b376*m.b537 + 2*m.b377*m.b379 + 2*m.b377*m.b469 + 2*
                       m.b378*m.b380 - 2*m.b380 + 2*m.b378*m.b558 + 2*m.b379*m.b380 + 2*m.b381*m.b856 - 2*m.b382*m.b383
                        + 2*m.b382*m.b384 - 4*m.b384 + 2*m.b382*m.b711 - 2*m.b383*m.b385 - 2*m.b385 - 2*m.b383*m.b672 + 
                       2*m.b384*m.b385 + 2*m.b384*m.b640 + 2*m.b384*m.b856 + 2*m.b385*m.b754 + 2*m.b385*m.b813 + 2*
                       m.b386*m.b387 - 2*m.b386 - 4*m.b387 - 2*m.b386*m.b430 + 2*m.b430 + 2*m.b386*m.b639 + 2*m.b386*
                       m.b754 + 2*m.b387*m.b388 + 2*m.b387*m.b685 + 2*m.b387*m.b812 + 2*m.b388*m.b486 - 4*m.b486 + 2*
                       m.b388*m.b571 + 2*m.b389*m.b585 + 2*m.b389*m.b733 + 2*m.b389*m.b742 + 2*m.b390*m.b631 - 2*m.b390*
                       m.b778 + 2*m.b391*m.b392 + 2*m.b391*m.b795 + 2*m.b392*m.b631 + 2*m.b392*m.b835 + 2*m.b393*m.b395
                        - 4*m.b393 - 4*m.b395 + 2*m.b393*m.b674 + 2*m.b393*m.b686 + 2*m.b393*m.b835 - 2*m.b394*m.b609 + 
                       2*m.b394 + 2*m.b394*m.b633 - 2*m.b394*m.b768 - 2*m.b394*m.b769 + 2*m.b395*m.b562 + 2*m.b395*
                       m.b621 + 2*m.b395*m.b769 + 2*m.b396*m.b399 + 2*m.b396*m.b729 - 2*m.b396*m.b746 + 2*m.b397*m.b399
                        + 2*m.b397*m.b769 + 2*m.b397*m.b824 + 2*m.b398*m.b531 - 2*m.b398*m.b689 - 2*m.b398*m.b788 + 2*
                       m.b399*m.b788 - 2*m.b400*m.b848 + 2*m.b401*m.b403 - 4*m.b401 - 2*m.b403 + 2*m.b401*m.b503 + 2*
                       m.b401*m.b704 + 2*m.b401*m.b832 - 2*m.b402*m.b404 + 2*m.b402 + 2*m.b402*m.b502 - 4*m.b502 - 2*
                       m.b402*m.b679 - 2*m.b402*m.b799 + 2*m.b403*m.b404 - 2*m.b403*m.b611 + 2*m.b403*m.b612 + 2*m.b404*
                       m.b405 - 2*m.b405 + 2*m.b405*m.b407 - 2*m.b407 - 2*m.b405*m.b715 + 2*m.b405*m.b748 - 2*m.b406*
                       m.b834 + 2*m.b407*m.b510 + 2*m.b510 - 2*m.b407*m.b567 + 2*m.b407*m.b834 - 2*m.b408*m.b409 - 2*
                       m.b409 + 2*m.b408*m.b509 - 2*m.b509 - 2*m.b408*m.b636 + 2*m.b409*m.b410 + 2*m.b409*m.b716 + 2*
                       m.b409*m.b834 + 2*m.b410*m.b636 + 2*m.b410*m.b809 + 2*m.b411*m.b413 - 2*m.b411*m.b707 + 2*m.b412*
                       m.b517 - 2*m.b517 - 2*m.b412*m.b790 + 2*m.b413*m.b517 + 2*m.b413*m.b809 + 2*m.b414*m.b415 + 2*
                       m.b415*m.b782 - 2*m.b415*m.b860 + 2*m.b416*m.b524 - 2*m.b524 + 2*m.b416*m.b637 + 2*m.b416*m.b782
                        + 2*m.b417*m.b418 + 2*m.b417*m.b419 + 2*m.b417*m.b523 - 4*m.b523 - 2*m.b418*m.b855 + 2*m.b419*
                       m.b524 + 2*m.b419*m.b855 + 2*m.b420*m.b421 - 2*m.b421 + 2*m.b420*m.b568 + 2*m.b421*m.b855 + 2*
                       m.b422*m.b851 - 2*m.b423*m.b424 + 2*m.b423*m.b425 - 4*m.b425 + 2*m.b423*m.b696 - 2*m.b424*m.b426
                        - 2*m.b426 - 2*m.b424*m.b476 + 2*m.b476 + 2*m.b425*m.b426 + 2*m.b425*m.b627 + 2*m.b425*m.b851 + 
                       2*m.b426*m.b741 + 2*m.b426*m.b803 + 2*m.b427*m.b429 - 2*m.b427 - 2*m.b429 - 2*m.b427*m.b480 + 2*
                       m.b427*m.b640 + 2*m.b427*m.b658 + 2*m.b428*m.b431 - 2*m.b428*m.b478 - 2*m.b478 + 2*m.b428*m.b743
                        + 2*m.b429*m.b431 - 2*m.b429*m.b571 + 2*m.b429*m.b741 + 2*m.b430*m.b432 - 2*m.b430*m.b551 - 2*
                       m.b430*m.b585 + 2*m.b431*m.b432 + 2*m.b432*m.b434 + 2*m.b433*m.b435 + 2*m.b433*m.b737 + 2*m.b433*
                       m.b755 + 2*m.b434*m.b435 + 2*m.b434*m.b775 + 2*m.b435*m.b859 + 2*m.b436*m.b439 + 2*m.b436*m.b787
                        + 2*m.b437*m.b439 + 2*m.b437*m.b767 + 2*m.b437*m.b859 - 2*m.b438*m.b829 + 2*m.b439*m.b829 + 2*
                       m.b440*m.b661 - 4*m.b440 + 2*m.b440*m.b700 + 2*m.b440*m.b829 + 2*m.b440*m.b858 - 2*m.b441*m.b620
                        + 4*m.b441 - 2*m.b441*m.b621 - 2*m.b441*m.b758 - 2*m.b441*m.b759 + 2*m.b442*m.b445 + 2*m.b442*
                       m.b724 - 2*m.b442*m.b759 + 2*m.b443*m.b445 + 2*m.b443*m.b759 + 2*m.b443*m.b830 + 2*m.b444*m.b536
                        - 2*m.b444*m.b702 - 2*m.b444*m.b780 + 2*m.b445*m.b780 - 2*m.b446*m.b839 + 2*m.b447*m.b576 + 2*
                       m.b447*m.b634 - 2*m.b447*m.b690 + 2*m.b448*m.b449 - 4*m.b448 + 2*m.b448*m.b450 + 2*m.b448*m.b690
                        + 2*m.b448*m.b838 - 2*m.b449*m.b451 - 2*m.b449*m.b505 + 2*m.b450*m.b451 + 2*m.b450*m.b611 + 2*
                       m.b451*m.b452 - 2*m.b452 + 2*m.b452*m.b454 - 2*m.b454 - 2*m.b452*m.b705 + 2*m.b452*m.b739 + 2*
                       m.b453*m.b808 - 2*m.b453*m.b827 + 2*m.b454*m.b455 - 2*m.b454*m.b580 + 2*m.b454*m.b827 - 2*m.b455*
                       m.b456 - 2*m.b456 - 2*m.b455*m.b653 + 2*m.b456*m.b458 + 2*m.b456*m.b706 + 2*m.b456*m.b827 - 2*
                       m.b457*m.b653 - 2*m.b457*m.b654 - 2*m.b457*m.b800 + 2*m.b458*m.b653 + 2*m.b458*m.b800 + 2*m.b459*
                       m.b461 - 2*m.b459*m.b693 + 2*m.b459*m.b842 + 2*m.b460*m.b463 - 2*m.b460*m.b800 + 2*m.b461*m.b463
                        + 2*m.b461*m.b800 + 2*m.b462*m.b465 + 2*m.b463*m.b465 + 2*m.b464*m.b466 - 4*m.b466 + 2*m.b465*
                       m.b466 + 2*m.b466*m.b557 + 2*m.b466*m.b772 - 2*m.b467*m.b537 - 2*m.b467*m.b569 + 2*m.b468*m.b569
                        + 2*m.b468*m.b655 + 2*m.b468*m.b772 + 2*m.b469*m.b471 - 2*m.b469*m.b547 - 2*m.b470*m.b527 + 2*
                       m.b527 + 2*m.b471*m.b527 + 2*m.b471*m.b569 + 2*m.b472*m.b550 - 2*m.b472 + 2*m.b472*m.b845 - 2*
                       m.b473*m.b474 + 2*m.b473*m.b475 - 4*m.b475 - 2*m.b474*m.b477 - 2*m.b474*m.b698 + 2*m.b475*m.b477
                        + 2*m.b475*m.b616 + 2*m.b475*m.b845 - 2*m.b476*m.b479 - 2*m.b479 - 2*m.b476*m.b549 + 2*m.b476*
                       m.b552 + 2*m.b477*m.b479 + 2*m.b478*m.b481 - 4*m.b481 + 2*m.b478*m.b627 + 2*m.b478*m.b672 + 2*
                       m.b479*m.b481 + 2*m.b479*m.b753 + 2*m.b480*m.b483 + 2*m.b480*m.b813 + 2*m.b481*m.b483 + 2*m.b481*
                       m.b571 + 2*m.b482*m.b485 - 2*m.b482*m.b543 - 2*m.b482*m.b596 + 2*m.b483*m.b485 + 2*m.b484*m.b487
                        - 2*m.b487 + 2*m.b485*m.b487 + 2*m.b486*m.b488 + 2*m.b486*m.b733 + 2*m.b486*m.b765 + 2*m.b487*
                       m.b488 - 2*m.b487*m.b699 + 2*m.b488*m.b857 + 2*m.b489*m.b491 + 2*m.b491 + 2*m.b489*m.b492 - 2*
                       m.b492 + 2*m.b490*m.b492 + 2*m.b490*m.b777 + 2*m.b490*m.b857 - 2*m.b491*m.b575 - 2*m.b491*m.b778
                        - 2*m.b491*m.b823 - 2*m.b492*m.b493 + 2*m.b492*m.b823 + 2*m.b493*m.b494 - 4*m.b494 - 2*m.b493*
                       m.b645 + 2*m.b494*m.b648 + 2*m.b494*m.b823 + 2*m.b494*m.b852 - 2*m.b495*m.b632 + 4*m.b495 - 2*
                       m.b495*m.b633 - 2*m.b495*m.b745 - 2*m.b495*m.b746 + 2*m.b496*m.b498 + 2*m.b496*m.b499 - 2*m.b496*
                       m.b769 + 2*m.b497*m.b499 + 2*m.b497*m.b746 + 2*m.b497*m.b836 - 2*m.b498*m.b770 + 2*m.b499*m.b770
                        - 2*m.b500*m.b650 - 2*m.b500*m.b833 + 2*m.b501*m.b502 + 2*m.b501*m.b703 + 2*m.b501*m.b833 + 2*
                       m.b502*m.b504 + 2*m.b502*m.b847 - 2*m.b503*m.b506 - 2*m.b503*m.b705 + 2*m.b504*m.b506 + 2*m.b504*
                       m.b623 - 2*m.b505*m.b508 - 2*m.b508 - 2*m.b505*m.b545 + 2*m.b506*m.b508 - 2*m.b507*m.b509 - 2*
                       m.b507*m.b592 - 2*m.b507*m.b635 + 2*m.b508*m.b509 + 2*m.b508*m.b735 + 2*m.b509*m.b819 - 2*m.b510*
                       m.b511 - 2*m.b511 - 2*m.b510*m.b666 - 2*m.b510*m.b691 + 2*m.b511*m.b513 + 2*m.b511*m.b692 + 2*
                       m.b511*m.b819 - 2*m.b512*m.b666 + 4*m.b512 - 2*m.b512*m.b667 - 2*m.b512*m.b789 - 2*m.b512*m.b790
                        + 2*m.b513*m.b666 + 2*m.b513*m.b790 + 2*m.b514*m.b516 - 2*m.b514*m.b681 + 2*m.b515*m.b518 - 2*
                       m.b515*m.b809 + 2*m.b516*m.b518 + 2*m.b516*m.b790 + 2*m.b517*m.b519 - 2*m.b517*m.b860 + 2*m.b518*
                       m.b860 + 2*m.b519*m.b520 + 2*m.b520*m.b521 - 2*m.b521 + 2*m.b520*m.b860 + 2*m.b521*m.b523 - 2*
                       m.b521*m.b718 + 2*m.b521*m.b761 + 2*m.b522*m.b557 - 2*m.b522*m.b559 + 2*m.b523*m.b559 + 2*m.b523*
                       m.b669 + 2*m.b524*m.b526 - 2*m.b524*m.b542 - 2*m.b525*m.b844 + 2*m.b526*m.b559 + 2*m.b526*m.b844
                        - 2*m.b527*m.b850 - 2*m.b527*m.b861 - 2*m.b528*m.b529 + 2*m.b528*m.b654 - 2*m.b530*m.b531 + 2*
                       m.b530*m.b634 - 2*m.b532*m.b581 + 2*m.b533*m.b534 - 2*m.b533*m.b659 + 2*m.b534*m.b543 - 2*m.b534*
                       m.b629 - 2*m.b534*m.b630 - 2*m.b535*m.b536 - 2*m.b537*m.b548 - 2*m.b538*m.b539 + 2*m.b539*m.b628
                        + 2*m.b539*m.b712 - 2*m.b539*m.b793 + 2*m.b540*m.b541 - 2*m.b540*m.b643 + 2*m.b541*m.b551 - 2*
                       m.b541*m.b642 - 2*m.b541*m.b644 + 2*m.b542*m.b581 - 2*m.b543*m.b544 + 2*m.b544*m.b617 + 2*m.b544*
                       m.b698 - 2*m.b544*m.b802 + 2*m.b545*m.b546 + 2*m.b545*m.b705 - 2*m.b546*m.b690 + 2*m.b549*m.b550
                        - 2*m.b550*m.b696 - 2*m.b550*m.b697 - 2*m.b551*m.b552 + 2*m.b552*m.b616 - 2*m.b552*m.b812 + 2*
                       m.b553*m.b645 - 2*m.b554*m.b555 + 2*m.b554*m.b556 - 2*m.b554*m.b679 + 2*m.b554*m.b715 + 2*m.b555*
                       m.b599 - 2*m.b555*m.b664 - 2*m.b556*m.b704 - 2*m.b557*m.b731 - 2*m.b557*m.b773 - 2*m.b558*m.b559
                        - 2*m.b560*m.b672 + 2*m.b560*m.b698 + 2*m.b561*m.b660 - 2*m.b562*m.b688 - 2*m.b563*m.b564 + 2*
                       m.b563*m.b565 - 2*m.b563*m.b665 + 2*m.b564*m.b589 - 2*m.b564*m.b651 - 2*m.b565*m.b714 - 2*m.b566*
                       m.b567 + 2*m.b566*m.b614 + 2*m.b567*m.b624 + 2*m.b567*m.b665 - 2*m.b568*m.b569 - 2*m.b570*m.b658
                        + 2*m.b570*m.b712 - 2*m.b572*m.b573 + 2*m.b572*m.b673 - 2*m.b573*m.b805 + 2*m.b574*m.b575 - 2*
                       m.b574*m.b675 - 2*m.b575*m.b779 + 2*m.b577*m.b578 - 2*m.b577*m.b652 - 2*m.b579*m.b580 + 2*m.b580*
                       m.b635 + 2*m.b580*m.b652 + 2*m.b581*m.b731 - 2*m.b581*m.b750 - 2*m.b582*m.b641 + 2*m.b582*m.b722
                        + 2*m.b583*m.b584 - 2*m.b583*m.b585 - 2*m.b583*m.b608 - 2*m.b586*m.b587 - 2*m.b586*m.b597 + 2*
                       m.b587*m.b608 + 2*m.b587*m.b794 - 2*m.b588*m.b662 - 2*m.b589*m.b590 + 2*m.b589*m.b591 - 2*m.b589*
                       m.b623 - 2*m.b591*m.b780 - 2*m.b591*m.b806 - 2*m.b593*m.b717 - 2*m.b594*m.b595 - 2*m.b594*m.b628
                        - 2*m.b595*m.b763 - 2*m.b599*m.b600 + 2*m.b599*m.b601 - 2*m.b599*m.b611 + 2*m.b600*m.b677 - 2*
                       m.b601*m.b788 - 2*m.b601*m.b798 - 2*m.b602*m.b603 - 2*m.b603*m.b624 - 2*m.b604*m.b707 - 2*m.b605*
                       m.b606 - 2*m.b605*m.b617 - 2*m.b606*m.b752 - 2*m.b608*m.b777 + 2*m.b610*m.b663 - 2*m.b610*m.b832
                        - 2*m.b612*m.b678 + 2*m.b613*m.b614 - 2*m.b613*m.b693 - 2*m.b614*m.b771 - 2*m.b615*m.b616 + 2*
                       m.b615*m.b617 - 2*m.b615*m.b618 - 2*m.b616*m.b684 - 2*m.b617*m.b697 + 2*m.b618*m.b785 - 2*m.b621*
                       m.b702 + 2*m.b622*m.b649 - 2*m.b622*m.b838 - 2*m.b624*m.b664 - 2*m.b625*m.b681 - 2*m.b626*m.b627
                        + 2*m.b626*m.b628 - 2*m.b626*m.b629 - 2*m.b627*m.b671 - 2*m.b631*m.b859 - 2*m.b633*m.b689 - 2*
                       m.b635*m.b651 - 2*m.b636*m.b668 - 2*m.b637*m.b638 - 2*m.b638*m.b815 - 2*m.b639*m.b640 + 2*m.b639*
                       m.b641 - 2*m.b639*m.b642 - 2*m.b640*m.b657 + 2*m.b642*m.b803 - 2*m.b643*m.b644 + 2*m.b644*m.b743
                        - 2*m.b645*m.b646 - 2*m.b646*m.b857 - 2*m.b647*m.b648 - 2*m.b647*m.b676 - 2*m.b648*m.b738 + 2*
                       m.b649*m.b650 + 2*m.b650*m.b702 - 2*m.b650*m.b825 + 2*m.b651*m.b818 - 2*m.b654*m.b694 - 2*m.b655*
                       m.b656 - 2*m.b656*m.b810 + 2*m.b657*m.b817 - 2*m.b657*m.b856 - 2*m.b660*m.b700 + 2*m.b662*m.b779
                        + 2*m.b664*m.b826 + 2*m.b667*m.b668 - 2*m.b667*m.b682 + 2*m.b668*m.b789 - 2*m.b668*m.b809 - 2*
                       m.b669*m.b670 - 2*m.b670*m.b801 + 2*m.b671*m.b720 + 2*m.b671*m.b822 - 2*m.b671*m.b851 - 2*m.b673*
                       m.b686 + 2*m.b675*m.b768 - 2*m.b675*m.b796 - 2*m.b677*m.b703 + 2*m.b680*m.b840 + 2*m.b681*m.b781
                        - 2*m.b683*m.b791 + 2*m.b684*m.b710 + 2*m.b684*m.b828 - 2*m.b684*m.b845 + 2*m.b685*m.b776 - 2*
                       m.b685*m.b804 - 2*m.b686*m.b723 + 2*m.b687*m.b723 + 2*m.b688*m.b758 - 2*m.b688*m.b836 + 2*m.b690*
                       m.b839 + 2*m.b691*m.b849 - 2*m.b695*m.b782 - 2*m.b698*m.b741 - 2*m.b700*m.b713 + 2*m.b701*m.b713
                        - 2*m.b703*m.b704 + 2*m.b704*m.b848 - 2*m.b708*m.b772 - 2*m.b709*m.b736 - 2*m.b710*m.b711 - 2*
                       m.b712*m.b752 - 2*m.b712*m.b754 - 2*m.b713*m.b852 + 2*m.b714*m.b853 - 2*m.b715*m.b747 - 2*m.b717*
                       m.b841 + 2*m.b718*m.b726 - 2*m.b719*m.b732 - 2*m.b720*m.b721 - 2*m.b722*m.b763 - 2*m.b722*m.b764
                        + 2*m.b723*m.b846 - 2*m.b723*m.b858 - 2*m.b726*m.b727 - 2*m.b726*m.b728 - 2*m.b733*m.b859 + 2*
                       m.b735*m.b814 - 2*m.b735*m.b819 - 2*m.b737*m.b857 - 2*m.b739*m.b814 - 2*m.b740*m.b741 - 2*m.b740*
                       m.b743 - 2*m.b742*m.b743 + 2*m.b744*m.b786 - 2*m.b744*m.b846 + 2*m.b746*m.b852 - 2*m.b748*m.b808
                        + 2*m.b749*m.b750 - 2*m.b749*m.b751 - 2*m.b750*m.b791 - 2*m.b753*m.b754 - 2*m.b753*m.b756 - 2*
                       m.b755*m.b756 + 2*m.b756*m.b812 + 2*m.b757*m.b778 - 2*m.b757*m.b835 + 2*m.b759*m.b858 - 2*m.b761*
                       m.b772 - 2*m.b762*m.b801 + 2*m.b764*m.b817 - 2*m.b765*m.b766 + 2*m.b766*m.b802 + 2*m.b770*m.b833
                        - 2*m.b773*m.b810 + 2*m.b774*m.b822 - 2*m.b775*m.b776 + 2*m.b776*m.b793 + 2*m.b777*m.b778 + 2*
                       m.b780*m.b839 - 2*m.b783*m.b815 - 2*m.b784*m.b785 + 2*m.b785*m.b828 - 2*m.b786*m.b787 + 2*m.b788*
                       m.b848 - 2*m.b792*m.b820 - 2*m.b794*m.b795 + 2*m.b796*m.b837 + 2*m.b797*m.b853 - 2*m.b798*m.b799
                        - 2*m.b802*m.b803 - 2*m.b803*m.b828 - 2*m.b804*m.b805 - 2*m.b806*m.b807 - 2*m.b808*m.b826 - 2*
                       m.b811*m.b845 - 2*m.b812*m.b813 - 2*m.b813*m.b822 - 2*m.b814*m.b818 - 2*m.b816*m.b851 - 2*m.b821*
                       m.b856 - 2*m.b824*m.b825 - 2*m.b830*m.b831 - 2*m.b832*m.b833 - 2*m.b836*m.b837 - 2*m.b838*m.b839
                        - 2*m.b841*m.b842 - 2*m.b843*m.b844 + 2*m.b844*m.b861 - 2*m.b847*m.b848 - 2*m.b854*m.b855
                        + m.x862 <= 0)
