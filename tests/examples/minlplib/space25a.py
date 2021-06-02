#  MINLP written by GAMS Convert at 04/21/18 13:54:16
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        202      152        0       50        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        384      144      240        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1513     1402      111        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x3 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x4 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x5 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x6 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x7 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x8 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x9 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x10 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x11 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x12 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x13 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x14 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x15 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x16 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x17 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x18 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x19 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x20 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x21 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x22 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x23 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x24 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x25 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x26 = Var(within=Reals,bounds=(0.1,3.4),initialize=0.1)
m.x27 = Var(within=Reals,bounds=(None,None),initialize=13.3333333333333)
m.x28 = Var(within=Reals,bounds=(None,None),initialize=7.66261028176921)
m.x29 = Var(within=Reals,bounds=(None,None),initialize=7.66261028176921)
m.x30 = Var(within=Reals,bounds=(None,None),initialize=7.66261028176921)
m.x31 = Var(within=Reals,bounds=(None,None),initialize=7.66261028176921)
m.x32 = Var(within=Reals,bounds=(None,None),initialize=9.36329177569045)
m.x33 = Var(within=Reals,bounds=(None,None),initialize=9.36329177569045)
m.x34 = Var(within=Reals,bounds=(None,None),initialize=9.36329177569045)
m.x35 = Var(within=Reals,bounds=(None,None),initialize=9.36329177569045)
m.x36 = Var(within=Reals,bounds=(None,None),initialize=13.3333333333333)
m.x37 = Var(within=Reals,bounds=(None,None),initialize=13.3333333333333)
m.x38 = Var(within=Reals,bounds=(None,None),initialize=13.3333333333333)
m.x39 = Var(within=Reals,bounds=(None,None),initialize=13.3333333333333)
m.x40 = Var(within=Reals,bounds=(None,None),initialize=5.52052447473883)
m.x41 = Var(within=Reals,bounds=(None,None),initialize=5.52052447473883)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=5.52052447473883)
m.x43 = Var(within=Reals,bounds=(None,None),initialize=5.52052447473883)
m.x44 = Var(within=Reals,bounds=(None,None),initialize=5.52052447473883)
m.x45 = Var(within=Reals,bounds=(None,None),initialize=5.52052447473883)
m.x46 = Var(within=Reals,bounds=(None,None),initialize=5.52052447473883)
m.x47 = Var(within=Reals,bounds=(None,None),initialize=5.52052447473883)
m.x48 = Var(within=Reals,bounds=(None,None),initialize=7.49268649265355)
m.x49 = Var(within=Reals,bounds=(None,None),initialize=7.49268649265355)
m.x50 = Var(within=Reals,bounds=(None,None),initialize=7.49268649265355)
m.x51 = Var(within=Reals,bounds=(None,None),initialize=7.49268649265355)
m.x52 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x53 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x54 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x55 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x56 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x57 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x58 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x59 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x60 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x61 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x62 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x66 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x70 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x72 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x76 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x78 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x80 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x81 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x82 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x83 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x84 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x85 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x86 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x87 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x88 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x89 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x90 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x91 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x92 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x93 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x94 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x95 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x96 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x97 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x98 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x99 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x100 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x101 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x102 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x105 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x111 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x117 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x119 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x121 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x123 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x124 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x125 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x126 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x127 = Var(within=Reals,bounds=(-0.35,0.35),initialize=0)
m.x128 = Var(within=Reals,bounds=(-0.35,0.35),initialize=0)
m.x129 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x130 = Var(within=Reals,bounds=(-0.35,0.35),initialize=0)
m.x131 = Var(within=Reals,bounds=(-0.35,0.35),initialize=0)
m.x132 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x133 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x134 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x135 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x136 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x137 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x138 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x139 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x140 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x141 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x142 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x143 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x144 = Var(within=Reals,bounds=(None,None),initialize=0)
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

m.obj = Objective(expr=   7.5*m.x2 + 13.0503831361382*m.x3 + 13.0503831361382*m.x4 + 13.0503831361382*m.x5
                        + 13.0503831361382*m.x6 + 10.6800046816469*m.x7 + 10.6800046816469*m.x8 + 10.6800046816469*m.x9
                        + 10.6800046816469*m.x10 + 7.5*m.x11 + 7.5*m.x12 + 7.5*m.x13 + 7.5*m.x14
                        + 18.1142209327368*m.x15 + 18.1142209327368*m.x16 + 18.1142209327368*m.x17
                        + 18.1142209327368*m.x18 + 18.1142209327368*m.x19 + 18.1142209327368*m.x20
                        + 18.1142209327368*m.x21 + 18.1142209327368*m.x22 + 13.3463478150391*m.x23
                        + 13.3463478150391*m.x24 + 13.3463478150391*m.x25 + 13.3463478150391*m.x26, sense=minimize)

m.c2 = Constraint(expr= - 133.333333333333*m.x2 + m.x27 == 0)

m.c3 = Constraint(expr= - 76.6261028176921*m.x3 + m.x28 == 0)

m.c4 = Constraint(expr= - 76.6261028176921*m.x4 + m.x29 == 0)

m.c5 = Constraint(expr= - 76.6261028176921*m.x5 + m.x30 == 0)

m.c6 = Constraint(expr= - 76.6261028176921*m.x6 + m.x31 == 0)

m.c7 = Constraint(expr= - 93.6329177569045*m.x7 + m.x32 == 0)

m.c8 = Constraint(expr= - 93.6329177569045*m.x8 + m.x33 == 0)

m.c9 = Constraint(expr= - 93.6329177569045*m.x9 + m.x34 == 0)

m.c10 = Constraint(expr= - 93.6329177569045*m.x10 + m.x35 == 0)

m.c11 = Constraint(expr= - 133.333333333333*m.x11 + m.x36 == 0)

m.c12 = Constraint(expr= - 133.333333333333*m.x12 + m.x37 == 0)

m.c13 = Constraint(expr= - 133.333333333333*m.x13 + m.x38 == 0)

m.c14 = Constraint(expr= - 133.333333333333*m.x14 + m.x39 == 0)

m.c15 = Constraint(expr= - 55.2052447473883*m.x15 + m.x40 == 0)

m.c16 = Constraint(expr= - 55.2052447473883*m.x16 + m.x41 == 0)

