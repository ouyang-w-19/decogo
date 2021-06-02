#  NLP written by GAMS Convert at 04/21/18 13:52:27
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        197      170        5       22        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        194      194        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        621      383      238        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(-1.69454444444444,1.69454444444444),initialize=0)
m.x39 = Var(within=Reals,bounds=(-1.69454444444444,1.69454444444444),initialize=0)
m.x40 = Var(within=Reals,bounds=(-1.69454444444444,1.69454444444444),initialize=0)
m.x41 = Var(within=Reals,bounds=(-1.69444444444444,1.69444444444444),initialize=0)
m.x42 = Var(within=Reals,bounds=(-1.69454444444444,1.69454444444444),initialize=0)
m.x43 = Var(within=Reals,bounds=(-1.69454444444444,1.69454444444444),initialize=0)
m.x44 = Var(within=Reals,bounds=(-1.69444444444444,1.69444444444444),initialize=0)
m.x45 = Var(within=Reals,bounds=(-1.69444444444444,1.69444444444444),initialize=0)
m.x46 = Var(within=Reals,bounds=(-1.69454444444444,1.69454444444444),initialize=0)
m.x47 = Var(within=Reals,bounds=(-5.34037777777778,5.34037777777778),initialize=0)
m.x48 = Var(within=Reals,bounds=(-5.34037777777778,5.34037777777778),initialize=0)
m.x49 = Var(within=Reals,bounds=(-5.34037777777778,5.34037777777778),initialize=0)
m.x50 = Var(within=Reals,bounds=(-5.34027777777778,5.34027777777778),initialize=0)
m.x51 = Var(within=Reals,bounds=(-5.34037777777778,5.34037777777778),initialize=0)
m.x52 = Var(within=Reals,bounds=(-5.34037777777778,5.34037777777778),initialize=0)
m.x53 = Var(within=Reals,bounds=(-5.34027777777778,5.34027777777778),initialize=0)
m.x54 = Var(within=Reals,bounds=(-5.34027777777778,5.34027777777778),initialize=0)
m.x55 = Var(within=Reals,bounds=(-5.34037777777778,5.34037777777778),initialize=0)
m.x56 = Var(within=Reals,bounds=(-3.48536077097506,3.48536077097506),initialize=0)
m.x57 = Var(within=Reals,bounds=(-3.48536077097506,3.48536077097506),initialize=0)
m.x58 = Var(within=Reals,bounds=(-3.48536077097506,3.48536077097506),initialize=0)
m.x59 = Var(within=Reals,bounds=(-3.48526077097506,3.48526077097506),initialize=0)
m.x60 = Var(within=Reals,bounds=(-3.48536077097506,3.48536077097506),initialize=0)
m.x61 = Var(within=Reals,bounds=(-3.48536077097506,3.48536077097506),initialize=0)
m.x62 = Var(within=Reals,bounds=(-3.48526077097506,3.48526077097506),initialize=0)
m.x63 = Var(within=Reals,bounds=(-3.48526077097506,3.48526077097506),initialize=0)
m.x64 = Var(within=Reals,bounds=(-3.48536077097506,3.48536077097506),initialize=0)
m.x65 = Var(within=Reals,bounds=(-1,1),initialize=1)
m.x66 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x67 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x68 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x69 = Var(within=Reals,bounds=(-1,1),initialize=1)
m.x70 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x71 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x72 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x73 = Var(within=Reals,bounds=(-1,1),initialize=1)
m.x74 = Var(within=Reals,bounds=(-1,1),initialize=1)
m.x75 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x76 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x77 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x78 = Var(within=Reals,bounds=(-1,1),initialize=1)
m.x79 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x80 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x81 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x82 = Var(within=Reals,bounds=(-1,1),initialize=1)
m.x83 = Var(within=Reals,bounds=(-1,1),initialize=1)
m.x84 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x85 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x86 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x87 = Var(within=Reals,bounds=(-1,1),initialize=1)
m.x88 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x89 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x90 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x91 = Var(within=Reals,bounds=(-1,1),initialize=1)
m.x92 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x93 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x94 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x95 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x96 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x97 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x98 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x99 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x100 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x101 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x102 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x103 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x104 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x105 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x106 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x107 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x108 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x109 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x110 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x111 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x112 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x113 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x114 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x115 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x116 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x117 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x118 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x119 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x120 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x121 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x122 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x123 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x124 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x125 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x126 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x127 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x128 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x129 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x130 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x131 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x132 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x133 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x134 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x135 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x136 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x137 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x138 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x139 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x140 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x141 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x142 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x143 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x144 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x145 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x146 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x147 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x148 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x149 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x150 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x151 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x152 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x153 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x154 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x155 = Var(within=Reals,bounds=(18.9752196276824,None),initialize=18.9752196276824)
m.x156 = Var(within=Reals,bounds=(0.333333333333333,0.666666666666667),initialize=0.333333333333333)
m.x157 = Var(within=Reals,bounds=(0.333333333333333,0.666666666666667),initialize=0.333333333333333)
m.x158 = Var(within=Reals,bounds=(0.333333333333333,0.666666666666667),initialize=0.333333333333333)
m.x159 = Var(within=Reals,bounds=(1.25,2.08333333333333),initialize=1.25)
m.x160 = Var(within=Reals,bounds=(1.25,2.08333333333333),initialize=1.25)
m.x161 = Var(within=Reals,bounds=(1.25,2.08333333333333),initialize=1.25)
m.x162 = Var(within=Reals,bounds=(0.666666666666667,1.42857142857143),initialize=0.666666666666667)
m.x163 = Var(within=Reals,bounds=(0.666666666666667,1.42857142857143),initialize=0.666666666666667)
m.x164 = Var(within=Reals,bounds=(0.666666666666667,1.42857142857143),initialize=0.666666666666667)
m.x165 = Var(within=Reals,bounds=(2,9),initialize=2)
m.x166 = Var(within=Reals,bounds=(2,9),initialize=2)
m.x167 = Var(within=Reals,bounds=(2,9),initialize=2)
m.x168 = Var(within=Reals,bounds=(1,8),initialize=1)
m.x169 = Var(within=Reals,bounds=(1,8),initialize=1)
m.x170 = Var(within=Reals,bounds=(1,8),initialize=1)
m.x171 = Var(within=Reals,bounds=(0.6,8.4),initialize=0.6)
m.x172 = Var(within=Reals,bounds=(0.6,8.4),initialize=0.6)
m.x173 = Var(within=Reals,bounds=(0.6,8.4),initialize=0.6)
m.x174 = Var(within=Reals,bounds=(0.7,8.3),initialize=0.7)
m.x175 = Var(within=Reals,bounds=(0.7,8.3),initialize=0.7)
m.x176 = Var(within=Reals,bounds=(0.7,8.3),initialize=0.7)
m.x177 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,10),initialize=0)

