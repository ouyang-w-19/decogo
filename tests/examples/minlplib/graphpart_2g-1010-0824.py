#  MINLP written by GAMS Convert at 04/21/18 13:52:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        101      101        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        301        1      300        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        601      301      300        0
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

m.obj = Objective(expr=(-140500*m.b1*m.b4) - 6168*m.b1*m.b28 + 69805*m.b1*m.b31 + 99537*m.b1*m.b271 - 140500*m.b2*m.b5
                        - 6168*m.b2*m.b29 + 69805*m.b2*m.b32 + 99537*m.b2*m.b272 - 140500*m.b3*m.b6 - 6168*m.b3*m.b30 + 
                       69805*m.b3*m.b33 + 99537*m.b3*m.b273 + 243172*m.b4*m.b7 - 106973*m.b4*m.b34 - 75892*m.b4*m.b274
                        + 243172*m.b5*m.b8 - 106973*m.b5*m.b35 - 75892*m.b5*m.b275 + 243172*m.b6*m.b9 - 106973*m.b6*
                       m.b36 - 75892*m.b6*m.b276 + 57380*m.b7*m.b10 - 161384*m.b7*m.b37 - 31457*m.b7*m.b277 + 57380*m.b8
                       *m.b11 - 161384*m.b8*m.b38 - 31457*m.b8*m.b278 + 57380*m.b9*m.b12 - 161384*m.b9*m.b39 - 31457*
                       m.b9*m.b279 + 47389*m.b10*m.b13 - 130709*m.b10*m.b40 - 118141*m.b10*m.b280 + 47389*m.b11*m.b14 - 
                       130709*m.b11*m.b41 - 118141*m.b11*m.b281 + 47389*m.b12*m.b15 - 130709*m.b12*m.b42 - 118141*m.b12*
                       m.b282 + 8824*m.b13*m.b16 + 59639*m.b13*m.b43 + 77772*m.b13*m.b283 + 8824*m.b14*m.b17 + 59639*
                       m.b14*m.b44 + 77772*m.b14*m.b284 + 8824*m.b15*m.b18 + 59639*m.b15*m.b45 + 77772*m.b15*m.b285 + 
                       44460*m.b16*m.b19 + 16922*m.b16*m.b46 + 101315*m.b16*m.b286 + 44460*m.b17*m.b20 + 16922*m.b17*
                       m.b47 + 101315*m.b17*m.b287 + 44460*m.b18*m.b21 + 16922*m.b18*m.b48 + 101315*m.b18*m.b288 - 16373
                       *m.b19*m.b22 - 17220*m.b19*m.b49 - 22319*m.b19*m.b289 - 16373*m.b20*m.b23 - 17220*m.b20*m.b50 - 
                       22319*m.b20*m.b290 - 16373*m.b21*m.b24 - 17220*m.b21*m.b51 - 22319*m.b21*m.b291 + 142391*m.b22*
                       m.b25 - 32331*m.b22*m.b52 + 205481*m.b22*m.b292 + 142391*m.b23*m.b26 - 32331*m.b23*m.b53 + 205481
                       *m.b23*m.b293 + 142391*m.b24*m.b27 - 32331*m.b24*m.b54 + 205481*m.b24*m.b294 - 67473*m.b25*m.b28
                        - 38478*m.b25*m.b55 + 12209*m.b25*m.b295 - 67473*m.b26*m.b29 - 38478*m.b26*m.b56 + 12209*m.b26*
                       m.b296 - 67473*m.b27*m.b30 - 38478*m.b27*m.b57 + 12209*m.b27*m.b297 + 41199*m.b28*m.b58 + 88687*
                       m.b28*m.b298 + 41199*m.b29*m.b59 + 88687*m.b29*m.b299 + 41199*m.b30*m.b60 + 88687*m.b30*m.b300 - 
                       103914*m.b31*m.b34 - 78967*m.b31*m.b58 - 35106*m.b31*m.b61 - 103914*m.b32*m.b35 - 78967*m.b32*
                       m.b59 - 35106*m.b32*m.b62 - 103914*m.b33*m.b36 - 78967*m.b33*m.b60 - 35106*m.b33*m.b63 + 126330*
                       m.b34*m.b37 + 63341*m.b34*m.b64 + 126330*m.b35*m.b38 + 63341*m.b35*m.b65 + 126330*m.b36*m.b39 + 
                       63341*m.b36*m.b66 + 179120*m.b37*m.b40 - 148919*m.b37*m.b67 + 179120*m.b38*m.b41 - 148919*m.b38*
                       m.b68 + 179120*m.b39*m.b42 - 148919*m.b39*m.b69 - 79*m.b40*m.b43 + 57817*m.b40*m.b70 - 79*m.b41*
                       m.b44 + 57817*m.b41*m.b71 - 79*m.b42*m.b45 + 57817*m.b42*m.b72 - 145504*m.b43*m.b46 - 25404*m.b43
                       *m.b73 - 145504*m.b44*m.b47 - 25404*m.b44*m.b74 - 145504*m.b45*m.b48 - 25404*m.b45*m.b75 + 2643*
                       m.b46*m.b49 - 94271*m.b46*m.b76 + 2643*m.b47*m.b50 - 94271*m.b47*m.b77 + 2643*m.b48*m.b51 - 94271
                       *m.b48*m.b78 - 3237*m.b49*m.b52 - 113326*m.b49*m.b79 - 3237*m.b50*m.b53 - 113326*m.b50*m.b80 - 
                       3237*m.b51*m.b54 - 113326*m.b51*m.b81 - 34448*m.b52*m.b55 + 70947*m.b52*m.b82 - 34448*m.b53*m.b56
                        + 70947*m.b53*m.b83 - 34448*m.b54*m.b57 + 70947*m.b54*m.b84 + 87914*m.b55*m.b58 - 194219*m.b55*
                       m.b85 + 87914*m.b56*m.b59 - 194219*m.b56*m.b86 + 87914*m.b57*m.b60 - 194219*m.b57*m.b87 + 100179*
                       m.b58*m.b88 + 100179*m.b59*m.b89 + 100179*m.b60*m.b90 + 113386*m.b61*m.b64 + 146383*m.b61*m.b88
                        + 95534*m.b61*m.b91 + 113386*m.b62*m.b65 + 146383*m.b62*m.b89 + 95534*m.b62*m.b92 + 113386*m.b63
                       *m.b66 + 146383*m.b63*m.b90 + 95534*m.b63*m.b93 - 216283*m.b64*m.b67 + 132661*m.b64*m.b94 - 
                       216283*m.b65*m.b68 + 132661*m.b65*m.b95 - 216283*m.b66*m.b69 + 132661*m.b66*m.b96 + 45184*m.b67*
                       m.b70 - 161057*m.b67*m.b97 + 45184*m.b68*m.b71 - 161057*m.b68*m.b98 + 45184*m.b69*m.b72 - 161057*
                       m.b69*m.b99 + 107039*m.b70*m.b73 - 41532*m.b70*m.b100 + 107039*m.b71*m.b74 - 41532*m.b71*m.b101
                        + 107039*m.b72*m.b75 - 41532*m.b72*m.b102 - 52792*m.b73*m.b76 - 16199*m.b73*m.b103 - 52792*m.b74
                       *m.b77 - 16199*m.b74*m.b104 - 52792*m.b75*m.b78 - 16199*m.b75*m.b105 - 155271*m.b76*m.b79 + 
                       119259*m.b76*m.b106 - 155271*m.b77*m.b80 + 119259*m.b77*m.b107 - 155271*m.b78*m.b81 + 119259*
                       m.b78*m.b108 - 110981*m.b79*m.b82 - 78323*m.b79*m.b109 - 110981*m.b80*m.b83 - 78323*m.b80*m.b110
                        - 110981*m.b81*m.b84 - 78323*m.b81*m.b111 + 158177*m.b82*m.b85 - 43898*m.b82*m.b112 + 158177*
                       m.b83*m.b86 - 43898*m.b83*m.b113 + 158177*m.b84*m.b87 - 43898*m.b84*m.b114 - 114367*m.b85*m.b88
                        - 213090*m.b85*m.b115 - 114367*m.b86*m.b89 - 213090*m.b86*m.b116 - 114367*m.b87*m.b90 - 213090*
                       m.b87*m.b117 + 217366*m.b88*m.b118 + 217366*m.b89*m.b119 + 217366*m.b90*m.b120 + 51648*m.b91*
                       m.b94 + 54470*m.b91*m.b118 + 103741*m.b91*m.b121 + 51648*m.b92*m.b95 + 54470*m.b92*m.b119 + 
                       103741*m.b92*m.b122 + 51648*m.b93*m.b96 + 54470*m.b93*m.b120 + 103741*m.b93*m.b123 - 103486*m.b94
                       *m.b97 - 25206*m.b94*m.b124 - 103486*m.b95*m.b98 - 25206*m.b95*m.b125 - 103486*m.b96*m.b99 - 
                       25206*m.b96*m.b126 - 121719*m.b97*m.b100 - 189420*m.b97*m.b127 - 121719*m.b98*m.b101 - 189420*
                       m.b98*m.b128 - 121719*m.b99*m.b102 - 189420*m.b99*m.b129 - 30445*m.b100*m.b103 - 31937*m.b100*
                       m.b130 - 30445*m.b101*m.b104 - 31937*m.b101*m.b131 - 30445*m.b102*m.b105 - 31937*m.b102*m.b132 - 
                       50463*m.b103*m.b106 - 122279*m.b103*m.b133 - 50463*m.b104*m.b107 - 122279*m.b104*m.b134 - 50463*
                       m.b105*m.b108 - 122279*m.b105*m.b135 - 55487*m.b106*m.b109 - 4137*m.b106*m.b136 - 55487*m.b107*
                       m.b110 - 4137*m.b107*m.b137 - 55487*m.b108*m.b111 - 4137*m.b108*m.b138 + 143431*m.b109*m.b112 - 
                       44217*m.b109*m.b139 + 143431*m.b110*m.b113 - 44217*m.b110*m.b140 + 143431*m.b111*m.b114 - 44217*
                       m.b111*m.b141 + 52272*m.b112*m.b115 - 45507*m.b112*m.b142 + 52272*m.b113*m.b116 - 45507*m.b113*
                       m.b143 + 52272*m.b114*m.b117 - 45507*m.b114*m.b144 - 111550*m.b115*m.b118 - 58115*m.b115*m.b145
                        - 111550*m.b116*m.b119 - 58115*m.b116*m.b146 - 111550*m.b117*m.b120 - 58115*m.b117*m.b147 + 
                       132392*m.b118*m.b148 + 132392*m.b119*m.b149 + 132392*m.b120*m.b150 + 120695*m.b121*m.b124 + 44324
                       *m.b121*m.b148 - 93232*m.b121*m.b151 + 120695*m.b122*m.b125 + 44324*m.b122*m.b149 - 93232*m.b122*
                       m.b152 + 120695*m.b123*m.b126 + 44324*m.b123*m.b150 - 93232*m.b123*m.b153 + 71125*m.b124*m.b127
                        + 71545*m.b124*m.b154 + 71125*m.b125*m.b128 + 71545*m.b125*m.b155 + 71125*m.b126*m.b129 + 71545*
                       m.b126*m.b156 + 61420*m.b127*m.b130 - 75807*m.b127*m.b157 + 61420*m.b128*m.b131 - 75807*m.b128*
                       m.b158 + 61420*m.b129*m.b132 - 75807*m.b129*m.b159 + 2350*m.b130*m.b133 - 50108*m.b130*m.b160 + 
                       2350*m.b131*m.b134 - 50108*m.b131*m.b161 + 2350*m.b132*m.b135 - 50108*m.b132*m.b162 - 79469*
                       m.b133*m.b136 + 162799*m.b133*m.b163 - 79469*m.b134*m.b137 + 162799*m.b134*m.b164 - 79469*m.b135*
                       m.b138 + 162799*m.b135*m.b165 - 28158*m.b136*m.b139 + 108362*m.b136*m.b166 - 28158*m.b137*m.b140
                        + 108362*m.b137*m.b167 - 28158*m.b138*m.b141 + 108362*m.b138*m.b168 + 37422*m.b139*m.b142 - 
                       155036*m.b139*m.b169 + 37422*m.b140*m.b143 - 155036*m.b140*m.b170 + 37422*m.b141*m.b144 - 155036*
                       m.b141*m.b171 - 4442*m.b142*m.b145 + 57204*m.b142*m.b172 - 4442*m.b143*m.b146 + 57204*m.b143*
                       m.b173 - 4442*m.b144*m.b147 + 57204*m.b144*m.b174 - 4297*m.b145*m.b148 - 80716*m.b145*m.b175 - 
                       4297*m.b146*m.b149 - 80716*m.b146*m.b176 - 4297*m.b147*m.b150 - 80716*m.b147*m.b177 + 47830*
                       m.b148*m.b178 + 47830*m.b149*m.b179 + 47830*m.b150*m.b180 + 63143*m.b151*m.b154 - 85053*m.b151*
                       m.b178 - 81899*m.b151*m.b181 + 63143*m.b152*m.b155 - 85053*m.b152*m.b179 - 81899*m.b152*m.b182 + 
                       63143*m.b153*m.b156 - 85053*m.b153*m.b180 - 81899*m.b153*m.b183 + 94887*m.b154*m.b157 - 93735*
                       m.b154*m.b184 + 94887*m.b155*m.b158 - 93735*m.b155*m.b185 + 94887*m.b156*m.b159 - 93735*m.b156*
                       m.b186 + 31709*m.b157*m.b160 + 37028*m.b157*m.b187 + 31709*m.b158*m.b161 + 37028*m.b158*m.b188 + 
                       31709*m.b159*m.b162 + 37028*m.b159*m.b189 + 22317*m.b160*m.b163 + 221122*m.b160*m.b190 + 22317*
                       m.b161*m.b164 + 221122*m.b161*m.b191 + 22317*m.b162*m.b165 + 221122*m.b162*m.b192 - 47890*m.b163*
                       m.b166 - 24565*m.b163*m.b193 - 47890*m.b164*m.b167 - 24565*m.b164*m.b194 - 47890*m.b165*m.b168 - 
                       24565*m.b165*m.b195 + 25735*m.b166*m.b169 + 92913*m.b166*m.b196 + 25735*m.b167*m.b170 + 92913*
                       m.b167*m.b197 + 25735*m.b168*m.b171 + 92913*m.b168*m.b198 + 82226*m.b169*m.b172 - 46424*m.b169*
                       m.b199 + 82226*m.b170*m.b173 - 46424*m.b170*m.b200 + 82226*m.b171*m.b174 - 46424*m.b171*m.b201 + 
                       116524*m.b172*m.b175 - 59183*m.b172*m.b202 + 116524*m.b173*m.b176 - 59183*m.b173*m.b203 + 116524*
                       m.b174*m.b177 - 59183*m.b174*m.b204 + 10300*m.b175*m.b178 - 12844*m.b175*m.b205 + 10300*m.b176*
                       m.b179 - 12844*m.b176*m.b206 + 10300*m.b177*m.b180 - 12844*m.b177*m.b207 - 51909*m.b178*m.b208 - 
                       51909*m.b179*m.b209 - 51909*m.b180*m.b210 - 120463*m.b181*m.b184 + 110062*m.b181*m.b208 + 58801*
                       m.b181*m.b211 - 120463*m.b182*m.b185 + 110062*m.b182*m.b209 + 58801*m.b182*m.b212 - 120463*m.b183
                       *m.b186 + 110062*m.b183*m.b210 + 58801*m.b183*m.b213 - 108142*m.b184*m.b187 - 210930*m.b184*
                       m.b214 - 108142*m.b185*m.b188 - 210930*m.b185*m.b215 - 108142*m.b186*m.b189 - 210930*m.b186*
                       m.b216 + 145601*m.b187*m.b190 + 104550*m.b187*m.b217 + 145601*m.b188*m.b191 + 104550*m.b188*
                       m.b218 + 145601*m.b189*m.b192 + 104550*m.b189*m.b219 + 231665*m.b190*m.b193 + 51705*m.b190*m.b220
                        + 231665*m.b191*m.b194 + 51705*m.b191*m.b221 + 231665*m.b192*m.b195 + 51705*m.b192*m.b222 - 
                       49380*m.b193*m.b196 + 21233*m.b193*m.b223 - 49380*m.b194*m.b197 + 21233*m.b194*m.b224 - 49380*
                       m.b195*m.b198 + 21233*m.b195*m.b225 + 61670*m.b196*m.b199 - 101100*m.b196*m.b226 + 61670*m.b197*
                       m.b200 - 101100*m.b197*m.b227 + 61670*m.b198*m.b201 - 101100*m.b198*m.b228 + 66074*m.b199*m.b202
                        - 103726*m.b199*m.b229 + 66074*m.b200*m.b203 - 103726*m.b200*m.b230 + 66074*m.b201*m.b204 - 
                       103726*m.b201*m.b231 + 23275*m.b202*m.b205 - 239558*m.b202*m.b232 + 23275*m.b203*m.b206 - 239558*
                       m.b203*m.b233 + 23275*m.b204*m.b207 - 239558*m.b204*m.b234 - 144999*m.b205*m.b208 + 30889*m.b205*
                       m.b235 - 144999*m.b206*m.b209 + 30889*m.b206*m.b236 - 144999*m.b207*m.b210 + 30889*m.b207*m.b237
                        - 65255*m.b208*m.b238 - 65255*m.b209*m.b239 - 65255*m.b210*m.b240 - 208953*m.b211*m.b214 + 11477
                       *m.b211*m.b238 + 268429*m.b211*m.b241 - 208953*m.b212*m.b215 + 11477*m.b212*m.b239 + 268429*
                       m.b212*m.b242 - 208953*m.b213*m.b216 + 11477*m.b213*m.b240 + 268429*m.b213*m.b243 + 26984*m.b214*
                       m.b217 - 170553*m.b214*m.b244 + 26984*m.b215*m.b218 - 170553*m.b215*m.b245 + 26984*m.b216*m.b219
                        - 170553*m.b216*m.b246 + 69156*m.b217*m.b220 + 44984*m.b217*m.b247 + 69156*m.b218*m.b221 + 44984
                       *m.b218*m.b248 + 69156*m.b219*m.b222 + 44984*m.b219*m.b249 - 23255*m.b220*m.b223 - 5961*m.b220*
                       m.b250 - 23255*m.b221*m.b224 - 5961*m.b221*m.b251 - 23255*m.b222*m.b225 - 5961*m.b222*m.b252 + 
                       71643*m.b223*m.b226 + 57314*m.b223*m.b253 + 71643*m.b224*m.b227 + 57314*m.b224*m.b254 + 71643*
                       m.b225*m.b228 + 57314*m.b225*m.b255 + 18626*m.b226*m.b229 + 243235*m.b226*m.b256 + 18626*m.b227*
                       m.b230 + 243235*m.b227*m.b257 + 18626*m.b228*m.b231 + 243235*m.b228*m.b258 - 32740*m.b229*m.b232
                        - 41971*m.b229*m.b259 - 32740*m.b230*m.b233 - 41971*m.b230*m.b260 - 32740*m.b231*m.b234 - 41971*
                       m.b231*m.b261 + 59354*m.b232*m.b235 + 63438*m.b232*m.b262 + 59354*m.b233*m.b236 + 63438*m.b233*
                       m.b263 + 59354*m.b234*m.b237 + 63438*m.b234*m.b264 + 2745*m.b235*m.b238 + 1963*m.b235*m.b265 + 
                       2745*m.b236*m.b239 + 1963*m.b236*m.b266 + 2745*m.b237*m.b240 + 1963*m.b237*m.b267 + 19196*m.b238*
                       m.b268 + 19196*m.b239*m.b269 + 19196*m.b240*m.b270 + 29280*m.b241*m.b244 + 9212*m.b241*m.b268 + 
                       152008*m.b241*m.b271 + 29280*m.b242*m.b245 + 9212*m.b242*m.b269 + 152008*m.b242*m.b272 + 29280*
                       m.b243*m.b246 + 9212*m.b243*m.b270 + 152008*m.b243*m.b273 + 37618*m.b244*m.b247 + 6449*m.b244*
                       m.b274 + 37618*m.b245*m.b248 + 6449*m.b245*m.b275 + 37618*m.b246*m.b249 + 6449*m.b246*m.b276 + 
                       101612*m.b247*m.b250 - 104102*m.b247*m.b277 + 101612*m.b248*m.b251 - 104102*m.b248*m.b278 + 
                       101612*m.b249*m.b252 - 104102*m.b249*m.b279 + 33724*m.b250*m.b253 + 126817*m.b250*m.b280 + 33724*
                       m.b251*m.b254 + 126817*m.b251*m.b281 + 33724*m.b252*m.b255 + 126817*m.b252*m.b282 + 72754*m.b253*
                       m.b256 - 17622*m.b253*m.b283 + 72754*m.b254*m.b257 - 17622*m.b254*m.b284 + 72754*m.b255*m.b258 - 
                       17622*m.b255*m.b285 + 73668*m.b256*m.b259 + 161048*m.b256*m.b286 + 73668*m.b257*m.b260 + 161048*
                       m.b257*m.b287 + 73668*m.b258*m.b261 + 161048*m.b258*m.b288 - 55290*m.b259*m.b262 + 69537*m.b259*
                       m.b289 - 55290*m.b260*m.b263 + 69537*m.b260*m.b290 - 55290*m.b261*m.b264 + 69537*m.b261*m.b291 - 
                       142640*m.b262*m.b265 + 50161*m.b262*m.b292 - 142640*m.b263*m.b266 + 50161*m.b263*m.b293 - 142640*
                       m.b264*m.b267 + 50161*m.b264*m.b294 + 115122*m.b265*m.b268 + 209308*m.b265*m.b295 + 115122*m.b266
                       *m.b269 + 209308*m.b266*m.b296 + 115122*m.b267*m.b270 + 209308*m.b267*m.b297 - 89633*m.b268*
                       m.b298 - 89633*m.b269*m.b299 - 89633*m.b270*m.b300 + 85472*m.b271*m.b274 - 65488*m.b271*m.b298 + 
                       85472*m.b272*m.b275 - 65488*m.b272*m.b299 + 85472*m.b273*m.b276 - 65488*m.b273*m.b300 - 97644*
                       m.b274*m.b277 - 97644*m.b275*m.b278 - 97644*m.b276*m.b279 - 22383*m.b277*m.b280 - 22383*m.b278*
                       m.b281 - 22383*m.b279*m.b282 + 39505*m.b280*m.b283 + 39505*m.b281*m.b284 + 39505*m.b282*m.b285 - 
                       26866*m.b283*m.b286 - 26866*m.b284*m.b287 - 26866*m.b285*m.b288 - 104695*m.b286*m.b289 - 104695*
                       m.b287*m.b290 - 104695*m.b288*m.b291 - 118676*m.b289*m.b292 - 118676*m.b290*m.b293 - 118676*
                       m.b291*m.b294 - 80157*m.b292*m.b295 - 80157*m.b293*m.b296 - 80157*m.b294*m.b297 - 29119*m.b295*
                       m.b298 - 29119*m.b296*m.b299 - 29119*m.b297*m.b300, sense=minimize)

