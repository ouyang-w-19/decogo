#  MINLP written by GAMS Convert at 04/21/18 13:51:13
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        894       33      370      491        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        361       73      216       72        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       4918     4160      758        0
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
m.i82 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i83 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i84 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i85 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i86 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i87 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i88 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i89 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i90 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i91 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i92 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i93 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i94 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i95 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i96 = Var(within=Integers,bounds=(0,4),initialize=2)
m.i97 = Var(within=Integers,bounds=(0,4),initialize=2)
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
m.x242 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,1),initialize=0)
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
m.x322 = Var(within=Reals,bounds=(0,None),initialize=2000)
m.x323 = Var(within=Reals,bounds=(0,None),initialize=2000)
m.x324 = Var(within=Reals,bounds=(0,None),initialize=2000)
m.x325 = Var(within=Reals,bounds=(0,None),initialize=2000)
m.x326 = Var(within=Reals,bounds=(0,None),initialize=2000)
m.x327 = Var(within=Reals,bounds=(0,None),initialize=2000)
m.x328 = Var(within=Reals,bounds=(0,None),initialize=2000)
m.x329 = Var(within=Reals,bounds=(0,None),initialize=2000)
m.x330 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x331 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x332 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x333 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x334 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x335 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x336 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x337 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x338 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x339 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x340 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x341 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x342 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x343 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x344 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x345 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x346 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x347 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x348 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x349 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x350 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x351 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x352 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x353 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x354 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x355 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x356 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x357 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x358 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x359 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x360 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x361 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13 + m.x14
                        + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20 + m.x21 + m.x22 + m.x23 + m.x24 + m.x25
                        + 10*m.x242 + 10*m.x243 + 10*m.x244 + 10*m.x245 + 10*m.x246 + 10*m.x247 + 10*m.x248 + 10*m.x249
                       , sense=minimize)

m.c2 = Constraint(expr=   m.i26 + m.i34 + m.i42 + m.i50 + m.i58 + m.i66 + m.i74 + m.i82 + m.i90 <= 4)

m.c3 = Constraint(expr=   m.i27 + m.i35 + m.i43 + m.i51 + m.i59 + m.i67 + m.i75 + m.i83 + m.i91 <= 4)

m.c4 = Constraint(expr=   m.i28 + m.i36 + m.i44 + m.i52 + m.i60 + m.i68 + m.i76 + m.i84 + m.i92 <= 4)

m.c5 = Constraint(expr=   m.i29 + m.i37 + m.i45 + m.i53 + m.i61 + m.i69 + m.i77 + m.i85 + m.i93 <= 4)

m.c6 = Constraint(expr=   m.i30 + m.i38 + m.i46 + m.i54 + m.i62 + m.i70 + m.i78 + m.i86 + m.i94 <= 4)

m.c7 = Constraint(expr=   m.i31 + m.i39 + m.i47 + m.i55 + m.i63 + m.i71 + m.i79 + m.i87 + m.i95 <= 4)

m.c8 = Constraint(expr=   m.i32 + m.i40 + m.i48 + m.i56 + m.i64 + m.i72 + m.i80 + m.i88 + m.i96 <= 4)

m.c9 = Constraint(expr=   m.i33 + m.i41 + m.i49 + m.i57 + m.i65 + m.i73 + m.i81 + m.i89 + m.i97 <= 4)

m.c10 = Constraint(expr=   m.x2 - 0.1287*m.x330 + 0.1287*m.x354 >= 0)

m.c11 = Constraint(expr=   m.x3 - 0.19305*m.x331 + 0.19305*m.x354 >= 0)

m.c12 = Constraint(expr=   m.x4 - 0.1287*m.x332 + 0.1287*m.x354 >= 0)

m.c13 = Constraint(expr=   m.x5 - 0.1287*m.x333 + 0.1287*m.x355 >= 0)

m.c14 = Constraint(expr=   m.x6 - 0.19305*m.x334 + 0.19305*m.x355 >= 0)

m.c15 = Constraint(expr=   m.x7 - 0.1287*m.x335 + 0.1287*m.x355 >= 0)

m.c16 = Constraint(expr=   m.x8 - 0.1287*m.x336 + 0.1287*m.x356 >= 0)

m.c17 = Constraint(expr=   m.x9 - 0.19305*m.x337 + 0.19305*m.x356 >= 0)

m.c18 = Constraint(expr=   m.x10 - 0.1287*m.x338 + 0.1287*m.x356 >= 0)

m.c19 = Constraint(expr=   m.x11 - 0.1725*m.x339 + 0.1725*m.x357 >= 0)

m.c20 = Constraint(expr=   m.x12 - 0.22815*m.x340 + 0.22815*m.x357 >= 0)

m.c21 = Constraint(expr=   m.x13 - 0.1521*m.x341 + 0.1521*m.x357 >= 0)

m.c22 = Constraint(expr=   m.x14 - 0.1725*m.x342 + 0.1725*m.x358 >= 0)

m.c23 = Constraint(expr=   m.x15 - 0.22815*m.x343 + 0.22815*m.x358 >= 0)

m.c24 = Constraint(expr=   m.x16 - 0.1521*m.x344 + 0.1521*m.x358 >= 0)

m.c25 = Constraint(expr=   m.x17 - 0.1725*m.x345 + 0.1725*m.x359 >= 0)

m.c26 = Constraint(expr=   m.x18 - 0.22815*m.x346 + 0.22815*m.x359 >= 0)

m.c27 = Constraint(expr=   m.x19 - 0.1521*m.x347 + 0.1521*m.x359 >= 0)

m.c28 = Constraint(expr=   m.x20 - 0.1521*m.x348 + 0.1521*m.x360 >= 0)

m.c29 = Constraint(expr=   m.x21 - 0.19305*m.x349 + 0.19305*m.x360 >= 0)

m.c30 = Constraint(expr=   m.x22 - 0.1521*m.x350 + 0.1521*m.x360 >= 0)

m.c31 = Constraint(expr=   m.x23 - 0.1521*m.x351 + 0.1521*m.x361 >= 0)

m.c32 = Constraint(expr=   m.x24 - 0.19305*m.x352 + 0.19305*m.x361 >= 0)

m.c33 = Constraint(expr=   m.x25 - 0.1521*m.x353 + 0.1521*m.x361 >= 0)

m.c34 = Constraint(expr=   m.b250 + m.b258 + m.b266 + m.b274 + m.b282 + m.b290 + m.b298 + m.b306 + m.b314 <= 2)

m.c35 = Constraint(expr=   m.b251 + m.b259 + m.b267 + m.b275 + m.b283 + m.b291 + m.b299 + m.b307 + m.b315 <= 2)

m.c36 = Constraint(expr=   m.b252 + m.b260 + m.b268 + m.b276 + m.b284 + m.b292 + m.b300 + m.b308 + m.b316 <= 2)

m.c37 = Constraint(expr=   m.b253 + m.b261 + m.b269 + m.b277 + m.b285 + m.b293 + m.b301 + m.b309 + m.b317 <= 2)

m.c38 = Constraint(expr=   m.b254 + m.b262 + m.b270 + m.b278 + m.b286 + m.b294 + m.b302 + m.b310 + m.b318 <= 2)

m.c39 = Constraint(expr=   m.b255 + m.b263 + m.b271 + m.b279 + m.b287 + m.b295 + m.b303 + m.b311 + m.b319 <= 2)

m.c40 = Constraint(expr=   m.b256 + m.b264 + m.b272 + m.b280 + m.b288 + m.b296 + m.b304 + m.b312 + m.b320 <= 2)

m.c41 = Constraint(expr=   m.b257 + m.b265 + m.b273 + m.b281 + m.b289 + m.b297 + m.b305 + m.b313 + m.b321 <= 2)

m.c42 = Constraint(expr=   m.b250 + m.b266 <= 1)

m.c43 = Constraint(expr=   m.b250 + m.b274 <= 1)

m.c44 = Constraint(expr=   m.b250 + m.b282 <= 1)

m.c45 = Constraint(expr=   m.b250 + m.b306 <= 1)

m.c46 = Constraint(expr=   m.b250 + m.b314 <= 1)

m.c47 = Constraint(expr=   m.b258 + m.b266 <= 1)

m.c48 = Constraint(expr=   m.b258 + m.b274 <= 1)

m.c49 = Constraint(expr=   m.b258 + m.b282 <= 1)

m.c50 = Constraint(expr=   m.b258 + m.b306 <= 1)

m.c51 = Constraint(expr=   m.b258 + m.b314 <= 1)

m.c52 = Constraint(expr=   m.b266 + m.b282 <= 1)

m.c53 = Constraint(expr=   m.b266 + m.b290 <= 1)

m.c54 = Constraint(expr=   m.b266 + m.b298 <= 1)

m.c55 = Constraint(expr=   m.b266 + m.b314 <= 1)

m.c56 = Constraint(expr=   m.b274 + m.b282 <= 1)

m.c57 = Constraint(expr=   m.b274 + m.b290 <= 1)

m.c58 = Constraint(expr=   m.b274 + m.b298 <= 1)

m.c59 = Constraint(expr=   m.b274 + m.b314 <= 1)

m.c60 = Constraint(expr=   m.b282 + m.b290 <= 1)

m.c61 = Constraint(expr=   m.b282 + m.b298 <= 1)

m.c62 = Constraint(expr=   m.b282 + m.b306 <= 1)

m.c63 = Constraint(expr=   m.b282 + m.b314 <= 1)

m.c64 = Constraint(expr=   m.b290 + m.b306 <= 1)

m.c65 = Constraint(expr=   m.b290 + m.b314 <= 1)

m.c66 = Constraint(expr=   m.b298 + m.b306 <= 1)

m.c67 = Constraint(expr=   m.b298 + m.b314 <= 1)

m.c68 = Constraint(expr=   m.b306 + m.b314 <= 1)

m.c69 = Constraint(expr=   m.b251 + m.b267 <= 1)

m.c70 = Constraint(expr=   m.b251 + m.b275 <= 1)

m.c71 = Constraint(expr=   m.b251 + m.b283 <= 1)

m.c72 = Constraint(expr=   m.b251 + m.b307 <= 1)

m.c73 = Constraint(expr=   m.b251 + m.b315 <= 1)

m.c74 = Constraint(expr=   m.b259 + m.b267 <= 1)

m.c75 = Constraint(expr=   m.b259 + m.b275 <= 1)

m.c76 = Constraint(expr=   m.b259 + m.b283 <= 1)

m.c77 = Constraint(expr=   m.b259 + m.b307 <= 1)

m.c78 = Constraint(expr=   m.b259 + m.b315 <= 1)

m.c79 = Constraint(expr=   m.b267 + m.b283 <= 1)

m.c80 = Constraint(expr=   m.b267 + m.b291 <= 1)

m.c81 = Constraint(expr=   m.b267 + m.b299 <= 1)

m.c82 = Constraint(expr=   m.b267 + m.b315 <= 1)

m.c83 = Constraint(expr=   m.b275 + m.b283 <= 1)

m.c84 = Constraint(expr=   m.b275 + m.b291 <= 1)

m.c85 = Constraint(expr=   m.b275 + m.b299 <= 1)

m.c86 = Constraint(expr=   m.b275 + m.b315 <= 1)

m.c87 = Constraint(expr=   m.b283 + m.b291 <= 1)

m.c88 = Constraint(expr=   m.b283 + m.b299 <= 1)

m.c89 = Constraint(expr=   m.b283 + m.b307 <= 1)

m.c90 = Constraint(expr=   m.b283 + m.b315 <= 1)

m.c91 = Constraint(expr=   m.b291 + m.b307 <= 1)

m.c92 = Constraint(expr=   m.b291 + m.b315 <= 1)

m.c93 = Constraint(expr=   m.b299 + m.b307 <= 1)

m.c94 = Constraint(expr=   m.b299 + m.b315 <= 1)

m.c95 = Constraint(expr=   m.b307 + m.b315 <= 1)

m.c96 = Constraint(expr=   m.b252 + m.b268 <= 1)

m.c97 = Constraint(expr=   m.b252 + m.b276 <= 1)

m.c98 = Constraint(expr=   m.b252 + m.b284 <= 1)

m.c99 = Constraint(expr=   m.b252 + m.b308 <= 1)

m.c100 = Constraint(expr=   m.b252 + m.b316 <= 1)

m.c101 = Constraint(expr=   m.b260 + m.b268 <= 1)

m.c102 = Constraint(expr=   m.b260 + m.b276 <= 1)

m.c103 = Constraint(expr=   m.b260 + m.b284 <= 1)

m.c104 = Constraint(expr=   m.b260 + m.b308 <= 1)

m.c105 = Constraint(expr=   m.b260 + m.b316 <= 1)

m.c106 = Constraint(expr=   m.b268 + m.b284 <= 1)

m.c107 = Constraint(expr=   m.b268 + m.b292 <= 1)

m.c108 = Constraint(expr=   m.b268 + m.b300 <= 1)

m.c109 = Constraint(expr=   m.b268 + m.b316 <= 1)

m.c110 = Constraint(expr=   m.b276 + m.b284 <= 1)

m.c111 = Constraint(expr=   m.b276 + m.b292 <= 1)

m.c112 = Constraint(expr=   m.b276 + m.b300 <= 1)

m.c113 = Constraint(expr=   m.b276 + m.b316 <= 1)

m.c114 = Constraint(expr=   m.b284 + m.b292 <= 1)

m.c115 = Constraint(expr=   m.b284 + m.b300 <= 1)

m.c116 = Constraint(expr=   m.b284 + m.b308 <= 1)

m.c117 = Constraint(expr=   m.b284 + m.b316 <= 1)

m.c118 = Constraint(expr=   m.b292 + m.b308 <= 1)

m.c119 = Constraint(expr=   m.b292 + m.b316 <= 1)

m.c120 = Constraint(expr=   m.b300 + m.b308 <= 1)

m.c121 = Constraint(expr=   m.b300 + m.b316 <= 1)

m.c122 = Constraint(expr=   m.b308 + m.b316 <= 1)

m.c123 = Constraint(expr=   m.b253 + m.b269 <= 1)

m.c124 = Constraint(expr=   m.b253 + m.b277 <= 1)

m.c125 = Constraint(expr=   m.b253 + m.b285 <= 1)

m.c126 = Constraint(expr=   m.b253 + m.b309 <= 1)

m.c127 = Constraint(expr=   m.b253 + m.b317 <= 1)

m.c128 = Constraint(expr=   m.b261 + m.b269 <= 1)

m.c129 = Constraint(expr=   m.b261 + m.b277 <= 1)

m.c130 = Constraint(expr=   m.b261 + m.b285 <= 1)

m.c131 = Constraint(expr=   m.b261 + m.b309 <= 1)

m.c132 = Constraint(expr=   m.b261 + m.b317 <= 1)

m.c133 = Constraint(expr=   m.b269 + m.b285 <= 1)

m.c134 = Constraint(expr=   m.b269 + m.b293 <= 1)

m.c135 = Constraint(expr=   m.b269 + m.b301 <= 1)

m.c136 = Constraint(expr=   m.b269 + m.b317 <= 1)

m.c137 = Constraint(expr=   m.b277 + m.b285 <= 1)

m.c138 = Constraint(expr=   m.b277 + m.b293 <= 1)

m.c139 = Constraint(expr=   m.b277 + m.b301 <= 1)

m.c140 = Constraint(expr=   m.b277 + m.b317 <= 1)

m.c141 = Constraint(expr=   m.b285 + m.b293 <= 1)

m.c142 = Constraint(expr=   m.b285 + m.b301 <= 1)

m.c143 = Constraint(expr=   m.b285 + m.b309 <= 1)

m.c144 = Constraint(expr=   m.b285 + m.b317 <= 1)

m.c145 = Constraint(expr=   m.b293 + m.b309 <= 1)

m.c146 = Constraint(expr=   m.b293 + m.b317 <= 1)

m.c147 = Constraint(expr=   m.b301 + m.b309 <= 1)

m.c148 = Constraint(expr=   m.b301 + m.b317 <= 1)

m.c149 = Constraint(expr=   m.b309 + m.b317 <= 1)

m.c150 = Constraint(expr=   m.b254 + m.b270 <= 1)

m.c151 = Constraint(expr=   m.b254 + m.b278 <= 1)

m.c152 = Constraint(expr=   m.b254 + m.b286 <= 1)

m.c153 = Constraint(expr=   m.b254 + m.b310 <= 1)

m.c154 = Constraint(expr=   m.b254 + m.b318 <= 1)

m.c155 = Constraint(expr=   m.b262 + m.b270 <= 1)

m.c156 = Constraint(expr=   m.b262 + m.b278 <= 1)

m.c157 = Constraint(expr=   m.b262 + m.b286 <= 1)

m.c158 = Constraint(expr=   m.b262 + m.b310 <= 1)

