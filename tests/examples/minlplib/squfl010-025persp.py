#  MINLP written by GAMS Convert at 04/21/18 13:54:18
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        526       26        0      500        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        511      501       10        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1761     1011      750        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x34 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x58 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x60 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x61 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x62 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x63 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x64 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x65 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x66 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x67 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x68 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x69 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x70 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x71 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x72 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x73 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x74 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x75 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x76 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x77 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x78 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x79 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x80 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x81 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x82 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x83 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x84 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x85 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x86 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x87 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x88 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x89 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x90 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x91 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x92 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x93 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x95 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x96 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x97 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x98 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x100 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x101 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x102 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x103 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x104 = Var(within=Reals,bounds=(0,None),initialize=0.1)
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
m.b251 = Var(within=Binary,bounds=(0,1),initialize=0.1)
m.b252 = Var(within=Binary,bounds=(0,1),initialize=0.1)
m.b253 = Var(within=Binary,bounds=(0,1),initialize=0.1)
m.b254 = Var(within=Binary,bounds=(0,1),initialize=0.1)
m.b255 = Var(within=Binary,bounds=(0,1),initialize=0.1)
m.b256 = Var(within=Binary,bounds=(0,1),initialize=0.1)
m.b257 = Var(within=Binary,bounds=(0,1),initialize=0.1)
m.b258 = Var(within=Binary,bounds=(0,1),initialize=0.1)
m.b259 = Var(within=Binary,bounds=(0,1),initialize=0.1)
m.b260 = Var(within=Binary,bounds=(0,1),initialize=0.1)
m.x261 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x262 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x263 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x264 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x265 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x266 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x267 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x268 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x269 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x270 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x271 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x272 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x273 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x274 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x275 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x276 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x277 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x278 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x279 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x280 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x281 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x282 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x283 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x284 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x285 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x286 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x287 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x288 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x289 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x290 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x291 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x292 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x293 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x294 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x295 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x296 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x297 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x298 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x299 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x300 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x301 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x302 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x303 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x304 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x305 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x306 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x307 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x308 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x309 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x310 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x311 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x312 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x313 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x314 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x315 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x316 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x317 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x318 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x319 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x320 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x321 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x322 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x323 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x324 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x325 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x326 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x327 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x328 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x329 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x330 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x331 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x332 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x333 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x334 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x335 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x336 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x337 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x338 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x339 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x340 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x341 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x342 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x343 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x344 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x345 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x346 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x347 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x348 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x349 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x350 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x351 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x352 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x353 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x354 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x355 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x356 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x357 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x358 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x359 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x360 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x361 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x362 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x363 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x364 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x365 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x366 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x367 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x368 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x369 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x370 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x371 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x372 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x373 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x374 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x375 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x376 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x377 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x378 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x379 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x380 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x381 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x382 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x383 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x384 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x385 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x386 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x387 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x388 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x389 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x390 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x391 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x392 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x393 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x394 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x395 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x396 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x397 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x398 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x399 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x400 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x401 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x402 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x403 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x404 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x405 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x406 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x407 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x408 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x409 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x410 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x411 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x412 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x413 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x414 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x415 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x416 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x417 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x418 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x419 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x420 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x421 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x422 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x423 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x424 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x425 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x426 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x427 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x428 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x429 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x430 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x431 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x432 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x433 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x434 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x435 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x436 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x437 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x438 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x439 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x440 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x441 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x442 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x443 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x444 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x445 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x446 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x447 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x448 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x449 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x450 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x451 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x452 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x453 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x454 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x455 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x456 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x457 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x458 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x459 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x460 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x461 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x462 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x463 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x464 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x465 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x466 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x467 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x468 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x469 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x470 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x471 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x472 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x473 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x474 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x475 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x476 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x477 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x478 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x479 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x480 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x481 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x482 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x483 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x484 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x485 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x486 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x487 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x488 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x489 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x490 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x491 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x492 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x493 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x494 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x495 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x496 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x497 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x498 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x499 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x500 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x501 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x502 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x503 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x504 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x505 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x506 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x507 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x508 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x509 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x510 = Var(within=Reals,bounds=(0,None),initialize=0.01)

