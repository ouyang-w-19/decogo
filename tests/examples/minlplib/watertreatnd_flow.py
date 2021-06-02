#  MINLP written by GAMS Convert at 04/21/18 13:55:19
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        380      366        5        9        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        421      416        5        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1175      870      305        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


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
m.x307 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x309 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x311 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x312 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x313 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x314 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x315 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x316 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x317 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x318 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x319 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x320 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x321 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x322 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x323 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x324 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x325 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x326 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x327 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x328 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x329 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x330 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x331 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x332 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x333 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x334 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x335 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x336 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x337 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x338 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x339 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x340 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x341 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x342 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x343 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x344 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x345 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x346 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x347 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x348 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x349 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x350 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x351 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x352 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x353 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x354 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x355 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x356 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x357 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x358 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x359 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x360 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x361 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x362 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x363 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x364 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x365 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x366 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x367 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x368 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x369 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x370 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x371 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x372 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x373 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x374 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x375 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x376 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x377 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x378 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x379 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x380 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x381 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x382 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x383 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x384 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x385 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x386 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x387 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x388 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x389 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x390 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x391 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x392 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x393 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x394 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x395 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x396 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x397 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x398 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x399 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x400 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x401 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x402 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x403 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x404 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x405 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x406 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x407 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x408 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x409 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x410 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x411 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x412 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x413 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x414 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x415 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x416 = Var(within=Reals,bounds=(0,40),initialize=0)
m.b417 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b418 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b419 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b420 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b421 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   m.x2 + m.x3 + m.x4 + m.x5 + m.x6, sense=minimize)

m.c2 = Constraint(expr= - m.x7 + m.x307 == 0)

m.c3 = Constraint(expr= - m.x8 + m.x308 == 0)

m.c4 = Constraint(expr= - m.x9 + m.x309 == 0)

m.c5 = Constraint(expr= - m.x10 + m.x310 == 0)

m.c6 = Constraint(expr= - m.x11 + m.x311 == 0)

m.c7 = Constraint(expr= - m.x12 + m.x312 == 0)

m.c8 = Constraint(expr= - m.x13 + m.x307 == 0)

m.c9 = Constraint(expr= - m.x14 + m.x308 == 0)

m.c10 = Constraint(expr= - m.x15 + m.x309 == 0)

m.c11 = Constraint(expr= - m.x16 + m.x310 == 0)

m.c12 = Constraint(expr= - m.x17 + m.x311 == 0)

m.c13 = Constraint(expr= - m.x18 + m.x312 == 0)

m.c14 = Constraint(expr= - m.x19 + m.x307 == 0)

m.c15 = Constraint(expr= - m.x20 + m.x308 == 0)

m.c16 = Constraint(expr= - m.x21 + m.x309 == 0)

m.c17 = Constraint(expr= - m.x22 + m.x310 == 0)

m.c18 = Constraint(expr= - m.x23 + m.x311 == 0)

m.c19 = Constraint(expr= - m.x24 + m.x312 == 0)

m.c20 = Constraint(expr= - m.x25 + m.x307 == 0)

m.c21 = Constraint(expr= - m.x26 + m.x308 == 0)

m.c22 = Constraint(expr= - m.x27 + m.x309 == 0)

m.c23 = Constraint(expr= - m.x28 + m.x310 == 0)

m.c24 = Constraint(expr= - m.x29 + m.x311 == 0)

m.c25 = Constraint(expr= - m.x30 + m.x312 == 0)

m.c26 = Constraint(expr= - m.x31 + 10*m.x307 == 0)

m.c27 = Constraint(expr= - m.x32 + 10*m.x308 == 0)

m.c28 = Constraint(expr= - m.x33 + 10*m.x309 == 0)

m.c29 = Constraint(expr= - m.x34 + 10*m.x310 == 0)

m.c30 = Constraint(expr= - m.x35 + 10*m.x311 == 0)

m.c31 = Constraint(expr= - m.x36 + 10*m.x312 == 0)

m.c32 = Constraint(expr= - m.x37 + 2*m.x313 == 0)

m.c33 = Constraint(expr= - m.x38 + 2*m.x314 == 0)

m.c34 = Constraint(expr= - m.x39 + 2*m.x315 == 0)

m.c35 = Constraint(expr= - m.x40 + 2*m.x316 == 0)

m.c36 = Constraint(expr= - m.x41 + 2*m.x317 == 0)

m.c37 = Constraint(expr= - m.x42 + 2*m.x318 == 0)

m.c38 = Constraint(expr= - m.x43 == 0)

m.c39 = Constraint(expr= - m.x44 == 0)

m.c40 = Constraint(expr= - m.x45 == 0)

m.c41 = Constraint(expr= - m.x46 == 0)

