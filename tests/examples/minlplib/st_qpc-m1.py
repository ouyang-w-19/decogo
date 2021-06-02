#  NLP written by GAMS Convert at 04/21/18 13:54:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          6        1        5        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          6        6        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         27       22        5        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=10*m.x1 - 0.34*m.x1*m.x1 - 0.28*m.x1*m.x2 + 10*m.x2 - 0.22*m.x1*m.x3 + 10*m.x3 - 0.24*m.x1*m.x4
                        + 10*m.x4 - 0.51*m.x1*m.x5 + 10*m.x5 - 0.28*m.x2*m.x1 - 0.34*m.x2*m.x2 - 0.23*m.x2*m.x3 - 0.24*
                       m.x2*m.x4 - 0.45*m.x2*m.x5 - 0.22*m.x3*m.x1 - 0.23*m.x3*m.x2 - 0.35*m.x3*m.x3 - 0.22*m.x3*m.x4 - 
                       0.34*m.x3*m.x5 - 0.24*m.x4*m.x1 - 0.24*m.x4*m.x2 - 0.22*m.x4*m.x3 - 0.2*m.x4*m.x4 - 0.38*m.x4*
                       m.x5 - 0.51*m.x5*m.x1 - 0.45*m.x5*m.x2 - 0.34*m.x5*m.x3 - 0.38*m.x5*m.x4 - 0.99*m.x5*m.x5
                       , sense=minimize)

m.c1 = Constraint(expr=   m.x1 + m.x2 + 2*m.x3 + m.x4 + m.x5 >= 10)

m.c2 = Constraint(expr=   2*m.x1 + 3*m.x2 + m.x5 >= 8)

m.c3 = Constraint(expr=   m.x2 + 4*m.x3 - m.x4 + 2*m.x5 >= 12)

m.c4 = Constraint(expr=   8*m.x1 - m.x2 - m.x3 + 6*m.x4 >= 20)

m.c5 = Constraint(expr= - 2*m.x1 - m.x2 - 3*m.x3 - m.x4 - m.x5 >= -30)
