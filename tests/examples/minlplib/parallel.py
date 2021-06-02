#  MINLP written by GAMS Convert at 04/21/18 13:52:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        116       82        5       29        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        206      181       25        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        752      597      155        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b15 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b18 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b19 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b21 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b23 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b24 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b25 = Var(within=Binary,bounds=(0,1),initialize=1)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(1,690),initialize=690)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=1013.33333333333*m.x26/m.x51 + 1013.33333333333*m.x27/m.x51 + 1013.33333333333*m.x28/m.x51 + 
                       1013.33333333333*m.x29/m.x51 + 1013.33333333333*m.x30/m.x51 + 781.25*m.x31/m.x51 + 781.25*m.x32/
                       m.x51 + 781.25*m.x33/m.x51 + 781.25*m.x34/m.x51 + 781.25*m.x35/m.x51 + 962.5*m.x36/m.x51 + 962.5*
                       m.x37/m.x51 + 962.5*m.x38/m.x51 + 962.5*m.x39/m.x51 + 962.5*m.x40/m.x51 + 937.5*m.x41/m.x51 + 
                       937.5*m.x42/m.x51 + 937.5*m.x43/m.x51 + 937.5*m.x44/m.x51 + 937.5*m.x45/m.x51 + 923.203125*m.x46/
                       m.x51 + 923.203125*m.x47/m.x51 + 923.203125*m.x48/m.x51 + 923.203125*m.x49/m.x51 + 923.203125*
                       m.x50/m.x51 - 1406.25*m.x82/m.x51 - 1406.25*m.x83/m.x51 - 1406.25*m.x84/m.x51 - 1406.25*m.x85/
                       m.x51 - 1406.25*m.x86/m.x51 - 4331.25*m.x87/m.x51 - 4331.25*m.x88/m.x51 - 4331.25*m.x89/m.x51 - 
                       4331.25*m.x90/m.x51 - 4331.25*m.x91/m.x51 - 3375*m.x92/m.x51 - 3375*m.x93/m.x51 - 3375*m.x94/
                       m.x51 - 3375*m.x95/m.x51 - 3375*m.x96/m.x51 - 4154.4140625*m.x97/m.x51 - 4154.4140625*m.x98/m.x51
                        - 4154.4140625*m.x99/m.x51 - 4154.4140625*m.x100/m.x51 - 4154.4140625*m.x101/m.x51 - 1824*m.x102
                       /m.x51 - 1824*m.x103/m.x51 - 1824*m.x104/m.x51 - 1824*m.x105/m.x51 - 1824*m.x106/m.x51 - 2598.75*
                       m.x112/m.x51 - 2598.75*m.x113/m.x51 - 2598.75*m.x114/m.x51 - 2598.75*m.x115/m.x51 - 2598.75*
                       m.x116/m.x51 - 1687.5*m.x117/m.x51 - 1687.5*m.x118/m.x51 - 1687.5*m.x119/m.x51 - 1687.5*m.x120/
                       m.x51 - 1687.5*m.x121/m.x51 - 2492.6484375*m.x122/m.x51 - 2492.6484375*m.x123/m.x51 - 
                       2492.6484375*m.x124/m.x51 - 2492.6484375*m.x125/m.x51 - 2492.6484375*m.x126/m.x51 - 4560*m.x127/
                       m.x51 - 4560*m.x128/m.x51 - 4560*m.x129/m.x51 - 4560*m.x130/m.x51 - 4560*m.x131/m.x51 - 2109.375*
                       m.x132/m.x51 - 2109.375*m.x133/m.x51 - 2109.375*m.x134/m.x51 - 2109.375*m.x135/m.x51 - 2109.375*
                       m.x136/m.x51 - 1687.5*m.x142/m.x51 - 1687.5*m.x143/m.x51 - 1687.5*m.x144/m.x51 - 1687.5*m.x145/
                       m.x51 - 1687.5*m.x146/m.x51 - 4985.296875*m.x147/m.x51 - 4985.296875*m.x148/m.x51 - 4985.296875*
                       m.x149/m.x51 - 4985.296875*m.x150/m.x51 - 4985.296875*m.x151/m.x51 - 3648*m.x152/m.x51 - 3648*
                       m.x153/m.x51 - 3648*m.x154/m.x51 - 3648*m.x155/m.x51 - 3648*m.x156/m.x51 - 1406.25*m.x157/m.x51
                        - 1406.25*m.x158/m.x51 - 1406.25*m.x159/m.x51 - 1406.25*m.x160/m.x51 - 1406.25*m.x161/m.x51 - 
                       1732.5*m.x162/m.x51 - 1732.5*m.x163/m.x51 - 1732.5*m.x164/m.x51 - 1732.5*m.x165/m.x51 - 1732.5*
                       m.x166/m.x51 - 4154.4140625*m.x172/m.x51 - 4154.4140625*m.x173/m.x51 - 4154.4140625*m.x174/m.x51
                        - 4154.4140625*m.x175/m.x51 - 4154.4140625*m.x176/m.x51 - 4560*m.x177/m.x51 - 4560*m.x178/m.x51
                        - 4560*m.x179/m.x51 - 4560*m.x180/m.x51 - 4560*m.x181/m.x51 - 2109.375*m.x182/m.x51 - 2109.375*
                       m.x183/m.x51 - 2109.375*m.x184/m.x51 - 2109.375*m.x185/m.x51 - 2109.375*m.x186/m.x51 - 5197.5*
                       m.x187/m.x51 - 5197.5*m.x188/m.x51 - 5197.5*m.x189/m.x51 - 5197.5*m.x190/m.x51 - 5197.5*m.x191/
                       m.x51 - 4218.75*m.x192/m.x51 - 4218.75*m.x193/m.x51 - 4218.75*m.x194/m.x51 - 4218.75*m.x195/m.x51
                        - 4218.75*m.x196/m.x51 - (2500*m.x72/m.x51 + 2500*m.x73/m.x51 + 2500*m.x74/m.x51 + 2500*m.x75/
                       m.x51 + 2500*m.x76/m.x51) + 3*m.x72 + 3*m.x73 + 3*m.x74 + 3*m.x75 + 3*m.x76
                        + 2.63768115942029*m.x52 + 2.63768115942029*m.x53 + 2.63768115942029*m.x54
                        + 2.63768115942029*m.x55 + 2.63768115942029*m.x56 + 2.81449275362319*m.x57
                        + 2.81449275362319*m.x58 + 2.81449275362319*m.x59 + 2.81449275362319*m.x60
                        + 2.81449275362319*m.x61 + 2.88405797101449*m.x62 + 2.88405797101449*m.x63
                        + 2.88405797101449*m.x64 + 2.88405797101449*m.x65 + 2.88405797101449*m.x66
                        + 2.88405797101449*m.x67 + 2.88405797101449*m.x68 + 2.88405797101449*m.x69
                        + 2.88405797101449*m.x70 + 2.88405797101449*m.x71 + 100000*m.x202 + 100000*m.x203
                        + 100000*m.x204 + 100000*m.x205, sense=minimize)

