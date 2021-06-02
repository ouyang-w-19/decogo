#  NLP written by GAMS Convert at 04/21/18 13:53:10
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         17        8        0        9        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         14       14        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         59       47       12        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,200),initialize=0)

m.obj = Objective(expr=   m.x5 - 5*m.x6 - 3*m.x9 - 9*m.x10 + 6*m.x11 + 7*m.x13 + m.x14, sense=minimize)

m.c2 = Constraint(expr=   m.x9 + m.x10 <= 300)

m.c3 = Constraint(expr=   m.x11 + m.x12 <= 50)

m.c4 = Constraint(expr=   m.x13 + m.x14 <= 300)

m.c5 = Constraint(expr=   m.x5 + m.x6 <= 300)

m.c6 = Constraint(expr=   m.x9 + m.x10 + m.x11 + m.x12 + m.x13 + m.x14 <= 300)

m.c7 = Constraint(expr=   m.x5 + m.x9 + m.x11 + m.x13 <= 100)

m.c8 = Constraint(expr=   m.x6 + m.x10 + m.x12 + m.x14 <= 200)

m.c9 = Constraint(expr= - 0.5*m.x5 + 0.5*m.x9 - 1.5*m.x11 - 1.5*m.x13 <= 0)

m.c10 = Constraint(expr=   0.5*m.x6 + 1.5*m.x10 - 0.5*m.x12 - 0.5*m.x14 <= 0)

m.c11 = Constraint(expr=   m.x2 + m.x3 + m.x4 == 1)

m.c12 = Constraint(expr=-m.x2*m.x7 + m.x9 == 0)

m.c13 = Constraint(expr=-m.x2*m.x8 + m.x10 == 0)

m.c14 = Constraint(expr=-m.x3*m.x7 + m.x11 == 0)

m.c15 = Constraint(expr=-m.x3*m.x8 + m.x12 == 0)

m.c16 = Constraint(expr=-m.x4*m.x7 + m.x13 == 0)

m.c17 = Constraint(expr=-m.x4*m.x8 + m.x14 == 0)
