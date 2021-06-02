#  MINLP written by GAMS Convert at 04/21/18 13:51:12
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        154      110       12       32        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        135      127        8        0        0        0        0        0
#  FX      1        0        1        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        539      356      183        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0.95,1),initialize=0.95)
m.x2 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x3 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x4 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x5 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x6 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x7 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x8 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x9 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x19 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x20 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x21 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x22 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x23 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x24 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x25 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x26 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x27 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x28 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x29 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x30 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x31 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x32 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x33 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x34 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x35 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x45 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x46 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x47 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x48 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x49 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x50 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x51 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x52 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x53 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x54 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x55 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x56 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x57 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x58 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x59 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x60 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x61 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x62 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x63 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x64 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x65 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x66 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x67 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x68 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x69 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x70 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x71 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x72 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x73 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x74 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x75 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x76 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x77 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x78 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x79 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x80 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x81 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x82 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x83 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x84 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x85 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x86 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x87 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x88 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x89 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x90 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x91 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x92 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x93 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x94 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x95 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x96 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x97 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x98 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x99 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x100 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x101 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x102 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x103 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x104 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x105 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x106 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x107 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x108 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x109 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x110 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x111 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x112 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x113 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x114 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x115 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x116 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x117 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x118 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x119 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x120 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x121 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x122 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x123 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x124 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x125 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x126 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.b127 = Var(within=Binary,bounds=(1,1),initialize=1)
m.b128 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b129 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b130 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b131 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b132 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b133 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b134 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   m.x1, sense=maximize)

m.c2 = Constraint(expr= - m.x10 + 0.001*m.b127 <= 0)

m.c3 = Constraint(expr= - m.x11 + 0.001*m.b128 <= 0)

m.c4 = Constraint(expr= - m.x12 + 0.001*m.b129 <= 0)

m.c5 = Constraint(expr= - m.x13 + 0.001*m.b130 <= 0)

m.c6 = Constraint(expr= - m.x14 + 0.001*m.b131 <= 0)

m.c7 = Constraint(expr= - m.x15 + 0.001*m.b132 <= 0)

m.c8 = Constraint(expr= - m.x16 + 0.001*m.b133 <= 0)

m.c9 = Constraint(expr= - m.x17 + 0.001*m.b134 <= 0)

m.c10 = Constraint(expr=   m.x10 - 10*m.b127 <= 0)

m.c11 = Constraint(expr=   m.x11 - 10*m.b128 <= 0)

m.c12 = Constraint(expr=   m.x12 - 10*m.b129 <= 0)

m.c13 = Constraint(expr=   m.x13 - 10*m.b130 <= 0)

m.c14 = Constraint(expr=   m.x14 - 10*m.b131 <= 0)

m.c15 = Constraint(expr=   m.x15 - 10*m.b132 <= 0)

m.c16 = Constraint(expr=   m.x16 - 10*m.b133 <= 0)

m.c17 = Constraint(expr=   m.x17 - 10*m.b134 <= 0)

m.c18 = Constraint(expr= - m.x36 + 0.001*m.b127 <= 0)

m.c19 = Constraint(expr= - m.x37 + 0.001*m.b128 <= 0)

m.c20 = Constraint(expr= - m.x38 + 0.001*m.b129 <= 0)

m.c21 = Constraint(expr= - m.x39 + 0.001*m.b130 <= 0)

m.c22 = Constraint(expr= - m.x40 + 0.001*m.b131 <= 0)

m.c23 = Constraint(expr= - m.x41 + 0.001*m.b132 <= 0)

m.c24 = Constraint(expr= - m.x42 + 0.001*m.b133 <= 0)

m.c25 = Constraint(expr= - m.x43 + 0.001*m.b134 <= 0)

m.c26 = Constraint(expr=   m.x36 - 10*m.b127 <= 0)

m.c27 = Constraint(expr=   m.x37 - 10*m.b128 <= 0)

m.c28 = Constraint(expr=   m.x38 - 10*m.b129 <= 0)

m.c29 = Constraint(expr=   m.x39 - 10*m.b130 <= 0)

m.c30 = Constraint(expr=   m.x40 - 10*m.b131 <= 0)

m.c31 = Constraint(expr=   m.x41 - 10*m.b132 <= 0)

m.c32 = Constraint(expr=   m.x42 - 10*m.b133 <= 0)

m.c33 = Constraint(expr=   m.x43 - 10*m.b134 <= 0)

m.c34 = Constraint(expr=   m.b127 - m.b128 >= 0)