m.c1 = Constraint(expr=   m.b1 + m.b2 + m.b3 == 1)

m.c2 = Constraint(expr=   m.b4 + m.b5 + m.b6 == 1)

m.c3 = Constraint(expr=   m.b7 + m.b8 + m.b9 == 1)

m.c4 = Constraint(expr=   m.b10 + m.b11 + m.b12 == 1)

m.c5 = Constraint(expr=   m.b13 + m.b14 + m.b15 == 1)

m.c6 = Constraint(expr=   m.b16 + m.b17 + m.b18 == 1)

m.c7 = Constraint(expr=   m.b19 + m.b20 + m.b21 == 1)

m.c8 = Constraint(expr=   m.b22 + m.b23 + m.b24 == 1)

m.c9 = Constraint(expr=   m.b25 + m.b26 + m.b27 == 1)

m.c10 = Constraint(expr=   m.b28 + m.b29 + m.b30 == 1)

m.c11 = Constraint(expr=   m.b31 + m.b32 + m.b33 == 1)

m.c12 = Constraint(expr=   m.b34 + m.b35 + m.b36 == 1)

m.c13 = Constraint(expr=   m.b37 + m.b38 + m.b39 == 1)

m.c14 = Constraint(expr=   m.b40 + m.b41 + m.b42 == 1)

