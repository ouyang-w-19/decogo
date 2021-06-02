#  NLP written by GAMS Convert at 04/21/18 13:52:38
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          6        6        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          6        6        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         11        6        5        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=2*m.x2*m.x4 + 4*m.x2*m.x5 + 3*m.x2*m.x6 + 6*m.x3*m.x4 + 2*m.x3*m.x5 + 3*m.x3*m.x6 + 5*m.x4*m.x5
                        + 3*m.x4*m.x6 + 3*m.x5*m.x6, sense=minimize)

m.c2 = Constraint(expr=   m.x2 == 1)

m.c3 = Constraint(expr=   m.x3 == 1)

m.c4 = Constraint(expr=   m.x4 == 1)

m.c5 = Constraint(expr=   m.x5 == 1)

m.c6 = Constraint(expr=   m.x6 == 1)
