#  MINLP written by GAMS Convert at 04/21/18 13:54:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        136       82       28       26        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        113       89       24        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        314      300       14        0
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
m.x25 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x26 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x27 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x28 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x29 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x30 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x31 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x32 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x33 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x34 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x38 = Var(within=Reals,bounds=(-3,3),initialize=0)
m.x39 = Var(within=Reals,bounds=(-3,3),initialize=0)
m.x40 = Var(within=Reals,bounds=(-3,3),initialize=0)
m.x41 = Var(within=Reals,bounds=(-3,3),initialize=0)
m.x42 = Var(within=Reals,bounds=(-3,3),initialize=0)
m.x43 = Var(within=Reals,bounds=(-3,3),initialize=0)
m.x44 = Var(within=Reals,bounds=(-3,3),initialize=0)
m.x45 = Var(within=Reals,bounds=(None,3),initialize=0)
m.x46 = Var(within=Reals,bounds=(-3,3),initialize=0)
m.x47 = Var(within=Reals,bounds=(-3,3),initialize=0)
m.x48 = Var(within=Reals,bounds=(-3,3),initialize=0)
m.x49 = Var(within=Reals,bounds=(-3,3),initialize=0)
m.x50 = Var(within=Reals,bounds=(-3,3),initialize=0)
m.x51 = Var(within=Reals,bounds=(-3,3),initialize=0)
m.x52 = Var(within=Reals,bounds=(-3,3),initialize=0)
m.x53 = Var(within=Reals,bounds=(-3,3),initialize=0)
m.x54 = Var(within=Reals,bounds=(-3,3),initialize=0)
m.x55 = Var(within=Reals,bounds=(-3,3),initialize=0)
m.x56 = Var(within=Reals,bounds=(-3,3),initialize=0)
m.x57 = Var(within=Reals,bounds=(None,3),initialize=0)
m.x58 = Var(within=Reals,bounds=(-3,3),initialize=0)
m.x59 = Var(within=Reals,bounds=(-3,3),initialize=0)
m.x60 = Var(within=Reals,bounds=(-3,3),initialize=0)
m.x61 = Var(within=Reals,bounds=(-3,3),initialize=0)
m.x62 = Var(within=Reals,bounds=(-3,0),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x64 = Var(within=Reals,bounds=(-3,0),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x66 = Var(within=Reals,bounds=(-3,0),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x68 = Var(within=Reals,bounds=(-3,0),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x70 = Var(within=Reals,bounds=(-3,0),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x72 = Var(within=Reals,bounds=(-3,0),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x74 = Var(within=Reals,bounds=(-3,0),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x76 = Var(within=Reals,bounds=(-3,0),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x78 = Var(within=Reals,bounds=(-3,0),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x80 = Var(within=Reals,bounds=(-3,0),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x82 = Var(within=Reals,bounds=(-3,0),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x84 = Var(within=Reals,bounds=(-3,0),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x98 = Var(within=Reals,bounds=(-6,6),initialize=0)
m.x99 = Var(within=Reals,bounds=(-6,6),initialize=0)
m.x100 = Var(within=Reals,bounds=(-6,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(-6,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(-6,6),initialize=0)
m.x107 = Var(within=Reals,bounds=(-6,6),initialize=0)
m.x108 = Var(within=Reals,bounds=(-6,6),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,3),initialize=0)

m.obj = Objective(expr= - m.x112, sense=minimize)

m.c1 = Constraint(expr=-m.x36*m.x31 - m.x25 + m.x27 == 0)

m.c2 = Constraint(expr=-m.x36*m.x32 - m.x26 + m.x28 == 0)

m.c3 = Constraint(expr=(-m.x37*m.x31) - m.x35*m.x33 - m.x25 + m.x29 == 0)

m.c4 = Constraint(expr=(-m.x37*m.x32) - m.x35*m.x34 - m.x26 + m.x30 == 0)

m.c5 = Constraint(expr=m.x31**2 + m.x32**2 == 1)

m.c6 = Constraint(expr=   m.x32 + m.x33 == 0)

m.c7 = Constraint(expr= - m.x31 + m.x34 == 0)

m.c8 = Constraint(expr= - m.x36 + m.x112 <= 0)

m.c9 = Constraint(expr= - m.x35 + m.x112 <= 0)

m.c10 = Constraint(expr= - m.x25 - m.x50 == 0)

m.c11 = Constraint(expr= - m.x25 + m.x39 == 1)

m.c12 = Constraint(expr= - m.x25 + 0.8944*m.x40 - 0.4472*m.x52 == 1)

m.c13 = Constraint(expr= - m.x25 - 0.8944*m.x41 - 0.4772*m.x53 == 1)

m.c14 = Constraint(expr= - m.x27 - m.x54 == 0)

m.c15 = Constraint(expr= - m.x27 + m.x43 == 1)

m.c16 = Constraint(expr= - m.x27 + 0.8944*m.x44 - 0.4472*m.x56 == 1)

m.c17 = Constraint(expr= - m.x27 - 0.8944*m.x45 - 0.4772*m.x57 == 1)

m.c18 = Constraint(expr= - m.x29 - m.x58 == 0)

m.c19 = Constraint(expr= - m.x29 + m.x47 == 1)

m.c20 = Constraint(expr= - m.x29 + 0.8944*m.x48 - 0.4472*m.x60 == 1)

m.c21 = Constraint(expr= - m.x29 - 0.8944*m.x49 - 0.4772*m.x61 == 1)

m.c22 = Constraint(expr= - m.x26 + m.x38 == 1)

m.c23 = Constraint(expr= - m.x26 + m.x51 == 0)

m.c24 = Constraint(expr= - m.x26 + 0.4472*m.x40 + 0.8944*m.x52 == 0)

m.c25 = Constraint(expr= - m.x26 + 0.4772*m.x41 - 0.8944*m.x53 == 0)

m.c26 = Constraint(expr= - m.x28 + m.x42 == 1)

m.c27 = Constraint(expr= - m.x28 + m.x55 == 0)

m.c28 = Constraint(expr= - m.x28 + 0.4472*m.x44 + 0.8944*m.x56 == 0)

m.c29 = Constraint(expr= - m.x28 + 0.4772*m.x45 - 0.8944*m.x57 == 0)

m.c30 = Constraint(expr= - m.x30 + m.x46 == 1)

m.c31 = Constraint(expr= - m.x30 + m.x59 == 0)

m.c32 = Constraint(expr= - m.x30 + 0.4472*m.x48 + 0.8944*m.x60 == 0)

m.c33 = Constraint(expr= - m.x30 + 0.4772*m.x49 - 0.8944*m.x61 == 0)

m.c34 = Constraint(expr= - 3.5*m.b1 - m.x62 <= 0)

m.c35 = Constraint(expr= - 3.5*m.b3 - m.x64 <= 0)

m.c36 = Constraint(expr= - 3.5*m.b5 - m.x66 <= 0)

m.c37 = Constraint(expr= - 3.5*m.b7 - m.x68 <= 0)

m.c38 = Constraint(expr= - 3.5*m.b9 - m.x70 <= 0)

m.c39 = Constraint(expr= - 3.5*m.b11 - m.x72 <= 0)

m.c40 = Constraint(expr= - 3.5*m.b13 - m.x74 <= 0)

m.c41 = Constraint(expr= - 3.5*m.b15 - m.x76 <= 0)

m.c42 = Constraint(expr= - 3.5*m.b17 - m.x78 <= 0)

m.c43 = Constraint(expr= - 3.5*m.b19 - m.x80 <= 0)

m.c44 = Constraint(expr= - 3.5*m.b21 - m.x82 <= 0)

m.c45 = Constraint(expr= - 3.5*m.b23 - m.x84 <= 0)

m.c46 = Constraint(expr= - m.x63 <= 0)

m.c47 = Constraint(expr= - m.x65 <= 0)

m.c48 = Constraint(expr= - m.x67 <= 0)

m.c49 = Constraint(expr= - m.x69 <= 0)

m.c50 = Constraint(expr= - m.x71 <= 0)

m.c51 = Constraint(expr= - m.x73 <= 0)

m.c52 = Constraint(expr= - m.x75 <= 0)

m.c53 = Constraint(expr= - m.x77 <= 0)

m.c54 = Constraint(expr= - m.x79 <= 0)

m.c55 = Constraint(expr= - m.x81 <= 0)

m.c56 = Constraint(expr= - m.x83 <= 0)

m.c57 = Constraint(expr= - m.x85 <= 0)

m.c58 = Constraint(expr= - m.x62 >= 0)

m.c59 = Constraint(expr= - m.x64 >= 0)

m.c60 = Constraint(expr= - m.x66 >= 0)

m.c61 = Constraint(expr= - m.x68 >= 0)

m.c62 = Constraint(expr= - m.x70 >= 0)

m.c63 = Constraint(expr= - m.x72 >= 0)

m.c64 = Constraint(expr= - m.x74 >= 0)

m.c65 = Constraint(expr= - m.x76 >= 0)

m.c66 = Constraint(expr= - m.x78 >= 0)

m.c67 = Constraint(expr= - m.x80 >= 0)

m.c68 = Constraint(expr= - m.x82 >= 0)

m.c69 = Constraint(expr= - m.x84 >= 0)

m.c70 = Constraint(expr=   3.5*m.b2 - m.x63 >= 0)

m.c71 = Constraint(expr=   3.5*m.b4 - m.x65 >= 0)

m.c72 = Constraint(expr=   3.5*m.b6 - m.x67 >= 0)

m.c73 = Constraint(expr=   3.5*m.b8 - m.x69 >= 0)

m.c74 = Constraint(expr=   3.5*m.b10 - m.x71 >= 0)

m.c75 = Constraint(expr=   3.5*m.b12 - m.x73 >= 0)

m.c76 = Constraint(expr=   3.5*m.b14 - m.x75 >= 0)

m.c77 = Constraint(expr=   3.5*m.b16 - m.x77 >= 0)

m.c78 = Constraint(expr=   3.5*m.b18 - m.x79 >= 0)

m.c79 = Constraint(expr=   3.5*m.b20 - m.x81 >= 0)

m.c80 = Constraint(expr=   3.5*m.b22 - m.x83 >= 0)

m.c81 = Constraint(expr=   3.5*m.b24 - m.x85 >= 0)

m.c82 = Constraint(expr=   m.b1 + m.b2 == 1)

m.c83 = Constraint(expr=   m.b3 + m.b4 == 1)

m.c84 = Constraint(expr=   m.b5 + m.b6 == 1)

m.c85 = Constraint(expr=   m.b7 + m.b8 == 1)

m.c86 = Constraint(expr=   m.b9 + m.b10 == 1)

m.c87 = Constraint(expr=   m.b11 + m.b12 == 1)

m.c88 = Constraint(expr=   m.b13 + m.b14 == 1)

m.c89 = Constraint(expr=   m.b15 + m.b16 == 1)

m.c90 = Constraint(expr=   m.b17 + m.b18 == 1)

m.c91 = Constraint(expr=   m.b19 + m.b20 == 1)

m.c92 = Constraint(expr=   m.b21 + m.b22 == 1)

m.c93 = Constraint(expr=   m.b23 + m.b24 == 1)

m.c94 = Constraint(expr=   m.x50 - m.x62 - m.x63 == 0)

m.c95 = Constraint(expr=   m.x51 - m.x64 - m.x65 == 0)

m.c96 = Constraint(expr=   m.x52 - m.x66 - m.x67 == 0)

m.c97 = Constraint(expr=   m.x53 - m.x68 - m.x69 == 0)

m.c98 = Constraint(expr=   m.x54 - m.x70 - m.x71 == 0)

m.c99 = Constraint(expr=   m.x55 - m.x72 - m.x73 == 0)

m.c100 = Constraint(expr=   m.x56 - m.x74 - m.x75 == 0)

m.c101 = Constraint(expr=   m.x57 - m.x76 - m.x77 == 0)

m.c102 = Constraint(expr=   m.x58 - m.x78 - m.x79 == 0)

m.c103 = Constraint(expr=   m.x59 - m.x80 - m.x81 == 0)

m.c104 = Constraint(expr=   m.x60 - m.x82 - m.x83 == 0)

m.c105 = Constraint(expr=   m.x61 - m.x84 - m.x85 == 0)

m.c106 = Constraint(expr= - m.x63 + m.x86 == 0)

m.c107 = Constraint(expr= - m.x65 + m.x87 == 0)

m.c108 = Constraint(expr= - m.x67 + m.x88 == 0)

m.c109 = Constraint(expr= - m.x69 + m.x89 == 0)

m.c110 = Constraint(expr= - m.x71 + m.x90 == 0)

m.c111 = Constraint(expr= - m.x73 + m.x91 == 0)

m.c112 = Constraint(expr= - m.x75 + m.x92 == 0)

m.c113 = Constraint(expr= - m.x77 + m.x93 == 0)

m.c114 = Constraint(expr= - m.x79 + m.x94 == 0)

m.c115 = Constraint(expr= - m.x81 + m.x95 == 0)

m.c116 = Constraint(expr= - m.x83 + m.x96 == 0)

m.c117 = Constraint(expr= - m.x85 + m.x97 == 0)

m.c118 = Constraint(expr= - m.x50 - m.x54 - m.x58 + m.x98 == 0)

m.c119 = Constraint(expr= - m.x51 - m.x55 - m.x59 + m.x99 == 0)

m.c120 = Constraint(expr= - m.x52 - m.x56 - m.x60 + m.x100 == 0)

m.c121 = Constraint(expr= - m.x53 - m.x57 - m.x61 + m.x101 == 0)

m.c122 = Constraint(expr= - m.x86 - m.x90 - m.x94 + m.x102 == 0)

m.c123 = Constraint(expr= - m.x87 - m.x91 - m.x95 + m.x103 == 0)

m.c124 = Constraint(expr= - m.x88 - m.x92 - m.x96 + m.x104 == 0)

m.c125 = Constraint(expr= - m.x89 - m.x93 - m.x97 + m.x105 == 0)

m.c126 = Constraint(expr=   m.x102 >= 0)

m.c127 = Constraint(expr=   m.x103 >= 0)

m.c128 = Constraint(expr=   m.x104 >= 0)

m.c129 = Constraint(expr=   m.x105 >= 0)

m.c130 = Constraint(expr= - m.x50 - m.x51 - m.x52 - m.x53 + m.x106 == 0)

m.c131 = Constraint(expr= - m.x54 - m.x55 - m.x56 - m.x57 + m.x107 == 0)

m.c132 = Constraint(expr= - m.x58 - m.x59 - m.x60 - m.x61 + m.x108 == 0)

m.c133 = Constraint(expr= - m.x86 - m.x87 - m.x88 - m.x89 + m.x109 == 0)

m.c134 = Constraint(expr= - m.x90 - m.x91 - m.x92 - m.x93 + m.x110 == 0)

m.c135 = Constraint(expr= - m.x94 - m.x95 - m.x96 - m.x97 + m.x111 == 0)
