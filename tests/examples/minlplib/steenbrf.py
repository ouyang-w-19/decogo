#  NLP written by GAMS Convert at 04/21/18 13:54:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        109      109        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        469      469        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        973      865      108        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x2 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x7 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x8 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x13 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x14 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x19 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x20 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x25 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x26 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x31 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x32 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x34 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x37 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x38 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x43 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x44 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x49 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x50 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x55 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x56 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x58 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x60 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x61 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x62 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x63 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x64 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x65 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x66 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x67 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x68 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x69 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x70 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x71 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x72 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x73 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x74 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x75 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x76 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x77 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x78 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x79 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x80 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x81 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x82 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x83 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x84 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x85 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x86 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x87 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x88 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x89 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x90 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x91 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x92 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x93 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x95 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x96 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x97 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x98 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x100 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x101 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x102 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x103 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x104 = Var(within=Reals,bounds=(0.01,None),initialize=0.1)
m.x105 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x106 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x107 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x108 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x109 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x110 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x111 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x112 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x113 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x114 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x115 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x116 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x117 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x118 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x119 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x120 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x121 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x122 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x123 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x124 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x125 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x126 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x127 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x128 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x129 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x130 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x131 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x132 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x133 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x134 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x135 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x136 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x137 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x138 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x139 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x140 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x141 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x142 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x143 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x144 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x145 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x146 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x147 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x148 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x149 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x150 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x151 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x152 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x153 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x154 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x155 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x156 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x157 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x158 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x159 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x160 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x161 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x162 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x163 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x164 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x165 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x166 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x167 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x168 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x169 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x170 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x171 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x172 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x173 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x174 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x175 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x176 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x177 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x178 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x179 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x180 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x181 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x182 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x183 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x184 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x185 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x186 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x187 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x188 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x189 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x190 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x191 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x192 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x193 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x194 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x195 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x196 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x197 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x198 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x199 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x200 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x201 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x202 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x203 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x204 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x205 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x206 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x207 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x208 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x209 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x210 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x211 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x212 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x213 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x214 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x215 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x216 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x217 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x218 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x219 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x220 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x221 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x222 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x223 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x224 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x225 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x226 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x227 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x228 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x229 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x230 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x231 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x232 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x233 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x234 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x235 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x236 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x237 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x238 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x239 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x240 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x241 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x242 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x243 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x244 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x245 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x246 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x247 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x248 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x249 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x250 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x251 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x252 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x253 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x254 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x255 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x256 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x257 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x258 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x259 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x260 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x261 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x262 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x263 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x264 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x265 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x266 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x267 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x268 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x269 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x270 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x271 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x272 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x273 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x274 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x275 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x276 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x277 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x278 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x279 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x280 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x281 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x282 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x283 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x284 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x285 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x286 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x287 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x288 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x289 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x290 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x291 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x292 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x293 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x294 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x295 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x296 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x297 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x298 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x299 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x300 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x301 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x302 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x303 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x304 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x305 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x306 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x307 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x308 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x309 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x310 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x311 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x312 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x313 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x314 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x315 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x316 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x317 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x318 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x319 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x320 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x321 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x322 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x323 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x324 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x325 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x326 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x327 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x328 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x329 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x330 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x331 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x332 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x333 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x334 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x335 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x336 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x337 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x338 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x339 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x340 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x341 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x342 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x343 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x344 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x345 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x346 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x347 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x348 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x349 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x350 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x351 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x352 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x353 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x354 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x355 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x356 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x357 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x358 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x359 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x360 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x361 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x362 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x363 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x364 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x365 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x366 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x367 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x368 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x369 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x370 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x371 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x372 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x373 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x374 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x375 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x376 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x377 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x378 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x379 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x380 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x381 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x382 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x383 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x384 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x385 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x386 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x387 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x388 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x389 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x390 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x391 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x392 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x393 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x394 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x395 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x396 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x397 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x398 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x399 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x400 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x401 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x402 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x403 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x404 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x405 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x406 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x407 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x408 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x409 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x410 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x411 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x412 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x413 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x414 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x415 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x416 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x417 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x418 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x419 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x420 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x421 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x422 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x423 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x424 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x425 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x426 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x427 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x428 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x429 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x430 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x431 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x432 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x433 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x434 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x435 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x436 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x437 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x438 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x439 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x440 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x441 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x442 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x443 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x444 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x445 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x446 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x447 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x448 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x449 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x450 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x451 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x452 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x453 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x454 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x455 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x456 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x457 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x458 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x459 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x460 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x461 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x462 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x463 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x464 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x465 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x466 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x467 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x468 = Var(within=Reals,bounds=(0,None),initialize=0.1)

