#  NLP written by GAMS Convert at 04/21/18 13:51:44
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


m.x1 = Var(within=Reals,bounds=(0,3),initialize=2.3295)
m.x2 = Var(within=Reals,bounds=(0,4),initialize=3.17846)

m.obj = Objective(expr= - m.x1 - m.x2, sense=minimize)

m.c2 = Constraint(expr=8*m.x1**3 - 2*m.x1**4 - 8*m.x1**2 + m.x2 <= 2)

m.c3 = Constraint(expr=32*m.x1**3 - 4*m.x1**4 - 88*m.x1**2 + 96*m.x1 + m.x2 <= 36)