m.c17 = Constraint(expr= - 55.2052447473883*m.x17 + m.x42 == 0)

m.c18 = Constraint(expr= - 55.2052447473883*m.x18 + m.x43 == 0)

m.c19 = Constraint(expr= - 55.2052447473883*m.x19 + m.x44 == 0)

m.c20 = Constraint(expr= - 55.2052447473883*m.x20 + m.x45 == 0)

m.c21 = Constraint(expr= - 55.2052447473883*m.x21 + m.x46 == 0)

m.c22 = Constraint(expr= - 55.2052447473883*m.x22 + m.x47 == 0)

m.c23 = Constraint(expr= - 74.9268649265355*m.x23 + m.x48 == 0)

m.c24 = Constraint(expr= - 74.9268649265355*m.x24 + m.x49 == 0)

m.c25 = Constraint(expr= - 74.9268649265355*m.x25 + m.x50 == 0)

m.c26 = Constraint(expr= - 74.9268649265355*m.x26 + m.x51 == 0)

m.c27 = Constraint(expr= - 40*m.x2 + m.x52 == 0)

m.c28 = Constraint(expr= - 40*m.x3 + m.x54 == 0)

m.c29 = Constraint(expr= - 40*m.x4 + m.x56 == 0)

m.c30 = Constraint(expr= - 40*m.x5 + m.x58 == 0)

m.c31 = Constraint(expr= - 40*m.x6 + m.x60 == 0)

m.c32 = Constraint(expr= - 40*m.x7 + m.x62 == 0)

m.c33 = Constraint(expr= - 40*m.x8 + m.x64 == 0)

m.c34 = Constraint(expr= - 40*m.x9 + m.x66 == 0)

m.c35 = Constraint(expr= - 40*m.x10 + m.x68 == 0)

m.c36 = Constraint(expr= - 40*m.x11 + m.x70 == 0)

m.c37 = Constraint(expr= - 40*m.x12 + m.x72 == 0)

m.c38 = Constraint(expr= - 40*m.x13 + m.x74 == 0)

m.c39 = Constraint(expr= - 40*m.x14 + m.x76 == 0)

m.c40 = Constraint(expr= - 40*m.x15 + m.x78 == 0)

m.c41 = Constraint(expr= - 40*m.x16 + m.x80 == 0)

m.c42 = Constraint(expr= - 40*m.x17 + m.x82 == 0)

m.c43 = Constraint(expr= - 40*m.x18 + m.x84 == 0)

m.c44 = Constraint(expr= - 40*m.x19 + m.x86 == 0)

m.c45 = Constraint(expr= - 40*m.x20 + m.x88 == 0)

m.c46 = Constraint(expr= - 40*m.x21 + m.x90 == 0)

m.c47 = Constraint(expr= - 40*m.x22 + m.x92 == 0)

m.c48 = Constraint(expr= - 40*m.x23 + m.x94 == 0)

m.c49 = Constraint(expr= - 40*m.x24 + m.x96 == 0)

m.c50 = Constraint(expr= - 40*m.x25 + m.x98 == 0)

m.c51 = Constraint(expr= - 40*m.x26 + m.x100 == 0)

m.c52 = Constraint(expr= - 40*m.x2 + m.x53 == 0)

m.c53 = Constraint(expr= - 40*m.x3 + m.x55 == 0)

m.c54 = Constraint(expr= - 40*m.x4 + m.x57 == 0)

m.c55 = Constraint(expr= - 40*m.x5 + m.x59 == 0)

m.c56 = Constraint(expr= - 40*m.x6 + m.x61 == 0)

m.c57 = Constraint(expr= - 40*m.x7 + m.x63 == 0)

m.c58 = Constraint(expr= - 40*m.x8 + m.x65 == 0)

m.c59 = Constraint(expr= - 40*m.x9 + m.x67 == 0)

m.c60 = Constraint(expr= - 40*m.x10 + m.x69 == 0)

m.c61 = Constraint(expr= - 40*m.x11 + m.x71 == 0)

m.c62 = Constraint(expr= - 40*m.x12 + m.x73 == 0)

m.c63 = Constraint(expr= - 40*m.x13 + m.x75 == 0)

m.c64 = Constraint(expr= - 40*m.x14 + m.x77 == 0)

m.c65 = Constraint(expr= - 40*m.x15 + m.x79 == 0)

m.c66 = Constraint(expr= - 40*m.x16 + m.x81 == 0)

m.c67 = Constraint(expr= - 40*m.x17 + m.x83 == 0)

m.c68 = Constraint(expr= - 40*m.x18 + m.x85 == 0)

m.c69 = Constraint(expr= - 40*m.x19 + m.x87 == 0)

m.c70 = Constraint(expr= - 40*m.x20 + m.x89 == 0)

m.c71 = Constraint(expr= - 40*m.x21 + m.x91 == 0)

m.c72 = Constraint(expr= - 40*m.x22 + m.x93 == 0)

m.c73 = Constraint(expr= - 40*m.x23 + m.x95 == 0)

m.c74 = Constraint(expr= - 40*m.x24 + m.x97 == 0)

m.c75 = Constraint(expr= - 40*m.x25 + m.x99 == 0)

m.c76 = Constraint(expr= - 40*m.x26 + m.x101 == 0)

m.c77 = Constraint(expr=m.x27*(m.x130 - m.x127) - m.x102 == 0)

m.c78 = Constraint(expr=m.x28*(-0.574695771132691*m.x127 - 0.287347885566345*m.x128 + 0.766261028176921*m.x129 + 
                        0.574695771132691*m.x136 + 0.287347885566345*m.x137 - 0.766261028176921*m.x138) - m.x103 == 0)

m.c79 = Constraint(expr=m.x29*(0.574695771132691*m.x130 - 0.287347885566345*m.x131 + 0.766261028176921*m.x132 - 
                        0.574695771132691*m.x133 + 0.287347885566345*m.x134 - 0.766261028176921*m.x135) - m.x104 == 0)

m.c80 = Constraint(expr=m.x30*(0.287347885566345*m.x128 - 0.574695771132691*m.x127 + 0.766261028176921*m.x129 + 
                        0.574695771132691*m.x139 - 0.287347885566345*m.x140 - 0.766261028176921*m.x141) - m.x105 == 0)

