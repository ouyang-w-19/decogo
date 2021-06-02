#  NLP written by GAMS Convert at 04/21/18 13:52:28
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        300       24      276        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         97       97        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2580      276     2304        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(-2,2),initialize=-1.313011472)
m.x2 = Var(within=Reals,bounds=(-2,2),initialize=1.373066832)
m.x3 = Var(within=Reals,bounds=(-2,2),initialize=0.201501424)
m.x4 = Var(within=Reals,bounds=(-2,2),initialize=-0.795448384)
m.x5 = Var(within=Reals,bounds=(-2,2),initialize=-0.831151532)
m.x6 = Var(within=Reals,bounds=(-2,2),initialize=-1.103788532)
m.x7 = Var(within=Reals,bounds=(-2,2),initialize=-0.600677984)
m.x8 = Var(within=Reals,bounds=(-2,2),initialize=1.425081388)
m.x9 = Var(within=Reals,bounds=(-2,2),initialize=-1.731545108)
m.x10 = Var(within=Reals,bounds=(-2,2),initialize=0.000842675999999987)
m.x11 = Var(within=Reals,bounds=(-2,2),initialize=1.992470508)
m.x12 = Var(within=Reals,bounds=(-2,2),initialize=0.314933512)
m.x13 = Var(within=Reals,bounds=(-2,2),initialize=1.964532156)
m.x14 = Var(within=Reals,bounds=(-2,2),initialize=1.049001868)
m.x15 = Var(within=Reals,bounds=(-2,2),initialize=-1.477230068)
m.x16 = Var(within=Reals,bounds=(-2,2),initialize=0.558875036)
m.x17 = Var(within=Reals,bounds=(-2,2),initialize=-1.361928544)
m.x18 = Var(within=Reals,bounds=(-2,2),initialize=-0.999677868)
m.x19 = Var(within=Reals,bounds=(-2,2),initialize=0.675714436)
m.x20 = Var(within=Reals,bounds=(-2,2),initialize=-0.258574476)
m.x21 = Var(within=Reals,bounds=(-2,2),initialize=-0.561198936)
m.x22 = Var(within=Reals,bounds=(-2,2),initialize=-0.594234528)
m.x23 = Var(within=Reals,bounds=(-2,2),initialize=-1.47403364)
m.x24 = Var(within=Reals,bounds=(-2,2),initialize=-1.399592848)
m.x25 = Var(within=Reals,bounds=(-2,2),initialize=0.3564546)
m.x26 = Var(within=Reals,bounds=(-2,2),initialize=1.323571248)
m.x27 = Var(within=Reals,bounds=(-2,2),initialize=-1.076737048)
m.x28 = Var(within=Reals,bounds=(-2,2),initialize=0.66293784)
m.x29 = Var(within=Reals,bounds=(-2,2),initialize=1.103430424)
m.x30 = Var(within=Reals,bounds=(-2,2),initialize=-0.785366092)
m.x31 = Var(within=Reals,bounds=(-2,2),initialize=-1.558030836)
m.x32 = Var(within=Reals,bounds=(-2,2),initialize=0.00953946399999994)
m.x33 = Var(within=Reals,bounds=(-2,2),initialize=-1.359308952)
m.x34 = Var(within=Reals,bounds=(-2,2),initialize=1.489849244)
m.x35 = Var(within=Reals,bounds=(-2,2),initialize=-0.93954182)
m.x36 = Var(within=Reals,bounds=(-2,2),initialize=-0.856742712)
m.x37 = Var(within=Reals,bounds=(-2,2),initialize=0.375823688)
m.x38 = Var(within=Reals,bounds=(-2,2),initialize=0.890876284)
m.x39 = Var(within=Reals,bounds=(-2,2),initialize=0.512994708)
m.x40 = Var(within=Reals,bounds=(-2,2),initialize=-0.14480854)
m.x41 = Var(within=Reals,bounds=(-2,2),initialize=-0.346772024)
m.x42 = Var(within=Reals,bounds=(-2,2),initialize=-1.529218572)
m.x43 = Var(within=Reals,bounds=(-2,2),initialize=-0.743150932)
m.x44 = Var(within=Reals,bounds=(-2,2),initialize=-1.813793944)
m.x45 = Var(within=Reals,bounds=(-2,2),initialize=-0.645798912)
m.x46 = Var(within=Reals,bounds=(-2,2),initialize=-1.271601628)
m.x47 = Var(within=Reals,bounds=(-2,2),initialize=0.582908508)
m.x48 = Var(within=Reals,bounds=(-2,2),initialize=0.242982188)
m.x49 = Var(within=Reals,bounds=(-2,2),initialize=1.07984688)
m.x50 = Var(within=Reals,bounds=(-2,2),initialize=-0.808776544)
m.x51 = Var(within=Reals,bounds=(-2,2),initialize=0.644425044)
m.x52 = Var(within=Reals,bounds=(-2,2),initialize=1.023286696)
m.x53 = Var(within=Reals,bounds=(-2,2),initialize=0.509789996)
m.x54 = Var(within=Reals,bounds=(-2,2),initialize=-0.864543208)
m.x55 = Var(within=Reals,bounds=(-2,2),initialize=-1.654301504)
m.x56 = Var(within=Reals,bounds=(-2,2),initialize=-1.589941324)
m.x57 = Var(within=Reals,bounds=(-2,2),initialize=0.565004604)
m.x58 = Var(within=Reals,bounds=(-2,2),initialize=0.181237992)
m.x59 = Var(within=Reals,bounds=(-2,2),initialize=-1.873900592)
m.x60 = Var(within=Reals,bounds=(-2,2),initialize=1.169442568)
m.x61 = Var(within=Reals,bounds=(-2,2),initialize=-1.708932008)
m.x62 = Var(within=Reals,bounds=(-2,2),initialize=-1.297355804)
m.x63 = Var(within=Reals,bounds=(-2,2),initialize=0.102530452)
m.x64 = Var(within=Reals,bounds=(-2,2),initialize=1.000830676)
m.x65 = Var(within=Reals,bounds=(-2,2),initialize=-1.287505144)
m.x66 = Var(within=Reals,bounds=(-2,2),initialize=-1.863436056)
m.x67 = Var(within=Reals,bounds=(-2,2),initialize=0.340524692)
m.x68 = Var(within=Reals,bounds=(-2,2),initialize=0.484919936)
m.x69 = Var(within=Reals,bounds=(-2,2),initialize=-0.4425524)
m.x70 = Var(within=Reals,bounds=(-2,2),initialize=-0.565143388)
m.x71 = Var(within=Reals,bounds=(-2,2),initialize=-1.027861532)
m.x72 = Var(within=Reals,bounds=(-2,2),initialize=-1.014313844)
m.x73 = Var(within=Reals,bounds=(-2,2),initialize=-1.477988788)
m.x74 = Var(within=Reals,bounds=(-2,2),initialize=1.73379888)
m.x75 = Var(within=Reals,bounds=(-2,2),initialize=-0.480248376)
m.x76 = Var(within=Reals,bounds=(-2,2),initialize=1.133601844)
m.x77 = Var(within=Reals,bounds=(-2,2),initialize=-0.799862968)
m.x78 = Var(within=Reals,bounds=(-2,2),initialize=-1.498067112)
m.x79 = Var(within=Reals,bounds=(-2,2),initialize=0.99549642)
m.x80 = Var(within=Reals,bounds=(-2,2),initialize=-1.723070148)
m.x81 = Var(within=Reals,bounds=(-2,2),initialize=-1.191937772)
m.x82 = Var(within=Reals,bounds=(-2,2),initialize=-1.979736568)
m.x83 = Var(within=Reals,bounds=(-2,2),initialize=-0.921547792)
m.x84 = Var(within=Reals,bounds=(-2,2),initialize=-0.00059409999999982)
m.x85 = Var(within=Reals,bounds=(-2,2),initialize=-1.394856524)
m.x86 = Var(within=Reals,bounds=(-2,2),initialize=-1.30332218)
m.x87 = Var(within=Reals,bounds=(-2,2),initialize=-0.677449064)
m.x88 = Var(within=Reals,bounds=(-2,2),initialize=-0.732375784)
m.x89 = Var(within=Reals,bounds=(-2,2),initialize=-0.71165218)
m.x90 = Var(within=Reals,bounds=(-2,2),initialize=1.855906564)
m.x91 = Var(within=Reals,bounds=(-2,2),initialize=1.97440882)
m.x92 = Var(within=Reals,bounds=(-2,2),initialize=-0.52038778)
m.x93 = Var(within=Reals,bounds=(-2,2),initialize=-0.508445732)
m.x94 = Var(within=Reals,bounds=(-2,2),initialize=1.08791332)
m.x95 = Var(within=Reals,bounds=(-2,2),initialize=-0.413263432)
m.x96 = Var(within=Reals,bounds=(-2,2),initialize=1.6523853)
m.x97 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x97, sense=maximize)

m.c1 = Constraint(expr=m.x1**2 + m.x2**2 + m.x3**2 + m.x4**2 == 4)

m.c2 = Constraint(expr=m.x5**2 + m.x6**2 + m.x7**2 + m.x8**2 == 4)

m.c3 = Constraint(expr=m.x9**2 + m.x10**2 + m.x11**2 + m.x12**2 == 4)

m.c4 = Constraint(expr=m.x13**2 + m.x14**2 + m.x15**2 + m.x16**2 == 4)

m.c5 = Constraint(expr=m.x17**2 + m.x18**2 + m.x19**2 + m.x20**2 == 4)

