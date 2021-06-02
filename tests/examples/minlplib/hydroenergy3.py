#  MINLP written by GAMS Convert at 04/21/18 13:52:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       1499      337      504      658        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#       1009      673      336        0        0        0        0        0
#  FX      7        7        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       4423     3943      480        0
# 
#  Reformulation has removed 1 variable and 1 equation


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
m.x337 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x338 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x339 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x340 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x341 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x342 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x343 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x344 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x345 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x346 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x347 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x348 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x349 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x350 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x351 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x352 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x353 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x354 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x355 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x356 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x357 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x358 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x359 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x360 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x361 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x362 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x363 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x364 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x365 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x366 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x367 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x368 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x369 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x370 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x371 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x372 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x373 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x374 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x375 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x376 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x377 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x378 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x379 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x380 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x381 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x382 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x383 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x384 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x385 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x386 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x387 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x388 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x389 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x390 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x391 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x392 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x393 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x394 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x395 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x396 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x397 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x398 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x399 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x400 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x401 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x402 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x403 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x404 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x405 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x406 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x407 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x408 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x409 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x410 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x411 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x412 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x413 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x414 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x415 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x416 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x417 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x418 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x419 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x420 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x421 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x422 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x423 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x424 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x425 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x426 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x427 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x428 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x429 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x430 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x431 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x432 = Var(within=Reals,bounds=(0,185.99),initialize=0)
m.x433 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x434 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x435 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x436 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x437 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x438 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x439 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x440 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x441 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x442 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x443 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x444 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x445 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x446 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x447 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x448 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x449 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x450 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x451 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x452 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x453 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x454 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x455 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x456 = Var(within=Reals,bounds=(0,201.02),initialize=0)
m.x457 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x458 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x459 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x460 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x461 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x462 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x463 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x464 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x465 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x466 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x467 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x468 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x469 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x470 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x471 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x472 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x473 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x474 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x475 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x476 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x477 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x478 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x479 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x480 = Var(within=Reals,bounds=(0,134.02),initialize=0)
m.x481 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x482 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x483 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x484 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x485 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x486 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x487 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x488 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x489 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x490 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x491 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x492 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x493 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x494 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x495 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x496 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x497 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x498 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x499 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x500 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x501 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x502 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x503 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x504 = Var(within=Reals,bounds=(0,117.01),initialize=0)
m.x505 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x506 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x507 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x508 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x509 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x510 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x511 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x512 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x513 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x514 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x515 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x516 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x517 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x518 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x519 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x520 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x521 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x522 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x523 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x524 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x525 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x526 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x527 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x528 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x529 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x530 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x531 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x532 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x533 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x534 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x535 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x536 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x537 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x538 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x539 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x540 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x541 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x542 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x543 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x544 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x545 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x546 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x547 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x548 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x549 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x550 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x551 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x552 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x553 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x554 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x555 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x556 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x557 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x558 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x559 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x560 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x561 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x562 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x563 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x564 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x565 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x566 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x567 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x568 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x569 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x570 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x571 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x572 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x573 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x574 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x575 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x576 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x577 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x578 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x579 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x580 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x581 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x582 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x583 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x584 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x585 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x586 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x587 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x588 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x589 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x590 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x591 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x592 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x593 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x594 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x595 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x596 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x597 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x598 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x599 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x600 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x601 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x602 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x603 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x604 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x605 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x606 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x607 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x608 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x609 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x610 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x611 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x612 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x613 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x614 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x615 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x616 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x617 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x618 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x619 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x620 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x621 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x622 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x623 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x624 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x625 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x626 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x627 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x628 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x629 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x630 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x631 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x632 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x633 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x634 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x635 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x636 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x637 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x638 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x639 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x640 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x641 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x642 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x643 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x644 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x645 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x646 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x647 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x648 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x649 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x650 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x651 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x652 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x653 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x654 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x655 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x656 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x657 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x658 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x659 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x660 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x661 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x662 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x663 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x664 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x665 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x666 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x667 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x668 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x669 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x670 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x671 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x672 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x673 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x674 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x675 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x676 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x677 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x678 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x679 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x680 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x681 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x682 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x683 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x684 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x685 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x686 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x687 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x688 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x689 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x690 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x691 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x692 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x693 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x694 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x695 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x696 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x697 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x698 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x699 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x700 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x701 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x702 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x703 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x704 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x705 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x706 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x707 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x708 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x709 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x710 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x711 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x712 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x713 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x714 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x715 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x716 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x717 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x718 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x719 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x720 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x721 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x722 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x723 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x724 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x725 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x726 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x727 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x728 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x729 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x730 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x731 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x732 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x733 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x734 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x735 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x736 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x737 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x738 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x739 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x740 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x741 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x742 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x743 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x744 = Var(within=Reals,bounds=(0,0.05904),initialize=0)
m.x745 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x746 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x747 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x748 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x749 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x750 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x751 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x752 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x753 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x754 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x755 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x756 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x757 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x758 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x759 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x760 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x761 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x762 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x763 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x764 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x765 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x766 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x767 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x768 = Var(within=Reals,bounds=(0,3.24),initialize=0)
m.x769 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x770 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x771 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x772 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x773 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x774 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x775 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x776 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x777 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x778 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x779 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x780 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x781 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x782 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x783 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x784 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x785 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x786 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x787 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x788 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x789 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x790 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x791 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x792 = Var(within=Reals,bounds=(0,3.172716),initialize=0)
m.x793 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x794 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x795 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x796 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x797 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x798 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x799 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x800 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x801 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x802 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x803 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x804 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x805 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x806 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x807 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x808 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x809 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x810 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x811 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x812 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x813 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x814 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x815 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x816 = Var(within=Reals,bounds=(0,1.174824),initialize=0)
m.x817 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x818 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x819 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x820 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x821 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x822 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x823 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x824 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x825 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x826 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x827 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x828 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x829 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x830 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x831 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x832 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x833 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x834 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x835 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x836 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x837 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x838 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x839 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x840 = Var(within=Reals,bounds=(0,4.883436),initialize=0)
m.x841 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x842 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x843 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x844 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x845 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x846 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x847 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x848 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x849 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x850 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x851 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x852 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x853 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x854 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x855 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x856 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x857 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x858 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x859 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x860 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x861 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x862 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x863 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x864 = Var(within=Reals,bounds=(10.35,10.35),initialize=10.35)
m.x865 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x866 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x867 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x868 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x869 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x870 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x871 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x872 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x873 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x874 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x875 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x876 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x877 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x878 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x879 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x880 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x881 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x882 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x883 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x884 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x885 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x886 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x887 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x888 = Var(within=Reals,bounds=(10.64,10.64),initialize=10.64)
m.x889 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x890 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x891 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x892 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x893 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x894 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x895 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x896 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x897 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x898 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x899 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x900 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x901 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x902 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x903 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x904 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x905 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x906 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x907 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x908 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x909 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x910 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x911 = Var(within=Reals,bounds=(39,97.5),initialize=39)
m.x912 = Var(within=Reals,bounds=(78,78),initialize=78)
m.x913 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x914 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x915 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x916 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x917 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x918 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x919 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x920 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x921 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x922 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x923 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x924 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x925 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x926 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x927 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x928 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x929 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x930 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x931 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x932 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x933 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x934 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x935 = Var(within=Reals,bounds=(4.8,12),initialize=4.8)
m.x936 = Var(within=Reals,bounds=(9.6,9.6),initialize=9.6)
m.x937 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x938 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x939 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x940 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x941 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x942 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x943 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x944 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x945 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x946 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x947 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x948 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x949 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x950 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x951 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x952 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x953 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x954 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x955 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x956 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x957 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x958 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x959 = Var(within=Reals,bounds=(4.4,11),initialize=4.4)
m.x960 = Var(within=Reals,bounds=(8.8,8.8),initialize=8.8)
m.x961 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x962 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x963 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x964 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x965 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x966 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x967 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x968 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x969 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x970 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x971 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x972 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x973 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x974 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x975 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x976 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x977 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x978 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x979 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x980 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x981 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x982 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x983 = Var(within=Reals,bounds=(36.89,58.38),initialize=36.89)
m.x984 = Var(within=Reals,bounds=(46.7,46.7),initialize=46.7)
m.x985 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x986 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x987 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x988 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x989 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x990 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x991 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x992 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x993 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x994 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x995 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x996 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x997 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x998 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x999 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x1000 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x1001 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x1002 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x1003 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x1004 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x1005 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x1006 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x1007 = Var(within=Reals,bounds=(8.6,21.5),initialize=8.6)
m.x1008 = Var(within=Reals,bounds=(17.2,17.2),initialize=17.2)

m.obj = Objective(expr= - 470.2*m.b169 - 470.2*m.b170 - 470.2*m.b171 - 470.2*m.b172 - 470.2*m.b173 - 470.2*m.b174
                        - 470.2*m.b175 - 470.2*m.b176 - 470.2*m.b177 - 470.2*m.b178 - 470.2*m.b179 - 470.2*m.b180
                        - 470.2*m.b181 - 470.2*m.b182 - 470.2*m.b183 - 470.2*m.b184 - 470.2*m.b185 - 470.2*m.b186
                        - 470.2*m.b187 - 470.2*m.b188 - 470.2*m.b189 - 470.2*m.b190 - 470.2*m.b191 - 470.2*m.b192
                        - 592.85*m.b193 - 592.85*m.b194 - 592.85*m.b195 - 592.85*m.b196 - 592.85*m.b197 - 592.85*m.b198
                        - 592.85*m.b199 - 592.85*m.b200 - 592.85*m.b201 - 592.85*m.b202 - 592.85*m.b203 - 592.85*m.b204
                        - 592.85*m.b205 - 592.85*m.b206 - 592.85*m.b207 - 592.85*m.b208 - 592.85*m.b209 - 592.85*m.b210
                        - 592.85*m.b211 - 592.85*m.b212 - 592.85*m.b213 - 592.85*m.b214 - 592.85*m.b215 - 592.85*m.b216
                        - 150*m.b217 - 150*m.b218 - 150*m.b219 - 150*m.b220 - 150*m.b221 - 150*m.b222 - 150*m.b223
                        - 150*m.b224 - 150*m.b225 - 150*m.b226 - 150*m.b227 - 150*m.b228 - 150*m.b229 - 150*m.b230
                        - 150*m.b231 - 150*m.b232 - 150*m.b233 - 150*m.b234 - 150*m.b235 - 150*m.b236 - 150*m.b237
                        - 150*m.b238 - 150*m.b239 - 150*m.b240 - 464.975*m.b241 - 464.975*m.b242 - 464.975*m.b243
                        - 464.975*m.b244 - 464.975*m.b245 - 464.975*m.b246 - 464.975*m.b247 - 464.975*m.b248
                        - 464.975*m.b249 - 464.975*m.b250 - 464.975*m.b251 - 464.975*m.b252 - 464.975*m.b253
                        - 464.975*m.b254 - 464.975*m.b255 - 464.975*m.b256 - 464.975*m.b257 - 464.975*m.b258
                        - 464.975*m.b259 - 464.975*m.b260 - 464.975*m.b261 - 464.975*m.b262 - 464.975*m.b263
                        - 464.975*m.b264 - 502.55*m.b265 - 502.55*m.b266 - 502.55*m.b267 - 502.55*m.b268 - 502.55*m.b269
                        - 502.55*m.b270 - 502.55*m.b271 - 502.55*m.b272 - 502.55*m.b273 - 502.55*m.b274 - 502.55*m.b275
                        - 502.55*m.b276 - 502.55*m.b277 - 502.55*m.b278 - 502.55*m.b279 - 502.55*m.b280 - 502.55*m.b281
                        - 502.55*m.b282 - 502.55*m.b283 - 502.55*m.b284 - 502.55*m.b285 - 502.55*m.b286 - 502.55*m.b287
                        - 502.55*m.b288 - 335.05*m.b289 - 335.05*m.b290 - 335.05*m.b291 - 335.05*m.b292 - 335.05*m.b293
                        - 335.05*m.b294 - 335.05*m.b295 - 335.05*m.b296 - 335.05*m.b297 - 335.05*m.b298 - 335.05*m.b299
                        - 335.05*m.b300 - 335.05*m.b301 - 335.05*m.b302 - 335.05*m.b303 - 335.05*m.b304 - 335.05*m.b305
                        - 335.05*m.b306 - 335.05*m.b307 - 335.05*m.b308 - 335.05*m.b309 - 335.05*m.b310 - 335.05*m.b311
                        - 335.05*m.b312 - 292.525*m.b313 - 292.525*m.b314 - 292.525*m.b315 - 292.525*m.b316
                        - 292.525*m.b317 - 292.525*m.b318 - 292.525*m.b319 - 292.525*m.b320 - 292.525*m.b321
                        - 292.525*m.b322 - 292.525*m.b323 - 292.525*m.b324 - 292.525*m.b325 - 292.525*m.b326
                        - 292.525*m.b327 - 292.525*m.b328 - 292.525*m.b329 - 292.525*m.b330 - 292.525*m.b331
                        - 292.525*m.b332 - 292.525*m.b333 - 292.525*m.b334 - 292.525*m.b335 - 292.525*m.b336
                        + 50.4*m.x337 + 46.287*m.x338 + 44.187*m.x339 + 44.787*m.x340 + 45.477*m.x341 + 47.523*m.x342
                        + 58.359*m.x343 + 68.487*m.x344 + 87.441*m.x345 + 91.395*m.x346 + 93.846*m.x347 + 94.995*m.x348
                        + 86.187*m.x349 + 92.295*m.x350 + 93.495*m.x351 + 92.259*m.x352 + 93.795*m.x353 + 103.254*m.x354
                        + 103.359*m.x355 + 100.623*m.x356 + 95.418*m.x357 + 92.136*m.x358 + 82.305*m.x359
                        + 68.946*m.x360 + 50.4*m.x361 + 46.287*m.x362 + 44.187*m.x363 + 44.787*m.x364 + 45.477*m.x365
                        + 47.523*m.x366 + 58.359*m.x367 + 68.487*m.x368 + 87.441*m.x369 + 91.395*m.x370 + 93.846*m.x371
                        + 94.995*m.x372 + 86.187*m.x373 + 92.295*m.x374 + 93.495*m.x375 + 92.259*m.x376 + 93.795*m.x377
                        + 103.254*m.x378 + 103.359*m.x379 + 100.623*m.x380 + 95.418*m.x381 + 92.136*m.x382
                        + 82.305*m.x383 + 68.946*m.x384 + 50.4*m.x385 + 46.287*m.x386 + 44.187*m.x387 + 44.787*m.x388
                        + 45.477*m.x389 + 47.523*m.x390 + 58.359*m.x391 + 68.487*m.x392 + 87.441*m.x393 + 91.395*m.x394
                        + 93.846*m.x395 + 94.995*m.x396 + 86.187*m.x397 + 92.295*m.x398 + 93.495*m.x399 + 92.259*m.x400
                        + 93.795*m.x401 + 103.254*m.x402 + 103.359*m.x403 + 100.623*m.x404 + 95.418*m.x405
                        + 92.136*m.x406 + 82.305*m.x407 + 68.946*m.x408 + 50.4*m.x409 + 46.287*m.x410 + 44.187*m.x411
                        + 44.787*m.x412 + 45.477*m.x413 + 47.523*m.x414 + 58.359*m.x415 + 68.487*m.x416 + 87.441*m.x417
                        + 91.395*m.x418 + 93.846*m.x419 + 94.995*m.x420 + 86.187*m.x421 + 92.295*m.x422 + 93.495*m.x423
                        + 92.259*m.x424 + 93.795*m.x425 + 103.254*m.x426 + 103.359*m.x427 + 100.623*m.x428
                        + 95.418*m.x429 + 92.136*m.x430 + 82.305*m.x431 + 68.946*m.x432 + 50.4*m.x433 + 46.287*m.x434
                        + 44.187*m.x435 + 44.787*m.x436 + 45.477*m.x437 + 47.523*m.x438 + 58.359*m.x439 + 68.487*m.x440
                        + 87.441*m.x441 + 91.395*m.x442 + 93.846*m.x443 + 94.995*m.x444 + 86.187*m.x445 + 92.295*m.x446
                        + 93.495*m.x447 + 92.259*m.x448 + 93.795*m.x449 + 103.254*m.x450 + 103.359*m.x451
                        + 100.623*m.x452 + 95.418*m.x453 + 92.136*m.x454 + 82.305*m.x455 + 68.946*m.x456 + 50.4*m.x457
                        + 46.287*m.x458 + 44.187*m.x459 + 44.787*m.x460 + 45.477*m.x461 + 47.523*m.x462 + 58.359*m.x463
                        + 68.487*m.x464 + 87.441*m.x465 + 91.395*m.x466 + 93.846*m.x467 + 94.995*m.x468 + 86.187*m.x469
                        + 92.295*m.x470 + 93.495*m.x471 + 92.259*m.x472 + 93.795*m.x473 + 103.254*m.x474
                        + 103.359*m.x475 + 100.623*m.x476 + 95.418*m.x477 + 92.136*m.x478 + 82.305*m.x479
                        + 68.946*m.x480 + 50.4*m.x481 + 46.287*m.x482 + 44.187*m.x483 + 44.787*m.x484 + 45.477*m.x485
                        + 47.523*m.x486 + 58.359*m.x487 + 68.487*m.x488 + 87.441*m.x489 + 91.395*m.x490 + 93.846*m.x491
                        + 94.995*m.x492 + 86.187*m.x493 + 92.295*m.x494 + 93.495*m.x495 + 92.259*m.x496 + 93.795*m.x497
                        + 103.254*m.x498 + 103.359*m.x499 + 100.623*m.x500 + 95.418*m.x501 + 92.136*m.x502
                        + 82.305*m.x503 + 68.946*m.x504, sense=maximize)

m.c2 = Constraint(expr=   m.x505 + m.x673 + m.x841 == 10.4208)

m.c3 = Constraint(expr=   m.x506 + m.x674 - m.x841 + m.x842 == 0.0708)

m.c4 = Constraint(expr=   m.x507 + m.x675 - m.x842 + m.x843 == 0.0708)

m.c5 = Constraint(expr=   m.x508 + m.x676 - m.x843 + m.x844 == 0.0708)

m.c6 = Constraint(expr=   m.x509 + m.x677 - m.x844 + m.x845 == 0.0708)

m.c7 = Constraint(expr=   m.x510 + m.x678 - m.x845 + m.x846 == 0.0708)

m.c8 = Constraint(expr=   m.x511 + m.x679 - m.x846 + m.x847 == 0.7374)

m.c9 = Constraint(expr=   m.x512 + m.x680 - m.x847 + m.x848 == 0.7374)

m.c10 = Constraint(expr=   m.x513 + m.x681 - m.x848 + m.x849 == 0.7374)

m.c11 = Constraint(expr=   m.x514 + m.x682 - m.x849 + m.x850 == 0.7374)

m.c12 = Constraint(expr=   m.x515 + m.x683 - m.x850 + m.x851 == 0.7374)

m.c13 = Constraint(expr=   m.x516 + m.x684 - m.x851 + m.x852 == 0.7374)

m.c14 = Constraint(expr=   m.x517 + m.x685 - m.x852 + m.x853 == 0.7374)

m.c15 = Constraint(expr=   m.x518 + m.x686 - m.x853 + m.x854 == 0.7374)

m.c16 = Constraint(expr=   m.x519 + m.x687 - m.x854 + m.x855 == 0.7374)

m.c17 = Constraint(expr=   m.x520 + m.x688 - m.x855 + m.x856 == 0.7374)

m.c18 = Constraint(expr=   m.x521 + m.x689 - m.x856 + m.x857 == 0.7374)

m.c19 = Constraint(expr=   m.x522 + m.x690 - m.x857 + m.x858 == 0.7374)

m.c20 = Constraint(expr=   m.x523 + m.x691 - m.x858 + m.x859 == 0.7374)

m.c21 = Constraint(expr=   m.x524 + m.x692 - m.x859 + m.x860 == 0.7374)

m.c22 = Constraint(expr=   m.x525 + m.x693 - m.x860 + m.x861 == 0.7374)

m.c23 = Constraint(expr=   m.x526 + m.x694 - m.x861 + m.x862 == 0.7374)

m.c24 = Constraint(expr=   m.x527 + m.x695 - m.x862 + m.x863 == 0.7374)

m.c25 = Constraint(expr=   m.x528 + m.x696 - m.x863 + m.x864 == 0.7374)

m.c26 = Constraint(expr= - m.x505 + m.x529 - m.x673 + m.x697 + m.x865 == 10.7948)

m.c27 = Constraint(expr= - m.x506 + m.x530 - m.x674 + m.x698 - m.x865 + m.x866 == 0.1548)

m.c28 = Constraint(expr= - m.x507 + m.x531 - m.x675 + m.x699 - m.x866 + m.x867 == 0.1548)

m.c29 = Constraint(expr= - m.x508 + m.x532 - m.x676 + m.x700 - m.x867 + m.x868 == 0.1548)

m.c30 = Constraint(expr= - m.x509 + m.x533 - m.x677 + m.x701 - m.x868 + m.x869 == 0.1548)

m.c31 = Constraint(expr= - m.x510 + m.x534 - m.x678 + m.x702 - m.x869 + m.x870 == 0.1548)

m.c32 = Constraint(expr= - m.x511 + m.x535 - m.x679 + m.x703 - m.x870 + m.x871 == 0.1548)

m.c33 = Constraint(expr= - m.x512 + m.x536 - m.x680 + m.x704 - m.x871 + m.x872 == 0.1548)

m.c34 = Constraint(expr= - m.x513 + m.x537 - m.x681 + m.x705 - m.x872 + m.x873 == 0.1548)

m.c35 = Constraint(expr= - m.x514 + m.x538 - m.x682 + m.x706 - m.x873 + m.x874 == 0.1548)

m.c36 = Constraint(expr= - m.x515 + m.x539 - m.x683 + m.x707 - m.x874 + m.x875 == 0.1548)

m.c37 = Constraint(expr= - m.x516 + m.x540 - m.x684 + m.x708 - m.x875 + m.x876 == 0.1548)

