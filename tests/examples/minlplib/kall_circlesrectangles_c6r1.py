#  NLP written by GAMS Convert at 04/21/18 13:52:27
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        192      155       15       22        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        184      184        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        653      355      298        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(2.89,36),initialize=2.89)
m.x2 = Var(within=Reals,bounds=(0,9),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,9),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,9),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,9),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,9),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,9),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,9.84885780179611),initialize=0)
m.x38 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x39 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x40 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x41 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x42 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x43 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x44 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x45 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x46 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x47 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x48 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x49 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x50 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x51 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x52 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x53 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x54 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x55 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x56 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x57 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x58 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x59 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x60 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x61 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x62 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x63 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x64 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x65 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x66 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x67 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x68 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x69 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x70 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x71 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x72 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x73 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x74 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x75 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x76 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x77 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x78 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x79 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x80 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x81 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x82 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x83 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x84 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x85 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x86 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x87 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x88 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x89 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x90 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x91 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x92 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x93 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x94 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x95 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x96 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x97 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x98 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x99 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x100 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x101 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x102 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x103 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x104 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x105 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x106 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x107 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x108 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x109 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x110 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x111 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x112 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x113 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x114 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x115 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x116 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x117 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x118 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x119 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x120 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x121 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x122 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x123 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x124 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x125 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x126 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x127 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x128 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x129 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x130 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x131 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x132 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x133 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x134 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x135 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x136 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x137 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x138 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x139 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x140 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x141 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x142 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x143 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x144 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x145 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x146 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x147 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x148 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x149 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x150 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x151 = Var(within=Reals,bounds=(-9.84885780179611,9.84885780179611),initialize=0)
m.x152 = Var(within=Reals,bounds=(-0.8,0.8),initialize=0)
m.x153 = Var(within=Reals,bounds=(-0.5,0.5),initialize=0)
m.x154 = Var(within=Reals,bounds=(-0.8,0.8),initialize=0)
m.x155 = Var(within=Reals,bounds=(-0.5,0.5),initialize=0)
m.x156 = Var(within=Reals,bounds=(-0.8,0.8),initialize=0)
m.x157 = Var(within=Reals,bounds=(-0.5,0.5),initialize=0)
m.x158 = Var(within=Reals,bounds=(-0.8,0.8),initialize=0)
m.x159 = Var(within=Reals,bounds=(-0.5,0.5),initialize=0)
m.x160 = Var(within=Reals,bounds=(1.2,7.8),initialize=1.2)
m.x161 = Var(within=Reals,bounds=(1.2,2.8),initialize=1.2)
m.x162 = Var(within=Reals,bounds=(0.6,8.4),initialize=0.6)
m.x163 = Var(within=Reals,bounds=(0.6,3.4),initialize=0.6)
m.x164 = Var(within=Reals,bounds=(0.8,8.2),initialize=0.8)
m.x165 = Var(within=Reals,bounds=(0.8,3.2),initialize=0.8)
m.x166 = Var(within=Reals,bounds=(1.7,7.3),initialize=1.7)
m.x167 = Var(within=Reals,bounds=(1.7,2.3),initialize=1.7)
m.x168 = Var(within=Reals,bounds=(1.3,7.7),initialize=1.3)
m.x169 = Var(within=Reals,bounds=(1.3,2.7),initialize=1.3)
m.x170 = Var(within=Reals,bounds=(0.5,8.5),initialize=0.5)
m.x171 = Var(within=Reals,bounds=(0.5,3.5),initialize=0.5)
m.x172 = Var(within=Reals,bounds=(0,9),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,9),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,9),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,9),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,9),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,9),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,36),initialize=0)

m.obj = Objective(expr=m.x184, sense=minimize)

m.c1 = Constraint(expr= - m.x1 + m.x184 == -23.2393785915978)

m.c2 = Constraint(expr=-m.x172*m.x173 + m.x1 == 0)

m.c3 = Constraint(expr=(m.x160 - m.x162)*(m.x160 - m.x162) + (m.x161 - m.x163)*(m.x161 - m.x163) >= 3.24)

