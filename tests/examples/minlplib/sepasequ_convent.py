#  MINLP written by GAMS Convert at 04/21/18 13:54:10
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       1129      353      236      540        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        642      622       20        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       4319     2899     1420        0
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
m.x21 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x22 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x23 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x24 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x25 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x26 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x27 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x28 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x29 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x30 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x31 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x32 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x33 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x34 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x35 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x36 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x37 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x38 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x39 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x40 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x41 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x42 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x43 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x44 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x45 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x46 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x47 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x48 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x49 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x50 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x51 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x52 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x53 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x54 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x55 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x56 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x57 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x58 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x59 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x60 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x61 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x62 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x63 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x64 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x65 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x66 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x67 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x68 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x69 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x70 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x71 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x72 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x73 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x74 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x75 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x76 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x77 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x78 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x79 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x80 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x81 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x82 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x83 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x84 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x85 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x86 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x87 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x88 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x89 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x90 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x91 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x92 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x93 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x94 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x95 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x96 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x97 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x98 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x99 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x100 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x101 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x102 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x103 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x104 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x105 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x106 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x107 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x108 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x109 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x110 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x111 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x112 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x113 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x114 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x115 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x116 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x117 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x118 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x119 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x120 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x121 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x122 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x123 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x124 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x125 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x126 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x127 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x128 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x129 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x130 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x131 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x132 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x133 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x134 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x135 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x136 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x137 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x138 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x139 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x140 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x141 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x142 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x143 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x144 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x145 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x146 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x147 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x148 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x149 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x150 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x151 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x152 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x153 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x154 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x155 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x156 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x157 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x158 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x159 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x160 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x161 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x162 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x163 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x164 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x165 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x166 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x167 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x168 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x169 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x170 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x171 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x172 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x173 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x174 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x175 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x176 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x177 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x178 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x179 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x180 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x181 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x182 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x183 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x184 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x185 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x186 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x187 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x188 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x189 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x190 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x191 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x192 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x193 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x194 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x195 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x196 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x197 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x198 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x199 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x200 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x201 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x202 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x203 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x204 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x205 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x206 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x207 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x208 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x209 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x210 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x211 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x212 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x213 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x214 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x215 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x216 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x217 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x218 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x219 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x220 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x221 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x222 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x223 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x224 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x225 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x226 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x227 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x228 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x229 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x230 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x231 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x232 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x233 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x234 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x235 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x236 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x237 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x238 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x239 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x240 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x241 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x242 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x243 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x244 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x245 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x246 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x247 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x248 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x249 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x250 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x251 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x252 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x253 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x254 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x255 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x256 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x257 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x258 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x259 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x260 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x261 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x262 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x263 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x264 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x265 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x266 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x267 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x268 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x269 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x270 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x271 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x272 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x273 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x274 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x275 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x276 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x277 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x278 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x279 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x280 = Var(within=Reals,bounds=(0,2),initialize=2)
m.x281 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x282 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x283 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x284 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x285 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x286 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x287 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x288 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x289 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x290 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x291 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x292 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x293 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x294 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x295 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x296 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x297 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x298 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x299 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x300 = Var(within=Reals,bounds=(0,0.6),initialize=0.6)
m.x301 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x302 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x303 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x304 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x305 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x306 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x307 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x308 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x309 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x310 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x311 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x312 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x313 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x314 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x315 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x316 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x317 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x318 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x319 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x320 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x321 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x322 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x323 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x324 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x325 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x326 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x327 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x328 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x329 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x330 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x331 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x332 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x333 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x334 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x335 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x336 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x337 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x338 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x339 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x340 = Var(within=Reals,bounds=(0,0.2),initialize=0.2)
m.x341 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x342 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x343 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x344 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x345 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x346 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x347 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x348 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x349 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x350 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x351 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x352 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x353 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x354 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x355 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x356 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x357 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x358 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x359 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x360 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x361 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x362 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x363 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x364 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x365 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x366 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x367 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x368 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x369 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x370 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x371 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x372 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x373 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x374 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x375 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x376 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x377 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x378 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x379 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x380 = Var(within=Reals,bounds=(0,0.4),initialize=0.4)
m.x381 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x382 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x383 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x384 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x385 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x386 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x387 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x388 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x389 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x390 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x391 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x392 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x393 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x394 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x395 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x396 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x397 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x398 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x399 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x400 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x401 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x402 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x403 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x404 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x405 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x406 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x407 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x408 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x409 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x410 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x411 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x412 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x413 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x414 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x415 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x416 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x417 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x418 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x419 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x420 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x421 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x422 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x423 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x424 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x425 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x426 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x427 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x428 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x429 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x430 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x431 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x432 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x433 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x434 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x435 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x436 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x437 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x438 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x439 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x440 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x441 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x442 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x443 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x444 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x445 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x446 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x447 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x448 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x449 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x450 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x451 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x452 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x453 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x454 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x455 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x456 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x457 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x458 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x459 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x460 = Var(within=Reals,bounds=(0,40),initialize=10)
m.x461 = Var(within=Reals,bounds=(4.05,10.49),initialize=7.27)
m.x462 = Var(within=Reals,bounds=(1.77,4.03),initialize=2.9)
m.x463 = Var(within=Reals,bounds=(1.32,1.75),initialize=1.535)
m.x464 = Var(within=Reals,bounds=(1.01,1.3),initialize=1.155)
m.x465 = Var(within=Reals,bounds=(4.05,10.49),initialize=7.27)
m.x466 = Var(within=Reals,bounds=(1.77,4.03),initialize=2.9)
m.x467 = Var(within=Reals,bounds=(1.32,1.75),initialize=1.535)
m.x468 = Var(within=Reals,bounds=(1.77,4.03),initialize=2.9)
m.x469 = Var(within=Reals,bounds=(1.32,1.75),initialize=1.535)
m.x470 = Var(within=Reals,bounds=(1.01,1.3),initialize=1.155)
m.x471 = Var(within=Reals,bounds=(4.05,10.49),initialize=7.27)
m.x472 = Var(within=Reals,bounds=(1.77,4.03),initialize=2.9)
m.x473 = Var(within=Reals,bounds=(1.77,4.03),initialize=2.9)
m.x474 = Var(within=Reals,bounds=(1.32,1.75),initialize=1.535)
m.x475 = Var(within=Reals,bounds=(1.32,1.75),initialize=1.535)
m.x476 = Var(within=Reals,bounds=(1.01,1.3),initialize=1.155)
m.x477 = Var(within=Reals,bounds=(4.05,10.49),initialize=7.27)
m.x478 = Var(within=Reals,bounds=(1.77,4.03),initialize=2.9)
m.x479 = Var(within=Reals,bounds=(1.32,1.75),initialize=1.535)
m.x480 = Var(within=Reals,bounds=(1.01,1.3),initialize=1.155)
m.x481 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x482 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x483 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x484 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x485 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x486 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x487 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x488 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x489 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x490 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x491 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x492 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x493 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x494 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x495 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x496 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x497 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x498 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x499 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x500 = Var(within=Reals,bounds=(0,10),initialize=0.4)
m.x501 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x502 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x503 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x504 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x505 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x506 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x507 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x508 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x509 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x510 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x511 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x512 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x513 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x514 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x515 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x516 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x517 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x518 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x519 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x520 = Var(within=Reals,bounds=(0,10),initialize=0.3)
m.x521 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x522 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x523 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x524 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x525 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x526 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x527 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x528 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x529 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x530 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x531 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x532 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x533 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x534 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x535 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x536 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x537 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x538 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x539 = Var(within=Reals,bounds=(0.1,25),initialize=2)
m.x540 = Var(within=Reals,bounds=(0.1,25),initialize=2)
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
m.x582 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x583 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x584 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x585 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x586 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x587 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x588 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x589 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x590 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x591 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x592 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x593 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x594 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x595 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x596 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x597 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x598 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x599 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x600 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x601 = Var(within=Reals,bounds=(0,100),initialize=5)
m.x602 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x603 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x604 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x605 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x606 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x607 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x608 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x609 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x610 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x611 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x612 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x613 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x614 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x615 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x616 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x617 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x618 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x619 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x620 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x621 = Var(within=Reals,bounds=(0,1000),initialize=0)
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

m.obj = Objective(expr=   3*m.b1 + 3*m.b2 + 3*m.b3 + 3*m.b4 + 3*m.b5 + 3*m.b6 + 3*m.b7 + 3*m.b8 + 3*m.b9 + 3*m.b10
                        + 3*m.b11 + 3*m.b12 + 3*m.b13 + 3*m.b14 + 3*m.b15 + 3*m.b16 + 3*m.b17 + 3*m.b18 + 3*m.b19
                        + 3*m.b20 + 81.44*m.x481 + 81.44*m.x482 + 81.44*m.x483 + 81.44*m.x484 + 81.44*m.x485
                        + 81.44*m.x486 + 81.44*m.x487 + 81.44*m.x488 + 81.44*m.x489 + 81.44*m.x490 + 81.44*m.x491
                        + 81.44*m.x492 + 81.44*m.x493 + 81.44*m.x494 + 81.44*m.x495 + 81.44*m.x496 + 81.44*m.x497
                        + 81.44*m.x498 + 81.44*m.x499 + 81.44*m.x500 + 3.04*m.x501 + 3.04*m.x502 + 3.04*m.x503
                        + 3.04*m.x504 + 3.04*m.x505 + 3.04*m.x506 + 3.04*m.x507 + 3.04*m.x508 + 3.04*m.x509
                        + 3.04*m.x510 + 3.04*m.x511 + 3.04*m.x512 + 3.04*m.x513 + 3.04*m.x514 + 3.04*m.x515
                        + 3.04*m.x516 + 3.04*m.x517 + 3.04*m.x518 + 3.04*m.x519 + 3.04*m.x520 + m.x581 + m.x602 + m.x603
                        + m.x604 + m.x605 + m.x606 + m.x607 + m.x608 + m.x609 + m.x610 + m.x611 + m.x612 + m.x613
                        + m.x614 + m.x615 + m.x616 + m.x617 + m.x618 + m.x619 + m.x620 + m.x621, sense=minimize)

m.c1 = Constraint(expr= - m.b2 + m.b17 >= 0)

m.c2 = Constraint(expr= - m.b3 + m.b11 + m.b12 >= 0)

m.c3 = Constraint(expr= - m.b4 + m.b5 + m.b6 + m.b7 >= 0)

m.c4 = Constraint(expr= - m.b6 + m.b17 >= 0)

m.c5 = Constraint(expr= - m.b7 + m.b11 + m.b12 >= 0)

m.c6 = Constraint(expr= - m.b9 + m.b18 >= 0)

m.c7 = Constraint(expr= - m.b10 + m.b13 + m.b14 >= 0)

m.c8 = Constraint(expr= - m.b12 + m.b17 >= 0)

m.c9 = Constraint(expr= - m.b14 + m.b18 >= 0)

m.c10 = Constraint(expr= - m.b16 + m.b19 >= 0)

m.c11 = Constraint(expr= - m.b1 + m.b8 + m.b9 + m.b10 >= 0)

m.c12 = Constraint(expr= - m.b2 + m.b15 + m.b16 >= 0)

m.c13 = Constraint(expr= - m.b3 + m.b20 >= 0)

m.c14 = Constraint(expr= - m.b5 + m.b13 + m.b14 >= 0)

m.c15 = Constraint(expr= - m.b6 + m.b19 >= 0)

m.c16 = Constraint(expr= - m.b8 + m.b15 + m.b16 >= 0)

m.c17 = Constraint(expr= - m.b9 + m.b20 >= 0)

m.c18 = Constraint(expr= - m.b11 + m.b18 >= 0)

m.c19 = Constraint(expr= - m.b13 + m.b19 >= 0)

m.c20 = Constraint(expr= - m.b15 + m.b20 >= 0)

m.c21 = Constraint(expr=   m.b4 - m.b5 >= 0)

m.c22 = Constraint(expr=   m.b4 - m.b6 >= 0)

m.c23 = Constraint(expr=   m.b4 - m.b7 >= 0)

m.c24 = Constraint(expr=   m.b1 - m.b8 >= 0)

m.c25 = Constraint(expr=   m.b1 - m.b9 >= 0)

m.c26 = Constraint(expr=   m.b1 - m.b10 >= 0)

m.c27 = Constraint(expr=   m.b3 + m.b7 - m.b11 >= 0)

m.c28 = Constraint(expr=   m.b3 + m.b7 - m.b12 >= 0)

m.c29 = Constraint(expr=   m.b5 + m.b10 - m.b13 >= 0)

m.c30 = Constraint(expr=   m.b5 + m.b10 - m.b14 >= 0)

m.c31 = Constraint(expr=   m.b2 + m.b8 - m.b15 >= 0)

m.c32 = Constraint(expr=   m.b2 + m.b8 - m.b16 >= 0)

m.c33 = Constraint(expr=   m.b2 + m.b6 + m.b12 - m.b17 >= 0)

m.c34 = Constraint(expr=   m.b9 + m.b11 + m.b14 - m.b18 >= 0)

m.c35 = Constraint(expr=   m.b6 + m.b13 + m.b16 - m.b19 >= 0)

m.c36 = Constraint(expr=   m.b3 + m.b9 + m.b15 - m.b20 >= 0)

m.c37 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8 + m.b9 + m.b10 + m.b11 + m.b12 + m.b13
                         + m.b14 + m.b15 + m.b16 + m.b17 + m.b18 + m.b19 + m.b20 == 4)

m.c39 = Constraint(expr=   m.x21 - m.x41 - m.x61 - m.x81 - m.x101 - m.x121 == 0)

m.c40 = Constraint(expr=   m.x22 - m.x42 - m.x62 - m.x82 - m.x102 - m.x122 == 0)

m.c41 = Constraint(expr=   m.x23 - m.x43 - m.x63 - m.x83 - m.x103 - m.x123 == 0)

m.c42 = Constraint(expr=   m.x24 - m.x44 - m.x64 - m.x84 - m.x104 - m.x124 == 0)

m.c43 = Constraint(expr=   m.x25 - m.x45 - m.x65 - m.x85 - m.x105 - m.x125 == 0)

m.c44 = Constraint(expr=   m.x26 - m.x46 - m.x66 - m.x86 - m.x106 - m.x126 == 0)

m.c45 = Constraint(expr=   m.x27 - m.x47 - m.x67 - m.x87 - m.x107 - m.x127 == 0)

m.c46 = Constraint(expr=   m.x28 - m.x48 - m.x68 - m.x88 - m.x108 - m.x128 == 0)

m.c47 = Constraint(expr=   m.x29 - m.x49 - m.x69 - m.x89 - m.x109 - m.x129 == 0)

m.c48 = Constraint(expr=   m.x30 - m.x50 - m.x70 - m.x90 - m.x110 - m.x130 == 0)

m.c49 = Constraint(expr=   m.x31 - m.x51 - m.x71 - m.x91 - m.x111 - m.x131 == 0)

m.c50 = Constraint(expr=   m.x32 - m.x52 - m.x72 - m.x92 - m.x112 - m.x132 == 0)

m.c51 = Constraint(expr=   m.x33 - m.x53 - m.x73 - m.x93 - m.x113 - m.x133 == 0)

m.c52 = Constraint(expr=   m.x34 - m.x54 - m.x74 - m.x94 - m.x114 - m.x134 == 0)

m.c53 = Constraint(expr=   m.x35 - m.x55 - m.x75 - m.x95 - m.x115 - m.x135 == 0)

m.c54 = Constraint(expr=   m.x36 - m.x56 - m.x76 - m.x96 - m.x116 - m.x136 == 0)

m.c55 = Constraint(expr=   m.x37 - m.x57 - m.x77 - m.x97 - m.x117 - m.x137 == 0)

m.c56 = Constraint(expr=   m.x38 - m.x58 - m.x78 - m.x98 - m.x118 - m.x138 == 0)

m.c57 = Constraint(expr=   m.x39 - m.x59 - m.x79 - m.x99 - m.x119 - m.x139 == 0)

m.c58 = Constraint(expr=   m.x40 - m.x60 - m.x80 - m.x100 - m.x120 - m.x140 == 0)

m.c59 = Constraint(expr=   m.x141 - m.x161 - m.x181 - m.x201 - m.x221 - m.x241 == 0)

m.c60 = Constraint(expr=   m.x142 - m.x162 - m.x182 - m.x202 - m.x222 - m.x242 == 0)

m.c61 = Constraint(expr=   m.x143 - m.x163 - m.x183 - m.x203 - m.x223 - m.x243 == 0)

m.c62 = Constraint(expr=   m.x144 - m.x164 - m.x184 - m.x204 - m.x224 - m.x244 == 0)

m.c63 = Constraint(expr=   m.x145 - m.x165 - m.x185 - m.x205 - m.x225 - m.x245 == 0)

m.c64 = Constraint(expr=   m.x146 - m.x166 - m.x186 - m.x206 - m.x226 - m.x246 == 0)

m.c65 = Constraint(expr=   m.x147 - m.x167 - m.x187 - m.x207 - m.x227 - m.x247 == 0)

m.c66 = Constraint(expr=   m.x148 - m.x168 - m.x188 - m.x208 - m.x228 - m.x248 == 0)

m.c67 = Constraint(expr=   m.x149 - m.x169 - m.x189 - m.x209 - m.x229 - m.x249 == 0)

m.c68 = Constraint(expr=   m.x150 - m.x170 - m.x190 - m.x210 - m.x230 - m.x250 == 0)

m.c69 = Constraint(expr=   m.x151 - m.x171 - m.x191 - m.x211 - m.x231 - m.x251 == 0)

m.c70 = Constraint(expr=   m.x152 - m.x172 - m.x192 - m.x212 - m.x232 - m.x252 == 0)

m.c71 = Constraint(expr=   m.x153 - m.x173 - m.x193 - m.x213 - m.x233 - m.x253 == 0)

m.c72 = Constraint(expr=   m.x154 - m.x174 - m.x194 - m.x214 - m.x234 - m.x254 == 0)

m.c73 = Constraint(expr=   m.x155 - m.x175 - m.x195 - m.x215 - m.x235 - m.x255 == 0)

m.c74 = Constraint(expr=   m.x156 - m.x176 - m.x196 - m.x216 - m.x236 - m.x256 == 0)

m.c75 = Constraint(expr=   m.x157 - m.x177 - m.x197 - m.x217 - m.x237 - m.x257 == 0)

m.c76 = Constraint(expr=   m.x158 - m.x178 - m.x198 - m.x218 - m.x238 - m.x258 == 0)

m.c77 = Constraint(expr=   m.x159 - m.x179 - m.x199 - m.x219 - m.x239 - m.x259 == 0)

m.c78 = Constraint(expr=   m.x160 - m.x180 - m.x200 - m.x220 - m.x240 - m.x260 == 0)

m.c79 = Constraint(expr=   m.x261 - m.x281 - m.x301 - m.x321 - m.x341 - m.x361 == 0)

m.c80 = Constraint(expr=   m.x262 - m.x282 - m.x302 - m.x322 - m.x342 - m.x362 == 0)

m.c81 = Constraint(expr=   m.x263 - m.x283 - m.x303 - m.x323 - m.x343 - m.x363 == 0)

m.c82 = Constraint(expr=   m.x264 - m.x284 - m.x304 - m.x324 - m.x344 - m.x364 == 0)

m.c83 = Constraint(expr=   m.x265 - m.x285 - m.x305 - m.x325 - m.x345 - m.x365 == 0)

m.c84 = Constraint(expr=   m.x266 - m.x286 - m.x306 - m.x326 - m.x346 - m.x366 == 0)

m.c85 = Constraint(expr=   m.x267 - m.x287 - m.x307 - m.x327 - m.x347 - m.x367 == 0)

m.c86 = Constraint(expr=   m.x268 - m.x288 - m.x308 - m.x328 - m.x348 - m.x368 == 0)

m.c87 = Constraint(expr=   m.x269 - m.x289 - m.x309 - m.x329 - m.x349 - m.x369 == 0)

m.c88 = Constraint(expr=   m.x270 - m.x290 - m.x310 - m.x330 - m.x350 - m.x370 == 0)

m.c89 = Constraint(expr=   m.x271 - m.x291 - m.x311 - m.x331 - m.x351 - m.x371 == 0)

m.c90 = Constraint(expr=   m.x272 - m.x292 - m.x312 - m.x332 - m.x352 - m.x372 == 0)

m.c91 = Constraint(expr=   m.x273 - m.x293 - m.x313 - m.x333 - m.x353 - m.x373 == 0)

