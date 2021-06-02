#  MINLP written by GAMS Convert at 04/21/18 13:52:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        263       57       18      188        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        292      247       45        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1349     1260       89        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,100000000),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,4100),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,4100),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,2325),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,2325),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,4100),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,4100),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,1125),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,1125),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,4100),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,4100),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,875),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,875),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,2325),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,2325),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,1125),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,1125),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,875),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,875),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,2325),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,2325),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,1125),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,1125),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,875),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,875),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,2325),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,1125),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,875),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,2325),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,1125),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,875),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,4100),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,4100),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,725),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,725),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,4100),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,725),initialize=0)
m.x174 = Var(within=Reals,bounds=(65,125),initialize=125)
m.x175 = Var(within=Reals,bounds=(65,125),initialize=125)
m.x176 = Var(within=Reals,bounds=(65,125),initialize=125)
m.x177 = Var(within=Reals,bounds=(25,85),initialize=85)
m.x178 = Var(within=Reals,bounds=(25,85),initialize=85)
m.x179 = Var(within=Reals,bounds=(25,85),initialize=85)
m.x180 = Var(within=Reals,bounds=(25,45),initialize=45)
m.x181 = Var(within=Reals,bounds=(25,45),initialize=45)
m.x182 = Var(within=Reals,bounds=(25,45),initialize=45)
m.x183 = Var(within=Reals,bounds=(35,240),initialize=35)
m.x184 = Var(within=Reals,bounds=(35,240),initialize=35)
m.x185 = Var(within=Reals,bounds=(35,240),initialize=35)
m.x186 = Var(within=Reals,bounds=(35,55),initialize=35)
m.x187 = Var(within=Reals,bounds=(35,55),initialize=35)
m.x188 = Var(within=Reals,bounds=(35,55),initialize=35)
m.x189 = Var(within=Reals,bounds=(65,125),initialize=65)
m.x190 = Var(within=Reals,bounds=(25,85),initialize=25)
m.x191 = Var(within=Reals,bounds=(25,45),initialize=25)
m.x192 = Var(within=Reals,bounds=(10,175),initialize=10)
m.x193 = Var(within=Reals,bounds=(10,175),initialize=10)
m.x194 = Var(within=Reals,bounds=(10,175),initialize=10)
m.x195 = Var(within=Reals,bounds=(10,90),initialize=70)
m.x196 = Var(within=Reals,bounds=(10,90),initialize=70)
m.x197 = Var(within=Reals,bounds=(10,90),initialize=70)
m.x198 = Var(within=Reals,bounds=(10,215),initialize=10)
m.x199 = Var(within=Reals,bounds=(10,215),initialize=10)
m.x200 = Var(within=Reals,bounds=(10,215),initialize=10)
m.x201 = Var(within=Reals,bounds=(10,50),initialize=30)
m.x202 = Var(within=Reals,bounds=(10,50),initialize=30)
m.x203 = Var(within=Reals,bounds=(10,50),initialize=30)
m.x204 = Var(within=Reals,bounds=(10,215),initialize=10)
m.x205 = Var(within=Reals,bounds=(10,215),initialize=10)
m.x206 = Var(within=Reals,bounds=(10,215),initialize=10)
m.x207 = Var(within=Reals,bounds=(10,30),initialize=10)
m.x208 = Var(within=Reals,bounds=(10,30),initialize=10)
m.x209 = Var(within=Reals,bounds=(10,30),initialize=10)
m.x210 = Var(within=Reals,bounds=(10,75),initialize=75)
m.x211 = Var(within=Reals,bounds=(10,75),initialize=75)
m.x212 = Var(within=Reals,bounds=(10,75),initialize=75)
m.x213 = Var(within=Reals,bounds=(10,55),initialize=35)
m.x214 = Var(within=Reals,bounds=(10,55),initialize=35)
m.x215 = Var(within=Reals,bounds=(10,55),initialize=35)
m.x216 = Var(within=Reals,bounds=(10,55),initialize=10)
m.x217 = Var(within=Reals,bounds=(10,55),initialize=10)
m.x218 = Var(within=Reals,bounds=(10,55),initialize=10)
m.x219 = Var(within=Reals,bounds=(10,95),initialize=95)
m.x220 = Var(within=Reals,bounds=(10,95),initialize=95)
m.x221 = Var(within=Reals,bounds=(10,95),initialize=95)
m.x222 = Var(within=Reals,bounds=(10,65),initialize=55)
m.x223 = Var(within=Reals,bounds=(10,65),initialize=55)
m.x224 = Var(within=Reals,bounds=(10,65),initialize=55)
m.x225 = Var(within=Reals,bounds=(10,65),initialize=15)
m.x226 = Var(within=Reals,bounds=(10,65),initialize=15)
m.x227 = Var(within=Reals,bounds=(10,65),initialize=15)
m.x228 = Var(within=Reals,bounds=(10,95),initialize=85)
m.x229 = Var(within=Reals,bounds=(10,55),initialize=45)
m.x230 = Var(within=Reals,bounds=(10,15),initialize=10)
m.x231 = Var(within=Reals,bounds=(10,95),initialize=35)
m.x232 = Var(within=Reals,bounds=(10,55),initialize=10)
m.x233 = Var(within=Reals,bounds=(10,15),initialize=10)
m.x234 = Var(within=Reals,bounds=(10,130),initialize=70)
m.x235 = Var(within=Reals,bounds=(10,90),initialize=30)
m.x236 = Var(within=Reals,bounds=(10,50),initialize=30)
m.x237 = Var(within=Reals,bounds=(10,210),initialize=10)
m.x238 = Var(within=Reals,bounds=(10,210),initialize=10)
m.x239 = Var(within=Reals,bounds=(10,210),initialize=10)
m.x240 = Var(within=Reals,bounds=(10,25),initialize=10)
m.x241 = Var(within=Reals,bounds=(10,25),initialize=10)
m.x242 = Var(within=Reals,bounds=(10,25),initialize=10)
m.x243 = Var(within=Reals,bounds=(10,240),initialize=34)
m.x244 = Var(within=Reals,bounds=(10,240),initialize=219)
m.b245 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b246 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b247 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b248 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b249 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b250 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b251 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b252 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b253 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b254 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b255 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b256 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b257 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b258 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b259 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b260 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b261 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b262 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b263 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b264 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b265 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b266 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b267 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b268 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b269 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b270 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b271 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b272 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b273 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b274 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b275 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b276 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b277 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b278 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b279 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b280 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b281 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b282 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b283 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b284 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b285 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b286 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b287 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b288 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b289 = Var(within=Binary,bounds=(0,1),initialize=1)
m.x291 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x292 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   m.x132 + m.x133 - m.x134 - m.x135 - m.x136 - m.x137, sense=maximize)

m.c1 = Constraint(expr= - m.x138 - m.x139 - m.x140 - m.x141 - m.x150 - m.x151 - m.x156 - m.x157 - m.x162 - m.x165
                        == -2325)

