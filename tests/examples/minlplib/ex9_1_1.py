#  NLP written by GAMS Convert at 04/21/18 13:51:48
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         13       13        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         14       14        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         37       27       10        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=0)
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

m.obj = Objective(expr= - 3*m.x1 + 2*m.x2 - m.x4, sense=minimize)

m.c2 = Constraint(expr=   m.x1 + 4*m.x2 - 2*m.x4 + m.x5 == 16)

m.c3 = Constraint(expr=   3*m.x1 - 2*m.x2 + 8*m.x4 + m.x6 == 48)

m.c4 = Constraint(expr=   m.x1 - 3*m.x2 - 2*m.x4 + m.x7 == -12)

m.c5 = Constraint(expr= - m.x1 + m.x8 == 0)

m.c6 = Constraint(expr=   m.x1 + m.x9 == 4)

m.c7 = Constraint(expr=m.x10*m.x5 == 0)

m.c8 = Constraint(expr=m.x11*m.x6 == 0)

m.c9 = Constraint(expr=m.x12*m.x7 == 0)

m.c10 = Constraint(expr=m.x13*m.x8 == 0)

m.c11 = Constraint(expr=m.x14*m.x9 == 0)

m.c12 = Constraint(expr=   m.x10 + 3*m.x11 + m.x12 - m.x13 + m.x14 == 1)

m.c13 = Constraint(expr=   2*m.x11 - 3*m.x12 == 0)
