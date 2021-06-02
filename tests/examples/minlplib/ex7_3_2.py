#  NLP written by GAMS Convert at 04/21/18 13:51:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          8        1        0        7        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        5        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         17       14        3        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   m.x4, sense=minimize)

m.c2 = Constraint(expr=m.x1**4*m.x2**4 - m.x1**4 - m.x2**4*m.x3 <= 0)

m.c3 = Constraint(expr= - m.x1 - 0.25*m.x4 <= -1.4)

m.c4 = Constraint(expr=   m.x1 - 0.25*m.x4 <= 1.4)

m.c5 = Constraint(expr= - m.x2 - 0.2*m.x4 <= -1.5)

m.c6 = Constraint(expr=   m.x2 - 0.2*m.x4 <= 1.5)

m.c7 = Constraint(expr= - m.x3 - 0.2*m.x4 <= -0.8)

m.c8 = Constraint(expr=   m.x3 - 0.2*m.x4 <= 0.8)
