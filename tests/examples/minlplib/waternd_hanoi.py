#  MINLP written by GAMS Convert at 04/21/18 13:55:14
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        202      134       34       34        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        305      101      204        0        0        0        0        0
#  FX      1        1        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        986      850      136        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(100,100),initialize=100)
m.x2 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x3 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x4 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x5 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x6 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x7 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x8 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x9 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x10 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x11 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x12 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x13 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x14 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x15 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x16 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x17 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x18 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x19 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x20 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x21 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x22 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x23 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x24 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x25 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x26 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x27 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x28 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x29 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x30 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x31 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x32 = Var(within=Reals,bounds=(30,100),initialize=30)
m.x33 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x68 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x69 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x70 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x71 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x72 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x73 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x74 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x75 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x76 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x77 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x78 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x79 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x80 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x81 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x82 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x83 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x84 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x85 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x86 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x87 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x88 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x89 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x90 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x91 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x92 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x93 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x94 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x95 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x96 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x97 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x98 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x99 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
m.x100 = Var(within=Reals,bounds=(0.0729658769900397,0.810731966555996),initialize=0.0729658769900397)
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

m.obj = Objective(expr=   4573*m.b101 + 7040*m.b102 + 9839*m.b103 + 12933*m.b104 + 18075*m.b105 + 27828*m.b106
                        + 61735.5*m.b107 + 95040*m.b108 + 132826.5*m.b109 + 174595.5*m.b110 + 244012.5*m.b111
                        + 375678*m.b112 + 41157*m.b113 + 63360*m.b114 + 88551*m.b115 + 116397*m.b116 + 162675*m.b117
                        + 250452*m.b118 + 100606*m.b119 + 154880*m.b120 + 216458*m.b121 + 284526*m.b122 + 397650*m.b123
                        + 612216*m.b124 + 52589.5*m.b125 + 80960*m.b126 + 113148.5*m.b127 + 148729.5*m.b128
                        + 207862.5*m.b129 + 320022*m.b130 + 66308.5*m.b131 + 102080*m.b132 + 142665.5*m.b133
                        + 187528.5*m.b134 + 262087.5*m.b135 + 403506*m.b136 + 20578.5*m.b137 + 31680*m.b138
                        + 44275.5*m.b139 + 58198.5*m.b140 + 81337.5*m.b141 + 125226*m.b142 + 38870.5*m.b143
                        + 59840*m.b144 + 83631.5*m.b145 + 109930.5*m.b146 + 153637.5*m.b147 + 236538*m.b148
                        + 38870.5*m.b149 + 59840*m.b150 + 83631.5*m.b151 + 109930.5*m.b152 + 153637.5*m.b153
                        + 236538*m.b154 + 36584*m.b155 + 56320*m.b156 + 78712*m.b157 + 103464*m.b158 + 144600*m.b159
                        + 222624*m.b160 + 43443.5*m.b161 + 66880*m.b162 + 93470.5*m.b163 + 122863.5*m.b164
                        + 171712.5*m.b165 + 264366*m.b166 + 36584*m.b167 + 56320*m.b168 + 78712*m.b169 + 103464*m.b170
                        + 144600*m.b171 + 222624*m.b172 + 54876*m.b173 + 84480*m.b174 + 118068*m.b175 + 155196*m.b176
                        + 216900*m.b177 + 333936*m.b178 + 160055*m.b179 + 246400*m.b180 + 344365*m.b181 + 452655*m.b182
                        + 632625*m.b183 + 973980*m.b184 + 22865*m.b185 + 35200*m.b186 + 49195*m.b187 + 64665*m.b188
                        + 90375*m.b189 + 139140*m.b190 + 25151.5*m.b191 + 38720*m.b192 + 54114.5*m.b193 + 71131.5*m.b194
                        + 99412.5*m.b195 + 153054*m.b196 + 124842.9*m.b197 + 192192*m.b198 + 268604.7*m.b199
                        + 353070.9*m.b200 + 493447.5*m.b201 + 759704.4*m.b202 + 80027.5*m.b203 + 123200*m.b204
                        + 172182.5*m.b205 + 226327.5*m.b206 + 316312.5*m.b207 + 486990*m.b208 + 36584*m.b209
                        + 56320*m.b210 + 78712*m.b211 + 103464*m.b212 + 144600*m.b213 + 222624*m.b214 + 18292*m.b215
                        + 28160*m.b216 + 39356*m.b217 + 51732*m.b218 + 72300*m.b219 + 111312*m.b220 + 68595*m.b221
                        + 105600*m.b222 + 147585*m.b223 + 193995*m.b224 + 271125*m.b225 + 417420*m.b226
                        + 121184.5*m.b227 + 186560*m.b228 + 260733.5*m.b229 + 342724.5*m.b230 + 478987.5*m.b231
                        + 737442*m.b232 + 22865*m.b233 + 35200*m.b234 + 49195*m.b235 + 64665*m.b236 + 90375*m.b237
                        + 139140*m.b238 + 56247.9*m.b239 + 86592*m.b240 + 121019.7*m.b241 + 159075.9*m.b242
                        + 222322.5*m.b243 + 342284.4*m.b244 + 68595*m.b245 + 105600*m.b246 + 147585*m.b247
                        + 193995*m.b248 + 271125*m.b249 + 417420*m.b250 + 59449*m.b251 + 91520*m.b252 + 127907*m.b253
                        + 168129*m.b254 + 234975*m.b255 + 361764*m.b256 + 38870.5*m.b257 + 59840*m.b258 + 83631.5*m.b259
                        + 109930.5*m.b260 + 153637.5*m.b261 + 236538*m.b262 + 13719*m.b263 + 21120*m.b264 + 29517*m.b265
                        + 38799*m.b266 + 54225*m.b267 + 83484*m.b268 + 34297.5*m.b269 + 52800*m.b270 + 73792.5*m.b271
                        + 96997.5*m.b272 + 135562.5*m.b273 + 208710*m.b274 + 91460*m.b275 + 140800*m.b276
                        + 196780*m.b277 + 258660*m.b278 + 361500*m.b279 + 556560*m.b280 + 73168*m.b281 + 112640*m.b282
                        + 157424*m.b283 + 206928*m.b284 + 289200*m.b285 + 445248*m.b286 + 6859.5*m.b287 + 10560*m.b288
                        + 14758.5*m.b289 + 19399.5*m.b290 + 27112.5*m.b291 + 41742*m.b292 + 39327.8*m.b293
                        + 60544*m.b294 + 84615.4*m.b295 + 111223.8*m.b296 + 155445*m.b297 + 239320.8*m.b298
                        + 43443.5*m.b299 + 66880*m.b300 + 93470.5*m.b301 + 122863.5*m.b302 + 171712.5*m.b303
                        + 264366*m.b304, sense=minimize)

