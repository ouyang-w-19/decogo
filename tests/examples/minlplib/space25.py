#  MINLP written by GAMS Convert at 04/21/18 13:54:16
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        236      186        0       50        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        894      144      750        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2057     1946      111        0
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

m.c172 = Constraint(expr= - m.x4 + 0.1*m.b205 + 0.2*m.b206 + 0.3*m.b207 + 0.4*m.b208 + 0.5*m.b209 + 0.6*m.b210
                          + 0.7*m.b211 + 0.8*m.b212 + 0.9*m.b213 + m.b214 + 1.1*m.b215 + 1.2*m.b216 + 1.3*m.b217
                          + 1.4*m.b218 + 1.5*m.b219 + 1.6*m.b220 + 1.7*m.b221 + 1.8*m.b222 + 1.9*m.b223 + 2*m.b224
                          + 2.1*m.b225 + 2.2*m.b226 + 2.3*m.b227 + 2.4*m.b228 + 2.5*m.b229 + 2.6*m.b230 + 2.8*m.b231
                          + 3*m.b232 + 3.2*m.b233 + 3.4*m.b234 == 0)

m.c173 = Constraint(expr= - m.x5 + 0.1*m.b235 + 0.2*m.b236 + 0.3*m.b237 + 0.4*m.b238 + 0.5*m.b239 + 0.6*m.b240
                          + 0.7*m.b241 + 0.8*m.b242 + 0.9*m.b243 + m.b244 + 1.1*m.b245 + 1.2*m.b246 + 1.3*m.b247
                          + 1.4*m.b248 + 1.5*m.b249 + 1.6*m.b250 + 1.7*m.b251 + 1.8*m.b252 + 1.9*m.b253 + 2*m.b254
                          + 2.1*m.b255 + 2.2*m.b256 + 2.3*m.b257 + 2.4*m.b258 + 2.5*m.b259 + 2.6*m.b260 + 2.8*m.b261
                          + 3*m.b262 + 3.2*m.b263 + 3.4*m.b264 == 0)

m.c174 = Constraint(expr= - m.x6 + 0.1*m.b265 + 0.2*m.b266 + 0.3*m.b267 + 0.4*m.b268 + 0.5*m.b269 + 0.6*m.b270
                          + 0.7*m.b271 + 0.8*m.b272 + 0.9*m.b273 + m.b274 + 1.1*m.b275 + 1.2*m.b276 + 1.3*m.b277
                          + 1.4*m.b278 + 1.5*m.b279 + 1.6*m.b280 + 1.7*m.b281 + 1.8*m.b282 + 1.9*m.b283 + 2*m.b284
                          + 2.1*m.b285 + 2.2*m.b286 + 2.3*m.b287 + 2.4*m.b288 + 2.5*m.b289 + 2.6*m.b290 + 2.8*m.b291
                          + 3*m.b292 + 3.2*m.b293 + 3.4*m.b294 == 0)

m.c175 = Constraint(expr= - m.x7 + 0.1*m.b295 + 0.2*m.b296 + 0.3*m.b297 + 0.4*m.b298 + 0.5*m.b299 + 0.6*m.b300
                          + 0.7*m.b301 + 0.8*m.b302 + 0.9*m.b303 + m.b304 + 1.1*m.b305 + 1.2*m.b306 + 1.3*m.b307
                          + 1.4*m.b308 + 1.5*m.b309 + 1.6*m.b310 + 1.7*m.b311 + 1.8*m.b312 + 1.9*m.b313 + 2*m.b314
                          + 2.1*m.b315 + 2.2*m.b316 + 2.3*m.b317 + 2.4*m.b318 + 2.5*m.b319 + 2.6*m.b320 + 2.8*m.b321
                          + 3*m.b322 + 3.2*m.b323 + 3.4*m.b324 == 0)

m.c176 = Constraint(expr= - m.x8 + 0.1*m.b325 + 0.2*m.b326 + 0.3*m.b327 + 0.4*m.b328 + 0.5*m.b329 + 0.6*m.b330
                          + 0.7*m.b331 + 0.8*m.b332 + 0.9*m.b333 + m.b334 + 1.1*m.b335 + 1.2*m.b336 + 1.3*m.b337
                          + 1.4*m.b338 + 1.5*m.b339 + 1.6*m.b340 + 1.7*m.b341 + 1.8*m.b342 + 1.9*m.b343 + 2*m.b344
                          + 2.1*m.b345 + 2.2*m.b346 + 2.3*m.b347 + 2.4*m.b348 + 2.5*m.b349 + 2.6*m.b350 + 2.8*m.b351
                          + 3*m.b352 + 3.2*m.b353 + 3.4*m.b354 == 0)

