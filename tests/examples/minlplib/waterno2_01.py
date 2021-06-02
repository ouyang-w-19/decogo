#  MINLP written by GAMS Convert at 04/21/18 13:55:18
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        205      121       35       49        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        167      158        9        0        0        0        0        0
#  FX      4        4        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        542      441      101        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x27 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x31 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,2.4),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,1.16),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x42 = Var(within=Reals,bounds=(3.5,3.5),initialize=3.5)
m.x43 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x44 = Var(within=Reals,bounds=(4.1,4.1),initialize=4.1)
m.x45 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x46 = Var(within=Reals,bounds=(4,4),initialize=4)
m.x47 = Var(within=Reals,bounds=(2,6),initialize=2)
m.x48 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x49 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x51 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x53 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x55 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x57 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x59 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,0.7),initialize=0)
m.x61 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x63 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,0.58),initialize=0)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(62,65),initialize=62)
m.x67 = Var(within=Reals,bounds=(92.5,95),initialize=92.5)
m.x68 = Var(within=Reals,bounds=(105,109),initialize=105)
m.x69 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x70 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x73 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x75 = Var(within=Reals,bounds=(-125,125),initialize=0)
m.x76 = Var(within=Reals,bounds=(49,49),initialize=49)
m.x77 = Var(within=Reals,bounds=(-49,1000),initialize=0)
m.x78 = Var(within=Reals,bounds=(-65,1000),initialize=0)
m.x79 = Var(within=Reals,bounds=(-95,1000),initialize=0)
m.x80 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x81 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x82 = Var(within=Reals,bounds=(0.2,0.8),initialize=0.2)
m.x83 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x84 = Var(within=Reals,bounds=(0.25,0.5),initialize=0.25)
m.x85 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x86 = Var(within=Reals,bounds=(0.4,0.7),initialize=0.4)
m.x87 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x88 = Var(within=Reals,bounds=(0.24,0.58),initialize=0.24)
m.x89 = Var(within=Reals,bounds=(0.6,1),initialize=0.6)
m.x90 = Var(within=Reals,bounds=(0.8,1),initialize=0.8)
m.x91 = Var(within=Reals,bounds=(0.85,1),initialize=0.85)
m.x92 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x93 = Var(within=Reals,bounds=(100,1000),initialize=100)
m.x94 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x95 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x100 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,54.1717996137183),initialize=0)
m.x105 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x110 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x111 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,93.045051789432),initialize=0)
m.x115 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x117 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x120 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x121 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x123 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,112.384987749469),initialize=0)
m.x125 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x126 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x127 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x128 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x130 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x131 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x132 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x133 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,42.066542469172),initialize=0)
m.x135 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x136 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x137 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x138 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,0.64),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,0.512),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,0.25),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,0.125),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,0.49),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,0.343),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,0.3364),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,0.195112),initialize=0)
m.x160 = Var(within=Reals,bounds=(0.36,1),initialize=0.36)
m.x161 = Var(within=Reals,bounds=(0.216,1),initialize=0.216)
m.x162 = Var(within=Reals,bounds=(0.64,1),initialize=0.64)
m.x163 = Var(within=Reals,bounds=(0.512,1),initialize=0.512)
m.x164 = Var(within=Reals,bounds=(0.7225,1),initialize=0.7225)
m.x165 = Var(within=Reals,bounds=(0.614125,1),initialize=0.614125)
m.x166 = Var(within=Reals,bounds=(0.49,1),initialize=0.49)
m.x167 = Var(within=Reals,bounds=(0.343,1),initialize=0.343)

m.obj = Objective(expr=   m.x94 + m.x99 + m.x104 + m.x109 + m.x114 + m.x119 + m.x124 + m.x129 + m.x134, sense=minimize)

m.c2 = Constraint(expr=   m.x49 + 27.42831624*m.x51 + 37.5407324*m.x53 - 57.2814121*m.x55 == 0)

m.c3 = Constraint(expr= - 57.2814121*m.x55 + m.x57 + 27.42831624*m.x59 + 37.5407324*m.x61 == 0)

