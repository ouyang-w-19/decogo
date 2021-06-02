#  NLP written by GAMS Convert at 04/21/18 13:51:14
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         52       52        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        103      103        0        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        354      201      153        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=0.9616)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0.9264)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0.8944)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=0.8656)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0.84)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=0.8176)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=0.7984)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=0.7824)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=0.7696)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=0.76)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=0.7536)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0.7504)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=0.7504)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=0.7536)
m.x16 = Var(within=Reals,bounds=(None,None),initialize=0.76)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=0.7696)
m.x18 = Var(within=Reals,bounds=(None,None),initialize=0.7824)
m.x19 = Var(within=Reals,bounds=(None,None),initialize=0.7984)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=0.8176)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=0.84)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=0.8656)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=0.8944)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=0.9264)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=0.9616)
m.x26 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x27 = Var(within=Reals,bounds=(None,None),initialize=1.0416)
m.x28 = Var(within=Reals,bounds=(None,None),initialize=1.0864)
m.x29 = Var(within=Reals,bounds=(None,None),initialize=1.1344)
m.x30 = Var(within=Reals,bounds=(None,None),initialize=1.1856)
m.x31 = Var(within=Reals,bounds=(None,None),initialize=1.24)
m.x32 = Var(within=Reals,bounds=(None,None),initialize=1.2976)
m.x33 = Var(within=Reals,bounds=(None,None),initialize=1.3584)
m.x34 = Var(within=Reals,bounds=(None,None),initialize=1.4224)
m.x35 = Var(within=Reals,bounds=(None,None),initialize=1.4896)
m.x36 = Var(within=Reals,bounds=(None,None),initialize=1.56)
m.x37 = Var(within=Reals,bounds=(None,None),initialize=1.6336)
m.x38 = Var(within=Reals,bounds=(None,None),initialize=1.7104)
m.x39 = Var(within=Reals,bounds=(None,None),initialize=1.7904)
m.x40 = Var(within=Reals,bounds=(None,None),initialize=1.8736)
m.x41 = Var(within=Reals,bounds=(None,None),initialize=1.96)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=2.0496)
m.x43 = Var(within=Reals,bounds=(None,None),initialize=2.1424)
m.x44 = Var(within=Reals,bounds=(None,None),initialize=2.2384)
m.x45 = Var(within=Reals,bounds=(None,None),initialize=2.3376)
m.x46 = Var(within=Reals,bounds=(None,None),initialize=2.44)
m.x47 = Var(within=Reals,bounds=(None,None),initialize=2.5456)
m.x48 = Var(within=Reals,bounds=(None,None),initialize=2.6544)
m.x49 = Var(within=Reals,bounds=(None,None),initialize=2.7664)
m.x50 = Var(within=Reals,bounds=(None,None),initialize=2.8816)
m.x51 = Var(within=Reals,bounds=(3,3),initialize=3)
m.x52 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x53 = Var(within=Reals,bounds=(None,None),initialize=-1.84)
m.x54 = Var(within=Reals,bounds=(None,None),initialize=-1.68)
m.x55 = Var(within=Reals,bounds=(None,None),initialize=-1.52)
m.x56 = Var(within=Reals,bounds=(None,None),initialize=-1.36)
m.x57 = Var(within=Reals,bounds=(None,None),initialize=-1.2)
m.x58 = Var(within=Reals,bounds=(None,None),initialize=-1.04)
m.x59 = Var(within=Reals,bounds=(None,None),initialize=-0.88)
m.x60 = Var(within=Reals,bounds=(None,None),initialize=-0.72)
m.x61 = Var(within=Reals,bounds=(None,None),initialize=-0.56)
m.x62 = Var(within=Reals,bounds=(None,None),initialize=-0.4)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=-0.24)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=-0.0800000000000001)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=0.0800000000000001)
m.x66 = Var(within=Reals,bounds=(None,None),initialize=0.24)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0.4)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=0.56)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=0.72)
m.x70 = Var(within=Reals,bounds=(None,None),initialize=0.88)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=1.04)
m.x72 = Var(within=Reals,bounds=(None,None),initialize=1.2)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=1.36)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=1.52)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=1.68)
m.x76 = Var(within=Reals,bounds=(None,None),initialize=1.84)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=2)
m.x78 = Var(within=Reals,bounds=(None,None),initialize=2.16)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=2.32)
m.x80 = Var(within=Reals,bounds=(None,None),initialize=2.48)
m.x81 = Var(within=Reals,bounds=(None,None),initialize=2.64)
m.x82 = Var(within=Reals,bounds=(None,None),initialize=2.8)
m.x83 = Var(within=Reals,bounds=(None,None),initialize=2.96)
m.x84 = Var(within=Reals,bounds=(None,None),initialize=3.12)
m.x85 = Var(within=Reals,bounds=(None,None),initialize=3.28)
m.x86 = Var(within=Reals,bounds=(None,None),initialize=3.44)
m.x87 = Var(within=Reals,bounds=(None,None),initialize=3.6)
m.x88 = Var(within=Reals,bounds=(None,None),initialize=3.76)
m.x89 = Var(within=Reals,bounds=(None,None),initialize=3.92)
m.x90 = Var(within=Reals,bounds=(None,None),initialize=4.08)
m.x91 = Var(within=Reals,bounds=(None,None),initialize=4.24)
m.x92 = Var(within=Reals,bounds=(None,None),initialize=4.4)
m.x93 = Var(within=Reals,bounds=(None,None),initialize=4.56)
m.x94 = Var(within=Reals,bounds=(None,None),initialize=4.72)
m.x95 = Var(within=Reals,bounds=(None,None),initialize=4.88)
m.x96 = Var(within=Reals,bounds=(None,None),initialize=5.04)
m.x97 = Var(within=Reals,bounds=(None,None),initialize=5.2)
m.x98 = Var(within=Reals,bounds=(None,None),initialize=5.36)
m.x99 = Var(within=Reals,bounds=(None,None),initialize=5.52)
m.x100 = Var(within=Reals,bounds=(None,None),initialize=5.68)
m.x101 = Var(within=Reals,bounds=(None,None),initialize=5.84)
m.x102 = Var(within=Reals,bounds=(None,None),initialize=6)