m.obj = Objective(expr=   31*m.b251 + 99*m.b252 + 59*m.b253 + 85*m.b254 + 31*m.b255 + 18*m.b256 + 55*m.b257 + 56*m.b258
                        + 2*m.b259 + 42*m.b260 + 23.5458254446414*m.x261 + 18.979955090698*m.x262
                        + 40.4475389896435*m.x263 + 32.3871907368369*m.x264 + 5.87832983721956*m.x265
                        + 27.7861809155978*m.x266 + 29.0093260544642*m.x267 + 27.8172341004716*m.x268
                        + 23.8990137163284*m.x269 + 31.1572073885704*m.x270 + 13.2824851151917*m.x271
                        + 33.2405661163705*m.x272 + 11.9226979325457*m.x273 + 20.4359563497062*m.x274
                        + 24.448648939004*m.x275 + 18.4191355125177*m.x276 + 39.1206587833304*m.x277
                        + 10.0203431071565*m.x278 + 19.3631588126017*m.x279 + 23.3360726377184*m.x280
                        + 28.9471017656799*m.x281 + 11.4841952994712*m.x282 + 6.08794717116601*m.x283
                        + 23.4037893982626*m.x284 + 23.6180996877181*m.x285 + 30.4354193350913*m.x286
                        + 40.4712603455849*m.x287 + 36.2213094971555*m.x288 + 5.60976290451329*m.x289
                        + 23.1725988276517*m.x290 + 20.1796238073169*m.x291 + 4.57861955410779*m.x292
                        + 30.5653982993017*m.x293 + 50.4967526356669*m.x294 + 8.28478358470783*m.x295
                        + 25.018545195819*m.x296 + 12.6329611025149*m.x297 + 27.6454711698144*m.x298
                        + 33.9905967791569*m.x299 + 6.07228540920208*m.x300 + 37.4354673126797*m.x301
                        + 37.4709444132233*m.x302 + 35.7354026371941*m.x303 + 22.4419684331029*m.x304
                        + 32.5374941409*m.x305 + 15.9337490518623*m.x306 + 39.6539821536571*m.x307
                        + 34.007214287844*m.x308 + 31.9891521836171*m.x309 + 11.3076337580825*m.x310
                        + 48.8107919790236*m.x311 + 16.5702835116504*m.x312 + 17.1831503223043*m.x313
                        + 35.1142641830025*m.x314 + 29.1350141677348*m.x315 + 47.6949431536515*m.x316
                        + 32.149139849139*m.x317 + 52.2374267154665*m.x318 + 29.9609434870647*m.x319
                        + 42.6183607184712*m.x320 + 38.2238650857062*m.x321 + 29.3601737959953*m.x322
                        + 15.0635022726005*m.x323 + 47.0245320338646*m.x324 + 29.0759225713501*m.x325
                        + 13.0424768501865*m.x326 + 14.4753873350758*m.x327 + 22.3704949637257*m.x328
                        + 42.3038766759241*m.x329 + 49.2326533720743*m.x330 + 46.1780910030554*m.x331
                        + 29.881771182396*m.x332 + 30.5553734434501*m.x333 + 3.7922842075966*m.x334
                        + 39.37658717414*m.x335 + 38.4041161777079*m.x336 + 25.9812660558023*m.x337
                        + 20.5750893036448*m.x338 + 18.2591550063973*m.x339 + 21.315708405139*m.x340
                        + 33.6312833302058*m.x341 + 15.2250454251428*m.x342 + 40.6998421656809*m.x343
                        + 38.4406211511874*m.x344 + 26.1744753218587*m.x345 + 28.8520619191213*m.x346
                        + 13.6877901486106*m.x347 + 14.6611183170587*m.x348 + 38.8217787386064*m.x349
                        + 12.3633235324976*m.x350 + 22.2787064512218*m.x351 + 20.7514901250986*m.x352
                        + 25.2034704837712*m.x353 + 30.6376270730567*m.x354 + 39.5843101734575*m.x355
                        + 31.1038558069605*m.x356 + 31.6979288753493*m.x357 + 28.645307801904*m.x358
                        + 14.1025463900177*m.x359 + 24.4462384012991*m.x360 + 23.9588130600444*m.x361
                        + 37.2092218308638*m.x362 + 38.9284967423033*m.x363 + 12.2912287240524*m.x364
                        + 17.3040001983168*m.x365 + 15.1907239390981*m.x366 + 10.214640056875*m.x367
                        + 24.5444413988224*m.x368 + 45.991792998601*m.x369 + 8.80808064222724*m.x370
                        + 18.2698135895014*m.x371 + 18.0129352025772*m.x372 + 24.5906708393765*m.x373
                        + 27.2479130814562*m.x374 + 8.14284930897828*m.x375 + 34.6101764845155*m.x376
                        + 39.6172338889732*m.x377 + 31.2334618018089*m.x378 + 15.8448912894477*m.x379
                        + 25.9622870070524*m.x380 + 12.0380295338836*m.x381 + 34.2734923291195*m.x382
                        + 28.2417522551125*m.x383 + 31.2100255255497*m.x384 + 5.69874151661421*m.x385
                        + 20.1924959476585*m.x386 + 25.1047390556883*m.x387 + 50.8540191789234*m.x388
                        + 40.7654848119428*m.x389 + 13.1660129719096*m.x390 + 29.3477563113135*m.x391
                        + 37.623504079514*m.x392 + 25.0512445521536*m.x393 + 24.194699080593*m.x394
                        + 36.8817798615649*m.x395 + 13.4670522383906*m.x396 + 42.8355399696766*m.x397
                        + 21.9449104264389*m.x398 + 14.6179503747045*m.x399 + 33.2656663596617*m.x400
                        + 25.9752193871067*m.x401 + 49.3747299640844*m.x402 + 15.5177231557714*m.x403
                        + 19.9897426371933*m.x404 + 18.8657675463725*m.x405 + 32.1150351106216*m.x406
                        + 10.6354802846521*m.x407 + 6.03289686797428*m.x408 + 33.2130951842154*m.x409
                        + 28.5459989363559*m.x410 + 27.1814982971647*m.x411 + 17.4732774311302*m.x412
                        + 45.7430205440514*m.x413 + 41.078689482825*m.x414 + 14.0894075046248*m.x415
                        + 34.4518041752158*m.x416 + 37.6827979486941*m.x417 + 31.9402692210917*m.x418
                        + 17.176342113498*m.x419 + 39.5175600805753*m.x420 + 18.6428109082815*m.x421
                        + 41.5887207579041*m.x422 + 16.8382070886681*m.x423 + 22.1667280473665*m.x424
                        + 33.1071436309494*m.x425 + 18.7491083157469*m.x426 + 43.8897007571818*m.x427
                        + 8.18685938107562*m.x428 + 25.3225669621538*m.x429 + 26.1676213722903*m.x430
                        + 36.3794013637756*m.x431 + 3.36357996902708*m.x432 + 3.41423836465036*m.x433
                        + 27.3030303493034*m.x434 + 31.6570416640525*m.x435 + 29.2490776122094*m.x436
                        + 47.155909768506*m.x437 + 43.747688859322*m.x438 + 10.7493671026891*m.x439
                        + 27.3502033243542*m.x440 + 16.7299902035031*m.x441 + 11.8402360490836*m.x442
                        + 28.1306173784301*m.x443 + 56.2444171745252*m.x444 + 2.57815337422008*m.x445
                        + 26.6018920054246*m.x446 + 19.1214185252706*m.x447 + 34.3953781800726*m.x448
                        + 34.0930847416161*m.x449 + 13.8204269927978*m.x450 + 44.358450354143*m.x451
                        + 45.1466792975147*m.x452 + 41.4784118603196*m.x453 + 22.1771123969423*m.x454
                        + 31.6502071872129*m.x455 + 11.7484412314793*m.x456 + 44.4308470618447*m.x457
                        + 38.2511037822993*m.x458 + 39.6390015319532*m.x459 + 10.8473239818109*m.x460
                        + 32.7864705333551*m.x461 + 10.2391421240902*m.x462 + 39.5607896432743*m.x463
                        + 39.8410872942397*m.x464 + 15.9484846229643*m.x465 + 37.9732738105522*m.x466
                        + 36.3288913334737*m.x467 + 37.3308942844016*m.x468 + 14.138807380771*m.x469
                        + 40.5225760141947*m.x470 + 23.0942213546361*m.x471 + 38.8745557957034*m.x472
                        + 11.721117960742*m.x473 + 28.5280949777182*m.x474 + 31.7525052480902*m.x475
                        + 11.4257984420683*m.x476 + 37.4452338564339*m.x477 + 1.12488644365266*m.x478
                        + 29.4353246473701*m.x479 + 32.1453138866363*m.x480 + 39.0350080216973*m.x481
                        + 6.46693171499145*m.x482 + 9.11562848937319*m.x483 + 20.7606750347532*m.x484
                        + 33.4319480801873*m.x485 + 28.1441444643013*m.x486 + 34.4021397840332*m.x487
                        + 33.6749639035632*m.x488 + 10.1168794661545*m.x489 + 17.6213921739784*m.x490
                        + 20.3933915426277*m.x491 + 6.98038357032972*m.x492 + 29.2368220177179*m.x493
                        + 44.3389168003468*m.x494 + 12.4614270571251*m.x495 + 20.9897984897617*m.x496
                        + 13.7049805915567*m.x497 + 21.5807687963342*m.x498 + 30.6259335202425*m.x499
                        + 3.25199498753833*m.x500 + 31.4568158826796*m.x501 + 34.4026496483618*m.x502
                        + 29.5859985016407*m.x503 + 19.9367729999238*m.x504 + 29.9359444021784*m.x505
                        + 17.2658241038544*m.x506 + 33.6872082476686*m.x507 + 28.2574825233421*m.x508
                        + 26.807114591537*m.x509 + 10.9132753163671*m.x510, sense=minimize)

m.c2 = Constraint(expr=   m.x1 - m.b251 <= 0)

m.c3 = Constraint(expr=   m.x2 - m.b251 <= 0)

m.c4 = Constraint(expr=   m.x3 - m.b251 <= 0)

m.c5 = Constraint(expr=   m.x4 - m.b251 <= 0)

m.c6 = Constraint(expr=   m.x5 - m.b251 <= 0)

m.c7 = Constraint(expr=   m.x6 - m.b251 <= 0)

m.c8 = Constraint(expr=   m.x7 - m.b251 <= 0)

m.c9 = Constraint(expr=   m.x8 - m.b251 <= 0)

m.c10 = Constraint(expr=   m.x9 - m.b251 <= 0)

m.c11 = Constraint(expr=   m.x10 - m.b251 <= 0)

m.c12 = Constraint(expr=   m.x11 - m.b251 <= 0)

m.c13 = Constraint(expr=   m.x12 - m.b251 <= 0)

m.c14 = Constraint(expr=   m.x13 - m.b251 <= 0)

m.c15 = Constraint(expr=   m.x14 - m.b251 <= 0)

m.c16 = Constraint(expr=   m.x15 - m.b251 <= 0)

m.c17 = Constraint(expr=   m.x16 - m.b251 <= 0)

m.c18 = Constraint(expr=   m.x17 - m.b251 <= 0)

m.c19 = Constraint(expr=   m.x18 - m.b251 <= 0)

m.c20 = Constraint(expr=   m.x19 - m.b251 <= 0)

m.c21 = Constraint(expr=   m.x20 - m.b251 <= 0)

m.c22 = Constraint(expr=   m.x21 - m.b251 <= 0)

m.c23 = Constraint(expr=   m.x22 - m.b251 <= 0)

m.c24 = Constraint(expr=   m.x23 - m.b251 <= 0)

m.c25 = Constraint(expr=   m.x24 - m.b251 <= 0)

m.c26 = Constraint(expr=   m.x25 - m.b251 <= 0)