m.c92 = Constraint(expr=   m.x274 - m.x294 - m.x314 - m.x334 - m.x354 - m.x374 == 0)

m.c93 = Constraint(expr=   m.x275 - m.x295 - m.x315 - m.x335 - m.x355 - m.x375 == 0)

m.c94 = Constraint(expr=   m.x276 - m.x296 - m.x316 - m.x336 - m.x356 - m.x376 == 0)

m.c95 = Constraint(expr=   m.x277 - m.x297 - m.x317 - m.x337 - m.x357 - m.x377 == 0)

m.c96 = Constraint(expr=   m.x278 - m.x298 - m.x318 - m.x338 - m.x358 - m.x378 == 0)

m.c97 = Constraint(expr=   m.x279 - m.x299 - m.x319 - m.x339 - m.x359 - m.x379 == 0)

m.c98 = Constraint(expr=   m.x280 - m.x300 - m.x320 - m.x340 - m.x360 - m.x380 == 0)

m.c99 = Constraint(expr=   m.x21 - m.x141 - m.x261 == 0)

m.c100 = Constraint(expr=   m.x22 - m.x142 - m.x262 == 0)

m.c101 = Constraint(expr=   m.x23 - m.x143 - m.x263 == 0)

m.c102 = Constraint(expr=   m.x24 - m.x144 - m.x264 == 0)

m.c103 = Constraint(expr=   m.x25 - m.x145 - m.x265 == 0)

m.c104 = Constraint(expr=   m.x26 - m.x146 - m.x266 == 0)

m.c105 = Constraint(expr=   m.x27 - m.x147 - m.x267 == 0)

m.c106 = Constraint(expr=   m.x28 - m.x148 - m.x268 == 0)

m.c107 = Constraint(expr=   m.x29 - m.x149 - m.x269 == 0)

m.c108 = Constraint(expr=   m.x30 - m.x150 - m.x270 == 0)

m.c109 = Constraint(expr=   m.x31 - m.x151 - m.x271 == 0)

m.c110 = Constraint(expr=   m.x32 - m.x152 - m.x272 == 0)

m.c111 = Constraint(expr=   m.x33 - m.x153 - m.x273 == 0)

m.c112 = Constraint(expr=   m.x34 - m.x154 - m.x274 == 0)

m.c113 = Constraint(expr=   m.x35 - m.x155 - m.x275 == 0)

m.c114 = Constraint(expr=   m.x36 - m.x156 - m.x276 == 0)

m.c115 = Constraint(expr=   m.x37 - m.x157 - m.x277 == 0)

m.c116 = Constraint(expr=   m.x38 - m.x158 - m.x278 == 0)

m.c117 = Constraint(expr=   m.x39 - m.x159 - m.x279 == 0)

m.c118 = Constraint(expr=   m.x40 - m.x160 - m.x280 == 0)

m.c119 = Constraint(expr=   m.x41 - m.x161 - m.x281 == 0)

m.c120 = Constraint(expr=   m.x42 - m.x162 - m.x282 == 0)

m.c121 = Constraint(expr=   m.x43 - m.x163 - m.x283 == 0)

m.c122 = Constraint(expr=   m.x44 - m.x164 - m.x284 == 0)

m.c123 = Constraint(expr=   m.x45 - m.x165 - m.x285 == 0)

m.c124 = Constraint(expr=   m.x46 - m.x166 - m.x286 == 0)

m.c125 = Constraint(expr=   m.x47 - m.x167 - m.x287 == 0)

m.c126 = Constraint(expr=   m.x48 - m.x168 - m.x288 == 0)

m.c127 = Constraint(expr=   m.x49 - m.x169 - m.x289 == 0)

m.c128 = Constraint(expr=   m.x50 - m.x170 - m.x290 == 0)

m.c129 = Constraint(expr=   m.x51 - m.x171 - m.x291 == 0)

m.c130 = Constraint(expr=   m.x52 - m.x172 - m.x292 == 0)

m.c131 = Constraint(expr=   m.x53 - m.x173 - m.x293 == 0)

m.c132 = Constraint(expr=   m.x54 - m.x174 - m.x294 == 0)

m.c133 = Constraint(expr=   m.x55 - m.x175 - m.x295 == 0)

m.c134 = Constraint(expr=   m.x56 - m.x176 - m.x296 == 0)

m.c135 = Constraint(expr=   m.x57 - m.x177 - m.x297 == 0)

m.c136 = Constraint(expr=   m.x58 - m.x178 - m.x298 == 0)

m.c137 = Constraint(expr=   m.x59 - m.x179 - m.x299 == 0)

m.c138 = Constraint(expr=   m.x60 - m.x180 - m.x300 == 0)

m.c139 = Constraint(expr=   m.x61 - m.x181 - m.x301 == 0)

m.c140 = Constraint(expr=   m.x62 - m.x182 - m.x302 == 0)

m.c141 = Constraint(expr=   m.x63 - m.x183 - m.x303 == 0)

m.c142 = Constraint(expr=   m.x64 - m.x184 - m.x304 == 0)

m.c143 = Constraint(expr=   m.x65 - m.x185 - m.x305 == 0)

m.c144 = Constraint(expr=   m.x66 - m.x186 - m.x306 == 0)

m.c145 = Constraint(expr=   m.x67 - m.x187 - m.x307 == 0)

m.c146 = Constraint(expr=   m.x68 - m.x188 - m.x308 == 0)

m.c147 = Constraint(expr=   m.x69 - m.x189 - m.x309 == 0)

m.c148 = Constraint(expr=   m.x70 - m.x190 - m.x310 == 0)

m.c149 = Constraint(expr=   m.x71 - m.x191 - m.x311 == 0)

m.c150 = Constraint(expr=   m.x72 - m.x192 - m.x312 == 0)

m.c151 = Constraint(expr=   m.x73 - m.x193 - m.x313 == 0)

m.c152 = Constraint(expr=   m.x74 - m.x194 - m.x314 == 0)

m.c153 = Constraint(expr=   m.x75 - m.x195 - m.x315 == 0)

m.c154 = Constraint(expr=   m.x76 - m.x196 - m.x316 == 0)

m.c155 = Constraint(expr=   m.x77 - m.x197 - m.x317 == 0)

m.c156 = Constraint(expr=   m.x78 - m.x198 - m.x318 == 0)

m.c157 = Constraint(expr=   m.x79 - m.x199 - m.x319 == 0)

m.c158 = Constraint(expr=   m.x80 - m.x200 - m.x320 == 0)

m.c159 = Constraint(expr=   m.x81 - m.x201 - m.x321 == 0)

m.c160 = Constraint(expr=   m.x82 - m.x202 - m.x322 == 0)

m.c161 = Constraint(expr=   m.x83 - m.x203 - m.x323 == 0)

m.c162 = Constraint(expr=   m.x84 - m.x204 - m.x324 == 0)

m.c163 = Constraint(expr=   m.x85 - m.x205 - m.x325 == 0)

m.c164 = Constraint(expr=   m.x86 - m.x206 - m.x326 == 0)

m.c165 = Constraint(expr=   m.x87 - m.x207 - m.x327 == 0)

m.c166 = Constraint(expr=   m.x88 - m.x208 - m.x328 == 0)

m.c167 = Constraint(expr=   m.x89 - m.x209 - m.x329 == 0)

m.c168 = Constraint(expr=   m.x90 - m.x210 - m.x330 == 0)

m.c169 = Constraint(expr=   m.x91 - m.x211 - m.x331 == 0)

m.c170 = Constraint(expr=   m.x92 - m.x212 - m.x332 == 0)

m.c171 = Constraint(expr=   m.x93 - m.x213 - m.x333 == 0)

m.c172 = Constraint(expr=   m.x94 - m.x214 - m.x334 == 0)

m.c173 = Constraint(expr=   m.x95 - m.x215 - m.x335 == 0)

m.c174 = Constraint(expr=   m.x96 - m.x216 - m.x336 == 0)

m.c175 = Constraint(expr=   m.x97 - m.x217 - m.x337 == 0)

m.c176 = Constraint(expr=   m.x98 - m.x218 - m.x338 == 0)

m.c177 = Constraint(expr=   m.x99 - m.x219 - m.x339 == 0)

m.c178 = Constraint(expr=   m.x100 - m.x220 - m.x340 == 0)

m.c179 = Constraint(expr=   m.x101 - m.x221 - m.x341 == 0)

m.c180 = Constraint(expr=   m.x102 - m.x222 - m.x342 == 0)

m.c181 = Constraint(expr=   m.x103 - m.x223 - m.x343 == 0)

m.c182 = Constraint(expr=   m.x104 - m.x224 - m.x344 == 0)

m.c183 = Constraint(expr=   m.x105 - m.x225 - m.x345 == 0)

m.c184 = Constraint(expr=   m.x106 - m.x226 - m.x346 == 0)

m.c185 = Constraint(expr=   m.x107 - m.x227 - m.x347 == 0)

m.c186 = Constraint(expr=   m.x108 - m.x228 - m.x348 == 0)

m.c187 = Constraint(expr=   m.x109 - m.x229 - m.x349 == 0)

m.c188 = Constraint(expr=   m.x110 - m.x230 - m.x350 == 0)

m.c189 = Constraint(expr=   m.x111 - m.x231 - m.x351 == 0)

m.c190 = Constraint(expr=   m.x112 - m.x232 - m.x352 == 0)

m.c191 = Constraint(expr=   m.x113 - m.x233 - m.x353 == 0)

m.c192 = Constraint(expr=   m.x114 - m.x234 - m.x354 == 0)

m.c193 = Constraint(expr=   m.x115 - m.x235 - m.x355 == 0)

m.c194 = Constraint(expr=   m.x116 - m.x236 - m.x356 == 0)

m.c195 = Constraint(expr=   m.x117 - m.x237 - m.x357 == 0)

m.c196 = Constraint(expr=   m.x118 - m.x238 - m.x358 == 0)

m.c197 = Constraint(expr=   m.x119 - m.x239 - m.x359 == 0)

m.c198 = Constraint(expr=   m.x120 - m.x240 - m.x360 == 0)

m.c199 = Constraint(expr=   m.x121 - m.x241 - m.x361 == 0)

m.c200 = Constraint(expr=   m.x122 - m.x242 - m.x362 == 0)

m.c201 = Constraint(expr=   m.x123 - m.x243 - m.x363 == 0)

m.c202 = Constraint(expr=   m.x124 - m.x244 - m.x364 == 0)

m.c203 = Constraint(expr=   m.x125 - m.x245 - m.x365 == 0)

m.c204 = Constraint(expr=   m.x126 - m.x246 - m.x366 == 0)

m.c205 = Constraint(expr=   m.x127 - m.x247 - m.x367 == 0)

m.c206 = Constraint(expr=   m.x128 - m.x248 - m.x368 == 0)

m.c207 = Constraint(expr=   m.x129 - m.x249 - m.x369 == 0)

m.c208 = Constraint(expr=   m.x130 - m.x250 - m.x370 == 0)

m.c209 = Constraint(expr=   m.x131 - m.x251 - m.x371 == 0)

m.c210 = Constraint(expr=   m.x132 - m.x252 - m.x372 == 0)

m.c211 = Constraint(expr=   m.x133 - m.x253 - m.x373 == 0)

m.c212 = Constraint(expr=   m.x134 - m.x254 - m.x374 == 0)

m.c213 = Constraint(expr=   m.x135 - m.x255 - m.x375 == 0)

m.c214 = Constraint(expr=   m.x136 - m.x256 - m.x376 == 0)

m.c215 = Constraint(expr=   m.x137 - m.x257 - m.x377 == 0)

m.c216 = Constraint(expr=   m.x138 - m.x258 - m.x378 == 0)

m.c217 = Constraint(expr=   m.x139 - m.x259 - m.x379 == 0)

m.c218 = Constraint(expr=   m.x140 - m.x260 - m.x380 == 0)

m.c219 = Constraint(expr=   m.x21 + m.x421 - m.x441 == 0)

m.c220 = Constraint(expr=   m.x22 + m.x422 - m.x442 == 0)

m.c221 = Constraint(expr=   m.x23 + m.x423 - m.x443 == 0)

m.c222 = Constraint(expr=   m.x24 + m.x424 - m.x444 == 0)

m.c223 = Constraint(expr=   m.x25 + m.x425 - m.x445 == 0)

m.c224 = Constraint(expr=   m.x26 + m.x426 - m.x446 == 0)

m.c225 = Constraint(expr=   m.x27 + m.x427 - m.x447 == 0)

m.c226 = Constraint(expr=   m.x28 + m.x428 - m.x448 == 0)

m.c227 = Constraint(expr=   m.x29 + m.x429 - m.x449 == 0)

m.c228 = Constraint(expr=   m.x30 + m.x430 - m.x450 == 0)

m.c229 = Constraint(expr=   m.x31 + m.x431 - m.x451 == 0)

m.c230 = Constraint(expr=   m.x32 + m.x432 - m.x452 == 0)

m.c231 = Constraint(expr=   m.x33 + m.x433 - m.x453 == 0)

m.c232 = Constraint(expr=   m.x34 + m.x434 - m.x454 == 0)

m.c233 = Constraint(expr=   m.x35 + m.x435 - m.x455 == 0)

m.c234 = Constraint(expr=   m.x36 + m.x436 - m.x456 == 0)

m.c235 = Constraint(expr=   m.x37 + m.x437 - m.x457 == 0)

m.c236 = Constraint(expr=   m.x38 + m.x438 - m.x458 == 0)

m.c237 = Constraint(expr=   m.x39 + m.x439 - m.x459 == 0)

m.c238 = Constraint(expr=   m.x40 + m.x440 - m.x460 == 0)

m.c239 = Constraint(expr= - m.x381 + m.x401 == 0)

m.c240 = Constraint(expr= - m.x382 + m.x402 == 0)

m.c241 = Constraint(expr= - m.x383 + m.x403 == 0)

m.c242 = Constraint(expr= - m.x384 + m.x404 == 0)

m.c243 = Constraint(expr= - m.x385 + m.x405 == 0)

m.c244 = Constraint(expr= - m.x386 + m.x406 == 0)

m.c245 = Constraint(expr= - m.x387 + m.x407 == 0)

m.c246 = Constraint(expr= - m.x388 + m.x408 == 0)

m.c247 = Constraint(expr= - m.x389 + m.x409 == 0)

m.c248 = Constraint(expr= - m.x390 + m.x410 == 0)

m.c249 = Constraint(expr= - m.x391 + m.x411 == 0)

m.c250 = Constraint(expr= - m.x392 + m.x412 == 0)

m.c251 = Constraint(expr= - m.x393 + m.x413 == 0)

m.c252 = Constraint(expr= - m.x394 + m.x414 == 0)

m.c253 = Constraint(expr= - m.x395 + m.x415 == 0)

m.c254 = Constraint(expr= - m.x396 + m.x416 == 0)

m.c255 = Constraint(expr= - m.x397 + m.x417 == 0)

m.c256 = Constraint(expr= - m.x398 + m.x418 == 0)

m.c257 = Constraint(expr= - m.x399 + m.x419 == 0)

m.c258 = Constraint(expr= - m.x400 + m.x420 == 0)

m.c259 = Constraint(expr= - m.x141 + m.x381 - m.x421 == 0)

m.c260 = Constraint(expr= - m.x142 + m.x382 - m.x422 == 0)

m.c261 = Constraint(expr= - m.x143 + m.x383 - m.x423 == 0)

m.c262 = Constraint(expr= - m.x144 + m.x384 - m.x424 == 0)

m.c263 = Constraint(expr= - m.x145 + m.x385 - m.x425 == 0)

m.c264 = Constraint(expr= - m.x146 + m.x386 - m.x426 == 0)

m.c265 = Constraint(expr= - m.x147 + m.x387 - m.x427 == 0)

m.c266 = Constraint(expr= - m.x148 + m.x388 - m.x428 == 0)

m.c267 = Constraint(expr= - m.x149 + m.x389 - m.x429 == 0)

m.c268 = Constraint(expr= - m.x150 + m.x390 - m.x430 == 0)

m.c269 = Constraint(expr= - m.x151 + m.x391 - m.x431 == 0)

m.c270 = Constraint(expr= - m.x152 + m.x392 - m.x432 == 0)

m.c271 = Constraint(expr= - m.x153 + m.x393 - m.x433 == 0)

m.c272 = Constraint(expr= - m.x154 + m.x394 - m.x434 == 0)

m.c273 = Constraint(expr= - m.x155 + m.x395 - m.x435 == 0)

m.c274 = Constraint(expr= - m.x156 + m.x396 - m.x436 == 0)

m.c275 = Constraint(expr= - m.x157 + m.x397 - m.x437 == 0)

m.c276 = Constraint(expr= - m.x158 + m.x398 - m.x438 == 0)

m.c277 = Constraint(expr= - m.x159 + m.x399 - m.x439 == 0)

m.c278 = Constraint(expr= - m.x160 + m.x400 - m.x440 == 0)

m.c279 = Constraint(expr= - m.x261 - m.x401 + m.x441 == 0)

m.c280 = Constraint(expr= - m.x262 - m.x402 + m.x442 == 0)

m.c281 = Constraint(expr= - m.x263 - m.x403 + m.x443 == 0)

m.c282 = Constraint(expr= - m.x264 - m.x404 + m.x444 == 0)

m.c283 = Constraint(expr= - m.x265 - m.x405 + m.x445 == 0)

m.c284 = Constraint(expr= - m.x266 - m.x406 + m.x446 == 0)

m.c285 = Constraint(expr= - m.x267 - m.x407 + m.x447 == 0)

m.c286 = Constraint(expr= - m.x268 - m.x408 + m.x448 == 0)

m.c287 = Constraint(expr= - m.x269 - m.x409 + m.x449 == 0)

m.c288 = Constraint(expr= - m.x270 - m.x410 + m.x450 == 0)

m.c289 = Constraint(expr= - m.x271 - m.x411 + m.x451 == 0)

m.c290 = Constraint(expr= - m.x272 - m.x412 + m.x452 == 0)

m.c291 = Constraint(expr= - m.x273 - m.x413 + m.x453 == 0)

m.c292 = Constraint(expr= - m.x274 - m.x414 + m.x454 == 0)

m.c293 = Constraint(expr= - m.x275 - m.x415 + m.x455 == 0)

m.c294 = Constraint(expr= - m.x276 - m.x416 + m.x456 == 0)

m.c295 = Constraint(expr= - m.x277 - m.x417 + m.x457 == 0)

m.c296 = Constraint(expr= - m.x278 - m.x418 + m.x458 == 0)

m.c297 = Constraint(expr= - m.x279 - m.x419 + m.x459 == 0)

m.c298 = Constraint(expr= - m.x280 - m.x420 + m.x460 == 0)

m.c299 = Constraint(expr= - m.x21 - m.x22 - m.x23 - m.x24 == -2)

m.c300 = Constraint(expr= - m.x41 - m.x42 - m.x43 - m.x44 == -0.6)

m.c301 = Constraint(expr= - m.x61 - m.x62 - m.x63 - m.x64 == -0.4)

m.c302 = Constraint(expr= - m.x81 - m.x82 - m.x83 - m.x84 == -0.2)

m.c303 = Constraint(expr= - m.x101 - m.x102 - m.x103 - m.x104 == -0.4)

m.c304 = Constraint(expr= - m.x121 - m.x122 - m.x123 - m.x124 == -0.4)

m.c305 = Constraint(expr= - m.x25 - m.x26 - m.x27 + m.x144 == 0)

m.c306 = Constraint(expr= - m.x28 - m.x29 - m.x30 + m.x261 == 0)

m.c307 = Constraint(expr= - m.x22 - m.x31 + m.x143 + m.x147 == 0)

m.c308 = Constraint(expr= - m.x33 - m.x34 + m.x150 + m.x265 == 0)

m.c309 = Constraint(expr= - m.x35 - m.x36 + m.x262 + m.x268 == 0)

m.c310 = Constraint(expr= - m.x37 + m.x142 + m.x146 + m.x152 == 0)

m.c311 = Constraint(expr= - m.x38 + m.x149 + m.x154 + m.x271 == 0)

m.c312 = Constraint(expr= - m.x39 + m.x156 + m.x266 + m.x273 == 0)

m.c313 = Constraint(expr= - m.x40 + m.x263 + m.x269 + m.x275 == 0)

m.c314 = Constraint(expr= - m.x45 - m.x46 - m.x47 + m.x164 == 0)