m.c6 = Constraint(expr=m.x21**2 + m.x22**2 + m.x23**2 + m.x24**2 == 4)

m.c7 = Constraint(expr=m.x25**2 + m.x26**2 + m.x27**2 + m.x28**2 == 4)

m.c8 = Constraint(expr=m.x29**2 + m.x30**2 + m.x31**2 + m.x32**2 == 4)

m.c9 = Constraint(expr=m.x33**2 + m.x34**2 + m.x35**2 + m.x36**2 == 4)

m.c10 = Constraint(expr=m.x37**2 + m.x38**2 + m.x39**2 + m.x40**2 == 4)

m.c11 = Constraint(expr=m.x41**2 + m.x42**2 + m.x43**2 + m.x44**2 == 4)

m.c12 = Constraint(expr=m.x45**2 + m.x46**2 + m.x47**2 + m.x48**2 == 4)

m.c13 = Constraint(expr=m.x49**2 + m.x50**2 + m.x51**2 + m.x52**2 == 4)

m.c14 = Constraint(expr=m.x53**2 + m.x54**2 + m.x55**2 + m.x56**2 == 4)

m.c15 = Constraint(expr=m.x57**2 + m.x58**2 + m.x59**2 + m.x60**2 == 4)

m.c16 = Constraint(expr=m.x61**2 + m.x62**2 + m.x63**2 + m.x64**2 == 4)

m.c17 = Constraint(expr=m.x65**2 + m.x66**2 + m.x67**2 + m.x68**2 == 4)

m.c18 = Constraint(expr=m.x69**2 + m.x70**2 + m.x71**2 + m.x72**2 == 4)

m.c19 = Constraint(expr=m.x73**2 + m.x74**2 + m.x75**2 + m.x76**2 == 4)

m.c20 = Constraint(expr=m.x77**2 + m.x78**2 + m.x79**2 + m.x80**2 == 4)

m.c21 = Constraint(expr=m.x81**2 + m.x82**2 + m.x83**2 + m.x84**2 == 4)

m.c22 = Constraint(expr=m.x85**2 + m.x86**2 + m.x87**2 + m.x88**2 == 4)

m.c23 = Constraint(expr=m.x89**2 + m.x90**2 + m.x91**2 + m.x92**2 == 4)

m.c24 = Constraint(expr=m.x93**2 + m.x94**2 + m.x95**2 + m.x96**2 == 4)

m.c25 = Constraint(expr=(m.x1 - m.x5)**2 + (m.x2 - m.x6)**2 + (m.x3 - m.x7)**2 + (m.x4 - m.x8)**2 - 4*m.x97 >= 0)

m.c26 = Constraint(expr=(m.x1 - m.x9)**2 + (m.x2 - m.x10)**2 + (m.x3 - m.x11)**2 + (m.x4 - m.x12)**2 - 4*m.x97 >= 0)

m.c27 = Constraint(expr=(m.x1 - m.x13)**2 + (m.x2 - m.x14)**2 + (m.x3 - m.x15)**2 + (m.x4 - m.x16)**2 - 4*m.x97 >= 0)

m.c28 = Constraint(expr=(m.x1 - m.x17)**2 + (m.x2 - m.x18)**2 + (m.x3 - m.x19)**2 + (m.x4 - m.x20)**2 - 4*m.x97 >= 0)

m.c29 = Constraint(expr=(m.x1 - m.x21)**2 + (m.x2 - m.x22)**2 + (m.x3 - m.x23)**2 + (m.x4 - m.x24)**2 - 4*m.x97 >= 0)

m.c30 = Constraint(expr=(m.x1 - m.x25)**2 + (m.x2 - m.x26)**2 + (m.x3 - m.x27)**2 + (m.x4 - m.x28)**2 - 4*m.x97 >= 0)

m.c31 = Constraint(expr=(m.x1 - m.x29)**2 + (m.x2 - m.x30)**2 + (m.x3 - m.x31)**2 + (m.x4 - m.x32)**2 - 4*m.x97 >= 0)

m.c32 = Constraint(expr=(m.x1 - m.x33)**2 + (m.x2 - m.x34)**2 + (m.x3 - m.x35)**2 + (m.x4 - m.x36)**2 - 4*m.x97 >= 0)

m.c33 = Constraint(expr=(m.x1 - m.x37)**2 + (m.x2 - m.x38)**2 + (m.x3 - m.x39)**2 + (m.x4 - m.x40)**2 - 4*m.x97 >= 0)

m.c34 = Constraint(expr=(m.x1 - m.x41)**2 + (m.x2 - m.x42)**2 + (m.x3 - m.x43)**2 + (m.x4 - m.x44)**2 - 4*m.x97 >= 0)

m.c35 = Constraint(expr=(m.x1 - m.x45)**2 + (m.x2 - m.x46)**2 + (m.x3 - m.x47)**2 + (m.x4 - m.x48)**2 - 4*m.x97 >= 0)

m.c36 = Constraint(expr=(m.x1 - m.x49)**2 + (m.x2 - m.x50)**2 + (m.x3 - m.x51)**2 + (m.x4 - m.x52)**2 - 4*m.x97 >= 0)

m.c37 = Constraint(expr=(m.x1 - m.x53)**2 + (m.x2 - m.x54)**2 + (m.x3 - m.x55)**2 + (m.x4 - m.x56)**2 - 4*m.x97 >= 0)

m.c38 = Constraint(expr=(m.x1 - m.x57)**2 + (m.x2 - m.x58)**2 + (m.x3 - m.x59)**2 + (m.x4 - m.x60)**2 - 4*m.x97 >= 0)

m.c39 = Constraint(expr=(m.x1 - m.x61)**2 + (m.x2 - m.x62)**2 + (m.x3 - m.x63)**2 + (m.x4 - m.x64)**2 - 4*m.x97 >= 0)

m.c40 = Constraint(expr=(m.x1 - m.x65)**2 + (m.x2 - m.x66)**2 + (m.x3 - m.x67)**2 + (m.x4 - m.x68)**2 - 4*m.x97 >= 0)

m.c41 = Constraint(expr=(m.x1 - m.x69)**2 + (m.x2 - m.x70)**2 + (m.x3 - m.x71)**2 + (m.x4 - m.x72)**2 - 4*m.x97 >= 0)

m.c42 = Constraint(expr=(m.x1 - m.x73)**2 + (m.x2 - m.x74)**2 + (m.x3 - m.x75)**2 + (m.x4 - m.x76)**2 - 4*m.x97 >= 0)

m.c43 = Constraint(expr=(m.x1 - m.x77)**2 + (m.x2 - m.x78)**2 + (m.x3 - m.x79)**2 + (m.x4 - m.x80)**2 - 4*m.x97 >= 0)

m.c44 = Constraint(expr=(m.x1 - m.x81)**2 + (m.x2 - m.x82)**2 + (m.x3 - m.x83)**2 + (m.x4 - m.x84)**2 - 4*m.x97 >= 0)

m.c45 = Constraint(expr=(m.x1 - m.x85)**2 + (m.x2 - m.x86)**2 + (m.x3 - m.x87)**2 + (m.x4 - m.x88)**2 - 4*m.x97 >= 0)

m.c46 = Constraint(expr=(m.x1 - m.x89)**2 + (m.x2 - m.x90)**2 + (m.x3 - m.x91)**2 + (m.x4 - m.x92)**2 - 4*m.x97 >= 0)

m.c47 = Constraint(expr=(m.x1 - m.x93)**2 + (m.x2 - m.x94)**2 + (m.x3 - m.x95)**2 + (m.x4 - m.x96)**2 - 4*m.x97 >= 0)

m.c48 = Constraint(expr=(m.x5 - m.x9)**2 + (m.x6 - m.x10)**2 + (m.x7 - m.x11)**2 + (m.x8 - m.x12)**2 - 4*m.x97 >= 0)

m.c49 = Constraint(expr=(m.x5 - m.x13)**2 + (m.x6 - m.x14)**2 + (m.x7 - m.x15)**2 + (m.x8 - m.x16)**2 - 4*m.x97 >= 0)

m.c50 = Constraint(expr=(m.x5 - m.x17)**2 + (m.x6 - m.x18)**2 + (m.x7 - m.x19)**2 + (m.x8 - m.x20)**2 - 4*m.x97 >= 0)

m.c51 = Constraint(expr=(m.x5 - m.x21)**2 + (m.x6 - m.x22)**2 + (m.x7 - m.x23)**2 + (m.x8 - m.x24)**2 - 4*m.x97 >= 0)

m.c52 = Constraint(expr=(m.x5 - m.x25)**2 + (m.x6 - m.x26)**2 + (m.x7 - m.x27)**2 + (m.x8 - m.x28)**2 - 4*m.x97 >= 0)

m.c53 = Constraint(expr=(m.x5 - m.x29)**2 + (m.x6 - m.x30)**2 + (m.x7 - m.x31)**2 + (m.x8 - m.x32)**2 - 4*m.x97 >= 0)

m.c54 = Constraint(expr=(m.x5 - m.x33)**2 + (m.x6 - m.x34)**2 + (m.x7 - m.x35)**2 + (m.x8 - m.x36)**2 - 4*m.x97 >= 0)

m.c55 = Constraint(expr=(m.x5 - m.x37)**2 + (m.x6 - m.x38)**2 + (m.x7 - m.x39)**2 + (m.x8 - m.x40)**2 - 4*m.x97 >= 0)

