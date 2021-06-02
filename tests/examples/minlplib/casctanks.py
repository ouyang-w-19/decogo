#  MINLP written by GAMS Convert at 04/21/18 13:51:13
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        518      358       80       80        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        501      461       40        0        0        0        0        0
#  FX      7        7        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1606     1092      514        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(7.2,10.8),initialize=9)
m.x2 = Var(within=Reals,bounds=(7.2,10.8),initialize=9)
m.x3 = Var(within=Reals,bounds=(7.2,10.8),initialize=9)
m.x4 = Var(within=Reals,bounds=(7.2,10.8),initialize=9)
m.x5 = Var(within=Reals,bounds=(7.2,10.8),initialize=9)
m.x6 = Var(within=Reals,bounds=(7.2,10.8),initialize=9)
m.x7 = Var(within=Reals,bounds=(7.2,10.8),initialize=9)
m.x8 = Var(within=Reals,bounds=(7.2,10.8),initialize=9)
m.x9 = Var(within=Reals,bounds=(7.2,10.8),initialize=9)
m.x10 = Var(within=Reals,bounds=(7.2,10.8),initialize=9)
m.x11 = Var(within=Reals,bounds=(7.2,10.8),initialize=9)
m.x12 = Var(within=Reals,bounds=(7.2,10.8),initialize=9)
m.x13 = Var(within=Reals,bounds=(7.2,10.8),initialize=9)
m.x14 = Var(within=Reals,bounds=(7.2,10.8),initialize=9)
m.x15 = Var(within=Reals,bounds=(7.2,10.8),initialize=9)
m.x16 = Var(within=Reals,bounds=(7.2,10.8),initialize=9)
m.x17 = Var(within=Reals,bounds=(7.2,10.8),initialize=9)
m.x18 = Var(within=Reals,bounds=(7.2,10.8),initialize=9)
m.x19 = Var(within=Reals,bounds=(7.2,10.8),initialize=9)
m.x20 = Var(within=Reals,bounds=(7.2,10.8),initialize=9)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x92 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x102 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x103 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x104 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x105 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x106 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x107 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x108 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x109 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x110 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x111 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x112 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x113 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x114 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x115 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x116 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x117 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x118 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x119 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x120 = Var(within=Reals,bounds=(0.75,0.75),initialize=0.75)
m.x121 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x122 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x123 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x124 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x125 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x126 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x127 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x128 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x129 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x130 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x131 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x132 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x133 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x134 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x135 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x136 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x137 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x138 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x139 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x140 = Var(within=Reals,bounds=(0.75,0.75),initialize=0.75)
m.x141 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x142 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x143 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x144 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x145 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x146 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x147 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x148 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x149 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x150 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x151 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x152 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x153 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x154 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x155 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x156 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x157 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x158 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x159 = Var(within=Reals,bounds=(0.05,1),initialize=0.05)
m.x160 = Var(within=Reals,bounds=(0.75,0.75),initialize=0.75)
m.x161 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x162 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x163 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x164 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x165 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x166 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x167 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x168 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x169 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x170 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x171 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x172 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x173 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x174 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x175 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x176 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x177 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x178 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x179 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x180 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x181 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x182 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x183 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x184 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x185 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x186 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x187 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x188 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x189 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x190 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x191 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x192 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x193 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x194 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x195 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x196 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x197 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x198 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x199 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x200 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x201 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x202 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x203 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x204 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x205 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x206 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x207 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x208 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x209 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x210 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x211 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x212 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x213 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x214 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x215 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x216 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x217 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x218 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x219 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x220 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x221 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x222 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x223 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x224 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x225 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x226 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x227 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x228 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x229 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x230 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x231 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x232 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x233 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x234 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x235 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x236 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x237 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x238 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x239 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x240 = Var(within=Reals,bounds=(0.25,1.25),initialize=1)
m.x241 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x255 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x258 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x262 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x263 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x264 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x265 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x266 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x267 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x268 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x269 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x270 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x271 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x272 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x273 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x274 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x275 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x276 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x277 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x278 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x279 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x280 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x281 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x282 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x283 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x284 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x285 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x286 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x287 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x289 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x290 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x291 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x292 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x293 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x294 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x295 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x296 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x297 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x298 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x299 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x300 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x301 = Var(within=Reals,bounds=(0.1,0.1),initialize=0.1)
m.x302 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x303 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x304 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x305 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x306 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x307 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x309 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x311 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x312 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x313 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x314 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x315 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x316 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x317 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x318 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x319 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x320 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x321 = Var(within=Reals,bounds=(0.1,0.1),initialize=0.1)
m.x322 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x323 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x324 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x325 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x326 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x327 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x328 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x329 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x330 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x331 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x332 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x333 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x334 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x335 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x336 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x337 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x338 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x339 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x340 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x341 = Var(within=Reals,bounds=(0.1,0.1),initialize=0.1)
m.x342 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x343 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x344 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x345 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x346 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x347 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x348 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x349 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x350 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x351 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x352 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x353 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x354 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x355 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x356 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x357 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x358 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x359 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x360 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x361 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x362 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x363 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x364 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x365 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x366 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x367 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x368 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x369 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x370 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x371 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x372 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x373 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x374 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x375 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x376 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x377 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x378 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x379 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x380 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x381 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x382 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x383 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x384 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x385 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x386 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x387 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x388 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x389 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x390 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x391 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x392 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x393 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x394 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x395 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x396 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x397 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x398 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x399 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x400 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x401 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x402 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x403 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x404 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x405 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x406 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x407 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x408 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x409 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x410 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x411 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x412 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x413 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x414 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x415 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x416 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x417 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x418 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x419 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x420 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x421 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x422 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x423 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x424 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x425 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x426 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x427 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x428 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x429 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x430 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x431 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x432 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x433 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x434 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x435 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x436 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x437 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x438 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x439 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x440 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x441 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x442 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x443 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x444 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x445 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x446 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x447 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x448 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x449 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x450 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x451 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x452 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x453 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x454 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x455 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x456 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x457 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x458 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x459 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x460 = Var(within=Reals,bounds=(0,None),initialize=1)
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

