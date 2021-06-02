#  NLP written by GAMS Convert at 04/21/18 13:53:09
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         50       23        0       27        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         34       34        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        220      180       40        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,75),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,75),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,75),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,75),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,75),initialize=0)

m.obj = Objective(expr= - 9*m.x10 - 18*m.x11 - 8*m.x12 - 3*m.x13 - 13*m.x14 - 22*m.x15 - 12*m.x16 - 7*m.x17 - 14*m.x18
                        - 23*m.x19 - 13*m.x20 - 8*m.x21 - 6*m.x22 - 15*m.x23 - 5*m.x24 - 11*m.x26 - 20*m.x27 - 10*m.x28
                        - 5*m.x29, sense=minimize)

m.c2 = Constraint(expr=   m.x10 + m.x11 + m.x12 + m.x13 <= 75)

m.c3 = Constraint(expr=   m.x14 + m.x15 + m.x16 + m.x17 <= 75)

m.c4 = Constraint(expr=   m.x18 + m.x19 + m.x20 + m.x21 <= 75)

m.c5 = Constraint(expr=   m.x22 + m.x23 + m.x24 + m.x25 <= 75)

m.c6 = Constraint(expr=   m.x26 + m.x27 + m.x28 + m.x29 <= 75)

m.c7 = Constraint(expr=   m.x10 + m.x11 + m.x12 + m.x13 + m.x14 + m.x15 + m.x16 + m.x17 <= 75)

m.c8 = Constraint(expr=   m.x18 + m.x19 + m.x20 + m.x21 + m.x22 + m.x23 + m.x24 + m.x25 + m.x26 + m.x27 + m.x28 + m.x29
                        <= 75)

m.c9 = Constraint(expr=   m.x10 + m.x14 + m.x18 + m.x22 + m.x26 <= 10)

m.c10 = Constraint(expr=   m.x11 + m.x15 + m.x19 + m.x23 + m.x27 <= 25)

m.c11 = Constraint(expr=   m.x12 + m.x16 + m.x20 + m.x24 + m.x28 <= 30)

m.c12 = Constraint(expr=   m.x13 + m.x17 + m.x21 + m.x25 + m.x29 <= 10)

m.c13 = Constraint(expr= - 2*m.x10 + m.x14 + m.x18 - 2*m.x26 <= 0)

m.c14 = Constraint(expr=   3*m.x10 - 2*m.x14 + 2.5*m.x18 - 0.3*m.x26 <= 0)

m.c15 = Constraint(expr=   0.75*m.x10 - 0.25*m.x14 - 0.25*m.x18 - 0.25*m.x22 + 0.75*m.x26 <= 0)

m.c16 = Constraint(expr= - 0.25*m.x10 + 1.25*m.x14 + 0.15*m.x18 + 0.25*m.x22 + 0.85*m.x26 <= 0)

m.c17 = Constraint(expr= - 3*m.x11 - m.x23 - 3*m.x27 <= 0)

m.c18 = Constraint(expr=   3.5*m.x11 - 1.5*m.x15 + 3*m.x19 + 0.5*m.x23 + 0.2*m.x27 <= 0)

m.c19 = Constraint(expr=   0.5*m.x11 - 0.5*m.x15 - 0.5*m.x19 - 0.5*m.x23 + 0.5*m.x27 <= 0)

m.c20 = Constraint(expr= - m.x11 + 0.5*m.x15 - 0.6*m.x19 - 0.5*m.x23 + 0.1*m.x27 <= 0)

m.c21 = Constraint(expr= - 0.5*m.x12 + 2.5*m.x16 + 2.5*m.x20 + 1.5*m.x24 - 0.5*m.x28 <= 0)

m.c22 = Constraint(expr=   0.5*m.x12 - 4.5*m.x16 - 2.5*m.x24 - 2.8*m.x28 <= 0)

m.c23 = Constraint(expr=   0.1*m.x12 - 0.9*m.x16 - 0.9*m.x20 - 0.9*m.x24 + 0.1*m.x28 <= 0)

m.c24 = Constraint(expr= - 0.3*m.x12 + 1.2*m.x16 + 0.1*m.x20 + 0.2*m.x24 + 0.8*m.x28 <= 0)

m.c25 = Constraint(expr= - 2*m.x13 + m.x17 + m.x21 - 2*m.x29 <= 0)

m.c26 = Constraint(expr=   2*m.x13 - 3*m.x17 + 1.5*m.x21 - m.x25 - 1.3*m.x29 <= 0)

m.c27 = Constraint(expr= - m.x17 - m.x21 - m.x25 <= 0)

m.c28 = Constraint(expr= - 1.3*m.x13 + 0.2*m.x17 - 0.9*m.x21 - 0.8*m.x25 - 0.2*m.x29 <= 0)

m.c29 = Constraint(expr=   m.x2 + m.x3 + m.x4 + m.x5 == 1)

m.c30 = Constraint(expr=   m.x6 + m.x7 + m.x8 + m.x9 == 1)

m.c31 = Constraint(expr=-m.x2*m.x30 + m.x10 == 0)

m.c32 = Constraint(expr=-m.x3*m.x30 + m.x11 == 0)

m.c33 = Constraint(expr=-m.x4*m.x30 + m.x12 == 0)

m.c34 = Constraint(expr=-m.x5*m.x30 + m.x13 == 0)

m.c35 = Constraint(expr=-m.x2*m.x31 + m.x14 == 0)

m.c36 = Constraint(expr=-m.x3*m.x31 + m.x15 == 0)

m.c37 = Constraint(expr=-m.x4*m.x31 + m.x16 == 0)

m.c38 = Constraint(expr=-m.x5*m.x31 + m.x17 == 0)

m.c39 = Constraint(expr=-m.x6*m.x32 + m.x18 == 0)

m.c40 = Constraint(expr=-m.x7*m.x32 + m.x19 == 0)

m.c41 = Constraint(expr=-m.x8*m.x32 + m.x20 == 0)

m.c42 = Constraint(expr=-m.x9*m.x32 + m.x21 == 0)

m.c43 = Constraint(expr=-m.x6*m.x33 + m.x22 == 0)

m.c44 = Constraint(expr=-m.x7*m.x33 + m.x23 == 0)

m.c45 = Constraint(expr=-m.x8*m.x33 + m.x24 == 0)

m.c46 = Constraint(expr=-m.x9*m.x33 + m.x25 == 0)

m.c47 = Constraint(expr=-m.x6*m.x34 + m.x26 == 0)

m.c48 = Constraint(expr=-m.x7*m.x34 + m.x27 == 0)

m.c49 = Constraint(expr=-m.x8*m.x34 + m.x28 == 0)

m.c50 = Constraint(expr=-m.x9*m.x34 + m.x29 == 0)
