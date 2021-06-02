#  NLP written by GAMS Convert at 04/21/18 13:53:11
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         19       11        0        8        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         15       15        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         57       41       16        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,200),initialize=0)

m.obj = Objective(expr=   m.x4 - 5*m.x5 - 3*m.x12 - 9*m.x13 + 7*m.x14 + m.x15, sense=minimize)

m.c2 = Constraint(expr=   m.x12 + m.x13 <= 300)

m.c3 = Constraint(expr=   m.x14 + m.x15 <= 300)

m.c4 = Constraint(expr=   m.x4 + m.x5 <= 300)

m.c5 = Constraint(expr=   m.x12 + m.x13 + m.x14 + m.x15 <= 300)

m.c6 = Constraint(expr=   m.x4 + m.x12 + m.x14 <= 100)

m.c7 = Constraint(expr=   m.x5 + m.x13 + m.x15 <= 200)

m.c8 = Constraint(expr= - 0.5*m.x4 + 0.5*m.x12 - 1.5*m.x14 <= 0)

m.c9 = Constraint(expr=   0.5*m.x5 + 1.5*m.x13 - 0.5*m.x15 <= 0)

m.c10 = Constraint(expr=   m.x8 + m.x9 == 1)

m.c11 = Constraint(expr=   m.x10 + m.x11 == 1)

m.c12 = Constraint(expr=-m.x8*m.x6 + m.x12 == 0)

m.c13 = Constraint(expr=-m.x8*m.x7 + m.x13 == 0)

m.c14 = Constraint(expr=-m.x9*m.x6 + m.x14 == 0)

m.c15 = Constraint(expr=-m.x9*m.x7 + m.x15 == 0)

m.c16 = Constraint(expr=-m.x10*m.x2 + m.x12 == 0)

m.c17 = Constraint(expr=-m.x11*m.x2 + m.x13 == 0)

m.c18 = Constraint(expr=-m.x10*m.x3 + m.x14 == 0)

m.c19 = Constraint(expr=-m.x11*m.x3 + m.x15 == 0)