m.c2 = Constraint(expr= - m.x33 + m.x34 == -0.24722)

m.c3 = Constraint(expr= - m.x34 + m.x35 + m.x36 - m.x52 == -0.23611)

m.c4 = Constraint(expr= - m.x35 + m.x37 == -0.03611)

m.c5 = Constraint(expr= - m.x37 + m.x38 == -0.20139)

m.c6 = Constraint(expr= - m.x38 + m.x39 == -0.27917)

m.c7 = Constraint(expr= - m.x39 + m.x40 == -0.375)

m.c8 = Constraint(expr= - m.x40 + m.x41 == -0.15278)

m.c9 = Constraint(expr= - m.x41 + m.x42 == -0.14583)

m.c10 = Constraint(expr= - m.x42 + m.x43 + m.x44 == -0.14583)

m.c11 = Constraint(expr= - m.x43 + m.x45 == -0.13889)

m.c12 = Constraint(expr= - m.x45 + m.x46 == -0.15556)

m.c13 = Constraint(expr= - m.x46 == -0.26111)

m.c14 = Constraint(expr= - m.x44 + m.x47 == -0.17083)

m.c15 = Constraint(expr= - m.x47 + m.x48 == -0.07778)

m.c16 = Constraint(expr= - m.x48 + m.x49 - m.x61 == -0.08611)

m.c17 = Constraint(expr= - m.x49 + m.x50 == -0.24028)

m.c18 = Constraint(expr= - m.x50 + m.x51 == -0.37361)

m.c19 = Constraint(expr= - m.x51 + m.x52 == -0.01667)

m.c20 = Constraint(expr= - m.x36 + m.x53 + m.x54 == -0.35417)

m.c21 = Constraint(expr= - m.x53 + m.x55 == -0.25833)

m.c22 = Constraint(expr= - m.x55 == -0.13472)

m.c23 = Constraint(expr= - m.x54 + m.x56 + m.x57 == -0.29028)

m.c24 = Constraint(expr= - m.x56 + m.x58 == -0.22778)

m.c25 = Constraint(expr= - m.x58 + m.x59 - m.x66 == -0.04722)

m.c26 = Constraint(expr= - m.x59 + m.x60 == -0.25)

m.c27 = Constraint(expr= - m.x60 + m.x61 == -0.10278)