m.c15 = Constraint(expr=   m.b43 + m.b44 + m.b45 == 1)

m.c16 = Constraint(expr=   m.b46 + m.b47 + m.b48 == 1)

m.c17 = Constraint(expr=   m.b49 + m.b50 + m.b51 == 1)

m.c18 = Constraint(expr=   m.b52 + m.b53 + m.b54 == 1)

m.c19 = Constraint(expr=   m.b55 + m.b56 + m.b57 == 1)

m.c20 = Constraint(expr=   m.b58 + m.b59 + m.b60 == 1)

m.c21 = Constraint(expr=   m.b61 + m.b62 + m.b63 == 1)

m.c22 = Constraint(expr=   m.b64 + m.b65 + m.b66 == 1)

m.c23 = Constraint(expr=   m.b67 + m.b68 + m.b69 == 1)

m.c24 = Constraint(expr=   m.b70 + m.b71 + m.b72 == 1)

m.c25 = Constraint(expr=   m.b73 + m.b74 + m.b75 == 1)

m.c26 = Constraint(expr=   m.b76 + m.b77 + m.b78 == 1)

m.c27 = Constraint(expr=   m.b79 + m.b80 + m.b81 == 1)

m.c28 = Constraint(expr=   m.b82 + m.b83 + m.b84 == 1)

