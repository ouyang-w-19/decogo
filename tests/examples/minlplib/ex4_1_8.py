#  NLP written by GAMS Convert at 04/21/18 13:51:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          2        2        0        0        0        0        0        0
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


m.x1 = Var(within=Reals,bounds=(0,2),initialize=0.7175)
m.x2 = Var(within=Reals,bounds=(0,3),initialize=1.47)

m.obj = Objective(expr=m.x2**2 - 7*m.x2 - 12*m.x1, sense=minimize)

m.c2 = Constraint(expr=-2*m.x1**4 - m.x2 == -2)
