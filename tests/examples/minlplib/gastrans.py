#  MINLP written by GAMS Convert at 04/21/18 13:52:21
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        150       63       45       42        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        107       86       21        0        0        0        0        0
#  FX      5        5        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        419      374       45        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,None),initialize=5.45594117499038)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=3.49005882500962)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=8.46373378118172)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=8.88226621881828)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=13.428)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=4.8)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=0.766)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=-4.49)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=8.938)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=22.012)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=18.1380867287228)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=3.87391327127718)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=12.1798336524591)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=3.44716634754093)
m.x16 = Var(within=Reals,bounds=(None,None),initialize=13.486)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=11.366)
m.x18 = Var(within=Reals,bounds=(None,None),initialize=12.566)
m.x19 = Var(within=Reals,bounds=(None,None),initialize=22.464)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=15.616)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=2.141)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=2.141)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=2.141)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=1.919)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(None,None),initialize=-75.3049979497412)
m.x28 = Var(within=Reals,bounds=(None,None),initialize=-68.3754533453309)
m.x29 = Var(within=Reals,bounds=(None,None),initialize=6.90403568495296)
m.x30 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(None,None),initialize=10.0403890555214)
m.x33 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(None,None),initialize=19.0338757369553)
m.x35 = Var(within=Reals,bounds=(None,None),initialize=6.17166731394037)
m.x36 = Var(within=Reals,bounds=(None,None),initialize=8.7272279190673)
m.x37 = Var(within=Reals,bounds=(None,None),initialize=1.6114349200345)
m.x38 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=-14.7474499350948)
m.x43 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(None,None),initialize=1.46180871006652)
m.x45 = Var(within=Reals,bounds=(None,None),initialize=-4.68001962388774)
m.b46 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b47 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b48 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b49 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b50 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b51 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b52 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b53 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b54 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b55 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b56 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b57 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b58 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b59 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b60 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b61 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b62 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b63 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b64 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b65 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b66 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,1.2),initialize=0)
m.x68 = Var(within=Reals,bounds=(None,-4.034),initialize=-4.034)
m.x69 = Var(within=Reals,bounds=(None,-0.222),initialize=-0.222)
m.x70 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x71 = Var(within=Reals,bounds=(None,-15.616),initialize=-15.616)
m.x72 = Var(within=Reals,bounds=(None,-3.918),initialize=-3.918)
m.x73 = Var(within=Reals,bounds=(0,8.4),initialize=0)
m.x74 = Var(within=Reals,bounds=(None,-5.256),initialize=-5.256)
m.x75 = Var(within=Reals,bounds=(None,-6.385),initialize=-6.385)
m.x76 = Var(within=Reals,bounds=(0,4.8),initialize=0)
m.x77 = Var(within=Reals,bounds=(None,-6.848),initialize=-6.848)
m.x78 = Var(within=Reals,bounds=(None,-2.12),initialize=-2.12)
m.x79 = Var(within=Reals,bounds=(None,-1.919),initialize=-1.919)
m.x80 = Var(within=Reals,bounds=(0,0.96),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x82 = Var(within=Reals,bounds=(20.344,22.012),initialize=20.344)
m.x83 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x85 = Var(within=Reals,bounds=(8.87,11.594),initialize=8.946)
m.x86 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,4382.44),initialize=0)
m.x88 = Var(within=Reals,bounds=(900,6400),initialize=900)
m.x89 = Var(within=Reals,bounds=(0,4382.44),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,4382.44),initialize=0)
m.x91 = Var(within=Reals,bounds=(2500,4382.44),initialize=2500)
m.x92 = Var(within=Reals,bounds=(900,6400),initialize=900)
m.x93 = Var(within=Reals,bounds=(0,5929),initialize=0)
m.x94 = Var(within=Reals,bounds=(900,6400),initialize=900)
m.x95 = Var(within=Reals,bounds=(900,4382.44),initialize=900)
m.x96 = Var(within=Reals,bounds=(0,5929),initialize=900)
m.x97 = Var(within=Reals,bounds=(0,4382.44),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,4382.44),initialize=0)
m.x99 = Var(within=Reals,bounds=(625,4382.44),initialize=625)
m.x100 = Var(within=Reals,bounds=(0,4382.44),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,3969),initialize=0)
m.x102 = Var(within=Reals,bounds=(2500,4382.44),initialize=2500)
m.x103 = Var(within=Reals,bounds=(0,4382.44),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,4382.44),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,5929),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,6400),initialize=0)

