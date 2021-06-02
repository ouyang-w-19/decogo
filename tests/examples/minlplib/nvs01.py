#  MINLP written by GAMS Convert at 04/21/18 13:52:42
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          4        2        2        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          4        2        0        2        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         10        3        7        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,200),initialize=100)
m.i2 = Var(within=Integers,bounds=(0,200),initialize=100)
m.x3 = Var(within=Reals,bounds=(0,100),initialize=100)

m.obj = Objective(expr=0.04712385*sqrt(900 + m.i1**2)*m.i2, sense=minimize)

m.c1 = Constraint(expr=420.169404664517*sqrt(900 + m.i1**2) - m.x3*m.i1*m.i2 == 0)

m.c2 = Constraint(expr= - m.x3 >= -100)

m.c3 = Constraint(expr=(2960.87631843 + 18505.4769901875*m.i2**2)/(7200 + m.i1**2) - m.x3 >= 0)
