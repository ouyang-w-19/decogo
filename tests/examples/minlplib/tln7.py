#  MINLP written by GAMS Convert at 04/21/18 13:54:54
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         43        1        0       42        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         64        1        7       56        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        288      190       98        0
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
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)
m.i8 = Var(within=Integers,bounds=(0,15),initialize=1)
m.i9 = Var(within=Integers,bounds=(0,15),initialize=1)
m.i10 = Var(within=Integers,bounds=(0,15),initialize=1)
m.i11 = Var(within=Integers,bounds=(0,15),initialize=1)
m.i12 = Var(within=Integers,bounds=(0,15),initialize=1)
m.i13 = Var(within=Integers,bounds=(0,15),initialize=1)
m.i14 = Var(within=Integers,bounds=(0,15),initialize=1)
m.i15 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i16 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i17 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i18 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i19 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i20 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i21 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i22 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i23 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i24 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i25 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i26 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i27 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i28 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i29 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i30 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i31 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i32 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i33 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i34 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i35 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i36 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i37 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i38 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i39 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i40 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i41 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i42 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i43 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i44 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i45 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i46 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i47 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i48 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i49 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i50 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i51 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i52 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i53 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i54 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i55 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i56 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i57 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i58 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i59 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i60 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i61 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i62 = Var(within=Integers,bounds=(0,6),initialize=1)
m.i63 = Var(within=Integers,bounds=(0,6),initialize=1)

m.obj = Objective(expr=   0.1*m.b1 + 0.2*m.b2 + 0.3*m.b3 + 0.4*m.b4 + 0.5*m.b5 + 0.6*m.b6 + 0.7*m.b7 + m.i8 + m.i9
                        + m.i10 + m.i11 + m.i12 + m.i13 + m.i14, sense=minimize)

m.c2 = Constraint(expr=   550*m.i15 + 630*m.i22 + 685*m.i29 + 720*m.i36 + 760*m.i43 + 810*m.i50 + 850*m.i57 <= 3400)

m.c3 = Constraint(expr=   550*m.i16 + 630*m.i23 + 685*m.i30 + 720*m.i37 + 760*m.i44 + 810*m.i51 + 850*m.i58 <= 3400)

m.c4 = Constraint(expr=   550*m.i17 + 630*m.i24 + 685*m.i31 + 720*m.i38 + 760*m.i45 + 810*m.i52 + 850*m.i59 <= 3400)

m.c5 = Constraint(expr=   550*m.i18 + 630*m.i25 + 685*m.i32 + 720*m.i39 + 760*m.i46 + 810*m.i53 + 850*m.i60 <= 3400)

m.c6 = Constraint(expr=   550*m.i19 + 630*m.i26 + 685*m.i33 + 720*m.i40 + 760*m.i47 + 810*m.i54 + 850*m.i61 <= 3400)

m.c7 = Constraint(expr=   550*m.i20 + 630*m.i27 + 685*m.i34 + 720*m.i41 + 760*m.i48 + 810*m.i55 + 850*m.i62 <= 3400)

m.c8 = Constraint(expr=   550*m.i21 + 630*m.i28 + 685*m.i35 + 720*m.i42 + 760*m.i49 + 810*m.i56 + 850*m.i63 <= 3400)

m.c9 = Constraint(expr= - 550*m.i15 - 630*m.i22 - 685*m.i29 - 720*m.i36 - 760*m.i43 - 810*m.i50 - 850*m.i57 <= -3200)

m.c10 = Constraint(expr= - 550*m.i16 - 630*m.i23 - 685*m.i30 - 720*m.i37 - 760*m.i44 - 810*m.i51 - 850*m.i58 <= -3200)

m.c11 = Constraint(expr= - 550*m.i17 - 630*m.i24 - 685*m.i31 - 720*m.i38 - 760*m.i45 - 810*m.i52 - 850*m.i59 <= -3200)

m.c12 = Constraint(expr= - 550*m.i18 - 630*m.i25 - 685*m.i32 - 720*m.i39 - 760*m.i46 - 810*m.i53 - 850*m.i60 <= -3200)

m.c13 = Constraint(expr= - 550*m.i19 - 630*m.i26 - 685*m.i33 - 720*m.i40 - 760*m.i47 - 810*m.i54 - 850*m.i61 <= -3200)