m.obj = Objective(expr=(-0.75 + m.x101)**2*m.x1 + (-0.75 + m.x102)**2*m.x2 + (-0.75 + m.x103)**2*m.x3 + (-0.75 + m.x104)
                       **2*m.x4 + (-0.75 + m.x105)**2*m.x5 + (-0.75 + m.x106)**2*m.x6 + (-0.75 + m.x107)**2*m.x7 + (-
                       0.75 + m.x108)**2*m.x8 + (-0.75 + m.x109)**2*m.x9 + (-0.75 + m.x110)**2*m.x10 + (-0.75 + m.x111)
                       **2*m.x11 + (-0.75 + m.x112)**2*m.x12 + (-0.75 + m.x113)**2*m.x13 + (-0.75 + m.x114)**2*m.x14 + (
                       -0.75 + m.x115)**2*m.x15 + (-0.75 + m.x116)**2*m.x16 + (-0.75 + m.x117)**2*m.x17 + (-0.75 + 
                       m.x118)**2*m.x18 + (-0.75 + m.x119)**2*m.x19 + (-0.75 + m.x120)**2*m.x20 + (-0.75 + m.x121)**2*
                       m.x1 + (-0.75 + m.x122)**2*m.x2 + (-0.75 + m.x123)**2*m.x3 + (-0.75 + m.x124)**2*m.x4 + (-0.75 + 
                       m.x125)**2*m.x5 + (-0.75 + m.x126)**2*m.x6 + (-0.75 + m.x127)**2*m.x7 + (-0.75 + m.x128)**2*m.x8
                        + (-0.75 + m.x129)**2*m.x9 + (-0.75 + m.x130)**2*m.x10 + (-0.75 + m.x131)**2*m.x11 + (-0.75 + 
                       m.x132)**2*m.x12 + (-0.75 + m.x133)**2*m.x13 + (-0.75 + m.x134)**2*m.x14 + (-0.75 + m.x135)**2*
                       m.x15 + (-0.75 + m.x136)**2*m.x16 + (-0.75 + m.x137)**2*m.x17 + (-0.75 + m.x138)**2*m.x18 + (-
                       0.75 + m.x139)**2*m.x19 + (-0.75 + m.x140)**2*m.x20 + (-0.75 + m.x141)**2*m.x1 + (-0.75 + m.x142)
                       **2*m.x2 + (-0.75 + m.x143)**2*m.x3 + (-0.75 + m.x144)**2*m.x4 + (-0.75 + m.x145)**2*m.x5 + (-
                       0.75 + m.x146)**2*m.x6 + (-0.75 + m.x147)**2*m.x7 + (-0.75 + m.x148)**2*m.x8 + (-0.75 + m.x149)**
                       2*m.x9 + (-0.75 + m.x150)**2*m.x10 + (-0.75 + m.x151)**2*m.x11 + (-0.75 + m.x152)**2*m.x12 + (-
                       0.75 + m.x153)**2*m.x13 + (-0.75 + m.x154)**2*m.x14 + (-0.75 + m.x155)**2*m.x15 + (-0.75 + m.x156
                       )**2*m.x16 + (-0.75 + m.x157)**2*m.x17 + (-0.75 + m.x158)**2*m.x18 + (-0.75 + m.x159)**2*m.x19 + 
                       (-0.75 + m.x160)**2*m.x20, sense=minimize)

m.c1 = Constraint(expr=-m.x1*m.x361 + m.x101 - m.x301 == 0)

m.c2 = Constraint(expr=-m.x2*m.x362 + m.x102 - m.x302 == 0)

m.c3 = Constraint(expr=-m.x3*m.x363 + m.x103 - m.x303 == 0)

m.c4 = Constraint(expr=-m.x4*m.x364 + m.x104 - m.x304 == 0)

m.c5 = Constraint(expr=-m.x5*m.x365 + m.x105 - m.x305 == 0)

m.c6 = Constraint(expr=-m.x6*m.x366 + m.x106 - m.x306 == 0)

m.c7 = Constraint(expr=-m.x7*m.x367 + m.x107 - m.x307 == 0)

m.c8 = Constraint(expr=-m.x8*m.x368 + m.x108 - m.x308 == 0)

m.c9 = Constraint(expr=-m.x9*m.x369 + m.x109 - m.x309 == 0)

m.c10 = Constraint(expr=-m.x10*m.x370 + m.x110 - m.x310 == 0)

m.c11 = Constraint(expr=-m.x11*m.x371 + m.x111 - m.x311 == 0)

m.c12 = Constraint(expr=-m.x12*m.x372 + m.x112 - m.x312 == 0)

m.c13 = Constraint(expr=-m.x13*m.x373 + m.x113 - m.x313 == 0)

m.c14 = Constraint(expr=-m.x14*m.x374 + m.x114 - m.x314 == 0)

m.c15 = Constraint(expr=-m.x15*m.x375 + m.x115 - m.x315 == 0)

m.c16 = Constraint(expr=-m.x16*m.x376 + m.x116 - m.x316 == 0)

m.c17 = Constraint(expr=-m.x17*m.x377 + m.x117 - m.x317 == 0)

m.c18 = Constraint(expr=-m.x18*m.x378 + m.x118 - m.x318 == 0)

m.c19 = Constraint(expr=-m.x19*m.x379 + m.x119 - m.x319 == 0)

m.c20 = Constraint(expr=-m.x20*m.x380 + m.x120 - m.x320 == 0)

m.c21 = Constraint(expr=-m.x1*m.x381 + m.x121 - m.x321 == 0)

m.c22 = Constraint(expr=-m.x2*m.x382 + m.x122 - m.x322 == 0)

m.c23 = Constraint(expr=-m.x3*m.x383 + m.x123 - m.x323 == 0)

m.c24 = Constraint(expr=-m.x4*m.x384 + m.x124 - m.x324 == 0)

m.c25 = Constraint(expr=-m.x5*m.x385 + m.x125 - m.x325 == 0)

m.c26 = Constraint(expr=-m.x6*m.x386 + m.x126 - m.x326 == 0)

m.c27 = Constraint(expr=-m.x7*m.x387 + m.x127 - m.x327 == 0)

m.c28 = Constraint(expr=-m.x8*m.x388 + m.x128 - m.x328 == 0)

m.c29 = Constraint(expr=-m.x9*m.x389 + m.x129 - m.x329 == 0)

m.c30 = Constraint(expr=-m.x10*m.x390 + m.x130 - m.x330 == 0)

m.c31 = Constraint(expr=-m.x11*m.x391 + m.x131 - m.x331 == 0)

m.c32 = Constraint(expr=-m.x12*m.x392 + m.x132 - m.x332 == 0)

m.c33 = Constraint(expr=-m.x13*m.x393 + m.x133 - m.x333 == 0)

m.c34 = Constraint(expr=-m.x14*m.x394 + m.x134 - m.x334 == 0)

m.c35 = Constraint(expr=-m.x15*m.x395 + m.x135 - m.x335 == 0)

m.c36 = Constraint(expr=-m.x16*m.x396 + m.x136 - m.x336 == 0)

m.c37 = Constraint(expr=-m.x17*m.x397 + m.x137 - m.x337 == 0)

m.c38 = Constraint(expr=-m.x18*m.x398 + m.x138 - m.x338 == 0)

m.c39 = Constraint(expr=-m.x19*m.x399 + m.x139 - m.x339 == 0)

m.c40 = Constraint(expr=-m.x20*m.x400 + m.x140 - m.x340 == 0)

m.c41 = Constraint(expr=-m.x1*m.x401 + m.x141 - m.x341 == 0)

m.c42 = Constraint(expr=-m.x2*m.x402 + m.x142 - m.x342 == 0)

m.c43 = Constraint(expr=-m.x3*m.x403 + m.x143 - m.x343 == 0)

m.c44 = Constraint(expr=-m.x4*m.x404 + m.x144 - m.x344 == 0)

m.c45 = Constraint(expr=-m.x5*m.x405 + m.x145 - m.x345 == 0)

m.c46 = Constraint(expr=-m.x6*m.x406 + m.x146 - m.x346 == 0)

m.c47 = Constraint(expr=-m.x7*m.x407 + m.x147 - m.x347 == 0)

m.c48 = Constraint(expr=-m.x8*m.x408 + m.x148 - m.x348 == 0)

m.c49 = Constraint(expr=-m.x9*m.x409 + m.x149 - m.x349 == 0)

m.c50 = Constraint(expr=-m.x10*m.x410 + m.x150 - m.x350 == 0)

m.c51 = Constraint(expr=-m.x11*m.x411 + m.x151 - m.x351 == 0)

m.c52 = Constraint(expr=-m.x12*m.x412 + m.x152 - m.x352 == 0)

m.c53 = Constraint(expr=-m.x13*m.x413 + m.x153 - m.x353 == 0)

m.c54 = Constraint(expr=-m.x14*m.x414 + m.x154 - m.x354 == 0)

m.c55 = Constraint(expr=-m.x15*m.x415 + m.x155 - m.x355 == 0)

m.c56 = Constraint(expr=-m.x16*m.x416 + m.x156 - m.x356 == 0)

