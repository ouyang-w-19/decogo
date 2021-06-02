#  NLP written by GAMS Convert at 04/21/18 13:54:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          2        1        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          7        7        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         13        7        6        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,99),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,99),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,99),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,99),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,99),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,99),initialize=0)

m.obj = Objective(expr=10.5*m.x1 - 1.5*m.x1**2 - m.x2**2 - 3.95*m.x2 - m.x3**2 + 3*m.x3 - 2*m.x4**2 + 5*m.x4 - m.x5**2
                        + 1.5*m.x5 - 2.5*m.x6**2 - 1.5*m.x6, sense=minimize)

m.c1 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 <= 10000000000)
