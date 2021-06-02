#  NLP written by GAMS Convert at 04/21/18 13:51:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          5        1        0        4        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          9        9        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         18        4       14        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0.1,10),initialize=0.1)
m.x2 = Var(within=Reals,bounds=(0.1,10),initialize=0.1)
m.x3 = Var(within=Reals,bounds=(0.1,10),initialize=0.1)
m.x4 = Var(within=Reals,bounds=(0.1,10),initialize=0.1)
m.x5 = Var(within=Reals,bounds=(0.1,10),initialize=0.1)
m.x6 = Var(within=Reals,bounds=(0.1,10),initialize=0.1)
m.x7 = Var(within=Reals,bounds=(0.1,10),initialize=0.1)
m.x8 = Var(within=Reals,bounds=(0.1,10),initialize=0.1)

m.obj = Objective(expr=0.4*m.x1**0.67/m.x7**0.67 + 0.4*m.x2**0.67/m.x8**0.67 - m.x1 - m.x2 + 10, sense=minimize)

m.c2 = Constraint(expr=0.0588*m.x5*m.x7 + 0.1*m.x1 <= 1)

m.c3 = Constraint(expr=0.0588*m.x6*m.x8 + 0.1*m.x1 + 0.1*m.x2 <= 1)

m.c4 = Constraint(expr=4*m.x3/m.x5 + 2/(m.x3**0.71*m.x5) + 0.0588*m.x7/m.x3**1.3 <= 1)

m.c5 = Constraint(expr=4*m.x4/m.x6 + 2/(m.x4**0.71*m.x6) + 0.0588*m.x4**1.3*m.x8 <= 1)
