#  MINLP written by GAMS Convert at 04/21/18 13:51:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         36        1        5       30        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         25        1        4       20        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        153      121       32        0
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
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b18 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b19 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=0)
m.i21 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i22 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i23 = Var(within=Integers,bounds=(0,9),initialize=0)
m.i24 = Var(within=Integers,bounds=(0,6),initialize=0)

m.obj = Objective(expr=   0.1*m.b17 + 0.2*m.b18 + 0.3*m.b19 + 0.4*m.b20 + m.i21 + m.i22 + m.i23 + m.i24, sense=minimize)

m.c2 = Constraint(expr=m.i21*m.i1 + m.i22*m.i2 + m.i23*m.i3 + m.i24*m.i4 >= 9)

m.c3 = Constraint(expr=m.i21*m.i5 + m.i22*m.i6 + m.i23*m.i7 + m.i24*m.i8 >= 7)

m.c4 = Constraint(expr=m.i21*m.i9 + m.i22*m.i10 + m.i23*m.i11 + m.i24*m.i12 >= 12)

m.c5 = Constraint(expr=m.i21*m.i13 + m.i22*m.i14 + m.i23*m.i15 + m.i24*m.i16 >= 11)

m.c6 = Constraint(expr= - 330*m.i1 - 360*m.i5 - 385*m.i9 - 415*m.i13 + 1700*m.b17 <= 0)

m.c7 = Constraint(expr= - 330*m.i2 - 360*m.i6 - 385*m.i10 - 415*m.i14 + 1700*m.b18 <= 0)

m.c8 = Constraint(expr= - 330*m.i3 - 360*m.i7 - 385*m.i11 - 415*m.i15 + 1700*m.b19 <= 0)

m.c9 = Constraint(expr= - 330*m.i4 - 360*m.i8 - 385*m.i12 - 415*m.i16 + 1700*m.b20 <= 0)

m.c10 = Constraint(expr=   330*m.i1 + 360*m.i5 + 385*m.i9 + 415*m.i13 - 1900*m.b17 <= 0)

m.c11 = Constraint(expr=   330*m.i2 + 360*m.i6 + 385*m.i10 + 415*m.i14 - 1900*m.b18 <= 0)

m.c12 = Constraint(expr=   330*m.i3 + 360*m.i7 + 385*m.i11 + 415*m.i15 - 1900*m.b19 <= 0)

m.c13 = Constraint(expr=   330*m.i4 + 360*m.i8 + 385*m.i12 + 415*m.i16 - 1900*m.b20 <= 0)

m.c14 = Constraint(expr= - m.i1 - m.i5 - m.i9 - m.i13 + m.b17 <= 0)

m.c15 = Constraint(expr= - m.i2 - m.i6 - m.i10 - m.i14 + m.b18 <= 0)

m.c16 = Constraint(expr= - m.i3 - m.i7 - m.i11 - m.i15 + m.b19 <= 0)

m.c17 = Constraint(expr= - m.i4 - m.i8 - m.i12 - m.i16 + m.b20 <= 0)

m.c18 = Constraint(expr=   m.i1 + m.i5 + m.i9 + m.i13 - 5*m.b17 <= 0)

m.c19 = Constraint(expr=   m.i2 + m.i6 + m.i10 + m.i14 - 5*m.b18 <= 0)

m.c20 = Constraint(expr=   m.i3 + m.i7 + m.i11 + m.i15 - 5*m.b19 <= 0)

m.c21 = Constraint(expr=   m.i4 + m.i8 + m.i12 + m.i16 - 5*m.b20 <= 0)

m.c22 = Constraint(expr=   m.b17 - m.i21 <= 0)

m.c23 = Constraint(expr=   m.b18 - m.i22 <= 0)

m.c24 = Constraint(expr=   m.b19 - m.i23 <= 0)

m.c25 = Constraint(expr=   m.b20 - m.i24 <= 0)

m.c26 = Constraint(expr= - 15*m.b17 + m.i21 <= 0)

m.c27 = Constraint(expr= - 12*m.b18 + m.i22 <= 0)

m.c28 = Constraint(expr= - 9*m.b19 + m.i23 <= 0)

m.c29 = Constraint(expr= - 6*m.b20 + m.i24 <= 0)

m.c30 = Constraint(expr=   m.i21 + m.i22 + m.i23 + m.i24 >= 8)

m.c31 = Constraint(expr= - m.b17 + m.b18 <= 0)

m.c32 = Constraint(expr= - m.b18 + m.b19 <= 0)

m.c33 = Constraint(expr= - m.b19 + m.b20 <= 0)

m.c34 = Constraint(expr= - m.i21 + m.i22 <= 0)

m.c35 = Constraint(expr= - m.i22 + m.i23 <= 0)

m.c36 = Constraint(expr= - m.i23 + m.i24 <= 0)