m.c177 = Constraint(expr= - m.x9 + 0.1*m.b355 + 0.2*m.b356 + 0.3*m.b357 + 0.4*m.b358 + 0.5*m.b359 + 0.6*m.b360
                          + 0.7*m.b361 + 0.8*m.b362 + 0.9*m.b363 + m.b364 + 1.1*m.b365 + 1.2*m.b366 + 1.3*m.b367
                          + 1.4*m.b368 + 1.5*m.b369 + 1.6*m.b370 + 1.7*m.b371 + 1.8*m.b372 + 1.9*m.b373 + 2*m.b374
                          + 2.1*m.b375 + 2.2*m.b376 + 2.3*m.b377 + 2.4*m.b378 + 2.5*m.b379 + 2.6*m.b380 + 2.8*m.b381
                          + 3*m.b382 + 3.2*m.b383 + 3.4*m.b384 == 0)

m.c178 = Constraint(expr= - m.x10 + 0.1*m.b385 + 0.2*m.b386 + 0.3*m.b387 + 0.4*m.b388 + 0.5*m.b389 + 0.6*m.b390
                          + 0.7*m.b391 + 0.8*m.b392 + 0.9*m.b393 + m.b394 + 1.1*m.b395 + 1.2*m.b396 + 1.3*m.b397
                          + 1.4*m.b398 + 1.5*m.b399 + 1.6*m.b400 + 1.7*m.b401 + 1.8*m.b402 + 1.9*m.b403 + 2*m.b404
                          + 2.1*m.b405 + 2.2*m.b406 + 2.3*m.b407 + 2.4*m.b408 + 2.5*m.b409 + 2.6*m.b410 + 2.8*m.b411
                          + 3*m.b412 + 3.2*m.b413 + 3.4*m.b414 == 0)

m.c179 = Constraint(expr= - m.x11 + 0.1*m.b415 + 0.2*m.b416 + 0.3*m.b417 + 0.4*m.b418 + 0.5*m.b419 + 0.6*m.b420
                          + 0.7*m.b421 + 0.8*m.b422 + 0.9*m.b423 + m.b424 + 1.1*m.b425 + 1.2*m.b426 + 1.3*m.b427
                          + 1.4*m.b428 + 1.5*m.b429 + 1.6*m.b430 + 1.7*m.b431 + 1.8*m.b432 + 1.9*m.b433 + 2*m.b434
                          + 2.1*m.b435 + 2.2*m.b436 + 2.3*m.b437 + 2.4*m.b438 + 2.5*m.b439 + 2.6*m.b440 + 2.8*m.b441
                          + 3*m.b442 + 3.2*m.b443 + 3.4*m.b444 == 0)

m.c180 = Constraint(expr= - m.x12 + 0.1*m.b445 + 0.2*m.b446 + 0.3*m.b447 + 0.4*m.b448 + 0.5*m.b449 + 0.6*m.b450
                          + 0.7*m.b451 + 0.8*m.b452 + 0.9*m.b453 + m.b454 + 1.1*m.b455 + 1.2*m.b456 + 1.3*m.b457
                          + 1.4*m.b458 + 1.5*m.b459 + 1.6*m.b460 + 1.7*m.b461 + 1.8*m.b462 + 1.9*m.b463 + 2*m.b464
                          + 2.1*m.b465 + 2.2*m.b466 + 2.3*m.b467 + 2.4*m.b468 + 2.5*m.b469 + 2.6*m.b470 + 2.8*m.b471
                          + 3*m.b472 + 3.2*m.b473 + 3.4*m.b474 == 0)

m.c181 = Constraint(expr= - m.x13 + 0.1*m.b475 + 0.2*m.b476 + 0.3*m.b477 + 0.4*m.b478 + 0.5*m.b479 + 0.6*m.b480
                          + 0.7*m.b481 + 0.8*m.b482 + 0.9*m.b483 + m.b484 + 1.1*m.b485 + 1.2*m.b486 + 1.3*m.b487
                          + 1.4*m.b488 + 1.5*m.b489 + 1.6*m.b490 + 1.7*m.b491 + 1.8*m.b492 + 1.9*m.b493 + 2*m.b494
                          + 2.1*m.b495 + 2.2*m.b496 + 2.3*m.b497 + 2.4*m.b498 + 2.5*m.b499 + 2.6*m.b500 + 2.8*m.b501
                          + 3*m.b502 + 3.2*m.b503 + 3.4*m.b504 == 0)

