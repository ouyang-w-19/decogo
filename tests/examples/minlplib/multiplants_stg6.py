#  MINLP written by GAMS Convert at 04/21/18 13:52:37
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        388      197       28      163        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        694      310      384        0        0        0        0        0
#  FX     97       97        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2887     2721      166        0


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
m.x385 = Var(within=Reals,bounds=(0,702000),initialize=0)
m.x386 = Var(within=Reals,bounds=(0,702000),initialize=0)
m.x387 = Var(within=Reals,bounds=(0,702000),initialize=0)
m.x388 = Var(within=Reals,bounds=(0,702000),initialize=0)
m.x389 = Var(within=Reals,bounds=(0,702000),initialize=0)
m.x390 = Var(within=Reals,bounds=(0,702000),initialize=0)
m.x391 = Var(within=Reals,bounds=(0,702000),initialize=0)
m.x392 = Var(within=Reals,bounds=(0,702000),initialize=0)
m.x393 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x394 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x395 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x396 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x397 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x398 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x399 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x400 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x401 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x402 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x403 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x404 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x405 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x406 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x407 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x408 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x409 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x410 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x411 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x412 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x413 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x414 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x415 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x416 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x417 = Var(within=Reals,bounds=(0,774000),initialize=0)
m.x418 = Var(within=Reals,bounds=(0,774000),initialize=0)
m.x419 = Var(within=Reals,bounds=(0,774000),initialize=0)
m.x420 = Var(within=Reals,bounds=(0,774000),initialize=0)
m.x421 = Var(within=Reals,bounds=(0,774000),initialize=0)
m.x422 = Var(within=Reals,bounds=(0,774000),initialize=0)
m.x423 = Var(within=Reals,bounds=(0,774000),initialize=0)
m.x424 = Var(within=Reals,bounds=(0,774000),initialize=0)
m.x425 = Var(within=Reals,bounds=(0,1116000),initialize=0)
m.x426 = Var(within=Reals,bounds=(0,1116000),initialize=0)
m.x427 = Var(within=Reals,bounds=(0,1116000),initialize=0)
m.x428 = Var(within=Reals,bounds=(0,1116000),initialize=0)
m.x429 = Var(within=Reals,bounds=(0,1116000),initialize=0)
m.x430 = Var(within=Reals,bounds=(0,1116000),initialize=0)
m.x431 = Var(within=Reals,bounds=(0,1116000),initialize=0)
m.x432 = Var(within=Reals,bounds=(0,1116000),initialize=0)
m.x433 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x434 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x435 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x436 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x437 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x438 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x439 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x440 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x441 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x442 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x443 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x444 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x445 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x446 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x447 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x448 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x449 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x450 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x451 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x452 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x453 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x454 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x455 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x456 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x457 = Var(within=Reals,bounds=(0,726000),initialize=0)
m.x458 = Var(within=Reals,bounds=(0,726000),initialize=0)
m.x459 = Var(within=Reals,bounds=(0,726000),initialize=0)
m.x460 = Var(within=Reals,bounds=(0,726000),initialize=0)
m.x461 = Var(within=Reals,bounds=(0,726000),initialize=0)
m.x462 = Var(within=Reals,bounds=(0,726000),initialize=0)
m.x463 = Var(within=Reals,bounds=(0,726000),initialize=0)
m.x464 = Var(within=Reals,bounds=(0,726000),initialize=0)
m.x465 = Var(within=Reals,bounds=(0,696000),initialize=0)
m.x466 = Var(within=Reals,bounds=(0,696000),initialize=0)
m.x467 = Var(within=Reals,bounds=(0,696000),initialize=0)
m.x468 = Var(within=Reals,bounds=(0,696000),initialize=0)
m.x469 = Var(within=Reals,bounds=(0,696000),initialize=0)
m.x470 = Var(within=Reals,bounds=(0,696000),initialize=0)
m.x471 = Var(within=Reals,bounds=(0,696000),initialize=0)
m.x472 = Var(within=Reals,bounds=(0,696000),initialize=0)
m.x473 = Var(within=Reals,bounds=(0,852000),initialize=0)
m.x474 = Var(within=Reals,bounds=(0,852000),initialize=0)
m.x475 = Var(within=Reals,bounds=(0,852000),initialize=0)
m.x476 = Var(within=Reals,bounds=(0,852000),initialize=0)
m.x477 = Var(within=Reals,bounds=(0,852000),initialize=0)
m.x478 = Var(within=Reals,bounds=(0,852000),initialize=0)
m.x479 = Var(within=Reals,bounds=(0,852000),initialize=0)
m.x480 = Var(within=Reals,bounds=(0,852000),initialize=0)
m.x481 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x482 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x483 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x484 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x485 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x486 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x487 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x488 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x489 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x490 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x491 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x492 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x493 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x494 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x495 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x496 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x497 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x498 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x499 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x500 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x501 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x502 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x503 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x504 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x505 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x506 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x507 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x508 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x509 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x510 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x511 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x512 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x513 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x514 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x515 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x516 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x517 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x518 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x519 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x520 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x521 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x522 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x523 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x524 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x525 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x526 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x527 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x528 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x529 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x530 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x531 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x532 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x533 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x534 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x535 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x536 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x537 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x538 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x539 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x540 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x541 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x542 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x543 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x544 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x545 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x546 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x547 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x548 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x549 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x550 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x551 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x552 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x553 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x554 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x555 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x556 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x557 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x558 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x559 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x560 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x561 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x562 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x563 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x564 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x565 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x566 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x567 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x568 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x569 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x570 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x571 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x572 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x573 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x574 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x575 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x576 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x577 = Var(within=Reals,bounds=(0,702000),initialize=0)
m.x578 = Var(within=Reals,bounds=(0,702000),initialize=0)
m.x579 = Var(within=Reals,bounds=(0,702000),initialize=0)
m.x580 = Var(within=Reals,bounds=(0,702000),initialize=0)
m.x581 = Var(within=Reals,bounds=(0,702000),initialize=0)
m.x582 = Var(within=Reals,bounds=(0,702000),initialize=0)
m.x583 = Var(within=Reals,bounds=(0,702000),initialize=0)
m.x584 = Var(within=Reals,bounds=(0,702000),initialize=0)
m.x585 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x586 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x587 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x588 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x589 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x590 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x591 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x592 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x593 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x594 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x595 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x596 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x597 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x598 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x599 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x600 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x601 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x602 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x603 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x604 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x605 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x606 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x607 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x608 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x609 = Var(within=Reals,bounds=(0,774000),initialize=0)
m.x610 = Var(within=Reals,bounds=(0,774000),initialize=0)
m.x611 = Var(within=Reals,bounds=(0,774000),initialize=0)
m.x612 = Var(within=Reals,bounds=(0,774000),initialize=0)
m.x613 = Var(within=Reals,bounds=(0,774000),initialize=0)
m.x614 = Var(within=Reals,bounds=(0,774000),initialize=0)
m.x615 = Var(within=Reals,bounds=(0,774000),initialize=0)
m.x616 = Var(within=Reals,bounds=(0,774000),initialize=0)
m.x617 = Var(within=Reals,bounds=(0,1116000),initialize=0)
m.x618 = Var(within=Reals,bounds=(0,1116000),initialize=0)
m.x619 = Var(within=Reals,bounds=(0,1116000),initialize=0)
m.x620 = Var(within=Reals,bounds=(0,1116000),initialize=0)
m.x621 = Var(within=Reals,bounds=(0,1116000),initialize=0)
m.x622 = Var(within=Reals,bounds=(0,1116000),initialize=0)
m.x623 = Var(within=Reals,bounds=(0,1116000),initialize=0)
m.x624 = Var(within=Reals,bounds=(0,1116000),initialize=0)
m.x625 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x626 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x627 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x628 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x629 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x630 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x631 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x632 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x633 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x634 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x635 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x636 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x637 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x638 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x639 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x640 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x641 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x642 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x643 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x644 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x645 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x646 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x647 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x648 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x649 = Var(within=Reals,bounds=(0,726000),initialize=0)
m.x650 = Var(within=Reals,bounds=(0,726000),initialize=0)
m.x651 = Var(within=Reals,bounds=(0,726000),initialize=0)
m.x652 = Var(within=Reals,bounds=(0,726000),initialize=0)
m.x653 = Var(within=Reals,bounds=(0,726000),initialize=0)
m.x654 = Var(within=Reals,bounds=(0,726000),initialize=0)
m.x655 = Var(within=Reals,bounds=(0,726000),initialize=0)
m.x656 = Var(within=Reals,bounds=(0,726000),initialize=0)
m.x657 = Var(within=Reals,bounds=(0,696000),initialize=0)
m.x658 = Var(within=Reals,bounds=(0,696000),initialize=0)
m.x659 = Var(within=Reals,bounds=(0,696000),initialize=0)
m.x660 = Var(within=Reals,bounds=(0,696000),initialize=0)
m.x661 = Var(within=Reals,bounds=(0,696000),initialize=0)
m.x662 = Var(within=Reals,bounds=(0,696000),initialize=0)
m.x663 = Var(within=Reals,bounds=(0,696000),initialize=0)
m.x664 = Var(within=Reals,bounds=(0,696000),initialize=0)
m.x665 = Var(within=Reals,bounds=(0,852000),initialize=0)
m.x666 = Var(within=Reals,bounds=(0,852000),initialize=0)
m.x667 = Var(within=Reals,bounds=(0,852000),initialize=0)
m.x668 = Var(within=Reals,bounds=(0,852000),initialize=0)
m.x669 = Var(within=Reals,bounds=(0,852000),initialize=0)
m.x670 = Var(within=Reals,bounds=(0,852000),initialize=0)
m.x671 = Var(within=Reals,bounds=(0,852000),initialize=0)
m.x672 = Var(within=Reals,bounds=(0,852000),initialize=0)
m.x673 = Var(within=Reals,bounds=(0,702000),initialize=0)
m.x674 = Var(within=Reals,bounds=(0,1116000),initialize=0)
m.x675 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x676 = Var(within=Reals,bounds=(0,852000),initialize=0)
m.x677 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x678 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x679 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x680 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x681 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x682 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x683 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x684 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x685 = Var(within=Reals,bounds=(0,702000),initialize=0)
m.x686 = Var(within=Reals,bounds=(0,672000),initialize=0)
m.x687 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x688 = Var(within=Reals,bounds=(0,774000),initialize=0)
m.x689 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x690 = Var(within=Reals,bounds=(0,804000),initialize=0)
m.x691 = Var(within=Reals,bounds=(0,726000),initialize=0)
m.x692 = Var(within=Reals,bounds=(0,696000),initialize=0)
m.x693 = Var(within=Reals,bounds=(200,600),initialize=200)
m.x694 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x694, sense=maximize)

