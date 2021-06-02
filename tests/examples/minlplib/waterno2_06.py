#  MINLP written by GAMS Convert at 04/21/18 13:55:18
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       1235      736      205      294        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        997      943       54        0        0        0        0        0
#  FX      9        9        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       3277     2671      606        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


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
m.b46 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b47 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b48 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b49 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b50 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b51 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b52 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b53 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b54 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b55 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x56 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x57 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x60 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x83 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x87 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x88 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x90 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x92 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x93 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x96 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x99 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x102 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x105 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x109 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x111 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x113 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x117 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x119 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x121 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x123 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x124 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x125 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x126 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x127 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x128 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x129 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x130 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x131 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x132 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x133 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x134 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x135 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x136 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x137 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x138 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x139 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x140 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x141 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x142 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x143 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x144 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x145 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x146 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x147 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x148 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x149 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x150 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x151 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x152 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x153 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x154 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x155 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x156 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x157 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x158 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x159 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x160 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x161 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x162 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x163 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x164 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x165 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x166 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x167 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x168 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x169 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x170 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x171 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x172 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x173 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x174 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x175 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x176 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x177 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x178 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x179 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x180 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x181 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x182 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x183 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x184 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x185 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x186 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x187 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,1.16),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,1.16),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,1.16),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,1.16),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,1.16),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x235 = Var(within=Reals,bounds=(0,1.16),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x242 = Var(within=Reals,bounds=(3.5,3.5),initialize=3.5)
m.x243 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x244 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x245 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x246 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x247 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x248 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x249 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x250 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x251 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x252 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x253 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x254 = Var(within=Reals,bounds=(4.1,4.1),initialize=4.1)
m.x255 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x256 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x257 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x258 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x259 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x260 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x261 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x262 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x263 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x264 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x265 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x266 = Var(within=Reals,bounds=(4,4),initialize=4)
m.x267 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x268 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x269 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x270 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x271 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x272 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x273 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x274 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x275 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x276 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x277 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x278 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x279 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x280 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x281 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x282 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x283 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x284 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x285 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x286 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x287 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x289 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x290 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x291 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x292 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x293 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x294 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x295 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x296 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x297 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x298 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x299 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x300 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x301 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x302 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x303 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x304 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x305 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x306 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x307 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x309 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x311 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x312 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x313 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x314 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x315 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x316 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x317 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x318 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x319 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x320 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x321 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x322 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x323 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x324 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x325 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x326 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x327 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x328 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x329 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x330 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x331 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x332 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x333 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x334 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x335 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x336 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x337 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x338 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x339 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x340 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x341 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x342 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x343 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x344 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x345 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x346 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x347 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x348 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x349 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x350 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x351 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x352 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x353 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x354 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x355 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x356 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x357 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x358 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x359 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x360 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x361 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x362 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x363 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x364 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x365 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x366 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x367 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x368 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x369 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x370 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x371 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x372 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x373 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x374 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x375 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x376 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x377 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x378 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x379 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x380 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x381 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x382 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x383 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x384 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x385 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x386 = Var(within=Reals,bounds=(62,65),initialize=62)
m.x387 = Var(within=Reals,bounds=(62,65),initialize=62)
m.x388 = Var(within=Reals,bounds=(62,65),initialize=62)
m.x389 = Var(within=Reals,bounds=(62,65),initialize=62)
m.x390 = Var(within=Reals,bounds=(62,65),initialize=62)
m.x391 = Var(within=Reals,bounds=(62,65),initialize=62)
m.x392 = Var(within=Reals,bounds=(92.5,95),initialize=92.5)
m.x393 = Var(within=Reals,bounds=(92.5,95),initialize=92.5)
m.x394 = Var(within=Reals,bounds=(92.5,95),initialize=92.5)
m.x395 = Var(within=Reals,bounds=(92.5,95),initialize=92.5)
m.x396 = Var(within=Reals,bounds=(92.5,95),initialize=92.5)
m.x397 = Var(within=Reals,bounds=(92.5,95),initialize=92.5)
m.x398 = Var(within=Reals,bounds=(105,109),initialize=105)
m.x399 = Var(within=Reals,bounds=(105,109),initialize=105)
m.x400 = Var(within=Reals,bounds=(105,109),initialize=105)
m.x401 = Var(within=Reals,bounds=(105,109),initialize=105)
m.x402 = Var(within=Reals,bounds=(105,109),initialize=105)
m.x403 = Var(within=Reals,bounds=(105,109),initialize=105)
m.x404 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x405 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x406 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x407 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x408 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x409 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x410 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x411 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x412 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x413 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x414 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x415 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x416 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x417 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x418 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x419 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x420 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x421 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x422 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x423 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x424 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x425 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x426 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x427 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x428 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x429 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x430 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x431 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x432 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x433 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x434 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x435 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x436 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x437 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x438 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x439 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x440 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x441 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x442 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x443 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x444 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x445 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x446 = Var(within=Reals,bounds=(49,49),initialize=49)
m.x447 = Var(within=Reals,bounds=(-49,1000),initialize=0)
m.x448 = Var(within=Reals,bounds=(49,49),initialize=49)
m.x449 = Var(within=Reals,bounds=(-49,1000),initialize=0)
m.x450 = Var(within=Reals,bounds=(49,49),initialize=49)
m.x451 = Var(within=Reals,bounds=(-49,1000),initialize=0)
m.x452 = Var(within=Reals,bounds=(49,49),initialize=49)
m.x453 = Var(within=Reals,bounds=(-49,1000),initialize=0)
m.x454 = Var(within=Reals,bounds=(49,49),initialize=49)
m.x455 = Var(within=Reals,bounds=(-49,1000),initialize=0)
m.x456 = Var(within=Reals,bounds=(49,49),initialize=49)
m.x457 = Var(within=Reals,bounds=(-49,1000),initialize=0)
m.x458 = Var(within=Reals,bounds=(-65,1000),initialize=0)
m.x459 = Var(within=Reals,bounds=(-65,1000),initialize=0)
m.x460 = Var(within=Reals,bounds=(-65,1000),initialize=0)
m.x461 = Var(within=Reals,bounds=(-65,1000),initialize=0)
m.x462 = Var(within=Reals,bounds=(-65,1000),initialize=0)
m.x463 = Var(within=Reals,bounds=(-65,1000),initialize=0)
m.x464 = Var(within=Reals,bounds=(-95,1000),initialize=0)
m.x465 = Var(within=Reals,bounds=(-95,1000),initialize=0)
m.x466 = Var(within=Reals,bounds=(-95,1000),initialize=0)
m.x467 = Var(within=Reals,bounds=(-95,1000),initialize=0)
m.x468 = Var(within=Reals,bounds=(-95,1000),initialize=0)
m.x469 = Var(within=Reals,bounds=(-95,1000),initialize=0)
m.x470 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x471 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x472 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x473 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x474 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x475 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x476 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x477 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x478 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x479 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x480 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x481 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x482 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x483 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x484 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x485 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x486 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x487 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x488 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x489 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x490 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x491 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x492 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x493 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x494 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x495 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x496 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x497 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x498 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x499 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x500 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x501 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x502 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x503 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x504 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x505 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x506 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x507 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x508 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x509 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x510 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x511 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x512 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x513 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x514 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x515 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x516 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x517 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x518 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x519 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x520 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x521 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x522 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x523 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x524 = Var(within=Reals,bounds=(0.6,1),initialize=0.6)
m.x525 = Var(within=Reals,bounds=(0.6,1),initialize=0.6)
m.x526 = Var(within=Reals,bounds=(0.6,1),initialize=0.6)
m.x527 = Var(within=Reals,bounds=(0.6,1),initialize=0.6)
m.x528 = Var(within=Reals,bounds=(0.6,1),initialize=0.6)
m.x529 = Var(within=Reals,bounds=(0.6,1),initialize=0.6)
m.x530 = Var(within=Reals,bounds=(0.8,1),initialize=0.8)
m.x531 = Var(within=Reals,bounds=(0.8,1),initialize=0.8)
m.x532 = Var(within=Reals,bounds=(0.8,1),initialize=0.8)
m.x533 = Var(within=Reals,bounds=(0.8,1),initialize=0.8)
m.x534 = Var(within=Reals,bounds=(0.8,1),initialize=0.8)
m.x535 = Var(within=Reals,bounds=(0.8,1),initialize=0.8)
m.x536 = Var(within=Reals,bounds=(0.85,1),initialize=0.85)
m.x537 = Var(within=Reals,bounds=(0.85,1),initialize=0.85)
m.x538 = Var(within=Reals,bounds=(0.85,1),initialize=0.85)
m.x539 = Var(within=Reals,bounds=(0.85,1),initialize=0.85)
m.x540 = Var(within=Reals,bounds=(0.85,1),initialize=0.85)
m.x541 = Var(within=Reals,bounds=(0.85,1),initialize=0.85)
m.x542 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x543 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x544 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x545 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x546 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x547 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x548 = Var(within=Reals,bounds=(100,1000),initialize=100)
m.x549 = Var(within=Reals,bounds=(100,1000),initialize=100)
m.x550 = Var(within=Reals,bounds=(100,1000),initialize=100)
m.x551 = Var(within=Reals,bounds=(100,1000),initialize=100)
m.x552 = Var(within=Reals,bounds=(100,1000),initialize=100)
m.x553 = Var(within=Reals,bounds=(100,1000),initialize=100)
m.x554 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x555 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x556 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x557 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x558 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x559 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x560 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x561 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x562 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x563 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x564 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x565 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x566 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x567 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x568 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x569 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x570 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x571 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x572 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x573 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x574 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x575 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x576 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x577 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x578 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x579 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x580 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x581 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x582 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x583 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x584 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x585 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x586 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x587 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x588 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x589 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x590 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x591 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x592 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x593 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x594 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x595 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x596 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x597 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x598 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x599 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x600 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x601 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x602 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x603 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x604 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x605 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x606 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x607 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x608 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x609 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x610 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x611 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x612 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x613 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x614 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x615 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x616 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x617 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x618 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x619 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x620 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x621 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x622 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x623 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x624 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x625 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x626 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x627 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x628 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x629 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x630 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x631 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x632 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x633 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x634 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x635 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x636 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x637 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x638 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x639 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x640 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x641 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x642 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x643 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x644 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x645 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x646 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x647 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x648 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x649 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x650 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x651 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x652 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x653 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x654 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x655 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x656 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x657 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x658 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x659 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x660 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x661 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x662 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x663 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x664 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x665 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x666 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x667 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x668 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x669 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x670 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x671 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x672 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x673 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x674 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x675 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x676 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x677 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x678 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x679 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x680 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x681 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x682 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x683 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x684 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x685 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x686 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x687 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x688 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x689 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x690 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x691 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x692 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x693 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x694 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x695 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x696 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x697 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x698 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x699 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x700 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x701 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x702 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x703 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x704 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x705 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x706 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x707 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x708 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x709 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x710 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x711 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x712 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x713 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x714 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x715 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x716 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x717 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x718 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x719 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x720 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x721 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x722 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x723 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x724 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x725 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x726 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x727 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x728 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x729 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x730 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x731 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x732 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x733 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x734 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x735 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x736 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x737 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x738 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x739 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x740 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x741 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x742 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x743 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x744 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x745 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x746 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x747 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x748 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x749 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x750 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x751 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x752 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x753 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x754 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x755 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x756 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x757 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x758 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x759 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x760 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x761 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x762 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x763 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x764 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x765 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x766 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x767 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x768 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x769 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x770 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x771 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x772 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x773 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x774 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x775 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x776 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x777 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x778 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x779 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x780 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x781 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x782 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x783 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x784 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x785 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x786 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x787 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x788 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x789 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x790 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x791 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x792 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x793 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x794 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x795 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x796 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x797 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x798 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x799 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x800 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x801 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x802 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x803 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x804 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x805 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x806 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x807 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x808 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x809 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x810 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x811 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x812 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x813 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x814 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x815 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x816 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x817 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x818 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x819 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x820 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x821 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x822 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x823 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x824 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x825 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x826 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x827 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x828 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x829 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x830 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x831 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x832 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x833 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x834 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x835 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x836 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x837 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x838 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x839 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x840 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x841 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x842 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x843 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x844 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x845 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x846 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x847 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x848 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x849 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x850 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x851 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x852 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x853 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x854 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x855 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x856 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x857 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x858 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x859 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x860 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x861 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x862 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x863 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x864 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x865 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x866 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x867 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x868 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x869 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x870 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x871 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x872 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x873 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x874 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x875 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x876 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x877 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x878 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x879 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x880 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x881 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x882 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x883 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x884 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x885 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x886 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x887 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x888 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x889 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x890 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x891 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x892 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x893 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x894 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x895 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x896 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x897 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x898 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x899 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x900 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x901 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x902 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x903 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x904 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x905 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x906 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x907 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x908 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x909 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x910 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x911 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x912 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x913 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x914 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x915 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x916 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x917 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x918 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x919 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x920 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x921 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x922 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x923 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x924 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x925 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x926 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x927 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x928 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x929 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x930 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x931 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x932 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x933 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x934 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x935 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x936 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x937 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x938 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x939 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x940 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x941 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x942 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x943 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x944 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x945 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x946 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x947 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x948 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x949 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x950 = Var(within=Reals,bounds=(0.36,1),initialize=0.36)
m.x951 = Var(within=Reals,bounds=(0.216,1),initialize=0.216)
m.x952 = Var(within=Reals,bounds=(0.36,1),initialize=0.36)
m.x953 = Var(within=Reals,bounds=(0.216,1),initialize=0.216)
m.x954 = Var(within=Reals,bounds=(0.36,1),initialize=0.36)
m.x955 = Var(within=Reals,bounds=(0.216,1),initialize=0.216)
m.x956 = Var(within=Reals,bounds=(0.36,1),initialize=0.36)
m.x957 = Var(within=Reals,bounds=(0.216,1),initialize=0.216)
m.x958 = Var(within=Reals,bounds=(0.36,1),initialize=0.36)
m.x959 = Var(within=Reals,bounds=(0.216,1),initialize=0.216)
m.x960 = Var(within=Reals,bounds=(0.36,1),initialize=0.36)
m.x961 = Var(within=Reals,bounds=(0.216,1),initialize=0.216)
m.x962 = Var(within=Reals,bounds=(0.64,1),initialize=0.64)
m.x963 = Var(within=Reals,bounds=(0.512,1),initialize=0.512)
m.x964 = Var(within=Reals,bounds=(0.64,1),initialize=0.64)
m.x965 = Var(within=Reals,bounds=(0.512,1),initialize=0.512)
m.x966 = Var(within=Reals,bounds=(0.64,1),initialize=0.64)
m.x967 = Var(within=Reals,bounds=(0.512,1),initialize=0.512)
m.x968 = Var(within=Reals,bounds=(0.64,1),initialize=0.64)
m.x969 = Var(within=Reals,bounds=(0.512,1),initialize=0.512)
m.x970 = Var(within=Reals,bounds=(0.64,1),initialize=0.64)
m.x971 = Var(within=Reals,bounds=(0.512,1),initialize=0.512)
m.x972 = Var(within=Reals,bounds=(0.64,1),initialize=0.64)
m.x973 = Var(within=Reals,bounds=(0.512,1),initialize=0.512)
m.x974 = Var(within=Reals,bounds=(0.7225,1),initialize=0.7225)
m.x975 = Var(within=Reals,bounds=(0.614125,1),initialize=0.614125)
m.x976 = Var(within=Reals,bounds=(0.7225,1),initialize=0.7225)
m.x977 = Var(within=Reals,bounds=(0.614125,1),initialize=0.614125)
m.x978 = Var(within=Reals,bounds=(0.7225,1),initialize=0.7225)
m.x979 = Var(within=Reals,bounds=(0.614125,1),initialize=0.614125)
m.x980 = Var(within=Reals,bounds=(0.7225,1),initialize=0.7225)
m.x981 = Var(within=Reals,bounds=(0.614125,1),initialize=0.614125)
m.x982 = Var(within=Reals,bounds=(0.7225,1),initialize=0.7225)
m.x983 = Var(within=Reals,bounds=(0.614125,1),initialize=0.614125)
m.x984 = Var(within=Reals,bounds=(0.7225,1),initialize=0.7225)
m.x985 = Var(within=Reals,bounds=(0.614125,1),initialize=0.614125)
m.x986 = Var(within=Reals,bounds=(0.49,1),initialize=0.49)
m.x987 = Var(within=Reals,bounds=(0.343,1),initialize=0.343)
m.x988 = Var(within=Reals,bounds=(0.49,1),initialize=0.49)
m.x989 = Var(within=Reals,bounds=(0.343,1),initialize=0.343)
m.x990 = Var(within=Reals,bounds=(0.49,1),initialize=0.49)
m.x991 = Var(within=Reals,bounds=(0.343,1),initialize=0.343)
m.x992 = Var(within=Reals,bounds=(0.49,1),initialize=0.49)
m.x993 = Var(within=Reals,bounds=(0.343,1),initialize=0.343)
m.x994 = Var(within=Reals,bounds=(0.49,1),initialize=0.49)
m.x995 = Var(within=Reals,bounds=(0.343,1),initialize=0.343)
m.x996 = Var(within=Reals,bounds=(0.49,1),initialize=0.49)
m.x997 = Var(within=Reals,bounds=(0.343,1),initialize=0.343)

m.obj = Objective(expr=   m.x554 + m.x561 + m.x568 + m.x569 + m.x577 + m.x583 + m.x584 + m.x589 + m.x594 + m.x599
                        + m.x604 + m.x609 + m.x614 + m.x619 + m.x624 + m.x632 + m.x638 + m.x639 + m.x644 + m.x649
                        + m.x657 + m.x663 + m.x664 + m.x669 + m.x674 + m.x679 + m.x685 + m.x690 + m.x694 + m.x699
                        + m.x704 + m.x709 + m.x714 + m.x719 + m.x724 + m.x729 + m.x734 + m.x739 + m.x744 + m.x749
                        + m.x754 + m.x759 + m.x764 + m.x769 + m.x774 + m.x779 + m.x784 + m.x789 + m.x794 + m.x799
                        + m.x804 + m.x809 + m.x814 + m.x819, sense=minimize)

m.c2 = Constraint(expr=   m.x279 + 27.42831624*m.x281 + 37.5407324*m.x283 - 57.2814121*m.x285 == 0)

m.c3 = Constraint(expr=   m.x287 - 57.2814121*m.x289 + 37.5407324*m.x291 + 27.42831624*m.x293 == 0)

m.c4 = Constraint(expr=   m.x295 - 57.2814121*m.x297 + 37.5407324*m.x299 + 27.42831624*m.x301 == 0)

m.c5 = Constraint(expr=   m.x303 - 57.2814121*m.x305 + 37.5407324*m.x307 + 27.42831624*m.x309 == 0)

m.c6 = Constraint(expr=   m.x311 - 57.2814121*m.x313 + 37.5407324*m.x315 + 27.42831624*m.x317 == 0)

m.c7 = Constraint(expr=   m.x319 - 57.2814121*m.x321 + 37.5407324*m.x323 + 27.42831624*m.x325 == 0)

m.c8 = Constraint(expr= - 57.2814121*m.x285 + m.x327 + 27.42831624*m.x329 + 37.5407324*m.x331 == 0)

m.c9 = Constraint(expr= - 57.2814121*m.x289 + m.x333 + 27.42831624*m.x335 + 37.5407324*m.x337 == 0)

m.c10 = Constraint(expr= - 57.2814121*m.x297 + m.x339 + 37.5407324*m.x341 + 27.42831624*m.x343 == 0)

m.c11 = Constraint(expr= - 57.2814121*m.x305 + m.x345 + 37.5407324*m.x347 + 27.42831624*m.x349 == 0)

m.c12 = Constraint(expr= - 57.2814121*m.x313 + m.x351 + 37.5407324*m.x353 + 27.42831624*m.x355 == 0)

m.c13 = Constraint(expr= - 57.2814121*m.x321 + m.x357 + 27.42831624*m.x359 + 37.5407324*m.x361 == 0)

m.c14 = Constraint(expr= - 57.2814121*m.x285 + m.x363 + 37.5407324*m.x365 + 27.42831624*m.x367 == 0)

m.c15 = Constraint(expr= - 57.2814121*m.x289 + m.x369 + 37.5407324*m.x371 + 27.42831624*m.x373 == 0)

m.c16 = Constraint(expr= - 57.2814121*m.x297 + m.x375 + 37.5407324*m.x377 + 27.42831624*m.x379 == 0)

m.c17 = Constraint(expr= - 57.2814121*m.x305 + m.x381 + 37.5407324*m.x383 + 27.42831624*m.x385 == 0)

m.c18 = Constraint(expr=   m.x56 + 37.5407324*m.x57 + 27.42831624*m.x58 - 57.2814121*m.x313 == 0)

m.c19 = Constraint(expr=   m.x59 + 37.5407324*m.x60 + 27.42831624*m.x61 - 57.2814121*m.x321 == 0)

m.c20 = Constraint(expr=   m.x62 - 76.45219958*m.x63 + 43.14087708*m.x64 + 50.37356589*m.x65 == 0)

m.c21 = Constraint(expr=   m.x66 + 43.14087708*m.x67 - 76.45219958*m.x68 + 50.37356589*m.x69 == 0)

m.c22 = Constraint(expr=   m.x70 + 50.37356589*m.x71 + 43.14087708*m.x72 - 76.45219958*m.x73 == 0)

m.c23 = Constraint(expr=   m.x74 + 50.37356589*m.x75 + 43.14087708*m.x76 - 76.45219958*m.x77 == 0)

m.c24 = Constraint(expr=   m.x78 + 50.37356589*m.x79 + 43.14087708*m.x80 - 76.45219958*m.x81 == 0)

m.c25 = Constraint(expr=   m.x82 + 43.14087708*m.x83 - 76.45219958*m.x84 + 50.37356589*m.x85 == 0)

m.c26 = Constraint(expr= - 76.45219958*m.x63 + m.x86 + 43.14087708*m.x87 + 50.37356589*m.x88 == 0)

m.c27 = Constraint(expr= - 76.45219958*m.x68 + m.x89 + 50.37356589*m.x90 + 43.14087708*m.x91 == 0)

m.c28 = Constraint(expr= - 76.45219958*m.x73 + m.x92 + 43.14087708*m.x93 + 50.37356589*m.x94 == 0)

m.c29 = Constraint(expr= - 76.45219958*m.x77 + m.x95 + 50.37356589*m.x96 + 43.14087708*m.x97 == 0)

m.c30 = Constraint(expr= - 76.45219958*m.x81 + m.x98 + 43.14087708*m.x99 + 50.37356589*m.x100 == 0)

m.c31 = Constraint(expr= - 76.45219958*m.x84 + m.x101 + 43.14087708*m.x102 + 50.37356589*m.x103 == 0)

m.c32 = Constraint(expr=   m.x104 - 25.39911174*m.x105 - 69.39622571*m.x106 + 58.31011875*m.x107 == 0)

m.c33 = Constraint(expr=   m.x108 - 25.39911174*m.x109 - 69.39622571*m.x110 + 58.31011875*m.x111 == 0)

m.c34 = Constraint(expr=   m.x112 + 58.31011875*m.x113 - 69.39622571*m.x114 - 25.39911174*m.x115 == 0)

m.c35 = Constraint(expr=   m.x116 - 69.39622571*m.x117 - 25.39911174*m.x118 + 58.31011875*m.x119 == 0)

m.c36 = Constraint(expr=   m.x120 - 69.39622571*m.x121 - 25.39911174*m.x122 + 58.31011875*m.x123 == 0)

m.c37 = Constraint(expr=   m.x124 + 58.31011875*m.x125 - 69.39622571*m.x126 - 25.39911174*m.x127 == 0)

m.c38 = Constraint(expr= - 69.39622571*m.x106 + m.x128 - 25.39911174*m.x129 + 58.31011875*m.x130 == 0)

m.c39 = Constraint(expr= - 69.39622571*m.x110 + m.x131 + 58.31011875*m.x132 - 25.39911174*m.x133 == 0)

m.c40 = Constraint(expr= - 69.39622571*m.x114 + m.x134 + 58.31011875*m.x135 - 25.39911174*m.x136 == 0)

m.c41 = Constraint(expr= - 69.39622571*m.x117 + m.x137 + 58.31011875*m.x138 - 25.39911174*m.x139 == 0)

m.c42 = Constraint(expr= - 69.39622571*m.x121 + m.x140 - 25.39911174*m.x141 + 58.31011875*m.x142 == 0)

m.c43 = Constraint(expr= - 69.39622571*m.x126 + m.x143 - 25.39911174*m.x144 + 58.31011875*m.x145 == 0)

m.c44 = Constraint(expr=   m.x146 - 2.03724124*m.x147 - 34.92732674*m.x148 + 63.61644904*m.x149 == 0)

m.c45 = Constraint(expr=   m.x150 - 34.92732674*m.x151 + 63.61644904*m.x152 - 2.03724124*m.x153 == 0)

m.c46 = Constraint(expr=   m.x154 - 2.03724124*m.x155 + 63.61644904*m.x156 - 34.92732674*m.x157 == 0)

m.c47 = Constraint(expr=   m.x158 + 63.61644904*m.x159 - 2.03724124*m.x160 - 34.92732674*m.x161 == 0)

m.c48 = Constraint(expr=   m.x162 + 63.61644904*m.x163 - 2.03724124*m.x164 - 34.92732674*m.x165 == 0)

m.c49 = Constraint(expr=   m.x166 + 63.61644904*m.x167 - 34.92732674*m.x168 - 2.03724124*m.x169 == 0)

m.c50 = Constraint(expr= - 34.92732674*m.x148 + m.x170 - 2.03724124*m.x171 + 63.61644904*m.x172 == 0)

m.c51 = Constraint(expr= - 34.92732674*m.x151 + m.x173 + 63.61644904*m.x174 - 2.03724124*m.x175 == 0)

m.c52 = Constraint(expr= - 34.92732674*m.x157 + m.x176 + 63.61644904*m.x177 - 2.03724124*m.x178 == 0)

m.c53 = Constraint(expr= - 34.92732674*m.x161 + m.x179 - 2.03724124*m.x180 + 63.61644904*m.x181 == 0)

m.c54 = Constraint(expr= - 34.92732674*m.x165 + m.x182 + 63.61644904*m.x183 - 2.03724124*m.x184 == 0)

m.c55 = Constraint(expr= - 34.92732674*m.x168 + m.x185 + 63.61644904*m.x186 - 2.03724124*m.x187 == 0)

m.c56 = Constraint(expr=   m.x188 + m.x189 + m.x190 + m.x191 + m.x192 + m.x193 >= 1.752499999)

m.c57 = Constraint(expr= - m.x194 + m.x195 == 0)

m.c58 = Constraint(expr= - m.x196 + m.x197 == 0)

m.c59 = Constraint(expr= - m.x198 + m.x199 == 0)

m.c60 = Constraint(expr= - m.x200 + m.x201 == 0)

m.c61 = Constraint(expr= - m.x202 + m.x203 == 0)

m.c62 = Constraint(expr= - m.x204 + m.x205 == 0)

m.c63 = Constraint(expr= - m.x206 + m.x207 == 0)

m.c64 = Constraint(expr= - m.x208 + m.x209 == 0)

m.c65 = Constraint(expr= - m.x210 + m.x211 == 0)

m.c66 = Constraint(expr= - m.x212 + m.x213 == 0)

m.c67 = Constraint(expr= - m.x214 + m.x215 == 0)

m.c68 = Constraint(expr= - m.x216 + m.x217 == 0)

m.c69 = Constraint(expr=   m.x206 - m.x218 == 0)

m.c70 = Constraint(expr=   m.x208 - m.x219 == 0)

m.c71 = Constraint(expr=   m.x210 - m.x220 == 0)

m.c72 = Constraint(expr=   m.x212 - m.x221 == 0)

m.c73 = Constraint(expr=   m.x214 - m.x222 == 0)

m.c74 = Constraint(expr=   m.x216 - m.x223 == 0)

m.c75 = Constraint(expr= - m.x224 + m.x225 == 0)

m.c76 = Constraint(expr= - m.x226 + m.x227 == 0)

m.c77 = Constraint(expr= - m.x228 + m.x229 == 0)

m.c78 = Constraint(expr= - m.x230 + m.x231 == 0)

m.c79 = Constraint(expr= - m.x232 + m.x233 == 0)

m.c80 = Constraint(expr= - m.x234 + m.x235 == 0)

m.c81 = Constraint(expr=   m.x236 == 0.296666667)

m.c82 = Constraint(expr=   m.x237 == 0.294444444)

m.c83 = Constraint(expr=   m.x238 == 0.283888889)

m.c84 = Constraint(expr=   m.x239 == 0.277222222)

m.c85 = Constraint(expr=   m.x240 == 0.293333333)

m.c86 = Constraint(expr=   m.x241 == 0.306944444)

m.c87 = Constraint(expr=   m.x188 - m.x195 == 0)

m.c88 = Constraint(expr=   m.x189 - m.x197 == 0)

m.c89 = Constraint(expr=   m.x190 - m.x199 == 0)

m.c90 = Constraint(expr=   m.x191 - m.x201 == 0)

m.c91 = Constraint(expr=   m.x192 - m.x203 == 0)

m.c92 = Constraint(expr=   m.x193 - m.x205 == 0)

m.c93 = Constraint(expr=   3600*m.x194 - 3600*m.x207 + 1800*m.x242 - 1800*m.x243 == 0)

m.c94 = Constraint(expr=   3600*m.x196 - 3600*m.x209 + 1800*m.x244 - 1800*m.x245 == 0)

m.c95 = Constraint(expr=   3600*m.x198 - 3600*m.x211 + 1800*m.x246 - 1800*m.x247 == 0)

m.c96 = Constraint(expr=   3600*m.x200 - 3600*m.x213 + 1800*m.x248 - 1800*m.x249 == 0)

m.c97 = Constraint(expr=   3600*m.x202 - 3600*m.x215 + 1800*m.x250 - 1800*m.x251 == 0)

m.c98 = Constraint(expr=   3600*m.x204 - 3600*m.x217 + 1800*m.x252 - 1800*m.x253 == 0)

m.c99 = Constraint(expr=   3600*m.x218 - 3600*m.x225 + 720*m.x254 - 720*m.x255 == 0)

m.c100 = Constraint(expr=   3600*m.x219 - 3600*m.x227 + 720*m.x256 - 720*m.x257 == 0)

m.c101 = Constraint(expr=   3600*m.x220 - 3600*m.x229 + 720*m.x258 - 720*m.x259 == 0)

m.c102 = Constraint(expr=   3600*m.x221 - 3600*m.x231 + 720*m.x260 - 720*m.x261 == 0)

m.c103 = Constraint(expr=   3600*m.x222 - 3600*m.x233 + 720*m.x262 - 720*m.x263 == 0)

m.c104 = Constraint(expr=   3600*m.x223 - 3600*m.x235 + 720*m.x264 - 720*m.x265 == 0)

m.c105 = Constraint(expr=   3600*m.x224 - 3600*m.x236 + 1600*m.x266 - 1600*m.x267 == 0)

m.c106 = Constraint(expr=   3600*m.x226 - 3600*m.x237 + 1600*m.x268 - 1600*m.x269 == 0)

m.c107 = Constraint(expr=   3600*m.x228 - 3600*m.x238 + 1600*m.x270 - 1600*m.x271 == 0)

m.c108 = Constraint(expr=   3600*m.x230 - 3600*m.x239 + 1600*m.x272 - 1600*m.x273 == 0)

m.c109 = Constraint(expr=   3600*m.x232 - 3600*m.x240 + 1600*m.x274 - 1600*m.x275 == 0)

m.c110 = Constraint(expr=   3600*m.x234 - 3600*m.x241 + 1600*m.x276 - 1600*m.x277 == 0)

m.c111 = Constraint(expr= - m.x243 + m.x244 == 0)

m.c112 = Constraint(expr= - m.x245 + m.x246 == 0)

m.c113 = Constraint(expr= - m.x247 + m.x248 == 0)

m.c114 = Constraint(expr= - m.x249 + m.x250 == 0)

m.c115 = Constraint(expr= - m.x251 + m.x252 == 0)

m.c116 = Constraint(expr= - m.x255 + m.x256 == 0)

m.c117 = Constraint(expr= - m.x257 + m.x258 == 0)

m.c118 = Constraint(expr= - m.x259 + m.x260 == 0)

m.c119 = Constraint(expr= - m.x261 + m.x262 == 0)

m.c120 = Constraint(expr= - m.x263 + m.x264 == 0)

m.c121 = Constraint(expr= - m.x267 + m.x268 == 0)

m.c122 = Constraint(expr= - m.x269 + m.x270 == 0)

m.c123 = Constraint(expr= - m.x271 + m.x272 == 0)

m.c124 = Constraint(expr= - m.x273 + m.x274 == 0)

m.c125 = Constraint(expr= - m.x275 + m.x276 == 0)

m.c126 = Constraint(expr= - 0.2*m.b2 + m.x278 >= 0)

m.c127 = Constraint(expr= - 0.2*m.b3 + m.x280 >= 0)

m.c128 = Constraint(expr= - 0.2*m.b4 + m.x282 >= 0)

m.c129 = Constraint(expr= - 0.2*m.b5 + m.x284 >= 0)

m.c130 = Constraint(expr= - 0.2*m.b6 + m.x286 >= 0)

m.c131 = Constraint(expr= - 0.2*m.b7 + m.x288 >= 0)

m.c132 = Constraint(expr= - 0.2*m.b8 + m.x290 >= 0)

m.c133 = Constraint(expr= - 0.2*m.b9 + m.x292 >= 0)

m.c134 = Constraint(expr= - 0.2*m.b10 + m.x294 >= 0)

m.c135 = Constraint(expr= - 0.2*m.b11 + m.x296 >= 0)

m.c136 = Constraint(expr= - 0.2*m.b12 + m.x298 >= 0)

m.c137 = Constraint(expr= - 0.2*m.b13 + m.x300 >= 0)

m.c138 = Constraint(expr= - 0.2*m.b14 + m.x302 >= 0)

m.c139 = Constraint(expr= - 0.2*m.b15 + m.x304 >= 0)

m.c140 = Constraint(expr= - 0.2*m.b16 + m.x306 >= 0)

m.c141 = Constraint(expr= - 0.2*m.b17 + m.x308 >= 0)

m.c142 = Constraint(expr= - 0.2*m.b18 + m.x310 >= 0)

m.c143 = Constraint(expr= - 0.2*m.b19 + m.x312 >= 0)

m.c144 = Constraint(expr= - 0.25*m.b20 + m.x314 >= 0)

m.c145 = Constraint(expr= - 0.25*m.b21 + m.x316 >= 0)

m.c146 = Constraint(expr= - 0.25*m.b22 + m.x318 >= 0)

m.c147 = Constraint(expr= - 0.25*m.b23 + m.x320 >= 0)

m.c148 = Constraint(expr= - 0.25*m.b24 + m.x322 >= 0)

m.c149 = Constraint(expr= - 0.25*m.b25 + m.x324 >= 0)

m.c150 = Constraint(expr= - 0.25*m.b26 + m.x326 >= 0)

m.c151 = Constraint(expr= - 0.25*m.b27 + m.x328 >= 0)

m.c152 = Constraint(expr= - 0.25*m.b28 + m.x330 >= 0)

m.c153 = Constraint(expr= - 0.25*m.b29 + m.x332 >= 0)

m.c154 = Constraint(expr= - 0.25*m.b30 + m.x334 >= 0)

m.c155 = Constraint(expr= - 0.25*m.b31 + m.x336 >= 0)

m.c156 = Constraint(expr= - 0.4*m.b32 + m.x338 >= 0)

m.c157 = Constraint(expr= - 0.4*m.b33 + m.x340 >= 0)

m.c158 = Constraint(expr= - 0.4*m.b34 + m.x342 >= 0)

m.c159 = Constraint(expr= - 0.4*m.b35 + m.x344 >= 0)

m.c160 = Constraint(expr= - 0.4*m.b36 + m.x346 >= 0)

m.c161 = Constraint(expr= - 0.4*m.b37 + m.x348 >= 0)

m.c162 = Constraint(expr= - 0.4*m.b38 + m.x350 >= 0)

m.c163 = Constraint(expr= - 0.4*m.b39 + m.x352 >= 0)

m.c164 = Constraint(expr= - 0.4*m.b40 + m.x354 >= 0)

m.c165 = Constraint(expr= - 0.4*m.b41 + m.x356 >= 0)

m.c166 = Constraint(expr= - 0.4*m.b42 + m.x358 >= 0)

m.c167 = Constraint(expr= - 0.4*m.b43 + m.x360 >= 0)

m.c168 = Constraint(expr= - 0.24*m.b44 + m.x362 >= 0)

m.c169 = Constraint(expr= - 0.24*m.b45 + m.x364 >= 0)

m.c170 = Constraint(expr= - 0.24*m.b46 + m.x366 >= 0)

m.c171 = Constraint(expr= - 0.24*m.b47 + m.x368 >= 0)

m.c172 = Constraint(expr= - 0.24*m.b48 + m.x370 >= 0)

m.c173 = Constraint(expr= - 0.24*m.b49 + m.x372 >= 0)

m.c174 = Constraint(expr= - 0.24*m.b50 + m.x374 >= 0)

m.c175 = Constraint(expr= - 0.24*m.b51 + m.x376 >= 0)

m.c176 = Constraint(expr= - 0.24*m.b52 + m.x378 >= 0)

m.c177 = Constraint(expr= - 0.24*m.b53 + m.x380 >= 0)

m.c178 = Constraint(expr= - 0.24*m.b54 + m.x382 >= 0)

m.c179 = Constraint(expr= - 0.24*m.b55 + m.x384 >= 0)

m.c180 = Constraint(expr= - 0.8*m.b2 + m.x278 <= 0)

m.c181 = Constraint(expr= - 0.8*m.b3 + m.x280 <= 0)

m.c182 = Constraint(expr= - 0.8*m.b4 + m.x282 <= 0)

m.c183 = Constraint(expr= - 0.8*m.b5 + m.x284 <= 0)

m.c184 = Constraint(expr= - 0.8*m.b6 + m.x286 <= 0)

m.c185 = Constraint(expr= - 0.8*m.b7 + m.x288 <= 0)

m.c186 = Constraint(expr= - 0.8*m.b8 + m.x290 <= 0)

m.c187 = Constraint(expr= - 0.8*m.b9 + m.x292 <= 0)

m.c188 = Constraint(expr= - 0.8*m.b10 + m.x294 <= 0)

m.c189 = Constraint(expr= - 0.8*m.b11 + m.x296 <= 0)

m.c190 = Constraint(expr= - 0.8*m.b12 + m.x298 <= 0)

m.c191 = Constraint(expr= - 0.8*m.b13 + m.x300 <= 0)

m.c192 = Constraint(expr= - 0.8*m.b14 + m.x302 <= 0)

m.c193 = Constraint(expr= - 0.8*m.b15 + m.x304 <= 0)

m.c194 = Constraint(expr= - 0.8*m.b16 + m.x306 <= 0)

m.c195 = Constraint(expr= - 0.8*m.b17 + m.x308 <= 0)

m.c196 = Constraint(expr= - 0.8*m.b18 + m.x310 <= 0)

m.c197 = Constraint(expr= - 0.8*m.b19 + m.x312 <= 0)

m.c198 = Constraint(expr= - 0.5*m.b20 + m.x314 <= 0)

m.c199 = Constraint(expr= - 0.5*m.b21 + m.x316 <= 0)

m.c200 = Constraint(expr= - 0.5*m.b22 + m.x318 <= 0)

m.c201 = Constraint(expr= - 0.5*m.b23 + m.x320 <= 0)

m.c202 = Constraint(expr= - 0.5*m.b24 + m.x322 <= 0)

m.c203 = Constraint(expr= - 0.5*m.b25 + m.x324 <= 0)

m.c204 = Constraint(expr= - 0.5*m.b26 + m.x326 <= 0)

m.c205 = Constraint(expr= - 0.5*m.b27 + m.x328 <= 0)

m.c206 = Constraint(expr= - 0.5*m.b28 + m.x330 <= 0)

m.c207 = Constraint(expr= - 0.5*m.b29 + m.x332 <= 0)

m.c208 = Constraint(expr= - 0.5*m.b30 + m.x334 <= 0)

m.c209 = Constraint(expr= - 0.5*m.b31 + m.x336 <= 0)

m.c210 = Constraint(expr= - 0.7*m.b32 + m.x338 <= 0)

m.c211 = Constraint(expr= - 0.7*m.b33 + m.x340 <= 0)

m.c212 = Constraint(expr= - 0.7*m.b34 + m.x342 <= 0)

m.c213 = Constraint(expr= - 0.7*m.b35 + m.x344 <= 0)

m.c214 = Constraint(expr= - 0.7*m.b36 + m.x346 <= 0)

m.c215 = Constraint(expr= - 0.7*m.b37 + m.x348 <= 0)

m.c216 = Constraint(expr= - 0.7*m.b38 + m.x350 <= 0)

m.c217 = Constraint(expr= - 0.7*m.b39 + m.x352 <= 0)

m.c218 = Constraint(expr= - 0.7*m.b40 + m.x354 <= 0)

m.c219 = Constraint(expr= - 0.7*m.b41 + m.x356 <= 0)

m.c220 = Constraint(expr= - 0.7*m.b42 + m.x358 <= 0)

m.c221 = Constraint(expr= - 0.7*m.b43 + m.x360 <= 0)

m.c222 = Constraint(expr= - 0.58*m.b44 + m.x362 <= 0)

m.c223 = Constraint(expr= - 0.58*m.b45 + m.x364 <= 0)

m.c224 = Constraint(expr= - 0.58*m.b46 + m.x366 <= 0)

m.c225 = Constraint(expr= - 0.58*m.b47 + m.x368 <= 0)

m.c226 = Constraint(expr= - 0.58*m.b48 + m.x370 <= 0)

m.c227 = Constraint(expr= - 0.58*m.b49 + m.x372 <= 0)

m.c228 = Constraint(expr= - 0.58*m.b50 + m.x374 <= 0)

m.c229 = Constraint(expr= - 0.58*m.b51 + m.x376 <= 0)

m.c230 = Constraint(expr= - 0.58*m.b52 + m.x378 <= 0)

m.c231 = Constraint(expr= - 0.58*m.b53 + m.x380 <= 0)

m.c232 = Constraint(expr= - 0.58*m.b54 + m.x382 <= 0)

m.c233 = Constraint(expr= - 0.58*m.b55 + m.x384 <= 0)

m.c234 = Constraint(expr= - m.x242 + m.x386 == 60)

m.c235 = Constraint(expr= - m.x244 + m.x387 == 60)

m.c236 = Constraint(expr= - m.x246 + m.x388 == 60)

m.c237 = Constraint(expr= - m.x248 + m.x389 == 60)

m.c238 = Constraint(expr= - m.x250 + m.x390 == 60)

m.c239 = Constraint(expr= - m.x252 + m.x391 == 60)

m.c240 = Constraint(expr= - m.x254 + m.x392 == 90)

m.c241 = Constraint(expr= - m.x256 + m.x393 == 90)

m.c242 = Constraint(expr= - m.x258 + m.x394 == 90)

m.c243 = Constraint(expr= - m.x260 + m.x395 == 90)

m.c244 = Constraint(expr= - m.x262 + m.x396 == 90)

m.c245 = Constraint(expr= - m.x264 + m.x397 == 90)

m.c246 = Constraint(expr= - m.x266 + m.x398 == 103)

m.c247 = Constraint(expr= - m.x268 + m.x399 == 103)

m.c248 = Constraint(expr= - m.x270 + m.x400 == 103)

m.c249 = Constraint(expr= - m.x272 + m.x401 == 103)

m.c250 = Constraint(expr= - m.x274 + m.x402 == 103)

m.c251 = Constraint(expr= - m.x276 + m.x403 == 103)

m.c252 = Constraint(expr= - m.x386 + m.x404 - m.x405 == 0)

m.c253 = Constraint(expr= - m.x387 + m.x406 - m.x407 == 0)

m.c254 = Constraint(expr= - m.x388 + m.x408 - m.x409 == 0)

m.c255 = Constraint(expr= - m.x389 + m.x410 - m.x411 == 0)

m.c256 = Constraint(expr= - m.x390 + m.x412 - m.x413 == 0)

m.c257 = Constraint(expr= - m.x391 + m.x414 - m.x415 == 0)

m.c258 = Constraint(expr=   m.x416 - m.x417 - m.x418 == 0)

m.c259 = Constraint(expr=   m.x419 - m.x420 - m.x421 == 0)

m.c260 = Constraint(expr=   m.x422 - m.x423 - m.x424 == 0)

m.c261 = Constraint(expr=   m.x425 - m.x426 - m.x427 == 0)

m.c262 = Constraint(expr=   m.x428 - m.x429 - m.x430 == 0)

m.c263 = Constraint(expr=   m.x431 - m.x432 - m.x433 == 0)

m.c264 = Constraint(expr= - m.x398 + m.x434 - m.x435 == 0)

m.c265 = Constraint(expr= - m.x399 + m.x436 - m.x437 == 0)

m.c266 = Constraint(expr= - m.x400 + m.x438 - m.x439 == 0)

m.c267 = Constraint(expr= - m.x401 + m.x440 - m.x441 == 0)

m.c268 = Constraint(expr= - m.x402 + m.x442 - m.x443 == 0)

m.c269 = Constraint(expr= - m.x403 + m.x444 - m.x445 == 0)

m.c270 = Constraint(expr=   m.x404 - m.x446 - m.x447 == 0)

m.c271 = Constraint(expr=   m.x406 - m.x448 - m.x449 == 0)

m.c272 = Constraint(expr=   m.x408 - m.x450 - m.x451 == 0)

m.c273 = Constraint(expr=   m.x410 - m.x452 - m.x453 == 0)

m.c274 = Constraint(expr=   m.x412 - m.x454 - m.x455 == 0)

m.c275 = Constraint(expr=   m.x414 - m.x456 - m.x457 == 0)

m.c276 = Constraint(expr= - m.x386 + m.x416 - m.x458 == 0)

m.c277 = Constraint(expr= - m.x387 + m.x419 - m.x459 == 0)

m.c278 = Constraint(expr= - m.x388 + m.x422 - m.x460 == 0)

m.c279 = Constraint(expr= - m.x389 + m.x425 - m.x461 == 0)

m.c280 = Constraint(expr= - m.x390 + m.x428 - m.x462 == 0)

m.c281 = Constraint(expr= - m.x391 + m.x431 - m.x463 == 0)

m.c282 = Constraint(expr= - m.x392 + m.x434 - m.x464 == 0)

m.c283 = Constraint(expr= - m.x393 + m.x436 - m.x465 == 0)

m.c284 = Constraint(expr= - m.x394 + m.x438 - m.x466 == 0)

m.c285 = Constraint(expr= - m.x395 + m.x440 - m.x467 == 0)

m.c286 = Constraint(expr= - m.x396 + m.x442 - m.x468 == 0)

m.c287 = Constraint(expr= - m.x397 + m.x444 - m.x469 == 0)

m.c288 = Constraint(expr=   0.2*m.b2 - m.x278 + m.x470 <= 0.2)

m.c289 = Constraint(expr=   0.2*m.b3 - m.x280 + m.x471 <= 0.2)

m.c290 = Constraint(expr=   0.2*m.b4 - m.x282 + m.x472 <= 0.2)

m.c291 = Constraint(expr=   0.2*m.b5 - m.x284 + m.x473 <= 0.2)

m.c292 = Constraint(expr=   0.2*m.b6 - m.x286 + m.x474 <= 0.2)

m.c293 = Constraint(expr=   0.2*m.b7 - m.x288 + m.x475 <= 0.2)

m.c294 = Constraint(expr=   0.2*m.b8 - m.x290 + m.x476 <= 0.2)

m.c295 = Constraint(expr=   0.2*m.b9 - m.x292 + m.x477 <= 0.2)

m.c296 = Constraint(expr=   0.2*m.b10 - m.x294 + m.x478 <= 0.2)

m.c297 = Constraint(expr=   0.2*m.b11 - m.x296 + m.x479 <= 0.2)

m.c298 = Constraint(expr=   0.2*m.b12 - m.x298 + m.x480 <= 0.2)

m.c299 = Constraint(expr=   0.2*m.b13 - m.x300 + m.x481 <= 0.2)

m.c300 = Constraint(expr=   0.2*m.b14 - m.x302 + m.x482 <= 0.2)

m.c301 = Constraint(expr=   0.2*m.b15 - m.x304 + m.x483 <= 0.2)

m.c302 = Constraint(expr=   0.2*m.b16 - m.x306 + m.x484 <= 0.2)

m.c303 = Constraint(expr=   0.2*m.b17 - m.x308 + m.x485 <= 0.2)

m.c304 = Constraint(expr=   0.2*m.b18 - m.x310 + m.x486 <= 0.2)

m.c305 = Constraint(expr=   0.2*m.b19 - m.x312 + m.x487 <= 0.2)

m.c306 = Constraint(expr=   0.25*m.b20 - m.x314 + m.x488 <= 0.25)

m.c307 = Constraint(expr=   0.25*m.b21 - m.x316 + m.x489 <= 0.25)

m.c308 = Constraint(expr=   0.25*m.b22 - m.x318 + m.x490 <= 0.25)

m.c309 = Constraint(expr=   0.25*m.b23 - m.x320 + m.x491 <= 0.25)

m.c310 = Constraint(expr=   0.25*m.b24 - m.x322 + m.x492 <= 0.25)

m.c311 = Constraint(expr=   0.25*m.b25 - m.x324 + m.x493 <= 0.25)

m.c312 = Constraint(expr=   0.25*m.b26 - m.x326 + m.x494 <= 0.25)

m.c313 = Constraint(expr=   0.25*m.b27 - m.x328 + m.x495 <= 0.25)

m.c314 = Constraint(expr=   0.25*m.b28 - m.x330 + m.x496 <= 0.25)

m.c315 = Constraint(expr=   0.25*m.b29 - m.x332 + m.x497 <= 0.25)

m.c316 = Constraint(expr=   0.25*m.b30 - m.x334 + m.x498 <= 0.25)

m.c317 = Constraint(expr=   0.25*m.b31 - m.x336 + m.x499 <= 0.25)

m.c318 = Constraint(expr=   0.4*m.b32 - m.x338 + m.x500 <= 0.4)

m.c319 = Constraint(expr=   0.4*m.b33 - m.x340 + m.x501 <= 0.4)

m.c320 = Constraint(expr=   0.4*m.b34 - m.x342 + m.x502 <= 0.4)

m.c321 = Constraint(expr=   0.4*m.b35 - m.x344 + m.x503 <= 0.4)

m.c322 = Constraint(expr=   0.4*m.b36 - m.x346 + m.x504 <= 0.4)

m.c323 = Constraint(expr=   0.4*m.b37 - m.x348 + m.x505 <= 0.4)

m.c324 = Constraint(expr=   0.4*m.b38 - m.x350 + m.x506 <= 0.4)

m.c325 = Constraint(expr=   0.4*m.b39 - m.x352 + m.x507 <= 0.4)

m.c326 = Constraint(expr=   0.4*m.b40 - m.x354 + m.x508 <= 0.4)

m.c327 = Constraint(expr=   0.4*m.b41 - m.x356 + m.x509 <= 0.4)

m.c328 = Constraint(expr=   0.4*m.b42 - m.x358 + m.x510 <= 0.4)

m.c329 = Constraint(expr=   0.4*m.b43 - m.x360 + m.x511 <= 0.4)

m.c330 = Constraint(expr=   0.24*m.b44 - m.x362 + m.x512 <= 0.24)

m.c331 = Constraint(expr=   0.24*m.b45 - m.x364 + m.x513 <= 0.24)

m.c332 = Constraint(expr=   0.24*m.b46 - m.x366 + m.x514 <= 0.24)

m.c333 = Constraint(expr=   0.24*m.b47 - m.x368 + m.x515 <= 0.24)

m.c334 = Constraint(expr=   0.24*m.b48 - m.x370 + m.x516 <= 0.24)

m.c335 = Constraint(expr=   0.24*m.b49 - m.x372 + m.x517 <= 0.24)

m.c336 = Constraint(expr=   0.24*m.b50 - m.x374 + m.x518 <= 0.24)

m.c337 = Constraint(expr=   0.24*m.b51 - m.x376 + m.x519 <= 0.24)

m.c338 = Constraint(expr=   0.24*m.b52 - m.x378 + m.x520 <= 0.24)

m.c339 = Constraint(expr=   0.24*m.b53 - m.x380 + m.x521 <= 0.24)

m.c340 = Constraint(expr=   0.24*m.b54 - m.x382 + m.x522 <= 0.24)

m.c341 = Constraint(expr=   0.24*m.b55 - m.x384 + m.x523 <= 0.24)

m.c342 = Constraint(expr= - m.x278 + m.x470 >= 0)

m.c343 = Constraint(expr= - m.x280 + m.x471 >= 0)

m.c344 = Constraint(expr= - m.x282 + m.x472 >= 0)

m.c345 = Constraint(expr= - m.x284 + m.x473 >= 0)

m.c346 = Constraint(expr= - m.x286 + m.x474 >= 0)

m.c347 = Constraint(expr= - m.x288 + m.x475 >= 0)

m.c348 = Constraint(expr= - m.x290 + m.x476 >= 0)

m.c349 = Constraint(expr= - m.x292 + m.x477 >= 0)

m.c350 = Constraint(expr= - m.x294 + m.x478 >= 0)

m.c351 = Constraint(expr= - m.x296 + m.x479 >= 0)

m.c352 = Constraint(expr= - m.x298 + m.x480 >= 0)

m.c353 = Constraint(expr= - m.x300 + m.x481 >= 0)

m.c354 = Constraint(expr= - m.x302 + m.x482 >= 0)

m.c355 = Constraint(expr= - m.x304 + m.x483 >= 0)

m.c356 = Constraint(expr= - m.x306 + m.x484 >= 0)

m.c357 = Constraint(expr= - m.x308 + m.x485 >= 0)

m.c358 = Constraint(expr= - m.x310 + m.x486 >= 0)

m.c359 = Constraint(expr= - m.x312 + m.x487 >= 0)

m.c360 = Constraint(expr= - m.x314 + m.x488 >= 0)

m.c361 = Constraint(expr= - m.x316 + m.x489 >= 0)

m.c362 = Constraint(expr= - m.x318 + m.x490 >= 0)

m.c363 = Constraint(expr= - m.x320 + m.x491 >= 0)

m.c364 = Constraint(expr= - m.x322 + m.x492 >= 0)

m.c365 = Constraint(expr= - m.x324 + m.x493 >= 0)

m.c366 = Constraint(expr= - m.x326 + m.x494 >= 0)

m.c367 = Constraint(expr= - m.x328 + m.x495 >= 0)

m.c368 = Constraint(expr= - m.x330 + m.x496 >= 0)

m.c369 = Constraint(expr= - m.x332 + m.x497 >= 0)

m.c370 = Constraint(expr= - m.x334 + m.x498 >= 0)

m.c371 = Constraint(expr= - m.x336 + m.x499 >= 0)

m.c372 = Constraint(expr= - m.x338 + m.x500 >= 0)

m.c373 = Constraint(expr= - m.x340 + m.x501 >= 0)

m.c374 = Constraint(expr= - m.x342 + m.x502 >= 0)

m.c375 = Constraint(expr= - m.x344 + m.x503 >= 0)

m.c376 = Constraint(expr= - m.x346 + m.x504 >= 0)

m.c377 = Constraint(expr= - m.x348 + m.x505 >= 0)

m.c378 = Constraint(expr= - m.x350 + m.x506 >= 0)

m.c379 = Constraint(expr= - m.x352 + m.x507 >= 0)

m.c380 = Constraint(expr= - m.x354 + m.x508 >= 0)

m.c381 = Constraint(expr= - m.x356 + m.x509 >= 0)

m.c382 = Constraint(expr= - m.x358 + m.x510 >= 0)

m.c383 = Constraint(expr= - m.x360 + m.x511 >= 0)

m.c384 = Constraint(expr= - m.x362 + m.x512 >= 0)

m.c385 = Constraint(expr= - m.x364 + m.x513 >= 0)

m.c386 = Constraint(expr= - m.x366 + m.x514 >= 0)

m.c387 = Constraint(expr= - m.x368 + m.x515 >= 0)

m.c388 = Constraint(expr= - m.x370 + m.x516 >= 0)

m.c389 = Constraint(expr= - m.x372 + m.x517 >= 0)

m.c390 = Constraint(expr= - m.x374 + m.x518 >= 0)

m.c391 = Constraint(expr= - m.x376 + m.x519 >= 0)

m.c392 = Constraint(expr= - m.x378 + m.x520 >= 0)

m.c393 = Constraint(expr= - m.x380 + m.x521 >= 0)

m.c394 = Constraint(expr= - m.x382 + m.x522 >= 0)

m.c395 = Constraint(expr= - m.x384 + m.x523 >= 0)

m.c396 = Constraint(expr= - 0.6*m.b2 + m.x470 <= 0.2)

m.c397 = Constraint(expr= - 0.6*m.b3 + m.x471 <= 0.2)

m.c398 = Constraint(expr= - 0.6*m.b4 + m.x472 <= 0.2)

m.c399 = Constraint(expr= - 0.6*m.b5 + m.x473 <= 0.2)

m.c400 = Constraint(expr= - 0.6*m.b6 + m.x474 <= 0.2)

m.c401 = Constraint(expr= - 0.6*m.b7 + m.x475 <= 0.2)

m.c402 = Constraint(expr= - 0.6*m.b8 + m.x476 <= 0.2)

m.c403 = Constraint(expr= - 0.6*m.b9 + m.x477 <= 0.2)

m.c404 = Constraint(expr= - 0.6*m.b10 + m.x478 <= 0.2)

m.c405 = Constraint(expr= - 0.6*m.b11 + m.x479 <= 0.2)

m.c406 = Constraint(expr= - 0.6*m.b12 + m.x480 <= 0.2)

m.c407 = Constraint(expr= - 0.6*m.b13 + m.x481 <= 0.2)

m.c408 = Constraint(expr= - 0.6*m.b14 + m.x482 <= 0.2)

m.c409 = Constraint(expr= - 0.6*m.b15 + m.x483 <= 0.2)

m.c410 = Constraint(expr= - 0.6*m.b16 + m.x484 <= 0.2)

m.c411 = Constraint(expr= - 0.6*m.b17 + m.x485 <= 0.2)

m.c412 = Constraint(expr= - 0.6*m.b18 + m.x486 <= 0.2)

m.c413 = Constraint(expr= - 0.6*m.b19 + m.x487 <= 0.2)

m.c414 = Constraint(expr= - 0.25*m.b20 + m.x488 <= 0.25)

m.c415 = Constraint(expr= - 0.25*m.b21 + m.x489 <= 0.25)

m.c416 = Constraint(expr= - 0.25*m.b22 + m.x490 <= 0.25)

m.c417 = Constraint(expr= - 0.25*m.b23 + m.x491 <= 0.25)

m.c418 = Constraint(expr= - 0.25*m.b24 + m.x492 <= 0.25)

m.c419 = Constraint(expr= - 0.25*m.b25 + m.x493 <= 0.25)

m.c420 = Constraint(expr= - 0.25*m.b26 + m.x494 <= 0.25)

m.c421 = Constraint(expr= - 0.25*m.b27 + m.x495 <= 0.25)

m.c422 = Constraint(expr= - 0.25*m.b28 + m.x496 <= 0.25)

m.c423 = Constraint(expr= - 0.25*m.b29 + m.x497 <= 0.25)

m.c424 = Constraint(expr= - 0.25*m.b30 + m.x498 <= 0.25)

m.c425 = Constraint(expr= - 0.25*m.b31 + m.x499 <= 0.25)

m.c426 = Constraint(expr= - 0.3*m.b32 + m.x500 <= 0.4)

m.c427 = Constraint(expr= - 0.3*m.b33 + m.x501 <= 0.4)

m.c428 = Constraint(expr= - 0.3*m.b34 + m.x502 <= 0.4)

m.c429 = Constraint(expr= - 0.3*m.b35 + m.x503 <= 0.4)

m.c430 = Constraint(expr= - 0.3*m.b36 + m.x504 <= 0.4)

m.c431 = Constraint(expr= - 0.3*m.b37 + m.x505 <= 0.4)

m.c432 = Constraint(expr= - 0.3*m.b38 + m.x506 <= 0.4)

m.c433 = Constraint(expr= - 0.3*m.b39 + m.x507 <= 0.4)

m.c434 = Constraint(expr= - 0.3*m.b40 + m.x508 <= 0.4)

m.c435 = Constraint(expr= - 0.3*m.b41 + m.x509 <= 0.4)

m.c436 = Constraint(expr= - 0.3*m.b42 + m.x510 <= 0.4)

m.c437 = Constraint(expr= - 0.3*m.b43 + m.x511 <= 0.4)

m.c438 = Constraint(expr= - 0.34*m.b44 + m.x512 <= 0.24)

m.c439 = Constraint(expr= - 0.34*m.b45 + m.x513 <= 0.24)

m.c440 = Constraint(expr= - 0.34*m.b46 + m.x514 <= 0.24)

m.c441 = Constraint(expr= - 0.34*m.b47 + m.x515 <= 0.24)

m.c442 = Constraint(expr= - 0.34*m.b48 + m.x516 <= 0.24)

m.c443 = Constraint(expr= - 0.34*m.b49 + m.x517 <= 0.24)

m.c444 = Constraint(expr= - 0.34*m.b50 + m.x518 <= 0.24)

m.c445 = Constraint(expr= - 0.34*m.b51 + m.x519 <= 0.24)

m.c446 = Constraint(expr= - 0.34*m.b52 + m.x520 <= 0.24)

m.c447 = Constraint(expr= - 0.34*m.b53 + m.x521 <= 0.24)

m.c448 = Constraint(expr= - 0.34*m.b54 + m.x522 <= 0.24)

m.c449 = Constraint(expr= - 0.34*m.b55 + m.x523 <= 0.24)

m.c450 = Constraint(expr= - 0.4*m.b2 + m.x524 <= 0.6)

m.c451 = Constraint(expr= - 0.4*m.b3 + m.x525 <= 0.6)

m.c452 = Constraint(expr= - 0.4*m.b4 + m.x526 <= 0.6)

m.c453 = Constraint(expr= - 0.4*m.b5 + m.x527 <= 0.6)

m.c454 = Constraint(expr= - 0.4*m.b6 + m.x528 <= 0.6)

m.c455 = Constraint(expr= - 0.4*m.b7 + m.x529 <= 0.6)

m.c456 = Constraint(expr= - 0.2*m.b20 + m.x530 <= 0.8)

m.c457 = Constraint(expr= - 0.2*m.b21 + m.x531 <= 0.8)

m.c458 = Constraint(expr= - 0.2*m.b22 + m.x532 <= 0.8)

m.c459 = Constraint(expr= - 0.2*m.b23 + m.x533 <= 0.8)

m.c460 = Constraint(expr= - 0.2*m.b24 + m.x534 <= 0.8)

m.c461 = Constraint(expr= - 0.2*m.b25 + m.x535 <= 0.8)

m.c462 = Constraint(expr= - 0.15*m.b32 + m.x536 <= 0.85)

m.c463 = Constraint(expr= - 0.15*m.b33 + m.x537 <= 0.85)

m.c464 = Constraint(expr= - 0.15*m.b34 + m.x538 <= 0.85)

m.c465 = Constraint(expr= - 0.15*m.b35 + m.x539 <= 0.85)

m.c466 = Constraint(expr= - 0.15*m.b36 + m.x540 <= 0.85)

m.c467 = Constraint(expr= - 0.15*m.b37 + m.x541 <= 0.85)

m.c468 = Constraint(expr= - 0.3*m.b44 + m.x542 <= 0.7)

m.c469 = Constraint(expr= - 0.3*m.b45 + m.x543 <= 0.7)

m.c470 = Constraint(expr= - 0.3*m.b46 + m.x544 <= 0.7)

m.c471 = Constraint(expr= - 0.3*m.b47 + m.x545 <= 0.7)

m.c472 = Constraint(expr= - 0.3*m.b48 + m.x546 <= 0.7)

m.c473 = Constraint(expr= - 0.3*m.b49 + m.x547 <= 0.7)

m.c474 = Constraint(expr=   m.b2 - m.b8 >= 0)

m.c475 = Constraint(expr=   m.b3 - m.b9 >= 0)

m.c476 = Constraint(expr=   m.b4 - m.b10 >= 0)

m.c477 = Constraint(expr=   m.b5 - m.b11 >= 0)

m.c478 = Constraint(expr=   m.b6 - m.b12 >= 0)

m.c479 = Constraint(expr=   m.b7 - m.b13 >= 0)

m.c480 = Constraint(expr=   m.b8 - m.b14 >= 0)

m.c481 = Constraint(expr=   m.b9 - m.b15 >= 0)

m.c482 = Constraint(expr=   m.b10 - m.b16 >= 0)

m.c483 = Constraint(expr=   m.b11 - m.b17 >= 0)

m.c484 = Constraint(expr=   m.b12 - m.b18 >= 0)

m.c485 = Constraint(expr=   m.b13 - m.b19 >= 0)

m.c486 = Constraint(expr=   m.b20 - m.b26 >= 0)

m.c487 = Constraint(expr=   m.b21 - m.b27 >= 0)

m.c488 = Constraint(expr=   m.b22 - m.b28 >= 0)

m.c489 = Constraint(expr=   m.b23 - m.b29 >= 0)

m.c490 = Constraint(expr=   m.b24 - m.b30 >= 0)

m.c491 = Constraint(expr=   m.b25 - m.b31 >= 0)

m.c492 = Constraint(expr=   m.b32 - m.b38 >= 0)

m.c493 = Constraint(expr=   m.b33 - m.b39 >= 0)

m.c494 = Constraint(expr=   m.b34 - m.b40 >= 0)

m.c495 = Constraint(expr=   m.b35 - m.b41 >= 0)

m.c496 = Constraint(expr=   m.b36 - m.b42 >= 0)

m.c497 = Constraint(expr=   m.b37 - m.b43 >= 0)

m.c498 = Constraint(expr=   m.b44 - m.b50 >= 0)

m.c499 = Constraint(expr=   m.b45 - m.b51 >= 0)

m.c500 = Constraint(expr=   m.b46 - m.b52 >= 0)

m.c501 = Constraint(expr=   m.b47 - m.b53 >= 0)

m.c502 = Constraint(expr=   m.b48 - m.b54 >= 0)

m.c503 = Constraint(expr=   m.b49 - m.b55 >= 0)

m.c504 = Constraint(expr=   m.x195 - m.x278 - m.x290 - m.x302 == 0)

m.c505 = Constraint(expr=   m.x197 - m.x280 - m.x292 - m.x304 == 0)

m.c506 = Constraint(expr=   m.x199 - m.x282 - m.x294 - m.x306 == 0)

m.c507 = Constraint(expr=   m.x201 - m.x284 - m.x296 - m.x308 == 0)

m.c508 = Constraint(expr=   m.x203 - m.x286 - m.x298 - m.x310 == 0)

m.c509 = Constraint(expr=   m.x205 - m.x288 - m.x300 - m.x312 == 0)

m.c510 = Constraint(expr=   m.x207 - m.x314 - m.x326 - m.x338 - m.x350 == 0)

m.c511 = Constraint(expr=   m.x209 - m.x316 - m.x328 - m.x340 - m.x352 == 0)

m.c512 = Constraint(expr=   m.x211 - m.x318 - m.x330 - m.x342 - m.x354 == 0)

m.c513 = Constraint(expr=   m.x213 - m.x320 - m.x332 - m.x344 - m.x356 == 0)

m.c514 = Constraint(expr=   m.x215 - m.x322 - m.x334 - m.x346 - m.x358 == 0)

m.c515 = Constraint(expr=   m.x217 - m.x324 - m.x336 - m.x348 - m.x360 == 0)

m.c516 = Constraint(expr=   m.x225 - m.x362 - m.x374 == 0)

m.c517 = Constraint(expr=   m.x227 - m.x364 - m.x376 == 0)

m.c518 = Constraint(expr=   m.x229 - m.x366 - m.x378 == 0)

m.c519 = Constraint(expr=   m.x231 - m.x368 - m.x380 == 0)

m.c520 = Constraint(expr=   m.x233 - m.x370 - m.x382 == 0)

m.c521 = Constraint(expr=   m.x235 - m.x372 - m.x384 == 0)

m.c522 = Constraint(expr= - 2000*m.b2 + m.x279 - m.x447 >= -2000)

m.c523 = Constraint(expr= - 2000*m.b3 + m.x287 - m.x449 >= -2000)

m.c524 = Constraint(expr= - 2000*m.b4 + m.x295 - m.x451 >= -2000)

m.c525 = Constraint(expr= - 2000*m.b5 + m.x303 - m.x453 >= -2000)

m.c526 = Constraint(expr= - 2000*m.b6 + m.x311 - m.x455 >= -2000)

m.c527 = Constraint(expr= - 2000*m.b7 + m.x319 - m.x457 >= -2000)

m.c528 = Constraint(expr= - 2000*m.b8 + m.x327 - m.x447 >= -2000)

m.c529 = Constraint(expr= - 2000*m.b9 + m.x333 - m.x449 >= -2000)

m.c530 = Constraint(expr= - 2000*m.b10 + m.x339 - m.x451 >= -2000)

m.c531 = Constraint(expr= - 2000*m.b11 + m.x345 - m.x453 >= -2000)

m.c532 = Constraint(expr= - 2000*m.b12 + m.x351 - m.x455 >= -2000)

m.c533 = Constraint(expr= - 2000*m.b13 + m.x357 - m.x457 >= -2000)

m.c534 = Constraint(expr= - 2000*m.b14 + m.x363 - m.x447 >= -2000)

m.c535 = Constraint(expr= - 2000*m.b15 + m.x369 - m.x449 >= -2000)

m.c536 = Constraint(expr= - 2000*m.b16 + m.x375 - m.x451 >= -2000)

m.c537 = Constraint(expr= - 2000*m.b17 + m.x381 - m.x453 >= -2000)

m.c538 = Constraint(expr= - 2000*m.b18 + m.x56 - m.x455 >= -2000)

m.c539 = Constraint(expr= - 2000*m.b19 + m.x59 - m.x457 >= -2000)

m.c540 = Constraint(expr= - 2000*m.b20 + m.x62 - m.x458 >= -2000)

m.c541 = Constraint(expr= - 2000*m.b21 + m.x66 - m.x459 >= -2000)

m.c542 = Constraint(expr= - 2000*m.b22 + m.x70 - m.x460 >= -2000)

m.c543 = Constraint(expr= - 2000*m.b23 + m.x74 - m.x461 >= -2000)

m.c544 = Constraint(expr= - 2000*m.b24 + m.x78 - m.x462 >= -2000)

m.c545 = Constraint(expr= - 2000*m.b25 + m.x82 - m.x463 >= -2000)

m.c546 = Constraint(expr= - 2000*m.b26 + m.x86 - m.x458 >= -2000)

m.c547 = Constraint(expr= - 2000*m.b27 + m.x89 - m.x459 >= -2000)

m.c548 = Constraint(expr= - 2000*m.b28 + m.x92 - m.x460 >= -2000)

m.c549 = Constraint(expr= - 2000*m.b29 + m.x95 - m.x461 >= -2000)

m.c550 = Constraint(expr= - 2000*m.b30 + m.x98 - m.x462 >= -2000)

m.c551 = Constraint(expr= - 2000*m.b31 + m.x101 - m.x463 >= -2000)

m.c552 = Constraint(expr= - 2000*m.b32 + m.x104 - m.x458 >= -2000)

m.c553 = Constraint(expr= - 2000*m.b33 + m.x108 - m.x459 >= -2000)

m.c554 = Constraint(expr= - 2000*m.b34 + m.x112 - m.x460 >= -2000)

m.c555 = Constraint(expr= - 2000*m.b35 + m.x116 - m.x461 >= -2000)

m.c556 = Constraint(expr= - 2000*m.b36 + m.x120 - m.x462 >= -2000)

m.c557 = Constraint(expr= - 2000*m.b37 + m.x124 - m.x463 >= -2000)

m.c558 = Constraint(expr= - 2000*m.b38 + m.x128 - m.x458 >= -2000)

m.c559 = Constraint(expr= - 2000*m.b39 + m.x131 - m.x459 >= -2000)

m.c560 = Constraint(expr= - 2000*m.b40 + m.x134 - m.x460 >= -2000)

m.c561 = Constraint(expr= - 2000*m.b41 + m.x137 - m.x461 >= -2000)

m.c562 = Constraint(expr= - 2000*m.b42 + m.x140 - m.x462 >= -2000)

m.c563 = Constraint(expr= - 2000*m.b43 + m.x143 - m.x463 >= -2000)

m.c564 = Constraint(expr= - 2000*m.b44 + m.x146 - m.x464 >= -2000)

m.c565 = Constraint(expr= - 2000*m.b45 + m.x150 - m.x465 >= -2000)

m.c566 = Constraint(expr= - 2000*m.b46 + m.x154 - m.x466 >= -2000)

m.c567 = Constraint(expr= - 2000*m.b47 + m.x158 - m.x467 >= -2000)

m.c568 = Constraint(expr= - 2000*m.b48 + m.x162 - m.x468 >= -2000)

m.c569 = Constraint(expr= - 2000*m.b49 + m.x166 - m.x469 >= -2000)

m.c570 = Constraint(expr= - 2000*m.b50 + m.x170 - m.x464 >= -2000)

m.c571 = Constraint(expr= - 2000*m.b51 + m.x173 - m.x465 >= -2000)

m.c572 = Constraint(expr= - 2000*m.b52 + m.x176 - m.x466 >= -2000)

m.c573 = Constraint(expr= - 2000*m.b53 + m.x179 - m.x467 >= -2000)

m.c574 = Constraint(expr= - 2000*m.b54 + m.x182 - m.x468 >= -2000)

m.c575 = Constraint(expr= - 2000*m.b55 + m.x185 - m.x469 >= -2000)

m.c576 = Constraint(expr=   1049*m.b2 + m.x279 - m.x447 <= 1049)

m.c577 = Constraint(expr=   1049*m.b3 + m.x287 - m.x449 <= 1049)

m.c578 = Constraint(expr=   1049*m.b4 + m.x295 - m.x451 <= 1049)

m.c579 = Constraint(expr=   1049*m.b5 + m.x303 - m.x453 <= 1049)

m.c580 = Constraint(expr=   1049*m.b6 + m.x311 - m.x455 <= 1049)

m.c581 = Constraint(expr=   1049*m.b7 + m.x319 - m.x457 <= 1049)

m.c582 = Constraint(expr=   1049*m.b8 + m.x327 - m.x447 <= 1049)

m.c583 = Constraint(expr=   1049*m.b9 + m.x333 - m.x449 <= 1049)

m.c584 = Constraint(expr=   1049*m.b10 + m.x339 - m.x451 <= 1049)

m.c585 = Constraint(expr=   1049*m.b11 + m.x345 - m.x453 <= 1049)

m.c586 = Constraint(expr=   1049*m.b12 + m.x351 - m.x455 <= 1049)

m.c587 = Constraint(expr=   1049*m.b13 + m.x357 - m.x457 <= 1049)

m.c588 = Constraint(expr=   1049*m.b14 + m.x363 - m.x447 <= 1049)

m.c589 = Constraint(expr=   1049*m.b15 + m.x369 - m.x449 <= 1049)

m.c590 = Constraint(expr=   1049*m.b16 + m.x375 - m.x451 <= 1049)

m.c591 = Constraint(expr=   1049*m.b17 + m.x381 - m.x453 <= 1049)

m.c592 = Constraint(expr=   1049*m.b18 + m.x56 - m.x455 <= 1049)

m.c593 = Constraint(expr=   1049*m.b19 + m.x59 - m.x457 <= 1049)

m.c594 = Constraint(expr=   1065*m.b20 + m.x62 - m.x458 <= 1065)

m.c595 = Constraint(expr=   1065*m.b21 + m.x66 - m.x459 <= 1065)

m.c596 = Constraint(expr=   1065*m.b22 + m.x70 - m.x460 <= 1065)

m.c597 = Constraint(expr=   1065*m.b23 + m.x74 - m.x461 <= 1065)

m.c598 = Constraint(expr=   1065*m.b24 + m.x78 - m.x462 <= 1065)

m.c599 = Constraint(expr=   1065*m.b25 + m.x82 - m.x463 <= 1065)

m.c600 = Constraint(expr=   1065*m.b26 + m.x86 - m.x458 <= 1065)

m.c601 = Constraint(expr=   1065*m.b27 + m.x89 - m.x459 <= 1065)

m.c602 = Constraint(expr=   1065*m.b28 + m.x92 - m.x460 <= 1065)

m.c603 = Constraint(expr=   1065*m.b29 + m.x95 - m.x461 <= 1065)

m.c604 = Constraint(expr=   1065*m.b30 + m.x98 - m.x462 <= 1065)

m.c605 = Constraint(expr=   1065*m.b31 + m.x101 - m.x463 <= 1065)

m.c606 = Constraint(expr=   1065*m.b32 + m.x104 - m.x458 <= 1065)

m.c607 = Constraint(expr=   1065*m.b33 + m.x108 - m.x459 <= 1065)

m.c608 = Constraint(expr=   1065*m.b34 + m.x112 - m.x460 <= 1065)

m.c609 = Constraint(expr=   1065*m.b35 + m.x116 - m.x461 <= 1065)

m.c610 = Constraint(expr=   1065*m.b36 + m.x120 - m.x462 <= 1065)

m.c611 = Constraint(expr=   1065*m.b37 + m.x124 - m.x463 <= 1065)

m.c612 = Constraint(expr=   1065*m.b38 + m.x128 - m.x458 <= 1065)

m.c613 = Constraint(expr=   1065*m.b39 + m.x131 - m.x459 <= 1065)

m.c614 = Constraint(expr=   1065*m.b40 + m.x134 - m.x460 <= 1065)

m.c615 = Constraint(expr=   1065*m.b41 + m.x137 - m.x461 <= 1065)

m.c616 = Constraint(expr=   1065*m.b42 + m.x140 - m.x462 <= 1065)

m.c617 = Constraint(expr=   1065*m.b43 + m.x143 - m.x463 <= 1065)

m.c618 = Constraint(expr=   1095*m.b44 + m.x146 - m.x464 <= 1095)

m.c619 = Constraint(expr=   1095*m.b45 + m.x150 - m.x465 <= 1095)

m.c620 = Constraint(expr=   1095*m.b46 + m.x154 - m.x466 <= 1095)

m.c621 = Constraint(expr=   1095*m.b47 + m.x158 - m.x467 <= 1095)

m.c622 = Constraint(expr=   1095*m.b48 + m.x162 - m.x468 <= 1095)

m.c623 = Constraint(expr=   1095*m.b49 + m.x166 - m.x469 <= 1095)

m.c624 = Constraint(expr=   1095*m.b50 + m.x170 - m.x464 <= 1095)

m.c625 = Constraint(expr=   1095*m.b51 + m.x173 - m.x465 <= 1095)

m.c626 = Constraint(expr=   1095*m.b52 + m.x176 - m.x466 <= 1095)

m.c627 = Constraint(expr=   1095*m.b53 + m.x179 - m.x467 <= 1095)

m.c628 = Constraint(expr=   1095*m.b54 + m.x182 - m.x468 <= 1095)

m.c629 = Constraint(expr=   1095*m.b55 + m.x185 - m.x469 <= 1095)

m.c630 = Constraint(expr= - m.x392 + m.x417 >= 0)

m.c631 = Constraint(expr= - m.x393 + m.x420 >= 0)

m.c632 = Constraint(expr= - m.x394 + m.x423 >= 0)

m.c633 = Constraint(expr= - m.x395 + m.x426 >= 0)

m.c634 = Constraint(expr= - m.x396 + m.x429 >= 0)

m.c635 = Constraint(expr= - m.x397 + m.x432 >= 0)

m.c636 = Constraint(expr=   m.x398 - m.x548 >= 0)

m.c637 = Constraint(expr=   m.x399 - m.x549 >= 0)

m.c638 = Constraint(expr=   m.x400 - m.x550 >= 0)

m.c639 = Constraint(expr=   m.x401 - m.x551 >= 0)

m.c640 = Constraint(expr=   m.x402 - m.x552 >= 0)

m.c641 = Constraint(expr=   m.x403 - m.x553 >= 0)

m.c642 = Constraint(expr= - 0.309838295393634*m.x554 + 13.94696158*m.x555 + 24.46510819*m.x556 - 7.28623839*m.x557
                          - 23.57687014*m.x558 <= 0)

m.c643 = Constraint(expr= - 7.28623839*m.x559 - 23.57687014*m.x560 - 0.309838295393634*m.x561 + 13.94696158*m.x562
                          + 24.46510819*m.x563 <= 0)

m.c644 = Constraint(expr=   13.94696158*m.x564 + 24.46510819*m.x565 - 7.28623839*m.x566 - 23.57687014*m.x567
                          - 0.309838295393634*m.x568 <= 0)

m.c645 = Constraint(expr= - 0.309838295393634*m.x569 + 13.94696158*m.x570 + 24.46510819*m.x571 - 7.28623839*m.x572
                          - 23.57687014*m.x573 <= 0)

m.c646 = Constraint(expr=   24.46510819*m.x574 - 7.28623839*m.x575 - 23.57687014*m.x576 - 0.309838295393634*m.x577
                          + 13.94696158*m.x578 <= 0)

m.c647 = Constraint(expr=   13.94696158*m.x579 + 24.46510819*m.x580 - 7.28623839*m.x581 - 23.57687014*m.x582
                          - 0.309838295393634*m.x583 <= 0)

m.c648 = Constraint(expr= - 0.309838295393634*m.x584 + 13.94696158*m.x585 + 24.46510819*m.x586 - 7.28623839*m.x587
                          - 23.57687014*m.x588 <= 0)

m.c649 = Constraint(expr= - 0.309838295393634*m.x589 + 13.94696158*m.x590 + 24.46510819*m.x591 - 7.28623839*m.x592
                          - 23.57687014*m.x593 <= 0)

m.c650 = Constraint(expr= - 0.309838295393634*m.x594 + 13.94696158*m.x595 + 24.46510819*m.x596 - 7.28623839*m.x597
                          - 23.57687014*m.x598 <= 0)

m.c651 = Constraint(expr= - 0.309838295393634*m.x599 + 13.94696158*m.x600 + 24.46510819*m.x601 - 7.28623839*m.x602
                          - 23.57687014*m.x603 <= 0)

m.c652 = Constraint(expr= - 0.309838295393634*m.x604 + 13.94696158*m.x605 + 24.46510819*m.x606 - 7.28623839*m.x607
                          - 23.57687014*m.x608 <= 0)

m.c653 = Constraint(expr= - 0.309838295393634*m.x609 + 13.94696158*m.x610 + 24.46510819*m.x611 - 7.28623839*m.x612
                          - 23.57687014*m.x613 <= 0)

m.c654 = Constraint(expr= - 0.309838295393634*m.x614 + 13.94696158*m.x615 + 24.46510819*m.x616 - 7.28623839*m.x617
                          - 23.57687014*m.x618 <= 0)

m.c655 = Constraint(expr= - 0.309838295393634*m.x619 + 13.94696158*m.x620 + 24.46510819*m.x621 - 7.28623839*m.x622
                          - 23.57687014*m.x623 <= 0)

m.c656 = Constraint(expr= - 0.309838295393634*m.x624 + 13.94696158*m.x625 + 24.46510819*m.x626 - 7.28623839*m.x627
                          - 23.57687014*m.x628 <= 0)

m.c657 = Constraint(expr=   24.46510819*m.x629 - 7.28623839*m.x630 - 23.57687014*m.x631 - 0.309838295393634*m.x632
                          + 13.94696158*m.x633 <= 0)

m.c658 = Constraint(expr=   13.94696158*m.x634 + 24.46510819*m.x635 - 7.28623839*m.x636 - 23.57687014*m.x637
                          - 0.309838295393634*m.x638 <= 0)

m.c659 = Constraint(expr= - 0.309838295393634*m.x639 + 13.94696158*m.x640 + 24.46510819*m.x641 - 7.28623839*m.x642
                          - 23.57687014*m.x643 <= 0)

m.c660 = Constraint(expr= - 0.309838295393634*m.x644 + 29.29404529*m.x645 - 108.39408287*m.x646 + 442.21990639*m.x647
                          - 454.58448169*m.x648 <= 0)

m.c661 = Constraint(expr= - 0.309838295393634*m.x649 + 29.29404529*m.x650 - 108.39408287*m.x651 + 442.21990639*m.x652
                          - 454.58448169*m.x653 <= 0)

m.c662 = Constraint(expr= - 108.39408287*m.x654 + 442.21990639*m.x655 - 454.58448169*m.x656 - 0.309838295393634*m.x657
                          + 29.29404529*m.x658 <= 0)

m.c663 = Constraint(expr=   29.29404529*m.x659 - 108.39408287*m.x660 + 442.21990639*m.x661 - 454.58448169*m.x662
                          - 0.309838295393634*m.x663 <= 0)

m.c664 = Constraint(expr= - 0.309838295393634*m.x664 + 29.29404529*m.x665 - 108.39408287*m.x666 + 442.21990639*m.x667
                          - 454.58448169*m.x668 <= 0)

m.c665 = Constraint(expr= - 0.309838295393634*m.x669 + 29.29404529*m.x670 - 108.39408287*m.x671 + 442.21990639*m.x672
                          - 454.58448169*m.x673 <= 0)

m.c666 = Constraint(expr= - 0.309838295393634*m.x674 + 29.29404529*m.x675 - 108.39408287*m.x676 + 442.21990639*m.x677
                          - 454.58448169*m.x678 <= 0)

m.c667 = Constraint(expr= - 0.309838295393634*m.x679 + 29.29404529*m.x680 - 108.39408287*m.x681 + 442.21990639*m.x682
                          - 454.58448169*m.x683 <= 0)

m.c668 = Constraint(expr= - 454.58448169*m.x684 - 0.309838295393634*m.x685 + 29.29404529*m.x686 - 108.39408287*m.x687
                          + 442.21990639*m.x688 <= 0)

m.c669 = Constraint(expr=   29.29404529*m.x689 - 0.309838295393634*m.x690 - 108.39408287*m.x691 + 442.21990639*m.x692
                          - 454.58448169*m.x693 <= 0)

m.c670 = Constraint(expr= - 0.309838295393634*m.x694 + 29.29404529*m.x695 - 108.39408287*m.x696 + 442.21990639*m.x697
                          - 454.58448169*m.x698 <= 0)

m.c671 = Constraint(expr= - 0.309838295393634*m.x699 + 29.29404529*m.x700 - 108.39408287*m.x701 + 442.21990639*m.x702
                          - 454.58448169*m.x703 <= 0)

m.c672 = Constraint(expr= - 0.309838295393634*m.x704 + 25.92674585*m.x705 + 18.13482123*m.x706 + 22.12766012*m.x707
                          - 42.68950769*m.x708 <= 0)

m.c673 = Constraint(expr= - 0.309838295393634*m.x709 + 25.92674585*m.x710 + 18.13482123*m.x711 + 22.12766012*m.x712
                          - 42.68950769*m.x713 <= 0)

m.c674 = Constraint(expr= - 0.309838295393634*m.x714 + 25.92674585*m.x715 + 18.13482123*m.x716 + 22.12766012*m.x717
                          - 42.68950769*m.x718 <= 0)

m.c675 = Constraint(expr= - 0.309838295393634*m.x719 + 25.92674585*m.x720 + 18.13482123*m.x721 + 22.12766012*m.x722
                          - 42.68950769*m.x723 <= 0)

m.c676 = Constraint(expr= - 0.309838295393634*m.x724 + 25.92674585*m.x725 + 18.13482123*m.x726 + 22.12766012*m.x727
                          - 42.68950769*m.x728 <= 0)

m.c677 = Constraint(expr= - 0.309838295393634*m.x729 + 25.92674585*m.x730 + 18.13482123*m.x731 + 22.12766012*m.x732
                          - 42.68950769*m.x733 <= 0)

m.c678 = Constraint(expr= - 0.309838295393634*m.x734 + 25.92674585*m.x735 + 18.13482123*m.x736 + 22.12766012*m.x737
                          - 42.68950769*m.x738 <= 0)

m.c679 = Constraint(expr= - 0.309838295393634*m.x739 + 25.92674585*m.x740 + 18.13482123*m.x741 + 22.12766012*m.x742
                          - 42.68950769*m.x743 <= 0)

m.c680 = Constraint(expr= - 0.309838295393634*m.x744 + 25.92674585*m.x745 + 18.13482123*m.x746 + 22.12766012*m.x747
                          - 42.68950769*m.x748 <= 0)

m.c681 = Constraint(expr= - 0.309838295393634*m.x749 + 25.92674585*m.x750 + 18.13482123*m.x751 + 22.12766012*m.x752
                          - 42.68950769*m.x753 <= 0)

m.c682 = Constraint(expr= - 0.309838295393634*m.x754 + 25.92674585*m.x755 + 18.13482123*m.x756 + 22.12766012*m.x757
                          - 42.68950769*m.x758 <= 0)

m.c683 = Constraint(expr= - 0.309838295393634*m.x759 + 25.92674585*m.x760 + 18.13482123*m.x761 + 22.12766012*m.x762
                          - 42.68950769*m.x763 <= 0)

m.c684 = Constraint(expr= - 0.309838295393634*m.x764 + 17.4714791*m.x765 - 39.98407808*m.x766 + 134.55943082*m.x767
                          - 135.88441782*m.x768 <= 0)

m.c685 = Constraint(expr= - 0.309838295393634*m.x769 + 17.4714791*m.x770 - 39.98407808*m.x771 + 134.55943082*m.x772
                          - 135.88441782*m.x773 <= 0)

m.c686 = Constraint(expr= - 0.309838295393634*m.x774 + 17.4714791*m.x775 - 39.98407808*m.x776 + 134.55943082*m.x777
                          - 135.88441782*m.x778 <= 0)

m.c687 = Constraint(expr= - 0.309838295393634*m.x779 + 17.4714791*m.x780 - 39.98407808*m.x781 + 134.55943082*m.x782
                          - 135.88441782*m.x783 <= 0)

m.c688 = Constraint(expr= - 0.309838295393634*m.x784 + 17.4714791*m.x785 - 39.98407808*m.x786 + 134.55943082*m.x787
                          - 135.88441782*m.x788 <= 0)

m.c689 = Constraint(expr= - 0.309838295393634*m.x789 + 17.4714791*m.x790 - 39.98407808*m.x791 + 134.55943082*m.x792
                          - 135.88441782*m.x793 <= 0)

m.c690 = Constraint(expr= - 0.309838295393634*m.x794 + 17.4714791*m.x795 - 39.98407808*m.x796 + 134.55943082*m.x797
                          - 135.88441782*m.x798 <= 0)

m.c691 = Constraint(expr= - 0.309838295393634*m.x799 + 17.4714791*m.x800 - 39.98407808*m.x801 + 134.55943082*m.x802
                          - 135.88441782*m.x803 <= 0)

m.c692 = Constraint(expr= - 0.309838295393634*m.x804 + 17.4714791*m.x805 - 39.98407808*m.x806 + 134.55943082*m.x807
                          - 135.88441782*m.x808 <= 0)

m.c693 = Constraint(expr= - 0.309838295393634*m.x809 + 17.4714791*m.x810 - 39.98407808*m.x811 + 134.55943082*m.x812
                          - 135.88441782*m.x813 <= 0)

m.c694 = Constraint(expr= - 0.309838295393634*m.x814 + 17.4714791*m.x815 - 39.98407808*m.x816 + 134.55943082*m.x817
                          - 135.88441782*m.x818 <= 0)

m.c695 = Constraint(expr= - 0.309838295393634*m.x819 + 17.4714791*m.x820 - 39.98407808*m.x821 + 134.55943082*m.x822
                          - 135.88441782*m.x823 <= 0)

m.c696 = Constraint(expr=m.x194**2 - m.x824 == 0)

m.c697 = Constraint(expr=   m.x405 - 5*m.x824 == 0)

m.c698 = Constraint(expr=m.x196**2 - m.x825 == 0)

m.c699 = Constraint(expr=   m.x407 - 5*m.x825 == 0)

m.c700 = Constraint(expr=m.x198**2 - m.x826 == 0)

m.c701 = Constraint(expr=   m.x409 - 5*m.x826 == 0)

m.c702 = Constraint(expr=m.x200**2 - m.x827 == 0)

m.c703 = Constraint(expr=   m.x411 - 5*m.x827 == 0)

m.c704 = Constraint(expr=m.x202**2 - m.x828 == 0)

m.c705 = Constraint(expr=   m.x413 - 5*m.x828 == 0)

m.c706 = Constraint(expr=m.x204**2 - m.x829 == 0)

m.c707 = Constraint(expr=   m.x415 - 5*m.x829 == 0)

m.c708 = Constraint(expr=m.x206**2 - m.x830 == 0)

m.c709 = Constraint(expr=   m.x418 - 4*m.x830 == 0)

m.c710 = Constraint(expr=m.x208**2 - m.x831 == 0)

m.c711 = Constraint(expr=   m.x421 - 4*m.x831 == 0)

m.c712 = Constraint(expr=m.x210**2 - m.x832 == 0)

m.c713 = Constraint(expr=   m.x424 - 4*m.x832 == 0)

m.c714 = Constraint(expr=m.x212**2 - m.x833 == 0)

m.c715 = Constraint(expr=   m.x427 - 4*m.x833 == 0)

m.c716 = Constraint(expr=m.x214**2 - m.x834 == 0)

m.c717 = Constraint(expr=   m.x430 - 4*m.x834 == 0)

m.c718 = Constraint(expr=m.x216**2 - m.x835 == 0)

m.c719 = Constraint(expr=   m.x433 - 4*m.x835 == 0)

m.c720 = Constraint(expr=m.x224**2 - m.x836 == 0)

m.c721 = Constraint(expr=   m.x435 - 5*m.x836 == 0)

m.c722 = Constraint(expr=m.x226**2 - m.x837 == 0)

m.c723 = Constraint(expr=   m.x437 - 5*m.x837 == 0)

m.c724 = Constraint(expr=m.x228**2 - m.x838 == 0)

m.c725 = Constraint(expr=   m.x439 - 5*m.x838 == 0)

m.c726 = Constraint(expr=m.x230**2 - m.x839 == 0)

m.c727 = Constraint(expr=   m.x441 - 5*m.x839 == 0)

m.c728 = Constraint(expr=m.x232**2 - m.x840 == 0)

m.c729 = Constraint(expr=   m.x443 - 5*m.x840 == 0)

m.c730 = Constraint(expr=m.x234**2 - m.x841 == 0)

m.c731 = Constraint(expr=   m.x445 - 5*m.x841 == 0)

m.c732 = Constraint(expr=m.x278**2 - m.x842 == 0)

m.c733 = Constraint(expr=   m.x281 - m.x842 == 0)

m.c734 = Constraint(expr=m.x278**3 - m.x843 == 0)

m.c735 = Constraint(expr=   m.x558 - m.x843 == 0)

m.c736 = Constraint(expr=m.x280**2 - m.x844 == 0)

m.c737 = Constraint(expr=   m.x293 - m.x844 == 0)

m.c738 = Constraint(expr=m.x280**3 - m.x845 == 0)

m.c739 = Constraint(expr=   m.x560 - m.x845 == 0)

m.c740 = Constraint(expr=m.x282**2 - m.x846 == 0)

m.c741 = Constraint(expr=   m.x301 - m.x846 == 0)

m.c742 = Constraint(expr=m.x282**3 - m.x847 == 0)

m.c743 = Constraint(expr=   m.x567 - m.x847 == 0)

m.c744 = Constraint(expr=m.x284**2 - m.x848 == 0)

m.c745 = Constraint(expr=   m.x309 - m.x848 == 0)

m.c746 = Constraint(expr=m.x284**3 - m.x849 == 0)

m.c747 = Constraint(expr=   m.x573 - m.x849 == 0)

m.c748 = Constraint(expr=m.x286**2 - m.x850 == 0)

m.c749 = Constraint(expr=   m.x317 - m.x850 == 0)

m.c750 = Constraint(expr=m.x286**3 - m.x851 == 0)

m.c751 = Constraint(expr=   m.x576 - m.x851 == 0)

m.c752 = Constraint(expr=m.x288**2 - m.x852 == 0)

m.c753 = Constraint(expr=   m.x325 - m.x852 == 0)

m.c754 = Constraint(expr=m.x288**3 - m.x853 == 0)

m.c755 = Constraint(expr=   m.x582 - m.x853 == 0)

m.c756 = Constraint(expr=m.x290**2 - m.x854 == 0)

m.c757 = Constraint(expr=   m.x329 - m.x854 == 0)

m.c758 = Constraint(expr=m.x290**3 - m.x855 == 0)

m.c759 = Constraint(expr=   m.x588 - m.x855 == 0)

m.c760 = Constraint(expr=m.x292**2 - m.x856 == 0)

m.c761 = Constraint(expr=   m.x335 - m.x856 == 0)

m.c762 = Constraint(expr=m.x292**3 - m.x857 == 0)

m.c763 = Constraint(expr=   m.x593 - m.x857 == 0)

m.c764 = Constraint(expr=m.x294**2 - m.x858 == 0)

m.c765 = Constraint(expr=   m.x343 - m.x858 == 0)

m.c766 = Constraint(expr=m.x294**3 - m.x859 == 0)

m.c767 = Constraint(expr=   m.x598 - m.x859 == 0)

m.c768 = Constraint(expr=m.x296**2 - m.x860 == 0)

m.c769 = Constraint(expr=   m.x349 - m.x860 == 0)

m.c770 = Constraint(expr=m.x296**3 - m.x861 == 0)

m.c771 = Constraint(expr=   m.x603 - m.x861 == 0)

m.c772 = Constraint(expr=m.x298**2 - m.x862 == 0)

m.c773 = Constraint(expr=   m.x355 - m.x862 == 0)

m.c774 = Constraint(expr=m.x298**3 - m.x863 == 0)

m.c775 = Constraint(expr=   m.x608 - m.x863 == 0)

m.c776 = Constraint(expr=m.x300**2 - m.x864 == 0)

m.c777 = Constraint(expr=   m.x359 - m.x864 == 0)

m.c778 = Constraint(expr=m.x300**3 - m.x865 == 0)

m.c779 = Constraint(expr=   m.x613 - m.x865 == 0)

m.c780 = Constraint(expr=m.x302**2 - m.x866 == 0)

m.c781 = Constraint(expr=   m.x367 - m.x866 == 0)

m.c782 = Constraint(expr=m.x302**3 - m.x867 == 0)

m.c783 = Constraint(expr=   m.x618 - m.x867 == 0)

m.c784 = Constraint(expr=m.x304**2 - m.x868 == 0)

m.c785 = Constraint(expr=   m.x373 - m.x868 == 0)

m.c786 = Constraint(expr=m.x304**3 - m.x869 == 0)

m.c787 = Constraint(expr=   m.x623 - m.x869 == 0)

m.c788 = Constraint(expr=m.x306**2 - m.x870 == 0)

m.c789 = Constraint(expr=   m.x379 - m.x870 == 0)

m.c790 = Constraint(expr=m.x306**3 - m.x871 == 0)

m.c791 = Constraint(expr=   m.x628 - m.x871 == 0)

m.c792 = Constraint(expr=m.x308**2 - m.x872 == 0)

m.c793 = Constraint(expr=   m.x385 - m.x872 == 0)

m.c794 = Constraint(expr=m.x308**3 - m.x873 == 0)

m.c795 = Constraint(expr=   m.x631 - m.x873 == 0)

m.c796 = Constraint(expr=m.x310**2 - m.x874 == 0)

m.c797 = Constraint(expr=   m.x58 - m.x874 == 0)

m.c798 = Constraint(expr=m.x310**3 - m.x875 == 0)

m.c799 = Constraint(expr=   m.x637 - m.x875 == 0)

m.c800 = Constraint(expr=m.x312**2 - m.x876 == 0)

m.c801 = Constraint(expr=   m.x61 - m.x876 == 0)

m.c802 = Constraint(expr=m.x312**3 - m.x877 == 0)

m.c803 = Constraint(expr=   m.x643 - m.x877 == 0)

m.c804 = Constraint(expr=m.x314**2 - m.x878 == 0)

m.c805 = Constraint(expr=   m.x65 - m.x878 == 0)

m.c806 = Constraint(expr=m.x314**3 - m.x879 == 0)

m.c807 = Constraint(expr=   m.x648 - m.x879 == 0)

m.c808 = Constraint(expr=m.x316**2 - m.x880 == 0)

m.c809 = Constraint(expr=   m.x69 - m.x880 == 0)

m.c810 = Constraint(expr=m.x316**3 - m.x881 == 0)

m.c811 = Constraint(expr=   m.x653 - m.x881 == 0)

m.c812 = Constraint(expr=m.x318**2 - m.x882 == 0)

m.c813 = Constraint(expr=   m.x71 - m.x882 == 0)

m.c814 = Constraint(expr=m.x318**3 - m.x883 == 0)

m.c815 = Constraint(expr=   m.x656 - m.x883 == 0)

m.c816 = Constraint(expr=m.x320**2 - m.x884 == 0)

m.c817 = Constraint(expr=   m.x75 - m.x884 == 0)

m.c818 = Constraint(expr=m.x320**3 - m.x885 == 0)

m.c819 = Constraint(expr=   m.x662 - m.x885 == 0)

m.c820 = Constraint(expr=m.x322**2 - m.x886 == 0)

m.c821 = Constraint(expr=   m.x79 - m.x886 == 0)

m.c822 = Constraint(expr=m.x322**3 - m.x887 == 0)

m.c823 = Constraint(expr=   m.x668 - m.x887 == 0)

m.c824 = Constraint(expr=m.x324**2 - m.x888 == 0)

m.c825 = Constraint(expr=   m.x85 - m.x888 == 0)

m.c826 = Constraint(expr=m.x324**3 - m.x889 == 0)

m.c827 = Constraint(expr=   m.x673 - m.x889 == 0)

m.c828 = Constraint(expr=m.x326**2 - m.x890 == 0)

m.c829 = Constraint(expr=   m.x88 - m.x890 == 0)

m.c830 = Constraint(expr=m.x326**3 - m.x891 == 0)

m.c831 = Constraint(expr=   m.x678 - m.x891 == 0)

m.c832 = Constraint(expr=m.x328**2 - m.x892 == 0)

m.c833 = Constraint(expr=   m.x90 - m.x892 == 0)

m.c834 = Constraint(expr=m.x328**3 - m.x893 == 0)

m.c835 = Constraint(expr=   m.x683 - m.x893 == 0)

m.c836 = Constraint(expr=m.x330**2 - m.x894 == 0)

m.c837 = Constraint(expr=   m.x94 - m.x894 == 0)

m.c838 = Constraint(expr=m.x330**3 - m.x895 == 0)

m.c839 = Constraint(expr=   m.x684 - m.x895 == 0)

m.c840 = Constraint(expr=m.x332**2 - m.x896 == 0)

m.c841 = Constraint(expr=   m.x96 - m.x896 == 0)

m.c842 = Constraint(expr=m.x332**3 - m.x897 == 0)

m.c843 = Constraint(expr=   m.x693 - m.x897 == 0)

m.c844 = Constraint(expr=m.x334**2 - m.x898 == 0)

m.c845 = Constraint(expr=   m.x100 - m.x898 == 0)

m.c846 = Constraint(expr=m.x334**3 - m.x899 == 0)

m.c847 = Constraint(expr=   m.x698 - m.x899 == 0)

m.c848 = Constraint(expr=m.x336**2 - m.x900 == 0)

m.c849 = Constraint(expr=   m.x103 - m.x900 == 0)

m.c850 = Constraint(expr=m.x336**3 - m.x901 == 0)

m.c851 = Constraint(expr=   m.x703 - m.x901 == 0)

m.c852 = Constraint(expr=m.x338**2 - m.x902 == 0)

m.c853 = Constraint(expr=   m.x105 - m.x902 == 0)

m.c854 = Constraint(expr=m.x338**3 - m.x903 == 0)

m.c855 = Constraint(expr=   m.x708 - m.x903 == 0)

m.c856 = Constraint(expr=m.x340**2 - m.x904 == 0)

m.c857 = Constraint(expr=   m.x109 - m.x904 == 0)

m.c858 = Constraint(expr=m.x340**3 - m.x905 == 0)

m.c859 = Constraint(expr=   m.x713 - m.x905 == 0)

m.c860 = Constraint(expr=m.x342**2 - m.x906 == 0)

m.c861 = Constraint(expr=   m.x115 - m.x906 == 0)

m.c862 = Constraint(expr=m.x342**3 - m.x907 == 0)

m.c863 = Constraint(expr=   m.x718 - m.x907 == 0)

m.c864 = Constraint(expr=m.x344**2 - m.x908 == 0)

m.c865 = Constraint(expr=   m.x118 - m.x908 == 0)

m.c866 = Constraint(expr=m.x344**3 - m.x909 == 0)

m.c867 = Constraint(expr=   m.x723 - m.x909 == 0)

m.c868 = Constraint(expr=m.x346**2 - m.x910 == 0)

m.c869 = Constraint(expr=   m.x122 - m.x910 == 0)

m.c870 = Constraint(expr=m.x346**3 - m.x911 == 0)

m.c871 = Constraint(expr=   m.x728 - m.x911 == 0)

m.c872 = Constraint(expr=m.x348**2 - m.x912 == 0)

m.c873 = Constraint(expr=   m.x127 - m.x912 == 0)

m.c874 = Constraint(expr=m.x348**3 - m.x913 == 0)

m.c875 = Constraint(expr=   m.x733 - m.x913 == 0)

m.c876 = Constraint(expr=m.x350**2 - m.x914 == 0)

m.c877 = Constraint(expr=   m.x129 - m.x914 == 0)

m.c878 = Constraint(expr=m.x350**3 - m.x915 == 0)

m.c879 = Constraint(expr=   m.x738 - m.x915 == 0)

m.c880 = Constraint(expr=m.x352**2 - m.x916 == 0)

m.c881 = Constraint(expr=   m.x133 - m.x916 == 0)

m.c882 = Constraint(expr=m.x352**3 - m.x917 == 0)

m.c883 = Constraint(expr=   m.x743 - m.x917 == 0)

m.c884 = Constraint(expr=m.x354**2 - m.x918 == 0)

m.c885 = Constraint(expr=   m.x136 - m.x918 == 0)

m.c886 = Constraint(expr=m.x354**3 - m.x919 == 0)

m.c887 = Constraint(expr=   m.x748 - m.x919 == 0)

m.c888 = Constraint(expr=m.x356**2 - m.x920 == 0)

m.c889 = Constraint(expr=   m.x139 - m.x920 == 0)

m.c890 = Constraint(expr=m.x356**3 - m.x921 == 0)

m.c891 = Constraint(expr=   m.x753 - m.x921 == 0)

m.c892 = Constraint(expr=m.x358**2 - m.x922 == 0)

m.c893 = Constraint(expr=   m.x141 - m.x922 == 0)

m.c894 = Constraint(expr=m.x358**3 - m.x923 == 0)

m.c895 = Constraint(expr=   m.x758 - m.x923 == 0)

m.c896 = Constraint(expr=m.x360**2 - m.x924 == 0)

m.c897 = Constraint(expr=   m.x144 - m.x924 == 0)

m.c898 = Constraint(expr=m.x360**3 - m.x925 == 0)

m.c899 = Constraint(expr=   m.x763 - m.x925 == 0)

m.c900 = Constraint(expr=m.x362**2 - m.x926 == 0)

m.c901 = Constraint(expr=   m.x149 - m.x926 == 0)

m.c902 = Constraint(expr=m.x362**3 - m.x927 == 0)

m.c903 = Constraint(expr=   m.x768 - m.x927 == 0)

m.c904 = Constraint(expr=m.x364**2 - m.x928 == 0)

m.c905 = Constraint(expr=   m.x152 - m.x928 == 0)

m.c906 = Constraint(expr=m.x364**3 - m.x929 == 0)

m.c907 = Constraint(expr=   m.x773 - m.x929 == 0)

m.c908 = Constraint(expr=m.x366**2 - m.x930 == 0)

m.c909 = Constraint(expr=   m.x156 - m.x930 == 0)

m.c910 = Constraint(expr=m.x366**3 - m.x931 == 0)

m.c911 = Constraint(expr=   m.x778 - m.x931 == 0)

m.c912 = Constraint(expr=m.x368**2 - m.x932 == 0)

m.c913 = Constraint(expr=   m.x159 - m.x932 == 0)

m.c914 = Constraint(expr=m.x368**3 - m.x933 == 0)

m.c915 = Constraint(expr=   m.x783 - m.x933 == 0)

m.c916 = Constraint(expr=m.x370**2 - m.x934 == 0)

m.c917 = Constraint(expr=   m.x163 - m.x934 == 0)

m.c918 = Constraint(expr=m.x370**3 - m.x935 == 0)

m.c919 = Constraint(expr=   m.x788 - m.x935 == 0)

m.c920 = Constraint(expr=m.x372**2 - m.x936 == 0)

m.c921 = Constraint(expr=   m.x167 - m.x936 == 0)

m.c922 = Constraint(expr=m.x372**3 - m.x937 == 0)

m.c923 = Constraint(expr=   m.x793 - m.x937 == 0)

m.c924 = Constraint(expr=m.x374**2 - m.x938 == 0)

m.c925 = Constraint(expr=   m.x172 - m.x938 == 0)

m.c926 = Constraint(expr=m.x374**3 - m.x939 == 0)

m.c927 = Constraint(expr=   m.x798 - m.x939 == 0)

m.c928 = Constraint(expr=m.x376**2 - m.x940 == 0)

m.c929 = Constraint(expr=   m.x174 - m.x940 == 0)

m.c930 = Constraint(expr=m.x376**3 - m.x941 == 0)

m.c931 = Constraint(expr=   m.x803 - m.x941 == 0)

m.c932 = Constraint(expr=m.x378**2 - m.x942 == 0)

m.c933 = Constraint(expr=   m.x177 - m.x942 == 0)

m.c934 = Constraint(expr=m.x378**3 - m.x943 == 0)

m.c935 = Constraint(expr=   m.x808 - m.x943 == 0)

m.c936 = Constraint(expr=m.x380**2 - m.x944 == 0)

m.c937 = Constraint(expr=   m.x181 - m.x944 == 0)

m.c938 = Constraint(expr=m.x380**3 - m.x945 == 0)

m.c939 = Constraint(expr=   m.x813 - m.x945 == 0)

m.c940 = Constraint(expr=m.x382**2 - m.x946 == 0)

m.c941 = Constraint(expr=   m.x183 - m.x946 == 0)

m.c942 = Constraint(expr=m.x382**3 - m.x947 == 0)

m.c943 = Constraint(expr=   m.x818 - m.x947 == 0)

m.c944 = Constraint(expr=m.x384**2 - m.x948 == 0)

m.c945 = Constraint(expr=   m.x186 - m.x948 == 0)

m.c946 = Constraint(expr=m.x384**3 - m.x949 == 0)

m.c947 = Constraint(expr=   m.x823 - m.x949 == 0)

m.c948 = Constraint(expr=m.x278*m.x524 - m.x283 == 0)

m.c949 = Constraint(expr=m.x524*m.x842 - m.x557 == 0)

m.c950 = Constraint(expr=m.x290*m.x524 - m.x331 == 0)

m.c951 = Constraint(expr=m.x524*m.x854 - m.x587 == 0)

m.c952 = Constraint(expr=m.x302*m.x524 - m.x365 == 0)

m.c953 = Constraint(expr=m.x524*m.x866 - m.x617 == 0)

m.c954 = Constraint(expr=m.x524**2 - m.x950 == 0)

m.c955 = Constraint(expr=   m.x285 - m.x950 == 0)

m.c956 = Constraint(expr=m.x278*m.x950 - m.x556 == 0)

m.c957 = Constraint(expr=m.x290*m.x950 - m.x586 == 0)

m.c958 = Constraint(expr=m.x302*m.x950 - m.x616 == 0)

m.c959 = Constraint(expr=m.x524**3 - m.x951 == 0)

m.c960 = Constraint(expr=m.b2*m.x951 - m.x555 == 0)

m.c961 = Constraint(expr=m.b8*m.x951 - m.x585 == 0)

m.c962 = Constraint(expr=m.b14*m.x951 - m.x615 == 0)

m.c963 = Constraint(expr=m.x280*m.x525 - m.x291 == 0)

m.c964 = Constraint(expr=m.x525*m.x844 - m.x559 == 0)

m.c965 = Constraint(expr=m.x292*m.x525 - m.x337 == 0)

m.c966 = Constraint(expr=m.x525*m.x856 - m.x592 == 0)

m.c967 = Constraint(expr=m.x304*m.x525 - m.x371 == 0)

m.c968 = Constraint(expr=m.x525*m.x868 - m.x622 == 0)

m.c969 = Constraint(expr=m.x525**2 - m.x952 == 0)

m.c970 = Constraint(expr=   m.x289 - m.x952 == 0)

m.c971 = Constraint(expr=m.x280*m.x952 - m.x563 == 0)

m.c972 = Constraint(expr=m.x292*m.x952 - m.x591 == 0)

m.c973 = Constraint(expr=m.x304*m.x952 - m.x621 == 0)

m.c974 = Constraint(expr=m.x525**3 - m.x953 == 0)

m.c975 = Constraint(expr=m.b3*m.x953 - m.x562 == 0)

m.c976 = Constraint(expr=m.b9*m.x953 - m.x590 == 0)

m.c977 = Constraint(expr=m.b15*m.x953 - m.x620 == 0)

m.c978 = Constraint(expr=m.x282*m.x526 - m.x299 == 0)

m.c979 = Constraint(expr=m.x526*m.x846 - m.x566 == 0)

m.c980 = Constraint(expr=m.x294*m.x526 - m.x341 == 0)

m.c981 = Constraint(expr=m.x526*m.x858 - m.x597 == 0)

m.c982 = Constraint(expr=m.x306*m.x526 - m.x377 == 0)

m.c983 = Constraint(expr=m.x526*m.x870 - m.x627 == 0)

m.c984 = Constraint(expr=m.x526**2 - m.x954 == 0)

m.c985 = Constraint(expr=   m.x297 - m.x954 == 0)

m.c986 = Constraint(expr=m.x282*m.x954 - m.x565 == 0)

m.c987 = Constraint(expr=m.x294*m.x954 - m.x596 == 0)

m.c988 = Constraint(expr=m.x306*m.x954 - m.x626 == 0)

m.c989 = Constraint(expr=m.x526**3 - m.x955 == 0)

m.c990 = Constraint(expr=m.b4*m.x955 - m.x564 == 0)

m.c991 = Constraint(expr=m.b10*m.x955 - m.x595 == 0)

m.c992 = Constraint(expr=m.b16*m.x955 - m.x625 == 0)

m.c993 = Constraint(expr=m.x284*m.x527 - m.x307 == 0)

m.c994 = Constraint(expr=m.x527*m.x848 - m.x572 == 0)

m.c995 = Constraint(expr=m.x296*m.x527 - m.x347 == 0)

m.c996 = Constraint(expr=m.x527*m.x860 - m.x602 == 0)

m.c997 = Constraint(expr=m.x308*m.x527 - m.x383 == 0)

m.c998 = Constraint(expr=m.x527*m.x872 - m.x630 == 0)

m.c999 = Constraint(expr=m.x527**2 - m.x956 == 0)

m.c1000 = Constraint(expr=   m.x305 - m.x956 == 0)

m.c1001 = Constraint(expr=m.x284*m.x956 - m.x571 == 0)

m.c1002 = Constraint(expr=m.x296*m.x956 - m.x601 == 0)

m.c1003 = Constraint(expr=m.x308*m.x956 - m.x629 == 0)

m.c1004 = Constraint(expr=m.x527**3 - m.x957 == 0)

m.c1005 = Constraint(expr=m.b5*m.x957 - m.x570 == 0)

m.c1006 = Constraint(expr=m.b11*m.x957 - m.x600 == 0)

m.c1007 = Constraint(expr=m.b17*m.x957 - m.x633 == 0)

m.c1008 = Constraint(expr=m.x286*m.x528 - m.x315 == 0)

m.c1009 = Constraint(expr=m.x528*m.x850 - m.x575 == 0)

m.c1010 = Constraint(expr=m.x298*m.x528 - m.x353 == 0)

m.c1011 = Constraint(expr=m.x528*m.x862 - m.x607 == 0)

m.c1012 = Constraint(expr=m.x310*m.x528 - m.x57 == 0)

m.c1013 = Constraint(expr=m.x528*m.x874 - m.x636 == 0)

m.c1014 = Constraint(expr=m.x528**2 - m.x958 == 0)

m.c1015 = Constraint(expr=   m.x313 - m.x958 == 0)

m.c1016 = Constraint(expr=m.x286*m.x958 - m.x574 == 0)

m.c1017 = Constraint(expr=m.x298*m.x958 - m.x606 == 0)

m.c1018 = Constraint(expr=m.x310*m.x958 - m.x635 == 0)

m.c1019 = Constraint(expr=m.x528**3 - m.x959 == 0)

m.c1020 = Constraint(expr=m.b6*m.x959 - m.x578 == 0)

m.c1021 = Constraint(expr=m.b12*m.x959 - m.x605 == 0)

m.c1022 = Constraint(expr=m.b18*m.x959 - m.x634 == 0)

m.c1023 = Constraint(expr=m.x288*m.x529 - m.x323 == 0)

m.c1024 = Constraint(expr=m.x529*m.x852 - m.x581 == 0)

m.c1025 = Constraint(expr=m.x300*m.x529 - m.x361 == 0)

m.c1026 = Constraint(expr=m.x529*m.x864 - m.x612 == 0)

m.c1027 = Constraint(expr=m.x312*m.x529 - m.x60 == 0)

m.c1028 = Constraint(expr=m.x529*m.x876 - m.x642 == 0)

m.c1029 = Constraint(expr=m.x529**2 - m.x960 == 0)

m.c1030 = Constraint(expr=   m.x321 - m.x960 == 0)

m.c1031 = Constraint(expr=m.x288*m.x960 - m.x580 == 0)

m.c1032 = Constraint(expr=m.x300*m.x960 - m.x611 == 0)

m.c1033 = Constraint(expr=m.x312*m.x960 - m.x641 == 0)

m.c1034 = Constraint(expr=m.x529**3 - m.x961 == 0)

m.c1035 = Constraint(expr=m.b7*m.x961 - m.x579 == 0)

m.c1036 = Constraint(expr=m.b13*m.x961 - m.x610 == 0)

m.c1037 = Constraint(expr=m.b19*m.x961 - m.x640 == 0)

m.c1038 = Constraint(expr=m.x314*m.x530 - m.x64 == 0)

m.c1039 = Constraint(expr=m.x530*m.x878 - m.x647 == 0)

m.c1040 = Constraint(expr=m.x326*m.x530 - m.x87 == 0)

m.c1041 = Constraint(expr=m.x530*m.x890 - m.x677 == 0)

m.c1042 = Constraint(expr=m.x530**2 - m.x962 == 0)

m.c1043 = Constraint(expr=   m.x63 - m.x962 == 0)

m.c1044 = Constraint(expr=m.x314*m.x962 - m.x646 == 0)

m.c1045 = Constraint(expr=m.x326*m.x962 - m.x676 == 0)

m.c1046 = Constraint(expr=m.x530**3 - m.x963 == 0)

m.c1047 = Constraint(expr=m.b20*m.x963 - m.x645 == 0)

m.c1048 = Constraint(expr=m.b26*m.x963 - m.x675 == 0)

m.c1049 = Constraint(expr=m.x316*m.x531 - m.x67 == 0)

m.c1050 = Constraint(expr=m.x531*m.x880 - m.x652 == 0)

m.c1051 = Constraint(expr=m.x328*m.x531 - m.x91 == 0)

m.c1052 = Constraint(expr=m.x531*m.x892 - m.x682 == 0)

m.c1053 = Constraint(expr=m.x531**2 - m.x964 == 0)

m.c1054 = Constraint(expr=   m.x68 - m.x964 == 0)

m.c1055 = Constraint(expr=m.x316*m.x964 - m.x651 == 0)

m.c1056 = Constraint(expr=m.x328*m.x964 - m.x681 == 0)

m.c1057 = Constraint(expr=m.x531**3 - m.x965 == 0)

m.c1058 = Constraint(expr=m.b21*m.x965 - m.x650 == 0)

m.c1059 = Constraint(expr=m.b27*m.x965 - m.x680 == 0)

m.c1060 = Constraint(expr=m.x318*m.x532 - m.x72 == 0)

m.c1061 = Constraint(expr=m.x532*m.x882 - m.x655 == 0)

m.c1062 = Constraint(expr=m.x330*m.x532 - m.x93 == 0)

m.c1063 = Constraint(expr=m.x532*m.x894 - m.x688 == 0)

m.c1064 = Constraint(expr=m.x532**2 - m.x966 == 0)

m.c1065 = Constraint(expr=   m.x73 - m.x966 == 0)

m.c1066 = Constraint(expr=m.x318*m.x966 - m.x654 == 0)

m.c1067 = Constraint(expr=m.x330*m.x966 - m.x687 == 0)

m.c1068 = Constraint(expr=m.x532**3 - m.x967 == 0)

m.c1069 = Constraint(expr=m.b22*m.x967 - m.x658 == 0)

m.c1070 = Constraint(expr=m.b28*m.x967 - m.x686 == 0)

m.c1071 = Constraint(expr=m.x320*m.x533 - m.x76 == 0)

m.c1072 = Constraint(expr=m.x533*m.x884 - m.x661 == 0)

m.c1073 = Constraint(expr=m.x332*m.x533 - m.x97 == 0)

m.c1074 = Constraint(expr=m.x533*m.x896 - m.x692 == 0)

m.c1075 = Constraint(expr=m.x533**2 - m.x968 == 0)

m.c1076 = Constraint(expr=   m.x77 - m.x968 == 0)

m.c1077 = Constraint(expr=m.x320*m.x968 - m.x660 == 0)

m.c1078 = Constraint(expr=m.x332*m.x968 - m.x691 == 0)

m.c1079 = Constraint(expr=m.x533**3 - m.x969 == 0)

m.c1080 = Constraint(expr=m.b23*m.x969 - m.x659 == 0)

m.c1081 = Constraint(expr=m.b29*m.x969 - m.x689 == 0)

m.c1082 = Constraint(expr=m.x322*m.x534 - m.x80 == 0)

m.c1083 = Constraint(expr=m.x534*m.x886 - m.x667 == 0)

m.c1084 = Constraint(expr=m.x334*m.x534 - m.x99 == 0)

m.c1085 = Constraint(expr=m.x534*m.x898 - m.x697 == 0)

m.c1086 = Constraint(expr=m.x534**2 - m.x970 == 0)

m.c1087 = Constraint(expr=   m.x81 - m.x970 == 0)

m.c1088 = Constraint(expr=m.x322*m.x970 - m.x666 == 0)

m.c1089 = Constraint(expr=m.x334*m.x970 - m.x696 == 0)

m.c1090 = Constraint(expr=m.x534**3 - m.x971 == 0)

m.c1091 = Constraint(expr=m.b24*m.x971 - m.x665 == 0)

m.c1092 = Constraint(expr=m.b30*m.x971 - m.x695 == 0)

m.c1093 = Constraint(expr=m.x324*m.x535 - m.x83 == 0)

m.c1094 = Constraint(expr=m.x535*m.x888 - m.x672 == 0)

m.c1095 = Constraint(expr=m.x336*m.x535 - m.x102 == 0)

m.c1096 = Constraint(expr=m.x535*m.x900 - m.x702 == 0)

m.c1097 = Constraint(expr=m.x535**2 - m.x972 == 0)

m.c1098 = Constraint(expr=   m.x84 - m.x972 == 0)

m.c1099 = Constraint(expr=m.x324*m.x972 - m.x671 == 0)

m.c1100 = Constraint(expr=m.x336*m.x972 - m.x701 == 0)

m.c1101 = Constraint(expr=m.x535**3 - m.x973 == 0)

m.c1102 = Constraint(expr=m.b25*m.x973 - m.x670 == 0)

m.c1103 = Constraint(expr=m.b31*m.x973 - m.x700 == 0)

m.c1104 = Constraint(expr=m.x338*m.x536 - m.x107 == 0)

m.c1105 = Constraint(expr=m.x536*m.x902 - m.x707 == 0)

m.c1106 = Constraint(expr=m.x350*m.x536 - m.x130 == 0)

m.c1107 = Constraint(expr=m.x536*m.x914 - m.x737 == 0)

m.c1108 = Constraint(expr=m.x536**2 - m.x974 == 0)

m.c1109 = Constraint(expr=   m.x106 - m.x974 == 0)

m.c1110 = Constraint(expr=m.x338*m.x974 - m.x706 == 0)

m.c1111 = Constraint(expr=m.x350*m.x974 - m.x736 == 0)

m.c1112 = Constraint(expr=m.x536**3 - m.x975 == 0)

m.c1113 = Constraint(expr=m.b32*m.x975 - m.x705 == 0)

m.c1114 = Constraint(expr=m.b38*m.x975 - m.x735 == 0)

m.c1115 = Constraint(expr=m.x340*m.x537 - m.x111 == 0)

m.c1116 = Constraint(expr=m.x537*m.x904 - m.x712 == 0)

m.c1117 = Constraint(expr=m.x352*m.x537 - m.x132 == 0)

m.c1118 = Constraint(expr=m.x537*m.x916 - m.x742 == 0)

m.c1119 = Constraint(expr=m.x537**2 - m.x976 == 0)

m.c1120 = Constraint(expr=   m.x110 - m.x976 == 0)

m.c1121 = Constraint(expr=m.x340*m.x976 - m.x711 == 0)

m.c1122 = Constraint(expr=m.x352*m.x976 - m.x741 == 0)

m.c1123 = Constraint(expr=m.x537**3 - m.x977 == 0)

m.c1124 = Constraint(expr=m.b33*m.x977 - m.x710 == 0)

m.c1125 = Constraint(expr=m.b39*m.x977 - m.x740 == 0)

m.c1126 = Constraint(expr=m.x342*m.x538 - m.x113 == 0)

m.c1127 = Constraint(expr=m.x538*m.x906 - m.x717 == 0)

m.c1128 = Constraint(expr=m.x354*m.x538 - m.x135 == 0)

m.c1129 = Constraint(expr=m.x538*m.x918 - m.x747 == 0)

m.c1130 = Constraint(expr=m.x538**2 - m.x978 == 0)

m.c1131 = Constraint(expr=   m.x114 - m.x978 == 0)

m.c1132 = Constraint(expr=m.x342*m.x978 - m.x716 == 0)

m.c1133 = Constraint(expr=m.x354*m.x978 - m.x746 == 0)

m.c1134 = Constraint(expr=m.x538**3 - m.x979 == 0)

m.c1135 = Constraint(expr=m.b34*m.x979 - m.x715 == 0)

m.c1136 = Constraint(expr=m.b40*m.x979 - m.x745 == 0)

m.c1137 = Constraint(expr=m.x344*m.x539 - m.x119 == 0)

m.c1138 = Constraint(expr=m.x539*m.x908 - m.x722 == 0)

m.c1139 = Constraint(expr=m.x356*m.x539 - m.x138 == 0)

m.c1140 = Constraint(expr=m.x539*m.x920 - m.x752 == 0)

m.c1141 = Constraint(expr=m.x539**2 - m.x980 == 0)

m.c1142 = Constraint(expr=   m.x117 - m.x980 == 0)

m.c1143 = Constraint(expr=m.x344*m.x980 - m.x721 == 0)

m.c1144 = Constraint(expr=m.x356*m.x980 - m.x751 == 0)

m.c1145 = Constraint(expr=m.x539**3 - m.x981 == 0)

m.c1146 = Constraint(expr=m.b35*m.x981 - m.x720 == 0)

m.c1147 = Constraint(expr=m.b41*m.x981 - m.x750 == 0)

m.c1148 = Constraint(expr=m.x346*m.x540 - m.x123 == 0)

m.c1149 = Constraint(expr=m.x540*m.x910 - m.x727 == 0)

m.c1150 = Constraint(expr=m.x358*m.x540 - m.x142 == 0)

m.c1151 = Constraint(expr=m.x540*m.x922 - m.x757 == 0)

m.c1152 = Constraint(expr=m.x540**2 - m.x982 == 0)

m.c1153 = Constraint(expr=   m.x121 - m.x982 == 0)

m.c1154 = Constraint(expr=m.x346*m.x982 - m.x726 == 0)

m.c1155 = Constraint(expr=m.x358*m.x982 - m.x756 == 0)

m.c1156 = Constraint(expr=m.x540**3 - m.x983 == 0)

m.c1157 = Constraint(expr=m.b36*m.x983 - m.x725 == 0)

m.c1158 = Constraint(expr=m.b42*m.x983 - m.x755 == 0)

m.c1159 = Constraint(expr=m.x348*m.x541 - m.x125 == 0)

m.c1160 = Constraint(expr=m.x541*m.x912 - m.x732 == 0)

m.c1161 = Constraint(expr=m.x360*m.x541 - m.x145 == 0)

m.c1162 = Constraint(expr=m.x541*m.x924 - m.x762 == 0)

m.c1163 = Constraint(expr=m.x541**2 - m.x984 == 0)

m.c1164 = Constraint(expr=   m.x126 - m.x984 == 0)

m.c1165 = Constraint(expr=m.x348*m.x984 - m.x731 == 0)

m.c1166 = Constraint(expr=m.x360*m.x984 - m.x761 == 0)

m.c1167 = Constraint(expr=m.x541**3 - m.x985 == 0)

m.c1168 = Constraint(expr=m.b37*m.x985 - m.x730 == 0)

m.c1169 = Constraint(expr=m.b43*m.x985 - m.x760 == 0)

m.c1170 = Constraint(expr=m.x362*m.x542 - m.x147 == 0)

m.c1171 = Constraint(expr=m.x542*m.x926 - m.x767 == 0)

m.c1172 = Constraint(expr=m.x374*m.x542 - m.x171 == 0)

m.c1173 = Constraint(expr=m.x542*m.x938 - m.x797 == 0)

m.c1174 = Constraint(expr=m.x542**2 - m.x986 == 0)

m.c1175 = Constraint(expr=   m.x148 - m.x986 == 0)

m.c1176 = Constraint(expr=m.x362*m.x986 - m.x766 == 0)

m.c1177 = Constraint(expr=m.x374*m.x986 - m.x796 == 0)

m.c1178 = Constraint(expr=m.x542**3 - m.x987 == 0)

m.c1179 = Constraint(expr=m.b44*m.x987 - m.x765 == 0)

m.c1180 = Constraint(expr=m.b50*m.x987 - m.x795 == 0)

m.c1181 = Constraint(expr=m.x364*m.x543 - m.x153 == 0)

m.c1182 = Constraint(expr=m.x543*m.x928 - m.x772 == 0)

m.c1183 = Constraint(expr=m.x376*m.x543 - m.x175 == 0)

m.c1184 = Constraint(expr=m.x543*m.x940 - m.x802 == 0)

m.c1185 = Constraint(expr=m.x543**2 - m.x988 == 0)

m.c1186 = Constraint(expr=   m.x151 - m.x988 == 0)

m.c1187 = Constraint(expr=m.x364*m.x988 - m.x771 == 0)

m.c1188 = Constraint(expr=m.x376*m.x988 - m.x801 == 0)

m.c1189 = Constraint(expr=m.x543**3 - m.x989 == 0)

m.c1190 = Constraint(expr=m.b45*m.x989 - m.x770 == 0)

m.c1191 = Constraint(expr=m.b51*m.x989 - m.x800 == 0)

m.c1192 = Constraint(expr=m.x366*m.x544 - m.x155 == 0)

m.c1193 = Constraint(expr=m.x544*m.x930 - m.x777 == 0)

m.c1194 = Constraint(expr=m.x378*m.x544 - m.x178 == 0)

m.c1195 = Constraint(expr=m.x544*m.x942 - m.x807 == 0)

m.c1196 = Constraint(expr=m.x544**2 - m.x990 == 0)

m.c1197 = Constraint(expr=   m.x157 - m.x990 == 0)

m.c1198 = Constraint(expr=m.x366*m.x990 - m.x776 == 0)

m.c1199 = Constraint(expr=m.x378*m.x990 - m.x806 == 0)

m.c1200 = Constraint(expr=m.x544**3 - m.x991 == 0)

m.c1201 = Constraint(expr=m.b46*m.x991 - m.x775 == 0)

m.c1202 = Constraint(expr=m.b52*m.x991 - m.x805 == 0)

m.c1203 = Constraint(expr=m.x368*m.x545 - m.x160 == 0)

m.c1204 = Constraint(expr=m.x545*m.x932 - m.x782 == 0)

m.c1205 = Constraint(expr=m.x380*m.x545 - m.x180 == 0)

m.c1206 = Constraint(expr=m.x545*m.x944 - m.x812 == 0)

m.c1207 = Constraint(expr=m.x545**2 - m.x992 == 0)

m.c1208 = Constraint(expr=   m.x161 - m.x992 == 0)

m.c1209 = Constraint(expr=m.x368*m.x992 - m.x781 == 0)

m.c1210 = Constraint(expr=m.x380*m.x992 - m.x811 == 0)

m.c1211 = Constraint(expr=m.x545**3 - m.x993 == 0)

m.c1212 = Constraint(expr=m.b47*m.x993 - m.x780 == 0)

m.c1213 = Constraint(expr=m.b53*m.x993 - m.x810 == 0)

m.c1214 = Constraint(expr=m.x370*m.x546 - m.x164 == 0)

m.c1215 = Constraint(expr=m.x546*m.x934 - m.x787 == 0)

m.c1216 = Constraint(expr=m.x382*m.x546 - m.x184 == 0)

m.c1217 = Constraint(expr=m.x546*m.x946 - m.x817 == 0)

m.c1218 = Constraint(expr=m.x546**2 - m.x994 == 0)

m.c1219 = Constraint(expr=   m.x165 - m.x994 == 0)

m.c1220 = Constraint(expr=m.x370*m.x994 - m.x786 == 0)

m.c1221 = Constraint(expr=m.x382*m.x994 - m.x816 == 0)

m.c1222 = Constraint(expr=m.x546**3 - m.x995 == 0)

m.c1223 = Constraint(expr=m.b48*m.x995 - m.x785 == 0)

m.c1224 = Constraint(expr=m.b54*m.x995 - m.x815 == 0)

m.c1225 = Constraint(expr=m.x372*m.x547 - m.x169 == 0)

m.c1226 = Constraint(expr=m.x547*m.x936 - m.x792 == 0)

m.c1227 = Constraint(expr=m.x384*m.x547 - m.x187 == 0)

m.c1228 = Constraint(expr=m.x547*m.x948 - m.x822 == 0)

m.c1229 = Constraint(expr=m.x547**2 - m.x996 == 0)

m.c1230 = Constraint(expr=   m.x168 - m.x996 == 0)

m.c1231 = Constraint(expr=m.x372*m.x996 - m.x791 == 0)

m.c1232 = Constraint(expr=m.x384*m.x996 - m.x821 == 0)

m.c1233 = Constraint(expr=m.x547**3 - m.x997 == 0)

m.c1234 = Constraint(expr=m.b49*m.x997 - m.x790 == 0)

m.c1235 = Constraint(expr=m.b55*m.x997 - m.x820 == 0)
