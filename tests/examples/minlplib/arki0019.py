#  NLP written by GAMS Convert at 04/21/18 13:51:02
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          3        2        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        511      511        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1022      512      510        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=40)
m.x2 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x3 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x4 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x5 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x6 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x7 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x8 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x9 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x10 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x11 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x12 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x13 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x14 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x15 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x16 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x17 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x18 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x19 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x20 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x21 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x22 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x23 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x24 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x25 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x26 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x27 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x28 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x29 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x30 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x31 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x32 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x33 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x34 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x35 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x36 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x37 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x38 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x39 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x40 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x41 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x42 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x43 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x44 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x45 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x46 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x47 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x48 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x49 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x50 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x51 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x52 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x53 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x54 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x55 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x56 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x57 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x58 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x59 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x60 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x61 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x62 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x63 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x64 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x65 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x66 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x67 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x68 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x69 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x70 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x71 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x72 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x73 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x74 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x75 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x76 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x77 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x78 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x79 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x80 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x81 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x82 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x83 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x84 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x85 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x86 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x87 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x88 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x89 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x90 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x91 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x92 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x93 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x94 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x95 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x96 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x97 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x98 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x99 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x100 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x101 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x102 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x103 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x104 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x105 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x106 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x107 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x108 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x109 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x110 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x111 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x112 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x113 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x114 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x115 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x116 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x117 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x118 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x119 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x120 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x121 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x122 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x123 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x124 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x125 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x126 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x127 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x128 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x129 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x130 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x131 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x132 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x133 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x134 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x135 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x136 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x137 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x138 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x139 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x140 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x141 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x142 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x143 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x144 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x145 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x146 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x147 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x148 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x149 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x150 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x151 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x152 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x153 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x154 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x155 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x156 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x157 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x158 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x159 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x160 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x161 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x162 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x163 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x164 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x165 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x166 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x167 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x168 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x169 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x170 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x171 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x172 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x173 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x174 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x175 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x176 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x177 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x178 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x179 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x180 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x181 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x182 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x183 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x184 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x185 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x186 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x187 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x188 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x189 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x190 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x191 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x192 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x193 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x194 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x195 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x196 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x197 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x198 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x199 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x200 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x201 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x202 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x203 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x204 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x205 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x206 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x207 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x208 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x209 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x210 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x211 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x212 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x213 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x214 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x215 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x216 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x217 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x218 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x219 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x220 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x221 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x222 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x223 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x224 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x225 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x226 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x227 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x228 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x229 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x230 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x231 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x232 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x233 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x234 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x235 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x236 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x237 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x238 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x239 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x240 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x241 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x242 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x243 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x244 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x245 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x246 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x247 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x248 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x249 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x250 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x251 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x252 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x253 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x254 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x255 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x256 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x257 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x258 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x259 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x260 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x261 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x262 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x263 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x264 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x265 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x266 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x267 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x268 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x269 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x270 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x271 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x272 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x273 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x274 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x275 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x276 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x277 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x278 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x279 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x280 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x281 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x282 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x283 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x284 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x285 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x286 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x287 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x288 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x289 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x290 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x291 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x292 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x293 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x294 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x295 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x296 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x297 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x298 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x299 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x300 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x301 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x302 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x303 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x304 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x305 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x306 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x307 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x308 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x309 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x310 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x311 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x312 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x313 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x314 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x315 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x316 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x317 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x318 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x319 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x320 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x321 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x322 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x323 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x324 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x325 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x326 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x327 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x328 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x329 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x330 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x331 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x332 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x333 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x334 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x335 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x336 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x337 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x338 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x339 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x340 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x341 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x342 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x343 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x344 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x345 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x346 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x347 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x348 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x349 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x350 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x351 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x352 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x353 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x354 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x355 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x356 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x357 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x358 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x359 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x360 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x361 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x362 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x363 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x364 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x365 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x366 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x367 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x368 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x369 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x370 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x371 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x372 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x373 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x374 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x375 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x376 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x377 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x378 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x379 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x380 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x381 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x382 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x383 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x384 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x385 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x386 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x387 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x388 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x389 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x390 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x391 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x392 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x393 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x394 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x395 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x396 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x397 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x398 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x399 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x400 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x401 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x402 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x403 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x404 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x405 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x406 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x407 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x408 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x409 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x410 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x411 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x412 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x413 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x414 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x415 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x416 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x417 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x418 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x419 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x420 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x421 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x422 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x423 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x424 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x425 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x426 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x427 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x428 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x429 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x430 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x431 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x432 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x433 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x434 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x435 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x436 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x437 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x438 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x439 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x440 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x441 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x442 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x443 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x444 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x445 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x446 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x447 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x448 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x449 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x450 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x451 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x452 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x453 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x454 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x455 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x456 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x457 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x458 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x459 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x460 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x461 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x462 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x463 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x464 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x465 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x466 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x467 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x468 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x469 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x470 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x471 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x472 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x473 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x474 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x475 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x476 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x477 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x478 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x479 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x480 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x481 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x482 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x483 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x484 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x485 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x486 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x487 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x488 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x489 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x490 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x491 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x492 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x493 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x494 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x495 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x496 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x497 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x498 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x499 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x500 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x501 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x502 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x503 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x504 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x505 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x506 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x507 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x508 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x509 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)
m.x510 = Var(within=Reals,bounds=(5E-5,None),initialize=0.05)