m.c182 = Constraint(expr= - m.x14 + 0.1*m.b505 + 0.2*m.b506 + 0.3*m.b507 + 0.4*m.b508 + 0.5*m.b509 + 0.6*m.b510
                          + 0.7*m.b511 + 0.8*m.b512 + 0.9*m.b513 + m.b514 + 1.1*m.b515 + 1.2*m.b516 + 1.3*m.b517
                          + 1.4*m.b518 + 1.5*m.b519 + 1.6*m.b520 + 1.7*m.b521 + 1.8*m.b522 + 1.9*m.b523 + 2*m.b524
                          + 2.1*m.b525 + 2.2*m.b526 + 2.3*m.b527 + 2.4*m.b528 + 2.5*m.b529 + 2.6*m.b530 + 2.8*m.b531
                          + 3*m.b532 + 3.2*m.b533 + 3.4*m.b534 == 0)

m.c183 = Constraint(expr= - m.x15 + 0.1*m.b535 + 0.2*m.b536 + 0.3*m.b537 + 0.4*m.b538 + 0.5*m.b539 + 0.6*m.b540
                          + 0.7*m.b541 + 0.8*m.b542 + 0.9*m.b543 + m.b544 + 1.1*m.b545 + 1.2*m.b546 + 1.3*m.b547
                          + 1.4*m.b548 + 1.5*m.b549 + 1.6*m.b550 + 1.7*m.b551 + 1.8*m.b552 + 1.9*m.b553 + 2*m.b554
                          + 2.1*m.b555 + 2.2*m.b556 + 2.3*m.b557 + 2.4*m.b558 + 2.5*m.b559 + 2.6*m.b560 + 2.8*m.b561
                          + 3*m.b562 + 3.2*m.b563 + 3.4*m.b564 == 0)

m.c184 = Constraint(expr= - m.x16 + 0.1*m.b565 + 0.2*m.b566 + 0.3*m.b567 + 0.4*m.b568 + 0.5*m.b569 + 0.6*m.b570
                          + 0.7*m.b571 + 0.8*m.b572 + 0.9*m.b573 + m.b574 + 1.1*m.b575 + 1.2*m.b576 + 1.3*m.b577
                          + 1.4*m.b578 + 1.5*m.b579 + 1.6*m.b580 + 1.7*m.b581 + 1.8*m.b582 + 1.9*m.b583 + 2*m.b584
                          + 2.1*m.b585 + 2.2*m.b586 + 2.3*m.b587 + 2.4*m.b588 + 2.5*m.b589 + 2.6*m.b590 + 2.8*m.b591
                          + 3*m.b592 + 3.2*m.b593 + 3.4*m.b594 == 0)

m.c185 = Constraint(expr= - m.x17 + 0.1*m.b595 + 0.2*m.b596 + 0.3*m.b597 + 0.4*m.b598 + 0.5*m.b599 + 0.6*m.b600
                          + 0.7*m.b601 + 0.8*m.b602 + 0.9*m.b603 + m.b604 + 1.1*m.b605 + 1.2*m.b606 + 1.3*m.b607
                          + 1.4*m.b608 + 1.5*m.b609 + 1.6*m.b610 + 1.7*m.b611 + 1.8*m.b612 + 1.9*m.b613 + 2*m.b614
                          + 2.1*m.b615 + 2.2*m.b616 + 2.3*m.b617 + 2.4*m.b618 + 2.5*m.b619 + 2.6*m.b620 + 2.8*m.b621
                          + 3*m.b622 + 3.2*m.b623 + 3.4*m.b624 == 0)

m.c186 = Constraint(expr= - m.x18 + 0.1*m.b625 + 0.2*m.b626 + 0.3*m.b627 + 0.4*m.b628 + 0.5*m.b629 + 0.6*m.b630
                          + 0.7*m.b631 + 0.8*m.b632 + 0.9*m.b633 + m.b634 + 1.1*m.b635 + 1.2*m.b636 + 1.3*m.b637
                          + 1.4*m.b638 + 1.5*m.b639 + 1.6*m.b640 + 1.7*m.b641 + 1.8*m.b642 + 1.9*m.b643 + 2*m.b644
                          + 2.1*m.b645 + 2.2*m.b646 + 2.3*m.b647 + 2.4*m.b648 + 2.5*m.b649 + 2.6*m.b650 + 2.8*m.b651
                          + 3*m.b652 + 3.2*m.b653 + 3.4*m.b654 == 0)