m.c42 = Constraint(expr= - m.x47 == 0)

m.c43 = Constraint(expr= - m.x48 == 0)

m.c44 = Constraint(expr= - m.x49 == 0)

m.c45 = Constraint(expr= - m.x50 == 0)

m.c46 = Constraint(expr= - m.x51 == 0)

m.c47 = Constraint(expr= - m.x52 == 0)

m.c48 = Constraint(expr= - m.x53 == 0)

m.c49 = Constraint(expr= - m.x54 == 0)

m.c50 = Constraint(expr= - m.x55 + m.x313 == 0)

m.c51 = Constraint(expr= - m.x56 + m.x314 == 0)

m.c52 = Constraint(expr= - m.x57 + m.x315 == 0)

m.c53 = Constraint(expr= - m.x58 + m.x316 == 0)

m.c54 = Constraint(expr= - m.x59 + m.x317 == 0)

m.c55 = Constraint(expr= - m.x60 + m.x318 == 0)

m.c56 = Constraint(expr= - m.x61 + 15*m.x313 == 0)

m.c57 = Constraint(expr= - m.x62 + 15*m.x314 == 0)

m.c58 = Constraint(expr= - m.x63 + 15*m.x315 == 0)

m.c59 = Constraint(expr= - m.x64 + 15*m.x316 == 0)

m.c60 = Constraint(expr= - m.x65 + 15*m.x317 == 0)

m.c61 = Constraint(expr= - m.x66 + 15*m.x318 == 0)

m.c62 = Constraint(expr= - m.x67 + m.x319 == 0)

m.c63 = Constraint(expr= - m.x68 + m.x320 == 0)

m.c64 = Constraint(expr= - m.x69 + m.x321 == 0)

m.c65 = Constraint(expr= - m.x70 + m.x322 == 0)

m.c66 = Constraint(expr= - m.x71 + m.x323 == 0)

m.c67 = Constraint(expr= - m.x72 + m.x324 == 0)

m.c68 = Constraint(expr= - m.x73 == 0)

m.c69 = Constraint(expr= - m.x74 == 0)

m.c70 = Constraint(expr= - m.x75 == 0)

m.c71 = Constraint(expr= - m.x76 == 0)

m.c72 = Constraint(expr= - m.x77 == 0)

m.c73 = Constraint(expr= - m.x78 == 0)

m.c74 = Constraint(expr= - m.x79 + m.x319 == 0)

m.c75 = Constraint(expr= - m.x80 + m.x320 == 0)

m.c76 = Constraint(expr= - m.x81 + m.x321 == 0)

m.c77 = Constraint(expr= - m.x82 + m.x322 == 0)

m.c78 = Constraint(expr= - m.x83 + m.x323 == 0)

m.c79 = Constraint(expr= - m.x84 + m.x324 == 0)

m.c80 = Constraint(expr= - m.x85 + 2*m.x319 == 0)

m.c81 = Constraint(expr= - m.x86 + 2*m.x320 == 0)

m.c82 = Constraint(expr= - m.x87 + 2*m.x321 == 0)

m.c83 = Constraint(expr= - m.x88 + 2*m.x322 == 0)

m.c84 = Constraint(expr= - m.x89 + 2*m.x323 == 0)

m.c85 = Constraint(expr= - m.x90 + 2*m.x324 == 0)

m.c86 = Constraint(expr= - m.x91 + 5*m.x319 == 0)

m.c87 = Constraint(expr= - m.x92 + 5*m.x320 == 0)

m.c88 = Constraint(expr= - m.x93 + 5*m.x321 == 0)

m.c89 = Constraint(expr= - m.x94 + 5*m.x322 == 0)

m.c90 = Constraint(expr= - m.x95 + 5*m.x323 == 0)

m.c91 = Constraint(expr= - m.x96 + 5*m.x324 == 0)

m.c92 = Constraint(expr= - m.x97 + 3*m.x325 == 0)

m.c93 = Constraint(expr= - m.x98 + 3*m.x326 == 0)

m.c94 = Constraint(expr= - m.x99 + 3*m.x327 == 0)

m.c95 = Constraint(expr= - m.x100 + 3*m.x328 == 0)

m.c96 = Constraint(expr= - m.x101 + 3*m.x329 == 0)

m.c97 = Constraint(expr= - m.x102 + 3*m.x330 == 0)

m.c98 = Constraint(expr= - m.x103 + m.x325 == 0)

m.c99 = Constraint(expr= - m.x104 + m.x326 == 0)

m.c100 = Constraint(expr= - m.x105 + m.x327 == 0)

m.c101 = Constraint(expr= - m.x106 + m.x328 == 0)

m.c102 = Constraint(expr= - m.x107 + m.x329 == 0)