m.obj = Objective(expr=   2.28*m.x73 + 2.28*m.x76 + 1.68*m.x80 + 1.68*m.x82 + 2.28*m.x85, sense=minimize)

m.c2 = Constraint(expr= - m.x17 + m.x18 - m.x67 == 0)

m.c3 = Constraint(expr= - m.x6 + m.x7 - m.x68 == 0)

m.c4 = Constraint(expr= - m.x23 + m.x24 - m.x69 == 0)

m.c5 = Constraint(expr= - m.x10 - m.x11 + m.x12 + m.x13 - m.x70 == 0)

m.c6 = Constraint(expr= - m.x20 - m.x71 == 0)

m.c7 = Constraint(expr= - m.x3 - m.x4 + m.x5 - m.x72 == 0)

m.c8 = Constraint(expr= - m.x1 - m.x2 + m.x3 + m.x4 - m.x73 == 0)

m.c9 = Constraint(expr= - m.x7 + m.x8 - m.x74 == 0)

m.c10 = Constraint(expr= - m.x12 - m.x13 + m.x14 + m.x15 - m.x75 == 0)

m.c11 = Constraint(expr=   m.x6 - m.x76 == 0)

m.c12 = Constraint(expr= - m.x19 + m.x20 - m.x77 == 0)

m.c13 = Constraint(expr= - m.x16 + m.x17 - m.x78 == 0)

m.c14 = Constraint(expr= - m.x24 - m.x79 == 0)

m.c15 = Constraint(expr= - m.x9 - m.x18 + m.x19 - m.x80 == 0)

m.c16 = Constraint(expr= - m.x22 + m.x23 - m.x81 == 0)

m.c17 = Constraint(expr=   m.x10 + m.x11 - m.x82 == 0)

m.c18 = Constraint(expr= - m.x21 + m.x22 - m.x83 == 0)

m.c19 = Constraint(expr= - m.x14 - m.x15 + m.x16 + m.x21 - m.x84 == 0)

m.c20 = Constraint(expr=   m.x1 + m.x2 - m.x85 == 0)

m.c21 = Constraint(expr= - m.x5 - m.x8 + m.x9 - m.x86 == 0)

m.c22 = Constraint(expr=m.x1**2*m.x25 + 8.99076279639865*m.x93 - 8.99076279639865*m.x105 == 0)

m.c23 = Constraint(expr=m.x2**2*m.x26 + 8.99076279639865*m.x93 - 8.99076279639865*m.x105 == 0)

m.c24 = Constraint(expr=m.x3**2*m.x27 + 5.99384186426577*m.x92 - 5.99384186426577*m.x93 == 0)

m.c25 = Constraint(expr=m.x4**2*m.x28 + 5.99384186426577*m.x92 - 5.99384186426577*m.x93 == 0)

m.c26 = Constraint(expr=m.x5**2*m.x29 - 1.38319427636902*m.x92 + 1.38319427636902*m.x106 == 0)

m.c27 = Constraint(expr=m.x6**2*m.x30 + 0.0993769948466698*m.x88 - 0.0993769948466698*m.x96 == 0)

m.c28 = Constraint(expr=m.x7**2*m.x31 - 0.147352095807131*m.x88 + 0.147352095807131*m.x94 == 0)

m.c29 = Constraint(expr=m.x8**2*m.x32 - 0.224905830442463*m.x94 + 0.224905830442463*m.x106 == 0)

m.c30 = Constraint(expr=m.x9**2*m.x33 + 0.653873657919902*m.x100 - 0.653873657919902*m.x106 == 0)

m.c31 = Constraint(expr=m.x12**2*m.x34 - 1.79815255927973*m.x90 + 1.79815255927973*m.x95 == 0)

m.c32 = Constraint(expr=m.x13**2*m.x35 - 0.0265962529480588*m.x90 + 0.0265962529480588*m.x95 == 0)

m.c33 = Constraint(expr=m.x14**2*m.x36 - 1.43852204742378*m.x95 + 1.43852204742378*m.x104 == 0)

