#  NLP written by GAMS Convert at 04/21/18 13:51:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          7        5        0        2        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          7        7        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         34       24       10        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(-2,2),initialize=0)
m.x2 = Var(within=Reals,bounds=(-2,2),initialize=0)
m.x3 = Var(within=Reals,bounds=(-2,2),initialize=0)
m.x4 = Var(within=Reals,bounds=(-2,2),initialize=0)
m.x5 = Var(within=Reals,bounds=(-2,2),initialize=0)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   m.x6, sense=minimize)

m.c2 = Constraint(expr=   2*m.x1 + m.x2 + m.x3 + m.x4 + m.x5 == 6)

m.c3 = Constraint(expr=   m.x1 + 2*m.x2 + m.x3 + m.x4 + m.x5 == 6)

m.c4 = Constraint(expr=   m.x1 + m.x2 + 2*m.x3 + m.x4 + m.x5 == 6)

m.c5 = Constraint(expr=   m.x1 + m.x2 + m.x3 + 2*m.x4 + m.x5 == 6)

m.c6 = Constraint(expr=m.x1*m.x2*m.x3*m.x4*m.x5 - m.x6 <= 1)

m.c7 = Constraint(expr=-m.x1*m.x2*m.x3*m.x4*m.x5 - m.x6 <= -1)
