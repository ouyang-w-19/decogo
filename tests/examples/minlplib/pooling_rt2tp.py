#  NLP written by GAMS Convert at 04/21/18 13:53:11
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         53       21        3       29        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         35       35        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        300      264       36        0
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
m.x8 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,60.98),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,161.29),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,161.29),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,5),initialize=0)

m.obj = Objective(expr= - 140.8*m.x8 - 180.8*m.x9 - 100.8*m.x10 - 140.8*m.x11 - 180.8*m.x12 - 100.8*m.x13 - 128*m.x14
                        - 168*m.x15 - 88*m.x16 - 128*m.x17 - 168*m.x18 - 88*m.x19 + 110*m.x20 + 70*m.x21 + 150*m.x22
                        + 110*m.x23 + 70*m.x24 + 150*m.x25 - 180.8*m.x28 - 128*m.x31 - 88*m.x32 + 110*m.x35
                       , sense=minimize)

m.c2 = Constraint(expr=   m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13 + m.x28 <= 60.98)

m.c3 = Constraint(expr=   m.x14 + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x31 + m.x32 <= 161.29)

m.c4 = Constraint(expr=   m.x20 + m.x21 + m.x22 + m.x23 + m.x24 + m.x25 + m.x35 <= 5)

m.c5 = Constraint(expr=   m.x8 + m.x9 + m.x10 + m.x14 + m.x15 + m.x16 + m.x20 + m.x21 + m.x22 <= 12.5)

m.c6 = Constraint(expr=   m.x11 + m.x12 + m.x13 + m.x17 + m.x18 + m.x19 + m.x23 + m.x24 + m.x25 <= 17.5)

m.c7 = Constraint(expr=   m.x8 + m.x11 + m.x14 + m.x17 + m.x20 + m.x23 + m.x31 + m.x35 >= 5)

m.c8 = Constraint(expr=   m.x9 + m.x12 + m.x15 + m.x18 + m.x21 + m.x24 + m.x28 >= 5)

m.c9 = Constraint(expr=   m.x10 + m.x13 + m.x16 + m.x19 + m.x22 + m.x25 + m.x32 >= 5)

m.c10 = Constraint(expr=   m.x8 + m.x11 + m.x14 + m.x17 + m.x20 + m.x23 + m.x31 + m.x35 <= 300)

m.c11 = Constraint(expr=   m.x9 + m.x12 + m.x15 + m.x18 + m.x21 + m.x24 + m.x28 <= 300)

m.c12 = Constraint(expr=   m.x10 + m.x13 + m.x16 + m.x19 + m.x22 + m.x25 + m.x32 <= 300)

m.c13 = Constraint(expr=   0.0299999999999999*m.x8 + 0.0299999999999999*m.x11 - 0.17*m.x14 - 0.17*m.x17 - 0.04*m.x20
                         - 0.04*m.x23 - 0.17*m.x31 - 0.04*m.x35 <= 0)

m.c14 = Constraint(expr= - 3*m.x14 - 3*m.x17 - 3*m.x20 - 3*m.x23 - 3*m.x31 - 3*m.x35 <= 0)

m.c15 = Constraint(expr= - 14.8*m.x8 - 14.8*m.x11 - 26.1*m.x14 - 26.1*m.x17 - 26.1*m.x31 <= 0)

m.c16 = Constraint(expr= - 8.2*m.x8 - 8.2*m.x11 - 15.2*m.x14 - 15.2*m.x17 - 15.2*m.x31 <= 0)

m.c17 = Constraint(expr= - 0.08*m.x8 - 0.08*m.x11 + 0.12*m.x14 + 0.12*m.x17 - 0.01*m.x20 - 0.01*m.x23 + 0.12*m.x31
                         - 0.01*m.x35 <= 0)

m.c18 = Constraint(expr= - 4.2*m.x8 - 4.2*m.x11 + 7.09999999999999*m.x14 + 7.09999999999999*m.x17 - 19*m.x20 - 19*m.x23
                         + 7.09999999999999*m.x31 - 19*m.x35 <= 0)

m.c19 = Constraint(expr= - 5.5*m.x8 - 5.5*m.x11 + 1.5*m.x14 + 1.5*m.x17 - 13.7*m.x20 - 13.7*m.x23 + 1.5*m.x31
                         - 13.7*m.x35 <= 0)

m.c20 = Constraint(expr=   0.0299999999999999*m.x9 + 0.0299999999999999*m.x12 - 0.17*m.x15 - 0.17*m.x18 - 0.04*m.x21
                         - 0.04*m.x24 + 0.0299999999999999*m.x28 <= 0)