m.c27 = Constraint(expr=   m.x26 - m.b252 <= 0)

m.c28 = Constraint(expr=   m.x27 - m.b252 <= 0)

m.c29 = Constraint(expr=   m.x28 - m.b252 <= 0)

m.c30 = Constraint(expr=   m.x29 - m.b252 <= 0)

m.c31 = Constraint(expr=   m.x30 - m.b252 <= 0)

m.c32 = Constraint(expr=   m.x31 - m.b252 <= 0)

m.c33 = Constraint(expr=   m.x32 - m.b252 <= 0)

m.c34 = Constraint(expr=   m.x33 - m.b252 <= 0)

m.c35 = Constraint(expr=   m.x34 - m.b252 <= 0)

m.c36 = Constraint(expr=   m.x35 - m.b252 <= 0)

m.c37 = Constraint(expr=   m.x36 - m.b252 <= 0)

m.c38 = Constraint(expr=   m.x37 - m.b252 <= 0)

m.c39 = Constraint(expr=   m.x38 - m.b252 <= 0)

m.c40 = Constraint(expr=   m.x39 - m.b252 <= 0)

m.c41 = Constraint(expr=   m.x40 - m.b252 <= 0)

m.c42 = Constraint(expr=   m.x41 - m.b252 <= 0)

m.c43 = Constraint(expr=   m.x42 - m.b252 <= 0)

m.c44 = Constraint(expr=   m.x43 - m.b252 <= 0)

m.c45 = Constraint(expr=   m.x44 - m.b252 <= 0)

m.c46 = Constraint(expr=   m.x45 - m.b252 <= 0)

m.c47 = Constraint(expr=   m.x46 - m.b252 <= 0)

m.c48 = Constraint(expr=   m.x47 - m.b252 <= 0)

m.c49 = Constraint(expr=   m.x48 - m.b252 <= 0)

m.c50 = Constraint(expr=   m.x49 - m.b252 <= 0)

m.c51 = Constraint(expr=   m.x50 - m.b252 <= 0)

m.c52 = Constraint(expr=   m.x51 - m.b253 <= 0)

m.c53 = Constraint(expr=   m.x52 - m.b253 <= 0)

m.c54 = Constraint(expr=   m.x53 - m.b253 <= 0)

m.c55 = Constraint(expr=   m.x54 - m.b253 <= 0)

m.c56 = Constraint(expr=   m.x55 - m.b253 <= 0)

m.c57 = Constraint(expr=   m.x56 - m.b253 <= 0)

m.c58 = Constraint(expr=   m.x57 - m.b253 <= 0)

m.c59 = Constraint(expr=   m.x58 - m.b253 <= 0)

m.c60 = Constraint(expr=   m.x59 - m.b253 <= 0)

m.c61 = Constraint(expr=   m.x60 - m.b253 <= 0)

m.c62 = Constraint(expr=   m.x61 - m.b253 <= 0)

m.c63 = Constraint(expr=   m.x62 - m.b253 <= 0)

m.c64 = Constraint(expr=   m.x63 - m.b253 <= 0)

m.c65 = Constraint(expr=   m.x64 - m.b253 <= 0)

m.c66 = Constraint(expr=   m.x65 - m.b253 <= 0)

m.c67 = Constraint(expr=   m.x66 - m.b253 <= 0)

m.c68 = Constraint(expr=   m.x67 - m.b253 <= 0)

m.c69 = Constraint(expr=   m.x68 - m.b253 <= 0)

m.c70 = Constraint(expr=   m.x69 - m.b253 <= 0)

m.c71 = Constraint(expr=   m.x70 - m.b253 <= 0)

m.c72 = Constraint(expr=   m.x71 - m.b253 <= 0)

m.c73 = Constraint(expr=   m.x72 - m.b253 <= 0)

m.c74 = Constraint(expr=   m.x73 - m.b253 <= 0)

m.c75 = Constraint(expr=   m.x74 - m.b253 <= 0)

m.c76 = Constraint(expr=   m.x75 - m.b253 <= 0)

m.c77 = Constraint(expr=   m.x76 - m.b254 <= 0)

m.c78 = Constraint(expr=   m.x77 - m.b254 <= 0)

m.c79 = Constraint(expr=   m.x78 - m.b254 <= 0)

m.c80 = Constraint(expr=   m.x79 - m.b254 <= 0)

m.c81 = Constraint(expr=   m.x80 - m.b254 <= 0)

m.c82 = Constraint(expr=   m.x81 - m.b254 <= 0)

m.c83 = Constraint(expr=   m.x82 - m.b254 <= 0)

m.c84 = Constraint(expr=   m.x83 - m.b254 <= 0)

m.c85 = Constraint(expr=   m.x84 - m.b254 <= 0)

m.c86 = Constraint(expr=   m.x85 - m.b254 <= 0)

m.c87 = Constraint(expr=   m.x86 - m.b254 <= 0)

m.c88 = Constraint(expr=   m.x87 - m.b254 <= 0)

m.c89 = Constraint(expr=   m.x88 - m.b254 <= 0)

m.c90 = Constraint(expr=   m.x89 - m.b254 <= 0)

m.c91 = Constraint(expr=   m.x90 - m.b254 <= 0)

m.c92 = Constraint(expr=   m.x91 - m.b254 <= 0)

m.c93 = Constraint(expr=   m.x92 - m.b254 <= 0)

m.c94 = Constraint(expr=   m.x93 - m.b254 <= 0)

m.c95 = Constraint(expr=   m.x94 - m.b254 <= 0)

m.c96 = Constraint(expr=   m.x95 - m.b254 <= 0)

m.c97 = Constraint(expr=   m.x96 - m.b254 <= 0)

m.c98 = Constraint(expr=   m.x97 - m.b254 <= 0)

m.c99 = Constraint(expr=   m.x98 - m.b254 <= 0)

m.c100 = Constraint(expr=   m.x99 - m.b254 <= 0)

m.c101 = Constraint(expr=   m.x100 - m.b254 <= 0)

m.c102 = Constraint(expr=   m.x101 - m.b255 <= 0)

m.c103 = Constraint(expr=   m.x102 - m.b255 <= 0)

m.c104 = Constraint(expr=   m.x103 - m.b255 <= 0)

m.c105 = Constraint(expr=   m.x104 - m.b255 <= 0)

m.c106 = Constraint(expr=   m.x105 - m.b255 <= 0)

m.c107 = Constraint(expr=   m.x106 - m.b255 <= 0)

m.c108 = Constraint(expr=   m.x107 - m.b255 <= 0)

m.c109 = Constraint(expr=   m.x108 - m.b255 <= 0)

m.c110 = Constraint(expr=   m.x109 - m.b255 <= 0)

m.c111 = Constraint(expr=   m.x110 - m.b255 <= 0)

m.c112 = Constraint(expr=   m.x111 - m.b255 <= 0)

m.c113 = Constraint(expr=   m.x112 - m.b255 <= 0)

m.c114 = Constraint(expr=   m.x113 - m.b255 <= 0)

m.c115 = Constraint(expr=   m.x114 - m.b255 <= 0)

m.c116 = Constraint(expr=   m.x115 - m.b255 <= 0)

m.c117 = Constraint(expr=   m.x116 - m.b255 <= 0)

m.c118 = Constraint(expr=   m.x117 - m.b255 <= 0)

m.c119 = Constraint(expr=   m.x118 - m.b255 <= 0)

m.c120 = Constraint(expr=   m.x119 - m.b255 <= 0)

m.c121 = Constraint(expr=   m.x120 - m.b255 <= 0)

m.c122 = Constraint(expr=   m.x121 - m.b255 <= 0)

m.c123 = Constraint(expr=   m.x122 - m.b255 <= 0)

m.c124 = Constraint(expr=   m.x123 - m.b255 <= 0)

m.c125 = Constraint(expr=   m.x124 - m.b255 <= 0)

m.c126 = Constraint(expr=   m.x125 - m.b255 <= 0)

m.c127 = Constraint(expr=   m.x126 - m.b256 <= 0)

m.c128 = Constraint(expr=   m.x127 - m.b256 <= 0)

