#  MINLP written by GAMS Convert at 04/21/18 13:52:38
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        438      257       60      121        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#       1141     1081       60        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       4261     4081      180        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x101 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x235 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x301 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x321 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x341 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x421 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x422 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x423 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x424 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x425 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x426 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x427 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x428 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x429 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x430 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x431 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x432 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x433 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x434 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x435 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x436 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x437 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x438 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x439 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x440 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x441 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x442 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x443 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x444 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x445 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x446 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x447 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x448 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x449 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x450 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x451 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x452 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x453 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x454 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x455 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x456 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x457 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x458 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x459 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x460 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x461 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x462 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x463 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x464 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x465 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x466 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x467 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x468 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x469 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x470 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x471 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x472 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x473 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x474 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x475 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x476 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x477 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x478 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x479 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x480 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x481 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x482 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x483 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x484 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x485 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x486 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x487 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x488 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x489 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x490 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x491 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x492 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x493 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x494 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x495 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x496 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x497 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x498 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x499 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x500 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x501 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x502 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x503 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x504 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x505 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x506 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x507 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x508 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x509 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x510 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x511 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x512 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x513 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x514 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x515 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x516 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x517 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x518 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x519 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x520 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x521 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x522 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x523 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x524 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x525 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x526 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x527 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x528 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x529 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x530 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x531 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x532 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x533 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x534 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x535 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x536 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x537 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x538 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x539 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x540 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x541 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x542 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x543 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x544 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x545 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x546 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x547 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x548 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x549 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x550 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x551 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x552 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x553 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x554 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x555 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x556 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x557 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x558 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x559 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x560 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x561 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x562 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x563 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x564 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x565 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x566 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x567 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x568 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x569 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x570 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x571 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x572 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x573 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x574 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x575 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x576 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x577 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x578 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x579 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x580 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x581 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x582 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x583 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x584 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x585 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x586 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x587 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x588 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x589 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x590 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x591 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x592 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x593 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x594 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x595 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x596 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x597 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x598 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x599 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x600 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x601 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x602 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x603 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x604 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x605 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x606 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x607 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x608 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x609 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x610 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x611 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x612 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x613 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x614 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x615 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x616 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x617 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x618 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x619 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x620 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x621 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x622 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x623 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x624 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x625 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x626 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x627 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x628 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x629 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x630 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x631 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x632 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x633 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x634 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x635 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x636 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x637 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x638 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x639 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x640 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x641 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x642 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x643 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x644 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x645 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x646 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x647 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x648 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x649 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x650 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x651 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x652 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x653 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x654 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x655 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x656 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x657 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x658 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x659 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x660 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x661 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x662 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x663 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x664 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x665 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x666 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x667 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x668 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x669 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x670 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x671 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x672 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x673 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x674 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x675 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x676 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x677 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x678 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x679 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x680 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x681 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x682 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x683 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x684 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x685 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x686 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x687 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x688 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x689 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x690 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x691 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x692 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x693 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x694 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x695 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x696 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x697 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x698 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x699 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x700 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x701 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x702 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x703 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x704 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x705 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x706 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x707 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x708 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x709 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x710 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x711 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x712 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x713 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x714 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x715 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x716 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x717 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x718 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x719 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x720 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x721 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x722 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x723 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x724 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x725 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x726 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x727 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x728 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x729 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x730 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x731 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x732 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x733 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x734 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x735 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x736 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x737 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x738 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x739 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x740 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x741 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x742 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x743 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x744 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x745 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x746 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x747 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x748 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x749 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x750 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x751 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x752 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x753 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x754 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x755 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x756 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x757 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x758 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x759 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x760 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x761 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x762 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x763 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x764 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x765 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x766 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x767 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x768 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x769 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x770 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x771 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x772 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x773 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x774 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x775 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x776 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x777 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x778 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x779 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x780 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x781 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x782 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x783 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x784 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x785 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x786 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x787 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x788 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x789 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x790 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x791 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x792 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x793 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x794 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x795 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x796 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x797 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x798 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x799 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x800 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x801 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x802 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x803 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x804 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x805 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x806 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x807 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x808 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x809 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x810 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x811 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x812 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x813 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x814 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x815 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x816 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x817 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x818 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x819 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x820 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x821 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x822 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x823 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x824 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x825 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x826 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x827 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x828 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x829 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x830 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x831 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x832 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x833 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x834 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x835 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x836 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x837 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x838 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x839 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x840 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x841 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x842 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x843 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x844 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x845 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x846 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x847 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x848 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x849 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x850 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x851 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x852 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x853 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x854 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x855 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x856 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x857 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x858 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x859 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x860 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x861 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x862 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x863 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x864 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x865 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x866 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x867 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x868 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x869 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x870 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x871 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x872 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x873 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x874 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x875 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x876 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x877 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x878 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x879 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x880 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x881 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x882 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x883 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x884 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x885 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x886 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x887 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x888 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x889 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x890 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x891 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x892 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x893 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x894 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x895 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x896 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x897 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x898 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x899 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x900 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x901 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x902 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x903 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x904 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x905 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x906 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x907 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x908 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x909 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x910 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x911 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x912 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x913 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x914 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x915 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x916 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x917 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x918 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x919 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x920 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x921 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x922 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x923 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x924 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x925 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x926 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x927 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x928 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x929 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x930 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x931 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x932 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x933 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x934 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x935 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x936 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x937 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x938 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x939 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x940 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x941 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x942 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x943 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x944 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x945 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x946 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x947 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x948 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x949 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x950 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x951 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x952 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x953 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x954 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x955 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x956 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x957 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x958 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x959 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x960 = Var(within=Reals,bounds=(0,None),initialize=0)
m.b961 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b962 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b963 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b964 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b965 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b966 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b967 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b968 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b969 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b970 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b971 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b972 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b973 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b974 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b975 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b976 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b977 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b978 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b979 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b980 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b981 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b982 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b983 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b984 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b985 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b986 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b987 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b988 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b989 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b990 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b991 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b992 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b993 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b994 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b995 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b996 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b997 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b998 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b999 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1000 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1001 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1002 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1003 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1004 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1005 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1006 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1007 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1008 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1009 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1010 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1011 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1012 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1013 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1014 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1015 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1016 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1017 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1018 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1019 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1020 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x1021 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1022 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1023 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1024 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1025 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1026 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1027 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1028 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1029 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1030 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1031 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1032 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1033 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1034 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1035 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1036 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1037 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1038 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1039 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1040 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1041 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1042 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1043 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1044 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1045 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1046 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1047 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1048 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1049 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1050 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1051 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1052 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1053 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1054 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1055 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1056 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1057 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1058 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1059 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1060 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1061 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1062 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1063 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1064 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1065 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1066 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1067 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1068 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1069 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1070 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1071 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1072 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1073 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1074 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1075 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1076 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1077 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1078 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1079 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1080 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1082 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1083 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1084 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1085 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1086 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1087 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1088 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1089 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1090 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1091 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1092 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1093 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1094 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1095 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1096 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1097 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1098 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1099 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1100 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1101 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1102 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1103 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1104 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1105 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1106 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1107 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1108 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1109 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1110 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1111 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1112 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1113 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1114 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1115 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1116 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1117 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1118 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1119 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1120 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1121 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1122 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1123 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1124 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1125 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1126 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1127 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1128 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1129 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1130 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1131 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1132 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1133 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1134 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1135 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1136 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1137 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1138 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1139 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1140 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1141 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   1.152432865*m.b961 + 3.011993167*m.b962 + 2.960375281*m.b963 + 1.736309608*m.b964
                        + 1.152432865*m.b965 + 2.363195782*m.b966 + 2.05937716*m.b967 + 3.985025335*m.b968
                        + 3.789003172*m.b969 + 2.363195782*m.b970 + 3.921012982*m.b971 + 3.156380512*m.b972
                        + 2.415793864*m.b973 + 3.011993167*m.b974 + 2.05937716*m.b975 + 1.163363584*m.b976
                        + 2.330956801*m.b977 + 1.29144937*m.b978 + 3.761674897*m.b979 + 2.960375281*m.b980
                        + 2.330956801*m.b981 + 1.396790695*m.b982 + 3.628673512*m.b983 + 1.993672117*m.b984
                        + 3.921012982*m.b985 + 2.05780087*m.b986 + 2.23064791*m.b987 + 3.156380512*m.b988
                        + 1.396790695*m.b989 + 3.35525266*m.b990 + 1.976382727*m.b991 + 1.29144937*m.b992
                        + 1.840522939*m.b993 + 3.337820236*m.b994 + 3.628673512*m.b995 + 1.155800743*m.b996
                        + 1.736309608*m.b997 + 1.840522939*m.b998 + 1.155800743*m.b999 + 3.496770256*m.b1000
                        + 2.415793864*m.b1001 + 2.05780087*m.b1002 + 2.059284631*m.b1003 + 3.35525266*m.b1004
                        + 2.059284631*m.b1005 + 2.534210494*m.b1006 + 3.985025335*m.b1007 + 1.163363584*m.b1008
                        + 2.23064791*m.b1009 + 3.496770256*m.b1010 + 1.025018077*m.b1011 + 3.789003172*m.b1012
                        + 1.993672117*m.b1013 + 3.337820236*m.b1014 + 2.534210494*m.b1015 + 1.025018077*m.b1016
                        + 1.757500525*m.b1017 + 3.761674897*m.b1018 + 1.976382727*m.b1019 + 1.757500525*m.b1020
                       , sense=minimize)

m.c2 = Constraint(expr= - m.x1 - m.x17 - m.x33 - m.x49 + m.x65 + m.x209 + m.x305 + m.x577 == -222)

m.c3 = Constraint(expr= - m.x2 - m.x18 - m.x34 - m.x50 + m.x66 + m.x210 + m.x306 + m.x578 == 25)

m.c4 = Constraint(expr= - m.x3 - m.x19 - m.x35 - m.x51 + m.x67 + m.x211 + m.x307 + m.x579 == 12)

m.c5 = Constraint(expr= - m.x4 - m.x20 - m.x36 - m.x52 + m.x68 + m.x212 + m.x308 + m.x580 == 21)

m.c6 = Constraint(expr= - m.x5 - m.x21 - m.x37 - m.x53 + m.x69 + m.x213 + m.x309 + m.x581 == 25)

m.c7 = Constraint(expr= - m.x6 - m.x22 - m.x38 - m.x54 + m.x70 + m.x214 + m.x310 + m.x582 == 13)

m.c8 = Constraint(expr= - m.x7 - m.x23 - m.x39 - m.x55 + m.x71 + m.x215 + m.x311 + m.x583 == 17)

m.c9 = Constraint(expr= - m.x8 - m.x24 - m.x40 - m.x56 + m.x72 + m.x216 + m.x312 + m.x584 == 11)

m.c10 = Constraint(expr= - m.x9 - m.x25 - m.x41 - m.x57 + m.x73 + m.x217 + m.x313 + m.x585 == 22)

m.c11 = Constraint(expr= - m.x10 - m.x26 - m.x42 - m.x58 + m.x74 + m.x218 + m.x314 + m.x586 == 15)

m.c12 = Constraint(expr= - m.x11 - m.x27 - m.x43 - m.x59 + m.x75 + m.x219 + m.x315 + m.x587 == 16)

m.c13 = Constraint(expr= - m.x12 - m.x28 - m.x44 - m.x60 + m.x76 + m.x220 + m.x316 + m.x588 == 8)

m.c14 = Constraint(expr= - m.x13 - m.x29 - m.x45 - m.x61 + m.x77 + m.x221 + m.x317 + m.x589 == 13)

m.c15 = Constraint(expr= - m.x14 - m.x30 - m.x46 - m.x62 + m.x78 + m.x222 + m.x318 + m.x590 == 21)

m.c16 = Constraint(expr= - m.x15 - m.x31 - m.x47 - m.x63 + m.x79 + m.x223 + m.x319 + m.x591 == 22)

m.c17 = Constraint(expr= - m.x16 - m.x32 - m.x48 - m.x64 + m.x80 + m.x224 + m.x320 + m.x592 == 16)

