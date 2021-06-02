#  MINLP written by GAMS Convert at 04/21/18 13:55:18
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        823      490      137      196        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        665      629       36        0        0        0        0        0
#  FX      7        7        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2183     1779      404        0
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
m.x38 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x40 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x43 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x47 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x51 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x55 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x59 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x62 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
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
m.x101 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x103 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x105 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x107 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x111 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x115 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x117 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x118 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x119 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x121 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x123 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x124 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x125 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,1.16),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,1.16),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,1.16),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,1.16),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x162 = Var(within=Reals,bounds=(3.5,3.5),initialize=3.5)
m.x163 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x164 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x165 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x166 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x167 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x168 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x169 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x170 = Var(within=Reals,bounds=(4.1,4.1),initialize=4.1)
m.x171 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x172 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x173 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x174 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x175 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x176 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x177 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x178 = Var(within=Reals,bounds=(4,4),initialize=4)
m.x179 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x180 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x181 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x182 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x183 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x184 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x185 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x186 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x187 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x189 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x191 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x193 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x195 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x197 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x199 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x201 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x203 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x205 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x207 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x209 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x211 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x213 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x215 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x217 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x219 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x221 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x223 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x225 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x227 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x229 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x231 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x233 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x235 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x237 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x239 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x241 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x243 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x245 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x247 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x249 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x251 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x253 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x255 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x257 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x258 = Var(within=Reals,bounds=(62,65),initialize=62)
m.x259 = Var(within=Reals,bounds=(62,65),initialize=62)
m.x260 = Var(within=Reals,bounds=(62,65),initialize=62)
m.x261 = Var(within=Reals,bounds=(62,65),initialize=62)
m.x262 = Var(within=Reals,bounds=(92.5,95),initialize=92.5)
m.x263 = Var(within=Reals,bounds=(92.5,95),initialize=92.5)
m.x264 = Var(within=Reals,bounds=(92.5,95),initialize=92.5)
m.x265 = Var(within=Reals,bounds=(92.5,95),initialize=92.5)
m.x266 = Var(within=Reals,bounds=(105,109),initialize=105)
m.x267 = Var(within=Reals,bounds=(105,109),initialize=105)
m.x268 = Var(within=Reals,bounds=(105,109),initialize=105)
m.x269 = Var(within=Reals,bounds=(105,109),initialize=105)
m.x270 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x271 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x272 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x273 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x274 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x275 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x276 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x277 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x278 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x279 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x280 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x281 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x282 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x283 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x284 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x285 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x286 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x287 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x289 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x290 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x291 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x292 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x293 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x294 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x295 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x296 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x297 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x298 = Var(within=Reals,bounds=(49,49),initialize=49)
m.x299 = Var(within=Reals,bounds=(-49,1000),initialize=0)
m.x300 = Var(within=Reals,bounds=(49,49),initialize=49)
m.x301 = Var(within=Reals,bounds=(-49,1000),initialize=0)
m.x302 = Var(within=Reals,bounds=(49,49),initialize=49)
m.x303 = Var(within=Reals,bounds=(-49,1000),initialize=0)
m.x304 = Var(within=Reals,bounds=(49,49),initialize=49)
m.x305 = Var(within=Reals,bounds=(-49,1000),initialize=0)
m.x306 = Var(within=Reals,bounds=(-65,1000),initialize=0)
m.x307 = Var(within=Reals,bounds=(-65,1000),initialize=0)
m.x308 = Var(within=Reals,bounds=(-65,1000),initialize=0)
m.x309 = Var(within=Reals,bounds=(-65,1000),initialize=0)
m.x310 = Var(within=Reals,bounds=(-95,1000),initialize=0)
m.x311 = Var(within=Reals,bounds=(-95,1000),initialize=0)
m.x312 = Var(within=Reals,bounds=(-95,1000),initialize=0)
m.x313 = Var(within=Reals,bounds=(-95,1000),initialize=0)
m.x314 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x315 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x316 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x317 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x318 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x319 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x320 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x321 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x322 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x323 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x324 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x325 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x326 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x327 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x328 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x329 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x330 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x331 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x332 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x333 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x334 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x335 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x336 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x337 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x338 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x339 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x340 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x341 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x342 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x343 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x344 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x345 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x346 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x347 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x348 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x349 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x350 = Var(within=Reals,bounds=(0.6,1),initialize=0.6)
m.x351 = Var(within=Reals,bounds=(0.6,1),initialize=0.6)
m.x352 = Var(within=Reals,bounds=(0.6,1),initialize=0.6)
m.x353 = Var(within=Reals,bounds=(0.6,1),initialize=0.6)
m.x354 = Var(within=Reals,bounds=(0.8,1),initialize=0.8)
m.x355 = Var(within=Reals,bounds=(0.8,1),initialize=0.8)
m.x356 = Var(within=Reals,bounds=(0.8,1),initialize=0.8)
m.x357 = Var(within=Reals,bounds=(0.8,1),initialize=0.8)
m.x358 = Var(within=Reals,bounds=(0.85,1),initialize=0.85)
m.x359 = Var(within=Reals,bounds=(0.85,1),initialize=0.85)
m.x360 = Var(within=Reals,bounds=(0.85,1),initialize=0.85)
m.x361 = Var(within=Reals,bounds=(0.85,1),initialize=0.85)
m.x362 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x363 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x364 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x365 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x366 = Var(within=Reals,bounds=(100,1000),initialize=100)
m.x367 = Var(within=Reals,bounds=(100,1000),initialize=100)
m.x368 = Var(within=Reals,bounds=(100,1000),initialize=100)
m.x369 = Var(within=Reals,bounds=(100,1000),initialize=100)
m.x370 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x371 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x372 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x373 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x374 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x375 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x376 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x377 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x378 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x379 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x380 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x381 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x382 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x383 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x384 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x385 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x386 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x387 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x388 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x389 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x390 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x391 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x392 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x393 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x394 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x395 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x396 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x397 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x398 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x399 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x400 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x401 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x402 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x403 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x404 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x405 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x406 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x407 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x408 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x409 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x410 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x411 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x412 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x413 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x414 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x415 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x416 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x417 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x418 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x419 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x420 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x421 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x422 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x423 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x424 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x425 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x426 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x427 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x428 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x429 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x430 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x431 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x432 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x433 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x434 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x435 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x436 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x437 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x438 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x439 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x440 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x441 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x442 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x443 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x444 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x445 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x446 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x447 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x448 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x449 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x450 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x451 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x452 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x453 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x454 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x455 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x456 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x457 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x458 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x459 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x460 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x461 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x462 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x463 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x464 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x465 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x466 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x467 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x468 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x469 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x470 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x471 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x472 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x473 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x474 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x475 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x476 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x477 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x478 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x479 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x480 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x481 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x482 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x483 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x484 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x485 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x486 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x487 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x488 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x489 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x490 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x491 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x492 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x493 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x494 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x495 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x496 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x497 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x498 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x499 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x500 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x501 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x502 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x503 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x504 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x505 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x506 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x507 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x508 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x509 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x510 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x511 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x512 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x513 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x514 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x515 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x516 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x517 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x518 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x519 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x520 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x521 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x522 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x523 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x524 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x525 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x526 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x527 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x528 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x529 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x530 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x531 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x532 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x533 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x534 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x535 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x536 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x537 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x538 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x539 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x540 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x541 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x542 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x543 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x544 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x545 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x546 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x547 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x548 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x549 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x550 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x551 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x552 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x553 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x554 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x555 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x556 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x557 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x558 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x559 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x560 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x561 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x562 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x563 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x564 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x565 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x566 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x567 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x568 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x569 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x570 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x571 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x572 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x573 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x574 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x575 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x576 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x577 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x578 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x579 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x580 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x581 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x582 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x583 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x584 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x585 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x586 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x587 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x588 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x589 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x590 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x591 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x592 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x593 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x594 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x595 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x596 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x597 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x598 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x599 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x600 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x601 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x602 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x603 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x604 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x605 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x606 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x607 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x608 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x609 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x610 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x611 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x612 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x613 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x614 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x615 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x616 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x617 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x618 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x619 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x620 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x621 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x622 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x623 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x624 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x625 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x626 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x627 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x628 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x629 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x630 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x631 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x632 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x633 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x634 = Var(within=Reals,bounds=(0.36,1),initialize=0.36)
m.x635 = Var(within=Reals,bounds=(0.216,1),initialize=0.216)
m.x636 = Var(within=Reals,bounds=(0.36,1),initialize=0.36)
m.x637 = Var(within=Reals,bounds=(0.216,1),initialize=0.216)
m.x638 = Var(within=Reals,bounds=(0.36,1),initialize=0.36)
m.x639 = Var(within=Reals,bounds=(0.216,1),initialize=0.216)
m.x640 = Var(within=Reals,bounds=(0.36,1),initialize=0.36)
m.x641 = Var(within=Reals,bounds=(0.216,1),initialize=0.216)
m.x642 = Var(within=Reals,bounds=(0.64,1),initialize=0.64)
m.x643 = Var(within=Reals,bounds=(0.512,1),initialize=0.512)
m.x644 = Var(within=Reals,bounds=(0.64,1),initialize=0.64)
m.x645 = Var(within=Reals,bounds=(0.512,1),initialize=0.512)
m.x646 = Var(within=Reals,bounds=(0.64,1),initialize=0.64)
m.x647 = Var(within=Reals,bounds=(0.512,1),initialize=0.512)
m.x648 = Var(within=Reals,bounds=(0.64,1),initialize=0.64)
m.x649 = Var(within=Reals,bounds=(0.512,1),initialize=0.512)
m.x650 = Var(within=Reals,bounds=(0.7225,1),initialize=0.7225)
m.x651 = Var(within=Reals,bounds=(0.614125,1),initialize=0.614125)
m.x652 = Var(within=Reals,bounds=(0.7225,1),initialize=0.7225)
m.x653 = Var(within=Reals,bounds=(0.614125,1),initialize=0.614125)
m.x654 = Var(within=Reals,bounds=(0.7225,1),initialize=0.7225)
m.x655 = Var(within=Reals,bounds=(0.614125,1),initialize=0.614125)
m.x656 = Var(within=Reals,bounds=(0.7225,1),initialize=0.7225)
m.x657 = Var(within=Reals,bounds=(0.614125,1),initialize=0.614125)
m.x658 = Var(within=Reals,bounds=(0.49,1),initialize=0.49)
m.x659 = Var(within=Reals,bounds=(0.343,1),initialize=0.343)
m.x660 = Var(within=Reals,bounds=(0.49,1),initialize=0.49)
m.x661 = Var(within=Reals,bounds=(0.343,1),initialize=0.343)
m.x662 = Var(within=Reals,bounds=(0.49,1),initialize=0.49)
m.x663 = Var(within=Reals,bounds=(0.343,1),initialize=0.343)
m.x664 = Var(within=Reals,bounds=(0.49,1),initialize=0.49)
m.x665 = Var(within=Reals,bounds=(0.343,1),initialize=0.343)

m.obj = Objective(expr=   m.x370 + m.x375 + m.x384 + m.x389 + m.x390 + m.x395 + m.x400 + m.x407 + m.x410 + m.x415
                        + m.x420 + m.x425 + m.x430 + m.x435 + m.x440 + m.x445 + m.x450 + m.x455 + m.x460 + m.x465
                        + m.x470 + m.x475 + m.x480 + m.x485 + m.x490 + m.x495 + m.x500 + m.x505 + m.x510 + m.x515
                        + m.x520 + m.x525 + m.x530 + m.x535 + m.x540 + m.x545, sense=minimize)

