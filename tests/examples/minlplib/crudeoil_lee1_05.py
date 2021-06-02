#  MINLP written by GAMS Convert at 04/21/18 13:51:16
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       1241      452      288      501        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        536      496       40        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       4787     4147      640        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b2 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b15 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b18 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b19 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b21 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b23 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b24 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b25 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b26 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b27 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b28 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b29 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b30 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b31 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b32 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b33 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b34 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b35 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b36 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b38 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b39 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b40 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b41 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x58 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x60 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x61 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x62 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x63 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x64 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x65 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x66 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x67 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x68 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x69 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x70 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x71 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x72 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x73 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x74 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x75 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x76 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x77 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x78 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x79 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x80 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x81 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x82 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x83 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x84 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x85 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x86 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x87 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x88 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x89 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x90 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x91 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x92 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x93 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x95 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x96 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x97 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x98 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x100 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x101 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x102 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x103 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x104 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x105 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x106 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x107 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x108 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x109 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x110 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x111 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x112 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x113 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x114 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x115 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x116 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x117 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x118 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x119 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x120 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x121 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x122 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x123 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x124 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x125 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x126 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x127 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x128 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x129 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x130 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x131 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x132 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x133 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x134 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x135 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x136 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x137 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x138 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x139 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x140 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x141 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x142 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x143 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x144 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x145 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x146 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x147 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x148 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x149 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x150 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x151 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x152 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x153 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x154 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x155 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x156 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x157 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x158 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x159 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x160 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x161 = Var(within=Reals,bounds=(0,None),initialize=2.66666666666667)
m.x162 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x163 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x164 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x165 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x166 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x167 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x168 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x169 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x170 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x171 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x172 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x173 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x174 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x175 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x176 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x177 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x178 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x179 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x180 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x181 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x182 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x183 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x184 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x185 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x186 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x187 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x188 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x189 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x190 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x191 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x192 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x193 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x194 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x195 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x196 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x197 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x198 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x199 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x200 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x201 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x202 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x203 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x204 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x205 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x206 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x207 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x208 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x209 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x210 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x211 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x212 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x213 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x214 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x215 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x216 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x217 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x218 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x219 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x220 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x221 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x222 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x223 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x224 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x225 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x226 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x227 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x228 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x229 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x230 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x231 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x232 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x233 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x234 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x235 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x236 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x237 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x238 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x239 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x240 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x241 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x242 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x243 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x244 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x245 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x246 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x247 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x248 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x249 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x250 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x251 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x252 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x253 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x254 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x255 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x256 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x257 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x258 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x259 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x260 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x261 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x262 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x263 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x264 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x265 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x266 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x267 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x268 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x269 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x270 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x271 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x272 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x273 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x274 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x275 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x276 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x277 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x278 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x279 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x280 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x281 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x282 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x283 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x284 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x285 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x286 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x287 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x288 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x289 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x290 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x291 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x292 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x293 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x294 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x295 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x296 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x297 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x298 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x299 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x300 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x301 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x302 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x303 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x304 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x305 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x306 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x307 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x308 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x309 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x310 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x311 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x312 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x313 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x314 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x315 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x316 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x317 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x318 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x319 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x320 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x321 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x322 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x323 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x324 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x325 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x326 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x327 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x328 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x329 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x330 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x331 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x332 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x333 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x334 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x335 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x336 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x337 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x338 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x339 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x340 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x341 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x342 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x343 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x344 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x345 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x346 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x347 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x348 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x349 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x350 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x351 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x352 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x353 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x354 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x355 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x356 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x357 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x358 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x359 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x360 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x361 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x362 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x363 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x364 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x365 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x366 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x367 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x368 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x369 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x370 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x371 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x372 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x373 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x374 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x375 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x376 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x377 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x378 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x379 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x380 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x381 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x382 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x383 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x384 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x385 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x386 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x387 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x388 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x389 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x390 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x391 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x392 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x393 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x394 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x395 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x396 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x397 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x398 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x399 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x400 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x401 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x402 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x403 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x404 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x405 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x406 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x407 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x408 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x409 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x410 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x411 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x412 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x413 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x414 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x415 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x416 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x417 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x418 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x419 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x420 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x421 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x422 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x423 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x424 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x425 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x426 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x427 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x428 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x429 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x430 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x431 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x432 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x433 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x434 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x435 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x436 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x437 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x438 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x439 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x440 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x441 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x442 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x443 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x444 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x445 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x446 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x447 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x448 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x449 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x450 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x451 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x452 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x453 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x454 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x455 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x456 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x457 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x458 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x459 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x460 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x461 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x462 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x463 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x464 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x465 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x466 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x467 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x468 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x469 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x470 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x471 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x472 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x473 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x474 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x475 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x476 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x477 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x478 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x479 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x480 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x481 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x482 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x483 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x484 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x485 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x486 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x487 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x488 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x489 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x490 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x491 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x492 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x493 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x494 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x495 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x496 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x497 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x498 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x499 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x500 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x501 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x502 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x503 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x504 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x505 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x506 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x507 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x508 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x509 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x510 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x511 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x512 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x513 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x514 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x515 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x516 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x517 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x518 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x519 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x520 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x521 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x522 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x523 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x524 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x525 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x526 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x527 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x528 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x529 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x530 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x531 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x532 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x533 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x534 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x535 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x536 = Var(within=Reals,bounds=(0,None),initialize=2.5)

m.obj = Objective(expr=   0.1*m.x226 + 0.6*m.x227 + 0.2*m.x228 + 0.5*m.x229 + 0.1*m.x230 + 0.6*m.x231 + 0.2*m.x232
                        + 0.5*m.x233 + 0.1*m.x258 + 0.6*m.x259 + 0.2*m.x260 + 0.5*m.x261 + 0.1*m.x262 + 0.6*m.x263
                        + 0.2*m.x264 + 0.5*m.x265 + 0.1*m.x290 + 0.6*m.x291 + 0.2*m.x292 + 0.5*m.x293 + 0.1*m.x294
                        + 0.6*m.x295 + 0.2*m.x296 + 0.5*m.x297 + 0.1*m.x322 + 0.6*m.x323 + 0.2*m.x324 + 0.5*m.x325
                        + 0.1*m.x326 + 0.6*m.x327 + 0.2*m.x328 + 0.5*m.x329 + 0.1*m.x354 + 0.6*m.x355 + 0.2*m.x356
                        + 0.5*m.x357 + 0.1*m.x358 + 0.6*m.x359 + 0.2*m.x360 + 0.5*m.x361, sense=maximize)

m.c2 = Constraint(expr=   m.b2 + m.b3 <= 1)

m.c3 = Constraint(expr=   m.b2 + m.b4 <= 1)

m.c4 = Constraint(expr=   m.b2 + m.b5 <= 1)

m.c5 = Constraint(expr=   m.b3 + m.b6 <= 1)

m.c6 = Constraint(expr=   m.b3 + m.b7 <= 1)

m.c7 = Constraint(expr=   m.b4 + m.b8 <= 1)

m.c8 = Constraint(expr=   m.b5 + m.b9 <= 1)

m.c9 = Constraint(expr=   m.b6 + m.b8 <= 1)

m.c10 = Constraint(expr=   m.b7 + m.b9 <= 1)

m.c11 = Constraint(expr=   m.b8 + m.b9 <= 1)

m.c12 = Constraint(expr=   m.b10 + m.b11 <= 1)

m.c13 = Constraint(expr=   m.b10 + m.b12 <= 1)

m.c14 = Constraint(expr=   m.b10 + m.b13 <= 1)

m.c15 = Constraint(expr=   m.b11 + m.b14 <= 1)

m.c16 = Constraint(expr=   m.b11 + m.b15 <= 1)

m.c17 = Constraint(expr=   m.b12 + m.b16 <= 1)

m.c18 = Constraint(expr=   m.b13 + m.b17 <= 1)

m.c19 = Constraint(expr=   m.b14 + m.b16 <= 1)

m.c20 = Constraint(expr=   m.b15 + m.b17 <= 1)

m.c21 = Constraint(expr=   m.b16 + m.b17 <= 1)

m.c22 = Constraint(expr=   m.b18 + m.b19 <= 1)

m.c23 = Constraint(expr=   m.b18 + m.b20 <= 1)

m.c24 = Constraint(expr=   m.b18 + m.b21 <= 1)

m.c25 = Constraint(expr=   m.b19 + m.b22 <= 1)

m.c26 = Constraint(expr=   m.b19 + m.b23 <= 1)

m.c27 = Constraint(expr=   m.b20 + m.b24 <= 1)

m.c28 = Constraint(expr=   m.b21 + m.b25 <= 1)

m.c29 = Constraint(expr=   m.b22 + m.b24 <= 1)

m.c30 = Constraint(expr=   m.b23 + m.b25 <= 1)

m.c31 = Constraint(expr=   m.b24 + m.b25 <= 1)

m.c32 = Constraint(expr=   m.b26 + m.b27 <= 1)

m.c33 = Constraint(expr=   m.b26 + m.b28 <= 1)

m.c34 = Constraint(expr=   m.b26 + m.b29 <= 1)

m.c35 = Constraint(expr=   m.b27 + m.b30 <= 1)

m.c36 = Constraint(expr=   m.b27 + m.b31 <= 1)

m.c37 = Constraint(expr=   m.b28 + m.b32 <= 1)

m.c38 = Constraint(expr=   m.b29 + m.b33 <= 1)

m.c39 = Constraint(expr=   m.b30 + m.b32 <= 1)

m.c40 = Constraint(expr=   m.b31 + m.b33 <= 1)

m.c41 = Constraint(expr=   m.b32 + m.b33 <= 1)

m.c42 = Constraint(expr=   m.b34 + m.b35 <= 1)

m.c43 = Constraint(expr=   m.b34 + m.b36 <= 1)

m.c44 = Constraint(expr=   m.b34 + m.b37 <= 1)

m.c45 = Constraint(expr=   m.b35 + m.b38 <= 1)

m.c46 = Constraint(expr=   m.b35 + m.b39 <= 1)

m.c47 = Constraint(expr=   m.b36 + m.b40 <= 1)

m.c48 = Constraint(expr=   m.b37 + m.b41 <= 1)

m.c49 = Constraint(expr=   m.b38 + m.b40 <= 1)

m.c50 = Constraint(expr=   m.b39 + m.b41 <= 1)

m.c51 = Constraint(expr=   m.b40 + m.b41 <= 1)

m.c52 = Constraint(expr=   m.b2 + m.b10 + m.b18 + m.b26 + m.b34 >= 1)

m.c53 = Constraint(expr=   m.b3 + m.b11 + m.b19 + m.b27 + m.b35 >= 1)

m.c54 = Constraint(expr=   m.b8 + m.b16 + m.b24 + m.b32 + m.b40 >= 1)

m.c55 = Constraint(expr=   m.b9 + m.b17 + m.b25 + m.b33 + m.b41 >= 1)

m.c56 = Constraint(expr=   m.b8 + m.b9 + m.b16 + m.b17 + m.b24 + m.b25 + m.b32 + m.b33 + m.b40 + m.b41 >= 3)

m.c57 = Constraint(expr=   m.b2 + m.b10 + m.b18 + m.b26 + m.b34 <= 1)

m.c58 = Constraint(expr=   m.b3 + m.b11 + m.b19 + m.b27 + m.b35 <= 1)

m.c59 = Constraint(expr=   m.b8 + m.b16 + m.b24 + m.b32 + m.b40 <= 2)

m.c60 = Constraint(expr=   m.b9 + m.b17 + m.b25 + m.b33 + m.b41 <= 2)

m.c61 = Constraint(expr=   m.b8 + m.b9 + m.b16 + m.b17 + m.b24 + m.b25 + m.b32 + m.b33 + m.b40 + m.b41 <= 3)

m.c62 = Constraint(expr=   m.b8 + m.b9 >= 1)

m.c63 = Constraint(expr=   m.b8 + m.b9 <= 1)

m.c64 = Constraint(expr= - m.x43 - m.x51 - m.x59 - m.x67 - m.x75 + m.x122 + m.x130 + m.x138 + m.x146 + m.x154 <= 0)

m.c65 = Constraint(expr= - m.b3 >= 0)

m.c66 = Constraint(expr=   m.b2 - m.b3 - m.b11 >= 0)

m.c67 = Constraint(expr=   m.b2 - m.b3 + m.b10 - m.b11 - m.b19 >= 0)

m.c68 = Constraint(expr=   m.b2 - m.b3 + m.b10 - m.b11 + m.b18 - m.b19 - m.b27 >= 0)

m.c69 = Constraint(expr=   m.b2 - m.b3 + m.b10 - m.b11 + m.b18 - m.b19 + m.b26 - m.b27 - m.b35 >= 0)

m.c70 = Constraint(expr= - m.x42 - m.x82 + m.x122 == 0)

m.c71 = Constraint(expr= - m.x43 - m.x83 + m.x123 == 0)

m.c72 = Constraint(expr= - m.x44 - m.x84 + m.x124 == 0)

m.c73 = Constraint(expr= - m.x45 - m.x85 + m.x125 == 0)

m.c74 = Constraint(expr= - m.x46 - m.x86 + m.x126 == 0)

m.c75 = Constraint(expr= - m.x47 - m.x87 + m.x127 == 0)

m.c76 = Constraint(expr= - m.x48 - m.x88 + m.x128 == 0)

m.c77 = Constraint(expr= - m.x49 - m.x89 + m.x129 == 0)

m.c78 = Constraint(expr= - m.x50 - m.x90 + m.x130 == 0)

m.c79 = Constraint(expr= - m.x51 - m.x91 + m.x131 == 0)

m.c80 = Constraint(expr= - m.x52 - m.x92 + m.x132 == 0)

m.c81 = Constraint(expr= - m.x53 - m.x93 + m.x133 == 0)

m.c82 = Constraint(expr= - m.x54 - m.x94 + m.x134 == 0)

m.c83 = Constraint(expr= - m.x55 - m.x95 + m.x135 == 0)

m.c84 = Constraint(expr= - m.x56 - m.x96 + m.x136 == 0)

m.c85 = Constraint(expr= - m.x57 - m.x97 + m.x137 == 0)

m.c86 = Constraint(expr= - m.x58 - m.x98 + m.x138 == 0)

m.c87 = Constraint(expr= - m.x59 - m.x99 + m.x139 == 0)

m.c88 = Constraint(expr= - m.x60 - m.x100 + m.x140 == 0)

m.c89 = Constraint(expr= - m.x61 - m.x101 + m.x141 == 0)

m.c90 = Constraint(expr= - m.x62 - m.x102 + m.x142 == 0)

m.c91 = Constraint(expr= - m.x63 - m.x103 + m.x143 == 0)

m.c92 = Constraint(expr= - m.x64 - m.x104 + m.x144 == 0)

m.c93 = Constraint(expr= - m.x65 - m.x105 + m.x145 == 0)

m.c94 = Constraint(expr= - m.x66 - m.x106 + m.x146 == 0)

m.c95 = Constraint(expr= - m.x67 - m.x107 + m.x147 == 0)

m.c96 = Constraint(expr= - m.x68 - m.x108 + m.x148 == 0)

m.c97 = Constraint(expr= - m.x69 - m.x109 + m.x149 == 0)

m.c98 = Constraint(expr= - m.x70 - m.x110 + m.x150 == 0)

m.c99 = Constraint(expr= - m.x71 - m.x111 + m.x151 == 0)

m.c100 = Constraint(expr= - m.x72 - m.x112 + m.x152 == 0)

m.c101 = Constraint(expr= - m.x73 - m.x113 + m.x153 == 0)

m.c102 = Constraint(expr= - m.x74 - m.x114 + m.x154 == 0)

m.c103 = Constraint(expr= - m.x75 - m.x115 + m.x155 == 0)

m.c104 = Constraint(expr= - m.x76 - m.x116 + m.x156 == 0)

m.c105 = Constraint(expr= - m.x77 - m.x117 + m.x157 == 0)

m.c106 = Constraint(expr= - m.x78 - m.x118 + m.x158 == 0)

m.c107 = Constraint(expr= - m.x79 - m.x119 + m.x159 == 0)

m.c108 = Constraint(expr= - m.x80 - m.x120 + m.x160 == 0)

m.c109 = Constraint(expr= - m.x81 - m.x121 + m.x161 == 0)

m.c110 = Constraint(expr=   m.x42 >= 0)

m.c111 = Constraint(expr= - 4*m.b3 + m.x43 >= 0)

m.c112 = Constraint(expr=   m.x44 >= 0)

m.c113 = Constraint(expr=   m.x45 >= 0)

m.c114 = Constraint(expr=   m.x46 >= 0)

m.c115 = Constraint(expr=   m.x47 >= 0)

m.c116 = Constraint(expr=   m.x48 >= 0)

m.c117 = Constraint(expr=   m.x49 >= 0)

m.c118 = Constraint(expr=   m.x50 >= 0)

m.c119 = Constraint(expr= - 4*m.b11 + m.x51 >= 0)

m.c120 = Constraint(expr=   m.x52 >= 0)

m.c121 = Constraint(expr=   m.x53 >= 0)

m.c122 = Constraint(expr=   m.x54 >= 0)

m.c123 = Constraint(expr=   m.x55 >= 0)

m.c124 = Constraint(expr=   m.x56 >= 0)

m.c125 = Constraint(expr=   m.x57 >= 0)

m.c126 = Constraint(expr=   m.x58 >= 0)

