#  MINLP written by GAMS Convert at 04/21/18 13:55:18
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        411      244       69       98        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        333      315       18        0        0        0        0        0
#  FX      5        5        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1089      887      202        0
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
m.x20 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x27 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x31 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
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
m.x64 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,1.16),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,1.16),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x82 = Var(within=Reals,bounds=(3.5,3.5),initialize=3.5)
m.x83 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x84 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x85 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x86 = Var(within=Reals,bounds=(4.1,4.1),initialize=4.1)
m.x87 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x88 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x89 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x90 = Var(within=Reals,bounds=(4,4),initialize=4)
m.x91 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x92 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x93 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x94 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x95 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x97 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x99 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x101 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x103 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x105 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x107 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x109 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x111 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x113 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x115 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x117 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x119 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x121 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x123 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x125 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x127 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x129 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x130 = Var(within=Reals,bounds=(62,65),initialize=62)
m.x131 = Var(within=Reals,bounds=(62,65),initialize=62)
m.x132 = Var(within=Reals,bounds=(92.5,95),initialize=92.5)
m.x133 = Var(within=Reals,bounds=(92.5,95),initialize=92.5)
m.x134 = Var(within=Reals,bounds=(105,109),initialize=105)
m.x135 = Var(within=Reals,bounds=(105,109),initialize=105)
m.x136 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x137 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x139 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x142 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x145 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x147 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x149 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x150 = Var(within=Reals,bounds=(49,49),initialize=49)
m.x151 = Var(within=Reals,bounds=(-49,1000),initialize=0)
m.x152 = Var(within=Reals,bounds=(49,49),initialize=49)
m.x153 = Var(within=Reals,bounds=(-49,1000),initialize=0)
m.x154 = Var(within=Reals,bounds=(-65,1000),initialize=0)
m.x155 = Var(within=Reals,bounds=(-65,1000),initialize=0)
m.x156 = Var(within=Reals,bounds=(-95,1000),initialize=0)
m.x157 = Var(within=Reals,bounds=(-95,1000),initialize=0)
m.x158 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x159 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x160 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x161 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x162 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x163 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x164 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x165 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x166 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x167 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x168 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x169 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x170 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x171 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x172 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x173 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x174 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x175 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x176 = Var(within=Reals,bounds=(0.6,1),initialize=0.6)
m.x177 = Var(within=Reals,bounds=(0.6,1),initialize=0.6)
m.x178 = Var(within=Reals,bounds=(0.8,1),initialize=0.8)
m.x179 = Var(within=Reals,bounds=(0.8,1),initialize=0.8)
m.x180 = Var(within=Reals,bounds=(0.85,1),initialize=0.85)
m.x181 = Var(within=Reals,bounds=(0.85,1),initialize=0.85)
m.x182 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x183 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x184 = Var(within=Reals,bounds=(100,1000),initialize=100)
m.x185 = Var(within=Reals,bounds=(100,1000),initialize=100)
m.x186 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x187 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x189 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x190 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x191 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x192 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x193 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x194 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x197 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x198 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x199 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x200 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x201 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x203 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x204 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x205 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x207 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x208 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x209 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x210 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x212 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x213 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x214 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x215 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x217 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x218 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x219 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x220 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x222 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x223 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x224 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x225 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x227 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x228 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x229 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x230 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x232 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x233 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x234 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x235 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x237 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x238 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x239 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x240 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x242 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x243 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x244 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x245 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x247 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x248 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x249 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x250 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x252 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x253 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x254 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x255 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x257 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x258 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x259 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x260 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x262 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x263 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x264 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x265 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x266 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x267 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x268 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x269 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x270 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x271 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x272 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x273 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x274 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x275 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x276 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x277 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x278 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x279 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x280 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x281 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x282 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x283 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x284 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x285 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x286 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x287 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x289 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x290 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x291 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x292 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x293 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x294 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x295 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x296 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x297 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x298 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x299 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x300 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x301 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x302 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x303 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x304 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x305 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x306 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x307 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x309 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x311 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x312 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x313 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x314 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x315 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x316 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x317 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x318 = Var(within=Reals,bounds=(0.36,1),initialize=0.36)
m.x319 = Var(within=Reals,bounds=(0.216,1),initialize=0.216)
m.x320 = Var(within=Reals,bounds=(0.36,1),initialize=0.36)
m.x321 = Var(within=Reals,bounds=(0.216,1),initialize=0.216)
m.x322 = Var(within=Reals,bounds=(0.64,1),initialize=0.64)
m.x323 = Var(within=Reals,bounds=(0.512,1),initialize=0.512)
m.x324 = Var(within=Reals,bounds=(0.64,1),initialize=0.64)
m.x325 = Var(within=Reals,bounds=(0.512,1),initialize=0.512)
m.x326 = Var(within=Reals,bounds=(0.7225,1),initialize=0.7225)
m.x327 = Var(within=Reals,bounds=(0.614125,1),initialize=0.614125)
m.x328 = Var(within=Reals,bounds=(0.7225,1),initialize=0.7225)
m.x329 = Var(within=Reals,bounds=(0.614125,1),initialize=0.614125)
m.x330 = Var(within=Reals,bounds=(0.49,1),initialize=0.49)
m.x331 = Var(within=Reals,bounds=(0.343,1),initialize=0.343)
m.x332 = Var(within=Reals,bounds=(0.49,1),initialize=0.49)
m.x333 = Var(within=Reals,bounds=(0.343,1),initialize=0.343)

m.obj = Objective(expr=   m.x188 + m.x195 + m.x196 + m.x202 + m.x206 + m.x211 + m.x216 + m.x221 + m.x226 + m.x231
                        + m.x236 + m.x241 + m.x246 + m.x251 + m.x256 + m.x261 + m.x266 + m.x272, sense=minimize)

