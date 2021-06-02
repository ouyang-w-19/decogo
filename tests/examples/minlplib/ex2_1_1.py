#  NLP written by GAMS Convert at 04/21/18 13:51:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          2        1        0        1        0        0        0        0
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


m.x1 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x2 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=0)

m.obj = Objective(expr=42*m.x1 - 0.5*(100*m.x1*m.x1 + 100*m.x2*m.x2 + 100*m.x3*m.x3 + 100*m.x4*m.x4 + 100*m.x5*m.x5) + 
                       44*m.x2 + 45*m.x3 + 47*m.x4 + 47.5*m.x5, sense=minimize)

m.c2 = Constraint(expr=   20*m.x1 + 12*m.x2 + 11*m.x3 + 7*m.x4 + 4*m.x5 <= 40)