m.c2 = Constraint(expr= - m.x142 - m.x143 - m.x144 - m.x145 - m.x152 - m.x153 - m.x158 - m.x159 - m.x163 - m.x166
                        == -1125)

m.c3 = Constraint(expr= - m.x146 - m.x147 - m.x148 - m.x149 - m.x154 - m.x155 - m.x160 - m.x161 - m.x164 - m.x167
                        == -875)

m.c4 = Constraint(expr= - m.x138 - m.x139 - m.x142 - m.x143 - m.x146 - m.x147 - m.x168 - m.x169 - m.x172 == -4100)

m.c5 = Constraint(expr= - m.x140 - m.x141 - m.x144 - m.x145 - m.x148 - m.x149 - m.x170 - m.x171 - m.x173 == -725)

m.c6 = Constraint(expr= - m.x138 - m.x140 - m.x150 - m.x156 + 38.75*m.x174 - 38.75*m.x175 == 0)

m.c7 = Constraint(expr= - m.x139 - m.x141 - m.x151 - m.x157 + 38.75*m.x175 - 38.75*m.x176 == 0)

m.c8 = Constraint(expr= - m.x142 - m.x144 - m.x152 - m.x158 + 18.75*m.x177 - 18.75*m.x178 == 0)

m.c9 = Constraint(expr= - m.x143 - m.x145 - m.x153 - m.x159 + 18.75*m.x178 - 18.75*m.x179 == 0)

m.c10 = Constraint(expr= - m.x146 - m.x148 - m.x154 - m.x160 + 43.75*m.x180 - 43.75*m.x181 == 0)

m.c11 = Constraint(expr= - m.x147 - m.x149 - m.x155 - m.x161 + 43.75*m.x181 - 43.75*m.x182 == 0)

m.c12 = Constraint(expr= - m.x138 - m.x142 - m.x146 - m.x168 + 20*m.x183 - 20*m.x184 == 0)

m.c13 = Constraint(expr= - m.x139 - m.x143 - m.x147 - m.x169 + 20*m.x184 - 20*m.x185 == 0)

m.c14 = Constraint(expr= - m.x140 - m.x144 - m.x148 - m.x170 + 36.25*m.x186 - 36.25*m.x187 == 0)

m.c15 = Constraint(expr= - m.x141 - m.x145 - m.x149 - m.x171 + 36.25*m.x187 - 36.25*m.x188 == 0)

m.c16 = Constraint(expr= - m.x162 + 38.75*m.x176 - 38.75*m.x189 == 0)

m.c17 = Constraint(expr= - m.x163 + 18.75*m.x179 - 18.75*m.x190 == 0)

m.c18 = Constraint(expr= - m.x164 + 43.75*m.x182 - 43.75*m.x191 == 0)

m.c19 = Constraint(expr= - m.x165 + 38.75*m.x189 == 2518.75)

m.c20 = Constraint(expr= - m.x166 + 18.75*m.x190 == 468.75)

m.c21 = Constraint(expr= - m.x167 + 43.75*m.x191 == 1093.75)

m.c22 = Constraint(expr= - m.x172 - 20*m.x183 == -4800)

m.c23 = Constraint(expr= - m.x173 - 36.25*m.x186 == -1993.75)

m.c24 = Constraint(expr= - m.x174 == -125)

m.c25 = Constraint(expr= - m.x177 == -85)

m.c26 = Constraint(expr= - m.x180 == -45)

m.c27 = Constraint(expr= - m.x185 == -35)

m.c28 = Constraint(expr= - m.x188 == -35)

m.c29 = Constraint(expr=   m.x174 - m.x175 >= 0)

m.c30 = Constraint(expr=   m.x175 - m.x176 >= 0)

m.c31 = Constraint(expr=   m.x177 - m.x178 >= 0)

m.c32 = Constraint(expr=   m.x178 - m.x179 >= 0)

m.c33 = Constraint(expr=   m.x180 - m.x181 >= 0)

m.c34 = Constraint(expr=   m.x181 - m.x182 >= 0)

m.c35 = Constraint(expr=   m.x176 - m.x189 >= 0)

m.c36 = Constraint(expr=   m.x179 - m.x190 >= 0)

m.c37 = Constraint(expr=   m.x182 - m.x191 >= 0)

m.c38 = Constraint(expr=   m.x189 >= 65)

m.c39 = Constraint(expr=   m.x190 >= 25)

m.c40 = Constraint(expr=   m.x191 >= 25)

m.c41 = Constraint(expr=   m.x183 - m.x184 >= 0)

m.c42 = Constraint(expr=   m.x184 - m.x185 >= 0)

m.c43 = Constraint(expr=   m.x186 - m.x187 >= 0)

m.c44 = Constraint(expr=   m.x187 - m.x188 >= 0)

m.c45 = Constraint(expr= - m.x183 >= -240)

m.c46 = Constraint(expr= - m.x186 >= -55)

m.c47 = Constraint(expr=   m.x138 - 2325*m.b246 <= 0)

m.c48 = Constraint(expr=   m.x139 - 2325*m.b247 <= 0)

m.c49 = Constraint(expr=   m.x140 - 725*m.b248 <= 0)

m.c50 = Constraint(expr=   m.x141 - 725*m.b249 <= 0)

m.c51 = Constraint(expr=   m.x142 - 1125*m.b250 <= 0)

m.c52 = Constraint(expr=   m.x143 - 1125*m.b251 <= 0)

m.c53 = Constraint(expr=   m.x144 - 725*m.b252 <= 0)

m.c54 = Constraint(expr=   m.x145 - 725*m.b253 <= 0)

m.c55 = Constraint(expr=   m.x146 - 875*m.b254 <= 0)

m.c56 = Constraint(expr=   m.x147 - 875*m.b255 <= 0)

m.c57 = Constraint(expr=   m.x148 - 725*m.b256 <= 0)

m.c58 = Constraint(expr=   m.x149 - 725*m.b257 <= 0)

m.c59 = Constraint(expr=   m.x150 - 2325*m.b258 <= 0)

m.c60 = Constraint(expr=   m.x151 - 2325*m.b259 <= 0)

m.c61 = Constraint(expr=   m.x152 - 1125*m.b261 <= 0)

m.c62 = Constraint(expr=   m.x153 - 1125*m.b262 <= 0)

m.c63 = Constraint(expr=   m.x154 - 875*m.b264 <= 0)

m.c64 = Constraint(expr=   m.x155 - 875*m.b265 <= 0)

m.c65 = Constraint(expr=   m.x156 - 2325*m.b267 <= 0)

m.c66 = Constraint(expr=   m.x157 - 2325*m.b268 <= 0)

m.c67 = Constraint(expr=   m.x158 - 1125*m.b270 <= 0)

m.c68 = Constraint(expr=   m.x159 - 1125*m.b271 <= 0)

m.c69 = Constraint(expr=   m.x160 - 875*m.b273 <= 0)

m.c70 = Constraint(expr=   m.x161 - 875*m.b274 <= 0)

m.c71 = Constraint(expr=   m.x162 - 2325*m.b276 <= 0)