m.c18 = Constraint(expr=   m.x1 - m.x65 - m.x81 - m.x97 - m.x113 - m.x129 + m.x145 + m.x225 + m.x737 + m.x817 == 19)

m.c19 = Constraint(expr=   m.x2 - m.x66 - m.x82 - m.x98 - m.x114 - m.x130 + m.x146 + m.x226 + m.x738 + m.x818 == -215)

m.c20 = Constraint(expr=   m.x3 - m.x67 - m.x83 - m.x99 - m.x115 - m.x131 + m.x147 + m.x227 + m.x739 + m.x819 == 15)

m.c21 = Constraint(expr=   m.x4 - m.x68 - m.x84 - m.x100 - m.x116 - m.x132 + m.x148 + m.x228 + m.x740 + m.x820 == 16)

m.c22 = Constraint(expr=   m.x5 - m.x69 - m.x85 - m.x101 - m.x117 - m.x133 + m.x149 + m.x229 + m.x741 + m.x821 == 14)

m.c23 = Constraint(expr=   m.x6 - m.x70 - m.x86 - m.x102 - m.x118 - m.x134 + m.x150 + m.x230 + m.x742 + m.x822 == 17)

m.c24 = Constraint(expr=   m.x7 - m.x71 - m.x87 - m.x103 - m.x119 - m.x135 + m.x151 + m.x231 + m.x743 + m.x823 == 14)

m.c25 = Constraint(expr=   m.x8 - m.x72 - m.x88 - m.x104 - m.x120 - m.x136 + m.x152 + m.x232 + m.x744 + m.x824 == 5)

m.c26 = Constraint(expr=   m.x9 - m.x73 - m.x89 - m.x105 - m.x121 - m.x137 + m.x153 + m.x233 + m.x745 + m.x825 == 10)

m.c27 = Constraint(expr=   m.x10 - m.x74 - m.x90 - m.x106 - m.x122 - m.x138 + m.x154 + m.x234 + m.x746 + m.x826 == 5)

m.c28 = Constraint(expr=   m.x11 - m.x75 - m.x91 - m.x107 - m.x123 - m.x139 + m.x155 + m.x235 + m.x747 + m.x827 == 11)

m.c29 = Constraint(expr=   m.x12 - m.x76 - m.x92 - m.x108 - m.x124 - m.x140 + m.x156 + m.x236 + m.x748 + m.x828 == 13)

m.c30 = Constraint(expr=   m.x13 - m.x77 - m.x93 - m.x109 - m.x125 - m.x141 + m.x157 + m.x237 + m.x749 + m.x829 == 19)

m.c31 = Constraint(expr=   m.x14 - m.x78 - m.x94 - m.x110 - m.x126 - m.x142 + m.x158 + m.x238 + m.x750 + m.x830 == 9)

m.c32 = Constraint(expr=   m.x15 - m.x79 - m.x95 - m.x111 - m.x127 - m.x143 + m.x159 + m.x239 + m.x751 + m.x831 == 8)

m.c33 = Constraint(expr=   m.x16 - m.x80 - m.x96 - m.x112 - m.x128 - m.x144 + m.x160 + m.x240 + m.x752 + m.x832 == 10)

m.c34 = Constraint(expr=   m.x81 - m.x145 - m.x161 - m.x177 - m.x193 + m.x385 + m.x433 + m.x641 == 9)

m.c35 = Constraint(expr=   m.x82 - m.x146 - m.x162 - m.x178 - m.x194 + m.x386 + m.x434 + m.x642 == 8)

m.c36 = Constraint(expr=   m.x83 - m.x147 - m.x163 - m.x179 - m.x195 + m.x387 + m.x435 + m.x643 == -227)

m.c37 = Constraint(expr=   m.x84 - m.x148 - m.x164 - m.x180 - m.x196 + m.x388 + m.x436 + m.x644 == 16)

m.c38 = Constraint(expr=   m.x85 - m.x149 - m.x165 - m.x181 - m.x197 + m.x389 + m.x437 + m.x645 == 23)

m.c39 = Constraint(expr=   m.x86 - m.x150 - m.x166 - m.x182 - m.x198 + m.x390 + m.x438 + m.x646 == 6)

m.c40 = Constraint(expr=   m.x87 - m.x151 - m.x167 - m.x183 - m.x199 + m.x391 + m.x439 + m.x647 == 11)

m.c41 = Constraint(expr=   m.x88 - m.x152 - m.x168 - m.x184 - m.x200 + m.x392 + m.x440 + m.x648 == 11)

m.c42 = Constraint(expr=   m.x89 - m.x153 - m.x169 - m.x185 - m.x201 + m.x393 + m.x441 + m.x649 == 11)

m.c43 = Constraint(expr=   m.x90 - m.x154 - m.x170 - m.x186 - m.x202 + m.x394 + m.x442 + m.x650 == 21)

m.c44 = Constraint(expr=   m.x91 - m.x155 - m.x171 - m.x187 - m.x203 + m.x395 + m.x443 + m.x651 == 11)

m.c45 = Constraint(expr=   m.x92 - m.x156 - m.x172 - m.x188 - m.x204 + m.x396 + m.x444 + m.x652 == 9)

m.c46 = Constraint(expr=   m.x93 - m.x157 - m.x173 - m.x189 - m.x205 + m.x397 + m.x445 + m.x653 == 15)

m.c47 = Constraint(expr=   m.x94 - m.x158 - m.x174 - m.x190 - m.x206 + m.x398 + m.x446 + m.x654 == 13)

m.c48 = Constraint(expr=   m.x95 - m.x159 - m.x175 - m.x191 - m.x207 + m.x399 + m.x447 + m.x655 == 9)

m.c49 = Constraint(expr=   m.x96 - m.x160 - m.x176 - m.x192 - m.x208 + m.x400 + m.x448 + m.x656 == 13)

m.c50 = Constraint(expr=   m.x17 + m.x97 - m.x209 - m.x225 - m.x241 + m.x753 == 19)

m.c51 = Constraint(expr=   m.x18 + m.x98 - m.x210 - m.x226 - m.x242 + m.x754 == 13)

m.c52 = Constraint(expr=   m.x19 + m.x99 - m.x211 - m.x227 - m.x243 + m.x755 == 14)

m.c53 = Constraint(expr=   m.x20 + m.x100 - m.x212 - m.x228 - m.x244 + m.x756 == -256)

m.c54 = Constraint(expr=   m.x21 + m.x101 - m.x213 - m.x229 - m.x245 + m.x757 == 12)

m.c55 = Constraint(expr=   m.x22 + m.x102 - m.x214 - m.x230 - m.x246 + m.x758 == 18)

m.c56 = Constraint(expr=   m.x23 + m.x103 - m.x215 - m.x231 - m.x247 + m.x759 == 12)

m.c57 = Constraint(expr=   m.x24 + m.x104 - m.x216 - m.x232 - m.x248 + m.x760 == 12)

m.c58 = Constraint(expr=   m.x25 + m.x105 - m.x217 - m.x233 - m.x249 + m.x761 == 20)

m.c59 = Constraint(expr=   m.x26 + m.x106 - m.x218 - m.x234 - m.x250 + m.x762 == 9)

m.c60 = Constraint(expr=   m.x27 + m.x107 - m.x219 - m.x235 - m.x251 + m.x763 == 22)

m.c61 = Constraint(expr=   m.x28 + m.x108 - m.x220 - m.x236 - m.x252 + m.x764 == 6)

m.c62 = Constraint(expr=   m.x29 + m.x109 - m.x221 - m.x237 - m.x253 + m.x765 == 24)

m.c63 = Constraint(expr=   m.x30 + m.x110 - m.x222 - m.x238 - m.x254 + m.x766 == 16)

m.c64 = Constraint(expr=   m.x31 + m.x111 - m.x223 - m.x239 - m.x255 + m.x767 == 20)

m.c65 = Constraint(expr=   m.x32 + m.x112 - m.x224 - m.x240 - m.x256 + m.x768 == 18)

m.c66 = Constraint(expr= - m.x257 - m.x273 - m.x289 + m.x321 + m.x497 + m.x913 == 18)

m.c67 = Constraint(expr= - m.x258 - m.x274 - m.x290 + m.x322 + m.x498 + m.x914 == 5)

m.c68 = Constraint(expr= - m.x259 - m.x275 - m.x291 + m.x323 + m.x499 + m.x915 == 17)

m.c69 = Constraint(expr= - m.x260 - m.x276 - m.x292 + m.x324 + m.x500 + m.x916 == 24)

m.c70 = Constraint(expr= - m.x261 - m.x277 - m.x293 + m.x325 + m.x501 + m.x917 == -259)

m.c71 = Constraint(expr= - m.x262 - m.x278 - m.x294 + m.x326 + m.x502 + m.x918 == 21)

m.c72 = Constraint(expr= - m.x263 - m.x279 - m.x295 + m.x327 + m.x503 + m.x919 == 7)

m.c73 = Constraint(expr= - m.x264 - m.x280 - m.x296 + m.x328 + m.x504 + m.x920 == 23)

m.c74 = Constraint(expr= - m.x265 - m.x281 - m.x297 + m.x329 + m.x505 + m.x921 == 10)

m.c75 = Constraint(expr= - m.x266 - m.x282 - m.x298 + m.x330 + m.x506 + m.x922 == 12)

m.c76 = Constraint(expr= - m.x267 - m.x283 - m.x299 + m.x331 + m.x507 + m.x923 == 20)

m.c77 = Constraint(expr= - m.x268 - m.x284 - m.x300 + m.x332 + m.x508 + m.x924 == 19)

m.c78 = Constraint(expr= - m.x269 - m.x285 - m.x301 + m.x333 + m.x509 + m.x925 == 13)

m.c79 = Constraint(expr= - m.x270 - m.x286 - m.x302 + m.x334 + m.x510 + m.x926 == 7)

m.c80 = Constraint(expr= - m.x271 - m.x287 - m.x303 + m.x335 + m.x511 + m.x927 == 19)

m.c81 = Constraint(expr= - m.x272 - m.x288 - m.x304 + m.x336 + m.x512 + m.x928 == 12)

m.c82 = Constraint(expr=   m.x33 + m.x257 - m.x305 - m.x321 - m.x337 - m.x353 - m.x369 + m.x449 + m.x545 + m.x833 == 10)

m.c83 = Constraint(expr=   m.x34 + m.x258 - m.x306 - m.x322 - m.x338 - m.x354 - m.x370 + m.x450 + m.x546 + m.x834 == 8)

m.c84 = Constraint(expr=   m.x35 + m.x259 - m.x307 - m.x323 - m.x339 - m.x355 - m.x371 + m.x451 + m.x547 + m.x835 == 23)

m.c85 = Constraint(expr=   m.x36 + m.x260 - m.x308 - m.x324 - m.x340 - m.x356 - m.x372 + m.x452 + m.x548 + m.x836 == 24)

m.c86 = Constraint(expr=   m.x37 + m.x261 - m.x309 - m.x325 - m.x341 - m.x357 - m.x373 + m.x453 + m.x549 + m.x837 == 14)

m.c87 = Constraint(expr=   m.x38 + m.x262 - m.x310 - m.x326 - m.x342 - m.x358 - m.x374 + m.x454 + m.x550 + m.x838
                         == -242)

m.c88 = Constraint(expr=   m.x39 + m.x263 - m.x311 - m.x327 - m.x343 - m.x359 - m.x375 + m.x455 + m.x551 + m.x839 == 16)

m.c89 = Constraint(expr=   m.x40 + m.x264 - m.x312 - m.x328 - m.x344 - m.x360 - m.x376 + m.x456 + m.x552 + m.x840 == 9)

m.c90 = Constraint(expr=   m.x41 + m.x265 - m.x313 - m.x329 - m.x345 - m.x361 - m.x377 + m.x457 + m.x553 + m.x841 == 22)

m.c91 = Constraint(expr=   m.x42 + m.x266 - m.x314 - m.x330 - m.x346 - m.x362 - m.x378 + m.x458 + m.x554 + m.x842 == 16)

m.c92 = Constraint(expr=   m.x43 + m.x267 - m.x315 - m.x331 - m.x347 - m.x363 - m.x379 + m.x459 + m.x555 + m.x843 == 16)