m.obj = Objective(expr=0.01*(sqrt(1 + m.x52**2)*m.x1 + sqrt(1 + m.x53**2)*m.x2 + sqrt(1 + m.x53**2)*m.x2 + sqrt(1 + 
                       m.x54**2)*m.x3 + sqrt(1 + m.x54**2)*m.x3 + sqrt(1 + m.x55**2)*m.x4 + sqrt(1 + m.x55**2)*m.x4 + 
                       sqrt(1 + m.x56**2)*m.x5 + sqrt(1 + m.x56**2)*m.x5 + sqrt(1 + m.x57**2)*m.x6 + sqrt(1 + m.x57**2)*
                       m.x6 + sqrt(1 + m.x58**2)*m.x7 + sqrt(1 + m.x58**2)*m.x7 + sqrt(1 + m.x59**2)*m.x8 + sqrt(1 + 
                       m.x59**2)*m.x8 + sqrt(1 + m.x60**2)*m.x9 + sqrt(1 + m.x60**2)*m.x9 + sqrt(1 + m.x61**2)*m.x10 + 
                       sqrt(1 + m.x61**2)*m.x10 + sqrt(1 + m.x62**2)*m.x11 + sqrt(1 + m.x62**2)*m.x11 + sqrt(1 + m.x63**
                       2)*m.x12 + sqrt(1 + m.x63**2)*m.x12 + sqrt(1 + m.x64**2)*m.x13 + sqrt(1 + m.x64**2)*m.x13 + sqrt(
                       1 + m.x65**2)*m.x14 + sqrt(1 + m.x65**2)*m.x14 + sqrt(1 + m.x66**2)*m.x15 + sqrt(1 + m.x66**2)*
                       m.x15 + sqrt(1 + m.x67**2)*m.x16 + sqrt(1 + m.x67**2)*m.x16 + sqrt(1 + m.x68**2)*m.x17 + sqrt(1
                        + m.x68**2)*m.x17 + sqrt(1 + m.x69**2)*m.x18 + sqrt(1 + m.x69**2)*m.x18 + sqrt(1 + m.x70**2)*
                       m.x19 + sqrt(1 + m.x70**2)*m.x19 + sqrt(1 + m.x71**2)*m.x20 + sqrt(1 + m.x71**2)*m.x20 + sqrt(1
                        + m.x72**2)*m.x21 + sqrt(1 + m.x72**2)*m.x21 + sqrt(1 + m.x73**2)*m.x22 + sqrt(1 + m.x73**2)*
                       m.x22 + sqrt(1 + m.x74**2)*m.x23 + sqrt(1 + m.x74**2)*m.x23 + sqrt(1 + m.x75**2)*m.x24 + sqrt(1
                        + m.x75**2)*m.x24 + sqrt(1 + m.x76**2)*m.x25 + sqrt(1 + m.x76**2)*m.x25 + sqrt(1 + m.x77**2)*
                       m.x26 + sqrt(1 + m.x77**2)*m.x26 + sqrt(1 + m.x78**2)*m.x27 + sqrt(1 + m.x78**2)*m.x27 + sqrt(1
                        + m.x79**2)*m.x28 + sqrt(1 + m.x79**2)*m.x28 + sqrt(1 + m.x80**2)*m.x29 + sqrt(1 + m.x80**2)*
                       m.x29 + sqrt(1 + m.x81**2)*m.x30 + sqrt(1 + m.x81**2)*m.x30 + sqrt(1 + m.x82**2)*m.x31 + sqrt(1
                        + m.x82**2)*m.x31 + sqrt(1 + m.x83**2)*m.x32 + sqrt(1 + m.x83**2)*m.x32 + sqrt(1 + m.x84**2)*
                       m.x33 + sqrt(1 + m.x84**2)*m.x33 + sqrt(1 + m.x85**2)*m.x34 + sqrt(1 + m.x85**2)*m.x34 + sqrt(1
                        + m.x86**2)*m.x35 + sqrt(1 + m.x86**2)*m.x35 + sqrt(1 + m.x87**2)*m.x36 + sqrt(1 + m.x87**2)*
                       m.x36 + sqrt(1 + m.x88**2)*m.x37 + sqrt(1 + m.x88**2)*m.x37 + sqrt(1 + m.x89**2)*m.x38 + sqrt(1
                        + m.x89**2)*m.x38 + sqrt(1 + m.x90**2)*m.x39 + sqrt(1 + m.x90**2)*m.x39 + sqrt(1 + m.x91**2)*
                       m.x40 + sqrt(1 + m.x91**2)*m.x40 + sqrt(1 + m.x92**2)*m.x41 + sqrt(1 + m.x92**2)*m.x41 + sqrt(1
                        + m.x93**2)*m.x42 + sqrt(1 + m.x93**2)*m.x42 + sqrt(1 + m.x94**2)*m.x43 + sqrt(1 + m.x94**2)*
                       m.x43 + sqrt(1 + m.x95**2)*m.x44 + sqrt(1 + m.x95**2)*m.x44 + sqrt(1 + m.x96**2)*m.x45 + sqrt(1
                        + m.x96**2)*m.x45 + sqrt(1 + m.x97**2)*m.x46 + sqrt(1 + m.x97**2)*m.x46 + sqrt(1 + m.x98**2)*
                       m.x47 + sqrt(1 + m.x98**2)*m.x47 + sqrt(1 + m.x99**2)*m.x48 + sqrt(1 + m.x99**2)*m.x48 + sqrt(1
                        + m.x100**2)*m.x49 + sqrt(1 + m.x100**2)*m.x49 + sqrt(1 + m.x101**2)*m.x50 + sqrt(1 + m.x101**2)
                       *m.x50 + sqrt(1 + m.x102**2)*m.x51), sense=minimize)

