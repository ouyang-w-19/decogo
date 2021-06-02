#  NLP written by GAMS Convert at 04/21/18 13:51:47
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         72       72        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        111      111        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        581      118      463        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x3 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x4 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x5 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x6 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x7 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x8 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x9 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x10 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x11 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x12 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x13 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x14 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x15 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x16 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x17 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x18 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x19 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x20 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x21 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x22 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x23 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x24 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x25 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x26 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x27 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x28 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x29 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x30 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x31 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x32 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x33 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x34 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x35 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x36 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x37 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x38 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x39 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x40 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x41 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x42 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x43 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x44 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x45 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x46 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x47 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x48 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x49 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x50 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x51 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x52 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x53 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x54 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x55 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x56 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x57 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x58 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x59 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x60 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x61 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x62 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x63 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x64 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x65 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x66 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x67 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x68 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x69 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x70 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x71 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x72 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x73 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x74 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x75 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x76 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x77 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x78 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x79 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x80 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x81 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x82 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x83 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x84 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x85 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x86 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x87 = Var(within=Reals,bounds=(0,10000),initialize=7731)
m.x88 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x89 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x90 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x91 = Var(within=Reals,bounds=(0,100),initialize=1)
m.x92 = Var(within=Reals,bounds=(0,50000),initialize=1)
m.x93 = Var(within=Reals,bounds=(0,50000),initialize=1)
m.x94 = Var(within=Reals,bounds=(0,50000),initialize=1)
m.x95 = Var(within=Reals,bounds=(0,50000),initialize=1)
m.x96 = Var(within=Reals,bounds=(0,50000),initialize=1)
m.x97 = Var(within=Reals,bounds=(300,1200),initialize=1200)
m.x98 = Var(within=Reals,bounds=(300,1200),initialize=1200)
m.x99 = Var(within=Reals,bounds=(300,1200),initialize=1200)
m.x100 = Var(within=Reals,bounds=(300,1200),initialize=1200)
m.x101 = Var(within=Reals,bounds=(300,1200),initialize=1200)
m.x102 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,100000),initialize=0)

m.obj = Objective(expr= - m.x90, sense=minimize)

m.c2 = Constraint(expr= - m.x2 - m.x3 - m.x4 - m.x5 - m.x6 == -7731)

m.c3 = Constraint(expr= - m.x2 + m.x7 - m.x57 - m.x62 - m.x67 - m.x72 - m.x77 == 0)

m.c4 = Constraint(expr= - m.x3 + m.x8 - m.x58 - m.x63 - m.x68 - m.x73 - m.x78 == 0)

m.c5 = Constraint(expr= - m.x4 + m.x9 - m.x59 - m.x64 - m.x69 - m.x74 - m.x79 == 0)

m.c6 = Constraint(expr= - m.x5 + m.x10 - m.x60 - m.x65 - m.x70 - m.x75 - m.x80 == 0)

m.c7 = Constraint(expr= - m.x6 + m.x11 - m.x61 - m.x66 - m.x71 - m.x76 - m.x81 == 0)

m.c8 = Constraint(expr=m.x12*m.x7 - (m.x37*m.x57 + m.x41*m.x62 + m.x45*m.x67 + m.x49*m.x72 + m.x53*m.x77) - 2.5*m.x2
                        == 0)

m.c9 = Constraint(expr=m.x13*m.x7 - (m.x38*m.x57 + m.x42*m.x62 + m.x46*m.x67 + m.x50*m.x72 + m.x54*m.x77) - 3.46*m.x2
                        == 0)

m.c10 = Constraint(expr=m.x14*m.x7 - (m.x39*m.x57 + m.x43*m.x62 + m.x47*m.x67 + m.x51*m.x72 + m.x55*m.x77) == 0)

m.c11 = Constraint(expr=m.x15*m.x7 - (m.x40*m.x57 + m.x44*m.x62 + m.x48*m.x67 + m.x52*m.x72 + m.x56*m.x77) - 26.05*m.x2
                         == 0)

m.c12 = Constraint(expr=m.x16*m.x8 - (m.x37*m.x58 + m.x41*m.x63 + m.x45*m.x68 + m.x49*m.x73 + m.x53*m.x78) - 2.5*m.x3
                         == 0)

m.c13 = Constraint(expr=m.x17*m.x8 - (m.x38*m.x58 + m.x42*m.x63 + m.x46*m.x68 + m.x50*m.x73 + m.x54*m.x78) - 3.46*m.x3
                         == 0)

m.c14 = Constraint(expr=m.x18*m.x8 - (m.x39*m.x58 + m.x43*m.x63 + m.x47*m.x68 + m.x51*m.x73 + m.x55*m.x78) == 0)

m.c15 = Constraint(expr=m.x19*m.x8 - (m.x40*m.x58 + m.x44*m.x63 + m.x48*m.x68 + m.x52*m.x73 + m.x56*m.x78) - 26.05*m.x3
                         == 0)