m.c34 = Constraint(expr=m.x15**2*m.x37 - 0.021277002358447*m.x95 + 0.021277002358447*m.x104 == 0)

m.c35 = Constraint(expr=m.x16**2*m.x38 + 0.856263123466538*m.x98 - 0.856263123466538*m.x104 == 0)

m.c36 = Constraint(expr=m.x17**2*m.x39 + 0.899076279639865*m.x87 - 0.899076279639865*m.x98 == 0)

m.c37 = Constraint(expr=m.x18**2*m.x40 - 7.19261023711892*m.x87 + 7.19261023711892*m.x100 == 0)

m.c38 = Constraint(expr=m.x19**2*m.x41 + 3.59630511855946*m.x97 - 3.59630511855946*m.x100 == 0)

m.c39 = Constraint(expr=m.x20**2*m.x42 + 1.43852204742378*m.x91 - 1.43852204742378*m.x97 == 0)

m.c40 = Constraint(expr=m.x21**2*m.x43 + 0.0509935163731392*m.x103 - 0.0509935163731392*m.x104 == 0)

m.c41 = Constraint(expr=m.x23**2*m.x44 + 0.0016882734118691*m.x89 - 0.0016882734118691*m.x101 == 0)

m.c42 = Constraint(expr=m.x24**2*m.x45 - 0.0275751323938619*m.x89 + 0.0275751323938619*m.x99 == 0)

m.c43 = Constraint(expr=-m.x10**2 + 7.19261023711892*m.x90 - 7.19261023711892*m.x102 >= 0)

m.c44 = Constraint(expr=-m.x11**2 + 0.106385011792235*m.x90 - 0.106385011792235*m.x102 >= 0)

m.c45 = Constraint(expr=-m.x22**2 + 0.00636349209089121*m.x101 - 0.00636349209089121*m.x103 >= 0)

m.c46 = Constraint(expr=   m.x25 - 2*m.b46 == -1)

m.c47 = Constraint(expr=   m.x26 - 2*m.b47 == -1)

m.c48 = Constraint(expr=   m.x27 - 2*m.b48 == -1)

m.c49 = Constraint(expr=   m.x28 - 2*m.b49 == -1)

m.c50 = Constraint(expr=   m.x29 - 2*m.b50 == -1)

m.c51 = Constraint(expr=   m.x30 - 2*m.b51 == -1)

m.c52 = Constraint(expr=   m.x31 - 2*m.b52 == -1)

m.c53 = Constraint(expr=   m.x32 - 2*m.b53 == -1)

m.c54 = Constraint(expr=   m.x33 - 2*m.b54 == -1)

m.c55 = Constraint(expr=   m.x34 - 2*m.b55 == -1)

m.c56 = Constraint(expr=   m.x35 - 2*m.b56 == -1)

m.c57 = Constraint(expr=   m.x36 - 2*m.b57 == -1)

m.c58 = Constraint(expr=   m.x37 - 2*m.b58 == -1)

m.c59 = Constraint(expr=   m.x38 - 2*m.b59 == -1)

m.c60 = Constraint(expr=   m.x39 - 2*m.b60 == -1)

m.c61 = Constraint(expr=   m.x40 - 2*m.b61 == -1)

m.c62 = Constraint(expr=   m.x41 - 2*m.b62 == -1)

m.c63 = Constraint(expr=   m.x42 - 2*m.b63 == -1)

m.c64 = Constraint(expr=   m.x43 - 2*m.b64 == -1)

m.c65 = Constraint(expr=   m.x44 - 2*m.b65 == -1)

m.c66 = Constraint(expr=   m.x45 - 2*m.b66 == -1)

m.c67 = Constraint(expr= - 5929*m.b46 - m.x93 + m.x105 >= -5929)

m.c68 = Constraint(expr= - 5929*m.b47 - m.x93 + m.x105 >= -5929)

m.c69 = Constraint(expr= - 6400*m.b48 - m.x92 + m.x93 >= -6400)

m.c70 = Constraint(expr= - 6400*m.b49 - m.x92 + m.x93 >= -6400)

m.c71 = Constraint(expr= - 5500*m.b50 + m.x92 - m.x106 >= -5500)

m.c72 = Constraint(expr= - 6400*m.b51 - m.x88 + m.x96 >= -6400)

m.c73 = Constraint(expr= - 5500*m.b52 + m.x88 - m.x94 >= -5500)