m.c187 = Constraint(expr= - m.x19 + 0.1*m.b655 + 0.2*m.b656 + 0.3*m.b657 + 0.4*m.b658 + 0.5*m.b659 + 0.6*m.b660
                          + 0.7*m.b661 + 0.8*m.b662 + 0.9*m.b663 + m.b664 + 1.1*m.b665 + 1.2*m.b666 + 1.3*m.b667
                          + 1.4*m.b668 + 1.5*m.b669 + 1.6*m.b670 + 1.7*m.b671 + 1.8*m.b672 + 1.9*m.b673 + 2*m.b674
                          + 2.1*m.b675 + 2.2*m.b676 + 2.3*m.b677 + 2.4*m.b678 + 2.5*m.b679 + 2.6*m.b680 + 2.8*m.b681
                          + 3*m.b682 + 3.2*m.b683 + 3.4*m.b684 == 0)

m.c188 = Constraint(expr= - m.x20 + 0.1*m.b685 + 0.2*m.b686 + 0.3*m.b687 + 0.4*m.b688 + 0.5*m.b689 + 0.6*m.b690
                          + 0.7*m.b691 + 0.8*m.b692 + 0.9*m.b693 + m.b694 + 1.1*m.b695 + 1.2*m.b696 + 1.3*m.b697
                          + 1.4*m.b698 + 1.5*m.b699 + 1.6*m.b700 + 1.7*m.b701 + 1.8*m.b702 + 1.9*m.b703 + 2*m.b704
                          + 2.1*m.b705 + 2.2*m.b706 + 2.3*m.b707 + 2.4*m.b708 + 2.5*m.b709 + 2.6*m.b710 + 2.8*m.b711
                          + 3*m.b712 + 3.2*m.b713 + 3.4*m.b714 == 0)

m.c189 = Constraint(expr= - m.x21 + 0.1*m.b715 + 0.2*m.b716 + 0.3*m.b717 + 0.4*m.b718 + 0.5*m.b719 + 0.6*m.b720
                          + 0.7*m.b721 + 0.8*m.b722 + 0.9*m.b723 + m.b724 + 1.1*m.b725 + 1.2*m.b726 + 1.3*m.b727
                          + 1.4*m.b728 + 1.5*m.b729 + 1.6*m.b730 + 1.7*m.b731 + 1.8*m.b732 + 1.9*m.b733 + 2*m.b734
                          + 2.1*m.b735 + 2.2*m.b736 + 2.3*m.b737 + 2.4*m.b738 + 2.5*m.b739 + 2.6*m.b740 + 2.8*m.b741
                          + 3*m.b742 + 3.2*m.b743 + 3.4*m.b744 == 0)

m.c190 = Constraint(expr= - m.x22 + 0.1*m.b745 + 0.2*m.b746 + 0.3*m.b747 + 0.4*m.b748 + 0.5*m.b749 + 0.6*m.b750
                          + 0.7*m.b751 + 0.8*m.b752 + 0.9*m.b753 + m.b754 + 1.1*m.b755 + 1.2*m.b756 + 1.3*m.b757
                          + 1.4*m.b758 + 1.5*m.b759 + 1.6*m.b760 + 1.7*m.b761 + 1.8*m.b762 + 1.9*m.b763 + 2*m.b764
                          + 2.1*m.b765 + 2.2*m.b766 + 2.3*m.b767 + 2.4*m.b768 + 2.5*m.b769 + 2.6*m.b770 + 2.8*m.b771
                          + 3*m.b772 + 3.2*m.b773 + 3.4*m.b774 == 0)

m.c191 = Constraint(expr= - m.x23 + 0.1*m.b775 + 0.2*m.b776 + 0.3*m.b777 + 0.4*m.b778 + 0.5*m.b779 + 0.6*m.b780
                          + 0.7*m.b781 + 0.8*m.b782 + 0.9*m.b783 + m.b784 + 1.1*m.b785 + 1.2*m.b786 + 1.3*m.b787
                          + 1.4*m.b788 + 1.5*m.b789 + 1.6*m.b790 + 1.7*m.b791 + 1.8*m.b792 + 1.9*m.b793 + 2*m.b794
                          + 2.1*m.b795 + 2.2*m.b796 + 2.3*m.b797 + 2.4*m.b798 + 2.5*m.b799 + 2.6*m.b800 + 2.8*m.b801
                          + 3*m.b802 + 3.2*m.b803 + 3.4*m.b804 == 0)

