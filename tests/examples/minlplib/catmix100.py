#  NLP written by GAMS Convert at 04/21/18 13:51:13
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        201      201        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        304      304        0        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1203        3     1200        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x102 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x103 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x104 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x105 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x106 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x107 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x108 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x109 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x110 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x111 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x112 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x113 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x114 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x115 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x116 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x117 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x118 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x119 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x120 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x121 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x122 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x123 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x124 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x125 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x126 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x127 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x128 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x129 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x130 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x131 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x132 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x133 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x134 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x135 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x136 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x137 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x138 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x139 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x140 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x141 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x142 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x143 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x144 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x145 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x146 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x147 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x148 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x149 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x150 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x151 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x152 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x153 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x154 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x155 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x156 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x157 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x158 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x159 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x160 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x161 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x162 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x163 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x164 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x165 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x166 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x167 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x168 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x169 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x170 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x171 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x172 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x173 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x174 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x175 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x176 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x177 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x178 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x179 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x180 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x181 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x182 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x183 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x184 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x185 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x186 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x187 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x188 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x189 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x190 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x191 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x192 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x193 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x194 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x195 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x196 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x197 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x198 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x199 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x200 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x201 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x202 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x203 = Var(within=Reals,bounds=(0,0),initialize=0)
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
m.x225 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x226 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x227 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x228 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x229 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x230 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x231 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x232 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x233 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x234 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x235 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x236 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x237 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x238 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x239 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x240 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x241 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x242 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x243 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x244 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x245 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x246 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x247 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x248 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x249 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x250 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x251 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x252 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x253 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x254 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x255 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x256 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x257 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x258 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x259 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x260 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x261 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x262 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x263 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x264 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x265 = Var(within=Reals,bounds=(None,None),initialize=0)
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
m.x278 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x279 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x280 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x281 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x282 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x283 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x284 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x285 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x286 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x287 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x288 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x289 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x290 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x291 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x292 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x293 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x294 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x295 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x296 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x297 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x298 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x299 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x300 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x301 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x302 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x303 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   m.x202 + m.x303 - 1, sense=minimize)

m.c2 = Constraint(expr=m.x103 - (0.005*(m.x1*(10*m.x203 - m.x102) + m.x2*(10*m.x204 - m.x103)) + m.x102) == 0)

m.c3 = Constraint(expr=m.x104 - (0.005*(m.x2*(10*m.x204 - m.x103) + m.x3*(10*m.x205 - m.x104)) + m.x103) == 0)

m.c4 = Constraint(expr=m.x105 - (0.005*(m.x3*(10*m.x205 - m.x104) + m.x4*(10*m.x206 - m.x105)) + m.x104) == 0)

m.c5 = Constraint(expr=m.x106 - (0.005*(m.x4*(10*m.x206 - m.x105) + m.x5*(10*m.x207 - m.x106)) + m.x105) == 0)

m.c6 = Constraint(expr=m.x107 - (0.005*(m.x5*(10*m.x207 - m.x106) + m.x6*(10*m.x208 - m.x107)) + m.x106) == 0)

m.c7 = Constraint(expr=m.x108 - (0.005*(m.x6*(10*m.x208 - m.x107) + m.x7*(10*m.x209 - m.x108)) + m.x107) == 0)

m.c8 = Constraint(expr=m.x109 - (0.005*(m.x7*(10*m.x209 - m.x108) + m.x8*(10*m.x210 - m.x109)) + m.x108) == 0)

m.c9 = Constraint(expr=m.x110 - (0.005*(m.x8*(10*m.x210 - m.x109) + m.x9*(10*m.x211 - m.x110)) + m.x109) == 0)

m.c10 = Constraint(expr=m.x111 - (0.005*(m.x9*(10*m.x211 - m.x110) + m.x10*(10*m.x212 - m.x111)) + m.x110) == 0)

m.c11 = Constraint(expr=m.x112 - (0.005*(m.x10*(10*m.x212 - m.x111) + m.x11*(10*m.x213 - m.x112)) + m.x111) == 0)

m.c12 = Constraint(expr=m.x113 - (0.005*(m.x11*(10*m.x213 - m.x112) + m.x12*(10*m.x214 - m.x113)) + m.x112) == 0)

m.c13 = Constraint(expr=m.x114 - (0.005*(m.x12*(10*m.x214 - m.x113) + m.x13*(10*m.x215 - m.x114)) + m.x113) == 0)

m.c14 = Constraint(expr=m.x115 - (0.005*(m.x13*(10*m.x215 - m.x114) + m.x14*(10*m.x216 - m.x115)) + m.x114) == 0)

m.c15 = Constraint(expr=m.x116 - (0.005*(m.x14*(10*m.x216 - m.x115) + m.x15*(10*m.x217 - m.x116)) + m.x115) == 0)

m.c16 = Constraint(expr=m.x117 - (0.005*(m.x15*(10*m.x217 - m.x116) + m.x16*(10*m.x218 - m.x117)) + m.x116) == 0)

m.c17 = Constraint(expr=m.x118 - (0.005*(m.x16*(10*m.x218 - m.x117) + m.x17*(10*m.x219 - m.x118)) + m.x117) == 0)

m.c18 = Constraint(expr=m.x119 - (0.005*(m.x17*(10*m.x219 - m.x118) + m.x18*(10*m.x220 - m.x119)) + m.x118) == 0)

m.c19 = Constraint(expr=m.x120 - (0.005*(m.x18*(10*m.x220 - m.x119) + m.x19*(10*m.x221 - m.x120)) + m.x119) == 0)

m.c20 = Constraint(expr=m.x121 - (0.005*(m.x19*(10*m.x221 - m.x120) + m.x20*(10*m.x222 - m.x121)) + m.x120) == 0)

m.c21 = Constraint(expr=m.x122 - (0.005*(m.x20*(10*m.x222 - m.x121) + m.x21*(10*m.x223 - m.x122)) + m.x121) == 0)

m.c22 = Constraint(expr=m.x123 - (0.005*(m.x21*(10*m.x223 - m.x122) + m.x22*(10*m.x224 - m.x123)) + m.x122) == 0)

