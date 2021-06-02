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
m.x8 = Var(within=Reals,bounds=(0,60.98),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,161.29),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,161.29),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,5),initialize=0)

m.obj = Objective(expr= - 180.8*m.x8 - 128*m.x9 - 88*m.x10 + 110*m.x11 - 140.8*m.x18 - 180.8*m.x19 - 100.8*m.x20
                        - 140.8*m.x21 - 180.8*m.x22 - 100.8*m.x23 - 128*m.x24 - 168*m.x25 - 88*m.x26 - 128*m.x27
                        - 168*m.x28 - 88*m.x29 + 110*m.x30 + 70*m.x31 + 150*m.x32 + 110*m.x33 + 70*m.x34 + 150*m.x35
                       , sense=minimize)

m.c2 = Constraint(expr=   m.x8 + m.x18 + m.x19 + m.x20 + m.x21 + m.x22 + m.x23 <= 60.98)

m.c3 = Constraint(expr=   m.x9 + m.x10 + m.x24 + m.x25 + m.x26 + m.x27 + m.x28 + m.x29 <= 161.29)

m.c4 = Constraint(expr=   m.x11 + m.x30 + m.x31 + m.x32 + m.x33 + m.x34 + m.x35 <= 5)

m.c5 = Constraint(expr=   m.x18 + m.x19 + m.x20 + m.x24 + m.x25 + m.x26 + m.x30 + m.x31 + m.x32 <= 12.5)

m.c6 = Constraint(expr=   m.x21 + m.x22 + m.x23 + m.x27 + m.x28 + m.x29 + m.x33 + m.x34 + m.x35 <= 17.5)

m.c7 = Constraint(expr=   m.x9 + m.x11 + m.x18 + m.x21 + m.x24 + m.x27 + m.x30 + m.x33 >= 5)

m.c8 = Constraint(expr=   m.x8 + m.x19 + m.x22 + m.x25 + m.x28 + m.x31 + m.x34 >= 5)

m.c9 = Constraint(expr=   m.x10 + m.x20 + m.x23 + m.x26 + m.x29 + m.x32 + m.x35 >= 5)

m.c10 = Constraint(expr=   m.x9 + m.x11 + m.x18 + m.x21 + m.x24 + m.x27 + m.x30 + m.x33 <= 300)

m.c11 = Constraint(expr=   m.x8 + m.x19 + m.x22 + m.x25 + m.x28 + m.x31 + m.x34 <= 300)

m.c12 = Constraint(expr=   m.x10 + m.x20 + m.x23 + m.x26 + m.x29 + m.x32 + m.x35 <= 300)

m.c13 = Constraint(expr= - 0.17*m.x9 - 0.04*m.x11 + 0.0299999999999999*m.x18 + 0.0299999999999999*m.x21 - 0.17*m.x24
                         - 0.17*m.x27 - 0.04*m.x30 - 0.04*m.x33 <= 0)

m.c14 = Constraint(expr= - 3*m.x9 - 3*m.x11 - 3*m.x24 - 3*m.x27 - 3*m.x30 - 3*m.x33 <= 0)

m.c15 = Constraint(expr= - 26.1*m.x9 - 14.8*m.x18 - 14.8*m.x21 - 26.1*m.x24 - 26.1*m.x27 <= 0)

m.c16 = Constraint(expr= - 15.2*m.x9 - 8.2*m.x18 - 8.2*m.x21 - 15.2*m.x24 - 15.2*m.x27 <= 0)

m.c17 = Constraint(expr=   0.12*m.x9 - 0.01*m.x11 - 0.08*m.x18 - 0.08*m.x21 + 0.12*m.x24 + 0.12*m.x27 - 0.01*m.x30
                         - 0.01*m.x33 <= 0)

m.c18 = Constraint(expr=   7.09999999999999*m.x9 - 19*m.x11 - 4.2*m.x18 - 4.2*m.x21 + 7.09999999999999*m.x24
                         + 7.09999999999999*m.x27 - 19*m.x30 - 19*m.x33 <= 0)

m.c19 = Constraint(expr=   1.5*m.x9 - 13.7*m.x11 - 5.5*m.x18 - 5.5*m.x21 + 1.5*m.x24 + 1.5*m.x27 - 13.7*m.x30
                         - 13.7*m.x33 <= 0)

m.c20 = Constraint(expr=   0.0299999999999999*m.x8 + 0.0299999999999999*m.x19 + 0.0299999999999999*m.x22 - 0.17*m.x25
                         - 0.17*m.x28 - 0.04*m.x31 - 0.04*m.x34 <= 0)