m.c315 = Constraint(expr= - m.x65 - m.x66 - m.x67 + m.x184 == 0)

m.c316 = Constraint(expr= - m.x85 - m.x86 - m.x87 + m.x204 == 0)

m.c317 = Constraint(expr= - m.x105 - m.x106 - m.x107 + m.x224 == 0)

m.c318 = Constraint(expr= - m.x125 - m.x126 - m.x127 + m.x244 == 0)

m.c319 = Constraint(expr= - m.x48 - m.x49 - m.x50 + m.x281 == 0)

m.c320 = Constraint(expr= - m.x68 - m.x69 - m.x70 + m.x301 == 0)

m.c321 = Constraint(expr= - m.x88 - m.x89 - m.x90 + m.x321 == 0)

m.c322 = Constraint(expr= - m.x108 - m.x109 - m.x110 + m.x341 == 0)

m.c323 = Constraint(expr= - m.x128 - m.x129 - m.x130 + m.x361 == 0)

m.c324 = Constraint(expr= - m.x42 - m.x51 + m.x163 + m.x167 == 0)

m.c325 = Constraint(expr= - m.x62 - m.x71 + m.x183 + m.x187 == 0)

m.c326 = Constraint(expr= - m.x82 - m.x91 + m.x203 + m.x207 == 0)

m.c327 = Constraint(expr= - m.x102 - m.x111 + m.x223 + m.x227 == 0)

m.c328 = Constraint(expr= - m.x122 - m.x131 + m.x243 + m.x247 == 0)

m.c329 = Constraint(expr= - m.x53 - m.x54 + m.x170 + m.x285 == 0)

m.c330 = Constraint(expr= - m.x73 - m.x74 + m.x190 + m.x305 == 0)

m.c331 = Constraint(expr= - m.x93 - m.x94 + m.x210 + m.x325 == 0)

m.c332 = Constraint(expr= - m.x113 - m.x114 + m.x230 + m.x345 == 0)

m.c333 = Constraint(expr= - m.x133 - m.x134 + m.x250 + m.x365 == 0)

m.c334 = Constraint(expr= - m.x55 - m.x56 + m.x282 + m.x288 == 0)

m.c335 = Constraint(expr= - m.x75 - m.x76 + m.x302 + m.x308 == 0)

m.c336 = Constraint(expr= - m.x95 - m.x96 + m.x322 + m.x328 == 0)

m.c337 = Constraint(expr= - m.x115 - m.x116 + m.x342 + m.x348 == 0)

m.c338 = Constraint(expr= - m.x135 - m.x136 + m.x362 + m.x368 == 0)

m.c339 = Constraint(expr= - m.x57 + m.x162 + m.x166 + m.x172 == 0)

m.c340 = Constraint(expr= - m.x77 + m.x182 + m.x186 + m.x192 == 0)

m.c341 = Constraint(expr= - m.x97 + m.x202 + m.x206 + m.x212 == 0)

m.c342 = Constraint(expr= - m.x117 + m.x222 + m.x226 + m.x232 == 0)

m.c343 = Constraint(expr= - m.x137 + m.x242 + m.x246 + m.x252 == 0)

m.c344 = Constraint(expr= - m.x58 + m.x169 + m.x174 + m.x291 == 0)

m.c345 = Constraint(expr= - m.x78 + m.x189 + m.x194 + m.x311 == 0)

m.c346 = Constraint(expr= - m.x98 + m.x209 + m.x214 + m.x331 == 0)

m.c347 = Constraint(expr= - m.x118 + m.x229 + m.x234 + m.x351 == 0)

m.c348 = Constraint(expr= - m.x138 + m.x249 + m.x254 + m.x371 == 0)

m.c349 = Constraint(expr= - m.x59 + m.x176 + m.x286 + m.x293 == 0)

m.c350 = Constraint(expr= - m.x79 + m.x196 + m.x306 + m.x313 == 0)

m.c351 = Constraint(expr= - m.x99 + m.x216 + m.x326 + m.x333 == 0)

m.c352 = Constraint(expr= - m.x119 + m.x236 + m.x346 + m.x353 == 0)

m.c353 = Constraint(expr= - m.x139 + m.x256 + m.x366 + m.x373 == 0)

m.c354 = Constraint(expr= - m.x60 + m.x283 + m.x289 + m.x295 == 0)

m.c355 = Constraint(expr= - m.x80 + m.x303 + m.x309 + m.x315 == 0)

m.c356 = Constraint(expr= - m.x100 + m.x323 + m.x329 + m.x335 == 0)

m.c357 = Constraint(expr= - m.x120 + m.x343 + m.x349 + m.x355 == 0)

m.c358 = Constraint(expr= - m.x140 + m.x363 + m.x369 + m.x375 == 0)

m.c359 = Constraint(expr=   m.x141 + m.x145 + m.x151 + m.x157 == 0.6)

m.c360 = Constraint(expr=   m.x148 + m.x153 + m.x158 + m.x277 == 0.4)

m.c361 = Constraint(expr=   m.x155 + m.x159 + m.x272 + m.x278 == 0.2)

m.c362 = Constraint(expr=   m.x160 + m.x267 + m.x274 + m.x279 == 0.4)

m.c363 = Constraint(expr=   m.x264 + m.x270 + m.x276 + m.x280 == 0.4)

m.c364 = Constraint(expr=   m.x161 + m.x165 + m.x171 + m.x177 == 0.6)

m.c365 = Constraint(expr=   m.x188 + m.x193 + m.x198 + m.x317 == 0.4)

m.c366 = Constraint(expr=   m.x215 + m.x219 + m.x332 + m.x338 == 0.2)

m.c367 = Constraint(expr=   m.x240 + m.x347 + m.x354 + m.x359 == 0.4)

m.c368 = Constraint(expr=   m.x364 + m.x370 + m.x376 + m.x380 == 0.4)

m.c369 = Constraint(expr=1.2*(10.5*m.x41/(10.5 - m.x461) + 4.04*m.x61/(4.04 - m.x461) + 1.76*m.x81/(1.76 - m.x461) + 
                         1.31*m.x101/(1.31 - m.x461) + m.x121/(1 - m.x461)) + 10*m.b1 - m.x381 + m.x401 <= 10)

m.c370 = Constraint(expr=1.2*(10.5*m.x42/(10.5 - m.x462) + 4.04*m.x62/(4.04 - m.x462) + 1.76*m.x82/(1.76 - m.x462) + 
                         1.31*m.x102/(1.31 - m.x462) + m.x122/(1 - m.x462)) + 10*m.b2 - m.x382 + m.x402 <= 10)

m.c371 = Constraint(expr=1.2*(10.5*m.x43/(10.5 - m.x463) + 4.04*m.x63/(4.04 - m.x463) + 1.76*m.x83/(1.76 - m.x463) + 
                         1.31*m.x103/(1.31 - m.x463) + m.x123/(1 - m.x463)) + 10*m.b3 - m.x383 + m.x403 <= 10)

m.c372 = Constraint(expr=1.2*(10.5*m.x44/(10.5 - m.x464) + 4.04*m.x64/(4.04 - m.x464) + 1.76*m.x84/(1.76 - m.x464) + 
                         1.31*m.x104/(1.31 - m.x464) + m.x124/(1 - m.x464)) + 10*m.b4 - m.x384 + m.x404 <= 10)

m.c373 = Constraint(expr=1.2*(10.5*m.x45/(10.5 - m.x465) + 4.04*m.x65/(4.04 - m.x465) + 1.76*m.x85/(1.76 - m.x465) + 
                         1.31*m.x105/(1.31 - m.x465) + m.x125/(1 - m.x465)) + 10*m.b5 - m.x385 + m.x405 <= 10)

m.c374 = Constraint(expr=1.2*(10.5*m.x46/(10.5 - m.x466) + 4.04*m.x66/(4.04 - m.x466) + 1.76*m.x86/(1.76 - m.x466) + 
                         1.31*m.x106/(1.31 - m.x466) + m.x126/(1 - m.x466)) + 10*m.b6 - m.x386 + m.x406 <= 10)

m.c375 = Constraint(expr=1.2*(10.5*m.x47/(10.5 - m.x467) + 4.04*m.x67/(4.04 - m.x467) + 1.76*m.x87/(1.76 - m.x467) + 
                         1.31*m.x107/(1.31 - m.x467) + m.x127/(1 - m.x467)) + 10*m.b7 - m.x387 + m.x407 <= 10)

m.c376 = Constraint(expr=1.2*(10.5*m.x48/(10.5 - m.x468) + 4.04*m.x68/(4.04 - m.x468) + 1.76*m.x88/(1.76 - m.x468) + 
                         1.31*m.x108/(1.31 - m.x468) + m.x128/(1 - m.x468)) + 10*m.b8 - m.x388 + m.x408 <= 10)

m.c377 = Constraint(expr=1.2*(10.5*m.x49/(10.5 - m.x469) + 4.04*m.x69/(4.04 - m.x469) + 1.76*m.x89/(1.76 - m.x469) + 
                         1.31*m.x109/(1.31 - m.x469) + m.x129/(1 - m.x469)) + 10*m.b9 - m.x389 + m.x409 <= 10)

m.c378 = Constraint(expr=1.2*(10.5*m.x50/(10.5 - m.x470) + 4.04*m.x70/(4.04 - m.x470) + 1.76*m.x90/(1.76 - m.x470) + 
                         1.31*m.x110/(1.31 - m.x470) + m.x130/(1 - m.x470)) + 10*m.b10 - m.x390 + m.x410 <= 10)

m.c379 = Constraint(expr=1.2*(10.5*m.x51/(10.5 - m.x471) + 4.04*m.x71/(4.04 - m.x471) + 1.76*m.x91/(1.76 - m.x471) + 
                         1.31*m.x111/(1.31 - m.x471) + m.x131/(1 - m.x471)) + 10*m.b11 - m.x391 + m.x411 <= 10)

m.c380 = Constraint(expr=1.2*(10.5*m.x52/(10.5 - m.x472) + 4.04*m.x72/(4.04 - m.x472) + 1.76*m.x92/(1.76 - m.x472) + 
                         1.31*m.x112/(1.31 - m.x472) + m.x132/(1 - m.x472)) + 10*m.b12 - m.x392 + m.x412 <= 10)

m.c381 = Constraint(expr=1.2*(10.5*m.x53/(10.5 - m.x473) + 4.04*m.x73/(4.04 - m.x473) + 1.76*m.x93/(1.76 - m.x473) + 
                         1.31*m.x113/(1.31 - m.x473) + m.x133/(1 - m.x473)) + 10*m.b13 - m.x393 + m.x413 <= 10)

m.c382 = Constraint(expr=1.2*(10.5*m.x54/(10.5 - m.x474) + 4.04*m.x74/(4.04 - m.x474) + 1.76*m.x94/(1.76 - m.x474) + 
                         1.31*m.x114/(1.31 - m.x474) + m.x134/(1 - m.x474)) + 10*m.b14 - m.x394 + m.x414 <= 10)

m.c383 = Constraint(expr=1.2*(10.5*m.x55/(10.5 - m.x475) + 4.04*m.x75/(4.04 - m.x475) + 1.76*m.x95/(1.76 - m.x475) + 
                         1.31*m.x115/(1.31 - m.x475) + m.x135/(1 - m.x475)) + 10*m.b15 - m.x395 + m.x415 <= 10)

m.c384 = Constraint(expr=1.2*(10.5*m.x56/(10.5 - m.x476) + 4.04*m.x76/(4.04 - m.x476) + 1.76*m.x96/(1.76 - m.x476) + 
                         1.31*m.x116/(1.31 - m.x476) + m.x136/(1 - m.x476)) + 10*m.b16 - m.x396 + m.x416 <= 10)

m.c385 = Constraint(expr=1.2*(10.5*m.x57/(10.5 - m.x477) + 4.04*m.x77/(4.04 - m.x477) + 1.76*m.x97/(1.76 - m.x477) + 
                         1.31*m.x117/(1.31 - m.x477) + m.x137/(1 - m.x477)) + 10*m.b17 - m.x397 + m.x417 <= 10)

m.c386 = Constraint(expr=1.2*(10.5*m.x58/(10.5 - m.x478) + 4.04*m.x78/(4.04 - m.x478) + 1.76*m.x98/(1.76 - m.x478) + 
                         1.31*m.x118/(1.31 - m.x478) + m.x138/(1 - m.x478)) + 10*m.b18 - m.x398 + m.x418 <= 10)

m.c387 = Constraint(expr=1.2*(10.5*m.x59/(10.5 - m.x479) + 4.04*m.x79/(4.04 - m.x479) + 1.76*m.x99/(1.76 - m.x479) + 
                         1.31*m.x119/(1.31 - m.x479) + m.x139/(1 - m.x479)) + 10*m.b19 - m.x399 + m.x419 <= 10)

m.c388 = Constraint(expr=1.2*(10.5*m.x60/(10.5 - m.x480) + 4.04*m.x80/(4.04 - m.x480) + 1.76*m.x100/(1.76 - m.x480) + 
                         1.31*m.x120/(1.31 - m.x480) + m.x140/(1 - m.x480)) + 10*m.b20 - m.x400 + m.x420 <= 10)

m.c389 = Constraint(expr=1.2*(10.5*m.x41/(10.5 - m.x461) + 4.04*m.x61/(4.04 - m.x461) + 1.76*m.x81/(1.76 - m.x461) + 
                         1.31*m.x101/(1.31 - m.x461) + m.x121/(1 - m.x461)) - 10*m.b1 - m.x381 + m.x401 >= -10)

m.c390 = Constraint(expr=1.2*(10.5*m.x42/(10.5 - m.x462) + 4.04*m.x62/(4.04 - m.x462) + 1.76*m.x82/(1.76 - m.x462) + 
                         1.31*m.x102/(1.31 - m.x462) + m.x122/(1 - m.x462)) - 10*m.b2 - m.x382 + m.x402 >= -10)

m.c391 = Constraint(expr=1.2*(10.5*m.x43/(10.5 - m.x463) + 4.04*m.x63/(4.04 - m.x463) + 1.76*m.x83/(1.76 - m.x463) + 
                         1.31*m.x103/(1.31 - m.x463) + m.x123/(1 - m.x463)) - 10*m.b3 - m.x383 + m.x403 >= -10)

m.c392 = Constraint(expr=1.2*(10.5*m.x44/(10.5 - m.x464) + 4.04*m.x64/(4.04 - m.x464) + 1.76*m.x84/(1.76 - m.x464) + 
                         1.31*m.x104/(1.31 - m.x464) + m.x124/(1 - m.x464)) - 10*m.b4 - m.x384 + m.x404 >= -10)

m.c393 = Constraint(expr=1.2*(10.5*m.x45/(10.5 - m.x465) + 4.04*m.x65/(4.04 - m.x465) + 1.76*m.x85/(1.76 - m.x465) + 
                         1.31*m.x105/(1.31 - m.x465) + m.x125/(1 - m.x465)) - 10*m.b5 - m.x385 + m.x405 >= -10)

m.c394 = Constraint(expr=1.2*(10.5*m.x46/(10.5 - m.x466) + 4.04*m.x66/(4.04 - m.x466) + 1.76*m.x86/(1.76 - m.x466) + 
                         1.31*m.x106/(1.31 - m.x466) + m.x126/(1 - m.x466)) - 10*m.b6 - m.x386 + m.x406 >= -10)

m.c395 = Constraint(expr=1.2*(10.5*m.x47/(10.5 - m.x467) + 4.04*m.x67/(4.04 - m.x467) + 1.76*m.x87/(1.76 - m.x467) + 
                         1.31*m.x107/(1.31 - m.x467) + m.x127/(1 - m.x467)) - 10*m.b7 - m.x387 + m.x407 >= -10)

m.c396 = Constraint(expr=1.2*(10.5*m.x48/(10.5 - m.x468) + 4.04*m.x68/(4.04 - m.x468) + 1.76*m.x88/(1.76 - m.x468) + 
                         1.31*m.x108/(1.31 - m.x468) + m.x128/(1 - m.x468)) - 10*m.b8 - m.x388 + m.x408 >= -10)

m.c397 = Constraint(expr=1.2*(10.5*m.x49/(10.5 - m.x469) + 4.04*m.x69/(4.04 - m.x469) + 1.76*m.x89/(1.76 - m.x469) + 
                         1.31*m.x109/(1.31 - m.x469) + m.x129/(1 - m.x469)) - 10*m.b9 - m.x389 + m.x409 >= -10)

m.c398 = Constraint(expr=1.2*(10.5*m.x50/(10.5 - m.x470) + 4.04*m.x70/(4.04 - m.x470) + 1.76*m.x90/(1.76 - m.x470) + 
                         1.31*m.x110/(1.31 - m.x470) + m.x130/(1 - m.x470)) - 10*m.b10 - m.x390 + m.x410 >= -10)

m.c399 = Constraint(expr=1.2*(10.5*m.x51/(10.5 - m.x471) + 4.04*m.x71/(4.04 - m.x471) + 1.76*m.x91/(1.76 - m.x471) + 
                         1.31*m.x111/(1.31 - m.x471) + m.x131/(1 - m.x471)) - 10*m.b11 - m.x391 + m.x411 >= -10)

m.c400 = Constraint(expr=1.2*(10.5*m.x52/(10.5 - m.x472) + 4.04*m.x72/(4.04 - m.x472) + 1.76*m.x92/(1.76 - m.x472) + 
                         1.31*m.x112/(1.31 - m.x472) + m.x132/(1 - m.x472)) - 10*m.b12 - m.x392 + m.x412 >= -10)

m.c401 = Constraint(expr=1.2*(10.5*m.x53/(10.5 - m.x473) + 4.04*m.x73/(4.04 - m.x473) + 1.76*m.x93/(1.76 - m.x473) + 
                         1.31*m.x113/(1.31 - m.x473) + m.x133/(1 - m.x473)) - 10*m.b13 - m.x393 + m.x413 >= -10)

m.c402 = Constraint(expr=1.2*(10.5*m.x54/(10.5 - m.x474) + 4.04*m.x74/(4.04 - m.x474) + 1.76*m.x94/(1.76 - m.x474) + 
                         1.31*m.x114/(1.31 - m.x474) + m.x134/(1 - m.x474)) - 10*m.b14 - m.x394 + m.x414 >= -10)

m.c403 = Constraint(expr=1.2*(10.5*m.x55/(10.5 - m.x475) + 4.04*m.x75/(4.04 - m.x475) + 1.76*m.x95/(1.76 - m.x475) + 
                         1.31*m.x115/(1.31 - m.x475) + m.x135/(1 - m.x475)) - 10*m.b15 - m.x395 + m.x415 >= -10)

m.c404 = Constraint(expr=1.2*(10.5*m.x56/(10.5 - m.x476) + 4.04*m.x76/(4.04 - m.x476) + 1.76*m.x96/(1.76 - m.x476) + 
                         1.31*m.x116/(1.31 - m.x476) + m.x136/(1 - m.x476)) - 10*m.b16 - m.x396 + m.x416 >= -10)

m.c405 = Constraint(expr=1.2*(10.5*m.x57/(10.5 - m.x477) + 4.04*m.x77/(4.04 - m.x477) + 1.76*m.x97/(1.76 - m.x477) + 
                         1.31*m.x117/(1.31 - m.x477) + m.x137/(1 - m.x477)) - 10*m.b17 - m.x397 + m.x417 >= -10)

m.c406 = Constraint(expr=1.2*(10.5*m.x58/(10.5 - m.x478) + 4.04*m.x78/(4.04 - m.x478) + 1.76*m.x98/(1.76 - m.x478) + 
                         1.31*m.x118/(1.31 - m.x478) + m.x138/(1 - m.x478)) - 10*m.b18 - m.x398 + m.x418 >= -10)

m.c407 = Constraint(expr=1.2*(10.5*m.x59/(10.5 - m.x479) + 4.04*m.x79/(4.04 - m.x479) + 1.76*m.x99/(1.76 - m.x479) + 
                         1.31*m.x119/(1.31 - m.x479) + m.x139/(1 - m.x479)) - 10*m.b19 - m.x399 + m.x419 >= -10)

m.c408 = Constraint(expr=1.2*(10.5*m.x60/(10.5 - m.x480) + 4.04*m.x80/(4.04 - m.x480) + 1.76*m.x100/(1.76 - m.x480) + 
                         1.31*m.x120/(1.31 - m.x480) + m.x140/(1 - m.x480)) - 10*m.b20 - m.x400 + m.x420 >= -10)

