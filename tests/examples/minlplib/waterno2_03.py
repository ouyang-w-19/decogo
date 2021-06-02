#  MINLP written by GAMS Convert at 04/21/18 13:55:18
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        617      367      103      147        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        499      472       27        0        0        0        0        0
#  FX      6        6        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1636     1333      303        0
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
m.x29 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x30 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x33 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x37 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x41 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x45 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x48 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x51 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x54 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x58 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x62 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x66 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x71 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
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
m.x95 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,1.16),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,1.16),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,1.16),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x122 = Var(within=Reals,bounds=(3.5,3.5),initialize=3.5)
m.x123 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x124 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x125 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x126 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x127 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x128 = Var(within=Reals,bounds=(4.1,4.1),initialize=4.1)
m.x129 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x130 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x131 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x132 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x133 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x134 = Var(within=Reals,bounds=(4,4),initialize=4)
m.x135 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x136 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x137 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x138 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x139 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x140 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x141 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x143 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x145 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x147 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x149 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x151 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x153 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x155 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x157 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x159 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x161 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x163 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x165 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x167 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x169 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x171 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x173 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x175 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x177 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x179 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x181 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x183 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x185 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x187 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x189 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x191 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x193 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x194 = Var(within=Reals,bounds=(62,65),initialize=62)
m.x195 = Var(within=Reals,bounds=(62,65),initialize=62)
m.x196 = Var(within=Reals,bounds=(62,65),initialize=62)
m.x197 = Var(within=Reals,bounds=(92.5,95),initialize=92.5)
m.x198 = Var(within=Reals,bounds=(92.5,95),initialize=92.5)
m.x199 = Var(within=Reals,bounds=(92.5,95),initialize=92.5)
m.x200 = Var(within=Reals,bounds=(105,109),initialize=105)
m.x201 = Var(within=Reals,bounds=(105,109),initialize=105)
m.x202 = Var(within=Reals,bounds=(105,109),initialize=105)
m.x203 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x204 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x206 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x208 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x211 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x214 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x217 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x219 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x221 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x223 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x224 = Var(within=Reals,bounds=(49,49),initialize=49)
m.x225 = Var(within=Reals,bounds=(-49,1000),initialize=0)
m.x226 = Var(within=Reals,bounds=(49,49),initialize=49)
m.x227 = Var(within=Reals,bounds=(-49,1000),initialize=0)
m.x228 = Var(within=Reals,bounds=(49,49),initialize=49)
m.x229 = Var(within=Reals,bounds=(-49,1000),initialize=0)
m.x230 = Var(within=Reals,bounds=(-65,1000),initialize=0)
m.x231 = Var(within=Reals,bounds=(-65,1000),initialize=0)
m.x232 = Var(within=Reals,bounds=(-65,1000),initialize=0)
m.x233 = Var(within=Reals,bounds=(-95,1000),initialize=0)
m.x234 = Var(within=Reals,bounds=(-95,1000),initialize=0)
m.x235 = Var(within=Reals,bounds=(-95,1000),initialize=0)
m.x236 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x237 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x238 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x239 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x240 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x241 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x242 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x243 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x244 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x245 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x246 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x247 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x248 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x249 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x250 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x251 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x252 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x253 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x254 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x255 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x256 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x257 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x258 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x259 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x260 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x261 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x262 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x263 = Var(within=Reals,bounds=(0.6,1),initialize=0.6)
m.x264 = Var(within=Reals,bounds=(0.6,1),initialize=0.6)
m.x265 = Var(within=Reals,bounds=(0.6,1),initialize=0.6)
m.x266 = Var(within=Reals,bounds=(0.8,1),initialize=0.8)
m.x267 = Var(within=Reals,bounds=(0.8,1),initialize=0.8)
m.x268 = Var(within=Reals,bounds=(0.8,1),initialize=0.8)
m.x269 = Var(within=Reals,bounds=(0.85,1),initialize=0.85)
m.x270 = Var(within=Reals,bounds=(0.85,1),initialize=0.85)
m.x271 = Var(within=Reals,bounds=(0.85,1),initialize=0.85)
m.x272 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x273 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x274 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x275 = Var(within=Reals,bounds=(100,1000),initialize=100)
m.x276 = Var(within=Reals,bounds=(100,1000),initialize=100)
m.x277 = Var(within=Reals,bounds=(100,1000),initialize=100)
m.x278 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x279 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x280 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x281 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x282 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x283 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x284 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x285 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x286 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x287 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x289 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x290 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x291 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x292 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x293 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x294 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x295 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x296 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x297 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x298 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x299 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x300 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x301 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x302 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x303 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x304 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x305 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x306 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x307 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x309 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x310 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x311 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x312 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x313 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x314 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x315 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x316 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x317 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x318 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x319 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x320 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x321 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x322 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x323 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x324 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x325 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x326 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x327 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x328 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x329 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x330 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x331 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x332 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x333 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x334 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x335 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x336 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x337 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x338 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x339 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x340 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x341 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x342 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x343 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x344 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x345 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x346 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x347 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x348 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x349 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x350 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x351 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x352 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x353 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x354 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x355 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x356 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x357 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x358 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x359 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x360 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x361 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x362 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x363 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x364 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x365 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x366 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x367 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x368 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x369 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x370 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x371 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x372 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x373 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x374 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x375 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x376 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x377 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x378 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x379 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x380 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x381 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x382 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x383 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x384 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x385 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x386 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x387 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x388 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x389 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x390 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x391 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x392 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x393 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x394 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x395 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x396 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x397 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x398 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x399 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x400 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x401 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x402 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x403 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x404 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x405 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x406 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x407 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x408 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x409 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x410 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x411 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x412 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x413 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x414 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x415 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x416 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x417 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x418 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x419 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x420 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x421 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x422 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x423 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x424 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x425 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x426 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x427 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x428 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x429 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x430 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x431 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x432 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x433 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x434 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x435 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x436 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x437 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x438 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x439 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x440 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x441 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x442 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x443 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x444 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x445 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x446 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x447 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x448 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x449 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x450 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x451 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x452 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x453 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x454 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x455 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x456 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x457 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x458 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x459 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x460 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x461 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x462 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x463 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x464 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x465 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x466 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x467 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x468 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x469 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x470 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x471 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x472 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x473 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x474 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x475 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x476 = Var(within=Reals,bounds=(0.36,1),initialize=0.36)
m.x477 = Var(within=Reals,bounds=(0.216,1),initialize=0.216)
m.x478 = Var(within=Reals,bounds=(0.36,1),initialize=0.36)
m.x479 = Var(within=Reals,bounds=(0.216,1),initialize=0.216)
m.x480 = Var(within=Reals,bounds=(0.36,1),initialize=0.36)
m.x481 = Var(within=Reals,bounds=(0.216,1),initialize=0.216)
m.x482 = Var(within=Reals,bounds=(0.64,1),initialize=0.64)
m.x483 = Var(within=Reals,bounds=(0.512,1),initialize=0.512)
m.x484 = Var(within=Reals,bounds=(0.64,1),initialize=0.64)
m.x485 = Var(within=Reals,bounds=(0.512,1),initialize=0.512)
m.x486 = Var(within=Reals,bounds=(0.64,1),initialize=0.64)
m.x487 = Var(within=Reals,bounds=(0.512,1),initialize=0.512)
m.x488 = Var(within=Reals,bounds=(0.7225,1),initialize=0.7225)
m.x489 = Var(within=Reals,bounds=(0.614125,1),initialize=0.614125)
m.x490 = Var(within=Reals,bounds=(0.7225,1),initialize=0.7225)
m.x491 = Var(within=Reals,bounds=(0.614125,1),initialize=0.614125)
m.x492 = Var(within=Reals,bounds=(0.7225,1),initialize=0.7225)
m.x493 = Var(within=Reals,bounds=(0.614125,1),initialize=0.614125)
m.x494 = Var(within=Reals,bounds=(0.49,1),initialize=0.49)
m.x495 = Var(within=Reals,bounds=(0.343,1),initialize=0.343)
m.x496 = Var(within=Reals,bounds=(0.49,1),initialize=0.49)
m.x497 = Var(within=Reals,bounds=(0.343,1),initialize=0.343)
m.x498 = Var(within=Reals,bounds=(0.49,1),initialize=0.49)
m.x499 = Var(within=Reals,bounds=(0.343,1),initialize=0.343)

m.obj = Objective(expr=   m.x278 + m.x283 + m.x288 + m.x293 + m.x298 + m.x303 + m.x308 + m.x313 + m.x318 + m.x323
                        + m.x328 + m.x333 + m.x338 + m.x345 + m.x348 + m.x353 + m.x358 + m.x363 + m.x368 + m.x373
                        + m.x378 + m.x383 + m.x388 + m.x393 + m.x398 + m.x403 + m.x408, sense=minimize)