m.c57 = Constraint(expr=-m.x17*m.x417 + m.x157 - m.x357 == 0)

m.c58 = Constraint(expr=-m.x18*m.x418 + m.x158 - m.x358 == 0)

m.c59 = Constraint(expr=-m.x19*m.x419 + m.x159 - m.x359 == 0)

m.c60 = Constraint(expr=-m.x20*m.x420 + m.x160 - m.x360 == 0)

m.c61 = Constraint(expr=   m.x21 - 0.1*m.x161 == 0)

m.c62 = Constraint(expr=   m.x22 - 0.1*m.x162 == 0)

m.c63 = Constraint(expr=   m.x23 - 0.1*m.x163 == 0)

m.c64 = Constraint(expr=   m.x24 - 0.1*m.x164 == 0)

m.c65 = Constraint(expr=   m.x25 - 0.1*m.x165 == 0)

m.c66 = Constraint(expr=   m.x26 - 0.1*m.x166 == 0)

m.c67 = Constraint(expr=   m.x27 - 0.1*m.x167 == 0)

m.c68 = Constraint(expr=   m.x28 - 0.1*m.x168 == 0)

m.c69 = Constraint(expr=   m.x29 - 0.1*m.x169 == 0)

m.c70 = Constraint(expr=   m.x30 - 0.1*m.x170 == 0)

m.c71 = Constraint(expr=   m.x31 - 0.1*m.x171 == 0)

m.c72 = Constraint(expr=   m.x32 - 0.1*m.x172 == 0)

m.c73 = Constraint(expr=   m.x33 - 0.1*m.x173 == 0)

m.c74 = Constraint(expr=   m.x34 - 0.1*m.x174 == 0)

m.c75 = Constraint(expr=   m.x35 - 0.1*m.x175 == 0)

m.c76 = Constraint(expr=   m.x36 - 0.1*m.x176 == 0)

m.c77 = Constraint(expr=   m.x37 - 0.1*m.x177 == 0)

m.c78 = Constraint(expr=   m.x38 - 0.1*m.x178 == 0)

m.c79 = Constraint(expr=   m.x39 - 0.1*m.x179 == 0)

m.c80 = Constraint(expr=   m.x40 - 0.1*m.x180 == 0)

m.c81 = Constraint(expr=-0.1*sqrt(m.x241)*m.x181 + m.x41 == 0)

m.c82 = Constraint(expr=-0.1*sqrt(m.x242)*m.x182 + m.x42 == 0)

m.c83 = Constraint(expr=-0.1*sqrt(m.x243)*m.x183 + m.x43 == 0)

m.c84 = Constraint(expr=-0.1*sqrt(m.x244)*m.x184 + m.x44 == 0)

m.c85 = Constraint(expr=-0.1*sqrt(m.x245)*m.x185 + m.x45 == 0)

m.c86 = Constraint(expr=-0.1*sqrt(m.x246)*m.x186 + m.x46 == 0)

m.c87 = Constraint(expr=-0.1*sqrt(m.x247)*m.x187 + m.x47 == 0)

m.c88 = Constraint(expr=-0.1*sqrt(m.x248)*m.x188 + m.x48 == 0)

m.c89 = Constraint(expr=-0.1*sqrt(m.x249)*m.x189 + m.x49 == 0)

m.c90 = Constraint(expr=-0.1*sqrt(m.x250)*m.x190 + m.x50 == 0)

m.c91 = Constraint(expr=-0.1*sqrt(m.x251)*m.x191 + m.x51 == 0)

m.c92 = Constraint(expr=-0.1*sqrt(m.x252)*m.x192 + m.x52 == 0)

m.c93 = Constraint(expr=-0.1*sqrt(m.x253)*m.x193 + m.x53 == 0)

m.c94 = Constraint(expr=-0.1*sqrt(m.x254)*m.x194 + m.x54 == 0)

m.c95 = Constraint(expr=-0.1*sqrt(m.x255)*m.x195 + m.x55 == 0)

m.c96 = Constraint(expr=-0.1*sqrt(m.x256)*m.x196 + m.x56 == 0)

m.c97 = Constraint(expr=-0.1*sqrt(m.x257)*m.x197 + m.x57 == 0)

m.c98 = Constraint(expr=-0.1*sqrt(m.x258)*m.x198 + m.x58 == 0)

m.c99 = Constraint(expr=-0.1*sqrt(m.x259)*m.x199 + m.x59 == 0)

m.c100 = Constraint(expr=-0.1*sqrt(m.x260)*m.x200 + m.x60 == 0)

m.c101 = Constraint(expr=-0.1*sqrt(m.x261)*m.x201 + m.x61 == 0)

m.c102 = Constraint(expr=-0.1*sqrt(m.x262)*m.x202 + m.x62 == 0)

m.c103 = Constraint(expr=-0.1*sqrt(m.x263)*m.x203 + m.x63 == 0)

m.c104 = Constraint(expr=-0.1*sqrt(m.x264)*m.x204 + m.x64 == 0)

m.c105 = Constraint(expr=-0.1*sqrt(m.x265)*m.x205 + m.x65 == 0)

m.c106 = Constraint(expr=-0.1*sqrt(m.x266)*m.x206 + m.x66 == 0)

m.c107 = Constraint(expr=-0.1*sqrt(m.x267)*m.x207 + m.x67 == 0)

m.c108 = Constraint(expr=-0.1*sqrt(m.x268)*m.x208 + m.x68 == 0)

m.c109 = Constraint(expr=-0.1*sqrt(m.x269)*m.x209 + m.x69 == 0)

m.c110 = Constraint(expr=-0.1*sqrt(m.x270)*m.x210 + m.x70 == 0)

m.c111 = Constraint(expr=-0.1*sqrt(m.x271)*m.x211 + m.x71 == 0)

m.c112 = Constraint(expr=-0.1*sqrt(m.x272)*m.x212 + m.x72 == 0)

m.c113 = Constraint(expr=-0.1*sqrt(m.x273)*m.x213 + m.x73 == 0)

m.c114 = Constraint(expr=-0.1*sqrt(m.x274)*m.x214 + m.x74 == 0)

m.c115 = Constraint(expr=-0.1*sqrt(m.x275)*m.x215 + m.x75 == 0)

m.c116 = Constraint(expr=-0.1*sqrt(m.x276)*m.x216 + m.x76 == 0)

m.c117 = Constraint(expr=-0.1*sqrt(m.x277)*m.x217 + m.x77 == 0)

m.c118 = Constraint(expr=-0.1*sqrt(m.x278)*m.x218 + m.x78 == 0)

m.c119 = Constraint(expr=-0.1*sqrt(m.x279)*m.x219 + m.x79 == 0)

m.c120 = Constraint(expr=-0.1*sqrt(m.x280)*m.x220 + m.x80 == 0)

m.c121 = Constraint(expr=-0.1*sqrt(m.x281)*m.x221 + m.x81 == 0)

m.c122 = Constraint(expr=-0.1*sqrt(m.x282)*m.x222 + m.x82 == 0)

m.c123 = Constraint(expr=-0.1*sqrt(m.x283)*m.x223 + m.x83 == 0)

m.c124 = Constraint(expr=-0.1*sqrt(m.x284)*m.x224 + m.x84 == 0)

m.c125 = Constraint(expr=-0.1*sqrt(m.x285)*m.x225 + m.x85 == 0)

m.c126 = Constraint(expr=-0.1*sqrt(m.x286)*m.x226 + m.x86 == 0)

m.c127 = Constraint(expr=-0.1*sqrt(m.x287)*m.x227 + m.x87 == 0)