m.c4 = Constraint(expr=(m.x160 - m.x164)*(m.x160 - m.x164) + (m.x161 - m.x165)*(m.x161 - m.x165) >= 4)

m.c5 = Constraint(expr=(m.x160 - m.x166)*(m.x160 - m.x166) + (m.x161 - m.x167)*(m.x161 - m.x167) >= 8.41)

m.c6 = Constraint(expr=(m.x160 - m.x168)*(m.x160 - m.x168) + (m.x161 - m.x169)*(m.x161 - m.x169) >= 6.25)

m.c7 = Constraint(expr=(m.x160 - m.x170)*(m.x160 - m.x170) + (m.x161 - m.x171)*(m.x161 - m.x171) >= 2.89)

m.c8 = Constraint(expr=(m.x162 - m.x164)*(m.x162 - m.x164) + (m.x163 - m.x165)*(m.x163 - m.x165) >= 1.96)

m.c9 = Constraint(expr=(m.x162 - m.x166)*(m.x162 - m.x166) + (m.x163 - m.x167)*(m.x163 - m.x167) >= 5.29)

m.c10 = Constraint(expr=(m.x162 - m.x168)*(m.x162 - m.x168) + (m.x163 - m.x169)*(m.x163 - m.x169) >= 3.61)

m.c11 = Constraint(expr=(m.x162 - m.x170)*(m.x162 - m.x170) + (m.x163 - m.x171)*(m.x163 - m.x171) >= 1.21)

m.c12 = Constraint(expr=(m.x164 - m.x166)*(m.x164 - m.x166) + (m.x165 - m.x167)*(m.x165 - m.x167) >= 6.25)

m.c13 = Constraint(expr=(m.x164 - m.x168)*(m.x164 - m.x168) + (m.x165 - m.x169)*(m.x165 - m.x169) >= 4.41)

m.c14 = Constraint(expr=(m.x164 - m.x170)*(m.x164 - m.x170) + (m.x165 - m.x171)*(m.x165 - m.x171) >= 1.69)

m.c15 = Constraint(expr=(m.x166 - m.x168)*(m.x166 - m.x168) + (m.x167 - m.x169)*(m.x167 - m.x169) >= 9)

m.c16 = Constraint(expr=(m.x166 - m.x170)*(m.x166 - m.x170) + (m.x167 - m.x171)*(m.x167 - m.x171) >= 4.84)

m.c17 = Constraint(expr=(m.x168 - m.x170)*(m.x168 - m.x170) + (m.x169 - m.x171)*(m.x169 - m.x171) >= 3.24)

m.c18 = Constraint(expr=   m.x160 - m.x172 <= -1.2)

m.c19 = Constraint(expr=   m.x161 - m.x173 <= -1.2)

m.c20 = Constraint(expr=   m.x162 - m.x172 <= -0.6)

m.c21 = Constraint(expr=   m.x163 - m.x173 <= -0.6)

m.c22 = Constraint(expr=   m.x164 - m.x172 <= -0.8)

m.c23 = Constraint(expr=   m.x165 - m.x173 <= -0.8)

m.c24 = Constraint(expr=   m.x166 - m.x172 <= -1.7)

m.c25 = Constraint(expr=   m.x167 - m.x173 <= -1.7)

m.c26 = Constraint(expr=   m.x168 - m.x172 <= -1.3)

m.c27 = Constraint(expr=   m.x169 - m.x173 <= -1.3)

m.c28 = Constraint(expr=   m.x170 - m.x172 <= -0.5)

m.c29 = Constraint(expr=   m.x171 - m.x173 <= -0.5)

m.c30 = Constraint(expr= - m.x172 + m.x174 <= 0)

m.c31 = Constraint(expr= - m.x173 + m.x175 <= 0)

m.c32 = Constraint(expr= - m.x172 + m.x176 <= 0)

m.c33 = Constraint(expr= - m.x173 + m.x177 <= 0)