m.c56 = Constraint(expr=(m.x5 - m.x41)**2 + (m.x6 - m.x42)**2 + (m.x7 - m.x43)**2 + (m.x8 - m.x44)**2 - 4*m.x97 >= 0)

m.c57 = Constraint(expr=(m.x5 - m.x45)**2 + (m.x6 - m.x46)**2 + (m.x7 - m.x47)**2 + (m.x8 - m.x48)**2 - 4*m.x97 >= 0)

m.c58 = Constraint(expr=(m.x5 - m.x49)**2 + (m.x6 - m.x50)**2 + (m.x7 - m.x51)**2 + (m.x8 - m.x52)**2 - 4*m.x97 >= 0)

m.c59 = Constraint(expr=(m.x5 - m.x53)**2 + (m.x6 - m.x54)**2 + (m.x7 - m.x55)**2 + (m.x8 - m.x56)**2 - 4*m.x97 >= 0)

m.c60 = Constraint(expr=(m.x5 - m.x57)**2 + (m.x6 - m.x58)**2 + (m.x7 - m.x59)**2 + (m.x8 - m.x60)**2 - 4*m.x97 >= 0)

m.c61 = Constraint(expr=(m.x5 - m.x61)**2 + (m.x6 - m.x62)**2 + (m.x7 - m.x63)**2 + (m.x8 - m.x64)**2 - 4*m.x97 >= 0)

m.c62 = Constraint(expr=(m.x5 - m.x65)**2 + (m.x6 - m.x66)**2 + (m.x7 - m.x67)**2 + (m.x8 - m.x68)**2 - 4*m.x97 >= 0)

m.c63 = Constraint(expr=(m.x5 - m.x69)**2 + (m.x6 - m.x70)**2 + (m.x7 - m.x71)**2 + (m.x8 - m.x72)**2 - 4*m.x97 >= 0)

m.c64 = Constraint(expr=(m.x5 - m.x73)**2 + (m.x6 - m.x74)**2 + (m.x7 - m.x75)**2 + (m.x8 - m.x76)**2 - 4*m.x97 >= 0)

m.c65 = Constraint(expr=(m.x5 - m.x77)**2 + (m.x6 - m.x78)**2 + (m.x7 - m.x79)**2 + (m.x8 - m.x80)**2 - 4*m.x97 >= 0)

m.c66 = Constraint(expr=(m.x5 - m.x81)**2 + (m.x6 - m.x82)**2 + (m.x7 - m.x83)**2 + (m.x8 - m.x84)**2 - 4*m.x97 >= 0)

m.c67 = Constraint(expr=(m.x5 - m.x85)**2 + (m.x6 - m.x86)**2 + (m.x7 - m.x87)**2 + (m.x8 - m.x88)**2 - 4*m.x97 >= 0)

m.c68 = Constraint(expr=(m.x5 - m.x89)**2 + (m.x6 - m.x90)**2 + (m.x7 - m.x91)**2 + (m.x8 - m.x92)**2 - 4*m.x97 >= 0)

m.c69 = Constraint(expr=(m.x5 - m.x93)**2 + (m.x6 - m.x94)**2 + (m.x7 - m.x95)**2 + (m.x8 - m.x96)**2 - 4*m.x97 >= 0)

m.c70 = Constraint(expr=(m.x9 - m.x13)**2 + (m.x10 - m.x14)**2 + (m.x11 - m.x15)**2 + (m.x12 - m.x16)**2 - 4*m.x97 >= 0)

m.c71 = Constraint(expr=(m.x9 - m.x17)**2 + (m.x10 - m.x18)**2 + (m.x11 - m.x19)**2 + (m.x12 - m.x20)**2 - 4*m.x97 >= 0)

m.c72 = Constraint(expr=(m.x9 - m.x21)**2 + (m.x10 - m.x22)**2 + (m.x11 - m.x23)**2 + (m.x12 - m.x24)**2 - 4*m.x97 >= 0)

m.c73 = Constraint(expr=(m.x9 - m.x25)**2 + (m.x10 - m.x26)**2 + (m.x11 - m.x27)**2 + (m.x12 - m.x28)**2 - 4*m.x97 >= 0)

m.c74 = Constraint(expr=(m.x9 - m.x29)**2 + (m.x10 - m.x30)**2 + (m.x11 - m.x31)**2 + (m.x12 - m.x32)**2 - 4*m.x97 >= 0)

m.c75 = Constraint(expr=(m.x9 - m.x33)**2 + (m.x10 - m.x34)**2 + (m.x11 - m.x35)**2 + (m.x12 - m.x36)**2 - 4*m.x97 >= 0)

m.c76 = Constraint(expr=(m.x9 - m.x37)**2 + (m.x10 - m.x38)**2 + (m.x11 - m.x39)**2 + (m.x12 - m.x40)**2 - 4*m.x97 >= 0)

m.c77 = Constraint(expr=(m.x9 - m.x41)**2 + (m.x10 - m.x42)**2 + (m.x11 - m.x43)**2 + (m.x12 - m.x44)**2 - 4*m.x97 >= 0)

m.c78 = Constraint(expr=(m.x9 - m.x45)**2 + (m.x10 - m.x46)**2 + (m.x11 - m.x47)**2 + (m.x12 - m.x48)**2 - 4*m.x97 >= 0)

m.c79 = Constraint(expr=(m.x9 - m.x49)**2 + (m.x10 - m.x50)**2 + (m.x11 - m.x51)**2 + (m.x12 - m.x52)**2 - 4*m.x97 >= 0)

m.c80 = Constraint(expr=(m.x9 - m.x53)**2 + (m.x10 - m.x54)**2 + (m.x11 - m.x55)**2 + (m.x12 - m.x56)**2 - 4*m.x97 >= 0)

m.c81 = Constraint(expr=(m.x9 - m.x57)**2 + (m.x10 - m.x58)**2 + (m.x11 - m.x59)**2 + (m.x12 - m.x60)**2 - 4*m.x97 >= 0)

m.c82 = Constraint(expr=(m.x9 - m.x61)**2 + (m.x10 - m.x62)**2 + (m.x11 - m.x63)**2 + (m.x12 - m.x64)**2 - 4*m.x97 >= 0)

m.c83 = Constraint(expr=(m.x9 - m.x65)**2 + (m.x10 - m.x66)**2 + (m.x11 - m.x67)**2 + (m.x12 - m.x68)**2 - 4*m.x97 >= 0)

m.c84 = Constraint(expr=(m.x9 - m.x69)**2 + (m.x10 - m.x70)**2 + (m.x11 - m.x71)**2 + (m.x12 - m.x72)**2 - 4*m.x97 >= 0)

m.c85 = Constraint(expr=(m.x9 - m.x73)**2 + (m.x10 - m.x74)**2 + (m.x11 - m.x75)**2 + (m.x12 - m.x76)**2 - 4*m.x97 >= 0)

m.c86 = Constraint(expr=(m.x9 - m.x77)**2 + (m.x10 - m.x78)**2 + (m.x11 - m.x79)**2 + (m.x12 - m.x80)**2 - 4*m.x97 >= 0)

m.c87 = Constraint(expr=(m.x9 - m.x81)**2 + (m.x10 - m.x82)**2 + (m.x11 - m.x83)**2 + (m.x12 - m.x84)**2 - 4*m.x97 >= 0)

m.c88 = Constraint(expr=(m.x9 - m.x85)**2 + (m.x10 - m.x86)**2 + (m.x11 - m.x87)**2 + (m.x12 - m.x88)**2 - 4*m.x97 >= 0)

m.c89 = Constraint(expr=(m.x9 - m.x89)**2 + (m.x10 - m.x90)**2 + (m.x11 - m.x91)**2 + (m.x12 - m.x92)**2 - 4*m.x97 >= 0)

m.c90 = Constraint(expr=(m.x9 - m.x93)**2 + (m.x10 - m.x94)**2 + (m.x11 - m.x95)**2 + (m.x12 - m.x96)**2 - 4*m.x97 >= 0)

m.c91 = Constraint(expr=(m.x13 - m.x17)**2 + (m.x14 - m.x18)**2 + (m.x15 - m.x19)**2 + (m.x16 - m.x20)**2 - 4*m.x97
                         >= 0)

m.c92 = Constraint(expr=(m.x13 - m.x21)**2 + (m.x14 - m.x22)**2 + (m.x15 - m.x23)**2 + (m.x16 - m.x24)**2 - 4*m.x97
                         >= 0)

m.c93 = Constraint(expr=(m.x13 - m.x25)**2 + (m.x14 - m.x26)**2 + (m.x15 - m.x27)**2 + (m.x16 - m.x28)**2 - 4*m.x97
                         >= 0)

m.c94 = Constraint(expr=(m.x13 - m.x29)**2 + (m.x14 - m.x30)**2 + (m.x15 - m.x31)**2 + (m.x16 - m.x32)**2 - 4*m.x97
                         >= 0)

m.c95 = Constraint(expr=(m.x13 - m.x33)**2 + (m.x14 - m.x34)**2 + (m.x15 - m.x35)**2 + (m.x16 - m.x36)**2 - 4*m.x97
                         >= 0)

m.c96 = Constraint(expr=(m.x13 - m.x37)**2 + (m.x14 - m.x38)**2 + (m.x15 - m.x39)**2 + (m.x16 - m.x40)**2 - 4*m.x97
                         >= 0)

