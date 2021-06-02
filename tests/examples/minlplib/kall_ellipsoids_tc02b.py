#  NLP written by GAMS Convert at 04/21/18 13:52:27
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        129      110        3       16        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        125      125        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        384      251      133        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(-1.69454444444444,1.69454444444444),initialize=0)
m.x24 = Var(within=Reals,bounds=(-1.69454444444444,1.69454444444444),initialize=0)
m.x25 = Var(within=Reals,bounds=(-1.69454444444444,1.69454444444444),initialize=0)
m.x26 = Var(within=Reals,bounds=(-1.69444444444444,1.69444444444444),initialize=0)
m.x27 = Var(within=Reals,bounds=(-1.69454444444444,1.69454444444444),initialize=0)
m.x28 = Var(within=Reals,bounds=(-1.69454444444444,1.69454444444444),initialize=0)
m.x29 = Var(within=Reals,bounds=(-1.69444444444444,1.69444444444444),initialize=0)
m.x30 = Var(within=Reals,bounds=(-1.69444444444444,1.69444444444444),initialize=0)
m.x31 = Var(within=Reals,bounds=(-1.69454444444444,1.69454444444444),initialize=0)
m.x32 = Var(within=Reals,bounds=(-3.48536077097506,3.48536077097506),initialize=0)
m.x33 = Var(within=Reals,bounds=(-3.48536077097506,3.48536077097506),initialize=0)
m.x34 = Var(within=Reals,bounds=(-3.48536077097506,3.48536077097506),initialize=0)
m.x35 = Var(within=Reals,bounds=(-3.48526077097506,3.48526077097506),initialize=0)
m.x36 = Var(within=Reals,bounds=(-3.48536077097506,3.48536077097506),initialize=0)
m.x37 = Var(within=Reals,bounds=(-3.48536077097506,3.48536077097506),initialize=0)
m.x38 = Var(within=Reals,bounds=(-3.48526077097506,3.48526077097506),initialize=0)
m.x39 = Var(within=Reals,bounds=(-3.48526077097506,3.48526077097506),initialize=0)
m.x40 = Var(within=Reals,bounds=(-3.48536077097506,3.48536077097506),initialize=0)
m.x41 = Var(within=Reals,bounds=(-1,1),initialize=1)
m.x42 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x43 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x44 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x45 = Var(within=Reals,bounds=(-1,1),initialize=1)
m.x46 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x47 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x48 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x49 = Var(within=Reals,bounds=(-1,1),initialize=1)
m.x50 = Var(within=Reals,bounds=(-1,1),initialize=1)
m.x51 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x52 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x53 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x54 = Var(within=Reals,bounds=(-1,1),initialize=1)
m.x55 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x56 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x57 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x58 = Var(within=Reals,bounds=(-1,1),initialize=1)
m.x59 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x60 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x61 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x62 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x63 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x64 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x65 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x66 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x67 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x68 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x69 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x70 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x71 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x72 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x73 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x74 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x75 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x76 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x77 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x78 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x79 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x80 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x81 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x82 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x83 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x84 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x85 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x86 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x87 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x88 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x89 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x90 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x91 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x92 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x93 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x94 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x95 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x96 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x97 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x98 = Var(within=Reals,bounds=(16.9646003293849,None),initialize=16.9646003293849)
m.x99 = Var(within=Reals,bounds=(0.333333333333333,0.666666666666667),initialize=0.333333333333333)
m.x100 = Var(within=Reals,bounds=(0.333333333333333,0.666666666666667),initialize=0.333333333333333)
m.x101 = Var(within=Reals,bounds=(0.333333333333333,0.666666666666667),initialize=0.333333333333333)
m.x102 = Var(within=Reals,bounds=(0.666666666666667,1.42857142857143),initialize=0.666666666666667)
m.x103 = Var(within=Reals,bounds=(0.666666666666667,1.42857142857143),initialize=0.666666666666667)
m.x104 = Var(within=Reals,bounds=(0.666666666666667,1.42857142857143),initialize=0.666666666666667)
m.x105 = Var(within=Reals,bounds=(4.5,7),initialize=4.5)
m.x106 = Var(within=Reals,bounds=(2.5,4),initialize=2.5)
m.x107 = Var(within=Reals,bounds=(2,4),initialize=2)
m.x108 = Var(within=Reals,bounds=(1,6),initialize=1)
m.x109 = Var(within=Reals,bounds=(1,3),initialize=1)
m.x110 = Var(within=Reals,bounds=(1,3),initialize=1)
m.x111 = Var(within=Reals,bounds=(0.7,6.3),initialize=0.7)
m.x112 = Var(within=Reals,bounds=(0.7,3.3),initialize=0.7)
m.x113 = Var(within=Reals,bounds=(0.7,3.3),initialize=0.7)
m.x114 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,4),initialize=0)