m.c128 = Constraint(expr=-0.1*sqrt(m.x288)*m.x228 + m.x88 == 0)

m.c129 = Constraint(expr=-0.1*sqrt(m.x289)*m.x229 + m.x89 == 0)

m.c130 = Constraint(expr=-0.1*sqrt(m.x290)*m.x230 + m.x90 == 0)

m.c131 = Constraint(expr=-0.1*sqrt(m.x291)*m.x231 + m.x91 == 0)

m.c132 = Constraint(expr=-0.1*sqrt(m.x292)*m.x232 + m.x92 == 0)

m.c133 = Constraint(expr=-0.1*sqrt(m.x293)*m.x233 + m.x93 == 0)

m.c134 = Constraint(expr=-0.1*sqrt(m.x294)*m.x234 + m.x94 == 0)

m.c135 = Constraint(expr=-0.1*sqrt(m.x295)*m.x235 + m.x95 == 0)

m.c136 = Constraint(expr=-0.1*sqrt(m.x296)*m.x236 + m.x96 == 0)

m.c137 = Constraint(expr=-0.1*sqrt(m.x297)*m.x237 + m.x97 == 0)

m.c138 = Constraint(expr=-0.1*sqrt(m.x298)*m.x238 + m.x98 == 0)

m.c139 = Constraint(expr=-0.1*sqrt(m.x299)*m.x239 + m.x99 == 0)

m.c140 = Constraint(expr=-0.1*sqrt(m.x300)*m.x240 + m.x100 == 0)

m.c141 = Constraint(expr= - m.x141 + m.x281 == 0)

m.c142 = Constraint(expr= - m.x142 + m.x282 == 0)

m.c143 = Constraint(expr= - m.x143 + m.x283 == 0)

m.c144 = Constraint(expr= - m.x144 + m.x284 == 0)

m.c145 = Constraint(expr= - m.x145 + m.x285 == 0)

m.c146 = Constraint(expr= - m.x146 + m.x286 == 0)

m.c147 = Constraint(expr= - m.x147 + m.x287 == 0)

m.c148 = Constraint(expr= - m.x148 + m.x288 == 0)

m.c149 = Constraint(expr= - m.x149 + m.x289 == 0)

m.c150 = Constraint(expr= - m.x150 + m.x290 == 0)

m.c151 = Constraint(expr= - m.x151 + m.x291 == 0)

m.c152 = Constraint(expr= - m.x152 + m.x292 == 0)

m.c153 = Constraint(expr= - m.x153 + m.x293 == 0)

m.c154 = Constraint(expr= - m.x154 + m.x294 == 0)

m.c155 = Constraint(expr= - m.x155 + m.x295 == 0)

m.c156 = Constraint(expr= - m.x156 + m.x296 == 0)

m.c157 = Constraint(expr= - m.x157 + m.x297 == 0)

m.c158 = Constraint(expr= - m.x158 + m.x298 == 0)

m.c159 = Constraint(expr= - m.x159 + m.x299 == 0)

m.c160 = Constraint(expr= - m.x160 + m.x300 == 0)

m.c161 = Constraint(expr= - 0.5*m.x21 + 0.5*m.x41 + m.x361 == 0)

m.c162 = Constraint(expr= - 0.5*m.x22 + 0.5*m.x42 + m.x362 == 0)

m.c163 = Constraint(expr= - 0.5*m.x23 + 0.5*m.x43 + m.x363 == 0)

m.c164 = Constraint(expr= - 0.5*m.x24 + 0.5*m.x44 + m.x364 == 0)

m.c165 = Constraint(expr= - 0.5*m.x25 + 0.5*m.x45 + m.x365 == 0)

m.c166 = Constraint(expr= - 0.5*m.x26 + 0.5*m.x46 + m.x366 == 0)

m.c167 = Constraint(expr= - 0.5*m.x27 + 0.5*m.x47 + m.x367 == 0)

m.c168 = Constraint(expr= - 0.5*m.x28 + 0.5*m.x48 + m.x368 == 0)

m.c169 = Constraint(expr= - 0.5*m.x29 + 0.5*m.x49 + m.x369 == 0)

m.c170 = Constraint(expr= - 0.5*m.x30 + 0.5*m.x50 + m.x370 == 0)

m.c171 = Constraint(expr= - 0.5*m.x31 + 0.5*m.x51 + m.x371 == 0)

m.c172 = Constraint(expr= - 0.5*m.x32 + 0.5*m.x52 + m.x372 == 0)

m.c173 = Constraint(expr= - 0.5*m.x33 + 0.5*m.x53 + m.x373 == 0)

m.c174 = Constraint(expr= - 0.5*m.x34 + 0.5*m.x54 + m.x374 == 0)

m.c175 = Constraint(expr= - 0.5*m.x35 + 0.5*m.x55 + m.x375 == 0)

m.c176 = Constraint(expr= - 0.5*m.x36 + 0.5*m.x56 + m.x376 == 0)

m.c177 = Constraint(expr= - 0.5*m.x37 + 0.5*m.x57 + m.x377 == 0)

m.c178 = Constraint(expr= - 0.5*m.x38 + 0.5*m.x58 + m.x378 == 0)

m.c179 = Constraint(expr= - 0.5*m.x39 + 0.5*m.x59 + m.x379 == 0)

m.c180 = Constraint(expr= - 0.5*m.x40 + 0.5*m.x60 + m.x380 == 0)

m.c181 = Constraint(expr= - 0.5*m.x41 + 0.5*m.x61 + m.x381 == 0)

m.c182 = Constraint(expr= - 0.5*m.x42 + 0.5*m.x62 + m.x382 == 0)

m.c183 = Constraint(expr= - 0.5*m.x43 + 0.5*m.x63 + m.x383 == 0)

m.c184 = Constraint(expr= - 0.5*m.x44 + 0.5*m.x64 + m.x384 == 0)

m.c185 = Constraint(expr= - 0.5*m.x45 + 0.5*m.x65 + m.x385 == 0)

m.c186 = Constraint(expr= - 0.5*m.x46 + 0.5*m.x66 + m.x386 == 0)

m.c187 = Constraint(expr= - 0.5*m.x47 + 0.5*m.x67 + m.x387 == 0)

m.c188 = Constraint(expr= - 0.5*m.x48 + 0.5*m.x68 + m.x388 == 0)

m.c189 = Constraint(expr= - 0.5*m.x49 + 0.5*m.x69 + m.x389 == 0)

m.c190 = Constraint(expr= - 0.5*m.x50 + 0.5*m.x70 + m.x390 == 0)

m.c191 = Constraint(expr= - 0.5*m.x51 + 0.5*m.x71 + m.x391 == 0)

m.c192 = Constraint(expr= - 0.5*m.x52 + 0.5*m.x72 + m.x392 == 0)

m.c193 = Constraint(expr= - 0.5*m.x53 + 0.5*m.x73 + m.x393 == 0)

m.c194 = Constraint(expr= - 0.5*m.x54 + 0.5*m.x74 + m.x394 == 0)

m.c195 = Constraint(expr= - 0.5*m.x55 + 0.5*m.x75 + m.x395 == 0)

m.c196 = Constraint(expr= - 0.5*m.x56 + 0.5*m.x76 + m.x396 == 0)

m.c197 = Constraint(expr= - 0.5*m.x57 + 0.5*m.x77 + m.x397 == 0)

m.c198 = Constraint(expr= - 0.5*m.x58 + 0.5*m.x78 + m.x398 == 0)

m.c199 = Constraint(expr= - 0.5*m.x59 + 0.5*m.x79 + m.x399 == 0)