m.c72 = Constraint(expr=   m.x163 - 1125*m.b277 <= 0)

m.c73 = Constraint(expr=   m.x164 - 875*m.b278 <= 0)

m.c74 = Constraint(expr=   m.x165 - 2325*m.b279 <= 0)

m.c75 = Constraint(expr=   m.x166 - 1125*m.b280 <= 0)

m.c76 = Constraint(expr=   m.x167 - 875*m.b281 <= 0)

m.c77 = Constraint(expr=   m.x168 - 4100*m.b282 <= 0)

m.c78 = Constraint(expr=   m.x169 - 4100*m.b283 <= 0)

m.c79 = Constraint(expr=   m.x170 - 725*m.b285 <= 0)

m.c80 = Constraint(expr=   m.x171 - 725*m.b286 <= 0)

m.c81 = Constraint(expr=   m.x172 - 4100*m.b288 <= 0)

m.c82 = Constraint(expr=   m.x173 - 725*m.b289 <= 0)

m.c83 = Constraint(expr= - m.x174 + m.x183 + m.x192 + 175*m.b246 <= 175)

m.c84 = Constraint(expr= - m.x175 + m.x184 + m.x193 + 175*m.b247 <= 175)

m.c85 = Constraint(expr= - m.x174 + m.x186 + m.x195 + 90*m.b248 <= 90)

m.c86 = Constraint(expr= - m.x175 + m.x187 + m.x196 + 90*m.b249 <= 90)

m.c87 = Constraint(expr= - m.x177 + m.x183 + m.x198 + 215*m.b250 <= 215)

m.c88 = Constraint(expr= - m.x178 + m.x184 + m.x199 + 215*m.b251 <= 215)

m.c89 = Constraint(expr= - m.x177 + m.x186 + m.x201 + 50*m.b252 <= 50)

m.c90 = Constraint(expr= - m.x178 + m.x187 + m.x202 + 50*m.b253 <= 50)

m.c91 = Constraint(expr= - m.x180 + m.x183 + m.x204 + 215*m.b254 <= 215)

m.c92 = Constraint(expr= - m.x181 + m.x184 + m.x205 + 215*m.b255 <= 215)

m.c93 = Constraint(expr= - m.x180 + m.x186 + m.x207 + 30*m.b256 <= 30)

m.c94 = Constraint(expr= - m.x181 + m.x187 + m.x208 + 30*m.b257 <= 30)

m.c95 = Constraint(expr= - m.x175 + m.x184 + m.x193 + 175*m.b246 <= 175)

m.c96 = Constraint(expr= - m.x176 + m.x185 + m.x194 + 175*m.b247 <= 175)

m.c97 = Constraint(expr= - m.x175 + m.x187 + m.x196 + 90*m.b248 <= 90)

m.c98 = Constraint(expr= - m.x176 + m.x188 + m.x197 + 90*m.b249 <= 90)

m.c99 = Constraint(expr= - m.x178 + m.x184 + m.x199 + 215*m.b250 <= 215)

m.c100 = Constraint(expr= - m.x179 + m.x185 + m.x200 + 215*m.b251 <= 215)

m.c101 = Constraint(expr= - m.x178 + m.x187 + m.x202 + 50*m.b252 <= 50)

m.c102 = Constraint(expr= - m.x179 + m.x188 + m.x203 + 50*m.b253 <= 50)

m.c103 = Constraint(expr= - m.x181 + m.x184 + m.x205 + 215*m.b254 <= 215)

m.c104 = Constraint(expr= - m.x182 + m.x185 + m.x206 + 215*m.b255 <= 215)

m.c105 = Constraint(expr= - m.x181 + m.x187 + m.x208 + 30*m.b256 <= 30)

m.c106 = Constraint(expr= - m.x182 + m.x188 + m.x209 + 30*m.b257 <= 30)

m.c107 = Constraint(expr= - m.x174 + m.x210 + 75*m.b258 <= -5)

m.c108 = Constraint(expr= - m.x175 + m.x211 + 75*m.b259 <= -5)

m.c109 = Constraint(expr= - m.x177 + m.x213 + 55*m.b261 <= -25)

m.c110 = Constraint(expr= - m.x178 + m.x214 + 55*m.b262 <= -25)

m.c111 = Constraint(expr= - m.x180 + m.x216 + 55*m.b264 <= -25)

m.c112 = Constraint(expr= - m.x181 + m.x217 + 55*m.b265 <= -25)

m.c113 = Constraint(expr= - m.x175 + m.x211 + 75*m.b258 <= 25)

m.c114 = Constraint(expr= - m.x176 + m.x212 + 75*m.b259 <= 25)

m.c115 = Constraint(expr= - m.x178 + m.x214 + 55*m.b261 <= 5)

m.c116 = Constraint(expr= - m.x179 + m.x215 + 55*m.b262 <= 5)

m.c117 = Constraint(expr= - m.x181 + m.x217 + 55*m.b264 <= 5)

m.c118 = Constraint(expr= - m.x182 + m.x218 + 55*m.b265 <= 5)

m.c119 = Constraint(expr= - m.x174 + m.x219 + 95*m.b267 <= 5)

m.c120 = Constraint(expr= - m.x175 + m.x220 + 95*m.b268 <= 5)

m.c121 = Constraint(expr= - m.x177 + m.x222 + 65*m.b270 <= -25)

m.c122 = Constraint(expr= - m.x178 + m.x223 + 65*m.b271 <= -25)

m.c123 = Constraint(expr= - m.x180 + m.x225 + 65*m.b273 <= -25)

m.c124 = Constraint(expr= - m.x181 + m.x226 + 65*m.b274 <= -25)

m.c125 = Constraint(expr= - m.x175 + m.x220 + 95*m.b267 <= 65)

m.c126 = Constraint(expr= - m.x176 + m.x221 + 95*m.b268 <= 65)

m.c127 = Constraint(expr= - m.x178 + m.x223 + 65*m.b270 <= 35)

m.c128 = Constraint(expr= - m.x179 + m.x224 + 65*m.b271 <= 35)

m.c129 = Constraint(expr= - m.x181 + m.x226 + 65*m.b273 <= 35)

m.c130 = Constraint(expr= - m.x182 + m.x227 + 65*m.b274 <= 35)

m.c131 = Constraint(expr= - m.x176 + m.x228 + 95*m.b276 <= 55)

m.c132 = Constraint(expr= - m.x179 + m.x229 + 55*m.b277 <= 15)

m.c133 = Constraint(expr= - m.x182 + m.x230 + 15*m.b278 <= -25)

m.c134 = Constraint(expr= - m.x189 + m.x231 + 95*m.b276 <= 65)

m.c135 = Constraint(expr= - m.x190 + m.x232 + 55*m.b277 <= 25)

m.c136 = Constraint(expr= - m.x191 + m.x233 + 15*m.b278 <= -15)

m.c137 = Constraint(expr= - m.x189 + m.x234 + 130*m.b279 <= 135)

m.c138 = Constraint(expr= - m.x190 + m.x235 + 90*m.b280 <= 95)

