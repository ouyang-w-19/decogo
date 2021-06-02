#  MINLP written by GAMS Convert at 04/21/18 13:55:05
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        168      116        1       51        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        146      118       28        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        467      457       10        0
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
m.x47 = Var(within=Reals,bounds=(0,29.2),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,1.2),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=215.581)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=1.237)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=109.57)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(353.66,None),initialize=353.66)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=1.854)
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
m.x76 = Var(within=Reals,bounds=(32.8,None),initialize=32.8)
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
m.x93 = Var(within=Reals,bounds=(24.1,None),initialize=24.1)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,21),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(1.2,2.2),initialize=1.2)
m.x98 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,98.72),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(8.7,None),initialize=8.7)
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

m.obj = Objective(expr=   87.3969*m.x29 + 0.03781*m.x30 + 0.03781*m.x31 + 0.03781*m.x32 + 0.03781*m.x33 + 0.03781*m.x34
                        + 0.03781*m.x35 + 0.03781*m.x36 + 0.03781*m.x37 + 0.03781*m.x38 + 0.03781*m.x39 + 0.03781*m.x40
                        + 0.03781*m.x41 + 0.03781*m.x42 + 0.03781*m.x43 + 0.3*m.x44 + 0.017*m.x45, sense=minimize)

m.c1 = Constraint(expr=m.x53*m.x49 + m.x52*m.x51 - 0.5439*m.x44 - 0.5439*m.x46 - 1.22963*m.x47 - 2.74289*m.x48
                        - 6.94492*m.x50 == 0)

m.c2 = Constraint(expr=m.x53*m.x54 - 3.22692*m.x55 - 9.05971*m.x56 + m.x57 - m.x58 == 0)

m.c3 = Constraint(expr=m.x53*m.x59 + 7.32917*m.x60 + 7.70075*m.x61 - 7.31039*m.x62 - 7.31039*m.x63 - 7.31039*m.x64
                        - 7.31039*m.x65 - 7.31039*m.x66 - 7.31039*m.x67 - 7.31039*m.x68 - 7.31039*m.x69 - 7.31039*m.x70
                        - 7.31039*m.x71 - 7.31039*m.x72 - 7.31039*m.x73 - 7.31039*m.x74 - 7.31039*m.x75 - 7.31039*m.x76
                        == 0)

m.c4 = Constraint(expr=m.x53*m.x77 - 6.94492*m.x50 + 7.31039*m.x62 + 7.03739*m.x78 + 7.03739*m.x79 + 6.91604*m.x80
                        + 6.91604*m.x81 + 6.91604*m.x82 + 6.91604*m.x83 + 6.91604*m.x84 + 6.91604*m.x85 + 6.91604*m.x86
                        + 6.91604*m.x87 + 6.91604*m.x88 + 6.91604*m.x89 + 6.91604*m.x90 + 6.91604*m.x91 - 6.94492*m.x92
                        - 6.94492*m.x93 == 0)

m.c5 = Constraint(expr= - m.x44 - m.x46 - m.x47 - m.x48 + m.x49 - m.x50 + m.x51 == 0)

m.c6 = Constraint(expr=   m.x44 - m.x94 - m.x95 == 0)

m.c7 = Constraint(expr= - 0.08*m.x50 + m.x51 == 0)

m.c8 = Constraint(expr=   0.05391*m.x96 - m.x97 == 4.45329)

m.c9 = Constraint(expr=   m.x52 - 0.34851*m.x53 == 6.04388)

m.c10 = Constraint(expr=   m.x53 - 0.18673*m.x97 == 0.82639)

m.c11 = Constraint(expr=   m.x49 - m.x54 - m.x59 - m.x77 - m.x98 == 0)

m.c12 = Constraint(expr=   m.x98 >= 104.21999)

m.c13 = Constraint(expr= - 0.5*m.x49 + m.x99 == 0)

m.c14 = Constraint(expr= - 1.89474*m.x99 + m.x100 == 230)

m.c15 = Constraint(expr=   m.x100 - m.x101 == 0)

m.c16 = Constraint(expr=   m.x54 - m.x55 - m.x56 == 0)

m.c17 = Constraint(expr= - 0.05*m.x54 + m.x55 == 0)

m.c18 = Constraint(expr= - 116.41403*m.x29 + m.x57 == 0)

m.c19 = Constraint(expr=   m.x29 - m.x102 == 4.035)

m.c20 = Constraint(expr= - 23.39292*m.x102 + m.x103 == 0)

m.c21 = Constraint(expr= - 3.61341*m.x103 + m.x104 == 0)

m.c22 = Constraint(expr=   m.x56 - m.x61 + m.x105 - m.x106 - m.x107 - m.x108 - m.x109 - m.x110 == 0)

