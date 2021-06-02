#  NLP written by GAMS Convert at 04/21/18 13:53:09
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         58       23        0       35        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         34       34        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        255      215       40        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,10),initialize=0)

m.obj = Objective(expr= - 9*m.x15 - 18*m.x16 - 8*m.x17 - 3*m.x18 - 13*m.x19 - 22*m.x20 - 12*m.x21 - 7*m.x22 - 14*m.x23
                        - 23*m.x24 - 13*m.x25 - 8*m.x26 - 6*m.x27 - 15*m.x28 - 5*m.x29 - 11*m.x31 - 20*m.x32 - 10*m.x33
                        - 5*m.x34, sense=minimize)

m.c2 = Constraint(expr=   m.x15 + m.x16 + m.x17 + m.x18 <= 75)

m.c3 = Constraint(expr=   m.x19 + m.x20 + m.x21 + m.x22 <= 75)

m.c4 = Constraint(expr=   m.x23 + m.x24 + m.x25 + m.x26 <= 75)

m.c5 = Constraint(expr=   m.x27 + m.x28 + m.x29 + m.x30 <= 75)

m.c6 = Constraint(expr=   m.x31 + m.x32 + m.x33 + m.x34 <= 75)

m.c7 = Constraint(expr=   m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20 + m.x21 + m.x22 <= 75)

m.c8 = Constraint(expr=   m.x23 + m.x24 + m.x25 + m.x26 + m.x27 + m.x28 + m.x29 + m.x30 + m.x31 + m.x32 + m.x33 + m.x34
                        <= 75)

m.c9 = Constraint(expr=   m.x15 + m.x19 + m.x23 + m.x27 + m.x31 <= 10)

m.c10 = Constraint(expr=   m.x16 + m.x20 + m.x24 + m.x28 + m.x32 <= 25)

m.c11 = Constraint(expr=   m.x17 + m.x21 + m.x25 + m.x29 + m.x33 <= 30)

m.c12 = Constraint(expr=   m.x18 + m.x22 + m.x26 + m.x30 + m.x34 <= 10)

m.c13 = Constraint(expr= - 2*m.x15 + m.x19 + m.x23 - 2*m.x31 <= 0)

m.c14 = Constraint(expr=   3*m.x15 - 2*m.x19 + 2.5*m.x23 - 0.3*m.x31 <= 0)

m.c15 = Constraint(expr=   0.75*m.x15 - 0.25*m.x19 - 0.25*m.x23 - 0.25*m.x27 + 0.75*m.x31 <= 0)

m.c16 = Constraint(expr= - 0.25*m.x15 + 1.25*m.x19 + 0.15*m.x23 + 0.25*m.x27 + 0.85*m.x31 <= 0)

m.c17 = Constraint(expr= - m.x15 - 2*m.x19 + m.x23 - 3*m.x27 - 3*m.x31 <= 0)

m.c18 = Constraint(expr=   4*m.x15 - m.x19 + 5*m.x23 - m.x27 + 2*m.x31 <= 0)

m.c19 = Constraint(expr= - 3*m.x16 - m.x28 - 3*m.x32 <= 0)

m.c20 = Constraint(expr=   3.5*m.x16 - 1.5*m.x20 + 3*m.x24 + 0.5*m.x28 + 0.2*m.x32 <= 0)

m.c21 = Constraint(expr=   0.5*m.x16 - 0.5*m.x20 - 0.5*m.x24 - 0.5*m.x28 + 0.5*m.x32 <= 0)

m.c22 = Constraint(expr= - m.x16 + 0.5*m.x20 - 0.6*m.x24 - 0.5*m.x28 + 0.1*m.x32 <= 0)

m.c23 = Constraint(expr= - 2*m.x16 - 3*m.x20 - 4*m.x28 - 4*m.x32 <= 0)

m.c24 = Constraint(expr=   3*m.x16 - 2*m.x20 + 4*m.x24 - 2*m.x28 + m.x32 <= 0)