m.c1 = Constraint(expr= - m.x26 - m.x27 - m.x28 - m.x29 - m.x30 - m.x31 - m.x32 - m.x33 - m.x34 - m.x35 - m.x36 - m.x37
                        - m.x38 - m.x39 - m.x40 - m.x41 - m.x42 - m.x43 - m.x44 - m.x45 - m.x46 - m.x47 - m.x48 - m.x49
                        - m.x50 + m.x51 == 0)

m.c2 = Constraint(expr=-(m.x52/m.x51 + m.x53/m.x51 + m.x54/m.x51 + m.x55/m.x51 + m.x56/m.x51) - m.x202
                        <= -0.483091787439614)

m.c3 = Constraint(expr=-(m.x57/m.x51 + m.x58/m.x51 + m.x59/m.x51 + m.x60/m.x51 + m.x61/m.x51) - m.x203
                        <= -0.193236714975845)

m.c4 = Constraint(expr=-(m.x62/m.x51 + m.x63/m.x51 + m.x64/m.x51 + m.x65/m.x51 + m.x66/m.x51) - m.x204
                        <= -0.144927536231884)

m.c5 = Constraint(expr=-(m.x67/m.x51 + m.x68/m.x51 + m.x69/m.x51 + m.x70/m.x51 + m.x71/m.x51) - m.x205
                        <= -0.144927536231884)

