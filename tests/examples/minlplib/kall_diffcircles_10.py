#  NLP written by GAMS Convert at 04/21/18 13:52:27
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         71        2       45       24        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         24       24        0        0        0        0        0        0
#  FX      1        1        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        231       49      182        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(4,60),initialize=4)
m.x2 = Var(within=Reals,bounds=(1.2,13.8),initialize=1.2)
m.x3 = Var(within=Reals,bounds=(1.2,2.8),initialize=1.2)
m.x4 = Var(within=Reals,bounds=(0.6,14.4),initialize=0.6)
m.x5 = Var(within=Reals,bounds=(0.6,3.4),initialize=0.6)
m.x6 = Var(within=Reals,bounds=(0.8,14.2),initialize=0.8)
m.x7 = Var(within=Reals,bounds=(0.8,3.2),initialize=0.8)
m.x8 = Var(within=Reals,bounds=(1.7,13.3),initialize=1.7)
m.x9 = Var(within=Reals,bounds=(1.7,2.3),initialize=1.7)
m.x10 = Var(within=Reals,bounds=(0.5,14.5),initialize=0.5)
m.x11 = Var(within=Reals,bounds=(0.5,3.5),initialize=0.5)
m.x12 = Var(within=Reals,bounds=(1.3,13.7),initialize=1.3)
m.x13 = Var(within=Reals,bounds=(1.3,2.7),initialize=1.3)
m.x14 = Var(within=Reals,bounds=(2,13),initialize=2)
m.x15 = Var(within=Reals,bounds=(2,2),initialize=2)
m.x16 = Var(within=Reals,bounds=(1.3,13.7),initialize=1.3)
m.x17 = Var(within=Reals,bounds=(1.3,2.7),initialize=1.3)
m.x18 = Var(within=Reals,bounds=(0.6,14.4),initialize=0.6)
m.x19 = Var(within=Reals,bounds=(0.6,3.4),initialize=0.6)
m.x20 = Var(within=Reals,bounds=(0.7,14.3),initialize=0.7)
m.x21 = Var(within=Reals,bounds=(0.7,3.3),initialize=0.7)
m.x22 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,60),initialize=0)

m.obj = Objective(expr=m.x24, sense=minimize)

m.c1 = Constraint(expr= - m.x1 + m.x24 == -43.385394546075)

m.c2 = Constraint(expr=-m.x22*m.x23 + m.x1 == 0)

m.c3 = Constraint(expr=(m.x2 - m.x4)*(m.x2 - m.x4) + (m.x3 - m.x5)*(m.x3 - m.x5) >= 3.24)

m.c4 = Constraint(expr=(m.x2 - m.x6)*(m.x2 - m.x6) + (m.x3 - m.x7)*(m.x3 - m.x7) >= 4)

m.c5 = Constraint(expr=(m.x2 - m.x8)*(m.x2 - m.x8) + (m.x3 - m.x9)*(m.x3 - m.x9) >= 8.41)

m.c6 = Constraint(expr=(m.x2 - m.x10)*(m.x2 - m.x10) + (m.x3 - m.x11)*(m.x3 - m.x11) >= 2.89)

m.c7 = Constraint(expr=(m.x2 - m.x12)*(m.x2 - m.x12) + (m.x3 - m.x13)*(m.x3 - m.x13) >= 6.25)

m.c8 = Constraint(expr=(m.x2 - m.x14)*(m.x2 - m.x14) + (m.x3 - m.x15)*(m.x3 - m.x15) >= 10.24)

m.c9 = Constraint(expr=(m.x2 - m.x16)*(m.x2 - m.x16) + (m.x3 - m.x17)*(m.x3 - m.x17) >= 6.25)

m.c10 = Constraint(expr=(m.x2 - m.x18)*(m.x2 - m.x18) + (m.x3 - m.x19)*(m.x3 - m.x19) >= 3.24)

m.c11 = Constraint(expr=(m.x2 - m.x20)*(m.x2 - m.x20) + (m.x3 - m.x21)*(m.x3 - m.x21) >= 3.61)

m.c12 = Constraint(expr=(m.x4 - m.x6)*(m.x4 - m.x6) + (m.x5 - m.x7)*(m.x5 - m.x7) >= 1.96)

