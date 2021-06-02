#  MINLP written by GAMS Convert at 04/21/18 13:51:13
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        688       33      302      353        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        329       73      200       56        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       3980     3302      678        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=0)
m.i26 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i27 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i28 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i29 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i30 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i31 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i32 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i33 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i34 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i35 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i36 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i37 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i38 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i39 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i40 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i41 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i42 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i43 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i44 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i45 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i46 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i47 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i48 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i49 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i50 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i51 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i52 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i53 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i54 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i55 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i56 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i57 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i58 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i59 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i60 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i61 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i62 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i63 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i64 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i65 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i66 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i67 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i68 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i69 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i70 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i71 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i72 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i73 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i74 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i75 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i76 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i77 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i78 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i79 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i80 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i81 = Var(within=Integers,bounds=(0,4),initialize=2)
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
m.x226 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,1),initialize=0)
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
m.x290 = Var(within=Reals,bounds=(0,None),initialize=2000)
m.x291 = Var(within=Reals,bounds=(0,None),initialize=2000)
m.x292 = Var(within=Reals,bounds=(0,None),initialize=2000)
m.x293 = Var(within=Reals,bounds=(0,None),initialize=2000)
m.x294 = Var(within=Reals,bounds=(0,None),initialize=2000)
m.x295 = Var(within=Reals,bounds=(0,None),initialize=2000)
m.x296 = Var(within=Reals,bounds=(0,None),initialize=2000)
m.x297 = Var(within=Reals,bounds=(0,None),initialize=2000)
m.x298 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x299 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x300 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x301 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x302 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x303 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x304 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x305 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x306 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x307 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x309 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x311 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x312 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x313 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x314 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x315 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x316 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x317 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x318 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x319 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x320 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x321 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x322 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x323 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x324 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x325 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x326 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x327 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x328 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x329 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13 + m.x14
                        + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20 + m.x21 + m.x22 + m.x23 + m.x24 + m.x25
                        + 10*m.x226 + 10*m.x227 + 10*m.x228 + 10*m.x229 + 10*m.x230 + 10*m.x231 + 10*m.x232 + 10*m.x233
                       , sense=minimize)

m.c2 = Constraint(expr=   m.i26 + m.i34 + m.i42 + m.i50 + m.i58 + m.i66 + m.i74 <= 4)

m.c3 = Constraint(expr=   m.i27 + m.i35 + m.i43 + m.i51 + m.i59 + m.i67 + m.i75 <= 4)

m.c4 = Constraint(expr=   m.i28 + m.i36 + m.i44 + m.i52 + m.i60 + m.i68 + m.i76 <= 4)

m.c5 = Constraint(expr=   m.i29 + m.i37 + m.i45 + m.i53 + m.i61 + m.i69 + m.i77 <= 4)

m.c6 = Constraint(expr=   m.i30 + m.i38 + m.i46 + m.i54 + m.i62 + m.i70 + m.i78 <= 4)

m.c7 = Constraint(expr=   m.i31 + m.i39 + m.i47 + m.i55 + m.i63 + m.i71 + m.i79 <= 4)

m.c8 = Constraint(expr=   m.i32 + m.i40 + m.i48 + m.i56 + m.i64 + m.i72 + m.i80 <= 4)

m.c9 = Constraint(expr=   m.i33 + m.i41 + m.i49 + m.i57 + m.i65 + m.i73 + m.i81 <= 4)

m.c10 = Constraint(expr=   m.x2 - 0.1287*m.x298 + 0.1287*m.x322 >= 0)

m.c11 = Constraint(expr=   m.x3 - 0.19305*m.x299 + 0.19305*m.x322 >= 0)

m.c12 = Constraint(expr=   m.x4 - 0.1287*m.x300 + 0.1287*m.x322 >= 0)

m.c13 = Constraint(expr=   m.x5 - 0.1287*m.x301 + 0.1287*m.x323 >= 0)

m.c14 = Constraint(expr=   m.x6 - 0.19305*m.x302 + 0.19305*m.x323 >= 0)

m.c15 = Constraint(expr=   m.x7 - 0.1287*m.x303 + 0.1287*m.x323 >= 0)

m.c16 = Constraint(expr=   m.x8 - 0.1287*m.x304 + 0.1287*m.x324 >= 0)

m.c17 = Constraint(expr=   m.x9 - 0.19305*m.x305 + 0.19305*m.x324 >= 0)

m.c18 = Constraint(expr=   m.x10 - 0.1287*m.x306 + 0.1287*m.x324 >= 0)

m.c19 = Constraint(expr=   m.x11 - 0.1725*m.x307 + 0.1725*m.x325 >= 0)

m.c20 = Constraint(expr=   m.x12 - 0.22815*m.x308 + 0.22815*m.x325 >= 0)

m.c21 = Constraint(expr=   m.x13 - 0.1521*m.x309 + 0.1521*m.x325 >= 0)

m.c22 = Constraint(expr=   m.x14 - 0.1725*m.x310 + 0.1725*m.x326 >= 0)

m.c23 = Constraint(expr=   m.x15 - 0.22815*m.x311 + 0.22815*m.x326 >= 0)

m.c24 = Constraint(expr=   m.x16 - 0.1521*m.x312 + 0.1521*m.x326 >= 0)

m.c25 = Constraint(expr=   m.x17 - 0.1521*m.x313 + 0.1521*m.x327 >= 0)

m.c26 = Constraint(expr=   m.x18 - 0.19305*m.x314 + 0.19305*m.x327 >= 0)

m.c27 = Constraint(expr=   m.x19 - 0.1521*m.x315 + 0.1521*m.x327 >= 0)

m.c28 = Constraint(expr=   m.x20 - 0.1521*m.x316 + 0.1521*m.x328 >= 0)

m.c29 = Constraint(expr=   m.x21 - 0.19305*m.x317 + 0.19305*m.x328 >= 0)

m.c30 = Constraint(expr=   m.x22 - 0.1521*m.x318 + 0.1521*m.x328 >= 0)

m.c31 = Constraint(expr=   m.x23 - 0.1521*m.x319 + 0.1521*m.x329 >= 0)

m.c32 = Constraint(expr=   m.x24 - 0.19305*m.x320 + 0.19305*m.x329 >= 0)

m.c33 = Constraint(expr=   m.x25 - 0.1521*m.x321 + 0.1521*m.x329 >= 0)

m.c34 = Constraint(expr=   m.b234 + m.b242 + m.b250 + m.b258 + m.b266 + m.b274 + m.b282 <= 2)

m.c35 = Constraint(expr=   m.b235 + m.b243 + m.b251 + m.b259 + m.b267 + m.b275 + m.b283 <= 2)

m.c36 = Constraint(expr=   m.b236 + m.b244 + m.b252 + m.b260 + m.b268 + m.b276 + m.b284 <= 2)

m.c37 = Constraint(expr=   m.b237 + m.b245 + m.b253 + m.b261 + m.b269 + m.b277 + m.b285 <= 2)

m.c38 = Constraint(expr=   m.b238 + m.b246 + m.b254 + m.b262 + m.b270 + m.b278 + m.b286 <= 2)

m.c39 = Constraint(expr=   m.b239 + m.b247 + m.b255 + m.b263 + m.b271 + m.b279 + m.b287 <= 2)

m.c40 = Constraint(expr=   m.b240 + m.b248 + m.b256 + m.b264 + m.b272 + m.b280 + m.b288 <= 2)

m.c41 = Constraint(expr=   m.b241 + m.b249 + m.b257 + m.b265 + m.b273 + m.b281 + m.b289 <= 2)

m.c42 = Constraint(expr=   m.b234 + m.b250 <= 1)

m.c43 = Constraint(expr=   m.b234 + m.b258 <= 1)

m.c44 = Constraint(expr=   m.b234 + m.b266 <= 1)

m.c45 = Constraint(expr=   m.b242 + m.b250 <= 1)

m.c46 = Constraint(expr=   m.b242 + m.b258 <= 1)

m.c47 = Constraint(expr=   m.b242 + m.b266 <= 1)

m.c48 = Constraint(expr=   m.b250 + m.b266 <= 1)

m.c49 = Constraint(expr=   m.b250 + m.b274 <= 1)

m.c50 = Constraint(expr=   m.b250 + m.b282 <= 1)

m.c51 = Constraint(expr=   m.b258 + m.b266 <= 1)

m.c52 = Constraint(expr=   m.b258 + m.b274 <= 1)

m.c53 = Constraint(expr=   m.b258 + m.b282 <= 1)

m.c54 = Constraint(expr=   m.b266 + m.b274 <= 1)

m.c55 = Constraint(expr=   m.b266 + m.b282 <= 1)

m.c56 = Constraint(expr=   m.b235 + m.b251 <= 1)

m.c57 = Constraint(expr=   m.b235 + m.b259 <= 1)

m.c58 = Constraint(expr=   m.b235 + m.b267 <= 1)

m.c59 = Constraint(expr=   m.b243 + m.b251 <= 1)

m.c60 = Constraint(expr=   m.b243 + m.b259 <= 1)

m.c61 = Constraint(expr=   m.b243 + m.b267 <= 1)

m.c62 = Constraint(expr=   m.b251 + m.b267 <= 1)

m.c63 = Constraint(expr=   m.b251 + m.b275 <= 1)

m.c64 = Constraint(expr=   m.b251 + m.b283 <= 1)

m.c65 = Constraint(expr=   m.b259 + m.b267 <= 1)

m.c66 = Constraint(expr=   m.b259 + m.b275 <= 1)

m.c67 = Constraint(expr=   m.b259 + m.b283 <= 1)

m.c68 = Constraint(expr=   m.b267 + m.b275 <= 1)

m.c69 = Constraint(expr=   m.b267 + m.b283 <= 1)

m.c70 = Constraint(expr=   m.b236 + m.b252 <= 1)

m.c71 = Constraint(expr=   m.b236 + m.b260 <= 1)

m.c72 = Constraint(expr=   m.b236 + m.b268 <= 1)

m.c73 = Constraint(expr=   m.b244 + m.b252 <= 1)

m.c74 = Constraint(expr=   m.b244 + m.b260 <= 1)

m.c75 = Constraint(expr=   m.b244 + m.b268 <= 1)

m.c76 = Constraint(expr=   m.b252 + m.b268 <= 1)

m.c77 = Constraint(expr=   m.b252 + m.b276 <= 1)

m.c78 = Constraint(expr=   m.b252 + m.b284 <= 1)

m.c79 = Constraint(expr=   m.b260 + m.b268 <= 1)

m.c80 = Constraint(expr=   m.b260 + m.b276 <= 1)

m.c81 = Constraint(expr=   m.b260 + m.b284 <= 1)

m.c82 = Constraint(expr=   m.b268 + m.b276 <= 1)

m.c83 = Constraint(expr=   m.b268 + m.b284 <= 1)

m.c84 = Constraint(expr=   m.b237 + m.b253 <= 1)

m.c85 = Constraint(expr=   m.b237 + m.b261 <= 1)

m.c86 = Constraint(expr=   m.b237 + m.b269 <= 1)

m.c87 = Constraint(expr=   m.b245 + m.b253 <= 1)

m.c88 = Constraint(expr=   m.b245 + m.b261 <= 1)

m.c89 = Constraint(expr=   m.b245 + m.b269 <= 1)

m.c90 = Constraint(expr=   m.b253 + m.b269 <= 1)

m.c91 = Constraint(expr=   m.b253 + m.b277 <= 1)

m.c92 = Constraint(expr=   m.b253 + m.b285 <= 1)

m.c93 = Constraint(expr=   m.b261 + m.b269 <= 1)

m.c94 = Constraint(expr=   m.b261 + m.b277 <= 1)

m.c95 = Constraint(expr=   m.b261 + m.b285 <= 1)

m.c96 = Constraint(expr=   m.b269 + m.b277 <= 1)

m.c97 = Constraint(expr=   m.b269 + m.b285 <= 1)

m.c98 = Constraint(expr=   m.b238 + m.b254 <= 1)

m.c99 = Constraint(expr=   m.b238 + m.b262 <= 1)

m.c100 = Constraint(expr=   m.b238 + m.b270 <= 1)

m.c101 = Constraint(expr=   m.b246 + m.b254 <= 1)

m.c102 = Constraint(expr=   m.b246 + m.b262 <= 1)

m.c103 = Constraint(expr=   m.b246 + m.b270 <= 1)

m.c104 = Constraint(expr=   m.b254 + m.b270 <= 1)

m.c105 = Constraint(expr=   m.b254 + m.b278 <= 1)

m.c106 = Constraint(expr=   m.b254 + m.b286 <= 1)

m.c107 = Constraint(expr=   m.b262 + m.b270 <= 1)

m.c108 = Constraint(expr=   m.b262 + m.b278 <= 1)

m.c109 = Constraint(expr=   m.b262 + m.b286 <= 1)

m.c110 = Constraint(expr=   m.b270 + m.b278 <= 1)

m.c111 = Constraint(expr=   m.b270 + m.b286 <= 1)

m.c112 = Constraint(expr=   m.b239 + m.b255 <= 1)

m.c113 = Constraint(expr=   m.b239 + m.b263 <= 1)

m.c114 = Constraint(expr=   m.b239 + m.b271 <= 1)

m.c115 = Constraint(expr=   m.b247 + m.b255 <= 1)

m.c116 = Constraint(expr=   m.b247 + m.b263 <= 1)

m.c117 = Constraint(expr=   m.b247 + m.b271 <= 1)

m.c118 = Constraint(expr=   m.b255 + m.b271 <= 1)

m.c119 = Constraint(expr=   m.b255 + m.b279 <= 1)

m.c120 = Constraint(expr=   m.b255 + m.b287 <= 1)