m.c200 = Constraint(expr= - 0.5*m.x60 + 0.5*m.x80 + m.x400 == 0)

m.c201 = Constraint(expr= - 0.5*m.x61 + 0.5*m.x81 + m.x401 == 0)

m.c202 = Constraint(expr= - 0.5*m.x62 + 0.5*m.x82 + m.x402 == 0)

m.c203 = Constraint(expr= - 0.5*m.x63 + 0.5*m.x83 + m.x403 == 0)

m.c204 = Constraint(expr= - 0.5*m.x64 + 0.5*m.x84 + m.x404 == 0)

m.c205 = Constraint(expr= - 0.5*m.x65 + 0.5*m.x85 + m.x405 == 0)

m.c206 = Constraint(expr= - 0.5*m.x66 + 0.5*m.x86 + m.x406 == 0)

m.c207 = Constraint(expr= - 0.5*m.x67 + 0.5*m.x87 + m.x407 == 0)

m.c208 = Constraint(expr= - 0.5*m.x68 + 0.5*m.x88 + m.x408 == 0)

m.c209 = Constraint(expr= - 0.5*m.x69 + 0.5*m.x89 + m.x409 == 0)

m.c210 = Constraint(expr= - 0.5*m.x70 + 0.5*m.x90 + m.x410 == 0)

m.c211 = Constraint(expr= - 0.5*m.x71 + 0.5*m.x91 + m.x411 == 0)

m.c212 = Constraint(expr= - 0.5*m.x72 + 0.5*m.x92 + m.x412 == 0)

m.c213 = Constraint(expr= - 0.5*m.x73 + 0.5*m.x93 + m.x413 == 0)

m.c214 = Constraint(expr= - 0.5*m.x74 + 0.5*m.x94 + m.x414 == 0)

m.c215 = Constraint(expr= - 0.5*m.x75 + 0.5*m.x95 + m.x415 == 0)

m.c216 = Constraint(expr= - 0.5*m.x76 + 0.5*m.x96 + m.x416 == 0)

m.c217 = Constraint(expr= - 0.5*m.x77 + 0.5*m.x97 + m.x417 == 0)

m.c218 = Constraint(expr= - 0.5*m.x78 + 0.5*m.x98 + m.x418 == 0)

m.c219 = Constraint(expr= - 0.5*m.x79 + 0.5*m.x99 + m.x419 == 0)

m.c220 = Constraint(expr= - 0.5*m.x80 + 0.5*m.x100 + m.x420 == 0)

m.c221 = Constraint(expr=-m.x1*m.x361 - m.x301 + m.x302 == 0)

m.c222 = Constraint(expr=-m.x2*m.x362 - m.x302 + m.x303 == 0)

m.c223 = Constraint(expr=-m.x3*m.x363 - m.x303 + m.x304 == 0)

m.c224 = Constraint(expr=-m.x4*m.x364 - m.x304 + m.x305 == 0)

m.c225 = Constraint(expr=-m.x5*m.x365 - m.x305 + m.x306 == 0)

m.c226 = Constraint(expr=-m.x6*m.x366 - m.x306 + m.x307 == 0)

m.c227 = Constraint(expr=-m.x7*m.x367 - m.x307 + m.x308 == 0)

m.c228 = Constraint(expr=-m.x8*m.x368 - m.x308 + m.x309 == 0)

m.c229 = Constraint(expr=-m.x9*m.x369 - m.x309 + m.x310 == 0)

m.c230 = Constraint(expr=-m.x10*m.x370 - m.x310 + m.x311 == 0)

m.c231 = Constraint(expr=-m.x11*m.x371 - m.x311 + m.x312 == 0)

m.c232 = Constraint(expr=-m.x12*m.x372 - m.x312 + m.x313 == 0)

m.c233 = Constraint(expr=-m.x13*m.x373 - m.x313 + m.x314 == 0)

m.c234 = Constraint(expr=-m.x14*m.x374 - m.x314 + m.x315 == 0)

m.c235 = Constraint(expr=-m.x15*m.x375 - m.x315 + m.x316 == 0)

m.c236 = Constraint(expr=-m.x16*m.x376 - m.x316 + m.x317 == 0)

m.c237 = Constraint(expr=-m.x17*m.x377 - m.x317 + m.x318 == 0)

m.c238 = Constraint(expr=-m.x18*m.x378 - m.x318 + m.x319 == 0)

m.c239 = Constraint(expr=-m.x19*m.x379 - m.x319 + m.x320 == 0)

m.c240 = Constraint(expr=-m.x1*m.x381 - m.x321 + m.x322 == 0)

m.c241 = Constraint(expr=-m.x2*m.x382 - m.x322 + m.x323 == 0)

m.c242 = Constraint(expr=-m.x3*m.x383 - m.x323 + m.x324 == 0)

m.c243 = Constraint(expr=-m.x4*m.x384 - m.x324 + m.x325 == 0)

m.c244 = Constraint(expr=-m.x5*m.x385 - m.x325 + m.x326 == 0)

m.c245 = Constraint(expr=-m.x6*m.x386 - m.x326 + m.x327 == 0)

m.c246 = Constraint(expr=-m.x7*m.x387 - m.x327 + m.x328 == 0)

m.c247 = Constraint(expr=-m.x8*m.x388 - m.x328 + m.x329 == 0)

m.c248 = Constraint(expr=-m.x9*m.x389 - m.x329 + m.x330 == 0)

m.c249 = Constraint(expr=-m.x10*m.x390 - m.x330 + m.x331 == 0)

m.c250 = Constraint(expr=-m.x11*m.x391 - m.x331 + m.x332 == 0)

m.c251 = Constraint(expr=-m.x12*m.x392 - m.x332 + m.x333 == 0)

m.c252 = Constraint(expr=-m.x13*m.x393 - m.x333 + m.x334 == 0)

m.c253 = Constraint(expr=-m.x14*m.x394 - m.x334 + m.x335 == 0)

m.c254 = Constraint(expr=-m.x15*m.x395 - m.x335 + m.x336 == 0)

m.c255 = Constraint(expr=-m.x16*m.x396 - m.x336 + m.x337 == 0)

m.c256 = Constraint(expr=-m.x17*m.x397 - m.x337 + m.x338 == 0)

m.c257 = Constraint(expr=-m.x18*m.x398 - m.x338 + m.x339 == 0)

m.c258 = Constraint(expr=-m.x19*m.x399 - m.x339 + m.x340 == 0)

m.c259 = Constraint(expr=-m.x1*m.x401 - m.x341 + m.x342 == 0)

m.c260 = Constraint(expr=-m.x2*m.x402 - m.x342 + m.x343 == 0)

m.c261 = Constraint(expr=-m.x3*m.x403 - m.x343 + m.x344 == 0)

m.c262 = Constraint(expr=-m.x4*m.x404 - m.x344 + m.x345 == 0)

m.c263 = Constraint(expr=-m.x5*m.x405 - m.x345 + m.x346 == 0)

m.c264 = Constraint(expr=-m.x6*m.x406 - m.x346 + m.x347 == 0)

m.c265 = Constraint(expr=-m.x7*m.x407 - m.x347 + m.x348 == 0)

m.c266 = Constraint(expr=-m.x8*m.x408 - m.x348 + m.x349 == 0)

m.c267 = Constraint(expr=-m.x9*m.x409 - m.x349 + m.x350 == 0)

m.c268 = Constraint(expr=-m.x10*m.x410 - m.x350 + m.x351 == 0)

m.c269 = Constraint(expr=-m.x11*m.x411 - m.x351 + m.x352 == 0)

m.c270 = Constraint(expr=-m.x12*m.x412 - m.x352 + m.x353 == 0)

