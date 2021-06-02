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
#         12        6        6        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   m.x3, sense=minimize)

m.c2 = Constraint(expr=exp(10*m.x1/(1 + 0.01*m.x1))*(0.0476666666666666 - 0.0649999999999999*m.x1) - m.x1 - m.x3 <= 0)

m.c3 = Constraint(expr=m.x1 - exp(10*m.x1/(1 + 0.01*m.x1))*(0.0476666666666666 - 0.0649999999999999*m.x1) - m.x3 <= 0)

m.c4 = Constraint(expr=exp(10*m.x2/(1 + 0.01*m.x2))*(0.143 - 0.13*m.x1 - 0.195*m.x2) + m.x1 - 3*m.x2 - m.x3 <= 0)

m.c5 = Constraint(expr=(-exp(10*m.x2/(1 + 0.01*m.x2))*(0.143 - 0.13*m.x1 - 0.195*m.x2)) - m.x1 + 3*m.x2 - m.x3 <= 0)
