#  NLP written by GAMS Convert at 04/21/18 13:54:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         11        1        0       10        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         11       11        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         56       46       10        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,20),initialize=0)

m.obj = Objective(expr=m.x1*m.x6 + 2*m.x1 - 2*m.x6 + m.x2*m.x7 + 4*m.x2 - m.x7 + m.x3*m.x8 + 8*m.x3 - 2*m.x8 + m.x4*m.x9
                        - m.x4 - 4*m.x9 + m.x5*m.x10 - 3*m.x5 + 5*m.x10, sense=minimize)

m.c1 = Constraint(expr= - 8*m.x1 - 6*m.x3 + 7*m.x4 - 7*m.x5 <= 1)

m.c2 = Constraint(expr= - 6*m.x1 + 2*m.x2 - 3*m.x3 + 9*m.x4 - 3*m.x5 <= 3)

m.c3 = Constraint(expr=   6*m.x1 - 7*m.x3 - 8*m.x4 + 2*m.x5 <= 5)

m.c4 = Constraint(expr= - m.x1 + m.x2 - 8*m.x3 - 7*m.x4 - 5*m.x5 <= 4)

m.c5 = Constraint(expr=   4*m.x1 - 7*m.x2 + 4*m.x3 + 5*m.x4 + m.x5 <= 0)

m.c6 = Constraint(expr=   5*m.x7 - 4*m.x8 + 9*m.x9 - 7*m.x10 <= 0)

m.c7 = Constraint(expr=   7*m.x6 + 4*m.x7 + 3*m.x8 + 7*m.x9 + 5*m.x10 <= 7)

m.c8 = Constraint(expr=   6*m.x6 + m.x7 - 8*m.x8 + 8*m.x9 <= 3)

m.c9 = Constraint(expr= - 3*m.x6 + 2*m.x7 + 7*m.x8 + m.x10 <= 6)

m.c10 = Constraint(expr= - 2*m.x6 - 3*m.x7 + 8*m.x8 + 5*m.x9 - 2*m.x10 <= 2)
