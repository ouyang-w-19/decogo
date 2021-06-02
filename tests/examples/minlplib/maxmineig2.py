#  NLP written by GAMS Convert at 04/21/18 13:52:30
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        112      112        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        201      201        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1403      815      588        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x2 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x3 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x4 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x5 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x6 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x7 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x8 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x9 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x10 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x11 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x12 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x13 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x14 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x15 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x16 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x17 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x18 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x19 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x20 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x21 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x22 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x23 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x24 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x25 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x26 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x27 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x28 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x29 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x30 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x31 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x32 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x33 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x34 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x35 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x36 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x37 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x38 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x39 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x40 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x41 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x42 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x43 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x44 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x45 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x46 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x47 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x48 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x49 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x50 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x51 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x52 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x53 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x54 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x55 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x56 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x57 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x58 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x59 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x60 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x61 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x62 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x63 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x64 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x65 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x66 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x67 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x68 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x69 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x70 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x71 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x72 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x73 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x74 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x75 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x76 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x77 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x78 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x79 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x80 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x81 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x82 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x83 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x84 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x85 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x86 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x87 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x88 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x89 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x90 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x91 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x92 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x93 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x94 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x95 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x96 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x97 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x98 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x99 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x100 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)
m.x101 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x102 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x103 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x104 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x105 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x106 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x107 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x108 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x109 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x110 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x111 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x113 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x114 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x115 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x116 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x117 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x118 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x119 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x120 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x121 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x123 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x124 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x125 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x126 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x127 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x128 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x129 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x130 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x131 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x132 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x133 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x134 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x135 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x136 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x137 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x138 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x139 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x140 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x141 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x142 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x143 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x144 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x145 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x146 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x147 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x148 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x149 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x150 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x151 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x152 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x153 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x154 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x155 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x156 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x157 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x158 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x159 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x160 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x161 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x162 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x163 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x164 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x165 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x166 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x167 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x168 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x169 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x170 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x171 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x172 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x173 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x174 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x175 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x176 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x177 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x178 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x179 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x180 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x181 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x182 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x183 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x184 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x185 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x186 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x187 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x188 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x189 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x190 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x191 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x192 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x193 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x194 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x195 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x196 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x197 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x198 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x199 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x200 = Var(within=Reals,bounds=(None,None),initialize=1)

m.obj = Objective(expr=   1.08828*m.x102 + 1.05718*m.x103 + 0.228192*m.x104 - 1.30634*m.x105 - 0.65168*m.x106
                        - 1.260084*m.x107 - 0.469946*m.x108 - 0.34633*m.x109 + 2.809918*m.x110 + 3.586448*m.x112
                        + 0.972156*m.x113 - 1.285152*m.x114 + 3.645282*m.x115 + 0.38707*m.x116 + 1.048474*m.x117
                        + 0.627214*m.x118 + 3.746396*m.x119 - 4.027804*m.x120 + 3.29591*m.x123 + 4.485358*m.x124
                        - 1.217538*m.x125 + 0.095654*m.x126 + 0.943638*m.x127 - 0.621584*m.x128 - 1.716882*m.x129
                        - 2.250502*m.x130 + 1.323736*m.x134 + 2.264256*m.x135 + 0.875896*m.x136 + 1.144872*m.x137
                        - 0.163352*m.x138 + 0.966758*m.x139 + 3.761826*m.x140 + 1.477326*m.x145 + 1.132984*m.x146
                        - 1.461894*m.x147 + 5.21283*m.x148 - 3.950838*m.x149 + 1.46395*m.x150 + 4.341016*m.x156
                        - 1.031632*m.x157 - 1.94693*m.x158 + 1.343486*m.x159 + 1.343322*m.x160 + 4.430323*m.x167
                        + 0.825328*m.x168 + 0.150462*m.x169 + 0.956186*m.x170 + 0.964514*m.x178 - 0.61663*m.x179
                        + 4.296174*m.x180 + 2.642236*m.x189 + 3.406506*m.x190 + 0.266262*m.x200, sense=minimize)