m.c81 = Constraint(expr=m.x31*(0.574695771132691*m.x130 + 0.287347885566345*m.x131 + 0.766261028176921*m.x132 - 
                        0.574695771132691*m.x142 - 0.287347885566345*m.x143 - 0.766261028176921*m.x144) - m.x106 == 0)

m.c82 = Constraint(expr=m.x32*(0.936329177569045*m.x132 - 0.351123441588392*m.x131 + 0.351123441588392*m.x137 - 
                        0.936329177569045*m.x138) - m.x107 == 0)

m.c83 = Constraint(expr=m.x33*(0.351123441588392*m.x131 + 0.936329177569045*m.x132 - 0.351123441588392*m.x140 - 
                        0.936329177569045*m.x141) - m.x108 == 0)

m.c84 = Constraint(expr=m.x34*(0.936329177569045*m.x129 - 0.351123441588392*m.x128 + 0.351123441588392*m.x134 - 
                        0.936329177569045*m.x135) - m.x109 == 0)

m.c85 = Constraint(expr=m.x35*(0.351123441588392*m.x128 + 0.936329177569045*m.x129 - 0.351123441588392*m.x143 - 
                        0.936329177569045*m.x144) - m.x110 == 0)

m.c86 = Constraint(expr=m.x36*(m.x134 - m.x143) - m.x111 == 0)

m.c87 = Constraint(expr=m.x37*(m.x137 - m.x140) - m.x112 == 0)

m.c88 = Constraint(expr=m.x38*(m.x136 - m.x133) - m.x113 == 0)

m.c89 = Constraint(expr=m.x39*(m.x139 - m.x142) - m.x114 == 0)

m.c90 = Constraint(expr=m.x40*(0.345032779671177*m.x133 + 0.75907211527659*m.x134 + 0.552052447473883*m.x135) - m.x115
                         == 0)

m.c91 = Constraint(expr=m.x41*(0.345032779671177*m.x142 - 0.75907211527659*m.x143 + 0.552052447473883*m.x144) - m.x116
                         == 0)

m.c92 = Constraint(expr=m.x42*(0.75907211527659*m.x137 - 0.345032779671177*m.x136 + 0.552052447473883*m.x138) - m.x117
                         == 0)

m.c93 = Constraint(expr=m.x43*(-0.345032779671177*m.x139 - 0.75907211527659*m.x140 + 0.552052447473883*m.x141) - m.x118
                         == 0)

m.c94 = Constraint(expr=m.x44*(0.75907211527659*m.x136 - 0.345032779671177*m.x137 + 0.552052447473883*m.x138) - m.x119
                         == 0)

m.c95 = Constraint(expr=m.x45*(-0.75907211527659*m.x133 - 0.345032779671177*m.x134 + 0.552052447473883*m.x135) - m.x120
                         == 0)

m.c96 = Constraint(expr=m.x46*(0.75907211527659*m.x139 + 0.345032779671177*m.x140 + 0.552052447473883*m.x141) - m.x121
                         == 0)

m.c97 = Constraint(expr=m.x47*(0.345032779671177*m.x143 - 0.75907211527659*m.x142 + 0.552052447473883*m.x144) - m.x122
                         == 0)

m.c98 = Constraint(expr=m.x48*(0.468292905790847*m.x142 + 0.468292905790847*m.x143 + 0.749268649265355*m.x144) - m.x123
                         == 0)

m.c99 = Constraint(expr=m.x49*(0.468292905790847*m.x133 - 0.468292905790847*m.x134 + 0.749268649265355*m.x135) - m.x124
                         == 0)

m.c100 = Constraint(expr=m.x50*(-0.468292905790847*m.x136 - 0.468292905790847*m.x137 + 0.749268649265355*m.x138)
                          - m.x125 == 0)

m.c101 = Constraint(expr=m.x51*(0.468292905790847*m.x140 - 0.468292905790847*m.x139 + 0.749268649265355*m.x141) - m.x126
                          == 0)

m.c102 = Constraint(expr= - m.x102 - 0.574695771132691*m.x103 - 0.574695771132691*m.x105 == 1)

m.c103 = Constraint(expr= - 0.287347885566345*m.x103 + 0.287347885566345*m.x105 - 0.351123441588392*m.x109
                          + 0.351123441588392*m.x110 == 10)

m.c104 = Constraint(expr=   0.766261028176921*m.x103 + 0.766261028176921*m.x105 + 0.936329177569045*m.x109
                          + 0.936329177569045*m.x110 == -10)

m.c105 = Constraint(expr=   m.x102 + 0.574695771132691*m.x104 + 0.574695771132691*m.x106 == 0)

m.c106 = Constraint(expr= - 0.287347885566345*m.x104 + 0.287347885566345*m.x106 - 0.351123441588392*m.x107
                          + 0.351123441588392*m.x108 == 10)

m.c107 = Constraint(expr=   0.766261028176921*m.x104 + 0.766261028176921*m.x106 + 0.936329177569045*m.x107
                          + 0.936329177569045*m.x108 == -10)

m.c108 = Constraint(expr= - 0.574695771132691*m.x104 - m.x113 + 0.345032779671177*m.x115 - 0.75907211527659*m.x120
                          + 0.468292905790847*m.x124 == 0.5)

m.c109 = Constraint(expr=   0.287347885566345*m.x104 + 0.351123441588392*m.x109 + m.x111 + 0.75907211527659*m.x115
                          - 0.345032779671177*m.x120 - 0.468292905790847*m.x124 == 0)

m.c110 = Constraint(expr= - 0.766261028176921*m.x104 - 0.936329177569045*m.x109 + 0.552052447473883*m.x115
                          + 0.552052447473883*m.x120 + 0.749268649265355*m.x124 == 0)

m.c111 = Constraint(expr=   0.574695771132691*m.x103 + m.x113 - 0.345032779671177*m.x117 + 0.75907211527659*m.x119
                          - 0.468292905790847*m.x125 == 0)

m.c112 = Constraint(expr=   0.287347885566345*m.x103 + 0.351123441588392*m.x107 + m.x112 + 0.75907211527659*m.x117
                          - 0.345032779671177*m.x119 - 0.468292905790847*m.x125 == 0)

m.c113 = Constraint(expr= - 0.766261028176921*m.x103 - 0.936329177569045*m.x107 + 0.552052447473883*m.x117
                          + 0.552052447473883*m.x119 + 0.749268649265355*m.x125 == 0)