m.c23 = Constraint(expr=m.x124 - (0.005*(m.x22*(10*m.x224 - m.x123) + m.x23*(10*m.x225 - m.x124)) + m.x123) == 0)

m.c24 = Constraint(expr=m.x125 - (0.005*(m.x23*(10*m.x225 - m.x124) + m.x24*(10*m.x226 - m.x125)) + m.x124) == 0)

m.c25 = Constraint(expr=m.x126 - (0.005*(m.x24*(10*m.x226 - m.x125) + m.x25*(10*m.x227 - m.x126)) + m.x125) == 0)

m.c26 = Constraint(expr=m.x127 - (0.005*(m.x25*(10*m.x227 - m.x126) + m.x26*(10*m.x228 - m.x127)) + m.x126) == 0)

m.c27 = Constraint(expr=m.x128 - (0.005*(m.x26*(10*m.x228 - m.x127) + m.x27*(10*m.x229 - m.x128)) + m.x127) == 0)

m.c28 = Constraint(expr=m.x129 - (0.005*(m.x27*(10*m.x229 - m.x128) + m.x28*(10*m.x230 - m.x129)) + m.x128) == 0)

m.c29 = Constraint(expr=m.x130 - (0.005*(m.x28*(10*m.x230 - m.x129) + m.x29*(10*m.x231 - m.x130)) + m.x129) == 0)

m.c30 = Constraint(expr=m.x131 - (0.005*(m.x29*(10*m.x231 - m.x130) + m.x30*(10*m.x232 - m.x131)) + m.x130) == 0)

m.c31 = Constraint(expr=m.x132 - (0.005*(m.x30*(10*m.x232 - m.x131) + m.x31*(10*m.x233 - m.x132)) + m.x131) == 0)

m.c32 = Constraint(expr=m.x133 - (0.005*(m.x31*(10*m.x233 - m.x132) + m.x32*(10*m.x234 - m.x133)) + m.x132) == 0)

m.c33 = Constraint(expr=m.x134 - (0.005*(m.x32*(10*m.x234 - m.x133) + m.x33*(10*m.x235 - m.x134)) + m.x133) == 0)

m.c34 = Constraint(expr=m.x135 - (0.005*(m.x33*(10*m.x235 - m.x134) + m.x34*(10*m.x236 - m.x135)) + m.x134) == 0)

m.c35 = Constraint(expr=m.x136 - (0.005*(m.x34*(10*m.x236 - m.x135) + m.x35*(10*m.x237 - m.x136)) + m.x135) == 0)

m.c36 = Constraint(expr=m.x137 - (0.005*(m.x35*(10*m.x237 - m.x136) + m.x36*(10*m.x238 - m.x137)) + m.x136) == 0)

m.c37 = Constraint(expr=m.x138 - (0.005*(m.x36*(10*m.x238 - m.x137) + m.x37*(10*m.x239 - m.x138)) + m.x137) == 0)

m.c38 = Constraint(expr=m.x139 - (0.005*(m.x37*(10*m.x239 - m.x138) + m.x38*(10*m.x240 - m.x139)) + m.x138) == 0)

m.c39 = Constraint(expr=m.x140 - (0.005*(m.x38*(10*m.x240 - m.x139) + m.x39*(10*m.x241 - m.x140)) + m.x139) == 0)

m.c40 = Constraint(expr=m.x141 - (0.005*(m.x39*(10*m.x241 - m.x140) + m.x40*(10*m.x242 - m.x141)) + m.x140) == 0)

m.c41 = Constraint(expr=m.x142 - (0.005*(m.x40*(10*m.x242 - m.x141) + m.x41*(10*m.x243 - m.x142)) + m.x141) == 0)

m.c42 = Constraint(expr=m.x143 - (0.005*(m.x41*(10*m.x243 - m.x142) + m.x42*(10*m.x244 - m.x143)) + m.x142) == 0)

m.c43 = Constraint(expr=m.x144 - (0.005*(m.x42*(10*m.x244 - m.x143) + m.x43*(10*m.x245 - m.x144)) + m.x143) == 0)

m.c44 = Constraint(expr=m.x145 - (0.005*(m.x43*(10*m.x245 - m.x144) + m.x44*(10*m.x246 - m.x145)) + m.x144) == 0)

m.c45 = Constraint(expr=m.x146 - (0.005*(m.x44*(10*m.x246 - m.x145) + m.x45*(10*m.x247 - m.x146)) + m.x145) == 0)

m.c46 = Constraint(expr=m.x147 - (0.005*(m.x45*(10*m.x247 - m.x146) + m.x46*(10*m.x248 - m.x147)) + m.x146) == 0)

m.c47 = Constraint(expr=m.x148 - (0.005*(m.x46*(10*m.x248 - m.x147) + m.x47*(10*m.x249 - m.x148)) + m.x147) == 0)

m.c48 = Constraint(expr=m.x149 - (0.005*(m.x47*(10*m.x249 - m.x148) + m.x48*(10*m.x250 - m.x149)) + m.x148) == 0)

m.c49 = Constraint(expr=m.x150 - (0.005*(m.x48*(10*m.x250 - m.x149) + m.x49*(10*m.x251 - m.x150)) + m.x149) == 0)

m.c50 = Constraint(expr=m.x151 - (0.005*(m.x49*(10*m.x251 - m.x150) + m.x50*(10*m.x252 - m.x151)) + m.x150) == 0)

m.c51 = Constraint(expr=m.x152 - (0.005*(m.x50*(10*m.x252 - m.x151) + m.x51*(10*m.x253 - m.x152)) + m.x151) == 0)

m.c52 = Constraint(expr=m.x153 - (0.005*(m.x51*(10*m.x253 - m.x152) + m.x52*(10*m.x254 - m.x153)) + m.x152) == 0)

m.c53 = Constraint(expr=m.x154 - (0.005*(m.x52*(10*m.x254 - m.x153) + m.x53*(10*m.x255 - m.x154)) + m.x153) == 0)

m.c54 = Constraint(expr=m.x155 - (0.005*(m.x53*(10*m.x255 - m.x154) + m.x54*(10*m.x256 - m.x155)) + m.x154) == 0)

m.c55 = Constraint(expr=m.x156 - (0.005*(m.x54*(10*m.x256 - m.x155) + m.x55*(10*m.x257 - m.x156)) + m.x155) == 0)

