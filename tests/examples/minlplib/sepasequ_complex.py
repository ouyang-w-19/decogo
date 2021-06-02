#  MINLP written by GAMS Convert at 04/21/18 13:54:10
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       1311      174      661      476        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        498      448       50        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       4863     4023      840        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b15 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b18 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b19 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b21 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b23 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b24 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b25 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b26 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b27 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b28 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b29 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b30 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b31 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b32 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b33 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b34 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b35 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b36 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b38 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b39 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b40 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b41 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b42 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b43 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b44 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b45 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b46 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b47 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b48 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b49 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b50 = Var(within=Binary,bounds=(0,1),initialize=1)
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
m.x61 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x62 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,1),initialize=1)
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
m.x77 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x79 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x80 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x81 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x82 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x83 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x84 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x85 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x86 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x87 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x88 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x89 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x90 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x91 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x92 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x93 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x94 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x95 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x96 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x97 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x98 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x99 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x100 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x101 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x102 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x103 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x104 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x105 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x106 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x107 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x108 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x109 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x110 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x111 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x112 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x113 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x114 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x115 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x116 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x117 = Var(within=Reals,bounds=(0,20),initialize=1)
m.x118 = Var(within=Reals,bounds=(0,2),initialize=1)
m.x119 = Var(within=Reals,bounds=(0,2),initialize=1)
m.x120 = Var(within=Reals,bounds=(0,2),initialize=1)
m.x121 = Var(within=Reals,bounds=(0,2),initialize=1)
m.x122 = Var(within=Reals,bounds=(0,2),initialize=1)
m.x123 = Var(within=Reals,bounds=(0,2),initialize=1)
m.x124 = Var(within=Reals,bounds=(0,2),initialize=1)
m.x125 = Var(within=Reals,bounds=(0,2),initialize=1)
m.x126 = Var(within=Reals,bounds=(0,2),initialize=1)
m.x127 = Var(within=Reals,bounds=(0,2),initialize=1)
m.x128 = Var(within=Reals,bounds=(0,2),initialize=0.5)
m.x129 = Var(within=Reals,bounds=(0,2),initialize=0.5)
m.x130 = Var(within=Reals,bounds=(0,2),initialize=0.5)
m.x131 = Var(within=Reals,bounds=(0,2),initialize=0.5)
m.x132 = Var(within=Reals,bounds=(0,2),initialize=0.5)
m.x133 = Var(within=Reals,bounds=(0,2),initialize=0.5)
m.x134 = Var(within=Reals,bounds=(0,2),initialize=0.5)
m.x135 = Var(within=Reals,bounds=(0,2),initialize=0.5)
m.x136 = Var(within=Reals,bounds=(0,2),initialize=0.5)
m.x137 = Var(within=Reals,bounds=(0,2),initialize=0.5)
m.x138 = Var(within=Reals,bounds=(0,2),initialize=0.5)
m.x139 = Var(within=Reals,bounds=(0,2),initialize=0.5)
m.x140 = Var(within=Reals,bounds=(0,2),initialize=0.5)
m.x141 = Var(within=Reals,bounds=(0,2),initialize=0.5)
m.x142 = Var(within=Reals,bounds=(0,2),initialize=0.5)
m.x143 = Var(within=Reals,bounds=(0,2),initialize=0.5)
m.x144 = Var(within=Reals,bounds=(0,2),initialize=0.5)
m.x145 = Var(within=Reals,bounds=(0,2),initialize=0.5)
m.x146 = Var(within=Reals,bounds=(0,2),initialize=0.5)
m.x147 = Var(within=Reals,bounds=(0,2),initialize=0.5)
m.x148 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x235 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x255 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x258 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x262 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x263 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x264 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x265 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x266 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x267 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x268 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x269 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x270 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x271 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x272 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x273 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x274 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x275 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x276 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x277 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x278 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x279 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x280 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x281 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x282 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x283 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x284 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x285 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x286 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x287 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x289 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x290 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x291 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x292 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x293 = Var(within=Reals,bounds=(0,0.6),initialize=0)
m.x294 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x295 = Var(within=Reals,bounds=(0,0.2),initialize=0)
m.x296 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x297 = Var(within=Reals,bounds=(0,0.4),initialize=0)
m.x298 = Var(within=Reals,bounds=(4.05,10.49),initialize=7.27)
m.x299 = Var(within=Reals,bounds=(1.77,4.03),initialize=2.9)
m.x300 = Var(within=Reals,bounds=(1.32,1.75),initialize=1.32)
m.x301 = Var(within=Reals,bounds=(1.01,1.3),initialize=1.01)
m.x302 = Var(within=Reals,bounds=(4.05,10.49),initialize=7.27)
m.x303 = Var(within=Reals,bounds=(1.77,4.03),initialize=2.9)
m.x304 = Var(within=Reals,bounds=(1.32,1.75),initialize=1.32)
m.x305 = Var(within=Reals,bounds=(1.77,4.03),initialize=2.9)
m.x306 = Var(within=Reals,bounds=(1.32,1.75),initialize=1.32)
m.x307 = Var(within=Reals,bounds=(1.01,1.3),initialize=1.01)
m.x308 = Var(within=Reals,bounds=(4.05,10.49),initialize=7.27)
m.x309 = Var(within=Reals,bounds=(1.77,4.03),initialize=2.9)
m.x310 = Var(within=Reals,bounds=(1.77,4.03),initialize=2.9)
m.x311 = Var(within=Reals,bounds=(1.32,1.75),initialize=1.32)
m.x312 = Var(within=Reals,bounds=(1.32,1.75),initialize=1.32)
m.x313 = Var(within=Reals,bounds=(1.01,1.3),initialize=1.01)
m.x314 = Var(within=Reals,bounds=(4.05,10.49),initialize=7.27)
m.x315 = Var(within=Reals,bounds=(1.77,4.03),initialize=2.9)
m.x316 = Var(within=Reals,bounds=(1.32,1.75),initialize=1.32)
m.x317 = Var(within=Reals,bounds=(1.01,1.3),initialize=1.01)
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
m.x348 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x349 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x350 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x351 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x352 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x353 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x354 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x355 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x356 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x357 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x358 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x359 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x360 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x361 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x362 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x363 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x364 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x365 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x366 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x367 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x368 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x369 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x370 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x371 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x372 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x373 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x374 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x375 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x376 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x377 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x378 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x379 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x380 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x381 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x382 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x383 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x384 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x385 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x386 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x387 = Var(within=Reals,bounds=(0.1,25),initialize=2)
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
m.x449 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x450 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x451 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x452 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x453 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x454 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x455 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x456 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x457 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x458 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x459 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x460 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x461 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x462 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x463 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x464 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x465 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x466 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x467 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x468 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x469 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x470 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x471 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x472 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x473 = Var(within=Reals,bounds=(0,1000),initialize=0)
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
m.x489 = Var(within=Reals,bounds=(0,50),initialize=3)
m.x490 = Var(within=Reals,bounds=(0,50),initialize=3)
m.x491 = Var(within=Reals,bounds=(0,50),initialize=3)
m.x492 = Var(within=Reals,bounds=(0,50),initialize=3)
m.x493 = Var(within=Reals,bounds=(0,50),initialize=3)
m.x494 = Var(within=Reals,bounds=(0,50),initialize=3)
m.x495 = Var(within=Reals,bounds=(0,50),initialize=3)
m.x496 = Var(within=Reals,bounds=(0,50),initialize=3)
m.x497 = Var(within=Reals,bounds=(0,50),initialize=3)
m.x498 = Var(within=Reals,bounds=(0,50),initialize=3)

m.obj = Objective(expr=   1.5*m.x51 + 1.5*m.x52 + 1.5*m.x53 + 1.5*m.x54 + 1.5*m.x55 + 1.5*m.x56 + 1.5*m.x57 + 1.5*m.x58
                        + 1.5*m.x59 + 1.5*m.x60 + 1.5*m.x61 + 1.5*m.x62 + 1.5*m.x63 + 1.5*m.x64 + 1.5*m.x65
                        + 81.44*m.x348 + 81.44*m.x349 + 81.44*m.x350 + 81.44*m.x351 + 81.44*m.x352 + 81.44*m.x353
                        + 81.44*m.x354 + 81.44*m.x355 + 81.44*m.x356 + 81.44*m.x357 + 81.44*m.x358 + 81.44*m.x359
                        + 81.44*m.x360 + 81.44*m.x361 + 81.44*m.x362 + 3.04*m.x363 + 3.04*m.x364 + 3.04*m.x365
                        + 3.04*m.x366 + 3.04*m.x367 + 3.04*m.x368 + 3.04*m.x369 + 3.04*m.x370 + 3.04*m.x371
                        + 3.04*m.x372 + 3.04*m.x373 + 3.04*m.x374 + 3.04*m.x375 + 3.04*m.x376 + 3.04*m.x377 + m.x448
                        + m.x459 + m.x460 + m.x461 + m.x462 + m.x463 + m.x464 + m.x465 + m.x466 + m.x467 + m.x468
                        + m.x469 + m.x470 + m.x471 + m.x472 + m.x473, sense=minimize)

m.c1 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8 + m.b9 + m.b10 <= 1)

m.c2 = Constraint(expr=   m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 <= 1)

m.c3 = Constraint(expr=   m.b17 + m.b18 + m.b19 + m.b20 + m.b21 + m.b22 <= 1)

m.c4 = Constraint(expr=   m.b23 + m.b24 + m.b25 <= 1)

m.c5 = Constraint(expr=   m.b26 + m.b27 + m.b28 <= 1)

m.c6 = Constraint(expr=   m.b29 + m.b30 + m.b31 <= 1)

m.c7 = Constraint(expr=   m.b32 <= 1)

m.c8 = Constraint(expr=   m.b33 <= 1)

m.c9 = Constraint(expr=   m.b34 <= 1)

m.c10 = Constraint(expr=   m.b35 <= 1)

m.c11 = Constraint(expr=   m.b7 + m.b8 + m.b9 + m.b10 <= 1)

m.c12 = Constraint(expr=   m.b4 + m.b5 + m.b6 + m.b14 + m.b15 + m.b16 <= 1)

m.c13 = Constraint(expr=   m.b20 + m.b21 + m.b22 <= 1)

m.c14 = Constraint(expr=   m.b2 + m.b3 + m.b12 + m.b13 + m.b24 + m.b25 <= 1)

m.c15 = Constraint(expr=   m.b18 + m.b19 + m.b27 + m.b28 <= 1)

m.c16 = Constraint(expr=   m.b30 + m.b31 <= 1)

m.c17 = Constraint(expr=   m.b1 + m.b2 + m.b4 + m.b7 <= 1)

m.c18 = Constraint(expr=   m.b11 + m.b12 + m.b14 <= 1)

m.c19 = Constraint(expr=   m.b3 + m.b5 + m.b8 + m.b17 + m.b18 + m.b20 <= 1)

m.c20 = Constraint(expr=   m.b23 + m.b24 <= 1)

m.c21 = Constraint(expr=   m.b13 + m.b15 + m.b26 + m.b27 <= 1)

m.c22 = Constraint(expr=   m.b6 + m.b9 + m.b19 + m.b21 + m.b29 + m.b30 <= 1)

m.c23 = Constraint(expr=   m.b1 + m.b11 + m.b23 + m.b32 >= 1)

m.c24 = Constraint(expr=   m.b17 + m.b26 + m.b32 + m.b33 >= 1)

m.c25 = Constraint(expr=   m.b25 + m.b29 + m.b33 + m.b34 >= 1)

m.c26 = Constraint(expr=   m.b16 + m.b28 + m.b34 + m.b35 >= 1)

m.c27 = Constraint(expr=   m.b10 + m.b22 + m.b31 + m.b35 >= 1)

m.c28 = Constraint(expr=   m.b1 + m.b11 + m.b23 + m.b32 <= 1)

m.c29 = Constraint(expr=   m.b17 + m.b26 + m.b33 <= 1)

m.c30 = Constraint(expr=   m.b29 + m.b34 <= 1)

m.c31 = Constraint(expr=   m.b35 <= 1)

m.c32 = Constraint(expr=   m.b32 <= 1)

m.c33 = Constraint(expr=   m.b25 + m.b33 <= 1)

m.c34 = Constraint(expr=   m.b16 + m.b28 + m.b34 <= 1)

m.c35 = Constraint(expr=   m.b10 + m.b22 + m.b31 + m.b35 <= 1)

m.c36 = Constraint(expr=   m.b1 + m.b11 + m.b23 + m.b32 + m.x61 >= 1)

m.c37 = Constraint(expr=   m.b17 + m.b26 + m.b33 + m.x62 >= 1)

m.c38 = Constraint(expr=   m.b29 + m.b34 + m.x63 >= 1)

m.c39 = Constraint(expr=   m.b35 + m.x64 >= 1)

m.c40 = Constraint(expr=   m.x65 >= 1)

m.c41 = Constraint(expr=   m.x61 >= 1)

m.c42 = Constraint(expr=   m.b32 + m.x62 >= 1)

m.c43 = Constraint(expr=   m.b25 + m.b33 + m.x63 >= 1)

m.c44 = Constraint(expr=   m.b16 + m.b28 + m.b34 + m.x64 >= 1)

m.c45 = Constraint(expr=   m.b10 + m.b22 + m.b31 + m.b35 + m.x65 >= 1)

m.c46 = Constraint(expr= - m.b17 - m.b32 - m.x62 >= -2)

m.c47 = Constraint(expr= - m.b26 - m.b32 - m.x62 >= -2)

m.c48 = Constraint(expr= - m.b32 - m.b33 - m.x62 >= -2)

m.c49 = Constraint(expr= - m.b25 - m.b29 - m.x63 >= -2)

m.c50 = Constraint(expr= - m.b29 - m.b33 - m.x63 >= -2)

m.c51 = Constraint(expr= - m.b25 - m.b34 - m.x63 >= -2)

m.c52 = Constraint(expr= - m.b33 - m.b34 - m.x63 >= -2)

m.c53 = Constraint(expr= - m.b16 - m.b35 - m.x64 >= -2)

m.c54 = Constraint(expr= - m.b28 - m.b35 - m.x64 >= -2)

m.c55 = Constraint(expr= - m.b34 - m.b35 - m.x64 >= -2)

m.c56 = Constraint(expr=   m.b7 + m.b8 + m.b9 + m.b10 - m.x52 >= 0)

m.c57 = Constraint(expr=   m.b1 + m.b2 + m.b4 + m.b7 - m.x53 >= 0)

m.c58 = Constraint(expr=   m.b4 + m.b5 + m.b6 + m.b14 + m.b15 + m.b16 - m.x54 >= 0)

m.c59 = Constraint(expr=   m.b11 + m.b12 + m.b14 + m.b20 + m.b21 + m.b22 - m.x55 >= 0)

m.c60 = Constraint(expr=   m.b3 + m.b5 + m.b8 + m.b17 + m.b18 + m.b20 - m.x56 >= 0)

m.c61 = Constraint(expr=   m.b2 + m.b3 + m.b12 + m.b13 + m.b24 + m.b25 - m.x57 >= 0)

m.c62 = Constraint(expr=   m.b18 + m.b19 + m.b23 + m.b24 + m.b27 + m.b28 - m.x58 >= 0)

m.c63 = Constraint(expr=   m.b13 + m.b15 + m.b26 + m.b27 + m.b30 + m.b31 - m.x59 >= 0)

m.c64 = Constraint(expr=   m.b6 + m.b9 + m.b19 + m.b21 + m.b29 + m.b30 - m.x60 >= 0)

m.c65 = Constraint(expr= - m.b11 - m.b20 - m.x55 >= -2)

m.c66 = Constraint(expr= - m.b11 - m.b21 - m.x55 >= -2)

m.c67 = Constraint(expr= - m.b11 - m.b22 - m.x55 >= -2)

m.c68 = Constraint(expr= - m.b12 - m.b20 - m.x55 >= -2)

m.c69 = Constraint(expr= - m.b12 - m.b21 - m.x55 >= -2)

m.c70 = Constraint(expr= - m.b12 - m.b22 - m.x55 >= -2)

m.c71 = Constraint(expr= - m.b14 - m.b20 - m.x55 >= -2)

m.c72 = Constraint(expr= - m.b14 - m.b21 - m.x55 >= -2)

m.c73 = Constraint(expr= - m.b14 - m.b22 - m.x55 >= -2)

m.c74 = Constraint(expr= - m.b18 - m.b23 - m.x58 >= -2)

m.c75 = Constraint(expr= - m.b18 - m.b24 - m.x58 >= -2)

m.c76 = Constraint(expr= - m.b19 - m.b23 - m.x58 >= -2)

m.c77 = Constraint(expr= - m.b19 - m.b24 - m.x58 >= -2)

m.c78 = Constraint(expr= - m.b23 - m.b27 - m.x58 >= -2)

m.c79 = Constraint(expr= - m.b24 - m.b27 - m.x58 >= -2)

m.c80 = Constraint(expr= - m.b23 - m.b28 - m.x58 >= -2)

m.c81 = Constraint(expr= - m.b24 - m.b28 - m.x58 >= -2)

m.c82 = Constraint(expr= - m.b13 - m.b30 - m.x59 >= -2)

m.c83 = Constraint(expr= - m.b15 - m.b30 - m.x59 >= -2)

m.c84 = Constraint(expr= - m.b26 - m.b30 - m.x59 >= -2)

m.c85 = Constraint(expr= - m.b27 - m.b30 - m.x59 >= -2)

m.c86 = Constraint(expr= - m.b13 - m.b31 - m.x59 >= -2)

m.c87 = Constraint(expr= - m.b15 - m.b31 - m.x59 >= -2)

m.c88 = Constraint(expr= - m.b26 - m.b31 - m.x59 >= -2)

m.c89 = Constraint(expr= - m.b27 - m.b31 - m.x59 >= -2)

m.c90 = Constraint(expr= - m.b7 + m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 >= 0)

m.c91 = Constraint(expr= - m.b8 + m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 >= 0)

m.c92 = Constraint(expr= - m.b9 + m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 >= 0)

m.c93 = Constraint(expr= - m.b10 + m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 >= 0)

m.c94 = Constraint(expr= - m.b1 + m.b17 + m.b18 + m.b19 + m.b20 + m.b21 + m.b22 >= 0)

m.c95 = Constraint(expr= - m.b2 + m.b17 + m.b18 + m.b19 + m.b20 + m.b21 + m.b22 >= 0)

m.c96 = Constraint(expr= - m.b4 + m.b17 + m.b18 + m.b19 + m.b20 + m.b21 + m.b22 >= 0)

m.c97 = Constraint(expr= - m.b7 + m.b17 + m.b18 + m.b19 + m.b20 + m.b21 + m.b22 >= 0)

m.c98 = Constraint(expr= - m.b4 + m.b23 + m.b24 + m.b25 >= 0)

m.c99 = Constraint(expr= - m.b5 + m.b23 + m.b24 + m.b25 >= 0)

m.c100 = Constraint(expr= - m.b6 + m.b23 + m.b24 + m.b25 >= 0)

m.c101 = Constraint(expr= - m.b14 + m.b23 + m.b24 + m.b25 >= 0)

m.c102 = Constraint(expr= - m.b15 + m.b23 + m.b24 + m.b25 >= 0)

m.c103 = Constraint(expr= - m.b16 + m.b23 + m.b24 + m.b25 >= 0)

m.c104 = Constraint(expr= - m.b11 + m.b26 + m.b27 + m.b28 >= 0)

m.c105 = Constraint(expr= - m.b12 + m.b26 + m.b27 + m.b28 >= 0)

m.c106 = Constraint(expr= - m.b14 + m.b26 + m.b27 + m.b28 >= 0)

m.c107 = Constraint(expr= - m.b20 + m.b26 + m.b27 + m.b28 >= 0)

m.c108 = Constraint(expr= - m.b21 + m.b26 + m.b27 + m.b28 >= 0)

m.c109 = Constraint(expr= - m.b22 + m.b26 + m.b27 + m.b28 >= 0)

m.c110 = Constraint(expr= - m.b3 + m.b29 + m.b30 + m.b31 >= 0)

m.c111 = Constraint(expr= - m.b5 + m.b29 + m.b30 + m.b31 >= 0)

m.c112 = Constraint(expr= - m.b8 + m.b29 + m.b30 + m.b31 >= 0)

m.c113 = Constraint(expr= - m.b17 + m.b29 + m.b30 + m.b31 >= 0)

m.c114 = Constraint(expr= - m.b18 + m.b29 + m.b30 + m.b31 >= 0)

m.c115 = Constraint(expr= - m.b20 + m.b29 + m.b30 + m.b31 >= 0)

m.c116 = Constraint(expr= - m.b2 + m.b32 >= 0)

m.c117 = Constraint(expr= - m.b3 + m.b32 >= 0)

m.c118 = Constraint(expr= - m.b12 + m.b32 >= 0)

m.c119 = Constraint(expr= - m.b13 + m.b32 >= 0)

m.c120 = Constraint(expr= - m.b24 + m.b32 >= 0)

m.c121 = Constraint(expr= - m.b25 + m.b32 >= 0)