m.obj = Objective(expr=   m.x98, sense=minimize)

m.c2 = Constraint(expr=-m.x105*m.x106*m.x107 + m.x98 == 0)

m.c3 = Constraint(expr=m.x41*m.x45*m.x49 - m.x41*m.x46*m.x48 - m.x42*m.x44*m.x49 + m.x42*m.x47*m.x46 + m.x44*m.x43*m.x48
                        - m.x43*m.x45*m.x47 == 1)

m.c4 = Constraint(expr=m.x50*m.x54*m.x58 - m.x50*m.x55*m.x57 - m.x51*m.x53*m.x58 + m.x51*m.x56*m.x55 + m.x53*m.x52*m.x57
                        - m.x52*m.x54*m.x56 == 1)

m.c5 = Constraint(expr=   m.x62 + m.x63 + m.x64 == 1)

m.c6 = Constraint(expr=   m.x65 + m.x66 + m.x67 == 0)

m.c7 = Constraint(expr=   m.x68 + m.x69 + m.x70 == 0)

m.c8 = Constraint(expr=   m.x71 + m.x72 + m.x73 == 1)

m.c9 = Constraint(expr=   m.x74 + m.x75 + m.x76 == 0)

m.c10 = Constraint(expr=   m.x77 + m.x78 + m.x79 == 1)

m.c11 = Constraint(expr=   m.x80 + m.x81 + m.x82 == 1)

m.c12 = Constraint(expr=   m.x83 + m.x84 + m.x85 == 0)

m.c13 = Constraint(expr=   m.x86 + m.x87 + m.x88 == 0)

m.c14 = Constraint(expr=   m.x89 + m.x90 + m.x91 == 1)

m.c15 = Constraint(expr=   m.x92 + m.x93 + m.x94 == 0)

m.c16 = Constraint(expr=   m.x95 + m.x96 + m.x97 == 1)

m.c17 = Constraint(expr=   m.x23 - 0.25*m.x62 - 0.444444444444444*m.x63 - m.x64 == 0)

m.c18 = Constraint(expr=   m.x24 - 0.25*m.x65 - 0.444444444444444*m.x66 - m.x67 == 0)

m.c19 = Constraint(expr=   m.x25 - 0.25*m.x68 - 0.444444444444444*m.x69 - m.x70 == 0)

m.c20 = Constraint(expr=   m.x27 - 0.25*m.x71 - 0.444444444444444*m.x72 - m.x73 == 0)

m.c21 = Constraint(expr=   m.x28 - 0.25*m.x74 - 0.444444444444444*m.x75 - m.x76 == 0)

m.c22 = Constraint(expr=   m.x31 - 0.25*m.x77 - 0.444444444444444*m.x78 - m.x79 == 0)

m.c23 = Constraint(expr=   m.x32 - 0.444444444444444*m.x80 - m.x81 - 2.04081632653061*m.x82 == 0)

m.c24 = Constraint(expr=   m.x33 - 0.444444444444444*m.x83 - m.x84 - 2.04081632653061*m.x85 == 0)

m.c25 = Constraint(expr=   m.x34 - 0.444444444444444*m.x86 - m.x87 - 2.04081632653061*m.x88 == 0)

m.c26 = Constraint(expr=   m.x36 - 0.444444444444444*m.x89 - m.x90 - 2.04081632653061*m.x91 == 0)

m.c27 = Constraint(expr=   m.x37 - 0.444444444444444*m.x92 - m.x93 - 2.04081632653061*m.x94 == 0)

m.c28 = Constraint(expr=   m.x40 - 0.444444444444444*m.x95 - m.x96 - 2.04081632653061*m.x97 == 0)

m.c29 = Constraint(expr= - m.x24 + m.x26 == 0)

m.c30 = Constraint(expr= - m.x25 + m.x29 == 0)

m.c31 = Constraint(expr= - m.x28 + m.x30 == 0)

m.c32 = Constraint(expr= - m.x33 + m.x35 == 0)

m.c33 = Constraint(expr= - m.x34 + m.x38 == 0)

m.c34 = Constraint(expr= - m.x37 + m.x39 == 0)

m.c35 = Constraint(expr= - m.x105 + m.x108 <= -1)

m.c36 = Constraint(expr= - m.x106 + m.x109 <= -1)

m.c37 = Constraint(expr= - m.x107 + m.x110 <= -1)