m.c2 = Constraint(expr=   m.x141 + 27.42831624*m.x143 + 37.5407324*m.x145 - 57.2814121*m.x147 == 0)

m.c3 = Constraint(expr=   m.x149 + 27.42831624*m.x151 - 57.2814121*m.x153 + 37.5407324*m.x155 == 0)

m.c4 = Constraint(expr=   m.x157 + 27.42831624*m.x159 - 57.2814121*m.x161 + 37.5407324*m.x163 == 0)

m.c5 = Constraint(expr= - 57.2814121*m.x147 + m.x165 + 27.42831624*m.x167 + 37.5407324*m.x169 == 0)

m.c6 = Constraint(expr= - 57.2814121*m.x153 + m.x171 + 37.5407324*m.x173 + 27.42831624*m.x175 == 0)

m.c7 = Constraint(expr= - 57.2814121*m.x161 + m.x177 + 37.5407324*m.x179 + 27.42831624*m.x181 == 0)

m.c8 = Constraint(expr= - 57.2814121*m.x147 + m.x183 + 37.5407324*m.x185 + 27.42831624*m.x187 == 0)

m.c9 = Constraint(expr= - 57.2814121*m.x153 + m.x189 + 27.42831624*m.x191 + 37.5407324*m.x193 == 0)

m.c10 = Constraint(expr=   m.x29 + 27.42831624*m.x30 + 37.5407324*m.x31 - 57.2814121*m.x161 == 0)

m.c11 = Constraint(expr=   m.x32 - 76.45219958*m.x33 + 43.14087708*m.x34 + 50.37356589*m.x35 == 0)

m.c12 = Constraint(expr=   m.x36 + 50.37356589*m.x37 - 76.45219958*m.x38 + 43.14087708*m.x39 == 0)

m.c13 = Constraint(expr=   m.x40 + 43.14087708*m.x41 + 50.37356589*m.x42 - 76.45219958*m.x43 == 0)

m.c14 = Constraint(expr= - 76.45219958*m.x33 + m.x44 + 43.14087708*m.x45 + 50.37356589*m.x46 == 0)

m.c15 = Constraint(expr= - 76.45219958*m.x38 + m.x47 + 50.37356589*m.x48 + 43.14087708*m.x49 == 0)

m.c16 = Constraint(expr= - 76.45219958*m.x43 + m.x50 + 43.14087708*m.x51 + 50.37356589*m.x52 == 0)

m.c17 = Constraint(expr=   m.x53 + 58.31011875*m.x54 - 69.39622571*m.x55 - 25.39911174*m.x56 == 0)

m.c18 = Constraint(expr=   m.x57 - 25.39911174*m.x58 + 58.31011875*m.x59 - 69.39622571*m.x60 == 0)

m.c19 = Constraint(expr=   m.x61 - 69.39622571*m.x62 + 58.31011875*m.x63 - 25.39911174*m.x64 == 0)

m.c20 = Constraint(expr= - 69.39622571*m.x55 + m.x65 + 58.31011875*m.x66 - 25.39911174*m.x67 == 0)

m.c21 = Constraint(expr= - 69.39622571*m.x60 + m.x68 - 25.39911174*m.x69 + 58.31011875*m.x70 == 0)

m.c22 = Constraint(expr= - 69.39622571*m.x62 + m.x71 + 58.31011875*m.x72 - 25.39911174*m.x73 == 0)

m.c23 = Constraint(expr=   m.x74 - 2.03724124*m.x75 + 63.61644904*m.x76 - 34.92732674*m.x77 == 0)

m.c24 = Constraint(expr=   m.x78 - 2.03724124*m.x79 - 34.92732674*m.x80 + 63.61644904*m.x81 == 0)

m.c25 = Constraint(expr=   m.x82 - 2.03724124*m.x83 - 34.92732674*m.x84 + 63.61644904*m.x85 == 0)

m.c26 = Constraint(expr= - 34.92732674*m.x77 + m.x86 + 63.61644904*m.x87 - 2.03724124*m.x88 == 0)

m.c27 = Constraint(expr= - 34.92732674*m.x80 + m.x89 + 63.61644904*m.x90 - 2.03724124*m.x91 == 0)

m.c28 = Constraint(expr= - 34.92732674*m.x84 + m.x92 - 2.03724124*m.x93 + 63.61644904*m.x94 == 0)

m.c29 = Constraint(expr=   m.x95 + m.x96 + m.x97 >= 0.875)

m.c30 = Constraint(expr= - m.x98 + m.x99 == 0)

m.c31 = Constraint(expr= - m.x100 + m.x101 == 0)

m.c32 = Constraint(expr= - m.x102 + m.x103 == 0)

m.c33 = Constraint(expr= - m.x104 + m.x105 == 0)

m.c34 = Constraint(expr= - m.x106 + m.x107 == 0)

m.c35 = Constraint(expr= - m.x108 + m.x109 == 0)

m.c36 = Constraint(expr=   m.x104 - m.x110 == 0)

m.c37 = Constraint(expr=   m.x106 - m.x111 == 0)

m.c38 = Constraint(expr=   m.x108 - m.x112 == 0)

m.c39 = Constraint(expr= - m.x113 + m.x114 == 0)

m.c40 = Constraint(expr= - m.x115 + m.x116 == 0)

m.c41 = Constraint(expr= - m.x117 + m.x118 == 0)

m.c42 = Constraint(expr=   m.x119 == 0.296666667)

m.c43 = Constraint(expr=   m.x120 == 0.294444444)

m.c44 = Constraint(expr=   m.x121 == 0.283888889)

m.c45 = Constraint(expr=   m.x95 - m.x99 == 0)

m.c46 = Constraint(expr=   m.x96 - m.x101 == 0)

m.c47 = Constraint(expr=   m.x97 - m.x103 == 0)

m.c48 = Constraint(expr=   3600*m.x98 - 3600*m.x105 + 1800*m.x122 - 1800*m.x123 == 0)

m.c49 = Constraint(expr=   3600*m.x100 - 3600*m.x107 + 1800*m.x124 - 1800*m.x125 == 0)

m.c50 = Constraint(expr=   3600*m.x102 - 3600*m.x109 + 1800*m.x126 - 1800*m.x127 == 0)

m.c51 = Constraint(expr=   3600*m.x110 - 3600*m.x114 + 720*m.x128 - 720*m.x129 == 0)

m.c52 = Constraint(expr=   3600*m.x111 - 3600*m.x116 + 720*m.x130 - 720*m.x131 == 0)

m.c53 = Constraint(expr=   3600*m.x112 - 3600*m.x118 + 720*m.x132 - 720*m.x133 == 0)

m.c54 = Constraint(expr=   3600*m.x113 - 3600*m.x119 + 1600*m.x134 - 1600*m.x135 == 0)

m.c55 = Constraint(expr=   3600*m.x115 - 3600*m.x120 + 1600*m.x136 - 1600*m.x137 == 0)

m.c56 = Constraint(expr=   3600*m.x117 - 3600*m.x121 + 1600*m.x138 - 1600*m.x139 == 0)

m.c57 = Constraint(expr= - m.x123 + m.x124 == 0)

m.c58 = Constraint(expr= - m.x125 + m.x126 == 0)

m.c59 = Constraint(expr= - m.x129 + m.x130 == 0)

m.c60 = Constraint(expr= - m.x131 + m.x132 == 0)

m.c61 = Constraint(expr= - m.x135 + m.x136 == 0)

m.c62 = Constraint(expr= - m.x137 + m.x138 == 0)

m.c63 = Constraint(expr= - 0.2*m.b2 + m.x140 >= 0)

m.c64 = Constraint(expr= - 0.2*m.b3 + m.x142 >= 0)

m.c65 = Constraint(expr= - 0.2*m.b4 + m.x144 >= 0)

m.c66 = Constraint(expr= - 0.2*m.b5 + m.x146 >= 0)

m.c67 = Constraint(expr= - 0.2*m.b6 + m.x148 >= 0)

m.c68 = Constraint(expr= - 0.2*m.b7 + m.x150 >= 0)

m.c69 = Constraint(expr= - 0.2*m.b8 + m.x152 >= 0)

m.c70 = Constraint(expr= - 0.2*m.b9 + m.x154 >= 0)

m.c71 = Constraint(expr= - 0.2*m.b10 + m.x156 >= 0)

m.c72 = Constraint(expr= - 0.25*m.b11 + m.x158 >= 0)