m.c35 = Constraint(expr=   m.b128 - m.b129 >= 0)

m.c36 = Constraint(expr=   m.b129 - m.b130 >= 0)

m.c37 = Constraint(expr=   m.b130 - m.b131 >= 0)

m.c38 = Constraint(expr=   m.b131 - m.b132 >= 0)

m.c39 = Constraint(expr=   m.b132 - m.b133 >= 0)

m.c40 = Constraint(expr=   m.b133 - m.b134 >= 0)

m.c41 = Constraint(expr= - 1000000000*m.x2 + 1000000000*m.x10 + m.x18 == 0)

m.c42 = Constraint(expr=200000000*m.x1*m.x2 - 100000000*m.x3 + 100000000*m.x11 + m.x19 == 0)

m.c43 = Constraint(expr=20000000*m.x1*m.x3 - 10000000*m.x2 - 10000000*m.x4 - 10000000*m.x10 + 10000000*m.x12 + m.x20
                         == 0)

m.c44 = Constraint(expr=2000000*m.x1*m.x4 - 1000000*m.x3 - 1000000*m.x5 - 1000000*m.x11 + 1000000*m.x13 + m.x21 == 0)

m.c45 = Constraint(expr=200000*m.x1*m.x5 - 100000*m.x4 - 100000*m.x6 - 100000*m.x12 + 100000*m.x14 + m.x22 == 0)

m.c46 = Constraint(expr=20000*m.x1*m.x6 - 10000*m.x5 - 10000*m.x7 - 10000*m.x13 + 10000*m.x15 + m.x23 == 0)

m.c47 = Constraint(expr=2000*m.x1*m.x7 - 1000*m.x6 - 1000*m.x8 - 1000*m.x14 + 1000*m.x16 + m.x24 == 0)

m.c48 = Constraint(expr=200*m.x1*m.x8 - 100*m.x7 - 100*m.x9 - 100*m.x15 + 100*m.x17 + m.x25 == 0)

m.c49 = Constraint(expr=20*m.x1*m.x9 - 10*m.x8 - 10*m.x16 + m.x26 == 0)

m.c50 = Constraint(expr= - m.x9 - m.x17 + m.x27 == 0)

m.c51 = Constraint(expr= - m.x2 + 1E-5*m.x3 - 1E-10*m.x4 + m.x28 == 0)

m.c52 = Constraint(expr= - m.x3 + 2E-5*m.x4 - 3E-10*m.x5 + m.x29 == 0)

m.c53 = Constraint(expr= - m.x4 + 3E-5*m.x5 - 6E-10*m.x6 + m.x30 == 0)

m.c54 = Constraint(expr= - m.x5 + 4E-5*m.x6 - 1E-9*m.x7 + m.x31 == 0)

m.c55 = Constraint(expr= - m.x6 + 5E-5*m.x7 - 1.5E-9*m.x8 + m.x32 == 0)

m.c56 = Constraint(expr= - m.x7 + 6E-5*m.x8 - 2.1E-9*m.x9 + m.x33 == 0)

m.c57 = Constraint(expr= - m.x8 + 7E-5*m.x9 + m.x34 == 0)

m.c58 = Constraint(expr= - m.x9 + m.x35 == 0)

m.c59 = Constraint(expr= - m.x10 + 1E-5*m.x11 - 1E-10*m.x12 + m.x36 == 0)

m.c60 = Constraint(expr= - m.x11 + 2E-5*m.x12 - 3E-10*m.x13 + m.x37 == 0)

m.c61 = Constraint(expr= - m.x12 + 3E-5*m.x13 - 6E-10*m.x14 + m.x38 == 0)

m.c62 = Constraint(expr= - m.x13 + 4E-5*m.x14 - 1E-9*m.x15 + m.x39 == 0)

m.c63 = Constraint(expr= - m.x14 + 5E-5*m.x15 - 1.5E-9*m.x16 + m.x40 == 0)

m.c64 = Constraint(expr= - m.x15 + 6E-5*m.x16 - 2.1E-9*m.x17 + m.x41 == 0)

m.c65 = Constraint(expr= - m.x16 + 7E-5*m.x17 + m.x42 == 0)

m.c66 = Constraint(expr= - m.x17 + m.x43 == 0)

m.c67 = Constraint(expr= - m.x18 + 1E-5*m.x19 - 1E-10*m.x20 + m.x44 == 0)

m.c68 = Constraint(expr= - m.x19 + 2E-5*m.x20 - 3E-10*m.x21 + m.x45 == 0)