m.c1 = Constraint(expr=m.x694*m.x693 + (0.00203*m.x593 + 0.00203*m.x594)*(m.x678 - m.x677) + (0.00203*m.x594 + 0.00203*
                       m.x595)*(m.x679 - m.x678) + (0.00203*m.x595 + 0.00203*m.x596)*(m.x680 - m.x679) + (0.00203*m.x596
                        + 0.00203*m.x597)*(m.x681 - m.x680) + (0.00203*m.x597 + 0.00203*m.x598)*(m.x682 - m.x681) + (
                       0.00203*m.x598 + 0.00203*m.x599)*(m.x683 - m.x682) + (0.00203*m.x599 + 0.00203*m.x600)*(m.x684 - 
                       m.x683) + (0.00203*m.x593 + 0.00203*m.x600)*(m.x693 - m.x684) + (0.00203*m.x617 + 0.00203*m.x618)
                       *(m.x678 - m.x677) + (0.00203*m.x618 + 0.00203*m.x619)*(m.x679 - m.x678) + (0.00203*m.x619 + 
                       0.00203*m.x620)*(m.x680 - m.x679) + (0.00203*m.x620 + 0.00203*m.x621)*(m.x681 - m.x680) + (
                       0.00203*m.x621 + 0.00203*m.x622)*(m.x682 - m.x681) + (0.00203*m.x622 + 0.00203*m.x623)*(m.x683 - 
                       m.x682) + (0.00203*m.x623 + 0.00203*m.x624)*(m.x684 - m.x683) + (0.00203*m.x617 + 0.00203*m.x624)
                       *(m.x693 - m.x684) + (0.00203*m.x641 + 0.00203*m.x642)*(m.x678 - m.x677) + (0.00203*m.x642 + 
                       0.00203*m.x643)*(m.x679 - m.x678) + (0.00203*m.x643 + 0.00203*m.x644)*(m.x680 - m.x679) + (
                       0.00203*m.x644 + 0.00203*m.x645)*(m.x681 - m.x680) + (0.00203*m.x645 + 0.00203*m.x646)*(m.x682 - 
                       m.x681) + (0.00203*m.x646 + 0.00203*m.x647)*(m.x683 - m.x682) + (0.00203*m.x647 + 0.00203*m.x648)
                       *(m.x684 - m.x683) + (0.00203*m.x641 + 0.00203*m.x648)*(m.x693 - m.x684) + (0.00203*m.x665 + 
                       0.00203*m.x666)*(m.x678 - m.x677) + (0.00203*m.x666 + 0.00203*m.x667)*(m.x679 - m.x678) + (
                       0.00203*m.x667 + 0.00203*m.x668)*(m.x680 - m.x679) + (0.00203*m.x668 + 0.00203*m.x669)*(m.x681 - 
                       m.x680) + (0.00203*m.x669 + 0.00203*m.x670)*(m.x682 - m.x681) + (0.00203*m.x670 + 0.00203*m.x671)
                       *(m.x683 - m.x682) + (0.00203*m.x671 + 0.00203*m.x672)*(m.x684 - m.x683) + (0.00203*m.x665 + 
                       0.00203*m.x672)*(m.x693 - m.x684) + 7600*m.b97 + 7600*m.b98 + 7600*m.b99 + 7600*m.b100
                        + 7600*m.b101 + 7600*m.b102 + 7600*m.b103 + 7600*m.b104 + 7600*m.b105 + 7600*m.b106
                        + 7600*m.b107 + 7600*m.b108 + 7600*m.b109 + 7600*m.b110 + 7600*m.b111 + 7600*m.b112
                        + 7600*m.b113 + 7600*m.b114 + 7600*m.b115 + 7600*m.b116 + 7600*m.b117 + 7600*m.b118
                        + 7600*m.b119 + 7600*m.b120 + 7500*m.b121 + 7500*m.b122 + 7500*m.b123 + 7500*m.b124
                        + 7500*m.b125 + 7500*m.b126 + 7500*m.b127 + 7500*m.b128 + 750*m.b129 + 750*m.b130 + 750*m.b131
                        + 750*m.b132 + 750*m.b133 + 750*m.b134 + 750*m.b135 + 750*m.b136 + 3000*m.b137 + 3000*m.b138
                        + 3000*m.b139 + 3000*m.b140 + 3000*m.b141 + 3000*m.b142 + 3000*m.b143 + 3000*m.b144
                        + 7700*m.b145 + 7700*m.b146 + 7700*m.b147 + 7700*m.b148 + 7700*m.b149 + 7700*m.b150
                        + 7700*m.b151 + 7700*m.b152 + 770*m.b153 + 770*m.b154 + 770*m.b155 + 770*m.b156 + 770*m.b157
                        + 770*m.b158 + 770*m.b159 + 770*m.b160 + 3080*m.b161 + 3080*m.b162 + 3080*m.b163 + 3080*m.b164
                        + 3080*m.b165 + 3080*m.b166 + 3080*m.b167 + 3080*m.b168 + 7600*m.b169 + 7600*m.b170
                        + 7600*m.b171 + 7600*m.b172 + 7600*m.b173 + 7600*m.b174 + 7600*m.b175 + 7600*m.b176
                        + 3040*m.b177 + 3040*m.b178 + 3040*m.b179 + 3040*m.b180 + 3040*m.b181 + 3040*m.b182
                        + 3040*m.b183 + 3040*m.b184 + 3040*m.b185 + 3040*m.b186 + 3040*m.b187 + 3040*m.b188
                        + 3040*m.b189 + 3040*m.b190 + 3040*m.b191 + 3040*m.b192 + 2280*m.b193 + 2280*m.b194
                        + 2280*m.b195 + 2280*m.b196 + 2280*m.b197 + 2280*m.b198 + 2280*m.b199 + 2280*m.b200
                        + 2280*m.b201 + 2280*m.b202 + 2280*m.b203 + 2280*m.b204 + 2280*m.b205 + 2280*m.b206
                        + 2280*m.b207 + 2280*m.b208 + 9120*m.b209 + 9120*m.b210 + 9120*m.b211 + 9120*m.b212
                        + 9120*m.b213 + 9120*m.b214 + 9120*m.b215 + 9120*m.b216 + 2250*m.b217 + 2250*m.b218
                        + 2250*m.b219 + 2250*m.b220 + 2250*m.b221 + 2250*m.b222 + 2250*m.b223 + 2250*m.b224 + 750*m.b225
                        + 750*m.b226 + 750*m.b227 + 750*m.b228 + 750*m.b229 + 750*m.b230 + 750*m.b231 + 750*m.b232
                        + 9000*m.b233 + 9000*m.b234 + 9000*m.b235 + 9000*m.b236 + 9000*m.b237 + 9000*m.b238
                        + 9000*m.b239 + 9000*m.b240 + 2310*m.b241 + 2310*m.b242 + 2310*m.b243 + 2310*m.b244
                        + 2310*m.b245 + 2310*m.b246 + 2310*m.b247 + 2310*m.b248 + 770*m.b249 + 770*m.b250 + 770*m.b251
                        + 770*m.b252 + 770*m.b253 + 770*m.b254 + 770*m.b255 + 770*m.b256 + 9240*m.b257 + 9240*m.b258
                        + 9240*m.b259 + 9240*m.b260 + 9240*m.b261 + 9240*m.b262 + 9240*m.b263 + 9240*m.b264
                        + 9120*m.b265 + 9120*m.b266 + 9120*m.b267 + 9120*m.b268 + 9120*m.b269 + 9120*m.b270
                        + 9120*m.b271 + 9120*m.b272 + 9120*m.b273 + 9120*m.b274 + 9120*m.b275 + 9120*m.b276
                        + 9120*m.b277 + 9120*m.b278 + 9120*m.b279 + 9120*m.b280 + 9120*m.b281 + 9120*m.b282
                        + 9120*m.b283 + 9120*m.b284 + 9120*m.b285 + 9120*m.b286 + 9120*m.b287 + 9120*m.b288
                        + 1520*m.b289 + 1520*m.b290 + 1520*m.b291 + 1520*m.b292 + 1520*m.b293 + 1520*m.b294
                        + 1520*m.b295 + 1520*m.b296 + 1520*m.b297 + 1520*m.b298 + 1520*m.b299 + 1520*m.b300
                        + 1520*m.b301 + 1520*m.b302 + 1520*m.b303 + 1520*m.b304 + 6080*m.b305 + 6080*m.b306
                        + 6080*m.b307 + 6080*m.b308 + 6080*m.b309 + 6080*m.b310 + 6080*m.b311 + 6080*m.b312
                        + 1500*m.b313 + 1500*m.b314 + 1500*m.b315 + 1500*m.b316 + 1500*m.b317 + 1500*m.b318
                        + 1500*m.b319 + 1500*m.b320 + 750*m.b321 + 750*m.b322 + 750*m.b323 + 750*m.b324 + 750*m.b325
                        + 750*m.b326 + 750*m.b327 + 750*m.b328 + 6000*m.b329 + 6000*m.b330 + 6000*m.b331 + 6000*m.b332
                        + 6000*m.b333 + 6000*m.b334 + 6000*m.b335 + 6000*m.b336 + 1540*m.b337 + 1540*m.b338
                        + 1540*m.b339 + 1540*m.b340 + 1540*m.b341 + 1540*m.b342 + 1540*m.b343 + 1540*m.b344 + 770*m.b345
                        + 770*m.b346 + 770*m.b347 + 770*m.b348 + 770*m.b349 + 770*m.b350 + 770*m.b351 + 770*m.b352
                        + 6160*m.b353 + 6160*m.b354 + 6160*m.b355 + 6160*m.b356 + 6160*m.b357 + 6160*m.b358
                        + 6160*m.b359 + 6160*m.b360 + 6080*m.b361 + 6080*m.b362 + 6080*m.b363 + 6080*m.b364
                        + 6080*m.b365 + 6080*m.b366 + 6080*m.b367 + 6080*m.b368 + 6080*m.b369 + 6080*m.b370
                        + 6080*m.b371 + 6080*m.b372 + 6080*m.b373 + 6080*m.b374 + 6080*m.b375 + 6080*m.b376
                        + 6080*m.b377 + 6080*m.b378 + 6080*m.b379 + 6080*m.b380 + 6080*m.b381 + 6080*m.b382
                        + 6080*m.b383 + 6080*m.b384 - 4*m.x673 - 1.5*m.x674 - 6.5*m.x675 - 3*m.x676 + 0.1218*m.x685
                        + 0.1218*m.x686 + 0.1218*m.x687 + 0.1218*m.x688 + 0.1218*m.x689 + 0.1218*m.x690 + 0.1218*m.x691
                        + 0.1218*m.x692 == 0)

