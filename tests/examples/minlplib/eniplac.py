#  MINLP written by GAMS Convert at 04/21/18 13:51:42
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        190       88       30       72        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        142      118       24        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        511      463       48        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=250)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=170)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=260)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=510)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=250)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=170)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=260)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=510)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=250)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=170)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=260)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=510)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=250)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=170)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=260)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=510)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=250)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=170)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=260)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=510)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=250)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=170)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=260)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=510)
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
m.x38 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x97 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,500),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,None),initialize=0)
m.b119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b128 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b129 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b130 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b131 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b132 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b133 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b134 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b135 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b136 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b137 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b138 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b139 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b140 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b141 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b142 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr= - m.x97 + m.x112 + m.x113, sense=minimize)

m.c1 = Constraint(expr= - 3.3*m.x73 - 3.2*m.x74 - 3.1*m.x75 - 3.25*m.x76 - 3.3*m.x77 - 3.2*m.x78 - 3.1*m.x79
                        - 3.25*m.x80 - 3.3*m.x81 - 3.2*m.x82 - 3.1*m.x83 - 3.25*m.x84 - 3.3*m.x85 - 3.2*m.x86
                        - 3.1*m.x87 - 3.25*m.x88 - 3.3*m.x89 - 3.2*m.x90 - 3.1*m.x91 - 3.25*m.x92 - 3.3*m.x93
                        - 3.2*m.x94 - 3.1*m.x95 - 3.25*m.x96 + m.x113 == 0)

m.c2 = Constraint(expr= - 33*m.x105 - 33*m.x106 - 33*m.x107 - 33*m.x108 - 33*m.x109 - 33*m.x110 + m.x112 == 0)

m.c3 = Constraint(expr=   m.x25 - m.b119 == 0)

m.c4 = Constraint(expr=   m.x26 - m.b120 == 0)

m.c5 = Constraint(expr=   m.x27 - m.b121 == 0)

m.c6 = Constraint(expr=   m.x28 - m.b122 == 0)

m.c7 = Constraint(expr=   m.x29 - m.b123 == 0)

m.c8 = Constraint(expr=   m.x30 - m.b124 == 0)

m.c9 = Constraint(expr=   m.x31 - m.b125 == 0)

m.c10 = Constraint(expr=   m.x32 - m.b126 == 0)

m.c11 = Constraint(expr=   m.x33 - m.b127 == 0)

m.c12 = Constraint(expr=   m.x34 - m.b128 == 0)

m.c13 = Constraint(expr=   m.x35 - m.b129 == 0)

m.c14 = Constraint(expr=   m.x36 - m.b130 == 0)

m.c15 = Constraint(expr=   m.x37 - m.b131 == 0)

m.c16 = Constraint(expr=   m.x38 - m.b132 == 0)

m.c17 = Constraint(expr=   m.x39 - m.b133 == 0)

m.c18 = Constraint(expr=   m.x40 - m.b134 == 0)

m.c19 = Constraint(expr=   m.x41 - m.b135 == 0)

m.c20 = Constraint(expr=   m.x42 - m.b136 == 0)

m.c21 = Constraint(expr=   m.x43 - m.b137 == 0)

m.c22 = Constraint(expr=   m.x44 - m.b138 == 0)

m.c23 = Constraint(expr=   m.x45 - m.b139 == 0)

m.c24 = Constraint(expr=   m.x46 - m.b140 == 0)

m.c25 = Constraint(expr=   m.x47 - m.b141 == 0)

m.c26 = Constraint(expr=   m.x48 - m.b142 == 0)

m.c27 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 - m.x99 + m.x105 == 1170)

m.c28 = Constraint(expr=   m.x5 + m.x6 + m.x7 + m.x8 - m.x100 + m.x106 == 950)

m.c29 = Constraint(expr=   m.x9 + m.x10 + m.x11 + m.x12 - m.x101 + m.x107 == 950)

m.c30 = Constraint(expr=   m.x13 + m.x14 + m.x15 + m.x16 - m.x102 + m.x108 == 700)

