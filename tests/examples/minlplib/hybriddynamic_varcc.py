#  NLP written by GAMS Convert at 04/21/18 13:52:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        111      111        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        152      152        0        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        389      288      101        0
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
m.x71 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x72 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x73 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x74 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x75 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x76 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x77 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x78 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x79 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x80 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x81 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x82 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x83 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x84 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x85 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x86 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x87 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x88 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x89 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x90 = Var(within=Reals,bounds=(0,None),initialize=0.1)
m.x91 = Var(within=Reals,bounds=(0.16,0.24),initialize=0.2)
m.x92 = Var(within=Reals,bounds=(0.16,0.24),initialize=0.2)
m.x93 = Var(within=Reals,bounds=(0.16,0.24),initialize=0.2)
m.x94 = Var(within=Reals,bounds=(0.16,0.24),initialize=0.2)
m.x95 = Var(within=Reals,bounds=(0.16,0.24),initialize=0.2)
m.x96 = Var(within=Reals,bounds=(0.16,0.24),initialize=0.2)
m.x97 = Var(within=Reals,bounds=(0.16,0.24),initialize=0.2)
m.x98 = Var(within=Reals,bounds=(0.16,0.24),initialize=0.2)
m.x99 = Var(within=Reals,bounds=(0.16,0.24),initialize=0.2)
m.x100 = Var(within=Reals,bounds=(0.16,0.24),initialize=0.2)
m.x101 = Var(within=Reals,bounds=(-2,-2),initialize=-2)
m.x102 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x103 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x104 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x105 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x106 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x107 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x108 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x109 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x110 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x111 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x112 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x113 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x114 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x115 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x116 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x117 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x118 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x119 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x120 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x121 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x122 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x123 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x124 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x125 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x126 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x127 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x128 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x129 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x130 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x131 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x132 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x133 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x134 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x135 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x136 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x137 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x138 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x139 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x140 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x141 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x142 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x143 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x144 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x145 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x146 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x147 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x148 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x149 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x150 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x151 = Var(within=Reals,bounds=(None,None),initialize=1)

m.obj = Objective(expr=(-1.66666666666667 + m.x151)**2 + m.x131**2*m.x91 + m.x132**2*m.x92 + m.x133**2*m.x93 + m.x134**2
                       *m.x94 + m.x135**2*m.x95 + m.x136**2*m.x96 + m.x137**2*m.x97 + m.x138**2*m.x98 + m.x139**2*m.x99
                        + m.x140**2*m.x100 + 1000*(m.x81*m.x61 + m.x71*m.x51 + m.x82*m.x62 + m.x72*m.x52 + m.x83*m.x63
                        + m.x73*m.x53 + m.x84*m.x64 + m.x74*m.x54 + m.x85*m.x65 + m.x75*m.x55 + m.x86*m.x66 + m.x76*
                       m.x56 + m.x87*m.x67 + m.x77*m.x57 + m.x88*m.x68 + m.x78*m.x58 + m.x89*m.x69 + m.x79*m.x59 + m.x90
                       *m.x70 + m.x80*m.x60), sense=minimize)

m.c2 = Constraint(expr= - m.x91 - m.x111 + m.x121 == 0)

m.c3 = Constraint(expr= - m.x92 - m.x112 + m.x122 == 0)

m.c4 = Constraint(expr= - m.x93 - m.x113 + m.x123 == 0)

m.c5 = Constraint(expr= - m.x94 - m.x114 + m.x124 == 0)

m.c6 = Constraint(expr= - m.x95 - m.x115 + m.x125 == 0)

m.c7 = Constraint(expr= - m.x96 - m.x116 + m.x126 == 0)

m.c8 = Constraint(expr= - m.x97 - m.x117 + m.x127 == 0)

m.c9 = Constraint(expr= - m.x98 - m.x118 + m.x128 == 0)

m.c10 = Constraint(expr= - m.x99 - m.x119 + m.x129 == 0)

m.c11 = Constraint(expr= - m.x100 - m.x120 + m.x130 == 0)

m.c12 = Constraint(expr=-m.x91*m.x141 - m.x101 + m.x131 == 0)

m.c13 = Constraint(expr=-m.x92*m.x142 - m.x102 + m.x132 == 0)

m.c14 = Constraint(expr=-m.x93*m.x143 - m.x103 + m.x133 == 0)

m.c15 = Constraint(expr=-m.x94*m.x144 - m.x104 + m.x134 == 0)