m.c2 = Constraint(expr=   m.b1 - m.b8 + m.b97 + m.b105 + m.b113 - m.b128 - m.b152 - m.b176 + m.x481 - m.x488 == 0)

m.c3 = Constraint(expr= - m.b1 + m.b2 + m.b98 + m.b106 + m.b114 - m.b121 - m.b145 - m.b169 - m.x481 + m.x482 == 0)

m.c4 = Constraint(expr= - m.b2 + m.b3 + m.b99 + m.b107 + m.b115 - m.b122 - m.b146 - m.b170 - m.x482 + m.x483 == 0)

m.c5 = Constraint(expr= - m.b3 + m.b4 + m.b100 + m.b108 + m.b116 - m.b123 - m.b147 - m.b171 - m.x483 + m.x484 == 0)

m.c6 = Constraint(expr= - m.b4 + m.b5 + m.b101 + m.b109 + m.b117 - m.b124 - m.b148 - m.b172 - m.x484 + m.x485 == 0)

m.c7 = Constraint(expr= - m.b5 + m.b6 + m.b102 + m.b110 + m.b118 - m.b125 - m.b149 - m.b173 - m.x485 + m.x486 == 0)

m.c8 = Constraint(expr= - m.b6 + m.b7 + m.b103 + m.b111 + m.b119 - m.b126 - m.b150 - m.b174 - m.x486 + m.x487 == 0)

m.c9 = Constraint(expr= - m.b7 + m.b8 + m.b104 + m.b112 + m.b120 - m.b127 - m.b151 - m.b175 - m.x487 + m.x488 == 0)

m.c10 = Constraint(expr=   m.b25 - m.b32 - m.b104 + m.b121 + m.b129 + m.b137 - m.b160 - m.b184 + m.x489 - m.x496 == 0)

m.c11 = Constraint(expr= - m.b25 + m.b26 - m.b97 + m.b122 + m.b130 + m.b138 - m.b153 - m.b177 - m.x489 + m.x490 == 0)

m.c12 = Constraint(expr= - m.b26 + m.b27 - m.b98 + m.b123 + m.b131 + m.b139 - m.b154 - m.b178 - m.x490 + m.x491 == 0)

m.c13 = Constraint(expr= - m.b27 + m.b28 - m.b99 + m.b124 + m.b132 + m.b140 - m.b155 - m.b179 - m.x491 + m.x492 == 0)

m.c14 = Constraint(expr= - m.b28 + m.b29 - m.b100 + m.b125 + m.b133 + m.b141 - m.b156 - m.b180 - m.x492 + m.x493 == 0)

m.c15 = Constraint(expr= - m.b29 + m.b30 - m.b101 + m.b126 + m.b134 + m.b142 - m.b157 - m.b181 - m.x493 + m.x494 == 0)

m.c16 = Constraint(expr= - m.b30 + m.b31 - m.b102 + m.b127 + m.b135 + m.b143 - m.b158 - m.b182 - m.x494 + m.x495 == 0)

m.c17 = Constraint(expr= - m.b31 + m.b32 - m.b103 + m.b128 + m.b136 + m.b144 - m.b159 - m.b183 - m.x495 + m.x496 == 0)

m.c18 = Constraint(expr=   m.b49 - m.b56 - m.b112 - m.b136 + m.b145 + m.b153 + m.b161 - m.b192 + m.x497 - m.x504 == 0)

m.c19 = Constraint(expr= - m.b49 + m.b50 - m.b105 - m.b129 + m.b146 + m.b154 + m.b162 - m.b185 - m.x497 + m.x498 == 0)

m.c20 = Constraint(expr= - m.b50 + m.b51 - m.b106 - m.b130 + m.b147 + m.b155 + m.b163 - m.b186 - m.x498 + m.x499 == 0)

m.c21 = Constraint(expr= - m.b51 + m.b52 - m.b107 - m.b131 + m.b148 + m.b156 + m.b164 - m.b187 - m.x499 + m.x500 == 0)

m.c22 = Constraint(expr= - m.b52 + m.b53 - m.b108 - m.b132 + m.b149 + m.b157 + m.b165 - m.b188 - m.x500 + m.x501 == 0)

m.c23 = Constraint(expr= - m.b53 + m.b54 - m.b109 - m.b133 + m.b150 + m.b158 + m.b166 - m.b189 - m.x501 + m.x502 == 0)

m.c24 = Constraint(expr= - m.b54 + m.b55 - m.b110 - m.b134 + m.b151 + m.b159 + m.b167 - m.b190 - m.x502 + m.x503 == 0)

m.c25 = Constraint(expr= - m.b55 + m.b56 - m.b111 - m.b135 + m.b152 + m.b160 + m.b168 - m.b191 - m.x503 + m.x504 == 0)

m.c26 = Constraint(expr=   m.b73 - m.b80 - m.b120 - m.b144 - m.b168 + m.b169 + m.b177 + m.b185 + m.x505 - m.x512 == 0)

m.c27 = Constraint(expr= - m.b73 + m.b74 - m.b113 - m.b137 - m.b161 + m.b170 + m.b178 + m.b186 - m.x505 + m.x506 == 0)

m.c28 = Constraint(expr= - m.b74 + m.b75 - m.b114 - m.b138 - m.b162 + m.b171 + m.b179 + m.b187 - m.x506 + m.x507 == 0)

m.c29 = Constraint(expr= - m.b75 + m.b76 - m.b115 - m.b139 - m.b163 + m.b172 + m.b180 + m.b188 - m.x507 + m.x508 == 0)

m.c30 = Constraint(expr= - m.b76 + m.b77 - m.b116 - m.b140 - m.b164 + m.b173 + m.b181 + m.b189 - m.x508 + m.x509 == 0)

m.c31 = Constraint(expr= - m.b77 + m.b78 - m.b117 - m.b141 - m.b165 + m.b174 + m.b182 + m.b190 - m.x509 + m.x510 == 0)

m.c32 = Constraint(expr= - m.b78 + m.b79 - m.b118 - m.b142 - m.b166 + m.b175 + m.b183 + m.b191 - m.x510 + m.x511 == 0)

m.c33 = Constraint(expr= - m.b79 + m.b80 - m.b119 - m.b143 - m.b167 + m.b176 + m.b184 + m.b192 - m.x511 + m.x512 == 0)

m.c34 = Constraint(expr=   m.b9 - m.b16 + m.b193 + m.b201 + m.b209 - m.b224 - m.b248 - m.b272 + m.x513 - m.x520 == 0)

m.c35 = Constraint(expr= - m.b9 + m.b10 + m.b194 + m.b202 + m.b210 - m.b217 - m.b241 - m.b265 - m.x513 + m.x514 == 0)

m.c36 = Constraint(expr= - m.b10 + m.b11 + m.b195 + m.b203 + m.b211 - m.b218 - m.b242 - m.b266 - m.x514 + m.x515 == 0)

m.c37 = Constraint(expr= - m.b11 + m.b12 + m.b196 + m.b204 + m.b212 - m.b219 - m.b243 - m.b267 - m.x515 + m.x516 == 0)

m.c38 = Constraint(expr= - m.b12 + m.b13 + m.b197 + m.b205 + m.b213 - m.b220 - m.b244 - m.b268 - m.x516 + m.x517 == 0)

m.c39 = Constraint(expr= - m.b13 + m.b14 + m.b198 + m.b206 + m.b214 - m.b221 - m.b245 - m.b269 - m.x517 + m.x518 == 0)

m.c40 = Constraint(expr= - m.b14 + m.b15 + m.b199 + m.b207 + m.b215 - m.b222 - m.b246 - m.b270 - m.x518 + m.x519 == 0)

m.c41 = Constraint(expr= - m.b15 + m.b16 + m.b200 + m.b208 + m.b216 - m.b223 - m.b247 - m.b271 - m.x519 + m.x520 == 0)

m.c42 = Constraint(expr=   m.b33 - m.b40 - m.b200 + m.b217 + m.b225 + m.b233 - m.b256 - m.b280 + m.x521 - m.x528 == 0)

m.c43 = Constraint(expr= - m.b33 + m.b34 - m.b193 + m.b218 + m.b226 + m.b234 - m.b249 - m.b273 - m.x521 + m.x522 == 0)

m.c44 = Constraint(expr= - m.b34 + m.b35 - m.b194 + m.b219 + m.b227 + m.b235 - m.b250 - m.b274 - m.x522 + m.x523 == 0)

m.c45 = Constraint(expr= - m.b35 + m.b36 - m.b195 + m.b220 + m.b228 + m.b236 - m.b251 - m.b275 - m.x523 + m.x524 == 0)

m.c46 = Constraint(expr= - m.b36 + m.b37 - m.b196 + m.b221 + m.b229 + m.b237 - m.b252 - m.b276 - m.x524 + m.x525 == 0)

m.c47 = Constraint(expr= - m.b37 + m.b38 - m.b197 + m.b222 + m.b230 + m.b238 - m.b253 - m.b277 - m.x525 + m.x526 == 0)

m.c48 = Constraint(expr= - m.b38 + m.b39 - m.b198 + m.b223 + m.b231 + m.b239 - m.b254 - m.b278 - m.x526 + m.x527 == 0)

m.c49 = Constraint(expr= - m.b39 + m.b40 - m.b199 + m.b224 + m.b232 + m.b240 - m.b255 - m.b279 - m.x527 + m.x528 == 0)

m.c50 = Constraint(expr=   m.b57 - m.b64 - m.b208 - m.b232 + m.b241 + m.b249 + m.b257 - m.b288 + m.x529 - m.x536 == 0)

m.c51 = Constraint(expr= - m.b57 + m.b58 - m.b201 - m.b225 + m.b242 + m.b250 + m.b258 - m.b281 - m.x529 + m.x530 == 0)