m.obj = Objective(expr=   m.x155, sense=minimize)

m.c2 = Constraint(expr=-m.x165*m.x166*m.x167 + m.x155 == 0)

m.c3 = Constraint(expr=m.x65*m.x69*m.x73 - m.x65*m.x70*m.x72 - m.x66*m.x68*m.x73 + m.x66*m.x71*m.x70 + m.x68*m.x67*m.x72
                        - m.x67*m.x69*m.x71 == 1)

m.c4 = Constraint(expr=m.x74*m.x78*m.x82 - m.x74*m.x79*m.x81 - m.x75*m.x77*m.x82 + m.x75*m.x80*m.x79 + m.x77*m.x76*m.x81
                        - m.x76*m.x78*m.x80 == 1)

m.c5 = Constraint(expr=m.x83*m.x87*m.x91 - m.x83*m.x88*m.x90 - m.x84*m.x86*m.x91 + m.x84*m.x89*m.x88 + m.x86*m.x85*m.x90
                        - m.x85*m.x87*m.x89 == 1)

m.c6 = Constraint(expr=   m.x101 + m.x102 + m.x103 == 1)

m.c7 = Constraint(expr=   m.x104 + m.x105 + m.x106 == 0)

m.c8 = Constraint(expr=   m.x107 + m.x108 + m.x109 == 0)