m.c2 = Constraint(expr=   m.x95 + 27.42831624*m.x97 - 57.2814121*m.x99 + 37.5407324*m.x101 == 0)

m.c3 = Constraint(expr=   m.x103 + 37.5407324*m.x105 + 27.42831624*m.x107 - 57.2814121*m.x109 == 0)

m.c4 = Constraint(expr= - 57.2814121*m.x99 + m.x111 + 27.42831624*m.x113 + 37.5407324*m.x115 == 0)

m.c5 = Constraint(expr= - 57.2814121*m.x109 + m.x117 + 37.5407324*m.x119 + 27.42831624*m.x121 == 0)

m.c6 = Constraint(expr= - 57.2814121*m.x99 + m.x123 + 27.42831624*m.x125 + 37.5407324*m.x127 == 0)

m.c7 = Constraint(expr=   27.42831624*m.x20 + 37.5407324*m.x21 - 57.2814121*m.x109 + m.x129 == 0)

m.c8 = Constraint(expr=   m.x22 - 76.45219958*m.x23 + 43.14087708*m.x24 + 50.37356589*m.x25 == 0)

m.c9 = Constraint(expr=   m.x26 + 43.14087708*m.x27 - 76.45219958*m.x28 + 50.37356589*m.x29 == 0)

m.c10 = Constraint(expr= - 76.45219958*m.x23 + m.x30 + 50.37356589*m.x31 + 43.14087708*m.x32 == 0)

m.c11 = Constraint(expr= - 76.45219958*m.x28 + m.x33 + 50.37356589*m.x34 + 43.14087708*m.x35 == 0)

m.c12 = Constraint(expr=   m.x36 - 69.39622571*m.x37 + 58.31011875*m.x38 - 25.39911174*m.x39 == 0)

m.c13 = Constraint(expr=   m.x40 - 25.39911174*m.x41 + 58.31011875*m.x42 - 69.39622571*m.x43 == 0)

m.c14 = Constraint(expr= - 69.39622571*m.x37 + m.x44 - 25.39911174*m.x45 + 58.31011875*m.x46 == 0)

m.c15 = Constraint(expr= - 69.39622571*m.x43 + m.x47 - 25.39911174*m.x48 + 58.31011875*m.x49 == 0)

m.c16 = Constraint(expr=   m.x50 + 63.61644904*m.x51 - 34.92732674*m.x52 - 2.03724124*m.x53 == 0)

m.c17 = Constraint(expr=   m.x54 - 34.92732674*m.x55 - 2.03724124*m.x56 + 63.61644904*m.x57 == 0)

m.c18 = Constraint(expr= - 34.92732674*m.x52 + m.x58 + 63.61644904*m.x59 - 2.03724124*m.x60 == 0)

m.c19 = Constraint(expr= - 34.92732674*m.x55 + m.x61 + 63.61644904*m.x62 - 2.03724124*m.x63 == 0)

m.c20 = Constraint(expr=   m.x64 + m.x65 >= 0.591111111)

m.c21 = Constraint(expr= - m.x66 + m.x67 == 0)

m.c22 = Constraint(expr= - m.x68 + m.x69 == 0)

m.c23 = Constraint(expr= - m.x70 + m.x71 == 0)

m.c24 = Constraint(expr= - m.x72 + m.x73 == 0)

m.c25 = Constraint(expr=   m.x70 - m.x74 == 0)

m.c26 = Constraint(expr=   m.x72 - m.x75 == 0)

m.c27 = Constraint(expr= - m.x76 + m.x77 == 0)

m.c28 = Constraint(expr= - m.x78 + m.x79 == 0)

m.c29 = Constraint(expr=   m.x80 == 0.296666667)

m.c30 = Constraint(expr=   m.x81 == 0.294444444)

m.c31 = Constraint(expr=   m.x64 - m.x67 == 0)

m.c32 = Constraint(expr=   m.x65 - m.x69 == 0)

m.c33 = Constraint(expr=   3600*m.x66 - 3600*m.x71 + 1800*m.x82 - 1800*m.x83 == 0)

m.c34 = Constraint(expr=   3600*m.x68 - 3600*m.x73 + 1800*m.x84 - 1800*m.x85 == 0)

m.c35 = Constraint(expr=   3600*m.x74 - 3600*m.x77 + 720*m.x86 - 720*m.x87 == 0)

m.c36 = Constraint(expr=   3600*m.x75 - 3600*m.x79 + 720*m.x88 - 720*m.x89 == 0)

m.c37 = Constraint(expr=   3600*m.x76 - 3600*m.x80 + 1600*m.x90 - 1600*m.x91 == 0)

m.c38 = Constraint(expr=   3600*m.x78 - 3600*m.x81 + 1600*m.x92 - 1600*m.x93 == 0)

m.c39 = Constraint(expr= - m.x83 + m.x84 == 0)

m.c40 = Constraint(expr= - m.x87 + m.x88 == 0)

m.c41 = Constraint(expr= - m.x91 + m.x92 == 0)

m.c42 = Constraint(expr= - 0.2*m.b2 + m.x94 >= 0)

m.c43 = Constraint(expr= - 0.2*m.b3 + m.x96 >= 0)

m.c44 = Constraint(expr= - 0.2*m.b4 + m.x98 >= 0)

m.c45 = Constraint(expr= - 0.2*m.b5 + m.x100 >= 0)

m.c46 = Constraint(expr= - 0.2*m.b6 + m.x102 >= 0)

m.c47 = Constraint(expr= - 0.2*m.b7 + m.x104 >= 0)

m.c48 = Constraint(expr= - 0.25*m.b8 + m.x106 >= 0)

m.c49 = Constraint(expr= - 0.25*m.b9 + m.x108 >= 0)