m.c31 = Constraint(expr=   m.x17 + m.x18 + m.x19 + m.x20 - m.x103 + m.x109 == 600)

m.c32 = Constraint(expr=   m.x21 + m.x22 + m.x23 + m.x24 - m.x104 + m.x110 == 250)

m.c33 = Constraint(expr=-(601.56 + 0.0131*m.x1**2 + 1.0622*m.x1)*m.x25 + m.x73 == 0)

m.c34 = Constraint(expr=-(-92.8095 + 10.04286*m.x2 - 0.01048*m.x2**2)*m.x26 + m.x74 == 0)

m.c35 = Constraint(expr=-(657.32 + 0.018317*m.x3**2)*m.x27 + m.x75 == 0)

m.c36 = Constraint(expr=-(222.2 + 0.0001*m.x4**2 + 6.2749*m.x4)*m.x28 + m.x76 == 0)

m.c37 = Constraint(expr=-(601.56 + 0.0131*m.x5**2 + 1.0622*m.x5)*m.x29 + m.x77 == 0)

m.c38 = Constraint(expr=-(-92.8095 + 10.04286*m.x6 - 0.01048*m.x6**2)*m.x30 + m.x78 == 0)

m.c39 = Constraint(expr=-(657.32 + 0.018317*m.x7**2)*m.x31 + m.x79 == 0)

m.c40 = Constraint(expr=-(222.2 + 0.0001*m.x8**2 + 6.2749*m.x8)*m.x32 + m.x80 == 0)

m.c41 = Constraint(expr=-(601.56 + 0.0131*m.x9**2 + 1.0622*m.x9)*m.x33 + m.x81 == 0)

m.c42 = Constraint(expr=-(-92.8095 + 10.04286*m.x10 - 0.01048*m.x10**2)*m.x34 + m.x82 == 0)

m.c43 = Constraint(expr=-(657.32 + 0.018317*m.x11**2)*m.x35 + m.x83 == 0)

m.c44 = Constraint(expr=-(222.2 + 0.0001*m.x12**2 + 6.2749*m.x12)*m.x36 + m.x84 == 0)

m.c45 = Constraint(expr=-(601.56 + 0.0131*m.x13**2 + 1.0622*m.x13)*m.x37 + m.x85 == 0)

m.c46 = Constraint(expr=-(-92.8095 + 10.04286*m.x14 - 0.01048*m.x14**2)*m.x38 + m.x86 == 0)

m.c47 = Constraint(expr=-(657.32 + 0.018317*m.x15**2)*m.x39 + m.x87 == 0)

m.c48 = Constraint(expr=-(222.2 + 0.0001*m.x16**2 + 6.2749*m.x16)*m.x40 + m.x88 == 0)

m.c49 = Constraint(expr=-(601.56 + 0.0131*m.x17**2 + 1.0622*m.x17)*m.x41 + m.x89 == 0)

m.c50 = Constraint(expr=-(-92.8095 + 10.04286*m.x18 - 0.01048*m.x18**2)*m.x42 + m.x90 == 0)

m.c51 = Constraint(expr=-(657.32 + 0.018317*m.x19**2)*m.x43 + m.x91 == 0)

m.c52 = Constraint(expr=-(222.2 + 0.0001*m.x20**2 + 6.2749*m.x20)*m.x44 + m.x92 == 0)

m.c53 = Constraint(expr=-(601.56 + 0.0131*m.x21**2 + 1.0622*m.x21)*m.x45 + m.x93 == 0)

m.c54 = Constraint(expr=-(-92.8095 + 10.04286*m.x22 - 0.01048*m.x22**2)*m.x46 + m.x94 == 0)

m.c55 = Constraint(expr=-(657.32 + 0.018317*m.x23**2)*m.x47 + m.x95 == 0)

m.c56 = Constraint(expr=-(222.2 + 0.0001*m.x24**2 + 6.2749*m.x24)*m.x48 + m.x96 == 0)