m.c9 = Constraint(expr=   m.x110 + m.x111 + m.x112 == 1)

m.c10 = Constraint(expr=   m.x113 + m.x114 + m.x115 == 0)

m.c11 = Constraint(expr=   m.x116 + m.x117 + m.x118 == 1)

m.c12 = Constraint(expr=   m.x119 + m.x120 + m.x121 == 1)

m.c13 = Constraint(expr=   m.x122 + m.x123 + m.x124 == 0)

m.c14 = Constraint(expr=   m.x125 + m.x126 + m.x127 == 0)

m.c15 = Constraint(expr=   m.x128 + m.x129 + m.x130 == 1)

m.c16 = Constraint(expr=   m.x131 + m.x132 + m.x133 == 0)

m.c17 = Constraint(expr=   m.x134 + m.x135 + m.x136 == 1)

m.c18 = Constraint(expr=   m.x137 + m.x138 + m.x139 == 1)

m.c19 = Constraint(expr=   m.x140 + m.x141 + m.x142 == 0)

m.c20 = Constraint(expr=   m.x143 + m.x144 + m.x145 == 0)

m.c21 = Constraint(expr=   m.x146 + m.x147 + m.x148 == 1)

m.c22 = Constraint(expr=   m.x149 + m.x150 + m.x151 == 0)

m.c23 = Constraint(expr=   m.x152 + m.x153 + m.x154 == 1)

m.c24 = Constraint(expr=   m.x38 - 0.25*m.x101 - 0.444444444444444*m.x102 - m.x103 == 0)

m.c25 = Constraint(expr=   m.x39 - 0.25*m.x104 - 0.444444444444444*m.x105 - m.x106 == 0)

m.c26 = Constraint(expr=   m.x40 - 0.25*m.x107 - 0.444444444444444*m.x108 - m.x109 == 0)

m.c27 = Constraint(expr=   m.x42 - 0.25*m.x110 - 0.444444444444444*m.x111 - m.x112 == 0)

m.c28 = Constraint(expr=   m.x43 - 0.25*m.x113 - 0.444444444444444*m.x114 - m.x115 == 0)

m.c29 = Constraint(expr=   m.x46 - 0.25*m.x116 - 0.444444444444444*m.x117 - m.x118 == 0)

m.c30 = Constraint(expr=   m.x47 - m.x119 - 1.5625*m.x120 - 2.77777777777778*m.x121 == 0)

m.c31 = Constraint(expr=   m.x48 - m.x122 - 1.5625*m.x123 - 2.77777777777778*m.x124 == 0)

m.c32 = Constraint(expr=   m.x49 - m.x125 - 1.5625*m.x126 - 2.77777777777778*m.x127 == 0)

m.c33 = Constraint(expr=   m.x51 - m.x128 - 1.5625*m.x129 - 2.77777777777778*m.x130 == 0)

m.c34 = Constraint(expr=   m.x52 - m.x131 - 1.5625*m.x132 - 2.77777777777778*m.x133 == 0)

m.c35 = Constraint(expr=   m.x55 - m.x134 - 1.5625*m.x135 - 2.77777777777778*m.x136 == 0)

m.c36 = Constraint(expr=   m.x56 - 0.444444444444444*m.x137 - m.x138 - 2.04081632653061*m.x139 == 0)

m.c37 = Constraint(expr=   m.x57 - 0.444444444444444*m.x140 - m.x141 - 2.04081632653061*m.x142 == 0)

m.c38 = Constraint(expr=   m.x58 - 0.444444444444444*m.x143 - m.x144 - 2.04081632653061*m.x145 == 0)

m.c39 = Constraint(expr=   m.x60 - 0.444444444444444*m.x146 - m.x147 - 2.04081632653061*m.x148 == 0)

m.c40 = Constraint(expr=   m.x61 - 0.444444444444444*m.x149 - m.x150 - 2.04081632653061*m.x151 == 0)

m.c41 = Constraint(expr=   m.x64 - 0.444444444444444*m.x152 - m.x153 - 2.04081632653061*m.x154 == 0)

m.c42 = Constraint(expr= - m.x39 + m.x41 == 0)