m.c159 = Constraint(expr=   m.b262 + m.b318 <= 1)

m.c160 = Constraint(expr=   m.b270 + m.b286 <= 1)

m.c161 = Constraint(expr=   m.b270 + m.b294 <= 1)

m.c162 = Constraint(expr=   m.b270 + m.b302 <= 1)

m.c163 = Constraint(expr=   m.b270 + m.b318 <= 1)

m.c164 = Constraint(expr=   m.b278 + m.b286 <= 1)

m.c165 = Constraint(expr=   m.b278 + m.b294 <= 1)

m.c166 = Constraint(expr=   m.b278 + m.b302 <= 1)

m.c167 = Constraint(expr=   m.b278 + m.b318 <= 1)

m.c168 = Constraint(expr=   m.b286 + m.b294 <= 1)

m.c169 = Constraint(expr=   m.b286 + m.b302 <= 1)

m.c170 = Constraint(expr=   m.b286 + m.b310 <= 1)

m.c171 = Constraint(expr=   m.b286 + m.b318 <= 1)

m.c172 = Constraint(expr=   m.b294 + m.b310 <= 1)

m.c173 = Constraint(expr=   m.b294 + m.b318 <= 1)

m.c174 = Constraint(expr=   m.b302 + m.b310 <= 1)

m.c175 = Constraint(expr=   m.b302 + m.b318 <= 1)

m.c176 = Constraint(expr=   m.b310 + m.b318 <= 1)

m.c177 = Constraint(expr=   m.b255 + m.b271 <= 1)

m.c178 = Constraint(expr=   m.b255 + m.b279 <= 1)

m.c179 = Constraint(expr=   m.b255 + m.b287 <= 1)

m.c180 = Constraint(expr=   m.b255 + m.b311 <= 1)

m.c181 = Constraint(expr=   m.b255 + m.b319 <= 1)

m.c182 = Constraint(expr=   m.b263 + m.b271 <= 1)

m.c183 = Constraint(expr=   m.b263 + m.b279 <= 1)

m.c184 = Constraint(expr=   m.b263 + m.b287 <= 1)

m.c185 = Constraint(expr=   m.b263 + m.b311 <= 1)

m.c186 = Constraint(expr=   m.b263 + m.b319 <= 1)

m.c187 = Constraint(expr=   m.b271 + m.b287 <= 1)

m.c188 = Constraint(expr=   m.b271 + m.b295 <= 1)

m.c189 = Constraint(expr=   m.b271 + m.b303 <= 1)

m.c190 = Constraint(expr=   m.b271 + m.b319 <= 1)

m.c191 = Constraint(expr=   m.b279 + m.b287 <= 1)

m.c192 = Constraint(expr=   m.b279 + m.b295 <= 1)

m.c193 = Constraint(expr=   m.b279 + m.b303 <= 1)

m.c194 = Constraint(expr=   m.b279 + m.b319 <= 1)

m.c195 = Constraint(expr=   m.b287 + m.b295 <= 1)

m.c196 = Constraint(expr=   m.b287 + m.b303 <= 1)

m.c197 = Constraint(expr=   m.b287 + m.b311 <= 1)

m.c198 = Constraint(expr=   m.b287 + m.b319 <= 1)

m.c199 = Constraint(expr=   m.b295 + m.b311 <= 1)

m.c200 = Constraint(expr=   m.b295 + m.b319 <= 1)

m.c201 = Constraint(expr=   m.b303 + m.b311 <= 1)

m.c202 = Constraint(expr=   m.b303 + m.b319 <= 1)

m.c203 = Constraint(expr=   m.b311 + m.b319 <= 1)

m.c204 = Constraint(expr=   m.b256 + m.b272 <= 1)

m.c205 = Constraint(expr=   m.b256 + m.b280 <= 1)

m.c206 = Constraint(expr=   m.b256 + m.b288 <= 1)

m.c207 = Constraint(expr=   m.b256 + m.b312 <= 1)

m.c208 = Constraint(expr=   m.b256 + m.b320 <= 1)

m.c209 = Constraint(expr=   m.b264 + m.b272 <= 1)

m.c210 = Constraint(expr=   m.b264 + m.b280 <= 1)

m.c211 = Constraint(expr=   m.b264 + m.b288 <= 1)

m.c212 = Constraint(expr=   m.b264 + m.b312 <= 1)

m.c213 = Constraint(expr=   m.b264 + m.b320 <= 1)

m.c214 = Constraint(expr=   m.b272 + m.b288 <= 1)

m.c215 = Constraint(expr=   m.b272 + m.b296 <= 1)

m.c216 = Constraint(expr=   m.b272 + m.b304 <= 1)

m.c217 = Constraint(expr=   m.b272 + m.b320 <= 1)

m.c218 = Constraint(expr=   m.b280 + m.b288 <= 1)

m.c219 = Constraint(expr=   m.b280 + m.b296 <= 1)

m.c220 = Constraint(expr=   m.b280 + m.b304 <= 1)

m.c221 = Constraint(expr=   m.b280 + m.b320 <= 1)

m.c222 = Constraint(expr=   m.b288 + m.b296 <= 1)

m.c223 = Constraint(expr=   m.b288 + m.b304 <= 1)

m.c224 = Constraint(expr=   m.b288 + m.b312 <= 1)

m.c225 = Constraint(expr=   m.b288 + m.b320 <= 1)

m.c226 = Constraint(expr=   m.b296 + m.b312 <= 1)

m.c227 = Constraint(expr=   m.b296 + m.b320 <= 1)

m.c228 = Constraint(expr=   m.b304 + m.b312 <= 1)

m.c229 = Constraint(expr=   m.b304 + m.b320 <= 1)

m.c230 = Constraint(expr=   m.b312 + m.b320 <= 1)

m.c231 = Constraint(expr=   m.b257 + m.b273 <= 1)

m.c232 = Constraint(expr=   m.b257 + m.b281 <= 1)

m.c233 = Constraint(expr=   m.b257 + m.b289 <= 1)

m.c234 = Constraint(expr=   m.b257 + m.b313 <= 1)

m.c235 = Constraint(expr=   m.b257 + m.b321 <= 1)

m.c236 = Constraint(expr=   m.b265 + m.b273 <= 1)

m.c237 = Constraint(expr=   m.b265 + m.b281 <= 1)

m.c238 = Constraint(expr=   m.b265 + m.b289 <= 1)

m.c239 = Constraint(expr=   m.b265 + m.b313 <= 1)

m.c240 = Constraint(expr=   m.b265 + m.b321 <= 1)

m.c241 = Constraint(expr=   m.b273 + m.b289 <= 1)

m.c242 = Constraint(expr=   m.b273 + m.b297 <= 1)

m.c243 = Constraint(expr=   m.b273 + m.b305 <= 1)

m.c244 = Constraint(expr=   m.b273 + m.b321 <= 1)

m.c245 = Constraint(expr=   m.b281 + m.b289 <= 1)

m.c246 = Constraint(expr=   m.b281 + m.b297 <= 1)

m.c247 = Constraint(expr=   m.b281 + m.b305 <= 1)

m.c248 = Constraint(expr=   m.b281 + m.b321 <= 1)

m.c249 = Constraint(expr=   m.b289 + m.b297 <= 1)

m.c250 = Constraint(expr=   m.b289 + m.b305 <= 1)

m.c251 = Constraint(expr=   m.b289 + m.b313 <= 1)

m.c252 = Constraint(expr=   m.b289 + m.b321 <= 1)

m.c253 = Constraint(expr=   m.b297 + m.b313 <= 1)

m.c254 = Constraint(expr=   m.b297 + m.b321 <= 1)

m.c255 = Constraint(expr=   m.b305 + m.b313 <= 1)

m.c256 = Constraint(expr=   m.b305 + m.b321 <= 1)

m.c257 = Constraint(expr=   m.b313 + m.b321 <= 1)

m.c258 = Constraint(expr=   m.b266 + m.b274 + m.b282 + m.b306 + m.b314 <= 0)

m.c259 = Constraint(expr=   m.b267 + m.b275 + m.b283 + m.b307 + m.b315 <= 0)

m.c260 = Constraint(expr=   m.b268 + m.b276 + m.b284 + m.b308 + m.b316 <= 0)

m.c261 = Constraint(expr=   m.b253 + m.b261 + m.b285 + m.b293 + m.b301 + m.b317 <= 0)

m.c262 = Constraint(expr=   m.b254 + m.b262 + m.b286 + m.b294 + m.b302 + m.b318 <= 0)

m.c263 = Constraint(expr=   m.b255 + m.b263 + m.b287 + m.b295 + m.b303 + m.b319 <= 0)

m.c264 = Constraint(expr=   m.b256 + m.b264 + m.b272 + m.b280 + m.b296 + m.b304 + m.b312 <= 0)

m.c265 = Constraint(expr=   m.b257 + m.b265 + m.b273 + m.b281 + m.b297 + m.b305 + m.b313 <= 0)

m.c266 = Constraint(expr= - 330*m.i26 - 260*m.i34 - 480*m.i42 - 440*m.i50 - 711*m.i58 - 350*m.i66 - 300*m.i74
                          - 450*m.i82 - 450*m.i90 + 1000*m.b98 + 1100*m.b122 + 1200*m.b146 + 1300*m.b170 + 1400*m.b194
                          + 1500*m.b218 - 200*m.x242 <= 0)

m.c267 = Constraint(expr= - 330*m.i26 - 260*m.i34 - 480*m.i42 - 440*m.i50 - 711*m.i58 - 350*m.i66 - 300*m.i74
                          - 450*m.i82 - 450*m.i90 + 1000*m.b106 + 1100*m.b130 + 1200*m.b154 + 1300*m.b178 + 1400*m.b202
                          + 1500*m.b226 - 200*m.x242 <= 0)

m.c268 = Constraint(expr= - 330*m.i26 - 260*m.i34 - 480*m.i42 - 440*m.i50 - 711*m.i58 - 350*m.i66 - 300*m.i74
                          - 450*m.i82 - 450*m.i90 + 1000*m.b114 + 1100*m.b138 + 1200*m.b162 + 1300*m.b186 + 1400*m.b210
                          + 1500*m.b234 - 200*m.x242 <= 0)

m.c269 = Constraint(expr= - 330*m.i27 - 260*m.i35 - 480*m.i43 - 440*m.i51 - 711*m.i59 - 350*m.i67 - 300*m.i75
                          - 450*m.i83 - 450*m.i91 + 1000*m.b99 + 1100*m.b123 + 1200*m.b147 + 1300*m.b171 + 1400*m.b195
                          + 1500*m.b219 - 200*m.x243 <= 0)

m.c270 = Constraint(expr= - 330*m.i27 - 260*m.i35 - 480*m.i43 - 440*m.i51 - 711*m.i59 - 350*m.i67 - 300*m.i75
                          - 450*m.i83 - 450*m.i91 + 1000*m.b107 + 1100*m.b131 + 1200*m.b155 + 1300*m.b179 + 1400*m.b203
                          + 1500*m.b227 - 200*m.x243 <= 0)

m.c271 = Constraint(expr= - 330*m.i27 - 260*m.i35 - 480*m.i43 - 440*m.i51 - 711*m.i59 - 350*m.i67 - 300*m.i75
                          - 450*m.i83 - 450*m.i91 + 1000*m.b115 + 1100*m.b139 + 1200*m.b163 + 1300*m.b187 + 1400*m.b211
                          + 1500*m.b235 - 200*m.x243 <= 0)

m.c272 = Constraint(expr= - 330*m.i28 - 260*m.i36 - 480*m.i44 - 440*m.i52 - 711*m.i60 - 350*m.i68 - 300*m.i76
                          - 450*m.i84 - 450*m.i92 + 1000*m.b100 + 1100*m.b124 + 1200*m.b148 + 1300*m.b172 + 1400*m.b196
                          + 1500*m.b220 - 200*m.x244 <= 0)

m.c273 = Constraint(expr= - 330*m.i28 - 260*m.i36 - 480*m.i44 - 440*m.i52 - 711*m.i60 - 350*m.i68 - 300*m.i76
                          - 450*m.i84 - 450*m.i92 + 1000*m.b108 + 1100*m.b132 + 1200*m.b156 + 1300*m.b180 + 1400*m.b204
                          + 1500*m.b228 - 200*m.x244 <= 0)

m.c274 = Constraint(expr= - 330*m.i28 - 260*m.i36 - 480*m.i44 - 440*m.i52 - 711*m.i60 - 350*m.i68 - 300*m.i76
                          - 450*m.i84 - 450*m.i92 + 1000*m.b116 + 1100*m.b140 + 1200*m.b164 + 1300*m.b188 + 1400*m.b212
                          + 1500*m.b236 - 200*m.x244 <= 0)

m.c275 = Constraint(expr= - 330*m.i29 - 260*m.i37 - 480*m.i45 - 440*m.i53 - 711*m.i61 - 350*m.i69 - 300*m.i77
                          - 450*m.i85 - 450*m.i93 + 1000*m.b101 + 1100*m.b125 + 1200*m.b149 + 1300*m.b173 + 1400*m.b197
                          + 1500*m.b221 - 200*m.x245 <= 0)

m.c276 = Constraint(expr= - 330*m.i29 - 260*m.i37 - 480*m.i45 - 440*m.i53 - 711*m.i61 - 350*m.i69 - 300*m.i77
                          - 450*m.i85 - 450*m.i93 + 1000*m.b109 + 1100*m.b133 + 1200*m.b157 + 1300*m.b181 + 1400*m.b205
                          + 1500*m.b229 - 200*m.x245 <= 0)

m.c277 = Constraint(expr= - 330*m.i29 - 260*m.i37 - 480*m.i45 - 440*m.i53 - 711*m.i61 - 350*m.i69 - 300*m.i77
                          - 450*m.i85 - 450*m.i93 + 1000*m.b117 + 1100*m.b141 + 1200*m.b165 + 1300*m.b189 + 1400*m.b213
                          + 1500*m.b237 - 200*m.x245 <= 0)

m.c278 = Constraint(expr= - 330*m.i30 - 260*m.i38 - 480*m.i46 - 440*m.i54 - 711*m.i62 - 350*m.i70 - 300*m.i78
                          - 450*m.i86 - 450*m.i94 + 1000*m.b102 + 1100*m.b126 + 1200*m.b150 + 1300*m.b174 + 1400*m.b198
                          + 1500*m.b222 - 200*m.x246 <= 0)

m.c279 = Constraint(expr= - 330*m.i30 - 260*m.i38 - 480*m.i46 - 440*m.i54 - 711*m.i62 - 350*m.i70 - 300*m.i78
                          - 450*m.i86 - 450*m.i94 + 1000*m.b110 + 1100*m.b134 + 1200*m.b158 + 1300*m.b182 + 1400*m.b206
                          + 1500*m.b230 - 200*m.x246 <= 0)

m.c280 = Constraint(expr= - 330*m.i30 - 260*m.i38 - 480*m.i46 - 440*m.i54 - 711*m.i62 - 350*m.i70 - 300*m.i78
                          - 450*m.i86 - 450*m.i94 + 1000*m.b118 + 1100*m.b142 + 1200*m.b166 + 1300*m.b190 + 1400*m.b214
                          + 1500*m.b238 - 200*m.x246 <= 0)

m.c281 = Constraint(expr= - 330*m.i31 - 260*m.i39 - 480*m.i47 - 440*m.i55 - 711*m.i63 - 350*m.i71 - 300*m.i79
                          - 450*m.i87 - 450*m.i95 + 1000*m.b103 + 1100*m.b127 + 1200*m.b151 + 1300*m.b175 + 1400*m.b199
                          + 1500*m.b223 - 200*m.x247 <= 0)

m.c282 = Constraint(expr= - 330*m.i31 - 260*m.i39 - 480*m.i47 - 440*m.i55 - 711*m.i63 - 350*m.i71 - 300*m.i79
                          - 450*m.i87 - 450*m.i95 + 1000*m.b111 + 1100*m.b135 + 1200*m.b159 + 1300*m.b183 + 1400*m.b207
                          + 1500*m.b231 - 200*m.x247 <= 0)

m.c283 = Constraint(expr= - 330*m.i31 - 260*m.i39 - 480*m.i47 - 440*m.i55 - 711*m.i63 - 350*m.i71 - 300*m.i79
                          - 450*m.i87 - 450*m.i95 + 1000*m.b119 + 1100*m.b143 + 1200*m.b167 + 1300*m.b191 + 1400*m.b215
                          + 1500*m.b239 - 200*m.x247 <= 0)

m.c284 = Constraint(expr= - 330*m.i32 - 260*m.i40 - 480*m.i48 - 440*m.i56 - 711*m.i64 - 350*m.i72 - 300*m.i80
                          - 450*m.i88 - 450*m.i96 + 1000*m.b104 + 1100*m.b128 + 1200*m.b152 + 1300*m.b176 + 1400*m.b200
                          + 1500*m.b224 - 200*m.x248 <= 0)