m.c103 = Constraint(expr= - m.x108 + m.x330 == 0)

m.c104 = Constraint(expr= - m.x109 + m.x325 == 0)

m.c105 = Constraint(expr= - m.x110 + m.x326 == 0)

m.c106 = Constraint(expr= - m.x111 + m.x327 == 0)

m.c107 = Constraint(expr= - m.x112 + m.x328 == 0)

m.c108 = Constraint(expr= - m.x113 + m.x329 == 0)

m.c109 = Constraint(expr= - m.x114 + m.x330 == 0)

m.c110 = Constraint(expr= - m.x115 == 0)

m.c111 = Constraint(expr= - m.x116 == 0)

m.c112 = Constraint(expr= - m.x117 == 0)

m.c113 = Constraint(expr= - m.x118 == 0)

m.c114 = Constraint(expr= - m.x119 == 0)

m.c115 = Constraint(expr= - m.x120 == 0)

m.c116 = Constraint(expr= - m.x121 + 20*m.x325 == 0)

m.c117 = Constraint(expr= - m.x122 + 20*m.x326 == 0)

m.c118 = Constraint(expr= - m.x123 + 20*m.x327 == 0)

m.c119 = Constraint(expr= - m.x124 + 20*m.x328 == 0)

m.c120 = Constraint(expr= - m.x125 + 20*m.x329 == 0)

m.c121 = Constraint(expr= - m.x126 + 20*m.x330 == 0)

m.c122 = Constraint(expr= - m.x127 + 2*m.x331 == 0)

m.c123 = Constraint(expr= - m.x128 + 2*m.x332 == 0)

m.c124 = Constraint(expr= - m.x129 + 2*m.x333 == 0)

m.c125 = Constraint(expr= - m.x130 + 2*m.x334 == 0)

m.c126 = Constraint(expr= - m.x131 + 2*m.x335 == 0)

m.c127 = Constraint(expr= - m.x132 + 2*m.x336 == 0)

m.c128 = Constraint(expr= - m.x133 + 2*m.x331 == 0)

m.c129 = Constraint(expr= - m.x134 + 2*m.x332 == 0)

m.c130 = Constraint(expr= - m.x135 + 2*m.x333 == 0)

m.c131 = Constraint(expr= - m.x136 + 2*m.x334 == 0)

m.c132 = Constraint(expr= - m.x137 + 2*m.x335 == 0)

m.c133 = Constraint(expr= - m.x138 + 2*m.x336 == 0)

m.c134 = Constraint(expr= - m.x139 == 0)

m.c135 = Constraint(expr= - m.x140 == 0)

m.c136 = Constraint(expr= - m.x141 == 0)

m.c137 = Constraint(expr= - m.x142 == 0)

m.c138 = Constraint(expr= - m.x143 == 0)

m.c139 = Constraint(expr= - m.x144 == 0)

m.c140 = Constraint(expr= - m.x145 == 0)

m.c141 = Constraint(expr= - m.x146 == 0)

m.c142 = Constraint(expr= - m.x147 == 0)

m.c143 = Constraint(expr= - m.x148 == 0)

m.c144 = Constraint(expr= - m.x149 == 0)

m.c145 = Constraint(expr= - m.x150 == 0)

m.c146 = Constraint(expr= - m.x151 + 10*m.x331 == 0)

m.c147 = Constraint(expr= - m.x152 + 10*m.x332 == 0)

m.c148 = Constraint(expr= - m.x153 + 10*m.x333 == 0)

m.c149 = Constraint(expr= - m.x154 + 10*m.x334 == 0)

m.c150 = Constraint(expr= - m.x155 + 10*m.x335 == 0)

m.c151 = Constraint(expr= - m.x156 + 10*m.x336 == 0)

m.c152 = Constraint(expr=m.x337*m.x367 - m.x157 == 0)

m.c153 = Constraint(expr=m.x338*m.x367 - m.x158 == 0)

m.c154 = Constraint(expr=m.x339*m.x367 - m.x159 == 0)

m.c155 = Constraint(expr=m.x340*m.x367 - m.x160 == 0)

m.c156 = Constraint(expr=m.x341*m.x367 - m.x161 == 0)

m.c157 = Constraint(expr=m.x342*m.x367 - m.x162 == 0)

m.c158 = Constraint(expr=m.x337*m.x368 - m.x163 == 0)

m.c159 = Constraint(expr=m.x338*m.x368 - m.x164 == 0)

m.c160 = Constraint(expr=m.x339*m.x368 - m.x165 == 0)

m.c161 = Constraint(expr=m.x340*m.x368 - m.x166 == 0)

m.c162 = Constraint(expr=m.x341*m.x368 - m.x167 == 0)

