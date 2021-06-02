#  NLP written by GAMS Convert at 04/21/18 13:54:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         14        1        2       11        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         11       11        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        116      106       10        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,100),initialize=0)

m.obj = Objective(expr=m.x1*m.x6 - m.x1 - m.x6 + m.x2*m.x7 - 2*m.x2 - 2*m.x7 + m.x3*m.x8 - 3*m.x3 - 3*m.x8 + m.x4*m.x9
                        - 4*m.x4 - 4*m.x9 + m.x5*m.x10 - 5*m.x5 - 5*m.x10, sense=minimize)

m.c1 = Constraint(expr=   m.x1 + 7*m.x2 + 5*m.x3 + 5*m.x4 - 6*m.x6 - 3*m.x7 - 3*m.x8 + 5*m.x9 - 7*m.x10 <= 80)

m.c2 = Constraint(expr= - 3*m.x1 + 3*m.x2 + 8*m.x3 + 7*m.x4 - 9*m.x5 - 7*m.x6 - 9*m.x7 + 8*m.x9 - 7*m.x10 <= 57)

m.c3 = Constraint(expr=   m.x1 + m.x3 + 3*m.x4 + 8*m.x5 + 9*m.x6 + 9*m.x8 - 7*m.x9 - 8*m.x10 <= 92)

m.c4 = Constraint(expr= - m.x1 - 2*m.x2 + 2*m.x3 + 9*m.x5 + 5*m.x6 - 3*m.x7 + m.x8 - m.x9 - 5*m.x10 <= 55)

m.c5 = Constraint(expr= - 5*m.x1 + 8*m.x2 - 8*m.x3 + 3*m.x5 + 4*m.x7 - 5*m.x8 - 2*m.x9 + 9*m.x10 <= 76)

m.c6 = Constraint(expr=   4*m.x1 - m.x2 + 6*m.x3 - 4*m.x4 - 7*m.x5 - 8*m.x6 - 7*m.x7 + 6*m.x8 - 2*m.x9 - 9*m.x10 <= 14)

m.c7 = Constraint(expr=   7*m.x2 + 4*m.x3 + 9*m.x5 - 6*m.x8 - 5*m.x9 - 5*m.x10 <= 47)

m.c8 = Constraint(expr= - 5*m.x1 - m.x2 + 7*m.x4 - m.x5 + 2*m.x6 + 5*m.x7 - 8*m.x8 - 5*m.x9 + 2*m.x10 <= 51)

m.c9 = Constraint(expr= - 4*m.x1 - 7*m.x2 - 9*m.x4 + 2*m.x5 + 6*m.x6 - 9*m.x7 + m.x8 - 5*m.x9 <= 36)

m.c10 = Constraint(expr= - 2*m.x1 + 6*m.x2 + 8*m.x4 - 6*m.x5 + 8*m.x6 + 8*m.x7 + 5*m.x8 + 2*m.x9 - 7*m.x10 <= 92)

m.c11 = Constraint(expr=   m.x1 + m.x2 + m.x3 - 2*m.x4 + m.x5 + m.x6 + m.x7 + 4*m.x8 + m.x9 + 3*m.x10 <= 200)

m.c12 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 >= 1)

m.c13 = Constraint(expr=   m.x6 + m.x7 + m.x8 + m.x9 + m.x10 >= 2)