m.c50 = Constraint(expr= - 0.25*m.b10 + m.x110 >= 0)

m.c51 = Constraint(expr= - 0.25*m.b11 + m.x112 >= 0)

m.c52 = Constraint(expr= - 0.4*m.b12 + m.x114 >= 0)

m.c53 = Constraint(expr= - 0.4*m.b13 + m.x116 >= 0)

m.c54 = Constraint(expr= - 0.4*m.b14 + m.x118 >= 0)

m.c55 = Constraint(expr= - 0.4*m.b15 + m.x120 >= 0)

m.c56 = Constraint(expr= - 0.24*m.b16 + m.x122 >= 0)

m.c57 = Constraint(expr= - 0.24*m.b17 + m.x124 >= 0)

m.c58 = Constraint(expr= - 0.24*m.b18 + m.x126 >= 0)

m.c59 = Constraint(expr= - 0.24*m.b19 + m.x128 >= 0)

m.c60 = Constraint(expr= - 0.8*m.b2 + m.x94 <= 0)

m.c61 = Constraint(expr= - 0.8*m.b3 + m.x96 <= 0)

m.c62 = Constraint(expr= - 0.8*m.b4 + m.x98 <= 0)

m.c63 = Constraint(expr= - 0.8*m.b5 + m.x100 <= 0)

m.c64 = Constraint(expr= - 0.8*m.b6 + m.x102 <= 0)

m.c65 = Constraint(expr= - 0.8*m.b7 + m.x104 <= 0)

m.c66 = Constraint(expr= - 0.5*m.b8 + m.x106 <= 0)

m.c67 = Constraint(expr= - 0.5*m.b9 + m.x108 <= 0)

m.c68 = Constraint(expr= - 0.5*m.b10 + m.x110 <= 0)

m.c69 = Constraint(expr= - 0.5*m.b11 + m.x112 <= 0)

m.c70 = Constraint(expr= - 0.7*m.b12 + m.x114 <= 0)

m.c71 = Constraint(expr= - 0.7*m.b13 + m.x116 <= 0)

m.c72 = Constraint(expr= - 0.7*m.b14 + m.x118 <= 0)

m.c73 = Constraint(expr= - 0.7*m.b15 + m.x120 <= 0)

m.c74 = Constraint(expr= - 0.58*m.b16 + m.x122 <= 0)

m.c75 = Constraint(expr= - 0.58*m.b17 + m.x124 <= 0)

m.c76 = Constraint(expr= - 0.58*m.b18 + m.x126 <= 0)

m.c77 = Constraint(expr= - 0.58*m.b19 + m.x128 <= 0)

m.c78 = Constraint(expr= - m.x82 + m.x130 == 60)

m.c79 = Constraint(expr= - m.x84 + m.x131 == 60)

m.c80 = Constraint(expr= - m.x86 + m.x132 == 90)

m.c81 = Constraint(expr= - m.x88 + m.x133 == 90)

m.c82 = Constraint(expr= - m.x90 + m.x134 == 103)

m.c83 = Constraint(expr= - m.x92 + m.x135 == 103)

m.c84 = Constraint(expr= - m.x130 + m.x136 - m.x137 == 0)

m.c85 = Constraint(expr= - m.x131 + m.x138 - m.x139 == 0)

m.c86 = Constraint(expr=   m.x140 - m.x141 - m.x142 == 0)

m.c87 = Constraint(expr=   m.x143 - m.x144 - m.x145 == 0)

m.c88 = Constraint(expr= - m.x134 + m.x146 - m.x147 == 0)

m.c89 = Constraint(expr= - m.x135 + m.x148 - m.x149 == 0)

m.c90 = Constraint(expr=   m.x136 - m.x150 - m.x151 == 0)

m.c91 = Constraint(expr=   m.x138 - m.x152 - m.x153 == 0)

m.c92 = Constraint(expr= - m.x130 + m.x140 - m.x154 == 0)

m.c93 = Constraint(expr= - m.x131 + m.x143 - m.x155 == 0)

m.c94 = Constraint(expr= - m.x132 + m.x146 - m.x156 == 0)

m.c95 = Constraint(expr= - m.x133 + m.x148 - m.x157 == 0)

m.c96 = Constraint(expr=   0.2*m.b2 - m.x94 + m.x158 <= 0.2)

m.c97 = Constraint(expr=   0.2*m.b3 - m.x96 + m.x159 <= 0.2)

m.c98 = Constraint(expr=   0.2*m.b4 - m.x98 + m.x160 <= 0.2)

m.c99 = Constraint(expr=   0.2*m.b5 - m.x100 + m.x161 <= 0.2)

m.c100 = Constraint(expr=   0.2*m.b6 - m.x102 + m.x162 <= 0.2)

m.c101 = Constraint(expr=   0.2*m.b7 - m.x104 + m.x163 <= 0.2)

m.c102 = Constraint(expr=   0.25*m.b8 - m.x106 + m.x164 <= 0.25)

m.c103 = Constraint(expr=   0.25*m.b9 - m.x108 + m.x165 <= 0.25)

m.c104 = Constraint(expr=   0.25*m.b10 - m.x110 + m.x166 <= 0.25)

m.c105 = Constraint(expr=   0.25*m.b11 - m.x112 + m.x167 <= 0.25)

m.c106 = Constraint(expr=   0.4*m.b12 - m.x114 + m.x168 <= 0.4)

m.c107 = Constraint(expr=   0.4*m.b13 - m.x116 + m.x169 <= 0.4)

m.c108 = Constraint(expr=   0.4*m.b14 - m.x118 + m.x170 <= 0.4)

m.c109 = Constraint(expr=   0.4*m.b15 - m.x120 + m.x171 <= 0.4)

m.c110 = Constraint(expr=   0.24*m.b16 - m.x122 + m.x172 <= 0.24)

