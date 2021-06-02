#  NLP written by GAMS Convert at 04/21/18 13:55:06
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        205      193        0       12        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        209      209        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        843      663      180        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,1000000),initialize=0)

m.obj = Objective(expr=   m.x50 + m.x51 + m.x52 + m.x53 + m.x54, sense=minimize)

m.c2 = Constraint(expr= - m.x26 - m.x34 - m.x35 - m.x36 - m.x37 - m.x38 == -50)

m.c3 = Constraint(expr= - m.x27 - m.x39 - m.x40 - m.x41 - m.x42 - m.x43 == -120)

m.c4 = Constraint(expr= - m.x28 - m.x44 - m.x45 - m.x46 - m.x47 - m.x48 == -70)

m.c5 = Constraint(expr= - m.x1 - m.x6 - m.x11 - m.x16 - m.x21 - m.x34 - m.x39 - m.x44 + m.x50 == 0)

m.c6 = Constraint(expr= - m.x2 - m.x7 - m.x12 - m.x17 - m.x22 - m.x35 - m.x40 - m.x45 + m.x51 == 0)

m.c7 = Constraint(expr= - m.x3 - m.x8 - m.x13 - m.x18 - m.x23 - m.x36 - m.x41 - m.x46 + m.x52 == 0)

m.c8 = Constraint(expr= - m.x4 - m.x9 - m.x14 - m.x19 - m.x24 - m.x37 - m.x42 - m.x47 + m.x53 == 0)

m.c9 = Constraint(expr= - m.x5 - m.x10 - m.x15 - m.x20 - m.x25 - m.x38 - m.x43 - m.x48 + m.x54 == 0)

m.c10 = Constraint(expr= - m.x1 - m.x2 - m.x3 - m.x4 - m.x5 - m.x29 + m.x50 == 0)

m.c11 = Constraint(expr= - m.x6 - m.x7 - m.x8 - m.x9 - m.x10 - m.x30 + m.x51 == 0)

m.c12 = Constraint(expr= - m.x11 - m.x12 - m.x13 - m.x14 - m.x15 - m.x31 + m.x52 == 0)

m.c13 = Constraint(expr= - m.x16 - m.x17 - m.x18 - m.x19 - m.x20 - m.x32 + m.x53 == 0)

m.c14 = Constraint(expr= - m.x21 - m.x22 - m.x23 - m.x24 - m.x25 - m.x33 + m.x54 == 0)

m.c15 = Constraint(expr= - m.x26 - m.x27 - m.x28 - m.x29 - m.x30 - m.x31 - m.x32 - m.x33 + m.x49 == 0)

m.c16 = Constraint(expr= - m.x105 - m.x121 - m.x123 - m.x125 - m.x127 - m.x129 == -500)

m.c17 = Constraint(expr= - m.x106 - m.x122 - m.x124 - m.x126 - m.x128 - m.x130 == -10000)

m.c18 = Constraint(expr= - m.x107 - m.x131 - m.x133 - m.x135 - m.x137 - m.x139 == -13200)

m.c19 = Constraint(expr= - m.x108 - m.x132 - m.x134 - m.x136 - m.x138 - m.x140 == -16800)

m.c20 = Constraint(expr= - m.x109 - m.x141 - m.x143 - m.x145 - m.x147 - m.x149 == -7000)

m.c21 = Constraint(expr= - m.x110 - m.x142 - m.x144 - m.x146 - m.x148 - m.x150 == -1750)

m.c22 = Constraint(expr= - m.x121 + 500*m.x194 == 0)

m.c23 = Constraint(expr= - m.x122 + 10000*m.x194 == 0)

m.c24 = Constraint(expr= - m.x123 + 500*m.x195 == 0)

m.c25 = Constraint(expr= - m.x124 + 10000*m.x195 == 0)

m.c26 = Constraint(expr= - m.x125 + 500*m.x196 == 0)

m.c27 = Constraint(expr= - m.x126 + 10000*m.x196 == 0)