m.c129 = Constraint(expr=   m.x128 - m.b256 <= 0)

m.c130 = Constraint(expr=   m.x129 - m.b256 <= 0)

m.c131 = Constraint(expr=   m.x130 - m.b256 <= 0)

m.c132 = Constraint(expr=   m.x131 - m.b256 <= 0)

m.c133 = Constraint(expr=   m.x132 - m.b256 <= 0)

m.c134 = Constraint(expr=   m.x133 - m.b256 <= 0)

m.c135 = Constraint(expr=   m.x134 - m.b256 <= 0)

m.c136 = Constraint(expr=   m.x135 - m.b256 <= 0)

m.c137 = Constraint(expr=   m.x136 - m.b256 <= 0)

m.c138 = Constraint(expr=   m.x137 - m.b256 <= 0)

m.c139 = Constraint(expr=   m.x138 - m.b256 <= 0)

m.c140 = Constraint(expr=   m.x139 - m.b256 <= 0)

m.c141 = Constraint(expr=   m.x140 - m.b256 <= 0)

m.c142 = Constraint(expr=   m.x141 - m.b256 <= 0)

m.c143 = Constraint(expr=   m.x142 - m.b256 <= 0)

m.c144 = Constraint(expr=   m.x143 - m.b256 <= 0)

m.c145 = Constraint(expr=   m.x144 - m.b256 <= 0)

m.c146 = Constraint(expr=   m.x145 - m.b256 <= 0)

m.c147 = Constraint(expr=   m.x146 - m.b256 <= 0)

m.c148 = Constraint(expr=   m.x147 - m.b256 <= 0)

m.c149 = Constraint(expr=   m.x148 - m.b256 <= 0)

m.c150 = Constraint(expr=   m.x149 - m.b256 <= 0)

m.c151 = Constraint(expr=   m.x150 - m.b256 <= 0)

m.c152 = Constraint(expr=   m.x151 - m.b257 <= 0)

m.c153 = Constraint(expr=   m.x152 - m.b257 <= 0)

m.c154 = Constraint(expr=   m.x153 - m.b257 <= 0)

m.c155 = Constraint(expr=   m.x154 - m.b257 <= 0)

m.c156 = Constraint(expr=   m.x155 - m.b257 <= 0)

m.c157 = Constraint(expr=   m.x156 - m.b257 <= 0)

m.c158 = Constraint(expr=   m.x157 - m.b257 <= 0)

m.c159 = Constraint(expr=   m.x158 - m.b257 <= 0)

m.c160 = Constraint(expr=   m.x159 - m.b257 <= 0)

m.c161 = Constraint(expr=   m.x160 - m.b257 <= 0)

m.c162 = Constraint(expr=   m.x161 - m.b257 <= 0)

m.c163 = Constraint(expr=   m.x162 - m.b257 <= 0)

m.c164 = Constraint(expr=   m.x163 - m.b257 <= 0)

m.c165 = Constraint(expr=   m.x164 - m.b257 <= 0)

m.c166 = Constraint(expr=   m.x165 - m.b257 <= 0)

m.c167 = Constraint(expr=   m.x166 - m.b257 <= 0)

m.c168 = Constraint(expr=   m.x167 - m.b257 <= 0)

m.c169 = Constraint(expr=   m.x168 - m.b257 <= 0)

m.c170 = Constraint(expr=   m.x169 - m.b257 <= 0)

m.c171 = Constraint(expr=   m.x170 - m.b257 <= 0)

m.c172 = Constraint(expr=   m.x171 - m.b257 <= 0)

m.c173 = Constraint(expr=   m.x172 - m.b257 <= 0)

m.c174 = Constraint(expr=   m.x173 - m.b257 <= 0)

m.c175 = Constraint(expr=   m.x174 - m.b257 <= 0)

m.c176 = Constraint(expr=   m.x175 - m.b257 <= 0)

m.c177 = Constraint(expr=   m.x176 - m.b258 <= 0)

m.c178 = Constraint(expr=   m.x177 - m.b258 <= 0)

m.c179 = Constraint(expr=   m.x178 - m.b258 <= 0)

m.c180 = Constraint(expr=   m.x179 - m.b258 <= 0)

m.c181 = Constraint(expr=   m.x180 - m.b258 <= 0)

m.c182 = Constraint(expr=   m.x181 - m.b258 <= 0)

m.c183 = Constraint(expr=   m.x182 - m.b258 <= 0)

m.c184 = Constraint(expr=   m.x183 - m.b258 <= 0)

m.c185 = Constraint(expr=   m.x184 - m.b258 <= 0)

m.c186 = Constraint(expr=   m.x185 - m.b258 <= 0)

m.c187 = Constraint(expr=   m.x186 - m.b258 <= 0)

m.c188 = Constraint(expr=   m.x187 - m.b258 <= 0)

m.c189 = Constraint(expr=   m.x188 - m.b258 <= 0)

m.c190 = Constraint(expr=   m.x189 - m.b258 <= 0)

m.c191 = Constraint(expr=   m.x190 - m.b258 <= 0)

m.c192 = Constraint(expr=   m.x191 - m.b258 <= 0)

m.c193 = Constraint(expr=   m.x192 - m.b258 <= 0)

m.c194 = Constraint(expr=   m.x193 - m.b258 <= 0)

m.c195 = Constraint(expr=   m.x194 - m.b258 <= 0)

m.c196 = Constraint(expr=   m.x195 - m.b258 <= 0)

m.c197 = Constraint(expr=   m.x196 - m.b258 <= 0)

m.c198 = Constraint(expr=   m.x197 - m.b258 <= 0)

m.c199 = Constraint(expr=   m.x198 - m.b258 <= 0)

m.c200 = Constraint(expr=   m.x199 - m.b258 <= 0)

m.c201 = Constraint(expr=   m.x200 - m.b258 <= 0)

m.c202 = Constraint(expr=   m.x201 - m.b259 <= 0)

m.c203 = Constraint(expr=   m.x202 - m.b259 <= 0)

m.c204 = Constraint(expr=   m.x203 - m.b259 <= 0)

m.c205 = Constraint(expr=   m.x204 - m.b259 <= 0)

m.c206 = Constraint(expr=   m.x205 - m.b259 <= 0)

m.c207 = Constraint(expr=   m.x206 - m.b259 <= 0)

m.c208 = Constraint(expr=   m.x207 - m.b259 <= 0)

m.c209 = Constraint(expr=   m.x208 - m.b259 <= 0)

m.c210 = Constraint(expr=   m.x209 - m.b259 <= 0)

m.c211 = Constraint(expr=   m.x210 - m.b259 <= 0)

m.c212 = Constraint(expr=   m.x211 - m.b259 <= 0)

m.c213 = Constraint(expr=   m.x212 - m.b259 <= 0)

m.c214 = Constraint(expr=   m.x213 - m.b259 <= 0)

m.c215 = Constraint(expr=   m.x214 - m.b259 <= 0)

m.c216 = Constraint(expr=   m.x215 - m.b259 <= 0)

m.c217 = Constraint(expr=   m.x216 - m.b259 <= 0)

m.c218 = Constraint(expr=   m.x217 - m.b259 <= 0)

m.c219 = Constraint(expr=   m.x218 - m.b259 <= 0)

m.c220 = Constraint(expr=   m.x219 - m.b259 <= 0)

m.c221 = Constraint(expr=   m.x220 - m.b259 <= 0)

m.c222 = Constraint(expr=   m.x221 - m.b259 <= 0)

m.c223 = Constraint(expr=   m.x222 - m.b259 <= 0)

m.c224 = Constraint(expr=   m.x223 - m.b259 <= 0)

m.c225 = Constraint(expr=   m.x224 - m.b259 <= 0)

m.c226 = Constraint(expr=   m.x225 - m.b259 <= 0)

m.c227 = Constraint(expr=   m.x226 - m.b260 <= 0)

m.c228 = Constraint(expr=   m.x227 - m.b260 <= 0)

m.c229 = Constraint(expr=   m.x228 - m.b260 <= 0)