m.c69 = Constraint(expr= - m.x20 + 3E-5*m.x21 - 6E-10*m.x22 + m.x46 == 0)

m.c70 = Constraint(expr= - m.x21 + 4E-5*m.x22 - 1E-9*m.x23 + m.x47 == 0)

m.c71 = Constraint(expr= - m.x22 + 5E-5*m.x23 - 1.5E-9*m.x24 + m.x48 == 0)

m.c72 = Constraint(expr= - m.x23 + 6E-5*m.x24 - 2.1E-9*m.x25 + m.x49 == 0)

m.c73 = Constraint(expr= - m.x24 + 7E-5*m.x25 - 2.8E-9*m.x26 + m.x50 == 0)

m.c74 = Constraint(expr= - m.x25 + 8E-5*m.x26 - 3.6E-9*m.x27 + m.x51 == 0)

m.c75 = Constraint(expr= - m.x26 + 9E-5*m.x27 + m.x52 == 0)

m.c76 = Constraint(expr= - m.x27 + m.x53 == 0)

m.c77 = Constraint(expr= - m.x35 + m.x54 == 0)

m.c78 = Constraint(expr= - m.x33 + m.x55 == 0)

m.c79 = Constraint(expr= - m.x31 + m.x56 == 0)

m.c80 = Constraint(expr= - m.x29 + m.x57 == 0)

m.c81 = Constraint(expr= - m.x34 + m.x58 == 0)

m.c82 = Constraint(expr= - m.x32 + m.x59 == 0)

m.c83 = Constraint(expr= - m.x30 + m.x60 == 0)

m.c84 = Constraint(expr= - m.x28 + m.x61 == 0)

m.c85 = Constraint(expr=m.x54*m.x59/m.x58 - m.x55 + m.x62 == 0)

m.c86 = Constraint(expr=m.x54*m.x60/m.x58 - m.x56 + m.x63 == 0)

m.c87 = Constraint(expr=m.x54*m.x61/m.x58 - m.x57 + m.x64 == 0)

m.c88 = Constraint(expr=m.x58*m.x63/m.x62 - m.x59 + m.x66 == 0)

m.c89 = Constraint(expr=m.x58*m.x64/m.x62 - m.x60 + m.x67 == 0)

m.c90 = Constraint(expr=m.x58*m.x65/m.x62 - m.x61 + m.x68 == 0)

m.c91 = Constraint(expr=m.x62*m.x67/m.x66 - m.x63 + m.x70 == 0)

m.c92 = Constraint(expr=m.x62*m.x68/m.x66 - m.x64 + m.x71 == 0)

m.c93 = Constraint(expr=m.x62*m.x69/m.x66 - m.x65 + m.x72 == 0)

m.c94 = Constraint(expr=m.x66*m.x71/m.x70 - m.x67 + m.x74 == 0)

m.c95 = Constraint(expr=m.x66*m.x72/m.x70 - m.x68 + m.x75 == 0)

m.c96 = Constraint(expr=m.x66*m.x73/m.x70 - m.x69 + m.x76 == 0)

m.c97 = Constraint(expr=m.x70*m.x75/m.x74 - m.x71 + m.x78 == 0)

m.c98 = Constraint(expr=m.x70*m.x76/m.x74 - m.x72 + m.x79 == 0)

m.c99 = Constraint(expr=m.x70*m.x77/m.x74 - m.x73 + m.x80 == 0)

m.c100 = Constraint(expr=   m.x65 == 0)

m.c101 = Constraint(expr=   m.x69 == 0)

m.c102 = Constraint(expr=   m.x73 == 0)

m.c103 = Constraint(expr=   m.x77 == 0)

m.c104 = Constraint(expr=   m.x81 == 0)

m.c105 = Constraint(expr= - m.x53 + m.x82 == 0)

m.c106 = Constraint(expr= - m.x51 + m.x83 == 0)

m.c107 = Constraint(expr= - m.x49 + m.x84 == 0)

m.c108 = Constraint(expr= - m.x47 + m.x85 == 0)

m.c109 = Constraint(expr= - m.x45 + m.x86 == 0)

m.c110 = Constraint(expr= - m.x52 + m.x87 == 0)

m.c111 = Constraint(expr= - m.x50 + m.x88 == 0)

m.c112 = Constraint(expr= - m.x48 + m.x89 == 0)

m.c113 = Constraint(expr= - m.x46 + m.x90 == 0)

m.c114 = Constraint(expr= - m.x44 + m.x91 == 0)

m.c115 = Constraint(expr=m.x82*m.x88/m.x87 - m.x83 + m.x92 == 0)