m.c28 = Constraint(expr= - m.x127 + 500*m.x197 == 0)

m.c29 = Constraint(expr= - m.x128 + 10000*m.x197 == 0)

m.c30 = Constraint(expr= - m.x129 + 500*m.x198 == 0)

m.c31 = Constraint(expr= - m.x130 + 10000*m.x198 == 0)

m.c32 = Constraint(expr= - m.x131 + 13200*m.x199 == 0)

m.c33 = Constraint(expr= - m.x132 + 16800*m.x199 == 0)

m.c34 = Constraint(expr= - m.x133 + 13200*m.x200 == 0)

m.c35 = Constraint(expr= - m.x134 + 16800*m.x200 == 0)

m.c36 = Constraint(expr= - m.x135 + 13200*m.x201 == 0)

m.c37 = Constraint(expr= - m.x136 + 16800*m.x201 == 0)

m.c38 = Constraint(expr= - m.x137 + 13200*m.x202 == 0)

m.c39 = Constraint(expr= - m.x138 + 16800*m.x202 == 0)

m.c40 = Constraint(expr= - m.x139 + 13200*m.x203 == 0)

m.c41 = Constraint(expr= - m.x140 + 16800*m.x203 == 0)

m.c42 = Constraint(expr= - m.x141 + 7000*m.x204 == 0)

m.c43 = Constraint(expr= - m.x142 + 1750*m.x204 == 0)

m.c44 = Constraint(expr= - m.x143 + 7000*m.x205 == 0)

m.c45 = Constraint(expr= - m.x144 + 1750*m.x205 == 0)

m.c46 = Constraint(expr= - m.x145 + 7000*m.x206 == 0)

m.c47 = Constraint(expr= - m.x146 + 1750*m.x206 == 0)

m.c48 = Constraint(expr= - m.x147 + 7000*m.x207 == 0)

m.c49 = Constraint(expr= - m.x148 + 1750*m.x207 == 0)

m.c50 = Constraint(expr= - m.x149 + 7000*m.x208 == 0)

m.c51 = Constraint(expr= - m.x150 + 1750*m.x208 == 0)

m.c52 = Constraint(expr= - m.x105 + 500*m.x186 == 0)

m.c53 = Constraint(expr= - m.x106 + 10000*m.x186 == 0)

m.c54 = Constraint(expr= - m.x107 + 13200*m.x187 == 0)

m.c55 = Constraint(expr= - m.x108 + 16800*m.x187 == 0)

m.c56 = Constraint(expr= - m.x109 + 7000*m.x188 == 0)

m.c57 = Constraint(expr= - m.x110 + 1750*m.x188 == 0)

m.c58 = Constraint(expr= - m.x34 + 50*m.x194 == 0)

m.c59 = Constraint(expr= - m.x35 + 50*m.x195 == 0)

m.c60 = Constraint(expr= - m.x36 + 50*m.x196 == 0)

m.c61 = Constraint(expr= - m.x37 + 50*m.x197 == 0)

m.c62 = Constraint(expr= - m.x38 + 50*m.x198 == 0)

m.c63 = Constraint(expr= - m.x39 + 120*m.x199 == 0)

m.c64 = Constraint(expr= - m.x40 + 120*m.x200 == 0)

m.c65 = Constraint(expr= - m.x41 + 120*m.x201 == 0)

m.c66 = Constraint(expr= - m.x42 + 120*m.x202 == 0)

m.c67 = Constraint(expr= - m.x43 + 120*m.x203 == 0)

m.c68 = Constraint(expr= - m.x44 + 70*m.x204 == 0)

m.c69 = Constraint(expr= - m.x45 + 70*m.x205 == 0)

m.c70 = Constraint(expr= - m.x46 + 70*m.x206 == 0)

m.c71 = Constraint(expr= - m.x47 + 70*m.x207 == 0)

m.c72 = Constraint(expr= - m.x48 + 70*m.x208 == 0)