m.c93 = Constraint(expr=   m.x44 + m.x268 - m.x316 - m.x332 - m.x348 - m.x364 - m.x380 + m.x460 + m.x556 + m.x844 == 14)

m.c94 = Constraint(expr=   m.x45 + m.x269 - m.x317 - m.x333 - m.x349 - m.x365 - m.x381 + m.x461 + m.x557 + m.x845 == 14)

m.c95 = Constraint(expr=   m.x46 + m.x270 - m.x318 - m.x334 - m.x350 - m.x366 - m.x382 + m.x462 + m.x558 + m.x846 == 6)

m.c96 = Constraint(expr=   m.x47 + m.x271 - m.x319 - m.x335 - m.x351 - m.x367 - m.x383 + m.x463 + m.x559 + m.x847 == 14)

m.c97 = Constraint(expr=   m.x48 + m.x272 - m.x320 - m.x336 - m.x352 - m.x368 - m.x384 + m.x464 + m.x560 + m.x848 == 21)

m.c98 = Constraint(expr=   m.x161 - m.x385 - m.x401 - m.x417 + m.x657 + m.x769 == 10)

m.c99 = Constraint(expr=   m.x162 - m.x386 - m.x402 - m.x418 + m.x658 + m.x770 == 8)

m.c100 = Constraint(expr=   m.x163 - m.x387 - m.x403 - m.x419 + m.x659 + m.x771 == 21)

m.c101 = Constraint(expr=   m.x164 - m.x388 - m.x404 - m.x420 + m.x660 + m.x772 == 19)

m.c102 = Constraint(expr=   m.x165 - m.x389 - m.x405 - m.x421 + m.x661 + m.x773 == 23)

m.c103 = Constraint(expr=   m.x166 - m.x390 - m.x406 - m.x422 + m.x662 + m.x774 == 23)

m.c104 = Constraint(expr=   m.x167 - m.x391 - m.x407 - m.x423 + m.x663 + m.x775 == -182)

m.c105 = Constraint(expr=   m.x168 - m.x392 - m.x408 - m.x424 + m.x664 + m.x776 == 19)

m.c106 = Constraint(expr=   m.x169 - m.x393 - m.x409 - m.x425 + m.x665 + m.x777 == 16)

m.c107 = Constraint(expr=   m.x170 - m.x394 - m.x410 - m.x426 + m.x666 + m.x778 == 16)

m.c108 = Constraint(expr=   m.x171 - m.x395 - m.x411 - m.x427 + m.x667 + m.x779 == 12)

m.c109 = Constraint(expr=   m.x172 - m.x396 - m.x412 - m.x428 + m.x668 + m.x780 == 11)

m.c110 = Constraint(expr=   m.x173 - m.x397 - m.x413 - m.x429 + m.x669 + m.x781 == 20)

m.c111 = Constraint(expr=   m.x174 - m.x398 - m.x414 - m.x430 + m.x670 + m.x782 == 6)

m.c112 = Constraint(expr=   m.x175 - m.x399 - m.x415 - m.x431 + m.x671 + m.x783 == 19)

m.c113 = Constraint(expr=   m.x176 - m.x400 - m.x416 - m.x432 + m.x672 + m.x784 == 22)

m.c114 = Constraint(expr=   m.x177 + m.x337 - m.x433 - m.x449 - m.x465 - m.x481 + m.x689 + m.x929 == 15)

m.c115 = Constraint(expr=   m.x178 + m.x338 - m.x434 - m.x450 - m.x466 - m.x482 + m.x690 + m.x930 == 19)

m.c116 = Constraint(expr=   m.x179 + m.x339 - m.x435 - m.x451 - m.x467 - m.x483 + m.x691 + m.x931 == 15)

m.c117 = Constraint(expr=   m.x180 + m.x340 - m.x436 - m.x452 - m.x468 - m.x484 + m.x692 + m.x932 == 9)

m.c118 = Constraint(expr=   m.x181 + m.x341 - m.x437 - m.x453 - m.x469 - m.x485 + m.x693 + m.x933 == 22)

m.c119 = Constraint(expr=   m.x182 + m.x342 - m.x438 - m.x454 - m.x470 - m.x486 + m.x694 + m.x934 == 16)

m.c120 = Constraint(expr=   m.x183 + m.x343 - m.x439 - m.x455 - m.x471 - m.x487 + m.x695 + m.x935 == 9)

m.c121 = Constraint(expr=   m.x184 + m.x344 - m.x440 - m.x456 - m.x472 - m.x488 + m.x696 + m.x936 == -215)

m.c122 = Constraint(expr=   m.x185 + m.x345 - m.x441 - m.x457 - m.x473 - m.x489 + m.x697 + m.x937 == 12)

m.c123 = Constraint(expr=   m.x186 + m.x346 - m.x442 - m.x458 - m.x474 - m.x490 + m.x698 + m.x938 == 7)

m.c124 = Constraint(expr=   m.x187 + m.x347 - m.x443 - m.x459 - m.x475 - m.x491 + m.x699 + m.x939 == 14)

m.c125 = Constraint(expr=   m.x188 + m.x348 - m.x444 - m.x460 - m.x476 - m.x492 + m.x700 + m.x940 == 14)

m.c126 = Constraint(expr=   m.x189 + m.x349 - m.x445 - m.x461 - m.x477 - m.x493 + m.x701 + m.x941 == 14)

m.c127 = Constraint(expr=   m.x190 + m.x350 - m.x446 - m.x462 - m.x478 - m.x494 + m.x702 + m.x942 == 11)

m.c128 = Constraint(expr=   m.x191 + m.x351 - m.x447 - m.x463 - m.x479 - m.x495 + m.x703 + m.x943 == 20)

m.c129 = Constraint(expr=   m.x192 + m.x352 - m.x448 - m.x464 - m.x480 - m.x496 + m.x704 + m.x944 == 25)

m.c130 = Constraint(expr=   m.x273 - m.x497 - m.x513 - m.x529 + m.x593 + m.x849 == 22)

m.c131 = Constraint(expr=   m.x274 - m.x498 - m.x514 - m.x530 + m.x594 + m.x850 == 22)

m.c132 = Constraint(expr=   m.x275 - m.x499 - m.x515 - m.x531 + m.x595 + m.x851 == 13)

m.c133 = Constraint(expr=   m.x276 - m.x500 - m.x516 - m.x532 + m.x596 + m.x852 == 6)

m.c134 = Constraint(expr=   m.x277 - m.x501 - m.x517 - m.x533 + m.x597 + m.x853 == 23)

m.c135 = Constraint(expr=   m.x278 - m.x502 - m.x518 - m.x534 + m.x598 + m.x854 == 11)

m.c136 = Constraint(expr=   m.x279 - m.x503 - m.x519 - m.x535 + m.x599 + m.x855 == 18)

m.c137 = Constraint(expr=   m.x280 - m.x504 - m.x520 - m.x536 + m.x600 + m.x856 == 23)

m.c138 = Constraint(expr=   m.x281 - m.x505 - m.x521 - m.x537 + m.x601 + m.x857 == -216)

m.c139 = Constraint(expr=   m.x282 - m.x506 - m.x522 - m.x538 + m.x602 + m.x858 == 9)

m.c140 = Constraint(expr=   m.x283 - m.x507 - m.x523 - m.x539 + m.x603 + m.x859 == 17)

m.c141 = Constraint(expr=   m.x284 - m.x508 - m.x524 - m.x540 + m.x604 + m.x860 == 20)

m.c142 = Constraint(expr=   m.x285 - m.x509 - m.x525 - m.x541 + m.x605 + m.x861 == 19)

m.c143 = Constraint(expr=   m.x286 - m.x510 - m.x526 - m.x542 + m.x606 + m.x862 == 9)

m.c144 = Constraint(expr=   m.x287 - m.x511 - m.x527 - m.x543 + m.x607 + m.x863 == 14)

m.c145 = Constraint(expr=   m.x288 - m.x512 - m.x528 - m.x544 + m.x608 + m.x864 == 18)

m.c146 = Constraint(expr=   m.x353 - m.x545 - m.x561 + m.x609 == 18)

m.c147 = Constraint(expr=   m.x354 - m.x546 - m.x562 + m.x610 == 15)

m.c148 = Constraint(expr=   m.x355 - m.x547 - m.x563 + m.x611 == 15)

m.c149 = Constraint(expr=   m.x356 - m.x548 - m.x564 + m.x612 == 23)

m.c150 = Constraint(expr=   m.x357 - m.x549 - m.x565 + m.x613 == 11)

m.c151 = Constraint(expr=   m.x358 - m.x550 - m.x566 + m.x614 == 21)

m.c152 = Constraint(expr=   m.x359 - m.x551 - m.x567 + m.x615 == 8)

m.c153 = Constraint(expr=   m.x360 - m.x552 - m.x568 + m.x616 == 10)

m.c154 = Constraint(expr=   m.x361 - m.x553 - m.x569 + m.x617 == 16)

m.c155 = Constraint(expr=   m.x362 - m.x554 - m.x570 + m.x618 == -180)

m.c156 = Constraint(expr=   m.x363 - m.x555 - m.x571 + m.x619 == 12)

m.c157 = Constraint(expr=   m.x364 - m.x556 - m.x572 + m.x620 == 9)

m.c158 = Constraint(expr=   m.x365 - m.x557 - m.x573 + m.x621 == 8)

m.c159 = Constraint(expr=   m.x366 - m.x558 - m.x574 + m.x622 == 5)

m.c160 = Constraint(expr=   m.x367 - m.x559 - m.x575 + m.x623 == 16)

m.c161 = Constraint(expr=   m.x368 - m.x560 - m.x576 + m.x624 == 8)

m.c162 = Constraint(expr=   m.x49 + m.x513 + m.x561 - m.x577 - m.x593 - m.x609 - m.x625 + m.x785 == 8)

m.c163 = Constraint(expr=   m.x50 + m.x514 + m.x562 - m.x578 - m.x594 - m.x610 - m.x626 + m.x786 == 22)

m.c164 = Constraint(expr=   m.x51 + m.x515 + m.x563 - m.x579 - m.x595 - m.x611 - m.x627 + m.x787 == 8)

m.c165 = Constraint(expr=   m.x52 + m.x516 + m.x564 - m.x580 - m.x596 - m.x612 - m.x628 + m.x788 == 20)

m.c166 = Constraint(expr=   m.x53 + m.x517 + m.x565 - m.x581 - m.x597 - m.x613 - m.x629 + m.x789 == 14)

m.c167 = Constraint(expr=   m.x54 + m.x518 + m.x566 - m.x582 - m.x598 - m.x614 - m.x630 + m.x790 == 20)

m.c168 = Constraint(expr=   m.x55 + m.x519 + m.x567 - m.x583 - m.x599 - m.x615 - m.x631 + m.x791 == 15)

m.c169 = Constraint(expr=   m.x56 + m.x520 + m.x568 - m.x584 - m.x600 - m.x616 - m.x632 + m.x792 == 13)

m.c170 = Constraint(expr=   m.x57 + m.x521 + m.x569 - m.x585 - m.x601 - m.x617 - m.x633 + m.x793 == 22)

m.c171 = Constraint(expr=   m.x58 + m.x522 + m.x570 - m.x586 - m.x602 - m.x618 - m.x634 + m.x794 == 9)

m.c172 = Constraint(expr=   m.x59 + m.x523 + m.x571 - m.x587 - m.x603 - m.x619 - m.x635 + m.x795 == -203)

m.c173 = Constraint(expr=   m.x60 + m.x524 + m.x572 - m.x588 - m.x604 - m.x620 - m.x636 + m.x796 == 9)

m.c174 = Constraint(expr=   m.x61 + m.x525 + m.x573 - m.x589 - m.x605 - m.x621 - m.x637 + m.x797 == 7)

m.c175 = Constraint(expr=   m.x62 + m.x526 + m.x574 - m.x590 - m.x606 - m.x622 - m.x638 + m.x798 == 17)

m.c176 = Constraint(expr=   m.x63 + m.x527 + m.x575 - m.x591 - m.x607 - m.x623 - m.x639 + m.x799 == 23)