m.c121 = Constraint(expr=   m.b263 + m.b271 <= 1)

m.c122 = Constraint(expr=   m.b263 + m.b279 <= 1)

m.c123 = Constraint(expr=   m.b263 + m.b287 <= 1)

m.c124 = Constraint(expr=   m.b271 + m.b279 <= 1)

m.c125 = Constraint(expr=   m.b271 + m.b287 <= 1)

m.c126 = Constraint(expr=   m.b240 + m.b256 <= 1)

m.c127 = Constraint(expr=   m.b240 + m.b264 <= 1)

m.c128 = Constraint(expr=   m.b240 + m.b272 <= 1)

m.c129 = Constraint(expr=   m.b248 + m.b256 <= 1)

m.c130 = Constraint(expr=   m.b248 + m.b264 <= 1)

m.c131 = Constraint(expr=   m.b248 + m.b272 <= 1)

m.c132 = Constraint(expr=   m.b256 + m.b272 <= 1)

m.c133 = Constraint(expr=   m.b256 + m.b280 <= 1)

m.c134 = Constraint(expr=   m.b256 + m.b288 <= 1)

m.c135 = Constraint(expr=   m.b264 + m.b272 <= 1)

m.c136 = Constraint(expr=   m.b264 + m.b280 <= 1)

m.c137 = Constraint(expr=   m.b264 + m.b288 <= 1)

m.c138 = Constraint(expr=   m.b272 + m.b280 <= 1)

m.c139 = Constraint(expr=   m.b272 + m.b288 <= 1)

m.c140 = Constraint(expr=   m.b241 + m.b257 <= 1)

m.c141 = Constraint(expr=   m.b241 + m.b265 <= 1)

m.c142 = Constraint(expr=   m.b241 + m.b273 <= 1)

m.c143 = Constraint(expr=   m.b249 + m.b257 <= 1)

m.c144 = Constraint(expr=   m.b249 + m.b265 <= 1)

m.c145 = Constraint(expr=   m.b249 + m.b273 <= 1)

m.c146 = Constraint(expr=   m.b257 + m.b273 <= 1)

m.c147 = Constraint(expr=   m.b257 + m.b281 <= 1)

m.c148 = Constraint(expr=   m.b257 + m.b289 <= 1)

m.c149 = Constraint(expr=   m.b265 + m.b273 <= 1)

m.c150 = Constraint(expr=   m.b265 + m.b281 <= 1)

m.c151 = Constraint(expr=   m.b265 + m.b289 <= 1)

m.c152 = Constraint(expr=   m.b273 + m.b281 <= 1)

m.c153 = Constraint(expr=   m.b273 + m.b289 <= 1)

m.c154 = Constraint(expr=   m.b234 + m.b242 + m.b250 + m.b258 + m.b266 + m.b274 + m.b282 <= 0)

m.c155 = Constraint(expr=   m.b251 + m.b259 + m.b267 + m.b283 <= 0)

m.c156 = Constraint(expr=   m.b252 + m.b260 + m.b268 + m.b284 <= 0)

m.c157 = Constraint(expr=   m.b269 + m.b285 <= 0)

m.c158 = Constraint(expr=   m.b238 + m.b246 + m.b270 + m.b278 + m.b286 <= 0)

m.c159 = Constraint(expr=   m.b239 + m.b247 + m.b255 + m.b263 + m.b279 <= 0)

m.c160 = Constraint(expr=   m.b240 + m.b248 + m.b256 + m.b264 + m.b280 <= 0)

m.c161 = Constraint(expr=   m.b241 + m.b249 + m.b257 + m.b265 + m.b281 <= 0)

m.c162 = Constraint(expr= - 330*m.i26 - 260*m.i34 - 480*m.i42 - 440*m.i50 - 711*m.i58 - 350*m.i66 - 300*m.i74
                          + 1000*m.b82 + 1100*m.b106 + 1200*m.b130 + 1300*m.b154 + 1400*m.b178 + 1500*m.b202
                          - 200*m.x226 <= 0)

m.c163 = Constraint(expr= - 330*m.i26 - 260*m.i34 - 480*m.i42 - 440*m.i50 - 711*m.i58 - 350*m.i66 - 300*m.i74
                          + 1000*m.b90 + 1100*m.b114 + 1200*m.b138 + 1300*m.b162 + 1400*m.b186 + 1500*m.b210
                          - 200*m.x226 <= 0)

m.c164 = Constraint(expr= - 330*m.i26 - 260*m.i34 - 480*m.i42 - 440*m.i50 - 711*m.i58 - 350*m.i66 - 300*m.i74
                          + 1000*m.b98 + 1100*m.b122 + 1200*m.b146 + 1300*m.b170 + 1400*m.b194 + 1500*m.b218
                          - 200*m.x226 <= 0)

m.c165 = Constraint(expr= - 330*m.i27 - 260*m.i35 - 480*m.i43 - 440*m.i51 - 711*m.i59 - 350*m.i67 - 300*m.i75
                          + 1000*m.b83 + 1100*m.b107 + 1200*m.b131 + 1300*m.b155 + 1400*m.b179 + 1500*m.b203
                          - 200*m.x227 <= 0)

m.c166 = Constraint(expr= - 330*m.i27 - 260*m.i35 - 480*m.i43 - 440*m.i51 - 711*m.i59 - 350*m.i67 - 300*m.i75
                          + 1000*m.b91 + 1100*m.b115 + 1200*m.b139 + 1300*m.b163 + 1400*m.b187 + 1500*m.b211
                          - 200*m.x227 <= 0)

m.c167 = Constraint(expr= - 330*m.i27 - 260*m.i35 - 480*m.i43 - 440*m.i51 - 711*m.i59 - 350*m.i67 - 300*m.i75
                          + 1000*m.b99 + 1100*m.b123 + 1200*m.b147 + 1300*m.b171 + 1400*m.b195 + 1500*m.b219
                          - 200*m.x227 <= 0)

m.c168 = Constraint(expr= - 330*m.i28 - 260*m.i36 - 480*m.i44 - 440*m.i52 - 711*m.i60 - 350*m.i68 - 300*m.i76
                          + 1000*m.b84 + 1100*m.b108 + 1200*m.b132 + 1300*m.b156 + 1400*m.b180 + 1500*m.b204
                          - 200*m.x228 <= 0)

m.c169 = Constraint(expr= - 330*m.i28 - 260*m.i36 - 480*m.i44 - 440*m.i52 - 711*m.i60 - 350*m.i68 - 300*m.i76
                          + 1000*m.b92 + 1100*m.b116 + 1200*m.b140 + 1300*m.b164 + 1400*m.b188 + 1500*m.b212
                          - 200*m.x228 <= 0)

m.c170 = Constraint(expr= - 330*m.i28 - 260*m.i36 - 480*m.i44 - 440*m.i52 - 711*m.i60 - 350*m.i68 - 300*m.i76
                          + 1000*m.b100 + 1100*m.b124 + 1200*m.b148 + 1300*m.b172 + 1400*m.b196 + 1500*m.b220
                          - 200*m.x228 <= 0)

m.c171 = Constraint(expr= - 330*m.i29 - 260*m.i37 - 480*m.i45 - 440*m.i53 - 711*m.i61 - 350*m.i69 - 300*m.i77
                          + 1000*m.b85 + 1100*m.b109 + 1200*m.b133 + 1300*m.b157 + 1400*m.b181 + 1500*m.b205
                          - 200*m.x229 <= 0)

m.c172 = Constraint(expr= - 330*m.i29 - 260*m.i37 - 480*m.i45 - 440*m.i53 - 711*m.i61 - 350*m.i69 - 300*m.i77
                          + 1000*m.b93 + 1100*m.b117 + 1200*m.b141 + 1300*m.b165 + 1400*m.b189 + 1500*m.b213
                          - 200*m.x229 <= 0)

m.c173 = Constraint(expr= - 330*m.i29 - 260*m.i37 - 480*m.i45 - 440*m.i53 - 711*m.i61 - 350*m.i69 - 300*m.i77
                          + 1000*m.b101 + 1100*m.b125 + 1200*m.b149 + 1300*m.b173 + 1400*m.b197 + 1500*m.b221
                          - 200*m.x229 <= 0)

m.c174 = Constraint(expr= - 330*m.i30 - 260*m.i38 - 480*m.i46 - 440*m.i54 - 711*m.i62 - 350*m.i70 - 300*m.i78
                          + 1000*m.b86 + 1100*m.b110 + 1200*m.b134 + 1300*m.b158 + 1400*m.b182 + 1500*m.b206
                          - 200*m.x230 <= 0)

m.c175 = Constraint(expr= - 330*m.i30 - 260*m.i38 - 480*m.i46 - 440*m.i54 - 711*m.i62 - 350*m.i70 - 300*m.i78
                          + 1000*m.b94 + 1100*m.b118 + 1200*m.b142 + 1300*m.b166 + 1400*m.b190 + 1500*m.b214
                          - 200*m.x230 <= 0)

m.c176 = Constraint(expr= - 330*m.i30 - 260*m.i38 - 480*m.i46 - 440*m.i54 - 711*m.i62 - 350*m.i70 - 300*m.i78
                          + 1000*m.b102 + 1100*m.b126 + 1200*m.b150 + 1300*m.b174 + 1400*m.b198 + 1500*m.b222
                          - 200*m.x230 <= 0)

m.c177 = Constraint(expr= - 330*m.i31 - 260*m.i39 - 480*m.i47 - 440*m.i55 - 711*m.i63 - 350*m.i71 - 300*m.i79
                          + 1000*m.b87 + 1100*m.b111 + 1200*m.b135 + 1300*m.b159 + 1400*m.b183 + 1500*m.b207
                          - 200*m.x231 <= 0)

m.c178 = Constraint(expr= - 330*m.i31 - 260*m.i39 - 480*m.i47 - 440*m.i55 - 711*m.i63 - 350*m.i71 - 300*m.i79
                          + 1000*m.b95 + 1100*m.b119 + 1200*m.b143 + 1300*m.b167 + 1400*m.b191 + 1500*m.b215
                          - 200*m.x231 <= 0)

m.c179 = Constraint(expr= - 330*m.i31 - 260*m.i39 - 480*m.i47 - 440*m.i55 - 711*m.i63 - 350*m.i71 - 300*m.i79
                          + 1000*m.b103 + 1100*m.b127 + 1200*m.b151 + 1300*m.b175 + 1400*m.b199 + 1500*m.b223
                          - 200*m.x231 <= 0)

m.c180 = Constraint(expr= - 330*m.i32 - 260*m.i40 - 480*m.i48 - 440*m.i56 - 711*m.i64 - 350*m.i72 - 300*m.i80
                          + 1000*m.b88 + 1100*m.b112 + 1200*m.b136 + 1300*m.b160 + 1400*m.b184 + 1500*m.b208
                          - 200*m.x232 <= 0)

m.c181 = Constraint(expr= - 330*m.i32 - 260*m.i40 - 480*m.i48 - 440*m.i56 - 711*m.i64 - 350*m.i72 - 300*m.i80
                          + 1000*m.b96 + 1100*m.b120 + 1200*m.b144 + 1300*m.b168 + 1400*m.b192 + 1500*m.b216
                          - 200*m.x232 <= 0)

m.c182 = Constraint(expr= - 330*m.i32 - 260*m.i40 - 480*m.i48 - 440*m.i56 - 711*m.i64 - 350*m.i72 - 300*m.i80
                          + 1000*m.b104 + 1100*m.b128 + 1200*m.b152 + 1300*m.b176 + 1400*m.b200 + 1500*m.b224
                          - 200*m.x232 <= 0)

m.c183 = Constraint(expr= - 330*m.i33 - 260*m.i41 - 480*m.i49 - 440*m.i57 - 711*m.i65 - 350*m.i73 - 300*m.i81
                          + 1000*m.b89 + 1100*m.b113 + 1200*m.b137 + 1300*m.b161 + 1400*m.b185 + 1500*m.b209
                          - 200*m.x233 <= 0)

m.c184 = Constraint(expr= - 330*m.i33 - 260*m.i41 - 480*m.i49 - 440*m.i57 - 711*m.i65 - 350*m.i73 - 300*m.i81
                          + 1000*m.b97 + 1100*m.b121 + 1200*m.b145 + 1300*m.b169 + 1400*m.b193 + 1500*m.b217
                          - 200*m.x233 <= 0)

m.c185 = Constraint(expr= - 330*m.i33 - 260*m.i41 - 480*m.i49 - 440*m.i57 - 711*m.i65 - 350*m.i73 - 300*m.i81
                          + 1000*m.b105 + 1100*m.b129 + 1200*m.b153 + 1300*m.b177 + 1400*m.b201 + 1500*m.b225
                          - 200*m.x233 <= 0)

m.c186 = Constraint(expr= - 330*m.i26 - 260*m.i34 - 480*m.i42 - 440*m.i50 - 711*m.i58 - 350*m.i66 - 300*m.i74
                          + 1000*m.b82 + 1100*m.b106 + 1200*m.b130 + 1300*m.b154 + 1400*m.b178 + 1500*m.b202 - 20*m.x226
                          >= 0)

m.c187 = Constraint(expr= - 330*m.i26 - 260*m.i34 - 480*m.i42 - 440*m.i50 - 711*m.i58 - 350*m.i66 - 300*m.i74
                          + 1000*m.b90 + 1100*m.b114 + 1200*m.b138 + 1300*m.b162 + 1400*m.b186 + 1500*m.b210 - 20*m.x226
                          >= 0)