m.c21 = Constraint(expr=   2.1*m.x9 + 2.1*m.x12 - 0.9*m.x15 - 0.9*m.x18 - 0.9*m.x21 - 0.9*m.x24 + 2.1*m.x28 <= 0)

m.c22 = Constraint(expr= - 14.8*m.x9 - 14.8*m.x12 - 26.1*m.x15 - 26.1*m.x18 - 14.8*m.x28 <= 0)

m.c23 = Constraint(expr= - 8.2*m.x9 - 8.2*m.x12 - 15.2*m.x15 - 15.2*m.x18 - 8.2*m.x28 <= 0)

m.c24 = Constraint(expr= - 0.08*m.x9 - 0.08*m.x12 + 0.12*m.x15 + 0.12*m.x18 - 0.01*m.x21 - 0.01*m.x24 - 0.08*m.x28 <= 0)

m.c25 = Constraint(expr= - 3.2*m.x9 - 3.2*m.x12 + 8.09999999999999*m.x15 + 8.09999999999999*m.x18 - 18*m.x21 - 18*m.x24
                         - 3.2*m.x28 <= 0)

m.c26 = Constraint(expr= - 2.5*m.x9 - 2.5*m.x12 + 4.5*m.x15 + 4.5*m.x18 - 10.7*m.x21 - 10.7*m.x24 - 2.5*m.x28 <= 0)

m.c27 = Constraint(expr=   0.0299999999999999*m.x10 + 0.0299999999999999*m.x13 - 0.17*m.x16 - 0.17*m.x19 - 0.04*m.x22
                         - 0.04*m.x25 - 0.17*m.x32 <= 0)

m.c28 = Constraint(expr= - 3*m.x16 - 3*m.x19 - 3*m.x22 - 3*m.x25 - 3*m.x32 <= 0)

m.c29 = Constraint(expr= - 14.8*m.x10 - 14.8*m.x13 - 26.1*m.x16 - 26.1*m.x19 - 26.1*m.x32 <= 0)

m.c30 = Constraint(expr= - 8.2*m.x10 - 8.2*m.x13 - 15.2*m.x16 - 15.2*m.x19 - 15.2*m.x32 <= 0)

m.c31 = Constraint(expr= - 0.08*m.x10 - 0.08*m.x13 + 0.12*m.x16 + 0.12*m.x19 - 0.01*m.x22 - 0.01*m.x25 + 0.12*m.x32
                         <= 0)

m.c32 = Constraint(expr= - 8.2*m.x10 - 8.2*m.x13 + 3.09999999999999*m.x16 + 3.09999999999999*m.x19 - 23*m.x22 - 23*m.x25
                         + 3.09999999999999*m.x32 <= 0)

m.c33 = Constraint(expr= - 7*m.x10 - 7*m.x13 - 15.2*m.x22 - 15.2*m.x25 <= 0)

m.c34 = Constraint(expr=   m.x2 + m.x3 + m.x4 == 1)

m.c35 = Constraint(expr=   m.x5 + m.x6 + m.x7 == 1)

m.c36 = Constraint(expr=-m.x2*m.x26 + m.x8 == 0)

m.c37 = Constraint(expr=-m.x3*m.x26 + m.x9 == 0)

m.c38 = Constraint(expr=-m.x4*m.x26 + m.x10 == 0)

m.c39 = Constraint(expr=-m.x5*m.x27 + m.x11 == 0)

m.c40 = Constraint(expr=-m.x6*m.x27 + m.x12 == 0)

m.c41 = Constraint(expr=-m.x7*m.x27 + m.x13 == 0)

m.c42 = Constraint(expr=-m.x2*m.x29 + m.x14 == 0)

m.c43 = Constraint(expr=-m.x3*m.x29 + m.x15 == 0)

m.c44 = Constraint(expr=-m.x4*m.x29 + m.x16 == 0)

m.c45 = Constraint(expr=-m.x5*m.x30 + m.x17 == 0)

m.c46 = Constraint(expr=-m.x6*m.x30 + m.x18 == 0)

m.c47 = Constraint(expr=-m.x7*m.x30 + m.x19 == 0)

m.c48 = Constraint(expr=-m.x2*m.x33 + m.x20 == 0)

m.c49 = Constraint(expr=-m.x3*m.x33 + m.x21 == 0)

m.c50 = Constraint(expr=-m.x4*m.x33 + m.x22 == 0)

m.c51 = Constraint(expr=-m.x5*m.x34 + m.x23 == 0)

m.c52 = Constraint(expr=-m.x6*m.x34 + m.x24 == 0)

m.c53 = Constraint(expr=-m.x7*m.x34 + m.x25 == 0)
