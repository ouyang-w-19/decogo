#  MINLP written by GAMS Convert at 04/21/18 13:54:56
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        392      226       42      124        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        278      237       41        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1476      366     1110        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(None,None),initialize=0)
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
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x87 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x88 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x92 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x93 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(None,None),initialize=0)
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
m.x127 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x128 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x129 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x130 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x131 = Var(within=Reals,bounds=(None,None),initialize=0)
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
m.x145 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x146 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x147 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x148 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x149 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x150 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x151 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x152 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x153 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x154 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x155 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x156 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x157 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x158 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x159 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x160 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x161 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x162 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x163 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x164 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x165 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x166 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x167 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x168 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x169 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x170 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x171 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x172 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x173 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x174 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x175 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x176 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x177 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x178 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x179 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x180 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x181 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x182 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x183 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x184 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x185 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x186 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x187 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x188 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x189 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x190 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x191 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x192 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x193 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x194 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x195 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x196 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x197 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x198 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x199 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x200 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x201 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x202 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x203 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x204 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x205 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x206 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x207 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x208 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x209 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x210 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x211 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x212 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x213 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x214 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x215 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x216 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x217 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x218 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x219 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x220 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x221 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x222 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x223 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x224 = Var(within=Reals,bounds=(None,None),initialize=0)
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
m.x266 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x267 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x268 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x269 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x270 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x271 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x272 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x273 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x274 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x275 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x276 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x277 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=200*m.x266**2 + 200*m.x266 + 175*m.x267**2 + 175*m.x267 + 250*m.x268**2 + 300*m.x268 + 625*m.x269
                       **2 + 100*m.x269 + 250*m.x270**2 + 300*m.x270 + 83.4*m.x271**2 + 325*m.x271, sense=minimize)

m.c2 = Constraint(expr=-7.14285714285714*(m.x176*m.x207 - m.x177*m.x206)*m.b225 + m.x1 == 0)

m.c3 = Constraint(expr=-7.14285714285714*(m.x177*m.x206 - m.x176*m.x207)*m.b225 + m.x2 == 0)

m.c4 = Constraint(expr=-(0.97864768683274*(m.x191**2 + m.x221**2) - 0.97864768683274*(m.x191*m.x193 + m.x221*m.x223) + 
                       1.86832740213523*(m.x191*m.x223 - m.x193*m.x221))*m.b226 + m.x3 == 0)

m.c5 = Constraint(expr=-(0.97864768683274*(m.x193**2 + m.x223**2) - 0.97864768683274*(m.x193*m.x191 + m.x223*m.x221) + 
                       1.86832740213523*(m.x193*m.x221 - m.x191*m.x223))*m.b226 + m.x4 == 0)

m.c6 = Constraint(expr=-(4.10958904109589*(m.x170**2 + m.x200**2) - 4.10958904109589*(m.x170*m.x171 + m.x200*m.x201) + 
                       10.958904109589*(m.x170*m.x201 - m.x171*m.x200))*m.b227 + m.x5 == 0)

m.c7 = Constraint(expr=-(4.10958904109589*(m.x171**2 + m.x201**2) - 4.10958904109589*(m.x171*m.x170 + m.x201*m.x200) + 
                       10.958904109589*(m.x171*m.x200 - m.x170*m.x201))*m.b227 + m.x6 == 0)

m.c8 = Constraint(expr=-(2.48868778280543*(m.x178**2 + m.x208**2) - 2.48868778280543*(m.x178*m.x179 + m.x208*m.x209) + 
                       2.26244343891403*(m.x178*m.x209 - m.x179*m.x208))*m.b228 + m.x7 == 0)

m.c9 = Constraint(expr=-(2.48868778280543*(m.x179**2 + m.x209**2) - 2.48868778280543*(m.x179*m.x178 + m.x209*m.x208) + 
                       2.26244343891403*(m.x179*m.x208 - m.x178*m.x209))*m.b228 + m.x8 == 0)

m.c10 = Constraint(expr=-(2.55474452554745*(m.x174**2 + m.x204**2) - 2.55474452554745*(m.x174*m.x186 + m.x204*m.x216) + 
                        5.47445255474453*(m.x174*m.x216 - m.x186*m.x204))*m.b229 + m.x9 == 0)

m.c11 = Constraint(expr=-(2.55474452554745*(m.x186**2 + m.x216**2) - 2.55474452554745*(m.x186*m.x174 + m.x216*m.x204) + 
                        5.47445255474453*(m.x186*m.x204 - m.x174*m.x216))*m.b229 + m.x10 == 0)

m.c12 = Constraint(expr=-1.78571428571429*(m.x170*m.x204 - m.x174*m.x200)*m.b230 + m.x11 == 0)

m.c13 = Constraint(expr=-1.78571428571429*(m.x174*m.x200 - m.x170*m.x204)*m.b230 + m.x12 == 0)

m.c14 = Constraint(expr=-(5*(m.x170**2 + m.x200**2) - 5*(m.x170*m.x192 + m.x200*m.x222) + 15*(m.x170*m.x222 - m.x192*
                        m.x200))*m.b231 + m.x13 == 0)

m.c15 = Constraint(expr=-(5*(m.x192**2 + m.x222**2) - 5*(m.x192*m.x170 + m.x222*m.x200) + 15*(m.x192*m.x200 - m.x170*
                        m.x222))*m.b231 + m.x14 == 0)

m.c16 = Constraint(expr=-(5*(m.x165**2 + m.x195**2) - 5*(m.x165*m.x166 + m.x195*m.x196) + 15*(m.x165*m.x196 - m.x166*
                        m.x195))*m.b232 + m.x15 == 0)

m.c17 = Constraint(expr=-(5*(m.x166**2 + m.x196**2) - 5*(m.x166*m.x165 + m.x196*m.x195) + 15*(m.x166*m.x195 - m.x165*
                        m.x196))*m.b232 + m.x16 == 0)

m.c18 = Constraint(expr=-4.76190476190476*(m.x173*m.x205 - m.x175*m.x203)*m.b233 + m.x17 == 0)

m.c19 = Constraint(expr=-4.76190476190476*(m.x175*m.x203 - m.x173*m.x205)*m.b233 + m.x18 == 0)

m.c20 = Constraint(expr=-(5.88235294117647*(m.x167**2 + m.x197**2) - 5.88235294117647*(m.x167*m.x168 + m.x197*m.x198) + 
                        23.5294117647059*(m.x167*m.x198 - m.x168*m.x197))*m.b234 + m.x19 == 0)

m.c21 = Constraint(expr=-(5.88235294117647*(m.x168**2 + m.x198**2) - 5.88235294117647*(m.x168*m.x167 + m.x198*m.x197) + 
                        23.5294117647059*(m.x168*m.x197 - m.x167*m.x198))*m.b234 + m.x20 == 0)

m.c22 = Constraint(expr=-(1.46341463414634*(m.x176**2 + m.x206**2) - 1.46341463414634*(m.x176*m.x178 + m.x206*m.x208) + 
                        3.17073170731707*(m.x176*m.x208 - m.x178*m.x206))*m.b235 + m.x21 == 0)

m.c23 = Constraint(expr=-(1.46341463414634*(m.x178**2 + m.x208**2) - 1.46341463414634*(m.x178*m.x176 + m.x208*m.x206) + 
                        3.17073170731707*(m.x178*m.x206 - m.x176*m.x208))*m.b235 + m.x22 == 0)

m.c24 = Constraint(expr=-(1.31034482758621*(m.x188**2 + m.x218**2) - 1.31034482758621*(m.x188*m.x189 + m.x218*m.x219) + 
                        2.27586206896552*(m.x188*m.x219 - m.x189*m.x218))*m.b236 + m.x23 == 0)

m.c25 = Constraint(expr=-(1.31034482758621*(m.x189**2 + m.x219**2) - 1.31034482758621*(m.x189*m.x188 + m.x219*m.x218) + 
                        2.27586206896552*(m.x189*m.x218 - m.x188*m.x219))*m.b236 + m.x24 == 0)

m.c26 = Constraint(expr=-(1.44766146993318*(m.x187**2 + m.x217**2) - 1.44766146993318*(m.x187*m.x188 + m.x217*m.x218) + 
                        3.00668151447661*(m.x187*m.x218 - m.x188*m.x217))*m.b237 + m.x25 == 0)

m.c27 = Constraint(expr=-(1.44766146993318*(m.x188**2 + m.x218**2) - 1.44766146993318*(m.x188*m.x187 + m.x218*m.x217) + 
                        3.00668151447661*(m.x188*m.x217 - m.x187*m.x218))*m.b237 + m.x26 == 0)

