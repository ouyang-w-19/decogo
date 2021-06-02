#  MINLP written by GAMS Convert at 04/21/18 13:52:17
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        213      100      110        3        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        132       94       38        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        589      521       68        0
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
m.b21 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b23 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b24 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b25 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b26 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b27 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b28 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b29 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b30 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b31 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b32 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b33 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b34 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b35 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b36 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b38 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,130),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,125),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,212),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,334),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,833),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,381),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,950),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,155),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,401),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,532),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,816),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,161),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,2467),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,900),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,900),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,255),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,255),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,546),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,546),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,1331),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,1331),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,1509),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,1509),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,2200),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,2200),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,900),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,900),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,2200),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,2200),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,950),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,950),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,1400),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,1400),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,720),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,720),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,3000),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,1800),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,1800),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,1400),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,1400),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,2200),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,2200),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,1800),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,1800),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,1),initialize=0)
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

m.obj = Objective(expr=   20*m.b1 + 520*m.b2 + 20*m.b3 + 100*m.b4 + 20*m.b5 + 80*m.b6 + 550*m.b7 + 80*m.b9 + 400*m.b10
                        + 16*m.b11 + 50*m.b13 + 80*m.b15 + 300*m.b16 + 500*m.b17 + 500*m.b18 + 500*m.b19 + 500*m.b21
                        + 500*m.b22 + 320*m.b25 + 40*m.b26 + 40*m.b27 + 200*m.b28 + 200*m.b29 + 80*m.b30 + 10*m.b31
                        + 600*m.b32 + 420*m.b33 + 7500*m.b37 + 9300*m.b38 - 12.822715454568*m.x82
                        - 12.822715454568*m.x83 - 12.822715454568*m.x84 - 12.822715454568*m.x85 - 12.822715454568*m.x86
                        - 12.822715454568*m.x87 - 12.822715454568*m.x88 - 12.822715454568*m.x89
                        + 14104.9870000248, sense=minimize)

m.c2 = Constraint(expr= - m.x39 >= -130)

m.c3 = Constraint(expr= - m.x40 >= -125)

m.c4 = Constraint(expr= - m.x41 >= -212)

m.c5 = Constraint(expr= - m.x42 >= -334)

m.c6 = Constraint(expr= - m.x43 >= -833)

m.c7 = Constraint(expr= - m.x44 >= -381)

m.c8 = Constraint(expr= - m.x45 >= -5610)

m.c9 = Constraint(expr= - m.x46 >= -155)

m.c10 = Constraint(expr=   401*m.b1 - m.x47 >= 0)

m.c11 = Constraint(expr=   600*m.b2 - m.x48 - m.x49 >= 0)

m.c12 = Constraint(expr=   532*m.b3 - m.x50 >= 0)

m.c13 = Constraint(expr=   816*m.b4 - m.x51 >= 0)

m.c14 = Constraint(expr=   161*m.b5 - m.x52 >= 0)

m.c15 = Constraint(expr=   2467*m.b6 - m.x53 >= 0)

m.c16 = Constraint(expr=   923*m.b7 - m.x54 - m.x55 >= 0)

m.c17 = Constraint(expr=   401*m.b8 - m.x47 >= 0)

m.c18 = Constraint(expr=   600*m.b9 - m.x48 >= 0)

m.c19 = Constraint(expr=   600*m.b10 - m.x49 >= 0)

m.c20 = Constraint(expr=   532*m.b11 - m.x50 >= 0)

m.c21 = Constraint(expr=   816*m.b12 - m.x51 >= 0)

m.c22 = Constraint(expr=   161*m.b13 - m.x52 >= 0)

m.c23 = Constraint(expr=   2467*m.b14 - m.x53 >= 0)

m.c24 = Constraint(expr=   900*m.b15 - m.x54 >= 0)

m.c25 = Constraint(expr=   900*m.b16 - m.x55 >= 0)

m.c26 = Constraint(expr=   m.b1 - m.b8 >= 0)

m.c27 = Constraint(expr=   m.b2 - m.b9 >= 0)

m.c28 = Constraint(expr=   m.b2 - m.b10 >= 0)

m.c29 = Constraint(expr=   m.b3 - m.b11 >= 0)

m.c30 = Constraint(expr=   m.b4 - m.b12 >= 0)

