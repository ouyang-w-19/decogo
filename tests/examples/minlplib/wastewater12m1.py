#  NLP written by GAMS Convert at 04/21/18 13:55:06
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         58       47        0       11        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        197      197        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        688      448      240        0
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

m.obj = Objective(expr=   m.x187 + m.x188 + m.x189 + m.x190 + m.x191 + m.x192 + m.x193 + m.x194 + m.x195 + m.x196
                       , sense=minimize)

m.c2 = Constraint(expr= - m.x121 - m.x136 - m.x137 - m.x138 - m.x139 - m.x140 - m.x141 - m.x142 - m.x143 - m.x144
                        - m.x145 == -90)

m.c3 = Constraint(expr= - m.x122 - m.x146 - m.x147 - m.x148 - m.x149 - m.x150 - m.x151 - m.x152 - m.x153 - m.x154
                        - m.x155 == -350)

m.c4 = Constraint(expr= - m.x123 - m.x156 - m.x157 - m.x158 - m.x159 - m.x160 - m.x161 - m.x162 - m.x163 - m.x164
                        - m.x165 == -200)

m.c5 = Constraint(expr= - m.x124 - m.x166 - m.x167 - m.x168 - m.x169 - m.x170 - m.x171 - m.x172 - m.x173 - m.x174
                        - m.x175 == -40)

m.c6 = Constraint(expr= - m.x125 - m.x176 - m.x177 - m.x178 - m.x179 - m.x180 - m.x181 - m.x182 - m.x183 - m.x184
                        - m.x185 == -130)

m.c7 = Constraint(expr= - m.x21 - m.x31 - m.x41 - m.x51 - m.x61 - m.x71 - m.x81 - m.x91 - m.x101 - m.x111 - m.x136
                        - m.x146 - m.x156 - m.x166 - m.x176 + m.x187 == 0)

m.c8 = Constraint(expr= - m.x22 - m.x32 - m.x42 - m.x52 - m.x62 - m.x72 - m.x82 - m.x92 - m.x102 - m.x112 - m.x137
                        - m.x147 - m.x157 - m.x167 - m.x177 + m.x188 == 0)

m.c9 = Constraint(expr= - m.x23 - m.x33 - m.x43 - m.x53 - m.x63 - m.x73 - m.x83 - m.x93 - m.x103 - m.x113 - m.x138
                        - m.x148 - m.x158 - m.x168 - m.x178 + m.x189 == 0)

m.c10 = Constraint(expr= - m.x24 - m.x34 - m.x44 - m.x54 - m.x64 - m.x74 - m.x84 - m.x94 - m.x104 - m.x114 - m.x139
                         - m.x149 - m.x159 - m.x169 - m.x179 + m.x190 == 0)

m.c11 = Constraint(expr= - m.x25 - m.x35 - m.x45 - m.x55 - m.x65 - m.x75 - m.x85 - m.x95 - m.x105 - m.x115 - m.x140
                         - m.x150 - m.x160 - m.x170 - m.x180 + m.x191 == 0)

m.c12 = Constraint(expr= - m.x26 - m.x36 - m.x46 - m.x56 - m.x66 - m.x76 - m.x86 - m.x96 - m.x106 - m.x116 - m.x141
                         - m.x151 - m.x161 - m.x171 - m.x181 + m.x192 == 0)

m.c13 = Constraint(expr= - m.x27 - m.x37 - m.x47 - m.x57 - m.x67 - m.x77 - m.x87 - m.x97 - m.x107 - m.x117 - m.x142
                         - m.x152 - m.x162 - m.x172 - m.x182 + m.x193 == 0)

m.c14 = Constraint(expr= - m.x28 - m.x38 - m.x48 - m.x58 - m.x68 - m.x78 - m.x88 - m.x98 - m.x108 - m.x118 - m.x143
                         - m.x153 - m.x163 - m.x173 - m.x183 + m.x194 == 0)

m.c15 = Constraint(expr= - m.x29 - m.x39 - m.x49 - m.x59 - m.x69 - m.x79 - m.x89 - m.x99 - m.x109 - m.x119 - m.x144
                         - m.x154 - m.x164 - m.x174 - m.x184 + m.x195 == 0)

m.c16 = Constraint(expr= - m.x30 - m.x40 - m.x50 - m.x60 - m.x70 - m.x80 - m.x90 - m.x100 - m.x110 - m.x120 - m.x145
                         - m.x155 - m.x165 - m.x175 - m.x185 + m.x196 == 0)

m.c17 = Constraint(expr= - m.x21 - m.x22 - m.x23 - m.x24 - m.x25 - m.x26 - m.x27 - m.x28 - m.x29 - m.x30 - m.x126
                         + m.x187 == 0)

