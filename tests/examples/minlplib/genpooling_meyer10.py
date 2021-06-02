#  MINLP written by GAMS Convert at 04/21/18 13:52:21
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        424       41      177      206        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        395      208      187        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2792     1862      930        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,47.5),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,47.5),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,47.5),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,47.5),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,47.5),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,47.5),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,47.5),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,47.5),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,47.5),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,47.5),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,28),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,28),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,28),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,28),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,28),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,28),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,28),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,28),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,28),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,28),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,47.5),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,28),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,120),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,87.5000000000001),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,2000),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,150),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,875),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,175),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,437.5),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,120),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,175),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,1600),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,1750),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,227.5),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,6.00000000000001),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,1750),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,2000),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,1080),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,2000),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,360),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,1400),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,1400),initialize=0)
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

m.obj = Objective(expr=   40.0377777777778*m.x1 + 65.0613888888889*m.x2 + 75.0708333333333*m.x3 + 100.094444444444*m.x4
                        + 120.113333333333*m.x5 + 110.103888888889*m.x6 + 150.141666666667*m.x7 + 210.198333333333*m.x8
                        + 280.264444444444*m.x9 + 245.231388888889*m.x10 + 15.0141666666667*m.x11
                        + 40.0377777777778*m.x12 + 55.0519444444444*m.x13 + 75.0708333333333*m.x14 + 90.085*m.x15
                        + 90.085*m.x16 + 125.118055555556*m.x17 + 180.17*m.x18 + 260.245555555556*m.x19
                        + 215.203055555556*m.x20 + 40.0377777777778*m.x21 + 35.0330555555556*m.x22
                        + 30.0283333333333*m.x23 + 65.0613888888889*m.x24 + 100.094444444444*m.x25
                        + 85.0802777777778*m.x26 + 115.108611111111*m.x27 + 170.160555555556*m.x28
                        + 240.226666666667*m.x29 + 220.207777777778*m.x30 + 85.0802777777778*m.x31
                        + 80.0755555555556*m.x32 + 55.0519444444444*m.x33 + 100.094444444444*m.x34
                        + 140.132222222222*m.x35 + 120.113333333333*m.x36 + 140.132222222222*m.x37 + 180.17*m.x38
                        + 245.231388888889*m.x39 + 245.231388888889*m.x40 + 95.0897222222222*m.x41
                        + 70.0661111111111*m.x42 + 55.0519444444444*m.x43 + 45.0425*m.x44 + 75.0708333333333*m.x45
                        + 45.0425*m.x46 + 40.0377777777778*m.x47 + 75.0708333333333*m.x48 + 150.141666666667*m.x49
                        + 150.141666666667*m.x50 + 80.0755555555556*m.x51 + 70.0661111111111*m.x52
                        + 40.0377777777778*m.x53 + 90.085*m.x54 + 125.118055555556*m.x55 + 100.094444444444*m.x56
                        + 120.113333333333*m.x57 + 150.141666666667*m.x58 + 230.217222222222*m.x59
                        + 230.217222222222*m.x60 + 70.0661111111111*m.x61 + 45.0425*m.x62 + 30.0283333333333*m.x63
                        + 40.0377777777778*m.x64 + 75.0708333333333*m.x65 + 50.0472222222222*m.x66
                        + 60.0566666666667*m.x67 + 100.094444444444*m.x68 + 175.165277777778*m.x69
                        + 165.155833333333*m.x70 + 3980.41333333333*m.x71 + 2990.28972222222*m.x72
                        + 1177.97083333333*m.x73 + 3945.38027777778*m.x74 + 3980.41333333333*m.x75 + 3950.385*m.x76
                        + 2975.27555555556*m.x77 + 2990.28972222222*m.x78 + 1263.05111111111*m.x79
                        + 1293.07944444444*m.x80 + 3880.31888888889*m.x81 + 3900.33777777778*m.x82
                        + 3910.34722222222*m.x83 + 3930.36611111111*m.x84 + 3930.36611111111*m.x85
                        + 3960.39444444444*m.x86 + 4020.45111111111*m.x87 + 4090.51722222222*m.x88
                        + 4050.47944444444*m.x89 + 2915.21888888889*m.x90 + 2925.22833333333*m.x91
                        + 2925.22833333333*m.x92 + 2955.25666666667*m.x93 + 2945.24722222222*m.x94
                        + 2975.27555555556*m.x95 + 3035.33222222222*m.x96 + 3110.40305555556*m.x97 + 3075.37*m.x98
                        + 1142.93777777778*m.x99 + 1132.92833333333*m.x100 + 1142.93777777778*m.x101
                        + 1182.97555555556*m.x102 + 1162.95666666667*m.x103 + 1182.97555555556*m.x104
                        + 1243.03222222222*m.x105 + 1313.09833333333*m.x106 + 1293.07944444444*m.x107
                        + 3910.34722222222*m.x108 + 3890.32833333333*m.x109 + 3900.33777777778*m.x110
                        + 3900.33777777778*m.x111 + 3875.31416666667*m.x112 + 3910.34722222222*m.x113
                        + 3970.40388888889*m.x114 + 4040.47*m.x115 + 4010.44166666667*m.x116 + 3930.36611111111*m.x117
                        + 3920.35666666667*m.x118 + 3940.37555555556*m.x119 + 3900.33777777778*m.x120
                        + 3885.32361111111*m.x121 + 3910.34722222222*m.x122 + 3970.40388888889*m.x123 + 4040.47*m.x124
                        + 3980.41333333333*m.x125 + 3930.36611111111*m.x126 + 3910.34722222222*m.x127
                        + 3920.35666666667*m.x128 + 3875.31416666667*m.x129 + 3885.32361111111*m.x130
                        + 3890.32833333333*m.x131 + 3960.39444444444*m.x132 + 4030.46055555556*m.x133
                        + 3990.42277777778*m.x134 + 2995.29444444444*m.x135 + 2975.27555555556*m.x136
                        + 2975.27555555556*m.x137 + 2945.24722222222*m.x138 + 2945.24722222222*m.x139
                        + 2925.22833333333*m.x140 + 2955.25666666667*m.x141 + 3025.32277777778*m.x142
                        + 2995.29444444444*m.x143 + 3055.35111111111*m.x144 + 3035.33222222222*m.x145
                        + 3035.33222222222*m.x146 + 3005.30388888889*m.x147 + 3005.30388888889*m.x148
                        + 2995.29444444444*m.x149 + 2955.25666666667*m.x150 + 2965.26611111111*m.x151
                        + 2995.29444444444*m.x152 + 1333.11722222222*m.x153 + 1318.10305555556*m.x154
                        + 1313.09833333333*m.x155 + 1283.07*m.x156 + 1283.07*m.x157 + 1273.06055555556*m.x158
                        + 1233.02277777778*m.x159 + 1172.96611111111*m.x160 + 1213.00388888889*m.x161
                        + 1293.07944444444*m.x162 + 1283.07*m.x163 + 1293.07944444444*m.x164 + 1253.04166666667*m.x165
                        + 1223.01333333333*m.x166 + 1233.02277777778*m.x167 + 1202.99444444444*m.x168
                        + 1202.99444444444*m.x169 + 1213.00388888889*m.x170 + 150.141666666667*m.x171 + 135.1275*m.x172
                        + 100.094444444444*m.x173 + 90.085*m.x174 + 40.0377777777778*m.x175 + 70.0661111111111*m.x176
                        + 45.0425*m.x177 + 4984*m.b208 + 8099*m.b209 + 9345*m.b210 + 12460*m.b211 + 14952*m.b212
                        + 13706*m.b213 + 18690*m.b214 + 26166*m.b215 + 34888*m.b216 + 30527*m.b217 + 1869*m.b218
                        + 4984*m.b219 + 6853*m.b220 + 9345*m.b221 + 11214*m.b222 + 11214*m.b223 + 15575*m.b224
                        + 22428*m.b225 + 32396*m.b226 + 26789*m.b227 + 4984*m.b228 + 4361*m.b229 + 3738*m.b230
                        + 8099*m.b231 + 12460*m.b232 + 10591*m.b233 + 14329*m.b234 + 21182*m.b235 + 29904*m.b236
                        + 27412*m.b237 + 10591*m.b238 + 9968*m.b239 + 6853*m.b240 + 12460*m.b241 + 17444*m.b242
                        + 14952*m.b243 + 17444*m.b244 + 22428*m.b245 + 30527*m.b246 + 30527*m.b247 + 11837*m.b248
                        + 8722*m.b249 + 6853*m.b250 + 5607*m.b251 + 9345*m.b252 + 5607*m.b253 + 4984*m.b254
                        + 9345*m.b255 + 18690*m.b256 + 18690*m.b257 + 9968*m.b258 + 8722*m.b259 + 4984*m.b260
                        + 11214*m.b261 + 15575*m.b262 + 12460*m.b263 + 14952*m.b264 + 18690*m.b265 + 28658*m.b266
                        + 28658*m.b267 + 8722*m.b268 + 5607*m.b269 + 3738*m.b270 + 4984*m.b271 + 9345*m.b272
                        + 6230*m.b273 + 7476*m.b274 + 12460*m.b275 + 21805*m.b276 + 20559*m.b277 + 14952*m.b278
                        + 11837*m.b279 + 9345*m.b280 + 10591*m.b281 + 14952*m.b282 + 11214*m.b283 + 9968*m.b284
                        + 11837*m.b285 + 19936*m.b286 + 23674*m.b287 + 2492*m.b288 + 4984*m.b289 + 6230*m.b290
                        + 8722*m.b291 + 8722*m.b292 + 12460*m.b293 + 19936*m.b294 + 28658*m.b295 + 23674*m.b296
                        + 2492*m.b297 + 3738*m.b298 + 3738*m.b299 + 7476*m.b300 + 6230*m.b301 + 9968*m.b302
                        + 17444*m.b303 + 26789*m.b304 + 22428*m.b305 + 4984*m.b306 + 3738*m.b307 + 4984*m.b308
                        + 9968*m.b309 + 7476*m.b310 + 9968*m.b311 + 17444*m.b312 + 26166*m.b313 + 23674*m.b314
                        + 6230*m.b315 + 3738*m.b316 + 4984*m.b317 + 4984*m.b318 + 1869*m.b319 + 6230*m.b320
                        + 13706*m.b321 + 22428*m.b322 + 18690*m.b323 + 8722*m.b324 + 7476*m.b325 + 9968*m.b326
                        + 4984*m.b327 + 3115*m.b328 + 6230*m.b329 + 13706*m.b330 + 22428*m.b331 + 14952*m.b332
                        + 8722*m.b333 + 6230*m.b334 + 7476*m.b335 + 1869*m.b336 + 3115*m.b337 + 3738*m.b338
                        + 12460*m.b339 + 21182*m.b340 + 16198*m.b341 + 12460*m.b342 + 9968*m.b343 + 9968*m.b344
                        + 6230*m.b345 + 6230*m.b346 + 3738*m.b347 + 7476*m.b348 + 16198*m.b349 + 12460*m.b350
                        + 19936*m.b351 + 17444*m.b352 + 17444*m.b353 + 13706*m.b354 + 13706*m.b355 + 12460*m.b356
                        + 7476*m.b357 + 8722*m.b358 + 12460*m.b359 + 28658*m.b360 + 26789*m.b361 + 26166*m.b362
                        + 22428*m.b363 + 22428*m.b364 + 21182*m.b365 + 16198*m.b366 + 8722*m.b367 + 13706*m.b368
                        + 23674*m.b369 + 22428*m.b370 + 23674*m.b371 + 18690*m.b372 + 14952*m.b373 + 16198*m.b374
                        + 12460*m.b375 + 12460*m.b376 + 13706*m.b377 + 18690*m.b378 + 16821*m.b379 + 12460*m.b380
                        + 11214*m.b381 + 4984*m.b382 + 8722*m.b383 + 5607*m.b384 + 48901*m.b385 + 36676*m.b386
                        + 13972*m.b387 + 48901*m.b388 + 48901*m.b389 + 48901*m.b390 + 36676*m.b391 + 36676*m.b392
                        + 13972*m.b393 + 13972*m.b394, sense=minimize)