m.c73 = Constraint(expr= - 0.25*m.b12 + m.x160 >= 0)

m.c74 = Constraint(expr= - 0.25*m.b13 + m.x162 >= 0)

m.c75 = Constraint(expr= - 0.25*m.b14 + m.x164 >= 0)

m.c76 = Constraint(expr= - 0.25*m.b15 + m.x166 >= 0)

m.c77 = Constraint(expr= - 0.25*m.b16 + m.x168 >= 0)

m.c78 = Constraint(expr= - 0.4*m.b17 + m.x170 >= 0)

m.c79 = Constraint(expr= - 0.4*m.b18 + m.x172 >= 0)

m.c80 = Constraint(expr= - 0.4*m.b19 + m.x174 >= 0)

m.c81 = Constraint(expr= - 0.4*m.b20 + m.x176 >= 0)

m.c82 = Constraint(expr= - 0.4*m.b21 + m.x178 >= 0)

m.c83 = Constraint(expr= - 0.4*m.b22 + m.x180 >= 0)

m.c84 = Constraint(expr= - 0.24*m.b23 + m.x182 >= 0)

m.c85 = Constraint(expr= - 0.24*m.b24 + m.x184 >= 0)

m.c86 = Constraint(expr= - 0.24*m.b25 + m.x186 >= 0)

m.c87 = Constraint(expr= - 0.24*m.b26 + m.x188 >= 0)

m.c88 = Constraint(expr= - 0.24*m.b27 + m.x190 >= 0)

m.c89 = Constraint(expr= - 0.24*m.b28 + m.x192 >= 0)

m.c90 = Constraint(expr= - 0.8*m.b2 + m.x140 <= 0)

m.c91 = Constraint(expr= - 0.8*m.b3 + m.x142 <= 0)

m.c92 = Constraint(expr= - 0.8*m.b4 + m.x144 <= 0)

m.c93 = Constraint(expr= - 0.8*m.b5 + m.x146 <= 0)

m.c94 = Constraint(expr= - 0.8*m.b6 + m.x148 <= 0)

m.c95 = Constraint(expr= - 0.8*m.b7 + m.x150 <= 0)

m.c96 = Constraint(expr= - 0.8*m.b8 + m.x152 <= 0)

m.c97 = Constraint(expr= - 0.8*m.b9 + m.x154 <= 0)

m.c98 = Constraint(expr= - 0.8*m.b10 + m.x156 <= 0)

m.c99 = Constraint(expr= - 0.5*m.b11 + m.x158 <= 0)

m.c100 = Constraint(expr= - 0.5*m.b12 + m.x160 <= 0)

m.c101 = Constraint(expr= - 0.5*m.b13 + m.x162 <= 0)

m.c102 = Constraint(expr= - 0.5*m.b14 + m.x164 <= 0)

m.c103 = Constraint(expr= - 0.5*m.b15 + m.x166 <= 0)

m.c104 = Constraint(expr= - 0.5*m.b16 + m.x168 <= 0)

m.c105 = Constraint(expr= - 0.7*m.b17 + m.x170 <= 0)

m.c106 = Constraint(expr= - 0.7*m.b18 + m.x172 <= 0)

m.c107 = Constraint(expr= - 0.7*m.b19 + m.x174 <= 0)

m.c108 = Constraint(expr= - 0.7*m.b20 + m.x176 <= 0)

m.c109 = Constraint(expr= - 0.7*m.b21 + m.x178 <= 0)

m.c110 = Constraint(expr= - 0.7*m.b22 + m.x180 <= 0)

m.c111 = Constraint(expr= - 0.58*m.b23 + m.x182 <= 0)

m.c112 = Constraint(expr= - 0.58*m.b24 + m.x184 <= 0)

m.c113 = Constraint(expr= - 0.58*m.b25 + m.x186 <= 0)

m.c114 = Constraint(expr= - 0.58*m.b26 + m.x188 <= 0)

m.c115 = Constraint(expr= - 0.58*m.b27 + m.x190 <= 0)

m.c116 = Constraint(expr= - 0.58*m.b28 + m.x192 <= 0)

m.c117 = Constraint(expr= - m.x122 + m.x194 == 60)

m.c118 = Constraint(expr= - m.x124 + m.x195 == 60)

m.c119 = Constraint(expr= - m.x126 + m.x196 == 60)

m.c120 = Constraint(expr= - m.x128 + m.x197 == 90)

m.c121 = Constraint(expr= - m.x130 + m.x198 == 90)

m.c122 = Constraint(expr= - m.x132 + m.x199 == 90)

m.c123 = Constraint(expr= - m.x134 + m.x200 == 103)

m.c124 = Constraint(expr= - m.x136 + m.x201 == 103)

m.c125 = Constraint(expr= - m.x138 + m.x202 == 103)

m.c126 = Constraint(expr= - m.x194 + m.x203 - m.x204 == 0)

m.c127 = Constraint(expr= - m.x195 + m.x205 - m.x206 == 0)

m.c128 = Constraint(expr= - m.x196 + m.x207 - m.x208 == 0)

m.c129 = Constraint(expr=   m.x209 - m.x210 - m.x211 == 0)

m.c130 = Constraint(expr=   m.x212 - m.x213 - m.x214 == 0)

m.c131 = Constraint(expr=   m.x215 - m.x216 - m.x217 == 0)

m.c132 = Constraint(expr= - m.x200 + m.x218 - m.x219 == 0)

m.c133 = Constraint(expr= - m.x201 + m.x220 - m.x221 == 0)

m.c134 = Constraint(expr= - m.x202 + m.x222 - m.x223 == 0)

m.c135 = Constraint(expr=   m.x203 - m.x224 - m.x225 == 0)

m.c136 = Constraint(expr=   m.x205 - m.x226 - m.x227 == 0)

m.c137 = Constraint(expr=   m.x207 - m.x228 - m.x229 == 0)

m.c138 = Constraint(expr= - m.x194 + m.x209 - m.x230 == 0)

m.c139 = Constraint(expr= - m.x195 + m.x212 - m.x231 == 0)

m.c140 = Constraint(expr= - m.x196 + m.x215 - m.x232 == 0)

m.c141 = Constraint(expr= - m.x197 + m.x218 - m.x233 == 0)

m.c142 = Constraint(expr= - m.x198 + m.x220 - m.x234 == 0)

m.c143 = Constraint(expr= - m.x199 + m.x222 - m.x235 == 0)

m.c144 = Constraint(expr=   0.2*m.b2 - m.x140 + m.x236 <= 0.2)

m.c145 = Constraint(expr=   0.2*m.b3 - m.x142 + m.x237 <= 0.2)

m.c146 = Constraint(expr=   0.2*m.b4 - m.x144 + m.x238 <= 0.2)

m.c147 = Constraint(expr=   0.2*m.b5 - m.x146 + m.x239 <= 0.2)

m.c148 = Constraint(expr=   0.2*m.b6 - m.x148 + m.x240 <= 0.2)

m.c149 = Constraint(expr=   0.2*m.b7 - m.x150 + m.x241 <= 0.2)

m.c150 = Constraint(expr=   0.2*m.b8 - m.x152 + m.x242 <= 0.2)

m.c151 = Constraint(expr=   0.2*m.b9 - m.x154 + m.x243 <= 0.2)

m.c152 = Constraint(expr=   0.2*m.b10 - m.x156 + m.x244 <= 0.2)

m.c153 = Constraint(expr=   0.25*m.b11 - m.x158 + m.x245 <= 0.25)

m.c154 = Constraint(expr=   0.25*m.b12 - m.x160 + m.x246 <= 0.25)

m.c155 = Constraint(expr=   0.25*m.b13 - m.x162 + m.x247 <= 0.25)

m.c156 = Constraint(expr=   0.25*m.b14 - m.x164 + m.x248 <= 0.25)

m.c157 = Constraint(expr=   0.25*m.b15 - m.x166 + m.x249 <= 0.25)

m.c158 = Constraint(expr=   0.25*m.b16 - m.x168 + m.x250 <= 0.25)

m.c159 = Constraint(expr=   0.4*m.b17 - m.x170 + m.x251 <= 0.4)

m.c160 = Constraint(expr=   0.4*m.b18 - m.x172 + m.x252 <= 0.4)

m.c161 = Constraint(expr=   0.4*m.b19 - m.x174 + m.x253 <= 0.4)

m.c162 = Constraint(expr=   0.4*m.b20 - m.x176 + m.x254 <= 0.4)

m.c163 = Constraint(expr=   0.4*m.b21 - m.x178 + m.x255 <= 0.4)

