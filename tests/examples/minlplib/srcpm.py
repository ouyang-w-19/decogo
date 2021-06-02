#  NLP written by GAMS Convert at 04/21/18 13:54:21
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         28        2       14       12        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         40       40        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        163      158        5        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=3.1)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=13.6)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=1.1)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=16.4244058299284)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=8.9)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=4.4)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=7.1)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0.8)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=5.56103683518173)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0.312071787775987)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=1.73896316481828)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=2.5)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=2.7)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,13.6),initialize=13.6)
m.x24 = Var(within=Reals,bounds=(0,1.1),initialize=1.1)
m.x25 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x26 = Var(within=Reals,bounds=(0,16.2),initialize=15.7244058299284)
m.x27 = Var(within=Reals,bounds=(0,8.9),initialize=8.9)
m.x28 = Var(within=Reals,bounds=(0,4.4),initialize=4.4)
m.x29 = Var(within=Reals,bounds=(0,3.1),initialize=3.1)
m.x30 = Var(within=Reals,bounds=(0,1.7),initialize=0.928008053710258)
m.x31 = Var(within=Reals,bounds=(0,1.9),initialize=0.268195340806014)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=2.78989137704229)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=6.47831105055452)
m.x34 = Var(within=Reals,bounds=(2,None),initialize=12.8)
m.x35 = Var(within=Reals,bounds=(2,None),initialize=13.8)
m.x36 = Var(within=Reals,bounds=(2,None),initialize=8.3)
m.x37 = Var(within=Reals,bounds=(2,None),initialize=4.2)
m.x38 = Var(within=Reals,bounds=(2,None),initialize=8.6)
m.x39 = Var(within=Reals,bounds=(None,None),initialize=1560.6691675193)

m.obj = Objective(expr=-(-3865470.56640001*m.x34**(-4) - 5130022.82472*m.x35**(-4) - 423446.8691225*m.x36**(-4) - 
                       1808.40439881057*m.x37**(-2.33333333333333) - 17313.2956782741*m.x38**(-2.33333333333333))
                        + m.x39, sense=minimize)

m.c1 = Constraint(expr= - m.x3 - m.x4 + m.x23 >= 0)

m.c2 = Constraint(expr= - m.x5 - m.x6 + m.x24 >= 0)

m.c3 = Constraint(expr= - m.x7 - m.x8 + m.x25 >= 0)

m.c4 = Constraint(expr= - m.x9 - m.x10 + m.x26 >= -0.7)

m.c5 = Constraint(expr= - m.x11 - m.x12 + m.x27 >= 0)

m.c6 = Constraint(expr= - m.x13 - m.x14 + m.x28 >= 0)

m.c7 = Constraint(expr= - m.x1 - m.x2 + m.x29 >= 0)

m.c8 = Constraint(expr=   0.35*m.x3 + 0.34*m.x4 + 0.5*m.x5 + 0.49*m.x6 + 0.68*m.x7 + 0.67*m.x8 - m.x17 - m.x18
                        + 0.99*m.x21 + 0.99*m.x22 - m.x32 >= 0)

m.c9 = Constraint(expr=   0.38*m.x9 + 0.38*m.x10 + 0.48*m.x11 + 0.47*m.x12 + 0.66*m.x13 + 0.65*m.x14 - m.x19 - m.x20
                        - m.x21 - m.x22 - m.x33 >= 0)

m.c10 = Constraint(expr=   0.2*m.x1 + 0.2*m.x2 + 0.96*m.x15 + 0.96*m.x16 + 0.67*m.x17 + 0.36*m.x18 + 0.61*m.x19
                         + 0.25*m.x20 - m.x30 - m.x34 >= 0)

m.c11 = Constraint(expr=   0.28*m.x3 + 0.28*m.x4 + 0.25*m.x5 + 0.25*m.x6 + 0.2*m.x7 + 0.2*m.x8 + 0.26*m.x9 + 0.26*m.x10
                         + 0.23*m.x11 + 0.23*m.x12 + 0.18*m.x13 + 0.18*m.x14 + 0.07*m.x17 + 0.18*m.x18 + 0.02*m.x19
                         + 0.1*m.x20 + m.x30 + 0.93*m.x31 - m.x35 >= -0.5)

m.c12 = Constraint(expr=   0.8*m.x1 + 0.8*m.x2 + 0.35*m.x3 + 0.35*m.x4 + 0.23*m.x5 + 0.23*m.x6 + 0.1*m.x7 + 0.1*m.x8
                         + 0.33*m.x9 + 0.33*m.x10 + 0.27*m.x11 + 0.27*m.x12 + 0.14*m.x13 + 0.14*m.x14 - m.x15 - m.x16
                         + 0.04*m.x17 + 0.03*m.x18 + 0.06*m.x19 + 0.04*m.x20 - m.x31 - m.x36 >= 0)

m.c13 = Constraint(expr=   0.23*m.x17 + 0.42*m.x18 + m.x32 - m.x37 >= 0)

m.c14 = Constraint(expr=   0.3*m.x19 + 0.6*m.x20 + m.x33 - m.x38 >= -0.1)

m.c15 = Constraint(expr=   m.x1 <= 3.4)

m.c16 = Constraint(expr=   m.x2 <= 0)

m.c17 = Constraint(expr=   m.x21 <= 2.7)

m.c18 = Constraint(expr=   m.x22 <= 0.3)

m.c19 = Constraint(expr=   m.x3 + m.x5 + m.x7 + m.x9 + m.x11 + m.x13 <= 50.5)

m.c20 = Constraint(expr=   m.x4 + m.x6 + m.x8 + m.x10 + m.x12 + m.x14 <= 7.5)

m.c21 = Constraint(expr=   m.x15 <= 7.1)

m.c22 = Constraint(expr=   m.x16 <= 0.8)

m.c23 = Constraint(expr=   m.x17 + m.x19 <= 7.3)

m.c24 = Constraint(expr=   m.x18 + m.x20 <= 2.9)

m.c25 = Constraint(expr= - 0.83*m.x17 + m.x19 <= 3.9)

m.c26 = Constraint(expr=   m.x20 <= 2.5)

m.c27 = Constraint(expr= - 0.45*m.x3 - 0.5*m.x4 - 0.45*m.x5 - 0.5*m.x6 - 0.45*m.x7 - 0.5*m.x8 - 0.5*m.x9 - 0.55*m.x10
                         - 0.5*m.x11 - 0.55*m.x12 - 0.5*m.x13 - 0.55*m.x14 - 0.41*m.x15 - 0.5*m.x16 - 0.27*m.x17
                         - 0.45*m.x18 - 0.32*m.x19 - 0.28*m.x20 - 0.9*m.x21 - m.x22 - 32*m.x23 - 32*m.x24 - 32*m.x25
                         - 32*m.x26 - 32*m.x27 - 32*m.x28 - 32*m.x29 + 0.3*m.x30 + m.x39 == 0)
