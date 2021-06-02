#  NLP written by GAMS Convert at 04/21/18 13:54:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         16        8        3        5        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         15       15        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         44       30       14        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x2 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x6 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x7 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x8 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x9 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x10 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,3),initialize=0)

m.obj = Objective(expr= - m.x14, sense=minimize)

m.c1 = Constraint(expr=-m.x12*m.x7 - m.x1 + m.x3 == 0)

m.c2 = Constraint(expr=-m.x12*m.x8 - m.x2 + m.x4 == 0)

m.c3 = Constraint(expr=(-m.x13*m.x7) - m.x11*m.x9 - m.x1 + m.x5 == 0)

m.c4 = Constraint(expr=(-m.x13*m.x8) - m.x11*m.x10 - m.x2 + m.x6 == 0)

m.c5 = Constraint(expr=m.x7**2 + m.x8**2 == 1)

m.c6 = Constraint(expr=   m.x8 + m.x9 == 0)

m.c7 = Constraint(expr= - m.x7 + m.x10 == 0)

m.c8 = Constraint(expr= - m.x12 + m.x14 <= 0)

m.c9 = Constraint(expr= - m.x11 + m.x14 <= 0)

m.c10 = Constraint(expr=   2*m.x1 + m.x2 >= -1)

m.c11 = Constraint(expr=   2*m.x3 + m.x4 >= -1)

m.c12 = Constraint(expr=   2*m.x5 + m.x6 >= -1)

m.c13 = Constraint(expr=   m.x1 + m.x2 <= 1)

m.c14 = Constraint(expr=   m.x3 + m.x4 <= 1)

m.c15 = Constraint(expr=   m.x5 + m.x6 <= 1)