m.c28 = Constraint(expr=-(1.17647058823529*(m.x166**2 + m.x196**2) - 1.17647058823529*(m.x166*m.x169 + m.x196*m.x199) + 
                        4.70588235294118*(m.x166*m.x199 - m.x169*m.x196))*m.b238 + m.x27 == 0)

m.c29 = Constraint(expr=-(1.17647058823529*(m.x169**2 + m.x199**2) - 1.17647058823529*(m.x169*m.x166 + m.x199*m.x196) + 
                        4.70588235294118*(m.x169*m.x196 - m.x166*m.x199))*m.b238 + m.x28 == 0)

m.c30 = Constraint(expr=-(5.17241379310345*(m.x183**2 + m.x213**2) - 5.17241379310345*(m.x183*m.x184 + m.x213*m.x214) + 
                        12.0689655172414*(m.x183*m.x214 - m.x184*m.x213))*m.b239 + m.x29 == 0)

m.c31 = Constraint(expr=-(5.17241379310345*(m.x184**2 + m.x214**2) - 5.17241379310345*(m.x184*m.x183 + m.x214*m.x213) + 
                        12.0689655172414*(m.x184*m.x213 - m.x183*m.x214))*m.b239 + m.x30 == 0)

m.c32 = Constraint(expr=-3.84615384615385*(m.x168*m.x206 - m.x176*m.x198)*m.b240 + m.x31 == 0)

m.c33 = Constraint(expr=-3.84615384615385*(m.x176*m.x198 - m.x168*m.x206)*m.b240 + m.x32 == 0)

m.c34 = Constraint(expr=-(5.17241379310345*(m.x174**2 + m.x204**2) - 5.17241379310345*(m.x174*m.x185 + m.x204*m.x215) + 
                        12.0689655172414*(m.x174*m.x215 - m.x185*m.x204))*m.b241 + m.x33 == 0)

m.c35 = Constraint(expr=-(5.17241379310345*(m.x185**2 + m.x215**2) - 5.17241379310345*(m.x185*m.x174 + m.x215*m.x204) + 
                        12.0689655172414*(m.x185*m.x204 - m.x174*m.x215))*m.b241 + m.x34 == 0)

m.c36 = Constraint(expr=-9.09090909090909*(m.x173*m.x204 - m.x174*m.x203)*m.b242 + m.x35 == 0)

m.c37 = Constraint(expr=-9.09090909090909*(m.x174*m.x203 - m.x173*m.x204)*m.b242 + m.x36 == 0)

m.c38 = Constraint(expr=-(3.21100917431193*(m.x176**2 + m.x206**2) - 3.21100917431193*(m.x176*m.x179 + m.x206*m.x209) + 
                        5.96330275229358*(m.x176*m.x209 - m.x179*m.x206))*m.b243 + m.x37 == 0)

m.c39 = Constraint(expr=-(3.21100917431193*(m.x179**2 + m.x209**2) - 3.21100917431193*(m.x179*m.x176 + m.x209*m.x206) + 
                        5.96330275229358*(m.x179*m.x206 - m.x176*m.x209))*m.b243 + m.x38 == 0)

m.c40 = Constraint(expr=-(2.92682926829268*(m.x182**2 + m.x212**2) - 2.92682926829268*(m.x182*m.x183 + m.x212*m.x213) + 
                        6.34146341463415*(m.x182*m.x213 - m.x183*m.x212))*m.b244 + m.x39 == 0)

m.c41 = Constraint(expr=-(2.92682926829268*(m.x183**2 + m.x213**2) - 2.92682926829268*(m.x183*m.x182 + m.x213*m.x212) + 
                        6.34146341463415*(m.x183*m.x212 - m.x182*m.x213))*m.b244 + m.x40 == 0)

m.c42 = Constraint(expr=-2.5*(m.x192*m.x221 - m.x191*m.x222)*m.b245 + m.x41 == 0)

m.c43 = Constraint(expr=-2.5*(m.x191*m.x222 - m.x192*m.x221)*m.b245 + m.x42 == 0)

m.c44 = Constraint(expr=-(5.88235294117647*(m.x170**2 + m.x200**2) - 5.88235294117647*(m.x170*m.x172 + m.x200*m.x202) + 
                        23.5294117647059*(m.x170*m.x202 - m.x172*m.x200))*m.b246 + m.x43 == 0)

m.c45 = Constraint(expr=-(5.88235294117647*(m.x172**2 + m.x202**2) - 5.88235294117647*(m.x172*m.x170 + m.x202*m.x200) + 
                        23.5294117647059*(m.x172*m.x200 - m.x170*m.x202))*m.b246 + m.x44 == 0)

m.c46 = Constraint(expr=-(1.95729537366548*(m.x189**2 + m.x219**2) - 1.95729537366548*(m.x189*m.x191 + m.x219*m.x221) + 
                        3.73665480427046*(m.x189*m.x221 - m.x191*m.x219))*m.b247 + m.x45 == 0)

m.c47 = Constraint(expr=-(1.95729537366548*(m.x191**2 + m.x221**2) - 1.95729537366548*(m.x191*m.x189 + m.x221*m.x219) + 
                        3.73665480427046*(m.x191*m.x219 - m.x189*m.x221))*m.b247 + m.x46 == 0)

m.c48 = Constraint(expr=-(2.95857988165681*(m.x169**2 + m.x199**2) - 2.95857988165681*(m.x169*m.x171 + m.x199*m.x201) + 
                        7.10059171597633*(m.x169*m.x201 - m.x171*m.x199))*m.b248 + m.x47 == 0)

m.c49 = Constraint(expr=-(2.95857988165681*(m.x171**2 + m.x201**2) - 2.95857988165681*(m.x171*m.x169 + m.x201*m.x199) + 
                        7.10059171597633*(m.x171*m.x199 - m.x169*m.x201))*m.b248 + m.x48 == 0)

m.c50 = Constraint(expr=-(20*(m.x185**2 + m.x215**2) - 20*(m.x185*m.x186 + m.x215*m.x216) + 40*(m.x185*m.x216 - m.x186*
                        m.x215))*m.b249 + m.x49 == 0)

m.c51 = Constraint(expr=-(20*(m.x186**2 + m.x216**2) - 20*(m.x186*m.x185 + m.x216*m.x215) + 40*(m.x186*m.x215 - m.x185*
                        m.x216))*m.b249 + m.x50 == 0)

m.c52 = Constraint(expr=-(5.88235294117647*(m.x168**2 + m.x198**2) - 5.88235294117647*(m.x168*m.x170 + m.x198*m.x200) + 
                        23.5294117647059*(m.x168*m.x200 - m.x170*m.x198))*m.b250 + m.x51 == 0)

m.c53 = Constraint(expr=-(5.88235294117647*(m.x170**2 + m.x200**2) - 5.88235294117647*(m.x170*m.x168 + m.x200*m.x198) + 
                        23.5294117647059*(m.x170*m.x198 - m.x168*m.x200))*m.b250 + m.x52 == 0)

m.c54 = Constraint(expr=-(1.72413793103448*(m.x174**2 + m.x204**2) - 1.72413793103448*(m.x174*m.x184 + m.x204*m.x214) + 
                        4.02298850574713*(m.x174*m.x214 - m.x184*m.x204))*m.b251 + m.x53 == 0)

m.c55 = Constraint(expr=-(1.72413793103448*(m.x184**2 + m.x214**2) - 1.72413793103448*(m.x184*m.x174 + m.x214*m.x204) + 
                        4.02298850574713*(m.x184*m.x204 - m.x174*m.x214))*m.b251 + m.x54 == 0)

m.c56 = Constraint(expr=-(2.56410256410256*(m.x186**2 + m.x216**2) - 2.56410256410256*(m.x186*m.x188 + m.x216*m.x218) + 
                        3.84615384615385*(m.x186*m.x218 - m.x188*m.x216))*m.b252 + m.x55 == 0)

m.c57 = Constraint(expr=-(2.56410256410256*(m.x188**2 + m.x218**2) - 2.56410256410256*(m.x188*m.x186 + m.x218*m.x216) + 
                        3.84615384615385*(m.x188*m.x216 - m.x186*m.x218))*m.b252 + m.x56 == 0)

m.c58 = Constraint(expr=-(0.69204152249135*(m.x191**2 + m.x221**2) - 0.69204152249135*(m.x191*m.x194 + m.x221*m.x224) + 
                        1.29757785467128*(m.x191*m.x224 - m.x194*m.x221))*m.b253 + m.x57 == 0)

