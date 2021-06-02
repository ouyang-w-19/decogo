#  NLP written by GAMS Convert at 04/21/18 13:53:10
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         24       15        0        9        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         19       19        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         79       55       24        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,200),initialize=0)

m.obj = Objective(expr=   m.x5 - 5*m.x6 - 3*m.x14 - 9*m.x15 + 6*m.x16 + 7*m.x18 + m.x19, sense=minimize)

m.c2 = Constraint(expr=   m.x14 + m.x15 <= 300)

m.c3 = Constraint(expr=   m.x16 + m.x17 <= 50)

m.c4 = Constraint(expr=   m.x18 + m.x19 <= 300)

m.c5 = Constraint(expr=   m.x5 + m.x6 <= 300)

m.c6 = Constraint(expr=   m.x14 + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 <= 300)

m.c7 = Constraint(expr=   m.x5 + m.x14 + m.x16 + m.x18 <= 100)

m.c8 = Constraint(expr=   m.x6 + m.x15 + m.x17 + m.x19 <= 200)

m.c9 = Constraint(expr= - 0.5*m.x5 + 0.5*m.x14 - 1.5*m.x16 - 1.5*m.x18 <= 0)

m.c10 = Constraint(expr=   0.5*m.x6 + 1.5*m.x15 - 0.5*m.x17 - 0.5*m.x19 <= 0)

m.c11 = Constraint(expr=   m.x9 + m.x10 + m.x11 == 1)

m.c12 = Constraint(expr=   m.x12 + m.x13 == 1)

m.c13 = Constraint(expr=-m.x9*m.x7 + m.x14 == 0)

m.c14 = Constraint(expr=-m.x9*m.x8 + m.x15 == 0)

m.c15 = Constraint(expr=-m.x10*m.x7 + m.x16 == 0)

m.c16 = Constraint(expr=-m.x10*m.x8 + m.x17 == 0)

m.c17 = Constraint(expr=-m.x11*m.x7 + m.x18 == 0)

m.c18 = Constraint(expr=-m.x11*m.x8 + m.x19 == 0)

m.c19 = Constraint(expr=-m.x12*m.x2 + m.x14 == 0)

m.c20 = Constraint(expr=-m.x13*m.x2 + m.x15 == 0)

m.c21 = Constraint(expr=-m.x12*m.x3 + m.x16 == 0)

m.c22 = Constraint(expr=-m.x13*m.x3 + m.x17 == 0)

m.c23 = Constraint(expr=-m.x12*m.x4 + m.x18 == 0)

m.c24 = Constraint(expr=-m.x13*m.x4 + m.x19 == 0)