m.c28 = Constraint(expr= - m.x57 + m.x62 == -0.08056)

m.c29 = Constraint(expr= - m.x62 + m.x63 == -0.1)

m.c30 = Constraint(expr= - m.x63 + m.x64 == -0.1)

m.c31 = Constraint(expr= - m.x64 + m.x65 == -0.02917)

m.c32 = Constraint(expr= - m.x65 + m.x66 == -0.22361)

m.c33 = Constraint(expr=SignPower(m.x33,1.852) - 7.6849192909955*(1.27323954473516*m.x67)**2.435*(m.x1 - m.x2) == 0)

m.c34 = Constraint(expr=SignPower(m.x34,1.852) - 0.569253280814482*(1.27323954473516*m.x68)**2.435*(m.x2 - m.x3) == 0)

m.c35 = Constraint(expr=SignPower(m.x35,1.852) - 0.853879921221723*(1.27323954473516*m.x69)**2.435*(m.x3 - m.x4) == 0)

m.c36 = Constraint(expr=SignPower(m.x36,1.852) - 0.349314513227068*(1.27323954473516*m.x70)**2.435*(m.x3 - m.x20) == 0)

m.c37 = Constraint(expr=SignPower(m.x37,1.852) - 0.668253851390913*(1.27323954473516*m.x71)**2.435*(m.x4 - m.x5) == 0)

m.c38 = Constraint(expr=SignPower(m.x38,1.852) - 0.529994433861759*(1.27323954473516*m.x72)**2.435*(m.x5 - m.x6) == 0)

m.c39 = Constraint(expr=SignPower(m.x39,1.852) - 1.70775984244345*(1.27323954473516*m.x73)**2.435*(m.x6 - m.x7) == 0)

m.c40 = Constraint(expr=SignPower(m.x40,1.852) - 0.904108151881824*(1.27323954473516*m.x74)**2.435*(m.x7 - m.x8) == 0)

m.c41 = Constraint(expr=SignPower(m.x41,1.852) - 0.904108151881824*(1.27323954473516*m.x75)**2.435*(m.x8 - m.x9) == 0)

m.c42 = Constraint(expr=SignPower(m.x42,1.852) - 0.960614911374438*(1.27323954473516*m.x76)**2.435*(m.x9 - m.x10) == 0)

m.c43 = Constraint(expr=SignPower(m.x43,1.852) - 0.808938872736369*(1.27323954473516*m.x77)**2.435*(m.x10 - m.x11) == 0)

m.c44 = Constraint(expr=SignPower(m.x44,1.852) - 0.960614911374438*(1.27323954473516*m.x78)**2.435*(m.x10 - m.x14) == 0)

m.c45 = Constraint(expr=SignPower(m.x45,1.852) - 0.640409940916292*(1.27323954473516*m.x79)**2.435*(m.x11 - m.x12) == 0)

m.c46 = Constraint(expr=SignPower(m.x46,1.852) - 0.219569122599872*(1.27323954473516*m.x80)**2.435*(m.x12 - m.x13) == 0)

m.c47 = Constraint(expr=SignPower(m.x47,1.852) - 1.5369838581991*(1.27323954473516*m.x81)**2.435*(m.x14 - m.x15) == 0)

m.c48 = Constraint(expr=SignPower(m.x48,1.852) - 1.39725805290827*(1.27323954473516*m.x82)**2.435*(m.x15 - m.x16) == 0)

m.c49 = Constraint(expr=SignPower(m.x49,1.852) - 0.28149887512804*(1.27323954473516*m.x83)**2.435*(m.x16 - m.x17) == 0)

m.c50 = Constraint(expr=SignPower(m.x50,1.852) - 0.439138245199743*(1.27323954473516*m.x84)**2.435*(m.x17 - m.x18) == 0)

m.c51 = Constraint(expr=SignPower(m.x51,1.852) - 0.960614911374438*(1.27323954473516*m.x85)**2.435*(m.x18 - m.x19) == 0)

m.c52 = Constraint(expr=SignPower(m.x52,1.852) - 1.92122982274888*(1.27323954473516*m.x86)**2.435*(m.x19 - m.x3) == 0)

m.c53 = Constraint(expr=SignPower(m.x53,1.852) - 0.512327952733034*(1.27323954473516*m.x87)**2.435*(m.x20 - m.x21) == 0)

m.c54 = Constraint(expr=SignPower(m.x54,1.852) - 0.289996954377189*(1.27323954473516*m.x88)**2.435*(m.x20 - m.x23) == 0)

m.c55 = Constraint(expr=SignPower(m.x55,1.852) - 1.5369838581991*(1.27323954473516*m.x89)**2.435*(m.x21 - m.x22) == 0)