m.obj = Objective(expr=-(-0.5*sqrt(m.x104) - 0.5*sqrt(m.x103) - 0.5*((m.x106 + m.x108)*(m.x106 + m.x108)*m.x106 + m.x108
                       )/(m.x104*m.x104) - 0.5*((m.x105 + m.x107)*(m.x105 + m.x107)*m.x105 + m.x107)/(m.x103*m.x103) - 
                       0.5*sqrt(m.x98) - 0.5*sqrt(m.x97) - 0.5*((m.x100 + m.x102)*(m.x100 + m.x102)*m.x100 + m.x102)/(
                       m.x98*m.x98) - 0.5*((m.x99 + m.x101)*(m.x99 + m.x101)*m.x99 + m.x101)/(m.x97*m.x97) - 0.3*sqrt(
                       m.x92) - 0.3*sqrt(m.x91) - 0.3*((m.x94 + m.x96)*(m.x94 + m.x96)*m.x94 + m.x96)/(m.x92*m.x92) - 
                       0.3*((m.x93 + m.x95)*(m.x93 + m.x95)*m.x93 + m.x95)/(m.x91*m.x91) - 0.25*sqrt(m.x86) - 0.25*sqrt(
                       m.x85) - 0.25*((m.x88 + m.x90)*(m.x88 + m.x90)*m.x88 + m.x90)/(m.x86*m.x86) - 0.25*((m.x87 + 
                       m.x89)*(m.x87 + m.x89)*m.x87 + m.x89)/(m.x85*m.x85) - 0.6*sqrt(m.x80) - 0.6*sqrt(m.x79) - 0.6*((
                       m.x82 + m.x84)*(m.x82 + m.x84)*m.x82 + m.x84)/(m.x80*m.x80) - 0.6*((m.x81 + m.x83)*(m.x81 + m.x83
                       )*m.x81 + m.x83)/(m.x79*m.x79) - 0.4*sqrt(m.x74) - 0.4*sqrt(m.x73) - 0.4*((m.x76 + m.x78)*(m.x76
                        + m.x78)*m.x76 + m.x78)/(m.x74*m.x74) - 0.4*((m.x75 + m.x77)*(m.x75 + m.x77)*m.x75 + m.x77)/(
                       m.x73*m.x73) - 0.15*sqrt(m.x68) - 0.15*sqrt(m.x67) - 0.15*((m.x70 + m.x72)*(m.x70 + m.x72)*m.x70
                        + m.x72)/(m.x68*m.x68) - 0.15*((m.x69 + m.x71)*(m.x69 + m.x71)*m.x69 + m.x71)/(m.x67*m.x67) - 
                       0.55*sqrt(m.x62) - 0.55*sqrt(m.x61) - 0.55*((m.x64 + m.x66)*(m.x64 + m.x66)*m.x64 + m.x66)/(m.x62
                       *m.x62) - 0.55*((m.x63 + m.x65)*(m.x63 + m.x65)*m.x63 + m.x65)/(m.x61*m.x61) - 0.35*sqrt(m.x56)
                        - 0.35*sqrt(m.x55) - 0.35*((m.x58 + m.x60)*(m.x58 + m.x60)*m.x58 + m.x60)/(m.x56*m.x56) - 0.35*(
                       (m.x57 + m.x59)*(m.x57 + m.x59)*m.x57 + m.x59)/(m.x55*m.x55) - 0.6*sqrt(m.x50) - 0.6*sqrt(m.x49)
                        - 0.6*((m.x52 + m.x54)*(m.x52 + m.x54)*m.x52 + m.x54)/(m.x50*m.x50) - 0.6*((m.x51 + m.x53)*(
                       m.x51 + m.x53)*m.x51 + m.x53)/(m.x49*m.x49) - 0.25*sqrt(m.x44) - 0.25*sqrt(m.x43) - 0.25*((m.x46
                        + m.x48)*(m.x46 + m.x48)*m.x46 + m.x48)/(m.x44*m.x44) - 0.25*((m.x45 + m.x47)*(m.x45 + m.x47)*
                       m.x45 + m.x47)/(m.x43*m.x43) - sqrt(m.x38) - sqrt(m.x37) - ((m.x40 + m.x42)*(m.x40 + m.x42)*m.x40
                        + m.x42)/(m.x38*m.x38) - ((m.x39 + m.x41)*(m.x39 + m.x41)*m.x39 + m.x41)/(m.x37*m.x37) - 0.55*
                       sqrt(m.x32) - 0.55*sqrt(m.x31) - 0.55*((m.x34 + m.x36)*(m.x34 + m.x36)*m.x34 + m.x36)/(m.x32*
                       m.x32) - 0.55*((m.x33 + m.x35)*(m.x33 + m.x35)*m.x33 + m.x35)/(m.x31*m.x31) - 0.15*sqrt(m.x26) - 
                       0.15*sqrt(m.x25) - 0.15*((m.x28 + m.x30)*(m.x28 + m.x30)*m.x28 + m.x30)/(m.x26*m.x26) - 0.15*((
                       m.x27 + m.x29)*(m.x27 + m.x29)*m.x27 + m.x29)/(m.x25*m.x25) - 0.5*sqrt(m.x20) - 0.5*sqrt(m.x19)
                        - ((m.x22 + m.x24)*(m.x22 + m.x24)*m.x22 + m.x24)/(m.x20*m.x20) - ((m.x21 + m.x23)*(m.x21 + 
                       m.x23)*m.x21 + m.x23)/(m.x19*m.x19) - 0.3*sqrt(m.x14) - 0.3*sqrt(m.x13) - 0.3*((m.x16 + m.x18)*(
                       m.x16 + m.x18)*m.x16 + m.x18)/(m.x14*m.x14) - 0.3*((m.x15 + m.x17)*(m.x15 + m.x17)*m.x15 + m.x17)
                       /(m.x13*m.x13) - 0.4*sqrt(m.x8) - 0.4*sqrt(m.x7) - 0.4*((m.x10 + m.x12)*(m.x10 + m.x12)*m.x10 + 
                       m.x12)/(m.x8*m.x8) - 0.4*((m.x9 + m.x11)*(m.x9 + m.x11)*m.x9 + m.x11)/(m.x7*m.x7) - 0.35*sqrt(
                       m.x2) - 0.35*sqrt(m.x1) - 0.35*((m.x4 + m.x6)*(m.x4 + m.x6)*m.x4 + m.x6)/(m.x2*m.x2) - 0.35*((
                       m.x3 + m.x5)*(m.x3 + m.x5)*m.x3 + m.x5)/(m.x1*m.x1) - 0.35*m.x3 - 0.35*m.x5 - 0.5*m.x106 - 0.5*
                       m.x108 - 0.5*m.x105 - 0.5*m.x107 - 0.5*m.x100 - 0.5*m.x102 - 0.5*m.x99 - 0.5*m.x101 - 0.3*m.x94
                        - 0.3*m.x96 - 0.3*m.x93 - 0.3*m.x95 - 0.25*m.x88 - 0.25*m.x90 - 0.25*m.x87 - 0.25*m.x89 - 0.6*
                       m.x82 - 0.6*m.x84 - 0.6*m.x81 - 0.6*m.x83 - 0.4*m.x76 - 0.4*m.x78 - 0.4*m.x75 - 0.4*m.x77 - 0.15*
                       m.x70 - 0.15*m.x72 - 0.15*m.x69 - 0.15*m.x71 - 0.55*m.x64 - 0.55*m.x66 - 0.55*m.x63 - 0.55*m.x65
                        - 0.35*m.x58 - 0.35*m.x60 - 0.35*m.x57 - 0.35*m.x59 - 0.6*m.x52 - 0.6*m.x54 - 0.6*m.x51 - 0.6*
                       m.x53 - 0.25*m.x46 - 0.25*m.x48 - 0.25*m.x45 - 0.25*m.x47 - m.x40 - m.x42 - m.x39 - m.x41 - 0.55*
                       m.x34 - 0.55*m.x36 - 0.55*m.x33 - 0.55*m.x35 - 0.15*m.x28 - 0.15*m.x30 - 0.15*m.x27 - 0.15*m.x29
                        - m.x22 - m.x24 - m.x21 - m.x23 - 0.3*m.x16 - 0.3*m.x18 - 0.3*m.x15 - 0.3*m.x17 - 0.4*m.x10 - 
                       0.4*m.x12 - 0.4*m.x9 - 0.4*m.x11 - 0.35*m.x4 - 0.35*m.x6), sense=minimize)

