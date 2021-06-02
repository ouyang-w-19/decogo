#  MINLP written by GAMS Convert at 04/21/18 13:51:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        138       92        7       39        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        401       93      308        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        958      900       58        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x30 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x31 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x32 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x33 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x34 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x35 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x36 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x37 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x38 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x39 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x40 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x41 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x42 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x43 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x44 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x45 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x46 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x47 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x48 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x49 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x50 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x51 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x52 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x53 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x54 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x55 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x56 = Var(within=Reals,bounds=(0.01,10),initialize=1)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,None),initialize=100)
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
m.x401 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x401, sense=minimize)

m.c1 = Constraint(expr=(-m.x92*m.x401) - ((479700 - 479700*exp(-0.1*m.x1/m.x29))*m.x29 + 31980*m.x1 - 100*m.x29 + (
                       252000 - 252000*exp(-0.2*m.x2/m.x30))*m.x30 + 22680*m.x2 - 90*m.x30 + (423500 - 423500*exp(-0.1*
                       m.x3/m.x31))*m.x31 + 25410*m.x3 - 80*m.x31 + (157440 - 157440*exp(-0.2*m.x4/m.x32))*m.x32 + 19680
                       *m.x4 - 75*m.x32 + (172108.695652174 - 172108.695652174*exp(-0.23*m.x5/m.x33))*m.x33 + 40950*m.x5
                        - 90*m.x33 + (33970.5882352941 - 33970.5882352941*exp(-0.34*m.x6/m.x34))*m.x34 + 8580*m.x6 - 93*
                       m.x34 + (130200 - 130200*exp(-0.2*m.x7/m.x35))*m.x35 + 13440*m.x7 - 78*m.x35 + (200640 - 200640*
                       exp(-0.2*m.x8/m.x36))*m.x36 + 26334*m.x8 - 80*m.x36 + (526680 - 526680*exp(-0.1*m.x9/m.x37))*
                       m.x37 + 26334*m.x9 - 85*m.x37 + (212850 - 212850*exp(-0.2*m.x10/m.x38))*m.x38 + 29670*m.x10 - 75*
                       m.x38 + (141360 - 141360*exp(-0.25*m.x11/m.x39))*m.x39 + 28500*m.x11 - 90*m.x39 + (
                       152937.931034483 - 152937.931034483*exp(-0.29*m.x12/m.x40))*m.x40 + 49104*m.x12 - 94*m.x40 + (
                       76444.4444444444 - 76444.4444444444*exp(-0.27*m.x13/m.x41))*m.x41 + 13932*m.x13 - 78*m.x41 + (
                       76840 - 76840*exp(-0.3*m.x14/m.x42))*m.x42 + 11526*m.x14 - 70*m.x42 + (102300 - 102300*exp(-0.3*
                       m.x15/m.x43))*m.x43 + 18810*m.x15 - 90*m.x43 + (170800 - 170800*exp(-0.2*m.x16/m.x44))*m.x44 + 
                       17568*m.x16 - 90*m.x44 + (115200 - 115200*exp(-0.3*m.x17/m.x45))*m.x45 + 20160*m.x17 - 90*m.x45
                        + (176000 - 176000*exp(-0.27*m.x18/m.x46))*m.x46 + 30360*m.x18 - 85*m.x46 + (126357.142857143 - 
                       126357.142857143*exp(-0.28*m.x19/m.x47))*m.x47 + 36600*m.x19 - 93*m.x47 + (45931.0344827586 - 
                       45931.0344827586*exp(-0.29*m.x20/m.x48))*m.x48 + 9000*m.x20 - 92*m.x48 + (123318 - 123318*exp(-
                       0.25*m.x21/m.x49))*m.x49 + 17901*m.x21 - 75*m.x49 + (223200 - 223200*exp(-0.2*m.x22/m.x50))*m.x50
                        + 28800*m.x22 - 80*m.x50 + (225000 - 225000*exp(-0.2*m.x23/m.x51))*m.x51 + 23750*m.x23 - 90*
                       m.x51 + (240800 - 240800*exp(-0.15*m.x24/m.x52))*m.x52 + 21672*m.x24 - 85*m.x52 + (115920 - 
                       115920*exp(-0.25*m.x25/m.x53))*m.x53 + 19320*m.x25 - 80*m.x53 + (133241.379310345 - 
                       133241.379310345*exp(-0.29*m.x26/m.x54))*m.x54 + 42780*m.x26 - 92*m.x54 + (90763.6363636364 - 
                       90763.6363636364*exp(-0.22*m.x27/m.x55))*m.x55 + 13312*m.x27 - 85*m.x55 + (78857.1428571429 - 
                       78857.1428571429*exp(-0.28*m.x28/m.x56))*m.x56 + 11730*m.x28 - 72*m.x56) == 0)

