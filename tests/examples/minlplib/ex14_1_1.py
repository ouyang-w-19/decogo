#  NLP written by GAMS Convert at 04/21/18 13:51:43
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
#         14        6        8        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x2 = Var(within=Reals,bounds=(-5,5),initialize=0)
# bounds init
# m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(-10,10),initialize=0)

m.obj = Objective(expr=   m.x3, sense=minimize)

m.c2 = Constraint(expr=2*m.x2**2 + 4*m.x1*m.x2 - 42*m.x1 + 4*m.x1**3 - m.x3 <= 14)

m.c3 = Constraint(expr=(-2*m.x2**2) - 4*m.x1*m.x2 + 42*m.x1 - 4*m.x1**3 - m.x3 <= -14)

m.c4 = Constraint(expr=2*m.x1**2 + 4*m.x1*m.x2 - 26*m.x2 + 4*m.x2**3 - m.x3 <= 22)

m.c5 = Constraint(expr=(-2*m.x1**2) - 4*m.x1*m.x2 + 26*m.x2 - 4*m.x2**3 - m.x3 <= -22)