m.c285 = Constraint(expr= - 330*m.i32 - 260*m.i40 - 480*m.i48 - 440*m.i56 - 711*m.i64 - 350*m.i72 - 300*m.i80
                          - 450*m.i88 - 450*m.i96 + 1000*m.b112 + 1100*m.b136 + 1200*m.b160 + 1300*m.b184 + 1400*m.b208
                          + 1500*m.b232 - 200*m.x248 <= 0)

m.c286 = Constraint(expr= - 330*m.i32 - 260*m.i40 - 480*m.i48 - 440*m.i56 - 711*m.i64 - 350*m.i72 - 300*m.i80
                          - 450*m.i88 - 450*m.i96 + 1000*m.b120 + 1100*m.b144 + 1200*m.b168 + 1300*m.b192 + 1400*m.b216
                          + 1500*m.b240 - 200*m.x248 <= 0)

m.c287 = Constraint(expr= - 330*m.i33 - 260*m.i41 - 480*m.i49 - 440*m.i57 - 711*m.i65 - 350*m.i73 - 300*m.i81
                          - 450*m.i89 - 450*m.i97 + 1000*m.b105 + 1100*m.b129 + 1200*m.b153 + 1300*m.b177 + 1400*m.b201
                          + 1500*m.b225 - 200*m.x249 <= 0)

m.c288 = Constraint(expr= - 330*m.i33 - 260*m.i41 - 480*m.i49 - 440*m.i57 - 711*m.i65 - 350*m.i73 - 300*m.i81
                          - 450*m.i89 - 450*m.i97 + 1000*m.b113 + 1100*m.b137 + 1200*m.b161 + 1300*m.b185 + 1400*m.b209
                          + 1500*m.b233 - 200*m.x249 <= 0)

m.c289 = Constraint(expr= - 330*m.i33 - 260*m.i41 - 480*m.i49 - 440*m.i57 - 711*m.i65 - 350*m.i73 - 300*m.i81
                          - 450*m.i89 - 450*m.i97 + 1000*m.b121 + 1100*m.b145 + 1200*m.b169 + 1300*m.b193 + 1400*m.b217
                          + 1500*m.b241 - 200*m.x249 <= 0)

m.c290 = Constraint(expr= - 330*m.i26 - 260*m.i34 - 480*m.i42 - 440*m.i50 - 711*m.i58 - 350*m.i66 - 300*m.i74
                          - 450*m.i82 - 450*m.i90 + 1000*m.b98 + 1100*m.b122 + 1200*m.b146 + 1300*m.b170 + 1400*m.b194
                          + 1500*m.b218 - 20*m.x242 >= 0)

m.c291 = Constraint(expr= - 330*m.i26 - 260*m.i34 - 480*m.i42 - 440*m.i50 - 711*m.i58 - 350*m.i66 - 300*m.i74
                          - 450*m.i82 - 450*m.i90 + 1000*m.b106 + 1100*m.b130 + 1200*m.b154 + 1300*m.b178 + 1400*m.b202
                          + 1500*m.b226 - 20*m.x242 >= 0)

m.c292 = Constraint(expr= - 330*m.i26 - 260*m.i34 - 480*m.i42 - 440*m.i50 - 711*m.i58 - 350*m.i66 - 300*m.i74
                          - 450*m.i82 - 450*m.i90 + 1000*m.b114 + 1100*m.b138 + 1200*m.b162 + 1300*m.b186 + 1400*m.b210
                          + 1500*m.b234 - 20*m.x242 >= 0)

m.c293 = Constraint(expr= - 330*m.i27 - 260*m.i35 - 480*m.i43 - 440*m.i51 - 711*m.i59 - 350*m.i67 - 300*m.i75
                          - 450*m.i83 - 450*m.i91 + 1000*m.b99 + 1100*m.b123 + 1200*m.b147 + 1300*m.b171 + 1400*m.b195
                          + 1500*m.b219 - 20*m.x243 >= 0)

m.c294 = Constraint(expr= - 330*m.i27 - 260*m.i35 - 480*m.i43 - 440*m.i51 - 711*m.i59 - 350*m.i67 - 300*m.i75
                          - 450*m.i83 - 450*m.i91 + 1000*m.b107 + 1100*m.b131 + 1200*m.b155 + 1300*m.b179 + 1400*m.b203
                          + 1500*m.b227 - 20*m.x243 >= 0)

m.c295 = Constraint(expr= - 330*m.i27 - 260*m.i35 - 480*m.i43 - 440*m.i51 - 711*m.i59 - 350*m.i67 - 300*m.i75
                          - 450*m.i83 - 450*m.i91 + 1000*m.b115 + 1100*m.b139 + 1200*m.b163 + 1300*m.b187 + 1400*m.b211
                          + 1500*m.b235 - 20*m.x243 >= 0)

m.c296 = Constraint(expr= - 330*m.i28 - 260*m.i36 - 480*m.i44 - 440*m.i52 - 711*m.i60 - 350*m.i68 - 300*m.i76
                          - 450*m.i84 - 450*m.i92 + 1000*m.b100 + 1100*m.b124 + 1200*m.b148 + 1300*m.b172 + 1400*m.b196
                          + 1500*m.b220 - 20*m.x244 >= 0)

m.c297 = Constraint(expr= - 330*m.i28 - 260*m.i36 - 480*m.i44 - 440*m.i52 - 711*m.i60 - 350*m.i68 - 300*m.i76
                          - 450*m.i84 - 450*m.i92 + 1000*m.b108 + 1100*m.b132 + 1200*m.b156 + 1300*m.b180 + 1400*m.b204
                          + 1500*m.b228 - 20*m.x244 >= 0)

m.c298 = Constraint(expr= - 330*m.i28 - 260*m.i36 - 480*m.i44 - 440*m.i52 - 711*m.i60 - 350*m.i68 - 300*m.i76
                          - 450*m.i84 - 450*m.i92 + 1000*m.b116 + 1100*m.b140 + 1200*m.b164 + 1300*m.b188 + 1400*m.b212
                          + 1500*m.b236 - 20*m.x244 >= 0)

m.c299 = Constraint(expr= - 330*m.i29 - 260*m.i37 - 480*m.i45 - 440*m.i53 - 711*m.i61 - 350*m.i69 - 300*m.i77
                          - 450*m.i85 - 450*m.i93 + 1000*m.b101 + 1100*m.b125 + 1200*m.b149 + 1300*m.b173 + 1400*m.b197
                          + 1500*m.b221 - 20*m.x245 >= 0)

m.c300 = Constraint(expr= - 330*m.i29 - 260*m.i37 - 480*m.i45 - 440*m.i53 - 711*m.i61 - 350*m.i69 - 300*m.i77
                          - 450*m.i85 - 450*m.i93 + 1000*m.b109 + 1100*m.b133 + 1200*m.b157 + 1300*m.b181 + 1400*m.b205
                          + 1500*m.b229 - 20*m.x245 >= 0)

m.c301 = Constraint(expr= - 330*m.i29 - 260*m.i37 - 480*m.i45 - 440*m.i53 - 711*m.i61 - 350*m.i69 - 300*m.i77
                          - 450*m.i85 - 450*m.i93 + 1000*m.b117 + 1100*m.b141 + 1200*m.b165 + 1300*m.b189 + 1400*m.b213
                          + 1500*m.b237 - 20*m.x245 >= 0)

m.c302 = Constraint(expr= - 330*m.i30 - 260*m.i38 - 480*m.i46 - 440*m.i54 - 711*m.i62 - 350*m.i70 - 300*m.i78
                          - 450*m.i86 - 450*m.i94 + 1000*m.b102 + 1100*m.b126 + 1200*m.b150 + 1300*m.b174 + 1400*m.b198
                          + 1500*m.b222 - 20*m.x246 >= 0)

m.c303 = Constraint(expr= - 330*m.i30 - 260*m.i38 - 480*m.i46 - 440*m.i54 - 711*m.i62 - 350*m.i70 - 300*m.i78
                          - 450*m.i86 - 450*m.i94 + 1000*m.b110 + 1100*m.b134 + 1200*m.b158 + 1300*m.b182 + 1400*m.b206
                          + 1500*m.b230 - 20*m.x246 >= 0)

m.c304 = Constraint(expr= - 330*m.i30 - 260*m.i38 - 480*m.i46 - 440*m.i54 - 711*m.i62 - 350*m.i70 - 300*m.i78
                          - 450*m.i86 - 450*m.i94 + 1000*m.b118 + 1100*m.b142 + 1200*m.b166 + 1300*m.b190 + 1400*m.b214
                          + 1500*m.b238 - 20*m.x246 >= 0)

m.c305 = Constraint(expr= - 330*m.i31 - 260*m.i39 - 480*m.i47 - 440*m.i55 - 711*m.i63 - 350*m.i71 - 300*m.i79
                          - 450*m.i87 - 450*m.i95 + 1000*m.b103 + 1100*m.b127 + 1200*m.b151 + 1300*m.b175 + 1400*m.b199
                          + 1500*m.b223 - 20*m.x247 >= 0)

m.c306 = Constraint(expr= - 330*m.i31 - 260*m.i39 - 480*m.i47 - 440*m.i55 - 711*m.i63 - 350*m.i71 - 300*m.i79
                          - 450*m.i87 - 450*m.i95 + 1000*m.b111 + 1100*m.b135 + 1200*m.b159 + 1300*m.b183 + 1400*m.b207
                          + 1500*m.b231 - 20*m.x247 >= 0)

m.c307 = Constraint(expr= - 330*m.i31 - 260*m.i39 - 480*m.i47 - 440*m.i55 - 711*m.i63 - 350*m.i71 - 300*m.i79
                          - 450*m.i87 - 450*m.i95 + 1000*m.b119 + 1100*m.b143 + 1200*m.b167 + 1300*m.b191 + 1400*m.b215
                          + 1500*m.b239 - 20*m.x247 >= 0)

m.c308 = Constraint(expr= - 330*m.i32 - 260*m.i40 - 480*m.i48 - 440*m.i56 - 711*m.i64 - 350*m.i72 - 300*m.i80
                          - 450*m.i88 - 450*m.i96 + 1000*m.b104 + 1100*m.b128 + 1200*m.b152 + 1300*m.b176 + 1400*m.b200
                          + 1500*m.b224 - 20*m.x248 >= 0)

m.c309 = Constraint(expr= - 330*m.i32 - 260*m.i40 - 480*m.i48 - 440*m.i56 - 711*m.i64 - 350*m.i72 - 300*m.i80
                          - 450*m.i88 - 450*m.i96 + 1000*m.b112 + 1100*m.b136 + 1200*m.b160 + 1300*m.b184 + 1400*m.b208
                          + 1500*m.b232 - 20*m.x248 >= 0)

m.c310 = Constraint(expr= - 330*m.i32 - 260*m.i40 - 480*m.i48 - 440*m.i56 - 711*m.i64 - 350*m.i72 - 300*m.i80
                          - 450*m.i88 - 450*m.i96 + 1000*m.b120 + 1100*m.b144 + 1200*m.b168 + 1300*m.b192 + 1400*m.b216
                          + 1500*m.b240 - 20*m.x248 >= 0)

m.c311 = Constraint(expr= - 330*m.i33 - 260*m.i41 - 480*m.i49 - 440*m.i57 - 711*m.i65 - 350*m.i73 - 300*m.i81
                          - 450*m.i89 - 450*m.i97 + 1000*m.b105 + 1100*m.b129 + 1200*m.b153 + 1300*m.b177 + 1400*m.b201
                          + 1500*m.b225 - 20*m.x249 >= 0)

m.c312 = Constraint(expr= - 330*m.i33 - 260*m.i41 - 480*m.i49 - 440*m.i57 - 711*m.i65 - 350*m.i73 - 300*m.i81
                          - 450*m.i89 - 450*m.i97 + 1000*m.b113 + 1100*m.b137 + 1200*m.b161 + 1300*m.b185 + 1400*m.b209
                          + 1500*m.b233 - 20*m.x249 >= 0)

m.c313 = Constraint(expr= - 330*m.i33 - 260*m.i41 - 480*m.i49 - 440*m.i57 - 711*m.i65 - 350*m.i73 - 300*m.i81
                          - 450*m.i89 - 450*m.i97 + 1000*m.b121 + 1100*m.b145 + 1200*m.b169 + 1300*m.b193 + 1400*m.b217
                          + 1500*m.b241 - 20*m.x249 >= 0)

m.c314 = Constraint(expr=   m.b98 + m.b122 + m.b146 + m.b170 + m.b194 + m.b218 - m.b250 - m.b258 - m.b266 - m.b274
                          - m.b282 - m.b290 - m.b298 - m.b306 - m.b314 <= 0)

m.c315 = Constraint(expr=   m.b106 + m.b130 + m.b154 + m.b178 + m.b202 + m.b226 - m.b250 - m.b258 - m.b266 - m.b274
                          - m.b282 - m.b290 - m.b298 - m.b306 - m.b314 <= 0)

m.c316 = Constraint(expr=   m.b114 + m.b138 + m.b162 + m.b186 + m.b210 + m.b234 - m.b250 - m.b258 - m.b266 - m.b274
                          - m.b282 - m.b290 - m.b298 - m.b306 - m.b314 <= 0)

m.c317 = Constraint(expr=   m.b99 + m.b123 + m.b147 + m.b171 + m.b195 + m.b219 - m.b251 - m.b259 - m.b267 - m.b275
                          - m.b283 - m.b291 - m.b299 - m.b307 - m.b315 <= 0)

m.c318 = Constraint(expr=   m.b107 + m.b131 + m.b155 + m.b179 + m.b203 + m.b227 - m.b251 - m.b259 - m.b267 - m.b275
                          - m.b283 - m.b291 - m.b299 - m.b307 - m.b315 <= 0)

m.c319 = Constraint(expr=   m.b115 + m.b139 + m.b163 + m.b187 + m.b211 + m.b235 - m.b251 - m.b259 - m.b267 - m.b275
                          - m.b283 - m.b291 - m.b299 - m.b307 - m.b315 <= 0)

m.c320 = Constraint(expr=   m.b100 + m.b124 + m.b148 + m.b172 + m.b196 + m.b220 - m.b252 - m.b260 - m.b268 - m.b276
                          - m.b284 - m.b292 - m.b300 - m.b308 - m.b316 <= 0)

m.c321 = Constraint(expr=   m.b108 + m.b132 + m.b156 + m.b180 + m.b204 + m.b228 - m.b252 - m.b260 - m.b268 - m.b276
                          - m.b284 - m.b292 - m.b300 - m.b308 - m.b316 <= 0)

m.c322 = Constraint(expr=   m.b116 + m.b140 + m.b164 + m.b188 + m.b212 + m.b236 - m.b252 - m.b260 - m.b268 - m.b276
                          - m.b284 - m.b292 - m.b300 - m.b308 - m.b316 <= 0)

m.c323 = Constraint(expr=   m.b101 + m.b125 + m.b149 + m.b173 + m.b197 + m.b221 - m.b253 - m.b261 - m.b269 - m.b277
                          - m.b285 - m.b293 - m.b301 - m.b309 - m.b317 <= 0)

m.c324 = Constraint(expr=   m.b109 + m.b133 + m.b157 + m.b181 + m.b205 + m.b229 - m.b253 - m.b261 - m.b269 - m.b277
                          - m.b285 - m.b293 - m.b301 - m.b309 - m.b317 <= 0)

m.c325 = Constraint(expr=   m.b117 + m.b141 + m.b165 + m.b189 + m.b213 + m.b237 - m.b253 - m.b261 - m.b269 - m.b277
                          - m.b285 - m.b293 - m.b301 - m.b309 - m.b317 <= 0)

m.c326 = Constraint(expr=   m.b102 + m.b126 + m.b150 + m.b174 + m.b198 + m.b222 - m.b254 - m.b262 - m.b270 - m.b278
                          - m.b286 - m.b294 - m.b302 - m.b310 - m.b318 <= 0)

m.c327 = Constraint(expr=   m.b110 + m.b134 + m.b158 + m.b182 + m.b206 + m.b230 - m.b254 - m.b262 - m.b270 - m.b278
                          - m.b286 - m.b294 - m.b302 - m.b310 - m.b318 <= 0)

m.c328 = Constraint(expr=   m.b118 + m.b142 + m.b166 + m.b190 + m.b214 + m.b238 - m.b254 - m.b262 - m.b270 - m.b278
                          - m.b286 - m.b294 - m.b302 - m.b310 - m.b318 <= 0)

m.c329 = Constraint(expr=   m.b103 + m.b127 + m.b151 + m.b175 + m.b199 + m.b223 - m.b255 - m.b263 - m.b271 - m.b279
                          - m.b287 - m.b295 - m.b303 - m.b311 - m.b319 <= 0)