m.c74 = Constraint(expr= - 5500*m.b53 + m.x94 - m.x106 >= -5500)

m.c75 = Constraint(expr= - 4382.44*m.b54 - m.x100 + m.x106 >= -4382.44)

m.c76 = Constraint(expr= - 4382.44*m.b55 + m.x90 - m.x95 >= -4382.44)

m.c77 = Constraint(expr= - 4382.44*m.b56 + m.x90 - m.x95 >= -4382.44)

m.c78 = Constraint(expr= - 3482.44*m.b57 + m.x95 - m.x104 >= -3482.44)

m.c79 = Constraint(expr= - 3482.44*m.b58 + m.x95 - m.x104 >= -3482.44)

m.c80 = Constraint(expr= - 4382.44*m.b59 - m.x98 + m.x104 >= -4382.44)

m.c81 = Constraint(expr= - 4382.44*m.b60 - m.x87 + m.x98 >= -4382.44)

m.c82 = Constraint(expr= - 4382.44*m.b61 + m.x87 - m.x100 >= -4382.44)

m.c83 = Constraint(expr= - 4382.44*m.b62 - m.x97 + m.x100 >= -4382.44)

m.c84 = Constraint(expr= - 4382.44*m.b63 - m.x91 + m.x97 >= -4382.44)

m.c85 = Constraint(expr= - 4382.44*m.b64 - m.x103 + m.x104 >= -4382.44)

m.c86 = Constraint(expr= - 4382.44*m.b65 - m.x89 + m.x101 >= -4382.44)

m.c87 = Constraint(expr= - 4382.44*m.b66 + m.x89 - m.x99 >= -4382.44)

m.c88 = Constraint(expr= - 5929*m.b46 - m.x93 + m.x105 <= 0)

m.c89 = Constraint(expr= - 5929*m.b47 - m.x93 + m.x105 <= 0)

m.c90 = Constraint(expr= - 5029*m.b48 - m.x92 + m.x93 <= 0)

m.c91 = Constraint(expr= - 5029*m.b49 - m.x92 + m.x93 <= 0)

m.c92 = Constraint(expr= - 6400*m.b50 + m.x92 - m.x106 <= 0)

m.c93 = Constraint(expr= - 5029*m.b51 - m.x88 + m.x96 <= 0)

m.c94 = Constraint(expr= - 5500*m.b52 + m.x88 - m.x94 <= 0)

m.c95 = Constraint(expr= - 6400*m.b53 + m.x94 - m.x106 <= 0)

m.c96 = Constraint(expr= - 6400*m.b54 - m.x100 + m.x106 <= 0)

m.c97 = Constraint(expr= - 3482.44*m.b55 + m.x90 - m.x95 <= 0)

m.c98 = Constraint(expr= - 3482.44*m.b56 + m.x90 - m.x95 <= 0)

m.c99 = Constraint(expr= - 4382.44*m.b57 + m.x95 - m.x104 <= 0)

m.c100 = Constraint(expr= - 4382.44*m.b58 + m.x95 - m.x104 <= 0)

m.c101 = Constraint(expr= - 4382.44*m.b59 - m.x98 + m.x104 <= 0)

m.c102 = Constraint(expr= - 4382.44*m.b60 - m.x87 + m.x98 <= 0)

m.c103 = Constraint(expr= - 4382.44*m.b61 + m.x87 - m.x100 <= 0)

m.c104 = Constraint(expr= - 4382.44*m.b62 - m.x97 + m.x100 <= 0)

m.c105 = Constraint(expr= - 1882.44*m.b63 - m.x91 + m.x97 <= 0)

m.c106 = Constraint(expr= - 4382.44*m.b64 - m.x103 + m.x104 <= 0)

m.c107 = Constraint(expr= - 3969*m.b65 - m.x89 + m.x101 <= 0)

m.c108 = Constraint(expr= - 3757.44*m.b66 + m.x89 - m.x99 <= 0)

m.c109 = Constraint(expr=   m.x1 - 230.881425454383*m.b46 >= -230.881425454383)

m.c110 = Constraint(expr=   m.x2 - 230.881425454383*m.b47 >= -230.881425454383)

m.c111 = Constraint(expr=   m.x3 - 195.858591670881*m.b48 >= -195.858591670881)

