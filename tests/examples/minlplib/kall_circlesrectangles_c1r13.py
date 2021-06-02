#  NLP written by GAMS Convert at 04/21/18 13:52:27
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         52       40        0       12        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         49       49        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        153      105       48        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0.25,7.5),initialize=0.25)
m.x2 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,2.5),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,3.90512483795333),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,3.90512483795333),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,3.90512483795333),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,3.90512483795333),initialize=0)
m.x8 = Var(within=Reals,bounds=(-3.90512483795333,3.90512483795333),initialize=0)
m.x9 = Var(within=Reals,bounds=(-3.90512483795333,3.90512483795333),initialize=0)
m.x10 = Var(within=Reals,bounds=(-3.90512483795333,3.90512483795333),initialize=0)
m.x11 = Var(within=Reals,bounds=(-3.90512483795333,3.90512483795333),initialize=0)
m.x12 = Var(within=Reals,bounds=(-3.90512483795333,3.90512483795333),initialize=0)
m.x13 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x14 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x15 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x16 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x17 = Var(within=Reals,bounds=(-3.90512483795333,3.90512483795333),initialize=0)
m.x18 = Var(within=Reals,bounds=(-3.90512483795333,3.90512483795333),initialize=0)
m.x19 = Var(within=Reals,bounds=(-3.90512483795333,3.90512483795333),initialize=0)
m.x20 = Var(within=Reals,bounds=(-3.90512483795333,3.90512483795333),initialize=0)
m.x21 = Var(within=Reals,bounds=(-3.90512483795333,3.90512483795333),initialize=0)
m.x22 = Var(within=Reals,bounds=(-3.90512483795333,3.90512483795333),initialize=0)
m.x23 = Var(within=Reals,bounds=(-3.90512483795333,3.90512483795333),initialize=0)
m.x24 = Var(within=Reals,bounds=(-3.90512483795333,3.90512483795333),initialize=0)
m.x25 = Var(within=Reals,bounds=(-3.90512483795333,3.90512483795333),initialize=0)
m.x26 = Var(within=Reals,bounds=(-3.90512483795333,3.90512483795333),initialize=0)
m.x27 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x28 = Var(within=Reals,bounds=(-1.5,1.5),initialize=0)
m.x29 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x30 = Var(within=Reals,bounds=(-1.5,1.5),initialize=0)
m.x31 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x32 = Var(within=Reals,bounds=(-1.5,1.5),initialize=0)
m.x33 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x34 = Var(within=Reals,bounds=(-1.5,1.5),initialize=0)
m.x35 = Var(within=Reals,bounds=(0.5,2.5),initialize=0.5)
m.x36 = Var(within=Reals,bounds=(0.5,2),initialize=0.5)
m.x37 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,2.5),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,2.5),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,2.5),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,2.5),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,2.5),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,3),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,2.5),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,7.5),initialize=0)

m.obj = Objective(expr=m.x49, sense=minimize)

m.c1 = Constraint(expr= - m.x1 + m.x49 == -2.28539816339745)

m.c2 = Constraint(expr=-m.x37*m.x38 + m.x1 == 0)

m.c3 = Constraint(expr=   m.x35 - m.x37 <= -0.5)

m.c4 = Constraint(expr=   m.x36 - m.x38 <= -0.5)

m.c5 = Constraint(expr= - m.x37 + m.x39 <= 0)

m.c6 = Constraint(expr= - m.x38 + m.x40 <= 0)

m.c7 = Constraint(expr= - m.x37 + m.x41 <= 0)

m.c8 = Constraint(expr= - m.x38 + m.x42 <= 0)

m.c9 = Constraint(expr= - m.x37 + m.x43 <= 0)

m.c10 = Constraint(expr= - m.x38 + m.x44 <= 0)

m.c11 = Constraint(expr= - m.x37 + m.x45 <= 0)

m.c12 = Constraint(expr= - m.x38 + m.x46 <= 0)

