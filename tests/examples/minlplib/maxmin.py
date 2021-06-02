#  NLP written by GAMS Convert at 04/21/18 13:52:30
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         78        0        0       78        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         27       27        0        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        390       78      312        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0.550375356)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0.301137904)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=0.292212117)
m.x6 = Var(within=Reals,bounds=(0,1),initialize=0.224052867)
m.x7 = Var(within=Reals,bounds=(0,1),initialize=0.349830504)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=0.856270347)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=0.067113723)
m.x10 = Var(within=Reals,bounds=(0,1),initialize=0.500210669)
m.x11 = Var(within=Reals,bounds=(0,1),initialize=0.998117627)
m.x12 = Var(within=Reals,bounds=(0,1),initialize=0.578733378)
m.x13 = Var(within=Reals,bounds=(0,1),initialize=0.991133039)
m.x14 = Var(within=Reals,bounds=(0,1),initialize=0.762250467)
m.x15 = Var(within=Reals,bounds=(0,1),initialize=0.130692483)
m.x16 = Var(within=Reals,bounds=(0,1),initialize=0.639718759)
m.x17 = Var(within=Reals,bounds=(0,1),initialize=0.159517864)
m.x18 = Var(within=Reals,bounds=(0,1),initialize=0.250080533)
m.x19 = Var(within=Reals,bounds=(0,1),initialize=0.668928609)
m.x20 = Var(within=Reals,bounds=(0,1),initialize=0.435356381)
m.x21 = Var(within=Reals,bounds=(0,1),initialize=0.359700266)
m.x22 = Var(within=Reals,bounds=(0,1),initialize=0.351441368)
m.x23 = Var(within=Reals,bounds=(0,1),initialize=0.13149159)
m.x24 = Var(within=Reals,bounds=(0,1),initialize=0.150101788)
m.x25 = Var(within=Reals,bounds=(0,1),initialize=0.58911365)
m.x26 = Var(within=Reals,bounds=(0,1),initialize=0.830892812)
m.x27 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x27, sense=minimize)

m.c1 = Constraint(expr=-sqrt((m.x3 - m.x1)**2 + (m.x4 - m.x2)**2) - m.x27 <= 0)

m.c2 = Constraint(expr=-sqrt((m.x5 - m.x1)**2 + (m.x6 - m.x2)**2) - m.x27 <= 0)

m.c3 = Constraint(expr=-sqrt((m.x5 - m.x3)**2 + (m.x6 - m.x4)**2) - m.x27 <= 0)

m.c4 = Constraint(expr=-sqrt((m.x7 - m.x1)**2 + (m.x8 - m.x2)**2) - m.x27 <= 0)

m.c5 = Constraint(expr=-sqrt((m.x7 - m.x3)**2 + (m.x8 - m.x4)**2) - m.x27 <= 0)

m.c6 = Constraint(expr=-sqrt((m.x7 - m.x5)**2 + (m.x8 - m.x6)**2) - m.x27 <= 0)

m.c7 = Constraint(expr=-sqrt((m.x9 - m.x1)**2 + (m.x10 - m.x2)**2) - m.x27 <= 0)

m.c8 = Constraint(expr=-sqrt((m.x9 - m.x3)**2 + (m.x10 - m.x4)**2) - m.x27 <= 0)

m.c9 = Constraint(expr=-sqrt((m.x9 - m.x5)**2 + (m.x10 - m.x6)**2) - m.x27 <= 0)

m.c10 = Constraint(expr=-sqrt((m.x9 - m.x7)**2 + (m.x10 - m.x8)**2) - m.x27 <= 0)

m.c11 = Constraint(expr=-sqrt((m.x11 - m.x1)**2 + (m.x12 - m.x2)**2) - m.x27 <= 0)

m.c12 = Constraint(expr=-sqrt((m.x11 - m.x3)**2 + (m.x12 - m.x4)**2) - m.x27 <= 0)

m.c13 = Constraint(expr=-sqrt((m.x11 - m.x5)**2 + (m.x12 - m.x6)**2) - m.x27 <= 0)

m.c14 = Constraint(expr=-sqrt((m.x11 - m.x7)**2 + (m.x12 - m.x8)**2) - m.x27 <= 0)

m.c15 = Constraint(expr=-sqrt((m.x11 - m.x9)**2 + (m.x12 - m.x10)**2) - m.x27 <= 0)

m.c16 = Constraint(expr=-sqrt((m.x13 - m.x1)**2 + (m.x14 - m.x2)**2) - m.x27 <= 0)

m.c17 = Constraint(expr=-sqrt((m.x13 - m.x3)**2 + (m.x14 - m.x4)**2) - m.x27 <= 0)

