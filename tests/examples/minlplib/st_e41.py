#  NLP written by GAMS Convert at 04/21/18 13:54:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          3        1        0        2        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        5        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         13        1       12        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0.5,1),initialize=0.5)
m.x2 = Var(within=Reals,bounds=(0.5,1),initialize=0.5)
m.x3 = Var(within=Reals,bounds=(0.5,1),initialize=0.5)
m.x4 = Var(within=Reals,bounds=(0.5,1),initialize=0.5)

m.obj = Objective(expr=200*m.x1**0.6 + 200*m.x2**0.6 + 200*m.x3**0.6 + 300*m.x4**0.6, sense=minimize)

m.c1 = Constraint(expr=-(-(1 - m.x1)**2*m.x3*(1 - m.x4)**2 - (1 - (1 - (1 - m.x1)*(1 - m.x4))*m.x2)**2*(1 - m.x3))
                        <= 0.1)

m.c2 = Constraint(expr=(-(1 - m.x1)**2*m.x3*(1 - m.x4)**2) - (1 - (1 - (1 - m.x1)*(1 - m.x4))*m.x2)**2*(1 - m.x3) <= 0)