m.c122 = Constraint(expr= - m.b18 + m.b33 >= 0)

m.c123 = Constraint(expr= - m.b19 + m.b33 >= 0)

m.c124 = Constraint(expr= - m.b23 + m.b33 >= 0)

m.c125 = Constraint(expr= - m.b24 + m.b33 >= 0)

m.c126 = Constraint(expr= - m.b27 + m.b33 >= 0)

m.c127 = Constraint(expr= - m.b28 + m.b33 >= 0)

m.c128 = Constraint(expr= - m.b13 + m.b34 >= 0)

m.c129 = Constraint(expr= - m.b15 + m.b34 >= 0)

m.c130 = Constraint(expr= - m.b26 + m.b34 >= 0)

m.c131 = Constraint(expr= - m.b27 + m.b34 >= 0)

m.c132 = Constraint(expr= - m.b30 + m.b34 >= 0)

m.c133 = Constraint(expr= - m.b31 + m.b34 >= 0)

m.c134 = Constraint(expr= - m.b6 + m.b35 >= 0)

m.c135 = Constraint(expr= - m.b9 + m.b35 >= 0)

m.c136 = Constraint(expr= - m.b19 + m.b35 >= 0)

m.c137 = Constraint(expr= - m.b21 + m.b35 >= 0)

m.c138 = Constraint(expr= - m.b29 + m.b35 >= 0)

m.c139 = Constraint(expr= - m.b30 + m.b35 >= 0)

m.c140 = Constraint(expr=   m.b7 + m.b8 + m.b9 + m.b10 - m.b11 >= 0)

m.c141 = Constraint(expr=   m.b7 + m.b8 + m.b9 + m.b10 - m.b12 >= 0)

m.c142 = Constraint(expr=   m.b7 + m.b8 + m.b9 + m.b10 - m.b13 >= 0)

m.c143 = Constraint(expr=   m.b7 + m.b8 + m.b9 + m.b10 - m.b14 >= 0)

m.c144 = Constraint(expr=   m.b7 + m.b8 + m.b9 + m.b10 - m.b15 >= 0)

m.c145 = Constraint(expr=   m.b7 + m.b8 + m.b9 + m.b10 - m.b16 >= 0)

m.c146 = Constraint(expr=   m.b1 + m.b2 + m.b4 + m.b7 - m.b17 >= 0)

m.c147 = Constraint(expr=   m.b1 + m.b2 + m.b4 + m.b7 - m.b18 >= 0)

m.c148 = Constraint(expr=   m.b1 + m.b2 + m.b4 + m.b7 - m.b19 >= 0)

m.c149 = Constraint(expr=   m.b1 + m.b2 + m.b4 + m.b7 - m.b20 >= 0)

m.c150 = Constraint(expr=   m.b1 + m.b2 + m.b4 + m.b7 - m.b21 >= 0)

m.c151 = Constraint(expr=   m.b1 + m.b2 + m.b4 + m.b7 - m.b22 >= 0)

m.c152 = Constraint(expr=   m.b4 + m.b5 + m.b6 + m.b14 + m.b15 + m.b16 - m.b23 >= 0)

m.c153 = Constraint(expr=   m.b4 + m.b5 + m.b6 + m.b14 + m.b15 + m.b16 - m.b24 >= 0)

m.c154 = Constraint(expr=   m.b4 + m.b5 + m.b6 + m.b14 + m.b15 + m.b16 - m.b25 >= 0)

m.c155 = Constraint(expr=   m.b11 + m.b12 + m.b14 + m.b20 + m.b21 + m.b22 - m.b26 >= 0)

m.c156 = Constraint(expr=   m.b11 + m.b12 + m.b14 + m.b20 + m.b21 + m.b22 - m.b27 >= 0)

m.c157 = Constraint(expr=   m.b11 + m.b12 + m.b14 + m.b20 + m.b21 + m.b22 - m.b28 >= 0)

m.c158 = Constraint(expr=   m.b3 + m.b5 + m.b8 + m.b17 + m.b18 + m.b20 - m.b29 >= 0)

m.c159 = Constraint(expr=   m.b3 + m.b5 + m.b8 + m.b17 + m.b18 + m.b20 - m.b30 >= 0)

m.c160 = Constraint(expr=   m.b3 + m.b5 + m.b8 + m.b17 + m.b18 + m.b20 - m.b31 >= 0)

m.c161 = Constraint(expr=   m.b2 + m.b3 + m.b12 + m.b13 + m.b24 + m.b25 - m.b32 >= 0)

m.c162 = Constraint(expr=   m.b18 + m.b19 + m.b23 + m.b24 + m.b27 + m.b28 - m.b33 >= 0)

m.c163 = Constraint(expr=   m.b13 + m.b15 + m.b26 + m.b27 + m.b30 + m.b31 - m.b34 >= 0)

m.c164 = Constraint(expr=   m.b6 + m.b9 + m.b19 + m.b21 + m.b29 + m.b30 - m.b35 >= 0)

m.c165 = Constraint(expr= - m.b1 + m.x66 >= 0)

m.c166 = Constraint(expr= - m.b2 + m.x66 >= 0)

m.c167 = Constraint(expr= - m.b3 + m.x66 >= 0)

m.c168 = Constraint(expr= - m.b4 + m.x66 >= 0)

m.c169 = Constraint(expr= - m.b5 + m.x66 >= 0)

m.c170 = Constraint(expr= - m.b6 + m.x66 >= 0)

m.c171 = Constraint(expr= - m.b7 + m.x66 >= 0)

m.c172 = Constraint(expr= - m.b8 + m.x66 >= 0)

m.c173 = Constraint(expr= - m.b9 + m.x66 >= 0)

m.c174 = Constraint(expr= - m.b10 + m.x66 >= 0)

m.c175 = Constraint(expr= - m.b11 + m.x67 >= 0)

m.c176 = Constraint(expr= - m.b12 + m.x67 >= 0)

m.c177 = Constraint(expr= - m.b13 + m.x67 >= 0)

m.c178 = Constraint(expr= - m.b14 + m.x67 >= 0)

m.c179 = Constraint(expr= - m.b15 + m.x67 >= 0)

m.c180 = Constraint(expr= - m.b16 + m.x67 >= 0)

m.c181 = Constraint(expr= - m.b17 + m.x68 >= 0)

m.c182 = Constraint(expr= - m.b18 + m.x68 >= 0)

m.c183 = Constraint(expr= - m.b19 + m.x68 >= 0)

m.c184 = Constraint(expr= - m.b20 + m.x68 >= 0)

m.c185 = Constraint(expr= - m.b21 + m.x68 >= 0)

m.c186 = Constraint(expr= - m.b22 + m.x68 >= 0)

m.c187 = Constraint(expr= - m.b23 + m.x69 >= 0)

m.c188 = Constraint(expr= - m.b24 + m.x69 >= 0)

m.c189 = Constraint(expr= - m.b25 + m.x69 >= 0)

m.c190 = Constraint(expr= - m.b26 + m.x70 >= 0)

m.c191 = Constraint(expr= - m.b27 + m.x70 >= 0)

m.c192 = Constraint(expr= - m.b28 + m.x70 >= 0)

m.c193 = Constraint(expr= - m.b29 + m.x71 >= 0)

m.c194 = Constraint(expr= - m.b30 + m.x71 >= 0)

m.c195 = Constraint(expr= - m.b31 + m.x71 >= 0)

m.c196 = Constraint(expr= - m.b32 + m.x72 >= 0)

m.c197 = Constraint(expr= - m.b33 + m.x73 >= 0)

m.c198 = Constraint(expr= - m.b34 + m.x74 >= 0)

m.c199 = Constraint(expr= - m.b35 + m.x75 >= 0)

m.c200 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8 + m.b9 + m.b10 - m.x66 >= 0)

m.c201 = Constraint(expr=   m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 - m.x67 >= 0)

m.c202 = Constraint(expr=   m.b17 + m.b18 + m.b19 + m.b20 + m.b21 + m.b22 - m.x68 >= 0)

m.c203 = Constraint(expr=   m.b23 + m.b24 + m.b25 - m.x69 >= 0)

m.c204 = Constraint(expr=   m.b26 + m.b27 + m.b28 - m.x70 >= 0)

m.c205 = Constraint(expr=   m.b29 + m.b30 + m.b31 - m.x71 >= 0)

m.c206 = Constraint(expr=   m.b32 - m.x72 >= 0)

m.c207 = Constraint(expr=   m.b33 - m.x73 >= 0)

m.c208 = Constraint(expr=   m.b34 - m.x74 >= 0)

m.c209 = Constraint(expr=   m.b35 - m.x75 >= 0)

m.c211 = Constraint(expr=   m.x77 - 81.44*m.x348 - 81.44*m.x349 - 81.44*m.x350 - 81.44*m.x351 - 81.44*m.x352
                          - 81.44*m.x353 - 81.44*m.x354 - 81.44*m.x355 - 81.44*m.x356 - 81.44*m.x357 - 81.44*m.x358
                          - 81.44*m.x359 - 81.44*m.x360 - 81.44*m.x361 - 81.44*m.x362 - 3.04*m.x363 - 3.04*m.x364
                          - 3.04*m.x365 - 3.04*m.x366 - 3.04*m.x367 - 3.04*m.x368 - 3.04*m.x369 - 3.04*m.x370
                          - 3.04*m.x371 - 3.04*m.x372 - 3.04*m.x373 - 3.04*m.x374 - 3.04*m.x375 - 3.04*m.x376
                          - 3.04*m.x377 == 0)

m.c212 = Constraint(expr=   m.x148 == 0.6)

m.c213 = Constraint(expr=   m.x149 == 0.4)

m.c214 = Constraint(expr=   m.x150 == 0.2)

m.c215 = Constraint(expr=   m.x151 == 0.4)

m.c216 = Constraint(expr=   m.x152 == 0.4)

m.c217 = Constraint(expr= - m.x78 + m.x88 == 0)

m.c218 = Constraint(expr=   2*m.x66 + m.x148 - m.x198 - m.x248 <= 2)

m.c219 = Constraint(expr=   2*m.x66 + m.x149 - m.x199 - m.x249 <= 2)

m.c220 = Constraint(expr=   2*m.x66 + m.x150 - m.x200 - m.x250 <= 2)

m.c221 = Constraint(expr=   2*m.x66 + m.x151 - m.x201 - m.x251 <= 2)

m.c222 = Constraint(expr=   2*m.x66 + m.x152 - m.x202 - m.x252 <= 2)

m.c223 = Constraint(expr=   2*m.x67 + m.x153 - m.x203 - m.x253 <= 2)

m.c224 = Constraint(expr=   2*m.x67 + m.x154 - m.x204 - m.x254 <= 2)

m.c225 = Constraint(expr=   2*m.x67 + m.x155 - m.x205 - m.x255 <= 2)

m.c226 = Constraint(expr=   2*m.x67 + m.x156 - m.x206 - m.x256 <= 2)

m.c227 = Constraint(expr=   2*m.x67 + m.x157 - m.x207 - m.x257 <= 2)

m.c228 = Constraint(expr=   2*m.x68 + m.x158 - m.x208 - m.x258 <= 2)

m.c229 = Constraint(expr=   2*m.x68 + m.x159 - m.x209 - m.x259 <= 2)

m.c230 = Constraint(expr=   2*m.x68 + m.x160 - m.x210 - m.x260 <= 2)

m.c231 = Constraint(expr=   2*m.x68 + m.x161 - m.x211 - m.x261 <= 2)

m.c232 = Constraint(expr=   2*m.x68 + m.x162 - m.x212 - m.x262 <= 2)

m.c233 = Constraint(expr=   2*m.x69 + m.x163 - m.x213 - m.x263 <= 2)

m.c234 = Constraint(expr=   2*m.x69 + m.x164 - m.x214 - m.x264 <= 2)

m.c235 = Constraint(expr=   2*m.x69 + m.x165 - m.x215 - m.x265 <= 2)

m.c236 = Constraint(expr=   2*m.x69 + m.x166 - m.x216 - m.x266 <= 2)

m.c237 = Constraint(expr=   2*m.x69 + m.x167 - m.x217 - m.x267 <= 2)

m.c238 = Constraint(expr=   2*m.x70 + m.x168 - m.x218 - m.x268 <= 2)

m.c239 = Constraint(expr=   2*m.x70 + m.x169 - m.x219 - m.x269 <= 2)

m.c240 = Constraint(expr=   2*m.x70 + m.x170 - m.x220 - m.x270 <= 2)

m.c241 = Constraint(expr=   2*m.x70 + m.x171 - m.x221 - m.x271 <= 2)

m.c242 = Constraint(expr=   2*m.x70 + m.x172 - m.x222 - m.x272 <= 2)

m.c243 = Constraint(expr=   2*m.x71 + m.x173 - m.x223 - m.x273 <= 2)

m.c244 = Constraint(expr=   2*m.x71 + m.x174 - m.x224 - m.x274 <= 2)

m.c245 = Constraint(expr=   2*m.x71 + m.x175 - m.x225 - m.x275 <= 2)

m.c246 = Constraint(expr=   2*m.x71 + m.x176 - m.x226 - m.x276 <= 2)

m.c247 = Constraint(expr=   2*m.x71 + m.x177 - m.x227 - m.x277 <= 2)

m.c248 = Constraint(expr=   2*m.x72 + m.x178 - m.x228 - m.x278 <= 2)

m.c249 = Constraint(expr=   2*m.x72 + m.x179 - m.x229 - m.x279 <= 2)

m.c250 = Constraint(expr=   2*m.x72 + m.x180 - m.x230 - m.x280 <= 2)

m.c251 = Constraint(expr=   2*m.x72 + m.x181 - m.x231 - m.x281 <= 2)

m.c252 = Constraint(expr=   2*m.x72 + m.x182 - m.x232 - m.x282 <= 2)

m.c253 = Constraint(expr=   2*m.x73 + m.x183 - m.x233 - m.x283 <= 2)

m.c254 = Constraint(expr=   2*m.x73 + m.x184 - m.x234 - m.x284 <= 2)

m.c255 = Constraint(expr=   2*m.x73 + m.x185 - m.x235 - m.x285 <= 2)

m.c256 = Constraint(expr=   2*m.x73 + m.x186 - m.x236 - m.x286 <= 2)

m.c257 = Constraint(expr=   2*m.x73 + m.x187 - m.x237 - m.x287 <= 2)

m.c258 = Constraint(expr=   2*m.x74 + m.x188 - m.x238 - m.x288 <= 2)

m.c259 = Constraint(expr=   2*m.x74 + m.x189 - m.x239 - m.x289 <= 2)

m.c260 = Constraint(expr=   2*m.x74 + m.x190 - m.x240 - m.x290 <= 2)

m.c261 = Constraint(expr=   2*m.x74 + m.x191 - m.x241 - m.x291 <= 2)

m.c262 = Constraint(expr=   2*m.x74 + m.x192 - m.x242 - m.x292 <= 2)

m.c263 = Constraint(expr=   2*m.x75 + m.x193 - m.x243 - m.x293 <= 2)

m.c264 = Constraint(expr=   2*m.x75 + m.x194 - m.x244 - m.x294 <= 2)

m.c265 = Constraint(expr=   2*m.x75 + m.x195 - m.x245 - m.x295 <= 2)

m.c266 = Constraint(expr=   2*m.x75 + m.x196 - m.x246 - m.x296 <= 2)

m.c267 = Constraint(expr=   2*m.x75 + m.x197 - m.x247 - m.x297 <= 2)

m.c268 = Constraint(expr= - 2*m.x66 + m.x148 - m.x198 - m.x248 >= -2)

m.c269 = Constraint(expr= - 2*m.x66 + m.x149 - m.x199 - m.x249 >= -2)

m.c270 = Constraint(expr= - 2*m.x66 + m.x150 - m.x200 - m.x250 >= -2)

m.c271 = Constraint(expr= - 2*m.x66 + m.x151 - m.x201 - m.x251 >= -2)

m.c272 = Constraint(expr= - 2*m.x66 + m.x152 - m.x202 - m.x252 >= -2)

m.c273 = Constraint(expr= - 2*m.x67 + m.x153 - m.x203 - m.x253 >= -2)

m.c274 = Constraint(expr= - 2*m.x67 + m.x154 - m.x204 - m.x254 >= -2)

m.c275 = Constraint(expr= - 2*m.x67 + m.x155 - m.x205 - m.x255 >= -2)

m.c276 = Constraint(expr= - 2*m.x67 + m.x156 - m.x206 - m.x256 >= -2)

m.c277 = Constraint(expr= - 2*m.x67 + m.x157 - m.x207 - m.x257 >= -2)

m.c278 = Constraint(expr= - 2*m.x68 + m.x158 - m.x208 - m.x258 >= -2)

m.c279 = Constraint(expr= - 2*m.x68 + m.x159 - m.x209 - m.x259 >= -2)

m.c280 = Constraint(expr= - 2*m.x68 + m.x160 - m.x210 - m.x260 >= -2)

m.c281 = Constraint(expr= - 2*m.x68 + m.x161 - m.x211 - m.x261 >= -2)

m.c282 = Constraint(expr= - 2*m.x68 + m.x162 - m.x212 - m.x262 >= -2)

m.c283 = Constraint(expr= - 2*m.x69 + m.x163 - m.x213 - m.x263 >= -2)

m.c284 = Constraint(expr= - 2*m.x69 + m.x164 - m.x214 - m.x264 >= -2)

m.c285 = Constraint(expr= - 2*m.x69 + m.x165 - m.x215 - m.x265 >= -2)

m.c286 = Constraint(expr= - 2*m.x69 + m.x166 - m.x216 - m.x266 >= -2)

m.c287 = Constraint(expr= - 2*m.x69 + m.x167 - m.x217 - m.x267 >= -2)

m.c288 = Constraint(expr= - 2*m.x70 + m.x168 - m.x218 - m.x268 >= -2)

m.c289 = Constraint(expr= - 2*m.x70 + m.x169 - m.x219 - m.x269 >= -2)

m.c290 = Constraint(expr= - 2*m.x70 + m.x170 - m.x220 - m.x270 >= -2)

m.c291 = Constraint(expr= - 2*m.x70 + m.x171 - m.x221 - m.x271 >= -2)

m.c292 = Constraint(expr= - 2*m.x70 + m.x172 - m.x222 - m.x272 >= -2)

m.c293 = Constraint(expr= - 2*m.x71 + m.x173 - m.x223 - m.x273 >= -2)

m.c294 = Constraint(expr= - 2*m.x71 + m.x174 - m.x224 - m.x274 >= -2)

m.c295 = Constraint(expr= - 2*m.x71 + m.x175 - m.x225 - m.x275 >= -2)

m.c296 = Constraint(expr= - 2*m.x71 + m.x176 - m.x226 - m.x276 >= -2)

m.c297 = Constraint(expr= - 2*m.x71 + m.x177 - m.x227 - m.x277 >= -2)

m.c298 = Constraint(expr= - 2*m.x72 + m.x178 - m.x228 - m.x278 >= -2)

m.c299 = Constraint(expr= - 2*m.x72 + m.x179 - m.x229 - m.x279 >= -2)

m.c300 = Constraint(expr= - 2*m.x72 + m.x180 - m.x230 - m.x280 >= -2)

m.c301 = Constraint(expr= - 2*m.x72 + m.x181 - m.x231 - m.x281 >= -2)

m.c302 = Constraint(expr= - 2*m.x72 + m.x182 - m.x232 - m.x282 >= -2)

m.c303 = Constraint(expr= - 2*m.x73 + m.x183 - m.x233 - m.x283 >= -2)

m.c304 = Constraint(expr= - 2*m.x73 + m.x184 - m.x234 - m.x284 >= -2)

m.c305 = Constraint(expr= - 2*m.x73 + m.x185 - m.x235 - m.x285 >= -2)

m.c306 = Constraint(expr= - 2*m.x73 + m.x186 - m.x236 - m.x286 >= -2)

m.c307 = Constraint(expr= - 2*m.x73 + m.x187 - m.x237 - m.x287 >= -2)

m.c308 = Constraint(expr= - 2*m.x74 + m.x188 - m.x238 - m.x288 >= -2)

m.c309 = Constraint(expr= - 2*m.x74 + m.x189 - m.x239 - m.x289 >= -2)

m.c310 = Constraint(expr= - 2*m.x74 + m.x190 - m.x240 - m.x290 >= -2)

m.c311 = Constraint(expr= - 2*m.x74 + m.x191 - m.x241 - m.x291 >= -2)

m.c312 = Constraint(expr= - 2*m.x74 + m.x192 - m.x242 - m.x292 >= -2)

m.c313 = Constraint(expr= - 2*m.x75 + m.x193 - m.x243 - m.x293 >= -2)

m.c314 = Constraint(expr= - 2*m.x75 + m.x194 - m.x244 - m.x294 >= -2)

m.c315 = Constraint(expr= - 2*m.x75 + m.x195 - m.x245 - m.x295 >= -2)

m.c316 = Constraint(expr= - 2*m.x75 + m.x196 - m.x246 - m.x296 >= -2)

m.c317 = Constraint(expr= - 2*m.x75 + m.x197 - m.x247 - m.x297 >= -2)

