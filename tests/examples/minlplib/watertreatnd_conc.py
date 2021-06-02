#  MINLP written by GAMS Convert at 04/21/18 13:55:19
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        320      306        5        9        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        361      356        5        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1086      561      525        0
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
m.x307 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x309 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x311 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x312 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x313 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x314 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x315 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x316 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x317 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x318 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x319 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x320 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x321 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x322 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x323 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x324 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x325 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x326 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x327 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x328 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x329 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x330 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x331 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x332 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x333 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x334 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x335 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x336 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x337 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x338 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x339 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x340 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x341 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x342 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x343 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x344 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x345 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x346 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x347 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x348 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x349 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x350 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x351 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x352 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x353 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x354 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x355 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x356 = Var(within=Reals,bounds=(0,4),initialize=0)
m.b357 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b358 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b359 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b360 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b361 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   m.x2 + m.x3 + m.x4 + m.x5 + m.x6, sense=minimize)

m.c2 = Constraint(expr= - m.x247 - m.x248 - m.x249 - m.x250 - m.x251 - m.x252 == -10)

m.c3 = Constraint(expr= - m.x253 - m.x254 - m.x255 - m.x256 - m.x257 - m.x258 == -15)

m.c4 = Constraint(expr= - m.x259 - m.x260 - m.x261 - m.x262 - m.x263 - m.x264 == -5)

m.c5 = Constraint(expr= - m.x265 - m.x266 - m.x267 - m.x268 - m.x269 - m.x270 == -20)

m.c6 = Constraint(expr= - m.x271 - m.x272 - m.x273 - m.x274 - m.x275 - m.x276 == -10)

m.c7 = Constraint(expr= - m.x7 == -1)

m.c8 = Constraint(expr= - m.x8 == -1)

m.c9 = Constraint(expr= - m.x9 == -1)

m.c10 = Constraint(expr= - m.x10 == -1)

m.c11 = Constraint(expr= - m.x11 == -1)

m.c12 = Constraint(expr= - m.x12 == -1)

m.c13 = Constraint(expr= - m.x13 == -1)

m.c14 = Constraint(expr= - m.x14 == -1)

m.c15 = Constraint(expr= - m.x15 == -1)

m.c16 = Constraint(expr= - m.x16 == -1)

m.c17 = Constraint(expr= - m.x17 == -1)

m.c18 = Constraint(expr= - m.x18 == -1)

m.c19 = Constraint(expr= - m.x19 == -1)

m.c20 = Constraint(expr= - m.x20 == -1)

m.c21 = Constraint(expr= - m.x21 == -1)

m.c22 = Constraint(expr= - m.x22 == -1)

m.c23 = Constraint(expr= - m.x23 == -1)

m.c24 = Constraint(expr= - m.x24 == -1)

m.c25 = Constraint(expr= - m.x25 == -1)

m.c26 = Constraint(expr= - m.x26 == -1)

m.c27 = Constraint(expr= - m.x27 == -1)

m.c28 = Constraint(expr= - m.x28 == -1)

m.c29 = Constraint(expr= - m.x29 == -1)

m.c30 = Constraint(expr= - m.x30 == -1)

m.c31 = Constraint(expr= - m.x31 == -1.33333)

m.c32 = Constraint(expr= - m.x32 == -1.33333)

m.c33 = Constraint(expr= - m.x33 == -1.33333)

m.c34 = Constraint(expr= - m.x34 == -1.33333)

m.c35 = Constraint(expr= - m.x35 == -1.33333)

m.c36 = Constraint(expr= - m.x36 == -1.33333)

m.c37 = Constraint(expr= - m.x37 == 0)

m.c38 = Constraint(expr= - m.x38 == 0)

m.c39 = Constraint(expr= - m.x39 == 0)

m.c40 = Constraint(expr= - m.x40 == 0)

m.c41 = Constraint(expr= - m.x41 == 0)

m.c42 = Constraint(expr= - m.x42 == 0)

m.c43 = Constraint(expr= - m.x43 == 0)

m.c44 = Constraint(expr= - m.x44 == 0)

