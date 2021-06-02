#  NLP written by GAMS Convert at 04/21/18 13:52:27
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         40        2       21       17        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         18       18        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        121       35       86        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(2.89,32),initialize=2.89)
m.x2 = Var(within=Reals,bounds=(1.2,6.8),initialize=1.2)
m.x3 = Var(within=Reals,bounds=(1.2,2.8),initialize=1.2)
m.x4 = Var(within=Reals,bounds=(0.6,7.4),initialize=0.6)
m.x5 = Var(within=Reals,bounds=(0.6,3.4),initialize=0.6)
m.x6 = Var(within=Reals,bounds=(0.8,7.2),initialize=0.8)
m.x7 = Var(within=Reals,bounds=(0.8,3.2),initialize=0.8)
m.x8 = Var(within=Reals,bounds=(1.7,6.3),initialize=1.7)
m.x9 = Var(within=Reals,bounds=(1.7,2.3),initialize=1.7)
m.x10 = Var(within=Reals,bounds=(0.5,7.5),initialize=0.5)
m.x11 = Var(within=Reals,bounds=(0.5,3.5),initialize=0.5)
m.x12 = Var(within=Reals,bounds=(1.3,6.7),initialize=1.3)
m.x13 = Var(within=Reals,bounds=(1.3,2.7),initialize=1.3)
m.x14 = Var(within=Reals,bounds=(0.6,7.4),initialize=0.6)
m.x15 = Var(within=Reals,bounds=(0.6,3.4),initialize=0.6)
m.x16 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,32),initialize=0)

m.obj = Objective(expr=m.x18, sense=minimize)

m.c1 = Constraint(expr= - m.x1 + m.x18 == -23.9703519468901)

m.c2 = Constraint(expr=-m.x16*m.x17 + m.x1 == 0)

m.c3 = Constraint(expr=(m.x2 - m.x4)*(m.x2 - m.x4) + (m.x3 - m.x5)*(m.x3 - m.x5) >= 3.24)

m.c4 = Constraint(expr=(m.x2 - m.x6)*(m.x2 - m.x6) + (m.x3 - m.x7)*(m.x3 - m.x7) >= 4)

m.c5 = Constraint(expr=(m.x2 - m.x8)*(m.x2 - m.x8) + (m.x3 - m.x9)*(m.x3 - m.x9) >= 8.41)

m.c6 = Constraint(expr=(m.x2 - m.x10)*(m.x2 - m.x10) + (m.x3 - m.x11)*(m.x3 - m.x11) >= 2.89)

m.c7 = Constraint(expr=(m.x2 - m.x12)*(m.x2 - m.x12) + (m.x3 - m.x13)*(m.x3 - m.x13) >= 6.25)

m.c8 = Constraint(expr=(m.x2 - m.x14)*(m.x2 - m.x14) + (m.x3 - m.x15)*(m.x3 - m.x15) >= 3.24)

m.c9 = Constraint(expr=(m.x4 - m.x6)*(m.x4 - m.x6) + (m.x5 - m.x7)*(m.x5 - m.x7) >= 1.96)

m.c10 = Constraint(expr=(m.x4 - m.x8)*(m.x4 - m.x8) + (m.x5 - m.x9)*(m.x5 - m.x9) >= 5.29)

m.c11 = Constraint(expr=(m.x4 - m.x10)*(m.x4 - m.x10) + (m.x5 - m.x11)*(m.x5 - m.x11) >= 1.21)

m.c12 = Constraint(expr=(m.x4 - m.x12)*(m.x4 - m.x12) + (m.x5 - m.x13)*(m.x5 - m.x13) >= 3.61)

m.c13 = Constraint(expr=(m.x4 - m.x14)*(m.x4 - m.x14) + (m.x5 - m.x15)*(m.x5 - m.x15) >= 1.44)

m.c14 = Constraint(expr=(m.x6 - m.x8)*(m.x6 - m.x8) + (m.x7 - m.x9)*(m.x7 - m.x9) >= 6.25)

m.c15 = Constraint(expr=(m.x6 - m.x10)*(m.x6 - m.x10) + (m.x7 - m.x11)*(m.x7 - m.x11) >= 1.69)

m.c16 = Constraint(expr=(m.x6 - m.x12)*(m.x6 - m.x12) + (m.x7 - m.x13)*(m.x7 - m.x13) >= 4.41)

m.c17 = Constraint(expr=(m.x6 - m.x14)*(m.x6 - m.x14) + (m.x7 - m.x15)*(m.x7 - m.x15) >= 1.96)

m.c18 = Constraint(expr=(m.x8 - m.x10)*(m.x8 - m.x10) + (m.x9 - m.x11)*(m.x9 - m.x11) >= 4.84)

m.c19 = Constraint(expr=(m.x8 - m.x12)*(m.x8 - m.x12) + (m.x9 - m.x13)*(m.x9 - m.x13) >= 9)

m.c20 = Constraint(expr=(m.x8 - m.x14)*(m.x8 - m.x14) + (m.x9 - m.x15)*(m.x9 - m.x15) >= 5.29)

m.c21 = Constraint(expr=(m.x10 - m.x12)*(m.x10 - m.x12) + (m.x11 - m.x13)*(m.x11 - m.x13) >= 3.24)

m.c22 = Constraint(expr=(m.x10 - m.x14)*(m.x10 - m.x14) + (m.x11 - m.x15)*(m.x11 - m.x15) >= 1.21)

m.c23 = Constraint(expr=(m.x12 - m.x14)*(m.x12 - m.x14) + (m.x13 - m.x15)*(m.x13 - m.x15) >= 3.61)

m.c24 = Constraint(expr=   m.x2 - m.x16 <= -1.2)

m.c25 = Constraint(expr=   m.x3 - m.x17 <= -1.2)

m.c26 = Constraint(expr=   m.x4 - m.x16 <= -0.6)

m.c27 = Constraint(expr=   m.x5 - m.x17 <= -0.6)

m.c28 = Constraint(expr=   m.x6 - m.x16 <= -0.8)

m.c29 = Constraint(expr=   m.x7 - m.x17 <= -0.8)

m.c30 = Constraint(expr=   m.x8 - m.x16 <= -1.7)

m.c31 = Constraint(expr=   m.x9 - m.x17 <= -1.7)

m.c32 = Constraint(expr=   m.x10 - m.x16 <= -0.5)

m.c33 = Constraint(expr=   m.x11 - m.x17 <= -0.5)

m.c34 = Constraint(expr=   m.x12 - m.x16 <= -1.3)

m.c35 = Constraint(expr=   m.x13 - m.x17 <= -1.3)

m.c36 = Constraint(expr=   m.x14 - m.x16 <= -0.6)

m.c37 = Constraint(expr=   m.x15 - m.x17 <= -0.6)

m.c38 = Constraint(expr=   m.x2 <= 4)

m.c39 = Constraint(expr=   m.x3 <= 2)

m.c40 = Constraint(expr=   m.x4 - m.x14 <= 0)