m.c2 = Constraint(expr= - m.x1 - m.x2 - m.x3 - m.x4 - m.x5 - m.x6 - m.x7 - m.x8 - m.x9 - m.x10 - m.x171 <= -20)

m.c3 = Constraint(expr= - m.x11 - m.x12 - m.x13 - m.x14 - m.x15 - m.x16 - m.x17 - m.x18 - m.x19 - m.x20 - m.x172 <= -50)

m.c4 = Constraint(expr= - m.x21 - m.x22 - m.x23 - m.x24 - m.x25 - m.x26 - m.x27 - m.x28 - m.x29 - m.x30 - m.x173
                        <= -47.5)

m.c5 = Constraint(expr= - m.x31 - m.x32 - m.x33 - m.x34 - m.x35 - m.x36 - m.x37 - m.x38 - m.x39 - m.x40 - m.x174 <= -28)

m.c6 = Constraint(expr= - m.x41 - m.x42 - m.x43 - m.x44 - m.x45 - m.x46 - m.x47 - m.x48 - m.x49 - m.x50 - m.x175
                        <= -100)

m.c7 = Constraint(expr= - m.x51 - m.x52 - m.x53 - m.x54 - m.x55 - m.x56 - m.x57 - m.x58 - m.x59 - m.x60 - m.x176 <= -30)

m.c8 = Constraint(expr= - m.x61 - m.x62 - m.x63 - m.x64 - m.x65 - m.x66 - m.x67 - m.x68 - m.x69 - m.x70 - m.x177 <= -25)

m.c9 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 + m.x171 <= 20)

m.c10 = Constraint(expr=   m.x11 + m.x12 + m.x13 + m.x14 + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20 + m.x172 <= 50)

m.c11 = Constraint(expr=   m.x21 + m.x22 + m.x23 + m.x24 + m.x25 + m.x26 + m.x27 + m.x28 + m.x29 + m.x30 + m.x173
                         <= 47.5)

m.c12 = Constraint(expr=   m.x31 + m.x32 + m.x33 + m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 + m.x174 <= 28)

m.c13 = Constraint(expr=   m.x41 + m.x42 + m.x43 + m.x44 + m.x45 + m.x46 + m.x47 + m.x48 + m.x49 + m.x50 + m.x175
                         <= 100)

m.c14 = Constraint(expr=   m.x51 + m.x52 + m.x53 + m.x54 + m.x55 + m.x56 + m.x57 + m.x58 + m.x59 + m.x60 + m.x176 <= 30)

m.c15 = Constraint(expr=   m.x61 + m.x62 + m.x63 + m.x64 + m.x65 + m.x66 + m.x67 + m.x68 + m.x69 + m.x70 + m.x177 <= 25)

m.c16 = Constraint(expr=   m.x71 + m.x81 + m.x82 + m.x83 + m.x84 + m.x85 + m.x86 + m.x87 + m.x88 + m.x89 - 300.5*m.b385
                         <= 0)

m.c17 = Constraint(expr=   m.x72 + m.x90 + m.x91 + m.x92 + m.x93 + m.x94 + m.x95 + m.x96 + m.x97 + m.x98 - 300.5*m.b386
                         <= 0)

m.c18 = Constraint(expr=   m.x73 + m.x99 + m.x100 + m.x101 + m.x102 + m.x103 + m.x104 + m.x105 + m.x106 + m.x107
                         - 300.5*m.b387 <= 0)

m.c19 = Constraint(expr=   m.x74 + m.x108 + m.x109 + m.x110 + m.x111 + m.x112 + m.x113 + m.x114 + m.x115 + m.x116
                         - 300.5*m.b388 <= 0)

m.c20 = Constraint(expr=   m.x75 + m.x117 + m.x118 + m.x119 + m.x120 + m.x121 + m.x122 + m.x123 + m.x124 + m.x125
                         - 300.5*m.b389 <= 0)

m.c21 = Constraint(expr=   m.x76 + m.x126 + m.x127 + m.x128 + m.x129 + m.x130 + m.x131 + m.x132 + m.x133 + m.x134
                         - 300.5*m.b390 <= 0)

m.c22 = Constraint(expr=   m.x77 + m.x135 + m.x136 + m.x137 + m.x138 + m.x139 + m.x140 + m.x141 + m.x142 + m.x143
                         - 300.5*m.b391 <= 0)

m.c23 = Constraint(expr=   m.x78 + m.x144 + m.x145 + m.x146 + m.x147 + m.x148 + m.x149 + m.x150 + m.x151 + m.x152
                         - 300.5*m.b392 <= 0)

m.c24 = Constraint(expr=   m.x79 + m.x153 + m.x154 + m.x155 + m.x156 + m.x157 + m.x158 + m.x159 + m.x160 + m.x161
                         - 300.5*m.b393 <= 0)

m.c25 = Constraint(expr=   m.x80 + m.x162 + m.x163 + m.x164 + m.x165 + m.x166 + m.x167 + m.x168 + m.x169 + m.x170
                         - 300.5*m.b394 <= 0)

m.c26 = Constraint(expr= - m.x71 - m.x72 - m.x73 - m.x74 - m.x75 - m.x76 - m.x77 - m.x78 - m.x79 - m.x80 - m.x171
                         - m.x172 - m.x173 - m.x174 - m.x175 - m.x176 - m.x177 <= -300.5)

m.c27 = Constraint(expr=   m.x71 + m.x72 + m.x73 + m.x74 + m.x75 + m.x76 + m.x77 + m.x78 + m.x79 + m.x80 + m.x171
                         + m.x172 + m.x173 + m.x174 + m.x175 + m.x176 + m.x177 <= 300.5)

m.c28 = Constraint(expr=   m.x1 + m.x11 + m.x21 + m.x31 + m.x41 + m.x51 + m.x61 - m.x71 - m.x81 - m.x82 - m.x83 - m.x84
                         - m.x85 - m.x86 - m.x87 - m.x88 - m.x89 + m.x90 + m.x99 + m.x108 + m.x117 + m.x126 + m.x135
                         + m.x144 + m.x153 + m.x162 == 0)

m.c29 = Constraint(expr=   m.x2 + m.x12 + m.x22 + m.x32 + m.x42 + m.x52 + m.x62 - m.x72 + m.x81 - m.x90 - m.x91 - m.x92
                         - m.x93 - m.x94 - m.x95 - m.x96 - m.x97 - m.x98 + m.x100 + m.x109 + m.x118 + m.x127 + m.x136
                         + m.x145 + m.x154 + m.x163 == 0)

m.c30 = Constraint(expr=   m.x3 + m.x13 + m.x23 + m.x33 + m.x43 + m.x53 + m.x63 - m.x73 + m.x82 + m.x91 - m.x99 - m.x100
                         - m.x101 - m.x102 - m.x103 - m.x104 - m.x105 - m.x106 - m.x107 + m.x110 + m.x119 + m.x128
                         + m.x137 + m.x146 + m.x155 + m.x164 == 0)

m.c31 = Constraint(expr=   m.x4 + m.x14 + m.x24 + m.x34 + m.x44 + m.x54 + m.x64 - m.x74 + m.x83 + m.x92 + m.x101
                         - m.x108 - m.x109 - m.x110 - m.x111 - m.x112 - m.x113 - m.x114 - m.x115 - m.x116 + m.x120
                         + m.x129 + m.x138 + m.x147 + m.x156 + m.x165 == 0)

m.c32 = Constraint(expr=   m.x5 + m.x15 + m.x25 + m.x35 + m.x45 + m.x55 + m.x65 - m.x75 + m.x84 + m.x93 + m.x102
                         + m.x111 - m.x117 - m.x118 - m.x119 - m.x120 - m.x121 - m.x122 - m.x123 - m.x124 - m.x125
                         + m.x130 + m.x139 + m.x148 + m.x157 + m.x166 == 0)