m.c1 = Constraint(expr= - 0.1*m.x101 + 2*m.x102 + 2*m.x103 + 2*m.x104 + 2*m.x105 + 2*m.x106 + 2*m.x107 + 2*m.x108
                        + 2*m.x109 + 2*m.x110 - 0.1*m.x112 + 2*m.x113 + 2*m.x114 + 2*m.x115 + 2*m.x116 + 2*m.x117
                        + 2*m.x118 + 2*m.x119 + 2*m.x120 - 0.1*m.x123 + 2*m.x124 + 2*m.x125 + 2*m.x126 + 2*m.x127
                        + 2*m.x128 + 2*m.x129 + 2*m.x130 - 0.1*m.x134 + 2*m.x135 + 2*m.x136 + 2*m.x137 + 2*m.x138
                        + 2*m.x139 + 2*m.x140 - 0.1*m.x145 + 2*m.x146 + 2*m.x147 + 2*m.x148 + 2*m.x149 + 2*m.x150
                        - 0.1*m.x156 + 2*m.x157 + 2*m.x158 + 2*m.x159 + 2*m.x160 - 0.1*m.x167 + 2*m.x168 + 2*m.x169
                        + 2*m.x170 - 0.1*m.x178 + 2*m.x179 + 2*m.x180 - 0.1*m.x189 + 2*m.x190 - 0.1*m.x200 == 0)

m.c2 = Constraint(expr= - 0.1*m.x101 + 2*m.x102 + 2*m.x103 + 2*m.x104 + 2*m.x105 + 2*m.x106 + 2*m.x107 + 2*m.x108
                        + 2*m.x109 + 2*m.x110 - 0.1*m.x112 + 2*m.x113 + 2*m.x114 + 2*m.x115 + 2*m.x116 + 2*m.x117
                        + 2*m.x118 + 2*m.x119 + 2*m.x120 - 0.1*m.x123 + 2*m.x124 + 2*m.x125 + 2*m.x126 + 2*m.x127
                        + 2*m.x128 + 2*m.x129 + 2*m.x130 - 0.1*m.x134 + 2*m.x135 + 2*m.x136 + 2*m.x137 + 2*m.x138
                        + 2*m.x139 + 2*m.x140 - 0.1*m.x145 + 2*m.x146 + 2*m.x147 + 2*m.x148 + 2*m.x149 + 2*m.x150
                        - 0.1*m.x156 + 2*m.x157 + 2*m.x158 + 2*m.x159 + 2*m.x160 - 0.1*m.x167 + 2*m.x168 + 2*m.x169
                        + 2*m.x170 - 0.1*m.x178 + 2*m.x179 + 2*m.x180 - 0.1*m.x189 + 2*m.x190 - 0.1*m.x200 == 0)

m.c3 = Constraint(expr= - 0.1*m.x101 + 2*m.x102 + 2*m.x103 + 2*m.x104 + 2*m.x105 + 2*m.x106 + 2*m.x107 + 2*m.x108
                        + 2*m.x109 + 2*m.x110 - 0.1*m.x112 + 2*m.x113 + 2*m.x114 + 2*m.x115 + 2*m.x116 + 2*m.x117
                        + 2*m.x118 + 2*m.x119 + 2*m.x120 - 0.1*m.x123 + 2*m.x124 + 2*m.x125 + 2*m.x126 + 2*m.x127
                        + 2*m.x128 + 2*m.x129 + 2*m.x130 - 0.1*m.x134 + 2*m.x135 + 2*m.x136 + 2*m.x137 + 2*m.x138
                        + 2*m.x139 + 2*m.x140 - 0.1*m.x145 + 2*m.x146 + 2*m.x147 + 2*m.x148 + 2*m.x149 + 2*m.x150
                        - 0.1*m.x156 + 2*m.x157 + 2*m.x158 + 2*m.x159 + 2*m.x160 - 0.1*m.x167 + 2*m.x168 + 2*m.x169
                        + 2*m.x170 - 0.1*m.x178 + 2*m.x179 + 2*m.x180 - 0.1*m.x189 + 2*m.x190 - 0.1*m.x200 == 0)

