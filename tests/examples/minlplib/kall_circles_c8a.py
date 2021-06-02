#  NLP written by GAMS Convert at 04/21/18 13:52:26
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         86        2       36       48        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         22       22        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        243       97      146        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0.49,16.8),initialize=0.49)
m.x2 = Var(within=Reals,bounds=(0.5,7.5),initialize=0.5)
m.x3 = Var(within=Reals,bounds=(0.5,1.6),initialize=0.5)
m.x4 = Var(within=Reals,bounds=(0.5,7.5),initialize=0.5)
m.x5 = Var(within=Reals,bounds=(0.5,1.6),initialize=0.5)
m.x6 = Var(within=Reals,bounds=(0.5,7.5),initialize=0.5)
m.x7 = Var(within=Reals,bounds=(0.5,1.6),initialize=0.5)
m.x8 = Var(within=Reals,bounds=(0.5,7.5),initialize=0.5)
m.x9 = Var(within=Reals,bounds=(0.5,1.6),initialize=0.5)
m.x10 = Var(within=Reals,bounds=(0.5,7.5),initialize=0.5)
m.x11 = Var(within=Reals,bounds=(0.5,1.6),initialize=0.5)
m.x12 = Var(within=Reals,bounds=(0.5,7.5),initialize=0.5)
m.x13 = Var(within=Reals,bounds=(0.5,1.6),initialize=0.5)
m.x14 = Var(within=Reals,bounds=(0.5,7.5),initialize=0.5)
m.x15 = Var(within=Reals,bounds=(0.5,1.6),initialize=0.5)
m.x16 = Var(within=Reals,bounds=(0.5,7.5),initialize=0.5)
m.x17 = Var(within=Reals,bounds=(0.5,1.6),initialize=0.5)
m.x18 = Var(within=Reals,bounds=(0.7,7.3),initialize=0.7)
m.x19 = Var(within=Reals,bounds=(0.7,1.4),initialize=0.7)
m.x20 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,2.1),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,16.8),initialize=0)

m.obj = Objective(expr=m.x22, sense=minimize)

m.c1 = Constraint(expr= - m.x1 + m.x22 == -7.82256570743859)

m.c2 = Constraint(expr=-m.x20*m.x21 + m.x1 == 0)

m.c3 = Constraint(expr=(m.x2 - m.x4)*(m.x2 - m.x4) + (m.x3 - m.x5)*(m.x3 - m.x5) >= 1)

m.c4 = Constraint(expr=(m.x2 - m.x6)*(m.x2 - m.x6) + (m.x3 - m.x7)*(m.x3 - m.x7) >= 1)

m.c5 = Constraint(expr=(m.x2 - m.x8)*(m.x2 - m.x8) + (m.x3 - m.x9)*(m.x3 - m.x9) >= 1)

m.c6 = Constraint(expr=(m.x2 - m.x10)*(m.x2 - m.x10) + (m.x3 - m.x11)*(m.x3 - m.x11) >= 1)

m.c7 = Constraint(expr=(m.x2 - m.x12)*(m.x2 - m.x12) + (m.x3 - m.x13)*(m.x3 - m.x13) >= 1)

m.c8 = Constraint(expr=(m.x2 - m.x14)*(m.x2 - m.x14) + (m.x3 - m.x15)*(m.x3 - m.x15) >= 1)

m.c9 = Constraint(expr=(m.x2 - m.x16)*(m.x2 - m.x16) + (m.x3 - m.x17)*(m.x3 - m.x17) >= 1)

m.c10 = Constraint(expr=(m.x2 - m.x18)*(m.x2 - m.x18) + (m.x3 - m.x19)*(m.x3 - m.x19) >= 1.44)

m.c11 = Constraint(expr=(m.x4 - m.x6)*(m.x4 - m.x6) + (m.x5 - m.x7)*(m.x5 - m.x7) >= 1)

m.c12 = Constraint(expr=(m.x4 - m.x8)*(m.x4 - m.x8) + (m.x5 - m.x9)*(m.x5 - m.x9) >= 1)

m.c13 = Constraint(expr=(m.x4 - m.x10)*(m.x4 - m.x10) + (m.x5 - m.x11)*(m.x5 - m.x11) >= 1)