m.c97 = Constraint(expr=(m.x13 - m.x41)**2 + (m.x14 - m.x42)**2 + (m.x15 - m.x43)**2 + (m.x16 - m.x44)**2 - 4*m.x97
                         >= 0)

m.c98 = Constraint(expr=(m.x13 - m.x45)**2 + (m.x14 - m.x46)**2 + (m.x15 - m.x47)**2 + (m.x16 - m.x48)**2 - 4*m.x97
                         >= 0)

m.c99 = Constraint(expr=(m.x13 - m.x49)**2 + (m.x14 - m.x50)**2 + (m.x15 - m.x51)**2 + (m.x16 - m.x52)**2 - 4*m.x97
                         >= 0)

m.c100 = Constraint(expr=(m.x13 - m.x53)**2 + (m.x14 - m.x54)**2 + (m.x15 - m.x55)**2 + (m.x16 - m.x56)**2 - 4*m.x97
                          >= 0)

m.c101 = Constraint(expr=(m.x13 - m.x57)**2 + (m.x14 - m.x58)**2 + (m.x15 - m.x59)**2 + (m.x16 - m.x60)**2 - 4*m.x97
                          >= 0)

m.c102 = Constraint(expr=(m.x13 - m.x61)**2 + (m.x14 - m.x62)**2 + (m.x15 - m.x63)**2 + (m.x16 - m.x64)**2 - 4*m.x97
                          >= 0)

m.c103 = Constraint(expr=(m.x13 - m.x65)**2 + (m.x14 - m.x66)**2 + (m.x15 - m.x67)**2 + (m.x16 - m.x68)**2 - 4*m.x97
                          >= 0)

m.c104 = Constraint(expr=(m.x13 - m.x69)**2 + (m.x14 - m.x70)**2 + (m.x15 - m.x71)**2 + (m.x16 - m.x72)**2 - 4*m.x97
                          >= 0)

m.c105 = Constraint(expr=(m.x13 - m.x73)**2 + (m.x14 - m.x74)**2 + (m.x15 - m.x75)**2 + (m.x16 - m.x76)**2 - 4*m.x97
                          >= 0)

m.c106 = Constraint(expr=(m.x13 - m.x77)**2 + (m.x14 - m.x78)**2 + (m.x15 - m.x79)**2 + (m.x16 - m.x80)**2 - 4*m.x97
                          >= 0)

m.c107 = Constraint(expr=(m.x13 - m.x81)**2 + (m.x14 - m.x82)**2 + (m.x15 - m.x83)**2 + (m.x16 - m.x84)**2 - 4*m.x97
                          >= 0)

m.c108 = Constraint(expr=(m.x13 - m.x85)**2 + (m.x14 - m.x86)**2 + (m.x15 - m.x87)**2 + (m.x16 - m.x88)**2 - 4*m.x97
                          >= 0)

m.c109 = Constraint(expr=(m.x13 - m.x89)**2 + (m.x14 - m.x90)**2 + (m.x15 - m.x91)**2 + (m.x16 - m.x92)**2 - 4*m.x97
                          >= 0)

m.c110 = Constraint(expr=(m.x13 - m.x93)**2 + (m.x14 - m.x94)**2 + (m.x15 - m.x95)**2 + (m.x16 - m.x96)**2 - 4*m.x97
                          >= 0)

m.c111 = Constraint(expr=(m.x17 - m.x21)**2 + (m.x18 - m.x22)**2 + (m.x19 - m.x23)**2 + (m.x20 - m.x24)**2 - 4*m.x97
                          >= 0)

m.c112 = Constraint(expr=(m.x17 - m.x25)**2 + (m.x18 - m.x26)**2 + (m.x19 - m.x27)**2 + (m.x20 - m.x28)**2 - 4*m.x97
                          >= 0)

m.c113 = Constraint(expr=(m.x17 - m.x29)**2 + (m.x18 - m.x30)**2 + (m.x19 - m.x31)**2 + (m.x20 - m.x32)**2 - 4*m.x97
                          >= 0)

m.c114 = Constraint(expr=(m.x17 - m.x33)**2 + (m.x18 - m.x34)**2 + (m.x19 - m.x35)**2 + (m.x20 - m.x36)**2 - 4*m.x97
                          >= 0)

m.c115 = Constraint(expr=(m.x17 - m.x37)**2 + (m.x18 - m.x38)**2 + (m.x19 - m.x39)**2 + (m.x20 - m.x40)**2 - 4*m.x97
                          >= 0)

m.c116 = Constraint(expr=(m.x17 - m.x41)**2 + (m.x18 - m.x42)**2 + (m.x19 - m.x43)**2 + (m.x20 - m.x44)**2 - 4*m.x97
                          >= 0)

m.c117 = Constraint(expr=(m.x17 - m.x45)**2 + (m.x18 - m.x46)**2 + (m.x19 - m.x47)**2 + (m.x20 - m.x48)**2 - 4*m.x97
                          >= 0)

m.c118 = Constraint(expr=(m.x17 - m.x49)**2 + (m.x18 - m.x50)**2 + (m.x19 - m.x51)**2 + (m.x20 - m.x52)**2 - 4*m.x97
                          >= 0)

m.c119 = Constraint(expr=(m.x17 - m.x53)**2 + (m.x18 - m.x54)**2 + (m.x19 - m.x55)**2 + (m.x20 - m.x56)**2 - 4*m.x97
                          >= 0)

m.c120 = Constraint(expr=(m.x17 - m.x57)**2 + (m.x18 - m.x58)**2 + (m.x19 - m.x59)**2 + (m.x20 - m.x60)**2 - 4*m.x97
                          >= 0)

m.c121 = Constraint(expr=(m.x17 - m.x61)**2 + (m.x18 - m.x62)**2 + (m.x19 - m.x63)**2 + (m.x20 - m.x64)**2 - 4*m.x97
                          >= 0)

m.c122 = Constraint(expr=(m.x17 - m.x65)**2 + (m.x18 - m.x66)**2 + (m.x19 - m.x67)**2 + (m.x20 - m.x68)**2 - 4*m.x97
                          >= 0)

m.c123 = Constraint(expr=(m.x17 - m.x69)**2 + (m.x18 - m.x70)**2 + (m.x19 - m.x71)**2 + (m.x20 - m.x72)**2 - 4*m.x97
                          >= 0)

m.c124 = Constraint(expr=(m.x17 - m.x73)**2 + (m.x18 - m.x74)**2 + (m.x19 - m.x75)**2 + (m.x20 - m.x76)**2 - 4*m.x97
                          >= 0)

m.c125 = Constraint(expr=(m.x17 - m.x77)**2 + (m.x18 - m.x78)**2 + (m.x19 - m.x79)**2 + (m.x20 - m.x80)**2 - 4*m.x97
                          >= 0)

m.c126 = Constraint(expr=(m.x17 - m.x81)**2 + (m.x18 - m.x82)**2 + (m.x19 - m.x83)**2 + (m.x20 - m.x84)**2 - 4*m.x97
                          >= 0)

m.c127 = Constraint(expr=(m.x17 - m.x85)**2 + (m.x18 - m.x86)**2 + (m.x19 - m.x87)**2 + (m.x20 - m.x88)**2 - 4*m.x97
                          >= 0)

m.c128 = Constraint(expr=(m.x17 - m.x89)**2 + (m.x18 - m.x90)**2 + (m.x19 - m.x91)**2 + (m.x20 - m.x92)**2 - 4*m.x97
                          >= 0)

m.c129 = Constraint(expr=(m.x17 - m.x93)**2 + (m.x18 - m.x94)**2 + (m.x19 - m.x95)**2 + (m.x20 - m.x96)**2 - 4*m.x97
                          >= 0)

m.c130 = Constraint(expr=(m.x21 - m.x25)**2 + (m.x22 - m.x26)**2 + (m.x23 - m.x27)**2 + (m.x24 - m.x28)**2 - 4*m.x97
                          >= 0)

m.c131 = Constraint(expr=(m.x21 - m.x29)**2 + (m.x22 - m.x30)**2 + (m.x23 - m.x31)**2 + (m.x24 - m.x32)**2 - 4*m.x97
                          >= 0)

m.c132 = Constraint(expr=(m.x21 - m.x33)**2 + (m.x22 - m.x34)**2 + (m.x23 - m.x35)**2 + (m.x24 - m.x36)**2 - 4*m.x97
                          >= 0)

m.c133 = Constraint(expr=(m.x21 - m.x37)**2 + (m.x22 - m.x38)**2 + (m.x23 - m.x39)**2 + (m.x24 - m.x40)**2 - 4*m.x97
                          >= 0)

m.c134 = Constraint(expr=(m.x21 - m.x41)**2 + (m.x22 - m.x42)**2 + (m.x23 - m.x43)**2 + (m.x24 - m.x44)**2 - 4*m.x97
                          >= 0)

m.c135 = Constraint(expr=(m.x21 - m.x45)**2 + (m.x22 - m.x46)**2 + (m.x23 - m.x47)**2 + (m.x24 - m.x48)**2 - 4*m.x97
                          >= 0)

m.c136 = Constraint(expr=(m.x21 - m.x49)**2 + (m.x22 - m.x50)**2 + (m.x23 - m.x51)**2 + (m.x24 - m.x52)**2 - 4*m.x97
                          >= 0)

m.c137 = Constraint(expr=(m.x21 - m.x53)**2 + (m.x22 - m.x54)**2 + (m.x23 - m.x55)**2 + (m.x24 - m.x56)**2 - 4*m.x97
                          >= 0)

