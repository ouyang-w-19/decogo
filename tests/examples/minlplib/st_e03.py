#  NLP written by GAMS Convert at 04/21/18 13:54:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          8        7        1        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         11       11        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         28       17       11        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(1,2000),initialize=1)
m.x2 = Var(within=Reals,bounds=(1,16000),initialize=1)
m.x3 = Var(within=Reals,bounds=(0,120),initialize=0)
m.x4 = Var(within=Reals,bounds=(1,5000),initialize=1)
m.x5 = Var(within=Reals,bounds=(0,2000),initialize=0)
m.x6 = Var(within=Reals,bounds=(85,93),initialize=85)
m.x7 = Var(within=Reals,bounds=(90,95),initialize=90)
m.x8 = Var(within=Reals,bounds=(3,12),initialize=3)
m.x9 = Var(within=Reals,bounds=(1.2,4),initialize=1.2)
m.x10 = Var(within=Reals,bounds=(145,162),initialize=145)

m.obj = Objective(expr=-0.063*m.x4*m.x7 + 5.04*m.x1 + 0.035*m.x2 + 10*m.x3 + 3.36*m.x5, sense=minimize)

m.c1 = Constraint(expr=   m.x1 - 1.22*m.x4 + m.x5 == 0)

m.c2 = Constraint(expr=   m.x9 + 0.222*m.x10 == 35.82)

m.c3 = Constraint(expr=   3*m.x7 - m.x10 == 133)

m.c4 = Constraint(expr=0.038*m.x8**2 - 1.098*m.x8 - 0.325*m.x6 + m.x7 == 57.425)

m.c5 = Constraint(expr=m.x4*m.x9*m.x6 + 1000*m.x3*m.x6 - 98000*m.x3 == 0)

m.c6 = Constraint(expr=-m.x1*m.x8 + m.x2 + m.x5 == 0)

m.c7 = Constraint(expr=0.13167*m.x8*m.x1 + 1.12*m.x1 - 0.00667*m.x8**2*m.x1 - m.x4 >= 0)
