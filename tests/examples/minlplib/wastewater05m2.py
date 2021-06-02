#  NLP written by GAMS Convert at 04/21/18 13:55:06
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        152      140        0       12        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        134      134        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        551      455       96        0
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

m.obj = Objective(expr=   m.x26 + m.x27 + m.x28, sense=minimize)

m.c2 = Constraint(expr= - m.x10 - m.x16 - m.x17 - m.x18 == -13.1)

m.c3 = Constraint(expr= - m.x11 - m.x19 - m.x20 - m.x21 == -32.7)

m.c4 = Constraint(expr= - m.x12 - m.x22 - m.x23 - m.x24 == -56.5)

m.c5 = Constraint(expr= - m.x1 - m.x4 - m.x7 - m.x16 - m.x19 - m.x22 + m.x26 == 0)

m.c6 = Constraint(expr= - m.x2 - m.x5 - m.x8 - m.x17 - m.x20 - m.x23 + m.x27 == 0)

m.c7 = Constraint(expr= - m.x3 - m.x6 - m.x9 - m.x18 - m.x21 - m.x24 + m.x28 == 0)

m.c8 = Constraint(expr= - m.x1 - m.x2 - m.x3 - m.x13 + m.x26 == 0)

m.c9 = Constraint(expr= - m.x4 - m.x5 - m.x6 - m.x14 + m.x27 == 0)

m.c10 = Constraint(expr= - m.x7 - m.x8 - m.x9 - m.x15 + m.x28 == 0)

m.c11 = Constraint(expr= - m.x10 - m.x11 - m.x12 - m.x13 - m.x14 - m.x15 + m.x25 == 0)

m.c12 = Constraint(expr= - m.x56 - m.x74 - m.x77 - m.x80 == -131)

m.c13 = Constraint(expr= - m.x57 - m.x75 - m.x78 - m.x81 == -5109)

m.c14 = Constraint(expr= - m.x58 - m.x76 - m.x79 - m.x82 == -327.5)

m.c15 = Constraint(expr= - m.x59 - m.x83 - m.x86 - m.x89 == -3597)

m.c16 = Constraint(expr= - m.x60 - m.x84 - m.x87 - m.x90 == -548706)

m.c17 = Constraint(expr= - m.x61 - m.x85 - m.x88 - m.x91 == -1308)

m.c18 = Constraint(expr= - m.x62 - m.x92 - m.x95 - m.x98 == -5650)

m.c19 = Constraint(expr= - m.x63 - m.x93 - m.x96 - m.x99 == -1412.5)

m.c20 = Constraint(expr= - m.x64 - m.x94 - m.x97 - m.x100 == -1977.5)

m.c21 = Constraint(expr= - m.x74 + 131*m.x125 == 0)

m.c22 = Constraint(expr= - m.x75 + 5109*m.x125 == 0)

m.c23 = Constraint(expr= - m.x76 + 327.5*m.x125 == 0)

m.c24 = Constraint(expr= - m.x77 + 131*m.x126 == 0)

m.c25 = Constraint(expr= - m.x78 + 5109*m.x126 == 0)

m.c26 = Constraint(expr= - m.x79 + 327.5*m.x126 == 0)

m.c27 = Constraint(expr= - m.x80 + 131*m.x127 == 0)

m.c28 = Constraint(expr= - m.x81 + 5109*m.x127 == 0)

m.c29 = Constraint(expr= - m.x82 + 327.5*m.x127 == 0)

m.c30 = Constraint(expr= - m.x83 + 3597*m.x128 == 0)

m.c31 = Constraint(expr= - m.x84 + 548706*m.x128 == 0)

m.c32 = Constraint(expr= - m.x85 + 1308*m.x128 == 0)

m.c33 = Constraint(expr= - m.x86 + 3597*m.x129 == 0)

m.c34 = Constraint(expr= - m.x87 + 548706*m.x129 == 0)

m.c35 = Constraint(expr= - m.x88 + 1308*m.x129 == 0)

m.c36 = Constraint(expr= - m.x89 + 3597*m.x130 == 0)

m.c37 = Constraint(expr= - m.x90 + 548706*m.x130 == 0)