m.c138 = Constraint(expr=(m.x21 - m.x57)**2 + (m.x22 - m.x58)**2 + (m.x23 - m.x59)**2 + (m.x24 - m.x60)**2 - 4*m.x97
                          >= 0)

m.c139 = Constraint(expr=(m.x21 - m.x61)**2 + (m.x22 - m.x62)**2 + (m.x23 - m.x63)**2 + (m.x24 - m.x64)**2 - 4*m.x97
                          >= 0)

m.c140 = Constraint(expr=(m.x21 - m.x65)**2 + (m.x22 - m.x66)**2 + (m.x23 - m.x67)**2 + (m.x24 - m.x68)**2 - 4*m.x97
                          >= 0)

m.c141 = Constraint(expr=(m.x21 - m.x69)**2 + (m.x22 - m.x70)**2 + (m.x23 - m.x71)**2 + (m.x24 - m.x72)**2 - 4*m.x97
                          >= 0)

m.c142 = Constraint(expr=(m.x21 - m.x73)**2 + (m.x22 - m.x74)**2 + (m.x23 - m.x75)**2 + (m.x24 - m.x76)**2 - 4*m.x97
                          >= 0)

m.c143 = Constraint(expr=(m.x21 - m.x77)**2 + (m.x22 - m.x78)**2 + (m.x23 - m.x79)**2 + (m.x24 - m.x80)**2 - 4*m.x97
                          >= 0)

m.c144 = Constraint(expr=(m.x21 - m.x81)**2 + (m.x22 - m.x82)**2 + (m.x23 - m.x83)**2 + (m.x24 - m.x84)**2 - 4*m.x97
                          >= 0)

m.c145 = Constraint(expr=(m.x21 - m.x85)**2 + (m.x22 - m.x86)**2 + (m.x23 - m.x87)**2 + (m.x24 - m.x88)**2 - 4*m.x97
                          >= 0)

m.c146 = Constraint(expr=(m.x21 - m.x89)**2 + (m.x22 - m.x90)**2 + (m.x23 - m.x91)**2 + (m.x24 - m.x92)**2 - 4*m.x97
                          >= 0)

m.c147 = Constraint(expr=(m.x21 - m.x93)**2 + (m.x22 - m.x94)**2 + (m.x23 - m.x95)**2 + (m.x24 - m.x96)**2 - 4*m.x97
                          >= 0)

m.c148 = Constraint(expr=(m.x25 - m.x29)**2 + (m.x26 - m.x30)**2 + (m.x27 - m.x31)**2 + (m.x28 - m.x32)**2 - 4*m.x97
                          >= 0)

m.c149 = Constraint(expr=(m.x25 - m.x33)**2 + (m.x26 - m.x34)**2 + (m.x27 - m.x35)**2 + (m.x28 - m.x36)**2 - 4*m.x97
                          >= 0)

m.c150 = Constraint(expr=(m.x25 - m.x37)**2 + (m.x26 - m.x38)**2 + (m.x27 - m.x39)**2 + (m.x28 - m.x40)**2 - 4*m.x97
                          >= 0)

m.c151 = Constraint(expr=(m.x25 - m.x41)**2 + (m.x26 - m.x42)**2 + (m.x27 - m.x43)**2 + (m.x28 - m.x44)**2 - 4*m.x97
                          >= 0)

m.c152 = Constraint(expr=(m.x25 - m.x45)**2 + (m.x26 - m.x46)**2 + (m.x27 - m.x47)**2 + (m.x28 - m.x48)**2 - 4*m.x97
                          >= 0)

m.c153 = Constraint(expr=(m.x25 - m.x49)**2 + (m.x26 - m.x50)**2 + (m.x27 - m.x51)**2 + (m.x28 - m.x52)**2 - 4*m.x97
                          >= 0)

m.c154 = Constraint(expr=(m.x25 - m.x53)**2 + (m.x26 - m.x54)**2 + (m.x27 - m.x55)**2 + (m.x28 - m.x56)**2 - 4*m.x97
                          >= 0)

m.c155 = Constraint(expr=(m.x25 - m.x57)**2 + (m.x26 - m.x58)**2 + (m.x27 - m.x59)**2 + (m.x28 - m.x60)**2 - 4*m.x97
                          >= 0)

m.c156 = Constraint(expr=(m.x25 - m.x61)**2 + (m.x26 - m.x62)**2 + (m.x27 - m.x63)**2 + (m.x28 - m.x64)**2 - 4*m.x97
                          >= 0)

m.c157 = Constraint(expr=(m.x25 - m.x65)**2 + (m.x26 - m.x66)**2 + (m.x27 - m.x67)**2 + (m.x28 - m.x68)**2 - 4*m.x97
                          >= 0)

m.c158 = Constraint(expr=(m.x25 - m.x69)**2 + (m.x26 - m.x70)**2 + (m.x27 - m.x71)**2 + (m.x28 - m.x72)**2 - 4*m.x97
                          >= 0)

m.c159 = Constraint(expr=(m.x25 - m.x73)**2 + (m.x26 - m.x74)**2 + (m.x27 - m.x75)**2 + (m.x28 - m.x76)**2 - 4*m.x97
                          >= 0)

m.c160 = Constraint(expr=(m.x25 - m.x77)**2 + (m.x26 - m.x78)**2 + (m.x27 - m.x79)**2 + (m.x28 - m.x80)**2 - 4*m.x97
                          >= 0)

m.c161 = Constraint(expr=(m.x25 - m.x81)**2 + (m.x26 - m.x82)**2 + (m.x27 - m.x83)**2 + (m.x28 - m.x84)**2 - 4*m.x97
                          >= 0)

m.c162 = Constraint(expr=(m.x25 - m.x85)**2 + (m.x26 - m.x86)**2 + (m.x27 - m.x87)**2 + (m.x28 - m.x88)**2 - 4*m.x97
                          >= 0)

m.c163 = Constraint(expr=(m.x25 - m.x89)**2 + (m.x26 - m.x90)**2 + (m.x27 - m.x91)**2 + (m.x28 - m.x92)**2 - 4*m.x97
                          >= 0)

m.c164 = Constraint(expr=(m.x25 - m.x93)**2 + (m.x26 - m.x94)**2 + (m.x27 - m.x95)**2 + (m.x28 - m.x96)**2 - 4*m.x97
                          >= 0)

m.c165 = Constraint(expr=(m.x29 - m.x33)**2 + (m.x30 - m.x34)**2 + (m.x31 - m.x35)**2 + (m.x32 - m.x36)**2 - 4*m.x97
                          >= 0)

m.c166 = Constraint(expr=(m.x29 - m.x37)**2 + (m.x30 - m.x38)**2 + (m.x31 - m.x39)**2 + (m.x32 - m.x40)**2 - 4*m.x97
                          >= 0)

m.c167 = Constraint(expr=(m.x29 - m.x41)**2 + (m.x30 - m.x42)**2 + (m.x31 - m.x43)**2 + (m.x32 - m.x44)**2 - 4*m.x97
                          >= 0)

m.c168 = Constraint(expr=(m.x29 - m.x45)**2 + (m.x30 - m.x46)**2 + (m.x31 - m.x47)**2 + (m.x32 - m.x48)**2 - 4*m.x97
                          >= 0)

m.c169 = Constraint(expr=(m.x29 - m.x49)**2 + (m.x30 - m.x50)**2 + (m.x31 - m.x51)**2 + (m.x32 - m.x52)**2 - 4*m.x97
                          >= 0)

m.c170 = Constraint(expr=(m.x29 - m.x53)**2 + (m.x30 - m.x54)**2 + (m.x31 - m.x55)**2 + (m.x32 - m.x56)**2 - 4*m.x97
                          >= 0)

m.c171 = Constraint(expr=(m.x29 - m.x57)**2 + (m.x30 - m.x58)**2 + (m.x31 - m.x59)**2 + (m.x32 - m.x60)**2 - 4*m.x97
                          >= 0)

m.c172 = Constraint(expr=(m.x29 - m.x61)**2 + (m.x30 - m.x62)**2 + (m.x31 - m.x63)**2 + (m.x32 - m.x64)**2 - 4*m.x97
                          >= 0)

m.c173 = Constraint(expr=(m.x29 - m.x65)**2 + (m.x30 - m.x66)**2 + (m.x31 - m.x67)**2 + (m.x32 - m.x68)**2 - 4*m.x97
                          >= 0)

m.c174 = Constraint(expr=(m.x29 - m.x69)**2 + (m.x30 - m.x70)**2 + (m.x31 - m.x71)**2 + (m.x32 - m.x72)**2 - 4*m.x97
                          >= 0)

m.c175 = Constraint(expr=(m.x29 - m.x73)**2 + (m.x30 - m.x74)**2 + (m.x31 - m.x75)**2 + (m.x32 - m.x76)**2 - 4*m.x97
                          >= 0)

m.c176 = Constraint(expr=(m.x29 - m.x77)**2 + (m.x30 - m.x78)**2 + (m.x31 - m.x79)**2 + (m.x32 - m.x80)**2 - 4*m.x97
                          >= 0)

m.c177 = Constraint(expr=(m.x29 - m.x81)**2 + (m.x30 - m.x82)**2 + (m.x31 - m.x83)**2 + (m.x32 - m.x84)**2 - 4*m.x97
                          >= 0)

m.c178 = Constraint(expr=(m.x29 - m.x85)**2 + (m.x30 - m.x86)**2 + (m.x31 - m.x87)**2 + (m.x32 - m.x88)**2 - 4*m.x97
                          >= 0)

