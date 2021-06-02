#  MINLP written by GAMS Convert at 04/21/18 13:51:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         54        1        7       46        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         49        1        6       42        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        302      230       72        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i2 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i3 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i4 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i5 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i6 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i7 = Var(within=Integers,bounds=(0,5),initialize=2)
m.i8 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i9 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i10 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i11 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i12 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i13 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i14 = Var(within=Integers,bounds=(0,5),initialize=2)
m.i15 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i16 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i17 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i18 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i19 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i20 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i21 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i22 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i23 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i24 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i25 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i26 = Var(within=Integers,bounds=(0,5),initialize=2)
m.i27 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i28 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i29 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i30 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i31 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i32 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i33 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i34 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i35 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i36 = Var(within=Integers,bounds=(0,5),initialize=0)
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b38 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b39 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b40 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b41 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b42 = Var(within=Binary,bounds=(0,1),initialize=0)
m.i43 = Var(within=Integers,bounds=(0,15),initialize=8)
m.i44 = Var(within=Integers,bounds=(0,12),initialize=7)
m.i45 = Var(within=Integers,bounds=(0,8),initialize=0)
m.i46 = Var(within=Integers,bounds=(0,7),initialize=0)
m.i47 = Var(within=Integers,bounds=(0,4),initialize=0)
m.i48 = Var(within=Integers,bounds=(0,2),initialize=0)

m.obj = Objective(expr=   0.1*m.b37 + 0.2*m.b38 + 0.3*m.b39 + 0.4*m.b40 + 0.5*m.b41 + m.i43 + m.i44 + m.i45 + m.i46
                        + m.i47 + m.i48, sense=minimize)

m.c2 = Constraint(expr=m.i43*m.i1 + m.i44*m.i2 + m.i45*m.i3 + m.i46*m.i4 + m.i47*m.i5 + m.i48*m.i6 >= 8)

m.c3 = Constraint(expr=m.i43*m.i7 + m.i44*m.i8 + m.i45*m.i9 + m.i46*m.i10 + m.i47*m.i11 + m.i48*m.i12 >= 16)

m.c4 = Constraint(expr=m.i43*m.i13 + m.i44*m.i14 + m.i45*m.i15 + m.i46*m.i16 + m.i47*m.i17 + m.i48*m.i18 >= 12)

m.c5 = Constraint(expr=m.i43*m.i19 + m.i44*m.i20 + m.i45*m.i21 + m.i46*m.i22 + m.i47*m.i23 + m.i48*m.i24 >= 7)

m.c6 = Constraint(expr=m.i43*m.i25 + m.i44*m.i26 + m.i45*m.i27 + m.i46*m.i28 + m.i47*m.i29 + m.i48*m.i30 >= 14)

m.c7 = Constraint(expr=m.i43*m.i31 + m.i44*m.i32 + m.i45*m.i33 + m.i46*m.i34 + m.i47*m.i35 + m.i48*m.i36 >= 16)

m.c8 = Constraint(expr= - 330*m.i1 - 360*m.i7 - 380*m.i13 - 430*m.i19 - 490*m.i25 - 530*m.i31 + 2100*m.b37 <= 0)

m.c9 = Constraint(expr= - 330*m.i2 - 360*m.i8 - 380*m.i14 - 430*m.i20 - 490*m.i26 - 530*m.i32 + 2100*m.b38 <= 0)

m.c10 = Constraint(expr= - 330*m.i3 - 360*m.i9 - 380*m.i15 - 430*m.i21 - 490*m.i27 - 530*m.i33 + 2100*m.b39 <= 0)

m.c11 = Constraint(expr= - 330*m.i4 - 360*m.i10 - 380*m.i16 - 430*m.i22 - 490*m.i28 - 530*m.i34 + 2100*m.b40 <= 0)

m.c12 = Constraint(expr= - 330*m.i5 - 360*m.i11 - 380*m.i17 - 430*m.i23 - 490*m.i29 - 530*m.i35 + 2100*m.b41 <= 0)

m.c13 = Constraint(expr= - 330*m.i6 - 360*m.i12 - 380*m.i18 - 430*m.i24 - 490*m.i30 - 530*m.i36 + 2100*m.b42 <= 0)

m.c14 = Constraint(expr=   330*m.i1 + 360*m.i7 + 380*m.i13 + 430*m.i19 + 490*m.i25 + 530*m.i31 - 2200*m.b37 <= 0)

m.c15 = Constraint(expr=   330*m.i2 + 360*m.i8 + 380*m.i14 + 430*m.i20 + 490*m.i26 + 530*m.i32 - 2200*m.b38 <= 0)