m.c38 = Constraint(expr= - m.x105 + m.x111 <= -0.7)

m.c39 = Constraint(expr= - m.x106 + m.x112 <= -0.7)

m.c40 = Constraint(expr= - m.x107 + m.x113 <= -0.7)

m.c41 = Constraint(expr=m.x99**2 - (m.x27*m.x31 - m.x28*m.x30) == 0)

m.c42 = Constraint(expr=m.x102**2 - (m.x36*m.x40 - m.x37*m.x39) == 0)

m.c43 = Constraint(expr=m.x100**2 - (m.x23*m.x31 - m.x25*m.x29) == 0)

m.c44 = Constraint(expr=m.x103**2 - (m.x32*m.x40 - m.x34*m.x38) == 0)

m.c45 = Constraint(expr=m.x101**2 - (m.x23*m.x27 - m.x24*m.x26) == 0)

m.c46 = Constraint(expr=m.x104**2 - (m.x32*m.x36 - m.x33*m.x35) == 0)

m.c47 = Constraint(expr=   3*m.x99 - m.x108 + m.x114 == 0)

m.c48 = Constraint(expr=   3*m.x100 - m.x109 + m.x115 == 0)

m.c49 = Constraint(expr=   3*m.x101 - m.x110 + m.x116 == 0)

m.c50 = Constraint(expr=   1.05*m.x102 - m.x111 + m.x117 == 0)

m.c51 = Constraint(expr=   1.05*m.x103 - m.x112 + m.x118 == 0)

m.c52 = Constraint(expr=   1.05*m.x104 - m.x113 + m.x119 == 0)

m.c53 = Constraint(expr= - 3*m.x99 - m.x108 + m.x120 == 0)

m.c54 = Constraint(expr= - 3*m.x100 - m.x109 + m.x121 == 0)

m.c55 = Constraint(expr= - 3*m.x101 - m.x110 + m.x122 == 0)

m.c56 = Constraint(expr= - 1.05*m.x102 - m.x111 + m.x123 == 0)

m.c57 = Constraint(expr= - 1.05*m.x103 - m.x112 + m.x124 == 0)

m.c58 = Constraint(expr= - 1.05*m.x104 - m.x113 + m.x125 == 0)

m.c59 = Constraint(expr= - m.x105 + m.x120 <= 0)

m.c60 = Constraint(expr= - m.x106 + m.x121 <= 0)

m.c61 = Constraint(expr= - m.x107 + m.x122 <= 0)

m.c62 = Constraint(expr= - m.x105 + m.x123 <= 0)

m.c63 = Constraint(expr= - m.x106 + m.x124 <= 0)

m.c64 = Constraint(expr= - m.x107 + m.x125 <= 0)

m.c65 = Constraint(expr=   m.x105 - m.x106 >= 0)

m.c66 = Constraint(expr=   m.x106 - m.x107 >= 0)

m.c67 = Constraint(expr= - 0.5*m.x105 + m.x108 <= 0)

m.c68 = Constraint(expr= - 0.5*m.x106 + m.x109 <= 0)

m.c69 = Constraint(expr= - 0.5*m.x107 + m.x110 <= 0)

m.c70 = Constraint(expr=m.x59**2 + m.x60**2 + m.x61**2 == 1)

m.c71 = Constraint(expr=-m.x41*m.x41 + m.x62 == 0)

m.c72 = Constraint(expr=-m.x42*m.x42 + m.x63 == 0)

m.c73 = Constraint(expr=-m.x43*m.x43 + m.x64 == 0)

m.c74 = Constraint(expr=-m.x41*m.x44 + m.x65 == 0)

m.c75 = Constraint(expr=-m.x42*m.x45 + m.x66 == 0)

m.c76 = Constraint(expr=-m.x43*m.x46 + m.x67 == 0)

m.c77 = Constraint(expr=-m.x41*m.x47 + m.x68 == 0)

m.c78 = Constraint(expr=-m.x42*m.x48 + m.x69 == 0)

m.c79 = Constraint(expr=-m.x43*m.x49 + m.x70 == 0)

m.c80 = Constraint(expr=-m.x44*m.x44 + m.x71 == 0)

m.c81 = Constraint(expr=-m.x45*m.x45 + m.x72 == 0)

m.c82 = Constraint(expr=-m.x46*m.x46 + m.x73 == 0)

m.c83 = Constraint(expr=-m.x44*m.x47 + m.x74 == 0)

m.c84 = Constraint(expr=-m.x45*m.x48 + m.x75 == 0)

m.c85 = Constraint(expr=-m.x46*m.x49 + m.x76 == 0)

m.c86 = Constraint(expr=-m.x47*m.x47 + m.x77 == 0)

