#  NLP written by GAMS Convert at 04/21/18 13:54:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          9        9        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          9        9        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         25        9       16        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x2 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x6 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x7 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x8 = Var(within=Reals,bounds=(-1,1),initialize=0)

m.obj = Objective(expr= - 0, sense=minimize)

m.c1 = Constraint(expr=0.004731*m.x1*m.x3 - 0.1238*m.x1 - 0.3578*m.x2*m.x3 - 0.001637*m.x2 - 0.9338*m.x4 + m.x7
                        == 0.3571)

m.c2 = Constraint(expr=0.2238*m.x1*m.x3 + 0.2638*m.x1 + 0.7623*m.x2*m.x3 - 0.07745*m.x2 - 0.6734*m.x4 - m.x7 == 0.6022)

m.c3 = Constraint(expr=m.x6*m.x8 + 0.3578*m.x1 + 0.004731*m.x2 == 0)

m.c4 = Constraint(expr= - 0.7623*m.x1 + 0.2238*m.x2 == -0.3461)

m.c5 = Constraint(expr=m.x1**2 + m.x2**2 == 1)

m.c6 = Constraint(expr=m.x3**2 + m.x4**2 == 1)

m.c7 = Constraint(expr=m.x5**2 + m.x6**2 == 1)

m.c8 = Constraint(expr=m.x7**2 + m.x8**2 == 1)