m.c114 = Constraint(expr=   0.574695771132691*m.x105 + m.x114 - 0.345032779671177*m.x118 + 0.75907211527659*m.x121
                          - 0.468292905790847*m.x126 == 0)

m.c115 = Constraint(expr= - 0.287347885566345*m.x105 - 0.351123441588392*m.x108 - m.x112 - 0.75907211527659*m.x118
                          + 0.345032779671177*m.x121 + 0.468292905790847*m.x126 == 0)

m.c116 = Constraint(expr= - 0.766261028176921*m.x105 - 0.936329177569045*m.x108 + 0.552052447473883*m.x118
                          + 0.552052447473883*m.x121 + 0.749268649265355*m.x126 == 0)

m.c117 = Constraint(expr= - 0.574695771132691*m.x106 - m.x114 + 0.345032779671177*m.x116 - 0.75907211527659*m.x122
                          + 0.468292905790847*m.x123 == 0.6)

m.c118 = Constraint(expr= - 0.287347885566345*m.x106 - 0.351123441588392*m.x110 - m.x111 - 0.75907211527659*m.x116
                          + 0.345032779671177*m.x122 + 0.468292905790847*m.x123 == 0)

m.c119 = Constraint(expr= - 0.766261028176921*m.x106 - 0.936329177569045*m.x110 + 0.552052447473883*m.x116
                          + 0.552052447473883*m.x122 + 0.749268649265355*m.x123 == 0)

m.c120 = Constraint(expr= - m.x52 + m.x102 <= 0)

m.c121 = Constraint(expr= - m.x53 - m.x102 <= 0)

m.c122 = Constraint(expr= - m.x54 + m.x103 <= 0)

m.c123 = Constraint(expr= - m.x55 - m.x103 <= 0)

m.c124 = Constraint(expr= - m.x56 + m.x104 <= 0)

m.c125 = Constraint(expr= - m.x57 - m.x104 <= 0)

m.c126 = Constraint(expr= - m.x58 + m.x105 <= 0)

m.c127 = Constraint(expr= - m.x59 - m.x105 <= 0)

m.c128 = Constraint(expr= - m.x60 + m.x106 <= 0)

m.c129 = Constraint(expr= - m.x61 - m.x106 <= 0)

m.c130 = Constraint(expr= - m.x62 + m.x107 <= 0)

m.c131 = Constraint(expr= - m.x63 - m.x107 <= 0)

m.c132 = Constraint(expr= - m.x64 + m.x108 <= 0)

m.c133 = Constraint(expr= - m.x65 - m.x108 <= 0)

m.c134 = Constraint(expr= - m.x66 + m.x109 <= 0)

m.c135 = Constraint(expr= - m.x67 - m.x109 <= 0)

m.c136 = Constraint(expr= - m.x68 + m.x110 <= 0)

m.c137 = Constraint(expr= - m.x69 - m.x110 <= 0)

m.c138 = Constraint(expr= - m.x70 + m.x111 <= 0)

m.c139 = Constraint(expr= - m.x71 - m.x111 <= 0)

m.c140 = Constraint(expr= - m.x72 + m.x112 <= 0)

m.c141 = Constraint(expr= - m.x73 - m.x112 <= 0)

m.c142 = Constraint(expr= - m.x74 + m.x113 <= 0)

m.c143 = Constraint(expr= - m.x75 - m.x113 <= 0)

m.c144 = Constraint(expr= - m.x76 + m.x114 <= 0)

m.c145 = Constraint(expr= - m.x77 - m.x114 <= 0)

m.c146 = Constraint(expr= - m.x78 + m.x115 <= 0)

m.c147 = Constraint(expr= - m.x79 - m.x115 <= 0)

m.c148 = Constraint(expr= - m.x80 + m.x116 <= 0)

m.c149 = Constraint(expr= - m.x81 - m.x116 <= 0)

m.c150 = Constraint(expr= - m.x82 + m.x117 <= 0)

m.c151 = Constraint(expr= - m.x83 - m.x117 <= 0)

m.c152 = Constraint(expr= - m.x84 + m.x118 <= 0)

m.c153 = Constraint(expr= - m.x85 - m.x118 <= 0)

m.c154 = Constraint(expr= - m.x86 + m.x119 <= 0)

m.c155 = Constraint(expr= - m.x87 - m.x119 <= 0)

m.c156 = Constraint(expr= - m.x88 + m.x120 <= 0)

m.c157 = Constraint(expr= - m.x89 - m.x120 <= 0)

m.c158 = Constraint(expr= - m.x90 + m.x121 <= 0)

m.c159 = Constraint(expr= - m.x91 - m.x121 <= 0)

m.c160 = Constraint(expr= - m.x92 + m.x122 <= 0)

m.c161 = Constraint(expr= - m.x93 - m.x122 <= 0)

m.c162 = Constraint(expr= - m.x94 + m.x123 <= 0)

m.c163 = Constraint(expr= - m.x95 - m.x123 <= 0)

m.c164 = Constraint(expr= - m.x96 + m.x124 <= 0)

m.c165 = Constraint(expr= - m.x97 - m.x124 <= 0)

m.c166 = Constraint(expr= - m.x98 + m.x125 <= 0)

m.c167 = Constraint(expr= - m.x99 - m.x125 <= 0)

m.c168 = Constraint(expr= - m.x100 + m.x126 <= 0)

m.c169 = Constraint(expr= - m.x101 - m.x126 <= 0)

m.c170 = Constraint(expr= - m.x2 + 0.1*m.b145 + 0.2*m.b146 + 0.3*m.b147 + 0.4*m.b148 + 0.5*m.b149 + 0.6*m.b150
                          + 0.7*m.b151 + 0.8*m.b152 + 0.9*m.b153 + m.b154 + 1.1*m.b155 + 1.2*m.b156 + 1.3*m.b157
                          + 1.4*m.b158 + 1.5*m.b159 + 1.6*m.b160 + 1.7*m.b161 + 1.8*m.b162 + 1.9*m.b163 + 2*m.b164
                          + 2.1*m.b165 + 2.2*m.b166 + 2.3*m.b167 + 2.4*m.b168 + 2.5*m.b169 + 2.6*m.b170 + 2.8*m.b171
                          + 3*m.b172 + 3.2*m.b173 + 3.4*m.b174 == 0)