m.c179 = Constraint(expr=(m.x29 - m.x89)**2 + (m.x30 - m.x90)**2 + (m.x31 - m.x91)**2 + (m.x32 - m.x92)**2 - 4*m.x97
                          >= 0)

m.c180 = Constraint(expr=(m.x29 - m.x93)**2 + (m.x30 - m.x94)**2 + (m.x31 - m.x95)**2 + (m.x32 - m.x96)**2 - 4*m.x97
                          >= 0)

m.c181 = Constraint(expr=(m.x33 - m.x37)**2 + (m.x34 - m.x38)**2 + (m.x35 - m.x39)**2 + (m.x36 - m.x40)**2 - 4*m.x97
                          >= 0)

m.c182 = Constraint(expr=(m.x33 - m.x41)**2 + (m.x34 - m.x42)**2 + (m.x35 - m.x43)**2 + (m.x36 - m.x44)**2 - 4*m.x97
                          >= 0)

m.c183 = Constraint(expr=(m.x33 - m.x45)**2 + (m.x34 - m.x46)**2 + (m.x35 - m.x47)**2 + (m.x36 - m.x48)**2 - 4*m.x97
                          >= 0)

m.c184 = Constraint(expr=(m.x33 - m.x49)**2 + (m.x34 - m.x50)**2 + (m.x35 - m.x51)**2 + (m.x36 - m.x52)**2 - 4*m.x97
                          >= 0)

m.c185 = Constraint(expr=(m.x33 - m.x53)**2 + (m.x34 - m.x54)**2 + (m.x35 - m.x55)**2 + (m.x36 - m.x56)**2 - 4*m.x97
                          >= 0)

m.c186 = Constraint(expr=(m.x33 - m.x57)**2 + (m.x34 - m.x58)**2 + (m.x35 - m.x59)**2 + (m.x36 - m.x60)**2 - 4*m.x97
                          >= 0)

m.c187 = Constraint(expr=(m.x33 - m.x61)**2 + (m.x34 - m.x62)**2 + (m.x35 - m.x63)**2 + (m.x36 - m.x64)**2 - 4*m.x97
                          >= 0)

m.c188 = Constraint(expr=(m.x33 - m.x65)**2 + (m.x34 - m.x66)**2 + (m.x35 - m.x67)**2 + (m.x36 - m.x68)**2 - 4*m.x97
                          >= 0)

m.c189 = Constraint(expr=(m.x33 - m.x69)**2 + (m.x34 - m.x70)**2 + (m.x35 - m.x71)**2 + (m.x36 - m.x72)**2 - 4*m.x97
                          >= 0)

m.c190 = Constraint(expr=(m.x33 - m.x73)**2 + (m.x34 - m.x74)**2 + (m.x35 - m.x75)**2 + (m.x36 - m.x76)**2 - 4*m.x97
                          >= 0)

m.c191 = Constraint(expr=(m.x33 - m.x77)**2 + (m.x34 - m.x78)**2 + (m.x35 - m.x79)**2 + (m.x36 - m.x80)**2 - 4*m.x97
                          >= 0)

m.c192 = Constraint(expr=(m.x33 - m.x81)**2 + (m.x34 - m.x82)**2 + (m.x35 - m.x83)**2 + (m.x36 - m.x84)**2 - 4*m.x97
                          >= 0)

m.c193 = Constraint(expr=(m.x33 - m.x85)**2 + (m.x34 - m.x86)**2 + (m.x35 - m.x87)**2 + (m.x36 - m.x88)**2 - 4*m.x97
                          >= 0)

m.c194 = Constraint(expr=(m.x33 - m.x89)**2 + (m.x34 - m.x90)**2 + (m.x35 - m.x91)**2 + (m.x36 - m.x92)**2 - 4*m.x97
                          >= 0)

m.c195 = Constraint(expr=(m.x33 - m.x93)**2 + (m.x34 - m.x94)**2 + (m.x35 - m.x95)**2 + (m.x36 - m.x96)**2 - 4*m.x97
                          >= 0)

m.c196 = Constraint(expr=(m.x37 - m.x41)**2 + (m.x38 - m.x42)**2 + (m.x39 - m.x43)**2 + (m.x40 - m.x44)**2 - 4*m.x97
                          >= 0)

m.c197 = Constraint(expr=(m.x37 - m.x45)**2 + (m.x38 - m.x46)**2 + (m.x39 - m.x47)**2 + (m.x40 - m.x48)**2 - 4*m.x97
                          >= 0)

m.c198 = Constraint(expr=(m.x37 - m.x49)**2 + (m.x38 - m.x50)**2 + (m.x39 - m.x51)**2 + (m.x40 - m.x52)**2 - 4*m.x97
                          >= 0)

m.c199 = Constraint(expr=(m.x37 - m.x53)**2 + (m.x38 - m.x54)**2 + (m.x39 - m.x55)**2 + (m.x40 - m.x56)**2 - 4*m.x97
                          >= 0)

m.c200 = Constraint(expr=(m.x37 - m.x57)**2 + (m.x38 - m.x58)**2 + (m.x39 - m.x59)**2 + (m.x40 - m.x60)**2 - 4*m.x97
                          >= 0)

m.c201 = Constraint(expr=(m.x37 - m.x61)**2 + (m.x38 - m.x62)**2 + (m.x39 - m.x63)**2 + (m.x40 - m.x64)**2 - 4*m.x97
                          >= 0)

m.c202 = Constraint(expr=(m.x37 - m.x65)**2 + (m.x38 - m.x66)**2 + (m.x39 - m.x67)**2 + (m.x40 - m.x68)**2 - 4*m.x97
                          >= 0)

m.c203 = Constraint(expr=(m.x37 - m.x69)**2 + (m.x38 - m.x70)**2 + (m.x39 - m.x71)**2 + (m.x40 - m.x72)**2 - 4*m.x97
                          >= 0)

m.c204 = Constraint(expr=(m.x37 - m.x73)**2 + (m.x38 - m.x74)**2 + (m.x39 - m.x75)**2 + (m.x40 - m.x76)**2 - 4*m.x97
                          >= 0)

m.c205 = Constraint(expr=(m.x37 - m.x77)**2 + (m.x38 - m.x78)**2 + (m.x39 - m.x79)**2 + (m.x40 - m.x80)**2 - 4*m.x97
                          >= 0)

m.c206 = Constraint(expr=(m.x37 - m.x81)**2 + (m.x38 - m.x82)**2 + (m.x39 - m.x83)**2 + (m.x40 - m.x84)**2 - 4*m.x97
                          >= 0)

m.c207 = Constraint(expr=(m.x37 - m.x85)**2 + (m.x38 - m.x86)**2 + (m.x39 - m.x87)**2 + (m.x40 - m.x88)**2 - 4*m.x97
                          >= 0)

m.c208 = Constraint(expr=(m.x37 - m.x89)**2 + (m.x38 - m.x90)**2 + (m.x39 - m.x91)**2 + (m.x40 - m.x92)**2 - 4*m.x97
                          >= 0)

m.c209 = Constraint(expr=(m.x37 - m.x93)**2 + (m.x38 - m.x94)**2 + (m.x39 - m.x95)**2 + (m.x40 - m.x96)**2 - 4*m.x97
                          >= 0)

m.c210 = Constraint(expr=(m.x41 - m.x45)**2 + (m.x42 - m.x46)**2 + (m.x43 - m.x47)**2 + (m.x44 - m.x48)**2 - 4*m.x97
                          >= 0)

m.c211 = Constraint(expr=(m.x41 - m.x49)**2 + (m.x42 - m.x50)**2 + (m.x43 - m.x51)**2 + (m.x44 - m.x52)**2 - 4*m.x97
                          >= 0)

m.c212 = Constraint(expr=(m.x41 - m.x53)**2 + (m.x42 - m.x54)**2 + (m.x43 - m.x55)**2 + (m.x44 - m.x56)**2 - 4*m.x97
                          >= 0)

m.c213 = Constraint(expr=(m.x41 - m.x57)**2 + (m.x42 - m.x58)**2 + (m.x43 - m.x59)**2 + (m.x44 - m.x60)**2 - 4*m.x97
                          >= 0)

m.c214 = Constraint(expr=(m.x41 - m.x61)**2 + (m.x42 - m.x62)**2 + (m.x43 - m.x63)**2 + (m.x44 - m.x64)**2 - 4*m.x97
                          >= 0)

m.c215 = Constraint(expr=(m.x41 - m.x65)**2 + (m.x42 - m.x66)**2 + (m.x43 - m.x67)**2 + (m.x44 - m.x68)**2 - 4*m.x97
                          >= 0)

m.c216 = Constraint(expr=(m.x41 - m.x69)**2 + (m.x42 - m.x70)**2 + (m.x43 - m.x71)**2 + (m.x44 - m.x72)**2 - 4*m.x97
                          >= 0)

m.c217 = Constraint(expr=(m.x41 - m.x73)**2 + (m.x42 - m.x74)**2 + (m.x43 - m.x75)**2 + (m.x44 - m.x76)**2 - 4*m.x97
                          >= 0)

m.c218 = Constraint(expr=(m.x41 - m.x77)**2 + (m.x42 - m.x78)**2 + (m.x43 - m.x79)**2 + (m.x44 - m.x80)**2 - 4*m.x97
                          >= 0)

m.c219 = Constraint(expr=(m.x41 - m.x81)**2 + (m.x42 - m.x82)**2 + (m.x43 - m.x83)**2 + (m.x44 - m.x84)**2 - 4*m.x97
                          >= 0)