m.c192 = Constraint(expr= - m.x24 + 0.1*m.b805 + 0.2*m.b806 + 0.3*m.b807 + 0.4*m.b808 + 0.5*m.b809 + 0.6*m.b810
                          + 0.7*m.b811 + 0.8*m.b812 + 0.9*m.b813 + m.b814 + 1.1*m.b815 + 1.2*m.b816 + 1.3*m.b817
                          + 1.4*m.b818 + 1.5*m.b819 + 1.6*m.b820 + 1.7*m.b821 + 1.8*m.b822 + 1.9*m.b823 + 2*m.b824
                          + 2.1*m.b825 + 2.2*m.b826 + 2.3*m.b827 + 2.4*m.b828 + 2.5*m.b829 + 2.6*m.b830 + 2.8*m.b831
                          + 3*m.b832 + 3.2*m.b833 + 3.4*m.b834 == 0)

m.c193 = Constraint(expr= - m.x25 + 0.1*m.b835 + 0.2*m.b836 + 0.3*m.b837 + 0.4*m.b838 + 0.5*m.b839 + 0.6*m.b840
                          + 0.7*m.b841 + 0.8*m.b842 + 0.9*m.b843 + m.b844 + 1.1*m.b845 + 1.2*m.b846 + 1.3*m.b847
                          + 1.4*m.b848 + 1.5*m.b849 + 1.6*m.b850 + 1.7*m.b851 + 1.8*m.b852 + 1.9*m.b853 + 2*m.b854
                          + 2.1*m.b855 + 2.2*m.b856 + 2.3*m.b857 + 2.4*m.b858 + 2.5*m.b859 + 2.6*m.b860 + 2.8*m.b861
                          + 3*m.b862 + 3.2*m.b863 + 3.4*m.b864 == 0)

m.c194 = Constraint(expr= - m.x26 + 0.1*m.b865 + 0.2*m.b866 + 0.3*m.b867 + 0.4*m.b868 + 0.5*m.b869 + 0.6*m.b870
                          + 0.7*m.b871 + 0.8*m.b872 + 0.9*m.b873 + m.b874 + 1.1*m.b875 + 1.2*m.b876 + 1.3*m.b877
                          + 1.4*m.b878 + 1.5*m.b879 + 1.6*m.b880 + 1.7*m.b881 + 1.8*m.b882 + 1.9*m.b883 + 2*m.b884
                          + 2.1*m.b885 + 2.2*m.b886 + 2.3*m.b887 + 2.4*m.b888 + 2.5*m.b889 + 2.6*m.b890 + 2.8*m.b891
                          + 3*m.b892 + 3.2*m.b893 + 3.4*m.b894 == 0)

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

m.c203 = Constraint(expr=   m.b385 + m.b386 + m.b387 + m.b388 + m.b389 + m.b390 + m.b391 + m.b392 + m.b393 + m.b394
                          + m.b395 + m.b396 + m.b397 + m.b398 + m.b399 + m.b400 + m.b401 + m.b402 + m.b403 + m.b404
                          + m.b405 + m.b406 + m.b407 + m.b408 + m.b409 + m.b410 + m.b411 + m.b412 + m.b413 + m.b414
                          == 1)

m.c204 = Constraint(expr=   m.b415 + m.b416 + m.b417 + m.b418 + m.b419 + m.b420 + m.b421 + m.b422 + m.b423 + m.b424
                          + m.b425 + m.b426 + m.b427 + m.b428 + m.b429 + m.b430 + m.b431 + m.b432 + m.b433 + m.b434
                          + m.b435 + m.b436 + m.b437 + m.b438 + m.b439 + m.b440 + m.b441 + m.b442 + m.b443 + m.b444
                          == 1)