m.c1 = Constraint(expr=   m.x427 - m.x428 + m.x447 - m.x448 + m.x467 - m.x468 == 0)

m.c2 = Constraint(expr=   m.x367 - m.x368 + m.x387 - m.x388 + m.x407 - m.x408 - m.x467 + m.x468 == -2000)

m.c3 = Constraint(expr=   m.x307 - m.x308 + m.x327 - m.x328 + m.x347 - m.x348 - m.x447 + m.x448 == 2000)

m.c4 = Constraint(expr=   m.x247 - m.x248 + m.x267 - m.x268 + m.x287 - m.x288 - m.x407 + m.x408 == 0)

m.c5 = Constraint(expr=   m.x187 - m.x188 + m.x207 - m.x208 + m.x227 - m.x228 - m.x347 + m.x348 == 0)

m.c6 = Constraint(expr=   m.x167 - m.x168 - m.x227 + m.x228 - m.x287 + m.x288 == 0)

m.c7 = Constraint(expr=   m.x147 - m.x148 - m.x327 + m.x328 - m.x387 + m.x388 - m.x427 + m.x428 == 0)

m.c8 = Constraint(expr=   m.x127 - m.x128 - m.x147 + m.x148 - m.x207 + m.x208 - m.x267 + m.x268 - m.x307 + m.x308
                        - m.x367 + m.x368 == 0)

