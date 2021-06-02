#  MINLP written by GAMS Convert at 04/21/18 13:55:15
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        564      366       99       99        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#       1557      270     1287        0        0        0        0        0
#  FX      3        3        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       4946     4550      396        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(22.9,57),initialize=22.9)
m.x2 = Var(within=Reals,bounds=(25,57),initialize=25)
m.x3 = Var(within=Reals,bounds=(23.5,57),initialize=23.5)
m.x4 = Var(within=Reals,bounds=(23.8,57),initialize=23.8)
m.x5 = Var(within=Reals,bounds=(22.2,57),initialize=22.2)
m.x6 = Var(within=Reals,bounds=(27,57),initialize=27)
m.x7 = Var(within=Reals,bounds=(26.5,57),initialize=26.5)
m.x8 = Var(within=Reals,bounds=(25.2,57),initialize=25.2)
m.x9 = Var(within=Reals,bounds=(24.3,57),initialize=24.3)
m.x10 = Var(within=Reals,bounds=(25.2,57),initialize=25.2)
m.x11 = Var(within=Reals,bounds=(48,57),initialize=48)
m.x12 = Var(within=Reals,bounds=(23.2,57),initialize=23.2)
m.x13 = Var(within=Reals,bounds=(23.2,57),initialize=23.2)
m.x14 = Var(within=Reals,bounds=(39.2,57),initialize=39.2)
m.x15 = Var(within=Reals,bounds=(57,57),initialize=57)
m.x16 = Var(within=Reals,bounds=(24,57),initialize=24)
m.x17 = Var(within=Reals,bounds=(23.5,57),initialize=23.5)
m.x18 = Var(within=Reals,bounds=(22.8,57),initialize=22.8)
m.x19 = Var(within=Reals,bounds=(22.7,57),initialize=22.7)
m.x20 = Var(within=Reals,bounds=(21.8,57),initialize=21.8)
m.x21 = Var(within=Reals,bounds=(22.1,57),initialize=22.1)
m.x22 = Var(within=Reals,bounds=(22,57),initialize=22)
m.x23 = Var(within=Reals,bounds=(38.7,57),initialize=38.7)
m.x24 = Var(within=Reals,bounds=(23.2,57),initialize=23.2)
m.x25 = Var(within=Reals,bounds=(21.6,57),initialize=21.6)
m.x26 = Var(within=Reals,bounds=(23.8,57),initialize=23.8)
m.x27 = Var(within=Reals,bounds=(24.3,57),initialize=24.3)
m.x28 = Var(within=Reals,bounds=(23.6,57),initialize=23.6)
m.x29 = Var(within=Reals,bounds=(23.2,57),initialize=23.2)
m.x30 = Var(within=Reals,bounds=(22.8,57),initialize=22.8)
m.x31 = Var(within=Reals,bounds=(21.8,57),initialize=21.8)
m.x32 = Var(within=Reals,bounds=(23.8,57),initialize=23.8)
m.x33 = Var(within=Reals,bounds=(22.9,57),initialize=22.9)
m.x34 = Var(within=Reals,bounds=(23.7,57),initialize=23.7)
m.x35 = Var(within=Reals,bounds=(22.1,57),initialize=22.1)
m.x36 = Var(within=Reals,bounds=(26.7,57),initialize=26.7)
m.x37 = Var(within=Reals,bounds=(26.7,57),initialize=26.7)
m.x38 = Var(within=Reals,bounds=(24.2,57),initialize=24.2)
m.x39 = Var(within=Reals,bounds=(22.9,57),initialize=22.9)
m.x40 = Var(within=Reals,bounds=(22.9,57),initialize=22.9)
m.x41 = Var(within=Reals,bounds=(48.5,57),initialize=48.5)
m.x42 = Var(within=Reals,bounds=(53.08,53.08),initialize=53.08)
m.x43 = Var(within=Reals,bounds=(47.3,57),initialize=47.3)
m.x44 = Var(within=Reals,bounds=(21.1,57),initialize=21.1)
m.x45 = Var(within=Reals,bounds=(22.5,57.4),initialize=22.5)
m.x46 = Var(within=Reals,bounds=(22.8,57),initialize=22.8)
m.x47 = Var(within=Reals,bounds=(23.3,57),initialize=23.3)
m.x48 = Var(within=Reals,bounds=(21.8,57),initialize=21.8)
m.x49 = Var(within=Reals,bounds=(21.8,57),initialize=21.8)
m.x50 = Var(within=Reals,bounds=(21.6,57),initialize=21.6)
m.x51 = Var(within=Reals,bounds=(21.8,57),initialize=21.8)
m.x52 = Var(within=Reals,bounds=(21.6,57),initialize=21.6)
m.x53 = Var(within=Reals,bounds=(23.3,57),initialize=23.3)
m.x54 = Var(within=Reals,bounds=(22.5,57),initialize=22.5)
m.x55 = Var(within=Reals,bounds=(22.8,57),initialize=22.8)
m.x56 = Var(within=Reals,bounds=(23.2,57),initialize=23.2)
m.x57 = Var(within=Reals,bounds=(23.6,57),initialize=23.6)
m.x58 = Var(within=Reals,bounds=(23.8,57),initialize=23.8)
m.x59 = Var(within=Reals,bounds=(23.1,57),initialize=23.1)
m.x60 = Var(within=Reals,bounds=(23,57),initialize=23)
m.x61 = Var(within=Reals,bounds=(24.2,57),initialize=24.2)
m.x62 = Var(within=Reals,bounds=(55,55),initialize=55)
m.x63 = Var(within=Reals,bounds=(24.2,57),initialize=24.2)
m.x64 = Var(within=Reals,bounds=(22.1,57),initialize=22.1)
m.x65 = Var(within=Reals,bounds=(22.1,57),initialize=22.1)
m.x66 = Var(within=Reals,bounds=(23.3,57),initialize=23.3)
m.x67 = Var(within=Reals,bounds=(22.1,57),initialize=22.1)
m.x68 = Var(within=Reals,bounds=(21.5,57),initialize=21.5)
m.x69 = Var(within=Reals,bounds=(39.2,57),initialize=39.2)
m.x70 = Var(within=Reals,bounds=(22.1,57),initialize=22.1)
m.x71 = Var(within=Reals,bounds=(21.5,57),initialize=21.5)
m.x72 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x87 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x88 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x92 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x93 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x105 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x111 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x117 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x119 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x121 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x123 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x124 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x125 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x126 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x127 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x128 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x129 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x130 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x131 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x132 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x133 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x134 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x135 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x136 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x137 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x138 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x139 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x140 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x141 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x142 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x143 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x144 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x145 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x146 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x147 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x148 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x149 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x150 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x151 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x152 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x153 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x154 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x155 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x156 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x157 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x158 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x159 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x160 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x161 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x162 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x163 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x164 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x165 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x166 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x167 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x168 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x169 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x170 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x171 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x172 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x173 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x174 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x175 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x176 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x177 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x178 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x179 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x180 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x181 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x182 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x183 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x184 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x185 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x186 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x187 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x188 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x189 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x190 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x191 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x192 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x193 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x194 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x195 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x196 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x197 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x198 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x199 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x200 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x201 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x202 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x203 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x204 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x205 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x206 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x207 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x208 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x209 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x210 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x211 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x212 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x213 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x214 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x215 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x216 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x217 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x218 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x219 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x220 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x221 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x222 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x223 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x224 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x225 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x226 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x227 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x228 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x229 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x230 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x231 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x232 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x233 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x234 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x235 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x236 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x237 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x238 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x239 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x240 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x241 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x242 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x243 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x244 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x245 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x246 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x247 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x248 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x249 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x250 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x251 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x252 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x253 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x254 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x255 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x256 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x257 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x258 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x259 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x260 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x261 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x262 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x263 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x264 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x265 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x266 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x267 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x268 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x269 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.b270 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b271 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b272 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b273 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b274 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b275 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b276 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b277 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b278 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b279 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b280 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b281 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b282 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b283 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b284 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b285 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b286 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b287 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b288 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b289 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b290 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b291 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b292 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b293 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b294 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b295 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b296 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b297 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b298 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b299 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b300 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b301 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b302 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b303 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b304 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b305 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b306 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b307 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b308 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b309 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b310 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b311 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b312 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b313 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b314 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b315 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b316 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b317 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b318 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b319 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b320 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b321 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b322 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b323 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b324 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b325 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b326 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b327 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b328 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b329 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b330 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b331 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b332 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b333 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b334 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b335 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b336 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b337 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b338 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b339 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b340 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b341 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b342 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b343 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b344 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b345 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b346 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b347 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b348 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b349 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b350 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b351 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b352 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b353 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b354 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b355 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b356 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b357 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b358 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b359 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b360 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b361 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b362 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b363 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b364 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b365 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b366 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b367 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b368 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b369 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b370 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b371 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b372 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b373 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b374 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b375 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b376 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b377 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b378 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b379 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b380 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b381 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b382 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b383 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b384 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b385 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b386 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b387 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b388 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b389 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b390 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b391 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b392 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b393 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b394 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b395 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b396 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b397 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b398 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b399 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b400 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b401 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b402 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b403 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b404 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b405 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b406 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b407 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b408 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b409 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b410 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b411 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b412 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b413 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b414 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b415 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b416 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b417 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b418 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b419 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b420 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b421 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b422 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b423 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b424 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b425 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b426 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b427 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b428 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b429 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b430 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b431 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b432 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b433 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b434 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b435 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b436 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b437 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b438 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b439 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b440 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b441 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b442 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b443 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b444 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b445 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b446 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b447 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b448 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b449 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b450 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b451 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b452 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b453 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b454 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b455 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b456 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b457 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b458 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b459 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b460 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b461 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b462 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b463 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b464 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b465 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b466 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b467 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b468 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b469 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b470 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b471 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b472 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b473 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b474 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b475 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b476 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b477 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b478 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b479 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b480 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b481 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b482 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b483 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b484 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b485 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b486 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b487 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b488 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b489 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b490 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b491 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b492 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b493 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b494 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b495 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b496 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b497 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b498 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b499 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b500 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b501 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b502 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b503 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b504 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b505 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b506 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b507 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b508 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b509 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b510 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b511 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b512 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b513 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b514 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b515 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b516 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b517 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b518 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b519 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b520 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b521 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b522 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b523 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b524 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b525 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b526 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b527 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b528 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b529 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b530 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b531 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b532 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b533 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b534 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b535 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b536 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b537 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b538 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b539 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b540 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b541 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b542 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b543 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b544 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b545 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b546 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b547 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b548 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b549 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b550 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b551 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b552 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b553 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b554 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b555 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b556 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b557 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b558 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b559 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b560 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b561 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b562 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b563 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b564 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b565 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b566 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b567 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b568 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b569 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b570 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b571 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b572 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b573 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b574 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b575 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b576 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b577 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b578 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b579 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b580 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b581 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b582 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b583 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b584 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b585 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b586 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b587 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b588 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b589 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b590 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b591 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b592 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b593 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b594 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b595 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b596 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b597 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b598 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b599 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b600 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b601 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b602 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b603 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b604 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b605 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b606 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b607 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b608 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b609 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b610 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b611 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b612 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b613 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b614 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b615 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b616 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b617 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b618 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b619 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b620 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b621 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b622 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b623 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b624 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b625 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b626 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b627 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b628 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b629 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b630 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b631 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b632 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b633 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b634 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b635 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b636 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b637 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b638 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b639 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b640 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b641 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b642 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b643 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b644 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b645 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b646 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b647 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b648 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b649 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b650 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b651 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b652 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b653 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b654 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b655 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b656 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b657 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b658 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b659 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b660 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b661 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b662 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b663 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b664 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b665 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b666 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b667 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b668 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b669 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b670 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b671 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b672 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b673 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b674 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b675 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b676 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b677 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b678 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b679 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b680 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b681 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b682 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b683 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b684 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b685 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b686 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b687 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b688 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b689 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b690 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b691 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b692 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b693 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b694 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b695 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b696 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b697 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b698 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b699 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b700 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b701 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b702 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b703 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b704 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b705 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b706 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b707 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b708 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b709 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b710 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b711 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b712 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b713 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b714 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b715 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b716 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b717 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b718 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b719 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b720 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b721 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b722 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b723 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b724 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b725 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b726 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b727 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b728 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b729 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b730 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b731 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b732 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b733 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b734 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b735 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b736 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b737 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b738 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b739 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b740 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b741 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b742 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b743 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b744 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b745 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b746 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b747 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b748 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b749 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b750 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b751 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b752 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b753 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b754 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b755 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b756 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b757 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b758 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b759 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b760 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b761 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b762 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b763 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b764 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b765 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b766 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b767 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b768 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b769 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b770 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b771 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b772 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b773 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b774 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b775 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b776 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b777 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b778 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b779 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b780 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b781 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b782 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b783 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b784 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b785 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b786 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b787 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b788 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b789 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b790 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b791 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b792 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b793 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b794 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b795 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b796 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b797 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b798 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b799 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b800 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b801 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b802 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b803 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b804 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b805 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b806 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b807 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b808 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b809 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b810 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b811 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b812 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b813 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b814 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b815 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b816 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b817 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b818 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b819 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b820 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b821 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b822 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b823 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b824 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b825 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b826 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b827 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b828 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b829 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b830 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b831 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b832 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b833 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b834 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b835 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b836 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b837 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b838 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b839 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b840 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b841 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b842 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b843 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b844 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b845 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b846 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b847 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b848 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b849 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b850 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b851 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b852 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b853 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b854 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b855 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b856 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b857 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b858 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b859 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b860 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b861 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b862 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b863 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b864 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b865 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b866 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b867 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b868 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b869 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b870 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b871 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b872 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b873 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b874 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b875 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b876 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b877 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b878 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b879 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b880 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b881 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b882 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b883 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b884 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b885 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b886 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b887 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b888 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b889 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b890 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b891 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b892 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b893 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b894 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b895 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b896 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b897 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b898 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b899 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b900 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b901 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b902 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b903 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b904 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b905 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b906 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b907 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b908 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b909 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b910 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b911 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b912 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b913 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b914 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b915 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b916 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b917 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b918 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b919 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b920 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b921 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b922 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b923 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b924 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b925 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b926 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b927 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b928 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b929 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b930 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b931 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b932 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b933 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b934 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b935 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b936 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b937 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b938 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b939 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b940 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b941 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b942 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b943 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b944 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b945 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b946 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b947 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b948 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b949 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b950 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b951 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b952 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b953 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b954 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b955 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b956 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b957 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b958 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b959 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b960 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b961 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b962 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b963 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b964 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b965 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b966 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b967 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b968 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b969 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b970 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b971 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b972 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b973 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b974 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b975 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b976 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b977 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b978 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b979 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b980 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b981 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b982 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b983 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b984 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b985 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b986 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b987 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b988 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b989 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b990 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b991 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b992 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b993 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b994 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b995 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b996 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b997 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b998 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b999 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1000 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1001 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1002 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1003 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1004 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1005 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1006 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1007 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1008 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1009 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1010 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1011 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1012 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1013 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1014 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1015 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1016 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1017 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1018 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1019 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1020 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1021 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1022 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1023 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1024 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1025 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1026 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1027 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1028 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1029 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1030 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1031 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1032 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1033 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1034 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1035 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1036 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1037 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1038 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1039 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1040 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1041 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1042 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1043 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1044 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1045 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1046 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1047 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1048 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1049 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1050 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1051 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1052 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1053 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1054 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1055 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1056 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1057 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1058 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1059 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1060 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1061 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1062 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1063 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1064 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1065 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1066 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1067 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1068 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1069 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1070 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1071 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1072 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1073 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1074 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1075 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1076 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1077 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1078 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1079 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1080 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1081 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1082 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1083 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1084 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1085 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1086 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1087 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1088 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1089 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1090 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1091 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1092 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1093 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1094 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1095 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1096 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1097 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1098 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1099 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1100 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1101 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1102 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1103 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1104 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1105 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1106 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1109 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1128 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1129 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1130 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1131 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1132 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1133 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1134 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1135 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1136 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1137 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1138 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1139 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1140 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1141 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1142 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1143 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1144 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1145 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1146 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1147 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1148 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1149 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1150 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1151 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1152 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1153 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1154 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1155 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1156 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1157 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1158 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1159 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1160 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1161 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1162 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1163 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1164 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1165 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1166 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1167 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1168 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1169 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1170 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1171 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1172 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1173 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1174 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1175 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1176 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1177 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1178 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1179 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1180 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1181 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1182 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1183 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1184 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1185 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1186 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1187 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1188 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1189 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1190 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1191 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1192 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1193 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1194 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1195 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1196 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1197 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1198 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1199 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1200 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1201 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1202 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1203 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1204 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1205 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1206 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1207 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1208 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1209 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1210 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1211 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1212 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1213 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1214 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1215 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1216 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1217 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1218 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1219 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1220 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1221 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1222 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1223 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1224 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1225 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1226 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1227 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1228 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1229 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1230 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1231 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1232 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1233 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1234 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1235 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1236 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1237 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1238 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1239 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1240 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1241 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1242 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1243 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1244 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1245 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1246 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1247 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1248 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1249 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1250 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1251 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1252 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1253 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1254 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1255 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1256 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1257 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1258 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1259 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1260 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1261 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1262 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1263 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1264 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1265 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1266 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1267 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1268 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1269 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1270 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1271 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1272 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1273 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1274 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1275 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1276 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1277 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1278 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1279 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1280 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1281 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1282 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1283 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1284 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1285 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1286 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1287 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1288 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1289 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1290 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1291 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1292 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1293 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1294 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1295 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1296 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1297 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1298 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1299 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1300 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1301 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1302 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1303 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1304 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1305 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1306 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1307 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1308 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1309 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1310 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1311 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1312 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1313 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1314 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1315 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1316 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1317 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1318 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1319 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1320 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1321 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1322 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1323 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1324 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1325 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1326 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1327 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1328 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1329 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1330 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1331 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1332 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1333 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1334 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1335 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1336 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1337 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1338 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1339 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1340 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1341 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1342 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1343 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1344 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1345 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1346 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1347 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1348 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1349 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1350 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1351 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1352 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1353 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1354 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1355 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1356 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1357 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1358 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1359 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1360 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1361 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1362 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1363 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1364 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1365 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1366 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1367 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1368 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1369 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1370 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1371 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1372 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1373 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1374 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1375 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1376 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1377 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1378 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1379 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1380 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1381 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1382 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1383 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1384 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1385 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1386 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1387 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1388 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1389 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1390 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1391 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1392 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1393 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1394 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1395 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1396 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1397 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1398 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1399 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1400 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1401 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1402 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1403 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1404 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1405 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1406 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1407 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1408 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1409 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1410 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1411 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1412 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1413 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1414 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1415 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1416 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1417 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1418 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1419 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1420 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1421 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1422 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1423 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1424 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1425 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1426 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1427 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1428 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1429 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1430 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1431 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1432 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1433 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1434 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1435 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1436 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1437 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1438 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1439 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1440 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1441 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1442 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1443 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1444 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1445 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1446 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1447 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1448 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1449 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1450 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1451 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1452 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1453 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1454 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1455 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1456 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1457 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1458 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1459 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1460 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1461 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1462 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1463 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1464 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1465 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1466 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1467 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1468 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1469 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1470 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1471 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1472 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1473 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1474 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1475 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1476 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1477 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1478 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1479 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1480 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1481 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1482 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1483 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1484 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1485 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1486 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1487 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1488 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1489 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1490 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1491 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1492 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1493 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1494 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1495 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1496 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1497 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1498 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1499 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1500 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1501 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1502 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1503 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1504 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1505 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1506 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1507 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1508 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1509 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1510 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1511 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1512 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1513 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1514 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1515 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1516 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1517 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1518 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1519 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1520 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1521 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1522 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1523 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1524 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1525 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1526 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1527 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1528 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1529 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1530 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1531 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1532 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1533 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1534 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1535 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1536 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1537 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1538 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1539 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1540 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1541 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1542 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1543 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1544 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1545 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1546 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1547 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1548 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1549 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1550 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1551 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1552 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1553 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1554 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1555 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1556 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   27072.872*m.b270 + 37139.68*m.b271 + 39583.08*m.b272 + 54145.744*m.b273 + 73302*m.b274
                        + 90308.064*m.b275 + 120313.016*m.b276 + 138687.384*m.b277 + 165467.048*m.b278
                        + 187164.44*m.b279 + 240430.56*m.b280 + 312364.256*m.b281 + 382245.496*m.b282 + 5367.706*m.b283
                        + 7363.64*m.b284 + 7848.09*m.b285 + 10735.412*m.b286 + 14533.5*m.b287 + 17905.272*m.b288
                        + 23854.318*m.b289 + 27497.382*m.b290 + 32806.954*m.b291 + 37108.87*m.b292 + 47669.88*m.b293
                        + 61932.088*m.b294 + 75787.358*m.b295 + 7468.197*m.b296 + 10245.18*m.b297 + 10919.205*m.b298
                        + 14936.394*m.b299 + 20220.75*m.b300 + 24911.964*m.b301 + 33188.991*m.b302 + 38257.659*m.b303
                        + 45644.973*m.b304 + 51630.315*m.b305 + 66324.06*m.b306 + 86167.356*m.b307 + 105444.471*m.b308
                        + 12275.809*m.b309 + 16840.46*m.b310 + 17948.385*m.b311 + 24551.618*m.b312 + 33237.75*m.b313
                        + 40948.908*m.b314 + 54554.227*m.b315 + 62885.823*m.b316 + 75028.681*m.b317 + 84867.055*m.b318
                        + 109019.82*m.b319 + 141637.132*m.b320 + 173323.787*m.b321 + 39078.329*m.b322 + 53609.26*m.b323
                        + 57136.185*m.b324 + 78156.658*m.b325 + 105807.75*m.b326 + 130355.148*m.b327 + 173665.787*m.b328
                        + 200188.263*m.b329 + 238843.361*m.b330 + 270162.455*m.b331 + 347049.42*m.b332
                        + 450882.092*m.b333 + 551752.147*m.b334 + 20302.161*m.b335 + 27851.34*m.b336 + 29683.665*m.b337
                        + 40604.322*m.b338 + 54969.75*m.b339 + 67722.732*m.b340 + 90223.683*m.b341 + 104002.767*m.b342
                        + 124085.049*m.b343 + 140356.095*m.b344 + 180300.78*m.b345 + 234244.428*m.b346
                        + 286648.923*m.b347 + 44320*m.b348 + 60800*m.b349 + 64800*m.b350 + 88640*m.b351 + 120000*m.b352
                        + 147840*m.b353 + 196960*m.b354 + 227040*m.b355 + 270880*m.b356 + 306400*m.b357 + 393600*m.b358
                        + 511360*m.b359 + 625760*m.b360 + 3227.604*m.b361 + 4427.76*m.b362 + 4719.06*m.b363
                        + 6455.208*m.b364 + 8739*m.b365 + 10766.448*m.b366 + 14343.612*m.b367 + 16534.188*m.b368
                        + 19726.836*m.b369 + 22313.58*m.b370 + 28663.92*m.b371 + 37239.792*m.b372 + 45570.972*m.b373
                        + 5624.762*m.b374 + 7716.28*m.b375 + 8223.93*m.b376 + 11249.524*m.b377 + 15229.5*m.b378
                        + 18762.744*m.b379 + 24996.686*m.b380 + 28814.214*m.b381 + 34378.058*m.b382 + 38885.99*m.b383
                        + 49952.76*m.b384 + 64897.976*m.b385 + 79416.766*m.b386 + 19968.93*m.b387 + 27394.2*m.b388
                        + 29196.45*m.b389 + 39937.86*m.b390 + 54067.5*m.b391 + 66611.16*m.b392 + 88742.79*m.b393
                        + 102295.71*m.b394 + 122048.37*m.b395 + 138052.35*m.b396 + 177341.4*m.b397 + 230399.64*m.b398
                        + 281943.99*m.b399 + 63963.178*m.b400 + 87747.32*m.b401 + 93520.17*m.b402 + 127926.356*m.b403
                        + 173185.5*m.b404 + 213364.536*m.b405 + 284255.134*m.b406 + 327666.966*m.b407
                        + 390937.402*m.b408 + 442200.31*m.b409 + 568048.44*m.b410 + 738001.144*m.b411
                        + 903104.654*m.b412 + 15348.016*m.b413 + 21055.04*m.b414 + 22440.24*m.b415 + 30696.032*m.b416
                        + 41556*m.b417 + 51196.992*m.b418 + 68207.248*m.b419 + 78623.952*m.b420 + 93805.744*m.b421
                        + 106106.32*m.b422 + 136303.68*m.b423 + 177083.968*m.b424 + 216700.688*m.b425 + 40995.446*m.b426
                        + 56239.24*m.b427 + 59939.19*m.b428 + 81990.892*m.b429 + 110998.5*m.b430 + 136750.152*m.b431
                        + 182185.538*m.b432 + 210009.162*m.b433 + 250560.614*m.b434 + 283416.17*m.b435
                        + 364075.08*m.b436 + 473001.608*m.b437 + 578820.178*m.b438 + 33715.609*m.b439 + 46252.46*m.b440
                        + 49295.385*m.b441 + 67431.218*m.b442 + 91287.75*m.b443 + 112466.508*m.b444 + 149833.627*m.b445
                        + 172716.423*m.b446 + 206066.881*m.b447 + 233088.055*m.b448 + 299423.82*m.b449
                        + 389007.532*m.b450 + 476035.187*m.b451 + 16319.732*m.b452 + 22388.08*m.b453 + 23860.98*m.b454
                        + 32639.464*m.b455 + 44187*m.b456 + 54438.384*m.b457 + 72525.596*m.b458 + 83601.804*m.b459
                        + 99744.788*m.b460 + 112824.14*m.b461 + 144933.36*m.b462 + 188295.536*m.b463 + 230420.476*m.b464
                        + 4737.808*m.b465 + 6499.52*m.b466 + 6927.12*m.b467 + 9475.616*m.b468 + 12828*m.b469
                        + 15804.096*m.b470 + 21055.024*m.b471 + 24270.576*m.b472 + 28957.072*m.b473 + 32754.16*m.b474
                        + 42075.84*m.b475 + 54664.384*m.b476 + 66893.744*m.b477 + 1217.969*m.b478 + 1670.86*m.b479
                        + 1780.785*m.b480 + 2435.938*m.b481 + 3297.75*m.b482 + 4062.828*m.b483 + 5412.707*m.b484
                        + 6239.343*m.b485 + 7444.121*m.b486 + 8420.255*m.b487 + 10816.62*m.b488 + 14052.812*m.b489
                        + 17196.667*m.b490 + 17133.281*m.b491 + 23504.14*m.b492 + 25050.465*m.b493 + 34266.562*m.b494
                        + 46389.75*m.b495 + 57152.172*m.b496 + 76141.043*m.b497 + 87769.407*m.b498 + 104717.129*m.b499
                        + 118448.495*m.b500 + 152158.38*m.b501 + 197682.188*m.b502 + 241907.083*m.b503 + 9448.47*m.b504
                        + 12961.8*m.b505 + 13814.55*m.b506 + 18896.94*m.b507 + 25582.5*m.b508 + 31517.64*m.b509
                        + 41989.41*m.b510 + 48402.09*m.b511 + 57748.23*m.b512 + 65320.65*m.b513 + 83910.6*m.b514
                        + 109015.56*m.b515 + 133404.21*m.b516 + 16875.671*m.b517 + 23150.74*m.b518 + 24673.815*m.b519
                        + 33751.342*m.b520 + 45692.25*m.b521 + 56292.852*m.b522 + 74996.213*m.b523 + 86449.737*m.b524
                        + 103142.639*m.b525 + 116667.545*m.b526 + 149870.58*m.b527 + 194709.908*m.b528
                        + 238269.853*m.b529 + 1532.364*m.b530 + 2102.16*m.b531 + 2240.46*m.b532 + 3064.728*m.b533
                        + 4149*m.b534 + 5111.568*m.b535 + 6809.892*m.b536 + 7849.908*m.b537 + 9365.676*m.b538
                        + 10593.78*m.b539 + 13608.72*m.b540 + 17680.272*m.b541 + 21635.652*m.b542 + 9471.184*m.b543
                        + 12992.96*m.b544 + 13847.76*m.b545 + 18942.368*m.b546 + 25644*m.b547 + 31593.408*m.b548
                        + 42090.352*m.b549 + 48518.448*m.b550 + 57887.056*m.b551 + 65477.68*m.b552 + 84112.32*m.b553
                        + 109277.632*m.b554 + 133724.912*m.b555 + 23365.504*m.b556 + 32053.76*m.b557 + 34162.56*m.b558
                        + 46731.008*m.b559 + 63264*m.b560 + 77941.248*m.b561 + 103837.312*m.b562 + 119695.488*m.b563
                        + 142807.936*m.b564 + 161534.08*m.b565 + 207505.92*m.b566 + 269588.992*m.b567
                        + 329900.672*m.b568 + 12028.448*m.b569 + 16501.12*m.b570 + 17586.72*m.b571 + 24056.896*m.b572
                        + 32568*m.b573 + 40123.776*m.b574 + 53454.944*m.b575 + 61618.656*m.b576 + 73516.832*m.b577
                        + 83156.96*m.b578 + 106823.04*m.b579 + 138783.104*m.b580 + 169831.264*m.b581 + 20767.798*m.b582
                        + 28490.12*m.b583 + 30364.47*m.b584 + 41535.596*m.b585 + 56230.5*m.b586 + 69275.976*m.b587
                        + 92292.994*m.b588 + 106388.106*m.b589 + 126930.982*m.b590 + 143575.21*m.b591 + 184436.04*m.b592
                        + 239616.904*m.b593 + 293223.314*m.b594 + 6664.343*m.b595 + 9142.42*m.b596 + 9743.895*m.b597
                        + 13328.686*m.b598 + 18044.25*m.b599 + 22230.516*m.b600 + 29616.629*m.b601 + 34139.721*m.b602
                        + 40731.887*m.b603 + 46072.985*m.b604 + 59185.14*m.b605 + 76892.564*m.b606 + 94094.749*m.b607
                        + 23313.151*m.b608 + 31981.94*m.b609 + 34086.015*m.b610 + 46626.302*m.b611 + 63122.25*m.b612
                        + 77766.612*m.b613 + 103604.653*m.b614 + 119427.297*m.b615 + 142487.959*m.b616
                        + 161172.145*m.b617 + 207040.98*m.b618 + 268984.948*m.b619 + 329161.493*m.b620 + 17719.69*m.b621
                        + 24308.6*m.b622 + 25907.85*m.b623 + 35439.38*m.b624 + 47977.5*m.b625 + 59108.28*m.b626
                        + 78747.07*m.b627 + 90773.43*m.b628 + 108301.21*m.b629 + 122502.55*m.b630 + 157366.2*m.b631
                        + 204448.12*m.b632 + 250186.67*m.b633 + 6525.289*m.b634 + 8951.66*m.b635 + 9540.585*m.b636
                        + 13050.578*m.b637 + 17667.75*m.b638 + 21766.668*m.b639 + 28998.667*m.b640 + 33427.383*m.b641
                        + 39882.001*m.b642 + 45111.655*m.b643 + 57950.22*m.b644 + 75288.172*m.b645 + 92131.427*m.b646
                        + 26521.088*m.b647 + 36382.72*m.b648 + 38776.32*m.b649 + 53042.176*m.b650 + 71808*m.b651
                        + 88467.456*m.b652 + 117860.864*m.b653 + 135860.736*m.b654 + 162094.592*m.b655
                        + 183349.76*m.b656 + 235530.24*m.b657 + 305997.824*m.b658 + 374454.784*m.b659 + 10133.214*m.b660
                        + 13901.16*m.b661 + 14815.71*m.b662 + 20266.428*m.b663 + 27436.5*m.b664 + 33801.768*m.b665
                        + 45032.442*m.b666 + 51909.858*m.b667 + 61933.326*m.b668 + 70054.53*m.b669 + 89991.72*m.b670
                        + 116916.072*m.b671 + 143072.202*m.b672 + 99.443*m.b673 + 136.42*m.b674 + 145.395*m.b675
                        + 198.886*m.b676 + 269.25*m.b677 + 331.716*m.b678 + 441.929*m.b679 + 509.421*m.b680
                        + 607.787*m.b681 + 687.485*m.b682 + 883.14*m.b683 + 1147.364*m.b684 + 1404.049*m.b685
                        + 8984.772*m.b686 + 12325.68*m.b687 + 13136.58*m.b688 + 17969.544*m.b689 + 24327*m.b690
                        + 29970.864*m.b691 + 39928.716*m.b692 + 46026.684*m.b693 + 54914.148*m.b694 + 62114.94*m.b695
                        + 79792.56*m.b696 + 103665.456*m.b697 + 126857.196*m.b698 + 16663.766*m.b699 + 22860.04*m.b700
                        + 24363.99*m.b701 + 33327.532*m.b702 + 45118.5*m.b703 + 55585.992*m.b704 + 74054.498*m.b705
                        + 85364.202*m.b706 + 101847.494*m.b707 + 115202.57*m.b708 + 147988.68*m.b709 + 192264.968*m.b710
                        + 235277.938*m.b711 + 11715.715*m.b712 + 16072.1*m.b713 + 17129.475*m.b714 + 23431.43*m.b715
                        + 31721.25*m.b716 + 39080.58*m.b717 + 52065.145*m.b718 + 60016.605*m.b719 + 71605.435*m.b720
                        + 80994.925*m.b721 + 104045.7*m.b722 + 135174.82*m.b723 + 165415.745*m.b724 + 4959.408*m.b725
                        + 6803.52*m.b726 + 7251.12*m.b727 + 9918.816*m.b728 + 13428*m.b729 + 16543.296*m.b730
                        + 22039.824*m.b731 + 25405.776*m.b732 + 30311.472*m.b733 + 34286.16*m.b734 + 44043.84*m.b735
                        + 57221.184*m.b736 + 70022.544*m.b737 + 15813.93*m.b738 + 21694.2*m.b739 + 23121.45*m.b740
                        + 31627.86*m.b741 + 42817.5*m.b742 + 52751.16*m.b743 + 70277.79*m.b744 + 81010.71*m.b745
                        + 96653.37*m.b746 + 109327.35*m.b747 + 140441.4*m.b748 + 182459.64*m.b749 + 223278.99*m.b750
                        + 921.025*m.b751 + 1263.5*m.b752 + 1346.625*m.b753 + 1842.05*m.b754 + 2493.75*m.b755
                        + 3072.3*m.b756 + 4093.075*m.b757 + 4718.175*m.b758 + 5629.225*m.b759 + 6367.375*m.b760
                        + 8179.5*m.b761 + 10626.7*m.b762 + 13004.075*m.b763 + 15947.721*m.b764 + 21877.74*m.b765
                        + 23317.065*m.b766 + 31895.442*m.b767 + 43179.75*m.b768 + 53197.452*m.b769 + 70872.363*m.b770
                        + 81696.087*m.b771 + 97471.089*m.b772 + 110252.295*m.b773 + 141629.58*m.b774 + 184003.308*m.b775
                        + 225168.003*m.b776 + 12246.447*m.b777 + 16800.18*m.b778 + 17905.455*m.b779 + 24492.894*m.b780
                        + 33158.25*m.b781 + 40850.964*m.b782 + 54423.741*m.b783 + 62735.409*m.b784 + 74849.223*m.b785
                        + 84664.065*m.b786 + 108759.06*m.b787 + 141298.356*m.b788 + 172909.221*m.b789 + 52733.875*m.b790
                        + 72342.5*m.b791 + 77101.875*m.b792 + 105467.75*m.b793 + 142781.25*m.b794 + 175906.5*m.b795
                        + 234351.625*m.b796 + 270142.125*m.b797 + 322304.875*m.b798 + 364568.125*m.b799
                        + 468322.5*m.b800 + 608438.5*m.b801 + 744556.625*m.b802 + 6932.756*m.b803 + 9510.64*m.b804
                        + 10136.34*m.b805 + 13865.512*m.b806 + 18771*m.b807 + 23125.872*m.b808 + 30809.468*m.b809
                        + 35514.732*m.b810 + 42372.404*m.b811 + 47928.62*m.b812 + 61568.88*m.b813 + 79989.488*m.b814
                        + 97884.508*m.b815 + 150.411*m.b816 + 206.34*m.b817 + 219.915*m.b818 + 300.822*m.b819
                        + 407.25*m.b820 + 501.732*m.b821 + 668.433*m.b822 + 770.517*m.b823 + 919.299*m.b824
                        + 1039.845*m.b825 + 1335.78*m.b826 + 1735.428*m.b827 + 2123.673*m.b828 + 8463.181*m.b829
                        + 11610.14*m.b830 + 12373.965*m.b831 + 16926.362*m.b832 + 22914.75*m.b833 + 28230.972*m.b834
                        + 37610.743*m.b835 + 43354.707*m.b836 + 51726.229*m.b837 + 58508.995*m.b838 + 75160.38*m.b839
                        + 97647.388*m.b840 + 119492.783*m.b841 + 21117.095*m.b842 + 28969.3*m.b843 + 30875.175*m.b844
                        + 42234.19*m.b845 + 57176.25*m.b846 + 70441.14*m.b847 + 93845.285*m.b848 + 108177.465*m.b849
                        + 129065.855*m.b850 + 145990.025*m.b851 + 187538.1*m.b852 + 243647.06*m.b853 + 298155.085*m.b854
                        + 1767.537*m.b855 + 2424.78*m.b856 + 2584.305*m.b857 + 3535.074*m.b858 + 4785.75*m.b859
                        + 5896.044*m.b860 + 7855.011*m.b861 + 9054.639*m.b862 + 10803.033*m.b863 + 12219.615*m.b864
                        + 15697.26*m.b865 + 20393.676*m.b866 + 24956.091*m.b867 + 39010.741*m.b868 + 53516.54*m.b869
                        + 57037.365*m.b870 + 78021.482*m.b871 + 105624.75*m.b872 + 130129.692*m.b873 + 173365.423*m.b874
                        + 199842.027*m.b875 + 238430.269*m.b876 + 269695.195*m.b877 + 346449.18*m.b878
                        + 450102.268*m.b879 + 550797.863*m.b880 + 31159.73*m.b881 + 42746.2*m.b882 + 45558.45*m.b883
                        + 62319.46*m.b884 + 84367.5*m.b885 + 103940.76*m.b886 + 138475.19*m.b887 + 159623.31*m.b888
                        + 190445.57*m.b889 + 215418.35*m.b890 + 276725.4*m.b891 + 359518.04*m.b892 + 439948.39*m.b893
                        + 3476.627*m.b894 + 4769.38*m.b895 + 5083.155*m.b896 + 6953.254*m.b897 + 9413.25*m.b898
                        + 11597.124*m.b899 + 15450.281*m.b900 + 17809.869*m.b901 + 21248.843*m.b902 + 24035.165*m.b903
                        + 30875.46*m.b904 + 40112.996*m.b905 + 49086.961*m.b906 + 3359.179*m.b907 + 4608.26*m.b908
                        + 4911.435*m.b909 + 6718.358*m.b910 + 9095.25*m.b911 + 11205.348*m.b912 + 14928.337*m.b913
                        + 17208.213*m.b914 + 20531.011*m.b915 + 23223.205*m.b916 + 29832.42*m.b917 + 38757.892*m.b918
                        + 47428.697*m.b919 + 8608.052*m.b920 + 11808.88*m.b921 + 12585.78*m.b922 + 17216.104*m.b923
                        + 23307*m.b924 + 28714.224*m.b925 + 38254.556*m.b926 + 44096.844*m.b927 + 52611.668*m.b928
                        + 59510.54*m.b929 + 76446.96*m.b930 + 99318.896*m.b931 + 121538.236*m.b932 + 11768.622*m.b933
                        + 16144.68*m.b934 + 17206.83*m.b935 + 23537.244*m.b936 + 31864.5*m.b937 + 39257.064*m.b938
                        + 52300.266*m.b939 + 60287.634*m.b940 + 71928.798*m.b941 + 81360.69*m.b942 + 104515.56*m.b943
                        + 135785.256*m.b944 + 166162.746*m.b945 + 2016.56*m.b946 + 2766.4*m.b947 + 2948.4*m.b948
                        + 4033.12*m.b949 + 5460*m.b950 + 6726.72*m.b951 + 8961.68*m.b952 + 10330.32*m.b953
                        + 12325.04*m.b954 + 13941.2*m.b955 + 17908.8*m.b956 + 23266.88*m.b957 + 28472.08*m.b958
                        + 15743.295*m.b959 + 21597.3*m.b960 + 23018.175*m.b961 + 31486.59*m.b962 + 42626.25*m.b963
                        + 52515.54*m.b964 + 69963.885*m.b965 + 80648.865*m.b966 + 96221.655*m.b967 + 108839.025*m.b968
                        + 139814.1*m.b969 + 181644.66*m.b970 + 222281.685*m.b971 + 12234.813*m.b972 + 16784.22*m.b973
                        + 17888.445*m.b974 + 24469.626*m.b975 + 33126.75*m.b976 + 40812.156*m.b977 + 54372.039*m.b978
                        + 62675.811*m.b979 + 74778.117*m.b980 + 84583.635*m.b981 + 108655.74*m.b982 + 141164.124*m.b983
                        + 172744.959*m.b984 + 9223.823*m.b985 + 12653.62*m.b986 + 13486.095*m.b987 + 18447.646*m.b988
                        + 24974.25*m.b989 + 30768.276*m.b990 + 40991.069*m.b991 + 47251.281*m.b992 + 56375.207*m.b993
                        + 63767.585*m.b994 + 81915.54*m.b995 + 106423.604*m.b996 + 130232.389*m.b997 + 277*m.b998
                        + 380*m.b999 + 405*m.b1000 + 554*m.b1001 + 750*m.b1002 + 924*m.b1003 + 1231*m.b1004
                        + 1419*m.b1005 + 1693*m.b1006 + 1915*m.b1007 + 2460*m.b1008 + 3196*m.b1009 + 3911*m.b1010
                        + 6366.845*m.b1011 + 8734.3*m.b1012 + 9308.925*m.b1013 + 12733.69*m.b1014 + 17238.75*m.b1015
                        + 21238.14*m.b1016 + 28294.535*m.b1017 + 32615.715*m.b1018 + 38913.605*m.b1019
                        + 44016.275*m.b1020 + 56543.1*m.b1021 + 73460.06*m.b1022 + 89894.335*m.b1023 + 10932.359*m.b1024
                        + 14997.46*m.b1025 + 15984.135*m.b1026 + 21864.718*m.b1027 + 29600.25*m.b1028
                        + 36467.508*m.b1029 + 48583.877*m.b1030 + 56003.673*m.b1031 + 66817.631*m.b1032
                        + 75579.305*m.b1033 + 97088.82*m.b1034 + 126136.532*m.b1035 + 154355.437*m.b1036
                        + 13875.484*m.b1037 + 19034.96*m.b1038 + 20287.26*m.b1039 + 27750.968*m.b1040 + 37569*m.b1041
                        + 46285.008*m.b1042 + 61663.252*m.b1043 + 71080.548*m.b1044 + 84805.756*m.b1045
                        + 95926.18*m.b1046 + 123226.32*m.b1047 + 160094.032*m.b1048 + 195909.812*m.b1049
                        + 9721.869*m.b1050 + 13336.86*m.b1051 + 14214.285*m.b1052 + 19443.738*m.b1053 + 26322.75*m.b1054
                        + 32429.628*m.b1055 + 43204.407*m.b1056 + 49802.643*m.b1057 + 59419.221*m.b1058
                        + 67210.755*m.b1059 + 86338.62*m.b1060 + 112170.012*m.b1061 + 137264.367*m.b1062
                        + 1834.848*m.b1063 + 2517.12*m.b1064 + 2682.72*m.b1065 + 3669.696*m.b1066 + 4968*m.b1067
                        + 6120.576*m.b1068 + 8154.144*m.b1069 + 9399.456*m.b1070 + 11214.432*m.b1071 + 12684.96*m.b1072
                        + 16295.04*m.b1073 + 21170.304*m.b1074 + 25906.464*m.b1075 + 6428.339*m.b1076 + 8818.66*m.b1077
                        + 9398.835*m.b1078 + 12856.678*m.b1079 + 17405.25*m.b1080 + 21443.268*m.b1081
                        + 28567.817*m.b1082 + 32930.733*m.b1083 + 39289.451*m.b1084 + 44441.405*m.b1085
                        + 57089.22*m.b1086 + 74169.572*m.b1087 + 90762.577*m.b1088 + 17869.27*m.b1089 + 24513.8*m.b1090
                        + 26126.55*m.b1091 + 35738.54*m.b1092 + 48382.5*m.b1093 + 59607.24*m.b1094 + 79411.81*m.b1095
                        + 91539.69*m.b1096 + 109215.43*m.b1097 + 123536.65*m.b1098 + 158694.6*m.b1099
                        + 206173.96*m.b1100 + 252298.61*m.b1101 + 4287.406*m.b1102 + 5881.64*m.b1103 + 6268.59*m.b1104
                        + 8574.812*m.b1105 + 11608.5*m.b1106 + 14301.672*m.b1107 + 19053.418*m.b1108 + 21963.282*m.b1109
                        + 26204.254*m.b1110 + 29640.37*m.b1111 + 38075.88*m.b1112 + 49467.688*m.b1113
                        + 60534.458*m.b1114 + 6430.001*m.b1115 + 8820.94*m.b1116 + 9401.265*m.b1117 + 12860.002*m.b1118
                        + 17409.75*m.b1119 + 21448.812*m.b1120 + 28575.203*m.b1121 + 32939.247*m.b1122
                        + 39299.609*m.b1123 + 44452.895*m.b1124 + 57103.98*m.b1125 + 74188.748*m.b1126
                        + 90786.043*m.b1127 + 17888.383*m.b1128 + 24540.02*m.b1129 + 26154.495*m.b1130
                        + 35776.766*m.b1131 + 48434.25*m.b1132 + 59670.996*m.b1133 + 79496.749*m.b1134
                        + 91637.601*m.b1135 + 109332.247*m.b1136 + 123668.785*m.b1137 + 158864.34*m.b1138
                        + 206394.484*m.b1139 + 252568.469*m.b1140 + 4372.999*m.b1141 + 5999.06*m.b1142
                        + 6393.735*m.b1143 + 8745.998*m.b1144 + 11840.25*m.b1145 + 14587.188*m.b1146 + 19433.797*m.b1147
                        + 22401.753*m.b1148 + 26727.391*m.b1149 + 30232.105*m.b1150 + 38836.02*m.b1151
                        + 50455.252*m.b1152 + 61742.957*m.b1153 + 4341.975*m.b1154 + 5956.5*m.b1155 + 6348.375*m.b1156
                        + 8683.95*m.b1157 + 11756.25*m.b1158 + 14483.7*m.b1159 + 19295.925*m.b1160 + 22242.825*m.b1161
                        + 26537.775*m.b1162 + 30017.625*m.b1163 + 38560.5*m.b1164 + 50097.3*m.b1165 + 61304.925*m.b1166
                        + 5725.313*m.b1167 + 7854.22*m.b1168 + 8370.945*m.b1169 + 11450.626*m.b1170 + 15501.75*m.b1171
                        + 19098.156*m.b1172 + 25443.539*m.b1173 + 29329.311*m.b1174 + 34992.617*m.b1175
                        + 39581.135*m.b1176 + 50845.74*m.b1177 + 66058.124*m.b1178 + 80836.459*m.b1179
                        + 17500.86*m.b1180 + 24008.4*m.b1181 + 25587.9*m.b1182 + 35001.72*m.b1183 + 47385*m.b1184
                        + 58378.32*m.b1185 + 77774.58*m.b1186 + 89652.42*m.b1187 + 106963.74*m.b1188 + 120989.7*m.b1189
                        + 155422.8*m.b1190 + 201923.28*m.b1191 + 247096.98*m.b1192 + 4232.837*m.b1193 + 5806.78*m.b1194
                        + 6188.805*m.b1195 + 8465.674*m.b1196 + 11460.75*m.b1197 + 14119.644*m.b1198 + 18810.911*m.b1199
                        + 21683.739*m.b1200 + 25870.733*m.b1201 + 29263.115*m.b1202 + 37591.26*m.b1203
                        + 48838.076*m.b1204 + 59763.991*m.b1205 + 4986*m.b1206 + 6840*m.b1207 + 7290*m.b1208
                        + 9972*m.b1209 + 13500*m.b1210 + 16632*m.b1211 + 22158*m.b1212 + 25542*m.b1213 + 30474*m.b1214
                        + 34470*m.b1215 + 44280*m.b1216 + 57528*m.b1217 + 70398*m.b1218 + 30917.355*m.b1219
                        + 42413.7*m.b1220 + 45204.075*m.b1221 + 61834.71*m.b1222 + 83711.25*m.b1223 + 103132.26*m.b1224
                        + 137398.065*m.b1225 + 158381.685*m.b1226 + 188964.195*m.b1227 + 213742.725*m.b1228
                        + 274572.9*m.b1229 + 356721.54*m.b1230 + 436526.265*m.b1231 + 4582.411*m.b1232 + 6286.34*m.b1233
                        + 6699.915*m.b1234 + 9164.822*m.b1235 + 12407.25*m.b1236 + 15285.732*m.b1237 + 20364.433*m.b1238
                        + 23474.517*m.b1239 + 28007.299*m.b1240 + 31679.845*m.b1241 + 40695.78*m.b1242
                        + 52871.428*m.b1243 + 64699.673*m.b1244 + 9206.095*m.b1245 + 12629.3*m.b1246 + 13460.175*m.b1247
                        + 18412.19*m.b1248 + 24926.25*m.b1249 + 30709.14*m.b1250 + 40912.285*m.b1251 + 47160.465*m.b1252
                        + 56266.855*m.b1253 + 63645.025*m.b1254 + 81758.1*m.b1255 + 106219.06*m.b1256
                        + 129982.085*m.b1257 + 4973.258*m.b1258 + 6822.52*m.b1259 + 7271.37*m.b1260 + 9946.516*m.b1261
                        + 13465.5*m.b1262 + 16589.496*m.b1263 + 22101.374*m.b1264 + 25476.726*m.b1265
                        + 30396.122*m.b1266 + 34381.91*m.b1267 + 44166.84*m.b1268 + 57380.984*m.b1269
                        + 70218.094*m.b1270 + 21458.913*m.b1271 + 29438.22*m.b1272 + 31374.945*m.b1273
                        + 42917.826*m.b1274 + 58101.75*m.b1275 + 71581.356*m.b1276 + 95364.339*m.b1277
                        + 109928.511*m.b1278 + 131155.017*m.b1279 + 148353.135*m.b1280 + 190573.74*m.b1281
                        + 247590.924*m.b1282 + 302981.259*m.b1283 + 1450.649*m.b1284 + 1990.06*m.b1285
                        + 2120.985*m.b1286 + 2901.298*m.b1287 + 3927.75*m.b1288 + 4838.988*m.b1289 + 6446.747*m.b1290
                        + 7431.303*m.b1291 + 8866.241*m.b1292 + 10028.855*m.b1293 + 12883.02*m.b1294 + 16737.452*m.b1295
                        + 20481.907*m.b1296 + 12065.566*m.b1297 + 16552.04*m.b1298 + 17640.99*m.b1299
                        + 24131.132*m.b1300 + 32668.5*m.b1301 + 40247.592*m.b1302 + 53619.898*m.b1303
                        + 61808.802*m.b1304 + 73743.694*m.b1305 + 83413.57*m.b1306 + 107152.68*m.b1307
                        + 139211.368*m.b1308 + 170355.338*m.b1309 + 24920.859*m.b1310 + 34187.46*m.b1311
                        + 36436.635*m.b1312 + 49841.718*m.b1313 + 67475.25*m.b1314 + 83129.508*m.b1315
                        + 110749.377*m.b1316 + 127663.173*m.b1317 + 152314.131*m.b1318 + 172286.805*m.b1319
                        + 221318.82*m.b1320 + 287534.532*m.b1321 + 351860.937*m.b1322 + 9341.548*m.b1323
                        + 12815.12*m.b1324 + 13658.22*m.b1325 + 18683.096*m.b1326 + 25293*m.b1327 + 31160.976*m.b1328
                        + 41514.244*m.b1329 + 47854.356*m.b1330 + 57094.732*m.b1331 + 64581.46*m.b1332
                        + 82961.04*m.b1333 + 107781.904*m.b1334 + 131894.564*m.b1335 + 5498.45*m.b1336 + 7543*m.b1337
                        + 8039.25*m.b1338 + 10996.9*m.b1339 + 14887.5*m.b1340 + 18341.4*m.b1341 + 24435.35*m.b1342
                        + 28167.15*m.b1343 + 33606.05*m.b1344 + 38012.75*m.b1345 + 48831*m.b1346 + 63440.6*m.b1347
                        + 77633.35*m.b1348 + 2393.003*m.b1349 + 3282.82*m.b1350 + 3498.795*m.b1351 + 4786.006*m.b1352
                        + 6479.25*m.b1353 + 7982.436*m.b1354 + 10634.609*m.b1355 + 12258.741*m.b1356 + 14625.827*m.b1357
                        + 16543.685*m.b1358 + 21251.94*m.b1359 + 27610.244*m.b1360 + 33787.129*m.b1361
                        + 5173.529*m.b1362 + 7097.26*m.b1363 + 7564.185*m.b1364 + 10347.058*m.b1365 + 14007.75*m.b1366
                        + 17257.548*m.b1367 + 22991.387*m.b1368 + 26502.663*m.b1369 + 31620.161*m.b1370
                        + 35766.455*m.b1371 + 45945.42*m.b1372 + 59691.692*m.b1373 + 73045.747*m.b1374
                        + 6261.031*m.b1375 + 8589.14*m.b1376 + 9154.215*m.b1377 + 12522.062*m.b1378 + 16952.25*m.b1379
                        + 20885.172*m.b1380 + 27824.293*m.b1381 + 32073.657*m.b1382 + 38266.879*m.b1383
                        + 43284.745*m.b1384 + 55603.38*m.b1385 + 72239.188*m.b1386 + 88400.333*m.b1387
                        + 21729.265*m.b1388 + 29809.1*m.b1389 + 31770.225*m.b1390 + 43458.53*m.b1391 + 58833.75*m.b1392
                        + 72483.18*m.b1393 + 96565.795*m.b1394 + 111313.455*m.b1395 + 132807.385*m.b1396
                        + 150222.175*m.b1397 + 192974.7*m.b1398 + 250710.22*m.b1399 + 306798.395*m.b1400
                        + 4794.593*m.b1401 + 6577.42*m.b1402 + 7010.145*m.b1403 + 9589.186*m.b1404 + 12981.75*m.b1405
                        + 15993.516*m.b1406 + 21307.379*m.b1407 + 24561.471*m.b1408 + 29304.137*m.b1409
                        + 33146.735*m.b1410 + 42580.14*m.b1411 + 55319.564*m.b1412 + 67695.499*m.b1413
                        + 48316.279*m.b1414 + 66282.26*m.b1415 + 70642.935*m.b1416 + 96632.558*m.b1417
                        + 130820.25*m.b1418 + 161170.548*m.b1419 + 214719.637*m.b1420 + 247511.913*m.b1421
                        + 295304.911*m.b1422 + 334027.705*m.b1423 + 429090.42*m.b1424 + 557468.692*m.b1425
                        + 682183.997*m.b1426 + 4270.786*m.b1427 + 5858.84*m.b1428 + 6244.29*m.b1429 + 8541.572*m.b1430
                        + 11563.5*m.b1431 + 14246.232*m.b1432 + 18979.558*m.b1433 + 21878.142*m.b1434
                        + 26102.674*m.b1435 + 29525.47*m.b1436 + 37928.28*m.b1437 + 49275.928*m.b1438
                        + 60299.798*m.b1439 + 29713.513*m.b1440 + 40762.22*m.b1441 + 43443.945*m.b1442
                        + 59427.026*m.b1443 + 80451.75*m.b1444 + 99116.556*m.b1445 + 132048.139*m.b1446
                        + 152214.711*m.b1447 + 181606.417*m.b1448 + 205420.135*m.b1449 + 263881.74*m.b1450
                        + 342831.724*m.b1451 + 419529.059*m.b1452 + 138.5*m.b1453 + 190*m.b1454 + 202.5*m.b1455
                        + 277*m.b1456 + 375*m.b1457 + 462*m.b1458 + 615.5*m.b1459 + 709.5*m.b1460 + 846.5*m.b1461
                        + 957.5*m.b1462 + 1230*m.b1463 + 1598*m.b1464 + 1955.5*m.b1465 + 6649.385*m.b1466
                        + 9121.9*m.b1467 + 9722.025*m.b1468 + 13298.77*m.b1469 + 18003.75*m.b1470 + 22180.62*m.b1471
                        + 29550.155*m.b1472 + 34063.095*m.b1473 + 40640.465*m.b1474 + 45969.575*m.b1475
                        + 59052.3*m.b1476 + 76719.98*m.b1477 + 93883.555*m.b1478 + 6648*m.b1479 + 9120*m.b1480
                        + 9720*m.b1481 + 13296*m.b1482 + 18000*m.b1483 + 22176*m.b1484 + 29544*m.b1485 + 34056*m.b1486
                        + 40632*m.b1487 + 45960*m.b1488 + 59040*m.b1489 + 76704*m.b1490 + 93864*m.b1491
                        + 3139.795*m.b1492 + 4307.3*m.b1493 + 4590.675*m.b1494 + 6279.59*m.b1495 + 8501.25*m.b1496
                        + 10473.54*m.b1497 + 13953.385*m.b1498 + 16084.365*m.b1499 + 19190.155*m.b1500
                        + 21706.525*m.b1501 + 27884.1*m.b1502 + 36226.66*m.b1503 + 44331.185*m.b1504 + 45308.613*m.b1505
                        + 62156.22*m.b1506 + 66245.445*m.b1507 + 90617.226*m.b1508 + 122676.75*m.b1509
                        + 151137.756*m.b1510 + 201353.439*m.b1511 + 232104.411*m.b1512 + 276922.317*m.b1513
                        + 313234.635*m.b1514 + 402379.74*m.b1515 + 522766.524*m.b1516 + 639718.359*m.b1517
                        + 9003.331*m.b1518 + 12351.14*m.b1519 + 13163.715*m.b1520 + 18006.662*m.b1521 + 24377.25*m.b1522
                        + 30032.772*m.b1523 + 40011.193*m.b1524 + 46121.757*m.b1525 + 55027.579*m.b1526
                        + 62243.245*m.b1527 + 79957.38*m.b1528 + 103879.588*m.b1529 + 127119.233*m.b1530
                        + 4177.714*m.b1531 + 5731.16*m.b1532 + 6108.21*m.b1533 + 8355.428*m.b1534 + 11311.5*m.b1535
                        + 13935.768*m.b1536 + 18565.942*m.b1537 + 21401.358*m.b1538 + 25533.826*m.b1539
                        + 28882.03*m.b1540 + 37101.72*m.b1541 + 48202.072*m.b1542 + 58985.702*m.b1543 + 9179.78*m.b1544
                        + 12593.2*m.b1545 + 13421.7*m.b1546 + 18359.56*m.b1547 + 24855*m.b1548 + 30621.36*m.b1549
                        + 40795.34*m.b1550 + 47025.66*m.b1551 + 56106.02*m.b1552 + 63463.1*m.b1553 + 81524.4*m.b1554
                        + 105915.44*m.b1555 + 129610.54*m.b1556, sense=minimize)