m.c318 = Constraint(expr=   m.x118 - m.x148 - m.x149 - m.x150 - m.x151 - m.x152 == 0)

m.c319 = Constraint(expr=   m.x119 - m.x153 - m.x154 - m.x155 - m.x156 - m.x157 == 0)

m.c320 = Constraint(expr=   m.x120 - m.x158 - m.x159 - m.x160 - m.x161 - m.x162 == 0)

m.c321 = Constraint(expr=   m.x121 - m.x163 - m.x164 - m.x165 - m.x166 - m.x167 == 0)

m.c322 = Constraint(expr=   m.x122 - m.x168 - m.x169 - m.x170 - m.x171 - m.x172 == 0)

m.c323 = Constraint(expr=   m.x123 - m.x173 - m.x174 - m.x175 - m.x176 - m.x177 == 0)

m.c324 = Constraint(expr=   m.x124 - m.x178 - m.x179 - m.x180 - m.x181 - m.x182 == 0)

m.c325 = Constraint(expr=   m.x125 - m.x183 - m.x184 - m.x185 - m.x186 - m.x187 == 0)

m.c326 = Constraint(expr=   m.x126 - m.x188 - m.x189 - m.x190 - m.x191 - m.x192 == 0)

m.c327 = Constraint(expr=   m.x127 - m.x193 - m.x194 - m.x195 - m.x196 - m.x197 == 0)

m.c328 = Constraint(expr=   m.x128 - m.x198 - m.x199 - m.x200 - m.x201 - m.x202 == 0)

m.c329 = Constraint(expr=   m.x129 - m.x203 - m.x204 - m.x205 - m.x206 - m.x207 == 0)

m.c330 = Constraint(expr=   m.x130 - m.x208 - m.x209 - m.x210 - m.x211 - m.x212 == 0)

m.c331 = Constraint(expr=   m.x131 - m.x213 - m.x214 - m.x215 - m.x216 - m.x217 == 0)

m.c332 = Constraint(expr=   m.x132 - m.x218 - m.x219 - m.x220 - m.x221 - m.x222 == 0)

m.c333 = Constraint(expr=   m.x133 - m.x223 - m.x224 - m.x225 - m.x226 - m.x227 == 0)

m.c334 = Constraint(expr=   m.x134 - m.x228 - m.x229 - m.x230 - m.x231 - m.x232 == 0)

m.c335 = Constraint(expr=   m.x135 - m.x233 - m.x234 - m.x235 - m.x236 - m.x237 == 0)

m.c336 = Constraint(expr=   m.x136 - m.x238 - m.x239 - m.x240 - m.x241 - m.x242 == 0)

m.c337 = Constraint(expr=   m.x137 - m.x243 - m.x244 - m.x245 - m.x246 - m.x247 == 0)

m.c338 = Constraint(expr=   m.x138 - m.x248 - m.x249 - m.x250 - m.x251 - m.x252 == 0)

m.c339 = Constraint(expr=   m.x139 - m.x253 - m.x254 - m.x255 - m.x256 - m.x257 == 0)

m.c340 = Constraint(expr=   m.x140 - m.x258 - m.x259 - m.x260 - m.x261 - m.x262 == 0)

m.c341 = Constraint(expr=   m.x141 - m.x263 - m.x264 - m.x265 - m.x266 - m.x267 == 0)

m.c342 = Constraint(expr=   m.x142 - m.x268 - m.x269 - m.x270 - m.x271 - m.x272 == 0)

m.c343 = Constraint(expr=   m.x143 - m.x273 - m.x274 - m.x275 - m.x276 - m.x277 == 0)

m.c344 = Constraint(expr=   m.x144 - m.x278 - m.x279 - m.x280 - m.x281 - m.x282 == 0)

m.c345 = Constraint(expr=   m.x145 - m.x283 - m.x284 - m.x285 - m.x286 - m.x287 == 0)

m.c346 = Constraint(expr=   m.x146 - m.x288 - m.x289 - m.x290 - m.x291 - m.x292 == 0)

m.c347 = Constraint(expr=   m.x147 - m.x293 - m.x294 - m.x295 - m.x296 - m.x297 == 0)

m.c348 = Constraint(expr=   10*m.x66 - m.x78 + m.x98 + m.x128 <= 10)

m.c349 = Constraint(expr=   10*m.x67 - m.x79 + m.x99 + m.x129 <= 10)

m.c350 = Constraint(expr=   10*m.x68 - m.x80 + m.x100 + m.x130 <= 10)

m.c351 = Constraint(expr=   10*m.x69 - m.x81 + m.x101 + m.x131 <= 10)

m.c352 = Constraint(expr=   10*m.x70 - m.x82 + m.x102 + m.x132 <= 10)

m.c353 = Constraint(expr=   10*m.x71 - m.x83 + m.x103 + m.x133 <= 10)

m.c354 = Constraint(expr=   10*m.x72 - m.x84 + m.x104 + m.x134 <= 10)

m.c355 = Constraint(expr=   10*m.x73 - m.x85 + m.x105 + m.x135 <= 10)

m.c356 = Constraint(expr=   10*m.x74 - m.x86 + m.x106 + m.x136 <= 10)

m.c357 = Constraint(expr=   10*m.x75 - m.x87 + m.x107 + m.x137 <= 10)

m.c358 = Constraint(expr= - 10*m.x66 - m.x78 + m.x98 + m.x128 >= -10)

m.c359 = Constraint(expr= - 10*m.x67 - m.x79 + m.x99 + m.x129 >= -10)

m.c360 = Constraint(expr= - 10*m.x68 - m.x80 + m.x100 + m.x130 >= -10)

m.c361 = Constraint(expr= - 10*m.x69 - m.x81 + m.x101 + m.x131 >= -10)

m.c362 = Constraint(expr= - 10*m.x70 - m.x82 + m.x102 + m.x132 >= -10)

m.c363 = Constraint(expr= - 10*m.x71 - m.x83 + m.x103 + m.x133 >= -10)

m.c364 = Constraint(expr= - 10*m.x72 - m.x84 + m.x104 + m.x134 >= -10)

m.c365 = Constraint(expr= - 10*m.x73 - m.x85 + m.x105 + m.x135 >= -10)

m.c366 = Constraint(expr= - 10*m.x74 - m.x86 + m.x106 + m.x136 >= -10)

m.c367 = Constraint(expr= - 10*m.x75 - m.x87 + m.x107 + m.x137 >= -10)

m.c368 = Constraint(expr=   10*m.x66 + m.x88 - m.x108 + m.x138 <= 10)

m.c369 = Constraint(expr=   10*m.x67 + m.x89 - m.x109 + m.x139 <= 10)

m.c370 = Constraint(expr=   10*m.x68 + m.x90 - m.x110 + m.x140 <= 10)

m.c371 = Constraint(expr=   10*m.x69 + m.x91 - m.x111 + m.x141 <= 10)

m.c372 = Constraint(expr=   10*m.x70 + m.x92 - m.x112 + m.x142 <= 10)

m.c373 = Constraint(expr=   10*m.x71 + m.x93 - m.x113 + m.x143 <= 10)

m.c374 = Constraint(expr=   10*m.x72 + m.x94 - m.x114 + m.x144 <= 10)

m.c375 = Constraint(expr=   10*m.x73 + m.x95 - m.x115 + m.x145 <= 10)

m.c376 = Constraint(expr=   10*m.x74 + m.x96 - m.x116 + m.x146 <= 10)

m.c377 = Constraint(expr=   10*m.x75 + m.x97 - m.x117 + m.x147 <= 10)

m.c378 = Constraint(expr= - 10*m.x66 + m.x88 - m.x108 + m.x138 >= -10)

m.c379 = Constraint(expr= - 10*m.x67 + m.x89 - m.x109 + m.x139 >= -10)

m.c380 = Constraint(expr= - 10*m.x68 + m.x90 - m.x110 + m.x140 >= -10)

m.c381 = Constraint(expr= - 10*m.x69 + m.x91 - m.x111 + m.x141 >= -10)

m.c382 = Constraint(expr= - 10*m.x70 + m.x92 - m.x112 + m.x142 >= -10)

m.c383 = Constraint(expr= - 10*m.x71 + m.x93 - m.x113 + m.x143 >= -10)

m.c384 = Constraint(expr= - 10*m.x72 + m.x94 - m.x114 + m.x144 >= -10)

m.c385 = Constraint(expr= - 10*m.x73 + m.x95 - m.x115 + m.x145 >= -10)

m.c386 = Constraint(expr= - 10*m.x74 + m.x96 - m.x116 + m.x146 >= -10)

m.c387 = Constraint(expr= - 10*m.x75 + m.x97 - m.x117 + m.x147 >= -10)

m.c388 = Constraint(expr=   m.x153 - m.x198 == 0)

m.c389 = Constraint(expr=   m.x154 - m.x199 == 0)

m.c390 = Constraint(expr=   m.x155 - m.x200 == 0)

m.c391 = Constraint(expr=   m.x156 - m.x201 == 0)

m.c392 = Constraint(expr=   m.x157 - m.x202 == 0)

m.c393 = Constraint(expr=   m.x158 - m.x248 == 0)

m.c394 = Constraint(expr=   m.x159 - m.x249 == 0)

m.c395 = Constraint(expr=   m.x160 - m.x250 == 0)

m.c396 = Constraint(expr=   m.x161 - m.x251 == 0)

m.c397 = Constraint(expr=   m.x162 - m.x252 == 0)

m.c398 = Constraint(expr=   m.x163 - m.x203 == 0)

m.c399 = Constraint(expr=   m.x164 - m.x204 == 0)

m.c400 = Constraint(expr=   m.x165 - m.x205 == 0)

m.c401 = Constraint(expr=   m.x166 - m.x206 == 0)

m.c402 = Constraint(expr=   m.x167 - m.x207 == 0)

m.c403 = Constraint(expr=   m.x168 - m.x208 - m.x253 == 0)

m.c404 = Constraint(expr=   m.x169 - m.x209 - m.x254 == 0)

m.c405 = Constraint(expr=   m.x170 - m.x210 - m.x255 == 0)

m.c406 = Constraint(expr=   m.x171 - m.x211 - m.x256 == 0)

m.c407 = Constraint(expr=   m.x172 - m.x212 - m.x257 == 0)

m.c408 = Constraint(expr=   m.x173 - m.x258 == 0)

m.c409 = Constraint(expr=   m.x174 - m.x259 == 0)

m.c410 = Constraint(expr=   m.x175 - m.x260 == 0)

m.c411 = Constraint(expr=   m.x176 - m.x261 == 0)

m.c412 = Constraint(expr=   m.x177 - m.x262 == 0)

m.c413 = Constraint(expr=   m.x178 - m.x213 == 0)

m.c414 = Constraint(expr=   m.x179 - m.x214 == 0)

m.c415 = Constraint(expr=   m.x180 - m.x215 == 0)

m.c416 = Constraint(expr=   m.x181 - m.x216 == 0)

m.c417 = Constraint(expr=   m.x182 - m.x217 == 0)

m.c418 = Constraint(expr=   m.x183 - m.x218 - m.x263 == 0)

m.c419 = Constraint(expr=   m.x184 - m.x219 - m.x264 == 0)

m.c420 = Constraint(expr=   m.x185 - m.x220 - m.x265 == 0)

m.c421 = Constraint(expr=   m.x186 - m.x221 - m.x266 == 0)

m.c422 = Constraint(expr=   m.x187 - m.x222 - m.x267 == 0)

m.c423 = Constraint(expr=   m.x188 - m.x223 - m.x268 == 0)

m.c424 = Constraint(expr=   m.x189 - m.x224 - m.x269 == 0)

m.c425 = Constraint(expr=   m.x190 - m.x225 - m.x270 == 0)

m.c426 = Constraint(expr=   m.x191 - m.x226 - m.x271 == 0)

m.c427 = Constraint(expr=   m.x192 - m.x227 - m.x272 == 0)

m.c428 = Constraint(expr=   m.x193 - m.x273 == 0)

m.c429 = Constraint(expr=   m.x194 - m.x274 == 0)

m.c430 = Constraint(expr=   m.x195 - m.x275 == 0)

m.c431 = Constraint(expr=   m.x196 - m.x276 == 0)

m.c432 = Constraint(expr=   m.x197 - m.x277 == 0)

m.c433 = Constraint(expr= - 10*m.x52 - m.x78 + m.x79 - m.x89 <= 0)

m.c434 = Constraint(expr= - 10*m.x53 + m.x80 + m.x88 - m.x90 <= 0)

m.c435 = Constraint(expr= - 10*m.x54 - m.x79 + m.x81 - m.x91 <= 0)

m.c436 = Constraint(expr= - 10*m.x55 - m.x80 + m.x82 + m.x89 - m.x92 <= 0)

m.c437 = Constraint(expr= - 10*m.x56 + m.x83 + m.x90 - m.x93 <= 0)

m.c438 = Constraint(expr= - 10*m.x57 - m.x81 + m.x84 - m.x94 <= 0)

m.c439 = Constraint(expr= - 10*m.x58 - m.x82 + m.x85 + m.x91 - m.x95 <= 0)

m.c440 = Constraint(expr= - 10*m.x59 - m.x83 + m.x86 + m.x92 - m.x96 <= 0)

m.c441 = Constraint(expr= - 10*m.x60 + m.x87 + m.x93 - m.x97 <= 0)

m.c442 = Constraint(expr=   10*m.x52 - m.x78 + m.x79 - m.x89 >= 0)

m.c443 = Constraint(expr=   10*m.x53 + m.x80 + m.x88 - m.x90 >= 0)

m.c444 = Constraint(expr=   10*m.x54 - m.x79 + m.x81 - m.x91 >= 0)

m.c445 = Constraint(expr=   10*m.x55 - m.x80 + m.x82 + m.x89 - m.x92 >= 0)

m.c446 = Constraint(expr=   10*m.x56 + m.x83 + m.x90 - m.x93 >= 0)

m.c447 = Constraint(expr=   10*m.x57 - m.x81 + m.x84 - m.x94 >= 0)

m.c448 = Constraint(expr=   10*m.x58 - m.x82 + m.x85 + m.x91 - m.x95 >= 0)

m.c449 = Constraint(expr=   10*m.x59 - m.x83 + m.x86 + m.x92 - m.x96 >= 0)

m.c450 = Constraint(expr=   10*m.x60 + m.x87 + m.x93 - m.x97 >= 0)

m.c451 = Constraint(expr= - 10*m.x52 - m.x98 + m.x99 - m.x109 <= 0)

m.c452 = Constraint(expr= - 10*m.x53 + m.x100 + m.x108 - m.x110 <= 0)

m.c453 = Constraint(expr= - 10*m.x54 - m.x99 + m.x101 - m.x111 <= 0)

m.c454 = Constraint(expr= - 10*m.x55 - m.x100 + m.x102 + m.x109 - m.x112 <= 0)

m.c455 = Constraint(expr= - 10*m.x56 + m.x103 + m.x110 - m.x113 <= 0)

m.c456 = Constraint(expr= - 10*m.x57 - m.x101 + m.x104 - m.x114 <= 0)

m.c457 = Constraint(expr= - 10*m.x58 - m.x102 + m.x105 + m.x111 - m.x115 <= 0)

m.c458 = Constraint(expr= - 10*m.x59 - m.x103 + m.x106 + m.x112 - m.x116 <= 0)

m.c459 = Constraint(expr= - 10*m.x60 + m.x107 + m.x113 - m.x117 <= 0)

m.c460 = Constraint(expr=   10*m.x52 - m.x98 + m.x99 - m.x109 >= 0)

m.c461 = Constraint(expr=   10*m.x53 + m.x100 + m.x108 - m.x110 >= 0)

m.c462 = Constraint(expr=   10*m.x54 - m.x99 + m.x101 - m.x111 >= 0)

m.c463 = Constraint(expr=   10*m.x55 - m.x100 + m.x102 + m.x109 - m.x112 >= 0)

m.c464 = Constraint(expr=   10*m.x56 + m.x103 + m.x110 - m.x113 >= 0)

m.c465 = Constraint(expr=   10*m.x57 - m.x101 + m.x104 - m.x114 >= 0)

m.c466 = Constraint(expr=   10*m.x58 - m.x102 + m.x105 + m.x111 - m.x115 >= 0)

m.c467 = Constraint(expr=   10*m.x59 - m.x103 + m.x106 + m.x112 - m.x116 >= 0)

m.c468 = Constraint(expr=   10*m.x60 + m.x107 + m.x113 - m.x117 >= 0)

m.c469 = Constraint(expr=   10*m.x51 - m.x78 + m.x88 <= 10)

m.c470 = Constraint(expr=   10*m.x52 - m.x79 + m.x89 <= 10)

m.c471 = Constraint(expr=   10*m.x53 - m.x80 + m.x90 <= 10)

m.c472 = Constraint(expr=   10*m.x54 - m.x81 + m.x91 <= 10)

m.c473 = Constraint(expr=   10*m.x55 - m.x82 + m.x92 <= 10)

m.c474 = Constraint(expr=   10*m.x56 - m.x83 + m.x93 <= 10)

m.c475 = Constraint(expr=   10*m.x57 - m.x84 + m.x94 <= 10)

m.c476 = Constraint(expr=   10*m.x58 - m.x85 + m.x95 <= 10)

m.c477 = Constraint(expr=   10*m.x59 - m.x86 + m.x96 <= 10)

m.c478 = Constraint(expr=   10*m.x60 - m.x87 + m.x97 <= 10)

m.c479 = Constraint(expr= - 10*m.x51 - m.x78 + m.x88 >= -10)

m.c480 = Constraint(expr= - 10*m.x52 - m.x79 + m.x89 >= -10)

m.c481 = Constraint(expr= - 10*m.x53 - m.x80 + m.x90 >= -10)

m.c482 = Constraint(expr= - 10*m.x54 - m.x81 + m.x91 >= -10)

m.c483 = Constraint(expr= - 10*m.x55 - m.x82 + m.x92 >= -10)

m.c484 = Constraint(expr= - 10*m.x56 - m.x83 + m.x93 >= -10)

m.c485 = Constraint(expr= - 10*m.x57 - m.x84 + m.x94 >= -10)

m.c486 = Constraint(expr= - 10*m.x58 - m.x85 + m.x95 >= -10)

m.c487 = Constraint(expr= - 10*m.x59 - m.x86 + m.x96 >= -10)

m.c488 = Constraint(expr= - 10*m.x60 - m.x87 + m.x97 >= -10)

m.c489 = Constraint(expr= - 10*m.x67 - m.x78 + m.x79 <= 0)

m.c490 = Constraint(expr= - 10*m.x69 - m.x79 + m.x81 <= 0)

m.c491 = Constraint(expr= - 10*m.x70 - m.x80 + m.x82 <= 0)

m.c492 = Constraint(expr= - 10*m.x72 - m.x81 + m.x84 <= 0)

m.c493 = Constraint(expr= - 10*m.x73 - m.x82 + m.x85 <= 0)

m.c494 = Constraint(expr= - 10*m.x74 - m.x83 + m.x86 <= 0)

m.c495 = Constraint(expr=   10*m.x67 - m.x78 + m.x79 >= 0)

m.c496 = Constraint(expr=   10*m.x69 - m.x79 + m.x81 >= 0)

m.c497 = Constraint(expr=   10*m.x70 - m.x80 + m.x82 >= 0)

m.c498 = Constraint(expr=   10*m.x72 - m.x81 + m.x84 >= 0)

m.c499 = Constraint(expr=   10*m.x73 - m.x82 + m.x85 >= 0)

m.c500 = Constraint(expr=   10*m.x74 - m.x83 + m.x86 >= 0)

m.c501 = Constraint(expr= - 10*m.x67 - m.x98 + m.x99 <= 0)

m.c502 = Constraint(expr= - 10*m.x69 - m.x99 + m.x101 <= 0)

m.c503 = Constraint(expr= - 10*m.x70 - m.x100 + m.x102 <= 0)

m.c504 = Constraint(expr= - 10*m.x72 - m.x101 + m.x104 <= 0)

m.c505 = Constraint(expr= - 10*m.x73 - m.x102 + m.x105 <= 0)

m.c506 = Constraint(expr= - 10*m.x74 - m.x103 + m.x106 <= 0)

m.c507 = Constraint(expr=   10*m.x67 - m.x98 + m.x99 >= 0)

m.c508 = Constraint(expr=   10*m.x69 - m.x99 + m.x101 >= 0)

m.c509 = Constraint(expr=   10*m.x70 - m.x100 + m.x102 >= 0)

m.c510 = Constraint(expr=   10*m.x72 - m.x101 + m.x104 >= 0)

m.c511 = Constraint(expr=   10*m.x73 - m.x102 + m.x105 >= 0)

m.c512 = Constraint(expr=   10*m.x74 - m.x103 + m.x106 >= 0)

m.c513 = Constraint(expr= - 10*m.x68 - m.x108 + m.x110 <= 0)

m.c514 = Constraint(expr= - 10*m.x70 - m.x109 + m.x112 <= 0)

m.c515 = Constraint(expr= - 10*m.x71 - m.x110 + m.x113 <= 0)