m.c4 = Constraint(expr= - 0.1*m.x101 + 2*m.x102 + 2*m.x103 + 2*m.x104 + 2*m.x105 + 2*m.x106 + 2*m.x107 + 2*m.x108
                        + 2*m.x109 + 2*m.x110 - 0.1*m.x112 + 2*m.x113 + 2*m.x114 + 2*m.x115 + 2*m.x116 + 2*m.x117
                        + 2*m.x118 + 2*m.x119 + 2*m.x120 - 0.1*m.x123 + 2*m.x124 + 2*m.x125 + 2*m.x126 + 2*m.x127
                        + 2*m.x128 + 2*m.x129 + 2*m.x130 - 0.1*m.x134 + 2*m.x135 + 2*m.x136 + 2*m.x137 + 2*m.x138
                        + 2*m.x139 + 2*m.x140 - 0.1*m.x145 + 2*m.x146 + 2*m.x147 + 2*m.x148 + 2*m.x149 + 2*m.x150
                        - 0.1*m.x156 + 2*m.x157 + 2*m.x158 + 2*m.x159 + 2*m.x160 - 0.1*m.x167 + 2*m.x168 + 2*m.x169
                        + 2*m.x170 - 0.1*m.x178 + 2*m.x179 + 2*m.x180 - 0.1*m.x189 + 2*m.x190 - 0.1*m.x200 == 0)

m.c5 = Constraint(expr= - 0.1*m.x101 + 2*m.x102 + 2*m.x103 + 2*m.x104 + 2*m.x105 + 2*m.x106 + 2*m.x107 + 2*m.x108
                        + 2*m.x109 + 2*m.x110 - 0.1*m.x112 + 2*m.x113 + 2*m.x114 + 2*m.x115 + 2*m.x116 + 2*m.x117
                        + 2*m.x118 + 2*m.x119 + 2*m.x120 - 0.1*m.x123 + 2*m.x124 + 2*m.x125 + 2*m.x126 + 2*m.x127
                        + 2*m.x128 + 2*m.x129 + 2*m.x130 - 0.1*m.x134 + 2*m.x135 + 2*m.x136 + 2*m.x137 + 2*m.x138
                        + 2*m.x139 + 2*m.x140 - 0.1*m.x145 + 2*m.x146 + 2*m.x147 + 2*m.x148 + 2*m.x149 + 2*m.x150
                        - 0.1*m.x156 + 2*m.x157 + 2*m.x158 + 2*m.x159 + 2*m.x160 - 0.1*m.x167 + 2*m.x168 + 2*m.x169
                        + 2*m.x170 - 0.1*m.x178 + 2*m.x179 + 2*m.x180 - 0.1*m.x189 + 2*m.x190 - 0.1*m.x200 == 0)

m.c6 = Constraint(expr= - 0.1*m.x101 + 2*m.x102 + 2*m.x103 + 2*m.x104 + 2*m.x105 + 2*m.x106 + 2*m.x107 + 2*m.x108
                        + 2*m.x109 + 2*m.x110 - 0.1*m.x112 + 2*m.x113 + 2*m.x114 + 2*m.x115 + 2*m.x116 + 2*m.x117
                        + 2*m.x118 + 2*m.x119 + 2*m.x120 - 0.1*m.x123 + 2*m.x124 + 2*m.x125 + 2*m.x126 + 2*m.x127
                        + 2*m.x128 + 2*m.x129 + 2*m.x130 - 0.1*m.x134 + 2*m.x135 + 2*m.x136 + 2*m.x137 + 2*m.x138
                        + 2*m.x139 + 2*m.x140 - 0.1*m.x145 + 2*m.x146 + 2*m.x147 + 2*m.x148 + 2*m.x149 + 2*m.x150
                        - 0.1*m.x156 + 2*m.x157 + 2*m.x158 + 2*m.x159 + 2*m.x160 - 0.1*m.x167 + 2*m.x168 + 2*m.x169
                        + 2*m.x170 - 0.1*m.x178 + 2*m.x179 + 2*m.x180 - 0.1*m.x189 + 2*m.x190 - 0.1*m.x200 == 0)