m.c87 = Constraint(expr=-m.x48*m.x48 + m.x78 == 0)

m.c88 = Constraint(expr=-m.x49*m.x49 + m.x79 == 0)

m.c89 = Constraint(expr=-m.x50*m.x50 + m.x80 == 0)

m.c90 = Constraint(expr=-m.x51*m.x51 + m.x81 == 0)

m.c91 = Constraint(expr=-m.x52*m.x52 + m.x82 == 0)

m.c92 = Constraint(expr=-m.x50*m.x53 + m.x83 == 0)

m.c93 = Constraint(expr=-m.x51*m.x54 + m.x84 == 0)

m.c94 = Constraint(expr=-m.x52*m.x55 + m.x85 == 0)

m.c95 = Constraint(expr=-m.x50*m.x56 + m.x86 == 0)

m.c96 = Constraint(expr=-m.x51*m.x57 + m.x87 == 0)

m.c97 = Constraint(expr=-m.x52*m.x58 + m.x88 == 0)

m.c98 = Constraint(expr=-m.x53*m.x53 + m.x89 == 0)

m.c99 = Constraint(expr=-m.x54*m.x54 + m.x90 == 0)

m.c100 = Constraint(expr=-m.x55*m.x55 + m.x91 == 0)

m.c101 = Constraint(expr=-m.x53*m.x56 + m.x92 == 0)

m.c102 = Constraint(expr=-m.x54*m.x57 + m.x93 == 0)

m.c103 = Constraint(expr=-m.x55*m.x58 + m.x94 == 0)

m.c104 = Constraint(expr=-m.x56*m.x56 + m.x95 == 0)

m.c105 = Constraint(expr=-m.x57*m.x57 + m.x96 == 0)

m.c106 = Constraint(expr=-m.x58*m.x58 + m.x97 == 0)

m.c107 = Constraint(expr=m.x107**3 - m.x98 <= 0)

m.c108 = Constraint(expr=   m.x20 - m.x108 + m.x111 == 0)

m.c109 = Constraint(expr=   m.x21 - m.x109 + m.x112 == 0)

m.c110 = Constraint(expr=   m.x22 - m.x110 + m.x113 == 0)

m.c111 = Constraint(expr=m.x59*m.x20 + m.x60*m.x21 + m.x61*m.x22 - (sqrt((m.x2*m.x59)**2 + (m.x5*m.x60)**2 + (m.x8*m.x61
                         )**2 + (m.x3*m.x59)**2 + (m.x6*m.x60)**2 + (m.x9*m.x61)**2 + (m.x4*m.x59)**2 + (m.x7*m.x60)**2
                          + (m.x10*m.x61)**2) + sqrt((m.x11*m.x59)**2 + (m.x14*m.x60)**2 + (m.x17*m.x61)**2 + (m.x12*
                         m.x59)**2 + (m.x15*m.x60)**2 + (m.x18*m.x61)**2 + (m.x13*m.x59)**2 + (m.x16*m.x60)**2 + (m.x19*
                         m.x61)**2)) >= 0)

m.c112 = Constraint(expr=   m.x2 - 2*m.x41 == 0)

m.c113 = Constraint(expr=   m.x3 - 1.5*m.x42 == 0)

m.c114 = Constraint(expr=   m.x4 - m.x43 == 0)

m.c115 = Constraint(expr=   m.x5 - 2*m.x44 == 0)

m.c116 = Constraint(expr=   m.x6 - 1.5*m.x45 == 0)

m.c117 = Constraint(expr=   m.x7 - m.x46 == 0)

m.c118 = Constraint(expr=   m.x8 - 2*m.x47 == 0)

m.c119 = Constraint(expr=   m.x9 - 1.5*m.x48 == 0)

m.c120 = Constraint(expr=   m.x10 - m.x49 == 0)

m.c121 = Constraint(expr=   m.x11 - 1.5*m.x50 == 0)

m.c122 = Constraint(expr=   m.x12 - m.x51 == 0)

m.c123 = Constraint(expr=   m.x13 - 0.7*m.x52 == 0)

m.c124 = Constraint(expr=   m.x14 - 1.5*m.x53 == 0)

m.c125 = Constraint(expr=   m.x15 - m.x54 == 0)

m.c126 = Constraint(expr=   m.x16 - 0.7*m.x55 == 0)

m.c127 = Constraint(expr=   m.x17 - 1.5*m.x56 == 0)

m.c128 = Constraint(expr=   m.x18 - m.x57 == 0)

m.c129 = Constraint(expr=   m.x19 - 0.7*m.x58 == 0)