m.c230 = Constraint(expr=   m.x229 - m.b260 <= 0)

m.c231 = Constraint(expr=   m.x230 - m.b260 <= 0)

m.c232 = Constraint(expr=   m.x231 - m.b260 <= 0)

m.c233 = Constraint(expr=   m.x232 - m.b260 <= 0)

m.c234 = Constraint(expr=   m.x233 - m.b260 <= 0)

m.c235 = Constraint(expr=   m.x234 - m.b260 <= 0)

m.c236 = Constraint(expr=   m.x235 - m.b260 <= 0)

m.c237 = Constraint(expr=   m.x236 - m.b260 <= 0)

m.c238 = Constraint(expr=   m.x237 - m.b260 <= 0)

m.c239 = Constraint(expr=   m.x238 - m.b260 <= 0)

m.c240 = Constraint(expr=   m.x239 - m.b260 <= 0)

m.c241 = Constraint(expr=   m.x240 - m.b260 <= 0)

m.c242 = Constraint(expr=   m.x241 - m.b260 <= 0)

m.c243 = Constraint(expr=   m.x242 - m.b260 <= 0)

m.c244 = Constraint(expr=   m.x243 - m.b260 <= 0)

m.c245 = Constraint(expr=   m.x244 - m.b260 <= 0)

m.c246 = Constraint(expr=   m.x245 - m.b260 <= 0)

m.c247 = Constraint(expr=   m.x246 - m.b260 <= 0)

m.c248 = Constraint(expr=   m.x247 - m.b260 <= 0)

m.c249 = Constraint(expr=   m.x248 - m.b260 <= 0)

m.c250 = Constraint(expr=   m.x249 - m.b260 <= 0)

m.c251 = Constraint(expr=   m.x250 - m.b260 <= 0)

m.c252 = Constraint(expr=   m.x1 + m.x26 + m.x51 + m.x76 + m.x101 + m.x126 + m.x151 + m.x176 + m.x201 + m.x226 == 1)

m.c253 = Constraint(expr=   m.x2 + m.x27 + m.x52 + m.x77 + m.x102 + m.x127 + m.x152 + m.x177 + m.x202 + m.x227 == 1)

m.c254 = Constraint(expr=   m.x3 + m.x28 + m.x53 + m.x78 + m.x103 + m.x128 + m.x153 + m.x178 + m.x203 + m.x228 == 1)

m.c255 = Constraint(expr=   m.x4 + m.x29 + m.x54 + m.x79 + m.x104 + m.x129 + m.x154 + m.x179 + m.x204 + m.x229 == 1)

m.c256 = Constraint(expr=   m.x5 + m.x30 + m.x55 + m.x80 + m.x105 + m.x130 + m.x155 + m.x180 + m.x205 + m.x230 == 1)

m.c257 = Constraint(expr=   m.x6 + m.x31 + m.x56 + m.x81 + m.x106 + m.x131 + m.x156 + m.x181 + m.x206 + m.x231 == 1)

m.c258 = Constraint(expr=   m.x7 + m.x32 + m.x57 + m.x82 + m.x107 + m.x132 + m.x157 + m.x182 + m.x207 + m.x232 == 1)

m.c259 = Constraint(expr=   m.x8 + m.x33 + m.x58 + m.x83 + m.x108 + m.x133 + m.x158 + m.x183 + m.x208 + m.x233 == 1)

m.c260 = Constraint(expr=   m.x9 + m.x34 + m.x59 + m.x84 + m.x109 + m.x134 + m.x159 + m.x184 + m.x209 + m.x234 == 1)

m.c261 = Constraint(expr=   m.x10 + m.x35 + m.x60 + m.x85 + m.x110 + m.x135 + m.x160 + m.x185 + m.x210 + m.x235 == 1)

m.c262 = Constraint(expr=   m.x11 + m.x36 + m.x61 + m.x86 + m.x111 + m.x136 + m.x161 + m.x186 + m.x211 + m.x236 == 1)

m.c263 = Constraint(expr=   m.x12 + m.x37 + m.x62 + m.x87 + m.x112 + m.x137 + m.x162 + m.x187 + m.x212 + m.x237 == 1)

m.c264 = Constraint(expr=   m.x13 + m.x38 + m.x63 + m.x88 + m.x113 + m.x138 + m.x163 + m.x188 + m.x213 + m.x238 == 1)

m.c265 = Constraint(expr=   m.x14 + m.x39 + m.x64 + m.x89 + m.x114 + m.x139 + m.x164 + m.x189 + m.x214 + m.x239 == 1)

m.c266 = Constraint(expr=   m.x15 + m.x40 + m.x65 + m.x90 + m.x115 + m.x140 + m.x165 + m.x190 + m.x215 + m.x240 == 1)

m.c267 = Constraint(expr=   m.x16 + m.x41 + m.x66 + m.x91 + m.x116 + m.x141 + m.x166 + m.x191 + m.x216 + m.x241 == 1)

m.c268 = Constraint(expr=   m.x17 + m.x42 + m.x67 + m.x92 + m.x117 + m.x142 + m.x167 + m.x192 + m.x217 + m.x242 == 1)

m.c269 = Constraint(expr=   m.x18 + m.x43 + m.x68 + m.x93 + m.x118 + m.x143 + m.x168 + m.x193 + m.x218 + m.x243 == 1)

m.c270 = Constraint(expr=   m.x19 + m.x44 + m.x69 + m.x94 + m.x119 + m.x144 + m.x169 + m.x194 + m.x219 + m.x244 == 1)

m.c271 = Constraint(expr=   m.x20 + m.x45 + m.x70 + m.x95 + m.x120 + m.x145 + m.x170 + m.x195 + m.x220 + m.x245 == 1)

m.c272 = Constraint(expr=   m.x21 + m.x46 + m.x71 + m.x96 + m.x121 + m.x146 + m.x171 + m.x196 + m.x221 + m.x246 == 1)

m.c273 = Constraint(expr=   m.x22 + m.x47 + m.x72 + m.x97 + m.x122 + m.x147 + m.x172 + m.x197 + m.x222 + m.x247 == 1)

m.c274 = Constraint(expr=   m.x23 + m.x48 + m.x73 + m.x98 + m.x123 + m.x148 + m.x173 + m.x198 + m.x223 + m.x248 == 1)

m.c275 = Constraint(expr=   m.x24 + m.x49 + m.x74 + m.x99 + m.x124 + m.x149 + m.x174 + m.x199 + m.x224 + m.x249 == 1)

m.c276 = Constraint(expr=   m.x25 + m.x50 + m.x75 + m.x100 + m.x125 + m.x150 + m.x175 + m.x200 + m.x225 + m.x250 == 1)

m.c277 = Constraint(expr=m.x1*m.x1 - m.x261*m.b251 <= 0)

m.c278 = Constraint(expr=m.x2*m.x2 - m.x262*m.b251 <= 0)

m.c279 = Constraint(expr=m.x3*m.x3 - m.x263*m.b251 <= 0)

m.c280 = Constraint(expr=m.x4*m.x4 - m.x264*m.b251 <= 0)

m.c281 = Constraint(expr=m.x5*m.x5 - m.x265*m.b251 <= 0)

m.c282 = Constraint(expr=m.x6*m.x6 - m.x266*m.b251 <= 0)

m.c283 = Constraint(expr=m.x7*m.x7 - m.x267*m.b251 <= 0)

m.c284 = Constraint(expr=m.x8*m.x8 - m.x268*m.b251 <= 0)

m.c285 = Constraint(expr=m.x9*m.x9 - m.x269*m.b251 <= 0)

m.c286 = Constraint(expr=m.x10*m.x10 - m.x270*m.b251 <= 0)

m.c287 = Constraint(expr=m.x11*m.x11 - m.x271*m.b251 <= 0)

m.c288 = Constraint(expr=m.x12*m.x12 - m.x272*m.b251 <= 0)

m.c289 = Constraint(expr=m.x13*m.x13 - m.x273*m.b251 <= 0)