m.c31 = Constraint(expr=   m.b5 - m.b13 >= 0)

m.c32 = Constraint(expr=   m.b6 - m.b14 >= 0)

m.c33 = Constraint(expr=   m.b7 - m.b15 >= 0)

m.c34 = Constraint(expr=   m.b7 - m.b16 >= 0)

m.c35 = Constraint(expr= - m.b1 + m.b8 >= 0)

m.c36 = Constraint(expr= - m.b2 + m.b9 + m.b10 >= 0)

m.c37 = Constraint(expr= - m.b3 + m.b11 >= 0)

m.c38 = Constraint(expr= - m.b4 + m.b12 >= 0)

m.c39 = Constraint(expr= - m.b5 + m.b13 >= 0)

m.c40 = Constraint(expr= - m.b6 + m.b14 >= 0)

m.c41 = Constraint(expr= - m.b7 + m.b15 + m.b16 >= 0)

m.c42 = Constraint(expr= - 0.007177*m.x39 - 0.008782*m.x40 + m.x56 == 0)

m.c43 = Constraint(expr= - 0.992823*m.x39 - 0.991218*m.x40 + m.x57 == 0)

m.c44 = Constraint(expr= - 0.002687*m.x41 - 0.092341*m.x42 + m.x58 == 0)

m.c45 = Constraint(expr= - 0.997313*m.x41 - 0.907659*m.x42 + m.x59 == 0)

m.c46 = Constraint(expr= - 0.00684*m.x44 - 0.016427*m.x45 + m.x60 == 0)

m.c47 = Constraint(expr= - 0.99316*m.x44 - 0.983573*m.x45 + m.x61 == 0)

m.c48 = Constraint(expr= - 0.088511*m.x47 - 0.015894*m.x48 + m.x62 == 0)

m.c49 = Constraint(expr= - 0.911489*m.x47 - 0.984106*m.x48 + m.x63 == 0)

m.c50 = Constraint(expr= - 0.024263*m.x50 - 0.009488*m.x51 - 0.023048*m.x52 + m.x64 == 0)

m.c51 = Constraint(expr= - 0.975737*m.x50 - 0.990512*m.x51 - 0.976952*m.x52 + m.x65 == 0)

m.c52 = Constraint(expr= - m.x64 - m.x66 + m.x70 == 0)

m.c53 = Constraint(expr= - m.x65 - m.x67 + m.x71 == 0)

m.c54 = Constraint(expr= - 0.0383*m.x55 - m.x68 - m.x76 + m.x80 == 0)

m.c55 = Constraint(expr= - 0.9617*m.x55 - m.x69 - m.x77 + m.x81 == 0)

m.c56 = Constraint(expr=   m.x66 - 0.0334*m.x98 - 0.0383*m.x99 == 0)

m.c57 = Constraint(expr=   m.x67 - 0.9666*m.x98 - 0.9617*m.x99 == 0)

m.c58 = Constraint(expr=   m.x68 - 0.0334*m.x100 - 0.0383*m.x101 == 0)

m.c59 = Constraint(expr=   m.x69 - 0.9666*m.x100 - 0.9617*m.x101 == 0)

m.c60 = Constraint(expr=   m.x72 - 0.034121*m.x102 - 0.014483*m.x103 - m.x108 - m.x110 == 0)

m.c61 = Constraint(expr=   m.x73 - 0.965879*m.x102 - 0.985517*m.x103 - m.x109 - m.x111 == 0)

m.c62 = Constraint(expr=   m.x74 - 0.034121*m.x104 - 0.014483*m.x105 - m.x112 - m.x114 == 0)

m.c63 = Constraint(expr=   m.x75 - 0.965879*m.x104 - 0.985517*m.x105 - m.x113 - m.x115 == 0)

m.c64 = Constraint(expr=   m.x76 - 0.015894*m.x106 - m.x116 - m.x118 - m.x120 == 0)

m.c65 = Constraint(expr=   m.x77 - 0.984106*m.x106 - m.x117 - m.x119 - m.x121 == 0)

m.c66 = Constraint(expr=   m.x78 - 0.015894*m.x107 - m.x122 - m.x124 - m.x126 == 0)

m.c67 = Constraint(expr=   m.x79 - 0.984106*m.x107 - m.x123 - m.x125 - m.x127 == 0)