m.c271 = Constraint(expr=-m.x13*m.x413 - m.x353 + m.x354 == 0)

m.c272 = Constraint(expr=-m.x14*m.x414 - m.x354 + m.x355 == 0)

m.c273 = Constraint(expr=-m.x15*m.x415 - m.x355 + m.x356 == 0)

m.c274 = Constraint(expr=-m.x16*m.x416 - m.x356 + m.x357 == 0)

m.c275 = Constraint(expr=-m.x17*m.x417 - m.x357 + m.x358 == 0)

m.c276 = Constraint(expr=-m.x18*m.x418 - m.x358 + m.x359 == 0)

m.c277 = Constraint(expr=-m.x19*m.x419 - m.x359 + m.x360 == 0)

m.c278 = Constraint(expr= - m.x1 - m.x421 + m.x441 == 0)

m.c279 = Constraint(expr= - m.x2 - m.x422 + m.x442 == 0)

m.c280 = Constraint(expr= - m.x3 - m.x423 + m.x443 == 0)

m.c281 = Constraint(expr= - m.x4 - m.x424 + m.x444 == 0)

m.c282 = Constraint(expr= - m.x5 - m.x425 + m.x445 == 0)

m.c283 = Constraint(expr= - m.x6 - m.x426 + m.x446 == 0)

m.c284 = Constraint(expr= - m.x7 - m.x427 + m.x447 == 0)

m.c285 = Constraint(expr= - m.x8 - m.x428 + m.x448 == 0)

m.c286 = Constraint(expr= - m.x9 - m.x429 + m.x449 == 0)

m.c287 = Constraint(expr= - m.x10 - m.x430 + m.x450 == 0)

m.c288 = Constraint(expr= - m.x11 - m.x431 + m.x451 == 0)

m.c289 = Constraint(expr= - m.x12 - m.x432 + m.x452 == 0)

m.c290 = Constraint(expr= - m.x13 - m.x433 + m.x453 == 0)

m.c291 = Constraint(expr= - m.x14 - m.x434 + m.x454 == 0)

m.c292 = Constraint(expr= - m.x15 - m.x435 + m.x455 == 0)

m.c293 = Constraint(expr= - m.x16 - m.x436 + m.x456 == 0)

m.c294 = Constraint(expr= - m.x17 - m.x437 + m.x457 == 0)

m.c295 = Constraint(expr= - m.x18 - m.x438 + m.x458 == 0)

m.c296 = Constraint(expr= - m.x19 - m.x439 + m.x459 == 0)

m.c297 = Constraint(expr= - m.x20 - m.x440 + m.x460 == 0)

m.c298 = Constraint(expr= - m.x1 - m.x421 + m.x422 == 0)

m.c299 = Constraint(expr= - m.x2 - m.x422 + m.x423 == 0)

m.c300 = Constraint(expr= - m.x3 - m.x423 + m.x424 == 0)

m.c301 = Constraint(expr= - m.x4 - m.x424 + m.x425 == 0)

m.c302 = Constraint(expr= - m.x5 - m.x425 + m.x426 == 0)

m.c303 = Constraint(expr= - m.x6 - m.x426 + m.x427 == 0)

m.c304 = Constraint(expr= - m.x7 - m.x427 + m.x428 == 0)

m.c305 = Constraint(expr= - m.x8 - m.x428 + m.x429 == 0)

m.c306 = Constraint(expr= - m.x9 - m.x429 + m.x430 == 0)

m.c307 = Constraint(expr= - m.x10 - m.x430 + m.x431 == 0)

m.c308 = Constraint(expr= - m.x11 - m.x431 + m.x432 == 0)

m.c309 = Constraint(expr= - m.x12 - m.x432 + m.x433 == 0)

m.c310 = Constraint(expr= - m.x13 - m.x433 + m.x434 == 0)

m.c311 = Constraint(expr= - m.x14 - m.x434 + m.x435 == 0)

m.c312 = Constraint(expr= - m.x15 - m.x435 + m.x436 == 0)

m.c313 = Constraint(expr= - m.x16 - m.x436 + m.x437 == 0)

m.c314 = Constraint(expr= - m.x17 - m.x437 + m.x438 == 0)

m.c315 = Constraint(expr= - m.x18 - m.x438 + m.x439 == 0)

m.c316 = Constraint(expr= - m.x19 - m.x439 + m.x440 == 0)

m.c317 = Constraint(expr=(-0.5 + m.x121)*m.b461 - m.x101 + m.x241 == 0)

m.c318 = Constraint(expr=(-0.5 + m.x122)*m.b462 - m.x102 + m.x242 == 0)

m.c319 = Constraint(expr=(-0.5 + m.x123)*m.b463 - m.x103 + m.x243 == 0)

m.c320 = Constraint(expr=(-0.5 + m.x124)*m.b464 - m.x104 + m.x244 == 0)

m.c321 = Constraint(expr=(-0.5 + m.x125)*m.b465 - m.x105 + m.x245 == 0)

m.c322 = Constraint(expr=(-0.5 + m.x126)*m.b466 - m.x106 + m.x246 == 0)

m.c323 = Constraint(expr=(-0.5 + m.x127)*m.b467 - m.x107 + m.x247 == 0)

m.c324 = Constraint(expr=(-0.5 + m.x128)*m.b468 - m.x108 + m.x248 == 0)

m.c325 = Constraint(expr=(-0.5 + m.x129)*m.b469 - m.x109 + m.x249 == 0)

m.c326 = Constraint(expr=(-0.5 + m.x130)*m.b470 - m.x110 + m.x250 == 0)

m.c327 = Constraint(expr=(-0.5 + m.x131)*m.b471 - m.x111 + m.x251 == 0)

m.c328 = Constraint(expr=(-0.5 + m.x132)*m.b472 - m.x112 + m.x252 == 0)

m.c329 = Constraint(expr=(-0.5 + m.x133)*m.b473 - m.x113 + m.x253 == 0)

m.c330 = Constraint(expr=(-0.5 + m.x134)*m.b474 - m.x114 + m.x254 == 0)

m.c331 = Constraint(expr=(-0.5 + m.x135)*m.b475 - m.x115 + m.x255 == 0)

m.c332 = Constraint(expr=(-0.5 + m.x136)*m.b476 - m.x116 + m.x256 == 0)

m.c333 = Constraint(expr=(-0.5 + m.x137)*m.b477 - m.x117 + m.x257 == 0)

m.c334 = Constraint(expr=(-0.5 + m.x138)*m.b478 - m.x118 + m.x258 == 0)

m.c335 = Constraint(expr=(-0.5 + m.x139)*m.b479 - m.x119 + m.x259 == 0)

m.c336 = Constraint(expr=(-0.5 + m.x140)*m.b480 - m.x120 + m.x260 == 0)

m.c337 = Constraint(expr=(-0.5 + m.x141)*m.b481 - m.x121 + m.x261 == 0)

m.c338 = Constraint(expr=(-0.5 + m.x142)*m.b482 - m.x122 + m.x262 == 0)

m.c339 = Constraint(expr=(-0.5 + m.x143)*m.b483 - m.x123 + m.x263 == 0)

m.c340 = Constraint(expr=(-0.5 + m.x144)*m.b484 - m.x124 + m.x264 == 0)

m.c341 = Constraint(expr=(-0.5 + m.x145)*m.b485 - m.x125 + m.x265 == 0)

m.c342 = Constraint(expr=(-0.5 + m.x146)*m.b486 - m.x126 + m.x266 == 0)

m.c343 = Constraint(expr=(-0.5 + m.x147)*m.b487 - m.x127 + m.x267 == 0)