m.c52 = Constraint(expr= - m.b58 + m.b59 - m.b202 - m.b226 + m.b243 + m.b251 + m.b259 - m.b282 - m.x530 + m.x531 == 0)

m.c53 = Constraint(expr= - m.b59 + m.b60 - m.b203 - m.b227 + m.b244 + m.b252 + m.b260 - m.b283 - m.x531 + m.x532 == 0)

m.c54 = Constraint(expr= - m.b60 + m.b61 - m.b204 - m.b228 + m.b245 + m.b253 + m.b261 - m.b284 - m.x532 + m.x533 == 0)

m.c55 = Constraint(expr= - m.b61 + m.b62 - m.b205 - m.b229 + m.b246 + m.b254 + m.b262 - m.b285 - m.x533 + m.x534 == 0)

m.c56 = Constraint(expr= - m.b62 + m.b63 - m.b206 - m.b230 + m.b247 + m.b255 + m.b263 - m.b286 - m.x534 + m.x535 == 0)

m.c57 = Constraint(expr= - m.b63 + m.b64 - m.b207 - m.b231 + m.b248 + m.b256 + m.b264 - m.b287 - m.x535 + m.x536 == 0)

m.c58 = Constraint(expr=   m.b81 - m.b88 - m.b216 - m.b240 - m.b264 + m.b265 + m.b273 + m.b281 + m.x537 - m.x544 == 0)

m.c59 = Constraint(expr= - m.b81 + m.b82 - m.b209 - m.b233 - m.b257 + m.b266 + m.b274 + m.b282 - m.x537 + m.x538 == 0)

m.c60 = Constraint(expr= - m.b82 + m.b83 - m.b210 - m.b234 - m.b258 + m.b267 + m.b275 + m.b283 - m.x538 + m.x539 == 0)

m.c61 = Constraint(expr= - m.b83 + m.b84 - m.b211 - m.b235 - m.b259 + m.b268 + m.b276 + m.b284 - m.x539 + m.x540 == 0)

m.c62 = Constraint(expr= - m.b84 + m.b85 - m.b212 - m.b236 - m.b260 + m.b269 + m.b277 + m.b285 - m.x540 + m.x541 == 0)

m.c63 = Constraint(expr= - m.b85 + m.b86 - m.b213 - m.b237 - m.b261 + m.b270 + m.b278 + m.b286 - m.x541 + m.x542 == 0)

m.c64 = Constraint(expr= - m.b86 + m.b87 - m.b214 - m.b238 - m.b262 + m.b271 + m.b279 + m.b287 - m.x542 + m.x543 == 0)

m.c65 = Constraint(expr= - m.b87 + m.b88 - m.b215 - m.b239 - m.b263 + m.b272 + m.b280 + m.b288 - m.x543 + m.x544 == 0)

m.c66 = Constraint(expr=   m.b17 - m.b24 + m.b289 + m.b297 + m.b305 - m.b320 - m.b344 - m.b368 + m.x545 - m.x552 == 0)

m.c67 = Constraint(expr= - m.b17 + m.b18 + m.b290 + m.b298 + m.b306 - m.b313 - m.b337 - m.b361 - m.x545 + m.x546 == 0)

m.c68 = Constraint(expr= - m.b18 + m.b19 + m.b291 + m.b299 + m.b307 - m.b314 - m.b338 - m.b362 - m.x546 + m.x547 == 0)

m.c69 = Constraint(expr= - m.b19 + m.b20 + m.b292 + m.b300 + m.b308 - m.b315 - m.b339 - m.b363 - m.x547 + m.x548 == 0)

m.c70 = Constraint(expr= - m.b20 + m.b21 + m.b293 + m.b301 + m.b309 - m.b316 - m.b340 - m.b364 - m.x548 + m.x549 == 0)

m.c71 = Constraint(expr= - m.b21 + m.b22 + m.b294 + m.b302 + m.b310 - m.b317 - m.b341 - m.b365 - m.x549 + m.x550 == 0)

m.c72 = Constraint(expr= - m.b22 + m.b23 + m.b295 + m.b303 + m.b311 - m.b318 - m.b342 - m.b366 - m.x550 + m.x551 == 0)

m.c73 = Constraint(expr= - m.b23 + m.b24 + m.b296 + m.b304 + m.b312 - m.b319 - m.b343 - m.b367 - m.x551 + m.x552 == 0)

m.c74 = Constraint(expr=   m.b41 - m.b48 - m.b296 + m.b313 + m.b321 + m.b329 - m.b352 - m.b376 + m.x553 - m.x560 == 0)

m.c75 = Constraint(expr= - m.b41 + m.b42 - m.b289 + m.b314 + m.b322 + m.b330 - m.b345 - m.b369 - m.x553 + m.x554 == 0)

m.c76 = Constraint(expr= - m.b42 + m.b43 - m.b290 + m.b315 + m.b323 + m.b331 - m.b346 - m.b370 - m.x554 + m.x555 == 0)

m.c77 = Constraint(expr= - m.b43 + m.b44 - m.b291 + m.b316 + m.b324 + m.b332 - m.b347 - m.b371 - m.x555 + m.x556 == 0)

m.c78 = Constraint(expr= - m.b44 + m.b45 - m.b292 + m.b317 + m.b325 + m.b333 - m.b348 - m.b372 - m.x556 + m.x557 == 0)

m.c79 = Constraint(expr= - m.b45 + m.b46 - m.b293 + m.b318 + m.b326 + m.b334 - m.b349 - m.b373 - m.x557 + m.x558 == 0)

m.c80 = Constraint(expr= - m.b46 + m.b47 - m.b294 + m.b319 + m.b327 + m.b335 - m.b350 - m.b374 - m.x558 + m.x559 == 0)

m.c81 = Constraint(expr= - m.b47 + m.b48 - m.b295 + m.b320 + m.b328 + m.b336 - m.b351 - m.b375 - m.x559 + m.x560 == 0)

m.c82 = Constraint(expr=   m.b65 - m.b72 - m.b304 - m.b328 + m.b337 + m.b345 + m.b353 - m.b384 + m.x561 - m.x568 == 0)

m.c83 = Constraint(expr= - m.b65 + m.b66 - m.b297 - m.b321 + m.b338 + m.b346 + m.b354 - m.b377 - m.x561 + m.x562 == 0)

m.c84 = Constraint(expr= - m.b66 + m.b67 - m.b298 - m.b322 + m.b339 + m.b347 + m.b355 - m.b378 - m.x562 + m.x563 == 0)

m.c85 = Constraint(expr= - m.b67 + m.b68 - m.b299 - m.b323 + m.b340 + m.b348 + m.b356 - m.b379 - m.x563 + m.x564 == 0)

m.c86 = Constraint(expr= - m.b68 + m.b69 - m.b300 - m.b324 + m.b341 + m.b349 + m.b357 - m.b380 - m.x564 + m.x565 == 0)

m.c87 = Constraint(expr= - m.b69 + m.b70 - m.b301 - m.b325 + m.b342 + m.b350 + m.b358 - m.b381 - m.x565 + m.x566 == 0)

m.c88 = Constraint(expr= - m.b70 + m.b71 - m.b302 - m.b326 + m.b343 + m.b351 + m.b359 - m.b382 - m.x566 + m.x567 == 0)

m.c89 = Constraint(expr= - m.b71 + m.b72 - m.b303 - m.b327 + m.b344 + m.b352 + m.b360 - m.b383 - m.x567 + m.x568 == 0)

m.c90 = Constraint(expr=   m.b89 - m.b96 - m.b312 - m.b336 - m.b360 + m.b361 + m.b369 + m.b377 + m.x569 - m.x576 == 0)

m.c91 = Constraint(expr= - m.b89 + m.b90 - m.b305 - m.b329 - m.b353 + m.b362 + m.b370 + m.b378 - m.x569 + m.x570 == 0)

m.c92 = Constraint(expr= - m.b90 + m.b91 - m.b306 - m.b330 - m.b354 + m.b363 + m.b371 + m.b379 - m.x570 + m.x571 == 0)

m.c93 = Constraint(expr= - m.b91 + m.b92 - m.b307 - m.b331 - m.b355 + m.b364 + m.b372 + m.b380 - m.x571 + m.x572 == 0)

m.c94 = Constraint(expr= - m.b92 + m.b93 - m.b308 - m.b332 - m.b356 + m.b365 + m.b373 + m.b381 - m.x572 + m.x573 == 0)

m.c95 = Constraint(expr= - m.b93 + m.b94 - m.b309 - m.b333 - m.b357 + m.b366 + m.b374 + m.b382 - m.x573 + m.x574 == 0)

m.c96 = Constraint(expr= - m.b94 + m.b95 - m.b310 - m.b334 - m.b358 + m.b367 + m.b375 + m.b383 - m.x574 + m.x575 == 0)

m.c97 = Constraint(expr= - m.b95 + m.b96 - m.b311 - m.b335 - m.b359 + m.b368 + m.b376 + m.b384 - m.x575 + m.x576 == 0)

m.c98 = Constraint(expr= - m.x392 + m.x400 + m.x577 - m.x584 == 0)

m.c99 = Constraint(expr= - m.x385 + m.x393 - m.x577 + m.x578 == 0)

m.c100 = Constraint(expr= - m.x386 + m.x394 - m.x578 + m.x579 == 0)

m.c101 = Constraint(expr= - m.x387 + m.x395 - m.x579 + m.x580 == 0)

m.c102 = Constraint(expr= - m.x388 + m.x396 - m.x580 + m.x581 == 0)

m.c103 = Constraint(expr= - m.x389 + m.x397 - m.x581 + m.x582 == 0)

m.c104 = Constraint(expr= - m.x390 + m.x398 - m.x582 + m.x583 == 0)

m.c105 = Constraint(expr= - m.x391 + m.x399 - m.x583 + m.x584 == 0)

m.c106 = Constraint(expr= - m.x400 + m.x408 + m.x585 - m.x592 == 0)

m.c107 = Constraint(expr= - m.x393 + m.x401 - m.x585 + m.x586 == 0)

m.c108 = Constraint(expr= - m.x394 + m.x402 - m.x586 + m.x587 == 0)

m.c109 = Constraint(expr= - m.x395 + m.x403 - m.x587 + m.x588 == 0)

m.c110 = Constraint(expr= - m.x396 + m.x404 - m.x588 + m.x589 == 0)

m.c111 = Constraint(expr= - m.x397 + m.x405 - m.x589 + m.x590 == 0)

