#  NLP written by GAMS Convert at 04/21/18 13:55:05
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          6        6        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          6        6        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         20       10       10        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=1)

m.obj = Objective(expr=m.x1, sense=minimize)

m.c1 = Constraint(expr=m.x1*m.x2 == 1)

m.c2 = Constraint(expr=m.x3/m.x1/m.x4 == 4.8)

m.c3 = Constraint(expr=m.x5/m.x2/m.x6 == 0.98)

m.c4 = Constraint(expr=m.x6*m.x4 == 1)

m.c5 = Constraint(expr=   m.x1 - m.x2 + 1E-7*m.x3 - 1E-5*m.x5 == 0)

m.c6 = Constraint(expr=   2*m.x1 - 2*m.x2 + 1E-7*m.x3 - 0.01*m.x4 - 1E-5*m.x5 + 0.01*m.x6 == 0)
