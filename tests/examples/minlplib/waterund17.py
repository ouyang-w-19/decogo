#  NLP written by GAMS Convert at 04/21/18 13:55:19
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         67       35        3       29        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         75       75        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        348      168      180        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,100000),initialize=0)

m.obj = Objective(expr=   m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13 + m.x14
                        + m.x15 + m.x16, sense=minimize)

m.c2 = Constraint(expr= - m.x2 - m.x7 - m.x12 + m.x17 - m.x27 - m.x32 - m.x37 - m.x42 - m.x47 == 0)

m.c3 = Constraint(expr= - m.x3 - m.x8 - m.x13 + m.x18 - m.x28 - m.x33 - m.x38 - m.x43 - m.x48 == 0)

m.c4 = Constraint(expr= - m.x4 - m.x9 - m.x14 + m.x19 - m.x29 - m.x34 - m.x39 - m.x44 - m.x49 == 0)

m.c5 = Constraint(expr= - m.x5 - m.x10 - m.x15 + m.x20 - m.x30 - m.x35 - m.x40 - m.x45 - m.x50 == 0)

m.c6 = Constraint(expr= - m.x6 - m.x11 - m.x16 - m.x31 - m.x36 - m.x41 - m.x46 - m.x51 == -65)

m.c7 = Constraint(expr=   m.x17 - m.x22 - m.x27 - m.x28 - m.x29 - m.x30 - m.x31 == 0)

m.c8 = Constraint(expr=   m.x18 - m.x23 - m.x32 - m.x33 - m.x34 - m.x35 - m.x36 == 0)

m.c9 = Constraint(expr=   m.x19 - m.x24 - m.x37 - m.x38 - m.x39 - m.x40 - m.x41 == 0)

m.c10 = Constraint(expr=   m.x20 - m.x25 - m.x42 - m.x43 - m.x44 - m.x45 - m.x46 == 0)

m.c11 = Constraint(expr= - m.x26 - m.x47 - m.x48 - m.x49 - m.x50 - m.x51 == -75)

m.c12 = Constraint(expr=m.x17*m.x52 - (m.x27*m.x64 + m.x32*m.x67 + m.x37*m.x70 + m.x42*m.x73) - 3*m.x2 - 2*m.x12
                         - 150*m.x47 == 0)

m.c13 = Constraint(expr=m.x17*m.x53 - (m.x27*m.x65 + m.x32*m.x68 + m.x37*m.x71 + m.x42*m.x74) - 2*m.x7 - 4*m.x12
                         - 800*m.x47 == 0)

m.c14 = Constraint(expr=m.x17*m.x54 - (m.x27*m.x66 + m.x32*m.x69 + m.x37*m.x72 + m.x42*m.x75) - 2*m.x2 - 2*m.x7
                         - 220*m.x47 == 0)

m.c15 = Constraint(expr=m.x18*m.x55 - (m.x28*m.x64 + m.x33*m.x67 + m.x38*m.x70 + m.x43*m.x73) - 3*m.x3 - 2*m.x13
                         - 150*m.x48 == 0)

m.c16 = Constraint(expr=m.x18*m.x56 - (m.x28*m.x65 + m.x33*m.x68 + m.x38*m.x71 + m.x43*m.x74) - 2*m.x8 - 4*m.x13
                         - 800*m.x48 == 0)

m.c17 = Constraint(expr=m.x18*m.x57 - (m.x28*m.x66 + m.x33*m.x69 + m.x38*m.x72 + m.x43*m.x75) - 2*m.x3 - 2*m.x8
                         - 220*m.x48 == 0)

m.c18 = Constraint(expr=m.x19*m.x58 - (m.x29*m.x64 + m.x34*m.x67 + m.x39*m.x70 + m.x44*m.x73) - 3*m.x4 - 2*m.x14
                         - 150*m.x49 == 0)

m.c19 = Constraint(expr=m.x19*m.x59 - (m.x29*m.x65 + m.x34*m.x68 + m.x39*m.x71 + m.x44*m.x74) - 2*m.x9 - 4*m.x14
                         - 800*m.x49 == 0)

m.c20 = Constraint(expr=m.x19*m.x60 - (m.x29*m.x66 + m.x34*m.x69 + m.x39*m.x72 + m.x44*m.x75) - 2*m.x4 - 2*m.x9
                         - 220*m.x49 == 0)