m.c2 = Constraint(expr= - m.x1 + m.x2 - 0.01*m.x52 - 0.01*m.x53 == 0)

m.c3 = Constraint(expr= - m.x2 + m.x3 - 0.01*m.x53 - 0.01*m.x54 == 0)

m.c4 = Constraint(expr= - m.x3 + m.x4 - 0.01*m.x54 - 0.01*m.x55 == 0)

m.c5 = Constraint(expr= - m.x4 + m.x5 - 0.01*m.x55 - 0.01*m.x56 == 0)

m.c6 = Constraint(expr= - m.x5 + m.x6 - 0.01*m.x56 - 0.01*m.x57 == 0)

m.c7 = Constraint(expr= - m.x6 + m.x7 - 0.01*m.x57 - 0.01*m.x58 == 0)

m.c8 = Constraint(expr= - m.x7 + m.x8 - 0.01*m.x58 - 0.01*m.x59 == 0)

m.c9 = Constraint(expr= - m.x8 + m.x9 - 0.01*m.x59 - 0.01*m.x60 == 0)

m.c10 = Constraint(expr= - m.x9 + m.x10 - 0.01*m.x60 - 0.01*m.x61 == 0)

m.c11 = Constraint(expr= - m.x10 + m.x11 - 0.01*m.x61 - 0.01*m.x62 == 0)

m.c12 = Constraint(expr= - m.x11 + m.x12 - 0.01*m.x62 - 0.01*m.x63 == 0)

m.c13 = Constraint(expr= - m.x12 + m.x13 - 0.01*m.x63 - 0.01*m.x64 == 0)

m.c14 = Constraint(expr= - m.x13 + m.x14 - 0.01*m.x64 - 0.01*m.x65 == 0)