m.c330 = Constraint(expr=   m.b111 + m.b135 + m.b159 + m.b183 + m.b207 + m.b231 - m.b255 - m.b263 - m.b271 - m.b279
                          - m.b287 - m.b295 - m.b303 - m.b311 - m.b319 <= 0)

m.c331 = Constraint(expr=   m.b119 + m.b143 + m.b167 + m.b191 + m.b215 + m.b239 - m.b255 - m.b263 - m.b271 - m.b279
                          - m.b287 - m.b295 - m.b303 - m.b311 - m.b319 <= 0)

m.c332 = Constraint(expr=   m.b104 + m.b128 + m.b152 + m.b176 + m.b200 + m.b224 - m.b256 - m.b264 - m.b272 - m.b280
                          - m.b288 - m.b296 - m.b304 - m.b312 - m.b320 <= 0)

m.c333 = Constraint(expr=   m.b112 + m.b136 + m.b160 + m.b184 + m.b208 + m.b232 - m.b256 - m.b264 - m.b272 - m.b280
                          - m.b288 - m.b296 - m.b304 - m.b312 - m.b320 <= 0)

m.c334 = Constraint(expr=   m.b120 + m.b144 + m.b168 + m.b192 + m.b216 + m.b240 - m.b256 - m.b264 - m.b272 - m.b280
                          - m.b288 - m.b296 - m.b304 - m.b312 - m.b320 <= 0)

m.c335 = Constraint(expr=   m.b105 + m.b129 + m.b153 + m.b177 + m.b201 + m.b225 - m.b257 - m.b265 - m.b273 - m.b281
                          - m.b289 - m.b297 - m.b305 - m.b313 - m.b321 <= 0)

m.c336 = Constraint(expr=   m.b113 + m.b137 + m.b161 + m.b185 + m.b209 + m.b233 - m.b257 - m.b265 - m.b273 - m.b281
                          - m.b289 - m.b297 - m.b305 - m.b313 - m.b321 <= 0)

m.c337 = Constraint(expr=   m.b121 + m.b145 + m.b169 + m.b193 + m.b217 + m.b241 - m.b257 - m.b265 - m.b273 - m.b281
                          - m.b289 - m.b297 - m.b305 - m.b313 - m.b321 <= 0)

m.c338 = Constraint(expr=   m.b98 + m.b122 + m.b146 + m.b170 + m.b194 + m.b218 <= 1)

m.c339 = Constraint(expr=   m.b106 + m.b130 + m.b154 + m.b178 + m.b202 + m.b226 <= 1)

m.c340 = Constraint(expr=   m.b114 + m.b138 + m.b162 + m.b186 + m.b210 + m.b234 <= 1)

m.c341 = Constraint(expr=   m.b99 + m.b123 + m.b147 + m.b171 + m.b195 + m.b219 <= 1)

m.c342 = Constraint(expr=   m.b107 + m.b131 + m.b155 + m.b179 + m.b203 + m.b227 <= 1)

m.c343 = Constraint(expr=   m.b115 + m.b139 + m.b163 + m.b187 + m.b211 + m.b235 <= 1)

m.c344 = Constraint(expr=   m.b100 + m.b124 + m.b148 + m.b172 + m.b196 + m.b220 <= 1)

m.c345 = Constraint(expr=   m.b108 + m.b132 + m.b156 + m.b180 + m.b204 + m.b228 <= 1)

m.c346 = Constraint(expr=   m.b116 + m.b140 + m.b164 + m.b188 + m.b212 + m.b236 <= 1)

m.c347 = Constraint(expr=   m.b101 + m.b125 + m.b149 + m.b173 + m.b197 + m.b221 <= 1)

m.c348 = Constraint(expr=   m.b109 + m.b133 + m.b157 + m.b181 + m.b205 + m.b229 <= 1)

m.c349 = Constraint(expr=   m.b117 + m.b141 + m.b165 + m.b189 + m.b213 + m.b237 <= 1)

m.c350 = Constraint(expr=   m.b102 + m.b126 + m.b150 + m.b174 + m.b198 + m.b222 <= 1)

m.c351 = Constraint(expr=   m.b110 + m.b134 + m.b158 + m.b182 + m.b206 + m.b230 <= 1)

m.c352 = Constraint(expr=   m.b118 + m.b142 + m.b166 + m.b190 + m.b214 + m.b238 <= 1)

m.c353 = Constraint(expr=   m.b103 + m.b127 + m.b151 + m.b175 + m.b199 + m.b223 <= 1)

m.c354 = Constraint(expr=   m.b111 + m.b135 + m.b159 + m.b183 + m.b207 + m.b231 <= 1)

m.c355 = Constraint(expr=   m.b119 + m.b143 + m.b167 + m.b191 + m.b215 + m.b239 <= 1)

m.c356 = Constraint(expr=   m.b104 + m.b128 + m.b152 + m.b176 + m.b200 + m.b224 <= 1)

m.c357 = Constraint(expr=   m.b112 + m.b136 + m.b160 + m.b184 + m.b208 + m.b232 <= 1)

m.c358 = Constraint(expr=   m.b120 + m.b144 + m.b168 + m.b192 + m.b216 + m.b240 <= 1)

m.c359 = Constraint(expr=   m.b105 + m.b129 + m.b153 + m.b177 + m.b201 + m.b225 <= 1)

m.c360 = Constraint(expr=   m.b113 + m.b137 + m.b161 + m.b185 + m.b209 + m.b233 <= 1)

m.c361 = Constraint(expr=   m.b121 + m.b145 + m.b169 + m.b193 + m.b217 + m.b241 <= 1)

m.c362 = Constraint(expr=   m.b98 + m.b122 + m.b146 + m.b170 + m.b194 + m.b218 - m.x242 >= 0)

m.c363 = Constraint(expr=   m.b98 + m.b122 + m.b146 + m.b170 + m.b194 + m.b218 - m.x242 >= 0)

m.c364 = Constraint(expr=   m.b98 + m.b122 + m.b146 + m.b170 + m.b194 + m.b218 - m.x242 >= 0)

m.c365 = Constraint(expr=   m.b98 + m.b122 + m.b146 + m.b170 + m.b194 + m.b218 - m.x242 >= 0)

m.c366 = Constraint(expr=   m.b98 + m.b122 + m.b146 + m.b170 + m.b194 + m.b218 - m.x242 >= 0)

m.c367 = Constraint(expr=   m.b98 + m.b122 + m.b146 + m.b170 + m.b194 + m.b218 - m.x242 >= 0)

m.c368 = Constraint(expr=   m.b98 + m.b122 + m.b146 + m.b170 + m.b194 + m.b218 - m.x242 >= 0)

m.c369 = Constraint(expr=   m.b98 + m.b122 + m.b146 + m.b170 + m.b194 + m.b218 - m.x242 >= 0)

m.c370 = Constraint(expr=   m.b98 + m.b122 + m.b146 + m.b170 + m.b194 + m.b218 - m.x242 >= 0)

m.c371 = Constraint(expr=   m.b106 + m.b130 + m.b154 + m.b178 + m.b202 + m.b226 - m.x242 >= 0)

m.c372 = Constraint(expr=   m.b106 + m.b130 + m.b154 + m.b178 + m.b202 + m.b226 - m.x242 >= 0)

m.c373 = Constraint(expr=   m.b106 + m.b130 + m.b154 + m.b178 + m.b202 + m.b226 - m.x242 >= 0)

m.c374 = Constraint(expr=   m.b106 + m.b130 + m.b154 + m.b178 + m.b202 + m.b226 - m.x242 >= 0)

m.c375 = Constraint(expr=   m.b106 + m.b130 + m.b154 + m.b178 + m.b202 + m.b226 - m.x242 >= 0)

m.c376 = Constraint(expr=   m.b106 + m.b130 + m.b154 + m.b178 + m.b202 + m.b226 - m.x242 >= 0)

m.c377 = Constraint(expr=   m.b106 + m.b130 + m.b154 + m.b178 + m.b202 + m.b226 - m.x242 >= 0)

m.c378 = Constraint(expr=   m.b106 + m.b130 + m.b154 + m.b178 + m.b202 + m.b226 - m.x242 >= 0)

m.c379 = Constraint(expr=   m.b106 + m.b130 + m.b154 + m.b178 + m.b202 + m.b226 - m.x242 >= 0)

m.c380 = Constraint(expr=   m.b114 + m.b138 + m.b162 + m.b186 + m.b210 + m.b234 - m.x242 >= 0)

m.c381 = Constraint(expr=   m.b114 + m.b138 + m.b162 + m.b186 + m.b210 + m.b234 - m.x242 >= 0)

m.c382 = Constraint(expr=   m.b114 + m.b138 + m.b162 + m.b186 + m.b210 + m.b234 - m.x242 >= 0)

m.c383 = Constraint(expr=   m.b114 + m.b138 + m.b162 + m.b186 + m.b210 + m.b234 - m.x242 >= 0)

m.c384 = Constraint(expr=   m.b114 + m.b138 + m.b162 + m.b186 + m.b210 + m.b234 - m.x242 >= 0)

m.c385 = Constraint(expr=   m.b114 + m.b138 + m.b162 + m.b186 + m.b210 + m.b234 - m.x242 >= 0)

m.c386 = Constraint(expr=   m.b114 + m.b138 + m.b162 + m.b186 + m.b210 + m.b234 - m.x242 >= 0)

m.c387 = Constraint(expr=   m.b114 + m.b138 + m.b162 + m.b186 + m.b210 + m.b234 - m.x242 >= 0)

m.c388 = Constraint(expr=   m.b114 + m.b138 + m.b162 + m.b186 + m.b210 + m.b234 - m.x242 >= 0)

m.c389 = Constraint(expr=   m.b99 + m.b123 + m.b147 + m.b171 + m.b195 + m.b219 - m.x243 >= 0)

m.c390 = Constraint(expr=   m.b99 + m.b123 + m.b147 + m.b171 + m.b195 + m.b219 - m.x243 >= 0)

m.c391 = Constraint(expr=   m.b99 + m.b123 + m.b147 + m.b171 + m.b195 + m.b219 - m.x243 >= 0)

m.c392 = Constraint(expr=   m.b99 + m.b123 + m.b147 + m.b171 + m.b195 + m.b219 - m.x243 >= 0)

m.c393 = Constraint(expr=   m.b99 + m.b123 + m.b147 + m.b171 + m.b195 + m.b219 - m.x243 >= 0)

m.c394 = Constraint(expr=   m.b99 + m.b123 + m.b147 + m.b171 + m.b195 + m.b219 - m.x243 >= 0)

m.c395 = Constraint(expr=   m.b99 + m.b123 + m.b147 + m.b171 + m.b195 + m.b219 - m.x243 >= 0)

m.c396 = Constraint(expr=   m.b99 + m.b123 + m.b147 + m.b171 + m.b195 + m.b219 - m.x243 >= 0)

m.c397 = Constraint(expr=   m.b99 + m.b123 + m.b147 + m.b171 + m.b195 + m.b219 - m.x243 >= 0)

m.c398 = Constraint(expr=   m.b107 + m.b131 + m.b155 + m.b179 + m.b203 + m.b227 - m.x243 >= 0)

m.c399 = Constraint(expr=   m.b107 + m.b131 + m.b155 + m.b179 + m.b203 + m.b227 - m.x243 >= 0)

m.c400 = Constraint(expr=   m.b107 + m.b131 + m.b155 + m.b179 + m.b203 + m.b227 - m.x243 >= 0)

m.c401 = Constraint(expr=   m.b107 + m.b131 + m.b155 + m.b179 + m.b203 + m.b227 - m.x243 >= 0)

m.c402 = Constraint(expr=   m.b107 + m.b131 + m.b155 + m.b179 + m.b203 + m.b227 - m.x243 >= 0)

m.c403 = Constraint(expr=   m.b107 + m.b131 + m.b155 + m.b179 + m.b203 + m.b227 - m.x243 >= 0)

m.c404 = Constraint(expr=   m.b107 + m.b131 + m.b155 + m.b179 + m.b203 + m.b227 - m.x243 >= 0)

m.c405 = Constraint(expr=   m.b107 + m.b131 + m.b155 + m.b179 + m.b203 + m.b227 - m.x243 >= 0)

m.c406 = Constraint(expr=   m.b107 + m.b131 + m.b155 + m.b179 + m.b203 + m.b227 - m.x243 >= 0)

m.c407 = Constraint(expr=   m.b115 + m.b139 + m.b163 + m.b187 + m.b211 + m.b235 - m.x243 >= 0)

m.c408 = Constraint(expr=   m.b115 + m.b139 + m.b163 + m.b187 + m.b211 + m.b235 - m.x243 >= 0)

m.c409 = Constraint(expr=   m.b115 + m.b139 + m.b163 + m.b187 + m.b211 + m.b235 - m.x243 >= 0)

m.c410 = Constraint(expr=   m.b115 + m.b139 + m.b163 + m.b187 + m.b211 + m.b235 - m.x243 >= 0)

m.c411 = Constraint(expr=   m.b115 + m.b139 + m.b163 + m.b187 + m.b211 + m.b235 - m.x243 >= 0)

m.c412 = Constraint(expr=   m.b115 + m.b139 + m.b163 + m.b187 + m.b211 + m.b235 - m.x243 >= 0)

m.c413 = Constraint(expr=   m.b115 + m.b139 + m.b163 + m.b187 + m.b211 + m.b235 - m.x243 >= 0)

m.c414 = Constraint(expr=   m.b115 + m.b139 + m.b163 + m.b187 + m.b211 + m.b235 - m.x243 >= 0)

m.c415 = Constraint(expr=   m.b115 + m.b139 + m.b163 + m.b187 + m.b211 + m.b235 - m.x243 >= 0)

m.c416 = Constraint(expr=   m.b100 + m.b124 + m.b148 + m.b172 + m.b196 + m.b220 - m.x244 >= 0)

m.c417 = Constraint(expr=   m.b100 + m.b124 + m.b148 + m.b172 + m.b196 + m.b220 - m.x244 >= 0)

m.c418 = Constraint(expr=   m.b100 + m.b124 + m.b148 + m.b172 + m.b196 + m.b220 - m.x244 >= 0)

m.c419 = Constraint(expr=   m.b100 + m.b124 + m.b148 + m.b172 + m.b196 + m.b220 - m.x244 >= 0)

m.c420 = Constraint(expr=   m.b100 + m.b124 + m.b148 + m.b172 + m.b196 + m.b220 - m.x244 >= 0)

m.c421 = Constraint(expr=   m.b100 + m.b124 + m.b148 + m.b172 + m.b196 + m.b220 - m.x244 >= 0)

m.c422 = Constraint(expr=   m.b100 + m.b124 + m.b148 + m.b172 + m.b196 + m.b220 - m.x244 >= 0)

m.c423 = Constraint(expr=   m.b100 + m.b124 + m.b148 + m.b172 + m.b196 + m.b220 - m.x244 >= 0)

m.c424 = Constraint(expr=   m.b100 + m.b124 + m.b148 + m.b172 + m.b196 + m.b220 - m.x244 >= 0)

m.c425 = Constraint(expr=   m.b108 + m.b132 + m.b156 + m.b180 + m.b204 + m.b228 - m.x244 >= 0)

m.c426 = Constraint(expr=   m.b108 + m.b132 + m.b156 + m.b180 + m.b204 + m.b228 - m.x244 >= 0)

m.c427 = Constraint(expr=   m.b108 + m.b132 + m.b156 + m.b180 + m.b204 + m.b228 - m.x244 >= 0)

m.c428 = Constraint(expr=   m.b108 + m.b132 + m.b156 + m.b180 + m.b204 + m.b228 - m.x244 >= 0)

m.c429 = Constraint(expr=   m.b108 + m.b132 + m.b156 + m.b180 + m.b204 + m.b228 - m.x244 >= 0)

m.c430 = Constraint(expr=   m.b108 + m.b132 + m.b156 + m.b180 + m.b204 + m.b228 - m.x244 >= 0)

m.c431 = Constraint(expr=   m.b108 + m.b132 + m.b156 + m.b180 + m.b204 + m.b228 - m.x244 >= 0)

m.c432 = Constraint(expr=   m.b108 + m.b132 + m.b156 + m.b180 + m.b204 + m.b228 - m.x244 >= 0)

m.c433 = Constraint(expr=   m.b108 + m.b132 + m.b156 + m.b180 + m.b204 + m.b228 - m.x244 >= 0)

m.c434 = Constraint(expr=   m.b116 + m.b140 + m.b164 + m.b188 + m.b212 + m.b236 - m.x244 >= 0)

m.c435 = Constraint(expr=   m.b116 + m.b140 + m.b164 + m.b188 + m.b212 + m.b236 - m.x244 >= 0)