m.c344 = Constraint(expr=(-0.5 + m.x148)*m.b488 - m.x128 + m.x268 == 0)

m.c345 = Constraint(expr=(-0.5 + m.x149)*m.b489 - m.x129 + m.x269 == 0)

m.c346 = Constraint(expr=(-0.5 + m.x150)*m.b490 - m.x130 + m.x270 == 0)

m.c347 = Constraint(expr=(-0.5 + m.x151)*m.b491 - m.x131 + m.x271 == 0)

m.c348 = Constraint(expr=(-0.5 + m.x152)*m.b492 - m.x132 + m.x272 == 0)

m.c349 = Constraint(expr=(-0.5 + m.x153)*m.b493 - m.x133 + m.x273 == 0)

m.c350 = Constraint(expr=(-0.5 + m.x154)*m.b494 - m.x134 + m.x274 == 0)

m.c351 = Constraint(expr=(-0.5 + m.x155)*m.b495 - m.x135 + m.x275 == 0)

m.c352 = Constraint(expr=(-0.5 + m.x156)*m.b496 - m.x136 + m.x276 == 0)

m.c353 = Constraint(expr=(-0.5 + m.x157)*m.b497 - m.x137 + m.x277 == 0)

m.c354 = Constraint(expr=(-0.5 + m.x158)*m.b498 - m.x138 + m.x278 == 0)

m.c355 = Constraint(expr=(-0.5 + m.x159)*m.b499 - m.x139 + m.x279 == 0)

m.c356 = Constraint(expr=(-0.5 + m.x160)*m.b500 - m.x140 + m.x280 == 0)

m.c357 = Constraint(expr=   m.x121 - m.b461 <= 0.5)

m.c358 = Constraint(expr=   m.x122 - m.b462 <= 0.5)

m.c359 = Constraint(expr=   m.x123 - m.b463 <= 0.5)

m.c360 = Constraint(expr=   m.x124 - m.b464 <= 0.5)

m.c361 = Constraint(expr=   m.x125 - m.b465 <= 0.5)

m.c362 = Constraint(expr=   m.x126 - m.b466 <= 0.5)

m.c363 = Constraint(expr=   m.x127 - m.b467 <= 0.5)

m.c364 = Constraint(expr=   m.x128 - m.b468 <= 0.5)

m.c365 = Constraint(expr=   m.x129 - m.b469 <= 0.5)

m.c366 = Constraint(expr=   m.x130 - m.b470 <= 0.5)

m.c367 = Constraint(expr=   m.x131 - m.b471 <= 0.5)

m.c368 = Constraint(expr=   m.x132 - m.b472 <= 0.5)

m.c369 = Constraint(expr=   m.x133 - m.b473 <= 0.5)

m.c370 = Constraint(expr=   m.x134 - m.b474 <= 0.5)

m.c371 = Constraint(expr=   m.x135 - m.b475 <= 0.5)

m.c372 = Constraint(expr=   m.x136 - m.b476 <= 0.5)

m.c373 = Constraint(expr=   m.x137 - m.b477 <= 0.5)

m.c374 = Constraint(expr=   m.x138 - m.b478 <= 0.5)

m.c375 = Constraint(expr=   m.x139 - m.b479 <= 0.5)

m.c376 = Constraint(expr=   m.x140 - m.b480 <= 0.5)

m.c377 = Constraint(expr=   m.x141 - m.b481 <= 0.5)

m.c378 = Constraint(expr=   m.x142 - m.b482 <= 0.5)

m.c379 = Constraint(expr=   m.x143 - m.b483 <= 0.5)

m.c380 = Constraint(expr=   m.x144 - m.b484 <= 0.5)

m.c381 = Constraint(expr=   m.x145 - m.b485 <= 0.5)

m.c382 = Constraint(expr=   m.x146 - m.b486 <= 0.5)

m.c383 = Constraint(expr=   m.x147 - m.b487 <= 0.5)

m.c384 = Constraint(expr=   m.x148 - m.b488 <= 0.5)

m.c385 = Constraint(expr=   m.x149 - m.b489 <= 0.5)

m.c386 = Constraint(expr=   m.x150 - m.b490 <= 0.5)

m.c387 = Constraint(expr=   m.x151 - m.b491 <= 0.5)

m.c388 = Constraint(expr=   m.x152 - m.b492 <= 0.5)

m.c389 = Constraint(expr=   m.x153 - m.b493 <= 0.5)

m.c390 = Constraint(expr=   m.x154 - m.b494 <= 0.5)

m.c391 = Constraint(expr=   m.x155 - m.b495 <= 0.5)

m.c392 = Constraint(expr=   m.x156 - m.b496 <= 0.5)

m.c393 = Constraint(expr=   m.x157 - m.b497 <= 0.5)

m.c394 = Constraint(expr=   m.x158 - m.b498 <= 0.5)

m.c395 = Constraint(expr=   m.x159 - m.b499 <= 0.5)

m.c396 = Constraint(expr=   m.x160 - m.b500 <= 0.5)

m.c397 = Constraint(expr=   m.x121 - m.b461 >= -0.5)

m.c398 = Constraint(expr=   m.x122 - m.b462 >= -0.5)

m.c399 = Constraint(expr=   m.x123 - m.b463 >= -0.5)

m.c400 = Constraint(expr=   m.x124 - m.b464 >= -0.5)

m.c401 = Constraint(expr=   m.x125 - m.b465 >= -0.5)

m.c402 = Constraint(expr=   m.x126 - m.b466 >= -0.5)

m.c403 = Constraint(expr=   m.x127 - m.b467 >= -0.5)

m.c404 = Constraint(expr=   m.x128 - m.b468 >= -0.5)

m.c405 = Constraint(expr=   m.x129 - m.b469 >= -0.5)

m.c406 = Constraint(expr=   m.x130 - m.b470 >= -0.5)

m.c407 = Constraint(expr=   m.x131 - m.b471 >= -0.5)

m.c408 = Constraint(expr=   m.x132 - m.b472 >= -0.5)

m.c409 = Constraint(expr=   m.x133 - m.b473 >= -0.5)

m.c410 = Constraint(expr=   m.x134 - m.b474 >= -0.5)

m.c411 = Constraint(expr=   m.x135 - m.b475 >= -0.5)

m.c412 = Constraint(expr=   m.x136 - m.b476 >= -0.5)

m.c413 = Constraint(expr=   m.x137 - m.b477 >= -0.5)

m.c414 = Constraint(expr=   m.x138 - m.b478 >= -0.5)

m.c415 = Constraint(expr=   m.x139 - m.b479 >= -0.5)

m.c416 = Constraint(expr=   m.x140 - m.b480 >= -0.5)

m.c417 = Constraint(expr=   m.x141 - m.b481 >= -0.5)

m.c418 = Constraint(expr=   m.x142 - m.b482 >= -0.5)

m.c419 = Constraint(expr=   m.x143 - m.b483 >= -0.5)

m.c420 = Constraint(expr=   m.x144 - m.b484 >= -0.5)

m.c421 = Constraint(expr=   m.x145 - m.b485 >= -0.5)

m.c422 = Constraint(expr=   m.x146 - m.b486 >= -0.5)

m.c423 = Constraint(expr=   m.x147 - m.b487 >= -0.5)

m.c424 = Constraint(expr=   m.x148 - m.b488 >= -0.5)

m.c425 = Constraint(expr=   m.x149 - m.b489 >= -0.5)

m.c426 = Constraint(expr=   m.x150 - m.b490 >= -0.5)

m.c427 = Constraint(expr=   m.x151 - m.b491 >= -0.5)