m.c16 = Constraint(expr=-m.x95*m.x145 - m.x105 + m.x135 == 0)

m.c17 = Constraint(expr=-m.x96*m.x146 - m.x106 + m.x136 == 0)

m.c18 = Constraint(expr=-m.x97*m.x147 - m.x107 + m.x137 == 0)

m.c19 = Constraint(expr=-m.x98*m.x148 - m.x108 + m.x138 == 0)

m.c20 = Constraint(expr=-m.x99*m.x149 - m.x109 + m.x139 == 0)

m.c21 = Constraint(expr=-m.x100*m.x150 - m.x110 + m.x140 == 0)

m.c22 = Constraint(expr= - m.x91 - m.x111 + m.x112 == 0)

m.c23 = Constraint(expr= - m.x92 - m.x112 + m.x113 == 0)

m.c24 = Constraint(expr= - m.x93 - m.x113 + m.x114 == 0)

m.c25 = Constraint(expr= - m.x94 - m.x114 + m.x115 == 0)

m.c26 = Constraint(expr= - m.x95 - m.x115 + m.x116 == 0)

m.c27 = Constraint(expr= - m.x96 - m.x116 + m.x117 == 0)

m.c28 = Constraint(expr= - m.x97 - m.x117 + m.x118 == 0)

m.c29 = Constraint(expr= - m.x98 - m.x118 + m.x119 == 0)

m.c30 = Constraint(expr= - m.x99 - m.x119 + m.x120 == 0)

m.c31 = Constraint(expr=-m.x91*m.x141 - m.x101 + m.x102 == 0)

m.c32 = Constraint(expr=-m.x92*m.x142 - m.x102 + m.x103 == 0)

m.c33 = Constraint(expr=-m.x93*m.x143 - m.x103 + m.x104 == 0)

m.c34 = Constraint(expr=-m.x94*m.x144 - m.x104 + m.x105 == 0)

m.c35 = Constraint(expr=-m.x95*m.x145 - m.x105 + m.x106 == 0)

m.c36 = Constraint(expr=-m.x96*m.x146 - m.x106 + m.x107 == 0)

m.c37 = Constraint(expr=-m.x97*m.x147 - m.x107 + m.x108 == 0)

m.c38 = Constraint(expr=-m.x98*m.x148 - m.x108 + m.x109 == 0)

m.c39 = Constraint(expr=-m.x99*m.x149 - m.x109 + m.x110 == 0)

m.c40 = Constraint(expr=-m.x100*m.x150 - m.x110 + m.x151 == 0)

m.c41 = Constraint(expr=   m.x1 + m.x141 == 2)

m.c42 = Constraint(expr=   m.x2 + m.x142 == 2)

m.c43 = Constraint(expr=   m.x3 + m.x143 == 2)

m.c44 = Constraint(expr=   m.x4 + m.x144 == 2)

m.c45 = Constraint(expr=   m.x5 + m.x145 == 2)

m.c46 = Constraint(expr=   m.x6 + m.x146 == 2)

m.c47 = Constraint(expr=   m.x7 + m.x147 == 2)

m.c48 = Constraint(expr=   m.x8 + m.x148 == 2)

m.c49 = Constraint(expr=   m.x9 + m.x149 == 2)

m.c50 = Constraint(expr=   m.x10 + m.x150 == 2)

m.c51 = Constraint(expr= - m.x11 + m.x21 + m.x131 == 0)

m.c52 = Constraint(expr= - m.x12 + m.x22 + m.x132 == 0)

m.c53 = Constraint(expr= - m.x13 + m.x23 + m.x133 == 0)

m.c54 = Constraint(expr= - m.x14 + m.x24 + m.x134 == 0)

m.c55 = Constraint(expr= - m.x15 + m.x25 + m.x135 == 0)

m.c56 = Constraint(expr= - m.x16 + m.x26 + m.x136 == 0)

m.c57 = Constraint(expr= - m.x17 + m.x27 + m.x137 == 0)

m.c58 = Constraint(expr= - m.x18 + m.x28 + m.x138 == 0)

m.c59 = Constraint(expr= - m.x19 + m.x29 + m.x139 == 0)

m.c60 = Constraint(expr= - m.x20 + m.x30 + m.x140 == 0)

m.c61 = Constraint(expr= - m.x31 + m.x41 + m.x101 == 0)

m.c62 = Constraint(expr= - m.x32 + m.x42 + m.x102 == 0)