m.c2 = Constraint(expr=   m.x72 - m.x74 == -0.01001)

m.c3 = Constraint(expr= - m.x72 + m.x73 - m.x158 == -0.01243)

m.c4 = Constraint(expr=   m.x74 + m.x75 + m.x76 == -0.0085)

m.c5 = Constraint(expr= - m.x73 - m.x75 + m.x77 == -0.0085)

m.c6 = Constraint(expr= - m.x76 + m.x78 - m.x157 == -0.01212)

m.c7 = Constraint(expr=   m.x79 + m.x80 - m.x82 - m.x160 == -0.00163)

m.c8 = Constraint(expr= - m.x79 == 0)

m.c9 = Constraint(expr= - m.x80 + m.x81 - m.x162 == -0.0336)

m.c10 = Constraint(expr=   m.x82 + m.x83 - m.x115 == -0.00438)

m.c11 = Constraint(expr=   m.x84 == -0.0164)

m.c12 = Constraint(expr= - m.x84 - m.x112 - m.x126 == -0.02977)

m.c13 = Constraint(expr=   m.x85 - m.x102 == -0.00049)

m.c14 = Constraint(expr=   m.x86 - m.x89 == -0.00749)

m.c15 = Constraint(expr=   m.x87 - m.x88 == -0.00606)