m.c163 = Constraint(expr=m.x342*m.x368 - m.x168 == 0)

m.c164 = Constraint(expr=m.x337*m.x369 - m.x169 == 0)

m.c165 = Constraint(expr=m.x338*m.x369 - m.x170 == 0)

m.c166 = Constraint(expr=m.x339*m.x369 - m.x171 == 0)

m.c167 = Constraint(expr=m.x340*m.x369 - m.x172 == 0)

m.c168 = Constraint(expr=m.x341*m.x369 - m.x173 == 0)

m.c169 = Constraint(expr=m.x342*m.x369 - m.x174 == 0)

m.c170 = Constraint(expr=m.x337*m.x370 - m.x175 == 0)

m.c171 = Constraint(expr=m.x338*m.x370 - m.x176 == 0)

m.c172 = Constraint(expr=m.x339*m.x370 - m.x177 == 0)

m.c173 = Constraint(expr=m.x340*m.x370 - m.x178 == 0)

m.c174 = Constraint(expr=m.x341*m.x370 - m.x179 == 0)

m.c175 = Constraint(expr=m.x342*m.x370 - m.x180 == 0)

m.c176 = Constraint(expr=m.x337*m.x371 - m.x181 == 0)

m.c177 = Constraint(expr=m.x338*m.x371 - m.x182 == 0)

m.c178 = Constraint(expr=m.x339*m.x371 - m.x183 == 0)

m.c179 = Constraint(expr=m.x340*m.x371 - m.x184 == 0)

m.c180 = Constraint(expr=m.x341*m.x371 - m.x185 == 0)

m.c181 = Constraint(expr=m.x342*m.x371 - m.x186 == 0)

m.c182 = Constraint(expr=m.x343*m.x372 - m.x187 == 0)

m.c183 = Constraint(expr=m.x344*m.x372 - m.x188 == 0)

m.c184 = Constraint(expr=m.x345*m.x372 - m.x189 == 0)

m.c185 = Constraint(expr=m.x346*m.x372 - m.x190 == 0)

m.c186 = Constraint(expr=m.x347*m.x372 - m.x191 == 0)

m.c187 = Constraint(expr=m.x348*m.x372 - m.x192 == 0)

m.c188 = Constraint(expr=m.x343*m.x373 - m.x193 == 0)

m.c189 = Constraint(expr=m.x344*m.x373 - m.x194 == 0)

m.c190 = Constraint(expr=m.x345*m.x373 - m.x195 == 0)

m.c191 = Constraint(expr=m.x346*m.x373 - m.x196 == 0)

m.c192 = Constraint(expr=m.x347*m.x373 - m.x197 == 0)

m.c193 = Constraint(expr=m.x348*m.x373 - m.x198 == 0)

m.c194 = Constraint(expr=m.x343*m.x374 - m.x199 == 0)

m.c195 = Constraint(expr=m.x344*m.x374 - m.x200 == 0)

m.c196 = Constraint(expr=m.x345*m.x374 - m.x201 == 0)

m.c197 = Constraint(expr=m.x346*m.x374 - m.x202 == 0)

m.c198 = Constraint(expr=m.x347*m.x374 - m.x203 == 0)

m.c199 = Constraint(expr=m.x348*m.x374 - m.x204 == 0)

m.c200 = Constraint(expr=m.x343*m.x375 - m.x205 == 0)

m.c201 = Constraint(expr=m.x344*m.x375 - m.x206 == 0)

m.c202 = Constraint(expr=m.x345*m.x375 - m.x207 == 0)

m.c203 = Constraint(expr=m.x346*m.x375 - m.x208 == 0)

m.c204 = Constraint(expr=m.x347*m.x375 - m.x209 == 0)

m.c205 = Constraint(expr=m.x348*m.x375 - m.x210 == 0)

m.c206 = Constraint(expr=m.x343*m.x376 - m.x211 == 0)

m.c207 = Constraint(expr=m.x344*m.x376 - m.x212 == 0)

m.c208 = Constraint(expr=m.x345*m.x376 - m.x213 == 0)

m.c209 = Constraint(expr=m.x346*m.x376 - m.x214 == 0)

m.c210 = Constraint(expr=m.x347*m.x376 - m.x215 == 0)

m.c211 = Constraint(expr=m.x348*m.x376 - m.x216 == 0)

m.c212 = Constraint(expr=m.x349*m.x377 - m.x217 == 0)

m.c213 = Constraint(expr=m.x350*m.x377 - m.x218 == 0)

m.c214 = Constraint(expr=m.x351*m.x377 - m.x219 == 0)

m.c215 = Constraint(expr=m.x352*m.x377 - m.x220 == 0)