m.c45 = Constraint(expr= - m.x45 == 0)

m.c46 = Constraint(expr= - m.x46 == 0)

m.c47 = Constraint(expr= - m.x47 == 0)

m.c48 = Constraint(expr= - m.x48 == 0)

m.c49 = Constraint(expr= - m.x49 == -0.66666)

m.c50 = Constraint(expr= - m.x50 == -0.66666)

m.c51 = Constraint(expr= - m.x51 == -0.66666)

m.c52 = Constraint(expr= - m.x52 == -0.66666)

m.c53 = Constraint(expr= - m.x53 == -0.66666)

m.c54 = Constraint(expr= - m.x54 == -0.66666)

m.c55 = Constraint(expr= - m.x55 == -2)

m.c56 = Constraint(expr= - m.x56 == -2)

m.c57 = Constraint(expr= - m.x57 == -2)

m.c58 = Constraint(expr= - m.x58 == -2)

m.c59 = Constraint(expr= - m.x59 == -2)

m.c60 = Constraint(expr= - m.x60 == -2)

m.c61 = Constraint(expr= - m.x61 == -2)

m.c62 = Constraint(expr= - m.x62 == -2)

m.c63 = Constraint(expr= - m.x63 == -2)

m.c64 = Constraint(expr= - m.x64 == -2)

m.c65 = Constraint(expr= - m.x65 == -2)

m.c66 = Constraint(expr= - m.x66 == -2)

m.c67 = Constraint(expr= - m.x67 == 0)

m.c68 = Constraint(expr= - m.x68 == 0)

m.c69 = Constraint(expr= - m.x69 == 0)

m.c70 = Constraint(expr= - m.x70 == 0)

m.c71 = Constraint(expr= - m.x71 == 0)

m.c72 = Constraint(expr= - m.x72 == 0)

m.c73 = Constraint(expr= - m.x73 == -4)

m.c74 = Constraint(expr= - m.x74 == -4)

m.c75 = Constraint(expr= - m.x75 == -4)

m.c76 = Constraint(expr= - m.x76 == -4)

m.c77 = Constraint(expr= - m.x77 == -4)

m.c78 = Constraint(expr= - m.x78 == -4)

m.c79 = Constraint(expr= - m.x79 == -1.5)

m.c80 = Constraint(expr= - m.x80 == -1.5)

m.c81 = Constraint(expr= - m.x81 == -1.5)

m.c82 = Constraint(expr= - m.x82 == -1.5)

m.c83 = Constraint(expr= - m.x83 == -1.5)

m.c84 = Constraint(expr= - m.x84 == -1.5)

m.c85 = Constraint(expr= - m.x85 == -0.5)

m.c86 = Constraint(expr= - m.x86 == -0.5)

m.c87 = Constraint(expr= - m.x87 == -0.5)

m.c88 = Constraint(expr= - m.x88 == -0.5)

m.c89 = Constraint(expr= - m.x89 == -0.5)

m.c90 = Constraint(expr= - m.x90 == -0.5)

m.c91 = Constraint(expr= - m.x91 == -0.5)

m.c92 = Constraint(expr= - m.x92 == -0.5)

m.c93 = Constraint(expr= - m.x93 == -0.5)

m.c94 = Constraint(expr= - m.x94 == -0.5)

m.c95 = Constraint(expr= - m.x95 == -0.5)

m.c96 = Constraint(expr= - m.x96 == -0.5)

m.c97 = Constraint(expr= - m.x97 == 0)

m.c98 = Constraint(expr= - m.x98 == 0)

m.c99 = Constraint(expr= - m.x99 == 0)

m.c100 = Constraint(expr= - m.x100 == 0)

m.c101 = Constraint(expr= - m.x101 == 0)

m.c102 = Constraint(expr= - m.x102 == 0)

m.c103 = Constraint(expr= - m.x103 == -2)

m.c104 = Constraint(expr= - m.x104 == -2)

m.c105 = Constraint(expr= - m.x105 == -2)

m.c106 = Constraint(expr= - m.x106 == -2)

m.c107 = Constraint(expr= - m.x107 == -2)