m.c2 = Constraint(expr=   m.x187 + 27.42831624*m.x189 + 37.5407324*m.x191 - 57.2814121*m.x193 == 0)

m.c3 = Constraint(expr=   m.x195 + 27.42831624*m.x197 + 37.5407324*m.x199 - 57.2814121*m.x201 == 0)

m.c4 = Constraint(expr=   m.x203 + 27.42831624*m.x205 + 37.5407324*m.x207 - 57.2814121*m.x209 == 0)

m.c5 = Constraint(expr=   m.x211 + 27.42831624*m.x213 - 57.2814121*m.x215 + 37.5407324*m.x217 == 0)

m.c6 = Constraint(expr= - 57.2814121*m.x193 + m.x219 + 37.5407324*m.x221 + 27.42831624*m.x223 == 0)

m.c7 = Constraint(expr= - 57.2814121*m.x201 + m.x225 + 37.5407324*m.x227 + 27.42831624*m.x229 == 0)

m.c8 = Constraint(expr= - 57.2814121*m.x209 + m.x231 + 37.5407324*m.x233 + 27.42831624*m.x235 == 0)

m.c9 = Constraint(expr= - 57.2814121*m.x215 + m.x237 + 37.5407324*m.x239 + 27.42831624*m.x241 == 0)

m.c10 = Constraint(expr= - 57.2814121*m.x193 + m.x243 + 27.42831624*m.x245 + 37.5407324*m.x247 == 0)

m.c11 = Constraint(expr= - 57.2814121*m.x201 + m.x249 + 27.42831624*m.x251 + 37.5407324*m.x253 == 0)

m.c12 = Constraint(expr=   27.42831624*m.x38 - 57.2814121*m.x209 + m.x255 + 37.5407324*m.x257 == 0)

m.c13 = Constraint(expr=   m.x39 + 37.5407324*m.x40 + 27.42831624*m.x41 - 57.2814121*m.x215 == 0)

m.c14 = Constraint(expr=   m.x42 - 76.45219958*m.x43 + 43.14087708*m.x44 + 50.37356589*m.x45 == 0)

m.c15 = Constraint(expr=   m.x46 + 50.37356589*m.x47 + 43.14087708*m.x48 - 76.45219958*m.x49 == 0)

m.c16 = Constraint(expr=   m.x50 + 43.14087708*m.x51 + 50.37356589*m.x52 - 76.45219958*m.x53 == 0)

m.c17 = Constraint(expr=   m.x54 + 50.37356589*m.x55 + 43.14087708*m.x56 - 76.45219958*m.x57 == 0)

m.c18 = Constraint(expr= - 76.45219958*m.x43 + m.x58 + 43.14087708*m.x59 + 50.37356589*m.x60 == 0)

m.c19 = Constraint(expr= - 76.45219958*m.x49 + m.x61 + 43.14087708*m.x62 + 50.37356589*m.x63 == 0)

m.c20 = Constraint(expr= - 76.45219958*m.x53 + m.x64 + 43.14087708*m.x65 + 50.37356589*m.x66 == 0)

m.c21 = Constraint(expr= - 76.45219958*m.x57 + m.x67 + 43.14087708*m.x68 + 50.37356589*m.x69 == 0)

m.c22 = Constraint(expr=   m.x70 + 58.31011875*m.x71 - 25.39911174*m.x72 - 69.39622571*m.x73 == 0)

m.c23 = Constraint(expr=   m.x74 - 25.39911174*m.x75 - 69.39622571*m.x76 + 58.31011875*m.x77 == 0)

m.c24 = Constraint(expr=   m.x78 + 58.31011875*m.x79 - 69.39622571*m.x80 - 25.39911174*m.x81 == 0)

m.c25 = Constraint(expr=   m.x82 - 69.39622571*m.x83 - 25.39911174*m.x84 + 58.31011875*m.x85 == 0)

m.c26 = Constraint(expr= - 69.39622571*m.x73 + m.x86 + 58.31011875*m.x87 - 25.39911174*m.x88 == 0)

m.c27 = Constraint(expr= - 69.39622571*m.x76 + m.x89 + 58.31011875*m.x90 - 25.39911174*m.x91 == 0)

m.c28 = Constraint(expr= - 69.39622571*m.x80 + m.x92 + 58.31011875*m.x93 - 25.39911174*m.x94 == 0)

m.c29 = Constraint(expr= - 69.39622571*m.x83 + m.x95 - 25.39911174*m.x96 + 58.31011875*m.x97 == 0)

m.c30 = Constraint(expr=   m.x98 - 34.92732674*m.x99 + 63.61644904*m.x100 - 2.03724124*m.x101 == 0)

m.c31 = Constraint(expr=   m.x102 - 2.03724124*m.x103 - 34.92732674*m.x104 + 63.61644904*m.x105 == 0)

m.c32 = Constraint(expr=   m.x106 - 34.92732674*m.x107 - 2.03724124*m.x108 + 63.61644904*m.x109 == 0)

m.c33 = Constraint(expr=   m.x110 + 63.61644904*m.x111 - 2.03724124*m.x112 - 34.92732674*m.x113 == 0)

m.c34 = Constraint(expr= - 34.92732674*m.x99 + m.x114 - 2.03724124*m.x115 + 63.61644904*m.x116 == 0)

m.c35 = Constraint(expr= - 34.92732674*m.x104 + m.x117 + 63.61644904*m.x118 - 2.03724124*m.x119 == 0)

m.c36 = Constraint(expr= - 34.92732674*m.x107 + m.x120 - 2.03724124*m.x121 + 63.61644904*m.x122 == 0)

m.c37 = Constraint(expr= - 34.92732674*m.x113 + m.x123 - 2.03724124*m.x124 + 63.61644904*m.x125 == 0)

m.c38 = Constraint(expr=   m.x126 + m.x127 + m.x128 + m.x129 >= 1.152222222)

m.c39 = Constraint(expr= - m.x130 + m.x131 == 0)

m.c40 = Constraint(expr= - m.x132 + m.x133 == 0)

m.c41 = Constraint(expr= - m.x134 + m.x135 == 0)

m.c42 = Constraint(expr= - m.x136 + m.x137 == 0)

m.c43 = Constraint(expr= - m.x138 + m.x139 == 0)

m.c44 = Constraint(expr= - m.x140 + m.x141 == 0)

m.c45 = Constraint(expr= - m.x142 + m.x143 == 0)

m.c46 = Constraint(expr= - m.x144 + m.x145 == 0)

m.c47 = Constraint(expr=   m.x138 - m.x146 == 0)

m.c48 = Constraint(expr=   m.x140 - m.x147 == 0)

m.c49 = Constraint(expr=   m.x142 - m.x148 == 0)

m.c50 = Constraint(expr=   m.x144 - m.x149 == 0)

m.c51 = Constraint(expr= - m.x150 + m.x151 == 0)

m.c52 = Constraint(expr= - m.x152 + m.x153 == 0)

m.c53 = Constraint(expr= - m.x154 + m.x155 == 0)

m.c54 = Constraint(expr= - m.x156 + m.x157 == 0)

m.c55 = Constraint(expr=   m.x158 == 0.296666667)

m.c56 = Constraint(expr=   m.x159 == 0.294444444)

m.c57 = Constraint(expr=   m.x160 == 0.283888889)

m.c58 = Constraint(expr=   m.x161 == 0.277222222)

m.c59 = Constraint(expr=   m.x126 - m.x131 == 0)

m.c60 = Constraint(expr=   m.x127 - m.x133 == 0)

m.c61 = Constraint(expr=   m.x128 - m.x135 == 0)

m.c62 = Constraint(expr=   m.x129 - m.x137 == 0)

m.c63 = Constraint(expr=   3600*m.x130 - 3600*m.x139 + 1800*m.x162 - 1800*m.x163 == 0)

m.c64 = Constraint(expr=   3600*m.x132 - 3600*m.x141 + 1800*m.x164 - 1800*m.x165 == 0)

m.c65 = Constraint(expr=   3600*m.x134 - 3600*m.x143 + 1800*m.x166 - 1800*m.x167 == 0)

m.c66 = Constraint(expr=   3600*m.x136 - 3600*m.x145 + 1800*m.x168 - 1800*m.x169 == 0)

m.c67 = Constraint(expr=   3600*m.x146 - 3600*m.x151 + 720*m.x170 - 720*m.x171 == 0)

m.c68 = Constraint(expr=   3600*m.x147 - 3600*m.x153 + 720*m.x172 - 720*m.x173 == 0)

m.c69 = Constraint(expr=   3600*m.x148 - 3600*m.x155 + 720*m.x174 - 720*m.x175 == 0)

m.c70 = Constraint(expr=   3600*m.x149 - 3600*m.x157 + 720*m.x176 - 720*m.x177 == 0)

m.c71 = Constraint(expr=   3600*m.x150 - 3600*m.x158 + 1600*m.x178 - 1600*m.x179 == 0)

m.c72 = Constraint(expr=   3600*m.x152 - 3600*m.x159 + 1600*m.x180 - 1600*m.x181 == 0)

m.c73 = Constraint(expr=   3600*m.x154 - 3600*m.x160 + 1600*m.x182 - 1600*m.x183 == 0)

m.c74 = Constraint(expr=   3600*m.x156 - 3600*m.x161 + 1600*m.x184 - 1600*m.x185 == 0)

m.c75 = Constraint(expr= - m.x163 + m.x164 == 0)

m.c76 = Constraint(expr= - m.x165 + m.x166 == 0)

m.c77 = Constraint(expr= - m.x167 + m.x168 == 0)

m.c78 = Constraint(expr= - m.x171 + m.x172 == 0)

m.c79 = Constraint(expr= - m.x173 + m.x174 == 0)

m.c80 = Constraint(expr= - m.x175 + m.x176 == 0)

m.c81 = Constraint(expr= - m.x179 + m.x180 == 0)

m.c82 = Constraint(expr= - m.x181 + m.x182 == 0)

m.c83 = Constraint(expr= - m.x183 + m.x184 == 0)

m.c84 = Constraint(expr= - 0.2*m.b2 + m.x186 >= 0)

m.c85 = Constraint(expr= - 0.2*m.b3 + m.x188 >= 0)

m.c86 = Constraint(expr= - 0.2*m.b4 + m.x190 >= 0)

m.c87 = Constraint(expr= - 0.2*m.b5 + m.x192 >= 0)

m.c88 = Constraint(expr= - 0.2*m.b6 + m.x194 >= 0)

m.c89 = Constraint(expr= - 0.2*m.b7 + m.x196 >= 0)

m.c90 = Constraint(expr= - 0.2*m.b8 + m.x198 >= 0)

m.c91 = Constraint(expr= - 0.2*m.b9 + m.x200 >= 0)

m.c92 = Constraint(expr= - 0.2*m.b10 + m.x202 >= 0)

m.c93 = Constraint(expr= - 0.2*m.b11 + m.x204 >= 0)

m.c94 = Constraint(expr= - 0.2*m.b12 + m.x206 >= 0)

m.c95 = Constraint(expr= - 0.2*m.b13 + m.x208 >= 0)

m.c96 = Constraint(expr= - 0.25*m.b14 + m.x210 >= 0)

