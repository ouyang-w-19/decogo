#  NLP written by GAMS Convert at 04/21/18 13:54:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         11        1        0       10        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         21       21        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        181      161       20        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=(-0.00015*m.x1**2) - 0.0051*m.x1 - 0.00245*m.x2**2 - 0.2205*m.x2 - 0.00095*m.x3**2 - 0.0171*m.x3
                        - 0.0038*m.x4**2 - 0.6384*m.x4 - 0.0029*m.x5**2 - 0.435*m.x5 - 0.0024*m.x6**2 - 0.4704*m.x6 - 
                       0.0034*m.x7**2 - 0.4556*m.x7 - 0.0018*m.x8**2 - 0.2916*m.x8 - 0.00305*m.x9**2 - 0.0549*m.x9 - 
                       0.00025*m.x10**2 - 0.0245*m.x10 - 0.00195*m.x11**2 - 0.3588*m.x11 - 0.0008*m.x12**2 - 0.1456*
                       m.x12 - 0.0035*m.x13**2 - 0.672*m.x13 - 0.0027*m.x14**2 - 0.5184*m.x14 - 0.002*m.x15**2 - 0.016*
                       m.x15 - 0.0026*m.x16**2 - 0.1404*m.x16 - 0.0048*m.x17**2 - 0.2592*m.x17 - 0.00275*m.x18**2 - 
                       0.418*m.x18 - 0.00235*m.x19**2 - 0.1081*m.x19 - 0.00275*m.x20**2 - 0.264*m.x20, sense=minimize)

m.c1 = Constraint(expr=   6*m.x1 + 2*m.x2 + 4*m.x3 + 3*m.x5 + 4*m.x6 + 9*m.x7 + 5*m.x9 + m.x10 + 9*m.x11 + 6*m.x12
                        + 7*m.x14 + 9*m.x15 + 2*m.x16 + 8*m.x18 + 2*m.x19 + 4*m.x20 <= 405)

m.c2 = Constraint(expr=   6*m.x1 + 5*m.x2 + m.x3 + 8*m.x4 + 4*m.x6 + 3*m.x7 + 9*m.x8 + 6*m.x10 + 4*m.x11 + 7*m.x12
                        + 5*m.x13 + 2*m.x15 + 5*m.x16 + 8*m.x17 + 9*m.x19 + 8*m.x20 <= 450)

m.c3 = Constraint(expr=   8*m.x2 + 6*m.x3 + 2*m.x4 + 6*m.x5 + 4*m.x7 + 4*m.x8 + 6*m.x9 + 9*m.x11 + 4*m.x12 + 6*m.x13
                        + 9*m.x14 + 9*m.x16 + 9*m.x17 + 3*m.x18 + m.x20 <= 430)

m.c4 = Constraint(expr=   8*m.x1 + 7*m.x3 + 3*m.x4 + 2*m.x5 + m.x6 + 7*m.x8 + 4*m.x9 + 7*m.x10 + 3*m.x12 + 4*m.x13
                        + m.x14 + 6*m.x15 + 2*m.x17 + 8*m.x18 + 9*m.x19 <= 360)

m.c5 = Constraint(expr=   m.x1 + 5*m.x2 + 5*m.x4 + 5*m.x5 + m.x6 + 3*m.x7 + 5*m.x9 + 7*m.x10 + 4*m.x11 + 6*m.x13 + m.x14
                        + 3*m.x15 + 4*m.x16 + 3*m.x18 + 5*m.x19 + 5*m.x20 <= 315)

m.c6 = Constraint(expr=   m.x1 + 8*m.x2 + 7*m.x3 + m.x5 + 6*m.x6 + m.x7 + 6*m.x8 + 7*m.x10 + 3*m.x11 + 6*m.x12 + 4*m.x14
                        + 6*m.x15 + m.x16 + 4*m.x17 + m.x19 + 4*m.x20 <= 330)

m.c7 = Constraint(expr=   5*m.x2 + 8*m.x3 + 7*m.x4 + 3*m.x6 + 3*m.x7 + 8*m.x8 + 6*m.x9 + 6*m.x11 + 4*m.x12 + 3*m.x13
                        + 4*m.x15 + 2*m.x16 + 5*m.x17 + 2*m.x18 + 4*m.x20 <= 350)

m.c8 = Constraint(expr=   m.x1 + 3*m.x3 + 2*m.x4 + 7*m.x5 + 2*m.x7 + m.x8 + m.x9 + 7*m.x10 + 4*m.x12 + 3*m.x13 + 5*m.x14
                        + 3*m.x16 + 6*m.x17 + 3*m.x18 + m.x19 <= 245)

m.c9 = Constraint(expr=   5*m.x1 + 5*m.x2 + 2*m.x4 + m.x5 + 9*m.x6 + 7*m.x8 + 4*m.x9 + 8*m.x10 + 5*m.x11 + 2*m.x13
                        + 4*m.x14 + 4*m.x15 + 4*m.x17 + 8*m.x18 + 9*m.x19 + m.x20 <= 390)

m.c10 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13
                         + m.x14 + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20 <= 200)
