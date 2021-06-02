#  MINLP written by GAMS Convert at 04/21/18 13:54:17
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        562        1      561        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        562        1      561        0


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
m.x562 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x562, sense=maximize)

m.c1 = Constraint(expr=(-2*m.b1*m.b227) - 2*m.b1 + 2*m.b227 + 2*m.b1*m.b265 - 2*m.b265 + 2*m.b1*m.b360 + 2*m.b1*m.b373
                        - 2*m.b2*m.b38 + 2*m.b2 + 2*m.b38 - 2*m.b2*m.b314 - 2*m.b314 - 2*m.b2*m.b361 + 2*m.b2*m.b419 + 2
                       *m.b3*m.b362 - 2*m.b3 + 2*m.b3*m.b406 - 2*m.b4*m.b32 + 2*m.b4 + 2*m.b32 - 2*m.b4*m.b274 - 2*
                       m.b274 - 2*m.b4*m.b358 + 2*m.b4*m.b429 + 2*m.b5*m.b65 - 2*m.b5 - 2*m.b65 + 2*m.b5*m.b371 - 2*m.b5
                       *m.b409 + 2*m.b5*m.b410 + 2*m.b6*m.b271 - 2*m.b6 - 2*m.b271 + 2*m.b6*m.b359 + 2*m.b7*m.b66 - 2*
                       m.b7 - 2*m.b66 + 2*m.b7*m.b366 - 2*m.b7*m.b415 + 2*m.b7*m.b416 + 2*m.b8*m.b62 - 2*m.b8 - 2*m.b62
                        + 2*m.b8*m.b311 - 2*m.b311 + 2*m.b9*m.b100 - 2*m.b9 - 2*m.b100 + 2*m.b9*m.b361 - 2*m.b9*m.b396
                        + 2*m.b9*m.b397 + 2*m.b10*m.b85 - 2*m.b10 - 2*m.b85 + 2*m.b10*m.b367 + 2*m.b10*m.b379 - 2*m.b10*
                       m.b423 + 2*m.b11*m.b48 - 2*m.b11 - 2*m.b48 + 2*m.b11*m.b362 + 2*m.b12*m.b106 - 2*m.b12 - 2*m.b106
                        - 2*m.b12*m.b245 + 2*m.b245 + 2*m.b12*m.b371 + 2*m.b12*m.b372 + 2*m.b13*m.b184 - 2*m.b13 - 2*
                       m.b184 - 2*m.b13*m.b247 + 2*m.b247 + 2*m.b13*m.b288 - 4*m.b288 + 2*m.b13*m.b402 + 2*m.b14*m.b124
                        - 2*m.b14 - 2*m.b124 - 2*m.b14*m.b285 + 2*m.b285 + 2*m.b14*m.b366 + 2*m.b14*m.b380 + 2*m.b15*
                       m.b154 - 2*m.b15 - 2*m.b154 - 2*m.b15*m.b287 + 4*m.b287 + 2*m.b15*m.b331 - 4*m.b331 + 2*m.b15*
                       m.b334 + 2*m.b334 + 2*m.b16*m.b89 - 2*m.b16 - 2*m.b89 - 2*m.b16*m.b338 + 2*m.b338 + 2*m.b16*
                       m.b446 + 2*m.b16*m.b447 + 2*m.b17*m.b25 - 2*m.b17 - 2*m.b25 + 2*m.b17*m.b268 - 4*m.b268 + 2*m.b18
                       *m.b109 - 2*m.b18 - 4*m.b109 - 2*m.b18*m.b456 + 2*m.b18*m.b457 + 2*m.b18*m.b458 + 2*m.b19*m.b243
                        - 2*m.b19 - 2*m.b243 + 2*m.b19*m.b327 - 2*m.b327 + 2*m.b19*m.b415 - 2*m.b19*m.b453 + 2*m.b20*
                       m.b71 - 2*m.b20 - 2*m.b71 + 2*m.b20*m.b129 - 4*m.b129 + 2*m.b20*m.b158 - 2*m.b158 - 2*m.b20*
                       m.b463 + 2*m.b21*m.b36 - 2*m.b21 - 2*m.b36 + 2*m.b21*m.b465 - 2*m.b22*m.b242 - 2*m.b22 + 2*m.b242
                        + 2*m.b22*m.b284 - 4*m.b284 + 2*m.b22*m.b285 + 2*m.b22*m.b409 + 2*m.b23*m.b89 - 2*m.b23 + 2*
                       m.b23*m.b159 - 4*m.b159 + 2*m.b23*m.b186 - 4*m.b186 - 2*m.b23*m.b469 - 2*m.b24*m.b71 - 2*m.b24 + 
                       2*m.b24*m.b73 - 4*m.b73 + 2*m.b24*m.b159 + 2*m.b24*m.b470 + 2*m.b25*m.b26 - 2*m.b26 - 2*m.b25*
                       m.b59 - 2*m.b59 + 2*m.b25*m.b113 - 4*m.b113 + 2*m.b26*m.b46 - 2*m.b46 + 2*m.b27*m.b245 - 2*m.b27
                        - 2*m.b27*m.b283 + 2*m.b283 + 2*m.b27*m.b326 - 4*m.b326 + 2*m.b27*m.b400 + 2*m.b28*m.b109 - 2*
                       m.b28 + 2*m.b28*m.b187 - 4*m.b187 + 2*m.b28*m.b220 - 4*m.b220 - 2*m.b28*m.b476 + 2*m.b29*m.b43 - 
                       2*m.b29 - 2*m.b43 + 2*m.b29*m.b91 - 4*m.b91 + 2*m.b29*m.b187 - 2*m.b29*m.b458 + 2*m.b30*m.b31 - 2
                       *m.b30 - 2*m.b31 - 2*m.b30*m.b45 - 2*m.b45 + 2*m.b30*m.b139 - 4*m.b139 + 2*m.b30*m.b478 + 2*m.b31
                       *m.b60 - 4*m.b60 + 2*m.b32*m.b63 + 2*m.b63 - 2*m.b32*m.b118 + 4*m.b118 - 2*m.b32*m.b316 - 2*
                       m.b316 + 2*m.b33*m.b129 - 4*m.b33 + 2*m.b33*m.b221 - 4*m.b221 + 2*m.b33*m.b257 - 4*m.b257 + 2*
                       m.b33*m.b476 + 2*m.b34*m.b55 - 2*m.b34 - 4*m.b55 + 2*m.b34*m.b111 - 4*m.b111 + 2*m.b34*m.b221 - 2
                       *m.b34*m.b447 - 2*m.b35*m.b36 - 2*m.b35 + 2*m.b35*m.b58 - 2*m.b58 + 2*m.b35*m.b77 - 4*m.b77 + 2*
                       m.b35*m.b493 + 2*m.b36*m.b37 - 2*m.b37 + 2*m.b36*m.b167 - 4*m.b167 + 2*m.b37*m.b77 - 2*m.b38*
                       m.b145 + 4*m.b145 - 2*m.b38*m.b276 - 2*m.b276 + 2*m.b38*m.b387 + 2*m.b39*m.b40 - 2*m.b39 - 2*
                       m.b40 + 2*m.b39*m.b67 - 2*m.b67 + 2*m.b39*m.b153 - 4*m.b153 - 2*m.b39*m.b411 + 2*m.b40*m.b68 - 2*
                       m.b68 + 2*m.b40*m.b444 - 2*m.b40*m.b512 + 2*m.b41*m.b159 - 4*m.b41 + 2*m.b41*m.b258 - 2*m.b258 + 
                       2*m.b41*m.b297 - 4*m.b297 + 2*m.b41*m.b469 + 2*m.b42*m.b73 - 4*m.b42 + 2*m.b42*m.b131 - 4*m.b131
                        + 2*m.b42*m.b258 + 2*m.b42*m.b447 + 2*m.b43*m.b301 - 4*m.b301 + 2*m.b43*m.b459 - 2*m.b43*m.b477
                        + 2*m.b44*m.b45 - 2*m.b44 - 2*m.b44*m.b57 + 2*m.b57 + 2*m.b44*m.b495 + 2*m.b44*m.b503 + 2*m.b45*
                       m.b75 - 4*m.b75 + 2*m.b45*m.b95 - 4*m.b95 + 2*m.b46*m.b47 - 2*m.b47 + 2*m.b46*m.b351 - 2*m.b351
                        - 2*m.b46*m.b495 + 2*m.b47*m.b95 + 2*m.b48*m.b361 + 2*m.b48*m.b460 - 2*m.b48*m.b516 + 2*m.b49*
                       m.b398 - 2*m.b49 + 2*m.b49*m.b419 + 2*m.b49*m.b511 - 2*m.b49*m.b518 + 2*m.b50*m.b52 - 4*m.b50 - 4
                       *m.b52 + 2*m.b50*m.b401 + 2*m.b50*m.b418 + 2*m.b50*m.b506 + 2*m.b51*m.b88 + 2*m.b51 - 4*m.b88 - 2
                       *m.b51*m.b294 + 2*m.b294 - 2*m.b51*m.b296 + 2*m.b296 - 2*m.b51*m.b354 + 2*m.b52*m.b296 + 2*m.b52*
                       m.b354 + 2*m.b52*m.b444 + 2*m.b53*m.b187 - 4*m.b53 + 2*m.b53*m.b299 - 2*m.b299 + 2*m.b53*m.b339
                        - 4*m.b339 + 2*m.b53*m.b463 + 2*m.b54*m.b91 - 4*m.b54 + 2*m.b54*m.b161 - 4*m.b161 + 2*m.b54*
                       m.b299 + 2*m.b54*m.b458 + 2*m.b55*m.b132 - 4*m.b132 + 2*m.b55*m.b448 + 2*m.b55*m.b471 - 2*m.b56*
                       m.b57 - 2*m.b56 + 2*m.b56*m.b355 + 2*m.b56*m.b360 + 2*m.b56*m.b472 + 2*m.b57*m.b93 - 4*m.b93 - 2*
                       m.b57*m.b520 + 2*m.b58*m.b59 + 2*m.b58*m.b136 - 2*m.b136 - 2*m.b58*m.b508 + 2*m.b59*m.b93 + 2*
                       m.b59*m.b114 - 4*m.b114 + 2*m.b60*m.b61 - 2*m.b61 + 2*m.b60*m.b308 - 2*m.b308 + 2*m.b60*m.b495 + 
                       2*m.b61*m.b114 + 2*m.b62*m.b358 + 2*m.b62*m.b449 - 2*m.b62*m.b521 - 2*m.b63*m.b317 + 2*m.b317 - 2
                       *m.b63*m.b375 - 2*m.b63*m.b504 + 2*m.b64*m.b203 - 4*m.b64 - 4*m.b203 + 2*m.b64*m.b408 + 2*m.b64*
                       m.b429 + 2*m.b64*m.b504 + 2*m.b65*m.b123 - 4*m.b123 + 2*m.b65*m.b489 - 2*m.b65*m.b525 + 2*m.b66*
                       m.b500 - 2*m.b66*m.b524 + 2*m.b66*m.b525 + 2*m.b67*m.b69 - 4*m.b69 + 2*m.b67*m.b154 - 2*m.b67*
                       m.b185 + 4*m.b185 + 2*m.b68*m.b392 + 2*m.b68*m.b412 - 2*m.b68*m.b513 + 2*m.b69*m.b425 + 2*m.b69*
                       m.b502 + 2*m.b69*m.b513 + 2*m.b70*m.b221 - 2*m.b70 + 2*m.b70*m.b341 - 2*m.b341 - 2*m.b70*m.b354
                        + 2*m.b70*m.b456 + 2*m.b71*m.b72 - 4*m.b72 + 2*m.b71*m.b435 + 2*m.b72*m.b111 + 2*m.b72*m.b190 - 
                       4*m.b190 + 2*m.b72*m.b341 + 2*m.b73*m.b437 + 2*m.b73*m.b477 + 2*m.b74*m.b112 + 2*m.b74 - 4*m.b112
                        - 2*m.b74*m.b405 - 2*m.b74*m.b493 - 2*m.b74*m.b529 + 2*m.b75*m.b76 - 2*m.b76 + 2*m.b75*m.b165 - 
                       2*m.b165 + 2*m.b75*m.b508 + 2*m.b76*m.b112 + 2*m.b76*m.b140 - 2*m.b140 - 2*m.b76*m.b465 + 2*m.b77
                       *m.b78 - 2*m.b78 + 2*m.b77*m.b266 - 4*m.b266 + 2*m.b78*m.b140 + 2*m.b79*m.b117 - 2*m.b79 - 2*
                       m.b117 - 2*m.b79*m.b143 - 2*m.b143 + 2*m.b79*m.b235 - 4*m.b235 + 2*m.b79*m.b272 - 2*m.b272 - 2*
                       m.b80*m.b386 + 2*m.b80 + 2*m.b80*m.b397 - 2*m.b80*m.b497 - 2*m.b80*m.b498 + 2*m.b81*m.b413 - 4*
                       m.b81 + 2*m.b81*m.b439 + 2*m.b81*m.b498 + 2*m.b81*m.b518 + 2*m.b82*m.b104 - 2*m.b82 - 2*m.b104 + 
                       2*m.b82*m.b147 - 4*m.b147 + 2*m.b82*m.b369 - 2*m.b82*m.b461 + 2*m.b83*m.b85 - 4*m.b83 + 2*m.b83*
                       m.b368 + 2*m.b83*m.b391 + 2*m.b83*m.b501 + 2*m.b84*m.b105 - 2*m.b84 - 4*m.b105 - 2*m.b84*m.b150
                        - 2*m.b150 + 2*m.b84*m.b399 + 2*m.b84*m.b480 + 2*m.b85*m.b150 - 2*m.b85*m.b532 + 2*m.b86*m.b150
                        - 4*m.b86 + 2*m.b86*m.b152 - 2*m.b152 + 2*m.b86*m.b247 + 2*m.b86*m.b390 + 2*m.b87*m.b88 - 2*
                       m.b87 + 2*m.b87*m.b126 - 2*m.b126 - 2*m.b87*m.b218 + 4*m.b218 + 2*m.b87*m.b402 + 2*m.b88*m.b492
                        + 2*m.b88*m.b507 + 2*m.b89*m.b90 - 2*m.b90 - 2*m.b89*m.b471 + 2*m.b90*m.b131 + 2*m.b90*m.b223 - 
                       4*m.b223 - 2*m.b90*m.b342 - 2*m.b342 + 2*m.b91*m.b428 + 2*m.b91*m.b472 + 2*m.b92*m.b132 - 2*m.b92
                        + 2*m.b92*m.b227 + 2*m.b92*m.b346 - 4*m.b346 - 2*m.b92*m.b494 + 2*m.b93*m.b94 - 4*m.b94 + 2*
                       m.b93*m.b195 - 2*m.b195 + 2*m.b94*m.b137 - 4*m.b137 + 2*m.b94*m.b168 - 2*m.b168 + 2*m.b94*m.b465
                        + 2*m.b95*m.b96 - 2*m.b96 + 2*m.b95*m.b309 - 4*m.b309 + 2*m.b96*m.b168 + 2*m.b97*m.b98 - 2*m.b97
                        - 2*m.b98 + 2*m.b97*m.b394 + 2*m.b98*m.b170 - 2*m.b170 + 2*m.b98*m.b200 - 2*m.b200 - 2*m.b98*
                       m.b516 - 2*m.b99*m.b116 - 2*m.b99 - 2*m.b116 + 2*m.b99*m.b275 - 4*m.b275 + 2*m.b99*m.b312 - 2*
                       m.b312 + 2*m.b99*m.b509 + 2*m.b100*m.b102 - 4*m.b102 - 2*m.b100*m.b144 - 2*m.b144 + 2*m.b100*
                       m.b450 - 2*m.b101*m.b397 + 4*m.b101 - 2*m.b101*m.b398 - 2*m.b101*m.b486 - 2*m.b101*m.b487 + 2*
                       m.b102*m.b420 + 2*m.b102*m.b487 + 2*m.b102*m.b510 + 2*m.b103*m.b175 - 2*m.b103 - 4*m.b175 + 2*
                       m.b103*m.b364 - 2*m.b103*m.b466 + 2*m.b103*m.b467 - 2*m.b104*m.b242 + 2*m.b104*m.b363 + 2*m.b104*
                       m.b414 + 2*m.b105*m.b106 + 2*m.b105*m.b376 + 2*m.b105*m.b490 + 2*m.b106*m.b179 - 2*m.b179 - 2*
                       m.b106*m.b536 - 2*m.b107*m.b108 + 2*m.b107 + 2*m.b108 - 2*m.b107*m.b381 + 2*m.b107*m.b393 - 2*
                       m.b107*m.b502 + 2*m.b108*m.b446 - 2*m.b108*m.b463 - 2*m.b108*m.b538 + 2*m.b109*m.b110 - 2*m.b110
                        + 2*m.b109*m.b301 + 2*m.b110*m.b161 + 2*m.b110*m.b260 - 4*m.b260 - 2*m.b110*m.b300 - 2*m.b300 + 
                       2*m.b111*m.b162 - 2*m.b162 + 2*m.b111*m.b464 + 2*m.b112*m.b113 + 2*m.b112*m.b228 - 2*m.b228 + 2*
                       m.b113*m.b166 - 4*m.b166 + 2*m.b113*m.b197 - 2*m.b197 + 2*m.b114*m.b115 - 2*m.b115 + 2*m.b114*
                       m.b352 - 4*m.b352 + 2*m.b115*m.b197 + 2*m.b116*m.b198 - 2*m.b198 + 2*m.b116*m.b233 - 2*m.b233 + 2
                       *m.b116*m.b530 + 2*m.b117*m.b203 - 2*m.b117*m.b317 + 2*m.b117*m.b485 - 2*m.b118*m.b119 + 2*m.b119
                        - 2*m.b118*m.b204 - 2*m.b204 - 2*m.b118*m.b408 + 2*m.b119*m.b120 - 2*m.b120 - 2*m.b119*m.b461 - 
                       2*m.b119*m.b540 - 2*m.b120*m.b375 + 2*m.b120*m.b451 + 2*m.b120*m.b535 + 2*m.b121*m.b122 - 4*
                       m.b121 - 4*m.b122 + 2*m.b121*m.b208 - 4*m.b208 + 2*m.b121*m.b466 + 2*m.b121*m.b474 + 2*m.b122*
                       m.b368 + 2*m.b122*m.b453 + 2*m.b122*m.b535 + 2*m.b123*m.b124 + 2*m.b123*m.b388 + 2*m.b123*m.b481
                        + 2*m.b124*m.b210 - 2*m.b210 - 2*m.b124*m.b244 + 2*m.b244 + 2*m.b125*m.b181 - 2*m.b125 + 2*
                       m.b181 + 2*m.b125*m.b210 - 2*m.b125*m.b330 + 2*m.b330 + 2*m.b125*m.b525 + 2*m.b126*m.b183 - 2*
                       m.b183 - 2*m.b126*m.b292 + 2*m.b292 + 2*m.b126*m.b434 - 2*m.b127*m.b128 + 4*m.b127 + 2*m.b128 - 2
                       *m.b127*m.b392 - 2*m.b127*m.b393 - 2*m.b127*m.b492 + 2*m.b128*m.b457 - 2*m.b128*m.b469 - 2*m.b128
                       *m.b542 + 2*m.b129*m.b130 - 2*m.b130 + 2*m.b129*m.b471 + 2*m.b130*m.b190 - 2*m.b130*m.b259 - 2*
                       m.b259 + 2*m.b130*m.b303 - 4*m.b303 + 2*m.b131*m.b133 - 4*m.b133 + 2*m.b131*m.b459 + 2*m.b132*
                       m.b135 - 4*m.b135 + 2*m.b132*m.b304 - 4*m.b304 + 2*m.b133*m.b135 + 2*m.b133*m.b262 + 2*m.b262 + 2
                       *m.b133*m.b303 - 2*m.b134*m.b136 + 2*m.b134 + 2*m.b134*m.b261 - 2*m.b261 - 2*m.b134*m.b357 - 2*
                       m.b134*m.b472 + 2*m.b135*m.b136 + 2*m.b135*m.b357 + 2*m.b136*m.b196 - 4*m.b196 + 2*m.b137*m.b139
                        + 2*m.b137*m.b263 - 2*m.b263 + 2*m.b137*m.b494 - 2*m.b138*m.b168 + 2*m.b138 + 2*m.b138*m.b230 - 
                       4*m.b230 - 2*m.b138*m.b350 - 2*m.b350 - 2*m.b138*m.b356 + 2*m.b139*m.b196 + 2*m.b139*m.b230 + 2*
                       m.b140*m.b141 - 2*m.b141 - 2*m.b140*m.b373 + 2*m.b141*m.b230 + 2*m.b142*m.b143 - 2*m.b142 + 2*
                       m.b142*m.b522 + 2*m.b143*m.b231 - 2*m.b231 + 2*m.b143*m.b273 - 2*m.b273 + 2*m.b144*m.b273 + 2*
                       m.b144*m.b497 + 2*m.b144*m.b521 - 2*m.b145*m.b146 + 2*m.b146 - 2*m.b145*m.b237 - 2*m.b237 - 2*
                       m.b145*m.b413 + 2*m.b146*m.b147 - 2*m.b146*m.b466 - 2*m.b146*m.b543 + 2*m.b147*m.b386 + 2*m.b147*
                       m.b531 + 2*m.b148*m.b149 - 4*m.b148 - 4*m.b149 + 2*m.b148*m.b240 - 4*m.b240 + 2*m.b148*m.b461 + 2
                       *m.b148*m.b479 + 2*m.b149*m.b376 + 2*m.b149*m.b443 + 2*m.b149*m.b531 + 2*m.b150*m.b151 - 2*m.b151
                        + 2*m.b151*m.b433 - 2*m.b151*m.b482 + 2*m.b151*m.b544 + 2*m.b152*m.b153 - 2*m.b152*m.b211 - 2*
                       m.b211 + 2*m.b152*m.b249 - 2*m.b249 + 2*m.b153*m.b155 - 2*m.b155 + 2*m.b153*m.b433 + 2*m.b154*
                       m.b214 - 2*m.b214 - 2*m.b154*m.b253 + 2*m.b253 + 2*m.b155*m.b253 + 2*m.b155*m.b333 - 2*m.b333 - 2
                       *m.b155*m.b506 - 2*m.b156*m.b157 + 4*m.b156 + 2*m.b157 - 2*m.b156*m.b401 - 2*m.b156*m.b403 - 2*
                       m.b156*m.b483 + 2*m.b157*m.b158 - 2*m.b157*m.b476 - 2*m.b157*m.b545 - 2*m.b158*m.b393 + 2*m.b158*
                       m.b546 + 2*m.b159*m.b160 - 2*m.b160 + 2*m.b160*m.b223 + 2*m.b160*m.b345 - 4*m.b345 - 2*m.b160*
                       m.b547 + 2*m.b161*m.b163 - 4*m.b163 + 2*m.b161*m.b448 + 2*m.b162*m.b260 + 2*m.b162*m.b427 - 2*
                       m.b162*m.b539 + 2*m.b163*m.b226 + 2*m.b226 + 2*m.b163*m.b345 + 2*m.b163*m.b539 - 2*m.b164*m.b165
                        + 2*m.b164 + 2*m.b164*m.b225 - 4*m.b225 - 2*m.b164*m.b383 - 2*m.b164*m.b464 + 2*m.b165*m.b229 - 
                       2*m.b229 + 2*m.b165*m.b539 + 2*m.b166*m.b167 + 2*m.b166*m.b306 - 2*m.b306 + 2*m.b166*m.b503 + 2*
                       m.b167*m.b229 + 2*m.b167*m.b267 - 4*m.b267 + 2*m.b168*m.b169 - 2*m.b169 + 2*m.b169*m.b267 + 2*
                       m.b170*m.b171 - 2*m.b171 + 2*m.b171*m.b270 - 2*m.b270 + 2*m.b171*m.b313 - 2*m.b313 - 2*m.b171*
                       m.b496 + 2*m.b172*m.b173 - 2*m.b172 - 2*m.b173 + 2*m.b172*m.b235 - 2*m.b172*m.b359 + 2*m.b172*
                       m.b522 + 2*m.b173*m.b313 - 2*m.b173*m.b439 + 2*m.b173*m.b486 - 2*m.b174*m.b277 + 4*m.b174 - 2*
                       m.b277 - 2*m.b174*m.b419 - 2*m.b174*m.b420 - 2*m.b174*m.b473 + 2*m.b175*m.b398 + 2*m.b175*m.b473
                        + 2*m.b175*m.b523 + 2*m.b176*m.b177 - 4*m.b176 - 4*m.b177 + 2*m.b176*m.b280 - 4*m.b280 + 2*
                       m.b176*m.b452 + 2*m.b176*m.b488 + 2*m.b177*m.b178 - 2*m.b178 + 2*m.b177*m.b388 + 2*m.b177*m.b523
                        - 2*m.b178*m.b432 + 2*m.b178*m.b479 + 2*m.b178*m.b549 + 2*m.b179*m.b180 - 2*m.b180 - 2*m.b179*
                       m.b391 + 2*m.b179*m.b526 + 2*m.b180*m.b182 - 2*m.b182 - 2*m.b180*m.b491 + 2*m.b180*m.b550 - 2*
                       m.b181*m.b366 - 2*m.b181*m.b417 - 2*m.b181*m.b541 - 2*m.b182*m.b379 + 2*m.b182*m.b424 + 2*m.b182*
                       m.b541 + 2*m.b183*m.b378 + 2*m.b183*m.b482 - 2*m.b183*m.b512 - 2*m.b184*m.b217 + 2*m.b217 + 2*
                       m.b184*m.b249 + 2*m.b184*m.b401 - 2*m.b185*m.b292 - 2*m.b185*m.b412 - 2*m.b185*m.b484 + 2*m.b186*
                       m.b298 - 2*m.b298 + 2*m.b186*m.b393 + 2*m.b186*m.b484 + 2*m.b187*m.b189 - 4*m.b189 + 2*m.b188*
                       m.b189 - 4*m.b188 + 2*m.b188*m.b298 + 2*m.b188*m.b301 + 2*m.b188*m.b426 + 2*m.b189*m.b191 - 2*
                       m.b191 + 2*m.b189*m.b260 + 2*m.b190*m.b192 - 4*m.b192 + 2*m.b190*m.b437 + 2*m.b191*m.b192 + 2*
                       m.b191*m.b302 - 4*m.b302 - 2*m.b191*m.b355 + 2*m.b192*m.b193 + 2*m.b193 + 2*m.b192*m.b534 - 2*
                       m.b193*m.b195 - 2*m.b193*m.b227 - 2*m.b193*m.b459 - 2*m.b194*m.b226 + 2*m.b194 - 2*m.b194*m.b264
                        - 2*m.b264 - 2*m.b194*m.b356 + 2*m.b194*m.b405 + 2*m.b195*m.b264 + 2*m.b195*m.b534 + 2*m.b196*
                       m.b348 - 4*m.b348 + 2*m.b196*m.b351 - 2*m.b197*m.b265 + 2*m.b197*m.b553 + 2*m.b198*m.b199 - 2*
                       m.b199 + 2*m.b199*m.b310 - 2*m.b310 + 2*m.b199*m.b396 - 2*m.b199*m.b485 + 2*m.b200*m.b202 - 2*
                       m.b202 + 2*m.b200*m.b275 - 2*m.b200*m.b362 + 2*m.b201*m.b203 - 4*m.b201 + 2*m.b201*m.b204 + 2*
                       m.b201*m.b496 + 2*m.b201*m.b521 + 2*m.b202*m.b204 + 2*m.b202*m.b396 - 2*m.b202*m.b429 + 2*m.b203*
                       m.b205 - 4*m.b205 + 2*m.b204*m.b205 + 2*m.b205*m.b206 - 2*m.b206 + 2*m.b205*m.b375 + 2*m.b206*
                       m.b208 - 2*m.b206*m.b319 + 2*m.b319 + 2*m.b206*m.b461 - 2*m.b207*m.b323 + 2*m.b207 + 2*m.b323 - 2
                       *m.b207*m.b413 - 2*m.b207*m.b414 + 2*m.b207*m.b511 + 2*m.b208*m.b323 + 2*m.b208*m.b408 + 2*m.b209
                       *m.b244 - 2*m.b209 + 2*m.b209*m.b442 + 2*m.b209*m.b488 - 2*m.b209*m.b555 + 2*m.b210*m.b211 - 2*
                       m.b210*m.b400 + 2*m.b211*m.b213 - 2*m.b213 + 2*m.b211*m.b556 - 2*m.b212*m.b367 + 2*m.b212 - 2*
                       m.b212*m.b411 + 2*m.b212*m.b526 - 2*m.b212*m.b537 - 2*m.b213*m.b416 + 2*m.b213*m.b417 + 2*m.b213*
                       m.b537 - 2*m.b214*m.b216 - 2*m.b216 + 2*m.b214*m.b370 + 2*m.b214*m.b491 + 2*m.b215*m.b289 - 2*
                       m.b215 + 2*m.b289 + 2*m.b215*m.b392 + 2*m.b215*m.b411 - 2*m.b215*m.b455 + 2*m.b216*m.b455 + 2*
                       m.b216*m.b506 + 2*m.b216*m.b537 - 2*m.b217*m.b254 + 2*m.b254 + 2*m.b217*m.b512 - 2*m.b217*m.b552
                        - 2*m.b218*m.b219 - 2*m.b219 - 2*m.b218*m.b253 - 2*m.b218*m.b418 + 2*m.b219*m.b220 + 2*m.b219*
                       m.b469 + 2*m.b219*m.b552 + 2*m.b220*m.b340 - 2*m.b340 + 2*m.b220*m.b403 + 2*m.b221*m.b222 - 4*
                       m.b222 + 2*m.b222*m.b224 - 4*m.b224 + 2*m.b222*m.b303 + 2*m.b222*m.b547 + 2*m.b223*m.b225 + 2*
                       m.b223*m.b428 + 2*m.b224*m.b225 + 2*m.b224*m.b344 - 4*m.b344 + 2*m.b224*m.b355 + 2*m.b225*m.b529
                        - 2*m.b226*m.b228 - 2*m.b226*m.b448 - 2*m.b227*m.b307 - 2*m.b307 + 2*m.b228*m.b307 + 2*m.b228*
                       m.b529 + 2*m.b229*m.b308 - 2*m.b229*m.b360 + 2*m.b230*m.b558 + 2*m.b231*m.b232 - 2*m.b232 + 2*
                       m.b232*m.b234 - 2*m.b234 - 2*m.b232*m.b460 + 2*m.b232*m.b496 + 2*m.b233*m.b236 - 2*m.b236 - 2*
                       m.b233*m.b311 + 2*m.b233*m.b315 - 4*m.b315 + 2*m.b234*m.b236 - 2*m.b234*m.b385 + 2*m.b234*m.b406
                        + 2*m.b235*m.b237 + 2*m.b235*m.b518 + 2*m.b236*m.b237 - 2*m.b236*m.b419 + 2*m.b237*m.b548 + 2*
                       m.b238*m.b240 - 2*m.b238 - 2*m.b238*m.b450 + 2*m.b238*m.b452 + 2*m.b238*m.b548 - 2*m.b239*m.b281
                        + 4*m.b239 + 2*m.b281 - 2*m.b239*m.b420 - 2*m.b239*m.b421 - 2*m.b239*m.b511 + 2*m.b240*m.b281 + 
                       2*m.b240*m.b413 + 2*m.b241*m.b243 + 2*m.b241 - 2*m.b241*m.b414 - 2*m.b241*m.b499 - 2*m.b241*
                       m.b501 + 2*m.b242*m.b364 - 2*m.b242*m.b536 + 2*m.b243*m.b536 - 2*m.b243*m.b559 - 2*m.b244*m.b453
                        - 2*m.b244*m.b557 - 2*m.b245*m.b432 - 2*m.b245*m.b468 + 2*m.b246*m.b248 - 4*m.b246 - 2*m.b248 + 
                       2*m.b246*m.b468 + 2*m.b246*m.b491 + 2*m.b246*m.b544 - 2*m.b247*m.b250 - 2*m.b250 - 2*m.b247*
                       m.b372 + 2*m.b248*m.b250 - 2*m.b248*m.b410 + 2*m.b248*m.b411 - 2*m.b249*m.b252 - 2*m.b252 + 2*
                       m.b249*m.b365 + 2*m.b250*m.b252 + 2*m.b250*m.b533 + 2*m.b251*m.b332 - 2*m.b251 + 2*m.b332 + 2*
                       m.b251*m.b381 + 2*m.b251*m.b417 - 2*m.b251*m.b445 + 2*m.b252*m.b445 + 2*m.b252*m.b502 - 2*m.b253*
                       m.b545 - 2*m.b254*m.b255 - 2*m.b255 + 2*m.b254*m.b336 - 2*m.b336 - 2*m.b254*m.b425 + 2*m.b255*
                       m.b257 + 2*m.b255*m.b463 + 2*m.b255*m.b545 - 2*m.b256*m.b425 + 2*m.b256 - 2*m.b256*m.b426 + 2*
                       m.b256*m.b513 - 2*m.b256*m.b528 + 2*m.b257*m.b412 + 2*m.b257*m.b528 + 2*m.b258*m.b343 - 2*m.b343
                        - 2*m.b258*m.b514 + 2*m.b259*m.b343 + 2*m.b259*m.b528 + 2*m.b259*m.b546 + 2*m.b260*m.b261 + 2*
                       m.b261*m.b520 - 2*m.b261*m.b560 - 2*m.b262*m.b263 - 2*m.b262*m.b360 - 2*m.b262*m.b437 + 2*m.b263*
                       m.b349 - 2*m.b349 + 2*m.b263*m.b520 + 2*m.b264*m.b266 + 2*m.b264*m.b351 + 2*m.b265*m.b268 + 2*
                       m.b265*m.b356 + 2*m.b266*m.b268 + 2*m.b266*m.b349 + 2*m.b267*m.b269 - 2*m.b269 + 2*m.b267*m.b373
                        + 2*m.b268*m.b269 + 2*m.b270*m.b272 - 2*m.b271*m.b273 + 2*m.b271*m.b274 + 2*m.b271*m.b407 + 2*
                       m.b272*m.b274 - 2*m.b272*m.b449 + 2*m.b273*m.b276 + 2*m.b274*m.b276 + 2*m.b275*m.b277 + 2*m.b275*
                       m.b510 + 2*m.b276*m.b277 + 2*m.b277*m.b543 + 2*m.b278*m.b280 - 4*m.b278 + 2*m.b278*m.b321 + 2*
                       m.b321 + 2*m.b278*m.b450 + 2*m.b278*m.b543 + 2*m.b279*m.b320 + 2*m.b279 - 4*m.b320 - 2*m.b279*
                       m.b430 - 2*m.b279*m.b504 - 2*m.b279*m.b505 + 2*m.b280*m.b420 + 2*m.b280*m.b505 - 2*m.b281*m.b324
                        - 2*m.b324 - 2*m.b281*m.b559 + 2*m.b282*m.b284 - 2*m.b282 + 2*m.b282*m.b421 + 2*m.b282*m.b501 - 
                       2*m.b282*m.b505 + 2*m.b283*m.b369 - 2*m.b283*m.b467 - 2*m.b283*m.b532 + 2*m.b284*m.b532 + 2*
                       m.b284*m.b559 - 2*m.b285*m.b442 - 2*m.b285*m.b462 + 2*m.b286*m.b288 - 4*m.b286 + 2*m.b286*m.b462
                        + 2*m.b286*m.b482 + 2*m.b286*m.b550 - 2*m.b287*m.b290 - 2*m.b290 - 2*m.b287*m.b380 - 2*m.b287*
                       m.b526 + 2*m.b288*m.b290 + 2*m.b288*m.b410 - 2*m.b289*m.b291 - 2*m.b291 - 2*m.b289*m.b365 - 2*
                       m.b289*m.b491 + 2*m.b290*m.b291 + 2*m.b290*m.b527 + 2*m.b291*m.b293 - 2*m.b293 + 2*m.b291*m.b492
                        + 2*m.b292*m.b527 - 2*m.b292*m.b542 + 2*m.b293*m.b294 - 2*m.b293*m.b382 + 2*m.b293*m.b542 - 2*
                       m.b294*m.b295 - 2*m.b295 - 2*m.b294*m.b455 + 2*m.b295*m.b297 + 2*m.b295*m.b456 + 2*m.b295*m.b542
                        - 2*m.b296*m.b435 - 2*m.b296*m.b519 + 2*m.b297*m.b418 + 2*m.b297*m.b519 + 2*m.b298*m.b300 - 2*
                       m.b298*m.b446 + 2*m.b299*m.b302 - 2*m.b299*m.b519 + 2*m.b300*m.b302 + 2*m.b300*m.b519 + 2*m.b301*
                       m.b304 + 2*m.b302*m.b304 + 2*m.b303*m.b305 - 4*m.b305 + 2*m.b304*m.b305 + 2*m.b305*m.b384 + 2*
                       m.b305*m.b515 + 2*m.b306*m.b374 - 2*m.b306*m.b427 + 2*m.b306*m.b515 + 2*m.b307*m.b308 + 2*m.b307*
                       m.b309 - 2*m.b308*m.b353 + 2*m.b353 + 2*m.b309*m.b353 + 2*m.b309*m.b374 + 2*m.b310*m.b312 + 2*
                       m.b311*m.b314 + 2*m.b311*m.b395 + 2*m.b312*m.b314 - 2*m.b312*m.b438 + 2*m.b313*m.b316 - 2*m.b313*
                       m.b406 + 2*m.b314*m.b316 + 2*m.b315*m.b317 + 2*m.b315*m.b318 - 2*m.b318 + 2*m.b315*m.b516 + 2*
                       m.b316*m.b318 - 2*m.b317*m.b540 - 2*m.b318*m.b319 + 2*m.b318*m.b540 + 2*m.b319*m.b320 - 2*m.b319*
                       m.b429 + 2*m.b320*m.b322 - 4*m.b322 + 2*m.b320*m.b540 - 2*m.b321*m.b440 - 2*m.b321*m.b498 - 2*
                       m.b321*m.b499 + 2*m.b322*m.b375 + 2*m.b322*m.b414 + 2*m.b322*m.b499 - 2*m.b323*m.b389 - 2*m.b323*
                       m.b555 + 2*m.b324*m.b326 + 2*m.b324*m.b430 + 2*m.b324*m.b490 + 2*m.b325*m.b377 + 2*m.b325 - 2*
                       m.b325*m.b474 - 2*m.b325*m.b475 - 2*m.b325*m.b524 + 2*m.b326*m.b524 + 2*m.b326*m.b555 + 2*m.b327*
                       m.b390 + 2*m.b327*m.b432 - 2*m.b327*m.b454 + 2*m.b328*m.b454 - 2*m.b328 + 2*m.b328*m.b524 - 2*
                       m.b328*m.b544 + 2*m.b328*m.b549 + 2*m.b329*m.b330 - 4*m.b329 + 2*m.b329*m.b331 + 2*m.b329*m.b454
                        + 2*m.b329*m.b556 - 2*m.b330*m.b333 - 2*m.b330*m.b434 + 2*m.b331*m.b333 + 2*m.b331*m.b416 - 2*
                       m.b332*m.b335 - 2*m.b335 - 2*m.b332*m.b370 - 2*m.b332*m.b482 + 2*m.b333*m.b335 - 2*m.b334*m.b336
                        - 2*m.b334*m.b392 - 2*m.b334*m.b424 + 2*m.b335*m.b336 + 2*m.b335*m.b483 + 2*m.b336*m.b538 + 2*
                       m.b337*m.b338 - 2*m.b337 + 2*m.b337*m.b339 - 2*m.b337*m.b444 + 2*m.b337*m.b538 - 2*m.b338*m.b513
                        - 2*m.b338*m.b514 + 2*m.b339*m.b425 + 2*m.b339*m.b514 + 2*m.b340*m.b342 - 2*m.b340*m.b436 + 2*
                       m.b340*m.b547 + 2*m.b341*m.b344 - 2*m.b341*m.b528 + 2*m.b342*m.b344 + 2*m.b342*m.b514 + 2*m.b343*
                       m.b345 - 2*m.b343*m.b560 + 2*m.b344*m.b560 + 2*m.b345*m.b346 + 2*m.b346*m.b347 - 2*m.b347 + 2*
                       m.b346*m.b560 + 2*m.b347*m.b348 - 2*m.b347*m.b464 + 2*m.b347*m.b508 + 2*m.b348*m.b350 + 2*m.b348*
                       m.b427 + 2*m.b349*m.b352 - 2*m.b349*m.b383 + 2*m.b350*m.b352 + 2*m.b350*m.b383 - 2*m.b351*m.b554
                        + 2*m.b352*m.b554 - 2*m.b353*m.b558 - 2*m.b353*m.b561 + 2*m.b354*m.b426 - 2*m.b355*m.b405 + 2*
                       m.b356*m.b357 - 2*m.b357*m.b374 - 2*m.b358*m.b359 + 2*m.b358*m.b385 + 2*m.b359*m.b438 - 2*m.b361*
                       m.b362 - 2*m.b363*m.b364 + 2*m.b363*m.b432 - 2*m.b363*m.b500 - 2*m.b364*m.b535 - 2*m.b365*m.b366
                        + 2*m.b365*m.b367 - 2*m.b367*m.b454 - 2*m.b368*m.b369 - 2*m.b368*m.b489 - 2*m.b369*m.b531 - 2*
                       m.b370*m.b371 + 2*m.b370*m.b372 - 2*m.b371*m.b433 - 2*m.b372*m.b462 - 2*m.b373*m.b374 - 2*m.b376*
                       m.b377 - 2*m.b376*m.b480 + 2*m.b377*m.b451 - 2*m.b377*m.b523 - 2*m.b378*m.b379 + 2*m.b378*m.b380
                        - 2*m.b378*m.b434 + 2*m.b379*m.b399 - 2*m.b380*m.b468 - 2*m.b381*m.b382 + 2*m.b381*m.b404 + 2*
                       m.b382*m.b424 + 2*m.b382*m.b434 + 2*m.b383*m.b384 - 2*m.b384*m.b477 - 2*m.b384*m.b503 - 2*m.b385*
                       m.b397 + 2*m.b385*m.b439 + 2*m.b386*m.b387 - 2*m.b386*m.b441 - 2*m.b387*m.b510 - 2*m.b387*m.b511
                        - 2*m.b388*m.b389 - 2*m.b388*m.b475 + 2*m.b389*m.b440 + 2*m.b389*m.b481 - 2*m.b390*m.b391 - 2*
                       m.b390*m.b416 + 2*m.b391*m.b475 - 2*m.b394*m.b395 - 2*m.b394*m.b396 + 2*m.b394*m.b485 - 2*m.b398*
                       m.b431 - 2*m.b399*m.b400 - 2*m.b399*m.b410 + 2*m.b400*m.b500 - 2*m.b401*m.b402 - 2*m.b402*m.b417
                        + 2*m.b403*m.b404 - 2*m.b403*m.b457 - 2*m.b404*m.b506 - 2*m.b404*m.b507 + 2*m.b405*m.b477 - 2*
                       m.b406*m.b407 - 2*m.b408*m.b422 + 2*m.b409*m.b489 - 2*m.b409*m.b544 - 2*m.b412*m.b446 + 2*m.b415*
                       m.b480 - 2*m.b415*m.b550 - 2*m.b418*m.b436 + 2*m.b421*m.b422 - 2*m.b421*m.b488 + 2*m.b422*m.b504
                        - 2*m.b422*m.b523 + 2*m.b423*m.b442 + 2*m.b423*m.b475 - 2*m.b423*m.b556 - 2*m.b424*m.b433 - 2*
                       m.b426*m.b458 - 2*m.b427*m.b428 - 2*m.b428*m.b534 + 2*m.b430*m.b431 - 2*m.b430*m.b479 + 2*m.b431*
                       m.b498 - 2*m.b431*m.b531 + 2*m.b435*m.b436 - 2*m.b435*m.b447 + 2*m.b436*m.b507 - 2*m.b437*m.b529
                        - 2*m.b439*m.b450 + 2*m.b440*m.b441 - 2*m.b440*m.b474 + 2*m.b441*m.b487 - 2*m.b441*m.b535 - 2*
                       m.b442*m.b443 + 2*m.b443*m.b474 - 2*m.b443*m.b549 - 2*m.b444*m.b445 + 2*m.b445*m.b545 - 2*m.b448*
                       m.b520 - 2*m.b451*m.b452 - 2*m.b451*m.b467 - 2*m.b452*m.b487 + 2*m.b453*m.b467 + 2*m.b455*m.b552
                        - 2*m.b456*m.b507 - 2*m.b457*m.b546 - 2*m.b459*m.b515 + 2*m.b462*m.b551 + 2*m.b464*m.b470 - 2*
                       m.b465*m.b478 + 2*m.b466*m.b473 + 2*m.b468*m.b557 - 2*m.b470*m.b471 - 2*m.b470*m.b472 - 2*m.b473*
                       m.b548 + 2*m.b476*m.b484 - 2*m.b479*m.b481 - 2*m.b480*m.b481 + 2*m.b483*m.b533 - 2*m.b483*m.b538
                        - 2*m.b484*m.b552 - 2*m.b485*m.b517 + 2*m.b486*m.b517 - 2*m.b486*m.b548 - 2*m.b488*m.b490 - 2*
                       m.b489*m.b490 - 2*m.b492*m.b533 + 2*m.b493*m.b494 - 2*m.b493*m.b495 - 2*m.b494*m.b534 - 2*m.b496*
                       m.b509 + 2*m.b497*m.b509 - 2*m.b497*m.b543 + 2*m.b499*m.b555 - 2*m.b500*m.b501 - 2*m.b502*m.b527
                        - 2*m.b503*m.b539 + 2*m.b505*m.b559 - 2*m.b508*m.b515 - 2*m.b509*m.b510 + 2*m.b512*m.b541 + 2*
                       m.b516*m.b517 - 2*m.b517*m.b518 - 2*m.b521*m.b522 - 2*m.b522*m.b530 - 2*m.b525*m.b526 - 2*m.b527*
                       m.b541 + 2*m.b532*m.b551 - 2*m.b533*m.b537 + 2*m.b536*m.b557 - 2*m.b546*m.b547 - 2*m.b549*m.b551
                        - 2*m.b550*m.b551 - 2*m.b553*m.b554 + 2*m.b554*m.b561 - 2*m.b556*m.b557 + m.x562 <= 0)