m.c171 = Constraint(expr= - m.x3 + 0.1*m.b175 + 0.2*m.b176 + 0.3*m.b177 + 0.4*m.b178 + 0.5*m.b179 + 0.6*m.b180
                          + 0.7*m.b181 + 0.8*m.b182 + 0.9*m.b183 + m.b184 + 1.1*m.b185 + 1.2*m.b186 + 1.3*m.b187
                          + 1.4*m.b188 + 1.5*m.b189 + 1.6*m.b190 + 1.7*m.b191 + 1.8*m.b192 + 1.9*m.b193 + 2*m.b194
                          + 2.1*m.b195 + 2.2*m.b196 + 2.3*m.b197 + 2.4*m.b198 + 2.5*m.b199 + 2.6*m.b200 + 2.8*m.b201
                          + 3*m.b202 + 3.2*m.b203 + 3.4*m.b204 == 0)

m.c172 = Constraint(expr= - m.x4 + 0.1*m.b175 + 0.2*m.b176 + 0.3*m.b177 + 0.4*m.b178 + 0.5*m.b179 + 0.6*m.b180
                          + 0.7*m.b181 + 0.8*m.b182 + 0.9*m.b183 + m.b184 + 1.1*m.b185 + 1.2*m.b186 + 1.3*m.b187
                          + 1.4*m.b188 + 1.5*m.b189 + 1.6*m.b190 + 1.7*m.b191 + 1.8*m.b192 + 1.9*m.b193 + 2*m.b194
                          + 2.1*m.b195 + 2.2*m.b196 + 2.3*m.b197 + 2.4*m.b198 + 2.5*m.b199 + 2.6*m.b200 + 2.8*m.b201
                          + 3*m.b202 + 3.2*m.b203 + 3.4*m.b204 == 0)

m.c173 = Constraint(expr= - m.x5 + 0.1*m.b175 + 0.2*m.b176 + 0.3*m.b177 + 0.4*m.b178 + 0.5*m.b179 + 0.6*m.b180
                          + 0.7*m.b181 + 0.8*m.b182 + 0.9*m.b183 + m.b184 + 1.1*m.b185 + 1.2*m.b186 + 1.3*m.b187
                          + 1.4*m.b188 + 1.5*m.b189 + 1.6*m.b190 + 1.7*m.b191 + 1.8*m.b192 + 1.9*m.b193 + 2*m.b194
                          + 2.1*m.b195 + 2.2*m.b196 + 2.3*m.b197 + 2.4*m.b198 + 2.5*m.b199 + 2.6*m.b200 + 2.8*m.b201
                          + 3*m.b202 + 3.2*m.b203 + 3.4*m.b204 == 0)

m.c174 = Constraint(expr= - m.x6 + 0.1*m.b175 + 0.2*m.b176 + 0.3*m.b177 + 0.4*m.b178 + 0.5*m.b179 + 0.6*m.b180
                          + 0.7*m.b181 + 0.8*m.b182 + 0.9*m.b183 + m.b184 + 1.1*m.b185 + 1.2*m.b186 + 1.3*m.b187
                          + 1.4*m.b188 + 1.5*m.b189 + 1.6*m.b190 + 1.7*m.b191 + 1.8*m.b192 + 1.9*m.b193 + 2*m.b194
                          + 2.1*m.b195 + 2.2*m.b196 + 2.3*m.b197 + 2.4*m.b198 + 2.5*m.b199 + 2.6*m.b200 + 2.8*m.b201
                          + 3*m.b202 + 3.2*m.b203 + 3.4*m.b204 == 0)

m.c175 = Constraint(expr= - m.x7 + 0.1*m.b205 + 0.2*m.b206 + 0.3*m.b207 + 0.4*m.b208 + 0.5*m.b209 + 0.6*m.b210
                          + 0.7*m.b211 + 0.8*m.b212 + 0.9*m.b213 + m.b214 + 1.1*m.b215 + 1.2*m.b216 + 1.3*m.b217
                          + 1.4*m.b218 + 1.5*m.b219 + 1.6*m.b220 + 1.7*m.b221 + 1.8*m.b222 + 1.9*m.b223 + 2*m.b224
                          + 2.1*m.b225 + 2.2*m.b226 + 2.3*m.b227 + 2.4*m.b228 + 2.5*m.b229 + 2.6*m.b230 + 2.8*m.b231
                          + 3*m.b232 + 3.2*m.b233 + 3.4*m.b234 == 0)

m.c176 = Constraint(expr= - m.x8 + 0.1*m.b205 + 0.2*m.b206 + 0.3*m.b207 + 0.4*m.b208 + 0.5*m.b209 + 0.6*m.b210
                          + 0.7*m.b211 + 0.8*m.b212 + 0.9*m.b213 + m.b214 + 1.1*m.b215 + 1.2*m.b216 + 1.3*m.b217
                          + 1.4*m.b218 + 1.5*m.b219 + 1.6*m.b220 + 1.7*m.b221 + 1.8*m.b222 + 1.9*m.b223 + 2*m.b224
                          + 2.1*m.b225 + 2.2*m.b226 + 2.3*m.b227 + 2.4*m.b228 + 2.5*m.b229 + 2.6*m.b230 + 2.8*m.b231
                          + 3*m.b232 + 3.2*m.b233 + 3.4*m.b234 == 0)

m.c177 = Constraint(expr= - m.x9 + 0.1*m.b205 + 0.2*m.b206 + 0.3*m.b207 + 0.4*m.b208 + 0.5*m.b209 + 0.6*m.b210
                          + 0.7*m.b211 + 0.8*m.b212 + 0.9*m.b213 + m.b214 + 1.1*m.b215 + 1.2*m.b216 + 1.3*m.b217
                          + 1.4*m.b218 + 1.5*m.b219 + 1.6*m.b220 + 1.7*m.b221 + 1.8*m.b222 + 1.9*m.b223 + 2*m.b224
                          + 2.1*m.b225 + 2.2*m.b226 + 2.3*m.b227 + 2.4*m.b228 + 2.5*m.b229 + 2.6*m.b230 + 2.8*m.b231
                          + 3*m.b232 + 3.2*m.b233 + 3.4*m.b234 == 0)