m.c516 = Constraint(expr= - 10*m.x73 - m.x111 + m.x115 <= 0)

m.c517 = Constraint(expr= - 10*m.x74 - m.x112 + m.x116 <= 0)

m.c518 = Constraint(expr= - 10*m.x75 - m.x113 + m.x117 <= 0)

m.c519 = Constraint(expr=   10*m.x68 - m.x108 + m.x110 >= 0)

m.c520 = Constraint(expr=   10*m.x70 - m.x109 + m.x112 >= 0)

m.c521 = Constraint(expr=   10*m.x71 - m.x110 + m.x113 >= 0)

m.c522 = Constraint(expr=   10*m.x73 - m.x111 + m.x115 >= 0)

m.c523 = Constraint(expr=   10*m.x74 - m.x112 + m.x116 >= 0)

m.c524 = Constraint(expr=   10*m.x75 - m.x113 + m.x117 >= 0)

m.c525 = Constraint(expr= - 10*m.x68 - m.x88 + m.x90 <= 0)

m.c526 = Constraint(expr= - 10*m.x70 - m.x89 + m.x92 <= 0)

m.c527 = Constraint(expr= - 10*m.x71 - m.x90 + m.x93 <= 0)

m.c528 = Constraint(expr= - 10*m.x73 - m.x91 + m.x95 <= 0)

m.c529 = Constraint(expr= - 10*m.x74 - m.x92 + m.x96 <= 0)

m.c530 = Constraint(expr= - 10*m.x75 - m.x93 + m.x97 <= 0)

m.c531 = Constraint(expr=   10*m.x68 - m.x88 + m.x90 >= 0)

m.c532 = Constraint(expr=   10*m.x70 - m.x89 + m.x92 >= 0)

m.c533 = Constraint(expr=   10*m.x71 - m.x90 + m.x93 >= 0)

m.c534 = Constraint(expr=   10*m.x73 - m.x91 + m.x95 >= 0)

m.c535 = Constraint(expr=   10*m.x74 - m.x92 + m.x96 >= 0)

m.c536 = Constraint(expr=   10*m.x75 - m.x93 + m.x97 >= 0)

m.c537 = Constraint(expr= - 2*m.x67 - m.x198 + m.x203 <= 0)

m.c538 = Constraint(expr= - 2*m.x67 - m.x199 + m.x204 <= 0)

m.c539 = Constraint(expr= - 2*m.x67 - m.x200 + m.x205 <= 0)

m.c540 = Constraint(expr= - 2*m.x67 - m.x201 + m.x206 <= 0)

m.c541 = Constraint(expr= - 2*m.x67 - m.x202 + m.x207 <= 0)

m.c542 = Constraint(expr= - 2*m.x69 - m.x203 + m.x213 <= 0)

m.c543 = Constraint(expr= - 2*m.x69 - m.x204 + m.x214 <= 0)

m.c544 = Constraint(expr= - 2*m.x69 - m.x205 + m.x215 <= 0)

m.c545 = Constraint(expr= - 2*m.x69 - m.x206 + m.x216 <= 0)

m.c546 = Constraint(expr= - 2*m.x69 - m.x207 + m.x217 <= 0)

m.c547 = Constraint(expr= - 2*m.x70 - m.x208 + m.x218 <= 0)

m.c548 = Constraint(expr= - 2*m.x70 - m.x209 + m.x219 <= 0)

m.c549 = Constraint(expr= - 2*m.x70 - m.x210 + m.x220 <= 0)

m.c550 = Constraint(expr= - 2*m.x70 - m.x211 + m.x221 <= 0)

m.c551 = Constraint(expr= - 2*m.x70 - m.x212 + m.x222 <= 0)

m.c552 = Constraint(expr= - 2*m.x72 - m.x213 + m.x228 <= 0)

m.c553 = Constraint(expr= - 2*m.x72 - m.x214 + m.x229 <= 0)

m.c554 = Constraint(expr= - 2*m.x72 - m.x215 + m.x230 <= 0)

m.c555 = Constraint(expr= - 2*m.x72 - m.x216 + m.x231 <= 0)

m.c556 = Constraint(expr= - 2*m.x72 - m.x217 + m.x232 <= 0)

m.c557 = Constraint(expr= - 2*m.x73 - m.x218 + m.x233 <= 0)

m.c558 = Constraint(expr= - 2*m.x73 - m.x219 + m.x234 <= 0)

m.c559 = Constraint(expr= - 2*m.x73 - m.x220 + m.x235 <= 0)

m.c560 = Constraint(expr= - 2*m.x73 - m.x221 + m.x236 <= 0)

m.c561 = Constraint(expr= - 2*m.x73 - m.x222 + m.x237 <= 0)

m.c562 = Constraint(expr= - 2*m.x74 - m.x223 + m.x238 <= 0)

m.c563 = Constraint(expr= - 2*m.x74 - m.x224 + m.x239 <= 0)

m.c564 = Constraint(expr= - 2*m.x74 - m.x225 + m.x240 <= 0)

m.c565 = Constraint(expr= - 2*m.x74 - m.x226 + m.x241 <= 0)

m.c566 = Constraint(expr= - 2*m.x74 - m.x227 + m.x242 <= 0)

m.c567 = Constraint(expr=   2*m.x67 - m.x198 + m.x203 >= 0)

m.c568 = Constraint(expr=   2*m.x67 - m.x199 + m.x204 >= 0)

m.c569 = Constraint(expr=   2*m.x67 - m.x200 + m.x205 >= 0)

m.c570 = Constraint(expr=   2*m.x67 - m.x201 + m.x206 >= 0)

m.c571 = Constraint(expr=   2*m.x67 - m.x202 + m.x207 >= 0)

m.c572 = Constraint(expr=   2*m.x69 - m.x203 + m.x213 >= 0)

m.c573 = Constraint(expr=   2*m.x69 - m.x204 + m.x214 >= 0)

m.c574 = Constraint(expr=   2*m.x69 - m.x205 + m.x215 >= 0)

m.c575 = Constraint(expr=   2*m.x69 - m.x206 + m.x216 >= 0)

m.c576 = Constraint(expr=   2*m.x69 - m.x207 + m.x217 >= 0)

m.c577 = Constraint(expr=   2*m.x70 - m.x208 + m.x218 >= 0)

m.c578 = Constraint(expr=   2*m.x70 - m.x209 + m.x219 >= 0)

m.c579 = Constraint(expr=   2*m.x70 - m.x210 + m.x220 >= 0)

m.c580 = Constraint(expr=   2*m.x70 - m.x211 + m.x221 >= 0)

m.c581 = Constraint(expr=   2*m.x70 - m.x212 + m.x222 >= 0)

m.c582 = Constraint(expr=   2*m.x72 - m.x213 + m.x228 >= 0)

m.c583 = Constraint(expr=   2*m.x72 - m.x214 + m.x229 >= 0)

m.c584 = Constraint(expr=   2*m.x72 - m.x215 + m.x230 >= 0)

m.c585 = Constraint(expr=   2*m.x72 - m.x216 + m.x231 >= 0)

m.c586 = Constraint(expr=   2*m.x72 - m.x217 + m.x232 >= 0)

m.c587 = Constraint(expr=   2*m.x73 - m.x218 + m.x233 >= 0)

m.c588 = Constraint(expr=   2*m.x73 - m.x219 + m.x234 >= 0)

m.c589 = Constraint(expr=   2*m.x73 - m.x220 + m.x235 >= 0)

m.c590 = Constraint(expr=   2*m.x73 - m.x221 + m.x236 >= 0)

m.c591 = Constraint(expr=   2*m.x73 - m.x222 + m.x237 >= 0)

m.c592 = Constraint(expr=   2*m.x74 - m.x223 + m.x238 >= 0)

m.c593 = Constraint(expr=   2*m.x74 - m.x224 + m.x239 >= 0)

m.c594 = Constraint(expr=   2*m.x74 - m.x225 + m.x240 >= 0)

m.c595 = Constraint(expr=   2*m.x74 - m.x226 + m.x241 >= 0)

m.c596 = Constraint(expr=   2*m.x74 - m.x227 + m.x242 >= 0)

m.c597 = Constraint(expr= - 2*m.x68 - m.x248 + m.x258 <= 0)

m.c598 = Constraint(expr= - 2*m.x68 - m.x249 + m.x259 <= 0)

m.c599 = Constraint(expr= - 2*m.x68 - m.x250 + m.x260 <= 0)

m.c600 = Constraint(expr= - 2*m.x68 - m.x251 + m.x261 <= 0)

m.c601 = Constraint(expr= - 2*m.x68 - m.x252 + m.x262 <= 0)

m.c602 = Constraint(expr= - 2*m.x70 - m.x253 + m.x268 <= 0)

m.c603 = Constraint(expr= - 2*m.x70 - m.x254 + m.x269 <= 0)

m.c604 = Constraint(expr= - 2*m.x70 - m.x255 + m.x270 <= 0)

m.c605 = Constraint(expr= - 2*m.x70 - m.x256 + m.x271 <= 0)

m.c606 = Constraint(expr= - 2*m.x70 - m.x257 + m.x272 <= 0)

m.c607 = Constraint(expr= - 2*m.x71 - m.x258 + m.x273 <= 0)

m.c608 = Constraint(expr= - 2*m.x71 - m.x259 + m.x274 <= 0)

m.c609 = Constraint(expr= - 2*m.x71 - m.x260 + m.x275 <= 0)

m.c610 = Constraint(expr= - 2*m.x71 - m.x261 + m.x276 <= 0)

m.c611 = Constraint(expr= - 2*m.x71 - m.x262 + m.x277 <= 0)

m.c612 = Constraint(expr= - 2*m.x73 - m.x263 + m.x283 <= 0)

m.c613 = Constraint(expr= - 2*m.x73 - m.x264 + m.x284 <= 0)

m.c614 = Constraint(expr= - 2*m.x73 - m.x265 + m.x285 <= 0)

m.c615 = Constraint(expr= - 2*m.x73 - m.x266 + m.x286 <= 0)

m.c616 = Constraint(expr= - 2*m.x73 - m.x267 + m.x287 <= 0)

m.c617 = Constraint(expr= - 2*m.x74 - m.x268 + m.x288 <= 0)

m.c618 = Constraint(expr= - 2*m.x74 - m.x269 + m.x289 <= 0)

m.c619 = Constraint(expr= - 2*m.x74 - m.x270 + m.x290 <= 0)

m.c620 = Constraint(expr= - 2*m.x74 - m.x271 + m.x291 <= 0)

m.c621 = Constraint(expr= - 2*m.x74 - m.x272 + m.x292 <= 0)

m.c622 = Constraint(expr= - 2*m.x75 - m.x273 + m.x293 <= 0)

m.c623 = Constraint(expr= - 2*m.x75 - m.x274 + m.x294 <= 0)

m.c624 = Constraint(expr= - 2*m.x75 - m.x275 + m.x295 <= 0)

m.c625 = Constraint(expr= - 2*m.x75 - m.x276 + m.x296 <= 0)

m.c626 = Constraint(expr= - 2*m.x75 - m.x277 + m.x297 <= 0)

m.c627 = Constraint(expr=   2*m.x68 - m.x248 + m.x258 >= 0)

m.c628 = Constraint(expr=   2*m.x68 - m.x249 + m.x259 >= 0)

m.c629 = Constraint(expr=   2*m.x68 - m.x250 + m.x260 >= 0)

m.c630 = Constraint(expr=   2*m.x68 - m.x251 + m.x261 >= 0)

m.c631 = Constraint(expr=   2*m.x68 - m.x252 + m.x262 >= 0)

m.c632 = Constraint(expr=   2*m.x70 - m.x253 + m.x268 >= 0)

m.c633 = Constraint(expr=   2*m.x70 - m.x254 + m.x269 >= 0)

m.c634 = Constraint(expr=   2*m.x70 - m.x255 + m.x270 >= 0)

m.c635 = Constraint(expr=   2*m.x70 - m.x256 + m.x271 >= 0)

m.c636 = Constraint(expr=   2*m.x70 - m.x257 + m.x272 >= 0)

m.c637 = Constraint(expr=   2*m.x71 - m.x258 + m.x273 >= 0)

m.c638 = Constraint(expr=   2*m.x71 - m.x259 + m.x274 >= 0)

m.c639 = Constraint(expr=   2*m.x71 - m.x260 + m.x275 >= 0)

m.c640 = Constraint(expr=   2*m.x71 - m.x261 + m.x276 >= 0)

m.c641 = Constraint(expr=   2*m.x71 - m.x262 + m.x277 >= 0)

m.c642 = Constraint(expr=   2*m.x73 - m.x263 + m.x283 >= 0)

m.c643 = Constraint(expr=   2*m.x73 - m.x264 + m.x284 >= 0)

m.c644 = Constraint(expr=   2*m.x73 - m.x265 + m.x285 >= 0)

m.c645 = Constraint(expr=   2*m.x73 - m.x266 + m.x286 >= 0)

m.c646 = Constraint(expr=   2*m.x73 - m.x267 + m.x287 >= 0)

m.c647 = Constraint(expr=   2*m.x74 - m.x268 + m.x288 >= 0)

m.c648 = Constraint(expr=   2*m.x74 - m.x269 + m.x289 >= 0)

m.c649 = Constraint(expr=   2*m.x74 - m.x270 + m.x290 >= 0)

m.c650 = Constraint(expr=   2*m.x74 - m.x271 + m.x291 >= 0)

m.c651 = Constraint(expr=   2*m.x74 - m.x272 + m.x292 >= 0)

m.c652 = Constraint(expr=   2*m.x75 - m.x273 + m.x293 >= 0)

m.c653 = Constraint(expr=   2*m.x75 - m.x274 + m.x294 >= 0)

m.c654 = Constraint(expr=   2*m.x75 - m.x275 + m.x295 >= 0)

m.c655 = Constraint(expr=   2*m.x75 - m.x276 + m.x296 >= 0)

m.c656 = Constraint(expr=   2*m.x75 - m.x277 + m.x297 >= 0)

m.c657 = Constraint(expr=   m.x134 == 0.6)

m.c658 = Constraint(expr=   m.x135 + m.x144 == 0.4)

m.c659 = Constraint(expr=   m.x136 + m.x145 == 0.2)

m.c660 = Constraint(expr=   m.x137 + m.x146 == 0.4)

m.c661 = Constraint(expr=   m.x147 == 0.4)

m.c662 = Constraint(expr= - 10*m.x62 - m.x105 + m.x114 <= 0.4)

m.c663 = Constraint(expr=   10*m.x62 - m.x105 + m.x114 >= 0.4)

m.c664 = Constraint(expr= - 10*m.x63 - m.x106 + m.x115 <= 0.2)

m.c665 = Constraint(expr=   10*m.x63 - m.x106 + m.x115 >= 0.2)

m.c666 = Constraint(expr= - 10*m.x64 - m.x107 + m.x116 <= 0.4)

m.c667 = Constraint(expr=   10*m.x64 - m.x107 + m.x116 >= 0.4)

m.c668 = Constraint(expr= - 10*m.x67 + m.x89 <= 0)

m.c669 = Constraint(expr= - 10*m.x69 + m.x91 <= 0)

m.c670 = Constraint(expr= - 10*m.x72 + m.x94 <= 0)

m.c671 = Constraint(expr= - 10*m.x67 + m.x109 <= 0)

m.c672 = Constraint(expr= - 10*m.x69 + m.x111 <= 0)

m.c673 = Constraint(expr= - 10*m.x72 + m.x114 <= 0)

m.c674 = Constraint(expr= - 10*m.x68 + m.x80 <= 0)

m.c675 = Constraint(expr= - 10*m.x71 + m.x83 <= 0)

m.c676 = Constraint(expr= - 10*m.x75 + m.x87 <= 0)

m.c677 = Constraint(expr= - 10*m.x68 + m.x100 <= 0)

m.c678 = Constraint(expr= - 10*m.x71 + m.x103 <= 0)

m.c679 = Constraint(expr= - 10*m.x75 + m.x107 <= 0)

m.c680 = Constraint(expr=   2*m.b1 + m.x148 - m.x198 <= 2)

m.c681 = Constraint(expr=   2*m.b2 + m.x148 - m.x198 <= 2)

m.c682 = Constraint(expr=   2*m.b3 + m.x148 - m.x198 <= 2)

m.c683 = Constraint(expr=   2*m.b3 + m.x149 - m.x199 <= 2)

m.c684 = Constraint(expr=   2*m.b4 + m.x148 - m.x198 <= 2)

m.c685 = Constraint(expr=   2*m.b5 + m.x148 - m.x198 <= 2)

m.c686 = Constraint(expr=   2*m.b5 + m.x149 - m.x199 <= 2)

m.c687 = Constraint(expr=   2*m.b6 + m.x148 - m.x198 <= 2)

m.c688 = Constraint(expr=   2*m.b6 + m.x149 - m.x199 <= 2)

m.c689 = Constraint(expr=   2*m.b6 + m.x150 - m.x200 <= 2)

m.c690 = Constraint(expr=   2*m.b7 + m.x148 - m.x198 <= 2)

m.c691 = Constraint(expr=   2*m.b8 + m.x148 - m.x198 <= 2)

m.c692 = Constraint(expr=   2*m.b8 + m.x149 - m.x199 <= 2)

m.c693 = Constraint(expr=   2*m.b9 + m.x148 - m.x198 <= 2)

m.c694 = Constraint(expr=   2*m.b9 + m.x149 - m.x199 <= 2)

m.c695 = Constraint(expr=   2*m.b9 + m.x150 - m.x200 <= 2)

m.c696 = Constraint(expr=   2*m.b10 + m.x148 - m.x198 <= 2)

m.c697 = Constraint(expr=   2*m.b10 + m.x149 - m.x199 <= 2)

m.c698 = Constraint(expr=   2*m.b10 + m.x150 - m.x200 <= 2)

m.c699 = Constraint(expr=   2*m.b10 + m.x151 - m.x201 <= 2)

m.c700 = Constraint(expr=   2*m.b11 + m.x153 - m.x203 <= 2)

m.c701 = Constraint(expr=   2*m.b12 + m.x153 - m.x203 <= 2)

m.c702 = Constraint(expr=   2*m.b13 + m.x153 - m.x203 <= 2)

m.c703 = Constraint(expr=   2*m.b13 + m.x154 - m.x204 <= 2)

m.c704 = Constraint(expr=   2*m.b14 + m.x153 - m.x203 <= 2)

m.c705 = Constraint(expr=   2*m.b15 + m.x153 - m.x203 <= 2)

m.c706 = Constraint(expr=   2*m.b15 + m.x154 - m.x204 <= 2)

m.c707 = Constraint(expr=   2*m.b16 + m.x153 - m.x203 <= 2)

m.c708 = Constraint(expr=   2*m.b16 + m.x154 - m.x204 <= 2)

m.c709 = Constraint(expr=   2*m.b16 + m.x155 - m.x205 <= 2)

m.c710 = Constraint(expr=   2*m.b17 + m.x158 - m.x208 <= 2)

m.c711 = Constraint(expr=   2*m.b17 + m.x159 - m.x209 <= 2)

m.c712 = Constraint(expr=   2*m.b18 + m.x158 - m.x208 <= 2)

m.c713 = Constraint(expr=   2*m.b18 + m.x159 - m.x209 <= 2)

m.c714 = Constraint(expr=   2*m.b19 + m.x158 - m.x208 <= 2)

m.c715 = Constraint(expr=   2*m.b19 + m.x159 - m.x209 <= 2)

m.c716 = Constraint(expr=   2*m.b19 + m.x160 - m.x210 <= 2)

m.c717 = Constraint(expr=   2*m.b20 + m.x158 - m.x208 <= 2)

m.c718 = Constraint(expr=   2*m.b20 + m.x159 - m.x209 <= 2)

m.c719 = Constraint(expr=   2*m.b21 + m.x158 - m.x208 <= 2)

m.c720 = Constraint(expr=   2*m.b21 + m.x159 - m.x209 <= 2)

m.c721 = Constraint(expr=   2*m.b21 + m.x160 - m.x210 <= 2)

m.c722 = Constraint(expr=   2*m.b22 + m.x158 - m.x208 <= 2)

m.c723 = Constraint(expr=   2*m.b22 + m.x159 - m.x209 <= 2)

m.c724 = Constraint(expr=   2*m.b22 + m.x160 - m.x210 <= 2)

m.c725 = Constraint(expr=   2*m.b22 + m.x161 - m.x211 <= 2)

m.c726 = Constraint(expr=   2*m.b23 + m.x163 - m.x213 <= 2)

m.c727 = Constraint(expr=   2*m.b24 + m.x163 - m.x213 <= 2)

m.c728 = Constraint(expr=   2*m.b25 + m.x163 - m.x213 <= 2)

m.c729 = Constraint(expr=   2*m.b25 + m.x164 - m.x214 <= 2)

m.c730 = Constraint(expr=   2*m.b26 + m.x168 - m.x218 <= 2)

m.c731 = Constraint(expr=   2*m.b26 + m.x169 - m.x219 <= 2)

m.c732 = Constraint(expr=   2*m.b27 + m.x168 - m.x218 <= 2)