m.c2 = Constraint(expr= - 1300*m.x1 - 1100*m.x8 - 900*m.x15 - 1200*m.x22 + m.x57 + 300*m.x92 == 0)

m.c3 = Constraint(expr= - 1200*m.x2 - 1050*m.x9 - 800*m.x16 - 1000*m.x23 + m.x58 + 400*m.x92 == 0)

m.c4 = Constraint(expr= - 1100*m.x3 - 1000*m.x10 - 800*m.x17 - 800*m.x24 + m.x59 + 300*m.x92 == 0)

m.c5 = Constraint(expr= - 800*m.x4 - 1000*m.x11 - 1200*m.x18 - 700*m.x25 + m.x60 + 500*m.x92 == 0)

m.c6 = Constraint(expr= - 1300*m.x5 - 1200*m.x12 - 1000*m.x19 - 1200*m.x26 + m.x61 + 500*m.x92 == 0)

m.c7 = Constraint(expr= - 300*m.x6 - 400*m.x13 - 300*m.x20 - 400*m.x27 + m.x62 + 100*m.x92 == 0)

m.c8 = Constraint(expr= - 700*m.x7 - 600*m.x14 - 850*m.x21 - 600*m.x28 + m.x63 + 600*m.x92 == 0)

m.c9 = Constraint(expr=   m.x57 - 300*m.x92 <= 0)

m.c10 = Constraint(expr=   m.x58 - 300*m.x92 <= 0)

m.c11 = Constraint(expr=   m.x59 - 300*m.x92 <= 0)

m.c12 = Constraint(expr=   m.x60 - 300*m.x92 <= 0)

m.c13 = Constraint(expr=   m.x61 - 300*m.x92 <= 0)

m.c14 = Constraint(expr=   m.x62 - 300*m.x92 <= 0)

m.c15 = Constraint(expr=   m.x63 - 300*m.x92 <= 0)

m.c16 = Constraint(expr=   m.x29 - 0.01*m.b93 - m.b94 - 2*m.b95 - 3*m.b96 - 4*m.b97 - 5*m.b98 - 6*m.b99 - 7*m.b100
                         - 8*m.b101 - 9*m.b102 - 10*m.b103 == 0)

m.c17 = Constraint(expr=   m.x30 - 0.01*m.b104 - m.b105 - 2*m.b106 - 3*m.b107 - 4*m.b108 - 5*m.b109 - 6*m.b110
                         - 7*m.b111 - 8*m.b112 - 9*m.b113 - 10*m.b114 == 0)

m.c18 = Constraint(expr=   m.x31 - 0.01*m.b115 - m.b116 - 2*m.b117 - 3*m.b118 - 4*m.b119 - 5*m.b120 - 6*m.b121
                         - 7*m.b122 - 8*m.b123 - 9*m.b124 - 10*m.b125 == 0)

m.c19 = Constraint(expr=   m.x32 - 0.01*m.b126 - m.b127 - 2*m.b128 - 3*m.b129 - 4*m.b130 - 5*m.b131 - 6*m.b132
                         - 7*m.b133 - 8*m.b134 - 9*m.b135 - 10*m.b136 == 0)