m.c112 = Constraint(expr= - m.x398 + m.x406 - m.x590 + m.x591 == 0)

m.c113 = Constraint(expr= - m.x399 + m.x407 - m.x591 + m.x592 == 0)

m.c114 = Constraint(expr=m.x673/m.x693*(m.x693 - m.x684) - m.x408 + m.x593 - m.x600 == 0)

m.c115 = Constraint(expr=m.x673/m.x693*(m.x678 - m.x677) - m.x401 - m.x593 + m.x594 == 0)

m.c116 = Constraint(expr=m.x673/m.x693*(m.x679 - m.x678) - m.x402 - m.x594 + m.x595 == 0)

m.c117 = Constraint(expr=m.x673/m.x693*(m.x680 - m.x679) - m.x403 - m.x595 + m.x596 == 0)

m.c118 = Constraint(expr=m.x673/m.x693*(m.x681 - m.x680) - m.x404 - m.x596 + m.x597 == 0)

m.c119 = Constraint(expr=m.x673/m.x693*(m.x682 - m.x681) - m.x405 - m.x597 + m.x598 == 0)

m.c120 = Constraint(expr=m.x673/m.x693*(m.x683 - m.x682) - m.x406 - m.x598 + m.x599 == 0)

m.c121 = Constraint(expr=m.x673/m.x693*(m.x684 - m.x683) - m.x407 - m.x599 + m.x600 == 0)

m.c122 = Constraint(expr= - m.x416 + m.x424 + m.x601 - m.x608 == 0)

m.c123 = Constraint(expr= - m.x409 + m.x417 - m.x601 + m.x602 == 0)

m.c124 = Constraint(expr= - m.x410 + m.x418 - m.x602 + m.x603 == 0)

m.c125 = Constraint(expr= - m.x411 + m.x419 - m.x603 + m.x604 == 0)

m.c126 = Constraint(expr= - m.x412 + m.x420 - m.x604 + m.x605 == 0)

m.c127 = Constraint(expr= - m.x413 + m.x421 - m.x605 + m.x606 == 0)

m.c128 = Constraint(expr= - m.x414 + m.x422 - m.x606 + m.x607 == 0)

m.c129 = Constraint(expr= - m.x415 + m.x423 - m.x607 + m.x608 == 0)

m.c130 = Constraint(expr= - m.x424 + m.x432 + m.x609 - m.x616 == 0)

m.c131 = Constraint(expr= - m.x417 + m.x425 - m.x609 + m.x610 == 0)

m.c132 = Constraint(expr= - m.x418 + m.x426 - m.x610 + m.x611 == 0)

m.c133 = Constraint(expr= - m.x419 + m.x427 - m.x611 + m.x612 == 0)

m.c134 = Constraint(expr= - m.x420 + m.x428 - m.x612 + m.x613 == 0)

m.c135 = Constraint(expr= - m.x421 + m.x429 - m.x613 + m.x614 == 0)

m.c136 = Constraint(expr= - m.x422 + m.x430 - m.x614 + m.x615 == 0)

m.c137 = Constraint(expr= - m.x423 + m.x431 - m.x615 + m.x616 == 0)

m.c138 = Constraint(expr=m.x674/m.x693*(m.x693 - m.x684) - m.x432 + m.x617 - m.x624 == 0)

m.c139 = Constraint(expr=m.x674/m.x693*(m.x678 - m.x677) - m.x425 - m.x617 + m.x618 == 0)

m.c140 = Constraint(expr=m.x674/m.x693*(m.x679 - m.x678) - m.x426 - m.x618 + m.x619 == 0)

m.c141 = Constraint(expr=m.x674/m.x693*(m.x680 - m.x679) - m.x427 - m.x619 + m.x620 == 0)

m.c142 = Constraint(expr=m.x674/m.x693*(m.x681 - m.x680) - m.x428 - m.x620 + m.x621 == 0)

m.c143 = Constraint(expr=m.x674/m.x693*(m.x682 - m.x681) - m.x429 - m.x621 + m.x622 == 0)

m.c144 = Constraint(expr=m.x674/m.x693*(m.x683 - m.x682) - m.x430 - m.x622 + m.x623 == 0)

m.c145 = Constraint(expr=m.x674/m.x693*(m.x684 - m.x683) - m.x431 - m.x623 + m.x624 == 0)

m.c146 = Constraint(expr= - m.x440 + m.x448 + m.x625 - m.x632 == 0)

m.c147 = Constraint(expr= - m.x433 + m.x441 - m.x625 + m.x626 == 0)

m.c148 = Constraint(expr= - m.x434 + m.x442 - m.x626 + m.x627 == 0)

m.c149 = Constraint(expr= - m.x435 + m.x443 - m.x627 + m.x628 == 0)

m.c150 = Constraint(expr= - m.x436 + m.x444 - m.x628 + m.x629 == 0)

m.c151 = Constraint(expr= - m.x437 + m.x445 - m.x629 + m.x630 == 0)

m.c152 = Constraint(expr= - m.x438 + m.x446 - m.x630 + m.x631 == 0)

m.c153 = Constraint(expr= - m.x439 + m.x447 - m.x631 + m.x632 == 0)

m.c154 = Constraint(expr= - m.x448 + m.x456 + m.x633 - m.x640 == 0)

m.c155 = Constraint(expr= - m.x441 + m.x449 - m.x633 + m.x634 == 0)

m.c156 = Constraint(expr= - m.x442 + m.x450 - m.x634 + m.x635 == 0)

m.c157 = Constraint(expr= - m.x443 + m.x451 - m.x635 + m.x636 == 0)

m.c158 = Constraint(expr= - m.x444 + m.x452 - m.x636 + m.x637 == 0)

m.c159 = Constraint(expr= - m.x445 + m.x453 - m.x637 + m.x638 == 0)

m.c160 = Constraint(expr= - m.x446 + m.x454 - m.x638 + m.x639 == 0)

m.c161 = Constraint(expr= - m.x447 + m.x455 - m.x639 + m.x640 == 0)

m.c162 = Constraint(expr=m.x675/m.x693*(m.x693 - m.x684) - m.x456 + m.x641 - m.x648 == 0)

m.c163 = Constraint(expr=m.x675/m.x693*(m.x678 - m.x677) - m.x449 - m.x641 + m.x642 == 0)

m.c164 = Constraint(expr=m.x675/m.x693*(m.x679 - m.x678) - m.x450 - m.x642 + m.x643 == 0)

m.c165 = Constraint(expr=m.x675/m.x693*(m.x680 - m.x679) - m.x451 - m.x643 + m.x644 == 0)

m.c166 = Constraint(expr=m.x675/m.x693*(m.x681 - m.x680) - m.x452 - m.x644 + m.x645 == 0)

m.c167 = Constraint(expr=m.x675/m.x693*(m.x682 - m.x681) - m.x453 - m.x645 + m.x646 == 0)

m.c168 = Constraint(expr=m.x675/m.x693*(m.x683 - m.x682) - m.x454 - m.x646 + m.x647 == 0)

m.c169 = Constraint(expr=m.x675/m.x693*(m.x684 - m.x683) - m.x455 - m.x647 + m.x648 == 0)

m.c170 = Constraint(expr= - m.x464 + m.x472 + m.x649 - m.x656 == 0)

m.c171 = Constraint(expr= - m.x457 + m.x465 - m.x649 + m.x650 == 0)

m.c172 = Constraint(expr= - m.x458 + m.x466 - m.x650 + m.x651 == 0)

m.c173 = Constraint(expr= - m.x459 + m.x467 - m.x651 + m.x652 == 0)

m.c174 = Constraint(expr= - m.x460 + m.x468 - m.x652 + m.x653 == 0)

m.c175 = Constraint(expr= - m.x461 + m.x469 - m.x653 + m.x654 == 0)

m.c176 = Constraint(expr= - m.x462 + m.x470 - m.x654 + m.x655 == 0)

m.c177 = Constraint(expr= - m.x463 + m.x471 - m.x655 + m.x656 == 0)

m.c178 = Constraint(expr= - m.x472 + m.x480 + m.x657 - m.x664 == 0)

m.c179 = Constraint(expr= - m.x465 + m.x473 - m.x657 + m.x658 == 0)

m.c180 = Constraint(expr= - m.x466 + m.x474 - m.x658 + m.x659 == 0)

m.c181 = Constraint(expr= - m.x467 + m.x475 - m.x659 + m.x660 == 0)

m.c182 = Constraint(expr= - m.x468 + m.x476 - m.x660 + m.x661 == 0)

m.c183 = Constraint(expr= - m.x469 + m.x477 - m.x661 + m.x662 == 0)

m.c184 = Constraint(expr= - m.x470 + m.x478 - m.x662 + m.x663 == 0)

m.c185 = Constraint(expr= - m.x471 + m.x479 - m.x663 + m.x664 == 0)

m.c186 = Constraint(expr=m.x676/m.x693*(m.x693 - m.x684) - m.x480 + m.x665 - m.x672 == 0)

m.c187 = Constraint(expr=m.x676/m.x693*(m.x678 - m.x677) - m.x473 - m.x665 + m.x666 == 0)

m.c188 = Constraint(expr=m.x676/m.x693*(m.x679 - m.x678) - m.x474 - m.x666 + m.x667 == 0)

m.c189 = Constraint(expr=m.x676/m.x693*(m.x680 - m.x679) - m.x475 - m.x667 + m.x668 == 0)

m.c190 = Constraint(expr=m.x676/m.x693*(m.x681 - m.x680) - m.x476 - m.x668 + m.x669 == 0)

m.c191 = Constraint(expr=m.x676/m.x693*(m.x682 - m.x681) - m.x477 - m.x669 + m.x670 == 0)

m.c192 = Constraint(expr=m.x676/m.x693*(m.x683 - m.x682) - m.x478 - m.x670 + m.x671 == 0)

m.c193 = Constraint(expr=m.x676/m.x693*(m.x684 - m.x683) - m.x479 - m.x671 + m.x672 == 0)

m.c194 = Constraint(expr=   m.b1 + m.b25 + m.b49 + m.b73 + m.b97 + m.b105 + m.b113 + m.b121 + m.b129 + m.b137 + m.b145
                          + m.b153 + m.b161 + m.b169 + m.b177 + m.b185 + m.x481 + m.x489 + m.x497 + m.x505 == 1)