m.c16 = Constraint(expr= - m.x86 - m.x100 - m.x103 == -0.00277)

m.c17 = Constraint(expr=   m.x89 + m.x90 - m.x93 == -0.00503)

m.c18 = Constraint(expr= - m.x90 + m.x91 + m.x92 == -0.00481)

m.c19 = Constraint(expr= - m.x91 + m.x93 + m.x94 - m.x95 == -0.02104)

m.c20 = Constraint(expr=   m.x95 + m.x96 - m.x99 == -0.01694)

m.c21 = Constraint(expr= - m.x96 + m.x97 + m.x98 == -0.01041)

m.c22 = Constraint(expr= - m.x97 + m.x99 - m.x106 == -0.00217)

m.c23 = Constraint(expr= - m.x87 + m.x100 + m.x101 == -0.00655)

m.c24 = Constraint(expr= - m.x101 + m.x102 - m.x118 == -0.01041)

m.c25 = Constraint(expr=   m.x103 + m.x104 + m.x105 == -0.00278)

m.c26 = Constraint(expr= - m.x94 - m.x104 + m.x106 == -0.00532)

m.c27 = Constraint(expr=   m.x107 + m.x108 - m.x110 == -0.00363)

m.c28 = Constraint(expr= - m.x81 - m.x107 + m.x109 == -0.033)

m.c29 = Constraint(expr= - m.x108 + m.x110 + m.x111 - m.x116 == -0.006)

m.c30 = Constraint(expr=   m.x112 + m.x113 - m.x120 == -0.0064)

m.c31 = Constraint(expr= - m.x113 + m.x114 - m.x133 == -0.00296)

m.c32 = Constraint(expr= - m.x111 + m.x115 - m.x125 == -0.00309)

m.c33 = Constraint(expr=   m.x116 + m.x117 - m.x122 == -0.00309)

m.c34 = Constraint(expr= - m.x109 + m.x118 + m.x119 == -0.00879)

m.c35 = Constraint(expr= - m.x119 == -0.00168)

m.c36 = Constraint(expr=   m.x120 + m.x121 == -0.01264)

m.c37 = Constraint(expr= - m.x92 - m.x121 == -0.01264)

m.c38 = Constraint(expr= - m.x85 + m.x122 - m.x123 == -0.01264)

m.c39 = Constraint(expr= - m.x83 + m.x123 + m.x124 == -0.00556)

m.c40 = Constraint(expr= - m.x117 - m.x124 + m.x125 == -0.0026)

m.c41 = Constraint(expr=   m.x126 - m.x127 - m.x129 == -0.00457)

m.c42 = Constraint(expr=   m.x129 + m.x130 - m.x149 == -0.00756)

m.c43 = Constraint(expr=   m.x131 + m.x132 - m.x167 == -0.00621)

m.c44 = Constraint(expr= - m.x131 + m.x133 - m.x137 == -0.00309)

m.c45 = Constraint(expr=   m.x134 - m.x150 == -0.00059)

m.c46 = Constraint(expr= - m.x134 + m.x135 - m.x139 == -0.01263)

m.c47 = Constraint(expr= - m.x114 - m.x135 + m.x136 == -0.00341)

m.c48 = Constraint(expr= - m.x136 + m.x137 + m.x138 - m.x141 == -0.01321)

m.c49 = Constraint(expr= - m.x138 + m.x139 + m.x140 - m.x168 == -0.00387)

m.c50 = Constraint(expr= - m.x132 + m.x141 + m.x142 == -0.00643)

m.c51 = Constraint(expr= - m.x140 - m.x142 - m.x170 == -0.00255)

m.c52 = Constraint(expr=   m.x143 + m.x144 == 0)

m.c53 = Constraint(expr= - m.x143 + m.x145 + m.x146 + m.x147 + m.x148 == -0.0113)

m.c54 = Constraint(expr=   m.x149 + m.x150 - m.x151 == -0.00399)

m.c55 = Constraint(expr= - m.x130 + m.x151 - m.x152 == -0.00775)

m.c56 = Constraint(expr=   m.x152 + m.x153 - m.x159 == -0.00191)

m.c57 = Constraint(expr= - m.x77 + m.x154 + m.x155 == -0.00088)

m.c58 = Constraint(expr= - m.x153 - m.x154 + m.x156 == -0.00514)

m.c59 = Constraint(expr= - m.x145 - m.x156 + m.x157 == -0.00514)

m.c60 = Constraint(expr= - m.x155 + m.x158 + m.x159 == -0.00744)

m.c61 = Constraint(expr= - m.x161 + m.x162 == 0)

m.c62 = Constraint(expr=   m.x163 + m.x164 == -5E-6)

m.c63 = Constraint(expr= - m.x105 - m.x163 + m.x165 == 0)

m.c64 = Constraint(expr= - m.x144 + m.x166 == -0.00054)

m.c65 = Constraint(expr= - m.x98 - m.x164 - m.x165 == -0.00037)

m.c66 = Constraint(expr= - m.x78 - m.x146 + m.x167 == -0.00646)

m.c67 = Constraint(expr= - m.x128 == -0.025)

m.c68 = Constraint(expr= - m.x147 - m.x166 + m.x168 + m.x169 == -0.00215)

m.c69 = Constraint(expr= - m.x148 - m.x169 + m.x170 == -0.00175)

m.c70 = Constraint(expr=SignPower(m.x72,1.852) - 0.786293616578897*(1.27323954473516*m.x171)**2.435*(m.x1 - m.x2) == 0)

m.c71 = Constraint(expr=SignPower(m.x73,1.852) - 3.96579589792316*(1.27323954473516*m.x172)**2.435*(m.x2 - m.x4) == 0)

m.c72 = Constraint(expr=SignPower(m.x74,1.852) - 2.85038362486388*(1.27323954473516*m.x173)**2.435*(m.x3 - m.x1) == 0)

m.c73 = Constraint(expr=SignPower(m.x75,1.852) - 1.73407931290374*(1.27323954473516*m.x174)**2.435*(m.x3 - m.x4) == 0)

m.c74 = Constraint(expr=SignPower(m.x76,1.852) - 0.544732259049704*(1.27323954473516*m.x175)**2.435*(m.x3 - m.x5) == 0)

m.c75 = Constraint(expr=SignPower(m.x77,1.852) - 1.0485202258054*(1.27323954473516*m.x176)**2.435*(m.x4 - m.x58) == 0)

m.c76 = Constraint(expr=SignPower(m.x78,1.852) - 0.480307455687219*(1.27323954473516*m.x177)**2.435*(m.x5 - m.x68) == 0)

m.c77 = Constraint(expr=SignPower(m.x79,1.852) - 6.59536499398859*(1.27323954473516*m.x178)**2.435*(m.x6 - m.x7) == 0)

m.c78 = Constraint(expr=SignPower(m.x80,1.852) - 3.78455593962154*(1.27323954473516*m.x179)**2.435*(m.x6 - m.x8) == 0)

m.c79 = Constraint(expr=SignPower(m.x81,1.852) - 1.0660173798024*(1.27323954473516*m.x180)**2.435*(m.x8 - m.x28) == 0)

m.c80 = Constraint(expr=SignPower(m.x82,1.852) - 0.332804389989152*(1.27323954473516*m.x181)**2.435*(m.x9 - m.x6) == 0)

m.c81 = Constraint(expr=SignPower(m.x83,1.852) - 1.38696926274103*(1.27323954473516*m.x182)**2.435*(m.x9 - m.x39) == 0)

m.c82 = Constraint(expr=SignPower(m.x84,1.852) - 0.519258320449973*(1.27323954473516*m.x183)**2.435*(m.x10 - m.x11)
                         == 0)

m.c83 = Constraint(expr=SignPower(m.x85,1.852) - 0.631376002612248*(1.27323954473516*m.x184)**2.435*(m.x12 - m.x38)
                         == 0)

m.c84 = Constraint(expr=SignPower(m.x86,1.852) - 1.30438578501519*(1.27323954473516*m.x185)**2.435*(m.x13 - m.x16) == 0)

m.c85 = Constraint(expr=SignPower(m.x87,1.852) - 4.49305384178876*(1.27323954473516*m.x186)**2.435*(m.x14 - m.x23) == 0)

m.c86 = Constraint(expr=SignPower(m.x88,1.852) - 17.477642235605*(1.27323954473516*m.x187)**2.435*(m.x15 - m.x14) == 0)