m.c188 = Constraint(expr= - 330*m.i26 - 260*m.i34 - 480*m.i42 - 440*m.i50 - 711*m.i58 - 350*m.i66 - 300*m.i74
                          + 1000*m.b98 + 1100*m.b122 + 1200*m.b146 + 1300*m.b170 + 1400*m.b194 + 1500*m.b218 - 20*m.x226
                          >= 0)

m.c189 = Constraint(expr= - 330*m.i27 - 260*m.i35 - 480*m.i43 - 440*m.i51 - 711*m.i59 - 350*m.i67 - 300*m.i75
                          + 1000*m.b83 + 1100*m.b107 + 1200*m.b131 + 1300*m.b155 + 1400*m.b179 + 1500*m.b203 - 20*m.x227
                          >= 0)

m.c190 = Constraint(expr= - 330*m.i27 - 260*m.i35 - 480*m.i43 - 440*m.i51 - 711*m.i59 - 350*m.i67 - 300*m.i75
                          + 1000*m.b91 + 1100*m.b115 + 1200*m.b139 + 1300*m.b163 + 1400*m.b187 + 1500*m.b211 - 20*m.x227
                          >= 0)

m.c191 = Constraint(expr= - 330*m.i27 - 260*m.i35 - 480*m.i43 - 440*m.i51 - 711*m.i59 - 350*m.i67 - 300*m.i75
                          + 1000*m.b99 + 1100*m.b123 + 1200*m.b147 + 1300*m.b171 + 1400*m.b195 + 1500*m.b219 - 20*m.x227
                          >= 0)

m.c192 = Constraint(expr= - 330*m.i28 - 260*m.i36 - 480*m.i44 - 440*m.i52 - 711*m.i60 - 350*m.i68 - 300*m.i76
                          + 1000*m.b84 + 1100*m.b108 + 1200*m.b132 + 1300*m.b156 + 1400*m.b180 + 1500*m.b204 - 20*m.x228
                          >= 0)

m.c193 = Constraint(expr= - 330*m.i28 - 260*m.i36 - 480*m.i44 - 440*m.i52 - 711*m.i60 - 350*m.i68 - 300*m.i76
                          + 1000*m.b92 + 1100*m.b116 + 1200*m.b140 + 1300*m.b164 + 1400*m.b188 + 1500*m.b212 - 20*m.x228
                          >= 0)

m.c194 = Constraint(expr= - 330*m.i28 - 260*m.i36 - 480*m.i44 - 440*m.i52 - 711*m.i60 - 350*m.i68 - 300*m.i76
                          + 1000*m.b100 + 1100*m.b124 + 1200*m.b148 + 1300*m.b172 + 1400*m.b196 + 1500*m.b220
                          - 20*m.x228 >= 0)

m.c195 = Constraint(expr= - 330*m.i29 - 260*m.i37 - 480*m.i45 - 440*m.i53 - 711*m.i61 - 350*m.i69 - 300*m.i77
                          + 1000*m.b85 + 1100*m.b109 + 1200*m.b133 + 1300*m.b157 + 1400*m.b181 + 1500*m.b205 - 20*m.x229
                          >= 0)

m.c196 = Constraint(expr= - 330*m.i29 - 260*m.i37 - 480*m.i45 - 440*m.i53 - 711*m.i61 - 350*m.i69 - 300*m.i77
                          + 1000*m.b93 + 1100*m.b117 + 1200*m.b141 + 1300*m.b165 + 1400*m.b189 + 1500*m.b213 - 20*m.x229
                          >= 0)

m.c197 = Constraint(expr= - 330*m.i29 - 260*m.i37 - 480*m.i45 - 440*m.i53 - 711*m.i61 - 350*m.i69 - 300*m.i77
                          + 1000*m.b101 + 1100*m.b125 + 1200*m.b149 + 1300*m.b173 + 1400*m.b197 + 1500*m.b221
                          - 20*m.x229 >= 0)

m.c198 = Constraint(expr= - 330*m.i30 - 260*m.i38 - 480*m.i46 - 440*m.i54 - 711*m.i62 - 350*m.i70 - 300*m.i78
                          + 1000*m.b86 + 1100*m.b110 + 1200*m.b134 + 1300*m.b158 + 1400*m.b182 + 1500*m.b206 - 20*m.x230
                          >= 0)

m.c199 = Constraint(expr= - 330*m.i30 - 260*m.i38 - 480*m.i46 - 440*m.i54 - 711*m.i62 - 350*m.i70 - 300*m.i78
                          + 1000*m.b94 + 1100*m.b118 + 1200*m.b142 + 1300*m.b166 + 1400*m.b190 + 1500*m.b214 - 20*m.x230
                          >= 0)

m.c200 = Constraint(expr= - 330*m.i30 - 260*m.i38 - 480*m.i46 - 440*m.i54 - 711*m.i62 - 350*m.i70 - 300*m.i78
                          + 1000*m.b102 + 1100*m.b126 + 1200*m.b150 + 1300*m.b174 + 1400*m.b198 + 1500*m.b222
                          - 20*m.x230 >= 0)

m.c201 = Constraint(expr= - 330*m.i31 - 260*m.i39 - 480*m.i47 - 440*m.i55 - 711*m.i63 - 350*m.i71 - 300*m.i79
                          + 1000*m.b87 + 1100*m.b111 + 1200*m.b135 + 1300*m.b159 + 1400*m.b183 + 1500*m.b207 - 20*m.x231
                          >= 0)

m.c202 = Constraint(expr= - 330*m.i31 - 260*m.i39 - 480*m.i47 - 440*m.i55 - 711*m.i63 - 350*m.i71 - 300*m.i79
                          + 1000*m.b95 + 1100*m.b119 + 1200*m.b143 + 1300*m.b167 + 1400*m.b191 + 1500*m.b215 - 20*m.x231
                          >= 0)

m.c203 = Constraint(expr= - 330*m.i31 - 260*m.i39 - 480*m.i47 - 440*m.i55 - 711*m.i63 - 350*m.i71 - 300*m.i79
                          + 1000*m.b103 + 1100*m.b127 + 1200*m.b151 + 1300*m.b175 + 1400*m.b199 + 1500*m.b223
                          - 20*m.x231 >= 0)

m.c204 = Constraint(expr= - 330*m.i32 - 260*m.i40 - 480*m.i48 - 440*m.i56 - 711*m.i64 - 350*m.i72 - 300*m.i80
                          + 1000*m.b88 + 1100*m.b112 + 1200*m.b136 + 1300*m.b160 + 1400*m.b184 + 1500*m.b208 - 20*m.x232
                          >= 0)

m.c205 = Constraint(expr= - 330*m.i32 - 260*m.i40 - 480*m.i48 - 440*m.i56 - 711*m.i64 - 350*m.i72 - 300*m.i80
                          + 1000*m.b96 + 1100*m.b120 + 1200*m.b144 + 1300*m.b168 + 1400*m.b192 + 1500*m.b216 - 20*m.x232
                          >= 0)

m.c206 = Constraint(expr= - 330*m.i32 - 260*m.i40 - 480*m.i48 - 440*m.i56 - 711*m.i64 - 350*m.i72 - 300*m.i80
                          + 1000*m.b104 + 1100*m.b128 + 1200*m.b152 + 1300*m.b176 + 1400*m.b200 + 1500*m.b224
                          - 20*m.x232 >= 0)

m.c207 = Constraint(expr= - 330*m.i33 - 260*m.i41 - 480*m.i49 - 440*m.i57 - 711*m.i65 - 350*m.i73 - 300*m.i81
                          + 1000*m.b89 + 1100*m.b113 + 1200*m.b137 + 1300*m.b161 + 1400*m.b185 + 1500*m.b209 - 20*m.x233
                          >= 0)

m.c208 = Constraint(expr= - 330*m.i33 - 260*m.i41 - 480*m.i49 - 440*m.i57 - 711*m.i65 - 350*m.i73 - 300*m.i81
                          + 1000*m.b97 + 1100*m.b121 + 1200*m.b145 + 1300*m.b169 + 1400*m.b193 + 1500*m.b217 - 20*m.x233
                          >= 0)

m.c209 = Constraint(expr= - 330*m.i33 - 260*m.i41 - 480*m.i49 - 440*m.i57 - 711*m.i65 - 350*m.i73 - 300*m.i81
                          + 1000*m.b105 + 1100*m.b129 + 1200*m.b153 + 1300*m.b177 + 1400*m.b201 + 1500*m.b225
                          - 20*m.x233 >= 0)

m.c210 = Constraint(expr=   m.b82 + m.b106 + m.b130 + m.b154 + m.b178 + m.b202 - m.b234 - m.b242 - m.b250 - m.b258
                          - m.b266 - m.b274 - m.b282 <= 0)

m.c211 = Constraint(expr=   m.b90 + m.b114 + m.b138 + m.b162 + m.b186 + m.b210 - m.b234 - m.b242 - m.b250 - m.b258
                          - m.b266 - m.b274 - m.b282 <= 0)

m.c212 = Constraint(expr=   m.b98 + m.b122 + m.b146 + m.b170 + m.b194 + m.b218 - m.b234 - m.b242 - m.b250 - m.b258
                          - m.b266 - m.b274 - m.b282 <= 0)

m.c213 = Constraint(expr=   m.b83 + m.b107 + m.b131 + m.b155 + m.b179 + m.b203 - m.b235 - m.b243 - m.b251 - m.b259
                          - m.b267 - m.b275 - m.b283 <= 0)

m.c214 = Constraint(expr=   m.b91 + m.b115 + m.b139 + m.b163 + m.b187 + m.b211 - m.b235 - m.b243 - m.b251 - m.b259
                          - m.b267 - m.b275 - m.b283 <= 0)

m.c215 = Constraint(expr=   m.b99 + m.b123 + m.b147 + m.b171 + m.b195 + m.b219 - m.b235 - m.b243 - m.b251 - m.b259
                          - m.b267 - m.b275 - m.b283 <= 0)

m.c216 = Constraint(expr=   m.b84 + m.b108 + m.b132 + m.b156 + m.b180 + m.b204 - m.b236 - m.b244 - m.b252 - m.b260
                          - m.b268 - m.b276 - m.b284 <= 0)

m.c217 = Constraint(expr=   m.b92 + m.b116 + m.b140 + m.b164 + m.b188 + m.b212 - m.b236 - m.b244 - m.b252 - m.b260
                          - m.b268 - m.b276 - m.b284 <= 0)

m.c218 = Constraint(expr=   m.b100 + m.b124 + m.b148 + m.b172 + m.b196 + m.b220 - m.b236 - m.b244 - m.b252 - m.b260
                          - m.b268 - m.b276 - m.b284 <= 0)

m.c219 = Constraint(expr=   m.b85 + m.b109 + m.b133 + m.b157 + m.b181 + m.b205 - m.b237 - m.b245 - m.b253 - m.b261
                          - m.b269 - m.b277 - m.b285 <= 0)

m.c220 = Constraint(expr=   m.b93 + m.b117 + m.b141 + m.b165 + m.b189 + m.b213 - m.b237 - m.b245 - m.b253 - m.b261
                          - m.b269 - m.b277 - m.b285 <= 0)

m.c221 = Constraint(expr=   m.b101 + m.b125 + m.b149 + m.b173 + m.b197 + m.b221 - m.b237 - m.b245 - m.b253 - m.b261
                          - m.b269 - m.b277 - m.b285 <= 0)

m.c222 = Constraint(expr=   m.b86 + m.b110 + m.b134 + m.b158 + m.b182 + m.b206 - m.b238 - m.b246 - m.b254 - m.b262
                          - m.b270 - m.b278 - m.b286 <= 0)

m.c223 = Constraint(expr=   m.b94 + m.b118 + m.b142 + m.b166 + m.b190 + m.b214 - m.b238 - m.b246 - m.b254 - m.b262
                          - m.b270 - m.b278 - m.b286 <= 0)

m.c224 = Constraint(expr=   m.b102 + m.b126 + m.b150 + m.b174 + m.b198 + m.b222 - m.b238 - m.b246 - m.b254 - m.b262
                          - m.b270 - m.b278 - m.b286 <= 0)

m.c225 = Constraint(expr=   m.b87 + m.b111 + m.b135 + m.b159 + m.b183 + m.b207 - m.b239 - m.b247 - m.b255 - m.b263
                          - m.b271 - m.b279 - m.b287 <= 0)

m.c226 = Constraint(expr=   m.b95 + m.b119 + m.b143 + m.b167 + m.b191 + m.b215 - m.b239 - m.b247 - m.b255 - m.b263
                          - m.b271 - m.b279 - m.b287 <= 0)

m.c227 = Constraint(expr=   m.b103 + m.b127 + m.b151 + m.b175 + m.b199 + m.b223 - m.b239 - m.b247 - m.b255 - m.b263
                          - m.b271 - m.b279 - m.b287 <= 0)

m.c228 = Constraint(expr=   m.b88 + m.b112 + m.b136 + m.b160 + m.b184 + m.b208 - m.b240 - m.b248 - m.b256 - m.b264
                          - m.b272 - m.b280 - m.b288 <= 0)

m.c229 = Constraint(expr=   m.b96 + m.b120 + m.b144 + m.b168 + m.b192 + m.b216 - m.b240 - m.b248 - m.b256 - m.b264
                          - m.b272 - m.b280 - m.b288 <= 0)

m.c230 = Constraint(expr=   m.b104 + m.b128 + m.b152 + m.b176 + m.b200 + m.b224 - m.b240 - m.b248 - m.b256 - m.b264
                          - m.b272 - m.b280 - m.b288 <= 0)

m.c231 = Constraint(expr=   m.b89 + m.b113 + m.b137 + m.b161 + m.b185 + m.b209 - m.b241 - m.b249 - m.b257 - m.b265
                          - m.b273 - m.b281 - m.b289 <= 0)