m.c4 = Constraint(expr=   37.5407324*m.x11 - 57.2814121*m.x55 + m.x63 + 27.42831624*m.x65 == 0)

m.c5 = Constraint(expr=   m.x12 + 50.37356589*m.x13 + 43.14087708*m.x14 - 76.45219958*m.x15 == 0)

m.c6 = Constraint(expr= - 76.45219958*m.x15 + m.x16 + 50.37356589*m.x17 + 43.14087708*m.x18 == 0)

m.c7 = Constraint(expr=   m.x19 - 25.39911174*m.x20 + 58.31011875*m.x21 - 69.39622571*m.x22 == 0)

m.c8 = Constraint(expr= - 69.39622571*m.x22 + m.x23 - 25.39911174*m.x24 + 58.31011875*m.x25 == 0)

m.c9 = Constraint(expr=   m.x26 + 63.61644904*m.x27 - 2.03724124*m.x28 - 34.92732674*m.x29 == 0)

m.c10 = Constraint(expr= - 34.92732674*m.x29 + m.x30 + 63.61644904*m.x31 - 2.03724124*m.x32 == 0)

m.c11 = Constraint(expr=   m.x33 >= 0.296666667)

m.c12 = Constraint(expr= - m.x34 + m.x35 == 0)

m.c13 = Constraint(expr= - m.x36 + m.x37 == 0)

m.c14 = Constraint(expr=   m.x36 - m.x38 == 0)

m.c15 = Constraint(expr= - m.x39 + m.x40 == 0)

m.c16 = Constraint(expr=   m.x41 == 0.296666667)

m.c17 = Constraint(expr=   m.x33 - m.x35 == 0)

m.c18 = Constraint(expr=   3600*m.x34 - 3600*m.x37 + 1800*m.x42 - 1800*m.x43 == 0)

m.c19 = Constraint(expr=   3600*m.x38 - 3600*m.x40 + 720*m.x44 - 720*m.x45 == 0)

m.c20 = Constraint(expr=   3600*m.x39 - 3600*m.x41 + 1600*m.x46 - 1600*m.x47 == 0)

m.c21 = Constraint(expr= - 0.2*m.b2 + m.x48 >= 0)

m.c22 = Constraint(expr= - 0.2*m.b3 + m.x50 >= 0)

m.c23 = Constraint(expr= - 0.2*m.b4 + m.x52 >= 0)

m.c24 = Constraint(expr= - 0.25*m.b5 + m.x54 >= 0)

m.c25 = Constraint(expr= - 0.25*m.b6 + m.x56 >= 0)

m.c26 = Constraint(expr= - 0.4*m.b7 + m.x58 >= 0)

m.c27 = Constraint(expr= - 0.4*m.b8 + m.x60 >= 0)

m.c28 = Constraint(expr= - 0.24*m.b9 + m.x62 >= 0)

m.c29 = Constraint(expr= - 0.24*m.b10 + m.x64 >= 0)

m.c30 = Constraint(expr= - 0.8*m.b2 + m.x48 <= 0)

m.c31 = Constraint(expr= - 0.8*m.b3 + m.x50 <= 0)

m.c32 = Constraint(expr= - 0.8*m.b4 + m.x52 <= 0)

m.c33 = Constraint(expr= - 0.5*m.b5 + m.x54 <= 0)

m.c34 = Constraint(expr= - 0.5*m.b6 + m.x56 <= 0)

m.c35 = Constraint(expr= - 0.7*m.b7 + m.x58 <= 0)

m.c36 = Constraint(expr= - 0.7*m.b8 + m.x60 <= 0)

m.c37 = Constraint(expr= - 0.58*m.b9 + m.x62 <= 0)

m.c38 = Constraint(expr= - 0.58*m.b10 + m.x64 <= 0)

m.c39 = Constraint(expr= - m.x42 + m.x66 == 60)

m.c40 = Constraint(expr= - m.x44 + m.x67 == 90)

