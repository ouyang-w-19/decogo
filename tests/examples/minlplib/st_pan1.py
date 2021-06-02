#  NLP written by GAMS Convert at 04/21/18 13:54:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          5        1        0        4        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          4        4        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         16       13        3        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=1.25*m.x1 - 2.5*m.x1**2 - 5*m.x2**2 + 2.5*m.x2 - 7.5*m.x3**2 + 5*m.x3, sense=minimize)

m.c1 = Constraint(expr=   10*m.x1 + 0.2*m.x2 - 0.1*m.x3 <= 11)

m.c2 = Constraint(expr= - 0.3*m.x1 + 9*m.x2 + 0.2*m.x3 <= 8)

m.c3 = Constraint(expr= - 0.1*m.x1 + 0.4*m.x2 + 11*m.x3 <= 12)

m.c4 = Constraint(expr=   6*m.x1 + 8*m.x2 + 9*m.x3 <= 18)