m.c216 = Constraint(expr=m.x353*m.x377 - m.x221 == 0)

m.c217 = Constraint(expr=m.x354*m.x377 - m.x222 == 0)

m.c218 = Constraint(expr=m.x349*m.x378 - m.x223 == 0)

m.c219 = Constraint(expr=m.x350*m.x378 - m.x224 == 0)

m.c220 = Constraint(expr=m.x351*m.x378 - m.x225 == 0)

m.c221 = Constraint(expr=m.x352*m.x378 - m.x226 == 0)

m.c222 = Constraint(expr=m.x353*m.x378 - m.x227 == 0)

m.c223 = Constraint(expr=m.x354*m.x378 - m.x228 == 0)

m.c224 = Constraint(expr=m.x349*m.x379 - m.x229 == 0)

m.c225 = Constraint(expr=m.x350*m.x379 - m.x230 == 0)

m.c226 = Constraint(expr=m.x351*m.x379 - m.x231 == 0)

m.c227 = Constraint(expr=m.x352*m.x379 - m.x232 == 0)

m.c228 = Constraint(expr=m.x353*m.x379 - m.x233 == 0)

m.c229 = Constraint(expr=m.x354*m.x379 - m.x234 == 0)

m.c230 = Constraint(expr=m.x349*m.x380 - m.x235 == 0)

m.c231 = Constraint(expr=m.x350*m.x380 - m.x236 == 0)

m.c232 = Constraint(expr=m.x351*m.x380 - m.x237 == 0)

m.c233 = Constraint(expr=m.x352*m.x380 - m.x238 == 0)

m.c234 = Constraint(expr=m.x353*m.x380 - m.x239 == 0)

m.c235 = Constraint(expr=m.x354*m.x380 - m.x240 == 0)

m.c236 = Constraint(expr=m.x349*m.x381 - m.x241 == 0)

m.c237 = Constraint(expr=m.x350*m.x381 - m.x242 == 0)

m.c238 = Constraint(expr=m.x351*m.x381 - m.x243 == 0)

m.c239 = Constraint(expr=m.x352*m.x381 - m.x244 == 0)

m.c240 = Constraint(expr=m.x353*m.x381 - m.x245 == 0)

m.c241 = Constraint(expr=m.x354*m.x381 - m.x246 == 0)

m.c242 = Constraint(expr=m.x355*m.x382 - m.x247 == 0)

m.c243 = Constraint(expr=m.x356*m.x382 - m.x248 == 0)

m.c244 = Constraint(expr=m.x357*m.x382 - m.x249 == 0)

m.c245 = Constraint(expr=m.x358*m.x382 - m.x250 == 0)

m.c246 = Constraint(expr=m.x359*m.x382 - m.x251 == 0)

m.c247 = Constraint(expr=m.x360*m.x382 - m.x252 == 0)

m.c248 = Constraint(expr=m.x355*m.x383 - m.x253 == 0)

m.c249 = Constraint(expr=m.x356*m.x383 - m.x254 == 0)

m.c250 = Constraint(expr=m.x357*m.x383 - m.x255 == 0)

m.c251 = Constraint(expr=m.x358*m.x383 - m.x256 == 0)

m.c252 = Constraint(expr=m.x359*m.x383 - m.x257 == 0)

m.c253 = Constraint(expr=m.x360*m.x383 - m.x258 == 0)

m.c254 = Constraint(expr=m.x355*m.x384 - m.x259 == 0)

m.c255 = Constraint(expr=m.x356*m.x384 - m.x260 == 0)

m.c256 = Constraint(expr=m.x357*m.x384 - m.x261 == 0)

m.c257 = Constraint(expr=m.x358*m.x384 - m.x262 == 0)

m.c258 = Constraint(expr=m.x359*m.x384 - m.x263 == 0)

m.c259 = Constraint(expr=m.x360*m.x384 - m.x264 == 0)

m.c260 = Constraint(expr=m.x355*m.x385 - m.x265 == 0)

m.c261 = Constraint(expr=m.x356*m.x385 - m.x266 == 0)

m.c262 = Constraint(expr=m.x357*m.x385 - m.x267 == 0)

m.c263 = Constraint(expr=m.x358*m.x385 - m.x268 == 0)

m.c264 = Constraint(expr=m.x359*m.x385 - m.x269 == 0)

m.c265 = Constraint(expr=m.x360*m.x385 - m.x270 == 0)

m.c266 = Constraint(expr=m.x355*m.x386 - m.x271 == 0)

m.c267 = Constraint(expr=m.x356*m.x386 - m.x272 == 0)

m.c268 = Constraint(expr=m.x357*m.x386 - m.x273 == 0)

m.c269 = Constraint(expr=m.x358*m.x386 - m.x274 == 0)

