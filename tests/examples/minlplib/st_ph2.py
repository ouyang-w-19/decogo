#  NLP written by GAMS Convert at 04/21/18 13:54:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          6        1        0        5        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          7        7        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         31       25        6        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=6*m.x1 - 3*m.x1**2 - 2.5*m.x2**2 + 5*m.x2 - 2*m.x3**2 + 4*m.x3 - 1.5*m.x4**2 + 3*m.x4 - m.x5**2
                        + 2*m.x5 - 0.5*m.x6**2 + m.x6, sense=minimize)

m.c1 = Constraint(expr=   6*m.x1 + m.x2 + 9*m.x4 + 3*m.x5 + 5*m.x6 <= 96)

m.c2 = Constraint(expr=   m.x1 + 7*m.x3 + 6*m.x4 + 2*m.x5 + 2*m.x6 <= 72)

m.c3 = Constraint(expr=   5*m.x1 + 4*m.x2 + m.x3 + 3*m.x4 + 8*m.x5 <= 84)

m.c4 = Constraint(expr=   9*m.x1 + m.x2 + 2*m.x4 + 7*m.x5 + 6*m.x6 <= 100)

m.c5 = Constraint(expr=   2*m.x1 + 6*m.x4 + 3*m.x5 + 9*m.x6 <= 80)
