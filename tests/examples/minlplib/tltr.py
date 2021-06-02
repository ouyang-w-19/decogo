#  MINLP written by GAMS Convert at 04/21/18 13:54:54
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         55        1        3       51        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         49        1       12       36        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        228      174       54        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.i4 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i5 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i6 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i7 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i8 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i9 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i10 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i11 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i12 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i13 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i14 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i15 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i16 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i17 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i18 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i19 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i20 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i21 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i22 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i23 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i24 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i25 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i26 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i27 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i28 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i29 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i30 = Var(within=Integers,bounds=(0,5),initialize=0)
m.b31 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b32 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b33 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b34 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b35 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b36 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b38 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b39 = Var(within=Binary,bounds=(0,1),initialize=0)
m.i40 = Var(within=Integers,bounds=(0,100),initialize=15)
m.i41 = Var(within=Integers,bounds=(0,100),initialize=80)
m.i42 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i43 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i44 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i45 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i46 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i47 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i48 = Var(within=Integers,bounds=(0,100),initialize=0)

m.obj = Objective(expr=   35*m.b2 + 35*m.b3 + 6.53333333333333*m.b31 + 6.53333333333333*m.b32 + 6.7375*m.b33
                        + 6.53333333333333*m.b34 + 6.53333333333333*m.b35 + 6.7375*m.b36 + 6.53333333333333*m.b37
                        + 6.53333333333333*m.b38 + 6.7375*m.b39, sense=minimize)

m.c2 = Constraint(expr=m.i40*m.i4 + m.i43*m.i7 + m.i46*m.i10 + m.i41*m.i5 + m.i44*m.i8 + m.i47*m.i11 + m.i42*m.i6 + 
                       m.i45*m.i9 + m.i48*m.i12 >= 9)

m.c3 = Constraint(expr=m.i40*m.i13 + m.i43*m.i16 + m.i46*m.i19 + m.i41*m.i14 + m.i44*m.i17 + m.i47*m.i20 + m.i42*m.i15
                        + m.i45*m.i18 + m.i48*m.i21 >= 15)

m.c4 = Constraint(expr=m.i40*m.i22 + m.i43*m.i25 + m.i46*m.i28 + m.i41*m.i23 + m.i44*m.i26 + m.i47*m.i29 + m.i42*m.i24
                        + m.i45*m.i27 + m.i48*m.i30 >= 80)

m.c5 = Constraint(expr=   12*m.i4 + 24*m.i13 + 36*m.i22 - 48*m.b31 <= 0)

m.c6 = Constraint(expr=   12*m.i5 + 24*m.i14 + 36*m.i23 - 48*m.b32 <= 0)

m.c7 = Constraint(expr=   12*m.i6 + 24*m.i15 + 36*m.i24 - 62*m.b33 <= 0)

m.c8 = Constraint(expr=   12*m.i7 + 24*m.i16 + 36*m.i25 - 48*m.b34 <= 0)

m.c9 = Constraint(expr=   12*m.i8 + 24*m.i17 + 36*m.i26 - 48*m.b35 <= 0)

m.c10 = Constraint(expr=   12*m.i9 + 24*m.i18 + 36*m.i27 - 62*m.b36 <= 0)

m.c11 = Constraint(expr=   12*m.i10 + 24*m.i19 + 36*m.i28 - 48*m.b37 <= 0)

m.c12 = Constraint(expr=   12*m.i11 + 24*m.i20 + 36*m.i29 - 48*m.b38 <= 0)

m.c13 = Constraint(expr=   12*m.i12 + 24*m.i21 + 36*m.i30 - 62*m.b39 <= 0)

m.c14 = Constraint(expr= - m.i4 - m.i13 - m.i22 + m.b31 <= 0)

m.c15 = Constraint(expr= - m.i5 - m.i14 - m.i23 + m.b32 <= 0)

m.c16 = Constraint(expr= - m.i6 - m.i15 - m.i24 + m.b33 <= 0)