m.c164 = Constraint(expr=   0.4*m.b22 - m.x180 + m.x256 <= 0.4)

m.c165 = Constraint(expr=   0.24*m.b23 - m.x182 + m.x257 <= 0.24)

m.c166 = Constraint(expr=   0.24*m.b24 - m.x184 + m.x258 <= 0.24)

m.c167 = Constraint(expr=   0.24*m.b25 - m.x186 + m.x259 <= 0.24)

m.c168 = Constraint(expr=   0.24*m.b26 - m.x188 + m.x260 <= 0.24)

m.c169 = Constraint(expr=   0.24*m.b27 - m.x190 + m.x261 <= 0.24)

m.c170 = Constraint(expr=   0.24*m.b28 - m.x192 + m.x262 <= 0.24)

m.c171 = Constraint(expr= - m.x140 + m.x236 >= 0)

m.c172 = Constraint(expr= - m.x142 + m.x237 >= 0)

m.c173 = Constraint(expr= - m.x144 + m.x238 >= 0)

m.c174 = Constraint(expr= - m.x146 + m.x239 >= 0)

m.c175 = Constraint(expr= - m.x148 + m.x240 >= 0)

m.c176 = Constraint(expr= - m.x150 + m.x241 >= 0)

m.c177 = Constraint(expr= - m.x152 + m.x242 >= 0)

m.c178 = Constraint(expr= - m.x154 + m.x243 >= 0)

m.c179 = Constraint(expr= - m.x156 + m.x244 >= 0)

m.c180 = Constraint(expr= - m.x158 + m.x245 >= 0)

m.c181 = Constraint(expr= - m.x160 + m.x246 >= 0)

m.c182 = Constraint(expr= - m.x162 + m.x247 >= 0)

m.c183 = Constraint(expr= - m.x164 + m.x248 >= 0)

m.c184 = Constraint(expr= - m.x166 + m.x249 >= 0)

m.c185 = Constraint(expr= - m.x168 + m.x250 >= 0)

m.c186 = Constraint(expr= - m.x170 + m.x251 >= 0)

m.c187 = Constraint(expr= - m.x172 + m.x252 >= 0)

m.c188 = Constraint(expr= - m.x174 + m.x253 >= 0)

m.c189 = Constraint(expr= - m.x176 + m.x254 >= 0)

m.c190 = Constraint(expr= - m.x178 + m.x255 >= 0)

m.c191 = Constraint(expr= - m.x180 + m.x256 >= 0)

m.c192 = Constraint(expr= - m.x182 + m.x257 >= 0)

m.c193 = Constraint(expr= - m.x184 + m.x258 >= 0)

m.c194 = Constraint(expr= - m.x186 + m.x259 >= 0)

m.c195 = Constraint(expr= - m.x188 + m.x260 >= 0)

m.c196 = Constraint(expr= - m.x190 + m.x261 >= 0)

m.c197 = Constraint(expr= - m.x192 + m.x262 >= 0)

m.c198 = Constraint(expr= - 0.6*m.b2 + m.x236 <= 0.2)

m.c199 = Constraint(expr= - 0.6*m.b3 + m.x237 <= 0.2)

m.c200 = Constraint(expr= - 0.6*m.b4 + m.x238 <= 0.2)

m.c201 = Constraint(expr= - 0.6*m.b5 + m.x239 <= 0.2)

m.c202 = Constraint(expr= - 0.6*m.b6 + m.x240 <= 0.2)

m.c203 = Constraint(expr= - 0.6*m.b7 + m.x241 <= 0.2)

m.c204 = Constraint(expr= - 0.6*m.b8 + m.x242 <= 0.2)

m.c205 = Constraint(expr= - 0.6*m.b9 + m.x243 <= 0.2)

m.c206 = Constraint(expr= - 0.6*m.b10 + m.x244 <= 0.2)

m.c207 = Constraint(expr= - 0.25*m.b11 + m.x245 <= 0.25)

m.c208 = Constraint(expr= - 0.25*m.b12 + m.x246 <= 0.25)

m.c209 = Constraint(expr= - 0.25*m.b13 + m.x247 <= 0.25)

m.c210 = Constraint(expr= - 0.25*m.b14 + m.x248 <= 0.25)

m.c211 = Constraint(expr= - 0.25*m.b15 + m.x249 <= 0.25)

m.c212 = Constraint(expr= - 0.25*m.b16 + m.x250 <= 0.25)

m.c213 = Constraint(expr= - 0.3*m.b17 + m.x251 <= 0.4)

m.c214 = Constraint(expr= - 0.3*m.b18 + m.x252 <= 0.4)

m.c215 = Constraint(expr= - 0.3*m.b19 + m.x253 <= 0.4)

m.c216 = Constraint(expr= - 0.3*m.b20 + m.x254 <= 0.4)

m.c217 = Constraint(expr= - 0.3*m.b21 + m.x255 <= 0.4)

m.c218 = Constraint(expr= - 0.3*m.b22 + m.x256 <= 0.4)

m.c219 = Constraint(expr= - 0.34*m.b23 + m.x257 <= 0.24)

m.c220 = Constraint(expr= - 0.34*m.b24 + m.x258 <= 0.24)

m.c221 = Constraint(expr= - 0.34*m.b25 + m.x259 <= 0.24)

m.c222 = Constraint(expr= - 0.34*m.b26 + m.x260 <= 0.24)

m.c223 = Constraint(expr= - 0.34*m.b27 + m.x261 <= 0.24)

m.c224 = Constraint(expr= - 0.34*m.b28 + m.x262 <= 0.24)

m.c225 = Constraint(expr= - 0.4*m.b2 + m.x263 <= 0.6)

m.c226 = Constraint(expr= - 0.4*m.b3 + m.x264 <= 0.6)

m.c227 = Constraint(expr= - 0.4*m.b4 + m.x265 <= 0.6)

m.c228 = Constraint(expr= - 0.2*m.b11 + m.x266 <= 0.8)

m.c229 = Constraint(expr= - 0.2*m.b12 + m.x267 <= 0.8)

m.c230 = Constraint(expr= - 0.2*m.b13 + m.x268 <= 0.8)

m.c231 = Constraint(expr= - 0.15*m.b17 + m.x269 <= 0.85)

m.c232 = Constraint(expr= - 0.15*m.b18 + m.x270 <= 0.85)

m.c233 = Constraint(expr= - 0.15*m.b19 + m.x271 <= 0.85)

m.c234 = Constraint(expr= - 0.3*m.b23 + m.x272 <= 0.7)

m.c235 = Constraint(expr= - 0.3*m.b24 + m.x273 <= 0.7)

m.c236 = Constraint(expr= - 0.3*m.b25 + m.x274 <= 0.7)

m.c237 = Constraint(expr=   m.b2 - m.b5 >= 0)

m.c238 = Constraint(expr=   m.b3 - m.b6 >= 0)

m.c239 = Constraint(expr=   m.b4 - m.b7 >= 0)

m.c240 = Constraint(expr=   m.b5 - m.b8 >= 0)

m.c241 = Constraint(expr=   m.b6 - m.b9 >= 0)

m.c242 = Constraint(expr=   m.b7 - m.b10 >= 0)

m.c243 = Constraint(expr=   m.b11 - m.b14 >= 0)

m.c244 = Constraint(expr=   m.b12 - m.b15 >= 0)

m.c245 = Constraint(expr=   m.b13 - m.b16 >= 0)

m.c246 = Constraint(expr=   m.b17 - m.b20 >= 0)

m.c247 = Constraint(expr=   m.b18 - m.b21 >= 0)

m.c248 = Constraint(expr=   m.b19 - m.b22 >= 0)

m.c249 = Constraint(expr=   m.b23 - m.b26 >= 0)

m.c250 = Constraint(expr=   m.b24 - m.b27 >= 0)

m.c251 = Constraint(expr=   m.b25 - m.b28 >= 0)

m.c252 = Constraint(expr=   m.x99 - m.x140 - m.x146 - m.x152 == 0)

m.c253 = Constraint(expr=   m.x101 - m.x142 - m.x148 - m.x154 == 0)

m.c254 = Constraint(expr=   m.x103 - m.x144 - m.x150 - m.x156 == 0)

m.c255 = Constraint(expr=   m.x105 - m.x158 - m.x164 - m.x170 - m.x176 == 0)

m.c256 = Constraint(expr=   m.x107 - m.x160 - m.x166 - m.x172 - m.x178 == 0)

m.c257 = Constraint(expr=   m.x109 - m.x162 - m.x168 - m.x174 - m.x180 == 0)

m.c258 = Constraint(expr=   m.x114 - m.x182 - m.x188 == 0)