m.c21 = Constraint(expr=m.x20*m.x61 - (m.x30*m.x64 + m.x35*m.x67 + m.x40*m.x70 + m.x45*m.x73) - 3*m.x5 - 2*m.x15
                         - 150*m.x50 == 0)

m.c22 = Constraint(expr=m.x20*m.x62 - (m.x30*m.x65 + m.x35*m.x68 + m.x40*m.x71 + m.x45*m.x74) - 2*m.x10 - 4*m.x15
                         - 800*m.x50 == 0)

m.c23 = Constraint(expr=m.x20*m.x63 - (m.x30*m.x66 + m.x35*m.x69 + m.x40*m.x72 + m.x45*m.x75) - 2*m.x5 - 2*m.x10
                         - 220*m.x50 == 0)

m.c24 = Constraint(expr=-m.x17*(m.x64 - m.x52) == -6120)

m.c25 = Constraint(expr=-m.x17*(m.x65 - m.x53) == -3096)

m.c26 = Constraint(expr=-m.x17*(m.x66 - m.x54) == -1800)

m.c27 = Constraint(expr=-m.x18*(m.x67 - m.x55) == -6400)

m.c28 = Constraint(expr=-m.x18*(m.x68 - m.x56) == -60800)

m.c29 = Constraint(expr=-m.x18*(m.x69 - m.x57) == -8640)

m.c30 = Constraint(expr=-m.x19*(m.x70 - m.x58) == -5600)

m.c31 = Constraint(expr=-m.x19*(m.x71 - m.x59) == -1400)

m.c32 = Constraint(expr=-m.x19*(m.x72 - m.x60) == -11200)

m.c33 = Constraint(expr=-m.x20*(m.x73 - m.x61) == -648)

m.c34 = Constraint(expr=-m.x20*(m.x74 - m.x62) == -408)

m.c35 = Constraint(expr=-m.x20*(m.x75 - m.x63) == -360)

m.c36 = Constraint(expr=   m.x52 <= 30)

m.c37 = Constraint(expr=   m.x53 <= 37)

m.c38 = Constraint(expr=   m.x54 <= 10)

m.c39 = Constraint(expr=   m.x55 <= 20)

m.c40 = Constraint(expr=   m.x56 <= 300)

m.c41 = Constraint(expr=   m.x57 <= 45)

m.c42 = Constraint(expr=   m.x58 <= 120)

m.c43 = Constraint(expr=   m.x59 <= 20)

m.c44 = Constraint(expr=   m.x60 <= 200)

m.c45 = Constraint(expr=   m.x61 <= 23)

m.c46 = Constraint(expr=   m.x62 <= 43)

m.c47 = Constraint(expr=   m.x63 <= 15)

m.c48 = Constraint(expr=   m.x64 <= 115)

m.c49 = Constraint(expr=   m.x65 <= 80)

m.c50 = Constraint(expr=   m.x66 <= 35)

m.c51 = Constraint(expr=   m.x67 <= 120)

m.c52 = Constraint(expr=   m.x68 <= 1250)

m.c53 = Constraint(expr=   m.x69 <= 180)

m.c54 = Constraint(expr=   m.x70 <= 220)

m.c55 = Constraint(expr=   m.x71 <= 45)

m.c56 = Constraint(expr=   m.x72 <= 400)

m.c57 = Constraint(expr=   m.x73 <= 50)

m.c58 = Constraint(expr=   m.x74 <= 60)

m.c59 = Constraint(expr=   m.x75 <= 30)

m.c60 = Constraint(expr=-(m.x31*m.x64 + m.x36*m.x67 + m.x41*m.x70 + m.x46*m.x73) - 3*m.x6 - 2*m.x16 - 150*m.x51
                         >= -5850)

m.c61 = Constraint(expr=-(m.x31*m.x65 + m.x36*m.x68 + m.x41*m.x71 + m.x46*m.x74) - 2*m.x11 - 4*m.x16 - 800*m.x51
                         >= -26000)

m.c62 = Constraint(expr=-(m.x31*m.x66 + m.x36*m.x69 + m.x41*m.x72 + m.x46*m.x75) - 2*m.x6 - 2*m.x11 - 220*m.x51
                         >= -10400)

m.c63 = Constraint(expr=   m.x17 <= 72)

m.c64 = Constraint(expr=   m.x18 <= 64)

m.c65 = Constraint(expr=   m.x19 <= 56)

m.c66 = Constraint(expr=   m.x20 <= 24)

m.c67 = Constraint(expr=   m.x21 <= 0)