m.c17 = Constraint(expr= - m.i7 - m.i16 - m.i25 + m.b34 <= 0)

m.c18 = Constraint(expr= - m.i8 - m.i17 - m.i26 + m.b35 <= 0)

m.c19 = Constraint(expr= - m.i9 - m.i18 - m.i27 + m.b36 <= 0)

m.c20 = Constraint(expr= - m.i10 - m.i19 - m.i28 + m.b37 <= 0)

m.c21 = Constraint(expr= - m.i11 - m.i20 - m.i29 + m.b38 <= 0)

m.c22 = Constraint(expr= - m.i12 - m.i21 - m.i30 + m.b39 <= 0)

m.c23 = Constraint(expr= - 72*m.b31 + m.i40 <= 0)

m.c24 = Constraint(expr= - 182*m.b32 + m.i41 <= 0)

m.c25 = Constraint(expr= - 182*m.b33 + m.i42 <= 0)

m.c26 = Constraint(expr= - 72*m.b34 + m.i43 <= 0)

m.c27 = Constraint(expr= - 182*m.b35 + m.i44 <= 0)

m.c28 = Constraint(expr= - 182*m.b36 + m.i45 <= 0)

m.c29 = Constraint(expr= - 72*m.b37 + m.i46 <= 0)

m.c30 = Constraint(expr= - 182*m.b38 + m.i47 <= 0)

m.c31 = Constraint(expr= - 182*m.b39 + m.i48 <= 0)

m.c32 = Constraint(expr=   m.i4 + m.i13 + m.i22 - 5*m.b31 <= 0)

m.c33 = Constraint(expr=   m.i5 + m.i14 + m.i23 - 5*m.b32 <= 0)

m.c34 = Constraint(expr=   m.i6 + m.i15 + m.i24 - 5*m.b33 <= 0)

m.c35 = Constraint(expr=   m.i7 + m.i16 + m.i25 - 5*m.b34 <= 0)

m.c36 = Constraint(expr=   m.i8 + m.i17 + m.i26 - 5*m.b35 <= 0)

m.c37 = Constraint(expr=   m.i9 + m.i18 + m.i27 - 5*m.b36 <= 0)

m.c38 = Constraint(expr=   m.i10 + m.i19 + m.i28 - 5*m.b37 <= 0)

m.c39 = Constraint(expr=   m.i11 + m.i20 + m.i29 - 5*m.b38 <= 0)

m.c40 = Constraint(expr=   m.i12 + m.i21 + m.i30 - 5*m.b39 <= 0)

m.c41 = Constraint(expr= - 500*m.b1 + 7*m.i40 + 7*m.i43 + 7*m.i46 <= 0)

m.c42 = Constraint(expr= - 1270*m.b2 + 7*m.i41 + 7*m.i44 + 7*m.i47 <= 0)

m.c43 = Constraint(expr= - 1270*m.b3 + 7*m.i42 + 7*m.i45 + 7*m.i48 <= 0)

m.c44 = Constraint(expr= - m.b31 + m.b34 <= 0)

m.c45 = Constraint(expr= - m.b32 + m.b35 <= 0)

m.c46 = Constraint(expr= - m.b33 + m.b36 <= 0)

m.c47 = Constraint(expr= - m.b34 + m.b37 <= 0)

m.c48 = Constraint(expr= - m.b35 + m.b38 <= 0)

m.c49 = Constraint(expr= - m.b36 + m.b39 <= 0)

m.c50 = Constraint(expr= - m.i40 + m.i43 <= 0)

m.c51 = Constraint(expr= - m.i41 + m.i44 <= 0)

m.c52 = Constraint(expr= - m.i42 + m.i45 <= 0)

m.c53 = Constraint(expr= - m.i43 + m.i46 <= 0)

m.c54 = Constraint(expr= - m.i44 + m.i47 <= 0)

m.c55 = Constraint(expr= - m.i45 + m.i48 <= 0)
