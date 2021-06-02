#  NLP written by GAMS Convert at 04/21/18 13:50:54
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          8        8        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         15       15        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         32       13       19        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,2),initialize=1.745)
m.x3 = Var(within=Reals,bounds=(0,1.6),initialize=1.2)
m.x4 = Var(within=Reals,bounds=(0,1.2),initialize=1.1)
m.x5 = Var(within=Reals,bounds=(0,5),initialize=3.048)
m.x6 = Var(within=Reals,bounds=(0,2),initialize=1.974)
m.x7 = Var(within=Reals,bounds=(0.85,0.93),initialize=0.893)
m.x8 = Var(within=Reals,bounds=(0.9,0.95),initialize=0.928)
m.x9 = Var(within=Reals,bounds=(3,12),initialize=8)
m.x10 = Var(within=Reals,bounds=(1.2,4),initialize=3.6)
m.x11 = Var(within=Reals,bounds=(1.45,1.62),initialize=1.45)
m.x12 = Var(within=Reals,bounds=(0.99,1.01010101010101),initialize=1)
m.x13 = Var(within=Reals,bounds=(0.99,1.01010101010101),initialize=1)
m.x14 = Var(within=Reals,bounds=(0.9,1.11111111111111),initialize=1)
m.x15 = Var(within=Reals,bounds=(0.99,1.01010101010101),initialize=1)

m.obj = Objective(expr=-6.3*m.x5*m.x8 + 5.04*m.x2 + 0.35*m.x3 + m.x4 + 3.36*m.x6, sense=minimize)

m.c2 = Constraint(expr= - 0.819672131147541*m.x2 + m.x5 - 0.819672131147541*m.x6 == 0)

m.c3 = Constraint(expr=0.98*m.x4 - (0.01*m.x5*m.x10 + m.x4)*m.x7 == 0)

m.c4 = Constraint(expr=-m.x2*m.x9 + 10*m.x3 + m.x6 == 0)

m.c5 = Constraint(expr=m.x5*m.x12 - (1.12 + 0.13167*m.x9 - 0.0067*m.x9*m.x9)*m.x2 == 0)

m.c6 = Constraint(expr=m.x8*m.x13 - 0.01*(1.098*m.x9 - 0.038*m.x9*m.x9) - 0.325*m.x7 == 0.57425)

m.c7 = Constraint(expr=m.x10*m.x14 + 22.2*m.x11 == 35.82)

m.c8 = Constraint(expr=m.x11*m.x15 - 3*m.x8 == -1.33)
