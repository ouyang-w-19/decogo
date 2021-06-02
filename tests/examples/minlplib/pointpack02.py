#  NLP written by GAMS Convert at 04/21/18 13:53:08
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          3        0        0        3        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        5        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          9        5        4        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0.5,1),initialize=0.5)
m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x5, sense=maximize)

m.c1 = Constraint(expr=2*m.x1*m.x2 - m.x1*m.x1 - m.x2*m.x2 - m.x3*m.x3 + 2*m.x3*m.x4 - m.x4*m.x4 + m.x5 <= 0)

m.c2 = Constraint(expr= - m.x3 + m.x4 <= 0)

m.c3 = Constraint(expr= - m.x1 + m.x2 <= 0)
