#  NLP written by GAMS Convert at 04/21/18 13:52:29
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          8        5        0        3        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          7        7        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         43       19       24        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,None),initialize=10)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=-10)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=10)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=10)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=10)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=-10)

m.obj = Objective(expr=(m.x1 + m.x2)**2 + (m.x3 - m.x5)**2 + (m.x6 - m.x4)**2 + 2*(m.x1 + m.x3 - m.x4)**2 + (m.x2 - m.x1
                        + m.x3 - m.x4)**2 + 10*sin(m.x1 + m.x5 - m.x6)**2, sense=minimize)

m.c2 = Constraint(expr=m.x1**2 - sin(m.x2) - m.x4 + m.x5 + m.x6 == 0)

m.c3 = Constraint(expr=m.x1*m.x3 - m.x2*m.x4*m.x1 - sin((-m.x1) - m.x3 + m.x6) - m.x5 == 0)

m.c4 = Constraint(expr=m.x2*m.x6*cos(m.x5) - sin(m.x3*m.x4) + m.x2 - m.x5 == 0)

m.c5 = Constraint(expr=m.x1*m.x2 - m.x3**2 - m.x4*m.x5 - m.x6**2 == 0)

m.c6 = Constraint(expr=   2*m.x1 + 5*m.x2 + m.x3 + m.x4 <= 1)

m.c7 = Constraint(expr=   3*m.x1 - 2*m.x2 + m.x3 - 4*m.x4 <= 0)

m.c8 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 <= 2)
