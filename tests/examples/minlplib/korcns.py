#  CNS written by GAMS Convert at 04/21/18 13:52:28
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         78       78        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         96       96        0        0        0        0        0        0
#  FX     18       18        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        346      146      200        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x2 = Var(within=Reals,bounds=(0.01,None),initialize=1)
m.x3 = Var(within=Reals,bounds=(0.01,None),initialize=1)
m.x4 = Var(within=Reals,bounds=(0.01,None),initialize=1)
m.x5 = Var(within=Reals,bounds=(0.01,None),initialize=1)
m.x6 = Var(within=Reals,bounds=(0.01,None),initialize=1)
m.x7 = Var(within=Reals,bounds=(0.01,None),initialize=1)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x11 = Var(within=Reals,bounds=(0.01,None),initialize=1)
m.x12 = Var(within=Reals,bounds=(0.01,None),initialize=1)
m.x13 = Var(within=Reals,bounds=(0.01,None),initialize=1)
m.x14 = Var(within=Reals,bounds=(0.01,None),initialize=1)
m.x15 = Var(within=Reals,bounds=(0.01,None),initialize=1)
m.x16 = Var(within=Reals,bounds=(0.01,None),initialize=1)
m.x17 = Var(within=Reals,bounds=(0.01,None),initialize=1)
m.x18 = Var(within=Reals,bounds=(0.01,None),initialize=1)
m.x19 = Var(within=Reals,bounds=(0.01,None),initialize=1)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=0.737)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=0.2911)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=0.6625)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x25 = Var(within=Reals,bounds=(0.01,None),initialize=711.6443)
m.x26 = Var(within=Reals,bounds=(0.01,None),initialize=930.3509)
m.x27 = Var(within=Reals,bounds=(0.01,None),initialize=497.4428)
m.x28 = Var(within=Reals,bounds=(0.01,None),initialize=657.3677)
m.x29 = Var(within=Reals,bounds=(0.01,None),initialize=840.05)
m.x30 = Var(within=Reals,bounds=(0.01,None),initialize=515.4296)
m.x31 = Var(within=Reals,bounds=(0.01,None),initialize=641.7037)
m.x32 = Var(within=Reals,bounds=(0.01,None),initialize=812.2222)
m.x33 = Var(within=Reals,bounds=(0.01,None),initialize=492.0307)
m.x34 = Var(within=Reals,bounds=(0.01,None),initialize=15.6639)
m.x35 = Var(within=Reals,bounds=(0.01,None),initialize=27.8278)
m.x36 = Var(within=Reals,bounds=(0.01,None),initialize=23.3988)
m.x37 = Var(within=Reals,bounds=(0.01,None),initialize=69.9406)
m.x38 = Var(within=Reals,bounds=(0.01,None),initialize=118.1287)
m.x39 = Var(within=Reals,bounds=(0.01,None),initialize=5.412)
m.x40 = Var(within=Reals,bounds=(657.5754,657.5754),initialize=657.5754)
m.x41 = Var(within=Reals,bounds=(338.7076,338.7076),initialize=338.7076)
m.x42 = Var(within=Reals,bounds=(1548.5192,1548.5192),initialize=1548.5192)
m.x43 = Var(within=Reals,bounds=(0.01,None),initialize=0.074)
m.x44 = Var(within=Reals,bounds=(0.01,None),initialize=0.14)
m.x45 = Var(within=Reals,bounds=(0.01,None),initialize=0.152)
m.x46 = Var(within=Reals,bounds=(2515.9,2515.9),initialize=2515.9)
m.x47 = Var(within=Reals,bounds=(1565.987,1565.987),initialize=1565.987)
m.x48 = Var(within=Reals,bounds=(948.1,948.1),initialize=948.1)
m.x49 = Var(within=Reals,bounds=(0.01,None),initialize=2515.9)
m.x50 = Var(within=Reals,bounds=(0.01,None),initialize=442.643)
m.x51 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x53 = Var(within=Reals,bounds=(0.01,None),initialize=767.776)
m.x54 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x56 = Var(within=Reals,bounds=(0.01,None),initialize=355.568)
m.x57 = Var(within=Reals,bounds=(0.01,None),initialize=948.1)
m.x58 = Var(within=Reals,bounds=(0.01,None),initialize=256.645)
m.x59 = Var(within=Reals,bounds=(0.01,None),initialize=464.1656)
m.x60 = Var(within=Reals,bounds=(0.01,None),initialize=156.2598)
m.x61 = Var(within=Reals,bounds=(None,None),initialize=452.1765)
m.x62 = Var(within=Reals,bounds=(None,None),initialize=307.8561)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=202.0416)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=2.823)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=9.8806)
m.x66 = Var(within=Reals,bounds=(None,None),initialize=128.4482)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=148.4488)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=10.6931)
m.x70 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(0.01,None),initialize=1123.5941)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=194.0449)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=28.6572)
m.x76 = Var(within=Reals,bounds=(None,None),initialize=65.2754)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(141.1519,141.1519),initialize=141.1519)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=61.4089)
m.x80 = Var(within=Reals,bounds=(None,None),initialize=52.893)
m.x81 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(None,None),initialize=159.1419)
m.x83 = Var(within=Reals,bounds=(None,None),initialize=159.1419)
m.x84 = Var(within=Reals,bounds=(0.06,0.06),initialize=0.06)
m.x85 = Var(within=Reals,bounds=(0.06,0.06),initialize=0.06)
m.x86 = Var(within=Reals,bounds=(39.1744,39.1744),initialize=39.1744)
m.x87 = Var(within=Reals,bounds=(None,None),initialize=20.6884)
m.x88 = Var(within=Reals,bounds=(None,None),initialize=46.1511)
m.x89 = Var(within=Reals,bounds=(None,None),initialize=92.3023)
m.x90 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x92 = Var(within=Reals,bounds=(58.759,58.759),initialize=58.759)
m.x93 = Var(within=Reals,bounds=(None,None),initialize=548.7478)
m.x94 = Var(within=Reals,bounds=(None,None),initialize=574.8463)
m.x95 = Var(within=Reals,bounds=(None,None),initialize=100.1122)
m.x96 = Var(within=Reals,bounds=(None,None),initialize=0)