m.c18 = Constraint(expr=-sqrt((m.x13 - m.x5)**2 + (m.x14 - m.x6)**2) - m.x27 <= 0)

m.c19 = Constraint(expr=-sqrt((m.x13 - m.x7)**2 + (m.x14 - m.x8)**2) - m.x27 <= 0)

m.c20 = Constraint(expr=-sqrt((m.x13 - m.x9)**2 + (m.x14 - m.x10)**2) - m.x27 <= 0)

m.c21 = Constraint(expr=-sqrt((m.x13 - m.x11)**2 + (m.x14 - m.x12)**2) - m.x27 <= 0)

m.c22 = Constraint(expr=-sqrt((m.x15 - m.x1)**2 + (m.x16 - m.x2)**2) - m.x27 <= 0)

m.c23 = Constraint(expr=-sqrt((m.x15 - m.x3)**2 + (m.x16 - m.x4)**2) - m.x27 <= 0)

m.c24 = Constraint(expr=-sqrt((m.x15 - m.x5)**2 + (m.x16 - m.x6)**2) - m.x27 <= 0)

m.c25 = Constraint(expr=-sqrt((m.x15 - m.x7)**2 + (m.x16 - m.x8)**2) - m.x27 <= 0)

m.c26 = Constraint(expr=-sqrt((m.x15 - m.x9)**2 + (m.x16 - m.x10)**2) - m.x27 <= 0)

m.c27 = Constraint(expr=-sqrt((m.x15 - m.x11)**2 + (m.x16 - m.x12)**2) - m.x27 <= 0)

m.c28 = Constraint(expr=-sqrt((m.x15 - m.x13)**2 + (m.x16 - m.x14)**2) - m.x27 <= 0)

m.c29 = Constraint(expr=-sqrt((m.x17 - m.x1)**2 + (m.x18 - m.x2)**2) - m.x27 <= 0)

m.c30 = Constraint(expr=-sqrt((m.x17 - m.x3)**2 + (m.x18 - m.x4)**2) - m.x27 <= 0)

m.c31 = Constraint(expr=-sqrt((m.x17 - m.x5)**2 + (m.x18 - m.x6)**2) - m.x27 <= 0)

m.c32 = Constraint(expr=-sqrt((m.x17 - m.x7)**2 + (m.x18 - m.x8)**2) - m.x27 <= 0)

m.c33 = Constraint(expr=-sqrt((m.x17 - m.x9)**2 + (m.x18 - m.x10)**2) - m.x27 <= 0)

m.c34 = Constraint(expr=-sqrt((m.x17 - m.x11)**2 + (m.x18 - m.x12)**2) - m.x27 <= 0)

m.c35 = Constraint(expr=-sqrt((m.x17 - m.x13)**2 + (m.x18 - m.x14)**2) - m.x27 <= 0)

m.c36 = Constraint(expr=-sqrt((m.x17 - m.x15)**2 + (m.x18 - m.x16)**2) - m.x27 <= 0)

m.c37 = Constraint(expr=-sqrt((m.x19 - m.x1)**2 + (m.x20 - m.x2)**2) - m.x27 <= 0)

m.c38 = Constraint(expr=-sqrt((m.x19 - m.x3)**2 + (m.x20 - m.x4)**2) - m.x27 <= 0)

m.c39 = Constraint(expr=-sqrt((m.x19 - m.x5)**2 + (m.x20 - m.x6)**2) - m.x27 <= 0)

m.c40 = Constraint(expr=-sqrt((m.x19 - m.x7)**2 + (m.x20 - m.x8)**2) - m.x27 <= 0)

m.c41 = Constraint(expr=-sqrt((m.x19 - m.x9)**2 + (m.x20 - m.x10)**2) - m.x27 <= 0)

m.c42 = Constraint(expr=-sqrt((m.x19 - m.x11)**2 + (m.x20 - m.x12)**2) - m.x27 <= 0)

m.c43 = Constraint(expr=-sqrt((m.x19 - m.x13)**2 + (m.x20 - m.x14)**2) - m.x27 <= 0)

m.c44 = Constraint(expr=-sqrt((m.x19 - m.x15)**2 + (m.x20 - m.x16)**2) - m.x27 <= 0)

m.c45 = Constraint(expr=-sqrt((m.x19 - m.x17)**2 + (m.x20 - m.x18)**2) - m.x27 <= 0)

m.c46 = Constraint(expr=-sqrt((m.x21 - m.x1)**2 + (m.x22 - m.x2)**2) - m.x27 <= 0)

m.c47 = Constraint(expr=-sqrt((m.x21 - m.x3)**2 + (m.x22 - m.x4)**2) - m.x27 <= 0)

m.c48 = Constraint(expr=-sqrt((m.x21 - m.x5)**2 + (m.x22 - m.x6)**2) - m.x27 <= 0)