m.c34 = Constraint(expr= - m.x172 + m.x178 <= 0)

m.c35 = Constraint(expr= - m.x173 + m.x179 <= 0)

m.c36 = Constraint(expr= - m.x172 + m.x180 <= 0)

m.c37 = Constraint(expr= - m.x173 + m.x181 <= 0)

m.c38 = Constraint(expr=   m.x152 + m.x174 - m.x176 == 0)

m.c39 = Constraint(expr=   m.x153 + m.x175 - m.x177 == 0)

m.c40 = Constraint(expr=   m.x154 + m.x176 - m.x178 == 0)

m.c41 = Constraint(expr=   m.x155 + m.x177 - m.x179 == 0)

m.c42 = Constraint(expr=   m.x156 + m.x178 - m.x180 == 0)

m.c43 = Constraint(expr=   m.x157 + m.x179 - m.x181 == 0)

m.c44 = Constraint(expr=   m.x158 - m.x174 + 2*m.x180 - m.x182 == 0)

m.c45 = Constraint(expr=   m.x159 - m.x175 + 2*m.x181 - m.x183 == 0)

m.c46 = Constraint(expr=m.x152*m.x154 + m.x153*m.x155 == 0)

m.c47 = Constraint(expr=   m.x152 + m.x156 == 0)

m.c48 = Constraint(expr=   m.x153 + m.x157 == 0)

m.c49 = Constraint(expr=   m.x154 + m.x158 == 0)

m.c50 = Constraint(expr=   m.x155 + m.x159 == 0)

m.c51 = Constraint(expr=m.x152*m.x152 + m.x153*m.x153 == 0.25)

m.c52 = Constraint(expr=m.x154*m.x154 + m.x155*m.x155 == 0.64)

m.c53 = Constraint(expr=m.x68*m.x68 + m.x69*m.x69 == 1)

m.c54 = Constraint(expr=m.x70*m.x70 + m.x71*m.x71 == 1)

m.c55 = Constraint(expr=m.x72*m.x72 + m.x73*m.x73 == 1)

m.c56 = Constraint(expr=m.x74*m.x74 + m.x75*m.x75 == 1)

m.c57 = Constraint(expr=m.x76*m.x76 + m.x77*m.x77 == 1)

m.c58 = Constraint(expr=m.x78*m.x78 + m.x79*m.x79 == 1)

m.c59 = Constraint(expr= - m.x69 + m.x80 == 0)

m.c60 = Constraint(expr= - m.x71 + m.x82 == 0)

m.c61 = Constraint(expr= - m.x73 + m.x84 == 0)

m.c62 = Constraint(expr= - m.x75 + m.x86 == 0)

m.c63 = Constraint(expr= - m.x77 + m.x88 == 0)

m.c64 = Constraint(expr= - m.x79 + m.x90 == 0)

m.c65 = Constraint(expr=   m.x68 + m.x81 == 0)

m.c66 = Constraint(expr=   m.x70 + m.x83 == 0)

m.c67 = Constraint(expr=   m.x72 + m.x85 == 0)

m.c68 = Constraint(expr=   m.x74 + m.x87 == 0)

m.c69 = Constraint(expr=   m.x76 + m.x89 == 0)

m.c70 = Constraint(expr=   m.x78 + m.x91 == 0)

m.c71 = Constraint(expr=m.x68*m.x38 + m.x2 + m.x92 - m.x174 == 0)

m.c72 = Constraint(expr=m.x69*m.x38 + m.x3 + m.x93 - m.x175 == 0)

m.c73 = Constraint(expr=m.x68*m.x39 + m.x2 + m.x94 - m.x176 == 0)

m.c74 = Constraint(expr=m.x69*m.x39 + m.x3 + m.x95 - m.x177 == 0)

m.c75 = Constraint(expr=m.x68*m.x40 + m.x2 + m.x96 - m.x178 == 0)

m.c76 = Constraint(expr=m.x69*m.x40 + m.x3 + m.x97 - m.x179 == 0)

