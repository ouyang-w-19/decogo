#  MINLP written by GAMS Convert at 04/21/18 13:52:42
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        1        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          3        1        0        2        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          3        1        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,200),initialize=100)
m.i2 = Var(within=Integers,bounds=(0,200),initialize=100)

m.obj = Objective(expr=100*(0.5 - (0.6 + m.i1)**2 + m.i2)**2 + (0.4 - m.i1)**2, sense=minimize)
