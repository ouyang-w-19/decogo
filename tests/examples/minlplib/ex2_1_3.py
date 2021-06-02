#  NLP written by GAMS Convert at 04/21/18 13:51:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         10        1        0        9        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         14       14        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         41       37        4        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x2 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x6 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x7 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=3)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=3)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=3)
m.x13 = Var(within=Reals,bounds=(0,1),initialize=1)

m.obj = Objective(expr=5*m.x1 - 0.5*(10*m.x1*m.x1 + 10*m.x2*m.x2 + 10*m.x3*m.x3 + 10*m.x4*m.x4) + 5*m.x2 + 5*m.x3 + 5*
                       m.x4 - m.x5 - m.x6 - m.x7 - m.x8 - m.x9 - m.x10 - m.x11 - m.x12 - m.x13, sense=minimize)

m.c2 = Constraint(expr=   2*m.x1 + 2*m.x2 + m.x10 + m.x11 <= 10)

m.c3 = Constraint(expr=   2*m.x1 + 2*m.x3 + m.x10 + m.x12 <= 10)

m.c4 = Constraint(expr=   2*m.x2 + 2*m.x3 + m.x11 + m.x12 <= 10)

m.c5 = Constraint(expr= - 8*m.x1 + m.x10 <= 0)

m.c6 = Constraint(expr= - 8*m.x2 + m.x11 <= 0)

m.c7 = Constraint(expr= - 8*m.x3 + m.x12 <= 0)

m.c8 = Constraint(expr= - 2*m.x4 - m.x5 + m.x10 <= 0)

m.c9 = Constraint(expr= - 2*m.x6 - m.x7 + m.x11 <= 0)

m.c10 = Constraint(expr= - 2*m.x8 - m.x9 + m.x12 <= 0)
