#  MINLP written by GAMS Convert at 04/21/18 13:54:00
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          3        1        0        2        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          3        2        0        1        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          7        5        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,10),initialize=0)
m.i3 = Var(within=Integers,bounds=(0,10),initialize=0)

m.obj = Objective(expr=1.1*((-10 + 2*m.x2)**2 + (-5 + m.i3)**2) + sin((-10 + 2*m.x2)**2 + (-5 + m.i3)**2)
                       , sense=minimize)

m.c1 = Constraint(expr=   0.7*m.x2 + m.i3 <= 7)

m.c2 = Constraint(expr=   2.5*m.x2 + m.i3 <= 19)