m.c16 = Constraint(expr=   330*m.i3 + 360*m.i9 + 380*m.i15 + 430*m.i21 + 490*m.i27 + 530*m.i33 - 2200*m.b39 <= 0)

m.c17 = Constraint(expr=   330*m.i4 + 360*m.i10 + 380*m.i16 + 430*m.i22 + 490*m.i28 + 530*m.i34 - 2200*m.b40 <= 0)

m.c18 = Constraint(expr=   330*m.i5 + 360*m.i11 + 380*m.i17 + 430*m.i23 + 490*m.i29 + 530*m.i35 - 2200*m.b41 <= 0)

m.c19 = Constraint(expr=   330*m.i6 + 360*m.i12 + 380*m.i18 + 430*m.i24 + 490*m.i30 + 530*m.i36 - 2200*m.b42 <= 0)

m.c20 = Constraint(expr= - m.i1 - m.i7 - m.i13 - m.i19 - m.i25 - m.i31 + m.b37 <= 0)

m.c21 = Constraint(expr= - m.i2 - m.i8 - m.i14 - m.i20 - m.i26 - m.i32 + m.b38 <= 0)

m.c22 = Constraint(expr= - m.i3 - m.i9 - m.i15 - m.i21 - m.i27 - m.i33 + m.b39 <= 0)

m.c23 = Constraint(expr= - m.i4 - m.i10 - m.i16 - m.i22 - m.i28 - m.i34 + m.b40 <= 0)

m.c24 = Constraint(expr= - m.i5 - m.i11 - m.i17 - m.i23 - m.i29 - m.i35 + m.b41 <= 0)

m.c25 = Constraint(expr= - m.i6 - m.i12 - m.i18 - m.i24 - m.i30 - m.i36 + m.b42 <= 0)

m.c26 = Constraint(expr=   m.i1 + m.i7 + m.i13 + m.i19 + m.i25 + m.i31 - 5*m.b37 <= 0)

m.c27 = Constraint(expr=   m.i2 + m.i8 + m.i14 + m.i20 + m.i26 + m.i32 - 5*m.b38 <= 0)

m.c28 = Constraint(expr=   m.i3 + m.i9 + m.i15 + m.i21 + m.i27 + m.i33 - 5*m.b39 <= 0)

m.c29 = Constraint(expr=   m.i4 + m.i10 + m.i16 + m.i22 + m.i28 + m.i34 - 5*m.b40 <= 0)

m.c30 = Constraint(expr=   m.i5 + m.i11 + m.i17 + m.i23 + m.i29 + m.i35 - 5*m.b41 <= 0)

m.c31 = Constraint(expr=   m.i6 + m.i12 + m.i18 + m.i24 + m.i30 + m.i36 - 5*m.b42 <= 0)

m.c32 = Constraint(expr=   m.b37 - m.i43 <= 0)

m.c33 = Constraint(expr=   m.b38 - m.i44 <= 0)

m.c34 = Constraint(expr=   m.b39 - m.i45 <= 0)

m.c35 = Constraint(expr=   m.b40 - m.i46 <= 0)

m.c36 = Constraint(expr=   m.b41 - m.i47 <= 0)

m.c37 = Constraint(expr=   m.b42 - m.i48 <= 0)

m.c38 = Constraint(expr= - 15*m.b37 + m.i43 <= 0)

m.c39 = Constraint(expr= - 12*m.b38 + m.i44 <= 0)

m.c40 = Constraint(expr= - 8*m.b39 + m.i45 <= 0)

m.c41 = Constraint(expr= - 7*m.b40 + m.i46 <= 0)

m.c42 = Constraint(expr= - 4*m.b41 + m.i47 <= 0)

m.c43 = Constraint(expr= - 2*m.b42 + m.i48 <= 0)

m.c44 = Constraint(expr=   m.i43 + m.i44 + m.i45 + m.i46 + m.i47 + m.i48 >= 16)

m.c45 = Constraint(expr= - m.b37 + m.b38 <= 0)

m.c46 = Constraint(expr= - m.b38 + m.b39 <= 0)

m.c47 = Constraint(expr= - m.b39 + m.b40 <= 0)

m.c48 = Constraint(expr= - m.b40 + m.b41 <= 0)

m.c49 = Constraint(expr= - m.b41 + m.b42 <= 0)

m.c50 = Constraint(expr= - m.i43 + m.i44 <= 0)

m.c51 = Constraint(expr= - m.i44 + m.i45 <= 0)

m.c52 = Constraint(expr= - m.i45 + m.i46 <= 0)

m.c53 = Constraint(expr= - m.i46 + m.i47 <= 0)

m.c54 = Constraint(expr= - m.i47 + m.i48 <= 0)
