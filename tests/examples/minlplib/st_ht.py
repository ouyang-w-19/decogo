#  NLP written by GAMS Convert at 04/21/18 13:54:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          4        1        0        3        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          3        3        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          9        7        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,2),initialize=0)

m.obj = Objective(expr=2.4*m.x1 - m.x1**2 - m.x2**2 + 1.2*m.x2, sense=minimize)

m.c1 = Constraint(expr= - 2*m.x1 + m.x2 <= 1)

m.c2 = Constraint(expr=   m.x1 + m.x2 <= 4)

m.c3 = Constraint(expr=   0.5*m.x1 - m.x2 <= 1)