m.c38 = Constraint(expr= - m.x517 + m.x541 - m.x685 + m.x709 - m.x876 + m.x877 == 0.1548)

m.c39 = Constraint(expr= - m.x518 + m.x542 - m.x686 + m.x710 - m.x877 + m.x878 == 0.1548)

m.c40 = Constraint(expr= - m.x519 + m.x543 - m.x687 + m.x711 - m.x878 + m.x879 == 0.1548)

m.c41 = Constraint(expr= - m.x520 + m.x544 - m.x688 + m.x712 - m.x879 + m.x880 == 0.1548)

m.c42 = Constraint(expr= - m.x521 + m.x545 - m.x689 + m.x713 - m.x880 + m.x881 == 0.1548)

m.c43 = Constraint(expr= - m.x522 + m.x546 - m.x690 + m.x714 - m.x881 + m.x882 == 0.1548)

m.c44 = Constraint(expr= - m.x523 + m.x547 - m.x691 + m.x715 - m.x882 + m.x883 == 0.1548)

m.c45 = Constraint(expr= - m.x524 + m.x548 - m.x692 + m.x716 - m.x883 + m.x884 == 0.1548)

m.c46 = Constraint(expr= - m.x525 + m.x549 - m.x693 + m.x717 - m.x884 + m.x885 == 0.1548)

m.c47 = Constraint(expr= - m.x526 + m.x550 - m.x694 + m.x718 - m.x885 + m.x886 == 0.1548)

m.c48 = Constraint(expr= - m.x527 + m.x551 - m.x695 + m.x719 - m.x886 + m.x887 == 0.1548)

m.c49 = Constraint(expr= - m.x528 + m.x552 - m.x696 + m.x720 - m.x887 + m.x888 == 0.1548)

m.c50 = Constraint(expr=   m.x553 + m.x721 + m.x889 == 78.0108)

m.c51 = Constraint(expr=   m.x554 + m.x722 - m.x889 + m.x890 == 0.0108)

m.c52 = Constraint(expr=   m.x555 + m.x723 - m.x890 + m.x891 == 0.0108)

m.c53 = Constraint(expr=   m.x556 + m.x724 - m.x891 + m.x892 == 0.0108)

m.c54 = Constraint(expr=   m.x557 + m.x725 - m.x892 + m.x893 == 0.0108)

m.c55 = Constraint(expr=   m.x558 + m.x726 - m.x893 + m.x894 == 0.0108)

m.c56 = Constraint(expr=   m.x559 + m.x727 - m.x894 + m.x895 == 0.0108)

m.c57 = Constraint(expr=   m.x560 + m.x728 - m.x895 + m.x896 == 0.0108)

m.c58 = Constraint(expr=   m.x561 + m.x729 - m.x896 + m.x897 == 0.0108)

m.c59 = Constraint(expr=   m.x562 + m.x730 - m.x897 + m.x898 == 0.0108)

m.c60 = Constraint(expr=   m.x563 + m.x731 - m.x898 + m.x899 == 0.0108)

m.c61 = Constraint(expr=   m.x564 + m.x732 - m.x899 + m.x900 == 0.0108)

m.c62 = Constraint(expr=   m.x565 + m.x733 - m.x900 + m.x901 == 0.0108)

m.c63 = Constraint(expr=   m.x566 + m.x734 - m.x901 + m.x902 == 0.0108)

m.c64 = Constraint(expr=   m.x567 + m.x735 - m.x902 + m.x903 == 0.0108)

m.c65 = Constraint(expr=   m.x568 + m.x736 - m.x903 + m.x904 == 0.0108)

m.c66 = Constraint(expr=   m.x569 + m.x737 - m.x904 + m.x905 == 0.0108)

m.c67 = Constraint(expr=   m.x570 + m.x738 - m.x905 + m.x906 == 0.0108)

m.c68 = Constraint(expr=   m.x571 + m.x739 - m.x906 + m.x907 == 0.0108)

m.c69 = Constraint(expr=   m.x572 + m.x740 - m.x907 + m.x908 == 0.0108)

m.c70 = Constraint(expr=   m.x573 + m.x741 - m.x908 + m.x909 == 0.0108)

m.c71 = Constraint(expr=   m.x574 + m.x742 - m.x909 + m.x910 == 0.0108)

m.c72 = Constraint(expr=   m.x575 + m.x743 - m.x910 + m.x911 == 0.0108)

m.c73 = Constraint(expr=   m.x576 + m.x744 - m.x911 + m.x912 == 0.0108)

m.c74 = Constraint(expr= - m.x529 - m.x553 + m.x577 - m.x697 - m.x721 + m.x745 + m.x913 == 9.7115)

m.c75 = Constraint(expr= - m.x530 - m.x554 + m.x578 - m.x698 - m.x722 + m.x746 - m.x913 + m.x914 == 0.1115)

m.c76 = Constraint(expr= - m.x531 - m.x555 + m.x579 - m.x699 - m.x723 + m.x747 - m.x914 + m.x915 == 0.1115)

m.c77 = Constraint(expr= - m.x532 - m.x556 + m.x580 - m.x700 - m.x724 + m.x748 - m.x915 + m.x916 == 0.1115)

m.c78 = Constraint(expr= - m.x533 - m.x557 + m.x581 - m.x701 - m.x725 + m.x749 - m.x916 + m.x917 == 0.1115)

m.c79 = Constraint(expr= - m.x534 - m.x558 + m.x582 - m.x702 - m.x726 + m.x750 - m.x917 + m.x918 == 0.1115)

m.c80 = Constraint(expr= - m.x535 - m.x559 + m.x583 - m.x703 - m.x727 + m.x751 - m.x918 + m.x919 == 0.1115)

m.c81 = Constraint(expr= - m.x536 - m.x560 + m.x584 - m.x704 - m.x728 + m.x752 - m.x919 + m.x920 == 0.1115)

m.c82 = Constraint(expr= - m.x537 - m.x561 + m.x585 - m.x705 - m.x729 + m.x753 - m.x920 + m.x921 == 0.1115)

m.c83 = Constraint(expr= - m.x538 - m.x562 + m.x586 - m.x706 - m.x730 + m.x754 - m.x921 + m.x922 == 0.1115)

m.c84 = Constraint(expr= - m.x539 - m.x563 + m.x587 - m.x707 - m.x731 + m.x755 - m.x922 + m.x923 == 0.1115)

m.c85 = Constraint(expr= - m.x540 - m.x564 + m.x588 - m.x708 - m.x732 + m.x756 - m.x923 + m.x924 == 0.1115)

m.c86 = Constraint(expr= - m.x541 - m.x565 + m.x589 - m.x709 - m.x733 + m.x757 - m.x924 + m.x925 == 0.1115)

m.c87 = Constraint(expr= - m.x542 - m.x566 + m.x590 - m.x710 - m.x734 + m.x758 - m.x925 + m.x926 == 0.1115)

m.c88 = Constraint(expr= - m.x543 - m.x567 + m.x591 - m.x711 - m.x735 + m.x759 - m.x926 + m.x927 == 0.1115)

m.c89 = Constraint(expr= - m.x544 - m.x568 + m.x592 - m.x712 - m.x736 + m.x760 - m.x927 + m.x928 == 0.1115)

m.c90 = Constraint(expr= - m.x545 - m.x569 + m.x593 - m.x713 - m.x737 + m.x761 - m.x928 + m.x929 == 0.1115)

m.c91 = Constraint(expr= - m.x546 - m.x570 + m.x594 - m.x714 - m.x738 + m.x762 - m.x929 + m.x930 == 0.1115)

m.c92 = Constraint(expr= - m.x547 - m.x571 + m.x595 - m.x715 - m.x739 + m.x763 - m.x930 + m.x931 == 0.1115)

m.c93 = Constraint(expr= - m.x548 - m.x572 + m.x596 - m.x716 - m.x740 + m.x764 - m.x931 + m.x932 == 0.1115)

m.c94 = Constraint(expr= - m.x549 - m.x573 + m.x597 - m.x717 - m.x741 + m.x765 - m.x932 + m.x933 == 0.1115)

m.c95 = Constraint(expr= - m.x550 - m.x574 + m.x598 - m.x718 - m.x742 + m.x766 - m.x933 + m.x934 == 0.1115)

m.c96 = Constraint(expr= - m.x551 - m.x575 + m.x599 - m.x719 - m.x743 + m.x767 - m.x934 + m.x935 == 0.1115)

m.c97 = Constraint(expr= - m.x552 - m.x576 + m.x600 - m.x720 - m.x744 + m.x768 - m.x935 + m.x936 == 0.1115)

m.c98 = Constraint(expr= - m.x577 + m.x601 - m.x745 + m.x769 + m.x937 == 8.8143)

m.c99 = Constraint(expr= - m.x578 + m.x602 - m.x746 + m.x770 - m.x937 + m.x938 == 0.0143)

m.c100 = Constraint(expr= - m.x579 + m.x603 - m.x747 + m.x771 - m.x938 + m.x939 == 0.0143)

m.c101 = Constraint(expr= - m.x580 + m.x604 - m.x748 + m.x772 - m.x939 + m.x940 == 0.0143)

m.c102 = Constraint(expr= - m.x581 + m.x605 - m.x749 + m.x773 - m.x940 + m.x941 == 0.0143)

m.c103 = Constraint(expr= - m.x582 + m.x606 - m.x750 + m.x774 - m.x941 + m.x942 == 0.0143)

m.c104 = Constraint(expr= - m.x583 + m.x607 - m.x751 + m.x775 - m.x942 + m.x943 == 0.0143)

m.c105 = Constraint(expr= - m.x584 + m.x608 - m.x752 + m.x776 - m.x943 + m.x944 == 0.0143)

m.c106 = Constraint(expr= - m.x585 + m.x609 - m.x753 + m.x777 - m.x944 + m.x945 == 0.0143)

m.c107 = Constraint(expr= - m.x586 + m.x610 - m.x754 + m.x778 - m.x945 + m.x946 == 0.0143)

m.c108 = Constraint(expr= - m.x587 + m.x611 - m.x755 + m.x779 - m.x946 + m.x947 == 0.0143)

m.c109 = Constraint(expr= - m.x588 + m.x612 - m.x756 + m.x780 - m.x947 + m.x948 == 0.0143)

m.c110 = Constraint(expr= - m.x589 + m.x613 - m.x757 + m.x781 - m.x948 + m.x949 == 0.0143)

m.c111 = Constraint(expr= - m.x590 + m.x614 - m.x758 + m.x782 - m.x949 + m.x950 == 0.0143)

m.c112 = Constraint(expr= - m.x591 + m.x615 - m.x759 + m.x783 - m.x950 + m.x951 == 0.0143)

m.c113 = Constraint(expr= - m.x592 + m.x616 - m.x760 + m.x784 - m.x951 + m.x952 == 0.0143)

m.c114 = Constraint(expr= - m.x593 + m.x617 - m.x761 + m.x785 - m.x952 + m.x953 == 0.0143)

m.c115 = Constraint(expr= - m.x594 + m.x618 - m.x762 + m.x786 - m.x953 + m.x954 == 0.0143)

m.c116 = Constraint(expr= - m.x595 + m.x619 - m.x763 + m.x787 - m.x954 + m.x955 == 0.0143)

m.c117 = Constraint(expr= - m.x596 + m.x620 - m.x764 + m.x788 - m.x955 + m.x956 == 0.0143)

m.c118 = Constraint(expr= - m.x597 + m.x621 - m.x765 + m.x789 - m.x956 + m.x957 == 0.0143)

m.c119 = Constraint(expr= - m.x598 + m.x622 - m.x766 + m.x790 - m.x957 + m.x958 == 0.0143)

m.c120 = Constraint(expr= - m.x599 + m.x623 - m.x767 + m.x791 - m.x958 + m.x959 == 0.0143)

m.c121 = Constraint(expr= - m.x600 + m.x624 - m.x768 + m.x792 - m.x959 + m.x960 == 0.0143)

m.c122 = Constraint(expr=   m.x625 + m.x793 + m.x961 == 47.204)

m.c123 = Constraint(expr=   m.x626 + m.x794 - m.x961 + m.x962 == 0.504)

m.c124 = Constraint(expr=   m.x627 + m.x795 - m.x962 + m.x963 == 0.504)

m.c125 = Constraint(expr=   m.x628 + m.x796 - m.x963 + m.x964 == 0.504)

m.c126 = Constraint(expr=   m.x629 + m.x797 - m.x964 + m.x965 == 0.504)

m.c127 = Constraint(expr=   m.x630 + m.x798 - m.x965 + m.x966 == 0.504)

m.c128 = Constraint(expr=   m.x631 + m.x799 - m.x966 + m.x967 == 0.504)

m.c129 = Constraint(expr=   m.x632 + m.x800 - m.x967 + m.x968 == 0.504)

m.c130 = Constraint(expr=   m.x633 + m.x801 - m.x968 + m.x969 == 0.504)

m.c131 = Constraint(expr=   m.x634 + m.x802 - m.x969 + m.x970 == 0.504)

m.c132 = Constraint(expr=   m.x635 + m.x803 - m.x970 + m.x971 == 0.504)

m.c133 = Constraint(expr=   m.x636 + m.x804 - m.x971 + m.x972 == 0.504)

m.c134 = Constraint(expr=   m.x637 + m.x805 - m.x972 + m.x973 == 0.504)

m.c135 = Constraint(expr=   m.x638 + m.x806 - m.x973 + m.x974 == 0.504)

m.c136 = Constraint(expr=   m.x639 + m.x807 - m.x974 + m.x975 == 0.504)

m.c137 = Constraint(expr=   m.x640 + m.x808 - m.x975 + m.x976 == 0.504)

m.c138 = Constraint(expr=   m.x641 + m.x809 - m.x976 + m.x977 == 0.504)

m.c139 = Constraint(expr=   m.x642 + m.x810 - m.x977 + m.x978 == 0.504)

m.c140 = Constraint(expr=   m.x643 + m.x811 - m.x978 + m.x979 == 0.504)

m.c141 = Constraint(expr=   m.x644 + m.x812 - m.x979 + m.x980 == 0.504)

m.c142 = Constraint(expr=   m.x645 + m.x813 - m.x980 + m.x981 == 0.504)

m.c143 = Constraint(expr=   m.x646 + m.x814 - m.x981 + m.x982 == 0.504)

m.c144 = Constraint(expr=   m.x647 + m.x815 - m.x982 + m.x983 == 0.504)

m.c145 = Constraint(expr=   m.x648 + m.x816 - m.x983 + m.x984 == 0.504)

m.c146 = Constraint(expr= - m.x601 - m.x625 + m.x649 - m.x769 - m.x793 + m.x817 + m.x985 == 17.2)

m.c147 = Constraint(expr= - m.x602 - m.x626 + m.x650 - m.x770 - m.x794 + m.x818 - m.x985 + m.x986 == 0)

m.c148 = Constraint(expr= - m.x603 - m.x627 + m.x651 - m.x771 - m.x795 + m.x819 - m.x986 + m.x987 == 0)

m.c149 = Constraint(expr= - m.x604 - m.x628 + m.x652 - m.x772 - m.x796 + m.x820 - m.x987 + m.x988 == 0)

m.c150 = Constraint(expr= - m.x605 - m.x629 + m.x653 - m.x773 - m.x797 + m.x821 - m.x988 + m.x989 == 0)

m.c151 = Constraint(expr= - m.x606 - m.x630 + m.x654 - m.x774 - m.x798 + m.x822 - m.x989 + m.x990 == 0)

m.c152 = Constraint(expr= - m.x607 - m.x631 + m.x655 - m.x775 - m.x799 + m.x823 - m.x990 + m.x991 == 0)

m.c153 = Constraint(expr= - m.x608 - m.x632 + m.x656 - m.x776 - m.x800 + m.x824 - m.x991 + m.x992 == 0)

m.c154 = Constraint(expr= - m.x609 - m.x633 + m.x657 - m.x777 - m.x801 + m.x825 - m.x992 + m.x993 == 0)

m.c155 = Constraint(expr= - m.x610 - m.x634 + m.x658 - m.x778 - m.x802 + m.x826 - m.x993 + m.x994 == 0)

m.c156 = Constraint(expr= - m.x611 - m.x635 + m.x659 - m.x779 - m.x803 + m.x827 - m.x994 + m.x995 == 0)

m.c157 = Constraint(expr= - m.x612 - m.x636 + m.x660 - m.x780 - m.x804 + m.x828 - m.x995 + m.x996 == 0)

m.c158 = Constraint(expr= - m.x613 - m.x637 + m.x661 - m.x781 - m.x805 + m.x829 - m.x996 + m.x997 == 0)

m.c159 = Constraint(expr= - m.x614 - m.x638 + m.x662 - m.x782 - m.x806 + m.x830 - m.x997 + m.x998 == 0)

m.c160 = Constraint(expr= - m.x615 - m.x639 + m.x663 - m.x783 - m.x807 + m.x831 - m.x998 + m.x999 == 0)

m.c161 = Constraint(expr= - m.x616 - m.x640 + m.x664 - m.x784 - m.x808 + m.x832 - m.x999 + m.x1000 == 0)

m.c162 = Constraint(expr= - m.x617 - m.x641 + m.x665 - m.x785 - m.x809 + m.x833 - m.x1000 + m.x1001 == 0)

m.c163 = Constraint(expr= - m.x618 - m.x642 + m.x666 - m.x786 - m.x810 + m.x834 - m.x1001 + m.x1002 == 0)

m.c164 = Constraint(expr= - m.x619 - m.x643 + m.x667 - m.x787 - m.x811 + m.x835 - m.x1002 + m.x1003 == 0)

m.c165 = Constraint(expr= - m.x620 - m.x644 + m.x668 - m.x788 - m.x812 + m.x836 - m.x1003 + m.x1004 == 0)

m.c166 = Constraint(expr= - m.x621 - m.x645 + m.x669 - m.x789 - m.x813 + m.x837 - m.x1004 + m.x1005 == 0)

m.c167 = Constraint(expr= - m.x622 - m.x646 + m.x670 - m.x790 - m.x814 + m.x838 - m.x1005 + m.x1006 == 0)

m.c168 = Constraint(expr= - m.x623 - m.x647 + m.x671 - m.x791 - m.x815 + m.x839 - m.x1006 + m.x1007 == 0)

m.c169 = Constraint(expr= - m.x624 - m.x648 + m.x672 - m.x792 - m.x816 + m.x840 - m.x1007 + m.x1008 == 0)

m.c170 = Constraint(expr= - 4.1202*m.b1 + m.x673 <= 0)

m.c171 = Constraint(expr= - 4.1202*m.b2 + m.x674 <= 0)

m.c172 = Constraint(expr= - 4.1202*m.b3 + m.x675 <= 0)

m.c173 = Constraint(expr= - 4.1202*m.b4 + m.x676 <= 0)

m.c174 = Constraint(expr= - 4.1202*m.b5 + m.x677 <= 0)

m.c175 = Constraint(expr= - 4.1202*m.b6 + m.x678 <= 0)

m.c176 = Constraint(expr= - 4.1202*m.b7 + m.x679 <= 0)

m.c177 = Constraint(expr= - 4.1202*m.b8 + m.x680 <= 0)

m.c178 = Constraint(expr= - 4.1202*m.b9 + m.x681 <= 0)

m.c179 = Constraint(expr= - 4.1202*m.b10 + m.x682 <= 0)

m.c180 = Constraint(expr= - 4.1202*m.b11 + m.x683 <= 0)

m.c181 = Constraint(expr= - 4.1202*m.b12 + m.x684 <= 0)

m.c182 = Constraint(expr= - 4.1202*m.b13 + m.x685 <= 0)

m.c183 = Constraint(expr= - 4.1202*m.b14 + m.x686 <= 0)

m.c184 = Constraint(expr= - 4.1202*m.b15 + m.x687 <= 0)

m.c185 = Constraint(expr= - 4.1202*m.b16 + m.x688 <= 0)

m.c186 = Constraint(expr= - 4.1202*m.b17 + m.x689 <= 0)

m.c187 = Constraint(expr= - 4.1202*m.b18 + m.x690 <= 0)

m.c188 = Constraint(expr= - 4.1202*m.b19 + m.x691 <= 0)

m.c189 = Constraint(expr= - 4.1202*m.b20 + m.x692 <= 0)

m.c190 = Constraint(expr= - 4.1202*m.b21 + m.x693 <= 0)

m.c191 = Constraint(expr= - 4.1202*m.b22 + m.x694 <= 0)

m.c192 = Constraint(expr= - 4.1202*m.b23 + m.x695 <= 0)

m.c193 = Constraint(expr= - 4.1202*m.b24 + m.x696 <= 0)

m.c194 = Constraint(expr= - 3.888*m.b25 + m.x697 <= 0)

m.c195 = Constraint(expr= - 3.888*m.b26 + m.x698 <= 0)

m.c196 = Constraint(expr= - 3.888*m.b27 + m.x699 <= 0)

m.c197 = Constraint(expr= - 3.888*m.b28 + m.x700 <= 0)

m.c198 = Constraint(expr= - 3.888*m.b29 + m.x701 <= 0)

m.c199 = Constraint(expr= - 3.888*m.b30 + m.x702 <= 0)

m.c200 = Constraint(expr= - 3.888*m.b31 + m.x703 <= 0)

m.c201 = Constraint(expr= - 3.888*m.b32 + m.x704 <= 0)

m.c202 = Constraint(expr= - 3.888*m.b33 + m.x705 <= 0)

m.c203 = Constraint(expr= - 3.888*m.b34 + m.x706 <= 0)

m.c204 = Constraint(expr= - 3.888*m.b35 + m.x707 <= 0)

m.c205 = Constraint(expr= - 3.888*m.b36 + m.x708 <= 0)

m.c206 = Constraint(expr= - 3.888*m.b37 + m.x709 <= 0)

m.c207 = Constraint(expr= - 3.888*m.b38 + m.x710 <= 0)

m.c208 = Constraint(expr= - 3.888*m.b39 + m.x711 <= 0)

m.c209 = Constraint(expr= - 3.888*m.b40 + m.x712 <= 0)