m.c73 = Constraint(expr= - m.x26 + 50*m.x186 == 0)

m.c74 = Constraint(expr= - m.x27 + 120*m.x187 == 0)

m.c75 = Constraint(expr= - m.x28 + 70*m.x188 == 0)

m.c76 = Constraint(expr=   m.x186 + m.x194 + m.x195 + m.x196 + m.x197 + m.x198 == 1)

m.c77 = Constraint(expr=   m.x187 + m.x199 + m.x200 + m.x201 + m.x202 + m.x203 == 1)

m.c78 = Constraint(expr=   m.x188 + m.x204 + m.x205 + m.x206 + m.x207 + m.x208 == 1)

m.c79 = Constraint(expr= - 145*m.x50 + m.x55 + m.x65 + m.x75 + m.x85 + m.x95 + m.x121 + m.x131 + m.x141 <= 0)

m.c80 = Constraint(expr= - 400*m.x50 + m.x56 + m.x66 + m.x76 + m.x86 + m.x96 + m.x122 + m.x132 + m.x142 <= 0)

m.c81 = Constraint(expr= - 110*m.x51 + m.x57 + m.x67 + m.x77 + m.x87 + m.x97 + m.x123 + m.x133 + m.x143 <= 0)

m.c82 = Constraint(expr= - 90*m.x51 + m.x58 + m.x68 + m.x78 + m.x88 + m.x98 + m.x124 + m.x134 + m.x144 <= 0)

m.c83 = Constraint(expr= - 90*m.x52 + m.x59 + m.x69 + m.x79 + m.x89 + m.x99 + m.x125 + m.x135 + m.x145 <= 0)

m.c84 = Constraint(expr= - 100*m.x52 + m.x60 + m.x70 + m.x80 + m.x90 + m.x100 + m.x126 + m.x136 + m.x146 <= 0)

m.c85 = Constraint(expr= - 200*m.x53 + m.x61 + m.x71 + m.x81 + m.x91 + m.x101 + m.x127 + m.x137 + m.x147 <= 0)

m.c86 = Constraint(expr= - 90*m.x53 + m.x62 + m.x72 + m.x82 + m.x92 + m.x102 + m.x128 + m.x138 + m.x148 <= 0)

m.c87 = Constraint(expr= - 50*m.x54 + m.x63 + m.x73 + m.x83 + m.x93 + m.x103 + m.x129 + m.x139 + m.x149 <= 0)

m.c88 = Constraint(expr= - 80*m.x54 + m.x64 + m.x74 + m.x84 + m.x94 + m.x104 + m.x130 + m.x140 + m.x150 <= 0)

m.c89 = Constraint(expr=   0.1*m.x55 + 0.1*m.x65 + 0.1*m.x75 + 0.1*m.x85 + 0.1*m.x95 + 0.1*m.x121 + 0.1*m.x131
                         + 0.1*m.x141 - m.x151 == 0)

m.c90 = Constraint(expr=   m.x56 + m.x66 + m.x76 + m.x86 + m.x96 + m.x122 + m.x132 + m.x142 - m.x152 == 0)

m.c91 = Constraint(expr=   0.3*m.x57 + 0.3*m.x67 + 0.3*m.x77 + 0.3*m.x87 + 0.3*m.x97 + 0.3*m.x123 + 0.3*m.x133
                         + 0.3*m.x143 - m.x153 == 0)

m.c92 = Constraint(expr=   0.1*m.x58 + 0.1*m.x68 + 0.1*m.x78 + 0.1*m.x88 + 0.1*m.x98 + 0.1*m.x124 + 0.1*m.x134
                         + 0.1*m.x144 - m.x154 == 0)

m.c93 = Constraint(expr=   m.x59 + m.x69 + m.x79 + m.x89 + m.x99 + m.x125 + m.x135 + m.x145 - m.x155 == 0)