m.c13 = Constraint(expr=(m.x4 - m.x8)*(m.x4 - m.x8) + (m.x5 - m.x9)*(m.x5 - m.x9) >= 5.29)

m.c14 = Constraint(expr=(m.x4 - m.x10)*(m.x4 - m.x10) + (m.x5 - m.x11)*(m.x5 - m.x11) >= 1.21)

m.c15 = Constraint(expr=(m.x4 - m.x12)*(m.x4 - m.x12) + (m.x5 - m.x13)*(m.x5 - m.x13) >= 3.61)

m.c16 = Constraint(expr=(m.x4 - m.x14)*(m.x4 - m.x14) + (m.x5 - m.x15)*(m.x5 - m.x15) >= 6.76)

m.c17 = Constraint(expr=(m.x4 - m.x16)*(m.x4 - m.x16) + (m.x5 - m.x17)*(m.x5 - m.x17) >= 3.61)

m.c18 = Constraint(expr=(m.x4 - m.x18)*(m.x4 - m.x18) + (m.x5 - m.x19)*(m.x5 - m.x19) >= 1.44)

m.c19 = Constraint(expr=(m.x4 - m.x20)*(m.x4 - m.x20) + (m.x5 - m.x21)*(m.x5 - m.x21) >= 1.69)

m.c20 = Constraint(expr=(m.x6 - m.x8)*(m.x6 - m.x8) + (m.x7 - m.x9)*(m.x7 - m.x9) >= 6.25)

m.c21 = Constraint(expr=(m.x6 - m.x10)*(m.x6 - m.x10) + (m.x7 - m.x11)*(m.x7 - m.x11) >= 1.69)

m.c22 = Constraint(expr=(m.x6 - m.x12)*(m.x6 - m.x12) + (m.x7 - m.x13)*(m.x7 - m.x13) >= 4.41)

m.c23 = Constraint(expr=(m.x6 - m.x14)*(m.x6 - m.x14) + (m.x7 - m.x15)*(m.x7 - m.x15) >= 7.84)

m.c24 = Constraint(expr=(m.x6 - m.x16)*(m.x6 - m.x16) + (m.x7 - m.x17)*(m.x7 - m.x17) >= 4.41)

m.c25 = Constraint(expr=(m.x6 - m.x18)*(m.x6 - m.x18) + (m.x7 - m.x19)*(m.x7 - m.x19) >= 1.96)

m.c26 = Constraint(expr=(m.x6 - m.x20)*(m.x6 - m.x20) + (m.x7 - m.x21)*(m.x7 - m.x21) >= 2.25)

m.c27 = Constraint(expr=(m.x8 - m.x10)*(m.x8 - m.x10) + (m.x9 - m.x11)*(m.x9 - m.x11) >= 4.84)

m.c28 = Constraint(expr=(m.x8 - m.x12)*(m.x8 - m.x12) + (m.x9 - m.x13)*(m.x9 - m.x13) >= 9)

m.c29 = Constraint(expr=(m.x8 - m.x14)*(m.x8 - m.x14) + (m.x9 - m.x15)*(m.x9 - m.x15) >= 13.69)

m.c30 = Constraint(expr=(m.x8 - m.x16)*(m.x8 - m.x16) + (m.x9 - m.x17)*(m.x9 - m.x17) >= 9)

m.c31 = Constraint(expr=(m.x8 - m.x18)*(m.x8 - m.x18) + (m.x9 - m.x19)*(m.x9 - m.x19) >= 5.29)

m.c32 = Constraint(expr=(m.x8 - m.x20)*(m.x8 - m.x20) + (m.x9 - m.x21)*(m.x9 - m.x21) >= 5.76)

m.c33 = Constraint(expr=(m.x10 - m.x12)*(m.x10 - m.x12) + (m.x11 - m.x13)*(m.x11 - m.x13) >= 3.24)

m.c34 = Constraint(expr=(m.x10 - m.x14)*(m.x10 - m.x14) + (m.x11 - m.x15)*(m.x11 - m.x15) >= 6.25)

m.c35 = Constraint(expr=(m.x10 - m.x16)*(m.x10 - m.x16) + (m.x11 - m.x17)*(m.x11 - m.x17) >= 3.24)