m.c127 = Constraint(expr= - 4*m.b19 + m.x59 >= 0)

m.c128 = Constraint(expr=   m.x60 >= 0)

m.c129 = Constraint(expr=   m.x61 >= 0)

m.c130 = Constraint(expr=   m.x62 >= 0)

m.c131 = Constraint(expr=   m.x63 >= 0)

m.c132 = Constraint(expr=   m.x64 >= 0)

m.c133 = Constraint(expr=   m.x65 >= 0)

m.c134 = Constraint(expr=   m.x66 >= 0)

m.c135 = Constraint(expr= - 4*m.b27 + m.x67 >= 0)

m.c136 = Constraint(expr=   m.x68 >= 0)

m.c137 = Constraint(expr=   m.x69 >= 0)

m.c138 = Constraint(expr=   m.x70 >= 0)

m.c139 = Constraint(expr=   m.x71 >= 0)

m.c140 = Constraint(expr=   m.x72 >= 0)

m.c141 = Constraint(expr=   m.x73 >= 0)

m.c142 = Constraint(expr=   m.x74 >= 0)

m.c143 = Constraint(expr= - 4*m.b35 + m.x75 >= 0)

m.c144 = Constraint(expr=   m.x76 >= 0)

m.c145 = Constraint(expr=   m.x77 >= 0)

m.c146 = Constraint(expr=   m.x78 >= 0)

m.c147 = Constraint(expr=   m.x79 >= 0)

m.c148 = Constraint(expr=   m.x80 >= 0)

m.c149 = Constraint(expr=   m.x81 >= 0)

m.c150 = Constraint(expr= - 8*m.b2 + m.x122 <= 0)

m.c151 = Constraint(expr= - 8*m.b3 + m.x123 <= 0)

m.c152 = Constraint(expr= - 8*m.b4 + m.x124 <= 0)

m.c153 = Constraint(expr= - 8*m.b5 + m.x125 <= 0)

m.c154 = Constraint(expr= - 8*m.b6 + m.x126 <= 0)

m.c155 = Constraint(expr= - 8*m.b7 + m.x127 <= 0)

m.c156 = Constraint(expr= - 8*m.b8 + m.x128 <= 0)

m.c157 = Constraint(expr= - 8*m.b9 + m.x129 <= 0)

m.c158 = Constraint(expr= - 8*m.b10 + m.x130 <= 0)

m.c159 = Constraint(expr= - 8*m.b11 + m.x131 <= 0)

m.c160 = Constraint(expr= - 8*m.b12 + m.x132 <= 0)

m.c161 = Constraint(expr= - 8*m.b13 + m.x133 <= 0)

m.c162 = Constraint(expr= - 8*m.b14 + m.x134 <= 0)

m.c163 = Constraint(expr= - 8*m.b15 + m.x135 <= 0)

m.c164 = Constraint(expr= - 8*m.b16 + m.x136 <= 0)

m.c165 = Constraint(expr= - 8*m.b17 + m.x137 <= 0)

m.c166 = Constraint(expr= - 8*m.b18 + m.x138 <= 0)

m.c167 = Constraint(expr= - 8*m.b19 + m.x139 <= 0)

m.c168 = Constraint(expr= - 8*m.b20 + m.x140 <= 0)

m.c169 = Constraint(expr= - 8*m.b21 + m.x141 <= 0)

m.c170 = Constraint(expr= - 8*m.b22 + m.x142 <= 0)

m.c171 = Constraint(expr= - 8*m.b23 + m.x143 <= 0)

m.c172 = Constraint(expr= - 8*m.b24 + m.x144 <= 0)

m.c173 = Constraint(expr= - 8*m.b25 + m.x145 <= 0)

m.c174 = Constraint(expr= - 8*m.b26 + m.x146 <= 0)

m.c175 = Constraint(expr= - 8*m.b27 + m.x147 <= 0)

m.c176 = Constraint(expr= - 8*m.b28 + m.x148 <= 0)

m.c177 = Constraint(expr= - 8*m.b29 + m.x149 <= 0)

m.c178 = Constraint(expr= - 8*m.b30 + m.x150 <= 0)

m.c179 = Constraint(expr= - 8*m.b31 + m.x151 <= 0)

m.c180 = Constraint(expr= - 8*m.b32 + m.x152 <= 0)

m.c181 = Constraint(expr= - 8*m.b33 + m.x153 <= 0)

m.c182 = Constraint(expr= - 8*m.b34 + m.x154 <= 0)

m.c183 = Constraint(expr= - 8*m.b35 + m.x155 <= 0)

m.c184 = Constraint(expr= - 8*m.b36 + m.x156 <= 0)

m.c185 = Constraint(expr= - 8*m.b37 + m.x157 <= 0)

m.c186 = Constraint(expr= - 8*m.b38 + m.x158 <= 0)

m.c187 = Constraint(expr= - 8*m.b39 + m.x159 <= 0)

m.c188 = Constraint(expr= - 8*m.b40 + m.x160 <= 0)

m.c189 = Constraint(expr= - 8*m.b41 + m.x161 <= 0)

m.c190 = Constraint(expr= - 100*m.b2 + m.x162 >= 0)

m.c191 = Constraint(expr= - 100*m.b3 + m.x163 >= 0)

m.c192 = Constraint(expr= - 100*m.b10 + m.x170 >= 0)

m.c193 = Constraint(expr= - 100*m.b11 + m.x171 >= 0)

m.c194 = Constraint(expr= - 100*m.b18 + m.x178 >= 0)

m.c195 = Constraint(expr= - 100*m.b19 + m.x179 >= 0)

m.c196 = Constraint(expr= - 100*m.b26 + m.x186 >= 0)

m.c197 = Constraint(expr= - 100*m.b27 + m.x187 >= 0)

m.c198 = Constraint(expr= - 100*m.b34 + m.x194 >= 0)

m.c199 = Constraint(expr= - 100*m.b35 + m.x195 >= 0)

m.c200 = Constraint(expr= - 100*m.b2 + m.x162 <= 0)

m.c201 = Constraint(expr= - 100*m.b3 + m.x163 <= 0)

m.c202 = Constraint(expr= - 100*m.b4 + m.x164 <= 0)

m.c203 = Constraint(expr= - 100*m.b5 + m.x165 <= 0)

m.c204 = Constraint(expr= - 100*m.b6 + m.x166 <= 0)

m.c205 = Constraint(expr= - 100*m.b7 + m.x167 <= 0)

m.c206 = Constraint(expr= - 100*m.b8 + m.x168 <= 0)

m.c207 = Constraint(expr= - 100*m.b9 + m.x169 <= 0)

m.c208 = Constraint(expr= - 100*m.b10 + m.x170 <= 0)

m.c209 = Constraint(expr= - 100*m.b11 + m.x171 <= 0)

m.c210 = Constraint(expr= - 100*m.b12 + m.x172 <= 0)

m.c211 = Constraint(expr= - 100*m.b13 + m.x173 <= 0)

m.c212 = Constraint(expr= - 100*m.b14 + m.x174 <= 0)

m.c213 = Constraint(expr= - 100*m.b15 + m.x175 <= 0)

m.c214 = Constraint(expr= - 100*m.b16 + m.x176 <= 0)

m.c215 = Constraint(expr= - 100*m.b17 + m.x177 <= 0)

m.c216 = Constraint(expr= - 100*m.b18 + m.x178 <= 0)

m.c217 = Constraint(expr= - 100*m.b19 + m.x179 <= 0)

m.c218 = Constraint(expr= - 100*m.b20 + m.x180 <= 0)

m.c219 = Constraint(expr= - 100*m.b21 + m.x181 <= 0)

m.c220 = Constraint(expr= - 100*m.b22 + m.x182 <= 0)

m.c221 = Constraint(expr= - 100*m.b23 + m.x183 <= 0)

m.c222 = Constraint(expr= - 100*m.b24 + m.x184 <= 0)

m.c223 = Constraint(expr= - 100*m.b25 + m.x185 <= 0)

m.c224 = Constraint(expr= - 100*m.b26 + m.x186 <= 0)

m.c225 = Constraint(expr= - 100*m.b27 + m.x187 <= 0)

m.c226 = Constraint(expr= - 100*m.b28 + m.x188 <= 0)

m.c227 = Constraint(expr= - 100*m.b29 + m.x189 <= 0)

m.c228 = Constraint(expr= - 100*m.b30 + m.x190 <= 0)

m.c229 = Constraint(expr= - 100*m.b31 + m.x191 <= 0)

m.c230 = Constraint(expr= - 100*m.b32 + m.x192 <= 0)

m.c231 = Constraint(expr= - 100*m.b33 + m.x193 <= 0)

m.c232 = Constraint(expr= - 100*m.b34 + m.x194 <= 0)

m.c233 = Constraint(expr= - 100*m.b35 + m.x195 <= 0)

m.c234 = Constraint(expr= - 100*m.b36 + m.x196 <= 0)

m.c235 = Constraint(expr= - 100*m.b37 + m.x197 <= 0)

m.c236 = Constraint(expr= - 100*m.b38 + m.x198 <= 0)

m.c237 = Constraint(expr= - 100*m.b39 + m.x199 <= 0)

m.c238 = Constraint(expr= - 100*m.b40 + m.x200 <= 0)

m.c239 = Constraint(expr= - 100*m.b41 + m.x201 <= 0)

m.c240 = Constraint(expr=   m.x162 - m.x202 - m.x203 - m.x204 - m.x205 == 0)

m.c241 = Constraint(expr=   m.x163 - m.x206 - m.x207 - m.x208 - m.x209 == 0)

m.c242 = Constraint(expr=   m.x164 - m.x210 - m.x211 - m.x212 - m.x213 == 0)

m.c243 = Constraint(expr=   m.x165 - m.x214 - m.x215 - m.x216 - m.x217 == 0)

m.c244 = Constraint(expr=   m.x166 - m.x218 - m.x219 - m.x220 - m.x221 == 0)

m.c245 = Constraint(expr=   m.x167 - m.x222 - m.x223 - m.x224 - m.x225 == 0)

m.c246 = Constraint(expr=   m.x168 - m.x226 - m.x227 - m.x228 - m.x229 == 0)

m.c247 = Constraint(expr=   m.x169 - m.x230 - m.x231 - m.x232 - m.x233 == 0)

m.c248 = Constraint(expr=   m.x170 - m.x234 - m.x235 - m.x236 - m.x237 == 0)

m.c249 = Constraint(expr=   m.x171 - m.x238 - m.x239 - m.x240 - m.x241 == 0)

m.c250 = Constraint(expr=   m.x172 - m.x242 - m.x243 - m.x244 - m.x245 == 0)

m.c251 = Constraint(expr=   m.x173 - m.x246 - m.x247 - m.x248 - m.x249 == 0)

m.c252 = Constraint(expr=   m.x174 - m.x250 - m.x251 - m.x252 - m.x253 == 0)

m.c253 = Constraint(expr=   m.x175 - m.x254 - m.x255 - m.x256 - m.x257 == 0)

m.c254 = Constraint(expr=   m.x176 - m.x258 - m.x259 - m.x260 - m.x261 == 0)

m.c255 = Constraint(expr=   m.x177 - m.x262 - m.x263 - m.x264 - m.x265 == 0)

m.c256 = Constraint(expr=   m.x178 - m.x266 - m.x267 - m.x268 - m.x269 == 0)

m.c257 = Constraint(expr=   m.x179 - m.x270 - m.x271 - m.x272 - m.x273 == 0)

m.c258 = Constraint(expr=   m.x180 - m.x274 - m.x275 - m.x276 - m.x277 == 0)

m.c259 = Constraint(expr=   m.x181 - m.x278 - m.x279 - m.x280 - m.x281 == 0)

m.c260 = Constraint(expr=   m.x182 - m.x282 - m.x283 - m.x284 - m.x285 == 0)

m.c261 = Constraint(expr=   m.x183 - m.x286 - m.x287 - m.x288 - m.x289 == 0)

m.c262 = Constraint(expr=   m.x184 - m.x290 - m.x291 - m.x292 - m.x293 == 0)

m.c263 = Constraint(expr=   m.x185 - m.x294 - m.x295 - m.x296 - m.x297 == 0)

m.c264 = Constraint(expr=   m.x186 - m.x298 - m.x299 - m.x300 - m.x301 == 0)

m.c265 = Constraint(expr=   m.x187 - m.x302 - m.x303 - m.x304 - m.x305 == 0)

m.c266 = Constraint(expr=   m.x188 - m.x306 - m.x307 - m.x308 - m.x309 == 0)

m.c267 = Constraint(expr=   m.x189 - m.x310 - m.x311 - m.x312 - m.x313 == 0)

m.c268 = Constraint(expr=   m.x190 - m.x314 - m.x315 - m.x316 - m.x317 == 0)

m.c269 = Constraint(expr=   m.x191 - m.x318 - m.x319 - m.x320 - m.x321 == 0)

m.c270 = Constraint(expr=   m.x192 - m.x322 - m.x323 - m.x324 - m.x325 == 0)

m.c271 = Constraint(expr=   m.x193 - m.x326 - m.x327 - m.x328 - m.x329 == 0)

m.c272 = Constraint(expr=   m.x194 - m.x330 - m.x331 - m.x332 - m.x333 == 0)

m.c273 = Constraint(expr=   m.x195 - m.x334 - m.x335 - m.x336 - m.x337 == 0)

m.c274 = Constraint(expr=   m.x196 - m.x338 - m.x339 - m.x340 - m.x341 == 0)

m.c275 = Constraint(expr=   m.x197 - m.x342 - m.x343 - m.x344 - m.x345 == 0)

m.c276 = Constraint(expr=   m.x198 - m.x346 - m.x347 - m.x348 - m.x349 == 0)

m.c277 = Constraint(expr=   m.x199 - m.x350 - m.x351 - m.x352 - m.x353 == 0)

m.c278 = Constraint(expr=   m.x200 - m.x354 - m.x355 - m.x356 - m.x357 == 0)

m.c279 = Constraint(expr=   m.x201 - m.x358 - m.x359 - m.x360 - m.x361 == 0)

m.c280 = Constraint(expr=   m.x362 <= 100)

m.c281 = Constraint(expr=   m.x363 <= 100)

m.c282 = Constraint(expr=   m.x364 <= 100)

m.c283 = Constraint(expr=   m.x365 <= 100)

m.c284 = Constraint(expr=   m.x366 <= 100)

m.c285 = Constraint(expr=   m.x367 <= 100)

m.c286 = Constraint(expr=   m.x369 <= 100)

m.c287 = Constraint(expr=   m.x370 <= 100)

m.c288 = Constraint(expr=   m.x371 <= 100)

m.c289 = Constraint(expr=   m.x372 <= 100)

m.c290 = Constraint(expr=   m.x373 <= 100)

m.c291 = Constraint(expr=   m.x374 <= 100)

m.c292 = Constraint(expr=   m.x376 <= 100)

m.c293 = Constraint(expr=   m.x377 <= 100)

m.c294 = Constraint(expr=   m.x378 <= 100)

m.c295 = Constraint(expr=   m.x379 <= 100)

m.c296 = Constraint(expr=   m.x380 <= 100)

m.c297 = Constraint(expr=   m.x381 <= 100)

m.c298 = Constraint(expr=   m.x383 <= 100)

m.c299 = Constraint(expr=   m.x384 <= 100)

m.c300 = Constraint(expr=   m.x385 <= 100)

m.c301 = Constraint(expr=   m.x386 <= 100)

m.c302 = Constraint(expr=   m.x387 <= 100)

m.c303 = Constraint(expr=   m.x388 <= 100)

m.c304 = Constraint(expr=   m.x390 <= 100)

m.c305 = Constraint(expr=   m.x391 <= 100)

m.c306 = Constraint(expr=   m.x392 <= 100)

m.c307 = Constraint(expr=   m.x393 <= 100)

m.c308 = Constraint(expr=   m.x394 <= 100)

m.c309 = Constraint(expr=   m.x395 <= 100)

m.c310 = Constraint(expr=   m.x397 >= 0)

m.c311 = Constraint(expr=   m.x398 >= 0)

m.c312 = Constraint(expr=   m.x399 >= 0)

m.c313 = Constraint(expr=   m.x400 >= 0)

m.c314 = Constraint(expr=   m.x401 >= 0)

m.c315 = Constraint(expr=   m.x402 >= 0)

m.c316 = Constraint(expr=   m.x403 >= 0)

m.c317 = Constraint(expr=   m.x404 >= 0)

m.c318 = Constraint(expr=   m.x405 >= 0)

m.c319 = Constraint(expr=   m.x406 >= 0)

m.c320 = Constraint(expr=   m.x407 >= 0)

m.c321 = Constraint(expr=   m.x408 >= 0)

m.c322 = Constraint(expr=   m.x409 >= 0)

m.c323 = Constraint(expr=   m.x410 >= 0)

m.c324 = Constraint(expr=   m.x411 >= 0)

m.c325 = Constraint(expr=   m.x412 >= 0)

m.c326 = Constraint(expr=   m.x413 >= 0)

m.c327 = Constraint(expr=   m.x414 >= 0)

m.c328 = Constraint(expr=   m.x415 >= 0)

m.c329 = Constraint(expr=   m.x416 >= 0)

m.c330 = Constraint(expr=   m.x417 >= 0)

m.c331 = Constraint(expr=   m.x418 >= 0)