m.c59 = Constraint(expr=-(0.69204152249135*(m.x194**2 + m.x224**2) - 0.69204152249135*(m.x194*m.x191 + m.x224*m.x221) + 
                        1.29757785467128*(m.x194*m.x221 - m.x191*m.x224))*m.b253 + m.x58 == 0)

m.c60 = Constraint(expr=-(4.10958904109589*(m.x174**2 + m.x204**2) - 4.10958904109589*(m.x174*m.x181 + m.x204*m.x211) + 
                        10.958904109589*(m.x174*m.x211 - m.x181*m.x204))*m.b254 + m.x59 == 0)

m.c61 = Constraint(expr=-(4.10958904109589*(m.x181**2 + m.x211**2) - 4.10958904109589*(m.x181*m.x174 + m.x211*m.x204) + 
                        10.958904109589*(m.x181*m.x204 - m.x174*m.x211))*m.b254 + m.x60 == 0)

m.c62 = Constraint(expr=-(1.37614678899083*(m.x172**2 + m.x202**2) - 1.37614678899083*(m.x172*m.x192 + m.x202*m.x222) + 
                        4.58715596330275*(m.x172*m.x222 - m.x192*m.x202))*m.b255 + m.x61 == 0)

m.c63 = Constraint(expr=-(1.37614678899083*(m.x192**2 + m.x222**2) - 1.37614678899083*(m.x192*m.x172 + m.x222*m.x202) + 
                        4.58715596330275*(m.x192*m.x202 - m.x172*m.x222))*m.b255 + m.x62 == 0)

m.c64 = Constraint(expr=-(1.87110187110187*(m.x176**2 + m.x206**2) - 1.87110187110187*(m.x176*m.x180 + m.x206*m.x210) + 
                        4.15800415800416*(m.x176*m.x210 - m.x180*m.x206))*m.b256 + m.x63 == 0)

m.c65 = Constraint(expr=-(1.87110187110187*(m.x180**2 + m.x210**2) - 1.87110187110187*(m.x180*m.x176 + m.x210*m.x206) + 
                        4.15800415800416*(m.x180*m.x206 - m.x176*m.x210))*m.b256 + m.x64 == 0)

m.c66 = Constraint(expr=-4.76190476190476*(m.x170*m.x203 - m.x173*m.x200)*m.b257 + m.x65 == 0)

m.c67 = Constraint(expr=-4.76190476190476*(m.x173*m.x200 - m.x170*m.x203)*m.b257 + m.x66 == 0)

m.c68 = Constraint(expr=-(2*(m.x179**2 + m.x209**2) - 2*(m.x179*m.x187 + m.x209*m.x217) + 4*(m.x179*m.x217 - m.x187*
                        m.x209))*m.b258 + m.x67 == 0)

m.c69 = Constraint(expr=-(2*(m.x187**2 + m.x217**2) - 2*(m.x187*m.x179 + m.x217*m.x209) + 4*(m.x187*m.x209 - m.x179*
                        m.x217))*m.b258 + m.x68 == 0)

m.c70 = Constraint(expr=-(1.20831319478009*(m.x189**2 + m.x219**2) - 1.20831319478009*(m.x189*m.x190 + m.x219*m.x220) + 
                        1.83663605606573*(m.x189*m.x220 - m.x190*m.x219))*m.b259 + m.x69 == 0)

m.c71 = Constraint(expr=-(1.20831319478009*(m.x190**2 + m.x220**2) - 1.20831319478009*(m.x190*m.x189 + m.x220*m.x219) + 
                        1.83663605606573*(m.x190*m.x219 - m.x189*m.x220))*m.b259 + m.x70 == 0)

m.c72 = Constraint(expr=-(1.81818181818182*(m.x179**2 + m.x209**2) - 1.81818181818182*(m.x179*m.x182 + m.x209*m.x212) + 
                        3.63636363636364*(m.x179*m.x212 - m.x182*m.x209))*m.b260 + m.x71 == 0)

m.c73 = Constraint(expr=-(1.81818181818182*(m.x182**2 + m.x212**2) - 1.81818181818182*(m.x182*m.x179 + m.x212*m.x209) + 
                        3.63636363636364*(m.x182*m.x209 - m.x179*m.x212))*m.b260 + m.x72 == 0)

m.c74 = Constraint(expr=-(1.88235294117647*(m.x180**2 + m.x210**2) - 1.88235294117647*(m.x180*m.x181 + m.x210*m.x211) + 
                        4.47058823529412*(m.x180*m.x211 - m.x181*m.x210))*m.b261 + m.x73 == 0)

m.c75 = Constraint(expr=-(1.88235294117647*(m.x181**2 + m.x211**2) - 1.88235294117647*(m.x181*m.x180 + m.x211*m.x210) + 
                        4.47058823529412*(m.x181*m.x210 - m.x180*m.x211))*m.b261 + m.x74 == 0)

m.c76 = Constraint(expr=-(1.66666666666667*(m.x166**2 + m.x196**2) - 1.66666666666667*(m.x166*m.x170 + m.x196*m.x200) + 
                        5*(m.x166*m.x200 - m.x170*m.x196))*m.b262 + m.x75 == 0)

m.c77 = Constraint(expr=-(1.66666666666667*(m.x170**2 + m.x200**2) - 1.66666666666667*(m.x170*m.x166 + m.x200*m.x196) + 
                        5*(m.x170*m.x196 - m.x166*m.x200))*m.b262 + m.x76 == 0)

m.c78 = Constraint(expr=-(1.84615384615385*(m.x166**2 + m.x196**2) - 1.84615384615385*(m.x166*m.x168 + m.x196*m.x198) + 
                        5.23076923076923*(m.x166*m.x198 - m.x168*m.x196))*m.b263 + m.x77 == 0)

m.c79 = Constraint(expr=-(1.84615384615385*(m.x168**2 + m.x198**2) - 1.84615384615385*(m.x168*m.x166 + m.x198*m.x196) + 
                        5.23076923076923*(m.x168*m.x196 - m.x166*m.x198))*m.b263 + m.x78 == 0)

m.c80 = Constraint(expr=-(1.29533678756477*(m.x165**2 + m.x195**2) - 1.29533678756477*(m.x165*m.x167 + m.x195*m.x197) + 
                        4.92227979274611*(m.x165*m.x197 - m.x167*m.x195))*m.b264 + m.x79 == 0)

m.c81 = Constraint(expr=-(1.29533678756477*(m.x167**2 + m.x197**2) - 1.29533678756477*(m.x167*m.x165 + m.x197*m.x195) + 
                        4.92227979274611*(m.x167*m.x195 - m.x165*m.x197))*m.b264 + m.x80 == 0)

m.c82 = Constraint(expr=-(0.922722029988466*(m.x193**2 + m.x223**2) - 0.922722029988466*(m.x193*m.x194 + m.x223*m.x224)
                         + 1.73010380622837*(m.x193*m.x224 - m.x194*m.x223))*m.b265 + m.x81 == 0)

m.c83 = Constraint(expr=-(0.922722029988466*(m.x194**2 + m.x224**2) - 0.922722029988466*(m.x194*m.x193 + m.x224*m.x223)
                         + 1.73010380622837*(m.x194*m.x223 - m.x193*m.x224))*m.b265 + m.x82 == 0)

m.c84 = Constraint(expr=-(7.14285714285714*(m.x176**2 + m.x206**2) - 7.14285714285714*(m.x176*m.x177 + m.x206*m.x207))*
                        m.b225 + m.x83 == 0)

m.c85 = Constraint(expr=-(7.14285714285714*(m.x177**2 + m.x207**2) - 7.14285714285714*(m.x177*m.x176 + m.x207*m.x206))*
                        m.b225 + m.x84 == 0)

m.c86 = Constraint(expr=-(1.86832740213523*(m.x191**2 + m.x221**2) - 1.86832740213523*(m.x191*m.x193 + m.x221*m.x223) - 
                        0.97864768683274*(m.x191*m.x223 - m.x193*m.x221))*m.b226 + m.x85 == 0)

m.c87 = Constraint(expr=-(1.86832740213523*(m.x193**2 + m.x223**2) - 1.86832740213523*(m.x193*m.x191 + m.x223*m.x221) - 
                        0.97864768683274*(m.x193*m.x221 - m.x191*m.x223))*m.b226 + m.x86 == 0)

m.c88 = Constraint(expr=-(10.953904109589*(m.x170**2 + m.x200**2) - 10.958904109589*(m.x170*m.x171 + m.x200*m.x201) - 
                        4.10958904109589*(m.x170*m.x201 - m.x171*m.x200))*m.b227 + m.x87 == 0)