m.c56 = Constraint(expr=SignPower(m.x56,1.852) - 0.624790186259797*(1.27323954473516*m.x90)**2.435*(m.x23 - m.x24) == 0)

m.c57 = Constraint(expr=SignPower(m.x57,1.852) - 0.512327952733034*(1.27323954473516*m.x91)**2.435*(m.x23 - m.x28) == 0)

m.c58 = Constraint(expr=SignPower(m.x58,1.852) - 0.591147637768885*(1.27323954473516*m.x92)**2.435*(m.x24 - m.x25) == 0)

m.c59 = Constraint(expr=SignPower(m.x59,1.852) - 0.904108151881824*(1.27323954473516*m.x93)**2.435*(m.x25 - m.x26) == 0)

m.c60 = Constraint(expr=SignPower(m.x60,1.852) - 2.56163976366517*(1.27323954473516*m.x94)**2.435*(m.x26 - m.x27) == 0)

m.c61 = Constraint(expr=SignPower(m.x61,1.852) - 1.02465590546607*(1.27323954473516*m.x95)**2.435*(m.x27 - m.x16) == 0)

m.c62 = Constraint(expr=SignPower(m.x62,1.852) - 0.384245964549775*(1.27323954473516*m.x96)**2.435*(m.x28 - m.x29) == 0)

m.c63 = Constraint(expr=SignPower(m.x63,1.852) - 0.480307455687219*(1.27323954473516*m.x97)**2.435*(m.x29 - m.x30) == 0)

m.c64 = Constraint(expr=SignPower(m.x64,1.852) - 5.12327952733034*(1.27323954473516*m.x98)**2.435*(m.x30 - m.x31) == 0)

m.c65 = Constraint(expr=SignPower(m.x65,1.852) - 0.893595266394826*(1.27323954473516*m.x99)**2.435*(m.x31 - m.x32) == 0)

m.c66 = Constraint(expr=SignPower(m.x66,1.852) - 0.808938872736369*(1.27323954473516*m.x100)**2.435*(m.x32 - m.x25)
                         == 0)

m.c67 = Constraint(expr=   m.x33 - 7*m.x67 <= 0)

m.c68 = Constraint(expr=   m.x34 - 7*m.x68 <= 0)

m.c69 = Constraint(expr=   m.x35 - 3*m.x69 <= 0)

m.c70 = Constraint(expr=   m.x36 - 3*m.x70 <= 0)

m.c71 = Constraint(expr=   m.x37 - 3*m.x71 <= 0)

m.c72 = Constraint(expr=   m.x38 - 2.5*m.x72 <= 0)

m.c73 = Constraint(expr=   m.x39 - 2.5*m.x73 <= 0)

m.c74 = Constraint(expr=   m.x40 - 2*m.x74 <= 0)

m.c75 = Constraint(expr=   m.x41 - 2*m.x75 <= 0)

m.c76 = Constraint(expr=   m.x42 - 2*m.x76 <= 0)

m.c77 = Constraint(expr=   m.x43 - 2*m.x77 <= 0)

m.c78 = Constraint(expr=   m.x44 - 2*m.x78 <= 0)

m.c79 = Constraint(expr=   m.x45 - 2*m.x79 <= 0)

m.c80 = Constraint(expr=   m.x46 - 2*m.x80 <= 0)

m.c81 = Constraint(expr=   m.x47 - 2*m.x81 <= 0)

m.c82 = Constraint(expr=   m.x48 - 2*m.x82 <= 0)

m.c83 = Constraint(expr=   m.x49 - 2*m.x83 <= 0)

m.c84 = Constraint(expr=   m.x50 - 2*m.x84 <= 0)

m.c85 = Constraint(expr=   m.x51 - 3.5*m.x85 <= 0)

m.c86 = Constraint(expr=   m.x52 - 3.5*m.x86 <= 0)

m.c87 = Constraint(expr=   m.x53 - 2*m.x87 <= 0)

m.c88 = Constraint(expr=   m.x54 - 2*m.x88 <= 0)

m.c89 = Constraint(expr=   m.x55 - 2*m.x89 <= 0)

m.c90 = Constraint(expr=   m.x56 - 3*m.x90 <= 0)

m.c91 = Constraint(expr=   m.x57 - 2*m.x91 <= 0)

m.c92 = Constraint(expr=   m.x58 - 2*m.x92 <= 0)

m.c93 = Constraint(expr=   m.x59 - 2*m.x93 <= 0)

m.c94 = Constraint(expr=   m.x60 - 2*m.x94 <= 0)