m.c97 = Constraint(expr= - 0.25*m.b15 + m.x212 >= 0)

m.c98 = Constraint(expr= - 0.25*m.b16 + m.x214 >= 0)

m.c99 = Constraint(expr= - 0.25*m.b17 + m.x216 >= 0)

m.c100 = Constraint(expr= - 0.25*m.b18 + m.x218 >= 0)

m.c101 = Constraint(expr= - 0.25*m.b19 + m.x220 >= 0)

m.c102 = Constraint(expr= - 0.25*m.b20 + m.x222 >= 0)

m.c103 = Constraint(expr= - 0.25*m.b21 + m.x224 >= 0)

m.c104 = Constraint(expr= - 0.4*m.b22 + m.x226 >= 0)

m.c105 = Constraint(expr= - 0.4*m.b23 + m.x228 >= 0)

m.c106 = Constraint(expr= - 0.4*m.b24 + m.x230 >= 0)

m.c107 = Constraint(expr= - 0.4*m.b25 + m.x232 >= 0)

m.c108 = Constraint(expr= - 0.4*m.b26 + m.x234 >= 0)

m.c109 = Constraint(expr= - 0.4*m.b27 + m.x236 >= 0)

m.c110 = Constraint(expr= - 0.4*m.b28 + m.x238 >= 0)

m.c111 = Constraint(expr= - 0.4*m.b29 + m.x240 >= 0)

m.c112 = Constraint(expr= - 0.24*m.b30 + m.x242 >= 0)

m.c113 = Constraint(expr= - 0.24*m.b31 + m.x244 >= 0)

m.c114 = Constraint(expr= - 0.24*m.b32 + m.x246 >= 0)

m.c115 = Constraint(expr= - 0.24*m.b33 + m.x248 >= 0)

m.c116 = Constraint(expr= - 0.24*m.b34 + m.x250 >= 0)

m.c117 = Constraint(expr= - 0.24*m.b35 + m.x252 >= 0)

m.c118 = Constraint(expr= - 0.24*m.b36 + m.x254 >= 0)

m.c119 = Constraint(expr= - 0.24*m.b37 + m.x256 >= 0)

m.c120 = Constraint(expr= - 0.8*m.b2 + m.x186 <= 0)

m.c121 = Constraint(expr= - 0.8*m.b3 + m.x188 <= 0)

m.c122 = Constraint(expr= - 0.8*m.b4 + m.x190 <= 0)

m.c123 = Constraint(expr= - 0.8*m.b5 + m.x192 <= 0)

m.c124 = Constraint(expr= - 0.8*m.b6 + m.x194 <= 0)

m.c125 = Constraint(expr= - 0.8*m.b7 + m.x196 <= 0)

m.c126 = Constraint(expr= - 0.8*m.b8 + m.x198 <= 0)

m.c127 = Constraint(expr= - 0.8*m.b9 + m.x200 <= 0)

m.c128 = Constraint(expr= - 0.8*m.b10 + m.x202 <= 0)

m.c129 = Constraint(expr= - 0.8*m.b11 + m.x204 <= 0)

m.c130 = Constraint(expr= - 0.8*m.b12 + m.x206 <= 0)

m.c131 = Constraint(expr= - 0.8*m.b13 + m.x208 <= 0)

m.c132 = Constraint(expr= - 0.5*m.b14 + m.x210 <= 0)

m.c133 = Constraint(expr= - 0.5*m.b15 + m.x212 <= 0)

m.c134 = Constraint(expr= - 0.5*m.b16 + m.x214 <= 0)

m.c135 = Constraint(expr= - 0.5*m.b17 + m.x216 <= 0)

m.c136 = Constraint(expr= - 0.5*m.b18 + m.x218 <= 0)

m.c137 = Constraint(expr= - 0.5*m.b19 + m.x220 <= 0)

m.c138 = Constraint(expr= - 0.5*m.b20 + m.x222 <= 0)

m.c139 = Constraint(expr= - 0.5*m.b21 + m.x224 <= 0)

m.c140 = Constraint(expr= - 0.7*m.b22 + m.x226 <= 0)

m.c141 = Constraint(expr= - 0.7*m.b23 + m.x228 <= 0)

m.c142 = Constraint(expr= - 0.7*m.b24 + m.x230 <= 0)

m.c143 = Constraint(expr= - 0.7*m.b25 + m.x232 <= 0)

m.c144 = Constraint(expr= - 0.7*m.b26 + m.x234 <= 0)

m.c145 = Constraint(expr= - 0.7*m.b27 + m.x236 <= 0)

m.c146 = Constraint(expr= - 0.7*m.b28 + m.x238 <= 0)

m.c147 = Constraint(expr= - 0.7*m.b29 + m.x240 <= 0)

m.c148 = Constraint(expr= - 0.58*m.b30 + m.x242 <= 0)

m.c149 = Constraint(expr= - 0.58*m.b31 + m.x244 <= 0)

m.c150 = Constraint(expr= - 0.58*m.b32 + m.x246 <= 0)

m.c151 = Constraint(expr= - 0.58*m.b33 + m.x248 <= 0)

m.c152 = Constraint(expr= - 0.58*m.b34 + m.x250 <= 0)

m.c153 = Constraint(expr= - 0.58*m.b35 + m.x252 <= 0)

m.c154 = Constraint(expr= - 0.58*m.b36 + m.x254 <= 0)

m.c155 = Constraint(expr= - 0.58*m.b37 + m.x256 <= 0)

m.c156 = Constraint(expr= - m.x162 + m.x258 == 60)

m.c157 = Constraint(expr= - m.x164 + m.x259 == 60)

m.c158 = Constraint(expr= - m.x166 + m.x260 == 60)

m.c159 = Constraint(expr= - m.x168 + m.x261 == 60)

m.c160 = Constraint(expr= - m.x170 + m.x262 == 90)

m.c161 = Constraint(expr= - m.x172 + m.x263 == 90)

m.c162 = Constraint(expr= - m.x174 + m.x264 == 90)

m.c163 = Constraint(expr= - m.x176 + m.x265 == 90)

m.c164 = Constraint(expr= - m.x178 + m.x266 == 103)

m.c165 = Constraint(expr= - m.x180 + m.x267 == 103)

m.c166 = Constraint(expr= - m.x182 + m.x268 == 103)

m.c167 = Constraint(expr= - m.x184 + m.x269 == 103)

m.c168 = Constraint(expr= - m.x258 + m.x270 - m.x271 == 0)

m.c169 = Constraint(expr= - m.x259 + m.x272 - m.x273 == 0)

m.c170 = Constraint(expr= - m.x260 + m.x274 - m.x275 == 0)

m.c171 = Constraint(expr= - m.x261 + m.x276 - m.x277 == 0)

m.c172 = Constraint(expr=   m.x278 - m.x279 - m.x280 == 0)

m.c173 = Constraint(expr=   m.x281 - m.x282 - m.x283 == 0)

m.c174 = Constraint(expr=   m.x284 - m.x285 - m.x286 == 0)

m.c175 = Constraint(expr=   m.x287 - m.x288 - m.x289 == 0)

m.c176 = Constraint(expr= - m.x266 + m.x290 - m.x291 == 0)

m.c177 = Constraint(expr= - m.x267 + m.x292 - m.x293 == 0)

m.c178 = Constraint(expr= - m.x268 + m.x294 - m.x295 == 0)

m.c179 = Constraint(expr= - m.x269 + m.x296 - m.x297 == 0)

m.c180 = Constraint(expr=   m.x270 - m.x298 - m.x299 == 0)

m.c181 = Constraint(expr=   m.x272 - m.x300 - m.x301 == 0)

m.c182 = Constraint(expr=   m.x274 - m.x302 - m.x303 == 0)

m.c183 = Constraint(expr=   m.x276 - m.x304 - m.x305 == 0)

m.c184 = Constraint(expr= - m.x258 + m.x278 - m.x306 == 0)

m.c185 = Constraint(expr= - m.x259 + m.x281 - m.x307 == 0)

m.c186 = Constraint(expr= - m.x260 + m.x284 - m.x308 == 0)

m.c187 = Constraint(expr= - m.x261 + m.x287 - m.x309 == 0)

m.c188 = Constraint(expr= - m.x262 + m.x290 - m.x310 == 0)

m.c189 = Constraint(expr= - m.x263 + m.x292 - m.x311 == 0)

m.c190 = Constraint(expr= - m.x264 + m.x294 - m.x312 == 0)

m.c191 = Constraint(expr= - m.x265 + m.x296 - m.x313 == 0)

m.c192 = Constraint(expr=   0.2*m.b2 - m.x186 + m.x314 <= 0.2)

m.c193 = Constraint(expr=   0.2*m.b3 - m.x188 + m.x315 <= 0.2)

m.c194 = Constraint(expr=   0.2*m.b4 - m.x190 + m.x316 <= 0.2)

m.c195 = Constraint(expr=   0.2*m.b5 - m.x192 + m.x317 <= 0.2)

m.c196 = Constraint(expr=   0.2*m.b6 - m.x194 + m.x318 <= 0.2)

m.c197 = Constraint(expr=   0.2*m.b7 - m.x196 + m.x319 <= 0.2)

m.c198 = Constraint(expr=   0.2*m.b8 - m.x198 + m.x320 <= 0.2)

m.c199 = Constraint(expr=   0.2*m.b9 - m.x200 + m.x321 <= 0.2)

m.c200 = Constraint(expr=   0.2*m.b10 - m.x202 + m.x322 <= 0.2)

m.c201 = Constraint(expr=   0.2*m.b11 - m.x204 + m.x323 <= 0.2)

m.c202 = Constraint(expr=   0.2*m.b12 - m.x206 + m.x324 <= 0.2)

m.c203 = Constraint(expr=   0.2*m.b13 - m.x208 + m.x325 <= 0.2)

m.c204 = Constraint(expr=   0.25*m.b14 - m.x210 + m.x326 <= 0.25)

m.c205 = Constraint(expr=   0.25*m.b15 - m.x212 + m.x327 <= 0.25)

m.c206 = Constraint(expr=   0.25*m.b16 - m.x214 + m.x328 <= 0.25)

m.c207 = Constraint(expr=   0.25*m.b17 - m.x216 + m.x329 <= 0.25)

m.c208 = Constraint(expr=   0.25*m.b18 - m.x218 + m.x330 <= 0.25)

m.c209 = Constraint(expr=   0.25*m.b19 - m.x220 + m.x331 <= 0.25)

m.c210 = Constraint(expr=   0.25*m.b20 - m.x222 + m.x332 <= 0.25)

m.c211 = Constraint(expr=   0.25*m.b21 - m.x224 + m.x333 <= 0.25)

m.c212 = Constraint(expr=   0.4*m.b22 - m.x226 + m.x334 <= 0.4)

m.c213 = Constraint(expr=   0.4*m.b23 - m.x228 + m.x335 <= 0.4)

m.c214 = Constraint(expr=   0.4*m.b24 - m.x230 + m.x336 <= 0.4)

m.c215 = Constraint(expr=   0.4*m.b25 - m.x232 + m.x337 <= 0.4)

m.c216 = Constraint(expr=   0.4*m.b26 - m.x234 + m.x338 <= 0.4)

m.c217 = Constraint(expr=   0.4*m.b27 - m.x236 + m.x339 <= 0.4)

m.c218 = Constraint(expr=   0.4*m.b28 - m.x238 + m.x340 <= 0.4)

