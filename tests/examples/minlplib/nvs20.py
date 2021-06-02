#  MINLP written by GAMS Convert at 04/21/18 13:52:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          9        1        8        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         17       12        0        5        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         70       54       16        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,200),initialize=1)
m.i2 = Var(within=Integers,bounds=(0,200),initialize=1)
m.i3 = Var(within=Integers,bounds=(0,200),initialize=1)
m.i4 = Var(within=Integers,bounds=(0,200),initialize=1)
m.i5 = Var(within=Integers,bounds=(0,200),initialize=1)
m.x6 = Var(within=Reals,bounds=(0,200),initialize=1)
m.x7 = Var(within=Reals,bounds=(0,200),initialize=1)
m.x8 = Var(within=Reals,bounds=(0,200),initialize=1)
m.x9 = Var(within=Reals,bounds=(0,200),initialize=1)
m.x10 = Var(within=Reals,bounds=(0,200),initialize=1)
m.x11 = Var(within=Reals,bounds=(0,200),initialize=1)
m.x12 = Var(within=Reals,bounds=(0,200),initialize=1)
m.x13 = Var(within=Reals,bounds=(0,200),initialize=1)
m.x14 = Var(within=Reals,bounds=(0,200),initialize=1)
m.x15 = Var(within=Reals,bounds=(0,200),initialize=1)
m.x16 = Var(within=Reals,bounds=(0,200),initialize=1)

m.obj = Objective(expr=(1 + m.i1**2 + m.i1)**2 + (1 + m.i1**2 + m.i1)*(1 + m.i4**2 + m.i4) + (1 + m.i1**2 + m.i1)*(1 + 
                       m.x7**2 + m.x7) + (1 + m.i1**2 + m.i1)*(1 + m.x8**2 + m.x8) + (1 + m.i1**2 + m.i1)*(1 + m.x16**2
                        + m.x16) + (1 + m.i2**2 + m.i2)**2 + (1 + m.i2**2 + m.i2)*(1 + m.i3**2 + m.i3) + (1 + m.i2**2 + 
                       m.i2)*(1 + m.x7**2 + m.x7) + (1 + m.i2**2 + m.i2)*(1 + m.x10**2 + m.x10) + (1 + m.i3**2 + m.i3)**
                       2 + (1 + m.i3**2 + m.i3)*(1 + m.x7**2 + m.x7) + (1 + m.i3**2 + m.i3)*(1 + m.x9**2 + m.x9) + (1 + 
                       m.i3**2 + m.i3)*(1 + m.x10**2 + m.x10) + (1 + m.i3**2 + m.i3)*(1 + m.x14**2 + m.x14) + (1 + m.i4
                       **2 + m.i4)**2 + (1 + m.i4**2 + m.i4)*(1 + m.x7**2 + m.x7) + (1 + m.i4**2 + m.i4)*(1 + m.x11**2
                        + m.x11) + (1 + m.i4**2 + m.i4)*(1 + m.x15**2 + m.x15) + (1 + m.i5**2 + m.i5)**2 + (1 + m.i5**2
                        + m.i5)*(1 + m.x6**2 + m.x6) + (1 + m.i5**2 + m.i5)*(1 + m.x10**2 + m.x10) + (1 + m.i5**2 + m.i5
                       )*(1 + m.x12**2 + m.x12) + (1 + m.i5**2 + m.i5)*(1 + m.x16**2 + m.x16) + (1 + m.x6**2 + m.x6)**2
                        + (1 + m.x6**2 + m.x6)*(1 + m.x8**2 + m.x8) + (1 + m.x6**2 + m.x6)*(1 + m.x15**2 + m.x15) + (1
                        + m.x7**2 + m.x7)**2 + (1 + m.x7**2 + m.x7)*(1 + m.x11**2 + m.x11) + (1 + m.x7**2 + m.x7)*(1 + 
                       m.x13**2 + m.x13) + (1 + m.x8**2 + m.x8)**2 + (1 + m.x8**2 + m.x8)*(1 + m.x10**2 + m.x10) + (1 + 
                       m.x8**2 + m.x8)*(1 + m.x15**2 + m.x15) + (1 + m.x9**2 + m.x9)**2 + (1 + m.x9**2 + m.x9)*(1 + 
                       m.x12**2 + m.x12) + (1 + m.x9**2 + m.x9)*(1 + m.x16**2 + m.x16) + (1 + m.x10**2 + m.x10)**2 + (1
                        + m.x10**2 + m.x10)*(1 + m.x14**2 + m.x14) + (1 + m.x11**2 + m.x11)**2 + (1 + m.x11**2 + m.x11)*
                       (1 + m.x13**2 + m.x13) + (1 + m.x12**2 + m.x12)**2 + (1 + m.x12**2 + m.x12)*(1 + m.x14**2 + m.x14
                       ) + (1 + m.x13**2 + m.x13)**2 + (1 + m.x13**2 + m.x13)*(1 + m.x14**2 + m.x14) + (1 + m.x14**2 + 
                       m.x14)**2 + (1 + m.x15**2 + m.x15)**2 + (1 + m.x16**2 + m.x16)**2, sense=minimize)

m.c1 = Constraint(expr=   0.22*m.i1 + 0.2*m.i2 + 0.19*m.i3 + 0.25*m.i4 + 0.15*m.i5 + 0.11*m.x6 + 0.12*m.x7 + 0.13*m.x8
                        + m.x9 >= 2.5)

m.c2 = Constraint(expr= - 1.46*m.i1 - 1.3*m.i3 + 1.82*m.i4 - 1.15*m.i5 + 0.8*m.x7 + m.x10 >= 1.1)

m.c3 = Constraint(expr=   1.29*m.i1 - 0.89*m.i2 - 1.16*m.i5 - 0.96*m.x6 - 0.49*m.x8 + m.x11 >= -3.1)

m.c4 = Constraint(expr= - 1.1*m.i1 - 1.06*m.i2 + 0.95*m.i3 - 0.54*m.i4 - 1.78*m.x6 - 0.41*m.x7 + m.x12 >= -3.5)

m.c5 = Constraint(expr= - 1.43*m.i4 + 1.51*m.i5 + 0.59*m.x6 - 0.33*m.x7 - 0.43*m.x8 + m.x13 >= 1.3)

m.c6 = Constraint(expr= - 1.72*m.i2 - 0.33*m.i3 + 1.62*m.i5 + 1.24*m.x6 + 0.21*m.x7 - 0.26*m.x8 + m.x14 >= 2.1)

m.c7 = Constraint(expr=   1.12*m.i1 + 0.31*m.i4 + 1.12*m.x7 - 0.36*m.x9 + m.x15 >= 2.3)

m.c8 = Constraint(expr=   0.45*m.i2 + 0.26*m.i3 - 1.1*m.i4 + 0.58*m.i5 - 1.03*m.x7 + 0.1*m.x8 + m.x16 >= -1.5)