m.c87 = Constraint(expr=SignPower(m.x89,1.852) - 1.24244891775589*(1.27323954473516*m.x188)**2.435*(m.x17 - m.x13) == 0)

m.c88 = Constraint(expr=SignPower(m.x90,1.852) - 2.25298132248476*(1.27323954473516*m.x189)**2.435*(m.x17 - m.x18) == 0)

m.c89 = Constraint(expr=SignPower(m.x91,1.852) - 1.26141511268248*(1.27323954473516*m.x190)**2.435*(m.x18 - m.x19) == 0)

m.c90 = Constraint(expr=SignPower(m.x92,1.852) - 13.8917557682493*(1.27323954473516*m.x191)**2.435*(m.x18 - m.x37) == 0)

m.c91 = Constraint(expr=SignPower(m.x93,1.852) - 2.24757817354805*(1.27323954473516*m.x192)**2.435*(m.x19 - m.x17) == 0)

m.c92 = Constraint(expr=SignPower(m.x94,1.852) - 0.911053595764831*(1.27323954473516*m.x193)**2.435*(m.x19 - m.x26)
                         == 0)

m.c93 = Constraint(expr=SignPower(m.x95,1.852) - 1.76974007253949*(1.27323954473516*m.x194)**2.435*(m.x20 - m.x19) == 0)

m.c94 = Constraint(expr=SignPower(m.x96,1.852) - 1.02501124269687*(1.27323954473516*m.x195)**2.435*(m.x20 - m.x21) == 0)

m.c95 = Constraint(expr=SignPower(m.x97,1.852) - 3.19419730287855*(1.27323954473516*m.x196)**2.435*(m.x21 - m.x22) == 0)

m.c96 = Constraint(expr=SignPower(m.x98,1.852) - 0.913099496333959*(1.27323954473516*m.x197)**2.435*(m.x21 - m.x67)
                         == 0)

m.c97 = Constraint(expr=SignPower(m.x99,1.852) - 1.20133176348218*(1.27323954473516*m.x198)**2.435*(m.x22 - m.x20) == 0)

m.c98 = Constraint(expr=SignPower(m.x100,1.852) - 3.26226569214904*(1.27323954473516*m.x199)**2.435*(m.x23 - m.x16)
                         == 0)

m.c99 = Constraint(expr=SignPower(m.x101,1.852) - 0.802652833701903*(1.27323954473516*m.x200)**2.435*(m.x23 - m.x24)
                         == 0)

m.c100 = Constraint(expr=SignPower(m.x102,1.852) - 2.10073787408985*(1.27323954473516*m.x201)**2.435*(m.x24 - m.x12)
                          == 0)

m.c101 = Constraint(expr=SignPower(m.x103,1.852) - 214.064604206003*(1.27323954473516*m.x202)**2.435*(m.x25 - m.x16)
                          == 0)

m.c102 = Constraint(expr=SignPower(m.x104,1.852) - 2.36925616321233*(1.27323954473516*m.x203)**2.435*(m.x25 - m.x26)
                          == 0)

m.c103 = Constraint(expr=SignPower(m.x105,1.852) - 1.27745591459083*(1.27323954473516*m.x204)**2.435*(m.x25 - m.x65)
                          == 0)

m.c104 = Constraint(expr=SignPower(m.x106,1.852) - 1.81698056294964*(1.27323954473516*m.x205)**2.435*(m.x26 - m.x22)
                          == 0)

m.c105 = Constraint(expr=SignPower(m.x107,1.852) - 4.29229182919767*(1.27323954473516*m.x206)**2.435*(m.x27 - m.x28)
                          == 0)

m.c106 = Constraint(expr=SignPower(m.x108,1.852) - 1.34610602399641*(1.27323954473516*m.x207)**2.435*(m.x27 - m.x29)
                          == 0)

m.c107 = Constraint(expr=SignPower(m.x109,1.852) - 23.1125392210391*(1.27323954473516*m.x208)**2.435*(m.x28 - m.x34)
                          == 0)

m.c108 = Constraint(expr=SignPower(m.x110,1.852) - 1.33481307053576*(1.27323954473516*m.x209)**2.435*(m.x29 - m.x27)
                          == 0)

m.c109 = Constraint(expr=SignPower(m.x111,1.852) - 1.73823692994854*(1.27323954473516*m.x210)**2.435*(m.x29 - m.x32)
                          == 0)

m.c110 = Constraint(expr=SignPower(m.x112,1.852) - 0.403672713906527*(1.27323954473516*m.x211)**2.435*(m.x30 - m.x11)
                          == 0)

m.c111 = Constraint(expr=SignPower(m.x113,1.852) - 3.07052872422707*(1.27323954473516*m.x212)**2.435*(m.x30 - m.x31)
                          == 0)

m.c112 = Constraint(expr=SignPower(m.x114,1.852) - 141.527058766031*(1.27323954473516*m.x213)**2.435*(m.x31 - m.x48)
                          == 0)

m.c113 = Constraint(expr=SignPower(m.x115,1.852) - 2.51527486367804*(1.27323954473516*m.x214)**2.435*(m.x32 - m.x9)
                          == 0)

m.c114 = Constraint(expr=SignPower(m.x116,1.852) - 1.0080565738828*(1.27323954473516*m.x215)**2.435*(m.x33 - m.x29)
                          == 0)

m.c115 = Constraint(expr=SignPower(m.x117,1.852) - 12.0434403557366*(1.27323954473516*m.x216)**2.435*(m.x33 - m.x40)
                          == 0)

m.c116 = Constraint(expr=SignPower(m.x118,1.852) - 0.545676034096803*(1.27323954473516*m.x217)**2.435*(m.x34 - m.x24)
                          == 0)

m.c117 = Constraint(expr=SignPower(m.x119,1.852) - 0.683164662725176*(1.27323954473516*m.x218)**2.435*(m.x34 - m.x35)
                          == 0)

m.c118 = Constraint(expr=SignPower(m.x120,1.852) - 6.12295378136842*(1.27323954473516*m.x219)**2.435*(m.x36 - m.x30)
                          == 0)

m.c119 = Constraint(expr=SignPower(m.x121,1.852) - 6.33703248206111*(1.27323954473516*m.x220)**2.435*(m.x36 - m.x37)
                          == 0)

m.c120 = Constraint(expr=SignPower(m.x122,1.852) - 2.47294352265269*(1.27323954473516*m.x221)**2.435*(m.x38 - m.x33)
                          == 0)

m.c121 = Constraint(expr=SignPower(m.x123,1.852) - 1.80881214776526*(1.27323954473516*m.x222)**2.435*(m.x39 - m.x38)
                          == 0)

m.c122 = Constraint(expr=SignPower(m.x124,1.852) - 10.5562078173015*(1.27323954473516*m.x223)**2.435*(m.x39 - m.x40)
                          == 0)

m.c123 = Constraint(expr=SignPower(m.x125,1.852) - 1.35214556012941*(1.27323954473516*m.x224)**2.435*(m.x40 - m.x32)
                          == 0)

m.c124 = Constraint(expr=SignPower(m.x126,1.852) - 1.73988980755632*(1.27323954473516*m.x225)**2.435*(m.x41 - m.x11)
                          == 0)

m.c125 = Constraint(expr=SignPower(m.x127,1.852) - 2.30785287576068*(1.27323954473516*m.x226)**2.435*(m.x42 - m.x41)
                          == 0)

m.c126 = Constraint(expr=SignPower(m.x128,1.852) - 76.849192909955*(1.27323954473516*m.x227)**2.435*(m.x42 - m.x69)
                          == 0)

m.c127 = Constraint(expr=SignPower(m.x129,1.852) - 3.34344976767261*(1.27323954473516*m.x228)**2.435*(m.x43 - m.x41)
                          == 0)

m.c128 = Constraint(expr=SignPower(m.x130,1.852) - 1.9471759421784*(1.27323954473516*m.x229)**2.435*(m.x43 - m.x56)
                          == 0)

m.c129 = Constraint(expr=SignPower(m.x131,1.852) - 1.5341610019555*(1.27323954473516*m.x230)**2.435*(m.x44 - m.x45)
                          == 0)

m.c130 = Constraint(expr=SignPower(m.x132,1.852) - 2.18962284269183*(1.27323954473516*m.x231)**2.435*(m.x44 - m.x51)
                          == 0)

m.c131 = Constraint(expr=SignPower(m.x133,1.852) - 11.6016293644256*(1.27323954473516*m.x232)**2.435*(m.x45 - m.x31)
                          == 0)

m.c132 = Constraint(expr=SignPower(m.x134,1.852) - 3.31146606239303*(1.27323954473516*m.x233)**2.435*(m.x46 - m.x47)
                          == 0)

m.c133 = Constraint(expr=SignPower(m.x135,1.852) - 1.19127566129213*(1.27323954473516*m.x234)**2.435*(m.x47 - m.x48)
                          == 0)

m.c134 = Constraint(expr=SignPower(m.x136,1.852) - 4.96505962720991*(1.27323954473516*m.x235)**2.435*(m.x48 - m.x49)
                          == 0)

m.c135 = Constraint(expr=SignPower(m.x137,1.852) - 3.3106101283744*(1.27323954473516*m.x236)**2.435*(m.x49 - m.x45)
                          == 0)

m.c136 = Constraint(expr=SignPower(m.x138,1.852) - 1.19000283234418*(1.27323954473516*m.x237)**2.435*(m.x49 - m.x50)
                          == 0)

m.c137 = Constraint(expr=SignPower(m.x139,1.852) - 4.86787818521284*(1.27323954473516*m.x238)**2.435*(m.x50 - m.x47)
                          == 0)

m.c138 = Constraint(expr=SignPower(m.x140,1.852) - 4.90265983476587*(1.27323954473516*m.x239)**2.435*(m.x50 - m.x52)
                          == 0)

m.c139 = Constraint(expr=SignPower(m.x141,1.852) - 3.71808955004863*(1.27323954473516*m.x240)**2.435*(m.x51 - m.x49)
                          == 0)

m.c140 = Constraint(expr=SignPower(m.x142,1.852) - 1.21635316413351*(1.27323954473516*m.x241)**2.435*(m.x51 - m.x52)
                          == 0)

m.c141 = Constraint(expr=SignPower(m.x143,1.852) - 5.02906831424351*(1.27323954473516*m.x242)**2.435*(m.x53 - m.x54)
                          == 0)

m.c142 = Constraint(expr=SignPower(m.x144,1.852) - 4.26939960610861*(1.27323954473516*m.x243)**2.435*(m.x53 - m.x66)
                          == 0)

m.c143 = Constraint(expr=SignPower(m.x145,1.852) - 0.688520296644313*(1.27323954473516*m.x244)**2.435*(m.x54 - m.x60)
                          == 0)

m.c144 = Constraint(expr=SignPower(m.x146,1.852) - 4.64542059541528*(1.27323954473516*m.x245)**2.435*(m.x54 - m.x68)
                          == 0)

m.c145 = Constraint(expr=SignPower(m.x147,1.852) - 2.31229706363638*(1.27323954473516*m.x246)**2.435*(m.x54 - m.x70)
                          == 0)

m.c146 = Constraint(expr=SignPower(m.x148,1.852) - 4.28033824829871*(1.27323954473516*m.x247)**2.435*(m.x54 - m.x71)
                          == 0)

m.c147 = Constraint(expr=SignPower(m.x149,1.852) - 0.99199928887626*(1.27323954473516*m.x248)**2.435*(m.x55 - m.x43)
                          == 0)

m.c148 = Constraint(expr=SignPower(m.x150,1.852) - 14.6742778136252*(1.27323954473516*m.x249)**2.435*(m.x55 - m.x46)
                          == 0)

m.c149 = Constraint(expr=SignPower(m.x151,1.852) - 1.76429571858109*(1.27323954473516*m.x250)**2.435*(m.x56 - m.x55)
                          == 0)

m.c150 = Constraint(expr=SignPower(m.x152,1.852) - 0.854193125367691*(1.27323954473516*m.x251)**2.435*(m.x57 - m.x56)
                          == 0)

m.c151 = Constraint(expr=SignPower(m.x153,1.852) - 2.278768619083*(1.27323954473516*m.x252)**2.435*(m.x57 - m.x59) == 0)

m.c152 = Constraint(expr=SignPower(m.x154,1.852) - 3.87149586448136*(1.27323954473516*m.x253)**2.435*(m.x58 - m.x59)
                          == 0)

m.c153 = Constraint(expr=SignPower(m.x155,1.852) - 8.89561209745978*(1.27323954473516*m.x254)**2.435*(m.x58 - m.x61)
                          == 0)

m.c154 = Constraint(expr=SignPower(m.x156,1.852) - 4.11464329977807*(1.27323954473516*m.x255)**2.435*(m.x59 - m.x60)
                          == 0)

m.c155 = Constraint(expr=SignPower(m.x157,1.852) - 3.39995544440804*(1.27323954473516*m.x256)**2.435*(m.x60 - m.x5)
                          == 0)

m.c156 = Constraint(expr=SignPower(m.x158,1.852) - 0.979656994199185*(1.27323954473516*m.x257)**2.435*(m.x61 - m.x2)
                          == 0)

m.c157 = Constraint(expr=SignPower(m.x159,1.852) - 4.43984013576492*(1.27323954473516*m.x258)**2.435*(m.x61 - m.x57)
                          == 0)

m.c158 = Constraint(expr=SignPower(m.x160,1.852) - 0.440580832726327*(1.27323954473516*m.x259)**2.435*(m.x62 - m.x6)
                          == 0)

m.c159 = Constraint(expr=SignPower(m.x161,1.852) - 4.98438143144085*(1.27323954473516*m.x260)**2.435*(m.x62 - m.x63)
                          == 0)

m.c160 = Constraint(expr=SignPower(m.x162,1.852) - 0.716415673772992*(1.27323954473516*m.x261)**2.435*(m.x63 - m.x8)
                          == 0)

m.c161 = Constraint(expr=SignPower(m.x163,1.852) - 153.69838581991*(1.27323954473516*m.x262)**2.435*(m.x64 - m.x65)
                          == 0)

m.c162 = Constraint(expr=SignPower(m.x164,1.852) - 3.20138274984191*(1.27323954473516*m.x263)**2.435*(m.x64 - m.x67)
                          == 0)

m.c163 = Constraint(expr=SignPower(m.x165,1.852) - 3.20204970458146*(1.27323954473516*m.x264)**2.435*(m.x65 - m.x67)
                          == 0)

m.c164 = Constraint(expr=SignPower(m.x166,1.852) - 6.77981410762726*(1.27323954473516*m.x265)**2.435*(m.x66 - m.x70)
                          == 0)

m.c165 = Constraint(expr=SignPower(m.x167,1.852) - 0.469827368938827*(1.27323954473516*m.x266)**2.435*(m.x68 - m.x44)
                          == 0)

m.c166 = Constraint(expr=SignPower(m.x168,1.852) - 2.36437230132465*(1.27323954473516*m.x267)**2.435*(m.x70 - m.x50)
                          == 0)

m.c167 = Constraint(expr=SignPower(m.x169,1.852) - 5.09542453984584*(1.27323954473516*m.x268)**2.435*(m.x70 - m.x71)
                          == 0)

m.c168 = Constraint(expr=SignPower(m.x170,1.852) - 2.31892555552067*(1.27323954473516*m.x269)**2.435*(m.x71 - m.x52)
                          == 0)

m.c169 = Constraint(expr=   m.x72 - 2*m.x171 <= 0)

m.c170 = Constraint(expr=   m.x73 - 2*m.x172 <= 0)

m.c171 = Constraint(expr=   m.x74 - 2*m.x173 <= 0)

m.c172 = Constraint(expr=   m.x75 - 2*m.x174 <= 0)

m.c173 = Constraint(expr=   m.x76 - 2*m.x175 <= 0)

m.c174 = Constraint(expr=   m.x77 - 2*m.x176 <= 0)

m.c175 = Constraint(expr=   m.x78 - 2*m.x177 <= 0)

m.c176 = Constraint(expr=   m.x79 - 2*m.x178 <= 0)

m.c177 = Constraint(expr=   m.x80 - 2*m.x179 <= 0)

m.c178 = Constraint(expr=   m.x81 - 2*m.x180 <= 0)

m.c179 = Constraint(expr=   m.x82 - 2*m.x181 <= 0)

m.c180 = Constraint(expr=   m.x83 - 2*m.x182 <= 0)

m.c181 = Constraint(expr=   m.x84 - 2*m.x183 <= 0)

m.c182 = Constraint(expr=   m.x85 - 2*m.x184 <= 0)

m.c183 = Constraint(expr=   m.x86 - 2*m.x185 <= 0)

m.c184 = Constraint(expr=   m.x87 - 2*m.x186 <= 0)

m.c185 = Constraint(expr=   m.x88 - 2*m.x187 <= 0)

m.c186 = Constraint(expr=   m.x89 - 2*m.x188 <= 0)

m.c187 = Constraint(expr=   m.x90 - 2*m.x189 <= 0)

m.c188 = Constraint(expr=   m.x91 - 2*m.x190 <= 0)

m.c189 = Constraint(expr=   m.x92 - 2*m.x191 <= 0)

m.c190 = Constraint(expr=   m.x93 - 2*m.x192 <= 0)

m.c191 = Constraint(expr=   m.x94 - 2*m.x193 <= 0)

m.c192 = Constraint(expr=   m.x95 - 2*m.x194 <= 0)

m.c193 = Constraint(expr=   m.x96 - 2*m.x195 <= 0)

m.c194 = Constraint(expr=   m.x97 - 2*m.x196 <= 0)

m.c195 = Constraint(expr=   m.x98 - 2*m.x197 <= 0)

m.c196 = Constraint(expr=   m.x99 - 2*m.x198 <= 0)

m.c197 = Constraint(expr=   m.x100 - 2*m.x199 <= 0)

m.c198 = Constraint(expr=   m.x101 - 2*m.x200 <= 0)

m.c199 = Constraint(expr=   m.x102 - 2*m.x201 <= 0)

m.c200 = Constraint(expr=   m.x103 - 2*m.x202 <= 0)

m.c201 = Constraint(expr=   m.x104 - 2*m.x203 <= 0)

m.c202 = Constraint(expr=   m.x105 - 2*m.x204 <= 0)

m.c203 = Constraint(expr=   m.x106 - 2*m.x205 <= 0)

m.c204 = Constraint(expr=   m.x107 - 2*m.x206 <= 0)

m.c205 = Constraint(expr=   m.x108 - 2*m.x207 <= 0)

m.c206 = Constraint(expr=   m.x109 - 2*m.x208 <= 0)

m.c207 = Constraint(expr=   m.x110 - 2*m.x209 <= 0)

m.c208 = Constraint(expr=   m.x111 - 2*m.x210 <= 0)

m.c209 = Constraint(expr=   m.x112 - 2*m.x211 <= 0)

m.c210 = Constraint(expr=   m.x113 - 2*m.x212 <= 0)

m.c211 = Constraint(expr=   m.x114 - 2*m.x213 <= 0)

m.c212 = Constraint(expr=   m.x115 - 2*m.x214 <= 0)

m.c213 = Constraint(expr=   m.x116 - 2*m.x215 <= 0)

m.c214 = Constraint(expr=   m.x117 - 2*m.x216 <= 0)

m.c215 = Constraint(expr=   m.x118 - 2*m.x217 <= 0)

m.c216 = Constraint(expr=   m.x119 - 2*m.x218 <= 0)

m.c217 = Constraint(expr=   m.x120 - 2*m.x219 <= 0)

m.c218 = Constraint(expr=   m.x121 - 2*m.x220 <= 0)

m.c219 = Constraint(expr=   m.x122 - 2*m.x221 <= 0)

m.c220 = Constraint(expr=   m.x123 - 2*m.x222 <= 0)

m.c221 = Constraint(expr=   m.x124 - 2*m.x223 <= 0)

m.c222 = Constraint(expr=   m.x125 - 2*m.x224 <= 0)

m.c223 = Constraint(expr=   m.x126 - 2*m.x225 <= 0)

m.c224 = Constraint(expr=   m.x127 - 2*m.x226 <= 0)

m.c225 = Constraint(expr=   m.x128 - 2*m.x227 <= 0)

m.c226 = Constraint(expr=   m.x129 - 2*m.x228 <= 0)

m.c227 = Constraint(expr=   m.x130 - 2*m.x229 <= 0)

m.c228 = Constraint(expr=   m.x131 - 2*m.x230 <= 0)

m.c229 = Constraint(expr=   m.x132 - 2*m.x231 <= 0)

m.c230 = Constraint(expr=   m.x133 - 2*m.x232 <= 0)

m.c231 = Constraint(expr=   m.x134 - 2*m.x233 <= 0)

m.c232 = Constraint(expr=   m.x135 - 2*m.x234 <= 0)

m.c233 = Constraint(expr=   m.x136 - 2*m.x235 <= 0)

m.c234 = Constraint(expr=   m.x137 - 2*m.x236 <= 0)

m.c235 = Constraint(expr=   m.x138 - 2*m.x237 <= 0)

m.c236 = Constraint(expr=   m.x139 - 2*m.x238 <= 0)

m.c237 = Constraint(expr=   m.x140 - 2*m.x239 <= 0)

m.c238 = Constraint(expr=   m.x141 - 2*m.x240 <= 0)

m.c239 = Constraint(expr=   m.x142 - 2*m.x241 <= 0)

m.c240 = Constraint(expr=   m.x143 - 2*m.x242 <= 0)

m.c241 = Constraint(expr=   m.x144 - 2*m.x243 <= 0)

m.c242 = Constraint(expr=   m.x145 - 2*m.x244 <= 0)

m.c243 = Constraint(expr=   m.x146 - 2*m.x245 <= 0)

m.c244 = Constraint(expr=   m.x147 - 2*m.x246 <= 0)

m.c245 = Constraint(expr=   m.x148 - 2*m.x247 <= 0)

m.c246 = Constraint(expr=   m.x149 - 2*m.x248 <= 0)

m.c247 = Constraint(expr=   m.x150 - 2*m.x249 <= 0)

m.c248 = Constraint(expr=   m.x151 - 2*m.x250 <= 0)

m.c249 = Constraint(expr=   m.x152 - 2*m.x251 <= 0)

m.c250 = Constraint(expr=   m.x153 - 2*m.x252 <= 0)

m.c251 = Constraint(expr=   m.x154 - 2*m.x253 <= 0)

m.c252 = Constraint(expr=   m.x155 - 2*m.x254 <= 0)

m.c253 = Constraint(expr=   m.x156 - 2*m.x255 <= 0)

m.c254 = Constraint(expr=   m.x157 - 2*m.x256 <= 0)

m.c255 = Constraint(expr=   m.x158 - 2*m.x257 <= 0)

m.c256 = Constraint(expr=   m.x159 - 2*m.x258 <= 0)

m.c257 = Constraint(expr=   m.x160 - 2*m.x259 <= 0)

m.c258 = Constraint(expr=   m.x161 - 2*m.x260 <= 0)

m.c259 = Constraint(expr=   m.x162 - 2*m.x261 <= 0)

