#  NLP written by GAMS Convert at 04/21/18 13:51:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         14       14        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         17       17        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         43       25       18        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(10,350),initialize=10)
m.x2 = Var(within=Reals,bounds=(10,350),initialize=10)
m.x3 = Var(within=Reals,bounds=(10,200),initialize=10)
m.x4 = Var(within=Reals,bounds=(10,200),initialize=10)
m.x5 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x13 = Var(within=Reals,bounds=(150,310),initialize=150)
m.x14 = Var(within=Reals,bounds=(150,310),initialize=150)
m.x15 = Var(within=Reals,bounds=(150,310),initialize=150)
m.x16 = Var(within=Reals,bounds=(150,310),initialize=150)

m.obj = Objective(expr=1300*(1000/(0.0333333333333333*m.x1*m.x2 + 0.166666666666667*m.x1 + 0.166666666666667*m.x2))**0.6
                        + 1300*(600/(0.0333333333333333*m.x3*m.x4 + 0.166666666666667*m.x3 + 0.166666666666667*m.x4))**
                       0.6, sense=minimize)

m.c1 = Constraint(expr=   m.x5 + m.x9 == 10)

m.c2 = Constraint(expr=   m.x5 - m.x6 + m.x11 == 0)

m.c3 = Constraint(expr=   m.x7 + m.x9 - m.x10 == 0)

m.c4 = Constraint(expr= - m.x6 + m.x7 + m.x8 == 0)

m.c5 = Constraint(expr= - m.x10 + m.x11 + m.x12 == 0)

m.c6 = Constraint(expr=m.x16*m.x11 - m.x13*m.x6 + 150*m.x5 == 0)

m.c7 = Constraint(expr=m.x15*m.x7 - m.x14*m.x10 + 150*m.x9 == 0)

m.c8 = Constraint(expr=m.x6*m.x15 - m.x6*m.x13 == 1000)

m.c9 = Constraint(expr=m.x10*m.x16 - m.x10*m.x14 == 600)

m.c10 = Constraint(expr=   m.x1 + m.x15 == 500)

m.c11 = Constraint(expr=   m.x2 + m.x13 == 250)

m.c12 = Constraint(expr=   m.x3 + m.x16 == 350)

m.c13 = Constraint(expr=   m.x4 + m.x14 == 200)