m.c1 = Constraint(expr=-0.90909*m.x1*(1.1 + m.x23) + m.x5 == 0)

m.c2 = Constraint(expr=-0.81466*m.x1*(1.22751 + m.x23) + m.x6 == 0)

m.c3 = Constraint(expr=-0.92521*m.x1*(1.08084 + m.x23) + m.x7 == 0)

m.c4 = Constraint(expr= - m.x1 + m.x8 == 0)

m.c5 = Constraint(expr= - m.x1 + m.x9 == 0)

m.c6 = Constraint(expr= - m.x1 + m.x10 == 0)

m.c7 = Constraint(expr=m.x17*m.x25 - (m.x2*m.x31 + m.x5*m.x37) == 0)

m.c8 = Constraint(expr=m.x18*m.x26 - (m.x3*m.x32 + m.x6*m.x38) == 0)

m.c9 = Constraint(expr=m.x19*m.x27 - (m.x4*m.x33 + m.x7*m.x39) == 0)

m.c10 = Constraint(expr=m.x14*m.x28 - (m.x2*m.x31 + m.x8*m.x34) == 0)

m.c11 = Constraint(expr=m.x15*m.x29 - (m.x3*m.x32 + m.x9*m.x35) == 0)

m.c12 = Constraint(expr=m.x16*m.x30 - (m.x4*m.x33 + m.x10*m.x36) == 0)

m.c13 = Constraint(expr=   0.99*m.x14 - 0.12591*m.x17 - 0.10353*m.x18 - 0.02358*m.x19 - m.x20 == 0)

m.c14 = Constraint(expr=   0.9608*m.x15 - 0.19834*m.x17 - 0.35524*m.x18 - 0.11608*m.x19 - m.x21 == 0)

m.c15 = Constraint(expr=   0.95*m.x16 - 0.01407*m.x17 - 0.18954*m.x18 - 0.0839*m.x19 - m.x22 == 0)

m.c16 = Constraint(expr=   m.x11 - 0.93076*m.x18 - 0.06924*m.x19 == 0)

m.c17 = Constraint(expr=   m.x12 - 0.93774*m.x18 - 0.06226*m.x19 == 0)

m.c18 = Constraint(expr=   m.x13 - 0.9308*m.x18 - 0.0692*m.x19 == 0)

m.c19 = Constraint(expr= - 0.33263*m.x17 - 0.43486*m.x18 - 0.23251*m.x19 + m.x24 == 0)