m.c68 = Constraint(expr=-m.x90*m.x53 + m.x98 == 0)

m.c69 = Constraint(expr=-m.x90*m.x54 + m.x99 == 0)

m.c70 = Constraint(expr=-m.x91*m.x53 + m.x100 == 0)

m.c71 = Constraint(expr=-m.x91*m.x54 + m.x101 == 0)

m.c72 = Constraint(expr=-m.x92*m.x43 + m.x102 == 0)

m.c73 = Constraint(expr=-m.x92*m.x46 + m.x103 == 0)

m.c74 = Constraint(expr=-m.x93*m.x43 + m.x104 == 0)

m.c75 = Constraint(expr=-m.x93*m.x46 + m.x105 == 0)

m.c76 = Constraint(expr=-m.x94*m.x49 + m.x106 == 0)

m.c77 = Constraint(expr=-m.x95*m.x49 + m.x107 == 0)

m.c78 = Constraint(expr=-m.x92*m.x58 + m.x108 == 0)

m.c79 = Constraint(expr=-m.x92*m.x59 + m.x109 == 0)

m.c80 = Constraint(expr=-m.x92*m.x60 + m.x110 == 0)

m.c81 = Constraint(expr=-m.x92*m.x61 + m.x111 == 0)

m.c82 = Constraint(expr=-m.x93*m.x58 + m.x112 == 0)

m.c83 = Constraint(expr=-m.x93*m.x59 + m.x113 == 0)

m.c84 = Constraint(expr=-m.x93*m.x60 + m.x114 == 0)

m.c85 = Constraint(expr=-m.x93*m.x61 + m.x115 == 0)

m.c86 = Constraint(expr=-m.x94*m.x62 + m.x116 == 0)

m.c87 = Constraint(expr=-m.x94*m.x63 + m.x117 == 0)

m.c88 = Constraint(expr=-m.x94*m.x70 + m.x118 == 0)

m.c89 = Constraint(expr=-m.x94*m.x71 + m.x119 == 0)

m.c90 = Constraint(expr=-m.x94*m.x72 + m.x120 == 0)

m.c91 = Constraint(expr=-m.x94*m.x73 + m.x121 == 0)

m.c92 = Constraint(expr=-m.x95*m.x62 + m.x122 == 0)

m.c93 = Constraint(expr=-m.x95*m.x63 + m.x123 == 0)

m.c94 = Constraint(expr=-m.x95*m.x70 + m.x124 == 0)

m.c95 = Constraint(expr=-m.x95*m.x71 + m.x125 == 0)

m.c96 = Constraint(expr=-m.x95*m.x72 + m.x126 == 0)

m.c97 = Constraint(expr=-m.x95*m.x73 + m.x127 == 0)

m.c98 = Constraint(expr= - m.x56 - m.x74 + m.x82 == 0)

m.c99 = Constraint(expr= - m.x57 - m.x75 + m.x83 == 0)

m.c100 = Constraint(expr= - m.x80 + m.x88 == 0)

m.c101 = Constraint(expr= - m.x81 + m.x89 == 0)

m.c102 = Constraint(expr=   m.x84 - m.x128 == 0)

m.c103 = Constraint(expr=   m.x85 - m.x129 == 0)

m.c104 = Constraint(expr=   m.x86 - m.x130 == 0)

m.c105 = Constraint(expr=   m.x87 - m.x131 == 0)

m.c106 = Constraint(expr=-m.x96*m.x78 + m.x128 == 0)

m.c107 = Constraint(expr=-m.x96*m.x79 + m.x129 == 0)

m.c108 = Constraint(expr=-m.x97*m.x78 + m.x130 == 0)

m.c109 = Constraint(expr=-m.x97*m.x79 + m.x131 == 0)

m.c110 = Constraint(expr=   m.x90 + m.x91 == 1)

m.c111 = Constraint(expr=   m.x92 + m.x93 == 1)

m.c112 = Constraint(expr=   m.x94 + m.x95 == 1)

m.c113 = Constraint(expr=   m.x96 + m.x97 == 1)

m.c114 = Constraint(expr= - m.x56 - m.x57 >= -255)

m.c115 = Constraint(expr= - m.x58 - m.x59 >= -546)

m.c116 = Constraint(expr= - m.x60 - m.x61 >= -1331)

m.c117 = Constraint(expr= - m.x74 - m.x75 >= -1400)