m.c7 = Constraint(expr= - 0.1*m.x101 + 2*m.x102 + 2*m.x103 + 2*m.x104 + 2*m.x105 + 2*m.x106 + 2*m.x107 + 2*m.x108
                        + 2*m.x109 + 2*m.x110 - 0.1*m.x112 + 2*m.x113 + 2*m.x114 + 2*m.x115 + 2*m.x116 + 2*m.x117
                        + 2*m.x118 + 2*m.x119 + 2*m.x120 - 0.1*m.x123 + 2*m.x124 + 2*m.x125 + 2*m.x126 + 2*m.x127
                        + 2*m.x128 + 2*m.x129 + 2*m.x130 - 0.1*m.x134 + 2*m.x135 + 2*m.x136 + 2*m.x137 + 2*m.x138
                        + 2*m.x139 + 2*m.x140 - 0.1*m.x145 + 2*m.x146 + 2*m.x147 + 2*m.x148 + 2*m.x149 + 2*m.x150
                        - 0.1*m.x156 + 2*m.x157 + 2*m.x158 + 2*m.x159 + 2*m.x160 - 0.1*m.x167 + 2*m.x168 + 2*m.x169
                        + 2*m.x170 - 0.1*m.x178 + 2*m.x179 + 2*m.x180 - 0.1*m.x189 + 2*m.x190 - 0.1*m.x200 == 0)

m.c8 = Constraint(expr= - 0.1*m.x101 + 2*m.x102 + 2*m.x103 + 2*m.x104 + 2*m.x105 + 2*m.x106 + 2*m.x107 + 2*m.x108
                        + 2*m.x109 + 2*m.x110 - 0.1*m.x112 + 2*m.x113 + 2*m.x114 + 2*m.x115 + 2*m.x116 + 2*m.x117
                        + 2*m.x118 + 2*m.x119 + 2*m.x120 - 0.1*m.x123 + 2*m.x124 + 2*m.x125 + 2*m.x126 + 2*m.x127
                        + 2*m.x128 + 2*m.x129 + 2*m.x130 - 0.1*m.x134 + 2*m.x135 + 2*m.x136 + 2*m.x137 + 2*m.x138
                        + 2*m.x139 + 2*m.x140 - 0.1*m.x145 + 2*m.x146 + 2*m.x147 + 2*m.x148 + 2*m.x149 + 2*m.x150
                        - 0.1*m.x156 + 2*m.x157 + 2*m.x158 + 2*m.x159 + 2*m.x160 - 0.1*m.x167 + 2*m.x168 + 2*m.x169
                        + 2*m.x170 - 0.1*m.x178 + 2*m.x179 + 2*m.x180 - 0.1*m.x189 + 2*m.x190 - 0.1*m.x200 == 0)

m.c9 = Constraint(expr= - 0.1*m.x101 + 2*m.x102 + 2*m.x103 + 2*m.x104 + 2*m.x105 + 2*m.x106 + 2*m.x107 + 2*m.x108
                        + 2*m.x109 + 2*m.x110 - 0.1*m.x112 + 2*m.x113 + 2*m.x114 + 2*m.x115 + 2*m.x116 + 2*m.x117
                        + 2*m.x118 + 2*m.x119 + 2*m.x120 - 0.1*m.x123 + 2*m.x124 + 2*m.x125 + 2*m.x126 + 2*m.x127
                        + 2*m.x128 + 2*m.x129 + 2*m.x130 - 0.1*m.x134 + 2*m.x135 + 2*m.x136 + 2*m.x137 + 2*m.x138
                        + 2*m.x139 + 2*m.x140 - 0.1*m.x145 + 2*m.x146 + 2*m.x147 + 2*m.x148 + 2*m.x149 + 2*m.x150
                        - 0.1*m.x156 + 2*m.x157 + 2*m.x158 + 2*m.x159 + 2*m.x160 - 0.1*m.x167 + 2*m.x168 + 2*m.x169
                        + 2*m.x170 - 0.1*m.x178 + 2*m.x179 + 2*m.x180 - 0.1*m.x189 + 2*m.x190 + 0.9*m.x200 == 0)

m.c10 = Constraint(expr=   m.x101 + 2*m.x102 + 2*m.x103 + 2*m.x104 + 2*m.x105 + 2*m.x106 + 2*m.x107 + 2*m.x108
                         + 2*m.x109 + 2*m.x110 + m.x112 + 2*m.x113 + 2*m.x114 + 2*m.x115 + 2*m.x116 + 2*m.x117
                         + 2*m.x118 + 2*m.x119 + 2*m.x120 + m.x123 + 2*m.x124 + 2*m.x125 + 2*m.x126 + 2*m.x127
                         + 2*m.x128 + 2*m.x129 + 2*m.x130 + m.x134 + 2*m.x135 + 2*m.x136 + 2*m.x137 + 2*m.x138
                         + 2*m.x139 + 2*m.x140 + m.x145 + 2*m.x146 + 2*m.x147 + 2*m.x148 + 2*m.x149 + 2*m.x150 + m.x156
                         + 2*m.x157 + 2*m.x158 + 2*m.x159 + 2*m.x160 + m.x167 + 2*m.x168 + 2*m.x169 + 2*m.x170 + m.x178
                         + 2*m.x179 + 2*m.x180 + m.x189 + 2*m.x190 + m.x200 == 1)