m.obj = Objective(expr=-1000*(5.1896555300528e-7*log(100 + 0.77*m.x2*(3115.6025 + m.x1)/(0.000697151847870123 + m.x2) - 
                       m.x1) + 2.38853851131484e-6*log(100 + 0.77*m.x3*(3115.6025 + m.x1)/(0.00441135490801732 + m.x3)
                        - m.x1) + 1.75006368705556e-6*log(100 + 0.77*m.x4*(3115.6025 + m.x1)/(0.000853304974954616 + 
                       m.x4) - m.x1) + 5.4205853966032e-7*log(116.725409814076 - 0.994631725384071*m.x1) + 
                       1.28420497011416e-6*log(100 + 0.77*m.x5*(3115.6025 + m.x1)/(0.00111268459826716 + m.x5) - m.x1)
                        + 1.13642040985436e-6*log(100 + 0.77*m.x6*(3115.6025 + m.x1)/(0.000326187439886633 + m.x6) - 
                       m.x1) + 8.3264643528916e-7*log(100 + 0.77*m.x7*(3115.6025 + m.x1)/(0.00019264225638747 + m.x7) - 
                       m.x1) + 2.5790096715064e-7*log(273.722164695496 - 0.944241229522862*m.x1) + 6.1099986822816e-7*
                       log(100 + 0.77*m.x8*(3115.6025 + m.x1)/(0.000292444426062126 + m.x8) - m.x1) + 7.2368781007106e-6
                       *log(100 + 0.77*m.x9*(3115.6025 + m.x1)/(0.000340072769701281 + m.x9) - m.x1) + 
                       2.24152501608832e-6*log(122.167672752509 - 0.992884948335833*m.x1) + 5.31045518239344e-6*log(100
                        + 0.77*m.x10*(3115.6025 + m.x1)/(0.000928640395934794 + m.x10) - m.x1) + 1.40112029745028e-6*
                       log(100 + 0.77*m.x11*(3115.6025 + m.x1)/(0.000520524158336466 + m.x11) - m.x1) + 
                       3.31943054456628e-6*log(100 + 0.77*m.x12*(3115.6025 + m.x1)/(0.000148520174019557 + m.x12) - m.x1
                       ) + 6.4780110964124e-7*log(100 + 0.77*m.x13*(3115.6025 + m.x1)/(0.00104750410938401 + m.x13) - 
                       m.x1) + 9.559575451052e-8*log(369.775187215178 - 0.913411551308237*m.x1) + 7.004225000328e-8*log(
                       463.468636910111 - 0.883339213872723*m.x1) + 2.169464931432e-8*log(448.707925466966 - 
                       0.88807688867018*m.x1) + 5.139736486672e-8*log(809.359927930429 - 0.772320144199901*m.x1) + 
                       5.8738086293776e-7*log(100 + 0.77*m.x14*(3115.6025 + m.x1)/(0.000494204879879725 + m.x14) - m.x1)
                        + 1.8193327718832e-7*log(147.784367425591 - 0.984662880638467*m.x1) + 4.3102285130624e-7*log(100
                        + 0.77*m.x15*(3115.6025 + m.x1)/(0.000378101608644323 + m.x15) - m.x1) + 1.152774843986e-7*log(
                       439.112527740056 - 0.891156677483711*m.x1) + 2.7310693619852e-7*log(100 + 0.77*m.x16*(3115.6025
                        + m.x1)/(7.68864972863027e-5 + m.x16) - m.x1) + 5.447264353996e-8*log(642.105475210568 - 
                       0.826003004166749*m.x1) + 2.4063538402192e-7*log(100 + 0.77*m.x17*(3115.6025 + m.x1)/(
                       0.000285184441727289 + m.x17) - m.x1) + 7.453356083372e-8*log(493.516505615775 - 
                       0.873694893486645*m.x1) + 1.7657938873836e-7*log(100 + 0.77*m.x18*(3115.6025 + m.x1)/(
                       0.000288214605454492 + m.x18) - m.x1) + 4.7303472465e-8*log(440.16955630314 - 0.890817408092611*
                       m.x1) + 1.120678412982e-7*log(295.420037315374 - 0.937276967355311*m.x1) + 2.2412317111e-8*log(
                       573.716341402481 - 0.847953536626549*m.x1) + 6.7932840206568e-7*log(100 + 0.77*m.x19*(3115.6025
                        + m.x1)/(0.000204377628677949 + m.x19) - m.x1) + 1.60941456154132e-6*log(100 + 0.77*m.x20*(
                       3115.6025 + m.x1)/(6.19657352352374e-5 + m.x20) - m.x1) + 3.1708525773332e-7*log(100 + 0.77*m.x21
                       *(3115.6025 + m.x1)/(0.000484370227279492 + m.x21) - m.x1) + 1.7433187894212e-7*log(100 + 0.77*
                       m.x22*(3115.6025 + m.x1)/(2.04333582846966e-5 + m.x22) - m.x1) + 4.3774137231148e-7*log(
                       119.000522100771 - 0.993901493499004*m.x1) + 2.01470428953719e-6*log(103.022920309924 - 
                       0.999029747758283*m.x1) + 1.47615824512421e-6*log(115.545995934311 - 0.99501027620362*m.x1) + 
                       4.5722003637812e-7*log(101.873352153701 - 0.99939871913901*m.x1) + 1.08321186770806e-6*log(
                       111.940081528697 - 0.996167649265689*m.x1) + 9.5855732013751e-7*log(140.246799210435 - 
                       0.987082177777674*m.x1) + 7.0232752660181e-7*log(167.363613619287 - 0.978378623839438*m.x1) + 
                       2.1753644847374e-7*log(120.667450462708 - 0.993366467492979*m.x1) + 5.1537124044456e-7*log(
                       144.803854659423 - 0.985619521534142*m.x1) + 6.10422200994085e-6*log(100 + 0.77*m.x23*(3115.6025
                        + m.x1)/(0.00305512052568459 + m.x23) - m.x1) + 1.89070012630112e-6*log(102.487967250958 - 
                       0.999201449077359*m.x1) + 4.47930681656604e-6*log(100 + 0.77*m.x24*(3115.6025 + m.x1)/(
                       0.0083426507129411 + m.x24) - m.x1) + 1.18182857846273e-6*log(125.379696264084 - 
                       0.991854000545935*m.x1) + 2.79990082859373e-6*log(100 + 0.77*m.x25*(3115.6025 + m.x1)/(
                       0.00133426452380755 + m.x25) - m.x1) + 5.4641265701959e-7*log(112.679121242756 - 
                       0.995930443231203*m.x1) + 8.063390050507e-8*log(133.363509020125 - 0.989291474435482*m.x1) + 
                       5.907981841698e-8*log(146.753601064768 - 0.984993720776393*m.x1) + 1.829918287962e-8*log(
                       144.573259758642 - 0.985693534474105*m.x1) + 4.335307594052e-8*log(207.104998133011 - 
                       0.965623022149645*m.x1) + 4.9544888581316e-7*log(126.716260334795 - 0.991425009982886*m.x1) + 
                       1.5345859077612e-7*log(105.414841252999 - 0.998262024358692*m.x1) + 3.6356273231584e-7*log(
                       134.800988433026 - 0.988830093558782*m.x1) + 9.723520939885e-8*log(143.170525043829 - 
                       0.986143763511607*m.x1) + 2.3036250546307e-7*log(261.936397566447 - 0.948024050704014*m.x1) + 
                       4.594703752211e-8*log(175.505916825191 - 0.975765227809006*m.x1) + 2.0297313110372e-7*log(
                       145.922600022893 - 0.985260443197458*m.x1) + 6.286818655627e-8*log(151.27829160512 - 
                       0.983541452542447*m.x1) + 1.4894264850651e-7*log(145.448936430143 - 0.985412472730349*m.x1) + 
                       3.989992559625e-8*log(143.324491011074 - 0.986094345793125*m.x1) + 9.452791299495e-8*log(
                       123.450262944899 - 0.992473281509788*m.x1) + 1.890452726975e-8*log(163.953187166908 - 
                       0.979473252070215*m.x1) + 5.7300555932538e-7*log(163.598133703279 - 0.979587211878512*m.x1) + 
                       1.35752235328037e-6*log(100 + 0.77*m.x26*(3115.6025 + m.x1)/(0.000556683176287833 + m.x26) - m.x1
                       ) + 2.6745770515237e-7*log(127.252545117543 - 0.991252881226812*m.x1) + 1.4704690028817e-7*log(
                       100 + 0.77*m.x27*(3115.6025 + m.x1)/(0.000183567688642283 + m.x27) - m.x1) + 8.573813856476e-8*
                       log(175.098075010055 - 0.975896130841449*m.x1) + 3.9460970899603e-7*log(112.189454534394 - 
                       0.996087609207402*m.x1) + 2.8912748067577e-7*log(161.708775393222 - 0.980193630158783*m.x1) + 
                       8.955332375044e-8*log(107.565006489971 - 0.997571896129249*m.x1) + 2.1216310607822e-7*log(
                       147.609223184625 - 0.984719095845948*m.x1) + 1.8774766456787e-7*log(254.987449685228 - 
                       0.950254421196148*m.x1) + 1.3756126014697e-7*log(351.179935246506 - 0.919379980197568*m.x1) + 
                       4.260773904838e-8*log(181.517913158427 - 0.973835586164016*m.x1) + 1.0094309932872e-7*log(
                       271.59122797394 - 0.944925186067883*m.x1) + 1.19560239361145e-6*log(249.052415932832 - 
                       0.952159360530481*m.x1) + 3.7032165490144e-7*log(110.039136596835 - 0.99677778644842*m.x1) + 
                       8.7733865886348e-7*log(156.821256781618 - 0.981762353579567*m.x1) + 2.3147865116101e-7*log(
                       199.523689768056 - 0.968056358355068*m.x1) + 5.4840209400801e-7*log(415.971843439801 - 
                       0.898584032000295*m.x1) + 1.0702302104483e-7*log(150.509314160132 - 0.983788267546925*m.x1) + 
                       1.579334504759e-8*log(229.558267186124 - 0.958416304009859*m.x1) + 1.157165846826e-8*log(
                       278.639758958691 - 0.942662852864352*m.x1) + 3.58416630594e-9*log(270.755418624658 - 
                       0.945193451788327*m.x1) + 8.49134275924e-9*log(481.615742418209 - 0.877514624404683*m.x1) + 
                       9.704101076692e-8*log(204.592823836379 - 0.966429342691701*m.x1) + 3.005714047644e-8*log(
                       121.768604799103 - 0.993013035263933*m.x1) + 7.120915200608e-8*log(234.90398420317 - 
                       0.956700514843222*m.x1) + 1.904495755745e-8*log(265.661094609679 - 0.946828552548126*m.x1) + 
                       4.511991249359e-8*log(643.645574905152 - 0.825508685750139*m.x1) + 8.99940859807e-9*log(
                       378.882844396923 - 0.910488310239537*m.x1) + 3.975529739764e-8*log(275.639640374999 - 
                       0.943625786545299*m.x1) + 1.231366654199e-8*log(294.870657652889 - 0.937453299112166*m.x1) + 
                       2.917262622087e-8*log(273.926918368189 - 0.944175510718011*m.x1) + 7.81499206125e-9*log(
                       266.221094994647 - 0.946648811908885*m.x1) + 1.851469341315e-8*log(192.176519000713 - 
                       0.970414544538107*m.x1) + 3.70273198075e-9*log(339.418986006275 - 0.923154835699909*m.x1) + 
                       1.1223163527906e-7*log(338.189154866992 - 0.923549568705574*m.x1) + 2.6589088213369e-7*log(
                       739.647257673155 - 0.794695485809517*m.x1) + 5.238555739769e-8*log(206.622092527959 - 
                       0.965778018046924*m.x1) + 2.880131582229e-8*log(1358.00873885992 - 0.596222965265974*m.x1) + 
                       8.2928697456672e-7*log(117.708072269849 - 0.994316324925966*m.x1) + 3.81679258712616e-6*log(
                       102.816009888922 - 0.999096158804301*m.x1) + 2.79653439796344e-6*log(114.487098874626 - 
                       0.995350145317118*m.x1) + 8.6618867820768e-7*log(101.745069142043 - 0.999439893522347*m.x1) + 
                       2.05211010291984e-6*log(111.125650567867 - 0.996429053267268*m.x1) + 1.81595606503464e-6*log(100
                        + 0.77*m.x28*(3115.6025 + m.x1)/(0.00314596400504048 + m.x28) - m.x1) + 1.33053694836984e-6*log(
                       100 + 0.77*m.x29*(3115.6025 + m.x1)/(0.00185796732288463 + m.x29) - m.x1) + 4.1211581683536e-7*
                       log(119.262530850324 - 0.99381739780658*m.x1) + 9.7635426715584e-7*log(141.787032240127 - 
                       0.986587816565134*m.x1) + 1.15642525996044e-5*log(100 + 0.77*m.x30*(3115.6025 + m.x1)/(
                       0.00327988316455864 + m.x30) - m.x1) + 3.58187068147968e-6*log(102.317637448576 - 
                       0.999256119017565*m.x1) + 8.48590293956256e-6*log(100 + 0.77*m.x31*(3115.6025 + m.x1)/(
                       0.00895641248557199 + m.x31) - m.x1) + 2.23893629499672e-6*log(100 + 0.77*m.x32*(3115.6025 + m.x1
                       )/(0.00502027382308052 + m.x32) - m.x1) + 5.30432221878072e-6*log(100 + 0.77*m.x33*(3115.6025 + 
                       m.x1)/(0.00143242523884508 + m.x33) - m.x1) + 1.03516123415976e-6*log(111.814530003852 - 
                       0.996207946936796*m.x1) + 1.5275833546248e-7*log(131.106832242588 - 0.990015789163544*m.x1) + 
                       1.1192481901872e-7*log(143.607926262619 - 0.986003372939064*m.x1) + 3.466721440368e-8*log(
                       141.571690034213 - 0.986656933920738*m.x1) + 8.213101036128e-8*log(200.071509157679 - 
                       0.967880527391514*m.x1) + 9.3861200598624e-7*log(124.904463963847 - 0.992006533579349*m.x1) + 
                       2.9072237287968e-7*log(105.044555247892 - 0.998380873282811*m.x1) + 6.8875792286976e-7*log(
                       132.448415533481 - 0.989585187605453*m.x1) + 1.842089821164e-7*log(140.261800370076 - 
                       0.987077362927371*m.x1) + 4.3641436997448e-7*log(100 + 0.77*m.x34*(3115.6025 + m.x1)/(
                       0.000741543429815745 + m.x34) - m.x1) + 8.704518728904e-8*log(170.483695524706 - 
                       0.977377186106153*m.x1) + 3.8452607968608e-7*log(142.831818536397 - 0.986252476515731*m.x1) + 
                       1.1910176081928e-7*log(147.834377406707 - 0.984646829174548*m.x1) + 2.8216706525064e-7*log(
                       142.389460178795 - 0.986394458157356*m.x1) + 7.558912791e-8*log(140.405570410136 - 
                       0.987031217746765*m.x1) + 1.790800960068e-7*log(121.857913496112 - 0.992984370279549*m.x1) + 
                       3.5814019914e-8*log(159.679650282215 - 0.980844908719192*m.x1) + 1.08554063371632e-6*log(100 + 
                       0.77*m.x35*(3115.6025 + m.x1)/(0.00197115089250469 + m.x35) - m.x1) + 2.57178251010168e-6*log(100
                        + 0.77*m.x36*(3115.6025 + m.x1)/(0.00059763788778525 + m.x36) - m.x1) + 5.0669003470968e-7*log(
                       125.40476939922 - 0.991845952941936*m.x1) + 2.7857563112088e-7*log(100 + 0.77*m.x37*(3115.6025 + 
                       m.x1)/(0.000197072608583864 + m.x37) - m.x1) + 1.29788901763516e-6*log(100 + 0.77*m.x38*(
                       3115.6025 + m.x1)/(0.00103350340834749 + m.x38) - m.x1) + 5.97353308727723e-6*log(100 + 0.77*
                       m.x39*(3115.6025 + m.x1)/(0.00653968048251619 + m.x39) - m.x1) + 4.37676147566657e-6*log(100 + 
                       0.77*m.x40*(3115.6025 + m.x1)/(0.00126499499738795 + m.x40) - m.x1) + 1.35564262688804e-6*log(
                       111.307816465541 - 0.996370584352291*m.x1) + 3.21168816976702e-6*log(100 + 0.77*m.x41*(3115.6025
                        + m.x1)/(0.00164951628291331 + m.x41) - m.x1) + 2.84209146604267e-6*log(100 + 0.77*m.x42*(
                       3115.6025 + m.x1)/(0.000483561553932482 + m.x42) - m.x1) + 2.08237841158577e-6*log(100 + 0.77*
                       m.x43*(3115.6025 + m.x1)/(0.000285585456276797 + m.x43) - m.x1) + 6.4498853722358e-7*log(100 + 
                       0.77*m.x44*(3115.6025 + m.x1)/(0.000949480964356804 + m.x44) - m.x1) + 1.52805906703752e-6*log(
                       100 + 0.77*m.x45*(3115.6025 + m.x1)/(0.00043353870754387 + m.x45) - m.x1) + 1.80988209226695e-5*
                       log(100 + 0.77*m.x46*(3115.6025 + m.x1)/(0.000504146073263974 + m.x46) - m.x1) + 
                       5.60586475207904e-6*log(100 + 0.77*m.x47*(3115.6025 + m.x1)/(0.00794759125316883 + m.x47) - m.x1)
                        + 1.32809999044427e-5*log(100 + 0.77*m.x48*(3115.6025 + m.x1)/(0.00137667714323634 + m.x48) - 
                       m.x1) + 3.50408352908141e-6*log(100 + 0.77*m.x49*(3115.6025 + m.x1)/(0.00077165899138256 + m.x49)
                        - m.x1) + 8.30161544180841e-6*log(100 + 0.77*m.x50*(3115.6025 + m.x1)/(0.00022017600114885 + 
                       m.x50) - m.x1) + 1.62009586367803e-6*log(100 + 0.77*m.x51*(3115.6025 + m.x1)/(0.00155288847130484
                        + m.x51) - m.x1) + 2.3907690827119e-7*log(288.890309631698 - 0.939372782750143*m.x1) + 
                       1.7516975167866e-7*log(357.894740601638 - 0.917224761309686*m.x1) + 5.425648566354e-8*log(
                       346.901414191408 - 0.920753236591829*m.x1) + 1.2854046864884e-7*log(100 + 0.77*m.x52*(3115.6025
                        + m.x1)/(0.000176557293751724 + m.x52) - m.x1) + 1.46898992960372e-6*log(100 + 0.77*m.x53*(
                       3115.6025 + m.x1)/(0.000732641574913837 + m.x53) - m.x1) + 4.5499976065404e-7*log(
                       132.443353443726 - 0.989586812360137*m.x1) + 1.07795174808928e-6*log(100 + 0.77*m.x54*(3115.6025
                        + m.x1)/(0.000560522506580771 + m.x54) - m.x1) + 2.8829925245545e-7*log(100 + 0.77*m.x55*(
                       3115.6025 + m.x1)/(0.000450253536640847 + m.x55) - m.x1) + 6.8301738155719e-7*log(100 + 0.77*
                       m.x56*(3115.6025 + m.x1)/(0.00011398156261661 + m.x56) - m.x1) + 1.3623148088087e-7*log(100 + 
                       0.77*m.x57*(3115.6025 + m.x1)/(0.000253899142154748 + m.x57) - m.x1) + 6.0180877202324e-7*log(100
                        + 0.77*m.x58*(3115.6025 + m.x1)/(0.000422776032844626 + m.x58) - m.x1) + 1.8640214074159e-7*log(
                       100 + 0.77*m.x59*(3115.6025 + m.x1)/(0.00037775801625084 + m.x59) - m.x1) + 4.4161013781567e-7*
                       log(100 + 0.77*m.x60*(3115.6025 + m.x1)/(0.000427268145358538 + m.x60) - m.x1) + 
                       1.1830198951125e-7*log(340.563369854733 - 0.922787528301594*m.x1) + 2.8027220613915e-7*log(
                       235.410795115064 - 0.956537846174195*m.x1) + 5.605131221075e-8*log(441.491937984964 - 
                       0.890392969582941*m.x1) + 1.69894295932146e-6*log(100 + 0.77*m.x61*(3115.6025 + m.x1)/(
                       0.000302982738228342 + m.x61) - m.x1) + 4.02500989160129e-6*log(100 + 0.77*m.x62*(3115.6025 + 
                       m.x1)/(9.1862050946334e-5 + m.x62) - m.x1) + 7.9300344942529e-7*log(100 + 0.77*m.x63*(3115.6025
                        + m.x1)/(0.000718062043907347 + m.x63) - m.x1) + 4.3598930563389e-7*log(100 + 0.77*m.x64*(
                       3115.6025 + m.x1)/(3.02917441813244e-5 + m.x64) - m.x1) + 2.386749707546e-7*log(100 + 0.77*m.x65*
                       (3115.6025 + m.x1)/(0.000480318835957082 + m.x65) - m.x1) + 1.09850134760005e-6*log(
                       138.827733020974 - 0.98753764865031*m.x1) + 8.0486343825295e-7*log(100 + 0.77*m.x66*(3115.6025 + 
                       m.x1)/(0.000587904132419288 + m.x66) - m.x1) + 2.492955560374e-7*log(124.199690905835 - 
                       0.992232741209498*m.x1) + 5.906125790237e-7*log(100 + 0.77*m.x67*(3115.6025 + m.x1)/(
                       0.000766609702979113 + m.x67) - m.x1) + 5.2264568720645e-7*log(100 + 0.77*m.x68*(3115.6025 + m.x1
                       )/(0.000224734355806163 + m.x68) - m.x1) + 3.8293844830495e-7*log(100 + 0.77*m.x69*(3115.6025 + 
                       m.x1)/(0.000132725323223145 + m.x69) - m.x1) + 1.186100029873e-7*log(344.164724732999 - 
                       0.921631618689162*m.x1) + 2.810020334412e-7*log(100 + 0.77*m.x70*(3115.6025 + m.x1)/(
                       0.000201486328606083 + m.x70) - m.x1) + 3.32827806978575e-6*log(100 + 0.77*m.x71*(3115.6025 + 
                       m.x1)/(0.00023430097385907 + m.x71) - m.x1) + 1.0308890726224e-6*log(132.041291503744 - 
                       0.989715860253757*m.x1) + 2.4423060991458e-6*log(100 + 0.77*m.x72*(3115.6025 + m.x1)/(
                       0.000639808207294919 + m.x72) - m.x1) + 6.4438254924835e-7*log(100 + 0.77*m.x73*(3115.6025 + m.x1
                       )/(0.000358627117726995 + m.x73) - m.x1) + 1.52662345999335e-6*log(100 + 0.77*m.x74*(3115.6025 + 
                       m.x1)/(0.000102326397497417 + m.x74) - m.x1) + 2.9792711674805e-7*log(255.436528988183 - 
                       0.950110282364909*m.x1) + 4.396498723265e-8*log(472.644004866244 - 0.880394240001334*m.x1) + 
                       3.22127969271e-8*log(593.778869946635 - 0.841514163008075*m.x1) + 9.9774826299e-9*log(
                       574.960968571768 - 0.847554054610058*m.x1) + 2.36379167854e-8*log(1008.34110667307 - 
                       0.708454109061388*m.x1) + 2.701395294382e-7*log(100 + 0.77*m.x75*(3115.6025 + m.x1)/(
                       0.000340493844136466 + m.x75) - m.x1) + 8.36720652474e-8*log(168.737850847238 - 0.977937541503694
                       *m.x1) + 1.982296625168e-7*log(100 + 0.77*m.x76*(3115.6025 + m.x1)/(0.000260501819069085 + m.x76)
                        - m.x1) + 5.301671769575e-8*log(562.675437637781 - 0.851497282584097*m.x1) + 1.2560330764265e-7*
                       log(100 + 0.77*m.x77*(3115.6025 + m.x1)/(5.29727246513075e-5 + m.x77) - m.x1) + 2.505225352345e-8
                       *log(813.995783375217 - 0.770832195899439*m.x1) + 1.106694710494e-7*log(100 + 0.77*m.x78*(
                       3115.6025 + m.x1)/(0.000196484395045369 + m.x78) - m.x1) + 3.427837425665e-8*log(631.785089268111
                        - 0.829315488972643*m.x1) + 8.120978396145e-8*log(582.55897619313 - 0.845115358524353*m.x1) + 
                       2.175511426875e-8*log(564.030854811577 - 0.851062240830922*m.x1) + 5.154058605525e-8*log(
                       373.579196696883 - 0.91219059661915*m.x1) + 1.030754180125e-8*log(731.294065299251 - 
                       0.797376569925319*m.x1) + 3.124266833451e-7*log(100 + 0.77*m.x79*(3115.6025 + m.x1)/(
                       0.000140810678480119 + m.x79) - m.x1) + 7.4017817017615e-7*log(100 + 0.77*m.x80*(3115.6025 + m.x1
                       )/(4.26927216908973e-5 + m.x80) - m.x1) + 1.4582916761615e-7*log(412.601143991731 - 
                       0.899665909244927*m.x1) + 8.017614245715e-8*log(100 + 0.77*m.x81*(3115.6025 + m.x1)/(
                       1.40780332089543e-5 + m.x81) - m.x1) + 4.674802317404e-8*log(390.022082245375 - 0.906913002462485
                       *m.x1) + 2.1515773644787e-7*log(151.027826575194 - 0.983621843102516*m.x1) + 1.5764440881433e-7*
                       log(342.309228866923 - 0.922227168303106*m.x1) + 4.882822188676e-8*log(131.865551273648 - 
                       0.989772266753012*m.x1) + 1.1568020913038e-7*log(290.304903067674 - 0.938918747475753*m.x1) + 
                       1.0236788809523e-7*log(644.934834943347 - 0.825094878135658*m.x1) + 7.500415899913e-8*log(
                       897.171525613417 - 0.744135676610409*m.x1) + 2.323152340102e-8*log(412.345505235737 - 
                       0.899747960391052*m.x1) + 5.503840444488e-8*log(692.287531223752 - 0.80989631019241*m.x1) + 
                       6.5189248727705e-7*log(627.577976915564 - 0.830665825657938*m.x1) + 2.0191487236576e-7*log(
                       142.147090668079 - 0.986472250337429*m.x1) + 4.7836177274892e-7*log(324.491484308978 - 
                       0.927946044365744*m.x1) + 1.2621185309029e-7*log(473.12785885208 - 0.880238939706821*m.x1) + 
                       2.9901178435329e-7*log(1041.09237573213 - 0.697942091222442*m.x1) + 5.835343234307e-8*log(
                       301.153639757546 - 0.935436680463074*m.x1) + 8.61119301911e-9*log(568.894701148243 - 
                       0.849501115386753*m.x1) + 6.30935272554e-9*log(711.870091064714 - 0.803610989827902*m.x1) + 
                       1.95423754626e-9*log(689.945276050275 - 0.810648092608003*m.x1) + 4.62983562196e-9*log(
                       1169.90196090969 - 0.656598696107834*m.x1) + 5.291082237268e-8*log(489.770582229685 - 
                       0.874897204560054*m.x1) + 1.638841154076e-8*log(189.977742290068 - 0.971120275359239*m.x1) + 
                       3.882621134432e-8*log(585.248078101017 - 0.844252250375002*m.x1) + 1.038410831105e-8*log(
                       675.57524783692 - 0.815260371681907*m.x1) + 2.460126555311e-8*log(1431.31698254577 - 
                       0.572693569688118*m.x1) + 4.90685439103e-9*log(960.954196259431 - 0.723663658550977*m.x1) + 
                       2.167625277556e-8*log(703.571997904625 - 0.80627438901316*m.x1) + 6.71392659671e-9*log(
                       755.836939027607 - 0.789499161389296*m.x1) + 1.590613733223e-8*log(698.810231655749 - 
                       0.807802750300865*m.x1) + 4.26106090125e-9*log(677.162823229841 - 0.814750815217974*m.x1) + 
                       1.009498609635e-8*log(448.644758163218 - 0.888097163176876*m.x1) + 2.01888451675e-9*log(
                       868.998821335345 - 0.753178134458634*m.x1) + 6.119338691874e-8*log(866.013581015413 - 
                       0.754136292734579*m.x1) + 1.4497484232601e-7*log(1557.17087140146 - 0.532298850254018*m.x1) + 
                       2.856279938201e-8*log(496.376909904565 - 0.872776803233222*m.x1) + 1.570368335541e-8*log(
                       2077.53138725867 - 0.365281229791454*m.x1) + 4.5216208910888e-7*log(100 + 0.77*m.x82*(3115.6025
                        + m.x1)/(0.000609790965265749 + m.x82) - m.x1) + 2.08107562619314e-6*log(100 + 0.77*m.x83*(
                       3115.6025 + m.x1)/(0.0038585630601252 + m.x83) - m.x1) + 1.52478800997526e-6*log(100 + 0.77*m.x84
                       *(3115.6025 + m.x1)/(0.000746376368266585 + m.x84) - m.x1) + 4.7228244782872e-7*log(
                       119.10247354294 - 0.993868770633308*m.x1) + 1.11889661802836e-6*log(100 + 0.77*m.x85*(3115.6025
                        + m.x1)/(0.000973252839086021 + m.x85) - m.x1) + 9.9013551795506e-7*log(100 + 0.77*m.x86*(
                       3115.6025 + m.x1)/(0.00028531252471569 + m.x86) - m.x1) + 7.2546462764086e-7*log(100 + 0.77*m.x87
                       *(3115.6025 + m.x1)/(0.000168502038447399 + m.x87) - m.x1) + 2.2470285246244e-7*log(
                       296.570952433757 - 0.936907563646596*m.x1) + 5.3234935394736e-7*log(100 + 0.77*m.x88*(3115.6025
                        + m.x1)/(0.000255797885926617 + m.x88) - m.x1) + 6.3053162231951e-6*log(100 + 0.77*m.x89*(
                       3115.6025 + m.x1)/(0.000297457868225251 + m.x89) - m.x1) + 1.95298633636672e-6*log(
                       125.309989139262 - 0.991876374107653*m.x1) + 4.62687069591624e-6*log(100 + 0.77*m.x90*(3115.6025
                        + m.x1)/(0.000812271422864163 + m.x90) - m.x1) + 1.22076210476638e-6*log(100 + 0.77*m.x91*(
                       3115.6025 + m.x1)/(0.000455296690277536 + m.x91) - m.x1) + 2.89213925855238e-6*log(100 + 0.77*
                       m.x92*(3115.6025 + m.x1)/(0.000129908943874298 + m.x92) - m.x1) + 5.6441338228754e-7*log(100 + 
                       0.77*m.x93*(3115.6025 + m.x1)/(0.000916240190616427 + m.x93) - m.x1) + 8.329026044042e-8*log(
                       403.534122457219 - 0.902576107684719*m.x1) + 6.102611224188e-8*log(506.712574347542 - 
                       0.869459414560252*m.x1) + 1.890202133772e-8*log(490.532628751666 - 0.874652614140711*m.x1) + 
                       4.478127640312e-8*log(878.027135329109 - 0.750280359792654*m.x1) + 5.1177068795896e-7*log(100 + 
                       0.77*m.x94*(3115.6025 + m.x1)/(0.000432275510222909 + m.x94) - m.x1) + 1.5851404821672e-7*log(
                       154.474683040325 - 0.982515522105171*m.x1) + 3.7553974781504e-7*log(100 + 0.77*m.x95*(3115.6025
                        + m.x1)/(0.000330721270564153 + m.x95) - m.x1) + 1.004384739431e-7*log(479.999644229205 - 
                       0.878033335693753*m.x1) + 2.3795144418842e-7*log(100 + 0.77*m.x96*(3115.6025 + m.x1)/(
                       6.72517637862611e-5 + m.x96) - m.x1) + 4.746069206266e-8*log(700.334669156876 - 0.807313458903414
                       *m.x1) + 2.0965976898232e-7*log(100 + 0.77*m.x97*(3115.6025 + m.x1)/(0.000249447658398885 + m.x97
                       ) - m.x1) + 6.493928234762e-8*log(539.563417544517 - 0.858915436887563*m.x1) + 1.5384933516906e-7
                       *log(100 + 0.77*m.x98*(3115.6025 + m.x1)/(0.000252098108899402 + m.x98) - m.x1) + 
                       4.12143673275e-8*log(481.160537164744 - 0.877660729452893*m.x1) + 9.76419898197e-8*log(
                       320.839421249599 - 0.929118229540001*m.x1) + 1.95273078685e-8*log(626.683196813309 - 
                       0.830953018938292*m.x1) + 5.9188234689228e-7*log(100 + 0.77*m.x99*(3115.6025 + m.x1)/(
                       0.000178766838029624 + m.x99) - m.x1) + 1.40224384099222e-6*log(100 + 0.77*m.x100*(3115.6025 + 
                       m.x1)/(5.42007392190642e-5 + m.x100) - m.x1) + 2.7626868822422e-7*log(100 + 0.77*m.x101*(
                       3115.6025 + m.x1)/(0.000423673249007549 + m.x101) - m.x1) + 1.5189113443902e-7*log(100 + 0.77*
                       m.x102*(3115.6025 + m.x1)/(1.78728311631289e-5 + m.x102) - m.x1) + 7.0766353293472e-7*log(100 + 
                       0.77*m.x103*(3115.6025 + m.x1)/(0.000276679422907153 + m.x103) - m.x1) + 3.25702080163016e-6*log(
                       100 + 0.77*m.x104*(3115.6025 + m.x1)/(0.00175073928860366 + m.x104) - m.x1) + 2.38639394169944e-6
                       *log(100 + 0.77*m.x105*(3115.6025 + m.x1)/(0.00033865208670899 + m.x105) - m.x1) + 
                       7.3915322319968e-7*log(141.701349131272 - 0.986615317861867*m.x1) + 1.75114710581584e-6*log(100
                        + 0.77*m.x106*(3115.6025 + m.x1)/(0.000441592363940183 + m.x106) - m.x1) + 1.54962748005064e-6*
                       log(100 + 0.77*m.x107*(3115.6025 + m.x1)/(0.000129454369092067 + m.x107) - m.x1) + 
                       1.13540005626584e-6*log(100 + 0.77*m.x108*(3115.6025 + m.x1)/(7.64541448002395e-5 + m.x108) - 
                       m.x1) + 3.5167480481936e-7*log(100 + 0.77*m.x109*(3115.6025 + m.x1)/(0.000254185756096936 + 
                       m.x109) - m.x1) + 8.3316189845184e-7*log(100 + 0.77*m.x110*(3115.6025 + m.x1)/(
                       0.000116062741972903 + m.x110) - m.x1) + 9.8682363299644e-6*log(100 + 0.77*m.x111*(3115.6025 + 
                       m.x1)/(0.000134965055252807 + m.x111) - m.x1) + 3.05655260327168e-6*log(100 + 0.77*m.x112*(
                       3115.6025 + m.x1)/(0.00212765138815038 + m.x112) - m.x1) + 7.24135822522656e-6*log(100 + 0.77*
                       m.x113*(3115.6025 + m.x1)/(0.000368550538337489 + m.x113) - m.x1) + 1.91057332036472e-6*log(100
                        + 0.77*m.x114*(3115.6025 + m.x1)/(0.000206580996920193 + m.x114) - m.x1) + 4.52638895374872e-6*
                       log(100 + 0.77*m.x115*(3115.6025 + m.x1)/(5.89433652988846e-5 + m.x115) - m.x1) + 
                       8.8334422050376e-7*log(100 + 0.77*m.x116*(3115.6025 + m.x1)/(0.000415724111415154 + m.x116) - 
                       m.x1) + 1.3035475857448e-7*log(100 + 0.77*m.x117*(3115.6025 + m.x1)/(0.000156618059539867 + 
                       m.x117) - m.x1) + 9.550989618672e-8*log(100 + 0.77*m.x118*(3115.6025 + m.x1)/(
                       0.000111130510572367 + m.x118) - m.x1) + 2.958291179568e-8*log(819.669890654164 - 
                       0.769011004884556*m.x1) + 7.008565519328e-8*log(100 + 0.77*m.x119*(3115.6025 + m.x1)/(
                       4.72661916261924e-5 + m.x119) - m.x1) + 8.0095492704224e-7*log(100 + 0.77*m.x120*(3115.6025 + 
                       m.x1)/(0.000196135635845714 + m.x120) - m.x1) + 2.4808495467168e-7*log(216.865217149611 - 
                       0.962490331436821*m.x1) + 5.8774450821376e-7*log(100 + 0.77*m.x121*(3115.6025 + m.x1)/(
                       0.000150057602514548 + m.x121) - m.x1) + 1.571928452764e-7*log(100 + 0.77*m.x122*(3115.6025 + 
                       m.x1)/(0.00012053747251679 + m.x122) - m.x1) + 3.7240972588648e-7*log(100 + 0.77*m.x123*(
                       3115.6025 + m.x1)/(3.05140289931351e-5 + m.x123) - m.x1) + 7.427911766504e-8*log(100 + 0.77*
                       m.x124*(3115.6025 + m.x1)/(6.79713947342661e-5 + m.x124) - m.x1) + 3.2813138563808e-7*log(100 + 
                       0.77*m.x125*(3115.6025 + m.x1)/(0.000113181463981294 + m.x125) - m.x1) + 1.0163426585128e-7*log(
                       100 + 0.77*m.x126*(3115.6025 + m.x1)/(0.000101129680938306 + m.x126) - m.x1) + 2.4078437066664e-7
                       *log(100 + 0.77*m.x127*(3115.6025 + m.x1)/(0.000114384048402347 + m.x127) - m.x1) + 
                       6.450320691e-8*log(100 + 0.77*m.x128*(3115.6025 + m.x1)/(0.000120101258419391 + m.x128) - m.x1)
                        + 1.528161629268e-7*log(100 + 0.77*m.x129*(3115.6025 + m.x1)/(0.000223759740569752 + m.x129) - 
                       m.x1) + 3.0561526514e-8*log(1018.11416141955 - 0.705317298525872*m.x1) + 9.2633496432432e-7*log(
                       100 + 0.77*m.x130*(3115.6025 + m.x1)/(8.11115749466991e-5 + m.x130) - m.x1) + 2.19460422369368e-6
                       *log(100 + 0.77*m.x131*(3115.6025 + m.x1)/(2.45924096985208e-5 + m.x131) - m.x1) + 
                       4.3237874350168e-7*log(100 + 0.77*m.x132*(3115.6025 + m.x1)/(0.000192232546419447 + m.x132) - 
                       m.x1) + 2.3771965719288e-7*log(100 + 0.77*m.x133*(3115.6025 + m.x1)/(8.10940944291689e-6 + m.x133
                       ) - m.x1) + 3.69643743012e-8*log(259.243438352797 - 0.948888396914306*m.x1) + 1.701285009261e-7*
                       log(126.655917760543 - 0.991444377849696*m.x1) + 1.246518363399e-7*log(231.702010264842 - 
                       0.957728237069767*m.x1) + 3.86092191228e-8*log(116.581295018683 - 0.994677981219144*m.x1) + 
                       9.14701041714e-8*log(202.310059251124 - 0.967162030698356*m.x1) + 8.09438490669e-8*log(
                       416.457222584263 - 0.898428242182928*m.x1) + 5.93069314839e-8*log(590.940569459868 - 
                       0.842425158710115*m.x1) + 1.83695195706e-8*log(272.323136981283 - 0.944690268742151*m.x1) + 
                       4.35197051064e-8*log(447.679121507101 - 0.888407098945677*m.x1) + 5.154613236615e-7*log(
                       405.179826008594 - 0.902047894104401*m.x1) + 1.596571664928e-7*log(121.977097201104 - 
                       0.992946116457056*m.x1) + 3.782479433076e-7*log(221.559135870346 - 0.960983746845002*m.x1) + 
                       9.97976355387e-8*log(308.580883515259 - 0.93305279363614*m.x1) + 2.364331744287e-7*log(
                       700.293486922057 - 0.80732667696792*m.x1) + 4.61409481821e-8*log(208.388630306009 - 
                       0.96521102088408*m.x1) + 6.8090015433e-9*log(367.695674982814 - 0.914079002381461*m.x1) + 
                       4.9889013462e-9*log(460.789282500999 - 0.884199193414115*m.x1) + 1.5452454078e-9*log(
                       446.118879639336 - 0.888907882299062*m.x1) + 3.6608815788e-9*log(805.013912804639 - 
                       0.773715063842503*m.x1) + 4.18373935404e-8*log(318.676489558247 - 0.929812455357111*m.x1) + 
                       1.29585667428e-8*log(147.377954877314 - 0.984793324925977*m.x1) + 3.07004769696e-8*log(
                       378.042793763629 - 0.910757937264581*m.x1) + 8.2108726815e-9*log(436.583029316824 - 
                       0.89196855846764*m.x1) + 1.94525955633e-8*log(1040.3513804883 - 0.698179924913946*m.x1) + 
                       3.8799245409e-9*log(638.457618384797 - 0.827173839286367*m.x1) + 1.71397433868e-8*log(
                       455.219495877816 - 0.885986901128171*m.x1) + 5.3088040713e-9*log(490.658159781153 - 
                       0.874612323047901*m.x1) + 1.25772251769e-8*log(452.032892933289 - 0.887009689800516*m.x1) + 
                       3.3692857875e-9*log(437.633465661542 - 0.89163140494927*m.x1) + 7.9822593405e-9*log(
                       293.861493987256 - 0.937777205536568*m.x1) + 1.5963627525e-9*log(570.412097376226 - 
                       0.849014083992991*m.x1) + 4.83865435422e-8*log(568.252989540977 - 0.849707082485337*m.x1) + 
                       1.146338170503e-7*log(1166.15178222077 - 0.657802372985397*m.x1) + 2.25850407303e-8*log(
                       322.704323762715 - 0.928519660719647*m.x1) + 1.24171417323e-8*log(1798.72481850053 - 
                       0.454768437725759*m.x1) + 3.5753099129492e-7*log(120.525902665119 - 0.993411899411071*m.x1) + 
                       1.64553607990201e-6*log(103.26736425089 - 0.998951289758276*m.x1) + 1.20567155418859e-6*log(
                       116.796000913132 - 0.99460906809738*m.x1) + 3.7344044494348e-7*log(102.024916542162 - 
                       0.99935007224376*m.x1) + 8.8472746087274e-7*log(112.901715639768 - 0.995858998174585*m.x1) + 
                       7.8291422871929e-7*log(143.446715021488 - 0.986055116138375*m.x1) + 5.7363519347899e-7*log(
                       172.653107945594 - 0.976680880200348*m.x1) + 1.7767573956946e-7*log(122.32539836666 - 
                       0.992834323901505*m.x1) + 4.2093620145624e-7*log(148.358661660843 - 0.984478552170618*m.x1) + 
                       4.98570316708715e-6*log(100 + 0.77*m.x134*(3115.6025 + m.x1)/(0.00282626697367363 + m.x134) - 
                       m.x1) + 1.54425405766048e-6*log(102.68920156283 - 0.99913685986488*m.x1) + 3.65853242974116e-6*
                       log(100 + 0.77*m.x135*(3115.6025 + m.x1)/(0.00771771783949399 + m.x135) - m.x1) + 
                       9.6527394924367e-7*log(127.411304883875 - 0.991201924865616*m.x1) + 2.28685562319267e-6*log(100
                        + 0.77*m.x136*(3115.6025 + m.x1)/(0.00123431718195035 + m.x136) - m.x1) + 4.4628968445161e-7*
                       log(113.699934767029 - 0.995602797607516*m.x1) + 6.585879289253e-8*log(136.024511029641 - 
                       0.988437385375817*m.x1) + 4.825421442942e-8*log(150.459788227524 - 0.983804163648115*m.x1) + 
                       1.494609696198e-8*log(148.110144892852 - 0.984558317406392*m.x1) + 3.540919181308e-8*log(
                       215.360654511061 - 0.9629732436949*m.x1) + 4.0466435773564e-7*log(128.853558453294 - 
                       0.990739011650782*m.x1) + 1.2533931118548e-7*log(105.852231884397 - 0.998121637184334*m.x1) + 
                       2.9694461685536e-7*log(137.574819672958 - 0.987939790241869*m.x1) + 7.941812906915e-8*log(
                       146.598306222914 - 0.985043565017388*m.x1) + 1.8815158937453e-7*log(274.097414622119 - 
                       0.944120787352649*m.x1) + 3.752784386269e-8*log(181.412433739765 - 0.973869441387415*m.x1) + 
                       1.6578095962588e-7*log(149.564301239472 - 0.984091583814215*m.x1) + 5.134841365733e-8*log(
                       155.334716319722 - 0.982239481345993*m.x1) + 1.2165085627029e-7*log(149.05385875812 - 
                       0.984255418090684*m.x1) + 3.258878610375e-8*log(146.764254564814 - 0.98499030137355*m.x1) + 
                       7.720690932105e-8*log(125.329071289493 - 0.991870249401362*m.x1) + 1.544051991025e-8*log(
                       168.982812305731 - 0.977858917398567*m.x1) + 4.6800978523302e-7*log(168.600655860411 - 
                       0.977981576320981*m.x1) + 1.10877413782123e-6*log(100 + 0.77*m.x137*(3115.6025 + m.x1)/(
                       0.000514983046565565 + m.x137) - m.x1) + 2.1844957890923e-7*log(129.432213686124 - 
                       0.990553283454444*m.x1) + 1.2010247911743e-7*log(100 + 0.77*m.x138*(3115.6025 + m.x1)/(
                       0.000169816965151329 + m.x138) - m.x1) + 5.595595833396e-7*log(100 + 0.77*m.x139*(3115.6025 + 
                       m.x1)/(0.000969631097815696 + m.x139) - m.x1) + 2.5753725010113e-6*log(119.392186516001 - 
                       0.993775782849063*m.x1) + 1.8869555057667e-6*log(100 + 0.77*m.x140*(3115.6025 + m.x1)/(
                       0.00118681610349971 + m.x140) - m.x1) + 5.844589276524e-7*log(112.048952823725 - 
                       0.996132705367991*m.x1) + 1.3846568309562e-6*log(100 + 0.77*m.x141*(3115.6025 + m.x1)/(
                       0.00154757330391728 + m.x141) - m.x1) + 1.2253124072577e-6*log(100 + 0.77*m.x142*(3115.6025 + 
                       m.x1)/(0.000453676607753738 + m.x142) - m.x1) + 8.977769135187e-7*log(100 + 0.77*m.x143*(
                       3115.6025 + m.x1)/(0.000267935777718076 + m.x143) - m.x1) + 2.780742515298e-7*log(
                       227.498426217162 - 0.959077441291961*m.x1) + 6.587929193112e-7*log(100 + 0.77*m.x144*(3115.6025
                        + m.x1)/(0.000406745260389136 + m.x144) - m.x1) + 7.8029543025795e-6*log(100 + 0.77*m.x145*(
                       3115.6025 + m.x1)/(0.000472988967941613 + m.x145) - m.x1) + 2.4168594558624e-6*log(
                       115.979755437715 - 0.994871054495008*m.x1) + 5.7258445613508e-6*log(100 + 0.77*m.x146*(3115.6025
                        + m.x1)/(0.00129159609823484 + m.x146) - m.x1) + 1.5107173979271e-6*log(100 + 0.77*m.x147*(
                       3115.6025 + m.x1)/(0.000723969121833849 + m.x147) - m.x1) + 3.5790798862971e-6*log(100 + 0.77*
                       m.x148*(3115.6025 + m.x1)/(0.00020656874083075 + m.x148) - m.x1) + 6.984727924593e-7*log(100 + 
                       0.77*m.x149*(3115.6025 + m.x1)/(0.0014569172593482 + m.x149) - m.x1) + 1.030733547789e-7*log(
                       300.294195813365 - 0.935712532066152*m.x1) + 7.55210283246e-8*log(372.950133675651 - 
                       0.912392503961705*m.x1) + 2.33916275574e-8*log(361.393387088831 - 0.916101817517212*m.x1) + 
                       5.54177207004e-8*log(656.239567646576 - 0.821466452268357*m.x1) + 6.333264106332e-7*log(100 + 
                       0.77*m.x150*(3115.6025 + m.x1)/(0.000687363049653602 + m.x150) - m.x1) + 1.961642891124e-7*log(
                       134.549709596937 - 0.988910745322313*m.x1) + 4.647379111968e-7*log(100 + 0.77*m.x151*(3115.6025
                        + m.x1)/(0.000525881239497159 + m.x151) - m.x1) + 1.242946102395e-7*log(353.903089657918 - 
                       0.918505942379389*m.x1) + 2.944696474389e-7*log(100 + 0.77*m.x152*(3115.6025 + m.x1)/(
                       0.000106937303542527 + m.x152) - m.x1) + 5.87335508997e-8*log(516.195273474239 - 
                       0.866415798076218*m.x1) + 2.594581363644e-7*log(100 + 0.77*m.x153*(3115.6025 + m.x1)/(
                       0.000396647737730021 + m.x153) - m.x1) + 8.03636542029e-8*log(396.605249264855 - 
                       0.904800034900198*m.x1) + 1.903916138877e-7*log(100 + 0.77*m.x154*(3115.6025 + m.x1)/(
                       0.000400862229867344 + m.x154) - m.x1) + 5.10035997375e-8*log(354.727360960765 - 
                       0.918241379970402*m.x1) + 1.208339054865e-7*log(243.796027825877 - 0.953846478225038*m.x1) + 
                       2.41654320825e-8*log(460.605646202893 - 0.88425813427647*m.x1) + 7.324661827926e-7*log(100 + 0.77
                       *m.x155*(3115.6025 + m.x1)/(0.000284257877346811 + m.x155) - m.x1) + 1.7353046580099e-6*log(100
                        + 0.77*m.x156*(3115.6025 + m.x1)/(8.61848162156681e-5 + m.x156) - m.x1) + 3.418879994499e-7*log(
                       100 + 0.77*m.x157*(3115.6025 + m.x1)/(0.000673684559054268 + m.x157) - m.x1) + 1.879683015159e-7*
                       log(100 + 0.77*m.x158*(3115.6025 + m.x1)/(2.84196616363883e-5 + m.x158) - m.x1) + 
                       4.074501436232e-8*log(249.07063798668 - 0.952153511885204*m.x1) + 1.8752889355546e-7*log(
                       124.859074951742 - 0.992021101872995*m.x1) + 1.3740096939214e-7*log(223.191842620706 - 
                       0.960459704785605*m.x1) + 4.255809052408e-8*log(115.459144825851 - 0.995038152387588*m.x1) + 
                       1.0082547800804e-7*log(195.619011271494 - 0.969309624295303*m.x1) + 8.922261921434e-8*log(
                       397.575610857661 - 0.904488582591116*m.x1) + 6.537272227054e-8*log(563.967667251912 - 
                       0.851082521839063*m.x1) + 2.024831619316e-8*log(261.374980189838 - 0.948204246148269*m.x1) + 
                       4.797081089904e-8*log(427.227345312113 - 0.894971407516808*m.x1) + 5.681816460539e-7*log(
                       386.878396754352 - 0.9079220161255*m.x1) + 1.7598657260608e-7*log(120.492923527267 - 
                       0.993422484566864*m.x1) + 4.1693436380136e-7*log(213.671510258415 - 0.963515400228876*m.x1) + 
                       1.1000473212982e-7*log(295.531454568911 - 0.937241206293514*m.x1) + 2.6061507248382e-7*log(
                       669.104546649669 - 0.817337241625121*m.x1) + 5.086014931706e-8*log(201.317582629125 - 
                       0.967480581162351*m.x1) + 7.50541219538e-9*log(351.372276733356 - 0.91931824527251*m.x1) + 
                       5.49915589932e-9*log(439.694024130733 - 0.890970037374558*m.x1) + 1.70328992508e-9*log(
                       425.744308464212 - 0.895447410745045*m.x1) + 4.03530900568e-9*log(770.412001886567 - 
                       0.784821073328011*m.x1) + 4.611643597144e-8*log(305.054577441609 - 0.934184615193495*m.x1) + 
                       1.428394225608e-8*log(144.210295969209 - 0.985810033221758*m.x1) + 3.384045851456e-8*log(
                       361.165768375904 - 0.916174875204426*m.x1) + 9.0506638259e-9*log(416.6832011542 - 
                       0.898355710924548*m.x1) + 2.144216696738e-8*log(1000.33799452779 - 0.711022829604292*m.x1) + 
                       4.27675523074e-9*log(609.571269923759 - 0.836445352087194*m.x1) + 1.889276103448e-8*log(
                       434.3964722351 - 0.892670367213051*m.x1) + 5.85177761618e-9*log(468.1319046228 - 
                       0.881842467188032*m.x1) + 1.386359786034e-8*log(431.366382166974 - 0.89364292069769*m.x1) + 
                       3.7138893975e-9*log(417.681098644165 - 0.898035420550547*m.x1) + 8.7986683833e-9*log(
                       281.656582108581 - 0.941694557598865*m.x1) + 1.7596354465e-9*log(544.304427698094 - 
                       0.857393737584273*m.x1) + 5.333541954492e-8*log(542.237671927793 - 0.858057094277016*m.x1) + 
                       1.2635832772558e-7*log(1124.54527292762 - 0.671156614835294*m.x1) + 2.489499217358e-8*log(
                       308.855541867342 - 0.932964637861428*m.x1) + 1.368714141078e-8*log(1763.23723209658 - 
                       0.466158718226546*m.x1) + 6.37686849336e-8*log(569.736214727577 - 0.849231018806932*m.x1) + 
                       2.934953175558e-7*log(188.889418976798 - 0.971469589276296*m.x1) + 2.150417483922e-7*log(
                       498.037793762171 - 0.872243717302778*m.x1) + 6.66062709384e-8*log(155.847309756665 - 
                       0.982074956687618*m.x1) + 1.577986470492e-7*log(417.53184038923 - 0.898083327257174*m.x1) + 
                       1.396393934982e-7*log(921.108334776294 - 0.736452793712839*m.x1) + 1.023127024242e-7*log(
                       1223.70253679607 - 0.63933058315492*m.x1) + 3.16899752268e-8*log(602.595974199814 - 
                       0.838684179320111*m.x1) + 7.50775419792e-8*log(981.05542553819 - 0.717211863343225*m.x1) + 
                       8.89242449397e-7*log(898.744559240035 - 0.743630787547502*m.x1) + 2.754308097984e-7*log(
                       173.625982517328 - 0.976368621312466*m.x1) + 6.525302911128e-7*log(470.737308077767 - 
                       0.881006223329912*m.x1) + 1.721647964586e-7*log(689.934119679135 - 0.81065167341497*m.x1) + 
                       4.078800978786e-7*log(1379.48685669706 - 0.589329236737658*m.x1) + 7.95995507238e-8*log(
                       434.53489173985 - 0.892625939368116*m.x1) + 1.17464743374e-8*log(821.528017445544 - 
                       0.768414610835129*m.x1) + 8.6065484436e-9*log(1005.40092452386 - 0.70939780523226*m.x1) + 
                       2.6657631684e-9*log(978.126239585041 - 0.718152030117757*m.x1) + 6.3155297064e-9*log(
                       1509.82444407999 - 0.547495406079565*m.x1) + 7.21753206312e-8*log(713.319521316552 - 
                       0.803145773147713*m.x1) + 2.23553292984e-8*log(254.833607664751 - 0.950303799132029*m.x1) + 
                       5.29625911488e-8*log(843.299200702345 - 0.761426818503854*m.x1) + 1.4164896957e-8*log(
                       960.073904810529 - 0.723946201477714*m.x1) + 3.35584318974e-8*log(1751.11759537046 - 
                       0.470048699931889*m.x1) + 6.6934092702e-9*log(1294.134940734 - 0.61672423207582*m.x1) + 
                       2.95684403304e-8*log(995.115859229992 - 0.712698953338883*m.x1) + 9.1584251214e-9*log(
                       1059.13998011045 - 0.692149438155075*m.x1) + 2.16974620782e-8*log(989.193128395073 - 
                       0.714599943864767*m.x1) + 5.812486425e-9*log(962.075202498917 - 0.723303854551755*m.x1) + 
                       1.3770507159e-8*log(655.123209981677 - 0.821824764236877*m.x1) + 2.753947695e-9*log(
                       1191.8558240632 - 0.649552269885778*m.x1) + 8.34735149316e-8*log(1188.45417529629 - 
                       0.650644080784922*m.x1) + 1.977592722834e-7*log(1857.44137536029 - 0.435922465924234*m.x1) + 
                       3.89623353234e-8*log(722.540865408159 - 0.800186042536505*m.x1) + 2.14212958794e-8*log(
                       2241.25089526186 - 0.312732964085803*m.x1) + 1.37450609492688e-6*log(100 + 0.77*m.x159*(3115.6025
                        + m.x1)/(0.000940324545070664 + m.x159) - m.x1) + 6.32616311960964e-6*log(100 + 0.77*m.x160*(
                       3115.6025 + m.x1)/(0.00595007430547527 + m.x160) - m.x1) + 4.63513077204876e-6*log(100 + 0.77*
                       m.x161*(3115.6025 + m.x1)/(0.00115094525652066 + m.x161) - m.x1) + 1.43566901937072e-6*log(
                       112.422531061639 - 0.996012799751689*m.x1) + 3.40128077544936e-6*log(100 + 0.77*m.x162*(3115.6025
                        + m.x1)/(0.00150079877413969 + m.x162) - m.x1) + 3.00986601268356e-6*log(100 + 0.77*m.x163*(
                       3115.6025 + m.x1)/(0.000439964488305142 + m.x163) - m.x1) + 2.20530552287436e-6*log(100 + 0.77*
                       m.x164*(3115.6025 + m.x1)/(0.000259837570039233 + m.x164) - m.x1) + 6.8306354667144e-7*log(100 + 
                       0.77*m.x165*(3115.6025 + m.x1)/(0.000863877417965782 + m.x165) - m.x1) + 1.61826355914336e-6*log(
                       100 + 0.77*m.x166*(3115.6025 + m.x1)/(0.000394451614430133 + m.x166) - m.x1) + 
                       1.91672318134926e-5*log(100 + 0.77*m.x167*(3115.6025 + m.x1)/(0.000458693143304774 + m.x167) - 
                       m.x1) + 5.93679056095872e-6*log(100 + 0.77*m.x168*(3115.6025 + m.x1)/(0.00723105029860804 + 
                       m.x168) - m.x1) + 1.40650048404302e-5*log(100 + 0.77*m.x169*(3115.6025 + m.x1)/(
                       0.00125255833504483 + m.x169) - m.x1) + 3.71093683852188e-6*log(100 + 0.77*m.x170*(3115.6025 + 
                       m.x1)/(0.000702087563679832 + m.x170) - m.x1) + 8.79167699815788e-6*log(100 + 0.77*m.x171*(
                       3115.6025 + m.x1)/(0.000200325317210912 + m.x171) - m.x1) + 1.71573347854404e-6*log(100 + 0.77*
                       m.x172*(3115.6025 + m.x1)/(0.0014128827573583 + m.x172) - m.x1) + 2.5319011341492e-7*log(100 + 
                       0.77*m.x173*(3115.6025 + m.x1)/(0.00053228318911196 + m.x173) - m.x1) + 1.8551038498488e-7*log(
                       100 + 0.77*m.x174*(3115.6025 + m.x1)/(0.000377688899663851 + m.x174) - m.x1) + 5.745935840472e-8*
                       log(368.627863474912 - 0.913779802309533*m.x1) + 1.3612847878512e-7*log(100 + 0.77*m.x175*(
                       3115.6025 + m.x1)/(0.000160639196334586 + m.x175) - m.x1) + 1.55570744816496e-6*log(100 + 0.77*
                       m.x176*(3115.6025 + m.x1)/(0.000666587889373534 + m.x176) - m.x1) + 4.8185933905872e-7*log(
                       135.61051678515 - 0.988570263124019*m.x1) + 1.14158547275904e-6*log(100 + 0.77*m.x177*(3115.6025
                        + m.x1)/(0.000509986775800951 + m.x177) - m.x1) + 3.053181545406e-7*log(100 + 0.77*m.x178*(
                       3115.6025 + m.x1)/(0.000409659463712101 + m.x178) - m.x1) + 7.2333731246292e-7*log(100 + 0.77*
                       m.x179*(3115.6025 + m.x1)/(0.00010370518389028 + m.x179) - m.x1) + 1.4427350740116e-7*log(100 + 
                       0.77*m.x180*(3115.6025 + m.x1)/(0.000231008038688752 + m.x180) - m.x1) + 6.3733479048432e-7*log(
                       100 + 0.77*m.x181*(3115.6025 + m.x1)/(0.000384659283695111 + m.x181) - m.x1) + 1.9740584524212e-7
                       *log(100 + 0.77*m.x182*(3115.6025 + m.x1)/(0.000343700012896749 + m.x182) - m.x1) + 
                       4.6767929904756e-7*log(100 + 0.77*m.x183*(3115.6025 + m.x1)/(0.000388746395185924 + m.x183) - 
                       m.x1) + 1.25285601015e-7*log(361.799939823277 - 0.915971328234819*m.x1) + 2.968172550522e-7*log(
                       248.001154118093 - 0.952496778996007*m.x1) + 5.9360137281e-8*log(470.110557767541 - 
                       0.881207388372701*m.x1) + 1.79923508157528e-6*log(100 + 0.77*m.x184*(3115.6025 + m.x1)/(
                       0.000275666343417648 + m.x184) - m.x1) + 4.26261456332172e-6*log(100 + 0.77*m.x185*(3115.6025 + 
                       m.x1)/(8.35799287817407e-5 + m.x185) - m.x1) + 8.3981608575372e-7*log(100 + 0.77*m.x186*(
                       3115.6025 + m.x1)/(0.00065332282343346 + m.x186) - m.x1) + 4.6172665749852e-7*log(100 + 0.77*
                       m.x187*(3115.6025 + m.x1)/(2.75606934013358e-5 + m.x187) - m.x1) + 1.1756568780872e-6*log(100 + 
                       0.77*m.x188*(3115.6025 + m.x1)/(0.000592771973025286 + m.x188) - m.x1) + 5.4109597701466e-6*log(
                       100 + 0.77*m.x189*(3115.6025 + m.x1)/(0.00375087229637144 + m.x189) - m.x1) + 3.9645683588494e-6*
                       log(100 + 0.77*m.x190*(3115.6025 + m.x1)/(0.000725545338711303 + m.x190) - m.x1) + 
                       1.2279713880568e-6*log(119.646430506762 - 0.99369417937405*m.x1) + 2.9092189206884e-6*log(100 + 
                       0.77*m.x191*(3115.6025 + m.x1)/(0.000946089789024766 + m.x191) - m.x1) + 2.5744299665114e-6*log(
                       100 + 0.77*m.x192*(3115.6025 + m.x1)/(0.000277349580164474 + m.x192) - m.x1) + 1.8862649033134e-6
                       *log(100 + 0.77*m.x193*(3115.6025 + m.x1)/(0.000163799222157577 + m.x193) - m.x1) + 
                       5.842450315636e-7*log(100 + 0.77*m.x194*(3115.6025 + m.x1)/(0.000544580404908056 + m.x194) - m.x1
                       ) + 1.3841500527984e-6*log(100 + 0.77*m.x195*(3115.6025 + m.x1)/(0.00024865868170142 + m.x195) - 
                       m.x1) + 1.6394316473819e-5*log(100 + 0.77*m.x196*(3115.6025 + m.x1)/(0.000289155952586038 + 
                       m.x196) - m.x1) + 5.0779175752768e-6*log(100 + 0.77*m.x197*(3115.6025 + m.x1)/(
                       0.00455838781941915 + m.x197) - m.x1) + 1.20302265242856e-5*log(100 + 0.77*m.x198*(3115.6025 + 
                       m.x1)/(0.000789601291900758 + m.x198) - m.x1) + 3.1740771717622e-6*log(100 + 0.77*m.x199*(
                       3115.6025 + m.x1)/(0.000442589563933731 + m.x199) - m.x1) + 7.5197887961022e-6*log(100 + 0.77*
                       m.x200*(3115.6025 + m.x1)/(0.000126283243538118 + m.x200) - m.x1) + 1.4675190400826e-6*log(100 + 
                       0.77*m.x201*(3115.6025 + m.x1)/(0.000890668337993608 + m.x201) - m.x1) + 2.165612065298e-7*log(
                       100 + 0.77*m.x202*(3115.6025 + m.x1)/(0.00033554644284477 + m.x202) - m.x1) + 1.586726758572e-7*
                       log(100 + 0.77*m.x203*(3115.6025 + m.x1)/(0.000238091619980701 + m.x203) - m.x1) + 
                       4.91467372668e-8*log(499.876211729988 - 0.871653649099977*m.x1) + 1.164348291928e-7*log(100 + 
                       0.77*m.x204*(3115.6025 + m.x1)/(0.00010126547675015 + m.x204) - m.x1) + 1.3306439080024e-6*log(
                       100 + 0.77*m.x205*(3115.6025 + m.x1)/(0.00042021089468532 + m.x205) - m.x1) + 4.121489517768e-7*
                       log(156.002187849084 - 0.982025246208692*m.x1) + 9.764327840576e-7*log(100 + 0.77*m.x206*(
                       3115.6025 + m.x1)/(0.000321490988290235 + m.x206) - m.x1) + 2.61147905939e-7*log(100 + 0.77*
                       m.x207*(3115.6025 + m.x1)/(0.000258245570474664 + m.x207) - m.x1) + 6.186924086498e-7*log(100 + 
                       0.77*m.x208*(3115.6025 + m.x1)/(6.53747972334079e-5 + m.x208) - m.x1) + 1.234015199554e-7*log(100
                        + 0.77*m.x209*(3115.6025 + m.x1)/(0.000145625349881665 + m.x209) - m.x1) + 5.451318352408e-7*
                       log(100 + 0.77*m.x210*(3115.6025 + m.x1)/(0.000242485686174776 + m.x210) - m.x1) + 
                       1.688472248978e-7*log(100 + 0.77*m.x211*(3115.6025 + m.x1)/(0.000216665337347236 + m.x211) - m.x1
                       ) + 4.000203321714e-7*log(100 + 0.77*m.x212*(3115.6025 + m.x1)/(0.000245062163791024 + m.x212) - 
                       m.x1) + 1.07160585975e-7*log(490.323466912148 - 0.874719747813738*m.x1) + 2.53876827993e-7*log(
                       100 + 0.77*m.x213*(3115.6025 + m.x1)/(0.000479394172170398 + m.x213) - m.x1) + 5.0772531265e-8*
                       log(638.410997400727 - 0.82718880300015*m.x1) + 1.5389405014332e-6*log(100 + 0.77*m.x214*(
                       3115.6025 + m.x1)/(0.000173777535789056 + m.x214) - m.x1) + 3.6459439128718e-6*log(100 + 0.77*
                       m.x215*(3115.6025 + m.x1)/(5.26880209061672e-5 + m.x215) - m.x1) + 7.183202469518e-7*log(100 + 
                       0.77*m.x216*(3115.6025 + m.x1)/(0.000411848718720832 + m.x216) - m.x1) + 3.949288567638e-7*log(
                       100 + 0.77*m.x217*(3115.6025 + m.x1)/(1.73740084645212e-5 + m.x217) - m.x1) + 2.3027003834052e-7*
                       log(310.644288882208 - 0.932390512306301*m.x1) + 1.05981765339381e-6*log(135.946817505807 - 
                       0.988462322293743*m.x1) + 7.7652019480479e-7*log(274.907218484447 - 0.943860868488696*m.x1) + 
                       2.4051662000988e-7*log(122.393839487144 - 0.992812356683131*m.x1) + 5.6981417358594e-7*log(
                       236.453447120506 - 0.956203191157888*m.x1) + 5.0424073396149e-7*log(509.329744330999 - 
                       0.868619394055885*m.x1) + 3.6945328156719e-7*log(719.780347180692 - 0.801072072839622*m.x1) + 
                       1.1443315505226e-7*log(327.517012158458 - 0.926974955194555*m.x1) + 2.7110655469944e-7*log(
                       547.744519196025 - 0.856289587906023*m.x1) + 3.21107285072415e-6*log(495.371037182199 - 
                       0.873099653379339*m.x1) + 9.9458634278688e-7*log(129.657584748611 - 0.990480947184819*m.x1) + 
                       2.35630035822996e-6*log(261.674211430671 - 0.948108203331243*m.x1) + 6.2169063581427e-7*log(
                       373.959049138861 - 0.912068677201645*m.x1) + 1.47286345758327e-6*log(846.602134340364 - 
                       0.760366691726443*m.x1) + 2.8743562167141e-7*log(244.433016330596 - 0.953642027078038*m.x1) + 
                       4.241676143793e-8*log(448.653645634299 - 0.888094310607884*m.x1) + 3.107842418502e-8*log(
                       563.774842073764 - 0.851144412012199*m.x1) + 9.62612585838e-9*log(545.832820860844 - 
                       0.856903176557072*m.x1) + 2.280550820748e-8*log(964.57779102352 - 0.722500610708998*m.x1) + 
                       2.6062657347084e-7*log(386.804719169038 - 0.90794566406689*m.x1) + 8.072555581188e-8*log(
                       163.697577366872 - 0.979555293922485*m.x1) + 1.9124901050016e-7*log(461.599091032222 - 
                       0.88393927305161*m.x1) + 5.114973546615e-8*log(534.130728924762 - 0.860659140912629*m.x1) + 
                       1.2118019067993e-7*log(1218.02524091695 - 0.641152797599519*m.x1) + 2.417003911689e-8*log(
                       775.353772232083 - 0.783234936988245*m.x1) + 1.0677224872428e-7*log(556.971636607364 - 
                       0.853328004260054*m.x1) + 3.307126226673e-8*log(600.07781259564 - 0.839492421579569*m.x1) + 
                       7.834998369249e-8*log(553.074587453001 - 0.854578821446895*m.x1) + 2.098900852875e-8*log(
                       535.421327803972 - 0.860244903576765*m.x1) + 4.972558576005e-8*log(355.163421699796 - 
                       0.918101419645222*m.x1) + 9.94456200525e-9*log(695.545998372881 - 0.808850455610791*m.x1) + 
                       3.0142458643662e-7*log(692.989141812062 - 0.809671117605002*m.x1) + 7.1411281663263e-7*log(
                       1347.27032802532 - 0.599669621517727*m.x1) + 1.4069379756063e-7*log(391.919406907936 - 
                       0.906304027260237*m.x1) + 7.735274184483e-8*log(1939.03334836773 - 0.409734281453512*m.x1) + 
                       2.2272443732888e-6*log(100 + 0.77*m.x218*(3115.6025 + m.x1)/(0.000274060001623156 + m.x218) - 
                       m.x1) + 1.02508903122814e-5*log(100 + 0.77*m.x219*(3115.6025 + m.x1)/(0.00173416442478794 + 
                       m.x219) - m.x1) + 7.5107480204026e-6*log(100 + 0.77*m.x220*(3115.6025 + m.x1)/(
                       0.000335445948448057 + m.x220) - m.x1) + 2.3263525400872e-6*log(100 + 0.77*m.x221*(3115.6025 + 
                       m.x1)/(0.00279966370191667 + m.x221) - m.x1) + 5.5114222461836e-6*log(100 + 0.77*m.x222*(
                       3115.6025 + m.x1)/(0.000437411653915557 + m.x222) - m.x1) + 4.8771752747006e-6*log(100 + 0.77*
                       m.x223*(3115.6025 + m.x1)/(0.000128228779107299 + m.x223) - m.x1) + 3.5734685610586e-6*log(100 + 
                       0.77*m.x224*(3115.6025 + m.x1)/(7.57303265558781e-5 + m.x224) - m.x1) + 1.1068335357244e-6*log(
                       100 + 0.77*m.x225*(3115.6025 + m.x1)/(0.000251779290257831 + m.x225) - m.x1) + 2.6222280278736e-6
                       *log(100 + 0.77*m.x226*(3115.6025 + m.x1)/(0.00011496393522606 + m.x226) - m.x1) + 
                       3.1058508482201e-5*log(100 + 0.77*m.x227*(3115.6025 + m.x1)/(0.000133687293666454 + m.x227) - 
                       m.x1) + 9.6199525204672e-6*log(100 + 0.77*m.x228*(3115.6025 + m.x1)/(0.00210750816509285 + m.x228
                       ) - m.x1) + 2.27908795797624e-5*log(100 + 0.77*m.x229*(3115.6025 + m.x1)/(0.000365061340932758 + 
                       m.x229) - m.x1) + 6.0131877361138e-6*log(100 + 0.77*m.x230*(3115.6025 + m.x1)/(
                       0.000204625222058021 + m.x230) - m.x1) + 1.42459994889738e-5*log(100 + 0.77*m.x231*(3115.6025 + 
                       m.x1)/(5.83853277549572e-5 + m.x231) - m.x1) + 2.7801679092254e-6*log(100 + 0.77*m.x232*(
                       3115.6025 + m.x1)/(0.000411788305223751 + m.x232) - m.x1) + 4.102682829542e-7*log(100 + 0.77*
                       m.x233*(3115.6025 + m.x1)/(0.000155135301356022 + m.x233) - m.x1) + 3.006003121188e-7*log(100 + 
                       0.77*m.x234*(3115.6025 + m.x1)/(0.000110078398992706 + m.x234) - m.x1) + 9.31069226772e-8*log(100
                        + 0.77*m.x235*(3115.6025 + m.x1)/(0.000115570007588387 + m.x235) - m.x1) + 2.205820618312e-7*
                       log(100 + 0.77*m.x236*(3115.6025 + m.x1)/(4.68187059871874e-5 + m.x236) - m.x1) + 
                       2.5208623469896e-6*log(100 + 0.77*m.x237*(3115.6025 + m.x1)/(0.000194278750885906 + m.x237) - 
                       m.x1) + 7.808030139672e-7*log(100 + 0.77*m.x238*(3115.6025 + m.x1)/(0.000967158090120206 + m.x238
                       ) - m.x1) + 1.8498206957504e-6*log(100 + 0.77*m.x239*(3115.6025 + m.x1)/(0.000148636954481809 + 
                       m.x239) - m.x1) + 4.94736359681e-7*log(100 + 0.77*m.x240*(3115.6025 + m.x1)/(0.000119396301924079
                        + m.x240) - m.x1) + 1.1720929904342e-6*log(100 + 0.77*m.x241*(3115.6025 + m.x1)/(
                       3.02251419621976e-5 + m.x241) - m.x1) + 2.337802347766e-7*log(100 + 0.77*m.x242*(3115.6025 + m.x1
                       )/(6.73278856644583e-5 + m.x242) - m.x1) + 1.0327348356232e-6*log(100 + 0.77*m.x243*(3115.6025 + 
                       m.x1)/(0.000112109935305285 + m.x243) - m.x1) + 3.198756700262e-7*log(100 + 0.77*m.x244*(
                       3115.6025 + m.x1)/(0.000100172250725714 + m.x244) - m.x1) + 7.578257318406e-7*log(100 + 0.77*
                       m.x245*(3115.6025 + m.x1)/(0.0001133011344372 + m.x245) - m.x1) + 2.03012304525e-7*log(100 + 0.77
                       *m.x246*(3115.6025 + m.x1)/(0.000118964217618766 + m.x246) - m.x1) + 4.80961534947e-7*log(100 + 
                       0.77*m.x247*(3115.6025 + m.x1)/(0.000221641328507187 + m.x247) - m.x1) + 9.6186937435e-8*log(100
                        + 0.77*m.x248*(3115.6025 + m.x1)/(7.98854666975635e-5 + m.x248) - m.x1) + 2.9154735846228e-6*
                       log(100 + 0.77*m.x249*(3115.6025 + m.x1)/(8.03436631751567e-5 + m.x249) - m.x1) + 
                       6.9071241929722e-6*log(100 + 0.77*m.x250*(3115.6025 + m.x1)/(2.43595847174932e-5 + m.x250) - m.x1
                       ) + 1.3608347452922e-6*log(100 + 0.77*m.x251*(3115.6025 + m.x1)/(0.000190412613378249 + m.x251)
                        - m.x1) + 7.481800944402e-7*log(100 + 0.77*m.x252*(3115.6025 + m.x1)/(8.03263481518263e-6 + 
                       m.x252) - m.x1) + 3.48578463039596e-6*log(100 + 0.77*m.x253*(3115.6025 + m.x1)/(
                       0.000115610604617764 + m.x253) - m.x1) + 1.60433207630746e-5*log(100 + 0.77*m.x254*(3115.6025 + 
                       m.x1)/(0.000731547093588758 + m.x254) - m.x1) + 1.17548169955132e-5*log(100 + 0.77*m.x255*(
                       3115.6025 + m.x1)/(0.000141505906323334 + m.x255) - m.x1) + 3.64089546094324e-6*log(100 + 0.77*
                       m.x256*(3115.6025 + m.x1)/(0.00118102171563895 + m.x256) - m.x1) + 8.62574003453462e-6*log(100 + 
                       0.77*m.x257*(3115.6025 + m.x1)/(0.000184519541255673 + m.x257) - m.x1) + 7.63310161030727e-6*log(
                       100 + 0.77*m.x258*(3115.6025 + m.x1)/(5.40925585426253e-5 + m.x258) - m.x1) + 5.59271444872837e-6
                       *log(100 + 0.77*m.x259*(3115.6025 + m.x1)/(3.19463941807333e-5 + m.x259) - m.x1) + 
                       1.73226762788398e-6*log(100 + 0.77*m.x260*(3115.6025 + m.x1)/(0.000106211617180695 + m.x260) - 
                       m.x1) + 4.10396015209512e-6*log(100 + 0.77*m.x261*(3115.6025 + m.x1)/(4.84968619353583e-5 + 
                       m.x261) - m.x1) + 4.86086182588105e-5*log(100 + 0.77*m.x262*(3115.6025 + m.x1)/(
                       5.63952009010913e-5 + m.x262) - m.x1) + 1.50558614237142e-5*log(100 + 0.77*m.x263*(3115.6025 + 
                       m.x1)/(0.000889039961177141 + m.x263) - m.x1) + 3.56692326648611e-5*log(100 + 0.77*m.x264*(
                       3115.6025 + m.x1)/(0.000153998985980601 + m.x264) - m.x1) + 9.41103618516721e-6*log(100 + 0.77*
                       m.x265*(3115.6025 + m.x1)/(8.63199500184675e-5 + m.x265) - m.x1) + 2.22959306391542e-5*log(100 + 
                       0.77*m.x266*(3115.6025 + m.x1)/(2.46295081463161e-5 + m.x266) - m.x1) + 4.35114650377943e-6*log(
                       100 + 0.77*m.x267*(3115.6025 + m.x1)/(0.000173710481863398 + m.x267) - m.x1) + 6.4209697517339e-7
                       *log(100 + 0.77*m.x268*(3115.6025 + m.x1)/(6.54429171754531e-5 + m.x268) - m.x1) + 
                       4.7045935346946e-7*log(100 + 0.77*m.x269*(3115.6025 + m.x1)/(4.64359271237298e-5 + m.x269) - m.x1
                       ) + 1.4571848690874e-7*log(100 + 0.77*m.x270*(3115.6025 + m.x1)/(4.87525300074436e-5 + m.x270) - 
                       m.x1) + 3.4522550380804e-7*log(100 + 0.77*m.x271*(3115.6025 + m.x1)/(1.97501965793709e-5 + m.x271
                       ) - m.x1) + 3.94531616281732e-6*log(100 + 0.77*m.x272*(3115.6025 + m.x1)/(8.19553518254294e-5 + 
                       m.x272) - m.x1) + 1.22200831578924e-6*log(100 + 0.77*m.x273*(3115.6025 + m.x1)/(
                       0.000407989968975871 + m.x273) - m.x1) + 2.89509163321568e-6*log(100 + 0.77*m.x274*(3115.6025 + 
                       m.x1)/(6.27016276523772e-5 + m.x274) - m.x1) + 7.7429509727645e-7*log(100 + 0.77*m.x275*(
                       3115.6025 + m.x1)/(5.03666298358569e-5 + m.x275) - m.x1) + 1.83440298713939e-6*log(100 + 0.77*
                       m.x276*(3115.6025 + m.x1)/(1.27502988988239e-5 + m.x276) - m.x1) + 3.6588151666147e-7*log(100 + 
                       0.77*m.x277*(3115.6025 + m.x1)/(2.8401873761961e-5 + m.x277) - m.x1) + 1.61629826545444e-6*log(
                       100 + 0.77*m.x278*(3115.6025 + m.x1)/(4.72929188044174e-5 + m.x278) - m.x1) + 5.0062656239579e-7*
                       log(100 + 0.77*m.x279*(3115.6025 + m.x1)/(4.22570765661979e-5 + m.x279) - m.x1) + 
                       1.18604735082027e-6*log(100 + 0.77*m.x280*(3115.6025 + m.x1)/(4.77954191731146e-5 + m.x280) - 
                       m.x1) + 3.1772767253625e-7*log(100 + 0.77*m.x281*(3115.6025 + m.x1)/(5.01843576053702e-5 + m.x281
                       ) - m.x1) + 7.5273658626615e-7*log(100 + 0.77*m.x282*(3115.6025 + m.x1)/(9.34980947428967e-5 + 
                       m.x282) - m.x1) + 1.5053891354575e-7*log(100 + 0.77*m.x283*(3115.6025 + m.x1)/(
                       3.36992156840782e-5 + m.x283) - m.x1) + 4.56290882737626e-6*log(100 + 0.77*m.x284*(3115.6025 + 
                       m.x1)/(3.38925031813217e-5 + m.x284) - m.x1) + 1.08101058154415e-5*log(100 + 0.77*m.x285*(
                       3115.6025 + m.x1)/(1.02759479703261e-5 + m.x285) - m.x1) + 2.12979630638549e-6*log(100 + 0.77*
                       m.x286*(3115.6025 + m.x1)/(8.03244443885601e-5 + m.x286) - m.x1) + 1.17095129086209e-6*log(100 + 
                       0.77*m.x287*(3115.6025 + m.x1)/(3.38851989402637e-6 + m.x287) - m.x1) + 1.8183738183868e-7*log(
                       193.364173093206 - 0.970033348896977*m.x1) + 8.3690639350379e-7*log(115.254735565526 - 
                       0.995103760648052*m.x1) + 6.1319483935361e-7*log(176.825857180065 - 0.975341572880345*m.x1) + 
                       1.8992880179492e-7*log(109.471992936955 - 0.996959819830368*m.x1) + 4.4996525907646e-7*log(
                       159.35999423299 - 0.980947507189062*m.x1) + 3.9818386942891e-7*log(291.087251996003 - 
                       0.938667640690363*m.x1) + 2.9174623809521e-7*log(406.623520914578 - 0.901584518270679*m.x1) + 
                       9.036444975734e-8*log(201.277457067861 - 0.967493460071411*m.x1) + 2.1408476092296e-7*log(
                       311.19442233872 - 0.932213938607791*m.x1) + 2.53568846505985e-6*log(283.883103312431 - 
                       0.940979921760741*m.x1) + 7.8539517293792e-7*log(112.566524343699 - 0.995966582918168*m.x1) + 
                       1.86070011997164e-6*log(170.777277381972 - 0.97728295654469*m.x1) + 4.9093055416493e-7*log(
                       223.415319381483 - 0.960387976520919*m.x1) + 1.16307634663593e-6*log(483.165743746284 - 
                       0.877017127908235*m.x1) + 2.2697933812219e-7*log(162.956712613236 - 0.979793085731175*m.x1) + 
                       3.349525149487e-8*log(260.157811542521 - 0.948594914934585*m.x1) + 2.454170471418e-8*log(
                       319.709287061812 - 0.929480963293035*m.x1) + 7.60146450642e-9*log(310.18391133055 - 
                       0.932538277482269*m.x1) + 1.800882969332e-8*log(559.688690006188 - 0.852455924654641*m.x1) + 
                       2.0580903229556e-7*log(229.632746466765 - 0.958392398752163*m.x1) + 6.374656391292e-8*log(
                       127.215287247597 - 0.991264839706735*m.x1) + 1.5102363989344e-7*log(266.673373771106 - 
                       0.946503646157972*m.x1) + 4.039142063785e-8*log(304.020979998872 - 0.934516364010212*m.x1) + 
                       9.569238257287e-8*log(744.280921668034 - 0.793208240888228*m.x1) + 1.908635905751e-8*log(
                       439.474870738743 - 0.891040377988289*m.x1) + 8.431486050452e-8*log(316.086561642226 - 
                       0.930643732105676*m.x1) + 2.611538951407e-8*log(339.269581293755 - 0.923202789414325*m.x1) + 
                       6.187064545791e-8*log(314.017393171395 - 0.931307863191343*m.x1) + 1.657439407125e-8*log(
                       304.698766948572 - 0.934298817981892*m.x1) + 3.926681208795e-8*log(214.392130109138 - 
                       0.96328410632963*m.x1) + 7.85292403475e-9*log(392.620228975356 - 0.9060790877606*m.x1) + 
                       2.3802600639858e-7*log(391.153960662165 - 0.906549708872629*m.x1) + 5.6391359401217e-7*log(
                       850.86177688669 - 0.758999494676651*m.x1) + 1.1110169596417e-7*log(232.119855144384 - 
                       0.957594123401691*m.x1) + 6.108315331197e-8*log(1491.69160837479 - 0.55331541543737*m.x1) + 
                       1.75878843630284e-6*log(100 + 0.77*m.x288*(3115.6025 + m.x1)/(0.00320020232823025 + m.x288) - 
                       m.x1) + 8.09482226524927e-6*log(105.908941656468 - 0.998103435320627*m.x1) + 5.93101364389693e-6*
                       log(100 + 0.77*m.x289*(3115.6025 + m.x1)/(0.00391700685565556 + m.x289) - m.x1) + 
                       1.83705119893396e-6*log(103.663543949195 - 0.998824129859571*m.x1) + 4.35220572579398e-6*log(100
                        + 0.77*m.x290*(3115.6025 + m.x1)/(0.00510766177101759 + m.x290) - m.x1) + 3.85135981387583e-6*
                       log(100 + 0.77*m.x291*(3115.6025 + m.x1)/(0.00149732917979604 + m.x291) - m.x1) + 
                       2.82186151553773e-6*log(100 + 0.77*m.x292*(3115.6025 + m.x1)/(0.000884304042641739 + m.x292) - 
                       m.x1) + 8.7403342304542e-7*log(140.116885035848 - 0.987123875707556*m.x1) + 2.07069524479848e-6*
                       log(100 + 0.77*m.x293*(3115.6025 + m.x1)/(0.00134243541922925 + m.x293) - m.x1) + 
                       2.45259775812781e-5*log(100 + 0.77*m.x294*(3115.6025 + m.x1)/(0.00156106832778344 + m.x294) - 
                       m.x1) + 7.59658951379296e-6*log(104.864298820897 - 0.998438729324137*m.x1) + 1.79972776848313e-5*
                       log(100 + 0.77*m.x295*(3115.6025 + m.x1)/(0.00426282619236897 + m.x295) - m.x1) + 
                       4.74843496404409e-6*log(100 + 0.77*m.x296*(3115.6025 + m.x1)/(0.00238941147254734 + m.x296) - 
                       m.x1) + 1.12496407961671e-5*log(100 + 0.77*m.x297*(3115.6025 + m.x1)/(0.000681766258152549 + 
                       m.x297) - m.x1) + 2.19541565728847e-6*log(100 + 0.77*m.x298*(3115.6025 + m.x1)/(
                       0.00480845758341298 + m.x298) - m.x1) + 3.2397662353331e-7*log(164.437067242418 - 
                       0.979317943401824*m.x1) + 2.3737509868434e-7*log(189.824673314027 - 0.971169405174753*m.x1) + 
                       7.352375918346e-8*log(185.708911713758 - 0.972490421446973*m.x1) + 1.7418707361316e-7*log(
                       301.02255994106 - 0.935478752523449*m.x1) + 1.99064979064228e-6*log(100 + 0.77*m.x299*(3115.6025
                        + m.x1)/(0.00226859558939085 + m.x299) - m.x1) + 6.1657684646796e-7*log(110.574382290427 - 
                       0.996605991203812*m.x1) + 1.46074821781472e-6*log(100 + 0.77*m.x300*(3115.6025 + m.x1)/(
                       0.00173563571837019 + m.x300) - m.x1) + 3.9067854379205e-7*log(183.057292642768 - 
                       0.973341498909836*m.x1) + 9.2556686754731e-7*log(100 + 0.77*m.x301*(3115.6025 + m.x1)/(
                       0.00035293938957031 + m.x301) - m.x1) + 1.8460927704763e-7*log(243.449327510641 - 
                       0.953957756963335*m.x1) + 8.1551989015876e-7*log(100 + 0.77*m.x302*(3115.6025 + m.x1)/(
                       0.00130910922373505 + m.x302) - m.x1) + 2.5259627378291e-7*log(198.343400264271 - 
                       0.968435190219461*m.x1) + 5.9843237225283e-7*log(100 + 0.77*m.x303*(3115.6025 + m.x1)/(
                       0.00132301887203383 + m.x303) - m.x1) + 1.6031276042625e-7*log(183.348480295548 - 
                       0.973248037804711*m.x1) + 3.7980097564335e-7*log(145.468442132924 - 0.985406212078427*m.x1) + 
                       7.595595495175e-8*log(222.047016072243 - 0.960827154275219*m.x1) + 2.30226251258154e-6*log(100 + 
                       0.77*m.x304*(3115.6025 + m.x1)/(0.000938174036447789 + m.x304) - m.x1) + 5.45434991525821e-6*log(
                       100 + 0.77*m.x305*(3115.6025 + m.x1)/(0.000284447198664313 + m.x305) - m.x1) + 
                       1.07461060063421e-6*log(100 + 0.77*m.x306*(3115.6025 + m.x1)/(0.00222345064966968 + m.x306) - 
                       m.x1) + 5.9081550015561e-7*log(100 + 0.77*m.x307*(3115.6025 + m.x1)/(9.37971848687272e-5 + m.x307
                       ) - m.x1) + 2.75262012741516e-6*log(100 + 0.77*m.x308*(3115.6025 + m.x1)/(0.000497933292970139 + 
                       m.x308) - m.x1) + 1.26689317687422e-5*log(100 + 0.77*m.x309*(3115.6025 + m.x1)/(
                       0.00315076332727193 + m.x309) - m.x1) + 9.28242828710157e-6*log(100 + 0.77*m.x310*(3115.6025 + 
                       m.x1)/(0.000609464003265626 + m.x310) - m.x1) + 2.87510652270804e-6*log(100 + 0.77*m.x311*(
                       3115.6025 + m.x1)/(0.00508664437731854 + m.x311) - m.x1) + 6.81148956417702e-6*log(100 + 0.77*
                       m.x312*(3115.6025 + m.x1)/(0.000794723140654341 + m.x312) - m.x1) + 6.02763261502767e-6*log(100
                        + 0.77*m.x313*(3115.6025 + m.x1)/(0.000232975909860184 + m.x313) - m.x1) + 4.41639974662077e-6*
                       log(100 + 0.77*m.x314*(3115.6025 + m.x1)/(0.000137592682829811 + m.x314) - m.x1) + 
                       1.36792006511358e-6*log(100 + 0.77*m.x315*(3115.6025 + m.x1)/(0.000457451982621508 + m.x315) - 
                       m.x1) + 3.24077489419752e-6*log(100 + 0.77*m.x316*(3115.6025 + m.x1)/(0.000208875321100784 + 
                       m.x316) - m.x1) + 3.83847756451445e-5*log(100 + 0.77*m.x317*(3115.6025 + m.x1)/(
                       0.000242893359006603 + m.x317) - m.x1) + 1.1889164588399e-5*log(100 + 0.77*m.x318*(3115.6025 + 
                       m.x1)/(0.00382908295406458 + m.x318) - m.x1) + 2.81669288763827e-5*log(100 + 0.77*m.x319*(
                       3115.6025 + m.x1)/(0.000663271526491096 + m.x319) - m.x1) + 7.43161450573641e-6*log(100 + 0.77*
                       m.x320*(3115.6025 + m.x1)/(0.000371778844197042 + m.x320) - m.x1) + 1.76064312469634e-5*log(100
                        + 0.77*m.x321*(3115.6025 + m.x1)/(0.000106078954747077 + m.x321) - m.x1) + 3.43597058154303e-6*
                       log(100 + 0.77*m.x322*(3115.6025 + m.x1)/(0.000748168669679125 + m.x322) - m.x1) + 
                       5.0704482491619e-7*log(100 + 0.77*m.x323*(3115.6025 + m.x1)/(0.000281861749261525 + m.x323) - 
                       m.x1) + 3.7150771570866e-7*log(100 + 0.77*m.x324*(3115.6025 + m.x1)/(0.000199998903052942 + 
                       m.x324) - m.x1) + 1.1506954173354e-7*log(100 + 0.77*m.x325*(3115.6025 + m.x1)/(
                       0.000209976479990677 + m.x325) - m.x1) + 2.7261428086884e-7*log(100 + 0.77*m.x326*(3115.6025 + 
                       m.x1)/(8.50638265588891e-5 + m.x326) - m.x1) + 3.11549846886372e-6*log(100 + 0.77*m.x327*(
                       3115.6025 + m.x1)/(0.000352980579470926 + m.x327) - m.x1) + 9.6498350947404e-7*log(100 + 0.77*
                       m.x328*(3115.6025 + m.x1)/(0.00175720721660966 + m.x328) - m.x1) + 2.28616749032928e-6*log(100 + 
                       0.77*m.x329*(3115.6025 + m.x1)/(0.000270055052776176 + m.x329) - m.x1) + 6.1143773793045e-7*log(
                       100 + 0.77*m.x330*(3115.6025 + m.x1)/(0.000216928385876834 + m.x330) - m.x1) + 
                       1.44857331120219e-6*log(100 + 0.77*m.x331*(3115.6025 + m.x1)/(5.49153629810655e-5 + m.x331) - 
                       m.x1) + 2.8892571796587e-7*log(100 + 0.77*m.x332*(3115.6025 + m.x1)/(0.000122326481861876 + 
                       m.x332) - m.x1) + 1.27634251944324e-6*log(100 + 0.77*m.x333*(3115.6025 + m.x1)/(
                       0.000203689954501239 + m.x333) - m.x1) + 3.9532986058659e-7*log(100 + 0.77*m.x334*(3115.6025 + 
                       m.x1)/(0.000182000650852623 + m.x334) - m.x1) + 9.3658620830067e-7*log(100 + 0.77*m.x335*(
                       3115.6025 + m.x1)/(0.000205854216716901 + m.x335) - m.x1) + 2.5090006388625e-7*log(100 + 0.77*
                       m.x336*(3115.6025 + m.x1)/(0.000216143341872927 + m.x336) - m.x1) + 5.9441362496415e-7*log(100 + 
                       0.77*m.x337*(3115.6025 + m.x1)/(0.000402695015355116 + m.x337) - m.x1) + 1.1887608883575e-7*log(
                       100 + 0.77*m.x338*(3115.6025 + m.x1)/(0.000145142061072707 + m.x338) - m.x1) + 
                       3.60319297075146e-6*log(100 + 0.77*m.x339*(3115.6025 + m.x1)/(0.000145974547679888 + m.x339) - 
                       m.x1) + 8.53641805279629e-6*log(100 + 0.77*m.x340*(3115.6025 + m.x1)/(4.42583673718464e-5 + 
                       m.x340) - m.x1) + 1.68183660262029e-6*log(100 + 0.77*m.x341*(3115.6025 + m.x1)/(
                       0.000345956283445014 + m.x341) - m.x1) + 9.2466530012889e-7*log(100 + 0.77*m.x342*(3115.6025 + 
                       m.x1)/(1.45943088413546e-5 + m.x342) - m.x1) + 1.9937603495584e-7*log(337.116032640652 - 
                       0.923894003602625*m.x1) + 9.1762802938952e-7*log(140.874328942254 - 0.986880762567672*m.x1) + 
                       6.7233895742168e-7*log(297.292766602765 - 0.936675886412735*m.x1) + 2.0824789184096e-7*log(
                       125.483573075406 - 0.991820659703731*m.x1) + 4.9336549127248e-7*log(254.25882364464 - 
                       0.950488284803777*m.x1) + 4.3658966196808e-7*log(555.572368624705 - 0.853777120597154*m.x1) + 
                       3.1988586492248e-7*log(781.652769600945 - 0.781213177996569*m.x1) + 9.908031842192e-8*log(
                       355.861242670046 - 0.917877443393358*m.x1) + 2.3473375136448e-7*log(597.242366314084 - 
                       0.840402501181045*m.x1) + 2.7802617203068e-6*log(540.385754980185 - 0.858651495182654*m.x1) + 
                       8.6114842762496e-7*log(133.73528945573 - 0.98917214585117*m.x1) + 2.04016912480032e-6*log(
                       282.505104930273 - 0.941422211296122*m.x1) + 5.3828198766584e-7*log(407.270363915862 - 
                       0.901376904173154*m.x1) + 1.27525785951384e-6*log(915.333422034018 - 0.738306339774083*m.x1) + 
                       2.4887204156872e-7*log(263.204514879424 - 0.9476170291687*m.x1) + 3.672594911656e-8*log(
                       489.383061907709 - 0.875021585100247*m.x1) + 2.690881119984e-8*log(614.577491492312 - 
                       0.834838529147312*m.x1) + 8.33464405296e-9*log(595.172961948805 - 0.841066707980622*m.x1) + 
                       1.974582466016e-8*log(1038.00461477439 - 0.698933155056079*m.x1) + 2.2565980879328e-7*log(
                       421.441706101908 - 0.896828396401047*m.x1) + 6.989507342496e-8*log(172.31269511839 - 
                       0.976790140873751*m.x1) + 1.6559023343872e-7*log(503.543143364888 - 0.870476691630307*m.x1) + 
                       4.42872703708e-8*log(582.495725195754 - 0.845135659893791*m.x1) + 1.0492214318056e-7*log(
                       1296.19682040876 - 0.616062440440088*m.x1) + 2.092728432488e-8*log(840.465204251466 - 
                       0.762336432760127*m.x1) + 9.244723172576e-8*log(607.224377039528 - 0.837198623046577*m.x1) + 
                       2.863428168616e-8*log(653.71932095886 - 0.822275363767085*m.x1) + 6.783821812008e-8*log(
                       603.009773354627 - 0.838551364188908*m.x1) + 1.817303427e-8*log(583.894696018611 - 
                       0.844686638934649*m.x1) + 4.30541906196e-8*log(386.497448150095 - 0.908044287372958*m.x1) + 
                       8.610357458e-9*log(755.890960453142 - 0.78948182239129*m.x1) + 2.6098418758704e-7*log(
                       753.168856574781 - 0.790355523024911*m.x1) + 6.1830441735896e-7*log(1425.13050916184 - 
                       0.574679212395729*m.x1) + 1.2181772193496e-7*log(427.078436558279 - 0.895019202045743*m.x1) + 
                       6.697477046136e-8*log(1993.11512355808 - 0.392375913307915*m.x1) + 3.1203660011952e-7*log(
                       825.500626441516 - 0.767139541568119*m.x1) + 1.43614818364956e-6*log(253.821676807616 - 
                       0.950628593728624*m.x1) + 1.05225466264404e-6*log(727.460064530513 - 0.798607150774044*m.x1) + 
                       3.2592163931088e-7*log(197.663258929557 - 0.968653491923454*m.x1) + 7.7214942381144e-7*log(
                       612.435114895593 - 0.835526157494227*m.x1) + 6.8329151895324e-7*log(1253.77546341785 - 
                       0.629678220049622*m.x1) + 5.0064240538644e-7*log(1565.13156178004 - 0.529743745622224*m.x1) + 
                       1.5506721109176e-7*log(869.119411862432 - 0.753139429095197*m.x1) + 3.6737375043744e-7*log(
                       1319.24310584124 - 0.608665384675599*m.x1) + 4.3512923448354e-6*log(1228.83305190904 - 
                       0.637683866311882*m.x1) + 1.34775389436288e-6*log(228.026463886737 - 0.95890795957227*m.x1) + 
                       3.19299878499696e-6*log(689.056338131733 - 0.810933410750655*m.x1) + 8.4244669312452e-7*log(
                       981.250272507588 - 0.717149324245443*m.x1) + 1.99586237556852e-6*log(1708.54761640287 - 
                       0.483712182024867*m.x1) + 3.8950110394716e-7*log(637.181320846455 - 0.827583486389405*m.x1) + 
                       5.747852444268e-8*log(1140.45340526994 - 0.666050657851911*m.x1) + 4.211405830152e-8*log(
                       1345.26734846551 - 0.600312508265894*m.x1) + 1.304426579688e-8*log(1316.09032651707 - 
                       0.609677317142649*m.x1) + 3.090351352848e-8*log(1820.87972878856 - 0.447657482368638*m.x1) + 
                       3.5317243386384e-7*log(1010.3724312703 - 0.707802124542429*m.x1) + 1.0939038426288e-7*log(
                       362.464060898813 - 0.915758168476623*m.x1) + 2.5915959993216e-7*log(1165.73400069356 - 
                       0.657936466319577*m.x1) + 6.93124892274e-8*log(1296.55636528799 - 0.615947039043656*m.x1) + 
                       1.6421005083468e-7*log(2012.48192595162 - 0.386159843577085*m.x1) + 3.275257556364e-8*log(
                       1631.26886676703 - 0.508515971865144*m.x1) + 1.4468599440528e-7*log(1334.31202758498 - 
                       0.603828785095344*m.x1) + 4.481453303148e-8*log(1401.59969118774 - 0.582231786247527*m.x1) + 
                       1.0617127050924e-7*log(1327.97752237393 - 0.605861940868924*m.x1) + 2.8441993185e-8*log(
                       1298.7307493202 - 0.615249137423596*m.x1) + 6.73826383638e-8*log(937.204525824623 - 
                       0.731286476428035*m.x1) + 1.3475775399e-8*log(1534.49263325395 - 0.539577775645657*m.x1) + 
                       4.0845740862312e-7*log(1531.19227562112 - 0.540637075615032*m.x1) + 9.6768705563988e-7*log(
                       2090.8347738355 - 0.361011305570753*m.x1) + 1.9065274216788e-7*log(1021.75459043966 - 
                       0.704148847473432*m.x1) + 1.0481991816708e-7*log(2347.09064275551 - 0.278762087668273*m.x1) + 
                       6.80740688226184e-6*log(100 + 0.77*m.x343*(3115.6025 + m.x1)/(0.000162399166573692 + m.x343) - 
                       m.x1) + 3.133108432017e-5*log(100 + 0.77*m.x344*(3115.6025 + m.x1)/(0.00102761021535188 + m.x344)
                        - m.x1) + 2.29560430719712e-5*log(100 + 0.77*m.x345*(3115.6025 + m.x1)/(0.000198774509727227 + 
                       m.x345) - m.x1) + 7.11032362765496e-6*log(100 + 0.77*m.x346*(3115.6025 + m.x1)/(
                       0.00165899091142481 + m.x346) - m.x1) + 1.68452524472295e-5*log(100 + 0.77*m.x347*(3115.6025 + 
                       m.x1)/(0.000259196116269397 + m.x347) - m.x1) + 1.49067237206526e-5*log(100 + 0.77*m.x348*(
                       3115.6025 + m.x1)/(7.59842616013031e-5 + m.x348) - m.x1) + 1.0922041051192e-5*log(100 + 0.77*
                       m.x349*(3115.6025 + m.x1)/(4.48753624906532e-5 + m.x349) - m.x1) + 3.38295443417492e-6*log(100 + 
                       0.77*m.x350*(3115.6025 + m.x1)/(0.000149196331665396 + m.x350) - m.x1) + 8.01464506449648e-6*log(
                       100 + 0.77*m.x351*(3115.6025 + m.x1)/(6.81239405829684e-5 + m.x351) - m.x1) + 9.49280226858643e-5
                       *log(100 + 0.77*m.x352*(3115.6025 + m.x1)/(7.92188022489237e-5 + m.x352) - m.x1) + 
                       2.9402669855289e-5*log(100 + 0.77*m.x353*(3115.6025 + m.x1)/(0.00124884174097374 + m.x353) - m.x1
                       ) + 6.96586294547383e-5*log(100 + 0.77*m.x354*(3115.6025 + m.x1)/(0.00021632364140928 + m.x354)
                        - m.x1) + 1.83788613724093e-5*log(100 + 0.77*m.x355*(3115.6025 + m.x1)/(0.000121254343302067 + 
                       m.x355) - m.x1) + 4.35418385737073e-5*log(100 + 0.77*m.x356*(3115.6025 + m.x1)/(
                       3.45972725365983e-5 + m.x356) - m.x1) + 8.49737657262922e-6*log(100 + 0.77*m.x357*(3115.6025 + 
                       m.x1)/(0.000244012541695467 + m.x357) - m.x1) + 1.25395451278306e-6*log(100 + 0.77*m.x358*(
                       3115.6025 + m.x1)/(9.1928203667674e-5 + m.x358) - m.x1) + 9.1876251123084e-7*log(100 + 0.77*
                       m.x359*(3115.6025 + m.x1)/(6.52289285131175e-5 + m.x359) - m.x1) + 2.8457438879196e-7*log(100 + 
                       0.77*m.x360*(3115.6025 + m.x1)/(6.8483079625303e-5 + m.x360) - m.x1) + 6.7419267675416e-7*log(100
                        + 0.77*m.x361*(3115.6025 + m.x1)/(2.77432634727662e-5 + m.x361) - m.x1) + 7.70482839509528e-6*
                       log(100 + 0.77*m.x362*(3115.6025 + m.x1)/(0.000115123356345274 + m.x362) - m.x1) + 
                       2.38646637733896e-6*log(100 + 0.77*m.x363*(3115.6025 + m.x1)/(0.000573106862914264 + m.x363) - 
                       m.x1) + 5.65383946468672e-6*log(100 + 0.77*m.x364*(3115.6025 + m.x1)/(8.80774917424437e-5 + 
                       m.x364) - m.x1) + 1.5121249110283e-6*log(100 + 0.77*m.x365*(3115.6025 + m.x1)/(
                       7.07504189214491e-5 + m.x365) - m.x1) + 3.58241510694706e-6*log(100 + 0.77*m.x366*(3115.6025 + 
                       m.x1)/(1.79104496648944e-5 + m.x366) - m.x1) + 7.1453191137938e-7*log(100 + 0.77*m.x367*(
                       3115.6025 + m.x1)/(3.98963455240416e-5 + m.x367) - m.x1) + 3.15647726485976e-6*log(100 + 0.77*
                       m.x368*(3115.6025 + m.x1)/(6.64327517710652e-5 + m.x368) - m.x1) + 9.7767620999266e-7*log(100 + 
                       0.77*m.x369*(3115.6025 + m.x1)/(5.93588627866824e-5 + m.x369) - m.x1) + 2.31623802235458e-6*log(
                       100 + 0.77*m.x370*(3115.6025 + m.x1)/(6.7138618169301e-5 + m.x370) - m.x1) + 6.204920194575e-7*
                       log(100 + 0.77*m.x371*(3115.6025 + m.x1)/(7.04943796210888e-5 + m.x371) - m.x1) + 
                       1.4700231830721e-6*log(100 + 0.77*m.x372*(3115.6025 + m.x1)/(0.000131337542197591 + m.x372) - 
                       m.x1) + 2.939882249705e-7*log(100 + 0.77*m.x373*(3115.6025 + m.x1)/(4.73375652638053e-5 + m.x373)
                        - m.x1) + 8.91092831259804e-6*log(100 + 0.77*m.x374*(3115.6025 + m.x1)/(4.76090777999194e-5 + 
                       m.x374) - m.x1) + 2.11111117090605e-5*log(100 + 0.77*m.x375*(3115.6025 + m.x1)/(
                       1.44347085775828e-5 + m.x375) - m.x1) + 4.15929025203646e-6*log(100 + 0.77*m.x376*(3115.6025 + 
                       m.x1)/(0.000112832407263379 + m.x376) - m.x1) + 2.28675684857286e-6*log(100 + 0.77*m.x377*(
                       3115.6025 + m.x1)/(4.75988174724677e-6 + m.x377) - m.x1) + 8.43089005274e-8*log(268.6379716465 - 
                       0.945873078595071*m.x1) + 3.8803164215845e-7*log(128.327406131493 - 0.990907888239436*m.x1) + 
                       2.8430778199855e-7*log(239.572993467521 - 0.955201925320216*m.x1) + 8.80604873206e-8*log(
                       117.625736786455 - 0.994342751751401*m.x1) + 2.086263885053e-7*log(208.508539802713 - 
                       0.965172534107701*m.x1) + 1.8461794764005e-7*log(433.744528262518 - 0.892879618544882*m.x1) + 
                       1.3526814078655e-7*log(615.400559449551 - 0.834574352970396*m.x1) + 4.18974763537e-8*log(
                       282.426455742256 - 0.941447454949001*m.x1) + 9.92603975628e-8*log(466.371952966359 - 
                       0.882407350434993*m.x1) + 1.17567193504175e-6*log(421.946311777256 - 0.896666435536223*m.x1) + 
                       3.641484651856e-7*log(123.358083734547 - 0.992502867829081*m.x1) + 8.627135946402e-7*log(
                       228.858395401842 - 0.958640938501673*m.x1) + 2.2761994722115e-7*log(320.599393198273 - 
                       0.929195270193077*m.x1) + 5.3926033812615e-7*log(728.407398947384 - 0.798303089387243*m.x1) + 
                       1.0523896817045e-7*log(214.936952702276 - 0.96310923723348*m.x1) + 1.553007306785e-8*log(
                       382.680820667042 - 0.909269292001453*m.x1) + 1.13787611799e-8*log(480.056384794622 - 
                       0.878015123946453*m.x1) + 3.5244189531e-9*log(464.742740831163 - 0.882930270844512*m.x1) + 
                       8.3497937326e-9*log(836.025395487855 - 0.763761456897067*m.x1) + 9.54233560558e-8*log(
                       331.215308112915 - 0.925787930869578*m.x1) + 2.95560938106e-8*log(150.321278984262 - 
                       0.98384862029599*m.x1) + 7.00221093392e-8*log(393.527383487514 - 0.905787922725215*m.x1) + 
                       1.872748183175e-8*log(454.782462930071 - 0.886127173498522*m.x1) + 4.436777235785e-8*log(
                       1075.75197813101 - 0.686817564778881*m.x1) + 8.84939021305e-9*log(664.584532393001 - 
                       0.818788008934708*m.x1) + 3.90925843486e-8*log(474.243770813553 - 0.879880770793594*m.x1) + 
                       1.210840012385e-8*log(511.198542742875 - 0.868019574787581*m.x1) + 2.868632423505e-8*log(
                       470.917477630236 - 0.880948395172287*m.x1) + 7.68471766875e-9*log(455.879896829577 - 
                       0.885774935400271*m.x1) + 1.820605708725e-8*log(305.111286054903 - 0.934166413701715*m.x1) + 
                       3.64100816125e-9*log(594.114163141561 - 0.841406545558504*m.x1) + 1.103607558219e-7*log(
                       591.874012592349 - 0.842125555942278*m.x1) + 2.6145853301935e-7*log(1202.70807178794 - 
                       0.646069075953064*m.x1) + 5.151230037935e-8*log(335.44915647061 - 0.924429012856868*m.x1) + 
                       2.832120350835e-8*log(1828.83738966731 - 0.445103350100885*m.x1) + 8.1546287696304e-7*log(100 + 
                       0.77*m.x378*(3115.6025 + m.x1)/(0.00029817724214172 + m.x378) - m.x1) + 3.75316718979612e-6*log(
                       100 + 0.77*m.x379*(3115.6025 + m.x1)/(0.00188677064343949 + m.x379) - m.x1) + 2.74991656161108e-6
                       *log(100 + 0.77*m.x380*(3115.6025 + m.x1)/(0.00036496514341188 + m.x380) - m.x1) + 
                       8.5174943437776e-7*log(138.743343180511 - 0.987564734852886*m.x1) + 2.01790171520088e-6*log(100
                        + 0.77*m.x381*(3115.6025 + m.x1)/(0.000475903816218067 + m.x381) - m.x1) + 1.78568433201948e-6*
                       log(100 + 0.77*m.x382*(3115.6025 + m.x1)/(0.000139512893129108 + m.x382) - m.x1) + 
                       1.30835708397588e-6*log(100 + 0.77*m.x383*(3115.6025 + m.x1)/(8.23945843435174e-5 + m.x383) - 
                       m.x1) + 4.0524590394552e-7*log(100 + 0.77*m.x384*(3115.6025 + m.x1)/(0.000273935831397647 + 
                       m.x384) - m.x1) + 9.6007857840288e-7*log(100 + 0.77*m.x385*(3115.6025 + m.x1)/(
                       0.000125080744904183 + m.x385) - m.x1) + 1.13714781300258e-5*log(100 + 0.77*m.x386*(3115.6025 + 
                       m.x1)/(0.000145451756180262 + m.x386) - m.x1) + 3.52216139938176e-6*log(100 + 0.77*m.x387*(
                       3115.6025 + m.x1)/(0.00229296857891227 + m.x387) - m.x1) + 8.34444412724592e-6*log(100 + 0.77*
                       m.x388*(3115.6025 + m.x1)/(0.000397186686153369 + m.x388) - m.x1) + 2.20161354084804e-6*log(100
                        + 0.77*m.x389*(3115.6025 + m.x1)/(0.000222632212013906 + m.x389) - m.x1) + 5.21589991103604e-6*
                       log(100 + 0.77*m.x390*(3115.6025 + m.x1)/(6.35232281558983e-5 + m.x390) - m.x1) + 
                       1.01790524151132e-6*log(100 + 0.77*m.x391*(3115.6025 + m.x1)/(0.000448025616546069 + m.x391) - 
                       m.x1) + 1.5021187542636e-7*log(100 + 0.77*m.x392*(3115.6025 + m.x1)/(0.000168787185445507 + 
                       m.x392) - m.x1) + 1.1005904797704e-7*log(100 + 0.77*m.x393*(3115.6025 + m.x1)/(
                       0.000119765282188656 + m.x393) - m.x1) + 3.408931679976e-8*log(782.545765405689 - 
                       0.780926557413634*m.x1) + 8.076189793296e-8*log(100 + 0.77*m.x394*(3115.6025 + m.x1)/(
                       5.09387453448955e-5 + m.x394) - m.x1) + 9.2296547543568e-7*log(100 + 0.77*m.x395*(3115.6025 + 
                       m.x1)/(0.000211375252874563 + m.x395) - m.x1) + 2.8587607168176e-7*log(208.821730508207 - 
                       0.965072010788216*m.x1) + 6.7727642485632e-7*log(100 + 0.77*m.x396*(3115.6025 + m.x1)/(
                       0.00016171698498591 + m.x396) - m.x1) + 1.811382442098e-7*log(100 + 0.77*m.x397*(3115.6025 + m.x1
                       )/(0.000129903159230785 + m.x397) - m.x1) + 4.2913940361036e-7*log(100 + 0.77*m.x398*(3115.6025
                        + m.x1)/(3.28849500848452e-5 + m.x398) - m.x1) + 8.559415622028e-8*log(100 + 0.77*m.x399*(
                       3115.6025 + m.x1)/(7.32527298684983e-5 + m.x399) - m.x1) + 3.7811608384656e-7*log(100 + 0.77*
                       m.x400*(3115.6025 + m.x1)/(0.000121975593403019 + m.x400) - m.x1) + 1.1711635116396e-7*log(100 + 
                       0.77*m.x401*(3115.6025 + m.x1)/(0.000108987394306425 + m.x401) - m.x1) + 2.7746337983148e-7*log(
                       100 + 0.77*m.x402*(3115.6025 + m.x1)/(0.000123271617886315 + m.x402) - m.x1) + 7.4329067745e-8*
                       log(100 + 0.77*m.x403*(3115.6025 + m.x1)/(0.000129433051569077 + m.x403) - m.x1) + 
                       1.760948559126e-7*log(100 + 0.77*m.x404*(3115.6025 + m.x1)/(0.000241145733370368 + m.x404) - m.x1
                       ) + 3.5217005223e-8*log(976.093683297966 - 0.718804409966301*m.x1) + 1.06744482354024e-6*log(100
                        + 0.77*m.x405*(3115.6025 + m.x1)/(8.74138939182849e-5 + m.x405) - m.x1) + 2.52891125621076e-6*
                       log(100 + 0.77*m.x406*(3115.6025 + m.x1)/(2.65032246506635e-5 + m.x406) - m.x1) + 
                       4.9824358286676e-7*log(100 + 0.77*m.x407*(3115.6025 + m.x1)/(0.000207168895825208 + m.x407) - 
                       m.x1) + 2.7393181440516e-7*log(100 + 0.77*m.x408*(3115.6025 + m.x1)/(8.73950551754048e-6 + m.x408
                       ) - m.x1) + 1.27625335484744e-6*log(100 + 0.77*m.x409*(3115.6025 + m.x1)/(0.000344826568804241 + 
                       m.x409) - m.x1) + 5.87395496790682e-6*log(100 + 0.77*m.x410*(3115.6025 + m.x1)/(
                       0.00218195272860088 + m.x410) - m.x1) + 4.30380135804238e-6*log(100 + 0.77*m.x411*(3115.6025 + 
                       m.x1)/(0.000422063324591525 + m.x411) - m.x1) + 1.33304421798136e-6*log(133.575365188442 - 
                       0.989223475976656*m.x1) + 3.15814969207268e-6*log(100 + 0.77*m.x412*(3115.6025 + m.x1)/(
                       0.000550358165662165 + m.x412) - m.x1) + 2.79471412349978e-6*log(100 + 0.77*m.x413*(3115.6025 + 
                       m.x1)/(0.000161339449973174 + m.x413) - m.x1) + 2.04766539953518e-6*log(100 + 0.77*m.x414*(
                       3115.6025 + m.x1)/(9.52850781070775e-5 + m.x414) - m.x1) + 6.3423665142772e-7*log(100 + 0.77*
                       m.x415*(3115.6025 + m.x1)/(0.000316792630231961 + m.x415) - m.x1) + 1.50258649561968e-6*log(100
                        + 0.77*m.x416*(3115.6025 + m.x1)/(0.000144649416498018 + m.x416) - m.x1) + 1.77971156296763e-5*
                       log(100 + 0.77*m.x417*(3115.6025 + m.x1)/(0.000168207438132896 + m.x417) - m.x1) + 
                       5.51241562217536e-6*log(100 + 0.77*m.x418*(3115.6025 + m.x1)/(0.00265169964603287 + m.x418) - 
                       m.x1) + 1.30596071416471e-5*log(100 + 0.77*m.x419*(3115.6025 + m.x1)/(0.000459325873353868 + 
                       m.x419) - m.x1) + 3.44567085389494e-6*log(100 + 0.77*m.x420*(3115.6025 + m.x1)/(
                       0.000257462646118264 + m.x420) - m.x1) + 8.16322845351294e-6*log(100 + 0.77*m.x421*(3115.6025 + 
                       m.x1)/(7.34613300701079e-5 + m.x421) - m.x1) + 1.59308904929402e-6*log(100 + 0.77*m.x422*(
                       3115.6025 + m.x1)/(0.000518118468667565 + m.x422) - m.x1) + 2.3509152331346e-7*log(100 + 0.77*
                       m.x423*(3115.6025 + m.x1)/(0.000195193655951906 + m.x423) - m.x1) + 1.7224969177644e-7*log(100 + 
                       0.77*m.x424*(3115.6025 + m.x1)/(0.000138502358605079 + m.x424) - m.x1) + 5.335203619836e-8*log(
                       713.834896128684 - 0.802980355764677*m.x1) + 1.2639771360856e-7*log(100 + 0.77*m.x425*(3115.6025
                        + m.x1)/(5.89080261468274e-5 + m.x425) - m.x1) + 1.44450203401048e-6*log(100 + 0.77*m.x426*(
                       3115.6025 + m.x1)/(0.00024444455470623 + m.x426) - m.x1) + 4.4741496622536e-7*log(194.68097059979
                        - 0.969610702713266*m.x1) + 1.05998241465152e-6*log(100 + 0.77*m.x427*(3115.6025 + m.x1)/(
                       0.000187017334554172 + m.x427) - m.x1) + 2.834933366003e-7*log(100 + 0.77*m.x428*(3115.6025 + 
                       m.x1)/(0.000150226289413102 + m.x428) - m.x1) + 6.7163155923746e-7*log(100 + 0.77*m.x429*(
                       3115.6025 + m.x1)/(3.80297450657429e-5 + m.x429) - m.x1) + 1.3396051753858e-7*log(100 + 0.77*
                       m.x430*(3115.6025 + m.x1)/(8.47129959170147e-5 + m.x430) - m.x1) + 5.9177668801816e-7*log(100 + 
                       0.77*m.x431*(3115.6025 + m.x1)/(0.000141058469281279 + m.x431) - m.x1) + 1.8329483818706e-7*log(
                       100 + 0.77*m.x432*(3115.6025 + m.x1)/(0.000126038288340387 + m.x432) - m.x1) + 4.3424854688178e-7
                       *log(100 + 0.77*m.x433*(3115.6025 + m.x1)/(0.000142557254609265 + m.x433) - m.x1) + 
                       1.163299087575e-7*log(100 + 0.77*m.x434*(3115.6025 + m.x1)/(0.000149682634200548 + m.x434) - m.x1
                       ) + 2.756001002361e-7*log(100 + 0.77*m.x435*(3115.6025 + m.x1)/(0.000278872576668224 + m.x435) - 
                       m.x1) + 5.51169431905e-8*log(100 + 0.77*m.x436*(3115.6025 + m.x1)/(0.000100513140244829 + m.x436)
                        - m.x1) + 1.67062177279164e-6*log(100 + 0.77*m.x437*(3115.6025 + m.x1)/(0.000101089650199842 + 
                       m.x437) - m.x1) + 3.95791343300686e-6*log(100 + 0.77*m.x438*(3115.6025 + m.x1)/(
                       3.06496094500486e-5 + m.x438) - m.x1) + 7.7978417182286e-7*log(100 + 0.77*m.x439*(3115.6025 + 
                       m.x1)/(0.000239580120190449 + m.x439) - m.x1) + 4.2872141333526e-7*log(100 + 0.77*m.x440*(
                       3115.6025 + m.x1)/(1.0106786416741e-5 + m.x440) - m.x1) + 9.273520298852e-8*log(358.539933407436
                        - 0.917017676867496*m.x1) + 4.2681369198781e-7*log(144.935947672355 - 0.98557712427296*m.x1) + 
                       3.1272308985079e-7*log(315.477181856525 - 0.930839321814473*m.x1) + 9.686174432188e-8*log(
                       128.034017517148 - 0.991002055776644*m.x1) + 2.2947767514194e-7*log(268.780873913804 - 
                       0.945827211939327*m.x1) + 2.0306969658749e-7*log(592.240115646012 - 0.842008049600033*m.x1) + 
                       1.4878759437319e-7*log(829.685004457404 - 0.765796501813885*m.x1) + 4.608494417626e-8*log(
                       378.760424559288 - 0.910527602748012*m.x1) + 1.0918103615544e-7*log(636.338426930868 - 
                       0.827854026009137*m.x1) + 1.29317515543415e-6*log(576.130636396736 - 0.847178631934999*m.x1) + 
                       4.0054349689888e-7*log(137.098673227772 - 0.988092616684005*m.x1) + 9.4893801033396e-7*log(
                       299.450015262575 - 0.935983484651018*m.x1) + 2.5036955621227e-7*log(434.053417972084 - 
                       0.892780475695444*m.x1) + 5.9315702858127e-7*log(968.024268423618 - 0.721394411378339*m.x1) + 
                       1.1575713850541e-7*log(278.501752054383 - 0.942707148278902*m.x1) + 1.708223531993e-8*log(
                       521.879880291747 - 0.864591237074772*m.x1) + 1.251601813302e-8*log(654.639033329393 - 
                       0.821980168096093*m.x1) + 3.87666907038e-9*log(634.152014126405 - 0.828555788446567*m.x1) + 
                       9.18431875948e-9*log(1093.6490504942 - 0.681073227250844*m.x1) + 1.0496049928684e-7*log(
                       449.2537526685 - 0.887901697129688*m.x1) + 3.251009492388e-8*log(179.393118324343 - 
                       0.974517571376855*m.x1) + 7.702051008416e-8*log(536.964765902902 - 0.859749513648515*m.x1) + 
                       2.059921097615e-8*log(620.749808952132 - 0.83285742999881*m.x1) + 4.880213536193e-8*log(
                       1354.01132259096 - 0.597505996804482*m.x1) + 9.73384770289e-9*log(890.73349355316 - 
                       0.746202060900529*m.x1) + 4.299971559628e-8*log(646.879588813031 - 0.824470679808149*m.x1) + 
                       1.331858126873e-8*log(695.864610493836 - 0.808748192205573*m.x1) + 3.155339571849e-8*log(
                       642.42996136499 - 0.825898855401166*m.x1) + 8.45277127875e-9*log(622.229472198603 - 
                       0.832382509579254*m.x1) + 2.002567213005e-8*log(411.739691140382 - 0.89994240563731*m.x1) + 
                       4.00491085525e-9*log(802.850834872808 - 0.774409336597718*m.x1) + 1.2139082622462e-7*log(
                       800.012103104391 - 0.775320470726163*m.x1) + 2.8759015929463e-7*log(1482.01660573493 - 
                       0.556420754658229*m.x1) + 5.666072742263e-8*log(455.294784271713 - 0.885962736173272*m.x1) + 
                       3.115178278683e-8*log(2030.55035493416 - 0.380360506536326*m.x1) + 1.4513664887868e-7*log(
                       244.798336775476 - 0.953524771925984*m.x1) + 6.6799130162379e-7*log(124.108480080755 - 
                       0.992262016710811*m.x1) + 4.8943205843361e-7*log(219.621784363451 - 0.961605569271609*m.x1) + 
                       1.5159495555492e-7*log(114.990579362077 - 0.995188545598459*m.x1) + 3.5914754795646e-7*log(
                       192.815416502162 - 0.970209480669578*m.x1) + 3.1781733690891e-7*log(389.595030572337 - 
                       0.907050071190937*m.x1) + 2.3286230197521e-7*log(552.485529158339 - 0.854767888664122*m.x1) + 
                       7.212594727734e-8*log(256.774613290639 - 0.949680803860364*m.x1) + 1.7087545180296e-7*log(
                       418.572098212241 - 0.897749440690126*m.x1) + 2.02390357085985e-6*log(379.146592813175 - 
                       0.910403656174632*m.x1) + 6.2687673069792e-7*log(119.873056718799 - 0.993621440245089*m.x1) + 
                       1.48514995789164e-6*log(210.363968705052 - 0.964577005986787*m.x1) + 3.9184470620493e-7*log(
                       290.040074396276 - 0.939003748264974*m.x1) + 9.2832948667593e-7*log(655.767806524211 - 
                       0.821617871174448*m.x1) + 1.8116748144219e-7*log(198.35403749885 - 0.968431776037267*m.x1) + 
                       2.673481385487e-8*log(344.486646749132 - 0.921528292922755*m.x1) + 1.958838575418e-8*log(
                       430.76167441788 - 0.893837010845292*m.x1) + 6.06724026642e-9*log(417.122283752445 - 
                       0.898214780687702*m.x1) + 1.437405865332e-8*log(755.551665629421 - 0.789590724224473*m.x1) + 
                       1.6427003597556e-7*log(299.31993900287 - 0.936025234604585*m.x1) + 5.088042167292e-8*log(
                       142.88596479926 - 0.986235097449286*m.x1) + 1.2054212821344e-7*log(354.043606427674 - 
                       0.918460841385358*m.x1) + 3.223911043785e-8*log(408.265351965367 - 0.90105754762831*m.x1) + 
                       7.637852893287e-8*log(982.98447692449 - 0.716592704966538*m.x1) + 1.523410733751e-8*log(
                       597.250560461113 - 0.840399871144951*m.x1) + 6.729736306452e-8*log(425.581399511489 - 
                       0.895499698850707*m.x1) + 2.084444947407e-8*log(458.581981464026 - 0.884907660247408*m.x1) + 
                       4.938312493791e-8*log(422.618704492563 - 0.896450620869458*m.x1) + 1.322913907125e-8*log(
                       409.240663257227 - 0.900744506638049*m.x1) + 3.134148468795e-8*log(276.523652448133 - 
                       0.943342049427636*m.x1) + 6.26794703475e-9*log(533.199969835709 - 0.860957882195913*m.x1) + 
                       1.8998457063858e-7*log(531.173474307521 - 0.861608316751729*m.x1) + 4.5009738077217e-7*log(
                       1106.40538864313 - 0.676978886541806*m.x1) + 8.867773872417e-8*log(303.024440850973 - 
                       0.934836218403672*m.x1) + 4.875457447197e-8*log(1747.34237541307 - 0.471260414185356*m.x1) + 
                       3.14345285277512e-6*log(100 + 0.77*m.x441*(3115.6025 + m.x1)/(0.000157156288200091 + m.x441) - 
                       m.x1) + 1.44677390510339e-5*log(100 + 0.77*m.x442*(3115.6025 + m.x1)/(0.000994434950427626 + 
                       m.x442) - m.x1) + 1.06004004654177e-5*log(100 + 0.77*m.x443*(3115.6025 + m.x1)/(
                       0.000192357293430744 + m.x443) - m.x1) + 3.28333056596728e-6*log(100 + 0.77*m.x444*(3115.6025 + 
                       m.x1)/(0.00160543221555821 + m.x444) - m.x1) + 7.77862375156964e-6*log(100 + 0.77*m.x445*(
                       3115.6025 + m.x1)/(0.000250828254899286 + m.x445) - m.x1) + 6.88347031632794e-6*log(100 + 0.77*
                       m.x446*(3115.6025 + m.x1)/(7.35311933356927e-5 + m.x446) - m.x1) + 5.04346540383214e-6*log(100 + 
                       0.77*m.x447*(3115.6025 + m.x1)/(4.34266107976881e-5 + m.x447) - m.x1) + 1.56214516787956e-6*log(
                       100 + 0.77*m.x448*(3115.6025 + m.x1)/(0.000144379692287175 + m.x448) - m.x1) + 
                       3.70091862110064e-6*log(100 + 0.77*m.x449*(3115.6025 + m.x1)/(6.59246341312025e-5 + m.x449) - 
                       m.x1) + 4.38348652991099e-5*log(100 + 0.77*m.x450*(3115.6025 + m.x1)/(7.66613103980958e-5 + 
                       m.x450) - m.x1) + 1.35772560733293e-5*log(100 + 0.77*m.x451*(3115.6025 + m.x1)/(
                       0.00120852425970865 + m.x451) - m.x1) + 3.21662302940158e-5*log(100 + 0.77*m.x452*(3115.6025 + 
                       m.x1)/(0.000209339870709147 + m.x452) - m.x1) + 8.48679757374262e-6*log(100 + 0.77*m.x453*(
                       3115.6025 + m.x1)/(0.000117339780268179 + m.x453) - m.x1) + 2.01062929022566e-5*log(100 + 0.77*
                       m.x454*(3115.6025 + m.x1)/(3.34803376668285e-5 + m.x454) - m.x1) + 3.92382930685946e-6*log(100 + 
                       0.77*m.x455*(3115.6025 + m.x1)/(0.000236134865321051 + m.x455) - m.x1) + 5.7903794479058e-7*log(
                       100 + 0.77*m.x456*(3115.6025 + m.x1)/(8.89604027786557e-5 + m.x456) - m.x1) + 4.2425650279212e-7*
                       log(100 + 0.77*m.x457*(3115.6025 + m.x1)/(6.31230843400847e-5 + m.x457) - m.x1) + 
                       1.3140777240828e-7*log(100 + 0.77*m.x458*(3115.6025 + m.x1)/(6.62721787647855e-5 + m.x458) - m.x1
                       ) + 3.1132161331288e-7*log(100 + 0.77*m.x459*(3115.6025 + m.x1)/(2.68476027428296e-5 + m.x459) - 
                       m.x1) + 3.55785473346904e-6*log(100 + 0.77*m.x460*(3115.6025 + m.x1)/(0.000111406725478175 + 
                       m.x460) - m.x1) + 1.10199737897928e-6*log(100 + 0.77*m.x461*(3115.6025 + m.x1)/(
                       0.000554604738545467 + m.x461) - m.x1) + 2.61077060645696e-6*log(100 + 0.77*m.x462*(3115.6025 + 
                       m.x1)/(8.52340068502479e-5 + m.x462) - m.x1) + 6.982531597619e-7*log(100 + 0.77*m.x463*(3115.6025
                        + m.x1)/(6.84663195069478e-5 + m.x463) - m.x1) + 1.65425002244258e-6*log(100 + 0.77*m.x464*(
                       3115.6025 + m.x1)/(1.73322305077971e-5 + m.x464) - m.x1) + 3.2994904140034e-7*log(100 + 0.77*
                       m.x465*(3115.6025 + m.x1)/(3.86083359144677e-5 + m.x465) - m.x1) + 1.45756491929368e-6*log(100 + 
                       0.77*m.x466*(3115.6025 + m.x1)/(6.42880434889493e-5 + m.x466) - m.x1) + 4.5146105184338e-7*log(
                       100 + 0.77*m.x467*(3115.6025 + m.x1)/(5.74425272256582e-5 + m.x467) - m.x1) + 1.06956806681394e-6
                       *log(100 + 0.77*m.x468*(3115.6025 + m.x1)/(6.49711217673195e-5 + m.x468) - m.x1) + 
                       2.865242877975e-7*log(100 + 0.77*m.x469*(3115.6025 + m.x1)/(6.821854615363e-5 + m.x469) - m.x1)
                        + 6.788118660153e-7*log(100 + 0.77*m.x470*(3115.6025 + m.x1)/(0.000127097454183856 + m.x470) - 
                       m.x1) + 1.357547948065e-7*log(100 + 0.77*m.x471*(3115.6025 + m.x1)/(4.58093240639472e-5 + m.x471)
                        - m.x1) + 4.11479488586172e-6*log(100 + 0.77*m.x472*(3115.6025 + m.x1)/(4.60720711166307e-5 + 
                       m.x472) - m.x1) + 9.74846743772878e-6*log(100 + 0.77*m.x473*(3115.6025 + m.x1)/(
                       1.39686998964588e-5 + m.x473) - m.x1) + 1.92063336809678e-6*log(100 + 0.77*m.x474*(3115.6025 + 
                       m.x1)/(0.000109189737166214 + m.x474) - m.x1) + 1.05595456002198e-6*log(100 + 0.77*m.x475*(
                       3115.6025 + m.x1)/(4.60621420325593e-6 + m.x475) - m.x1) + 6.944196785648e-8*log(438.328502947439
                        - 0.891408322163229*m.x1) + 3.1960659732844e-7*log(160.672269148748 - 0.98052631259965*m.x1) + 
                       2.3417328105796e-7*log(383.737721647126 - 0.908930063560058*m.x1) + 7.253200423312e-8*log(
                       137.946787402231 - 0.987820401542806*m.x1) + 1.7183745576056e-7*log(323.76453259191 - 
                       0.928179370573778*m.x1) + 1.5206263520876e-7*log(723.154378888364 - 0.799989126055598*m.x1) + 
                       1.1141511543556e-7*log(994.136523516822 - 0.713013286028361*m.x1) + 3.450932449624e-8*log(
                       463.72887675709 - 0.883255685936479*m.x1) + 8.175693543456e-8*log(774.830149075393 - 
                       0.783403001802896*m.x1) + 9.683553244346e-7*log(704.117904521328 - 0.806099171983163*m.x1) + 
                       2.9993495178112e-7*log(150.148891888383 - 0.983903950555829*m.x1) + 7.1058369085104e-7*log(
                       363.245448869307 - 0.915507370125263*m.x1) + 1.8748171260148e-7*log(532.438202944837 - 
                       0.861202382863399*m.x1) + 4.4416780235748e-7*log(1144.15218362596 - 0.664863478692818*m.x1) + 
                       8.668125191084e-8*log(336.316624140497 - 0.924150585917011*m.x1) + 1.279151819132e-8*log(
                       639.374735800217 - 0.826879476505679*m.x1) + 9.37224377448e-9*log(796.090332382495 - 
                       0.776579222676033*m.x1) + 2.90292704712e-9*log(772.282933330948 - 0.784220569430488*m.x1) + 
                       6.87740089552e-9*log(1275.69246176927 - 0.622643626146379*m.x1) + 7.859651332816e-8*log(
                       551.137259264743 - 0.855200636389031*m.x1) + 2.434420688112e-8*log(206.64947926604 - 
                       0.965769227856879*m.x1) + 5.767449267584e-8*log(657.476234564291 - 0.821069525215655*m.x1) + 
                       1.54250996426e-8*log(756.635274889761 - 0.789242923354388*m.x1) + 3.654401139932e-8*log(
                       1535.04726916935 - 0.5393997568145*m.x1) + 7.28889911836e-9*log(1061.02290920942 - 
                       0.691545083427869*m.x1) + 3.219904385872e-8*log(787.089182577275 - 0.779468278582626*m.x1) + 
                       9.97321904252e-9*log(843.590944378369 - 0.761333178934614*m.x1) + 2.362781145276e-8*log(
                       781.918774588875 - 0.781127799650669*m.x1) + 6.329603565e-9*log(758.365707096016 - 
                       0.788687514823853*m.x1) + 1.49956223262e-8*log(504.84109778787 - 0.870060093420817*m.x1) + 
                       2.998957051e-9*log(964.386178144426 - 0.722562111776317*m.x1) + 9.089986953288e-8*log(
                       961.226291333032 - 0.723576325499472*m.x1) + 2.1535324185412e-7*log(1656.41268033145 - 
                       0.500445682550503*m.x1) + 4.242868172612e-8*log(558.546332794591 - 0.852822581573037*m.x1) + 
                       2.332707568692e-8*log(2135.61678696677 - 0.34663783747549*m.x1) + 1.0868132303496e-7*log(
                       952.855197136797 - 0.726263155477377*m.x1) + 5.0020569578538e-7*log(292.358397193926 - 
                       0.938259647309332*m.x1) + 3.6649684319742e-7*log(845.268759609223 - 0.760794658622458*m.x1) + 
                       1.1351743658424e-7*log(222.900839352747 - 0.960553106709618*m.x1) + 2.6893710843012e-7*log(
                       716.158724669567 - 0.802234487657021*m.x1) + 2.3798819199402e-7*log(1397.99930308635 - 
                       0.583387385558217*m.x1) + 1.7437210559262e-7*log(1698.31981573055 - 0.486994950180406*m.x1) + 
                       5.400940035348e-8*log(1000.01299130032 - 0.711127144332334*m.x1) + 1.2795507075312e-7*log(
                       1462.69503446476 - 0.562622306772202*m.x1) + 1.5155408332467e-6*log(1373.12671852222 - 
                       0.591370619800755*m.x1) + 4.6941825513024e-7*log(260.562902565146 - 0.948464894810828*m.x1) + 
                       1.11211099040808e-6*log(802.513881672884 - 0.774517486851136*m.x1) + 2.9342141646246e-7*log(
                       1119.29289935334 - 0.672842444004541*m.x1) + 6.9515231062446e-7*log(1830.61326417666 - 
                       0.444533356172151*m.x1) + 1.3566195531018e-7*log(744.203496969942 - 0.793233091522445*m.x1) + 
                       2.001958129314e-8*log(1283.98039223831 - 0.619983488831353*m.x1) + 1.466818819596e-8*log(
                       1488.17838576561 - 0.554443037657848*m.x1) + 4.54327493724e-9*log(1459.59879689333 - 
                       0.563616091303903*m.x1) + 1.076359226904e-8*log(1931.71652847139 - 0.412082726062971*m.x1) + 
                       1.2300879883032e-7*log(1149.82151209152 - 0.663043821510761*m.x1) + 3.810031158024e-8*log(
                       424.287526310851 - 0.895914987129825*m.x1) + 9.026443752768e-8*log(1309.64325245314 - 
                       0.611746603601347*m.x1) + 2.41413123627e-8*log(1440.37165493351 - 0.569787334894773*m.x1) + 
                       5.719382140914e-8*log(2099.27686813522 - 0.358301687029966*m.x1) + 1.140761450322e-8*log(
                       1759.78384606747 - 0.467267134986742*m.x1) + 5.039365667544e-8*log(1477.46685899388 - 
                       0.55788106506081*m.x1) + 1.560875467554e-8*log(1542.89054316818 - 0.536882338755287*m.x1) + 
                       3.697910483202e-8*log(1471.26264848806 - 0.559872400767407*m.x1) + 9.9062528175e-9*log(
                       1442.51559884057 - 0.56909920349577*m.x1) + 2.34691516449e-8*log(1072.76969944935 - 
                       0.687774772471984*m.x1) + 4.6935683145e-9*log(1669.57680330368 - 0.496220457101417*m.x1) + 
                       1.4226437397276e-7*log(1666.47040697755 - 0.497217502239919*m.x1) + 3.3704222341374e-7*log(
                       2166.0852268286 - 0.336858528381396*m.x1) + 6.640372395774e-8*log(1161.70370083739 - 
                       0.659230052345448*m.x1) + 3.650843324934e-8*log(2377.97102001738 - 0.268850561001483*m.x1) + 
                       2.34922704076588e-6*log(100 + 0.77*m.x476*(3115.6025 + m.x1)/(0.000455053041852194 + m.x476) - 
                       m.x1) + 1.08123154344204e-5*log(100 + 0.77*m.x477*(3115.6025 + m.x1)/(0.00287943075201725 + 
                       m.x477) - m.x1) + 7.92209986363301e-6*log(100 + 0.77*m.x478*(3115.6025 + m.x1)/(
                       0.000556979122506819 + m.x478) - m.x1) + 2.45376320581172e-6*log(100 + 0.77*m.x479*(3115.6025 + 
                       m.x1)/(0.00464860058445214 + m.x479) - m.x1) + 5.81327416474486e-6*log(100 + 0.77*m.x480*(
                       3115.6025 + m.x1)/(0.000726284399317671 + m.x480) - m.x1) + 5.14429048527031e-6*log(100 + 0.77*
                       m.x481*(3115.6025 + m.x1)/(0.000212912849887539 + m.x481) - m.x1) + 3.76918180763861e-6*log(100
                        + 0.77*m.x482*(3115.6025 + m.x1)/(0.000125743688446365 + m.x482) - m.x1) + 1.16745306574094e-6*
                       log(100 + 0.77*m.x483*(3115.6025 + m.x1)/(0.000418057838534042 + m.x483) - m.x1) + 
                       2.76584332820136e-6*log(100 + 0.77*m.x484*(3115.6025 + m.x1)/(0.000190887718448796 + m.x484) - 
                       m.x1) + 3.27595340894288e-5*log(100 + 0.77*m.x485*(3115.6025 + m.x1)/(0.0002219762434489 + m.x485
                       ) - m.x1) + 1.01468221731747e-5*log(100 + 0.77*m.x486*(3115.6025 + m.x1)/(0.0034993358956939 + 
                       m.x486) - m.x1) + 2.40391001695772e-5*log(100 + 0.77*m.x487*(3115.6025 + m.x1)/(
                       0.000606152932460819 + m.x487) - m.x1) + 6.34252056051713e-6*log(100 + 0.77*m.x488*(3115.6025 + 
                       m.x1)/(0.00033976256726883 + m.x488) - m.x1) + 1.50262304503281e-5*log(100 + 0.77*m.x489*(
                       3115.6025 + m.x1)/(9.6943810979624e-5 + m.x489) - m.x1) + 2.93243332817479e-6*log(100 + 0.77*
                       m.x490*(3115.6025 + m.x1)/(0.000683739034450168 + m.x490) - m.x1) + 4.3273803083467e-7*log(100 + 
                       0.77*m.x491*(3115.6025 + m.x1)/(0.000257588813991856 + m.x491) - m.x1) + 3.1706371791138e-7*log(
                       100 + 0.77*m.x492*(3115.6025 + m.x1)/(0.000182775706075957 + m.x492) - m.x1) + 9.820624223322e-8*
                       log(100 + 0.77*m.x493*(3115.6025 + m.x1)/(0.000191894049436265 + m.x493) - m.x1) + 
                       2.3266299404612e-7*log(100 + 0.77*m.x494*(3115.6025 + m.x1)/(7.77384311788353e-5 + m.x494) - m.x1
                       ) + 2.65892600857796e-6*log(100 + 0.77*m.x495*(3115.6025 + m.x1)/(0.00032258314250264 + m.x495)
                        - m.x1) + 8.2356636564972e-7*log(100 + 0.77*m.x496*(3115.6025 + m.x1)/(0.00160588275652981 + 
                       m.x496) - m.x1) + 1.95113246267104e-6*log(100 + 0.77*m.x497*(3115.6025 + m.x1)/(
                       0.000246798868379189 + m.x497) - m.x1) + 5.2183229112685e-7*log(100 + 0.77*m.x498*(3115.6025 + 
                       m.x1)/(0.000198247281816642 + m.x498) - m.x1) + 1.23628667803267e-6*log(100 + 0.77*m.x499*(
                       3115.6025 + m.x1)/(5.01862464746856e-5 + m.x499) - m.x1) + 2.4658401014291e-7*log(100 + 0.77*
                       m.x500*(3115.6025 + m.x1)/(0.000111792158620858 + m.x500) - m.x1) + 1.08929609650532e-6*log(100
                        + 0.77*m.x501*(3115.6025 + m.x1)/(0.000186148897250143 + m.x501) - m.x1) + 3.3739475682187e-7*
                       log(100 + 0.77*m.x502*(3115.6025 + m.x1)/(0.000166327399591117 + m.x502) - m.x1) + 
                       7.9933065395931e-7*log(100 + 0.77*m.x503*(3115.6025 + m.x1)/(0.000188126780871317 + m.x503) - 
                       m.x1) + 2.1413096879625e-7*log(100 + 0.77*m.x504*(3115.6025 + m.x1)/(0.000197529843021106 + 
                       m.x504) - m.x1) + 5.0730304093095e-7*log(100 + 0.77*m.x505*(3115.6025 + m.x1)/(
                       0.000368016347296246 + m.x505) - m.x1) + 1.0145494454975e-7*log(100 + 0.77*m.x506*(3115.6025 + 
                       m.x1)/(0.000132642940980837 + m.x506) - m.x1) + 3.07514948237178e-6*log(100 + 0.77*m.x507*(
                       3115.6025 + m.x1)/(0.000133403736790733 + m.x507) - m.x1) + 7.28541650959397e-6*log(100 + 0.77*
                       m.x508*(3115.6025 + m.x1)/(4.04469935718446e-5 + m.x508) - m.x1) + 1.43536552162597e-6*log(100 + 
                       0.77*m.x509*(3115.6025 + m.x1)/(0.000316163753964881 + m.x509) - m.x1) + 7.8915674018577e-7*log(
                       100 + 0.77*m.x510*(3115.6025 + m.x1)/(1.33374986684954e-5 + m.x510) - m.x1) + 1.7351096111916e-7*
                       log(1756.34518082976 - 0.468370826885087*m.x1) + 7.9858404930423e-7*log(725.200186930332 - 
                       0.799332492854807*m.x1) + 5.8511635425957e-7*log(1648.94114589024 - 0.502843785145813*m.x1) + 
                       1.8123187108404e-7*log(529.899097644463 - 0.862017347320634*m.x1) + 4.2936113456502e-7*log(
                       1498.32765799351 - 0.551185474400694*m.x1) + 3.7995083952567e-7*log(2083.00079499621 - 
                       0.363525740207165*m.x1) + 2.7838703825877e-7*log(2234.54546771311 - 0.314885173024123*m.x1) + 
                       8.622661836558e-8*log(1799.10804348668 - 0.454645435838916*m.x1) + 2.0428171728552e-7*log(
                       2119.22302589951 - 0.351899664382889*m.x1) + 2.41957807697445e-6*log(2068.46991167032 - 
                       0.368189648175491*m.x1) + 7.4943155217504e-7*log(639.346029121697 - 0.826888690350679*m.x1) + 
                       1.77549777117468e-6*log(1601.95443552502 - 0.517924884344193*m.x1) + 4.6845060919041e-7*log(
                       1897.31212561191 - 0.423125342333654*m.x1) + 1.10981852421741e-6*log(2289.83683300728 - 
                       0.297138568540986*m.x1) + 2.1658584562503e-7*log(1533.35146924954 - 0.539944049586061*m.x1) + 
                       3.196148790219e-8*log(2013.37867265892 - 0.385872019084936*m.x1) + 2.341792831266e-8*log(
                       2132.89963200708 - 0.347509949678408*m.x1) + 7.25338980954e-9*log(2117.53920216988 - 
                       0.352440113214097*m.x1) + 1.718419676484e-8*log(2328.32819868025 - 0.28478417940663*m.x1) + 
                       1.9638493823172e-7*log(1920.39808889742 - 0.415715551358873*m.x1) + 6.082757825004e-8*log(
                       1029.01261405065 - 0.701819274425846*m.x1) + 1.4410819516128e-7*log(2029.74189826765 - 
                       0.380619992997292*m.x1) + 3.854187816045e-8*log(2106.97326999007 - 0.355831409818786*m.x1) + 
                       9.131058258819e-8*log(2385.97240833931 - 0.266282393745893*m.x1) + 1.821238554387e-8*log(
                       2260.97728055389 - 0.306401480755683*m.x1) + 8.045404269924e-8*log(2127.19009521653 - 
                       0.3493425123338*m.x1) + 2.491955333259e-8*log(2161.20757843742 - 0.338424083804843*m.x1) + 
                       5.903755899867e-8*log(2123.85717760185 - 0.350412262924476*m.x1) + 1.581544463625e-8*log(
                       2108.16088165946 - 0.355450227793995*m.x1) + 3.746876597415e-8*log(1860.5916573208 - 
                       0.434911335024029*m.x1) + 7.49333488575e-9*log(2221.71201851028 - 0.319004263698504*m.x1) + 
                       2.2712668167546e-7*log(2220.3062861031 - 0.319455454890955*m.x1) + 5.3809172072229e-7*log(
                       2407.06872653783 - 0.259511209617455*m.x1) + 1.0601429614629e-7*log(1929.17750011989 - 
                       0.412897665822297*m.x1) + 5.828612649489e-8*log(2467.89538756556 - 0.239987967795776*m.x1))
                       , sense=minimize)