m.c220 = Constraint(expr=(m.x41 - m.x85)**2 + (m.x42 - m.x86)**2 + (m.x43 - m.x87)**2 + (m.x44 - m.x88)**2 - 4*m.x97
                          >= 0)

m.c221 = Constraint(expr=(m.x41 - m.x89)**2 + (m.x42 - m.x90)**2 + (m.x43 - m.x91)**2 + (m.x44 - m.x92)**2 - 4*m.x97
                          >= 0)

m.c222 = Constraint(expr=(m.x41 - m.x93)**2 + (m.x42 - m.x94)**2 + (m.x43 - m.x95)**2 + (m.x44 - m.x96)**2 - 4*m.x97
                          >= 0)

m.c223 = Constraint(expr=(m.x45 - m.x49)**2 + (m.x46 - m.x50)**2 + (m.x47 - m.x51)**2 + (m.x48 - m.x52)**2 - 4*m.x97
                          >= 0)

m.c224 = Constraint(expr=(m.x45 - m.x53)**2 + (m.x46 - m.x54)**2 + (m.x47 - m.x55)**2 + (m.x48 - m.x56)**2 - 4*m.x97
                          >= 0)

m.c225 = Constraint(expr=(m.x45 - m.x57)**2 + (m.x46 - m.x58)**2 + (m.x47 - m.x59)**2 + (m.x48 - m.x60)**2 - 4*m.x97
                          >= 0)

m.c226 = Constraint(expr=(m.x45 - m.x61)**2 + (m.x46 - m.x62)**2 + (m.x47 - m.x63)**2 + (m.x48 - m.x64)**2 - 4*m.x97
                          >= 0)

m.c227 = Constraint(expr=(m.x45 - m.x65)**2 + (m.x46 - m.x66)**2 + (m.x47 - m.x67)**2 + (m.x48 - m.x68)**2 - 4*m.x97
                          >= 0)

m.c228 = Constraint(expr=(m.x45 - m.x69)**2 + (m.x46 - m.x70)**2 + (m.x47 - m.x71)**2 + (m.x48 - m.x72)**2 - 4*m.x97
                          >= 0)

m.c229 = Constraint(expr=(m.x45 - m.x73)**2 + (m.x46 - m.x74)**2 + (m.x47 - m.x75)**2 + (m.x48 - m.x76)**2 - 4*m.x97
                          >= 0)

m.c230 = Constraint(expr=(m.x45 - m.x77)**2 + (m.x46 - m.x78)**2 + (m.x47 - m.x79)**2 + (m.x48 - m.x80)**2 - 4*m.x97
                          >= 0)

m.c231 = Constraint(expr=(m.x45 - m.x81)**2 + (m.x46 - m.x82)**2 + (m.x47 - m.x83)**2 + (m.x48 - m.x84)**2 - 4*m.x97
                          >= 0)

m.c232 = Constraint(expr=(m.x45 - m.x85)**2 + (m.x46 - m.x86)**2 + (m.x47 - m.x87)**2 + (m.x48 - m.x88)**2 - 4*m.x97
                          >= 0)

m.c233 = Constraint(expr=(m.x45 - m.x89)**2 + (m.x46 - m.x90)**2 + (m.x47 - m.x91)**2 + (m.x48 - m.x92)**2 - 4*m.x97
                          >= 0)

m.c234 = Constraint(expr=(m.x45 - m.x93)**2 + (m.x46 - m.x94)**2 + (m.x47 - m.x95)**2 + (m.x48 - m.x96)**2 - 4*m.x97
                          >= 0)

m.c235 = Constraint(expr=(m.x49 - m.x53)**2 + (m.x50 - m.x54)**2 + (m.x51 - m.x55)**2 + (m.x52 - m.x56)**2 - 4*m.x97
                          >= 0)

m.c236 = Constraint(expr=(m.x49 - m.x57)**2 + (m.x50 - m.x58)**2 + (m.x51 - m.x59)**2 + (m.x52 - m.x60)**2 - 4*m.x97
                          >= 0)

m.c237 = Constraint(expr=(m.x49 - m.x61)**2 + (m.x50 - m.x62)**2 + (m.x51 - m.x63)**2 + (m.x52 - m.x64)**2 - 4*m.x97
                          >= 0)

m.c238 = Constraint(expr=(m.x49 - m.x65)**2 + (m.x50 - m.x66)**2 + (m.x51 - m.x67)**2 + (m.x52 - m.x68)**2 - 4*m.x97
                          >= 0)

m.c239 = Constraint(expr=(m.x49 - m.x69)**2 + (m.x50 - m.x70)**2 + (m.x51 - m.x71)**2 + (m.x52 - m.x72)**2 - 4*m.x97
                          >= 0)

m.c240 = Constraint(expr=(m.x49 - m.x73)**2 + (m.x50 - m.x74)**2 + (m.x51 - m.x75)**2 + (m.x52 - m.x76)**2 - 4*m.x97
                          >= 0)

m.c241 = Constraint(expr=(m.x49 - m.x77)**2 + (m.x50 - m.x78)**2 + (m.x51 - m.x79)**2 + (m.x52 - m.x80)**2 - 4*m.x97
                          >= 0)

m.c242 = Constraint(expr=(m.x49 - m.x81)**2 + (m.x50 - m.x82)**2 + (m.x51 - m.x83)**2 + (m.x52 - m.x84)**2 - 4*m.x97
                          >= 0)

m.c243 = Constraint(expr=(m.x49 - m.x85)**2 + (m.x50 - m.x86)**2 + (m.x51 - m.x87)**2 + (m.x52 - m.x88)**2 - 4*m.x97
                          >= 0)

m.c244 = Constraint(expr=(m.x49 - m.x89)**2 + (m.x50 - m.x90)**2 + (m.x51 - m.x91)**2 + (m.x52 - m.x92)**2 - 4*m.x97
                          >= 0)

m.c245 = Constraint(expr=(m.x49 - m.x93)**2 + (m.x50 - m.x94)**2 + (m.x51 - m.x95)**2 + (m.x52 - m.x96)**2 - 4*m.x97
                          >= 0)

m.c246 = Constraint(expr=(m.x53 - m.x57)**2 + (m.x54 - m.x58)**2 + (m.x55 - m.x59)**2 + (m.x56 - m.x60)**2 - 4*m.x97
                          >= 0)

m.c247 = Constraint(expr=(m.x53 - m.x61)**2 + (m.x54 - m.x62)**2 + (m.x55 - m.x63)**2 + (m.x56 - m.x64)**2 - 4*m.x97
                          >= 0)

m.c248 = Constraint(expr=(m.x53 - m.x65)**2 + (m.x54 - m.x66)**2 + (m.x55 - m.x67)**2 + (m.x56 - m.x68)**2 - 4*m.x97
                          >= 0)

m.c249 = Constraint(expr=(m.x53 - m.x69)**2 + (m.x54 - m.x70)**2 + (m.x55 - m.x71)**2 + (m.x56 - m.x72)**2 - 4*m.x97
                          >= 0)

m.c250 = Constraint(expr=(m.x53 - m.x73)**2 + (m.x54 - m.x74)**2 + (m.x55 - m.x75)**2 + (m.x56 - m.x76)**2 - 4*m.x97
                          >= 0)

m.c251 = Constraint(expr=(m.x53 - m.x77)**2 + (m.x54 - m.x78)**2 + (m.x55 - m.x79)**2 + (m.x56 - m.x80)**2 - 4*m.x97
                          >= 0)

m.c252 = Constraint(expr=(m.x53 - m.x81)**2 + (m.x54 - m.x82)**2 + (m.x55 - m.x83)**2 + (m.x56 - m.x84)**2 - 4*m.x97
                          >= 0)

m.c253 = Constraint(expr=(m.x53 - m.x85)**2 + (m.x54 - m.x86)**2 + (m.x55 - m.x87)**2 + (m.x56 - m.x88)**2 - 4*m.x97
                          >= 0)

m.c254 = Constraint(expr=(m.x53 - m.x89)**2 + (m.x54 - m.x90)**2 + (m.x55 - m.x91)**2 + (m.x56 - m.x92)**2 - 4*m.x97
                          >= 0)

m.c255 = Constraint(expr=(m.x53 - m.x93)**2 + (m.x54 - m.x94)**2 + (m.x55 - m.x95)**2 + (m.x56 - m.x96)**2 - 4*m.x97
                          >= 0)

m.c256 = Constraint(expr=(m.x57 - m.x61)**2 + (m.x58 - m.x62)**2 + (m.x59 - m.x63)**2 + (m.x60 - m.x64)**2 - 4*m.x97
                          >= 0)

m.c257 = Constraint(expr=(m.x57 - m.x65)**2 + (m.x58 - m.x66)**2 + (m.x59 - m.x67)**2 + (m.x60 - m.x68)**2 - 4*m.x97
                          >= 0)

m.c258 = Constraint(expr=(m.x57 - m.x69)**2 + (m.x58 - m.x70)**2 + (m.x59 - m.x71)**2 + (m.x60 - m.x72)**2 - 4*m.x97
                          >= 0)

m.c259 = Constraint(expr=(m.x57 - m.x73)**2 + (m.x58 - m.x74)**2 + (m.x59 - m.x75)**2 + (m.x60 - m.x76)**2 - 4*m.x97
                          >= 0)