m.c290 = Constraint(expr=m.x14*m.x14 - m.x274*m.b251 <= 0)

m.c291 = Constraint(expr=m.x15*m.x15 - m.x275*m.b251 <= 0)

m.c292 = Constraint(expr=m.x16*m.x16 - m.x276*m.b251 <= 0)

m.c293 = Constraint(expr=m.x17*m.x17 - m.x277*m.b251 <= 0)

m.c294 = Constraint(expr=m.x18*m.x18 - m.x278*m.b251 <= 0)

m.c295 = Constraint(expr=m.x19*m.x19 - m.x279*m.b251 <= 0)

m.c296 = Constraint(expr=m.x20*m.x20 - m.x280*m.b251 <= 0)

m.c297 = Constraint(expr=m.x21*m.x21 - m.x281*m.b251 <= 0)

m.c298 = Constraint(expr=m.x22*m.x22 - m.x282*m.b251 <= 0)

m.c299 = Constraint(expr=m.x23*m.x23 - m.x283*m.b251 <= 0)

m.c300 = Constraint(expr=m.x24*m.x24 - m.x284*m.b251 <= 0)

m.c301 = Constraint(expr=m.x25*m.x25 - m.x285*m.b251 <= 0)

m.c302 = Constraint(expr=m.x26*m.x26 - m.x286*m.b252 <= 0)

m.c303 = Constraint(expr=m.x27*m.x27 - m.x287*m.b252 <= 0)

m.c304 = Constraint(expr=m.x28*m.x28 - m.x288*m.b252 <= 0)

m.c305 = Constraint(expr=m.x29*m.x29 - m.x289*m.b252 <= 0)

m.c306 = Constraint(expr=m.x30*m.x30 - m.x290*m.b252 <= 0)

m.c307 = Constraint(expr=m.x31*m.x31 - m.x291*m.b252 <= 0)

m.c308 = Constraint(expr=m.x32*m.x32 - m.x292*m.b252 <= 0)

m.c309 = Constraint(expr=m.x33*m.x33 - m.x293*m.b252 <= 0)

m.c310 = Constraint(expr=m.x34*m.x34 - m.x294*m.b252 <= 0)

m.c311 = Constraint(expr=m.x35*m.x35 - m.x295*m.b252 <= 0)

m.c312 = Constraint(expr=m.x36*m.x36 - m.x296*m.b252 <= 0)

m.c313 = Constraint(expr=m.x37*m.x37 - m.x297*m.b252 <= 0)

m.c314 = Constraint(expr=m.x38*m.x38 - m.x298*m.b252 <= 0)

m.c315 = Constraint(expr=m.x39*m.x39 - m.x299*m.b252 <= 0)

m.c316 = Constraint(expr=m.x40*m.x40 - m.x300*m.b252 <= 0)

m.c317 = Constraint(expr=m.x41*m.x41 - m.x301*m.b252 <= 0)

m.c318 = Constraint(expr=m.x42*m.x42 - m.x302*m.b252 <= 0)

m.c319 = Constraint(expr=m.x43*m.x43 - m.x303*m.b252 <= 0)

m.c320 = Constraint(expr=m.x44*m.x44 - m.x304*m.b252 <= 0)

m.c321 = Constraint(expr=m.x45*m.x45 - m.x305*m.b252 <= 0)

m.c322 = Constraint(expr=m.x46*m.x46 - m.x306*m.b252 <= 0)

m.c323 = Constraint(expr=m.x47*m.x47 - m.x307*m.b252 <= 0)

m.c324 = Constraint(expr=m.x48*m.x48 - m.x308*m.b252 <= 0)

m.c325 = Constraint(expr=m.x49*m.x49 - m.x309*m.b252 <= 0)

m.c326 = Constraint(expr=m.x50*m.x50 - m.x310*m.b252 <= 0)

m.c327 = Constraint(expr=m.x51*m.x51 - m.x311*m.b253 <= 0)

m.c328 = Constraint(expr=m.x52*m.x52 - m.x312*m.b253 <= 0)

m.c329 = Constraint(expr=m.x53*m.x53 - m.x313*m.b253 <= 0)

m.c330 = Constraint(expr=m.x54*m.x54 - m.x314*m.b253 <= 0)

m.c331 = Constraint(expr=m.x55*m.x55 - m.x315*m.b253 <= 0)

m.c332 = Constraint(expr=m.x56*m.x56 - m.x316*m.b253 <= 0)

m.c333 = Constraint(expr=m.x57*m.x57 - m.x317*m.b253 <= 0)

m.c334 = Constraint(expr=m.x58*m.x58 - m.x318*m.b253 <= 0)

m.c335 = Constraint(expr=m.x59*m.x59 - m.x319*m.b253 <= 0)

m.c336 = Constraint(expr=m.x60*m.x60 - m.x320*m.b253 <= 0)

m.c337 = Constraint(expr=m.x61*m.x61 - m.x321*m.b253 <= 0)

m.c338 = Constraint(expr=m.x62*m.x62 - m.x322*m.b253 <= 0)

m.c339 = Constraint(expr=m.x63*m.x63 - m.x323*m.b253 <= 0)

m.c340 = Constraint(expr=m.x64*m.x64 - m.x324*m.b253 <= 0)

m.c341 = Constraint(expr=m.x65*m.x65 - m.x325*m.b253 <= 0)

m.c342 = Constraint(expr=m.x66*m.x66 - m.x326*m.b253 <= 0)

m.c343 = Constraint(expr=m.x67*m.x67 - m.x327*m.b253 <= 0)

m.c344 = Constraint(expr=m.x68*m.x68 - m.x328*m.b253 <= 0)

m.c345 = Constraint(expr=m.x69*m.x69 - m.x329*m.b253 <= 0)

m.c346 = Constraint(expr=m.x70*m.x70 - m.x330*m.b253 <= 0)

m.c347 = Constraint(expr=m.x71*m.x71 - m.x331*m.b253 <= 0)

m.c348 = Constraint(expr=m.x72*m.x72 - m.x332*m.b253 <= 0)

m.c349 = Constraint(expr=m.x73*m.x73 - m.x333*m.b253 <= 0)

m.c350 = Constraint(expr=m.x74*m.x74 - m.x334*m.b253 <= 0)

m.c351 = Constraint(expr=m.x75*m.x75 - m.x335*m.b253 <= 0)

m.c352 = Constraint(expr=m.x76*m.x76 - m.x336*m.b254 <= 0)

m.c353 = Constraint(expr=m.x77*m.x77 - m.x337*m.b254 <= 0)

m.c354 = Constraint(expr=m.x78*m.x78 - m.x338*m.b254 <= 0)

m.c355 = Constraint(expr=m.x79*m.x79 - m.x339*m.b254 <= 0)

m.c356 = Constraint(expr=m.x80*m.x80 - m.x340*m.b254 <= 0)

m.c357 = Constraint(expr=m.x81*m.x81 - m.x341*m.b254 <= 0)

m.c358 = Constraint(expr=m.x82*m.x82 - m.x342*m.b254 <= 0)

m.c359 = Constraint(expr=m.x83*m.x83 - m.x343*m.b254 <= 0)

m.c360 = Constraint(expr=m.x84*m.x84 - m.x344*m.b254 <= 0)

m.c361 = Constraint(expr=m.x85*m.x85 - m.x345*m.b254 <= 0)

m.c362 = Constraint(expr=m.x86*m.x86 - m.x346*m.b254 <= 0)

m.c363 = Constraint(expr=m.x87*m.x87 - m.x347*m.b254 <= 0)

m.c364 = Constraint(expr=m.x88*m.x88 - m.x348*m.b254 <= 0)

m.c365 = Constraint(expr=m.x89*m.x89 - m.x349*m.b254 <= 0)

m.c366 = Constraint(expr=m.x90*m.x90 - m.x350*m.b254 <= 0)

m.c367 = Constraint(expr=m.x91*m.x91 - m.x351*m.b254 <= 0)

m.c368 = Constraint(expr=m.x92*m.x92 - m.x352*m.b254 <= 0)