m.c177 = Constraint(expr=   m.x64 + m.x528 + m.x576 - m.x592 - m.x608 - m.x624 - m.x640 + m.x800 == 13)

m.c178 = Constraint(expr=   m.x193 + m.x401 - m.x641 - m.x657 - m.x673 + m.x705 == 7)

m.c179 = Constraint(expr=   m.x194 + m.x402 - m.x642 - m.x658 - m.x674 + m.x706 == 8)

m.c180 = Constraint(expr=   m.x195 + m.x403 - m.x643 - m.x659 - m.x675 + m.x707 == 12)

m.c181 = Constraint(expr=   m.x196 + m.x404 - m.x644 - m.x660 - m.x676 + m.x708 == 19)

m.c182 = Constraint(expr=   m.x197 + m.x405 - m.x645 - m.x661 - m.x677 + m.x709 == 20)

m.c183 = Constraint(expr=   m.x198 + m.x406 - m.x646 - m.x662 - m.x678 + m.x710 == 18)

m.c184 = Constraint(expr=   m.x199 + m.x407 - m.x647 - m.x663 - m.x679 + m.x711 == 7)

m.c185 = Constraint(expr=   m.x200 + m.x408 - m.x648 - m.x664 - m.x680 + m.x712 == 13)

m.c186 = Constraint(expr=   m.x201 + m.x409 - m.x649 - m.x665 - m.x681 + m.x713 == 13)

m.c187 = Constraint(expr=   m.x202 + m.x410 - m.x650 - m.x666 - m.x682 + m.x714 == 15)

m.c188 = Constraint(expr=   m.x203 + m.x411 - m.x651 - m.x667 - m.x683 + m.x715 == 8)

m.c189 = Constraint(expr=   m.x204 + m.x412 - m.x652 - m.x668 - m.x684 + m.x716 == -214)

m.c190 = Constraint(expr=   m.x205 + m.x413 - m.x653 - m.x669 - m.x685 + m.x717 == 18)

m.c191 = Constraint(expr=   m.x206 + m.x414 - m.x654 - m.x670 - m.x686 + m.x718 == 25)

m.c192 = Constraint(expr=   m.x207 + m.x415 - m.x655 - m.x671 - m.x687 + m.x719 == 12)

m.c193 = Constraint(expr=   m.x208 + m.x416 - m.x656 - m.x672 - m.x688 + m.x720 == 8)

m.c194 = Constraint(expr=   m.x465 + m.x673 - m.x689 - m.x705 - m.x721 + m.x865 == 22)

m.c195 = Constraint(expr=   m.x466 + m.x674 - m.x690 - m.x706 - m.x722 + m.x866 == 11)

m.c196 = Constraint(expr=   m.x467 + m.x675 - m.x691 - m.x707 - m.x723 + m.x867 == 25)

m.c197 = Constraint(expr=   m.x468 + m.x676 - m.x692 - m.x708 - m.x724 + m.x868 == 17)

m.c198 = Constraint(expr=   m.x469 + m.x677 - m.x693 - m.x709 - m.x725 + m.x869 == 14)

m.c199 = Constraint(expr=   m.x470 + m.x678 - m.x694 - m.x710 - m.x726 + m.x870 == 17)

m.c200 = Constraint(expr=   m.x471 + m.x679 - m.x695 - m.x711 - m.x727 + m.x871 == 7)

m.c201 = Constraint(expr=   m.x472 + m.x680 - m.x696 - m.x712 - m.x728 + m.x872 == 25)

m.c202 = Constraint(expr=   m.x473 + m.x681 - m.x697 - m.x713 - m.x729 + m.x873 == 5)

m.c203 = Constraint(expr=   m.x474 + m.x682 - m.x698 - m.x714 - m.x730 + m.x874 == 11)

m.c204 = Constraint(expr=   m.x475 + m.x683 - m.x699 - m.x715 - m.x731 + m.x875 == 7)

m.c205 = Constraint(expr=   m.x476 + m.x684 - m.x700 - m.x716 - m.x732 + m.x876 == 20)

m.c206 = Constraint(expr=   m.x477 + m.x685 - m.x701 - m.x717 - m.x733 + m.x877 == -217)

m.c207 = Constraint(expr=   m.x478 + m.x686 - m.x702 - m.x718 - m.x734 + m.x878 == 7)

m.c208 = Constraint(expr=   m.x479 + m.x687 - m.x703 - m.x719 - m.x735 + m.x879 == 23)

m.c209 = Constraint(expr=   m.x480 + m.x688 - m.x704 - m.x720 - m.x736 + m.x880 == 13)

m.c210 = Constraint(expr=   m.x113 + m.x241 + m.x417 + m.x625 - m.x737 - m.x753 - m.x769 - m.x785 - m.x801 + m.x881
                          == 14)

m.c211 = Constraint(expr=   m.x114 + m.x242 + m.x418 + m.x626 - m.x738 - m.x754 - m.x770 - m.x786 - m.x802 + m.x882
                          == 23)

m.c212 = Constraint(expr=   m.x115 + m.x243 + m.x419 + m.x627 - m.x739 - m.x755 - m.x771 - m.x787 - m.x803 + m.x883
                          == 9)

m.c213 = Constraint(expr=   m.x116 + m.x244 + m.x420 + m.x628 - m.x740 - m.x756 - m.x772 - m.x788 - m.x804 + m.x884
                          == 13)

m.c214 = Constraint(expr=   m.x117 + m.x245 + m.x421 + m.x629 - m.x741 - m.x757 - m.x773 - m.x789 - m.x805 + m.x885
                          == 16)

m.c215 = Constraint(expr=   m.x118 + m.x246 + m.x422 + m.x630 - m.x742 - m.x758 - m.x774 - m.x790 - m.x806 + m.x886
                          == 24)

m.c216 = Constraint(expr=   m.x119 + m.x247 + m.x423 + m.x631 - m.x743 - m.x759 - m.x775 - m.x791 - m.x807 + m.x887
                          == 7)

m.c217 = Constraint(expr=   m.x120 + m.x248 + m.x424 + m.x632 - m.x744 - m.x760 - m.x776 - m.x792 - m.x808 + m.x888
                          == 6)

m.c218 = Constraint(expr=   m.x121 + m.x249 + m.x425 + m.x633 - m.x745 - m.x761 - m.x777 - m.x793 - m.x809 + m.x889
                          == 22)

m.c219 = Constraint(expr=   m.x122 + m.x250 + m.x426 + m.x634 - m.x746 - m.x762 - m.x778 - m.x794 - m.x810 + m.x890
                          == 10)

m.c220 = Constraint(expr=   m.x123 + m.x251 + m.x427 + m.x635 - m.x747 - m.x763 - m.x779 - m.x795 - m.x811 + m.x891
                          == 23)

m.c221 = Constraint(expr=   m.x124 + m.x252 + m.x428 + m.x636 - m.x748 - m.x764 - m.x780 - m.x796 - m.x812 + m.x892
                          == 22)

m.c222 = Constraint(expr=   m.x125 + m.x253 + m.x429 + m.x637 - m.x749 - m.x765 - m.x781 - m.x797 - m.x813 + m.x893
                          == 12)

m.c223 = Constraint(expr=   m.x126 + m.x254 + m.x430 + m.x638 - m.x750 - m.x766 - m.x782 - m.x798 - m.x814 + m.x894
                          == -189)

m.c224 = Constraint(expr=   m.x127 + m.x255 + m.x431 + m.x639 - m.x751 - m.x767 - m.x783 - m.x799 - m.x815 + m.x895
                          == 13)

m.c225 = Constraint(expr=   m.x128 + m.x256 + m.x432 + m.x640 - m.x752 - m.x768 - m.x784 - m.x800 - m.x816 + m.x896
                          == 22)

m.c226 = Constraint(expr=   m.x129 + m.x369 + m.x529 + m.x721 + m.x801 - m.x817 - m.x833 - m.x849 - m.x865 - m.x881
                          - m.x897 + m.x945 == 6)

m.c227 = Constraint(expr=   m.x130 + m.x370 + m.x530 + m.x722 + m.x802 - m.x818 - m.x834 - m.x850 - m.x866 - m.x882
                          - m.x898 + m.x946 == 5)

m.c228 = Constraint(expr=   m.x131 + m.x371 + m.x531 + m.x723 + m.x803 - m.x819 - m.x835 - m.x851 - m.x867 - m.x883
                          - m.x899 + m.x947 == 6)

m.c229 = Constraint(expr=   m.x132 + m.x372 + m.x532 + m.x724 + m.x804 - m.x820 - m.x836 - m.x852 - m.x868 - m.x884
                          - m.x900 + m.x948 == 12)

m.c230 = Constraint(expr=   m.x133 + m.x373 + m.x533 + m.x725 + m.x805 - m.x821 - m.x837 - m.x853 - m.x869 - m.x885
                          - m.x901 + m.x949 == 15)

m.c231 = Constraint(expr=   m.x134 + m.x374 + m.x534 + m.x726 + m.x806 - m.x822 - m.x838 - m.x854 - m.x870 - m.x886
                          - m.x902 + m.x950 == 8)

m.c232 = Constraint(expr=   m.x135 + m.x375 + m.x535 + m.x727 + m.x807 - m.x823 - m.x839 - m.x855 - m.x871 - m.x887
                          - m.x903 + m.x951 == 10)

m.c233 = Constraint(expr=   m.x136 + m.x376 + m.x536 + m.x728 + m.x808 - m.x824 - m.x840 - m.x856 - m.x872 - m.x888
                          - m.x904 + m.x952 == 10)

m.c234 = Constraint(expr=   m.x137 + m.x377 + m.x537 + m.x729 + m.x809 - m.x825 - m.x841 - m.x857 - m.x873 - m.x889
                          - m.x905 + m.x953 == 7)

m.c235 = Constraint(expr=   m.x138 + m.x378 + m.x538 + m.x730 + m.x810 - m.x826 - m.x842 - m.x858 - m.x874 - m.x890
                          - m.x906 + m.x954 == 15)

m.c236 = Constraint(expr=   m.x139 + m.x379 + m.x539 + m.x731 + m.x811 - m.x827 - m.x843 - m.x859 - m.x875 - m.x891
                          - m.x907 + m.x955 == 5)

m.c237 = Constraint(expr=   m.x140 + m.x380 + m.x540 + m.x732 + m.x812 - m.x828 - m.x844 - m.x860 - m.x876 - m.x892
                          - m.x908 + m.x956 == 20)

m.c238 = Constraint(expr=   m.x141 + m.x381 + m.x541 + m.x733 + m.x813 - m.x829 - m.x845 - m.x861 - m.x877 - m.x893
                          - m.x909 + m.x957 == 14)

m.c239 = Constraint(expr=   m.x142 + m.x382 + m.x542 + m.x734 + m.x814 - m.x830 - m.x846 - m.x862 - m.x878 - m.x894
                          - m.x910 + m.x958 == 17)

m.c240 = Constraint(expr=   m.x143 + m.x383 + m.x543 + m.x735 + m.x815 - m.x831 - m.x847 - m.x863 - m.x879 - m.x895
                          - m.x911 + m.x959 == -240)

m.c241 = Constraint(expr=   m.x144 + m.x384 + m.x544 + m.x736 + m.x816 - m.x832 - m.x848 - m.x864 - m.x880 - m.x896
                          - m.x912 + m.x960 == 7)

m.c242 = Constraint(expr=   m.x289 + m.x481 + m.x897 - m.x913 - m.x929 - m.x945 == 25)

m.c243 = Constraint(expr=   m.x290 + m.x482 + m.x898 - m.x914 - m.x930 - m.x946 == 23)

m.c244 = Constraint(expr=   m.x291 + m.x483 + m.x899 - m.x915 - m.x931 - m.x947 == 22)

m.c245 = Constraint(expr=   m.x292 + m.x484 + m.x900 - m.x916 - m.x932 - m.x948 == 17)

m.c246 = Constraint(expr=   m.x293 + m.x485 + m.x901 - m.x917 - m.x933 - m.x949 == 13)

m.c247 = Constraint(expr=   m.x294 + m.x486 + m.x902 - m.x918 - m.x934 - m.x950 == 9)

