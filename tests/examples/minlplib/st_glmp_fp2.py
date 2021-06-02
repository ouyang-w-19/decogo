#  NLP written by GAMS Convert at 04/21/18 13:54:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         10        3        2        5        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        5        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         23       21        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x3*m.x4, sense=minimize)

m.c1 = Constraint(expr=   2*m.x1 + m.x2 <= 14)

m.c2 = Constraint(expr=   m.x1 + m.x2 <= 10)

m.c3 = Constraint(expr=   1.44*m.x1 + m.x2 >= 4.89)

m.c4 = Constraint(expr= - 1.58*m.x1 + m.x2 <= 5.65)

m.c5 = Constraint(expr= - 1.03*m.x1 + m.x2 <= 5.93)

m.c6 = Constraint(expr=   m.x1 + 2*m.x2 >= 6)

m.c7 = Constraint(expr=   m.x1 - m.x2 <= 3)

m.c9 = Constraint(expr=   m.x1 + m.x2 - m.x3 == 0)

m.c10 = Constraint(expr=   m.x1 - m.x2 - m.x4 == -7)