m.c23 = Constraint(expr=   m.x59 + m.x60 + m.x61 - m.x62 - m.x63 - m.x64 - m.x65 - m.x66 - m.x67 - m.x68 - m.x69 - m.x70
                         - m.x71 - m.x72 - m.x73 - m.x74 - m.x75 - m.x76 == 0)

m.c24 = Constraint(expr= - m.x50 + m.x62 + m.x77 + m.x78 + m.x79 + m.x80 + m.x81 + m.x82 + m.x83 + m.x84 + m.x85 + m.x86
                         + m.x87 + m.x88 + m.x89 + m.x90 + m.x91 - m.x92 - m.x93 == 0)

m.c25 = Constraint(expr= - m.x46 + m.x111 + m.x112 == 0)

m.c26 = Constraint(expr=   m.x106 - m.x113 == 0)

m.c27 = Constraint(expr= - m.x60 + m.x107 == 0)

m.c28 = Constraint(expr= - m.x78 + m.x108 == 0)

m.c29 = Constraint(expr= - m.x79 + m.x109 == 0)

m.c30 = Constraint(expr=   7.70075*m.x106 - 6.08959*m.x113 - 0.00641*m.x114 == 0)

m.c31 = Constraint(expr= - 7.32917*m.x60 + 7.70075*m.x107 - 0.00641*m.x115 == 0)

m.c32 = Constraint(expr= - 7.03739*m.x78 + 7.70075*m.x108 - 0.00641*m.x116 == 0)

m.c33 = Constraint(expr= - 7.03739*m.x79 + 7.70075*m.x109 - 0.00641*m.x117 == 0)

m.c34 = Constraint(expr=   m.x63 - m.x80 == 0)

m.c35 = Constraint(expr=   m.x64 - m.x81 == 0)

m.c36 = Constraint(expr=   m.x65 - m.x82 == 0)

m.c37 = Constraint(expr=   m.x66 - m.x118 == 0)

m.c38 = Constraint(expr=   m.x67 - m.x83 == 0)

m.c39 = Constraint(expr=   m.x68 - m.x84 == 0)

m.c40 = Constraint(expr=   m.x69 - m.x85 == 0)

m.c41 = Constraint(expr=   m.x70 - m.x86 == 0)

m.c42 = Constraint(expr=   m.x71 - m.x87 == 0)

m.c43 = Constraint(expr=   m.x72 - m.x88 == 0)

m.c44 = Constraint(expr=   m.x73 - m.x89 == 0)

m.c45 = Constraint(expr=   m.x74 - m.x90 == 0)

m.c46 = Constraint(expr=   m.x75 - m.x91 == 0)

m.c47 = Constraint(expr=   7.31039*m.x63 - 6.91604*m.x80 - 0.00641*m.x119 == 0)

m.c48 = Constraint(expr=   7.31039*m.x64 - 6.91604*m.x81 - 0.00641*m.x120 == 0)

m.c49 = Constraint(expr=   7.31039*m.x65 - 6.91604*m.x82 - 0.00641*m.x121 == 0)

m.c50 = Constraint(expr=   7.31039*m.x66 - 5.77083*m.x118 - 0.00641*m.x122 == 0)

m.c51 = Constraint(expr=   7.31039*m.x67 - 6.91604*m.x83 - 0.00641*m.x123 == 0)

m.c52 = Constraint(expr=   7.31039*m.x68 - 6.91604*m.x84 - 0.00641*m.x124 == 0)

m.c53 = Constraint(expr=   7.31039*m.x69 - 6.91604*m.x85 - 0.00641*m.x125 == 0)

m.c54 = Constraint(expr=   7.31039*m.x70 - 6.91604*m.x86 - 0.00641*m.x126 == 0)

m.c55 = Constraint(expr=   7.31039*m.x71 - 6.91604*m.x87 - 0.00641*m.x127 == 0)

m.c56 = Constraint(expr=   7.31039*m.x72 - 6.91604*m.x88 - 0.00641*m.x128 == 0)

m.c57 = Constraint(expr=   7.31039*m.x73 - 6.91604*m.x89 - 0.00641*m.x129 == 0)

m.c58 = Constraint(expr=   7.31039*m.x74 - 6.91604*m.x90 - 0.00641*m.x130 == 0)

m.c59 = Constraint(expr=   7.31039*m.x75 - 6.91604*m.x91 - 0.00641*m.x131 == 0)

m.c60 = Constraint(expr=   m.x111 - m.x113 == 0)

m.c61 = Constraint(expr=   m.x112 - m.x118 == 0)

m.c62 = Constraint(expr=   5.6972*m.x111 - 0.12983*m.x132 == 0)

m.c63 = Constraint(expr=   5.6972*m.x112 - 0.12983*m.x133 == 0)