m.c409 = Constraint(expr=1.2*(10.5*m.x161/(10.5 - m.x461) + 4.04*m.x181/(4.04 - m.x461) + 1.76*m.x201/(1.76 - m.x461) + 
                         1.31*m.x221/(1.31 - m.x461) + m.x241/(1 - m.x461)) + 10*m.b1 - m.x381 <= 10)

m.c410 = Constraint(expr=1.2*(10.5*m.x162/(10.5 - m.x462) + 4.04*m.x182/(4.04 - m.x462) + 1.76*m.x202/(1.76 - m.x462) + 
                         1.31*m.x222/(1.31 - m.x462) + m.x242/(1 - m.x462)) + 10*m.b2 - m.x382 <= 10)

m.c411 = Constraint(expr=1.2*(10.5*m.x163/(10.5 - m.x463) + 4.04*m.x183/(4.04 - m.x463) + 1.76*m.x203/(1.76 - m.x463) + 
                         1.31*m.x223/(1.31 - m.x463) + m.x243/(1 - m.x463)) + 10*m.b3 - m.x383 <= 10)

m.c412 = Constraint(expr=1.2*(10.5*m.x164/(10.5 - m.x464) + 4.04*m.x184/(4.04 - m.x464) + 1.76*m.x204/(1.76 - m.x464) + 
                         1.31*m.x224/(1.31 - m.x464) + m.x244/(1 - m.x464)) + 10*m.b4 - m.x384 <= 10)

m.c413 = Constraint(expr=1.2*(10.5*m.x165/(10.5 - m.x465) + 4.04*m.x185/(4.04 - m.x465) + 1.76*m.x205/(1.76 - m.x465) + 
                         1.31*m.x225/(1.31 - m.x465) + m.x245/(1 - m.x465)) + 10*m.b5 - m.x385 <= 10)

m.c414 = Constraint(expr=1.2*(10.5*m.x166/(10.5 - m.x466) + 4.04*m.x186/(4.04 - m.x466) + 1.76*m.x206/(1.76 - m.x466) + 
                         1.31*m.x226/(1.31 - m.x466) + m.x246/(1 - m.x466)) + 10*m.b6 - m.x386 <= 10)

m.c415 = Constraint(expr=1.2*(10.5*m.x167/(10.5 - m.x467) + 4.04*m.x187/(4.04 - m.x467) + 1.76*m.x207/(1.76 - m.x467) + 
                         1.31*m.x227/(1.31 - m.x467) + m.x247/(1 - m.x467)) + 10*m.b7 - m.x387 <= 10)

m.c416 = Constraint(expr=1.2*(10.5*m.x168/(10.5 - m.x468) + 4.04*m.x188/(4.04 - m.x468) + 1.76*m.x208/(1.76 - m.x468) + 
                         1.31*m.x228/(1.31 - m.x468) + m.x248/(1 - m.x468)) + 10*m.b8 - m.x388 <= 10)

m.c417 = Constraint(expr=1.2*(10.5*m.x169/(10.5 - m.x469) + 4.04*m.x189/(4.04 - m.x469) + 1.76*m.x209/(1.76 - m.x469) + 
                         1.31*m.x229/(1.31 - m.x469) + m.x249/(1 - m.x469)) + 10*m.b9 - m.x389 <= 10)

m.c418 = Constraint(expr=1.2*(10.5*m.x170/(10.5 - m.x470) + 4.04*m.x190/(4.04 - m.x470) + 1.76*m.x210/(1.76 - m.x470) + 
                         1.31*m.x230/(1.31 - m.x470) + m.x250/(1 - m.x470)) + 10*m.b10 - m.x390 <= 10)

m.c419 = Constraint(expr=1.2*(10.5*m.x171/(10.5 - m.x471) + 4.04*m.x191/(4.04 - m.x471) + 1.76*m.x211/(1.76 - m.x471) + 
                         1.31*m.x231/(1.31 - m.x471) + m.x251/(1 - m.x471)) + 10*m.b11 - m.x391 <= 10)

m.c420 = Constraint(expr=1.2*(10.5*m.x172/(10.5 - m.x472) + 4.04*m.x192/(4.04 - m.x472) + 1.76*m.x212/(1.76 - m.x472) + 
                         1.31*m.x232/(1.31 - m.x472) + m.x252/(1 - m.x472)) + 10*m.b12 - m.x392 <= 10)

m.c421 = Constraint(expr=1.2*(10.5*m.x173/(10.5 - m.x473) + 4.04*m.x193/(4.04 - m.x473) + 1.76*m.x213/(1.76 - m.x473) + 
                         1.31*m.x233/(1.31 - m.x473) + m.x253/(1 - m.x473)) + 10*m.b13 - m.x393 <= 10)

m.c422 = Constraint(expr=1.2*(10.5*m.x174/(10.5 - m.x474) + 4.04*m.x194/(4.04 - m.x474) + 1.76*m.x214/(1.76 - m.x474) + 
                         1.31*m.x234/(1.31 - m.x474) + m.x254/(1 - m.x474)) + 10*m.b14 - m.x394 <= 10)

m.c423 = Constraint(expr=1.2*(10.5*m.x175/(10.5 - m.x475) + 4.04*m.x195/(4.04 - m.x475) + 1.76*m.x215/(1.76 - m.x475) + 
                         1.31*m.x235/(1.31 - m.x475) + m.x255/(1 - m.x475)) + 10*m.b15 - m.x395 <= 10)

m.c424 = Constraint(expr=1.2*(10.5*m.x176/(10.5 - m.x476) + 4.04*m.x196/(4.04 - m.x476) + 1.76*m.x216/(1.76 - m.x476) + 
                         1.31*m.x236/(1.31 - m.x476) + m.x256/(1 - m.x476)) + 10*m.b16 - m.x396 <= 10)

m.c425 = Constraint(expr=1.2*(10.5*m.x177/(10.5 - m.x477) + 4.04*m.x197/(4.04 - m.x477) + 1.76*m.x217/(1.76 - m.x477) + 
                         1.31*m.x237/(1.31 - m.x477) + m.x257/(1 - m.x477)) + 10*m.b17 - m.x397 <= 10)

m.c426 = Constraint(expr=1.2*(10.5*m.x178/(10.5 - m.x478) + 4.04*m.x198/(4.04 - m.x478) + 1.76*m.x218/(1.76 - m.x478) + 
                         1.31*m.x238/(1.31 - m.x478) + m.x258/(1 - m.x478)) + 10*m.b18 - m.x398 <= 10)

m.c427 = Constraint(expr=1.2*(10.5*m.x179/(10.5 - m.x479) + 4.04*m.x199/(4.04 - m.x479) + 1.76*m.x219/(1.76 - m.x479) + 
                         1.31*m.x239/(1.31 - m.x479) + m.x259/(1 - m.x479)) + 10*m.b19 - m.x399 <= 10)

m.c428 = Constraint(expr=1.2*(10.5*m.x180/(10.5 - m.x480) + 4.04*m.x200/(4.04 - m.x480) + 1.76*m.x220/(1.76 - m.x480) + 
                         1.31*m.x240/(1.31 - m.x480) + m.x260/(1 - m.x480)) + 10*m.b20 - m.x400 <= 10)

m.c429 = Constraint(expr=1.2*(10.5*m.x161/(10.5 - m.x461) + 4.04*m.x181/(4.04 - m.x461) + 1.76*m.x201/(1.76 - m.x461) + 
                         1.31*m.x221/(1.31 - m.x461) + m.x241/(1 - m.x461)) - 10*m.b1 - m.x381 >= -10)

m.c430 = Constraint(expr=1.2*(10.5*m.x162/(10.5 - m.x462) + 4.04*m.x182/(4.04 - m.x462) + 1.76*m.x202/(1.76 - m.x462) + 
                         1.31*m.x222/(1.31 - m.x462) + m.x242/(1 - m.x462)) - 10*m.b2 - m.x382 >= -10)

m.c431 = Constraint(expr=1.2*(10.5*m.x163/(10.5 - m.x463) + 4.04*m.x183/(4.04 - m.x463) + 1.76*m.x203/(1.76 - m.x463) + 
                         1.31*m.x223/(1.31 - m.x463) + m.x243/(1 - m.x463)) - 10*m.b3 - m.x383 >= -10)

m.c432 = Constraint(expr=1.2*(10.5*m.x164/(10.5 - m.x464) + 4.04*m.x184/(4.04 - m.x464) + 1.76*m.x204/(1.76 - m.x464) + 
                         1.31*m.x224/(1.31 - m.x464) + m.x244/(1 - m.x464)) - 10*m.b4 - m.x384 >= -10)

m.c433 = Constraint(expr=1.2*(10.5*m.x165/(10.5 - m.x465) + 4.04*m.x185/(4.04 - m.x465) + 1.76*m.x205/(1.76 - m.x465) + 
                         1.31*m.x225/(1.31 - m.x465) + m.x245/(1 - m.x465)) - 10*m.b5 - m.x385 >= -10)

m.c434 = Constraint(expr=1.2*(10.5*m.x166/(10.5 - m.x466) + 4.04*m.x186/(4.04 - m.x466) + 1.76*m.x206/(1.76 - m.x466) + 
                         1.31*m.x226/(1.31 - m.x466) + m.x246/(1 - m.x466)) - 10*m.b6 - m.x386 >= -10)

m.c435 = Constraint(expr=1.2*(10.5*m.x167/(10.5 - m.x467) + 4.04*m.x187/(4.04 - m.x467) + 1.76*m.x207/(1.76 - m.x467) + 
                         1.31*m.x227/(1.31 - m.x467) + m.x247/(1 - m.x467)) - 10*m.b7 - m.x387 >= -10)

m.c436 = Constraint(expr=1.2*(10.5*m.x168/(10.5 - m.x468) + 4.04*m.x188/(4.04 - m.x468) + 1.76*m.x208/(1.76 - m.x468) + 
                         1.31*m.x228/(1.31 - m.x468) + m.x248/(1 - m.x468)) - 10*m.b8 - m.x388 >= -10)

m.c437 = Constraint(expr=1.2*(10.5*m.x169/(10.5 - m.x469) + 4.04*m.x189/(4.04 - m.x469) + 1.76*m.x209/(1.76 - m.x469) + 
                         1.31*m.x229/(1.31 - m.x469) + m.x249/(1 - m.x469)) - 10*m.b9 - m.x389 >= -10)

m.c438 = Constraint(expr=1.2*(10.5*m.x170/(10.5 - m.x470) + 4.04*m.x190/(4.04 - m.x470) + 1.76*m.x210/(1.76 - m.x470) + 
                         1.31*m.x230/(1.31 - m.x470) + m.x250/(1 - m.x470)) - 10*m.b10 - m.x390 >= -10)

m.c439 = Constraint(expr=1.2*(10.5*m.x171/(10.5 - m.x471) + 4.04*m.x191/(4.04 - m.x471) + 1.76*m.x211/(1.76 - m.x471) + 
                         1.31*m.x231/(1.31 - m.x471) + m.x251/(1 - m.x471)) - 10*m.b11 - m.x391 >= -10)

m.c440 = Constraint(expr=1.2*(10.5*m.x172/(10.5 - m.x472) + 4.04*m.x192/(4.04 - m.x472) + 1.76*m.x212/(1.76 - m.x472) + 
                         1.31*m.x232/(1.31 - m.x472) + m.x252/(1 - m.x472)) - 10*m.b12 - m.x392 >= -10)

m.c441 = Constraint(expr=1.2*(10.5*m.x173/(10.5 - m.x473) + 4.04*m.x193/(4.04 - m.x473) + 1.76*m.x213/(1.76 - m.x473) + 
                         1.31*m.x233/(1.31 - m.x473) + m.x253/(1 - m.x473)) - 10*m.b13 - m.x393 >= -10)

m.c442 = Constraint(expr=1.2*(10.5*m.x174/(10.5 - m.x474) + 4.04*m.x194/(4.04 - m.x474) + 1.76*m.x214/(1.76 - m.x474) + 
                         1.31*m.x234/(1.31 - m.x474) + m.x254/(1 - m.x474)) - 10*m.b14 - m.x394 >= -10)

m.c443 = Constraint(expr=1.2*(10.5*m.x175/(10.5 - m.x475) + 4.04*m.x195/(4.04 - m.x475) + 1.76*m.x215/(1.76 - m.x475) + 
                         1.31*m.x235/(1.31 - m.x475) + m.x255/(1 - m.x475)) - 10*m.b15 - m.x395 >= -10)

m.c444 = Constraint(expr=1.2*(10.5*m.x176/(10.5 - m.x476) + 4.04*m.x196/(4.04 - m.x476) + 1.76*m.x216/(1.76 - m.x476) + 
                         1.31*m.x236/(1.31 - m.x476) + m.x256/(1 - m.x476)) - 10*m.b16 - m.x396 >= -10)

m.c445 = Constraint(expr=1.2*(10.5*m.x177/(10.5 - m.x477) + 4.04*m.x197/(4.04 - m.x477) + 1.76*m.x217/(1.76 - m.x477) + 
                         1.31*m.x237/(1.31 - m.x477) + m.x257/(1 - m.x477)) - 10*m.b17 - m.x397 >= -10)

m.c446 = Constraint(expr=1.2*(10.5*m.x178/(10.5 - m.x478) + 4.04*m.x198/(4.04 - m.x478) + 1.76*m.x218/(1.76 - m.x478) + 
                         1.31*m.x238/(1.31 - m.x478) + m.x258/(1 - m.x478)) - 10*m.b18 - m.x398 >= -10)

m.c447 = Constraint(expr=1.2*(10.5*m.x179/(10.5 - m.x479) + 4.04*m.x199/(4.04 - m.x479) + 1.76*m.x219/(1.76 - m.x479) + 
                         1.31*m.x239/(1.31 - m.x479) + m.x259/(1 - m.x479)) - 10*m.b19 - m.x399 >= -10)

m.c448 = Constraint(expr=1.2*(10.5*m.x180/(10.5 - m.x480) + 4.04*m.x200/(4.04 - m.x480) + 1.76*m.x220/(1.76 - m.x480) + 
                         1.31*m.x240/(1.31 - m.x480) + m.x260/(1 - m.x480)) - 10*m.b20 - m.x400 >= -10)

m.c449 = Constraint(expr=1.2*(10.5*m.x281/(10.5 - m.x461) + 4.04*m.x301/(4.04 - m.x461) + 1.76*m.x321/(1.76 - m.x461) + 
                         1.31*m.x341/(1.31 - m.x461) + m.x361/(1 - m.x461)) + 10*m.b1 + m.x401 <= 10)

m.c450 = Constraint(expr=1.2*(10.5*m.x282/(10.5 - m.x462) + 4.04*m.x302/(4.04 - m.x462) + 1.76*m.x322/(1.76 - m.x462) + 
                         1.31*m.x342/(1.31 - m.x462) + m.x362/(1 - m.x462)) + 10*m.b2 + m.x402 <= 10)

m.c451 = Constraint(expr=1.2*(10.5*m.x283/(10.5 - m.x463) + 4.04*m.x303/(4.04 - m.x463) + 1.76*m.x323/(1.76 - m.x463) + 
                         1.31*m.x343/(1.31 - m.x463) + m.x363/(1 - m.x463)) + 10*m.b3 + m.x403 <= 10)

m.c452 = Constraint(expr=1.2*(10.5*m.x284/(10.5 - m.x464) + 4.04*m.x304/(4.04 - m.x464) + 1.76*m.x324/(1.76 - m.x464) + 
                         1.31*m.x344/(1.31 - m.x464) + m.x364/(1 - m.x464)) + 10*m.b4 + m.x404 <= 10)

m.c453 = Constraint(expr=1.2*(10.5*m.x285/(10.5 - m.x465) + 4.04*m.x305/(4.04 - m.x465) + 1.76*m.x325/(1.76 - m.x465) + 
                         1.31*m.x345/(1.31 - m.x465) + m.x365/(1 - m.x465)) + 10*m.b5 + m.x405 <= 10)

m.c454 = Constraint(expr=1.2*(10.5*m.x286/(10.5 - m.x466) + 4.04*m.x306/(4.04 - m.x466) + 1.76*m.x326/(1.76 - m.x466) + 
                         1.31*m.x346/(1.31 - m.x466) + m.x366/(1 - m.x466)) + 10*m.b6 + m.x406 <= 10)

m.c455 = Constraint(expr=1.2*(10.5*m.x287/(10.5 - m.x467) + 4.04*m.x307/(4.04 - m.x467) + 1.76*m.x327/(1.76 - m.x467) + 
                         1.31*m.x347/(1.31 - m.x467) + m.x367/(1 - m.x467)) + 10*m.b7 + m.x407 <= 10)

m.c456 = Constraint(expr=1.2*(10.5*m.x288/(10.5 - m.x468) + 4.04*m.x308/(4.04 - m.x468) + 1.76*m.x328/(1.76 - m.x468) + 
                         1.31*m.x348/(1.31 - m.x468) + m.x368/(1 - m.x468)) + 10*m.b8 + m.x408 <= 10)

m.c457 = Constraint(expr=1.2*(10.5*m.x289/(10.5 - m.x469) + 4.04*m.x309/(4.04 - m.x469) + 1.76*m.x329/(1.76 - m.x469) + 
                         1.31*m.x349/(1.31 - m.x469) + m.x369/(1 - m.x469)) + 10*m.b9 + m.x409 <= 10)

m.c458 = Constraint(expr=1.2*(10.5*m.x290/(10.5 - m.x470) + 4.04*m.x310/(4.04 - m.x470) + 1.76*m.x330/(1.76 - m.x470) + 
                         1.31*m.x350/(1.31 - m.x470) + m.x370/(1 - m.x470)) + 10*m.b10 + m.x410 <= 10)

m.c459 = Constraint(expr=1.2*(10.5*m.x291/(10.5 - m.x471) + 4.04*m.x311/(4.04 - m.x471) + 1.76*m.x331/(1.76 - m.x471) + 
                         1.31*m.x351/(1.31 - m.x471) + m.x371/(1 - m.x471)) + 10*m.b11 + m.x411 <= 10)

m.c460 = Constraint(expr=1.2*(10.5*m.x292/(10.5 - m.x472) + 4.04*m.x312/(4.04 - m.x472) + 1.76*m.x332/(1.76 - m.x472) + 
                         1.31*m.x352/(1.31 - m.x472) + m.x372/(1 - m.x472)) + 10*m.b12 + m.x412 <= 10)

m.c461 = Constraint(expr=1.2*(10.5*m.x293/(10.5 - m.x473) + 4.04*m.x313/(4.04 - m.x473) + 1.76*m.x333/(1.76 - m.x473) + 
                         1.31*m.x353/(1.31 - m.x473) + m.x373/(1 - m.x473)) + 10*m.b13 + m.x413 <= 10)

m.c462 = Constraint(expr=1.2*(10.5*m.x294/(10.5 - m.x474) + 4.04*m.x314/(4.04 - m.x474) + 1.76*m.x334/(1.76 - m.x474) + 
                         1.31*m.x354/(1.31 - m.x474) + m.x374/(1 - m.x474)) + 10*m.b14 + m.x414 <= 10)

m.c463 = Constraint(expr=1.2*(10.5*m.x295/(10.5 - m.x475) + 4.04*m.x315/(4.04 - m.x475) + 1.76*m.x335/(1.76 - m.x475) + 
                         1.31*m.x355/(1.31 - m.x475) + m.x375/(1 - m.x475)) + 10*m.b15 + m.x415 <= 10)

m.c464 = Constraint(expr=1.2*(10.5*m.x296/(10.5 - m.x476) + 4.04*m.x316/(4.04 - m.x476) + 1.76*m.x336/(1.76 - m.x476) + 
                         1.31*m.x356/(1.31 - m.x476) + m.x376/(1 - m.x476)) + 10*m.b16 + m.x416 <= 10)

m.c465 = Constraint(expr=1.2*(10.5*m.x297/(10.5 - m.x477) + 4.04*m.x317/(4.04 - m.x477) + 1.76*m.x337/(1.76 - m.x477) + 
                         1.31*m.x357/(1.31 - m.x477) + m.x377/(1 - m.x477)) + 10*m.b17 + m.x417 <= 10)

m.c466 = Constraint(expr=1.2*(10.5*m.x298/(10.5 - m.x478) + 4.04*m.x318/(4.04 - m.x478) + 1.76*m.x338/(1.76 - m.x478) + 
                         1.31*m.x358/(1.31 - m.x478) + m.x378/(1 - m.x478)) + 10*m.b18 + m.x418 <= 10)

