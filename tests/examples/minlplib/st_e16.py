#  NLP written by GAMS Convert at 04/21/18 13:54:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         10       10        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         13       13        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         35       17       18        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x9 = Var(within=Reals,bounds=(100,290),initialize=100)
m.x10 = Var(within=Reals,bounds=(100,310),initialize=100)
m.x11 = Var(within=Reals,bounds=(100,290),initialize=100)
m.x12 = Var(within=Reals,bounds=(100,330),initialize=100)

m.obj = Objective(expr=1200*(800/(258.333333333333 + 2.5*(0.666666666666667*((320 - m.x10)*(300 - m.x9))**0.5 - 
                       0.166666666666667*m.x9 - 0.166666666666667*m.x10)))**0.6 + 1200*(5000/(106.666666666667 + 
                       0.666666666666667*((340 - m.x12)*(300 - m.x11))**0.5 - 0.166666666666667*m.x11 - 
                       0.166666666666667*m.x12))**0.6, sense=minimize)

m.c1 = Constraint(expr=   m.x1 + m.x2 == 10)

m.c2 = Constraint(expr=   m.x1 - m.x3 + m.x6 == 0)

m.c3 = Constraint(expr=   m.x2 - m.x4 + m.x5 == 0)

m.c4 = Constraint(expr= - m.x3 + m.x5 + m.x7 == 0)

m.c5 = Constraint(expr= - m.x4 + m.x6 + m.x8 == 0)

m.c6 = Constraint(expr=m.x12*m.x6 - m.x9*m.x3 + 100*m.x1 == 0)

m.c7 = Constraint(expr=m.x10*m.x5 - m.x11*m.x4 + 100*m.x2 == 0)

m.c8 = Constraint(expr=m.x3*(m.x10 - m.x9) == 800)

m.c9 = Constraint(expr=m.x4*(m.x12 - m.x11) == 1000)