m.c95 = Constraint(expr=   m.x61 - 2*m.x95 <= 0)

m.c96 = Constraint(expr=   m.x62 - 2*m.x96 <= 0)

m.c97 = Constraint(expr=   m.x63 - 2*m.x97 <= 0)

m.c98 = Constraint(expr=   m.x64 - 2*m.x98 <= 0)

m.c99 = Constraint(expr=   m.x65 - 2*m.x99 <= 0)

m.c100 = Constraint(expr=   m.x66 - 2*m.x100 <= 0)

m.c101 = Constraint(expr=   m.x33 + 7*m.x67 >= 0)

m.c102 = Constraint(expr=   m.x34 + 7*m.x68 >= 0)

m.c103 = Constraint(expr=   m.x35 + 3*m.x69 >= 0)

m.c104 = Constraint(expr=   m.x36 + 3*m.x70 >= 0)

m.c105 = Constraint(expr=   m.x37 + 3*m.x71 >= 0)

m.c106 = Constraint(expr=   m.x38 + 2.5*m.x72 >= 0)

m.c107 = Constraint(expr=   m.x39 + 2.5*m.x73 >= 0)

m.c108 = Constraint(expr=   m.x40 + 2*m.x74 >= 0)

m.c109 = Constraint(expr=   m.x41 + 2*m.x75 >= 0)

m.c110 = Constraint(expr=   m.x42 + 2*m.x76 >= 0)

m.c111 = Constraint(expr=   m.x43 + 2*m.x77 >= 0)

m.c112 = Constraint(expr=   m.x44 + 2*m.x78 >= 0)

m.c113 = Constraint(expr=   m.x45 + 2*m.x79 >= 0)

m.c114 = Constraint(expr=   m.x46 + 2*m.x80 >= 0)

m.c115 = Constraint(expr=   m.x47 + 2*m.x81 >= 0)

m.c116 = Constraint(expr=   m.x48 + 2*m.x82 >= 0)

m.c117 = Constraint(expr=   m.x49 + 2*m.x83 >= 0)

m.c118 = Constraint(expr=   m.x50 + 2*m.x84 >= 0)

m.c119 = Constraint(expr=   m.x51 + 3.5*m.x85 >= 0)

m.c120 = Constraint(expr=   m.x52 + 3.5*m.x86 >= 0)

m.c121 = Constraint(expr=   m.x53 + 2*m.x87 >= 0)

m.c122 = Constraint(expr=   m.x54 + 2*m.x88 >= 0)

m.c123 = Constraint(expr=   m.x55 + 2*m.x89 >= 0)

m.c124 = Constraint(expr=   m.x56 + 3*m.x90 >= 0)

m.c125 = Constraint(expr=   m.x57 + 2*m.x91 >= 0)

m.c126 = Constraint(expr=   m.x58 + 2*m.x92 >= 0)

m.c127 = Constraint(expr=   m.x59 + 2*m.x93 >= 0)

m.c128 = Constraint(expr=   m.x60 + 2*m.x94 >= 0)

m.c129 = Constraint(expr=   m.x61 + 2*m.x95 >= 0)

m.c130 = Constraint(expr=   m.x62 + 2*m.x96 >= 0)

m.c131 = Constraint(expr=   m.x63 + 2*m.x97 >= 0)

m.c132 = Constraint(expr=   m.x64 + 2*m.x98 >= 0)

m.c133 = Constraint(expr=   m.x65 + 2*m.x99 >= 0)

m.c134 = Constraint(expr=   m.x66 + 2*m.x100 >= 0)

m.c135 = Constraint(expr=   m.x67 - 0.0729658769900397*m.b101 - 0.129717114648959*m.b102 - 0.202682991638999*m.b103
                          - 0.291863507960159*m.b104 - 0.456036731187748*m.b105 - 0.810731966555996*m.b106 == 0)

m.c136 = Constraint(expr=   m.x68 - 0.0729658769900397*m.b107 - 0.129717114648959*m.b108 - 0.202682991638999*m.b109
                          - 0.291863507960159*m.b110 - 0.456036731187748*m.b111 - 0.810731966555996*m.b112 == 0)

m.c137 = Constraint(expr=   m.x69 - 0.0729658769900397*m.b113 - 0.129717114648959*m.b114 - 0.202682991638999*m.b115
                          - 0.291863507960159*m.b116 - 0.456036731187748*m.b117 - 0.810731966555996*m.b118 == 0)