m.c43 = Constraint(expr= - m.x40 + m.x44 == 0)

m.c44 = Constraint(expr= - m.x43 + m.x45 == 0)

m.c45 = Constraint(expr= - m.x48 + m.x50 == 0)

m.c46 = Constraint(expr= - m.x49 + m.x53 == 0)

m.c47 = Constraint(expr= - m.x52 + m.x54 == 0)

m.c48 = Constraint(expr= - m.x57 + m.x59 == 0)

m.c49 = Constraint(expr= - m.x58 + m.x62 == 0)

m.c50 = Constraint(expr= - m.x61 + m.x63 == 0)

m.c51 = Constraint(expr= - m.x165 + m.x168 <= -1)

m.c52 = Constraint(expr= - m.x166 + m.x169 <= -1)

m.c53 = Constraint(expr= - m.x167 + m.x170 <= -1)

m.c54 = Constraint(expr= - m.x165 + m.x171 <= -0.6)

m.c55 = Constraint(expr= - m.x166 + m.x172 <= -0.6)

m.c56 = Constraint(expr= - m.x167 + m.x173 <= -0.6)

m.c57 = Constraint(expr= - m.x165 + m.x174 <= -0.7)

m.c58 = Constraint(expr= - m.x166 + m.x175 <= -0.7)

m.c59 = Constraint(expr= - m.x167 + m.x176 <= -0.7)

m.c60 = Constraint(expr=m.x156**2 - (m.x42*m.x46 - m.x43*m.x45) == 0)

m.c61 = Constraint(expr=m.x159**2 - (m.x51*m.x55 - m.x52*m.x54) == 0)

m.c62 = Constraint(expr=m.x162**2 - (m.x60*m.x64 - m.x61*m.x63) == 0)

m.c63 = Constraint(expr=m.x157**2 - (m.x38*m.x46 - m.x40*m.x44) == 0)

m.c64 = Constraint(expr=m.x160**2 - (m.x47*m.x55 - m.x49*m.x53) == 0)

m.c65 = Constraint(expr=m.x163**2 - (m.x56*m.x64 - m.x58*m.x62) == 0)

m.c66 = Constraint(expr=m.x158**2 - (m.x38*m.x42 - m.x39*m.x41) == 0)

m.c67 = Constraint(expr=m.x161**2 - (m.x47*m.x51 - m.x48*m.x50) == 0)

m.c68 = Constraint(expr=m.x164**2 - (m.x56*m.x60 - m.x57*m.x59) == 0)

m.c69 = Constraint(expr=   3*m.x156 - m.x168 + m.x177 == 0)

m.c70 = Constraint(expr=   3*m.x157 - m.x169 + m.x178 == 0)

m.c71 = Constraint(expr=   3*m.x158 - m.x170 + m.x179 == 0)

m.c72 = Constraint(expr=   0.48*m.x159 - m.x171 + m.x180 == 0)

m.c73 = Constraint(expr=   0.48*m.x160 - m.x172 + m.x181 == 0)

m.c74 = Constraint(expr=   0.48*m.x161 - m.x173 + m.x182 == 0)

m.c75 = Constraint(expr=   1.05*m.x162 - m.x174 + m.x183 == 0)

m.c76 = Constraint(expr=   1.05*m.x163 - m.x175 + m.x184 == 0)

m.c77 = Constraint(expr=   1.05*m.x164 - m.x176 + m.x185 == 0)

m.c78 = Constraint(expr= - 3*m.x156 - m.x168 + m.x186 == 0)

m.c79 = Constraint(expr= - 3*m.x157 - m.x169 + m.x187 == 0)

m.c80 = Constraint(expr= - 3*m.x158 - m.x170 + m.x188 == 0)

m.c81 = Constraint(expr= - 0.48*m.x159 - m.x171 + m.x189 == 0)

m.c82 = Constraint(expr= - 0.48*m.x160 - m.x172 + m.x190 == 0)

m.c83 = Constraint(expr= - 0.48*m.x161 - m.x173 + m.x191 == 0)

m.c84 = Constraint(expr= - 1.05*m.x162 - m.x174 + m.x192 == 0)