m.c6 = Constraint(expr= - 1.33333333333333*m.x26 + m.x52 + 2.66666666666667*m.x102 + 6.66666666666667*m.x127
                        + 5.33333333333333*m.x152 + 6.66666666666667*m.x177 == 0)

m.c7 = Constraint(expr= - 1.33333333333333*m.x27 + m.x53 + 2.66666666666667*m.x103 + 6.66666666666667*m.x128
                        + 5.33333333333333*m.x153 + 6.66666666666667*m.x178 == 0)

m.c8 = Constraint(expr= - 1.33333333333333*m.x28 + m.x54 + 2.66666666666667*m.x104 + 6.66666666666667*m.x129
                        + 5.33333333333333*m.x154 + 6.66666666666667*m.x179 == 0)

m.c9 = Constraint(expr= - 1.33333333333333*m.x29 + m.x55 + 2.66666666666667*m.x105 + 6.66666666666667*m.x130
                        + 5.33333333333333*m.x155 + 6.66666666666667*m.x180 == 0)

m.c10 = Constraint(expr= - 1.33333333333333*m.x30 + m.x56 + 2.66666666666667*m.x106 + 6.66666666666667*m.x131
                         + 5.33333333333333*m.x156 + 6.66666666666667*m.x181 == 0)

m.c11 = Constraint(expr= - 1.04166666666667*m.x31 + m.x57 + 2.08333333333333*m.x82 + 3.125*m.x132
                         + 2.08333333333333*m.x157 + 3.125*m.x182 == 0)

m.c12 = Constraint(expr= - 1.04166666666667*m.x32 + m.x58 + 2.08333333333333*m.x83 + 3.125*m.x133
                         + 2.08333333333333*m.x158 + 3.125*m.x183 == 0)

m.c13 = Constraint(expr= - 1.04166666666667*m.x33 + m.x59 + 2.08333333333333*m.x84 + 3.125*m.x134
                         + 2.08333333333333*m.x159 + 3.125*m.x184 == 0)

m.c14 = Constraint(expr= - 1.04166666666667*m.x34 + m.x60 + 2.08333333333333*m.x85 + 3.125*m.x135
                         + 2.08333333333333*m.x160 + 3.125*m.x185 == 0)

m.c15 = Constraint(expr= - 1.04166666666667*m.x35 + m.x61 + 2.08333333333333*m.x86 + 3.125*m.x136
                         + 2.08333333333333*m.x161 + 3.125*m.x186 == 0)

m.c16 = Constraint(expr= - 1.25*m.x36 + m.x62 + 6.25*m.x87 + 3.75*m.x112 + 2.5*m.x162 + 7.5*m.x187 == 0)

m.c17 = Constraint(expr= - 1.25*m.x37 + m.x63 + 6.25*m.x88 + 3.75*m.x113 + 2.5*m.x163 + 7.5*m.x188 == 0)

m.c18 = Constraint(expr= - 1.25*m.x38 + m.x64 + 6.25*m.x89 + 3.75*m.x114 + 2.5*m.x164 + 7.5*m.x189 == 0)

m.c19 = Constraint(expr= - 1.25*m.x39 + m.x65 + 6.25*m.x90 + 3.75*m.x115 + 2.5*m.x165 + 7.5*m.x190 == 0)

m.c20 = Constraint(expr= - 1.25*m.x40 + m.x66 + 6.25*m.x91 + 3.75*m.x116 + 2.5*m.x166 + 7.5*m.x191 == 0)

m.c21 = Constraint(expr= - 1.25*m.x41 + m.x67 + 5*m.x92 + 2.5*m.x117 + 2.5*m.x142 + 6.25*m.x192 == 0)

