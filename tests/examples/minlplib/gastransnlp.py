#  NLP written by GAMS Convert at 04/21/18 13:52:21
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         45       42        3        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         65       65        0        0        0        0        0        0
#  FX      5        5        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        146      122       24        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,None),initialize=-0.656505736)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=0.686533416)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0.100750712)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=-0.397724192)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=-0.415575766)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=-0.551894266)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=-0.300338992)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=0.712540694)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=-0.865772554)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0.000421337999999993)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0.996235254)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=0.157466756)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0.982266078)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=0.524500934)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=-0.738615034)
m.x16 = Var(within=Reals,bounds=(None,None),initialize=0.279437518)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=-0.680964272)
m.x18 = Var(within=Reals,bounds=(None,None),initialize=-0.499838934)
m.x19 = Var(within=Reals,bounds=(None,None),initialize=0.337857218)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=-0.129287238)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=-0.280599468)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=-0.73701682)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=-0.699796424)
m.x25 = Var(within=Reals,bounds=(0,1.2),initialize=0)
m.x26 = Var(within=Reals,bounds=(None,-4.034),initialize=-4.034)
m.x27 = Var(within=Reals,bounds=(None,-0.222),initialize=-0.222)
m.x28 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x29 = Var(within=Reals,bounds=(None,-15.616),initialize=-15.616)
m.x30 = Var(within=Reals,bounds=(None,-3.918),initialize=-3.918)
m.x31 = Var(within=Reals,bounds=(0,8.4),initialize=0)
m.x32 = Var(within=Reals,bounds=(None,-5.256),initialize=-5.256)
m.x33 = Var(within=Reals,bounds=(None,-6.385),initialize=-6.385)
m.x34 = Var(within=Reals,bounds=(0,4.8),initialize=0)
m.x35 = Var(within=Reals,bounds=(None,-6.848),initialize=-6.848)
m.x36 = Var(within=Reals,bounds=(None,-2.12),initialize=-2.12)
m.x37 = Var(within=Reals,bounds=(None,-1.919),initialize=-1.919)
m.x38 = Var(within=Reals,bounds=(0,0.96),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x40 = Var(within=Reals,bounds=(20.344,22.012),initialize=20.344)
m.x41 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x43 = Var(within=Reals,bounds=(8.87,11.594),initialize=8.87)
m.x44 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,4382.44),initialize=0)
m.x46 = Var(within=Reals,bounds=(900,6400),initialize=900)
m.x47 = Var(within=Reals,bounds=(0,4382.44),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,4382.44),initialize=0)
m.x49 = Var(within=Reals,bounds=(2500,4382.44),initialize=2500)
m.x50 = Var(within=Reals,bounds=(900,6400),initialize=900)
m.x51 = Var(within=Reals,bounds=(0,5929),initialize=0)
m.x52 = Var(within=Reals,bounds=(900,6400),initialize=900)
m.x53 = Var(within=Reals,bounds=(900,4382.44),initialize=900)
m.x54 = Var(within=Reals,bounds=(0,5929),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,4382.44),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,4382.44),initialize=0)
m.x57 = Var(within=Reals,bounds=(625,4382.44),initialize=625)
m.x58 = Var(within=Reals,bounds=(0,4382.44),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,3969),initialize=0)
m.x60 = Var(within=Reals,bounds=(2500,4382.44),initialize=2500)
m.x61 = Var(within=Reals,bounds=(0,4382.44),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,4382.44),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,5929),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,6400),initialize=0)

m.obj = Objective(expr=   2.28*m.x31 + 2.28*m.x34 + 1.68*m.x38 + 1.68*m.x40 + 2.28*m.x43, sense=minimize)

m.c1 = Constraint(expr= - m.x17 + m.x18 - m.x25 == 0)

m.c2 = Constraint(expr= - m.x6 + m.x7 - m.x26 == 0)

m.c3 = Constraint(expr= - m.x23 + m.x24 - m.x27 == 0)

m.c4 = Constraint(expr= - m.x10 - m.x11 + m.x12 + m.x13 - m.x28 == 0)

m.c5 = Constraint(expr= - m.x20 - m.x29 == 0)

m.c6 = Constraint(expr= - m.x3 - m.x4 + m.x5 - m.x30 == 0)

m.c7 = Constraint(expr= - m.x1 - m.x2 + m.x3 + m.x4 - m.x31 == 0)

m.c8 = Constraint(expr= - m.x7 + m.x8 - m.x32 == 0)

m.c9 = Constraint(expr= - m.x12 - m.x13 + m.x14 + m.x15 - m.x33 == 0)

m.c10 = Constraint(expr=   m.x6 - m.x34 == 0)

