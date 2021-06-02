#  MINLP written by GAMS Convert at 04/21/18 13:54:17
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        326        1      325        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        326        1      325        0


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
m.x326 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x326, sense=maximize)

m.c1 = Constraint(expr=2*m.b1*m.b2 - 2*m.b1 - 2*m.b2 + 2*m.b1*m.b136 - 2*m.b136 + 2*m.b1*m.b232 - 2*m.b1*m.b236 + 2*m.b2
                       *m.b89 - 4*m.b89 - 2*m.b2*m.b133 + 2*m.b133 + 2*m.b2*m.b233 + 2*m.b3*m.b14 - 2*m.b3 - 2*m.b14 + 2
                       *m.b3*m.b59 - 2*m.b59 - 2*m.b3*m.b243 + 2*m.b3*m.b260 + 2*m.b4*m.b78 - 2*m.b4 - 2*m.b78 + 2*m.b4*
                       m.b201 - 2*m.b201 - 2*m.b4*m.b255 + 2*m.b4*m.b256 - 2*m.b5*m.b34 - 2*m.b5 + 2*m.b34 + 2*m.b5*
                       m.b35 - 2*m.b35 + 2*m.b5*m.b76 - 2*m.b76 + 2*m.b5*m.b248 + 2*m.b6*m.b201 - 2*m.b6 + 2*m.b6*m.b240
                        - 2*m.b6*m.b261 + 2*m.b6*m.b262 + 2*m.b7*m.b62 - 2*m.b7 - 2*m.b62 - 2*m.b7*m.b169 + 2*m.b169 + 2
                       *m.b7*m.b235 + 2*m.b7*m.b240 + 2*m.b8*m.b11 - 4*m.b8 - 4*m.b11 + 2*m.b8*m.b15 - 2*m.b15 + 2*m.b8*
                       m.b249 + 2*m.b8*m.b275 + 2*m.b9*m.b63 - 2*m.b9 - 2*m.b63 + 2*m.b9*m.b79 - 2*m.b79 - 2*m.b9*m.b199
                        + 2*m.b199 + 2*m.b9*m.b235 - 2*m.b10*m.b145 - 2*m.b10 + 2*m.b145 + 2*m.b10*m.b149 - 2*m.b149 + 2
                       *m.b10*m.b172 - 4*m.b172 + 2*m.b10*m.b252 + 2*m.b11*m.b63 + 2*m.b11*m.b97 - 2*m.b97 + 2*m.b11*
                       m.b241 + 2*m.b12*m.b122 - 2*m.b12 - 2*m.b122 - 2*m.b12*m.b171 + 4*m.b171 + 2*m.b12*m.b204 - 4*
                       m.b204 + 2*m.b12*m.b245 + 2*m.b13*m.b17 - 2*m.b13 - 2*m.b17 + 2*m.b13*m.b228 - 2*m.b228 + 2*m.b14
                       *m.b15 + 2*m.b14*m.b60 - 2*m.b60 - 2*m.b14*m.b283 + 2*m.b15*m.b35 - 2*m.b15*m.b169 + 2*m.b16*
                       m.b83 - 2*m.b16 - 4*m.b83 + 2*m.b16*m.b106 - 2*m.b106 - 2*m.b16*m.b180 + 4*m.b180 + 2*m.b16*
                       m.b273 + 2*m.b17*m.b18 - 2*m.b18 - 2*m.b17*m.b42 - 2*m.b42 + 2*m.b17*m.b56 - 4*m.b56 + 2*m.b18*
                       m.b22 - 2*m.b22 - 2*m.b19*m.b197 + 2*m.b19 - 2*m.b197 - 2*m.b19*m.b199 - 2*m.b19*m.b260 + 2*m.b19
                       *m.b261 + 2*m.b20*m.b107 - 2*m.b20 - 4*m.b107 + 2*m.b20*m.b127 - 4*m.b127 - 2*m.b20*m.b211 + 2*
                       m.b211 + 2*m.b20*m.b277 + 2*m.b21*m.b30 - 2*m.b21 - 2*m.b30 + 2*m.b21*m.b40 - 4*m.b40 - 2*m.b21*
                       m.b68 - 2*m.b68 + 2*m.b21*m.b107 + 2*m.b22*m.b23 - 2*m.b23 - 2*m.b22*m.b31 - 2*m.b31 + 2*m.b22*
                       m.b73 - 4*m.b73 + 2*m.b23*m.b26 - 2*m.b26 + 2*m.b24*m.b68 - 2*m.b24 + 2*m.b24*m.b128 - 4*m.b128
                        + 2*m.b24*m.b155 - 4*m.b155 - 2*m.b24*m.b281 + 2*m.b25*m.b40 - 2*m.b25 + 2*m.b25*m.b53 - 4*m.b53
                        + 2*m.b25*m.b128 - 2*m.b25*m.b277 + 2*m.b26*m.b27 - 2*m.b27 + 2*m.b26*m.b92 - 4*m.b92 - 2*m.b26*
                       m.b288 + 2*m.b27*m.b32 - 4*m.b32 + 2*m.b28*m.b83 - 2*m.b28 + 2*m.b28*m.b156 - 2*m.b156 + 2*m.b28*
                       m.b181 - 4*m.b181 - 2*m.b28*m.b284 + 2*m.b29*m.b53 - 2*m.b29 + 2*m.b29*m.b70 - 4*m.b70 + 2*m.b29*
                       m.b156 - 2*m.b29*m.b273 + 2*m.b30*m.b216 - 4*m.b216 - 2*m.b30*m.b220 + 2*m.b220 + 2*m.b30*m.b282
                        + 2*m.b31*m.b43 - 4*m.b43 + 2*m.b31*m.b55 - 4*m.b55 + 2*m.b31*m.b291 + 2*m.b32*m.b33 - 2*m.b33
                        + 2*m.b32*m.b113 - 4*m.b113 + 2*m.b32*m.b288 + 2*m.b33*m.b43 - 2*m.b34*m.b295 + 2*m.b35*m.b96 - 
                       2*m.b96 - 2*m.b35*m.b142 - 2*m.b142 + 2*m.b36*m.b37 - 2*m.b36 - 2*m.b37 + 2*m.b36*m.b47 - 2*m.b47
                        + 2*m.b36*m.b101 - 4*m.b101 - 2*m.b36*m.b257 + 2*m.b37*m.b48 - 2*m.b48 + 2*m.b37*m.b66 - 2*m.b66
                        - 2*m.b37*m.b123 - 2*m.b123 + 2*m.b38*m.b107 - 4*m.b38 + 2*m.b38*m.b182 - 2*m.b182 + 2*m.b38*
                       m.b212 - 4*m.b212 + 2*m.b38*m.b284 + 2*m.b39*m.b70 - 4*m.b39 + 2*m.b39*m.b85 - 4*m.b85 + 2*m.b39*
                       m.b182 + 2*m.b39*m.b273 + 2*m.b40*m.b86 - 4*m.b86 + 2*m.b40*m.b278 + 2*m.b41*m.b42 - 4*m.b41 + 2*
                       m.b41*m.b288 + 2*m.b41*m.b294 + 2*m.b41*m.b299 + 2*m.b42*m.b57 - 4*m.b57 + 2*m.b42*m.b72 - 4*
                       m.b72 + 2*m.b43*m.b44 - 2*m.b44 + 2*m.b43*m.b137 - 4*m.b137 + 2*m.b44*m.b57 + 2*m.b45*m.b95 - 2*
                       m.b45 - 2*m.b95 + 2*m.b45*m.b237 + 2*m.b46*m.b248 - 2*m.b46 + 2*m.b46*m.b261 + 2*m.b46*m.b262 - 2
                       *m.b46*m.b285 + 2*m.b47*m.b49 - 4*m.b49 + 2*m.b47*m.b122 - 2*m.b47*m.b152 + 4*m.b152 + 2*m.b48*
                       m.b50 - 4*m.b50 + 2*m.b48*m.b230 - 2*m.b48*m.b272 + 2*m.b49*m.b50 + 2*m.b49*m.b267 + 2*m.b49*
                       m.b292 + 2*m.b50*m.b154 + 2*m.b154 + 2*m.b50*m.b229 + 2*m.b51*m.b128 - 2*m.b51 + 2*m.b51*m.b214
                        - 2*m.b214 - 2*m.b51*m.b229 + 2*m.b51*m.b281 + 2*m.b52*m.b85 - 4*m.b52 + 2*m.b52*m.b109 - 4*
                       m.b109 + 2*m.b52*m.b214 + 2*m.b52*m.b277 + 2*m.b53*m.b220 + 2*m.b53*m.b274 + 2*m.b54*m.b55 - 2*
                       m.b54 + 2*m.b54*m.b223 - 2*m.b223 + 2*m.b54*m.b291 - 2*m.b54*m.b303 + 2*m.b55*m.b56 + 2*m.b55*
                       m.b90 - 2*m.b90 + 2*m.b56*m.b74 - 4*m.b74 + 2*m.b56*m.b91 - 4*m.b91 + 2*m.b57*m.b58 - 2*m.b58 + 2
                       *m.b57*m.b226 - 2*m.b226 + 2*m.b58*m.b74 + 2*m.b59*m.b116 - 2*m.b116 + 2*m.b60*m.b140 - 2*m.b140
                        - 2*m.b60*m.b166 + 2*m.b166 + 2*m.b60*m.b243 + 2*m.b61*m.b62 - 2*m.b61 + 2*m.b61*m.b254 + 2*
                       m.b61*m.b255 - 2*m.b61*m.b289 + 2*m.b62*m.b80 - 2*m.b80 - 2*m.b62*m.b305 - 2*m.b63*m.b145 + 2*
                       m.b63*m.b234 + 2*m.b64*m.b80 - 4*m.b64 + 2*m.b64*m.b100 - 2*m.b100 + 2*m.b64*m.b145 + 2*m.b64*
                       m.b249 + 2*m.b65*m.b67 - 2*m.b65 - 4*m.b67 + 2*m.b65*m.b102 - 2*m.b102 - 2*m.b65*m.b178 + 4*
                       m.b178 + 2*m.b65*m.b252 + 2*m.b66*m.b251 + 2*m.b66*m.b264 - 2*m.b66*m.b296 + 2*m.b67*m.b230 + 2*
                       m.b67*m.b290 + 2*m.b67*m.b296 + 2*m.b68*m.b69 - 2*m.b69 + 2*m.b68*m.b268 + 2*m.b69*m.b109 + 2*
                       m.b69*m.b131 - 4*m.b131 - 2*m.b69*m.b215 - 2*m.b215 + 2*m.b70*m.b270 + 2*m.b70*m.b282 + 2*m.b71*
                       m.b86 - 2*m.b71 + 2*m.b71*m.b231 + 2*m.b71*m.b247 - 2*m.b71*m.b299 + 2*m.b72*m.b73 + 2*m.b72*
                       m.b111 - 2*m.b111 + 2*m.b72*m.b299 + 2*m.b73*m.b93 - 4*m.b93 + 2*m.b73*m.b112 - 4*m.b112 + 2*
                       m.b74*m.b75 - 2*m.b75 + 2*m.b74*m.b193 - 2*m.b193 + 2*m.b75*m.b93 + 2*m.b76*m.b141 - 2*m.b141 + 2
                       *m.b77*m.b79 - 2*m.b77 - 2*m.b77*m.b166 + 2*m.b77*m.b250 + 2*m.b77*m.b260 + 2*m.b78*m.b96 - 2*
                       m.b78*m.b98 - 2*m.b98 + 2*m.b78*m.b283 + 2*m.b79*m.b98 - 2*m.b79*m.b168 + 2*m.b168 + 2*m.b80*
                       m.b81 - 2*m.b81 - 2*m.b80*m.b262 + 2*m.b81*m.b98 + 2*m.b81*m.b120 + 2*m.b120 - 2*m.b81*m.b171 - 2
                       *m.b82*m.b211 + 2*m.b82 - 2*m.b82*m.b259 + 2*m.b82*m.b269 - 2*m.b82*m.b310 + 2*m.b83*m.b84 - 2*
                       m.b84 + 2*m.b83*m.b216 + 2*m.b84*m.b131 + 2*m.b84*m.b158 - 4*m.b158 - 2*m.b84*m.b183 - 2*m.b183
                        + 2*m.b85*m.b87 - 2*m.b87 + 2*m.b85*m.b278 + 2*m.b86*m.b89 + 2*m.b86*m.b219 - 4*m.b219 + 2*m.b87
                       *m.b89 + 2*m.b87*m.b158 - 2*m.b87*m.b222 + 2*m.b222 - 2*m.b88*m.b90 + 2*m.b88 - 2*m.b88*m.b220 - 
                       2*m.b88*m.b231 + 2*m.b88*m.b242 + 2*m.b89*m.b90 + 2*m.b90*m.b91 + 2*m.b91*m.b92 + 2*m.b91*m.b134
                        - 2*m.b134 + 2*m.b92*m.b114 - 2*m.b114 + 2*m.b92*m.b135 - 4*m.b135 + 2*m.b93*m.b94 - 2*m.b94 + 2
                       *m.b93*m.b227 - 2*m.b227 + 2*m.b94*m.b114 + 2*m.b95*m.b196 + 2*m.b196 + 2*m.b95*m.b285 - 2*m.b95*
                       m.b300 + 2*m.b96*m.b97 - 2*m.b96*m.b196 + 2*m.b97*m.b118 - 2*m.b118 - 2*m.b97*m.b198 + 2*m.b198
                        + 2*m.b98*m.b99 - 2*m.b99 + 2*m.b99*m.b118 - 2*m.b99*m.b203 + 2*m.b203 + 2*m.b99*m.b266 + 2*
                       m.b100*m.b101 - 2*m.b100*m.b144 - 2*m.b144 + 2*m.b100*m.b173 - 2*m.b173 + 2*m.b101*m.b103 - 2*
                       m.b103 + 2*m.b101*m.b266 + 2*m.b102*m.b147 - 2*m.b147 - 2*m.b102*m.b177 + 2*m.b177 + 2*m.b102*
                       m.b271 + 2*m.b103*m.b174 - 2*m.b174 + 2*m.b103*m.b177 - 2*m.b103*m.b292 - 2*m.b104*m.b105 + 2*
                       m.b104 + 2*m.b105 - 2*m.b104*m.b244 + 2*m.b104*m.b253 - 2*m.b104*m.b290 + 2*m.b105*m.b106 - 2*
                       m.b105*m.b281 - 2*m.b105*m.b314 - 2*m.b106*m.b253 + 2*m.b106*m.b315 + 2*m.b107*m.b108 - 2*m.b108
                        + 2*m.b108*m.b158 + 2*m.b108*m.b185 - 4*m.b185 - 2*m.b108*m.b316 + 2*m.b109*m.b110 - 4*m.b110 + 
                       2*m.b109*m.b274 + 2*m.b110*m.b185 + 2*m.b110*m.b222 + 2*m.b110*m.b307 + 2*m.b111*m.b112 - 2*
                       m.b111*m.b246 + 2*m.b111*m.b307 + 2*m.b112*m.b113 + 2*m.b112*m.b162 - 2*m.b162 + 2*m.b113*m.b138
                        - 2*m.b138 + 2*m.b113*m.b163 - 4*m.b163 + 2*m.b114*m.b115 - 2*m.b115 - 2*m.b114*m.b136 + 2*
                       m.b115*m.b138 + 2*m.b116*m.b117 - 2*m.b117 + 2*m.b116*m.b166 - 2*m.b116*m.b304 + 2*m.b117*m.b194
                        - 2*m.b194 + 2*m.b117*m.b198 - 2*m.b117*m.b283 + 2*m.b118*m.b119 - 2*m.b119 - 2*m.b118*m.b250 + 
                       2*m.b119*m.b121 - 2*m.b121 - 2*m.b119*m.b286 + 2*m.b119*m.b318 - 2*m.b120*m.b235 - 2*m.b120*
                       m.b257 - 2*m.b120*m.b309 - 2*m.b121*m.b201 + 2*m.b121*m.b263 + 2*m.b121*m.b309 - 2*m.b122*m.b151
                        + 2*m.b151 + 2*m.b122*m.b173 + 2*m.b123*m.b151 + 2*m.b123*m.b206 - 2*m.b206 + 2*m.b123*m.b309 - 
                       2*m.b124*m.b125 + 4*m.b124 + 2*m.b125 - 2*m.b124*m.b251 - 2*m.b124*m.b253 - 2*m.b124*m.b287 + 2*
                       m.b125*m.b127 - 2*m.b125*m.b284 - 2*m.b125*m.b320 - 2*m.b126*m.b213 + 2*m.b126 - 2*m.b213 - 2*
                       m.b126*m.b264 - 2*m.b126*m.b265 + 2*m.b126*m.b296 + 2*m.b127*m.b213 + 2*m.b127*m.b253 + 2*m.b128*
                       m.b130 - 4*m.b130 + 2*m.b129*m.b130 - 4*m.b129 + 2*m.b129*m.b213 + 2*m.b129*m.b216 + 2*m.b129*
                       m.b265 + 2*m.b130*m.b185 + 2*m.b130*m.b218 - 4*m.b218 + 2*m.b131*m.b132 - 4*m.b132 + 2*m.b131*
                       m.b270 + 2*m.b132*m.b188 + 2*m.b188 + 2*m.b132*m.b218 + 2*m.b132*m.b303 - 2*m.b133*m.b134 + 2*
                       m.b133*m.b187 - 4*m.b187 - 2*m.b133*m.b278 + 2*m.b134*m.b135 + 2*m.b134*m.b303 + 2*m.b135*m.b137
                        + 2*m.b135*m.b190 - 2*m.b190 + 2*m.b136*m.b164 - 4*m.b164 + 2*m.b136*m.b191 - 2*m.b191 + 2*
                       m.b137*m.b164 + 2*m.b137*m.b192 - 2*m.b192 + 2*m.b138*m.b139 - 2*m.b139 - 2*m.b138*m.b232 + 2*
                       m.b139*m.b164 + 2*m.b140*m.b142 + 2*m.b141*m.b143 - 2*m.b143 + 2*m.b141*m.b289 - 2*m.b141*m.b308
                        + 2*m.b142*m.b143 + 2*m.b142*m.b308 + 2*m.b143*m.b168 - 2*m.b143*m.b279 + 2*m.b144*m.b146 - 2*
                       m.b146 + 2*m.b144*m.b318 + 2*m.b144*m.b321 - 2*m.b145*m.b148 - 2*m.b148 + 2*m.b146*m.b148 - 2*
                       m.b146*m.b256 + 2*m.b146*m.b257 - 2*m.b147*m.b150 - 2*m.b150 + 2*m.b147*m.b239 + 2*m.b147*m.b286
                        + 2*m.b148*m.b150 + 2*m.b148*m.b306 + 2*m.b149*m.b205 + 2*m.b205 + 2*m.b149*m.b251 - 2*m.b149*
                       m.b276 + 2*m.b150*m.b276 + 2*m.b150*m.b292 - 2*m.b151*m.b178 - 2*m.b151*m.b320 - 2*m.b152*m.b153
                        - 2*m.b153 - 2*m.b152*m.b177 - 2*m.b152*m.b258 + 2*m.b153*m.b155 + 2*m.b153*m.b284 + 2*m.b153*
                       m.b320 - 2*m.b154*m.b267 - 2*m.b154*m.b268 - 2*m.b154*m.b302 + 2*m.b155*m.b258 + 2*m.b155*m.b302
                        + 2*m.b156*m.b157 - 4*m.b157 - 2*m.b156*m.b293 + 2*m.b157*m.b159 - 2*m.b159 + 2*m.b157*m.b218 + 
                       2*m.b157*m.b316 + 2*m.b158*m.b160 - 4*m.b160 + 2*m.b159*m.b160 + 2*m.b159*m.b184 - 4*m.b184 - 2*
                       m.b159*m.b231 + 2*m.b160*m.b161 + 2*m.b161 + 2*m.b160*m.b298 - 2*m.b161*m.b162 - 2*m.b161*m.b236
                        - 2*m.b161*m.b274 + 2*m.b162*m.b163 + 2*m.b162*m.b298 + 2*m.b163*m.b224 - 2*m.b224 + 2*m.b163*
                       m.b226 + 2*m.b164*m.b323 + 2*m.b165*m.b167 - 2*m.b165 - 2*m.b167 - 2*m.b165*m.b260 + 2*m.b165*
                       m.b304 + 2*m.b165*m.b317 - 2*m.b166*m.b305 - 2*m.b167*m.b275 + 2*m.b167*m.b305 + 2*m.b167*m.b311
                        - 2*m.b168*m.b289 - 2*m.b168*m.b322 - 2*m.b169*m.b200 - 2*m.b200 + 2*m.b169*m.b283 + 2*m.b170*
                       m.b172 - 4*m.b170 + 2*m.b170*m.b200 + 2*m.b170*m.b286 + 2*m.b170*m.b321 - 2*m.b171*m.b174 - 2*
                       m.b171*m.b241 + 2*m.b172*m.b174 + 2*m.b172*m.b256 - 2*m.b173*m.b176 - 2*m.b176 + 2*m.b173*m.b234
                        + 2*m.b174*m.b176 + 2*m.b175*m.b244 - 2*m.b175 + 2*m.b175*m.b257 + 2*m.b175*m.b271 - 2*m.b175*
                       m.b272 + 2*m.b176*m.b272 + 2*m.b176*m.b290 - 2*m.b177*m.b314 - 2*m.b178*m.b179 - 2*m.b179 - 2*
                       m.b178*m.b264 + 2*m.b179*m.b181 + 2*m.b179*m.b281 + 2*m.b179*m.b314 - 2*m.b180*m.b230 - 2*m.b180*
                       m.b296 - 2*m.b180*m.b297 + 2*m.b181*m.b264 + 2*m.b181*m.b297 + 2*m.b182*m.b184 - 2*m.b182*m.b297
                        + 2*m.b183*m.b184 + 2*m.b183*m.b297 + 2*m.b183*m.b315 + 2*m.b184*m.b186 - 4*m.b186 + 2*m.b185*
                       m.b187 + 2*m.b186*m.b187 + 2*m.b186*m.b217 - 4*m.b217 + 2*m.b186*m.b231 + 2*m.b187*m.b189 - 2*
                       m.b189 - 2*m.b188*m.b190 - 2*m.b188*m.b242 - 2*m.b188*m.b270 + 2*m.b189*m.b190 - 2*m.b189*m.b282
                        + 2*m.b189*m.b294 + 2*m.b190*m.b192 - 2*m.b191*m.b193 + 2*m.b191*m.b236 + 2*m.b191*m.b247 + 2*
                       m.b192*m.b193 - 2*m.b192*m.b247 + 2*m.b193*m.b228 + 2*m.b194*m.b197 + 2*m.b194*m.b312 - 2*m.b194*
                       m.b317 + 2*m.b195*m.b197 - 2*m.b195 - 2*m.b195*m.b254 + 2*m.b195*m.b300 + 2*m.b195*m.b313 - 2*
                       m.b196*m.b295 - 2*m.b196*m.b301 + 2*m.b197*m.b301 - 2*m.b198*m.b285 - 2*m.b198*m.b319 + 2*m.b199*
                       m.b279 - 2*m.b199*m.b280 + 2*m.b200*m.b202 - 4*m.b202 + 2*m.b200*m.b322 + 2*m.b201*m.b204 + 2*
                       m.b202*m.b203 + 2*m.b202*m.b204 + 2*m.b202*m.b280 - 2*m.b203*m.b206 - 2*m.b203*m.b271 + 2*m.b204*
                       m.b206 - 2*m.b205*m.b207 - 2*m.b207 - 2*m.b205*m.b234 - 2*m.b205*m.b286 + 2*m.b206*m.b207 + 2*
                       m.b207*m.b208 - 2*m.b208 + 2*m.b207*m.b287 + 2*m.b208*m.b209 + 2*m.b209 - 2*m.b208*m.b245 + 2*
                       m.b208*m.b310 - 2*m.b209*m.b210 - 2*m.b210 - 2*m.b209*m.b267 - 2*m.b209*m.b276 + 2*m.b210*m.b211
                        + 2*m.b210*m.b212 + 2*m.b210*m.b310 - 2*m.b211*m.b293 + 2*m.b212*m.b267 + 2*m.b212*m.b293 + 2*
                       m.b213*m.b215 + 2*m.b214*m.b217 - 2*m.b214*m.b302 + 2*m.b215*m.b217 + 2*m.b215*m.b293 + 2*m.b216*
                       m.b219 + 2*m.b217*m.b219 + 2*m.b218*m.b221 - 4*m.b221 + 2*m.b219*m.b221 - 2*m.b220*m.b223 + 2*
                       m.b221*m.b223 + 2*m.b221*m.b246 - 2*m.b222*m.b224 - 2*m.b222*m.b247 + 2*m.b223*m.b224 + 2*m.b224*
                       m.b225 - 2*m.b225 + 2*m.b225*m.b226 + 2*m.b225*m.b227 - 2*m.b225*m.b242 - 2*m.b226*m.b324 - 2*
                       m.b227*m.b233 + 2*m.b227*m.b324 + 2*m.b228*m.b232 - 2*m.b228*m.b325 - 2*m.b229*m.b230 + 2*m.b229*
                       m.b265 - 2*m.b232*m.b233 + 2*m.b233*m.b242 - 2*m.b234*m.b235 + 2*m.b236*m.b246 - 2*m.b237*m.b238
                        - 2*m.b237*m.b248 + 2*m.b237*m.b254 + 2*m.b238*m.b295 - 2*m.b239*m.b240 + 2*m.b239*m.b241 - 2*
                       m.b239*m.b271 - 2*m.b240*m.b266 - 2*m.b241*m.b280 - 2*m.b244*m.b245 + 2*m.b244*m.b259 + 2*m.b245*
                       m.b263 - 2*m.b246*m.b282 - 2*m.b248*m.b279 - 2*m.b249*m.b250 - 2*m.b249*m.b256 + 2*m.b250*m.b279
                        - 2*m.b251*m.b252 - 2*m.b252*m.b263 - 2*m.b254*m.b275 + 2*m.b255*m.b275 - 2*m.b255*m.b318 + 2*
                       m.b258*m.b259 - 2*m.b258*m.b269 - 2*m.b259*m.b292 - 2*m.b261*m.b321 - 2*m.b262*m.b301 - 2*m.b263*
                       m.b266 - 2*m.b265*m.b277 + 2*m.b268*m.b269 - 2*m.b268*m.b273 - 2*m.b269*m.b315 - 2*m.b270*m.b307
                        + 2*m.b272*m.b314 - 2*m.b274*m.b303 + 2*m.b276*m.b320 - 2*m.b278*m.b298 + 2*m.b280*m.b319 + 2*
                       m.b285*m.b311 + 2*m.b287*m.b306 - 2*m.b287*m.b310 - 2*m.b288*m.b291 + 2*m.b289*m.b295 - 2*m.b290*
                       m.b306 - 2*m.b291*m.b294 - 2*m.b294*m.b298 - 2*m.b299*m.b307 + 2*m.b301*m.b319 + 2*m.b302*m.b316
                        + 2*m.b305*m.b322 - 2*m.b306*m.b309 - 2*m.b311*m.b312 - 2*m.b311*m.b313 - 2*m.b315*m.b316 - 2*
                       m.b318*m.b319 - 2*m.b321*m.b322 - 2*m.b323*m.b324 + 2*m.b324*m.b325 + m.x326 <= 0)