m.c33 = Constraint(expr=   m.x6 + m.x16 + m.x26 + m.x36 + m.x46 + m.x56 + m.x66 - m.x76 + m.x85 + m.x94 + m.x103
                         + m.x112 + m.x121 - m.x126 - m.x127 - m.x128 - m.x129 - m.x130 - m.x131 - m.x132 - m.x133
                         - m.x134 + m.x140 + m.x149 + m.x158 + m.x167 == 0)

m.c34 = Constraint(expr=   m.x7 + m.x17 + m.x27 + m.x37 + m.x47 + m.x57 + m.x67 - m.x77 + m.x86 + m.x95 + m.x104
                         + m.x113 + m.x122 + m.x131 - m.x135 - m.x136 - m.x137 - m.x138 - m.x139 - m.x140 - m.x141
                         - m.x142 - m.x143 + m.x150 + m.x159 + m.x168 == 0)

m.c35 = Constraint(expr=   m.x8 + m.x18 + m.x28 + m.x38 + m.x48 + m.x58 + m.x68 - m.x78 + m.x87 + m.x96 + m.x105
                         + m.x114 + m.x123 + m.x132 + m.x141 - m.x144 - m.x145 - m.x146 - m.x147 - m.x148 - m.x149
                         - m.x150 - m.x151 - m.x152 + m.x160 + m.x169 == 0)

m.c36 = Constraint(expr=   m.x9 + m.x19 + m.x29 + m.x39 + m.x49 + m.x59 + m.x69 - m.x79 + m.x88 + m.x97 + m.x106
                         + m.x115 + m.x124 + m.x133 + m.x142 + m.x151 - m.x153 - m.x154 - m.x155 - m.x156 - m.x157
                         - m.x158 - m.x159 - m.x160 - m.x161 + m.x170 == 0)

m.c37 = Constraint(expr=   m.x10 + m.x20 + m.x30 + m.x40 + m.x50 + m.x60 + m.x70 - m.x80 + m.x89 + m.x98 + m.x107
                         + m.x116 + m.x125 + m.x134 + m.x143 + m.x152 + m.x161 - m.x162 - m.x163 - m.x164 - m.x165
                         - m.x166 - m.x167 - m.x168 - m.x169 - m.x170 == 0)

m.c38 = Constraint(expr=0.1*(m.x181*m.x90 + m.x184*m.x99 + m.x187*m.x108 + m.x190*m.x117 + m.x193*m.x126 + m.x196*m.x135
                         + m.x199*m.x144 + m.x202*m.x153 + m.x205*m.x162) - (m.x178*m.x71 + m.x178*m.x81 + m.x178*m.x82
                         + m.x178*m.x83 + m.x178*m.x84 + m.x178*m.x85 + m.x178*m.x86 + m.x178*m.x87 + m.x178*m.x88 + 
                        m.x178*m.x89) + 10*m.x1 + 80*m.x11 + 40*m.x21 + 120*m.x31 + 50*m.x41 + 5*m.x51 + 100*m.x61 == 0)

m.c39 = Constraint(expr=0.05*(m.x182*m.x90 + m.x185*m.x99 + m.x188*m.x108 + m.x191*m.x117 + m.x194*m.x126 + m.x197*
                        m.x135 + m.x200*m.x144 + m.x203*m.x153 + m.x206*m.x162) - (m.x179*m.x71 + m.x179*m.x81 + m.x179*
                        m.x82 + m.x179*m.x83 + m.x179*m.x84 + m.x179*m.x85 + m.x179*m.x86 + m.x179*m.x87 + m.x179*m.x88
                         + m.x179*m.x89) + 25*m.x1 + 87.5000000000001*m.x11 + 4*m.x21 + 50*m.x31 + 35*m.x41 + 5*m.x51
                         + 2.5*m.x61 == 0)

m.c40 = Constraint(expr=m.x183*m.x90 + m.x186*m.x99 + m.x189*m.x108 + m.x192*m.x117 + m.x195*m.x126 + m.x198*m.x135 + 
                        m.x201*m.x144 + m.x204*m.x153 + m.x207*m.x162 - (m.x180*m.x71 + m.x180*m.x81 + m.x180*m.x82 + 
                        m.x180*m.x83 + m.x180*m.x84 + m.x180*m.x85 + m.x180*m.x86 + m.x180*m.x87 + m.x180*m.x88 + m.x180
                        *m.x89) + 500*m.x1 + 2000*m.x11 + 100*m.x21 + 400*m.x31 + 250*m.x41 + 50*m.x51 + 150*m.x61 == 0)

m.c41 = Constraint(expr=0.125*(m.x178*m.x81 + m.x184*m.x100 + m.x187*m.x109 + m.x190*m.x118 + m.x193*m.x127 + m.x196*
                        m.x136 + m.x199*m.x145 + m.x202*m.x154 + m.x205*m.x163) - (m.x181*m.x72 + m.x181*m.x90 + m.x181*
                        m.x91 + m.x181*m.x92 + m.x181*m.x93 + m.x181*m.x94 + m.x181*m.x95 + m.x181*m.x96 + m.x181*m.x97
                         + m.x181*m.x98) + 12.5*m.x2 + 100*m.x12 + 50*m.x22 + 150*m.x32 + 62.5*m.x42 + 6.25*m.x52
                         + 125*m.x62 == 0)

m.c42 = Constraint(expr=0.5*(m.x179*m.x81 + m.x185*m.x100 + m.x188*m.x109 + m.x191*m.x118 + m.x194*m.x127 + m.x197*
                        m.x136 + m.x200*m.x145 + m.x203*m.x154 + m.x206*m.x163) - (m.x182*m.x72 + m.x182*m.x90 + m.x182*
                        m.x91 + m.x182*m.x92 + m.x182*m.x93 + m.x182*m.x94 + m.x182*m.x95 + m.x182*m.x96 + m.x182*m.x97
                         + m.x182*m.x98) + 250*m.x2 + 875*m.x12 + 40*m.x22 + 500*m.x32 + 350*m.x42 + 50*m.x52 + 25*m.x62
                         == 0)

m.c43 = Constraint(expr=0.5*(m.x180*m.x81 + m.x186*m.x100 + m.x189*m.x109 + m.x192*m.x118 + m.x195*m.x127 + m.x198*
                        m.x136 + m.x201*m.x145 + m.x204*m.x154 + m.x207*m.x163) - (m.x183*m.x72 + m.x183*m.x90 + m.x183*
                        m.x91 + m.x183*m.x92 + m.x183*m.x93 + m.x183*m.x94 + m.x183*m.x95 + m.x183*m.x96 + m.x183*m.x97
                         + m.x183*m.x98) + 250*m.x2 + 1000*m.x12 + 50*m.x22 + 200*m.x32 + 125*m.x42 + 25*m.x52
                         + 75*m.x62 == 0)

m.c44 = Constraint(expr=0.01*(m.x178*m.x82 + m.x181*m.x91 + m.x187*m.x110 + m.x190*m.x119 + m.x193*m.x128 + m.x196*
                        m.x137 + m.x199*m.x146 + m.x202*m.x155 + m.x205*m.x164) - (m.x184*m.x73 + m.x184*m.x99 + m.x184*
                        m.x100 + m.x184*m.x101 + m.x184*m.x102 + m.x184*m.x103 + m.x184*m.x104 + m.x184*m.x105 + m.x184*
                        m.x106 + m.x184*m.x107) + m.x3 + 8.00000000000001*m.x13 + 4*m.x23 + 12*m.x33 + 5*m.x43
                         + 0.5*m.x53 + 10*m.x63 == 0)

m.c45 = Constraint(expr=0.1*(m.x179*m.x82 + m.x182*m.x91 + m.x188*m.x110 + m.x191*m.x119 + m.x194*m.x128 + m.x197*m.x137
                         + m.x200*m.x146 + m.x203*m.x155 + m.x206*m.x164) - (m.x185*m.x73 + m.x185*m.x99 + m.x185*m.x100
                         + m.x185*m.x101 + m.x185*m.x102 + m.x185*m.x103 + m.x185*m.x104 + m.x185*m.x105 + m.x185*m.x106
                         + m.x185*m.x107) + 50*m.x3 + 175*m.x13 + 8*m.x23 + 100*m.x33 + 70*m.x43 + 10*m.x53 + 5*m.x63
                         == 0)

m.c46 = Constraint(expr=0.05*(m.x180*m.x82 + m.x183*m.x91 + m.x189*m.x110 + m.x192*m.x119 + m.x195*m.x128 + m.x198*
                        m.x137 + m.x201*m.x146 + m.x204*m.x155 + m.x207*m.x164) - (m.x186*m.x73 + m.x186*m.x99 + m.x186*
                        m.x100 + m.x186*m.x101 + m.x186*m.x102 + m.x186*m.x103 + m.x186*m.x104 + m.x186*m.x105 + m.x186*
                        m.x106 + m.x186*m.x107) + 25*m.x3 + 100*m.x13 + 5*m.x23 + 20*m.x33 + 12.5*m.x43 + 2.5*m.x53
                         + 7.50000000000001*m.x63 == 0)

m.c47 = Constraint(expr=m.x178*m.x83 + m.x181*m.x92 + m.x184*m.x101 + m.x190*m.x120 + m.x193*m.x129 + m.x196*m.x138 + 
                        m.x199*m.x147 + m.x202*m.x156 + m.x205*m.x165 - (m.x187*m.x74 + m.x187*m.x108 + m.x187*m.x109 + 
                        m.x187*m.x110 + m.x187*m.x111 + m.x187*m.x112 + m.x187*m.x113 + m.x187*m.x114 + m.x187*m.x115 + 
                        m.x187*m.x116) + 100*m.x4 + 800*m.x14 + 400*m.x24 + 1200*m.x34 + 500*m.x44 + 50*m.x54
                         + 1000*m.x64 == 0)