m.c139 = Constraint(expr= - m.x191 + m.x236 + 50*m.b281 <= 55)

m.c140 = Constraint(expr=   m.x183 + m.x237 + 210*m.b282 <= 241)

m.c141 = Constraint(expr=   m.x184 + m.x238 + 210*m.b283 <= 241)

m.c142 = Constraint(expr=   m.x186 + m.x240 + 25*m.b285 <= 56)

m.c143 = Constraint(expr=   m.x187 + m.x241 + 25*m.b286 <= 56)

m.c144 = Constraint(expr=   m.x184 + m.x238 + 210*m.b282 <= 240)

m.c145 = Constraint(expr=   m.x185 + m.x239 + 210*m.b283 <= 240)

m.c146 = Constraint(expr=   m.x187 + m.x241 + 25*m.b285 <= 55)

m.c147 = Constraint(expr=   m.x188 + m.x242 + 25*m.b286 <= 55)

m.c148 = Constraint(expr=   m.x183 + m.x243 + 240*m.b288 <= 514)

m.c149 = Constraint(expr=   m.x186 + m.x244 + 240*m.b289 <= 514)

m.c150 = Constraint(expr=   m.x8 - m.x9 - m.x21 - m.x33 - m.x45 - m.x57 - m.x69 - m.x81 - m.x93 - m.x105 - m.x117 == 0)

m.c151 = Constraint(expr=   m.x8 - m.x10 - m.x22 - m.x34 - m.x46 - m.x58 - m.x70 - m.x82 - m.x94 - m.x106 - m.x118 == 0)

m.c152 = Constraint(expr=   m.x8 - m.x11 - m.x23 - m.x35 - m.x47 - m.x59 - m.x71 - m.x83 - m.x95 - m.x107 - m.x119 == 0)

m.c153 = Constraint(expr=   m.x8 - m.x12 - m.x24 - m.x36 - m.x48 - m.x60 - m.x72 - m.x84 - m.x96 - m.x108 - m.x120 == 0)

m.c154 = Constraint(expr=   m.x8 - m.x13 - m.x25 - m.x37 - m.x49 - m.x61 - m.x73 - m.x85 - m.x97 - m.x109 - m.x121 == 0)

m.c155 = Constraint(expr=   m.x8 - m.x14 - m.x26 - m.x38 - m.x50 - m.x62 - m.x74 - m.x86 - m.x98 - m.x110 - m.x122 == 0)

m.c156 = Constraint(expr=   m.x8 - m.x15 - m.x27 - m.x39 - m.x51 - m.x63 - m.x75 - m.x87 - m.x99 - m.x111 - m.x123 == 0)

m.c157 = Constraint(expr=   m.x8 - m.x16 - m.x28 - m.x40 - m.x52 - m.x64 - m.x76 - m.x88 - m.x100 - m.x112 - m.x124
                          == 0)

m.c158 = Constraint(expr=   m.x8 - m.x17 - m.x29 - m.x41 - m.x53 - m.x65 - m.x77 - m.x89 - m.x101 - m.x113 - m.x125
                          == 0)

m.c159 = Constraint(expr=   m.x8 - m.x18 - m.x30 - m.x42 - m.x54 - m.x66 - m.x78 - m.x90 - m.x102 - m.x114 - m.x126
                          == 0)

m.c160 = Constraint(expr=   m.x8 - m.x19 - m.x31 - m.x43 - m.x55 - m.x67 - m.x79 - m.x91 - m.x103 - m.x115 - m.x127
                          == 0)

m.c161 = Constraint(expr=   m.x8 - m.x20 - m.x32 - m.x44 - m.x56 - m.x68 - m.x80 - m.x92 - m.x104 - m.x116 - m.x128
                          == 0)

m.c162 = Constraint(expr=   2.85714285714286*m.x1 - m.x8 == 0)

m.c163 = Constraint(expr=   m.x2 - m.x5 - m.x7 - m.x172 - m.x173 == 0)

m.c164 = Constraint(expr=   m.x1 + m.x2 + m.x3 - m.x8 == 0)

m.c165 = Constraint(expr= - m.x7 - m.x150 - m.x151 - m.x152 - m.x153 - m.x154 - m.x155 + 1.42857142857143*m.x165
                          + 1.42857142857143*m.x166 + 1.42857142857143*m.x167 == 0)

m.c166 = Constraint(expr=   3.33333333333333*m.x4 - m.x5 - m.x156 - m.x157 - m.x158 - m.x159 - m.x160 - m.x161 == 0)

m.c167 = Constraint(expr=   m.x4 - m.x5 + m.x6 - m.x156 - m.x157 - m.x158 - m.x159 - m.x160 - m.x161 + m.x168 + m.x169
                          + m.x170 + m.x171 == 0)

m.c168 = Constraint(expr=   m.x1 + m.x4 <= 5000)

m.c169 = Constraint(expr=   m.x117 - 0.1528125*m.x129 <= 0)

m.c170 = Constraint(expr=   m.x118 - 0.183125*m.x129 <= 0)

m.c171 = Constraint(expr=   m.x119 - 0.215625*m.x129 <= 0)

m.c172 = Constraint(expr=   m.x120 - 0.220625*m.x129 <= 0)

m.c173 = Constraint(expr=   m.x121 - 0.2075*m.x129 <= 0)

m.c174 = Constraint(expr=   m.x122 - 0.1753125*m.x129 <= 0)

m.c175 = Constraint(expr=   m.x123 - 0.165625*m.x129 <= 0)

m.c176 = Constraint(expr=   m.x124 - 0.1640625*m.x129 <= 0)

m.c177 = Constraint(expr=   m.x125 - 0.1521875*m.x129 <= 0)

m.c178 = Constraint(expr=   m.x126 - 0.1534375*m.x129 <= 0)

m.c179 = Constraint(expr=   m.x127 - 0.1571875*m.x129 <= 0)

m.c180 = Constraint(expr=   m.x128 - 0.14625*m.x129 <= 0)

m.c181 = Constraint(expr= - 8.928*m.x117 - 8.064*m.x118 - 8.928*m.x119 - 8.64*m.x120 - 8.928*m.x121 - 8.64*m.x122
                          - 8.928*m.x123 - 8.928*m.x124 - 8.64*m.x125 - 8.928*m.x126 - 8.64*m.x127 - 8.928*m.x128
                          + m.x130 == 0)

m.c182 = Constraint(expr= - 40.7812064*m.x129 + m.x131 - 75526.6107*m.b245 == 0)

m.c183 = Constraint(expr=   m.x45 <= 64.2174432497013)

m.c184 = Constraint(expr=   m.x46 <= 71.0978835978836)

m.c185 = Constraint(expr=   m.x47 <= 256.869772998805)

m.c186 = Constraint(expr=   m.x48 <= 331.79012345679)

m.c187 = Constraint(expr=   m.x49 <= 449.522102747909)

m.c188 = Constraint(expr=   m.x50 <= 995.37037037037)

m.c189 = Constraint(expr=   m.x51 <= 642.174432497013)