m.c178 = Constraint(expr= - m.x10 + 0.1*m.b205 + 0.2*m.b206 + 0.3*m.b207 + 0.4*m.b208 + 0.5*m.b209 + 0.6*m.b210
                          + 0.7*m.b211 + 0.8*m.b212 + 0.9*m.b213 + m.b214 + 1.1*m.b215 + 1.2*m.b216 + 1.3*m.b217
                          + 1.4*m.b218 + 1.5*m.b219 + 1.6*m.b220 + 1.7*m.b221 + 1.8*m.b222 + 1.9*m.b223 + 2*m.b224
                          + 2.1*m.b225 + 2.2*m.b226 + 2.3*m.b227 + 2.4*m.b228 + 2.5*m.b229 + 2.6*m.b230 + 2.8*m.b231
                          + 3*m.b232 + 3.2*m.b233 + 3.4*m.b234 == 0)

m.c179 = Constraint(expr= - m.x11 + 0.1*m.b235 + 0.2*m.b236 + 0.3*m.b237 + 0.4*m.b238 + 0.5*m.b239 + 0.6*m.b240
                          + 0.7*m.b241 + 0.8*m.b242 + 0.9*m.b243 + m.b244 + 1.1*m.b245 + 1.2*m.b246 + 1.3*m.b247
                          + 1.4*m.b248 + 1.5*m.b249 + 1.6*m.b250 + 1.7*m.b251 + 1.8*m.b252 + 1.9*m.b253 + 2*m.b254
                          + 2.1*m.b255 + 2.2*m.b256 + 2.3*m.b257 + 2.4*m.b258 + 2.5*m.b259 + 2.6*m.b260 + 2.8*m.b261
                          + 3*m.b262 + 3.2*m.b263 + 3.4*m.b264 == 0)

m.c180 = Constraint(expr= - m.x12 + 0.1*m.b235 + 0.2*m.b236 + 0.3*m.b237 + 0.4*m.b238 + 0.5*m.b239 + 0.6*m.b240
                          + 0.7*m.b241 + 0.8*m.b242 + 0.9*m.b243 + m.b244 + 1.1*m.b245 + 1.2*m.b246 + 1.3*m.b247
                          + 1.4*m.b248 + 1.5*m.b249 + 1.6*m.b250 + 1.7*m.b251 + 1.8*m.b252 + 1.9*m.b253 + 2*m.b254
                          + 2.1*m.b255 + 2.2*m.b256 + 2.3*m.b257 + 2.4*m.b258 + 2.5*m.b259 + 2.6*m.b260 + 2.8*m.b261
                          + 3*m.b262 + 3.2*m.b263 + 3.4*m.b264 == 0)

m.c181 = Constraint(expr= - m.x13 + 0.1*m.b265 + 0.2*m.b266 + 0.3*m.b267 + 0.4*m.b268 + 0.5*m.b269 + 0.6*m.b270
                          + 0.7*m.b271 + 0.8*m.b272 + 0.9*m.b273 + m.b274 + 1.1*m.b275 + 1.2*m.b276 + 1.3*m.b277
                          + 1.4*m.b278 + 1.5*m.b279 + 1.6*m.b280 + 1.7*m.b281 + 1.8*m.b282 + 1.9*m.b283 + 2*m.b284
                          + 2.1*m.b285 + 2.2*m.b286 + 2.3*m.b287 + 2.4*m.b288 + 2.5*m.b289 + 2.6*m.b290 + 2.8*m.b291
                          + 3*m.b292 + 3.2*m.b293 + 3.4*m.b294 == 0)

m.c182 = Constraint(expr= - m.x14 + 0.1*m.b265 + 0.2*m.b266 + 0.3*m.b267 + 0.4*m.b268 + 0.5*m.b269 + 0.6*m.b270
                          + 0.7*m.b271 + 0.8*m.b272 + 0.9*m.b273 + m.b274 + 1.1*m.b275 + 1.2*m.b276 + 1.3*m.b277
                          + 1.4*m.b278 + 1.5*m.b279 + 1.6*m.b280 + 1.7*m.b281 + 1.8*m.b282 + 1.9*m.b283 + 2*m.b284
                          + 2.1*m.b285 + 2.2*m.b286 + 2.3*m.b287 + 2.4*m.b288 + 2.5*m.b289 + 2.6*m.b290 + 2.8*m.b291
                          + 3*m.b292 + 3.2*m.b293 + 3.4*m.b294 == 0)

m.c183 = Constraint(expr= - m.x15 + 0.1*m.b295 + 0.2*m.b296 + 0.3*m.b297 + 0.4*m.b298 + 0.5*m.b299 + 0.6*m.b300
                          + 0.7*m.b301 + 0.8*m.b302 + 0.9*m.b303 + m.b304 + 1.1*m.b305 + 1.2*m.b306 + 1.3*m.b307
                          + 1.4*m.b308 + 1.5*m.b309 + 1.6*m.b310 + 1.7*m.b311 + 1.8*m.b312 + 1.9*m.b313 + 2*m.b314
                          + 2.1*m.b315 + 2.2*m.b316 + 2.3*m.b317 + 2.4*m.b318 + 2.5*m.b319 + 2.6*m.b320 + 2.8*m.b321
                          + 3*m.b322 + 3.2*m.b323 + 3.4*m.b324 == 0)

m.c184 = Constraint(expr= - m.x16 + 0.1*m.b295 + 0.2*m.b296 + 0.3*m.b297 + 0.4*m.b298 + 0.5*m.b299 + 0.6*m.b300
                          + 0.7*m.b301 + 0.8*m.b302 + 0.9*m.b303 + m.b304 + 1.1*m.b305 + 1.2*m.b306 + 1.3*m.b307
                          + 1.4*m.b308 + 1.5*m.b309 + 1.6*m.b310 + 1.7*m.b311 + 1.8*m.b312 + 1.9*m.b313 + 2*m.b314
                          + 2.1*m.b315 + 2.2*m.b316 + 2.3*m.b317 + 2.4*m.b318 + 2.5*m.b319 + 2.6*m.b320 + 2.8*m.b321
                          + 3*m.b322 + 3.2*m.b323 + 3.4*m.b324 == 0)

