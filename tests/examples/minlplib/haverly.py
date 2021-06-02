#  NLP written by GAMS Convert at 04/21/18 13:52:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         10        8        0        2        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         13       13        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         34       27        7        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=1)

m.obj = Objective(expr=   m.x1 - m.x2, sense=minimize)

m.c1 = Constraint(expr=   m.x1 - 6*m.x3 - 16*m.x4 - 10*m.x5 == 0)

m.c2 = Constraint(expr=   m.x2 - 9*m.x6 - 15*m.x7 == 0)

m.c3 = Constraint(expr=   m.x6 - m.x8 - m.x10 == 0)

m.c4 = Constraint(expr=   m.x7 - m.x9 - m.x11 == 0)

m.c5 = Constraint(expr=   m.x3 + m.x4 - m.x10 - m.x11 == 0)

m.c6 = Constraint(expr=   m.x5 - m.x8 - m.x9 == 0)

m.c7 = Constraint(expr=m.x12*(m.x10 + m.x11) - 3*m.x3 - m.x4 == 0)

m.c8 = Constraint(expr=m.x12*m.x10 - 2.5*m.x10 - 0.5*m.x8 <= 0)

m.c9 = Constraint(expr=m.x12*m.x11 - 1.5*m.x11 + 0.5*m.x9 <= 0)