m.c259 = Constraint(expr=   m.x116 - m.x184 - m.x190 == 0)

m.c260 = Constraint(expr=   m.x118 - m.x186 - m.x192 == 0)

m.c261 = Constraint(expr= - 2000*m.b2 + m.x141 - m.x225 >= -2000)

m.c262 = Constraint(expr= - 2000*m.b3 + m.x149 - m.x227 >= -2000)

m.c263 = Constraint(expr= - 2000*m.b4 + m.x157 - m.x229 >= -2000)

m.c264 = Constraint(expr= - 2000*m.b5 + m.x165 - m.x225 >= -2000)

m.c265 = Constraint(expr= - 2000*m.b6 + m.x171 - m.x227 >= -2000)

m.c266 = Constraint(expr= - 2000*m.b7 + m.x177 - m.x229 >= -2000)

m.c267 = Constraint(expr= - 2000*m.b8 + m.x183 - m.x225 >= -2000)

m.c268 = Constraint(expr= - 2000*m.b9 + m.x189 - m.x227 >= -2000)

m.c269 = Constraint(expr= - 2000*m.b10 + m.x29 - m.x229 >= -2000)

m.c270 = Constraint(expr= - 2000*m.b11 + m.x32 - m.x230 >= -2000)

m.c271 = Constraint(expr= - 2000*m.b12 + m.x36 - m.x231 >= -2000)

m.c272 = Constraint(expr= - 2000*m.b13 + m.x40 - m.x232 >= -2000)

m.c273 = Constraint(expr= - 2000*m.b14 + m.x44 - m.x230 >= -2000)

m.c274 = Constraint(expr= - 2000*m.b15 + m.x47 - m.x231 >= -2000)

m.c275 = Constraint(expr= - 2000*m.b16 + m.x50 - m.x232 >= -2000)

m.c276 = Constraint(expr= - 2000*m.b17 + m.x53 - m.x230 >= -2000)

m.c277 = Constraint(expr= - 2000*m.b18 + m.x57 - m.x231 >= -2000)

m.c278 = Constraint(expr= - 2000*m.b19 + m.x61 - m.x232 >= -2000)

m.c279 = Constraint(expr= - 2000*m.b20 + m.x65 - m.x230 >= -2000)

m.c280 = Constraint(expr= - 2000*m.b21 + m.x68 - m.x231 >= -2000)

m.c281 = Constraint(expr= - 2000*m.b22 + m.x71 - m.x232 >= -2000)

m.c282 = Constraint(expr= - 2000*m.b23 + m.x74 - m.x233 >= -2000)

m.c283 = Constraint(expr= - 2000*m.b24 + m.x78 - m.x234 >= -2000)

m.c284 = Constraint(expr= - 2000*m.b25 + m.x82 - m.x235 >= -2000)

m.c285 = Constraint(expr= - 2000*m.b26 + m.x86 - m.x233 >= -2000)

m.c286 = Constraint(expr= - 2000*m.b27 + m.x89 - m.x234 >= -2000)

m.c287 = Constraint(expr= - 2000*m.b28 + m.x92 - m.x235 >= -2000)

m.c288 = Constraint(expr=   1049*m.b2 + m.x141 - m.x225 <= 1049)

m.c289 = Constraint(expr=   1049*m.b3 + m.x149 - m.x227 <= 1049)

m.c290 = Constraint(expr=   1049*m.b4 + m.x157 - m.x229 <= 1049)

m.c291 = Constraint(expr=   1049*m.b5 + m.x165 - m.x225 <= 1049)

m.c292 = Constraint(expr=   1049*m.b6 + m.x171 - m.x227 <= 1049)

m.c293 = Constraint(expr=   1049*m.b7 + m.x177 - m.x229 <= 1049)

m.c294 = Constraint(expr=   1049*m.b8 + m.x183 - m.x225 <= 1049)

m.c295 = Constraint(expr=   1049*m.b9 + m.x189 - m.x227 <= 1049)

m.c296 = Constraint(expr=   1049*m.b10 + m.x29 - m.x229 <= 1049)

m.c297 = Constraint(expr=   1065*m.b11 + m.x32 - m.x230 <= 1065)

m.c298 = Constraint(expr=   1065*m.b12 + m.x36 - m.x231 <= 1065)

m.c299 = Constraint(expr=   1065*m.b13 + m.x40 - m.x232 <= 1065)

m.c300 = Constraint(expr=   1065*m.b14 + m.x44 - m.x230 <= 1065)

m.c301 = Constraint(expr=   1065*m.b15 + m.x47 - m.x231 <= 1065)

m.c302 = Constraint(expr=   1065*m.b16 + m.x50 - m.x232 <= 1065)

m.c303 = Constraint(expr=   1065*m.b17 + m.x53 - m.x230 <= 1065)

m.c304 = Constraint(expr=   1065*m.b18 + m.x57 - m.x231 <= 1065)

m.c305 = Constraint(expr=   1065*m.b19 + m.x61 - m.x232 <= 1065)

m.c306 = Constraint(expr=   1065*m.b20 + m.x65 - m.x230 <= 1065)

m.c307 = Constraint(expr=   1065*m.b21 + m.x68 - m.x231 <= 1065)

m.c308 = Constraint(expr=   1065*m.b22 + m.x71 - m.x232 <= 1065)

m.c309 = Constraint(expr=   1095*m.b23 + m.x74 - m.x233 <= 1095)

m.c310 = Constraint(expr=   1095*m.b24 + m.x78 - m.x234 <= 1095)

m.c311 = Constraint(expr=   1095*m.b25 + m.x82 - m.x235 <= 1095)

m.c312 = Constraint(expr=   1095*m.b26 + m.x86 - m.x233 <= 1095)

m.c313 = Constraint(expr=   1095*m.b27 + m.x89 - m.x234 <= 1095)

m.c314 = Constraint(expr=   1095*m.b28 + m.x92 - m.x235 <= 1095)

m.c315 = Constraint(expr= - m.x197 + m.x210 >= 0)

m.c316 = Constraint(expr= - m.x198 + m.x213 >= 0)

m.c317 = Constraint(expr= - m.x199 + m.x216 >= 0)

m.c318 = Constraint(expr=   m.x200 - m.x275 >= 0)

m.c319 = Constraint(expr=   m.x201 - m.x276 >= 0)

m.c320 = Constraint(expr=   m.x202 - m.x277 >= 0)

m.c321 = Constraint(expr= - 0.309838295393634*m.x278 + 13.94696158*m.x279 + 24.46510819*m.x280 - 7.28623839*m.x281
                          - 23.57687014*m.x282 <= 0)

m.c322 = Constraint(expr= - 0.309838295393634*m.x283 + 13.94696158*m.x284 + 24.46510819*m.x285 - 7.28623839*m.x286
                          - 23.57687014*m.x287 <= 0)

m.c323 = Constraint(expr= - 0.309838295393634*m.x288 + 13.94696158*m.x289 + 24.46510819*m.x290 - 7.28623839*m.x291
                          - 23.57687014*m.x292 <= 0)

m.c324 = Constraint(expr= - 0.309838295393634*m.x293 + 13.94696158*m.x294 + 24.46510819*m.x295 - 7.28623839*m.x296
                          - 23.57687014*m.x297 <= 0)

m.c325 = Constraint(expr= - 0.309838295393634*m.x298 + 13.94696158*m.x299 + 24.46510819*m.x300 - 7.28623839*m.x301
                          - 23.57687014*m.x302 <= 0)

m.c326 = Constraint(expr= - 0.309838295393634*m.x303 + 13.94696158*m.x304 + 24.46510819*m.x305 - 7.28623839*m.x306
                          - 23.57687014*m.x307 <= 0)

m.c327 = Constraint(expr= - 0.309838295393634*m.x308 + 13.94696158*m.x309 + 24.46510819*m.x310 - 7.28623839*m.x311
                          - 23.57687014*m.x312 <= 0)

m.c328 = Constraint(expr= - 0.309838295393634*m.x313 + 13.94696158*m.x314 + 24.46510819*m.x315 - 7.28623839*m.x316
                          - 23.57687014*m.x317 <= 0)

m.c329 = Constraint(expr= - 0.309838295393634*m.x318 + 13.94696158*m.x319 + 24.46510819*m.x320 - 7.28623839*m.x321
                          - 23.57687014*m.x322 <= 0)

m.c330 = Constraint(expr= - 0.309838295393634*m.x323 + 29.29404529*m.x324 - 108.39408287*m.x325 + 442.21990639*m.x326
                          - 454.58448169*m.x327 <= 0)