m.c2 = Constraint(expr=   m.x1 - m.x2 - m.x3 - m.x4 - m.x5 - m.x6 - m.x7 - m.x8 - m.x9 - m.x10 - m.x11 - m.x12 - m.x13
                        - m.x14 - m.x15 - m.x16 - m.x17 - m.x18 - m.x19 - m.x20 - m.x21 - m.x22 - m.x23 - m.x24 - m.x25
                        - m.x26 - m.x27 - m.x28 - m.x29 - m.x30 - m.x31 - m.x32 - m.x33 - m.x34 - m.x35 - m.x36 - m.x37
                        - m.x38 - m.x39 - m.x40 - m.x41 - m.x42 - m.x43 - m.x44 - m.x45 - m.x46 - m.x47 - m.x48 - m.x49
                        - m.x50 - m.x51 - m.x52 - m.x53 - m.x54 - m.x55 - m.x56 - m.x57 - m.x58 - m.x59 - m.x60 - m.x61
                        - m.x62 - m.x63 - m.x64 - m.x65 - m.x66 - m.x67 - m.x68 - m.x69 - m.x70 - m.x71 - m.x72 - m.x73
                        - m.x74 - m.x75 - m.x76 - m.x77 - m.x78 - m.x79 - m.x80 - m.x81 - m.x82 - m.x83 - m.x84 - m.x85
                        - m.x86 - m.x87 - m.x88 - m.x89 - m.x90 - m.x91 - m.x92 - m.x93 - m.x94 - m.x95 - m.x96 - m.x97
                        - m.x98 - m.x99 - m.x100 - m.x101 - m.x102 - m.x103 - m.x104 - m.x105 - m.x106 - m.x107 - m.x108
                        - m.x109 - m.x110 - m.x111 - m.x112 - m.x113 - m.x114 - m.x115 - m.x116 - m.x117 - m.x118
                        - m.x119 - m.x120 - m.x121 - m.x122 - m.x123 - m.x124 - m.x125 - m.x126 - m.x127 - m.x128
                        - m.x129 - m.x130 - m.x131 - m.x132 - m.x133 - m.x134 - m.x135 - m.x136 - m.x137 - m.x138
                        - m.x139 - m.x140 - m.x141 - m.x142 - m.x143 - m.x144 - m.x145 - m.x146 - m.x147 - m.x148
                        - m.x149 - m.x150 - m.x151 - m.x152 - m.x153 - m.x154 - m.x155 - m.x156 - m.x157 - m.x158
                        - m.x159 - m.x160 - m.x161 - m.x162 - m.x163 - m.x164 - m.x165 - m.x166 - m.x167 - m.x168
                        - m.x169 - m.x170 - m.x171 - m.x172 - m.x173 - m.x174 - m.x175 - m.x176 - m.x177 - m.x178
                        - m.x179 - m.x180 - m.x181 - m.x182 - m.x183 - m.x184 - m.x185 - m.x186 - m.x187 - m.x188
                        - m.x189 - m.x190 - m.x191 - m.x192 - m.x193 - m.x194 - m.x195 - m.x196 - m.x197 - m.x198
                        - m.x199 - m.x200 - m.x201 - m.x202 - m.x203 - m.x204 - m.x205 - m.x206 - m.x207 - m.x208
                        - m.x209 - m.x210 - m.x211 - m.x212 - m.x213 - m.x214 - m.x215 - m.x216 - m.x217 - m.x218
                        - m.x219 - m.x220 - m.x221 - m.x222 - m.x223 - m.x224 - m.x225 - m.x226 - m.x227 - m.x228
                        - m.x229 - m.x230 - m.x231 - m.x232 - m.x233 - m.x234 - m.x235 - m.x236 - m.x237 - m.x238
                        - m.x239 - m.x240 - m.x241 - m.x242 - m.x243 - m.x244 - m.x245 - m.x246 - m.x247 - m.x248
                        - m.x249 - m.x250 - m.x251 - m.x252 - m.x253 - m.x254 - m.x255 - m.x256 - m.x257 - m.x258
                        - m.x259 - m.x260 - m.x261 - m.x262 - m.x263 - m.x264 - m.x265 - m.x266 - m.x267 - m.x268
                        - m.x269 - m.x270 - m.x271 - m.x272 - m.x273 - m.x274 - m.x275 - m.x276 - m.x277 - m.x278
                        - m.x279 - m.x280 - m.x281 - m.x282 - m.x283 - m.x284 - m.x285 - m.x286 - m.x287 - m.x288
                        - m.x289 - m.x290 - m.x291 - m.x292 - m.x293 - m.x294 - m.x295 - m.x296 - m.x297 - m.x298
                        - m.x299 - m.x300 - m.x301 - m.x302 - m.x303 - m.x304 - m.x305 - m.x306 - m.x307 - m.x308
                        - m.x309 - m.x310 - m.x311 - m.x312 - m.x313 - m.x314 - m.x315 - m.x316 - m.x317 - m.x318
                        - m.x319 - m.x320 - m.x321 - m.x322 - m.x323 - m.x324 - m.x325 - m.x326 - m.x327 - m.x328
                        - m.x329 - m.x330 - m.x331 - m.x332 - m.x333 - m.x334 - m.x335 - m.x336 - m.x337 - m.x338
                        - m.x339 - m.x340 - m.x341 - m.x342 - m.x343 - m.x344 - m.x345 - m.x346 - m.x347 - m.x348
                        - m.x349 - m.x350 - m.x351 - m.x352 - m.x353 - m.x354 - m.x355 - m.x356 - m.x357 - m.x358
                        - m.x359 - m.x360 - m.x361 - m.x362 - m.x363 - m.x364 - m.x365 - m.x366 - m.x367 - m.x368
                        - m.x369 - m.x370 - m.x371 - m.x372 - m.x373 - m.x374 - m.x375 - m.x376 - m.x377 - m.x378
                        - m.x379 - m.x380 - m.x381 - m.x382 - m.x383 - m.x384 - m.x385 - m.x386 - m.x387 - m.x388
                        - m.x389 - m.x390 - m.x391 - m.x392 - m.x393 - m.x394 - m.x395 - m.x396 - m.x397 - m.x398
                        - m.x399 - m.x400 - m.x401 - m.x402 - m.x403 - m.x404 - m.x405 - m.x406 - m.x407 - m.x408
                        - m.x409 - m.x410 - m.x411 - m.x412 - m.x413 - m.x414 - m.x415 - m.x416 - m.x417 - m.x418
                        - m.x419 - m.x420 - m.x421 - m.x422 - m.x423 - m.x424 - m.x425 - m.x426 - m.x427 - m.x428
                        - m.x429 - m.x430 - m.x431 - m.x432 - m.x433 - m.x434 - m.x435 - m.x436 - m.x437 - m.x438
                        - m.x439 - m.x440 - m.x441 - m.x442 - m.x443 - m.x444 - m.x445 - m.x446 - m.x447 - m.x448
                        - m.x449 - m.x450 - m.x451 - m.x452 - m.x453 - m.x454 - m.x455 - m.x456 - m.x457 - m.x458
                        - m.x459 - m.x460 - m.x461 - m.x462 - m.x463 - m.x464 - m.x465 - m.x466 - m.x467 - m.x468
                        - m.x469 - m.x470 - m.x471 - m.x472 - m.x473 - m.x474 - m.x475 - m.x476 - m.x477 - m.x478
                        - m.x479 - m.x480 - m.x481 - m.x482 - m.x483 - m.x484 - m.x485 - m.x486 - m.x487 - m.x488
                        - m.x489 - m.x490 - m.x491 - m.x492 - m.x493 - m.x494 - m.x495 - m.x496 - m.x497 - m.x498
                        - m.x499 - m.x500 - m.x501 - m.x502 - m.x503 - m.x504 - m.x505 - m.x506 - m.x507 - m.x508
                        - m.x509 - m.x510 == 0)

m.c3 = Constraint(expr=   m.x1 <= 100)