m.c94 = Constraint(expr=   0.2*m.x60 + 0.2*m.x70 + 0.2*m.x80 + 0.2*m.x90 + 0.2*m.x100 + 0.2*m.x126 + 0.2*m.x136
                         + 0.2*m.x146 - m.x156 == 0)

m.c95 = Constraint(expr=   0.5*m.x61 + 0.5*m.x71 + 0.5*m.x81 + 0.5*m.x91 + 0.5*m.x101 + 0.5*m.x127 + 0.5*m.x137
                         + 0.5*m.x147 - m.x157 == 0)

m.c96 = Constraint(expr=   m.x62 + m.x72 + m.x82 + m.x92 + m.x102 + m.x128 + m.x138 + m.x148 - m.x158 == 0)

m.c97 = Constraint(expr=   0.35*m.x63 + 0.35*m.x73 + 0.35*m.x83 + 0.35*m.x93 + 0.35*m.x103 + 0.35*m.x129 + 0.35*m.x139
                         + 0.35*m.x149 - m.x159 == 0)

m.c98 = Constraint(expr=   0.4*m.x64 + 0.4*m.x74 + 0.4*m.x84 + 0.4*m.x94 + 0.4*m.x104 + 0.4*m.x130 + 0.4*m.x140
                         + 0.4*m.x150 - m.x160 == 0)

m.c99 = Constraint(expr= - m.x55 - m.x57 - m.x59 - m.x61 - m.x63 - m.x111 + m.x151 == 0)

m.c100 = Constraint(expr= - m.x56 - m.x58 - m.x60 - m.x62 - m.x64 - m.x112 + m.x152 == 0)

m.c101 = Constraint(expr= - m.x65 - m.x67 - m.x69 - m.x71 - m.x73 - m.x113 + m.x153 == 0)

m.c102 = Constraint(expr= - m.x66 - m.x68 - m.x70 - m.x72 - m.x74 - m.x114 + m.x154 == 0)

m.c103 = Constraint(expr= - m.x75 - m.x77 - m.x79 - m.x81 - m.x83 - m.x115 + m.x155 == 0)

m.c104 = Constraint(expr= - m.x76 - m.x78 - m.x80 - m.x82 - m.x84 - m.x116 + m.x156 == 0)

m.c105 = Constraint(expr= - m.x85 - m.x87 - m.x89 - m.x91 - m.x93 - m.x117 + m.x157 == 0)

m.c106 = Constraint(expr= - m.x86 - m.x88 - m.x90 - m.x92 - m.x94 - m.x118 + m.x158 == 0)

m.c107 = Constraint(expr= - m.x95 - m.x97 - m.x99 - m.x101 - m.x103 - m.x119 + m.x159 == 0)

m.c108 = Constraint(expr= - m.x96 - m.x98 - m.x100 - m.x102 - m.x104 - m.x120 + m.x160 == 0)

m.c109 = Constraint(expr=m.x151*m.x161 - m.x55 == 0)

m.c110 = Constraint(expr=m.x152*m.x161 - m.x56 == 0)

m.c111 = Constraint(expr=m.x151*m.x162 - m.x57 == 0)

m.c112 = Constraint(expr=m.x152*m.x162 - m.x58 == 0)

m.c113 = Constraint(expr=m.x151*m.x163 - m.x59 == 0)

m.c114 = Constraint(expr=m.x152*m.x163 - m.x60 == 0)

m.c115 = Constraint(expr=m.x151*m.x164 - m.x61 == 0)

m.c116 = Constraint(expr=m.x152*m.x164 - m.x62 == 0)

m.c117 = Constraint(expr=m.x151*m.x165 - m.x63 == 0)

m.c118 = Constraint(expr=m.x152*m.x165 - m.x64 == 0)

m.c119 = Constraint(expr=m.x153*m.x166 - m.x65 == 0)

m.c120 = Constraint(expr=m.x154*m.x166 - m.x66 == 0)

m.c121 = Constraint(expr=m.x153*m.x167 - m.x67 == 0)

