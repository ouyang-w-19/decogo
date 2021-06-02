#  NLP written by GAMS Convert at 04/21/18 13:51:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          3        1        0        2        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          3        3        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          6        4        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(100,1000),initialize=100)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   m.x2, sense=minimize)

m.c2 = Constraint(expr=4510067.11409396*exp(-7548.11926028431/m.x1)*m.x1 + 0.00335570469798658*m.x1 - 2020510067.11409*
                       exp(-7548.11926028431/m.x1) - m.x2 <= 1)

m.c3 = Constraint(expr=(-4510067.11409396*exp(-7548.11926028431/m.x1)*m.x1) - 0.00335570469798658*m.x1 + 
                       2020510067.11409*exp(-7548.11926028431/m.x1) - m.x2 <= -1)
