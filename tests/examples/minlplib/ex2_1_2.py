#  NLP written by GAMS Convert at 04/21/18 13:51:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          3        1        0        2        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          7        7        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         15       10        5        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=20)

m.obj = Objective(expr=(-0.5*(m.x1*m.x1 + m.x2*m.x2 + m.x3*m.x3 + m.x4*m.x4 + m.x5*m.x5)) - 10.5*m.x1 - 7.5*m.x2 - 3.5*
                       m.x3 - 2.5*m.x4 - 1.5*m.x5 - 10*m.x6, sense=minimize)

m.c2 = Constraint(expr=   6*m.x1 + 3*m.x2 + 3*m.x3 + 2*m.x4 + m.x5 <= 6.5)

m.c3 = Constraint(expr=   10*m.x1 + 10*m.x3 + m.x6 <= 20)