m.c85 = Constraint(expr= - 1.05*m.x163 - m.x175 + m.x193 == 0)

m.c86 = Constraint(expr= - 1.05*m.x164 - m.x176 + m.x194 == 0)

m.c87 = Constraint(expr= - m.x165 + m.x186 <= 0)

m.c88 = Constraint(expr= - m.x166 + m.x187 <= 0)

m.c89 = Constraint(expr= - m.x167 + m.x188 <= 0)

m.c90 = Constraint(expr= - m.x165 + m.x189 <= 0)

m.c91 = Constraint(expr= - m.x166 + m.x190 <= 0)

m.c92 = Constraint(expr= - m.x167 + m.x191 <= 0)

m.c93 = Constraint(expr= - m.x165 + m.x192 <= 0)

m.c94 = Constraint(expr= - m.x166 + m.x193 <= 0)

m.c95 = Constraint(expr= - m.x167 + m.x194 <= 0)

m.c96 = Constraint(expr=   m.x165 - m.x166 >= 0)

m.c97 = Constraint(expr=   m.x166 - m.x167 >= 0)

m.c98 = Constraint(expr= - 0.5*m.x165 + m.x168 <= 0)

m.c99 = Constraint(expr= - 0.5*m.x166 + m.x169 <= 0)

m.c100 = Constraint(expr= - 0.5*m.x167 + m.x170 <= 0)

m.c101 = Constraint(expr=m.x92**2 + m.x93**2 + m.x94**2 == 1)

m.c102 = Constraint(expr=m.x95**2 + m.x96**2 + m.x97**2 == 1)

m.c103 = Constraint(expr=m.x98**2 + m.x99**2 + m.x100**2 == 1)

m.c104 = Constraint(expr=-m.x65*m.x65 + m.x101 == 0)

m.c105 = Constraint(expr=-m.x66*m.x66 + m.x102 == 0)

m.c106 = Constraint(expr=-m.x67*m.x67 + m.x103 == 0)

m.c107 = Constraint(expr=-m.x65*m.x68 + m.x104 == 0)

m.c108 = Constraint(expr=-m.x66*m.x69 + m.x105 == 0)

m.c109 = Constraint(expr=-m.x67*m.x70 + m.x106 == 0)

m.c110 = Constraint(expr=-m.x65*m.x71 + m.x107 == 0)

m.c111 = Constraint(expr=-m.x66*m.x72 + m.x108 == 0)

m.c112 = Constraint(expr=-m.x67*m.x73 + m.x109 == 0)

m.c113 = Constraint(expr=-m.x68*m.x68 + m.x110 == 0)

m.c114 = Constraint(expr=-m.x69*m.x69 + m.x111 == 0)

m.c115 = Constraint(expr=-m.x70*m.x70 + m.x112 == 0)

m.c116 = Constraint(expr=-m.x68*m.x71 + m.x113 == 0)

m.c117 = Constraint(expr=-m.x69*m.x72 + m.x114 == 0)

m.c118 = Constraint(expr=-m.x70*m.x73 + m.x115 == 0)

m.c119 = Constraint(expr=-m.x71*m.x71 + m.x116 == 0)

m.c120 = Constraint(expr=-m.x72*m.x72 + m.x117 == 0)

m.c121 = Constraint(expr=-m.x73*m.x73 + m.x118 == 0)

m.c122 = Constraint(expr=-m.x74*m.x74 + m.x119 == 0)

m.c123 = Constraint(expr=-m.x75*m.x75 + m.x120 == 0)

m.c124 = Constraint(expr=-m.x76*m.x76 + m.x121 == 0)

m.c125 = Constraint(expr=-m.x74*m.x77 + m.x122 == 0)

m.c126 = Constraint(expr=-m.x75*m.x78 + m.x123 == 0)

m.c127 = Constraint(expr=-m.x76*m.x79 + m.x124 == 0)

m.c128 = Constraint(expr=-m.x74*m.x80 + m.x125 == 0)

m.c129 = Constraint(expr=-m.x75*m.x81 + m.x126 == 0)

m.c130 = Constraint(expr=-m.x76*m.x82 + m.x127 == 0)