m.c77 = Constraint(expr=m.x68*m.x41 + m.x2 + m.x98 - m.x180 == 0)

m.c78 = Constraint(expr=m.x69*m.x41 + m.x3 + m.x99 - m.x181 == 0)

m.c79 = Constraint(expr=m.x70*m.x42 + m.x4 + m.x100 - m.x174 == 0)

m.c80 = Constraint(expr=m.x71*m.x42 + m.x5 + m.x101 - m.x175 == 0)

m.c81 = Constraint(expr=m.x70*m.x43 + m.x4 + m.x102 - m.x176 == 0)

m.c82 = Constraint(expr=m.x71*m.x43 + m.x5 + m.x103 - m.x177 == 0)

m.c83 = Constraint(expr=m.x70*m.x44 + m.x4 + m.x104 - m.x178 == 0)

m.c84 = Constraint(expr=m.x71*m.x44 + m.x5 + m.x105 - m.x179 == 0)

m.c85 = Constraint(expr=m.x70*m.x45 + m.x4 + m.x106 - m.x180 == 0)

m.c86 = Constraint(expr=m.x71*m.x45 + m.x5 + m.x107 - m.x181 == 0)

m.c87 = Constraint(expr=m.x72*m.x46 + m.x6 + m.x108 - m.x174 == 0)

m.c88 = Constraint(expr=m.x73*m.x46 + m.x7 + m.x109 - m.x175 == 0)

m.c89 = Constraint(expr=m.x72*m.x47 + m.x6 + m.x110 - m.x176 == 0)

m.c90 = Constraint(expr=m.x73*m.x47 + m.x7 + m.x111 - m.x177 == 0)

m.c91 = Constraint(expr=m.x72*m.x48 + m.x6 + m.x112 - m.x178 == 0)

m.c92 = Constraint(expr=m.x73*m.x48 + m.x7 + m.x113 - m.x179 == 0)

m.c93 = Constraint(expr=m.x72*m.x49 + m.x6 + m.x114 - m.x180 == 0)

m.c94 = Constraint(expr=m.x73*m.x49 + m.x7 + m.x115 - m.x181 == 0)

m.c95 = Constraint(expr=m.x74*m.x50 + m.x8 + m.x116 - m.x174 == 0)

m.c96 = Constraint(expr=m.x75*m.x50 + m.x9 + m.x117 - m.x175 == 0)

m.c97 = Constraint(expr=m.x74*m.x51 + m.x8 + m.x118 - m.x176 == 0)

m.c98 = Constraint(expr=m.x75*m.x51 + m.x9 + m.x119 - m.x177 == 0)

m.c99 = Constraint(expr=m.x74*m.x52 + m.x8 + m.x120 - m.x178 == 0)

m.c100 = Constraint(expr=m.x75*m.x52 + m.x9 + m.x121 - m.x179 == 0)

m.c101 = Constraint(expr=m.x74*m.x53 + m.x8 + m.x122 - m.x180 == 0)

m.c102 = Constraint(expr=m.x75*m.x53 + m.x9 + m.x123 - m.x181 == 0)

m.c103 = Constraint(expr=m.x76*m.x54 + m.x10 + m.x124 - m.x174 == 0)

m.c104 = Constraint(expr=m.x77*m.x54 + m.x11 + m.x125 - m.x175 == 0)

m.c105 = Constraint(expr=m.x76*m.x55 + m.x10 + m.x126 - m.x176 == 0)

m.c106 = Constraint(expr=m.x77*m.x55 + m.x11 + m.x127 - m.x177 == 0)

m.c107 = Constraint(expr=m.x76*m.x56 + m.x10 + m.x128 - m.x178 == 0)

m.c108 = Constraint(expr=m.x77*m.x56 + m.x11 + m.x129 - m.x179 == 0)

m.c109 = Constraint(expr=m.x76*m.x57 + m.x10 + m.x130 - m.x180 == 0)

m.c110 = Constraint(expr=m.x77*m.x57 + m.x11 + m.x131 - m.x181 == 0)