m.c112 = Constraint(expr=   m.x4 - 195.858591670881*m.b49 >= -195.858591670881)

m.c113 = Constraint(expr=   m.x5 - 87.2213765084548*m.b50 >= -87.2213765084548)

m.c114 = Constraint(expr=   m.x6 - 25.2192935471771*m.b51 >= -25.2192935471771)

m.c115 = Constraint(expr=   m.x7 - 28.4681669051455*m.b52 >= -28.4681669051455)

m.c116 = Constraint(expr=   m.x8 - 35.1707558553061*m.b53 >= -35.1707558553061)

m.c117 = Constraint(expr=   m.x9 - 53.5309450076729*m.b54 >= -53.5309450076729)

m.c118 = Constraint(expr=   m.x12 - 88.7710296317997*m.b55 >= -88.7710296317997)

m.c119 = Constraint(expr=   m.x13 - 10.7961327691767*m.b56 >= -10.7961327691767)

m.c120 = Constraint(expr=   m.x14 - 70.7782927092091*m.b57 >= -70.7782927092091)

m.c121 = Constraint(expr=   m.x15 - 8.6078966125965*m.b58 >= -8.6078966125965)

m.c122 = Constraint(expr=   m.x16 - 61.2578302162646*m.b59 >= -61.2578302162646)

m.c123 = Constraint(expr=   m.x17 - 62.7705970255575*m.b60 >= -62.7705970255575)

m.c124 = Constraint(expr=   m.x18 - 177.542059263599*m.b61 >= -177.542059263599)

m.c125 = Constraint(expr=   m.x19 - 125.541194051115*m.b62 >= -125.541194051115)

m.c126 = Constraint(expr=   m.x20 - 79.3992226757409*m.b63 >= -79.3992226757409)

m.c127 = Constraint(expr=   m.x21 - 14.9491145521834*m.b64 >= -14.9491145521834)

m.c128 = Constraint(expr=   m.x23 - 2.72006561154535*m.b65 >= -2.72006561154535)

m.c129 = Constraint(expr=   m.x24 - 10.9930142912741*m.b66 >= -10.9930142912741)

m.c130 = Constraint(expr=   m.x1 - 230.881425454383*m.b46 <= 0)

m.c131 = Constraint(expr=   m.x2 - 230.881425454383*m.b47 <= 0)

m.c132 = Constraint(expr=   m.x3 - 173.61748395652*m.b48 <= 0)

m.c133 = Constraint(expr=   m.x4 - 173.61748395652*m.b49 <= 0)

m.c134 = Constraint(expr=   m.x5 - 94.0874240733678*m.b50 <= 0)

m.c135 = Constraint(expr=   m.x6 - 22.3554670513479*m.b51 <= 0)

m.c136 = Constraint(expr=   m.x7 - 28.4681669051455*m.b52 <= 0)

m.c137 = Constraint(expr=   m.x8 - 37.939390016601*m.b53 <= 0)

m.c138 = Constraint(expr=   m.x9 - 64.6899637554959*m.b54 <= 0)

m.c139 = Constraint(expr=   m.x12 - 79.1325369145847*m.b55 <= 0)

m.c140 = Constraint(expr=   m.x13 - 9.62392098452798*m.b56 <= 0)

m.c141 = Constraint(expr=   m.x14 - 79.3992226757409*m.b57 <= 0)

m.c142 = Constraint(expr=   m.x15 - 9.65635470639685*m.b58 <= 0)

m.c143 = Constraint(expr=   m.x16 - 61.2578302162646*m.b59 <= 0)

m.c144 = Constraint(expr=   m.x17 - 62.7705970255575*m.b60 <= 0)

m.c145 = Constraint(expr=   m.x18 - 177.542059263599*m.b61 <= 0)

m.c146 = Constraint(expr=   m.x19 - 125.541194051115*m.b62 <= 0)

m.c147 = Constraint(expr=   m.x20 - 52.0377886055166*m.b63 <= 0)

m.c148 = Constraint(expr=   m.x21 - 14.9491145521834*m.b64 <= 0)

m.c149 = Constraint(expr=   m.x23 - 2.58858207745253*m.b65 <= 0)

m.c150 = Constraint(expr=   m.x24 - 10.1789933422708*m.b66 <= 0)