m.c131 = Constraint(expr=-m.x77*m.x77 + m.x128 == 0)

m.c132 = Constraint(expr=-m.x78*m.x78 + m.x129 == 0)

m.c133 = Constraint(expr=-m.x79*m.x79 + m.x130 == 0)

m.c134 = Constraint(expr=-m.x77*m.x80 + m.x131 == 0)

m.c135 = Constraint(expr=-m.x78*m.x81 + m.x132 == 0)

m.c136 = Constraint(expr=-m.x79*m.x82 + m.x133 == 0)

m.c137 = Constraint(expr=-m.x80*m.x80 + m.x134 == 0)

m.c138 = Constraint(expr=-m.x81*m.x81 + m.x135 == 0)

m.c139 = Constraint(expr=-m.x82*m.x82 + m.x136 == 0)

m.c140 = Constraint(expr=-m.x83*m.x83 + m.x137 == 0)

m.c141 = Constraint(expr=-m.x84*m.x84 + m.x138 == 0)

m.c142 = Constraint(expr=-m.x85*m.x85 + m.x139 == 0)

m.c143 = Constraint(expr=-m.x83*m.x86 + m.x140 == 0)

m.c144 = Constraint(expr=-m.x84*m.x87 + m.x141 == 0)

m.c145 = Constraint(expr=-m.x85*m.x88 + m.x142 == 0)

m.c146 = Constraint(expr=-m.x83*m.x89 + m.x143 == 0)

m.c147 = Constraint(expr=-m.x84*m.x90 + m.x144 == 0)

m.c148 = Constraint(expr=-m.x85*m.x91 + m.x145 == 0)

m.c149 = Constraint(expr=-m.x86*m.x86 + m.x146 == 0)

m.c150 = Constraint(expr=-m.x87*m.x87 + m.x147 == 0)

m.c151 = Constraint(expr=-m.x88*m.x88 + m.x148 == 0)

m.c152 = Constraint(expr=-m.x86*m.x89 + m.x149 == 0)

m.c153 = Constraint(expr=-m.x87*m.x90 + m.x150 == 0)

m.c154 = Constraint(expr=-m.x88*m.x91 + m.x151 == 0)

m.c155 = Constraint(expr=-m.x89*m.x89 + m.x152 == 0)

m.c156 = Constraint(expr=-m.x90*m.x90 + m.x153 == 0)

m.c157 = Constraint(expr=-m.x91*m.x91 + m.x154 == 0)

m.c158 = Constraint(expr=m.x167**3 - m.x155 <= 0)

m.c159 = Constraint(expr=   m.x29 - m.x168 + m.x171 == 0)

m.c160 = Constraint(expr=   m.x30 - m.x169 + m.x172 == 0)

m.c161 = Constraint(expr=   m.x31 - m.x170 + m.x173 == 0)

m.c162 = Constraint(expr=   m.x32 - m.x168 + m.x174 == 0)

m.c163 = Constraint(expr=   m.x33 - m.x169 + m.x175 == 0)

m.c164 = Constraint(expr=   m.x34 - m.x170 + m.x176 == 0)

m.c165 = Constraint(expr=   m.x35 - m.x171 + m.x174 == 0)

m.c166 = Constraint(expr=   m.x36 - m.x172 + m.x175 == 0)

m.c167 = Constraint(expr=   m.x37 - m.x173 + m.x176 == 0)

m.c168 = Constraint(expr=m.x92*m.x29 + m.x93*m.x30 + m.x94*m.x31 - (sqrt((m.x2*m.x92)**2 + (m.x5*m.x93)**2 + (m.x8*m.x94
                         )**2 + (m.x3*m.x92)**2 + (m.x6*m.x93)**2 + (m.x9*m.x94)**2 + (m.x4*m.x92)**2 + (m.x7*m.x93)**2
                          + (m.x10*m.x94)**2) + sqrt((m.x11*m.x92)**2 + (m.x14*m.x93)**2 + (m.x17*m.x94)**2 + (m.x12*
                         m.x92)**2 + (m.x15*m.x93)**2 + (m.x18*m.x94)**2 + (m.x13*m.x92)**2 + (m.x16*m.x93)**2 + (m.x19*
                         m.x94)**2)) >= 0)

