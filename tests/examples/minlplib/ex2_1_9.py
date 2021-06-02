#  NLP written by GAMS Convert at 04/21/18 13:51:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          2        2        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         11       11        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         21       11       10        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0.25)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0.25)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0.25)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0.25)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=-(m.x1*m.x2 + m.x2*m.x3 + m.x3*m.x4 + m.x4*m.x5 + m.x5*m.x6 + m.x6*m.x7 + m.x7*m.x8 + m.x8*m.x9
                        + m.x9*m.x10 + m.x1*m.x3 + m.x2*m.x4 + m.x3*m.x5 + m.x4*m.x6 + m.x5*m.x7 + m.x6*m.x8 + m.x7*m.x9
                        + m.x8*m.x10 + m.x1*m.x9 + m.x1*m.x10 + m.x2*m.x10 + m.x1*m.x5 + m.x4*m.x7), sense=minimize)

m.c2 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 == 1)
