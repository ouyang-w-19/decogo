#  NLP written by GAMS Convert at 04/21/18 13:54:00
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          2        0        0        2        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          2        2        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          4        0        4        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(1,5.5),initialize=1)
m.x2 = Var(within=Reals,bounds=(1,5.5),initialize=1)

m.obj = Objective(expr=m.x1, sense=minimize)

m.c1 = Constraint(expr=0.25*m.x1 - 0.0625*m.x1**2 - 0.0625*m.x2**2 + 0.5*m.x2 <= 1)

m.c2 = Constraint(expr=0.0714285714285714*m.x1**2 + 0.0714285714285714*m.x2**2 - 0.428571428571429*m.x1 - 
                       0.428571428571429*m.x2 <= -1)