m.c15 = Constraint(expr= - m.x14 + m.x15 - 0.01*m.x65 - 0.01*m.x66 == 0)

m.c16 = Constraint(expr= - m.x15 + m.x16 - 0.01*m.x66 - 0.01*m.x67 == 0)

m.c17 = Constraint(expr= - m.x16 + m.x17 - 0.01*m.x67 - 0.01*m.x68 == 0)

m.c18 = Constraint(expr= - m.x17 + m.x18 - 0.01*m.x68 - 0.01*m.x69 == 0)

m.c19 = Constraint(expr= - m.x18 + m.x19 - 0.01*m.x69 - 0.01*m.x70 == 0)

m.c20 = Constraint(expr= - m.x19 + m.x20 - 0.01*m.x70 - 0.01*m.x71 == 0)

m.c21 = Constraint(expr= - m.x20 + m.x21 - 0.01*m.x71 - 0.01*m.x72 == 0)

m.c22 = Constraint(expr= - m.x21 + m.x22 - 0.01*m.x72 - 0.01*m.x73 == 0)

m.c23 = Constraint(expr= - m.x22 + m.x23 - 0.01*m.x73 - 0.01*m.x74 == 0)

m.c24 = Constraint(expr= - m.x23 + m.x24 - 0.01*m.x74 - 0.01*m.x75 == 0)

m.c25 = Constraint(expr= - m.x24 + m.x25 - 0.01*m.x75 - 0.01*m.x76 == 0)

m.c26 = Constraint(expr= - m.x25 + m.x26 - 0.01*m.x76 - 0.01*m.x77 == 0)

m.c27 = Constraint(expr= - m.x26 + m.x27 - 0.01*m.x77 - 0.01*m.x78 == 0)

m.c28 = Constraint(expr= - m.x27 + m.x28 - 0.01*m.x78 - 0.01*m.x79 == 0)

m.c29 = Constraint(expr= - m.x28 + m.x29 - 0.01*m.x79 - 0.01*m.x80 == 0)

m.c30 = Constraint(expr= - m.x29 + m.x30 - 0.01*m.x80 - 0.01*m.x81 == 0)

m.c31 = Constraint(expr= - m.x30 + m.x31 - 0.01*m.x81 - 0.01*m.x82 == 0)

m.c32 = Constraint(expr= - m.x31 + m.x32 - 0.01*m.x82 - 0.01*m.x83 == 0)

m.c33 = Constraint(expr= - m.x32 + m.x33 - 0.01*m.x83 - 0.01*m.x84 == 0)

m.c34 = Constraint(expr= - m.x33 + m.x34 - 0.01*m.x84 - 0.01*m.x85 == 0)

m.c35 = Constraint(expr= - m.x34 + m.x35 - 0.01*m.x85 - 0.01*m.x86 == 0)

m.c36 = Constraint(expr= - m.x35 + m.x36 - 0.01*m.x86 - 0.01*m.x87 == 0)

m.c37 = Constraint(expr= - m.x36 + m.x37 - 0.01*m.x87 - 0.01*m.x88 == 0)

m.c38 = Constraint(expr= - m.x37 + m.x38 - 0.01*m.x88 - 0.01*m.x89 == 0)

m.c39 = Constraint(expr= - m.x38 + m.x39 - 0.01*m.x89 - 0.01*m.x90 == 0)

m.c40 = Constraint(expr= - m.x39 + m.x40 - 0.01*m.x90 - 0.01*m.x91 == 0)

m.c41 = Constraint(expr= - m.x40 + m.x41 - 0.01*m.x91 - 0.01*m.x92 == 0)

m.c42 = Constraint(expr= - m.x41 + m.x42 - 0.01*m.x92 - 0.01*m.x93 == 0)

m.c43 = Constraint(expr= - m.x42 + m.x43 - 0.01*m.x93 - 0.01*m.x94 == 0)

m.c44 = Constraint(expr= - m.x43 + m.x44 - 0.01*m.x94 - 0.01*m.x95 == 0)

m.c45 = Constraint(expr= - m.x44 + m.x45 - 0.01*m.x95 - 0.01*m.x96 == 0)

m.c46 = Constraint(expr= - m.x45 + m.x46 - 0.01*m.x96 - 0.01*m.x97 == 0)

m.c47 = Constraint(expr= - m.x46 + m.x47 - 0.01*m.x97 - 0.01*m.x98 == 0)

m.c48 = Constraint(expr= - m.x47 + m.x48 - 0.01*m.x98 - 0.01*m.x99 == 0)

m.c49 = Constraint(expr= - m.x48 + m.x49 - 0.01*m.x99 - 0.01*m.x100 == 0)