m.c248 = Constraint(expr=   m.x295 + m.x487 + m.x903 - m.x919 - m.x935 - m.x951 == 24)

m.c249 = Constraint(expr=   m.x296 + m.x488 + m.x904 - m.x920 - m.x936 - m.x952 == 25)

m.c250 = Constraint(expr=   m.x297 + m.x489 + m.x905 - m.x921 - m.x937 - m.x953 == 8)

m.c251 = Constraint(expr=   m.x298 + m.x490 + m.x906 - m.x922 - m.x938 - m.x954 == 10)

m.c252 = Constraint(expr=   m.x299 + m.x491 + m.x907 - m.x923 - m.x939 - m.x955 == 9)

m.c253 = Constraint(expr=   m.x300 + m.x492 + m.x908 - m.x924 - m.x940 - m.x956 == 20)

m.c254 = Constraint(expr=   m.x301 + m.x493 + m.x909 - m.x925 - m.x941 - m.x957 == 7)

m.c255 = Constraint(expr=   m.x302 + m.x494 + m.x910 - m.x926 - m.x942 - m.x958 == 20)

m.c256 = Constraint(expr=   m.x303 + m.x495 + m.x911 - m.x927 - m.x943 - m.x959 == 8)

m.c257 = Constraint(expr=   m.x304 + m.x496 + m.x912 - m.x928 - m.x944 - m.x960 == -226)

m.c258 = Constraint(expr= - m.x1 - m.x2 - m.x3 - m.x4 - m.x5 - m.x6 - m.x7 - m.x8 - m.x9 - m.x10 - m.x11 - m.x12 - m.x13
                          - m.x14 - m.x15 - m.x16 + m.x1082 >= 0)

m.c259 = Constraint(expr= - m.x17 - m.x18 - m.x19 - m.x20 - m.x21 - m.x22 - m.x23 - m.x24 - m.x25 - m.x26 - m.x27
                          - m.x28 - m.x29 - m.x30 - m.x31 - m.x32 + m.x1083 >= 0)

m.c260 = Constraint(expr= - m.x33 - m.x34 - m.x35 - m.x36 - m.x37 - m.x38 - m.x39 - m.x40 - m.x41 - m.x42 - m.x43
                          - m.x44 - m.x45 - m.x46 - m.x47 - m.x48 + m.x1084 >= 0)

m.c261 = Constraint(expr= - m.x49 - m.x50 - m.x51 - m.x52 - m.x53 - m.x54 - m.x55 - m.x56 - m.x57 - m.x58 - m.x59
                          - m.x60 - m.x61 - m.x62 - m.x63 - m.x64 + m.x1085 >= 0)

m.c262 = Constraint(expr= - m.x65 - m.x66 - m.x67 - m.x68 - m.x69 - m.x70 - m.x71 - m.x72 - m.x73 - m.x74 - m.x75
                          - m.x76 - m.x77 - m.x78 - m.x79 - m.x80 + m.x1086 >= 0)

m.c263 = Constraint(expr= - m.x81 - m.x82 - m.x83 - m.x84 - m.x85 - m.x86 - m.x87 - m.x88 - m.x89 - m.x90 - m.x91
                          - m.x92 - m.x93 - m.x94 - m.x95 - m.x96 + m.x1087 >= 0)

m.c264 = Constraint(expr= - m.x97 - m.x98 - m.x99 - m.x100 - m.x101 - m.x102 - m.x103 - m.x104 - m.x105 - m.x106
                          - m.x107 - m.x108 - m.x109 - m.x110 - m.x111 - m.x112 + m.x1088 >= 0)

m.c265 = Constraint(expr= - m.x113 - m.x114 - m.x115 - m.x116 - m.x117 - m.x118 - m.x119 - m.x120 - m.x121 - m.x122
                          - m.x123 - m.x124 - m.x125 - m.x126 - m.x127 - m.x128 + m.x1089 >= 0)

m.c266 = Constraint(expr= - m.x129 - m.x130 - m.x131 - m.x132 - m.x133 - m.x134 - m.x135 - m.x136 - m.x137 - m.x138
                          - m.x139 - m.x140 - m.x141 - m.x142 - m.x143 - m.x144 + m.x1090 >= 0)

m.c267 = Constraint(expr= - m.x145 - m.x146 - m.x147 - m.x148 - m.x149 - m.x150 - m.x151 - m.x152 - m.x153 - m.x154
                          - m.x155 - m.x156 - m.x157 - m.x158 - m.x159 - m.x160 + m.x1091 >= 0)

m.c268 = Constraint(expr= - m.x161 - m.x162 - m.x163 - m.x164 - m.x165 - m.x166 - m.x167 - m.x168 - m.x169 - m.x170
                          - m.x171 - m.x172 - m.x173 - m.x174 - m.x175 - m.x176 + m.x1092 >= 0)

m.c269 = Constraint(expr= - m.x177 - m.x178 - m.x179 - m.x180 - m.x181 - m.x182 - m.x183 - m.x184 - m.x185 - m.x186
                          - m.x187 - m.x188 - m.x189 - m.x190 - m.x191 - m.x192 + m.x1093 >= 0)

m.c270 = Constraint(expr= - m.x193 - m.x194 - m.x195 - m.x196 - m.x197 - m.x198 - m.x199 - m.x200 - m.x201 - m.x202
                          - m.x203 - m.x204 - m.x205 - m.x206 - m.x207 - m.x208 + m.x1094 >= 0)

m.c271 = Constraint(expr= - m.x209 - m.x210 - m.x211 - m.x212 - m.x213 - m.x214 - m.x215 - m.x216 - m.x217 - m.x218
                          - m.x219 - m.x220 - m.x221 - m.x222 - m.x223 - m.x224 + m.x1095 >= 0)

m.c272 = Constraint(expr= - m.x225 - m.x226 - m.x227 - m.x228 - m.x229 - m.x230 - m.x231 - m.x232 - m.x233 - m.x234
                          - m.x235 - m.x236 - m.x237 - m.x238 - m.x239 - m.x240 + m.x1096 >= 0)

m.c273 = Constraint(expr= - m.x241 - m.x242 - m.x243 - m.x244 - m.x245 - m.x246 - m.x247 - m.x248 - m.x249 - m.x250
                          - m.x251 - m.x252 - m.x253 - m.x254 - m.x255 - m.x256 + m.x1097 >= 0)

m.c274 = Constraint(expr= - m.x257 - m.x258 - m.x259 - m.x260 - m.x261 - m.x262 - m.x263 - m.x264 - m.x265 - m.x266
                          - m.x267 - m.x268 - m.x269 - m.x270 - m.x271 - m.x272 + m.x1098 >= 0)

m.c275 = Constraint(expr= - m.x273 - m.x274 - m.x275 - m.x276 - m.x277 - m.x278 - m.x279 - m.x280 - m.x281 - m.x282
                          - m.x283 - m.x284 - m.x285 - m.x286 - m.x287 - m.x288 + m.x1099 >= 0)

m.c276 = Constraint(expr= - m.x289 - m.x290 - m.x291 - m.x292 - m.x293 - m.x294 - m.x295 - m.x296 - m.x297 - m.x298
                          - m.x299 - m.x300 - m.x301 - m.x302 - m.x303 - m.x304 + m.x1100 >= 0)

m.c277 = Constraint(expr= - m.x305 - m.x306 - m.x307 - m.x308 - m.x309 - m.x310 - m.x311 - m.x312 - m.x313 - m.x314
                          - m.x315 - m.x316 - m.x317 - m.x318 - m.x319 - m.x320 + m.x1101 >= 0)

m.c278 = Constraint(expr= - m.x321 - m.x322 - m.x323 - m.x324 - m.x325 - m.x326 - m.x327 - m.x328 - m.x329 - m.x330
                          - m.x331 - m.x332 - m.x333 - m.x334 - m.x335 - m.x336 + m.x1102 >= 0)

m.c279 = Constraint(expr= - m.x337 - m.x338 - m.x339 - m.x340 - m.x341 - m.x342 - m.x343 - m.x344 - m.x345 - m.x346
                          - m.x347 - m.x348 - m.x349 - m.x350 - m.x351 - m.x352 + m.x1103 >= 0)

m.c280 = Constraint(expr= - m.x353 - m.x354 - m.x355 - m.x356 - m.x357 - m.x358 - m.x359 - m.x360 - m.x361 - m.x362
                          - m.x363 - m.x364 - m.x365 - m.x366 - m.x367 - m.x368 + m.x1104 >= 0)

m.c281 = Constraint(expr= - m.x369 - m.x370 - m.x371 - m.x372 - m.x373 - m.x374 - m.x375 - m.x376 - m.x377 - m.x378
                          - m.x379 - m.x380 - m.x381 - m.x382 - m.x383 - m.x384 + m.x1105 >= 0)

m.c282 = Constraint(expr= - m.x385 - m.x386 - m.x387 - m.x388 - m.x389 - m.x390 - m.x391 - m.x392 - m.x393 - m.x394
                          - m.x395 - m.x396 - m.x397 - m.x398 - m.x399 - m.x400 + m.x1106 >= 0)

m.c283 = Constraint(expr= - m.x401 - m.x402 - m.x403 - m.x404 - m.x405 - m.x406 - m.x407 - m.x408 - m.x409 - m.x410
                          - m.x411 - m.x412 - m.x413 - m.x414 - m.x415 - m.x416 + m.x1107 >= 0)

m.c284 = Constraint(expr= - m.x417 - m.x418 - m.x419 - m.x420 - m.x421 - m.x422 - m.x423 - m.x424 - m.x425 - m.x426
                          - m.x427 - m.x428 - m.x429 - m.x430 - m.x431 - m.x432 + m.x1108 >= 0)

m.c285 = Constraint(expr= - m.x433 - m.x434 - m.x435 - m.x436 - m.x437 - m.x438 - m.x439 - m.x440 - m.x441 - m.x442
                          - m.x443 - m.x444 - m.x445 - m.x446 - m.x447 - m.x448 + m.x1109 >= 0)

m.c286 = Constraint(expr= - m.x449 - m.x450 - m.x451 - m.x452 - m.x453 - m.x454 - m.x455 - m.x456 - m.x457 - m.x458
                          - m.x459 - m.x460 - m.x461 - m.x462 - m.x463 - m.x464 + m.x1110 >= 0)

m.c287 = Constraint(expr= - m.x465 - m.x466 - m.x467 - m.x468 - m.x469 - m.x470 - m.x471 - m.x472 - m.x473 - m.x474
                          - m.x475 - m.x476 - m.x477 - m.x478 - m.x479 - m.x480 + m.x1111 >= 0)

m.c288 = Constraint(expr= - m.x481 - m.x482 - m.x483 - m.x484 - m.x485 - m.x486 - m.x487 - m.x488 - m.x489 - m.x490
                          - m.x491 - m.x492 - m.x493 - m.x494 - m.x495 - m.x496 + m.x1112 >= 0)

m.c289 = Constraint(expr= - m.x497 - m.x498 - m.x499 - m.x500 - m.x501 - m.x502 - m.x503 - m.x504 - m.x505 - m.x506
                          - m.x507 - m.x508 - m.x509 - m.x510 - m.x511 - m.x512 + m.x1113 >= 0)

m.c290 = Constraint(expr= - m.x513 - m.x514 - m.x515 - m.x516 - m.x517 - m.x518 - m.x519 - m.x520 - m.x521 - m.x522
                          - m.x523 - m.x524 - m.x525 - m.x526 - m.x527 - m.x528 + m.x1114 >= 0)

m.c291 = Constraint(expr= - m.x529 - m.x530 - m.x531 - m.x532 - m.x533 - m.x534 - m.x535 - m.x536 - m.x537 - m.x538
                          - m.x539 - m.x540 - m.x541 - m.x542 - m.x543 - m.x544 + m.x1115 >= 0)

m.c292 = Constraint(expr= - m.x545 - m.x546 - m.x547 - m.x548 - m.x549 - m.x550 - m.x551 - m.x552 - m.x553 - m.x554
                          - m.x555 - m.x556 - m.x557 - m.x558 - m.x559 - m.x560 + m.x1116 >= 0)