m.c57 = Constraint(expr= - m.x73 - m.x77 - m.x81 - m.x85 - m.x89 - m.x93 + m.x114 == 0)

m.c58 = Constraint(expr= - m.x74 - m.x78 - m.x82 - m.x86 - m.x90 - m.x94 + m.x115 == 0)

m.c59 = Constraint(expr= - m.x75 - m.x79 - m.x83 - m.x87 - m.x91 - m.x95 + m.x116 == 0)

m.c60 = Constraint(expr= - m.x76 - m.x80 - m.x84 - m.x88 - m.x92 - m.x96 + m.x117 == 0)

m.c61 = Constraint(expr=   m.x98 == 231000)

m.c62 = Constraint(expr= - 30*m.x99 - 30*m.x100 - 30*m.x101 - 30*m.x102 - 30*m.x103 - 30*m.x104 + m.x111 == 0)

m.c63 = Constraint(expr=   m.x97 - m.x98 - m.x111 == 0)

m.c64 = Constraint(expr= - m.x1 + m.x5 <= 500)

m.c65 = Constraint(expr= - m.x2 + m.x6 <= 500)

m.c66 = Constraint(expr= - m.x3 + m.x7 <= 500)

m.c67 = Constraint(expr= - m.x4 + m.x8 <= 500)

m.c68 = Constraint(expr= - m.x5 + m.x9 <= 500)

m.c69 = Constraint(expr= - m.x6 + m.x10 <= 500)

m.c70 = Constraint(expr= - m.x7 + m.x11 <= 500)

m.c71 = Constraint(expr= - m.x8 + m.x12 <= 500)

m.c72 = Constraint(expr= - m.x9 + m.x13 <= 500)

m.c73 = Constraint(expr= - m.x10 + m.x14 <= 500)

m.c74 = Constraint(expr= - m.x11 + m.x15 <= 500)

m.c75 = Constraint(expr= - m.x12 + m.x16 <= 500)

m.c76 = Constraint(expr= - m.x13 + m.x17 <= 500)

m.c77 = Constraint(expr= - m.x14 + m.x18 <= 500)

m.c78 = Constraint(expr= - m.x15 + m.x19 <= 500)

m.c79 = Constraint(expr= - m.x16 + m.x20 <= 500)

m.c80 = Constraint(expr= - m.x17 + m.x21 <= 500)

m.c81 = Constraint(expr= - m.x18 + m.x22 <= 500)

m.c82 = Constraint(expr= - m.x19 + m.x23 <= 500)

m.c83 = Constraint(expr= - m.x20 + m.x24 <= 500)

m.c84 = Constraint(expr=   m.x1 - m.x5 <= 500)

m.c85 = Constraint(expr=   m.x2 - m.x6 <= 500)

m.c86 = Constraint(expr=   m.x3 - m.x7 <= 500)

m.c87 = Constraint(expr=   m.x4 - m.x8 <= 500)

m.c88 = Constraint(expr=   m.x5 - m.x9 <= 500)

m.c89 = Constraint(expr=   m.x6 - m.x10 <= 500)

m.c90 = Constraint(expr=   m.x7 - m.x11 <= 500)

m.c91 = Constraint(expr=   m.x8 - m.x12 <= 500)

m.c92 = Constraint(expr=   m.x9 - m.x13 <= 500)

m.c93 = Constraint(expr=   m.x10 - m.x14 <= 500)

m.c94 = Constraint(expr=   m.x11 - m.x15 <= 500)

m.c95 = Constraint(expr=   m.x12 - m.x16 <= 500)

m.c96 = Constraint(expr=   m.x13 - m.x17 <= 500)

m.c97 = Constraint(expr=   m.x14 - m.x18 <= 500)

m.c98 = Constraint(expr=   m.x15 - m.x19 <= 500)

m.c99 = Constraint(expr=   m.x16 - m.x20 <= 500)

m.c100 = Constraint(expr=   m.x17 - m.x21 <= 500)

m.c101 = Constraint(expr=   m.x18 - m.x22 <= 500)