m.c210 = Constraint(expr= - 3.888*m.b41 + m.x713 <= 0)

m.c211 = Constraint(expr= - 3.888*m.b42 + m.x714 <= 0)

m.c212 = Constraint(expr= - 3.888*m.b43 + m.x715 <= 0)

m.c213 = Constraint(expr= - 3.888*m.b44 + m.x716 <= 0)

m.c214 = Constraint(expr= - 3.888*m.b45 + m.x717 <= 0)

m.c215 = Constraint(expr= - 3.888*m.b46 + m.x718 <= 0)

m.c216 = Constraint(expr= - 3.888*m.b47 + m.x719 <= 0)

m.c217 = Constraint(expr= - 3.888*m.b48 + m.x720 <= 0)

m.c218 = Constraint(expr= - 0.05904*m.b49 + m.x721 <= 0)

m.c219 = Constraint(expr= - 0.05904*m.b50 + m.x722 <= 0)

m.c220 = Constraint(expr= - 0.05904*m.b51 + m.x723 <= 0)

m.c221 = Constraint(expr= - 0.05904*m.b52 + m.x724 <= 0)

m.c222 = Constraint(expr= - 0.05904*m.b53 + m.x725 <= 0)

m.c223 = Constraint(expr= - 0.05904*m.b54 + m.x726 <= 0)

m.c224 = Constraint(expr= - 0.05904*m.b55 + m.x727 <= 0)

m.c225 = Constraint(expr= - 0.05904*m.b56 + m.x728 <= 0)

m.c226 = Constraint(expr= - 0.05904*m.b57 + m.x729 <= 0)

m.c227 = Constraint(expr= - 0.05904*m.b58 + m.x730 <= 0)

m.c228 = Constraint(expr= - 0.05904*m.b59 + m.x731 <= 0)

m.c229 = Constraint(expr= - 0.05904*m.b60 + m.x732 <= 0)

m.c230 = Constraint(expr= - 0.05904*m.b61 + m.x733 <= 0)

m.c231 = Constraint(expr= - 0.05904*m.b62 + m.x734 <= 0)

m.c232 = Constraint(expr= - 0.05904*m.b63 + m.x735 <= 0)

m.c233 = Constraint(expr= - 0.05904*m.b64 + m.x736 <= 0)

m.c234 = Constraint(expr= - 0.05904*m.b65 + m.x737 <= 0)

m.c235 = Constraint(expr= - 0.05904*m.b66 + m.x738 <= 0)

m.c236 = Constraint(expr= - 0.05904*m.b67 + m.x739 <= 0)

m.c237 = Constraint(expr= - 0.05904*m.b68 + m.x740 <= 0)

m.c238 = Constraint(expr= - 0.05904*m.b69 + m.x741 <= 0)

m.c239 = Constraint(expr= - 0.05904*m.b70 + m.x742 <= 0)

m.c240 = Constraint(expr= - 0.05904*m.b71 + m.x743 <= 0)

m.c241 = Constraint(expr= - 0.05904*m.b72 + m.x744 <= 0)

m.c242 = Constraint(expr= - 3.24*m.b73 + m.x745 <= 0)

m.c243 = Constraint(expr= - 3.24*m.b74 + m.x746 <= 0)

m.c244 = Constraint(expr= - 3.24*m.b75 + m.x747 <= 0)

m.c245 = Constraint(expr= - 3.24*m.b76 + m.x748 <= 0)

m.c246 = Constraint(expr= - 3.24*m.b77 + m.x749 <= 0)

m.c247 = Constraint(expr= - 3.24*m.b78 + m.x750 <= 0)

m.c248 = Constraint(expr= - 3.24*m.b79 + m.x751 <= 0)

m.c249 = Constraint(expr= - 3.24*m.b80 + m.x752 <= 0)

m.c250 = Constraint(expr= - 3.24*m.b81 + m.x753 <= 0)

m.c251 = Constraint(expr= - 3.24*m.b82 + m.x754 <= 0)

m.c252 = Constraint(expr= - 3.24*m.b83 + m.x755 <= 0)

m.c253 = Constraint(expr= - 3.24*m.b84 + m.x756 <= 0)

m.c254 = Constraint(expr= - 3.24*m.b85 + m.x757 <= 0)

m.c255 = Constraint(expr= - 3.24*m.b86 + m.x758 <= 0)

m.c256 = Constraint(expr= - 3.24*m.b87 + m.x759 <= 0)

m.c257 = Constraint(expr= - 3.24*m.b88 + m.x760 <= 0)

m.c258 = Constraint(expr= - 3.24*m.b89 + m.x761 <= 0)

m.c259 = Constraint(expr= - 3.24*m.b90 + m.x762 <= 0)

m.c260 = Constraint(expr= - 3.24*m.b91 + m.x763 <= 0)

m.c261 = Constraint(expr= - 3.24*m.b92 + m.x764 <= 0)

m.c262 = Constraint(expr= - 3.24*m.b93 + m.x765 <= 0)

m.c263 = Constraint(expr= - 3.24*m.b94 + m.x766 <= 0)

m.c264 = Constraint(expr= - 3.24*m.b95 + m.x767 <= 0)

m.c265 = Constraint(expr= - 3.24*m.b96 + m.x768 <= 0)

m.c266 = Constraint(expr= - 3.172716*m.b97 + m.x769 <= 0)

m.c267 = Constraint(expr= - 3.172716*m.b98 + m.x770 <= 0)

m.c268 = Constraint(expr= - 3.172716*m.b99 + m.x771 <= 0)

m.c269 = Constraint(expr= - 3.172716*m.b100 + m.x772 <= 0)

m.c270 = Constraint(expr= - 3.172716*m.b101 + m.x773 <= 0)

m.c271 = Constraint(expr= - 3.172716*m.b102 + m.x774 <= 0)

m.c272 = Constraint(expr= - 3.172716*m.b103 + m.x775 <= 0)

m.c273 = Constraint(expr= - 3.172716*m.b104 + m.x776 <= 0)

m.c274 = Constraint(expr= - 3.172716*m.b105 + m.x777 <= 0)

m.c275 = Constraint(expr= - 3.172716*m.b106 + m.x778 <= 0)

m.c276 = Constraint(expr= - 3.172716*m.b107 + m.x779 <= 0)

m.c277 = Constraint(expr= - 3.172716*m.b108 + m.x780 <= 0)

m.c278 = Constraint(expr= - 3.172716*m.b109 + m.x781 <= 0)

m.c279 = Constraint(expr= - 3.172716*m.b110 + m.x782 <= 0)

m.c280 = Constraint(expr= - 3.172716*m.b111 + m.x783 <= 0)

m.c281 = Constraint(expr= - 3.172716*m.b112 + m.x784 <= 0)

m.c282 = Constraint(expr= - 3.172716*m.b113 + m.x785 <= 0)

m.c283 = Constraint(expr= - 3.172716*m.b114 + m.x786 <= 0)

m.c284 = Constraint(expr= - 3.172716*m.b115 + m.x787 <= 0)

m.c285 = Constraint(expr= - 3.172716*m.b116 + m.x788 <= 0)

m.c286 = Constraint(expr= - 3.172716*m.b117 + m.x789 <= 0)

m.c287 = Constraint(expr= - 3.172716*m.b118 + m.x790 <= 0)

m.c288 = Constraint(expr= - 3.172716*m.b119 + m.x791 <= 0)

m.c289 = Constraint(expr= - 3.172716*m.b120 + m.x792 <= 0)

m.c290 = Constraint(expr= - 1.174824*m.b121 + m.x793 <= 0)

m.c291 = Constraint(expr= - 1.174824*m.b122 + m.x794 <= 0)

m.c292 = Constraint(expr= - 1.174824*m.b123 + m.x795 <= 0)

m.c293 = Constraint(expr= - 1.174824*m.b124 + m.x796 <= 0)

m.c294 = Constraint(expr= - 1.174824*m.b125 + m.x797 <= 0)

m.c295 = Constraint(expr= - 1.174824*m.b126 + m.x798 <= 0)

m.c296 = Constraint(expr= - 1.174824*m.b127 + m.x799 <= 0)

m.c297 = Constraint(expr= - 1.174824*m.b128 + m.x800 <= 0)

m.c298 = Constraint(expr= - 1.174824*m.b129 + m.x801 <= 0)

m.c299 = Constraint(expr= - 1.174824*m.b130 + m.x802 <= 0)

m.c300 = Constraint(expr= - 1.174824*m.b131 + m.x803 <= 0)

m.c301 = Constraint(expr= - 1.174824*m.b132 + m.x804 <= 0)

m.c302 = Constraint(expr= - 1.174824*m.b133 + m.x805 <= 0)

m.c303 = Constraint(expr= - 1.174824*m.b134 + m.x806 <= 0)

m.c304 = Constraint(expr= - 1.174824*m.b135 + m.x807 <= 0)

m.c305 = Constraint(expr= - 1.174824*m.b136 + m.x808 <= 0)

m.c306 = Constraint(expr= - 1.174824*m.b137 + m.x809 <= 0)

m.c307 = Constraint(expr= - 1.174824*m.b138 + m.x810 <= 0)

m.c308 = Constraint(expr= - 1.174824*m.b139 + m.x811 <= 0)

m.c309 = Constraint(expr= - 1.174824*m.b140 + m.x812 <= 0)

m.c310 = Constraint(expr= - 1.174824*m.b141 + m.x813 <= 0)

m.c311 = Constraint(expr= - 1.174824*m.b142 + m.x814 <= 0)

m.c312 = Constraint(expr= - 1.174824*m.b143 + m.x815 <= 0)

m.c313 = Constraint(expr= - 1.174824*m.b144 + m.x816 <= 0)

m.c314 = Constraint(expr= - 4.883436*m.b145 + m.x817 <= 0)

m.c315 = Constraint(expr= - 4.883436*m.b146 + m.x818 <= 0)

m.c316 = Constraint(expr= - 4.883436*m.b147 + m.x819 <= 0)

m.c317 = Constraint(expr= - 4.883436*m.b148 + m.x820 <= 0)

m.c318 = Constraint(expr= - 4.883436*m.b149 + m.x821 <= 0)

m.c319 = Constraint(expr= - 4.883436*m.b150 + m.x822 <= 0)

m.c320 = Constraint(expr= - 4.883436*m.b151 + m.x823 <= 0)

m.c321 = Constraint(expr= - 4.883436*m.b152 + m.x824 <= 0)

m.c322 = Constraint(expr= - 4.883436*m.b153 + m.x825 <= 0)

m.c323 = Constraint(expr= - 4.883436*m.b154 + m.x826 <= 0)

m.c324 = Constraint(expr= - 4.883436*m.b155 + m.x827 <= 0)

m.c325 = Constraint(expr= - 4.883436*m.b156 + m.x828 <= 0)

m.c326 = Constraint(expr= - 4.883436*m.b157 + m.x829 <= 0)

m.c327 = Constraint(expr= - 4.883436*m.b158 + m.x830 <= 0)

m.c328 = Constraint(expr= - 4.883436*m.b159 + m.x831 <= 0)

m.c329 = Constraint(expr= - 4.883436*m.b160 + m.x832 <= 0)

m.c330 = Constraint(expr= - 4.883436*m.b161 + m.x833 <= 0)

m.c331 = Constraint(expr= - 4.883436*m.b162 + m.x834 <= 0)

m.c332 = Constraint(expr= - 4.883436*m.b163 + m.x835 <= 0)

m.c333 = Constraint(expr= - 4.883436*m.b164 + m.x836 <= 0)

m.c334 = Constraint(expr= - 4.883436*m.b165 + m.x837 <= 0)

m.c335 = Constraint(expr= - 4.883436*m.b166 + m.x838 <= 0)

m.c336 = Constraint(expr= - 4.883436*m.b167 + m.x839 <= 0)

m.c337 = Constraint(expr= - 4.883436*m.b168 + m.x840 <= 0)

m.c338 = Constraint(expr= - 0.605268*m.b1 + m.x673 >= 0)

m.c339 = Constraint(expr= - 0.605268*m.b2 + m.x674 >= 0)

m.c340 = Constraint(expr= - 0.605268*m.b3 + m.x675 >= 0)

m.c341 = Constraint(expr= - 0.605268*m.b4 + m.x676 >= 0)

m.c342 = Constraint(expr= - 0.605268*m.b5 + m.x677 >= 0)

m.c343 = Constraint(expr= - 0.605268*m.b6 + m.x678 >= 0)

m.c344 = Constraint(expr= - 0.605268*m.b7 + m.x679 >= 0)

m.c345 = Constraint(expr= - 0.605268*m.b8 + m.x680 >= 0)

m.c346 = Constraint(expr= - 0.605268*m.b9 + m.x681 >= 0)

m.c347 = Constraint(expr= - 0.605268*m.b10 + m.x682 >= 0)

m.c348 = Constraint(expr= - 0.605268*m.b11 + m.x683 >= 0)

m.c349 = Constraint(expr= - 0.605268*m.b12 + m.x684 >= 0)

m.c350 = Constraint(expr= - 0.605268*m.b13 + m.x685 >= 0)

m.c351 = Constraint(expr= - 0.605268*m.b14 + m.x686 >= 0)

m.c352 = Constraint(expr= - 0.605268*m.b15 + m.x687 >= 0)

m.c353 = Constraint(expr= - 0.605268*m.b16 + m.x688 >= 0)

m.c354 = Constraint(expr= - 0.605268*m.b17 + m.x689 >= 0)

m.c355 = Constraint(expr= - 0.605268*m.b18 + m.x690 >= 0)

m.c356 = Constraint(expr= - 0.605268*m.b19 + m.x691 >= 0)

m.c357 = Constraint(expr= - 0.605268*m.b20 + m.x692 >= 0)

m.c358 = Constraint(expr= - 0.605268*m.b21 + m.x693 >= 0)

m.c359 = Constraint(expr= - 0.605268*m.b22 + m.x694 >= 0)

m.c360 = Constraint(expr= - 0.605268*m.b23 + m.x695 >= 0)

m.c361 = Constraint(expr= - 0.605268*m.b24 + m.x696 >= 0)

m.c362 = Constraint(expr= - 0.37692*m.b25 + m.x697 >= 0)

m.c363 = Constraint(expr= - 0.37692*m.b26 + m.x698 >= 0)

m.c364 = Constraint(expr= - 0.37692*m.b27 + m.x699 >= 0)

m.c365 = Constraint(expr= - 0.37692*m.b28 + m.x700 >= 0)

m.c366 = Constraint(expr= - 0.37692*m.b29 + m.x701 >= 0)

m.c367 = Constraint(expr= - 0.37692*m.b30 + m.x702 >= 0)

m.c368 = Constraint(expr= - 0.37692*m.b31 + m.x703 >= 0)

m.c369 = Constraint(expr= - 0.37692*m.b32 + m.x704 >= 0)

m.c370 = Constraint(expr= - 0.37692*m.b33 + m.x705 >= 0)

m.c371 = Constraint(expr= - 0.37692*m.b34 + m.x706 >= 0)

m.c372 = Constraint(expr= - 0.37692*m.b35 + m.x707 >= 0)

m.c373 = Constraint(expr= - 0.37692*m.b36 + m.x708 >= 0)

m.c374 = Constraint(expr= - 0.37692*m.b37 + m.x709 >= 0)

m.c375 = Constraint(expr= - 0.37692*m.b38 + m.x710 >= 0)

m.c376 = Constraint(expr= - 0.37692*m.b39 + m.x711 >= 0)

m.c377 = Constraint(expr= - 0.37692*m.b40 + m.x712 >= 0)

m.c378 = Constraint(expr= - 0.37692*m.b41 + m.x713 >= 0)

m.c379 = Constraint(expr= - 0.37692*m.b42 + m.x714 >= 0)

m.c380 = Constraint(expr= - 0.37692*m.b43 + m.x715 >= 0)

m.c381 = Constraint(expr= - 0.37692*m.b44 + m.x716 >= 0)

m.c382 = Constraint(expr= - 0.37692*m.b45 + m.x717 >= 0)

m.c383 = Constraint(expr= - 0.37692*m.b46 + m.x718 >= 0)

m.c384 = Constraint(expr= - 0.37692*m.b47 + m.x719 >= 0)

m.c385 = Constraint(expr= - 0.37692*m.b48 + m.x720 >= 0)

m.c386 = Constraint(expr= - 0.0108*m.b49 + m.x721 >= 0)

m.c387 = Constraint(expr= - 0.0108*m.b50 + m.x722 >= 0)

m.c388 = Constraint(expr= - 0.0108*m.b51 + m.x723 >= 0)

m.c389 = Constraint(expr= - 0.0108*m.b52 + m.x724 >= 0)

m.c390 = Constraint(expr= - 0.0108*m.b53 + m.x725 >= 0)

m.c391 = Constraint(expr= - 0.0108*m.b54 + m.x726 >= 0)

m.c392 = Constraint(expr= - 0.0108*m.b55 + m.x727 >= 0)

m.c393 = Constraint(expr= - 0.0108*m.b56 + m.x728 >= 0)

m.c394 = Constraint(expr= - 0.0108*m.b57 + m.x729 >= 0)

m.c395 = Constraint(expr= - 0.0108*m.b58 + m.x730 >= 0)

m.c396 = Constraint(expr= - 0.0108*m.b59 + m.x731 >= 0)

m.c397 = Constraint(expr= - 0.0108*m.b60 + m.x732 >= 0)

m.c398 = Constraint(expr= - 0.0108*m.b61 + m.x733 >= 0)

m.c399 = Constraint(expr= - 0.0108*m.b62 + m.x734 >= 0)

m.c400 = Constraint(expr= - 0.0108*m.b63 + m.x735 >= 0)

m.c401 = Constraint(expr= - 0.0108*m.b64 + m.x736 >= 0)

m.c402 = Constraint(expr= - 0.0108*m.b65 + m.x737 >= 0)

m.c403 = Constraint(expr= - 0.0108*m.b66 + m.x738 >= 0)

m.c404 = Constraint(expr= - 0.0108*m.b67 + m.x739 >= 0)

m.c405 = Constraint(expr= - 0.0108*m.b68 + m.x740 >= 0)

m.c406 = Constraint(expr= - 0.0108*m.b69 + m.x741 >= 0)

m.c407 = Constraint(expr= - 0.0108*m.b70 + m.x742 >= 0)

m.c408 = Constraint(expr= - 0.0108*m.b71 + m.x743 >= 0)

m.c409 = Constraint(expr= - 0.0108*m.b72 + m.x744 >= 0)

m.c410 = Constraint(expr= - 0.376812*m.b73 + m.x745 >= 0)

m.c411 = Constraint(expr= - 0.376812*m.b74 + m.x746 >= 0)

m.c412 = Constraint(expr= - 0.376812*m.b75 + m.x747 >= 0)

m.c413 = Constraint(expr= - 0.376812*m.b76 + m.x748 >= 0)

m.c414 = Constraint(expr= - 0.376812*m.b77 + m.x749 >= 0)

m.c415 = Constraint(expr= - 0.376812*m.b78 + m.x750 >= 0)

m.c416 = Constraint(expr= - 0.376812*m.b79 + m.x751 >= 0)

m.c417 = Constraint(expr= - 0.376812*m.b80 + m.x752 >= 0)

m.c418 = Constraint(expr= - 0.376812*m.b81 + m.x753 >= 0)

m.c419 = Constraint(expr= - 0.376812*m.b82 + m.x754 >= 0)

m.c420 = Constraint(expr= - 0.376812*m.b83 + m.x755 >= 0)

m.c421 = Constraint(expr= - 0.376812*m.b84 + m.x756 >= 0)

m.c422 = Constraint(expr= - 0.376812*m.b85 + m.x757 >= 0)

m.c423 = Constraint(expr= - 0.376812*m.b86 + m.x758 >= 0)

m.c424 = Constraint(expr= - 0.376812*m.b87 + m.x759 >= 0)

m.c425 = Constraint(expr= - 0.376812*m.b88 + m.x760 >= 0)

m.c426 = Constraint(expr= - 0.376812*m.b89 + m.x761 >= 0)

m.c427 = Constraint(expr= - 0.376812*m.b90 + m.x762 >= 0)

m.c428 = Constraint(expr= - 0.376812*m.b91 + m.x763 >= 0)

m.c429 = Constraint(expr= - 0.376812*m.b92 + m.x764 >= 0)

m.c430 = Constraint(expr= - 0.376812*m.b93 + m.x765 >= 0)

m.c431 = Constraint(expr= - 0.376812*m.b94 + m.x766 >= 0)

m.c432 = Constraint(expr= - 0.376812*m.b95 + m.x767 >= 0)

m.c433 = Constraint(expr= - 0.376812*m.b96 + m.x768 >= 0)

m.c434 = Constraint(expr= - 0.335628*m.b97 + m.x769 >= 0)

m.c435 = Constraint(expr= - 0.335628*m.b98 + m.x770 >= 0)

m.c436 = Constraint(expr= - 0.335628*m.b99 + m.x771 >= 0)

m.c437 = Constraint(expr= - 0.335628*m.b100 + m.x772 >= 0)

m.c438 = Constraint(expr= - 0.335628*m.b101 + m.x773 >= 0)

m.c439 = Constraint(expr= - 0.335628*m.b102 + m.x774 >= 0)

m.c440 = Constraint(expr= - 0.335628*m.b103 + m.x775 >= 0)

m.c441 = Constraint(expr= - 0.335628*m.b104 + m.x776 >= 0)

m.c442 = Constraint(expr= - 0.335628*m.b105 + m.x777 >= 0)

m.c443 = Constraint(expr= - 0.335628*m.b106 + m.x778 >= 0)

m.c444 = Constraint(expr= - 0.335628*m.b107 + m.x779 >= 0)

m.c445 = Constraint(expr= - 0.335628*m.b108 + m.x780 >= 0)

m.c446 = Constraint(expr= - 0.335628*m.b109 + m.x781 >= 0)

m.c447 = Constraint(expr= - 0.335628*m.b110 + m.x782 >= 0)

m.c448 = Constraint(expr= - 0.335628*m.b111 + m.x783 >= 0)