m.c56 = Constraint(expr=m.x157 - (0.005*(m.x55*(10*m.x257 - m.x156) + m.x56*(10*m.x258 - m.x157)) + m.x156) == 0)

m.c57 = Constraint(expr=m.x158 - (0.005*(m.x56*(10*m.x258 - m.x157) + m.x57*(10*m.x259 - m.x158)) + m.x157) == 0)

m.c58 = Constraint(expr=m.x159 - (0.005*(m.x57*(10*m.x259 - m.x158) + m.x58*(10*m.x260 - m.x159)) + m.x158) == 0)

m.c59 = Constraint(expr=m.x160 - (0.005*(m.x58*(10*m.x260 - m.x159) + m.x59*(10*m.x261 - m.x160)) + m.x159) == 0)

m.c60 = Constraint(expr=m.x161 - (0.005*(m.x59*(10*m.x261 - m.x160) + m.x60*(10*m.x262 - m.x161)) + m.x160) == 0)

m.c61 = Constraint(expr=m.x162 - (0.005*(m.x60*(10*m.x262 - m.x161) + m.x61*(10*m.x263 - m.x162)) + m.x161) == 0)

m.c62 = Constraint(expr=m.x163 - (0.005*(m.x61*(10*m.x263 - m.x162) + m.x62*(10*m.x264 - m.x163)) + m.x162) == 0)

m.c63 = Constraint(expr=m.x164 - (0.005*(m.x62*(10*m.x264 - m.x163) + m.x63*(10*m.x265 - m.x164)) + m.x163) == 0)

m.c64 = Constraint(expr=m.x165 - (0.005*(m.x63*(10*m.x265 - m.x164) + m.x64*(10*m.x266 - m.x165)) + m.x164) == 0)

m.c65 = Constraint(expr=m.x166 - (0.005*(m.x64*(10*m.x266 - m.x165) + m.x65*(10*m.x267 - m.x166)) + m.x165) == 0)

m.c66 = Constraint(expr=m.x167 - (0.005*(m.x65*(10*m.x267 - m.x166) + m.x66*(10*m.x268 - m.x167)) + m.x166) == 0)

m.c67 = Constraint(expr=m.x168 - (0.005*(m.x66*(10*m.x268 - m.x167) + m.x67*(10*m.x269 - m.x168)) + m.x167) == 0)

m.c68 = Constraint(expr=m.x169 - (0.005*(m.x67*(10*m.x269 - m.x168) + m.x68*(10*m.x270 - m.x169)) + m.x168) == 0)

m.c69 = Constraint(expr=m.x170 - (0.005*(m.x68*(10*m.x270 - m.x169) + m.x69*(10*m.x271 - m.x170)) + m.x169) == 0)

m.c70 = Constraint(expr=m.x171 - (0.005*(m.x69*(10*m.x271 - m.x170) + m.x70*(10*m.x272 - m.x171)) + m.x170) == 0)

m.c71 = Constraint(expr=m.x172 - (0.005*(m.x70*(10*m.x272 - m.x171) + m.x71*(10*m.x273 - m.x172)) + m.x171) == 0)

m.c72 = Constraint(expr=m.x173 - (0.005*(m.x71*(10*m.x273 - m.x172) + m.x72*(10*m.x274 - m.x173)) + m.x172) == 0)

m.c73 = Constraint(expr=m.x174 - (0.005*(m.x72*(10*m.x274 - m.x173) + m.x73*(10*m.x275 - m.x174)) + m.x173) == 0)

m.c74 = Constraint(expr=m.x175 - (0.005*(m.x73*(10*m.x275 - m.x174) + m.x74*(10*m.x276 - m.x175)) + m.x174) == 0)

m.c75 = Constraint(expr=m.x176 - (0.005*(m.x74*(10*m.x276 - m.x175) + m.x75*(10*m.x277 - m.x176)) + m.x175) == 0)

m.c76 = Constraint(expr=m.x177 - (0.005*(m.x75*(10*m.x277 - m.x176) + m.x76*(10*m.x278 - m.x177)) + m.x176) == 0)

m.c77 = Constraint(expr=m.x178 - (0.005*(m.x76*(10*m.x278 - m.x177) + m.x77*(10*m.x279 - m.x178)) + m.x177) == 0)

m.c78 = Constraint(expr=m.x179 - (0.005*(m.x77*(10*m.x279 - m.x178) + m.x78*(10*m.x280 - m.x179)) + m.x178) == 0)

m.c79 = Constraint(expr=m.x180 - (0.005*(m.x78*(10*m.x280 - m.x179) + m.x79*(10*m.x281 - m.x180)) + m.x179) == 0)

m.c80 = Constraint(expr=m.x181 - (0.005*(m.x79*(10*m.x281 - m.x180) + m.x80*(10*m.x282 - m.x181)) + m.x180) == 0)

m.c81 = Constraint(expr=m.x182 - (0.005*(m.x80*(10*m.x282 - m.x181) + m.x81*(10*m.x283 - m.x182)) + m.x181) == 0)

m.c82 = Constraint(expr=m.x183 - (0.005*(m.x81*(10*m.x283 - m.x182) + m.x82*(10*m.x284 - m.x183)) + m.x182) == 0)

m.c83 = Constraint(expr=m.x184 - (0.005*(m.x82*(10*m.x284 - m.x183) + m.x83*(10*m.x285 - m.x184)) + m.x183) == 0)

m.c84 = Constraint(expr=m.x185 - (0.005*(m.x83*(10*m.x285 - m.x184) + m.x84*(10*m.x286 - m.x185)) + m.x184) == 0)

m.c85 = Constraint(expr=m.x186 - (0.005*(m.x84*(10*m.x286 - m.x185) + m.x85*(10*m.x287 - m.x186)) + m.x185) == 0)

m.c86 = Constraint(expr=m.x187 - (0.005*(m.x85*(10*m.x287 - m.x186) + m.x86*(10*m.x288 - m.x187)) + m.x186) == 0)

m.c87 = Constraint(expr=m.x188 - (0.005*(m.x86*(10*m.x288 - m.x187) + m.x87*(10*m.x289 - m.x188)) + m.x187) == 0)