m.c185 = Constraint(expr= - m.x17 + 0.1*m.b295 + 0.2*m.b296 + 0.3*m.b297 + 0.4*m.b298 + 0.5*m.b299 + 0.6*m.b300
                          + 0.7*m.b301 + 0.8*m.b302 + 0.9*m.b303 + m.b304 + 1.1*m.b305 + 1.2*m.b306 + 1.3*m.b307
                          + 1.4*m.b308 + 1.5*m.b309 + 1.6*m.b310 + 1.7*m.b311 + 1.8*m.b312 + 1.9*m.b313 + 2*m.b314
                          + 2.1*m.b315 + 2.2*m.b316 + 2.3*m.b317 + 2.4*m.b318 + 2.5*m.b319 + 2.6*m.b320 + 2.8*m.b321
                          + 3*m.b322 + 3.2*m.b323 + 3.4*m.b324 == 0)

m.c186 = Constraint(expr= - m.x18 + 0.1*m.b295 + 0.2*m.b296 + 0.3*m.b297 + 0.4*m.b298 + 0.5*m.b299 + 0.6*m.b300
                          + 0.7*m.b301 + 0.8*m.b302 + 0.9*m.b303 + m.b304 + 1.1*m.b305 + 1.2*m.b306 + 1.3*m.b307
                          + 1.4*m.b308 + 1.5*m.b309 + 1.6*m.b310 + 1.7*m.b311 + 1.8*m.b312 + 1.9*m.b313 + 2*m.b314
                          + 2.1*m.b315 + 2.2*m.b316 + 2.3*m.b317 + 2.4*m.b318 + 2.5*m.b319 + 2.6*m.b320 + 2.8*m.b321
                          + 3*m.b322 + 3.2*m.b323 + 3.4*m.b324 == 0)

m.c187 = Constraint(expr= - m.x19 + 0.1*m.b325 + 0.2*m.b326 + 0.3*m.b327 + 0.4*m.b328 + 0.5*m.b329 + 0.6*m.b330
                          + 0.7*m.b331 + 0.8*m.b332 + 0.9*m.b333 + m.b334 + 1.1*m.b335 + 1.2*m.b336 + 1.3*m.b337
                          + 1.4*m.b338 + 1.5*m.b339 + 1.6*m.b340 + 1.7*m.b341 + 1.8*m.b342 + 1.9*m.b343 + 2*m.b344
                          + 2.1*m.b345 + 2.2*m.b346 + 2.3*m.b347 + 2.4*m.b348 + 2.5*m.b349 + 2.6*m.b350 + 2.8*m.b351
                          + 3*m.b352 + 3.2*m.b353 + 3.4*m.b354 == 0)

m.c188 = Constraint(expr= - m.x20 + 0.1*m.b325 + 0.2*m.b326 + 0.3*m.b327 + 0.4*m.b328 + 0.5*m.b329 + 0.6*m.b330
                          + 0.7*m.b331 + 0.8*m.b332 + 0.9*m.b333 + m.b334 + 1.1*m.b335 + 1.2*m.b336 + 1.3*m.b337
                          + 1.4*m.b338 + 1.5*m.b339 + 1.6*m.b340 + 1.7*m.b341 + 1.8*m.b342 + 1.9*m.b343 + 2*m.b344
                          + 2.1*m.b345 + 2.2*m.b346 + 2.3*m.b347 + 2.4*m.b348 + 2.5*m.b349 + 2.6*m.b350 + 2.8*m.b351
                          + 3*m.b352 + 3.2*m.b353 + 3.4*m.b354 == 0)

m.c189 = Constraint(expr= - m.x21 + 0.1*m.b325 + 0.2*m.b326 + 0.3*m.b327 + 0.4*m.b328 + 0.5*m.b329 + 0.6*m.b330
                          + 0.7*m.b331 + 0.8*m.b332 + 0.9*m.b333 + m.b334 + 1.1*m.b335 + 1.2*m.b336 + 1.3*m.b337
                          + 1.4*m.b338 + 1.5*m.b339 + 1.6*m.b340 + 1.7*m.b341 + 1.8*m.b342 + 1.9*m.b343 + 2*m.b344
                          + 2.1*m.b345 + 2.2*m.b346 + 2.3*m.b347 + 2.4*m.b348 + 2.5*m.b349 + 2.6*m.b350 + 2.8*m.b351
                          + 3*m.b352 + 3.2*m.b353 + 3.4*m.b354 == 0)

m.c190 = Constraint(expr= - m.x22 + 0.1*m.b325 + 0.2*m.b326 + 0.3*m.b327 + 0.4*m.b328 + 0.5*m.b329 + 0.6*m.b330
                          + 0.7*m.b331 + 0.8*m.b332 + 0.9*m.b333 + m.b334 + 1.1*m.b335 + 1.2*m.b336 + 1.3*m.b337
                          + 1.4*m.b338 + 1.5*m.b339 + 1.6*m.b340 + 1.7*m.b341 + 1.8*m.b342 + 1.9*m.b343 + 2*m.b344
                          + 2.1*m.b345 + 2.2*m.b346 + 2.3*m.b347 + 2.4*m.b348 + 2.5*m.b349 + 2.6*m.b350 + 2.8*m.b351
                          + 3*m.b352 + 3.2*m.b353 + 3.4*m.b354 == 0)

m.c191 = Constraint(expr= - m.x23 + 0.1*m.b355 + 0.2*m.b356 + 0.3*m.b357 + 0.4*m.b358 + 0.5*m.b359 + 0.6*m.b360
                          + 0.7*m.b361 + 0.8*m.b362 + 0.9*m.b363 + m.b364 + 1.1*m.b365 + 1.2*m.b366 + 1.3*m.b367
                          + 1.4*m.b368 + 1.5*m.b369 + 1.6*m.b370 + 1.7*m.b371 + 1.8*m.b372 + 1.9*m.b373 + 2*m.b374
                          + 2.1*m.b375 + 2.2*m.b376 + 2.3*m.b377 + 2.4*m.b378 + 2.5*m.b379 + 2.6*m.b380 + 2.8*m.b381
                          + 3*m.b382 + 3.2*m.b383 + 3.4*m.b384 == 0)