m.c102 = Constraint(expr=   m.x19 - m.x23 <= 500)

m.c103 = Constraint(expr=   m.x20 - m.x24 <= 500)

m.c104 = Constraint(expr=   m.x1 <= 800)

m.c105 = Constraint(expr=   m.x2 <= 650)

m.c106 = Constraint(expr=   m.x3 <= 660)

m.c107 = Constraint(expr=   m.x4 <= 750)

m.c108 = Constraint(expr= - m.x1 <= 200)

m.c109 = Constraint(expr= - m.x2 <= 350)

m.c110 = Constraint(expr= - m.x3 <= 340)

m.c111 = Constraint(expr= - m.x4 <= 250)

m.c112 = Constraint(expr=   m.x1 + m.x49 - 250*m.b119 == 0)

m.c113 = Constraint(expr=   m.x2 + m.x50 - 170*m.b120 == 0)

m.c114 = Constraint(expr=   m.x3 + m.x51 - 260*m.b121 == 0)

m.c115 = Constraint(expr=   m.x4 + m.x52 - 510*m.b122 == 0)

m.c116 = Constraint(expr=   m.x5 + m.x53 - 250*m.b123 == 0)

m.c117 = Constraint(expr=   m.x6 + m.x54 - 170*m.b124 == 0)

m.c118 = Constraint(expr=   m.x7 + m.x55 - 260*m.b125 == 0)

m.c119 = Constraint(expr=   m.x8 + m.x56 - 510*m.b126 == 0)

m.c120 = Constraint(expr=   m.x9 + m.x57 - 250*m.b127 == 0)

m.c121 = Constraint(expr=   m.x10 + m.x58 - 170*m.b128 == 0)

m.c122 = Constraint(expr=   m.x11 + m.x59 - 260*m.b129 == 0)

m.c123 = Constraint(expr=   m.x12 + m.x60 - 510*m.b130 == 0)

m.c124 = Constraint(expr=   m.x13 + m.x61 - 250*m.b131 == 0)

m.c125 = Constraint(expr=   m.x14 + m.x62 - 170*m.b132 == 0)

m.c126 = Constraint(expr=   m.x15 + m.x63 - 260*m.b133 == 0)

m.c127 = Constraint(expr=   m.x16 + m.x64 - 510*m.b134 == 0)

m.c128 = Constraint(expr=   m.x17 + m.x65 - 250*m.b135 == 0)

m.c129 = Constraint(expr=   m.x18 + m.x66 - 170*m.b136 == 0)

m.c130 = Constraint(expr=   m.x19 + m.x67 - 260*m.b137 == 0)

m.c131 = Constraint(expr=   m.x20 + m.x68 - 510*m.b138 == 0)

m.c132 = Constraint(expr=   m.x21 + m.x69 - 250*m.b139 == 0)

m.c133 = Constraint(expr=   m.x22 + m.x70 - 170*m.b140 == 0)

m.c134 = Constraint(expr=   m.x23 + m.x71 - 260*m.b141 == 0)

m.c135 = Constraint(expr=   m.x24 + m.x72 - 510*m.b142 == 0)

m.c136 = Constraint(expr=   m.x49 + m.x50 + m.x51 + m.x52 >= 25)

m.c137 = Constraint(expr=   m.x53 + m.x54 + m.x55 + m.x56 >= 25)

m.c138 = Constraint(expr=   m.x57 + m.x58 + m.x59 + m.x60 >= 25)

m.c139 = Constraint(expr=   m.x61 + m.x62 + m.x63 + m.x64 >= 25)

m.c140 = Constraint(expr=   m.x65 + m.x66 + m.x67 + m.x68 >= 25)

m.c141 = Constraint(expr=   m.x69 + m.x70 + m.x71 + m.x72 >= 25)

m.c142 = Constraint(expr=   m.x1 - 250*m.b119 <= 0)

m.c143 = Constraint(expr=   m.x2 - 170*m.b120 <= 0)

m.c144 = Constraint(expr=   m.x3 - 260*m.b121 <= 0)