m.c190 = Constraint(expr=   m.x52 <= 321.087216248507)

m.c191 = Constraint(expr=   m.x53 <= 265.432098765432)

m.c192 = Constraint(expr=   m.x54 <= 256.869772998805)

m.c193 = Constraint(expr=   m.x55 <= 199.074074074074)

m.c194 = Constraint(expr=   m.x56 <= 128.434886499403)

m.c195 = Constraint(expr=   m.x57 <= 97.0728793309438)

m.c196 = Constraint(expr=   m.x58 <= 107.473544973545)

m.c197 = Constraint(expr=   m.x59 <= 116.487455197133)

m.c198 = Constraint(expr=   m.x60 <= 130.401234567901)

m.c199 = Constraint(expr=   m.x61 <= 126.194743130227)

m.c200 = Constraint(expr=   m.x62 <= 200.617283950617)

m.c201 = Constraint(expr=   m.x63 <= 194.145758661888)

m.c202 = Constraint(expr=   m.x64 <= 194.145758661888)

m.c203 = Constraint(expr=   m.x65 <= 160.493827160494)

m.c204 = Constraint(expr=   m.x66 <= 135.902031063321)

m.c205 = Constraint(expr=   m.x67 <= 120.37037037037)

m.c206 = Constraint(expr=   m.x68 <= 97.0728793309438)

m.c207 = Constraint(expr=   m.x69 <= 228.494623655914)

m.c208 = Constraint(expr=   m.x70 <= 252.97619047619)

m.c209 = Constraint(expr=   m.x71 <= 190.412186379928)

m.c210 = Constraint(expr=   m.x72 <= 196.759259259259)

m.c211 = Constraint(expr=   m.x73 <= 175.179211469534)

m.c212 = Constraint(expr=   m.x74 <= 181.018518518519)

m.c213 = Constraint(expr=   m.x75 <= 114.247311827957)

m.c214 = Constraint(expr=   m.x76 <= 114.247311827957)

m.c215 = Constraint(expr=   m.x77 <= 157.407407407407)

m.c216 = Constraint(expr=   m.x78 <= 190.412186379928)

m.c217 = Constraint(expr=   m.x79 <= 196.759259259259)

m.c218 = Constraint(expr=   m.x80 <= 228.494623655914)

m.c219 = Constraint(expr=   m.x81 <= 206.093189964158)

m.c220 = Constraint(expr=   m.x82 <= 228.174603174603)

m.c221 = Constraint(expr=   m.x83 <= 171.744324970131)

m.c222 = Constraint(expr=   m.x84 <= 177.469135802469)

m.c223 = Constraint(expr=   m.x85 <= 158.004778972521)

m.c224 = Constraint(expr=   m.x86 <= 163.271604938272)

m.c225 = Constraint(expr=   m.x87 <= 103.046594982079)

m.c226 = Constraint(expr=   m.x88 <= 103.046594982079)

m.c227 = Constraint(expr=   m.x89 <= 141.975308641975)

m.c228 = Constraint(expr=   m.x90 <= 171.744324970131)

m.c229 = Constraint(expr=   m.x91 <= 177.469135802469)

m.c230 = Constraint(expr=   m.x92 <= 206.093189964158)

m.c231 = Constraint(expr=   m.x93 <= 75.0448028673835)

m.c232 = Constraint(expr=   m.x94 <= 91.3938492063492)

m.c233 = Constraint(expr=   m.x95 <= 90.0537634408602)

m.c234 = Constraint(expr=   m.x96 <= 108.564814814815)

m.c235 = Constraint(expr=   m.x97 <= 150.089605734767)

m.c236 = Constraint(expr=   m.x98 <= 155.092592592593)

m.c237 = Constraint(expr=   m.x99 <= 150.089605734767)

m.c238 = Constraint(expr=   m.x100 <= 150.089605734767)

m.c239 = Constraint(expr=   m.x101 <= 139.583333333333)

m.c240 = Constraint(expr=   m.x102 <= 120.071684587814)

m.c241 = Constraint(expr=   m.x103 <= 108.564814814815)

m.c242 = Constraint(expr=   m.x104 <= 90.0537634408602)

m.c243 = Constraint(expr=   m.x105 <= 110.513739545998)

m.c244 = Constraint(expr=   m.x106 <= 134.589947089947)

m.c245 = Constraint(expr=   m.x107 <= 132.616487455197)

m.c246 = Constraint(expr=   m.x108 <= 137.037037037037)

m.c247 = Constraint(expr=   m.x109 <= 165.770609318996)

m.c248 = Constraint(expr=   m.x110 <= 171.296296296296)

m.c249 = Constraint(expr=   m.x111 <= 165.770609318996)

m.c250 = Constraint(expr=   m.x112 <= 165.770609318996)

m.c251 = Constraint(expr=   m.x113 <= 159.876543209877)

m.c252 = Constraint(expr=   m.x114 <= 143.667861409797)

m.c253 = Constraint(expr=   m.x115 <= 125.617283950617)

m.c254 = Constraint(expr=   m.x116 <= 110.513739545998)

m.c255 = Constraint(expr= - 350.4*m.x1 - 219*m.x4 + m.x132 == 0)

m.c256 = Constraint(expr= - 1.8858105504*m.x21 - 1.7033127552*m.x22 - 1.8858105504*m.x23 - 1.824977952*m.x24
                          - 1.8858105504*m.x25 - 1.824977952*m.x26 - 1.8858105504*m.x27 - 1.8858105504*m.x28
                          - 1.824977952*m.x29 - 1.8858105504*m.x30 - 1.824977952*m.x31 - 1.8858105504*m.x32
                          - 1.9052503776*m.x33 - 1.7208713088*m.x34 - 1.9052503776*m.x35 - 1.843790688*m.x36
                          - 1.9052503776*m.x37 - 1.843790688*m.x38 - 1.9052503776*m.x39 - 1.9052503776*m.x40
                          - 1.843790688*m.x41 - 1.9052503776*m.x42 - 1.843790688*m.x43 - 1.9052503776*m.x44
                          - 2.6372370096*m.x45 - 2.3820205248*m.x46 - 2.6372370096*m.x47 - 2.552164848*m.x48
                          - 2.6372370096*m.x49 - 2.552164848*m.x50 - 2.6372370096*m.x51 - 2.6372370096*m.x52
                          - 2.552164848*m.x53 - 2.6372370096*m.x54 - 2.552164848*m.x55 - 2.6372370096*m.x56
                          - 2.6052180768*m.x57 - 2.3531001984*m.x58 - 2.6052180768*m.x59 - 2.521178784*m.x60
                          - 2.6052180768*m.x61 - 2.521178784*m.x62 - 2.6052180768*m.x63 - 2.6052180768*m.x64
                          - 2.521178784*m.x65 - 2.6052180768*m.x66 - 2.521178784*m.x67 - 2.6052180768*m.x68
                          - 2.516022*m.x69 - 2.272536*m.x70 - 2.516022*m.x71 - 2.43486*m.x72 - 2.516022*m.x73
                          - 2.43486*m.x74 - 2.516022*m.x75 - 2.516022*m.x76 - 2.43486*m.x77 - 2.516022*m.x78
                          - 2.43486*m.x79 - 2.516022*m.x80 - 2.516022*m.x81 - 2.272536*m.x82 - 2.516022*m.x83
                          - 2.43486*m.x84 - 2.516022*m.x85 - 2.43486*m.x86 - 2.516022*m.x87 - 2.516022*m.x88
                          - 2.43486*m.x89 - 2.516022*m.x90 - 2.43486*m.x91 - 2.516022*m.x92 - 2.2770243504*m.x93
                          - 2.0566671552*m.x94 - 2.2770243504*m.x95 - 2.203571952*m.x96 - 2.2770243504*m.x97
                          - 2.203571952*m.x98 - 2.2770243504*m.x99 - 2.2770243504*m.x100 - 2.203571952*m.x101
                          - 2.2770243504*m.x102 - 2.203571952*m.x103 - 2.2770243504*m.x104 - 2.181838032*m.x105
                          - 1.970692416*m.x106 - 2.181838032*m.x107 - 2.11145616*m.x108 - 2.181838032*m.x109
                          - 2.11145616*m.x110 - 2.181838032*m.x111 - 2.181838032*m.x112 - 2.11145616*m.x113
                          - 2.181838032*m.x114 - 2.11145616*m.x115 - 2.181838032*m.x116 - 2.964412944*m.x117
                          - 2.677534272*m.x118 - 2.964412944*m.x119 - 2.86878672*m.x120 - 2.964412944*m.x121
                          - 2.86878672*m.x122 - 2.964412944*m.x123 - 2.964412944*m.x124 - 2.86878672*m.x125
                          - 2.964412944*m.x126 - 2.86878672*m.x127 - 2.964412944*m.x128 + m.x133 == 0)