m.c331 = Constraint(expr= - 0.309838295393634*m.x328 + 29.29404529*m.x329 - 108.39408287*m.x330 + 442.21990639*m.x331
                          - 454.58448169*m.x332 <= 0)

m.c332 = Constraint(expr= - 0.309838295393634*m.x333 + 29.29404529*m.x334 - 108.39408287*m.x335 + 442.21990639*m.x336
                          - 454.58448169*m.x337 <= 0)

m.c333 = Constraint(expr= - 0.309838295393634*m.x338 + 29.29404529*m.x339 - 108.39408287*m.x340 + 442.21990639*m.x341
                          - 454.58448169*m.x342 <= 0)

m.c334 = Constraint(expr=   442.21990639*m.x343 - 454.58448169*m.x344 - 0.309838295393634*m.x345 + 29.29404529*m.x346
                          - 108.39408287*m.x347 <= 0)

m.c335 = Constraint(expr= - 0.309838295393634*m.x348 + 29.29404529*m.x349 - 108.39408287*m.x350 + 442.21990639*m.x351
                          - 454.58448169*m.x352 <= 0)

m.c336 = Constraint(expr= - 0.309838295393634*m.x353 + 25.92674585*m.x354 + 18.13482123*m.x355 + 22.12766012*m.x356
                          - 42.68950769*m.x357 <= 0)

m.c337 = Constraint(expr= - 0.309838295393634*m.x358 + 25.92674585*m.x359 + 18.13482123*m.x360 + 22.12766012*m.x361
                          - 42.68950769*m.x362 <= 0)

m.c338 = Constraint(expr= - 0.309838295393634*m.x363 + 25.92674585*m.x364 + 18.13482123*m.x365 + 22.12766012*m.x366
                          - 42.68950769*m.x367 <= 0)

m.c339 = Constraint(expr= - 0.309838295393634*m.x368 + 25.92674585*m.x369 + 18.13482123*m.x370 + 22.12766012*m.x371
                          - 42.68950769*m.x372 <= 0)

m.c340 = Constraint(expr= - 0.309838295393634*m.x373 + 25.92674585*m.x374 + 18.13482123*m.x375 + 22.12766012*m.x376
                          - 42.68950769*m.x377 <= 0)

m.c341 = Constraint(expr= - 0.309838295393634*m.x378 + 25.92674585*m.x379 + 18.13482123*m.x380 + 22.12766012*m.x381
                          - 42.68950769*m.x382 <= 0)

m.c342 = Constraint(expr= - 0.309838295393634*m.x383 + 17.4714791*m.x384 - 39.98407808*m.x385 + 134.55943082*m.x386
                          - 135.88441782*m.x387 <= 0)

m.c343 = Constraint(expr= - 0.309838295393634*m.x388 + 17.4714791*m.x389 - 39.98407808*m.x390 + 134.55943082*m.x391
                          - 135.88441782*m.x392 <= 0)

m.c344 = Constraint(expr= - 0.309838295393634*m.x393 + 17.4714791*m.x394 - 39.98407808*m.x395 + 134.55943082*m.x396
                          - 135.88441782*m.x397 <= 0)

m.c345 = Constraint(expr= - 0.309838295393634*m.x398 + 17.4714791*m.x399 - 39.98407808*m.x400 + 134.55943082*m.x401
                          - 135.88441782*m.x402 <= 0)

m.c346 = Constraint(expr= - 0.309838295393634*m.x403 + 17.4714791*m.x404 - 39.98407808*m.x405 + 134.55943082*m.x406
                          - 135.88441782*m.x407 <= 0)

m.c347 = Constraint(expr= - 0.309838295393634*m.x408 + 17.4714791*m.x409 - 39.98407808*m.x410 + 134.55943082*m.x411
                          - 135.88441782*m.x412 <= 0)

m.c348 = Constraint(expr=m.x98**2 - m.x413 == 0)

m.c349 = Constraint(expr=   m.x204 - 5*m.x413 == 0)

m.c350 = Constraint(expr=m.x100**2 - m.x414 == 0)

m.c351 = Constraint(expr=   m.x206 - 5*m.x414 == 0)

m.c352 = Constraint(expr=m.x102**2 - m.x415 == 0)

m.c353 = Constraint(expr=   m.x208 - 5*m.x415 == 0)

m.c354 = Constraint(expr=m.x104**2 - m.x416 == 0)

m.c355 = Constraint(expr=   m.x211 - 4*m.x416 == 0)

m.c356 = Constraint(expr=m.x106**2 - m.x417 == 0)

m.c357 = Constraint(expr=   m.x214 - 4*m.x417 == 0)

m.c358 = Constraint(expr=m.x108**2 - m.x418 == 0)

m.c359 = Constraint(expr=   m.x217 - 4*m.x418 == 0)

m.c360 = Constraint(expr=m.x113**2 - m.x419 == 0)

m.c361 = Constraint(expr=   m.x219 - 5*m.x419 == 0)

m.c362 = Constraint(expr=m.x115**2 - m.x420 == 0)

m.c363 = Constraint(expr=   m.x221 - 5*m.x420 == 0)

m.c364 = Constraint(expr=m.x117**2 - m.x421 == 0)

m.c365 = Constraint(expr=   m.x223 - 5*m.x421 == 0)

m.c366 = Constraint(expr=m.x140**2 - m.x422 == 0)

m.c367 = Constraint(expr=   m.x143 - m.x422 == 0)

m.c368 = Constraint(expr=m.x140**3 - m.x423 == 0)

m.c369 = Constraint(expr=   m.x282 - m.x423 == 0)

m.c370 = Constraint(expr=m.x142**2 - m.x424 == 0)

m.c371 = Constraint(expr=   m.x151 - m.x424 == 0)

m.c372 = Constraint(expr=m.x142**3 - m.x425 == 0)

m.c373 = Constraint(expr=   m.x287 - m.x425 == 0)

m.c374 = Constraint(expr=m.x144**2 - m.x426 == 0)

m.c375 = Constraint(expr=   m.x159 - m.x426 == 0)

m.c376 = Constraint(expr=m.x144**3 - m.x427 == 0)

m.c377 = Constraint(expr=   m.x292 - m.x427 == 0)

m.c378 = Constraint(expr=m.x146**2 - m.x428 == 0)

m.c379 = Constraint(expr=   m.x167 - m.x428 == 0)

m.c380 = Constraint(expr=m.x146**3 - m.x429 == 0)

m.c381 = Constraint(expr=   m.x297 - m.x429 == 0)

m.c382 = Constraint(expr=m.x148**2 - m.x430 == 0)

m.c383 = Constraint(expr=   m.x175 - m.x430 == 0)

m.c384 = Constraint(expr=m.x148**3 - m.x431 == 0)

m.c385 = Constraint(expr=   m.x302 - m.x431 == 0)

m.c386 = Constraint(expr=m.x150**2 - m.x432 == 0)

m.c387 = Constraint(expr=   m.x181 - m.x432 == 0)

m.c388 = Constraint(expr=m.x150**3 - m.x433 == 0)

m.c389 = Constraint(expr=   m.x307 - m.x433 == 0)

m.c390 = Constraint(expr=m.x152**2 - m.x434 == 0)

m.c391 = Constraint(expr=   m.x187 - m.x434 == 0)

m.c392 = Constraint(expr=m.x152**3 - m.x435 == 0)

m.c393 = Constraint(expr=   m.x312 - m.x435 == 0)

m.c394 = Constraint(expr=m.x154**2 - m.x436 == 0)

m.c395 = Constraint(expr=   m.x191 - m.x436 == 0)

m.c396 = Constraint(expr=m.x154**3 - m.x437 == 0)

m.c397 = Constraint(expr=   m.x317 - m.x437 == 0)

m.c398 = Constraint(expr=m.x156**2 - m.x438 == 0)

m.c399 = Constraint(expr=   m.x30 - m.x438 == 0)

m.c400 = Constraint(expr=m.x156**3 - m.x439 == 0)

m.c401 = Constraint(expr=   m.x322 - m.x439 == 0)

m.c402 = Constraint(expr=m.x158**2 - m.x440 == 0)

m.c403 = Constraint(expr=   m.x35 - m.x440 == 0)

m.c404 = Constraint(expr=m.x158**3 - m.x441 == 0)

m.c405 = Constraint(expr=   m.x327 - m.x441 == 0)

m.c406 = Constraint(expr=m.x160**2 - m.x442 == 0)

m.c407 = Constraint(expr=   m.x37 - m.x442 == 0)

m.c408 = Constraint(expr=m.x160**3 - m.x443 == 0)

m.c409 = Constraint(expr=   m.x332 - m.x443 == 0)

