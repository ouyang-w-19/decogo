#  NLP written by GAMS Convert at 04/21/18 13:54:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          5        1        4        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          7        7        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         27       13       14        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,0.31),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,0.046),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,0.068),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,0.042),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,0.028),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,0.0134),initialize=0)

m.obj = Objective(expr=   4.3*m.x1 + 31.8*m.x2 + 63.3*m.x3 + 15.8*m.x4 + 68.5*m.x5 + 4.7*m.x6, sense=minimize)

m.c1 = Constraint(expr=17.1*m.x1 - 169*m.x1*m.x3 + 204.2*m.x3 - 3580*m.x3*m.x5 + 623.4*m.x5 - 3810*m.x4*m.x6 + 212.3*
                       m.x4 + 1495.5*m.x6 - 18500*m.x4*m.x6 + 38.2*m.x2 >= 4.97)

m.c2 = Constraint(expr=17.9*m.x1 - 139*m.x1*m.x3 + 113.9*m.x3 - 2450*m.x4*m.x5 + 169.7*m.x4 + 337.8*m.x5 - 16600*m.x4*
                       m.x6 + 1385.2*m.x6 - 17200*m.x5*m.x6 + 36.8*m.x2 >= -1.88)

m.c3 = Constraint(expr=26000*m.x4*m.x5 - 70*m.x4 - 819*m.x5 - 273*m.x2 >= -69.08)

m.c4 = Constraint(expr=159.9*m.x1 - 14000*m.x1*m.x6 + 2198*m.x6 - 311*m.x2 + 587*m.x4 + 391*m.x5 >= -118.02)
