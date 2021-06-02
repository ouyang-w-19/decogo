#  NLP written by GAMS Convert at 04/21/18 13:52:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         26       20        3        3        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         30       30        0        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         81       60       21        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(1000,1000),initialize=1000)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=1000)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=1000)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=1000)
m.x5 = Var(within=Reals,bounds=(100,None),initialize=100)
m.x6 = Var(within=Reals,bounds=(100,None),initialize=100)
m.x7 = Var(within=Reals,bounds=(100,None),initialize=100)
m.x8 = Var(within=Reals,bounds=(100,400),initialize=400)
m.x9 = Var(within=Reals,bounds=(100,400),initialize=400)
m.x10 = Var(within=Reals,bounds=(100,400),initialize=400)
m.x11 = Var(within=Reals,bounds=(100,100),initialize=100)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=100)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=100)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=100)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(0.01,None),initialize=1)
m.x26 = Var(within=Reals,bounds=(0.01,None),initialize=1)
m.x27 = Var(within=Reals,bounds=(0.01,None),initialize=1)
m.x28 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=-m.x26**0.944*m.x25*m.x27**0.891136, sense=minimize)

m.c2 = Constraint(expr=-0.01*(0.5*m.x5**0.5 + 0.5*(1004.72366 - m.x8 - m.x15)**0.5)**2 + m.x25 == 0)

m.c3 = Constraint(expr=-0.01*(0.5*m.x6**0.5 + 0.5*(1004.72366 - m.x9 - m.x16)**0.5)**2 + m.x26 == 0)

m.c4 = Constraint(expr=-0.01*(0.5*m.x7**0.5 + 0.5*(1004.72366 - m.x10 - m.x17)**0.5)**2 + m.x27 == 0)

m.c5 = Constraint(expr= - 0.07*m.x2 - m.x8 + m.x28 == 0)

m.c6 = Constraint(expr= - 0.07*m.x3 - m.x9 + m.x29 == 0)

m.c7 = Constraint(expr= - 0.07*m.x4 - m.x10 + m.x30 == 0)

m.c8 = Constraint(expr=   m.x22 - 0.2*m.x28 == 0)

m.c9 = Constraint(expr=   m.x23 - 0.2*m.x29 == 0)

m.c10 = Constraint(expr=   m.x24 - 0.2*m.x30 == 0)

m.c11 = Constraint(expr=   m.x5 + m.x19 + m.x22 - m.x28 == 0)

m.c12 = Constraint(expr=   m.x6 + m.x20 + m.x23 - m.x29 == 0)

m.c13 = Constraint(expr=   m.x7 + m.x21 + m.x24 - m.x30 == 0)

m.c14 = Constraint(expr=   m.x1 - m.x2 + m.x11 - m.x12 + m.x19 == 0)

m.c15 = Constraint(expr=   m.x2 - m.x3 + m.x12 - m.x13 + m.x20 == 0)

m.c16 = Constraint(expr=   m.x3 - m.x4 + m.x13 - m.x14 + m.x21 == 0)

m.c17 = Constraint(expr=m.x15*(m.x12 - 0.255905*m.x5) == 1)

m.c18 = Constraint(expr=m.x16*(m.x13 - 0.255905*m.x6) == 1)

m.c19 = Constraint(expr=m.x17*(m.x14 - 0.255905*m.x7) == 1)

m.c20 = Constraint(expr=   m.x4 + m.x14 == 1100)

m.c21 = Constraint(expr= - 0.25846405*m.x5 + m.x12 >= 0)

m.c22 = Constraint(expr= - 0.25846405*m.x6 + m.x13 >= 0)

m.c23 = Constraint(expr= - 0.25846405*m.x7 + m.x14 >= 0)

m.c24 = Constraint(expr=   m.x8 + m.x15 <= 904.251294)

m.c25 = Constraint(expr=   m.x9 + m.x16 <= 904.251294)

m.c26 = Constraint(expr=   m.x10 + m.x17 <= 904.251294)
