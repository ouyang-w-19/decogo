#  NLP written by GAMS Convert at 04/21/18 13:51:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          4        1        1        2        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          4        4        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         12        9        3        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,2),initialize=0.5)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,3),initialize=3)

m.obj = Objective(expr= - 2*m.x1 + m.x2 - m.x3, sense=minimize)

m.c2 = Constraint(expr=m.x1*(4*m.x1 - 2*m.x2 + 2*m.x3) + m.x2*(2*m.x2 - 2*m.x1 - m.x3) + m.x3*(2*m.x1 - m.x2 + 2*m.x3)
                        - 20*m.x1 + 9*m.x2 - 13*m.x3 >= -24)

m.c3 = Constraint(expr=   m.x1 + m.x2 + m.x3 <= 4)

m.c4 = Constraint(expr=   3*m.x2 + m.x3 <= 6)