m.c20 = Constraint(expr=   m.x33 - 0.01*m.b137 - m.b138 - 2*m.b139 - 3*m.b140 - 4*m.b141 - 5*m.b142 - 6*m.b143
                         - 7*m.b144 - 8*m.b145 - 9*m.b146 - 10*m.b147 == 0)

m.c21 = Constraint(expr=   m.x34 - 0.01*m.b148 - m.b149 - 2*m.b150 - 3*m.b151 - 4*m.b152 - 5*m.b153 - 6*m.b154
                         - 7*m.b155 - 8*m.b156 - 9*m.b157 - 10*m.b158 == 0)

m.c22 = Constraint(expr=   m.x35 - 0.01*m.b159 - m.b160 - 2*m.b161 - 3*m.b162 - 4*m.b163 - 5*m.b164 - 6*m.b165
                         - 7*m.b166 - 8*m.b167 - 9*m.b168 - 10*m.b169 == 0)

m.c23 = Constraint(expr=   m.x36 - 0.01*m.b170 - m.b171 - 2*m.b172 - 3*m.b173 - 4*m.b174 - 5*m.b175 - 6*m.b176
                         - 7*m.b177 - 8*m.b178 - 9*m.b179 - 10*m.b180 == 0)

m.c24 = Constraint(expr=   m.x37 - 0.01*m.b181 - m.b182 - 2*m.b183 - 3*m.b184 - 4*m.b185 - 5*m.b186 - 6*m.b187
                         - 7*m.b188 - 8*m.b189 - 9*m.b190 - 10*m.b191 == 0)

m.c25 = Constraint(expr=   m.x38 - 0.01*m.b192 - m.b193 - 2*m.b194 - 3*m.b195 - 4*m.b196 - 5*m.b197 - 6*m.b198
                         - 7*m.b199 - 8*m.b200 - 9*m.b201 - 10*m.b202 == 0)

m.c26 = Constraint(expr=   m.x39 - 0.01*m.b203 - m.b204 - 2*m.b205 - 3*m.b206 - 4*m.b207 - 5*m.b208 - 6*m.b209
                         - 7*m.b210 - 8*m.b211 - 9*m.b212 - 10*m.b213 == 0)

m.c27 = Constraint(expr=   m.x40 - 0.01*m.b214 - m.b215 - 2*m.b216 - 3*m.b217 - 4*m.b218 - 5*m.b219 - 6*m.b220
                         - 7*m.b221 - 8*m.b222 - 9*m.b223 - 10*m.b224 == 0)

m.c28 = Constraint(expr=   m.x41 - 0.01*m.b225 - m.b226 - 2*m.b227 - 3*m.b228 - 4*m.b229 - 5*m.b230 - 6*m.b231
                         - 7*m.b232 - 8*m.b233 - 9*m.b234 - 10*m.b235 == 0)

m.c29 = Constraint(expr=   m.x42 - 0.01*m.b236 - m.b237 - 2*m.b238 - 3*m.b239 - 4*m.b240 - 5*m.b241 - 6*m.b242
                         - 7*m.b243 - 8*m.b244 - 9*m.b245 - 10*m.b246 == 0)

m.c30 = Constraint(expr=   m.x43 - 0.01*m.b247 - m.b248 - 2*m.b249 - 3*m.b250 - 4*m.b251 - 5*m.b252 - 6*m.b253
                         - 7*m.b254 - 8*m.b255 - 9*m.b256 - 10*m.b257 == 0)

m.c31 = Constraint(expr=   m.x44 - 0.01*m.b258 - m.b259 - 2*m.b260 - 3*m.b261 - 4*m.b262 - 5*m.b263 - 6*m.b264
                         - 7*m.b265 - 8*m.b266 - 9*m.b267 - 10*m.b268 == 0)

m.c32 = Constraint(expr=   m.x45 - 0.01*m.b269 - m.b270 - 2*m.b271 - 3*m.b272 - 4*m.b273 - 5*m.b274 - 6*m.b275
                         - 7*m.b276 - 8*m.b277 - 9*m.b278 - 10*m.b279 == 0)