m.c16 = Constraint(expr=m.x20*m.x9 - (m.x37*m.x59 + m.x41*m.x64 + m.x45*m.x69 + m.x49*m.x74 + m.x53*m.x79) - 2.5*m.x4
                         == 0)

m.c17 = Constraint(expr=m.x21*m.x9 - (m.x38*m.x59 + m.x42*m.x64 + m.x46*m.x69 + m.x50*m.x74 + m.x54*m.x79) - 3.46*m.x4
                         == 0)

m.c18 = Constraint(expr=m.x22*m.x9 - (m.x39*m.x59 + m.x43*m.x64 + m.x47*m.x69 + m.x51*m.x74 + m.x55*m.x79) == 0)

m.c19 = Constraint(expr=m.x23*m.x9 - (m.x40*m.x59 + m.x44*m.x64 + m.x48*m.x69 + m.x52*m.x74 + m.x56*m.x79) - 26.05*m.x4
                         == 0)

m.c20 = Constraint(expr=m.x24*m.x10 - (m.x37*m.x60 + m.x41*m.x65 + m.x45*m.x70 + m.x49*m.x75 + m.x53*m.x80) - 2.5*m.x5
                         == 0)

m.c21 = Constraint(expr=m.x25*m.x10 - (m.x38*m.x60 + m.x42*m.x65 + m.x46*m.x70 + m.x50*m.x75 + m.x54*m.x80) - 3.46*m.x5
                         == 0)

m.c22 = Constraint(expr=m.x26*m.x10 - (m.x39*m.x60 + m.x43*m.x65 + m.x47*m.x70 + m.x51*m.x75 + m.x55*m.x80) == 0)

m.c23 = Constraint(expr=m.x27*m.x10 - (m.x40*m.x60 + m.x44*m.x65 + m.x48*m.x70 + m.x52*m.x75 + m.x56*m.x80) - 26.05*m.x5
                         == 0)

m.c24 = Constraint(expr=m.x28*m.x11 - (m.x37*m.x61 + m.x41*m.x66 + m.x45*m.x71 + m.x49*m.x76 + m.x53*m.x81) - 2.5*m.x6
                         == 0)

m.c25 = Constraint(expr=m.x29*m.x11 - (m.x38*m.x61 + m.x42*m.x66 + m.x46*m.x71 + m.x50*m.x76 + m.x54*m.x81) - 3.46*m.x6
                         == 0)

m.c26 = Constraint(expr=m.x30*m.x11 - (m.x39*m.x61 + m.x43*m.x66 + m.x47*m.x71 + m.x51*m.x76 + m.x55*m.x81) == 0)

m.c27 = Constraint(expr=m.x31*m.x11 - (m.x40*m.x61 + m.x44*m.x66 + m.x48*m.x71 + m.x52*m.x76 + m.x56*m.x81) - 26.05*m.x6
                         == 0)

m.c28 = Constraint(expr= - m.x7 + m.x32 == 0)

m.c29 = Constraint(expr= - m.x8 + m.x33 == 0)

m.c30 = Constraint(expr= - m.x9 + m.x34 == 0)

m.c31 = Constraint(expr= - m.x10 + m.x35 == 0)

m.c32 = Constraint(expr= - m.x11 + m.x36 == 0)

m.c33 = Constraint(expr=m.x37*m.x32 - (m.x12*m.x7 + m.x92*(m.x103 - m.x102)) == 0)

m.c34 = Constraint(expr=m.x38*m.x32 - (m.x13*m.x7 + m.x92*(0.5*m.x103 - 0.5*m.x102)) == 0)

m.c35 = Constraint(expr=m.x39*m.x32 - (m.x14*m.x7 + m.x92*(m.x102 - m.x103)) == 0)

m.c36 = Constraint(expr=m.x40*m.x32 - m.x15*m.x7 == 0)

m.c37 = Constraint(expr=m.x41*m.x33 - (m.x16*m.x8 + m.x93*(m.x105 - m.x104)) == 0)

m.c38 = Constraint(expr=m.x42*m.x33 - (m.x17*m.x8 + m.x93*(0.5*m.x105 - 0.5*m.x104)) == 0)

m.c39 = Constraint(expr=m.x43*m.x33 - (m.x18*m.x8 + m.x93*(m.x104 - m.x105)) == 0)

m.c40 = Constraint(expr=m.x44*m.x33 - m.x19*m.x8 == 0)

m.c41 = Constraint(expr=m.x45*m.x34 - (m.x20*m.x9 + m.x94*(m.x107 - m.x106)) == 0)

m.c42 = Constraint(expr=m.x46*m.x34 - (m.x21*m.x9 + m.x94*(0.5*m.x107 - 0.5*m.x106)) == 0)

m.c43 = Constraint(expr=m.x47*m.x34 - (m.x22*m.x9 + m.x94*(m.x106 - m.x107)) == 0)

m.c44 = Constraint(expr=m.x48*m.x34 - m.x23*m.x9 == 0)

m.c45 = Constraint(expr=m.x49*m.x35 - (m.x24*m.x10 + m.x95*(m.x109 - m.x108)) == 0)

