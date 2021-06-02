#  MINLP written by GAMS Convert at 04/21/18 13:51:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         45        1        6       38        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         36        1        5       30        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        222      172       50        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i2 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i3 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i4 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i5 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i6 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i7 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i8 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i9 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i10 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i11 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i12 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i13 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i14 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i15 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i16 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i17 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i18 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i19 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i20 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i21 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i22 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i23 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i24 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i25 = Var(within=Integers,bounds=(0,5),initialize=0)
m.b26 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b27 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b28 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b29 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b30 = Var(within=Binary,bounds=(0,1),initialize=0)
m.i31 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i32 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i33 = Var(within=Integers,bounds=(0,9),initialize=0)
m.i34 = Var(within=Integers,bounds=(0,6),initialize=0)
m.i35 = Var(within=Integers,bounds=(0,6),initialize=0)

m.obj = Objective(expr=   0.1*m.b26 + 0.2*m.b27 + 0.3*m.b28 + 0.4*m.b29 + 0.5*m.b30 + m.i31 + m.i32 + m.i33 + m.i34
                        + m.i35, sense=minimize)

m.c2 = Constraint(expr=m.i31*m.i1 + m.i32*m.i2 + m.i33*m.i3 + m.i34*m.i4 + m.i35*m.i5 >= 12)

m.c3 = Constraint(expr=m.i31*m.i6 + m.i32*m.i7 + m.i33*m.i8 + m.i34*m.i9 + m.i35*m.i10 >= 6)

m.c4 = Constraint(expr=m.i31*m.i11 + m.i32*m.i12 + m.i33*m.i13 + m.i34*m.i14 + m.i35*m.i15 >= 15)

m.c5 = Constraint(expr=m.i31*m.i16 + m.i32*m.i17 + m.i33*m.i18 + m.i34*m.i19 + m.i35*m.i20 >= 6)

m.c6 = Constraint(expr=m.i31*m.i21 + m.i32*m.i22 + m.i33*m.i23 + m.i34*m.i24 + m.i35*m.i25 >= 9)

m.c7 = Constraint(expr= - 330*m.i1 - 360*m.i6 - 370*m.i11 - 415*m.i16 - 435*m.i21 + 1800*m.b26 <= 0)

m.c8 = Constraint(expr= - 330*m.i2 - 360*m.i7 - 370*m.i12 - 415*m.i17 - 435*m.i22 + 1800*m.b27 <= 0)

m.c9 = Constraint(expr= - 330*m.i3 - 360*m.i8 - 370*m.i13 - 415*m.i18 - 435*m.i23 + 1800*m.b28 <= 0)

m.c10 = Constraint(expr= - 330*m.i4 - 360*m.i9 - 370*m.i14 - 415*m.i19 - 435*m.i24 + 1800*m.b29 <= 0)

m.c11 = Constraint(expr= - 330*m.i5 - 360*m.i10 - 370*m.i15 - 415*m.i20 - 435*m.i25 + 1800*m.b30 <= 0)

m.c12 = Constraint(expr=   330*m.i1 + 360*m.i6 + 370*m.i11 + 415*m.i16 + 435*m.i21 - 2000*m.b26 <= 0)

m.c13 = Constraint(expr=   330*m.i2 + 360*m.i7 + 370*m.i12 + 415*m.i17 + 435*m.i22 - 2000*m.b27 <= 0)

m.c14 = Constraint(expr=   330*m.i3 + 360*m.i8 + 370*m.i13 + 415*m.i18 + 435*m.i23 - 2000*m.b28 <= 0)

m.c15 = Constraint(expr=   330*m.i4 + 360*m.i9 + 370*m.i14 + 415*m.i19 + 435*m.i24 - 2000*m.b29 <= 0)

m.c16 = Constraint(expr=   330*m.i5 + 360*m.i10 + 370*m.i15 + 415*m.i20 + 435*m.i25 - 2000*m.b30 <= 0)

m.c17 = Constraint(expr= - m.i1 - m.i6 - m.i11 - m.i16 - m.i21 + m.b26 <= 0)

m.c18 = Constraint(expr= - m.i2 - m.i7 - m.i12 - m.i17 - m.i22 + m.b27 <= 0)

m.c19 = Constraint(expr= - m.i3 - m.i8 - m.i13 - m.i18 - m.i23 + m.b28 <= 0)

m.c20 = Constraint(expr= - m.i4 - m.i9 - m.i14 - m.i19 - m.i24 + m.b29 <= 0)

m.c21 = Constraint(expr= - m.i5 - m.i10 - m.i15 - m.i20 - m.i25 + m.b30 <= 0)

m.c22 = Constraint(expr=   m.i1 + m.i6 + m.i11 + m.i16 + m.i21 - 5*m.b26 <= 0)

m.c23 = Constraint(expr=   m.i2 + m.i7 + m.i12 + m.i17 + m.i22 - 5*m.b27 <= 0)

m.c24 = Constraint(expr=   m.i3 + m.i8 + m.i13 + m.i18 + m.i23 - 5*m.b28 <= 0)

m.c25 = Constraint(expr=   m.i4 + m.i9 + m.i14 + m.i19 + m.i24 - 5*m.b29 <= 0)

m.c26 = Constraint(expr=   m.i5 + m.i10 + m.i15 + m.i20 + m.i25 - 5*m.b30 <= 0)

m.c27 = Constraint(expr=   m.b26 - m.i31 <= 0)

m.c28 = Constraint(expr=   m.b27 - m.i32 <= 0)

m.c29 = Constraint(expr=   m.b28 - m.i33 <= 0)

m.c30 = Constraint(expr=   m.b29 - m.i34 <= 0)

m.c31 = Constraint(expr=   m.b30 - m.i35 <= 0)

m.c32 = Constraint(expr= - 15*m.b26 + m.i31 <= 0)

m.c33 = Constraint(expr= - 12*m.b27 + m.i32 <= 0)

m.c34 = Constraint(expr= - 9*m.b28 + m.i33 <= 0)

m.c35 = Constraint(expr= - 6*m.b29 + m.i34 <= 0)

m.c36 = Constraint(expr= - 6*m.b30 + m.i35 <= 0)

m.c37 = Constraint(expr=   m.i31 + m.i32 + m.i33 + m.i34 + m.i35 >= 10)

m.c38 = Constraint(expr= - m.b26 + m.b27 <= 0)

m.c39 = Constraint(expr= - m.b27 + m.b28 <= 0)

m.c40 = Constraint(expr= - m.b28 + m.b29 <= 0)

m.c41 = Constraint(expr= - m.b29 + m.b30 <= 0)

m.c42 = Constraint(expr= - m.i31 + m.i32 <= 0)

m.c43 = Constraint(expr= - m.i32 + m.i33 <= 0)

m.c44 = Constraint(expr= - m.i33 + m.i34 <= 0)

m.c45 = Constraint(expr= - m.i34 + m.i35 <= 0)
