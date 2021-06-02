#  NLP written by GAMS Convert at 04/21/18 13:51:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          7        1        0        6        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          9        9        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         21       13        8        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(100,10000),initialize=100)
m.x2 = Var(within=Reals,bounds=(1000,10000),initialize=1000)
m.x3 = Var(within=Reals,bounds=(1000,10000),initialize=1000)
m.x4 = Var(within=Reals,bounds=(10,1000),initialize=10)
m.x5 = Var(within=Reals,bounds=(10,1000),initialize=10)
m.x6 = Var(within=Reals,bounds=(10,1000),initialize=10)
m.x7 = Var(within=Reals,bounds=(10,1000),initialize=10)
m.x8 = Var(within=Reals,bounds=(10,1000),initialize=10)

m.obj = Objective(expr=   m.x1 + m.x2 + m.x3, sense=minimize)

m.c2 = Constraint(expr=   m.x4 + m.x6 <= 400)

m.c3 = Constraint(expr= - m.x4 + m.x5 + m.x7 <= 300)

m.c4 = Constraint(expr= - m.x5 + m.x8 <= 100)

m.c5 = Constraint(expr=m.x1 - m.x1*m.x6 + 833.333333333333*m.x4 <= 83333.3333333333)

m.c6 = Constraint(expr=m.x2*m.x4 - m.x2*m.x7 - 1250*m.x4 + 1250*m.x5 <= 0)

m.c7 = Constraint(expr=m.x3*m.x5 - m.x3*m.x8 - 2500*m.x5 <= -1250000)
