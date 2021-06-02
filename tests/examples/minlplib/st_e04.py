#  NLP written by GAMS Convert at 04/21/18 13:54:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          3        2        1        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        5        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          9        4        5        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,15.1),initialize=0)
m.x2 = Var(within=Reals,bounds=(14.7,94.2),initialize=14.7)
m.x3 = Var(within=Reals,bounds=(0,5371),initialize=0)
m.x4 = Var(within=Reals,bounds=(-459.67,80),initialize=0)

m.obj = Objective(expr=400*m.x1**0.9 + 22*(-14.7 + m.x2)**1.2 + m.x3 + 1000, sense=minimize)

m.c1 = Constraint(expr=m.x3*m.x1 + 144*m.x4 >= 11520)

m.c2 = Constraint(expr=-exp(11.86 - 3950/(460 + m.x4)) + m.x2 == 0)