m.c270 = Constraint(expr=m.x359*m.x386 - m.x275 == 0)

m.c271 = Constraint(expr=m.x360*m.x386 - m.x276 == 0)

m.c272 = Constraint(expr=m.x361*m.x387 - m.x277 == 0)

m.c273 = Constraint(expr=m.x362*m.x387 - m.x278 == 0)

m.c274 = Constraint(expr=m.x363*m.x387 - m.x279 == 0)

m.c275 = Constraint(expr=m.x364*m.x387 - m.x280 == 0)

m.c276 = Constraint(expr=m.x365*m.x387 - m.x281 == 0)

m.c277 = Constraint(expr=m.x366*m.x387 - m.x282 == 0)

m.c278 = Constraint(expr=m.x361*m.x388 - m.x283 == 0)

m.c279 = Constraint(expr=m.x362*m.x388 - m.x284 == 0)

m.c280 = Constraint(expr=m.x363*m.x388 - m.x285 == 0)

m.c281 = Constraint(expr=m.x364*m.x388 - m.x286 == 0)

m.c282 = Constraint(expr=m.x365*m.x388 - m.x287 == 0)

m.c283 = Constraint(expr=m.x366*m.x388 - m.x288 == 0)

m.c284 = Constraint(expr=m.x361*m.x389 - m.x289 == 0)

m.c285 = Constraint(expr=m.x362*m.x389 - m.x290 == 0)

m.c286 = Constraint(expr=m.x363*m.x389 - m.x291 == 0)

m.c287 = Constraint(expr=m.x364*m.x389 - m.x292 == 0)

m.c288 = Constraint(expr=m.x365*m.x389 - m.x293 == 0)

m.c289 = Constraint(expr=m.x366*m.x389 - m.x294 == 0)

m.c290 = Constraint(expr=m.x361*m.x390 - m.x295 == 0)

m.c291 = Constraint(expr=m.x362*m.x390 - m.x296 == 0)

m.c292 = Constraint(expr=m.x363*m.x390 - m.x297 == 0)

m.c293 = Constraint(expr=m.x364*m.x390 - m.x298 == 0)

m.c294 = Constraint(expr=m.x365*m.x390 - m.x299 == 0)

m.c295 = Constraint(expr=m.x366*m.x390 - m.x300 == 0)

m.c296 = Constraint(expr=m.x361*m.x391 - m.x301 == 0)

m.c297 = Constraint(expr=m.x362*m.x391 - m.x302 == 0)

m.c298 = Constraint(expr=m.x363*m.x391 - m.x303 == 0)

m.c299 = Constraint(expr=m.x364*m.x391 - m.x304 == 0)

m.c300 = Constraint(expr=m.x365*m.x391 - m.x305 == 0)

m.c301 = Constraint(expr=m.x366*m.x391 - m.x306 == 0)

m.c302 = Constraint(expr=   m.x307 + m.x308 + m.x309 + m.x310 + m.x311 + m.x312 == 1)

m.c303 = Constraint(expr=   m.x313 + m.x314 + m.x315 + m.x316 + m.x317 + m.x318 == 1)

m.c304 = Constraint(expr=   m.x319 + m.x320 + m.x321 + m.x322 + m.x323 + m.x324 == 1)

m.c305 = Constraint(expr=   m.x325 + m.x326 + m.x327 + m.x328 + m.x329 + m.x330 == 1)

m.c306 = Constraint(expr=   m.x331 + m.x332 + m.x333 + m.x334 + m.x335 + m.x336 == 1)

m.c307 = Constraint(expr=   m.x337 + m.x338 + m.x339 + m.x340 + m.x341 + m.x342 == 1)

m.c308 = Constraint(expr=   m.x343 + m.x344 + m.x345 + m.x346 + m.x347 + m.x348 == 1)

m.c309 = Constraint(expr=   m.x349 + m.x350 + m.x351 + m.x352 + m.x353 + m.x354 == 1)

m.c310 = Constraint(expr=   m.x355 + m.x356 + m.x357 + m.x358 + m.x359 + m.x360 == 1)

m.c311 = Constraint(expr=   m.x361 + m.x362 + m.x363 + m.x364 + m.x365 + m.x366 == 1)

m.c312 = Constraint(expr=   m.x7 + m.x37 + m.x67 + m.x97 + m.x127 + m.x157 + m.x187 + m.x217 + m.x247 + m.x277 - m.x392
                          == 0)

m.c313 = Constraint(expr=   m.x13 + m.x43 + m.x73 + m.x103 + m.x133 + m.x163 + m.x193 + m.x223 + m.x253 + m.x283
                          - m.x393 == 0)