m.c118 = Constraint(expr=   600*m.b25 - m.x62 - m.x63 >= 0)

m.c119 = Constraint(expr=   1509*m.b26 - m.x64 - m.x65 >= 0)

m.c120 = Constraint(expr=   2200*m.b27 - m.x66 - m.x67 >= 0)

m.c121 = Constraint(expr=   900*m.b28 - m.x68 - m.x69 >= 0)

m.c122 = Constraint(expr=   2200*m.b29 - m.x70 - m.x71 >= 0)

m.c123 = Constraint(expr=   950*m.b30 - m.x72 - m.x73 >= 0)

m.c124 = Constraint(expr=   720*m.b31 - m.x76 - m.x77 >= 0)

m.c125 = Constraint(expr=   3000*m.b32 - m.x78 - m.x79 >= 0)

m.c126 = Constraint(expr=   1800*m.b33 - m.x80 - m.x81 >= 0)

m.c127 = Constraint(expr= - m.x82 - m.x83 >= -1400)

m.c128 = Constraint(expr=   2200*m.b34 - m.x84 - m.x85 >= 0)

m.c129 = Constraint(expr=   800*m.b35 - m.x86 - m.x87 >= 0)

m.c130 = Constraint(expr=   1800*m.b36 - m.x88 - m.x89 >= 0)

m.c131 = Constraint(expr= - m.b8 + m.b17 >= 0)

m.c132 = Constraint(expr= - m.b9 + m.b17 >= 0)

m.c133 = Constraint(expr= - m.b10 + m.b21 >= 0)

m.c134 = Constraint(expr= - m.b11 + m.b18 >= 0)

m.c135 = Constraint(expr= - m.b12 + m.b18 >= 0)

m.c136 = Constraint(expr= - m.b13 + m.b18 >= 0)

m.c137 = Constraint(expr= - m.b14 + m.b19 >= 0)

m.c138 = Constraint(expr= - m.b15 + m.b19 >= 0)

m.c139 = Constraint(expr= - m.b16 + m.b22 >= 0)

m.c140 = Constraint(expr=   m.b21 - m.b25 >= 0)

m.c141 = Constraint(expr=   m.b20 - m.b26 >= 0)

m.c142 = Constraint(expr=   m.b20 - m.b27 >= 0)

m.c143 = Constraint(expr=   m.b22 - m.b28 >= 0)

m.c144 = Constraint(expr=   m.b21 - m.b29 >= 0)

m.c145 = Constraint(expr=   m.b21 - m.b30 >= 0)

m.c146 = Constraint(expr=   m.b22 - m.b31 >= 0)

m.c147 = Constraint(expr=   m.b23 - m.b32 >= 0)

m.c148 = Constraint(expr=   m.b24 - m.b33 >= 0)

m.c149 = Constraint(expr=   m.b17 - m.b25 >= 0)

m.c150 = Constraint(expr=   m.b18 - m.b26 >= 0)

m.c151 = Constraint(expr=   m.b19 - m.b27 >= 0)

m.c152 = Constraint(expr=   m.b19 - m.b28 >= 0)

m.c153 = Constraint(expr=   m.b20 - m.b29 >= 0)

m.c154 = Constraint(expr=   m.b21 - m.b31 >= 0)

m.c155 = Constraint(expr=   m.b21 - m.b32 >= 0)

m.c156 = Constraint(expr=   m.b22 - m.b33 >= 0)

m.c157 = Constraint(expr=   m.b23 - m.b34 >= 0)

m.c158 = Constraint(expr=   m.b23 - m.b35 >= 0)

m.c159 = Constraint(expr=   m.b24 - m.b36 >= 0)

m.c160 = Constraint(expr=   m.b8 + m.b9 - m.b17 >= 0)

m.c161 = Constraint(expr=   m.b11 + m.b12 + m.b13 - m.b18 >= 0)

m.c162 = Constraint(expr=   m.b14 + m.b15 - m.b19 >= 0)

m.c163 = Constraint(expr= - m.b20 + m.b26 + m.b27 >= 0)

m.c164 = Constraint(expr=   m.b10 - m.b21 + m.b25 + m.b29 + m.b30 >= 0)

m.c165 = Constraint(expr=   m.b16 - m.b22 + m.b28 + m.b31 >= 0)

