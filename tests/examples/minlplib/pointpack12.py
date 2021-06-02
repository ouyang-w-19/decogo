#  NLP written by GAMS Convert at 04/21/18 13:53:09
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         78        0        0       78        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         25       25        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        354       90      264        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0.5,1),initialize=0.5)
m.x2 = Var(within=Reals,bounds=(0.5,1),initialize=0.5)
m.x3 = Var(within=Reals,bounds=(0.5,1),initialize=0.5)
m.x4 = Var(within=Reals,bounds=(0.5,1),initialize=0.5)
m.x5 = Var(within=Reals,bounds=(0.5,1),initialize=0.5)
m.x6 = Var(within=Reals,bounds=(0.5,1),initialize=0.5)
m.x7 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x25, sense=maximize)

m.c1 = Constraint(expr=2*m.x1*m.x2 - m.x1*m.x1 - m.x2*m.x2 - m.x13*m.x13 + 2*m.x13*m.x14 - m.x14*m.x14 + m.x25 <= 0)

m.c2 = Constraint(expr=2*m.x1*m.x3 - m.x1*m.x1 - m.x3*m.x3 - m.x13*m.x13 + 2*m.x13*m.x15 - m.x15*m.x15 + m.x25 <= 0)

m.c3 = Constraint(expr=2*m.x1*m.x4 - m.x1*m.x1 - m.x4*m.x4 - m.x13*m.x13 + 2*m.x13*m.x16 - m.x16*m.x16 + m.x25 <= 0)

m.c4 = Constraint(expr=2*m.x1*m.x5 - m.x1*m.x1 - m.x5*m.x5 - m.x13*m.x13 + 2*m.x13*m.x17 - m.x17*m.x17 + m.x25 <= 0)

m.c5 = Constraint(expr=2*m.x1*m.x6 - m.x1*m.x1 - m.x6*m.x6 - m.x13*m.x13 + 2*m.x13*m.x18 - m.x18*m.x18 + m.x25 <= 0)

m.c6 = Constraint(expr=2*m.x1*m.x7 - m.x1*m.x1 - m.x7*m.x7 - m.x13*m.x13 + 2*m.x13*m.x19 - m.x19*m.x19 + m.x25 <= 0)

m.c7 = Constraint(expr=2*m.x1*m.x8 - m.x1*m.x1 - m.x8*m.x8 - m.x13*m.x13 + 2*m.x13*m.x20 - m.x20*m.x20 + m.x25 <= 0)

m.c8 = Constraint(expr=2*m.x1*m.x9 - m.x1*m.x1 - m.x9*m.x9 - m.x13*m.x13 + 2*m.x13*m.x21 - m.x21*m.x21 + m.x25 <= 0)

m.c9 = Constraint(expr=2*m.x1*m.x10 - m.x1*m.x1 - m.x10*m.x10 - m.x13*m.x13 + 2*m.x13*m.x22 - m.x22*m.x22 + m.x25 <= 0)

m.c10 = Constraint(expr=2*m.x1*m.x11 - m.x1*m.x1 - m.x11*m.x11 - m.x13*m.x13 + 2*m.x13*m.x23 - m.x23*m.x23 + m.x25 <= 0)

m.c11 = Constraint(expr=2*m.x1*m.x12 - m.x1*m.x1 - m.x12*m.x12 - m.x13*m.x13 + 2*m.x13*m.x24 - m.x24*m.x24 + m.x25 <= 0)

m.c12 = Constraint(expr=2*m.x2*m.x3 - m.x2*m.x2 - m.x3*m.x3 - m.x14*m.x14 + 2*m.x14*m.x15 - m.x15*m.x15 + m.x25 <= 0)

m.c13 = Constraint(expr=2*m.x2*m.x4 - m.x2*m.x2 - m.x4*m.x4 - m.x14*m.x14 + 2*m.x14*m.x16 - m.x16*m.x16 + m.x25 <= 0)

m.c14 = Constraint(expr=2*m.x2*m.x5 - m.x2*m.x2 - m.x5*m.x5 - m.x14*m.x14 + 2*m.x14*m.x17 - m.x17*m.x17 + m.x25 <= 0)

m.c15 = Constraint(expr=2*m.x2*m.x6 - m.x2*m.x2 - m.x6*m.x6 - m.x14*m.x14 + 2*m.x14*m.x18 - m.x18*m.x18 + m.x25 <= 0)