m.c108 = Constraint(expr= - m.x108 == -2)

m.c109 = Constraint(expr= - m.x109 == -2)

m.c110 = Constraint(expr= - m.x110 == -2)

m.c111 = Constraint(expr= - m.x111 == -2)

m.c112 = Constraint(expr= - m.x112 == -2)

m.c113 = Constraint(expr= - m.x113 == -2)

m.c114 = Constraint(expr= - m.x114 == -2)

m.c115 = Constraint(expr= - m.x115 == 0)

m.c116 = Constraint(expr= - m.x116 == 0)

m.c117 = Constraint(expr= - m.x117 == 0)

m.c118 = Constraint(expr= - m.x118 == 0)

m.c119 = Constraint(expr= - m.x119 == 0)

m.c120 = Constraint(expr= - m.x120 == 0)

m.c121 = Constraint(expr= - m.x121 == 0)

m.c122 = Constraint(expr= - m.x122 == 0)

m.c123 = Constraint(expr= - m.x123 == 0)

m.c124 = Constraint(expr= - m.x124 == 0)

m.c125 = Constraint(expr= - m.x125 == 0)

m.c126 = Constraint(expr= - m.x126 == 0)

m.c127 = Constraint(expr= - m.x277 - m.x278 - m.x279 - m.x280 - m.x281 - m.x282 + m.x307 == 0)

m.c128 = Constraint(expr= - m.x283 - m.x284 - m.x285 - m.x286 - m.x287 - m.x288 + m.x308 == 0)

m.c129 = Constraint(expr= - m.x289 - m.x290 - m.x291 - m.x292 - m.x293 - m.x294 + m.x309 == 0)

m.c130 = Constraint(expr= - m.x295 - m.x296 - m.x297 - m.x298 - m.x299 - m.x300 + m.x310 == 0)

m.c131 = Constraint(expr= - m.x301 - m.x302 - m.x303 - m.x304 - m.x305 - m.x306 + m.x311 == 0)

m.c132 = Constraint(expr= - m.x127 + m.x312 == 0)

m.c133 = Constraint(expr= - m.x128 + m.x312 == 0)

m.c134 = Constraint(expr= - m.x129 + m.x312 == 0)

m.c135 = Constraint(expr= - m.x130 + m.x312 == 0)

m.c136 = Constraint(expr= - m.x131 + m.x312 == 0)

m.c137 = Constraint(expr= - m.x132 + m.x312 == 0)

m.c138 = Constraint(expr= - m.x133 + m.x313 == 0)

m.c139 = Constraint(expr= - m.x134 + m.x313 == 0)

m.c140 = Constraint(expr= - m.x135 + m.x313 == 0)

m.c141 = Constraint(expr= - m.x136 + m.x313 == 0)

m.c142 = Constraint(expr= - m.x137 + m.x313 == 0)

m.c143 = Constraint(expr= - m.x138 + m.x313 == 0)

m.c144 = Constraint(expr= - m.x139 + m.x314 == 0)

m.c145 = Constraint(expr= - m.x140 + m.x314 == 0)

m.c146 = Constraint(expr= - m.x141 + m.x314 == 0)

m.c147 = Constraint(expr= - m.x142 + m.x314 == 0)

m.c148 = Constraint(expr= - m.x143 + m.x314 == 0)

m.c149 = Constraint(expr= - m.x144 + m.x314 == 0)

m.c150 = Constraint(expr= - m.x145 + m.x315 == 0)

m.c151 = Constraint(expr= - m.x146 + m.x315 == 0)

m.c152 = Constraint(expr= - m.x147 + m.x315 == 0)

m.c153 = Constraint(expr= - m.x148 + m.x315 == 0)

m.c154 = Constraint(expr= - m.x149 + m.x315 == 0)

m.c155 = Constraint(expr= - m.x150 + m.x315 == 0)

m.c156 = Constraint(expr= - m.x151 + m.x316 == 0)

m.c157 = Constraint(expr= - m.x152 + m.x316 == 0)

m.c158 = Constraint(expr= - m.x153 + m.x316 == 0)

m.c159 = Constraint(expr= - m.x154 + m.x316 == 0)