m.c116 = Constraint(expr=m.x82*m.x89/m.x87 - m.x84 + m.x93 == 0)

m.c117 = Constraint(expr=m.x82*m.x90/m.x87 - m.x85 + m.x94 == 0)

m.c118 = Constraint(expr=m.x82*m.x91/m.x87 - m.x86 + m.x95 == 0)

m.c119 = Constraint(expr=m.x87*m.x93/m.x92 - m.x88 + m.x97 == 0)

m.c120 = Constraint(expr=m.x87*m.x94/m.x92 - m.x89 + m.x98 == 0)

m.c121 = Constraint(expr=m.x87*m.x95/m.x92 - m.x90 + m.x99 == 0)

m.c122 = Constraint(expr=m.x87*m.x96/m.x92 - m.x91 + m.x100 == 0)

m.c123 = Constraint(expr=m.x92*m.x98/m.x97 - m.x93 + m.x102 == 0)

m.c124 = Constraint(expr=m.x92*m.x99/m.x97 - m.x94 + m.x103 == 0)

m.c125 = Constraint(expr=m.x92*m.x100/m.x97 - m.x95 + m.x104 == 0)

m.c126 = Constraint(expr=m.x92*m.x101/m.x97 - m.x96 + m.x105 == 0)

m.c127 = Constraint(expr=m.x97*m.x103/m.x102 - m.x98 + m.x107 == 0)

m.c128 = Constraint(expr=m.x97*m.x104/m.x102 - m.x99 + m.x108 == 0)

m.c129 = Constraint(expr=m.x97*m.x105/m.x102 - m.x100 + m.x109 == 0)

m.c130 = Constraint(expr=m.x97*m.x106/m.x102 - m.x101 + m.x110 == 0)

m.c131 = Constraint(expr=m.x102*m.x108/m.x107 - m.x103 + m.x112 == 0)

m.c132 = Constraint(expr=m.x102*m.x109/m.x107 - m.x104 + m.x113 == 0)

m.c133 = Constraint(expr=m.x102*m.x110/m.x107 - m.x105 + m.x114 == 0)

m.c134 = Constraint(expr=m.x102*m.x111/m.x107 - m.x106 + m.x115 == 0)

m.c135 = Constraint(expr=m.x107*m.x113/m.x112 - m.x108 + m.x117 == 0)

m.c136 = Constraint(expr=m.x107*m.x114/m.x112 - m.x109 + m.x118 == 0)

m.c137 = Constraint(expr=m.x107*m.x115/m.x112 - m.x110 + m.x119 == 0)

m.c138 = Constraint(expr=m.x107*m.x116/m.x112 - m.x111 + m.x120 == 0)

m.c139 = Constraint(expr=m.x112*m.x118/m.x117 - m.x113 + m.x122 == 0)

m.c140 = Constraint(expr=m.x112*m.x119/m.x117 - m.x114 + m.x123 == 0)

m.c141 = Constraint(expr=m.x112*m.x120/m.x117 - m.x115 + m.x124 == 0)

m.c142 = Constraint(expr=m.x112*m.x121/m.x117 - m.x116 + m.x125 == 0)

m.c143 = Constraint(expr=   m.x96 == 0)

m.c144 = Constraint(expr=   m.x101 == 0)

m.c145 = Constraint(expr=   m.x106 == 0)

m.c146 = Constraint(expr=   m.x111 == 0)

m.c147 = Constraint(expr=   m.x116 == 0)

m.c148 = Constraint(expr=   m.x121 == 0)

m.c149 = Constraint(expr=   m.x126 == 0)

m.c150 = Constraint(expr=m.x41*m.x42 - m.x40*m.x43 - 1E-5*m.b134 >= 0)

m.c151 = Constraint(expr=m.x40*m.x41*m.x42 - m.x40*m.x40*m.x43 + m.x38*m.x42*m.x43 - m.x39*m.x42*m.x42 - 1E-5*m.b133
                          >= 0)

m.c152 = Constraint(expr=m.x39*m.x40*m.x41*m.x42 - m.x40**2*m.x39*m.x43 - m.x39**2*m.x42**2 + 2*m.x38*m.x39*m.x42*m.x43
                          - m.x38**2*m.x43**2 + m.x38*m.x40*m.x41*m.x43 - m.x41**2*m.x38*m.x42 + m.x37*m.x41*m.x42**2 - 
                         m.x37*m.x40*m.x42*m.x43 - m.x36*m.x41*m.x42*m.x43 + m.x36*m.x40*m.x43**2 + (m.x39*m.x40 - m.x38
                         *m.x41)*(1 - m.b133) - 1E-5*m.b132 >= 0)