m.c50 = Constraint(expr= - m.x49 + m.x50 - 0.01*m.x100 - 0.01*m.x101 == 0)

m.c51 = Constraint(expr= - m.x50 + m.x51 - 0.01*m.x101 - 0.01*m.x102 == 0)

m.c52 = Constraint(expr=0.01*(sqrt(1 + m.x52**2) + sqrt(1 + m.x53**2) + sqrt(1 + m.x53**2) + sqrt(1 + m.x54**2) + sqrt(1
                         + m.x54**2) + sqrt(1 + m.x55**2) + sqrt(1 + m.x55**2) + sqrt(1 + m.x56**2) + sqrt(1 + m.x56**2)
                         + sqrt(1 + m.x57**2) + sqrt(1 + m.x57**2) + sqrt(1 + m.x58**2) + sqrt(1 + m.x58**2) + sqrt(1 + 
                        m.x59**2) + sqrt(1 + m.x59**2) + sqrt(1 + m.x60**2) + sqrt(1 + m.x60**2) + sqrt(1 + m.x61**2) + 
                        sqrt(1 + m.x61**2) + sqrt(1 + m.x62**2) + sqrt(1 + m.x62**2) + sqrt(1 + m.x63**2) + sqrt(1 + 
                        m.x63**2) + sqrt(1 + m.x64**2) + sqrt(1 + m.x64**2) + sqrt(1 + m.x65**2) + sqrt(1 + m.x65**2) + 
                        sqrt(1 + m.x66**2) + sqrt(1 + m.x66**2) + sqrt(1 + m.x67**2) + sqrt(1 + m.x67**2) + sqrt(1 + 
                        m.x68**2) + sqrt(1 + m.x68**2) + sqrt(1 + m.x69**2) + sqrt(1 + m.x69**2) + sqrt(1 + m.x70**2) + 
                        sqrt(1 + m.x70**2) + sqrt(1 + m.x71**2) + sqrt(1 + m.x71**2) + sqrt(1 + m.x72**2) + sqrt(1 + 
                        m.x72**2) + sqrt(1 + m.x73**2) + sqrt(1 + m.x73**2) + sqrt(1 + m.x74**2) + sqrt(1 + m.x74**2) + 
                        sqrt(1 + m.x75**2) + sqrt(1 + m.x75**2) + sqrt(1 + m.x76**2) + sqrt(1 + m.x76**2) + sqrt(1 + 
                        m.x77**2) + sqrt(1 + m.x77**2) + sqrt(1 + m.x78**2) + sqrt(1 + m.x78**2) + sqrt(1 + m.x79**2) + 
                        sqrt(1 + m.x79**2) + sqrt(1 + m.x80**2) + sqrt(1 + m.x80**2) + sqrt(1 + m.x81**2) + sqrt(1 + 
                        m.x81**2) + sqrt(1 + m.x82**2) + sqrt(1 + m.x82**2) + sqrt(1 + m.x83**2) + sqrt(1 + m.x83**2) + 
                        sqrt(1 + m.x84**2) + sqrt(1 + m.x84**2) + sqrt(1 + m.x85**2) + sqrt(1 + m.x85**2) + sqrt(1 + 
                        m.x86**2) + sqrt(1 + m.x86**2) + sqrt(1 + m.x87**2) + sqrt(1 + m.x87**2) + sqrt(1 + m.x88**2) + 
                        sqrt(1 + m.x88**2) + sqrt(1 + m.x89**2) + sqrt(1 + m.x89**2) + sqrt(1 + m.x90**2) + sqrt(1 + 
                        m.x90**2) + sqrt(1 + m.x91**2) + sqrt(1 + m.x91**2) + sqrt(1 + m.x92**2) + sqrt(1 + m.x92**2) + 
                        sqrt(1 + m.x93**2) + sqrt(1 + m.x93**2) + sqrt(1 + m.x94**2) + sqrt(1 + m.x94**2) + sqrt(1 + 
                        m.x95**2) + sqrt(1 + m.x95**2) + sqrt(1 + m.x96**2) + sqrt(1 + m.x96**2) + sqrt(1 + m.x97**2) + 
                        sqrt(1 + m.x97**2) + sqrt(1 + m.x98**2) + sqrt(1 + m.x98**2) + sqrt(1 + m.x99**2) + sqrt(1 + 
                        m.x99**2) + sqrt(1 + m.x100**2) + sqrt(1 + m.x100**2) + sqrt(1 + m.x101**2) + sqrt(1 + m.x101**2
                        ) + sqrt(1 + m.x102**2)) == 4)