m.c160 = Constraint(expr= - m.x155 + m.x316 == 0)

m.c161 = Constraint(expr= - m.x156 + m.x316 == 0)

m.c162 = Constraint(expr= - m.x157 + m.x317 == 0)

m.c163 = Constraint(expr= - m.x158 + m.x317 == 0)

m.c164 = Constraint(expr= - m.x159 + m.x317 == 0)

m.c165 = Constraint(expr= - m.x160 + m.x317 == 0)

m.c166 = Constraint(expr= - m.x161 + m.x317 == 0)

m.c167 = Constraint(expr= - m.x162 + m.x317 == 0)

m.c168 = Constraint(expr= - m.x163 + m.x318 == 0)

m.c169 = Constraint(expr= - m.x164 + m.x318 == 0)

m.c170 = Constraint(expr= - m.x165 + m.x318 == 0)

m.c171 = Constraint(expr= - m.x166 + m.x318 == 0)

m.c172 = Constraint(expr= - m.x167 + m.x318 == 0)

m.c173 = Constraint(expr= - m.x168 + m.x318 == 0)

m.c174 = Constraint(expr= - m.x169 + m.x319 == 0)

m.c175 = Constraint(expr= - m.x170 + m.x319 == 0)

m.c176 = Constraint(expr= - m.x171 + m.x319 == 0)

m.c177 = Constraint(expr= - m.x172 + m.x319 == 0)

m.c178 = Constraint(expr= - m.x173 + m.x319 == 0)

m.c179 = Constraint(expr= - m.x174 + m.x319 == 0)

m.c180 = Constraint(expr= - m.x175 + m.x320 == 0)

m.c181 = Constraint(expr= - m.x176 + m.x320 == 0)

m.c182 = Constraint(expr= - m.x177 + m.x320 == 0)

m.c183 = Constraint(expr= - m.x178 + m.x320 == 0)

m.c184 = Constraint(expr= - m.x179 + m.x320 == 0)

m.c185 = Constraint(expr= - m.x180 + m.x320 == 0)

m.c186 = Constraint(expr= - m.x181 + m.x321 == 0)

m.c187 = Constraint(expr= - m.x182 + m.x321 == 0)

m.c188 = Constraint(expr= - m.x183 + m.x321 == 0)

m.c189 = Constraint(expr= - m.x184 + m.x321 == 0)

m.c190 = Constraint(expr= - m.x185 + m.x321 == 0)

m.c191 = Constraint(expr= - m.x186 + m.x321 == 0)

m.c192 = Constraint(expr= - m.x187 + m.x322 == 0)

m.c193 = Constraint(expr= - m.x188 + m.x322 == 0)

m.c194 = Constraint(expr= - m.x189 + m.x322 == 0)

m.c195 = Constraint(expr= - m.x190 + m.x322 == 0)

m.c196 = Constraint(expr= - m.x191 + m.x322 == 0)

m.c197 = Constraint(expr= - m.x192 + m.x322 == 0)

m.c198 = Constraint(expr= - m.x193 + m.x323 == 0)

m.c199 = Constraint(expr= - m.x194 + m.x323 == 0)

m.c200 = Constraint(expr= - m.x195 + m.x323 == 0)

m.c201 = Constraint(expr= - m.x196 + m.x323 == 0)

m.c202 = Constraint(expr= - m.x197 + m.x323 == 0)

m.c203 = Constraint(expr= - m.x198 + m.x323 == 0)

m.c204 = Constraint(expr= - m.x199 + m.x324 == 0)

m.c205 = Constraint(expr= - m.x200 + m.x324 == 0)

m.c206 = Constraint(expr= - m.x201 + m.x324 == 0)

m.c207 = Constraint(expr= - m.x202 + m.x324 == 0)

m.c208 = Constraint(expr= - m.x203 + m.x324 == 0)

m.c209 = Constraint(expr= - m.x204 + m.x324 == 0)

m.c210 = Constraint(expr= - m.x205 + m.x325 == 0)

m.c211 = Constraint(expr= - m.x206 + m.x325 == 0)