m.c232 = Constraint(expr=   m.b97 + m.b121 + m.b145 + m.b169 + m.b193 + m.b217 - m.b241 - m.b249 - m.b257 - m.b265
                          - m.b273 - m.b281 - m.b289 <= 0)

m.c233 = Constraint(expr=   m.b105 + m.b129 + m.b153 + m.b177 + m.b201 + m.b225 - m.b241 - m.b249 - m.b257 - m.b265
                          - m.b273 - m.b281 - m.b289 <= 0)

m.c234 = Constraint(expr=   m.b82 + m.b106 + m.b130 + m.b154 + m.b178 + m.b202 <= 1)

m.c235 = Constraint(expr=   m.b90 + m.b114 + m.b138 + m.b162 + m.b186 + m.b210 <= 1)

m.c236 = Constraint(expr=   m.b98 + m.b122 + m.b146 + m.b170 + m.b194 + m.b218 <= 1)

m.c237 = Constraint(expr=   m.b83 + m.b107 + m.b131 + m.b155 + m.b179 + m.b203 <= 1)

m.c238 = Constraint(expr=   m.b91 + m.b115 + m.b139 + m.b163 + m.b187 + m.b211 <= 1)

m.c239 = Constraint(expr=   m.b99 + m.b123 + m.b147 + m.b171 + m.b195 + m.b219 <= 1)

m.c240 = Constraint(expr=   m.b84 + m.b108 + m.b132 + m.b156 + m.b180 + m.b204 <= 1)

m.c241 = Constraint(expr=   m.b92 + m.b116 + m.b140 + m.b164 + m.b188 + m.b212 <= 1)

m.c242 = Constraint(expr=   m.b100 + m.b124 + m.b148 + m.b172 + m.b196 + m.b220 <= 1)

m.c243 = Constraint(expr=   m.b85 + m.b109 + m.b133 + m.b157 + m.b181 + m.b205 <= 1)

m.c244 = Constraint(expr=   m.b93 + m.b117 + m.b141 + m.b165 + m.b189 + m.b213 <= 1)

m.c245 = Constraint(expr=   m.b101 + m.b125 + m.b149 + m.b173 + m.b197 + m.b221 <= 1)

m.c246 = Constraint(expr=   m.b86 + m.b110 + m.b134 + m.b158 + m.b182 + m.b206 <= 1)

m.c247 = Constraint(expr=   m.b94 + m.b118 + m.b142 + m.b166 + m.b190 + m.b214 <= 1)

m.c248 = Constraint(expr=   m.b102 + m.b126 + m.b150 + m.b174 + m.b198 + m.b222 <= 1)

m.c249 = Constraint(expr=   m.b87 + m.b111 + m.b135 + m.b159 + m.b183 + m.b207 <= 1)

m.c250 = Constraint(expr=   m.b95 + m.b119 + m.b143 + m.b167 + m.b191 + m.b215 <= 1)

m.c251 = Constraint(expr=   m.b103 + m.b127 + m.b151 + m.b175 + m.b199 + m.b223 <= 1)

m.c252 = Constraint(expr=   m.b88 + m.b112 + m.b136 + m.b160 + m.b184 + m.b208 <= 1)

m.c253 = Constraint(expr=   m.b96 + m.b120 + m.b144 + m.b168 + m.b192 + m.b216 <= 1)

m.c254 = Constraint(expr=   m.b104 + m.b128 + m.b152 + m.b176 + m.b200 + m.b224 <= 1)

m.c255 = Constraint(expr=   m.b89 + m.b113 + m.b137 + m.b161 + m.b185 + m.b209 <= 1)

m.c256 = Constraint(expr=   m.b97 + m.b121 + m.b145 + m.b169 + m.b193 + m.b217 <= 1)

m.c257 = Constraint(expr=   m.b105 + m.b129 + m.b153 + m.b177 + m.b201 + m.b225 <= 1)

m.c258 = Constraint(expr=   m.b82 + m.b106 + m.b130 + m.b154 + m.b178 + m.b202 - m.x226 >= 0)

m.c259 = Constraint(expr=   m.b82 + m.b106 + m.b130 + m.b154 + m.b178 + m.b202 - m.x226 >= 0)

m.c260 = Constraint(expr=   m.b82 + m.b106 + m.b130 + m.b154 + m.b178 + m.b202 - m.x226 >= 0)

m.c261 = Constraint(expr=   m.b82 + m.b106 + m.b130 + m.b154 + m.b178 + m.b202 - m.x226 >= 0)

m.c262 = Constraint(expr=   m.b82 + m.b106 + m.b130 + m.b154 + m.b178 + m.b202 - m.x226 >= 0)

m.c263 = Constraint(expr=   m.b82 + m.b106 + m.b130 + m.b154 + m.b178 + m.b202 - m.x226 >= 0)

m.c264 = Constraint(expr=   m.b82 + m.b106 + m.b130 + m.b154 + m.b178 + m.b202 - m.x226 >= 0)

m.c265 = Constraint(expr=   m.b90 + m.b114 + m.b138 + m.b162 + m.b186 + m.b210 - m.x226 >= 0)

m.c266 = Constraint(expr=   m.b90 + m.b114 + m.b138 + m.b162 + m.b186 + m.b210 - m.x226 >= 0)

m.c267 = Constraint(expr=   m.b90 + m.b114 + m.b138 + m.b162 + m.b186 + m.b210 - m.x226 >= 0)

m.c268 = Constraint(expr=   m.b90 + m.b114 + m.b138 + m.b162 + m.b186 + m.b210 - m.x226 >= 0)

m.c269 = Constraint(expr=   m.b90 + m.b114 + m.b138 + m.b162 + m.b186 + m.b210 - m.x226 >= 0)

m.c270 = Constraint(expr=   m.b90 + m.b114 + m.b138 + m.b162 + m.b186 + m.b210 - m.x226 >= 0)

m.c271 = Constraint(expr=   m.b90 + m.b114 + m.b138 + m.b162 + m.b186 + m.b210 - m.x226 >= 0)

m.c272 = Constraint(expr=   m.b98 + m.b122 + m.b146 + m.b170 + m.b194 + m.b218 - m.x226 >= 0)

m.c273 = Constraint(expr=   m.b98 + m.b122 + m.b146 + m.b170 + m.b194 + m.b218 - m.x226 >= 0)

m.c274 = Constraint(expr=   m.b98 + m.b122 + m.b146 + m.b170 + m.b194 + m.b218 - m.x226 >= 0)

m.c275 = Constraint(expr=   m.b98 + m.b122 + m.b146 + m.b170 + m.b194 + m.b218 - m.x226 >= 0)

m.c276 = Constraint(expr=   m.b98 + m.b122 + m.b146 + m.b170 + m.b194 + m.b218 - m.x226 >= 0)

m.c277 = Constraint(expr=   m.b98 + m.b122 + m.b146 + m.b170 + m.b194 + m.b218 - m.x226 >= 0)

m.c278 = Constraint(expr=   m.b98 + m.b122 + m.b146 + m.b170 + m.b194 + m.b218 - m.x226 >= 0)

m.c279 = Constraint(expr=   m.b83 + m.b107 + m.b131 + m.b155 + m.b179 + m.b203 - m.x227 >= 0)

m.c280 = Constraint(expr=   m.b83 + m.b107 + m.b131 + m.b155 + m.b179 + m.b203 - m.x227 >= 0)

m.c281 = Constraint(expr=   m.b83 + m.b107 + m.b131 + m.b155 + m.b179 + m.b203 - m.x227 >= 0)

m.c282 = Constraint(expr=   m.b83 + m.b107 + m.b131 + m.b155 + m.b179 + m.b203 - m.x227 >= 0)

m.c283 = Constraint(expr=   m.b83 + m.b107 + m.b131 + m.b155 + m.b179 + m.b203 - m.x227 >= 0)

m.c284 = Constraint(expr=   m.b83 + m.b107 + m.b131 + m.b155 + m.b179 + m.b203 - m.x227 >= 0)

m.c285 = Constraint(expr=   m.b83 + m.b107 + m.b131 + m.b155 + m.b179 + m.b203 - m.x227 >= 0)

m.c286 = Constraint(expr=   m.b91 + m.b115 + m.b139 + m.b163 + m.b187 + m.b211 - m.x227 >= 0)

m.c287 = Constraint(expr=   m.b91 + m.b115 + m.b139 + m.b163 + m.b187 + m.b211 - m.x227 >= 0)

m.c288 = Constraint(expr=   m.b91 + m.b115 + m.b139 + m.b163 + m.b187 + m.b211 - m.x227 >= 0)

m.c289 = Constraint(expr=   m.b91 + m.b115 + m.b139 + m.b163 + m.b187 + m.b211 - m.x227 >= 0)

m.c290 = Constraint(expr=   m.b91 + m.b115 + m.b139 + m.b163 + m.b187 + m.b211 - m.x227 >= 0)

m.c291 = Constraint(expr=   m.b91 + m.b115 + m.b139 + m.b163 + m.b187 + m.b211 - m.x227 >= 0)

m.c292 = Constraint(expr=   m.b91 + m.b115 + m.b139 + m.b163 + m.b187 + m.b211 - m.x227 >= 0)

m.c293 = Constraint(expr=   m.b99 + m.b123 + m.b147 + m.b171 + m.b195 + m.b219 - m.x227 >= 0)

m.c294 = Constraint(expr=   m.b99 + m.b123 + m.b147 + m.b171 + m.b195 + m.b219 - m.x227 >= 0)

m.c295 = Constraint(expr=   m.b99 + m.b123 + m.b147 + m.b171 + m.b195 + m.b219 - m.x227 >= 0)

m.c296 = Constraint(expr=   m.b99 + m.b123 + m.b147 + m.b171 + m.b195 + m.b219 - m.x227 >= 0)

m.c297 = Constraint(expr=   m.b99 + m.b123 + m.b147 + m.b171 + m.b195 + m.b219 - m.x227 >= 0)

m.c298 = Constraint(expr=   m.b99 + m.b123 + m.b147 + m.b171 + m.b195 + m.b219 - m.x227 >= 0)

m.c299 = Constraint(expr=   m.b99 + m.b123 + m.b147 + m.b171 + m.b195 + m.b219 - m.x227 >= 0)

m.c300 = Constraint(expr=   m.b84 + m.b108 + m.b132 + m.b156 + m.b180 + m.b204 - m.x228 >= 0)

m.c301 = Constraint(expr=   m.b84 + m.b108 + m.b132 + m.b156 + m.b180 + m.b204 - m.x228 >= 0)

m.c302 = Constraint(expr=   m.b84 + m.b108 + m.b132 + m.b156 + m.b180 + m.b204 - m.x228 >= 0)

m.c303 = Constraint(expr=   m.b84 + m.b108 + m.b132 + m.b156 + m.b180 + m.b204 - m.x228 >= 0)

m.c304 = Constraint(expr=   m.b84 + m.b108 + m.b132 + m.b156 + m.b180 + m.b204 - m.x228 >= 0)

m.c305 = Constraint(expr=   m.b84 + m.b108 + m.b132 + m.b156 + m.b180 + m.b204 - m.x228 >= 0)

m.c306 = Constraint(expr=   m.b84 + m.b108 + m.b132 + m.b156 + m.b180 + m.b204 - m.x228 >= 0)

m.c307 = Constraint(expr=   m.b92 + m.b116 + m.b140 + m.b164 + m.b188 + m.b212 - m.x228 >= 0)

m.c308 = Constraint(expr=   m.b92 + m.b116 + m.b140 + m.b164 + m.b188 + m.b212 - m.x228 >= 0)

m.c309 = Constraint(expr=   m.b92 + m.b116 + m.b140 + m.b164 + m.b188 + m.b212 - m.x228 >= 0)

m.c310 = Constraint(expr=   m.b92 + m.b116 + m.b140 + m.b164 + m.b188 + m.b212 - m.x228 >= 0)

m.c311 = Constraint(expr=   m.b92 + m.b116 + m.b140 + m.b164 + m.b188 + m.b212 - m.x228 >= 0)

m.c312 = Constraint(expr=   m.b92 + m.b116 + m.b140 + m.b164 + m.b188 + m.b212 - m.x228 >= 0)

m.c313 = Constraint(expr=   m.b92 + m.b116 + m.b140 + m.b164 + m.b188 + m.b212 - m.x228 >= 0)

m.c314 = Constraint(expr=   m.b100 + m.b124 + m.b148 + m.b172 + m.b196 + m.b220 - m.x228 >= 0)

m.c315 = Constraint(expr=   m.b100 + m.b124 + m.b148 + m.b172 + m.b196 + m.b220 - m.x228 >= 0)

m.c316 = Constraint(expr=   m.b100 + m.b124 + m.b148 + m.b172 + m.b196 + m.b220 - m.x228 >= 0)

m.c317 = Constraint(expr=   m.b100 + m.b124 + m.b148 + m.b172 + m.b196 + m.b220 - m.x228 >= 0)

m.c318 = Constraint(expr=   m.b100 + m.b124 + m.b148 + m.b172 + m.b196 + m.b220 - m.x228 >= 0)

m.c319 = Constraint(expr=   m.b100 + m.b124 + m.b148 + m.b172 + m.b196 + m.b220 - m.x228 >= 0)

m.c320 = Constraint(expr=   m.b100 + m.b124 + m.b148 + m.b172 + m.b196 + m.b220 - m.x228 >= 0)

m.c321 = Constraint(expr=   m.b85 + m.b109 + m.b133 + m.b157 + m.b181 + m.b205 - m.x229 >= 0)

m.c322 = Constraint(expr=   m.b85 + m.b109 + m.b133 + m.b157 + m.b181 + m.b205 - m.x229 >= 0)