m.c20 = Constraint(expr=-0.61447*m.x49**0.38258*m.x50**0.0674*m.x40**0.55002 + m.x28 == 0)

m.c21 = Constraint(expr=-1.60111*m.x53**0.53476*m.x41**0.46524 + m.x29 == 0)

m.c22 = Constraint(expr=-0.52019*m.x56**0.16234*m.x57**0.42326*m.x42**0.4144 + m.x30 == 0)

m.c23 = Constraint(expr=m.x43*m.x49 - 0.38258*m.x28*m.x20 == 0)

m.c24 = Constraint(expr=0.5278*m.x44*m.x50 - 0.0674*m.x28*m.x20 == 0)

m.c25 = Constraint(expr=1.21879*m.x44*m.x53 - 0.53476*m.x29*m.x21 == 0)

m.c26 = Constraint(expr=1.11541*m.x44*m.x56 - 0.16234*m.x30*m.x22 == 0)

m.c27 = Constraint(expr=m.x45*m.x57 - 0.42326*m.x30*m.x22 == 0)

m.c28 = Constraint(expr= - m.x46 + m.x49 + m.x52 + m.x55 == 0)

m.c29 = Constraint(expr= - m.x47 + m.x50 + m.x53 + m.x56 == 0)

m.c30 = Constraint(expr= - m.x48 + m.x51 + m.x54 + m.x57 == 0)

m.c31 = Constraint(expr=-3.85424*(0.86628*m.x34**1.5 + 0.13372*m.x31**1.5)**0.666666666666667 + m.x28 == 0)

m.c32 = Constraint(expr=-3.51886*(0.84602*m.x35**1.5 + 0.15398*m.x32**1.5)**0.666666666666667 + m.x29 == 0)

m.c33 = Constraint(expr=-3.23592*(0.82436*m.x36**1.5 + 0.17564*m.x33**1.5)**0.666666666666667 + m.x30 == 0)

m.c34 = Constraint(expr=m.x34/m.x31 - (0.154361176524911*m.x8/m.x2)**2 == 0)

m.c35 = Constraint(expr=m.x35/m.x32 - (0.182005153542469*m.x9/m.x3)**2 == 0)

m.c36 = Constraint(expr=m.x36/m.x33 - (0.213062254354893*m.x10/m.x4)**2 == 0)

m.c37 = Constraint(expr=-1.59539*(0.2482*m.x37**0.5 + 0.7518*m.x31**0.5)**2 + m.x25 == 0)

m.c38 = Constraint(expr=-1.34652*(0.05111*m.x38**(-0.515151515151515) + 0.94889*m.x32**(-0.515151515151515))**(-
                        1.94117647058824) + m.x26 == 0)

m.c39 = Constraint(expr=-1.01839*(1e-5*m.x39**(-1.5) + 0.99999*m.x33**(-1.5))**(-0.666666666666667) + m.x27 == 0)

m.c40 = Constraint(expr=m.x37/m.x31 - (0.330140994945464*m.x2/m.x5)**2 == 0)

m.c41 = Constraint(expr=m.x38/m.x32 - (0.0538629345867277*m.x3/m.x6)**0.66 == 0)

m.c42 = Constraint(expr=m.x39/m.x33 - (1.0000100001e-5*m.x4/m.x7)**0.4 == 0)

m.c43 = Constraint(expr= - 0.12591*m.x28 - 0.19834*m.x29 - 0.01407*m.x30 + m.x58 == 0)

m.c44 = Constraint(expr= - 0.10353*m.x28 - 0.35524*m.x29 - 0.18954*m.x30 + m.x59 == 0)

m.c45 = Constraint(expr= - 0.02358*m.x28 - 0.11608*m.x29 - 0.0839*m.x30 + m.x60 == 0)

m.c46 = Constraint(expr=m.x17*m.x61 - ((0.428123 - 0.428123*m.x84)*m.x93 + (0.428123 - 0.428123*m.x85)*m.x94) == 0)

m.c47 = Constraint(expr=m.x18*m.x62 - ((0.291478891 - 0.291478891*m.x84)*m.x93 + (0.291478891 - 0.291478891*m.x85)*m.x94
                        ) == 0)

