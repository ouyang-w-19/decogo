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
#          9        6        3        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,37.5),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,50),initialize=0)

m.obj = Objective(expr= - 0, sense=minimize)

m.c1 = Constraint(expr=m.x3*m.x3 - 0.000169*m.x2**3*m.x1 == 0)

m.c2 = Constraint(expr=   m.x1 + m.x2 + m.x3 == 50)

m.c3 = Constraint(expr= - 3*m.x1 + m.x2 == 0)