m.c111 = Constraint(expr=   0.24*m.b17 - m.x124 + m.x173 <= 0.24)

m.c112 = Constraint(expr=   0.24*m.b18 - m.x126 + m.x174 <= 0.24)

m.c113 = Constraint(expr=   0.24*m.b19 - m.x128 + m.x175 <= 0.24)

m.c114 = Constraint(expr= - m.x94 + m.x158 >= 0)

m.c115 = Constraint(expr= - m.x96 + m.x159 >= 0)

m.c116 = Constraint(expr= - m.x98 + m.x160 >= 0)

m.c117 = Constraint(expr= - m.x100 + m.x161 >= 0)

m.c118 = Constraint(expr= - m.x102 + m.x162 >= 0)

m.c119 = Constraint(expr= - m.x104 + m.x163 >= 0)

m.c120 = Constraint(expr= - m.x106 + m.x164 >= 0)

m.c121 = Constraint(expr= - m.x108 + m.x165 >= 0)

m.c122 = Constraint(expr= - m.x110 + m.x166 >= 0)

m.c123 = Constraint(expr= - m.x112 + m.x167 >= 0)

m.c124 = Constraint(expr= - m.x114 + m.x168 >= 0)

m.c125 = Constraint(expr= - m.x116 + m.x169 >= 0)

m.c126 = Constraint(expr= - m.x118 + m.x170 >= 0)

m.c127 = Constraint(expr= - m.x120 + m.x171 >= 0)

m.c128 = Constraint(expr= - m.x122 + m.x172 >= 0)

m.c129 = Constraint(expr= - m.x124 + m.x173 >= 0)

m.c130 = Constraint(expr= - m.x126 + m.x174 >= 0)

m.c131 = Constraint(expr= - m.x128 + m.x175 >= 0)

m.c132 = Constraint(expr= - 0.6*m.b2 + m.x158 <= 0.2)

m.c133 = Constraint(expr= - 0.6*m.b3 + m.x159 <= 0.2)

m.c134 = Constraint(expr= - 0.6*m.b4 + m.x160 <= 0.2)

m.c135 = Constraint(expr= - 0.6*m.b5 + m.x161 <= 0.2)

m.c136 = Constraint(expr= - 0.6*m.b6 + m.x162 <= 0.2)

m.c137 = Constraint(expr= - 0.6*m.b7 + m.x163 <= 0.2)

m.c138 = Constraint(expr= - 0.25*m.b8 + m.x164 <= 0.25)

m.c139 = Constraint(expr= - 0.25*m.b9 + m.x165 <= 0.25)

m.c140 = Constraint(expr= - 0.25*m.b10 + m.x166 <= 0.25)

m.c141 = Constraint(expr= - 0.25*m.b11 + m.x167 <= 0.25)

m.c142 = Constraint(expr= - 0.3*m.b12 + m.x168 <= 0.4)

m.c143 = Constraint(expr= - 0.3*m.b13 + m.x169 <= 0.4)

m.c144 = Constraint(expr= - 0.3*m.b14 + m.x170 <= 0.4)

m.c145 = Constraint(expr= - 0.3*m.b15 + m.x171 <= 0.4)

m.c146 = Constraint(expr= - 0.34*m.b16 + m.x172 <= 0.24)

m.c147 = Constraint(expr= - 0.34*m.b17 + m.x173 <= 0.24)

m.c148 = Constraint(expr= - 0.34*m.b18 + m.x174 <= 0.24)

m.c149 = Constraint(expr= - 0.34*m.b19 + m.x175 <= 0.24)

m.c150 = Constraint(expr= - 0.4*m.b2 + m.x176 <= 0.6)

m.c151 = Constraint(expr= - 0.4*m.b3 + m.x177 <= 0.6)

m.c152 = Constraint(expr= - 0.2*m.b8 + m.x178 <= 0.8)

m.c153 = Constraint(expr= - 0.2*m.b9 + m.x179 <= 0.8)

m.c154 = Constraint(expr= - 0.15*m.b12 + m.x180 <= 0.85)

m.c155 = Constraint(expr= - 0.15*m.b13 + m.x181 <= 0.85)

m.c156 = Constraint(expr= - 0.3*m.b16 + m.x182 <= 0.7)

m.c157 = Constraint(expr= - 0.3*m.b17 + m.x183 <= 0.7)

m.c158 = Constraint(expr=   m.b2 - m.b4 >= 0)

m.c159 = Constraint(expr=   m.b3 - m.b5 >= 0)

m.c160 = Constraint(expr=   m.b4 - m.b6 >= 0)

m.c161 = Constraint(expr=   m.b5 - m.b7 >= 0)

m.c162 = Constraint(expr=   m.b8 - m.b10 >= 0)

m.c163 = Constraint(expr=   m.b9 - m.b11 >= 0)

m.c164 = Constraint(expr=   m.b12 - m.b14 >= 0)

m.c165 = Constraint(expr=   m.b13 - m.b15 >= 0)

m.c166 = Constraint(expr=   m.b16 - m.b18 >= 0)

m.c167 = Constraint(expr=   m.b17 - m.b19 >= 0)

m.c168 = Constraint(expr=   m.x67 - m.x94 - m.x98 - m.x102 == 0)

m.c169 = Constraint(expr=   m.x69 - m.x96 - m.x100 - m.x104 == 0)

m.c170 = Constraint(expr=   m.x71 - m.x106 - m.x110 - m.x114 - m.x118 == 0)

m.c171 = Constraint(expr=   m.x73 - m.x108 - m.x112 - m.x116 - m.x120 == 0)

m.c172 = Constraint(expr=   m.x77 - m.x122 - m.x126 == 0)

m.c173 = Constraint(expr=   m.x79 - m.x124 - m.x128 == 0)

