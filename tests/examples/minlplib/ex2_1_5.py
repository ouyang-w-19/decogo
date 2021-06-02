#  NLP written by GAMS Convert at 04/21/18 13:51:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         12        1        0       11        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         11       11        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        112      105        7        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x2 = Var(within=Reals,bounds=(0,1),initialize=0.90755)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=0.71509)
m.x6 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x7 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=0.91698)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x10 = Var(within=Reals,bounds=(0,1),initialize=1)

m.obj = Objective(expr=(-0.5*(10*m.x1*m.x1 + 10*m.x2*m.x2 + 10*m.x3*m.x3 + 10*m.x4*m.x4 + 10*m.x5*m.x5 + 10*m.x6*m.x6 + 
                       10*m.x7*m.x7)) - 20*m.x1 - 80*m.x2 - 20*m.x3 - 50*m.x4 - 60*m.x5 - 90*m.x6 + 10*m.x8 + 10*m.x9
                        + 10*m.x10, sense=minimize)

m.c2 = Constraint(expr= - 2*m.x1 - 6*m.x2 - m.x3 - 3*m.x5 - 3*m.x6 - 2*m.x7 - 6*m.x8 - 2*m.x9 - 2*m.x10 <= -4)

m.c3 = Constraint(expr=   6*m.x1 - 5*m.x2 + 8*m.x3 - 3*m.x4 + m.x6 + 3*m.x7 + 8*m.x8 + 9*m.x9 - 3*m.x10 <= 22)

m.c4 = Constraint(expr= - 5*m.x1 + 6*m.x2 + 5*m.x3 + 3*m.x4 + 8*m.x5 - 8*m.x6 + 9*m.x7 + 2*m.x8 - 9*m.x10 <= -6)

m.c5 = Constraint(expr=   9*m.x1 + 5*m.x2 - 9*m.x4 + m.x5 - 8*m.x6 + 3*m.x7 - 9*m.x8 - 9*m.x9 - 3*m.x10 <= -23)

m.c6 = Constraint(expr= - 8*m.x1 + 7*m.x2 - 4*m.x3 - 5*m.x4 - 9*m.x5 + m.x6 - 7*m.x7 - m.x8 + 3*m.x9 - 2*m.x10 <= -12)

m.c7 = Constraint(expr= - 7*m.x1 - 5*m.x2 - 2*m.x3 - 6*m.x5 - 6*m.x6 - 7*m.x7 - 6*m.x8 + 7*m.x9 + 7*m.x10 <= -3)

m.c8 = Constraint(expr=   m.x1 - 3*m.x2 - 3*m.x3 - 4*m.x4 - m.x5 - 4*m.x7 + m.x8 + 6*m.x9 <= 1)

m.c9 = Constraint(expr=   m.x1 - 2*m.x2 + 6*m.x3 + 9*m.x4 - 7*m.x6 + 9*m.x7 - 9*m.x8 - 6*m.x9 + 4*m.x10 <= 12)

m.c10 = Constraint(expr= - 4*m.x1 + 6*m.x2 + 7*m.x3 + 2*m.x4 + 2*m.x5 + 6*m.x7 + 6*m.x8 - 7*m.x9 + 4*m.x10 <= 15)

m.c11 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 <= 9)

m.c12 = Constraint(expr= - m.x1 - m.x2 - m.x3 - m.x4 - m.x5 - m.x6 - m.x7 - m.x8 - m.x9 - m.x10 <= -1)