m.c29 = Constraint(expr=   m.b85 + m.b86 + m.b87 == 1)

m.c30 = Constraint(expr=   m.b88 + m.b89 + m.b90 == 1)

m.c31 = Constraint(expr=   m.b91 + m.b92 + m.b93 == 1)

m.c32 = Constraint(expr=   m.b94 + m.b95 + m.b96 == 1)

m.c33 = Constraint(expr=   m.b97 + m.b98 + m.b99 == 1)

m.c34 = Constraint(expr=   m.b100 + m.b101 + m.b102 == 1)

m.c35 = Constraint(expr=   m.b103 + m.b104 + m.b105 == 1)

m.c36 = Constraint(expr=   m.b106 + m.b107 + m.b108 == 1)

m.c37 = Constraint(expr=   m.b109 + m.b110 + m.b111 == 1)

m.c38 = Constraint(expr=   m.b112 + m.b113 + m.b114 == 1)

m.c39 = Constraint(expr=   m.b115 + m.b116 + m.b117 == 1)

m.c40 = Constraint(expr=   m.b118 + m.b119 + m.b120 == 1)

m.c41 = Constraint(expr=   m.b121 + m.b122 + m.b123 == 1)

m.c42 = Constraint(expr=   m.b124 + m.b125 + m.b126 == 1)