m.c18 = Constraint(expr= - m.x31 - m.x32 - m.x33 - m.x34 - m.x35 - m.x36 - m.x37 - m.x38 - m.x39 - m.x40 - m.x127
                         + m.x188 == 0)

m.c19 = Constraint(expr= - m.x41 - m.x42 - m.x43 - m.x44 - m.x45 - m.x46 - m.x47 - m.x48 - m.x49 - m.x50 - m.x128
                         + m.x189 == 0)

m.c20 = Constraint(expr= - m.x51 - m.x52 - m.x53 - m.x54 - m.x55 - m.x56 - m.x57 - m.x58 - m.x59 - m.x60 - m.x129
                         + m.x190 == 0)

m.c21 = Constraint(expr= - m.x61 - m.x62 - m.x63 - m.x64 - m.x65 - m.x66 - m.x67 - m.x68 - m.x69 - m.x70 - m.x130
                         + m.x191 == 0)

m.c22 = Constraint(expr= - m.x71 - m.x72 - m.x73 - m.x74 - m.x75 - m.x76 - m.x77 - m.x78 - m.x79 - m.x80 - m.x131
                         + m.x192 == 0)

m.c23 = Constraint(expr= - m.x81 - m.x82 - m.x83 - m.x84 - m.x85 - m.x86 - m.x87 - m.x88 - m.x89 - m.x90 - m.x132
                         + m.x193 == 0)

m.c24 = Constraint(expr= - m.x91 - m.x92 - m.x93 - m.x94 - m.x95 - m.x96 - m.x97 - m.x98 - m.x99 - m.x100 - m.x133
                         + m.x194 == 0)

m.c25 = Constraint(expr= - m.x101 - m.x102 - m.x103 - m.x104 - m.x105 - m.x106 - m.x107 - m.x108 - m.x109 - m.x110
                         - m.x134 + m.x195 == 0)

m.c26 = Constraint(expr= - m.x111 - m.x112 - m.x113 - m.x114 - m.x115 - m.x116 - m.x117 - m.x118 - m.x119 - m.x120
                         - m.x135 + m.x196 == 0)

m.c27 = Constraint(expr= - m.x121 - m.x122 - m.x123 - m.x124 - m.x125 - m.x126 - m.x127 - m.x128 - m.x129 - m.x130
                         - m.x131 - m.x132 - m.x133 - m.x134 - m.x135 + m.x186 == 0)

m.c28 = Constraint(expr=m.x21*m.x11 + m.x31*m.x12 + m.x41*m.x13 + m.x51*m.x14 + m.x61*m.x15 + m.x71*m.x16 + m.x81*m.x17
                         + m.x91*m.x18 + m.x101*m.x19 + m.x111*m.x20 - m.x187*m.x1 + 330*m.x136 + 50*m.x146 + 150*m.x156
                         + 240*m.x166 + 120*m.x176 == 0)

m.c29 = Constraint(expr=m.x22*m.x11 + m.x32*m.x12 + m.x42*m.x13 + m.x52*m.x14 + m.x62*m.x15 + m.x72*m.x16 + m.x82*m.x17
                         + m.x92*m.x18 + m.x102*m.x19 + m.x112*m.x20 - m.x188*m.x2 + 330*m.x137 + 50*m.x147 + 150*m.x157
                         + 240*m.x167 + 120*m.x177 == 0)

m.c30 = Constraint(expr=m.x23*m.x11 + m.x33*m.x12 + m.x43*m.x13 + m.x53*m.x14 + m.x63*m.x15 + m.x73*m.x16 + m.x83*m.x17
                         + m.x93*m.x18 + m.x103*m.x19 + m.x113*m.x20 - m.x189*m.x3 + 330*m.x138 + 50*m.x148 + 150*m.x158
                         + 240*m.x168 + 120*m.x178 == 0)

m.c31 = Constraint(expr=m.x24*m.x11 + m.x34*m.x12 + m.x44*m.x13 + m.x54*m.x14 + m.x64*m.x15 + m.x74*m.x16 + m.x84*m.x17
                         + m.x94*m.x18 + m.x104*m.x19 + m.x114*m.x20 - m.x190*m.x4 + 330*m.x139 + 50*m.x149 + 150*m.x159
                         + 240*m.x169 + 120*m.x179 == 0)

m.c32 = Constraint(expr=m.x25*m.x11 + m.x35*m.x12 + m.x45*m.x13 + m.x55*m.x14 + m.x65*m.x15 + m.x75*m.x16 + m.x85*m.x17
                         + m.x95*m.x18 + m.x105*m.x19 + m.x115*m.x20 - m.x191*m.x5 + 330*m.x140 + 50*m.x150 + 150*m.x160
                         + 240*m.x170 + 120*m.x180 == 0)