m.c48 = Constraint(expr=0.25*(m.x179*m.x83 + m.x182*m.x92 + m.x185*m.x101 + m.x191*m.x120 + m.x194*m.x129 + m.x197*
                        m.x138 + m.x200*m.x147 + m.x203*m.x156 + m.x206*m.x165) - (m.x188*m.x74 + m.x188*m.x108 + m.x188
                        *m.x109 + m.x188*m.x110 + m.x188*m.x111 + m.x188*m.x112 + m.x188*m.x113 + m.x188*m.x114 + m.x188
                        *m.x115 + m.x188*m.x116) + 125*m.x4 + 437.5*m.x14 + 20*m.x24 + 250*m.x34 + 175*m.x44 + 25*m.x54
                         + 12.5*m.x64 == 0)

m.c49 = Constraint(expr=0.25*(m.x180*m.x83 + m.x183*m.x92 + m.x186*m.x101 + m.x192*m.x120 + m.x195*m.x129 + m.x198*
                        m.x138 + m.x201*m.x147 + m.x204*m.x156 + m.x207*m.x165) - (m.x189*m.x74 + m.x189*m.x108 + m.x189
                        *m.x109 + m.x189*m.x110 + m.x189*m.x111 + m.x189*m.x112 + m.x189*m.x113 + m.x189*m.x114 + m.x189
                        *m.x115 + m.x189*m.x116) + 125*m.x4 + 500*m.x14 + 25*m.x24 + 100*m.x34 + 62.5*m.x44 + 12.5*m.x54
                         + 37.5*m.x64 == 0)

m.c50 = Constraint(expr=0.1*(m.x178*m.x84 + m.x181*m.x93 + m.x184*m.x102 + m.x187*m.x111 + m.x193*m.x130 + m.x196*m.x139
                         + m.x199*m.x148 + m.x202*m.x157 + m.x205*m.x166) - (m.x190*m.x75 + m.x190*m.x117 + m.x190*
                        m.x118 + m.x190*m.x119 + m.x190*m.x120 + m.x190*m.x121 + m.x190*m.x122 + m.x190*m.x123 + m.x190*
                        m.x124 + m.x190*m.x125) + 10*m.x5 + 80*m.x15 + 40*m.x25 + 120*m.x35 + 50*m.x45 + 5*m.x55
                         + 100*m.x65 == 0)

m.c51 = Constraint(expr=0.1*(m.x179*m.x84 + m.x182*m.x93 + m.x185*m.x102 + m.x188*m.x111 + m.x194*m.x130 + m.x197*m.x139
                         + m.x200*m.x148 + m.x203*m.x157 + m.x206*m.x166) - (m.x191*m.x75 + m.x191*m.x117 + m.x191*
                        m.x118 + m.x191*m.x119 + m.x191*m.x120 + m.x191*m.x121 + m.x191*m.x122 + m.x191*m.x123 + m.x191*
                        m.x124 + m.x191*m.x125) + 50*m.x5 + 175*m.x15 + 8*m.x25 + 100*m.x35 + 70*m.x45 + 10*m.x55
                         + 5*m.x65 == 0)

m.c52 = Constraint(expr=0.8*(m.x180*m.x84 + m.x183*m.x93 + m.x186*m.x102 + m.x189*m.x111 + m.x195*m.x130 + m.x198*m.x139
                         + m.x201*m.x148 + m.x204*m.x157 + m.x207*m.x166) - (m.x192*m.x75 + m.x192*m.x117 + m.x192*
                        m.x118 + m.x192*m.x119 + m.x192*m.x120 + m.x192*m.x121 + m.x192*m.x122 + m.x192*m.x123 + m.x192*
                        m.x124 + m.x192*m.x125) + 400*m.x5 + 1600*m.x15 + 80*m.x25 + 320*m.x35 + 200*m.x45 + 40*m.x55
                         + 120*m.x65 == 0)

m.c53 = Constraint(expr=m.x178*m.x85 + m.x181*m.x94 + m.x184*m.x103 + m.x187*m.x112 + m.x190*m.x121 + m.x196*m.x140 + 
                        m.x199*m.x149 + m.x202*m.x158 + m.x205*m.x167 - (m.x193*m.x76 + m.x193*m.x126 + m.x193*m.x127 + 
                        m.x193*m.x128 + m.x193*m.x129 + m.x193*m.x130 + m.x193*m.x131 + m.x193*m.x132 + m.x193*m.x133 + 
                        m.x193*m.x134) + 100*m.x6 + 800*m.x16 + 400*m.x26 + 1200*m.x36 + 500*m.x46 + 50*m.x56
                         + 1000*m.x66 == 0)

m.c54 = Constraint(expr=m.x179*m.x85 + m.x182*m.x94 + m.x185*m.x103 + m.x188*m.x112 + m.x191*m.x121 + m.x197*m.x140 + 
                        m.x200*m.x149 + m.x203*m.x158 + m.x206*m.x167 - (m.x194*m.x76 + m.x194*m.x126 + m.x194*m.x127 + 
                        m.x194*m.x128 + m.x194*m.x129 + m.x194*m.x130 + m.x194*m.x131 + m.x194*m.x132 + m.x194*m.x133 + 
                        m.x194*m.x134) + 500*m.x6 + 1750*m.x16 + 80*m.x26 + 1000*m.x36 + 700*m.x46 + 100*m.x56
                         + 50*m.x66 == 0)

m.c55 = Constraint(expr=0.05*(m.x180*m.x85 + m.x183*m.x94 + m.x186*m.x103 + m.x189*m.x112 + m.x192*m.x121 + m.x198*
                        m.x140 + m.x201*m.x149 + m.x204*m.x158 + m.x207*m.x167) - (m.x195*m.x76 + m.x195*m.x126 + m.x195
                        *m.x127 + m.x195*m.x128 + m.x195*m.x129 + m.x195*m.x130 + m.x195*m.x131 + m.x195*m.x132 + m.x195
                        *m.x133 + m.x195*m.x134) + 25*m.x6 + 100*m.x16 + 5*m.x26 + 20*m.x36 + 12.5*m.x46 + 2.5*m.x56
                         + 7.50000000000001*m.x66 == 0)

m.c56 = Constraint(expr=m.x178*m.x86 + m.x181*m.x95 + m.x184*m.x104 + m.x187*m.x113 + m.x190*m.x122 + m.x193*m.x131 + 
                        m.x199*m.x150 + m.x202*m.x159 + m.x205*m.x168 - (m.x196*m.x77 + m.x196*m.x135 + m.x196*m.x136 + 
                        m.x196*m.x137 + m.x196*m.x138 + m.x196*m.x139 + m.x196*m.x140 + m.x196*m.x141 + m.x196*m.x142 + 
                        m.x196*m.x143) + 100*m.x7 + 800*m.x17 + 400*m.x27 + 1200*m.x37 + 500*m.x47 + 50*m.x57
                         + 1000*m.x67 == 0)

m.c57 = Constraint(expr=0.13*(m.x179*m.x86 + m.x182*m.x95 + m.x185*m.x104 + m.x188*m.x113 + m.x191*m.x122 + m.x194*
                        m.x131 + m.x200*m.x150 + m.x203*m.x159 + m.x206*m.x168) - (m.x197*m.x77 + m.x197*m.x135 + m.x197
                        *m.x136 + m.x197*m.x137 + m.x197*m.x138 + m.x197*m.x139 + m.x197*m.x140 + m.x197*m.x141 + m.x197
                        *m.x142 + m.x197*m.x143) + 65*m.x7 + 227.5*m.x17 + 10.4*m.x27 + 130*m.x37 + 91*m.x47 + 13*m.x57
                         + 6.5*m.x67 == 0)

m.c58 = Constraint(expr=0.1*(m.x180*m.x86 + m.x183*m.x95 + m.x186*m.x104 + m.x189*m.x113 + m.x192*m.x122 + m.x195*m.x131
                         + m.x201*m.x150 + m.x204*m.x159 + m.x207*m.x168) - (m.x198*m.x77 + m.x198*m.x135 + m.x198*
                        m.x136 + m.x198*m.x137 + m.x198*m.x138 + m.x198*m.x139 + m.x198*m.x140 + m.x198*m.x141 + m.x198*
                        m.x142 + m.x198*m.x143) + 50*m.x7 + 200*m.x17 + 10*m.x27 + 40*m.x37 + 25*m.x47 + 5*m.x57
                         + 15*m.x67 == 0)

m.c59 = Constraint(expr=0.005*(m.x178*m.x87 + m.x181*m.x96 + m.x184*m.x105 + m.x187*m.x114 + m.x190*m.x123 + m.x193*
                        m.x132 + m.x196*m.x141 + m.x202*m.x160 + m.x205*m.x169) - (m.x199*m.x78 + m.x199*m.x144 + m.x199
                        *m.x145 + m.x199*m.x146 + m.x199*m.x147 + m.x199*m.x148 + m.x199*m.x149 + m.x199*m.x150 + m.x199
                        *m.x151 + m.x199*m.x152) + 0.5*m.x8 + 4*m.x18 + 2*m.x28 + 6.00000000000001*m.x38 + 2.5*m.x48
                         + 0.25*m.x58 + 5*m.x68 == 0)

m.c60 = Constraint(expr=m.x179*m.x87 + m.x182*m.x96 + m.x185*m.x105 + m.x188*m.x114 + m.x191*m.x123 + m.x194*m.x132 + 
                        m.x197*m.x141 + m.x203*m.x160 + m.x206*m.x169 - (m.x200*m.x78 + m.x200*m.x144 + m.x200*m.x145 + 
                        m.x200*m.x146 + m.x200*m.x147 + m.x200*m.x148 + m.x200*m.x149 + m.x200*m.x150 + m.x200*m.x151 + 
                        m.x200*m.x152) + 500*m.x8 + 1750*m.x18 + 80*m.x28 + 1000*m.x38 + 700*m.x48 + 100*m.x58
                         + 50*m.x68 == 0)