m.c9 = Constraint(expr= - m.x127 + m.x128 - m.x167 + m.x168 - m.x187 + m.x188 - m.x247 + m.x248 == 0)

m.c10 = Constraint(expr=   m.x425 - m.x426 + m.x445 - m.x446 + m.x465 - m.x466 == 0)

m.c11 = Constraint(expr=   m.x365 - m.x366 + m.x385 - m.x386 + m.x405 - m.x406 - m.x465 + m.x466 == -2000)

m.c12 = Constraint(expr=   m.x305 - m.x306 + m.x325 - m.x326 + m.x345 - m.x346 - m.x445 + m.x446 == 0)

m.c13 = Constraint(expr=   m.x245 - m.x246 + m.x265 - m.x266 + m.x285 - m.x286 - m.x405 + m.x406 == 2000)

m.c14 = Constraint(expr=   m.x185 - m.x186 + m.x205 - m.x206 + m.x225 - m.x226 - m.x345 + m.x346 == 0)

m.c15 = Constraint(expr=   m.x165 - m.x166 - m.x225 + m.x226 - m.x285 + m.x286 == 0)

m.c16 = Constraint(expr=   m.x145 - m.x146 - m.x325 + m.x326 - m.x385 + m.x386 - m.x425 + m.x426 == 0)

