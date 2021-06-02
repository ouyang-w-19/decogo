#  NLP written by GAMS Convert at 04/21/18 13:51:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          8        1        0        7        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        5        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         17       14        3        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   m.x4, sense=minimize)

m.c2 = Constraint(expr=10*m.x2**2*m.x3**3 + 10*m.x2**3*m.x3**2 + 200*m.x2**2*m.x3**2 + 100*m.x2**3*m.x3 + 100*m.x3**3*
                       m.x2 + m.x1*m.x2*m.x3**2 + m.x2**2*m.x1*m.x3 + 1000*m.x3**2*m.x2 + 8*m.x3**2*m.x1 + 1000*m.x2**2*
                       m.x3 + 8*m.x2**2*m.x1 + 6*m.x1*m.x2*m.x3 - m.x1**2 + 60*m.x1*m.x3 + 60*m.x1*m.x2 - 200*m.x1 <= 0)

m.c3 = Constraint(expr= - m.x1 - 800*m.x4 <= -800)

m.c4 = Constraint(expr=   m.x1 - 800*m.x4 <= 800)

m.c5 = Constraint(expr= - m.x2 - 2*m.x4 <= -4)

m.c6 = Constraint(expr=   m.x2 - 2*m.x4 <= 4)

m.c7 = Constraint(expr= - m.x3 - 3*m.x4 <= -6)

m.c8 = Constraint(expr=   m.x3 - 3*m.x4 <= 6)