m.c332 = Constraint(expr=   m.x419 >= 0)

m.c333 = Constraint(expr=   m.x420 >= 0)

m.c334 = Constraint(expr=   m.x421 >= 0)

m.c335 = Constraint(expr=   m.x422 >= 0)

m.c336 = Constraint(expr=   m.x423 >= 0)

m.c337 = Constraint(expr=   m.x424 >= 0)

m.c338 = Constraint(expr=   m.x425 >= 0)

m.c339 = Constraint(expr=   m.x426 >= 0)

m.c340 = Constraint(expr=   m.x427 >= 0)

m.c341 = Constraint(expr=   m.x428 >= 0)

m.c342 = Constraint(expr=   m.x429 >= 0)

m.c343 = Constraint(expr=   m.x430 >= 0)

m.c344 = Constraint(expr=   m.x431 >= 0)

m.c345 = Constraint(expr=   m.x432 >= 0)

m.c346 = Constraint(expr=   m.x433 >= 0)

m.c347 = Constraint(expr=   m.x434 >= 0)

m.c348 = Constraint(expr=   m.x435 >= 0)

m.c349 = Constraint(expr=   m.x436 >= 0)

m.c350 = Constraint(expr=   m.x437 >= 0)

m.c351 = Constraint(expr=   m.x438 >= 0)

m.c352 = Constraint(expr=   m.x439 >= 0)

m.c353 = Constraint(expr=   m.x440 >= 0)

m.c354 = Constraint(expr=   m.x441 >= 0)

m.c355 = Constraint(expr=   m.x442 >= 0)

m.c356 = Constraint(expr=   m.x443 >= 0)

m.c357 = Constraint(expr=   m.x444 >= 0)

m.c358 = Constraint(expr=   m.x445 >= 0)

m.c359 = Constraint(expr=   m.x446 >= 0)

m.c360 = Constraint(expr=   m.x447 >= 0)

m.c361 = Constraint(expr=   m.x448 >= 0)

m.c362 = Constraint(expr=   m.x449 >= 0)

m.c363 = Constraint(expr=   m.x450 >= 0)

m.c364 = Constraint(expr=   m.x451 >= 0)

m.c365 = Constraint(expr=   m.x452 >= 0)

m.c366 = Constraint(expr=   m.x453 >= 0)

m.c367 = Constraint(expr=   m.x454 >= 0)

m.c368 = Constraint(expr=   m.x455 >= 0)

m.c369 = Constraint(expr=   m.x456 >= 0)

m.c370 = Constraint(expr=   m.x457 >= 0)

m.c371 = Constraint(expr=   m.x458 >= 0)

m.c372 = Constraint(expr=   m.x459 >= 0)

m.c373 = Constraint(expr=   m.x460 >= 0)

m.c374 = Constraint(expr=   m.x461 >= 0)

m.c375 = Constraint(expr=   m.x462 >= 0)

m.c376 = Constraint(expr=   m.x463 >= 0)

m.c377 = Constraint(expr=   m.x464 >= 0)

m.c378 = Constraint(expr=   m.x465 >= 0)

m.c379 = Constraint(expr=   m.x466 >= 0)

m.c380 = Constraint(expr=   m.x467 >= 0)

m.c381 = Constraint(expr=   m.x468 >= 0)

m.c382 = Constraint(expr=   m.x469 >= 0)

m.c383 = Constraint(expr=   m.x470 >= 0)

m.c384 = Constraint(expr=   m.x471 >= 0)

m.c385 = Constraint(expr=   m.x472 >= 0)

m.c386 = Constraint(expr=   m.x473 >= 0)

m.c387 = Constraint(expr=   m.x474 >= 0)

m.c388 = Constraint(expr=   m.x475 >= 0)

m.c389 = Constraint(expr=   m.x476 >= 0)

m.c390 = Constraint(expr=   m.x477 >= 0)

m.c391 = Constraint(expr=   m.x478 >= 0)

m.c392 = Constraint(expr=   m.x479 >= 0)

m.c393 = Constraint(expr=   m.x480 >= 0)

m.c394 = Constraint(expr=   m.x481 >= 0)

m.c395 = Constraint(expr=   m.x482 >= 0)

m.c396 = Constraint(expr=   m.x483 >= 0)

m.c397 = Constraint(expr=   m.x484 >= 0)

m.c398 = Constraint(expr=   m.x485 >= 0)

m.c399 = Constraint(expr=   m.x486 >= 0)

m.c400 = Constraint(expr=   m.x487 >= 0)

m.c401 = Constraint(expr=   m.x488 >= 0)

m.c402 = Constraint(expr=   m.x489 >= 0)

m.c403 = Constraint(expr=   m.x490 >= 0)

m.c404 = Constraint(expr=   m.x491 >= 0)

m.c405 = Constraint(expr=   m.x492 >= 0)

m.c406 = Constraint(expr=   m.x493 >= 0)

m.c407 = Constraint(expr=   m.x494 >= 0)

m.c408 = Constraint(expr=   m.x495 >= 0)

m.c409 = Constraint(expr=   m.x496 >= 0)

m.c410 = Constraint(expr=   m.x497 >= 0)

m.c411 = Constraint(expr=   m.x498 >= 0)

m.c412 = Constraint(expr=   m.x499 >= 0)

m.c413 = Constraint(expr=   m.x500 >= 0)

m.c414 = Constraint(expr=   m.x501 >= 0)

m.c415 = Constraint(expr=   m.x502 >= 0)

m.c416 = Constraint(expr=   m.x503 >= 0)

m.c417 = Constraint(expr=   m.x504 >= 0)

m.c418 = Constraint(expr=   m.x505 >= 0)

m.c419 = Constraint(expr=   m.x506 >= 0)

m.c420 = Constraint(expr=   m.x507 >= 0)

m.c421 = Constraint(expr=   m.x508 >= 0)

m.c422 = Constraint(expr=   m.x509 >= 0)

m.c423 = Constraint(expr=   m.x510 >= 0)

m.c424 = Constraint(expr=   m.x511 >= 0)

m.c425 = Constraint(expr=   m.x512 >= 0)

m.c426 = Constraint(expr=   m.x513 >= 0)

m.c427 = Constraint(expr=   m.x514 >= 0)

m.c428 = Constraint(expr=   m.x515 >= 0)

m.c429 = Constraint(expr=   m.x516 >= 0)

m.c430 = Constraint(expr=   m.x517 >= 0)

m.c431 = Constraint(expr=   m.x518 >= 0)

m.c432 = Constraint(expr=   m.x519 >= 0)

m.c433 = Constraint(expr=   m.x520 >= 0)

m.c434 = Constraint(expr=   m.x521 >= 0)

m.c435 = Constraint(expr=   m.x522 >= 0)

m.c436 = Constraint(expr=   m.x523 >= 0)

m.c437 = Constraint(expr=   m.x524 >= 0)

m.c438 = Constraint(expr=   m.x525 >= 0)

m.c439 = Constraint(expr=   m.x526 >= 0)

m.c440 = Constraint(expr=   m.x527 >= 0)

m.c441 = Constraint(expr=   m.x528 >= 0)

m.c442 = Constraint(expr=   m.x529 >= 0)

m.c443 = Constraint(expr=   m.x530 >= 0)

m.c444 = Constraint(expr=   m.x531 >= 0)

m.c445 = Constraint(expr=   m.x532 >= 0)

m.c446 = Constraint(expr=   m.x533 >= 0)

m.c447 = Constraint(expr=   m.x534 >= 0)

m.c448 = Constraint(expr=   m.x535 >= 0)

m.c449 = Constraint(expr=   m.x536 >= 0)

m.c450 = Constraint(expr=   m.x397 <= 100)

m.c451 = Constraint(expr=   m.x398 <= 100)

m.c452 = Constraint(expr=   m.x399 <= 100)

m.c453 = Constraint(expr=   m.x400 <= 100)

m.c454 = Constraint(expr=   m.x401 <= 100)

m.c455 = Constraint(expr=   m.x402 <= 100)

m.c456 = Constraint(expr=   m.x403 <= 100)

m.c457 = Constraint(expr=   m.x404 <= 100)

m.c458 = Constraint(expr=   m.x405 <= 100)

m.c459 = Constraint(expr=   m.x406 <= 100)

m.c460 = Constraint(expr=   m.x407 <= 100)

m.c461 = Constraint(expr=   m.x408 <= 100)

m.c462 = Constraint(expr=   m.x409 <= 100)

m.c463 = Constraint(expr=   m.x410 <= 100)

m.c464 = Constraint(expr=   m.x411 <= 100)

m.c465 = Constraint(expr=   m.x412 <= 100)

m.c466 = Constraint(expr=   m.x413 <= 100)

m.c467 = Constraint(expr=   m.x414 <= 100)

m.c468 = Constraint(expr=   m.x415 <= 100)

m.c469 = Constraint(expr=   m.x416 <= 100)

m.c470 = Constraint(expr=   m.x417 <= 100)

m.c471 = Constraint(expr=   m.x418 <= 100)

m.c472 = Constraint(expr=   m.x419 <= 100)

m.c473 = Constraint(expr=   m.x420 <= 100)

m.c474 = Constraint(expr=   m.x425 <= 100)

m.c475 = Constraint(expr=   m.x426 <= 100)

m.c476 = Constraint(expr=   m.x427 <= 100)

m.c477 = Constraint(expr=   m.x428 <= 100)

m.c478 = Constraint(expr=   m.x429 <= 100)

m.c479 = Constraint(expr=   m.x430 <= 100)

m.c480 = Constraint(expr=   m.x431 <= 100)

m.c481 = Constraint(expr=   m.x432 <= 100)

m.c482 = Constraint(expr=   m.x433 <= 100)

m.c483 = Constraint(expr=   m.x434 <= 100)

m.c484 = Constraint(expr=   m.x435 <= 100)

m.c485 = Constraint(expr=   m.x436 <= 100)

m.c486 = Constraint(expr=   m.x437 <= 100)

m.c487 = Constraint(expr=   m.x438 <= 100)

m.c488 = Constraint(expr=   m.x439 <= 100)

m.c489 = Constraint(expr=   m.x440 <= 100)

m.c490 = Constraint(expr=   m.x441 <= 100)

m.c491 = Constraint(expr=   m.x442 <= 100)

m.c492 = Constraint(expr=   m.x443 <= 100)

m.c493 = Constraint(expr=   m.x444 <= 100)

m.c494 = Constraint(expr=   m.x445 <= 100)

m.c495 = Constraint(expr=   m.x446 <= 100)

m.c496 = Constraint(expr=   m.x447 <= 100)

m.c497 = Constraint(expr=   m.x448 <= 100)

m.c498 = Constraint(expr=   m.x453 <= 100)

m.c499 = Constraint(expr=   m.x454 <= 100)

m.c500 = Constraint(expr=   m.x455 <= 100)

m.c501 = Constraint(expr=   m.x456 <= 100)

m.c502 = Constraint(expr=   m.x457 <= 100)

m.c503 = Constraint(expr=   m.x458 <= 100)

m.c504 = Constraint(expr=   m.x459 <= 100)

m.c505 = Constraint(expr=   m.x460 <= 100)

m.c506 = Constraint(expr=   m.x461 <= 100)

m.c507 = Constraint(expr=   m.x462 <= 100)

m.c508 = Constraint(expr=   m.x463 <= 100)

m.c509 = Constraint(expr=   m.x464 <= 100)

m.c510 = Constraint(expr=   m.x465 <= 100)

m.c511 = Constraint(expr=   m.x466 <= 100)

m.c512 = Constraint(expr=   m.x467 <= 100)

m.c513 = Constraint(expr=   m.x468 <= 100)

m.c514 = Constraint(expr=   m.x469 <= 100)

m.c515 = Constraint(expr=   m.x470 <= 100)

m.c516 = Constraint(expr=   m.x471 <= 100)

m.c517 = Constraint(expr=   m.x472 <= 100)

m.c518 = Constraint(expr=   m.x473 <= 100)

m.c519 = Constraint(expr=   m.x474 <= 100)

m.c520 = Constraint(expr=   m.x475 <= 100)

m.c521 = Constraint(expr=   m.x476 <= 100)

m.c522 = Constraint(expr=   m.x481 <= 100)

m.c523 = Constraint(expr=   m.x482 <= 100)

m.c524 = Constraint(expr=   m.x483 <= 100)

m.c525 = Constraint(expr=   m.x484 <= 100)

m.c526 = Constraint(expr=   m.x485 <= 100)

m.c527 = Constraint(expr=   m.x486 <= 100)

m.c528 = Constraint(expr=   m.x487 <= 100)

m.c529 = Constraint(expr=   m.x488 <= 100)

m.c530 = Constraint(expr=   m.x489 <= 100)

m.c531 = Constraint(expr=   m.x490 <= 100)

m.c532 = Constraint(expr=   m.x491 <= 100)

m.c533 = Constraint(expr=   m.x492 <= 100)

m.c534 = Constraint(expr=   m.x493 <= 100)

m.c535 = Constraint(expr=   m.x494 <= 100)

m.c536 = Constraint(expr=   m.x495 <= 100)

m.c537 = Constraint(expr=   m.x496 <= 100)

m.c538 = Constraint(expr=   m.x497 <= 100)

m.c539 = Constraint(expr=   m.x498 <= 100)

m.c540 = Constraint(expr=   m.x499 <= 100)

m.c541 = Constraint(expr=   m.x500 <= 100)

m.c542 = Constraint(expr=   m.x501 <= 100)

m.c543 = Constraint(expr=   m.x502 <= 100)

m.c544 = Constraint(expr=   m.x503 <= 100)

m.c545 = Constraint(expr=   m.x504 <= 100)

m.c546 = Constraint(expr=   m.x509 <= 100)

m.c547 = Constraint(expr=   m.x510 <= 100)

m.c548 = Constraint(expr=   m.x511 <= 100)

m.c549 = Constraint(expr=   m.x512 <= 100)

m.c550 = Constraint(expr=   m.x513 <= 100)

m.c551 = Constraint(expr=   m.x514 <= 100)

m.c552 = Constraint(expr=   m.x515 <= 100)

m.c553 = Constraint(expr=   m.x516 <= 100)

m.c554 = Constraint(expr=   m.x517 <= 100)

m.c555 = Constraint(expr=   m.x518 <= 100)

m.c556 = Constraint(expr=   m.x519 <= 100)

m.c557 = Constraint(expr=   m.x520 <= 100)

m.c558 = Constraint(expr=   m.x521 <= 100)

m.c559 = Constraint(expr=   m.x522 <= 100)

m.c560 = Constraint(expr=   m.x523 <= 100)

m.c561 = Constraint(expr=   m.x524 <= 100)

m.c562 = Constraint(expr=   m.x525 <= 100)

m.c563 = Constraint(expr=   m.x526 <= 100)

m.c564 = Constraint(expr=   m.x527 <= 100)

m.c565 = Constraint(expr=   m.x528 <= 100)

m.c566 = Constraint(expr=   m.x529 <= 100)

m.c567 = Constraint(expr=   m.x530 <= 100)

m.c568 = Constraint(expr=   m.x531 <= 100)

m.c569 = Constraint(expr=   m.x532 <= 100)

m.c570 = Constraint(expr=   m.x362 - m.x397 - m.x398 - m.x399 - m.x400 == 0)

m.c571 = Constraint(expr=   m.x363 - m.x401 - m.x402 - m.x403 - m.x404 == 0)

m.c572 = Constraint(expr=   m.x364 - m.x405 - m.x406 - m.x407 - m.x408 == 0)

m.c573 = Constraint(expr=   m.x365 - m.x409 - m.x410 - m.x411 - m.x412 == 0)

m.c574 = Constraint(expr=   m.x366 - m.x413 - m.x414 - m.x415 - m.x416 == 0)

m.c575 = Constraint(expr=   m.x367 - m.x417 - m.x418 - m.x419 - m.x420 == 0)

m.c576 = Constraint(expr=   m.x368 - m.x421 - m.x422 - m.x423 - m.x424 == 0)

m.c577 = Constraint(expr=   m.x369 - m.x425 - m.x426 - m.x427 - m.x428 == 0)

m.c578 = Constraint(expr=   m.x370 - m.x429 - m.x430 - m.x431 - m.x432 == 0)

m.c579 = Constraint(expr=   m.x371 - m.x433 - m.x434 - m.x435 - m.x436 == 0)

m.c580 = Constraint(expr=   m.x372 - m.x437 - m.x438 - m.x439 - m.x440 == 0)

m.c581 = Constraint(expr=   m.x373 - m.x441 - m.x442 - m.x443 - m.x444 == 0)

m.c582 = Constraint(expr=   m.x374 - m.x445 - m.x446 - m.x447 - m.x448 == 0)

m.c583 = Constraint(expr=   m.x375 - m.x449 - m.x450 - m.x451 - m.x452 == 0)

m.c584 = Constraint(expr=   m.x376 - m.x453 - m.x454 - m.x455 - m.x456 == 0)

m.c585 = Constraint(expr=   m.x377 - m.x457 - m.x458 - m.x459 - m.x460 == 0)

m.c586 = Constraint(expr=   m.x378 - m.x461 - m.x462 - m.x463 - m.x464 == 0)

m.c587 = Constraint(expr=   m.x379 - m.x465 - m.x466 - m.x467 - m.x468 == 0)

m.c588 = Constraint(expr=   m.x380 - m.x469 - m.x470 - m.x471 - m.x472 == 0)