m.c467 = Constraint(expr=1.2*(10.5*m.x299/(10.5 - m.x479) + 4.04*m.x319/(4.04 - m.x479) + 1.76*m.x339/(1.76 - m.x479) + 
                         1.31*m.x359/(1.31 - m.x479) + m.x379/(1 - m.x479)) + 10*m.b19 + m.x419 <= 10)

m.c468 = Constraint(expr=1.2*(10.5*m.x300/(10.5 - m.x480) + 4.04*m.x320/(4.04 - m.x480) + 1.76*m.x340/(1.76 - m.x480) + 
                         1.31*m.x360/(1.31 - m.x480) + m.x380/(1 - m.x480)) + 10*m.b20 + m.x420 <= 10)

m.c469 = Constraint(expr=1.2*(10.5*m.x281/(10.5 - m.x461) + 4.04*m.x301/(4.04 - m.x461) + 1.76*m.x321/(1.76 - m.x461) + 
                         1.31*m.x341/(1.31 - m.x461) + m.x361/(1 - m.x461)) - 10*m.b1 + m.x401 >= -10)

m.c470 = Constraint(expr=1.2*(10.5*m.x282/(10.5 - m.x462) + 4.04*m.x302/(4.04 - m.x462) + 1.76*m.x322/(1.76 - m.x462) + 
                         1.31*m.x342/(1.31 - m.x462) + m.x362/(1 - m.x462)) - 10*m.b2 + m.x402 >= -10)

m.c471 = Constraint(expr=1.2*(10.5*m.x283/(10.5 - m.x463) + 4.04*m.x303/(4.04 - m.x463) + 1.76*m.x323/(1.76 - m.x463) + 
                         1.31*m.x343/(1.31 - m.x463) + m.x363/(1 - m.x463)) - 10*m.b3 + m.x403 >= -10)

m.c472 = Constraint(expr=1.2*(10.5*m.x284/(10.5 - m.x464) + 4.04*m.x304/(4.04 - m.x464) + 1.76*m.x324/(1.76 - m.x464) + 
                         1.31*m.x344/(1.31 - m.x464) + m.x364/(1 - m.x464)) - 10*m.b4 + m.x404 >= -10)

m.c473 = Constraint(expr=1.2*(10.5*m.x285/(10.5 - m.x465) + 4.04*m.x305/(4.04 - m.x465) + 1.76*m.x325/(1.76 - m.x465) + 
                         1.31*m.x345/(1.31 - m.x465) + m.x365/(1 - m.x465)) - 10*m.b5 + m.x405 >= -10)

m.c474 = Constraint(expr=1.2*(10.5*m.x286/(10.5 - m.x466) + 4.04*m.x306/(4.04 - m.x466) + 1.76*m.x326/(1.76 - m.x466) + 
                         1.31*m.x346/(1.31 - m.x466) + m.x366/(1 - m.x466)) - 10*m.b6 + m.x406 >= -10)

m.c475 = Constraint(expr=1.2*(10.5*m.x287/(10.5 - m.x467) + 4.04*m.x307/(4.04 - m.x467) + 1.76*m.x327/(1.76 - m.x467) + 
                         1.31*m.x347/(1.31 - m.x467) + m.x367/(1 - m.x467)) - 10*m.b7 + m.x407 >= -10)

m.c476 = Constraint(expr=1.2*(10.5*m.x288/(10.5 - m.x468) + 4.04*m.x308/(4.04 - m.x468) + 1.76*m.x328/(1.76 - m.x468) + 
                         1.31*m.x348/(1.31 - m.x468) + m.x368/(1 - m.x468)) - 10*m.b8 + m.x408 >= -10)

m.c477 = Constraint(expr=1.2*(10.5*m.x289/(10.5 - m.x469) + 4.04*m.x309/(4.04 - m.x469) + 1.76*m.x329/(1.76 - m.x469) + 
                         1.31*m.x349/(1.31 - m.x469) + m.x369/(1 - m.x469)) - 10*m.b9 + m.x409 >= -10)

m.c478 = Constraint(expr=1.2*(10.5*m.x290/(10.5 - m.x470) + 4.04*m.x310/(4.04 - m.x470) + 1.76*m.x330/(1.76 - m.x470) + 
                         1.31*m.x350/(1.31 - m.x470) + m.x370/(1 - m.x470)) - 10*m.b10 + m.x410 >= -10)

m.c479 = Constraint(expr=1.2*(10.5*m.x291/(10.5 - m.x471) + 4.04*m.x311/(4.04 - m.x471) + 1.76*m.x331/(1.76 - m.x471) + 
                         1.31*m.x351/(1.31 - m.x471) + m.x371/(1 - m.x471)) - 10*m.b11 + m.x411 >= -10)

m.c480 = Constraint(expr=1.2*(10.5*m.x292/(10.5 - m.x472) + 4.04*m.x312/(4.04 - m.x472) + 1.76*m.x332/(1.76 - m.x472) + 
                         1.31*m.x352/(1.31 - m.x472) + m.x372/(1 - m.x472)) - 10*m.b12 + m.x412 >= -10)

m.c481 = Constraint(expr=1.2*(10.5*m.x293/(10.5 - m.x473) + 4.04*m.x313/(4.04 - m.x473) + 1.76*m.x333/(1.76 - m.x473) + 
                         1.31*m.x353/(1.31 - m.x473) + m.x373/(1 - m.x473)) - 10*m.b13 + m.x413 >= -10)

m.c482 = Constraint(expr=1.2*(10.5*m.x294/(10.5 - m.x474) + 4.04*m.x314/(4.04 - m.x474) + 1.76*m.x334/(1.76 - m.x474) + 
                         1.31*m.x354/(1.31 - m.x474) + m.x374/(1 - m.x474)) - 10*m.b14 + m.x414 >= -10)

m.c483 = Constraint(expr=1.2*(10.5*m.x295/(10.5 - m.x475) + 4.04*m.x315/(4.04 - m.x475) + 1.76*m.x335/(1.76 - m.x475) + 
                         1.31*m.x355/(1.31 - m.x475) + m.x375/(1 - m.x475)) - 10*m.b15 + m.x415 >= -10)

m.c484 = Constraint(expr=1.2*(10.5*m.x296/(10.5 - m.x476) + 4.04*m.x316/(4.04 - m.x476) + 1.76*m.x336/(1.76 - m.x476) + 
                         1.31*m.x356/(1.31 - m.x476) + m.x376/(1 - m.x476)) - 10*m.b16 + m.x416 >= -10)

m.c485 = Constraint(expr=1.2*(10.5*m.x297/(10.5 - m.x477) + 4.04*m.x317/(4.04 - m.x477) + 1.76*m.x337/(1.76 - m.x477) + 
                         1.31*m.x357/(1.31 - m.x477) + m.x377/(1 - m.x477)) - 10*m.b17 + m.x417 >= -10)

m.c486 = Constraint(expr=1.2*(10.5*m.x298/(10.5 - m.x478) + 4.04*m.x318/(4.04 - m.x478) + 1.76*m.x338/(1.76 - m.x478) + 
                         1.31*m.x358/(1.31 - m.x478) + m.x378/(1 - m.x478)) - 10*m.b18 + m.x418 >= -10)

m.c487 = Constraint(expr=1.2*(10.5*m.x299/(10.5 - m.x479) + 4.04*m.x319/(4.04 - m.x479) + 1.76*m.x339/(1.76 - m.x479) + 
                         1.31*m.x359/(1.31 - m.x479) + m.x379/(1 - m.x479)) - 10*m.b19 + m.x419 >= -10)

m.c488 = Constraint(expr=1.2*(10.5*m.x300/(10.5 - m.x480) + 4.04*m.x320/(4.04 - m.x480) + 1.76*m.x340/(1.76 - m.x480) + 
                         1.31*m.x360/(1.31 - m.x480) + m.x380/(1 - m.x480)) - 10*m.b20 + m.x420 >= -10)

m.c489 = Constraint(expr= - 2*m.b1 + m.x21 <= 0)

m.c490 = Constraint(expr= - 2*m.b2 + m.x22 <= 0)

m.c491 = Constraint(expr= - 2*m.b3 + m.x23 <= 0)

m.c492 = Constraint(expr= - 2*m.b4 + m.x24 <= 0)

m.c493 = Constraint(expr= - 2*m.b5 + m.x25 <= 0)

m.c494 = Constraint(expr= - 2*m.b6 + m.x26 <= 0)

m.c495 = Constraint(expr= - 2*m.b7 + m.x27 <= 0)

m.c496 = Constraint(expr= - 2*m.b8 + m.x28 <= 0)

m.c497 = Constraint(expr= - 2*m.b9 + m.x29 <= 0)

m.c498 = Constraint(expr= - 2*m.b10 + m.x30 <= 0)

m.c499 = Constraint(expr= - 2*m.b11 + m.x31 <= 0)

m.c500 = Constraint(expr= - 2*m.b12 + m.x32 <= 0)

m.c501 = Constraint(expr= - 2*m.b13 + m.x33 <= 0)

m.c502 = Constraint(expr= - 2*m.b14 + m.x34 <= 0)

m.c503 = Constraint(expr= - 2*m.b15 + m.x35 <= 0)

m.c504 = Constraint(expr= - 2*m.b16 + m.x36 <= 0)

m.c505 = Constraint(expr= - 2*m.b17 + m.x37 <= 0)

m.c506 = Constraint(expr= - 2*m.b18 + m.x38 <= 0)

m.c507 = Constraint(expr= - 2*m.b19 + m.x39 <= 0)

m.c508 = Constraint(expr= - 2*m.b20 + m.x40 <= 0)

m.c509 = Constraint(expr= - 0.6*m.b1 + m.x41 <= 0)

m.c510 = Constraint(expr= - 0.6*m.b2 + m.x42 <= 0)

m.c511 = Constraint(expr= - 0.6*m.b3 + m.x43 <= 0)

m.c512 = Constraint(expr= - 0.6*m.b4 + m.x44 <= 0)

m.c513 = Constraint(expr= - 0.6*m.b5 + m.x45 <= 0)

m.c514 = Constraint(expr= - 0.6*m.b6 + m.x46 <= 0)

m.c515 = Constraint(expr= - 0.6*m.b7 + m.x47 <= 0)

m.c516 = Constraint(expr= - 0.6*m.b8 + m.x48 <= 0)

m.c517 = Constraint(expr= - 0.6*m.b9 + m.x49 <= 0)

m.c518 = Constraint(expr= - 0.6*m.b10 + m.x50 <= 0)

m.c519 = Constraint(expr= - 0.6*m.b11 + m.x51 <= 0)

m.c520 = Constraint(expr= - 0.6*m.b12 + m.x52 <= 0)

m.c521 = Constraint(expr= - 0.6*m.b13 + m.x53 <= 0)

m.c522 = Constraint(expr= - 0.6*m.b14 + m.x54 <= 0)

m.c523 = Constraint(expr= - 0.6*m.b15 + m.x55 <= 0)

m.c524 = Constraint(expr= - 0.6*m.b16 + m.x56 <= 0)

m.c525 = Constraint(expr= - 0.6*m.b17 + m.x57 <= 0)

m.c526 = Constraint(expr= - 0.6*m.b18 + m.x58 <= 0)

m.c527 = Constraint(expr= - 0.6*m.b19 + m.x59 <= 0)

m.c528 = Constraint(expr= - 0.6*m.b20 + m.x60 <= 0)

m.c529 = Constraint(expr= - 0.4*m.b1 + m.x61 <= 0)

m.c530 = Constraint(expr= - 0.4*m.b2 + m.x62 <= 0)

m.c531 = Constraint(expr= - 0.4*m.b3 + m.x63 <= 0)

m.c532 = Constraint(expr= - 0.4*m.b4 + m.x64 <= 0)

m.c533 = Constraint(expr= - 0.4*m.b5 + m.x65 <= 0)

m.c534 = Constraint(expr= - 0.4*m.b6 + m.x66 <= 0)

m.c535 = Constraint(expr= - 0.4*m.b7 + m.x67 <= 0)

m.c536 = Constraint(expr= - 0.4*m.b8 + m.x68 <= 0)

m.c537 = Constraint(expr= - 0.4*m.b9 + m.x69 <= 0)

m.c538 = Constraint(expr= - 0.4*m.b10 + m.x70 <= 0)

m.c539 = Constraint(expr= - 0.4*m.b11 + m.x71 <= 0)

m.c540 = Constraint(expr= - 0.4*m.b12 + m.x72 <= 0)

m.c541 = Constraint(expr= - 0.4*m.b13 + m.x73 <= 0)

m.c542 = Constraint(expr= - 0.4*m.b14 + m.x74 <= 0)

m.c543 = Constraint(expr= - 0.4*m.b15 + m.x75 <= 0)

m.c544 = Constraint(expr= - 0.4*m.b16 + m.x76 <= 0)

m.c545 = Constraint(expr= - 0.4*m.b17 + m.x77 <= 0)

m.c546 = Constraint(expr= - 0.4*m.b18 + m.x78 <= 0)

m.c547 = Constraint(expr= - 0.4*m.b19 + m.x79 <= 0)

m.c548 = Constraint(expr= - 0.4*m.b20 + m.x80 <= 0)

m.c549 = Constraint(expr= - 0.2*m.b1 + m.x81 <= 0)

m.c550 = Constraint(expr= - 0.2*m.b2 + m.x82 <= 0)

m.c551 = Constraint(expr= - 0.2*m.b3 + m.x83 <= 0)

m.c552 = Constraint(expr= - 0.2*m.b4 + m.x84 <= 0)

m.c553 = Constraint(expr= - 0.2*m.b5 + m.x85 <= 0)

m.c554 = Constraint(expr= - 0.2*m.b6 + m.x86 <= 0)

m.c555 = Constraint(expr= - 0.2*m.b7 + m.x87 <= 0)

m.c556 = Constraint(expr= - 0.2*m.b8 + m.x88 <= 0)

m.c557 = Constraint(expr= - 0.2*m.b9 + m.x89 <= 0)

m.c558 = Constraint(expr= - 0.2*m.b10 + m.x90 <= 0)

m.c559 = Constraint(expr= - 0.2*m.b11 + m.x91 <= 0)

m.c560 = Constraint(expr= - 0.2*m.b12 + m.x92 <= 0)

m.c561 = Constraint(expr= - 0.2*m.b13 + m.x93 <= 0)

m.c562 = Constraint(expr= - 0.2*m.b14 + m.x94 <= 0)

m.c563 = Constraint(expr= - 0.2*m.b15 + m.x95 <= 0)

m.c564 = Constraint(expr= - 0.2*m.b16 + m.x96 <= 0)

m.c565 = Constraint(expr= - 0.2*m.b17 + m.x97 <= 0)

m.c566 = Constraint(expr= - 0.2*m.b18 + m.x98 <= 0)

m.c567 = Constraint(expr= - 0.2*m.b19 + m.x99 <= 0)

m.c568 = Constraint(expr= - 0.2*m.b20 + m.x100 <= 0)

m.c569 = Constraint(expr= - 0.4*m.b1 + m.x101 <= 0)

m.c570 = Constraint(expr= - 0.4*m.b2 + m.x102 <= 0)

m.c571 = Constraint(expr= - 0.4*m.b3 + m.x103 <= 0)

m.c572 = Constraint(expr= - 0.4*m.b4 + m.x104 <= 0)

m.c573 = Constraint(expr= - 0.4*m.b5 + m.x105 <= 0)

m.c574 = Constraint(expr= - 0.4*m.b6 + m.x106 <= 0)

m.c575 = Constraint(expr= - 0.4*m.b7 + m.x107 <= 0)

m.c576 = Constraint(expr= - 0.4*m.b8 + m.x108 <= 0)

m.c577 = Constraint(expr= - 0.4*m.b9 + m.x109 <= 0)

m.c578 = Constraint(expr= - 0.4*m.b10 + m.x110 <= 0)

m.c579 = Constraint(expr= - 0.4*m.b11 + m.x111 <= 0)

m.c580 = Constraint(expr= - 0.4*m.b12 + m.x112 <= 0)

m.c581 = Constraint(expr= - 0.4*m.b13 + m.x113 <= 0)

m.c582 = Constraint(expr= - 0.4*m.b14 + m.x114 <= 0)

m.c583 = Constraint(expr= - 0.4*m.b15 + m.x115 <= 0)

m.c584 = Constraint(expr= - 0.4*m.b16 + m.x116 <= 0)

m.c585 = Constraint(expr= - 0.4*m.b17 + m.x117 <= 0)

m.c586 = Constraint(expr= - 0.4*m.b18 + m.x118 <= 0)

m.c587 = Constraint(expr= - 0.4*m.b19 + m.x119 <= 0)

m.c588 = Constraint(expr= - 0.4*m.b20 + m.x120 <= 0)

m.c589 = Constraint(expr= - 0.4*m.b1 + m.x121 <= 0)

m.c590 = Constraint(expr= - 0.4*m.b2 + m.x122 <= 0)

m.c591 = Constraint(expr= - 0.4*m.b3 + m.x123 <= 0)

m.c592 = Constraint(expr= - 0.4*m.b4 + m.x124 <= 0)

m.c593 = Constraint(expr= - 0.4*m.b5 + m.x125 <= 0)

m.c594 = Constraint(expr= - 0.4*m.b6 + m.x126 <= 0)

m.c595 = Constraint(expr= - 0.4*m.b7 + m.x127 <= 0)

m.c596 = Constraint(expr= - 0.4*m.b8 + m.x128 <= 0)

m.c597 = Constraint(expr= - 0.4*m.b9 + m.x129 <= 0)

m.c598 = Constraint(expr= - 0.4*m.b10 + m.x130 <= 0)

m.c599 = Constraint(expr= - 0.4*m.b11 + m.x131 <= 0)

m.c600 = Constraint(expr= - 0.4*m.b12 + m.x132 <= 0)

m.c601 = Constraint(expr= - 0.4*m.b13 + m.x133 <= 0)

m.c602 = Constraint(expr= - 0.4*m.b14 + m.x134 <= 0)

m.c603 = Constraint(expr= - 0.4*m.b15 + m.x135 <= 0)

m.c604 = Constraint(expr= - 0.4*m.b16 + m.x136 <= 0)

m.c605 = Constraint(expr= - 0.4*m.b17 + m.x137 <= 0)

m.c606 = Constraint(expr= - 0.4*m.b18 + m.x138 <= 0)

m.c607 = Constraint(expr= - 0.4*m.b19 + m.x139 <= 0)

m.c608 = Constraint(expr= - 0.4*m.b20 + m.x140 <= 0)

m.c609 = Constraint(expr= - 2*m.b1 + m.x141 <= 0)

m.c610 = Constraint(expr= - 2*m.b2 + m.x142 <= 0)

m.c611 = Constraint(expr= - 2*m.b3 + m.x143 <= 0)

m.c612 = Constraint(expr= - 2*m.b4 + m.x144 <= 0)

m.c613 = Constraint(expr= - 2*m.b5 + m.x145 <= 0)

m.c614 = Constraint(expr= - 2*m.b6 + m.x146 <= 0)

m.c615 = Constraint(expr= - 2*m.b7 + m.x147 <= 0)

m.c616 = Constraint(expr= - 2*m.b8 + m.x148 <= 0)

m.c617 = Constraint(expr= - 2*m.b9 + m.x149 <= 0)

m.c618 = Constraint(expr= - 2*m.b10 + m.x150 <= 0)

m.c619 = Constraint(expr= - 2*m.b11 + m.x151 <= 0)

m.c620 = Constraint(expr= - 2*m.b12 + m.x152 <= 0)

m.c621 = Constraint(expr= - 2*m.b13 + m.x153 <= 0)

m.c622 = Constraint(expr= - 2*m.b14 + m.x154 <= 0)

m.c623 = Constraint(expr= - 2*m.b15 + m.x155 <= 0)

m.c624 = Constraint(expr= - 2*m.b16 + m.x156 <= 0)

m.c625 = Constraint(expr= - 2*m.b17 + m.x157 <= 0)

m.c626 = Constraint(expr= - 2*m.b18 + m.x158 <= 0)

m.c627 = Constraint(expr= - 2*m.b19 + m.x159 <= 0)

m.c628 = Constraint(expr= - 2*m.b20 + m.x160 <= 0)

m.c629 = Constraint(expr= - 0.6*m.b1 + m.x161 <= 0)