m.c153 = Constraint(expr=m.x38*m.x39*m.x40*m.x41*m.x42 - m.x38*m.x39*m.x40**2*m.x43 + 2*m.x38**2*m.x39*m.x42*m.x43 - 
                         m.x39**2*m.x38*m.x42**2 - m.x38**3*m.x43**2 + m.x38**2*m.x40*m.x41*m.x43 - m.x38**2*m.x41**2*
                         m.x42 - 3*m.x37*m.x38*m.x40*m.x42*m.x43 + m.x40**3*m.x37*m.x43 - m.x40**2*m.x37*m.x41*m.x42 + 
                         m.x37*m.x39*m.x40*m.x42**2 + 2*m.x37*m.x38*m.x41*m.x42**2 - m.x37**2*m.x42**3 - m.x36**2*m.x42*
                         m.x43**2 - m.x36*m.x39*m.x41*m.x42**2 - m.x36*m.x38*m.x41*m.x42*m.x43 - m.x40**2*m.x36*m.x41*
                         m.x43 + 2*m.x36*m.x37*m.x42**2*m.x43 + 2*m.x36*m.x38*m.x40*m.x43**2 + m.x36*m.x40*m.x41**2*
                         m.x42 + (m.x38*m.x39*m.x40 - m.x38**2*m.x41 - m.x40**2*m.x37 + m.x36*m.x40*m.x41)*(1 - m.b133)
                          - 1E-5*m.b131 >= 0)

m.c154 = Constraint(expr=m.x36**3*m.x43**3 - m.x36**2*m.x41**3*m.x42 + m.x36**2*m.x40*m.x41**2*m.x43 - 2*m.x36**2*m.x39*
                         m.x40*m.x43**2 - m.x36**2*m.x38*m.x41*m.x43**2 + 3*m.x36**2*m.x39*m.x41*m.x42*m.x43 - 3*m.x36**
                         2*m.x37*m.x42*m.x43**2 + m.x36*m.x38*m.x39*m.x41**2*m.x42 + m.x39**3*m.x36*m.x42**2 + m.x36*
                         m.x37*m.x39*m.x40*m.x42*m.x43 - m.x39**2*m.x36*m.x40*m.x41*m.x42 - m.x36*m.x38*m.x39*m.x40*
                         m.x41*m.x43 - 2*m.x36*m.x37*m.x40**2*m.x41*m.x43 + m.x38**2*m.x36*m.x39*m.x43**2 - m.x36*m.x37*
                         m.x38*m.x41*m.x42*m.x43 - 2*m.x36*m.x38*m.x39**2*m.x42*m.x43 - 3*m.x36*m.x37*m.x39*m.x41*m.x42
                         **2 + 3*m.x36*m.x37*m.x38*m.x40*m.x43**2 + 2*m.x36*m.x37*m.x40*m.x41**2*m.x42 + 3*m.x37**2*
                         m.x36*m.x42**2*m.x43 + m.x39**2*m.x36*m.x40**2*m.x43 + m.x38**2*m.x37*m.x40*m.x41*m.x43 + 2*
                         m.x37**2*m.x38*m.x41*m.x42**2 + 2*m.x38**2*m.x37*m.x39*m.x42*m.x43 + m.x37**2*m.x40**3*m.x43 - 
                         m.x37*m.x38*m.x39**2*m.x42**2 - m.x37**3*m.x42**3 - m.x37**2*m.x40**2*m.x41*m.x42 - m.x38**3*
                         m.x37*m.x43**2 - m.x38**2*m.x37*m.x41**2*m.x42 - m.x37*m.x38*m.x39*m.x40**2*m.x43 + m.x37*m.x38
                         *m.x39*m.x40*m.x41*m.x42 + m.x37**2*m.x39*m.x40*m.x42**2 - 3*m.x37**2*m.x38*m.x40*m.x42*m.x43
                          + (m.x37*m.x38*m.x39*m.x40 - m.x38**2*m.x37*m.x41 - m.x37**2*m.x40**2 + 2*m.x36*m.x37*m.x40*
                         m.x41 + m.x36*m.x38*m.x39*m.x41 - m.x36**2*m.x41**2 - m.x39**2*m.x36*m.x40)*(1 - m.b133) + (
                         m.x37*m.x38 - m.x36*m.x39)*(1 - m.b131) - 1E-5*m.b130 >= 0)