m.c436 = Constraint(expr=   m.b116 + m.b140 + m.b164 + m.b188 + m.b212 + m.b236 - m.x244 >= 0)

m.c437 = Constraint(expr=   m.b116 + m.b140 + m.b164 + m.b188 + m.b212 + m.b236 - m.x244 >= 0)

m.c438 = Constraint(expr=   m.b116 + m.b140 + m.b164 + m.b188 + m.b212 + m.b236 - m.x244 >= 0)

m.c439 = Constraint(expr=   m.b116 + m.b140 + m.b164 + m.b188 + m.b212 + m.b236 - m.x244 >= 0)

m.c440 = Constraint(expr=   m.b116 + m.b140 + m.b164 + m.b188 + m.b212 + m.b236 - m.x244 >= 0)

m.c441 = Constraint(expr=   m.b116 + m.b140 + m.b164 + m.b188 + m.b212 + m.b236 - m.x244 >= 0)

m.c442 = Constraint(expr=   m.b116 + m.b140 + m.b164 + m.b188 + m.b212 + m.b236 - m.x244 >= 0)

m.c443 = Constraint(expr=   m.b101 + m.b125 + m.b149 + m.b173 + m.b197 + m.b221 - m.x245 >= 0)

m.c444 = Constraint(expr=   m.b101 + m.b125 + m.b149 + m.b173 + m.b197 + m.b221 - m.x245 >= 0)

m.c445 = Constraint(expr=   m.b101 + m.b125 + m.b149 + m.b173 + m.b197 + m.b221 - m.x245 >= 0)

m.c446 = Constraint(expr=   m.b101 + m.b125 + m.b149 + m.b173 + m.b197 + m.b221 - m.x245 >= 0)

m.c447 = Constraint(expr=   m.b101 + m.b125 + m.b149 + m.b173 + m.b197 + m.b221 - m.x245 >= 0)

m.c448 = Constraint(expr=   m.b101 + m.b125 + m.b149 + m.b173 + m.b197 + m.b221 - m.x245 >= 0)

m.c449 = Constraint(expr=   m.b101 + m.b125 + m.b149 + m.b173 + m.b197 + m.b221 - m.x245 >= 0)

m.c450 = Constraint(expr=   m.b101 + m.b125 + m.b149 + m.b173 + m.b197 + m.b221 - m.x245 >= 0)

m.c451 = Constraint(expr=   m.b101 + m.b125 + m.b149 + m.b173 + m.b197 + m.b221 - m.x245 >= 0)

m.c452 = Constraint(expr=   m.b109 + m.b133 + m.b157 + m.b181 + m.b205 + m.b229 - m.x245 >= 0)

m.c453 = Constraint(expr=   m.b109 + m.b133 + m.b157 + m.b181 + m.b205 + m.b229 - m.x245 >= 0)

m.c454 = Constraint(expr=   m.b109 + m.b133 + m.b157 + m.b181 + m.b205 + m.b229 - m.x245 >= 0)

m.c455 = Constraint(expr=   m.b109 + m.b133 + m.b157 + m.b181 + m.b205 + m.b229 - m.x245 >= 0)

m.c456 = Constraint(expr=   m.b109 + m.b133 + m.b157 + m.b181 + m.b205 + m.b229 - m.x245 >= 0)

m.c457 = Constraint(expr=   m.b109 + m.b133 + m.b157 + m.b181 + m.b205 + m.b229 - m.x245 >= 0)

m.c458 = Constraint(expr=   m.b109 + m.b133 + m.b157 + m.b181 + m.b205 + m.b229 - m.x245 >= 0)

m.c459 = Constraint(expr=   m.b109 + m.b133 + m.b157 + m.b181 + m.b205 + m.b229 - m.x245 >= 0)

m.c460 = Constraint(expr=   m.b109 + m.b133 + m.b157 + m.b181 + m.b205 + m.b229 - m.x245 >= 0)

m.c461 = Constraint(expr=   m.b117 + m.b141 + m.b165 + m.b189 + m.b213 + m.b237 - m.x245 >= 0)

m.c462 = Constraint(expr=   m.b117 + m.b141 + m.b165 + m.b189 + m.b213 + m.b237 - m.x245 >= 0)

m.c463 = Constraint(expr=   m.b117 + m.b141 + m.b165 + m.b189 + m.b213 + m.b237 - m.x245 >= 0)

m.c464 = Constraint(expr=   m.b117 + m.b141 + m.b165 + m.b189 + m.b213 + m.b237 - m.x245 >= 0)

m.c465 = Constraint(expr=   m.b117 + m.b141 + m.b165 + m.b189 + m.b213 + m.b237 - m.x245 >= 0)

m.c466 = Constraint(expr=   m.b117 + m.b141 + m.b165 + m.b189 + m.b213 + m.b237 - m.x245 >= 0)

m.c467 = Constraint(expr=   m.b117 + m.b141 + m.b165 + m.b189 + m.b213 + m.b237 - m.x245 >= 0)

m.c468 = Constraint(expr=   m.b117 + m.b141 + m.b165 + m.b189 + m.b213 + m.b237 - m.x245 >= 0)

m.c469 = Constraint(expr=   m.b117 + m.b141 + m.b165 + m.b189 + m.b213 + m.b237 - m.x245 >= 0)

m.c470 = Constraint(expr=   m.b102 + m.b126 + m.b150 + m.b174 + m.b198 + m.b222 - m.x246 >= 0)

m.c471 = Constraint(expr=   m.b102 + m.b126 + m.b150 + m.b174 + m.b198 + m.b222 - m.x246 >= 0)

m.c472 = Constraint(expr=   m.b102 + m.b126 + m.b150 + m.b174 + m.b198 + m.b222 - m.x246 >= 0)

m.c473 = Constraint(expr=   m.b102 + m.b126 + m.b150 + m.b174 + m.b198 + m.b222 - m.x246 >= 0)

m.c474 = Constraint(expr=   m.b102 + m.b126 + m.b150 + m.b174 + m.b198 + m.b222 - m.x246 >= 0)

m.c475 = Constraint(expr=   m.b102 + m.b126 + m.b150 + m.b174 + m.b198 + m.b222 - m.x246 >= 0)

m.c476 = Constraint(expr=   m.b102 + m.b126 + m.b150 + m.b174 + m.b198 + m.b222 - m.x246 >= 0)

m.c477 = Constraint(expr=   m.b102 + m.b126 + m.b150 + m.b174 + m.b198 + m.b222 - m.x246 >= 0)

m.c478 = Constraint(expr=   m.b102 + m.b126 + m.b150 + m.b174 + m.b198 + m.b222 - m.x246 >= 0)

m.c479 = Constraint(expr=   m.b110 + m.b134 + m.b158 + m.b182 + m.b206 + m.b230 - m.x246 >= 0)

m.c480 = Constraint(expr=   m.b110 + m.b134 + m.b158 + m.b182 + m.b206 + m.b230 - m.x246 >= 0)

m.c481 = Constraint(expr=   m.b110 + m.b134 + m.b158 + m.b182 + m.b206 + m.b230 - m.x246 >= 0)

m.c482 = Constraint(expr=   m.b110 + m.b134 + m.b158 + m.b182 + m.b206 + m.b230 - m.x246 >= 0)

m.c483 = Constraint(expr=   m.b110 + m.b134 + m.b158 + m.b182 + m.b206 + m.b230 - m.x246 >= 0)

m.c484 = Constraint(expr=   m.b110 + m.b134 + m.b158 + m.b182 + m.b206 + m.b230 - m.x246 >= 0)

m.c485 = Constraint(expr=   m.b110 + m.b134 + m.b158 + m.b182 + m.b206 + m.b230 - m.x246 >= 0)

m.c486 = Constraint(expr=   m.b110 + m.b134 + m.b158 + m.b182 + m.b206 + m.b230 - m.x246 >= 0)

m.c487 = Constraint(expr=   m.b110 + m.b134 + m.b158 + m.b182 + m.b206 + m.b230 - m.x246 >= 0)

m.c488 = Constraint(expr=   m.b118 + m.b142 + m.b166 + m.b190 + m.b214 + m.b238 - m.x246 >= 0)

m.c489 = Constraint(expr=   m.b118 + m.b142 + m.b166 + m.b190 + m.b214 + m.b238 - m.x246 >= 0)

m.c490 = Constraint(expr=   m.b118 + m.b142 + m.b166 + m.b190 + m.b214 + m.b238 - m.x246 >= 0)

m.c491 = Constraint(expr=   m.b118 + m.b142 + m.b166 + m.b190 + m.b214 + m.b238 - m.x246 >= 0)

m.c492 = Constraint(expr=   m.b118 + m.b142 + m.b166 + m.b190 + m.b214 + m.b238 - m.x246 >= 0)

m.c493 = Constraint(expr=   m.b118 + m.b142 + m.b166 + m.b190 + m.b214 + m.b238 - m.x246 >= 0)

m.c494 = Constraint(expr=   m.b118 + m.b142 + m.b166 + m.b190 + m.b214 + m.b238 - m.x246 >= 0)

m.c495 = Constraint(expr=   m.b118 + m.b142 + m.b166 + m.b190 + m.b214 + m.b238 - m.x246 >= 0)

m.c496 = Constraint(expr=   m.b118 + m.b142 + m.b166 + m.b190 + m.b214 + m.b238 - m.x246 >= 0)

m.c497 = Constraint(expr=   m.b103 + m.b127 + m.b151 + m.b175 + m.b199 + m.b223 - m.x247 >= 0)

m.c498 = Constraint(expr=   m.b103 + m.b127 + m.b151 + m.b175 + m.b199 + m.b223 - m.x247 >= 0)

m.c499 = Constraint(expr=   m.b103 + m.b127 + m.b151 + m.b175 + m.b199 + m.b223 - m.x247 >= 0)

m.c500 = Constraint(expr=   m.b103 + m.b127 + m.b151 + m.b175 + m.b199 + m.b223 - m.x247 >= 0)

m.c501 = Constraint(expr=   m.b103 + m.b127 + m.b151 + m.b175 + m.b199 + m.b223 - m.x247 >= 0)

m.c502 = Constraint(expr=   m.b103 + m.b127 + m.b151 + m.b175 + m.b199 + m.b223 - m.x247 >= 0)

m.c503 = Constraint(expr=   m.b103 + m.b127 + m.b151 + m.b175 + m.b199 + m.b223 - m.x247 >= 0)

m.c504 = Constraint(expr=   m.b103 + m.b127 + m.b151 + m.b175 + m.b199 + m.b223 - m.x247 >= 0)

m.c505 = Constraint(expr=   m.b103 + m.b127 + m.b151 + m.b175 + m.b199 + m.b223 - m.x247 >= 0)

m.c506 = Constraint(expr=   m.b111 + m.b135 + m.b159 + m.b183 + m.b207 + m.b231 - m.x247 >= 0)

m.c507 = Constraint(expr=   m.b111 + m.b135 + m.b159 + m.b183 + m.b207 + m.b231 - m.x247 >= 0)

m.c508 = Constraint(expr=   m.b111 + m.b135 + m.b159 + m.b183 + m.b207 + m.b231 - m.x247 >= 0)

m.c509 = Constraint(expr=   m.b111 + m.b135 + m.b159 + m.b183 + m.b207 + m.b231 - m.x247 >= 0)

m.c510 = Constraint(expr=   m.b111 + m.b135 + m.b159 + m.b183 + m.b207 + m.b231 - m.x247 >= 0)

m.c511 = Constraint(expr=   m.b111 + m.b135 + m.b159 + m.b183 + m.b207 + m.b231 - m.x247 >= 0)

m.c512 = Constraint(expr=   m.b111 + m.b135 + m.b159 + m.b183 + m.b207 + m.b231 - m.x247 >= 0)

m.c513 = Constraint(expr=   m.b111 + m.b135 + m.b159 + m.b183 + m.b207 + m.b231 - m.x247 >= 0)

m.c514 = Constraint(expr=   m.b111 + m.b135 + m.b159 + m.b183 + m.b207 + m.b231 - m.x247 >= 0)

m.c515 = Constraint(expr=   m.b119 + m.b143 + m.b167 + m.b191 + m.b215 + m.b239 - m.x247 >= 0)

m.c516 = Constraint(expr=   m.b119 + m.b143 + m.b167 + m.b191 + m.b215 + m.b239 - m.x247 >= 0)

m.c517 = Constraint(expr=   m.b119 + m.b143 + m.b167 + m.b191 + m.b215 + m.b239 - m.x247 >= 0)

m.c518 = Constraint(expr=   m.b119 + m.b143 + m.b167 + m.b191 + m.b215 + m.b239 - m.x247 >= 0)

m.c519 = Constraint(expr=   m.b119 + m.b143 + m.b167 + m.b191 + m.b215 + m.b239 - m.x247 >= 0)

m.c520 = Constraint(expr=   m.b119 + m.b143 + m.b167 + m.b191 + m.b215 + m.b239 - m.x247 >= 0)

m.c521 = Constraint(expr=   m.b119 + m.b143 + m.b167 + m.b191 + m.b215 + m.b239 - m.x247 >= 0)

m.c522 = Constraint(expr=   m.b119 + m.b143 + m.b167 + m.b191 + m.b215 + m.b239 - m.x247 >= 0)

m.c523 = Constraint(expr=   m.b119 + m.b143 + m.b167 + m.b191 + m.b215 + m.b239 - m.x247 >= 0)

m.c524 = Constraint(expr=   m.b104 + m.b128 + m.b152 + m.b176 + m.b200 + m.b224 - m.x248 >= 0)

m.c525 = Constraint(expr=   m.b104 + m.b128 + m.b152 + m.b176 + m.b200 + m.b224 - m.x248 >= 0)

m.c526 = Constraint(expr=   m.b104 + m.b128 + m.b152 + m.b176 + m.b200 + m.b224 - m.x248 >= 0)

m.c527 = Constraint(expr=   m.b104 + m.b128 + m.b152 + m.b176 + m.b200 + m.b224 - m.x248 >= 0)

m.c528 = Constraint(expr=   m.b104 + m.b128 + m.b152 + m.b176 + m.b200 + m.b224 - m.x248 >= 0)

m.c529 = Constraint(expr=   m.b104 + m.b128 + m.b152 + m.b176 + m.b200 + m.b224 - m.x248 >= 0)

m.c530 = Constraint(expr=   m.b104 + m.b128 + m.b152 + m.b176 + m.b200 + m.b224 - m.x248 >= 0)

m.c531 = Constraint(expr=   m.b104 + m.b128 + m.b152 + m.b176 + m.b200 + m.b224 - m.x248 >= 0)

m.c532 = Constraint(expr=   m.b104 + m.b128 + m.b152 + m.b176 + m.b200 + m.b224 - m.x248 >= 0)

m.c533 = Constraint(expr=   m.b112 + m.b136 + m.b160 + m.b184 + m.b208 + m.b232 - m.x248 >= 0)

m.c534 = Constraint(expr=   m.b112 + m.b136 + m.b160 + m.b184 + m.b208 + m.b232 - m.x248 >= 0)

m.c535 = Constraint(expr=   m.b112 + m.b136 + m.b160 + m.b184 + m.b208 + m.b232 - m.x248 >= 0)

m.c536 = Constraint(expr=   m.b112 + m.b136 + m.b160 + m.b184 + m.b208 + m.b232 - m.x248 >= 0)

m.c537 = Constraint(expr=   m.b112 + m.b136 + m.b160 + m.b184 + m.b208 + m.b232 - m.x248 >= 0)

m.c538 = Constraint(expr=   m.b112 + m.b136 + m.b160 + m.b184 + m.b208 + m.b232 - m.x248 >= 0)

m.c539 = Constraint(expr=   m.b112 + m.b136 + m.b160 + m.b184 + m.b208 + m.b232 - m.x248 >= 0)

m.c540 = Constraint(expr=   m.b112 + m.b136 + m.b160 + m.b184 + m.b208 + m.b232 - m.x248 >= 0)

m.c541 = Constraint(expr=   m.b112 + m.b136 + m.b160 + m.b184 + m.b208 + m.b232 - m.x248 >= 0)

m.c542 = Constraint(expr=   m.b120 + m.b144 + m.b168 + m.b192 + m.b216 + m.b240 - m.x248 >= 0)

m.c543 = Constraint(expr=   m.b120 + m.b144 + m.b168 + m.b192 + m.b216 + m.b240 - m.x248 >= 0)

m.c544 = Constraint(expr=   m.b120 + m.b144 + m.b168 + m.b192 + m.b216 + m.b240 - m.x248 >= 0)

m.c545 = Constraint(expr=   m.b120 + m.b144 + m.b168 + m.b192 + m.b216 + m.b240 - m.x248 >= 0)

m.c546 = Constraint(expr=   m.b120 + m.b144 + m.b168 + m.b192 + m.b216 + m.b240 - m.x248 >= 0)