m.c630 = Constraint(expr= - 0.6*m.b2 + m.x162 <= 0)

m.c631 = Constraint(expr= - 0.6*m.b3 + m.x163 <= 0)

m.c632 = Constraint(expr= - 0.6*m.b4 + m.x164 <= 0)

m.c633 = Constraint(expr= - 0.6*m.b5 + m.x165 <= 0)

m.c634 = Constraint(expr= - 0.6*m.b6 + m.x166 <= 0)

m.c635 = Constraint(expr= - 0.6*m.b7 + m.x167 <= 0)

m.c636 = Constraint(expr= - 0.6*m.b8 + m.x168 <= 0)

m.c637 = Constraint(expr= - 0.6*m.b9 + m.x169 <= 0)

m.c638 = Constraint(expr= - 0.6*m.b10 + m.x170 <= 0)

m.c639 = Constraint(expr= - 0.6*m.b11 + m.x171 <= 0)

m.c640 = Constraint(expr= - 0.6*m.b12 + m.x172 <= 0)

m.c641 = Constraint(expr= - 0.6*m.b13 + m.x173 <= 0)

m.c642 = Constraint(expr= - 0.6*m.b14 + m.x174 <= 0)

m.c643 = Constraint(expr= - 0.6*m.b15 + m.x175 <= 0)

m.c644 = Constraint(expr= - 0.6*m.b16 + m.x176 <= 0)

m.c645 = Constraint(expr= - 0.6*m.b17 + m.x177 <= 0)

m.c646 = Constraint(expr= - 0.6*m.b18 + m.x178 <= 0)

m.c647 = Constraint(expr= - 0.6*m.b19 + m.x179 <= 0)

m.c648 = Constraint(expr= - 0.6*m.b20 + m.x180 <= 0)

m.c649 = Constraint(expr= - 0.4*m.b1 + m.x181 <= 0)

m.c650 = Constraint(expr= - 0.4*m.b2 + m.x182 <= 0)

m.c651 = Constraint(expr= - 0.4*m.b3 + m.x183 <= 0)

m.c652 = Constraint(expr= - 0.4*m.b4 + m.x184 <= 0)

m.c653 = Constraint(expr= - 0.4*m.b5 + m.x185 <= 0)

m.c654 = Constraint(expr= - 0.4*m.b6 + m.x186 <= 0)

m.c655 = Constraint(expr= - 0.4*m.b7 + m.x187 <= 0)

m.c656 = Constraint(expr= - 0.4*m.b8 + m.x188 <= 0)

m.c657 = Constraint(expr= - 0.4*m.b9 + m.x189 <= 0)

m.c658 = Constraint(expr= - 0.4*m.b10 + m.x190 <= 0)

m.c659 = Constraint(expr= - 0.4*m.b11 + m.x191 <= 0)

m.c660 = Constraint(expr= - 0.4*m.b12 + m.x192 <= 0)

m.c661 = Constraint(expr= - 0.4*m.b13 + m.x193 <= 0)

m.c662 = Constraint(expr= - 0.4*m.b14 + m.x194 <= 0)

m.c663 = Constraint(expr= - 0.4*m.b15 + m.x195 <= 0)

m.c664 = Constraint(expr= - 0.4*m.b16 + m.x196 <= 0)

m.c665 = Constraint(expr= - 0.4*m.b17 + m.x197 <= 0)

m.c666 = Constraint(expr= - 0.4*m.b18 + m.x198 <= 0)

m.c667 = Constraint(expr= - 0.4*m.b19 + m.x199 <= 0)

m.c668 = Constraint(expr= - 0.4*m.b20 + m.x200 <= 0)

m.c669 = Constraint(expr= - 0.2*m.b1 + m.x201 <= 0)

m.c670 = Constraint(expr= - 0.2*m.b2 + m.x202 <= 0)

m.c671 = Constraint(expr= - 0.2*m.b3 + m.x203 <= 0)

m.c672 = Constraint(expr= - 0.2*m.b4 + m.x204 <= 0)

m.c673 = Constraint(expr= - 0.2*m.b5 + m.x205 <= 0)

m.c674 = Constraint(expr= - 0.2*m.b6 + m.x206 <= 0)

m.c675 = Constraint(expr= - 0.2*m.b7 + m.x207 <= 0)

m.c676 = Constraint(expr= - 0.2*m.b8 + m.x208 <= 0)

m.c677 = Constraint(expr= - 0.2*m.b9 + m.x209 <= 0)

m.c678 = Constraint(expr= - 0.2*m.b10 + m.x210 <= 0)

m.c679 = Constraint(expr= - 0.2*m.b11 + m.x211 <= 0)

m.c680 = Constraint(expr= - 0.2*m.b12 + m.x212 <= 0)

m.c681 = Constraint(expr= - 0.2*m.b13 + m.x213 <= 0)

m.c682 = Constraint(expr= - 0.2*m.b14 + m.x214 <= 0)

m.c683 = Constraint(expr= - 0.2*m.b15 + m.x215 <= 0)

m.c684 = Constraint(expr= - 0.2*m.b16 + m.x216 <= 0)

m.c685 = Constraint(expr= - 0.2*m.b17 + m.x217 <= 0)

m.c686 = Constraint(expr= - 0.2*m.b18 + m.x218 <= 0)

m.c687 = Constraint(expr= - 0.2*m.b19 + m.x219 <= 0)

m.c688 = Constraint(expr= - 0.2*m.b20 + m.x220 <= 0)

m.c689 = Constraint(expr= - 0.4*m.b1 + m.x221 <= 0)

m.c690 = Constraint(expr= - 0.4*m.b2 + m.x222 <= 0)

m.c691 = Constraint(expr= - 0.4*m.b3 + m.x223 <= 0)

m.c692 = Constraint(expr= - 0.4*m.b4 + m.x224 <= 0)

m.c693 = Constraint(expr= - 0.4*m.b5 + m.x225 <= 0)

m.c694 = Constraint(expr= - 0.4*m.b6 + m.x226 <= 0)

m.c695 = Constraint(expr= - 0.4*m.b7 + m.x227 <= 0)

m.c696 = Constraint(expr= - 0.4*m.b8 + m.x228 <= 0)

m.c697 = Constraint(expr= - 0.4*m.b9 + m.x229 <= 0)

m.c698 = Constraint(expr= - 0.4*m.b10 + m.x230 <= 0)

m.c699 = Constraint(expr= - 0.4*m.b11 + m.x231 <= 0)

m.c700 = Constraint(expr= - 0.4*m.b12 + m.x232 <= 0)

m.c701 = Constraint(expr= - 0.4*m.b13 + m.x233 <= 0)

m.c702 = Constraint(expr= - 0.4*m.b14 + m.x234 <= 0)

m.c703 = Constraint(expr= - 0.4*m.b15 + m.x235 <= 0)

m.c704 = Constraint(expr= - 0.4*m.b16 + m.x236 <= 0)

m.c705 = Constraint(expr= - 0.4*m.b17 + m.x237 <= 0)

m.c706 = Constraint(expr= - 0.4*m.b18 + m.x238 <= 0)

m.c707 = Constraint(expr= - 0.4*m.b19 + m.x239 <= 0)

m.c708 = Constraint(expr= - 0.4*m.b20 + m.x240 <= 0)

m.c709 = Constraint(expr= - 0.4*m.b1 + m.x241 <= 0)

m.c710 = Constraint(expr= - 0.4*m.b2 + m.x242 <= 0)

m.c711 = Constraint(expr= - 0.4*m.b3 + m.x243 <= 0)

m.c712 = Constraint(expr= - 0.4*m.b4 + m.x244 <= 0)

m.c713 = Constraint(expr= - 0.4*m.b5 + m.x245 <= 0)

m.c714 = Constraint(expr= - 0.4*m.b6 + m.x246 <= 0)

m.c715 = Constraint(expr= - 0.4*m.b7 + m.x247 <= 0)

m.c716 = Constraint(expr= - 0.4*m.b8 + m.x248 <= 0)

m.c717 = Constraint(expr= - 0.4*m.b9 + m.x249 <= 0)

m.c718 = Constraint(expr= - 0.4*m.b10 + m.x250 <= 0)

m.c719 = Constraint(expr= - 0.4*m.b11 + m.x251 <= 0)

m.c720 = Constraint(expr= - 0.4*m.b12 + m.x252 <= 0)

m.c721 = Constraint(expr= - 0.4*m.b13 + m.x253 <= 0)

m.c722 = Constraint(expr= - 0.4*m.b14 + m.x254 <= 0)

m.c723 = Constraint(expr= - 0.4*m.b15 + m.x255 <= 0)

m.c724 = Constraint(expr= - 0.4*m.b16 + m.x256 <= 0)

m.c725 = Constraint(expr= - 0.4*m.b17 + m.x257 <= 0)

m.c726 = Constraint(expr= - 0.4*m.b18 + m.x258 <= 0)

m.c727 = Constraint(expr= - 0.4*m.b19 + m.x259 <= 0)

m.c728 = Constraint(expr= - 0.4*m.b20 + m.x260 <= 0)

m.c729 = Constraint(expr= - 2*m.b1 + m.x261 <= 0)

m.c730 = Constraint(expr= - 2*m.b2 + m.x262 <= 0)

m.c731 = Constraint(expr= - 2*m.b3 + m.x263 <= 0)

m.c732 = Constraint(expr= - 2*m.b4 + m.x264 <= 0)

m.c733 = Constraint(expr= - 2*m.b5 + m.x265 <= 0)

m.c734 = Constraint(expr= - 2*m.b6 + m.x266 <= 0)

m.c735 = Constraint(expr= - 2*m.b7 + m.x267 <= 0)

m.c736 = Constraint(expr= - 2*m.b8 + m.x268 <= 0)

m.c737 = Constraint(expr= - 2*m.b9 + m.x269 <= 0)

m.c738 = Constraint(expr= - 2*m.b10 + m.x270 <= 0)

m.c739 = Constraint(expr= - 2*m.b11 + m.x271 <= 0)

m.c740 = Constraint(expr= - 2*m.b12 + m.x272 <= 0)

m.c741 = Constraint(expr= - 2*m.b13 + m.x273 <= 0)

m.c742 = Constraint(expr= - 2*m.b14 + m.x274 <= 0)

m.c743 = Constraint(expr= - 2*m.b15 + m.x275 <= 0)

m.c744 = Constraint(expr= - 2*m.b16 + m.x276 <= 0)

m.c745 = Constraint(expr= - 2*m.b17 + m.x277 <= 0)

m.c746 = Constraint(expr= - 2*m.b18 + m.x278 <= 0)

m.c747 = Constraint(expr= - 2*m.b19 + m.x279 <= 0)

m.c748 = Constraint(expr= - 2*m.b20 + m.x280 <= 0)

m.c749 = Constraint(expr= - 0.6*m.b1 + m.x281 <= 0)

m.c750 = Constraint(expr= - 0.6*m.b2 + m.x282 <= 0)

m.c751 = Constraint(expr= - 0.6*m.b3 + m.x283 <= 0)

m.c752 = Constraint(expr= - 0.6*m.b4 + m.x284 <= 0)

m.c753 = Constraint(expr= - 0.6*m.b5 + m.x285 <= 0)

m.c754 = Constraint(expr= - 0.6*m.b6 + m.x286 <= 0)

m.c755 = Constraint(expr= - 0.6*m.b7 + m.x287 <= 0)

m.c756 = Constraint(expr= - 0.6*m.b8 + m.x288 <= 0)

m.c757 = Constraint(expr= - 0.6*m.b9 + m.x289 <= 0)

m.c758 = Constraint(expr= - 0.6*m.b10 + m.x290 <= 0)

m.c759 = Constraint(expr= - 0.6*m.b11 + m.x291 <= 0)

m.c760 = Constraint(expr= - 0.6*m.b12 + m.x292 <= 0)

m.c761 = Constraint(expr= - 0.6*m.b13 + m.x293 <= 0)

m.c762 = Constraint(expr= - 0.6*m.b14 + m.x294 <= 0)

m.c763 = Constraint(expr= - 0.6*m.b15 + m.x295 <= 0)

m.c764 = Constraint(expr= - 0.6*m.b16 + m.x296 <= 0)

m.c765 = Constraint(expr= - 0.6*m.b17 + m.x297 <= 0)

m.c766 = Constraint(expr= - 0.6*m.b18 + m.x298 <= 0)

m.c767 = Constraint(expr= - 0.6*m.b19 + m.x299 <= 0)

m.c768 = Constraint(expr= - 0.6*m.b20 + m.x300 <= 0)

m.c769 = Constraint(expr= - 0.4*m.b1 + m.x301 <= 0)

m.c770 = Constraint(expr= - 0.4*m.b2 + m.x302 <= 0)

m.c771 = Constraint(expr= - 0.4*m.b3 + m.x303 <= 0)

m.c772 = Constraint(expr= - 0.4*m.b4 + m.x304 <= 0)

m.c773 = Constraint(expr= - 0.4*m.b5 + m.x305 <= 0)

m.c774 = Constraint(expr= - 0.4*m.b6 + m.x306 <= 0)

m.c775 = Constraint(expr= - 0.4*m.b7 + m.x307 <= 0)

m.c776 = Constraint(expr= - 0.4*m.b8 + m.x308 <= 0)

m.c777 = Constraint(expr= - 0.4*m.b9 + m.x309 <= 0)

m.c778 = Constraint(expr= - 0.4*m.b10 + m.x310 <= 0)

m.c779 = Constraint(expr= - 0.4*m.b11 + m.x311 <= 0)

m.c780 = Constraint(expr= - 0.4*m.b12 + m.x312 <= 0)

m.c781 = Constraint(expr= - 0.4*m.b13 + m.x313 <= 0)

m.c782 = Constraint(expr= - 0.4*m.b14 + m.x314 <= 0)

m.c783 = Constraint(expr= - 0.4*m.b15 + m.x315 <= 0)

m.c784 = Constraint(expr= - 0.4*m.b16 + m.x316 <= 0)

m.c785 = Constraint(expr= - 0.4*m.b17 + m.x317 <= 0)

m.c786 = Constraint(expr= - 0.4*m.b18 + m.x318 <= 0)

m.c787 = Constraint(expr= - 0.4*m.b19 + m.x319 <= 0)

m.c788 = Constraint(expr= - 0.4*m.b20 + m.x320 <= 0)

m.c789 = Constraint(expr= - 0.2*m.b1 + m.x321 <= 0)

m.c790 = Constraint(expr= - 0.2*m.b2 + m.x322 <= 0)

m.c791 = Constraint(expr= - 0.2*m.b3 + m.x323 <= 0)

m.c792 = Constraint(expr= - 0.2*m.b4 + m.x324 <= 0)

m.c793 = Constraint(expr= - 0.2*m.b5 + m.x325 <= 0)

m.c794 = Constraint(expr= - 0.2*m.b6 + m.x326 <= 0)

m.c795 = Constraint(expr= - 0.2*m.b7 + m.x327 <= 0)

m.c796 = Constraint(expr= - 0.2*m.b8 + m.x328 <= 0)

m.c797 = Constraint(expr= - 0.2*m.b9 + m.x329 <= 0)

m.c798 = Constraint(expr= - 0.2*m.b10 + m.x330 <= 0)

m.c799 = Constraint(expr= - 0.2*m.b11 + m.x331 <= 0)

m.c800 = Constraint(expr= - 0.2*m.b12 + m.x332 <= 0)

m.c801 = Constraint(expr= - 0.2*m.b13 + m.x333 <= 0)

m.c802 = Constraint(expr= - 0.2*m.b14 + m.x334 <= 0)

m.c803 = Constraint(expr= - 0.2*m.b15 + m.x335 <= 0)

m.c804 = Constraint(expr= - 0.2*m.b16 + m.x336 <= 0)

m.c805 = Constraint(expr= - 0.2*m.b17 + m.x337 <= 0)

m.c806 = Constraint(expr= - 0.2*m.b18 + m.x338 <= 0)

m.c807 = Constraint(expr= - 0.2*m.b19 + m.x339 <= 0)

m.c808 = Constraint(expr= - 0.2*m.b20 + m.x340 <= 0)

m.c809 = Constraint(expr= - 0.4*m.b1 + m.x341 <= 0)

m.c810 = Constraint(expr= - 0.4*m.b2 + m.x342 <= 0)

m.c811 = Constraint(expr= - 0.4*m.b3 + m.x343 <= 0)

m.c812 = Constraint(expr= - 0.4*m.b4 + m.x344 <= 0)

m.c813 = Constraint(expr= - 0.4*m.b5 + m.x345 <= 0)

m.c814 = Constraint(expr= - 0.4*m.b6 + m.x346 <= 0)

m.c815 = Constraint(expr= - 0.4*m.b7 + m.x347 <= 0)

m.c816 = Constraint(expr= - 0.4*m.b8 + m.x348 <= 0)

m.c817 = Constraint(expr= - 0.4*m.b9 + m.x349 <= 0)

m.c818 = Constraint(expr= - 0.4*m.b10 + m.x350 <= 0)

m.c819 = Constraint(expr= - 0.4*m.b11 + m.x351 <= 0)

m.c820 = Constraint(expr= - 0.4*m.b12 + m.x352 <= 0)

m.c821 = Constraint(expr= - 0.4*m.b13 + m.x353 <= 0)

m.c822 = Constraint(expr= - 0.4*m.b14 + m.x354 <= 0)

m.c823 = Constraint(expr= - 0.4*m.b15 + m.x355 <= 0)

m.c824 = Constraint(expr= - 0.4*m.b16 + m.x356 <= 0)

m.c825 = Constraint(expr= - 0.4*m.b17 + m.x357 <= 0)

m.c826 = Constraint(expr= - 0.4*m.b18 + m.x358 <= 0)

m.c827 = Constraint(expr= - 0.4*m.b19 + m.x359 <= 0)

m.c828 = Constraint(expr= - 0.4*m.b20 + m.x360 <= 0)

m.c829 = Constraint(expr= - 0.4*m.b1 + m.x361 <= 0)

m.c830 = Constraint(expr= - 0.4*m.b2 + m.x362 <= 0)

m.c831 = Constraint(expr= - 0.4*m.b3 + m.x363 <= 0)

m.c832 = Constraint(expr= - 0.4*m.b4 + m.x364 <= 0)

m.c833 = Constraint(expr= - 0.4*m.b5 + m.x365 <= 0)

m.c834 = Constraint(expr= - 0.4*m.b6 + m.x366 <= 0)

m.c835 = Constraint(expr= - 0.4*m.b7 + m.x367 <= 0)

m.c836 = Constraint(expr= - 0.4*m.b8 + m.x368 <= 0)

m.c837 = Constraint(expr= - 0.4*m.b9 + m.x369 <= 0)

m.c838 = Constraint(expr= - 0.4*m.b10 + m.x370 <= 0)

m.c839 = Constraint(expr= - 0.4*m.b11 + m.x371 <= 0)

m.c840 = Constraint(expr= - 0.4*m.b12 + m.x372 <= 0)

m.c841 = Constraint(expr= - 0.4*m.b13 + m.x373 <= 0)

m.c842 = Constraint(expr= - 0.4*m.b14 + m.x374 <= 0)

m.c843 = Constraint(expr= - 0.4*m.b15 + m.x375 <= 0)

m.c844 = Constraint(expr= - 0.4*m.b16 + m.x376 <= 0)

m.c845 = Constraint(expr= - 0.4*m.b17 + m.x377 <= 0)

m.c846 = Constraint(expr= - 0.4*m.b18 + m.x378 <= 0)

m.c847 = Constraint(expr= - 0.4*m.b19 + m.x379 <= 0)

m.c848 = Constraint(expr= - 0.4*m.b20 + m.x380 <= 0)

m.c849 = Constraint(expr= - 40*m.b1 + m.x381 <= 0)

m.c850 = Constraint(expr= - 40*m.b2 + m.x382 <= 0)

m.c851 = Constraint(expr= - 40*m.b3 + m.x383 <= 0)

m.c852 = Constraint(expr= - 40*m.b4 + m.x384 <= 0)

m.c853 = Constraint(expr= - 40*m.b5 + m.x385 <= 0)

m.c854 = Constraint(expr= - 40*m.b6 + m.x386 <= 0)

m.c855 = Constraint(expr= - 40*m.b7 + m.x387 <= 0)

m.c856 = Constraint(expr= - 40*m.b8 + m.x388 <= 0)

m.c857 = Constraint(expr= - 40*m.b9 + m.x389 <= 0)

