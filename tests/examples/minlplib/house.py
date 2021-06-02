#  NLP written by GAMS Convert at 04/21/18 13:52:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          9        5        3        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          9        9        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         26       17        9        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,None),initialize=30)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(40,68),initialize=68)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(56,100),initialize=56)
m.x7 = Var(within=Reals,bounds=(None,3000),initialize=0)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - m.x7 - m.x8, sense=minimize)

m.c1 = Constraint(expr=-(m.x1*m.x2 + m.x5*m.x4) + m.x7 == 0)

m.c2 = Constraint(expr=-m.x1*m.x3 + m.x8 == 0)

m.c4 = Constraint(expr= - m.x2 - m.x5 + m.x6 == 0)

m.c5 = Constraint(expr=   m.x1 - 0.333333333333333*m.x4 >= 0)

m.c6 = Constraint(expr=   m.x1 - 0.5*m.x4 <= 0)

m.c7 = Constraint(expr=m.x2*(m.x4 - m.x1) >= 1500)

m.c8 = Constraint(expr= - 0.5*m.x2 + m.x3 - m.x5 == 0)

m.c9 = Constraint(expr= - 0.5*m.x2 + m.x5 >= 0)