m.c46 = Constraint(expr=m.x50*m.x35 - (m.x25*m.x10 + m.x95*(0.5*m.x109 - 0.5*m.x108)) == 0)

m.c47 = Constraint(expr=m.x51*m.x35 - (m.x26*m.x10 + m.x95*(m.x108 - m.x109)) == 0)

m.c48 = Constraint(expr=m.x52*m.x35 - m.x27*m.x10 == 0)

m.c49 = Constraint(expr=m.x53*m.x36 - (m.x28*m.x11 + m.x96*(m.x111 - m.x110)) == 0)

m.c50 = Constraint(expr=m.x54*m.x36 - (m.x29*m.x11 + m.x96*(0.5*m.x111 - 0.5*m.x110)) == 0)

m.c51 = Constraint(expr=m.x55*m.x36 - (m.x30*m.x11 + m.x96*(m.x110 - m.x111)) == 0)

m.c52 = Constraint(expr=m.x56*m.x36 - m.x31*m.x11 == 0)

m.c53 = Constraint(expr=-628400000000*exp(-15500/m.x97)*m.x37**0.5*m.x38/(m.x37 + m.x38 + m.x39 + m.x40)**1.5 + m.x102
                         == 0)

m.c54 = Constraint(expr=-628400000000*exp(-15500/m.x98)*m.x41**0.5*m.x42/(m.x41 + m.x42 + m.x43 + m.x44)**1.5 + m.x104
                         == 0)

m.c55 = Constraint(expr=-628400000000*exp(-15500/m.x99)*m.x45**0.5*m.x46/(m.x45 + m.x46 + m.x47 + m.x48)**1.5 + m.x106
                         == 0)

m.c56 = Constraint(expr=-628400000000*exp(-15500/m.x100)*m.x49**0.5*m.x50/(m.x49 + m.x50 + m.x51 + m.x52)**1.5 + m.x108
                         == 0)

m.c57 = Constraint(expr=-628400000000*exp(-15500/m.x101)*m.x53**0.5*m.x54/(m.x53 + m.x54 + m.x55 + m.x56)**1.5 + m.x110
                         == 0)

m.c58 = Constraint(expr=-2.732e16*exp(-26799.5/m.x97)*m.x38**0.5*m.x39/m.x37**0.5/(m.x37 + m.x38 + m.x39 + m.x40)
                         + m.x103 == 0)

m.c59 = Constraint(expr=-2.732e16*exp(-26799.5/m.x98)*m.x42**0.5*m.x43/m.x41**0.5/(m.x41 + m.x42 + m.x43 + m.x44)
                         + m.x105 == 0)

m.c60 = Constraint(expr=-2.732e16*exp(-26799.5/m.x99)*m.x46**0.5*m.x47/m.x45**0.5/(m.x45 + m.x46 + m.x47 + m.x48)
                         + m.x107 == 0)

m.c61 = Constraint(expr=-2.732e16*exp(-26799.5/m.x100)*m.x50**0.5*m.x51/m.x49**0.5/(m.x49 + m.x50 + m.x51 + m.x52)
                         + m.x109 == 0)

m.c62 = Constraint(expr=-2.732e16*exp(-26799.5/m.x101)*m.x54**0.5*m.x55/m.x53**0.5/(m.x53 + m.x54 + m.x55 + m.x56)
                         + m.x111 == 0)

m.c63 = Constraint(expr=   m.x32 - m.x57 - m.x58 - m.x59 - m.x60 - m.x61 - m.x82 == 0)

m.c64 = Constraint(expr=   m.x33 - m.x62 - m.x63 - m.x64 - m.x65 - m.x66 - m.x83 == 0)

m.c65 = Constraint(expr=   m.x34 - m.x67 - m.x68 - m.x69 - m.x70 - m.x71 - m.x84 == 0)

m.c66 = Constraint(expr=   m.x35 - m.x72 - m.x73 - m.x74 - m.x75 - m.x76 - m.x85 == 0)

m.c67 = Constraint(expr=   m.x36 - m.x77 - m.x78 - m.x79 - m.x80 - m.x81 - m.x86 == 0)

m.c68 = Constraint(expr= - m.x82 - m.x83 - m.x84 - m.x85 - m.x86 + m.x87 == 0)

m.c69 = Constraint(expr=m.x87*m.x88 - (m.x82*m.x37 + m.x83*m.x41 + m.x84*m.x45 + m.x85*m.x49 + m.x86*m.x53) == 0)

m.c70 = Constraint(expr=m.x87*m.x89 - (m.x82*m.x38 + m.x83*m.x42 + m.x84*m.x46 + m.x85*m.x50 + m.x86*m.x54) == 0)

m.c71 = Constraint(expr=m.x87*m.x90 - (m.x82*m.x39 + m.x83*m.x43 + m.x84*m.x47 + m.x85*m.x51 + m.x86*m.x55) == 0)

m.c72 = Constraint(expr=m.x87*m.x91 - (m.x82*m.x40 + m.x83*m.x44 + m.x84*m.x48 + m.x85*m.x52 + m.x86*m.x56) == 0)
