#  NLP written by GAMS Convert at 04/21/18 13:51:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          6        1        0        5        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         11       11        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         57       47       10        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x6 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x7 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x10 = Var(within=Reals,bounds=(0,1),initialize=1)

m.obj = Objective(expr=48*m.x1 - 0.5*(100*m.x1*m.x1 + 100*m.x2*m.x2 + 100*m.x3*m.x3 + 100*m.x4*m.x4 + 100*m.x5*m.x5 + 
                       100*m.x6*m.x6 + 100*m.x7*m.x7 + 100*m.x8*m.x8 + 100*m.x9*m.x9 + 100*m.x10*m.x10) + 42*m.x2 + 48*
                       m.x3 + 45*m.x4 + 44*m.x5 + 41*m.x6 + 47*m.x7 + 42*m.x8 + 45*m.x9 + 46*m.x10, sense=minimize)

m.c2 = Constraint(expr= - 2*m.x1 - 6*m.x2 - m.x3 - 3*m.x5 - 3*m.x6 - 2*m.x7 - 6*m.x8 - 2*m.x9 - 2*m.x10 <= -4)

m.c3 = Constraint(expr=   6*m.x1 - 5*m.x2 + 8*m.x3 - 3*m.x4 + m.x6 + 3*m.x7 + 8*m.x8 + 9*m.x9 - 3*m.x10 <= 22)

m.c4 = Constraint(expr= - 5*m.x1 + 6*m.x2 + 5*m.x3 + 3*m.x4 + 8*m.x5 - 8*m.x6 + 9*m.x7 + 2*m.x8 - 9*m.x10 <= -6)

m.c5 = Constraint(expr=   9*m.x1 + 5*m.x2 - 9*m.x4 + m.x5 - 8*m.x6 + 3*m.x7 - 9*m.x8 - 9*m.x9 - 3*m.x10 <= -23)

m.c6 = Constraint(expr= - 8*m.x1 + 7*m.x2 - 4*m.x3 - 5*m.x4 - 9*m.x5 + m.x6 - 7*m.x7 - m.x8 + 3*m.x9 - 2*m.x10 <= -12)