m.c88 = Constraint(expr=m.x189 - (0.005*(m.x87*(10*m.x289 - m.x188) + m.x88*(10*m.x290 - m.x189)) + m.x188) == 0)

m.c89 = Constraint(expr=m.x190 - (0.005*(m.x88*(10*m.x290 - m.x189) + m.x89*(10*m.x291 - m.x190)) + m.x189) == 0)

m.c90 = Constraint(expr=m.x191 - (0.005*(m.x89*(10*m.x291 - m.x190) + m.x90*(10*m.x292 - m.x191)) + m.x190) == 0)

m.c91 = Constraint(expr=m.x192 - (0.005*(m.x90*(10*m.x292 - m.x191) + m.x91*(10*m.x293 - m.x192)) + m.x191) == 0)

m.c92 = Constraint(expr=m.x193 - (0.005*(m.x91*(10*m.x293 - m.x192) + m.x92*(10*m.x294 - m.x193)) + m.x192) == 0)

m.c93 = Constraint(expr=m.x194 - (0.005*(m.x92*(10*m.x294 - m.x193) + m.x93*(10*m.x295 - m.x194)) + m.x193) == 0)

m.c94 = Constraint(expr=m.x195 - (0.005*(m.x93*(10*m.x295 - m.x194) + m.x94*(10*m.x296 - m.x195)) + m.x194) == 0)

m.c95 = Constraint(expr=m.x196 - (0.005*(m.x94*(10*m.x296 - m.x195) + m.x95*(10*m.x297 - m.x196)) + m.x195) == 0)

m.c96 = Constraint(expr=m.x197 - (0.005*(m.x95*(10*m.x297 - m.x196) + m.x96*(10*m.x298 - m.x197)) + m.x196) == 0)

m.c97 = Constraint(expr=m.x198 - (0.005*(m.x96*(10*m.x298 - m.x197) + m.x97*(10*m.x299 - m.x198)) + m.x197) == 0)

m.c98 = Constraint(expr=m.x199 - (0.005*(m.x97*(10*m.x299 - m.x198) + m.x98*(10*m.x300 - m.x199)) + m.x198) == 0)

m.c99 = Constraint(expr=m.x200 - (0.005*(m.x98*(10*m.x300 - m.x199) + m.x99*(10*m.x301 - m.x200)) + m.x199) == 0)

m.c100 = Constraint(expr=m.x201 - (0.005*(m.x99*(10*m.x301 - m.x200) + m.x100*(10*m.x302 - m.x201)) + m.x200) == 0)

m.c101 = Constraint(expr=m.x202 - (0.005*(m.x100*(10*m.x302 - m.x201) + m.x101*(10*m.x303 - m.x202)) + m.x201) == 0)

m.c102 = Constraint(expr=m.x204 - (0.005*(m.x1*(m.x102 - 10*m.x203) - (1 - m.x1)*m.x203 + m.x2*(m.x103 - 10*m.x204) - (1
                          - m.x2)*m.x204) + m.x203) == 0)

m.c103 = Constraint(expr=m.x205 - (0.005*(m.x2*(m.x103 - 10*m.x204) - (1 - m.x2)*m.x204 + m.x3*(m.x104 - 10*m.x205) - (1
                          - m.x3)*m.x205) + m.x204) == 0)

m.c104 = Constraint(expr=m.x206 - (0.005*(m.x3*(m.x104 - 10*m.x205) - (1 - m.x3)*m.x205 + m.x4*(m.x105 - 10*m.x206) - (1
                          - m.x4)*m.x206) + m.x205) == 0)

m.c105 = Constraint(expr=m.x207 - (0.005*(m.x4*(m.x105 - 10*m.x206) - (1 - m.x4)*m.x206 + m.x5*(m.x106 - 10*m.x207) - (1
                          - m.x5)*m.x207) + m.x206) == 0)

m.c106 = Constraint(expr=m.x208 - (0.005*(m.x5*(m.x106 - 10*m.x207) - (1 - m.x5)*m.x207 + m.x6*(m.x107 - 10*m.x208) - (1
                          - m.x6)*m.x208) + m.x207) == 0)

m.c107 = Constraint(expr=m.x209 - (0.005*(m.x6*(m.x107 - 10*m.x208) - (1 - m.x6)*m.x208 + m.x7*(m.x108 - 10*m.x209) - (1
                          - m.x7)*m.x209) + m.x208) == 0)

m.c108 = Constraint(expr=m.x210 - (0.005*(m.x7*(m.x108 - 10*m.x209) - (1 - m.x7)*m.x209 + m.x8*(m.x109 - 10*m.x210) - (1
                          - m.x8)*m.x210) + m.x209) == 0)

m.c109 = Constraint(expr=m.x211 - (0.005*(m.x8*(m.x109 - 10*m.x210) - (1 - m.x8)*m.x210 + m.x9*(m.x110 - 10*m.x211) - (1
                          - m.x9)*m.x211) + m.x210) == 0)

m.c110 = Constraint(expr=m.x212 - (0.005*(m.x9*(m.x110 - 10*m.x211) - (1 - m.x9)*m.x211 + m.x10*(m.x111 - 10*m.x212) - (
                         1 - m.x10)*m.x212) + m.x211) == 0)

m.c111 = Constraint(expr=m.x213 - (0.005*(m.x10*(m.x111 - 10*m.x212) - (1 - m.x10)*m.x212 + m.x11*(m.x112 - 10*m.x213)
                          - (1 - m.x11)*m.x213) + m.x212) == 0)

m.c112 = Constraint(expr=m.x214 - (0.005*(m.x11*(m.x112 - 10*m.x213) - (1 - m.x11)*m.x213 + m.x12*(m.x113 - 10*m.x214)
                          - (1 - m.x12)*m.x214) + m.x213) == 0)

m.c113 = Constraint(expr=m.x215 - (0.005*(m.x12*(m.x113 - 10*m.x214) - (1 - m.x12)*m.x214 + m.x13*(m.x114 - 10*m.x215)
                          - (1 - m.x13)*m.x215) + m.x214) == 0)