m.c61 = Constraint(expr=m.x180*m.x87 + m.x183*m.x96 + m.x186*m.x105 + m.x189*m.x114 + m.x192*m.x123 + m.x195*m.x132 + 
                        m.x198*m.x141 + m.x204*m.x160 + m.x207*m.x169 - (m.x201*m.x78 + m.x201*m.x144 + m.x201*m.x145 + 
                        m.x201*m.x146 + m.x201*m.x147 + m.x201*m.x148 + m.x201*m.x149 + m.x201*m.x150 + m.x201*m.x151 + 
                        m.x201*m.x152) + 500*m.x8 + 2000*m.x18 + 100*m.x28 + 400*m.x38 + 250*m.x48 + 50*m.x58
                         + 150*m.x68 == 0)

m.c62 = Constraint(expr=0.9*(m.x178*m.x88 + m.x181*m.x97 + m.x184*m.x106 + m.x187*m.x115 + m.x190*m.x124 + m.x193*m.x133
                         + m.x196*m.x142 + m.x199*m.x151 + m.x205*m.x170) - (m.x202*m.x79 + m.x202*m.x153 + m.x202*
                        m.x154 + m.x202*m.x155 + m.x202*m.x156 + m.x202*m.x157 + m.x202*m.x158 + m.x202*m.x159 + m.x202*
                        m.x160 + m.x202*m.x161) + 90*m.x9 + 720*m.x19 + 360*m.x29 + 1080*m.x39 + 450*m.x49 + 45*m.x59
                         + 900*m.x69 == 0)

m.c63 = Constraint(expr=0.01*(m.x179*m.x88 + m.x182*m.x97 + m.x185*m.x106 + m.x188*m.x115 + m.x191*m.x124 + m.x194*
                        m.x133 + m.x197*m.x142 + m.x200*m.x151 + m.x206*m.x170) - (m.x203*m.x79 + m.x203*m.x153 + m.x203
                        *m.x154 + m.x203*m.x155 + m.x203*m.x156 + m.x203*m.x157 + m.x203*m.x158 + m.x203*m.x159 + m.x203
                        *m.x160 + m.x203*m.x161) + 5*m.x9 + 17.5*m.x19 + 0.800000000000001*m.x29 + 10*m.x39
                         + 7.00000000000001*m.x49 + m.x59 + 0.5*m.x69 == 0)

m.c64 = Constraint(expr=m.x180*m.x88 + m.x183*m.x97 + m.x186*m.x106 + m.x189*m.x115 + m.x192*m.x124 + m.x195*m.x133 + 
                        m.x198*m.x142 + m.x201*m.x151 + m.x207*m.x170 - (m.x204*m.x79 + m.x204*m.x153 + m.x204*m.x154 + 
                        m.x204*m.x155 + m.x204*m.x156 + m.x204*m.x157 + m.x204*m.x158 + m.x204*m.x159 + m.x204*m.x160 + 
                        m.x204*m.x161) + 500*m.x9 + 2000*m.x19 + 100*m.x29 + 400*m.x39 + 250*m.x49 + 50*m.x59
                         + 150*m.x69 == 0)

m.c65 = Constraint(expr=0.3*(m.x178*m.x89 + m.x181*m.x98 + m.x184*m.x107 + m.x187*m.x116 + m.x190*m.x125 + m.x193*m.x134
                         + m.x196*m.x143 + m.x199*m.x152 + m.x202*m.x161) - (m.x205*m.x80 + m.x205*m.x162 + m.x205*
                        m.x163 + m.x205*m.x164 + m.x205*m.x165 + m.x205*m.x166 + m.x205*m.x167 + m.x205*m.x168 + m.x205*
                        m.x169 + m.x205*m.x170) + 30*m.x10 + 240*m.x20 + 120*m.x30 + 360*m.x40 + 150*m.x50 + 15*m.x60
                         + 300*m.x70 == 0)

m.c66 = Constraint(expr=0.8*(m.x179*m.x89 + m.x182*m.x98 + m.x185*m.x107 + m.x188*m.x116 + m.x191*m.x125 + m.x194*m.x134
                         + m.x197*m.x143 + m.x200*m.x152 + m.x203*m.x161) - (m.x206*m.x80 + m.x206*m.x162 + m.x206*
                        m.x163 + m.x206*m.x164 + m.x206*m.x165 + m.x206*m.x166 + m.x206*m.x167 + m.x206*m.x168 + m.x206*
                        m.x169 + m.x206*m.x170) + 400*m.x10 + 1400*m.x20 + 64*m.x30 + 800*m.x40 + 560*m.x50 + 80*m.x60
                         + 40*m.x70 == 0)

m.c67 = Constraint(expr=0.7*(m.x180*m.x89 + m.x183*m.x98 + m.x186*m.x107 + m.x189*m.x116 + m.x192*m.x125 + m.x195*m.x134
                         + m.x198*m.x143 + m.x201*m.x152 + m.x204*m.x161) - (m.x207*m.x80 + m.x207*m.x162 + m.x207*
                        m.x163 + m.x207*m.x164 + m.x207*m.x165 + m.x207*m.x166 + m.x207*m.x167 + m.x207*m.x168 + m.x207*
                        m.x169 + m.x207*m.x170) + 350*m.x10 + 1400*m.x20 + 70*m.x30 + 280*m.x40 + 175*m.x50 + 35*m.x60
                         + 105*m.x70 == 0)

m.c68 = Constraint(expr=m.x178*m.x71 + m.x181*m.x72 + m.x184*m.x73 + m.x187*m.x74 + m.x190*m.x75 + m.x193*m.x76 + m.x196
                        *m.x77 + m.x199*m.x78 + m.x202*m.x79 + m.x205*m.x80 - 5*m.x71 - 5*m.x72 - 5*m.x73 - 5*m.x74 - 5*
                        m.x75 - 5*m.x76 - 5*m.x77 - 5*m.x78 - 5*m.x79 - 5*m.x80 + 95*m.x171 + 795*m.x172 + 395*m.x173
                         + 1195*m.x174 + 495*m.x175 + 45*m.x176 + 995*m.x177 <= 0)

m.c69 = Constraint(expr=m.x179*m.x71 + m.x182*m.x72 + m.x185*m.x73 + m.x188*m.x74 + m.x191*m.x75 + m.x194*m.x76 + m.x197
                        *m.x77 + m.x200*m.x78 + m.x203*m.x79 + m.x206*m.x80 - 5*m.x71 - 5*m.x72 - 5*m.x73 - 5*m.x74 - 5*
                        m.x75 - 5*m.x76 - 5*m.x77 - 5*m.x78 - 5*m.x79 - 5*m.x80 + 495*m.x171 + 1745*m.x172 + 75*m.x173
                         + 995*m.x174 + 695*m.x175 + 95*m.x176 + 45*m.x177 <= 0)

m.c70 = Constraint(expr=m.x180*m.x71 + m.x183*m.x72 + m.x186*m.x73 + m.x189*m.x74 + m.x192*m.x75 + m.x195*m.x76 + m.x198
                        *m.x77 + m.x201*m.x78 + m.x204*m.x79 + m.x207*m.x80 - 10*m.x71 - 10*m.x72 - 10*m.x73 - 10*m.x74
                         - 10*m.x75 - 10*m.x76 - 10*m.x77 - 10*m.x78 - 10*m.x79 - 10*m.x80 + 490*m.x171 + 1990*m.x172
                         + 90*m.x173 + 390*m.x174 + 240*m.x175 + 40*m.x176 + 140*m.x177 <= 0)

m.c71 = Constraint(expr=   m.x1 - 0.2*m.b208 >= 0)

m.c72 = Constraint(expr=   m.x2 - 0.2*m.b209 >= 0)

m.c73 = Constraint(expr=   m.x3 - 0.2*m.b210 >= 0)

m.c74 = Constraint(expr=   m.x4 - 0.2*m.b211 >= 0)

m.c75 = Constraint(expr=   m.x5 - 0.2*m.b212 >= 0)

m.c76 = Constraint(expr=   m.x6 - 0.2*m.b213 >= 0)

m.c77 = Constraint(expr=   m.x7 - 0.2*m.b214 >= 0)

m.c78 = Constraint(expr=   m.x8 - 0.2*m.b215 >= 0)

m.c79 = Constraint(expr=   m.x9 - 0.2*m.b216 >= 0)

m.c80 = Constraint(expr=   m.x10 - 0.2*m.b217 >= 0)

m.c81 = Constraint(expr=   m.x11 - 0.2*m.b218 >= 0)

m.c82 = Constraint(expr=   m.x12 - 0.2*m.b219 >= 0)

m.c83 = Constraint(expr=   m.x13 - 0.2*m.b220 >= 0)

m.c84 = Constraint(expr=   m.x14 - 0.2*m.b221 >= 0)

m.c85 = Constraint(expr=   m.x15 - 0.2*m.b222 >= 0)

m.c86 = Constraint(expr=   m.x16 - 0.2*m.b223 >= 0)

m.c87 = Constraint(expr=   m.x17 - 0.2*m.b224 >= 0)

m.c88 = Constraint(expr=   m.x18 - 0.2*m.b225 >= 0)

m.c89 = Constraint(expr=   m.x19 - 0.2*m.b226 >= 0)

m.c90 = Constraint(expr=   m.x20 - 0.2*m.b227 >= 0)

m.c91 = Constraint(expr=   m.x21 - 0.2*m.b228 >= 0)

m.c92 = Constraint(expr=   m.x22 - 0.2*m.b229 >= 0)

m.c93 = Constraint(expr=   m.x23 - 0.2*m.b230 >= 0)

m.c94 = Constraint(expr=   m.x24 - 0.2*m.b231 >= 0)

m.c95 = Constraint(expr=   m.x25 - 0.2*m.b232 >= 0)

