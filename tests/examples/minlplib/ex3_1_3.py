#  NLP written by GAMS Convert at 04/21/18 13:51:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          7        1        3        3        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          7        7        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         19       11        8        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=5)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x3 = Var(within=Reals,bounds=(1,5),initialize=5)
m.x4 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x5 = Var(within=Reals,bounds=(1,5),initialize=5)
m.x6 = Var(within=Reals,bounds=(0,10),initialize=10)

m.obj = Objective(expr=(-25*(-2 + m.x1)**2) - (-2 + m.x2)**2 - (-1 + m.x3)**2 - (-4 + m.x4)**2 - (-1 + m.x5)**2 - (-4 + 
                       m.x6)**2, sense=minimize)

m.c2 = Constraint(expr=(-3 + m.x3)**2 + m.x4 >= 4)

m.c3 = Constraint(expr=(-3 + m.x5)**2 + m.x6 >= 4)

m.c4 = Constraint(expr=   m.x1 - 3*m.x2 <= 2)

m.c5 = Constraint(expr= - m.x1 + m.x2 <= 2)

m.c6 = Constraint(expr=   m.x1 + m.x2 <= 6)

m.c7 = Constraint(expr=   m.x1 + m.x2 >= 2)
