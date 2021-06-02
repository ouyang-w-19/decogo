#  NLP written by GAMS Convert at 04/21/18 13:54:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         11        1        0       10        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          4        4        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         28       25        3        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=m.x1 - 0.5*m.x1**2 - 0.5*m.x2**2 + m.x2 - 0.5*m.x3**2 + m.x3, sense=minimize)

m.c1 = Constraint(expr=   m.x1 <= 4)

m.c2 = Constraint(expr=   m.x2 <= 4)

m.c3 = Constraint(expr=   m.x3 <= 4)

m.c4 = Constraint(expr=   2*m.x1 + 3*m.x2 + 4*m.x3 <= 35)

m.c5 = Constraint(expr=   2*m.x1 + 3*m.x2 - 4*m.x3 <= 19)

m.c6 = Constraint(expr=   2*m.x1 - 3*m.x2 + 4*m.x3 <= 23)

m.c7 = Constraint(expr= - 2*m.x1 + 3*m.x2 + 4*m.x3 <= 27)

m.c8 = Constraint(expr=   2*m.x1 - 3*m.x2 - 4*m.x3 <= 7)

m.c9 = Constraint(expr= - 2*m.x1 - 3*m.x2 + 4*m.x3 <= 15)

m.c10 = Constraint(expr= - 2*m.x1 + 3*m.x2 - 4*m.x3 <= 11)
