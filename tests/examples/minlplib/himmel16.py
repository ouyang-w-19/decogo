#  NLP written by GAMS Convert at 04/21/18 13:52:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         22        7        0       15        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         19       19        0        0        0        0        0        0
#  FX      3        3        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         97       13       84        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=0.5)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0.5)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0.5)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=0.4)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=0.8)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=0.8)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=0.4)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - m.x13 - m.x14 - m.x15 - m.x16 - m.x17 - m.x18, sense=minimize)

m.c1 = Constraint(expr=(m.x1 - m.x2)**2 + (m.x7 - m.x8)**2 <= 1)

m.c2 = Constraint(expr=(m.x1 - m.x3)**2 + (m.x7 - m.x9)**2 <= 1)

m.c3 = Constraint(expr=(m.x1 - m.x4)**2 + (m.x7 - m.x10)**2 <= 1)

m.c4 = Constraint(expr=(m.x1 - m.x5)**2 + (m.x7 - m.x11)**2 <= 1)

m.c5 = Constraint(expr=(m.x1 - m.x6)**2 + (m.x7 - m.x12)**2 <= 1)

m.c6 = Constraint(expr=(m.x2 - m.x3)**2 + (m.x8 - m.x9)**2 <= 1)

m.c7 = Constraint(expr=(m.x2 - m.x4)**2 + (m.x8 - m.x10)**2 <= 1)

m.c8 = Constraint(expr=(m.x2 - m.x5)**2 + (m.x8 - m.x11)**2 <= 1)

m.c9 = Constraint(expr=(m.x2 - m.x6)**2 + (m.x8 - m.x12)**2 <= 1)

m.c10 = Constraint(expr=(m.x3 - m.x4)**2 + (m.x9 - m.x10)**2 <= 1)

m.c11 = Constraint(expr=(m.x3 - m.x5)**2 + (m.x9 - m.x11)**2 <= 1)

m.c12 = Constraint(expr=(m.x3 - m.x6)**2 + (m.x9 - m.x12)**2 <= 1)

m.c13 = Constraint(expr=(m.x4 - m.x5)**2 + (m.x10 - m.x11)**2 <= 1)

m.c14 = Constraint(expr=(m.x4 - m.x6)**2 + (m.x10 - m.x12)**2 <= 1)

m.c15 = Constraint(expr=(m.x5 - m.x6)**2 + (m.x11 - m.x12)**2 <= 1)

m.c17 = Constraint(expr=-0.5*(m.x1*m.x8 - m.x7*m.x2) + m.x13 == 0)

m.c18 = Constraint(expr=-0.5*(m.x2*m.x9 - m.x8*m.x3) + m.x14 == 0)

m.c19 = Constraint(expr=-0.5*(m.x3*m.x10 - m.x9*m.x4) + m.x15 == 0)

m.c20 = Constraint(expr=-0.5*(m.x4*m.x11 - m.x10*m.x5) + m.x16 == 0)

m.c21 = Constraint(expr=-0.5*(m.x5*m.x12 - m.x11*m.x6) + m.x17 == 0)

m.c22 = Constraint(expr=-0.5*(m.x6*m.x7 - m.x12*m.x1) + m.x18 == 0)