m.c41 = Constraint(expr= - m.x46 + m.x68 == 103)

m.c42 = Constraint(expr= - m.x66 + m.x69 - m.x70 == 0)

m.c43 = Constraint(expr=   m.x71 - m.x72 - m.x73 == 0)

m.c44 = Constraint(expr= - m.x68 + m.x74 - m.x75 == 0)

m.c45 = Constraint(expr=   m.x69 - m.x76 - m.x77 == 0)

m.c46 = Constraint(expr= - m.x66 + m.x71 - m.x78 == 0)

m.c47 = Constraint(expr= - m.x67 + m.x74 - m.x79 == 0)

m.c48 = Constraint(expr=   0.2*m.b2 - m.x48 + m.x80 <= 0.2)

m.c49 = Constraint(expr=   0.2*m.b3 - m.x50 + m.x81 <= 0.2)

m.c50 = Constraint(expr=   0.2*m.b4 - m.x52 + m.x82 <= 0.2)

m.c51 = Constraint(expr=   0.25*m.b5 - m.x54 + m.x83 <= 0.25)

m.c52 = Constraint(expr=   0.25*m.b6 - m.x56 + m.x84 <= 0.25)

m.c53 = Constraint(expr=   0.4*m.b7 - m.x58 + m.x85 <= 0.4)

m.c54 = Constraint(expr=   0.4*m.b8 - m.x60 + m.x86 <= 0.4)

m.c55 = Constraint(expr=   0.24*m.b9 - m.x62 + m.x87 <= 0.24)

m.c56 = Constraint(expr=   0.24*m.b10 - m.x64 + m.x88 <= 0.24)

m.c57 = Constraint(expr= - m.x48 + m.x80 >= 0)

m.c58 = Constraint(expr= - m.x50 + m.x81 >= 0)

m.c59 = Constraint(expr= - m.x52 + m.x82 >= 0)

m.c60 = Constraint(expr= - m.x54 + m.x83 >= 0)

m.c61 = Constraint(expr= - m.x56 + m.x84 >= 0)

m.c62 = Constraint(expr= - m.x58 + m.x85 >= 0)

m.c63 = Constraint(expr= - m.x60 + m.x86 >= 0)

m.c64 = Constraint(expr= - m.x62 + m.x87 >= 0)

m.c65 = Constraint(expr= - m.x64 + m.x88 >= 0)

m.c66 = Constraint(expr= - 0.6*m.b2 + m.x80 <= 0.2)

m.c67 = Constraint(expr= - 0.6*m.b3 + m.x81 <= 0.2)

m.c68 = Constraint(expr= - 0.6*m.b4 + m.x82 <= 0.2)

m.c69 = Constraint(expr= - 0.25*m.b5 + m.x83 <= 0.25)

m.c70 = Constraint(expr= - 0.25*m.b6 + m.x84 <= 0.25)

m.c71 = Constraint(expr= - 0.3*m.b7 + m.x85 <= 0.4)

m.c72 = Constraint(expr= - 0.3*m.b8 + m.x86 <= 0.4)

m.c73 = Constraint(expr= - 0.34*m.b9 + m.x87 <= 0.24)

m.c74 = Constraint(expr= - 0.34*m.b10 + m.x88 <= 0.24)

m.c75 = Constraint(expr= - 0.4*m.b2 + m.x89 <= 0.6)

m.c76 = Constraint(expr= - 0.2*m.b5 + m.x90 <= 0.8)

m.c77 = Constraint(expr= - 0.15*m.b7 + m.x91 <= 0.85)

m.c78 = Constraint(expr= - 0.3*m.b9 + m.x92 <= 0.7)

m.c79 = Constraint(expr=   m.b2 - m.b3 >= 0)

m.c80 = Constraint(expr=   m.b3 - m.b4 >= 0)

m.c81 = Constraint(expr=   m.b5 - m.b6 >= 0)

m.c82 = Constraint(expr=   m.b7 - m.b8 >= 0)