m.c212 = Constraint(expr= - m.x207 + m.x325 == 0)

m.c213 = Constraint(expr= - m.x208 + m.x325 == 0)

m.c214 = Constraint(expr= - m.x209 + m.x325 == 0)

m.c215 = Constraint(expr= - m.x210 + m.x325 == 0)

m.c216 = Constraint(expr= - m.x211 + m.x326 == 0)

m.c217 = Constraint(expr= - m.x212 + m.x326 == 0)

m.c218 = Constraint(expr= - m.x213 + m.x326 == 0)

m.c219 = Constraint(expr= - m.x214 + m.x326 == 0)

m.c220 = Constraint(expr= - m.x215 + m.x326 == 0)

m.c221 = Constraint(expr= - m.x216 + m.x326 == 0)

m.c222 = Constraint(expr= - m.x217 + m.x327 == 0)

m.c223 = Constraint(expr= - m.x218 + m.x327 == 0)

m.c224 = Constraint(expr= - m.x219 + m.x327 == 0)

m.c225 = Constraint(expr= - m.x220 + m.x327 == 0)

m.c226 = Constraint(expr= - m.x221 + m.x327 == 0)

m.c227 = Constraint(expr= - m.x222 + m.x327 == 0)

m.c228 = Constraint(expr= - m.x223 + m.x328 == 0)

m.c229 = Constraint(expr= - m.x224 + m.x328 == 0)

m.c230 = Constraint(expr= - m.x225 + m.x328 == 0)

m.c231 = Constraint(expr= - m.x226 + m.x328 == 0)

m.c232 = Constraint(expr= - m.x227 + m.x328 == 0)

m.c233 = Constraint(expr= - m.x228 + m.x328 == 0)

m.c234 = Constraint(expr= - m.x229 + m.x329 == 0)

m.c235 = Constraint(expr= - m.x230 + m.x329 == 0)

m.c236 = Constraint(expr= - m.x231 + m.x329 == 0)

m.c237 = Constraint(expr= - m.x232 + m.x329 == 0)

m.c238 = Constraint(expr= - m.x233 + m.x329 == 0)

m.c239 = Constraint(expr= - m.x234 + m.x329 == 0)

m.c240 = Constraint(expr= - m.x235 + m.x330 == 0)

m.c241 = Constraint(expr= - m.x236 + m.x330 == 0)

m.c242 = Constraint(expr= - m.x237 + m.x330 == 0)

m.c243 = Constraint(expr= - m.x238 + m.x330 == 0)

m.c244 = Constraint(expr= - m.x239 + m.x330 == 0)

m.c245 = Constraint(expr= - m.x240 + m.x330 == 0)

m.c246 = Constraint(expr= - m.x241 + m.x331 == 0)

m.c247 = Constraint(expr= - m.x242 + m.x331 == 0)

m.c248 = Constraint(expr= - m.x243 + m.x331 == 0)

m.c249 = Constraint(expr= - m.x244 + m.x331 == 0)

m.c250 = Constraint(expr= - m.x245 + m.x331 == 0)

m.c251 = Constraint(expr= - m.x246 + m.x331 == 0)

m.c252 = Constraint(expr=m.x247*m.x7 + m.x253*m.x31 + m.x259*m.x55 + m.x265*m.x79 + m.x271*m.x103 + m.x277*m.x127 + 
                         m.x283*m.x151 + m.x289*m.x175 + m.x295*m.x199 + m.x301*m.x223 - m.x332*m.x337 == 0)

m.c253 = Constraint(expr=m.x248*m.x8 + m.x254*m.x32 + m.x260*m.x56 + m.x266*m.x80 + m.x272*m.x104 + m.x278*m.x128 + 
                         m.x284*m.x152 + m.x290*m.x176 + m.x296*m.x200 + m.x302*m.x224 - m.x333*m.x341 == 0)

m.c254 = Constraint(expr=m.x249*m.x9 + m.x255*m.x33 + m.x261*m.x57 + m.x267*m.x81 + m.x273*m.x105 + m.x279*m.x129 + 
                         m.x285*m.x153 + m.x291*m.x177 + m.x297*m.x201 + m.x303*m.x225 - m.x334*m.x345 == 0)