m.c589 = Constraint(expr=   m.x381 - m.x473 - m.x474 - m.x475 - m.x476 == 0)

m.c590 = Constraint(expr=   m.x382 - m.x477 - m.x478 - m.x479 - m.x480 == 0)

m.c591 = Constraint(expr=   m.x383 - m.x481 - m.x482 - m.x483 - m.x484 == 0)

m.c592 = Constraint(expr=   m.x384 - m.x485 - m.x486 - m.x487 - m.x488 == 0)

m.c593 = Constraint(expr=   m.x385 - m.x489 - m.x490 - m.x491 - m.x492 == 0)

m.c594 = Constraint(expr=   m.x386 - m.x493 - m.x494 - m.x495 - m.x496 == 0)

m.c595 = Constraint(expr=   m.x387 - m.x497 - m.x498 - m.x499 - m.x500 == 0)

m.c596 = Constraint(expr=   m.x388 - m.x501 - m.x502 - m.x503 - m.x504 == 0)

m.c597 = Constraint(expr=   m.x389 - m.x505 - m.x506 - m.x507 - m.x508 == 0)

m.c598 = Constraint(expr=   m.x390 - m.x509 - m.x510 - m.x511 - m.x512 == 0)

m.c599 = Constraint(expr=   m.x391 - m.x513 - m.x514 - m.x515 - m.x516 == 0)

m.c600 = Constraint(expr=   m.x392 - m.x517 - m.x518 - m.x519 - m.x520 == 0)

m.c601 = Constraint(expr=   m.x393 - m.x521 - m.x522 - m.x523 - m.x524 == 0)

m.c602 = Constraint(expr=   m.x394 - m.x525 - m.x526 - m.x527 - m.x528 == 0)

m.c603 = Constraint(expr=   m.x395 - m.x529 - m.x530 - m.x531 - m.x532 == 0)

m.c604 = Constraint(expr=   m.x396 - m.x533 - m.x534 - m.x535 - m.x536 == 0)

m.c605 = Constraint(expr=   m.x362 == 100)

m.c606 = Constraint(expr=   m.x363 == 100)

m.c607 = Constraint(expr=   m.x364 == 25)

m.c608 = Constraint(expr=   m.x365 == 75)

m.c609 = Constraint(expr=   m.x366 == 50)

m.c610 = Constraint(expr=   m.x367 == 50)

m.c611 = Constraint(expr=   m.x368 == 0)

m.c612 = Constraint(expr=   m.x162 + m.x369 == 100)

m.c613 = Constraint(expr=   m.x163 + m.x370 == 100)

m.c614 = Constraint(expr= - m.x162 + m.x164 + m.x165 + m.x371 == 25)

m.c615 = Constraint(expr= - m.x163 + m.x166 + m.x167 + m.x372 == 75)

m.c616 = Constraint(expr= - m.x164 - m.x166 + m.x168 + m.x373 == 50)

m.c617 = Constraint(expr= - m.x165 - m.x167 + m.x169 + m.x374 == 50)

m.c618 = Constraint(expr= - m.x168 - m.x169 + m.x375 == 0)

m.c619 = Constraint(expr=   m.x162 + m.x170 + m.x376 == 100)

m.c620 = Constraint(expr=   m.x163 + m.x171 + m.x377 == 100)

m.c621 = Constraint(expr= - m.x162 + m.x164 + m.x165 - m.x170 + m.x172 + m.x173 + m.x378 == 25)

m.c622 = Constraint(expr= - m.x163 + m.x166 + m.x167 - m.x171 + m.x174 + m.x175 + m.x379 == 75)

m.c623 = Constraint(expr= - m.x164 - m.x166 + m.x168 - m.x172 - m.x174 + m.x176 + m.x380 == 50)

m.c624 = Constraint(expr= - m.x165 - m.x167 + m.x169 - m.x173 - m.x175 + m.x177 + m.x381 == 50)

m.c625 = Constraint(expr= - m.x168 - m.x169 - m.x176 - m.x177 + m.x382 == 0)

m.c626 = Constraint(expr=   m.x162 + m.x170 + m.x178 + m.x383 == 100)

m.c627 = Constraint(expr=   m.x163 + m.x171 + m.x179 + m.x384 == 100)

m.c628 = Constraint(expr= - m.x162 + m.x164 + m.x165 - m.x170 + m.x172 + m.x173 - m.x178 + m.x180 + m.x181 + m.x385
                          == 25)

m.c629 = Constraint(expr= - m.x163 + m.x166 + m.x167 - m.x171 + m.x174 + m.x175 - m.x179 + m.x182 + m.x183 + m.x386
                          == 75)

m.c630 = Constraint(expr= - m.x164 - m.x166 + m.x168 - m.x172 - m.x174 + m.x176 - m.x180 - m.x182 + m.x184 + m.x387
                          == 50)

m.c631 = Constraint(expr= - m.x165 - m.x167 + m.x169 - m.x173 - m.x175 + m.x177 - m.x181 - m.x183 + m.x185 + m.x388
                          == 50)

m.c632 = Constraint(expr= - m.x168 - m.x169 - m.x176 - m.x177 - m.x184 - m.x185 + m.x389 == 0)

m.c633 = Constraint(expr=   m.x162 + m.x170 + m.x178 + m.x186 + m.x390 == 100)

m.c634 = Constraint(expr=   m.x163 + m.x171 + m.x179 + m.x187 + m.x391 == 100)

m.c635 = Constraint(expr= - m.x162 + m.x164 + m.x165 - m.x170 + m.x172 + m.x173 - m.x178 + m.x180 + m.x181 - m.x186
                          + m.x188 + m.x189 + m.x392 == 25)

m.c636 = Constraint(expr= - m.x163 + m.x166 + m.x167 - m.x171 + m.x174 + m.x175 - m.x179 + m.x182 + m.x183 - m.x187
                          + m.x190 + m.x191 + m.x393 == 75)

m.c637 = Constraint(expr= - m.x164 - m.x166 + m.x168 - m.x172 - m.x174 + m.x176 - m.x180 - m.x182 + m.x184 - m.x188
                          - m.x190 + m.x192 + m.x394 == 50)

m.c638 = Constraint(expr= - m.x165 - m.x167 + m.x169 - m.x173 - m.x175 + m.x177 - m.x181 - m.x183 + m.x185 - m.x189
                          - m.x191 + m.x193 + m.x395 == 50)

m.c639 = Constraint(expr= - m.x168 - m.x169 - m.x176 - m.x177 - m.x184 - m.x185 - m.x192 - m.x193 + m.x396 == 0)

m.c640 = Constraint(expr=   m.x397 == 100)

m.c641 = Constraint(expr=   m.x398 == 0)

m.c642 = Constraint(expr=   m.x399 == 0)

m.c643 = Constraint(expr=   m.x400 == 0)

m.c644 = Constraint(expr=   m.x401 == 0)

m.c645 = Constraint(expr=   m.x402 == 100)

m.c646 = Constraint(expr=   m.x403 == 0)

m.c647 = Constraint(expr=   m.x404 == 0)

m.c648 = Constraint(expr=   m.x405 == 25)

m.c649 = Constraint(expr=   m.x406 == 0)

m.c650 = Constraint(expr=   m.x407 == 0)

m.c651 = Constraint(expr=   m.x408 == 0)

m.c652 = Constraint(expr=   m.x409 == 0)

m.c653 = Constraint(expr=   m.x410 == 75)

m.c654 = Constraint(expr=   m.x411 == 0)

m.c655 = Constraint(expr=   m.x412 == 0)

m.c656 = Constraint(expr=   m.x413 == 0)

m.c657 = Constraint(expr=   m.x414 == 0)

m.c658 = Constraint(expr=   m.x415 == 50)

m.c659 = Constraint(expr=   m.x416 == 0)

m.c660 = Constraint(expr=   m.x417 == 0)

m.c661 = Constraint(expr=   m.x418 == 0)

m.c662 = Constraint(expr=   m.x419 == 0)

m.c663 = Constraint(expr=   m.x420 == 50)

m.c664 = Constraint(expr=   m.x421 == 0)

m.c665 = Constraint(expr=   m.x422 == 0)

m.c666 = Constraint(expr=   m.x423 == 0)

m.c667 = Constraint(expr=   m.x424 == 0)

m.c668 = Constraint(expr=   m.x202 + m.x425 == 100)

m.c669 = Constraint(expr=   m.x203 + m.x426 == 0)

m.c670 = Constraint(expr=   m.x204 + m.x427 == 0)

m.c671 = Constraint(expr=   m.x205 + m.x428 == 0)

m.c672 = Constraint(expr=   m.x206 + m.x429 == 0)

m.c673 = Constraint(expr=   m.x207 + m.x430 == 100)

m.c674 = Constraint(expr=   m.x208 + m.x431 == 0)

m.c675 = Constraint(expr=   m.x209 + m.x432 == 0)

m.c676 = Constraint(expr= - m.x202 + m.x210 + m.x214 + m.x433 == 25)

m.c677 = Constraint(expr= - m.x203 + m.x211 + m.x215 + m.x434 == 0)

m.c678 = Constraint(expr= - m.x204 + m.x212 + m.x216 + m.x435 == 0)

m.c679 = Constraint(expr= - m.x205 + m.x213 + m.x217 + m.x436 == 0)

m.c680 = Constraint(expr= - m.x206 + m.x218 + m.x222 + m.x437 == 0)

m.c681 = Constraint(expr= - m.x207 + m.x219 + m.x223 + m.x438 == 75)

m.c682 = Constraint(expr= - m.x208 + m.x220 + m.x224 + m.x439 == 0)

m.c683 = Constraint(expr= - m.x209 + m.x221 + m.x225 + m.x440 == 0)

m.c684 = Constraint(expr= - m.x210 - m.x218 + m.x226 + m.x441 == 0)

m.c685 = Constraint(expr= - m.x211 - m.x219 + m.x227 + m.x442 == 0)

m.c686 = Constraint(expr= - m.x212 - m.x220 + m.x228 + m.x443 == 50)

m.c687 = Constraint(expr= - m.x213 - m.x221 + m.x229 + m.x444 == 0)

m.c688 = Constraint(expr= - m.x214 - m.x222 + m.x230 + m.x445 == 0)

m.c689 = Constraint(expr= - m.x215 - m.x223 + m.x231 + m.x446 == 0)

m.c690 = Constraint(expr= - m.x216 - m.x224 + m.x232 + m.x447 == 0)

m.c691 = Constraint(expr= - m.x217 - m.x225 + m.x233 + m.x448 == 50)

m.c692 = Constraint(expr= - m.x226 - m.x230 + m.x449 == 0)

m.c693 = Constraint(expr= - m.x227 - m.x231 + m.x450 == 0)

m.c694 = Constraint(expr= - m.x228 - m.x232 + m.x451 == 0)

m.c695 = Constraint(expr= - m.x229 - m.x233 + m.x452 == 0)

m.c696 = Constraint(expr=   m.x202 + m.x234 + m.x453 == 100)

m.c697 = Constraint(expr=   m.x203 + m.x235 + m.x454 == 0)

m.c698 = Constraint(expr=   m.x204 + m.x236 + m.x455 == 0)

m.c699 = Constraint(expr=   m.x205 + m.x237 + m.x456 == 0)

m.c700 = Constraint(expr=   m.x206 + m.x238 + m.x457 == 0)

m.c701 = Constraint(expr=   m.x207 + m.x239 + m.x458 == 100)

m.c702 = Constraint(expr=   m.x208 + m.x240 + m.x459 == 0)

m.c703 = Constraint(expr=   m.x209 + m.x241 + m.x460 == 0)

m.c704 = Constraint(expr= - m.x202 + m.x210 + m.x214 - m.x234 + m.x242 + m.x246 + m.x461 == 25)

m.c705 = Constraint(expr= - m.x203 + m.x211 + m.x215 - m.x235 + m.x243 + m.x247 + m.x462 == 0)

m.c706 = Constraint(expr= - m.x204 + m.x212 + m.x216 - m.x236 + m.x244 + m.x248 + m.x463 == 0)

m.c707 = Constraint(expr= - m.x205 + m.x213 + m.x217 - m.x237 + m.x245 + m.x249 + m.x464 == 0)

m.c708 = Constraint(expr= - m.x206 + m.x218 + m.x222 - m.x238 + m.x250 + m.x254 + m.x465 == 0)

m.c709 = Constraint(expr= - m.x207 + m.x219 + m.x223 - m.x239 + m.x251 + m.x255 + m.x466 == 75)

m.c710 = Constraint(expr= - m.x208 + m.x220 + m.x224 - m.x240 + m.x252 + m.x256 + m.x467 == 0)

m.c711 = Constraint(expr= - m.x209 + m.x221 + m.x225 - m.x241 + m.x253 + m.x257 + m.x468 == 0)

m.c712 = Constraint(expr= - m.x210 - m.x218 + m.x226 - m.x242 - m.x250 + m.x258 + m.x469 == 0)

m.c713 = Constraint(expr= - m.x211 - m.x219 + m.x227 - m.x243 - m.x251 + m.x259 + m.x470 == 0)

m.c714 = Constraint(expr= - m.x212 - m.x220 + m.x228 - m.x244 - m.x252 + m.x260 + m.x471 == 50)

m.c715 = Constraint(expr= - m.x213 - m.x221 + m.x229 - m.x245 - m.x253 + m.x261 + m.x472 == 0)

m.c716 = Constraint(expr= - m.x214 - m.x222 + m.x230 - m.x246 - m.x254 + m.x262 + m.x473 == 0)

m.c717 = Constraint(expr= - m.x215 - m.x223 + m.x231 - m.x247 - m.x255 + m.x263 + m.x474 == 0)

m.c718 = Constraint(expr= - m.x216 - m.x224 + m.x232 - m.x248 - m.x256 + m.x264 + m.x475 == 0)

m.c719 = Constraint(expr= - m.x217 - m.x225 + m.x233 - m.x249 - m.x257 + m.x265 + m.x476 == 50)

m.c720 = Constraint(expr= - m.x226 - m.x230 - m.x258 - m.x262 + m.x477 == 0)

m.c721 = Constraint(expr= - m.x227 - m.x231 - m.x259 - m.x263 + m.x478 == 0)

m.c722 = Constraint(expr= - m.x228 - m.x232 - m.x260 - m.x264 + m.x479 == 0)

m.c723 = Constraint(expr= - m.x229 - m.x233 - m.x261 - m.x265 + m.x480 == 0)

m.c724 = Constraint(expr=   m.x202 + m.x234 + m.x266 + m.x481 == 100)

m.c725 = Constraint(expr=   m.x203 + m.x235 + m.x267 + m.x482 == 0)

m.c726 = Constraint(expr=   m.x204 + m.x236 + m.x268 + m.x483 == 0)

m.c727 = Constraint(expr=   m.x205 + m.x237 + m.x269 + m.x484 == 0)

m.c728 = Constraint(expr=   m.x206 + m.x238 + m.x270 + m.x485 == 0)

m.c729 = Constraint(expr=   m.x207 + m.x239 + m.x271 + m.x486 == 100)

m.c730 = Constraint(expr=   m.x208 + m.x240 + m.x272 + m.x487 == 0)

m.c731 = Constraint(expr=   m.x209 + m.x241 + m.x273 + m.x488 == 0)

m.c732 = Constraint(expr= - m.x202 + m.x210 + m.x214 - m.x234 + m.x242 + m.x246 - m.x266 + m.x274 + m.x278 + m.x489
                          == 25)

m.c733 = Constraint(expr= - m.x203 + m.x211 + m.x215 - m.x235 + m.x243 + m.x247 - m.x267 + m.x275 + m.x279 + m.x490
                          == 0)

m.c734 = Constraint(expr= - m.x204 + m.x212 + m.x216 - m.x236 + m.x244 + m.x248 - m.x268 + m.x276 + m.x280 + m.x491
                          == 0)

m.c735 = Constraint(expr= - m.x205 + m.x213 + m.x217 - m.x237 + m.x245 + m.x249 - m.x269 + m.x277 + m.x281 + m.x492
                          == 0)

m.c736 = Constraint(expr= - m.x206 + m.x218 + m.x222 - m.x238 + m.x250 + m.x254 - m.x270 + m.x282 + m.x286 + m.x493
                          == 0)

m.c737 = Constraint(expr= - m.x207 + m.x219 + m.x223 - m.x239 + m.x251 + m.x255 - m.x271 + m.x283 + m.x287 + m.x494
                          == 75)

m.c738 = Constraint(expr= - m.x208 + m.x220 + m.x224 - m.x240 + m.x252 + m.x256 - m.x272 + m.x284 + m.x288 + m.x495
                          == 0)

m.c739 = Constraint(expr= - m.x209 + m.x221 + m.x225 - m.x241 + m.x253 + m.x257 - m.x273 + m.x285 + m.x289 + m.x496
                          == 0)

m.c740 = Constraint(expr= - m.x210 - m.x218 + m.x226 - m.x242 - m.x250 + m.x258 - m.x274 - m.x282 + m.x290 + m.x497
                          == 0)

m.c741 = Constraint(expr= - m.x211 - m.x219 + m.x227 - m.x243 - m.x251 + m.x259 - m.x275 - m.x283 + m.x291 + m.x498
                          == 0)

m.c742 = Constraint(expr= - m.x212 - m.x220 + m.x228 - m.x244 - m.x252 + m.x260 - m.x276 - m.x284 + m.x292 + m.x499
                          == 50)