m.c174 = Constraint(expr= - 2000*m.b2 + m.x95 - m.x151 >= -2000)

m.c175 = Constraint(expr= - 2000*m.b3 + m.x103 - m.x153 >= -2000)

m.c176 = Constraint(expr= - 2000*m.b4 + m.x111 - m.x151 >= -2000)

m.c177 = Constraint(expr= - 2000*m.b5 + m.x117 - m.x153 >= -2000)

m.c178 = Constraint(expr= - 2000*m.b6 + m.x123 - m.x151 >= -2000)

m.c179 = Constraint(expr= - 2000*m.b7 + m.x129 - m.x153 >= -2000)

m.c180 = Constraint(expr= - 2000*m.b8 + m.x22 - m.x154 >= -2000)

m.c181 = Constraint(expr= - 2000*m.b9 + m.x26 - m.x155 >= -2000)

m.c182 = Constraint(expr= - 2000*m.b10 + m.x30 - m.x154 >= -2000)

m.c183 = Constraint(expr= - 2000*m.b11 + m.x33 - m.x155 >= -2000)

m.c184 = Constraint(expr= - 2000*m.b12 + m.x36 - m.x154 >= -2000)

m.c185 = Constraint(expr= - 2000*m.b13 + m.x40 - m.x155 >= -2000)

m.c186 = Constraint(expr= - 2000*m.b14 + m.x44 - m.x154 >= -2000)

m.c187 = Constraint(expr= - 2000*m.b15 + m.x47 - m.x155 >= -2000)

m.c188 = Constraint(expr= - 2000*m.b16 + m.x50 - m.x156 >= -2000)

m.c189 = Constraint(expr= - 2000*m.b17 + m.x54 - m.x157 >= -2000)

m.c190 = Constraint(expr= - 2000*m.b18 + m.x58 - m.x156 >= -2000)

m.c191 = Constraint(expr= - 2000*m.b19 + m.x61 - m.x157 >= -2000)

m.c192 = Constraint(expr=   1049*m.b2 + m.x95 - m.x151 <= 1049)

m.c193 = Constraint(expr=   1049*m.b3 + m.x103 - m.x153 <= 1049)

m.c194 = Constraint(expr=   1049*m.b4 + m.x111 - m.x151 <= 1049)

m.c195 = Constraint(expr=   1049*m.b5 + m.x117 - m.x153 <= 1049)

m.c196 = Constraint(expr=   1049*m.b6 + m.x123 - m.x151 <= 1049)

m.c197 = Constraint(expr=   1049*m.b7 + m.x129 - m.x153 <= 1049)

m.c198 = Constraint(expr=   1065*m.b8 + m.x22 - m.x154 <= 1065)

m.c199 = Constraint(expr=   1065*m.b9 + m.x26 - m.x155 <= 1065)

m.c200 = Constraint(expr=   1065*m.b10 + m.x30 - m.x154 <= 1065)

m.c201 = Constraint(expr=   1065*m.b11 + m.x33 - m.x155 <= 1065)

m.c202 = Constraint(expr=   1065*m.b12 + m.x36 - m.x154 <= 1065)

m.c203 = Constraint(expr=   1065*m.b13 + m.x40 - m.x155 <= 1065)

m.c204 = Constraint(expr=   1065*m.b14 + m.x44 - m.x154 <= 1065)

m.c205 = Constraint(expr=   1065*m.b15 + m.x47 - m.x155 <= 1065)

m.c206 = Constraint(expr=   1095*m.b16 + m.x50 - m.x156 <= 1095)

m.c207 = Constraint(expr=   1095*m.b17 + m.x54 - m.x157 <= 1095)

m.c208 = Constraint(expr=   1095*m.b18 + m.x58 - m.x156 <= 1095)

m.c209 = Constraint(expr=   1095*m.b19 + m.x61 - m.x157 <= 1095)

m.c210 = Constraint(expr= - m.x132 + m.x141 >= 0)

m.c211 = Constraint(expr= - m.x133 + m.x144 >= 0)

m.c212 = Constraint(expr=   m.x134 - m.x184 >= 0)

m.c213 = Constraint(expr=   m.x135 - m.x185 >= 0)

m.c214 = Constraint(expr= - 7.28623839*m.x186 - 23.57687014*m.x187 - 0.309838295393634*m.x188 + 13.94696158*m.x189
                          + 24.46510819*m.x190 <= 0)

m.c215 = Constraint(expr=   13.94696158*m.x191 + 24.46510819*m.x192 - 7.28623839*m.x193 - 23.57687014*m.x194
                          - 0.309838295393634*m.x195 <= 0)

m.c216 = Constraint(expr= - 0.309838295393634*m.x196 + 13.94696158*m.x197 + 24.46510819*m.x198 - 7.28623839*m.x199
                          - 23.57687014*m.x200 <= 0)

m.c217 = Constraint(expr= - 23.57687014*m.x201 - 0.309838295393634*m.x202 + 13.94696158*m.x203 + 24.46510819*m.x204
                          - 7.28623839*m.x205 <= 0)

m.c218 = Constraint(expr= - 0.309838295393634*m.x206 + 13.94696158*m.x207 + 24.46510819*m.x208 - 7.28623839*m.x209
                          - 23.57687014*m.x210 <= 0)

m.c219 = Constraint(expr= - 0.309838295393634*m.x211 + 13.94696158*m.x212 + 24.46510819*m.x213 - 7.28623839*m.x214
                          - 23.57687014*m.x215 <= 0)

m.c220 = Constraint(expr= - 0.309838295393634*m.x216 + 29.29404529*m.x217 - 108.39408287*m.x218 + 442.21990639*m.x219
                          - 454.58448169*m.x220 <= 0)