m.c195 = Constraint(expr=   m.b9 + m.b33 + m.b57 + m.b81 + m.b193 + m.b201 + m.b209 + m.b217 + m.b225 + m.b233 + m.b241
                          + m.b249 + m.b257 + m.b265 + m.b273 + m.b281 + m.x513 + m.x521 + m.x529 + m.x537 == 1)

m.c196 = Constraint(expr=   m.b17 + m.b41 + m.b65 + m.b89 + m.b289 + m.b297 + m.b305 + m.b313 + m.b321 + m.b329 + m.b337
                          + m.b345 + m.b353 + m.b361 + m.b369 + m.b377 + m.x545 + m.x553 + m.x561 + m.x569 == 1)

m.c197 = Constraint(expr= - 10*m.b97 - 10*m.b105 - 10*m.b113 - 10*m.b121 - m.b129 - 4*m.b137 - 10*m.b145 - m.b153
                          - 4*m.b161 - 10*m.b169 - 4*m.b177 - 4*m.b185 - 0.000854700854700855*m.x385
                          - 0.000746268656716418*m.x409 - 0.000746268656716418*m.x433 - 0.000826446280991736*m.x457
                          - m.x677 + m.x678 >= 0)

m.c198 = Constraint(expr= - 10*m.b98 - 10*m.b106 - 10*m.b114 - 10*m.b122 - m.b130 - 4*m.b138 - 10*m.b146 - m.b154
                          - 4*m.b162 - 10*m.b170 - 4*m.b178 - 4*m.b186 - 0.000854700854700855*m.x386
                          - 0.000746268656716418*m.x410 - 0.000746268656716418*m.x434 - 0.000826446280991736*m.x458
                          - m.x678 + m.x679 >= 0)

m.c199 = Constraint(expr= - 10*m.b99 - 10*m.b107 - 10*m.b115 - 10*m.b123 - m.b131 - 4*m.b139 - 10*m.b147 - m.b155
                          - 4*m.b163 - 10*m.b171 - 4*m.b179 - 4*m.b187 - 0.000854700854700855*m.x387
                          - 0.000746268656716418*m.x411 - 0.000746268656716418*m.x435 - 0.000826446280991736*m.x459
                          - m.x679 + m.x680 >= 0)

m.c200 = Constraint(expr= - 10*m.b100 - 10*m.b108 - 10*m.b116 - 10*m.b124 - m.b132 - 4*m.b140 - 10*m.b148 - m.b156
                          - 4*m.b164 - 10*m.b172 - 4*m.b180 - 4*m.b188 - 0.000854700854700855*m.x388
                          - 0.000746268656716418*m.x412 - 0.000746268656716418*m.x436 - 0.000826446280991736*m.x460
                          - m.x680 + m.x681 >= 0)

m.c201 = Constraint(expr= - 10*m.b101 - 10*m.b109 - 10*m.b117 - 10*m.b125 - m.b133 - 4*m.b141 - 10*m.b149 - m.b157
                          - 4*m.b165 - 10*m.b173 - 4*m.b181 - 4*m.b189 - 0.000854700854700855*m.x389
                          - 0.000746268656716418*m.x413 - 0.000746268656716418*m.x437 - 0.000826446280991736*m.x461
                          - m.x681 + m.x682 >= 0)

m.c202 = Constraint(expr= - 10*m.b102 - 10*m.b110 - 10*m.b118 - 10*m.b126 - m.b134 - 4*m.b142 - 10*m.b150 - m.b158
                          - 4*m.b166 - 10*m.b174 - 4*m.b182 - 4*m.b190 - 0.000854700854700855*m.x390
                          - 0.000746268656716418*m.x414 - 0.000746268656716418*m.x438 - 0.000826446280991736*m.x462
                          - m.x682 + m.x683 >= 0)

m.c203 = Constraint(expr= - 10*m.b103 - 10*m.b111 - 10*m.b119 - 10*m.b127 - m.b135 - 4*m.b143 - 10*m.b151 - m.b159
                          - 4*m.b167 - 10*m.b175 - 4*m.b183 - 4*m.b191 - 0.000854700854700855*m.x391
                          - 0.000746268656716418*m.x415 - 0.000746268656716418*m.x439 - 0.000826446280991736*m.x463
                          - m.x683 + m.x684 >= 0)

m.c204 = Constraint(expr= - 10*m.b104 - 10*m.b112 - 10*m.b120 - 10*m.b128 - m.b136 - 4*m.b144 - 10*m.b152 - m.b160
                          - 4*m.b168 - 10*m.b176 - 4*m.b184 - 4*m.b192 - 0.000854700854700855*m.x392
                          - 0.000746268656716418*m.x416 - 0.000746268656716418*m.x440 - 0.000826446280991736*m.x464
                          - m.x684 + m.x693 >= 0)

m.c205 = Constraint(expr= - 3*m.b193 - 3*m.b201 - 12*m.b209 - 3*m.b217 - m.b225 - 12*m.b233 - 3*m.b241 - m.b249
                          - 12*m.b257 - 12*m.b265 - 12*m.b273 - 12*m.b281 - 0.000892857142857143*m.x393
                          - 0.000775193798449612*m.x417 - 0.000746268656716418*m.x441 - 0.000862068965517241*m.x465
                          - m.x677 + m.x678 >= 0)

m.c206 = Constraint(expr= - 3*m.b194 - 3*m.b202 - 12*m.b210 - 3*m.b218 - m.b226 - 12*m.b234 - 3*m.b242 - m.b250
                          - 12*m.b258 - 12*m.b266 - 12*m.b274 - 12*m.b282 - 0.000892857142857143*m.x394
                          - 0.000775193798449612*m.x418 - 0.000746268656716418*m.x442 - 0.000862068965517241*m.x466
                          - m.x678 + m.x679 >= 0)

m.c207 = Constraint(expr= - 3*m.b195 - 3*m.b203 - 12*m.b211 - 3*m.b219 - m.b227 - 12*m.b235 - 3*m.b243 - m.b251
                          - 12*m.b259 - 12*m.b267 - 12*m.b275 - 12*m.b283 - 0.000892857142857143*m.x395
                          - 0.000775193798449612*m.x419 - 0.000746268656716418*m.x443 - 0.000862068965517241*m.x467
                          - m.x679 + m.x680 >= 0)

m.c208 = Constraint(expr= - 3*m.b196 - 3*m.b204 - 12*m.b212 - 3*m.b220 - m.b228 - 12*m.b236 - 3*m.b244 - m.b252
                          - 12*m.b260 - 12*m.b268 - 12*m.b276 - 12*m.b284 - 0.000892857142857143*m.x396
                          - 0.000775193798449612*m.x420 - 0.000746268656716418*m.x444 - 0.000862068965517241*m.x468
                          - m.x680 + m.x681 >= 0)

m.c209 = Constraint(expr= - 3*m.b197 - 3*m.b205 - 12*m.b213 - 3*m.b221 - m.b229 - 12*m.b237 - 3*m.b245 - m.b253
                          - 12*m.b261 - 12*m.b269 - 12*m.b277 - 12*m.b285 - 0.000892857142857143*m.x397
                          - 0.000775193798449612*m.x421 - 0.000746268656716418*m.x445 - 0.000862068965517241*m.x469
                          - m.x681 + m.x682 >= 0)

m.c210 = Constraint(expr= - 3*m.b198 - 3*m.b206 - 12*m.b214 - 3*m.b222 - m.b230 - 12*m.b238 - 3*m.b246 - m.b254
                          - 12*m.b262 - 12*m.b270 - 12*m.b278 - 12*m.b286 - 0.000892857142857143*m.x398
                          - 0.000775193798449612*m.x422 - 0.000746268656716418*m.x446 - 0.000862068965517241*m.x470
                          - m.x682 + m.x683 >= 0)

m.c211 = Constraint(expr= - 3*m.b199 - 3*m.b207 - 12*m.b215 - 3*m.b223 - m.b231 - 12*m.b239 - 3*m.b247 - m.b255
                          - 12*m.b263 - 12*m.b271 - 12*m.b279 - 12*m.b287 - 0.000892857142857143*m.x399
                          - 0.000775193798449612*m.x423 - 0.000746268656716418*m.x447 - 0.000862068965517241*m.x471
                          - m.x683 + m.x684 >= 0)

m.c212 = Constraint(expr= - 3*m.b200 - 3*m.b208 - 12*m.b216 - 3*m.b224 - m.b232 - 12*m.b240 - 3*m.b248 - m.b256
                          - 12*m.b264 - 12*m.b272 - 12*m.b280 - 12*m.b288 - 0.000892857142857143*m.x400
                          - 0.000775193798449612*m.x424 - 0.000746268656716418*m.x448 - 0.000862068965517241*m.x472
                          - m.x684 + m.x693 >= 0)

m.c213 = Constraint(expr= - 2*m.b289 - 2*m.b297 - 8*m.b305 - 2*m.b313 - m.b321 - 8*m.b329 - 2*m.b337 - m.b345 - 8*m.b353
                          - 8*m.b361 - 8*m.b369 - 8*m.b377 - 0.000892857142857143*m.x401 - 0.000537634408602151*m.x425
                          - 0.000746268656716418*m.x449 - 0.000704225352112676*m.x473 - m.x677 + m.x678 >= 0)

m.c214 = Constraint(expr= - 2*m.b290 - 2*m.b298 - 8*m.b306 - 2*m.b314 - m.b322 - 8*m.b330 - 2*m.b338 - m.b346 - 8*m.b354
                          - 8*m.b362 - 8*m.b370 - 8*m.b378 - 0.000892857142857143*m.x402 - 0.000537634408602151*m.x426
                          - 0.000746268656716418*m.x450 - 0.000704225352112676*m.x474 - m.x678 + m.x679 >= 0)

m.c215 = Constraint(expr= - 2*m.b291 - 2*m.b299 - 8*m.b307 - 2*m.b315 - m.b323 - 8*m.b331 - 2*m.b339 - m.b347 - 8*m.b355
                          - 8*m.b363 - 8*m.b371 - 8*m.b379 - 0.000892857142857143*m.x403 - 0.000537634408602151*m.x427
                          - 0.000746268656716418*m.x451 - 0.000704225352112676*m.x475 - m.x679 + m.x680 >= 0)