m.c33 = Constraint(expr=m.x26*m.x11 + m.x36*m.x12 + m.x46*m.x13 + m.x56*m.x14 + m.x66*m.x15 + m.x76*m.x16 + m.x86*m.x17
                         + m.x96*m.x18 + m.x106*m.x19 + m.x116*m.x20 - m.x192*m.x6 + 330*m.x141 + 50*m.x151 + 150*m.x161
                         + 240*m.x171 + 120*m.x181 == 0)

m.c34 = Constraint(expr=m.x27*m.x11 + m.x37*m.x12 + m.x47*m.x13 + m.x57*m.x14 + m.x67*m.x15 + m.x77*m.x16 + m.x87*m.x17
                         + m.x97*m.x18 + m.x107*m.x19 + m.x117*m.x20 - m.x193*m.x7 + 330*m.x142 + 50*m.x152 + 150*m.x162
                         + 240*m.x172 + 120*m.x182 == 0)

m.c35 = Constraint(expr=m.x28*m.x11 + m.x38*m.x12 + m.x48*m.x13 + m.x58*m.x14 + m.x68*m.x15 + m.x78*m.x16 + m.x88*m.x17
                         + m.x98*m.x18 + m.x108*m.x19 + m.x118*m.x20 - m.x194*m.x8 + 330*m.x143 + 50*m.x153 + 150*m.x163
                         + 240*m.x173 + 120*m.x183 == 0)

m.c36 = Constraint(expr=m.x29*m.x11 + m.x39*m.x12 + m.x49*m.x13 + m.x59*m.x14 + m.x69*m.x15 + m.x79*m.x16 + m.x89*m.x17
                         + m.x99*m.x18 + m.x109*m.x19 + m.x119*m.x20 - m.x195*m.x9 + 330*m.x144 + 50*m.x154 + 150*m.x164
                         + 240*m.x174 + 120*m.x184 == 0)

m.c37 = Constraint(expr=m.x30*m.x11 + m.x40*m.x12 + m.x50*m.x13 + m.x60*m.x14 + m.x70*m.x15 + m.x80*m.x16 + m.x90*m.x17
                         + m.x100*m.x18 + m.x110*m.x19 + m.x120*m.x20 - m.x196*m.x10 + 330*m.x145 + 50*m.x155
                         + 150*m.x165 + 240*m.x175 + 120*m.x185 == 0)

m.c38 = Constraint(expr=   m.x1 <= 30)

m.c39 = Constraint(expr=   m.x2 <= 100)

m.c40 = Constraint(expr=   m.x3 <= 50)

m.c41 = Constraint(expr=   m.x4 <= 227)

m.c42 = Constraint(expr=   m.x5 <= 100)

m.c43 = Constraint(expr=   m.x6 <= 300)

m.c44 = Constraint(expr=   m.x7 <= 12)

m.c45 = Constraint(expr=   m.x8 <= 970)

m.c46 = Constraint(expr=   m.x9 <= 20)

m.c47 = Constraint(expr=   m.x10 <= 250)

m.c48 = Constraint(expr= - 0.05*m.x1 + m.x11 == 0)

m.c49 = Constraint(expr= - 0.2*m.x2 + m.x12 == 0)

m.c50 = Constraint(expr= - 0.15*m.x3 + m.x13 == 0)

m.c51 = Constraint(expr= - 0.88*m.x4 + m.x14 == 0)

m.c52 = Constraint(expr= - 0.7*m.x5 + m.x15 == 0)

m.c53 = Constraint(expr= - 0.4*m.x6 + m.x16 == 0)

m.c54 = Constraint(expr= - 0.33*m.x7 + m.x17 == 0)

m.c55 = Constraint(expr= - 0.3*m.x8 + m.x18 == 0)

m.c56 = Constraint(expr= - 0.4*m.x9 + m.x19 == 0)

m.c57 = Constraint(expr= - 0.3*m.x10 + m.x20 == 0)

m.c58 = Constraint(expr=m.x126*m.x11 + m.x127*m.x12 + m.x128*m.x13 + m.x129*m.x14 + m.x130*m.x15 + m.x131*m.x16 + m.x132
                        *m.x17 + m.x133*m.x18 + m.x134*m.x19 + m.x135*m.x20 + 330*m.x121 + 50*m.x122 + 150*m.x123
                         + 240*m.x124 + 120*m.x125 - 10*m.x186 <= 0)
