#  NLP written by GAMS Convert at 04/21/18 13:52:27
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         24        2       10       12        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         14       14        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         67       25       42        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(2.89,90),initialize=2.89)
m.x2 = Var(within=Reals,bounds=(1.2,16.8),initialize=1.2)
m.x3 = Var(within=Reals,bounds=(1.2,3.8),initialize=1.2)
m.x4 = Var(within=Reals,bounds=(0.6,17.4),initialize=0.6)
m.x5 = Var(within=Reals,bounds=(0.6,4.4),initialize=0.6)
m.x6 = Var(within=Reals,bounds=(0.8,17.2),initialize=0.8)
m.x7 = Var(within=Reals,bounds=(0.8,4.2),initialize=0.8)
m.x8 = Var(within=Reals,bounds=(1.7,16.3),initialize=1.7)
m.x9 = Var(within=Reals,bounds=(1.7,3.3),initialize=1.7)
m.x10 = Var(within=Reals,bounds=(0.5,17.5),initialize=0.5)
m.x11 = Var(within=Reals,bounds=(0.5,4.5),initialize=0.5)
m.x12 = Var(within=Reals,bounds=(0,18),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,90),initialize=0)

m.obj = Objective(expr=m.x14, sense=minimize)

m.c1 = Constraint(expr= - m.x1 + m.x14 == -17.530087007031)

m.c2 = Constraint(expr=-m.x12*m.x13 + m.x1 == 0)

m.c3 = Constraint(expr=(m.x2 - m.x4)*(m.x2 - m.x4) + (m.x3 - m.x5)*(m.x3 - m.x5) >= 3.24)

m.c4 = Constraint(expr=(m.x2 - m.x6)*(m.x2 - m.x6) + (m.x3 - m.x7)*(m.x3 - m.x7) >= 4)

m.c5 = Constraint(expr=(m.x2 - m.x8)*(m.x2 - m.x8) + (m.x3 - m.x9)*(m.x3 - m.x9) >= 8.41)

m.c6 = Constraint(expr=(m.x2 - m.x10)*(m.x2 - m.x10) + (m.x3 - m.x11)*(m.x3 - m.x11) >= 2.89)

m.c7 = Constraint(expr=(m.x4 - m.x6)*(m.x4 - m.x6) + (m.x5 - m.x7)*(m.x5 - m.x7) >= 1.96)

m.c8 = Constraint(expr=(m.x4 - m.x8)*(m.x4 - m.x8) + (m.x5 - m.x9)*(m.x5 - m.x9) >= 5.29)

m.c9 = Constraint(expr=(m.x4 - m.x10)*(m.x4 - m.x10) + (m.x5 - m.x11)*(m.x5 - m.x11) >= 1.21)

m.c10 = Constraint(expr=(m.x6 - m.x8)*(m.x6 - m.x8) + (m.x7 - m.x9)*(m.x7 - m.x9) >= 6.25)

m.c11 = Constraint(expr=(m.x6 - m.x10)*(m.x6 - m.x10) + (m.x7 - m.x11)*(m.x7 - m.x11) >= 1.69)

m.c12 = Constraint(expr=(m.x8 - m.x10)*(m.x8 - m.x10) + (m.x9 - m.x11)*(m.x9 - m.x11) >= 4.84)

m.c13 = Constraint(expr=   m.x2 - m.x12 <= -1.2)

m.c14 = Constraint(expr=   m.x3 - m.x13 <= -1.2)

m.c15 = Constraint(expr=   m.x4 - m.x12 <= -0.6)

m.c16 = Constraint(expr=   m.x5 - m.x13 <= -0.6)

m.c17 = Constraint(expr=   m.x6 - m.x12 <= -0.8)

m.c18 = Constraint(expr=   m.x7 - m.x13 <= -0.8)

m.c19 = Constraint(expr=   m.x8 - m.x12 <= -1.7)

m.c20 = Constraint(expr=   m.x9 - m.x13 <= -1.7)

m.c21 = Constraint(expr=   m.x10 - m.x12 <= -0.5)

m.c22 = Constraint(expr=   m.x11 - m.x13 <= -0.5)

m.c23 = Constraint(expr=   m.x2 <= 9)

m.c24 = Constraint(expr=   m.x3 <= 2.5)