m.c49 = Constraint(expr=-sqrt((m.x21 - m.x7)**2 + (m.x22 - m.x8)**2) - m.x27 <= 0)

m.c50 = Constraint(expr=-sqrt((m.x21 - m.x9)**2 + (m.x22 - m.x10)**2) - m.x27 <= 0)

m.c51 = Constraint(expr=-sqrt((m.x21 - m.x11)**2 + (m.x22 - m.x12)**2) - m.x27 <= 0)

m.c52 = Constraint(expr=-sqrt((m.x21 - m.x13)**2 + (m.x22 - m.x14)**2) - m.x27 <= 0)

m.c53 = Constraint(expr=-sqrt((m.x21 - m.x15)**2 + (m.x22 - m.x16)**2) - m.x27 <= 0)

m.c54 = Constraint(expr=-sqrt((m.x21 - m.x17)**2 + (m.x22 - m.x18)**2) - m.x27 <= 0)

m.c55 = Constraint(expr=-sqrt((m.x21 - m.x19)**2 + (m.x22 - m.x20)**2) - m.x27 <= 0)

m.c56 = Constraint(expr=-sqrt((m.x23 - m.x1)**2 + (m.x24 - m.x2)**2) - m.x27 <= 0)

m.c57 = Constraint(expr=-sqrt((m.x23 - m.x3)**2 + (m.x24 - m.x4)**2) - m.x27 <= 0)

m.c58 = Constraint(expr=-sqrt((m.x23 - m.x5)**2 + (m.x24 - m.x6)**2) - m.x27 <= 0)

m.c59 = Constraint(expr=-sqrt((m.x23 - m.x7)**2 + (m.x24 - m.x8)**2) - m.x27 <= 0)

m.c60 = Constraint(expr=-sqrt((m.x23 - m.x9)**2 + (m.x24 - m.x10)**2) - m.x27 <= 0)

m.c61 = Constraint(expr=-sqrt((m.x23 - m.x11)**2 + (m.x24 - m.x12)**2) - m.x27 <= 0)

m.c62 = Constraint(expr=-sqrt((m.x23 - m.x13)**2 + (m.x24 - m.x14)**2) - m.x27 <= 0)

m.c63 = Constraint(expr=-sqrt((m.x23 - m.x15)**2 + (m.x24 - m.x16)**2) - m.x27 <= 0)

m.c64 = Constraint(expr=-sqrt((m.x23 - m.x17)**2 + (m.x24 - m.x18)**2) - m.x27 <= 0)

m.c65 = Constraint(expr=-sqrt((m.x23 - m.x19)**2 + (m.x24 - m.x20)**2) - m.x27 <= 0)

m.c66 = Constraint(expr=-sqrt((m.x23 - m.x21)**2 + (m.x24 - m.x22)**2) - m.x27 <= 0)

m.c67 = Constraint(expr=-sqrt((m.x25 - m.x1)**2 + (m.x26 - m.x2)**2) - m.x27 <= 0)

m.c68 = Constraint(expr=-sqrt((m.x25 - m.x3)**2 + (m.x26 - m.x4)**2) - m.x27 <= 0)

m.c69 = Constraint(expr=-sqrt((m.x25 - m.x5)**2 + (m.x26 - m.x6)**2) - m.x27 <= 0)

m.c70 = Constraint(expr=-sqrt((m.x25 - m.x7)**2 + (m.x26 - m.x8)**2) - m.x27 <= 0)

m.c71 = Constraint(expr=-sqrt((m.x25 - m.x9)**2 + (m.x26 - m.x10)**2) - m.x27 <= 0)

m.c72 = Constraint(expr=-sqrt((m.x25 - m.x11)**2 + (m.x26 - m.x12)**2) - m.x27 <= 0)

m.c73 = Constraint(expr=-sqrt((m.x25 - m.x13)**2 + (m.x26 - m.x14)**2) - m.x27 <= 0)

m.c74 = Constraint(expr=-sqrt((m.x25 - m.x15)**2 + (m.x26 - m.x16)**2) - m.x27 <= 0)

m.c75 = Constraint(expr=-sqrt((m.x25 - m.x17)**2 + (m.x26 - m.x18)**2) - m.x27 <= 0)

m.c76 = Constraint(expr=-sqrt((m.x25 - m.x19)**2 + (m.x26 - m.x20)**2) - m.x27 <= 0)

m.c77 = Constraint(expr=-sqrt((m.x25 - m.x21)**2 + (m.x26 - m.x22)**2) - m.x27 <= 0)

m.c78 = Constraint(expr=-sqrt((m.x25 - m.x23)**2 + (m.x26 - m.x24)**2) - m.x27 <= 0)