m.c64 = Constraint(expr=   m.x45 - m.x132 - m.x133 == 4117)

m.c65 = Constraint(expr= - 0.33333*m.x45 + m.x134 == 0)

m.c66 = Constraint(expr= - 0.20286*m.x134 + m.x135 == 0)

m.c67 = Constraint(expr=   m.x135 - m.x136 == 0)

m.c68 = Constraint(expr=   m.x135 - m.x137 == 0)

m.c69 = Constraint(expr=   m.x138 == 1)

m.c70 = Constraint(expr=   m.x139 == 1)

m.c71 = Constraint(expr=   m.x140 == 1)

m.c72 = Constraint(expr=   m.x141 == 1)

m.c73 = Constraint(expr=   m.x138 - m.x142 == 0)

m.c74 = Constraint(expr=   m.x138 - m.x143 == 0)

m.c75 = Constraint(expr=   m.x139 - m.x144 == 0)

m.c76 = Constraint(expr=   0.01*m.x111 - 100*m.x144 <= 0)

m.c77 = Constraint(expr=   m.x141 - m.x145 == 0)

m.c78 = Constraint(expr=   0.01*m.x112 - 100*m.x145 <= 0)

m.c79 = Constraint(expr=   0.1*m.x49 - 100*m.x142 <= 0)

m.c80 = Constraint(expr=   0.1*m.x103 - 100*m.x143 <= 0)

m.c81 = Constraint(expr=   0.1*m.x56 - 100*m.x138 <= 0)

m.c82 = Constraint(expr=   0.1*m.x106 - 100*m.x139 <= 0)

m.c83 = Constraint(expr=   0.1*m.x107 - 100*m.x140 <= 0)

m.c84 = Constraint(expr= - 100*m.b1 + 0.1*m.x108 <= 0)

m.c85 = Constraint(expr= - 100*m.b2 + 0.1*m.x109 <= 0)

m.c86 = Constraint(expr=   0.1*m.x60 - 100*m.x140 <= 0)

m.c87 = Constraint(expr= - 100*m.b1 + 0.1*m.x78 <= 0)

m.c88 = Constraint(expr= - 100*m.b2 + 0.1*m.x79 <= 0)

m.c89 = Constraint(expr=   0.1*m.x113 - 100*m.x139 <= 0)

m.c90 = Constraint(expr= - 100*m.b3 + 0.1*m.x63 <= 0)

m.c91 = Constraint(expr= - 100*m.b4 + 0.1*m.x64 <= 0)

m.c92 = Constraint(expr= - m.b5 + 0.1*m.x65 <= 0)

m.c93 = Constraint(expr=   0.1*m.x66 - 100*m.x141 <= 0)

m.c94 = Constraint(expr= - 100*m.b6 + 0.1*m.x67 <= 0)

m.c95 = Constraint(expr= - 100*m.b7 + 0.1*m.x68 <= 0)

m.c96 = Constraint(expr= - 100*m.b8 + 0.1*m.x69 <= 0)

m.c97 = Constraint(expr= - 100*m.b9 + 0.1*m.x70 <= 0)

m.c98 = Constraint(expr= - 100*m.b10 + 0.1*m.x71 <= 0)

m.c99 = Constraint(expr= - 100*m.b11 + 0.1*m.x72 <= 0)

m.c100 = Constraint(expr= - 100*m.b12 + 0.1*m.x73 <= 0)

m.c101 = Constraint(expr= - 100*m.b13 + 0.1*m.x74 <= 0)

m.c102 = Constraint(expr= - 100*m.b14 + 0.1*m.x75 <= 0)

m.c103 = Constraint(expr= - 100*m.b3 + 0.1*m.x80 <= 0)

m.c104 = Constraint(expr= - 100*m.b4 + 0.1*m.x81 <= 0)

m.c105 = Constraint(expr= - 100*m.b5 + 0.1*m.x82 <= 0)

m.c106 = Constraint(expr= - 100*m.b6 + 0.1*m.x83 <= 0)

m.c107 = Constraint(expr= - 100*m.b7 + 0.1*m.x84 <= 0)

m.c108 = Constraint(expr= - 100*m.b8 + 0.1*m.x85 <= 0)

m.c109 = Constraint(expr= - 100*m.b9 + 0.1*m.x86 <= 0)

m.c110 = Constraint(expr= - 100*m.b10 + 0.1*m.x87 <= 0)

m.c111 = Constraint(expr= - 100*m.b11 + 0.1*m.x88 <= 0)

m.c112 = Constraint(expr= - 100*m.b12 + 0.1*m.x89 <= 0)

m.c113 = Constraint(expr= - 100*m.b13 + 0.1*m.x90 <= 0)