m.c410 = Constraint(expr=m.x162**2 - m.x444 == 0)

m.c411 = Constraint(expr=   m.x42 - m.x444 == 0)

m.c412 = Constraint(expr=m.x162**3 - m.x445 == 0)

m.c413 = Constraint(expr=   m.x337 - m.x445 == 0)

m.c414 = Constraint(expr=m.x164**2 - m.x446 == 0)

m.c415 = Constraint(expr=   m.x46 - m.x446 == 0)

m.c416 = Constraint(expr=m.x164**3 - m.x447 == 0)

m.c417 = Constraint(expr=   m.x342 - m.x447 == 0)

m.c418 = Constraint(expr=m.x166**2 - m.x448 == 0)

m.c419 = Constraint(expr=   m.x48 - m.x448 == 0)

m.c420 = Constraint(expr=m.x166**3 - m.x449 == 0)

m.c421 = Constraint(expr=   m.x344 - m.x449 == 0)

m.c422 = Constraint(expr=m.x168**2 - m.x450 == 0)

m.c423 = Constraint(expr=   m.x52 - m.x450 == 0)

m.c424 = Constraint(expr=m.x168**3 - m.x451 == 0)

m.c425 = Constraint(expr=   m.x352 - m.x451 == 0)

m.c426 = Constraint(expr=m.x170**2 - m.x452 == 0)

m.c427 = Constraint(expr=   m.x56 - m.x452 == 0)

m.c428 = Constraint(expr=m.x170**3 - m.x453 == 0)

m.c429 = Constraint(expr=   m.x357 - m.x453 == 0)

m.c430 = Constraint(expr=m.x172**2 - m.x454 == 0)

m.c431 = Constraint(expr=   m.x58 - m.x454 == 0)

m.c432 = Constraint(expr=m.x172**3 - m.x455 == 0)

m.c433 = Constraint(expr=   m.x362 - m.x455 == 0)

m.c434 = Constraint(expr=m.x174**2 - m.x456 == 0)

m.c435 = Constraint(expr=   m.x64 - m.x456 == 0)

m.c436 = Constraint(expr=m.x174**3 - m.x457 == 0)

m.c437 = Constraint(expr=   m.x367 - m.x457 == 0)

m.c438 = Constraint(expr=m.x176**2 - m.x458 == 0)

m.c439 = Constraint(expr=   m.x67 - m.x458 == 0)

m.c440 = Constraint(expr=m.x176**3 - m.x459 == 0)

m.c441 = Constraint(expr=   m.x372 - m.x459 == 0)

m.c442 = Constraint(expr=m.x178**2 - m.x460 == 0)

m.c443 = Constraint(expr=   m.x69 - m.x460 == 0)

m.c444 = Constraint(expr=m.x178**3 - m.x461 == 0)

m.c445 = Constraint(expr=   m.x377 - m.x461 == 0)

m.c446 = Constraint(expr=m.x180**2 - m.x462 == 0)

m.c447 = Constraint(expr=   m.x73 - m.x462 == 0)

m.c448 = Constraint(expr=m.x180**3 - m.x463 == 0)

m.c449 = Constraint(expr=   m.x382 - m.x463 == 0)

m.c450 = Constraint(expr=m.x182**2 - m.x464 == 0)

m.c451 = Constraint(expr=   m.x76 - m.x464 == 0)

m.c452 = Constraint(expr=m.x182**3 - m.x465 == 0)

m.c453 = Constraint(expr=   m.x387 - m.x465 == 0)

m.c454 = Constraint(expr=m.x184**2 - m.x466 == 0)

m.c455 = Constraint(expr=   m.x81 - m.x466 == 0)

m.c456 = Constraint(expr=m.x184**3 - m.x467 == 0)

m.c457 = Constraint(expr=   m.x392 - m.x467 == 0)

m.c458 = Constraint(expr=m.x186**2 - m.x468 == 0)

m.c459 = Constraint(expr=   m.x85 - m.x468 == 0)

m.c460 = Constraint(expr=m.x186**3 - m.x469 == 0)

m.c461 = Constraint(expr=   m.x397 - m.x469 == 0)

m.c462 = Constraint(expr=m.x188**2 - m.x470 == 0)

m.c463 = Constraint(expr=   m.x87 - m.x470 == 0)

m.c464 = Constraint(expr=m.x188**3 - m.x471 == 0)

m.c465 = Constraint(expr=   m.x402 - m.x471 == 0)

m.c466 = Constraint(expr=m.x190**2 - m.x472 == 0)

m.c467 = Constraint(expr=   m.x90 - m.x472 == 0)

m.c468 = Constraint(expr=m.x190**3 - m.x473 == 0)

m.c469 = Constraint(expr=   m.x407 - m.x473 == 0)

m.c470 = Constraint(expr=m.x192**2 - m.x474 == 0)

m.c471 = Constraint(expr=   m.x94 - m.x474 == 0)

m.c472 = Constraint(expr=m.x192**3 - m.x475 == 0)

m.c473 = Constraint(expr=   m.x412 - m.x475 == 0)

m.c474 = Constraint(expr=m.x140*m.x263 - m.x145 == 0)

m.c475 = Constraint(expr=m.x263*m.x422 - m.x281 == 0)

m.c476 = Constraint(expr=m.x146*m.x263 - m.x169 == 0)

m.c477 = Constraint(expr=m.x263*m.x428 - m.x296 == 0)

m.c478 = Constraint(expr=m.x152*m.x263 - m.x185 == 0)

m.c479 = Constraint(expr=m.x263*m.x434 - m.x311 == 0)

m.c480 = Constraint(expr=m.x263**2 - m.x476 == 0)

m.c481 = Constraint(expr=   m.x147 - m.x476 == 0)

m.c482 = Constraint(expr=m.x140*m.x476 - m.x280 == 0)

m.c483 = Constraint(expr=m.x146*m.x476 - m.x295 == 0)

m.c484 = Constraint(expr=m.x152*m.x476 - m.x310 == 0)

m.c485 = Constraint(expr=m.x263**3 - m.x477 == 0)

m.c486 = Constraint(expr=m.b2*m.x477 - m.x279 == 0)

m.c487 = Constraint(expr=m.b5*m.x477 - m.x294 == 0)

m.c488 = Constraint(expr=m.b8*m.x477 - m.x309 == 0)

m.c489 = Constraint(expr=m.x142*m.x264 - m.x155 == 0)

m.c490 = Constraint(expr=m.x264*m.x424 - m.x286 == 0)

m.c491 = Constraint(expr=m.x148*m.x264 - m.x173 == 0)

m.c492 = Constraint(expr=m.x264*m.x430 - m.x301 == 0)

m.c493 = Constraint(expr=m.x154*m.x264 - m.x193 == 0)

m.c494 = Constraint(expr=m.x264*m.x436 - m.x316 == 0)

m.c495 = Constraint(expr=m.x264**2 - m.x478 == 0)

m.c496 = Constraint(expr=   m.x153 - m.x478 == 0)

m.c497 = Constraint(expr=m.x142*m.x478 - m.x285 == 0)

m.c498 = Constraint(expr=m.x148*m.x478 - m.x300 == 0)

m.c499 = Constraint(expr=m.x154*m.x478 - m.x315 == 0)

m.c500 = Constraint(expr=m.x264**3 - m.x479 == 0)

m.c501 = Constraint(expr=m.b3*m.x479 - m.x284 == 0)

m.c502 = Constraint(expr=m.b6*m.x479 - m.x299 == 0)

m.c503 = Constraint(expr=m.b9*m.x479 - m.x314 == 0)

m.c504 = Constraint(expr=m.x144*m.x265 - m.x163 == 0)

m.c505 = Constraint(expr=m.x265*m.x426 - m.x291 == 0)

m.c506 = Constraint(expr=m.x150*m.x265 - m.x179 == 0)

m.c507 = Constraint(expr=m.x265*m.x432 - m.x306 == 0)

m.c508 = Constraint(expr=m.x156*m.x265 - m.x31 == 0)

m.c509 = Constraint(expr=m.x265*m.x438 - m.x321 == 0)

m.c510 = Constraint(expr=m.x265**2 - m.x480 == 0)

m.c511 = Constraint(expr=   m.x161 - m.x480 == 0)

m.c512 = Constraint(expr=m.x144*m.x480 - m.x290 == 0)

m.c513 = Constraint(expr=m.x150*m.x480 - m.x305 == 0)

m.c514 = Constraint(expr=m.x156*m.x480 - m.x320 == 0)

m.c515 = Constraint(expr=m.x265**3 - m.x481 == 0)