m.c138 = Constraint(expr=   m.x70 - 0.0729658769900397*m.b119 - 0.129717114648959*m.b120 - 0.202682991638999*m.b121
                          - 0.291863507960159*m.b122 - 0.456036731187748*m.b123 - 0.810731966555996*m.b124 == 0)

m.c139 = Constraint(expr=   m.x71 - 0.0729658769900397*m.b125 - 0.129717114648959*m.b126 - 0.202682991638999*m.b127
                          - 0.291863507960159*m.b128 - 0.456036731187748*m.b129 - 0.810731966555996*m.b130 == 0)

m.c140 = Constraint(expr=   m.x72 - 0.0729658769900397*m.b131 - 0.129717114648959*m.b132 - 0.202682991638999*m.b133
                          - 0.291863507960159*m.b134 - 0.456036731187748*m.b135 - 0.810731966555996*m.b136 == 0)

m.c141 = Constraint(expr=   m.x73 - 0.0729658769900397*m.b137 - 0.129717114648959*m.b138 - 0.202682991638999*m.b139
                          - 0.291863507960159*m.b140 - 0.456036731187748*m.b141 - 0.810731966555996*m.b142 == 0)

m.c142 = Constraint(expr=   m.x74 - 0.0729658769900397*m.b143 - 0.129717114648959*m.b144 - 0.202682991638999*m.b145
                          - 0.291863507960159*m.b146 - 0.456036731187748*m.b147 - 0.810731966555996*m.b148 == 0)

m.c143 = Constraint(expr=   m.x75 - 0.0729658769900397*m.b149 - 0.129717114648959*m.b150 - 0.202682991638999*m.b151
                          - 0.291863507960159*m.b152 - 0.456036731187748*m.b153 - 0.810731966555996*m.b154 == 0)

m.c144 = Constraint(expr=   m.x76 - 0.0729658769900397*m.b155 - 0.129717114648959*m.b156 - 0.202682991638999*m.b157
                          - 0.291863507960159*m.b158 - 0.456036731187748*m.b159 - 0.810731966555996*m.b160 == 0)

m.c145 = Constraint(expr=   m.x77 - 0.0729658769900397*m.b161 - 0.129717114648959*m.b162 - 0.202682991638999*m.b163
                          - 0.291863507960159*m.b164 - 0.456036731187748*m.b165 - 0.810731966555996*m.b166 == 0)

m.c146 = Constraint(expr=   m.x78 - 0.0729658769900397*m.b167 - 0.129717114648959*m.b168 - 0.202682991638999*m.b169
                          - 0.291863507960159*m.b170 - 0.456036731187748*m.b171 - 0.810731966555996*m.b172 == 0)

m.c147 = Constraint(expr=   m.x79 - 0.0729658769900397*m.b173 - 0.129717114648959*m.b174 - 0.202682991638999*m.b175
                          - 0.291863507960159*m.b176 - 0.456036731187748*m.b177 - 0.810731966555996*m.b178 == 0)

m.c148 = Constraint(expr=   m.x80 - 0.0729658769900397*m.b179 - 0.129717114648959*m.b180 - 0.202682991638999*m.b181
                          - 0.291863507960159*m.b182 - 0.456036731187748*m.b183 - 0.810731966555996*m.b184 == 0)

m.c149 = Constraint(expr=   m.x81 - 0.0729658769900397*m.b185 - 0.129717114648959*m.b186 - 0.202682991638999*m.b187
                          - 0.291863507960159*m.b188 - 0.456036731187748*m.b189 - 0.810731966555996*m.b190 == 0)

m.c150 = Constraint(expr=   m.x82 - 0.0729658769900397*m.b191 - 0.129717114648959*m.b192 - 0.202682991638999*m.b193
                          - 0.291863507960159*m.b194 - 0.456036731187748*m.b195 - 0.810731966555996*m.b196 == 0)

m.c151 = Constraint(expr=   m.x83 - 0.0729658769900397*m.b197 - 0.129717114648959*m.b198 - 0.202682991638999*m.b199
                          - 0.291863507960159*m.b200 - 0.456036731187748*m.b201 - 0.810731966555996*m.b202 == 0)

m.c152 = Constraint(expr=   m.x84 - 0.0729658769900397*m.b203 - 0.129717114648959*m.b204 - 0.202682991638999*m.b205
                          - 0.291863507960159*m.b206 - 0.456036731187748*m.b207 - 0.810731966555996*m.b208 == 0)

m.c153 = Constraint(expr=   m.x85 - 0.0729658769900397*m.b209 - 0.129717114648959*m.b210 - 0.202682991638999*m.b211
                          - 0.291863507960159*m.b212 - 0.456036731187748*m.b213 - 0.810731966555996*m.b214 == 0)