m.c216 = Constraint(expr= - 2*m.b292 - 2*m.b300 - 8*m.b308 - 2*m.b316 - m.b324 - 8*m.b332 - 2*m.b340 - m.b348 - 8*m.b356
                          - 8*m.b364 - 8*m.b372 - 8*m.b380 - 0.000892857142857143*m.x404 - 0.000537634408602151*m.x428
                          - 0.000746268656716418*m.x452 - 0.000704225352112676*m.x476 - m.x680 + m.x681 >= 0)

m.c217 = Constraint(expr= - 2*m.b293 - 2*m.b301 - 8*m.b309 - 2*m.b317 - m.b325 - 8*m.b333 - 2*m.b341 - m.b349 - 8*m.b357
                          - 8*m.b365 - 8*m.b373 - 8*m.b381 - 0.000892857142857143*m.x405 - 0.000537634408602151*m.x429
                          - 0.000746268656716418*m.x453 - 0.000704225352112676*m.x477 - m.x681 + m.x682 >= 0)

m.c218 = Constraint(expr= - 2*m.b294 - 2*m.b302 - 8*m.b310 - 2*m.b318 - m.b326 - 8*m.b334 - 2*m.b342 - m.b350 - 8*m.b358
                          - 8*m.b366 - 8*m.b374 - 8*m.b382 - 0.000892857142857143*m.x406 - 0.000537634408602151*m.x430
                          - 0.000746268656716418*m.x454 - 0.000704225352112676*m.x478 - m.x682 + m.x683 >= 0)

m.c219 = Constraint(expr= - 2*m.b295 - 2*m.b303 - 8*m.b311 - 2*m.b319 - m.b327 - 8*m.b335 - 2*m.b343 - m.b351 - 8*m.b359
                          - 8*m.b367 - 8*m.b375 - 8*m.b383 - 0.000892857142857143*m.x407 - 0.000537634408602151*m.x431
                          - 0.000746268656716418*m.x455 - 0.000704225352112676*m.x479 - m.x683 + m.x684 >= 0)

m.c220 = Constraint(expr= - 2*m.b296 - 2*m.b304 - 8*m.b312 - 2*m.b320 - m.b328 - 8*m.b336 - 2*m.b344 - m.b352 - 8*m.b360
                          - 8*m.b368 - 8*m.b376 - 8*m.b384 - 0.000892857142857143*m.x408 - 0.000537634408602151*m.x432
                          - 0.000746268656716418*m.x456 - 0.000704225352112676*m.x480 - m.x684 + m.x693 >= 0)

m.c221 = Constraint(expr= - 702000*m.b1 + m.x385 <= 0)

m.c222 = Constraint(expr= - 702000*m.b2 + m.x386 <= 0)

m.c223 = Constraint(expr= - 702000*m.b3 + m.x387 <= 0)

m.c224 = Constraint(expr= - 702000*m.b4 + m.x388 <= 0)

m.c225 = Constraint(expr= - 702000*m.b5 + m.x389 <= 0)

m.c226 = Constraint(expr= - 702000*m.b6 + m.x390 <= 0)

m.c227 = Constraint(expr= - 702000*m.b7 + m.x391 <= 0)

m.c228 = Constraint(expr= - 702000*m.b8 + m.x392 <= 0)

m.c229 = Constraint(expr= - 672000*m.b9 + m.x393 <= 0)

m.c230 = Constraint(expr= - 672000*m.b10 + m.x394 <= 0)

m.c231 = Constraint(expr= - 672000*m.b11 + m.x395 <= 0)

m.c232 = Constraint(expr= - 672000*m.b12 + m.x396 <= 0)

m.c233 = Constraint(expr= - 672000*m.b13 + m.x397 <= 0)

m.c234 = Constraint(expr= - 672000*m.b14 + m.x398 <= 0)

m.c235 = Constraint(expr= - 672000*m.b15 + m.x399 <= 0)

m.c236 = Constraint(expr= - 672000*m.b16 + m.x400 <= 0)

m.c237 = Constraint(expr= - 672000*m.b17 + m.x401 <= 0)

m.c238 = Constraint(expr= - 672000*m.b18 + m.x402 <= 0)

m.c239 = Constraint(expr= - 672000*m.b19 + m.x403 <= 0)

m.c240 = Constraint(expr= - 672000*m.b20 + m.x404 <= 0)

m.c241 = Constraint(expr= - 672000*m.b21 + m.x405 <= 0)

m.c242 = Constraint(expr= - 672000*m.b22 + m.x406 <= 0)

m.c243 = Constraint(expr= - 672000*m.b23 + m.x407 <= 0)

m.c244 = Constraint(expr= - 672000*m.b24 + m.x408 <= 0)

m.c245 = Constraint(expr= - 804000*m.b25 + m.x409 <= 0)

m.c246 = Constraint(expr= - 804000*m.b26 + m.x410 <= 0)

m.c247 = Constraint(expr= - 804000*m.b27 + m.x411 <= 0)

m.c248 = Constraint(expr= - 804000*m.b28 + m.x412 <= 0)

m.c249 = Constraint(expr= - 804000*m.b29 + m.x413 <= 0)

m.c250 = Constraint(expr= - 804000*m.b30 + m.x414 <= 0)

m.c251 = Constraint(expr= - 804000*m.b31 + m.x415 <= 0)

m.c252 = Constraint(expr= - 804000*m.b32 + m.x416 <= 0)

m.c253 = Constraint(expr= - 774000*m.b33 + m.x417 <= 0)

m.c254 = Constraint(expr= - 774000*m.b34 + m.x418 <= 0)

m.c255 = Constraint(expr= - 774000*m.b35 + m.x419 <= 0)

m.c256 = Constraint(expr= - 774000*m.b36 + m.x420 <= 0)

m.c257 = Constraint(expr= - 774000*m.b37 + m.x421 <= 0)

m.c258 = Constraint(expr= - 774000*m.b38 + m.x422 <= 0)

m.c259 = Constraint(expr= - 774000*m.b39 + m.x423 <= 0)

m.c260 = Constraint(expr= - 774000*m.b40 + m.x424 <= 0)

m.c261 = Constraint(expr= - 1116000*m.b41 + m.x425 <= 0)

m.c262 = Constraint(expr= - 1116000*m.b42 + m.x426 <= 0)

m.c263 = Constraint(expr= - 1116000*m.b43 + m.x427 <= 0)

m.c264 = Constraint(expr= - 1116000*m.b44 + m.x428 <= 0)

m.c265 = Constraint(expr= - 1116000*m.b45 + m.x429 <= 0)

m.c266 = Constraint(expr= - 1116000*m.b46 + m.x430 <= 0)

m.c267 = Constraint(expr= - 1116000*m.b47 + m.x431 <= 0)

m.c268 = Constraint(expr= - 1116000*m.b48 + m.x432 <= 0)

m.c269 = Constraint(expr= - 804000*m.b49 + m.x433 <= 0)

m.c270 = Constraint(expr= - 804000*m.b50 + m.x434 <= 0)

m.c271 = Constraint(expr= - 804000*m.b51 + m.x435 <= 0)

m.c272 = Constraint(expr= - 804000*m.b52 + m.x436 <= 0)

m.c273 = Constraint(expr= - 804000*m.b53 + m.x437 <= 0)

m.c274 = Constraint(expr= - 804000*m.b54 + m.x438 <= 0)

m.c275 = Constraint(expr= - 804000*m.b55 + m.x439 <= 0)

m.c276 = Constraint(expr= - 804000*m.b56 + m.x440 <= 0)

m.c277 = Constraint(expr= - 804000*m.b57 + m.x441 <= 0)

m.c278 = Constraint(expr= - 804000*m.b58 + m.x442 <= 0)

m.c279 = Constraint(expr= - 804000*m.b59 + m.x443 <= 0)

m.c280 = Constraint(expr= - 804000*m.b60 + m.x444 <= 0)

m.c281 = Constraint(expr= - 804000*m.b61 + m.x445 <= 0)

m.c282 = Constraint(expr= - 804000*m.b62 + m.x446 <= 0)

m.c283 = Constraint(expr= - 804000*m.b63 + m.x447 <= 0)

m.c284 = Constraint(expr= - 804000*m.b64 + m.x448 <= 0)

m.c285 = Constraint(expr= - 804000*m.b65 + m.x449 <= 0)

m.c286 = Constraint(expr= - 804000*m.b66 + m.x450 <= 0)

m.c287 = Constraint(expr= - 804000*m.b67 + m.x451 <= 0)

m.c288 = Constraint(expr= - 804000*m.b68 + m.x452 <= 0)

m.c289 = Constraint(expr= - 804000*m.b69 + m.x453 <= 0)

m.c290 = Constraint(expr= - 804000*m.b70 + m.x454 <= 0)

m.c291 = Constraint(expr= - 804000*m.b71 + m.x455 <= 0)

m.c292 = Constraint(expr= - 804000*m.b72 + m.x456 <= 0)

m.c293 = Constraint(expr= - 726000*m.b73 + m.x457 <= 0)

m.c294 = Constraint(expr= - 726000*m.b74 + m.x458 <= 0)

m.c295 = Constraint(expr= - 726000*m.b75 + m.x459 <= 0)

m.c296 = Constraint(expr= - 726000*m.b76 + m.x460 <= 0)

m.c297 = Constraint(expr= - 726000*m.b77 + m.x461 <= 0)

m.c298 = Constraint(expr= - 726000*m.b78 + m.x462 <= 0)

m.c299 = Constraint(expr= - 726000*m.b79 + m.x463 <= 0)

m.c300 = Constraint(expr= - 726000*m.b80 + m.x464 <= 0)

m.c301 = Constraint(expr= - 696000*m.b81 + m.x465 <= 0)

m.c302 = Constraint(expr= - 696000*m.b82 + m.x466 <= 0)

m.c303 = Constraint(expr= - 696000*m.b83 + m.x467 <= 0)

m.c304 = Constraint(expr= - 696000*m.b84 + m.x468 <= 0)

m.c305 = Constraint(expr= - 696000*m.b85 + m.x469 <= 0)

m.c306 = Constraint(expr= - 696000*m.b86 + m.x470 <= 0)

m.c307 = Constraint(expr= - 696000*m.b87 + m.x471 <= 0)

m.c308 = Constraint(expr= - 696000*m.b88 + m.x472 <= 0)

m.c309 = Constraint(expr= - 852000*m.b89 + m.x473 <= 0)

m.c310 = Constraint(expr= - 852000*m.b90 + m.x474 <= 0)

m.c311 = Constraint(expr= - 852000*m.b91 + m.x475 <= 0)

