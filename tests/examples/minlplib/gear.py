#  MINLP written by GAMS Convert at 04/21/18 13:52:21
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        1        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        1        0        4        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          5        1        4        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(12,60),initialize=12)
m.i2 = Var(within=Integers,bounds=(12,60),initialize=12)
m.i3 = Var(within=Integers,bounds=(12,60),initialize=12)
m.i4 = Var(within=Integers,bounds=(12,60),initialize=12)

m.obj = Objective(expr=(0.14427932477276 - m.i1*m.i2/(m.i3*m.i4))**2, sense=minimize)