m.c114 = Constraint(expr=m.x216 - (0.005*(m.x13*(m.x114 - 10*m.x215) - (1 - m.x13)*m.x215 + m.x14*(m.x115 - 10*m.x216)
                          - (1 - m.x14)*m.x216) + m.x215) == 0)

m.c115 = Constraint(expr=m.x217 - (0.005*(m.x14*(m.x115 - 10*m.x216) - (1 - m.x14)*m.x216 + m.x15*(m.x116 - 10*m.x217)
                          - (1 - m.x15)*m.x217) + m.x216) == 0)

m.c116 = Constraint(expr=m.x218 - (0.005*(m.x15*(m.x116 - 10*m.x217) - (1 - m.x15)*m.x217 + m.x16*(m.x117 - 10*m.x218)
                          - (1 - m.x16)*m.x218) + m.x217) == 0)

m.c117 = Constraint(expr=m.x219 - (0.005*(m.x16*(m.x117 - 10*m.x218) - (1 - m.x16)*m.x218 + m.x17*(m.x118 - 10*m.x219)
                          - (1 - m.x17)*m.x219) + m.x218) == 0)

m.c118 = Constraint(expr=m.x220 - (0.005*(m.x17*(m.x118 - 10*m.x219) - (1 - m.x17)*m.x219 + m.x18*(m.x119 - 10*m.x220)
                          - (1 - m.x18)*m.x220) + m.x219) == 0)

m.c119 = Constraint(expr=m.x221 - (0.005*(m.x18*(m.x119 - 10*m.x220) - (1 - m.x18)*m.x220 + m.x19*(m.x120 - 10*m.x221)
                          - (1 - m.x19)*m.x221) + m.x220) == 0)

m.c120 = Constraint(expr=m.x222 - (0.005*(m.x19*(m.x120 - 10*m.x221) - (1 - m.x19)*m.x221 + m.x20*(m.x121 - 10*m.x222)
                          - (1 - m.x20)*m.x222) + m.x221) == 0)

m.c121 = Constraint(expr=m.x223 - (0.005*(m.x20*(m.x121 - 10*m.x222) - (1 - m.x20)*m.x222 + m.x21*(m.x122 - 10*m.x223)
                          - (1 - m.x21)*m.x223) + m.x222) == 0)

m.c122 = Constraint(expr=m.x224 - (0.005*(m.x21*(m.x122 - 10*m.x223) - (1 - m.x21)*m.x223 + m.x22*(m.x123 - 10*m.x224)
                          - (1 - m.x22)*m.x224) + m.x223) == 0)

m.c123 = Constraint(expr=m.x225 - (0.005*(m.x22*(m.x123 - 10*m.x224) - (1 - m.x22)*m.x224 + m.x23*(m.x124 - 10*m.x225)
                          - (1 - m.x23)*m.x225) + m.x224) == 0)

m.c124 = Constraint(expr=m.x226 - (0.005*(m.x23*(m.x124 - 10*m.x225) - (1 - m.x23)*m.x225 + m.x24*(m.x125 - 10*m.x226)
                          - (1 - m.x24)*m.x226) + m.x225) == 0)

m.c125 = Constraint(expr=m.x227 - (0.005*(m.x24*(m.x125 - 10*m.x226) - (1 - m.x24)*m.x226 + m.x25*(m.x126 - 10*m.x227)
                          - (1 - m.x25)*m.x227) + m.x226) == 0)

m.c126 = Constraint(expr=m.x228 - (0.005*(m.x25*(m.x126 - 10*m.x227) - (1 - m.x25)*m.x227 + m.x26*(m.x127 - 10*m.x228)
                          - (1 - m.x26)*m.x228) + m.x227) == 0)

m.c127 = Constraint(expr=m.x229 - (0.005*(m.x26*(m.x127 - 10*m.x228) - (1 - m.x26)*m.x228 + m.x27*(m.x128 - 10*m.x229)
                          - (1 - m.x27)*m.x229) + m.x228) == 0)

m.c128 = Constraint(expr=m.x230 - (0.005*(m.x27*(m.x128 - 10*m.x229) - (1 - m.x27)*m.x229 + m.x28*(m.x129 - 10*m.x230)
                          - (1 - m.x28)*m.x230) + m.x229) == 0)

m.c129 = Constraint(expr=m.x231 - (0.005*(m.x28*(m.x129 - 10*m.x230) - (1 - m.x28)*m.x230 + m.x29*(m.x130 - 10*m.x231)
                          - (1 - m.x29)*m.x231) + m.x230) == 0)

m.c130 = Constraint(expr=m.x232 - (0.005*(m.x29*(m.x130 - 10*m.x231) - (1 - m.x29)*m.x231 + m.x30*(m.x131 - 10*m.x232)
                          - (1 - m.x30)*m.x232) + m.x231) == 0)

m.c131 = Constraint(expr=m.x233 - (0.005*(m.x30*(m.x131 - 10*m.x232) - (1 - m.x30)*m.x232 + m.x31*(m.x132 - 10*m.x233)
                          - (1 - m.x31)*m.x233) + m.x232) == 0)

m.c132 = Constraint(expr=m.x234 - (0.005*(m.x31*(m.x132 - 10*m.x233) - (1 - m.x31)*m.x233 + m.x32*(m.x133 - 10*m.x234)
                          - (1 - m.x32)*m.x234) + m.x233) == 0)

m.c133 = Constraint(expr=m.x235 - (0.005*(m.x32*(m.x133 - 10*m.x234) - (1 - m.x32)*m.x234 + m.x33*(m.x134 - 10*m.x235)
                          - (1 - m.x33)*m.x235) + m.x234) == 0)

m.c134 = Constraint(expr=m.x236 - (0.005*(m.x33*(m.x134 - 10*m.x235) - (1 - m.x33)*m.x235 + m.x34*(m.x135 - 10*m.x236)
                          - (1 - m.x34)*m.x236) + m.x235) == 0)

m.c135 = Constraint(expr=m.x237 - (0.005*(m.x34*(m.x135 - 10*m.x236) - (1 - m.x34)*m.x236 + m.x35*(m.x136 - 10*m.x237)
                          - (1 - m.x35)*m.x237) + m.x236) == 0)