m.c145 = Constraint(expr=   m.x4 - 510*m.b122 <= 0)

m.c146 = Constraint(expr=   m.x5 - 250*m.b123 <= 0)

m.c147 = Constraint(expr=   m.x6 - 170*m.b124 <= 0)

m.c148 = Constraint(expr=   m.x7 - 260*m.b125 <= 0)

m.c149 = Constraint(expr=   m.x8 - 510*m.b126 <= 0)

m.c150 = Constraint(expr=   m.x9 - 250*m.b127 <= 0)

m.c151 = Constraint(expr=   m.x10 - 170*m.b128 <= 0)

m.c152 = Constraint(expr=   m.x11 - 260*m.b129 <= 0)

m.c153 = Constraint(expr=   m.x12 - 510*m.b130 <= 0)

m.c154 = Constraint(expr=   m.x13 - 250*m.b131 <= 0)

m.c155 = Constraint(expr=   m.x14 - 170*m.b132 <= 0)

m.c156 = Constraint(expr=   m.x15 - 260*m.b133 <= 0)

m.c157 = Constraint(expr=   m.x16 - 510*m.b134 <= 0)

m.c158 = Constraint(expr=   m.x17 - 250*m.b135 <= 0)

m.c159 = Constraint(expr=   m.x18 - 170*m.b136 <= 0)

m.c160 = Constraint(expr=   m.x19 - 260*m.b137 <= 0)

m.c161 = Constraint(expr=   m.x20 - 510*m.b138 <= 0)

m.c162 = Constraint(expr=   m.x21 - 250*m.b139 <= 0)

m.c163 = Constraint(expr=   m.x22 - 170*m.b140 <= 0)

m.c164 = Constraint(expr=   m.x23 - 260*m.b141 <= 0)

m.c165 = Constraint(expr=   m.x24 - 510*m.b142 <= 0)

m.c166 = Constraint(expr=   m.x1 - 140*m.b119 >= 0)

m.c167 = Constraint(expr=   m.x2 - 140*m.b120 >= 0)

m.c168 = Constraint(expr=   m.x3 - 140*m.b121 >= 0)

m.c169 = Constraint(expr=   m.x4 - 160*m.b122 >= 0)

m.c170 = Constraint(expr=   m.x5 - 140*m.b123 >= 0)

m.c171 = Constraint(expr=   m.x6 - 140*m.b124 >= 0)

m.c172 = Constraint(expr=   m.x7 - 140*m.b125 >= 0)

m.c173 = Constraint(expr=   m.x8 - 160*m.b126 >= 0)

m.c174 = Constraint(expr=   m.x9 - 140*m.b127 >= 0)

m.c175 = Constraint(expr=   m.x10 - 140*m.b128 >= 0)

m.c176 = Constraint(expr=   m.x11 - 140*m.b129 >= 0)

m.c177 = Constraint(expr=   m.x12 - 160*m.b130 >= 0)

m.c178 = Constraint(expr=   m.x13 - 140*m.b131 >= 0)

m.c179 = Constraint(expr=   m.x14 - 140*m.b132 >= 0)

m.c180 = Constraint(expr=   m.x15 - 140*m.b133 >= 0)

m.c181 = Constraint(expr=   m.x16 - 160*m.b134 >= 0)

m.c182 = Constraint(expr=   m.x17 - 140*m.b135 >= 0)

m.c183 = Constraint(expr=   m.x18 - 140*m.b136 >= 0)

m.c184 = Constraint(expr=   m.x19 - 140*m.b137 >= 0)

m.c185 = Constraint(expr=   m.x20 - 160*m.b138 >= 0)

m.c186 = Constraint(expr=   m.x21 - 140*m.b139 >= 0)

m.c187 = Constraint(expr=   m.x22 - 140*m.b140 >= 0)

m.c188 = Constraint(expr=   m.x23 - 140*m.b141 >= 0)

m.c189 = Constraint(expr=   m.x24 - 160*m.b142 >= 0)