m.c449 = Constraint(expr= - 0.335628*m.b112 + m.x784 >= 0)

m.c450 = Constraint(expr= - 0.335628*m.b113 + m.x785 >= 0)

m.c451 = Constraint(expr= - 0.335628*m.b114 + m.x786 >= 0)

m.c452 = Constraint(expr= - 0.335628*m.b115 + m.x787 >= 0)

m.c453 = Constraint(expr= - 0.335628*m.b116 + m.x788 >= 0)

m.c454 = Constraint(expr= - 0.335628*m.b117 + m.x789 >= 0)

m.c455 = Constraint(expr= - 0.335628*m.b118 + m.x790 >= 0)

m.c456 = Constraint(expr= - 0.335628*m.b119 + m.x791 >= 0)

m.c457 = Constraint(expr= - 0.335628*m.b120 + m.x792 >= 0)

m.c458 = Constraint(expr= - 0.341964*m.b121 + m.x793 >= 0)

m.c459 = Constraint(expr= - 0.341964*m.b122 + m.x794 >= 0)

m.c460 = Constraint(expr= - 0.341964*m.b123 + m.x795 >= 0)

m.c461 = Constraint(expr= - 0.341964*m.b124 + m.x796 >= 0)

m.c462 = Constraint(expr= - 0.341964*m.b125 + m.x797 >= 0)

m.c463 = Constraint(expr= - 0.341964*m.b126 + m.x798 >= 0)

m.c464 = Constraint(expr= - 0.341964*m.b127 + m.x799 >= 0)

m.c465 = Constraint(expr= - 0.341964*m.b128 + m.x800 >= 0)

m.c466 = Constraint(expr= - 0.341964*m.b129 + m.x801 >= 0)

m.c467 = Constraint(expr= - 0.341964*m.b130 + m.x802 >= 0)

m.c468 = Constraint(expr= - 0.341964*m.b131 + m.x803 >= 0)

m.c469 = Constraint(expr= - 0.341964*m.b132 + m.x804 >= 0)

m.c470 = Constraint(expr= - 0.341964*m.b133 + m.x805 >= 0)

m.c471 = Constraint(expr= - 0.341964*m.b134 + m.x806 >= 0)

m.c472 = Constraint(expr= - 0.341964*m.b135 + m.x807 >= 0)

m.c473 = Constraint(expr= - 0.341964*m.b136 + m.x808 >= 0)

m.c474 = Constraint(expr= - 0.341964*m.b137 + m.x809 >= 0)

m.c475 = Constraint(expr= - 0.341964*m.b138 + m.x810 >= 0)

m.c476 = Constraint(expr= - 0.341964*m.b139 + m.x811 >= 0)

m.c477 = Constraint(expr= - 0.341964*m.b140 + m.x812 >= 0)

m.c478 = Constraint(expr= - 0.341964*m.b141 + m.x813 >= 0)

m.c479 = Constraint(expr= - 0.341964*m.b142 + m.x814 >= 0)

m.c480 = Constraint(expr= - 0.341964*m.b143 + m.x815 >= 0)

m.c481 = Constraint(expr= - 0.341964*m.b144 + m.x816 >= 0)

m.c482 = Constraint(expr= - 0.658188*m.b145 + m.x817 >= 0)

m.c483 = Constraint(expr= - 0.658188*m.b146 + m.x818 >= 0)

m.c484 = Constraint(expr= - 0.658188*m.b147 + m.x819 >= 0)

m.c485 = Constraint(expr= - 0.658188*m.b148 + m.x820 >= 0)

m.c486 = Constraint(expr= - 0.658188*m.b149 + m.x821 >= 0)

m.c487 = Constraint(expr= - 0.658188*m.b150 + m.x822 >= 0)

m.c488 = Constraint(expr= - 0.658188*m.b151 + m.x823 >= 0)

m.c489 = Constraint(expr= - 0.658188*m.b152 + m.x824 >= 0)

m.c490 = Constraint(expr= - 0.658188*m.b153 + m.x825 >= 0)

m.c491 = Constraint(expr= - 0.658188*m.b154 + m.x826 >= 0)

m.c492 = Constraint(expr= - 0.658188*m.b155 + m.x827 >= 0)

m.c493 = Constraint(expr= - 0.658188*m.b156 + m.x828 >= 0)

m.c494 = Constraint(expr= - 0.658188*m.b157 + m.x829 >= 0)

m.c495 = Constraint(expr= - 0.658188*m.b158 + m.x830 >= 0)

m.c496 = Constraint(expr= - 0.658188*m.b159 + m.x831 >= 0)

m.c497 = Constraint(expr= - 0.658188*m.b160 + m.x832 >= 0)

m.c498 = Constraint(expr= - 0.658188*m.b161 + m.x833 >= 0)

m.c499 = Constraint(expr= - 0.658188*m.b162 + m.x834 >= 0)

m.c500 = Constraint(expr= - 0.658188*m.b163 + m.x835 >= 0)

m.c501 = Constraint(expr= - 0.658188*m.b164 + m.x836 >= 0)

m.c502 = Constraint(expr= - 0.658188*m.b165 + m.x837 >= 0)

m.c503 = Constraint(expr= - 0.658188*m.b166 + m.x838 >= 0)

m.c504 = Constraint(expr= - 0.658188*m.b167 + m.x839 >= 0)

m.c505 = Constraint(expr= - 0.658188*m.b168 + m.x840 >= 0)

m.c506 = Constraint(expr= - 28*m.b1 + m.x337 >= 0)

m.c507 = Constraint(expr= - 28*m.b2 + m.x338 >= 0)

m.c508 = Constraint(expr= - 28*m.b3 + m.x339 >= 0)

m.c509 = Constraint(expr= - 28*m.b4 + m.x340 >= 0)

m.c510 = Constraint(expr= - 28*m.b5 + m.x341 >= 0)

m.c511 = Constraint(expr= - 28*m.b6 + m.x342 >= 0)

m.c512 = Constraint(expr= - 28*m.b7 + m.x343 >= 0)

m.c513 = Constraint(expr= - 28*m.b8 + m.x344 >= 0)

m.c514 = Constraint(expr= - 28*m.b9 + m.x345 >= 0)

m.c515 = Constraint(expr= - 28*m.b10 + m.x346 >= 0)

m.c516 = Constraint(expr= - 28*m.b11 + m.x347 >= 0)

m.c517 = Constraint(expr= - 28*m.b12 + m.x348 >= 0)

m.c518 = Constraint(expr= - 28*m.b13 + m.x349 >= 0)

m.c519 = Constraint(expr= - 28*m.b14 + m.x350 >= 0)

m.c520 = Constraint(expr= - 28*m.b15 + m.x351 >= 0)

m.c521 = Constraint(expr= - 28*m.b16 + m.x352 >= 0)

m.c522 = Constraint(expr= - 28*m.b17 + m.x353 >= 0)

m.c523 = Constraint(expr= - 28*m.b18 + m.x354 >= 0)

m.c524 = Constraint(expr= - 28*m.b19 + m.x355 >= 0)

m.c525 = Constraint(expr= - 28*m.b20 + m.x356 >= 0)

m.c526 = Constraint(expr= - 28*m.b21 + m.x357 >= 0)

m.c527 = Constraint(expr= - 28*m.b22 + m.x358 >= 0)

m.c528 = Constraint(expr= - 28*m.b23 + m.x359 >= 0)

m.c529 = Constraint(expr= - 28*m.b24 + m.x360 >= 0)

m.c530 = Constraint(expr= - 29.99*m.b25 + m.x361 >= 0)

m.c531 = Constraint(expr= - 29.99*m.b26 + m.x362 >= 0)

m.c532 = Constraint(expr= - 29.99*m.b27 + m.x363 >= 0)

m.c533 = Constraint(expr= - 29.99*m.b28 + m.x364 >= 0)

m.c534 = Constraint(expr= - 29.99*m.b29 + m.x365 >= 0)

m.c535 = Constraint(expr= - 29.99*m.b30 + m.x366 >= 0)

m.c536 = Constraint(expr= - 29.99*m.b31 + m.x367 >= 0)

m.c537 = Constraint(expr= - 29.99*m.b32 + m.x368 >= 0)

m.c538 = Constraint(expr= - 29.99*m.b33 + m.x369 >= 0)

m.c539 = Constraint(expr= - 29.99*m.b34 + m.x370 >= 0)

m.c540 = Constraint(expr= - 29.99*m.b35 + m.x371 >= 0)

m.c541 = Constraint(expr= - 29.99*m.b36 + m.x372 >= 0)

m.c542 = Constraint(expr= - 29.99*m.b37 + m.x373 >= 0)

m.c543 = Constraint(expr= - 29.99*m.b38 + m.x374 >= 0)

m.c544 = Constraint(expr= - 29.99*m.b39 + m.x375 >= 0)

m.c545 = Constraint(expr= - 29.99*m.b40 + m.x376 >= 0)

m.c546 = Constraint(expr= - 29.99*m.b41 + m.x377 >= 0)

m.c547 = Constraint(expr= - 29.99*m.b42 + m.x378 >= 0)

m.c548 = Constraint(expr= - 29.99*m.b43 + m.x379 >= 0)

m.c549 = Constraint(expr= - 29.99*m.b44 + m.x380 >= 0)

m.c550 = Constraint(expr= - 29.99*m.b45 + m.x381 >= 0)

m.c551 = Constraint(expr= - 29.99*m.b46 + m.x382 >= 0)

m.c552 = Constraint(expr= - 29.99*m.b47 + m.x383 >= 0)

m.c553 = Constraint(expr= - 29.99*m.b48 + m.x384 >= 0)

m.c554 = Constraint(expr= - 10.67*m.b49 + m.x385 >= 0)

m.c555 = Constraint(expr= - 10.67*m.b50 + m.x386 >= 0)

m.c556 = Constraint(expr= - 10.67*m.b51 + m.x387 >= 0)

m.c557 = Constraint(expr= - 10.67*m.b52 + m.x388 >= 0)

m.c558 = Constraint(expr= - 10.67*m.b53 + m.x389 >= 0)

m.c559 = Constraint(expr= - 10.67*m.b54 + m.x390 >= 0)

m.c560 = Constraint(expr= - 10.67*m.b55 + m.x391 >= 0)

m.c561 = Constraint(expr= - 10.67*m.b56 + m.x392 >= 0)

m.c562 = Constraint(expr= - 10.67*m.b57 + m.x393 >= 0)

m.c563 = Constraint(expr= - 10.67*m.b58 + m.x394 >= 0)

m.c564 = Constraint(expr= - 10.67*m.b59 + m.x395 >= 0)

m.c565 = Constraint(expr= - 10.67*m.b60 + m.x396 >= 0)

m.c566 = Constraint(expr= - 10.67*m.b61 + m.x397 >= 0)

m.c567 = Constraint(expr= - 10.67*m.b62 + m.x398 >= 0)

m.c568 = Constraint(expr= - 10.67*m.b63 + m.x399 >= 0)

m.c569 = Constraint(expr= - 10.67*m.b64 + m.x400 >= 0)

m.c570 = Constraint(expr= - 10.67*m.b65 + m.x401 >= 0)

m.c571 = Constraint(expr= - 10.67*m.b66 + m.x402 >= 0)

m.c572 = Constraint(expr= - 10.67*m.b67 + m.x403 >= 0)

m.c573 = Constraint(expr= - 10.67*m.b68 + m.x404 >= 0)

m.c574 = Constraint(expr= - 10.67*m.b69 + m.x405 >= 0)

m.c575 = Constraint(expr= - 10.67*m.b70 + m.x406 >= 0)

m.c576 = Constraint(expr= - 10.67*m.b71 + m.x407 >= 0)

m.c577 = Constraint(expr= - 10.67*m.b72 + m.x408 >= 0)

m.c578 = Constraint(expr= - 24.99*m.b73 + m.x409 >= 0)

m.c579 = Constraint(expr= - 24.99*m.b74 + m.x410 >= 0)

m.c580 = Constraint(expr= - 24.99*m.b75 + m.x411 >= 0)

m.c581 = Constraint(expr= - 24.99*m.b76 + m.x412 >= 0)

m.c582 = Constraint(expr= - 24.99*m.b77 + m.x413 >= 0)

m.c583 = Constraint(expr= - 24.99*m.b78 + m.x414 >= 0)

m.c584 = Constraint(expr= - 24.99*m.b79 + m.x415 >= 0)

m.c585 = Constraint(expr= - 24.99*m.b80 + m.x416 >= 0)

m.c586 = Constraint(expr= - 24.99*m.b81 + m.x417 >= 0)

m.c587 = Constraint(expr= - 24.99*m.b82 + m.x418 >= 0)

m.c588 = Constraint(expr= - 24.99*m.b83 + m.x419 >= 0)

m.c589 = Constraint(expr= - 24.99*m.b84 + m.x420 >= 0)

m.c590 = Constraint(expr= - 24.99*m.b85 + m.x421 >= 0)

m.c591 = Constraint(expr= - 24.99*m.b86 + m.x422 >= 0)

m.c592 = Constraint(expr= - 24.99*m.b87 + m.x423 >= 0)

m.c593 = Constraint(expr= - 24.99*m.b88 + m.x424 >= 0)

m.c594 = Constraint(expr= - 24.99*m.b89 + m.x425 >= 0)

m.c595 = Constraint(expr= - 24.99*m.b90 + m.x426 >= 0)

m.c596 = Constraint(expr= - 24.99*m.b91 + m.x427 >= 0)

m.c597 = Constraint(expr= - 24.99*m.b92 + m.x428 >= 0)

m.c598 = Constraint(expr= - 24.99*m.b93 + m.x429 >= 0)

m.c599 = Constraint(expr= - 24.99*m.b94 + m.x430 >= 0)

m.c600 = Constraint(expr= - 24.99*m.b95 + m.x431 >= 0)

m.c601 = Constraint(expr= - 24.99*m.b96 + m.x432 >= 0)

m.c602 = Constraint(expr= - 29.99*m.b97 + m.x433 >= 0)

m.c603 = Constraint(expr= - 29.99*m.b98 + m.x434 >= 0)

m.c604 = Constraint(expr= - 29.99*m.b99 + m.x435 >= 0)

m.c605 = Constraint(expr= - 29.99*m.b100 + m.x436 >= 0)

m.c606 = Constraint(expr= - 29.99*m.b101 + m.x437 >= 0)

m.c607 = Constraint(expr= - 29.99*m.b102 + m.x438 >= 0)

m.c608 = Constraint(expr= - 29.99*m.b103 + m.x439 >= 0)

m.c609 = Constraint(expr= - 29.99*m.b104 + m.x440 >= 0)

m.c610 = Constraint(expr= - 29.99*m.b105 + m.x441 >= 0)

m.c611 = Constraint(expr= - 29.99*m.b106 + m.x442 >= 0)

m.c612 = Constraint(expr= - 29.99*m.b107 + m.x443 >= 0)

m.c613 = Constraint(expr= - 29.99*m.b108 + m.x444 >= 0)

m.c614 = Constraint(expr= - 29.99*m.b109 + m.x445 >= 0)

m.c615 = Constraint(expr= - 29.99*m.b110 + m.x446 >= 0)

m.c616 = Constraint(expr= - 29.99*m.b111 + m.x447 >= 0)

m.c617 = Constraint(expr= - 29.99*m.b112 + m.x448 >= 0)

m.c618 = Constraint(expr= - 29.99*m.b113 + m.x449 >= 0)

m.c619 = Constraint(expr= - 29.99*m.b114 + m.x450 >= 0)

m.c620 = Constraint(expr= - 29.99*m.b115 + m.x451 >= 0)

m.c621 = Constraint(expr= - 29.99*m.b116 + m.x452 >= 0)

m.c622 = Constraint(expr= - 29.99*m.b117 + m.x453 >= 0)

m.c623 = Constraint(expr= - 29.99*m.b118 + m.x454 >= 0)

m.c624 = Constraint(expr= - 29.99*m.b119 + m.x455 >= 0)

m.c625 = Constraint(expr= - 29.99*m.b120 + m.x456 >= 0)

m.c626 = Constraint(expr= - 39.99*m.b121 + m.x457 >= 0)

m.c627 = Constraint(expr= - 39.99*m.b122 + m.x458 >= 0)

m.c628 = Constraint(expr= - 39.99*m.b123 + m.x459 >= 0)

m.c629 = Constraint(expr= - 39.99*m.b124 + m.x460 >= 0)

m.c630 = Constraint(expr= - 39.99*m.b125 + m.x461 >= 0)

m.c631 = Constraint(expr= - 39.99*m.b126 + m.x462 >= 0)

m.c632 = Constraint(expr= - 39.99*m.b127 + m.x463 >= 0)

m.c633 = Constraint(expr= - 39.99*m.b128 + m.x464 >= 0)

m.c634 = Constraint(expr= - 39.99*m.b129 + m.x465 >= 0)

m.c635 = Constraint(expr= - 39.99*m.b130 + m.x466 >= 0)

m.c636 = Constraint(expr= - 39.99*m.b131 + m.x467 >= 0)

m.c637 = Constraint(expr= - 39.99*m.b132 + m.x468 >= 0)

m.c638 = Constraint(expr= - 39.99*m.b133 + m.x469 >= 0)

m.c639 = Constraint(expr= - 39.99*m.b134 + m.x470 >= 0)

m.c640 = Constraint(expr= - 39.99*m.b135 + m.x471 >= 0)

m.c641 = Constraint(expr= - 39.99*m.b136 + m.x472 >= 0)

m.c642 = Constraint(expr= - 39.99*m.b137 + m.x473 >= 0)

m.c643 = Constraint(expr= - 39.99*m.b138 + m.x474 >= 0)

m.c644 = Constraint(expr= - 39.99*m.b139 + m.x475 >= 0)

m.c645 = Constraint(expr= - 39.99*m.b140 + m.x476 >= 0)

m.c646 = Constraint(expr= - 39.99*m.b141 + m.x477 >= 0)

m.c647 = Constraint(expr= - 39.99*m.b142 + m.x478 >= 0)

m.c648 = Constraint(expr= - 39.99*m.b143 + m.x479 >= 0)

m.c649 = Constraint(expr= - 39.99*m.b144 + m.x480 >= 0)

m.c650 = Constraint(expr= - 19.99*m.b145 + m.x481 >= 0)

m.c651 = Constraint(expr= - 19.99*m.b146 + m.x482 >= 0)

m.c652 = Constraint(expr= - 19.99*m.b147 + m.x483 >= 0)

m.c653 = Constraint(expr= - 19.99*m.b148 + m.x484 >= 0)

m.c654 = Constraint(expr= - 19.99*m.b149 + m.x485 >= 0)

m.c655 = Constraint(expr= - 19.99*m.b150 + m.x486 >= 0)

m.c656 = Constraint(expr= - 19.99*m.b151 + m.x487 >= 0)

m.c657 = Constraint(expr= - 19.99*m.b152 + m.x488 >= 0)

m.c658 = Constraint(expr= - 19.99*m.b153 + m.x489 >= 0)

m.c659 = Constraint(expr= - 19.99*m.b154 + m.x490 >= 0)

m.c660 = Constraint(expr= - 19.99*m.b155 + m.x491 >= 0)

m.c661 = Constraint(expr= - 19.99*m.b156 + m.x492 >= 0)

m.c662 = Constraint(expr= - 19.99*m.b157 + m.x493 >= 0)

m.c663 = Constraint(expr= - 19.99*m.b158 + m.x494 >= 0)

m.c664 = Constraint(expr= - 19.99*m.b159 + m.x495 >= 0)

m.c665 = Constraint(expr= - 19.99*m.b160 + m.x496 >= 0)

m.c666 = Constraint(expr= - 19.99*m.b161 + m.x497 >= 0)

m.c667 = Constraint(expr= - 19.99*m.b162 + m.x498 >= 0)

m.c668 = Constraint(expr= - 19.99*m.b163 + m.x499 >= 0)

m.c669 = Constraint(expr= - 19.99*m.b164 + m.x500 >= 0)

m.c670 = Constraint(expr= - 19.99*m.b165 + m.x501 >= 0)

m.c671 = Constraint(expr= - 19.99*m.b166 + m.x502 >= 0)

m.c672 = Constraint(expr= - 19.99*m.b167 + m.x503 >= 0)

m.c673 = Constraint(expr= - 19.99*m.b168 + m.x504 >= 0)

m.c674 = Constraint(expr= - 188.08*m.b1 + m.x337 <= 0)

m.c675 = Constraint(expr= - 188.08*m.b2 + m.x338 <= 0)

m.c676 = Constraint(expr= - 188.08*m.b3 + m.x339 <= 0)

m.c677 = Constraint(expr= - 188.08*m.b4 + m.x340 <= 0)

m.c678 = Constraint(expr= - 188.08*m.b5 + m.x341 <= 0)

m.c679 = Constraint(expr= - 188.08*m.b6 + m.x342 <= 0)

m.c680 = Constraint(expr= - 188.08*m.b7 + m.x343 <= 0)

m.c681 = Constraint(expr= - 188.08*m.b8 + m.x344 <= 0)

m.c682 = Constraint(expr= - 188.08*m.b9 + m.x345 <= 0)

m.c683 = Constraint(expr= - 188.08*m.b10 + m.x346 <= 0)

m.c684 = Constraint(expr= - 188.08*m.b11 + m.x347 <= 0)

m.c685 = Constraint(expr= - 188.08*m.b12 + m.x348 <= 0)

m.c686 = Constraint(expr= - 188.08*m.b13 + m.x349 <= 0)

m.c687 = Constraint(expr= - 188.08*m.b14 + m.x350 <= 0)

m.c688 = Constraint(expr= - 188.08*m.b15 + m.x351 <= 0)

m.c689 = Constraint(expr= - 188.08*m.b16 + m.x352 <= 0)

m.c690 = Constraint(expr= - 188.08*m.b17 + m.x353 <= 0)

m.c691 = Constraint(expr= - 188.08*m.b18 + m.x354 <= 0)

m.c692 = Constraint(expr= - 188.08*m.b19 + m.x355 <= 0)

m.c693 = Constraint(expr= - 188.08*m.b20 + m.x356 <= 0)

