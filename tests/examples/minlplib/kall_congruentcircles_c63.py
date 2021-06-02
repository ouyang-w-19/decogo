#  NLP written by GAMS Convert at 04/21/18 13:52:27
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         46        2       15       29        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         16       16        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        121       59       62        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0.25,15.2),initialize=0.25)
m.x2 = Var(within=Reals,bounds=(0.5,7.5),initialize=0.5)
m.x3 = Var(within=Reals,bounds=(0.5,1.4),initialize=0.5)
m.x4 = Var(within=Reals,bounds=(0.5,7.5),initialize=0.5)
m.x5 = Var(within=Reals,bounds=(0.5,1.4),initialize=0.5)
m.x6 = Var(within=Reals,bounds=(0.5,7.5),initialize=0.5)
m.x7 = Var(within=Reals,bounds=(0.5,1.4),initialize=0.5)
m.x8 = Var(within=Reals,bounds=(0.5,7.5),initialize=0.5)
m.x9 = Var(within=Reals,bounds=(0.5,1.4),initialize=0.5)
m.x10 = Var(within=Reals,bounds=(0.5,7.5),initialize=0.5)
m.x11 = Var(within=Reals,bounds=(0.5,1.4),initialize=0.5)
m.x12 = Var(within=Reals,bounds=(0.5,7.5),initialize=0.5)
m.x13 = Var(within=Reals,bounds=(0.5,1.4),initialize=0.5)
m.x14 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,1.9),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,15.2),initialize=0)

m.obj = Objective(expr=m.x16, sense=minimize)

m.c1 = Constraint(expr= - m.x1 + m.x16 == -4.71238898038469)

m.c2 = Constraint(expr=-m.x14*m.x15 + m.x1 == 0)

m.c3 = Constraint(expr=(m.x2 - m.x4)*(m.x2 - m.x4) + (m.x3 - m.x5)*(m.x3 - m.x5) >= 1)

m.c4 = Constraint(expr=(m.x2 - m.x6)*(m.x2 - m.x6) + (m.x3 - m.x7)*(m.x3 - m.x7) >= 1)

m.c5 = Constraint(expr=(m.x2 - m.x8)*(m.x2 - m.x8) + (m.x3 - m.x9)*(m.x3 - m.x9) >= 1)

m.c6 = Constraint(expr=(m.x2 - m.x10)*(m.x2 - m.x10) + (m.x3 - m.x11)*(m.x3 - m.x11) >= 1)

m.c7 = Constraint(expr=(m.x2 - m.x12)*(m.x2 - m.x12) + (m.x3 - m.x13)*(m.x3 - m.x13) >= 1)

m.c8 = Constraint(expr=(m.x4 - m.x6)*(m.x4 - m.x6) + (m.x5 - m.x7)*(m.x5 - m.x7) >= 1)

m.c9 = Constraint(expr=(m.x4 - m.x8)*(m.x4 - m.x8) + (m.x5 - m.x9)*(m.x5 - m.x9) >= 1)

m.c10 = Constraint(expr=(m.x4 - m.x10)*(m.x4 - m.x10) + (m.x5 - m.x11)*(m.x5 - m.x11) >= 1)

m.c11 = Constraint(expr=(m.x4 - m.x12)*(m.x4 - m.x12) + (m.x5 - m.x13)*(m.x5 - m.x13) >= 1)

m.c12 = Constraint(expr=(m.x6 - m.x8)*(m.x6 - m.x8) + (m.x7 - m.x9)*(m.x7 - m.x9) >= 1)

m.c13 = Constraint(expr=(m.x6 - m.x10)*(m.x6 - m.x10) + (m.x7 - m.x11)*(m.x7 - m.x11) >= 1)

m.c14 = Constraint(expr=(m.x6 - m.x12)*(m.x6 - m.x12) + (m.x7 - m.x13)*(m.x7 - m.x13) >= 1)

m.c15 = Constraint(expr=(m.x8 - m.x10)*(m.x8 - m.x10) + (m.x9 - m.x11)*(m.x9 - m.x11) >= 1)

m.c16 = Constraint(expr=(m.x8 - m.x12)*(m.x8 - m.x12) + (m.x9 - m.x13)*(m.x9 - m.x13) >= 1)

m.c17 = Constraint(expr=(m.x10 - m.x12)*(m.x10 - m.x12) + (m.x11 - m.x13)*(m.x11 - m.x13) >= 1)

m.c18 = Constraint(expr=   m.x2 - m.x14 <= -0.5)

m.c19 = Constraint(expr=   m.x3 - m.x15 <= -0.5)

m.c20 = Constraint(expr=   m.x4 - m.x14 <= -0.5)

m.c21 = Constraint(expr=   m.x5 - m.x15 <= -0.5)

m.c22 = Constraint(expr=   m.x6 - m.x14 <= -0.5)

m.c23 = Constraint(expr=   m.x7 - m.x15 <= -0.5)

m.c24 = Constraint(expr=   m.x8 - m.x14 <= -0.5)

m.c25 = Constraint(expr=   m.x9 - m.x15 <= -0.5)

m.c26 = Constraint(expr=   m.x10 - m.x14 <= -0.5)

m.c27 = Constraint(expr=   m.x11 - m.x15 <= -0.5)

m.c28 = Constraint(expr=   m.x12 - m.x14 <= -0.5)

m.c29 = Constraint(expr=   m.x13 - m.x15 <= -0.5)

m.c30 = Constraint(expr=   m.x2 <= 4)

m.c31 = Constraint(expr=   m.x3 <= 0.95)

m.c32 = Constraint(expr=   m.x2 - m.x4 <= 0)

m.c33 = Constraint(expr=   m.x2 - m.x6 <= 0)

m.c34 = Constraint(expr=   m.x2 - m.x8 <= 0)

m.c35 = Constraint(expr=   m.x2 - m.x10 <= 0)

m.c36 = Constraint(expr=   m.x2 - m.x12 <= 0)

m.c37 = Constraint(expr=   m.x4 - m.x6 <= 0)

m.c38 = Constraint(expr=   m.x4 - m.x8 <= 0)

m.c39 = Constraint(expr=   m.x4 - m.x10 <= 0)

m.c40 = Constraint(expr=   m.x4 - m.x12 <= 0)

m.c41 = Constraint(expr=   m.x6 - m.x8 <= 0)

m.c42 = Constraint(expr=   m.x6 - m.x10 <= 0)

m.c43 = Constraint(expr=   m.x6 - m.x12 <= 0)

m.c44 = Constraint(expr=   m.x8 - m.x10 <= 0)

m.c45 = Constraint(expr=   m.x8 - m.x12 <= 0)

m.c46 = Constraint(expr=   m.x10 - m.x12 <= 0)