m.c192 = Constraint(expr= - m.x24 + 0.1*m.b355 + 0.2*m.b356 + 0.3*m.b357 + 0.4*m.b358 + 0.5*m.b359 + 0.6*m.b360
                          + 0.7*m.b361 + 0.8*m.b362 + 0.9*m.b363 + m.b364 + 1.1*m.b365 + 1.2*m.b366 + 1.3*m.b367
                          + 1.4*m.b368 + 1.5*m.b369 + 1.6*m.b370 + 1.7*m.b371 + 1.8*m.b372 + 1.9*m.b373 + 2*m.b374
                          + 2.1*m.b375 + 2.2*m.b376 + 2.3*m.b377 + 2.4*m.b378 + 2.5*m.b379 + 2.6*m.b380 + 2.8*m.b381
                          + 3*m.b382 + 3.2*m.b383 + 3.4*m.b384 == 0)

m.c193 = Constraint(expr= - m.x25 + 0.1*m.b355 + 0.2*m.b356 + 0.3*m.b357 + 0.4*m.b358 + 0.5*m.b359 + 0.6*m.b360
                          + 0.7*m.b361 + 0.8*m.b362 + 0.9*m.b363 + m.b364 + 1.1*m.b365 + 1.2*m.b366 + 1.3*m.b367
                          + 1.4*m.b368 + 1.5*m.b369 + 1.6*m.b370 + 1.7*m.b371 + 1.8*m.b372 + 1.9*m.b373 + 2*m.b374
                          + 2.1*m.b375 + 2.2*m.b376 + 2.3*m.b377 + 2.4*m.b378 + 2.5*m.b379 + 2.6*m.b380 + 2.8*m.b381
                          + 3*m.b382 + 3.2*m.b383 + 3.4*m.b384 == 0)

m.c194 = Constraint(expr= - m.x26 + 0.1*m.b355 + 0.2*m.b356 + 0.3*m.b357 + 0.4*m.b358 + 0.5*m.b359 + 0.6*m.b360
                          + 0.7*m.b361 + 0.8*m.b362 + 0.9*m.b363 + m.b364 + 1.1*m.b365 + 1.2*m.b366 + 1.3*m.b367
                          + 1.4*m.b368 + 1.5*m.b369 + 1.6*m.b370 + 1.7*m.b371 + 1.8*m.b372 + 1.9*m.b373 + 2*m.b374
                          + 2.1*m.b375 + 2.2*m.b376 + 2.3*m.b377 + 2.4*m.b378 + 2.5*m.b379 + 2.6*m.b380 + 2.8*m.b381
                          + 3*m.b382 + 3.2*m.b383 + 3.4*m.b384 == 0)

m.c195 = Constraint(expr=   m.b145 + m.b146 + m.b147 + m.b148 + m.b149 + m.b150 + m.b151 + m.b152 + m.b153 + m.b154
                          + m.b155 + m.b156 + m.b157 + m.b158 + m.b159 + m.b160 + m.b161 + m.b162 + m.b163 + m.b164
                          + m.b165 + m.b166 + m.b167 + m.b168 + m.b169 + m.b170 + m.b171 + m.b172 + m.b173 + m.b174
                          == 1)

m.c196 = Constraint(expr=   m.b175 + m.b176 + m.b177 + m.b178 + m.b179 + m.b180 + m.b181 + m.b182 + m.b183 + m.b184
                          + m.b185 + m.b186 + m.b187 + m.b188 + m.b189 + m.b190 + m.b191 + m.b192 + m.b193 + m.b194
                          + m.b195 + m.b196 + m.b197 + m.b198 + m.b199 + m.b200 + m.b201 + m.b202 + m.b203 + m.b204
                          == 1)

m.c197 = Constraint(expr=   m.b205 + m.b206 + m.b207 + m.b208 + m.b209 + m.b210 + m.b211 + m.b212 + m.b213 + m.b214
                          + m.b215 + m.b216 + m.b217 + m.b218 + m.b219 + m.b220 + m.b221 + m.b222 + m.b223 + m.b224
                          + m.b225 + m.b226 + m.b227 + m.b228 + m.b229 + m.b230 + m.b231 + m.b232 + m.b233 + m.b234
                          == 1)

m.c198 = Constraint(expr=   m.b235 + m.b236 + m.b237 + m.b238 + m.b239 + m.b240 + m.b241 + m.b242 + m.b243 + m.b244
                          + m.b245 + m.b246 + m.b247 + m.b248 + m.b249 + m.b250 + m.b251 + m.b252 + m.b253 + m.b254
                          + m.b255 + m.b256 + m.b257 + m.b258 + m.b259 + m.b260 + m.b261 + m.b262 + m.b263 + m.b264
                          == 1)

m.c199 = Constraint(expr=   m.b265 + m.b266 + m.b267 + m.b268 + m.b269 + m.b270 + m.b271 + m.b272 + m.b273 + m.b274
                          + m.b275 + m.b276 + m.b277 + m.b278 + m.b279 + m.b280 + m.b281 + m.b282 + m.b283 + m.b284
                          + m.b285 + m.b286 + m.b287 + m.b288 + m.b289 + m.b290 + m.b291 + m.b292 + m.b293 + m.b294
                          == 1)

m.c200 = Constraint(expr=   m.b295 + m.b296 + m.b297 + m.b298 + m.b299 + m.b300 + m.b301 + m.b302 + m.b303 + m.b304
                          + m.b305 + m.b306 + m.b307 + m.b308 + m.b309 + m.b310 + m.b311 + m.b312 + m.b313 + m.b314
                          + m.b315 + m.b316 + m.b317 + m.b318 + m.b319 + m.b320 + m.b321 + m.b322 + m.b323 + m.b324
                          == 1)

m.c201 = Constraint(expr=   m.b325 + m.b326 + m.b327 + m.b328 + m.b329 + m.b330 + m.b331 + m.b332 + m.b333 + m.b334
                          + m.b335 + m.b336 + m.b337 + m.b338 + m.b339 + m.b340 + m.b341 + m.b342 + m.b343 + m.b344
                          + m.b345 + m.b346 + m.b347 + m.b348 + m.b349 + m.b350 + m.b351 + m.b352 + m.b353 + m.b354
                          == 1)

m.c202 = Constraint(expr=   m.b355 + m.b356 + m.b357 + m.b358 + m.b359 + m.b360 + m.b361 + m.b362 + m.b363 + m.b364
                          + m.b365 + m.b366 + m.b367 + m.b368 + m.b369 + m.b370 + m.b371 + m.b372 + m.b373 + m.b374
                          + m.b375 + m.b376 + m.b377 + m.b378 + m.b379 + m.b380 + m.b381 + m.b382 + m.b383 + m.b384
                          == 1)