m.c14 = Constraint(expr= - 550*m.i20 - 630*m.i27 - 685*m.i34 - 720*m.i41 - 760*m.i48 - 810*m.i55 - 850*m.i62 <= -3200)

m.c15 = Constraint(expr= - 550*m.i21 - 630*m.i28 - 685*m.i35 - 720*m.i42 - 760*m.i49 - 810*m.i56 - 850*m.i63 <= -3200)

m.c16 = Constraint(expr=   m.i15 + m.i22 + m.i29 + m.i36 + m.i43 + m.i50 + m.i57 <= 6)

m.c17 = Constraint(expr=   m.i16 + m.i23 + m.i30 + m.i37 + m.i44 + m.i51 + m.i58 <= 6)

m.c18 = Constraint(expr=   m.i17 + m.i24 + m.i31 + m.i38 + m.i45 + m.i52 + m.i59 <= 6)

m.c19 = Constraint(expr=   m.i18 + m.i25 + m.i32 + m.i39 + m.i46 + m.i53 + m.i60 <= 6)

m.c20 = Constraint(expr=   m.i19 + m.i26 + m.i33 + m.i40 + m.i47 + m.i54 + m.i61 <= 6)

m.c21 = Constraint(expr=   m.i20 + m.i27 + m.i34 + m.i41 + m.i48 + m.i55 + m.i62 <= 6)

m.c22 = Constraint(expr=   m.i21 + m.i28 + m.i35 + m.i42 + m.i49 + m.i56 + m.i63 <= 6)

m.c23 = Constraint(expr=   m.b1 - m.i8 <= 0)

m.c24 = Constraint(expr=   m.b2 - m.i9 <= 0)

m.c25 = Constraint(expr=   m.b3 - m.i10 <= 0)

m.c26 = Constraint(expr=   m.b4 - m.i11 <= 0)

m.c27 = Constraint(expr=   m.b5 - m.i12 <= 0)

m.c28 = Constraint(expr=   m.b6 - m.i13 <= 0)

m.c29 = Constraint(expr=   m.b7 - m.i14 <= 0)

m.c30 = Constraint(expr= - 15*m.b1 + m.i8 <= 0)

m.c31 = Constraint(expr= - 15*m.b2 + m.i9 <= 0)

m.c32 = Constraint(expr= - 15*m.b3 + m.i10 <= 0)

m.c33 = Constraint(expr= - 15*m.b4 + m.i11 <= 0)

m.c34 = Constraint(expr= - 15*m.b5 + m.i12 <= 0)

m.c35 = Constraint(expr= - 15*m.b6 + m.i13 <= 0)

m.c36 = Constraint(expr= - 15*m.b7 + m.i14 <= 0)

m.c37 = Constraint(expr=-(m.i8*m.i15 + m.i9*m.i16 + m.i10*m.i17 + m.i11*m.i18 + m.i12*m.i19 + m.i13*m.i20 + m.i14*m.i21)
                         <= -8)

m.c38 = Constraint(expr=-(m.i8*m.i22 + m.i9*m.i23 + m.i10*m.i24 + m.i11*m.i25 + m.i12*m.i26 + m.i13*m.i27 + m.i14*m.i28)
                         <= -11)

m.c39 = Constraint(expr=-(m.i8*m.i29 + m.i9*m.i30 + m.i10*m.i31 + m.i11*m.i32 + m.i12*m.i33 + m.i13*m.i34 + m.i14*m.i35)
                         <= -15)

m.c40 = Constraint(expr=-(m.i8*m.i36 + m.i9*m.i37 + m.i10*m.i38 + m.i11*m.i39 + m.i12*m.i40 + m.i13*m.i41 + m.i14*m.i42)
                         <= -5)

m.c41 = Constraint(expr=-(m.i8*m.i43 + m.i9*m.i44 + m.i10*m.i45 + m.i11*m.i46 + m.i12*m.i47 + m.i13*m.i48 + m.i14*m.i49)
                         <= -8)

m.c42 = Constraint(expr=-(m.i8*m.i50 + m.i9*m.i51 + m.i10*m.i52 + m.i11*m.i53 + m.i12*m.i54 + m.i13*m.i55 + m.i14*m.i56)
                         <= -12)

m.c43 = Constraint(expr=-(m.i8*m.i57 + m.i9*m.i58 + m.i10*m.i59 + m.i11*m.i60 + m.i12*m.i61 + m.i13*m.i62 + m.i14*m.i63)
                         <= -6)