m.c260 = Constraint(expr=   m.x163 - 2*m.x262 <= 0)

m.c261 = Constraint(expr=   m.x164 - 2*m.x263 <= 0)

m.c262 = Constraint(expr=   m.x165 - 2*m.x264 <= 0)

m.c263 = Constraint(expr=   m.x166 - 2*m.x265 <= 0)

m.c264 = Constraint(expr=   m.x167 - 2*m.x266 <= 0)

m.c265 = Constraint(expr=   m.x168 - 2*m.x267 <= 0)

m.c266 = Constraint(expr=   m.x169 - 2*m.x268 <= 0)

m.c267 = Constraint(expr=   m.x170 - 2*m.x269 <= 0)

m.c268 = Constraint(expr=   m.x72 + 2*m.x171 >= 0)

m.c269 = Constraint(expr=   m.x73 + 2*m.x172 >= 0)

m.c270 = Constraint(expr=   m.x74 + 2*m.x173 >= 0)

m.c271 = Constraint(expr=   m.x75 + 2*m.x174 >= 0)

m.c272 = Constraint(expr=   m.x76 + 2*m.x175 >= 0)

m.c273 = Constraint(expr=   m.x77 + 2*m.x176 >= 0)

m.c274 = Constraint(expr=   m.x78 + 2*m.x177 >= 0)

m.c275 = Constraint(expr=   m.x79 + 2*m.x178 >= 0)

m.c276 = Constraint(expr=   m.x80 + 2*m.x179 >= 0)

m.c277 = Constraint(expr=   m.x81 + 2*m.x180 >= 0)

m.c278 = Constraint(expr=   m.x82 + 2*m.x181 >= 0)

m.c279 = Constraint(expr=   m.x83 + 2*m.x182 >= 0)

m.c280 = Constraint(expr=   m.x84 + 2*m.x183 >= 0)

m.c281 = Constraint(expr=   m.x85 + 2*m.x184 >= 0)

m.c282 = Constraint(expr=   m.x86 + 2*m.x185 >= 0)

m.c283 = Constraint(expr=   m.x87 + 2*m.x186 >= 0)

m.c284 = Constraint(expr=   m.x88 + 2*m.x187 >= 0)

m.c285 = Constraint(expr=   m.x89 + 2*m.x188 >= 0)

m.c286 = Constraint(expr=   m.x90 + 2*m.x189 >= 0)

m.c287 = Constraint(expr=   m.x91 + 2*m.x190 >= 0)

m.c288 = Constraint(expr=   m.x92 + 2*m.x191 >= 0)

m.c289 = Constraint(expr=   m.x93 + 2*m.x192 >= 0)

m.c290 = Constraint(expr=   m.x94 + 2*m.x193 >= 0)

m.c291 = Constraint(expr=   m.x95 + 2*m.x194 >= 0)

m.c292 = Constraint(expr=   m.x96 + 2*m.x195 >= 0)

m.c293 = Constraint(expr=   m.x97 + 2*m.x196 >= 0)

m.c294 = Constraint(expr=   m.x98 + 2*m.x197 >= 0)

m.c295 = Constraint(expr=   m.x99 + 2*m.x198 >= 0)

m.c296 = Constraint(expr=   m.x100 + 2*m.x199 >= 0)

m.c297 = Constraint(expr=   m.x101 + 2*m.x200 >= 0)

m.c298 = Constraint(expr=   m.x102 + 2*m.x201 >= 0)

m.c299 = Constraint(expr=   m.x103 + 2*m.x202 >= 0)

m.c300 = Constraint(expr=   m.x104 + 2*m.x203 >= 0)

m.c301 = Constraint(expr=   m.x105 + 2*m.x204 >= 0)

m.c302 = Constraint(expr=   m.x106 + 2*m.x205 >= 0)

m.c303 = Constraint(expr=   m.x107 + 2*m.x206 >= 0)

m.c304 = Constraint(expr=   m.x108 + 2*m.x207 >= 0)

m.c305 = Constraint(expr=   m.x109 + 2*m.x208 >= 0)

m.c306 = Constraint(expr=   m.x110 + 2*m.x209 >= 0)

m.c307 = Constraint(expr=   m.x111 + 2*m.x210 >= 0)

m.c308 = Constraint(expr=   m.x112 + 2*m.x211 >= 0)

m.c309 = Constraint(expr=   m.x113 + 2*m.x212 >= 0)

m.c310 = Constraint(expr=   m.x114 + 2*m.x213 >= 0)

m.c311 = Constraint(expr=   m.x115 + 2*m.x214 >= 0)

m.c312 = Constraint(expr=   m.x116 + 2*m.x215 >= 0)

m.c313 = Constraint(expr=   m.x117 + 2*m.x216 >= 0)

m.c314 = Constraint(expr=   m.x118 + 2*m.x217 >= 0)

m.c315 = Constraint(expr=   m.x119 + 2*m.x218 >= 0)

m.c316 = Constraint(expr=   m.x120 + 2*m.x219 >= 0)

m.c317 = Constraint(expr=   m.x121 + 2*m.x220 >= 0)

m.c318 = Constraint(expr=   m.x122 + 2*m.x221 >= 0)

m.c319 = Constraint(expr=   m.x123 + 2*m.x222 >= 0)

m.c320 = Constraint(expr=   m.x124 + 2*m.x223 >= 0)

m.c321 = Constraint(expr=   m.x125 + 2*m.x224 >= 0)

m.c322 = Constraint(expr=   m.x126 + 2*m.x225 >= 0)

m.c323 = Constraint(expr=   m.x127 + 2*m.x226 >= 0)

m.c324 = Constraint(expr=   m.x128 + 2*m.x227 >= 0)

m.c325 = Constraint(expr=   m.x129 + 2*m.x228 >= 0)

m.c326 = Constraint(expr=   m.x130 + 2*m.x229 >= 0)

m.c327 = Constraint(expr=   m.x131 + 2*m.x230 >= 0)

m.c328 = Constraint(expr=   m.x132 + 2*m.x231 >= 0)

m.c329 = Constraint(expr=   m.x133 + 2*m.x232 >= 0)

m.c330 = Constraint(expr=   m.x134 + 2*m.x233 >= 0)

m.c331 = Constraint(expr=   m.x135 + 2*m.x234 >= 0)

m.c332 = Constraint(expr=   m.x136 + 2*m.x235 >= 0)

m.c333 = Constraint(expr=   m.x137 + 2*m.x236 >= 0)

m.c334 = Constraint(expr=   m.x138 + 2*m.x237 >= 0)

m.c335 = Constraint(expr=   m.x139 + 2*m.x238 >= 0)

m.c336 = Constraint(expr=   m.x140 + 2*m.x239 >= 0)

m.c337 = Constraint(expr=   m.x141 + 2*m.x240 >= 0)

m.c338 = Constraint(expr=   m.x142 + 2*m.x241 >= 0)

m.c339 = Constraint(expr=   m.x143 + 2*m.x242 >= 0)

m.c340 = Constraint(expr=   m.x144 + 2*m.x243 >= 0)

m.c341 = Constraint(expr=   m.x145 + 2*m.x244 >= 0)

m.c342 = Constraint(expr=   m.x146 + 2*m.x245 >= 0)

m.c343 = Constraint(expr=   m.x147 + 2*m.x246 >= 0)

m.c344 = Constraint(expr=   m.x148 + 2*m.x247 >= 0)

m.c345 = Constraint(expr=   m.x149 + 2*m.x248 >= 0)

m.c346 = Constraint(expr=   m.x150 + 2*m.x249 >= 0)

m.c347 = Constraint(expr=   m.x151 + 2*m.x250 >= 0)

m.c348 = Constraint(expr=   m.x152 + 2*m.x251 >= 0)

m.c349 = Constraint(expr=   m.x153 + 2*m.x252 >= 0)

m.c350 = Constraint(expr=   m.x154 + 2*m.x253 >= 0)

m.c351 = Constraint(expr=   m.x155 + 2*m.x254 >= 0)

m.c352 = Constraint(expr=   m.x156 + 2*m.x255 >= 0)

m.c353 = Constraint(expr=   m.x157 + 2*m.x256 >= 0)

m.c354 = Constraint(expr=   m.x158 + 2*m.x257 >= 0)

m.c355 = Constraint(expr=   m.x159 + 2*m.x258 >= 0)

m.c356 = Constraint(expr=   m.x160 + 2*m.x259 >= 0)

m.c357 = Constraint(expr=   m.x161 + 2*m.x260 >= 0)

m.c358 = Constraint(expr=   m.x162 + 2*m.x261 >= 0)

m.c359 = Constraint(expr=   m.x163 + 2*m.x262 >= 0)

m.c360 = Constraint(expr=   m.x164 + 2*m.x263 >= 0)

m.c361 = Constraint(expr=   m.x165 + 2*m.x264 >= 0)

m.c362 = Constraint(expr=   m.x166 + 2*m.x265 >= 0)

m.c363 = Constraint(expr=   m.x167 + 2*m.x266 >= 0)

m.c364 = Constraint(expr=   m.x168 + 2*m.x267 >= 0)

m.c365 = Constraint(expr=   m.x169 + 2*m.x268 >= 0)

m.c366 = Constraint(expr=   m.x170 + 2*m.x269 >= 0)

m.c367 = Constraint(expr=   m.x171 - 0.00785398163397448*m.b270 - 0.0122718463030851*m.b271 - 0.0176714586764426*m.b272
                          - 0.0314159265358979*m.b273 - 0.0490873852123405*m.b274 - 0.0706858347057703*m.b275
                          - 0.0962112750161874*m.b276 - 0.125663706143592*m.b277 - 0.159043128087983*m.b278
                          - 0.196349540849362*m.b279 - 0.282743338823081*m.b280 - 0.38484510006475*m.b281
                          - 0.502654824574367*m.b282 == 0)

m.c368 = Constraint(expr=   m.x172 - 0.00785398163397448*m.b283 - 0.0122718463030851*m.b284 - 0.0176714586764426*m.b285
                          - 0.0314159265358979*m.b286 - 0.0490873852123405*m.b287 - 0.0706858347057703*m.b288
                          - 0.0962112750161874*m.b289 - 0.125663706143592*m.b290 - 0.159043128087983*m.b291
                          - 0.196349540849362*m.b292 - 0.282743338823081*m.b293 - 0.38484510006475*m.b294
                          - 0.502654824574367*m.b295 == 0)

m.c369 = Constraint(expr=   m.x173 - 0.00785398163397448*m.b296 - 0.0122718463030851*m.b297 - 0.0176714586764426*m.b298
                          - 0.0314159265358979*m.b299 - 0.0490873852123405*m.b300 - 0.0706858347057703*m.b301
                          - 0.0962112750161874*m.b302 - 0.125663706143592*m.b303 - 0.159043128087983*m.b304
                          - 0.196349540849362*m.b305 - 0.282743338823081*m.b306 - 0.38484510006475*m.b307
                          - 0.502654824574367*m.b308 == 0)

m.c370 = Constraint(expr=   m.x174 - 0.00785398163397448*m.b309 - 0.0122718463030851*m.b310 - 0.0176714586764426*m.b311
                          - 0.0314159265358979*m.b312 - 0.0490873852123405*m.b313 - 0.0706858347057703*m.b314
                          - 0.0962112750161874*m.b315 - 0.125663706143592*m.b316 - 0.159043128087983*m.b317
                          - 0.196349540849362*m.b318 - 0.282743338823081*m.b319 - 0.38484510006475*m.b320
                          - 0.502654824574367*m.b321 == 0)

m.c371 = Constraint(expr=   m.x175 - 0.00785398163397448*m.b322 - 0.0122718463030851*m.b323 - 0.0176714586764426*m.b324
                          - 0.0314159265358979*m.b325 - 0.0490873852123405*m.b326 - 0.0706858347057703*m.b327
                          - 0.0962112750161874*m.b328 - 0.125663706143592*m.b329 - 0.159043128087983*m.b330
                          - 0.196349540849362*m.b331 - 0.282743338823081*m.b332 - 0.38484510006475*m.b333
                          - 0.502654824574367*m.b334 == 0)

m.c372 = Constraint(expr=   m.x176 - 0.00785398163397448*m.b335 - 0.0122718463030851*m.b336 - 0.0176714586764426*m.b337
                          - 0.0314159265358979*m.b338 - 0.0490873852123405*m.b339 - 0.0706858347057703*m.b340
                          - 0.0962112750161874*m.b341 - 0.125663706143592*m.b342 - 0.159043128087983*m.b343
                          - 0.196349540849362*m.b344 - 0.282743338823081*m.b345 - 0.38484510006475*m.b346
                          - 0.502654824574367*m.b347 == 0)

m.c373 = Constraint(expr=   m.x177 - 0.00785398163397448*m.b348 - 0.0122718463030851*m.b349 - 0.0176714586764426*m.b350
                          - 0.0314159265358979*m.b351 - 0.0490873852123405*m.b352 - 0.0706858347057703*m.b353
                          - 0.0962112750161874*m.b354 - 0.125663706143592*m.b355 - 0.159043128087983*m.b356
                          - 0.196349540849362*m.b357 - 0.282743338823081*m.b358 - 0.38484510006475*m.b359
                          - 0.502654824574367*m.b360 == 0)

m.c374 = Constraint(expr=   m.x178 - 0.00785398163397448*m.b361 - 0.0122718463030851*m.b362 - 0.0176714586764426*m.b363
                          - 0.0314159265358979*m.b364 - 0.0490873852123405*m.b365 - 0.0706858347057703*m.b366
                          - 0.0962112750161874*m.b367 - 0.125663706143592*m.b368 - 0.159043128087983*m.b369
                          - 0.196349540849362*m.b370 - 0.282743338823081*m.b371 - 0.38484510006475*m.b372
                          - 0.502654824574367*m.b373 == 0)

m.c375 = Constraint(expr=   m.x179 - 0.00785398163397448*m.b374 - 0.0122718463030851*m.b375 - 0.0176714586764426*m.b376
                          - 0.0314159265358979*m.b377 - 0.0490873852123405*m.b378 - 0.0706858347057703*m.b379
                          - 0.0962112750161874*m.b380 - 0.125663706143592*m.b381 - 0.159043128087983*m.b382
                          - 0.196349540849362*m.b383 - 0.282743338823081*m.b384 - 0.38484510006475*m.b385
                          - 0.502654824574367*m.b386 == 0)

m.c376 = Constraint(expr=   m.x180 - 0.00785398163397448*m.b387 - 0.0122718463030851*m.b388 - 0.0176714586764426*m.b389
                          - 0.0314159265358979*m.b390 - 0.0490873852123405*m.b391 - 0.0706858347057703*m.b392
                          - 0.0962112750161874*m.b393 - 0.125663706143592*m.b394 - 0.159043128087983*m.b395
                          - 0.196349540849362*m.b396 - 0.282743338823081*m.b397 - 0.38484510006475*m.b398
                          - 0.502654824574367*m.b399 == 0)

m.c377 = Constraint(expr=   m.x181 - 0.00785398163397448*m.b400 - 0.0122718463030851*m.b401 - 0.0176714586764426*m.b402
                          - 0.0314159265358979*m.b403 - 0.0490873852123405*m.b404 - 0.0706858347057703*m.b405
                          - 0.0962112750161874*m.b406 - 0.125663706143592*m.b407 - 0.159043128087983*m.b408
                          - 0.196349540849362*m.b409 - 0.282743338823081*m.b410 - 0.38484510006475*m.b411
                          - 0.502654824574367*m.b412 == 0)

m.c378 = Constraint(expr=   m.x182 - 0.00785398163397448*m.b413 - 0.0122718463030851*m.b414 - 0.0176714586764426*m.b415
                          - 0.0314159265358979*m.b416 - 0.0490873852123405*m.b417 - 0.0706858347057703*m.b418
                          - 0.0962112750161874*m.b419 - 0.125663706143592*m.b420 - 0.159043128087983*m.b421
                          - 0.196349540849362*m.b422 - 0.282743338823081*m.b423 - 0.38484510006475*m.b424
                          - 0.502654824574367*m.b425 == 0)

m.c379 = Constraint(expr=   m.x183 - 0.00785398163397448*m.b426 - 0.0122718463030851*m.b427 - 0.0176714586764426*m.b428
                          - 0.0314159265358979*m.b429 - 0.0490873852123405*m.b430 - 0.0706858347057703*m.b431
                          - 0.0962112750161874*m.b432 - 0.125663706143592*m.b433 - 0.159043128087983*m.b434
                          - 0.196349540849362*m.b435 - 0.282743338823081*m.b436 - 0.38484510006475*m.b437
                          - 0.502654824574367*m.b438 == 0)

m.c380 = Constraint(expr=   m.x184 - 0.00785398163397448*m.b439 - 0.0122718463030851*m.b440 - 0.0176714586764426*m.b441
                          - 0.0314159265358979*m.b442 - 0.0490873852123405*m.b443 - 0.0706858347057703*m.b444
                          - 0.0962112750161874*m.b445 - 0.125663706143592*m.b446 - 0.159043128087983*m.b447
                          - 0.196349540849362*m.b448 - 0.282743338823081*m.b449 - 0.38484510006475*m.b450
                          - 0.502654824574367*m.b451 == 0)

m.c381 = Constraint(expr=   m.x185 - 0.00785398163397448*m.b452 - 0.0122718463030851*m.b453 - 0.0176714586764426*m.b454
                          - 0.0314159265358979*m.b455 - 0.0490873852123405*m.b456 - 0.0706858347057703*m.b457
                          - 0.0962112750161874*m.b458 - 0.125663706143592*m.b459 - 0.159043128087983*m.b460
                          - 0.196349540849362*m.b461 - 0.282743338823081*m.b462 - 0.38484510006475*m.b463
                          - 0.502654824574367*m.b464 == 0)

m.c382 = Constraint(expr=   m.x186 - 0.00785398163397448*m.b465 - 0.0122718463030851*m.b466 - 0.0176714586764426*m.b467
                          - 0.0314159265358979*m.b468 - 0.0490873852123405*m.b469 - 0.0706858347057703*m.b470
                          - 0.0962112750161874*m.b471 - 0.125663706143592*m.b472 - 0.159043128087983*m.b473
                          - 0.196349540849362*m.b474 - 0.282743338823081*m.b475 - 0.38484510006475*m.b476
                          - 0.502654824574367*m.b477 == 0)

m.c383 = Constraint(expr=   m.x187 - 0.00785398163397448*m.b478 - 0.0122718463030851*m.b479 - 0.0176714586764426*m.b480
                          - 0.0314159265358979*m.b481 - 0.0490873852123405*m.b482 - 0.0706858347057703*m.b483
                          - 0.0962112750161874*m.b484 - 0.125663706143592*m.b485 - 0.159043128087983*m.b486
                          - 0.196349540849362*m.b487 - 0.282743338823081*m.b488 - 0.38484510006475*m.b489
                          - 0.502654824574367*m.b490 == 0)

m.c384 = Constraint(expr=   m.x188 - 0.00785398163397448*m.b491 - 0.0122718463030851*m.b492 - 0.0176714586764426*m.b493
                          - 0.0314159265358979*m.b494 - 0.0490873852123405*m.b495 - 0.0706858347057703*m.b496
                          - 0.0962112750161874*m.b497 - 0.125663706143592*m.b498 - 0.159043128087983*m.b499
                          - 0.196349540849362*m.b500 - 0.282743338823081*m.b501 - 0.38484510006475*m.b502
                          - 0.502654824574367*m.b503 == 0)

m.c385 = Constraint(expr=   m.x189 - 0.00785398163397448*m.b504 - 0.0122718463030851*m.b505 - 0.0176714586764426*m.b506
                          - 0.0314159265358979*m.b507 - 0.0490873852123405*m.b508 - 0.0706858347057703*m.b509
                          - 0.0962112750161874*m.b510 - 0.125663706143592*m.b511 - 0.159043128087983*m.b512
                          - 0.196349540849362*m.b513 - 0.282743338823081*m.b514 - 0.38484510006475*m.b515
                          - 0.502654824574367*m.b516 == 0)

m.c386 = Constraint(expr=   m.x190 - 0.00785398163397448*m.b517 - 0.0122718463030851*m.b518 - 0.0176714586764426*m.b519
                          - 0.0314159265358979*m.b520 - 0.0490873852123405*m.b521 - 0.0706858347057703*m.b522
                          - 0.0962112750161874*m.b523 - 0.125663706143592*m.b524 - 0.159043128087983*m.b525
                          - 0.196349540849362*m.b526 - 0.282743338823081*m.b527 - 0.38484510006475*m.b528
                          - 0.502654824574367*m.b529 == 0)

m.c387 = Constraint(expr=   m.x191 - 0.00785398163397448*m.b530 - 0.0122718463030851*m.b531 - 0.0176714586764426*m.b532
                          - 0.0314159265358979*m.b533 - 0.0490873852123405*m.b534 - 0.0706858347057703*m.b535
                          - 0.0962112750161874*m.b536 - 0.125663706143592*m.b537 - 0.159043128087983*m.b538
                          - 0.196349540849362*m.b539 - 0.282743338823081*m.b540 - 0.38484510006475*m.b541
                          - 0.502654824574367*m.b542 == 0)

m.c388 = Constraint(expr=   m.x192 - 0.00785398163397448*m.b543 - 0.0122718463030851*m.b544 - 0.0176714586764426*m.b545
                          - 0.0314159265358979*m.b546 - 0.0490873852123405*m.b547 - 0.0706858347057703*m.b548
                          - 0.0962112750161874*m.b549 - 0.125663706143592*m.b550 - 0.159043128087983*m.b551
                          - 0.196349540849362*m.b552 - 0.282743338823081*m.b553 - 0.38484510006475*m.b554
                          - 0.502654824574367*m.b555 == 0)

m.c389 = Constraint(expr=   m.x193 - 0.00785398163397448*m.b556 - 0.0122718463030851*m.b557 - 0.0176714586764426*m.b558
                          - 0.0314159265358979*m.b559 - 0.0490873852123405*m.b560 - 0.0706858347057703*m.b561
                          - 0.0962112750161874*m.b562 - 0.125663706143592*m.b563 - 0.159043128087983*m.b564
                          - 0.196349540849362*m.b565 - 0.282743338823081*m.b566 - 0.38484510006475*m.b567
                          - 0.502654824574367*m.b568 == 0)

m.c390 = Constraint(expr=   m.x194 - 0.00785398163397448*m.b569 - 0.0122718463030851*m.b570 - 0.0176714586764426*m.b571
                          - 0.0314159265358979*m.b572 - 0.0490873852123405*m.b573 - 0.0706858347057703*m.b574
                          - 0.0962112750161874*m.b575 - 0.125663706143592*m.b576 - 0.159043128087983*m.b577
                          - 0.196349540849362*m.b578 - 0.282743338823081*m.b579 - 0.38484510006475*m.b580
                          - 0.502654824574367*m.b581 == 0)