m.c16 = Constraint(expr=2*m.x2*m.x7 - m.x2*m.x2 - m.x7*m.x7 - m.x14*m.x14 + 2*m.x14*m.x19 - m.x19*m.x19 + m.x25 <= 0)

m.c17 = Constraint(expr=2*m.x2*m.x8 - m.x2*m.x2 - m.x8*m.x8 - m.x14*m.x14 + 2*m.x14*m.x20 - m.x20*m.x20 + m.x25 <= 0)

m.c18 = Constraint(expr=2*m.x2*m.x9 - m.x2*m.x2 - m.x9*m.x9 - m.x14*m.x14 + 2*m.x14*m.x21 - m.x21*m.x21 + m.x25 <= 0)

m.c19 = Constraint(expr=2*m.x2*m.x10 - m.x2*m.x2 - m.x10*m.x10 - m.x14*m.x14 + 2*m.x14*m.x22 - m.x22*m.x22 + m.x25 <= 0)

m.c20 = Constraint(expr=2*m.x2*m.x11 - m.x2*m.x2 - m.x11*m.x11 - m.x14*m.x14 + 2*m.x14*m.x23 - m.x23*m.x23 + m.x25 <= 0)

m.c21 = Constraint(expr=2*m.x2*m.x12 - m.x2*m.x2 - m.x12*m.x12 - m.x14*m.x14 + 2*m.x14*m.x24 - m.x24*m.x24 + m.x25 <= 0)

m.c22 = Constraint(expr=2*m.x3*m.x4 - m.x3*m.x3 - m.x4*m.x4 - m.x15*m.x15 + 2*m.x15*m.x16 - m.x16*m.x16 + m.x25 <= 0)

m.c23 = Constraint(expr=2*m.x3*m.x5 - m.x3*m.x3 - m.x5*m.x5 - m.x15*m.x15 + 2*m.x15*m.x17 - m.x17*m.x17 + m.x25 <= 0)

m.c24 = Constraint(expr=2*m.x3*m.x6 - m.x3*m.x3 - m.x6*m.x6 - m.x15*m.x15 + 2*m.x15*m.x18 - m.x18*m.x18 + m.x25 <= 0)

m.c25 = Constraint(expr=2*m.x3*m.x7 - m.x3*m.x3 - m.x7*m.x7 - m.x15*m.x15 + 2*m.x15*m.x19 - m.x19*m.x19 + m.x25 <= 0)

m.c26 = Constraint(expr=2*m.x3*m.x8 - m.x3*m.x3 - m.x8*m.x8 - m.x15*m.x15 + 2*m.x15*m.x20 - m.x20*m.x20 + m.x25 <= 0)

m.c27 = Constraint(expr=2*m.x3*m.x9 - m.x3*m.x3 - m.x9*m.x9 - m.x15*m.x15 + 2*m.x15*m.x21 - m.x21*m.x21 + m.x25 <= 0)

m.c28 = Constraint(expr=2*m.x3*m.x10 - m.x3*m.x3 - m.x10*m.x10 - m.x15*m.x15 + 2*m.x15*m.x22 - m.x22*m.x22 + m.x25 <= 0)

m.c29 = Constraint(expr=2*m.x3*m.x11 - m.x3*m.x3 - m.x11*m.x11 - m.x15*m.x15 + 2*m.x15*m.x23 - m.x23*m.x23 + m.x25 <= 0)

m.c30 = Constraint(expr=2*m.x3*m.x12 - m.x3*m.x3 - m.x12*m.x12 - m.x15*m.x15 + 2*m.x15*m.x24 - m.x24*m.x24 + m.x25 <= 0)

m.c31 = Constraint(expr=2*m.x4*m.x5 - m.x4*m.x4 - m.x5*m.x5 - m.x16*m.x16 + 2*m.x16*m.x17 - m.x17*m.x17 + m.x25 <= 0)

m.c32 = Constraint(expr=2*m.x4*m.x6 - m.x4*m.x4 - m.x6*m.x6 - m.x16*m.x16 + 2*m.x16*m.x18 - m.x18*m.x18 + m.x25 <= 0)

m.c33 = Constraint(expr=2*m.x4*m.x7 - m.x4*m.x4 - m.x7*m.x7 - m.x16*m.x16 + 2*m.x16*m.x19 - m.x19*m.x19 + m.x25 <= 0)

