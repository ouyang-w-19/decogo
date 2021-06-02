#  MINLP written by GAMS Convert at 04/21/18 13:51:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         35       14        0       21        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         25       16        3        6        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         94       58       36        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,80),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,45),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,2950),initialize=983.333333333333)
m.x5 = Var(within=Reals,bounds=(0,2950),initialize=983.333333333333)
m.x6 = Var(within=Reals,bounds=(0,2950),initialize=983.333333333333)
m.x7 = Var(within=Reals,bounds=(0,400),initialize=133.333333333333)
m.x8 = Var(within=Reals,bounds=(0,400),initialize=133.333333333333)
m.x9 = Var(within=Reals,bounds=(0,400),initialize=133.333333333333)
m.x10 = Var(within=Reals,bounds=(0,350),initialize=116.666666666667)
m.x11 = Var(within=Reals,bounds=(0,350),initialize=116.666666666667)
m.x12 = Var(within=Reals,bounds=(0,350),initialize=116.666666666667)
m.x13 = Var(within=Reals,bounds=(0,1),initialize=0.333333333333333)
m.x14 = Var(within=Reals,bounds=(0,1),initialize=0.333333333333333)
m.x15 = Var(within=Reals,bounds=(0,1),initialize=0.333333333333333)
m.i16 = Var(within=Integers,bounds=(0,3),initialize=1)
m.i17 = Var(within=Integers,bounds=(0,3),initialize=1)
m.i18 = Var(within=Integers,bounds=(0,3),initialize=1)
m.i19 = Var(within=Integers,bounds=(0,3),initialize=1)
m.i20 = Var(within=Integers,bounds=(0,3),initialize=1)
m.i21 = Var(within=Integers,bounds=(0,3),initialize=1)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b23 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b24 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=(6329.03 + 1800*m.x1)*m.i16*m.i19*m.b22 + (2489.31 + 1800*m.x2)*m.i17*m.i20*m.b23 + (3270.27 + 
                       1800*m.x3)*m.i18*m.i21*m.b24, sense=minimize)

m.c2 = Constraint(expr=(-19.9*(0.000338983050847458*m.x4)**3) - 0.161*(0.000338983050847458*m.x4)**2*m.x10 + 
                       1.90169491525424e-7*m.x10**2*m.x4 + m.x1 == 0)

m.c3 = Constraint(expr=(-1.21*(0.000338983050847458*m.x5)**3) - 0.0644*(0.000338983050847458*m.x5)**2*m.x11 + 
                       1.91186440677966e-7*m.x11**2*m.x5 + m.x2 == 0)

m.c4 = Constraint(expr=(-6.52*(0.000338983050847458*m.x6)**3) - 0.102*(0.000338983050847458*m.x6)**2*m.x12 + 
                       7.86440677966102e-8*m.x12**2*m.x6 + m.x3 == 0)

m.c5 = Constraint(expr=(-0.00023593220338983*m.x4*m.x10) - 629*(0.000338983050847458*m.x4)**2 + 0.0116*m.x10**2 + m.x7
                        == 0)

m.c6 = Constraint(expr=(-0.001*m.x5*m.x11) - 215*(0.000338983050847458*m.x5)**2 + 0.115*m.x11**2 + m.x8 == 0)

m.c7 = Constraint(expr=(-0.000179661016949153*m.x6*m.x12) - 361*(0.000338983050847458*m.x6)**2 + 0.00946*m.x12**2 + m.x9
                        == 0)

m.c8 = Constraint(expr=   m.x13 + m.x14 + m.x15 == 1)

m.c9 = Constraint(expr=0.00285714285714286*m.x10*m.i16 - m.x13 == 0)

m.c10 = Constraint(expr=0.00285714285714286*m.x11*m.i17 - m.x14 == 0)

m.c11 = Constraint(expr=0.00285714285714286*m.x12*m.i18 - m.x15 == 0)

m.c12 = Constraint(expr=0.0025*m.x7*m.i19 - m.b22 == 0)

m.c13 = Constraint(expr=0.0025*m.x8*m.i20 - m.b23 == 0)

m.c14 = Constraint(expr=0.0025*m.x9*m.i21 - m.b24 == 0)

m.c15 = Constraint(expr=   0.000338983050847458*m.x4 - m.b22 <= 0)

m.c16 = Constraint(expr=   0.000338983050847458*m.x5 - m.b23 <= 0)

m.c17 = Constraint(expr=   0.000338983050847458*m.x6 - m.b24 <= 0)

m.c18 = Constraint(expr=   0.0125*m.x1 - m.b22 <= 0)

m.c19 = Constraint(expr=   0.04*m.x2 - m.b23 <= 0)

m.c20 = Constraint(expr=   0.0222222222222222*m.x3 - m.b24 <= 0)

m.c21 = Constraint(expr=   0.0025*m.x7 - m.b22 <= 0)

m.c22 = Constraint(expr=   0.0025*m.x8 - m.b23 <= 0)

m.c23 = Constraint(expr=   0.0025*m.x9 - m.b24 <= 0)

m.c24 = Constraint(expr=   0.00285714285714286*m.x10 - m.b22 <= 0)

m.c25 = Constraint(expr=   0.00285714285714286*m.x11 - m.b23 <= 0)

m.c26 = Constraint(expr=   0.00285714285714286*m.x12 - m.b24 <= 0)

m.c27 = Constraint(expr=   m.x13 - m.b22 <= 0)

m.c28 = Constraint(expr=   m.x14 - m.b23 <= 0)

m.c29 = Constraint(expr=   m.x15 - m.b24 <= 0)

m.c30 = Constraint(expr=   m.i16 - 3*m.b22 <= 0)

m.c31 = Constraint(expr=   m.i17 - 3*m.b23 <= 0)

m.c32 = Constraint(expr=   m.i18 - 3*m.b24 <= 0)

m.c33 = Constraint(expr=   m.i19 - 3*m.b22 <= 0)

m.c34 = Constraint(expr=   m.i20 - 3*m.b23 <= 0)

m.c35 = Constraint(expr=   m.i21 - 3*m.b24 <= 0)