m.c219 = Constraint(expr=   0.4*m.b29 - m.x240 + m.x341 <= 0.4)

m.c220 = Constraint(expr=   0.24*m.b30 - m.x242 + m.x342 <= 0.24)

m.c221 = Constraint(expr=   0.24*m.b31 - m.x244 + m.x343 <= 0.24)

m.c222 = Constraint(expr=   0.24*m.b32 - m.x246 + m.x344 <= 0.24)

m.c223 = Constraint(expr=   0.24*m.b33 - m.x248 + m.x345 <= 0.24)

m.c224 = Constraint(expr=   0.24*m.b34 - m.x250 + m.x346 <= 0.24)

m.c225 = Constraint(expr=   0.24*m.b35 - m.x252 + m.x347 <= 0.24)

m.c226 = Constraint(expr=   0.24*m.b36 - m.x254 + m.x348 <= 0.24)

m.c227 = Constraint(expr=   0.24*m.b37 - m.x256 + m.x349 <= 0.24)

m.c228 = Constraint(expr= - m.x186 + m.x314 >= 0)

m.c229 = Constraint(expr= - m.x188 + m.x315 >= 0)

m.c230 = Constraint(expr= - m.x190 + m.x316 >= 0)

m.c231 = Constraint(expr= - m.x192 + m.x317 >= 0)

m.c232 = Constraint(expr= - m.x194 + m.x318 >= 0)

m.c233 = Constraint(expr= - m.x196 + m.x319 >= 0)

m.c234 = Constraint(expr= - m.x198 + m.x320 >= 0)

m.c235 = Constraint(expr= - m.x200 + m.x321 >= 0)

m.c236 = Constraint(expr= - m.x202 + m.x322 >= 0)

m.c237 = Constraint(expr= - m.x204 + m.x323 >= 0)

m.c238 = Constraint(expr= - m.x206 + m.x324 >= 0)

m.c239 = Constraint(expr= - m.x208 + m.x325 >= 0)

m.c240 = Constraint(expr= - m.x210 + m.x326 >= 0)

m.c241 = Constraint(expr= - m.x212 + m.x327 >= 0)

m.c242 = Constraint(expr= - m.x214 + m.x328 >= 0)

m.c243 = Constraint(expr= - m.x216 + m.x329 >= 0)

m.c244 = Constraint(expr= - m.x218 + m.x330 >= 0)

m.c245 = Constraint(expr= - m.x220 + m.x331 >= 0)

m.c246 = Constraint(expr= - m.x222 + m.x332 >= 0)

m.c247 = Constraint(expr= - m.x224 + m.x333 >= 0)

m.c248 = Constraint(expr= - m.x226 + m.x334 >= 0)

m.c249 = Constraint(expr= - m.x228 + m.x335 >= 0)

m.c250 = Constraint(expr= - m.x230 + m.x336 >= 0)

m.c251 = Constraint(expr= - m.x232 + m.x337 >= 0)

m.c252 = Constraint(expr= - m.x234 + m.x338 >= 0)

m.c253 = Constraint(expr= - m.x236 + m.x339 >= 0)

m.c254 = Constraint(expr= - m.x238 + m.x340 >= 0)

m.c255 = Constraint(expr= - m.x240 + m.x341 >= 0)

m.c256 = Constraint(expr= - m.x242 + m.x342 >= 0)

m.c257 = Constraint(expr= - m.x244 + m.x343 >= 0)

m.c258 = Constraint(expr= - m.x246 + m.x344 >= 0)

m.c259 = Constraint(expr= - m.x248 + m.x345 >= 0)

m.c260 = Constraint(expr= - m.x250 + m.x346 >= 0)

m.c261 = Constraint(expr= - m.x252 + m.x347 >= 0)

m.c262 = Constraint(expr= - m.x254 + m.x348 >= 0)

m.c263 = Constraint(expr= - m.x256 + m.x349 >= 0)

m.c264 = Constraint(expr= - 0.6*m.b2 + m.x314 <= 0.2)

m.c265 = Constraint(expr= - 0.6*m.b3 + m.x315 <= 0.2)

m.c266 = Constraint(expr= - 0.6*m.b4 + m.x316 <= 0.2)

m.c267 = Constraint(expr= - 0.6*m.b5 + m.x317 <= 0.2)

m.c268 = Constraint(expr= - 0.6*m.b6 + m.x318 <= 0.2)

m.c269 = Constraint(expr= - 0.6*m.b7 + m.x319 <= 0.2)

m.c270 = Constraint(expr= - 0.6*m.b8 + m.x320 <= 0.2)

m.c271 = Constraint(expr= - 0.6*m.b9 + m.x321 <= 0.2)

m.c272 = Constraint(expr= - 0.6*m.b10 + m.x322 <= 0.2)

m.c273 = Constraint(expr= - 0.6*m.b11 + m.x323 <= 0.2)

m.c274 = Constraint(expr= - 0.6*m.b12 + m.x324 <= 0.2)

m.c275 = Constraint(expr= - 0.6*m.b13 + m.x325 <= 0.2)

m.c276 = Constraint(expr= - 0.25*m.b14 + m.x326 <= 0.25)

m.c277 = Constraint(expr= - 0.25*m.b15 + m.x327 <= 0.25)

m.c278 = Constraint(expr= - 0.25*m.b16 + m.x328 <= 0.25)

m.c279 = Constraint(expr= - 0.25*m.b17 + m.x329 <= 0.25)

m.c280 = Constraint(expr= - 0.25*m.b18 + m.x330 <= 0.25)

m.c281 = Constraint(expr= - 0.25*m.b19 + m.x331 <= 0.25)

m.c282 = Constraint(expr= - 0.25*m.b20 + m.x332 <= 0.25)

m.c283 = Constraint(expr= - 0.25*m.b21 + m.x333 <= 0.25)

m.c284 = Constraint(expr= - 0.3*m.b22 + m.x334 <= 0.4)

m.c285 = Constraint(expr= - 0.3*m.b23 + m.x335 <= 0.4)

m.c286 = Constraint(expr= - 0.3*m.b24 + m.x336 <= 0.4)

m.c287 = Constraint(expr= - 0.3*m.b25 + m.x337 <= 0.4)

m.c288 = Constraint(expr= - 0.3*m.b26 + m.x338 <= 0.4)

m.c289 = Constraint(expr= - 0.3*m.b27 + m.x339 <= 0.4)

m.c290 = Constraint(expr= - 0.3*m.b28 + m.x340 <= 0.4)

m.c291 = Constraint(expr= - 0.3*m.b29 + m.x341 <= 0.4)

m.c292 = Constraint(expr= - 0.34*m.b30 + m.x342 <= 0.24)

m.c293 = Constraint(expr= - 0.34*m.b31 + m.x343 <= 0.24)

m.c294 = Constraint(expr= - 0.34*m.b32 + m.x344 <= 0.24)

m.c295 = Constraint(expr= - 0.34*m.b33 + m.x345 <= 0.24)

m.c296 = Constraint(expr= - 0.34*m.b34 + m.x346 <= 0.24)

m.c297 = Constraint(expr= - 0.34*m.b35 + m.x347 <= 0.24)

m.c298 = Constraint(expr= - 0.34*m.b36 + m.x348 <= 0.24)

m.c299 = Constraint(expr= - 0.34*m.b37 + m.x349 <= 0.24)

m.c300 = Constraint(expr= - 0.4*m.b2 + m.x350 <= 0.6)

m.c301 = Constraint(expr= - 0.4*m.b3 + m.x351 <= 0.6)

m.c302 = Constraint(expr= - 0.4*m.b4 + m.x352 <= 0.6)

m.c303 = Constraint(expr= - 0.4*m.b5 + m.x353 <= 0.6)

m.c304 = Constraint(expr= - 0.2*m.b14 + m.x354 <= 0.8)

m.c305 = Constraint(expr= - 0.2*m.b15 + m.x355 <= 0.8)

m.c306 = Constraint(expr= - 0.2*m.b16 + m.x356 <= 0.8)

m.c307 = Constraint(expr= - 0.2*m.b17 + m.x357 <= 0.8)

m.c308 = Constraint(expr= - 0.15*m.b22 + m.x358 <= 0.85)

m.c309 = Constraint(expr= - 0.15*m.b23 + m.x359 <= 0.85)

m.c310 = Constraint(expr= - 0.15*m.b24 + m.x360 <= 0.85)

m.c311 = Constraint(expr= - 0.15*m.b25 + m.x361 <= 0.85)

m.c312 = Constraint(expr= - 0.3*m.b30 + m.x362 <= 0.7)

m.c313 = Constraint(expr= - 0.3*m.b31 + m.x363 <= 0.7)

m.c314 = Constraint(expr= - 0.3*m.b32 + m.x364 <= 0.7)

m.c315 = Constraint(expr= - 0.3*m.b33 + m.x365 <= 0.7)

m.c316 = Constraint(expr=   m.b2 - m.b6 >= 0)

m.c317 = Constraint(expr=   m.b3 - m.b7 >= 0)

m.c318 = Constraint(expr=   m.b4 - m.b8 >= 0)

m.c319 = Constraint(expr=   m.b5 - m.b9 >= 0)

m.c320 = Constraint(expr=   m.b6 - m.b10 >= 0)

m.c321 = Constraint(expr=   m.b7 - m.b11 >= 0)

m.c322 = Constraint(expr=   m.b8 - m.b12 >= 0)

m.c323 = Constraint(expr=   m.b9 - m.b13 >= 0)

m.c324 = Constraint(expr=   m.b14 - m.b18 >= 0)

m.c325 = Constraint(expr=   m.b15 - m.b19 >= 0)

m.c326 = Constraint(expr=   m.b16 - m.b20 >= 0)

m.c327 = Constraint(expr=   m.b17 - m.b21 >= 0)

m.c328 = Constraint(expr=   m.b22 - m.b26 >= 0)

m.c329 = Constraint(expr=   m.b23 - m.b27 >= 0)

m.c330 = Constraint(expr=   m.b24 - m.b28 >= 0)

m.c331 = Constraint(expr=   m.b25 - m.b29 >= 0)

m.c332 = Constraint(expr=   m.b30 - m.b34 >= 0)

m.c333 = Constraint(expr=   m.b31 - m.b35 >= 0)

m.c334 = Constraint(expr=   m.b32 - m.b36 >= 0)

m.c335 = Constraint(expr=   m.b33 - m.b37 >= 0)

m.c336 = Constraint(expr=   m.x131 - m.x186 - m.x194 - m.x202 == 0)

m.c337 = Constraint(expr=   m.x133 - m.x188 - m.x196 - m.x204 == 0)

m.c338 = Constraint(expr=   m.x135 - m.x190 - m.x198 - m.x206 == 0)

m.c339 = Constraint(expr=   m.x137 - m.x192 - m.x200 - m.x208 == 0)

m.c340 = Constraint(expr=   m.x139 - m.x210 - m.x218 - m.x226 - m.x234 == 0)

m.c341 = Constraint(expr=   m.x141 - m.x212 - m.x220 - m.x228 - m.x236 == 0)

m.c342 = Constraint(expr=   m.x143 - m.x214 - m.x222 - m.x230 - m.x238 == 0)

m.c343 = Constraint(expr=   m.x145 - m.x216 - m.x224 - m.x232 - m.x240 == 0)

m.c344 = Constraint(expr=   m.x151 - m.x242 - m.x250 == 0)