m.c43 = Constraint(expr=   m.b127 + m.b128 + m.b129 == 1)

m.c44 = Constraint(expr=   m.b130 + m.b131 + m.b132 == 1)

m.c45 = Constraint(expr=   m.b133 + m.b134 + m.b135 == 1)

m.c46 = Constraint(expr=   m.b136 + m.b137 + m.b138 == 1)

m.c47 = Constraint(expr=   m.b139 + m.b140 + m.b141 == 1)

m.c48 = Constraint(expr=   m.b142 + m.b143 + m.b144 == 1)

m.c49 = Constraint(expr=   m.b145 + m.b146 + m.b147 == 1)

m.c50 = Constraint(expr=   m.b148 + m.b149 + m.b150 == 1)

m.c51 = Constraint(expr=   m.b151 + m.b152 + m.b153 == 1)

m.c52 = Constraint(expr=   m.b154 + m.b155 + m.b156 == 1)

m.c53 = Constraint(expr=   m.b157 + m.b158 + m.b159 == 1)

m.c54 = Constraint(expr=   m.b160 + m.b161 + m.b162 == 1)

m.c55 = Constraint(expr=   m.b163 + m.b164 + m.b165 == 1)

m.c56 = Constraint(expr=   m.b166 + m.b167 + m.b168 == 1)