m.c323 = Constraint(expr=   m.b85 + m.b109 + m.b133 + m.b157 + m.b181 + m.b205 - m.x229 >= 0)

m.c324 = Constraint(expr=   m.b85 + m.b109 + m.b133 + m.b157 + m.b181 + m.b205 - m.x229 >= 0)

m.c325 = Constraint(expr=   m.b85 + m.b109 + m.b133 + m.b157 + m.b181 + m.b205 - m.x229 >= 0)

m.c326 = Constraint(expr=   m.b85 + m.b109 + m.b133 + m.b157 + m.b181 + m.b205 - m.x229 >= 0)

m.c327 = Constraint(expr=   m.b85 + m.b109 + m.b133 + m.b157 + m.b181 + m.b205 - m.x229 >= 0)

m.c328 = Constraint(expr=   m.b93 + m.b117 + m.b141 + m.b165 + m.b189 + m.b213 - m.x229 >= 0)

m.c329 = Constraint(expr=   m.b93 + m.b117 + m.b141 + m.b165 + m.b189 + m.b213 - m.x229 >= 0)

m.c330 = Constraint(expr=   m.b93 + m.b117 + m.b141 + m.b165 + m.b189 + m.b213 - m.x229 >= 0)

m.c331 = Constraint(expr=   m.b93 + m.b117 + m.b141 + m.b165 + m.b189 + m.b213 - m.x229 >= 0)

m.c332 = Constraint(expr=   m.b93 + m.b117 + m.b141 + m.b165 + m.b189 + m.b213 - m.x229 >= 0)

m.c333 = Constraint(expr=   m.b93 + m.b117 + m.b141 + m.b165 + m.b189 + m.b213 - m.x229 >= 0)

m.c334 = Constraint(expr=   m.b93 + m.b117 + m.b141 + m.b165 + m.b189 + m.b213 - m.x229 >= 0)

m.c335 = Constraint(expr=   m.b101 + m.b125 + m.b149 + m.b173 + m.b197 + m.b221 - m.x229 >= 0)

m.c336 = Constraint(expr=   m.b101 + m.b125 + m.b149 + m.b173 + m.b197 + m.b221 - m.x229 >= 0)

m.c337 = Constraint(expr=   m.b101 + m.b125 + m.b149 + m.b173 + m.b197 + m.b221 - m.x229 >= 0)

m.c338 = Constraint(expr=   m.b101 + m.b125 + m.b149 + m.b173 + m.b197 + m.b221 - m.x229 >= 0)

m.c339 = Constraint(expr=   m.b101 + m.b125 + m.b149 + m.b173 + m.b197 + m.b221 - m.x229 >= 0)

m.c340 = Constraint(expr=   m.b101 + m.b125 + m.b149 + m.b173 + m.b197 + m.b221 - m.x229 >= 0)

m.c341 = Constraint(expr=   m.b101 + m.b125 + m.b149 + m.b173 + m.b197 + m.b221 - m.x229 >= 0)

m.c342 = Constraint(expr=   m.b86 + m.b110 + m.b134 + m.b158 + m.b182 + m.b206 - m.x230 >= 0)

m.c343 = Constraint(expr=   m.b86 + m.b110 + m.b134 + m.b158 + m.b182 + m.b206 - m.x230 >= 0)

m.c344 = Constraint(expr=   m.b86 + m.b110 + m.b134 + m.b158 + m.b182 + m.b206 - m.x230 >= 0)

m.c345 = Constraint(expr=   m.b86 + m.b110 + m.b134 + m.b158 + m.b182 + m.b206 - m.x230 >= 0)

m.c346 = Constraint(expr=   m.b86 + m.b110 + m.b134 + m.b158 + m.b182 + m.b206 - m.x230 >= 0)

m.c347 = Constraint(expr=   m.b86 + m.b110 + m.b134 + m.b158 + m.b182 + m.b206 - m.x230 >= 0)

m.c348 = Constraint(expr=   m.b86 + m.b110 + m.b134 + m.b158 + m.b182 + m.b206 - m.x230 >= 0)

m.c349 = Constraint(expr=   m.b94 + m.b118 + m.b142 + m.b166 + m.b190 + m.b214 - m.x230 >= 0)

m.c350 = Constraint(expr=   m.b94 + m.b118 + m.b142 + m.b166 + m.b190 + m.b214 - m.x230 >= 0)

m.c351 = Constraint(expr=   m.b94 + m.b118 + m.b142 + m.b166 + m.b190 + m.b214 - m.x230 >= 0)

m.c352 = Constraint(expr=   m.b94 + m.b118 + m.b142 + m.b166 + m.b190 + m.b214 - m.x230 >= 0)

m.c353 = Constraint(expr=   m.b94 + m.b118 + m.b142 + m.b166 + m.b190 + m.b214 - m.x230 >= 0)

m.c354 = Constraint(expr=   m.b94 + m.b118 + m.b142 + m.b166 + m.b190 + m.b214 - m.x230 >= 0)

m.c355 = Constraint(expr=   m.b94 + m.b118 + m.b142 + m.b166 + m.b190 + m.b214 - m.x230 >= 0)

m.c356 = Constraint(expr=   m.b102 + m.b126 + m.b150 + m.b174 + m.b198 + m.b222 - m.x230 >= 0)

m.c357 = Constraint(expr=   m.b102 + m.b126 + m.b150 + m.b174 + m.b198 + m.b222 - m.x230 >= 0)

m.c358 = Constraint(expr=   m.b102 + m.b126 + m.b150 + m.b174 + m.b198 + m.b222 - m.x230 >= 0)

m.c359 = Constraint(expr=   m.b102 + m.b126 + m.b150 + m.b174 + m.b198 + m.b222 - m.x230 >= 0)

m.c360 = Constraint(expr=   m.b102 + m.b126 + m.b150 + m.b174 + m.b198 + m.b222 - m.x230 >= 0)

m.c361 = Constraint(expr=   m.b102 + m.b126 + m.b150 + m.b174 + m.b198 + m.b222 - m.x230 >= 0)

m.c362 = Constraint(expr=   m.b102 + m.b126 + m.b150 + m.b174 + m.b198 + m.b222 - m.x230 >= 0)

m.c363 = Constraint(expr=   m.b87 + m.b111 + m.b135 + m.b159 + m.b183 + m.b207 - m.x231 >= 0)

m.c364 = Constraint(expr=   m.b87 + m.b111 + m.b135 + m.b159 + m.b183 + m.b207 - m.x231 >= 0)

m.c365 = Constraint(expr=   m.b87 + m.b111 + m.b135 + m.b159 + m.b183 + m.b207 - m.x231 >= 0)

m.c366 = Constraint(expr=   m.b87 + m.b111 + m.b135 + m.b159 + m.b183 + m.b207 - m.x231 >= 0)

m.c367 = Constraint(expr=   m.b87 + m.b111 + m.b135 + m.b159 + m.b183 + m.b207 - m.x231 >= 0)

m.c368 = Constraint(expr=   m.b87 + m.b111 + m.b135 + m.b159 + m.b183 + m.b207 - m.x231 >= 0)

m.c369 = Constraint(expr=   m.b87 + m.b111 + m.b135 + m.b159 + m.b183 + m.b207 - m.x231 >= 0)

m.c370 = Constraint(expr=   m.b95 + m.b119 + m.b143 + m.b167 + m.b191 + m.b215 - m.x231 >= 0)

m.c371 = Constraint(expr=   m.b95 + m.b119 + m.b143 + m.b167 + m.b191 + m.b215 - m.x231 >= 0)

m.c372 = Constraint(expr=   m.b95 + m.b119 + m.b143 + m.b167 + m.b191 + m.b215 - m.x231 >= 0)

m.c373 = Constraint(expr=   m.b95 + m.b119 + m.b143 + m.b167 + m.b191 + m.b215 - m.x231 >= 0)

m.c374 = Constraint(expr=   m.b95 + m.b119 + m.b143 + m.b167 + m.b191 + m.b215 - m.x231 >= 0)

m.c375 = Constraint(expr=   m.b95 + m.b119 + m.b143 + m.b167 + m.b191 + m.b215 - m.x231 >= 0)

m.c376 = Constraint(expr=   m.b95 + m.b119 + m.b143 + m.b167 + m.b191 + m.b215 - m.x231 >= 0)

m.c377 = Constraint(expr=   m.b103 + m.b127 + m.b151 + m.b175 + m.b199 + m.b223 - m.x231 >= 0)

m.c378 = Constraint(expr=   m.b103 + m.b127 + m.b151 + m.b175 + m.b199 + m.b223 - m.x231 >= 0)

m.c379 = Constraint(expr=   m.b103 + m.b127 + m.b151 + m.b175 + m.b199 + m.b223 - m.x231 >= 0)

m.c380 = Constraint(expr=   m.b103 + m.b127 + m.b151 + m.b175 + m.b199 + m.b223 - m.x231 >= 0)

m.c381 = Constraint(expr=   m.b103 + m.b127 + m.b151 + m.b175 + m.b199 + m.b223 - m.x231 >= 0)

m.c382 = Constraint(expr=   m.b103 + m.b127 + m.b151 + m.b175 + m.b199 + m.b223 - m.x231 >= 0)

m.c383 = Constraint(expr=   m.b103 + m.b127 + m.b151 + m.b175 + m.b199 + m.b223 - m.x231 >= 0)

m.c384 = Constraint(expr=   m.b88 + m.b112 + m.b136 + m.b160 + m.b184 + m.b208 - m.x232 >= 0)

m.c385 = Constraint(expr=   m.b88 + m.b112 + m.b136 + m.b160 + m.b184 + m.b208 - m.x232 >= 0)

m.c386 = Constraint(expr=   m.b88 + m.b112 + m.b136 + m.b160 + m.b184 + m.b208 - m.x232 >= 0)

m.c387 = Constraint(expr=   m.b88 + m.b112 + m.b136 + m.b160 + m.b184 + m.b208 - m.x232 >= 0)

m.c388 = Constraint(expr=   m.b88 + m.b112 + m.b136 + m.b160 + m.b184 + m.b208 - m.x232 >= 0)

m.c389 = Constraint(expr=   m.b88 + m.b112 + m.b136 + m.b160 + m.b184 + m.b208 - m.x232 >= 0)

m.c390 = Constraint(expr=   m.b88 + m.b112 + m.b136 + m.b160 + m.b184 + m.b208 - m.x232 >= 0)

m.c391 = Constraint(expr=   m.b96 + m.b120 + m.b144 + m.b168 + m.b192 + m.b216 - m.x232 >= 0)

m.c392 = Constraint(expr=   m.b96 + m.b120 + m.b144 + m.b168 + m.b192 + m.b216 - m.x232 >= 0)

m.c393 = Constraint(expr=   m.b96 + m.b120 + m.b144 + m.b168 + m.b192 + m.b216 - m.x232 >= 0)

m.c394 = Constraint(expr=   m.b96 + m.b120 + m.b144 + m.b168 + m.b192 + m.b216 - m.x232 >= 0)

m.c395 = Constraint(expr=   m.b96 + m.b120 + m.b144 + m.b168 + m.b192 + m.b216 - m.x232 >= 0)

m.c396 = Constraint(expr=   m.b96 + m.b120 + m.b144 + m.b168 + m.b192 + m.b216 - m.x232 >= 0)

m.c397 = Constraint(expr=   m.b96 + m.b120 + m.b144 + m.b168 + m.b192 + m.b216 - m.x232 >= 0)

m.c398 = Constraint(expr=   m.b104 + m.b128 + m.b152 + m.b176 + m.b200 + m.b224 - m.x232 >= 0)

m.c399 = Constraint(expr=   m.b104 + m.b128 + m.b152 + m.b176 + m.b200 + m.b224 - m.x232 >= 0)

m.c400 = Constraint(expr=   m.b104 + m.b128 + m.b152 + m.b176 + m.b200 + m.b224 - m.x232 >= 0)

m.c401 = Constraint(expr=   m.b104 + m.b128 + m.b152 + m.b176 + m.b200 + m.b224 - m.x232 >= 0)

m.c402 = Constraint(expr=   m.b104 + m.b128 + m.b152 + m.b176 + m.b200 + m.b224 - m.x232 >= 0)

m.c403 = Constraint(expr=   m.b104 + m.b128 + m.b152 + m.b176 + m.b200 + m.b224 - m.x232 >= 0)

m.c404 = Constraint(expr=   m.b104 + m.b128 + m.b152 + m.b176 + m.b200 + m.b224 - m.x232 >= 0)

m.c405 = Constraint(expr=   m.b89 + m.b113 + m.b137 + m.b161 + m.b185 + m.b209 - m.x233 >= 0)

m.c406 = Constraint(expr=   m.b89 + m.b113 + m.b137 + m.b161 + m.b185 + m.b209 - m.x233 >= 0)

m.c407 = Constraint(expr=   m.b89 + m.b113 + m.b137 + m.b161 + m.b185 + m.b209 - m.x233 >= 0)

m.c408 = Constraint(expr=   m.b89 + m.b113 + m.b137 + m.b161 + m.b185 + m.b209 - m.x233 >= 0)

m.c409 = Constraint(expr=   m.b89 + m.b113 + m.b137 + m.b161 + m.b185 + m.b209 - m.x233 >= 0)

m.c410 = Constraint(expr=   m.b89 + m.b113 + m.b137 + m.b161 + m.b185 + m.b209 - m.x233 >= 0)

m.c411 = Constraint(expr=   m.b89 + m.b113 + m.b137 + m.b161 + m.b185 + m.b209 - m.x233 >= 0)

m.c412 = Constraint(expr=   m.b97 + m.b121 + m.b145 + m.b169 + m.b193 + m.b217 - m.x233 >= 0)