m.c34 = Constraint(expr=2*m.x4*m.x8 - m.x4*m.x4 - m.x8*m.x8 - m.x16*m.x16 + 2*m.x16*m.x20 - m.x20*m.x20 + m.x25 <= 0)

m.c35 = Constraint(expr=2*m.x4*m.x9 - m.x4*m.x4 - m.x9*m.x9 - m.x16*m.x16 + 2*m.x16*m.x21 - m.x21*m.x21 + m.x25 <= 0)

m.c36 = Constraint(expr=2*m.x4*m.x10 - m.x4*m.x4 - m.x10*m.x10 - m.x16*m.x16 + 2*m.x16*m.x22 - m.x22*m.x22 + m.x25 <= 0)

m.c37 = Constraint(expr=2*m.x4*m.x11 - m.x4*m.x4 - m.x11*m.x11 - m.x16*m.x16 + 2*m.x16*m.x23 - m.x23*m.x23 + m.x25 <= 0)

m.c38 = Constraint(expr=2*m.x4*m.x12 - m.x4*m.x4 - m.x12*m.x12 - m.x16*m.x16 + 2*m.x16*m.x24 - m.x24*m.x24 + m.x25 <= 0)

m.c39 = Constraint(expr=2*m.x5*m.x6 - m.x5*m.x5 - m.x6*m.x6 - m.x17*m.x17 + 2*m.x17*m.x18 - m.x18*m.x18 + m.x25 <= 0)

m.c40 = Constraint(expr=2*m.x5*m.x7 - m.x5*m.x5 - m.x7*m.x7 - m.x17*m.x17 + 2*m.x17*m.x19 - m.x19*m.x19 + m.x25 <= 0)

m.c41 = Constraint(expr=2*m.x5*m.x8 - m.x5*m.x5 - m.x8*m.x8 - m.x17*m.x17 + 2*m.x17*m.x20 - m.x20*m.x20 + m.x25 <= 0)

m.c42 = Constraint(expr=2*m.x5*m.x9 - m.x5*m.x5 - m.x9*m.x9 - m.x17*m.x17 + 2*m.x17*m.x21 - m.x21*m.x21 + m.x25 <= 0)

m.c43 = Constraint(expr=2*m.x5*m.x10 - m.x5*m.x5 - m.x10*m.x10 - m.x17*m.x17 + 2*m.x17*m.x22 - m.x22*m.x22 + m.x25 <= 0)

m.c44 = Constraint(expr=2*m.x5*m.x11 - m.x5*m.x5 - m.x11*m.x11 - m.x17*m.x17 + 2*m.x17*m.x23 - m.x23*m.x23 + m.x25 <= 0)

m.c45 = Constraint(expr=2*m.x5*m.x12 - m.x5*m.x5 - m.x12*m.x12 - m.x17*m.x17 + 2*m.x17*m.x24 - m.x24*m.x24 + m.x25 <= 0)

m.c46 = Constraint(expr=2*m.x6*m.x7 - m.x6*m.x6 - m.x7*m.x7 - m.x18*m.x18 + 2*m.x18*m.x19 - m.x19*m.x19 + m.x25 <= 0)

m.c47 = Constraint(expr=2*m.x6*m.x8 - m.x6*m.x6 - m.x8*m.x8 - m.x18*m.x18 + 2*m.x18*m.x20 - m.x20*m.x20 + m.x25 <= 0)

m.c48 = Constraint(expr=2*m.x6*m.x9 - m.x6*m.x6 - m.x9*m.x9 - m.x18*m.x18 + 2*m.x18*m.x21 - m.x21*m.x21 + m.x25 <= 0)

m.c49 = Constraint(expr=2*m.x6*m.x10 - m.x6*m.x6 - m.x10*m.x10 - m.x18*m.x18 + 2*m.x18*m.x22 - m.x22*m.x22 + m.x25 <= 0)

m.c50 = Constraint(expr=2*m.x6*m.x11 - m.x6*m.x6 - m.x11*m.x11 - m.x18*m.x18 + 2*m.x18*m.x23 - m.x23*m.x23 + m.x25 <= 0)

m.c51 = Constraint(expr=2*m.x6*m.x12 - m.x6*m.x6 - m.x12*m.x12 - m.x18*m.x18 + 2*m.x18*m.x24 - m.x24*m.x24 + m.x25 <= 0)

m.c52 = Constraint(expr=2*m.x7*m.x8 - m.x7*m.x7 - m.x8*m.x8 - m.x19*m.x19 + 2*m.x19*m.x20 - m.x20*m.x20 + m.x25 <= 0)