m.c391 = Constraint(expr=   m.x195 - 0.00785398163397448*m.b582 - 0.0122718463030851*m.b583 - 0.0176714586764426*m.b584
                          - 0.0314159265358979*m.b585 - 0.0490873852123405*m.b586 - 0.0706858347057703*m.b587
                          - 0.0962112750161874*m.b588 - 0.125663706143592*m.b589 - 0.159043128087983*m.b590
                          - 0.196349540849362*m.b591 - 0.282743338823081*m.b592 - 0.38484510006475*m.b593
                          - 0.502654824574367*m.b594 == 0)

m.c392 = Constraint(expr=   m.x196 - 0.00785398163397448*m.b595 - 0.0122718463030851*m.b596 - 0.0176714586764426*m.b597
                          - 0.0314159265358979*m.b598 - 0.0490873852123405*m.b599 - 0.0706858347057703*m.b600
                          - 0.0962112750161874*m.b601 - 0.125663706143592*m.b602 - 0.159043128087983*m.b603
                          - 0.196349540849362*m.b604 - 0.282743338823081*m.b605 - 0.38484510006475*m.b606
                          - 0.502654824574367*m.b607 == 0)

m.c393 = Constraint(expr=   m.x197 - 0.00785398163397448*m.b608 - 0.0122718463030851*m.b609 - 0.0176714586764426*m.b610
                          - 0.0314159265358979*m.b611 - 0.0490873852123405*m.b612 - 0.0706858347057703*m.b613
                          - 0.0962112750161874*m.b614 - 0.125663706143592*m.b615 - 0.159043128087983*m.b616
                          - 0.196349540849362*m.b617 - 0.282743338823081*m.b618 - 0.38484510006475*m.b619
                          - 0.502654824574367*m.b620 == 0)

m.c394 = Constraint(expr=   m.x198 - 0.00785398163397448*m.b621 - 0.0122718463030851*m.b622 - 0.0176714586764426*m.b623
                          - 0.0314159265358979*m.b624 - 0.0490873852123405*m.b625 - 0.0706858347057703*m.b626
                          - 0.0962112750161874*m.b627 - 0.125663706143592*m.b628 - 0.159043128087983*m.b629
                          - 0.196349540849362*m.b630 - 0.282743338823081*m.b631 - 0.38484510006475*m.b632
                          - 0.502654824574367*m.b633 == 0)

m.c395 = Constraint(expr=   m.x199 - 0.00785398163397448*m.b634 - 0.0122718463030851*m.b635 - 0.0176714586764426*m.b636
                          - 0.0314159265358979*m.b637 - 0.0490873852123405*m.b638 - 0.0706858347057703*m.b639
                          - 0.0962112750161874*m.b640 - 0.125663706143592*m.b641 - 0.159043128087983*m.b642
                          - 0.196349540849362*m.b643 - 0.282743338823081*m.b644 - 0.38484510006475*m.b645
                          - 0.502654824574367*m.b646 == 0)

m.c396 = Constraint(expr=   m.x200 - 0.00785398163397448*m.b647 - 0.0122718463030851*m.b648 - 0.0176714586764426*m.b649
                          - 0.0314159265358979*m.b650 - 0.0490873852123405*m.b651 - 0.0706858347057703*m.b652
                          - 0.0962112750161874*m.b653 - 0.125663706143592*m.b654 - 0.159043128087983*m.b655
                          - 0.196349540849362*m.b656 - 0.282743338823081*m.b657 - 0.38484510006475*m.b658
                          - 0.502654824574367*m.b659 == 0)

m.c397 = Constraint(expr=   m.x201 - 0.00785398163397448*m.b660 - 0.0122718463030851*m.b661 - 0.0176714586764426*m.b662
                          - 0.0314159265358979*m.b663 - 0.0490873852123405*m.b664 - 0.0706858347057703*m.b665
                          - 0.0962112750161874*m.b666 - 0.125663706143592*m.b667 - 0.159043128087983*m.b668
                          - 0.196349540849362*m.b669 - 0.282743338823081*m.b670 - 0.38484510006475*m.b671
                          - 0.502654824574367*m.b672 == 0)

m.c398 = Constraint(expr=   m.x202 - 0.00785398163397448*m.b673 - 0.0122718463030851*m.b674 - 0.0176714586764426*m.b675
                          - 0.0314159265358979*m.b676 - 0.0490873852123405*m.b677 - 0.0706858347057703*m.b678
                          - 0.0962112750161874*m.b679 - 0.125663706143592*m.b680 - 0.159043128087983*m.b681
                          - 0.196349540849362*m.b682 - 0.282743338823081*m.b683 - 0.38484510006475*m.b684
                          - 0.502654824574367*m.b685 == 0)

m.c399 = Constraint(expr=   m.x203 - 0.00785398163397448*m.b686 - 0.0122718463030851*m.b687 - 0.0176714586764426*m.b688
                          - 0.0314159265358979*m.b689 - 0.0490873852123405*m.b690 - 0.0706858347057703*m.b691
                          - 0.0962112750161874*m.b692 - 0.125663706143592*m.b693 - 0.159043128087983*m.b694
                          - 0.196349540849362*m.b695 - 0.282743338823081*m.b696 - 0.38484510006475*m.b697
                          - 0.502654824574367*m.b698 == 0)

m.c400 = Constraint(expr=   m.x204 - 0.00785398163397448*m.b699 - 0.0122718463030851*m.b700 - 0.0176714586764426*m.b701
                          - 0.0314159265358979*m.b702 - 0.0490873852123405*m.b703 - 0.0706858347057703*m.b704
                          - 0.0962112750161874*m.b705 - 0.125663706143592*m.b706 - 0.159043128087983*m.b707
                          - 0.196349540849362*m.b708 - 0.282743338823081*m.b709 - 0.38484510006475*m.b710
                          - 0.502654824574367*m.b711 == 0)

m.c401 = Constraint(expr=   m.x205 - 0.00785398163397448*m.b712 - 0.0122718463030851*m.b713 - 0.0176714586764426*m.b714
                          - 0.0314159265358979*m.b715 - 0.0490873852123405*m.b716 - 0.0706858347057703*m.b717
                          - 0.0962112750161874*m.b718 - 0.125663706143592*m.b719 - 0.159043128087983*m.b720
                          - 0.196349540849362*m.b721 - 0.282743338823081*m.b722 - 0.38484510006475*m.b723
                          - 0.502654824574367*m.b724 == 0)

m.c402 = Constraint(expr=   m.x206 - 0.00785398163397448*m.b725 - 0.0122718463030851*m.b726 - 0.0176714586764426*m.b727
                          - 0.0314159265358979*m.b728 - 0.0490873852123405*m.b729 - 0.0706858347057703*m.b730
                          - 0.0962112750161874*m.b731 - 0.125663706143592*m.b732 - 0.159043128087983*m.b733
                          - 0.196349540849362*m.b734 - 0.282743338823081*m.b735 - 0.38484510006475*m.b736
                          - 0.502654824574367*m.b737 == 0)

m.c403 = Constraint(expr=   m.x207 - 0.00785398163397448*m.b738 - 0.0122718463030851*m.b739 - 0.0176714586764426*m.b740
                          - 0.0314159265358979*m.b741 - 0.0490873852123405*m.b742 - 0.0706858347057703*m.b743
                          - 0.0962112750161874*m.b744 - 0.125663706143592*m.b745 - 0.159043128087983*m.b746
                          - 0.196349540849362*m.b747 - 0.282743338823081*m.b748 - 0.38484510006475*m.b749
                          - 0.502654824574367*m.b750 == 0)

m.c404 = Constraint(expr=   m.x208 - 0.00785398163397448*m.b751 - 0.0122718463030851*m.b752 - 0.0176714586764426*m.b753
                          - 0.0314159265358979*m.b754 - 0.0490873852123405*m.b755 - 0.0706858347057703*m.b756
                          - 0.0962112750161874*m.b757 - 0.125663706143592*m.b758 - 0.159043128087983*m.b759
                          - 0.196349540849362*m.b760 - 0.282743338823081*m.b761 - 0.38484510006475*m.b762
                          - 0.502654824574367*m.b763 == 0)

m.c405 = Constraint(expr=   m.x209 - 0.00785398163397448*m.b764 - 0.0122718463030851*m.b765 - 0.0176714586764426*m.b766
                          - 0.0314159265358979*m.b767 - 0.0490873852123405*m.b768 - 0.0706858347057703*m.b769
                          - 0.0962112750161874*m.b770 - 0.125663706143592*m.b771 - 0.159043128087983*m.b772
                          - 0.196349540849362*m.b773 - 0.282743338823081*m.b774 - 0.38484510006475*m.b775
                          - 0.502654824574367*m.b776 == 0)

m.c406 = Constraint(expr=   m.x210 - 0.00785398163397448*m.b777 - 0.0122718463030851*m.b778 - 0.0176714586764426*m.b779
                          - 0.0314159265358979*m.b780 - 0.0490873852123405*m.b781 - 0.0706858347057703*m.b782
                          - 0.0962112750161874*m.b783 - 0.125663706143592*m.b784 - 0.159043128087983*m.b785
                          - 0.196349540849362*m.b786 - 0.282743338823081*m.b787 - 0.38484510006475*m.b788
                          - 0.502654824574367*m.b789 == 0)

m.c407 = Constraint(expr=   m.x211 - 0.00785398163397448*m.b790 - 0.0122718463030851*m.b791 - 0.0176714586764426*m.b792
                          - 0.0314159265358979*m.b793 - 0.0490873852123405*m.b794 - 0.0706858347057703*m.b795
                          - 0.0962112750161874*m.b796 - 0.125663706143592*m.b797 - 0.159043128087983*m.b798
                          - 0.196349540849362*m.b799 - 0.282743338823081*m.b800 - 0.38484510006475*m.b801
                          - 0.502654824574367*m.b802 == 0)

m.c408 = Constraint(expr=   m.x212 - 0.00785398163397448*m.b803 - 0.0122718463030851*m.b804 - 0.0176714586764426*m.b805
                          - 0.0314159265358979*m.b806 - 0.0490873852123405*m.b807 - 0.0706858347057703*m.b808
                          - 0.0962112750161874*m.b809 - 0.125663706143592*m.b810 - 0.159043128087983*m.b811
                          - 0.196349540849362*m.b812 - 0.282743338823081*m.b813 - 0.38484510006475*m.b814
                          - 0.502654824574367*m.b815 == 0)

m.c409 = Constraint(expr=   m.x213 - 0.00785398163397448*m.b816 - 0.0122718463030851*m.b817 - 0.0176714586764426*m.b818
                          - 0.0314159265358979*m.b819 - 0.0490873852123405*m.b820 - 0.0706858347057703*m.b821
                          - 0.0962112750161874*m.b822 - 0.125663706143592*m.b823 - 0.159043128087983*m.b824
                          - 0.196349540849362*m.b825 - 0.282743338823081*m.b826 - 0.38484510006475*m.b827
                          - 0.502654824574367*m.b828 == 0)

m.c410 = Constraint(expr=   m.x214 - 0.00785398163397448*m.b829 - 0.0122718463030851*m.b830 - 0.0176714586764426*m.b831
                          - 0.0314159265358979*m.b832 - 0.0490873852123405*m.b833 - 0.0706858347057703*m.b834
                          - 0.0962112750161874*m.b835 - 0.125663706143592*m.b836 - 0.159043128087983*m.b837
                          - 0.196349540849362*m.b838 - 0.282743338823081*m.b839 - 0.38484510006475*m.b840
                          - 0.502654824574367*m.b841 == 0)

m.c411 = Constraint(expr=   m.x215 - 0.00785398163397448*m.b842 - 0.0122718463030851*m.b843 - 0.0176714586764426*m.b844
                          - 0.0314159265358979*m.b845 - 0.0490873852123405*m.b846 - 0.0706858347057703*m.b847
                          - 0.0962112750161874*m.b848 - 0.125663706143592*m.b849 - 0.159043128087983*m.b850
                          - 0.196349540849362*m.b851 - 0.282743338823081*m.b852 - 0.38484510006475*m.b853
                          - 0.502654824574367*m.b854 == 0)

m.c412 = Constraint(expr=   m.x216 - 0.00785398163397448*m.b855 - 0.0122718463030851*m.b856 - 0.0176714586764426*m.b857
                          - 0.0314159265358979*m.b858 - 0.0490873852123405*m.b859 - 0.0706858347057703*m.b860
                          - 0.0962112750161874*m.b861 - 0.125663706143592*m.b862 - 0.159043128087983*m.b863
                          - 0.196349540849362*m.b864 - 0.282743338823081*m.b865 - 0.38484510006475*m.b866
                          - 0.502654824574367*m.b867 == 0)

m.c413 = Constraint(expr=   m.x217 - 0.00785398163397448*m.b868 - 0.0122718463030851*m.b869 - 0.0176714586764426*m.b870
                          - 0.0314159265358979*m.b871 - 0.0490873852123405*m.b872 - 0.0706858347057703*m.b873
                          - 0.0962112750161874*m.b874 - 0.125663706143592*m.b875 - 0.159043128087983*m.b876
                          - 0.196349540849362*m.b877 - 0.282743338823081*m.b878 - 0.38484510006475*m.b879
                          - 0.502654824574367*m.b880 == 0)

m.c414 = Constraint(expr=   m.x218 - 0.00785398163397448*m.b881 - 0.0122718463030851*m.b882 - 0.0176714586764426*m.b883
                          - 0.0314159265358979*m.b884 - 0.0490873852123405*m.b885 - 0.0706858347057703*m.b886
                          - 0.0962112750161874*m.b887 - 0.125663706143592*m.b888 - 0.159043128087983*m.b889
                          - 0.196349540849362*m.b890 - 0.282743338823081*m.b891 - 0.38484510006475*m.b892
                          - 0.502654824574367*m.b893 == 0)

m.c415 = Constraint(expr=   m.x219 - 0.00785398163397448*m.b894 - 0.0122718463030851*m.b895 - 0.0176714586764426*m.b896
                          - 0.0314159265358979*m.b897 - 0.0490873852123405*m.b898 - 0.0706858347057703*m.b899
                          - 0.0962112750161874*m.b900 - 0.125663706143592*m.b901 - 0.159043128087983*m.b902
                          - 0.196349540849362*m.b903 - 0.282743338823081*m.b904 - 0.38484510006475*m.b905
                          - 0.502654824574367*m.b906 == 0)

m.c416 = Constraint(expr=   m.x220 - 0.00785398163397448*m.b907 - 0.0122718463030851*m.b908 - 0.0176714586764426*m.b909
                          - 0.0314159265358979*m.b910 - 0.0490873852123405*m.b911 - 0.0706858347057703*m.b912
                          - 0.0962112750161874*m.b913 - 0.125663706143592*m.b914 - 0.159043128087983*m.b915
                          - 0.196349540849362*m.b916 - 0.282743338823081*m.b917 - 0.38484510006475*m.b918
                          - 0.502654824574367*m.b919 == 0)

m.c417 = Constraint(expr=   m.x221 - 0.00785398163397448*m.b920 - 0.0122718463030851*m.b921 - 0.0176714586764426*m.b922
                          - 0.0314159265358979*m.b923 - 0.0490873852123405*m.b924 - 0.0706858347057703*m.b925
                          - 0.0962112750161874*m.b926 - 0.125663706143592*m.b927 - 0.159043128087983*m.b928
                          - 0.196349540849362*m.b929 - 0.282743338823081*m.b930 - 0.38484510006475*m.b931
                          - 0.502654824574367*m.b932 == 0)

m.c418 = Constraint(expr=   m.x222 - 0.00785398163397448*m.b933 - 0.0122718463030851*m.b934 - 0.0176714586764426*m.b935
                          - 0.0314159265358979*m.b936 - 0.0490873852123405*m.b937 - 0.0706858347057703*m.b938
                          - 0.0962112750161874*m.b939 - 0.125663706143592*m.b940 - 0.159043128087983*m.b941
                          - 0.196349540849362*m.b942 - 0.282743338823081*m.b943 - 0.38484510006475*m.b944
                          - 0.502654824574367*m.b945 == 0)

m.c419 = Constraint(expr=   m.x223 - 0.00785398163397448*m.b946 - 0.0122718463030851*m.b947 - 0.0176714586764426*m.b948
                          - 0.0314159265358979*m.b949 - 0.0490873852123405*m.b950 - 0.0706858347057703*m.b951
                          - 0.0962112750161874*m.b952 - 0.125663706143592*m.b953 - 0.159043128087983*m.b954
                          - 0.196349540849362*m.b955 - 0.282743338823081*m.b956 - 0.38484510006475*m.b957
                          - 0.502654824574367*m.b958 == 0)

m.c420 = Constraint(expr=   m.x224 - 0.00785398163397448*m.b959 - 0.0122718463030851*m.b960 - 0.0176714586764426*m.b961
                          - 0.0314159265358979*m.b962 - 0.0490873852123405*m.b963 - 0.0706858347057703*m.b964
                          - 0.0962112750161874*m.b965 - 0.125663706143592*m.b966 - 0.159043128087983*m.b967
                          - 0.196349540849362*m.b968 - 0.282743338823081*m.b969 - 0.38484510006475*m.b970
                          - 0.502654824574367*m.b971 == 0)

m.c421 = Constraint(expr=   m.x225 - 0.00785398163397448*m.b972 - 0.0122718463030851*m.b973 - 0.0176714586764426*m.b974
                          - 0.0314159265358979*m.b975 - 0.0490873852123405*m.b976 - 0.0706858347057703*m.b977
                          - 0.0962112750161874*m.b978 - 0.125663706143592*m.b979 - 0.159043128087983*m.b980
                          - 0.196349540849362*m.b981 - 0.282743338823081*m.b982 - 0.38484510006475*m.b983
                          - 0.502654824574367*m.b984 == 0)

m.c422 = Constraint(expr=   m.x226 - 0.00785398163397448*m.b985 - 0.0122718463030851*m.b986 - 0.0176714586764426*m.b987
                          - 0.0314159265358979*m.b988 - 0.0490873852123405*m.b989 - 0.0706858347057703*m.b990
                          - 0.0962112750161874*m.b991 - 0.125663706143592*m.b992 - 0.159043128087983*m.b993
                          - 0.196349540849362*m.b994 - 0.282743338823081*m.b995 - 0.38484510006475*m.b996
                          - 0.502654824574367*m.b997 == 0)

m.c423 = Constraint(expr=   m.x227 - 0.00785398163397448*m.b998 - 0.0122718463030851*m.b999 - 0.0176714586764426*m.b1000
                          - 0.0314159265358979*m.b1001 - 0.0490873852123405*m.b1002 - 0.0706858347057703*m.b1003
                          - 0.0962112750161874*m.b1004 - 0.125663706143592*m.b1005 - 0.159043128087983*m.b1006
                          - 0.196349540849362*m.b1007 - 0.282743338823081*m.b1008 - 0.38484510006475*m.b1009
                          - 0.502654824574367*m.b1010 == 0)

m.c424 = Constraint(expr=   m.x228 - 0.00785398163397448*m.b1011 - 0.0122718463030851*m.b1012
                          - 0.0176714586764426*m.b1013 - 0.0314159265358979*m.b1014 - 0.0490873852123405*m.b1015
                          - 0.0706858347057703*m.b1016 - 0.0962112750161874*m.b1017 - 0.125663706143592*m.b1018
                          - 0.159043128087983*m.b1019 - 0.196349540849362*m.b1020 - 0.282743338823081*m.b1021
                          - 0.38484510006475*m.b1022 - 0.502654824574367*m.b1023 == 0)

m.c425 = Constraint(expr=   m.x229 - 0.00785398163397448*m.b1024 - 0.0122718463030851*m.b1025
                          - 0.0176714586764426*m.b1026 - 0.0314159265358979*m.b1027 - 0.0490873852123405*m.b1028
                          - 0.0706858347057703*m.b1029 - 0.0962112750161874*m.b1030 - 0.125663706143592*m.b1031
                          - 0.159043128087983*m.b1032 - 0.196349540849362*m.b1033 - 0.282743338823081*m.b1034
                          - 0.38484510006475*m.b1035 - 0.502654824574367*m.b1036 == 0)

m.c426 = Constraint(expr=   m.x230 - 0.00785398163397448*m.b1037 - 0.0122718463030851*m.b1038
                          - 0.0176714586764426*m.b1039 - 0.0314159265358979*m.b1040 - 0.0490873852123405*m.b1041
                          - 0.0706858347057703*m.b1042 - 0.0962112750161874*m.b1043 - 0.125663706143592*m.b1044
                          - 0.159043128087983*m.b1045 - 0.196349540849362*m.b1046 - 0.282743338823081*m.b1047
                          - 0.38484510006475*m.b1048 - 0.502654824574367*m.b1049 == 0)

m.c427 = Constraint(expr=   m.x231 - 0.00785398163397448*m.b1050 - 0.0122718463030851*m.b1051
                          - 0.0176714586764426*m.b1052 - 0.0314159265358979*m.b1053 - 0.0490873852123405*m.b1054
                          - 0.0706858347057703*m.b1055 - 0.0962112750161874*m.b1056 - 0.125663706143592*m.b1057
                          - 0.159043128087983*m.b1058 - 0.196349540849362*m.b1059 - 0.282743338823081*m.b1060
                          - 0.38484510006475*m.b1061 - 0.502654824574367*m.b1062 == 0)

m.c428 = Constraint(expr=   m.x232 - 0.00785398163397448*m.b1063 - 0.0122718463030851*m.b1064
                          - 0.0176714586764426*m.b1065 - 0.0314159265358979*m.b1066 - 0.0490873852123405*m.b1067
                          - 0.0706858347057703*m.b1068 - 0.0962112750161874*m.b1069 - 0.125663706143592*m.b1070
                          - 0.159043128087983*m.b1071 - 0.196349540849362*m.b1072 - 0.282743338823081*m.b1073
                          - 0.38484510006475*m.b1074 - 0.502654824574367*m.b1075 == 0)

m.c429 = Constraint(expr=   m.x233 - 0.00785398163397448*m.b1076 - 0.0122718463030851*m.b1077
                          - 0.0176714586764426*m.b1078 - 0.0314159265358979*m.b1079 - 0.0490873852123405*m.b1080
                          - 0.0706858347057703*m.b1081 - 0.0962112750161874*m.b1082 - 0.125663706143592*m.b1083
                          - 0.159043128087983*m.b1084 - 0.196349540849362*m.b1085 - 0.282743338823081*m.b1086
                          - 0.38484510006475*m.b1087 - 0.502654824574367*m.b1088 == 0)

m.c430 = Constraint(expr=   m.x234 - 0.00785398163397448*m.b1089 - 0.0122718463030851*m.b1090
                          - 0.0176714586764426*m.b1091 - 0.0314159265358979*m.b1092 - 0.0490873852123405*m.b1093
                          - 0.0706858347057703*m.b1094 - 0.0962112750161874*m.b1095 - 0.125663706143592*m.b1096
                          - 0.159043128087983*m.b1097 - 0.196349540849362*m.b1098 - 0.282743338823081*m.b1099
                          - 0.38484510006475*m.b1100 - 0.502654824574367*m.b1101 == 0)