m.c314 = Constraint(expr=   m.x19 + m.x49 + m.x79 + m.x109 + m.x139 + m.x169 + m.x199 + m.x229 + m.x259 + m.x289
                          - m.x394 == 0)

m.c315 = Constraint(expr=   m.x25 + m.x55 + m.x85 + m.x115 + m.x145 + m.x175 + m.x205 + m.x235 + m.x265 + m.x295
                          - m.x395 == 0)

m.c316 = Constraint(expr=   m.x31 + m.x61 + m.x91 + m.x121 + m.x151 + m.x181 + m.x211 + m.x241 + m.x271 + m.x301
                          - m.x396 == 0)

m.c317 = Constraint(expr=   m.x8 + m.x38 + m.x68 + m.x98 + m.x128 + m.x158 + m.x188 + m.x218 + m.x248 + m.x278 - m.x397
                          == 0)

m.c318 = Constraint(expr=   m.x14 + m.x44 + m.x74 + m.x104 + m.x134 + m.x164 + m.x194 + m.x224 + m.x254 + m.x284
                          - m.x398 == 0)

m.c319 = Constraint(expr=   m.x20 + m.x50 + m.x80 + m.x110 + m.x140 + m.x170 + m.x200 + m.x230 + m.x260 + m.x290
                          - m.x399 == 0)

m.c320 = Constraint(expr=   m.x26 + m.x56 + m.x86 + m.x116 + m.x146 + m.x176 + m.x206 + m.x236 + m.x266 + m.x296
                          - m.x400 == 0)

m.c321 = Constraint(expr=   m.x32 + m.x62 + m.x92 + m.x122 + m.x152 + m.x182 + m.x212 + m.x242 + m.x272 + m.x302
                          - m.x401 == 0)

m.c322 = Constraint(expr=   m.x9 + m.x39 + m.x69 + m.x99 + m.x129 + m.x159 + m.x189 + m.x219 + m.x249 + m.x279 - m.x402
                          == 0)

m.c323 = Constraint(expr=   m.x15 + m.x45 + m.x75 + m.x105 + m.x135 + m.x165 + m.x195 + m.x225 + m.x255 + m.x285
                          - m.x403 == 0)

m.c324 = Constraint(expr=   m.x21 + m.x51 + m.x81 + m.x111 + m.x141 + m.x171 + m.x201 + m.x231 + m.x261 + m.x291
                          - m.x404 == 0)

m.c325 = Constraint(expr=   m.x27 + m.x57 + m.x87 + m.x117 + m.x147 + m.x177 + m.x207 + m.x237 + m.x267 + m.x297
                          - m.x405 == 0)

m.c326 = Constraint(expr=   m.x33 + m.x63 + m.x93 + m.x123 + m.x153 + m.x183 + m.x213 + m.x243 + m.x273 + m.x303
                          - m.x406 == 0)

m.c327 = Constraint(expr=   m.x10 + m.x40 + m.x70 + m.x100 + m.x130 + m.x160 + m.x190 + m.x220 + m.x250 + m.x280
                          - m.x407 == 0)

m.c328 = Constraint(expr=   m.x16 + m.x46 + m.x76 + m.x106 + m.x136 + m.x166 + m.x196 + m.x226 + m.x256 + m.x286
                          - m.x408 == 0)

m.c329 = Constraint(expr=   m.x22 + m.x52 + m.x82 + m.x112 + m.x142 + m.x172 + m.x202 + m.x232 + m.x262 + m.x292
                          - m.x409 == 0)

m.c330 = Constraint(expr=   m.x28 + m.x58 + m.x88 + m.x118 + m.x148 + m.x178 + m.x208 + m.x238 + m.x268 + m.x298
                          - m.x410 == 0)

m.c331 = Constraint(expr=   m.x34 + m.x64 + m.x94 + m.x124 + m.x154 + m.x184 + m.x214 + m.x244 + m.x274 + m.x304
                          - m.x411 == 0)

m.c332 = Constraint(expr=   m.x11 + m.x41 + m.x71 + m.x101 + m.x131 + m.x161 + m.x191 + m.x221 + m.x251 + m.x281
                          - m.x412 == 0)

m.c333 = Constraint(expr=   m.x17 + m.x47 + m.x77 + m.x107 + m.x137 + m.x167 + m.x197 + m.x227 + m.x257 + m.x287
                          - m.x413 == 0)

m.c334 = Constraint(expr=   m.x23 + m.x53 + m.x83 + m.x113 + m.x143 + m.x173 + m.x203 + m.x233 + m.x263 + m.x293
                          - m.x414 == 0)

m.c335 = Constraint(expr=   m.x29 + m.x59 + m.x89 + m.x119 + m.x149 + m.x179 + m.x209 + m.x239 + m.x269 + m.x299
                          - m.x415 == 0)