m.c257 = Constraint(expr=-(322*((1.76923076923077*m.x138/(1e-6 + (m.x192*m.x193*(0.5*m.x192 + 0.5*m.x193))**0.33333))**
                         0.83 + (1.76923076923077*m.x139/(1e-6 + (m.x193*m.x194*(0.5*m.x193 + 0.5*m.x194))**0.33333))**
                         0.83 + (3*m.x140/(1e-6 + (m.x195*m.x196*(0.5*m.x195 + 0.5*m.x196))**0.33333))**0.83 + (3*m.x141
                         /(1e-6 + (m.x196*m.x197*(0.5*m.x196 + 0.5*m.x197))**0.33333))**0.83 + (2.76923076923077*m.x142/
                         (1e-6 + (m.x198*m.x199*(0.5*m.x198 + 0.5*m.x199))**0.33333))**0.83 + (2.76923076923077*m.x143/(
                         1e-6 + (m.x199*m.x200*(0.5*m.x199 + 0.5*m.x200))**0.33333))**0.83 + (4*m.x144/(1e-6 + (m.x201*
                         m.x202*(0.5*m.x201 + 0.5*m.x202))**0.33333))**0.83 + (4*m.x145/(1e-6 + (m.x202*m.x203*(0.5*
                         m.x202 + 0.5*m.x203))**0.33333))**0.83 + (1.43589743589744*m.x146/(1e-6 + (m.x204*m.x205*(0.5*
                         m.x204 + 0.5*m.x205))**0.33333))**0.83 + (1.43589743589744*m.x147/(1e-6 + (m.x205*m.x206*(0.5*
                         m.x205 + 0.5*m.x206))**0.33333))**0.83 + (2.66666666666667*m.x148/(1e-6 + (m.x207*m.x208*(0.5*
                         m.x207 + 0.5*m.x208))**0.33333))**0.83 + (2.66666666666667*m.x149/(1e-6 + (m.x208*m.x209*(0.5*
                         m.x208 + 0.5*m.x209))**0.33333))**0.83) + 322*((3*m.x150/(1e-6 + (m.x210*m.x211*(0.5*m.x210 + 
                         0.5*m.x211))**0.33333))**0.83 + (3*m.x151/(1e-6 + (m.x211*m.x212*(0.5*m.x211 + 0.5*m.x212))**
                         0.33333))**0.83 + (4*m.x152/(1e-6 + (m.x213*m.x214*(0.5*m.x213 + 0.5*m.x214))**0.33333))**0.83
                          + (4*m.x153/(1e-6 + (m.x214*m.x215*(0.5*m.x214 + 0.5*m.x215))**0.33333))**0.83 + (
                         2.66666666666667*m.x154/(1e-6 + (m.x216*m.x217*(0.5*m.x216 + 0.5*m.x217))**0.33333))**0.83 + (
                         2.66666666666667*m.x155/(1e-6 + (m.x217*m.x218*(0.5*m.x217 + 0.5*m.x218))**0.33333))**0.83) + 
                         322*((3*m.x156/(1e-6 + (m.x219*m.x220*(0.5*m.x219 + 0.5*m.x220))**0.33333))**0.83 + (3*m.x157/(
                         1e-6 + (m.x220*m.x221*(0.5*m.x220 + 0.5*m.x221))**0.33333))**0.83 + (4*m.x158/(1e-6 + (m.x222*
                         m.x223*(0.5*m.x222 + 0.5*m.x223))**0.33333))**0.83 + (4*m.x159/(1e-6 + (m.x223*m.x224*(0.5*
                         m.x223 + 0.5*m.x224))**0.33333))**0.83 + (2.66666666666667*m.x160/(1e-6 + (m.x225*m.x226*(0.5*
                         m.x225 + 0.5*m.x226))**0.33333))**0.83 + (2.66666666666667*m.x161/(1e-6 + (m.x226*m.x227*(0.5*
                         m.x226 + 0.5*m.x227))**0.33333))**0.83) + 322*((1.4*m.x162/(1e-6 + (m.x228*m.x231*(0.5*m.x228
                          + 0.5*m.x231))**0.33333))**0.83 + (2.4*m.x163/(1e-6 + (m.x229*m.x232*(0.5*m.x229 + 0.5*m.x232)
                         )**0.33333))**0.83 + (1.06666666666667*m.x164/(1e-6 + (m.x230*m.x233*(0.5*m.x230 + 0.5*m.x233))
                         **0.33333))**0.83) + 322*((1.43478260869565*m.x165/(1e-6 + (70*m.x234*(35 + 0.5*m.x234))**
                         0.33333))**0.83 + (2.43478260869565*m.x166/(1e-6 + (30*m.x235*(15 + 0.5*m.x235))**0.33333))**
                         0.83 + (1.10144927536232*m.x167/(1e-6 + (30*m.x236*(15 + 0.5*m.x236))**0.33333))**0.83) + 322*(
                         (2.01923076923077*m.x168/(1e-6 + (m.x237*m.x238*(0.5*m.x237 + 0.5*m.x238))**0.33333))**0.83 + (
                         2.01923076923077*m.x169/(1e-6 + (m.x238*m.x239*(0.5*m.x238 + 0.5*m.x239))**0.33333))**0.83 + (
                         3.25*m.x170/(1e-6 + (m.x240*m.x241*(0.5*m.x240 + 0.5*m.x241))**0.33333))**0.83 + (3.25*m.x171/(
                         1e-6 + (m.x241*m.x242*(0.5*m.x241 + 0.5*m.x242))**0.33333))**0.83) + 322*((0.969230769230769*
                         m.x172/(1e-6 + (35*m.x243*(17.5 + 0.5*m.x243))**0.33333))**0.83 + (2.2*m.x173/(1e-6 + (220*
                         m.x244*(110 + 0.5*m.x244))**0.33333))**0.83)) + m.x134 == 0)

