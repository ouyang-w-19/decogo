#  MINLP written by GAMS Convert at 04/21/18 13:54:54
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         31        1        0       30        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         36        1        5       30        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        156      106       50        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)
m.i6 = Var(within=Integers,bounds=(0,15),initialize=1)
m.i7 = Var(within=Integers,bounds=(0,15),initialize=1)
m.i8 = Var(within=Integers,bounds=(0,15),initialize=1)
m.i9 = Var(within=Integers,bounds=(0,15),initialize=1)
m.i10 = Var(within=Integers,bounds=(0,15),initialize=1)
m.i11 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i12 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i13 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i14 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i15 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i16 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i17 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i18 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i19 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i20 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i21 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i22 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i23 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i24 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i25 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i26 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i27 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i28 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i29 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i30 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i31 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i32 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i33 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i34 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i35 = Var(within=Integers,bounds=(0,5),initialize=1)

m.obj = Objective(expr=   0.1*m.b1 + 0.2*m.b2 + 0.3*m.b3 + 0.4*m.b4 + 0.5*m.b5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10
                       , sense=minimize)

m.c2 = Constraint(expr=   330*m.i11 + 360*m.i16 + 370*m.i21 + 415*m.i26 + 435*m.i31 <= 2000)

m.c3 = Constraint(expr=   330*m.i12 + 360*m.i17 + 370*m.i22 + 415*m.i27 + 435*m.i32 <= 2000)

m.c4 = Constraint(expr=   330*m.i13 + 360*m.i18 + 370*m.i23 + 415*m.i28 + 435*m.i33 <= 2000)

m.c5 = Constraint(expr=   330*m.i14 + 360*m.i19 + 370*m.i24 + 415*m.i29 + 435*m.i34 <= 2000)

m.c6 = Constraint(expr=   330*m.i15 + 360*m.i20 + 370*m.i25 + 415*m.i30 + 435*m.i35 <= 2000)

m.c7 = Constraint(expr= - 330*m.i11 - 360*m.i16 - 370*m.i21 - 415*m.i26 - 435*m.i31 <= -1800)

m.c8 = Constraint(expr= - 330*m.i12 - 360*m.i17 - 370*m.i22 - 415*m.i27 - 435*m.i32 <= -1800)

m.c9 = Constraint(expr= - 330*m.i13 - 360*m.i18 - 370*m.i23 - 415*m.i28 - 435*m.i33 <= -1800)

m.c10 = Constraint(expr= - 330*m.i14 - 360*m.i19 - 370*m.i24 - 415*m.i29 - 435*m.i34 <= -1800)

m.c11 = Constraint(expr= - 330*m.i15 - 360*m.i20 - 370*m.i25 - 415*m.i30 - 435*m.i35 <= -1800)

m.c12 = Constraint(expr=   m.i11 + m.i16 + m.i21 + m.i26 + m.i31 <= 5)

m.c13 = Constraint(expr=   m.i12 + m.i17 + m.i22 + m.i27 + m.i32 <= 5)

m.c14 = Constraint(expr=   m.i13 + m.i18 + m.i23 + m.i28 + m.i33 <= 5)

m.c15 = Constraint(expr=   m.i14 + m.i19 + m.i24 + m.i29 + m.i34 <= 5)

m.c16 = Constraint(expr=   m.i15 + m.i20 + m.i25 + m.i30 + m.i35 <= 5)

m.c17 = Constraint(expr=   m.b1 - m.i6 <= 0)

m.c18 = Constraint(expr=   m.b2 - m.i7 <= 0)

m.c19 = Constraint(expr=   m.b3 - m.i8 <= 0)

m.c20 = Constraint(expr=   m.b4 - m.i9 <= 0)

m.c21 = Constraint(expr=   m.b5 - m.i10 <= 0)

m.c22 = Constraint(expr= - 15*m.b1 + m.i6 <= 0)

m.c23 = Constraint(expr= - 15*m.b2 + m.i7 <= 0)

m.c24 = Constraint(expr= - 15*m.b3 + m.i8 <= 0)

m.c25 = Constraint(expr= - 15*m.b4 + m.i9 <= 0)

m.c26 = Constraint(expr= - 15*m.b5 + m.i10 <= 0)

m.c27 = Constraint(expr=-(m.i6*m.i11 + m.i7*m.i12 + m.i8*m.i13 + m.i9*m.i14 + m.i10*m.i15) <= -12)

m.c28 = Constraint(expr=-(m.i6*m.i16 + m.i7*m.i17 + m.i8*m.i18 + m.i9*m.i19 + m.i10*m.i20) <= -6)

m.c29 = Constraint(expr=-(m.i6*m.i21 + m.i7*m.i22 + m.i8*m.i23 + m.i9*m.i24 + m.i10*m.i25) <= -15)

m.c30 = Constraint(expr=-(m.i6*m.i26 + m.i7*m.i27 + m.i8*m.i28 + m.i9*m.i29 + m.i10*m.i30) <= -6)

m.c31 = Constraint(expr=-(m.i6*m.i31 + m.i7*m.i32 + m.i8*m.i33 + m.i9*m.i34 + m.i10*m.i35) <= -9)