m.c96 = Constraint(expr=   m.x26 - 0.2*m.b233 >= 0)

m.c97 = Constraint(expr=   m.x27 - 0.2*m.b234 >= 0)

m.c98 = Constraint(expr=   m.x28 - 0.2*m.b235 >= 0)

m.c99 = Constraint(expr=   m.x29 - 0.2*m.b236 >= 0)

m.c100 = Constraint(expr=   m.x30 - 0.2*m.b237 >= 0)

m.c101 = Constraint(expr=   m.x31 - 0.2*m.b238 >= 0)

m.c102 = Constraint(expr=   m.x32 - 0.2*m.b239 >= 0)

m.c103 = Constraint(expr=   m.x33 - 0.2*m.b240 >= 0)

m.c104 = Constraint(expr=   m.x34 - 0.2*m.b241 >= 0)

m.c105 = Constraint(expr=   m.x35 - 0.2*m.b242 >= 0)

m.c106 = Constraint(expr=   m.x36 - 0.2*m.b243 >= 0)

m.c107 = Constraint(expr=   m.x37 - 0.2*m.b244 >= 0)

m.c108 = Constraint(expr=   m.x38 - 0.2*m.b245 >= 0)

m.c109 = Constraint(expr=   m.x39 - 0.2*m.b246 >= 0)

m.c110 = Constraint(expr=   m.x40 - 0.2*m.b247 >= 0)

m.c111 = Constraint(expr=   m.x41 - 0.2*m.b248 >= 0)

m.c112 = Constraint(expr=   m.x42 - 0.2*m.b249 >= 0)

m.c113 = Constraint(expr=   m.x43 - 0.2*m.b250 >= 0)

m.c114 = Constraint(expr=   m.x44 - 0.2*m.b251 >= 0)

m.c115 = Constraint(expr=   m.x45 - 0.2*m.b252 >= 0)

m.c116 = Constraint(expr=   m.x46 - 0.2*m.b253 >= 0)

m.c117 = Constraint(expr=   m.x47 - 0.2*m.b254 >= 0)

m.c118 = Constraint(expr=   m.x48 - 0.2*m.b255 >= 0)

m.c119 = Constraint(expr=   m.x49 - 0.2*m.b256 >= 0)

m.c120 = Constraint(expr=   m.x50 - 0.2*m.b257 >= 0)

m.c121 = Constraint(expr=   m.x51 - 0.2*m.b258 >= 0)

m.c122 = Constraint(expr=   m.x52 - 0.2*m.b259 >= 0)

m.c123 = Constraint(expr=   m.x53 - 0.2*m.b260 >= 0)

m.c124 = Constraint(expr=   m.x54 - 0.2*m.b261 >= 0)

m.c125 = Constraint(expr=   m.x55 - 0.2*m.b262 >= 0)

m.c126 = Constraint(expr=   m.x56 - 0.2*m.b263 >= 0)

m.c127 = Constraint(expr=   m.x57 - 0.2*m.b264 >= 0)

m.c128 = Constraint(expr=   m.x58 - 0.2*m.b265 >= 0)

m.c129 = Constraint(expr=   m.x59 - 0.2*m.b266 >= 0)

m.c130 = Constraint(expr=   m.x60 - 0.2*m.b267 >= 0)

m.c131 = Constraint(expr=   m.x61 - 0.2*m.b268 >= 0)

m.c132 = Constraint(expr=   m.x62 - 0.2*m.b269 >= 0)

m.c133 = Constraint(expr=   m.x63 - 0.2*m.b270 >= 0)

m.c134 = Constraint(expr=   m.x64 - 0.2*m.b271 >= 0)

m.c135 = Constraint(expr=   m.x65 - 0.2*m.b272 >= 0)

m.c136 = Constraint(expr=   m.x66 - 0.2*m.b273 >= 0)

m.c137 = Constraint(expr=   m.x67 - 0.2*m.b274 >= 0)

m.c138 = Constraint(expr=   m.x68 - 0.2*m.b275 >= 0)

m.c139 = Constraint(expr=   m.x69 - 0.2*m.b276 >= 0)

m.c140 = Constraint(expr=   m.x70 - 0.2*m.b277 >= 0)

m.c141 = Constraint(expr=   m.x1 - 20*m.b208 <= 0)

m.c142 = Constraint(expr=   m.x2 - 20*m.b209 <= 0)

m.c143 = Constraint(expr=   m.x3 - 20*m.b210 <= 0)

m.c144 = Constraint(expr=   m.x4 - 20*m.b211 <= 0)

m.c145 = Constraint(expr=   m.x5 - 20*m.b212 <= 0)

m.c146 = Constraint(expr=   m.x6 - 20*m.b213 <= 0)

m.c147 = Constraint(expr=   m.x7 - 20*m.b214 <= 0)

m.c148 = Constraint(expr=   m.x8 - 20*m.b215 <= 0)

m.c149 = Constraint(expr=   m.x9 - 20*m.b216 <= 0)

m.c150 = Constraint(expr=   m.x10 - 20*m.b217 <= 0)

m.c151 = Constraint(expr=   m.x11 - 50*m.b218 <= 0)

m.c152 = Constraint(expr=   m.x12 - 50*m.b219 <= 0)

m.c153 = Constraint(expr=   m.x13 - 50*m.b220 <= 0)

m.c154 = Constraint(expr=   m.x14 - 50*m.b221 <= 0)

m.c155 = Constraint(expr=   m.x15 - 50*m.b222 <= 0)

m.c156 = Constraint(expr=   m.x16 - 50*m.b223 <= 0)

m.c157 = Constraint(expr=   m.x17 - 50*m.b224 <= 0)

m.c158 = Constraint(expr=   m.x18 - 50*m.b225 <= 0)

m.c159 = Constraint(expr=   m.x19 - 50*m.b226 <= 0)

m.c160 = Constraint(expr=   m.x20 - 50*m.b227 <= 0)

m.c161 = Constraint(expr=   m.x21 - 47.5*m.b228 <= 0)

m.c162 = Constraint(expr=   m.x22 - 47.5*m.b229 <= 0)

m.c163 = Constraint(expr=   m.x23 - 47.5*m.b230 <= 0)

m.c164 = Constraint(expr=   m.x24 - 47.5*m.b231 <= 0)

m.c165 = Constraint(expr=   m.x25 - 47.5*m.b232 <= 0)

m.c166 = Constraint(expr=   m.x26 - 47.5*m.b233 <= 0)

m.c167 = Constraint(expr=   m.x27 - 47.5*m.b234 <= 0)

m.c168 = Constraint(expr=   m.x28 - 47.5*m.b235 <= 0)

m.c169 = Constraint(expr=   m.x29 - 47.5*m.b236 <= 0)

m.c170 = Constraint(expr=   m.x30 - 47.5*m.b237 <= 0)

m.c171 = Constraint(expr=   m.x31 - 28*m.b238 <= 0)

m.c172 = Constraint(expr=   m.x32 - 28*m.b239 <= 0)

m.c173 = Constraint(expr=   m.x33 - 28*m.b240 <= 0)

m.c174 = Constraint(expr=   m.x34 - 28*m.b241 <= 0)

m.c175 = Constraint(expr=   m.x35 - 28*m.b242 <= 0)

m.c176 = Constraint(expr=   m.x36 - 28*m.b243 <= 0)

m.c177 = Constraint(expr=   m.x37 - 28*m.b244 <= 0)

m.c178 = Constraint(expr=   m.x38 - 28*m.b245 <= 0)

m.c179 = Constraint(expr=   m.x39 - 28*m.b246 <= 0)

m.c180 = Constraint(expr=   m.x40 - 28*m.b247 <= 0)

m.c181 = Constraint(expr=   m.x41 - 100*m.b248 <= 0)

m.c182 = Constraint(expr=   m.x42 - 100*m.b249 <= 0)

m.c183 = Constraint(expr=   m.x43 - 100*m.b250 <= 0)

m.c184 = Constraint(expr=   m.x44 - 100*m.b251 <= 0)

m.c185 = Constraint(expr=   m.x45 - 100*m.b252 <= 0)

m.c186 = Constraint(expr=   m.x46 - 100*m.b253 <= 0)

m.c187 = Constraint(expr=   m.x47 - 100*m.b254 <= 0)

m.c188 = Constraint(expr=   m.x48 - 100*m.b255 <= 0)

m.c189 = Constraint(expr=   m.x49 - 100*m.b256 <= 0)

m.c190 = Constraint(expr=   m.x50 - 100*m.b257 <= 0)

m.c191 = Constraint(expr=   m.x51 - 30*m.b258 <= 0)

m.c192 = Constraint(expr=   m.x52 - 30*m.b259 <= 0)

m.c193 = Constraint(expr=   m.x53 - 30*m.b260 <= 0)

m.c194 = Constraint(expr=   m.x54 - 30*m.b261 <= 0)

m.c195 = Constraint(expr=   m.x55 - 30*m.b262 <= 0)

m.c196 = Constraint(expr=   m.x56 - 30*m.b263 <= 0)

m.c197 = Constraint(expr=   m.x57 - 30*m.b264 <= 0)

m.c198 = Constraint(expr=   m.x58 - 30*m.b265 <= 0)

m.c199 = Constraint(expr=   m.x59 - 30*m.b266 <= 0)

m.c200 = Constraint(expr=   m.x60 - 30*m.b267 <= 0)

m.c201 = Constraint(expr=   m.x61 - 25*m.b268 <= 0)

m.c202 = Constraint(expr=   m.x62 - 25*m.b269 <= 0)

m.c203 = Constraint(expr=   m.x63 - 25*m.b270 <= 0)

m.c204 = Constraint(expr=   m.x64 - 25*m.b271 <= 0)

m.c205 = Constraint(expr=   m.x65 - 25*m.b272 <= 0)

m.c206 = Constraint(expr=   m.x66 - 25*m.b273 <= 0)

m.c207 = Constraint(expr=   m.x67 - 25*m.b274 <= 0)

