#  MINLP written by GAMS Convert at 04/21/18 13:52:21
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          5        5        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         29        5       24        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         33       29        4        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(12,60),initialize=12)
m.x3 = Var(within=Reals,bounds=(12,60),initialize=12)
m.x4 = Var(within=Reals,bounds=(12,60),initialize=12)
m.x5 = Var(within=Reals,bounds=(12,60),initialize=12)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b15 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b18 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b19 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b21 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b23 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b24 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b25 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b26 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b27 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b28 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b29 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=(0.14427932477276 - m.x2*m.x3/(m.x4*m.x5))**2, sense=minimize)

m.c2 = Constraint(expr=   m.x2 - m.b6 - 2*m.b7 - 4*m.b8 - 8*m.b9 - 16*m.b10 - 32*m.b11 == 0)

m.c3 = Constraint(expr=   m.x3 - m.b12 - 2*m.b13 - 4*m.b14 - 8*m.b15 - 16*m.b16 - 32*m.b17 == 0)

m.c4 = Constraint(expr=   m.x4 - m.b18 - 2*m.b19 - 4*m.b20 - 8*m.b21 - 16*m.b22 - 32*m.b23 == 0)

m.c5 = Constraint(expr=   m.x5 - m.b24 - 2*m.b25 - 4*m.b26 - 8*m.b27 - 16*m.b28 - 32*m.b29 == 0)