m.c205 = Constraint(expr=   m.b445 + m.b446 + m.b447 + m.b448 + m.b449 + m.b450 + m.b451 + m.b452 + m.b453 + m.b454
                          + m.b455 + m.b456 + m.b457 + m.b458 + m.b459 + m.b460 + m.b461 + m.b462 + m.b463 + m.b464
                          + m.b465 + m.b466 + m.b467 + m.b468 + m.b469 + m.b470 + m.b471 + m.b472 + m.b473 + m.b474
                          == 1)

m.c206 = Constraint(expr=   m.b475 + m.b476 + m.b477 + m.b478 + m.b479 + m.b480 + m.b481 + m.b482 + m.b483 + m.b484
                          + m.b485 + m.b486 + m.b487 + m.b488 + m.b489 + m.b490 + m.b491 + m.b492 + m.b493 + m.b494
                          + m.b495 + m.b496 + m.b497 + m.b498 + m.b499 + m.b500 + m.b501 + m.b502 + m.b503 + m.b504
                          == 1)

m.c207 = Constraint(expr=   m.b505 + m.b506 + m.b507 + m.b508 + m.b509 + m.b510 + m.b511 + m.b512 + m.b513 + m.b514
                          + m.b515 + m.b516 + m.b517 + m.b518 + m.b519 + m.b520 + m.b521 + m.b522 + m.b523 + m.b524
                          + m.b525 + m.b526 + m.b527 + m.b528 + m.b529 + m.b530 + m.b531 + m.b532 + m.b533 + m.b534
                          == 1)

m.c208 = Constraint(expr=   m.b535 + m.b536 + m.b537 + m.b538 + m.b539 + m.b540 + m.b541 + m.b542 + m.b543 + m.b544
                          + m.b545 + m.b546 + m.b547 + m.b548 + m.b549 + m.b550 + m.b551 + m.b552 + m.b553 + m.b554
                          + m.b555 + m.b556 + m.b557 + m.b558 + m.b559 + m.b560 + m.b561 + m.b562 + m.b563 + m.b564
                          == 1)

m.c209 = Constraint(expr=   m.b565 + m.b566 + m.b567 + m.b568 + m.b569 + m.b570 + m.b571 + m.b572 + m.b573 + m.b574
                          + m.b575 + m.b576 + m.b577 + m.b578 + m.b579 + m.b580 + m.b581 + m.b582 + m.b583 + m.b584
                          + m.b585 + m.b586 + m.b587 + m.b588 + m.b589 + m.b590 + m.b591 + m.b592 + m.b593 + m.b594
                          == 1)

m.c210 = Constraint(expr=   m.b595 + m.b596 + m.b597 + m.b598 + m.b599 + m.b600 + m.b601 + m.b602 + m.b603 + m.b604
                          + m.b605 + m.b606 + m.b607 + m.b608 + m.b609 + m.b610 + m.b611 + m.b612 + m.b613 + m.b614
                          + m.b615 + m.b616 + m.b617 + m.b618 + m.b619 + m.b620 + m.b621 + m.b622 + m.b623 + m.b624
                          == 1)

m.c211 = Constraint(expr=   m.b625 + m.b626 + m.b627 + m.b628 + m.b629 + m.b630 + m.b631 + m.b632 + m.b633 + m.b634
                          + m.b635 + m.b636 + m.b637 + m.b638 + m.b639 + m.b640 + m.b641 + m.b642 + m.b643 + m.b644
                          + m.b645 + m.b646 + m.b647 + m.b648 + m.b649 + m.b650 + m.b651 + m.b652 + m.b653 + m.b654
                          == 1)

m.c212 = Constraint(expr=   m.b655 + m.b656 + m.b657 + m.b658 + m.b659 + m.b660 + m.b661 + m.b662 + m.b663 + m.b664
                          + m.b665 + m.b666 + m.b667 + m.b668 + m.b669 + m.b670 + m.b671 + m.b672 + m.b673 + m.b674
                          + m.b675 + m.b676 + m.b677 + m.b678 + m.b679 + m.b680 + m.b681 + m.b682 + m.b683 + m.b684
                          == 1)

m.c213 = Constraint(expr=   m.b685 + m.b686 + m.b687 + m.b688 + m.b689 + m.b690 + m.b691 + m.b692 + m.b693 + m.b694
                          + m.b695 + m.b696 + m.b697 + m.b698 + m.b699 + m.b700 + m.b701 + m.b702 + m.b703 + m.b704
                          + m.b705 + m.b706 + m.b707 + m.b708 + m.b709 + m.b710 + m.b711 + m.b712 + m.b713 + m.b714
                          == 1)