m.c293 = Constraint(expr= - m.x561 - m.x562 - m.x563 - m.x564 - m.x565 - m.x566 - m.x567 - m.x568 - m.x569 - m.x570
                          - m.x571 - m.x572 - m.x573 - m.x574 - m.x575 - m.x576 + m.x1117 >= 0)

m.c294 = Constraint(expr= - m.x577 - m.x578 - m.x579 - m.x580 - m.x581 - m.x582 - m.x583 - m.x584 - m.x585 - m.x586
                          - m.x587 - m.x588 - m.x589 - m.x590 - m.x591 - m.x592 + m.x1118 >= 0)

m.c295 = Constraint(expr= - m.x593 - m.x594 - m.x595 - m.x596 - m.x597 - m.x598 - m.x599 - m.x600 - m.x601 - m.x602
                          - m.x603 - m.x604 - m.x605 - m.x606 - m.x607 - m.x608 + m.x1119 >= 0)

m.c296 = Constraint(expr= - m.x609 - m.x610 - m.x611 - m.x612 - m.x613 - m.x614 - m.x615 - m.x616 - m.x617 - m.x618
                          - m.x619 - m.x620 - m.x621 - m.x622 - m.x623 - m.x624 + m.x1120 >= 0)

m.c297 = Constraint(expr= - m.x625 - m.x626 - m.x627 - m.x628 - m.x629 - m.x630 - m.x631 - m.x632 - m.x633 - m.x634
                          - m.x635 - m.x636 - m.x637 - m.x638 - m.x639 - m.x640 + m.x1121 >= 0)

m.c298 = Constraint(expr= - m.x641 - m.x642 - m.x643 - m.x644 - m.x645 - m.x646 - m.x647 - m.x648 - m.x649 - m.x650
                          - m.x651 - m.x652 - m.x653 - m.x654 - m.x655 - m.x656 + m.x1122 >= 0)

m.c299 = Constraint(expr= - m.x657 - m.x658 - m.x659 - m.x660 - m.x661 - m.x662 - m.x663 - m.x664 - m.x665 - m.x666
                          - m.x667 - m.x668 - m.x669 - m.x670 - m.x671 - m.x672 + m.x1123 >= 0)

m.c300 = Constraint(expr= - m.x673 - m.x674 - m.x675 - m.x676 - m.x677 - m.x678 - m.x679 - m.x680 - m.x681 - m.x682
                          - m.x683 - m.x684 - m.x685 - m.x686 - m.x687 - m.x688 + m.x1124 >= 0)

m.c301 = Constraint(expr= - m.x689 - m.x690 - m.x691 - m.x692 - m.x693 - m.x694 - m.x695 - m.x696 - m.x697 - m.x698
                          - m.x699 - m.x700 - m.x701 - m.x702 - m.x703 - m.x704 + m.x1125 >= 0)

m.c302 = Constraint(expr= - m.x705 - m.x706 - m.x707 - m.x708 - m.x709 - m.x710 - m.x711 - m.x712 - m.x713 - m.x714
                          - m.x715 - m.x716 - m.x717 - m.x718 - m.x719 - m.x720 + m.x1126 >= 0)

m.c303 = Constraint(expr= - m.x721 - m.x722 - m.x723 - m.x724 - m.x725 - m.x726 - m.x727 - m.x728 - m.x729 - m.x730
                          - m.x731 - m.x732 - m.x733 - m.x734 - m.x735 - m.x736 + m.x1127 >= 0)

m.c304 = Constraint(expr= - m.x737 - m.x738 - m.x739 - m.x740 - m.x741 - m.x742 - m.x743 - m.x744 - m.x745 - m.x746
                          - m.x747 - m.x748 - m.x749 - m.x750 - m.x751 - m.x752 + m.x1128 >= 0)

m.c305 = Constraint(expr= - m.x753 - m.x754 - m.x755 - m.x756 - m.x757 - m.x758 - m.x759 - m.x760 - m.x761 - m.x762
                          - m.x763 - m.x764 - m.x765 - m.x766 - m.x767 - m.x768 + m.x1129 >= 0)

m.c306 = Constraint(expr= - m.x769 - m.x770 - m.x771 - m.x772 - m.x773 - m.x774 - m.x775 - m.x776 - m.x777 - m.x778
                          - m.x779 - m.x780 - m.x781 - m.x782 - m.x783 - m.x784 + m.x1130 >= 0)

m.c307 = Constraint(expr= - m.x785 - m.x786 - m.x787 - m.x788 - m.x789 - m.x790 - m.x791 - m.x792 - m.x793 - m.x794
                          - m.x795 - m.x796 - m.x797 - m.x798 - m.x799 - m.x800 + m.x1131 >= 0)

m.c308 = Constraint(expr= - m.x801 - m.x802 - m.x803 - m.x804 - m.x805 - m.x806 - m.x807 - m.x808 - m.x809 - m.x810
                          - m.x811 - m.x812 - m.x813 - m.x814 - m.x815 - m.x816 + m.x1132 >= 0)

m.c309 = Constraint(expr= - m.x817 - m.x818 - m.x819 - m.x820 - m.x821 - m.x822 - m.x823 - m.x824 - m.x825 - m.x826
                          - m.x827 - m.x828 - m.x829 - m.x830 - m.x831 - m.x832 + m.x1133 >= 0)

m.c310 = Constraint(expr= - m.x833 - m.x834 - m.x835 - m.x836 - m.x837 - m.x838 - m.x839 - m.x840 - m.x841 - m.x842
                          - m.x843 - m.x844 - m.x845 - m.x846 - m.x847 - m.x848 + m.x1134 >= 0)

m.c311 = Constraint(expr= - m.x849 - m.x850 - m.x851 - m.x852 - m.x853 - m.x854 - m.x855 - m.x856 - m.x857 - m.x858
                          - m.x859 - m.x860 - m.x861 - m.x862 - m.x863 - m.x864 + m.x1135 >= 0)

m.c312 = Constraint(expr= - m.x865 - m.x866 - m.x867 - m.x868 - m.x869 - m.x870 - m.x871 - m.x872 - m.x873 - m.x874
                          - m.x875 - m.x876 - m.x877 - m.x878 - m.x879 - m.x880 + m.x1136 >= 0)

m.c313 = Constraint(expr= - m.x881 - m.x882 - m.x883 - m.x884 - m.x885 - m.x886 - m.x887 - m.x888 - m.x889 - m.x890
                          - m.x891 - m.x892 - m.x893 - m.x894 - m.x895 - m.x896 + m.x1137 >= 0)

m.c314 = Constraint(expr= - m.x897 - m.x898 - m.x899 - m.x900 - m.x901 - m.x902 - m.x903 - m.x904 - m.x905 - m.x906
                          - m.x907 - m.x908 - m.x909 - m.x910 - m.x911 - m.x912 + m.x1138 >= 0)

m.c315 = Constraint(expr= - m.x913 - m.x914 - m.x915 - m.x916 - m.x917 - m.x918 - m.x919 - m.x920 - m.x921 - m.x922
                          - m.x923 - m.x924 - m.x925 - m.x926 - m.x927 - m.x928 + m.x1139 >= 0)

m.c316 = Constraint(expr= - m.x929 - m.x930 - m.x931 - m.x932 - m.x933 - m.x934 - m.x935 - m.x936 - m.x937 - m.x938
                          - m.x939 - m.x940 - m.x941 - m.x942 - m.x943 - m.x944 + m.x1140 >= 0)

m.c317 = Constraint(expr= - m.x945 - m.x946 - m.x947 - m.x948 - m.x949 - m.x950 - m.x951 - m.x952 - m.x953 - m.x954
                          - m.x955 - m.x956 - m.x957 - m.x958 - m.x959 - m.x960 + m.x1141 >= 0)

m.c318 = Constraint(expr=137*m.x1082*m.b961 - 137*m.b961*m.x1021 + m.x1082*m.x1021 <= 0)

m.c319 = Constraint(expr=505*m.x1083*m.b962 - 505*m.b962*m.x1022 + m.x1083*m.x1022 <= 0)

m.c320 = Constraint(expr=427*m.x1084*m.b963 - 427*m.b963*m.x1023 + m.x1084*m.x1023 <= 0)

m.c321 = Constraint(expr=559*m.x1085*m.b964 - 559*m.b964*m.x1024 + m.x1085*m.x1024 <= 0)

m.c322 = Constraint(expr=137*m.x1086*m.b965 - 137*m.b965*m.x1025 + m.x1086*m.x1025 <= 0)

m.c323 = Constraint(expr=196*m.x1087*m.b966 - 196*m.b966*m.x1026 + m.x1087*m.x1026 <= 0)

m.c324 = Constraint(expr=341*m.x1088*m.b967 - 341*m.b967*m.x1027 + m.x1088*m.x1027 <= 0)

m.c325 = Constraint(expr=263*m.x1089*m.b968 - 263*m.b968*m.x1028 + m.x1089*m.x1028 <= 0)

m.c326 = Constraint(expr=245*m.x1090*m.b969 - 245*m.b969*m.x1029 + m.x1090*m.x1029 <= 0)

m.c327 = Constraint(expr=196*m.x1091*m.b970 - 196*m.b970*m.x1030 + m.x1091*m.x1030 <= 0)

m.c328 = Constraint(expr=346*m.x1092*m.b971 - 346*m.b971*m.x1031 + m.x1092*m.x1031 <= 0)

m.c329 = Constraint(expr=361*m.x1093*m.b972 - 361*m.b972*m.x1032 + m.x1093*m.x1032 <= 0)

m.c330 = Constraint(expr=179*m.x1094*m.b973 - 179*m.b973*m.x1033 + m.x1094*m.x1033 <= 0)

m.c331 = Constraint(expr=505*m.x1095*m.b974 - 505*m.b974*m.x1034 + m.x1095*m.x1034 <= 0)

m.c332 = Constraint(expr=341*m.x1096*m.b975 - 341*m.b975*m.x1035 + m.x1096*m.x1035 <= 0)

m.c333 = Constraint(expr=160*m.x1097*m.b976 - 160*m.b976*m.x1036 + m.x1097*m.x1036 <= 0)

m.c334 = Constraint(expr=389*m.x1098*m.b977 - 389*m.b977*m.x1037 + m.x1098*m.x1037 <= 0)

m.c335 = Constraint(expr=153*m.x1099*m.b978 - 153*m.b978*m.x1038 + m.x1099*m.x1038 <= 0)

m.c336 = Constraint(expr=164*m.x1100*m.b979 - 164*m.b979*m.x1039 + m.x1100*m.x1039 <= 0)

m.c337 = Constraint(expr=427*m.x1101*m.b980 - 427*m.b980*m.x1040 + m.x1101*m.x1040 <= 0)

m.c338 = Constraint(expr=389*m.x1102*m.b981 - 389*m.b981*m.x1041 + m.x1102*m.x1041 <= 0)

m.c339 = Constraint(expr=513*m.x1103*m.b982 - 513*m.b982*m.x1042 + m.x1103*m.x1042 <= 0)

m.c340 = Constraint(expr=353*m.x1104*m.b983 - 353*m.b983*m.x1043 + m.x1104*m.x1043 <= 0)

m.c341 = Constraint(expr=305*m.x1105*m.b984 - 305*m.b984*m.x1044 + m.x1105*m.x1044 <= 0)

m.c342 = Constraint(expr=346*m.x1106*m.b985 - 346*m.b985*m.x1045 + m.x1106*m.x1045 <= 0)

m.c343 = Constraint(expr=463*m.x1107*m.b986 - 463*m.b986*m.x1046 + m.x1107*m.x1046 <= 0)

m.c344 = Constraint(expr=511*m.x1108*m.b987 - 511*m.b987*m.x1047 + m.x1108*m.x1047 <= 0)

m.c345 = Constraint(expr=361*m.x1109*m.b988 - 361*m.b988*m.x1048 + m.x1109*m.x1048 <= 0)

m.c346 = Constraint(expr=513*m.x1110*m.b989 - 513*m.b989*m.x1049 + m.x1110*m.x1049 <= 0)

m.c347 = Constraint(expr=218*m.x1111*m.b990 - 218*m.b990*m.x1050 + m.x1111*m.x1050 <= 0)