m.c89 = Constraint(expr=-(10.953904109589*(m.x171**2 + m.x201**2) - 10.958904109589*(m.x171*m.x170 + m.x201*m.x200) - 
                        4.10958904109589*(m.x171*m.x200 - m.x170*m.x201))*m.b227 + m.x88 == 0)

m.c90 = Constraint(expr=-(2.26244343891403*(m.x178**2 + m.x208**2) - 2.26244343891403*(m.x178*m.x179 + m.x208*m.x209) - 
                        2.48868778280543*(m.x178*m.x209 - m.x179*m.x208))*m.b228 + m.x89 == 0)

m.c91 = Constraint(expr=-(2.26244343891403*(m.x179**2 + m.x209**2) - 2.26244343891403*(m.x179*m.x178 + m.x209*m.x208) - 
                        2.48868778280543*(m.x179*m.x208 - m.x178*m.x209))*m.b228 + m.x90 == 0)

m.c92 = Constraint(expr=-(5.47445255474453*(m.x174**2 + m.x204**2) - 5.47445255474453*(m.x174*m.x186 + m.x204*m.x216) - 
                        2.55474452554745*(m.x174*m.x216 - m.x186*m.x204))*m.b229 + m.x91 == 0)

m.c93 = Constraint(expr=-(5.47445255474453*(m.x186**2 + m.x216**2) - 5.47445255474453*(m.x186*m.x174 + m.x216*m.x204) - 
                        2.55474452554745*(m.x186*m.x204 - m.x174*m.x216))*m.b229 + m.x92 == 0)

m.c94 = Constraint(expr=-(1.78571428571429*(m.x170**2 + m.x200**2) - 1.78571428571429*(m.x170*m.x174 + m.x200*m.x204))*
                        m.b230 + m.x93 == 0)

m.c95 = Constraint(expr=-(1.78571428571429*(m.x174**2 + m.x204**2) - 1.78571428571429*(m.x174*m.x170 + m.x204*m.x200))*
                        m.b230 + m.x94 == 0)

m.c96 = Constraint(expr=-(14.995*(m.x170**2 + m.x200**2) - 15*(m.x170*m.x192 + m.x200*m.x222) - 5*(m.x170*m.x222 - 
                        m.x192*m.x200))*m.b231 + m.x95 == 0)

m.c97 = Constraint(expr=-(14.995*(m.x192**2 + m.x222**2) - 15*(m.x192*m.x170 + m.x222*m.x200) - 5*(m.x192*m.x200 - 
                        m.x170*m.x222))*m.b231 + m.x96 == 0)

m.c98 = Constraint(expr=-(14.985*(m.x165**2 + m.x195**2) - 15*(m.x165*m.x166 + m.x195*m.x196) - 5*(m.x165*m.x196 - 
                        m.x166*m.x195))*m.b232 + m.x97 == 0)

m.c99 = Constraint(expr=-(14.985*(m.x166**2 + m.x196**2) - 15*(m.x166*m.x165 + m.x196*m.x195) - 5*(m.x166*m.x195 - 
                        m.x165*m.x196))*m.b232 + m.x98 == 0)

m.c100 = Constraint(expr=-(4.76190476190476*(m.x173**2 + m.x203**2) - 4.76190476190476*(m.x173*m.x175 + m.x203*m.x205))*
                         m.b233 + m.x99 == 0)

m.c101 = Constraint(expr=-(4.76190476190476*(m.x175**2 + m.x205**2) - 4.76190476190476*(m.x175*m.x173 + m.x205*m.x203))*
                         m.b233 + m.x100 == 0)

m.c102 = Constraint(expr=-(23.5294117647059*(m.x167**2 + m.x197**2) - 23.5294117647059*(m.x167*m.x168 + m.x197*m.x198)
                          - 5.88235294117647*(m.x167*m.x198 - m.x168*m.x197))*m.b234 + m.x101 == 0)

m.c103 = Constraint(expr=-(23.5294117647059*(m.x168**2 + m.x198**2) - 23.5294117647059*(m.x168*m.x167 + m.x198*m.x197)
                          - 5.88235294117647*(m.x168*m.x197 - m.x167*m.x198))*m.b234 + m.x102 == 0)

m.c104 = Constraint(expr=-(3.17073170731707*(m.x176**2 + m.x206**2) - 3.17073170731707*(m.x176*m.x178 + m.x206*m.x208)
                          - 1.46341463414634*(m.x176*m.x208 - m.x178*m.x206))*m.b235 + m.x103 == 0)

m.c105 = Constraint(expr=-(3.17073170731707*(m.x178**2 + m.x208**2) - 3.17073170731707*(m.x178*m.x176 + m.x208*m.x206)
                          - 1.46341463414634*(m.x178*m.x206 - m.x176*m.x208))*m.b235 + m.x104 == 0)

m.c106 = Constraint(expr=-(2.27586206896552*(m.x188**2 + m.x218**2) - 2.27586206896552*(m.x188*m.x189 + m.x218*m.x219)
                          - 1.31034482758621*(m.x188*m.x219 - m.x189*m.x218))*m.b236 + m.x105 == 0)

m.c107 = Constraint(expr=-(2.27586206896552*(m.x189**2 + m.x219**2) - 2.27586206896552*(m.x189*m.x188 + m.x219*m.x218)
                          - 1.31034482758621*(m.x189*m.x218 - m.x188*m.x219))*m.b236 + m.x106 == 0)

m.c108 = Constraint(expr=-(3.00668151447661*(m.x187**2 + m.x217**2) - 3.00668151447661*(m.x187*m.x188 + m.x217*m.x218)
                          - 1.44766146993318*(m.x187*m.x218 - m.x188*m.x217))*m.b237 + m.x107 == 0)

m.c109 = Constraint(expr=-(3.00668151447661*(m.x188**2 + m.x218**2) - 3.00668151447661*(m.x188*m.x187 + m.x218*m.x217)
                          - 1.44766146993318*(m.x188*m.x217 - m.x187*m.x218))*m.b237 + m.x108 == 0)

m.c110 = Constraint(expr=-(4.69588235294118*(m.x166**2 + m.x196**2) - 4.70588235294118*(m.x166*m.x169 + m.x196*m.x199)
                          - 1.17647058823529*(m.x166*m.x199 - m.x169*m.x196))*m.b238 + m.x109 == 0)

m.c111 = Constraint(expr=-(4.69588235294118*(m.x169**2 + m.x199**2) - 4.70588235294118*(m.x169*m.x166 + m.x199*m.x196)
                          - 1.17647058823529*(m.x169*m.x196 - m.x166*m.x199))*m.b238 + m.x110 == 0)

m.c112 = Constraint(expr=-(12.0689655172414*(m.x183**2 + m.x213**2) - 12.0689655172414*(m.x183*m.x184 + m.x213*m.x214)
                          - 5.17241379310345*(m.x183*m.x214 - m.x184*m.x213))*m.b239 + m.x111 == 0)

m.c113 = Constraint(expr=-(12.0689655172414*(m.x184**2 + m.x214**2) - 12.0689655172414*(m.x184*m.x183 + m.x214*m.x213)
                          - 5.17241379310345*(m.x184*m.x213 - m.x183*m.x214))*m.b239 + m.x112 == 0)

m.c114 = Constraint(expr=-(3.84615384615385*(m.x168**2 + m.x198**2) - 3.84615384615385*(m.x168*m.x176 + m.x198*m.x206))*
                         m.b240 + m.x113 == 0)

m.c115 = Constraint(expr=-(3.84615384615385*(m.x176**2 + m.x206**2) - 3.84615384615385*(m.x176*m.x168 + m.x206*m.x198))*
                         m.b240 + m.x114 == 0)

m.c116 = Constraint(expr=-(12.0689655172414*(m.x174**2 + m.x204**2) - 12.0689655172414*(m.x174*m.x185 + m.x204*m.x215)
                          - 5.17241379310345*(m.x174*m.x215 - m.x185*m.x204))*m.b241 + m.x115 == 0)

m.c117 = Constraint(expr=-(12.0689655172414*(m.x185**2 + m.x215**2) - 12.0689655172414*(m.x185*m.x174 + m.x215*m.x204)
                          - 5.17241379310345*(m.x185*m.x204 - m.x174*m.x215))*m.b241 + m.x116 == 0)

m.c118 = Constraint(expr=-(9.09090909090909*(m.x173**2 + m.x203**2) - 9.09090909090909*(m.x173*m.x174 + m.x203*m.x204))*
                         m.b242 + m.x117 == 0)