m.c111 = Constraint(expr=m.x78*m.x58 + m.x12 + m.x132 - m.x174 == 0)

m.c112 = Constraint(expr=m.x79*m.x58 + m.x13 + m.x133 - m.x175 == 0)

m.c113 = Constraint(expr=m.x78*m.x59 + m.x12 + m.x134 - m.x176 == 0)

m.c114 = Constraint(expr=m.x79*m.x59 + m.x13 + m.x135 - m.x177 == 0)

m.c115 = Constraint(expr=m.x78*m.x60 + m.x12 + m.x136 - m.x178 == 0)

m.c116 = Constraint(expr=m.x79*m.x60 + m.x13 + m.x137 - m.x179 == 0)

m.c117 = Constraint(expr=m.x78*m.x61 + m.x12 + m.x138 - m.x180 == 0)

m.c118 = Constraint(expr=m.x79*m.x61 + m.x13 + m.x139 - m.x181 == 0)

m.c119 = Constraint(expr=m.x68*m.x62 + m.x2 + m.x140 - m.x160 == 0)

m.c120 = Constraint(expr=m.x69*m.x62 + m.x3 + m.x141 - m.x161 == 0)

m.c121 = Constraint(expr=m.x70*m.x63 + m.x4 + m.x142 - m.x162 == 0)

m.c122 = Constraint(expr=m.x71*m.x63 + m.x5 + m.x143 - m.x163 == 0)

m.c123 = Constraint(expr=m.x72*m.x64 + m.x6 + m.x144 - m.x164 == 0)

m.c124 = Constraint(expr=m.x73*m.x64 + m.x7 + m.x145 - m.x165 == 0)

m.c125 = Constraint(expr=m.x74*m.x65 + m.x8 + m.x146 - m.x166 == 0)

m.c126 = Constraint(expr=m.x75*m.x65 + m.x9 + m.x147 - m.x167 == 0)

m.c127 = Constraint(expr=m.x76*m.x66 + m.x10 + m.x148 - m.x168 == 0)

m.c128 = Constraint(expr=m.x77*m.x66 + m.x11 + m.x149 - m.x169 == 0)

m.c129 = Constraint(expr=m.x78*m.x67 + m.x12 + m.x150 - m.x170 == 0)

m.c130 = Constraint(expr=m.x79*m.x67 + m.x13 + m.x151 - m.x171 == 0)

m.c131 = Constraint(expr=-m.x14*m.x80 + m.x92 == 0)

m.c132 = Constraint(expr=-m.x14*m.x81 + m.x93 == 0)

m.c133 = Constraint(expr=-m.x15*m.x80 + m.x94 == 0)

m.c134 = Constraint(expr=-m.x15*m.x81 + m.x95 == 0)

m.c135 = Constraint(expr=-m.x16*m.x80 + m.x96 == 0)

m.c136 = Constraint(expr=-m.x16*m.x81 + m.x97 == 0)

m.c137 = Constraint(expr=-m.x17*m.x80 + m.x98 == 0)

m.c138 = Constraint(expr=-m.x17*m.x81 + m.x99 == 0)

m.c139 = Constraint(expr=-m.x18*m.x82 + m.x100 == 0)

m.c140 = Constraint(expr=-m.x18*m.x83 + m.x101 == 0)

m.c141 = Constraint(expr=-m.x19*m.x82 + m.x102 == 0)

m.c142 = Constraint(expr=-m.x19*m.x83 + m.x103 == 0)

m.c143 = Constraint(expr=-m.x20*m.x82 + m.x104 == 0)

m.c144 = Constraint(expr=-m.x20*m.x83 + m.x105 == 0)

m.c145 = Constraint(expr=-m.x21*m.x82 + m.x106 == 0)

m.c146 = Constraint(expr=-m.x21*m.x83 + m.x107 == 0)

m.c147 = Constraint(expr=-m.x22*m.x84 + m.x108 == 0)