m.c348 = Constraint(expr=338*m.x1112*m.b991 - 338*m.b991*m.x1051 + m.x1112*m.x1051 <= 0)

m.c349 = Constraint(expr=153*m.x1113*m.b992 - 153*m.b992*m.x1052 + m.x1113*m.x1052 <= 0)

m.c350 = Constraint(expr=439*m.x1114*m.b993 - 439*m.b993*m.x1053 + m.x1114*m.x1053 <= 0)

m.c351 = Constraint(expr=194*m.x1115*m.b994 - 194*m.b994*m.x1054 + m.x1115*m.x1054 <= 0)

m.c352 = Constraint(expr=353*m.x1116*m.b995 - 353*m.b995*m.x1055 + m.x1116*m.x1055 <= 0)

m.c353 = Constraint(expr=415*m.x1117*m.b996 - 415*m.b996*m.x1056 + m.x1117*m.x1056 <= 0)

m.c354 = Constraint(expr=559*m.x1118*m.b997 - 559*m.b997*m.x1057 + m.x1118*m.x1057 <= 0)

m.c355 = Constraint(expr=439*m.x1119*m.b998 - 439*m.b998*m.x1058 + m.x1119*m.x1058 <= 0)

m.c356 = Constraint(expr=415*m.x1120*m.b999 - 415*m.b999*m.x1059 + m.x1120*m.x1059 <= 0)

m.c357 = Constraint(expr=421*m.x1121*m.b1000 - 421*m.b1000*m.x1060 + m.x1121*m.x1060 <= 0)

m.c358 = Constraint(expr=179*m.x1122*m.b1001 - 179*m.b1001*m.x1061 + m.x1122*m.x1061 <= 0)

m.c359 = Constraint(expr=463*m.x1123*m.b1002 - 463*m.b1002*m.x1062 + m.x1123*m.x1062 <= 0)

m.c360 = Constraint(expr=534*m.x1124*m.b1003 - 534*m.b1003*m.x1063 + m.x1124*m.x1063 <= 0)

m.c361 = Constraint(expr=218*m.x1125*m.b1004 - 218*m.b1004*m.x1064 + m.x1125*m.x1064 <= 0)

m.c362 = Constraint(expr=534*m.x1126*m.b1005 - 534*m.b1005*m.x1065 + m.x1126*m.x1065 <= 0)

m.c363 = Constraint(expr=425*m.x1127*m.b1006 - 425*m.b1006*m.x1066 + m.x1127*m.x1066 <= 0)

m.c364 = Constraint(expr=263*m.x1128*m.b1007 - 263*m.b1007*m.x1067 + m.x1128*m.x1067 <= 0)

m.c365 = Constraint(expr=160*m.x1129*m.b1008 - 160*m.b1008*m.x1068 + m.x1129*m.x1068 <= 0)

m.c366 = Constraint(expr=511*m.x1130*m.b1009 - 511*m.b1009*m.x1069 + m.x1130*m.x1069 <= 0)

m.c367 = Constraint(expr=421*m.x1131*m.b1010 - 421*m.b1010*m.x1070 + m.x1131*m.x1070 <= 0)

m.c368 = Constraint(expr=497*m.x1132*m.b1011 - 497*m.b1011*m.x1071 + m.x1132*m.x1071 <= 0)

m.c369 = Constraint(expr=245*m.x1133*m.b1012 - 245*m.b1012*m.x1072 + m.x1133*m.x1072 <= 0)

m.c370 = Constraint(expr=305*m.x1134*m.b1013 - 305*m.b1013*m.x1073 + m.x1134*m.x1073 <= 0)

m.c371 = Constraint(expr=194*m.x1135*m.b1014 - 194*m.b1014*m.x1074 + m.x1135*m.x1074 <= 0)

m.c372 = Constraint(expr=425*m.x1136*m.b1015 - 425*m.b1015*m.x1075 + m.x1136*m.x1075 <= 0)

m.c373 = Constraint(expr=497*m.x1137*m.b1016 - 497*m.b1016*m.x1076 + m.x1137*m.x1076 <= 0)

m.c374 = Constraint(expr=552*m.x1138*m.b1017 - 552*m.b1017*m.x1077 + m.x1138*m.x1077 <= 0)

m.c375 = Constraint(expr=164*m.x1139*m.b1018 - 164*m.b1018*m.x1078 + m.x1139*m.x1078 <= 0)

m.c376 = Constraint(expr=338*m.x1140*m.b1019 - 338*m.b1019*m.x1079 + m.x1140*m.x1079 <= 0)

m.c377 = Constraint(expr=552*m.x1141*m.b1020 - 552*m.b1020*m.x1080 + m.x1141*m.x1080 <= 0)

m.c378 = Constraint(expr=   m.x1021 + m.x1022 + m.x1023 + m.x1024 + m.x1025 + m.x1026 + m.x1027 + m.x1028 + m.x1029
                          + m.x1030 + m.x1031 + m.x1032 + m.x1033 + m.x1034 + m.x1035 + m.x1036 + m.x1037 + m.x1038
                          + m.x1039 + m.x1040 + m.x1041 + m.x1042 + m.x1043 + m.x1044 + m.x1045 + m.x1046 + m.x1047
                          + m.x1048 + m.x1049 + m.x1050 + m.x1051 + m.x1052 + m.x1053 + m.x1054 + m.x1055 + m.x1056
                          + m.x1057 + m.x1058 + m.x1059 + m.x1060 + m.x1061 + m.x1062 + m.x1063 + m.x1064 + m.x1065
                          + m.x1066 + m.x1067 + m.x1068 + m.x1069 + m.x1070 + m.x1071 + m.x1072 + m.x1073 + m.x1074
                          + m.x1075 + m.x1076 + m.x1077 + m.x1078 + m.x1079 + m.x1080 <= 14012)

m.c379 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13
                          + m.x14 + m.x15 + m.x16 - 137*m.b961 <= 0)

m.c380 = Constraint(expr=   m.x17 + m.x18 + m.x19 + m.x20 + m.x21 + m.x22 + m.x23 + m.x24 + m.x25 + m.x26 + m.x27
                          + m.x28 + m.x29 + m.x30 + m.x31 + m.x32 - 505*m.b962 <= 0)

m.c381 = Constraint(expr=   m.x33 + m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 + m.x42 + m.x43
                          + m.x44 + m.x45 + m.x46 + m.x47 + m.x48 - 427*m.b963 <= 0)

m.c382 = Constraint(expr=   m.x49 + m.x50 + m.x51 + m.x52 + m.x53 + m.x54 + m.x55 + m.x56 + m.x57 + m.x58 + m.x59
                          + m.x60 + m.x61 + m.x62 + m.x63 + m.x64 - 559*m.b964 <= 0)

m.c383 = Constraint(expr=   m.x65 + m.x66 + m.x67 + m.x68 + m.x69 + m.x70 + m.x71 + m.x72 + m.x73 + m.x74 + m.x75
                          + m.x76 + m.x77 + m.x78 + m.x79 + m.x80 - 137*m.b965 <= 0)

m.c384 = Constraint(expr=   m.x81 + m.x82 + m.x83 + m.x84 + m.x85 + m.x86 + m.x87 + m.x88 + m.x89 + m.x90 + m.x91
                          + m.x92 + m.x93 + m.x94 + m.x95 + m.x96 - 196*m.b966 <= 0)

m.c385 = Constraint(expr=   m.x97 + m.x98 + m.x99 + m.x100 + m.x101 + m.x102 + m.x103 + m.x104 + m.x105 + m.x106
                          + m.x107 + m.x108 + m.x109 + m.x110 + m.x111 + m.x112 - 341*m.b967 <= 0)

m.c386 = Constraint(expr=   m.x113 + m.x114 + m.x115 + m.x116 + m.x117 + m.x118 + m.x119 + m.x120 + m.x121 + m.x122
                          + m.x123 + m.x124 + m.x125 + m.x126 + m.x127 + m.x128 - 263*m.b968 <= 0)

m.c387 = Constraint(expr=   m.x129 + m.x130 + m.x131 + m.x132 + m.x133 + m.x134 + m.x135 + m.x136 + m.x137 + m.x138
                          + m.x139 + m.x140 + m.x141 + m.x142 + m.x143 + m.x144 - 245*m.b969 <= 0)

m.c388 = Constraint(expr=   m.x145 + m.x146 + m.x147 + m.x148 + m.x149 + m.x150 + m.x151 + m.x152 + m.x153 + m.x154
                          + m.x155 + m.x156 + m.x157 + m.x158 + m.x159 + m.x160 - 196*m.b970 <= 0)

m.c389 = Constraint(expr=   m.x161 + m.x162 + m.x163 + m.x164 + m.x165 + m.x166 + m.x167 + m.x168 + m.x169 + m.x170
                          + m.x171 + m.x172 + m.x173 + m.x174 + m.x175 + m.x176 - 346*m.b971 <= 0)

m.c390 = Constraint(expr=   m.x177 + m.x178 + m.x179 + m.x180 + m.x181 + m.x182 + m.x183 + m.x184 + m.x185 + m.x186
                          + m.x187 + m.x188 + m.x189 + m.x190 + m.x191 + m.x192 - 361*m.b972 <= 0)

m.c391 = Constraint(expr=   m.x193 + m.x194 + m.x195 + m.x196 + m.x197 + m.x198 + m.x199 + m.x200 + m.x201 + m.x202
                          + m.x203 + m.x204 + m.x205 + m.x206 + m.x207 + m.x208 - 179*m.b973 <= 0)

m.c392 = Constraint(expr=   m.x209 + m.x210 + m.x211 + m.x212 + m.x213 + m.x214 + m.x215 + m.x216 + m.x217 + m.x218
                          + m.x219 + m.x220 + m.x221 + m.x222 + m.x223 + m.x224 - 505*m.b974 <= 0)

m.c393 = Constraint(expr=   m.x225 + m.x226 + m.x227 + m.x228 + m.x229 + m.x230 + m.x231 + m.x232 + m.x233 + m.x234
                          + m.x235 + m.x236 + m.x237 + m.x238 + m.x239 + m.x240 - 341*m.b975 <= 0)

m.c394 = Constraint(expr=   m.x241 + m.x242 + m.x243 + m.x244 + m.x245 + m.x246 + m.x247 + m.x248 + m.x249 + m.x250
                          + m.x251 + m.x252 + m.x253 + m.x254 + m.x255 + m.x256 - 160*m.b976 <= 0)

m.c395 = Constraint(expr=   m.x257 + m.x258 + m.x259 + m.x260 + m.x261 + m.x262 + m.x263 + m.x264 + m.x265 + m.x266
                          + m.x267 + m.x268 + m.x269 + m.x270 + m.x271 + m.x272 - 389*m.b977 <= 0)

m.c396 = Constraint(expr=   m.x273 + m.x274 + m.x275 + m.x276 + m.x277 + m.x278 + m.x279 + m.x280 + m.x281 + m.x282
                          + m.x283 + m.x284 + m.x285 + m.x286 + m.x287 + m.x288 - 153*m.b978 <= 0)

m.c397 = Constraint(expr=   m.x289 + m.x290 + m.x291 + m.x292 + m.x293 + m.x294 + m.x295 + m.x296 + m.x297 + m.x298
                          + m.x299 + m.x300 + m.x301 + m.x302 + m.x303 + m.x304 - 164*m.b979 <= 0)

m.c398 = Constraint(expr=   m.x305 + m.x306 + m.x307 + m.x308 + m.x309 + m.x310 + m.x311 + m.x312 + m.x313 + m.x314
                          + m.x315 + m.x316 + m.x317 + m.x318 + m.x319 + m.x320 - 427*m.b980 <= 0)

m.c399 = Constraint(expr=   m.x321 + m.x322 + m.x323 + m.x324 + m.x325 + m.x326 + m.x327 + m.x328 + m.x329 + m.x330
                          + m.x331 + m.x332 + m.x333 + m.x334 + m.x335 + m.x336 - 389*m.b981 <= 0)