m.c255 = Constraint(expr=m.x250*m.x10 + m.x256*m.x34 + m.x262*m.x58 + m.x268*m.x82 + m.x274*m.x106 + m.x280*m.x130 + 
                         m.x286*m.x154 + m.x292*m.x178 + m.x298*m.x202 + m.x304*m.x226 - m.x335*m.x349 == 0)

m.c256 = Constraint(expr=m.x251*m.x11 + m.x257*m.x35 + m.x263*m.x59 + m.x269*m.x83 + m.x275*m.x107 + m.x281*m.x131 + 
                         m.x287*m.x155 + m.x293*m.x179 + m.x299*m.x203 + m.x305*m.x227 - m.x336*m.x353 == 0)

m.c257 = Constraint(expr=m.x247*m.x13 + m.x253*m.x37 + m.x259*m.x61 + m.x265*m.x85 + m.x271*m.x109 + m.x277*m.x133 + 
                         m.x283*m.x157 + m.x289*m.x181 + m.x295*m.x205 + m.x301*m.x229 - m.x332*m.x338 == 0)

m.c258 = Constraint(expr=m.x248*m.x14 + m.x254*m.x38 + m.x260*m.x62 + m.x266*m.x86 + m.x272*m.x110 + m.x278*m.x134 + 
                         m.x284*m.x158 + m.x290*m.x182 + m.x296*m.x206 + m.x302*m.x230 - m.x333*m.x342 == 0)

m.c259 = Constraint(expr=m.x249*m.x15 + m.x255*m.x39 + m.x261*m.x63 + m.x267*m.x87 + m.x273*m.x111 + m.x279*m.x135 + 
                         m.x285*m.x159 + m.x291*m.x183 + m.x297*m.x207 + m.x303*m.x231 - m.x334*m.x346 == 0)

m.c260 = Constraint(expr=m.x250*m.x16 + m.x256*m.x40 + m.x262*m.x64 + m.x268*m.x88 + m.x274*m.x112 + m.x280*m.x136 + 
                         m.x286*m.x160 + m.x292*m.x184 + m.x298*m.x208 + m.x304*m.x232 - m.x335*m.x350 == 0)

m.c261 = Constraint(expr=m.x251*m.x17 + m.x257*m.x41 + m.x263*m.x65 + m.x269*m.x89 + m.x275*m.x113 + m.x281*m.x137 + 
                         m.x287*m.x161 + m.x293*m.x185 + m.x299*m.x209 + m.x305*m.x233 - m.x336*m.x354 == 0)

m.c262 = Constraint(expr=m.x247*m.x19 + m.x253*m.x43 + m.x259*m.x67 + m.x265*m.x91 + m.x271*m.x115 + m.x277*m.x139 + 
                         m.x283*m.x163 + m.x289*m.x187 + m.x295*m.x211 + m.x301*m.x235 - m.x332*m.x339 == 0)

m.c263 = Constraint(expr=m.x248*m.x20 + m.x254*m.x44 + m.x260*m.x68 + m.x266*m.x92 + m.x272*m.x116 + m.x278*m.x140 + 
                         m.x284*m.x164 + m.x290*m.x188 + m.x296*m.x212 + m.x302*m.x236 - m.x333*m.x343 == 0)

m.c264 = Constraint(expr=m.x249*m.x21 + m.x255*m.x45 + m.x261*m.x69 + m.x267*m.x93 + m.x273*m.x117 + m.x279*m.x141 + 
                         m.x285*m.x165 + m.x291*m.x189 + m.x297*m.x213 + m.x303*m.x237 - m.x334*m.x347 == 0)

m.c265 = Constraint(expr=m.x250*m.x22 + m.x256*m.x46 + m.x262*m.x70 + m.x268*m.x94 + m.x274*m.x118 + m.x280*m.x142 + 
                         m.x286*m.x166 + m.x292*m.x190 + m.x298*m.x214 + m.x304*m.x238 - m.x335*m.x351 == 0)