m.c258 = Constraint(expr=   m.x135 - 4186*m.b246 - 4186*m.b247 - 4186*m.b248 - 4186*m.b249 - 4186*m.b250 - 4186*m.b251
                          - 4186*m.b252 - 4186*m.b253 - 4186*m.b254 - 4186*m.b255 - 4186*m.b256 - 4186*m.b257
                          - 4186*m.b258 - 4186*m.b259 - 4186*m.b260 - 4186*m.b261 - 4186*m.b262 - 4186*m.b263
                          - 4186*m.b264 - 4186*m.b265 - 4186*m.b266 - 4186*m.b267 - 4186*m.b268 - 4186*m.b269
                          - 4186*m.b270 - 4186*m.b271 - 4186*m.b272 - 4186*m.b273 - 4186*m.b274 - 4186*m.b275
                          - 4186*m.b276 - 4186*m.b277 - 4186*m.b278 - 4186*m.b279 - 4186*m.b280 - 4186*m.b281
                          - 4186*m.b282 - 4186*m.b283 - 4186*m.b284 - 4186*m.b285 - 4186*m.b286 - 4186*m.b287
                          - 4186*m.b288 - 4186*m.b289 == 0)

m.c259 = Constraint(expr= - 10*m.x3 - 10*m.x6 + m.x136 - 10*m.x162 - 10*m.x163 - 10*m.x164 == 0)

m.c260 = Constraint(expr= - 4.16732256*m.x9 - 3.76403328*m.x10 - 4.16732256*m.x11 - 4.0328928*m.x12 - 4.16732256*m.x13
                          - 4.0328928*m.x14 - 4.16732256*m.x15 - 4.16732256*m.x16 - 4.0328928*m.x17 - 4.16732256*m.x18
                          - 4.0328928*m.x19 - 4.16732256*m.x20 - 48.86660448*m.x21 - 44.13757824*m.x22
                          - 48.86660448*m.x23 - 47.2902624*m.x24 - 48.86660448*m.x25 - 47.2902624*m.x26
                          - 48.86660448*m.x27 - 48.86660448*m.x28 - 47.2902624*m.x29 - 48.86660448*m.x30
                          - 47.2902624*m.x31 - 48.86660448*m.x32 - 15.62819616*m.x33 - 14.11579008*m.x34
                          - 15.62819616*m.x35 - 15.1240608*m.x36 - 15.62819616*m.x37 - 15.1240608*m.x38
                          - 15.62819616*m.x39 - 15.62819616*m.x40 - 15.1240608*m.x41 - 15.62819616*m.x42
                          - 15.1240608*m.x43 - 15.62819616*m.x44 - 5.43795552*m.x45 - 4.91170176*m.x46
                          - 5.43795552*m.x47 - 5.2625376*m.x48 - 5.43795552*m.x49 - 5.2625376*m.x50 - 5.43795552*m.x51
                          - 5.43795552*m.x52 - 5.2625376*m.x53 - 5.43795552*m.x54 - 5.2625376*m.x55 - 5.43795552*m.x56
                          - 22.87032192*m.x57 - 20.65706496*m.x58 - 22.87032192*m.x59 - 22.1325696*m.x60
                          - 22.87032192*m.x61 - 22.1325696*m.x62 - 22.87032192*m.x63 - 22.87032192*m.x64
                          - 22.1325696*m.x65 - 22.87032192*m.x66 - 22.1325696*m.x67 - 22.87032192*m.x68
                          - 6.78492288*m.x69 - 6.12831744*m.x70 - 6.78492288*m.x71 - 6.5660544*m.x72 - 6.78492288*m.x73
                          - 6.5660544*m.x74 - 6.78492288*m.x75 - 6.78492288*m.x76 - 6.5660544*m.x77 - 6.78492288*m.x78
                          - 6.5660544*m.x79 - 6.78492288*m.x80 - 7.760664*m.x81 - 7.009632*m.x82 - 7.760664*m.x83
                          - 7.51032*m.x84 - 7.760664*m.x85 - 7.51032*m.x86 - 7.760664*m.x87 - 7.760664*m.x88
                          - 7.51032*m.x89 - 7.760664*m.x90 - 7.51032*m.x91 - 7.760664*m.x92 - 83.85856128*m.x93
                          - 75.74321664*m.x94 - 83.85856128*m.x95 - 81.1534464*m.x96 - 83.85856128*m.x97
                          - 81.1534464*m.x98 - 83.85856128*m.x99 - 83.85856128*m.x100 - 81.1534464*m.x101
                          - 83.85856128*m.x102 - 81.1534464*m.x103 - 83.85856128*m.x104 - 38.62574208*m.x105
                          - 34.88776704*m.x106 - 38.62574208*m.x107 - 37.3797504*m.x108 - 38.62574208*m.x109
                          - 37.3797504*m.x110 - 38.62574208*m.x111 - 38.62574208*m.x112 - 37.3797504*m.x113
                          - 38.62574208*m.x114 - 37.3797504*m.x115 - 38.62574208*m.x116 - m.x130 - m.x131 + m.x137 == 0)