m.c369 = Constraint(expr=m.x93*m.x93 - m.x353*m.b254 <= 0)

m.c370 = Constraint(expr=m.x94*m.x94 - m.x354*m.b254 <= 0)

m.c371 = Constraint(expr=m.x95*m.x95 - m.x355*m.b254 <= 0)

m.c372 = Constraint(expr=m.x96*m.x96 - m.x356*m.b254 <= 0)

m.c373 = Constraint(expr=m.x97*m.x97 - m.x357*m.b254 <= 0)

m.c374 = Constraint(expr=m.x98*m.x98 - m.x358*m.b254 <= 0)

m.c375 = Constraint(expr=m.x99*m.x99 - m.x359*m.b254 <= 0)

m.c376 = Constraint(expr=m.x100*m.x100 - m.x360*m.b254 <= 0)

m.c377 = Constraint(expr=m.x101*m.x101 - m.x361*m.b255 <= 0)

m.c378 = Constraint(expr=m.x102*m.x102 - m.x362*m.b255 <= 0)

m.c379 = Constraint(expr=m.x103*m.x103 - m.x363*m.b255 <= 0)

m.c380 = Constraint(expr=m.x104*m.x104 - m.x364*m.b255 <= 0)

m.c381 = Constraint(expr=m.x105*m.x105 - m.x365*m.b255 <= 0)

m.c382 = Constraint(expr=m.x106*m.x106 - m.x366*m.b255 <= 0)

m.c383 = Constraint(expr=m.x107*m.x107 - m.x367*m.b255 <= 0)

m.c384 = Constraint(expr=m.x108*m.x108 - m.x368*m.b255 <= 0)

m.c385 = Constraint(expr=m.x109*m.x109 - m.x369*m.b255 <= 0)

m.c386 = Constraint(expr=m.x110*m.x110 - m.x370*m.b255 <= 0)

m.c387 = Constraint(expr=m.x111*m.x111 - m.x371*m.b255 <= 0)

m.c388 = Constraint(expr=m.x112*m.x112 - m.x372*m.b255 <= 0)

m.c389 = Constraint(expr=m.x113*m.x113 - m.x373*m.b255 <= 0)

m.c390 = Constraint(expr=m.x114*m.x114 - m.x374*m.b255 <= 0)

m.c391 = Constraint(expr=m.x115*m.x115 - m.x375*m.b255 <= 0)

m.c392 = Constraint(expr=m.x116*m.x116 - m.x376*m.b255 <= 0)

m.c393 = Constraint(expr=m.x117*m.x117 - m.x377*m.b255 <= 0)

m.c394 = Constraint(expr=m.x118*m.x118 - m.x378*m.b255 <= 0)

m.c395 = Constraint(expr=m.x119*m.x119 - m.x379*m.b255 <= 0)

m.c396 = Constraint(expr=m.x120*m.x120 - m.x380*m.b255 <= 0)

m.c397 = Constraint(expr=m.x121*m.x121 - m.x381*m.b255 <= 0)

m.c398 = Constraint(expr=m.x122*m.x122 - m.x382*m.b255 <= 0)

m.c399 = Constraint(expr=m.x123*m.x123 - m.x383*m.b255 <= 0)

m.c400 = Constraint(expr=m.x124*m.x124 - m.x384*m.b255 <= 0)

m.c401 = Constraint(expr=m.x125*m.x125 - m.x385*m.b255 <= 0)

m.c402 = Constraint(expr=m.x126*m.x126 - m.x386*m.b256 <= 0)

m.c403 = Constraint(expr=m.x127*m.x127 - m.x387*m.b256 <= 0)

m.c404 = Constraint(expr=m.x128*m.x128 - m.x388*m.b256 <= 0)

m.c405 = Constraint(expr=m.x129*m.x129 - m.x389*m.b256 <= 0)

m.c406 = Constraint(expr=m.x130*m.x130 - m.x390*m.b256 <= 0)

m.c407 = Constraint(expr=m.x131*m.x131 - m.x391*m.b256 <= 0)

m.c408 = Constraint(expr=m.x132*m.x132 - m.x392*m.b256 <= 0)

m.c409 = Constraint(expr=m.x133*m.x133 - m.x393*m.b256 <= 0)

m.c410 = Constraint(expr=m.x134*m.x134 - m.x394*m.b256 <= 0)

m.c411 = Constraint(expr=m.x135*m.x135 - m.x395*m.b256 <= 0)

m.c412 = Constraint(expr=m.x136*m.x136 - m.x396*m.b256 <= 0)

m.c413 = Constraint(expr=m.x137*m.x137 - m.x397*m.b256 <= 0)

m.c414 = Constraint(expr=m.x138*m.x138 - m.x398*m.b256 <= 0)

m.c415 = Constraint(expr=m.x139*m.x139 - m.x399*m.b256 <= 0)

m.c416 = Constraint(expr=m.x140*m.x140 - m.x400*m.b256 <= 0)

m.c417 = Constraint(expr=m.x141*m.x141 - m.x401*m.b256 <= 0)

m.c418 = Constraint(expr=m.x142*m.x142 - m.x402*m.b256 <= 0)

m.c419 = Constraint(expr=m.x143*m.x143 - m.x403*m.b256 <= 0)

m.c420 = Constraint(expr=m.x144*m.x144 - m.x404*m.b256 <= 0)

m.c421 = Constraint(expr=m.x145*m.x145 - m.x405*m.b256 <= 0)

m.c422 = Constraint(expr=m.x146*m.x146 - m.x406*m.b256 <= 0)

m.c423 = Constraint(expr=m.x147*m.x147 - m.x407*m.b256 <= 0)

m.c424 = Constraint(expr=m.x148*m.x148 - m.x408*m.b256 <= 0)

m.c425 = Constraint(expr=m.x149*m.x149 - m.x409*m.b256 <= 0)

m.c426 = Constraint(expr=m.x150*m.x150 - m.x410*m.b256 <= 0)

m.c427 = Constraint(expr=m.x151*m.x151 - m.x411*m.b257 <= 0)

m.c428 = Constraint(expr=m.x152*m.x152 - m.x412*m.b257 <= 0)

m.c429 = Constraint(expr=m.x153*m.x153 - m.x413*m.b257 <= 0)

m.c430 = Constraint(expr=m.x154*m.x154 - m.x414*m.b257 <= 0)

m.c431 = Constraint(expr=m.x155*m.x155 - m.x415*m.b257 <= 0)

m.c432 = Constraint(expr=m.x156*m.x156 - m.x416*m.b257 <= 0)

m.c433 = Constraint(expr=m.x157*m.x157 - m.x417*m.b257 <= 0)

m.c434 = Constraint(expr=m.x158*m.x158 - m.x418*m.b257 <= 0)

m.c435 = Constraint(expr=m.x159*m.x159 - m.x419*m.b257 <= 0)

m.c436 = Constraint(expr=m.x160*m.x160 - m.x420*m.b257 <= 0)

m.c437 = Constraint(expr=m.x161*m.x161 - m.x421*m.b257 <= 0)

m.c438 = Constraint(expr=m.x162*m.x162 - m.x422*m.b257 <= 0)

m.c439 = Constraint(expr=m.x163*m.x163 - m.x423*m.b257 <= 0)

m.c440 = Constraint(expr=m.x164*m.x164 - m.x424*m.b257 <= 0)

m.c441 = Constraint(expr=m.x165*m.x165 - m.x425*m.b257 <= 0)

m.c442 = Constraint(expr=m.x166*m.x166 - m.x426*m.b257 <= 0)

m.c443 = Constraint(expr=m.x167*m.x167 - m.x427*m.b257 <= 0)

m.c444 = Constraint(expr=m.x168*m.x168 - m.x428*m.b257 <= 0)

m.c445 = Constraint(expr=m.x169*m.x169 - m.x429*m.b257 <= 0)

m.c446 = Constraint(expr=m.x170*m.x170 - m.x430*m.b257 <= 0)

m.c447 = Constraint(expr=m.x171*m.x171 - m.x431*m.b257 <= 0)

