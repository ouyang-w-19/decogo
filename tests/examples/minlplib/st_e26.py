#  NLP written by GAMS Convert at 04/21/18 13:54:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          5        1        0        4        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          3        3        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         11        9        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,30),initialize=0)

m.obj = Objective(expr=(-3*m.x1**2) - 5*m.x1 - 3*m.x2**2 - 5*m.x2, sense=minimize)

m.c1 = Constraint(expr=   0.7*m.x1 + m.x2 <= 6.3)

m.c2 = Constraint(expr=   0.5*m.x1 + 0.8333*m.x2 <= 6)

m.c3 = Constraint(expr=   m.x1 + 0.6*m.x2 <= 7.08)

m.c4 = Constraint(expr=   0.1*m.x1 + 0.25*m.x2 <= 1.35)