m.c53 = Constraint(expr=2*m.x7*m.x9 - m.x7*m.x7 - m.x9*m.x9 - m.x19*m.x19 + 2*m.x19*m.x21 - m.x21*m.x21 + m.x25 <= 0)

m.c54 = Constraint(expr=2*m.x7*m.x10 - m.x7*m.x7 - m.x10*m.x10 - m.x19*m.x19 + 2*m.x19*m.x22 - m.x22*m.x22 + m.x25 <= 0)

m.c55 = Constraint(expr=2*m.x7*m.x11 - m.x7*m.x7 - m.x11*m.x11 - m.x19*m.x19 + 2*m.x19*m.x23 - m.x23*m.x23 + m.x25 <= 0)

m.c56 = Constraint(expr=2*m.x7*m.x12 - m.x7*m.x7 - m.x12*m.x12 - m.x19*m.x19 + 2*m.x19*m.x24 - m.x24*m.x24 + m.x25 <= 0)

m.c57 = Constraint(expr=2*m.x8*m.x9 - m.x8*m.x8 - m.x9*m.x9 - m.x20*m.x20 + 2*m.x20*m.x21 - m.x21*m.x21 + m.x25 <= 0)

m.c58 = Constraint(expr=2*m.x8*m.x10 - m.x8*m.x8 - m.x10*m.x10 - m.x20*m.x20 + 2*m.x20*m.x22 - m.x22*m.x22 + m.x25 <= 0)

m.c59 = Constraint(expr=2*m.x8*m.x11 - m.x8*m.x8 - m.x11*m.x11 - m.x20*m.x20 + 2*m.x20*m.x23 - m.x23*m.x23 + m.x25 <= 0)

m.c60 = Constraint(expr=2*m.x8*m.x12 - m.x8*m.x8 - m.x12*m.x12 - m.x20*m.x20 + 2*m.x20*m.x24 - m.x24*m.x24 + m.x25 <= 0)

m.c61 = Constraint(expr=2*m.x9*m.x10 - m.x9*m.x9 - m.x10*m.x10 - m.x21*m.x21 + 2*m.x21*m.x22 - m.x22*m.x22 + m.x25 <= 0)

m.c62 = Constraint(expr=2*m.x9*m.x11 - m.x9*m.x9 - m.x11*m.x11 - m.x21*m.x21 + 2*m.x21*m.x23 - m.x23*m.x23 + m.x25 <= 0)

m.c63 = Constraint(expr=2*m.x9*m.x12 - m.x9*m.x9 - m.x12*m.x12 - m.x21*m.x21 + 2*m.x21*m.x24 - m.x24*m.x24 + m.x25 <= 0)

m.c64 = Constraint(expr=2*m.x10*m.x11 - m.x10*m.x10 - m.x11*m.x11 - m.x22*m.x22 + 2*m.x22*m.x23 - m.x23*m.x23 + m.x25
                         <= 0)

m.c65 = Constraint(expr=2*m.x10*m.x12 - m.x10*m.x10 - m.x12*m.x12 - m.x22*m.x22 + 2*m.x22*m.x24 - m.x24*m.x24 + m.x25
                         <= 0)

m.c66 = Constraint(expr=2*m.x11*m.x12 - m.x11*m.x11 - m.x12*m.x12 - m.x23*m.x23 + 2*m.x23*m.x24 - m.x24*m.x24 + m.x25
                         <= 0)

m.c67 = Constraint(expr= - m.x13 + m.x14 <= 0)

m.c68 = Constraint(expr= - m.x1 + m.x2 <= 0)

m.c69 = Constraint(expr= - m.x2 + m.x3 <= 0)

m.c70 = Constraint(expr= - m.x3 + m.x4 <= 0)

m.c71 = Constraint(expr= - m.x4 + m.x5 <= 0)

m.c72 = Constraint(expr= - m.x5 + m.x6 <= 0)

m.c73 = Constraint(expr= - m.x6 + m.x7 <= 0)

m.c74 = Constraint(expr= - m.x7 + m.x8 <= 0)

m.c75 = Constraint(expr= - m.x8 + m.x9 <= 0)

m.c76 = Constraint(expr= - m.x9 + m.x10 <= 0)

m.c77 = Constraint(expr= - m.x10 + m.x11 <= 0)

m.c78 = Constraint(expr= - m.x11 + m.x12 <= 0)
