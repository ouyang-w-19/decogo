#  MINLP written by GAMS Convert at 04/21/18 13:54:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         19       18        1        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         36       17        0       19        0        0        0        0
#  FX      1        0        0        1        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        169      106       63        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,14),initialize=0)
m.i2 = Var(within=Integers,bounds=(0,14),initialize=0)
m.i3 = Var(within=Integers,bounds=(0,14),initialize=0)
m.i4 = Var(within=Integers,bounds=(0,14),initialize=0)
m.i5 = Var(within=Integers,bounds=(0,14),initialize=0)
m.i6 = Var(within=Integers,bounds=(0,14),initialize=0)
m.i7 = Var(within=Integers,bounds=(0,14),initialize=0)
m.i8 = Var(within=Integers,bounds=(0,14),initialize=0)
m.i9 = Var(within=Integers,bounds=(0,14),initialize=0)
m.i10 = Var(within=Integers,bounds=(0,14),initialize=0)
m.i11 = Var(within=Integers,bounds=(0,14),initialize=0)
m.i12 = Var(within=Integers,bounds=(0,14),initialize=0)
m.i13 = Var(within=Integers,bounds=(0,14),initialize=0)
m.i14 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i15 = Var(within=Integers,bounds=(0,14),initialize=0)
m.i16 = Var(within=Integers,bounds=(0,14),initialize=0)
m.i17 = Var(within=Integers,bounds=(0,14),initialize=0)
m.i18 = Var(within=Integers,bounds=(0,14),initialize=0)
m.i19 = Var(within=Integers,bounds=(0,14),initialize=0)
m.x20 = Var(within=Reals,bounds=(1,1000),initialize=1)
m.x21 = Var(within=Reals,bounds=(1,1000),initialize=1)
m.x22 = Var(within=Reals,bounds=(1,100),initialize=1)
m.x23 = Var(within=Reals,bounds=(1,32.2),initialize=1)
m.x24 = Var(within=Reals,bounds=(1,100),initialize=1)
m.x25 = Var(within=Reals,bounds=(18.4,100),initialize=18.4)
m.x26 = Var(within=Reals,bounds=(1.4,14),initialize=1.4)
m.x27 = Var(within=Reals,bounds=(1.4,14),initialize=1.4)
m.x28 = Var(within=Reals,bounds=(0.001,1),initialize=0.001)
m.x29 = Var(within=Reals,bounds=(0.001,1),initialize=0.001)
m.x30 = Var(within=Reals,bounds=(0.001,1),initialize=0.001)
m.x31 = Var(within=Reals,bounds=(0.001,1),initialize=0.001)
m.x32 = Var(within=Reals,bounds=(0.001,1),initialize=0.001)
m.x33 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x34 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x35 = Var(within=Reals,bounds=(-10,10),initialize=0)

m.obj = Objective(expr=-m.x25/m.x23, sense=minimize)

m.c1 = Constraint(expr=   23.58*m.i1 + 22.88*m.i2 + 21.74*m.i3 + 18.25*m.i4 - 0.03*m.i5 + 38.13*m.i6 + 66.86*m.i7
                        + 93.84*m.i8 + 92.88*m.i9 + 76.34*m.i10 + 22.42*m.i11 + 31.22*m.i12 + 73.23*m.i13 + 50.17*m.i14
                        + 52.82*m.i15 + 11.74*m.i16 + 63.56*m.i17 + 68.78*m.i18 + 52.1*m.i19 - m.x20 == -198.2)

m.c2 = Constraint(expr=-m.x20/(0.584 + 0.0136065*m.i1 - (0.0141*m.i1 + 0.0189*m.i2 + 0.0164*m.i3 + 0.0067*m.i4 + 0.0111*
                       m.i5 + 0.0105*m.i6 + 0.0133*m.i7 + 0.0068*m.i8 + 0.0741*m.i9 + 0.0204*m.i10 + 0.0168*m.i11 + 
                       0.0098*m.i12 + 0.0243*m.i13 + 0.0295*m.i14 + 0.013*m.i15 + 0.0169*m.i16 + 0.0031*m.i17 + 0.0119*
                       m.i18 + 0.0019*m.i19)**2 + 0.0182385*m.i2 + 0.015826*m.i3 + 0.0064655*m.i4 + 0.0107115*m.i5 + 
                       0.0101325*m.i6 + 0.0128345*m.i7 + 0.006562*m.i8 + 0.0715065*m.i9 + 0.02316*m.i10 + 0.016212*m.i11
                        + 0.009457*m.i12 + 0.0234495*m.i13 + 0.0284675*m.i14 + 0.012545*m.i15 + 0.0163085*m.i16 + 
                       0.0029915*m.i17 + 0.0114835*m.i18 + 0.0018335*m.i19) + m.x21 == 0)