m.c83 = Constraint(expr=   m.b9 - m.b10 >= 0)

m.c84 = Constraint(expr=   m.x35 - m.x48 - m.x50 - m.x52 == 0)

m.c85 = Constraint(expr=   m.x37 - m.x54 - m.x56 - m.x58 - m.x60 == 0)

m.c86 = Constraint(expr=   m.x40 - m.x62 - m.x64 == 0)

m.c87 = Constraint(expr= - 2000*m.b2 + m.x49 - m.x77 >= -2000)

m.c88 = Constraint(expr= - 2000*m.b3 + m.x57 - m.x77 >= -2000)

m.c89 = Constraint(expr= - 2000*m.b4 + m.x63 - m.x77 >= -2000)

m.c90 = Constraint(expr= - 2000*m.b5 + m.x12 - m.x78 >= -2000)

m.c91 = Constraint(expr= - 2000*m.b6 + m.x16 - m.x78 >= -2000)

m.c92 = Constraint(expr= - 2000*m.b7 + m.x19 - m.x78 >= -2000)

m.c93 = Constraint(expr= - 2000*m.b8 + m.x23 - m.x78 >= -2000)

m.c94 = Constraint(expr= - 2000*m.b9 + m.x26 - m.x79 >= -2000)

m.c95 = Constraint(expr= - 2000*m.b10 + m.x30 - m.x79 >= -2000)

m.c96 = Constraint(expr=   1049*m.b2 + m.x49 - m.x77 <= 1049)

m.c97 = Constraint(expr=   1049*m.b3 + m.x57 - m.x77 <= 1049)

m.c98 = Constraint(expr=   1049*m.b4 + m.x63 - m.x77 <= 1049)

m.c99 = Constraint(expr=   1065*m.b5 + m.x12 - m.x78 <= 1065)

m.c100 = Constraint(expr=   1065*m.b6 + m.x16 - m.x78 <= 1065)

m.c101 = Constraint(expr=   1065*m.b7 + m.x19 - m.x78 <= 1065)

m.c102 = Constraint(expr=   1065*m.b8 + m.x23 - m.x78 <= 1065)

m.c103 = Constraint(expr=   1095*m.b9 + m.x26 - m.x79 <= 1095)

m.c104 = Constraint(expr=   1095*m.b10 + m.x30 - m.x79 <= 1095)

m.c105 = Constraint(expr= - m.x67 + m.x72 >= 0)

m.c106 = Constraint(expr=   m.x68 - m.x93 >= 0)

m.c107 = Constraint(expr= - 0.309838295393634*m.x94 + 13.94696158*m.x95 + 24.46510819*m.x96 - 7.28623839*m.x97
                          - 23.57687014*m.x98 <= 0)

m.c108 = Constraint(expr= - 0.309838295393634*m.x99 + 13.94696158*m.x100 + 24.46510819*m.x101 - 7.28623839*m.x102
                          - 23.57687014*m.x103 <= 0)

m.c109 = Constraint(expr= - 0.309838295393634*m.x104 + 13.94696158*m.x105 + 24.46510819*m.x106 - 7.28623839*m.x107
                          - 23.57687014*m.x108 <= 0)

m.c110 = Constraint(expr= - 0.309838295393634*m.x109 + 29.29404529*m.x110 - 108.39408287*m.x111 + 442.21990639*m.x112
                          - 454.58448169*m.x113 <= 0)

m.c111 = Constraint(expr= - 0.309838295393634*m.x114 + 29.29404529*m.x115 - 108.39408287*m.x116 + 442.21990639*m.x117
                          - 454.58448169*m.x118 <= 0)

m.c112 = Constraint(expr= - 0.309838295393634*m.x119 + 25.92674585*m.x120 + 18.13482123*m.x121 + 22.12766012*m.x122
                          - 42.68950769*m.x123 <= 0)

m.c113 = Constraint(expr= - 0.309838295393634*m.x124 + 25.92674585*m.x125 + 18.13482123*m.x126 + 22.12766012*m.x127
                          - 42.68950769*m.x128 <= 0)