m.c221 = Constraint(expr= - 0.309838295393634*m.x221 + 29.29404529*m.x222 - 108.39408287*m.x223 + 442.21990639*m.x224
                          - 454.58448169*m.x225 <= 0)

m.c222 = Constraint(expr= - 0.309838295393634*m.x226 + 29.29404529*m.x227 - 108.39408287*m.x228 + 442.21990639*m.x229
                          - 454.58448169*m.x230 <= 0)

m.c223 = Constraint(expr= - 0.309838295393634*m.x231 + 29.29404529*m.x232 - 108.39408287*m.x233 + 442.21990639*m.x234
                          - 454.58448169*m.x235 <= 0)

m.c224 = Constraint(expr= - 0.309838295393634*m.x236 + 25.92674585*m.x237 + 18.13482123*m.x238 + 22.12766012*m.x239
                          - 42.68950769*m.x240 <= 0)

m.c225 = Constraint(expr= - 0.309838295393634*m.x241 + 25.92674585*m.x242 + 18.13482123*m.x243 + 22.12766012*m.x244
                          - 42.68950769*m.x245 <= 0)

m.c226 = Constraint(expr= - 0.309838295393634*m.x246 + 25.92674585*m.x247 + 18.13482123*m.x248 + 22.12766012*m.x249
                          - 42.68950769*m.x250 <= 0)

m.c227 = Constraint(expr= - 0.309838295393634*m.x251 + 25.92674585*m.x252 + 18.13482123*m.x253 + 22.12766012*m.x254
                          - 42.68950769*m.x255 <= 0)

m.c228 = Constraint(expr= - 0.309838295393634*m.x256 + 17.4714791*m.x257 - 39.98407808*m.x258 + 134.55943082*m.x259
                          - 135.88441782*m.x260 <= 0)

m.c229 = Constraint(expr= - 0.309838295393634*m.x261 + 17.4714791*m.x262 - 39.98407808*m.x263 + 134.55943082*m.x264
                          - 135.88441782*m.x265 <= 0)

m.c230 = Constraint(expr= - 0.309838295393634*m.x266 + 17.4714791*m.x267 - 39.98407808*m.x268 + 134.55943082*m.x269
                          - 135.88441782*m.x270 <= 0)

m.c231 = Constraint(expr= - 135.88441782*m.x271 - 0.309838295393634*m.x272 + 17.4714791*m.x273 - 39.98407808*m.x274
                          + 134.55943082*m.x275 <= 0)

m.c232 = Constraint(expr=m.x66**2 - m.x276 == 0)

m.c233 = Constraint(expr=   m.x137 - 5*m.x276 == 0)

m.c234 = Constraint(expr=m.x68**2 - m.x277 == 0)

m.c235 = Constraint(expr=   m.x139 - 5*m.x277 == 0)

m.c236 = Constraint(expr=m.x70**2 - m.x278 == 0)

m.c237 = Constraint(expr=   m.x142 - 4*m.x278 == 0)

m.c238 = Constraint(expr=m.x72**2 - m.x279 == 0)

m.c239 = Constraint(expr=   m.x145 - 4*m.x279 == 0)

m.c240 = Constraint(expr=m.x76**2 - m.x280 == 0)

m.c241 = Constraint(expr=   m.x147 - 5*m.x280 == 0)

m.c242 = Constraint(expr=m.x78**2 - m.x281 == 0)

m.c243 = Constraint(expr=   m.x149 - 5*m.x281 == 0)

m.c244 = Constraint(expr=m.x94**2 - m.x282 == 0)

m.c245 = Constraint(expr=   m.x97 - m.x282 == 0)

m.c246 = Constraint(expr=m.x94**3 - m.x283 == 0)

m.c247 = Constraint(expr=   m.x187 - m.x283 == 0)

m.c248 = Constraint(expr=m.x96**2 - m.x284 == 0)

m.c249 = Constraint(expr=   m.x107 - m.x284 == 0)

m.c250 = Constraint(expr=m.x96**3 - m.x285 == 0)

m.c251 = Constraint(expr=   m.x194 - m.x285 == 0)

m.c252 = Constraint(expr=m.x98**2 - m.x286 == 0)

m.c253 = Constraint(expr=   m.x113 - m.x286 == 0)

m.c254 = Constraint(expr=m.x98**3 - m.x287 == 0)

m.c255 = Constraint(expr=   m.x200 - m.x287 == 0)

m.c256 = Constraint(expr=m.x100**2 - m.x288 == 0)

m.c257 = Constraint(expr=   m.x121 - m.x288 == 0)

m.c258 = Constraint(expr=m.x100**3 - m.x289 == 0)

m.c259 = Constraint(expr=   m.x201 - m.x289 == 0)

m.c260 = Constraint(expr=m.x102**2 - m.x290 == 0)

m.c261 = Constraint(expr=   m.x125 - m.x290 == 0)

m.c262 = Constraint(expr=m.x102**3 - m.x291 == 0)

m.c263 = Constraint(expr=   m.x210 - m.x291 == 0)

m.c264 = Constraint(expr=m.x104**2 - m.x292 == 0)

m.c265 = Constraint(expr=   m.x20 - m.x292 == 0)

m.c266 = Constraint(expr=m.x104**3 - m.x293 == 0)

m.c267 = Constraint(expr=   m.x215 - m.x293 == 0)

m.c268 = Constraint(expr=m.x106**2 - m.x294 == 0)

m.c269 = Constraint(expr=   m.x25 - m.x294 == 0)

m.c270 = Constraint(expr=m.x106**3 - m.x295 == 0)

m.c271 = Constraint(expr=   m.x220 - m.x295 == 0)

m.c272 = Constraint(expr=m.x108**2 - m.x296 == 0)

m.c273 = Constraint(expr=   m.x29 - m.x296 == 0)