m.c858 = Constraint(expr= - 40*m.b10 + m.x390 <= 0)

m.c859 = Constraint(expr= - 40*m.b11 + m.x391 <= 0)

m.c860 = Constraint(expr= - 40*m.b12 + m.x392 <= 0)

m.c861 = Constraint(expr= - 40*m.b13 + m.x393 <= 0)

m.c862 = Constraint(expr= - 40*m.b14 + m.x394 <= 0)

m.c863 = Constraint(expr= - 40*m.b15 + m.x395 <= 0)

m.c864 = Constraint(expr= - 40*m.b16 + m.x396 <= 0)

m.c865 = Constraint(expr= - 40*m.b17 + m.x397 <= 0)

m.c866 = Constraint(expr= - 40*m.b18 + m.x398 <= 0)

m.c867 = Constraint(expr= - 40*m.b19 + m.x399 <= 0)

m.c868 = Constraint(expr= - 40*m.b20 + m.x400 <= 0)

m.c869 = Constraint(expr= - 40*m.b1 + m.x401 <= 0)

m.c870 = Constraint(expr= - 40*m.b2 + m.x402 <= 0)

m.c871 = Constraint(expr= - 40*m.b3 + m.x403 <= 0)

m.c872 = Constraint(expr= - 40*m.b4 + m.x404 <= 0)

m.c873 = Constraint(expr= - 40*m.b5 + m.x405 <= 0)

m.c874 = Constraint(expr= - 40*m.b6 + m.x406 <= 0)

m.c875 = Constraint(expr= - 40*m.b7 + m.x407 <= 0)

m.c876 = Constraint(expr= - 40*m.b8 + m.x408 <= 0)

m.c877 = Constraint(expr= - 40*m.b9 + m.x409 <= 0)

m.c878 = Constraint(expr= - 40*m.b10 + m.x410 <= 0)

m.c879 = Constraint(expr= - 40*m.b11 + m.x411 <= 0)

m.c880 = Constraint(expr= - 40*m.b12 + m.x412 <= 0)

m.c881 = Constraint(expr= - 40*m.b13 + m.x413 <= 0)

m.c882 = Constraint(expr= - 40*m.b14 + m.x414 <= 0)

m.c883 = Constraint(expr= - 40*m.b15 + m.x415 <= 0)

m.c884 = Constraint(expr= - 40*m.b16 + m.x416 <= 0)

m.c885 = Constraint(expr= - 40*m.b17 + m.x417 <= 0)

m.c886 = Constraint(expr= - 40*m.b18 + m.x418 <= 0)

m.c887 = Constraint(expr= - 40*m.b19 + m.x419 <= 0)

m.c888 = Constraint(expr= - 40*m.b20 + m.x420 <= 0)

m.c889 = Constraint(expr= - 40*m.b1 + m.x421 <= 0)

m.c890 = Constraint(expr= - 40*m.b2 + m.x422 <= 0)

m.c891 = Constraint(expr= - 40*m.b3 + m.x423 <= 0)

m.c892 = Constraint(expr= - 40*m.b4 + m.x424 <= 0)

m.c893 = Constraint(expr= - 40*m.b5 + m.x425 <= 0)

m.c894 = Constraint(expr= - 40*m.b6 + m.x426 <= 0)

m.c895 = Constraint(expr= - 40*m.b7 + m.x427 <= 0)

m.c896 = Constraint(expr= - 40*m.b8 + m.x428 <= 0)

m.c897 = Constraint(expr= - 40*m.b9 + m.x429 <= 0)

m.c898 = Constraint(expr= - 40*m.b10 + m.x430 <= 0)

m.c899 = Constraint(expr= - 40*m.b11 + m.x431 <= 0)

m.c900 = Constraint(expr= - 40*m.b12 + m.x432 <= 0)

m.c901 = Constraint(expr= - 40*m.b13 + m.x433 <= 0)

m.c902 = Constraint(expr= - 40*m.b14 + m.x434 <= 0)

m.c903 = Constraint(expr= - 40*m.b15 + m.x435 <= 0)

m.c904 = Constraint(expr= - 40*m.b16 + m.x436 <= 0)

m.c905 = Constraint(expr= - 40*m.b17 + m.x437 <= 0)

m.c906 = Constraint(expr= - 40*m.b18 + m.x438 <= 0)

m.c907 = Constraint(expr= - 40*m.b19 + m.x439 <= 0)

m.c908 = Constraint(expr= - 40*m.b20 + m.x440 <= 0)

m.c909 = Constraint(expr= - 40*m.b1 + m.x441 <= 0)

m.c910 = Constraint(expr= - 40*m.b2 + m.x442 <= 0)

m.c911 = Constraint(expr= - 40*m.b3 + m.x443 <= 0)

m.c912 = Constraint(expr= - 40*m.b4 + m.x444 <= 0)

m.c913 = Constraint(expr= - 40*m.b5 + m.x445 <= 0)

m.c914 = Constraint(expr= - 40*m.b6 + m.x446 <= 0)

m.c915 = Constraint(expr= - 40*m.b7 + m.x447 <= 0)

m.c916 = Constraint(expr= - 40*m.b8 + m.x448 <= 0)

m.c917 = Constraint(expr= - 40*m.b9 + m.x449 <= 0)

m.c918 = Constraint(expr= - 40*m.b10 + m.x450 <= 0)

m.c919 = Constraint(expr= - 40*m.b11 + m.x451 <= 0)

m.c920 = Constraint(expr= - 40*m.b12 + m.x452 <= 0)

m.c921 = Constraint(expr= - 40*m.b13 + m.x453 <= 0)

m.c922 = Constraint(expr= - 40*m.b14 + m.x454 <= 0)

m.c923 = Constraint(expr= - 40*m.b15 + m.x455 <= 0)

m.c924 = Constraint(expr= - 40*m.b16 + m.x456 <= 0)

m.c925 = Constraint(expr= - 40*m.b17 + m.x457 <= 0)

m.c926 = Constraint(expr= - 40*m.b18 + m.x458 <= 0)

m.c927 = Constraint(expr= - 40*m.b19 + m.x459 <= 0)

m.c928 = Constraint(expr= - 40*m.b20 + m.x460 <= 0)

m.c929 = Constraint(expr=100*m.x501*m.x141 - m.x381*(30.77*m.x161 + 33.19*m.x181 + 35.58*m.x201 + 36.83*m.x221 + 38.3*
                         m.x241) - 1000*m.b1 >= -1000)

m.c930 = Constraint(expr=100*m.x502*m.x142 - m.x382*(30.77*m.x162 + 33.19*m.x182 + 35.58*m.x202 + 36.83*m.x222 + 38.3*
                         m.x242) - 1000*m.b2 >= -1000)

m.c931 = Constraint(expr=100*m.x503*m.x143 - m.x383*(30.77*m.x163 + 33.19*m.x183 + 35.58*m.x203 + 36.83*m.x223 + 38.3*
                         m.x243) - 1000*m.b3 >= -1000)

m.c932 = Constraint(expr=100*m.x504*m.x144 - m.x384*(30.77*m.x164 + 33.19*m.x184 + 35.58*m.x204 + 36.83*m.x224 + 38.3*
                         m.x244) - 1000*m.b4 >= -1000)

m.c933 = Constraint(expr=100*m.x505*m.x145 - m.x385*(30.77*m.x165 + 33.19*m.x185 + 35.58*m.x205 + 36.83*m.x225 + 38.3*
                         m.x245) - 1000*m.b5 >= -1000)

m.c934 = Constraint(expr=100*m.x506*m.x146 - m.x386*(30.77*m.x166 + 33.19*m.x186 + 35.58*m.x206 + 36.83*m.x226 + 38.3*
                         m.x246) - 1000*m.b6 >= -1000)

m.c935 = Constraint(expr=100*m.x507*m.x147 - m.x387*(30.77*m.x167 + 33.19*m.x187 + 35.58*m.x207 + 36.83*m.x227 + 38.3*
                         m.x247) - 1000*m.b7 >= -1000)

m.c936 = Constraint(expr=100*m.x508*m.x148 - m.x388*(30.77*m.x168 + 33.19*m.x188 + 35.58*m.x208 + 36.83*m.x228 + 38.3*
                         m.x248) - 1000*m.b8 >= -1000)

m.c937 = Constraint(expr=100*m.x509*m.x149 - m.x389*(30.77*m.x169 + 33.19*m.x189 + 35.58*m.x209 + 36.83*m.x229 + 38.3*
                         m.x249) - 1000*m.b9 >= -1000)

m.c938 = Constraint(expr=100*m.x510*m.x150 - m.x390*(30.77*m.x170 + 33.19*m.x190 + 35.58*m.x210 + 36.83*m.x230 + 38.3*
                         m.x250) - 1000*m.b10 >= -1000)

m.c939 = Constraint(expr=100*m.x511*m.x151 - m.x391*(30.77*m.x171 + 33.19*m.x191 + 35.58*m.x211 + 36.83*m.x231 + 38.3*
                         m.x251) - 1000*m.b11 >= -1000)

m.c940 = Constraint(expr=100*m.x512*m.x152 - m.x392*(30.77*m.x172 + 33.19*m.x192 + 35.58*m.x212 + 36.83*m.x232 + 38.3*
                         m.x252) - 1000*m.b12 >= -1000)

m.c941 = Constraint(expr=100*m.x513*m.x153 - m.x393*(30.77*m.x173 + 33.19*m.x193 + 35.58*m.x213 + 36.83*m.x233 + 38.3*
                         m.x253) - 1000*m.b13 >= -1000)

m.c942 = Constraint(expr=100*m.x514*m.x154 - m.x394*(30.77*m.x174 + 33.19*m.x194 + 35.58*m.x214 + 36.83*m.x234 + 38.3*
                         m.x254) - 1000*m.b14 >= -1000)

m.c943 = Constraint(expr=100*m.x515*m.x155 - m.x395*(30.77*m.x175 + 33.19*m.x195 + 35.58*m.x215 + 36.83*m.x235 + 38.3*
                         m.x255) - 1000*m.b15 >= -1000)

m.c944 = Constraint(expr=100*m.x516*m.x156 - m.x396*(30.77*m.x176 + 33.19*m.x196 + 35.58*m.x216 + 36.83*m.x236 + 38.3*
                         m.x256) - 1000*m.b16 >= -1000)

m.c945 = Constraint(expr=100*m.x517*m.x157 - m.x397*(30.77*m.x177 + 33.19*m.x197 + 35.58*m.x217 + 36.83*m.x237 + 38.3*
                         m.x257) - 1000*m.b17 >= -1000)

m.c946 = Constraint(expr=100*m.x518*m.x158 - m.x398*(30.77*m.x178 + 33.19*m.x198 + 35.58*m.x218 + 36.83*m.x238 + 38.3*
                         m.x258) - 1000*m.b18 >= -1000)

m.c947 = Constraint(expr=100*m.x519*m.x159 - m.x399*(30.77*m.x179 + 33.19*m.x199 + 35.58*m.x219 + 36.83*m.x239 + 38.3*
                         m.x259) - 1000*m.b19 >= -1000)

m.c948 = Constraint(expr=100*m.x520*m.x160 - m.x400*(30.77*m.x180 + 33.19*m.x200 + 35.58*m.x220 + 36.83*m.x240 + 38.3*
                         m.x260) - 1000*m.b20 >= -1000)

m.c949 = Constraint(expr=100*m.x501*m.x141 - m.x381*(30.77*m.x161 + 33.19*m.x181 + 35.58*m.x201 + 36.83*m.x221 + 38.3*
                         m.x241) + 1000*m.b1 <= 1000)

m.c950 = Constraint(expr=100*m.x502*m.x142 - m.x382*(30.77*m.x162 + 33.19*m.x182 + 35.58*m.x202 + 36.83*m.x222 + 38.3*
                         m.x242) + 1000*m.b2 <= 1000)

m.c951 = Constraint(expr=100*m.x503*m.x143 - m.x383*(30.77*m.x163 + 33.19*m.x183 + 35.58*m.x203 + 36.83*m.x223 + 38.3*
                         m.x243) + 1000*m.b3 <= 1000)

m.c952 = Constraint(expr=100*m.x504*m.x144 - m.x384*(30.77*m.x164 + 33.19*m.x184 + 35.58*m.x204 + 36.83*m.x224 + 38.3*
                         m.x244) + 1000*m.b4 <= 1000)

m.c953 = Constraint(expr=100*m.x505*m.x145 - m.x385*(30.77*m.x165 + 33.19*m.x185 + 35.58*m.x205 + 36.83*m.x225 + 38.3*
                         m.x245) + 1000*m.b5 <= 1000)

m.c954 = Constraint(expr=100*m.x506*m.x146 - m.x386*(30.77*m.x166 + 33.19*m.x186 + 35.58*m.x206 + 36.83*m.x226 + 38.3*
                         m.x246) + 1000*m.b6 <= 1000)

m.c955 = Constraint(expr=100*m.x507*m.x147 - m.x387*(30.77*m.x167 + 33.19*m.x187 + 35.58*m.x207 + 36.83*m.x227 + 38.3*
                         m.x247) + 1000*m.b7 <= 1000)

m.c956 = Constraint(expr=100*m.x508*m.x148 - m.x388*(30.77*m.x168 + 33.19*m.x188 + 35.58*m.x208 + 36.83*m.x228 + 38.3*
                         m.x248) + 1000*m.b8 <= 1000)

m.c957 = Constraint(expr=100*m.x509*m.x149 - m.x389*(30.77*m.x169 + 33.19*m.x189 + 35.58*m.x209 + 36.83*m.x229 + 38.3*
                         m.x249) + 1000*m.b9 <= 1000)

m.c958 = Constraint(expr=100*m.x510*m.x150 - m.x390*(30.77*m.x170 + 33.19*m.x190 + 35.58*m.x210 + 36.83*m.x230 + 38.3*
                         m.x250) + 1000*m.b10 <= 1000)

m.c959 = Constraint(expr=100*m.x511*m.x151 - m.x391*(30.77*m.x171 + 33.19*m.x191 + 35.58*m.x211 + 36.83*m.x231 + 38.3*
                         m.x251) + 1000*m.b11 <= 1000)

m.c960 = Constraint(expr=100*m.x512*m.x152 - m.x392*(30.77*m.x172 + 33.19*m.x192 + 35.58*m.x212 + 36.83*m.x232 + 38.3*
                         m.x252) + 1000*m.b12 <= 1000)

m.c961 = Constraint(expr=100*m.x513*m.x153 - m.x393*(30.77*m.x173 + 33.19*m.x193 + 35.58*m.x213 + 36.83*m.x233 + 38.3*
                         m.x253) + 1000*m.b13 <= 1000)

m.c962 = Constraint(expr=100*m.x514*m.x154 - m.x394*(30.77*m.x174 + 33.19*m.x194 + 35.58*m.x214 + 36.83*m.x234 + 38.3*
                         m.x254) + 1000*m.b14 <= 1000)

m.c963 = Constraint(expr=100*m.x515*m.x155 - m.x395*(30.77*m.x175 + 33.19*m.x195 + 35.58*m.x215 + 36.83*m.x235 + 38.3*
                         m.x255) + 1000*m.b15 <= 1000)

m.c964 = Constraint(expr=100*m.x516*m.x156 - m.x396*(30.77*m.x176 + 33.19*m.x196 + 35.58*m.x216 + 36.83*m.x236 + 38.3*
                         m.x256) + 1000*m.b16 <= 1000)

m.c965 = Constraint(expr=100*m.x517*m.x157 - m.x397*(30.77*m.x177 + 33.19*m.x197 + 35.58*m.x217 + 36.83*m.x237 + 38.3*
                         m.x257) + 1000*m.b17 <= 1000)

m.c966 = Constraint(expr=100*m.x518*m.x158 - m.x398*(30.77*m.x178 + 33.19*m.x198 + 35.58*m.x218 + 36.83*m.x238 + 38.3*
                         m.x258) + 1000*m.b18 <= 1000)

m.c967 = Constraint(expr=100*m.x519*m.x159 - m.x399*(30.77*m.x179 + 33.19*m.x199 + 35.58*m.x219 + 36.83*m.x239 + 38.3*
                         m.x259) + 1000*m.b19 <= 1000)

m.c968 = Constraint(expr=100*m.x520*m.x160 - m.x400*(30.77*m.x180 + 33.19*m.x200 + 35.58*m.x220 + 36.83*m.x240 + 38.3*
                         m.x260) + 1000*m.b20 <= 1000)

m.c969 = Constraint(expr=100*m.x481*m.x261 - m.x401*(30.77*m.x281 + 33.19*m.x301 + 35.58*m.x321 + 36.83*m.x341 + 38.3*
                         m.x361) - 1000*m.b1 >= -1000)

m.c970 = Constraint(expr=100*m.x482*m.x262 - m.x402*(30.77*m.x282 + 33.19*m.x302 + 35.58*m.x322 + 36.83*m.x342 + 38.3*
                         m.x362) - 1000*m.b2 >= -1000)

m.c971 = Constraint(expr=100*m.x483*m.x263 - m.x403*(30.77*m.x283 + 33.19*m.x303 + 35.58*m.x323 + 36.83*m.x343 + 38.3*
                         m.x363) - 1000*m.b3 >= -1000)

m.c972 = Constraint(expr=100*m.x484*m.x264 - m.x404*(30.77*m.x284 + 33.19*m.x304 + 35.58*m.x324 + 36.83*m.x344 + 38.3*
                         m.x364) - 1000*m.b4 >= -1000)

m.c973 = Constraint(expr=100*m.x485*m.x265 - m.x405*(30.77*m.x285 + 33.19*m.x305 + 35.58*m.x325 + 36.83*m.x345 + 38.3*
                         m.x365) - 1000*m.b5 >= -1000)

m.c974 = Constraint(expr=100*m.x486*m.x266 - m.x406*(30.77*m.x286 + 33.19*m.x306 + 35.58*m.x326 + 36.83*m.x346 + 38.3*
                         m.x366) - 1000*m.b6 >= -1000)

m.c975 = Constraint(expr=100*m.x487*m.x267 - m.x407*(30.77*m.x287 + 33.19*m.x307 + 35.58*m.x327 + 36.83*m.x347 + 38.3*
                         m.x367) - 1000*m.b7 >= -1000)

m.c976 = Constraint(expr=100*m.x488*m.x268 - m.x408*(30.77*m.x288 + 33.19*m.x308 + 35.58*m.x328 + 36.83*m.x348 + 38.3*
                         m.x368) - 1000*m.b8 >= -1000)

m.c977 = Constraint(expr=100*m.x489*m.x269 - m.x409*(30.77*m.x289 + 33.19*m.x309 + 35.58*m.x329 + 36.83*m.x349 + 38.3*
                         m.x369) - 1000*m.b9 >= -1000)

m.c978 = Constraint(expr=100*m.x490*m.x270 - m.x410*(30.77*m.x290 + 33.19*m.x310 + 35.58*m.x330 + 36.83*m.x350 + 38.3*
                         m.x370) - 1000*m.b10 >= -1000)

m.c979 = Constraint(expr=100*m.x491*m.x271 - m.x411*(30.77*m.x291 + 33.19*m.x311 + 35.58*m.x331 + 36.83*m.x351 + 38.3*
                         m.x371) - 1000*m.b11 >= -1000)

m.c980 = Constraint(expr=100*m.x492*m.x272 - m.x412*(30.77*m.x292 + 33.19*m.x312 + 35.58*m.x332 + 36.83*m.x352 + 38.3*
                         m.x372) - 1000*m.b12 >= -1000)

m.c981 = Constraint(expr=100*m.x493*m.x273 - m.x413*(30.77*m.x293 + 33.19*m.x313 + 35.58*m.x333 + 36.83*m.x353 + 38.3*
                         m.x373) - 1000*m.b13 >= -1000)

m.c982 = Constraint(expr=100*m.x494*m.x274 - m.x414*(30.77*m.x294 + 33.19*m.x314 + 35.58*m.x334 + 36.83*m.x354 + 38.3*
                         m.x374) - 1000*m.b14 >= -1000)

m.c983 = Constraint(expr=100*m.x495*m.x275 - m.x415*(30.77*m.x295 + 33.19*m.x315 + 35.58*m.x335 + 36.83*m.x355 + 38.3*
                         m.x375) - 1000*m.b15 >= -1000)

m.c984 = Constraint(expr=100*m.x496*m.x276 - m.x416*(30.77*m.x296 + 33.19*m.x316 + 35.58*m.x336 + 36.83*m.x356 + 38.3*
                         m.x376) - 1000*m.b16 >= -1000)