m.c17 = Constraint(expr=   m.x125 - m.x126 - m.x145 + m.x146 - m.x205 + m.x206 - m.x265 + m.x266 - m.x305 + m.x306
                         - m.x365 + m.x366 == 0)

m.c18 = Constraint(expr= - m.x125 + m.x126 - m.x165 + m.x166 - m.x185 + m.x186 - m.x245 + m.x246 == 0)

m.c19 = Constraint(expr=   m.x423 - m.x424 + m.x443 - m.x444 + m.x463 - m.x464 == 0)

m.c20 = Constraint(expr=   m.x363 - m.x364 + m.x383 - m.x384 + m.x403 - m.x404 - m.x463 + m.x464 == -1000)

m.c21 = Constraint(expr=   m.x303 - m.x304 + m.x323 - m.x324 + m.x343 - m.x344 - m.x443 + m.x444 == 0)

m.c22 = Constraint(expr=   m.x243 - m.x244 + m.x263 - m.x264 + m.x283 - m.x284 - m.x403 + m.x404 == 0)

m.c23 = Constraint(expr=   m.x183 - m.x184 + m.x203 - m.x204 + m.x223 - m.x224 - m.x343 + m.x344 == 1000)

m.c24 = Constraint(expr=   m.x163 - m.x164 - m.x223 + m.x224 - m.x283 + m.x284 == 0)

m.c25 = Constraint(expr=   m.x143 - m.x144 - m.x323 + m.x324 - m.x383 + m.x384 - m.x423 + m.x424 == 0)

m.c26 = Constraint(expr=   m.x123 - m.x124 - m.x143 + m.x144 - m.x203 + m.x204 - m.x263 + m.x264 - m.x303 + m.x304
                         - m.x363 + m.x364 == 0)

m.c27 = Constraint(expr= - m.x123 + m.x124 - m.x163 + m.x164 - m.x183 + m.x184 - m.x243 + m.x244 == 0)

m.c28 = Constraint(expr=   m.x421 - m.x422 + m.x441 - m.x442 + m.x461 - m.x462 == 0)

m.c29 = Constraint(expr=   m.x361 - m.x362 + m.x381 - m.x382 + m.x401 - m.x402 - m.x461 + m.x462 == 0)

m.c30 = Constraint(expr=   m.x301 - m.x302 + m.x321 - m.x322 + m.x341 - m.x342 - m.x441 + m.x442 == -1000)

m.c31 = Constraint(expr=   m.x241 - m.x242 + m.x261 - m.x262 + m.x281 - m.x282 - m.x401 + m.x402 == 1000)

m.c32 = Constraint(expr=   m.x181 - m.x182 + m.x201 - m.x202 + m.x221 - m.x222 - m.x341 + m.x342 == 0)

m.c33 = Constraint(expr=   m.x161 - m.x162 - m.x221 + m.x222 - m.x281 + m.x282 == 0)

m.c34 = Constraint(expr=   m.x141 - m.x142 - m.x321 + m.x322 - m.x381 + m.x382 - m.x421 + m.x422 == 0)

m.c35 = Constraint(expr=   m.x121 - m.x122 - m.x141 + m.x142 - m.x201 + m.x202 - m.x261 + m.x262 - m.x301 + m.x302
                         - m.x361 + m.x362 == 0)

m.c36 = Constraint(expr= - m.x121 + m.x122 - m.x161 + m.x162 - m.x181 + m.x182 - m.x241 + m.x242 == 0)

m.c37 = Constraint(expr=   m.x419 - m.x420 + m.x439 - m.x440 + m.x459 - m.x460 == 0)

m.c38 = Constraint(expr=   m.x359 - m.x360 + m.x379 - m.x380 + m.x399 - m.x400 - m.x459 + m.x460 == 0)