m.c57 = Constraint(expr=   m.b169 + m.b170 + m.b171 == 1)

m.c58 = Constraint(expr=   m.b172 + m.b173 + m.b174 == 1)

m.c59 = Constraint(expr=   m.b175 + m.b176 + m.b177 == 1)

m.c60 = Constraint(expr=   m.b178 + m.b179 + m.b180 == 1)

m.c61 = Constraint(expr=   m.b181 + m.b182 + m.b183 == 1)

m.c62 = Constraint(expr=   m.b184 + m.b185 + m.b186 == 1)

m.c63 = Constraint(expr=   m.b187 + m.b188 + m.b189 == 1)

m.c64 = Constraint(expr=   m.b190 + m.b191 + m.b192 == 1)

m.c65 = Constraint(expr=   m.b193 + m.b194 + m.b195 == 1)

m.c66 = Constraint(expr=   m.b196 + m.b197 + m.b198 == 1)

m.c67 = Constraint(expr=   m.b199 + m.b200 + m.b201 == 1)

m.c68 = Constraint(expr=   m.b202 + m.b203 + m.b204 == 1)

m.c69 = Constraint(expr=   m.b205 + m.b206 + m.b207 == 1)

m.c70 = Constraint(expr=   m.b208 + m.b209 + m.b210 == 1)