m.c743 = Constraint(expr= - m.x213 - m.x221 + m.x229 - m.x245 - m.x253 + m.x261 - m.x277 - m.x285 + m.x293 + m.x500
                          == 0)

m.c744 = Constraint(expr= - m.x214 - m.x222 + m.x230 - m.x246 - m.x254 + m.x262 - m.x278 - m.x286 + m.x294 + m.x501
                          == 0)

m.c745 = Constraint(expr= - m.x215 - m.x223 + m.x231 - m.x247 - m.x255 + m.x263 - m.x279 - m.x287 + m.x295 + m.x502
                          == 0)

m.c746 = Constraint(expr= - m.x216 - m.x224 + m.x232 - m.x248 - m.x256 + m.x264 - m.x280 - m.x288 + m.x296 + m.x503
                          == 0)

m.c747 = Constraint(expr= - m.x217 - m.x225 + m.x233 - m.x249 - m.x257 + m.x265 - m.x281 - m.x289 + m.x297 + m.x504
                          == 50)

m.c748 = Constraint(expr= - m.x226 - m.x230 - m.x258 - m.x262 - m.x290 - m.x294 + m.x505 == 0)

m.c749 = Constraint(expr= - m.x227 - m.x231 - m.x259 - m.x263 - m.x291 - m.x295 + m.x506 == 0)

m.c750 = Constraint(expr= - m.x228 - m.x232 - m.x260 - m.x264 - m.x292 - m.x296 + m.x507 == 0)

m.c751 = Constraint(expr= - m.x229 - m.x233 - m.x261 - m.x265 - m.x293 - m.x297 + m.x508 == 0)

m.c752 = Constraint(expr=   m.x202 + m.x234 + m.x266 + m.x298 + m.x509 == 100)

m.c753 = Constraint(expr=   m.x203 + m.x235 + m.x267 + m.x299 + m.x510 == 0)

m.c754 = Constraint(expr=   m.x204 + m.x236 + m.x268 + m.x300 + m.x511 == 0)

m.c755 = Constraint(expr=   m.x205 + m.x237 + m.x269 + m.x301 + m.x512 == 0)

m.c756 = Constraint(expr=   m.x206 + m.x238 + m.x270 + m.x302 + m.x513 == 0)

m.c757 = Constraint(expr=   m.x207 + m.x239 + m.x271 + m.x303 + m.x514 == 100)

m.c758 = Constraint(expr=   m.x208 + m.x240 + m.x272 + m.x304 + m.x515 == 0)

m.c759 = Constraint(expr=   m.x209 + m.x241 + m.x273 + m.x305 + m.x516 == 0)

m.c760 = Constraint(expr= - m.x202 + m.x210 + m.x214 - m.x234 + m.x242 + m.x246 - m.x266 + m.x274 + m.x278 - m.x298
                          + m.x306 + m.x310 + m.x517 == 25)

m.c761 = Constraint(expr= - m.x203 + m.x211 + m.x215 - m.x235 + m.x243 + m.x247 - m.x267 + m.x275 + m.x279 - m.x299
                          + m.x307 + m.x311 + m.x518 == 0)

m.c762 = Constraint(expr= - m.x204 + m.x212 + m.x216 - m.x236 + m.x244 + m.x248 - m.x268 + m.x276 + m.x280 - m.x300
                          + m.x308 + m.x312 + m.x519 == 0)

m.c763 = Constraint(expr= - m.x205 + m.x213 + m.x217 - m.x237 + m.x245 + m.x249 - m.x269 + m.x277 + m.x281 - m.x301
                          + m.x309 + m.x313 + m.x520 == 0)

m.c764 = Constraint(expr= - m.x206 + m.x218 + m.x222 - m.x238 + m.x250 + m.x254 - m.x270 + m.x282 + m.x286 - m.x302
                          + m.x314 + m.x318 + m.x521 == 0)

m.c765 = Constraint(expr= - m.x207 + m.x219 + m.x223 - m.x239 + m.x251 + m.x255 - m.x271 + m.x283 + m.x287 - m.x303
                          + m.x315 + m.x319 + m.x522 == 75)

m.c766 = Constraint(expr= - m.x208 + m.x220 + m.x224 - m.x240 + m.x252 + m.x256 - m.x272 + m.x284 + m.x288 - m.x304
                          + m.x316 + m.x320 + m.x523 == 0)

m.c767 = Constraint(expr= - m.x209 + m.x221 + m.x225 - m.x241 + m.x253 + m.x257 - m.x273 + m.x285 + m.x289 - m.x305
                          + m.x317 + m.x321 + m.x524 == 0)

m.c768 = Constraint(expr= - m.x210 - m.x218 + m.x226 - m.x242 - m.x250 + m.x258 - m.x274 - m.x282 + m.x290 - m.x306
                          - m.x314 + m.x322 + m.x525 == 0)

m.c769 = Constraint(expr= - m.x211 - m.x219 + m.x227 - m.x243 - m.x251 + m.x259 - m.x275 - m.x283 + m.x291 - m.x307
                          - m.x315 + m.x323 + m.x526 == 0)

m.c770 = Constraint(expr= - m.x212 - m.x220 + m.x228 - m.x244 - m.x252 + m.x260 - m.x276 - m.x284 + m.x292 - m.x308
                          - m.x316 + m.x324 + m.x527 == 50)

m.c771 = Constraint(expr= - m.x213 - m.x221 + m.x229 - m.x245 - m.x253 + m.x261 - m.x277 - m.x285 + m.x293 - m.x309
                          - m.x317 + m.x325 + m.x528 == 0)

m.c772 = Constraint(expr= - m.x214 - m.x222 + m.x230 - m.x246 - m.x254 + m.x262 - m.x278 - m.x286 + m.x294 - m.x310
                          - m.x318 + m.x326 + m.x529 == 0)

m.c773 = Constraint(expr= - m.x215 - m.x223 + m.x231 - m.x247 - m.x255 + m.x263 - m.x279 - m.x287 + m.x295 - m.x311
                          - m.x319 + m.x327 + m.x530 == 0)

m.c774 = Constraint(expr= - m.x216 - m.x224 + m.x232 - m.x248 - m.x256 + m.x264 - m.x280 - m.x288 + m.x296 - m.x312
                          - m.x320 + m.x328 + m.x531 == 0)

m.c775 = Constraint(expr= - m.x217 - m.x225 + m.x233 - m.x249 - m.x257 + m.x265 - m.x281 - m.x289 + m.x297 - m.x313
                          - m.x321 + m.x329 + m.x532 == 50)

m.c776 = Constraint(expr= - m.x226 - m.x230 - m.x258 - m.x262 - m.x290 - m.x294 - m.x322 - m.x326 + m.x533 == 0)

m.c777 = Constraint(expr= - m.x227 - m.x231 - m.x259 - m.x263 - m.x291 - m.x295 - m.x323 - m.x327 + m.x534 == 0)

m.c778 = Constraint(expr= - m.x228 - m.x232 - m.x260 - m.x264 - m.x292 - m.x296 - m.x324 - m.x328 + m.x535 == 0)

m.c779 = Constraint(expr= - m.x229 - m.x233 - m.x261 - m.x265 - m.x293 - m.x297 - m.x325 - m.x329 + m.x536 == 0)

m.c780 = Constraint(expr=m.x162*m.x397 - m.x202*m.x362 == 0)

m.c781 = Constraint(expr=m.x162*m.x398 - m.x203*m.x362 == 0)

m.c782 = Constraint(expr=m.x162*m.x399 - m.x204*m.x362 == 0)

m.c783 = Constraint(expr=m.x162*m.x400 - m.x205*m.x362 == 0)

m.c784 = Constraint(expr=m.x163*m.x401 - m.x206*m.x363 == 0)

m.c785 = Constraint(expr=m.x163*m.x402 - m.x207*m.x363 == 0)

m.c786 = Constraint(expr=m.x163*m.x403 - m.x208*m.x363 == 0)

m.c787 = Constraint(expr=m.x163*m.x404 - m.x209*m.x363 == 0)

m.c788 = Constraint(expr=m.x164*m.x405 - m.x210*m.x364 == 0)

m.c789 = Constraint(expr=m.x164*m.x406 - m.x211*m.x364 == 0)

m.c790 = Constraint(expr=m.x164*m.x407 - m.x212*m.x364 == 0)

m.c791 = Constraint(expr=m.x164*m.x408 - m.x213*m.x364 == 0)

m.c792 = Constraint(expr=m.x165*m.x405 - m.x214*m.x364 == 0)

m.c793 = Constraint(expr=m.x165*m.x406 - m.x215*m.x364 == 0)

m.c794 = Constraint(expr=m.x165*m.x407 - m.x216*m.x364 == 0)

m.c795 = Constraint(expr=m.x165*m.x408 - m.x217*m.x364 == 0)

m.c796 = Constraint(expr=m.x166*m.x409 - m.x218*m.x365 == 0)

m.c797 = Constraint(expr=m.x166*m.x410 - m.x219*m.x365 == 0)

m.c798 = Constraint(expr=m.x166*m.x411 - m.x220*m.x365 == 0)

m.c799 = Constraint(expr=m.x166*m.x412 - m.x221*m.x365 == 0)

m.c800 = Constraint(expr=m.x167*m.x409 - m.x222*m.x365 == 0)

m.c801 = Constraint(expr=m.x167*m.x410 - m.x223*m.x365 == 0)

m.c802 = Constraint(expr=m.x167*m.x411 - m.x224*m.x365 == 0)

m.c803 = Constraint(expr=m.x167*m.x412 - m.x225*m.x365 == 0)

m.c804 = Constraint(expr=m.x168*m.x413 - m.x226*m.x366 == 0)

m.c805 = Constraint(expr=m.x168*m.x414 - m.x227*m.x366 == 0)

m.c806 = Constraint(expr=m.x168*m.x415 - m.x228*m.x366 == 0)

m.c807 = Constraint(expr=m.x168*m.x416 - m.x229*m.x366 == 0)

m.c808 = Constraint(expr=m.x169*m.x417 - m.x230*m.x367 == 0)

m.c809 = Constraint(expr=m.x169*m.x418 - m.x231*m.x367 == 0)

m.c810 = Constraint(expr=m.x169*m.x419 - m.x232*m.x367 == 0)

m.c811 = Constraint(expr=m.x169*m.x420 - m.x233*m.x367 == 0)

m.c812 = Constraint(expr=m.x170*m.x425 - m.x234*m.x369 == 0)

m.c813 = Constraint(expr=m.x170*m.x426 - m.x235*m.x369 == 0)

m.c814 = Constraint(expr=m.x170*m.x427 - m.x236*m.x369 == 0)

m.c815 = Constraint(expr=m.x170*m.x428 - m.x237*m.x369 == 0)

m.c816 = Constraint(expr=m.x171*m.x429 - m.x238*m.x370 == 0)

m.c817 = Constraint(expr=m.x171*m.x430 - m.x239*m.x370 == 0)

m.c818 = Constraint(expr=m.x171*m.x431 - m.x240*m.x370 == 0)

m.c819 = Constraint(expr=m.x171*m.x432 - m.x241*m.x370 == 0)

m.c820 = Constraint(expr=m.x172*m.x433 - m.x242*m.x371 == 0)

m.c821 = Constraint(expr=m.x172*m.x434 - m.x243*m.x371 == 0)

m.c822 = Constraint(expr=m.x172*m.x435 - m.x244*m.x371 == 0)

m.c823 = Constraint(expr=m.x172*m.x436 - m.x245*m.x371 == 0)

m.c824 = Constraint(expr=m.x173*m.x433 - m.x246*m.x371 == 0)

m.c825 = Constraint(expr=m.x173*m.x434 - m.x247*m.x371 == 0)

m.c826 = Constraint(expr=m.x173*m.x435 - m.x248*m.x371 == 0)

m.c827 = Constraint(expr=m.x173*m.x436 - m.x249*m.x371 == 0)

m.c828 = Constraint(expr=m.x174*m.x437 - m.x250*m.x372 == 0)

m.c829 = Constraint(expr=m.x174*m.x438 - m.x251*m.x372 == 0)

m.c830 = Constraint(expr=m.x174*m.x439 - m.x252*m.x372 == 0)

m.c831 = Constraint(expr=m.x174*m.x440 - m.x253*m.x372 == 0)

m.c832 = Constraint(expr=m.x175*m.x437 - m.x254*m.x372 == 0)

m.c833 = Constraint(expr=m.x175*m.x438 - m.x255*m.x372 == 0)

m.c834 = Constraint(expr=m.x175*m.x439 - m.x256*m.x372 == 0)

m.c835 = Constraint(expr=m.x175*m.x440 - m.x257*m.x372 == 0)

m.c836 = Constraint(expr=m.x176*m.x441 - m.x258*m.x373 == 0)

m.c837 = Constraint(expr=m.x176*m.x442 - m.x259*m.x373 == 0)

m.c838 = Constraint(expr=m.x176*m.x443 - m.x260*m.x373 == 0)

m.c839 = Constraint(expr=m.x176*m.x444 - m.x261*m.x373 == 0)

m.c840 = Constraint(expr=m.x177*m.x445 - m.x262*m.x374 == 0)

m.c841 = Constraint(expr=m.x177*m.x446 - m.x263*m.x374 == 0)

m.c842 = Constraint(expr=m.x177*m.x447 - m.x264*m.x374 == 0)

m.c843 = Constraint(expr=m.x177*m.x448 - m.x265*m.x374 == 0)

m.c844 = Constraint(expr=m.x178*m.x453 - m.x266*m.x376 == 0)

m.c845 = Constraint(expr=m.x178*m.x454 - m.x267*m.x376 == 0)

m.c846 = Constraint(expr=m.x178*m.x455 - m.x268*m.x376 == 0)

m.c847 = Constraint(expr=m.x178*m.x456 - m.x269*m.x376 == 0)

m.c848 = Constraint(expr=m.x179*m.x457 - m.x270*m.x377 == 0)

m.c849 = Constraint(expr=m.x179*m.x458 - m.x271*m.x377 == 0)

m.c850 = Constraint(expr=m.x179*m.x459 - m.x272*m.x377 == 0)

m.c851 = Constraint(expr=m.x179*m.x460 - m.x273*m.x377 == 0)

m.c852 = Constraint(expr=m.x180*m.x461 - m.x274*m.x378 == 0)

m.c853 = Constraint(expr=m.x180*m.x462 - m.x275*m.x378 == 0)

m.c854 = Constraint(expr=m.x180*m.x463 - m.x276*m.x378 == 0)

m.c855 = Constraint(expr=m.x180*m.x464 - m.x277*m.x378 == 0)

m.c856 = Constraint(expr=m.x181*m.x461 - m.x278*m.x378 == 0)

m.c857 = Constraint(expr=m.x181*m.x462 - m.x279*m.x378 == 0)

m.c858 = Constraint(expr=m.x181*m.x463 - m.x280*m.x378 == 0)

m.c859 = Constraint(expr=m.x181*m.x464 - m.x281*m.x378 == 0)

m.c860 = Constraint(expr=m.x182*m.x465 - m.x282*m.x379 == 0)

m.c861 = Constraint(expr=m.x182*m.x466 - m.x283*m.x379 == 0)

m.c862 = Constraint(expr=m.x182*m.x467 - m.x284*m.x379 == 0)

m.c863 = Constraint(expr=m.x182*m.x468 - m.x285*m.x379 == 0)

m.c864 = Constraint(expr=m.x183*m.x465 - m.x286*m.x379 == 0)

m.c865 = Constraint(expr=m.x183*m.x466 - m.x287*m.x379 == 0)

m.c866 = Constraint(expr=m.x183*m.x467 - m.x288*m.x379 == 0)

m.c867 = Constraint(expr=m.x183*m.x468 - m.x289*m.x379 == 0)

m.c868 = Constraint(expr=m.x184*m.x469 - m.x290*m.x380 == 0)

m.c869 = Constraint(expr=m.x184*m.x470 - m.x291*m.x380 == 0)

m.c870 = Constraint(expr=m.x184*m.x471 - m.x292*m.x380 == 0)

m.c871 = Constraint(expr=m.x184*m.x472 - m.x293*m.x380 == 0)

m.c872 = Constraint(expr=m.x185*m.x473 - m.x294*m.x381 == 0)

m.c873 = Constraint(expr=m.x185*m.x474 - m.x295*m.x381 == 0)

m.c874 = Constraint(expr=m.x185*m.x475 - m.x296*m.x381 == 0)

m.c875 = Constraint(expr=m.x185*m.x476 - m.x297*m.x381 == 0)

m.c876 = Constraint(expr=m.x186*m.x481 - m.x298*m.x383 == 0)

m.c877 = Constraint(expr=m.x186*m.x482 - m.x299*m.x383 == 0)

m.c878 = Constraint(expr=m.x186*m.x483 - m.x300*m.x383 == 0)

m.c879 = Constraint(expr=m.x186*m.x484 - m.x301*m.x383 == 0)

m.c880 = Constraint(expr=m.x187*m.x485 - m.x302*m.x384 == 0)

m.c881 = Constraint(expr=m.x187*m.x486 - m.x303*m.x384 == 0)

m.c882 = Constraint(expr=m.x187*m.x487 - m.x304*m.x384 == 0)

m.c883 = Constraint(expr=m.x187*m.x488 - m.x305*m.x384 == 0)

