#  NLP written by GAMS Convert at 04/21/18 13:54:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          3        1        0        2        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          3        3        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          7        5        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,5),initialize=0)

m.obj = Objective(expr=m.x1*m.x2 - m.x1 - m.x2, sense=minimize)

m.c1 = Constraint(expr= - 6*m.x1 + 8*m.x2 <= 3)

m.c2 = Constraint(expr=   3*m.x1 - m.x2 <= 3)
