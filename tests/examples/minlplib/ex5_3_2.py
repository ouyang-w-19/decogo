#  NLP written by GAMS Convert at 04/21/18 13:51:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         17       17        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         23       23        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         64       40       24        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   0.00432*m.x1 + 0.01517*m.x2 + 0.01517*m.x9 + 0.00432*m.x13 + 0.9979, sense=minimize)

m.c1 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 == 300)

m.c2 = Constraint(expr=   m.x5 - m.x6 - m.x7 == 0)

m.c3 = Constraint(expr=   m.x8 - m.x9 - m.x10 - m.x11 == 0)

m.c4 = Constraint(expr=   m.x12 - m.x13 - m.x14 - m.x15 == 0)

m.c5 = Constraint(expr=   m.x16 - m.x17 - m.x18 == 0)

m.c6 = Constraint(expr=m.x13*m.x21 + 0.333*m.x1 - m.x5 == 0)

m.c7 = Constraint(expr=m.x13*m.x22 - m.x8*m.x20 + 0.333*m.x1 == 0)

m.c8 = Constraint(expr=-m.x8*m.x19 + 0.333*m.x1 == 0)

m.c9 = Constraint(expr=-m.x12*m.x21 - 0.333*m.x2 == 0)

m.c10 = Constraint(expr=m.x9*m.x20 - m.x12*m.x22 + 0.333*m.x2 == 0)

m.c11 = Constraint(expr=m.x9*m.x19 + 0.333*m.x2 - m.x16 == 0)

m.c12 = Constraint(expr=m.x14*m.x21 + 0.333*m.x3 + m.x6 == 30)

m.c13 = Constraint(expr=m.x10*m.x20 + m.x14*m.x22 + 0.333*m.x3 == 50)

m.c14 = Constraint(expr=m.x10*m.x19 + 0.333*m.x3 + m.x17 == 30)

m.c15 = Constraint(expr=   m.x19 + m.x20 == 1)

m.c16 = Constraint(expr=   m.x21 + m.x22 == 1)