m.c345 = Constraint(expr=   m.x153 - m.x244 - m.x252 == 0)

m.c346 = Constraint(expr=   m.x155 - m.x246 - m.x254 == 0)

m.c347 = Constraint(expr=   m.x157 - m.x248 - m.x256 == 0)

m.c348 = Constraint(expr= - 2000*m.b2 + m.x187 - m.x299 >= -2000)

m.c349 = Constraint(expr= - 2000*m.b3 + m.x195 - m.x301 >= -2000)

m.c350 = Constraint(expr= - 2000*m.b4 + m.x203 - m.x303 >= -2000)

m.c351 = Constraint(expr= - 2000*m.b5 + m.x211 - m.x305 >= -2000)

m.c352 = Constraint(expr= - 2000*m.b6 + m.x219 - m.x299 >= -2000)

m.c353 = Constraint(expr= - 2000*m.b7 + m.x225 - m.x301 >= -2000)

m.c354 = Constraint(expr= - 2000*m.b8 + m.x231 - m.x303 >= -2000)

m.c355 = Constraint(expr= - 2000*m.b9 + m.x237 - m.x305 >= -2000)

m.c356 = Constraint(expr= - 2000*m.b10 + m.x243 - m.x299 >= -2000)

m.c357 = Constraint(expr= - 2000*m.b11 + m.x249 - m.x301 >= -2000)

m.c358 = Constraint(expr= - 2000*m.b12 + m.x255 - m.x303 >= -2000)

m.c359 = Constraint(expr= - 2000*m.b13 + m.x39 - m.x305 >= -2000)

m.c360 = Constraint(expr= - 2000*m.b14 + m.x42 - m.x306 >= -2000)

m.c361 = Constraint(expr= - 2000*m.b15 + m.x46 - m.x307 >= -2000)

m.c362 = Constraint(expr= - 2000*m.b16 + m.x50 - m.x308 >= -2000)

m.c363 = Constraint(expr= - 2000*m.b17 + m.x54 - m.x309 >= -2000)

m.c364 = Constraint(expr= - 2000*m.b18 + m.x58 - m.x306 >= -2000)

m.c365 = Constraint(expr= - 2000*m.b19 + m.x61 - m.x307 >= -2000)

m.c366 = Constraint(expr= - 2000*m.b20 + m.x64 - m.x308 >= -2000)

m.c367 = Constraint(expr= - 2000*m.b21 + m.x67 - m.x309 >= -2000)

m.c368 = Constraint(expr= - 2000*m.b22 + m.x70 - m.x306 >= -2000)

m.c369 = Constraint(expr= - 2000*m.b23 + m.x74 - m.x307 >= -2000)

m.c370 = Constraint(expr= - 2000*m.b24 + m.x78 - m.x308 >= -2000)

m.c371 = Constraint(expr= - 2000*m.b25 + m.x82 - m.x309 >= -2000)

m.c372 = Constraint(expr= - 2000*m.b26 + m.x86 - m.x306 >= -2000)

m.c373 = Constraint(expr= - 2000*m.b27 + m.x89 - m.x307 >= -2000)

m.c374 = Constraint(expr= - 2000*m.b28 + m.x92 - m.x308 >= -2000)

m.c375 = Constraint(expr= - 2000*m.b29 + m.x95 - m.x309 >= -2000)

m.c376 = Constraint(expr= - 2000*m.b30 + m.x98 - m.x310 >= -2000)

m.c377 = Constraint(expr= - 2000*m.b31 + m.x102 - m.x311 >= -2000)

m.c378 = Constraint(expr= - 2000*m.b32 + m.x106 - m.x312 >= -2000)

m.c379 = Constraint(expr= - 2000*m.b33 + m.x110 - m.x313 >= -2000)

m.c380 = Constraint(expr= - 2000*m.b34 + m.x114 - m.x310 >= -2000)

m.c381 = Constraint(expr= - 2000*m.b35 + m.x117 - m.x311 >= -2000)

m.c382 = Constraint(expr= - 2000*m.b36 + m.x120 - m.x312 >= -2000)

m.c383 = Constraint(expr= - 2000*m.b37 + m.x123 - m.x313 >= -2000)

m.c384 = Constraint(expr=   1049*m.b2 + m.x187 - m.x299 <= 1049)

m.c385 = Constraint(expr=   1049*m.b3 + m.x195 - m.x301 <= 1049)

m.c386 = Constraint(expr=   1049*m.b4 + m.x203 - m.x303 <= 1049)

m.c387 = Constraint(expr=   1049*m.b5 + m.x211 - m.x305 <= 1049)

m.c388 = Constraint(expr=   1049*m.b6 + m.x219 - m.x299 <= 1049)

m.c389 = Constraint(expr=   1049*m.b7 + m.x225 - m.x301 <= 1049)

m.c390 = Constraint(expr=   1049*m.b8 + m.x231 - m.x303 <= 1049)

m.c391 = Constraint(expr=   1049*m.b9 + m.x237 - m.x305 <= 1049)

m.c392 = Constraint(expr=   1049*m.b10 + m.x243 - m.x299 <= 1049)

m.c393 = Constraint(expr=   1049*m.b11 + m.x249 - m.x301 <= 1049)

m.c394 = Constraint(expr=   1049*m.b12 + m.x255 - m.x303 <= 1049)

m.c395 = Constraint(expr=   1049*m.b13 + m.x39 - m.x305 <= 1049)

m.c396 = Constraint(expr=   1065*m.b14 + m.x42 - m.x306 <= 1065)

m.c397 = Constraint(expr=   1065*m.b15 + m.x46 - m.x307 <= 1065)

m.c398 = Constraint(expr=   1065*m.b16 + m.x50 - m.x308 <= 1065)

m.c399 = Constraint(expr=   1065*m.b17 + m.x54 - m.x309 <= 1065)

m.c400 = Constraint(expr=   1065*m.b18 + m.x58 - m.x306 <= 1065)

m.c401 = Constraint(expr=   1065*m.b19 + m.x61 - m.x307 <= 1065)

m.c402 = Constraint(expr=   1065*m.b20 + m.x64 - m.x308 <= 1065)

m.c403 = Constraint(expr=   1065*m.b21 + m.x67 - m.x309 <= 1065)

m.c404 = Constraint(expr=   1065*m.b22 + m.x70 - m.x306 <= 1065)

m.c405 = Constraint(expr=   1065*m.b23 + m.x74 - m.x307 <= 1065)

m.c406 = Constraint(expr=   1065*m.b24 + m.x78 - m.x308 <= 1065)

m.c407 = Constraint(expr=   1065*m.b25 + m.x82 - m.x309 <= 1065)

m.c408 = Constraint(expr=   1065*m.b26 + m.x86 - m.x306 <= 1065)

m.c409 = Constraint(expr=   1065*m.b27 + m.x89 - m.x307 <= 1065)

m.c410 = Constraint(expr=   1065*m.b28 + m.x92 - m.x308 <= 1065)

m.c411 = Constraint(expr=   1065*m.b29 + m.x95 - m.x309 <= 1065)

m.c412 = Constraint(expr=   1095*m.b30 + m.x98 - m.x310 <= 1095)

m.c413 = Constraint(expr=   1095*m.b31 + m.x102 - m.x311 <= 1095)

m.c414 = Constraint(expr=   1095*m.b32 + m.x106 - m.x312 <= 1095)

m.c415 = Constraint(expr=   1095*m.b33 + m.x110 - m.x313 <= 1095)

m.c416 = Constraint(expr=   1095*m.b34 + m.x114 - m.x310 <= 1095)

m.c417 = Constraint(expr=   1095*m.b35 + m.x117 - m.x311 <= 1095)

m.c418 = Constraint(expr=   1095*m.b36 + m.x120 - m.x312 <= 1095)

m.c419 = Constraint(expr=   1095*m.b37 + m.x123 - m.x313 <= 1095)

m.c420 = Constraint(expr= - m.x262 + m.x279 >= 0)

m.c421 = Constraint(expr= - m.x263 + m.x282 >= 0)

m.c422 = Constraint(expr= - m.x264 + m.x285 >= 0)

m.c423 = Constraint(expr= - m.x265 + m.x288 >= 0)

m.c424 = Constraint(expr=   m.x266 - m.x366 >= 0)

m.c425 = Constraint(expr=   m.x267 - m.x367 >= 0)

m.c426 = Constraint(expr=   m.x268 - m.x368 >= 0)

m.c427 = Constraint(expr=   m.x269 - m.x369 >= 0)

m.c428 = Constraint(expr= - 0.309838295393634*m.x370 + 13.94696158*m.x371 + 24.46510819*m.x372 - 7.28623839*m.x373
                          - 23.57687014*m.x374 <= 0)

m.c429 = Constraint(expr= - 0.309838295393634*m.x375 + 13.94696158*m.x376 + 24.46510819*m.x377 - 7.28623839*m.x378
                          - 23.57687014*m.x379 <= 0)

m.c430 = Constraint(expr=   13.94696158*m.x380 + 24.46510819*m.x381 - 7.28623839*m.x382 - 23.57687014*m.x383
                          - 0.309838295393634*m.x384 <= 0)

m.c431 = Constraint(expr=   13.94696158*m.x385 + 24.46510819*m.x386 - 7.28623839*m.x387 - 23.57687014*m.x388
                          - 0.309838295393634*m.x389 <= 0)

m.c432 = Constraint(expr= - 0.309838295393634*m.x390 + 13.94696158*m.x391 + 24.46510819*m.x392 - 7.28623839*m.x393
                          - 23.57687014*m.x394 <= 0)

m.c433 = Constraint(expr= - 0.309838295393634*m.x395 + 13.94696158*m.x396 + 24.46510819*m.x397 - 7.28623839*m.x398
                          - 23.57687014*m.x399 <= 0)

m.c434 = Constraint(expr= - 0.309838295393634*m.x400 + 13.94696158*m.x401 + 24.46510819*m.x402 - 7.28623839*m.x403
                          - 23.57687014*m.x404 <= 0)

m.c435 = Constraint(expr=   24.46510819*m.x405 - 7.28623839*m.x406 - 0.309838295393634*m.x407 + 13.94696158*m.x408
                          - 23.57687014*m.x409 <= 0)

m.c436 = Constraint(expr= - 0.309838295393634*m.x410 + 13.94696158*m.x411 + 24.46510819*m.x412 - 7.28623839*m.x413
                          - 23.57687014*m.x414 <= 0)

m.c437 = Constraint(expr= - 0.309838295393634*m.x415 + 13.94696158*m.x416 + 24.46510819*m.x417 - 7.28623839*m.x418
                          - 23.57687014*m.x419 <= 0)

m.c438 = Constraint(expr= - 0.309838295393634*m.x420 + 13.94696158*m.x421 + 24.46510819*m.x422 - 7.28623839*m.x423
                          - 23.57687014*m.x424 <= 0)

m.c439 = Constraint(expr= - 0.309838295393634*m.x425 + 13.94696158*m.x426 + 24.46510819*m.x427 - 7.28623839*m.x428
                          - 23.57687014*m.x429 <= 0)

m.c440 = Constraint(expr= - 0.309838295393634*m.x430 + 29.29404529*m.x431 - 108.39408287*m.x432 + 442.21990639*m.x433
                          - 454.58448169*m.x434 <= 0)

m.c441 = Constraint(expr= - 0.309838295393634*m.x435 + 29.29404529*m.x436 - 108.39408287*m.x437 + 442.21990639*m.x438
                          - 454.58448169*m.x439 <= 0)