m.c14 = Constraint(expr=(m.x4 - m.x12)*(m.x4 - m.x12) + (m.x5 - m.x13)*(m.x5 - m.x13) >= 1)

m.c15 = Constraint(expr=(m.x4 - m.x14)*(m.x4 - m.x14) + (m.x5 - m.x15)*(m.x5 - m.x15) >= 1)

m.c16 = Constraint(expr=(m.x4 - m.x16)*(m.x4 - m.x16) + (m.x5 - m.x17)*(m.x5 - m.x17) >= 1)

m.c17 = Constraint(expr=(m.x4 - m.x18)*(m.x4 - m.x18) + (m.x5 - m.x19)*(m.x5 - m.x19) >= 1.44)

m.c18 = Constraint(expr=(m.x6 - m.x8)*(m.x6 - m.x8) + (m.x7 - m.x9)*(m.x7 - m.x9) >= 1)

m.c19 = Constraint(expr=(m.x6 - m.x10)*(m.x6 - m.x10) + (m.x7 - m.x11)*(m.x7 - m.x11) >= 1)

m.c20 = Constraint(expr=(m.x6 - m.x12)*(m.x6 - m.x12) + (m.x7 - m.x13)*(m.x7 - m.x13) >= 1)

m.c21 = Constraint(expr=(m.x6 - m.x14)*(m.x6 - m.x14) + (m.x7 - m.x15)*(m.x7 - m.x15) >= 1)

m.c22 = Constraint(expr=(m.x6 - m.x16)*(m.x6 - m.x16) + (m.x7 - m.x17)*(m.x7 - m.x17) >= 1)

m.c23 = Constraint(expr=(m.x6 - m.x18)*(m.x6 - m.x18) + (m.x7 - m.x19)*(m.x7 - m.x19) >= 1.44)

m.c24 = Constraint(expr=(m.x8 - m.x10)*(m.x8 - m.x10) + (m.x9 - m.x11)*(m.x9 - m.x11) >= 1)

m.c25 = Constraint(expr=(m.x8 - m.x12)*(m.x8 - m.x12) + (m.x9 - m.x13)*(m.x9 - m.x13) >= 1)

m.c26 = Constraint(expr=(m.x8 - m.x14)*(m.x8 - m.x14) + (m.x9 - m.x15)*(m.x9 - m.x15) >= 1)

m.c27 = Constraint(expr=(m.x8 - m.x16)*(m.x8 - m.x16) + (m.x9 - m.x17)*(m.x9 - m.x17) >= 1)

m.c28 = Constraint(expr=(m.x8 - m.x18)*(m.x8 - m.x18) + (m.x9 - m.x19)*(m.x9 - m.x19) >= 1.44)

m.c29 = Constraint(expr=(m.x10 - m.x12)*(m.x10 - m.x12) + (m.x11 - m.x13)*(m.x11 - m.x13) >= 1)

m.c30 = Constraint(expr=(m.x10 - m.x14)*(m.x10 - m.x14) + (m.x11 - m.x15)*(m.x11 - m.x15) >= 1)

m.c31 = Constraint(expr=(m.x10 - m.x16)*(m.x10 - m.x16) + (m.x11 - m.x17)*(m.x11 - m.x17) >= 1)

m.c32 = Constraint(expr=(m.x10 - m.x18)*(m.x10 - m.x18) + (m.x11 - m.x19)*(m.x11 - m.x19) >= 1.44)

m.c33 = Constraint(expr=(m.x12 - m.x14)*(m.x12 - m.x14) + (m.x13 - m.x15)*(m.x13 - m.x15) >= 1)

m.c34 = Constraint(expr=(m.x12 - m.x16)*(m.x12 - m.x16) + (m.x13 - m.x17)*(m.x13 - m.x17) >= 1)

m.c35 = Constraint(expr=(m.x12 - m.x18)*(m.x12 - m.x18) + (m.x13 - m.x19)*(m.x13 - m.x19) >= 1.44)

m.c36 = Constraint(expr=(m.x14 - m.x16)*(m.x14 - m.x16) + (m.x15 - m.x17)*(m.x15 - m.x17) >= 1)