m.c169 = Constraint(expr=m.x95*m.x32 + m.x96*m.x33 + m.x97*m.x34 - (sqrt((m.x2*m.x95)**2 + (m.x5*m.x96)**2 + (m.x8*m.x97
                         )**2 + (m.x3*m.x95)**2 + (m.x6*m.x96)**2 + (m.x9*m.x97)**2 + (m.x4*m.x95)**2 + (m.x7*m.x96)**2
                          + (m.x10*m.x97)**2) + sqrt((m.x20*m.x95)**2 + (m.x23*m.x96)**2 + (m.x26*m.x97)**2 + (m.x21*
                         m.x95)**2 + (m.x24*m.x96)**2 + (m.x27*m.x97)**2 + (m.x22*m.x95)**2 + (m.x25*m.x96)**2 + (m.x28*
                         m.x97)**2)) >= 0)

m.c170 = Constraint(expr=m.x98*m.x35 + m.x99*m.x36 + m.x100*m.x37 - (sqrt((m.x11*m.x98)**2 + (m.x14*m.x99)**2 + (m.x17*
                         m.x100)**2 + (m.x12*m.x98)**2 + (m.x15*m.x99)**2 + (m.x18*m.x100)**2 + (m.x13*m.x98)**2 + (
                         m.x16*m.x99)**2 + (m.x19*m.x100)**2) + sqrt((m.x20*m.x98)**2 + (m.x23*m.x99)**2 + (m.x26*m.x100
                         )**2 + (m.x21*m.x98)**2 + (m.x24*m.x99)**2 + (m.x27*m.x100)**2 + (m.x22*m.x98)**2 + (m.x25*
                         m.x99)**2 + (m.x28*m.x100)**2)) >= 0)

m.c171 = Constraint(expr=   m.x2 - 2*m.x65 == 0)

m.c172 = Constraint(expr=   m.x3 - 1.5*m.x66 == 0)

m.c173 = Constraint(expr=   m.x4 - m.x67 == 0)

m.c174 = Constraint(expr=   m.x5 - 2*m.x68 == 0)

m.c175 = Constraint(expr=   m.x6 - 1.5*m.x69 == 0)

m.c176 = Constraint(expr=   m.x7 - m.x70 == 0)

m.c177 = Constraint(expr=   m.x8 - 2*m.x71 == 0)

m.c178 = Constraint(expr=   m.x9 - 1.5*m.x72 == 0)

m.c179 = Constraint(expr=   m.x10 - m.x73 == 0)

m.c180 = Constraint(expr=   m.x11 - m.x74 == 0)

m.c181 = Constraint(expr=   m.x12 - 0.8*m.x75 == 0)

m.c182 = Constraint(expr=   m.x13 - 0.6*m.x76 == 0)

m.c183 = Constraint(expr=   m.x14 - m.x77 == 0)

m.c184 = Constraint(expr=   m.x15 - 0.8*m.x78 == 0)

m.c185 = Constraint(expr=   m.x16 - 0.6*m.x79 == 0)

m.c186 = Constraint(expr=   m.x17 - m.x80 == 0)

m.c187 = Constraint(expr=   m.x18 - 0.8*m.x81 == 0)

m.c188 = Constraint(expr=   m.x19 - 0.6*m.x82 == 0)

m.c189 = Constraint(expr=   m.x20 - 1.5*m.x83 == 0)

m.c190 = Constraint(expr=   m.x21 - m.x84 == 0)

m.c191 = Constraint(expr=   m.x22 - 0.7*m.x85 == 0)

m.c192 = Constraint(expr=   m.x23 - 1.5*m.x86 == 0)

m.c193 = Constraint(expr=   m.x24 - m.x87 == 0)

m.c194 = Constraint(expr=   m.x25 - 0.7*m.x88 == 0)

m.c195 = Constraint(expr=   m.x26 - 1.5*m.x89 == 0)

m.c196 = Constraint(expr=   m.x27 - m.x90 == 0)

m.c197 = Constraint(expr=   m.x28 - 0.7*m.x91 == 0)
