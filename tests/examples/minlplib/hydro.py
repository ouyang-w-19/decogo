#  NLP written by GAMS Convert at 04/21/18 13:52:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         25       19        6        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         32       32        0        0        0        0        0        0
#  FX      1        1        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         67       55       12        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(150,1500),initialize=150)
m.x2 = Var(within=Reals,bounds=(150,1500),initialize=150)
m.x3 = Var(within=Reals,bounds=(150,1500),initialize=150)
m.x4 = Var(within=Reals,bounds=(150,1500),initialize=150)
m.x5 = Var(within=Reals,bounds=(150,1500),initialize=150)
m.x6 = Var(within=Reals,bounds=(150,1500),initialize=150)
m.x7 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(100000,100000),initialize=100000)
m.x26 = Var(within=Reals,bounds=(60000,120000),initialize=60000)
m.x27 = Var(within=Reals,bounds=(60000,120000),initialize=60000)
m.x28 = Var(within=Reals,bounds=(60000,120000),initialize=60000)
m.x29 = Var(within=Reals,bounds=(60000,120000),initialize=60000)
m.x30 = Var(within=Reals,bounds=(60000,120000),initialize=60000)
m.x31 = Var(within=Reals,bounds=(60000,120000),initialize=60000)

m.obj = Objective(expr=82.8*(0.0016*m.x1**2 + 8*m.x1 + 0.0016*m.x2**2 + 8*m.x2 + 0.0016*m.x3**2 + 8*m.x3 + 0.0016*m.x4**
                       2 + 8*m.x4 + 0.0016*m.x5**2 + 8*m.x5 + 0.0016*m.x6**2 + 8*m.x6) + 248400, sense=minimize)

m.c2 = Constraint(expr=   m.x1 + m.x7 - m.x13 >= 1200)

m.c3 = Constraint(expr=   m.x2 + m.x8 - m.x14 >= 1500)

m.c4 = Constraint(expr=   m.x3 + m.x9 - m.x15 >= 1100)

m.c5 = Constraint(expr=   m.x4 + m.x10 - m.x16 >= 1800)

m.c6 = Constraint(expr=   m.x5 + m.x11 - m.x17 >= 950)

m.c7 = Constraint(expr=   m.x6 + m.x12 - m.x18 >= 1300)

m.c8 = Constraint(expr=   12*m.x19 - m.x25 + m.x26 == 24000)

m.c9 = Constraint(expr=   12*m.x20 - m.x26 + m.x27 == 24000)

m.c10 = Constraint(expr=   12*m.x21 - m.x27 + m.x28 == 24000)

m.c11 = Constraint(expr=   12*m.x22 - m.x28 + m.x29 == 24000)

m.c12 = Constraint(expr=   12*m.x23 - m.x29 + m.x30 == 24000)

m.c13 = Constraint(expr=   12*m.x24 - m.x30 + m.x31 == 24000)

m.c14 = Constraint(expr=-8e-5*m.x7**2 + m.x13 == 0)

m.c15 = Constraint(expr=-8e-5*m.x8**2 + m.x14 == 0)

m.c16 = Constraint(expr=-8e-5*m.x9**2 + m.x15 == 0)

m.c17 = Constraint(expr=-8e-5*m.x10**2 + m.x16 == 0)

m.c18 = Constraint(expr=-8e-5*m.x11**2 + m.x17 == 0)

m.c19 = Constraint(expr=-8e-5*m.x12**2 + m.x18 == 0)

m.c20 = Constraint(expr= - 4.97*m.x7 + m.x19 == 330)

m.c21 = Constraint(expr= - 4.97*m.x8 + m.x20 == 330)

m.c22 = Constraint(expr= - 4.97*m.x9 + m.x21 == 330)

m.c23 = Constraint(expr= - 4.97*m.x10 + m.x22 == 330)

m.c24 = Constraint(expr= - 4.97*m.x11 + m.x23 == 330)

m.c25 = Constraint(expr= - 4.97*m.x12 + m.x24 == 330)
