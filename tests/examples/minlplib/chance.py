#  NLP written by GAMS Convert at 04/21/18 13:51:14
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          4        2        2        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        5        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         17       13        4        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,None),initialize=0.685244910300343)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0.0126990526103601)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0.302056037089293)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   24.55*m.x2 + 26.75*m.x3 + 39*m.x4 + 40.5*m.x5, sense=minimize)

m.c2 = Constraint(expr=   m.x2 + m.x3 + m.x4 + m.x5 == 1)

m.c3 = Constraint(expr=12*m.x2 - 1.645*sqrt(0.28*m.x2**2 + 0.19*m.x3**2 + 20.5*m.x4**2 + 0.62*m.x5**2) + 11.9*m.x3 + 
                       41.8*m.x4 + 52.1*m.x5 >= 21)

m.c4 = Constraint(expr=   2.3*m.x2 + 5.6*m.x3 + 11.1*m.x4 + 1.3*m.x5 >= 5)