m.c312 = Constraint(expr= - 852000*m.b92 + m.x476 <= 0)

m.c313 = Constraint(expr= - 852000*m.b93 + m.x477 <= 0)

m.c314 = Constraint(expr= - 852000*m.b94 + m.x478 <= 0)

m.c315 = Constraint(expr= - 852000*m.b95 + m.x479 <= 0)

m.c316 = Constraint(expr= - 852000*m.b96 + m.x480 <= 0)

m.c317 = Constraint(expr=   m.x673 - 150*m.x693 >= 0)

m.c318 = Constraint(expr=   m.x674 - 250*m.x693 >= 0)

m.c319 = Constraint(expr=   m.x675 - 500*m.x693 >= 0)

m.c320 = Constraint(expr=   m.x676 - 50*m.x693 >= 0)

m.c321 = Constraint(expr=   m.x577 - m.x685 <= 0)

m.c322 = Constraint(expr=   m.x578 - m.x685 <= 0)

m.c323 = Constraint(expr=   m.x579 - m.x685 <= 0)

m.c324 = Constraint(expr=   m.x580 - m.x685 <= 0)

m.c325 = Constraint(expr=   m.x581 - m.x685 <= 0)

m.c326 = Constraint(expr=   m.x582 - m.x685 <= 0)

m.c327 = Constraint(expr=   m.x583 - m.x685 <= 0)

m.c328 = Constraint(expr=   m.x584 - m.x685 <= 0)

m.c329 = Constraint(expr=   m.x585 - m.x686 <= 0)

m.c330 = Constraint(expr=   m.x586 - m.x686 <= 0)

m.c331 = Constraint(expr=   m.x587 - m.x686 <= 0)

m.c332 = Constraint(expr=   m.x588 - m.x686 <= 0)

m.c333 = Constraint(expr=   m.x589 - m.x686 <= 0)

m.c334 = Constraint(expr=   m.x590 - m.x686 <= 0)

m.c335 = Constraint(expr=   m.x591 - m.x686 <= 0)

m.c336 = Constraint(expr=   m.x592 - m.x686 <= 0)

m.c337 = Constraint(expr=   m.x601 - m.x687 <= 0)

m.c338 = Constraint(expr=   m.x602 - m.x687 <= 0)

m.c339 = Constraint(expr=   m.x603 - m.x687 <= 0)

m.c340 = Constraint(expr=   m.x604 - m.x687 <= 0)

m.c341 = Constraint(expr=   m.x605 - m.x687 <= 0)

m.c342 = Constraint(expr=   m.x606 - m.x687 <= 0)

m.c343 = Constraint(expr=   m.x607 - m.x687 <= 0)

m.c344 = Constraint(expr=   m.x608 - m.x687 <= 0)

m.c345 = Constraint(expr=   m.x609 - m.x688 <= 0)

m.c346 = Constraint(expr=   m.x610 - m.x688 <= 0)

m.c347 = Constraint(expr=   m.x611 - m.x688 <= 0)

m.c348 = Constraint(expr=   m.x612 - m.x688 <= 0)

m.c349 = Constraint(expr=   m.x613 - m.x688 <= 0)

m.c350 = Constraint(expr=   m.x614 - m.x688 <= 0)

m.c351 = Constraint(expr=   m.x615 - m.x688 <= 0)

m.c352 = Constraint(expr=   m.x616 - m.x688 <= 0)

m.c353 = Constraint(expr=   m.x625 - m.x689 <= 0)

m.c354 = Constraint(expr=   m.x626 - m.x689 <= 0)

m.c355 = Constraint(expr=   m.x627 - m.x689 <= 0)

m.c356 = Constraint(expr=   m.x628 - m.x689 <= 0)

m.c357 = Constraint(expr=   m.x629 - m.x689 <= 0)

m.c358 = Constraint(expr=   m.x630 - m.x689 <= 0)

m.c359 = Constraint(expr=   m.x631 - m.x689 <= 0)

m.c360 = Constraint(expr=   m.x632 - m.x689 <= 0)

m.c361 = Constraint(expr=   m.x633 - m.x690 <= 0)

m.c362 = Constraint(expr=   m.x634 - m.x690 <= 0)

m.c363 = Constraint(expr=   m.x635 - m.x690 <= 0)

m.c364 = Constraint(expr=   m.x636 - m.x690 <= 0)

m.c365 = Constraint(expr=   m.x637 - m.x690 <= 0)

m.c366 = Constraint(expr=   m.x638 - m.x690 <= 0)

m.c367 = Constraint(expr=   m.x639 - m.x690 <= 0)

m.c368 = Constraint(expr=   m.x640 - m.x690 <= 0)

m.c369 = Constraint(expr=   m.x649 - m.x691 <= 0)

m.c370 = Constraint(expr=   m.x650 - m.x691 <= 0)

m.c371 = Constraint(expr=   m.x651 - m.x691 <= 0)

m.c372 = Constraint(expr=   m.x652 - m.x691 <= 0)

m.c373 = Constraint(expr=   m.x653 - m.x691 <= 0)

m.c374 = Constraint(expr=   m.x654 - m.x691 <= 0)

m.c375 = Constraint(expr=   m.x655 - m.x691 <= 0)

m.c376 = Constraint(expr=   m.x656 - m.x691 <= 0)

m.c377 = Constraint(expr=   m.x657 - m.x692 <= 0)

m.c378 = Constraint(expr=   m.x658 - m.x692 <= 0)

m.c379 = Constraint(expr=   m.x659 - m.x692 <= 0)

m.c380 = Constraint(expr=   m.x660 - m.x692 <= 0)

m.c381 = Constraint(expr=   m.x661 - m.x692 <= 0)

m.c382 = Constraint(expr=   m.x662 - m.x692 <= 0)

m.c383 = Constraint(expr=   m.x663 - m.x692 <= 0)

m.c384 = Constraint(expr=   m.x664 - m.x692 <= 0)

m.c385 = Constraint(expr=   m.b97 + m.b98 + m.b99 + m.b100 + m.b101 + m.b102 + m.b103 + m.b104 + m.b105 + m.b106
                          + m.b107 + m.b108 + m.b109 + m.b110 + m.b111 + m.b112 + m.b113 + m.b114 + m.b115 + m.b116
                          + m.b117 + m.b118 + m.b119 + m.b120 + m.b121 + m.b122 + m.b123 + m.b124 + m.b125 + m.b126
                          + m.b127 + m.b128 + m.b129 + m.b130 + m.b131 + m.b132 + m.b133 + m.b134 + m.b135 + m.b136
                          + m.b137 + m.b138 + m.b139 + m.b140 + m.b141 + m.b142 + m.b143 + m.b144 + m.b145 + m.b146
                          + m.b147 + m.b148 + m.b149 + m.b150 + m.b151 + m.b152 + m.b153 + m.b154 + m.b155 + m.b156
                          + m.b157 + m.b158 + m.b159 + m.b160 + m.b161 + m.b162 + m.b163 + m.b164 + m.b165 + m.b166
                          + m.b167 + m.b168 + m.b169 + m.b170 + m.b171 + m.b172 + m.b173 + m.b174 + m.b175 + m.b176
                          + m.b177 + m.b178 + m.b179 + m.b180 + m.b181 + m.b182 + m.b183 + m.b184 + m.b185 + m.b186
                          + m.b187 + m.b188 + m.b189 + m.b190 + m.b191 + m.b192 <= 4)

m.c386 = Constraint(expr=   m.b193 + m.b194 + m.b195 + m.b196 + m.b197 + m.b198 + m.b199 + m.b200 + m.b201 + m.b202
                          + m.b203 + m.b204 + m.b205 + m.b206 + m.b207 + m.b208 + m.b209 + m.b210 + m.b211 + m.b212
                          + m.b213 + m.b214 + m.b215 + m.b216 + m.b217 + m.b218 + m.b219 + m.b220 + m.b221 + m.b222
                          + m.b223 + m.b224 + m.b225 + m.b226 + m.b227 + m.b228 + m.b229 + m.b230 + m.b231 + m.b232
                          + m.b233 + m.b234 + m.b235 + m.b236 + m.b237 + m.b238 + m.b239 + m.b240 + m.b241 + m.b242
                          + m.b243 + m.b244 + m.b245 + m.b246 + m.b247 + m.b248 + m.b249 + m.b250 + m.b251 + m.b252
                          + m.b253 + m.b254 + m.b255 + m.b256 + m.b257 + m.b258 + m.b259 + m.b260 + m.b261 + m.b262
                          + m.b263 + m.b264 + m.b265 + m.b266 + m.b267 + m.b268 + m.b269 + m.b270 + m.b271 + m.b272
                          + m.b273 + m.b274 + m.b275 + m.b276 + m.b277 + m.b278 + m.b279 + m.b280 + m.b281 + m.b282
                          + m.b283 + m.b284 + m.b285 + m.b286 + m.b287 + m.b288 <= 4)

m.c387 = Constraint(expr=   m.b289 + m.b290 + m.b291 + m.b292 + m.b293 + m.b294 + m.b295 + m.b296 + m.b297 + m.b298
                          + m.b299 + m.b300 + m.b301 + m.b302 + m.b303 + m.b304 + m.b305 + m.b306 + m.b307 + m.b308
                          + m.b309 + m.b310 + m.b311 + m.b312 + m.b313 + m.b314 + m.b315 + m.b316 + m.b317 + m.b318
                          + m.b319 + m.b320 + m.b321 + m.b322 + m.b323 + m.b324 + m.b325 + m.b326 + m.b327 + m.b328
                          + m.b329 + m.b330 + m.b331 + m.b332 + m.b333 + m.b334 + m.b335 + m.b336 + m.b337 + m.b338
                          + m.b339 + m.b340 + m.b341 + m.b342 + m.b343 + m.b344 + m.b345 + m.b346 + m.b347 + m.b348
                          + m.b349 + m.b350 + m.b351 + m.b352 + m.b353 + m.b354 + m.b355 + m.b356 + m.b357 + m.b358
                          + m.b359 + m.b360 + m.b361 + m.b362 + m.b363 + m.b364 + m.b365 + m.b366 + m.b367 + m.b368
                          + m.b369 + m.b370 + m.b371 + m.b372 + m.b373 + m.b374 + m.b375 + m.b376 + m.b377 + m.b378
                          + m.b379 + m.b380 + m.b381 + m.b382 + m.b383 + m.b384 <= 4)

m.c388 = Constraint(expr=   m.b1 == 1)