m.c33 = Constraint(expr=   m.x46 - 0.01*m.b280 - m.b281 - 2*m.b282 - 3*m.b283 - 4*m.b284 - 5*m.b285 - 6*m.b286
                         - 7*m.b287 - 8*m.b288 - 9*m.b289 - 10*m.b290 == 0)

m.c34 = Constraint(expr=   m.x47 - 0.01*m.b291 - m.b292 - 2*m.b293 - 3*m.b294 - 4*m.b295 - 5*m.b296 - 6*m.b297
                         - 7*m.b298 - 8*m.b299 - 9*m.b300 - 10*m.b301 == 0)

m.c35 = Constraint(expr=   m.x48 - 0.01*m.b302 - m.b303 - 2*m.b304 - 3*m.b305 - 4*m.b306 - 5*m.b307 - 6*m.b308
                         - 7*m.b309 - 8*m.b310 - 9*m.b311 - 10*m.b312 == 0)

m.c36 = Constraint(expr=   m.x49 - 0.01*m.b313 - m.b314 - 2*m.b315 - 3*m.b316 - 4*m.b317 - 5*m.b318 - 6*m.b319
                         - 7*m.b320 - 8*m.b321 - 9*m.b322 - 10*m.b323 == 0)

m.c37 = Constraint(expr=   m.x50 - 0.01*m.b324 - m.b325 - 2*m.b326 - 3*m.b327 - 4*m.b328 - 5*m.b329 - 6*m.b330
                         - 7*m.b331 - 8*m.b332 - 9*m.b333 - 10*m.b334 == 0)

m.c38 = Constraint(expr=   m.x51 - 0.01*m.b335 - m.b336 - 2*m.b337 - 3*m.b338 - 4*m.b339 - 5*m.b340 - 6*m.b341
                         - 7*m.b342 - 8*m.b343 - 9*m.b344 - 10*m.b345 == 0)

m.c39 = Constraint(expr=   m.x52 - 0.01*m.b346 - m.b347 - 2*m.b348 - 3*m.b349 - 4*m.b350 - 5*m.b351 - 6*m.b352
                         - 7*m.b353 - 8*m.b354 - 9*m.b355 - 10*m.b356 == 0)

m.c40 = Constraint(expr=   m.x53 - 0.01*m.b357 - m.b358 - 2*m.b359 - 3*m.b360 - 4*m.b361 - 5*m.b362 - 6*m.b363
                         - 7*m.b364 - 8*m.b365 - 9*m.b366 - 10*m.b367 == 0)

m.c41 = Constraint(expr=   m.x54 - 0.01*m.b368 - m.b369 - 2*m.b370 - 3*m.b371 - 4*m.b372 - 5*m.b373 - 6*m.b374
                         - 7*m.b375 - 8*m.b376 - 9*m.b377 - 10*m.b378 == 0)

m.c42 = Constraint(expr=   m.x55 - 0.01*m.b379 - m.b380 - 2*m.b381 - 3*m.b382 - 4*m.b383 - 5*m.b384 - 6*m.b385
                         - 7*m.b386 - 8*m.b387 - 9*m.b388 - 10*m.b389 == 0)

m.c43 = Constraint(expr=   m.x56 - 0.01*m.b390 - m.b391 - 2*m.b392 - 3*m.b393 - 4*m.b394 - 5*m.b395 - 6*m.b396
                         - 7*m.b397 - 8*m.b398 - 9*m.b399 - 10*m.b400 == 0)

m.c44 = Constraint(expr= - m.b93 - m.b94 - m.b95 - m.b96 - m.b97 - m.b98 - m.b99 - m.b100 - m.b101 - m.b102 - m.b103
                         == -1)

m.c45 = Constraint(expr= - m.b104 - m.b105 - m.b106 - m.b107 - m.b108 - m.b109 - m.b110 - m.b111 - m.b112 - m.b113
                         - m.b114 == -1)

m.c46 = Constraint(expr= - m.b115 - m.b116 - m.b117 - m.b118 - m.b119 - m.b120 - m.b121 - m.b122 - m.b123 - m.b124
                         - m.b125 == -1)