m.c36 = Constraint(expr=(m.x10 - m.x18)*(m.x10 - m.x18) + (m.x11 - m.x19)*(m.x11 - m.x19) >= 1.21)

m.c37 = Constraint(expr=(m.x10 - m.x20)*(m.x10 - m.x20) + (m.x11 - m.x21)*(m.x11 - m.x21) >= 1.44)

m.c38 = Constraint(expr=(m.x12 - m.x14)*(m.x12 - m.x14) + (m.x13 - m.x15)*(m.x13 - m.x15) >= 10.89)

m.c39 = Constraint(expr=(m.x12 - m.x16)*(m.x12 - m.x16) + (m.x13 - m.x17)*(m.x13 - m.x17) >= 6.76)

m.c40 = Constraint(expr=(m.x12 - m.x18)*(m.x12 - m.x18) + (m.x13 - m.x19)*(m.x13 - m.x19) >= 3.61)

m.c41 = Constraint(expr=(m.x12 - m.x20)*(m.x12 - m.x20) + (m.x13 - m.x21)*(m.x13 - m.x21) >= 4)

m.c42 = Constraint(expr=(m.x14 - m.x16)*(m.x14 - m.x16) + (m.x15 - m.x17)*(m.x15 - m.x17) >= 10.89)

m.c43 = Constraint(expr=(m.x14 - m.x18)*(m.x14 - m.x18) + (m.x15 - m.x19)*(m.x15 - m.x19) >= 6.76)

m.c44 = Constraint(expr=(m.x14 - m.x20)*(m.x14 - m.x20) + (m.x15 - m.x21)*(m.x15 - m.x21) >= 7.29)

m.c45 = Constraint(expr=(m.x16 - m.x18)*(m.x16 - m.x18) + (m.x17 - m.x19)*(m.x17 - m.x19) >= 3.61)

m.c46 = Constraint(expr=(m.x16 - m.x20)*(m.x16 - m.x20) + (m.x17 - m.x21)*(m.x17 - m.x21) >= 4)

m.c47 = Constraint(expr=(m.x18 - m.x20)*(m.x18 - m.x20) + (m.x19 - m.x21)*(m.x19 - m.x21) >= 1.69)

m.c48 = Constraint(expr=   m.x2 - m.x22 <= -1.2)

m.c49 = Constraint(expr=   m.x3 - m.x23 <= -1.2)

m.c50 = Constraint(expr=   m.x4 - m.x22 <= -0.6)

m.c51 = Constraint(expr=   m.x5 - m.x23 <= -0.6)

m.c52 = Constraint(expr=   m.x6 - m.x22 <= -0.8)

m.c53 = Constraint(expr=   m.x7 - m.x23 <= -0.8)

m.c54 = Constraint(expr=   m.x8 - m.x22 <= -1.7)

m.c55 = Constraint(expr=   m.x9 - m.x23 <= -1.7)

m.c56 = Constraint(expr=   m.x10 - m.x22 <= -0.5)

m.c57 = Constraint(expr=   m.x11 - m.x23 <= -0.5)

m.c58 = Constraint(expr=   m.x12 - m.x22 <= -1.3)

m.c59 = Constraint(expr=   m.x13 - m.x23 <= -1.3)

m.c60 = Constraint(expr=   m.x14 - m.x22 <= -2)

m.c61 = Constraint(expr=   m.x15 - m.x23 <= -2)

m.c62 = Constraint(expr=   m.x16 - m.x22 <= -1.3)

m.c63 = Constraint(expr=   m.x17 - m.x23 <= -1.3)

m.c64 = Constraint(expr=   m.x18 - m.x22 <= -0.6)

m.c65 = Constraint(expr=   m.x19 - m.x23 <= -0.6)

m.c66 = Constraint(expr=   m.x20 - m.x22 <= -0.7)

m.c67 = Constraint(expr=   m.x21 - m.x23 <= -0.7)

m.c68 = Constraint(expr=   m.x2 <= 7.5)

m.c69 = Constraint(expr=   m.x3 <= 2)

m.c70 = Constraint(expr=   m.x4 - m.x18 <= 0)

m.c71 = Constraint(expr=   m.x12 - m.x16 <= 0)
