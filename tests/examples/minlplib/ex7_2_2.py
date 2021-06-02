#  NLP written by GAMS Convert at 04/21/18 13:51:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          6        5        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          7        7        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         17        7       10        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(1E-5,16),initialize=1E-5)
m.x6 = Var(within=Reals,bounds=(1E-5,16),initialize=1E-5)

m.obj = Objective(expr= - m.x4, sense=minimize)

m.c2 = Constraint(expr=0.09755988*m.x1*m.x5 + m.x1 == 1)

m.c3 = Constraint(expr=0.0965842812*m.x2*m.x6 + m.x2 - m.x1 == 0)

m.c4 = Constraint(expr=0.0391908*m.x3*m.x5 + m.x3 + m.x1 == 1)

m.c5 = Constraint(expr=0.03527172*m.x4*m.x6 + m.x4 - m.x1 + m.x2 - m.x3 == 0)

m.c6 = Constraint(expr=m.x5**0.5 + m.x6**0.5 <= 4)
