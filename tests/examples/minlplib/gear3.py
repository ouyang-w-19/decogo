#  MINLP written by GAMS Convert at 04/21/18 13:52:21
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          5        5        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          9        5        0        4        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         13        9        4        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(12,60),initialize=12)
m.x3 = Var(within=Reals,bounds=(12,60),initialize=12)
m.x4 = Var(within=Reals,bounds=(12,60),initialize=12)
m.x5 = Var(within=Reals,bounds=(12,60),initialize=12)
m.i6 = Var(within=Integers,bounds=(12,60),initialize=12)
m.i7 = Var(within=Integers,bounds=(12,60),initialize=12)
m.i8 = Var(within=Integers,bounds=(12,60),initialize=12)
m.i9 = Var(within=Integers,bounds=(12,60),initialize=12)

m.obj = Objective(expr=(0.14427932477276 - m.x2*m.x3/(m.x4*m.x5))**2, sense=minimize)

m.c2 = Constraint(expr=   m.x2 - m.i6 == 0)

m.c3 = Constraint(expr=   m.x3 - m.i7 == 0)

m.c4 = Constraint(expr=   m.x4 - m.i8 == 0)

m.c5 = Constraint(expr=   m.x5 - m.i9 == 0)