m.c119 = Constraint(expr=-(9.09090909090909*(m.x174**2 + m.x204**2) - 9.09090909090909*(m.x174*m.x173 + m.x204*m.x203))*
                         m.b242 + m.x118 == 0)

m.c120 = Constraint(expr=-(5.96330275229358*(m.x176**2 + m.x206**2) - 5.96330275229358*(m.x176*m.x179 + m.x206*m.x209)
                          - 3.21100917431193*(m.x176*m.x209 - m.x179*m.x206))*m.b243 + m.x119 == 0)

m.c121 = Constraint(expr=-(5.96330275229358*(m.x179**2 + m.x209**2) - 5.96330275229358*(m.x179*m.x176 + m.x209*m.x206)
                          - 3.21100917431193*(m.x179*m.x206 - m.x176*m.x209))*m.b243 + m.x120 == 0)

m.c122 = Constraint(expr=-(6.34146341463415*(m.x182**2 + m.x212**2) - 6.34146341463415*(m.x182*m.x183 + m.x212*m.x213)
                          - 2.92682926829268*(m.x182*m.x213 - m.x183*m.x212))*m.b244 + m.x121 == 0)

m.c123 = Constraint(expr=-(6.34146341463415*(m.x183**2 + m.x213**2) - 6.34146341463415*(m.x183*m.x182 + m.x213*m.x212)
                          - 2.92682926829268*(m.x183*m.x212 - m.x182*m.x213))*m.b244 + m.x122 == 0)

m.c124 = Constraint(expr=-(2.5*(m.x192**2 + m.x222**2) - 2.5*(m.x192*m.x191 + m.x222*m.x221))*m.b245 + m.x123 == 0)

m.c125 = Constraint(expr=-(2.5*(m.x191**2 + m.x221**2) - 2.5*(m.x191*m.x192 + m.x221*m.x222))*m.b245 + m.x124 == 0)

m.c126 = Constraint(expr=-(23.5294117647059*(m.x170**2 + m.x200**2) - 23.5294117647059*(m.x170*m.x172 + m.x200*m.x202)
                          - 5.88235294117647*(m.x170*m.x202 - m.x172*m.x200))*m.b246 + m.x125 == 0)

m.c127 = Constraint(expr=-(23.5294117647059*(m.x172**2 + m.x202**2) - 23.5294117647059*(m.x172*m.x170 + m.x202*m.x200)
                          - 5.88235294117647*(m.x172*m.x200 - m.x170*m.x202))*m.b246 + m.x126 == 0)

m.c128 = Constraint(expr=-(3.73665480427046*(m.x189**2 + m.x219**2) - 3.73665480427046*(m.x189*m.x191 + m.x219*m.x221)
                          - 1.95729537366548*(m.x189*m.x221 - m.x191*m.x219))*m.b247 + m.x127 == 0)

m.c129 = Constraint(expr=-(3.73665480427046*(m.x191**2 + m.x221**2) - 3.73665480427046*(m.x191*m.x189 + m.x221*m.x219)
                          - 1.95729537366548*(m.x191*m.x219 - m.x189*m.x221))*m.b247 + m.x128 == 0)

m.c130 = Constraint(expr=-(7.09559171597633*(m.x169**2 + m.x199**2) - 7.10059171597633*(m.x169*m.x171 + m.x199*m.x201)
                          - 2.95857988165681*(m.x169*m.x201 - m.x171*m.x199))*m.b248 + m.x129 == 0)

m.c131 = Constraint(expr=-(7.09559171597633*(m.x171**2 + m.x201**2) - 7.10059171597633*(m.x171*m.x169 + m.x201*m.x199)
                          - 2.95857988165681*(m.x171*m.x199 - m.x169*m.x201))*m.b248 + m.x130 == 0)

m.c132 = Constraint(expr=-(40*(m.x185**2 + m.x215**2) - 40*(m.x185*m.x186 + m.x215*m.x216) - 20*(m.x185*m.x216 - m.x186*
                         m.x215))*m.b249 + m.x131 == 0)

m.c133 = Constraint(expr=-(40*(m.x186**2 + m.x216**2) - 40*(m.x186*m.x185 + m.x216*m.x215) - 20*(m.x186*m.x215 - m.x185*
                         m.x216))*m.b249 + m.x132 == 0)

m.c134 = Constraint(expr=-(23.5294117647059*(m.x168**2 + m.x198**2) - 23.5294117647059*(m.x168*m.x170 + m.x198*m.x200)
                          - 5.88235294117647*(m.x168*m.x200 - m.x170*m.x198))*m.b250 + m.x133 == 0)

m.c135 = Constraint(expr=-(23.5294117647059*(m.x170**2 + m.x200**2) - 23.5294117647059*(m.x170*m.x168 + m.x200*m.x198)
                          - 5.88235294117647*(m.x170*m.x198 - m.x168*m.x200))*m.b250 + m.x134 == 0)

m.c136 = Constraint(expr=-(4.02298850574713*(m.x174**2 + m.x204**2) - 4.02298850574713*(m.x174*m.x184 + m.x204*m.x214)
                          - 1.72413793103448*(m.x174*m.x214 - m.x184*m.x204))*m.b251 + m.x135 == 0)

m.c137 = Constraint(expr=-(4.02298850574713*(m.x184**2 + m.x214**2) - 4.02298850574713*(m.x184*m.x174 + m.x214*m.x204)
                          - 1.72413793103448*(m.x184*m.x204 - m.x174*m.x214))*m.b251 + m.x136 == 0)

m.c138 = Constraint(expr=-(3.84615384615385*(m.x186**2 + m.x216**2) - 3.84615384615385*(m.x186*m.x188 + m.x216*m.x218)
                          - 2.56410256410256*(m.x186*m.x218 - m.x188*m.x216))*m.b252 + m.x137 == 0)

m.c139 = Constraint(expr=-(3.84615384615385*(m.x188**2 + m.x218**2) - 3.84615384615385*(m.x188*m.x186 + m.x218*m.x216)
                          - 2.56410256410256*(m.x188*m.x216 - m.x186*m.x218))*m.b252 + m.x138 == 0)

m.c140 = Constraint(expr=-(1.29757785467128*(m.x191**2 + m.x221**2) - 1.29757785467128*(m.x191*m.x194 + m.x221*m.x224)
                          - 0.69204152249135*(m.x191*m.x224 - m.x194*m.x221))*m.b253 + m.x139 == 0)

m.c141 = Constraint(expr=-(1.29757785467128*(m.x194**2 + m.x224**2) - 1.29757785467128*(m.x194*m.x191 + m.x224*m.x221)
                          - 0.69204152249135*(m.x194*m.x221 - m.x191*m.x224))*m.b253 + m.x140 == 0)

m.c142 = Constraint(expr=-(10.958904109589*(m.x174**2 + m.x204**2) - 10.958904109589*(m.x174*m.x181 + m.x204*m.x211) - 
                         4.10958904109589*(m.x174*m.x211 - m.x181*m.x204))*m.b254 + m.x141 == 0)

m.c143 = Constraint(expr=-(10.958904109589*(m.x181**2 + m.x211**2) - 10.958904109589*(m.x181*m.x174 + m.x211*m.x204) - 
                         4.10958904109589*(m.x181*m.x204 - m.x174*m.x211))*m.b254 + m.x142 == 0)

m.c144 = Constraint(expr=-(4.57715596330275*(m.x172**2 + m.x202**2) - 4.58715596330275*(m.x172*m.x192 + m.x202*m.x222)
                          - 1.37614678899083*(m.x172*m.x222 - m.x192*m.x202))*m.b255 + m.x143 == 0)

m.c145 = Constraint(expr=-(4.57715596330275*(m.x192**2 + m.x222**2) - 4.58715596330275*(m.x192*m.x172 + m.x222*m.x202)
                          - 1.37614678899083*(m.x192*m.x202 - m.x172*m.x222))*m.b255 + m.x144 == 0)

m.c146 = Constraint(expr=-(4.15800415800416*(m.x176**2 + m.x206**2) - 4.15800415800416*(m.x176*m.x180 + m.x206*m.x210)
                          - 1.87110187110187*(m.x176*m.x210 - m.x180*m.x206))*m.b256 + m.x145 == 0)

m.c147 = Constraint(expr=-(4.15800415800416*(m.x180**2 + m.x210**2) - 4.15800415800416*(m.x180*m.x176 + m.x210*m.x206)
                          - 1.87110187110187*(m.x180*m.x206 - m.x176*m.x210))*m.b256 + m.x146 == 0)

m.c148 = Constraint(expr=-(4.76190476190476*(m.x170**2 + m.x200**2) - 4.76190476190476*(m.x170*m.x173 + m.x200*m.x203))*
                         m.b257 + m.x147 == 0)