m.c208 = Constraint(expr=   m.x68 - 25*m.b275 <= 0)

m.c209 = Constraint(expr=   m.x69 - 25*m.b276 <= 0)

m.c210 = Constraint(expr=   m.x70 - 25*m.b277 <= 0)

m.c211 = Constraint(expr=   m.x71 - 0.2*m.b278 >= 0)

m.c212 = Constraint(expr=   m.x72 - 0.2*m.b279 >= 0)

m.c213 = Constraint(expr=   m.x73 - 0.2*m.b280 >= 0)

m.c214 = Constraint(expr=   m.x74 - 0.2*m.b281 >= 0)

m.c215 = Constraint(expr=   m.x75 - 0.2*m.b282 >= 0)

m.c216 = Constraint(expr=   m.x76 - 0.2*m.b283 >= 0)

m.c217 = Constraint(expr=   m.x77 - 0.2*m.b284 >= 0)

m.c218 = Constraint(expr=   m.x78 - 0.2*m.b285 >= 0)

m.c219 = Constraint(expr=   m.x79 - 0.2*m.b286 >= 0)

m.c220 = Constraint(expr=   m.x80 - 0.2*m.b287 >= 0)

m.c221 = Constraint(expr=   m.x71 - 300.5*m.b278 <= 0)

m.c222 = Constraint(expr=   m.x72 - 300.5*m.b279 <= 0)

m.c223 = Constraint(expr=   m.x73 - 300.5*m.b280 <= 0)

m.c224 = Constraint(expr=   m.x74 - 300.5*m.b281 <= 0)

m.c225 = Constraint(expr=   m.x75 - 300.5*m.b282 <= 0)

m.c226 = Constraint(expr=   m.x76 - 300.5*m.b283 <= 0)

m.c227 = Constraint(expr=   m.x77 - 300.5*m.b284 <= 0)

m.c228 = Constraint(expr=   m.x78 - 300.5*m.b285 <= 0)

m.c229 = Constraint(expr=   m.x79 - 300.5*m.b286 <= 0)

m.c230 = Constraint(expr=   m.x80 - 300.5*m.b287 <= 0)

m.c231 = Constraint(expr=   m.x171 - 0.2*m.b378 >= 0)

m.c232 = Constraint(expr=   m.x172 - 0.2*m.b379 >= 0)

m.c233 = Constraint(expr=   m.x173 - 0.2*m.b380 >= 0)

m.c234 = Constraint(expr=   m.x174 - 0.2*m.b381 >= 0)

m.c235 = Constraint(expr=   m.x175 - 0.2*m.b382 >= 0)

m.c236 = Constraint(expr=   m.x176 - 0.2*m.b383 >= 0)

m.c237 = Constraint(expr=   m.x177 - 0.2*m.b384 >= 0)

m.c238 = Constraint(expr=   m.x171 - 20*m.b378 <= 0)

m.c239 = Constraint(expr=   m.x172 - 50*m.b379 <= 0)

m.c240 = Constraint(expr=   m.x173 - 47.5*m.b380 <= 0)

m.c241 = Constraint(expr=   m.x174 - 28*m.b381 <= 0)

m.c242 = Constraint(expr=   m.x175 - 100*m.b382 <= 0)

m.c243 = Constraint(expr=   m.x176 - 30*m.b383 <= 0)

m.c244 = Constraint(expr=   m.x177 - 25*m.b384 <= 0)

m.c245 = Constraint(expr=   m.x90 - 0.2*m.b297 >= 0)

m.c246 = Constraint(expr=   m.x99 - 0.2*m.b306 >= 0)

m.c247 = Constraint(expr=   m.x108 - 0.2*m.b315 >= 0)

m.c248 = Constraint(expr=   m.x117 - 0.2*m.b324 >= 0)

m.c249 = Constraint(expr=   m.x126 - 0.2*m.b333 >= 0)

m.c250 = Constraint(expr=   m.x135 - 0.2*m.b342 >= 0)

m.c251 = Constraint(expr=   m.x144 - 0.2*m.b351 >= 0)

m.c252 = Constraint(expr=   m.x153 - 0.2*m.b360 >= 0)

m.c253 = Constraint(expr=   m.x162 - 0.2*m.b369 >= 0)

m.c254 = Constraint(expr=   m.x81 - 0.2*m.b288 >= 0)

m.c255 = Constraint(expr=   m.x100 - 0.2*m.b307 >= 0)

m.c256 = Constraint(expr=   m.x109 - 0.2*m.b316 >= 0)

m.c257 = Constraint(expr=   m.x118 - 0.2*m.b325 >= 0)

m.c258 = Constraint(expr=   m.x127 - 0.2*m.b334 >= 0)

m.c259 = Constraint(expr=   m.x136 - 0.2*m.b343 >= 0)

m.c260 = Constraint(expr=   m.x145 - 0.2*m.b352 >= 0)

m.c261 = Constraint(expr=   m.x154 - 0.2*m.b361 >= 0)

m.c262 = Constraint(expr=   m.x163 - 0.2*m.b370 >= 0)

m.c263 = Constraint(expr=   m.x82 - 0.2*m.b289 >= 0)

m.c264 = Constraint(expr=   m.x91 - 0.2*m.b298 >= 0)

m.c265 = Constraint(expr=   m.x110 - 0.2*m.b317 >= 0)

m.c266 = Constraint(expr=   m.x119 - 0.2*m.b326 >= 0)

m.c267 = Constraint(expr=   m.x128 - 0.2*m.b335 >= 0)

m.c268 = Constraint(expr=   m.x137 - 0.2*m.b344 >= 0)

m.c269 = Constraint(expr=   m.x146 - 0.2*m.b353 >= 0)

m.c270 = Constraint(expr=   m.x155 - 0.2*m.b362 >= 0)

m.c271 = Constraint(expr=   m.x164 - 0.2*m.b371 >= 0)

m.c272 = Constraint(expr=   m.x83 - 0.2*m.b290 >= 0)

m.c273 = Constraint(expr=   m.x92 - 0.2*m.b299 >= 0)

m.c274 = Constraint(expr=   m.x101 - 0.2*m.b308 >= 0)

m.c275 = Constraint(expr=   m.x120 - 0.2*m.b327 >= 0)

m.c276 = Constraint(expr=   m.x129 - 0.2*m.b336 >= 0)

m.c277 = Constraint(expr=   m.x138 - 0.2*m.b345 >= 0)

m.c278 = Constraint(expr=   m.x147 - 0.2*m.b354 >= 0)

m.c279 = Constraint(expr=   m.x156 - 0.2*m.b363 >= 0)

m.c280 = Constraint(expr=   m.x165 - 0.2*m.b372 >= 0)

m.c281 = Constraint(expr=   m.x84 - 0.2*m.b291 >= 0)

m.c282 = Constraint(expr=   m.x93 - 0.2*m.b300 >= 0)

m.c283 = Constraint(expr=   m.x102 - 0.2*m.b309 >= 0)

m.c284 = Constraint(expr=   m.x111 - 0.2*m.b318 >= 0)

m.c285 = Constraint(expr=   m.x130 - 0.2*m.b337 >= 0)

m.c286 = Constraint(expr=   m.x139 - 0.2*m.b346 >= 0)

m.c287 = Constraint(expr=   m.x148 - 0.2*m.b355 >= 0)

m.c288 = Constraint(expr=   m.x157 - 0.2*m.b364 >= 0)

m.c289 = Constraint(expr=   m.x166 - 0.2*m.b373 >= 0)

m.c290 = Constraint(expr=   m.x85 - 0.2*m.b292 >= 0)

m.c291 = Constraint(expr=   m.x94 - 0.2*m.b301 >= 0)

m.c292 = Constraint(expr=   m.x103 - 0.2*m.b310 >= 0)

m.c293 = Constraint(expr=   m.x112 - 0.2*m.b319 >= 0)

m.c294 = Constraint(expr=   m.x121 - 0.2*m.b328 >= 0)

m.c295 = Constraint(expr=   m.x140 - 0.2*m.b347 >= 0)

m.c296 = Constraint(expr=   m.x149 - 0.2*m.b356 >= 0)

m.c297 = Constraint(expr=   m.x158 - 0.2*m.b365 >= 0)

m.c298 = Constraint(expr=   m.x167 - 0.2*m.b374 >= 0)

m.c299 = Constraint(expr=   m.x86 - 0.2*m.b293 >= 0)

m.c300 = Constraint(expr=   m.x95 - 0.2*m.b302 >= 0)

m.c301 = Constraint(expr=   m.x104 - 0.2*m.b311 >= 0)

m.c302 = Constraint(expr=   m.x113 - 0.2*m.b320 >= 0)

m.c303 = Constraint(expr=   m.x122 - 0.2*m.b329 >= 0)

m.c304 = Constraint(expr=   m.x131 - 0.2*m.b338 >= 0)

m.c305 = Constraint(expr=   m.x150 - 0.2*m.b357 >= 0)

m.c306 = Constraint(expr=   m.x159 - 0.2*m.b366 >= 0)

m.c307 = Constraint(expr=   m.x168 - 0.2*m.b375 >= 0)

m.c308 = Constraint(expr=   m.x87 - 0.2*m.b294 >= 0)

m.c309 = Constraint(expr=   m.x96 - 0.2*m.b303 >= 0)

m.c310 = Constraint(expr=   m.x105 - 0.2*m.b312 >= 0)

m.c311 = Constraint(expr=   m.x114 - 0.2*m.b321 >= 0)

m.c312 = Constraint(expr=   m.x123 - 0.2*m.b330 >= 0)

m.c313 = Constraint(expr=   m.x132 - 0.2*m.b339 >= 0)

m.c314 = Constraint(expr=   m.x141 - 0.2*m.b348 >= 0)

m.c315 = Constraint(expr=   m.x160 - 0.2*m.b367 >= 0)

m.c316 = Constraint(expr=   m.x169 - 0.2*m.b376 >= 0)

