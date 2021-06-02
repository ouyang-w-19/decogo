#  NLP written by GAMS Convert at 04/21/18 13:53:08
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         21        0        0       21        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         13       13        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         87       27       60        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0.5,1),initialize=0.5)
m.x2 = Var(within=Reals,bounds=(0.5,1),initialize=0.5)
m.x3 = Var(within=Reals,bounds=(0.5,1),initialize=0.5)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x13, sense=maximize)

m.c1 = Constraint(expr=2*m.x1*m.x2 - m.x1*m.x1 - m.x2*m.x2 - m.x7*m.x7 + 2*m.x7*m.x8 - m.x8*m.x8 + m.x13 <= 0)

m.c2 = Constraint(expr=2*m.x1*m.x3 - m.x1*m.x1 - m.x3*m.x3 - m.x7*m.x7 + 2*m.x7*m.x9 - m.x9*m.x9 + m.x13 <= 0)

m.c3 = Constraint(expr=2*m.x1*m.x4 - m.x1*m.x1 - m.x4*m.x4 - m.x7*m.x7 + 2*m.x7*m.x10 - m.x10*m.x10 + m.x13 <= 0)

m.c4 = Constraint(expr=2*m.x1*m.x5 - m.x1*m.x1 - m.x5*m.x5 - m.x7*m.x7 + 2*m.x7*m.x11 - m.x11*m.x11 + m.x13 <= 0)

m.c5 = Constraint(expr=2*m.x1*m.x6 - m.x1*m.x1 - m.x6*m.x6 - m.x7*m.x7 + 2*m.x7*m.x12 - m.x12*m.x12 + m.x13 <= 0)

m.c6 = Constraint(expr=2*m.x2*m.x3 - m.x2*m.x2 - m.x3*m.x3 - m.x8*m.x8 + 2*m.x8*m.x9 - m.x9*m.x9 + m.x13 <= 0)

m.c7 = Constraint(expr=2*m.x2*m.x4 - m.x2*m.x2 - m.x4*m.x4 - m.x8*m.x8 + 2*m.x8*m.x10 - m.x10*m.x10 + m.x13 <= 0)

m.c8 = Constraint(expr=2*m.x2*m.x5 - m.x2*m.x2 - m.x5*m.x5 - m.x8*m.x8 + 2*m.x8*m.x11 - m.x11*m.x11 + m.x13 <= 0)

m.c9 = Constraint(expr=2*m.x2*m.x6 - m.x2*m.x2 - m.x6*m.x6 - m.x8*m.x8 + 2*m.x8*m.x12 - m.x12*m.x12 + m.x13 <= 0)

m.c10 = Constraint(expr=2*m.x3*m.x4 - m.x3*m.x3 - m.x4*m.x4 - m.x9*m.x9 + 2*m.x9*m.x10 - m.x10*m.x10 + m.x13 <= 0)

m.c11 = Constraint(expr=2*m.x3*m.x5 - m.x3*m.x3 - m.x5*m.x5 - m.x9*m.x9 + 2*m.x9*m.x11 - m.x11*m.x11 + m.x13 <= 0)

m.c12 = Constraint(expr=2*m.x3*m.x6 - m.x3*m.x3 - m.x6*m.x6 - m.x9*m.x9 + 2*m.x9*m.x12 - m.x12*m.x12 + m.x13 <= 0)

m.c13 = Constraint(expr=2*m.x4*m.x5 - m.x4*m.x4 - m.x5*m.x5 - m.x10*m.x10 + 2*m.x10*m.x11 - m.x11*m.x11 + m.x13 <= 0)

m.c14 = Constraint(expr=2*m.x4*m.x6 - m.x4*m.x4 - m.x6*m.x6 - m.x10*m.x10 + 2*m.x10*m.x12 - m.x12*m.x12 + m.x13 <= 0)

m.c15 = Constraint(expr=2*m.x5*m.x6 - m.x5*m.x5 - m.x6*m.x6 - m.x11*m.x11 + 2*m.x11*m.x12 - m.x12*m.x12 + m.x13 <= 0)

m.c16 = Constraint(expr= - m.x7 + m.x8 <= 0)

m.c17 = Constraint(expr= - m.x1 + m.x2 <= 0)

m.c18 = Constraint(expr= - m.x2 + m.x3 <= 0)

m.c19 = Constraint(expr= - m.x3 + m.x4 <= 0)

m.c20 = Constraint(expr= - m.x4 + m.x5 <= 0)

m.c21 = Constraint(expr= - m.x5 + m.x6 <= 0)
