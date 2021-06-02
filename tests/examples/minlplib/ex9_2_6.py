#  NLP written by GAMS Convert at 04/21/18 13:51:48
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         13       13        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         17       17        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         33       17       16        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,200),initialize=0)

m.obj = Objective(expr=m.x2*m.x2 - 2*m.x2 + m.x3*m.x3 - 2*m.x3 + m.x4*m.x4 + m.x5*m.x5, sense=minimize)

m.c2 = Constraint(expr= - m.x4 + m.x6 == -0.5)

m.c3 = Constraint(expr= - m.x5 + m.x7 == -0.5)

m.c4 = Constraint(expr=   m.x4 + m.x8 == 1.5)

m.c5 = Constraint(expr=   m.x5 + m.x9 == 1.5)

m.c6 = Constraint(expr=m.x6*m.x12 == 0)

m.c7 = Constraint(expr=m.x7*m.x13 == 0)

m.c8 = Constraint(expr=m.x8*m.x14 == 0)

m.c9 = Constraint(expr=m.x9*m.x15 == 0)

m.c10 = Constraint(expr=m.x10*m.x16 == 0)

m.c11 = Constraint(expr=m.x11*m.x17 == 0)

m.c12 = Constraint(expr= - 2*m.x2 + 2*m.x4 - m.x12 + m.x14 == 0)

m.c13 = Constraint(expr= - 2*m.x3 + 2*m.x5 - m.x13 + m.x15 == 0)
