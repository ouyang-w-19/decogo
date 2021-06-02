#  NLP written by GAMS Convert at 04/21/18 13:54:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          5        1        0        4        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        5        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         21       17        4        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=16*m.x1 - 4*m.x1**2 - 0.5*m.x2**2 + m.x2 - 2.5*m.x3**2 + 15*m.x3 - m.x4**2 + 8*m.x4
                       , sense=minimize)

m.c1 = Constraint(expr=   m.x1 - m.x2 + 3*m.x3 - 2*m.x4 <= 6)

m.c2 = Constraint(expr= - m.x1 + 4*m.x2 + m.x3 - 2*m.x4 <= 7)

m.c3 = Constraint(expr=   2*m.x1 + m.x2 + 2*m.x3 + m.x4 <= 29)

m.c4 = Constraint(expr=   m.x1 - m.x2 + m.x3 + m.x4 <= 11)