m.c38 = Constraint(expr= - m.x91 + 1308*m.x130 == 0)

m.c39 = Constraint(expr= - m.x92 + 5650*m.x131 == 0)

m.c40 = Constraint(expr= - m.x93 + 1412.5*m.x131 == 0)

m.c41 = Constraint(expr= - m.x94 + 1977.5*m.x131 == 0)

m.c42 = Constraint(expr= - m.x95 + 5650*m.x132 == 0)

m.c43 = Constraint(expr= - m.x96 + 1412.5*m.x132 == 0)

m.c44 = Constraint(expr= - m.x97 + 1977.5*m.x132 == 0)

m.c45 = Constraint(expr= - m.x98 + 5650*m.x133 == 0)

m.c46 = Constraint(expr= - m.x99 + 1412.5*m.x133 == 0)

m.c47 = Constraint(expr= - m.x100 + 1977.5*m.x133 == 0)

m.c48 = Constraint(expr= - m.x56 + 131*m.x119 == 0)

m.c49 = Constraint(expr= - m.x57 + 5109*m.x119 == 0)

m.c50 = Constraint(expr= - m.x58 + 327.5*m.x119 == 0)

m.c51 = Constraint(expr= - m.x59 + 3597*m.x120 == 0)

m.c52 = Constraint(expr= - m.x60 + 548706*m.x120 == 0)

m.c53 = Constraint(expr= - m.x61 + 1308*m.x120 == 0)

m.c54 = Constraint(expr= - m.x62 + 5650*m.x121 == 0)

m.c55 = Constraint(expr= - m.x63 + 1412.5*m.x121 == 0)

m.c56 = Constraint(expr= - m.x64 + 1977.5*m.x121 == 0)

m.c57 = Constraint(expr= - m.x16 + 13.1*m.x125 == 0)

m.c58 = Constraint(expr= - m.x17 + 13.1*m.x126 == 0)

m.c59 = Constraint(expr= - m.x18 + 13.1*m.x127 == 0)

m.c60 = Constraint(expr= - m.x19 + 32.7*m.x128 == 0)

m.c61 = Constraint(expr= - m.x20 + 32.7*m.x129 == 0)

m.c62 = Constraint(expr= - m.x21 + 32.7*m.x130 == 0)

m.c63 = Constraint(expr= - m.x22 + 56.5*m.x131 == 0)

m.c64 = Constraint(expr= - m.x23 + 56.5*m.x132 == 0)

m.c65 = Constraint(expr= - m.x24 + 56.5*m.x133 == 0)

m.c66 = Constraint(expr= - m.x10 + 13.1*m.x119 == 0)

m.c67 = Constraint(expr= - m.x11 + 32.7*m.x120 == 0)

m.c68 = Constraint(expr= - m.x12 + 56.5*m.x121 == 0)

m.c69 = Constraint(expr=   m.x119 + m.x125 + m.x126 + m.x127 == 1)

m.c70 = Constraint(expr=   m.x120 + m.x128 + m.x129 + m.x130 == 1)

m.c71 = Constraint(expr=   m.x121 + m.x131 + m.x132 + m.x133 == 1)

m.c72 = Constraint(expr= - 20000*m.x26 + m.x29 + m.x38 + m.x47 + m.x74 + m.x83 + m.x92 <= 0)

m.c73 = Constraint(expr= - 20000*m.x26 + m.x30 + m.x39 + m.x48 + m.x75 + m.x84 + m.x93 <= 0)

m.c74 = Constraint(expr= - 20000*m.x26 + m.x31 + m.x40 + m.x49 + m.x76 + m.x85 + m.x94 <= 0)

m.c75 = Constraint(expr= - 20000*m.x27 + m.x32 + m.x41 + m.x50 + m.x77 + m.x86 + m.x95 <= 0)

m.c76 = Constraint(expr= - 20000*m.x27 + m.x33 + m.x42 + m.x51 + m.x78 + m.x87 + m.x96 <= 0)

m.c77 = Constraint(expr= - 20000*m.x27 + m.x34 + m.x43 + m.x52 + m.x79 + m.x88 + m.x97 <= 0)

m.c78 = Constraint(expr= - 20000*m.x28 + m.x35 + m.x44 + m.x53 + m.x80 + m.x89 + m.x98 <= 0)