m.c266 = Constraint(expr=m.x251*m.x23 + m.x257*m.x47 + m.x263*m.x71 + m.x269*m.x95 + m.x275*m.x119 + m.x281*m.x143 + 
                         m.x287*m.x167 + m.x293*m.x191 + m.x299*m.x215 + m.x305*m.x239 - m.x336*m.x355 == 0)

m.c267 = Constraint(expr=m.x247*m.x25 + m.x253*m.x49 + m.x259*m.x73 + m.x265*m.x97 + m.x271*m.x121 + m.x277*m.x145 + 
                         m.x283*m.x169 + m.x289*m.x193 + m.x295*m.x217 + m.x301*m.x241 - m.x332*m.x340 == 0)

m.c268 = Constraint(expr=m.x248*m.x26 + m.x254*m.x50 + m.x260*m.x74 + m.x266*m.x98 + m.x272*m.x122 + m.x278*m.x146 + 
                         m.x284*m.x170 + m.x290*m.x194 + m.x296*m.x218 + m.x302*m.x242 - m.x333*m.x344 == 0)

m.c269 = Constraint(expr=m.x249*m.x27 + m.x255*m.x51 + m.x261*m.x75 + m.x267*m.x99 + m.x273*m.x123 + m.x279*m.x147 + 
                         m.x285*m.x171 + m.x291*m.x195 + m.x297*m.x219 + m.x303*m.x243 - m.x334*m.x348 == 0)

m.c270 = Constraint(expr=m.x250*m.x28 + m.x256*m.x52 + m.x262*m.x76 + m.x268*m.x100 + m.x274*m.x124 + m.x280*m.x148 + 
                         m.x286*m.x172 + m.x292*m.x196 + m.x298*m.x220 + m.x304*m.x244 - m.x335*m.x352 == 0)

m.c271 = Constraint(expr=m.x251*m.x29 + m.x257*m.x53 + m.x263*m.x77 + m.x269*m.x101 + m.x275*m.x125 + m.x281*m.x149 + 
                         m.x287*m.x173 + m.x293*m.x197 + m.x299*m.x221 + m.x305*m.x245 - m.x336*m.x356 == 0)

m.c272 = Constraint(expr=   m.x247 + m.x253 + m.x259 + m.x265 + m.x271 + m.x277 + m.x283 + m.x289 + m.x295 + m.x301
                          - m.x332 == 0)

m.c273 = Constraint(expr=   m.x248 + m.x254 + m.x260 + m.x266 + m.x272 + m.x278 + m.x284 + m.x290 + m.x296 + m.x302
                          - m.x333 == 0)

m.c274 = Constraint(expr=   m.x249 + m.x255 + m.x261 + m.x267 + m.x273 + m.x279 + m.x285 + m.x291 + m.x297 + m.x303
                          - m.x334 == 0)

m.c275 = Constraint(expr=   m.x250 + m.x256 + m.x262 + m.x268 + m.x274 + m.x280 + m.x286 + m.x292 + m.x298 + m.x304
                          - m.x335 == 0)

m.c276 = Constraint(expr=   m.x251 + m.x257 + m.x263 + m.x269 + m.x275 + m.x281 + m.x287 + m.x293 + m.x299 + m.x305
                          - m.x336 == 0)

m.c277 = Constraint(expr=   m.x312 - 0.05*m.x337 == 0)

m.c278 = Constraint(expr=   m.x316 - 0.2*m.x341 == 0)

m.c279 = Constraint(expr=   m.x320 - m.x345 == 0)

m.c280 = Constraint(expr=   m.x324 - m.x349 == 0)

m.c281 = Constraint(expr=   m.x328 - m.x353 == 0)

m.c282 = Constraint(expr=   m.x313 - 0.05*m.x338 == 0)

m.c283 = Constraint(expr=   m.x317 - 0.2*m.x342 == 0)

m.c284 = Constraint(expr=   m.x321 - 0.4*m.x346 == 0)

m.c285 = Constraint(expr=   m.x325 - 0.4*m.x350 == 0)

m.c286 = Constraint(expr=   m.x329 - 0.4*m.x354 == 0)

