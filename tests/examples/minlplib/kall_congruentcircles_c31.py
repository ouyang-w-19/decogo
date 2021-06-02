#  NLP written by GAMS Convert at 04/21/18 13:52:27
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         16        2        3       11        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         10       10        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         37       23       14        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0.25,32),initialize=0.25)
m.x2 = Var(within=Reals,bounds=(0.5,7.5),initialize=0.5)
m.x3 = Var(within=Reals,bounds=(0.5,3.5),initialize=0.5)
m.x4 = Var(within=Reals,bounds=(0.5,7.5),initialize=0.5)
m.x5 = Var(within=Reals,bounds=(0.5,3.5),initialize=0.5)
m.x6 = Var(within=Reals,bounds=(0.5,7.5),initialize=0.5)
m.x7 = Var(within=Reals,bounds=(0.5,3.5),initialize=0.5)
m.x8 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,32),initialize=0)

m.obj = Objective(expr=m.x10, sense=minimize)

m.c1 = Constraint(expr= - m.x1 + m.x10 == -2.35619449019234)

m.c2 = Constraint(expr=-m.x8*m.x9 + m.x1 == 0)

m.c3 = Constraint(expr=(m.x2 - m.x4)*(m.x2 - m.x4) + (m.x3 - m.x5)*(m.x3 - m.x5) >= 1)

m.c4 = Constraint(expr=(m.x2 - m.x6)*(m.x2 - m.x6) + (m.x3 - m.x7)*(m.x3 - m.x7) >= 1)

m.c5 = Constraint(expr=(m.x4 - m.x6)*(m.x4 - m.x6) + (m.x5 - m.x7)*(m.x5 - m.x7) >= 1)

m.c6 = Constraint(expr=   m.x2 - m.x8 <= -0.5)

m.c7 = Constraint(expr=   m.x3 - m.x9 <= -0.5)

m.c8 = Constraint(expr=   m.x4 - m.x8 <= -0.5)

m.c9 = Constraint(expr=   m.x5 - m.x9 <= -0.5)

m.c10 = Constraint(expr=   m.x6 - m.x8 <= -0.5)

m.c11 = Constraint(expr=   m.x7 - m.x9 <= -0.5)

m.c12 = Constraint(expr=   m.x2 <= 4)

m.c13 = Constraint(expr=   m.x3 <= 2)

m.c14 = Constraint(expr=   m.x2 - m.x4 <= 0)

m.c15 = Constraint(expr=   m.x2 - m.x6 <= 0)

m.c16 = Constraint(expr=   m.x4 - m.x6 <= 0)