m.c79 = Constraint(expr= - 20000*m.x28 + m.x36 + m.x45 + m.x54 + m.x81 + m.x90 + m.x99 <= 0)

m.c80 = Constraint(expr= - 20000*m.x28 + m.x37 + m.x46 + m.x55 + m.x82 + m.x91 + m.x100 <= 0)

m.c81 = Constraint(expr=   m.x29 + m.x38 + m.x47 + m.x74 + m.x83 + m.x92 - m.x101 == 0)

m.c82 = Constraint(expr=   0.001*m.x30 + 0.001*m.x39 + 0.001*m.x48 + 0.001*m.x75 + 0.001*m.x84 + 0.001*m.x93 - m.x102
                         == 0)

m.c83 = Constraint(expr=   m.x31 + m.x40 + m.x49 + m.x76 + m.x85 + m.x94 - m.x103 == 0)

m.c84 = Constraint(expr=   0.1*m.x32 + 0.1*m.x41 + 0.1*m.x50 + 0.1*m.x77 + 0.1*m.x86 + 0.1*m.x95 - m.x104 == 0)

m.c85 = Constraint(expr=   0.1*m.x33 + 0.1*m.x42 + 0.1*m.x51 + 0.1*m.x78 + 0.1*m.x87 + 0.1*m.x96 - m.x105 == 0)

m.c86 = Constraint(expr=   0.03*m.x34 + 0.03*m.x43 + 0.03*m.x52 + 0.03*m.x79 + 0.03*m.x88 + 0.03*m.x97 - m.x106 == 0)

m.c87 = Constraint(expr=   0.05*m.x35 + 0.05*m.x44 + 0.05*m.x53 + 0.05*m.x80 + 0.05*m.x89 + 0.05*m.x98 - m.x107 == 0)

m.c88 = Constraint(expr=   m.x36 + m.x45 + m.x54 + m.x81 + m.x90 + m.x99 - m.x108 == 0)

m.c89 = Constraint(expr=   0.8*m.x37 + 0.8*m.x46 + 0.8*m.x55 + 0.8*m.x82 + 0.8*m.x91 + 0.8*m.x100 - m.x109 == 0)

m.c90 = Constraint(expr= - m.x29 - m.x32 - m.x35 - m.x65 + m.x101 == 0)

m.c91 = Constraint(expr= - m.x30 - m.x33 - m.x36 - m.x66 + m.x102 == 0)

m.c92 = Constraint(expr= - m.x31 - m.x34 - m.x37 - m.x67 + m.x103 == 0)

m.c93 = Constraint(expr= - m.x38 - m.x41 - m.x44 - m.x68 + m.x104 == 0)

m.c94 = Constraint(expr= - m.x39 - m.x42 - m.x45 - m.x69 + m.x105 == 0)

m.c95 = Constraint(expr= - m.x40 - m.x43 - m.x46 - m.x70 + m.x106 == 0)

m.c96 = Constraint(expr= - m.x47 - m.x50 - m.x53 - m.x71 + m.x107 == 0)

m.c97 = Constraint(expr= - m.x48 - m.x51 - m.x54 - m.x72 + m.x108 == 0)

m.c98 = Constraint(expr= - m.x49 - m.x52 - m.x55 - m.x73 + m.x109 == 0)

m.c99 = Constraint(expr=m.x101*m.x110 - m.x29 == 0)

m.c100 = Constraint(expr=m.x102*m.x110 - m.x30 == 0)

m.c101 = Constraint(expr=m.x103*m.x110 - m.x31 == 0)

m.c102 = Constraint(expr=m.x101*m.x111 - m.x32 == 0)

m.c103 = Constraint(expr=m.x102*m.x111 - m.x33 == 0)

m.c104 = Constraint(expr=m.x103*m.x111 - m.x34 == 0)

m.c105 = Constraint(expr=m.x101*m.x112 - m.x35 == 0)

m.c106 = Constraint(expr=m.x102*m.x112 - m.x36 == 0)

m.c107 = Constraint(expr=m.x103*m.x112 - m.x37 == 0)

m.c108 = Constraint(expr=m.x104*m.x113 - m.x38 == 0)