m.c148 = Constraint(expr=-m.x22*m.x85 + m.x109 == 0)

m.c149 = Constraint(expr=-m.x23*m.x84 + m.x110 == 0)

m.c150 = Constraint(expr=-m.x23*m.x85 + m.x111 == 0)

m.c151 = Constraint(expr=-m.x24*m.x84 + m.x112 == 0)

m.c152 = Constraint(expr=-m.x24*m.x85 + m.x113 == 0)

m.c153 = Constraint(expr=-m.x25*m.x84 + m.x114 == 0)

m.c154 = Constraint(expr=-m.x25*m.x85 + m.x115 == 0)

m.c155 = Constraint(expr=-m.x26*m.x86 + m.x116 == 0)

m.c156 = Constraint(expr=-m.x26*m.x87 + m.x117 == 0)

m.c157 = Constraint(expr=-m.x27*m.x86 + m.x118 == 0)

m.c158 = Constraint(expr=-m.x27*m.x87 + m.x119 == 0)

m.c159 = Constraint(expr=-m.x28*m.x86 + m.x120 == 0)

m.c160 = Constraint(expr=-m.x28*m.x87 + m.x121 == 0)

m.c161 = Constraint(expr=-m.x29*m.x86 + m.x122 == 0)

m.c162 = Constraint(expr=-m.x29*m.x87 + m.x123 == 0)

m.c163 = Constraint(expr=-m.x30*m.x88 + m.x124 == 0)

m.c164 = Constraint(expr=-m.x30*m.x89 + m.x125 == 0)

m.c165 = Constraint(expr=-m.x31*m.x88 + m.x126 == 0)

m.c166 = Constraint(expr=-m.x31*m.x89 + m.x127 == 0)

m.c167 = Constraint(expr=-m.x32*m.x88 + m.x128 == 0)

m.c168 = Constraint(expr=-m.x32*m.x89 + m.x129 == 0)

m.c169 = Constraint(expr=-m.x33*m.x88 + m.x130 == 0)

m.c170 = Constraint(expr=-m.x33*m.x89 + m.x131 == 0)

m.c171 = Constraint(expr=-m.x34*m.x90 + m.x132 == 0)

m.c172 = Constraint(expr=-m.x34*m.x91 + m.x133 == 0)

m.c173 = Constraint(expr=-m.x35*m.x90 + m.x134 == 0)

m.c174 = Constraint(expr=-m.x35*m.x91 + m.x135 == 0)

m.c175 = Constraint(expr=-m.x36*m.x90 + m.x136 == 0)

m.c176 = Constraint(expr=-m.x36*m.x91 + m.x137 == 0)

m.c177 = Constraint(expr=-m.x37*m.x90 + m.x138 == 0)

m.c178 = Constraint(expr=-m.x37*m.x91 + m.x139 == 0)

m.c179 = Constraint(expr=   1.2*m.x80 + m.x140 == 0)

m.c180 = Constraint(expr=   1.2*m.x81 + m.x141 == 0)

m.c181 = Constraint(expr=   0.6*m.x82 + m.x142 == 0)

m.c182 = Constraint(expr=   0.6*m.x83 + m.x143 == 0)

m.c183 = Constraint(expr=   0.8*m.x84 + m.x144 == 0)

m.c184 = Constraint(expr=   0.8*m.x85 + m.x145 == 0)

m.c185 = Constraint(expr=   1.7*m.x86 + m.x146 == 0)

m.c186 = Constraint(expr=   1.7*m.x87 + m.x147 == 0)

m.c187 = Constraint(expr=   1.3*m.x88 + m.x148 == 0)

m.c188 = Constraint(expr=   1.3*m.x89 + m.x149 == 0)

m.c189 = Constraint(expr=   0.5*m.x90 + m.x150 == 0)

m.c190 = Constraint(expr=   0.5*m.x91 + m.x151 == 0)

m.c191 = Constraint(expr=   m.x160 <= 4.5)

m.c192 = Constraint(expr=   m.x161 <= 2)
