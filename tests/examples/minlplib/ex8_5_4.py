#  NLP written by GAMS Convert at 04/21/18 13:51:48
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          5        5        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          6        6        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         17        7       10        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(None,None),initialize=0.5)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0.5)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=2)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=1)

m.obj = Objective(expr=log(m.x2)*m.x2 + log(m.x3)*m.x3 - log(m.x4 - m.x6) + m.x4 - log(1 + m.x6/m.x4)*m.x5/m.x6 + 
                       0.362259780811985*m.x2 + 3.27527428318836*m.x3 - 1, sense=minimize)

m.c2 = Constraint(expr=m.x4**3 - m.x4**2 + (-m.x6**2 - m.x6 + m.x5)*m.x4 - m.x5*m.x6 == 0)

m.c3 = Constraint(expr=-(0.352565*m.x2*m.x2 + 0.844083*m.x2*m.x3 + 0.844083*m.x3*m.x2 + 2.14335*m.x3*m.x3) + m.x5 == 0)

m.c4 = Constraint(expr= - 0.12932*m.x2 - 0.271567*m.x3 + m.x6 == 0)

m.c5 = Constraint(expr=   m.x2 + m.x3 == 1)