m.c63 = Constraint(expr= - m.x33 + m.x43 + m.x103 == 0)

m.c64 = Constraint(expr= - m.x34 + m.x44 + m.x104 == 0)

m.c65 = Constraint(expr= - m.x35 + m.x45 + m.x105 == 0)

m.c66 = Constraint(expr= - m.x36 + m.x46 + m.x106 == 0)

m.c67 = Constraint(expr= - m.x37 + m.x47 + m.x107 == 0)

m.c68 = Constraint(expr= - m.x38 + m.x48 + m.x108 == 0)

m.c69 = Constraint(expr= - m.x39 + m.x49 + m.x109 == 0)

m.c70 = Constraint(expr= - m.x40 + m.x50 + m.x110 == 0)

m.c71 = Constraint(expr= - m.x11 - m.x31 + m.x51 == 0)

m.c72 = Constraint(expr= - m.x12 - m.x32 + m.x52 == 0)

m.c73 = Constraint(expr= - m.x13 - m.x33 + m.x53 == 0)

m.c74 = Constraint(expr= - m.x14 - m.x34 + m.x54 == 0)

m.c75 = Constraint(expr= - m.x15 - m.x35 + m.x55 == 0)

m.c76 = Constraint(expr= - m.x16 - m.x36 + m.x56 == 0)

m.c77 = Constraint(expr= - m.x17 - m.x37 + m.x57 == 0)

m.c78 = Constraint(expr= - m.x18 - m.x38 + m.x58 == 0)

m.c79 = Constraint(expr= - m.x19 - m.x39 + m.x59 == 0)

m.c80 = Constraint(expr= - m.x20 - m.x40 + m.x60 == 0)

m.c81 = Constraint(expr= - m.x21 - m.x41 + m.x61 == 0)

m.c82 = Constraint(expr= - m.x22 - m.x42 + m.x62 == 0)

m.c83 = Constraint(expr= - m.x23 - m.x43 + m.x63 == 0)

m.c84 = Constraint(expr= - m.x24 - m.x44 + m.x64 == 0)

m.c85 = Constraint(expr= - m.x25 - m.x45 + m.x65 == 0)

m.c86 = Constraint(expr= - m.x26 - m.x46 + m.x66 == 0)

m.c87 = Constraint(expr= - m.x27 - m.x47 + m.x67 == 0)

m.c88 = Constraint(expr= - m.x28 - m.x48 + m.x68 == 0)

m.c89 = Constraint(expr= - m.x29 - m.x49 + m.x69 == 0)

m.c90 = Constraint(expr= - m.x30 - m.x50 + m.x70 == 0)

m.c91 = Constraint(expr=   m.x1 + m.x71 == 1)

m.c92 = Constraint(expr=   m.x2 + m.x72 == 1)

m.c93 = Constraint(expr=   m.x3 + m.x73 == 1)

m.c94 = Constraint(expr=   m.x4 + m.x74 == 1)

m.c95 = Constraint(expr=   m.x5 + m.x75 == 1)

m.c96 = Constraint(expr=   m.x6 + m.x76 == 1)

m.c97 = Constraint(expr=   m.x7 + m.x77 == 1)

m.c98 = Constraint(expr=   m.x8 + m.x78 == 1)

m.c99 = Constraint(expr=   m.x9 + m.x79 == 1)

m.c100 = Constraint(expr=   m.x10 + m.x80 == 1)

m.c101 = Constraint(expr= - m.x1 + m.x81 == 1)

m.c102 = Constraint(expr= - m.x2 + m.x82 == 1)

m.c103 = Constraint(expr= - m.x3 + m.x83 == 1)

m.c104 = Constraint(expr= - m.x4 + m.x84 == 1)

m.c105 = Constraint(expr= - m.x5 + m.x85 == 1)

m.c106 = Constraint(expr= - m.x6 + m.x86 == 1)

m.c107 = Constraint(expr= - m.x7 + m.x87 == 1)

m.c108 = Constraint(expr= - m.x8 + m.x88 == 1)

m.c109 = Constraint(expr= - m.x9 + m.x89 == 1)

m.c110 = Constraint(expr= - m.x10 + m.x90 == 1)

m.c111 = Constraint(expr=   m.x91 + m.x92 + m.x93 + m.x94 + m.x95 + m.x96 + m.x97 + m.x98 + m.x99 + m.x100 == 2)