m.c694 = Constraint(expr= - 188.08*m.b21 + m.x357 <= 0)

m.c695 = Constraint(expr= - 188.08*m.b22 + m.x358 <= 0)

m.c696 = Constraint(expr= - 188.08*m.b23 + m.x359 <= 0)

m.c697 = Constraint(expr= - 188.08*m.b24 + m.x360 <= 0)

m.c698 = Constraint(expr= - 237.14*m.b25 + m.x361 <= 0)

m.c699 = Constraint(expr= - 237.14*m.b26 + m.x362 <= 0)

m.c700 = Constraint(expr= - 237.14*m.b27 + m.x363 <= 0)

m.c701 = Constraint(expr= - 237.14*m.b28 + m.x364 <= 0)

m.c702 = Constraint(expr= - 237.14*m.b29 + m.x365 <= 0)

m.c703 = Constraint(expr= - 237.14*m.b30 + m.x366 <= 0)

m.c704 = Constraint(expr= - 237.14*m.b31 + m.x367 <= 0)

m.c705 = Constraint(expr= - 237.14*m.b32 + m.x368 <= 0)

m.c706 = Constraint(expr= - 237.14*m.b33 + m.x369 <= 0)

m.c707 = Constraint(expr= - 237.14*m.b34 + m.x370 <= 0)

m.c708 = Constraint(expr= - 237.14*m.b35 + m.x371 <= 0)

m.c709 = Constraint(expr= - 237.14*m.b36 + m.x372 <= 0)

m.c710 = Constraint(expr= - 237.14*m.b37 + m.x373 <= 0)

m.c711 = Constraint(expr= - 237.14*m.b38 + m.x374 <= 0)

m.c712 = Constraint(expr= - 237.14*m.b39 + m.x375 <= 0)

m.c713 = Constraint(expr= - 237.14*m.b40 + m.x376 <= 0)

m.c714 = Constraint(expr= - 237.14*m.b41 + m.x377 <= 0)

m.c715 = Constraint(expr= - 237.14*m.b42 + m.x378 <= 0)

m.c716 = Constraint(expr= - 237.14*m.b43 + m.x379 <= 0)

m.c717 = Constraint(expr= - 237.14*m.b44 + m.x380 <= 0)

m.c718 = Constraint(expr= - 237.14*m.b45 + m.x381 <= 0)

m.c719 = Constraint(expr= - 237.14*m.b46 + m.x382 <= 0)

m.c720 = Constraint(expr= - 237.14*m.b47 + m.x383 <= 0)

m.c721 = Constraint(expr= - 237.14*m.b48 + m.x384 <= 0)

m.c722 = Constraint(expr= - 60*m.b49 + m.x385 <= 0)

m.c723 = Constraint(expr= - 60*m.b50 + m.x386 <= 0)

m.c724 = Constraint(expr= - 60*m.b51 + m.x387 <= 0)

m.c725 = Constraint(expr= - 60*m.b52 + m.x388 <= 0)

m.c726 = Constraint(expr= - 60*m.b53 + m.x389 <= 0)

m.c727 = Constraint(expr= - 60*m.b54 + m.x390 <= 0)

m.c728 = Constraint(expr= - 60*m.b55 + m.x391 <= 0)

m.c729 = Constraint(expr= - 60*m.b56 + m.x392 <= 0)

m.c730 = Constraint(expr= - 60*m.b57 + m.x393 <= 0)

m.c731 = Constraint(expr= - 60*m.b58 + m.x394 <= 0)

m.c732 = Constraint(expr= - 60*m.b59 + m.x395 <= 0)

m.c733 = Constraint(expr= - 60*m.b60 + m.x396 <= 0)

m.c734 = Constraint(expr= - 60*m.b61 + m.x397 <= 0)

m.c735 = Constraint(expr= - 60*m.b62 + m.x398 <= 0)

m.c736 = Constraint(expr= - 60*m.b63 + m.x399 <= 0)

m.c737 = Constraint(expr= - 60*m.b64 + m.x400 <= 0)

m.c738 = Constraint(expr= - 60*m.b65 + m.x401 <= 0)

m.c739 = Constraint(expr= - 60*m.b66 + m.x402 <= 0)

m.c740 = Constraint(expr= - 60*m.b67 + m.x403 <= 0)

m.c741 = Constraint(expr= - 60*m.b68 + m.x404 <= 0)

m.c742 = Constraint(expr= - 60*m.b69 + m.x405 <= 0)

m.c743 = Constraint(expr= - 60*m.b70 + m.x406 <= 0)

m.c744 = Constraint(expr= - 60*m.b71 + m.x407 <= 0)

m.c745 = Constraint(expr= - 60*m.b72 + m.x408 <= 0)

m.c746 = Constraint(expr= - 185.99*m.b73 + m.x409 <= 0)

m.c747 = Constraint(expr= - 185.99*m.b74 + m.x410 <= 0)

m.c748 = Constraint(expr= - 185.99*m.b75 + m.x411 <= 0)

m.c749 = Constraint(expr= - 185.99*m.b76 + m.x412 <= 0)

m.c750 = Constraint(expr= - 185.99*m.b77 + m.x413 <= 0)

m.c751 = Constraint(expr= - 185.99*m.b78 + m.x414 <= 0)

m.c752 = Constraint(expr= - 185.99*m.b79 + m.x415 <= 0)

m.c753 = Constraint(expr= - 185.99*m.b80 + m.x416 <= 0)

m.c754 = Constraint(expr= - 185.99*m.b81 + m.x417 <= 0)

m.c755 = Constraint(expr= - 185.99*m.b82 + m.x418 <= 0)

m.c756 = Constraint(expr= - 185.99*m.b83 + m.x419 <= 0)

m.c757 = Constraint(expr= - 185.99*m.b84 + m.x420 <= 0)

m.c758 = Constraint(expr= - 185.99*m.b85 + m.x421 <= 0)

m.c759 = Constraint(expr= - 185.99*m.b86 + m.x422 <= 0)

m.c760 = Constraint(expr= - 185.99*m.b87 + m.x423 <= 0)

m.c761 = Constraint(expr= - 185.99*m.b88 + m.x424 <= 0)

m.c762 = Constraint(expr= - 185.99*m.b89 + m.x425 <= 0)

m.c763 = Constraint(expr= - 185.99*m.b90 + m.x426 <= 0)

m.c764 = Constraint(expr= - 185.99*m.b91 + m.x427 <= 0)

m.c765 = Constraint(expr= - 185.99*m.b92 + m.x428 <= 0)

m.c766 = Constraint(expr= - 185.99*m.b93 + m.x429 <= 0)

m.c767 = Constraint(expr= - 185.99*m.b94 + m.x430 <= 0)

m.c768 = Constraint(expr= - 185.99*m.b95 + m.x431 <= 0)

m.c769 = Constraint(expr= - 185.99*m.b96 + m.x432 <= 0)

m.c770 = Constraint(expr= - 201.02*m.b97 + m.x433 <= 0)

m.c771 = Constraint(expr= - 201.02*m.b98 + m.x434 <= 0)

m.c772 = Constraint(expr= - 201.02*m.b99 + m.x435 <= 0)

m.c773 = Constraint(expr= - 201.02*m.b100 + m.x436 <= 0)

m.c774 = Constraint(expr= - 201.02*m.b101 + m.x437 <= 0)

m.c775 = Constraint(expr= - 201.02*m.b102 + m.x438 <= 0)

m.c776 = Constraint(expr= - 201.02*m.b103 + m.x439 <= 0)

m.c777 = Constraint(expr= - 201.02*m.b104 + m.x440 <= 0)

m.c778 = Constraint(expr= - 201.02*m.b105 + m.x441 <= 0)

m.c779 = Constraint(expr= - 201.02*m.b106 + m.x442 <= 0)

m.c780 = Constraint(expr= - 201.02*m.b107 + m.x443 <= 0)

m.c781 = Constraint(expr= - 201.02*m.b108 + m.x444 <= 0)

m.c782 = Constraint(expr= - 201.02*m.b109 + m.x445 <= 0)

m.c783 = Constraint(expr= - 201.02*m.b110 + m.x446 <= 0)

m.c784 = Constraint(expr= - 201.02*m.b111 + m.x447 <= 0)

m.c785 = Constraint(expr= - 201.02*m.b112 + m.x448 <= 0)

m.c786 = Constraint(expr= - 201.02*m.b113 + m.x449 <= 0)

m.c787 = Constraint(expr= - 201.02*m.b114 + m.x450 <= 0)

m.c788 = Constraint(expr= - 201.02*m.b115 + m.x451 <= 0)

m.c789 = Constraint(expr= - 201.02*m.b116 + m.x452 <= 0)

m.c790 = Constraint(expr= - 201.02*m.b117 + m.x453 <= 0)

m.c791 = Constraint(expr= - 201.02*m.b118 + m.x454 <= 0)

m.c792 = Constraint(expr= - 201.02*m.b119 + m.x455 <= 0)

m.c793 = Constraint(expr= - 201.02*m.b120 + m.x456 <= 0)

m.c794 = Constraint(expr= - 134.02*m.b121 + m.x457 <= 0)

m.c795 = Constraint(expr= - 134.02*m.b122 + m.x458 <= 0)

m.c796 = Constraint(expr= - 134.02*m.b123 + m.x459 <= 0)

m.c797 = Constraint(expr= - 134.02*m.b124 + m.x460 <= 0)

m.c798 = Constraint(expr= - 134.02*m.b125 + m.x461 <= 0)

m.c799 = Constraint(expr= - 134.02*m.b126 + m.x462 <= 0)

m.c800 = Constraint(expr= - 134.02*m.b127 + m.x463 <= 0)

m.c801 = Constraint(expr= - 134.02*m.b128 + m.x464 <= 0)

m.c802 = Constraint(expr= - 134.02*m.b129 + m.x465 <= 0)

m.c803 = Constraint(expr= - 134.02*m.b130 + m.x466 <= 0)

m.c804 = Constraint(expr= - 134.02*m.b131 + m.x467 <= 0)

m.c805 = Constraint(expr= - 134.02*m.b132 + m.x468 <= 0)

m.c806 = Constraint(expr= - 134.02*m.b133 + m.x469 <= 0)

m.c807 = Constraint(expr= - 134.02*m.b134 + m.x470 <= 0)

m.c808 = Constraint(expr= - 134.02*m.b135 + m.x471 <= 0)

m.c809 = Constraint(expr= - 134.02*m.b136 + m.x472 <= 0)

m.c810 = Constraint(expr= - 134.02*m.b137 + m.x473 <= 0)

m.c811 = Constraint(expr= - 134.02*m.b138 + m.x474 <= 0)

m.c812 = Constraint(expr= - 134.02*m.b139 + m.x475 <= 0)

m.c813 = Constraint(expr= - 134.02*m.b140 + m.x476 <= 0)

m.c814 = Constraint(expr= - 134.02*m.b141 + m.x477 <= 0)

m.c815 = Constraint(expr= - 134.02*m.b142 + m.x478 <= 0)

m.c816 = Constraint(expr= - 134.02*m.b143 + m.x479 <= 0)

m.c817 = Constraint(expr= - 134.02*m.b144 + m.x480 <= 0)

m.c818 = Constraint(expr= - 117.01*m.b145 + m.x481 <= 0)

m.c819 = Constraint(expr= - 117.01*m.b146 + m.x482 <= 0)

m.c820 = Constraint(expr= - 117.01*m.b147 + m.x483 <= 0)

m.c821 = Constraint(expr= - 117.01*m.b148 + m.x484 <= 0)

m.c822 = Constraint(expr= - 117.01*m.b149 + m.x485 <= 0)

m.c823 = Constraint(expr= - 117.01*m.b150 + m.x486 <= 0)

m.c824 = Constraint(expr= - 117.01*m.b151 + m.x487 <= 0)

m.c825 = Constraint(expr= - 117.01*m.b152 + m.x488 <= 0)

m.c826 = Constraint(expr= - 117.01*m.b153 + m.x489 <= 0)

m.c827 = Constraint(expr= - 117.01*m.b154 + m.x490 <= 0)

m.c828 = Constraint(expr= - 117.01*m.b155 + m.x491 <= 0)

m.c829 = Constraint(expr= - 117.01*m.b156 + m.x492 <= 0)

m.c830 = Constraint(expr= - 117.01*m.b157 + m.x493 <= 0)

m.c831 = Constraint(expr= - 117.01*m.b158 + m.x494 <= 0)

m.c832 = Constraint(expr= - 117.01*m.b159 + m.x495 <= 0)

m.c833 = Constraint(expr= - 117.01*m.b160 + m.x496 <= 0)

m.c834 = Constraint(expr= - 117.01*m.b161 + m.x497 <= 0)

m.c835 = Constraint(expr= - 117.01*m.b162 + m.x498 <= 0)

m.c836 = Constraint(expr= - 117.01*m.b163 + m.x499 <= 0)

m.c837 = Constraint(expr= - 117.01*m.b164 + m.x500 <= 0)

m.c838 = Constraint(expr= - 117.01*m.b165 + m.x501 <= 0)

m.c839 = Constraint(expr= - 117.01*m.b166 + m.x502 <= 0)

m.c840 = Constraint(expr= - 117.01*m.b167 + m.x503 <= 0)

m.c841 = Constraint(expr= - 117.01*m.b168 + m.x504 <= 0)

m.c842 = Constraint(expr=   m.x673 - m.x674 <= 2.0601)

m.c843 = Constraint(expr=   m.x674 - m.x675 <= 2.0601)

m.c844 = Constraint(expr=   m.x675 - m.x676 <= 2.0601)

m.c845 = Constraint(expr=   m.x676 - m.x677 <= 2.0601)

m.c846 = Constraint(expr=   m.x677 - m.x678 <= 2.0601)

m.c847 = Constraint(expr=   m.x678 - m.x679 <= 2.0601)

m.c848 = Constraint(expr=   m.x679 - m.x680 <= 2.0601)

m.c849 = Constraint(expr=   m.x680 - m.x681 <= 2.0601)

m.c850 = Constraint(expr=   m.x681 - m.x682 <= 2.0601)

m.c851 = Constraint(expr=   m.x682 - m.x683 <= 2.0601)

m.c852 = Constraint(expr=   m.x683 - m.x684 <= 2.0601)

m.c853 = Constraint(expr=   m.x684 - m.x685 <= 2.0601)

m.c854 = Constraint(expr=   m.x685 - m.x686 <= 2.0601)

m.c855 = Constraint(expr=   m.x686 - m.x687 <= 2.0601)

m.c856 = Constraint(expr=   m.x687 - m.x688 <= 2.0601)

m.c857 = Constraint(expr=   m.x688 - m.x689 <= 2.0601)

m.c858 = Constraint(expr=   m.x689 - m.x690 <= 2.0601)

m.c859 = Constraint(expr=   m.x690 - m.x691 <= 2.0601)

m.c860 = Constraint(expr=   m.x691 - m.x692 <= 2.0601)

m.c861 = Constraint(expr=   m.x692 - m.x693 <= 2.0601)

m.c862 = Constraint(expr=   m.x693 - m.x694 <= 2.0601)

m.c863 = Constraint(expr=   m.x694 - m.x695 <= 2.0601)

m.c864 = Constraint(expr=   m.x695 - m.x696 <= 2.0601)

m.c865 = Constraint(expr=   m.x697 - m.x698 <= 1.944)

m.c866 = Constraint(expr=   m.x698 - m.x699 <= 1.944)

m.c867 = Constraint(expr=   m.x699 - m.x700 <= 1.944)

m.c868 = Constraint(expr=   m.x700 - m.x701 <= 1.944)

m.c869 = Constraint(expr=   m.x701 - m.x702 <= 1.944)

m.c870 = Constraint(expr=   m.x702 - m.x703 <= 1.944)

m.c871 = Constraint(expr=   m.x703 - m.x704 <= 1.944)

m.c872 = Constraint(expr=   m.x704 - m.x705 <= 1.944)

m.c873 = Constraint(expr=   m.x705 - m.x706 <= 1.944)

m.c874 = Constraint(expr=   m.x706 - m.x707 <= 1.944)

m.c875 = Constraint(expr=   m.x707 - m.x708 <= 1.944)

m.c876 = Constraint(expr=   m.x708 - m.x709 <= 1.944)

m.c877 = Constraint(expr=   m.x709 - m.x710 <= 1.944)

m.c878 = Constraint(expr=   m.x710 - m.x711 <= 1.944)

m.c879 = Constraint(expr=   m.x711 - m.x712 <= 1.944)

m.c880 = Constraint(expr=   m.x712 - m.x713 <= 1.944)

m.c881 = Constraint(expr=   m.x713 - m.x714 <= 1.944)

m.c882 = Constraint(expr=   m.x714 - m.x715 <= 1.944)

m.c883 = Constraint(expr=   m.x715 - m.x716 <= 1.944)

m.c884 = Constraint(expr=   m.x716 - m.x717 <= 1.944)

m.c885 = Constraint(expr=   m.x717 - m.x718 <= 1.944)

m.c886 = Constraint(expr=   m.x718 - m.x719 <= 1.944)

m.c887 = Constraint(expr=   m.x719 - m.x720 <= 1.944)

m.c888 = Constraint(expr=   m.x721 - m.x722 <= 0.02952)

m.c889 = Constraint(expr=   m.x722 - m.x723 <= 0.02952)

m.c890 = Constraint(expr=   m.x723 - m.x724 <= 0.02952)

m.c891 = Constraint(expr=   m.x724 - m.x725 <= 0.02952)

m.c892 = Constraint(expr=   m.x725 - m.x726 <= 0.02952)

m.c893 = Constraint(expr=   m.x726 - m.x727 <= 0.02952)

m.c894 = Constraint(expr=   m.x727 - m.x728 <= 0.02952)

m.c895 = Constraint(expr=   m.x728 - m.x729 <= 0.02952)

m.c896 = Constraint(expr=   m.x729 - m.x730 <= 0.02952)

m.c897 = Constraint(expr=   m.x730 - m.x731 <= 0.02952)

m.c898 = Constraint(expr=   m.x731 - m.x732 <= 0.02952)

m.c899 = Constraint(expr=   m.x732 - m.x733 <= 0.02952)

m.c900 = Constraint(expr=   m.x733 - m.x734 <= 0.02952)

m.c901 = Constraint(expr=   m.x734 - m.x735 <= 0.02952)

m.c902 = Constraint(expr=   m.x735 - m.x736 <= 0.02952)

m.c903 = Constraint(expr=   m.x736 - m.x737 <= 0.02952)

m.c904 = Constraint(expr=   m.x737 - m.x738 <= 0.02952)

m.c905 = Constraint(expr=   m.x738 - m.x739 <= 0.02952)

m.c906 = Constraint(expr=   m.x739 - m.x740 <= 0.02952)

m.c907 = Constraint(expr=   m.x740 - m.x741 <= 0.02952)

m.c908 = Constraint(expr=   m.x741 - m.x742 <= 0.02952)

m.c909 = Constraint(expr=   m.x742 - m.x743 <= 0.02952)

m.c910 = Constraint(expr=   m.x743 - m.x744 <= 0.02952)

m.c911 = Constraint(expr=   m.x745 - m.x746 <= 1.62)

m.c912 = Constraint(expr=   m.x746 - m.x747 <= 1.62)

m.c913 = Constraint(expr=   m.x747 - m.x748 <= 1.62)

m.c914 = Constraint(expr=   m.x748 - m.x749 <= 1.62)

m.c915 = Constraint(expr=   m.x749 - m.x750 <= 1.62)

m.c916 = Constraint(expr=   m.x750 - m.x751 <= 1.62)

m.c917 = Constraint(expr=   m.x751 - m.x752 <= 1.62)

m.c918 = Constraint(expr=   m.x752 - m.x753 <= 1.62)

m.c919 = Constraint(expr=   m.x753 - m.x754 <= 1.62)

m.c920 = Constraint(expr=   m.x754 - m.x755 <= 1.62)

m.c921 = Constraint(expr=   m.x755 - m.x756 <= 1.62)

m.c922 = Constraint(expr=   m.x756 - m.x757 <= 1.62)

m.c923 = Constraint(expr=   m.x757 - m.x758 <= 1.62)

m.c924 = Constraint(expr=   m.x758 - m.x759 <= 1.62)

m.c925 = Constraint(expr=   m.x759 - m.x760 <= 1.62)

m.c926 = Constraint(expr=   m.x760 - m.x761 <= 1.62)

m.c927 = Constraint(expr=   m.x761 - m.x762 <= 1.62)

m.c928 = Constraint(expr=   m.x762 - m.x763 <= 1.62)

m.c929 = Constraint(expr=   m.x763 - m.x764 <= 1.62)

m.c930 = Constraint(expr=   m.x764 - m.x765 <= 1.62)

m.c931 = Constraint(expr=   m.x765 - m.x766 <= 1.62)

m.c932 = Constraint(expr=   m.x766 - m.x767 <= 1.62)

m.c933 = Constraint(expr=   m.x767 - m.x768 <= 1.62)

m.c934 = Constraint(expr=   m.x769 - m.x770 <= 1.586358)

m.c935 = Constraint(expr=   m.x770 - m.x771 <= 1.586358)

m.c936 = Constraint(expr=   m.x771 - m.x772 <= 1.586358)

m.c937 = Constraint(expr=   m.x772 - m.x773 <= 1.586358)

m.c938 = Constraint(expr=   m.x773 - m.x774 <= 1.586358)

m.c939 = Constraint(expr=   m.x774 - m.x775 <= 1.586358)

m.c940 = Constraint(expr=   m.x775 - m.x776 <= 1.586358)

m.c941 = Constraint(expr=   m.x776 - m.x777 <= 1.586358)

m.c942 = Constraint(expr=   m.x777 - m.x778 <= 1.586358)

m.c943 = Constraint(expr=   m.x778 - m.x779 <= 1.586358)

m.c944 = Constraint(expr=   m.x779 - m.x780 <= 1.586358)

m.c945 = Constraint(expr=   m.x780 - m.x781 <= 1.586358)

m.c946 = Constraint(expr=   m.x781 - m.x782 <= 1.586358)