m.c39 = Constraint(expr=   m.x299 - m.x300 + m.x319 - m.x320 + m.x339 - m.x340 - m.x439 + m.x440 == -2000)

m.c40 = Constraint(expr=   m.x239 - m.x240 + m.x259 - m.x260 + m.x279 - m.x280 - m.x399 + m.x400 == 0)

m.c41 = Constraint(expr=   m.x179 - m.x180 + m.x199 - m.x200 + m.x219 - m.x220 - m.x339 + m.x340 == 2000)

m.c42 = Constraint(expr=   m.x159 - m.x160 - m.x219 + m.x220 - m.x279 + m.x280 == 0)

m.c43 = Constraint(expr=   m.x139 - m.x140 - m.x319 + m.x320 - m.x379 + m.x380 - m.x419 + m.x420 == 0)

m.c44 = Constraint(expr=   m.x119 - m.x120 - m.x139 + m.x140 - m.x199 + m.x200 - m.x259 + m.x260 - m.x299 + m.x300
                         - m.x359 + m.x360 == 0)

m.c45 = Constraint(expr= - m.x119 + m.x120 - m.x159 + m.x160 - m.x179 + m.x180 - m.x239 + m.x240 == 0)

m.c46 = Constraint(expr=   m.x417 - m.x418 + m.x437 - m.x438 + m.x457 - m.x458 == 0)

m.c47 = Constraint(expr=   m.x357 - m.x358 + m.x377 - m.x378 + m.x397 - m.x398 - m.x457 + m.x458 == 0)

m.c48 = Constraint(expr=   m.x297 - m.x298 + m.x317 - m.x318 + m.x337 - m.x338 - m.x437 + m.x438 == 0)

m.c49 = Constraint(expr=   m.x237 - m.x238 + m.x257 - m.x258 + m.x277 - m.x278 - m.x397 + m.x398 == -1000)

m.c50 = Constraint(expr=   m.x177 - m.x178 + m.x197 - m.x198 + m.x217 - m.x218 - m.x337 + m.x338 == 1000)

m.c51 = Constraint(expr=   m.x157 - m.x158 - m.x217 + m.x218 - m.x277 + m.x278 == 0)

m.c52 = Constraint(expr=   m.x137 - m.x138 - m.x317 + m.x318 - m.x377 + m.x378 - m.x417 + m.x418 == 0)

m.c53 = Constraint(expr=   m.x117 - m.x118 - m.x137 + m.x138 - m.x197 + m.x198 - m.x257 + m.x258 - m.x297 + m.x298
                         - m.x357 + m.x358 == 0)

m.c54 = Constraint(expr= - m.x117 + m.x118 - m.x157 + m.x158 - m.x177 + m.x178 - m.x237 + m.x238 == 0)

m.c55 = Constraint(expr=   m.x415 - m.x416 + m.x435 - m.x436 + m.x455 - m.x456 == 0)

m.c56 = Constraint(expr=   m.x355 - m.x356 + m.x375 - m.x376 + m.x395 - m.x396 - m.x455 + m.x456 == 200)

m.c57 = Constraint(expr=   m.x295 - m.x296 + m.x315 - m.x316 + m.x335 - m.x336 - m.x435 + m.x436 == -200)

m.c58 = Constraint(expr=   m.x235 - m.x236 + m.x255 - m.x256 + m.x275 - m.x276 - m.x395 + m.x396 == 0)

m.c59 = Constraint(expr=   m.x175 - m.x176 + m.x195 - m.x196 + m.x215 - m.x216 - m.x335 + m.x336 == 0)

m.c60 = Constraint(expr=   m.x155 - m.x156 - m.x215 + m.x216 - m.x275 + m.x276 == 0)

m.c61 = Constraint(expr=   m.x135 - m.x136 - m.x315 + m.x316 - m.x375 + m.x376 - m.x415 + m.x416 == 0)

m.c62 = Constraint(expr=   m.x115 - m.x116 - m.x135 + m.x136 - m.x195 + m.x196 - m.x255 + m.x256 - m.x295 + m.x296
                         - m.x355 + m.x356 == 0)

