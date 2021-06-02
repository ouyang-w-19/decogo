#  NLP written by GAMS Convert at 04/21/18 13:55:04
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          3        3        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          3        3        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          7        1        6        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x2*m.x2 + m.x3*m.x3, sense=minimize)

m.c2 = Constraint(expr=m.x2 - sin(2*m.x2 + 3*m.x3) - cos(3*m.x2 - 5*m.x3) == 0)

m.c3 = Constraint(expr=m.x3 - sin(m.x2 - 2*m.x3) + cos(m.x2 + 3*m.x3) == 0)