m.c547 = Constraint(expr=   m.b120 + m.b144 + m.b168 + m.b192 + m.b216 + m.b240 - m.x248 >= 0)

m.c548 = Constraint(expr=   m.b120 + m.b144 + m.b168 + m.b192 + m.b216 + m.b240 - m.x248 >= 0)

m.c549 = Constraint(expr=   m.b120 + m.b144 + m.b168 + m.b192 + m.b216 + m.b240 - m.x248 >= 0)

m.c550 = Constraint(expr=   m.b120 + m.b144 + m.b168 + m.b192 + m.b216 + m.b240 - m.x248 >= 0)

m.c551 = Constraint(expr=   m.b105 + m.b129 + m.b153 + m.b177 + m.b201 + m.b225 - m.x249 >= 0)

m.c552 = Constraint(expr=   m.b105 + m.b129 + m.b153 + m.b177 + m.b201 + m.b225 - m.x249 >= 0)

m.c553 = Constraint(expr=   m.b105 + m.b129 + m.b153 + m.b177 + m.b201 + m.b225 - m.x249 >= 0)

m.c554 = Constraint(expr=   m.b105 + m.b129 + m.b153 + m.b177 + m.b201 + m.b225 - m.x249 >= 0)

m.c555 = Constraint(expr=   m.b105 + m.b129 + m.b153 + m.b177 + m.b201 + m.b225 - m.x249 >= 0)

m.c556 = Constraint(expr=   m.b105 + m.b129 + m.b153 + m.b177 + m.b201 + m.b225 - m.x249 >= 0)

m.c557 = Constraint(expr=   m.b105 + m.b129 + m.b153 + m.b177 + m.b201 + m.b225 - m.x249 >= 0)

m.c558 = Constraint(expr=   m.b105 + m.b129 + m.b153 + m.b177 + m.b201 + m.b225 - m.x249 >= 0)

m.c559 = Constraint(expr=   m.b105 + m.b129 + m.b153 + m.b177 + m.b201 + m.b225 - m.x249 >= 0)

m.c560 = Constraint(expr=   m.b113 + m.b137 + m.b161 + m.b185 + m.b209 + m.b233 - m.x249 >= 0)

m.c561 = Constraint(expr=   m.b113 + m.b137 + m.b161 + m.b185 + m.b209 + m.b233 - m.x249 >= 0)

m.c562 = Constraint(expr=   m.b113 + m.b137 + m.b161 + m.b185 + m.b209 + m.b233 - m.x249 >= 0)

m.c563 = Constraint(expr=   m.b113 + m.b137 + m.b161 + m.b185 + m.b209 + m.b233 - m.x249 >= 0)

m.c564 = Constraint(expr=   m.b113 + m.b137 + m.b161 + m.b185 + m.b209 + m.b233 - m.x249 >= 0)

m.c565 = Constraint(expr=   m.b113 + m.b137 + m.b161 + m.b185 + m.b209 + m.b233 - m.x249 >= 0)

m.c566 = Constraint(expr=   m.b113 + m.b137 + m.b161 + m.b185 + m.b209 + m.b233 - m.x249 >= 0)

m.c567 = Constraint(expr=   m.b113 + m.b137 + m.b161 + m.b185 + m.b209 + m.b233 - m.x249 >= 0)

m.c568 = Constraint(expr=   m.b113 + m.b137 + m.b161 + m.b185 + m.b209 + m.b233 - m.x249 >= 0)

m.c569 = Constraint(expr=   m.b121 + m.b145 + m.b169 + m.b193 + m.b217 + m.b241 - m.x249 >= 0)

m.c570 = Constraint(expr=   m.b121 + m.b145 + m.b169 + m.b193 + m.b217 + m.b241 - m.x249 >= 0)

m.c571 = Constraint(expr=   m.b121 + m.b145 + m.b169 + m.b193 + m.b217 + m.b241 - m.x249 >= 0)

m.c572 = Constraint(expr=   m.b121 + m.b145 + m.b169 + m.b193 + m.b217 + m.b241 - m.x249 >= 0)

m.c573 = Constraint(expr=   m.b121 + m.b145 + m.b169 + m.b193 + m.b217 + m.b241 - m.x249 >= 0)

m.c574 = Constraint(expr=   m.b121 + m.b145 + m.b169 + m.b193 + m.b217 + m.b241 - m.x249 >= 0)

m.c575 = Constraint(expr=   m.b121 + m.b145 + m.b169 + m.b193 + m.b217 + m.b241 - m.x249 >= 0)

m.c576 = Constraint(expr=   m.b121 + m.b145 + m.b169 + m.b193 + m.b217 + m.b241 - m.x249 >= 0)

m.c577 = Constraint(expr=   m.b121 + m.b145 + m.b169 + m.b193 + m.b217 + m.b241 - m.x249 >= 0)

m.c578 = Constraint(expr=m.x322*m.b98 + 1.5*m.x322*m.b106 + m.x322*m.b114 + m.x323*m.b99 + 1.5*m.x323*m.b107 + m.x323*
                         m.b115 + m.x324*m.b100 + 1.5*m.x324*m.b108 + m.x324*m.b116 + 1.5*m.x328*m.b112 + 1.5*m.x329*
                         m.b113 <= 999999)

m.c579 = Constraint(expr=m.x322*m.b122 + 1.5*m.x322*m.b130 + m.x322*m.b138 + m.x323*m.b123 + 1.5*m.x323*m.b131 + m.x323*
                         m.b139 + m.x324*m.b124 + 1.5*m.x324*m.b132 + m.x324*m.b140 + 1.5*m.x328*m.b136 + 1.5*m.x329*
                         m.b137 <= 999999)

m.c580 = Constraint(expr=m.x322*m.b146 + 1.5*m.x322*m.b154 + m.x322*m.b162 + m.x323*m.b147 + 1.5*m.x323*m.b155 + m.x323*
                         m.b163 + m.x324*m.b148 + 1.5*m.x324*m.b156 + m.x324*m.b164 + 1.5*m.x328*m.b160 + 1.5*m.x329*
                         m.b161 <= 999999)

m.c581 = Constraint(expr=m.x322*m.b170 + 1.5*m.x322*m.b178 + m.x322*m.b186 + m.x323*m.b171 + 1.5*m.x323*m.b179 + m.x323*
                         m.b187 + m.x324*m.b172 + 1.5*m.x324*m.b180 + m.x324*m.b188 + 1.5*m.x328*m.b184 + 1.5*m.x329*
                         m.b185 <= 888888)

m.c582 = Constraint(expr=m.x322*m.b194 + 1.5*m.x322*m.b202 + m.x322*m.b210 + m.x323*m.b195 + 1.5*m.x323*m.b203 + m.x323*
                         m.b211 + m.x324*m.b196 + 1.5*m.x324*m.b204 + m.x324*m.b212 + 1.5*m.x328*m.b208 + 1.5*m.x329*
                         m.b209 <= 9999999)

m.c583 = Constraint(expr=m.x322*m.b218 + 1.5*m.x322*m.b226 + m.x322*m.b234 + m.x323*m.b219 + 1.5*m.x323*m.b227 + m.x323*
                         m.b235 + m.x324*m.b220 + 1.5*m.x324*m.b228 + m.x324*m.b236 + 1.5*m.x328*m.b232 + 1.5*m.x329*
                         m.b233 <= 999999)

m.c584 = Constraint(expr=1.5*m.x325*m.b109 + m.x325*m.b117 + 1.5*m.x326*m.b110 + m.x326*m.b118 + 1.5*m.x327*m.b111 + 
                         m.x327*m.b119 + m.x328*m.b104 + m.x328*m.b120 + m.x329*m.b105 + m.x329*m.b121 <= 72722)

m.c585 = Constraint(expr=1.5*m.x325*m.b133 + m.x325*m.b141 + 1.5*m.x326*m.b134 + m.x326*m.b142 + 1.5*m.x327*m.b135 + 
                         m.x327*m.b143 + m.x328*m.b128 + m.x328*m.b144 + m.x329*m.b129 + m.x329*m.b145 <= 32737)

m.c586 = Constraint(expr=1.5*m.x325*m.b157 + m.x325*m.b165 + 1.5*m.x326*m.b158 + m.x326*m.b166 + 1.5*m.x327*m.b159 + 
                         m.x327*m.b167 + m.x328*m.b152 + m.x328*m.b168 + m.x329*m.b153 + m.x329*m.b169 <= 999999)

m.c587 = Constraint(expr=1.5*m.x325*m.b181 + m.x325*m.b189 + 1.5*m.x326*m.b182 + m.x326*m.b190 + 1.5*m.x327*m.b183 + 
                         m.x327*m.b191 + m.x328*m.b176 + m.x328*m.b192 + m.x329*m.b177 + m.x329*m.b193 <= 999999)

m.c588 = Constraint(expr=1.5*m.x325*m.b205 + m.x325*m.b213 + 1.5*m.x326*m.b206 + m.x326*m.b214 + 1.5*m.x327*m.b207 + 
                         m.x327*m.b215 + m.x328*m.b200 + m.x328*m.b216 + m.x329*m.b201 + m.x329*m.b217 <= 122344)

m.c589 = Constraint(expr=1.5*m.x325*m.b229 + m.x325*m.b237 + 1.5*m.x326*m.b230 + m.x326*m.b238 + 1.5*m.x327*m.b231 + 
                         m.x327*m.b239 + m.x328*m.b224 + m.x328*m.b240 + m.x329*m.b225 + m.x329*m.b241 <= 147559)

m.c590 = Constraint(expr=m.x325*m.b101 + m.x326*m.b102 + m.x327*m.b103 <= 999999)

m.c591 = Constraint(expr=m.x325*m.b125 + m.x326*m.b126 + m.x327*m.b127 <= 999999)

m.c592 = Constraint(expr=m.x325*m.b149 + m.x326*m.b150 + m.x327*m.b151 <= 999999)

m.c593 = Constraint(expr=m.x325*m.b173 + m.x326*m.b174 + m.x327*m.b175 <= 999999)

m.c594 = Constraint(expr=m.x325*m.b197 + m.x326*m.b198 + m.x327*m.b199 <= 999999)

m.c595 = Constraint(expr=m.x325*m.b221 + m.x326*m.b222 + m.x327*m.b223 <= 999999)

m.c596 = Constraint(expr=0.527704485488127*m.i26*m.x322 + 0.527704485488127*m.i27*m.x323 + 0.527704485488127*m.i28*
                         m.x324 + 0.527704485488127*m.i29*m.x325 + 0.527704485488127*m.i30*m.x326 + 0.527704485488127*
                         m.i31*m.x327 + 0.527704485488127*m.i32*m.x328 + 0.527704485488127*m.i33*m.x329 >= 1000)

m.c597 = Constraint(expr=1.33333333333333*m.i34*m.x322 + 1.33333333333333*m.i35*m.x323 + 1.33333333333333*m.i36*m.x324
                          + 1.33333333333333*m.i37*m.x325 + 1.33333333333333*m.i38*m.x326 + 1.33333333333333*m.i39*
                         m.x327 + 1.33333333333333*m.i40*m.x328 + 1.33333333333333*m.i41*m.x329 >= 1500)

m.c598 = Constraint(expr=0.858369098712446*m.i42*m.x322 + 0.858369098712446*m.i43*m.x323 + 0.858369098712446*m.i44*
                         m.x324 + 0.858369098712446*m.i45*m.x325 + 0.858369098712446*m.i46*m.x326 + 0.858369098712446*
                         m.i47*m.x327 + 0.858369098712446*m.i48*m.x328 + 0.858369098712446*m.i49*m.x329 >= 2000)

m.c599 = Constraint(expr=1.32450331125828*m.i50*m.x322 + 1.32450331125828*m.i51*m.x323 + 1.32450331125828*m.i52*m.x324
                          + 1.32450331125828*m.i53*m.x325 + 1.32450331125828*m.i54*m.x326 + 1.32450331125828*m.i55*
                         m.x327 + 1.32450331125828*m.i56*m.x328 + 1.32450331125828*m.i57*m.x329 >= 2000)

m.c600 = Constraint(expr=0.50125313283208*m.i58*m.x322 + 0.50125313283208*m.i59*m.x323 + 0.50125313283208*m.i60*m.x324
                          + 0.50125313283208*m.i61*m.x325 + 0.50125313283208*m.i62*m.x326 + 0.50125313283208*m.i63*
                         m.x327 + 0.50125313283208*m.i64*m.x328 + 0.50125313283208*m.i65*m.x329 >= 1500)

m.c601 = Constraint(expr=0.555555555555556*m.i66*m.x322 + 0.555555555555556*m.i67*m.x323 + 0.555555555555556*m.i68*
                         m.x324 + 0.555555555555556*m.i69*m.x325 + 0.555555555555556*m.i70*m.x326 + 0.555555555555556*
                         m.i71*m.x327 + 0.555555555555556*m.i72*m.x328 + 0.555555555555556*m.i73*m.x329 >= 1500)

m.c602 = Constraint(expr=1.17647058823529*m.i74*m.x322 + 1.17647058823529*m.i75*m.x323 + 1.17647058823529*m.i76*m.x324
                          + 1.17647058823529*m.i77*m.x325 + 1.17647058823529*m.i78*m.x326 + 1.17647058823529*m.i79*
                         m.x327 + 1.17647058823529*m.i80*m.x328 + 1.17647058823529*m.i81*m.x329 >= 2500)

m.c603 = Constraint(expr=0.833333333333333*m.i82*m.x322 + 0.833333333333333*m.i83*m.x323 + 0.833333333333333*m.i84*
                         m.x324 + 0.833333333333333*m.i85*m.x325 + 0.833333333333333*m.i86*m.x326 + 0.833333333333333*
                         m.i87*m.x327 + 0.833333333333333*m.i88*m.x328 + 0.833333333333333*m.i89*m.x329 >= 3000)

m.c604 = Constraint(expr=1.25*m.i90*m.x322 + 1.25*m.i91*m.x323 + 1.25*m.i92*m.x324 + 1.25*m.i93*m.x325 + 1.25*m.i94*
                         m.x326 + 1.25*m.i95*m.x327 + 1.25*m.i96*m.x328 + 1.25*m.i97*m.x329 >= 2000)

m.c605 = Constraint(expr=0.527704485488127*m.i26*m.x322 + 0.527704485488127*m.i27*m.x323 + 0.527704485488127*m.i28*
                         m.x324 + 0.527704485488127*m.i29*m.x325 + 0.527704485488127*m.i30*m.x326 + 0.527704485488127*
                         m.i31*m.x327 + 0.527704485488127*m.i32*m.x328 + 0.527704485488127*m.i33*m.x329 <= 1500)

m.c606 = Constraint(expr=1.33333333333333*m.i34*m.x322 + 1.33333333333333*m.i35*m.x323 + 1.33333333333333*m.i36*m.x324
                          + 1.33333333333333*m.i37*m.x325 + 1.33333333333333*m.i38*m.x326 + 1.33333333333333*m.i39*
                         m.x327 + 1.33333333333333*m.i40*m.x328 + 1.33333333333333*m.i41*m.x329 <= 2250)

m.c607 = Constraint(expr=0.858369098712446*m.i42*m.x322 + 0.858369098712446*m.i43*m.x323 + 0.858369098712446*m.i44*
                         m.x324 + 0.858369098712446*m.i45*m.x325 + 0.858369098712446*m.i46*m.x326 + 0.858369098712446*
                         m.i47*m.x327 + 0.858369098712446*m.i48*m.x328 + 0.858369098712446*m.i49*m.x329 <= 3000)

m.c608 = Constraint(expr=1.32450331125828*m.i50*m.x322 + 1.32450331125828*m.i51*m.x323 + 1.32450331125828*m.i52*m.x324
                          + 1.32450331125828*m.i53*m.x325 + 1.32450331125828*m.i54*m.x326 + 1.32450331125828*m.i55*
                         m.x327 + 1.32450331125828*m.i56*m.x328 + 1.32450331125828*m.i57*m.x329 <= 3000)

m.c609 = Constraint(expr=0.50125313283208*m.i58*m.x322 + 0.50125313283208*m.i59*m.x323 + 0.50125313283208*m.i60*m.x324
                          + 0.50125313283208*m.i61*m.x325 + 0.50125313283208*m.i62*m.x326 + 0.50125313283208*m.i63*
                         m.x327 + 0.50125313283208*m.i64*m.x328 + 0.50125313283208*m.i65*m.x329 <= 2250)

m.c610 = Constraint(expr=0.555555555555556*m.i66*m.x322 + 0.555555555555556*m.i67*m.x323 + 0.555555555555556*m.i68*
                         m.x324 + 0.555555555555556*m.i69*m.x325 + 0.555555555555556*m.i70*m.x326 + 0.555555555555556*
                         m.i71*m.x327 + 0.555555555555556*m.i72*m.x328 + 0.555555555555556*m.i73*m.x329 <= 2250)