m.c261 = Constraint(expr= - 0.5928825888*m.x9 - 0.5355068544*m.x10 - 0.5928825888*m.x11 - 0.573757344*m.x12
                          - 0.5928825888*m.x13 - 0.573757344*m.x14 - 0.5928825888*m.x15 - 0.5928825888*m.x16
                          - 0.573757344*m.x17 - 0.5928825888*m.x18 - 0.573757344*m.x19 - 0.5928825888*m.x20
                          - 0.21572047872*m.x21 - 0.19484430336*m.x22 - 0.21572047872*m.x23 - 0.2087617536*m.x24
                          - 0.21572047872*m.x25 - 0.2087617536*m.x26 - 0.21572047872*m.x27 - 0.21572047872*m.x28
                          - 0.2087617536*m.x29 - 0.21572047872*m.x30 - 0.2087617536*m.x31 - 0.21572047872*m.x32
                          - 0.21183251328*m.x33 - 0.19133259264*m.x34 - 0.21183251328*m.x35 - 0.2049992064*m.x36
                          - 0.21183251328*m.x37 - 0.2049992064*m.x38 - 0.21183251328*m.x39 - 0.21183251328*m.x40
                          - 0.2049992064*m.x41 - 0.21183251328*m.x42 - 0.2049992064*m.x43 - 0.21183251328*m.x44
                          - 0.06543518688*m.x45 - 0.05910274944*m.x46 - 0.06543518688*m.x47 - 0.0633243744*m.x48
                          - 0.06543518688*m.x49 - 0.0633243744*m.x50 - 0.06543518688*m.x51 - 0.06543518688*m.x52
                          - 0.0633243744*m.x53 - 0.06543518688*m.x54 - 0.0633243744*m.x55 - 0.06543518688*m.x56
                          - 0.07183897344*m.x57 - 0.06488681472*m.x58 - 0.07183897344*m.x59 - 0.0695215872*m.x60
                          - 0.07183897344*m.x61 - 0.0695215872*m.x62 - 0.07183897344*m.x63 - 0.07183897344*m.x64
                          - 0.0695215872*m.x65 - 0.07183897344*m.x66 - 0.0695215872*m.x67 - 0.07183897344*m.x68
                          - 0.0896781888*m.x69 - 0.0809996544*m.x70 - 0.0896781888*m.x71 - 0.086785344*m.x72
                          - 0.0896781888*m.x73 - 0.086785344*m.x74 - 0.0896781888*m.x75 - 0.0896781888*m.x76
                          - 0.086785344*m.x77 - 0.0896781888*m.x78 - 0.086785344*m.x79 - 0.0896781888*m.x80
                          - 0.0896781888*m.x81 - 0.0809996544*m.x82 - 0.0896781888*m.x83 - 0.086785344*m.x84
                          - 0.0896781888*m.x85 - 0.086785344*m.x86 - 0.0896781888*m.x87 - 0.0896781888*m.x88
                          - 0.086785344*m.x89 - 0.0896781888*m.x90 - 0.086785344*m.x91 - 0.0896781888*m.x92
                          - 0.13747771872*m.x93 - 0.12417342336*m.x94 - 0.13747771872*m.x95 - 0.1330429536*m.x96
                          - 0.13747771872*m.x97 - 0.1330429536*m.x98 - 0.13747771872*m.x99 - 0.13747771872*m.x100
                          - 0.1330429536*m.x101 - 0.13747771872*m.x102 - 0.1330429536*m.x103 - 0.13747771872*m.x104
                          - 0.1565149824*m.x105 - 0.1413683712*m.x106 - 0.1565149824*m.x107 - 0.151466112*m.x108
                          - 0.1565149824*m.x109 - 0.151466112*m.x110 - 0.1565149824*m.x111 - 0.1565149824*m.x112
                          - 0.151466112*m.x113 - 0.1565149824*m.x114 - 0.151466112*m.x115 - 0.1565149824*m.x116 + m.x291
                          == 0)

m.c262 = Constraint(expr= - 2.846630304E-5*m.x9 - 2.571149952E-5*m.x10 - 2.846630304E-5*m.x11 - 2.75480352E-5*m.x12
                          - 2.846630304E-5*m.x13 - 2.75480352E-5*m.x14 - 2.846630304E-5*m.x15 - 2.846630304E-5*m.x16
                          - 2.75480352E-5*m.x17 - 2.846630304E-5*m.x18 - 2.75480352E-5*m.x19 - 2.846630304E-5*m.x20
                          - 4.866036768E-5*m.x21 - 4.395129984E-5*m.x22 - 4.866036768E-5*m.x23 - 4.70906784E-5*m.x24
                          - 4.866036768E-5*m.x25 - 4.70906784E-5*m.x26 - 4.866036768E-5*m.x27 - 4.866036768E-5*m.x28
                          - 4.70906784E-5*m.x29 - 4.866036768E-5*m.x30 - 4.70906784E-5*m.x31 - 4.866036768E-5*m.x32
                          - 0.00014073143904*m.x33 - 0.00012711226752*m.x34 - 0.00014073143904*m.x35
                          - 0.0001361917152*m.x36 - 0.00014073143904*m.x37 - 0.0001361917152*m.x38
                          - 0.00014073143904*m.x39 - 0.00014073143904*m.x40 - 0.0001361917152*m.x41
                          - 0.00014073143904*m.x42 - 0.0001361917152*m.x43 - 0.00014073143904*m.x44 - 0.1793563776*m.x45
                          - 0.1619993088*m.x46 - 0.1793563776*m.x47 - 0.173570688*m.x48 - 0.1793563776*m.x49
                          - 0.173570688*m.x50 - 0.1793563776*m.x51 - 0.1793563776*m.x52 - 0.173570688*m.x53
                          - 0.1793563776*m.x54 - 0.173570688*m.x55 - 0.1793563776*m.x56 - 1.4073143904*m.x57
                          - 1.2711226752*m.x58 - 1.4073143904*m.x59 - 1.361917152*m.x60 - 1.4073143904*m.x61
                          - 1.361917152*m.x62 - 1.4073143904*m.x63 - 1.4073143904*m.x64 - 1.361917152*m.x65
                          - 1.4073143904*m.x66 - 1.361917152*m.x67 - 1.4073143904*m.x68 - 0.03928971744*m.x69
                          - 0.03548748672*m.x70 - 0.03928971744*m.x71 - 0.0380223072*m.x72 - 0.03928971744*m.x73
                          - 0.0380223072*m.x74 - 0.03928971744*m.x75 - 0.03928971744*m.x76 - 0.0380223072*m.x77
                          - 0.03928971744*m.x78 - 0.0380223072*m.x79 - 0.03928971744*m.x80 - 0.14560880544*m.x81
                          - 0.13151763072*m.x82 - 0.14560880544*m.x83 - 0.1409117472*m.x84 - 0.14560880544*m.x85
                          - 0.1409117472*m.x86 - 0.14560880544*m.x87 - 0.14560880544*m.x88 - 0.1409117472*m.x89
                          - 0.14560880544*m.x90 - 0.1409117472*m.x91 - 0.14560880544*m.x92 - 6.604452288*m.x93
                          - 5.965311744*m.x94 - 6.604452288*m.x95 - 6.39140544*m.x96 - 6.604452288*m.x97
                          - 6.39140544*m.x98 - 6.604452288*m.x99 - 6.604452288*m.x100 - 6.39140544*m.x101
                          - 6.604452288*m.x102 - 6.39140544*m.x103 - 6.604452288*m.x104 - 7.699141152*m.x105
                          - 6.954062976*m.x106 - 7.699141152*m.x107 - 7.45078176*m.x108 - 7.699141152*m.x109
                          - 7.45078176*m.x110 - 7.699141152*m.x111 - 7.699141152*m.x112 - 7.45078176*m.x113
                          - 7.699141152*m.x114 - 7.45078176*m.x115 - 7.699141152*m.x116 - 0.0026662373856*m.x117
                          - 0.0024082144128*m.x118 - 0.0026662373856*m.x119 - 0.002580229728*m.x120
                          - 0.0026662373856*m.x121 - 0.002580229728*m.x122 - 0.0026662373856*m.x123
                          - 0.0026662373856*m.x124 - 0.002580229728*m.x125 - 0.0026662373856*m.x126
                          - 0.002580229728*m.x127 - 0.0026662373856*m.x128 + m.x292 == 0)