m.c63 = Constraint(expr= - m.x115 + m.x116 - m.x155 + m.x156 - m.x175 + m.x176 - m.x235 + m.x236 == 0)

m.c64 = Constraint(expr=   m.x413 - m.x414 + m.x433 - m.x434 + m.x453 - m.x454 == 0)

m.c65 = Constraint(expr=   m.x353 - m.x354 + m.x373 - m.x374 + m.x393 - m.x394 - m.x453 + m.x454 == 200)

m.c66 = Constraint(expr=   m.x293 - m.x294 + m.x313 - m.x314 + m.x333 - m.x334 - m.x433 + m.x434 == 0)

m.c67 = Constraint(expr=   m.x233 - m.x234 + m.x253 - m.x254 + m.x273 - m.x274 - m.x393 + m.x394 == -200)

m.c68 = Constraint(expr=   m.x173 - m.x174 + m.x193 - m.x194 + m.x213 - m.x214 - m.x333 + m.x334 == 0)

m.c69 = Constraint(expr=   m.x153 - m.x154 - m.x213 + m.x214 - m.x273 + m.x274 == 0)

m.c70 = Constraint(expr=   m.x133 - m.x134 - m.x313 + m.x314 - m.x373 + m.x374 - m.x413 + m.x414 == 0)

m.c71 = Constraint(expr=   m.x113 - m.x114 - m.x133 + m.x134 - m.x193 + m.x194 - m.x253 + m.x254 - m.x293 + m.x294
                         - m.x353 + m.x354 == 0)

m.c72 = Constraint(expr= - m.x113 + m.x114 - m.x153 + m.x154 - m.x173 + m.x174 - m.x233 + m.x234 == 0)

m.c73 = Constraint(expr=   m.x411 - m.x412 + m.x431 - m.x432 + m.x451 - m.x452 == 0)

m.c74 = Constraint(expr=   m.x351 - m.x352 + m.x371 - m.x372 + m.x391 - m.x392 - m.x451 + m.x452 == 100)

m.c75 = Constraint(expr=   m.x291 - m.x292 + m.x311 - m.x312 + m.x331 - m.x332 - m.x431 + m.x432 == 0)

m.c76 = Constraint(expr=   m.x231 - m.x232 + m.x251 - m.x252 + m.x271 - m.x272 - m.x391 + m.x392 == 0)

m.c77 = Constraint(expr=   m.x171 - m.x172 + m.x191 - m.x192 + m.x211 - m.x212 - m.x331 + m.x332 == -100)

m.c78 = Constraint(expr=   m.x151 - m.x152 - m.x211 + m.x212 - m.x271 + m.x272 == 0)

m.c79 = Constraint(expr=   m.x131 - m.x132 - m.x311 + m.x312 - m.x371 + m.x372 - m.x411 + m.x412 == 0)

m.c80 = Constraint(expr=   m.x111 - m.x112 - m.x131 + m.x132 - m.x191 + m.x192 - m.x251 + m.x252 - m.x291 + m.x292
                         - m.x351 + m.x352 == 0)

m.c81 = Constraint(expr= - m.x111 + m.x112 - m.x151 + m.x152 - m.x171 + m.x172 - m.x231 + m.x232 == 0)

m.c82 = Constraint(expr=   m.x409 - m.x410 + m.x429 - m.x430 + m.x449 - m.x450 == 0)

m.c83 = Constraint(expr=   m.x349 - m.x350 + m.x369 - m.x370 + m.x389 - m.x390 - m.x449 + m.x450 == 0)

m.c84 = Constraint(expr=   m.x289 - m.x290 + m.x309 - m.x310 + m.x329 - m.x330 - m.x429 + m.x430 == 100)

m.c85 = Constraint(expr=   m.x229 - m.x230 + m.x249 - m.x250 + m.x269 - m.x270 - m.x389 + m.x390 == -100)