m.c25 = Constraint(expr= - 0.5*m.x17 + 2.5*m.x21 + 2.5*m.x25 + 1.5*m.x29 - 0.5*m.x33 <= 0)

m.c26 = Constraint(expr=   0.5*m.x17 - 4.5*m.x21 - 2.5*m.x29 - 2.8*m.x33 <= 0)

m.c27 = Constraint(expr=   0.1*m.x17 - 0.9*m.x21 - 0.9*m.x25 - 0.9*m.x29 + 0.1*m.x33 <= 0)

m.c28 = Constraint(expr= - 0.3*m.x17 + 1.2*m.x21 + 0.1*m.x25 + 0.2*m.x29 + 0.8*m.x33 <= 0)

m.c29 = Constraint(expr= - 2*m.x17 - 3*m.x21 - 4*m.x29 - 4*m.x33 <= 0)

m.c30 = Constraint(expr=   3*m.x17 - 2*m.x21 + 4*m.x25 - 2*m.x29 + m.x33 <= 0)

m.c31 = Constraint(expr= - 2*m.x18 + m.x22 + m.x26 - 2*m.x34 <= 0)

m.c32 = Constraint(expr=   2*m.x18 - 3*m.x22 + 1.5*m.x26 - m.x30 - 1.3*m.x34 <= 0)

m.c33 = Constraint(expr= - m.x22 - m.x26 - m.x30 <= 0)

m.c34 = Constraint(expr= - 1.3*m.x18 + 0.2*m.x22 - 0.9*m.x26 - 0.8*m.x30 - 0.2*m.x34 <= 0)

m.c35 = Constraint(expr= - 3*m.x18 - 4*m.x22 - m.x26 - 5*m.x30 - 5*m.x34 <= 0)

m.c36 = Constraint(expr=   3*m.x18 - 2*m.x22 + 4*m.x26 - 2*m.x30 + m.x34 <= 0)

m.c37 = Constraint(expr=   m.x2 + m.x3 == 1)

m.c38 = Constraint(expr=   m.x4 + m.x5 + m.x6 == 1)

m.c39 = Constraint(expr=-m.x2*m.x7 + m.x15 == 0)

m.c40 = Constraint(expr=-m.x2*m.x8 + m.x16 == 0)

m.c41 = Constraint(expr=-m.x2*m.x9 + m.x17 == 0)

m.c42 = Constraint(expr=-m.x2*m.x10 + m.x18 == 0)

m.c43 = Constraint(expr=-m.x3*m.x7 + m.x19 == 0)

m.c44 = Constraint(expr=-m.x3*m.x8 + m.x20 == 0)

m.c45 = Constraint(expr=-m.x3*m.x9 + m.x21 == 0)

m.c46 = Constraint(expr=-m.x3*m.x10 + m.x22 == 0)

m.c47 = Constraint(expr=-m.x4*m.x11 + m.x23 == 0)

m.c48 = Constraint(expr=-m.x4*m.x12 + m.x24 == 0)

m.c49 = Constraint(expr=-m.x4*m.x13 + m.x25 == 0)

m.c50 = Constraint(expr=-m.x4*m.x14 + m.x26 == 0)

m.c51 = Constraint(expr=-m.x5*m.x11 + m.x27 == 0)

m.c52 = Constraint(expr=-m.x5*m.x12 + m.x28 == 0)

m.c53 = Constraint(expr=-m.x5*m.x13 + m.x29 == 0)

m.c54 = Constraint(expr=-m.x5*m.x14 + m.x30 == 0)

m.c55 = Constraint(expr=-m.x6*m.x11 + m.x31 == 0)

m.c56 = Constraint(expr=-m.x6*m.x12 + m.x32 == 0)

m.c57 = Constraint(expr=-m.x6*m.x13 + m.x33 == 0)

m.c58 = Constraint(expr=-m.x6*m.x14 + m.x34 == 0)