m.c22 = Constraint(expr= - 1.25*m.x42 + m.x68 + 5*m.x93 + 2.5*m.x118 + 2.5*m.x143 + 6.25*m.x193 == 0)

m.c23 = Constraint(expr= - 1.25*m.x43 + m.x69 + 5*m.x94 + 2.5*m.x119 + 2.5*m.x144 + 6.25*m.x194 == 0)

m.c24 = Constraint(expr= - 1.25*m.x44 + m.x70 + 5*m.x95 + 2.5*m.x120 + 2.5*m.x145 + 6.25*m.x195 == 0)

m.c25 = Constraint(expr= - 1.25*m.x45 + m.x71 + 5*m.x96 + 2.5*m.x121 + 2.5*m.x146 + 6.25*m.x196 == 0)

m.c26 = Constraint(expr= - 1.21875*m.x46 + m.x72 + 6.09375*m.x97 + 3.65625*m.x122 + 7.3125*m.x147 + 6.09375*m.x172 == 0)

m.c27 = Constraint(expr= - 1.21875*m.x47 + m.x73 + 6.09375*m.x98 + 3.65625*m.x123 + 7.3125*m.x148 + 6.09375*m.x173 == 0)

m.c28 = Constraint(expr= - 1.21875*m.x48 + m.x74 + 6.09375*m.x99 + 3.65625*m.x124 + 7.3125*m.x149 + 6.09375*m.x174 == 0)

m.c29 = Constraint(expr= - 1.21875*m.x49 + m.x75 + 6.09375*m.x100 + 3.65625*m.x125 + 7.3125*m.x150 + 6.09375*m.x175
                         == 0)

m.c30 = Constraint(expr= - 1.21875*m.x50 + m.x76 + 6.09375*m.x101 + 3.65625*m.x126 + 7.3125*m.x151 + 6.09375*m.x176
                         == 0)

m.c31 = Constraint(expr=   m.b1 + m.b6 + m.b11 + m.b16 >= 1)

m.c32 = Constraint(expr=   m.b2 + m.b7 + m.b12 + m.b17 >= 1)

m.c33 = Constraint(expr=   m.b3 + m.b8 + m.b13 + m.b18 >= 1)

m.c34 = Constraint(expr=   m.b4 + m.b9 + m.b14 + m.b19 >= 1)

m.c35 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 + m.b5 == 1)

m.c36 = Constraint(expr=   m.b6 + m.b7 + m.b8 + m.b9 + m.b10 == 1)

m.c37 = Constraint(expr=   m.b11 + m.b12 + m.b13 + m.b14 + m.b15 == 1)

m.c38 = Constraint(expr=   m.b16 + m.b17 + m.b18 + m.b19 + m.b20 == 1)

m.c39 = Constraint(expr=   m.b21 + m.b22 + m.b23 + m.b24 + m.b25 == 1)

m.c40 = Constraint(expr=   m.b25 >= 1)

m.c41 = Constraint(expr= - 256*m.b1 + m.x26 <= 0)

m.c42 = Constraint(expr= - 256*m.b6 + m.x27 <= 0)

m.c43 = Constraint(expr= - 256*m.b11 + m.x28 <= 0)

m.c44 = Constraint(expr= - 256*m.b16 + m.x29 <= 0)

m.c45 = Constraint(expr= - 256*m.b21 + m.x30 <= 0)

m.c46 = Constraint(expr= - 131*m.b2 + m.x31 <= 0)

m.c47 = Constraint(expr= - 131*m.b7 + m.x32 <= 0)

m.c48 = Constraint(expr= - 131*m.b12 + m.x33 <= 0)

m.c49 = Constraint(expr= - 131*m.b17 + m.x34 <= 0)

m.c50 = Constraint(expr= - 131*m.b22 + m.x35 <= 0)

m.c51 = Constraint(expr= - 86*m.b3 + m.x36 <= 0)

m.c52 = Constraint(expr= - 86*m.b8 + m.x37 <= 0)

