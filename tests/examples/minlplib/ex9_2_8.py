#  NLP written by GAMS Convert at 04/21/18 13:51:48
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          6        6        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          7        7        0        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         14        8        6        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,0),initialize=0)

m.obj = Objective(expr=3*m.x3 - 4*m.x2*m.x3 + 2*m.x2 + 1, sense=minimize)

m.c2 = Constraint(expr= - m.x3 + m.x4 == 0)

m.c3 = Constraint(expr=   m.x3 + m.x5 == 1)

m.c4 = Constraint(expr=m.x6*m.x4 == 0)

m.c5 = Constraint(expr=m.x7*m.x5 == 0)

m.c6 = Constraint(expr=   4*m.x2 - m.x6 + m.x7 == 1)