m.c733 = Constraint(expr=   2*m.b27 + m.x169 - m.x219 <= 2)

m.c734 = Constraint(expr=   2*m.b28 + m.x168 - m.x218 <= 2)

m.c735 = Constraint(expr=   2*m.b28 + m.x169 - m.x219 <= 2)

m.c736 = Constraint(expr=   2*m.b28 + m.x170 - m.x220 <= 2)

m.c737 = Constraint(expr=   2*m.b29 + m.x173 - m.x223 <= 2)

m.c738 = Constraint(expr=   2*m.b29 + m.x174 - m.x224 <= 2)

m.c739 = Constraint(expr=   2*m.b29 + m.x175 - m.x225 <= 2)

m.c740 = Constraint(expr=   2*m.b30 + m.x173 - m.x223 <= 2)

m.c741 = Constraint(expr=   2*m.b30 + m.x174 - m.x224 <= 2)

m.c742 = Constraint(expr=   2*m.b30 + m.x175 - m.x225 <= 2)

m.c743 = Constraint(expr=   2*m.b31 + m.x173 - m.x223 <= 2)

m.c744 = Constraint(expr=   2*m.b31 + m.x174 - m.x224 <= 2)

m.c745 = Constraint(expr=   2*m.b31 + m.x175 - m.x225 <= 2)

m.c746 = Constraint(expr=   2*m.b31 + m.x176 - m.x226 <= 2)

m.c747 = Constraint(expr=   2*m.b32 + m.x178 - m.x228 <= 2)

m.c748 = Constraint(expr=   2*m.b33 + m.x183 - m.x233 <= 2)

m.c749 = Constraint(expr=   2*m.b33 + m.x184 - m.x234 <= 2)

m.c750 = Constraint(expr=   2*m.b34 + m.x188 - m.x238 <= 2)

m.c751 = Constraint(expr=   2*m.b34 + m.x189 - m.x239 <= 2)

m.c752 = Constraint(expr=   2*m.b34 + m.x190 - m.x240 <= 2)

m.c753 = Constraint(expr=   2*m.b35 + m.x193 - m.x243 <= 2)

m.c754 = Constraint(expr=   2*m.b35 + m.x194 - m.x244 <= 2)

m.c755 = Constraint(expr=   2*m.b35 + m.x195 - m.x245 <= 2)

m.c756 = Constraint(expr=   2*m.b35 + m.x196 - m.x246 <= 2)

m.c757 = Constraint(expr= - 2*m.b1 + m.x148 - m.x198 >= -2)

m.c758 = Constraint(expr= - 2*m.b2 + m.x148 - m.x198 >= -2)

m.c759 = Constraint(expr= - 2*m.b3 + m.x148 - m.x198 >= -2)

m.c760 = Constraint(expr= - 2*m.b3 + m.x149 - m.x199 >= -2)

m.c761 = Constraint(expr= - 2*m.b4 + m.x148 - m.x198 >= -2)

m.c762 = Constraint(expr= - 2*m.b5 + m.x148 - m.x198 >= -2)

m.c763 = Constraint(expr= - 2*m.b5 + m.x149 - m.x199 >= -2)

m.c764 = Constraint(expr= - 2*m.b6 + m.x148 - m.x198 >= -2)

m.c765 = Constraint(expr= - 2*m.b6 + m.x149 - m.x199 >= -2)

m.c766 = Constraint(expr= - 2*m.b6 + m.x150 - m.x200 >= -2)

m.c767 = Constraint(expr= - 2*m.b7 + m.x148 - m.x198 >= -2)

m.c768 = Constraint(expr= - 2*m.b8 + m.x148 - m.x198 >= -2)

m.c769 = Constraint(expr= - 2*m.b8 + m.x149 - m.x199 >= -2)

m.c770 = Constraint(expr= - 2*m.b9 + m.x148 - m.x198 >= -2)

m.c771 = Constraint(expr= - 2*m.b9 + m.x149 - m.x199 >= -2)

m.c772 = Constraint(expr= - 2*m.b9 + m.x150 - m.x200 >= -2)

m.c773 = Constraint(expr= - 2*m.b10 + m.x148 - m.x198 >= -2)

m.c774 = Constraint(expr= - 2*m.b10 + m.x149 - m.x199 >= -2)

m.c775 = Constraint(expr= - 2*m.b10 + m.x150 - m.x200 >= -2)

m.c776 = Constraint(expr= - 2*m.b10 + m.x151 - m.x201 >= -2)

m.c777 = Constraint(expr= - 2*m.b11 + m.x153 - m.x203 >= -2)

m.c778 = Constraint(expr= - 2*m.b12 + m.x153 - m.x203 >= -2)

m.c779 = Constraint(expr= - 2*m.b13 + m.x153 - m.x203 >= -2)

m.c780 = Constraint(expr= - 2*m.b13 + m.x154 - m.x204 >= -2)

m.c781 = Constraint(expr= - 2*m.b14 + m.x153 - m.x203 >= -2)

m.c782 = Constraint(expr= - 2*m.b15 + m.x153 - m.x203 >= -2)

m.c783 = Constraint(expr= - 2*m.b15 + m.x154 - m.x204 >= -2)

m.c784 = Constraint(expr= - 2*m.b16 + m.x153 - m.x203 >= -2)

m.c785 = Constraint(expr= - 2*m.b16 + m.x154 - m.x204 >= -2)

m.c786 = Constraint(expr= - 2*m.b16 + m.x155 - m.x205 >= -2)

m.c787 = Constraint(expr= - 2*m.b17 + m.x158 - m.x208 >= -2)

m.c788 = Constraint(expr= - 2*m.b17 + m.x159 - m.x209 >= -2)

m.c789 = Constraint(expr= - 2*m.b18 + m.x158 - m.x208 >= -2)

m.c790 = Constraint(expr= - 2*m.b18 + m.x159 - m.x209 >= -2)

m.c791 = Constraint(expr= - 2*m.b19 + m.x158 - m.x208 >= -2)

m.c792 = Constraint(expr= - 2*m.b19 + m.x159 - m.x209 >= -2)

m.c793 = Constraint(expr= - 2*m.b19 + m.x160 - m.x210 >= -2)

m.c794 = Constraint(expr= - 2*m.b20 + m.x158 - m.x208 >= -2)

m.c795 = Constraint(expr= - 2*m.b20 + m.x159 - m.x209 >= -2)

m.c796 = Constraint(expr= - 2*m.b21 + m.x158 - m.x208 >= -2)

m.c797 = Constraint(expr= - 2*m.b21 + m.x159 - m.x209 >= -2)

m.c798 = Constraint(expr= - 2*m.b21 + m.x160 - m.x210 >= -2)

m.c799 = Constraint(expr= - 2*m.b22 + m.x158 - m.x208 >= -2)

m.c800 = Constraint(expr= - 2*m.b22 + m.x159 - m.x209 >= -2)

m.c801 = Constraint(expr= - 2*m.b22 + m.x160 - m.x210 >= -2)

m.c802 = Constraint(expr= - 2*m.b22 + m.x161 - m.x211 >= -2)

m.c803 = Constraint(expr= - 2*m.b23 + m.x163 - m.x213 >= -2)

m.c804 = Constraint(expr= - 2*m.b24 + m.x163 - m.x213 >= -2)

m.c805 = Constraint(expr= - 2*m.b25 + m.x163 - m.x213 >= -2)

m.c806 = Constraint(expr= - 2*m.b25 + m.x164 - m.x214 >= -2)

m.c807 = Constraint(expr= - 2*m.b26 + m.x168 - m.x218 >= -2)

m.c808 = Constraint(expr= - 2*m.b26 + m.x169 - m.x219 >= -2)

m.c809 = Constraint(expr= - 2*m.b27 + m.x168 - m.x218 >= -2)

m.c810 = Constraint(expr= - 2*m.b27 + m.x169 - m.x219 >= -2)

m.c811 = Constraint(expr= - 2*m.b28 + m.x168 - m.x218 >= -2)

m.c812 = Constraint(expr= - 2*m.b28 + m.x169 - m.x219 >= -2)

m.c813 = Constraint(expr= - 2*m.b28 + m.x170 - m.x220 >= -2)

m.c814 = Constraint(expr= - 2*m.b29 + m.x173 - m.x223 >= -2)

m.c815 = Constraint(expr= - 2*m.b29 + m.x174 - m.x224 >= -2)

m.c816 = Constraint(expr= - 2*m.b29 + m.x175 - m.x225 >= -2)

m.c817 = Constraint(expr= - 2*m.b30 + m.x173 - m.x223 >= -2)

m.c818 = Constraint(expr= - 2*m.b30 + m.x174 - m.x224 >= -2)

m.c819 = Constraint(expr= - 2*m.b30 + m.x175 - m.x225 >= -2)

m.c820 = Constraint(expr= - 2*m.b31 + m.x173 - m.x223 >= -2)

m.c821 = Constraint(expr= - 2*m.b31 + m.x174 - m.x224 >= -2)

m.c822 = Constraint(expr= - 2*m.b31 + m.x175 - m.x225 >= -2)

m.c823 = Constraint(expr= - 2*m.b31 + m.x176 - m.x226 >= -2)

m.c824 = Constraint(expr= - 2*m.b32 + m.x178 - m.x228 >= -2)

m.c825 = Constraint(expr= - 2*m.b33 + m.x183 - m.x233 >= -2)

m.c826 = Constraint(expr= - 2*m.b33 + m.x184 - m.x234 >= -2)

m.c827 = Constraint(expr= - 2*m.b34 + m.x188 - m.x238 >= -2)

m.c828 = Constraint(expr= - 2*m.b34 + m.x189 - m.x239 >= -2)

m.c829 = Constraint(expr= - 2*m.b34 + m.x190 - m.x240 >= -2)

m.c830 = Constraint(expr= - 2*m.b35 + m.x193 - m.x243 >= -2)

m.c831 = Constraint(expr= - 2*m.b35 + m.x194 - m.x244 >= -2)

m.c832 = Constraint(expr= - 2*m.b35 + m.x195 - m.x245 >= -2)

m.c833 = Constraint(expr= - 2*m.b35 + m.x196 - m.x246 >= -2)

m.c834 = Constraint(expr=   2*m.b1 + m.x199 <= 2)

m.c835 = Constraint(expr=   2*m.b1 + m.x200 <= 2)

m.c836 = Constraint(expr=   2*m.b1 + m.x201 <= 2)

m.c837 = Constraint(expr=   2*m.b1 + m.x202 <= 2)

m.c838 = Constraint(expr=   2*m.b2 + m.x200 <= 2)

m.c839 = Constraint(expr=   2*m.b2 + m.x201 <= 2)

m.c840 = Constraint(expr=   2*m.b2 + m.x202 <= 2)

m.c841 = Constraint(expr=   2*m.b3 + m.x200 <= 2)

m.c842 = Constraint(expr=   2*m.b3 + m.x201 <= 2)

m.c843 = Constraint(expr=   2*m.b3 + m.x202 <= 2)

m.c844 = Constraint(expr=   2*m.b4 + m.x201 <= 2)

m.c845 = Constraint(expr=   2*m.b4 + m.x202 <= 2)

m.c846 = Constraint(expr=   2*m.b5 + m.x201 <= 2)

m.c847 = Constraint(expr=   2*m.b5 + m.x202 <= 2)

m.c848 = Constraint(expr=   2*m.b6 + m.x201 <= 2)

m.c849 = Constraint(expr=   2*m.b6 + m.x202 <= 2)

m.c850 = Constraint(expr=   2*m.b7 + m.x202 <= 2)

m.c851 = Constraint(expr=   2*m.b8 + m.x202 <= 2)

m.c852 = Constraint(expr=   2*m.b9 + m.x202 <= 2)

m.c853 = Constraint(expr=   2*m.b10 + m.x202 <= 2)

m.c854 = Constraint(expr=   2*m.b11 + m.x204 <= 2)

m.c855 = Constraint(expr=   2*m.b11 + m.x205 <= 2)

m.c856 = Constraint(expr=   2*m.b11 + m.x206 <= 2)

m.c857 = Constraint(expr=   2*m.b11 + m.x207 <= 2)

m.c858 = Constraint(expr=   2*m.b12 + m.x205 <= 2)

m.c859 = Constraint(expr=   2*m.b12 + m.x206 <= 2)

m.c860 = Constraint(expr=   2*m.b12 + m.x207 <= 2)

m.c861 = Constraint(expr=   2*m.b13 + m.x205 <= 2)

m.c862 = Constraint(expr=   2*m.b13 + m.x206 <= 2)

m.c863 = Constraint(expr=   2*m.b13 + m.x207 <= 2)

m.c864 = Constraint(expr=   2*m.b14 + m.x206 <= 2)

m.c865 = Constraint(expr=   2*m.b14 + m.x207 <= 2)

m.c866 = Constraint(expr=   2*m.b15 + m.x206 <= 2)

m.c867 = Constraint(expr=   2*m.b15 + m.x207 <= 2)

m.c868 = Constraint(expr=   2*m.b16 + m.x206 <= 2)

m.c869 = Constraint(expr=   2*m.b16 + m.x207 <= 2)

m.c870 = Constraint(expr=   2*m.b17 + m.x210 <= 2)

m.c871 = Constraint(expr=   2*m.b17 + m.x211 <= 2)

m.c872 = Constraint(expr=   2*m.b17 + m.x212 <= 2)

m.c873 = Constraint(expr=   2*m.b18 + m.x211 <= 2)

m.c874 = Constraint(expr=   2*m.b18 + m.x212 <= 2)

m.c875 = Constraint(expr=   2*m.b19 + m.x211 <= 2)

m.c876 = Constraint(expr=   2*m.b19 + m.x212 <= 2)

m.c877 = Constraint(expr=   2*m.b20 + m.x212 <= 2)

m.c878 = Constraint(expr=   2*m.b21 + m.x212 <= 2)

m.c879 = Constraint(expr=   2*m.b22 + m.x212 <= 2)

m.c880 = Constraint(expr=   2*m.b23 + m.x214 <= 2)

m.c881 = Constraint(expr=   2*m.b23 + m.x215 <= 2)

m.c882 = Constraint(expr=   2*m.b23 + m.x216 <= 2)

m.c883 = Constraint(expr=   2*m.b23 + m.x217 <= 2)

m.c884 = Constraint(expr=   2*m.b24 + m.x215 <= 2)

m.c885 = Constraint(expr=   2*m.b24 + m.x216 <= 2)

m.c886 = Constraint(expr=   2*m.b24 + m.x217 <= 2)

m.c887 = Constraint(expr=   2*m.b25 + m.x215 <= 2)

m.c888 = Constraint(expr=   2*m.b25 + m.x216 <= 2)

m.c889 = Constraint(expr=   2*m.b25 + m.x217 <= 2)

m.c890 = Constraint(expr=   2*m.b26 + m.x220 <= 2)

m.c891 = Constraint(expr=   2*m.b26 + m.x221 <= 2)

m.c892 = Constraint(expr=   2*m.b26 + m.x222 <= 2)

m.c893 = Constraint(expr=   2*m.b27 + m.x221 <= 2)

m.c894 = Constraint(expr=   2*m.b27 + m.x222 <= 2)

m.c895 = Constraint(expr=   2*m.b28 + m.x221 <= 2)

m.c896 = Constraint(expr=   2*m.b28 + m.x222 <= 2)

m.c897 = Constraint(expr=   2*m.b29 + m.x226 <= 2)

m.c898 = Constraint(expr=   2*m.b29 + m.x227 <= 2)

m.c899 = Constraint(expr=   2*m.b30 + m.x227 <= 2)

m.c900 = Constraint(expr=   2*m.b31 + m.x227 <= 2)

m.c901 = Constraint(expr=   2*m.b32 + m.x229 <= 2)

m.c902 = Constraint(expr=   2*m.b32 + m.x230 <= 2)

m.c903 = Constraint(expr=   2*m.b32 + m.x231 <= 2)

m.c904 = Constraint(expr=   2*m.b32 + m.x232 <= 2)

m.c905 = Constraint(expr=   2*m.b33 + m.x235 <= 2)

m.c906 = Constraint(expr=   2*m.b33 + m.x236 <= 2)

m.c907 = Constraint(expr=   2*m.b33 + m.x237 <= 2)

m.c908 = Constraint(expr=   2*m.b34 + m.x241 <= 2)

m.c909 = Constraint(expr=   2*m.b34 + m.x242 <= 2)

m.c910 = Constraint(expr=   2*m.b35 + m.x247 <= 2)

m.c911 = Constraint(expr=1.2*(10.5*m.x148/(10.5 - m.x298) + 4.04*m.x149/(4.04 - m.x298) + 1.76*m.x150/(1.76 - m.x298) + 
                         1.31*m.x151/(1.31 - m.x298) + m.x152/(1 - m.x298)) + 200*m.x66 - m.x78 + m.x88 <= 200)

m.c912 = Constraint(expr=1.2*(10.5*m.x148/(10.5 - m.x299) + 4.04*m.x149/(4.04 - m.x299) + 1.76*m.x150/(1.76 - m.x299) + 
                         1.31*m.x151/(1.31 - m.x299) + m.x152/(1 - m.x299)) + 200*m.x66 - m.x78 + m.x88 <= 200)

m.c913 = Constraint(expr=1.2*(10.5*m.x148/(10.5 - m.x300) + 4.04*m.x149/(4.04 - m.x300) + 1.76*m.x150/(1.76 - m.x300) + 
                         1.31*m.x151/(1.31 - m.x300) + m.x152/(1 - m.x300)) + 200*m.x66 - m.x78 + m.x88 <= 200)

m.c914 = Constraint(expr=1.2*(10.5*m.x148/(10.5 - m.x301) + 4.04*m.x149/(4.04 - m.x301) + 1.76*m.x150/(1.76 - m.x301) + 
                         1.31*m.x151/(1.31 - m.x301) + m.x152/(1 - m.x301)) + 200*m.x66 - m.x78 + m.x88 <= 200)

m.c915 = Constraint(expr=1.2*(10.5*m.x153/(10.5 - m.x302) + 4.04*m.x154/(4.04 - m.x302) + 1.76*m.x155/(1.76 - m.x302) + 
                         1.31*m.x156/(1.31 - m.x302) + m.x157/(1 - m.x302)) + 200*m.x67 - m.x79 + m.x89 <= 200)

m.c916 = Constraint(expr=1.2*(10.5*m.x153/(10.5 - m.x303) + 4.04*m.x154/(4.04 - m.x303) + 1.76*m.x155/(1.76 - m.x303) + 
                         1.31*m.x156/(1.31 - m.x303) + m.x157/(1 - m.x303)) + 200*m.x67 - m.x79 + m.x89 <= 200)

m.c917 = Constraint(expr=1.2*(10.5*m.x153/(10.5 - m.x304) + 4.04*m.x154/(4.04 - m.x304) + 1.76*m.x155/(1.76 - m.x304) + 
                         1.31*m.x156/(1.31 - m.x304) + m.x157/(1 - m.x304)) + 200*m.x67 - m.x79 + m.x89 <= 200)

m.c918 = Constraint(expr=1.2*(10.5*m.x158/(10.5 - m.x305) + 4.04*m.x159/(4.04 - m.x305) + 1.76*m.x160/(1.76 - m.x305) + 
                         1.31*m.x161/(1.31 - m.x305) + m.x162/(1 - m.x305)) + 200*m.x68 - m.x80 + m.x90 <= 200)

m.c919 = Constraint(expr=1.2*(10.5*m.x158/(10.5 - m.x306) + 4.04*m.x159/(4.04 - m.x306) + 1.76*m.x160/(1.76 - m.x306) + 
                         1.31*m.x161/(1.31 - m.x306) + m.x162/(1 - m.x306)) + 200*m.x68 - m.x80 + m.x90 <= 200)

m.c920 = Constraint(expr=1.2*(10.5*m.x158/(10.5 - m.x307) + 4.04*m.x159/(4.04 - m.x307) + 1.76*m.x160/(1.76 - m.x307) + 
                         1.31*m.x161/(1.31 - m.x307) + m.x162/(1 - m.x307)) + 200*m.x68 - m.x80 + m.x90 <= 200)

m.c921 = Constraint(expr=1.2*(10.5*m.x163/(10.5 - m.x308) + 4.04*m.x164/(4.04 - m.x308) + 1.76*m.x165/(1.76 - m.x308) + 
                         1.31*m.x166/(1.31 - m.x308) + m.x167/(1 - m.x308)) + 200*m.x69 - m.x81 + m.x91 <= 200)

m.c922 = Constraint(expr=1.2*(10.5*m.x163/(10.5 - m.x309) + 4.04*m.x164/(4.04 - m.x309) + 1.76*m.x165/(1.76 - m.x309) + 
                         1.31*m.x166/(1.31 - m.x309) + m.x167/(1 - m.x309)) + 200*m.x69 - m.x81 + m.x91 <= 200)

m.c923 = Constraint(expr=1.2*(10.5*m.x168/(10.5 - m.x310) + 4.04*m.x169/(4.04 - m.x310) + 1.76*m.x170/(1.76 - m.x310) + 
                         1.31*m.x171/(1.31 - m.x310) + m.x172/(1 - m.x310)) + 200*m.x70 - m.x82 + m.x92 <= 200)