m.c136 = Constraint(expr=m.x238 - (0.005*(m.x35*(m.x136 - 10*m.x237) - (1 - m.x35)*m.x237 + m.x36*(m.x137 - 10*m.x238)
                          - (1 - m.x36)*m.x238) + m.x237) == 0)

m.c137 = Constraint(expr=m.x239 - (0.005*(m.x36*(m.x137 - 10*m.x238) - (1 - m.x36)*m.x238 + m.x37*(m.x138 - 10*m.x239)
                          - (1 - m.x37)*m.x239) + m.x238) == 0)

m.c138 = Constraint(expr=m.x240 - (0.005*(m.x37*(m.x138 - 10*m.x239) - (1 - m.x37)*m.x239 + m.x38*(m.x139 - 10*m.x240)
                          - (1 - m.x38)*m.x240) + m.x239) == 0)

m.c139 = Constraint(expr=m.x241 - (0.005*(m.x38*(m.x139 - 10*m.x240) - (1 - m.x38)*m.x240 + m.x39*(m.x140 - 10*m.x241)
                          - (1 - m.x39)*m.x241) + m.x240) == 0)

m.c140 = Constraint(expr=m.x242 - (0.005*(m.x39*(m.x140 - 10*m.x241) - (1 - m.x39)*m.x241 + m.x40*(m.x141 - 10*m.x242)
                          - (1 - m.x40)*m.x242) + m.x241) == 0)

m.c141 = Constraint(expr=m.x243 - (0.005*(m.x40*(m.x141 - 10*m.x242) - (1 - m.x40)*m.x242 + m.x41*(m.x142 - 10*m.x243)
                          - (1 - m.x41)*m.x243) + m.x242) == 0)

m.c142 = Constraint(expr=m.x244 - (0.005*(m.x41*(m.x142 - 10*m.x243) - (1 - m.x41)*m.x243 + m.x42*(m.x143 - 10*m.x244)
                          - (1 - m.x42)*m.x244) + m.x243) == 0)

m.c143 = Constraint(expr=m.x245 - (0.005*(m.x42*(m.x143 - 10*m.x244) - (1 - m.x42)*m.x244 + m.x43*(m.x144 - 10*m.x245)
                          - (1 - m.x43)*m.x245) + m.x244) == 0)

m.c144 = Constraint(expr=m.x246 - (0.005*(m.x43*(m.x144 - 10*m.x245) - (1 - m.x43)*m.x245 + m.x44*(m.x145 - 10*m.x246)
                          - (1 - m.x44)*m.x246) + m.x245) == 0)

m.c145 = Constraint(expr=m.x247 - (0.005*(m.x44*(m.x145 - 10*m.x246) - (1 - m.x44)*m.x246 + m.x45*(m.x146 - 10*m.x247)
                          - (1 - m.x45)*m.x247) + m.x246) == 0)

m.c146 = Constraint(expr=m.x248 - (0.005*(m.x45*(m.x146 - 10*m.x247) - (1 - m.x45)*m.x247 + m.x46*(m.x147 - 10*m.x248)
                          - (1 - m.x46)*m.x248) + m.x247) == 0)

m.c147 = Constraint(expr=m.x249 - (0.005*(m.x46*(m.x147 - 10*m.x248) - (1 - m.x46)*m.x248 + m.x47*(m.x148 - 10*m.x249)
                          - (1 - m.x47)*m.x249) + m.x248) == 0)

m.c148 = Constraint(expr=m.x250 - (0.005*(m.x47*(m.x148 - 10*m.x249) - (1 - m.x47)*m.x249 + m.x48*(m.x149 - 10*m.x250)
                          - (1 - m.x48)*m.x250) + m.x249) == 0)

m.c149 = Constraint(expr=m.x251 - (0.005*(m.x48*(m.x149 - 10*m.x250) - (1 - m.x48)*m.x250 + m.x49*(m.x150 - 10*m.x251)
                          - (1 - m.x49)*m.x251) + m.x250) == 0)

m.c150 = Constraint(expr=m.x252 - (0.005*(m.x49*(m.x150 - 10*m.x251) - (1 - m.x49)*m.x251 + m.x50*(m.x151 - 10*m.x252)
                          - (1 - m.x50)*m.x252) + m.x251) == 0)

m.c151 = Constraint(expr=m.x253 - (0.005*(m.x50*(m.x151 - 10*m.x252) - (1 - m.x50)*m.x252 + m.x51*(m.x152 - 10*m.x253)
                          - (1 - m.x51)*m.x253) + m.x252) == 0)

m.c152 = Constraint(expr=m.x254 - (0.005*(m.x51*(m.x152 - 10*m.x253) - (1 - m.x51)*m.x253 + m.x52*(m.x153 - 10*m.x254)
                          - (1 - m.x52)*m.x254) + m.x253) == 0)

m.c153 = Constraint(expr=m.x255 - (0.005*(m.x52*(m.x153 - 10*m.x254) - (1 - m.x52)*m.x254 + m.x53*(m.x154 - 10*m.x255)
                          - (1 - m.x53)*m.x255) + m.x254) == 0)

m.c154 = Constraint(expr=m.x256 - (0.005*(m.x53*(m.x154 - 10*m.x255) - (1 - m.x53)*m.x255 + m.x54*(m.x155 - 10*m.x256)
                          - (1 - m.x54)*m.x256) + m.x255) == 0)

m.c155 = Constraint(expr=m.x257 - (0.005*(m.x54*(m.x155 - 10*m.x256) - (1 - m.x54)*m.x256 + m.x55*(m.x156 - 10*m.x257)
                          - (1 - m.x55)*m.x257) + m.x256) == 0)

m.c156 = Constraint(expr=m.x258 - (0.005*(m.x55*(m.x156 - 10*m.x257) - (1 - m.x55)*m.x257 + m.x56*(m.x157 - 10*m.x258)
                          - (1 - m.x56)*m.x258) + m.x257) == 0)

m.c157 = Constraint(expr=m.x259 - (0.005*(m.x56*(m.x157 - 10*m.x258) - (1 - m.x56)*m.x258 + m.x57*(m.x158 - 10*m.x259)
                          - (1 - m.x57)*m.x259) + m.x258) == 0)

