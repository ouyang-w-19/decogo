#  NLP written by GAMS Convert at 04/21/18 13:54:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          4        4        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          4        4        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          9        5        4        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,9.422),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,5.9023),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,267.417085245),initialize=0)

m.obj = Objective(expr=   m.x3, sense=minimize)

m.c1 = Constraint(expr=30*m.x1 - 6*m.x1*m.x1 - m.x3 == -250)

m.c2 = Constraint(expr=20*m.x2 - 12*m.x2*m.x2 - m.x3 == -300)

m.c3 = Constraint(expr=0.5*(m.x1 + m.x2)**2 - m.x3 == -150)