m.c924 = Constraint(expr=1.2*(10.5*m.x168/(10.5 - m.x311) + 4.04*m.x169/(4.04 - m.x311) + 1.76*m.x170/(1.76 - m.x311) + 
                         1.31*m.x171/(1.31 - m.x311) + m.x172/(1 - m.x311)) + 200*m.x70 - m.x82 + m.x92 <= 200)

m.c925 = Constraint(expr=1.2*(10.5*m.x173/(10.5 - m.x312) + 4.04*m.x174/(4.04 - m.x312) + 1.76*m.x175/(1.76 - m.x312) + 
                         1.31*m.x176/(1.31 - m.x312) + m.x177/(1 - m.x312)) + 200*m.x71 - m.x83 + m.x93 <= 200)

m.c926 = Constraint(expr=1.2*(10.5*m.x173/(10.5 - m.x313) + 4.04*m.x174/(4.04 - m.x313) + 1.76*m.x175/(1.76 - m.x313) + 
                         1.31*m.x176/(1.31 - m.x313) + m.x177/(1 - m.x313)) + 200*m.x71 - m.x83 + m.x93 <= 200)

m.c927 = Constraint(expr=1.2*(10.5*m.x178/(10.5 - m.x314) + 4.04*m.x179/(4.04 - m.x314) + 1.76*m.x180/(1.76 - m.x314) + 
                         1.31*m.x181/(1.31 - m.x314) + m.x182/(1 - m.x314)) + 200*m.x72 - m.x84 + m.x94 <= 200)

m.c928 = Constraint(expr=1.2*(10.5*m.x183/(10.5 - m.x315) + 4.04*m.x184/(4.04 - m.x315) + 1.76*m.x185/(1.76 - m.x315) + 
                         1.31*m.x186/(1.31 - m.x315) + m.x187/(1 - m.x315)) + 200*m.x73 - m.x85 + m.x95 <= 200)

m.c929 = Constraint(expr=1.2*(10.5*m.x188/(10.5 - m.x316) + 4.04*m.x189/(4.04 - m.x316) + 1.76*m.x190/(1.76 - m.x316) + 
                         1.31*m.x191/(1.31 - m.x316) + m.x192/(1 - m.x316)) + 200*m.x74 - m.x86 + m.x96 <= 200)

m.c930 = Constraint(expr=1.2*(10.5*m.x193/(10.5 - m.x317) + 4.04*m.x194/(4.04 - m.x317) + 1.76*m.x195/(1.76 - m.x317) + 
                         1.31*m.x196/(1.31 - m.x317) + m.x197/(1 - m.x317)) + 200*m.x75 - m.x87 + m.x97 <= 200)

m.c931 = Constraint(expr=1.2*(10.5*m.x148/(10.5 - m.x298) + 4.04*m.x149/(4.04 - m.x298) + 1.76*m.x150/(1.76 - m.x298) + 
                         1.31*m.x151/(1.31 - m.x298) + m.x152/(1 - m.x298)) - 200*m.x66 - m.x78 + m.x88 >= -200)

m.c932 = Constraint(expr=1.2*(10.5*m.x148/(10.5 - m.x299) + 4.04*m.x149/(4.04 - m.x299) + 1.76*m.x150/(1.76 - m.x299) + 
                         1.31*m.x151/(1.31 - m.x299) + m.x152/(1 - m.x299)) - 200*m.x66 - m.x78 + m.x88 >= -200)

m.c933 = Constraint(expr=1.2*(10.5*m.x148/(10.5 - m.x300) + 4.04*m.x149/(4.04 - m.x300) + 1.76*m.x150/(1.76 - m.x300) + 
                         1.31*m.x151/(1.31 - m.x300) + m.x152/(1 - m.x300)) - 200*m.x66 - m.x78 + m.x88 >= -200)

m.c934 = Constraint(expr=1.2*(10.5*m.x148/(10.5 - m.x301) + 4.04*m.x149/(4.04 - m.x301) + 1.76*m.x150/(1.76 - m.x301) + 
                         1.31*m.x151/(1.31 - m.x301) + m.x152/(1 - m.x301)) - 200*m.x66 - m.x78 + m.x88 >= -200)

m.c935 = Constraint(expr=1.2*(10.5*m.x153/(10.5 - m.x302) + 4.04*m.x154/(4.04 - m.x302) + 1.76*m.x155/(1.76 - m.x302) + 
                         1.31*m.x156/(1.31 - m.x302) + m.x157/(1 - m.x302)) - 200*m.x67 - m.x79 + m.x89 >= -200)

m.c936 = Constraint(expr=1.2*(10.5*m.x153/(10.5 - m.x303) + 4.04*m.x154/(4.04 - m.x303) + 1.76*m.x155/(1.76 - m.x303) + 
                         1.31*m.x156/(1.31 - m.x303) + m.x157/(1 - m.x303)) - 200*m.x67 - m.x79 + m.x89 >= -200)

m.c937 = Constraint(expr=1.2*(10.5*m.x153/(10.5 - m.x304) + 4.04*m.x154/(4.04 - m.x304) + 1.76*m.x155/(1.76 - m.x304) + 
                         1.31*m.x156/(1.31 - m.x304) + m.x157/(1 - m.x304)) - 200*m.x67 - m.x79 + m.x89 >= -200)

m.c938 = Constraint(expr=1.2*(10.5*m.x158/(10.5 - m.x305) + 4.04*m.x159/(4.04 - m.x305) + 1.76*m.x160/(1.76 - m.x305) + 
                         1.31*m.x161/(1.31 - m.x305) + m.x162/(1 - m.x305)) - 200*m.x68 - m.x80 + m.x90 >= -200)

m.c939 = Constraint(expr=1.2*(10.5*m.x158/(10.5 - m.x306) + 4.04*m.x159/(4.04 - m.x306) + 1.76*m.x160/(1.76 - m.x306) + 
                         1.31*m.x161/(1.31 - m.x306) + m.x162/(1 - m.x306)) - 200*m.x68 - m.x80 + m.x90 >= -200)

m.c940 = Constraint(expr=1.2*(10.5*m.x158/(10.5 - m.x307) + 4.04*m.x159/(4.04 - m.x307) + 1.76*m.x160/(1.76 - m.x307) + 
                         1.31*m.x161/(1.31 - m.x307) + m.x162/(1 - m.x307)) - 200*m.x68 - m.x80 + m.x90 >= -200)

m.c941 = Constraint(expr=1.2*(10.5*m.x163/(10.5 - m.x308) + 4.04*m.x164/(4.04 - m.x308) + 1.76*m.x165/(1.76 - m.x308) + 
                         1.31*m.x166/(1.31 - m.x308) + m.x167/(1 - m.x308)) - 200*m.x69 - m.x81 + m.x91 >= -200)

m.c942 = Constraint(expr=1.2*(10.5*m.x163/(10.5 - m.x309) + 4.04*m.x164/(4.04 - m.x309) + 1.76*m.x165/(1.76 - m.x309) + 
                         1.31*m.x166/(1.31 - m.x309) + m.x167/(1 - m.x309)) - 200*m.x69 - m.x81 + m.x91 >= -200)

m.c943 = Constraint(expr=1.2*(10.5*m.x168/(10.5 - m.x310) + 4.04*m.x169/(4.04 - m.x310) + 1.76*m.x170/(1.76 - m.x310) + 
                         1.31*m.x171/(1.31 - m.x310) + m.x172/(1 - m.x310)) - 200*m.x70 - m.x82 + m.x92 >= -200)

m.c944 = Constraint(expr=1.2*(10.5*m.x168/(10.5 - m.x311) + 4.04*m.x169/(4.04 - m.x311) + 1.76*m.x170/(1.76 - m.x311) + 
                         1.31*m.x171/(1.31 - m.x311) + m.x172/(1 - m.x311)) - 200*m.x70 - m.x82 + m.x92 >= -200)

m.c945 = Constraint(expr=1.2*(10.5*m.x173/(10.5 - m.x312) + 4.04*m.x174/(4.04 - m.x312) + 1.76*m.x175/(1.76 - m.x312) + 
                         1.31*m.x176/(1.31 - m.x312) + m.x177/(1 - m.x312)) - 200*m.x71 - m.x83 + m.x93 >= -200)

m.c946 = Constraint(expr=1.2*(10.5*m.x173/(10.5 - m.x313) + 4.04*m.x174/(4.04 - m.x313) + 1.76*m.x175/(1.76 - m.x313) + 
                         1.31*m.x176/(1.31 - m.x313) + m.x177/(1 - m.x313)) - 200*m.x71 - m.x83 + m.x93 >= -200)

m.c947 = Constraint(expr=1.2*(10.5*m.x178/(10.5 - m.x314) + 4.04*m.x179/(4.04 - m.x314) + 1.76*m.x180/(1.76 - m.x314) + 
                         1.31*m.x181/(1.31 - m.x314) + m.x182/(1 - m.x314)) - 200*m.x72 - m.x84 + m.x94 >= -200)

m.c948 = Constraint(expr=1.2*(10.5*m.x183/(10.5 - m.x315) + 4.04*m.x184/(4.04 - m.x315) + 1.76*m.x185/(1.76 - m.x315) + 
                         1.31*m.x186/(1.31 - m.x315) + m.x187/(1 - m.x315)) - 200*m.x73 - m.x85 + m.x95 >= -200)

m.c949 = Constraint(expr=1.2*(10.5*m.x188/(10.5 - m.x316) + 4.04*m.x189/(4.04 - m.x316) + 1.76*m.x190/(1.76 - m.x316) + 
                         1.31*m.x191/(1.31 - m.x316) + m.x192/(1 - m.x316)) - 200*m.x74 - m.x86 + m.x96 >= -200)

m.c950 = Constraint(expr=1.2*(10.5*m.x193/(10.5 - m.x317) + 4.04*m.x194/(4.04 - m.x317) + 1.76*m.x195/(1.76 - m.x317) + 
                         1.31*m.x196/(1.31 - m.x317) + m.x197/(1 - m.x317)) - 200*m.x75 - m.x87 + m.x97 >= -200)

m.c951 = Constraint(expr=1.2*(10.5*m.x198/(10.5 - m.x298) + 4.04*m.x199/(4.04 - m.x298) + 1.76*m.x200/(1.76 - m.x298) + 
                         1.31*m.x201/(1.31 - m.x298) + m.x202/(1 - m.x298)) + 200*m.x66 - m.x78 <= 200)

m.c952 = Constraint(expr=1.2*(10.5*m.x198/(10.5 - m.x299) + 4.04*m.x199/(4.04 - m.x299) + 1.76*m.x200/(1.76 - m.x299) + 
                         1.31*m.x201/(1.31 - m.x299) + m.x202/(1 - m.x299)) + 200*m.x66 - m.x78 <= 200)

m.c953 = Constraint(expr=1.2*(10.5*m.x198/(10.5 - m.x300) + 4.04*m.x199/(4.04 - m.x300) + 1.76*m.x200/(1.76 - m.x300) + 
                         1.31*m.x201/(1.31 - m.x300) + m.x202/(1 - m.x300)) + 200*m.x66 - m.x78 <= 200)

m.c954 = Constraint(expr=1.2*(10.5*m.x198/(10.5 - m.x301) + 4.04*m.x199/(4.04 - m.x301) + 1.76*m.x200/(1.76 - m.x301) + 
                         1.31*m.x201/(1.31 - m.x301) + m.x202/(1 - m.x301)) + 200*m.x66 - m.x78 <= 200)

m.c955 = Constraint(expr=1.2*(10.5*m.x203/(10.5 - m.x302) + 4.04*m.x204/(4.04 - m.x302) + 1.76*m.x205/(1.76 - m.x302) + 
                         1.31*m.x206/(1.31 - m.x302) + m.x207/(1 - m.x302)) + 200*m.x67 - m.x79 <= 200)

m.c956 = Constraint(expr=1.2*(10.5*m.x203/(10.5 - m.x303) + 4.04*m.x204/(4.04 - m.x303) + 1.76*m.x205/(1.76 - m.x303) + 
                         1.31*m.x206/(1.31 - m.x303) + m.x207/(1 - m.x303)) + 200*m.x67 - m.x79 <= 200)

m.c957 = Constraint(expr=1.2*(10.5*m.x203/(10.5 - m.x304) + 4.04*m.x204/(4.04 - m.x304) + 1.76*m.x205/(1.76 - m.x304) + 
                         1.31*m.x206/(1.31 - m.x304) + m.x207/(1 - m.x304)) + 200*m.x67 - m.x79 <= 200)

m.c958 = Constraint(expr=1.2*(10.5*m.x208/(10.5 - m.x305) + 4.04*m.x209/(4.04 - m.x305) + 1.76*m.x210/(1.76 - m.x305) + 
                         1.31*m.x211/(1.31 - m.x305) + m.x212/(1 - m.x305)) + 200*m.x68 - m.x80 <= 200)

m.c959 = Constraint(expr=1.2*(10.5*m.x208/(10.5 - m.x306) + 4.04*m.x209/(4.04 - m.x306) + 1.76*m.x210/(1.76 - m.x306) + 
                         1.31*m.x211/(1.31 - m.x306) + m.x212/(1 - m.x306)) + 200*m.x68 - m.x80 <= 200)

m.c960 = Constraint(expr=1.2*(10.5*m.x208/(10.5 - m.x307) + 4.04*m.x209/(4.04 - m.x307) + 1.76*m.x210/(1.76 - m.x307) + 
                         1.31*m.x211/(1.31 - m.x307) + m.x212/(1 - m.x307)) + 200*m.x68 - m.x80 <= 200)

m.c961 = Constraint(expr=1.2*(10.5*m.x213/(10.5 - m.x308) + 4.04*m.x214/(4.04 - m.x308) + 1.76*m.x215/(1.76 - m.x308) + 
                         1.31*m.x216/(1.31 - m.x308) + m.x217/(1 - m.x308)) + 200*m.x69 - m.x81 <= 200)

m.c962 = Constraint(expr=1.2*(10.5*m.x213/(10.5 - m.x309) + 4.04*m.x214/(4.04 - m.x309) + 1.76*m.x215/(1.76 - m.x309) + 
                         1.31*m.x216/(1.31 - m.x309) + m.x217/(1 - m.x309)) + 200*m.x69 - m.x81 <= 200)

m.c963 = Constraint(expr=1.2*(10.5*m.x218/(10.5 - m.x310) + 4.04*m.x219/(4.04 - m.x310) + 1.76*m.x220/(1.76 - m.x310) + 
                         1.31*m.x221/(1.31 - m.x310) + m.x222/(1 - m.x310)) + 200*m.x70 - m.x82 <= 200)

m.c964 = Constraint(expr=1.2*(10.5*m.x218/(10.5 - m.x311) + 4.04*m.x219/(4.04 - m.x311) + 1.76*m.x220/(1.76 - m.x311) + 
                         1.31*m.x221/(1.31 - m.x311) + m.x222/(1 - m.x311)) + 200*m.x70 - m.x82 <= 200)

m.c965 = Constraint(expr=1.2*(10.5*m.x223/(10.5 - m.x312) + 4.04*m.x224/(4.04 - m.x312) + 1.76*m.x225/(1.76 - m.x312) + 
                         1.31*m.x226/(1.31 - m.x312) + m.x227/(1 - m.x312)) + 200*m.x71 - m.x83 <= 200)

m.c966 = Constraint(expr=1.2*(10.5*m.x223/(10.5 - m.x313) + 4.04*m.x224/(4.04 - m.x313) + 1.76*m.x225/(1.76 - m.x313) + 
                         1.31*m.x226/(1.31 - m.x313) + m.x227/(1 - m.x313)) + 200*m.x71 - m.x83 <= 200)

m.c967 = Constraint(expr=1.2*(10.5*m.x228/(10.5 - m.x314) + 4.04*m.x229/(4.04 - m.x314) + 1.76*m.x230/(1.76 - m.x314) + 
                         1.31*m.x231/(1.31 - m.x314) + m.x232/(1 - m.x314)) + 200*m.x72 - m.x84 <= 200)

m.c968 = Constraint(expr=1.2*(10.5*m.x233/(10.5 - m.x315) + 4.04*m.x234/(4.04 - m.x315) + 1.76*m.x235/(1.76 - m.x315) + 
                         1.31*m.x236/(1.31 - m.x315) + m.x237/(1 - m.x315)) + 200*m.x73 - m.x85 <= 200)

m.c969 = Constraint(expr=1.2*(10.5*m.x238/(10.5 - m.x316) + 4.04*m.x239/(4.04 - m.x316) + 1.76*m.x240/(1.76 - m.x316) + 
                         1.31*m.x241/(1.31 - m.x316) + m.x242/(1 - m.x316)) + 200*m.x74 - m.x86 <= 200)

m.c970 = Constraint(expr=1.2*(10.5*m.x243/(10.5 - m.x317) + 4.04*m.x244/(4.04 - m.x317) + 1.76*m.x245/(1.76 - m.x317) + 
                         1.31*m.x246/(1.31 - m.x317) + m.x247/(1 - m.x317)) + 200*m.x75 - m.x87 <= 200)

m.c971 = Constraint(expr=-1.2*(10.5*m.x248/(10.5 - m.x298) + 4.04*m.x249/(4.04 - m.x298) + 1.76*m.x250/(1.76 - m.x298)
                          + 1.31*m.x251/(1.31 - m.x298) + m.x252/(1 - m.x298)) + 200*m.x66 - m.x88 <= 200)

m.c972 = Constraint(expr=-1.2*(10.5*m.x248/(10.5 - m.x299) + 4.04*m.x249/(4.04 - m.x299) + 1.76*m.x250/(1.76 - m.x299)
                          + 1.31*m.x251/(1.31 - m.x299) + m.x252/(1 - m.x299)) + 200*m.x66 - m.x88 <= 200)

m.c973 = Constraint(expr=-1.2*(10.5*m.x248/(10.5 - m.x300) + 4.04*m.x249/(4.04 - m.x300) + 1.76*m.x250/(1.76 - m.x300)
                          + 1.31*m.x251/(1.31 - m.x300) + m.x252/(1 - m.x300)) + 200*m.x66 - m.x88 <= 200)

m.c974 = Constraint(expr=-1.2*(10.5*m.x248/(10.5 - m.x301) + 4.04*m.x249/(4.04 - m.x301) + 1.76*m.x250/(1.76 - m.x301)
                          + 1.31*m.x251/(1.31 - m.x301) + m.x252/(1 - m.x301)) + 200*m.x66 - m.x88 <= 200)

m.c975 = Constraint(expr=-1.2*(10.5*m.x253/(10.5 - m.x302) + 4.04*m.x254/(4.04 - m.x302) + 1.76*m.x255/(1.76 - m.x302)
                          + 1.31*m.x256/(1.31 - m.x302) + m.x257/(1 - m.x302)) + 200*m.x67 - m.x89 <= 200)

m.c976 = Constraint(expr=-1.2*(10.5*m.x253/(10.5 - m.x303) + 4.04*m.x254/(4.04 - m.x303) + 1.76*m.x255/(1.76 - m.x303)
                          + 1.31*m.x256/(1.31 - m.x303) + m.x257/(1 - m.x303)) + 200*m.x67 - m.x89 <= 200)

m.c977 = Constraint(expr=-1.2*(10.5*m.x253/(10.5 - m.x304) + 4.04*m.x254/(4.04 - m.x304) + 1.76*m.x255/(1.76 - m.x304)
                          + 1.31*m.x256/(1.31 - m.x304) + m.x257/(1 - m.x304)) + 200*m.x67 - m.x89 <= 200)

m.c978 = Constraint(expr=-1.2*(10.5*m.x258/(10.5 - m.x305) + 4.04*m.x259/(4.04 - m.x305) + 1.76*m.x260/(1.76 - m.x305)
                          + 1.31*m.x261/(1.31 - m.x305) + m.x262/(1 - m.x305)) + 200*m.x68 - m.x90 <= 200)

m.c979 = Constraint(expr=-1.2*(10.5*m.x258/(10.5 - m.x306) + 4.04*m.x259/(4.04 - m.x306) + 1.76*m.x260/(1.76 - m.x306)
                          + 1.31*m.x261/(1.31 - m.x306) + m.x262/(1 - m.x306)) + 200*m.x68 - m.x90 <= 200)

m.c980 = Constraint(expr=-1.2*(10.5*m.x258/(10.5 - m.x307) + 4.04*m.x259/(4.04 - m.x307) + 1.76*m.x260/(1.76 - m.x307)
                          + 1.31*m.x261/(1.31 - m.x307) + m.x262/(1 - m.x307)) + 200*m.x68 - m.x90 <= 200)

m.c981 = Constraint(expr=-1.2*(10.5*m.x263/(10.5 - m.x308) + 4.04*m.x264/(4.04 - m.x308) + 1.76*m.x265/(1.76 - m.x308)
                          + 1.31*m.x266/(1.31 - m.x308) + m.x267/(1 - m.x308)) + 200*m.x69 - m.x91 <= 200)