m.c154 = Constraint(expr=   m.x86 - 0.0729658769900397*m.b215 - 0.129717114648959*m.b216 - 0.202682991638999*m.b217
                          - 0.291863507960159*m.b218 - 0.456036731187748*m.b219 - 0.810731966555996*m.b220 == 0)

m.c155 = Constraint(expr=   m.x87 - 0.0729658769900397*m.b221 - 0.129717114648959*m.b222 - 0.202682991638999*m.b223
                          - 0.291863507960159*m.b224 - 0.456036731187748*m.b225 - 0.810731966555996*m.b226 == 0)

m.c156 = Constraint(expr=   m.x88 - 0.0729658769900397*m.b227 - 0.129717114648959*m.b228 - 0.202682991638999*m.b229
                          - 0.291863507960159*m.b230 - 0.456036731187748*m.b231 - 0.810731966555996*m.b232 == 0)

m.c157 = Constraint(expr=   m.x89 - 0.0729658769900397*m.b233 - 0.129717114648959*m.b234 - 0.202682991638999*m.b235
                          - 0.291863507960159*m.b236 - 0.456036731187748*m.b237 - 0.810731966555996*m.b238 == 0)

m.c158 = Constraint(expr=   m.x90 - 0.0729658769900397*m.b239 - 0.129717114648959*m.b240 - 0.202682991638999*m.b241
                          - 0.291863507960159*m.b242 - 0.456036731187748*m.b243 - 0.810731966555996*m.b244 == 0)

m.c159 = Constraint(expr=   m.x91 - 0.0729658769900397*m.b245 - 0.129717114648959*m.b246 - 0.202682991638999*m.b247
                          - 0.291863507960159*m.b248 - 0.456036731187748*m.b249 - 0.810731966555996*m.b250 == 0)

m.c160 = Constraint(expr=   m.x92 - 0.0729658769900397*m.b251 - 0.129717114648959*m.b252 - 0.202682991638999*m.b253
                          - 0.291863507960159*m.b254 - 0.456036731187748*m.b255 - 0.810731966555996*m.b256 == 0)

m.c161 = Constraint(expr=   m.x93 - 0.0729658769900397*m.b257 - 0.129717114648959*m.b258 - 0.202682991638999*m.b259
                          - 0.291863507960159*m.b260 - 0.456036731187748*m.b261 - 0.810731966555996*m.b262 == 0)

m.c162 = Constraint(expr=   m.x94 - 0.0729658769900397*m.b263 - 0.129717114648959*m.b264 - 0.202682991638999*m.b265
                          - 0.291863507960159*m.b266 - 0.456036731187748*m.b267 - 0.810731966555996*m.b268 == 0)

m.c163 = Constraint(expr=   m.x95 - 0.0729658769900397*m.b269 - 0.129717114648959*m.b270 - 0.202682991638999*m.b271
                          - 0.291863507960159*m.b272 - 0.456036731187748*m.b273 - 0.810731966555996*m.b274 == 0)

m.c164 = Constraint(expr=   m.x96 - 0.0729658769900397*m.b275 - 0.129717114648959*m.b276 - 0.202682991638999*m.b277
                          - 0.291863507960159*m.b278 - 0.456036731187748*m.b279 - 0.810731966555996*m.b280 == 0)

m.c165 = Constraint(expr=   m.x97 - 0.0729658769900397*m.b281 - 0.129717114648959*m.b282 - 0.202682991638999*m.b283
                          - 0.291863507960159*m.b284 - 0.456036731187748*m.b285 - 0.810731966555996*m.b286 == 0)

m.c166 = Constraint(expr=   m.x98 - 0.0729658769900397*m.b287 - 0.129717114648959*m.b288 - 0.202682991638999*m.b289
                          - 0.291863507960159*m.b290 - 0.456036731187748*m.b291 - 0.810731966555996*m.b292 == 0)

m.c167 = Constraint(expr=   m.x99 - 0.0729658769900397*m.b293 - 0.129717114648959*m.b294 - 0.202682991638999*m.b295
                          - 0.291863507960159*m.b296 - 0.456036731187748*m.b297 - 0.810731966555996*m.b298 == 0)

m.c168 = Constraint(expr=   m.x100 - 0.0729658769900397*m.b299 - 0.129717114648959*m.b300 - 0.202682991638999*m.b301
                          - 0.291863507960159*m.b302 - 0.456036731187748*m.b303 - 0.810731966555996*m.b304 == 0)

m.c169 = Constraint(expr=   m.b101 + m.b102 + m.b103 + m.b104 + m.b105 + m.b106 == 1)