m.c287 = Constraint(expr=   m.x314 - 0.4*m.x339 == 0)

m.c288 = Constraint(expr=   m.x318 - 0.4*m.x343 == 0)

m.c289 = Constraint(expr=   m.x322 - 0.05*m.x347 == 0)

m.c290 = Constraint(expr=   m.x326 - 0.2*m.x351 == 0)

m.c291 = Constraint(expr=   m.x330 - 0.15*m.x355 == 0)

m.c292 = Constraint(expr=   m.x315 - m.x340 == 0)

m.c293 = Constraint(expr=   m.x319 - m.x344 == 0)

m.c294 = Constraint(expr=   m.x323 - 0.05*m.x348 == 0)

m.c295 = Constraint(expr=   m.x327 - 0.15*m.x352 == 0)

m.c296 = Constraint(expr=   m.x331 - 0.2*m.x356 == 0)

m.c297 = Constraint(expr=   m.x307 - m.x332 == 0)

m.c298 = Constraint(expr=   m.x308 - m.x333 == 0)

m.c299 = Constraint(expr=   m.x309 - m.x334 == 0)

m.c300 = Constraint(expr=   m.x310 - m.x335 == 0)

m.c301 = Constraint(expr=   m.x311 - m.x336 == 0)

m.c302 = Constraint(expr=m.x252*m.x12 + m.x258*m.x36 + m.x264*m.x60 + m.x270*m.x84 + m.x276*m.x108 + m.x282*m.x132 + 
                         m.x288*m.x156 + m.x294*m.x180 + m.x300*m.x204 + m.x306*m.x228 <= 30)

m.c303 = Constraint(expr=m.x252*m.x18 + m.x258*m.x42 + m.x264*m.x66 + m.x270*m.x90 + m.x276*m.x114 + m.x282*m.x138 + 
                         m.x288*m.x162 + m.x294*m.x186 + m.x300*m.x210 + m.x306*m.x234 <= 30)

m.c304 = Constraint(expr=m.x252*m.x24 + m.x258*m.x48 + m.x264*m.x72 + m.x270*m.x96 + m.x276*m.x120 + m.x282*m.x144 + 
                         m.x288*m.x168 + m.x294*m.x192 + m.x300*m.x216 + m.x306*m.x240 <= 30)

m.c305 = Constraint(expr=m.x252*m.x30 + m.x258*m.x54 + m.x264*m.x78 + m.x270*m.x102 + m.x276*m.x126 + m.x282*m.x150 + 
                         m.x288*m.x174 + m.x294*m.x198 + m.x300*m.x222 + m.x306*m.x246 <= 30)

m.c306 = Constraint(expr=   m.x332 - 5*m.b357 >= 0)

m.c307 = Constraint(expr=   m.x333 - 3*m.b358 >= 0)

m.c308 = Constraint(expr=   m.x334 - 4*m.b359 >= 0)

m.c309 = Constraint(expr=   m.x335 - 3*m.b360 >= 0)

m.c310 = Constraint(expr=   m.x336 - m.b361 >= 0)

m.c311 = Constraint(expr=-(1500*m.x332**0.7 + 8000*m.x332) + m.x2 == 0)

m.c312 = Constraint(expr=-(1000*m.x333**0.7 + 8000*m.x333) + m.x3 == 0)

m.c313 = Constraint(expr=-(4000*m.x334**0.7 + 8000*m.x334) + m.x4 == 0)

m.c314 = Constraint(expr=-(3000*m.x335**0.7 + 8000*m.x335) + m.x5 == 0)

m.c315 = Constraint(expr=-(3000*m.x336**0.7 + 8000*m.x336) + m.x6 == 0)

m.c316 = Constraint(expr=   m.x332 - 100*m.b357 <= 0)

m.c317 = Constraint(expr=   m.x333 - 100*m.b358 <= 0)

m.c318 = Constraint(expr=   m.x334 - 100*m.b359 <= 0)

m.c319 = Constraint(expr=   m.x335 - 100*m.b360 <= 0)

m.c320 = Constraint(expr=   m.x336 - 100*m.b361 <= 0)
