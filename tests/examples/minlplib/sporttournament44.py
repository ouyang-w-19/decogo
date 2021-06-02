#  MINLP written by GAMS Convert at 04/21/18 13:54:17
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        947        1      946        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        947        1      946        0


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
m.b862 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b863 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b864 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b865 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b866 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b867 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b868 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b869 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b870 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b871 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b872 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b873 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b874 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b875 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b876 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b877 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b878 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b879 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b880 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b881 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b882 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b883 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b884 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b885 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b886 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b887 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b888 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b889 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b890 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b891 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b892 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b893 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b894 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b895 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b896 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b897 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b898 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b899 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b900 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b901 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b902 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b903 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b904 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b905 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b906 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b907 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b908 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b909 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b910 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b911 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b912 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b913 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b914 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b915 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b916 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b917 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b918 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b919 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b920 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b921 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b922 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b923 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b924 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b925 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b926 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b927 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b928 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b929 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b930 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b931 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b932 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b933 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b934 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b935 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b936 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b937 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b938 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b939 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b940 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b941 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b942 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b943 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b944 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b945 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b946 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x947 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x947, sense=maximize)

m.c1 = Constraint(expr=2*m.b1*m.b87 - 2*m.b1 - 4*m.b87 - 2*m.b1*m.b613 + 2*m.b1*m.b614 + 2*m.b1*m.b624 + 2*m.b2*m.b431
                        - 2*m.b2 - 2*m.b431 - 2*m.b2*m.b477 + 2*m.b477 + 2*m.b2*m.b615 + 2*m.b2*m.b628 - 2*m.b3*m.b536
                        - 2*m.b3 + 2*m.b536 + 2*m.b3*m.b620 + 2*m.b3*m.b621 + 2*m.b3*m.b640 + 2*m.b4*m.b23 - 2*m.b4 - 2*
                       m.b23 + 2*m.b4*m.b108 - 2*m.b108 - 2*m.b4*m.b500 + 4*m.b500 + 2*m.b4*m.b664 + 2*m.b5*m.b281 - 2*
                       m.b5 - 2*m.b281 - 2*m.b5*m.b642 + 2*m.b5*m.b643 + 2*m.b5*m.b709 + 2*m.b6*m.b134 - 2*m.b6 - 2*
                       m.b134 + 2*m.b6*m.b576 + 2*m.b576 + 2*m.b6*m.b636 - 2*m.b6*m.b679 + 2*m.b7*m.b148 - 2*m.b7 - 2*
                       m.b148 - 2*m.b7*m.b236 + 2*m.b236 + 2*m.b7*m.b544 - 2*m.b544 + 2*m.b7*m.b698 - 2*m.b8*m.b653 - 2*
                       m.b8 + 2*m.b8*m.b654 + 2*m.b8*m.b655 + 2*m.b8*m.b722 + 2*m.b9*m.b516 - 2*m.b9 + 2*m.b516 + 2*m.b9
                       *m.b627 - 2*m.b9*m.b693 + 2*m.b9*m.b694 + 2*m.b10*m.b171 - 2*m.b10 - 2*m.b171 - 2*m.b10*m.b277 + 
                       2*m.b277 + 2*m.b10*m.b487 - 2*m.b487 + 2*m.b10*m.b653 + 2*m.b11*m.b113 - 2*m.b11 - 2*m.b113 + 2*
                       m.b11*m.b337 - 2*m.b337 + 2*m.b11*m.b649 - 2*m.b11*m.b706 + 2*m.b12*m.b198 - 2*m.b12 - 2*m.b198
                        - 2*m.b12*m.b318 + 2*m.b318 + 2*m.b12*m.b544 + 2*m.b12*m.b642 + 2*m.b13*m.b208 - 2*m.b13 - 2*
                       m.b208 + 2*m.b13*m.b675 - 2*m.b13*m.b750 + 2*m.b13*m.b751 + 2*m.b14*m.b135 - 2*m.b14 - 2*m.b135
                        + 2*m.b14*m.b301 - 2*m.b301 + 2*m.b14*m.b636 - 2*m.b14*m.b715 + 2*m.b15*m.b237 - 2*m.b15 - 2*
                       m.b237 - 2*m.b15*m.b355 + 2*m.b355 + 2*m.b15*m.b631 + 2*m.b15*m.b653 + 2*m.b16*m.b248 - 2*m.b16
                        - 2*m.b248 + 2*m.b16*m.b687 - 2*m.b16*m.b761 + 2*m.b16*m.b762 + 2*m.b17*m.b161 - 2*m.b17 - 2*
                       m.b161 - 2*m.b17*m.b412 + 2*m.b412 + 2*m.b17*m.b627 + 2*m.b17*m.b650 + 2*m.b18*m.b340 - 2*m.b18
                        - 2*m.b340 + 2*m.b18*m.b579 - 2*m.b579 + 2*m.b18*m.b581 + 2*m.b581 - 2*m.b18*m.b769 + 2*m.b19*
                       m.b278 - 2*m.b19 - 2*m.b278 - 2*m.b19*m.b393 + 2*m.b393 + 2*m.b19*m.b623 + 2*m.b19*m.b642 + 2*
                       m.b20*m.b108 - 2*m.b20 + 2*m.b20*m.b246 - 2*m.b246 + 2*m.b20*m.b290 - 4*m.b290 - 2*m.b20*m.b776
                        + 2*m.b21*m.b185 - 2*m.b21 - 2*m.b185 + 2*m.b21*m.b337 - 2*m.b21*m.b461 + 2*m.b461 + 2*m.b21*
                       m.b660 + 2*m.b22*m.b319 - 2*m.b22 - 2*m.b319 - 2*m.b22*m.b436 + 2*m.b436 + 2*m.b22*m.b617 + 2*
                       m.b22*m.b631 + 2*m.b23*m.b72 - 4*m.b72 - 2*m.b23*m.b327 - 2*m.b327 + 2*m.b23*m.b558 - 2*m.b558 + 
                       2*m.b24*m.b218 - 2*m.b24 - 2*m.b218 + 2*m.b24*m.b301 - 2*m.b24*m.b515 + 2*m.b515 + 2*m.b24*m.b671
                        + 2*m.b25*m.b126 - 2*m.b25 - 2*m.b126 + 2*m.b25*m.b356 - 2*m.b356 - 2*m.b25*m.b484 + 2*m.b484 + 
                       2*m.b25*m.b623 + 2*m.b26*m.b47 - 2*m.b26 - 2*m.b47 + 2*m.b26*m.b434 - 4*m.b434 + 2*m.b27*m.b106
                        - 2*m.b27 - 2*m.b106 + 2*m.b27*m.b394 - 2*m.b394 - 2*m.b27*m.b541 + 2*m.b541 + 2*m.b27*m.b617 + 
                       2*m.b28*m.b164 - 2*m.b28 - 4*m.b164 - 2*m.b28*m.b587 + 2*m.b587 + 2*m.b28*m.b758 + 2*m.b28*m.b759
                        + 2*m.b29*m.b126 - 2*m.b29 + 2*m.b29*m.b437 - 2*m.b437 + 2*m.b29*m.b643 - 2*m.b29*m.b795 + 2*
                       m.b30*m.b189 - 2*m.b30 - 4*m.b189 - 2*m.b30*m.b772 + 2*m.b30*m.b773 + 2*m.b30*m.b774 + 2*m.b31*
                       m.b106 - 4*m.b31 + 2*m.b31*m.b485 - 2*m.b485 + 2*m.b31*m.b654 + 2*m.b31*m.b795 + 2*m.b32*m.b573
                        - 2*m.b32 - 2*m.b573 + 2*m.b32*m.b693 - 2*m.b32*m.b766 + 2*m.b32*m.b767 + 2*m.b33*m.b224 - 2*
                       m.b33 - 4*m.b224 + 2*m.b33*m.b265 - 2*m.b265 - 2*m.b33*m.b783 + 2*m.b33*m.b784 + 2*m.b34*m.b80 - 
                       2*m.b34 - 4*m.b80 - 2*m.b34*m.b118 - 2*m.b118 + 2*m.b34*m.b224 + 2*m.b34*m.b803 + 2*m.b35*m.b85
                        - 2*m.b35 - 2*m.b85 + 2*m.b35*m.b786 - 2*m.b36*m.b323 + 2*m.b36 + 2*m.b323 + 2*m.b36*m.b493 - 2*
                       m.b493 - 2*m.b36*m.b547 - 2*m.b547 - 2*m.b36*m.b622 + 2*m.b37*m.b515 - 2*m.b37 + 2*m.b37*m.b679
                        - 2*m.b37*m.b779 + 2*m.b37*m.b780 + 2*m.b38*m.b118 - 2*m.b38 + 2*m.b38*m.b266 - 4*m.b266 + 2*
                       m.b38*m.b308 - 4*m.b308 - 2*m.b38*m.b793 + 2*m.b39*m.b54 - 2*m.b39 - 2*m.b54 + 2*m.b39*m.b100 - 4
                       *m.b100 + 2*m.b39*m.b266 - 2*m.b39*m.b784 + 2*m.b40*m.b104 - 2*m.b40 - 2*m.b104 + 2*m.b40*m.b794
                        - 2*m.b41*m.b283 + 2*m.b41 + 2*m.b283 - 2*m.b41*m.b490 - 2*m.b490 + 2*m.b41*m.b550 - 2*m.b550 - 
                       2*m.b41*m.b616 + 2*m.b42*m.b150 - 2*m.b42 - 2*m.b150 + 2*m.b42*m.b284 - 4*m.b284 + 2*m.b42*m.b443
                        - 2*m.b443 - 2*m.b42*m.b833 + 2*m.b43*m.b299 - 2*m.b43 - 2*m.b299 + 2*m.b43*m.b461 + 2*m.b43*
                       m.b669 - 2*m.b43*m.b790 + 2*m.b44*m.b140 - 2*m.b44 - 2*m.b140 + 2*m.b44*m.b309 - 4*m.b309 + 2*
                       m.b44*m.b345 - 4*m.b345 - 2*m.b44*m.b802 + 2*m.b45*m.b65 - 2*m.b45 - 4*m.b65 + 2*m.b45*m.b120 - 4
                       *m.b120 + 2*m.b45*m.b309 - 2*m.b45*m.b774 + 2*m.b46*m.b81 - 2*m.b46 - 2*m.b81 + 2*m.b46*m.b120 - 
                       2*m.b46*m.b229 + 2*m.b229 + 2*m.b46*m.b803 + 2*m.b47*m.b48 - 2*m.b48 - 2*m.b47*m.b103 - 2*m.b103
                        + 2*m.b47*m.b233 - 4*m.b233 + 2*m.b48*m.b124 - 4*m.b124 + 2*m.b49*m.b150 - 2*m.b49 + 2*m.b49*
                       m.b203 - 2*m.b203 - 2*m.b49*m.b399 + 2*m.b399 + 2*m.b49*m.b493 + 2*m.b50*m.b90 + 2*m.b50 + 2*
                       m.b90 - 2*m.b50*m.b154 + 4*m.b154 - 2*m.b50*m.b451 - 2*m.b451 - 2*m.b50*m.b645 + 2*m.b51*m.b335
                        - 2*m.b51 - 2*m.b335 + 2*m.b51*m.b412 + 2*m.b51*m.b658 - 2*m.b51*m.b799 + 2*m.b52*m.b164 - 2*
                       m.b52 + 2*m.b52*m.b346 - 4*m.b346 + 2*m.b52*m.b383 - 4*m.b383 - 2*m.b52*m.b810 + 2*m.b53*m.b80 - 
                       2*m.b53 + 2*m.b53*m.b142 - 4*m.b142 + 2*m.b53*m.b346 - 2*m.b53*m.b759 + 2*m.b54*m.b531 - 4*m.b531
                        + 2*m.b54*m.b785 - 2*m.b54*m.b811 + 2*m.b55*m.b83 - 2*m.b55 - 2*m.b83 - 2*m.b55*m.b85 + 2*m.b55*
                       m.b146 - 4*m.b146 + 2*m.b55*m.b829 + 2*m.b56*m.b57 - 2*m.b56 - 2*m.b57 - 2*m.b56*m.b84 - 2*m.b84
                        + 2*m.b56*m.b274 - 4*m.b274 + 2*m.b56*m.b812 + 2*m.b57*m.b146 + 2*m.b58*m.b242 - 2*m.b58 - 2*
                       m.b242 - 2*m.b58*m.b360 + 2*m.b360 + 2*m.b58*m.b550 + 2*m.b58*m.b833 + 2*m.b59*m.b74 + 2*m.b59 + 
                       2*m.b74 - 2*m.b59*m.b181 + 4*m.b181 - 2*m.b59*m.b632 - 2*m.b59*m.b689 + 2*m.b60*m.b160 - 2*m.b60
                        - 2*m.b160 + 2*m.b60*m.b376 - 4*m.b376 + 2*m.b60*m.b715 - 2*m.b60*m.b808 + 2*m.b61*m.b62 - 2*
                       m.b61 - 2*m.b62 + 2*m.b61*m.b114 - 2*m.b114 + 2*m.b61*m.b260 - 4*m.b260 - 2*m.b61*m.b695 + 2*
                       m.b62*m.b95 - 2*m.b95 + 2*m.b62*m.b137 - 2*m.b137 - 2*m.b62*m.b854 + 2*m.b63*m.b189 - 4*m.b63 + 2
                       *m.b63*m.b384 - 2*m.b384 + 2*m.b63*m.b422 - 4*m.b422 + 2*m.b63*m.b810 + 2*m.b64*m.b100 - 4*m.b64
                        + 2*m.b64*m.b166 - 4*m.b166 + 2*m.b64*m.b384 + 2*m.b64*m.b759 + 2*m.b65*m.b227 - 4*m.b227 + 2*
                       m.b65*m.b775 + 2*m.b65*m.b804 + 2*m.b66*m.b67 - 2*m.b66 - 2*m.b67 - 2*m.b66*m.b82 + 2*m.b82 + 2*
                       m.b66*m.b831 + 2*m.b66*m.b839 - 2*m.b67*m.b68 - 2*m.b68 + 2*m.b67*m.b102 - 4*m.b102 + 2*m.b67*
                       m.b169 - 4*m.b169 + 2*m.b68*m.b69 - 2*m.b69 + 2*m.b68*m.b599 - 2*m.b599 + 2*m.b68*m.b818 + 2*
                       m.b69*m.b169 + 2*m.b70*m.b107 - 2*m.b70 - 2*m.b107 + 2*m.b70*m.b607 + 2*m.b70*m.b709 - 2*m.b70*
                       m.b858 + 2*m.b71*m.b203 - 2*m.b71 + 2*m.b71*m.b286 - 4*m.b286 - 2*m.b71*m.b323 + 2*m.b71*m.b613
                        + 2*m.b72*m.b150 + 2*m.b72*m.b286 + 2*m.b72*m.b725 + 2*m.b73*m.b75 + 2*m.b73 - 2*m.b75 - 2*m.b73
                       *m.b213 + 4*m.b213 - 2*m.b73*m.b625 - 2*m.b73*m.b702 - 2*m.b74*m.b634 - 2*m.b74*m.b852 - 2*m.b74*
                       m.b853 + 2*m.b75*m.b647 + 2*m.b75*m.b853 - 2*m.b75*m.b861 + 2*m.b76*m.b93 - 2*m.b76 - 2*m.b93 + 2
                       *m.b76*m.b183 - 4*m.b183 + 2*m.b76*m.b513 - 2*m.b513 - 2*m.b76*m.b568 + 2*m.b568 + 2*m.b77*m.b134
                        - 2*m.b77 + 2*m.b77*m.b410 - 4*m.b410 + 2*m.b77*m.b706 - 2*m.b77*m.b817 + 2*m.b78*m.b224 - 4*
                       m.b78 + 2*m.b78*m.b423 - 2*m.b423 + 2*m.b78*m.b472 - 4*m.b472 + 2*m.b78*m.b802 + 2*m.b79*m.b120
                        - 4*m.b79 + 2*m.b79*m.b191 - 4*m.b191 + 2*m.b79*m.b423 + 2*m.b79*m.b774 + 2*m.b80*m.b760 + 2*
                       m.b80*m.b811 - 2*m.b81*m.b82 + 2*m.b81*m.b606 + 2*m.b81*m.b620 + 2*m.b82*m.b122 - 4*m.b122 - 2*
                       m.b82*m.b864 + 2*m.b83*m.b84 - 2*m.b83*m.b846 + 2*m.b83*m.b847 + 2*m.b84*m.b122 + 2*m.b84*m.b195
                        - 4*m.b195 + 2*m.b85*m.b86 - 2*m.b86 + 2*m.b85*m.b539 - 2*m.b539 + 2*m.b86*m.b195 + 2*m.b87*
                       m.b127 - 2*m.b127 + 2*m.b87*m.b722 + 2*m.b87*m.b858 + 2*m.b88*m.b242 - 2*m.b88 - 2*m.b88*m.b283
                        + 2*m.b88*m.b325 - 4*m.b325 + 2*m.b88*m.b608 + 2*m.b89*m.b91 + 2*m.b89 - 2*m.b91 - 2*m.b89*
                       m.b566 + 2*m.b566 - 2*m.b89*m.b619 - 2*m.b89*m.b712 - 2*m.b90*m.b564 + 2*m.b564 - 2*m.b90*m.b647
                        - 2*m.b90*m.b844 + 2*m.b91*m.b656 + 2*m.b91*m.b844 - 2*m.b91*m.b868 + 2*m.b92*m.b215 - 2*m.b92
                        - 4*m.b215 + 2*m.b92*m.b570 - 2*m.b570 - 2*m.b92*m.b764 + 2*m.b92*m.b765 - 2*m.b93*m.b571 + 2*
                       m.b571 + 2*m.b93*m.b604 + 2*m.b93*m.b678 + 2*m.b94*m.b459 - 4*m.b94 - 4*m.b459 + 2*m.b94*m.b693
                        + 2*m.b94*m.b694 + 2*m.b94*m.b817 + 2*m.b95*m.b97 - 4*m.b97 + 2*m.b95*m.b603 - 2*m.b95*m.b746 + 
                       2*m.b96*m.b97 - 4*m.b96 + 2*m.b96*m.b680 + 2*m.b96*m.b733 + 2*m.b96*m.b838 + 2*m.b97*m.b471 + 2*
                       m.b471 + 2*m.b97*m.b602 + 2*m.b98*m.b266 - 4*m.b98 + 2*m.b98*m.b473 - 2*m.b473 + 2*m.b98*m.b528
                        - 4*m.b528 + 2*m.b98*m.b793 + 2*m.b99*m.b142 - 4*m.b99 + 2*m.b99*m.b226 - 4*m.b226 + 2*m.b99*
                       m.b473 + 2*m.b99*m.b784 + 2*m.b100*m.b749 + 2*m.b100*m.b805 + 2*m.b101*m.b144 + 2*m.b101 - 4*
                       m.b144 - 2*m.b101*m.b674 - 2*m.b101*m.b829 - 2*m.b101*m.b871 + 2*m.b102*m.b103 + 2*m.b102*m.b846
                        + 2*m.b102*m.b857 + 2*m.b103*m.b144 + 2*m.b103*m.b234 - 2*m.b234 + 2*m.b104*m.b105 - 2*m.b105 + 
                       2*m.b104*m.b480 - 2*m.b480 - 2*m.b104*m.b831 + 2*m.b105*m.b234 + 2*m.b106*m.b630 - 2*m.b106*
                       m.b872 - 2*m.b107*m.b240 + 2*m.b240 + 2*m.b107*m.b286 + 2*m.b107*m.b362 - 4*m.b362 - 2*m.b108*
                       m.b368 + 2*m.b368 + 2*m.b108*m.b633 - 2*m.b109*m.b506 + 2*m.b109 + 2*m.b506 - 2*m.b109*m.b656 + 2
                       *m.b109*m.b666 - 2*m.b109*m.b836 + 2*m.b110*m.b369 - 4*m.b110 - 4*m.b369 + 2*m.b110*m.b667 + 2*
                       m.b110*m.b726 + 2*m.b110*m.b836 + 2*m.b111*m.b255 - 2*m.b111 - 4*m.b255 + 2*m.b111*m.b610 - 2*
                       m.b111*m.b777 + 2*m.b111*m.b778 + 2*m.b112*m.b113 - 4*m.b112 + 2*m.b112*m.b514 - 4*m.b514 + 2*
                       m.b112*m.b679 + 2*m.b112*m.b808 - 2*m.b113*m.b876 + 2*m.b113*m.b877 + 2*m.b114*m.b116 - 4*m.b116
                        + 2*m.b114*m.b162 - 2*m.b162 - 2*m.b114*m.b419 + 4*m.b419 + 2*m.b115*m.b672 - 2*m.b115 + 2*
                       m.b115*m.b718 + 2*m.b115*m.b845 - 2*m.b115*m.b862 + 2*m.b116*m.b603 + 2*m.b116*m.b828 + 2*m.b116*
                       m.b862 + 2*m.b117*m.b309 - 4*m.b117 + 2*m.b117*m.b529 - 2*m.b529 + 2*m.b117*m.b588 - 4*m.b588 + 2
                       *m.b117*m.b783 + 2*m.b118*m.b119 - 4*m.b119 + 2*m.b118*m.b734 + 2*m.b119*m.b166 + 2*m.b119*m.b268
                        - 4*m.b268 + 2*m.b119*m.b529 + 2*m.b120*m.b737 + 2*m.b121*m.b428 - 2*m.b121 + 2*m.b428 + 2*
                       m.b121*m.b595 - 4*m.b595 + 2*m.b121*m.b811 - 2*m.b121*m.b830 + 2*m.b122*m.b123 - 2*m.b123 + 2*
                       m.b122*m.b231 - 2*m.b231 + 2*m.b123*m.b167 - 4*m.b167 + 2*m.b123*m.b275 - 2*m.b275 - 2*m.b123*
                       m.b794 + 2*m.b124*m.b125 - 2*m.b125 + 2*m.b124*m.b432 - 4*m.b432 + 2*m.b124*m.b831 + 2*m.b125*
                       m.b275 + 2*m.b126*m.b622 - 2*m.b126*m.b881 - 2*m.b127*m.b201 + 2*m.b201 + 2*m.b127*m.b325 + 2*
                       m.b127*m.b401 - 4*m.b401 + 2*m.b128*m.b129 - 2*m.b128 - 2*m.b129 - 2*m.b128*m.b331 + 2*m.b331 + 2
                       *m.b128*m.b558 + 2*m.b128*m.b688 + 2*m.b129*m.b504 - 2*m.b504 - 2*m.b129*m.b625 + 2*m.b129*m.b875
                        - 2*m.b130*m.b666 + 4*m.b130 - 2*m.b130*m.b667 - 2*m.b130*m.b826 - 2*m.b130*m.b827 + 2*m.b131*
                       m.b677 - 4*m.b131 + 2*m.b131*m.b740 + 2*m.b131*m.b827 + 2*m.b131*m.b868 + 2*m.b132*m.b297 - 4*
                       m.b132 - 4*m.b297 + 2*m.b132*m.b605 + 2*m.b132*m.b777 + 2*m.b132*m.b789 + 2*m.b133*m.b135 - 4*
                       m.b133 + 2*m.b133*m.b572 - 4*m.b572 + 2*m.b133*m.b669 + 2*m.b133*m.b799 + 2*m.b134*m.b217 - 4*
                       m.b217 - 2*m.b134*m.b219 - 2*m.b219 + 2*m.b135*m.b219 - 2*m.b135*m.b886 + 2*m.b136*m.b219 - 4*
                       m.b136 + 2*m.b136*m.b259 - 2*m.b259 + 2*m.b136*m.b657 + 2*m.b136*m.b809 - 2*m.b137*m.b138 + 2*
                       m.b138 + 2*m.b137*m.b661 + 2*m.b137*m.b708 - 2*m.b138*m.b587 + 2*m.b138*m.b735 - 2*m.b138*m.b888
                        + 2*m.b139*m.b346 - 2*m.b139 + 2*m.b139*m.b590 - 2*m.b590 - 2*m.b139*m.b602 + 2*m.b139*m.b772 + 
                       2*m.b140*m.b141 - 4*m.b141 + 2*m.b140*m.b747 - 2*m.b140*m.b804 + 2*m.b141*m.b191 + 2*m.b141*
                       m.b311 - 4*m.b311 + 2*m.b141*m.b590 + 2*m.b142*m.b721 + 2*m.b142*m.b785 + 2*m.b143*m.b227 - 2*
                       m.b143 + 2*m.b143*m.b477 + 2*m.b143*m.b535 - 4*m.b535 - 2*m.b143*m.b839 + 2*m.b144*m.b145 - 2*
                       m.b145 + 2*m.b144*m.b272 - 2*m.b272 + 2*m.b145*m.b193 - 4*m.b193 + 2*m.b145*m.b317 - 2*m.b317 - 2
                       *m.b145*m.b786 + 2*m.b146*m.b147 - 2*m.b147 + 2*m.b146*m.b481 - 4*m.b481 + 2*m.b147*m.b317 + 2*
                       m.b148*m.b199 - 2*m.b199 + 2*m.b149*m.b202 + 2*m.b149 - 2*m.b202 - 2*m.b149*m.b549 - 2*m.b549 - 2
                       *m.b149*m.b722 - 2*m.b149*m.b882 - 2*m.b150*m.b825 + 2*m.b151*m.b153 - 2*m.b151 - 2*m.b153 - 2*
                       m.b151*m.b292 + 2*m.b292 + 2*m.b151*m.b501 - 2*m.b501 + 2*m.b151*m.b676 + 2*m.b152*m.b252 - 2*
                       m.b152 - 2*m.b252 + 2*m.b152*m.b290 - 2*m.b152*m.b562 - 2*m.b562 + 2*m.b152*m.b664 + 2*m.b153*
                       m.b562 - 2*m.b153*m.b619 + 2*m.b153*m.b866 - 2*m.b154*m.b677 - 2*m.b154*m.b821 - 2*m.b154*m.b822
                        + 2*m.b155*m.b690 - 4*m.b155 + 2*m.b155*m.b752 + 2*m.b155*m.b822 + 2*m.b155*m.b861 + 2*m.b156*
                       m.b647 - 4*m.b156 + 2*m.b156*m.b741 + 2*m.b156*m.b822 + 2*m.b156*m.b885 + 2*m.b157*m.b158 - 4*
                       m.b157 - 4*m.b158 + 2*m.b157*m.b333 - 4*m.b333 + 2*m.b157*m.b764 + 2*m.b157*m.b798 + 2*m.b158*
                       m.b409 - 2*m.b409 + 2*m.b158*m.b609 + 2*m.b158*m.b885 + 2*m.b159*m.b161 - 2*m.b159 - 2*m.b159*
                       m.b609 + 2*m.b159*m.b658 + 2*m.b159*m.b790 + 2*m.b160*m.b184 - 2*m.b184 - 2*m.b160*m.b257 - 2*
                       m.b257 + 2*m.b160*m.b668 + 2*m.b161*m.b257 - 2*m.b161*m.b895 + 2*m.b162*m.b378 - 2*m.b378 - 2*
                       m.b162*m.b523 + 4*m.b523 + 2*m.b162*m.b770 - 2*m.b163*m.b697 + 2*m.b163 + 2*m.b163*m.b748 - 2*
                       m.b163*m.b772 - 2*m.b163*m.b897 + 2*m.b164*m.b165 - 2*m.b165 + 2*m.b164*m.b531 + 2*m.b165*m.b226
                        + 2*m.b165*m.b349 - 4*m.b349 - 2*m.b165*m.b591 - 2*m.b591 + 2*m.b166*m.b312 - 2*m.b312 + 2*
                       m.b166*m.b775 + 2*m.b167*m.b168 - 4*m.b168 + 2*m.b167*m.b315 - 2*m.b315 + 2*m.b167*m.b830 + 2*
                       m.b168*m.b232 - 4*m.b232 + 2*m.b168*m.b354 - 2*m.b354 + 2*m.b168*m.b786 + 2*m.b169*m.b170 - 2*
                       m.b170 + 2*m.b169*m.b540 - 4*m.b540 + 2*m.b170*m.b354 + 2*m.b171*m.b238 - 2*m.b238 + 2*m.b172*
                       m.b199 - 4*m.b172 + 2*m.b172*m.b238 + 2*m.b172*m.b397 - 2*m.b397 + 2*m.b172*m.b616 + 2*m.b173*
                       m.b241 + 2*m.b173 - 2*m.b241 - 2*m.b173*m.b492 - 2*m.b492 - 2*m.b173*m.b709 - 2*m.b173*m.b873 + 2
                       *m.b174*m.b206 + 2*m.b174 - 2*m.b206 - 2*m.b174*m.b446 - 2*m.b446 - 2*m.b174*m.b624 - 2*m.b174*
                       m.b751 + 2*m.b175*m.b206 - 2*m.b175 + 2*m.b175*m.b496 - 4*m.b496 - 2*m.b175*m.b738 + 2*m.b175*
                       m.b833 + 2*m.b176*m.b178 - 2*m.b176 - 4*m.b178 - 2*m.b176*m.b250 + 2*m.b250 + 2*m.b176*m.b448 - 2
                       *m.b448 + 2*m.b176*m.b665 + 2*m.b177*m.b179 + 2*m.b177 - 2*m.b179 - 2*m.b177*m.b248 - 2*m.b177*
                       m.b504 - 2*m.b177*m.b787 + 2*m.b178*m.b179 + 2*m.b178*m.b619 + 2*m.b178*m.b859 - 2*m.b179*m.b180
                        - 2*m.b180 + 2*m.b179*m.b852 + 2*m.b180*m.b182 - 4*m.b182 + 2*m.b180*m.b645 + 2*m.b180*m.b763 - 
                       2*m.b181*m.b370 - 2*m.b370 - 2*m.b181*m.b690 - 2*m.b181*m.b815 + 2*m.b182*m.b703 + 2*m.b182*
                       m.b815 + 2*m.b182*m.b852 + 2*m.b183*m.b569 + 2*m.b569 + 2*m.b183*m.b656 + 2*m.b183*m.b815 + 2*
                       m.b184*m.b185 - 2*m.b184*m.b604 + 2*m.b184*m.b779 + 2*m.b185*m.b300 - 2*m.b300 - 2*m.b185*m.b411
                        + 2*m.b411 + 2*m.b186*m.b300 - 2*m.b186 + 2*m.b186*m.b339 + 2*m.b339 - 2*m.b186*m.b518 + 2*
                       m.b518 + 2*m.b186*m.b877 + 2*m.b187*m.b415 - 2*m.b187 - 2*m.b415 - 2*m.b187*m.b467 + 2*m.b467 + 2
                       *m.b187*m.b680 + 2*m.b187*m.b756 - 2*m.b188*m.b682 + 2*m.b188 + 2*m.b188*m.b758 - 2*m.b188*m.b783
                        - 2*m.b188*m.b904 + 2*m.b189*m.b190 - 2*m.b190 + 2*m.b189*m.b804 + 2*m.b190*m.b268 + 2*m.b190*
                       m.b386 - 4*m.b386 - 2*m.b190*m.b530 - 2*m.b530 + 2*m.b191*m.b269 - 2*m.b269 + 2*m.b191*m.b760 + 2
                       *m.b192*m.b427 + 2*m.b192 - 4*m.b427 - 2*m.b192*m.b612 - 2*m.b192*m.b805 - 2*m.b192*m.b857 + 2*
                       m.b193*m.b194 - 4*m.b194 + 2*m.b193*m.b352 - 2*m.b352 + 2*m.b193*m.b839 + 2*m.b194*m.b273 - 4*
                       m.b273 + 2*m.b194*m.b392 - 4*m.b392 + 2*m.b194*m.b794 + 2*m.b195*m.b196 - 2*m.b196 + 2*m.b195*
                       m.b600 - 4*m.b600 + 2*m.b196*m.b392 - 2*m.b197*m.b279 + 2*m.b197 - 2*m.b279 - 2*m.b197*m.b683 + 2
                       *m.b198*m.b279 + 2*m.b199*m.b542 - 2*m.b542 - 2*m.b199*m.b892 - 2*m.b200*m.b358 + 2*m.b200 - 2*
                       m.b358 - 2*m.b200*m.b654 + 2*m.b200*m.b820 - 2*m.b200*m.b858 + 2*m.b201*m.b285 - 2*m.b285 - 2*
                       m.b201*m.b442 - 2*m.b442 - 2*m.b201*m.b699 + 2*m.b202*m.b445 - 4*m.b445 + 2*m.b202*m.b553 - 4*
                       m.b553 - 2*m.b202*m.b893 + 2*m.b203*m.b205 - 2*m.b205 - 2*m.b203*m.b841 + 2*m.b204*m.b207 + 2*
                       m.b204 - 4*m.b207 - 2*m.b204*m.b402 - 2*m.b402 - 2*m.b204*m.b618 - 2*m.b204*m.b739 + 2*m.b205*
                       m.b207 + 2*m.b205*m.b553 - 2*m.b205*m.b750 + 2*m.b206*m.b558 - 2*m.b206*m.b900 + 2*m.b207*m.b501
                        + 2*m.b207*m.b900 - 2*m.b208*m.b210 + 2*m.b210 + 2*m.b208*m.b211 - 4*m.b211 + 2*m.b208*m.b403 - 
                       2*m.b403 + 2*m.b209*m.b211 - 2*m.b209 - 2*m.b209*m.b850 + 2*m.b209*m.b900 + 2*m.b209*m.b907 + 2*
                       m.b210*m.b212 - 2*m.b212 - 2*m.b210*m.b450 - 2*m.b450 - 2*m.b210*m.b796 + 2*m.b211*m.b212 + 2*
                       m.b211*m.b625 + 2*m.b212*m.b564 - 2*m.b212*m.b752 - 2*m.b213*m.b214 + 2*m.b214 - 2*m.b213*m.b404
                        - 2*m.b404 - 2*m.b213*m.b703 + 2*m.b214*m.b215 - 2*m.b214*m.b568 - 2*m.b214*m.b908 + 2*m.b215*
                       m.b512 + 2*m.b512 + 2*m.b215*m.b667 - 2*m.b216*m.b691 + 2*m.b216 + 2*m.b216*m.b767 - 2*m.b216*
                       m.b807 - 2*m.b216*m.b808 + 2*m.b217*m.b218 + 2*m.b217*m.b609 + 2*m.b217*m.b766 + 2*m.b218*m.b336
                        - 2*m.b336 - 2*m.b218*m.b460 + 2*m.b460 + 2*m.b219*m.b220 - 2*m.b220 + 2*m.b220*m.b303 + 2*
                       m.b303 + 2*m.b220*m.b336 - 2*m.b220*m.b578 + 2*m.b578 - 2*m.b221*m.b418 - 2*m.b221 + 2*m.b418 + 2
                       *m.b221*m.b672 + 2*m.b221*m.b745 + 2*m.b221*m.b801 - 2*m.b222*m.b223 + 2*m.b222 + 2*m.b223 - 2*
                       m.b222*m.b637 + 2*m.b222*m.b673 - 2*m.b222*m.b828 + 2*m.b223*m.b773 - 2*m.b223*m.b793 - 2*m.b223*
                       m.b911 + 2*m.b224*m.b225 - 2*m.b225 + 2*m.b225*m.b311 + 2*m.b225*m.b425 - 4*m.b425 - 2*m.b225*
                       m.b474 - 2*m.b474 + 2*m.b226*m.b228 - 4*m.b228 + 2*m.b226*m.b749 + 2*m.b227*m.b230 - 4*m.b230 + 2
                       *m.b227*m.b534 - 4*m.b534 + 2*m.b228*m.b230 + 2*m.b228*m.b389 + 2*m.b389 + 2*m.b228*m.b425 - 2*
                       m.b229*m.b231 + 2*m.b229*m.b388 - 4*m.b388 - 2*m.b229*m.b536 + 2*m.b230*m.b231 + 2*m.b230*m.b612
                        + 2*m.b231*m.b316 - 4*m.b316 + 2*m.b232*m.b233 + 2*m.b232*m.b390 - 2*m.b390 + 2*m.b232*m.b847 + 
                       2*m.b233*m.b316 + 2*m.b233*m.b433 - 4*m.b433 + 2*m.b234*m.b235 - 2*m.b235 - 2*m.b234*m.b640 + 2*
                       m.b235*m.b433 - 2*m.b236*m.b320 - 2*m.b320 + 2*m.b237*m.b320 + 2*m.b238*m.b239 - 2*m.b239 - 2*
                       m.b238*m.b684 + 2*m.b239*m.b320 + 2*m.b239*m.b489 - 2*m.b489 - 2*m.b239*m.b881 + 2*m.b240*m.b324
                        - 2*m.b324 - 2*m.b240*m.b398 - 2*m.b398 - 2*m.b240*m.b685 + 2*m.b241*m.b243 - 2*m.b243 + 2*
                       m.b241*m.b496 - 2*m.b241*m.b899 + 2*m.b242*m.b245 - 2*m.b245 - 2*m.b242*m.b849 + 2*m.b243*m.b245
                        + 2*m.b243*m.b324 - 2*m.b243*m.b711 + 2*m.b244*m.b247 + 2*m.b244 - 4*m.b247 - 2*m.b244*m.b363 - 
                       2*m.b363 - 2*m.b244*m.b614 - 2*m.b244*m.b725 + 2*m.b245*m.b247 - 2*m.b245*m.b761 + 2*m.b246*
                       m.b644 + 2*m.b246*m.b825 - 2*m.b246*m.b894 + 2*m.b247*m.b448 + 2*m.b247*m.b894 + 2*m.b248*m.b251
                        - 4*m.b251 + 2*m.b248*m.b366 - 2*m.b366 + 2*m.b249*m.b251 - 2*m.b249 + 2*m.b249*m.b502 - 2*
                       m.b502 - 2*m.b249*m.b842 + 2*m.b249*m.b894 + 2*m.b250*m.b253 - 2*m.b253 - 2*m.b250*m.b806 - 2*
                       m.b250*m.b867 + 2*m.b251*m.b253 + 2*m.b251*m.b632 + 2*m.b252*m.b369 - 2*m.b252*m.b506 + 2*m.b252*
                       m.b835 + 2*m.b253*m.b506 - 2*m.b253*m.b740 + 2*m.b254*m.b255 + 2*m.b254 - 2*m.b254*m.b566 - 2*
                       m.b254*m.b764 - 2*m.b254*m.b913 + 2*m.b255*m.b457 + 2*m.b457 + 2*m.b255*m.b677 - 2*m.b256*m.b678
                        + 2*m.b256 + 2*m.b256*m.b780 - 2*m.b256*m.b816 - 2*m.b256*m.b817 + 2*m.b257*m.b258 - 2*m.b258 + 
                       2*m.b257*m.b878 + 2*m.b258*m.b769 - 2*m.b258*m.b837 + 2*m.b258*m.b915 + 2*m.b259*m.b260 - 2*
                       m.b259*m.b302 - 2*m.b302 + 2*m.b259*m.b415 + 2*m.b260*m.b262 - 2*m.b262 + 2*m.b260*m.b769 - 2*
                       m.b261*m.b380 - 2*m.b261 + 2*m.b380 + 2*m.b261*m.b661 + 2*m.b261*m.b732 + 2*m.b261*m.b792 + 2*
                       m.b262*m.b380 + 2*m.b262*m.b465 - 2*m.b465 - 2*m.b262*m.b828 - 2*m.b263*m.b264 + 2*m.b263 + 2*
                       m.b264 - 2*m.b263*m.b583 + 2*m.b583 - 2*m.b263*m.b651 + 2*m.b263*m.b663 + 2*m.b264*m.b265 - 2*
                       m.b264*m.b802 - 2*m.b264*m.b916 - 2*m.b265*m.b663 + 2*m.b265*m.b917 + 2*m.b266*m.b267 - 2*m.b267
                        + 2*m.b267*m.b349 + 2*m.b267*m.b475 - 4*m.b475 - 2*m.b267*m.b918 + 2*m.b268*m.b270 - 4*m.b270 + 
                       2*m.b268*m.b737 + 2*m.b269*m.b386 + 2*m.b269*m.b736 - 2*m.b269*m.b905 + 2*m.b270*m.b351 + 2*
                       m.b351 + 2*m.b270*m.b475 + 2*m.b270*m.b905 - 2*m.b271*m.b272 + 2*m.b271 + 2*m.b271*m.b350 - 4*
                       m.b350 - 2*m.b271*m.b477 - 2*m.b271*m.b785 + 2*m.b272*m.b353 - 4*m.b353 + 2*m.b272*m.b905 + 2*
                       m.b273*m.b274 + 2*m.b273*m.b429 - 2*m.b429 + 2*m.b273*m.b857 + 2*m.b274*m.b353 + 2*m.b274*m.b482
                        - 4*m.b482 + 2*m.b275*m.b276 - 2*m.b276 - 2*m.b275*m.b628 + 2*m.b276*m.b482 - 2*m.b277*m.b357 - 
                       2*m.b357 + 2*m.b278*m.b357 + 2*m.b279*m.b280 - 2*m.b280 + 2*m.b279*m.b892 + 2*m.b280*m.b357 + 2*
                       m.b280*m.b546 - 2*m.b546 - 2*m.b280*m.b872 + 2*m.b281*m.b284 - 2*m.b281*m.b399 + 2*m.b281*m.b616
                        + 2*m.b282*m.b284 - 2*m.b282 - 2*m.b282*m.b360 + 2*m.b282*m.b546 + 2*m.b282*m.b872 - 2*m.b283*
                       m.b359 - 2*m.b359 + 2*m.b283*m.b361 - 4*m.b361 + 2*m.b284*m.b361 + 2*m.b285*m.b287 - 2*m.b287 + 2
                       *m.b285*m.b553 - 2*m.b285*m.b906 + 2*m.b286*m.b288 - 2*m.b288 + 2*m.b287*m.b288 + 2*m.b287*m.b361
                        - 2*m.b287*m.b701 + 2*m.b288*m.b289 - 4*m.b289 - 2*m.b288*m.b776 + 2*m.b289*m.b403 + 2*m.b289*
                       m.b686 + 2*m.b289*m.b884 + 2*m.b290*m.b293 - 4*m.b293 + 2*m.b290*m.b329 - 2*m.b329 + 2*m.b291*
                       m.b293 - 2*m.b291 + 2*m.b291*m.b559 - 2*m.b559 - 2*m.b291*m.b835 + 2*m.b291*m.b884 + 2*m.b292*
                       m.b294 - 2*m.b294 - 2*m.b292*m.b449 + 2*m.b449 - 2*m.b292*m.b860 + 2*m.b293*m.b294 + 2*m.b293*
                       m.b645 - 2*m.b294*m.b726 + 2*m.b294*m.b826 + 2*m.b295*m.b297 + 2*m.b295 - 2*m.b295*m.b508 + 2*
                       m.b508 - 2*m.b295*m.b777 - 2*m.b295*m.b919 - 2*m.b296*m.b406 + 4*m.b296 + 2*m.b406 - 2*m.b296*
                       m.b677 - 2*m.b296*m.b678 - 2*m.b296*m.b853 + 2*m.b297*m.b406 + 2*m.b297*m.b690 + 2*m.b298*m.b299
                        - 2*m.b298 + 2*m.b298*m.b691 + 2*m.b298*m.b817 - 2*m.b298*m.b823 - 2*m.b299*m.b920 + 2*m.b299*
                       m.b921 + 2*m.b300*m.b302 - 2*m.b300*m.b658 + 2*m.b301*m.b635 - 2*m.b301*m.b755 + 2*m.b302*m.b755
                        + 2*m.b302*m.b922 - 2*m.b303*m.b660 - 2*m.b303*m.b717 - 2*m.b303*m.b910 - 2*m.b304*m.b342 - 2*
                       m.b304 + 2*m.b342 + 2*m.b304*m.b651 + 2*m.b304*m.b717 + 2*m.b304*m.b782 + 2*m.b305*m.b342 - 2*
                       m.b305 + 2*m.b305*m.b520 - 2*m.b520 - 2*m.b305*m.b838 + 2*m.b305*m.b910 - 2*m.b306*m.b307 + 4*
                       m.b306 + 2*m.b307 - 2*m.b306*m.b523 - 2*m.b306*m.b661 - 2*m.b306*m.b663 + 2*m.b307*m.b308 - 2*
                       m.b307*m.b810 - 2*m.b307*m.b924 + 2*m.b308*m.b663 + 2*m.b308*m.b925 + 2*m.b309*m.b310 - 2*m.b310
                        + 2*m.b310*m.b386 + 2*m.b310*m.b533 - 4*m.b533 - 2*m.b310*m.b926 + 2*m.b311*m.b313 - 4*m.b313 + 
                       2*m.b311*m.b721 + 2*m.b312*m.b349 + 2*m.b312*m.b720 - 2*m.b312*m.b898 + 2*m.b313*m.b314 + 2*
                       m.b314 + 2*m.b313*m.b533 + 2*m.b313*m.b898 - 2*m.b314*m.b315 - 2*m.b314*m.b428 - 2*m.b314*m.b775
                        + 2*m.b315*m.b391 - 4*m.b391 + 2*m.b315*m.b898 + 2*m.b316*m.b478 - 2*m.b478 + 2*m.b316*m.b599 - 
                       2*m.b317*m.b621 + 2*m.b317*m.b927 - 2*m.b318*m.b395 - 2*m.b395 + 2*m.b319*m.b395 + 2*m.b320*
                       m.b321 - 2*m.b321 + 2*m.b321*m.b395 + 2*m.b321*m.b723 - 2*m.b321*m.b865 - 2*m.b322*m.b323 - 2*
                       m.b322 + 2*m.b322*m.b723 + 2*m.b322*m.b881 + 2*m.b322*m.b912 + 2*m.b323*m.b400 - 4*m.b400 + 2*
                       m.b324*m.b326 - 2*m.b326 - 2*m.b324*m.b912 + 2*m.b325*m.b327 + 2*m.b325*m.b849 + 2*m.b326*m.b327
                        + 2*m.b326*m.b400 - 2*m.b326*m.b686 + 2*m.b327*m.b328 - 4*m.b328 + 2*m.b328*m.b330 - 2*m.b330 + 
                       2*m.b328*m.b366 + 2*m.b328*m.b701 + 2*m.b329*m.b365 - 4*m.b365 - 2*m.b329*m.b560 + 2*m.b560 + 2*
                       m.b329*m.b724 + 2*m.b330*m.b560 - 2*m.b330*m.b751 + 2*m.b330*m.b875 - 2*m.b331*m.b503 + 2*m.b503
                        + 2*m.b331*m.b712 - 2*m.b331*m.b851 - 2*m.b332*m.b373 + 4*m.b332 + 2*m.b373 - 2*m.b332*m.b690 - 
                       2*m.b332*m.b691 - 2*m.b332*m.b844 + 2*m.b333*m.b373 + 2*m.b333*m.b703 + 2*m.b333*m.b788 + 2*
                       m.b334*m.b335 - 2*m.b334 - 2*m.b334*m.b407 + 2*m.b407 + 2*m.b334*m.b704 + 2*m.b334*m.b808 + 2*
                       m.b335*m.b460 - 2*m.b335*m.b931 + 2*m.b336*m.b338 - 4*m.b338 - 2*m.b336*m.b669 + 2*m.b337*m.b626
                        - 2*m.b337*m.b744 + 2*m.b338*m.b744 + 2*m.b338*m.b837 + 2*m.b338*m.b932 - 2*m.b339*m.b671 - 2*
                       m.b339*m.b732 - 2*m.b339*m.b903 + 2*m.b340*m.b637 + 2*m.b340*m.b770 - 2*m.b340*m.b771 + 2*m.b341*
                       m.b580 - 2*m.b341 - 2*m.b580 + 2*m.b341*m.b771 - 2*m.b341*m.b845 + 2*m.b341*m.b903 - 2*m.b342*
                       m.b469 + 2*m.b469 - 2*m.b342*m.b924 - 2*m.b343*m.b344 + 4*m.b343 - 2*m.b344 - 2*m.b343*m.b467 - 2
                       *m.b343*m.b672 - 2*m.b343*m.b673 + 2*m.b344*m.b345 + 2*m.b344*m.b810 + 2*m.b344*m.b924 + 2*m.b345
                       *m.b589 - 2*m.b589 + 2*m.b345*m.b673 + 2*m.b346*m.b348 - 4*m.b348 + 2*m.b347*m.b348 - 4*m.b347 + 
                       2*m.b347*m.b531 + 2*m.b347*m.b589 + 2*m.b347*m.b719 + 2*m.b348*m.b425 + 2*m.b348*m.b594 - 4*
                       m.b594 + 2*m.b349*m.b350 + 2*m.b350*m.b594 + 2*m.b350*m.b890 - 2*m.b351*m.b352 - 2*m.b351*m.b615
                        - 2*m.b351*m.b760 + 2*m.b352*m.b430 - 2*m.b430 + 2*m.b352*m.b890 + 2*m.b353*m.b537 - 4*m.b537 + 
                       2*m.b353*m.b539 - 2*m.b354*m.b431 + 2*m.b354*m.b934 - 2*m.b355*m.b438 - 2*m.b438 + 2*m.b356*
                       m.b438 + 2*m.b357*m.b358 + 2*m.b358*m.b438 + 2*m.b358*m.b710 + 2*m.b359*m.b710 + 2*m.b359*m.b891
                        + 2*m.b359*m.b906 + 2*m.b360*m.b444 - 4*m.b444 - 2*m.b360*m.b655 + 2*m.b361*m.b363 + 2*m.b362*
                       m.b364 - 4*m.b364 + 2*m.b362*m.b841 + 2*m.b362*m.b873 + 2*m.b363*m.b364 + 2*m.b363*m.b444 + 2*
                       m.b364*m.b365 + 2*m.b364*m.b776 + 2*m.b365*m.b367 - 2*m.b367 + 2*m.b365*m.b711 - 2*m.b366*m.b503
                        + 2*m.b366*m.b738 + 2*m.b367*m.b503 - 2*m.b367*m.b739 + 2*m.b367*m.b866 - 2*m.b368*m.b560 + 2*
                       m.b368*m.b702 - 2*m.b368*m.b843 + 2*m.b369*m.b371 - 4*m.b371 + 2*m.b369*m.b450 + 2*m.b370*m.b371
                        + 2*m.b370*m.b702 + 2*m.b370*m.b860 + 2*m.b371*m.b634 + 2*m.b371*m.b797 - 2*m.b372*m.b374 + 4*
                       m.b372 + 2*m.b374 - 2*m.b372*m.b703 - 2*m.b372*m.b704 - 2*m.b372*m.b836 - 2*m.b373*m.b408 - 2*
                       m.b408 - 2*m.b373*m.b931 - 2*m.b374*m.b375 - 2*m.b375 + 2*m.b374*m.b931 - 2*m.b374*m.b936 + 2*
                       m.b375*m.b376 + 2*m.b375*m.b713 + 2*m.b375*m.b799 + 2*m.b376*m.b411 + 2*m.b376*m.b931 + 2*m.b377*
                       m.b578 - 4*m.b377 + 2*m.b377*m.b731 + 2*m.b377*m.b915 + 2*m.b377*m.b937 + 2*m.b378*m.b670 + 2*
                       m.b378*m.b837 - 2*m.b378*m.b854 + 2*m.b379*m.b731 - 2*m.b379 - 2*m.b379*m.b800 + 2*m.b379*m.b854
                        + 2*m.b379*m.b896 - 2*m.b380*m.b419 - 2*m.b380*m.b916 - 2*m.b381*m.b382 + 4*m.b381 - 2*m.b382 - 
                       2*m.b381*m.b418 - 2*m.b381*m.b680 - 2*m.b381*m.b681 + 2*m.b382*m.b383 + 2*m.b382*m.b802 + 2*
                       m.b382*m.b916 + 2*m.b383*m.b681 + 2*m.b383*m.b889 + 2*m.b384*m.b385 - 4*m.b385 - 2*m.b384*m.b855
                        + 2*m.b385*m.b387 - 2*m.b387 + 2*m.b385*m.b475 + 2*m.b385*m.b926 + 2*m.b386*m.b388 + 2*m.b387*
                       m.b388 + 2*m.b387*m.b532 - 4*m.b532 - 2*m.b387*m.b606 + 2*m.b388*m.b880 - 2*m.b389*m.b390 - 2*
                       m.b389*m.b620 - 2*m.b389*m.b749 + 2*m.b390*m.b479 - 2*m.b479 + 2*m.b390*m.b880 + 2*m.b391*m.b480
                        + 2*m.b391*m.b597 - 4*m.b597 + 2*m.b391*m.b599 + 2*m.b392*m.b621 + 2*m.b392*m.b939 - 2*m.b393*
                       m.b486 - 2*m.b486 + 2*m.b394*m.b486 + 2*m.b395*m.b396 - 2*m.b396 + 2*m.b396*m.b486 + 2*m.b396*
                       m.b700 - 2*m.b396*m.b848 + 2*m.b397*m.b398 - 2*m.b397*m.b623 + 2*m.b397*m.b824 + 2*m.b398*m.b700
                        + 2*m.b398*m.b899 + 2*m.b399*m.b494 - 4*m.b494 - 2*m.b399*m.b814 + 2*m.b400*m.b402 + 2*m.b400*
                       m.b912 + 2*m.b401*m.b555 - 2*m.b555 + 2*m.b401*m.b834 + 2*m.b401*m.b882 + 2*m.b402*m.b494 + 2*
                       m.b402*m.b555 - 2*m.b403*m.b449 + 2*m.b403*m.b750 + 2*m.b404*m.b689 + 2*m.b404*m.b867 + 2*m.b404*
                       m.b930 - 2*m.b405*m.b407 + 2*m.b405 + 2*m.b405*m.b567 - 4*m.b567 - 2*m.b405*m.b713 - 2*m.b405*
                       m.b827 - 2*m.b406*m.b458 - 2*m.b458 - 2*m.b406*m.b920 + 2*m.b407*m.b920 - 2*m.b407*m.b943 + 2*
                       m.b408*m.b410 + 2*m.b408*m.b727 + 2*m.b408*m.b790 + 2*m.b409*m.b742 + 2*m.b409*m.b789 - 2*m.b409*
                       m.b895 + 2*m.b410*m.b895 + 2*m.b410*m.b920 - 2*m.b411*m.b754 - 2*m.b411*m.b938 - 2*m.b412*m.b575
                        - 2*m.b575 - 2*m.b412*m.b729 + 2*m.b413*m.b414 - 4*m.b413 - 2*m.b414 + 2*m.b413*m.b518 + 2*
                       m.b413*m.b575 + 2*m.b413*m.b922 + 2*m.b414*m.b416 - 2*m.b416 - 2*m.b414*m.b636 + 2*m.b414*m.b716
                        - 2*m.b415*m.b417 - 2*m.b417 + 2*m.b415*m.b659 + 2*m.b416*m.b417 - 2*m.b416*m.b809 + 2*m.b416*
                       m.b887 + 2*m.b417*m.b746 + 2*m.b417*m.b845 + 2*m.b418*m.b887 - 2*m.b418*m.b911 - 2*m.b419*m.b420
                        - 2*m.b420 - 2*m.b419*m.b696 + 2*m.b420*m.b422 + 2*m.b420*m.b793 + 2*m.b420*m.b911 - 2*m.b421*
                       m.b718 + 2*m.b421 - 2*m.b421*m.b719 + 2*m.b421*m.b862 - 2*m.b421*m.b879 + 2*m.b422*m.b696 + 2*
                       m.b422*m.b879 + 2*m.b423*m.b424 - 4*m.b424 - 2*m.b423*m.b863 + 2*m.b424*m.b426 - 4*m.b426 + 2*
                       m.b424*m.b533 + 2*m.b424*m.b918 + 2*m.b425*m.b427 + 2*m.b426*m.b427 + 2*m.b426*m.b593 - 4*m.b593
                        + 2*m.b426*m.b606 + 2*m.b427*m.b871 - 2*m.b428*m.b538 - 2*m.b538 - 2*m.b428*m.b611 + 2*m.b429*
                       m.b538 - 2*m.b429*m.b736 + 2*m.b429*m.b871 + 2*m.b430*m.b432 + 2*m.b430*m.b539 - 2*m.b430*m.b620
                        + 2*m.b431*m.b434 + 2*m.b431*m.b611 + 2*m.b432*m.b434 + 2*m.b432*m.b538 + 2*m.b433*m.b435 - 2*
                       m.b435 + 2*m.b433*m.b628 + 2*m.b434*m.b435 - 2*m.b436*m.b543 - 2*m.b543 + 2*m.b437*m.b543 + 2*
                       m.b438*m.b439 - 2*m.b439 + 2*m.b439*m.b441 - 2*m.b441 + 2*m.b439*m.b543 - 2*m.b439*m.b840 + 2*
                       m.b440*m.b442 - 2*m.b440 - 2*m.b440*m.b631 + 2*m.b440*m.b820 + 2*m.b440*m.b892 + 2*m.b441*m.b442
                        - 2*m.b441*m.b685 + 2*m.b441*m.b698 + 2*m.b442*m.b893 + 2*m.b443*m.b551 - 4*m.b551 + 2*m.b443*
                       m.b655 - 2*m.b443*m.b820 + 2*m.b444*m.b446 + 2*m.b444*m.b906 + 2*m.b445*m.b498 - 2*m.b498 + 2*
                       m.b445*m.b825 + 2*m.b445*m.b873 + 2*m.b446*m.b498 + 2*m.b446*m.b551 - 2*m.b447*m.b686 + 2*m.b447
                        + 2*m.b447*m.b688 - 2*m.b447*m.b849 - 2*m.b447*m.b907 + 2*m.b448*m.b761 - 2*m.b448*m.b806 + 2*
                       m.b449*m.b901 - 2*m.b449*m.b942 + 2*m.b450*m.b452 - 2*m.b452 + 2*m.b450*m.b633 + 2*m.b451*m.b452
                        + 2*m.b451*m.b842 + 2*m.b451*m.b942 - 2*m.b452*m.b566 + 2*m.b452*m.b919 + 2*m.b453*m.b454 + 2*
                       m.b453 - 4*m.b454 - 2*m.b453*m.b565 - 2*m.b565 - 2*m.b453*m.b740 - 2*m.b453*m.b788 + 2*m.b454*
                       m.b456 - 4*m.b456 + 2*m.b454*m.b511 + 2*m.b511 + 2*m.b454*m.b919 + 2*m.b455*m.b510 + 2*m.b455 - 4
                       *m.b510 - 2*m.b455*m.b727 - 2*m.b455*m.b822 - 2*m.b455*m.b823 + 2*m.b456*m.b634 + 2*m.b456*m.b678
                        + 2*m.b456*m.b823 - 2*m.b457*m.b513 - 2*m.b457*m.b692 - 2*m.b457*m.b914 + 2*m.b458*m.b459 + 2*
                       m.b458*m.b741 + 2*m.b458*m.b779 + 2*m.b459*m.b886 + 2*m.b459*m.b914 - 2*m.b460*m.b767 - 2*m.b460*
                       m.b933 - 2*m.b461*m.b742 - 2*m.b461*m.b791 + 2*m.b462*m.b463 - 4*m.b462 + 2*m.b463 + 2*m.b462*
                       m.b464 - 2*m.b464 + 2*m.b462*m.b791 + 2*m.b462*m.b932 - 2*m.b463*m.b465 - 2*m.b463*m.b770 - 2*
                       m.b463*m.b878 + 2*m.b464*m.b465 - 2*m.b464*m.b649 + 2*m.b464*m.b707 + 2*m.b465*m.b466 - 2*m.b466
                        + 2*m.b466*m.b468 - 2*m.b468 - 2*m.b466*m.b801 + 2*m.b466*m.b838 + 2*m.b467*m.b896 - 2*m.b467*
                       m.b904 + 2*m.b468*m.b585 + 2*m.b585 - 2*m.b468*m.b662 + 2*m.b468*m.b904 - 2*m.b469*m.b470 - 2*
                       m.b470 + 2*m.b469*m.b584 - 2*m.b584 - 2*m.b469*m.b708 + 2*m.b470*m.b472 + 2*m.b470*m.b783 + 2*
                       m.b470*m.b904 - 2*m.b471*m.b733 - 2*m.b471*m.b734 - 2*m.b471*m.b870 + 2*m.b472*m.b708 + 2*m.b472*
                       m.b870 + 2*m.b473*m.b592 - 2*m.b592 - 2*m.b473*m.b870 + 2*m.b474*m.b592 + 2*m.b474*m.b870 + 2*
                       m.b474*m.b917 + 2*m.b475*m.b476 - 2*m.b476 + 2*m.b476*m.b639 + 2*m.b476*m.b864 - 2*m.b476*m.b945
                        - 2*m.b477*m.b598 - 2*m.b598 + 2*m.b478*m.b598 - 2*m.b478*m.b720 + 2*m.b478*m.b864 + 2*m.b479*
                       m.b480 + 2*m.b479*m.b481 - 2*m.b479*m.b615 - 2*m.b480*m.b940 + 2*m.b481*m.b598 + 2*m.b481*m.b940
                        + 2*m.b482*m.b483 - 2*m.b483 + 2*m.b482*m.b640 + 2*m.b483*m.b940 - 2*m.b484*m.b819 + 2*m.b485*
                       m.b819 + 2*m.b486*m.b488 - 4*m.b488 + 2*m.b487*m.b490 + 2*m.b487*m.b683 - 2*m.b487*m.b710 + 2*
                       m.b488*m.b490 + 2*m.b488*m.b819 + 2*m.b488*m.b840 + 2*m.b489*m.b492 - 2*m.b489*m.b642 + 2*m.b489*
                       m.b814 + 2*m.b490*m.b492 - 2*m.b491*m.b613 + 2*m.b491 - 2*m.b491*m.b840 + 2*m.b491*m.b881 - 2*
                       m.b491*m.b883 + 2*m.b492*m.b883 + 2*m.b493*m.b495 - 2*m.b495 - 2*m.b493*m.b824 + 2*m.b494*m.b497
                        - 2*m.b497 + 2*m.b494*m.b899 + 2*m.b495*m.b497 - 2*m.b495*m.b624 + 2*m.b495*m.b883 + 2*m.b496*
                       m.b499 - 4*m.b499 + 2*m.b496*m.b882 + 2*m.b497*m.b499 - 2*m.b497*m.b644 + 2*m.b498*m.b750 - 2*
                       m.b498*m.b944 + 2*m.b499*m.b738 + 2*m.b499*m.b944 - 2*m.b500*m.b502 - 2*m.b500*m.b701 - 2*m.b500*
                       m.b841 + 2*m.b501*m.b776 - 2*m.b501*m.b796 + 2*m.b502*m.b796 + 2*m.b502*m.b944 - 2*m.b503*m.b935
                        + 2*m.b504*m.b507 - 2*m.b507 + 2*m.b504*m.b868 + 2*m.b505*m.b507 - 2*m.b505 - 2*m.b505*m.b666 + 
                       2*m.b505*m.b850 + 2*m.b505*m.b935 - 2*m.b506*m.b913 - 2*m.b507*m.b508 + 2*m.b507*m.b913 + 2*
                       m.b508*m.b510 - 2*m.b508*m.b726 + 2*m.b509*m.b568 - 2*m.b509 + 2*m.b509*m.b763 + 2*m.b509*m.b930
                        - 2*m.b509*m.b943 + 2*m.b510*m.b913 + 2*m.b510*m.b943 - 2*m.b511*m.b741 - 2*m.b511*m.b815 - 2*
                       m.b511*m.b816 - 2*m.b512*m.b570 - 2*m.b512*m.b705 - 2*m.b512*m.b909 + 2*m.b513*m.b514 + 2*m.b513*
                       m.b766 + 2*m.b514*m.b876 + 2*m.b514*m.b909 - 2*m.b515*m.b753 - 2*m.b515*m.b781 - 2*m.b516*m.b519
                        - 2*m.b519 - 2*m.b516*m.b657 - 2*m.b516*m.b659 + 2*m.b517*m.b519 - 4*m.b517 + 2*m.b517*m.b781 + 
                       2*m.b517*m.b809 + 2*m.b517*m.b937 - 2*m.b518*m.b520 - 2*m.b518*m.b782 + 2*m.b519*m.b520 + 2*
                       m.b519*m.b695 + 2*m.b520*m.b522 - 2*m.b522 - 2*m.b521*m.b524 + 2*m.b521 - 2*m.b524 - 2*m.b521*
                       m.b672 - 2*m.b521*m.b716 + 2*m.b521*m.b717 + 2*m.b522*m.b524 - 2*m.b522*m.b792 + 2*m.b522*m.b828
                        - 2*m.b523*m.b896 - 2*m.b523*m.b897 + 2*m.b524*m.b525 + 2*m.b525 + 2*m.b524*m.b897 - 2*m.b525*
                       m.b526 - 2*m.b526 - 2*m.b525*m.b718 - 2*m.b525*m.b771 + 2*m.b526*m.b528 + 2*m.b526*m.b772 + 2*
                       m.b526*m.b897 - 2*m.b527*m.b603 + 4*m.b527 - 2*m.b527*m.b747 - 2*m.b527*m.b862 - 2*m.b527*m.b863
                        + 2*m.b528*m.b718 + 2*m.b528*m.b863 + 2*m.b529*m.b532 - 2*m.b529*m.b879 + 2*m.b530*m.b532 + 2*
                       m.b530*m.b863 + 2*m.b530*m.b925 + 2*m.b531*m.b534 + 2*m.b532*m.b534 + 2*m.b533*m.b535 + 2*m.b534*
                       m.b535 + 2*m.b535*m.b856 + 2*m.b536*m.b639 - 2*m.b536*m.b641 + 2*m.b537*m.b641 + 2*m.b537*m.b720
                        + 2*m.b537*m.b856 + 2*m.b538*m.b540 - 2*m.b539*m.b601 + 2*m.b601 + 2*m.b540*m.b601 + 2*m.b540*
                       m.b641 - 2*m.b541*m.b813 + 2*m.b542*m.b813 + 2*m.b543*m.b545 - 4*m.b545 + 2*m.b544*m.b547 - 2*
                       m.b544*m.b723 + 2*m.b545*m.b547 + 2*m.b545*m.b813 + 2*m.b545*m.b848 + 2*m.b546*m.b549 - 2*m.b546*
                       m.b653 + 2*m.b547*m.b549 - 2*m.b548*m.b608 + 2*m.b548 - 2*m.b548*m.b848 + 2*m.b548*m.b872 - 2*
                       m.b548*m.b874 + 2*m.b549*m.b874 + 2*m.b550*m.b552 - 2*m.b552 - 2*m.b550*m.b832 + 2*m.b551*m.b554
                        - 4*m.b554 + 2*m.b551*m.b893 + 2*m.b552*m.b554 - 2*m.b552*m.b618 + 2*m.b552*m.b874 + 2*m.b553*
                       m.b556 - 4*m.b556 + 2*m.b554*m.b556 + 2*m.b554*m.b644 + 2*m.b555*m.b761 - 2*m.b555*m.b941 + 2*
                       m.b556*m.b724 + 2*m.b556*m.b941 - 2*m.b557*m.b559 + 4*m.b557 - 2*m.b557*m.b688 - 2*m.b557*m.b711
                        - 2*m.b557*m.b834 - 2*m.b558*m.b787 + 2*m.b559*m.b787 + 2*m.b559*m.b941 - 2*m.b560*m.b929 + 2*
                       m.b561*m.b563 - 2*m.b561 - 4*m.b563 + 2*m.b561*m.b675 - 2*m.b561*m.b859 + 2*m.b561*m.b860 + 2*
                       m.b562*m.b565 + 2*m.b562*m.b861 + 2*m.b563*m.b565 + 2*m.b563*m.b666 + 2*m.b563*m.b929 - 2*m.b564*
                       m.b843 - 2*m.b564*m.b908 + 2*m.b565*m.b908 + 2*m.b566*m.b567 + 2*m.b567*m.b908 + 2*m.b567*m.b936
                        - 2*m.b568*m.b807 - 2*m.b569*m.b610 - 2*m.b569*m.b714 - 2*m.b569*m.b902 + 2*m.b570*m.b571 + 2*
                       m.b570*m.b572 - 2*m.b571*m.b753 - 2*m.b571*m.b869 + 2*m.b572*m.b869 + 2*m.b572*m.b902 + 2*m.b573*
                       m.b657 + 2*m.b573*m.b729 - 2*m.b573*m.b768 + 2*m.b574*m.b768 - 2*m.b574 + 2*m.b574*m.b869 - 2*
                       m.b574*m.b915 + 2*m.b574*m.b921 + 2*m.b575*m.b577 - 4*m.b577 + 2*m.b575*m.b938 - 2*m.b576*m.b579
                        - 2*m.b576*m.b668 - 2*m.b576*m.b670 + 2*m.b577*m.b579 + 2*m.b577*m.b768 + 2*m.b577*m.b800 - 2*
                       m.b578*m.b580 - 2*m.b578*m.b792 + 2*m.b579*m.b580 + 2*m.b580*m.b582 - 2*m.b582 - 2*m.b581*m.b584
                        - 2*m.b581*m.b680 - 2*m.b581*m.b707 + 2*m.b582*m.b583 + 2*m.b582*m.b584 - 2*m.b582*m.b782 - 2*
                       m.b583*m.b887 - 2*m.b583*m.b888 + 2*m.b584*m.b888 - 2*m.b585*m.b586 - 2*m.b586 - 2*m.b585*m.b733
                        - 2*m.b585*m.b757 + 2*m.b586*m.b587 + 2*m.b586*m.b588 + 2*m.b586*m.b888 - 2*m.b587*m.b855 + 2*
                       m.b588*m.b733 + 2*m.b588*m.b855 + 2*m.b589*m.b591 - 2*m.b589*m.b748 + 2*m.b590*m.b593 - 2*m.b590*
                       m.b889 + 2*m.b591*m.b593 + 2*m.b591*m.b855 + 2*m.b592*m.b594 - 2*m.b592*m.b945 + 2*m.b593*m.b945
                        + 2*m.b594*m.b595 + 2*m.b595*m.b596 - 2*m.b596 + 2*m.b595*m.b945 + 2*m.b596*m.b597 - 2*m.b596*
                       m.b785 + 2*m.b596*m.b846 + 2*m.b597*m.b629 + 2*m.b597*m.b736 + 2*m.b598*m.b600 - 2*m.b599*m.b928
                        + 2*m.b600*m.b629 + 2*m.b600*m.b928 - 2*m.b601*m.b934 - 2*m.b601*m.b946 - 2*m.b602*m.b603 + 2*
                       m.b602*m.b719 - 2*m.b604*m.b605 + 2*m.b604*m.b729 + 2*m.b605*m.b730 - 2*m.b605*m.b885 - 2*m.b606*
                       m.b674 - 2*m.b607*m.b608 - 2*m.b607*m.b614 + 2*m.b607*m.b618 + 2*m.b608*m.b699 - 2*m.b609*m.b610
                        + 2*m.b610*m.b743 + 2*m.b611*m.b612 - 2*m.b611*m.b621 - 2*m.b612*m.b629 + 2*m.b613*m.b685 + 2*
                       m.b614*m.b686 + 2*m.b615*m.b674 - 2*m.b616*m.b617 - 2*m.b617*m.b891 + 2*m.b618*m.b701 + 2*m.b619*
                       m.b726 - 2*m.b622*m.b623 + 2*m.b622*m.b685 + 2*m.b624*m.b711 + 2*m.b625*m.b740 - 2*m.b626*m.b627
                        - 2*m.b626*m.b770 + 2*m.b626*m.b782 - 2*m.b627*m.b731 - 2*m.b628*m.b629 - 2*m.b630*m.b631 - 2*
                       m.b630*m.b655 + 2*m.b630*m.b699 - 2*m.b632*m.b633 + 2*m.b632*m.b752 - 2*m.b633*m.b875 - 2*m.b634*
                       m.b728 - 2*m.b635*m.b636 - 2*m.b635*m.b756 + 2*m.b635*m.b792 - 2*m.b637*m.b638 + 2*m.b637*m.b682
                        + 2*m.b638*m.b695 + 2*m.b638*m.b756 - 2*m.b638*m.b757 - 2*m.b639*m.b811 - 2*m.b639*m.b847 - 2*
                       m.b640*m.b641 - 2*m.b643*m.b813 - 2*m.b643*m.b865 - 2*m.b644*m.b762 - 2*m.b645*m.b646 + 2*m.b646*
                       m.b687 - 2*m.b646*m.b866 + 2*m.b646*m.b867 - 2*m.b647*m.b714 - 2*m.b648*m.b649 + 2*m.b648*m.b650
                        - 2*m.b648*m.b745 + 2*m.b648*m.b801 + 2*m.b649*m.b668 - 2*m.b650*m.b768 - 2*m.b650*m.b769 - 2*
                       m.b651*m.b652 + 2*m.b651*m.b697 + 2*m.b652*m.b707 + 2*m.b652*m.b745 - 2*m.b652*m.b746 - 2*m.b654*
                       m.b819 - 2*m.b656*m.b705 - 2*m.b657*m.b658 + 2*m.b659*m.b660 - 2*m.b659*m.b732 - 2*m.b660*m.b781
                        - 2*m.b661*m.b662 + 2*m.b662*m.b716 + 2*m.b662*m.b732 - 2*m.b664*m.b665 - 2*m.b664*m.b850 - 2*
                       m.b665*m.b738 + 2*m.b665*m.b739 - 2*m.b667*m.b692 - 2*m.b668*m.b669 + 2*m.b670*m.b671 - 2*m.b670*
                       m.b717 - 2*m.b671*m.b791 - 2*m.b673*m.b773 + 2*m.b674*m.b805 - 2*m.b675*m.b676 - 2*m.b675*m.b842
                        - 2*m.b676*m.b724 + 2*m.b676*m.b725 - 2*m.b679*m.b915 + 2*m.b681*m.b682 - 2*m.b681*m.b758 - 2*
                       m.b682*m.b838 + 2*m.b683*m.b684 - 2*m.b683*m.b698 - 2*m.b687*m.b688 - 2*m.b687*m.b835 + 2*m.b689*
                       m.b835 - 2*m.b689*m.b942 + 2*m.b691*m.b692 + 2*m.b692*m.b853 - 2*m.b693*m.b922 - 2*m.b694*m.b869
                        - 2*m.b694*m.b877 - 2*m.b695*m.b755 + 2*m.b696*m.b697 - 2*m.b696*m.b748 - 2*m.b697*m.b845 - 2*
                       m.b698*m.b700 - 2*m.b699*m.b700 - 2*m.b702*m.b935 + 2*m.b704*m.b705 - 2*m.b704*m.b798 + 2*m.b705*
                       m.b844 + 2*m.b706*m.b753 - 2*m.b706*m.b932 - 2*m.b707*m.b744 - 2*m.b708*m.b735 - 2*m.b709*m.b710
                        + 2*m.b712*m.b821 - 2*m.b712*m.b929 + 2*m.b713*m.b714 - 2*m.b713*m.b789 + 2*m.b714*m.b836 + 2*
                       m.b715*m.b742 - 2*m.b715*m.b937 - 2*m.b716*m.b731 - 2*m.b719*m.b784 - 2*m.b720*m.b721 - 2*m.b721*
                       m.b890 - 2*m.b722*m.b723 - 2*m.b724*m.b825 - 2*m.b725*m.b901 + 2*m.b727*m.b728 - 2*m.b727*m.b778
                        + 2*m.b728*m.b827 - 2*m.b728*m.b885 - 2*m.b729*m.b730 + 2*m.b730*m.b778 - 2*m.b730*m.b886 + 2*
                       m.b734*m.b735 - 2*m.b734*m.b774 - 2*m.b735*m.b889 - 2*m.b736*m.b737 - 2*m.b737*m.b880 + 2*m.b739*
                       m.b849 - 2*m.b741*m.b765 - 2*m.b742*m.b743 + 2*m.b743*m.b765 - 2*m.b743*m.b876 + 2*m.b744*m.b903
                        - 2*m.b745*m.b800 + 2*m.b746*m.b911 + 2*m.b747*m.b748 - 2*m.b747*m.b759 - 2*m.b749*m.b871 + 2*
                       m.b751*m.b841 - 2*m.b752*m.b763 + 2*m.b753*m.b754 + 2*m.b754*m.b798 - 2*m.b754*m.b902 + 2*m.b755*
                       m.b910 - 2*m.b756*m.b809 + 2*m.b757*m.b854 + 2*m.b757*m.b916 - 2*m.b758*m.b925 - 2*m.b760*m.b864
                        + 2*m.b762*m.b834 - 2*m.b762*m.b884 - 2*m.b763*m.b797 + 2*m.b764*m.b797 - 2*m.b765*m.b766 - 2*
                       m.b767*m.b909 + 2*m.b771*m.b924 - 2*m.b773*m.b917 - 2*m.b775*m.b856 + 2*m.b777*m.b788 - 2*m.b778*
                       m.b779 - 2*m.b780*m.b914 - 2*m.b780*m.b921 + 2*m.b781*m.b923 - 2*m.b786*m.b818 + 2*m.b787*m.b929
                        - 2*m.b788*m.b930 - 2*m.b789*m.b790 + 2*m.b791*m.b933 - 2*m.b794*m.b812 + 2*m.b796*m.b935 - 2*
                       m.b797*m.b936 - 2*m.b798*m.b799 + 2*m.b800*m.b878 - 2*m.b801*m.b837 - 2*m.b803*m.b804 - 2*m.b803*
                       m.b805 + 2*m.b806*m.b907 + 2*m.b806*m.b942 + 2*m.b807*m.b902 + 2*m.b807*m.b936 + 2*m.b814*m.b865
                        - 2*m.b814*m.b912 + 2*m.b816*m.b909 + 2*m.b816*m.b943 - 2*m.b820*m.b906 + 2*m.b821*m.b851 - 2*
                       m.b821*m.b930 + 2*m.b823*m.b914 + 2*m.b824*m.b848 - 2*m.b824*m.b899 + 2*m.b826*m.b843 - 2*m.b826*
                       m.b919 + 2*m.b829*m.b830 - 2*m.b829*m.b831 - 2*m.b830*m.b880 + 2*m.b832*m.b840 + 2*m.b832*m.b891
                        - 2*m.b832*m.b893 - 2*m.b833*m.b834 - 2*m.b839*m.b890 + 2*m.b842*m.b843 - 2*m.b846*m.b856 - 2*
                       m.b847*m.b898 + 2*m.b850*m.b851 - 2*m.b851*m.b852 - 2*m.b857*m.b905 + 2*m.b858*m.b865 - 2*m.b859*
                       m.b900 + 2*m.b859*m.b901 - 2*m.b860*m.b861 - 2*m.b866*m.b894 - 2*m.b867*m.b868 - 2*m.b873*m.b874
                        - 2*m.b875*m.b884 + 2*m.b876*m.b923 - 2*m.b877*m.b878 + 2*m.b879*m.b918 - 2*m.b882*m.b883 + 2*
                       m.b886*m.b933 - 2*m.b887*m.b910 + 2*m.b889*m.b926 - 2*m.b891*m.b892 + 2*m.b895*m.b938 - 2*m.b896*
                       m.b903 - 2*m.b901*m.b941 - 2*m.b907*m.b944 - 2*m.b917*m.b918 - 2*m.b921*m.b923 - 2*m.b922*m.b923
                        - 2*m.b925*m.b926 - 2*m.b927*m.b928 + 2*m.b928*m.b946 - 2*m.b932*m.b933 - 2*m.b937*m.b938 - 2*
                       m.b939*m.b940 + m.x947 <= 0)