m.c47 = Constraint(expr= - m.b126 - m.b127 - m.b128 - m.b129 - m.b130 - m.b131 - m.b132 - m.b133 - m.b134 - m.b135
                         - m.b136 == -1)

m.c48 = Constraint(expr= - m.b137 - m.b138 - m.b139 - m.b140 - m.b141 - m.b142 - m.b143 - m.b144 - m.b145 - m.b146
                         - m.b147 == -1)

m.c49 = Constraint(expr= - m.b148 - m.b149 - m.b150 - m.b151 - m.b152 - m.b153 - m.b154 - m.b155 - m.b156 - m.b157
                         - m.b158 == -1)

m.c50 = Constraint(expr= - m.b159 - m.b160 - m.b161 - m.b162 - m.b163 - m.b164 - m.b165 - m.b166 - m.b167 - m.b168
                         - m.b169 == -1)

m.c51 = Constraint(expr= - m.b170 - m.b171 - m.b172 - m.b173 - m.b174 - m.b175 - m.b176 - m.b177 - m.b178 - m.b179
                         - m.b180 == -1)

m.c52 = Constraint(expr= - m.b181 - m.b182 - m.b183 - m.b184 - m.b185 - m.b186 - m.b187 - m.b188 - m.b189 - m.b190
                         - m.b191 == -1)

m.c53 = Constraint(expr= - m.b192 - m.b193 - m.b194 - m.b195 - m.b196 - m.b197 - m.b198 - m.b199 - m.b200 - m.b201
                         - m.b202 == -1)

m.c54 = Constraint(expr= - m.b203 - m.b204 - m.b205 - m.b206 - m.b207 - m.b208 - m.b209 - m.b210 - m.b211 - m.b212
                         - m.b213 == -1)

m.c55 = Constraint(expr= - m.b214 - m.b215 - m.b216 - m.b217 - m.b218 - m.b219 - m.b220 - m.b221 - m.b222 - m.b223
                         - m.b224 == -1)

m.c56 = Constraint(expr= - m.b225 - m.b226 - m.b227 - m.b228 - m.b229 - m.b230 - m.b231 - m.b232 - m.b233 - m.b234
                         - m.b235 == -1)

m.c57 = Constraint(expr= - m.b236 - m.b237 - m.b238 - m.b239 - m.b240 - m.b241 - m.b242 - m.b243 - m.b244 - m.b245
                         - m.b246 == -1)

m.c58 = Constraint(expr= - m.b247 - m.b248 - m.b249 - m.b250 - m.b251 - m.b252 - m.b253 - m.b254 - m.b255 - m.b256
                         - m.b257 == -1)

m.c59 = Constraint(expr= - m.b258 - m.b259 - m.b260 - m.b261 - m.b262 - m.b263 - m.b264 - m.b265 - m.b266 - m.b267
                         - m.b268 == -1)

m.c60 = Constraint(expr= - m.b269 - m.b270 - m.b271 - m.b272 - m.b273 - m.b274 - m.b275 - m.b276 - m.b277 - m.b278
                         - m.b279 == -1)

m.c61 = Constraint(expr= - m.b280 - m.b281 - m.b282 - m.b283 - m.b284 - m.b285 - m.b286 - m.b287 - m.b288 - m.b289
                         - m.b290 == -1)

m.c62 = Constraint(expr= - m.b291 - m.b292 - m.b293 - m.b294 - m.b295 - m.b296 - m.b297 - m.b298 - m.b299 - m.b300
                         - m.b301 == -1)

m.c63 = Constraint(expr= - m.b302 - m.b303 - m.b304 - m.b305 - m.b306 - m.b307 - m.b308 - m.b309 - m.b310 - m.b311
                         - m.b312 == -1)

m.c64 = Constraint(expr= - m.b313 - m.b314 - m.b315 - m.b316 - m.b317 - m.b318 - m.b319 - m.b320 - m.b321 - m.b322
                         - m.b323 == -1)

m.c65 = Constraint(expr= - m.b324 - m.b325 - m.b326 - m.b327 - m.b328 - m.b329 - m.b330 - m.b331 - m.b332 - m.b333
                         - m.b334 == -1)