m.c448 = Constraint(expr=m.x172*m.x172 - m.x432*m.b257 <= 0)

m.c449 = Constraint(expr=m.x173*m.x173 - m.x433*m.b257 <= 0)

m.c450 = Constraint(expr=m.x174*m.x174 - m.x434*m.b257 <= 0)

m.c451 = Constraint(expr=m.x175*m.x175 - m.x435*m.b257 <= 0)

m.c452 = Constraint(expr=m.x176*m.x176 - m.x436*m.b258 <= 0)

m.c453 = Constraint(expr=m.x177*m.x177 - m.x437*m.b258 <= 0)

m.c454 = Constraint(expr=m.x178*m.x178 - m.x438*m.b258 <= 0)

m.c455 = Constraint(expr=m.x179*m.x179 - m.x439*m.b258 <= 0)

m.c456 = Constraint(expr=m.x180*m.x180 - m.x440*m.b258 <= 0)

m.c457 = Constraint(expr=m.x181*m.x181 - m.x441*m.b258 <= 0)

m.c458 = Constraint(expr=m.x182*m.x182 - m.x442*m.b258 <= 0)

m.c459 = Constraint(expr=m.x183*m.x183 - m.x443*m.b258 <= 0)

m.c460 = Constraint(expr=m.x184*m.x184 - m.x444*m.b258 <= 0)

m.c461 = Constraint(expr=m.x185*m.x185 - m.x445*m.b258 <= 0)

m.c462 = Constraint(expr=m.x186*m.x186 - m.x446*m.b258 <= 0)

m.c463 = Constraint(expr=m.x187*m.x187 - m.x447*m.b258 <= 0)

m.c464 = Constraint(expr=m.x188*m.x188 - m.x448*m.b258 <= 0)

m.c465 = Constraint(expr=m.x189*m.x189 - m.x449*m.b258 <= 0)

m.c466 = Constraint(expr=m.x190*m.x190 - m.x450*m.b258 <= 0)

m.c467 = Constraint(expr=m.x191*m.x191 - m.x451*m.b258 <= 0)

m.c468 = Constraint(expr=m.x192*m.x192 - m.x452*m.b258 <= 0)

m.c469 = Constraint(expr=m.x193*m.x193 - m.x453*m.b258 <= 0)

m.c470 = Constraint(expr=m.x194*m.x194 - m.x454*m.b258 <= 0)

m.c471 = Constraint(expr=m.x195*m.x195 - m.x455*m.b258 <= 0)

m.c472 = Constraint(expr=m.x196*m.x196 - m.x456*m.b258 <= 0)

m.c473 = Constraint(expr=m.x197*m.x197 - m.x457*m.b258 <= 0)

m.c474 = Constraint(expr=m.x198*m.x198 - m.x458*m.b258 <= 0)

m.c475 = Constraint(expr=m.x199*m.x199 - m.x459*m.b258 <= 0)

m.c476 = Constraint(expr=m.x200*m.x200 - m.x460*m.b258 <= 0)

m.c477 = Constraint(expr=m.x201*m.x201 - m.x461*m.b259 <= 0)

m.c478 = Constraint(expr=m.x202*m.x202 - m.x462*m.b259 <= 0)

m.c479 = Constraint(expr=m.x203*m.x203 - m.x463*m.b259 <= 0)

m.c480 = Constraint(expr=m.x204*m.x204 - m.x464*m.b259 <= 0)

m.c481 = Constraint(expr=m.x205*m.x205 - m.x465*m.b259 <= 0)

m.c482 = Constraint(expr=m.x206*m.x206 - m.x466*m.b259 <= 0)

m.c483 = Constraint(expr=m.x207*m.x207 - m.x467*m.b259 <= 0)

m.c484 = Constraint(expr=m.x208*m.x208 - m.x468*m.b259 <= 0)

m.c485 = Constraint(expr=m.x209*m.x209 - m.x469*m.b259 <= 0)

m.c486 = Constraint(expr=m.x210*m.x210 - m.x470*m.b259 <= 0)

m.c487 = Constraint(expr=m.x211*m.x211 - m.x471*m.b259 <= 0)

m.c488 = Constraint(expr=m.x212*m.x212 - m.x472*m.b259 <= 0)

m.c489 = Constraint(expr=m.x213*m.x213 - m.x473*m.b259 <= 0)

m.c490 = Constraint(expr=m.x214*m.x214 - m.x474*m.b259 <= 0)

m.c491 = Constraint(expr=m.x215*m.x215 - m.x475*m.b259 <= 0)

m.c492 = Constraint(expr=m.x216*m.x216 - m.x476*m.b259 <= 0)

m.c493 = Constraint(expr=m.x217*m.x217 - m.x477*m.b259 <= 0)

m.c494 = Constraint(expr=m.x218*m.x218 - m.x478*m.b259 <= 0)

m.c495 = Constraint(expr=m.x219*m.x219 - m.x479*m.b259 <= 0)

m.c496 = Constraint(expr=m.x220*m.x220 - m.x480*m.b259 <= 0)

m.c497 = Constraint(expr=m.x221*m.x221 - m.x481*m.b259 <= 0)

m.c498 = Constraint(expr=m.x222*m.x222 - m.x482*m.b259 <= 0)

m.c499 = Constraint(expr=m.x223*m.x223 - m.x483*m.b259 <= 0)

m.c500 = Constraint(expr=m.x224*m.x224 - m.x484*m.b259 <= 0)

m.c501 = Constraint(expr=m.x225*m.x225 - m.x485*m.b259 <= 0)

m.c502 = Constraint(expr=m.x226*m.x226 - m.x486*m.b260 <= 0)

m.c503 = Constraint(expr=m.x227*m.x227 - m.x487*m.b260 <= 0)

m.c504 = Constraint(expr=m.x228*m.x228 - m.x488*m.b260 <= 0)

m.c505 = Constraint(expr=m.x229*m.x229 - m.x489*m.b260 <= 0)

m.c506 = Constraint(expr=m.x230*m.x230 - m.x490*m.b260 <= 0)

m.c507 = Constraint(expr=m.x231*m.x231 - m.x491*m.b260 <= 0)

m.c508 = Constraint(expr=m.x232*m.x232 - m.x492*m.b260 <= 0)

m.c509 = Constraint(expr=m.x233*m.x233 - m.x493*m.b260 <= 0)

m.c510 = Constraint(expr=m.x234*m.x234 - m.x494*m.b260 <= 0)

m.c511 = Constraint(expr=m.x235*m.x235 - m.x495*m.b260 <= 0)

m.c512 = Constraint(expr=m.x236*m.x236 - m.x496*m.b260 <= 0)

m.c513 = Constraint(expr=m.x237*m.x237 - m.x497*m.b260 <= 0)

m.c514 = Constraint(expr=m.x238*m.x238 - m.x498*m.b260 <= 0)

m.c515 = Constraint(expr=m.x239*m.x239 - m.x499*m.b260 <= 0)

m.c516 = Constraint(expr=m.x240*m.x240 - m.x500*m.b260 <= 0)

m.c517 = Constraint(expr=m.x241*m.x241 - m.x501*m.b260 <= 0)

m.c518 = Constraint(expr=m.x242*m.x242 - m.x502*m.b260 <= 0)

m.c519 = Constraint(expr=m.x243*m.x243 - m.x503*m.b260 <= 0)

m.c520 = Constraint(expr=m.x244*m.x244 - m.x504*m.b260 <= 0)

m.c521 = Constraint(expr=m.x245*m.x245 - m.x505*m.b260 <= 0)

m.c522 = Constraint(expr=m.x246*m.x246 - m.x506*m.b260 <= 0)

m.c523 = Constraint(expr=m.x247*m.x247 - m.x507*m.b260 <= 0)

m.c524 = Constraint(expr=m.x248*m.x248 - m.x508*m.b260 <= 0)

m.c525 = Constraint(expr=m.x249*m.x249 - m.x509*m.b260 <= 0)

m.c526 = Constraint(expr=m.x250*m.x250 - m.x510*m.b260 <= 0)