m.c158 = Constraint(expr=m.x260 - (0.005*(m.x57*(m.x158 - 10*m.x259) - (1 - m.x57)*m.x259 + m.x58*(m.x159 - 10*m.x260)
                          - (1 - m.x58)*m.x260) + m.x259) == 0)

m.c159 = Constraint(expr=m.x261 - (0.005*(m.x58*(m.x159 - 10*m.x260) - (1 - m.x58)*m.x260 + m.x59*(m.x160 - 10*m.x261)
                          - (1 - m.x59)*m.x261) + m.x260) == 0)

m.c160 = Constraint(expr=m.x262 - (0.005*(m.x59*(m.x160 - 10*m.x261) - (1 - m.x59)*m.x261 + m.x60*(m.x161 - 10*m.x262)
                          - (1 - m.x60)*m.x262) + m.x261) == 0)

m.c161 = Constraint(expr=m.x263 - (0.005*(m.x60*(m.x161 - 10*m.x262) - (1 - m.x60)*m.x262 + m.x61*(m.x162 - 10*m.x263)
                          - (1 - m.x61)*m.x263) + m.x262) == 0)

m.c162 = Constraint(expr=m.x264 - (0.005*(m.x61*(m.x162 - 10*m.x263) - (1 - m.x61)*m.x263 + m.x62*(m.x163 - 10*m.x264)
                          - (1 - m.x62)*m.x264) + m.x263) == 0)

m.c163 = Constraint(expr=m.x265 - (0.005*(m.x62*(m.x163 - 10*m.x264) - (1 - m.x62)*m.x264 + m.x63*(m.x164 - 10*m.x265)
                          - (1 - m.x63)*m.x265) + m.x264) == 0)

m.c164 = Constraint(expr=m.x266 - (0.005*(m.x63*(m.x164 - 10*m.x265) - (1 - m.x63)*m.x265 + m.x64*(m.x165 - 10*m.x266)
                          - (1 - m.x64)*m.x266) + m.x265) == 0)

m.c165 = Constraint(expr=m.x267 - (0.005*(m.x64*(m.x165 - 10*m.x266) - (1 - m.x64)*m.x266 + m.x65*(m.x166 - 10*m.x267)
                          - (1 - m.x65)*m.x267) + m.x266) == 0)

m.c166 = Constraint(expr=m.x268 - (0.005*(m.x65*(m.x166 - 10*m.x267) - (1 - m.x65)*m.x267 + m.x66*(m.x167 - 10*m.x268)
                          - (1 - m.x66)*m.x268) + m.x267) == 0)

m.c167 = Constraint(expr=m.x269 - (0.005*(m.x66*(m.x167 - 10*m.x268) - (1 - m.x66)*m.x268 + m.x67*(m.x168 - 10*m.x269)
                          - (1 - m.x67)*m.x269) + m.x268) == 0)

m.c168 = Constraint(expr=m.x270 - (0.005*(m.x67*(m.x168 - 10*m.x269) - (1 - m.x67)*m.x269 + m.x68*(m.x169 - 10*m.x270)
                          - (1 - m.x68)*m.x270) + m.x269) == 0)

m.c169 = Constraint(expr=m.x271 - (0.005*(m.x68*(m.x169 - 10*m.x270) - (1 - m.x68)*m.x270 + m.x69*(m.x170 - 10*m.x271)
                          - (1 - m.x69)*m.x271) + m.x270) == 0)

m.c170 = Constraint(expr=m.x272 - (0.005*(m.x69*(m.x170 - 10*m.x271) - (1 - m.x69)*m.x271 + m.x70*(m.x171 - 10*m.x272)
                          - (1 - m.x70)*m.x272) + m.x271) == 0)

m.c171 = Constraint(expr=m.x273 - (0.005*(m.x70*(m.x171 - 10*m.x272) - (1 - m.x70)*m.x272 + m.x71*(m.x172 - 10*m.x273)
                          - (1 - m.x71)*m.x273) + m.x272) == 0)

m.c172 = Constraint(expr=m.x274 - (0.005*(m.x71*(m.x172 - 10*m.x273) - (1 - m.x71)*m.x273 + m.x72*(m.x173 - 10*m.x274)
                          - (1 - m.x72)*m.x274) + m.x273) == 0)

m.c173 = Constraint(expr=m.x275 - (0.005*(m.x72*(m.x173 - 10*m.x274) - (1 - m.x72)*m.x274 + m.x73*(m.x174 - 10*m.x275)
                          - (1 - m.x73)*m.x275) + m.x274) == 0)

m.c174 = Constraint(expr=m.x276 - (0.005*(m.x73*(m.x174 - 10*m.x275) - (1 - m.x73)*m.x275 + m.x74*(m.x175 - 10*m.x276)
                          - (1 - m.x74)*m.x276) + m.x275) == 0)

m.c175 = Constraint(expr=m.x277 - (0.005*(m.x74*(m.x175 - 10*m.x276) - (1 - m.x74)*m.x276 + m.x75*(m.x176 - 10*m.x277)
                          - (1 - m.x75)*m.x277) + m.x276) == 0)

m.c176 = Constraint(expr=m.x278 - (0.005*(m.x75*(m.x176 - 10*m.x277) - (1 - m.x75)*m.x277 + m.x76*(m.x177 - 10*m.x278)
                          - (1 - m.x76)*m.x278) + m.x277) == 0)

m.c177 = Constraint(expr=m.x279 - (0.005*(m.x76*(m.x177 - 10*m.x278) - (1 - m.x76)*m.x278 + m.x77*(m.x178 - 10*m.x279)
                          - (1 - m.x77)*m.x279) + m.x278) == 0)

m.c178 = Constraint(expr=m.x280 - (0.005*(m.x77*(m.x178 - 10*m.x279) - (1 - m.x77)*m.x279 + m.x78*(m.x179 - 10*m.x280)
                          - (1 - m.x78)*m.x280) + m.x279) == 0)

m.c179 = Constraint(expr=m.x281 - (0.005*(m.x78*(m.x179 - 10*m.x280) - (1 - m.x78)*m.x280 + m.x79*(m.x180 - 10*m.x281)
                          - (1 - m.x79)*m.x281) + m.x280) == 0)