m.c66 = Constraint(expr= - m.b335 - m.b336 - m.b337 - m.b338 - m.b339 - m.b340 - m.b341 - m.b342 - m.b343 - m.b344
                         - m.b345 == -1)

m.c67 = Constraint(expr= - m.b346 - m.b347 - m.b348 - m.b349 - m.b350 - m.b351 - m.b352 - m.b353 - m.b354 - m.b355
                         - m.b356 == -1)

m.c68 = Constraint(expr= - m.b357 - m.b358 - m.b359 - m.b360 - m.b361 - m.b362 - m.b363 - m.b364 - m.b365 - m.b366
                         - m.b367 == -1)

m.c69 = Constraint(expr= - m.b368 - m.b369 - m.b370 - m.b371 - m.b372 - m.b373 - m.b374 - m.b375 - m.b376 - m.b377
                         - m.b378 == -1)

m.c70 = Constraint(expr= - m.b379 - m.b380 - m.b381 - m.b382 - m.b383 - m.b384 - m.b385 - m.b386 - m.b387 - m.b388
                         - m.b389 == -1)

m.c71 = Constraint(expr= - m.b390 - m.b391 - m.b392 - m.b393 - m.b394 - m.b395 - m.b396 - m.b397 - m.b398 - m.b399
                         - m.b400 == -1)

m.c72 = Constraint(expr= - m.x1 - 2*m.x29 + m.x64 == 0)

m.c73 = Constraint(expr= - m.x2 - 3*m.x30 + m.x65 == 0)

m.c74 = Constraint(expr= - m.x3 - 3*m.x31 + m.x66 == 0)

m.c75 = Constraint(expr= - m.x4 - 3*m.x32 + m.x67 == 0)

m.c76 = Constraint(expr= - m.x5 - m.x33 + m.x68 == 0)

m.c77 = Constraint(expr= - m.x6 - 2*m.x34 + m.x69 == 0)

m.c78 = Constraint(expr= - m.x7 - 3*m.x35 + m.x70 == 0)

m.c79 = Constraint(expr= - m.x8 - 3*m.x36 + m.x71 == 0)

m.c80 = Constraint(expr= - m.x9 - m.x37 + m.x72 == 0)

m.c81 = Constraint(expr= - m.x10 - 2*m.x38 + m.x73 == 0)

m.c82 = Constraint(expr= - m.x11 - 2*m.x39 + m.x74 == 0)

m.c83 = Constraint(expr= - m.x12 - 2*m.x40 + m.x75 == 0)

m.c84 = Constraint(expr= - m.x13 - m.x41 + m.x76 == 0)

m.c85 = Constraint(expr= - m.x14 - m.x42 + m.x77 == 0)

m.c86 = Constraint(expr= - m.x15 - m.x43 + m.x78 == 0)

m.c87 = Constraint(expr= - m.x16 - 3*m.x44 + m.x79 == 0)

m.c88 = Constraint(expr= - m.x17 - m.x45 + m.x80 == 0)

m.c89 = Constraint(expr= - m.x18 - m.x46 + m.x81 == 0)

m.c90 = Constraint(expr= - m.x19 - 2*m.x47 + m.x82 == 0)

m.c91 = Constraint(expr= - m.x20 - m.x48 + m.x83 == 0)

m.c92 = Constraint(expr= - m.x21 - 2*m.x49 + m.x84 == 0)

m.c93 = Constraint(expr= - m.x22 - 2*m.x50 + m.x85 == 0)

m.c94 = Constraint(expr= - m.x23 - m.x51 + m.x86 == 0)

m.c95 = Constraint(expr= - m.x24 - 3*m.x52 + m.x87 == 0)

m.c96 = Constraint(expr= - m.x25 - 2*m.x53 + m.x88 == 0)

m.c97 = Constraint(expr= - m.x26 - 2*m.x54 + m.x89 == 0)

m.c98 = Constraint(expr= - m.x27 - m.x55 + m.x90 == 0)