m.c114 = Constraint(expr= - 0.309838295393634*m.x129 + 17.4714791*m.x130 - 39.98407808*m.x131 + 134.55943082*m.x132
                          - 135.88441782*m.x133 <= 0)

m.c115 = Constraint(expr= - 0.309838295393634*m.x134 + 17.4714791*m.x135 - 39.98407808*m.x136 + 134.55943082*m.x137
                          - 135.88441782*m.x138 <= 0)

m.c116 = Constraint(expr=m.x34**2 - m.x139 == 0)

m.c117 = Constraint(expr=   m.x70 - 5*m.x139 == 0)

m.c118 = Constraint(expr=m.x36**2 - m.x140 == 0)

m.c119 = Constraint(expr=   m.x73 - 4*m.x140 == 0)

m.c120 = Constraint(expr=m.x39**2 - m.x141 == 0)

m.c121 = Constraint(expr=   m.x75 - 5*m.x141 == 0)

m.c122 = Constraint(expr=m.x48**2 - m.x142 == 0)

m.c123 = Constraint(expr=   m.x51 - m.x142 == 0)

m.c124 = Constraint(expr=m.x48**3 - m.x143 == 0)

m.c125 = Constraint(expr=   m.x98 - m.x143 == 0)

m.c126 = Constraint(expr=m.x50**2 - m.x144 == 0)

m.c127 = Constraint(expr=   m.x59 - m.x144 == 0)

m.c128 = Constraint(expr=m.x50**3 - m.x145 == 0)

m.c129 = Constraint(expr=   m.x103 - m.x145 == 0)

m.c130 = Constraint(expr=m.x52**2 - m.x146 == 0)

m.c131 = Constraint(expr=   m.x65 - m.x146 == 0)

m.c132 = Constraint(expr=m.x52**3 - m.x147 == 0)

m.c133 = Constraint(expr=   m.x108 - m.x147 == 0)

m.c134 = Constraint(expr=m.x54**2 - m.x148 == 0)

m.c135 = Constraint(expr=   m.x13 - m.x148 == 0)

m.c136 = Constraint(expr=m.x54**3 - m.x149 == 0)

m.c137 = Constraint(expr=   m.x113 - m.x149 == 0)

m.c138 = Constraint(expr=m.x56**2 - m.x150 == 0)

m.c139 = Constraint(expr=   m.x17 - m.x150 == 0)

m.c140 = Constraint(expr=m.x56**3 - m.x151 == 0)

m.c141 = Constraint(expr=   m.x118 - m.x151 == 0)

m.c142 = Constraint(expr=m.x58**2 - m.x152 == 0)

m.c143 = Constraint(expr=   m.x20 - m.x152 == 0)

m.c144 = Constraint(expr=m.x58**3 - m.x153 == 0)

m.c145 = Constraint(expr=   m.x123 - m.x153 == 0)

m.c146 = Constraint(expr=m.x60**2 - m.x154 == 0)

m.c147 = Constraint(expr=   m.x24 - m.x154 == 0)

m.c148 = Constraint(expr=m.x60**3 - m.x155 == 0)

m.c149 = Constraint(expr=   m.x128 - m.x155 == 0)

m.c150 = Constraint(expr=m.x62**2 - m.x156 == 0)

m.c151 = Constraint(expr=   m.x27 - m.x156 == 0)

m.c152 = Constraint(expr=m.x62**3 - m.x157 == 0)

m.c153 = Constraint(expr=   m.x133 - m.x157 == 0)

m.c154 = Constraint(expr=m.x64**2 - m.x158 == 0)

m.c155 = Constraint(expr=   m.x31 - m.x158 == 0)

m.c156 = Constraint(expr=m.x64**3 - m.x159 == 0)

m.c157 = Constraint(expr=   m.x138 - m.x159 == 0)

m.c158 = Constraint(expr=m.x48*m.x89 - m.x53 == 0)

m.c159 = Constraint(expr=m.x89*m.x142 - m.x97 == 0)