m.c53 = Constraint(expr= - 86*m.b13 + m.x38 <= 0)

m.c54 = Constraint(expr= - 86*m.b18 + m.x39 <= 0)

m.c55 = Constraint(expr= - 86*m.b23 + m.x40 <= 0)

m.c56 = Constraint(expr= - 85*m.b4 + m.x41 <= 0)

m.c57 = Constraint(expr= - 85*m.b9 + m.x42 <= 0)

m.c58 = Constraint(expr= - 85*m.b14 + m.x43 <= 0)

m.c59 = Constraint(expr= - 85*m.b19 + m.x44 <= 0)

m.c60 = Constraint(expr= - 85*m.b24 + m.x45 <= 0)

m.c61 = Constraint(expr= - 690*m.b5 + m.x46 <= 0)

m.c62 = Constraint(expr= - 690*m.b10 + m.x47 <= 0)

m.c63 = Constraint(expr= - 690*m.b15 + m.x48 <= 0)

m.c64 = Constraint(expr= - 690*m.b20 + m.x49 <= 0)

m.c65 = Constraint(expr= - 690*m.b25 + m.x50 <= 0)

m.c66 = Constraint(expr= - m.b1 + m.x77 + m.x102 + m.x127 + m.x152 + m.x177 == 0)

m.c67 = Constraint(expr= - m.b6 + m.x78 + m.x103 + m.x128 + m.x153 + m.x178 == 0)

m.c68 = Constraint(expr= - m.b11 + m.x79 + m.x104 + m.x129 + m.x154 + m.x179 == 0)

m.c69 = Constraint(expr= - m.b16 + m.x80 + m.x105 + m.x130 + m.x155 + m.x180 == 0)

m.c70 = Constraint(expr= - m.b21 + m.x81 + m.x106 + m.x131 + m.x156 + m.x181 == 0)

m.c71 = Constraint(expr= - m.b2 + m.x82 + m.x107 + m.x132 + m.x157 + m.x182 == 0)

m.c72 = Constraint(expr= - m.b7 + m.x83 + m.x108 + m.x133 + m.x158 + m.x183 == 0)

m.c73 = Constraint(expr= - m.b12 + m.x84 + m.x109 + m.x134 + m.x159 + m.x184 == 0)

m.c74 = Constraint(expr= - m.b17 + m.x85 + m.x110 + m.x135 + m.x160 + m.x185 == 0)

m.c75 = Constraint(expr= - m.b22 + m.x86 + m.x111 + m.x136 + m.x161 + m.x186 == 0)

m.c76 = Constraint(expr= - m.b3 + m.x87 + m.x112 + m.x137 + m.x162 + m.x187 == 0)

m.c77 = Constraint(expr= - m.b8 + m.x88 + m.x113 + m.x138 + m.x163 + m.x188 == 0)

m.c78 = Constraint(expr= - m.b13 + m.x89 + m.x114 + m.x139 + m.x164 + m.x189 == 0)

m.c79 = Constraint(expr= - m.b18 + m.x90 + m.x115 + m.x140 + m.x165 + m.x190 == 0)

m.c80 = Constraint(expr= - m.b23 + m.x91 + m.x116 + m.x141 + m.x166 + m.x191 == 0)

m.c81 = Constraint(expr= - m.b4 + m.x92 + m.x117 + m.x142 + m.x167 + m.x192 == 0)

m.c82 = Constraint(expr= - m.b9 + m.x93 + m.x118 + m.x143 + m.x168 + m.x193 == 0)

m.c83 = Constraint(expr= - m.b14 + m.x94 + m.x119 + m.x144 + m.x169 + m.x194 == 0)

m.c84 = Constraint(expr= - m.b19 + m.x95 + m.x120 + m.x145 + m.x170 + m.x195 == 0)

m.c85 = Constraint(expr= - m.b24 + m.x96 + m.x121 + m.x146 + m.x171 + m.x196 == 0)

m.c86 = Constraint(expr= - m.b5 + m.x97 + m.x122 + m.x147 + m.x172 + m.x197 == 0)

