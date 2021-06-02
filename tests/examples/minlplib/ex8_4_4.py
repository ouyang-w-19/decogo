#  NLP written by GAMS Convert at 04/21/18 13:51:47
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         13       13        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         18       18        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         61       25       36        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(4,6),initialize=4.343494264)
m.x2 = Var(within=Reals,bounds=(-6,-4),initialize=-4.313466584)
m.x3 = Var(within=Reals,bounds=(2,4),initialize=3.100750712)
m.x4 = Var(within=Reals,bounds=(-3,-1),initialize=-2.397724192)
m.x5 = Var(within=Reals,bounds=(1,3),initialize=1.584424234)
m.x6 = Var(within=Reals,bounds=(-2,0),initialize=-1.551894266)
m.x7 = Var(within=Reals,bounds=(0.5,2.5),initialize=1.199661008)
m.x8 = Var(within=Reals,bounds=(-1.5,0.5),initialize=0.212540694)
m.x9 = Var(within=Reals,bounds=(0.2,2.2),initialize=0.334227446)
m.x10 = Var(within=Reals,bounds=(-1.2,0.8),initialize=-0.199578662)
m.x11 = Var(within=Reals,bounds=(0.1,2.1),initialize=2.096235254)
m.x12 = Var(within=Reals,bounds=(-1.1,0.9),initialize=0.057466756)
m.x13 = Var(within=Reals,bounds=(0,1),initialize=0.991133039)
m.x14 = Var(within=Reals,bounds=(0,1),initialize=0.762250467)
m.x15 = Var(within=Reals,bounds=(1.1,1.3),initialize=1.1261384966)
m.x16 = Var(within=Reals,bounds=(0,1),initialize=0.639718759)
m.x17 = Var(within=Reals,bounds=(0,1),initialize=0.159517864)

m.obj = Objective(expr=(-5 + m.x1)**2 + (5 + m.x2)**2 + (-3 + m.x3)**2 + (2 + m.x4)**2 + (-2 + m.x5)**2 + (1 + m.x6)**2
                        + (-1.5 + m.x7)**2 + (0.5 + m.x8)**2 + (-1.2 + m.x9)**2 + (0.2 + m.x10)**2 + (-1.1 + m.x11)**2
                        + (0.1 + m.x12)**2, sense=minimize)

m.c2 = Constraint(expr=m.x14/0.1570795**m.x15 - m.x1 + m.x13 == 0)

m.c3 = Constraint(expr=m.x14/0.314159**m.x15 - m.x3 + m.x13 == 0)

m.c4 = Constraint(expr=m.x14/0.4712385**m.x15 - m.x5 + m.x13 == 0)

m.c5 = Constraint(expr=m.x14/0.628318**m.x15 - m.x7 + m.x13 == 0)

m.c6 = Constraint(expr=m.x14/0.7853975**m.x15 - m.x9 + m.x13 == 0)

m.c7 = Constraint(expr=m.x14/0.942477**m.x15 - m.x11 + m.x13 == 0)

m.c8 = Constraint(expr=-m.x17/0.1570795**m.x15 - m.x2 + 0.1570795*m.x16 == 0)

m.c9 = Constraint(expr=-m.x17/0.314159**m.x15 - m.x4 + 0.314159*m.x16 == 0)

m.c10 = Constraint(expr=-m.x17/0.4712385**m.x15 - m.x6 + 0.4712385*m.x16 == 0)

m.c11 = Constraint(expr=-m.x17/0.628318**m.x15 - m.x8 + 0.628318*m.x16 == 0)

m.c12 = Constraint(expr=-m.x17/0.7853975**m.x15 - m.x10 + 0.7853975*m.x16 == 0)

m.c13 = Constraint(expr=-m.x17/0.942477**m.x15 - m.x12 + 0.942477*m.x16 == 0)