m.c442 = Constraint(expr= - 0.309838295393634*m.x440 + 29.29404529*m.x441 - 108.39408287*m.x442 + 442.21990639*m.x443
                          - 454.58448169*m.x444 <= 0)

m.c443 = Constraint(expr= - 0.309838295393634*m.x445 + 29.29404529*m.x446 - 108.39408287*m.x447 + 442.21990639*m.x448
                          - 454.58448169*m.x449 <= 0)

m.c444 = Constraint(expr= - 0.309838295393634*m.x450 + 29.29404529*m.x451 - 108.39408287*m.x452 + 442.21990639*m.x453
                          - 454.58448169*m.x454 <= 0)

m.c445 = Constraint(expr= - 0.309838295393634*m.x455 + 29.29404529*m.x456 - 108.39408287*m.x457 + 442.21990639*m.x458
                          - 454.58448169*m.x459 <= 0)

m.c446 = Constraint(expr= - 0.309838295393634*m.x460 + 29.29404529*m.x461 - 108.39408287*m.x462 + 442.21990639*m.x463
                          - 454.58448169*m.x464 <= 0)

m.c447 = Constraint(expr= - 0.309838295393634*m.x465 + 29.29404529*m.x466 - 108.39408287*m.x467 + 442.21990639*m.x468
                          - 454.58448169*m.x469 <= 0)

m.c448 = Constraint(expr= - 0.309838295393634*m.x470 + 25.92674585*m.x471 + 18.13482123*m.x472 + 22.12766012*m.x473
                          - 42.68950769*m.x474 <= 0)

m.c449 = Constraint(expr= - 0.309838295393634*m.x475 + 25.92674585*m.x476 + 18.13482123*m.x477 + 22.12766012*m.x478
                          - 42.68950769*m.x479 <= 0)

m.c450 = Constraint(expr= - 0.309838295393634*m.x480 + 25.92674585*m.x481 + 18.13482123*m.x482 + 22.12766012*m.x483
                          - 42.68950769*m.x484 <= 0)

m.c451 = Constraint(expr= - 0.309838295393634*m.x485 + 25.92674585*m.x486 + 18.13482123*m.x487 + 22.12766012*m.x488
                          - 42.68950769*m.x489 <= 0)

m.c452 = Constraint(expr= - 0.309838295393634*m.x490 + 25.92674585*m.x491 + 18.13482123*m.x492 + 22.12766012*m.x493
                          - 42.68950769*m.x494 <= 0)

m.c453 = Constraint(expr= - 0.309838295393634*m.x495 + 25.92674585*m.x496 + 18.13482123*m.x497 + 22.12766012*m.x498
                          - 42.68950769*m.x499 <= 0)

m.c454 = Constraint(expr= - 0.309838295393634*m.x500 + 25.92674585*m.x501 + 18.13482123*m.x502 + 22.12766012*m.x503
                          - 42.68950769*m.x504 <= 0)

m.c455 = Constraint(expr= - 0.309838295393634*m.x505 + 25.92674585*m.x506 + 18.13482123*m.x507 + 22.12766012*m.x508
                          - 42.68950769*m.x509 <= 0)

m.c456 = Constraint(expr= - 0.309838295393634*m.x510 + 17.4714791*m.x511 - 39.98407808*m.x512 + 134.55943082*m.x513
                          - 135.88441782*m.x514 <= 0)

m.c457 = Constraint(expr= - 0.309838295393634*m.x515 + 17.4714791*m.x516 - 39.98407808*m.x517 + 134.55943082*m.x518
                          - 135.88441782*m.x519 <= 0)

m.c458 = Constraint(expr= - 0.309838295393634*m.x520 + 17.4714791*m.x521 - 39.98407808*m.x522 + 134.55943082*m.x523
                          - 135.88441782*m.x524 <= 0)

m.c459 = Constraint(expr= - 0.309838295393634*m.x525 + 17.4714791*m.x526 - 39.98407808*m.x527 + 134.55943082*m.x528
                          - 135.88441782*m.x529 <= 0)

m.c460 = Constraint(expr= - 0.309838295393634*m.x530 + 17.4714791*m.x531 - 39.98407808*m.x532 + 134.55943082*m.x533
                          - 135.88441782*m.x534 <= 0)

m.c461 = Constraint(expr= - 0.309838295393634*m.x535 + 17.4714791*m.x536 - 39.98407808*m.x537 + 134.55943082*m.x538
                          - 135.88441782*m.x539 <= 0)

m.c462 = Constraint(expr= - 0.309838295393634*m.x540 + 17.4714791*m.x541 - 39.98407808*m.x542 + 134.55943082*m.x543
                          - 135.88441782*m.x544 <= 0)

m.c463 = Constraint(expr= - 0.309838295393634*m.x545 + 17.4714791*m.x546 - 39.98407808*m.x547 + 134.55943082*m.x548
                          - 135.88441782*m.x549 <= 0)

m.c464 = Constraint(expr=m.x130**2 - m.x550 == 0)

m.c465 = Constraint(expr=   m.x271 - 5*m.x550 == 0)

m.c466 = Constraint(expr=m.x132**2 - m.x551 == 0)

m.c467 = Constraint(expr=   m.x273 - 5*m.x551 == 0)

m.c468 = Constraint(expr=m.x134**2 - m.x552 == 0)

m.c469 = Constraint(expr=   m.x275 - 5*m.x552 == 0)

m.c470 = Constraint(expr=m.x136**2 - m.x553 == 0)

m.c471 = Constraint(expr=   m.x277 - 5*m.x553 == 0)

m.c472 = Constraint(expr=m.x138**2 - m.x554 == 0)

m.c473 = Constraint(expr=   m.x280 - 4*m.x554 == 0)

m.c474 = Constraint(expr=m.x140**2 - m.x555 == 0)

m.c475 = Constraint(expr=   m.x283 - 4*m.x555 == 0)

m.c476 = Constraint(expr=m.x142**2 - m.x556 == 0)

m.c477 = Constraint(expr=   m.x286 - 4*m.x556 == 0)

m.c478 = Constraint(expr=m.x144**2 - m.x557 == 0)

m.c479 = Constraint(expr=   m.x289 - 4*m.x557 == 0)

m.c480 = Constraint(expr=m.x150**2 - m.x558 == 0)

m.c481 = Constraint(expr=   m.x291 - 5*m.x558 == 0)

m.c482 = Constraint(expr=m.x152**2 - m.x559 == 0)

m.c483 = Constraint(expr=   m.x293 - 5*m.x559 == 0)

m.c484 = Constraint(expr=m.x154**2 - m.x560 == 0)

m.c485 = Constraint(expr=   m.x295 - 5*m.x560 == 0)

m.c486 = Constraint(expr=m.x156**2 - m.x561 == 0)

m.c487 = Constraint(expr=   m.x297 - 5*m.x561 == 0)

m.c488 = Constraint(expr=m.x186**2 - m.x562 == 0)

m.c489 = Constraint(expr=   m.x189 - m.x562 == 0)

m.c490 = Constraint(expr=m.x186**3 - m.x563 == 0)

m.c491 = Constraint(expr=   m.x374 - m.x563 == 0)

m.c492 = Constraint(expr=m.x188**2 - m.x564 == 0)

m.c493 = Constraint(expr=   m.x197 - m.x564 == 0)

m.c494 = Constraint(expr=m.x188**3 - m.x565 == 0)

m.c495 = Constraint(expr=   m.x379 - m.x565 == 0)

m.c496 = Constraint(expr=m.x190**2 - m.x566 == 0)

m.c497 = Constraint(expr=   m.x205 - m.x566 == 0)

m.c498 = Constraint(expr=m.x190**3 - m.x567 == 0)

m.c499 = Constraint(expr=   m.x383 - m.x567 == 0)

m.c500 = Constraint(expr=m.x192**2 - m.x568 == 0)

m.c501 = Constraint(expr=   m.x213 - m.x568 == 0)

m.c502 = Constraint(expr=m.x192**3 - m.x569 == 0)

m.c503 = Constraint(expr=   m.x388 - m.x569 == 0)

m.c504 = Constraint(expr=m.x194**2 - m.x570 == 0)

m.c505 = Constraint(expr=   m.x223 - m.x570 == 0)

m.c506 = Constraint(expr=m.x194**3 - m.x571 == 0)

m.c507 = Constraint(expr=   m.x394 - m.x571 == 0)

m.c508 = Constraint(expr=m.x196**2 - m.x572 == 0)

m.c509 = Constraint(expr=   m.x229 - m.x572 == 0)

m.c510 = Constraint(expr=m.x196**3 - m.x573 == 0)

m.c511 = Constraint(expr=   m.x399 - m.x573 == 0)

m.c512 = Constraint(expr=m.x198**2 - m.x574 == 0)

m.c513 = Constraint(expr=   m.x235 - m.x574 == 0)

m.c514 = Constraint(expr=m.x198**3 - m.x575 == 0)

m.c515 = Constraint(expr=   m.x404 - m.x575 == 0)

m.c516 = Constraint(expr=m.x200**2 - m.x576 == 0)

m.c517 = Constraint(expr=   m.x241 - m.x576 == 0)

m.c518 = Constraint(expr=m.x200**3 - m.x577 == 0)

m.c519 = Constraint(expr=   m.x409 - m.x577 == 0)

m.c520 = Constraint(expr=m.x202**2 - m.x578 == 0)

m.c521 = Constraint(expr=   m.x245 - m.x578 == 0)

m.c522 = Constraint(expr=m.x202**3 - m.x579 == 0)

m.c523 = Constraint(expr=   m.x414 - m.x579 == 0)

m.c524 = Constraint(expr=m.x204**2 - m.x580 == 0)

m.c525 = Constraint(expr=   m.x251 - m.x580 == 0)

m.c526 = Constraint(expr=m.x204**3 - m.x581 == 0)

m.c527 = Constraint(expr=   m.x419 - m.x581 == 0)

m.c528 = Constraint(expr=m.x206**2 - m.x582 == 0)

m.c529 = Constraint(expr=   m.x38 - m.x582 == 0)

m.c530 = Constraint(expr=m.x206**3 - m.x583 == 0)

m.c531 = Constraint(expr=   m.x424 - m.x583 == 0)

m.c532 = Constraint(expr=m.x208**2 - m.x584 == 0)

m.c533 = Constraint(expr=   m.x41 - m.x584 == 0)

m.c534 = Constraint(expr=m.x208**3 - m.x585 == 0)

m.c535 = Constraint(expr=   m.x429 - m.x585 == 0)

m.c536 = Constraint(expr=m.x210**2 - m.x586 == 0)

m.c537 = Constraint(expr=   m.x45 - m.x586 == 0)

m.c538 = Constraint(expr=m.x210**3 - m.x587 == 0)

m.c539 = Constraint(expr=   m.x434 - m.x587 == 0)

m.c540 = Constraint(expr=m.x212**2 - m.x588 == 0)

m.c541 = Constraint(expr=   m.x47 - m.x588 == 0)

m.c542 = Constraint(expr=m.x212**3 - m.x589 == 0)

m.c543 = Constraint(expr=   m.x439 - m.x589 == 0)

m.c544 = Constraint(expr=m.x214**2 - m.x590 == 0)

m.c545 = Constraint(expr=   m.x52 - m.x590 == 0)

m.c546 = Constraint(expr=m.x214**3 - m.x591 == 0)