m.c985 = Constraint(expr=100*m.x497*m.x277 - m.x417*(30.77*m.x297 + 33.19*m.x317 + 35.58*m.x337 + 36.83*m.x357 + 38.3*
                         m.x377) - 1000*m.b17 >= -1000)

m.c986 = Constraint(expr=100*m.x498*m.x278 - m.x418*(30.77*m.x298 + 33.19*m.x318 + 35.58*m.x338 + 36.83*m.x358 + 38.3*
                         m.x378) - 1000*m.b18 >= -1000)

m.c987 = Constraint(expr=100*m.x499*m.x279 - m.x419*(30.77*m.x299 + 33.19*m.x319 + 35.58*m.x339 + 36.83*m.x359 + 38.3*
                         m.x379) - 1000*m.b19 >= -1000)

m.c988 = Constraint(expr=100*m.x500*m.x280 - m.x420*(30.77*m.x300 + 33.19*m.x320 + 35.58*m.x340 + 36.83*m.x360 + 38.3*
                         m.x380) - 1000*m.b20 >= -1000)

m.c989 = Constraint(expr=100*m.x481*m.x261 - m.x401*(30.77*m.x281 + 33.19*m.x301 + 35.58*m.x321 + 36.83*m.x341 + 38.3*
                         m.x361) + 1000*m.b1 <= 1000)

m.c990 = Constraint(expr=100*m.x482*m.x262 - m.x402*(30.77*m.x282 + 33.19*m.x302 + 35.58*m.x322 + 36.83*m.x342 + 38.3*
                         m.x362) + 1000*m.b2 <= 1000)

m.c991 = Constraint(expr=100*m.x483*m.x263 - m.x403*(30.77*m.x283 + 33.19*m.x303 + 35.58*m.x323 + 36.83*m.x343 + 38.3*
                         m.x363) + 1000*m.b3 <= 1000)

m.c992 = Constraint(expr=100*m.x484*m.x264 - m.x404*(30.77*m.x284 + 33.19*m.x304 + 35.58*m.x324 + 36.83*m.x344 + 38.3*
                         m.x364) + 1000*m.b4 <= 1000)

m.c993 = Constraint(expr=100*m.x485*m.x265 - m.x405*(30.77*m.x285 + 33.19*m.x305 + 35.58*m.x325 + 36.83*m.x345 + 38.3*
                         m.x365) + 1000*m.b5 <= 1000)

m.c994 = Constraint(expr=100*m.x486*m.x266 - m.x406*(30.77*m.x286 + 33.19*m.x306 + 35.58*m.x326 + 36.83*m.x346 + 38.3*
                         m.x366) + 1000*m.b6 <= 1000)

m.c995 = Constraint(expr=100*m.x487*m.x267 - m.x407*(30.77*m.x287 + 33.19*m.x307 + 35.58*m.x327 + 36.83*m.x347 + 38.3*
                         m.x367) + 1000*m.b7 <= 1000)

m.c996 = Constraint(expr=100*m.x488*m.x268 - m.x408*(30.77*m.x288 + 33.19*m.x308 + 35.58*m.x328 + 36.83*m.x348 + 38.3*
                         m.x368) + 1000*m.b8 <= 1000)

m.c997 = Constraint(expr=100*m.x489*m.x269 - m.x409*(30.77*m.x289 + 33.19*m.x309 + 35.58*m.x329 + 36.83*m.x349 + 38.3*
                         m.x369) + 1000*m.b9 <= 1000)

m.c998 = Constraint(expr=100*m.x490*m.x270 - m.x410*(30.77*m.x290 + 33.19*m.x310 + 35.58*m.x330 + 36.83*m.x350 + 38.3*
                         m.x370) + 1000*m.b10 <= 1000)

m.c999 = Constraint(expr=100*m.x491*m.x271 - m.x411*(30.77*m.x291 + 33.19*m.x311 + 35.58*m.x331 + 36.83*m.x351 + 38.3*
                         m.x371) + 1000*m.b11 <= 1000)

m.c1000 = Constraint(expr=100*m.x492*m.x272 - m.x412*(30.77*m.x292 + 33.19*m.x312 + 35.58*m.x332 + 36.83*m.x352 + 38.3*
                          m.x372) + 1000*m.b12 <= 1000)

m.c1001 = Constraint(expr=100*m.x493*m.x273 - m.x413*(30.77*m.x293 + 33.19*m.x313 + 35.58*m.x333 + 36.83*m.x353 + 38.3*
                          m.x373) + 1000*m.b13 <= 1000)

m.c1002 = Constraint(expr=100*m.x494*m.x274 - m.x414*(30.77*m.x294 + 33.19*m.x314 + 35.58*m.x334 + 36.83*m.x354 + 38.3*
                          m.x374) + 1000*m.b14 <= 1000)

m.c1003 = Constraint(expr=100*m.x495*m.x275 - m.x415*(30.77*m.x295 + 33.19*m.x315 + 35.58*m.x335 + 36.83*m.x355 + 38.3*
                          m.x375) + 1000*m.b15 <= 1000)

m.c1004 = Constraint(expr=100*m.x496*m.x276 - m.x416*(30.77*m.x296 + 33.19*m.x316 + 35.58*m.x336 + 36.83*m.x356 + 38.3*
                          m.x376) + 1000*m.b16 <= 1000)

m.c1005 = Constraint(expr=100*m.x497*m.x277 - m.x417*(30.77*m.x297 + 33.19*m.x317 + 35.58*m.x337 + 36.83*m.x357 + 38.3*
                          m.x377) + 1000*m.b17 <= 1000)

m.c1006 = Constraint(expr=100*m.x498*m.x278 - m.x418*(30.77*m.x298 + 33.19*m.x318 + 35.58*m.x338 + 36.83*m.x358 + 38.3*
                          m.x378) + 1000*m.b18 <= 1000)

m.c1007 = Constraint(expr=100*m.x499*m.x279 - m.x419*(30.77*m.x299 + 33.19*m.x319 + 35.58*m.x339 + 36.83*m.x359 + 38.3*
                          m.x379) + 1000*m.b19 <= 1000)

m.c1008 = Constraint(expr=100*m.x500*m.x280 - m.x420*(30.77*m.x300 + 33.19*m.x320 + 35.58*m.x340 + 36.83*m.x360 + 38.3*
                          m.x380) + 1000*m.b20 <= 1000)

m.c1009 = Constraint(expr= - 1.67762719858172*m.x381 + m.x521 >= 0)

m.c1010 = Constraint(expr= - 1.67762719858172*m.x382 + m.x522 >= 0)

m.c1011 = Constraint(expr= - 1.67762719858172*m.x383 + m.x523 >= 0)

m.c1012 = Constraint(expr= - 1.67762719858172*m.x384 + m.x524 >= 0)

m.c1013 = Constraint(expr= - 1.67762719858172*m.x385 + m.x525 >= 0)

m.c1014 = Constraint(expr= - 1.67762719858172*m.x386 + m.x526 >= 0)

m.c1015 = Constraint(expr= - 1.67762719858172*m.x387 + m.x527 >= 0)

m.c1016 = Constraint(expr= - 1.67762719858172*m.x388 + m.x528 >= 0)

m.c1017 = Constraint(expr= - 1.67762719858172*m.x389 + m.x529 >= 0)

m.c1018 = Constraint(expr= - 1.67762719858172*m.x390 + m.x530 >= 0)

m.c1019 = Constraint(expr= - 1.67762719858172*m.x391 + m.x531 >= 0)

m.c1020 = Constraint(expr= - 1.67762719858172*m.x392 + m.x532 >= 0)

m.c1021 = Constraint(expr= - 1.67762719858172*m.x393 + m.x533 >= 0)

m.c1022 = Constraint(expr= - 1.67762719858172*m.x394 + m.x534 >= 0)

m.c1023 = Constraint(expr= - 1.67762719858172*m.x395 + m.x535 >= 0)

m.c1024 = Constraint(expr= - 1.67762719858172*m.x396 + m.x536 >= 0)

m.c1025 = Constraint(expr= - 1.67762719858172*m.x397 + m.x537 >= 0)

m.c1026 = Constraint(expr= - 1.67762719858172*m.x398 + m.x538 >= 0)

m.c1027 = Constraint(expr= - 1.67762719858172*m.x399 + m.x539 >= 0)

m.c1028 = Constraint(expr= - 1.67762719858172*m.x400 + m.x540 >= 0)

m.c1029 = Constraint(expr= - 13.7791538202982*m.x521 + m.x541 >= 0)

m.c1030 = Constraint(expr= - 15.2408491577645*m.x522 + m.x542 >= 0)

m.c1031 = Constraint(expr= - 35.6315282953964*m.x523 + m.x543 >= 0)

m.c1032 = Constraint(expr= - 38.5904815785076*m.x524 + m.x544 >= 0)

m.c1033 = Constraint(expr= - 13.7791538202982*m.x525 + m.x545 >= 0)

m.c1034 = Constraint(expr= - 35.6315282953964*m.x526 + m.x546 >= 0)

m.c1035 = Constraint(expr= - 35.6315282953964*m.x527 + m.x547 >= 0)

m.c1036 = Constraint(expr= - 15.2408491577645*m.x528 + m.x548 >= 0)

m.c1037 = Constraint(expr= - 35.6315282953964*m.x529 + m.x549 >= 0)

m.c1038 = Constraint(expr= - 38.5904815785076*m.x530 + m.x550 >= 0)

m.c1039 = Constraint(expr= - 13.7791538202982*m.x531 + m.x551 >= 0)

m.c1040 = Constraint(expr= - 15.2408491577645*m.x532 + m.x552 >= 0)

m.c1041 = Constraint(expr= - 15.2408491577645*m.x533 + m.x553 >= 0)

m.c1042 = Constraint(expr= - 35.6315282953964*m.x534 + m.x554 >= 0)

m.c1043 = Constraint(expr= - 35.6315282953964*m.x535 + m.x555 >= 0)

m.c1044 = Constraint(expr= - 38.5904815785076*m.x536 + m.x556 >= 0)

m.c1045 = Constraint(expr= - 13.7791538202982*m.x537 + m.x557 >= 0)

m.c1046 = Constraint(expr= - 15.2408491577645*m.x538 + m.x558 >= 0)

m.c1047 = Constraint(expr= - 35.6315282953964*m.x539 + m.x559 >= 0)

m.c1048 = Constraint(expr= - 38.5904815785076*m.x540 + m.x560 >= 0)

m.c1049 = Constraint(expr=-0.0001*(22.83*m.x521**2 + 406.8*m.x521) + m.x561 >= 0.05711)

m.c1050 = Constraint(expr=-0.0001*(22.83*m.x522**2 + 406.8*m.x522) + m.x562 >= 0.05711)

m.c1051 = Constraint(expr=-0.0001*(22.83*m.x523**2 + 406.8*m.x523) + m.x563 >= 0.05711)

m.c1052 = Constraint(expr=-0.0001*(22.83*m.x524**2 + 406.8*m.x524) + m.x564 >= 0.05711)

m.c1053 = Constraint(expr=-0.0001*(22.83*m.x525**2 + 406.8*m.x525) + m.x565 >= 0.05711)

m.c1054 = Constraint(expr=-0.0001*(22.83*m.x526**2 + 406.8*m.x526) + m.x566 >= 0.05711)

m.c1055 = Constraint(expr=-0.0001*(22.83*m.x527**2 + 406.8*m.x527) + m.x567 >= 0.05711)

m.c1056 = Constraint(expr=-0.0001*(22.83*m.x528**2 + 406.8*m.x528) + m.x568 >= 0.05711)

m.c1057 = Constraint(expr=-0.0001*(22.83*m.x529**2 + 406.8*m.x529) + m.x569 >= 0.05711)

m.c1058 = Constraint(expr=-0.0001*(22.83*m.x530**2 + 406.8*m.x530) + m.x570 >= 0.05711)

m.c1059 = Constraint(expr=-0.0001*(22.83*m.x531**2 + 406.8*m.x531) + m.x571 >= 0.05711)

m.c1060 = Constraint(expr=-0.0001*(22.83*m.x532**2 + 406.8*m.x532) + m.x572 >= 0.05711)

m.c1061 = Constraint(expr=-0.0001*(22.83*m.x533**2 + 406.8*m.x533) + m.x573 >= 0.05711)

m.c1062 = Constraint(expr=-0.0001*(22.83*m.x534**2 + 406.8*m.x534) + m.x574 >= 0.05711)

m.c1063 = Constraint(expr=-0.0001*(22.83*m.x535**2 + 406.8*m.x535) + m.x575 >= 0.05711)

m.c1064 = Constraint(expr=-0.0001*(22.83*m.x536**2 + 406.8*m.x536) + m.x576 >= 0.05711)

m.c1065 = Constraint(expr=-0.0001*(22.83*m.x537**2 + 406.8*m.x537) + m.x577 >= 0.05711)

m.c1066 = Constraint(expr=-0.0001*(22.83*m.x538**2 + 406.8*m.x538) + m.x578 >= 0.05711)

m.c1067 = Constraint(expr=-0.0001*(22.83*m.x539**2 + 406.8*m.x539) + m.x579 >= 0.05711)

m.c1068 = Constraint(expr=-0.0001*(22.83*m.x540**2 + 406.8*m.x540) + m.x580 >= 0.05711)

m.c1069 = Constraint(expr= - 57.650802630846*m.b1 + m.x622 >= -41.3522129303489)

m.c1070 = Constraint(expr= - 57.650802630846*m.b2 + m.x623 >= -38.9160540345718)

m.c1071 = Constraint(expr= - 57.650802630846*m.b3 + m.x624 >= -4.93158880518534)

m.c1072 = Constraint(expr= - 57.650802630846*m.b4 + m.x625 >= 0)

m.c1073 = Constraint(expr= - 57.650802630846*m.b5 + m.x626 >= -41.3522129303489)

m.c1074 = Constraint(expr= - 57.650802630846*m.b6 + m.x627 >= -4.93158880518534)

m.c1075 = Constraint(expr= - 57.650802630846*m.b7 + m.x628 >= -4.93158880518534)

m.c1076 = Constraint(expr= - 57.650802630846*m.b8 + m.x629 >= -38.9160540345718)

m.c1077 = Constraint(expr= - 57.650802630846*m.b9 + m.x630 >= -4.93158880518534)

m.c1078 = Constraint(expr= - 57.650802630846*m.b10 + m.x631 >= 0)

m.c1079 = Constraint(expr= - 57.650802630846*m.b11 + m.x632 >= -41.3522129303489)

m.c1080 = Constraint(expr= - 57.650802630846*m.b12 + m.x633 >= -38.9160540345718)

m.c1081 = Constraint(expr= - 57.650802630846*m.b13 + m.x634 >= -38.9160540345718)

m.c1082 = Constraint(expr= - 57.650802630846*m.b14 + m.x635 >= -4.93158880518534)

m.c1083 = Constraint(expr= - 57.650802630846*m.b15 + m.x636 >= -4.93158880518534)

m.c1084 = Constraint(expr= - 57.650802630846*m.b16 + m.x637 >= 0)

m.c1085 = Constraint(expr= - 57.650802630846*m.b17 + m.x638 >= -41.3522129303489)

m.c1086 = Constraint(expr= - 57.650802630846*m.b18 + m.x639 >= -38.9160540345718)

m.c1087 = Constraint(expr= - 57.650802630846*m.b19 + m.x640 >= -4.93158880518534)

m.c1088 = Constraint(expr= - 57.650802630846*m.b20 + m.x641 >= 0)

m.c1089 = Constraint(expr=-1.2*(m.x561*m.x622 + m.x562*m.x623 + m.x563*m.x624 + m.x564*m.x625 + m.x565*m.x626 + m.x566*
                          m.x627 + m.x567*m.x628 + m.x568*m.x629 + m.x569*m.x630 + m.x570*m.x631 + m.x571*m.x632 + 
                          m.x572*m.x633 + m.x573*m.x634 + m.x574*m.x635 + m.x575*m.x636 + m.x576*m.x637 + m.x577*m.x638
                           + m.x578*m.x639 + m.x579*m.x640 + m.x580*m.x641) + m.x581 == 0)

m.c1090 = Constraint(expr= - 15*m.b1 - 0.06038*m.x541 + m.x582 >= -14.4693)

m.c1091 = Constraint(expr= - 15*m.b2 - 0.06038*m.x542 + m.x583 >= -14.4693)

m.c1092 = Constraint(expr= - 15*m.b3 - 0.06038*m.x543 + m.x584 >= -14.4693)

m.c1093 = Constraint(expr= - 15*m.b4 - 0.06038*m.x544 + m.x585 >= -14.4693)

m.c1094 = Constraint(expr= - 15*m.b5 - 0.06038*m.x545 + m.x586 >= -14.4693)

m.c1095 = Constraint(expr= - 15*m.b6 - 0.06038*m.x546 + m.x587 >= -14.4693)

m.c1096 = Constraint(expr= - 15*m.b7 - 0.06038*m.x547 + m.x588 >= -14.4693)

m.c1097 = Constraint(expr= - 15*m.b8 - 0.06038*m.x548 + m.x589 >= -14.4693)

m.c1098 = Constraint(expr= - 15*m.b9 - 0.06038*m.x549 + m.x590 >= -14.4693)

m.c1099 = Constraint(expr= - 15*m.b10 - 0.06038*m.x550 + m.x591 >= -14.4693)

m.c1100 = Constraint(expr= - 15*m.b11 - 0.06038*m.x551 + m.x592 >= -14.4693)

m.c1101 = Constraint(expr= - 15*m.b12 - 0.06038*m.x552 + m.x593 >= -14.4693)

m.c1102 = Constraint(expr= - 15*m.b13 - 0.06038*m.x553 + m.x594 >= -14.4693)

m.c1103 = Constraint(expr= - 15*m.b14 - 0.06038*m.x554 + m.x595 >= -14.4693)

m.c1104 = Constraint(expr= - 15*m.b15 - 0.06038*m.x555 + m.x596 >= -14.4693)

m.c1105 = Constraint(expr= - 15*m.b16 - 0.06038*m.x556 + m.x597 >= -14.4693)

m.c1106 = Constraint(expr= - 15*m.b17 - 0.06038*m.x557 + m.x598 >= -14.4693)

m.c1107 = Constraint(expr= - 15*m.b18 - 0.06038*m.x558 + m.x599 >= -14.4693)

m.c1108 = Constraint(expr= - 15*m.b19 - 0.06038*m.x559 + m.x600 >= -14.4693)

m.c1109 = Constraint(expr= - 15*m.b20 - 0.06038*m.x560 + m.x601 >= -14.4693)

m.c1110 = Constraint(expr= - 4.22*m.x582 + m.x602 == 0)

m.c1111 = Constraint(expr= - 4.22*m.x583 + m.x603 == 0)

m.c1112 = Constraint(expr= - 4.22*m.x584 + m.x604 == 0)

m.c1113 = Constraint(expr= - 4.22*m.x585 + m.x605 == 0)

m.c1114 = Constraint(expr= - 4.22*m.x586 + m.x606 == 0)

m.c1115 = Constraint(expr= - 4.22*m.x587 + m.x607 == 0)

m.c1116 = Constraint(expr= - 4.22*m.x588 + m.x608 == 0)

m.c1117 = Constraint(expr= - 4.22*m.x589 + m.x609 == 0)

m.c1118 = Constraint(expr= - 4.22*m.x590 + m.x610 == 0)

m.c1119 = Constraint(expr= - 4.22*m.x591 + m.x611 == 0)

m.c1120 = Constraint(expr= - 4.22*m.x592 + m.x612 == 0)

m.c1121 = Constraint(expr= - 4.22*m.x593 + m.x613 == 0)

m.c1122 = Constraint(expr= - 4.22*m.x594 + m.x614 == 0)

m.c1123 = Constraint(expr= - 4.22*m.x595 + m.x615 == 0)

m.c1124 = Constraint(expr= - 4.22*m.x596 + m.x616 == 0)

m.c1125 = Constraint(expr= - 4.22*m.x597 + m.x617 == 0)

m.c1126 = Constraint(expr= - 4.22*m.x598 + m.x618 == 0)

m.c1127 = Constraint(expr= - 4.22*m.x599 + m.x619 == 0)

m.c1128 = Constraint(expr= - 4.22*m.x600 + m.x620 == 0)

m.c1129 = Constraint(expr= - 4.22*m.x601 + m.x621 == 0)