m.c87 = Constraint(expr= - m.b10 + m.x98 + m.x123 + m.x148 + m.x173 + m.x198 == 0)

m.c88 = Constraint(expr= - m.b15 + m.x99 + m.x124 + m.x149 + m.x174 + m.x199 == 0)

m.c89 = Constraint(expr= - m.b20 + m.x100 + m.x125 + m.x150 + m.x175 + m.x200 == 0)

m.c90 = Constraint(expr= - m.b25 + m.x101 + m.x126 + m.x151 + m.x176 + m.x201 == 0)

m.c91 = Constraint(expr= - m.b21 + m.x77 + m.x82 + m.x87 + m.x92 + m.x97 == 0)

m.c92 = Constraint(expr= - m.b1 + m.x78 + m.x83 + m.x88 + m.x93 + m.x98 == 0)

m.c93 = Constraint(expr= - m.b6 + m.x79 + m.x84 + m.x89 + m.x94 + m.x99 == 0)

m.c94 = Constraint(expr= - m.b11 + m.x80 + m.x85 + m.x90 + m.x95 + m.x100 == 0)

m.c95 = Constraint(expr= - m.b16 + m.x81 + m.x86 + m.x91 + m.x96 + m.x101 == 0)

m.c96 = Constraint(expr= - m.b22 + m.x102 + m.x107 + m.x112 + m.x117 + m.x122 == 0)

m.c97 = Constraint(expr= - m.b2 + m.x103 + m.x108 + m.x113 + m.x118 + m.x123 == 0)

m.c98 = Constraint(expr= - m.b7 + m.x104 + m.x109 + m.x114 + m.x119 + m.x124 == 0)

m.c99 = Constraint(expr= - m.b12 + m.x105 + m.x110 + m.x115 + m.x120 + m.x125 == 0)

m.c100 = Constraint(expr= - m.b17 + m.x106 + m.x111 + m.x116 + m.x121 + m.x126 == 0)

m.c101 = Constraint(expr= - m.b23 + m.x127 + m.x132 + m.x137 + m.x142 + m.x147 == 0)

m.c102 = Constraint(expr= - m.b3 + m.x128 + m.x133 + m.x138 + m.x143 + m.x148 == 0)

m.c103 = Constraint(expr= - m.b8 + m.x129 + m.x134 + m.x139 + m.x144 + m.x149 == 0)

m.c104 = Constraint(expr= - m.b13 + m.x130 + m.x135 + m.x140 + m.x145 + m.x150 == 0)

m.c105 = Constraint(expr= - m.b18 + m.x131 + m.x136 + m.x141 + m.x146 + m.x151 == 0)

m.c106 = Constraint(expr= - m.b24 + m.x152 + m.x157 + m.x162 + m.x167 + m.x172 == 0)

m.c107 = Constraint(expr= - m.b4 + m.x153 + m.x158 + m.x163 + m.x168 + m.x173 == 0)

m.c108 = Constraint(expr= - m.b9 + m.x154 + m.x159 + m.x164 + m.x169 + m.x174 == 0)

m.c109 = Constraint(expr= - m.b14 + m.x155 + m.x160 + m.x165 + m.x170 + m.x175 == 0)

m.c110 = Constraint(expr= - m.b19 + m.x156 + m.x161 + m.x166 + m.x171 + m.x176 == 0)

m.c111 = Constraint(expr= - m.b25 + m.x177 + m.x182 + m.x187 + m.x192 + m.x197 == 0)

m.c112 = Constraint(expr= - m.b5 + m.x178 + m.x183 + m.x188 + m.x193 + m.x198 == 0)

m.c113 = Constraint(expr= - m.b10 + m.x179 + m.x184 + m.x189 + m.x194 + m.x199 == 0)

m.c114 = Constraint(expr= - m.b15 + m.x180 + m.x185 + m.x190 + m.x195 + m.x200 == 0)

m.c115 = Constraint(expr= - m.b20 + m.x181 + m.x186 + m.x191 + m.x196 + m.x201 == 0)