m.c114 = Constraint(expr= - 100*m.b14 + 0.1*m.x91 <= 0)

m.c115 = Constraint(expr=   0.1*m.x118 - 100*m.x141 <= 0)

m.c116 = Constraint(expr=   0.01*m.x114 - 163.03*m.x139 == 0)

m.c117 = Constraint(expr=   0.01*m.x115 - 56*m.x140 == 0)

m.c118 = Constraint(expr= - 444*m.b3 + m.x119 == 0)

m.c119 = Constraint(expr= - 100*m.b4 + m.x120 == 0)

m.c120 = Constraint(expr= - 125*m.b5 + m.x121 == 0)

m.c121 = Constraint(expr=   0.01*m.x122 - 94.5*m.x141 == 0)

m.c122 = Constraint(expr= - 75*m.b6 + m.x123 == 0)

m.c123 = Constraint(expr= - 60*m.b7 + m.x124 == 0)

m.c124 = Constraint(expr= - 36*m.b8 + m.x125 == 0)

m.c125 = Constraint(expr= - 26*m.b9 + m.x126 == 0)

m.c126 = Constraint(expr= - 445*m.b10 + m.x127 == 0)

m.c127 = Constraint(expr= - 444*m.b15 + m.x30 == 0)

m.c128 = Constraint(expr= - 100*m.b16 + m.x31 == 0)

m.c129 = Constraint(expr= - 125*m.b17 + m.x32 == 0)

m.c130 = Constraint(expr= - 75*m.b18 + m.x33 == 0)

m.c131 = Constraint(expr= - 60*m.b19 + m.x34 == 0)

m.c132 = Constraint(expr= - 36*m.b20 + m.x35 == 0)

m.c133 = Constraint(expr= - 26*m.b21 + m.x36 == 0)

m.c134 = Constraint(expr= - 445*m.b22 + m.x37 == 0)

m.c135 = Constraint(expr= - 300*m.b1 + 0.01*m.x116 <= 0)

m.c136 = Constraint(expr= - 300*m.b2 + 0.01*m.x117 <= 0)

m.c137 = Constraint(expr= - 300*m.b11 + 0.01*m.x128 <= 0)

m.c138 = Constraint(expr= - 300*m.b12 + 0.01*m.x129 <= 0)

m.c139 = Constraint(expr= - 300*m.b13 + 0.01*m.x130 <= 0)

m.c140 = Constraint(expr= - 300*m.b14 + 0.01*m.x131 <= 0)

m.c141 = Constraint(expr= - 300*m.b23 + 0.01*m.x38 <= 0)

m.c142 = Constraint(expr= - 300*m.b24 + 0.01*m.x39 <= 0)

m.c143 = Constraint(expr= - 300*m.b25 + 0.01*m.x40 <= 0)

m.c144 = Constraint(expr= - 300*m.b26 + 0.01*m.x41 <= 0)

m.c145 = Constraint(expr= - 300*m.b27 + 0.01*m.x42 <= 0)

m.c146 = Constraint(expr= - 300*m.b28 + 0.01*m.x43 <= 0)

m.c147 = Constraint(expr=   m.x38 - m.x100 + m.x116 == 0)

m.c148 = Constraint(expr=   m.x39 - m.x101 + m.x117 == 0)

m.c149 = Constraint(expr=   m.x40 - m.x104 + m.x128 == 0)

m.c150 = Constraint(expr=   m.x41 + m.x129 - m.x135 == 0)

m.c151 = Constraint(expr=   m.x42 + m.x130 - m.x136 == 0)

m.c152 = Constraint(expr=   m.x43 + m.x131 - m.x137 == 0)

m.c153 = Constraint(expr=   m.b1 + m.b23 == 1)

m.c154 = Constraint(expr=   m.b2 + m.b24 == 1)

m.c155 = Constraint(expr=   m.b3 + m.b15 == 1)

m.c156 = Constraint(expr=   m.b4 + m.b16 == 1)

m.c157 = Constraint(expr=   m.b5 + m.b17 == 1)

m.c158 = Constraint(expr=   m.b6 + m.b18 == 1)

m.c159 = Constraint(expr=   m.b7 + m.b19 == 1)

m.c160 = Constraint(expr=   m.b8 + m.b20 == 1)

m.c161 = Constraint(expr=   m.b9 + m.b21 == 1)

m.c162 = Constraint(expr=   m.b10 + m.b22 == 1)

m.c163 = Constraint(expr=   m.b11 + m.b25 == 1)

m.c164 = Constraint(expr=   m.b12 + m.b26 == 1)

m.c165 = Constraint(expr=   m.b13 + m.b27 == 1)

m.c166 = Constraint(expr=   m.b14 + m.b28 == 1)

m.c167 = Constraint(expr=   m.b14 + m.b24 == 0)