m.c413 = Constraint(expr=   m.b97 + m.b121 + m.b145 + m.b169 + m.b193 + m.b217 - m.x233 >= 0)

m.c414 = Constraint(expr=   m.b97 + m.b121 + m.b145 + m.b169 + m.b193 + m.b217 - m.x233 >= 0)

m.c415 = Constraint(expr=   m.b97 + m.b121 + m.b145 + m.b169 + m.b193 + m.b217 - m.x233 >= 0)

m.c416 = Constraint(expr=   m.b97 + m.b121 + m.b145 + m.b169 + m.b193 + m.b217 - m.x233 >= 0)

m.c417 = Constraint(expr=   m.b97 + m.b121 + m.b145 + m.b169 + m.b193 + m.b217 - m.x233 >= 0)

m.c418 = Constraint(expr=   m.b97 + m.b121 + m.b145 + m.b169 + m.b193 + m.b217 - m.x233 >= 0)

m.c419 = Constraint(expr=   m.b105 + m.b129 + m.b153 + m.b177 + m.b201 + m.b225 - m.x233 >= 0)

m.c420 = Constraint(expr=   m.b105 + m.b129 + m.b153 + m.b177 + m.b201 + m.b225 - m.x233 >= 0)

m.c421 = Constraint(expr=   m.b105 + m.b129 + m.b153 + m.b177 + m.b201 + m.b225 - m.x233 >= 0)

m.c422 = Constraint(expr=   m.b105 + m.b129 + m.b153 + m.b177 + m.b201 + m.b225 - m.x233 >= 0)

m.c423 = Constraint(expr=   m.b105 + m.b129 + m.b153 + m.b177 + m.b201 + m.b225 - m.x233 >= 0)

m.c424 = Constraint(expr=   m.b105 + m.b129 + m.b153 + m.b177 + m.b201 + m.b225 - m.x233 >= 0)

m.c425 = Constraint(expr=   m.b105 + m.b129 + m.b153 + m.b177 + m.b201 + m.b225 - m.x233 >= 0)

m.c426 = Constraint(expr=m.x290*m.b82 + 1.5*m.x290*m.b90 + m.x290*m.b98 + m.x291*m.b83 + 1.5*m.x291*m.b91 + m.x291*m.b99
                          + m.x292*m.b84 + 1.5*m.x292*m.b92 + m.x292*m.b100 + 1.5*m.x295*m.b95 + 1.5*m.x296*m.b96 + 1.5*
                         m.x297*m.b97 <= 999999)

m.c427 = Constraint(expr=m.x290*m.b106 + 1.5*m.x290*m.b114 + m.x290*m.b122 + m.x291*m.b107 + 1.5*m.x291*m.b115 + m.x291*
                         m.b123 + m.x292*m.b108 + 1.5*m.x292*m.b116 + m.x292*m.b124 + 1.5*m.x295*m.b119 + 1.5*m.x296*
                         m.b120 + 1.5*m.x297*m.b121 <= 999999)

m.c428 = Constraint(expr=m.x290*m.b130 + 1.5*m.x290*m.b138 + m.x290*m.b146 + m.x291*m.b131 + 1.5*m.x291*m.b139 + m.x291*
                         m.b147 + m.x292*m.b132 + 1.5*m.x292*m.b140 + m.x292*m.b148 + 1.5*m.x295*m.b143 + 1.5*m.x296*
                         m.b144 + 1.5*m.x297*m.b145 <= 999999)

m.c429 = Constraint(expr=m.x290*m.b154 + 1.5*m.x290*m.b162 + m.x290*m.b170 + m.x291*m.b155 + 1.5*m.x291*m.b163 + m.x291*
                         m.b171 + m.x292*m.b156 + 1.5*m.x292*m.b164 + m.x292*m.b172 + 1.5*m.x295*m.b167 + 1.5*m.x296*
                         m.b168 + 1.5*m.x297*m.b169 <= 888888)

m.c430 = Constraint(expr=m.x290*m.b178 + 1.5*m.x290*m.b186 + m.x290*m.b194 + m.x291*m.b179 + 1.5*m.x291*m.b187 + m.x291*
                         m.b195 + m.x292*m.b180 + 1.5*m.x292*m.b188 + m.x292*m.b196 + 1.5*m.x295*m.b191 + 1.5*m.x296*
                         m.b192 + 1.5*m.x297*m.b193 <= 9999999)

m.c431 = Constraint(expr=m.x290*m.b202 + 1.5*m.x290*m.b210 + m.x290*m.b218 + m.x291*m.b203 + 1.5*m.x291*m.b211 + m.x291*
                         m.b219 + m.x292*m.b204 + 1.5*m.x292*m.b212 + m.x292*m.b220 + 1.5*m.x295*m.b215 + 1.5*m.x296*
                         m.b216 + 1.5*m.x297*m.b217 <= 999999)

m.c432 = Constraint(expr=1.5*m.x293*m.b93 + m.x293*m.b101 + 1.5*m.x294*m.b94 + m.x294*m.b102 + m.x295*m.b87 + m.x295*
                         m.b103 + m.x296*m.b88 + m.x296*m.b104 + m.x297*m.b89 + m.x297*m.b105 <= 72722)

m.c433 = Constraint(expr=1.5*m.x293*m.b117 + m.x293*m.b125 + 1.5*m.x294*m.b118 + m.x294*m.b126 + m.x295*m.b111 + m.x295*
                         m.b127 + m.x296*m.b112 + m.x296*m.b128 + m.x297*m.b113 + m.x297*m.b129 <= 32737)

m.c434 = Constraint(expr=1.5*m.x293*m.b141 + m.x293*m.b149 + 1.5*m.x294*m.b142 + m.x294*m.b150 + m.x295*m.b135 + m.x295*
                         m.b151 + m.x296*m.b136 + m.x296*m.b152 + m.x297*m.b137 + m.x297*m.b153 <= 999999)

m.c435 = Constraint(expr=1.5*m.x293*m.b165 + m.x293*m.b173 + 1.5*m.x294*m.b166 + m.x294*m.b174 + m.x295*m.b159 + m.x295*
                         m.b175 + m.x296*m.b160 + m.x296*m.b176 + m.x297*m.b161 + m.x297*m.b177 <= 999999)

m.c436 = Constraint(expr=1.5*m.x293*m.b189 + m.x293*m.b197 + 1.5*m.x294*m.b190 + m.x294*m.b198 + m.x295*m.b183 + m.x295*
                         m.b199 + m.x296*m.b184 + m.x296*m.b200 + m.x297*m.b185 + m.x297*m.b201 <= 122344)

m.c437 = Constraint(expr=1.5*m.x293*m.b213 + m.x293*m.b221 + 1.5*m.x294*m.b214 + m.x294*m.b222 + m.x295*m.b207 + m.x295*
                         m.b223 + m.x296*m.b208 + m.x296*m.b224 + m.x297*m.b209 + m.x297*m.b225 <= 147559)

m.c438 = Constraint(expr=m.x293*m.b85 + m.x294*m.b86 <= 999999)

m.c439 = Constraint(expr=m.x293*m.b109 + m.x294*m.b110 <= 999999)

m.c440 = Constraint(expr=m.x293*m.b133 + m.x294*m.b134 <= 999999)

m.c441 = Constraint(expr=m.x293*m.b157 + m.x294*m.b158 <= 999999)

m.c442 = Constraint(expr=m.x293*m.b181 + m.x294*m.b182 <= 999999)

m.c443 = Constraint(expr=m.x293*m.b205 + m.x294*m.b206 <= 999999)

m.c444 = Constraint(expr=0.527704485488127*m.i26*m.x290 + 0.527704485488127*m.i27*m.x291 + 0.527704485488127*m.i28*
                         m.x292 + 0.527704485488127*m.i29*m.x293 + 0.527704485488127*m.i30*m.x294 + 0.527704485488127*
                         m.i31*m.x295 + 0.527704485488127*m.i32*m.x296 + 0.527704485488127*m.i33*m.x297 >= 1000)

m.c445 = Constraint(expr=1.33333333333333*m.i34*m.x290 + 1.33333333333333*m.i35*m.x291 + 1.33333333333333*m.i36*m.x292
                          + 1.33333333333333*m.i37*m.x293 + 1.33333333333333*m.i38*m.x294 + 1.33333333333333*m.i39*
                         m.x295 + 1.33333333333333*m.i40*m.x296 + 1.33333333333333*m.i41*m.x297 >= 1500)

m.c446 = Constraint(expr=0.858369098712446*m.i42*m.x290 + 0.858369098712446*m.i43*m.x291 + 0.858369098712446*m.i44*
                         m.x292 + 0.858369098712446*m.i45*m.x293 + 0.858369098712446*m.i46*m.x294 + 0.858369098712446*
                         m.i47*m.x295 + 0.858369098712446*m.i48*m.x296 + 0.858369098712446*m.i49*m.x297 >= 2000)

m.c447 = Constraint(expr=1.32450331125828*m.i50*m.x290 + 1.32450331125828*m.i51*m.x291 + 1.32450331125828*m.i52*m.x292
                          + 1.32450331125828*m.i53*m.x293 + 1.32450331125828*m.i54*m.x294 + 1.32450331125828*m.i55*
                         m.x295 + 1.32450331125828*m.i56*m.x296 + 1.32450331125828*m.i57*m.x297 >= 2000)

m.c448 = Constraint(expr=0.50125313283208*m.i58*m.x290 + 0.50125313283208*m.i59*m.x291 + 0.50125313283208*m.i60*m.x292
                          + 0.50125313283208*m.i61*m.x293 + 0.50125313283208*m.i62*m.x294 + 0.50125313283208*m.i63*
                         m.x295 + 0.50125313283208*m.i64*m.x296 + 0.50125313283208*m.i65*m.x297 >= 1500)

m.c449 = Constraint(expr=0.555555555555556*m.i66*m.x290 + 0.555555555555556*m.i67*m.x291 + 0.555555555555556*m.i68*
                         m.x292 + 0.555555555555556*m.i69*m.x293 + 0.555555555555556*m.i70*m.x294 + 0.555555555555556*
                         m.i71*m.x295 + 0.555555555555556*m.i72*m.x296 + 0.555555555555556*m.i73*m.x297 >= 1500)

m.c450 = Constraint(expr=1.17647058823529*m.i74*m.x290 + 1.17647058823529*m.i75*m.x291 + 1.17647058823529*m.i76*m.x292
                          + 1.17647058823529*m.i77*m.x293 + 1.17647058823529*m.i78*m.x294 + 1.17647058823529*m.i79*
                         m.x295 + 1.17647058823529*m.i80*m.x296 + 1.17647058823529*m.i81*m.x297 >= 2500)

m.c451 = Constraint(expr=0.527704485488127*m.i26*m.x290 + 0.527704485488127*m.i27*m.x291 + 0.527704485488127*m.i28*
                         m.x292 + 0.527704485488127*m.i29*m.x293 + 0.527704485488127*m.i30*m.x294 + 0.527704485488127*
                         m.i31*m.x295 + 0.527704485488127*m.i32*m.x296 + 0.527704485488127*m.i33*m.x297 <= 1500)

m.c452 = Constraint(expr=1.33333333333333*m.i34*m.x290 + 1.33333333333333*m.i35*m.x291 + 1.33333333333333*m.i36*m.x292
                          + 1.33333333333333*m.i37*m.x293 + 1.33333333333333*m.i38*m.x294 + 1.33333333333333*m.i39*
                         m.x295 + 1.33333333333333*m.i40*m.x296 + 1.33333333333333*m.i41*m.x297 <= 2250)

m.c453 = Constraint(expr=0.858369098712446*m.i42*m.x290 + 0.858369098712446*m.i43*m.x291 + 0.858369098712446*m.i44*
                         m.x292 + 0.858369098712446*m.i45*m.x293 + 0.858369098712446*m.i46*m.x294 + 0.858369098712446*
                         m.i47*m.x295 + 0.858369098712446*m.i48*m.x296 + 0.858369098712446*m.i49*m.x297 <= 3000)

m.c454 = Constraint(expr=1.32450331125828*m.i50*m.x290 + 1.32450331125828*m.i51*m.x291 + 1.32450331125828*m.i52*m.x292
                          + 1.32450331125828*m.i53*m.x293 + 1.32450331125828*m.i54*m.x294 + 1.32450331125828*m.i55*
                         m.x295 + 1.32450331125828*m.i56*m.x296 + 1.32450331125828*m.i57*m.x297 <= 3000)

m.c455 = Constraint(expr=0.50125313283208*m.i58*m.x290 + 0.50125313283208*m.i59*m.x291 + 0.50125313283208*m.i60*m.x292
                          + 0.50125313283208*m.i61*m.x293 + 0.50125313283208*m.i62*m.x294 + 0.50125313283208*m.i63*
                         m.x295 + 0.50125313283208*m.i64*m.x296 + 0.50125313283208*m.i65*m.x297 <= 2250)

m.c456 = Constraint(expr=0.555555555555556*m.i66*m.x290 + 0.555555555555556*m.i67*m.x291 + 0.555555555555556*m.i68*
                         m.x292 + 0.555555555555556*m.i69*m.x293 + 0.555555555555556*m.i70*m.x294 + 0.555555555555556*
                         m.i71*m.x295 + 0.555555555555556*m.i72*m.x296 + 0.555555555555556*m.i73*m.x297 <= 2250)

m.c457 = Constraint(expr=1.17647058823529*m.i74*m.x290 + 1.17647058823529*m.i75*m.x291 + 1.17647058823529*m.i76*m.x292
                          + 1.17647058823529*m.i77*m.x293 + 1.17647058823529*m.i78*m.x294 + 1.17647058823529*m.i79*
                         m.x295 + 1.17647058823529*m.i80*m.x296 + 1.17647058823529*m.i81*m.x297 <= 3750)