m.c122 = Constraint(expr=m.x154*m.x167 - m.x68 == 0)

m.c123 = Constraint(expr=m.x153*m.x168 - m.x69 == 0)

m.c124 = Constraint(expr=m.x154*m.x168 - m.x70 == 0)

m.c125 = Constraint(expr=m.x153*m.x169 - m.x71 == 0)

m.c126 = Constraint(expr=m.x154*m.x169 - m.x72 == 0)

m.c127 = Constraint(expr=m.x153*m.x170 - m.x73 == 0)

m.c128 = Constraint(expr=m.x154*m.x170 - m.x74 == 0)

m.c129 = Constraint(expr=m.x155*m.x171 - m.x75 == 0)

m.c130 = Constraint(expr=m.x156*m.x171 - m.x76 == 0)

m.c131 = Constraint(expr=m.x155*m.x172 - m.x77 == 0)

m.c132 = Constraint(expr=m.x156*m.x172 - m.x78 == 0)

m.c133 = Constraint(expr=m.x155*m.x173 - m.x79 == 0)

m.c134 = Constraint(expr=m.x156*m.x173 - m.x80 == 0)

m.c135 = Constraint(expr=m.x155*m.x174 - m.x81 == 0)

m.c136 = Constraint(expr=m.x156*m.x174 - m.x82 == 0)

m.c137 = Constraint(expr=m.x155*m.x175 - m.x83 == 0)

m.c138 = Constraint(expr=m.x156*m.x175 - m.x84 == 0)

m.c139 = Constraint(expr=m.x157*m.x176 - m.x85 == 0)

m.c140 = Constraint(expr=m.x158*m.x176 - m.x86 == 0)

m.c141 = Constraint(expr=m.x157*m.x177 - m.x87 == 0)

m.c142 = Constraint(expr=m.x158*m.x177 - m.x88 == 0)

m.c143 = Constraint(expr=m.x157*m.x178 - m.x89 == 0)

m.c144 = Constraint(expr=m.x158*m.x178 - m.x90 == 0)

m.c145 = Constraint(expr=m.x157*m.x179 - m.x91 == 0)

m.c146 = Constraint(expr=m.x158*m.x179 - m.x92 == 0)

m.c147 = Constraint(expr=m.x157*m.x180 - m.x93 == 0)

m.c148 = Constraint(expr=m.x158*m.x180 - m.x94 == 0)

m.c149 = Constraint(expr=m.x159*m.x181 - m.x95 == 0)

m.c150 = Constraint(expr=m.x160*m.x181 - m.x96 == 0)

m.c151 = Constraint(expr=m.x159*m.x182 - m.x97 == 0)

m.c152 = Constraint(expr=m.x160*m.x182 - m.x98 == 0)

m.c153 = Constraint(expr=m.x159*m.x183 - m.x99 == 0)

m.c154 = Constraint(expr=m.x160*m.x183 - m.x100 == 0)

m.c155 = Constraint(expr=m.x159*m.x184 - m.x101 == 0)

m.c156 = Constraint(expr=m.x160*m.x184 - m.x102 == 0)

m.c157 = Constraint(expr=m.x159*m.x185 - m.x103 == 0)

m.c158 = Constraint(expr=m.x160*m.x185 - m.x104 == 0)

m.c159 = Constraint(expr=m.x151*m.x189 - m.x111 == 0)

m.c160 = Constraint(expr=m.x152*m.x189 - m.x112 == 0)

m.c161 = Constraint(expr=m.x153*m.x190 - m.x113 == 0)

m.c162 = Constraint(expr=m.x154*m.x190 - m.x114 == 0)

m.c163 = Constraint(expr=m.x155*m.x191 - m.x115 == 0)

m.c164 = Constraint(expr=m.x156*m.x191 - m.x116 == 0)

m.c165 = Constraint(expr=m.x157*m.x192 - m.x117 == 0)

m.c166 = Constraint(expr=m.x158*m.x192 - m.x118 == 0)

