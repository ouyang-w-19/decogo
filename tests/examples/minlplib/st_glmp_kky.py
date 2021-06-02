#  NLP written by GAMS Convert at 04/21/18 13:54:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         14        6        0        8        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          8        8        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         37       33        4        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x4*m.x5 + m.x6*m.x7 + m.x3, sense=minimize)

m.c1 = Constraint(expr= - 5*m.x1 + 8*m.x2 <= 24)

m.c2 = Constraint(expr= - 5*m.x1 - 8*m.x2 <= 100)

m.c3 = Constraint(expr= - 6*m.x1 + 3*m.x2 <= 100)

m.c4 = Constraint(expr= - 4*m.x1 - 5*m.x2 <= -10)

m.c5 = Constraint(expr=   5*m.x1 - 8*m.x2 <= 100)

m.c6 = Constraint(expr=   5*m.x1 + 8*m.x2 <= 44)

m.c7 = Constraint(expr=   6*m.x1 - 3*m.x2 <= 15)

m.c8 = Constraint(expr=   4*m.x1 + 5*m.x2 <= 100)

m.c10 = Constraint(expr=   3*m.x1 - 4*m.x2 - m.x3 == 0)

m.c11 = Constraint(expr=   m.x1 + 2*m.x2 - m.x4 == 1.5)

m.c12 = Constraint(expr=   2*m.x1 - m.x2 - m.x5 == -4)

m.c13 = Constraint(expr=   m.x1 - 2*m.x2 - m.x6 == -8.5)

m.c14 = Constraint(expr=   2*m.x1 + m.x2 - m.x7 == 1)
