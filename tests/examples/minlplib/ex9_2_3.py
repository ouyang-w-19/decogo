#  NLP written by GAMS Convert at 04/21/18 13:51:48
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         16       15        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         17       17        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         45       33       12        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,None),initialize=-8)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=-8)
m.x4 = Var(within=Reals,bounds=(0,50),initialize=1)
m.x5 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,200),initialize=0)

m.obj = Objective(expr= - 3*m.x1 - 3*m.x2 + 2*m.x4 + 2*m.x5 - 60, sense=minimize)

m.c2 = Constraint(expr=   m.x1 - 2*m.x2 + m.x4 + m.x5 <= 40)

m.c3 = Constraint(expr=   2*m.x1 - m.x4 + m.x6 == -10)

m.c4 = Constraint(expr=   2*m.x2 - m.x5 + m.x7 == -10)

m.c5 = Constraint(expr= - m.x1 + m.x8 == 10)

m.c6 = Constraint(expr=   m.x1 + m.x9 == 20)

m.c7 = Constraint(expr= - m.x2 + m.x10 == 10)

m.c8 = Constraint(expr=   m.x2 + m.x11 == 20)

m.c9 = Constraint(expr=m.x6*m.x12 == 0)

m.c10 = Constraint(expr=m.x7*m.x13 == 0)

m.c11 = Constraint(expr=m.x8*m.x14 == 0)

m.c12 = Constraint(expr=m.x9*m.x15 == 0)

m.c13 = Constraint(expr=m.x10*m.x16 == 0)

m.c14 = Constraint(expr=m.x11*m.x17 == 0)

m.c15 = Constraint(expr=   2*m.x1 - 2*m.x4 + 2*m.x12 - m.x14 + m.x15 == -40)

m.c16 = Constraint(expr=   2*m.x2 - 2*m.x5 + 2*m.x13 - m.x16 + m.x17 == -40)