m.c167 = Constraint(expr=m.x159*m.x193 - m.x119 == 0)

m.c168 = Constraint(expr=m.x160*m.x193 - m.x120 == 0)

m.c169 = Constraint(expr=m.x50*m.x161 - m.x1 == 0)

m.c170 = Constraint(expr=m.x50*m.x162 - m.x2 == 0)

m.c171 = Constraint(expr=m.x50*m.x163 - m.x3 == 0)

m.c172 = Constraint(expr=m.x50*m.x164 - m.x4 == 0)

m.c173 = Constraint(expr=m.x50*m.x165 - m.x5 == 0)

m.c174 = Constraint(expr=m.x51*m.x166 - m.x6 == 0)

m.c175 = Constraint(expr=m.x51*m.x167 - m.x7 == 0)

m.c176 = Constraint(expr=m.x51*m.x168 - m.x8 == 0)

m.c177 = Constraint(expr=m.x51*m.x169 - m.x9 == 0)

m.c178 = Constraint(expr=m.x51*m.x170 - m.x10 == 0)

m.c179 = Constraint(expr=m.x52*m.x171 - m.x11 == 0)

m.c180 = Constraint(expr=m.x52*m.x172 - m.x12 == 0)

m.c181 = Constraint(expr=m.x52*m.x173 - m.x13 == 0)

m.c182 = Constraint(expr=m.x52*m.x174 - m.x14 == 0)

m.c183 = Constraint(expr=m.x52*m.x175 - m.x15 == 0)

m.c184 = Constraint(expr=m.x53*m.x176 - m.x16 == 0)

m.c185 = Constraint(expr=m.x53*m.x177 - m.x17 == 0)

m.c186 = Constraint(expr=m.x53*m.x178 - m.x18 == 0)

m.c187 = Constraint(expr=m.x53*m.x179 - m.x19 == 0)

m.c188 = Constraint(expr=m.x53*m.x180 - m.x20 == 0)

m.c189 = Constraint(expr=m.x54*m.x181 - m.x21 == 0)

m.c190 = Constraint(expr=m.x54*m.x182 - m.x22 == 0)

m.c191 = Constraint(expr=m.x54*m.x183 - m.x23 == 0)

m.c192 = Constraint(expr=m.x54*m.x184 - m.x24 == 0)

m.c193 = Constraint(expr=m.x54*m.x185 - m.x25 == 0)

m.c194 = Constraint(expr=m.x50*m.x189 - m.x29 == 0)

m.c195 = Constraint(expr=m.x51*m.x190 - m.x30 == 0)

m.c196 = Constraint(expr=m.x52*m.x191 - m.x31 == 0)

m.c197 = Constraint(expr=m.x53*m.x192 - m.x32 == 0)

m.c198 = Constraint(expr=m.x54*m.x193 - m.x33 == 0)

m.c199 = Constraint(expr=   m.x161 + m.x162 + m.x163 + m.x164 + m.x165 + m.x189 == 1)

m.c200 = Constraint(expr=   m.x166 + m.x167 + m.x168 + m.x169 + m.x170 + m.x190 == 1)

m.c201 = Constraint(expr=   m.x171 + m.x172 + m.x173 + m.x174 + m.x175 + m.x191 == 1)

m.c202 = Constraint(expr=   m.x176 + m.x177 + m.x178 + m.x179 + m.x180 + m.x192 == 1)

m.c203 = Constraint(expr=   m.x181 + m.x182 + m.x183 + m.x184 + m.x185 + m.x193 == 1)

m.c204 = Constraint(expr= - 10*m.x49 + m.x105 + m.x107 + m.x109 + m.x111 + m.x113 + m.x115 + m.x117 + m.x119 <= 0)

m.c205 = Constraint(expr= - 5*m.x49 + m.x106 + m.x108 + m.x110 + m.x112 + m.x114 + m.x116 + m.x118 + m.x120 <= 0)
