#  MINLP written by GAMS Convert at 04/21/18 13:54:54
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         25        1        0       24        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         25        1        4       20        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        105       73       32        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.i5 = Var(within=Integers,bounds=(0,12),initialize=1)
m.i6 = Var(within=Integers,bounds=(0,12),initialize=1)
m.i7 = Var(within=Integers,bounds=(0,12),initialize=1)
m.i8 = Var(within=Integers,bounds=(0,12),initialize=1)
m.i9 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i10 = Var(within=Integers,bounds=(0,5),initialize=1)
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

m.obj = Objective(expr=   0.1*m.b1 + 0.2*m.b2 + 0.3*m.b3 + 0.4*m.b4 + m.i5 + m.i6 + m.i7 + m.i8, sense=minimize)

m.c2 = Constraint(expr=   330*m.i9 + 360*m.i13 + 385*m.i17 + 415*m.i21 <= 1900)

m.c3 = Constraint(expr=   330*m.i10 + 360*m.i14 + 385*m.i18 + 415*m.i22 <= 1900)

m.c4 = Constraint(expr=   330*m.i11 + 360*m.i15 + 385*m.i19 + 415*m.i23 <= 1900)

m.c5 = Constraint(expr=   330*m.i12 + 360*m.i16 + 385*m.i20 + 415*m.i24 <= 1900)

m.c6 = Constraint(expr= - 330*m.i9 - 360*m.i13 - 385*m.i17 - 415*m.i21 <= -1700)

m.c7 = Constraint(expr= - 330*m.i10 - 360*m.i14 - 385*m.i18 - 415*m.i22 <= -1700)

m.c8 = Constraint(expr= - 330*m.i11 - 360*m.i15 - 385*m.i19 - 415*m.i23 <= -1700)

m.c9 = Constraint(expr= - 330*m.i12 - 360*m.i16 - 385*m.i20 - 415*m.i24 <= -1700)

m.c10 = Constraint(expr=   m.i9 + m.i13 + m.i17 + m.i21 <= 5)

m.c11 = Constraint(expr=   m.i10 + m.i14 + m.i18 + m.i22 <= 5)

m.c12 = Constraint(expr=   m.i11 + m.i15 + m.i19 + m.i23 <= 5)

m.c13 = Constraint(expr=   m.i12 + m.i16 + m.i20 + m.i24 <= 5)

m.c14 = Constraint(expr=   m.b1 - m.i5 <= 0)

m.c15 = Constraint(expr=   m.b2 - m.i6 <= 0)

m.c16 = Constraint(expr=   m.b3 - m.i7 <= 0)

m.c17 = Constraint(expr=   m.b4 - m.i8 <= 0)

m.c18 = Constraint(expr= - 12*m.b1 + m.i5 <= 0)

m.c19 = Constraint(expr= - 12*m.b2 + m.i6 <= 0)

m.c20 = Constraint(expr= - 12*m.b3 + m.i7 <= 0)

m.c21 = Constraint(expr= - 12*m.b4 + m.i8 <= 0)

m.c22 = Constraint(expr=-(m.i5*m.i9 + m.i6*m.i10 + m.i7*m.i11 + m.i8*m.i12) <= -8)

m.c23 = Constraint(expr=-(m.i5*m.i13 + m.i6*m.i14 + m.i7*m.i15 + m.i8*m.i16) <= -7)

m.c24 = Constraint(expr=-(m.i5*m.i17 + m.i6*m.i18 + m.i7*m.i19 + m.i8*m.i20) <= -12)

m.c25 = Constraint(expr=-(m.i5*m.i21 + m.i6*m.i22 + m.i7*m.i23 + m.i8*m.i24) <= -11)