m.c982 = Constraint(expr=-1.2*(10.5*m.x263/(10.5 - m.x309) + 4.04*m.x264/(4.04 - m.x309) + 1.76*m.x265/(1.76 - m.x309)
                          + 1.31*m.x266/(1.31 - m.x309) + m.x267/(1 - m.x309)) + 200*m.x69 - m.x91 <= 200)

m.c983 = Constraint(expr=-1.2*(10.5*m.x268/(10.5 - m.x310) + 4.04*m.x269/(4.04 - m.x310) + 1.76*m.x270/(1.76 - m.x310)
                          + 1.31*m.x271/(1.31 - m.x310) + m.x272/(1 - m.x310)) + 200*m.x70 - m.x92 <= 200)

m.c984 = Constraint(expr=-1.2*(10.5*m.x268/(10.5 - m.x311) + 4.04*m.x269/(4.04 - m.x311) + 1.76*m.x270/(1.76 - m.x311)
                          + 1.31*m.x271/(1.31 - m.x311) + m.x272/(1 - m.x311)) + 200*m.x70 - m.x92 <= 200)

m.c985 = Constraint(expr=-1.2*(10.5*m.x273/(10.5 - m.x312) + 4.04*m.x274/(4.04 - m.x312) + 1.76*m.x275/(1.76 - m.x312)
                          + 1.31*m.x276/(1.31 - m.x312) + m.x277/(1 - m.x312)) + 200*m.x71 - m.x93 <= 200)

m.c986 = Constraint(expr=-1.2*(10.5*m.x273/(10.5 - m.x313) + 4.04*m.x274/(4.04 - m.x313) + 1.76*m.x275/(1.76 - m.x313)
                          + 1.31*m.x276/(1.31 - m.x313) + m.x277/(1 - m.x313)) + 200*m.x71 - m.x93 <= 200)

m.c987 = Constraint(expr=-1.2*(10.5*m.x278/(10.5 - m.x314) + 4.04*m.x279/(4.04 - m.x314) + 1.76*m.x280/(1.76 - m.x314)
                          + 1.31*m.x281/(1.31 - m.x314) + m.x282/(1 - m.x314)) + 200*m.x72 - m.x94 <= 200)

m.c988 = Constraint(expr=-1.2*(10.5*m.x283/(10.5 - m.x315) + 4.04*m.x284/(4.04 - m.x315) + 1.76*m.x285/(1.76 - m.x315)
                          + 1.31*m.x286/(1.31 - m.x315) + m.x287/(1 - m.x315)) + 200*m.x73 - m.x95 <= 200)

m.c989 = Constraint(expr=-1.2*(10.5*m.x288/(10.5 - m.x316) + 4.04*m.x289/(4.04 - m.x316) + 1.76*m.x290/(1.76 - m.x316)
                          + 1.31*m.x291/(1.31 - m.x316) + m.x292/(1 - m.x316)) + 200*m.x74 - m.x96 <= 200)

m.c990 = Constraint(expr=-1.2*(10.5*m.x293/(10.5 - m.x317) + 4.04*m.x294/(4.04 - m.x317) + 1.76*m.x295/(1.76 - m.x317)
                          + 1.31*m.x296/(1.31 - m.x317) + m.x297/(1 - m.x317)) + 200*m.x75 - m.x97 <= 200)

m.c991 = Constraint(expr=   m.x318 + m.x333 <= 1)

m.c992 = Constraint(expr=   m.x319 + m.x334 <= 1)

m.c993 = Constraint(expr=   m.x320 + m.x335 <= 1)

m.c994 = Constraint(expr=   m.x321 + m.x336 <= 1)

m.c995 = Constraint(expr=   m.x322 + m.x337 <= 1)

m.c996 = Constraint(expr=   m.x323 + m.x338 <= 1)

m.c997 = Constraint(expr=   m.x324 + m.x339 <= 1)

m.c998 = Constraint(expr=   m.x325 + m.x340 <= 1)

m.c999 = Constraint(expr=   m.x326 + m.x341 <= 1)

m.c1000 = Constraint(expr=   m.x327 + m.x342 <= 1)

m.c1001 = Constraint(expr=   m.x328 + m.x343 <= 1)

m.c1002 = Constraint(expr=   m.x329 + m.x344 <= 1)

m.c1003 = Constraint(expr=   m.x330 + m.x345 <= 1)

m.c1004 = Constraint(expr=   m.x331 + m.x346 <= 1)

m.c1005 = Constraint(expr=   m.x332 + m.x347 <= 1)

m.c1006 = Constraint(expr=   m.x51 - m.x318 - m.x333 == 0)

m.c1007 = Constraint(expr=   m.x52 - m.x319 - m.x334 == 0)

m.c1008 = Constraint(expr=   m.x53 - m.x320 - m.x335 == 0)

m.c1009 = Constraint(expr=   m.x54 - m.x321 - m.x336 == 0)

m.c1010 = Constraint(expr=   m.x55 - m.x322 - m.x337 == 0)

m.c1011 = Constraint(expr=   m.x56 - m.x323 - m.x338 == 0)

m.c1012 = Constraint(expr=   m.x57 - m.x324 - m.x339 == 0)

m.c1013 = Constraint(expr=   m.x58 - m.x325 - m.x340 == 0)

m.c1014 = Constraint(expr=   m.x59 - m.x326 - m.x341 == 0)

m.c1015 = Constraint(expr=   m.x60 - m.x327 - m.x342 == 0)

m.c1016 = Constraint(expr=   m.x61 - m.x328 - m.x343 == 0)

m.c1017 = Constraint(expr=   m.x62 - m.x329 - m.x344 == 0)

m.c1018 = Constraint(expr=   m.x63 - m.x330 - m.x345 == 0)

m.c1019 = Constraint(expr=   m.x64 - m.x331 - m.x346 == 0)

m.c1020 = Constraint(expr=   m.x65 - m.x332 - m.x347 == 0)

m.c1021 = Constraint(expr= - m.b7 - m.x52 + m.x334 >= -1)

m.c1022 = Constraint(expr= - m.b8 - m.x52 + m.x334 >= -1)

m.c1023 = Constraint(expr= - m.b9 - m.x52 + m.x334 >= -1)

m.c1024 = Constraint(expr= - m.b10 - m.x52 + m.x334 >= -1)

m.c1025 = Constraint(expr= - m.b4 - m.x54 + m.x336 >= -1)

m.c1026 = Constraint(expr= - m.b5 - m.x54 + m.x336 >= -1)

m.c1027 = Constraint(expr= - m.b6 - m.x54 + m.x336 >= -1)

m.c1028 = Constraint(expr= - m.b14 - m.x54 + m.x336 >= -1)

m.c1029 = Constraint(expr= - m.b15 - m.x54 + m.x336 >= -1)

m.c1030 = Constraint(expr= - m.b16 - m.x54 + m.x336 >= -1)

m.c1031 = Constraint(expr= - m.b20 - m.x55 + m.x337 >= -1)

m.c1032 = Constraint(expr= - m.b21 - m.x55 + m.x337 >= -1)

m.c1033 = Constraint(expr= - m.b22 - m.x55 + m.x337 >= -1)

m.c1034 = Constraint(expr= - m.b2 - m.x57 + m.x339 >= -1)

m.c1035 = Constraint(expr= - m.b3 - m.x57 + m.x339 >= -1)

m.c1036 = Constraint(expr= - m.b12 - m.x57 + m.x339 >= -1)

m.c1037 = Constraint(expr= - m.b13 - m.x57 + m.x339 >= -1)

m.c1038 = Constraint(expr= - m.b24 - m.x57 + m.x339 >= -1)

m.c1039 = Constraint(expr= - m.b25 - m.x57 + m.x339 >= -1)

m.c1040 = Constraint(expr= - m.b18 - m.x58 + m.x340 >= -1)

m.c1041 = Constraint(expr= - m.b19 - m.x58 + m.x340 >= -1)

m.c1042 = Constraint(expr= - m.b27 - m.x58 + m.x340 >= -1)

m.c1043 = Constraint(expr= - m.b28 - m.x58 + m.x340 >= -1)

m.c1044 = Constraint(expr= - m.b30 - m.x59 + m.x341 >= -1)

m.c1045 = Constraint(expr= - m.b31 - m.x59 + m.x341 >= -1)

m.c1046 = Constraint(expr= - m.b1 - m.x61 + m.x343 >= -1)

m.c1047 = Constraint(expr= - m.b11 - m.x61 + m.x343 >= -1)

m.c1048 = Constraint(expr= - m.b23 - m.x61 + m.x343 >= -1)

m.c1049 = Constraint(expr= - m.b32 - m.x61 + m.x343 >= -1)

m.c1050 = Constraint(expr= - m.b17 - m.x62 + m.x344 >= -1)

m.c1051 = Constraint(expr= - m.b26 - m.x62 + m.x344 >= -1)

m.c1052 = Constraint(expr= - m.b33 - m.x62 + m.x344 >= -1)

m.c1053 = Constraint(expr= - m.b29 - m.x63 + m.x345 >= -1)

m.c1054 = Constraint(expr= - m.b34 - m.x63 + m.x345 >= -1)

m.c1055 = Constraint(expr= - m.b35 - m.x64 + m.x346 >= -1)

m.c1056 = Constraint(expr= - m.b1 - m.x53 + m.x320 >= -1)

m.c1057 = Constraint(expr= - m.b2 - m.x53 + m.x320 >= -1)

m.c1058 = Constraint(expr= - m.b4 - m.x53 + m.x320 >= -1)

m.c1059 = Constraint(expr= - m.b7 - m.x53 + m.x320 >= -1)

m.c1060 = Constraint(expr= - m.b11 - m.x55 + m.x322 >= -1)

m.c1061 = Constraint(expr= - m.b12 - m.x55 + m.x322 >= -1)

m.c1062 = Constraint(expr= - m.b14 - m.x55 + m.x322 >= -1)

m.c1063 = Constraint(expr= - m.b3 - m.x56 + m.x323 >= -1)

m.c1064 = Constraint(expr= - m.b5 - m.x56 + m.x323 >= -1)

m.c1065 = Constraint(expr= - m.b8 - m.x56 + m.x323 >= -1)

m.c1066 = Constraint(expr= - m.b17 - m.x56 + m.x323 >= -1)

m.c1067 = Constraint(expr= - m.b18 - m.x56 + m.x323 >= -1)

m.c1068 = Constraint(expr= - m.b20 - m.x56 + m.x323 >= -1)

m.c1069 = Constraint(expr= - m.b23 - m.x58 + m.x325 >= -1)

m.c1070 = Constraint(expr= - m.b24 - m.x58 + m.x325 >= -1)

m.c1071 = Constraint(expr= - m.b13 - m.x59 + m.x326 >= -1)

m.c1072 = Constraint(expr= - m.b15 - m.x59 + m.x326 >= -1)

m.c1073 = Constraint(expr= - m.b26 - m.x59 + m.x326 >= -1)

m.c1074 = Constraint(expr= - m.b27 - m.x59 + m.x326 >= -1)

m.c1075 = Constraint(expr= - m.b6 - m.x60 + m.x327 >= -1)

m.c1076 = Constraint(expr= - m.b9 - m.x60 + m.x327 >= -1)

m.c1077 = Constraint(expr= - m.b19 - m.x60 + m.x327 >= -1)

m.c1078 = Constraint(expr= - m.b21 - m.x60 + m.x327 >= -1)

m.c1079 = Constraint(expr= - m.b29 - m.x60 + m.x327 >= -1)

m.c1080 = Constraint(expr= - m.b30 - m.x60 + m.x327 >= -1)

m.c1081 = Constraint(expr= - m.b32 - m.x62 + m.x329 >= -1)

m.c1082 = Constraint(expr= - m.b25 - m.x63 + m.x330 >= -1)

m.c1083 = Constraint(expr= - m.b33 - m.x63 + m.x330 >= -1)

m.c1084 = Constraint(expr= - m.b16 - m.x64 + m.x331 >= -1)

m.c1085 = Constraint(expr= - m.b28 - m.x64 + m.x331 >= -1)

m.c1086 = Constraint(expr= - m.b34 - m.x64 + m.x331 >= -1)

m.c1087 = Constraint(expr= - m.b10 - m.x65 + m.x332 >= -1)

m.c1088 = Constraint(expr= - m.b22 - m.x65 + m.x332 >= -1)

m.c1089 = Constraint(expr= - m.b31 - m.x65 + m.x332 >= -1)

m.c1090 = Constraint(expr= - m.b35 - m.x65 + m.x332 >= -1)

m.c1091 = Constraint(expr=100*m.x364*m.x128 - m.x78*(30.77*m.x198 + 33.19*m.x199 + 35.58*m.x200 + 36.83*m.x201 + 38.3*
                          m.x202) - 1000*m.x334 >= -1000)

m.c1092 = Constraint(expr=100*m.x366*m.x129 - m.x79*(30.77*m.x203 + 33.19*m.x204 + 35.58*m.x205 + 36.83*m.x206 + 38.3*
                          m.x207) - 1000*m.x336 >= -1000)

m.c1093 = Constraint(expr=100*m.x367*m.x130 - m.x80*(30.77*m.x208 + 33.19*m.x209 + 35.58*m.x210 + 36.83*m.x211 + 38.3*
                          m.x212) - 1000*m.x337 >= -1000)

m.c1094 = Constraint(expr=100*m.x369*m.x131 - m.x81*(30.77*m.x213 + 33.19*m.x214 + 35.58*m.x215 + 36.83*m.x216 + 38.3*
                          m.x217) - 1000*m.x339 >= -1000)

m.c1095 = Constraint(expr=100*m.x370*m.x132 - m.x82*(30.77*m.x218 + 33.19*m.x219 + 35.58*m.x220 + 36.83*m.x221 + 38.3*
                          m.x222) - 1000*m.x340 >= -1000)

m.c1096 = Constraint(expr=100*m.x371*m.x133 - m.x83*(30.77*m.x223 + 33.19*m.x224 + 35.58*m.x225 + 36.83*m.x226 + 38.3*
                          m.x227) - 1000*m.x341 >= -1000)

m.c1097 = Constraint(expr=100*m.x373*m.x134 - m.x84*(30.77*m.x228 + 33.19*m.x229 + 35.58*m.x230 + 36.83*m.x231 + 38.3*
                          m.x232) - 1000*m.x343 >= -1000)

m.c1098 = Constraint(expr=100*m.x374*m.x135 - m.x85*(30.77*m.x233 + 33.19*m.x234 + 35.58*m.x235 + 36.83*m.x236 + 38.3*
                          m.x237) - 1000*m.x344 >= -1000)

m.c1099 = Constraint(expr=100*m.x375*m.x136 - m.x86*(30.77*m.x238 + 33.19*m.x239 + 35.58*m.x240 + 36.83*m.x241 + 38.3*
                          m.x242) - 1000*m.x345 >= -1000)

m.c1100 = Constraint(expr=100*m.x376*m.x137 - m.x87*(30.77*m.x243 + 33.19*m.x244 + 35.58*m.x245 + 36.83*m.x246 + 38.3*
                          m.x247) - 1000*m.x346 >= -1000)

m.c1101 = Constraint(expr=100*m.x364*m.x128 - m.x78*(30.77*m.x198 + 33.19*m.x199 + 35.58*m.x200 + 36.83*m.x201 + 38.3*
                          m.x202) + 1000*m.x334 <= 1000)

m.c1102 = Constraint(expr=100*m.x366*m.x129 - m.x79*(30.77*m.x203 + 33.19*m.x204 + 35.58*m.x205 + 36.83*m.x206 + 38.3*
                          m.x207) + 1000*m.x336 <= 1000)

m.c1103 = Constraint(expr=100*m.x367*m.x130 - m.x80*(30.77*m.x208 + 33.19*m.x209 + 35.58*m.x210 + 36.83*m.x211 + 38.3*
                          m.x212) + 1000*m.x337 <= 1000)

m.c1104 = Constraint(expr=100*m.x369*m.x131 - m.x81*(30.77*m.x213 + 33.19*m.x214 + 35.58*m.x215 + 36.83*m.x216 + 38.3*
                          m.x217) + 1000*m.x339 <= 1000)

m.c1105 = Constraint(expr=100*m.x370*m.x132 - m.x82*(30.77*m.x218 + 33.19*m.x219 + 35.58*m.x220 + 36.83*m.x221 + 38.3*
                          m.x222) + 1000*m.x340 <= 1000)

m.c1106 = Constraint(expr=100*m.x371*m.x133 - m.x83*(30.77*m.x223 + 33.19*m.x224 + 35.58*m.x225 + 36.83*m.x226 + 38.3*
                          m.x227) + 1000*m.x341 <= 1000)

m.c1107 = Constraint(expr=100*m.x373*m.x134 - m.x84*(30.77*m.x228 + 33.19*m.x229 + 35.58*m.x230 + 36.83*m.x231 + 38.3*
                          m.x232) + 1000*m.x343 <= 1000)

m.c1108 = Constraint(expr=100*m.x374*m.x135 - m.x85*(30.77*m.x233 + 33.19*m.x234 + 35.58*m.x235 + 36.83*m.x236 + 38.3*
                          m.x237) + 1000*m.x344 <= 1000)

m.c1109 = Constraint(expr=100*m.x375*m.x136 - m.x86*(30.77*m.x238 + 33.19*m.x239 + 35.58*m.x240 + 36.83*m.x241 + 38.3*
                          m.x242) + 1000*m.x345 <= 1000)

m.c1110 = Constraint(expr=100*m.x376*m.x137 - m.x87*(30.77*m.x243 + 33.19*m.x244 + 35.58*m.x245 + 36.83*m.x246 + 38.3*
                          m.x247) + 1000*m.x346 <= 1000)

m.c1111 = Constraint(expr=100*m.x350*m.x138 - m.x88*(30.77*m.x248 + 33.19*m.x249 + 35.58*m.x250 + 36.83*m.x251 + 38.3*
                          m.x252) - 1000*m.x320 >= -1000)

m.c1112 = Constraint(expr=100*m.x352*m.x139 - m.x89*(30.77*m.x253 + 33.19*m.x254 + 35.58*m.x255 + 36.83*m.x256 + 38.3*
                          m.x257) - 1000*m.x322 >= -1000)

m.c1113 = Constraint(expr=100*m.x353*m.x140 - m.x90*(30.77*m.x258 + 33.19*m.x259 + 35.58*m.x260 + 36.83*m.x261 + 38.3*
                          m.x262) - 1000*m.x323 >= -1000)

m.c1114 = Constraint(expr=100*m.x355*m.x141 - m.x91*(30.77*m.x263 + 33.19*m.x264 + 35.58*m.x265 + 36.83*m.x266 + 38.3*
                          m.x267) - 1000*m.x325 >= -1000)

m.c1115 = Constraint(expr=100*m.x356*m.x142 - m.x92*(30.77*m.x268 + 33.19*m.x269 + 35.58*m.x270 + 36.83*m.x271 + 38.3*
                          m.x272) - 1000*m.x326 >= -1000)

m.c1116 = Constraint(expr=100*m.x357*m.x143 - m.x93*(30.77*m.x273 + 33.19*m.x274 + 35.58*m.x275 + 36.83*m.x276 + 38.3*
                          m.x277) - 1000*m.x327 >= -1000)

m.c1117 = Constraint(expr=100*m.x359*m.x144 - m.x94*(30.77*m.x278 + 33.19*m.x279 + 35.58*m.x280 + 36.83*m.x281 + 38.3*
                          m.x282) - 1000*m.x329 >= -1000)

m.c1118 = Constraint(expr=100*m.x360*m.x145 - m.x95*(30.77*m.x283 + 33.19*m.x284 + 35.58*m.x285 + 36.83*m.x286 + 38.3*
                          m.x287) - 1000*m.x330 >= -1000)

m.c1119 = Constraint(expr=100*m.x361*m.x146 - m.x96*(30.77*m.x288 + 33.19*m.x289 + 35.58*m.x290 + 36.83*m.x291 + 38.3*
                          m.x292) - 1000*m.x331 >= -1000)

m.c1120 = Constraint(expr=100*m.x362*m.x147 - m.x97*(30.77*m.x293 + 33.19*m.x294 + 35.58*m.x295 + 36.83*m.x296 + 38.3*
                          m.x297) - 1000*m.x332 >= -1000)

m.c1121 = Constraint(expr=100*m.x350*m.x138 - m.x88*(30.77*m.x248 + 33.19*m.x249 + 35.58*m.x250 + 36.83*m.x251 + 38.3*
                          m.x252) + 1000*m.x320 <= 1000)

m.c1122 = Constraint(expr=100*m.x352*m.x139 - m.x89*(30.77*m.x253 + 33.19*m.x254 + 35.58*m.x255 + 36.83*m.x256 + 38.3*
                          m.x257) + 1000*m.x322 <= 1000)

m.c1123 = Constraint(expr=100*m.x353*m.x140 - m.x90*(30.77*m.x258 + 33.19*m.x259 + 35.58*m.x260 + 36.83*m.x261 + 38.3*
                          m.x262) + 1000*m.x323 <= 1000)