m.c611 = Constraint(expr=1.17647058823529*m.i74*m.x322 + 1.17647058823529*m.i75*m.x323 + 1.17647058823529*m.i76*m.x324
                          + 1.17647058823529*m.i77*m.x325 + 1.17647058823529*m.i78*m.x326 + 1.17647058823529*m.i79*
                         m.x327 + 1.17647058823529*m.i80*m.x328 + 1.17647058823529*m.i81*m.x329 <= 3750)

m.c612 = Constraint(expr=0.833333333333333*m.i82*m.x322 + 0.833333333333333*m.i83*m.x323 + 0.833333333333333*m.i84*
                         m.x324 + 0.833333333333333*m.i85*m.x325 + 0.833333333333333*m.i86*m.x326 + 0.833333333333333*
                         m.i87*m.x327 + 0.833333333333333*m.i88*m.x328 + 0.833333333333333*m.i89*m.x329 <= 4500)

m.c613 = Constraint(expr=1.25*m.i90*m.x322 + 1.25*m.i91*m.x323 + 1.25*m.i92*m.x324 + 1.25*m.i93*m.x325 + 1.25*m.i94*
                         m.x326 + 1.25*m.i95*m.x327 + 1.25*m.i96*m.x328 + 1.25*m.i97*m.x329 <= 3000)

m.c614 = Constraint(expr= - 500*m.x242 + m.x322 >= 0)

m.c615 = Constraint(expr= - 500*m.x243 + m.x323 >= 0)

m.c616 = Constraint(expr= - 500*m.x244 + m.x324 >= 0)

m.c617 = Constraint(expr= - 500*m.x245 + m.x325 >= 0)

m.c618 = Constraint(expr= - 500*m.x246 + m.x326 >= 0)

m.c619 = Constraint(expr= - 500*m.x247 + m.x327 >= 0)

m.c620 = Constraint(expr= - 500*m.x248 + m.x328 >= 0)

m.c621 = Constraint(expr= - 500*m.x249 + m.x329 >= 0)

m.c622 = Constraint(expr= - 2000*m.x242 + m.x322 <= 0)

m.c623 = Constraint(expr= - 2000*m.x243 + m.x323 <= 0)

m.c624 = Constraint(expr= - 2000*m.x244 + m.x324 <= 0)

m.c625 = Constraint(expr= - 2000*m.x245 + m.x325 <= 0)

m.c626 = Constraint(expr= - 2000*m.x246 + m.x326 <= 0)

m.c627 = Constraint(expr= - 2000*m.x247 + m.x327 <= 0)

m.c628 = Constraint(expr= - 2000*m.x248 + m.x328 <= 0)

m.c629 = Constraint(expr= - 2000*m.x249 + m.x329 <= 0)

m.c630 = Constraint(expr= - m.x242 + m.b250 + m.b258 + m.b266 + m.b274 + m.b282 + m.b290 + m.b298 + m.b306 + m.b314
                          >= 0)

m.c631 = Constraint(expr= - m.x243 + m.b251 + m.b259 + m.b267 + m.b275 + m.b283 + m.b291 + m.b299 + m.b307 + m.b315
                          >= 0)

m.c632 = Constraint(expr= - m.x244 + m.b252 + m.b260 + m.b268 + m.b276 + m.b284 + m.b292 + m.b300 + m.b308 + m.b316
                          >= 0)

m.c633 = Constraint(expr= - m.x245 + m.b253 + m.b261 + m.b269 + m.b277 + m.b285 + m.b293 + m.b301 + m.b309 + m.b317
                          >= 0)

m.c634 = Constraint(expr= - m.x246 + m.b254 + m.b262 + m.b270 + m.b278 + m.b286 + m.b294 + m.b302 + m.b310 + m.b318
                          >= 0)

m.c635 = Constraint(expr= - m.x247 + m.b255 + m.b263 + m.b271 + m.b279 + m.b287 + m.b295 + m.b303 + m.b311 + m.b319
                          >= 0)

m.c636 = Constraint(expr= - m.x248 + m.b256 + m.b264 + m.b272 + m.b280 + m.b288 + m.b296 + m.b304 + m.b312 + m.b320
                          >= 0)

m.c637 = Constraint(expr= - m.x249 + m.b257 + m.b265 + m.b273 + m.b281 + m.b289 + m.b297 + m.b305 + m.b313 + m.b321
                          >= 0)

m.c638 = Constraint(expr=   m.x242 - m.b250 >= 0)

m.c639 = Constraint(expr=   m.x243 - m.b251 >= 0)

m.c640 = Constraint(expr=   m.x244 - m.b252 >= 0)

m.c641 = Constraint(expr=   m.x245 - m.b253 >= 0)

m.c642 = Constraint(expr=   m.x246 - m.b254 >= 0)

m.c643 = Constraint(expr=   m.x247 - m.b255 >= 0)

m.c644 = Constraint(expr=   m.x248 - m.b256 >= 0)

m.c645 = Constraint(expr=   m.x249 - m.b257 >= 0)

m.c646 = Constraint(expr=   m.x242 - m.b258 >= 0)

m.c647 = Constraint(expr=   m.x243 - m.b259 >= 0)

m.c648 = Constraint(expr=   m.x244 - m.b260 >= 0)

m.c649 = Constraint(expr=   m.x245 - m.b261 >= 0)

m.c650 = Constraint(expr=   m.x246 - m.b262 >= 0)

m.c651 = Constraint(expr=   m.x247 - m.b263 >= 0)

m.c652 = Constraint(expr=   m.x248 - m.b264 >= 0)

m.c653 = Constraint(expr=   m.x249 - m.b265 >= 0)

m.c654 = Constraint(expr=   m.x242 - m.b266 >= 0)

m.c655 = Constraint(expr=   m.x243 - m.b267 >= 0)

m.c656 = Constraint(expr=   m.x244 - m.b268 >= 0)

m.c657 = Constraint(expr=   m.x245 - m.b269 >= 0)

m.c658 = Constraint(expr=   m.x246 - m.b270 >= 0)

m.c659 = Constraint(expr=   m.x247 - m.b271 >= 0)

m.c660 = Constraint(expr=   m.x248 - m.b272 >= 0)

m.c661 = Constraint(expr=   m.x249 - m.b273 >= 0)

m.c662 = Constraint(expr=   m.x242 - m.b274 >= 0)

m.c663 = Constraint(expr=   m.x243 - m.b275 >= 0)

m.c664 = Constraint(expr=   m.x244 - m.b276 >= 0)

m.c665 = Constraint(expr=   m.x245 - m.b277 >= 0)

m.c666 = Constraint(expr=   m.x246 - m.b278 >= 0)

m.c667 = Constraint(expr=   m.x247 - m.b279 >= 0)

m.c668 = Constraint(expr=   m.x248 - m.b280 >= 0)

m.c669 = Constraint(expr=   m.x249 - m.b281 >= 0)

m.c670 = Constraint(expr=   m.x242 - m.b282 >= 0)

m.c671 = Constraint(expr=   m.x243 - m.b283 >= 0)

m.c672 = Constraint(expr=   m.x244 - m.b284 >= 0)

m.c673 = Constraint(expr=   m.x245 - m.b285 >= 0)

m.c674 = Constraint(expr=   m.x246 - m.b286 >= 0)

m.c675 = Constraint(expr=   m.x247 - m.b287 >= 0)

m.c676 = Constraint(expr=   m.x248 - m.b288 >= 0)

m.c677 = Constraint(expr=   m.x249 - m.b289 >= 0)

m.c678 = Constraint(expr=   m.x242 - m.b290 >= 0)

m.c679 = Constraint(expr=   m.x243 - m.b291 >= 0)

m.c680 = Constraint(expr=   m.x244 - m.b292 >= 0)

m.c681 = Constraint(expr=   m.x245 - m.b293 >= 0)

m.c682 = Constraint(expr=   m.x246 - m.b294 >= 0)

m.c683 = Constraint(expr=   m.x247 - m.b295 >= 0)

m.c684 = Constraint(expr=   m.x248 - m.b296 >= 0)

m.c685 = Constraint(expr=   m.x249 - m.b297 >= 0)

m.c686 = Constraint(expr=   m.x242 - m.b298 >= 0)

m.c687 = Constraint(expr=   m.x243 - m.b299 >= 0)

m.c688 = Constraint(expr=   m.x244 - m.b300 >= 0)

m.c689 = Constraint(expr=   m.x245 - m.b301 >= 0)

m.c690 = Constraint(expr=   m.x246 - m.b302 >= 0)

m.c691 = Constraint(expr=   m.x247 - m.b303 >= 0)

m.c692 = Constraint(expr=   m.x248 - m.b304 >= 0)

m.c693 = Constraint(expr=   m.x249 - m.b305 >= 0)

m.c694 = Constraint(expr=   m.x242 - m.b306 >= 0)

m.c695 = Constraint(expr=   m.x243 - m.b307 >= 0)

m.c696 = Constraint(expr=   m.x244 - m.b308 >= 0)

m.c697 = Constraint(expr=   m.x245 - m.b309 >= 0)

m.c698 = Constraint(expr=   m.x246 - m.b310 >= 0)

m.c699 = Constraint(expr=   m.x247 - m.b311 >= 0)

m.c700 = Constraint(expr=   m.x248 - m.b312 >= 0)

m.c701 = Constraint(expr=   m.x249 - m.b313 >= 0)

m.c702 = Constraint(expr=   m.x242 - m.b314 >= 0)

m.c703 = Constraint(expr=   m.x243 - m.b315 >= 0)

m.c704 = Constraint(expr=   m.x244 - m.b316 >= 0)

m.c705 = Constraint(expr=   m.x245 - m.b317 >= 0)

m.c706 = Constraint(expr=   m.x246 - m.b318 >= 0)

m.c707 = Constraint(expr=   m.x247 - m.b319 >= 0)

m.c708 = Constraint(expr=   m.x248 - m.b320 >= 0)

m.c709 = Constraint(expr=   m.x249 - m.b321 >= 0)

m.c710 = Constraint(expr=   m.b250 + m.b251 + m.b252 + m.b253 + m.b254 + m.b255 + m.b256 + m.b257 >= 1)

m.c711 = Constraint(expr=   m.b258 + m.b259 + m.b260 + m.b261 + m.b262 + m.b263 + m.b264 + m.b265 >= 1)

m.c712 = Constraint(expr=   m.b266 + m.b267 + m.b268 + m.b269 + m.b270 + m.b271 + m.b272 + m.b273 >= 1)

m.c713 = Constraint(expr=   m.b274 + m.b275 + m.b276 + m.b277 + m.b278 + m.b279 + m.b280 + m.b281 >= 1)

m.c714 = Constraint(expr=   m.b282 + m.b283 + m.b284 + m.b285 + m.b286 + m.b287 + m.b288 + m.b289 >= 1)

m.c715 = Constraint(expr=   m.b290 + m.b291 + m.b292 + m.b293 + m.b294 + m.b295 + m.b296 + m.b297 >= 1)

m.c716 = Constraint(expr=   m.b298 + m.b299 + m.b300 + m.b301 + m.b302 + m.b303 + m.b304 + m.b305 >= 1)

m.c717 = Constraint(expr=   m.b306 + m.b307 + m.b308 + m.b309 + m.b310 + m.b311 + m.b312 + m.b313 >= 1)

m.c718 = Constraint(expr=   m.b314 + m.b315 + m.b316 + m.b317 + m.b318 + m.b319 + m.b320 + m.b321 >= 1)

m.c719 = Constraint(expr= - m.i26 + m.b250 <= 0)

m.c720 = Constraint(expr= - m.i27 + m.b251 <= 0)

m.c721 = Constraint(expr= - m.i28 + m.b252 <= 0)

m.c722 = Constraint(expr= - m.i29 + m.b253 <= 0)

m.c723 = Constraint(expr= - m.i30 + m.b254 <= 0)

m.c724 = Constraint(expr= - m.i31 + m.b255 <= 0)

m.c725 = Constraint(expr= - m.i32 + m.b256 <= 0)

m.c726 = Constraint(expr= - m.i33 + m.b257 <= 0)

m.c727 = Constraint(expr= - m.i34 + m.b258 <= 0)

m.c728 = Constraint(expr= - m.i35 + m.b259 <= 0)

m.c729 = Constraint(expr= - m.i36 + m.b260 <= 0)

m.c730 = Constraint(expr= - m.i37 + m.b261 <= 0)

m.c731 = Constraint(expr= - m.i38 + m.b262 <= 0)

m.c732 = Constraint(expr= - m.i39 + m.b263 <= 0)

m.c733 = Constraint(expr= - m.i40 + m.b264 <= 0)

m.c734 = Constraint(expr= - m.i41 + m.b265 <= 0)

m.c735 = Constraint(expr= - m.i42 + m.b266 <= 0)

m.c736 = Constraint(expr= - m.i43 + m.b267 <= 0)

m.c737 = Constraint(expr= - m.i44 + m.b268 <= 0)

m.c738 = Constraint(expr= - m.i45 + m.b269 <= 0)

m.c739 = Constraint(expr= - m.i46 + m.b270 <= 0)

m.c740 = Constraint(expr= - m.i47 + m.b271 <= 0)

m.c741 = Constraint(expr= - m.i48 + m.b272 <= 0)

m.c742 = Constraint(expr= - m.i49 + m.b273 <= 0)

m.c743 = Constraint(expr= - m.i50 + m.b274 <= 0)

m.c744 = Constraint(expr= - m.i51 + m.b275 <= 0)

m.c745 = Constraint(expr= - m.i52 + m.b276 <= 0)

m.c746 = Constraint(expr= - m.i53 + m.b277 <= 0)

m.c747 = Constraint(expr= - m.i54 + m.b278 <= 0)

m.c748 = Constraint(expr= - m.i55 + m.b279 <= 0)

m.c749 = Constraint(expr= - m.i56 + m.b280 <= 0)

m.c750 = Constraint(expr= - m.i57 + m.b281 <= 0)

m.c751 = Constraint(expr= - m.i58 + m.b282 <= 0)

m.c752 = Constraint(expr= - m.i59 + m.b283 <= 0)

m.c753 = Constraint(expr= - m.i60 + m.b284 <= 0)

m.c754 = Constraint(expr= - m.i61 + m.b285 <= 0)

m.c755 = Constraint(expr= - m.i62 + m.b286 <= 0)

m.c756 = Constraint(expr= - m.i63 + m.b287 <= 0)

m.c757 = Constraint(expr= - m.i64 + m.b288 <= 0)

m.c758 = Constraint(expr= - m.i65 + m.b289 <= 0)

m.c759 = Constraint(expr= - m.i66 + m.b290 <= 0)

m.c760 = Constraint(expr= - m.i67 + m.b291 <= 0)

m.c761 = Constraint(expr= - m.i68 + m.b292 <= 0)

m.c762 = Constraint(expr= - m.i69 + m.b293 <= 0)

m.c763 = Constraint(expr= - m.i70 + m.b294 <= 0)

m.c764 = Constraint(expr= - m.i71 + m.b295 <= 0)

m.c765 = Constraint(expr= - m.i72 + m.b296 <= 0)

m.c766 = Constraint(expr= - m.i73 + m.b297 <= 0)

m.c767 = Constraint(expr= - m.i74 + m.b298 <= 0)

m.c768 = Constraint(expr= - m.i75 + m.b299 <= 0)

m.c769 = Constraint(expr= - m.i76 + m.b300 <= 0)

m.c770 = Constraint(expr= - m.i77 + m.b301 <= 0)

m.c771 = Constraint(expr= - m.i78 + m.b302 <= 0)

m.c772 = Constraint(expr= - m.i79 + m.b303 <= 0)

m.c773 = Constraint(expr= - m.i80 + m.b304 <= 0)

m.c774 = Constraint(expr= - m.i81 + m.b305 <= 0)

m.c775 = Constraint(expr= - m.i82 + m.b306 <= 0)

m.c776 = Constraint(expr= - m.i83 + m.b307 <= 0)

m.c777 = Constraint(expr= - m.i84 + m.b308 <= 0)

m.c778 = Constraint(expr= - m.i85 + m.b309 <= 0)

m.c779 = Constraint(expr= - m.i86 + m.b310 <= 0)

m.c780 = Constraint(expr= - m.i87 + m.b311 <= 0)

m.c781 = Constraint(expr= - m.i88 + m.b312 <= 0)

m.c782 = Constraint(expr= - m.i89 + m.b313 <= 0)

m.c783 = Constraint(expr= - m.i90 + m.b314 <= 0)

m.c784 = Constraint(expr= - m.i91 + m.b315 <= 0)

m.c785 = Constraint(expr= - m.i92 + m.b316 <= 0)