m.c99 = Constraint(expr= - m.x28 - m.x56 + m.x91 == 0)

m.c100 = Constraint(expr=   m.x64 + m.x65 + m.x66 + m.x67 + m.x68 + m.x69 + m.x70 - m.x92 <= 0)

m.c101 = Constraint(expr=   m.x71 + m.x72 + m.x73 + m.x74 + m.x75 + m.x76 + m.x77 - m.x92 <= 0)

m.c102 = Constraint(expr=   m.x78 + m.x79 + m.x80 + m.x81 + m.x82 + m.x83 + m.x84 - m.x92 <= 0)

m.c103 = Constraint(expr=   m.x85 + m.x86 + m.x87 + m.x88 + m.x89 + m.x90 + m.x91 - m.x92 <= 0)

m.c104 = Constraint(expr=   m.x1 + 100*m.b93 <= 100)

m.c105 = Constraint(expr=   m.x2 + 100*m.b104 <= 100)

m.c106 = Constraint(expr=   m.x3 + 100*m.b115 <= 100)

m.c107 = Constraint(expr=   m.x4 + 100*m.b126 <= 100)

m.c108 = Constraint(expr=   m.x5 + 100*m.b137 <= 100)

m.c109 = Constraint(expr=   m.x6 + 100*m.b148 <= 100)

m.c110 = Constraint(expr=   m.x7 + 100*m.b159 <= 100)

m.c111 = Constraint(expr=   m.x8 + 100*m.b170 <= 100)

m.c112 = Constraint(expr=   m.x9 + 100*m.b181 <= 100)

m.c113 = Constraint(expr=   m.x10 + 100*m.b192 <= 100)

m.c114 = Constraint(expr=   m.x11 + 100*m.b203 <= 100)

m.c115 = Constraint(expr=   m.x12 + 100*m.b214 <= 100)

m.c116 = Constraint(expr=   m.x13 + 100*m.b225 <= 100)

m.c117 = Constraint(expr=   m.x14 + 100*m.b236 <= 100)

m.c118 = Constraint(expr=   m.x15 + 100*m.b247 <= 100)

m.c119 = Constraint(expr=   m.x16 + 100*m.b258 <= 100)

m.c120 = Constraint(expr=   m.x17 + 100*m.b269 <= 100)

m.c121 = Constraint(expr=   m.x18 + 100*m.b280 <= 100)

m.c122 = Constraint(expr=   m.x19 + 100*m.b291 <= 100)

m.c123 = Constraint(expr=   m.x20 + 100*m.b302 <= 100)

m.c124 = Constraint(expr=   m.x21 + 100*m.b313 <= 100)

m.c125 = Constraint(expr=   m.x22 + 100*m.b324 <= 100)

m.c126 = Constraint(expr=   m.x23 + 100*m.b335 <= 100)

m.c127 = Constraint(expr=   m.x24 + 100*m.b346 <= 100)

m.c128 = Constraint(expr=   m.x25 + 100*m.b357 <= 100)

m.c129 = Constraint(expr=   m.x26 + 100*m.b368 <= 100)

m.c130 = Constraint(expr=   m.x27 + 100*m.b379 <= 100)

m.c131 = Constraint(expr=   m.x28 + 100*m.b390 <= 100)

m.c132 = Constraint(expr=   m.x29 + m.x36 + m.x43 + m.x50 >= 1)

m.c133 = Constraint(expr=   m.x30 + m.x37 + m.x44 + m.x51 >= 1)

m.c134 = Constraint(expr=   m.x31 + m.x38 + m.x45 + m.x52 >= 1)

m.c135 = Constraint(expr=   m.x32 + m.x39 + m.x46 + m.x53 >= 1)

m.c136 = Constraint(expr=   m.x33 + m.x40 + m.x47 + m.x54 >= 1)

m.c137 = Constraint(expr=   m.x34 + m.x41 + m.x48 + m.x55 >= 1)

m.c138 = Constraint(expr=   m.x35 + m.x42 + m.x49 + m.x56 >= 1)
