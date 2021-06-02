#  NLP written by GAMS Convert at 04/21/18 13:51:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          7        2        0        5        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          8        8        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         28       12       16        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,200),initialize=0)

m.obj = Objective(expr=-((9 - 6*m.x1 - 16*m.x2 - 15*m.x3)*m.x4 + (15 - 6*m.x1 - 16*m.x2 - 15*m.x3)*m.x5) + m.x6 - 5*m.x7
                       , sense=minimize)

m.c2 = Constraint(expr=m.x3*m.x4 + m.x3*m.x5 <= 50)

m.c3 = Constraint(expr=   m.x4 + m.x6 <= 100)

m.c4 = Constraint(expr=   m.x5 + m.x7 <= 200)

m.c5 = Constraint(expr=(-2.5 + 3*m.x1 + m.x2 + m.x3)*m.x4 - 0.5*m.x6 <= 0)

m.c6 = Constraint(expr=(-1.5 + 3*m.x1 + m.x2 + m.x3)*m.x5 + 0.5*m.x7 <= 0)

m.c7 = Constraint(expr=   m.x1 + m.x2 + m.x3 == 1)