m.c109 = Constraint(expr=m.x105*m.x113 - m.x39 == 0)

m.c110 = Constraint(expr=m.x106*m.x113 - m.x40 == 0)

m.c111 = Constraint(expr=m.x104*m.x114 - m.x41 == 0)

m.c112 = Constraint(expr=m.x105*m.x114 - m.x42 == 0)

m.c113 = Constraint(expr=m.x106*m.x114 - m.x43 == 0)

m.c114 = Constraint(expr=m.x104*m.x115 - m.x44 == 0)

m.c115 = Constraint(expr=m.x105*m.x115 - m.x45 == 0)

m.c116 = Constraint(expr=m.x106*m.x115 - m.x46 == 0)

m.c117 = Constraint(expr=m.x107*m.x116 - m.x47 == 0)

m.c118 = Constraint(expr=m.x108*m.x116 - m.x48 == 0)

m.c119 = Constraint(expr=m.x109*m.x116 - m.x49 == 0)

m.c120 = Constraint(expr=m.x107*m.x117 - m.x50 == 0)

m.c121 = Constraint(expr=m.x108*m.x117 - m.x51 == 0)

m.c122 = Constraint(expr=m.x109*m.x117 - m.x52 == 0)

m.c123 = Constraint(expr=m.x107*m.x118 - m.x53 == 0)

m.c124 = Constraint(expr=m.x108*m.x118 - m.x54 == 0)

m.c125 = Constraint(expr=m.x109*m.x118 - m.x55 == 0)

m.c126 = Constraint(expr=m.x101*m.x122 - m.x65 == 0)

m.c127 = Constraint(expr=m.x102*m.x122 - m.x66 == 0)

m.c128 = Constraint(expr=m.x103*m.x122 - m.x67 == 0)

m.c129 = Constraint(expr=m.x104*m.x123 - m.x68 == 0)

m.c130 = Constraint(expr=m.x105*m.x123 - m.x69 == 0)

m.c131 = Constraint(expr=m.x106*m.x123 - m.x70 == 0)

m.c132 = Constraint(expr=m.x107*m.x124 - m.x71 == 0)

m.c133 = Constraint(expr=m.x108*m.x124 - m.x72 == 0)

m.c134 = Constraint(expr=m.x109*m.x124 - m.x73 == 0)

m.c135 = Constraint(expr=m.x26*m.x110 - m.x1 == 0)

m.c136 = Constraint(expr=m.x26*m.x111 - m.x2 == 0)

m.c137 = Constraint(expr=m.x26*m.x112 - m.x3 == 0)

m.c138 = Constraint(expr=m.x27*m.x113 - m.x4 == 0)

m.c139 = Constraint(expr=m.x27*m.x114 - m.x5 == 0)

m.c140 = Constraint(expr=m.x27*m.x115 - m.x6 == 0)

m.c141 = Constraint(expr=m.x28*m.x116 - m.x7 == 0)

m.c142 = Constraint(expr=m.x28*m.x117 - m.x8 == 0)

m.c143 = Constraint(expr=m.x28*m.x118 - m.x9 == 0)

m.c144 = Constraint(expr=m.x26*m.x122 - m.x13 == 0)

m.c145 = Constraint(expr=m.x27*m.x123 - m.x14 == 0)

m.c146 = Constraint(expr=m.x28*m.x124 - m.x15 == 0)

m.c147 = Constraint(expr=   m.x110 + m.x111 + m.x112 + m.x122 == 1)

m.c148 = Constraint(expr=   m.x113 + m.x114 + m.x115 + m.x123 == 1)

m.c149 = Constraint(expr=   m.x116 + m.x117 + m.x118 + m.x124 == 1)

m.c150 = Constraint(expr= - 2*m.x25 + m.x56 + m.x59 + m.x62 + m.x65 + m.x68 + m.x71 <= 0)

m.c151 = Constraint(expr= - 2*m.x25 + m.x57 + m.x60 + m.x63 + m.x66 + m.x69 + m.x72 <= 0)

m.c152 = Constraint(expr= - 5*m.x25 + m.x58 + m.x61 + m.x64 + m.x67 + m.x70 + m.x73 <= 0)