m.c71 = Constraint(expr=   m.b211 + m.b212 + m.b213 == 1)

m.c72 = Constraint(expr=   m.b214 + m.b215 + m.b216 == 1)

m.c73 = Constraint(expr=   m.b217 + m.b218 + m.b219 == 1)

m.c74 = Constraint(expr=   m.b220 + m.b221 + m.b222 == 1)

m.c75 = Constraint(expr=   m.b223 + m.b224 + m.b225 == 1)

m.c76 = Constraint(expr=   m.b226 + m.b227 + m.b228 == 1)

m.c77 = Constraint(expr=   m.b229 + m.b230 + m.b231 == 1)

m.c78 = Constraint(expr=   m.b232 + m.b233 + m.b234 == 1)

m.c79 = Constraint(expr=   m.b235 + m.b236 + m.b237 == 1)

m.c80 = Constraint(expr=   m.b238 + m.b239 + m.b240 == 1)

m.c81 = Constraint(expr=   m.b241 + m.b242 + m.b243 == 1)

m.c82 = Constraint(expr=   m.b244 + m.b245 + m.b246 == 1)

m.c83 = Constraint(expr=   m.b247 + m.b248 + m.b249 == 1)

m.c84 = Constraint(expr=   m.b250 + m.b251 + m.b252 == 1)