m.c86 = Constraint(expr=   m.x169 - m.x170 + m.x189 - m.x190 + m.x209 - m.x210 - m.x329 + m.x330 == 0)

m.c87 = Constraint(expr=   m.x149 - m.x150 - m.x209 + m.x210 - m.x269 + m.x270 == 0)

m.c88 = Constraint(expr=   m.x129 - m.x130 - m.x309 + m.x310 - m.x369 + m.x370 - m.x409 + m.x410 == 0)

m.c89 = Constraint(expr=   m.x109 - m.x110 - m.x129 + m.x130 - m.x189 + m.x190 - m.x249 + m.x250 - m.x289 + m.x290
                         - m.x349 + m.x350 == 0)

m.c90 = Constraint(expr= - m.x109 + m.x110 - m.x149 + m.x150 - m.x169 + m.x170 - m.x229 + m.x230 == 0)

m.c91 = Constraint(expr= - m.x3 + m.x4 - m.x9 + m.x10 - m.x15 + m.x16 == 0)

m.c92 = Constraint(expr=   m.x3 - m.x4 - m.x21 + m.x22 - m.x27 + m.x28 - m.x33 + m.x34 == 0)

m.c93 = Constraint(expr=   m.x9 - m.x10 - m.x39 + m.x40 - m.x45 + m.x46 - m.x51 + m.x52 == 200)

m.c94 = Constraint(expr=   m.x21 - m.x22 - m.x57 + m.x58 - m.x63 + m.x64 - m.x69 + m.x70 == 0)

m.c95 = Constraint(expr=   m.x39 - m.x40 - m.x75 + m.x76 - m.x81 + m.x82 - m.x87 + m.x88 == -200)

m.c96 = Constraint(expr=   m.x57 - m.x58 + m.x75 - m.x76 - m.x93 + m.x94 == 0)

m.c97 = Constraint(expr=   m.x15 - m.x16 + m.x27 - m.x28 + m.x45 - m.x46 - m.x99 + m.x100 == 0)

m.c98 = Constraint(expr=   m.x33 - m.x34 + m.x51 - m.x52 + m.x63 - m.x64 + m.x81 - m.x82 + m.x99 - m.x100 - m.x105
                         + m.x106 == 0)

m.c99 = Constraint(expr=   m.x69 - m.x70 + m.x87 - m.x88 + m.x93 - m.x94 + m.x105 - m.x106 == 0)

m.c100 = Constraint(expr= - m.x5 + m.x6 - m.x11 + m.x12 - m.x17 + m.x18 == 0)

m.c101 = Constraint(expr=   m.x5 - m.x6 - m.x23 + m.x24 - m.x29 + m.x30 - m.x35 + m.x36 == 0)

m.c102 = Constraint(expr=   m.x11 - m.x12 - m.x41 + m.x42 - m.x47 + m.x48 - m.x53 + m.x54 == 0)

m.c103 = Constraint(expr=   m.x23 - m.x24 - m.x59 + m.x60 - m.x65 + m.x66 - m.x71 + m.x72 == 100)

m.c104 = Constraint(expr=   m.x41 - m.x42 - m.x77 + m.x78 - m.x83 + m.x84 - m.x89 + m.x90 == -100)

m.c105 = Constraint(expr=   m.x59 - m.x60 + m.x77 - m.x78 - m.x95 + m.x96 == 0)

m.c106 = Constraint(expr=   m.x17 - m.x18 + m.x29 - m.x30 + m.x47 - m.x48 - m.x101 + m.x102 == 0)

m.c107 = Constraint(expr=   m.x35 - m.x36 + m.x53 - m.x54 + m.x65 - m.x66 + m.x83 - m.x84 + m.x101 - m.x102 - m.x107
                          + m.x108 == 0)

m.c108 = Constraint(expr=   m.x71 - m.x72 + m.x89 - m.x90 + m.x95 - m.x96 + m.x107 - m.x108 == 0)
