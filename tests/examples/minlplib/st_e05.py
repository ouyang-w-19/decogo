#  NLP written by GAMS Convert at 04/21/18 13:54:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          4        4        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          6        6        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         11        7        4        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,15834),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,36250),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,10000),initialize=0)
m.x4 = Var(within=Reals,bounds=(100,300),initialize=100)
m.x5 = Var(within=Reals,bounds=(100,400),initialize=100)

m.obj = Objective(expr=   m.x1 + m.x2 + m.x3, sense=minimize)

m.c1 = Constraint(expr=100000*m.x4 - 120*m.x1*(300 - m.x4) == 10000000)

m.c2 = Constraint(expr=100000*m.x5 - 80*m.x2*(400 - m.x5) - 100000*m.x4 == 0)

m.c3 = Constraint(expr= - 4000*m.x3 - 100000*m.x5 == -50000000)