m.c274 = Constraint(expr=m.x108**3 - m.x297 == 0)

m.c275 = Constraint(expr=   m.x225 - m.x297 == 0)

m.c276 = Constraint(expr=m.x110**2 - m.x298 == 0)

m.c277 = Constraint(expr=   m.x31 - m.x298 == 0)

m.c278 = Constraint(expr=m.x110**3 - m.x299 == 0)

m.c279 = Constraint(expr=   m.x230 - m.x299 == 0)

m.c280 = Constraint(expr=m.x112**2 - m.x300 == 0)

m.c281 = Constraint(expr=   m.x34 - m.x300 == 0)

m.c282 = Constraint(expr=m.x112**3 - m.x301 == 0)

m.c283 = Constraint(expr=   m.x235 - m.x301 == 0)

m.c284 = Constraint(expr=m.x114**2 - m.x302 == 0)

m.c285 = Constraint(expr=   m.x39 - m.x302 == 0)

m.c286 = Constraint(expr=m.x114**3 - m.x303 == 0)

m.c287 = Constraint(expr=   m.x240 - m.x303 == 0)

m.c288 = Constraint(expr=m.x116**2 - m.x304 == 0)

m.c289 = Constraint(expr=   m.x41 - m.x304 == 0)

m.c290 = Constraint(expr=m.x116**3 - m.x305 == 0)

m.c291 = Constraint(expr=   m.x245 - m.x305 == 0)

m.c292 = Constraint(expr=m.x118**2 - m.x306 == 0)

m.c293 = Constraint(expr=   m.x45 - m.x306 == 0)

m.c294 = Constraint(expr=m.x118**3 - m.x307 == 0)

m.c295 = Constraint(expr=   m.x250 - m.x307 == 0)

m.c296 = Constraint(expr=m.x120**2 - m.x308 == 0)

m.c297 = Constraint(expr=   m.x48 - m.x308 == 0)

m.c298 = Constraint(expr=m.x120**3 - m.x309 == 0)

m.c299 = Constraint(expr=   m.x255 - m.x309 == 0)

m.c300 = Constraint(expr=m.x122**2 - m.x310 == 0)

m.c301 = Constraint(expr=   m.x51 - m.x310 == 0)

m.c302 = Constraint(expr=m.x122**3 - m.x311 == 0)

m.c303 = Constraint(expr=   m.x260 - m.x311 == 0)

m.c304 = Constraint(expr=m.x124**2 - m.x312 == 0)

m.c305 = Constraint(expr=   m.x57 - m.x312 == 0)

m.c306 = Constraint(expr=m.x124**3 - m.x313 == 0)

m.c307 = Constraint(expr=   m.x265 - m.x313 == 0)

m.c308 = Constraint(expr=m.x126**2 - m.x314 == 0)

m.c309 = Constraint(expr=   m.x59 - m.x314 == 0)

m.c310 = Constraint(expr=m.x126**3 - m.x315 == 0)

m.c311 = Constraint(expr=   m.x270 - m.x315 == 0)

m.c312 = Constraint(expr=m.x128**2 - m.x316 == 0)

m.c313 = Constraint(expr=   m.x62 - m.x316 == 0)

m.c314 = Constraint(expr=m.x128**3 - m.x317 == 0)

m.c315 = Constraint(expr=   m.x271 - m.x317 == 0)

m.c316 = Constraint(expr=m.x94*m.x176 - m.x101 == 0)

m.c317 = Constraint(expr=m.x176*m.x282 - m.x186 == 0)

m.c318 = Constraint(expr=m.x98*m.x176 - m.x115 == 0)

m.c319 = Constraint(expr=m.x176*m.x286 - m.x199 == 0)

m.c320 = Constraint(expr=m.x102*m.x176 - m.x127 == 0)

m.c321 = Constraint(expr=m.x176*m.x290 - m.x209 == 0)

m.c322 = Constraint(expr=m.x176**2 - m.x318 == 0)

m.c323 = Constraint(expr=   m.x99 - m.x318 == 0)

m.c324 = Constraint(expr=m.x94*m.x318 - m.x190 == 0)

m.c325 = Constraint(expr=m.x98*m.x318 - m.x198 == 0)

m.c326 = Constraint(expr=m.x102*m.x318 - m.x208 == 0)

m.c327 = Constraint(expr=m.x176**3 - m.x319 == 0)

m.c328 = Constraint(expr=m.b2*m.x319 - m.x189 == 0)

m.c329 = Constraint(expr=m.b4*m.x319 - m.x197 == 0)

m.c330 = Constraint(expr=m.b6*m.x319 - m.x207 == 0)

m.c331 = Constraint(expr=m.x96*m.x177 - m.x105 == 0)

m.c332 = Constraint(expr=m.x177*m.x284 - m.x193 == 0)

m.c333 = Constraint(expr=m.x100*m.x177 - m.x119 == 0)

m.c334 = Constraint(expr=m.x177*m.x288 - m.x205 == 0)

m.c335 = Constraint(expr=m.x104*m.x177 - m.x21 == 0)

m.c336 = Constraint(expr=m.x177*m.x292 - m.x214 == 0)

m.c337 = Constraint(expr=m.x177**2 - m.x320 == 0)

m.c338 = Constraint(expr=   m.x109 - m.x320 == 0)

m.c339 = Constraint(expr=m.x96*m.x320 - m.x192 == 0)

m.c340 = Constraint(expr=m.x100*m.x320 - m.x204 == 0)

m.c341 = Constraint(expr=m.x104*m.x320 - m.x213 == 0)

m.c342 = Constraint(expr=m.x177**3 - m.x321 == 0)

m.c343 = Constraint(expr=m.b3*m.x321 - m.x191 == 0)