m.c170 = Constraint(expr=   m.b107 + m.b108 + m.b109 + m.b110 + m.b111 + m.b112 == 1)

m.c171 = Constraint(expr=   m.b113 + m.b114 + m.b115 + m.b116 + m.b117 + m.b118 == 1)

m.c172 = Constraint(expr=   m.b119 + m.b120 + m.b121 + m.b122 + m.b123 + m.b124 == 1)

m.c173 = Constraint(expr=   m.b125 + m.b126 + m.b127 + m.b128 + m.b129 + m.b130 == 1)

m.c174 = Constraint(expr=   m.b131 + m.b132 + m.b133 + m.b134 + m.b135 + m.b136 == 1)

m.c175 = Constraint(expr=   m.b137 + m.b138 + m.b139 + m.b140 + m.b141 + m.b142 == 1)

m.c176 = Constraint(expr=   m.b143 + m.b144 + m.b145 + m.b146 + m.b147 + m.b148 == 1)

m.c177 = Constraint(expr=   m.b149 + m.b150 + m.b151 + m.b152 + m.b153 + m.b154 == 1)

m.c178 = Constraint(expr=   m.b155 + m.b156 + m.b157 + m.b158 + m.b159 + m.b160 == 1)

m.c179 = Constraint(expr=   m.b161 + m.b162 + m.b163 + m.b164 + m.b165 + m.b166 == 1)

m.c180 = Constraint(expr=   m.b167 + m.b168 + m.b169 + m.b170 + m.b171 + m.b172 == 1)

m.c181 = Constraint(expr=   m.b173 + m.b174 + m.b175 + m.b176 + m.b177 + m.b178 == 1)

m.c182 = Constraint(expr=   m.b179 + m.b180 + m.b181 + m.b182 + m.b183 + m.b184 == 1)

m.c183 = Constraint(expr=   m.b185 + m.b186 + m.b187 + m.b188 + m.b189 + m.b190 == 1)

m.c184 = Constraint(expr=   m.b191 + m.b192 + m.b193 + m.b194 + m.b195 + m.b196 == 1)

m.c185 = Constraint(expr=   m.b197 + m.b198 + m.b199 + m.b200 + m.b201 + m.b202 == 1)

m.c186 = Constraint(expr=   m.b203 + m.b204 + m.b205 + m.b206 + m.b207 + m.b208 == 1)

m.c187 = Constraint(expr=   m.b209 + m.b210 + m.b211 + m.b212 + m.b213 + m.b214 == 1)

m.c188 = Constraint(expr=   m.b215 + m.b216 + m.b217 + m.b218 + m.b219 + m.b220 == 1)

m.c189 = Constraint(expr=   m.b221 + m.b222 + m.b223 + m.b224 + m.b225 + m.b226 == 1)

m.c190 = Constraint(expr=   m.b227 + m.b228 + m.b229 + m.b230 + m.b231 + m.b232 == 1)

m.c191 = Constraint(expr=   m.b233 + m.b234 + m.b235 + m.b236 + m.b237 + m.b238 == 1)

m.c192 = Constraint(expr=   m.b239 + m.b240 + m.b241 + m.b242 + m.b243 + m.b244 == 1)

m.c193 = Constraint(expr=   m.b245 + m.b246 + m.b247 + m.b248 + m.b249 + m.b250 == 1)

m.c194 = Constraint(expr=   m.b251 + m.b252 + m.b253 + m.b254 + m.b255 + m.b256 == 1)

m.c195 = Constraint(expr=   m.b257 + m.b258 + m.b259 + m.b260 + m.b261 + m.b262 == 1)

m.c196 = Constraint(expr=   m.b263 + m.b264 + m.b265 + m.b266 + m.b267 + m.b268 == 1)

m.c197 = Constraint(expr=   m.b269 + m.b270 + m.b271 + m.b272 + m.b273 + m.b274 == 1)

m.c198 = Constraint(expr=   m.b275 + m.b276 + m.b277 + m.b278 + m.b279 + m.b280 == 1)

m.c199 = Constraint(expr=   m.b281 + m.b282 + m.b283 + m.b284 + m.b285 + m.b286 == 1)

m.c200 = Constraint(expr=   m.b287 + m.b288 + m.b289 + m.b290 + m.b291 + m.b292 == 1)

m.c201 = Constraint(expr=   m.b293 + m.b294 + m.b295 + m.b296 + m.b297 + m.b298 == 1)

m.c202 = Constraint(expr=   m.b299 + m.b300 + m.b301 + m.b302 + m.b303 + m.b304 == 1)