m.c428 = Constraint(expr=   m.x152 - m.b492 >= -0.5)

m.c429 = Constraint(expr=   m.x153 - m.b493 >= -0.5)

m.c430 = Constraint(expr=   m.x154 - m.b494 >= -0.5)

m.c431 = Constraint(expr=   m.x155 - m.b495 >= -0.5)

m.c432 = Constraint(expr=   m.x156 - m.b496 >= -0.5)

m.c433 = Constraint(expr=   m.x157 - m.b497 >= -0.5)

m.c434 = Constraint(expr=   m.x158 - m.b498 >= -0.5)

m.c435 = Constraint(expr=   m.x159 - m.b499 >= -0.5)

m.c436 = Constraint(expr=   m.x160 - m.b500 >= -0.5)

m.c437 = Constraint(expr=   m.x321 - m.b461 <= 0.5)

m.c438 = Constraint(expr=   m.x322 - m.b462 <= 0.5)

m.c439 = Constraint(expr=   m.x323 - m.b463 <= 0.5)

m.c440 = Constraint(expr=   m.x324 - m.b464 <= 0.5)

m.c441 = Constraint(expr=   m.x325 - m.b465 <= 0.5)

m.c442 = Constraint(expr=   m.x326 - m.b466 <= 0.5)

m.c443 = Constraint(expr=   m.x327 - m.b467 <= 0.5)

m.c444 = Constraint(expr=   m.x328 - m.b468 <= 0.5)

m.c445 = Constraint(expr=   m.x329 - m.b469 <= 0.5)

m.c446 = Constraint(expr=   m.x330 - m.b470 <= 0.5)

m.c447 = Constraint(expr=   m.x331 - m.b471 <= 0.5)

m.c448 = Constraint(expr=   m.x332 - m.b472 <= 0.5)

m.c449 = Constraint(expr=   m.x333 - m.b473 <= 0.5)

m.c450 = Constraint(expr=   m.x334 - m.b474 <= 0.5)

m.c451 = Constraint(expr=   m.x335 - m.b475 <= 0.5)

m.c452 = Constraint(expr=   m.x336 - m.b476 <= 0.5)

m.c453 = Constraint(expr=   m.x337 - m.b477 <= 0.5)

m.c454 = Constraint(expr=   m.x338 - m.b478 <= 0.5)

m.c455 = Constraint(expr=   m.x339 - m.b479 <= 0.5)

m.c456 = Constraint(expr=   m.x340 - m.b480 <= 0.5)

m.c457 = Constraint(expr=   m.x341 - m.b481 <= 0.5)

m.c458 = Constraint(expr=   m.x342 - m.b482 <= 0.5)

m.c459 = Constraint(expr=   m.x343 - m.b483 <= 0.5)

m.c460 = Constraint(expr=   m.x344 - m.b484 <= 0.5)

m.c461 = Constraint(expr=   m.x345 - m.b485 <= 0.5)

m.c462 = Constraint(expr=   m.x346 - m.b486 <= 0.5)

m.c463 = Constraint(expr=   m.x347 - m.b487 <= 0.5)

m.c464 = Constraint(expr=   m.x348 - m.b488 <= 0.5)

m.c465 = Constraint(expr=   m.x349 - m.b489 <= 0.5)

m.c466 = Constraint(expr=   m.x350 - m.b490 <= 0.5)

m.c467 = Constraint(expr=   m.x351 - m.b491 <= 0.5)

m.c468 = Constraint(expr=   m.x352 - m.b492 <= 0.5)

m.c469 = Constraint(expr=   m.x353 - m.b493 <= 0.5)

m.c470 = Constraint(expr=   m.x354 - m.b494 <= 0.5)

m.c471 = Constraint(expr=   m.x355 - m.b495 <= 0.5)

m.c472 = Constraint(expr=   m.x356 - m.b496 <= 0.5)

m.c473 = Constraint(expr=   m.x357 - m.b497 <= 0.5)

m.c474 = Constraint(expr=   m.x358 - m.b498 <= 0.5)

m.c475 = Constraint(expr=   m.x359 - m.b499 <= 0.5)

m.c476 = Constraint(expr=   m.x360 - m.b500 <= 0.5)

m.c477 = Constraint(expr=   m.x321 - m.b461 >= -0.5)

m.c478 = Constraint(expr=   m.x322 - m.b462 >= -0.5)

m.c479 = Constraint(expr=   m.x323 - m.b463 >= -0.5)

m.c480 = Constraint(expr=   m.x324 - m.b464 >= -0.5)

m.c481 = Constraint(expr=   m.x325 - m.b465 >= -0.5)

m.c482 = Constraint(expr=   m.x326 - m.b466 >= -0.5)

m.c483 = Constraint(expr=   m.x327 - m.b467 >= -0.5)

m.c484 = Constraint(expr=   m.x328 - m.b468 >= -0.5)

m.c485 = Constraint(expr=   m.x329 - m.b469 >= -0.5)

m.c486 = Constraint(expr=   m.x330 - m.b470 >= -0.5)

m.c487 = Constraint(expr=   m.x331 - m.b471 >= -0.5)

m.c488 = Constraint(expr=   m.x332 - m.b472 >= -0.5)

m.c489 = Constraint(expr=   m.x333 - m.b473 >= -0.5)

m.c490 = Constraint(expr=   m.x334 - m.b474 >= -0.5)

m.c491 = Constraint(expr=   m.x335 - m.b475 >= -0.5)

m.c492 = Constraint(expr=   m.x336 - m.b476 >= -0.5)

m.c493 = Constraint(expr=   m.x337 - m.b477 >= -0.5)

m.c494 = Constraint(expr=   m.x338 - m.b478 >= -0.5)

m.c495 = Constraint(expr=   m.x339 - m.b479 >= -0.5)

m.c496 = Constraint(expr=   m.x340 - m.b480 >= -0.5)

m.c497 = Constraint(expr=   m.x341 - m.b481 >= -0.5)

m.c498 = Constraint(expr=   m.x342 - m.b482 >= -0.5)

m.c499 = Constraint(expr=   m.x343 - m.b483 >= -0.5)

m.c500 = Constraint(expr=   m.x344 - m.b484 >= -0.5)

m.c501 = Constraint(expr=   m.x345 - m.b485 >= -0.5)

m.c502 = Constraint(expr=   m.x346 - m.b486 >= -0.5)

m.c503 = Constraint(expr=   m.x347 - m.b487 >= -0.5)

m.c504 = Constraint(expr=   m.x348 - m.b488 >= -0.5)

m.c505 = Constraint(expr=   m.x349 - m.b489 >= -0.5)

m.c506 = Constraint(expr=   m.x350 - m.b490 >= -0.5)

m.c507 = Constraint(expr=   m.x351 - m.b491 >= -0.5)

m.c508 = Constraint(expr=   m.x352 - m.b492 >= -0.5)

m.c509 = Constraint(expr=   m.x353 - m.b493 >= -0.5)

m.c510 = Constraint(expr=   m.x354 - m.b494 >= -0.5)

m.c511 = Constraint(expr=   m.x355 - m.b495 >= -0.5)

m.c512 = Constraint(expr=   m.x356 - m.b496 >= -0.5)

m.c513 = Constraint(expr=   m.x357 - m.b497 >= -0.5)

m.c514 = Constraint(expr=   m.x358 - m.b498 >= -0.5)

m.c515 = Constraint(expr=   m.x359 - m.b499 >= -0.5)

m.c516 = Constraint(expr=   m.x360 - m.b500 >= -0.5)

m.c518 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13
                          + m.x14 + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20 == 180)
