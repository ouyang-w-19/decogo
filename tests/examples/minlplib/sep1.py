#  MINLP written by GAMS Convert at 04/21/18 13:54:10
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         32       23        5        4        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         30       28        2        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         99       87       12        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,50),initialize=10)
m.x2 = Var(within=Reals,bounds=(0,50),initialize=2.5)
m.x3 = Var(within=Reals,bounds=(0,50),initialize=4)
m.x4 = Var(within=Reals,bounds=(0,50),initialize=14)
m.x5 = Var(within=Reals,bounds=(0,25),initialize=8)
m.x6 = Var(within=Reals,bounds=(0,25),initialize=25)
m.x7 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,1),initialize=0.1)
m.x26 = Var(within=Reals,bounds=(0,1),initialize=0.1)
m.x27 = Var(within=Reals,bounds=(0,1),initialize=0.1)
m.b28 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b29 = Var(within=Binary,bounds=(0,1),initialize=0.5)

m.obj = Objective(expr= - 35*m.x1 - 30*m.x4 + 10*m.x5 + 8*m.x6 + m.x9 + m.x10 + 4*m.x11 + 4*m.x12 + 50*m.b28 + 2*m.b29
                       , sense=minimize)

m.c1 = Constraint(expr= - 0.55*m.x5 - 0.5*m.x6 + m.x7 == 0)

m.c2 = Constraint(expr= - 0.45*m.x5 - 0.5*m.x6 + m.x8 == 0)

m.c3 = Constraint(expr=-m.x25*m.x7 + m.x9 == 0)

m.c4 = Constraint(expr=-m.x25*m.x8 + m.x10 == 0)

m.c5 = Constraint(expr=-m.x26*m.x7 + m.x11 == 0)

m.c6 = Constraint(expr=-m.x26*m.x8 + m.x12 == 0)

m.c7 = Constraint(expr=-m.x27*m.x7 + m.x13 == 0)

m.c8 = Constraint(expr=-m.x27*m.x8 + m.x14 == 0)

m.c9 = Constraint(expr= - m.x7 + m.x9 + m.x11 + m.x13 + m.x15 == 0)

m.c10 = Constraint(expr= - m.x8 + m.x10 + m.x12 + m.x14 + m.x16 == 0)

m.c11 = Constraint(expr= - 0.85*m.x9 + m.x17 == 0)

m.c12 = Constraint(expr= - 0.2*m.x10 + m.x18 == 0)

m.c13 = Constraint(expr= - 0.15*m.x9 + m.x19 == 0)

m.c14 = Constraint(expr= - 0.8*m.x10 + m.x20 == 0)

m.c15 = Constraint(expr= - 0.975*m.x11 + m.x21 == 0)

m.c16 = Constraint(expr= - 0.05*m.x12 + m.x22 == 0)

m.c17 = Constraint(expr= - 0.025*m.x11 + m.x23 == 0)

m.c18 = Constraint(expr= - 0.95*m.x12 + m.x24 == 0)

m.c19 = Constraint(expr=   m.x1 - m.x13 - m.x17 - m.x21 == 0)

m.c20 = Constraint(expr=   m.x2 - m.x14 - m.x18 - m.x22 == 0)

m.c21 = Constraint(expr=   m.x3 - m.x15 - m.x19 - m.x23 == 0)

m.c22 = Constraint(expr=   m.x4 - m.x16 - m.x20 - m.x24 == 0)

m.c23 = Constraint(expr=   m.x9 + m.x10 - 2.5*m.b29 >= 0)

m.c24 = Constraint(expr=   m.x9 + m.x10 - 25*m.b29 <= 0)

m.c25 = Constraint(expr=   m.x11 + m.x12 - 2.5*m.b28 >= 0)

m.c26 = Constraint(expr=   m.x11 + m.x12 - 25*m.b28 <= 0)

m.c27 = Constraint(expr=   m.x1 - 4*m.x2 >= 0)

m.c28 = Constraint(expr= - 3*m.x3 + m.x4 >= 0)

m.c29 = Constraint(expr=   m.x1 + m.x2 <= 15)

m.c30 = Constraint(expr=   m.x3 + m.x4 <= 18)

m.c31 = Constraint(expr=   m.b28 + m.b29 >= 1)