m.c149 = Constraint(expr=-(4.76190476190476*(m.x173**2 + m.x203**2) - 4.76190476190476*(m.x173*m.x170 + m.x203*m.x200))*
                         m.b257 + m.x148 == 0)

m.c150 = Constraint(expr=-(4*(m.x179**2 + m.x209**2) - 4*(m.x179*m.x187 + m.x209*m.x217) - 2*(m.x179*m.x217 - m.x187*
                         m.x209))*m.b258 + m.x149 == 0)

m.c151 = Constraint(expr=-(4*(m.x187**2 + m.x217**2) - 4*(m.x187*m.x179 + m.x217*m.x209) - 2*(m.x187*m.x209 - m.x179*
                         m.x217))*m.b258 + m.x150 == 0)

m.c152 = Constraint(expr=-(1.83663605606573*(m.x189**2 + m.x219**2) - 1.83663605606573*(m.x189*m.x190 + m.x219*m.x220)
                          - 1.20831319478009*(m.x189*m.x220 - m.x190*m.x219))*m.b259 + m.x151 == 0)

m.c153 = Constraint(expr=-(1.83663605606573*(m.x190**2 + m.x220**2) - 1.83663605606573*(m.x190*m.x189 + m.x220*m.x219)
                          - 1.20831319478009*(m.x190*m.x219 - m.x189*m.x220))*m.b259 + m.x152 == 0)

m.c154 = Constraint(expr=-(3.63636363636364*(m.x179**2 + m.x209**2) - 3.63636363636364*(m.x179*m.x182 + m.x209*m.x212)
                          - 1.81818181818182*(m.x179*m.x212 - m.x182*m.x209))*m.b260 + m.x153 == 0)

m.c155 = Constraint(expr=-(3.63636363636364*(m.x182**2 + m.x212**2) - 3.63636363636364*(m.x182*m.x179 + m.x212*m.x209)
                          - 1.81818181818182*(m.x182*m.x209 - m.x179*m.x212))*m.b260 + m.x154 == 0)

m.c156 = Constraint(expr=-(4.47058823529412*(m.x180**2 + m.x210**2) - 4.47058823529412*(m.x180*m.x181 + m.x210*m.x211)
                          - 1.88235294117647*(m.x180*m.x211 - m.x181*m.x210))*m.b261 + m.x155 == 0)

m.c157 = Constraint(expr=-(4.47058823529412*(m.x181**2 + m.x211**2) - 4.47058823529412*(m.x181*m.x180 + m.x211*m.x210)
                          - 1.88235294117647*(m.x181*m.x210 - m.x180*m.x211))*m.b261 + m.x156 == 0)

m.c158 = Constraint(expr=-(4.99*(m.x166**2 + m.x196**2) - 5*(m.x166*m.x170 + m.x196*m.x200) - 1.66666666666667*(m.x166*
                         m.x200 - m.x170*m.x196))*m.b262 + m.x157 == 0)

m.c159 = Constraint(expr=-(4.99*(m.x170**2 + m.x200**2) - 5*(m.x170*m.x166 + m.x200*m.x196) - 1.66666666666667*(m.x170*
                         m.x196 - m.x166*m.x200))*m.b262 + m.x158 == 0)

m.c160 = Constraint(expr=-(5.22076923076923*(m.x166**2 + m.x196**2) - 5.23076923076923*(m.x166*m.x168 + m.x196*m.x198)
                          - 1.84615384615385*(m.x166*m.x198 - m.x168*m.x196))*m.b263 + m.x159 == 0)

m.c161 = Constraint(expr=-(5.22076923076923*(m.x168**2 + m.x198**2) - 5.23076923076923*(m.x168*m.x166 + m.x198*m.x196)
                          - 1.84615384615385*(m.x168*m.x196 - m.x166*m.x198))*m.b263 + m.x160 == 0)

m.c162 = Constraint(expr=-(4.91227979274611*(m.x165**2 + m.x195**2) - 4.92227979274611*(m.x165*m.x167 + m.x195*m.x197)
                          - 1.29533678756477*(m.x165*m.x197 - m.x167*m.x195))*m.b264 + m.x161 == 0)

m.c163 = Constraint(expr=-(4.91227979274611*(m.x167**2 + m.x197**2) - 4.92227979274611*(m.x167*m.x165 + m.x197*m.x195)
                          - 1.29533678756477*(m.x167*m.x195 - m.x165*m.x197))*m.b264 + m.x162 == 0)

m.c164 = Constraint(expr=-(1.73010380622837*(m.x193**2 + m.x223**2) - 1.73010380622837*(m.x193*m.x194 + m.x223*m.x224)
                          - 0.922722029988466*(m.x193*m.x224 - m.x194*m.x223))*m.b265 + m.x163 == 0)

m.c165 = Constraint(expr=-(1.73010380622837*(m.x194**2 + m.x224**2) - 1.73010380622837*(m.x194*m.x193 + m.x224*m.x223)
                          - 0.922722029988466*(m.x194*m.x223 - m.x193*m.x224))*m.b265 + m.x164 == 0)

m.c166 = Constraint(expr=m.x1**2 + m.x83**2 <= 0.4225)

m.c167 = Constraint(expr=m.x2**2 + m.x84**2 <= 0.4225)

m.c168 = Constraint(expr=m.x3**2 + m.x85**2 <= 0.0256)

m.c169 = Constraint(expr=m.x4**2 + m.x86**2 <= 0.0256)

m.c170 = Constraint(expr=m.x5**2 + m.x87**2 <= 1.69)

m.c171 = Constraint(expr=m.x6**2 + m.x88**2 <= 1.69)

m.c172 = Constraint(expr=m.x7**2 + m.x89**2 <= 0.0256)

m.c173 = Constraint(expr=m.x8**2 + m.x90**2 <= 0.0256)

m.c174 = Constraint(expr=m.x9**2 + m.x91**2 <= 0.1024)

m.c175 = Constraint(expr=m.x10**2 + m.x92**2 <= 0.1024)

m.c176 = Constraint(expr=m.x11**2 + m.x93**2 <= 0.1024)

m.c177 = Constraint(expr=m.x12**2 + m.x94**2 <= 0.1024)

m.c178 = Constraint(expr=m.x13**2 + m.x95**2 <= 0.1024)

m.c179 = Constraint(expr=m.x14**2 + m.x96**2 <= 0.1024)

m.c180 = Constraint(expr=m.x15**2 + m.x97**2 <= 1.69)

m.c181 = Constraint(expr=m.x16**2 + m.x98**2 <= 1.69)

m.c182 = Constraint(expr=m.x17**2 + m.x99**2 <= 0.4225)

m.c183 = Constraint(expr=m.x18**2 + m.x100**2 <= 0.4225)

m.c184 = Constraint(expr=m.x19**2 + m.x101**2 <= 1.69)

m.c185 = Constraint(expr=m.x20**2 + m.x102**2 <= 1.69)

m.c186 = Constraint(expr=m.x21**2 + m.x103**2 <= 0.1024)

m.c187 = Constraint(expr=m.x22**2 + m.x104**2 <= 0.1024)

m.c188 = Constraint(expr=m.x23**2 + m.x105**2 <= 0.0256)

m.c189 = Constraint(expr=m.x24**2 + m.x106**2 <= 0.0256)

m.c190 = Constraint(expr=m.x25**2 + m.x107**2 <= 0.0256)

m.c191 = Constraint(expr=m.x26**2 + m.x108**2 <= 0.0256)

m.c192 = Constraint(expr=m.x27**2 + m.x109**2 <= 1.69)

m.c193 = Constraint(expr=m.x28**2 + m.x110**2 <= 1.69)

m.c194 = Constraint(expr=m.x29**2 + m.x111**2 <= 0.1024)

m.c195 = Constraint(expr=m.x30**2 + m.x112**2 <= 0.1024)

m.c196 = Constraint(expr=m.x31**2 + m.x113**2 <= 0.4225)

m.c197 = Constraint(expr=m.x32**2 + m.x114**2 <= 0.4225)

m.c198 = Constraint(expr=m.x33**2 + m.x115**2 <= 0.1024)

m.c199 = Constraint(expr=m.x34**2 + m.x116**2 <= 0.1024)

m.c200 = Constraint(expr=m.x35**2 + m.x117**2 <= 0.4225)

m.c201 = Constraint(expr=m.x36**2 + m.x118**2 <= 0.4225)

m.c202 = Constraint(expr=m.x37**2 + m.x119**2 <= 0.1024)