m.c547 = Constraint(expr=   m.x444 - m.x591 == 0)

m.c548 = Constraint(expr=m.x216**2 - m.x592 == 0)

m.c549 = Constraint(expr=   m.x55 - m.x592 == 0)

m.c550 = Constraint(expr=m.x216**3 - m.x593 == 0)

m.c551 = Constraint(expr=   m.x449 - m.x593 == 0)

m.c552 = Constraint(expr=m.x218**2 - m.x594 == 0)

m.c553 = Constraint(expr=   m.x60 - m.x594 == 0)

m.c554 = Constraint(expr=m.x218**3 - m.x595 == 0)

m.c555 = Constraint(expr=   m.x454 - m.x595 == 0)

m.c556 = Constraint(expr=m.x220**2 - m.x596 == 0)

m.c557 = Constraint(expr=   m.x63 - m.x596 == 0)

m.c558 = Constraint(expr=m.x220**3 - m.x597 == 0)

m.c559 = Constraint(expr=   m.x459 - m.x597 == 0)

m.c560 = Constraint(expr=m.x222**2 - m.x598 == 0)

m.c561 = Constraint(expr=   m.x66 - m.x598 == 0)

m.c562 = Constraint(expr=m.x222**3 - m.x599 == 0)

m.c563 = Constraint(expr=   m.x464 - m.x599 == 0)

m.c564 = Constraint(expr=m.x224**2 - m.x600 == 0)

m.c565 = Constraint(expr=   m.x69 - m.x600 == 0)

m.c566 = Constraint(expr=m.x224**3 - m.x601 == 0)

m.c567 = Constraint(expr=   m.x469 - m.x601 == 0)

m.c568 = Constraint(expr=m.x226**2 - m.x602 == 0)

m.c569 = Constraint(expr=   m.x72 - m.x602 == 0)

m.c570 = Constraint(expr=m.x226**3 - m.x603 == 0)

m.c571 = Constraint(expr=   m.x474 - m.x603 == 0)

m.c572 = Constraint(expr=m.x228**2 - m.x604 == 0)

m.c573 = Constraint(expr=   m.x75 - m.x604 == 0)

m.c574 = Constraint(expr=m.x228**3 - m.x605 == 0)

m.c575 = Constraint(expr=   m.x479 - m.x605 == 0)

m.c576 = Constraint(expr=m.x230**2 - m.x606 == 0)

m.c577 = Constraint(expr=   m.x81 - m.x606 == 0)

m.c578 = Constraint(expr=m.x230**3 - m.x607 == 0)

m.c579 = Constraint(expr=   m.x484 - m.x607 == 0)

m.c580 = Constraint(expr=m.x232**2 - m.x608 == 0)

m.c581 = Constraint(expr=   m.x84 - m.x608 == 0)

m.c582 = Constraint(expr=m.x232**3 - m.x609 == 0)

m.c583 = Constraint(expr=   m.x489 - m.x609 == 0)

m.c584 = Constraint(expr=m.x234**2 - m.x610 == 0)

m.c585 = Constraint(expr=   m.x88 - m.x610 == 0)

m.c586 = Constraint(expr=m.x234**3 - m.x611 == 0)

m.c587 = Constraint(expr=   m.x494 - m.x611 == 0)

m.c588 = Constraint(expr=m.x236**2 - m.x612 == 0)

m.c589 = Constraint(expr=   m.x91 - m.x612 == 0)

m.c590 = Constraint(expr=m.x236**3 - m.x613 == 0)

m.c591 = Constraint(expr=   m.x499 - m.x613 == 0)

m.c592 = Constraint(expr=m.x238**2 - m.x614 == 0)

m.c593 = Constraint(expr=   m.x94 - m.x614 == 0)

m.c594 = Constraint(expr=m.x238**3 - m.x615 == 0)

m.c595 = Constraint(expr=   m.x504 - m.x615 == 0)

m.c596 = Constraint(expr=m.x240**2 - m.x616 == 0)

m.c597 = Constraint(expr=   m.x96 - m.x616 == 0)

m.c598 = Constraint(expr=m.x240**3 - m.x617 == 0)

m.c599 = Constraint(expr=   m.x509 - m.x617 == 0)

m.c600 = Constraint(expr=m.x242**2 - m.x618 == 0)

m.c601 = Constraint(expr=   m.x100 - m.x618 == 0)

m.c602 = Constraint(expr=m.x242**3 - m.x619 == 0)

m.c603 = Constraint(expr=   m.x514 - m.x619 == 0)

m.c604 = Constraint(expr=m.x244**2 - m.x620 == 0)

m.c605 = Constraint(expr=   m.x105 - m.x620 == 0)

m.c606 = Constraint(expr=m.x244**3 - m.x621 == 0)

m.c607 = Constraint(expr=   m.x519 - m.x621 == 0)

m.c608 = Constraint(expr=m.x246**2 - m.x622 == 0)

m.c609 = Constraint(expr=   m.x109 - m.x622 == 0)

m.c610 = Constraint(expr=m.x246**3 - m.x623 == 0)

m.c611 = Constraint(expr=   m.x524 - m.x623 == 0)

m.c612 = Constraint(expr=m.x248**2 - m.x624 == 0)

m.c613 = Constraint(expr=   m.x111 - m.x624 == 0)

m.c614 = Constraint(expr=m.x248**3 - m.x625 == 0)

m.c615 = Constraint(expr=   m.x529 - m.x625 == 0)

m.c616 = Constraint(expr=m.x250**2 - m.x626 == 0)

m.c617 = Constraint(expr=   m.x116 - m.x626 == 0)

m.c618 = Constraint(expr=m.x250**3 - m.x627 == 0)

m.c619 = Constraint(expr=   m.x534 - m.x627 == 0)

m.c620 = Constraint(expr=m.x252**2 - m.x628 == 0)

m.c621 = Constraint(expr=   m.x118 - m.x628 == 0)

m.c622 = Constraint(expr=m.x252**3 - m.x629 == 0)

m.c623 = Constraint(expr=   m.x539 - m.x629 == 0)

m.c624 = Constraint(expr=m.x254**2 - m.x630 == 0)

m.c625 = Constraint(expr=   m.x122 - m.x630 == 0)

m.c626 = Constraint(expr=m.x254**3 - m.x631 == 0)

m.c627 = Constraint(expr=   m.x544 - m.x631 == 0)

m.c628 = Constraint(expr=m.x256**2 - m.x632 == 0)

m.c629 = Constraint(expr=   m.x125 - m.x632 == 0)

m.c630 = Constraint(expr=m.x256**3 - m.x633 == 0)

m.c631 = Constraint(expr=   m.x549 - m.x633 == 0)

m.c632 = Constraint(expr=m.x186*m.x350 - m.x191 == 0)

m.c633 = Constraint(expr=m.x350*m.x562 - m.x373 == 0)

m.c634 = Constraint(expr=m.x194*m.x350 - m.x221 == 0)

m.c635 = Constraint(expr=m.x350*m.x570 - m.x393 == 0)

m.c636 = Constraint(expr=m.x202*m.x350 - m.x247 == 0)

m.c637 = Constraint(expr=m.x350*m.x578 - m.x413 == 0)

m.c638 = Constraint(expr=m.x350**2 - m.x634 == 0)

m.c639 = Constraint(expr=   m.x193 - m.x634 == 0)

m.c640 = Constraint(expr=m.x186*m.x634 - m.x372 == 0)

m.c641 = Constraint(expr=m.x194*m.x634 - m.x392 == 0)

m.c642 = Constraint(expr=m.x202*m.x634 - m.x412 == 0)

m.c643 = Constraint(expr=m.x350**3 - m.x635 == 0)

m.c644 = Constraint(expr=m.b2*m.x635 - m.x371 == 0)

m.c645 = Constraint(expr=m.b6*m.x635 - m.x391 == 0)

m.c646 = Constraint(expr=m.b10*m.x635 - m.x411 == 0)

m.c647 = Constraint(expr=m.x188*m.x351 - m.x199 == 0)

m.c648 = Constraint(expr=m.x351*m.x564 - m.x378 == 0)

m.c649 = Constraint(expr=m.x196*m.x351 - m.x227 == 0)

m.c650 = Constraint(expr=m.x351*m.x572 - m.x398 == 0)

m.c651 = Constraint(expr=m.x204*m.x351 - m.x253 == 0)

m.c652 = Constraint(expr=m.x351*m.x580 - m.x418 == 0)

m.c653 = Constraint(expr=m.x351**2 - m.x636 == 0)

m.c654 = Constraint(expr=   m.x201 - m.x636 == 0)

m.c655 = Constraint(expr=m.x188*m.x636 - m.x377 == 0)

m.c656 = Constraint(expr=m.x196*m.x636 - m.x397 == 0)

m.c657 = Constraint(expr=m.x204*m.x636 - m.x417 == 0)

m.c658 = Constraint(expr=m.x351**3 - m.x637 == 0)

m.c659 = Constraint(expr=m.b3*m.x637 - m.x376 == 0)

m.c660 = Constraint(expr=m.b7*m.x637 - m.x396 == 0)

m.c661 = Constraint(expr=m.b11*m.x637 - m.x416 == 0)

m.c662 = Constraint(expr=m.x190*m.x352 - m.x207 == 0)

m.c663 = Constraint(expr=m.x352*m.x566 - m.x382 == 0)

m.c664 = Constraint(expr=m.x198*m.x352 - m.x233 == 0)

m.c665 = Constraint(expr=m.x352*m.x574 - m.x403 == 0)

m.c666 = Constraint(expr=m.x206*m.x352 - m.x257 == 0)

m.c667 = Constraint(expr=m.x352*m.x582 - m.x423 == 0)

m.c668 = Constraint(expr=m.x352**2 - m.x638 == 0)

m.c669 = Constraint(expr=   m.x209 - m.x638 == 0)

m.c670 = Constraint(expr=m.x190*m.x638 - m.x381 == 0)

m.c671 = Constraint(expr=m.x198*m.x638 - m.x402 == 0)

m.c672 = Constraint(expr=m.x206*m.x638 - m.x422 == 0)

m.c673 = Constraint(expr=m.x352**3 - m.x639 == 0)

m.c674 = Constraint(expr=m.b4*m.x639 - m.x380 == 0)

m.c675 = Constraint(expr=m.b8*m.x639 - m.x401 == 0)

m.c676 = Constraint(expr=m.b12*m.x639 - m.x421 == 0)

m.c677 = Constraint(expr=m.x192*m.x353 - m.x217 == 0)

m.c678 = Constraint(expr=m.x353*m.x568 - m.x387 == 0)

m.c679 = Constraint(expr=m.x200*m.x353 - m.x239 == 0)

m.c680 = Constraint(expr=m.x353*m.x576 - m.x406 == 0)

m.c681 = Constraint(expr=m.x208*m.x353 - m.x40 == 0)

m.c682 = Constraint(expr=m.x353*m.x584 - m.x428 == 0)

m.c683 = Constraint(expr=m.x353**2 - m.x640 == 0)

m.c684 = Constraint(expr=   m.x215 - m.x640 == 0)

m.c685 = Constraint(expr=m.x192*m.x640 - m.x386 == 0)

m.c686 = Constraint(expr=m.x200*m.x640 - m.x405 == 0)

m.c687 = Constraint(expr=m.x208*m.x640 - m.x427 == 0)