m.c431 = Constraint(expr=   m.x235 - 0.00785398163397448*m.b1102 - 0.0122718463030851*m.b1103
                          - 0.0176714586764426*m.b1104 - 0.0314159265358979*m.b1105 - 0.0490873852123405*m.b1106
                          - 0.0706858347057703*m.b1107 - 0.0962112750161874*m.b1108 - 0.125663706143592*m.b1109
                          - 0.159043128087983*m.b1110 - 0.196349540849362*m.b1111 - 0.282743338823081*m.b1112
                          - 0.38484510006475*m.b1113 - 0.502654824574367*m.b1114 == 0)

m.c432 = Constraint(expr=   m.x236 - 0.00785398163397448*m.b1115 - 0.0122718463030851*m.b1116
                          - 0.0176714586764426*m.b1117 - 0.0314159265358979*m.b1118 - 0.0490873852123405*m.b1119
                          - 0.0706858347057703*m.b1120 - 0.0962112750161874*m.b1121 - 0.125663706143592*m.b1122
                          - 0.159043128087983*m.b1123 - 0.196349540849362*m.b1124 - 0.282743338823081*m.b1125
                          - 0.38484510006475*m.b1126 - 0.502654824574367*m.b1127 == 0)

m.c433 = Constraint(expr=   m.x237 - 0.00785398163397448*m.b1128 - 0.0122718463030851*m.b1129
                          - 0.0176714586764426*m.b1130 - 0.0314159265358979*m.b1131 - 0.0490873852123405*m.b1132
                          - 0.0706858347057703*m.b1133 - 0.0962112750161874*m.b1134 - 0.125663706143592*m.b1135
                          - 0.159043128087983*m.b1136 - 0.196349540849362*m.b1137 - 0.282743338823081*m.b1138
                          - 0.38484510006475*m.b1139 - 0.502654824574367*m.b1140 == 0)

m.c434 = Constraint(expr=   m.x238 - 0.00785398163397448*m.b1141 - 0.0122718463030851*m.b1142
                          - 0.0176714586764426*m.b1143 - 0.0314159265358979*m.b1144 - 0.0490873852123405*m.b1145
                          - 0.0706858347057703*m.b1146 - 0.0962112750161874*m.b1147 - 0.125663706143592*m.b1148
                          - 0.159043128087983*m.b1149 - 0.196349540849362*m.b1150 - 0.282743338823081*m.b1151
                          - 0.38484510006475*m.b1152 - 0.502654824574367*m.b1153 == 0)

m.c435 = Constraint(expr=   m.x239 - 0.00785398163397448*m.b1154 - 0.0122718463030851*m.b1155
                          - 0.0176714586764426*m.b1156 - 0.0314159265358979*m.b1157 - 0.0490873852123405*m.b1158
                          - 0.0706858347057703*m.b1159 - 0.0962112750161874*m.b1160 - 0.125663706143592*m.b1161
                          - 0.159043128087983*m.b1162 - 0.196349540849362*m.b1163 - 0.282743338823081*m.b1164
                          - 0.38484510006475*m.b1165 - 0.502654824574367*m.b1166 == 0)

m.c436 = Constraint(expr=   m.x240 - 0.00785398163397448*m.b1167 - 0.0122718463030851*m.b1168
                          - 0.0176714586764426*m.b1169 - 0.0314159265358979*m.b1170 - 0.0490873852123405*m.b1171
                          - 0.0706858347057703*m.b1172 - 0.0962112750161874*m.b1173 - 0.125663706143592*m.b1174
                          - 0.159043128087983*m.b1175 - 0.196349540849362*m.b1176 - 0.282743338823081*m.b1177
                          - 0.38484510006475*m.b1178 - 0.502654824574367*m.b1179 == 0)

m.c437 = Constraint(expr=   m.x241 - 0.00785398163397448*m.b1180 - 0.0122718463030851*m.b1181
                          - 0.0176714586764426*m.b1182 - 0.0314159265358979*m.b1183 - 0.0490873852123405*m.b1184
                          - 0.0706858347057703*m.b1185 - 0.0962112750161874*m.b1186 - 0.125663706143592*m.b1187
                          - 0.159043128087983*m.b1188 - 0.196349540849362*m.b1189 - 0.282743338823081*m.b1190
                          - 0.38484510006475*m.b1191 - 0.502654824574367*m.b1192 == 0)

m.c438 = Constraint(expr=   m.x242 - 0.00785398163397448*m.b1193 - 0.0122718463030851*m.b1194
                          - 0.0176714586764426*m.b1195 - 0.0314159265358979*m.b1196 - 0.0490873852123405*m.b1197
                          - 0.0706858347057703*m.b1198 - 0.0962112750161874*m.b1199 - 0.125663706143592*m.b1200
                          - 0.159043128087983*m.b1201 - 0.196349540849362*m.b1202 - 0.282743338823081*m.b1203
                          - 0.38484510006475*m.b1204 - 0.502654824574367*m.b1205 == 0)

m.c439 = Constraint(expr=   m.x243 - 0.00785398163397448*m.b1206 - 0.0122718463030851*m.b1207
                          - 0.0176714586764426*m.b1208 - 0.0314159265358979*m.b1209 - 0.0490873852123405*m.b1210
                          - 0.0706858347057703*m.b1211 - 0.0962112750161874*m.b1212 - 0.125663706143592*m.b1213
                          - 0.159043128087983*m.b1214 - 0.196349540849362*m.b1215 - 0.282743338823081*m.b1216
                          - 0.38484510006475*m.b1217 - 0.502654824574367*m.b1218 == 0)

m.c440 = Constraint(expr=   m.x244 - 0.00785398163397448*m.b1219 - 0.0122718463030851*m.b1220
                          - 0.0176714586764426*m.b1221 - 0.0314159265358979*m.b1222 - 0.0490873852123405*m.b1223
                          - 0.0706858347057703*m.b1224 - 0.0962112750161874*m.b1225 - 0.125663706143592*m.b1226
                          - 0.159043128087983*m.b1227 - 0.196349540849362*m.b1228 - 0.282743338823081*m.b1229
                          - 0.38484510006475*m.b1230 - 0.502654824574367*m.b1231 == 0)

m.c441 = Constraint(expr=   m.x245 - 0.00785398163397448*m.b1232 - 0.0122718463030851*m.b1233
                          - 0.0176714586764426*m.b1234 - 0.0314159265358979*m.b1235 - 0.0490873852123405*m.b1236
                          - 0.0706858347057703*m.b1237 - 0.0962112750161874*m.b1238 - 0.125663706143592*m.b1239
                          - 0.159043128087983*m.b1240 - 0.196349540849362*m.b1241 - 0.282743338823081*m.b1242
                          - 0.38484510006475*m.b1243 - 0.502654824574367*m.b1244 == 0)

m.c442 = Constraint(expr=   m.x246 - 0.00785398163397448*m.b1245 - 0.0122718463030851*m.b1246
                          - 0.0176714586764426*m.b1247 - 0.0314159265358979*m.b1248 - 0.0490873852123405*m.b1249
                          - 0.0706858347057703*m.b1250 - 0.0962112750161874*m.b1251 - 0.125663706143592*m.b1252
                          - 0.159043128087983*m.b1253 - 0.196349540849362*m.b1254 - 0.282743338823081*m.b1255
                          - 0.38484510006475*m.b1256 - 0.502654824574367*m.b1257 == 0)

m.c443 = Constraint(expr=   m.x247 - 0.00785398163397448*m.b1258 - 0.0122718463030851*m.b1259
                          - 0.0176714586764426*m.b1260 - 0.0314159265358979*m.b1261 - 0.0490873852123405*m.b1262
                          - 0.0706858347057703*m.b1263 - 0.0962112750161874*m.b1264 - 0.125663706143592*m.b1265
                          - 0.159043128087983*m.b1266 - 0.196349540849362*m.b1267 - 0.282743338823081*m.b1268
                          - 0.38484510006475*m.b1269 - 0.502654824574367*m.b1270 == 0)

m.c444 = Constraint(expr=   m.x248 - 0.00785398163397448*m.b1271 - 0.0122718463030851*m.b1272
                          - 0.0176714586764426*m.b1273 - 0.0314159265358979*m.b1274 - 0.0490873852123405*m.b1275
                          - 0.0706858347057703*m.b1276 - 0.0962112750161874*m.b1277 - 0.125663706143592*m.b1278
                          - 0.159043128087983*m.b1279 - 0.196349540849362*m.b1280 - 0.282743338823081*m.b1281
                          - 0.38484510006475*m.b1282 - 0.502654824574367*m.b1283 == 0)

m.c445 = Constraint(expr=   m.x249 - 0.00785398163397448*m.b1284 - 0.0122718463030851*m.b1285
                          - 0.0176714586764426*m.b1286 - 0.0314159265358979*m.b1287 - 0.0490873852123405*m.b1288
                          - 0.0706858347057703*m.b1289 - 0.0962112750161874*m.b1290 - 0.125663706143592*m.b1291
                          - 0.159043128087983*m.b1292 - 0.196349540849362*m.b1293 - 0.282743338823081*m.b1294
                          - 0.38484510006475*m.b1295 - 0.502654824574367*m.b1296 == 0)

m.c446 = Constraint(expr=   m.x250 - 0.00785398163397448*m.b1297 - 0.0122718463030851*m.b1298
                          - 0.0176714586764426*m.b1299 - 0.0314159265358979*m.b1300 - 0.0490873852123405*m.b1301
                          - 0.0706858347057703*m.b1302 - 0.0962112750161874*m.b1303 - 0.125663706143592*m.b1304
                          - 0.159043128087983*m.b1305 - 0.196349540849362*m.b1306 - 0.282743338823081*m.b1307
                          - 0.38484510006475*m.b1308 - 0.502654824574367*m.b1309 == 0)

m.c447 = Constraint(expr=   m.x251 - 0.00785398163397448*m.b1310 - 0.0122718463030851*m.b1311
                          - 0.0176714586764426*m.b1312 - 0.0314159265358979*m.b1313 - 0.0490873852123405*m.b1314
                          - 0.0706858347057703*m.b1315 - 0.0962112750161874*m.b1316 - 0.125663706143592*m.b1317
                          - 0.159043128087983*m.b1318 - 0.196349540849362*m.b1319 - 0.282743338823081*m.b1320
                          - 0.38484510006475*m.b1321 - 0.502654824574367*m.b1322 == 0)

m.c448 = Constraint(expr=   m.x252 - 0.00785398163397448*m.b1323 - 0.0122718463030851*m.b1324
                          - 0.0176714586764426*m.b1325 - 0.0314159265358979*m.b1326 - 0.0490873852123405*m.b1327
                          - 0.0706858347057703*m.b1328 - 0.0962112750161874*m.b1329 - 0.125663706143592*m.b1330
                          - 0.159043128087983*m.b1331 - 0.196349540849362*m.b1332 - 0.282743338823081*m.b1333
                          - 0.38484510006475*m.b1334 - 0.502654824574367*m.b1335 == 0)

m.c449 = Constraint(expr=   m.x253 - 0.00785398163397448*m.b1336 - 0.0122718463030851*m.b1337
                          - 0.0176714586764426*m.b1338 - 0.0314159265358979*m.b1339 - 0.0490873852123405*m.b1340
                          - 0.0706858347057703*m.b1341 - 0.0962112750161874*m.b1342 - 0.125663706143592*m.b1343
                          - 0.159043128087983*m.b1344 - 0.196349540849362*m.b1345 - 0.282743338823081*m.b1346
                          - 0.38484510006475*m.b1347 - 0.502654824574367*m.b1348 == 0)

m.c450 = Constraint(expr=   m.x254 - 0.00785398163397448*m.b1349 - 0.0122718463030851*m.b1350
                          - 0.0176714586764426*m.b1351 - 0.0314159265358979*m.b1352 - 0.0490873852123405*m.b1353
                          - 0.0706858347057703*m.b1354 - 0.0962112750161874*m.b1355 - 0.125663706143592*m.b1356
                          - 0.159043128087983*m.b1357 - 0.196349540849362*m.b1358 - 0.282743338823081*m.b1359
                          - 0.38484510006475*m.b1360 - 0.502654824574367*m.b1361 == 0)

m.c451 = Constraint(expr=   m.x255 - 0.00785398163397448*m.b1362 - 0.0122718463030851*m.b1363
                          - 0.0176714586764426*m.b1364 - 0.0314159265358979*m.b1365 - 0.0490873852123405*m.b1366
                          - 0.0706858347057703*m.b1367 - 0.0962112750161874*m.b1368 - 0.125663706143592*m.b1369
                          - 0.159043128087983*m.b1370 - 0.196349540849362*m.b1371 - 0.282743338823081*m.b1372
                          - 0.38484510006475*m.b1373 - 0.502654824574367*m.b1374 == 0)

m.c452 = Constraint(expr=   m.x256 - 0.00785398163397448*m.b1375 - 0.0122718463030851*m.b1376
                          - 0.0176714586764426*m.b1377 - 0.0314159265358979*m.b1378 - 0.0490873852123405*m.b1379
                          - 0.0706858347057703*m.b1380 - 0.0962112750161874*m.b1381 - 0.125663706143592*m.b1382
                          - 0.159043128087983*m.b1383 - 0.196349540849362*m.b1384 - 0.282743338823081*m.b1385
                          - 0.38484510006475*m.b1386 - 0.502654824574367*m.b1387 == 0)

m.c453 = Constraint(expr=   m.x257 - 0.00785398163397448*m.b1388 - 0.0122718463030851*m.b1389
                          - 0.0176714586764426*m.b1390 - 0.0314159265358979*m.b1391 - 0.0490873852123405*m.b1392
                          - 0.0706858347057703*m.b1393 - 0.0962112750161874*m.b1394 - 0.125663706143592*m.b1395
                          - 0.159043128087983*m.b1396 - 0.196349540849362*m.b1397 - 0.282743338823081*m.b1398
                          - 0.38484510006475*m.b1399 - 0.502654824574367*m.b1400 == 0)

m.c454 = Constraint(expr=   m.x258 - 0.00785398163397448*m.b1401 - 0.0122718463030851*m.b1402
                          - 0.0176714586764426*m.b1403 - 0.0314159265358979*m.b1404 - 0.0490873852123405*m.b1405
                          - 0.0706858347057703*m.b1406 - 0.0962112750161874*m.b1407 - 0.125663706143592*m.b1408
                          - 0.159043128087983*m.b1409 - 0.196349540849362*m.b1410 - 0.282743338823081*m.b1411
                          - 0.38484510006475*m.b1412 - 0.502654824574367*m.b1413 == 0)

m.c455 = Constraint(expr=   m.x259 - 0.00785398163397448*m.b1414 - 0.0122718463030851*m.b1415
                          - 0.0176714586764426*m.b1416 - 0.0314159265358979*m.b1417 - 0.0490873852123405*m.b1418
                          - 0.0706858347057703*m.b1419 - 0.0962112750161874*m.b1420 - 0.125663706143592*m.b1421
                          - 0.159043128087983*m.b1422 - 0.196349540849362*m.b1423 - 0.282743338823081*m.b1424
                          - 0.38484510006475*m.b1425 - 0.502654824574367*m.b1426 == 0)

m.c456 = Constraint(expr=   m.x260 - 0.00785398163397448*m.b1427 - 0.0122718463030851*m.b1428
                          - 0.0176714586764426*m.b1429 - 0.0314159265358979*m.b1430 - 0.0490873852123405*m.b1431
                          - 0.0706858347057703*m.b1432 - 0.0962112750161874*m.b1433 - 0.125663706143592*m.b1434
                          - 0.159043128087983*m.b1435 - 0.196349540849362*m.b1436 - 0.282743338823081*m.b1437
                          - 0.38484510006475*m.b1438 - 0.502654824574367*m.b1439 == 0)

m.c457 = Constraint(expr=   m.x261 - 0.00785398163397448*m.b1440 - 0.0122718463030851*m.b1441
                          - 0.0176714586764426*m.b1442 - 0.0314159265358979*m.b1443 - 0.0490873852123405*m.b1444
                          - 0.0706858347057703*m.b1445 - 0.0962112750161874*m.b1446 - 0.125663706143592*m.b1447
                          - 0.159043128087983*m.b1448 - 0.196349540849362*m.b1449 - 0.282743338823081*m.b1450
                          - 0.38484510006475*m.b1451 - 0.502654824574367*m.b1452 == 0)

m.c458 = Constraint(expr=   m.x262 - 0.00785398163397448*m.b1453 - 0.0122718463030851*m.b1454
                          - 0.0176714586764426*m.b1455 - 0.0314159265358979*m.b1456 - 0.0490873852123405*m.b1457
                          - 0.0706858347057703*m.b1458 - 0.0962112750161874*m.b1459 - 0.125663706143592*m.b1460
                          - 0.159043128087983*m.b1461 - 0.196349540849362*m.b1462 - 0.282743338823081*m.b1463
                          - 0.38484510006475*m.b1464 - 0.502654824574367*m.b1465 == 0)

m.c459 = Constraint(expr=   m.x263 - 0.00785398163397448*m.b1466 - 0.0122718463030851*m.b1467
                          - 0.0176714586764426*m.b1468 - 0.0314159265358979*m.b1469 - 0.0490873852123405*m.b1470
                          - 0.0706858347057703*m.b1471 - 0.0962112750161874*m.b1472 - 0.125663706143592*m.b1473
                          - 0.159043128087983*m.b1474 - 0.196349540849362*m.b1475 - 0.282743338823081*m.b1476
                          - 0.38484510006475*m.b1477 - 0.502654824574367*m.b1478 == 0)

m.c460 = Constraint(expr=   m.x264 - 0.00785398163397448*m.b1479 - 0.0122718463030851*m.b1480
                          - 0.0176714586764426*m.b1481 - 0.0314159265358979*m.b1482 - 0.0490873852123405*m.b1483
                          - 0.0706858347057703*m.b1484 - 0.0962112750161874*m.b1485 - 0.125663706143592*m.b1486
                          - 0.159043128087983*m.b1487 - 0.196349540849362*m.b1488 - 0.282743338823081*m.b1489
                          - 0.38484510006475*m.b1490 - 0.502654824574367*m.b1491 == 0)

m.c461 = Constraint(expr=   m.x265 - 0.00785398163397448*m.b1492 - 0.0122718463030851*m.b1493
                          - 0.0176714586764426*m.b1494 - 0.0314159265358979*m.b1495 - 0.0490873852123405*m.b1496
                          - 0.0706858347057703*m.b1497 - 0.0962112750161874*m.b1498 - 0.125663706143592*m.b1499
                          - 0.159043128087983*m.b1500 - 0.196349540849362*m.b1501 - 0.282743338823081*m.b1502
                          - 0.38484510006475*m.b1503 - 0.502654824574367*m.b1504 == 0)

m.c462 = Constraint(expr=   m.x266 - 0.00785398163397448*m.b1505 - 0.0122718463030851*m.b1506
                          - 0.0176714586764426*m.b1507 - 0.0314159265358979*m.b1508 - 0.0490873852123405*m.b1509
                          - 0.0706858347057703*m.b1510 - 0.0962112750161874*m.b1511 - 0.125663706143592*m.b1512
                          - 0.159043128087983*m.b1513 - 0.196349540849362*m.b1514 - 0.282743338823081*m.b1515
                          - 0.38484510006475*m.b1516 - 0.502654824574367*m.b1517 == 0)

m.c463 = Constraint(expr=   m.x267 - 0.00785398163397448*m.b1518 - 0.0122718463030851*m.b1519
                          - 0.0176714586764426*m.b1520 - 0.0314159265358979*m.b1521 - 0.0490873852123405*m.b1522
                          - 0.0706858347057703*m.b1523 - 0.0962112750161874*m.b1524 - 0.125663706143592*m.b1525
                          - 0.159043128087983*m.b1526 - 0.196349540849362*m.b1527 - 0.282743338823081*m.b1528
                          - 0.38484510006475*m.b1529 - 0.502654824574367*m.b1530 == 0)

m.c464 = Constraint(expr=   m.x268 - 0.00785398163397448*m.b1531 - 0.0122718463030851*m.b1532
                          - 0.0176714586764426*m.b1533 - 0.0314159265358979*m.b1534 - 0.0490873852123405*m.b1535
                          - 0.0706858347057703*m.b1536 - 0.0962112750161874*m.b1537 - 0.125663706143592*m.b1538
                          - 0.159043128087983*m.b1539 - 0.196349540849362*m.b1540 - 0.282743338823081*m.b1541
                          - 0.38484510006475*m.b1542 - 0.502654824574367*m.b1543 == 0)

m.c465 = Constraint(expr=   m.x269 - 0.00785398163397448*m.b1544 - 0.0122718463030851*m.b1545
                          - 0.0176714586764426*m.b1546 - 0.0314159265358979*m.b1547 - 0.0490873852123405*m.b1548
                          - 0.0706858347057703*m.b1549 - 0.0962112750161874*m.b1550 - 0.125663706143592*m.b1551
                          - 0.159043128087983*m.b1552 - 0.196349540849362*m.b1553 - 0.282743338823081*m.b1554
                          - 0.38484510006475*m.b1555 - 0.502654824574367*m.b1556 == 0)

m.c466 = Constraint(expr=   m.b270 + m.b271 + m.b272 + m.b273 + m.b274 + m.b275 + m.b276 + m.b277 + m.b278 + m.b279
                          + m.b280 + m.b281 + m.b282 == 1)

m.c467 = Constraint(expr=   m.b283 + m.b284 + m.b285 + m.b286 + m.b287 + m.b288 + m.b289 + m.b290 + m.b291 + m.b292
                          + m.b293 + m.b294 + m.b295 == 1)

m.c468 = Constraint(expr=   m.b296 + m.b297 + m.b298 + m.b299 + m.b300 + m.b301 + m.b302 + m.b303 + m.b304 + m.b305
                          + m.b306 + m.b307 + m.b308 == 1)

m.c469 = Constraint(expr=   m.b309 + m.b310 + m.b311 + m.b312 + m.b313 + m.b314 + m.b315 + m.b316 + m.b317 + m.b318
                          + m.b319 + m.b320 + m.b321 == 1)

m.c470 = Constraint(expr=   m.b322 + m.b323 + m.b324 + m.b325 + m.b326 + m.b327 + m.b328 + m.b329 + m.b330 + m.b331
                          + m.b332 + m.b333 + m.b334 == 1)

m.c471 = Constraint(expr=   m.b335 + m.b336 + m.b337 + m.b338 + m.b339 + m.b340 + m.b341 + m.b342 + m.b343 + m.b344
                          + m.b345 + m.b346 + m.b347 == 1)

m.c472 = Constraint(expr=   m.b348 + m.b349 + m.b350 + m.b351 + m.b352 + m.b353 + m.b354 + m.b355 + m.b356 + m.b357
                          + m.b358 + m.b359 + m.b360 == 1)

m.c473 = Constraint(expr=   m.b361 + m.b362 + m.b363 + m.b364 + m.b365 + m.b366 + m.b367 + m.b368 + m.b369 + m.b370
                          + m.b371 + m.b372 + m.b373 == 1)

m.c474 = Constraint(expr=   m.b374 + m.b375 + m.b376 + m.b377 + m.b378 + m.b379 + m.b380 + m.b381 + m.b382 + m.b383
                          + m.b384 + m.b385 + m.b386 == 1)