m.c203 = Constraint(expr=m.x38**2 + m.x120**2 <= 0.1024)

m.c204 = Constraint(expr=m.x39**2 + m.x121**2 <= 0.0256)

m.c205 = Constraint(expr=m.x40**2 + m.x122**2 <= 0.0256)

m.c206 = Constraint(expr=m.x41**2 + m.x123**2 <= 0.4225)

m.c207 = Constraint(expr=m.x42**2 + m.x124**2 <= 0.4225)

m.c208 = Constraint(expr=m.x43**2 + m.x125**2 <= 0.1024)

m.c209 = Constraint(expr=m.x44**2 + m.x126**2 <= 0.1024)

m.c210 = Constraint(expr=m.x45**2 + m.x127**2 <= 0.0256)

m.c211 = Constraint(expr=m.x46**2 + m.x128**2 <= 0.0256)

m.c212 = Constraint(expr=m.x47**2 + m.x129**2 <= 0.49)

m.c213 = Constraint(expr=m.x48**2 + m.x130**2 <= 0.49)

m.c214 = Constraint(expr=m.x49**2 + m.x131**2 <= 0.1024)

m.c215 = Constraint(expr=m.x50**2 + m.x132**2 <= 0.1024)

m.c216 = Constraint(expr=m.x51**2 + m.x133**2 <= 0.81)

m.c217 = Constraint(expr=m.x52**2 + m.x134**2 <= 0.81)

m.c218 = Constraint(expr=m.x53**2 + m.x135**2 <= 0.1024)

m.c219 = Constraint(expr=m.x54**2 + m.x136**2 <= 0.1024)

m.c220 = Constraint(expr=m.x55**2 + m.x137**2 <= 0.0256)

m.c221 = Constraint(expr=m.x56**2 + m.x138**2 <= 0.0256)

m.c222 = Constraint(expr=m.x57**2 + m.x139**2 <= 0.0256)

m.c223 = Constraint(expr=m.x58**2 + m.x140**2 <= 0.0256)

m.c224 = Constraint(expr=m.x59**2 + m.x141**2 <= 0.1024)

m.c225 = Constraint(expr=m.x60**2 + m.x142**2 <= 0.1024)

m.c226 = Constraint(expr=m.x61**2 + m.x143**2 <= 0.1024)

m.c227 = Constraint(expr=m.x62**2 + m.x144**2 <= 0.1024)

m.c228 = Constraint(expr=m.x63**2 + m.x145**2 <= 0.1024)

m.c229 = Constraint(expr=m.x64**2 + m.x146**2 <= 0.1024)

m.c230 = Constraint(expr=m.x65**2 + m.x147**2 <= 0.4225)

m.c231 = Constraint(expr=m.x66**2 + m.x148**2 <= 0.4225)

m.c232 = Constraint(expr=m.x67**2 + m.x149**2 <= 0.0256)

m.c233 = Constraint(expr=m.x68**2 + m.x150**2 <= 0.0256)

m.c234 = Constraint(expr=m.x69**2 + m.x151**2 <= 0.0256)

m.c235 = Constraint(expr=m.x70**2 + m.x152**2 <= 0.0256)

m.c236 = Constraint(expr=m.x71**2 + m.x153**2 <= 0.0256)

m.c237 = Constraint(expr=m.x72**2 + m.x154**2 <= 0.0256)

m.c238 = Constraint(expr=m.x73**2 + m.x155**2 <= 0.0256)

m.c239 = Constraint(expr=m.x74**2 + m.x156**2 <= 0.0256)

m.c240 = Constraint(expr=m.x75**2 + m.x157**2 <= 0.4225)

m.c241 = Constraint(expr=m.x76**2 + m.x158**2 <= 0.4225)

m.c242 = Constraint(expr=m.x77**2 + m.x159**2 <= 0.4225)

m.c243 = Constraint(expr=m.x78**2 + m.x160**2 <= 0.4225)

m.c244 = Constraint(expr=m.x79**2 + m.x161**2 <= 1.69)

m.c245 = Constraint(expr=m.x80**2 + m.x162**2 <= 1.69)

m.c246 = Constraint(expr=m.x81**2 + m.x163**2 <= 0.0256)

m.c247 = Constraint(expr=m.x82**2 + m.x164**2 <= 0.0256)

m.c248 = Constraint(expr=m.x165**2 + m.x195**2 <= 1.1025)

m.c249 = Constraint(expr=m.x166**2 + m.x196**2 <= 1.21)

m.c250 = Constraint(expr=m.x167**2 + m.x197**2 <= 1.1025)

m.c251 = Constraint(expr=m.x168**2 + m.x198**2 <= 1.1025)

m.c252 = Constraint(expr=m.x169**2 + m.x199**2 <= 1.1025)

m.c253 = Constraint(expr=m.x170**2 + m.x200**2 <= 1.1025)

m.c254 = Constraint(expr=m.x171**2 + m.x201**2 <= 1.1025)

m.c255 = Constraint(expr=m.x172**2 + m.x202**2 <= 1.1025)

m.c256 = Constraint(expr=m.x173**2 + m.x203**2 <= 1.1025)

m.c257 = Constraint(expr=m.x174**2 + m.x204**2 <= 1.1025)

m.c258 = Constraint(expr=m.x175**2 + m.x205**2 <= 1.1025)

m.c259 = Constraint(expr=m.x176**2 + m.x206**2 <= 1.1025)

m.c260 = Constraint(expr=m.x177**2 + m.x207**2 <= 1.21)

m.c261 = Constraint(expr=m.x178**2 + m.x208**2 <= 1.1025)

m.c262 = Constraint(expr=m.x179**2 + m.x209**2 <= 1.1025)

m.c263 = Constraint(expr=m.x180**2 + m.x210**2 <= 1.1025)

m.c264 = Constraint(expr=m.x181**2 + m.x211**2 <= 1.1025)

m.c265 = Constraint(expr=m.x182**2 + m.x212**2 <= 1.1025)

m.c266 = Constraint(expr=m.x183**2 + m.x213**2 <= 1.1025)

m.c267 = Constraint(expr=m.x184**2 + m.x214**2 <= 1.1025)

m.c268 = Constraint(expr=m.x185**2 + m.x215**2 <= 1.1025)

m.c269 = Constraint(expr=m.x186**2 + m.x216**2 <= 1.21)

m.c270 = Constraint(expr=m.x187**2 + m.x217**2 <= 1.21)

m.c271 = Constraint(expr=m.x188**2 + m.x218**2 <= 1.1025)

m.c272 = Constraint(expr=m.x189**2 + m.x219**2 <= 1.1025)

m.c273 = Constraint(expr=m.x190**2 + m.x220**2 <= 1.1025)

m.c274 = Constraint(expr=m.x191**2 + m.x221**2 <= 1.21)

m.c275 = Constraint(expr=m.x192**2 + m.x222**2 <= 1.1025)

m.c276 = Constraint(expr=m.x193**2 + m.x223**2 <= 1.1025)

m.c277 = Constraint(expr=m.x194**2 + m.x224**2 <= 1.1025)

m.c278 = Constraint(expr=m.x165**2 + m.x195**2 >= 0.9025)

m.c279 = Constraint(expr=m.x166**2 + m.x196**2 >= 0.9025)

m.c280 = Constraint(expr=m.x167**2 + m.x197**2 >= 0.9025)

m.c281 = Constraint(expr=m.x168**2 + m.x198**2 >= 0.9025)

m.c282 = Constraint(expr=m.x169**2 + m.x199**2 >= 0.9025)

m.c283 = Constraint(expr=m.x170**2 + m.x200**2 >= 0.9025)

m.c284 = Constraint(expr=m.x171**2 + m.x201**2 >= 0.9025)

m.c285 = Constraint(expr=m.x172**2 + m.x202**2 >= 0.9025)

m.c286 = Constraint(expr=m.x173**2 + m.x203**2 >= 0.9025)

m.c287 = Constraint(expr=m.x174**2 + m.x204**2 >= 0.9025)

m.c288 = Constraint(expr=m.x175**2 + m.x205**2 >= 0.9025)

m.c289 = Constraint(expr=m.x176**2 + m.x206**2 >= 0.9025)

m.c290 = Constraint(expr=m.x177**2 + m.x207**2 >= 0.9025)

m.c291 = Constraint(expr=m.x178**2 + m.x208**2 >= 0.9025)

m.c292 = Constraint(expr=m.x179**2 + m.x209**2 >= 0.9025)

m.c293 = Constraint(expr=m.x180**2 + m.x210**2 >= 0.9025)

m.c294 = Constraint(expr=m.x181**2 + m.x211**2 >= 0.9025)