m.c317 = Constraint(expr=   m.x88 - 0.2*m.b295 >= 0)

m.c318 = Constraint(expr=   m.x97 - 0.2*m.b304 >= 0)

m.c319 = Constraint(expr=   m.x106 - 0.2*m.b313 >= 0)

m.c320 = Constraint(expr=   m.x115 - 0.2*m.b322 >= 0)

m.c321 = Constraint(expr=   m.x124 - 0.2*m.b331 >= 0)

m.c322 = Constraint(expr=   m.x133 - 0.2*m.b340 >= 0)

m.c323 = Constraint(expr=   m.x142 - 0.2*m.b349 >= 0)

m.c324 = Constraint(expr=   m.x151 - 0.2*m.b358 >= 0)

m.c325 = Constraint(expr=   m.x170 - 0.2*m.b377 >= 0)

m.c326 = Constraint(expr=   m.x89 - 0.2*m.b296 >= 0)

m.c327 = Constraint(expr=   m.x98 - 0.2*m.b305 >= 0)

m.c328 = Constraint(expr=   m.x107 - 0.2*m.b314 >= 0)

m.c329 = Constraint(expr=   m.x116 - 0.2*m.b323 >= 0)

m.c330 = Constraint(expr=   m.x125 - 0.2*m.b332 >= 0)

m.c331 = Constraint(expr=   m.x134 - 0.2*m.b341 >= 0)

m.c332 = Constraint(expr=   m.x143 - 0.2*m.b350 >= 0)

m.c333 = Constraint(expr=   m.x152 - 0.2*m.b359 >= 0)

m.c334 = Constraint(expr=   m.x161 - 0.2*m.b368 >= 0)

m.c335 = Constraint(expr=   m.x90 - 300.5*m.b297 <= 0)

m.c336 = Constraint(expr=   m.x99 - 300.5*m.b306 <= 0)

m.c337 = Constraint(expr=   m.x108 - 300.5*m.b315 <= 0)

m.c338 = Constraint(expr=   m.x117 - 300.5*m.b324 <= 0)

m.c339 = Constraint(expr=   m.x126 - 300.5*m.b333 <= 0)

m.c340 = Constraint(expr=   m.x135 - 300.5*m.b342 <= 0)

m.c341 = Constraint(expr=   m.x144 - 300.5*m.b351 <= 0)

m.c342 = Constraint(expr=   m.x153 - 300.5*m.b360 <= 0)

m.c343 = Constraint(expr=   m.x162 - 300.5*m.b369 <= 0)

m.c344 = Constraint(expr=   m.x81 - 300.5*m.b288 <= 0)

m.c345 = Constraint(expr=   m.x100 - 300.5*m.b307 <= 0)

m.c346 = Constraint(expr=   m.x109 - 300.5*m.b316 <= 0)

m.c347 = Constraint(expr=   m.x118 - 300.5*m.b325 <= 0)

m.c348 = Constraint(expr=   m.x127 - 300.5*m.b334 <= 0)

m.c349 = Constraint(expr=   m.x136 - 300.5*m.b343 <= 0)

m.c350 = Constraint(expr=   m.x145 - 300.5*m.b352 <= 0)

m.c351 = Constraint(expr=   m.x154 - 300.5*m.b361 <= 0)

m.c352 = Constraint(expr=   m.x163 - 300.5*m.b370 <= 0)

m.c353 = Constraint(expr=   m.x82 - 300.5*m.b289 <= 0)

m.c354 = Constraint(expr=   m.x91 - 300.5*m.b298 <= 0)

m.c355 = Constraint(expr=   m.x110 - 300.5*m.b317 <= 0)

m.c356 = Constraint(expr=   m.x119 - 300.5*m.b326 <= 0)

m.c357 = Constraint(expr=   m.x128 - 300.5*m.b335 <= 0)

m.c358 = Constraint(expr=   m.x137 - 300.5*m.b344 <= 0)

m.c359 = Constraint(expr=   m.x146 - 300.5*m.b353 <= 0)

m.c360 = Constraint(expr=   m.x155 - 300.5*m.b362 <= 0)

m.c361 = Constraint(expr=   m.x164 - 300.5*m.b371 <= 0)

m.c362 = Constraint(expr=   m.x83 - 300.5*m.b290 <= 0)

m.c363 = Constraint(expr=   m.x92 - 300.5*m.b299 <= 0)

m.c364 = Constraint(expr=   m.x101 - 300.5*m.b308 <= 0)

m.c365 = Constraint(expr=   m.x120 - 300.5*m.b327 <= 0)

m.c366 = Constraint(expr=   m.x129 - 300.5*m.b336 <= 0)

m.c367 = Constraint(expr=   m.x138 - 300.5*m.b345 <= 0)

m.c368 = Constraint(expr=   m.x147 - 300.5*m.b354 <= 0)

m.c369 = Constraint(expr=   m.x156 - 300.5*m.b363 <= 0)

m.c370 = Constraint(expr=   m.x165 - 300.5*m.b372 <= 0)

m.c371 = Constraint(expr=   m.x84 - 300.5*m.b291 <= 0)

m.c372 = Constraint(expr=   m.x93 - 300.5*m.b300 <= 0)

m.c373 = Constraint(expr=   m.x102 - 300.5*m.b309 <= 0)

m.c374 = Constraint(expr=   m.x111 - 300.5*m.b318 <= 0)

m.c375 = Constraint(expr=   m.x130 - 300.5*m.b337 <= 0)

m.c376 = Constraint(expr=   m.x139 - 300.5*m.b346 <= 0)

m.c377 = Constraint(expr=   m.x148 - 300.5*m.b355 <= 0)

m.c378 = Constraint(expr=   m.x157 - 300.5*m.b364 <= 0)

m.c379 = Constraint(expr=   m.x166 - 300.5*m.b373 <= 0)

m.c380 = Constraint(expr=   m.x85 - 300.5*m.b292 <= 0)

m.c381 = Constraint(expr=   m.x94 - 300.5*m.b301 <= 0)

m.c382 = Constraint(expr=   m.x103 - 300.5*m.b310 <= 0)

m.c383 = Constraint(expr=   m.x112 - 300.5*m.b319 <= 0)

m.c384 = Constraint(expr=   m.x121 - 300.5*m.b328 <= 0)

m.c385 = Constraint(expr=   m.x140 - 300.5*m.b347 <= 0)

m.c386 = Constraint(expr=   m.x149 - 300.5*m.b356 <= 0)

m.c387 = Constraint(expr=   m.x158 - 300.5*m.b365 <= 0)

m.c388 = Constraint(expr=   m.x167 - 300.5*m.b374 <= 0)

m.c389 = Constraint(expr=   m.x86 - 300.5*m.b293 <= 0)

m.c390 = Constraint(expr=   m.x95 - 300.5*m.b302 <= 0)

m.c391 = Constraint(expr=   m.x104 - 300.5*m.b311 <= 0)

m.c392 = Constraint(expr=   m.x113 - 300.5*m.b320 <= 0)

m.c393 = Constraint(expr=   m.x122 - 300.5*m.b329 <= 0)

m.c394 = Constraint(expr=   m.x131 - 300.5*m.b338 <= 0)

m.c395 = Constraint(expr=   m.x150 - 300.5*m.b357 <= 0)

m.c396 = Constraint(expr=   m.x159 - 300.5*m.b366 <= 0)

m.c397 = Constraint(expr=   m.x168 - 300.5*m.b375 <= 0)

m.c398 = Constraint(expr=   m.x87 - 300.5*m.b294 <= 0)

m.c399 = Constraint(expr=   m.x96 - 300.5*m.b303 <= 0)

m.c400 = Constraint(expr=   m.x105 - 300.5*m.b312 <= 0)

m.c401 = Constraint(expr=   m.x114 - 300.5*m.b321 <= 0)

m.c402 = Constraint(expr=   m.x123 - 300.5*m.b330 <= 0)

m.c403 = Constraint(expr=   m.x132 - 300.5*m.b339 <= 0)

m.c404 = Constraint(expr=   m.x141 - 300.5*m.b348 <= 0)

m.c405 = Constraint(expr=   m.x160 - 300.5*m.b367 <= 0)

m.c406 = Constraint(expr=   m.x169 - 300.5*m.b376 <= 0)

m.c407 = Constraint(expr=   m.x88 - 300.5*m.b295 <= 0)

m.c408 = Constraint(expr=   m.x97 - 300.5*m.b304 <= 0)

m.c409 = Constraint(expr=   m.x106 - 300.5*m.b313 <= 0)

m.c410 = Constraint(expr=   m.x115 - 300.5*m.b322 <= 0)

m.c411 = Constraint(expr=   m.x124 - 300.5*m.b331 <= 0)

m.c412 = Constraint(expr=   m.x133 - 300.5*m.b340 <= 0)

m.c413 = Constraint(expr=   m.x142 - 300.5*m.b349 <= 0)

m.c414 = Constraint(expr=   m.x151 - 300.5*m.b358 <= 0)

m.c415 = Constraint(expr=   m.x170 - 300.5*m.b377 <= 0)

m.c416 = Constraint(expr=   m.x89 - 300.5*m.b296 <= 0)

m.c417 = Constraint(expr=   m.x98 - 300.5*m.b305 <= 0)

m.c418 = Constraint(expr=   m.x107 - 300.5*m.b314 <= 0)

m.c419 = Constraint(expr=   m.x116 - 300.5*m.b323 <= 0)

m.c420 = Constraint(expr=   m.x125 - 300.5*m.b332 <= 0)

m.c421 = Constraint(expr=   m.x134 - 300.5*m.b341 <= 0)

m.c422 = Constraint(expr=   m.x143 - 300.5*m.b350 <= 0)

m.c423 = Constraint(expr=   m.x152 - 300.5*m.b359 <= 0)

m.c424 = Constraint(expr=   m.x161 - 300.5*m.b368 <= 0)
