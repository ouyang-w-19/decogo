#  NLP written by GAMS Convert at 04/21/18 13:54:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          3        3        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          4        4        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          7        3        4        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,34),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,17),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,300),initialize=0)

m.obj = Objective(expr=35*m.x1**0.6 + 35*m.x2**0.6, sense=minimize)

m.c1 = Constraint(expr=600*m.x1 - m.x1*m.x3 - 50*m.x3 == -5000)

m.c2 = Constraint(expr=   600*m.x2 + 50*m.x3 == 15000)