m.c11 = Constraint(expr=   m.x1 - m.x101 == 0)

m.c12 = Constraint(expr=   m.x2 - m.x111 == 0)

m.c13 = Constraint(expr=m.x56*m.x2 + m.x3 - m.x112 == 0)

m.c14 = Constraint(expr=   m.x4 - m.x121 == 0)

m.c15 = Constraint(expr=m.x56*m.x4 + m.x5 - m.x122 == 0)

m.c16 = Constraint(expr=m.x57*m.x4 + m.x5*m.x65 + m.x6 - m.x123 == 0)

m.c17 = Constraint(expr=   m.x7 - m.x131 == 0)

m.c18 = Constraint(expr=m.x56*m.x7 + m.x8 - m.x132 == 0)

m.c19 = Constraint(expr=m.x57*m.x7 + m.x65*m.x8 + m.x9 - m.x133 == 0)

m.c20 = Constraint(expr=m.x58*m.x7 + m.x8*m.x66 + m.x9*m.x73 + m.x10 - m.x134 == 0)

m.c21 = Constraint(expr=   m.x11 - m.x141 == 0)

m.c22 = Constraint(expr=m.x56*m.x11 + m.x12 - m.x142 == 0)

m.c23 = Constraint(expr=m.x57*m.x11 + m.x65*m.x12 + m.x13 - m.x143 == 0)

m.c24 = Constraint(expr=m.x58*m.x11 + m.x66*m.x12 + m.x73*m.x13 + m.x14 - m.x144 == 0)

m.c25 = Constraint(expr=m.x59*m.x11 + m.x12*m.x67 + m.x13*m.x74 + m.x14*m.x80 + m.x15 - m.x145 == 0)

m.c26 = Constraint(expr=   m.x16 - m.x151 == 0)

m.c27 = Constraint(expr=m.x56*m.x16 + m.x17 - m.x152 == 0)

m.c28 = Constraint(expr=m.x57*m.x16 + m.x65*m.x17 + m.x18 - m.x153 == 0)

m.c29 = Constraint(expr=m.x58*m.x16 + m.x66*m.x17 + m.x73*m.x18 + m.x19 - m.x154 == 0)

m.c30 = Constraint(expr=m.x59*m.x16 + m.x67*m.x17 + m.x74*m.x18 + m.x80*m.x19 + m.x20 - m.x155 == 0)

m.c31 = Constraint(expr=m.x60*m.x16 + m.x17*m.x68 + m.x18*m.x75 + m.x19*m.x81 + m.x20*m.x86 + m.x21 - m.x156 == 0)

m.c32 = Constraint(expr=   m.x22 - m.x161 == 0)

m.c33 = Constraint(expr=m.x56*m.x22 + m.x23 - m.x162 == 0)

m.c34 = Constraint(expr=m.x57*m.x22 + m.x65*m.x23 + m.x24 - m.x163 == 0)

m.c35 = Constraint(expr=m.x58*m.x22 + m.x66*m.x23 + m.x73*m.x24 + m.x25 - m.x164 == 0)

m.c36 = Constraint(expr=m.x59*m.x22 + m.x67*m.x23 + m.x74*m.x24 + m.x80*m.x25 + m.x26 - m.x165 == 0)

m.c37 = Constraint(expr=m.x60*m.x22 + m.x68*m.x23 + m.x75*m.x24 + m.x81*m.x25 + m.x86*m.x26 + m.x27 - m.x166 == 0)

m.c38 = Constraint(expr=m.x61*m.x22 + m.x23*m.x69 + m.x24*m.x76 + m.x25*m.x82 + m.x26*m.x87 + m.x27*m.x91 + m.x28
                         - m.x167 == 0)

