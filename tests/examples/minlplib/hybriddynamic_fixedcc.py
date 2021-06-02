#  NLP written by GAMS Convert at 04/21/18 13:52:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        100      100        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        122      122        0        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        280      229       51        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(-1,1),initialize=-1)
m.x2 = Var(within=Reals,bounds=(-1,1),initialize=-1)
m.x3 = Var(within=Reals,bounds=(-1,1),initialize=-1)
m.x4 = Var(within=Reals,bounds=(-1,1),initialize=-1)
m.x5 = Var(within=Reals,bounds=(-1,1),initialize=-1)
m.x6 = Var(within=Reals,bounds=(-1,1),initialize=-1)
m.x7 = Var(within=Reals,bounds=(-1,1),initialize=-1)
m.x8 = Var(within=Reals,bounds=(-1,1),initialize=-1)
m.x9 = Var(within=Reals,bounds=(-1,1),initialize=-1)
m.x10 = Var(within=Reals,bounds=(-1,1),initialize=-1)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x34 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x58 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x60 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x61 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x62 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x63 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x64 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x65 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x66 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x67 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x68 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x69 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x70 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x71 = Var(within=Reals,bounds=(-2,-2),initialize=-2)
m.x72 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x76 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x78 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x80 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x81 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x82 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x83 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x84 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x85 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x86 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x87 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x88 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x89 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x90 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x91 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x92 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x93 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x94 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x95 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x96 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x97 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x98 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x99 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x100 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x101 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x102 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x103 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x104 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x105 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x106 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x107 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x108 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x109 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x110 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x111 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x117 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x119 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x121 = Var(within=Reals,bounds=(None,None),initialize=1)

m.obj = Objective(expr=(-1.66666666666667 + m.x121)**2 + 0.2*m.x101**2 + 0.2*m.x102**2 + 0.2*m.x103**2 + 0.2*m.x104**2
                        + 0.2*m.x105**2 + 0.2*m.x106**2 + 0.2*m.x107**2 + 0.2*m.x108**2 + 0.2*m.x109**2 + 0.2*m.x110**2
                        + 1000*(m.x61*m.x41 + m.x51*m.x31 + m.x62*m.x42 + m.x52*m.x32 + m.x63*m.x43 + m.x53*m.x33 + 
                       m.x64*m.x44 + m.x54*m.x34 + m.x65*m.x45 + m.x55*m.x35 + m.x66*m.x46 + m.x56*m.x36 + m.x67*m.x47
                        + m.x57*m.x37 + m.x68*m.x48 + m.x58*m.x38 + m.x69*m.x49 + m.x59*m.x39 + m.x70*m.x50 + m.x60*
                       m.x40), sense=minimize)

m.c2 = Constraint(expr= - m.x81 + m.x91 == 0.2)

m.c3 = Constraint(expr= - m.x82 + m.x92 == 0.2)

m.c4 = Constraint(expr= - m.x83 + m.x93 == 0.2)

m.c5 = Constraint(expr= - m.x84 + m.x94 == 0.2)

m.c6 = Constraint(expr= - m.x85 + m.x95 == 0.2)

m.c7 = Constraint(expr= - m.x86 + m.x96 == 0.2)

m.c8 = Constraint(expr= - m.x87 + m.x97 == 0.2)

m.c9 = Constraint(expr= - m.x88 + m.x98 == 0.2)

m.c10 = Constraint(expr= - m.x89 + m.x99 == 0.2)

m.c11 = Constraint(expr= - m.x90 + m.x100 == 0.2)

m.c12 = Constraint(expr= - m.x71 + m.x101 - 0.2*m.x111 == 0)

m.c13 = Constraint(expr= - m.x72 + m.x102 - 0.2*m.x112 == 0)

m.c14 = Constraint(expr= - m.x73 + m.x103 - 0.2*m.x113 == 0)

m.c15 = Constraint(expr= - m.x74 + m.x104 - 0.2*m.x114 == 0)

m.c16 = Constraint(expr= - m.x75 + m.x105 - 0.2*m.x115 == 0)

m.c17 = Constraint(expr= - m.x76 + m.x106 - 0.2*m.x116 == 0)

m.c18 = Constraint(expr= - m.x77 + m.x107 - 0.2*m.x117 == 0)

m.c19 = Constraint(expr= - m.x78 + m.x108 - 0.2*m.x118 == 0)

m.c20 = Constraint(expr= - m.x79 + m.x109 - 0.2*m.x119 == 0)

m.c21 = Constraint(expr= - m.x80 + m.x110 - 0.2*m.x120 == 0)

m.c22 = Constraint(expr= - m.x81 + m.x82 == 0.2)

m.c23 = Constraint(expr= - m.x82 + m.x83 == 0.2)

m.c24 = Constraint(expr= - m.x83 + m.x84 == 0.2)

m.c25 = Constraint(expr= - m.x84 + m.x85 == 0.2)

m.c26 = Constraint(expr= - m.x85 + m.x86 == 0.2)

m.c27 = Constraint(expr= - m.x86 + m.x87 == 0.2)

m.c28 = Constraint(expr= - m.x87 + m.x88 == 0.2)

m.c29 = Constraint(expr= - m.x88 + m.x89 == 0.2)

m.c30 = Constraint(expr= - m.x89 + m.x90 == 0.2)

m.c31 = Constraint(expr= - m.x71 + m.x72 - 0.2*m.x111 == 0)

m.c32 = Constraint(expr= - m.x72 + m.x73 - 0.2*m.x112 == 0)

m.c33 = Constraint(expr= - m.x73 + m.x74 - 0.2*m.x113 == 0)