m.c947 = Constraint(expr=   m.x782 - m.x783 <= 1.586358)

m.c948 = Constraint(expr=   m.x783 - m.x784 <= 1.586358)

m.c949 = Constraint(expr=   m.x784 - m.x785 <= 1.586358)

m.c950 = Constraint(expr=   m.x785 - m.x786 <= 1.586358)

m.c951 = Constraint(expr=   m.x786 - m.x787 <= 1.586358)

m.c952 = Constraint(expr=   m.x787 - m.x788 <= 1.586358)

m.c953 = Constraint(expr=   m.x788 - m.x789 <= 1.586358)

m.c954 = Constraint(expr=   m.x789 - m.x790 <= 1.586358)

m.c955 = Constraint(expr=   m.x790 - m.x791 <= 1.586358)

m.c956 = Constraint(expr=   m.x791 - m.x792 <= 1.586358)

m.c957 = Constraint(expr=   m.x793 - m.x794 <= 0.587412)

m.c958 = Constraint(expr=   m.x794 - m.x795 <= 0.587412)

m.c959 = Constraint(expr=   m.x795 - m.x796 <= 0.587412)

m.c960 = Constraint(expr=   m.x796 - m.x797 <= 0.587412)

m.c961 = Constraint(expr=   m.x797 - m.x798 <= 0.587412)

m.c962 = Constraint(expr=   m.x798 - m.x799 <= 0.587412)

m.c963 = Constraint(expr=   m.x799 - m.x800 <= 0.587412)

m.c964 = Constraint(expr=   m.x800 - m.x801 <= 0.587412)

m.c965 = Constraint(expr=   m.x801 - m.x802 <= 0.587412)

m.c966 = Constraint(expr=   m.x802 - m.x803 <= 0.587412)

m.c967 = Constraint(expr=   m.x803 - m.x804 <= 0.587412)

m.c968 = Constraint(expr=   m.x804 - m.x805 <= 0.587412)

m.c969 = Constraint(expr=   m.x805 - m.x806 <= 0.587412)

m.c970 = Constraint(expr=   m.x806 - m.x807 <= 0.587412)

m.c971 = Constraint(expr=   m.x807 - m.x808 <= 0.587412)

m.c972 = Constraint(expr=   m.x808 - m.x809 <= 0.587412)

m.c973 = Constraint(expr=   m.x809 - m.x810 <= 0.587412)

m.c974 = Constraint(expr=   m.x810 - m.x811 <= 0.587412)

m.c975 = Constraint(expr=   m.x811 - m.x812 <= 0.587412)

m.c976 = Constraint(expr=   m.x812 - m.x813 <= 0.587412)

m.c977 = Constraint(expr=   m.x813 - m.x814 <= 0.587412)

m.c978 = Constraint(expr=   m.x814 - m.x815 <= 0.587412)

m.c979 = Constraint(expr=   m.x815 - m.x816 <= 0.587412)

m.c980 = Constraint(expr=   m.x817 - m.x818 <= 2.441718)

m.c981 = Constraint(expr=   m.x818 - m.x819 <= 2.441718)

m.c982 = Constraint(expr=   m.x819 - m.x820 <= 2.441718)

m.c983 = Constraint(expr=   m.x820 - m.x821 <= 2.441718)

m.c984 = Constraint(expr=   m.x821 - m.x822 <= 2.441718)

m.c985 = Constraint(expr=   m.x822 - m.x823 <= 2.441718)

m.c986 = Constraint(expr=   m.x823 - m.x824 <= 2.441718)

m.c987 = Constraint(expr=   m.x824 - m.x825 <= 2.441718)

m.c988 = Constraint(expr=   m.x825 - m.x826 <= 2.441718)

m.c989 = Constraint(expr=   m.x826 - m.x827 <= 2.441718)

m.c990 = Constraint(expr=   m.x827 - m.x828 <= 2.441718)

m.c991 = Constraint(expr=   m.x828 - m.x829 <= 2.441718)

m.c992 = Constraint(expr=   m.x829 - m.x830 <= 2.441718)

m.c993 = Constraint(expr=   m.x830 - m.x831 <= 2.441718)

m.c994 = Constraint(expr=   m.x831 - m.x832 <= 2.441718)

m.c995 = Constraint(expr=   m.x832 - m.x833 <= 2.441718)

m.c996 = Constraint(expr=   m.x833 - m.x834 <= 2.441718)

m.c997 = Constraint(expr=   m.x834 - m.x835 <= 2.441718)

m.c998 = Constraint(expr=   m.x835 - m.x836 <= 2.441718)

m.c999 = Constraint(expr=   m.x836 - m.x837 <= 2.441718)

m.c1000 = Constraint(expr=   m.x837 - m.x838 <= 2.441718)

m.c1001 = Constraint(expr=   m.x838 - m.x839 <= 2.441718)

m.c1002 = Constraint(expr=   m.x839 - m.x840 <= 2.441718)

m.c1003 = Constraint(expr= - m.x673 + m.x674 <= 2.0601)

m.c1004 = Constraint(expr= - m.x674 + m.x675 <= 2.0601)

m.c1005 = Constraint(expr= - m.x675 + m.x676 <= 2.0601)

m.c1006 = Constraint(expr= - m.x676 + m.x677 <= 2.0601)

m.c1007 = Constraint(expr= - m.x677 + m.x678 <= 2.0601)

m.c1008 = Constraint(expr= - m.x678 + m.x679 <= 2.0601)

m.c1009 = Constraint(expr= - m.x679 + m.x680 <= 2.0601)

m.c1010 = Constraint(expr= - m.x680 + m.x681 <= 2.0601)

m.c1011 = Constraint(expr= - m.x681 + m.x682 <= 2.0601)

m.c1012 = Constraint(expr= - m.x682 + m.x683 <= 2.0601)

m.c1013 = Constraint(expr= - m.x683 + m.x684 <= 2.0601)

m.c1014 = Constraint(expr= - m.x684 + m.x685 <= 2.0601)

m.c1015 = Constraint(expr= - m.x685 + m.x686 <= 2.0601)

m.c1016 = Constraint(expr= - m.x686 + m.x687 <= 2.0601)

m.c1017 = Constraint(expr= - m.x687 + m.x688 <= 2.0601)

m.c1018 = Constraint(expr= - m.x688 + m.x689 <= 2.0601)

m.c1019 = Constraint(expr= - m.x689 + m.x690 <= 2.0601)

m.c1020 = Constraint(expr= - m.x690 + m.x691 <= 2.0601)

m.c1021 = Constraint(expr= - m.x691 + m.x692 <= 2.0601)

m.c1022 = Constraint(expr= - m.x692 + m.x693 <= 2.0601)

m.c1023 = Constraint(expr= - m.x693 + m.x694 <= 2.0601)

m.c1024 = Constraint(expr= - m.x694 + m.x695 <= 2.0601)

m.c1025 = Constraint(expr= - m.x695 + m.x696 <= 2.0601)

m.c1026 = Constraint(expr= - m.x697 + m.x698 <= 1.944)

m.c1027 = Constraint(expr= - m.x698 + m.x699 <= 1.944)

m.c1028 = Constraint(expr= - m.x699 + m.x700 <= 1.944)

m.c1029 = Constraint(expr= - m.x700 + m.x701 <= 1.944)

m.c1030 = Constraint(expr= - m.x701 + m.x702 <= 1.944)

m.c1031 = Constraint(expr= - m.x702 + m.x703 <= 1.944)

m.c1032 = Constraint(expr= - m.x703 + m.x704 <= 1.944)

m.c1033 = Constraint(expr= - m.x704 + m.x705 <= 1.944)

m.c1034 = Constraint(expr= - m.x705 + m.x706 <= 1.944)

m.c1035 = Constraint(expr= - m.x706 + m.x707 <= 1.944)

m.c1036 = Constraint(expr= - m.x707 + m.x708 <= 1.944)

m.c1037 = Constraint(expr= - m.x708 + m.x709 <= 1.944)

m.c1038 = Constraint(expr= - m.x709 + m.x710 <= 1.944)

m.c1039 = Constraint(expr= - m.x710 + m.x711 <= 1.944)

m.c1040 = Constraint(expr= - m.x711 + m.x712 <= 1.944)

m.c1041 = Constraint(expr= - m.x712 + m.x713 <= 1.944)

m.c1042 = Constraint(expr= - m.x713 + m.x714 <= 1.944)

m.c1043 = Constraint(expr= - m.x714 + m.x715 <= 1.944)

m.c1044 = Constraint(expr= - m.x715 + m.x716 <= 1.944)

m.c1045 = Constraint(expr= - m.x716 + m.x717 <= 1.944)

m.c1046 = Constraint(expr= - m.x717 + m.x718 <= 1.944)

m.c1047 = Constraint(expr= - m.x718 + m.x719 <= 1.944)

m.c1048 = Constraint(expr= - m.x719 + m.x720 <= 1.944)

m.c1049 = Constraint(expr= - m.x721 + m.x722 <= 0.02952)

m.c1050 = Constraint(expr= - m.x722 + m.x723 <= 0.02952)

m.c1051 = Constraint(expr= - m.x723 + m.x724 <= 0.02952)

m.c1052 = Constraint(expr= - m.x724 + m.x725 <= 0.02952)

m.c1053 = Constraint(expr= - m.x725 + m.x726 <= 0.02952)

m.c1054 = Constraint(expr= - m.x726 + m.x727 <= 0.02952)

m.c1055 = Constraint(expr= - m.x727 + m.x728 <= 0.02952)

m.c1056 = Constraint(expr= - m.x728 + m.x729 <= 0.02952)

m.c1057 = Constraint(expr= - m.x729 + m.x730 <= 0.02952)

m.c1058 = Constraint(expr= - m.x730 + m.x731 <= 0.02952)

m.c1059 = Constraint(expr= - m.x731 + m.x732 <= 0.02952)

m.c1060 = Constraint(expr= - m.x732 + m.x733 <= 0.02952)

m.c1061 = Constraint(expr= - m.x733 + m.x734 <= 0.02952)

m.c1062 = Constraint(expr= - m.x734 + m.x735 <= 0.02952)

m.c1063 = Constraint(expr= - m.x735 + m.x736 <= 0.02952)

m.c1064 = Constraint(expr= - m.x736 + m.x737 <= 0.02952)

m.c1065 = Constraint(expr= - m.x737 + m.x738 <= 0.02952)

m.c1066 = Constraint(expr= - m.x738 + m.x739 <= 0.02952)

m.c1067 = Constraint(expr= - m.x739 + m.x740 <= 0.02952)

m.c1068 = Constraint(expr= - m.x740 + m.x741 <= 0.02952)

m.c1069 = Constraint(expr= - m.x741 + m.x742 <= 0.02952)

m.c1070 = Constraint(expr= - m.x742 + m.x743 <= 0.02952)

m.c1071 = Constraint(expr= - m.x743 + m.x744 <= 0.02952)

m.c1072 = Constraint(expr= - m.x745 + m.x746 <= 1.62)

m.c1073 = Constraint(expr= - m.x746 + m.x747 <= 1.62)

m.c1074 = Constraint(expr= - m.x747 + m.x748 <= 1.62)

m.c1075 = Constraint(expr= - m.x748 + m.x749 <= 1.62)

m.c1076 = Constraint(expr= - m.x749 + m.x750 <= 1.62)

m.c1077 = Constraint(expr= - m.x750 + m.x751 <= 1.62)

m.c1078 = Constraint(expr= - m.x751 + m.x752 <= 1.62)

m.c1079 = Constraint(expr= - m.x752 + m.x753 <= 1.62)

m.c1080 = Constraint(expr= - m.x753 + m.x754 <= 1.62)

m.c1081 = Constraint(expr= - m.x754 + m.x755 <= 1.62)

m.c1082 = Constraint(expr= - m.x755 + m.x756 <= 1.62)

m.c1083 = Constraint(expr= - m.x756 + m.x757 <= 1.62)

m.c1084 = Constraint(expr= - m.x757 + m.x758 <= 1.62)

m.c1085 = Constraint(expr= - m.x758 + m.x759 <= 1.62)

m.c1086 = Constraint(expr= - m.x759 + m.x760 <= 1.62)

m.c1087 = Constraint(expr= - m.x760 + m.x761 <= 1.62)

m.c1088 = Constraint(expr= - m.x761 + m.x762 <= 1.62)

m.c1089 = Constraint(expr= - m.x762 + m.x763 <= 1.62)

m.c1090 = Constraint(expr= - m.x763 + m.x764 <= 1.62)

m.c1091 = Constraint(expr= - m.x764 + m.x765 <= 1.62)

m.c1092 = Constraint(expr= - m.x765 + m.x766 <= 1.62)

m.c1093 = Constraint(expr= - m.x766 + m.x767 <= 1.62)

m.c1094 = Constraint(expr= - m.x767 + m.x768 <= 1.62)

m.c1095 = Constraint(expr= - m.x769 + m.x770 <= 1.586358)

m.c1096 = Constraint(expr= - m.x770 + m.x771 <= 1.586358)

m.c1097 = Constraint(expr= - m.x771 + m.x772 <= 1.586358)

m.c1098 = Constraint(expr= - m.x772 + m.x773 <= 1.586358)

m.c1099 = Constraint(expr= - m.x773 + m.x774 <= 1.586358)

m.c1100 = Constraint(expr= - m.x774 + m.x775 <= 1.586358)

m.c1101 = Constraint(expr= - m.x775 + m.x776 <= 1.586358)

m.c1102 = Constraint(expr= - m.x776 + m.x777 <= 1.586358)

m.c1103 = Constraint(expr= - m.x777 + m.x778 <= 1.586358)

m.c1104 = Constraint(expr= - m.x778 + m.x779 <= 1.586358)

m.c1105 = Constraint(expr= - m.x779 + m.x780 <= 1.586358)

m.c1106 = Constraint(expr= - m.x780 + m.x781 <= 1.586358)

m.c1107 = Constraint(expr= - m.x781 + m.x782 <= 1.586358)

m.c1108 = Constraint(expr= - m.x782 + m.x783 <= 1.586358)

m.c1109 = Constraint(expr= - m.x783 + m.x784 <= 1.586358)

m.c1110 = Constraint(expr= - m.x784 + m.x785 <= 1.586358)

m.c1111 = Constraint(expr= - m.x785 + m.x786 <= 1.586358)

m.c1112 = Constraint(expr= - m.x786 + m.x787 <= 1.586358)

m.c1113 = Constraint(expr= - m.x787 + m.x788 <= 1.586358)

m.c1114 = Constraint(expr= - m.x788 + m.x789 <= 1.586358)

m.c1115 = Constraint(expr= - m.x789 + m.x790 <= 1.586358)

m.c1116 = Constraint(expr= - m.x790 + m.x791 <= 1.586358)

m.c1117 = Constraint(expr= - m.x791 + m.x792 <= 1.586358)

m.c1118 = Constraint(expr= - m.x793 + m.x794 <= 0.587412)

m.c1119 = Constraint(expr= - m.x794 + m.x795 <= 0.587412)

m.c1120 = Constraint(expr= - m.x795 + m.x796 <= 0.587412)

m.c1121 = Constraint(expr= - m.x796 + m.x797 <= 0.587412)

m.c1122 = Constraint(expr= - m.x797 + m.x798 <= 0.587412)

m.c1123 = Constraint(expr= - m.x798 + m.x799 <= 0.587412)

m.c1124 = Constraint(expr= - m.x799 + m.x800 <= 0.587412)

m.c1125 = Constraint(expr= - m.x800 + m.x801 <= 0.587412)

m.c1126 = Constraint(expr= - m.x801 + m.x802 <= 0.587412)

m.c1127 = Constraint(expr= - m.x802 + m.x803 <= 0.587412)

m.c1128 = Constraint(expr= - m.x803 + m.x804 <= 0.587412)

m.c1129 = Constraint(expr= - m.x804 + m.x805 <= 0.587412)

m.c1130 = Constraint(expr= - m.x805 + m.x806 <= 0.587412)

m.c1131 = Constraint(expr= - m.x806 + m.x807 <= 0.587412)

m.c1132 = Constraint(expr= - m.x807 + m.x808 <= 0.587412)

m.c1133 = Constraint(expr= - m.x808 + m.x809 <= 0.587412)

m.c1134 = Constraint(expr= - m.x809 + m.x810 <= 0.587412)

m.c1135 = Constraint(expr= - m.x810 + m.x811 <= 0.587412)

m.c1136 = Constraint(expr= - m.x811 + m.x812 <= 0.587412)

m.c1137 = Constraint(expr= - m.x812 + m.x813 <= 0.587412)

m.c1138 = Constraint(expr= - m.x813 + m.x814 <= 0.587412)

m.c1139 = Constraint(expr= - m.x814 + m.x815 <= 0.587412)

m.c1140 = Constraint(expr= - m.x815 + m.x816 <= 0.587412)

m.c1141 = Constraint(expr= - m.x817 + m.x818 <= 2.441718)

m.c1142 = Constraint(expr= - m.x818 + m.x819 <= 2.441718)

m.c1143 = Constraint(expr= - m.x819 + m.x820 <= 2.441718)

m.c1144 = Constraint(expr= - m.x820 + m.x821 <= 2.441718)

m.c1145 = Constraint(expr= - m.x821 + m.x822 <= 2.441718)

m.c1146 = Constraint(expr= - m.x822 + m.x823 <= 2.441718)

m.c1147 = Constraint(expr= - m.x823 + m.x824 <= 2.441718)

m.c1148 = Constraint(expr= - m.x824 + m.x825 <= 2.441718)

m.c1149 = Constraint(expr= - m.x825 + m.x826 <= 2.441718)

m.c1150 = Constraint(expr= - m.x826 + m.x827 <= 2.441718)

m.c1151 = Constraint(expr= - m.x827 + m.x828 <= 2.441718)

m.c1152 = Constraint(expr= - m.x828 + m.x829 <= 2.441718)

m.c1153 = Constraint(expr= - m.x829 + m.x830 <= 2.441718)

m.c1154 = Constraint(expr= - m.x830 + m.x831 <= 2.441718)

m.c1155 = Constraint(expr= - m.x831 + m.x832 <= 2.441718)

m.c1156 = Constraint(expr= - m.x832 + m.x833 <= 2.441718)

m.c1157 = Constraint(expr= - m.x833 + m.x834 <= 2.441718)

m.c1158 = Constraint(expr= - m.x834 + m.x835 <= 2.441718)

m.c1159 = Constraint(expr= - m.x835 + m.x836 <= 2.441718)

m.c1160 = Constraint(expr= - m.x836 + m.x837 <= 2.441718)

m.c1161 = Constraint(expr= - m.x837 + m.x838 <= 2.441718)

m.c1162 = Constraint(expr= - m.x838 + m.x839 <= 2.441718)

m.c1163 = Constraint(expr= - m.x839 + m.x840 <= 2.441718)

m.c1164 = Constraint(expr= - m.b1 + m.b169 >= 0)

m.c1165 = Constraint(expr=   m.b1 - m.b2 + m.b170 >= 0)

m.c1166 = Constraint(expr=   m.b2 - m.b3 + m.b171 >= 0)

m.c1167 = Constraint(expr=   m.b3 - m.b4 + m.b172 >= 0)

m.c1168 = Constraint(expr=   m.b4 - m.b5 + m.b173 >= 0)

m.c1169 = Constraint(expr=   m.b5 - m.b6 + m.b174 >= 0)

m.c1170 = Constraint(expr=   m.b6 - m.b7 + m.b175 >= 0)

m.c1171 = Constraint(expr=   m.b7 - m.b8 + m.b176 >= 0)

m.c1172 = Constraint(expr=   m.b8 - m.b9 + m.b177 >= 0)

m.c1173 = Constraint(expr=   m.b9 - m.b10 + m.b178 >= 0)

m.c1174 = Constraint(expr=   m.b10 - m.b11 + m.b179 >= 0)

m.c1175 = Constraint(expr=   m.b11 - m.b12 + m.b180 >= 0)

m.c1176 = Constraint(expr=   m.b12 - m.b13 + m.b181 >= 0)

m.c1177 = Constraint(expr=   m.b13 - m.b14 + m.b182 >= 0)

m.c1178 = Constraint(expr=   m.b14 - m.b15 + m.b183 >= 0)

m.c1179 = Constraint(expr=   m.b15 - m.b16 + m.b184 >= 0)

m.c1180 = Constraint(expr=   m.b16 - m.b17 + m.b185 >= 0)

m.c1181 = Constraint(expr=   m.b17 - m.b18 + m.b186 >= 0)

m.c1182 = Constraint(expr=   m.b18 - m.b19 + m.b187 >= 0)

m.c1183 = Constraint(expr=   m.b19 - m.b20 + m.b188 >= 0)

m.c1184 = Constraint(expr=   m.b20 - m.b21 + m.b189 >= 0)

m.c1185 = Constraint(expr=   m.b21 - m.b22 + m.b190 >= 0)

m.c1186 = Constraint(expr=   m.b22 - m.b23 + m.b191 >= 0)

m.c1187 = Constraint(expr=   m.b23 - m.b24 + m.b192 >= 0)

m.c1188 = Constraint(expr= - m.b25 + m.b193 >= 0)

m.c1189 = Constraint(expr=   m.b25 - m.b26 + m.b194 >= 0)

m.c1190 = Constraint(expr=   m.b26 - m.b27 + m.b195 >= 0)

m.c1191 = Constraint(expr=   m.b27 - m.b28 + m.b196 >= 0)

m.c1192 = Constraint(expr=   m.b28 - m.b29 + m.b197 >= 0)

m.c1193 = Constraint(expr=   m.b29 - m.b30 + m.b198 >= 0)

m.c1194 = Constraint(expr=   m.b30 - m.b31 + m.b199 >= 0)

m.c1195 = Constraint(expr=   m.b31 - m.b32 + m.b200 >= 0)

m.c1196 = Constraint(expr=   m.b32 - m.b33 + m.b201 >= 0)

m.c1197 = Constraint(expr=   m.b33 - m.b34 + m.b202 >= 0)

m.c1198 = Constraint(expr=   m.b34 - m.b35 + m.b203 >= 0)