m.c180 = Constraint(expr=m.x282 - (0.005*(m.x79*(m.x180 - 10*m.x281) - (1 - m.x79)*m.x281 + m.x80*(m.x181 - 10*m.x282)
                          - (1 - m.x80)*m.x282) + m.x281) == 0)

m.c181 = Constraint(expr=m.x283 - (0.005*(m.x80*(m.x181 - 10*m.x282) - (1 - m.x80)*m.x282 + m.x81*(m.x182 - 10*m.x283)
                          - (1 - m.x81)*m.x283) + m.x282) == 0)

m.c182 = Constraint(expr=m.x284 - (0.005*(m.x81*(m.x182 - 10*m.x283) - (1 - m.x81)*m.x283 + m.x82*(m.x183 - 10*m.x284)
                          - (1 - m.x82)*m.x284) + m.x283) == 0)

m.c183 = Constraint(expr=m.x285 - (0.005*(m.x82*(m.x183 - 10*m.x284) - (1 - m.x82)*m.x284 + m.x83*(m.x184 - 10*m.x285)
                          - (1 - m.x83)*m.x285) + m.x284) == 0)

m.c184 = Constraint(expr=m.x286 - (0.005*(m.x83*(m.x184 - 10*m.x285) - (1 - m.x83)*m.x285 + m.x84*(m.x185 - 10*m.x286)
                          - (1 - m.x84)*m.x286) + m.x285) == 0)

m.c185 = Constraint(expr=m.x287 - (0.005*(m.x84*(m.x185 - 10*m.x286) - (1 - m.x84)*m.x286 + m.x85*(m.x186 - 10*m.x287)
                          - (1 - m.x85)*m.x287) + m.x286) == 0)

m.c186 = Constraint(expr=m.x288 - (0.005*(m.x85*(m.x186 - 10*m.x287) - (1 - m.x85)*m.x287 + m.x86*(m.x187 - 10*m.x288)
                          - (1 - m.x86)*m.x288) + m.x287) == 0)

m.c187 = Constraint(expr=m.x289 - (0.005*(m.x86*(m.x187 - 10*m.x288) - (1 - m.x86)*m.x288 + m.x87*(m.x188 - 10*m.x289)
                          - (1 - m.x87)*m.x289) + m.x288) == 0)

m.c188 = Constraint(expr=m.x290 - (0.005*(m.x87*(m.x188 - 10*m.x289) - (1 - m.x87)*m.x289 + m.x88*(m.x189 - 10*m.x290)
                          - (1 - m.x88)*m.x290) + m.x289) == 0)

m.c189 = Constraint(expr=m.x291 - (0.005*(m.x88*(m.x189 - 10*m.x290) - (1 - m.x88)*m.x290 + m.x89*(m.x190 - 10*m.x291)
                          - (1 - m.x89)*m.x291) + m.x290) == 0)

m.c190 = Constraint(expr=m.x292 - (0.005*(m.x89*(m.x190 - 10*m.x291) - (1 - m.x89)*m.x291 + m.x90*(m.x191 - 10*m.x292)
                          - (1 - m.x90)*m.x292) + m.x291) == 0)

m.c191 = Constraint(expr=m.x293 - (0.005*(m.x90*(m.x191 - 10*m.x292) - (1 - m.x90)*m.x292 + m.x91*(m.x192 - 10*m.x293)
                          - (1 - m.x91)*m.x293) + m.x292) == 0)

m.c192 = Constraint(expr=m.x294 - (0.005*(m.x91*(m.x192 - 10*m.x293) - (1 - m.x91)*m.x293 + m.x92*(m.x193 - 10*m.x294)
                          - (1 - m.x92)*m.x294) + m.x293) == 0)

m.c193 = Constraint(expr=m.x295 - (0.005*(m.x92*(m.x193 - 10*m.x294) - (1 - m.x92)*m.x294 + m.x93*(m.x194 - 10*m.x295)
                          - (1 - m.x93)*m.x295) + m.x294) == 0)

m.c194 = Constraint(expr=m.x296 - (0.005*(m.x93*(m.x194 - 10*m.x295) - (1 - m.x93)*m.x295 + m.x94*(m.x195 - 10*m.x296)
                          - (1 - m.x94)*m.x296) + m.x295) == 0)

m.c195 = Constraint(expr=m.x297 - (0.005*(m.x94*(m.x195 - 10*m.x296) - (1 - m.x94)*m.x296 + m.x95*(m.x196 - 10*m.x297)
                          - (1 - m.x95)*m.x297) + m.x296) == 0)

m.c196 = Constraint(expr=m.x298 - (0.005*(m.x95*(m.x196 - 10*m.x297) - (1 - m.x95)*m.x297 + m.x96*(m.x197 - 10*m.x298)
                          - (1 - m.x96)*m.x298) + m.x297) == 0)

m.c197 = Constraint(expr=m.x299 - (0.005*(m.x96*(m.x197 - 10*m.x298) - (1 - m.x96)*m.x298 + m.x97*(m.x198 - 10*m.x299)
                          - (1 - m.x97)*m.x299) + m.x298) == 0)

m.c198 = Constraint(expr=m.x300 - (0.005*(m.x97*(m.x198 - 10*m.x299) - (1 - m.x97)*m.x299 + m.x98*(m.x199 - 10*m.x300)
                          - (1 - m.x98)*m.x300) + m.x299) == 0)

m.c199 = Constraint(expr=m.x301 - (0.005*(m.x98*(m.x199 - 10*m.x300) - (1 - m.x98)*m.x300 + m.x99*(m.x200 - 10*m.x301)
                          - (1 - m.x99)*m.x301) + m.x300) == 0)

m.c200 = Constraint(expr=m.x302 - (0.005*(m.x99*(m.x200 - 10*m.x301) - (1 - m.x99)*m.x301 + m.x100*(m.x201 - 10*m.x302)
                          - (1 - m.x100)*m.x302) + m.x301) == 0)

m.c201 = Constraint(expr=m.x303 - (0.005*(m.x100*(m.x201 - 10*m.x302) - (1 - m.x100)*m.x302 + m.x101*(m.x202 - 10*m.x303
                         ) - (1 - m.x101)*m.x303) + m.x302) == 0)