m.c21 = Constraint(expr=   2.1*m.x8 + 2.1*m.x19 + 2.1*m.x22 - 0.9*m.x25 - 0.9*m.x28 - 0.9*m.x31 - 0.9*m.x34 <= 0)

m.c22 = Constraint(expr= - 14.8*m.x8 - 14.8*m.x19 - 14.8*m.x22 - 26.1*m.x25 - 26.1*m.x28 <= 0)

m.c23 = Constraint(expr= - 8.2*m.x8 - 8.2*m.x19 - 8.2*m.x22 - 15.2*m.x25 - 15.2*m.x28 <= 0)

m.c24 = Constraint(expr= - 0.08*m.x8 - 0.08*m.x19 - 0.08*m.x22 + 0.12*m.x25 + 0.12*m.x28 - 0.01*m.x31 - 0.01*m.x34 <= 0)

m.c25 = Constraint(expr= - 3.2*m.x8 - 3.2*m.x19 - 3.2*m.x22 + 8.09999999999999*m.x25 + 8.09999999999999*m.x28 - 18*m.x31
                         - 18*m.x34 <= 0)

m.c26 = Constraint(expr= - 2.5*m.x8 - 2.5*m.x19 - 2.5*m.x22 + 4.5*m.x25 + 4.5*m.x28 - 10.7*m.x31 - 10.7*m.x34 <= 0)

m.c27 = Constraint(expr= - 0.17*m.x10 + 0.0299999999999999*m.x20 + 0.0299999999999999*m.x23 - 0.17*m.x26 - 0.17*m.x29
                         - 0.04*m.x32 - 0.04*m.x35 <= 0)

m.c28 = Constraint(expr= - 3*m.x10 - 3*m.x26 - 3*m.x29 - 3*m.x32 - 3*m.x35 <= 0)

m.c29 = Constraint(expr= - 26.1*m.x10 - 14.8*m.x20 - 14.8*m.x23 - 26.1*m.x26 - 26.1*m.x29 <= 0)

m.c30 = Constraint(expr= - 15.2*m.x10 - 8.2*m.x20 - 8.2*m.x23 - 15.2*m.x26 - 15.2*m.x29 <= 0)

m.c31 = Constraint(expr=   0.12*m.x10 - 0.08*m.x20 - 0.08*m.x23 + 0.12*m.x26 + 0.12*m.x29 - 0.01*m.x32 - 0.01*m.x35
                         <= 0)

m.c32 = Constraint(expr=   3.09999999999999*m.x10 - 8.2*m.x20 - 8.2*m.x23 + 3.09999999999999*m.x26
                         + 3.09999999999999*m.x29 - 23*m.x32 - 23*m.x35 <= 0)

m.c33 = Constraint(expr= - 7*m.x20 - 7*m.x23 - 15.2*m.x32 - 15.2*m.x35 <= 0)

m.c34 = Constraint(expr=   m.x2 + m.x4 + m.x6 == 1)

m.c35 = Constraint(expr=   m.x3 + m.x5 + m.x7 == 1)

m.c36 = Constraint(expr=-m.x2*m.x12 + m.x18 == 0)

m.c37 = Constraint(expr=-m.x2*m.x13 + m.x19 == 0)

m.c38 = Constraint(expr=-m.x2*m.x14 + m.x20 == 0)

m.c39 = Constraint(expr=-m.x3*m.x15 + m.x21 == 0)

m.c40 = Constraint(expr=-m.x3*m.x16 + m.x22 == 0)

m.c41 = Constraint(expr=-m.x3*m.x17 + m.x23 == 0)

m.c42 = Constraint(expr=-m.x4*m.x12 + m.x24 == 0)

m.c43 = Constraint(expr=-m.x4*m.x13 + m.x25 == 0)

m.c44 = Constraint(expr=-m.x4*m.x14 + m.x26 == 0)

m.c45 = Constraint(expr=-m.x5*m.x15 + m.x27 == 0)

m.c46 = Constraint(expr=-m.x5*m.x16 + m.x28 == 0)

m.c47 = Constraint(expr=-m.x5*m.x17 + m.x29 == 0)

m.c48 = Constraint(expr=-m.x6*m.x12 + m.x30 == 0)

m.c49 = Constraint(expr=-m.x6*m.x13 + m.x31 == 0)

m.c50 = Constraint(expr=-m.x6*m.x14 + m.x32 == 0)

m.c51 = Constraint(expr=-m.x7*m.x15 + m.x33 == 0)

m.c52 = Constraint(expr=-m.x7*m.x16 + m.x34 == 0)

m.c53 = Constraint(expr=-m.x7*m.x17 + m.x35 == 0)