m.c3 = Constraint(expr=-1/(0.113 + 0.014*m.i1 + 0.0096*m.i2 + 0.0044*m.i3 - 0.0011*m.i4 + 0.0089*m.i5 + 0.0081*m.i6 - 
                       0.0025*m.i7 + 0.0066*m.i8 - 0.0048*m.i9 - 0.012*m.i10 + 0.0017*m.i11 - 0.0016*m.i12 - 0.0013*
                       m.i13 - 0.0013*m.i14 - 0.005*m.i15 - 0.0042*m.i16 - 0.002*m.i17 - 0.0017*m.i18 - 0.0019*m.i19)**2
                        + m.x22 == 0)

m.c4 = Constraint(expr=   8.8*m.i1 + 7.26*m.i2 + 5*m.i3 + 1.76*m.i4 + 4*m.i5 + 8.6*m.i6 + 9*m.i7 + 8.6*m.i8 + 10.7*m.i9
                        + 10.7*m.i10 + 8.4*m.i11 + 8.4*m.i12 + 14*m.i13 + 10.5*m.i14 + 10.5*m.i15 + 7.5*m.i16
                        + 10.7*m.i17 + 8*m.i18 + 8*m.i19 - m.x23 == 0)

m.c5 = Constraint(expr=   2.373*m.i1 + 2.226*m.i2 + 1.691*m.i3 + 0.636*m.i4 - 0.67*m.i5 + 4.532*m.i6 + 6.582*m.i7
                        + 9.52*m.i8 + 16.826*m.i9 + 12.499*m.i10 + 2.41*m.i11 + 4.682*m.i12 + 10.788*m.i13 + 6.436*m.i14
                        + 6.93*m.i15 + 1.896*m.i16 + 6.884*m.i17 + 6.817*m.i18 + 5.984*m.i19 - m.x24 == -15.3)

m.c6 = Constraint(expr=-m.x20/m.x21 + m.x32 == 0)

m.c7 = Constraint(expr=-272.04/m.x21 + m.x30 == 0)

m.c8 = Constraint(expr=-316.48/m.x21 + m.x31 == 0)

m.c9 = Constraint(expr=-log(m.x22)*m.x32/(1 - m.x32) + m.x33 == 0)

m.c10 = Constraint(expr= - 0.4605*m.x33 + m.x34 == 0.4835)

m.c11 = Constraint(expr=-(m.x33 - (1 + m.x32)*m.x34)/(3 + m.x32)/(1 - m.x32)**2/m.x34 + m.x35 == 0)

m.c12 = Constraint(expr=-exp(-(1 + m.x35*(3 + m.x30)*(1 - m.x30)**3 - m.x30**2)*m.x34/m.x30) + m.x28 == 0)

m.c13 = Constraint(expr=-exp(-(1 + m.x35*(3 + m.x31)*(1 - m.x31)**3 - m.x31**2)*m.x34/m.x31) + m.x29 == 0)

m.c14 = Constraint(expr=-m.x28*m.x22 + m.x26 == 0)

m.c15 = Constraint(expr=-m.x29*m.x22 + m.x27 == 0)

m.c16 = Constraint(expr=-((1 - m.x30)/(1 - m.x32))**0.38*m.x24 + m.x25 == 0)

m.c17 = Constraint(expr=   m.i1 - m.i3 - 2*m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 + m.i13 - m.i16 + m.i17 == 2)

m.c18 = Constraint(expr=   m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 + m.i11 + m.i12 + m.i13
                         + m.i14 + m.i15 + m.i16 + m.i17 + m.i18 + m.i19 >= 2)