m.c688 = Constraint(expr=m.x353**3 - m.x641 == 0)

m.c689 = Constraint(expr=m.b5*m.x641 - m.x385 == 0)

m.c690 = Constraint(expr=m.b9*m.x641 - m.x408 == 0)

m.c691 = Constraint(expr=m.b13*m.x641 - m.x426 == 0)

m.c692 = Constraint(expr=m.x210*m.x354 - m.x44 == 0)

m.c693 = Constraint(expr=m.x354*m.x586 - m.x433 == 0)

m.c694 = Constraint(expr=m.x218*m.x354 - m.x59 == 0)

m.c695 = Constraint(expr=m.x354*m.x594 - m.x453 == 0)

m.c696 = Constraint(expr=m.x354**2 - m.x642 == 0)

m.c697 = Constraint(expr=   m.x43 - m.x642 == 0)

m.c698 = Constraint(expr=m.x210*m.x642 - m.x432 == 0)

m.c699 = Constraint(expr=m.x218*m.x642 - m.x452 == 0)

m.c700 = Constraint(expr=m.x354**3 - m.x643 == 0)

m.c701 = Constraint(expr=m.b14*m.x643 - m.x431 == 0)

m.c702 = Constraint(expr=m.b18*m.x643 - m.x451 == 0)

m.c703 = Constraint(expr=m.x212*m.x355 - m.x48 == 0)

m.c704 = Constraint(expr=m.x355*m.x588 - m.x438 == 0)

m.c705 = Constraint(expr=m.x220*m.x355 - m.x62 == 0)

m.c706 = Constraint(expr=m.x355*m.x596 - m.x458 == 0)

m.c707 = Constraint(expr=m.x355**2 - m.x644 == 0)

m.c708 = Constraint(expr=   m.x49 - m.x644 == 0)

m.c709 = Constraint(expr=m.x212*m.x644 - m.x437 == 0)

m.c710 = Constraint(expr=m.x220*m.x644 - m.x457 == 0)

m.c711 = Constraint(expr=m.x355**3 - m.x645 == 0)

m.c712 = Constraint(expr=m.b15*m.x645 - m.x436 == 0)

m.c713 = Constraint(expr=m.b19*m.x645 - m.x456 == 0)

m.c714 = Constraint(expr=m.x214*m.x356 - m.x51 == 0)

m.c715 = Constraint(expr=m.x356*m.x590 - m.x443 == 0)

m.c716 = Constraint(expr=m.x222*m.x356 - m.x65 == 0)

m.c717 = Constraint(expr=m.x356*m.x598 - m.x463 == 0)

m.c718 = Constraint(expr=m.x356**2 - m.x646 == 0)

m.c719 = Constraint(expr=   m.x53 - m.x646 == 0)

m.c720 = Constraint(expr=m.x214*m.x646 - m.x442 == 0)

m.c721 = Constraint(expr=m.x222*m.x646 - m.x462 == 0)

m.c722 = Constraint(expr=m.x356**3 - m.x647 == 0)

m.c723 = Constraint(expr=m.b16*m.x647 - m.x441 == 0)

m.c724 = Constraint(expr=m.b20*m.x647 - m.x461 == 0)

m.c725 = Constraint(expr=m.x216*m.x357 - m.x56 == 0)

m.c726 = Constraint(expr=m.x357*m.x592 - m.x448 == 0)

m.c727 = Constraint(expr=m.x224*m.x357 - m.x68 == 0)

m.c728 = Constraint(expr=m.x357*m.x600 - m.x468 == 0)

m.c729 = Constraint(expr=m.x357**2 - m.x648 == 0)

m.c730 = Constraint(expr=   m.x57 - m.x648 == 0)

m.c731 = Constraint(expr=m.x216*m.x648 - m.x447 == 0)

m.c732 = Constraint(expr=m.x224*m.x648 - m.x467 == 0)

m.c733 = Constraint(expr=m.x357**3 - m.x649 == 0)

m.c734 = Constraint(expr=m.b17*m.x649 - m.x446 == 0)

m.c735 = Constraint(expr=m.b21*m.x649 - m.x466 == 0)

m.c736 = Constraint(expr=m.x226*m.x358 - m.x71 == 0)

m.c737 = Constraint(expr=m.x358*m.x602 - m.x473 == 0)

m.c738 = Constraint(expr=m.x234*m.x358 - m.x87 == 0)

m.c739 = Constraint(expr=m.x358*m.x610 - m.x493 == 0)

m.c740 = Constraint(expr=m.x358**2 - m.x650 == 0)

m.c741 = Constraint(expr=   m.x73 - m.x650 == 0)

m.c742 = Constraint(expr=m.x226*m.x650 - m.x472 == 0)

m.c743 = Constraint(expr=m.x234*m.x650 - m.x492 == 0)

m.c744 = Constraint(expr=m.x358**3 - m.x651 == 0)

m.c745 = Constraint(expr=m.b22*m.x651 - m.x471 == 0)

m.c746 = Constraint(expr=m.b26*m.x651 - m.x491 == 0)

m.c747 = Constraint(expr=m.x228*m.x359 - m.x77 == 0)

m.c748 = Constraint(expr=m.x359*m.x604 - m.x478 == 0)

m.c749 = Constraint(expr=m.x236*m.x359 - m.x90 == 0)

m.c750 = Constraint(expr=m.x359*m.x612 - m.x498 == 0)

m.c751 = Constraint(expr=m.x359**2 - m.x652 == 0)

m.c752 = Constraint(expr=   m.x76 - m.x652 == 0)

m.c753 = Constraint(expr=m.x228*m.x652 - m.x477 == 0)

m.c754 = Constraint(expr=m.x236*m.x652 - m.x497 == 0)

m.c755 = Constraint(expr=m.x359**3 - m.x653 == 0)

m.c756 = Constraint(expr=m.b23*m.x653 - m.x476 == 0)

m.c757 = Constraint(expr=m.b27*m.x653 - m.x496 == 0)

m.c758 = Constraint(expr=m.x230*m.x360 - m.x79 == 0)

m.c759 = Constraint(expr=m.x360*m.x606 - m.x483 == 0)

m.c760 = Constraint(expr=m.x238*m.x360 - m.x93 == 0)

m.c761 = Constraint(expr=m.x360*m.x614 - m.x503 == 0)

m.c762 = Constraint(expr=m.x360**2 - m.x654 == 0)

m.c763 = Constraint(expr=   m.x80 - m.x654 == 0)

m.c764 = Constraint(expr=m.x230*m.x654 - m.x482 == 0)

m.c765 = Constraint(expr=m.x238*m.x654 - m.x502 == 0)

m.c766 = Constraint(expr=m.x360**3 - m.x655 == 0)

m.c767 = Constraint(expr=m.b24*m.x655 - m.x481 == 0)

m.c768 = Constraint(expr=m.b28*m.x655 - m.x501 == 0)

m.c769 = Constraint(expr=m.x232*m.x361 - m.x85 == 0)

m.c770 = Constraint(expr=m.x361*m.x608 - m.x488 == 0)

m.c771 = Constraint(expr=m.x240*m.x361 - m.x97 == 0)

m.c772 = Constraint(expr=m.x361*m.x616 - m.x508 == 0)

m.c773 = Constraint(expr=m.x361**2 - m.x656 == 0)

m.c774 = Constraint(expr=   m.x83 - m.x656 == 0)

m.c775 = Constraint(expr=m.x232*m.x656 - m.x487 == 0)

m.c776 = Constraint(expr=m.x240*m.x656 - m.x507 == 0)

m.c777 = Constraint(expr=m.x361**3 - m.x657 == 0)

m.c778 = Constraint(expr=m.b25*m.x657 - m.x486 == 0)

m.c779 = Constraint(expr=m.b29*m.x657 - m.x506 == 0)

m.c780 = Constraint(expr=m.x242*m.x362 - m.x101 == 0)

m.c781 = Constraint(expr=m.x362*m.x618 - m.x513 == 0)

m.c782 = Constraint(expr=m.x250*m.x362 - m.x115 == 0)

m.c783 = Constraint(expr=m.x362*m.x626 - m.x533 == 0)

m.c784 = Constraint(expr=m.x362**2 - m.x658 == 0)

m.c785 = Constraint(expr=   m.x99 - m.x658 == 0)

m.c786 = Constraint(expr=m.x242*m.x658 - m.x512 == 0)

m.c787 = Constraint(expr=m.x250*m.x658 - m.x532 == 0)

m.c788 = Constraint(expr=m.x362**3 - m.x659 == 0)

m.c789 = Constraint(expr=m.b30*m.x659 - m.x511 == 0)

m.c790 = Constraint(expr=m.b34*m.x659 - m.x531 == 0)

m.c791 = Constraint(expr=m.x244*m.x363 - m.x103 == 0)

m.c792 = Constraint(expr=m.x363*m.x620 - m.x518 == 0)

m.c793 = Constraint(expr=m.x252*m.x363 - m.x119 == 0)

m.c794 = Constraint(expr=m.x363*m.x628 - m.x538 == 0)

m.c795 = Constraint(expr=m.x363**2 - m.x660 == 0)

m.c796 = Constraint(expr=   m.x104 - m.x660 == 0)

m.c797 = Constraint(expr=m.x244*m.x660 - m.x517 == 0)

m.c798 = Constraint(expr=m.x252*m.x660 - m.x537 == 0)

m.c799 = Constraint(expr=m.x363**3 - m.x661 == 0)

m.c800 = Constraint(expr=m.b31*m.x661 - m.x516 == 0)

m.c801 = Constraint(expr=m.b35*m.x661 - m.x536 == 0)

m.c802 = Constraint(expr=m.x246*m.x364 - m.x108 == 0)

m.c803 = Constraint(expr=m.x364*m.x622 - m.x523 == 0)

m.c804 = Constraint(expr=m.x254*m.x364 - m.x121 == 0)

m.c805 = Constraint(expr=m.x364*m.x630 - m.x543 == 0)

m.c806 = Constraint(expr=m.x364**2 - m.x662 == 0)

m.c807 = Constraint(expr=   m.x107 - m.x662 == 0)

m.c808 = Constraint(expr=m.x246*m.x662 - m.x522 == 0)

m.c809 = Constraint(expr=m.x254*m.x662 - m.x542 == 0)

m.c810 = Constraint(expr=m.x364**3 - m.x663 == 0)

m.c811 = Constraint(expr=m.b32*m.x663 - m.x521 == 0)

m.c812 = Constraint(expr=m.b36*m.x663 - m.x541 == 0)

m.c813 = Constraint(expr=m.x248*m.x365 - m.x112 == 0)

m.c814 = Constraint(expr=m.x365*m.x624 - m.x528 == 0)

m.c815 = Constraint(expr=m.x256*m.x365 - m.x124 == 0)

m.c816 = Constraint(expr=m.x365*m.x632 - m.x548 == 0)

m.c817 = Constraint(expr=m.x365**2 - m.x664 == 0)

m.c818 = Constraint(expr=   m.x113 - m.x664 == 0)

m.c819 = Constraint(expr=m.x248*m.x664 - m.x527 == 0)

m.c820 = Constraint(expr=m.x256*m.x664 - m.x547 == 0)

m.c821 = Constraint(expr=m.x365**3 - m.x665 == 0)

m.c822 = Constraint(expr=m.b33*m.x665 - m.x526 == 0)

m.c823 = Constraint(expr=m.b37*m.x665 - m.x546 == 0)
