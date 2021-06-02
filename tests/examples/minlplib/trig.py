#  NLP written by GAMS Convert at 04/21/18 13:55:04
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          2        1        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          2        2        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          3        1        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(-2,5),initialize=1)

m.obj = Objective(expr=sin(11*m.x1) + cos(13*m.x1) - sin(17*m.x1) - cos(19*m.x1), sense=minimize)

m.c2 = Constraint(expr=5*sin(m.x1) - m.x1 <= 0)
