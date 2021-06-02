#  NLP written by GAMS Convert at 04/21/18 13:51:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         16       12        0        4        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         14       14        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         46       21       25        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   m.x4, sense=minimize)

m.c2 = Constraint(expr=m.x3**8*m.x13 - m.x3**6*m.x11 + m.x3**4*m.x9 - m.x3**2*m.x7 + m.x5 == 0)

m.c3 = Constraint(expr=m.x3**6*m.x12 - m.x3**4*m.x10 + m.x3**2*m.x8 - m.x6 == 0)

m.c4 = Constraint(expr= - m.x1 - 0.145*m.x4 <= -0.175)

m.c5 = Constraint(expr=   m.x1 - 0.145*m.x4 <= 0.175)

m.c6 = Constraint(expr= - m.x2 - 0.15*m.x4 <= -0.2)

m.c7 = Constraint(expr=   m.x2 - 0.15*m.x4 <= 0.2)

m.c8 = Constraint(expr=-4.53*m.x1**2 + m.x5 == 0)

m.c9 = Constraint(expr=-(5.28*m.x1**2 + 0.364*m.x1) + m.x6 == 0)

m.c10 = Constraint(expr=-(5.72*m.x1**2*m.x2 + 1.13*m.x1**2 + 0.425*m.x1) + m.x7 == 0)

m.c11 = Constraint(expr=-(6.93*m.x1**2*m.x2 + 0.0911*m.x1) + m.x8 == 0.00422)

m.c12 = Constraint(expr=-(1.45*m.x1**2*m.x2 + 0.168*m.x1*m.x2) + m.x9 == 0.000338)

m.c13 = Constraint(expr=-(1.56*m.x1**2*m.x2**2 + 0.00084*m.x1**2*m.x2 + 0.0135*m.x1*m.x2) + m.x10 == 1.35E-5)

m.c14 = Constraint(expr=-(0.125*m.x1**2*m.x2**2 + 1.68e-5*m.x1**2*m.x2 + 0.000539*m.x1*m.x2) + m.x11 == 2.7E-7)

m.c15 = Constraint(expr=-(0.005*m.x1**2*m.x2**2 + 1.08e-5*m.x1*m.x2) + m.x12 == 0)

m.c16 = Constraint(expr=-0.0001*m.x1**2*m.x2**2 + m.x13 == 0)