m.c39 = Constraint(expr=   m.x29 - m.x171 == 0)

m.c40 = Constraint(expr=m.x56*m.x29 + m.x30 - m.x172 == 0)

m.c41 = Constraint(expr=m.x57*m.x29 + m.x65*m.x30 + m.x31 - m.x173 == 0)

m.c42 = Constraint(expr=m.x58*m.x29 + m.x66*m.x30 + m.x73*m.x31 + m.x32 - m.x174 == 0)

m.c43 = Constraint(expr=m.x59*m.x29 + m.x67*m.x30 + m.x74*m.x31 + m.x80*m.x32 + m.x33 - m.x175 == 0)

m.c44 = Constraint(expr=m.x60*m.x29 + m.x68*m.x30 + m.x75*m.x31 + m.x81*m.x32 + m.x86*m.x33 + m.x34 - m.x176 == 0)

m.c45 = Constraint(expr=m.x61*m.x29 + m.x91*m.x34 + m.x69*m.x30 + m.x76*m.x31 + m.x82*m.x32 + m.x87*m.x33 + m.x35
                         - m.x177 == 0)

m.c46 = Constraint(expr=m.x62*m.x29 + m.x30*m.x70 + m.x31*m.x77 + m.x32*m.x83 + m.x33*m.x88 + m.x34*m.x92 + m.x35*m.x95
                         + m.x36 - m.x178 == 0)

m.c47 = Constraint(expr=   m.x37 - m.x181 == 0)

m.c48 = Constraint(expr=m.x56*m.x37 + m.x38 - m.x182 == 0)

m.c49 = Constraint(expr=m.x57*m.x37 + m.x65*m.x38 + m.x39 - m.x183 == 0)

m.c50 = Constraint(expr=m.x58*m.x37 + m.x66*m.x38 + m.x73*m.x39 + m.x40 - m.x184 == 0)

m.c51 = Constraint(expr=m.x59*m.x37 + m.x67*m.x38 + m.x74*m.x39 + m.x80*m.x40 + m.x41 - m.x185 == 0)

m.c52 = Constraint(expr=m.x60*m.x37 + m.x68*m.x38 + m.x75*m.x39 + m.x81*m.x40 + m.x86*m.x41 + m.x42 - m.x186 == 0)

m.c53 = Constraint(expr=m.x61*m.x37 + m.x91*m.x42 + m.x69*m.x38 + m.x76*m.x39 + m.x82*m.x40 + m.x87*m.x41 + m.x43
                         - m.x187 == 0)

m.c54 = Constraint(expr=m.x62*m.x37 + m.x92*m.x42 + m.x70*m.x38 + m.x77*m.x39 + m.x95*m.x43 + m.x83*m.x40 + m.x88*m.x41
                         + m.x44 - m.x188 == 0)

m.c55 = Constraint(expr=m.x63*m.x37 + m.x38*m.x71 + m.x39*m.x78 + m.x40*m.x84 + m.x41*m.x89 + m.x42*m.x93 + m.x43*m.x96
                         + m.x44*m.x98 + m.x45 - m.x189 == 0)

m.c56 = Constraint(expr=   m.x46 - m.x191 == 0)

m.c57 = Constraint(expr=m.x56*m.x46 + m.x47 - m.x192 == 0)

m.c58 = Constraint(expr=m.x57*m.x46 + m.x65*m.x47 + m.x48 - m.x193 == 0)

m.c59 = Constraint(expr=m.x58*m.x46 + m.x66*m.x47 + m.x73*m.x48 + m.x49 - m.x194 == 0)

m.c60 = Constraint(expr=m.x59*m.x46 + m.x67*m.x47 + m.x74*m.x48 + m.x80*m.x49 + m.x50 - m.x195 == 0)

m.c61 = Constraint(expr=m.x60*m.x46 + m.x68*m.x47 + m.x75*m.x48 + m.x81*m.x49 + m.x86*m.x50 + m.x51 - m.x196 == 0)

m.c62 = Constraint(expr=m.x61*m.x46 + m.x91*m.x51 + m.x69*m.x47 + m.x76*m.x48 + m.x82*m.x49 + m.x87*m.x50 + m.x52
                         - m.x197 == 0)

