#  MINLP written by GAMS Convert at 04/21/18 13:54:54
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         37        1        0       36        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         49        1        6       42        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        217      145       72        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0)
m.i7 = Var(within=Integers,bounds=(0,16),initialize=1)
m.i8 = Var(within=Integers,bounds=(0,16),initialize=1)
m.i9 = Var(within=Integers,bounds=(0,16),initialize=1)
m.i10 = Var(within=Integers,bounds=(0,16),initialize=1)
m.i11 = Var(within=Integers,bounds=(0,16),initialize=1)
m.i12 = Var(within=Integers,bounds=(0,16),initialize=1)
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
m.i36 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i37 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i38 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i39 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i40 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i41 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i42 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i43 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i44 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i45 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i46 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i47 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i48 = Var(within=Integers,bounds=(0,5),initialize=1)

m.obj = Objective(expr=   0.1*m.b1 + 0.2*m.b2 + 0.3*m.b3 + 0.4*m.b4 + 0.5*m.b5 + 0.6*m.b6 + m.i7 + m.i8 + m.i9 + m.i10
                        + m.i11 + m.i12, sense=minimize)

m.c2 = Constraint(expr=   330*m.i13 + 360*m.i19 + 380*m.i25 + 430*m.i31 + 490*m.i37 + 530*m.i43 <= 2200)

m.c3 = Constraint(expr=   330*m.i14 + 360*m.i20 + 380*m.i26 + 430*m.i32 + 490*m.i38 + 530*m.i44 <= 2200)

m.c4 = Constraint(expr=   330*m.i15 + 360*m.i21 + 380*m.i27 + 430*m.i33 + 490*m.i39 + 530*m.i45 <= 2200)

m.c5 = Constraint(expr=   330*m.i16 + 360*m.i22 + 380*m.i28 + 430*m.i34 + 490*m.i40 + 530*m.i46 <= 2200)

m.c6 = Constraint(expr=   330*m.i17 + 360*m.i23 + 380*m.i29 + 430*m.i35 + 490*m.i41 + 530*m.i47 <= 2200)

m.c7 = Constraint(expr=   330*m.i18 + 360*m.i24 + 380*m.i30 + 430*m.i36 + 490*m.i42 + 530*m.i48 <= 2200)

m.c8 = Constraint(expr= - 330*m.i13 - 360*m.i19 - 380*m.i25 - 430*m.i31 - 490*m.i37 - 530*m.i43 <= -2100)

m.c9 = Constraint(expr= - 330*m.i14 - 360*m.i20 - 380*m.i26 - 430*m.i32 - 490*m.i38 - 530*m.i44 <= -2100)

m.c10 = Constraint(expr= - 330*m.i15 - 360*m.i21 - 380*m.i27 - 430*m.i33 - 490*m.i39 - 530*m.i45 <= -2100)

m.c11 = Constraint(expr= - 330*m.i16 - 360*m.i22 - 380*m.i28 - 430*m.i34 - 490*m.i40 - 530*m.i46 <= -2100)

m.c12 = Constraint(expr= - 330*m.i17 - 360*m.i23 - 380*m.i29 - 430*m.i35 - 490*m.i41 - 530*m.i47 <= -2100)

m.c13 = Constraint(expr= - 330*m.i18 - 360*m.i24 - 380*m.i30 - 430*m.i36 - 490*m.i42 - 530*m.i48 <= -2100)

m.c14 = Constraint(expr=   m.i13 + m.i19 + m.i25 + m.i31 + m.i37 + m.i43 <= 5)

m.c15 = Constraint(expr=   m.i14 + m.i20 + m.i26 + m.i32 + m.i38 + m.i44 <= 5)

m.c16 = Constraint(expr=   m.i15 + m.i21 + m.i27 + m.i33 + m.i39 + m.i45 <= 5)

m.c17 = Constraint(expr=   m.i16 + m.i22 + m.i28 + m.i34 + m.i40 + m.i46 <= 5)

m.c18 = Constraint(expr=   m.i17 + m.i23 + m.i29 + m.i35 + m.i41 + m.i47 <= 5)

m.c19 = Constraint(expr=   m.i18 + m.i24 + m.i30 + m.i36 + m.i42 + m.i48 <= 5)

m.c20 = Constraint(expr=   m.b1 - m.i7 <= 0)

m.c21 = Constraint(expr=   m.b2 - m.i8 <= 0)

m.c22 = Constraint(expr=   m.b3 - m.i9 <= 0)

m.c23 = Constraint(expr=   m.b4 - m.i10 <= 0)

m.c24 = Constraint(expr=   m.b5 - m.i11 <= 0)

m.c25 = Constraint(expr=   m.b6 - m.i12 <= 0)

m.c26 = Constraint(expr= - 16*m.b1 + m.i7 <= 0)

m.c27 = Constraint(expr= - 16*m.b2 + m.i8 <= 0)

m.c28 = Constraint(expr= - 16*m.b3 + m.i9 <= 0)

m.c29 = Constraint(expr= - 16*m.b4 + m.i10 <= 0)

m.c30 = Constraint(expr= - 16*m.b5 + m.i11 <= 0)

m.c31 = Constraint(expr= - 16*m.b6 + m.i12 <= 0)

m.c32 = Constraint(expr=-(m.i7*m.i13 + m.i8*m.i14 + m.i9*m.i15 + m.i10*m.i16 + m.i11*m.i17 + m.i12*m.i18) <= -8)

m.c33 = Constraint(expr=-(m.i7*m.i19 + m.i8*m.i20 + m.i9*m.i21 + m.i10*m.i22 + m.i11*m.i23 + m.i12*m.i24) <= -16)

m.c34 = Constraint(expr=-(m.i7*m.i25 + m.i8*m.i26 + m.i9*m.i27 + m.i10*m.i28 + m.i11*m.i29 + m.i12*m.i30) <= -12)

m.c35 = Constraint(expr=-(m.i7*m.i31 + m.i8*m.i32 + m.i9*m.i33 + m.i10*m.i34 + m.i11*m.i35 + m.i12*m.i36) <= -7)

m.c36 = Constraint(expr=-(m.i7*m.i37 + m.i8*m.i38 + m.i9*m.i39 + m.i10*m.i40 + m.i11*m.i41 + m.i12*m.i42) <= -14)

m.c37 = Constraint(expr=-(m.i7*m.i43 + m.i8*m.i44 + m.i9*m.i45 + m.i10*m.i46 + m.i11*m.i47 + m.i12*m.i48) <= -16)