m.c260 = Constraint(expr=(m.x57 - m.x77)**2 + (m.x58 - m.x78)**2 + (m.x59 - m.x79)**2 + (m.x60 - m.x80)**2 - 4*m.x97
                          >= 0)

m.c261 = Constraint(expr=(m.x57 - m.x81)**2 + (m.x58 - m.x82)**2 + (m.x59 - m.x83)**2 + (m.x60 - m.x84)**2 - 4*m.x97
                          >= 0)

m.c262 = Constraint(expr=(m.x57 - m.x85)**2 + (m.x58 - m.x86)**2 + (m.x59 - m.x87)**2 + (m.x60 - m.x88)**2 - 4*m.x97
                          >= 0)

m.c263 = Constraint(expr=(m.x57 - m.x89)**2 + (m.x58 - m.x90)**2 + (m.x59 - m.x91)**2 + (m.x60 - m.x92)**2 - 4*m.x97
                          >= 0)

m.c264 = Constraint(expr=(m.x57 - m.x93)**2 + (m.x58 - m.x94)**2 + (m.x59 - m.x95)**2 + (m.x60 - m.x96)**2 - 4*m.x97
                          >= 0)

m.c265 = Constraint(expr=(m.x61 - m.x65)**2 + (m.x62 - m.x66)**2 + (m.x63 - m.x67)**2 + (m.x64 - m.x68)**2 - 4*m.x97
                          >= 0)

m.c266 = Constraint(expr=(m.x61 - m.x69)**2 + (m.x62 - m.x70)**2 + (m.x63 - m.x71)**2 + (m.x64 - m.x72)**2 - 4*m.x97
                          >= 0)

m.c267 = Constraint(expr=(m.x61 - m.x73)**2 + (m.x62 - m.x74)**2 + (m.x63 - m.x75)**2 + (m.x64 - m.x76)**2 - 4*m.x97
                          >= 0)

m.c268 = Constraint(expr=(m.x61 - m.x77)**2 + (m.x62 - m.x78)**2 + (m.x63 - m.x79)**2 + (m.x64 - m.x80)**2 - 4*m.x97
                          >= 0)

m.c269 = Constraint(expr=(m.x61 - m.x81)**2 + (m.x62 - m.x82)**2 + (m.x63 - m.x83)**2 + (m.x64 - m.x84)**2 - 4*m.x97
                          >= 0)

m.c270 = Constraint(expr=(m.x61 - m.x85)**2 + (m.x62 - m.x86)**2 + (m.x63 - m.x87)**2 + (m.x64 - m.x88)**2 - 4*m.x97
                          >= 0)

m.c271 = Constraint(expr=(m.x61 - m.x89)**2 + (m.x62 - m.x90)**2 + (m.x63 - m.x91)**2 + (m.x64 - m.x92)**2 - 4*m.x97
                          >= 0)

m.c272 = Constraint(expr=(m.x61 - m.x93)**2 + (m.x62 - m.x94)**2 + (m.x63 - m.x95)**2 + (m.x64 - m.x96)**2 - 4*m.x97
                          >= 0)

m.c273 = Constraint(expr=(m.x65 - m.x69)**2 + (m.x66 - m.x70)**2 + (m.x67 - m.x71)**2 + (m.x68 - m.x72)**2 - 4*m.x97
                          >= 0)

m.c274 = Constraint(expr=(m.x65 - m.x73)**2 + (m.x66 - m.x74)**2 + (m.x67 - m.x75)**2 + (m.x68 - m.x76)**2 - 4*m.x97
                          >= 0)

m.c275 = Constraint(expr=(m.x65 - m.x77)**2 + (m.x66 - m.x78)**2 + (m.x67 - m.x79)**2 + (m.x68 - m.x80)**2 - 4*m.x97
                          >= 0)

m.c276 = Constraint(expr=(m.x65 - m.x81)**2 + (m.x66 - m.x82)**2 + (m.x67 - m.x83)**2 + (m.x68 - m.x84)**2 - 4*m.x97
                          >= 0)

m.c277 = Constraint(expr=(m.x65 - m.x85)**2 + (m.x66 - m.x86)**2 + (m.x67 - m.x87)**2 + (m.x68 - m.x88)**2 - 4*m.x97
                          >= 0)

m.c278 = Constraint(expr=(m.x65 - m.x89)**2 + (m.x66 - m.x90)**2 + (m.x67 - m.x91)**2 + (m.x68 - m.x92)**2 - 4*m.x97
                          >= 0)

m.c279 = Constraint(expr=(m.x65 - m.x93)**2 + (m.x66 - m.x94)**2 + (m.x67 - m.x95)**2 + (m.x68 - m.x96)**2 - 4*m.x97
                          >= 0)

m.c280 = Constraint(expr=(m.x69 - m.x73)**2 + (m.x70 - m.x74)**2 + (m.x71 - m.x75)**2 + (m.x72 - m.x76)**2 - 4*m.x97
                          >= 0)

m.c281 = Constraint(expr=(m.x69 - m.x77)**2 + (m.x70 - m.x78)**2 + (m.x71 - m.x79)**2 + (m.x72 - m.x80)**2 - 4*m.x97
                          >= 0)

m.c282 = Constraint(expr=(m.x69 - m.x81)**2 + (m.x70 - m.x82)**2 + (m.x71 - m.x83)**2 + (m.x72 - m.x84)**2 - 4*m.x97
                          >= 0)

m.c283 = Constraint(expr=(m.x69 - m.x85)**2 + (m.x70 - m.x86)**2 + (m.x71 - m.x87)**2 + (m.x72 - m.x88)**2 - 4*m.x97
                          >= 0)

m.c284 = Constraint(expr=(m.x69 - m.x89)**2 + (m.x70 - m.x90)**2 + (m.x71 - m.x91)**2 + (m.x72 - m.x92)**2 - 4*m.x97
                          >= 0)

m.c285 = Constraint(expr=(m.x69 - m.x93)**2 + (m.x70 - m.x94)**2 + (m.x71 - m.x95)**2 + (m.x72 - m.x96)**2 - 4*m.x97
                          >= 0)

m.c286 = Constraint(expr=(m.x73 - m.x77)**2 + (m.x74 - m.x78)**2 + (m.x75 - m.x79)**2 + (m.x76 - m.x80)**2 - 4*m.x97
                          >= 0)

m.c287 = Constraint(expr=(m.x73 - m.x81)**2 + (m.x74 - m.x82)**2 + (m.x75 - m.x83)**2 + (m.x76 - m.x84)**2 - 4*m.x97
                          >= 0)

m.c288 = Constraint(expr=(m.x73 - m.x85)**2 + (m.x74 - m.x86)**2 + (m.x75 - m.x87)**2 + (m.x76 - m.x88)**2 - 4*m.x97
                          >= 0)

m.c289 = Constraint(expr=(m.x73 - m.x89)**2 + (m.x74 - m.x90)**2 + (m.x75 - m.x91)**2 + (m.x76 - m.x92)**2 - 4*m.x97
                          >= 0)

m.c290 = Constraint(expr=(m.x73 - m.x93)**2 + (m.x74 - m.x94)**2 + (m.x75 - m.x95)**2 + (m.x76 - m.x96)**2 - 4*m.x97
                          >= 0)

m.c291 = Constraint(expr=(m.x77 - m.x81)**2 + (m.x78 - m.x82)**2 + (m.x79 - m.x83)**2 + (m.x80 - m.x84)**2 - 4*m.x97
                          >= 0)

m.c292 = Constraint(expr=(m.x77 - m.x85)**2 + (m.x78 - m.x86)**2 + (m.x79 - m.x87)**2 + (m.x80 - m.x88)**2 - 4*m.x97
                          >= 0)

m.c293 = Constraint(expr=(m.x77 - m.x89)**2 + (m.x78 - m.x90)**2 + (m.x79 - m.x91)**2 + (m.x80 - m.x92)**2 - 4*m.x97
                          >= 0)

m.c294 = Constraint(expr=(m.x77 - m.x93)**2 + (m.x78 - m.x94)**2 + (m.x79 - m.x95)**2 + (m.x80 - m.x96)**2 - 4*m.x97
                          >= 0)

m.c295 = Constraint(expr=(m.x81 - m.x85)**2 + (m.x82 - m.x86)**2 + (m.x83 - m.x87)**2 + (m.x84 - m.x88)**2 - 4*m.x97
                          >= 0)

m.c296 = Constraint(expr=(m.x81 - m.x89)**2 + (m.x82 - m.x90)**2 + (m.x83 - m.x91)**2 + (m.x84 - m.x92)**2 - 4*m.x97
                          >= 0)

m.c297 = Constraint(expr=(m.x81 - m.x93)**2 + (m.x82 - m.x94)**2 + (m.x83 - m.x95)**2 + (m.x84 - m.x96)**2 - 4*m.x97
                          >= 0)

m.c298 = Constraint(expr=(m.x85 - m.x89)**2 + (m.x86 - m.x90)**2 + (m.x87 - m.x91)**2 + (m.x88 - m.x92)**2 - 4*m.x97
                          >= 0)

m.c299 = Constraint(expr=(m.x85 - m.x93)**2 + (m.x86 - m.x94)**2 + (m.x87 - m.x95)**2 + (m.x88 - m.x96)**2 - 4*m.x97
                          >= 0)

m.c300 = Constraint(expr=(m.x89 - m.x93)**2 + (m.x90 - m.x94)**2 + (m.x91 - m.x95)**2 + (m.x92 - m.x96)**2 - 4*m.x97
                          >= 0)