m.c458 = Constraint(expr= - 500*m.x226 + m.x290 >= 0)

m.c459 = Constraint(expr= - 500*m.x227 + m.x291 >= 0)

m.c460 = Constraint(expr= - 500*m.x228 + m.x292 >= 0)

m.c461 = Constraint(expr= - 500*m.x229 + m.x293 >= 0)

m.c462 = Constraint(expr= - 500*m.x230 + m.x294 >= 0)

m.c463 = Constraint(expr= - 500*m.x231 + m.x295 >= 0)

m.c464 = Constraint(expr= - 500*m.x232 + m.x296 >= 0)

m.c465 = Constraint(expr= - 500*m.x233 + m.x297 >= 0)

m.c466 = Constraint(expr= - 2000*m.x226 + m.x290 <= 0)

m.c467 = Constraint(expr= - 2000*m.x227 + m.x291 <= 0)

m.c468 = Constraint(expr= - 2000*m.x228 + m.x292 <= 0)

m.c469 = Constraint(expr= - 2000*m.x229 + m.x293 <= 0)

m.c470 = Constraint(expr= - 2000*m.x230 + m.x294 <= 0)

m.c471 = Constraint(expr= - 2000*m.x231 + m.x295 <= 0)

m.c472 = Constraint(expr= - 2000*m.x232 + m.x296 <= 0)

m.c473 = Constraint(expr= - 2000*m.x233 + m.x297 <= 0)

m.c474 = Constraint(expr= - m.x226 + m.b234 + m.b242 + m.b250 + m.b258 + m.b266 + m.b274 + m.b282 >= 0)

m.c475 = Constraint(expr= - m.x227 + m.b235 + m.b243 + m.b251 + m.b259 + m.b267 + m.b275 + m.b283 >= 0)

m.c476 = Constraint(expr= - m.x228 + m.b236 + m.b244 + m.b252 + m.b260 + m.b268 + m.b276 + m.b284 >= 0)

m.c477 = Constraint(expr= - m.x229 + m.b237 + m.b245 + m.b253 + m.b261 + m.b269 + m.b277 + m.b285 >= 0)

m.c478 = Constraint(expr= - m.x230 + m.b238 + m.b246 + m.b254 + m.b262 + m.b270 + m.b278 + m.b286 >= 0)

m.c479 = Constraint(expr= - m.x231 + m.b239 + m.b247 + m.b255 + m.b263 + m.b271 + m.b279 + m.b287 >= 0)

m.c480 = Constraint(expr= - m.x232 + m.b240 + m.b248 + m.b256 + m.b264 + m.b272 + m.b280 + m.b288 >= 0)

m.c481 = Constraint(expr= - m.x233 + m.b241 + m.b249 + m.b257 + m.b265 + m.b273 + m.b281 + m.b289 >= 0)

m.c482 = Constraint(expr=   m.x226 - m.b234 >= 0)

m.c483 = Constraint(expr=   m.x227 - m.b235 >= 0)

m.c484 = Constraint(expr=   m.x228 - m.b236 >= 0)

m.c485 = Constraint(expr=   m.x229 - m.b237 >= 0)

m.c486 = Constraint(expr=   m.x230 - m.b238 >= 0)

m.c487 = Constraint(expr=   m.x231 - m.b239 >= 0)

m.c488 = Constraint(expr=   m.x232 - m.b240 >= 0)

m.c489 = Constraint(expr=   m.x233 - m.b241 >= 0)

m.c490 = Constraint(expr=   m.x226 - m.b242 >= 0)

m.c491 = Constraint(expr=   m.x227 - m.b243 >= 0)

m.c492 = Constraint(expr=   m.x228 - m.b244 >= 0)

m.c493 = Constraint(expr=   m.x229 - m.b245 >= 0)

m.c494 = Constraint(expr=   m.x230 - m.b246 >= 0)

m.c495 = Constraint(expr=   m.x231 - m.b247 >= 0)

m.c496 = Constraint(expr=   m.x232 - m.b248 >= 0)

m.c497 = Constraint(expr=   m.x233 - m.b249 >= 0)

m.c498 = Constraint(expr=   m.x226 - m.b250 >= 0)

m.c499 = Constraint(expr=   m.x227 - m.b251 >= 0)

m.c500 = Constraint(expr=   m.x228 - m.b252 >= 0)

m.c501 = Constraint(expr=   m.x229 - m.b253 >= 0)

m.c502 = Constraint(expr=   m.x230 - m.b254 >= 0)

m.c503 = Constraint(expr=   m.x231 - m.b255 >= 0)

m.c504 = Constraint(expr=   m.x232 - m.b256 >= 0)

m.c505 = Constraint(expr=   m.x233 - m.b257 >= 0)

m.c506 = Constraint(expr=   m.x226 - m.b258 >= 0)

m.c507 = Constraint(expr=   m.x227 - m.b259 >= 0)

m.c508 = Constraint(expr=   m.x228 - m.b260 >= 0)

m.c509 = Constraint(expr=   m.x229 - m.b261 >= 0)

m.c510 = Constraint(expr=   m.x230 - m.b262 >= 0)

m.c511 = Constraint(expr=   m.x231 - m.b263 >= 0)

m.c512 = Constraint(expr=   m.x232 - m.b264 >= 0)

m.c513 = Constraint(expr=   m.x233 - m.b265 >= 0)

m.c514 = Constraint(expr=   m.x226 - m.b266 >= 0)

m.c515 = Constraint(expr=   m.x227 - m.b267 >= 0)

m.c516 = Constraint(expr=   m.x228 - m.b268 >= 0)

m.c517 = Constraint(expr=   m.x229 - m.b269 >= 0)

m.c518 = Constraint(expr=   m.x230 - m.b270 >= 0)

m.c519 = Constraint(expr=   m.x231 - m.b271 >= 0)

m.c520 = Constraint(expr=   m.x232 - m.b272 >= 0)

m.c521 = Constraint(expr=   m.x233 - m.b273 >= 0)

m.c522 = Constraint(expr=   m.x226 - m.b274 >= 0)

m.c523 = Constraint(expr=   m.x227 - m.b275 >= 0)

m.c524 = Constraint(expr=   m.x228 - m.b276 >= 0)

m.c525 = Constraint(expr=   m.x229 - m.b277 >= 0)

m.c526 = Constraint(expr=   m.x230 - m.b278 >= 0)

m.c527 = Constraint(expr=   m.x231 - m.b279 >= 0)

m.c528 = Constraint(expr=   m.x232 - m.b280 >= 0)

m.c529 = Constraint(expr=   m.x233 - m.b281 >= 0)

m.c530 = Constraint(expr=   m.x226 - m.b282 >= 0)

m.c531 = Constraint(expr=   m.x227 - m.b283 >= 0)

m.c532 = Constraint(expr=   m.x228 - m.b284 >= 0)

m.c533 = Constraint(expr=   m.x229 - m.b285 >= 0)

m.c534 = Constraint(expr=   m.x230 - m.b286 >= 0)

m.c535 = Constraint(expr=   m.x231 - m.b287 >= 0)

m.c536 = Constraint(expr=   m.x232 - m.b288 >= 0)

m.c537 = Constraint(expr=   m.x233 - m.b289 >= 0)

m.c538 = Constraint(expr=   m.b234 + m.b235 + m.b236 + m.b237 + m.b238 + m.b239 + m.b240 + m.b241 >= 1)

m.c539 = Constraint(expr=   m.b242 + m.b243 + m.b244 + m.b245 + m.b246 + m.b247 + m.b248 + m.b249 >= 1)

m.c540 = Constraint(expr=   m.b250 + m.b251 + m.b252 + m.b253 + m.b254 + m.b255 + m.b256 + m.b257 >= 1)

m.c541 = Constraint(expr=   m.b258 + m.b259 + m.b260 + m.b261 + m.b262 + m.b263 + m.b264 + m.b265 >= 1)

m.c542 = Constraint(expr=   m.b266 + m.b267 + m.b268 + m.b269 + m.b270 + m.b271 + m.b272 + m.b273 >= 1)

m.c543 = Constraint(expr=   m.b274 + m.b275 + m.b276 + m.b277 + m.b278 + m.b279 + m.b280 + m.b281 >= 1)

m.c544 = Constraint(expr=   m.b282 + m.b283 + m.b284 + m.b285 + m.b286 + m.b287 + m.b288 + m.b289 >= 1)

m.c545 = Constraint(expr= - m.i26 + m.b234 <= 0)

m.c546 = Constraint(expr= - m.i27 + m.b235 <= 0)

m.c547 = Constraint(expr= - m.i28 + m.b236 <= 0)

m.c548 = Constraint(expr= - m.i29 + m.b237 <= 0)

m.c549 = Constraint(expr= - m.i30 + m.b238 <= 0)

m.c550 = Constraint(expr= - m.i31 + m.b239 <= 0)

m.c551 = Constraint(expr= - m.i32 + m.b240 <= 0)

m.c552 = Constraint(expr= - m.i33 + m.b241 <= 0)

m.c553 = Constraint(expr= - m.i34 + m.b242 <= 0)

m.c554 = Constraint(expr= - m.i35 + m.b243 <= 0)

m.c555 = Constraint(expr= - m.i36 + m.b244 <= 0)

m.c556 = Constraint(expr= - m.i37 + m.b245 <= 0)

m.c557 = Constraint(expr= - m.i38 + m.b246 <= 0)

m.c558 = Constraint(expr= - m.i39 + m.b247 <= 0)

m.c559 = Constraint(expr= - m.i40 + m.b248 <= 0)

m.c560 = Constraint(expr= - m.i41 + m.b249 <= 0)

m.c561 = Constraint(expr= - m.i42 + m.b250 <= 0)

m.c562 = Constraint(expr= - m.i43 + m.b251 <= 0)

m.c563 = Constraint(expr= - m.i44 + m.b252 <= 0)

m.c564 = Constraint(expr= - m.i45 + m.b253 <= 0)

m.c565 = Constraint(expr= - m.i46 + m.b254 <= 0)

m.c566 = Constraint(expr= - m.i47 + m.b255 <= 0)

m.c567 = Constraint(expr= - m.i48 + m.b256 <= 0)

m.c568 = Constraint(expr= - m.i49 + m.b257 <= 0)

m.c569 = Constraint(expr= - m.i50 + m.b258 <= 0)

m.c570 = Constraint(expr= - m.i51 + m.b259 <= 0)

m.c571 = Constraint(expr= - m.i52 + m.b260 <= 0)

m.c572 = Constraint(expr= - m.i53 + m.b261 <= 0)

m.c573 = Constraint(expr= - m.i54 + m.b262 <= 0)

m.c574 = Constraint(expr= - m.i55 + m.b263 <= 0)

m.c575 = Constraint(expr= - m.i56 + m.b264 <= 0)

m.c576 = Constraint(expr= - m.i57 + m.b265 <= 0)

m.c577 = Constraint(expr= - m.i58 + m.b266 <= 0)

m.c578 = Constraint(expr= - m.i59 + m.b267 <= 0)

m.c579 = Constraint(expr= - m.i60 + m.b268 <= 0)

m.c580 = Constraint(expr= - m.i61 + m.b269 <= 0)

m.c581 = Constraint(expr= - m.i62 + m.b270 <= 0)

m.c582 = Constraint(expr= - m.i63 + m.b271 <= 0)

m.c583 = Constraint(expr= - m.i64 + m.b272 <= 0)

m.c584 = Constraint(expr= - m.i65 + m.b273 <= 0)

m.c585 = Constraint(expr= - m.i66 + m.b274 <= 0)

m.c586 = Constraint(expr= - m.i67 + m.b275 <= 0)

m.c587 = Constraint(expr= - m.i68 + m.b276 <= 0)

m.c588 = Constraint(expr= - m.i69 + m.b277 <= 0)

m.c589 = Constraint(expr= - m.i70 + m.b278 <= 0)

m.c590 = Constraint(expr= - m.i71 + m.b279 <= 0)

m.c591 = Constraint(expr= - m.i72 + m.b280 <= 0)

m.c592 = Constraint(expr= - m.i73 + m.b281 <= 0)

m.c593 = Constraint(expr= - m.i74 + m.b282 <= 0)

m.c594 = Constraint(expr= - m.i75 + m.b283 <= 0)

m.c595 = Constraint(expr= - m.i76 + m.b284 <= 0)

m.c596 = Constraint(expr= - m.i77 + m.b285 <= 0)

m.c597 = Constraint(expr= - m.i78 + m.b286 <= 0)

m.c598 = Constraint(expr= - m.i79 + m.b287 <= 0)

m.c599 = Constraint(expr= - m.i80 + m.b288 <= 0)

m.c600 = Constraint(expr= - m.i81 + m.b289 <= 0)

m.c601 = Constraint(expr=   m.i26 - 4*m.b234 <= 0)

m.c602 = Constraint(expr=   m.i27 - 4*m.b235 <= 0)

m.c603 = Constraint(expr=   m.i28 - 4*m.b236 <= 0)

m.c604 = Constraint(expr=   m.i29 - 4*m.b237 <= 0)

m.c605 = Constraint(expr=   m.i30 - 4*m.b238 <= 0)

m.c606 = Constraint(expr=   m.i31 - 4*m.b239 <= 0)

m.c607 = Constraint(expr=   m.i32 - 4*m.b240 <= 0)

m.c608 = Constraint(expr=   m.i33 - 4*m.b241 <= 0)

m.c609 = Constraint(expr=   m.i34 - 4*m.b242 <= 0)

