#  NLP written by GAMS Convert at 04/21/18 13:52:29
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          5        3        0        2        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          3        3        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         11        7        4        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,None),initialize=10)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=-10)

m.obj = Objective(expr=(2*m.x1**2 - m.x2)**2 + (m.x2 - 6*m.x1**2)**2, sense=minimize)

m.c2 = Constraint(expr=m.x1 - (m.x1*m.x2 + 10*m.x2) == 0)

m.c3 = Constraint(expr=   m.x1 - 3*m.x2 == 0)

m.c4 = Constraint(expr=   m.x1 + m.x2 <= 1)

m.c5 = Constraint(expr= - m.x1 + m.x2 <= 2)
