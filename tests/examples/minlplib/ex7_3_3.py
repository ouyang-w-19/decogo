#  NLP written by GAMS Convert at 04/21/18 13:51:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          9        3        0        6        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          6        6        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         22       17        5        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   m.x5, sense=minimize)

m.c2 = Constraint(expr=9.625*m.x1*m.x4 - 4*m.x1 - 78*m.x4 + 16*m.x2*m.x4 - m.x2 + 16*m.x4**2 + m.x3 == -12)

m.c3 = Constraint(expr=16*m.x1*m.x4 - 19*m.x1 - 24*m.x4 - 8*m.x2 - m.x3 == -44)

m.c4 = Constraint(expr=   m.x1 - 0.25*m.x5 <= 2.25)

m.c5 = Constraint(expr= - m.x1 - 0.25*m.x5 <= -2.25)

m.c6 = Constraint(expr= - m.x2 - 0.5*m.x5 <= -1.5)

m.c7 = Constraint(expr=   m.x2 - 0.5*m.x5 <= 1.5)

m.c8 = Constraint(expr= - m.x3 - 1.5*m.x5 <= -1.5)

m.c9 = Constraint(expr=   m.x3 - 1.5*m.x5 <= 1.5)