m.c610 = Constraint(expr=   m.i35 - 4*m.b243 <= 0)

m.c611 = Constraint(expr=   m.i36 - 4*m.b244 <= 0)

m.c612 = Constraint(expr=   m.i37 - 4*m.b245 <= 0)

m.c613 = Constraint(expr=   m.i38 - 4*m.b246 <= 0)

m.c614 = Constraint(expr=   m.i39 - 4*m.b247 <= 0)

m.c615 = Constraint(expr=   m.i40 - 4*m.b248 <= 0)

m.c616 = Constraint(expr=   m.i41 - 4*m.b249 <= 0)

m.c617 = Constraint(expr=   m.i42 - 4*m.b250 <= 0)

m.c618 = Constraint(expr=   m.i43 - 4*m.b251 <= 0)

m.c619 = Constraint(expr=   m.i44 - 4*m.b252 <= 0)

m.c620 = Constraint(expr=   m.i45 - 4*m.b253 <= 0)

m.c621 = Constraint(expr=   m.i46 - 4*m.b254 <= 0)

m.c622 = Constraint(expr=   m.i47 - 4*m.b255 <= 0)

m.c623 = Constraint(expr=   m.i48 - 4*m.b256 <= 0)

m.c624 = Constraint(expr=   m.i49 - 4*m.b257 <= 0)

m.c625 = Constraint(expr=   m.i50 - 4*m.b258 <= 0)

m.c626 = Constraint(expr=   m.i51 - 4*m.b259 <= 0)

m.c627 = Constraint(expr=   m.i52 - 4*m.b260 <= 0)

m.c628 = Constraint(expr=   m.i53 - 4*m.b261 <= 0)

m.c629 = Constraint(expr=   m.i54 - 4*m.b262 <= 0)

m.c630 = Constraint(expr=   m.i55 - 4*m.b263 <= 0)

m.c631 = Constraint(expr=   m.i56 - 4*m.b264 <= 0)

m.c632 = Constraint(expr=   m.i57 - 4*m.b265 <= 0)

m.c633 = Constraint(expr=   m.i58 - 4*m.b266 <= 0)

m.c634 = Constraint(expr=   m.i59 - 4*m.b267 <= 0)

m.c635 = Constraint(expr=   m.i60 - 4*m.b268 <= 0)

m.c636 = Constraint(expr=   m.i61 - 4*m.b269 <= 0)

m.c637 = Constraint(expr=   m.i62 - 4*m.b270 <= 0)

m.c638 = Constraint(expr=   m.i63 - 4*m.b271 <= 0)

m.c639 = Constraint(expr=   m.i64 - 4*m.b272 <= 0)

m.c640 = Constraint(expr=   m.i65 - 4*m.b273 <= 0)

m.c641 = Constraint(expr=   m.i66 - 4*m.b274 <= 0)

m.c642 = Constraint(expr=   m.i67 - 4*m.b275 <= 0)

m.c643 = Constraint(expr=   m.i68 - 4*m.b276 <= 0)

m.c644 = Constraint(expr=   m.i69 - 4*m.b277 <= 0)

m.c645 = Constraint(expr=   m.i70 - 4*m.b278 <= 0)

m.c646 = Constraint(expr=   m.i71 - 4*m.b279 <= 0)

m.c647 = Constraint(expr=   m.i72 - 4*m.b280 <= 0)

m.c648 = Constraint(expr=   m.i73 - 4*m.b281 <= 0)

m.c649 = Constraint(expr=   m.i74 - 4*m.b282 <= 0)

m.c650 = Constraint(expr=   m.i75 - 4*m.b283 <= 0)

m.c651 = Constraint(expr=   m.i76 - 4*m.b284 <= 0)

m.c652 = Constraint(expr=   m.i77 - 4*m.b285 <= 0)

m.c653 = Constraint(expr=   m.i78 - 4*m.b286 <= 0)

m.c654 = Constraint(expr=   m.i79 - 4*m.b287 <= 0)

m.c655 = Constraint(expr=   m.i80 - 4*m.b288 <= 0)

m.c656 = Constraint(expr=   m.i81 - 4*m.b289 <= 0)

m.c657 = Constraint(expr=m.b82*m.x290 + 1.1*m.b106*m.x290 + 1.2*m.b130*m.x290 + 1.3*m.b154*m.x290 + 1.4*m.b178*m.x290 + 
                         1.5*m.b202*m.x290 - m.x298 == 0)

m.c658 = Constraint(expr=m.b90*m.x290 + 1.1*m.b114*m.x290 + 1.2*m.b138*m.x290 + 1.3*m.b162*m.x290 + 1.4*m.b186*m.x290 + 
                         1.5*m.b210*m.x290 - m.x299 == 0)

m.c659 = Constraint(expr=m.b98*m.x290 + 1.1*m.b122*m.x290 + 1.2*m.b146*m.x290 + 1.3*m.b170*m.x290 + 1.4*m.b194*m.x290 + 
                         1.5*m.b218*m.x290 - m.x300 == 0)

m.c660 = Constraint(expr=m.b83*m.x291 + 1.1*m.b107*m.x291 + 1.2*m.b131*m.x291 + 1.3*m.b155*m.x291 + 1.4*m.b179*m.x291 + 
                         1.5*m.b203*m.x291 - m.x301 == 0)

m.c661 = Constraint(expr=m.b91*m.x291 + 1.1*m.b115*m.x291 + 1.2*m.b139*m.x291 + 1.3*m.b163*m.x291 + 1.4*m.b187*m.x291 + 
                         1.5*m.b211*m.x291 - m.x302 == 0)

m.c662 = Constraint(expr=m.b99*m.x291 + 1.1*m.b123*m.x291 + 1.2*m.b147*m.x291 + 1.3*m.b171*m.x291 + 1.4*m.b195*m.x291 + 
                         1.5*m.b219*m.x291 - m.x303 == 0)

m.c663 = Constraint(expr=m.b84*m.x292 + 1.1*m.b108*m.x292 + 1.2*m.b132*m.x292 + 1.3*m.b156*m.x292 + 1.4*m.b180*m.x292 + 
                         1.5*m.b204*m.x292 - m.x304 == 0)

m.c664 = Constraint(expr=m.b92*m.x292 + 1.1*m.b116*m.x292 + 1.2*m.b140*m.x292 + 1.3*m.b164*m.x292 + 1.4*m.b188*m.x292 + 
                         1.5*m.b212*m.x292 - m.x305 == 0)

m.c665 = Constraint(expr=m.b100*m.x292 + 1.1*m.b124*m.x292 + 1.2*m.b148*m.x292 + 1.3*m.b172*m.x292 + 1.4*m.b196*m.x292
                          + 1.5*m.b220*m.x292 - m.x306 == 0)

m.c666 = Constraint(expr=m.b85*m.x293 + 1.1*m.b109*m.x293 + 1.2*m.b133*m.x293 + 1.3*m.b157*m.x293 + 1.4*m.b181*m.x293 + 
                         1.5*m.b205*m.x293 - m.x307 == 0)

m.c667 = Constraint(expr=m.b93*m.x293 + 1.1*m.b117*m.x293 + 1.2*m.b141*m.x293 + 1.3*m.b165*m.x293 + 1.4*m.b189*m.x293 + 
                         1.5*m.b213*m.x293 - m.x308 == 0)

m.c668 = Constraint(expr=m.b101*m.x293 + 1.1*m.b125*m.x293 + 1.2*m.b149*m.x293 + 1.3*m.b173*m.x293 + 1.4*m.b197*m.x293
                          + 1.5*m.b221*m.x293 - m.x309 == 0)

m.c669 = Constraint(expr=m.b86*m.x294 + 1.1*m.b110*m.x294 + 1.2*m.b134*m.x294 + 1.3*m.b158*m.x294 + 1.4*m.b182*m.x294 + 
                         1.5*m.b206*m.x294 - m.x310 == 0)

m.c670 = Constraint(expr=m.b94*m.x294 + 1.1*m.b118*m.x294 + 1.2*m.b142*m.x294 + 1.3*m.b166*m.x294 + 1.4*m.b190*m.x294 + 
                         1.5*m.b214*m.x294 - m.x311 == 0)

m.c671 = Constraint(expr=m.b102*m.x294 + 1.1*m.b126*m.x294 + 1.2*m.b150*m.x294 + 1.3*m.b174*m.x294 + 1.4*m.b198*m.x294
                          + 1.5*m.b222*m.x294 - m.x312 == 0)

m.c672 = Constraint(expr=m.b87*m.x295 + 1.1*m.b111*m.x295 + 1.2*m.b135*m.x295 + 1.3*m.b159*m.x295 + 1.4*m.b183*m.x295 + 
                         1.5*m.b207*m.x295 - m.x313 == 0)

m.c673 = Constraint(expr=m.b95*m.x295 + 1.1*m.b119*m.x295 + 1.2*m.b143*m.x295 + 1.3*m.b167*m.x295 + 1.4*m.b191*m.x295 + 
                         1.5*m.b215*m.x295 - m.x314 == 0)

m.c674 = Constraint(expr=m.b103*m.x295 + 1.1*m.b127*m.x295 + 1.2*m.b151*m.x295 + 1.3*m.b175*m.x295 + 1.4*m.b199*m.x295
                          + 1.5*m.b223*m.x295 - m.x315 == 0)

m.c675 = Constraint(expr=m.b88*m.x296 + 1.1*m.b112*m.x296 + 1.2*m.b136*m.x296 + 1.3*m.b160*m.x296 + 1.4*m.b184*m.x296 + 
                         1.5*m.b208*m.x296 - m.x316 == 0)

m.c676 = Constraint(expr=m.b96*m.x296 + 1.1*m.b120*m.x296 + 1.2*m.b144*m.x296 + 1.3*m.b168*m.x296 + 1.4*m.b192*m.x296 + 
                         1.5*m.b216*m.x296 - m.x317 == 0)

m.c677 = Constraint(expr=m.b104*m.x296 + 1.1*m.b128*m.x296 + 1.2*m.b152*m.x296 + 1.3*m.b176*m.x296 + 1.4*m.b200*m.x296
                          + 1.5*m.b224*m.x296 - m.x318 == 0)

m.c678 = Constraint(expr=m.b89*m.x297 + 1.1*m.b113*m.x297 + 1.2*m.b137*m.x297 + 1.3*m.b161*m.x297 + 1.4*m.b185*m.x297 + 
                         1.5*m.b209*m.x297 - m.x319 == 0)

m.c679 = Constraint(expr=m.b97*m.x297 + 1.1*m.b121*m.x297 + 1.2*m.b145*m.x297 + 1.3*m.b169*m.x297 + 1.4*m.b193*m.x297 + 
                         1.5*m.b217*m.x297 - m.x320 == 0)

m.c680 = Constraint(expr=m.b105*m.x297 + 1.1*m.b129*m.x297 + 1.2*m.b153*m.x297 + 1.3*m.b177*m.x297 + 1.4*m.b201*m.x297
                          + 1.5*m.b225*m.x297 - m.x321 == 0)

m.c681 = Constraint(expr=0.33*m.i26*m.x290 + 0.26*m.i34*m.x290 + 0.48*m.i42*m.x290 + 0.44*m.i50*m.x290 + 0.711*m.i58*
                         m.x290 + 0.35*m.i66*m.x290 + 0.3*m.i74*m.x290 - m.x322 == 0)

m.c682 = Constraint(expr=0.33*m.i27*m.x291 + 0.26*m.i35*m.x291 + 0.48*m.i43*m.x291 + 0.44*m.i51*m.x291 + 0.711*m.i59*
                         m.x291 + 0.35*m.i67*m.x291 + 0.3*m.i75*m.x291 - m.x323 == 0)

m.c683 = Constraint(expr=0.33*m.i28*m.x292 + 0.26*m.i36*m.x292 + 0.48*m.i44*m.x292 + 0.44*m.i52*m.x292 + 0.711*m.i60*
                         m.x292 + 0.35*m.i68*m.x292 + 0.3*m.i76*m.x292 - m.x324 == 0)

m.c684 = Constraint(expr=0.33*m.i29*m.x293 + 0.26*m.i37*m.x293 + 0.48*m.i45*m.x293 + 0.44*m.i53*m.x293 + 0.711*m.i61*
                         m.x293 + 0.35*m.i69*m.x293 + 0.3*m.i77*m.x293 - m.x325 == 0)

m.c685 = Constraint(expr=0.33*m.i30*m.x294 + 0.26*m.i38*m.x294 + 0.48*m.i46*m.x294 + 0.44*m.i54*m.x294 + 0.711*m.i62*
                         m.x294 + 0.35*m.i70*m.x294 + 0.3*m.i78*m.x294 - m.x326 == 0)

m.c686 = Constraint(expr=0.33*m.i31*m.x295 + 0.26*m.i39*m.x295 + 0.48*m.i47*m.x295 + 0.44*m.i55*m.x295 + 0.711*m.i63*
                         m.x295 + 0.35*m.i71*m.x295 + 0.3*m.i79*m.x295 - m.x327 == 0)

m.c687 = Constraint(expr=0.33*m.i32*m.x296 + 0.26*m.i40*m.x296 + 0.48*m.i48*m.x296 + 0.44*m.i56*m.x296 + 0.711*m.i64*
                         m.x296 + 0.35*m.i72*m.x296 + 0.3*m.i80*m.x296 - m.x328 == 0)

m.c688 = Constraint(expr=0.33*m.i33*m.x297 + 0.26*m.i41*m.x297 + 0.48*m.i49*m.x297 + 0.44*m.i57*m.x297 + 0.711*m.i65*
                         m.x297 + 0.35*m.i73*m.x297 + 0.3*m.i81*m.x297 - m.x329 == 0)