m.c475 = Constraint(expr=   m.b387 + m.b388 + m.b389 + m.b390 + m.b391 + m.b392 + m.b393 + m.b394 + m.b395 + m.b396
                          + m.b397 + m.b398 + m.b399 == 1)

m.c476 = Constraint(expr=   m.b400 + m.b401 + m.b402 + m.b403 + m.b404 + m.b405 + m.b406 + m.b407 + m.b408 + m.b409
                          + m.b410 + m.b411 + m.b412 == 1)

m.c477 = Constraint(expr=   m.b413 + m.b414 + m.b415 + m.b416 + m.b417 + m.b418 + m.b419 + m.b420 + m.b421 + m.b422
                          + m.b423 + m.b424 + m.b425 == 1)

m.c478 = Constraint(expr=   m.b426 + m.b427 + m.b428 + m.b429 + m.b430 + m.b431 + m.b432 + m.b433 + m.b434 + m.b435
                          + m.b436 + m.b437 + m.b438 == 1)

m.c479 = Constraint(expr=   m.b439 + m.b440 + m.b441 + m.b442 + m.b443 + m.b444 + m.b445 + m.b446 + m.b447 + m.b448
                          + m.b449 + m.b450 + m.b451 == 1)

m.c480 = Constraint(expr=   m.b452 + m.b453 + m.b454 + m.b455 + m.b456 + m.b457 + m.b458 + m.b459 + m.b460 + m.b461
                          + m.b462 + m.b463 + m.b464 == 1)

m.c481 = Constraint(expr=   m.b465 + m.b466 + m.b467 + m.b468 + m.b469 + m.b470 + m.b471 + m.b472 + m.b473 + m.b474
                          + m.b475 + m.b476 + m.b477 == 1)

m.c482 = Constraint(expr=   m.b478 + m.b479 + m.b480 + m.b481 + m.b482 + m.b483 + m.b484 + m.b485 + m.b486 + m.b487
                          + m.b488 + m.b489 + m.b490 == 1)

m.c483 = Constraint(expr=   m.b491 + m.b492 + m.b493 + m.b494 + m.b495 + m.b496 + m.b497 + m.b498 + m.b499 + m.b500
                          + m.b501 + m.b502 + m.b503 == 1)

m.c484 = Constraint(expr=   m.b504 + m.b505 + m.b506 + m.b507 + m.b508 + m.b509 + m.b510 + m.b511 + m.b512 + m.b513
                          + m.b514 + m.b515 + m.b516 == 1)

m.c485 = Constraint(expr=   m.b517 + m.b518 + m.b519 + m.b520 + m.b521 + m.b522 + m.b523 + m.b524 + m.b525 + m.b526
                          + m.b527 + m.b528 + m.b529 == 1)

m.c486 = Constraint(expr=   m.b530 + m.b531 + m.b532 + m.b533 + m.b534 + m.b535 + m.b536 + m.b537 + m.b538 + m.b539
                          + m.b540 + m.b541 + m.b542 == 1)

m.c487 = Constraint(expr=   m.b543 + m.b544 + m.b545 + m.b546 + m.b547 + m.b548 + m.b549 + m.b550 + m.b551 + m.b552
                          + m.b553 + m.b554 + m.b555 == 1)

m.c488 = Constraint(expr=   m.b556 + m.b557 + m.b558 + m.b559 + m.b560 + m.b561 + m.b562 + m.b563 + m.b564 + m.b565
                          + m.b566 + m.b567 + m.b568 == 1)

m.c489 = Constraint(expr=   m.b569 + m.b570 + m.b571 + m.b572 + m.b573 + m.b574 + m.b575 + m.b576 + m.b577 + m.b578
                          + m.b579 + m.b580 + m.b581 == 1)

m.c490 = Constraint(expr=   m.b582 + m.b583 + m.b584 + m.b585 + m.b586 + m.b587 + m.b588 + m.b589 + m.b590 + m.b591
                          + m.b592 + m.b593 + m.b594 == 1)

m.c491 = Constraint(expr=   m.b595 + m.b596 + m.b597 + m.b598 + m.b599 + m.b600 + m.b601 + m.b602 + m.b603 + m.b604
                          + m.b605 + m.b606 + m.b607 == 1)

m.c492 = Constraint(expr=   m.b608 + m.b609 + m.b610 + m.b611 + m.b612 + m.b613 + m.b614 + m.b615 + m.b616 + m.b617
                          + m.b618 + m.b619 + m.b620 == 1)

m.c493 = Constraint(expr=   m.b621 + m.b622 + m.b623 + m.b624 + m.b625 + m.b626 + m.b627 + m.b628 + m.b629 + m.b630
                          + m.b631 + m.b632 + m.b633 == 1)

m.c494 = Constraint(expr=   m.b634 + m.b635 + m.b636 + m.b637 + m.b638 + m.b639 + m.b640 + m.b641 + m.b642 + m.b643
                          + m.b644 + m.b645 + m.b646 == 1)

m.c495 = Constraint(expr=   m.b647 + m.b648 + m.b649 + m.b650 + m.b651 + m.b652 + m.b653 + m.b654 + m.b655 + m.b656
                          + m.b657 + m.b658 + m.b659 == 1)

m.c496 = Constraint(expr=   m.b660 + m.b661 + m.b662 + m.b663 + m.b664 + m.b665 + m.b666 + m.b667 + m.b668 + m.b669
                          + m.b670 + m.b671 + m.b672 == 1)

m.c497 = Constraint(expr=   m.b673 + m.b674 + m.b675 + m.b676 + m.b677 + m.b678 + m.b679 + m.b680 + m.b681 + m.b682
                          + m.b683 + m.b684 + m.b685 == 1)

m.c498 = Constraint(expr=   m.b686 + m.b687 + m.b688 + m.b689 + m.b690 + m.b691 + m.b692 + m.b693 + m.b694 + m.b695
                          + m.b696 + m.b697 + m.b698 == 1)

m.c499 = Constraint(expr=   m.b699 + m.b700 + m.b701 + m.b702 + m.b703 + m.b704 + m.b705 + m.b706 + m.b707 + m.b708
                          + m.b709 + m.b710 + m.b711 == 1)

m.c500 = Constraint(expr=   m.b712 + m.b713 + m.b714 + m.b715 + m.b716 + m.b717 + m.b718 + m.b719 + m.b720 + m.b721
                          + m.b722 + m.b723 + m.b724 == 1)

m.c501 = Constraint(expr=   m.b725 + m.b726 + m.b727 + m.b728 + m.b729 + m.b730 + m.b731 + m.b732 + m.b733 + m.b734
                          + m.b735 + m.b736 + m.b737 == 1)

m.c502 = Constraint(expr=   m.b738 + m.b739 + m.b740 + m.b741 + m.b742 + m.b743 + m.b744 + m.b745 + m.b746 + m.b747
                          + m.b748 + m.b749 + m.b750 == 1)

m.c503 = Constraint(expr=   m.b751 + m.b752 + m.b753 + m.b754 + m.b755 + m.b756 + m.b757 + m.b758 + m.b759 + m.b760
                          + m.b761 + m.b762 + m.b763 == 1)

m.c504 = Constraint(expr=   m.b764 + m.b765 + m.b766 + m.b767 + m.b768 + m.b769 + m.b770 + m.b771 + m.b772 + m.b773
                          + m.b774 + m.b775 + m.b776 == 1)

m.c505 = Constraint(expr=   m.b777 + m.b778 + m.b779 + m.b780 + m.b781 + m.b782 + m.b783 + m.b784 + m.b785 + m.b786
                          + m.b787 + m.b788 + m.b789 == 1)

m.c506 = Constraint(expr=   m.b790 + m.b791 + m.b792 + m.b793 + m.b794 + m.b795 + m.b796 + m.b797 + m.b798 + m.b799
                          + m.b800 + m.b801 + m.b802 == 1)

m.c507 = Constraint(expr=   m.b803 + m.b804 + m.b805 + m.b806 + m.b807 + m.b808 + m.b809 + m.b810 + m.b811 + m.b812
                          + m.b813 + m.b814 + m.b815 == 1)

m.c508 = Constraint(expr=   m.b816 + m.b817 + m.b818 + m.b819 + m.b820 + m.b821 + m.b822 + m.b823 + m.b824 + m.b825
                          + m.b826 + m.b827 + m.b828 == 1)

m.c509 = Constraint(expr=   m.b829 + m.b830 + m.b831 + m.b832 + m.b833 + m.b834 + m.b835 + m.b836 + m.b837 + m.b838
                          + m.b839 + m.b840 + m.b841 == 1)

m.c510 = Constraint(expr=   m.b842 + m.b843 + m.b844 + m.b845 + m.b846 + m.b847 + m.b848 + m.b849 + m.b850 + m.b851
                          + m.b852 + m.b853 + m.b854 == 1)

m.c511 = Constraint(expr=   m.b855 + m.b856 + m.b857 + m.b858 + m.b859 + m.b860 + m.b861 + m.b862 + m.b863 + m.b864
                          + m.b865 + m.b866 + m.b867 == 1)

m.c512 = Constraint(expr=   m.b868 + m.b869 + m.b870 + m.b871 + m.b872 + m.b873 + m.b874 + m.b875 + m.b876 + m.b877
                          + m.b878 + m.b879 + m.b880 == 1)

m.c513 = Constraint(expr=   m.b881 + m.b882 + m.b883 + m.b884 + m.b885 + m.b886 + m.b887 + m.b888 + m.b889 + m.b890
                          + m.b891 + m.b892 + m.b893 == 1)

m.c514 = Constraint(expr=   m.b894 + m.b895 + m.b896 + m.b897 + m.b898 + m.b899 + m.b900 + m.b901 + m.b902 + m.b903
                          + m.b904 + m.b905 + m.b906 == 1)

m.c515 = Constraint(expr=   m.b907 + m.b908 + m.b909 + m.b910 + m.b911 + m.b912 + m.b913 + m.b914 + m.b915 + m.b916
                          + m.b917 + m.b918 + m.b919 == 1)

m.c516 = Constraint(expr=   m.b920 + m.b921 + m.b922 + m.b923 + m.b924 + m.b925 + m.b926 + m.b927 + m.b928 + m.b929
                          + m.b930 + m.b931 + m.b932 == 1)

m.c517 = Constraint(expr=   m.b933 + m.b934 + m.b935 + m.b936 + m.b937 + m.b938 + m.b939 + m.b940 + m.b941 + m.b942
                          + m.b943 + m.b944 + m.b945 == 1)

m.c518 = Constraint(expr=   m.b946 + m.b947 + m.b948 + m.b949 + m.b950 + m.b951 + m.b952 + m.b953 + m.b954 + m.b955
                          + m.b956 + m.b957 + m.b958 == 1)

m.c519 = Constraint(expr=   m.b959 + m.b960 + m.b961 + m.b962 + m.b963 + m.b964 + m.b965 + m.b966 + m.b967 + m.b968
                          + m.b969 + m.b970 + m.b971 == 1)

m.c520 = Constraint(expr=   m.b972 + m.b973 + m.b974 + m.b975 + m.b976 + m.b977 + m.b978 + m.b979 + m.b980 + m.b981
                          + m.b982 + m.b983 + m.b984 == 1)

m.c521 = Constraint(expr=   m.b985 + m.b986 + m.b987 + m.b988 + m.b989 + m.b990 + m.b991 + m.b992 + m.b993 + m.b994
                          + m.b995 + m.b996 + m.b997 == 1)

m.c522 = Constraint(expr=   m.b998 + m.b999 + m.b1000 + m.b1001 + m.b1002 + m.b1003 + m.b1004 + m.b1005 + m.b1006
                          + m.b1007 + m.b1008 + m.b1009 + m.b1010 == 1)

m.c523 = Constraint(expr=   m.b1011 + m.b1012 + m.b1013 + m.b1014 + m.b1015 + m.b1016 + m.b1017 + m.b1018 + m.b1019
                          + m.b1020 + m.b1021 + m.b1022 + m.b1023 == 1)

m.c524 = Constraint(expr=   m.b1024 + m.b1025 + m.b1026 + m.b1027 + m.b1028 + m.b1029 + m.b1030 + m.b1031 + m.b1032
                          + m.b1033 + m.b1034 + m.b1035 + m.b1036 == 1)

m.c525 = Constraint(expr=   m.b1037 + m.b1038 + m.b1039 + m.b1040 + m.b1041 + m.b1042 + m.b1043 + m.b1044 + m.b1045
                          + m.b1046 + m.b1047 + m.b1048 + m.b1049 == 1)

m.c526 = Constraint(expr=   m.b1050 + m.b1051 + m.b1052 + m.b1053 + m.b1054 + m.b1055 + m.b1056 + m.b1057 + m.b1058
                          + m.b1059 + m.b1060 + m.b1061 + m.b1062 == 1)

m.c527 = Constraint(expr=   m.b1063 + m.b1064 + m.b1065 + m.b1066 + m.b1067 + m.b1068 + m.b1069 + m.b1070 + m.b1071
                          + m.b1072 + m.b1073 + m.b1074 + m.b1075 == 1)

m.c528 = Constraint(expr=   m.b1076 + m.b1077 + m.b1078 + m.b1079 + m.b1080 + m.b1081 + m.b1082 + m.b1083 + m.b1084
                          + m.b1085 + m.b1086 + m.b1087 + m.b1088 == 1)

m.c529 = Constraint(expr=   m.b1089 + m.b1090 + m.b1091 + m.b1092 + m.b1093 + m.b1094 + m.b1095 + m.b1096 + m.b1097
                          + m.b1098 + m.b1099 + m.b1100 + m.b1101 == 1)

m.c530 = Constraint(expr=   m.b1102 + m.b1103 + m.b1104 + m.b1105 + m.b1106 + m.b1107 + m.b1108 + m.b1109 + m.b1110
                          + m.b1111 + m.b1112 + m.b1113 + m.b1114 == 1)

m.c531 = Constraint(expr=   m.b1115 + m.b1116 + m.b1117 + m.b1118 + m.b1119 + m.b1120 + m.b1121 + m.b1122 + m.b1123
                          + m.b1124 + m.b1125 + m.b1126 + m.b1127 == 1)

m.c532 = Constraint(expr=   m.b1128 + m.b1129 + m.b1130 + m.b1131 + m.b1132 + m.b1133 + m.b1134 + m.b1135 + m.b1136
                          + m.b1137 + m.b1138 + m.b1139 + m.b1140 == 1)

m.c533 = Constraint(expr=   m.b1141 + m.b1142 + m.b1143 + m.b1144 + m.b1145 + m.b1146 + m.b1147 + m.b1148 + m.b1149
                          + m.b1150 + m.b1151 + m.b1152 + m.b1153 == 1)

m.c534 = Constraint(expr=   m.b1154 + m.b1155 + m.b1156 + m.b1157 + m.b1158 + m.b1159 + m.b1160 + m.b1161 + m.b1162
                          + m.b1163 + m.b1164 + m.b1165 + m.b1166 == 1)

m.c535 = Constraint(expr=   m.b1167 + m.b1168 + m.b1169 + m.b1170 + m.b1171 + m.b1172 + m.b1173 + m.b1174 + m.b1175
                          + m.b1176 + m.b1177 + m.b1178 + m.b1179 == 1)

m.c536 = Constraint(expr=   m.b1180 + m.b1181 + m.b1182 + m.b1183 + m.b1184 + m.b1185 + m.b1186 + m.b1187 + m.b1188
                          + m.b1189 + m.b1190 + m.b1191 + m.b1192 == 1)

m.c537 = Constraint(expr=   m.b1193 + m.b1194 + m.b1195 + m.b1196 + m.b1197 + m.b1198 + m.b1199 + m.b1200 + m.b1201
                          + m.b1202 + m.b1203 + m.b1204 + m.b1205 == 1)

m.c538 = Constraint(expr=   m.b1206 + m.b1207 + m.b1208 + m.b1209 + m.b1210 + m.b1211 + m.b1212 + m.b1213 + m.b1214
                          + m.b1215 + m.b1216 + m.b1217 + m.b1218 == 1)

m.c539 = Constraint(expr=   m.b1219 + m.b1220 + m.b1221 + m.b1222 + m.b1223 + m.b1224 + m.b1225 + m.b1226 + m.b1227
                          + m.b1228 + m.b1229 + m.b1230 + m.b1231 == 1)

m.c540 = Constraint(expr=   m.b1232 + m.b1233 + m.b1234 + m.b1235 + m.b1236 + m.b1237 + m.b1238 + m.b1239 + m.b1240
                          + m.b1241 + m.b1242 + m.b1243 + m.b1244 == 1)

m.c541 = Constraint(expr=   m.b1245 + m.b1246 + m.b1247 + m.b1248 + m.b1249 + m.b1250 + m.b1251 + m.b1252 + m.b1253
                          + m.b1254 + m.b1255 + m.b1256 + m.b1257 == 1)

m.c542 = Constraint(expr=   m.b1258 + m.b1259 + m.b1260 + m.b1261 + m.b1262 + m.b1263 + m.b1264 + m.b1265 + m.b1266
                          + m.b1267 + m.b1268 + m.b1269 + m.b1270 == 1)

m.c543 = Constraint(expr=   m.b1271 + m.b1272 + m.b1273 + m.b1274 + m.b1275 + m.b1276 + m.b1277 + m.b1278 + m.b1279
                          + m.b1280 + m.b1281 + m.b1282 + m.b1283 == 1)

m.c544 = Constraint(expr=   m.b1284 + m.b1285 + m.b1286 + m.b1287 + m.b1288 + m.b1289 + m.b1290 + m.b1291 + m.b1292
                          + m.b1293 + m.b1294 + m.b1295 + m.b1296 == 1)

m.c545 = Constraint(expr=   m.b1297 + m.b1298 + m.b1299 + m.b1300 + m.b1301 + m.b1302 + m.b1303 + m.b1304 + m.b1305
                          + m.b1306 + m.b1307 + m.b1308 + m.b1309 == 1)

m.c546 = Constraint(expr=   m.b1310 + m.b1311 + m.b1312 + m.b1313 + m.b1314 + m.b1315 + m.b1316 + m.b1317 + m.b1318
                          + m.b1319 + m.b1320 + m.b1321 + m.b1322 == 1)

m.c547 = Constraint(expr=   m.b1323 + m.b1324 + m.b1325 + m.b1326 + m.b1327 + m.b1328 + m.b1329 + m.b1330 + m.b1331
                          + m.b1332 + m.b1333 + m.b1334 + m.b1335 == 1)

m.c548 = Constraint(expr=   m.b1336 + m.b1337 + m.b1338 + m.b1339 + m.b1340 + m.b1341 + m.b1342 + m.b1343 + m.b1344
                          + m.b1345 + m.b1346 + m.b1347 + m.b1348 == 1)

m.c549 = Constraint(expr=   m.b1349 + m.b1350 + m.b1351 + m.b1352 + m.b1353 + m.b1354 + m.b1355 + m.b1356 + m.b1357
                          + m.b1358 + m.b1359 + m.b1360 + m.b1361 == 1)

m.c550 = Constraint(expr=   m.b1362 + m.b1363 + m.b1364 + m.b1365 + m.b1366 + m.b1367 + m.b1368 + m.b1369 + m.b1370
                          + m.b1371 + m.b1372 + m.b1373 + m.b1374 == 1)

m.c551 = Constraint(expr=   m.b1375 + m.b1376 + m.b1377 + m.b1378 + m.b1379 + m.b1380 + m.b1381 + m.b1382 + m.b1383
                          + m.b1384 + m.b1385 + m.b1386 + m.b1387 == 1)

m.c552 = Constraint(expr=   m.b1388 + m.b1389 + m.b1390 + m.b1391 + m.b1392 + m.b1393 + m.b1394 + m.b1395 + m.b1396
                          + m.b1397 + m.b1398 + m.b1399 + m.b1400 == 1)

m.c553 = Constraint(expr=   m.b1401 + m.b1402 + m.b1403 + m.b1404 + m.b1405 + m.b1406 + m.b1407 + m.b1408 + m.b1409
                          + m.b1410 + m.b1411 + m.b1412 + m.b1413 == 1)

m.c554 = Constraint(expr=   m.b1414 + m.b1415 + m.b1416 + m.b1417 + m.b1418 + m.b1419 + m.b1420 + m.b1421 + m.b1422
                          + m.b1423 + m.b1424 + m.b1425 + m.b1426 == 1)

m.c555 = Constraint(expr=   m.b1427 + m.b1428 + m.b1429 + m.b1430 + m.b1431 + m.b1432 + m.b1433 + m.b1434 + m.b1435
                          + m.b1436 + m.b1437 + m.b1438 + m.b1439 == 1)

m.c556 = Constraint(expr=   m.b1440 + m.b1441 + m.b1442 + m.b1443 + m.b1444 + m.b1445 + m.b1446 + m.b1447 + m.b1448
                          + m.b1449 + m.b1450 + m.b1451 + m.b1452 == 1)

m.c557 = Constraint(expr=   m.b1453 + m.b1454 + m.b1455 + m.b1456 + m.b1457 + m.b1458 + m.b1459 + m.b1460 + m.b1461
                          + m.b1462 + m.b1463 + m.b1464 + m.b1465 == 1)

m.c558 = Constraint(expr=   m.b1466 + m.b1467 + m.b1468 + m.b1469 + m.b1470 + m.b1471 + m.b1472 + m.b1473 + m.b1474
                          + m.b1475 + m.b1476 + m.b1477 + m.b1478 == 1)

m.c559 = Constraint(expr=   m.b1479 + m.b1480 + m.b1481 + m.b1482 + m.b1483 + m.b1484 + m.b1485 + m.b1486 + m.b1487
                          + m.b1488 + m.b1489 + m.b1490 + m.b1491 == 1)

m.c560 = Constraint(expr=   m.b1492 + m.b1493 + m.b1494 + m.b1495 + m.b1496 + m.b1497 + m.b1498 + m.b1499 + m.b1500
                          + m.b1501 + m.b1502 + m.b1503 + m.b1504 == 1)

m.c561 = Constraint(expr=   m.b1505 + m.b1506 + m.b1507 + m.b1508 + m.b1509 + m.b1510 + m.b1511 + m.b1512 + m.b1513
                          + m.b1514 + m.b1515 + m.b1516 + m.b1517 == 1)

m.c562 = Constraint(expr=   m.b1518 + m.b1519 + m.b1520 + m.b1521 + m.b1522 + m.b1523 + m.b1524 + m.b1525 + m.b1526
                          + m.b1527 + m.b1528 + m.b1529 + m.b1530 == 1)

m.c563 = Constraint(expr=   m.b1531 + m.b1532 + m.b1533 + m.b1534 + m.b1535 + m.b1536 + m.b1537 + m.b1538 + m.b1539
                          + m.b1540 + m.b1541 + m.b1542 + m.b1543 == 1)

m.c564 = Constraint(expr=   m.b1544 + m.b1545 + m.b1546 + m.b1547 + m.b1548 + m.b1549 + m.b1550 + m.b1551 + m.b1552
                          + m.b1553 + m.b1554 + m.b1555 + m.b1556 == 1)