m.c516 = Constraint(expr=m.b4*m.x481 - m.x289 == 0)

m.c517 = Constraint(expr=m.b7*m.x481 - m.x304 == 0)

m.c518 = Constraint(expr=m.b10*m.x481 - m.x319 == 0)

m.c519 = Constraint(expr=m.x158*m.x266 - m.x34 == 0)

m.c520 = Constraint(expr=m.x266*m.x440 - m.x326 == 0)

m.c521 = Constraint(expr=m.x164*m.x266 - m.x45 == 0)

m.c522 = Constraint(expr=m.x266*m.x446 - m.x341 == 0)

m.c523 = Constraint(expr=m.x266**2 - m.x482 == 0)

m.c524 = Constraint(expr=   m.x33 - m.x482 == 0)

m.c525 = Constraint(expr=m.x158*m.x482 - m.x325 == 0)

m.c526 = Constraint(expr=m.x164*m.x482 - m.x340 == 0)

m.c527 = Constraint(expr=m.x266**3 - m.x483 == 0)

m.c528 = Constraint(expr=m.b11*m.x483 - m.x324 == 0)

m.c529 = Constraint(expr=m.b14*m.x483 - m.x339 == 0)

m.c530 = Constraint(expr=m.x160*m.x267 - m.x39 == 0)

m.c531 = Constraint(expr=m.x267*m.x442 - m.x331 == 0)

m.c532 = Constraint(expr=m.x166*m.x267 - m.x49 == 0)

m.c533 = Constraint(expr=m.x267*m.x448 - m.x343 == 0)

m.c534 = Constraint(expr=m.x267**2 - m.x484 == 0)

m.c535 = Constraint(expr=   m.x38 - m.x484 == 0)

m.c536 = Constraint(expr=m.x160*m.x484 - m.x330 == 0)

m.c537 = Constraint(expr=m.x166*m.x484 - m.x347 == 0)

m.c538 = Constraint(expr=m.x267**3 - m.x485 == 0)

m.c539 = Constraint(expr=m.b12*m.x485 - m.x329 == 0)

m.c540 = Constraint(expr=m.b15*m.x485 - m.x346 == 0)

m.c541 = Constraint(expr=m.x162*m.x268 - m.x41 == 0)

m.c542 = Constraint(expr=m.x268*m.x444 - m.x336 == 0)

m.c543 = Constraint(expr=m.x168*m.x268 - m.x51 == 0)

m.c544 = Constraint(expr=m.x268*m.x450 - m.x351 == 0)

m.c545 = Constraint(expr=m.x268**2 - m.x486 == 0)

m.c546 = Constraint(expr=   m.x43 - m.x486 == 0)

m.c547 = Constraint(expr=m.x162*m.x486 - m.x335 == 0)

m.c548 = Constraint(expr=m.x168*m.x486 - m.x350 == 0)

m.c549 = Constraint(expr=m.x268**3 - m.x487 == 0)

m.c550 = Constraint(expr=m.b13*m.x487 - m.x334 == 0)

m.c551 = Constraint(expr=m.b16*m.x487 - m.x349 == 0)

m.c552 = Constraint(expr=m.x170*m.x269 - m.x54 == 0)

m.c553 = Constraint(expr=m.x269*m.x452 - m.x356 == 0)

m.c554 = Constraint(expr=m.x176*m.x269 - m.x66 == 0)

m.c555 = Constraint(expr=m.x269*m.x458 - m.x371 == 0)

m.c556 = Constraint(expr=m.x269**2 - m.x488 == 0)

m.c557 = Constraint(expr=   m.x55 - m.x488 == 0)

m.c558 = Constraint(expr=m.x170*m.x488 - m.x355 == 0)

m.c559 = Constraint(expr=m.x176*m.x488 - m.x370 == 0)

m.c560 = Constraint(expr=m.x269**3 - m.x489 == 0)

m.c561 = Constraint(expr=m.b17*m.x489 - m.x354 == 0)

m.c562 = Constraint(expr=m.b20*m.x489 - m.x369 == 0)

m.c563 = Constraint(expr=m.x172*m.x270 - m.x59 == 0)

m.c564 = Constraint(expr=m.x270*m.x454 - m.x361 == 0)

m.c565 = Constraint(expr=m.x178*m.x270 - m.x70 == 0)

m.c566 = Constraint(expr=m.x270*m.x460 - m.x376 == 0)

m.c567 = Constraint(expr=m.x270**2 - m.x490 == 0)

m.c568 = Constraint(expr=   m.x60 - m.x490 == 0)

m.c569 = Constraint(expr=m.x172*m.x490 - m.x360 == 0)

m.c570 = Constraint(expr=m.x178*m.x490 - m.x375 == 0)

m.c571 = Constraint(expr=m.x270**3 - m.x491 == 0)

m.c572 = Constraint(expr=m.b18*m.x491 - m.x359 == 0)

m.c573 = Constraint(expr=m.b21*m.x491 - m.x374 == 0)

m.c574 = Constraint(expr=m.x174*m.x271 - m.x63 == 0)

m.c575 = Constraint(expr=m.x271*m.x456 - m.x366 == 0)

m.c576 = Constraint(expr=m.x180*m.x271 - m.x72 == 0)

m.c577 = Constraint(expr=m.x271*m.x462 - m.x381 == 0)

m.c578 = Constraint(expr=m.x271**2 - m.x492 == 0)

m.c579 = Constraint(expr=   m.x62 - m.x492 == 0)

m.c580 = Constraint(expr=m.x174*m.x492 - m.x365 == 0)

m.c581 = Constraint(expr=m.x180*m.x492 - m.x380 == 0)

m.c582 = Constraint(expr=m.x271**3 - m.x493 == 0)

m.c583 = Constraint(expr=m.b19*m.x493 - m.x364 == 0)

m.c584 = Constraint(expr=m.b22*m.x493 - m.x379 == 0)

m.c585 = Constraint(expr=m.x182*m.x272 - m.x75 == 0)

m.c586 = Constraint(expr=m.x272*m.x464 - m.x386 == 0)

m.c587 = Constraint(expr=m.x188*m.x272 - m.x88 == 0)

m.c588 = Constraint(expr=m.x272*m.x470 - m.x401 == 0)

m.c589 = Constraint(expr=m.x272**2 - m.x494 == 0)

m.c590 = Constraint(expr=   m.x77 - m.x494 == 0)

m.c591 = Constraint(expr=m.x182*m.x494 - m.x385 == 0)

m.c592 = Constraint(expr=m.x188*m.x494 - m.x400 == 0)

m.c593 = Constraint(expr=m.x272**3 - m.x495 == 0)

m.c594 = Constraint(expr=m.b23*m.x495 - m.x384 == 0)

m.c595 = Constraint(expr=m.b26*m.x495 - m.x399 == 0)

m.c596 = Constraint(expr=m.x184*m.x273 - m.x79 == 0)

m.c597 = Constraint(expr=m.x273*m.x466 - m.x391 == 0)

m.c598 = Constraint(expr=m.x190*m.x273 - m.x91 == 0)

m.c599 = Constraint(expr=m.x273*m.x472 - m.x406 == 0)

m.c600 = Constraint(expr=m.x273**2 - m.x496 == 0)

m.c601 = Constraint(expr=   m.x80 - m.x496 == 0)

m.c602 = Constraint(expr=m.x184*m.x496 - m.x390 == 0)

m.c603 = Constraint(expr=m.x190*m.x496 - m.x405 == 0)

m.c604 = Constraint(expr=m.x273**3 - m.x497 == 0)

m.c605 = Constraint(expr=m.b24*m.x497 - m.x389 == 0)

m.c606 = Constraint(expr=m.b27*m.x497 - m.x404 == 0)

m.c607 = Constraint(expr=m.x186*m.x274 - m.x83 == 0)

m.c608 = Constraint(expr=m.x274*m.x468 - m.x396 == 0)

m.c609 = Constraint(expr=m.x192*m.x274 - m.x93 == 0)

m.c610 = Constraint(expr=m.x274*m.x474 - m.x411 == 0)

m.c611 = Constraint(expr=m.x274**2 - m.x498 == 0)

m.c612 = Constraint(expr=   m.x84 - m.x498 == 0)

m.c613 = Constraint(expr=m.x186*m.x498 - m.x395 == 0)

m.c614 = Constraint(expr=m.x192*m.x498 - m.x410 == 0)

m.c615 = Constraint(expr=m.x274**3 - m.x499 == 0)

m.c616 = Constraint(expr=m.b25*m.x499 - m.x394 == 0)

m.c617 = Constraint(expr=m.b28*m.x499 - m.x409 == 0)
