#  NLP written by GAMS Convert at 04/21/18 13:54:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          2        1        1        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          3        3        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          5        3        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,115.8),initialize=0)
m.x2 = Var(within=Reals,bounds=(1E-5,30),initialize=1E-5)

m.obj = Objective(expr=   29.4*m.x1 + 18*m.x2, sense=minimize)

m.c1 = Constraint(expr=m.x1 - 0.2458*m.x1**2/m.x2 >= 6)