m.c85 = Constraint(expr=   m.b253 + m.b254 + m.b255 == 1)

m.c86 = Constraint(expr=   m.b256 + m.b257 + m.b258 == 1)

m.c87 = Constraint(expr=   m.b259 + m.b260 + m.b261 == 1)

m.c88 = Constraint(expr=   m.b262 + m.b263 + m.b264 == 1)

m.c89 = Constraint(expr=   m.b265 + m.b266 + m.b267 == 1)

m.c90 = Constraint(expr=   m.b268 + m.b269 + m.b270 == 1)

m.c91 = Constraint(expr=   m.b271 + m.b272 + m.b273 == 1)

m.c92 = Constraint(expr=   m.b274 + m.b275 + m.b276 == 1)

m.c93 = Constraint(expr=   m.b277 + m.b278 + m.b279 == 1)

m.c94 = Constraint(expr=   m.b280 + m.b281 + m.b282 == 1)

m.c95 = Constraint(expr=   m.b283 + m.b284 + m.b285 == 1)

m.c96 = Constraint(expr=   m.b286 + m.b287 + m.b288 == 1)

m.c97 = Constraint(expr=   m.b289 + m.b290 + m.b291 == 1)

m.c98 = Constraint(expr=   m.b292 + m.b293 + m.b294 == 1)

m.c99 = Constraint(expr=   m.b295 + m.b296 + m.b297 == 1)

m.c100 = Constraint(expr=   m.b298 + m.b299 + m.b300 == 1)