m.c400 = Constraint(expr=   m.x337 + m.x338 + m.x339 + m.x340 + m.x341 + m.x342 + m.x343 + m.x344 + m.x345 + m.x346
                          + m.x347 + m.x348 + m.x349 + m.x350 + m.x351 + m.x352 - 513*m.b982 <= 0)

m.c401 = Constraint(expr=   m.x353 + m.x354 + m.x355 + m.x356 + m.x357 + m.x358 + m.x359 + m.x360 + m.x361 + m.x362
                          + m.x363 + m.x364 + m.x365 + m.x366 + m.x367 + m.x368 - 353*m.b983 <= 0)

m.c402 = Constraint(expr=   m.x369 + m.x370 + m.x371 + m.x372 + m.x373 + m.x374 + m.x375 + m.x376 + m.x377 + m.x378
                          + m.x379 + m.x380 + m.x381 + m.x382 + m.x383 + m.x384 - 305*m.b984 <= 0)

m.c403 = Constraint(expr=   m.x385 + m.x386 + m.x387 + m.x388 + m.x389 + m.x390 + m.x391 + m.x392 + m.x393 + m.x394
                          + m.x395 + m.x396 + m.x397 + m.x398 + m.x399 + m.x400 - 346*m.b985 <= 0)

m.c404 = Constraint(expr=   m.x401 + m.x402 + m.x403 + m.x404 + m.x405 + m.x406 + m.x407 + m.x408 + m.x409 + m.x410
                          + m.x411 + m.x412 + m.x413 + m.x414 + m.x415 + m.x416 - 463*m.b986 <= 0)

m.c405 = Constraint(expr=   m.x417 + m.x418 + m.x419 + m.x420 + m.x421 + m.x422 + m.x423 + m.x424 + m.x425 + m.x426
                          + m.x427 + m.x428 + m.x429 + m.x430 + m.x431 + m.x432 - 511*m.b987 <= 0)

m.c406 = Constraint(expr=   m.x433 + m.x434 + m.x435 + m.x436 + m.x437 + m.x438 + m.x439 + m.x440 + m.x441 + m.x442
                          + m.x443 + m.x444 + m.x445 + m.x446 + m.x447 + m.x448 - 361*m.b988 <= 0)

m.c407 = Constraint(expr=   m.x449 + m.x450 + m.x451 + m.x452 + m.x453 + m.x454 + m.x455 + m.x456 + m.x457 + m.x458
                          + m.x459 + m.x460 + m.x461 + m.x462 + m.x463 + m.x464 - 513*m.b989 <= 0)

m.c408 = Constraint(expr=   m.x465 + m.x466 + m.x467 + m.x468 + m.x469 + m.x470 + m.x471 + m.x472 + m.x473 + m.x474
                          + m.x475 + m.x476 + m.x477 + m.x478 + m.x479 + m.x480 - 218*m.b990 <= 0)

m.c409 = Constraint(expr=   m.x481 + m.x482 + m.x483 + m.x484 + m.x485 + m.x486 + m.x487 + m.x488 + m.x489 + m.x490
                          + m.x491 + m.x492 + m.x493 + m.x494 + m.x495 + m.x496 - 338*m.b991 <= 0)

m.c410 = Constraint(expr=   m.x497 + m.x498 + m.x499 + m.x500 + m.x501 + m.x502 + m.x503 + m.x504 + m.x505 + m.x506
                          + m.x507 + m.x508 + m.x509 + m.x510 + m.x511 + m.x512 - 153*m.b992 <= 0)

m.c411 = Constraint(expr=   m.x513 + m.x514 + m.x515 + m.x516 + m.x517 + m.x518 + m.x519 + m.x520 + m.x521 + m.x522
                          + m.x523 + m.x524 + m.x525 + m.x526 + m.x527 + m.x528 - 439*m.b993 <= 0)

m.c412 = Constraint(expr=   m.x529 + m.x530 + m.x531 + m.x532 + m.x533 + m.x534 + m.x535 + m.x536 + m.x537 + m.x538
                          + m.x539 + m.x540 + m.x541 + m.x542 + m.x543 + m.x544 - 194*m.b994 <= 0)

m.c413 = Constraint(expr=   m.x545 + m.x546 + m.x547 + m.x548 + m.x549 + m.x550 + m.x551 + m.x552 + m.x553 + m.x554
                          + m.x555 + m.x556 + m.x557 + m.x558 + m.x559 + m.x560 - 353*m.b995 <= 0)

m.c414 = Constraint(expr=   m.x561 + m.x562 + m.x563 + m.x564 + m.x565 + m.x566 + m.x567 + m.x568 + m.x569 + m.x570
                          + m.x571 + m.x572 + m.x573 + m.x574 + m.x575 + m.x576 - 415*m.b996 <= 0)

m.c415 = Constraint(expr=   m.x577 + m.x578 + m.x579 + m.x580 + m.x581 + m.x582 + m.x583 + m.x584 + m.x585 + m.x586
                          + m.x587 + m.x588 + m.x589 + m.x590 + m.x591 + m.x592 - 559*m.b997 <= 0)

m.c416 = Constraint(expr=   m.x593 + m.x594 + m.x595 + m.x596 + m.x597 + m.x598 + m.x599 + m.x600 + m.x601 + m.x602
                          + m.x603 + m.x604 + m.x605 + m.x606 + m.x607 + m.x608 - 439*m.b998 <= 0)

m.c417 = Constraint(expr=   m.x609 + m.x610 + m.x611 + m.x612 + m.x613 + m.x614 + m.x615 + m.x616 + m.x617 + m.x618
                          + m.x619 + m.x620 + m.x621 + m.x622 + m.x623 + m.x624 - 415*m.b999 <= 0)

m.c418 = Constraint(expr=   m.x625 + m.x626 + m.x627 + m.x628 + m.x629 + m.x630 + m.x631 + m.x632 + m.x633 + m.x634
                          + m.x635 + m.x636 + m.x637 + m.x638 + m.x639 + m.x640 - 421*m.b1000 <= 0)

m.c419 = Constraint(expr=   m.x641 + m.x642 + m.x643 + m.x644 + m.x645 + m.x646 + m.x647 + m.x648 + m.x649 + m.x650
                          + m.x651 + m.x652 + m.x653 + m.x654 + m.x655 + m.x656 - 179*m.b1001 <= 0)

m.c420 = Constraint(expr=   m.x657 + m.x658 + m.x659 + m.x660 + m.x661 + m.x662 + m.x663 + m.x664 + m.x665 + m.x666
                          + m.x667 + m.x668 + m.x669 + m.x670 + m.x671 + m.x672 - 463*m.b1002 <= 0)

m.c421 = Constraint(expr=   m.x673 + m.x674 + m.x675 + m.x676 + m.x677 + m.x678 + m.x679 + m.x680 + m.x681 + m.x682
                          + m.x683 + m.x684 + m.x685 + m.x686 + m.x687 + m.x688 - 534*m.b1003 <= 0)

m.c422 = Constraint(expr=   m.x689 + m.x690 + m.x691 + m.x692 + m.x693 + m.x694 + m.x695 + m.x696 + m.x697 + m.x698
                          + m.x699 + m.x700 + m.x701 + m.x702 + m.x703 + m.x704 - 218*m.b1004 <= 0)

m.c423 = Constraint(expr=   m.x705 + m.x706 + m.x707 + m.x708 + m.x709 + m.x710 + m.x711 + m.x712 + m.x713 + m.x714
                          + m.x715 + m.x716 + m.x717 + m.x718 + m.x719 + m.x720 - 534*m.b1005 <= 0)

m.c424 = Constraint(expr=   m.x721 + m.x722 + m.x723 + m.x724 + m.x725 + m.x726 + m.x727 + m.x728 + m.x729 + m.x730
                          + m.x731 + m.x732 + m.x733 + m.x734 + m.x735 + m.x736 - 425*m.b1006 <= 0)

m.c425 = Constraint(expr=   m.x737 + m.x738 + m.x739 + m.x740 + m.x741 + m.x742 + m.x743 + m.x744 + m.x745 + m.x746
                          + m.x747 + m.x748 + m.x749 + m.x750 + m.x751 + m.x752 - 263*m.b1007 <= 0)

m.c426 = Constraint(expr=   m.x753 + m.x754 + m.x755 + m.x756 + m.x757 + m.x758 + m.x759 + m.x760 + m.x761 + m.x762
                          + m.x763 + m.x764 + m.x765 + m.x766 + m.x767 + m.x768 - 160*m.b1008 <= 0)

m.c427 = Constraint(expr=   m.x769 + m.x770 + m.x771 + m.x772 + m.x773 + m.x774 + m.x775 + m.x776 + m.x777 + m.x778
                          + m.x779 + m.x780 + m.x781 + m.x782 + m.x783 + m.x784 - 511*m.b1009 <= 0)

m.c428 = Constraint(expr=   m.x785 + m.x786 + m.x787 + m.x788 + m.x789 + m.x790 + m.x791 + m.x792 + m.x793 + m.x794
                          + m.x795 + m.x796 + m.x797 + m.x798 + m.x799 + m.x800 - 421*m.b1010 <= 0)

m.c429 = Constraint(expr=   m.x801 + m.x802 + m.x803 + m.x804 + m.x805 + m.x806 + m.x807 + m.x808 + m.x809 + m.x810
                          + m.x811 + m.x812 + m.x813 + m.x814 + m.x815 + m.x816 - 497*m.b1011 <= 0)

m.c430 = Constraint(expr=   m.x817 + m.x818 + m.x819 + m.x820 + m.x821 + m.x822 + m.x823 + m.x824 + m.x825 + m.x826
                          + m.x827 + m.x828 + m.x829 + m.x830 + m.x831 + m.x832 - 245*m.b1012 <= 0)

m.c431 = Constraint(expr=   m.x833 + m.x834 + m.x835 + m.x836 + m.x837 + m.x838 + m.x839 + m.x840 + m.x841 + m.x842
                          + m.x843 + m.x844 + m.x845 + m.x846 + m.x847 + m.x848 - 305*m.b1013 <= 0)

m.c432 = Constraint(expr=   m.x849 + m.x850 + m.x851 + m.x852 + m.x853 + m.x854 + m.x855 + m.x856 + m.x857 + m.x858
                          + m.x859 + m.x860 + m.x861 + m.x862 + m.x863 + m.x864 - 194*m.b1014 <= 0)

m.c433 = Constraint(expr=   m.x865 + m.x866 + m.x867 + m.x868 + m.x869 + m.x870 + m.x871 + m.x872 + m.x873 + m.x874
                          + m.x875 + m.x876 + m.x877 + m.x878 + m.x879 + m.x880 - 425*m.b1015 <= 0)

m.c434 = Constraint(expr=   m.x881 + m.x882 + m.x883 + m.x884 + m.x885 + m.x886 + m.x887 + m.x888 + m.x889 + m.x890
                          + m.x891 + m.x892 + m.x893 + m.x894 + m.x895 + m.x896 - 497*m.b1016 <= 0)

m.c435 = Constraint(expr=   m.x897 + m.x898 + m.x899 + m.x900 + m.x901 + m.x902 + m.x903 + m.x904 + m.x905 + m.x906
                          + m.x907 + m.x908 + m.x909 + m.x910 + m.x911 + m.x912 - 552*m.b1017 <= 0)

m.c436 = Constraint(expr=   m.x913 + m.x914 + m.x915 + m.x916 + m.x917 + m.x918 + m.x919 + m.x920 + m.x921 + m.x922
                          + m.x923 + m.x924 + m.x925 + m.x926 + m.x927 + m.x928 - 164*m.b1018 <= 0)

m.c437 = Constraint(expr=   m.x929 + m.x930 + m.x931 + m.x932 + m.x933 + m.x934 + m.x935 + m.x936 + m.x937 + m.x938
                          + m.x939 + m.x940 + m.x941 + m.x942 + m.x943 + m.x944 - 338*m.b1019 <= 0)

m.c438 = Constraint(expr=   m.x945 + m.x946 + m.x947 + m.x948 + m.x949 + m.x950 + m.x951 + m.x952 + m.x953 + m.x954
                          + m.x955 + m.x956 + m.x957 + m.x958 + m.x959 + m.x960 - 552*m.b1020 <= 0)