m.c1124 = Constraint(expr=100*m.x355*m.x141 - m.x91*(30.77*m.x263 + 33.19*m.x264 + 35.58*m.x265 + 36.83*m.x266 + 38.3*
                          m.x267) + 1000*m.x325 <= 1000)

m.c1125 = Constraint(expr=100*m.x356*m.x142 - m.x92*(30.77*m.x268 + 33.19*m.x269 + 35.58*m.x270 + 36.83*m.x271 + 38.3*
                          m.x272) + 1000*m.x326 <= 1000)

m.c1126 = Constraint(expr=100*m.x357*m.x143 - m.x93*(30.77*m.x273 + 33.19*m.x274 + 35.58*m.x275 + 36.83*m.x276 + 38.3*
                          m.x277) + 1000*m.x327 <= 1000)

m.c1127 = Constraint(expr=100*m.x359*m.x144 - m.x94*(30.77*m.x278 + 33.19*m.x279 + 35.58*m.x280 + 36.83*m.x281 + 38.3*
                          m.x282) + 1000*m.x329 <= 1000)

m.c1128 = Constraint(expr=100*m.x360*m.x145 - m.x95*(30.77*m.x283 + 33.19*m.x284 + 35.58*m.x285 + 36.83*m.x286 + 38.3*
                          m.x287) + 1000*m.x330 <= 1000)

m.c1129 = Constraint(expr=100*m.x361*m.x146 - m.x96*(30.77*m.x288 + 33.19*m.x289 + 35.58*m.x290 + 36.83*m.x291 + 38.3*
                          m.x292) + 1000*m.x331 <= 1000)

m.c1130 = Constraint(expr=100*m.x362*m.x147 - m.x97*(30.77*m.x293 + 33.19*m.x294 + 35.58*m.x295 + 36.83*m.x296 + 38.3*
                          m.x297) + 1000*m.x332 <= 1000)

m.c1131 = Constraint(expr= - 13.7791538202982*m.x378 + m.x388 == 0)

m.c1132 = Constraint(expr= - 9.22958979117519*m.x378 + m.x389 == 0)

m.c1133 = Constraint(expr= - 15.2408491577645*m.x378 + m.x390 == 0)

m.c1134 = Constraint(expr= - 8.48765327911028*m.x378 + m.x391 == 0)

m.c1135 = Constraint(expr= - 12.2935740754423*m.x378 + m.x392 == 0)

m.c1136 = Constraint(expr= - 35.6315282953964*m.x378 + m.x393 == 0)

m.c1137 = Constraint(expr= - 7.97230033233105*m.x378 + m.x394 == 0)

m.c1138 = Constraint(expr= - 10.6896359708028*m.x378 + m.x395 == 0)

m.c1139 = Constraint(expr= - 20.5224492413529*m.x378 + m.x396 == 0)

m.c1140 = Constraint(expr= - 38.5904815785076*m.x378 + m.x397 == 0)

m.c1141 = Constraint(expr= - 13.7791538202982*m.x379 + m.x398 == 0)

m.c1142 = Constraint(expr= - 9.22958979117519*m.x379 + m.x399 == 0)

m.c1143 = Constraint(expr= - 15.2408491577645*m.x379 + m.x400 == 0)

m.c1144 = Constraint(expr= - 8.48765327911028*m.x379 + m.x401 == 0)

m.c1145 = Constraint(expr= - 12.2935740754423*m.x379 + m.x402 == 0)

m.c1146 = Constraint(expr= - 35.6315282953964*m.x379 + m.x403 == 0)

m.c1147 = Constraint(expr= - 15.2408491577645*m.x380 + m.x404 == 0)

m.c1148 = Constraint(expr= - 12.2935740754423*m.x380 + m.x405 == 0)

m.c1149 = Constraint(expr= - 35.6315282953964*m.x380 + m.x406 == 0)

m.c1150 = Constraint(expr= - 10.6896359708028*m.x380 + m.x407 == 0)

m.c1151 = Constraint(expr= - 20.5224492413529*m.x380 + m.x408 == 0)

m.c1152 = Constraint(expr= - 38.5904815785076*m.x380 + m.x409 == 0)

m.c1153 = Constraint(expr= - 13.7791538202982*m.x381 + m.x410 == 0)

m.c1154 = Constraint(expr= - 9.22958979117519*m.x381 + m.x411 == 0)

m.c1155 = Constraint(expr= - 15.2408491577645*m.x381 + m.x412 == 0)

m.c1156 = Constraint(expr= - 15.2408491577645*m.x382 + m.x413 == 0)

m.c1157 = Constraint(expr= - 12.2935740754423*m.x382 + m.x414 == 0)

m.c1158 = Constraint(expr= - 35.6315282953964*m.x382 + m.x415 == 0)

m.c1159 = Constraint(expr= - 35.6315282953964*m.x383 + m.x416 == 0)

m.c1160 = Constraint(expr= - 20.5224492413529*m.x383 + m.x417 == 0)

m.c1161 = Constraint(expr= - 38.5904815785076*m.x383 + m.x418 == 0)

m.c1162 = Constraint(expr= - 13.7791538202982*m.x384 + m.x419 == 0)

m.c1163 = Constraint(expr= - 15.2408491577645*m.x385 + m.x420 == 0)

m.c1164 = Constraint(expr= - 35.6315282953964*m.x386 + m.x421 == 0)

m.c1165 = Constraint(expr= - 38.5904815785076*m.x387 + m.x422 == 0)

m.c1166 = Constraint(expr= - 1000*m.b1 - m.x388 + m.x423 >= -1000)

m.c1167 = Constraint(expr= - 1000*m.b2 - m.x389 + m.x423 >= -1000)

m.c1168 = Constraint(expr= - 1000*m.b3 - m.x390 + m.x423 >= -1000)

m.c1169 = Constraint(expr= - 1000*m.b4 - m.x391 + m.x423 >= -1000)

m.c1170 = Constraint(expr= - 1000*m.b5 - m.x392 + m.x423 >= -1000)

m.c1171 = Constraint(expr= - 1000*m.b6 - m.x393 + m.x423 >= -1000)

m.c1172 = Constraint(expr= - 1000*m.b7 - m.x394 + m.x423 >= -1000)

m.c1173 = Constraint(expr= - 1000*m.b8 - m.x395 + m.x423 >= -1000)

m.c1174 = Constraint(expr= - 1000*m.b9 - m.x396 + m.x423 >= -1000)

m.c1175 = Constraint(expr= - 1000*m.b10 - m.x397 + m.x423 >= -1000)

m.c1176 = Constraint(expr= - 1000*m.b11 - m.x398 + m.x424 >= -1000)

m.c1177 = Constraint(expr= - 1000*m.b12 - m.x399 + m.x424 >= -1000)

m.c1178 = Constraint(expr= - 1000*m.b13 - m.x400 + m.x424 >= -1000)

m.c1179 = Constraint(expr= - 1000*m.b14 - m.x401 + m.x424 >= -1000)

m.c1180 = Constraint(expr= - 1000*m.b15 - m.x402 + m.x424 >= -1000)

m.c1181 = Constraint(expr= - 1000*m.b16 - m.x403 + m.x424 >= -1000)

m.c1182 = Constraint(expr= - 1000*m.b17 - m.x404 + m.x425 >= -1000)

m.c1183 = Constraint(expr= - 1000*m.b18 - m.x405 + m.x425 >= -1000)

m.c1184 = Constraint(expr= - 1000*m.b19 - m.x406 + m.x425 >= -1000)

m.c1185 = Constraint(expr= - 1000*m.b20 - m.x407 + m.x425 >= -1000)

m.c1186 = Constraint(expr= - 1000*m.b21 - m.x408 + m.x425 >= -1000)

m.c1187 = Constraint(expr= - 1000*m.b22 - m.x409 + m.x425 >= -1000)

m.c1188 = Constraint(expr= - 1000*m.b23 - m.x410 + m.x426 >= -1000)

m.c1189 = Constraint(expr= - 1000*m.b24 - m.x411 + m.x426 >= -1000)

m.c1190 = Constraint(expr= - 1000*m.b25 - m.x412 + m.x426 >= -1000)

m.c1191 = Constraint(expr= - 1000*m.b26 - m.x413 + m.x427 >= -1000)

m.c1192 = Constraint(expr= - 1000*m.b27 - m.x414 + m.x427 >= -1000)

m.c1193 = Constraint(expr= - 1000*m.b28 - m.x415 + m.x427 >= -1000)

m.c1194 = Constraint(expr= - 1000*m.b29 - m.x416 + m.x428 >= -1000)

m.c1195 = Constraint(expr= - 1000*m.b30 - m.x417 + m.x428 >= -1000)

m.c1196 = Constraint(expr= - 1000*m.b31 - m.x418 + m.x428 >= -1000)

m.c1197 = Constraint(expr= - 1000*m.b32 - m.x419 + m.x429 >= -1000)

m.c1198 = Constraint(expr= - 1000*m.b33 - m.x420 + m.x430 >= -1000)

m.c1199 = Constraint(expr= - 1000*m.b34 - m.x421 + m.x431 >= -1000)

m.c1200 = Constraint(expr= - 1000*m.b35 - m.x422 + m.x432 >= -1000)

m.c1201 = Constraint(expr= - 1000*m.x66 + m.x378 - 1.67762719858172*m.x489 >= -1000)

m.c1202 = Constraint(expr= - 1000*m.x67 + m.x379 - 1.67762719858172*m.x490 >= -1000)

m.c1203 = Constraint(expr= - 1000*m.x68 + m.x380 - 1.67762719858172*m.x491 >= -1000)

m.c1204 = Constraint(expr= - 1000*m.x69 + m.x381 - 1.67762719858172*m.x492 >= -1000)

m.c1205 = Constraint(expr= - 1000*m.x70 + m.x382 - 1.67762719858172*m.x493 >= -1000)

m.c1206 = Constraint(expr= - 1000*m.x71 + m.x383 - 1.67762719858172*m.x494 >= -1000)

m.c1207 = Constraint(expr= - 1000*m.x72 + m.x384 - 1.67762719858172*m.x495 >= -1000)

m.c1208 = Constraint(expr= - 1000*m.x73 + m.x385 - 1.67762719858172*m.x496 >= -1000)

m.c1209 = Constraint(expr= - 1000*m.x74 + m.x386 - 1.67762719858172*m.x497 >= -1000)

m.c1210 = Constraint(expr= - 1000*m.x75 + m.x387 - 1.67762719858172*m.x498 >= -1000)

m.c1211 = Constraint(expr= - m.x78 + m.x489 >= 0)

m.c1212 = Constraint(expr= - m.x79 + m.x490 >= 0)

m.c1213 = Constraint(expr= - m.x80 + m.x491 >= 0)

m.c1214 = Constraint(expr= - m.x81 + m.x492 >= 0)

m.c1215 = Constraint(expr= - m.x82 + m.x493 >= 0)

m.c1216 = Constraint(expr= - m.x83 + m.x494 >= 0)

m.c1217 = Constraint(expr= - m.x84 + m.x495 >= 0)

m.c1218 = Constraint(expr= - m.x85 + m.x496 >= 0)

m.c1219 = Constraint(expr= - m.x86 + m.x497 >= 0)

m.c1220 = Constraint(expr= - m.x87 + m.x498 >= 0)

m.c1221 = Constraint(expr= - m.x88 + m.x489 >= 0)

m.c1222 = Constraint(expr= - m.x89 + m.x490 >= 0)

m.c1223 = Constraint(expr= - m.x90 + m.x491 >= 0)

m.c1224 = Constraint(expr= - m.x91 + m.x492 >= 0)

m.c1225 = Constraint(expr= - m.x92 + m.x493 >= 0)

m.c1226 = Constraint(expr= - m.x93 + m.x494 >= 0)

m.c1227 = Constraint(expr= - m.x94 + m.x495 >= 0)

m.c1228 = Constraint(expr= - m.x95 + m.x496 >= 0)

m.c1229 = Constraint(expr= - m.x96 + m.x497 >= 0)

m.c1230 = Constraint(expr= - m.x97 + m.x498 >= 0)

m.c1231 = Constraint(expr=-0.0001*(22.83*m.x378**2 + 406.8*m.x378) + m.x433 == 0.05711)

m.c1232 = Constraint(expr=-0.0001*(22.83*m.x379**2 + 406.8*m.x379) + m.x434 == 0.05711)

m.c1233 = Constraint(expr=-0.0001*(22.83*m.x380**2 + 406.8*m.x380) + m.x435 == 0.05711)

m.c1234 = Constraint(expr=-0.0001*(22.83*m.x381**2 + 406.8*m.x381) + m.x436 == 0.05711)

m.c1235 = Constraint(expr=-0.0001*(22.83*m.x382**2 + 406.8*m.x382) + m.x437 == 0.05711)

m.c1236 = Constraint(expr=-0.0001*(22.83*m.x383**2 + 406.8*m.x383) + m.x438 == 0.05711)

m.c1237 = Constraint(expr=-0.0001*(22.83*m.x384**2 + 406.8*m.x384) + m.x439 == 0.05711)

m.c1238 = Constraint(expr=-0.0001*(22.83*m.x385**2 + 406.8*m.x385) + m.x440 == 0.05711)

m.c1239 = Constraint(expr=-0.0001*(22.83*m.x386**2 + 406.8*m.x386) + m.x441 == 0.05711)

m.c1240 = Constraint(expr=-0.0001*(22.83*m.x387**2 + 406.8*m.x387) + m.x442 == 0.05711)

m.c1241 = Constraint(expr= - 57.650802630846*m.b1 + m.x474 >= -41.3522129303489)

m.c1242 = Constraint(expr= - 57.650802630846*m.b2 + m.x474 >= -48.934819645554)

m.c1243 = Constraint(expr= - 57.650802630846*m.b3 + m.x474 >= -38.9160540345718)

m.c1244 = Constraint(expr= - 57.650802630846*m.b4 + m.x474 >= -50.1713804989955)

m.c1245 = Constraint(expr= - 57.650802630846*m.b5 + m.x474 >= -43.8281791717755)

m.c1246 = Constraint(expr= - 57.650802630846*m.b6 + m.x474 >= -4.93158880518534)

m.c1247 = Constraint(expr= - 57.650802630846*m.b7 + m.x474 >= -51.0303020769609)

m.c1248 = Constraint(expr= - 57.650802630846*m.b8 + m.x474 >= -46.5014093461746)

m.c1249 = Constraint(expr= - 57.650802630846*m.b9 + m.x474 >= -30.1133872285911)

m.c1250 = Constraint(expr= - 57.650802630846*m.b10 + m.x474 >= 0)

m.c1251 = Constraint(expr= - 57.650802630846*m.b11 + m.x475 >= -41.3522129303489)

m.c1252 = Constraint(expr= - 57.650802630846*m.b12 + m.x475 >= -48.934819645554)

m.c1253 = Constraint(expr= - 57.650802630846*m.b13 + m.x475 >= -38.9160540345718)

m.c1254 = Constraint(expr= - 57.650802630846*m.b14 + m.x475 >= -50.1713804989955)

m.c1255 = Constraint(expr= - 57.650802630846*m.b15 + m.x475 >= -43.8281791717755)

m.c1256 = Constraint(expr= - 57.650802630846*m.b16 + m.x475 >= -4.93158880518534)

m.c1257 = Constraint(expr= - 57.650802630846*m.b17 + m.x476 >= -38.9160540345718)

m.c1258 = Constraint(expr= - 57.650802630846*m.b18 + m.x476 >= -43.8281791717755)

m.c1259 = Constraint(expr= - 57.650802630846*m.b19 + m.x476 >= -4.93158880518534)

m.c1260 = Constraint(expr= - 57.650802630846*m.b20 + m.x476 >= -46.5014093461746)

m.c1261 = Constraint(expr= - 57.650802630846*m.b21 + m.x476 >= -30.1133872285911)

m.c1262 = Constraint(expr= - 57.650802630846*m.b22 + m.x476 >= 0)

m.c1263 = Constraint(expr= - 57.650802630846*m.b23 + m.x477 >= -41.3522129303489)

m.c1264 = Constraint(expr= - 57.650802630846*m.b24 + m.x477 >= -48.934819645554)

m.c1265 = Constraint(expr= - 57.650802630846*m.b25 + m.x477 >= -38.9160540345718)

m.c1266 = Constraint(expr= - 57.650802630846*m.b26 + m.x478 >= -38.9160540345718)

m.c1267 = Constraint(expr= - 57.650802630846*m.b27 + m.x478 >= -43.8281791717755)

m.c1268 = Constraint(expr= - 57.650802630846*m.b28 + m.x478 >= -4.93158880518534)

m.c1269 = Constraint(expr= - 57.650802630846*m.b29 + m.x479 >= -4.93158880518534)

m.c1270 = Constraint(expr= - 57.650802630846*m.b30 + m.x479 >= -30.1133872285911)

m.c1271 = Constraint(expr= - 57.650802630846*m.b31 + m.x479 >= 0)

m.c1272 = Constraint(expr= - 57.650802630846*m.b32 + m.x480 >= -41.3522129303489)

m.c1273 = Constraint(expr= - 57.650802630846*m.b33 + m.x481 >= -38.9160540345718)

m.c1274 = Constraint(expr= - 57.650802630846*m.b34 + m.x482 >= -4.93158880518534)

m.c1275 = Constraint(expr= - 57.650802630846*m.b35 + m.x483 >= 0)

m.c1276 = Constraint(expr=-1.2*(m.x433*m.x474 + m.x434*m.x475 + m.x435*m.x476 + m.x436*m.x477 + m.x437*m.x478 + m.x438*
                          m.x479 + m.x439*m.x480 + m.x440*m.x481 + m.x441*m.x482 + m.x442*m.x483 + m.x443*m.x484 + 
                          m.x444*m.x485 + m.x445*m.x486 + m.x446*m.x487 + m.x447*m.x488) + m.x448 == 0)

m.c1277 = Constraint(expr= - 15*m.x66 - 0.06038*m.x423 + m.x449 >= -14.4693)

m.c1278 = Constraint(expr= - 15*m.x67 - 0.06038*m.x424 + m.x450 >= -14.4693)

m.c1279 = Constraint(expr= - 15*m.x68 - 0.06038*m.x425 + m.x451 >= -14.4693)

m.c1280 = Constraint(expr= - 15*m.x69 - 0.06038*m.x426 + m.x452 >= -14.4693)

m.c1281 = Constraint(expr= - 15*m.x70 - 0.06038*m.x427 + m.x453 >= -14.4693)

m.c1282 = Constraint(expr= - 15*m.x71 - 0.06038*m.x428 + m.x454 >= -14.4693)

m.c1283 = Constraint(expr= - 15*m.x72 - 0.06038*m.x429 + m.x455 >= -14.4693)

m.c1284 = Constraint(expr= - 15*m.x73 - 0.06038*m.x430 + m.x456 >= -14.4693)

m.c1285 = Constraint(expr= - 15*m.x74 - 0.06038*m.x431 + m.x457 >= -14.4693)

m.c1286 = Constraint(expr= - 15*m.x75 - 0.06038*m.x432 + m.x458 >= -14.4693)

m.c1287 = Constraint(expr= - 4.22*m.x449 + m.x459 == 0)

m.c1288 = Constraint(expr= - 4.22*m.x450 + m.x460 == 0)

m.c1289 = Constraint(expr= - 4.22*m.x451 + m.x461 == 0)

m.c1290 = Constraint(expr= - 4.22*m.x452 + m.x462 == 0)

m.c1291 = Constraint(expr= - 4.22*m.x453 + m.x463 == 0)

m.c1292 = Constraint(expr= - 4.22*m.x454 + m.x464 == 0)

m.c1293 = Constraint(expr= - 4.22*m.x455 + m.x465 == 0)

m.c1294 = Constraint(expr= - 4.22*m.x456 + m.x466 == 0)

m.c1295 = Constraint(expr= - 4.22*m.x457 + m.x467 == 0)

m.c1296 = Constraint(expr= - 4.22*m.x458 + m.x468 == 0)

m.c1297 = Constraint(expr= - m.b46 + m.x61 == 0)

m.c1298 = Constraint(expr= - m.b47 + m.x62 == 0)

m.c1299 = Constraint(expr= - m.b48 + m.x63 == 0)

m.c1300 = Constraint(expr= - m.b49 + m.x64 == 0)

m.c1301 = Constraint(expr= - m.b50 + m.x65 == 0)

m.c1302 = Constraint(expr= - m.b36 + m.x51 == 0)

m.c1303 = Constraint(expr= - m.b37 + m.x52 == 0)

m.c1304 = Constraint(expr= - m.b38 + m.x53 == 0)

m.c1305 = Constraint(expr= - m.b39 + m.x54 == 0)

m.c1306 = Constraint(expr= - m.b40 + m.x55 == 0)

m.c1307 = Constraint(expr= - m.b41 + m.x56 == 0)

m.c1308 = Constraint(expr= - m.b42 + m.x57 == 0)

m.c1309 = Constraint(expr= - m.b43 + m.x58 == 0)

m.c1310 = Constraint(expr= - m.b44 + m.x59 == 0)

m.c1311 = Constraint(expr= - m.b45 + m.x60 == 0)