m.c344 = Constraint(expr=m.b5*m.x321 - m.x203 == 0)

m.c345 = Constraint(expr=m.b7*m.x321 - m.x212 == 0)

m.c346 = Constraint(expr=m.x106*m.x178 - m.x24 == 0)

m.c347 = Constraint(expr=m.x178*m.x294 - m.x219 == 0)

m.c348 = Constraint(expr=m.x110*m.x178 - m.x32 == 0)

m.c349 = Constraint(expr=m.x178*m.x298 - m.x229 == 0)

m.c350 = Constraint(expr=m.x178**2 - m.x322 == 0)

m.c351 = Constraint(expr=   m.x23 - m.x322 == 0)

m.c352 = Constraint(expr=m.x106*m.x322 - m.x218 == 0)

m.c353 = Constraint(expr=m.x110*m.x322 - m.x228 == 0)

m.c354 = Constraint(expr=m.x178**3 - m.x323 == 0)

m.c355 = Constraint(expr=m.b8*m.x323 - m.x217 == 0)

m.c356 = Constraint(expr=m.b10*m.x323 - m.x227 == 0)

m.c357 = Constraint(expr=m.x108*m.x179 - m.x27 == 0)

m.c358 = Constraint(expr=m.x179*m.x296 - m.x224 == 0)

m.c359 = Constraint(expr=m.x112*m.x179 - m.x35 == 0)

m.c360 = Constraint(expr=m.x179*m.x300 - m.x234 == 0)

m.c361 = Constraint(expr=m.x179**2 - m.x324 == 0)

m.c362 = Constraint(expr=   m.x28 - m.x324 == 0)

m.c363 = Constraint(expr=m.x108*m.x324 - m.x223 == 0)

m.c364 = Constraint(expr=m.x112*m.x324 - m.x233 == 0)

m.c365 = Constraint(expr=m.x179**3 - m.x325 == 0)

m.c366 = Constraint(expr=m.b9*m.x325 - m.x222 == 0)

m.c367 = Constraint(expr=m.b11*m.x325 - m.x232 == 0)

m.c368 = Constraint(expr=m.x114*m.x180 - m.x38 == 0)

m.c369 = Constraint(expr=m.x180*m.x302 - m.x239 == 0)

m.c370 = Constraint(expr=m.x118*m.x180 - m.x46 == 0)

m.c371 = Constraint(expr=m.x180*m.x306 - m.x249 == 0)

m.c372 = Constraint(expr=m.x180**2 - m.x326 == 0)

m.c373 = Constraint(expr=   m.x37 - m.x326 == 0)

m.c374 = Constraint(expr=m.x114*m.x326 - m.x238 == 0)

m.c375 = Constraint(expr=m.x118*m.x326 - m.x248 == 0)

m.c376 = Constraint(expr=m.x180**3 - m.x327 == 0)

m.c377 = Constraint(expr=m.b12*m.x327 - m.x237 == 0)

m.c378 = Constraint(expr=m.b14*m.x327 - m.x247 == 0)

m.c379 = Constraint(expr=m.x116*m.x181 - m.x42 == 0)

m.c380 = Constraint(expr=m.x181*m.x304 - m.x244 == 0)

m.c381 = Constraint(expr=m.x120*m.x181 - m.x49 == 0)

m.c382 = Constraint(expr=m.x181*m.x308 - m.x254 == 0)

m.c383 = Constraint(expr=m.x181**2 - m.x328 == 0)

m.c384 = Constraint(expr=   m.x43 - m.x328 == 0)

m.c385 = Constraint(expr=m.x116*m.x328 - m.x243 == 0)

m.c386 = Constraint(expr=m.x120*m.x328 - m.x253 == 0)

m.c387 = Constraint(expr=m.x181**3 - m.x329 == 0)

m.c388 = Constraint(expr=m.b13*m.x329 - m.x242 == 0)

m.c389 = Constraint(expr=m.b15*m.x329 - m.x252 == 0)

m.c390 = Constraint(expr=m.x122*m.x182 - m.x53 == 0)

m.c391 = Constraint(expr=m.x182*m.x310 - m.x259 == 0)

m.c392 = Constraint(expr=m.x126*m.x182 - m.x60 == 0)

m.c393 = Constraint(expr=m.x182*m.x314 - m.x269 == 0)

m.c394 = Constraint(expr=m.x182**2 - m.x330 == 0)

m.c395 = Constraint(expr=   m.x52 - m.x330 == 0)

m.c396 = Constraint(expr=m.x122*m.x330 - m.x258 == 0)

m.c397 = Constraint(expr=m.x126*m.x330 - m.x268 == 0)

m.c398 = Constraint(expr=m.x182**3 - m.x331 == 0)

m.c399 = Constraint(expr=m.b16*m.x331 - m.x257 == 0)

m.c400 = Constraint(expr=m.b18*m.x331 - m.x267 == 0)

m.c401 = Constraint(expr=m.x124*m.x183 - m.x56 == 0)

m.c402 = Constraint(expr=m.x183*m.x312 - m.x264 == 0)

m.c403 = Constraint(expr=m.x128*m.x183 - m.x63 == 0)

m.c404 = Constraint(expr=m.x183*m.x316 - m.x275 == 0)

m.c405 = Constraint(expr=m.x183**2 - m.x332 == 0)

m.c406 = Constraint(expr=   m.x55 - m.x332 == 0)

m.c407 = Constraint(expr=m.x124*m.x332 - m.x263 == 0)

m.c408 = Constraint(expr=m.x128*m.x332 - m.x274 == 0)

m.c409 = Constraint(expr=m.x183**3 - m.x333 == 0)

m.c410 = Constraint(expr=m.b17*m.x333 - m.x262 == 0)

m.c411 = Constraint(expr=m.b19*m.x333 - m.x273 == 0)