m.c160 = Constraint(expr=m.x50*m.x89 - m.x61 == 0)

m.c161 = Constraint(expr=m.x89*m.x144 - m.x102 == 0)

m.c162 = Constraint(expr=m.x52*m.x89 - m.x11 == 0)

m.c163 = Constraint(expr=m.x89*m.x146 - m.x107 == 0)

m.c164 = Constraint(expr=m.x89**2 - m.x160 == 0)

m.c165 = Constraint(expr=   m.x55 - m.x160 == 0)

m.c166 = Constraint(expr=m.x48*m.x160 - m.x96 == 0)

m.c167 = Constraint(expr=m.x50*m.x160 - m.x101 == 0)

m.c168 = Constraint(expr=m.x52*m.x160 - m.x106 == 0)

m.c169 = Constraint(expr=m.x89**3 - m.x161 == 0)

m.c170 = Constraint(expr=m.b2*m.x161 - m.x95 == 0)

m.c171 = Constraint(expr=m.b3*m.x161 - m.x100 == 0)

m.c172 = Constraint(expr=m.b4*m.x161 - m.x105 == 0)

m.c173 = Constraint(expr=m.x54*m.x90 - m.x14 == 0)

m.c174 = Constraint(expr=m.x90*m.x148 - m.x112 == 0)

m.c175 = Constraint(expr=m.x56*m.x90 - m.x18 == 0)

m.c176 = Constraint(expr=m.x90*m.x150 - m.x117 == 0)

m.c177 = Constraint(expr=m.x90**2 - m.x162 == 0)

m.c178 = Constraint(expr=   m.x15 - m.x162 == 0)

m.c179 = Constraint(expr=m.x54*m.x162 - m.x111 == 0)

m.c180 = Constraint(expr=m.x56*m.x162 - m.x116 == 0)

m.c181 = Constraint(expr=m.x90**3 - m.x163 == 0)

m.c182 = Constraint(expr=m.b5*m.x163 - m.x110 == 0)

m.c183 = Constraint(expr=m.b6*m.x163 - m.x115 == 0)

m.c184 = Constraint(expr=m.x58*m.x91 - m.x21 == 0)

m.c185 = Constraint(expr=m.x91*m.x152 - m.x122 == 0)

m.c186 = Constraint(expr=m.x60*m.x91 - m.x25 == 0)

m.c187 = Constraint(expr=m.x91*m.x154 - m.x127 == 0)

m.c188 = Constraint(expr=m.x91**2 - m.x164 == 0)

m.c189 = Constraint(expr=   m.x22 - m.x164 == 0)

m.c190 = Constraint(expr=m.x58*m.x164 - m.x121 == 0)

m.c191 = Constraint(expr=m.x60*m.x164 - m.x126 == 0)

m.c192 = Constraint(expr=m.x91**3 - m.x165 == 0)

m.c193 = Constraint(expr=m.b7*m.x165 - m.x120 == 0)

m.c194 = Constraint(expr=m.b8*m.x165 - m.x125 == 0)

m.c195 = Constraint(expr=m.x62*m.x92 - m.x28 == 0)

m.c196 = Constraint(expr=m.x92*m.x156 - m.x132 == 0)

m.c197 = Constraint(expr=m.x64*m.x92 - m.x32 == 0)

m.c198 = Constraint(expr=m.x92*m.x158 - m.x137 == 0)

m.c199 = Constraint(expr=m.x92**2 - m.x166 == 0)

m.c200 = Constraint(expr=   m.x29 - m.x166 == 0)

m.c201 = Constraint(expr=m.x62*m.x166 - m.x131 == 0)

m.c202 = Constraint(expr=m.x64*m.x166 - m.x136 == 0)

m.c203 = Constraint(expr=m.x92**3 - m.x167 == 0)

m.c204 = Constraint(expr=m.b9*m.x167 - m.x130 == 0)

m.c205 = Constraint(expr=m.b10*m.x167 - m.x135 == 0)