m.c295 = Constraint(expr=m.x182**2 + m.x212**2 >= 0.9025)

m.c296 = Constraint(expr=m.x183**2 + m.x213**2 >= 0.9025)

m.c297 = Constraint(expr=m.x184**2 + m.x214**2 >= 0.9025)

m.c298 = Constraint(expr=m.x185**2 + m.x215**2 >= 0.9025)

m.c299 = Constraint(expr=m.x186**2 + m.x216**2 >= 0.9025)

m.c300 = Constraint(expr=m.x187**2 + m.x217**2 >= 0.9025)

m.c301 = Constraint(expr=m.x188**2 + m.x218**2 >= 0.9025)

m.c302 = Constraint(expr=m.x189**2 + m.x219**2 >= 0.9025)

m.c303 = Constraint(expr=m.x190**2 + m.x220**2 >= 0.9025)

m.c304 = Constraint(expr=m.x191**2 + m.x221**2 >= 0.9025)

m.c305 = Constraint(expr=m.x192**2 + m.x222**2 >= 0.9025)

m.c306 = Constraint(expr=m.x193**2 + m.x223**2 >= 0.9025)

m.c307 = Constraint(expr=m.x194**2 + m.x224**2 >= 0.9025)

m.c308 = Constraint(expr=   m.x266 <= 0.8)

m.c309 = Constraint(expr=   m.x267 <= 0.8)

m.c310 = Constraint(expr=   m.x268 <= 0.4)

m.c311 = Constraint(expr=   m.x269 <= 0.5)

m.c312 = Constraint(expr=   m.x270 <= 0.3)

m.c313 = Constraint(expr=   m.x271 <= 0.55)

m.c314 = Constraint(expr=   m.x266 >= 0)

m.c315 = Constraint(expr=   m.x267 >= 0)

m.c316 = Constraint(expr=   m.x268 >= 0)

m.c317 = Constraint(expr=   m.x269 >= 0)

m.c318 = Constraint(expr=   m.x270 >= 0)

m.c319 = Constraint(expr=   m.x271 >= 0)

m.c320 = Constraint(expr=   m.x272 <= 1.5)

m.c321 = Constraint(expr=   m.x273 <= 0.6)

m.c322 = Constraint(expr=   m.x274 <= 0.447)

m.c323 = Constraint(expr=   m.x275 <= 0.625)

m.c324 = Constraint(expr=   m.x276 <= 0.4)

m.c325 = Constraint(expr=   m.x277 <= 0.487)

m.c326 = Constraint(expr=   m.x272 >= -0.2)

m.c327 = Constraint(expr=   m.x273 >= -0.2)

m.c328 = Constraint(expr=   m.x274 >= -0.15)

m.c329 = Constraint(expr=   m.x275 >= -0.15)

m.c330 = Constraint(expr=   m.x276 >= -0.1)

m.c331 = Constraint(expr=   m.x277 >= -0.15)

m.c332 = Constraint(expr=   m.x195 == 0)

m.c333 = Constraint(expr=   m.x15 + m.x79 - m.x266 == 0)

m.c334 = Constraint(expr=   m.x16 + m.x27 + m.x75 + m.x77 - m.x267 == -0.217)

m.c335 = Constraint(expr=   m.x2 - m.x268 == 0)

m.c336 = Constraint(expr=   m.x10 + m.x50 + m.x55 - m.x269 == 0)

m.c337 = Constraint(expr=   m.x25 + m.x68 - m.x270 == -0.032)

m.c338 = Constraint(expr=   m.x3 + m.x42 + m.x46 + m.x57 - m.x271 == 0)

m.c339 = Constraint(expr=   m.x97 + m.x161 - m.x272 == 0)

m.c340 = Constraint(expr=   m.x98 + m.x109 + m.x157 + m.x159 - m.x273 == -0.127)

m.c341 = Constraint(expr=   m.x84 - m.x274 == 0)

m.c342 = Constraint(expr=   m.x92 + m.x132 + m.x137 - m.x275 == 0)

m.c343 = Constraint(expr=   m.x107 + m.x150 - m.x276 == -0.016)

m.c344 = Constraint(expr=   m.x85 + m.x124 + m.x128 + m.x139 - m.x277 == 0)

m.c345 = Constraint(expr=   m.x19 + m.x80 == -0.024)

m.c346 = Constraint(expr=   m.x20 + m.x31 + m.x51 + m.x78 == -0.076)

m.c347 = Constraint(expr=   m.x28 + m.x47 == 0)

m.c348 = Constraint(expr=   m.x5 + m.x11 + m.x13 + m.x43 + m.x52 + m.x65 + m.x76 == 0)

m.c349 = Constraint(expr=   m.x6 + m.x48 == -0.228)

m.c350 = Constraint(expr=   m.x44 + m.x61 == -0.3)

m.c351 = Constraint(expr=   m.x17 + m.x35 + m.x66 == 0)

m.c352 = Constraint(expr=   m.x9 + m.x12 + m.x33 + m.x36 + m.x53 + m.x59 == -0.058)

m.c353 = Constraint(expr=   m.x18 == 0)

m.c354 = Constraint(expr=   m.x1 + m.x21 + m.x32 + m.x37 + m.x63 == -0.112)

m.c355 = Constraint(expr=   m.x7 + m.x22 == -0.062)

m.c356 = Constraint(expr=   m.x8 + m.x38 + m.x67 + m.x71 == -0.082)

m.c357 = Constraint(expr=   m.x64 + m.x73 == -0.035)

m.c358 = Constraint(expr=   m.x60 + m.x74 == -0.09)

m.c359 = Constraint(expr=   m.x39 + m.x72 == -0.032)

m.c360 = Constraint(expr=   m.x29 + m.x40 == -0.095)

m.c361 = Constraint(expr=   m.x30 + m.x54 == -0.022)

m.c362 = Constraint(expr=   m.x34 + m.x49 == -0.175)

m.c363 = Constraint(expr=   m.x23 + m.x26 + m.x56 == -0.087)

m.c364 = Constraint(expr=   m.x24 + m.x45 + m.x69 == 0)

m.c365 = Constraint(expr=   m.x70 == -0.035)

m.c366 = Constraint(expr=   m.x14 + m.x41 + m.x62 == 0)

m.c367 = Constraint(expr=   m.x4 + m.x81 == -0.024)

m.c368 = Constraint(expr=   m.x58 + m.x82 == -0.106)

m.c369 = Constraint(expr=   m.x101 + m.x162 == -0.012)

m.c370 = Constraint(expr=   m.x102 + m.x113 + m.x133 + m.x160 == -0.016)

m.c371 = Constraint(expr=   m.x110 + m.x129 == 0)

m.c372 = Constraint(expr=   m.x87 + m.x93 + m.x95 + m.x125 + m.x134 + m.x147 + m.x158 == 0)

m.c373 = Constraint(expr=   m.x88 + m.x130 == -0.109)

m.c374 = Constraint(expr=   m.x126 + m.x143 == -0.3)

m.c375 = Constraint(expr=   m.x99 + m.x117 + m.x148 == 0)

m.c376 = Constraint(expr=   m.x91 + m.x94 + m.x115 + m.x118 + m.x135 + m.x141 == -0.02)

m.c377 = Constraint(expr=   m.x100 == 0)

m.c378 = Constraint(expr=   m.x83 + m.x103 + m.x114 + m.x119 + m.x145 == -0.075)

m.c379 = Constraint(expr=   m.x89 + m.x104 == -0.016)

m.c380 = Constraint(expr=   m.x90 + m.x120 + m.x149 + m.x153 == -0.025)

m.c381 = Constraint(expr=   m.x146 + m.x155 == -0.018)

m.c382 = Constraint(expr=   m.x142 + m.x156 == -0.058)

m.c383 = Constraint(expr=   m.x121 + m.x154 == -0.009)

m.c384 = Constraint(expr=   m.x111 + m.x122 == -0.034)

m.c385 = Constraint(expr=   m.x112 + m.x136 == -0.007)

m.c386 = Constraint(expr=   m.x116 + m.x131 == -0.112)

m.c387 = Constraint(expr=   m.x105 + m.x108 + m.x138 == -0.067)

m.c388 = Constraint(expr=   m.x106 + m.x127 + m.x151 == 0)

m.c389 = Constraint(expr=   m.x152 == -0.023)

m.c390 = Constraint(expr=   m.x96 + m.x123 + m.x144 == 0)

m.c391 = Constraint(expr=   m.x86 + m.x163 == -0.009)

m.c392 = Constraint(expr=   m.x140 + m.x164 == -0.019)