m.c336 = Constraint(expr=   m.x35 + m.x65 + m.x95 + m.x125 + m.x155 + m.x185 + m.x215 + m.x245 + m.x275 + m.x305
                          - m.x416 == 0)

m.c337 = Constraint(expr=   m.x367 - 0.05*m.x392 == 0)

m.c338 = Constraint(expr=   m.x372 - 0.2*m.x397 == 0)

m.c339 = Constraint(expr=   m.x377 - m.x402 == 0)

m.c340 = Constraint(expr=   m.x382 - m.x407 == 0)

m.c341 = Constraint(expr=   m.x387 - m.x412 == 0)

m.c342 = Constraint(expr=   m.x368 - 0.05*m.x393 == 0)

m.c343 = Constraint(expr=   m.x373 - 0.2*m.x398 == 0)

m.c344 = Constraint(expr=   m.x378 - 0.4*m.x403 == 0)

m.c345 = Constraint(expr=   m.x383 - 0.4*m.x408 == 0)

m.c346 = Constraint(expr=   m.x388 - 0.4*m.x413 == 0)

m.c347 = Constraint(expr=   m.x369 - 0.4*m.x394 == 0)

m.c348 = Constraint(expr=   m.x374 - 0.4*m.x399 == 0)

m.c349 = Constraint(expr=   m.x379 - 0.05*m.x404 == 0)

m.c350 = Constraint(expr=   m.x384 - 0.2*m.x409 == 0)

m.c351 = Constraint(expr=   m.x389 - 0.15*m.x414 == 0)

m.c352 = Constraint(expr=   m.x370 - m.x395 == 0)

m.c353 = Constraint(expr=   m.x375 - m.x400 == 0)

m.c354 = Constraint(expr=   m.x380 - 0.05*m.x405 == 0)

m.c355 = Constraint(expr=   m.x385 - 0.15*m.x410 == 0)

m.c356 = Constraint(expr=   m.x390 - 0.2*m.x415 == 0)

m.c357 = Constraint(expr=   m.x371 - m.x396 == 0)

m.c358 = Constraint(expr=   m.x376 - m.x401 == 0)

m.c359 = Constraint(expr=   m.x381 - m.x406 == 0)

m.c360 = Constraint(expr=   m.x386 - m.x411 == 0)

m.c361 = Constraint(expr=   m.x391 - m.x416 == 0)

m.c362 = Constraint(expr=   m.x12 + m.x42 + m.x72 + m.x102 + m.x132 + m.x162 + m.x192 + m.x222 + m.x252 + m.x282 <= 3)

m.c363 = Constraint(expr=   m.x18 + m.x48 + m.x78 + m.x108 + m.x138 + m.x168 + m.x198 + m.x228 + m.x258 + m.x288 <= 3)

m.c364 = Constraint(expr=   m.x24 + m.x54 + m.x84 + m.x114 + m.x144 + m.x174 + m.x204 + m.x234 + m.x264 + m.x294 <= 3)

m.c365 = Constraint(expr=   m.x30 + m.x60 + m.x90 + m.x120 + m.x150 + m.x180 + m.x210 + m.x240 + m.x270 + m.x300 <= 3)

m.c366 = Constraint(expr=   m.x396 - 5*m.b417 >= 0)

m.c367 = Constraint(expr=   m.x401 - 3*m.b418 >= 0)

m.c368 = Constraint(expr=   m.x406 - 4*m.b419 >= 0)

m.c369 = Constraint(expr=   m.x411 - 3*m.b420 >= 0)

m.c370 = Constraint(expr=   m.x416 - m.b421 >= 0)

m.c371 = Constraint(expr=-(1500*m.x396**0.7 + 8000*m.x396) + m.x2 == 0)

m.c372 = Constraint(expr=-(1000*m.x401**0.7 + 8000*m.x401) + m.x3 == 0)

m.c373 = Constraint(expr=-(4000*m.x406**0.7 + 8000*m.x406) + m.x4 == 0)

m.c374 = Constraint(expr=-(3000*m.x411**0.7 + 8000*m.x411) + m.x5 == 0)

m.c375 = Constraint(expr=-(3000*m.x416**0.7 + 8000*m.x416) + m.x6 == 0)

m.c376 = Constraint(expr=   m.x396 - 40*m.b417 <= 0)

m.c377 = Constraint(expr=   m.x401 - 40*m.b418 <= 0)

m.c378 = Constraint(expr=   m.x406 - 40*m.b419 <= 0)

m.c379 = Constraint(expr=   m.x411 - 40*m.b420 <= 0)

m.c380 = Constraint(expr=   m.x416 - 40*m.b421 <= 0)