m.c884 = Constraint(expr=m.x188*m.x489 - m.x306*m.x385 == 0)

m.c885 = Constraint(expr=m.x188*m.x490 - m.x307*m.x385 == 0)

m.c886 = Constraint(expr=m.x188*m.x491 - m.x308*m.x385 == 0)

m.c887 = Constraint(expr=m.x188*m.x492 - m.x309*m.x385 == 0)

m.c888 = Constraint(expr=m.x189*m.x489 - m.x310*m.x385 == 0)

m.c889 = Constraint(expr=m.x189*m.x490 - m.x311*m.x385 == 0)

m.c890 = Constraint(expr=m.x189*m.x491 - m.x312*m.x385 == 0)

m.c891 = Constraint(expr=m.x189*m.x492 - m.x313*m.x385 == 0)

m.c892 = Constraint(expr=m.x190*m.x493 - m.x314*m.x386 == 0)

m.c893 = Constraint(expr=m.x190*m.x494 - m.x315*m.x386 == 0)

m.c894 = Constraint(expr=m.x190*m.x495 - m.x316*m.x386 == 0)

m.c895 = Constraint(expr=m.x190*m.x496 - m.x317*m.x386 == 0)

m.c896 = Constraint(expr=m.x191*m.x493 - m.x318*m.x386 == 0)

m.c897 = Constraint(expr=m.x191*m.x494 - m.x319*m.x386 == 0)

m.c898 = Constraint(expr=m.x191*m.x495 - m.x320*m.x386 == 0)

m.c899 = Constraint(expr=m.x191*m.x496 - m.x321*m.x386 == 0)

m.c900 = Constraint(expr=m.x192*m.x497 - m.x322*m.x387 == 0)

m.c901 = Constraint(expr=m.x192*m.x498 - m.x323*m.x387 == 0)

m.c902 = Constraint(expr=m.x192*m.x499 - m.x324*m.x387 == 0)

m.c903 = Constraint(expr=m.x192*m.x500 - m.x325*m.x387 == 0)

m.c904 = Constraint(expr=m.x193*m.x501 - m.x326*m.x388 == 0)

m.c905 = Constraint(expr=m.x193*m.x502 - m.x327*m.x388 == 0)

m.c906 = Constraint(expr=m.x193*m.x503 - m.x328*m.x388 == 0)

m.c907 = Constraint(expr=m.x193*m.x504 - m.x329*m.x388 == 0)

m.c908 = Constraint(expr=m.x194*m.x509 - m.x330*m.x390 == 0)

m.c909 = Constraint(expr=m.x194*m.x510 - m.x331*m.x390 == 0)

m.c910 = Constraint(expr=m.x194*m.x511 - m.x332*m.x390 == 0)

m.c911 = Constraint(expr=m.x194*m.x512 - m.x333*m.x390 == 0)

m.c912 = Constraint(expr=m.x195*m.x513 - m.x334*m.x391 == 0)

m.c913 = Constraint(expr=m.x195*m.x514 - m.x335*m.x391 == 0)

m.c914 = Constraint(expr=m.x195*m.x515 - m.x336*m.x391 == 0)

m.c915 = Constraint(expr=m.x195*m.x516 - m.x337*m.x391 == 0)

m.c916 = Constraint(expr=m.x196*m.x517 - m.x338*m.x392 == 0)

m.c917 = Constraint(expr=m.x196*m.x518 - m.x339*m.x392 == 0)

m.c918 = Constraint(expr=m.x196*m.x519 - m.x340*m.x392 == 0)

m.c919 = Constraint(expr=m.x196*m.x520 - m.x341*m.x392 == 0)

m.c920 = Constraint(expr=m.x197*m.x517 - m.x342*m.x392 == 0)

m.c921 = Constraint(expr=m.x197*m.x518 - m.x343*m.x392 == 0)

m.c922 = Constraint(expr=m.x197*m.x519 - m.x344*m.x392 == 0)

m.c923 = Constraint(expr=m.x197*m.x520 - m.x345*m.x392 == 0)

m.c924 = Constraint(expr=m.x198*m.x521 - m.x346*m.x393 == 0)

m.c925 = Constraint(expr=m.x198*m.x522 - m.x347*m.x393 == 0)

m.c926 = Constraint(expr=m.x198*m.x523 - m.x348*m.x393 == 0)

m.c927 = Constraint(expr=m.x198*m.x524 - m.x349*m.x393 == 0)

m.c928 = Constraint(expr=m.x199*m.x521 - m.x350*m.x393 == 0)

m.c929 = Constraint(expr=m.x199*m.x522 - m.x351*m.x393 == 0)

m.c930 = Constraint(expr=m.x199*m.x523 - m.x352*m.x393 == 0)

m.c931 = Constraint(expr=m.x199*m.x524 - m.x353*m.x393 == 0)

m.c932 = Constraint(expr=m.x200*m.x525 - m.x354*m.x394 == 0)

m.c933 = Constraint(expr=m.x200*m.x526 - m.x355*m.x394 == 0)

m.c934 = Constraint(expr=m.x200*m.x527 - m.x356*m.x394 == 0)

m.c935 = Constraint(expr=m.x200*m.x528 - m.x357*m.x394 == 0)

m.c936 = Constraint(expr=m.x201*m.x529 - m.x358*m.x395 == 0)

m.c937 = Constraint(expr=m.x201*m.x530 - m.x359*m.x395 == 0)

m.c938 = Constraint(expr=m.x201*m.x531 - m.x360*m.x395 == 0)

m.c939 = Constraint(expr=m.x201*m.x532 - m.x361*m.x395 == 0)

m.c940 = Constraint(expr=   m.x162 >= 0)

m.c941 = Constraint(expr=   m.x163 >= 0)

m.c942 = Constraint(expr=   m.x164 >= 0)

m.c943 = Constraint(expr=   m.x165 >= 0)

m.c944 = Constraint(expr=   m.x166 >= 0)

m.c945 = Constraint(expr=   m.x167 >= 0)

m.c946 = Constraint(expr= - 5*m.x88 + m.x168 >= 0)

m.c947 = Constraint(expr= - 5*m.x89 + m.x169 >= 0)

m.c948 = Constraint(expr=   m.x170 >= 0)

m.c949 = Constraint(expr=   m.x171 >= 0)

m.c950 = Constraint(expr=   m.x172 >= 0)

m.c951 = Constraint(expr=   m.x173 >= 0)

m.c952 = Constraint(expr=   m.x174 >= 0)

m.c953 = Constraint(expr=   m.x175 >= 0)

m.c954 = Constraint(expr= - 5*m.x96 + m.x176 >= 0)

m.c955 = Constraint(expr= - 5*m.x97 + m.x177 >= 0)

m.c956 = Constraint(expr=   m.x178 >= 0)

m.c957 = Constraint(expr=   m.x179 >= 0)

m.c958 = Constraint(expr=   m.x180 >= 0)

m.c959 = Constraint(expr=   m.x181 >= 0)

m.c960 = Constraint(expr=   m.x182 >= 0)

m.c961 = Constraint(expr=   m.x183 >= 0)

m.c962 = Constraint(expr= - 5*m.x104 + m.x184 >= 0)

m.c963 = Constraint(expr= - 5*m.x105 + m.x185 >= 0)

m.c964 = Constraint(expr=   m.x186 >= 0)

m.c965 = Constraint(expr=   m.x187 >= 0)

m.c966 = Constraint(expr=   m.x188 >= 0)

m.c967 = Constraint(expr=   m.x189 >= 0)

m.c968 = Constraint(expr=   m.x190 >= 0)

m.c969 = Constraint(expr=   m.x191 >= 0)

m.c970 = Constraint(expr= - 5*m.x112 + m.x192 >= 0)

m.c971 = Constraint(expr= - 5*m.x113 + m.x193 >= 0)

m.c972 = Constraint(expr=   m.x194 >= 0)

m.c973 = Constraint(expr=   m.x195 >= 0)

m.c974 = Constraint(expr=   m.x196 >= 0)

m.c975 = Constraint(expr=   m.x197 >= 0)

m.c976 = Constraint(expr=   m.x198 >= 0)

m.c977 = Constraint(expr=   m.x199 >= 0)

m.c978 = Constraint(expr= - 5*m.x120 + m.x200 >= 0)

m.c979 = Constraint(expr= - 5*m.x121 + m.x201 >= 0)

m.c980 = Constraint(expr= - 50*m.x82 + m.x162 <= 0)

m.c981 = Constraint(expr= - 50*m.x83 + m.x163 <= 0)

m.c982 = Constraint(expr= - 50*m.x84 + m.x164 <= 0)

m.c983 = Constraint(expr= - 50*m.x85 + m.x165 <= 0)

m.c984 = Constraint(expr= - 50*m.x86 + m.x166 <= 0)

m.c985 = Constraint(expr= - 50*m.x87 + m.x167 <= 0)

m.c986 = Constraint(expr= - 50*m.x88 + m.x168 <= 0)

m.c987 = Constraint(expr= - 50*m.x89 + m.x169 <= 0)

m.c988 = Constraint(expr= - 50*m.x90 + m.x170 <= 0)

m.c989 = Constraint(expr= - 50*m.x91 + m.x171 <= 0)

m.c990 = Constraint(expr= - 50*m.x92 + m.x172 <= 0)

m.c991 = Constraint(expr= - 50*m.x93 + m.x173 <= 0)

m.c992 = Constraint(expr= - 50*m.x94 + m.x174 <= 0)

m.c993 = Constraint(expr= - 50*m.x95 + m.x175 <= 0)

m.c994 = Constraint(expr= - 50*m.x96 + m.x176 <= 0)

m.c995 = Constraint(expr= - 50*m.x97 + m.x177 <= 0)

m.c996 = Constraint(expr= - 50*m.x98 + m.x178 <= 0)

m.c997 = Constraint(expr= - 50*m.x99 + m.x179 <= 0)

m.c998 = Constraint(expr= - 50*m.x100 + m.x180 <= 0)

m.c999 = Constraint(expr= - 50*m.x101 + m.x181 <= 0)

m.c1000 = Constraint(expr= - 50*m.x102 + m.x182 <= 0)

m.c1001 = Constraint(expr= - 50*m.x103 + m.x183 <= 0)

m.c1002 = Constraint(expr= - 50*m.x104 + m.x184 <= 0)

m.c1003 = Constraint(expr= - 50*m.x105 + m.x185 <= 0)

m.c1004 = Constraint(expr= - 50*m.x106 + m.x186 <= 0)

m.c1005 = Constraint(expr= - 50*m.x107 + m.x187 <= 0)

m.c1006 = Constraint(expr= - 50*m.x108 + m.x188 <= 0)

m.c1007 = Constraint(expr= - 50*m.x109 + m.x189 <= 0)

m.c1008 = Constraint(expr= - 50*m.x110 + m.x190 <= 0)

m.c1009 = Constraint(expr= - 50*m.x111 + m.x191 <= 0)

m.c1010 = Constraint(expr= - 50*m.x112 + m.x192 <= 0)

m.c1011 = Constraint(expr= - 50*m.x113 + m.x193 <= 0)

m.c1012 = Constraint(expr= - 50*m.x114 + m.x194 <= 0)

m.c1013 = Constraint(expr= - 50*m.x115 + m.x195 <= 0)

m.c1014 = Constraint(expr= - 50*m.x116 + m.x196 <= 0)

m.c1015 = Constraint(expr= - 50*m.x117 + m.x197 <= 0)

m.c1016 = Constraint(expr= - 50*m.x118 + m.x198 <= 0)

m.c1017 = Constraint(expr= - 50*m.x119 + m.x199 <= 0)

m.c1018 = Constraint(expr= - 50*m.x120 + m.x200 <= 0)

m.c1019 = Constraint(expr= - 50*m.x121 + m.x201 <= 0)

m.c1020 = Constraint(expr=   m.x88 + m.x89 + m.x96 + m.x97 + m.x104 + m.x105 + m.x112 + m.x113 + m.x120 + m.x121 == 8)

m.c1021 = Constraint(expr=   m.x168 + m.x176 + m.x184 + m.x192 + m.x200 >= 100)

m.c1022 = Constraint(expr=   m.x169 + m.x177 + m.x185 + m.x193 + m.x201 >= 100)

m.c1023 = Constraint(expr=   m.x168 + m.x176 + m.x184 + m.x192 + m.x200 <= 100)

m.c1024 = Constraint(expr=   m.x169 + m.x177 + m.x185 + m.x193 + m.x201 <= 100)

m.c1025 = Constraint(expr= - 0.15*m.x168 + 0.1*m.x226 + 0.6*m.x227 + 0.2*m.x228 + 0.5*m.x229 >= 0)

m.c1026 = Constraint(expr= - 0.45*m.x169 + 0.1*m.x230 + 0.6*m.x231 + 0.2*m.x232 + 0.5*m.x233 >= 0)

m.c1027 = Constraint(expr= - 0.15*m.x176 + 0.1*m.x258 + 0.6*m.x259 + 0.2*m.x260 + 0.5*m.x261 >= 0)

m.c1028 = Constraint(expr= - 0.45*m.x177 + 0.1*m.x262 + 0.6*m.x263 + 0.2*m.x264 + 0.5*m.x265 >= 0)

m.c1029 = Constraint(expr= - 0.15*m.x184 + 0.1*m.x290 + 0.6*m.x291 + 0.2*m.x292 + 0.5*m.x293 >= 0)

m.c1030 = Constraint(expr= - 0.45*m.x185 + 0.1*m.x294 + 0.6*m.x295 + 0.2*m.x296 + 0.5*m.x297 >= 0)

m.c1031 = Constraint(expr= - 0.15*m.x192 + 0.1*m.x322 + 0.6*m.x323 + 0.2*m.x324 + 0.5*m.x325 >= 0)

m.c1032 = Constraint(expr= - 0.45*m.x193 + 0.1*m.x326 + 0.6*m.x327 + 0.2*m.x328 + 0.5*m.x329 >= 0)

m.c1033 = Constraint(expr= - 0.15*m.x200 + 0.1*m.x354 + 0.6*m.x355 + 0.2*m.x356 + 0.5*m.x357 >= 0)

m.c1034 = Constraint(expr= - 0.45*m.x201 + 0.1*m.x358 + 0.6*m.x359 + 0.2*m.x360 + 0.5*m.x361 >= 0)

m.c1035 = Constraint(expr= - 0.25*m.x168 + 0.1*m.x226 + 0.6*m.x227 + 0.2*m.x228 + 0.5*m.x229 <= 0)

m.c1036 = Constraint(expr= - 0.55*m.x169 + 0.1*m.x230 + 0.6*m.x231 + 0.2*m.x232 + 0.5*m.x233 <= 0)

m.c1037 = Constraint(expr= - 0.25*m.x176 + 0.1*m.x258 + 0.6*m.x259 + 0.2*m.x260 + 0.5*m.x261 <= 0)

m.c1038 = Constraint(expr= - 0.55*m.x177 + 0.1*m.x262 + 0.6*m.x263 + 0.2*m.x264 + 0.5*m.x265 <= 0)

m.c1039 = Constraint(expr= - 0.25*m.x184 + 0.1*m.x290 + 0.6*m.x291 + 0.2*m.x292 + 0.5*m.x293 <= 0)

m.c1040 = Constraint(expr= - 0.55*m.x185 + 0.1*m.x294 + 0.6*m.x295 + 0.2*m.x296 + 0.5*m.x297 <= 0)

m.c1041 = Constraint(expr= - 0.25*m.x192 + 0.1*m.x322 + 0.6*m.x323 + 0.2*m.x324 + 0.5*m.x325 <= 0)

m.c1042 = Constraint(expr= - 0.55*m.x193 + 0.1*m.x326 + 0.6*m.x327 + 0.2*m.x328 + 0.5*m.x329 <= 0)

m.c1043 = Constraint(expr= - 0.25*m.x200 + 0.1*m.x354 + 0.6*m.x355 + 0.2*m.x356 + 0.5*m.x357 <= 0)

m.c1044 = Constraint(expr= - 0.55*m.x201 + 0.1*m.x358 + 0.6*m.x359 + 0.2*m.x360 + 0.5*m.x361 <= 0)

m.c1045 = Constraint(expr= - m.x162 - m.x170 - m.x178 - m.x186 - m.x194 >= -100)

m.c1046 = Constraint(expr= - m.x163 - m.x171 - m.x179 - m.x187 - m.x195 >= -100)

m.c1047 = Constraint(expr=   m.x162 - m.x164 - m.x165 + m.x170 - m.x172 - m.x173 + m.x178 - m.x180 - m.x181 + m.x186
                           - m.x188 - m.x189 + m.x194 - m.x196 - m.x197 >= -25)

m.c1048 = Constraint(expr=   m.x163 - m.x166 - m.x167 + m.x171 - m.x174 - m.x175 + m.x179 - m.x182 - m.x183 + m.x187
                           - m.x190 - m.x191 + m.x195 - m.x198 - m.x199 >= -75)

m.c1049 = Constraint(expr=   m.x164 + m.x166 - m.x168 + m.x172 + m.x174 - m.x176 + m.x180 + m.x182 - m.x184 + m.x188
                           + m.x190 - m.x192 + m.x196 + m.x198 - m.x200 >= -50)

m.c1050 = Constraint(expr=   m.x165 + m.x167 - m.x169 + m.x173 + m.x175 - m.x177 + m.x181 + m.x183 - m.x185 + m.x189
                           + m.x191 - m.x193 + m.x197 + m.x199 - m.x201 >= -50)