m.c166 = Constraint(expr= - m.b23 + m.b32 >= 0)

m.c167 = Constraint(expr= - m.b24 + m.b33 >= 0)

m.c168 = Constraint(expr= - m.b17 + m.b25 >= 0)

m.c169 = Constraint(expr= - m.b18 + m.b26 >= 0)

m.c170 = Constraint(expr= - m.b19 + m.b27 + m.b28 >= 0)

m.c171 = Constraint(expr= - m.b20 + m.b29 >= 0)

m.c172 = Constraint(expr= - m.b21 + m.b31 + m.b32 >= 0)

m.c173 = Constraint(expr= - m.b22 + m.b33 >= 0)

m.c174 = Constraint(expr= - m.b23 + m.b34 + m.b35 >= 0)

m.c175 = Constraint(expr= - m.b24 + m.b36 >= 0)

m.c176 = Constraint(expr= - m.x82 - m.x83 >= -1100)

m.c177 = Constraint(expr=   1800*m.b37 - m.x84 - m.x85 >= 0)

m.c178 = Constraint(expr=   2400*m.b38 - m.x86 - m.x87 - m.x88 - m.x89 >= 0)

m.c179 = Constraint(expr=   0.972*m.x82 - 0.028*m.x83 <= 0)

m.c180 = Constraint(expr=   0.972*m.x84 - 0.028*m.x85 <= 0)

m.c181 = Constraint(expr=   0.972*m.x86 - 0.028*m.x87 + 0.972*m.x88 - 0.028*m.x89 <= 0)

m.c182 = Constraint(expr= - m.b34 + m.b37 >= 0)

m.c183 = Constraint(expr= - m.b35 + m.b38 >= 0)

m.c184 = Constraint(expr= - m.b36 + m.b38 >= 0)

m.c185 = Constraint(expr=   m.b34 - m.b37 >= 0)

m.c186 = Constraint(expr=   m.b35 + m.b36 - m.b38 >= 0)

m.c187 = Constraint(expr=   m.b1 - m.b8 == 0)

m.c188 = Constraint(expr= - m.b8 + m.b17 == 0)

m.c189 = Constraint(expr=   m.b4 - m.b12 == 0)

m.c190 = Constraint(expr= - m.b12 + m.b18 == 0)

m.c191 = Constraint(expr=   m.b6 - m.b14 == 0)

m.c192 = Constraint(expr= - m.b14 + m.b19 == 0)

m.c193 = Constraint(expr=   m.b23 - m.b34 == 0)

m.c194 = Constraint(expr= - m.b34 + m.b37 == 0)

m.c195 = Constraint(expr=   m.b24 - m.b36 == 0)

m.c196 = Constraint(expr= - m.b36 + m.b38 == 0)

m.c197 = Constraint(expr= - m.x43 + m.x102 + m.x104 == 0)

m.c198 = Constraint(expr= - m.x46 + m.x103 + m.x105 == 0)

m.c199 = Constraint(expr= - m.x49 + m.x106 + m.x107 == 0)

m.c200 = Constraint(expr= - m.x53 + m.x98 + m.x100 == 0)

m.c201 = Constraint(expr= - m.x54 + m.x99 + m.x101 == 0)

m.c202 = Constraint(expr= - m.x58 + m.x108 + m.x112 == 0)

m.c203 = Constraint(expr= - m.x59 + m.x109 + m.x113 == 0)

m.c204 = Constraint(expr= - m.x60 + m.x110 + m.x114 == 0)

m.c205 = Constraint(expr= - m.x61 + m.x111 + m.x115 == 0)

m.c206 = Constraint(expr= - m.x62 + m.x116 + m.x122 == 0)

m.c207 = Constraint(expr= - m.x63 + m.x117 + m.x123 == 0)

m.c208 = Constraint(expr= - m.x70 + m.x118 + m.x124 == 0)

m.c209 = Constraint(expr= - m.x71 + m.x119 + m.x125 == 0)

m.c210 = Constraint(expr= - m.x72 + m.x120 + m.x126 == 0)

m.c211 = Constraint(expr= - m.x73 + m.x121 + m.x127 == 0)

m.c212 = Constraint(expr= - m.x78 + m.x128 + m.x130 == 0)

m.c213 = Constraint(expr= - m.x79 + m.x129 + m.x131 == 0)
