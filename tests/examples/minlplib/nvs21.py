#  MINLP written by GAMS Convert at 04/21/18 13:52:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          3        1        2        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          4        2        0        2        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          8        1        7        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,200),initialize=1)
m.i2 = Var(within=Integers,bounds=(0,200),initialize=1)
m.x3 = Var(within=Reals,bounds=(0,0.2),initialize=0.1)

m.obj = Objective(expr=-0.00201*m.i1**4*m.i2*m.x3**2, sense=minimize)

m.c1 = Constraint(expr=-m.i1**2*m.i2 >= -675)

m.c2 = Constraint(expr=-0.1*m.i1**2*m.x3**2 >= -0.419)
