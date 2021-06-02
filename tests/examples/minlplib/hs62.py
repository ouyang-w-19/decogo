#  NLP written by GAMS Convert at 04/21/18 13:52:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          2        2        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          4        4        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          7        1        6        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=-32.174*(255*log((0.03 + m.x2 + m.x3 + m.x4)/(0.03 + 0.09*m.x2 + m.x3 + m.x4)) + 280*log((0.03 + 
                       m.x3 + m.x4)/(0.03 + 0.07*m.x3 + m.x4)) + 290*log((0.03 + m.x4)/(0.03 + 0.13*m.x4)))
                       , sense=minimize)

m.c2 = Constraint(expr=20*(-1 + m.x2 + m.x3 + m.x4)**2 == 0)