m.c1051 = Constraint(expr=   m.x168 + m.x169 + m.x176 + m.x177 + m.x184 + m.x185 + m.x192 + m.x193 + m.x200 + m.x201
                           >= 0)

m.c1052 = Constraint(expr= - m.x162 - m.x170 - m.x178 - m.x186 - m.x194 <= 0)

m.c1053 = Constraint(expr= - m.x163 - m.x171 - m.x179 - m.x187 - m.x195 <= 0)

m.c1054 = Constraint(expr=   m.x162 - m.x164 - m.x165 + m.x170 - m.x172 - m.x173 + m.x178 - m.x180 - m.x181 + m.x186
                           - m.x188 - m.x189 + m.x194 - m.x196 - m.x197 <= 75)

m.c1055 = Constraint(expr=   m.x163 - m.x166 - m.x167 + m.x171 - m.x174 - m.x175 + m.x179 - m.x182 - m.x183 + m.x187
                           - m.x190 - m.x191 + m.x195 - m.x198 - m.x199 <= 25)

m.c1056 = Constraint(expr=   m.x164 + m.x166 - m.x168 + m.x172 + m.x174 - m.x176 + m.x180 + m.x182 - m.x184 + m.x188
                           + m.x190 - m.x192 + m.x196 + m.x198 - m.x200 <= 50)

m.c1057 = Constraint(expr=   m.x165 + m.x167 - m.x169 + m.x173 + m.x175 - m.x177 + m.x181 + m.x183 - m.x185 + m.x189
                           + m.x191 - m.x193 + m.x197 + m.x199 - m.x201 <= 50)

m.c1058 = Constraint(expr= - m.x202 - m.x234 - m.x266 - m.x298 - m.x330 >= -100)

m.c1059 = Constraint(expr= - m.x203 - m.x235 - m.x267 - m.x299 - m.x331 >= 0)

m.c1060 = Constraint(expr= - m.x204 - m.x236 - m.x268 - m.x300 - m.x332 >= 0)

m.c1061 = Constraint(expr= - m.x205 - m.x237 - m.x269 - m.x301 - m.x333 >= 0)

m.c1062 = Constraint(expr= - m.x206 - m.x238 - m.x270 - m.x302 - m.x334 >= 0)

m.c1063 = Constraint(expr= - m.x207 - m.x239 - m.x271 - m.x303 - m.x335 >= -100)

m.c1064 = Constraint(expr= - m.x208 - m.x240 - m.x272 - m.x304 - m.x336 >= 0)

m.c1065 = Constraint(expr= - m.x209 - m.x241 - m.x273 - m.x305 - m.x337 >= 0)

m.c1066 = Constraint(expr=   m.x202 - m.x210 - m.x214 + m.x234 - m.x242 - m.x246 + m.x266 - m.x274 - m.x278 + m.x298
                           - m.x306 - m.x310 + m.x330 - m.x338 - m.x342 >= -25)

m.c1067 = Constraint(expr=   m.x203 - m.x211 - m.x215 + m.x235 - m.x243 - m.x247 + m.x267 - m.x275 - m.x279 + m.x299
                           - m.x307 - m.x311 + m.x331 - m.x339 - m.x343 >= 0)

m.c1068 = Constraint(expr=   m.x204 - m.x212 - m.x216 + m.x236 - m.x244 - m.x248 + m.x268 - m.x276 - m.x280 + m.x300
                           - m.x308 - m.x312 + m.x332 - m.x340 - m.x344 >= 0)

m.c1069 = Constraint(expr=   m.x205 - m.x213 - m.x217 + m.x237 - m.x245 - m.x249 + m.x269 - m.x277 - m.x281 + m.x301
                           - m.x309 - m.x313 + m.x333 - m.x341 - m.x345 >= 0)

m.c1070 = Constraint(expr=   m.x206 - m.x218 - m.x222 + m.x238 - m.x250 - m.x254 + m.x270 - m.x282 - m.x286 + m.x302
                           - m.x314 - m.x318 + m.x334 - m.x346 - m.x350 >= 0)

m.c1071 = Constraint(expr=   m.x207 - m.x219 - m.x223 + m.x239 - m.x251 - m.x255 + m.x271 - m.x283 - m.x287 + m.x303
                           - m.x315 - m.x319 + m.x335 - m.x347 - m.x351 >= -75)

m.c1072 = Constraint(expr=   m.x208 - m.x220 - m.x224 + m.x240 - m.x252 - m.x256 + m.x272 - m.x284 - m.x288 + m.x304
                           - m.x316 - m.x320 + m.x336 - m.x348 - m.x352 >= 0)

m.c1073 = Constraint(expr=   m.x209 - m.x221 - m.x225 + m.x241 - m.x253 - m.x257 + m.x273 - m.x285 - m.x289 + m.x305
                           - m.x317 - m.x321 + m.x337 - m.x349 - m.x353 >= 0)

m.c1074 = Constraint(expr=   m.x210 + m.x218 - m.x226 + m.x242 + m.x250 - m.x258 + m.x274 + m.x282 - m.x290 + m.x306
                           + m.x314 - m.x322 + m.x338 + m.x346 - m.x354 >= 0)

m.c1075 = Constraint(expr=   m.x211 + m.x219 - m.x227 + m.x243 + m.x251 - m.x259 + m.x275 + m.x283 - m.x291 + m.x307
                           + m.x315 - m.x323 + m.x339 + m.x347 - m.x355 >= 0)

m.c1076 = Constraint(expr=   m.x212 + m.x220 - m.x228 + m.x244 + m.x252 - m.x260 + m.x276 + m.x284 - m.x292 + m.x308
                           + m.x316 - m.x324 + m.x340 + m.x348 - m.x356 >= -50)

m.c1077 = Constraint(expr=   m.x213 + m.x221 - m.x229 + m.x245 + m.x253 - m.x261 + m.x277 + m.x285 - m.x293 + m.x309
                           + m.x317 - m.x325 + m.x341 + m.x349 - m.x357 >= 0)

m.c1078 = Constraint(expr=   m.x214 + m.x222 - m.x230 + m.x246 + m.x254 - m.x262 + m.x278 + m.x286 - m.x294 + m.x310
                           + m.x318 - m.x326 + m.x342 + m.x350 - m.x358 >= 0)

m.c1079 = Constraint(expr=   m.x215 + m.x223 - m.x231 + m.x247 + m.x255 - m.x263 + m.x279 + m.x287 - m.x295 + m.x311
                           + m.x319 - m.x327 + m.x343 + m.x351 - m.x359 >= 0)

m.c1080 = Constraint(expr=   m.x216 + m.x224 - m.x232 + m.x248 + m.x256 - m.x264 + m.x280 + m.x288 - m.x296 + m.x312
                           + m.x320 - m.x328 + m.x344 + m.x352 - m.x360 >= 0)

m.c1081 = Constraint(expr=   m.x217 + m.x225 - m.x233 + m.x249 + m.x257 - m.x265 + m.x281 + m.x289 - m.x297 + m.x313
                           + m.x321 - m.x329 + m.x345 + m.x353 - m.x361 >= -50)

m.c1082 = Constraint(expr=   m.x226 + m.x230 + m.x258 + m.x262 + m.x290 + m.x294 + m.x322 + m.x326 + m.x354 + m.x358
                           >= 0)

m.c1083 = Constraint(expr=   m.x227 + m.x231 + m.x259 + m.x263 + m.x291 + m.x295 + m.x323 + m.x327 + m.x355 + m.x359
                           >= 0)

m.c1084 = Constraint(expr=   m.x228 + m.x232 + m.x260 + m.x264 + m.x292 + m.x296 + m.x324 + m.x328 + m.x356 + m.x360
                           >= 0)

m.c1085 = Constraint(expr=   m.x229 + m.x233 + m.x261 + m.x265 + m.x293 + m.x297 + m.x325 + m.x329 + m.x357 + m.x361
                           >= 0)

m.c1086 = Constraint(expr= - m.x202 - m.x234 - m.x266 - m.x298 - m.x330 <= 0)

m.c1087 = Constraint(expr= - m.x203 - m.x235 - m.x267 - m.x299 - m.x331 <= 100)

m.c1088 = Constraint(expr= - m.x204 - m.x236 - m.x268 - m.x300 - m.x332 <= 100)

m.c1089 = Constraint(expr= - m.x205 - m.x237 - m.x269 - m.x301 - m.x333 <= 100)

m.c1090 = Constraint(expr= - m.x206 - m.x238 - m.x270 - m.x302 - m.x334 <= 100)

m.c1091 = Constraint(expr= - m.x207 - m.x239 - m.x271 - m.x303 - m.x335 <= 0)

m.c1092 = Constraint(expr= - m.x208 - m.x240 - m.x272 - m.x304 - m.x336 <= 100)

m.c1093 = Constraint(expr= - m.x209 - m.x241 - m.x273 - m.x305 - m.x337 <= 100)

m.c1094 = Constraint(expr=   m.x202 - m.x210 - m.x214 + m.x234 - m.x242 - m.x246 + m.x266 - m.x274 - m.x278 + m.x298
                           - m.x306 - m.x310 + m.x330 - m.x338 - m.x342 <= 75)

m.c1095 = Constraint(expr=   m.x203 - m.x211 - m.x215 + m.x235 - m.x243 - m.x247 + m.x267 - m.x275 - m.x279 + m.x299
                           - m.x307 - m.x311 + m.x331 - m.x339 - m.x343 <= 100)

m.c1096 = Constraint(expr=   m.x204 - m.x212 - m.x216 + m.x236 - m.x244 - m.x248 + m.x268 - m.x276 - m.x280 + m.x300
                           - m.x308 - m.x312 + m.x332 - m.x340 - m.x344 <= 100)

m.c1097 = Constraint(expr=   m.x205 - m.x213 - m.x217 + m.x237 - m.x245 - m.x249 + m.x269 - m.x277 - m.x281 + m.x301
                           - m.x309 - m.x313 + m.x333 - m.x341 - m.x345 <= 100)

m.c1098 = Constraint(expr=   m.x206 - m.x218 - m.x222 + m.x238 - m.x250 - m.x254 + m.x270 - m.x282 - m.x286 + m.x302
                           - m.x314 - m.x318 + m.x334 - m.x346 - m.x350 <= 100)

m.c1099 = Constraint(expr=   m.x207 - m.x219 - m.x223 + m.x239 - m.x251 - m.x255 + m.x271 - m.x283 - m.x287 + m.x303
                           - m.x315 - m.x319 + m.x335 - m.x347 - m.x351 <= 25)

m.c1100 = Constraint(expr=   m.x208 - m.x220 - m.x224 + m.x240 - m.x252 - m.x256 + m.x272 - m.x284 - m.x288 + m.x304
                           - m.x316 - m.x320 + m.x336 - m.x348 - m.x352 <= 100)

m.c1101 = Constraint(expr=   m.x209 - m.x221 - m.x225 + m.x241 - m.x253 - m.x257 + m.x273 - m.x285 - m.x289 + m.x305
                           - m.x317 - m.x321 + m.x337 - m.x349 - m.x353 <= 100)

m.c1102 = Constraint(expr=   m.x210 + m.x218 - m.x226 + m.x242 + m.x250 - m.x258 + m.x274 + m.x282 - m.x290 + m.x306
                           + m.x314 - m.x322 + m.x338 + m.x346 - m.x354 <= 100)

m.c1103 = Constraint(expr=   m.x211 + m.x219 - m.x227 + m.x243 + m.x251 - m.x259 + m.x275 + m.x283 - m.x291 + m.x307
                           + m.x315 - m.x323 + m.x339 + m.x347 - m.x355 <= 100)

m.c1104 = Constraint(expr=   m.x212 + m.x220 - m.x228 + m.x244 + m.x252 - m.x260 + m.x276 + m.x284 - m.x292 + m.x308
                           + m.x316 - m.x324 + m.x340 + m.x348 - m.x356 <= 50)

m.c1105 = Constraint(expr=   m.x213 + m.x221 - m.x229 + m.x245 + m.x253 - m.x261 + m.x277 + m.x285 - m.x293 + m.x309
                           + m.x317 - m.x325 + m.x341 + m.x349 - m.x357 <= 100)

m.c1106 = Constraint(expr=   m.x214 + m.x222 - m.x230 + m.x246 + m.x254 - m.x262 + m.x278 + m.x286 - m.x294 + m.x310
                           + m.x318 - m.x326 + m.x342 + m.x350 - m.x358 <= 100)

m.c1107 = Constraint(expr=   m.x215 + m.x223 - m.x231 + m.x247 + m.x255 - m.x263 + m.x279 + m.x287 - m.x295 + m.x311
                           + m.x319 - m.x327 + m.x343 + m.x351 - m.x359 <= 100)

m.c1108 = Constraint(expr=   m.x216 + m.x224 - m.x232 + m.x248 + m.x256 - m.x264 + m.x280 + m.x288 - m.x296 + m.x312
                           + m.x320 - m.x328 + m.x344 + m.x352 - m.x360 <= 100)

m.c1109 = Constraint(expr=   m.x217 + m.x225 - m.x233 + m.x249 + m.x257 - m.x265 + m.x281 + m.x289 - m.x297 + m.x313
                           + m.x321 - m.x329 + m.x345 + m.x353 - m.x361 <= 50)

m.c1110 = Constraint(expr=   8*m.b10 + 8*m.b11 - m.x50 - m.x51 + m.x122 + m.x123 <= 8)

m.c1111 = Constraint(expr=   8*m.b10 + 8*m.b12 - m.x50 - m.x52 + m.x122 + m.x124 <= 8)

m.c1112 = Constraint(expr=   8*m.b10 + 8*m.b13 - m.x50 - m.x53 + m.x122 + m.x125 <= 8)

m.c1113 = Constraint(expr=   8*m.b11 + 8*m.b14 - m.x51 - m.x54 + m.x123 + m.x126 <= 8)

m.c1114 = Constraint(expr=   8*m.b11 + 8*m.b15 - m.x51 - m.x55 + m.x123 + m.x127 <= 8)

m.c1115 = Constraint(expr=   8*m.b12 + 8*m.b16 - m.x52 - m.x56 + m.x124 + m.x128 <= 8)

m.c1116 = Constraint(expr=   8*m.b13 + 8*m.b17 - m.x53 - m.x57 + m.x125 + m.x129 <= 8)

m.c1117 = Constraint(expr=   8*m.b14 + 8*m.b16 - m.x54 - m.x56 + m.x126 + m.x128 <= 8)

m.c1118 = Constraint(expr=   8*m.b15 + 8*m.b17 - m.x55 - m.x57 + m.x127 + m.x129 <= 8)

m.c1119 = Constraint(expr=   8*m.b16 + 8*m.b17 - m.x56 - m.x57 + m.x128 + m.x129 <= 8)

m.c1120 = Constraint(expr=   8*m.b18 + 8*m.b19 - m.x58 - m.x59 + m.x90 + m.x91 + m.x122 + m.x123 <= 8)

m.c1121 = Constraint(expr=   8*m.b18 + 8*m.b20 - m.x58 - m.x60 + m.x90 + m.x92 + m.x122 + m.x124 <= 8)

m.c1122 = Constraint(expr=   8*m.b18 + 8*m.b21 - m.x58 - m.x61 + m.x90 + m.x93 + m.x122 + m.x125 <= 8)

m.c1123 = Constraint(expr=   8*m.b19 + 8*m.b22 - m.x59 - m.x62 + m.x91 + m.x94 + m.x123 + m.x126 <= 8)

m.c1124 = Constraint(expr=   8*m.b19 + 8*m.b23 - m.x59 - m.x63 + m.x91 + m.x95 + m.x123 + m.x127 <= 8)

m.c1125 = Constraint(expr=   8*m.b20 + 8*m.b24 - m.x60 - m.x64 + m.x92 + m.x96 + m.x124 + m.x128 <= 8)

m.c1126 = Constraint(expr=   8*m.b21 + 8*m.b25 - m.x61 - m.x65 + m.x93 + m.x97 + m.x125 + m.x129 <= 8)

m.c1127 = Constraint(expr=   8*m.b22 + 8*m.b24 - m.x62 - m.x64 + m.x94 + m.x96 + m.x126 + m.x128 <= 8)

m.c1128 = Constraint(expr=   8*m.b23 + 8*m.b25 - m.x63 - m.x65 + m.x95 + m.x97 + m.x127 + m.x129 <= 8)

m.c1129 = Constraint(expr=   8*m.b24 + 8*m.b25 - m.x64 - m.x65 + m.x96 + m.x97 + m.x128 + m.x129 <= 8)

m.c1130 = Constraint(expr=   8*m.b26 + 8*m.b27 - m.x66 - m.x67 + m.x90 + m.x91 + m.x98 + m.x99 + m.x122 + m.x123 <= 8)

m.c1131 = Constraint(expr=   8*m.b26 + 8*m.b28 - m.x66 - m.x68 + m.x90 + m.x92 + m.x98 + m.x100 + m.x122 + m.x124 <= 8)

m.c1132 = Constraint(expr=   8*m.b26 + 8*m.b29 - m.x66 - m.x69 + m.x90 + m.x93 + m.x98 + m.x101 + m.x122 + m.x125 <= 8)

m.c1133 = Constraint(expr=   8*m.b27 + 8*m.b30 - m.x67 - m.x70 + m.x91 + m.x94 + m.x99 + m.x102 + m.x123 + m.x126 <= 8)