m.c214 = Constraint(expr=   m.b715 + m.b716 + m.b717 + m.b718 + m.b719 + m.b720 + m.b721 + m.b722 + m.b723 + m.b724
                          + m.b725 + m.b726 + m.b727 + m.b728 + m.b729 + m.b730 + m.b731 + m.b732 + m.b733 + m.b734
                          + m.b735 + m.b736 + m.b737 + m.b738 + m.b739 + m.b740 + m.b741 + m.b742 + m.b743 + m.b744
                          == 1)

m.c215 = Constraint(expr=   m.b745 + m.b746 + m.b747 + m.b748 + m.b749 + m.b750 + m.b751 + m.b752 + m.b753 + m.b754
                          + m.b755 + m.b756 + m.b757 + m.b758 + m.b759 + m.b760 + m.b761 + m.b762 + m.b763 + m.b764
                          + m.b765 + m.b766 + m.b767 + m.b768 + m.b769 + m.b770 + m.b771 + m.b772 + m.b773 + m.b774
                          == 1)

m.c216 = Constraint(expr=   m.b775 + m.b776 + m.b777 + m.b778 + m.b779 + m.b780 + m.b781 + m.b782 + m.b783 + m.b784
                          + m.b785 + m.b786 + m.b787 + m.b788 + m.b789 + m.b790 + m.b791 + m.b792 + m.b793 + m.b794
                          + m.b795 + m.b796 + m.b797 + m.b798 + m.b799 + m.b800 + m.b801 + m.b802 + m.b803 + m.b804
                          == 1)

m.c217 = Constraint(expr=   m.b805 + m.b806 + m.b807 + m.b808 + m.b809 + m.b810 + m.b811 + m.b812 + m.b813 + m.b814
                          + m.b815 + m.b816 + m.b817 + m.b818 + m.b819 + m.b820 + m.b821 + m.b822 + m.b823 + m.b824
                          + m.b825 + m.b826 + m.b827 + m.b828 + m.b829 + m.b830 + m.b831 + m.b832 + m.b833 + m.b834
                          == 1)

m.c218 = Constraint(expr=   m.b835 + m.b836 + m.b837 + m.b838 + m.b839 + m.b840 + m.b841 + m.b842 + m.b843 + m.b844
                          + m.b845 + m.b846 + m.b847 + m.b848 + m.b849 + m.b850 + m.b851 + m.b852 + m.b853 + m.b854
                          + m.b855 + m.b856 + m.b857 + m.b858 + m.b859 + m.b860 + m.b861 + m.b862 + m.b863 + m.b864
                          == 1)

m.c219 = Constraint(expr=   m.b865 + m.b866 + m.b867 + m.b868 + m.b869 + m.b870 + m.b871 + m.b872 + m.b873 + m.b874
                          + m.b875 + m.b876 + m.b877 + m.b878 + m.b879 + m.b880 + m.b881 + m.b882 + m.b883 + m.b884
                          + m.b885 + m.b886 + m.b887 + m.b888 + m.b889 + m.b890 + m.b891 + m.b892 + m.b893 + m.b894
                          == 1)

m.c220 = Constraint(expr= - m.x3 + m.x4 == 0)

m.c221 = Constraint(expr= - m.x3 + m.x5 == 0)

m.c222 = Constraint(expr= - m.x3 + m.x6 == 0)

m.c223 = Constraint(expr= - m.x7 + m.x8 == 0)

m.c224 = Constraint(expr= - m.x7 + m.x9 == 0)

m.c225 = Constraint(expr= - m.x7 + m.x10 == 0)

m.c226 = Constraint(expr= - m.x11 + m.x12 == 0)

m.c227 = Constraint(expr= - m.x13 + m.x14 == 0)

m.c228 = Constraint(expr= - m.x15 + m.x16 == 0)

m.c229 = Constraint(expr= - m.x15 + m.x17 == 0)

m.c230 = Constraint(expr= - m.x15 + m.x18 == 0)

m.c231 = Constraint(expr= - m.x19 + m.x20 == 0)

m.c232 = Constraint(expr= - m.x19 + m.x21 == 0)

m.c233 = Constraint(expr= - m.x19 + m.x22 == 0)

m.c234 = Constraint(expr= - m.x23 + m.x24 == 0)

m.c235 = Constraint(expr= - m.x23 + m.x25 == 0)

m.c236 = Constraint(expr= - m.x23 + m.x26 == 0)
