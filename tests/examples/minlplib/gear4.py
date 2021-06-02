#  MINLP written by GAMS Convert at 04/21/18 13:52:21
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          2        2        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          7        3        0        4        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          9        5        4        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(12,60),initialize=12)
m.i2 = Var(within=Integers,bounds=(12,60),initialize=12)
m.i3 = Var(within=Integers,bounds=(12,60),initialize=12)
m.i4 = Var(within=Integers,bounds=(12,60),initialize=12)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   m.x6 + m.x7, sense=minimize)

m.c1 = Constraint(expr=-1000000*m.i1*m.i2/(m.i3*m.i4) - m.x6 + m.x7 == -144279.32477276)
