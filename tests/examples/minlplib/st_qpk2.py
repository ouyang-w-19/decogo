#  NLP written by GAMS Convert at 04/21/18 13:54:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         13        1        0       12        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          7        7        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         79       73        6        0
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

m.obj = Objective(expr=0.5*m.x1*m.x2 - m.x1*m.x1 + 0.5*m.x2*m.x1 - m.x2*m.x2 + 0.5*m.x2*m.x3 + 0.5*m.x3*m.x2 - m.x3*m.x3
                        + 0.5*m.x3*m.x4 + 0.5*m.x4*m.x3 - m.x4*m.x4 + 0.5*m.x4*m.x5 + 0.5*m.x5*m.x4 - m.x5*m.x5 + 0.5*
                       m.x5*m.x6 + 0.5*m.x6*m.x5 - m.x6*m.x6, sense=minimize)

m.c1 = Constraint(expr= - m.x1 - 2*m.x2 - 3*m.x3 - 4*m.x4 - 5*m.x5 - 6*m.x6 <= 0)

m.c2 = Constraint(expr= - 2*m.x1 - 3*m.x2 - 4*m.x3 - 5*m.x4 - 6*m.x5 - m.x6 <= 0)

m.c3 = Constraint(expr= - 3*m.x1 - 4*m.x2 - 5*m.x3 - 6*m.x4 - m.x5 - 2*m.x6 <= 0)

m.c4 = Constraint(expr= - 4*m.x1 - 5*m.x2 - 6*m.x3 - m.x4 - 2*m.x5 - 3*m.x6 <= 0)

m.c5 = Constraint(expr= - 5*m.x1 - 6*m.x2 - m.x3 - 2*m.x4 - 3*m.x5 - 4*m.x6 <= 0)

m.c6 = Constraint(expr= - 6*m.x1 - m.x2 - 2*m.x3 - 3*m.x4 - 4*m.x5 - 5*m.x6 <= 0)

m.c7 = Constraint(expr=   m.x1 + 2*m.x2 + 3*m.x3 + 4*m.x4 + 5*m.x5 + 6*m.x6 <= 21)

m.c8 = Constraint(expr=   2*m.x1 + 3*m.x2 + 4*m.x3 + 5*m.x4 + 6*m.x5 + m.x6 <= 21)

m.c9 = Constraint(expr=   3*m.x1 + 4*m.x2 + 5*m.x3 + 6*m.x4 + m.x5 + 2*m.x6 <= 21)

m.c10 = Constraint(expr=   4*m.x1 + 5*m.x2 + 6*m.x3 + m.x4 + 2*m.x5 + 3*m.x6 <= 21)

m.c11 = Constraint(expr=   5*m.x1 + 6*m.x2 + m.x3 + 2*m.x4 + 3*m.x5 + 4*m.x6 <= 21)

m.c12 = Constraint(expr=   6*m.x1 + m.x2 + 2*m.x3 + 3*m.x4 + 4*m.x5 + 5*m.x6 <= 21)