m.c37 = Constraint(expr=(m.x14 - m.x18)*(m.x14 - m.x18) + (m.x15 - m.x19)*(m.x15 - m.x19) >= 1.44)

m.c38 = Constraint(expr=(m.x16 - m.x18)*(m.x16 - m.x18) + (m.x17 - m.x19)*(m.x17 - m.x19) >= 1.44)

m.c39 = Constraint(expr=   m.x2 - m.x20 <= -0.5)

m.c40 = Constraint(expr=   m.x3 - m.x21 <= -0.5)

m.c41 = Constraint(expr=   m.x4 - m.x20 <= -0.5)

m.c42 = Constraint(expr=   m.x5 - m.x21 <= -0.5)

m.c43 = Constraint(expr=   m.x6 - m.x20 <= -0.5)

m.c44 = Constraint(expr=   m.x7 - m.x21 <= -0.5)

m.c45 = Constraint(expr=   m.x8 - m.x20 <= -0.5)

m.c46 = Constraint(expr=   m.x9 - m.x21 <= -0.5)

m.c47 = Constraint(expr=   m.x10 - m.x20 <= -0.5)

m.c48 = Constraint(expr=   m.x11 - m.x21 <= -0.5)

m.c49 = Constraint(expr=   m.x12 - m.x20 <= -0.5)

m.c50 = Constraint(expr=   m.x13 - m.x21 <= -0.5)

m.c51 = Constraint(expr=   m.x14 - m.x20 <= -0.5)

m.c52 = Constraint(expr=   m.x15 - m.x21 <= -0.5)

m.c53 = Constraint(expr=   m.x16 - m.x20 <= -0.5)

m.c54 = Constraint(expr=   m.x17 - m.x21 <= -0.5)

m.c55 = Constraint(expr=   m.x18 - m.x20 <= -0.7)

m.c56 = Constraint(expr=   m.x19 - m.x21 <= -0.7)

m.c57 = Constraint(expr=   m.x2 <= 4)

m.c58 = Constraint(expr=   m.x3 <= 1.05)

m.c59 = Constraint(expr=   m.x2 - m.x4 <= 0)

m.c60 = Constraint(expr=   m.x2 - m.x6 <= 0)

m.c61 = Constraint(expr=   m.x2 - m.x8 <= 0)

m.c62 = Constraint(expr=   m.x2 - m.x10 <= 0)

m.c63 = Constraint(expr=   m.x2 - m.x12 <= 0)

m.c64 = Constraint(expr=   m.x2 - m.x14 <= 0)

m.c65 = Constraint(expr=   m.x2 - m.x16 <= 0)

m.c66 = Constraint(expr=   m.x4 - m.x6 <= 0)

m.c67 = Constraint(expr=   m.x4 - m.x8 <= 0)

m.c68 = Constraint(expr=   m.x4 - m.x10 <= 0)

m.c69 = Constraint(expr=   m.x4 - m.x12 <= 0)

m.c70 = Constraint(expr=   m.x4 - m.x14 <= 0)

m.c71 = Constraint(expr=   m.x4 - m.x16 <= 0)

m.c72 = Constraint(expr=   m.x6 - m.x8 <= 0)

m.c73 = Constraint(expr=   m.x6 - m.x10 <= 0)

m.c74 = Constraint(expr=   m.x6 - m.x12 <= 0)

m.c75 = Constraint(expr=   m.x6 - m.x14 <= 0)

m.c76 = Constraint(expr=   m.x6 - m.x16 <= 0)

m.c77 = Constraint(expr=   m.x8 - m.x10 <= 0)

m.c78 = Constraint(expr=   m.x8 - m.x12 <= 0)

m.c79 = Constraint(expr=   m.x8 - m.x14 <= 0)

m.c80 = Constraint(expr=   m.x8 - m.x16 <= 0)

m.c81 = Constraint(expr=   m.x10 - m.x12 <= 0)

m.c82 = Constraint(expr=   m.x10 - m.x14 <= 0)

m.c83 = Constraint(expr=   m.x10 - m.x16 <= 0)

m.c84 = Constraint(expr=   m.x12 - m.x14 <= 0)

m.c85 = Constraint(expr=   m.x12 - m.x16 <= 0)

m.c86 = Constraint(expr=   m.x14 - m.x16 <= 0)