m.c1134 = Constraint(expr=   8*m.b27 + 8*m.b31 - m.x67 - m.x71 + m.x91 + m.x95 + m.x99 + m.x103 + m.x123 + m.x127 <= 8)

m.c1135 = Constraint(expr=   8*m.b28 + 8*m.b32 - m.x68 - m.x72 + m.x92 + m.x96 + m.x100 + m.x104 + m.x124 + m.x128 <= 8)

m.c1136 = Constraint(expr=   8*m.b29 + 8*m.b33 - m.x69 - m.x73 + m.x93 + m.x97 + m.x101 + m.x105 + m.x125 + m.x129 <= 8)

m.c1137 = Constraint(expr=   8*m.b30 + 8*m.b32 - m.x70 - m.x72 + m.x94 + m.x96 + m.x102 + m.x104 + m.x126 + m.x128 <= 8)

m.c1138 = Constraint(expr=   8*m.b31 + 8*m.b33 - m.x71 - m.x73 + m.x95 + m.x97 + m.x103 + m.x105 + m.x127 + m.x129 <= 8)

m.c1139 = Constraint(expr=   8*m.b32 + 8*m.b33 - m.x72 - m.x73 + m.x96 + m.x97 + m.x104 + m.x105 + m.x128 + m.x129 <= 8)

m.c1140 = Constraint(expr=   8*m.b34 + 8*m.b35 - m.x74 - m.x75 + m.x90 + m.x91 + m.x98 + m.x99 + m.x106 + m.x107
                           + m.x122 + m.x123 <= 8)

m.c1141 = Constraint(expr=   8*m.b34 + 8*m.b36 - m.x74 - m.x76 + m.x90 + m.x92 + m.x98 + m.x100 + m.x106 + m.x108
                           + m.x122 + m.x124 <= 8)

m.c1142 = Constraint(expr=   8*m.b34 + 8*m.b37 - m.x74 - m.x77 + m.x90 + m.x93 + m.x98 + m.x101 + m.x106 + m.x109
                           + m.x122 + m.x125 <= 8)

m.c1143 = Constraint(expr=   8*m.b35 + 8*m.b38 - m.x75 - m.x78 + m.x91 + m.x94 + m.x99 + m.x102 + m.x107 + m.x110
                           + m.x123 + m.x126 <= 8)

m.c1144 = Constraint(expr=   8*m.b35 + 8*m.b39 - m.x75 - m.x79 + m.x91 + m.x95 + m.x99 + m.x103 + m.x107 + m.x111
                           + m.x123 + m.x127 <= 8)

m.c1145 = Constraint(expr=   8*m.b36 + 8*m.b40 - m.x76 - m.x80 + m.x92 + m.x96 + m.x100 + m.x104 + m.x108 + m.x112
                           + m.x124 + m.x128 <= 8)

m.c1146 = Constraint(expr=   8*m.b37 + 8*m.b41 - m.x77 - m.x81 + m.x93 + m.x97 + m.x101 + m.x105 + m.x109 + m.x113
                           + m.x125 + m.x129 <= 8)

m.c1147 = Constraint(expr=   8*m.b38 + 8*m.b40 - m.x78 - m.x80 + m.x94 + m.x96 + m.x102 + m.x104 + m.x110 + m.x112
                           + m.x126 + m.x128 <= 8)

m.c1148 = Constraint(expr=   8*m.b39 + 8*m.b41 - m.x79 - m.x81 + m.x95 + m.x97 + m.x103 + m.x105 + m.x111 + m.x113
                           + m.x127 + m.x129 <= 8)

m.c1149 = Constraint(expr=   8*m.b40 + 8*m.b41 - m.x80 - m.x81 + m.x96 + m.x97 + m.x104 + m.x105 + m.x112 + m.x113
                           + m.x128 + m.x129 <= 8)

m.c1150 = Constraint(expr=   8*m.b18 + 8*m.b19 - m.x58 - m.x59 + m.x130 + m.x131 <= 8)

m.c1151 = Constraint(expr=   8*m.b18 + 8*m.b20 - m.x58 - m.x60 + m.x130 + m.x132 <= 8)

m.c1152 = Constraint(expr=   8*m.b18 + 8*m.b21 - m.x58 - m.x61 + m.x130 + m.x133 <= 8)

m.c1153 = Constraint(expr=   8*m.b19 + 8*m.b22 - m.x59 - m.x62 + m.x131 + m.x134 <= 8)

m.c1154 = Constraint(expr=   8*m.b19 + 8*m.b23 - m.x59 - m.x63 + m.x131 + m.x135 <= 8)

m.c1155 = Constraint(expr=   8*m.b20 + 8*m.b24 - m.x60 - m.x64 + m.x132 + m.x136 <= 8)

m.c1156 = Constraint(expr=   8*m.b21 + 8*m.b25 - m.x61 - m.x65 + m.x133 + m.x137 <= 8)

m.c1157 = Constraint(expr=   8*m.b22 + 8*m.b24 - m.x62 - m.x64 + m.x134 + m.x136 <= 8)

m.c1158 = Constraint(expr=   8*m.b23 + 8*m.b25 - m.x63 - m.x65 + m.x135 + m.x137 <= 8)

m.c1159 = Constraint(expr=   8*m.b24 + 8*m.b25 - m.x64 - m.x65 + m.x136 + m.x137 <= 8)

m.c1160 = Constraint(expr=   8*m.b26 + 8*m.b27 - m.x66 - m.x67 + m.x98 + m.x99 + m.x130 + m.x131 <= 8)

m.c1161 = Constraint(expr=   8*m.b26 + 8*m.b28 - m.x66 - m.x68 + m.x98 + m.x100 + m.x130 + m.x132 <= 8)

m.c1162 = Constraint(expr=   8*m.b26 + 8*m.b29 - m.x66 - m.x69 + m.x98 + m.x101 + m.x130 + m.x133 <= 8)

m.c1163 = Constraint(expr=   8*m.b27 + 8*m.b30 - m.x67 - m.x70 + m.x99 + m.x102 + m.x131 + m.x134 <= 8)

m.c1164 = Constraint(expr=   8*m.b27 + 8*m.b31 - m.x67 - m.x71 + m.x99 + m.x103 + m.x131 + m.x135 <= 8)

m.c1165 = Constraint(expr=   8*m.b28 + 8*m.b32 - m.x68 - m.x72 + m.x100 + m.x104 + m.x132 + m.x136 <= 8)

m.c1166 = Constraint(expr=   8*m.b29 + 8*m.b33 - m.x69 - m.x73 + m.x101 + m.x105 + m.x133 + m.x137 <= 8)

m.c1167 = Constraint(expr=   8*m.b30 + 8*m.b32 - m.x70 - m.x72 + m.x102 + m.x104 + m.x134 + m.x136 <= 8)

m.c1168 = Constraint(expr=   8*m.b31 + 8*m.b33 - m.x71 - m.x73 + m.x103 + m.x105 + m.x135 + m.x137 <= 8)

m.c1169 = Constraint(expr=   8*m.b32 + 8*m.b33 - m.x72 - m.x73 + m.x104 + m.x105 + m.x136 + m.x137 <= 8)

m.c1170 = Constraint(expr=   8*m.b34 + 8*m.b35 - m.x74 - m.x75 + m.x98 + m.x99 + m.x106 + m.x107 + m.x130 + m.x131 <= 8)

m.c1171 = Constraint(expr=   8*m.b34 + 8*m.b36 - m.x74 - m.x76 + m.x98 + m.x100 + m.x106 + m.x108 + m.x130 + m.x132
                           <= 8)

m.c1172 = Constraint(expr=   8*m.b34 + 8*m.b37 - m.x74 - m.x77 + m.x98 + m.x101 + m.x106 + m.x109 + m.x130 + m.x133
                           <= 8)

m.c1173 = Constraint(expr=   8*m.b35 + 8*m.b38 - m.x75 - m.x78 + m.x99 + m.x102 + m.x107 + m.x110 + m.x131 + m.x134
                           <= 8)

m.c1174 = Constraint(expr=   8*m.b35 + 8*m.b39 - m.x75 - m.x79 + m.x99 + m.x103 + m.x107 + m.x111 + m.x131 + m.x135
                           <= 8)

m.c1175 = Constraint(expr=   8*m.b36 + 8*m.b40 - m.x76 - m.x80 + m.x100 + m.x104 + m.x108 + m.x112 + m.x132 + m.x136
                           <= 8)

m.c1176 = Constraint(expr=   8*m.b37 + 8*m.b41 - m.x77 - m.x81 + m.x101 + m.x105 + m.x109 + m.x113 + m.x133 + m.x137
                           <= 8)

m.c1177 = Constraint(expr=   8*m.b38 + 8*m.b40 - m.x78 - m.x80 + m.x102 + m.x104 + m.x110 + m.x112 + m.x134 + m.x136
                           <= 8)

m.c1178 = Constraint(expr=   8*m.b39 + 8*m.b41 - m.x79 - m.x81 + m.x103 + m.x105 + m.x111 + m.x113 + m.x135 + m.x137
                           <= 8)

m.c1179 = Constraint(expr=   8*m.b40 + 8*m.b41 - m.x80 - m.x81 + m.x104 + m.x105 + m.x112 + m.x113 + m.x136 + m.x137
                           <= 8)

m.c1180 = Constraint(expr=   8*m.b26 + 8*m.b27 - m.x66 - m.x67 + m.x138 + m.x139 <= 8)

m.c1181 = Constraint(expr=   8*m.b26 + 8*m.b28 - m.x66 - m.x68 + m.x138 + m.x140 <= 8)

m.c1182 = Constraint(expr=   8*m.b26 + 8*m.b29 - m.x66 - m.x69 + m.x138 + m.x141 <= 8)

m.c1183 = Constraint(expr=   8*m.b27 + 8*m.b30 - m.x67 - m.x70 + m.x139 + m.x142 <= 8)

m.c1184 = Constraint(expr=   8*m.b27 + 8*m.b31 - m.x67 - m.x71 + m.x139 + m.x143 <= 8)

m.c1185 = Constraint(expr=   8*m.b28 + 8*m.b32 - m.x68 - m.x72 + m.x140 + m.x144 <= 8)

m.c1186 = Constraint(expr=   8*m.b29 + 8*m.b33 - m.x69 - m.x73 + m.x141 + m.x145 <= 8)

m.c1187 = Constraint(expr=   8*m.b30 + 8*m.b32 - m.x70 - m.x72 + m.x142 + m.x144 <= 8)

m.c1188 = Constraint(expr=   8*m.b31 + 8*m.b33 - m.x71 - m.x73 + m.x143 + m.x145 <= 8)

m.c1189 = Constraint(expr=   8*m.b32 + 8*m.b33 - m.x72 - m.x73 + m.x144 + m.x145 <= 8)

m.c1190 = Constraint(expr=   8*m.b34 + 8*m.b35 - m.x74 - m.x75 + m.x106 + m.x107 + m.x138 + m.x139 <= 8)

m.c1191 = Constraint(expr=   8*m.b34 + 8*m.b36 - m.x74 - m.x76 + m.x106 + m.x108 + m.x138 + m.x140 <= 8)

m.c1192 = Constraint(expr=   8*m.b34 + 8*m.b37 - m.x74 - m.x77 + m.x106 + m.x109 + m.x138 + m.x141 <= 8)

m.c1193 = Constraint(expr=   8*m.b35 + 8*m.b38 - m.x75 - m.x78 + m.x107 + m.x110 + m.x139 + m.x142 <= 8)

m.c1194 = Constraint(expr=   8*m.b35 + 8*m.b39 - m.x75 - m.x79 + m.x107 + m.x111 + m.x139 + m.x143 <= 8)

m.c1195 = Constraint(expr=   8*m.b36 + 8*m.b40 - m.x76 - m.x80 + m.x108 + m.x112 + m.x140 + m.x144 <= 8)

m.c1196 = Constraint(expr=   8*m.b37 + 8*m.b41 - m.x77 - m.x81 + m.x109 + m.x113 + m.x141 + m.x145 <= 8)

m.c1197 = Constraint(expr=   8*m.b38 + 8*m.b40 - m.x78 - m.x80 + m.x110 + m.x112 + m.x142 + m.x144 <= 8)

m.c1198 = Constraint(expr=   8*m.b39 + 8*m.b41 - m.x79 - m.x81 + m.x111 + m.x113 + m.x143 + m.x145 <= 8)

m.c1199 = Constraint(expr=   8*m.b40 + 8*m.b41 - m.x80 - m.x81 + m.x112 + m.x113 + m.x144 + m.x145 <= 8)

m.c1200 = Constraint(expr=   8*m.b34 + 8*m.b35 - m.x74 - m.x75 + m.x146 + m.x147 <= 8)

m.c1201 = Constraint(expr=   8*m.b34 + 8*m.b36 - m.x74 - m.x76 + m.x146 + m.x148 <= 8)

m.c1202 = Constraint(expr=   8*m.b34 + 8*m.b37 - m.x74 - m.x77 + m.x146 + m.x149 <= 8)

m.c1203 = Constraint(expr=   8*m.b35 + 8*m.b38 - m.x75 - m.x78 + m.x147 + m.x150 <= 8)

m.c1204 = Constraint(expr=   8*m.b35 + 8*m.b39 - m.x75 - m.x79 + m.x147 + m.x151 <= 8)

m.c1205 = Constraint(expr=   8*m.b36 + 8*m.b40 - m.x76 - m.x80 + m.x148 + m.x152 <= 8)

m.c1206 = Constraint(expr=   8*m.b37 + 8*m.b41 - m.x77 - m.x81 + m.x149 + m.x153 <= 8)

m.c1207 = Constraint(expr=   8*m.b38 + 8*m.b40 - m.x78 - m.x80 + m.x150 + m.x152 <= 8)

m.c1208 = Constraint(expr=   8*m.b39 + 8*m.b41 - m.x79 - m.x81 + m.x151 + m.x153 <= 8)

m.c1209 = Constraint(expr=   8*m.b40 + 8*m.b41 - m.x80 - m.x81 + m.x152 + m.x153 <= 8)

m.c1210 = Constraint(expr= - m.b3 - m.b4 - m.b5 + m.b10 <= 0)

m.c1211 = Constraint(expr= - m.b2 - m.b6 - m.b7 + m.b11 <= 0)

m.c1212 = Constraint(expr= - m.b2 - m.b8 + m.b12 <= 0)

m.c1213 = Constraint(expr= - m.b2 - m.b9 + m.b13 <= 0)

m.c1214 = Constraint(expr= - m.b3 - m.b8 + m.b14 <= 0)

m.c1215 = Constraint(expr= - m.b3 - m.b9 + m.b15 <= 0)

m.c1216 = Constraint(expr= - m.b4 - m.b6 - m.b9 + m.b16 <= 0)

m.c1217 = Constraint(expr= - m.b5 - m.b7 - m.b8 + m.b17 <= 0)

m.c1218 = Constraint(expr= - m.b11 - m.b12 - m.b13 + m.b18 <= 0)

m.c1219 = Constraint(expr= - m.b10 - m.b14 - m.b15 + m.b19 <= 0)

m.c1220 = Constraint(expr= - m.b10 - m.b16 + m.b20 <= 0)

m.c1221 = Constraint(expr= - m.b10 - m.b17 + m.b21 <= 0)

m.c1222 = Constraint(expr= - m.b11 - m.b16 + m.b22 <= 0)

m.c1223 = Constraint(expr= - m.b11 - m.b17 + m.b23 <= 0)

m.c1224 = Constraint(expr= - m.b12 - m.b14 - m.b17 + m.b24 <= 0)

m.c1225 = Constraint(expr= - m.b13 - m.b15 - m.b16 + m.b25 <= 0)

m.c1226 = Constraint(expr= - m.b19 - m.b20 - m.b21 + m.b26 <= 0)

m.c1227 = Constraint(expr= - m.b18 - m.b22 - m.b23 + m.b27 <= 0)

m.c1228 = Constraint(expr= - m.b18 - m.b24 + m.b28 <= 0)

m.c1229 = Constraint(expr= - m.b18 - m.b25 + m.b29 <= 0)

m.c1230 = Constraint(expr= - m.b19 - m.b24 + m.b30 <= 0)

m.c1231 = Constraint(expr= - m.b19 - m.b25 + m.b31 <= 0)

m.c1232 = Constraint(expr= - m.b20 - m.b22 - m.b25 + m.b32 <= 0)

m.c1233 = Constraint(expr= - m.b21 - m.b23 - m.b24 + m.b33 <= 0)

m.c1234 = Constraint(expr= - m.b27 - m.b28 - m.b29 + m.b34 <= 0)

m.c1235 = Constraint(expr= - m.b26 - m.b30 - m.b31 + m.b35 <= 0)

m.c1236 = Constraint(expr= - m.b26 - m.b32 + m.b36 <= 0)

m.c1237 = Constraint(expr= - m.b26 - m.b33 + m.b37 <= 0)

m.c1238 = Constraint(expr= - m.b27 - m.b32 + m.b38 <= 0)

m.c1239 = Constraint(expr= - m.b27 - m.b33 + m.b39 <= 0)

m.c1240 = Constraint(expr= - m.b28 - m.b30 - m.b33 + m.b40 <= 0)

m.c1241 = Constraint(expr= - m.b29 - m.b31 - m.b32 + m.b41 <= 0)