m.c786 = Constraint(expr= - m.i93 + m.b317 <= 0)

m.c787 = Constraint(expr= - m.i94 + m.b318 <= 0)

m.c788 = Constraint(expr= - m.i95 + m.b319 <= 0)

m.c789 = Constraint(expr= - m.i96 + m.b320 <= 0)

m.c790 = Constraint(expr= - m.i97 + m.b321 <= 0)

m.c791 = Constraint(expr=   m.i26 - 4*m.b250 <= 0)

m.c792 = Constraint(expr=   m.i27 - 4*m.b251 <= 0)

m.c793 = Constraint(expr=   m.i28 - 4*m.b252 <= 0)

m.c794 = Constraint(expr=   m.i29 - 4*m.b253 <= 0)

m.c795 = Constraint(expr=   m.i30 - 4*m.b254 <= 0)

m.c796 = Constraint(expr=   m.i31 - 4*m.b255 <= 0)

m.c797 = Constraint(expr=   m.i32 - 4*m.b256 <= 0)

m.c798 = Constraint(expr=   m.i33 - 4*m.b257 <= 0)

m.c799 = Constraint(expr=   m.i34 - 4*m.b258 <= 0)

m.c800 = Constraint(expr=   m.i35 - 4*m.b259 <= 0)

m.c801 = Constraint(expr=   m.i36 - 4*m.b260 <= 0)

m.c802 = Constraint(expr=   m.i37 - 4*m.b261 <= 0)

m.c803 = Constraint(expr=   m.i38 - 4*m.b262 <= 0)

m.c804 = Constraint(expr=   m.i39 - 4*m.b263 <= 0)

m.c805 = Constraint(expr=   m.i40 - 4*m.b264 <= 0)

m.c806 = Constraint(expr=   m.i41 - 4*m.b265 <= 0)

m.c807 = Constraint(expr=   m.i42 - 4*m.b266 <= 0)

m.c808 = Constraint(expr=   m.i43 - 4*m.b267 <= 0)

m.c809 = Constraint(expr=   m.i44 - 4*m.b268 <= 0)

m.c810 = Constraint(expr=   m.i45 - 4*m.b269 <= 0)

m.c811 = Constraint(expr=   m.i46 - 4*m.b270 <= 0)

m.c812 = Constraint(expr=   m.i47 - 4*m.b271 <= 0)

m.c813 = Constraint(expr=   m.i48 - 4*m.b272 <= 0)

m.c814 = Constraint(expr=   m.i49 - 4*m.b273 <= 0)

m.c815 = Constraint(expr=   m.i50 - 4*m.b274 <= 0)

m.c816 = Constraint(expr=   m.i51 - 4*m.b275 <= 0)

m.c817 = Constraint(expr=   m.i52 - 4*m.b276 <= 0)

m.c818 = Constraint(expr=   m.i53 - 4*m.b277 <= 0)

m.c819 = Constraint(expr=   m.i54 - 4*m.b278 <= 0)

m.c820 = Constraint(expr=   m.i55 - 4*m.b279 <= 0)

m.c821 = Constraint(expr=   m.i56 - 4*m.b280 <= 0)

m.c822 = Constraint(expr=   m.i57 - 4*m.b281 <= 0)

m.c823 = Constraint(expr=   m.i58 - 4*m.b282 <= 0)

m.c824 = Constraint(expr=   m.i59 - 4*m.b283 <= 0)

m.c825 = Constraint(expr=   m.i60 - 4*m.b284 <= 0)

m.c826 = Constraint(expr=   m.i61 - 4*m.b285 <= 0)

m.c827 = Constraint(expr=   m.i62 - 4*m.b286 <= 0)

m.c828 = Constraint(expr=   m.i63 - 4*m.b287 <= 0)

m.c829 = Constraint(expr=   m.i64 - 4*m.b288 <= 0)

m.c830 = Constraint(expr=   m.i65 - 4*m.b289 <= 0)

m.c831 = Constraint(expr=   m.i66 - 4*m.b290 <= 0)

m.c832 = Constraint(expr=   m.i67 - 4*m.b291 <= 0)

m.c833 = Constraint(expr=   m.i68 - 4*m.b292 <= 0)

m.c834 = Constraint(expr=   m.i69 - 4*m.b293 <= 0)

m.c835 = Constraint(expr=   m.i70 - 4*m.b294 <= 0)

m.c836 = Constraint(expr=   m.i71 - 4*m.b295 <= 0)

m.c837 = Constraint(expr=   m.i72 - 4*m.b296 <= 0)

m.c838 = Constraint(expr=   m.i73 - 4*m.b297 <= 0)

m.c839 = Constraint(expr=   m.i74 - 4*m.b298 <= 0)

m.c840 = Constraint(expr=   m.i75 - 4*m.b299 <= 0)

m.c841 = Constraint(expr=   m.i76 - 4*m.b300 <= 0)

m.c842 = Constraint(expr=   m.i77 - 4*m.b301 <= 0)

m.c843 = Constraint(expr=   m.i78 - 4*m.b302 <= 0)

m.c844 = Constraint(expr=   m.i79 - 4*m.b303 <= 0)

m.c845 = Constraint(expr=   m.i80 - 4*m.b304 <= 0)

m.c846 = Constraint(expr=   m.i81 - 4*m.b305 <= 0)

m.c847 = Constraint(expr=   m.i82 - 4*m.b306 <= 0)

m.c848 = Constraint(expr=   m.i83 - 4*m.b307 <= 0)

m.c849 = Constraint(expr=   m.i84 - 4*m.b308 <= 0)

m.c850 = Constraint(expr=   m.i85 - 4*m.b309 <= 0)

m.c851 = Constraint(expr=   m.i86 - 4*m.b310 <= 0)

m.c852 = Constraint(expr=   m.i87 - 4*m.b311 <= 0)

m.c853 = Constraint(expr=   m.i88 - 4*m.b312 <= 0)

m.c854 = Constraint(expr=   m.i89 - 4*m.b313 <= 0)

m.c855 = Constraint(expr=   m.i90 - 4*m.b314 <= 0)

m.c856 = Constraint(expr=   m.i91 - 4*m.b315 <= 0)

m.c857 = Constraint(expr=   m.i92 - 4*m.b316 <= 0)

m.c858 = Constraint(expr=   m.i93 - 4*m.b317 <= 0)

m.c859 = Constraint(expr=   m.i94 - 4*m.b318 <= 0)

m.c860 = Constraint(expr=   m.i95 - 4*m.b319 <= 0)

m.c861 = Constraint(expr=   m.i96 - 4*m.b320 <= 0)

m.c862 = Constraint(expr=   m.i97 - 4*m.b321 <= 0)

m.c863 = Constraint(expr=m.b98*m.x322 + 1.1*m.b122*m.x322 + 1.2*m.b146*m.x322 + 1.3*m.b170*m.x322 + 1.4*m.b194*m.x322 + 
                         1.5*m.b218*m.x322 - m.x330 == 0)

m.c864 = Constraint(expr=m.b106*m.x322 + 1.1*m.b130*m.x322 + 1.2*m.b154*m.x322 + 1.3*m.b178*m.x322 + 1.4*m.b202*m.x322
                          + 1.5*m.b226*m.x322 - m.x331 == 0)

m.c865 = Constraint(expr=m.b114*m.x322 + 1.1*m.b138*m.x322 + 1.2*m.b162*m.x322 + 1.3*m.b186*m.x322 + 1.4*m.b210*m.x322
                          + 1.5*m.b234*m.x322 - m.x332 == 0)

m.c866 = Constraint(expr=m.b99*m.x323 + 1.1*m.b123*m.x323 + 1.2*m.b147*m.x323 + 1.3*m.b171*m.x323 + 1.4*m.b195*m.x323 + 
                         1.5*m.b219*m.x323 - m.x333 == 0)

m.c867 = Constraint(expr=m.b107*m.x323 + 1.1*m.b131*m.x323 + 1.2*m.b155*m.x323 + 1.3*m.b179*m.x323 + 1.4*m.b203*m.x323
                          + 1.5*m.b227*m.x323 - m.x334 == 0)

m.c868 = Constraint(expr=m.b115*m.x323 + 1.1*m.b139*m.x323 + 1.2*m.b163*m.x323 + 1.3*m.b187*m.x323 + 1.4*m.b211*m.x323
                          + 1.5*m.b235*m.x323 - m.x335 == 0)

m.c869 = Constraint(expr=m.b100*m.x324 + 1.1*m.b124*m.x324 + 1.2*m.b148*m.x324 + 1.3*m.b172*m.x324 + 1.4*m.b196*m.x324
                          + 1.5*m.b220*m.x324 - m.x336 == 0)

m.c870 = Constraint(expr=m.b108*m.x324 + 1.1*m.b132*m.x324 + 1.2*m.b156*m.x324 + 1.3*m.b180*m.x324 + 1.4*m.b204*m.x324
                          + 1.5*m.b228*m.x324 - m.x337 == 0)

m.c871 = Constraint(expr=m.b116*m.x324 + 1.1*m.b140*m.x324 + 1.2*m.b164*m.x324 + 1.3*m.b188*m.x324 + 1.4*m.b212*m.x324
                          + 1.5*m.b236*m.x324 - m.x338 == 0)

m.c872 = Constraint(expr=m.b101*m.x325 + 1.1*m.b125*m.x325 + 1.2*m.b149*m.x325 + 1.3*m.b173*m.x325 + 1.4*m.b197*m.x325
                          + 1.5*m.b221*m.x325 - m.x339 == 0)

m.c873 = Constraint(expr=m.b109*m.x325 + 1.1*m.b133*m.x325 + 1.2*m.b157*m.x325 + 1.3*m.b181*m.x325 + 1.4*m.b205*m.x325
                          + 1.5*m.b229*m.x325 - m.x340 == 0)

m.c874 = Constraint(expr=m.b117*m.x325 + 1.1*m.b141*m.x325 + 1.2*m.b165*m.x325 + 1.3*m.b189*m.x325 + 1.4*m.b213*m.x325
                          + 1.5*m.b237*m.x325 - m.x341 == 0)

m.c875 = Constraint(expr=m.b102*m.x326 + 1.1*m.b126*m.x326 + 1.2*m.b150*m.x326 + 1.3*m.b174*m.x326 + 1.4*m.b198*m.x326
                          + 1.5*m.b222*m.x326 - m.x342 == 0)

m.c876 = Constraint(expr=m.b110*m.x326 + 1.1*m.b134*m.x326 + 1.2*m.b158*m.x326 + 1.3*m.b182*m.x326 + 1.4*m.b206*m.x326
                          + 1.5*m.b230*m.x326 - m.x343 == 0)

m.c877 = Constraint(expr=m.b118*m.x326 + 1.1*m.b142*m.x326 + 1.2*m.b166*m.x326 + 1.3*m.b190*m.x326 + 1.4*m.b214*m.x326
                          + 1.5*m.b238*m.x326 - m.x344 == 0)

m.c878 = Constraint(expr=m.b103*m.x327 + 1.1*m.b127*m.x327 + 1.2*m.b151*m.x327 + 1.3*m.b175*m.x327 + 1.4*m.b199*m.x327
                          + 1.5*m.b223*m.x327 - m.x345 == 0)

m.c879 = Constraint(expr=m.b111*m.x327 + 1.1*m.b135*m.x327 + 1.2*m.b159*m.x327 + 1.3*m.b183*m.x327 + 1.4*m.b207*m.x327
                          + 1.5*m.b231*m.x327 - m.x346 == 0)

m.c880 = Constraint(expr=m.b119*m.x327 + 1.1*m.b143*m.x327 + 1.2*m.b167*m.x327 + 1.3*m.b191*m.x327 + 1.4*m.b215*m.x327
                          + 1.5*m.b239*m.x327 - m.x347 == 0)

m.c881 = Constraint(expr=m.b104*m.x328 + 1.1*m.b128*m.x328 + 1.2*m.b152*m.x328 + 1.3*m.b176*m.x328 + 1.4*m.b200*m.x328
                          + 1.5*m.b224*m.x328 - m.x348 == 0)

m.c882 = Constraint(expr=m.b112*m.x328 + 1.1*m.b136*m.x328 + 1.2*m.b160*m.x328 + 1.3*m.b184*m.x328 + 1.4*m.b208*m.x328
                          + 1.5*m.b232*m.x328 - m.x349 == 0)

m.c883 = Constraint(expr=m.b120*m.x328 + 1.1*m.b144*m.x328 + 1.2*m.b168*m.x328 + 1.3*m.b192*m.x328 + 1.4*m.b216*m.x328
                          + 1.5*m.b240*m.x328 - m.x350 == 0)

m.c884 = Constraint(expr=m.b105*m.x329 + 1.1*m.b129*m.x329 + 1.2*m.b153*m.x329 + 1.3*m.b177*m.x329 + 1.4*m.b201*m.x329
                          + 1.5*m.b225*m.x329 - m.x351 == 0)

m.c885 = Constraint(expr=m.b113*m.x329 + 1.1*m.b137*m.x329 + 1.2*m.b161*m.x329 + 1.3*m.b185*m.x329 + 1.4*m.b209*m.x329
                          + 1.5*m.b233*m.x329 - m.x352 == 0)

m.c886 = Constraint(expr=m.b121*m.x329 + 1.1*m.b145*m.x329 + 1.2*m.b169*m.x329 + 1.3*m.b193*m.x329 + 1.4*m.b217*m.x329
                          + 1.5*m.b241*m.x329 - m.x353 == 0)

m.c887 = Constraint(expr=0.33*m.i26*m.x322 + 0.26*m.i34*m.x322 + 0.48*m.i42*m.x322 + 0.44*m.i50*m.x322 + 0.711*m.i58*
                         m.x322 + 0.35*m.i66*m.x322 + 0.3*m.i74*m.x322 + 0.45*m.i82*m.x322 + 0.45*m.i90*m.x322 - m.x354
                          == 0)

m.c888 = Constraint(expr=0.33*m.i27*m.x323 + 0.26*m.i35*m.x323 + 0.48*m.i43*m.x323 + 0.44*m.i51*m.x323 + 0.711*m.i59*
                         m.x323 + 0.35*m.i67*m.x323 + 0.3*m.i75*m.x323 + 0.45*m.i83*m.x323 + 0.45*m.i91*m.x323 - m.x355
                          == 0)

m.c889 = Constraint(expr=0.33*m.i28*m.x324 + 0.26*m.i36*m.x324 + 0.48*m.i44*m.x324 + 0.44*m.i52*m.x324 + 0.711*m.i60*
                         m.x324 + 0.35*m.i68*m.x324 + 0.3*m.i76*m.x324 + 0.45*m.i84*m.x324 + 0.45*m.i92*m.x324 - m.x356
                          == 0)

m.c890 = Constraint(expr=0.33*m.i29*m.x325 + 0.26*m.i37*m.x325 + 0.48*m.i45*m.x325 + 0.44*m.i53*m.x325 + 0.711*m.i61*
                         m.x325 + 0.35*m.i69*m.x325 + 0.3*m.i77*m.x325 + 0.45*m.i85*m.x325 + 0.45*m.i93*m.x325 - m.x357
                          == 0)

m.c891 = Constraint(expr=0.33*m.i30*m.x326 + 0.26*m.i38*m.x326 + 0.48*m.i46*m.x326 + 0.44*m.i54*m.x326 + 0.711*m.i62*
                         m.x326 + 0.35*m.i70*m.x326 + 0.3*m.i78*m.x326 + 0.45*m.i86*m.x326 + 0.45*m.i94*m.x326 - m.x358
                          == 0)

m.c892 = Constraint(expr=0.33*m.i31*m.x327 + 0.26*m.i39*m.x327 + 0.48*m.i47*m.x327 + 0.44*m.i55*m.x327 + 0.711*m.i63*
                         m.x327 + 0.35*m.i71*m.x327 + 0.3*m.i79*m.x327 + 0.45*m.i87*m.x327 + 0.45*m.i95*m.x327 - m.x359
                          == 0)

m.c893 = Constraint(expr=0.33*m.i32*m.x328 + 0.26*m.i40*m.x328 + 0.48*m.i48*m.x328 + 0.44*m.i56*m.x328 + 0.711*m.i64*
                         m.x328 + 0.35*m.i72*m.x328 + 0.3*m.i80*m.x328 + 0.45*m.i88*m.x328 + 0.45*m.i96*m.x328 - m.x360
                          == 0)

m.c894 = Constraint(expr=0.33*m.i33*m.x329 + 0.26*m.i41*m.x329 + 0.48*m.i49*m.x329 + 0.44*m.i57*m.x329 + 0.711*m.i65*
                         m.x329 + 0.35*m.i73*m.x329 + 0.3*m.i81*m.x329 + 0.45*m.i89*m.x329 + 0.45*m.i97*m.x329 - m.x361
                          == 0)