m.c11 = Constraint(expr= - m.x19 + m.x20 - m.x35 == 0)

m.c12 = Constraint(expr= - m.x16 + m.x17 - m.x36 == 0)

m.c13 = Constraint(expr= - m.x24 - m.x37 == 0)

m.c14 = Constraint(expr= - m.x9 - m.x18 + m.x19 - m.x38 == 0)

m.c15 = Constraint(expr= - m.x22 + m.x23 - m.x39 == 0)

m.c16 = Constraint(expr=   m.x10 + m.x11 - m.x40 == 0)

m.c17 = Constraint(expr= - m.x21 + m.x22 - m.x41 == 0)

m.c18 = Constraint(expr= - m.x14 - m.x15 + m.x16 + m.x21 - m.x42 == 0)

m.c19 = Constraint(expr=   m.x1 + m.x2 - m.x43 == 0)

m.c20 = Constraint(expr= - m.x5 - m.x8 + m.x9 - m.x44 == 0)

m.c21 = Constraint(expr=SignPower(m.x1,2) + 8.99076279639866*m.x51 - 8.99076279639866*m.x63 == 0)

m.c22 = Constraint(expr=SignPower(m.x2,2) + 8.99076279639866*m.x51 - 8.99076279639866*m.x63 == 0)

m.c23 = Constraint(expr=SignPower(m.x3,2) + 5.99384186426577*m.x50 - 5.99384186426577*m.x51 == 0)

m.c24 = Constraint(expr=SignPower(m.x4,2) + 5.99384186426577*m.x50 - 5.99384186426577*m.x51 == 0)

m.c25 = Constraint(expr=SignPower(m.x5,2) - 1.38319427636902*m.x50 + 1.38319427636902*m.x64 == 0)

m.c26 = Constraint(expr=SignPower(m.x6,2) + 0.0993769948466698*m.x46 - 0.0993769948466698*m.x54 == 0)

m.c27 = Constraint(expr=SignPower(m.x7,2) - 0.147352095807131*m.x46 + 0.147352095807131*m.x52 == 0)

m.c28 = Constraint(expr=SignPower(m.x8,2) - 0.224905830442463*m.x52 + 0.224905830442463*m.x64 == 0)

m.c29 = Constraint(expr=SignPower(m.x9,2) + 0.653873657919902*m.x58 - 0.653873657919902*m.x64 == 0)

m.c30 = Constraint(expr=SignPower(m.x12,2) - 1.79815255927973*m.x48 + 1.79815255927973*m.x53 == 0)

m.c31 = Constraint(expr=SignPower(m.x13,2) - 0.0265962529480588*m.x48 + 0.0265962529480588*m.x53 == 0)

m.c32 = Constraint(expr=SignPower(m.x14,2) - 1.43852204742379*m.x53 + 1.43852204742379*m.x62 == 0)

m.c33 = Constraint(expr=SignPower(m.x15,2) - 0.021277002358447*m.x53 + 0.021277002358447*m.x62 == 0)

m.c34 = Constraint(expr=SignPower(m.x16,2) + 0.856263123466539*m.x56 - 0.856263123466539*m.x62 == 0)

m.c35 = Constraint(expr=SignPower(m.x17,2) + 0.899076279639866*m.x45 - 0.899076279639866*m.x56 == 0)

m.c36 = Constraint(expr=SignPower(m.x18,2) - 7.19261023711893*m.x45 + 7.19261023711893*m.x58 == 0)

m.c37 = Constraint(expr=SignPower(m.x19,2) + 3.59630511855946*m.x55 - 3.59630511855946*m.x58 == 0)

m.c38 = Constraint(expr=SignPower(m.x20,2) + 1.43852204742379*m.x49 - 1.43852204742379*m.x55 == 0)

m.c39 = Constraint(expr=SignPower(m.x21,2) + 0.0509935163731392*m.x61 - 0.0509935163731392*m.x62 == 0)

m.c40 = Constraint(expr=SignPower(m.x23,2) + 0.0016882734118691*m.x47 - 0.0016882734118691*m.x59 == 0)

m.c41 = Constraint(expr=SignPower(m.x24,2) - 0.0275751323938619*m.x47 + 0.0275751323938619*m.x57 == 0)

m.c42 = Constraint(expr=-m.x10**2 + 7.19261023711893*m.x48 - 7.19261023711893*m.x60 >= 0)

m.c43 = Constraint(expr=-m.x11**2 + 0.106385011792235*m.x48 - 0.106385011792235*m.x60 >= 0)

m.c44 = Constraint(expr=-m.x22**2 + 0.0063634920908912*m.x59 - 0.0063634920908912*m.x61 >= 0)