m.c63 = Constraint(expr=m.x62*m.x46 + m.x92*m.x51 + m.x70*m.x47 + m.x77*m.x48 + m.x95*m.x52 + m.x83*m.x49 + m.x88*m.x50
                         + m.x53 - m.x198 == 0)

m.c64 = Constraint(expr=m.x63*m.x46 + m.x93*m.x51 + m.x71*m.x47 + m.x78*m.x48 + m.x96*m.x52 + m.x84*m.x49 + m.x98*m.x53
                         + m.x89*m.x50 + m.x54 - m.x199 == 0)

m.c65 = Constraint(expr=m.x64*m.x46 + m.x47*m.x72 + m.x48*m.x79 + m.x49*m.x85 + m.x50*m.x90 + m.x51*m.x94 + m.x52*m.x97
                         + m.x53*m.x99 + m.x54*m.x100 + m.x55 - m.x200 == 0)

m.c66 = Constraint(expr=m.x1*m.x56 - m.x102 == 0)

m.c67 = Constraint(expr=m.x1*m.x57 - m.x103 == 0)

m.c68 = Constraint(expr=m.x1*m.x58 - m.x104 == 0)

m.c69 = Constraint(expr=m.x1*m.x59 - m.x105 == 0)

m.c70 = Constraint(expr=m.x1*m.x60 - m.x106 == 0)

m.c71 = Constraint(expr=m.x1*m.x61 - m.x107 == 0)

m.c72 = Constraint(expr=m.x1*m.x62 - m.x108 == 0)

m.c73 = Constraint(expr=m.x1*m.x63 - m.x109 == 0)

m.c74 = Constraint(expr=m.x1*m.x64 - m.x110 == 0)

m.c75 = Constraint(expr=m.x3*m.x65 - m.x113 == 0)

m.c76 = Constraint(expr=m.x3*m.x66 - m.x114 == 0)

m.c77 = Constraint(expr=m.x3*m.x67 - m.x115 == 0)

m.c78 = Constraint(expr=m.x3*m.x68 - m.x116 == 0)

m.c79 = Constraint(expr=m.x3*m.x69 - m.x117 == 0)

m.c80 = Constraint(expr=m.x3*m.x70 - m.x118 == 0)

m.c81 = Constraint(expr=m.x3*m.x71 - m.x119 == 0)

m.c82 = Constraint(expr=m.x3*m.x72 - m.x120 == 0)

m.c83 = Constraint(expr=m.x4*m.x58 + m.x6*m.x73 - m.x124 == 0)

m.c84 = Constraint(expr=m.x4*m.x59 + m.x6*m.x74 - m.x125 == 0)

m.c85 = Constraint(expr=m.x4*m.x60 + m.x6*m.x75 - m.x126 == 0)

m.c86 = Constraint(expr=m.x4*m.x61 + m.x6*m.x76 - m.x127 == 0)

m.c87 = Constraint(expr=m.x4*m.x62 + m.x6*m.x77 - m.x128 == 0)

m.c88 = Constraint(expr=m.x4*m.x63 + m.x6*m.x78 - m.x129 == 0)

m.c89 = Constraint(expr=m.x4*m.x64 + m.x6*m.x79 - m.x130 == 0)

m.c90 = Constraint(expr=m.x7*m.x59 + m.x8*m.x67 + m.x10*m.x80 - m.x135 == 0)

m.c91 = Constraint(expr=m.x7*m.x60 + m.x8*m.x68 + m.x10*m.x81 - m.x136 == 0)

m.c92 = Constraint(expr=m.x7*m.x61 + m.x8*m.x69 + m.x10*m.x82 - m.x137 == 0)

m.c93 = Constraint(expr=m.x7*m.x62 + m.x8*m.x70 + m.x10*m.x83 - m.x138 == 0)

m.c94 = Constraint(expr=m.x7*m.x63 + m.x8*m.x71 + m.x10*m.x84 - m.x139 == 0)

m.c95 = Constraint(expr=m.x7*m.x64 + m.x8*m.x72 + m.x10*m.x85 - m.x140 == 0)

m.c96 = Constraint(expr=m.x11*m.x60 + m.x12*m.x68 + m.x13*m.x75 + m.x15*m.x86 - m.x146 == 0)

m.c97 = Constraint(expr=m.x11*m.x61 + m.x12*m.x69 + m.x13*m.x76 + m.x15*m.x87 - m.x147 == 0)