m.c1199 = Constraint(expr=   m.b35 - m.b36 + m.b204 >= 0)

m.c1200 = Constraint(expr=   m.b36 - m.b37 + m.b205 >= 0)

m.c1201 = Constraint(expr=   m.b37 - m.b38 + m.b206 >= 0)

m.c1202 = Constraint(expr=   m.b38 - m.b39 + m.b207 >= 0)

m.c1203 = Constraint(expr=   m.b39 - m.b40 + m.b208 >= 0)

m.c1204 = Constraint(expr=   m.b40 - m.b41 + m.b209 >= 0)

m.c1205 = Constraint(expr=   m.b41 - m.b42 + m.b210 >= 0)

m.c1206 = Constraint(expr=   m.b42 - m.b43 + m.b211 >= 0)

m.c1207 = Constraint(expr=   m.b43 - m.b44 + m.b212 >= 0)

m.c1208 = Constraint(expr=   m.b44 - m.b45 + m.b213 >= 0)

m.c1209 = Constraint(expr=   m.b45 - m.b46 + m.b214 >= 0)

m.c1210 = Constraint(expr=   m.b46 - m.b47 + m.b215 >= 0)

m.c1211 = Constraint(expr=   m.b47 - m.b48 + m.b216 >= 0)

m.c1212 = Constraint(expr= - m.b49 + m.b217 >= 0)

m.c1213 = Constraint(expr=   m.b49 - m.b50 + m.b218 >= 0)

m.c1214 = Constraint(expr=   m.b50 - m.b51 + m.b219 >= 0)

m.c1215 = Constraint(expr=   m.b51 - m.b52 + m.b220 >= 0)

m.c1216 = Constraint(expr=   m.b52 - m.b53 + m.b221 >= 0)

m.c1217 = Constraint(expr=   m.b53 - m.b54 + m.b222 >= 0)

m.c1218 = Constraint(expr=   m.b54 - m.b55 + m.b223 >= 0)

m.c1219 = Constraint(expr=   m.b55 - m.b56 + m.b224 >= 0)

m.c1220 = Constraint(expr=   m.b56 - m.b57 + m.b225 >= 0)

m.c1221 = Constraint(expr=   m.b57 - m.b58 + m.b226 >= 0)

m.c1222 = Constraint(expr=   m.b58 - m.b59 + m.b227 >= 0)

m.c1223 = Constraint(expr=   m.b59 - m.b60 + m.b228 >= 0)

m.c1224 = Constraint(expr=   m.b60 - m.b61 + m.b229 >= 0)

m.c1225 = Constraint(expr=   m.b61 - m.b62 + m.b230 >= 0)

m.c1226 = Constraint(expr=   m.b62 - m.b63 + m.b231 >= 0)

m.c1227 = Constraint(expr=   m.b63 - m.b64 + m.b232 >= 0)

m.c1228 = Constraint(expr=   m.b64 - m.b65 + m.b233 >= 0)

m.c1229 = Constraint(expr=   m.b65 - m.b66 + m.b234 >= 0)

m.c1230 = Constraint(expr=   m.b66 - m.b67 + m.b235 >= 0)

m.c1231 = Constraint(expr=   m.b67 - m.b68 + m.b236 >= 0)

m.c1232 = Constraint(expr=   m.b68 - m.b69 + m.b237 >= 0)

m.c1233 = Constraint(expr=   m.b69 - m.b70 + m.b238 >= 0)

m.c1234 = Constraint(expr=   m.b70 - m.b71 + m.b239 >= 0)

m.c1235 = Constraint(expr=   m.b71 - m.b72 + m.b240 >= 0)

m.c1236 = Constraint(expr= - m.b73 + m.b241 >= 0)

m.c1237 = Constraint(expr=   m.b73 - m.b74 + m.b242 >= 0)

m.c1238 = Constraint(expr=   m.b74 - m.b75 + m.b243 >= 0)

m.c1239 = Constraint(expr=   m.b75 - m.b76 + m.b244 >= 0)

m.c1240 = Constraint(expr=   m.b76 - m.b77 + m.b245 >= 0)

m.c1241 = Constraint(expr=   m.b77 - m.b78 + m.b246 >= 0)

m.c1242 = Constraint(expr=   m.b78 - m.b79 + m.b247 >= 0)

m.c1243 = Constraint(expr=   m.b79 - m.b80 + m.b248 >= 0)

m.c1244 = Constraint(expr=   m.b80 - m.b81 + m.b249 >= 0)

m.c1245 = Constraint(expr=   m.b81 - m.b82 + m.b250 >= 0)

m.c1246 = Constraint(expr=   m.b82 - m.b83 + m.b251 >= 0)

m.c1247 = Constraint(expr=   m.b83 - m.b84 + m.b252 >= 0)

m.c1248 = Constraint(expr=   m.b84 - m.b85 + m.b253 >= 0)

m.c1249 = Constraint(expr=   m.b85 - m.b86 + m.b254 >= 0)

m.c1250 = Constraint(expr=   m.b86 - m.b87 + m.b255 >= 0)

m.c1251 = Constraint(expr=   m.b87 - m.b88 + m.b256 >= 0)

m.c1252 = Constraint(expr=   m.b88 - m.b89 + m.b257 >= 0)

m.c1253 = Constraint(expr=   m.b89 - m.b90 + m.b258 >= 0)

m.c1254 = Constraint(expr=   m.b90 - m.b91 + m.b259 >= 0)

m.c1255 = Constraint(expr=   m.b91 - m.b92 + m.b260 >= 0)

m.c1256 = Constraint(expr=   m.b92 - m.b93 + m.b261 >= 0)

m.c1257 = Constraint(expr=   m.b93 - m.b94 + m.b262 >= 0)

m.c1258 = Constraint(expr=   m.b94 - m.b95 + m.b263 >= 0)

m.c1259 = Constraint(expr=   m.b95 - m.b96 + m.b264 >= 0)

m.c1260 = Constraint(expr= - m.b97 + m.b265 >= 0)

m.c1261 = Constraint(expr=   m.b97 - m.b98 + m.b266 >= 0)

m.c1262 = Constraint(expr=   m.b98 - m.b99 + m.b267 >= 0)

m.c1263 = Constraint(expr=   m.b99 - m.b100 + m.b268 >= 0)

m.c1264 = Constraint(expr=   m.b100 - m.b101 + m.b269 >= 0)

m.c1265 = Constraint(expr=   m.b101 - m.b102 + m.b270 >= 0)

m.c1266 = Constraint(expr=   m.b102 - m.b103 + m.b271 >= 0)

m.c1267 = Constraint(expr=   m.b103 - m.b104 + m.b272 >= 0)

m.c1268 = Constraint(expr=   m.b104 - m.b105 + m.b273 >= 0)

m.c1269 = Constraint(expr=   m.b105 - m.b106 + m.b274 >= 0)

m.c1270 = Constraint(expr=   m.b106 - m.b107 + m.b275 >= 0)

m.c1271 = Constraint(expr=   m.b107 - m.b108 + m.b276 >= 0)

m.c1272 = Constraint(expr=   m.b108 - m.b109 + m.b277 >= 0)

m.c1273 = Constraint(expr=   m.b109 - m.b110 + m.b278 >= 0)

m.c1274 = Constraint(expr=   m.b110 - m.b111 + m.b279 >= 0)

m.c1275 = Constraint(expr=   m.b111 - m.b112 + m.b280 >= 0)

m.c1276 = Constraint(expr=   m.b112 - m.b113 + m.b281 >= 0)

m.c1277 = Constraint(expr=   m.b113 - m.b114 + m.b282 >= 0)

m.c1278 = Constraint(expr=   m.b114 - m.b115 + m.b283 >= 0)

m.c1279 = Constraint(expr=   m.b115 - m.b116 + m.b284 >= 0)

m.c1280 = Constraint(expr=   m.b116 - m.b117 + m.b285 >= 0)

m.c1281 = Constraint(expr=   m.b117 - m.b118 + m.b286 >= 0)

m.c1282 = Constraint(expr=   m.b118 - m.b119 + m.b287 >= 0)

m.c1283 = Constraint(expr=   m.b119 - m.b120 + m.b288 >= 0)

m.c1284 = Constraint(expr= - m.b121 + m.b289 >= 0)

m.c1285 = Constraint(expr=   m.b121 - m.b122 + m.b290 >= 0)

m.c1286 = Constraint(expr=   m.b122 - m.b123 + m.b291 >= 0)

m.c1287 = Constraint(expr=   m.b123 - m.b124 + m.b292 >= 0)

m.c1288 = Constraint(expr=   m.b124 - m.b125 + m.b293 >= 0)

m.c1289 = Constraint(expr=   m.b125 - m.b126 + m.b294 >= 0)

m.c1290 = Constraint(expr=   m.b126 - m.b127 + m.b295 >= 0)

m.c1291 = Constraint(expr=   m.b127 - m.b128 + m.b296 >= 0)

m.c1292 = Constraint(expr=   m.b128 - m.b129 + m.b297 >= 0)

m.c1293 = Constraint(expr=   m.b129 - m.b130 + m.b298 >= 0)

m.c1294 = Constraint(expr=   m.b130 - m.b131 + m.b299 >= 0)

m.c1295 = Constraint(expr=   m.b131 - m.b132 + m.b300 >= 0)

m.c1296 = Constraint(expr=   m.b132 - m.b133 + m.b301 >= 0)

m.c1297 = Constraint(expr=   m.b133 - m.b134 + m.b302 >= 0)

m.c1298 = Constraint(expr=   m.b134 - m.b135 + m.b303 >= 0)

m.c1299 = Constraint(expr=   m.b135 - m.b136 + m.b304 >= 0)

m.c1300 = Constraint(expr=   m.b136 - m.b137 + m.b305 >= 0)

m.c1301 = Constraint(expr=   m.b137 - m.b138 + m.b306 >= 0)

m.c1302 = Constraint(expr=   m.b138 - m.b139 + m.b307 >= 0)

m.c1303 = Constraint(expr=   m.b139 - m.b140 + m.b308 >= 0)

m.c1304 = Constraint(expr=   m.b140 - m.b141 + m.b309 >= 0)

m.c1305 = Constraint(expr=   m.b141 - m.b142 + m.b310 >= 0)

m.c1306 = Constraint(expr=   m.b142 - m.b143 + m.b311 >= 0)

m.c1307 = Constraint(expr=   m.b143 - m.b144 + m.b312 >= 0)

m.c1308 = Constraint(expr= - m.b145 + m.b313 >= 0)

m.c1309 = Constraint(expr=   m.b145 - m.b146 + m.b314 >= 0)

m.c1310 = Constraint(expr=   m.b146 - m.b147 + m.b315 >= 0)

m.c1311 = Constraint(expr=   m.b147 - m.b148 + m.b316 >= 0)

m.c1312 = Constraint(expr=   m.b148 - m.b149 + m.b317 >= 0)

m.c1313 = Constraint(expr=   m.b149 - m.b150 + m.b318 >= 0)

m.c1314 = Constraint(expr=   m.b150 - m.b151 + m.b319 >= 0)

m.c1315 = Constraint(expr=   m.b151 - m.b152 + m.b320 >= 0)

m.c1316 = Constraint(expr=   m.b152 - m.b153 + m.b321 >= 0)

m.c1317 = Constraint(expr=   m.b153 - m.b154 + m.b322 >= 0)

m.c1318 = Constraint(expr=   m.b154 - m.b155 + m.b323 >= 0)

m.c1319 = Constraint(expr=   m.b155 - m.b156 + m.b324 >= 0)

m.c1320 = Constraint(expr=   m.b156 - m.b157 + m.b325 >= 0)

m.c1321 = Constraint(expr=   m.b157 - m.b158 + m.b326 >= 0)

m.c1322 = Constraint(expr=   m.b158 - m.b159 + m.b327 >= 0)

m.c1323 = Constraint(expr=   m.b159 - m.b160 + m.b328 >= 0)

m.c1324 = Constraint(expr=   m.b160 - m.b161 + m.b329 >= 0)

m.c1325 = Constraint(expr=   m.b161 - m.b162 + m.b330 >= 0)

m.c1326 = Constraint(expr=   m.b162 - m.b163 + m.b331 >= 0)

m.c1327 = Constraint(expr=   m.b163 - m.b164 + m.b332 >= 0)

m.c1328 = Constraint(expr=   m.b164 - m.b165 + m.b333 >= 0)

m.c1329 = Constraint(expr=   m.b165 - m.b166 + m.b334 >= 0)

m.c1330 = Constraint(expr=   m.b166 - m.b167 + m.b335 >= 0)

m.c1331 = Constraint(expr=   m.b167 - m.b168 + m.b336 >= 0)

m.c1332 = Constraint(expr=-(0.5061084326298*m.x673*m.x841 + 50.09702*m.x673 - 0.5580651303227*m.x865*m.x673) + m.x337
                           == 0)

m.c1333 = Constraint(expr=-(0.5061084326298*m.x674*m.x842 + 50.09702*m.x674 - 0.5580651303227*m.x866*m.x674) + m.x338
                           == 0)

m.c1334 = Constraint(expr=-(0.5061084326298*m.x675*m.x843 + 50.09702*m.x675 - 0.5580651303227*m.x867*m.x675) + m.x339
                           == 0)

m.c1335 = Constraint(expr=-(0.5061084326298*m.x676*m.x844 + 50.09702*m.x676 - 0.5580651303227*m.x868*m.x676) + m.x340
                           == 0)

m.c1336 = Constraint(expr=-(0.5061084326298*m.x677*m.x845 + 50.09702*m.x677 - 0.5580651303227*m.x869*m.x677) + m.x341
                           == 0)

m.c1337 = Constraint(expr=-(0.5061084326298*m.x678*m.x846 + 50.09702*m.x678 - 0.5580651303227*m.x870*m.x678) + m.x342
                           == 0)

m.c1338 = Constraint(expr=-(0.5061084326298*m.x679*m.x847 + 50.09702*m.x679 - 0.5580651303227*m.x871*m.x679) + m.x343
                           == 0)

m.c1339 = Constraint(expr=-(0.5061084326298*m.x680*m.x848 + 50.09702*m.x680 - 0.5580651303227*m.x872*m.x680) + m.x344
                           == 0)

m.c1340 = Constraint(expr=-(0.5061084326298*m.x681*m.x849 + 50.09702*m.x681 - 0.5580651303227*m.x873*m.x681) + m.x345
                           == 0)

m.c1341 = Constraint(expr=-(0.5061084326298*m.x682*m.x850 + 50.09702*m.x682 - 0.5580651303227*m.x874*m.x682) + m.x346
                           == 0)

m.c1342 = Constraint(expr=-(0.5061084326298*m.x683*m.x851 + 50.09702*m.x683 - 0.5580651303227*m.x875*m.x683) + m.x347
                           == 0)

m.c1343 = Constraint(expr=-(0.5061084326298*m.x684*m.x852 + 50.09702*m.x684 - 0.5580651303227*m.x876*m.x684) + m.x348
                           == 0)

m.c1344 = Constraint(expr=-(0.5061084326298*m.x685*m.x853 + 50.09702*m.x685 - 0.5580651303227*m.x877*m.x685) + m.x349
                           == 0)

m.c1345 = Constraint(expr=-(0.5061084326298*m.x686*m.x854 + 50.09702*m.x686 - 0.5580651303227*m.x878*m.x686) + m.x350
                           == 0)

m.c1346 = Constraint(expr=-(0.5061084326298*m.x687*m.x855 + 50.09702*m.x687 - 0.5580651303227*m.x879*m.x687) + m.x351
                           == 0)

m.c1347 = Constraint(expr=-(0.5061084326298*m.x688*m.x856 + 50.09702*m.x688 - 0.5580651303227*m.x880*m.x688) + m.x352
                           == 0)

m.c1348 = Constraint(expr=-(0.5061084326298*m.x689*m.x857 + 50.09702*m.x689 - 0.5580651303227*m.x881*m.x689) + m.x353
                           == 0)

m.c1349 = Constraint(expr=-(0.5061084326298*m.x690*m.x858 + 50.09702*m.x690 - 0.5580651303227*m.x882*m.x690) + m.x354
                           == 0)

m.c1350 = Constraint(expr=-(0.5061084326298*m.x691*m.x859 + 50.09702*m.x691 - 0.5580651303227*m.x883*m.x691) + m.x355
                           == 0)

m.c1351 = Constraint(expr=-(0.5061084326298*m.x692*m.x860 + 50.09702*m.x692 - 0.5580651303227*m.x884*m.x692) + m.x356
                           == 0)

m.c1352 = Constraint(expr=-(0.5061084326298*m.x693*m.x861 + 50.09702*m.x693 - 0.5580651303227*m.x885*m.x693) + m.x357
                           == 0)

m.c1353 = Constraint(expr=-(0.5061084326298*m.x694*m.x862 + 50.09702*m.x694 - 0.5580651303227*m.x886*m.x694) + m.x358
                           == 0)

m.c1354 = Constraint(expr=-(0.5061084326298*m.x695*m.x863 + 50.09702*m.x695 - 0.5580651303227*m.x887*m.x695) + m.x359
                           == 0)

m.c1355 = Constraint(expr=-(0.5061084326298*m.x696*m.x864 + 50.09702*m.x696 - 0.5580651303227*m.x888*m.x696) + m.x360
                           == 0)

m.c1356 = Constraint(expr=-(0.5623466695665*m.x697*m.x865 + 78.54163*m.x697 - 0.5499405370095*m.x913*m.x697) + m.x361
                           == 0)

m.c1357 = Constraint(expr=-(0.5623466695665*m.x698*m.x866 + 78.54163*m.x698 - 0.5499405370095*m.x914*m.x698) + m.x362
                           == 0)

m.c1358 = Constraint(expr=-(0.5623466695665*m.x699*m.x867 + 78.54163*m.x699 - 0.5499405370095*m.x915*m.x699) + m.x363
                           == 0)

m.c1359 = Constraint(expr=-(0.5623466695665*m.x700*m.x868 + 78.54163*m.x700 - 0.5499405370095*m.x916*m.x700) + m.x364
                           == 0)

m.c1360 = Constraint(expr=-(0.5623466695665*m.x701*m.x869 + 78.54163*m.x701 - 0.5499405370095*m.x917*m.x701) + m.x365
                           == 0)

m.c1361 = Constraint(expr=-(0.5623466695665*m.x702*m.x870 + 78.54163*m.x702 - 0.5499405370095*m.x918*m.x702) + m.x366
                           == 0)

m.c1362 = Constraint(expr=-(0.5623466695665*m.x703*m.x871 + 78.54163*m.x703 - 0.5499405370095*m.x919*m.x703) + m.x367
                           == 0)

m.c1363 = Constraint(expr=-(0.5623466695665*m.x704*m.x872 + 78.54163*m.x704 - 0.5499405370095*m.x920*m.x704) + m.x368
                           == 0)

m.c1364 = Constraint(expr=-(0.5623466695665*m.x705*m.x873 + 78.54163*m.x705 - 0.5499405370095*m.x921*m.x705) + m.x369
                           == 0)

m.c1365 = Constraint(expr=-(0.5623466695665*m.x706*m.x874 + 78.54163*m.x706 - 0.5499405370095*m.x922*m.x706) + m.x370
                           == 0)

m.c1366 = Constraint(expr=-(0.5623466695665*m.x707*m.x875 + 78.54163*m.x707 - 0.5499405370095*m.x923*m.x707) + m.x371
                           == 0)

m.c1367 = Constraint(expr=-(0.5623466695665*m.x708*m.x876 + 78.54163*m.x708 - 0.5499405370095*m.x924*m.x708) + m.x372
                           == 0)

m.c1368 = Constraint(expr=-(0.5623466695665*m.x709*m.x877 + 78.54163*m.x709 - 0.5499405370095*m.x925*m.x709) + m.x373
                           == 0)

m.c1369 = Constraint(expr=-(0.5623466695665*m.x710*m.x878 + 78.54163*m.x710 - 0.5499405370095*m.x926*m.x710) + m.x374
                           == 0)

m.c1370 = Constraint(expr=-(0.5623466695665*m.x711*m.x879 + 78.54163*m.x711 - 0.5499405370095*m.x927*m.x711) + m.x375
                           == 0)

m.c1371 = Constraint(expr=-(0.5623466695665*m.x712*m.x880 + 78.54163*m.x712 - 0.5499405370095*m.x928*m.x712) + m.x376
                           == 0)

m.c1372 = Constraint(expr=-(0.5623466695665*m.x713*m.x881 + 78.54163*m.x713 - 0.5499405370095*m.x929*m.x713) + m.x377
                           == 0)

m.c1373 = Constraint(expr=-(0.5623466695665*m.x714*m.x882 + 78.54163*m.x714 - 0.5499405370095*m.x930*m.x714) + m.x378
                           == 0)

m.c1374 = Constraint(expr=-(0.5623466695665*m.x715*m.x883 + 78.54163*m.x715 - 0.5499405370095*m.x931*m.x715) + m.x379
                           == 0)

m.c1375 = Constraint(expr=-(0.5623466695665*m.x716*m.x884 + 78.54163*m.x716 - 0.5499405370095*m.x932*m.x716) + m.x380
                           == 0)

m.c1376 = Constraint(expr=-(0.5623466695665*m.x717*m.x885 + 78.54163*m.x717 - 0.5499405370095*m.x933*m.x717) + m.x381
                           == 0)

m.c1377 = Constraint(expr=-(0.5623466695665*m.x718*m.x886 + 78.54163*m.x718 - 0.5499405370095*m.x934*m.x718) + m.x382
                           == 0)

m.c1378 = Constraint(expr=-(0.5623466695665*m.x719*m.x887 + 78.54163*m.x719 - 0.5499405370095*m.x935*m.x719) + m.x383
                           == 0)

m.c1379 = Constraint(expr=-(0.5623466695665*m.x720*m.x888 + 78.54163*m.x720 - 0.5499405370095*m.x936*m.x720) + m.x384
                           == 0)

m.c1380 = Constraint(expr=-(1.0195418832074*m.x721*m.x889 + 989.1982*m.x721 - 0.4602295096966*m.x913*m.x721) + m.x385
                           == 0)