m.c48 = Constraint(expr=m.x19*m.x63 - ((0.191298109 - 0.191298109*m.x84)*m.x93 + (0.191298109 - 0.191298109*m.x85)*m.x94
                        ) == 0)

m.c49 = Constraint(expr=   m.x70 == 0)

m.c50 = Constraint(expr=   m.x71 == 0)

m.c51 = Constraint(expr=   m.x72 == 0)

m.c52 = Constraint(expr=   m.x73 - m.x93 - m.x94 == 0)

m.c53 = Constraint(expr=-(m.x43*m.x46 + m.x44*m.x47 + m.x45*m.x48 + m.x91*m.x1) + m.x93 == 0)

m.c54 = Constraint(expr=-(m.x20*m.x28 + m.x21*m.x29 + m.x22*m.x30 - (m.x43*m.x46 + m.x44*m.x47 + m.x45*m.x48) + m.x92*
                        m.x1) + m.x81 - m.x90 + m.x94 == 0)

m.c55 = Constraint(expr= - 0.0891*m.x93 - 0.0891*m.x94 + m.x95 == 0)

m.c56 = Constraint(expr=   m.x64 - 0.02*m.x78 == 0)

m.c57 = Constraint(expr=   m.x65 - 0.07*m.x78 == 0)

m.c58 = Constraint(expr=   m.x66 - 0.91*m.x78 == 0)

m.c59 = Constraint(expr=   m.x74 - m.x75 - m.x76 + m.x77 - m.x95 == 0)

m.c60 = Constraint(expr=-(0.090909*m.x37 + 0.1853432966*m.x38 + 0.0747939764*m.x39)*m.x1 + m.x75 == 0)

m.c61 = Constraint(expr=-(0.90909*m.x37 + 0.81466*m.x38 + 0.92521*m.x39)*m.x1*m.x23 + m.x90 == 0)

m.c62 = Constraint(expr=-(0.01*m.x14*m.x28 + 0.0392*m.x15*m.x29 + 0.05*m.x16*m.x30) + m.x76 == 0)

m.c63 = Constraint(expr=   m.x77 == 0)

m.c64 = Constraint(expr=-(0.9109*m.x84*m.x93 + 0.9109*m.x85*m.x94) + m.x79 == 0)

m.c65 = Constraint(expr=-(m.x17*m.x64 + m.x18*m.x65 + m.x19*m.x66) + m.x74 - m.x80 == 0)

m.c66 = Constraint(expr=   m.x81 == 0)

m.c67 = Constraint(expr=-m.x86*m.x1 - m.x79 - m.x80 - m.x81 + m.x83 == 0)

m.c68 = Constraint(expr=m.x11*m.x87 + 0.13*(m.x70*m.x17 + m.x71*m.x18 + m.x72*m.x19) - 0.13*m.x82 == 0)

m.c69 = Constraint(expr=m.x12*m.x88 + 0.29*(m.x70*m.x17 + m.x71*m.x18 + m.x72*m.x19) - 0.29*m.x82 == 0)

m.c70 = Constraint(expr=m.x13*m.x89 + 0.58*(m.x70*m.x17 + m.x71*m.x18 + m.x72*m.x19) - 0.58*m.x82 == 0)

m.c71 = Constraint(expr=   m.x67 == 0)

m.c72 = Constraint(expr=   m.x68 - 0.93076*m.x87 - 0.93774*m.x88 - 0.9308*m.x89 == 0)

m.c73 = Constraint(expr=   m.x69 - 0.06924*m.x87 - 0.06226*m.x88 - 0.0692*m.x89 == 0)

m.c74 = Constraint(expr= - m.x34 - m.x35 - m.x36 + 0.90909*m.x37 + 0.81466*m.x38 + 0.92521*m.x39 - m.x86 - m.x91 - m.x92
                         == 0)

m.c75 = Constraint(expr=   m.x25 - m.x58 - m.x61 - m.x64 - m.x67 - m.x70 == 0)

m.c76 = Constraint(expr=   m.x26 - m.x59 - m.x62 - m.x65 - m.x68 - m.x71 == 0)

m.c77 = Constraint(expr=   m.x27 - m.x60 - m.x63 - m.x66 - m.x69 - m.x72 == 0)

m.c78 = Constraint(expr=-m.x61**0.47*m.x62**0.31999*m.x63**0.21001 + m.x96 == 0)