m.c98 = Constraint(expr=m.x11*m.x62 + m.x12*m.x70 + m.x13*m.x77 + m.x15*m.x88 - m.x148 == 0)

m.c99 = Constraint(expr=m.x11*m.x63 + m.x12*m.x71 + m.x13*m.x78 + m.x15*m.x89 - m.x149 == 0)

m.c100 = Constraint(expr=m.x11*m.x64 + m.x12*m.x72 + m.x13*m.x79 + m.x15*m.x90 - m.x150 == 0)

m.c101 = Constraint(expr=m.x16*m.x61 + m.x17*m.x69 + m.x18*m.x76 + m.x19*m.x82 + m.x21*m.x91 - m.x157 == 0)

m.c102 = Constraint(expr=m.x16*m.x62 + m.x17*m.x70 + m.x18*m.x77 + m.x19*m.x83 + m.x21*m.x92 - m.x158 == 0)

m.c103 = Constraint(expr=m.x16*m.x63 + m.x17*m.x71 + m.x18*m.x78 + m.x19*m.x84 + m.x21*m.x93 - m.x159 == 0)

m.c104 = Constraint(expr=m.x16*m.x64 + m.x17*m.x72 + m.x18*m.x79 + m.x19*m.x85 + m.x21*m.x94 - m.x160 == 0)

m.c105 = Constraint(expr=m.x22*m.x62 + m.x23*m.x70 + m.x24*m.x77 + m.x25*m.x83 + m.x26*m.x88 + m.x28*m.x95 - m.x168
                          == 0)

m.c106 = Constraint(expr=m.x22*m.x63 + m.x23*m.x71 + m.x24*m.x78 + m.x25*m.x84 + m.x26*m.x89 + m.x28*m.x96 - m.x169
                          == 0)

m.c107 = Constraint(expr=m.x22*m.x64 + m.x23*m.x72 + m.x24*m.x79 + m.x25*m.x85 + m.x26*m.x90 + m.x28*m.x97 - m.x170
                          == 0)

m.c108 = Constraint(expr=m.x29*m.x63 + m.x30*m.x71 + m.x31*m.x78 + m.x32*m.x84 + m.x33*m.x89 + m.x34*m.x93 + m.x36*m.x98
                          - m.x179 == 0)

m.c109 = Constraint(expr=m.x29*m.x64 + m.x30*m.x72 + m.x31*m.x79 + m.x32*m.x85 + m.x33*m.x90 + m.x34*m.x94 + m.x36*m.x99
                          - m.x180 == 0)

m.c110 = Constraint(expr=m.x37*m.x64 + m.x38*m.x72 + m.x39*m.x79 + m.x40*m.x85 + m.x41*m.x90 + m.x42*m.x94 + m.x43*m.x97
                          + m.x45*m.x100 - m.x190 == 0)

m.c111 = Constraint(expr= - 0.1*m.x101 + 2*m.x102 + 2*m.x103 + 2*m.x104 + 2*m.x105 + 2*m.x106 + 2*m.x107 + 2*m.x108
                          + 2*m.x109 + 2*m.x110 - 0.1*m.x112 + 2*m.x113 + 2*m.x114 + 2*m.x115 + 2*m.x116 + 2*m.x117
                          + 2*m.x118 + 2*m.x119 + 2*m.x120 - 0.1*m.x123 + 2*m.x124 + 2*m.x125 + 2*m.x126 + 2*m.x127
                          + 2*m.x128 + 2*m.x129 + 2*m.x130 - 0.1*m.x134 + 2*m.x135 + 2*m.x136 + 2*m.x137 + 2*m.x138
                          + 2*m.x139 + 2*m.x140 - 0.1*m.x145 + 2*m.x146 + 2*m.x147 + 2*m.x148 + 2*m.x149 + 2*m.x150
                          - 0.1*m.x156 + 2*m.x157 + 2*m.x158 + 2*m.x159 + 2*m.x160 - 0.1*m.x167 + 2*m.x168 + 2*m.x169
                          + 2*m.x170 - 0.1*m.x178 + 2*m.x179 + 2*m.x180 - 0.1*m.x189 + 2*m.x190 - 0.1*m.x200 == 0)