m.c1381 = Constraint(expr=-(1.0195418832074*m.x722*m.x890 + 989.1982*m.x722 - 0.4602295096966*m.x914*m.x722) + m.x386
                           == 0)

m.c1382 = Constraint(expr=-(1.0195418832074*m.x723*m.x891 + 989.1982*m.x723 - 0.4602295096966*m.x915*m.x723) + m.x387
                           == 0)

m.c1383 = Constraint(expr=-(1.0195418832074*m.x724*m.x892 + 989.1982*m.x724 - 0.4602295096966*m.x916*m.x724) + m.x388
                           == 0)

m.c1384 = Constraint(expr=-(1.0195418832074*m.x725*m.x893 + 989.1982*m.x725 - 0.4602295096966*m.x917*m.x725) + m.x389
                           == 0)

m.c1385 = Constraint(expr=-(1.0195418832074*m.x726*m.x894 + 989.1982*m.x726 - 0.4602295096966*m.x918*m.x726) + m.x390
                           == 0)

m.c1386 = Constraint(expr=-(1.0195418832074*m.x727*m.x895 + 989.1982*m.x727 - 0.4602295096966*m.x919*m.x727) + m.x391
                           == 0)

m.c1387 = Constraint(expr=-(1.0195418832074*m.x728*m.x896 + 989.1982*m.x728 - 0.4602295096966*m.x920*m.x728) + m.x392
                           == 0)

m.c1388 = Constraint(expr=-(1.0195418832074*m.x729*m.x897 + 989.1982*m.x729 - 0.4602295096966*m.x921*m.x729) + m.x393
                           == 0)

m.c1389 = Constraint(expr=-(1.0195418832074*m.x730*m.x898 + 989.1982*m.x730 - 0.4602295096966*m.x922*m.x730) + m.x394
                           == 0)

m.c1390 = Constraint(expr=-(1.0195418832074*m.x731*m.x899 + 989.1982*m.x731 - 0.4602295096966*m.x923*m.x731) + m.x395
                           == 0)

m.c1391 = Constraint(expr=-(1.0195418832074*m.x732*m.x900 + 989.1982*m.x732 - 0.4602295096966*m.x924*m.x732) + m.x396
                           == 0)

m.c1392 = Constraint(expr=-(1.0195418832074*m.x733*m.x901 + 989.1982*m.x733 - 0.4602295096966*m.x925*m.x733) + m.x397
                           == 0)

m.c1393 = Constraint(expr=-(1.0195418832074*m.x734*m.x902 + 989.1982*m.x734 - 0.4602295096966*m.x926*m.x734) + m.x398
                           == 0)

m.c1394 = Constraint(expr=-(1.0195418832074*m.x735*m.x903 + 989.1982*m.x735 - 0.4602295096966*m.x927*m.x735) + m.x399
                           == 0)

m.c1395 = Constraint(expr=-(1.0195418832074*m.x736*m.x904 + 989.1982*m.x736 - 0.4602295096966*m.x928*m.x736) + m.x400
                           == 0)

m.c1396 = Constraint(expr=-(1.0195418832074*m.x737*m.x905 + 989.1982*m.x737 - 0.4602295096966*m.x929*m.x737) + m.x401
                           == 0)

m.c1397 = Constraint(expr=-(1.0195418832074*m.x738*m.x906 + 989.1982*m.x738 - 0.4602295096966*m.x930*m.x738) + m.x402
                           == 0)

m.c1398 = Constraint(expr=-(1.0195418832074*m.x739*m.x907 + 989.1982*m.x739 - 0.4602295096966*m.x931*m.x739) + m.x403
                           == 0)

m.c1399 = Constraint(expr=-(1.0195418832074*m.x740*m.x908 + 989.1982*m.x740 - 0.4602295096966*m.x932*m.x740) + m.x404
                           == 0)

m.c1400 = Constraint(expr=-(1.0195418832074*m.x741*m.x909 + 989.1982*m.x741 - 0.4602295096966*m.x933*m.x741) + m.x405
                           == 0)

m.c1401 = Constraint(expr=-(1.0195418832074*m.x742*m.x910 + 989.1982*m.x742 - 0.4602295096966*m.x934*m.x742) + m.x406
                           == 0)

m.c1402 = Constraint(expr=-(1.0195418832074*m.x743*m.x911 + 989.1982*m.x743 - 0.4602295096966*m.x935*m.x743) + m.x407
                           == 0)

m.c1403 = Constraint(expr=-(1.0195418832074*m.x744*m.x912 + 989.1982*m.x744 - 0.4602295096966*m.x936*m.x744) + m.x408
                           == 0)

m.c1404 = Constraint(expr=-(0.5742413664547*m.x745*m.x913 + 67.34698*m.x745 - 0.6264451520993*m.x937*m.x745) + m.x409
                           == 0)

m.c1405 = Constraint(expr=-(0.5742413664547*m.x746*m.x914 + 67.34698*m.x746 - 0.6264451520993*m.x938*m.x746) + m.x410
                           == 0)

m.c1406 = Constraint(expr=-(0.5742413664547*m.x747*m.x915 + 67.34698*m.x747 - 0.6264451520993*m.x939*m.x747) + m.x411
                           == 0)

m.c1407 = Constraint(expr=-(0.5742413664547*m.x748*m.x916 + 67.34698*m.x748 - 0.6264451520993*m.x940*m.x748) + m.x412
                           == 0)

m.c1408 = Constraint(expr=-(0.5742413664547*m.x749*m.x917 + 67.34698*m.x749 - 0.6264451520993*m.x941*m.x749) + m.x413
                           == 0)

m.c1409 = Constraint(expr=-(0.5742413664547*m.x750*m.x918 + 67.34698*m.x750 - 0.6264451520993*m.x942*m.x750) + m.x414
                           == 0)

m.c1410 = Constraint(expr=-(0.5742413664547*m.x751*m.x919 + 67.34698*m.x751 - 0.6264451520993*m.x943*m.x751) + m.x415
                           == 0)

m.c1411 = Constraint(expr=-(0.5742413664547*m.x752*m.x920 + 67.34698*m.x752 - 0.6264451520993*m.x944*m.x752) + m.x416
                           == 0)

m.c1412 = Constraint(expr=-(0.5742413664547*m.x753*m.x921 + 67.34698*m.x753 - 0.6264451520993*m.x945*m.x753) + m.x417
                           == 0)

m.c1413 = Constraint(expr=-(0.5742413664547*m.x754*m.x922 + 67.34698*m.x754 - 0.6264451520993*m.x946*m.x754) + m.x418
                           == 0)

m.c1414 = Constraint(expr=-(0.5742413664547*m.x755*m.x923 + 67.34698*m.x755 - 0.6264451520993*m.x947*m.x755) + m.x419
                           == 0)

m.c1415 = Constraint(expr=-(0.5742413664547*m.x756*m.x924 + 67.34698*m.x756 - 0.6264451520993*m.x948*m.x756) + m.x420
                           == 0)

m.c1416 = Constraint(expr=-(0.5742413664547*m.x757*m.x925 + 67.34698*m.x757 - 0.6264451520993*m.x949*m.x757) + m.x421
                           == 0)

m.c1417 = Constraint(expr=-(0.5742413664547*m.x758*m.x926 + 67.34698*m.x758 - 0.6264451520993*m.x950*m.x758) + m.x422
                           == 0)

m.c1418 = Constraint(expr=-(0.5742413664547*m.x759*m.x927 + 67.34698*m.x759 - 0.6264451520993*m.x951*m.x759) + m.x423
                           == 0)

m.c1419 = Constraint(expr=-(0.5742413664547*m.x760*m.x928 + 67.34698*m.x760 - 0.6264451520993*m.x952*m.x760) + m.x424
                           == 0)

m.c1420 = Constraint(expr=-(0.5742413664547*m.x761*m.x929 + 67.34698*m.x761 - 0.6264451520993*m.x953*m.x761) + m.x425
                           == 0)

m.c1421 = Constraint(expr=-(0.5742413664547*m.x762*m.x930 + 67.34698*m.x762 - 0.6264451520993*m.x954*m.x762) + m.x426
                           == 0)

m.c1422 = Constraint(expr=-(0.5742413664547*m.x763*m.x931 + 67.34698*m.x763 - 0.6264451520993*m.x955*m.x763) + m.x427
                           == 0)

m.c1423 = Constraint(expr=-(0.5742413664547*m.x764*m.x932 + 67.34698*m.x764 - 0.6264451520993*m.x956*m.x764) + m.x428
                           == 0)

m.c1424 = Constraint(expr=-(0.5742413664547*m.x765*m.x933 + 67.34698*m.x765 - 0.6264451520993*m.x957*m.x765) + m.x429
                           == 0)

m.c1425 = Constraint(expr=-(0.5742413664547*m.x766*m.x934 + 67.34698*m.x766 - 0.6264451520993*m.x958*m.x766) + m.x430
                           == 0)

m.c1426 = Constraint(expr=-(0.5742413664547*m.x767*m.x935 + 67.34698*m.x767 - 0.6264451520993*m.x959*m.x767) + m.x431
                           == 0)

m.c1427 = Constraint(expr=-(0.5742413664547*m.x768*m.x936 + 67.34698*m.x768 - 0.6264451520993*m.x960*m.x768) + m.x432
                           == 0)

m.c1428 = Constraint(expr=-(0.6698483287091*m.x769*m.x937 + 82.51898*m.x769 - 0.3884080900057*m.x985*m.x769) + m.x433
                           == 0)

m.c1429 = Constraint(expr=-(0.6698483287091*m.x770*m.x938 + 82.51898*m.x770 - 0.3884080900057*m.x986*m.x770) + m.x434
                           == 0)

m.c1430 = Constraint(expr=-(0.6698483287091*m.x771*m.x939 + 82.51898*m.x771 - 0.3884080900057*m.x987*m.x771) + m.x435
                           == 0)

m.c1431 = Constraint(expr=-(0.6698483287091*m.x772*m.x940 + 82.51898*m.x772 - 0.3884080900057*m.x988*m.x772) + m.x436
                           == 0)

m.c1432 = Constraint(expr=-(0.6698483287091*m.x773*m.x941 + 82.51898*m.x773 - 0.3884080900057*m.x989*m.x773) + m.x437
                           == 0)

m.c1433 = Constraint(expr=-(0.6698483287091*m.x774*m.x942 + 82.51898*m.x774 - 0.3884080900057*m.x990*m.x774) + m.x438
                           == 0)

m.c1434 = Constraint(expr=-(0.6698483287091*m.x775*m.x943 + 82.51898*m.x775 - 0.3884080900057*m.x991*m.x775) + m.x439
                           == 0)

m.c1435 = Constraint(expr=-(0.6698483287091*m.x776*m.x944 + 82.51898*m.x776 - 0.3884080900057*m.x992*m.x776) + m.x440
                           == 0)

m.c1436 = Constraint(expr=-(0.6698483287091*m.x777*m.x945 + 82.51898*m.x777 - 0.3884080900057*m.x993*m.x777) + m.x441
                           == 0)

m.c1437 = Constraint(expr=-(0.6698483287091*m.x778*m.x946 + 82.51898*m.x778 - 0.3884080900057*m.x994*m.x778) + m.x442
                           == 0)

m.c1438 = Constraint(expr=-(0.6698483287091*m.x779*m.x947 + 82.51898*m.x779 - 0.3884080900057*m.x995*m.x779) + m.x443
                           == 0)

m.c1439 = Constraint(expr=-(0.6698483287091*m.x780*m.x948 + 82.51898*m.x780 - 0.3884080900057*m.x996*m.x780) + m.x444
                           == 0)

m.c1440 = Constraint(expr=-(0.6698483287091*m.x781*m.x949 + 82.51898*m.x781 - 0.3884080900057*m.x997*m.x781) + m.x445
                           == 0)

m.c1441 = Constraint(expr=-(0.6698483287091*m.x782*m.x950 + 82.51898*m.x782 - 0.3884080900057*m.x998*m.x782) + m.x446
                           == 0)

m.c1442 = Constraint(expr=-(0.6698483287091*m.x783*m.x951 + 82.51898*m.x783 - 0.3884080900057*m.x999*m.x783) + m.x447
                           == 0)

m.c1443 = Constraint(expr=-(0.6698483287091*m.x784*m.x952 + 82.51898*m.x784 - 0.3884080900057*m.x1000*m.x784) + m.x448
                           == 0)

m.c1444 = Constraint(expr=-(0.6698483287091*m.x785*m.x953 + 82.51898*m.x785 - 0.3884080900057*m.x1001*m.x785) + m.x449
                           == 0)

m.c1445 = Constraint(expr=-(0.6698483287091*m.x786*m.x954 + 82.51898*m.x786 - 0.3884080900057*m.x1002*m.x786) + m.x450
                           == 0)

m.c1446 = Constraint(expr=-(0.6698483287091*m.x787*m.x955 + 82.51898*m.x787 - 0.3884080900057*m.x1003*m.x787) + m.x451
                           == 0)

m.c1447 = Constraint(expr=-(0.6698483287091*m.x788*m.x956 + 82.51898*m.x788 - 0.3884080900057*m.x1004*m.x788) + m.x452
                           == 0)

m.c1448 = Constraint(expr=-(0.6698483287091*m.x789*m.x957 + 82.51898*m.x789 - 0.3884080900057*m.x1005*m.x789) + m.x453
                           == 0)

m.c1449 = Constraint(expr=-(0.6698483287091*m.x790*m.x958 + 82.51898*m.x790 - 0.3884080900057*m.x1006*m.x790) + m.x454
                           == 0)

m.c1450 = Constraint(expr=-(0.6698483287091*m.x791*m.x959 + 82.51898*m.x791 - 0.3884080900057*m.x1007*m.x791) + m.x455
                           == 0)

m.c1451 = Constraint(expr=-(0.6698483287091*m.x792*m.x960 + 82.51898*m.x792 - 0.3884080900057*m.x1008*m.x792) + m.x456
                           == 0)

m.c1452 = Constraint(expr=-(0.4372222561898*m.x793*m.x961 + 96.44253*m.x793 - 0.3096143033983*m.x985*m.x793) + m.x457
                           == 0)

m.c1453 = Constraint(expr=-(0.4372222561898*m.x794*m.x962 + 96.44253*m.x794 - 0.3096143033983*m.x986*m.x794) + m.x458
                           == 0)

m.c1454 = Constraint(expr=-(0.4372222561898*m.x795*m.x963 + 96.44253*m.x795 - 0.3096143033983*m.x987*m.x795) + m.x459
                           == 0)

m.c1455 = Constraint(expr=-(0.4372222561898*m.x796*m.x964 + 96.44253*m.x796 - 0.3096143033983*m.x988*m.x796) + m.x460
                           == 0)

m.c1456 = Constraint(expr=-(0.4372222561898*m.x797*m.x965 + 96.44253*m.x797 - 0.3096143033983*m.x989*m.x797) + m.x461
                           == 0)

m.c1457 = Constraint(expr=-(0.4372222561898*m.x798*m.x966 + 96.44253*m.x798 - 0.3096143033983*m.x990*m.x798) + m.x462
                           == 0)

m.c1458 = Constraint(expr=-(0.4372222561898*m.x799*m.x967 + 96.44253*m.x799 - 0.3096143033983*m.x991*m.x799) + m.x463
                           == 0)

m.c1459 = Constraint(expr=-(0.4372222561898*m.x800*m.x968 + 96.44253*m.x800 - 0.3096143033983*m.x992*m.x800) + m.x464
                           == 0)

m.c1460 = Constraint(expr=-(0.4372222561898*m.x801*m.x969 + 96.44253*m.x801 - 0.3096143033983*m.x993*m.x801) + m.x465
                           == 0)

m.c1461 = Constraint(expr=-(0.4372222561898*m.x802*m.x970 + 96.44253*m.x802 - 0.3096143033983*m.x994*m.x802) + m.x466
                           == 0)

m.c1462 = Constraint(expr=-(0.4372222561898*m.x803*m.x971 + 96.44253*m.x803 - 0.3096143033983*m.x995*m.x803) + m.x467
                           == 0)

m.c1463 = Constraint(expr=-(0.4372222561898*m.x804*m.x972 + 96.44253*m.x804 - 0.3096143033983*m.x996*m.x804) + m.x468
                           == 0)

m.c1464 = Constraint(expr=-(0.4372222561898*m.x805*m.x973 + 96.44253*m.x805 - 0.3096143033983*m.x997*m.x805) + m.x469
                           == 0)

m.c1465 = Constraint(expr=-(0.4372222561898*m.x806*m.x974 + 96.44253*m.x806 - 0.3096143033983*m.x998*m.x806) + m.x470
                           == 0)

m.c1466 = Constraint(expr=-(0.4372222561898*m.x807*m.x975 + 96.44253*m.x807 - 0.3096143033983*m.x999*m.x807) + m.x471
                           == 0)

m.c1467 = Constraint(expr=-(0.4372222561898*m.x808*m.x976 + 96.44253*m.x808 - 0.3096143033983*m.x1000*m.x808) + m.x472
                           == 0)

m.c1468 = Constraint(expr=-(0.4372222561898*m.x809*m.x977 + 96.44253*m.x809 - 0.3096143033983*m.x1001*m.x809) + m.x473
                           == 0)

m.c1469 = Constraint(expr=-(0.4372222561898*m.x810*m.x978 + 96.44253*m.x810 - 0.3096143033983*m.x1002*m.x810) + m.x474
                           == 0)

m.c1470 = Constraint(expr=-(0.4372222561898*m.x811*m.x979 + 96.44253*m.x811 - 0.3096143033983*m.x1003*m.x811) + m.x475
                           == 0)

m.c1471 = Constraint(expr=-(0.4372222561898*m.x812*m.x980 + 96.44253*m.x812 - 0.3096143033983*m.x1004*m.x812) + m.x476
                           == 0)

m.c1472 = Constraint(expr=-(0.4372222561898*m.x813*m.x981 + 96.44253*m.x813 - 0.3096143033983*m.x1005*m.x813) + m.x477
                           == 0)

m.c1473 = Constraint(expr=-(0.4372222561898*m.x814*m.x982 + 96.44253*m.x814 - 0.3096143033983*m.x1006*m.x814) + m.x478
                           == 0)

m.c1474 = Constraint(expr=-(0.4372222561898*m.x815*m.x983 + 96.44253*m.x815 - 0.3096143033983*m.x1007*m.x815) + m.x479
                           == 0)

m.c1475 = Constraint(expr=-(0.4372222561898*m.x816*m.x984 + 96.44253*m.x816 - 0.3096143033983*m.x1008*m.x816) + m.x480
                           == 0)

m.c1476 = Constraint(expr=-(0.3293431260086*m.x817*m.x985 + 22.86819*m.x817) + m.x481 == 0)

m.c1477 = Constraint(expr=-(0.3293431260086*m.x818*m.x986 + 22.86819*m.x818) + m.x482 == 0)

m.c1478 = Constraint(expr=-(0.3293431260086*m.x819*m.x987 + 22.86819*m.x819) + m.x483 == 0)

m.c1479 = Constraint(expr=-(0.3293431260086*m.x820*m.x988 + 22.86819*m.x820) + m.x484 == 0)

m.c1480 = Constraint(expr=-(0.3293431260086*m.x821*m.x989 + 22.86819*m.x821) + m.x485 == 0)

m.c1481 = Constraint(expr=-(0.3293431260086*m.x822*m.x990 + 22.86819*m.x822) + m.x486 == 0)

m.c1482 = Constraint(expr=-(0.3293431260086*m.x823*m.x991 + 22.86819*m.x823) + m.x487 == 0)

m.c1483 = Constraint(expr=-(0.3293431260086*m.x824*m.x992 + 22.86819*m.x824) + m.x488 == 0)

m.c1484 = Constraint(expr=-(0.3293431260086*m.x825*m.x993 + 22.86819*m.x825) + m.x489 == 0)

m.c1485 = Constraint(expr=-(0.3293431260086*m.x826*m.x994 + 22.86819*m.x826) + m.x490 == 0)

m.c1486 = Constraint(expr=-(0.3293431260086*m.x827*m.x995 + 22.86819*m.x827) + m.x491 == 0)

m.c1487 = Constraint(expr=-(0.3293431260086*m.x828*m.x996 + 22.86819*m.x828) + m.x492 == 0)

m.c1488 = Constraint(expr=-(0.3293431260086*m.x829*m.x997 + 22.86819*m.x829) + m.x493 == 0)

m.c1489 = Constraint(expr=-(0.3293431260086*m.x830*m.x998 + 22.86819*m.x830) + m.x494 == 0)

m.c1490 = Constraint(expr=-(0.3293431260086*m.x831*m.x999 + 22.86819*m.x831) + m.x495 == 0)

m.c1491 = Constraint(expr=-(0.3293431260086*m.x832*m.x1000 + 22.86819*m.x832) + m.x496 == 0)

m.c1492 = Constraint(expr=-(0.3293431260086*m.x833*m.x1001 + 22.86819*m.x833) + m.x497 == 0)

m.c1493 = Constraint(expr=-(0.3293431260086*m.x834*m.x1002 + 22.86819*m.x834) + m.x498 == 0)

m.c1494 = Constraint(expr=-(0.3293431260086*m.x835*m.x1003 + 22.86819*m.x835) + m.x499 == 0)

m.c1495 = Constraint(expr=-(0.3293431260086*m.x836*m.x1004 + 22.86819*m.x836) + m.x500 == 0)

m.c1496 = Constraint(expr=-(0.3293431260086*m.x837*m.x1005 + 22.86819*m.x837) + m.x501 == 0)

m.c1497 = Constraint(expr=-(0.3293431260086*m.x838*m.x1006 + 22.86819*m.x838) + m.x502 == 0)

m.c1498 = Constraint(expr=-(0.3293431260086*m.x839*m.x1007 + 22.86819*m.x839) + m.x503 == 0)

m.c1499 = Constraint(expr=-(0.3293431260086*m.x840*m.x1008 + 22.86819*m.x840) + m.x504 == 0)
