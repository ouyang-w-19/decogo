#  MINLP written by GAMS Convert at 04/21/18 13:54:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          3        2        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          3        2        0        1        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          7        1        6        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(15,25),initialize=15)
m.x2 = Var(within=Reals,bounds=(3,5.5),initialize=3)

m.obj = Objective(expr=2*m.x2**2 + 0.008*m.i1**3 - 3.2*m.x2*m.i1 - 2*m.i1, sense=minimize)

m.c1 = Constraint(expr=(-11 + m.x2**2 - 6*m.x2 + 0.8*m.i1)*((3.25*m.x2 - 0.62*m.i1)**2 + (-6.35 + 0.2*m.i1 + m.x2)**2)*(
                       (3.55*m.x2 - 0.66*m.i1)**2 + (-6.85 + 0.2*m.i1 + m.x2)**2)*((3.6*m.x2 - 0.7*m.i1)**2 + (-7.1 + 
                       0.2*m.i1 + m.x2)**2)*((3.8*m.x2 - 0.82*m.i1)**2 + (-7.9 + 0.2*m.i1 + m.x2)**2) == 0)

m.c2 = Constraint(expr=0.6*m.i1 - 0.2*m.x2*m.i1 + exp((-3) + m.x2) <= 1)
