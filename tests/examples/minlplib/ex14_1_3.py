#  NLP written by GAMS Convert at 04/21/18 13:51:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          5        1        0        4        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          4        4        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         14        6        8        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(5.49E-6,4.553),initialize=5.49E-6)
m.x2 = Var(within=Reals,bounds=(0.0021961,18.21),initialize=0.0021961)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   m.x3, sense=minimize)

m.c2 = Constraint(expr=10000*m.x1*m.x2 - m.x3 <= 1)

m.c3 = Constraint(expr=-10000*m.x1*m.x2 - m.x3 <= -1)

m.c4 = Constraint(expr=exp(-m.x1) + exp(-m.x2) - m.x3 <= 1.001)

m.c5 = Constraint(expr=(-exp(-m.x1)) - exp(-m.x2) - m.x3 <= -1.001)
