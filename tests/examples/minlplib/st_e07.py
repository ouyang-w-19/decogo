#  NLP written by GAMS Convert at 04/21/18 13:54:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          8        6        0        2        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         11       11        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         32       25        7        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x10 = Var(within=Reals,bounds=(1,3),initialize=1)

m.obj = Objective(expr=   6*m.x1 + 16*m.x2 - 9*m.x5 + 10*m.x6 - 15*m.x9, sense=minimize)

m.c1 = Constraint(expr=   m.x1 + m.x2 - m.x3 - m.x4 == 0)

m.c2 = Constraint(expr=   m.x3 - m.x5 + m.x7 == 0)

m.c3 = Constraint(expr=   m.x4 + m.x8 - m.x9 == 0)

m.c4 = Constraint(expr= - m.x6 + m.x7 + m.x8 == 0)

m.c5 = Constraint(expr=m.x10*m.x3 - 2.5*m.x5 + 2*m.x7 <= 0)

m.c6 = Constraint(expr=m.x10*m.x4 + 2*m.x8 - 1.5*m.x9 <= 0)

m.c7 = Constraint(expr=-m.x10*(m.x3 + m.x4) + 3*m.x1 + m.x2 == 0)