m.c13 = Constraint(expr=   m.x27 + m.x39 - m.x41 == 0)

m.c14 = Constraint(expr=   m.x28 + m.x40 - m.x42 == 0)

m.c15 = Constraint(expr=   m.x29 + m.x41 - m.x43 == 0)

m.c16 = Constraint(expr=   m.x30 + m.x42 - m.x44 == 0)

m.c17 = Constraint(expr=   m.x31 + m.x43 - m.x45 == 0)

m.c18 = Constraint(expr=   m.x32 + m.x44 - m.x46 == 0)

m.c19 = Constraint(expr=   m.x33 - m.x39 + 2*m.x45 - m.x47 == 0)

m.c20 = Constraint(expr=   m.x34 - m.x40 + 2*m.x46 - m.x48 == 0)

m.c21 = Constraint(expr=m.x27*m.x29 + m.x28*m.x30 == 0)

m.c22 = Constraint(expr=   m.x27 + m.x31 == 0)

m.c23 = Constraint(expr=   m.x28 + m.x32 == 0)

m.c24 = Constraint(expr=   m.x29 + m.x33 == 0)

m.c25 = Constraint(expr=   m.x30 + m.x34 == 0)

m.c26 = Constraint(expr=m.x27*m.x27 + m.x28*m.x28 == 2.25)

m.c27 = Constraint(expr=m.x29*m.x29 + m.x30*m.x30 == 1)

m.c28 = Constraint(expr=m.x13*m.x13 + m.x14*m.x14 == 1)

m.c29 = Constraint(expr= - m.x14 + m.x15 == 0)

m.c30 = Constraint(expr=   m.x13 + m.x16 == 0)

m.c31 = Constraint(expr=m.x13*m.x8 + m.x2 + m.x17 - m.x39 == 0)

m.c32 = Constraint(expr=m.x14*m.x8 + m.x3 + m.x18 - m.x40 == 0)

m.c33 = Constraint(expr=m.x13*m.x9 + m.x2 + m.x19 - m.x41 == 0)

m.c34 = Constraint(expr=m.x14*m.x9 + m.x3 + m.x20 - m.x42 == 0)

m.c35 = Constraint(expr=m.x13*m.x10 + m.x2 + m.x21 - m.x43 == 0)

m.c36 = Constraint(expr=m.x14*m.x10 + m.x3 + m.x22 - m.x44 == 0)

m.c37 = Constraint(expr=m.x13*m.x11 + m.x2 + m.x23 - m.x45 == 0)

m.c38 = Constraint(expr=m.x14*m.x11 + m.x3 + m.x24 - m.x46 == 0)

m.c39 = Constraint(expr=m.x13*m.x12 + m.x2 + m.x25 - m.x35 == 0)

m.c40 = Constraint(expr=m.x14*m.x12 + m.x3 + m.x26 - m.x36 == 0)

m.c41 = Constraint(expr=-m.x4*m.x15 + m.x17 == 0)

m.c42 = Constraint(expr=-m.x4*m.x16 + m.x18 == 0)

m.c43 = Constraint(expr=-m.x5*m.x15 + m.x19 == 0)

m.c44 = Constraint(expr=-m.x5*m.x16 + m.x20 == 0)

m.c45 = Constraint(expr=-m.x6*m.x15 + m.x21 == 0)

m.c46 = Constraint(expr=-m.x6*m.x16 + m.x22 == 0)

m.c47 = Constraint(expr=-m.x7*m.x15 + m.x23 == 0)

m.c48 = Constraint(expr=-m.x7*m.x16 + m.x24 == 0)

m.c49 = Constraint(expr=   0.5*m.x15 + m.x25 == 0)

m.c50 = Constraint(expr=   0.5*m.x16 + m.x26 == 0)

m.c51 = Constraint(expr=   m.x35 <= 1.5)

m.c52 = Constraint(expr=   m.x36 <= 1.25)