m.c34 = Constraint(expr= - m.x74 + m.x75 - 0.2*m.x114 == 0)

m.c35 = Constraint(expr= - m.x75 + m.x76 - 0.2*m.x115 == 0)

m.c36 = Constraint(expr= - m.x76 + m.x77 - 0.2*m.x116 == 0)

m.c37 = Constraint(expr= - m.x77 + m.x78 - 0.2*m.x117 == 0)

m.c38 = Constraint(expr= - m.x78 + m.x79 - 0.2*m.x118 == 0)

m.c39 = Constraint(expr= - m.x79 + m.x80 - 0.2*m.x119 == 0)

m.c40 = Constraint(expr= - m.x80 - 0.2*m.x120 + m.x121 == 0)

m.c41 = Constraint(expr=   m.x1 + m.x111 == 2)

m.c42 = Constraint(expr=   m.x2 + m.x112 == 2)

m.c43 = Constraint(expr=   m.x3 + m.x113 == 2)

m.c44 = Constraint(expr=   m.x4 + m.x114 == 2)

m.c45 = Constraint(expr=   m.x5 + m.x115 == 2)

m.c46 = Constraint(expr=   m.x6 + m.x116 == 2)

m.c47 = Constraint(expr=   m.x7 + m.x117 == 2)

m.c48 = Constraint(expr=   m.x8 + m.x118 == 2)

m.c49 = Constraint(expr=   m.x9 + m.x119 == 2)

m.c50 = Constraint(expr=   m.x10 + m.x120 == 2)

m.c51 = Constraint(expr= - m.x11 + m.x21 + m.x101 == 0)

m.c52 = Constraint(expr= - m.x12 + m.x22 + m.x102 == 0)

m.c53 = Constraint(expr= - m.x13 + m.x23 + m.x103 == 0)

m.c54 = Constraint(expr= - m.x14 + m.x24 + m.x104 == 0)

m.c55 = Constraint(expr= - m.x15 + m.x25 + m.x105 == 0)

m.c56 = Constraint(expr= - m.x16 + m.x26 + m.x106 == 0)

m.c57 = Constraint(expr= - m.x17 + m.x27 + m.x107 == 0)

m.c58 = Constraint(expr= - m.x18 + m.x28 + m.x108 == 0)

m.c59 = Constraint(expr= - m.x19 + m.x29 + m.x109 == 0)

m.c60 = Constraint(expr= - m.x20 + m.x30 + m.x110 == 0)

m.c61 = Constraint(expr= - m.x11 + m.x31 == 0)

m.c62 = Constraint(expr= - m.x12 + m.x32 == 0)

m.c63 = Constraint(expr= - m.x13 + m.x33 == 0)

m.c64 = Constraint(expr= - m.x14 + m.x34 == 0)

m.c65 = Constraint(expr= - m.x15 + m.x35 == 0)

m.c66 = Constraint(expr= - m.x16 + m.x36 == 0)

m.c67 = Constraint(expr= - m.x17 + m.x37 == 0)

m.c68 = Constraint(expr= - m.x18 + m.x38 == 0)

m.c69 = Constraint(expr= - m.x19 + m.x39 == 0)

m.c70 = Constraint(expr= - m.x20 + m.x40 == 0)

m.c71 = Constraint(expr= - m.x21 + m.x41 == 0)

m.c72 = Constraint(expr= - m.x22 + m.x42 == 0)

m.c73 = Constraint(expr= - m.x23 + m.x43 == 0)

m.c74 = Constraint(expr= - m.x24 + m.x44 == 0)

m.c75 = Constraint(expr= - m.x25 + m.x45 == 0)

m.c76 = Constraint(expr= - m.x26 + m.x46 == 0)

m.c77 = Constraint(expr= - m.x27 + m.x47 == 0)

m.c78 = Constraint(expr= - m.x28 + m.x48 == 0)

m.c79 = Constraint(expr= - m.x29 + m.x49 == 0)

m.c80 = Constraint(expr= - m.x30 + m.x50 == 0)

m.c81 = Constraint(expr=   m.x1 + m.x51 == 1)

m.c82 = Constraint(expr=   m.x2 + m.x52 == 1)

m.c83 = Constraint(expr=   m.x3 + m.x53 == 1)

m.c84 = Constraint(expr=   m.x4 + m.x54 == 1)

m.c85 = Constraint(expr=   m.x5 + m.x55 == 1)

m.c86 = Constraint(expr=   m.x6 + m.x56 == 1)

m.c87 = Constraint(expr=   m.x7 + m.x57 == 1)

m.c88 = Constraint(expr=   m.x8 + m.x58 == 1)

m.c89 = Constraint(expr=   m.x9 + m.x59 == 1)

m.c90 = Constraint(expr=   m.x10 + m.x60 == 1)

m.c91 = Constraint(expr= - m.x1 + m.x61 == 1)

m.c92 = Constraint(expr= - m.x2 + m.x62 == 1)

m.c93 = Constraint(expr= - m.x3 + m.x63 == 1)

m.c94 = Constraint(expr= - m.x4 + m.x64 == 1)

m.c95 = Constraint(expr= - m.x5 + m.x65 == 1)

m.c96 = Constraint(expr= - m.x6 + m.x66 == 1)

m.c97 = Constraint(expr= - m.x7 + m.x67 == 1)

m.c98 = Constraint(expr= - m.x8 + m.x68 == 1)

m.c99 = Constraint(expr= - m.x9 + m.x69 == 1)

m.c100 = Constraint(expr= - m.x10 + m.x70 == 1)
