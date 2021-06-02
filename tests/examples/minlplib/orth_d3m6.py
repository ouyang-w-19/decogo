#  NLP written by GAMS Convert at 04/21/18 13:52:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         62       17        5       40        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         25       25        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        526       58      468        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x2 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x6 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x7 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x8 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x9 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x10 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x11 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x12 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x13 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x14 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x15 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x16 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x17 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x18 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x19 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,1),initialize=0)

m.obj = Objective(expr=m.x1, sense=minimize)

m.c1 = Constraint(expr=   m.x2 == 1)

m.c2 = Constraint(expr=   m.x3 == 0)

m.c3 = Constraint(expr=   m.x4 == 0)

m.c4 = Constraint(expr=   m.x5 == 0)

m.c5 = Constraint(expr=   m.x6 >= 0)

m.c6 = Constraint(expr=   m.x7 - m.x8 >= 0)

m.c7 = Constraint(expr=   m.x8 - m.x9 >= 0)

m.c8 = Constraint(expr=   m.x9 - m.x10 >= 0)

m.c9 = Constraint(expr=   m.x10 >= 0)

m.c10 = Constraint(expr=m.x2**2 + m.x3**2 + m.x4**2 == 1)

m.c11 = Constraint(expr=m.x6**2 + m.x11**2 + m.x5**2 == 1)

m.c12 = Constraint(expr=m.x7**2 + m.x12**2 + m.x13**2 == 1)

m.c13 = Constraint(expr=m.x8**2 + m.x14**2 + m.x15**2 == 1)

m.c14 = Constraint(expr=m.x9**2 + m.x16**2 + m.x17**2 == 1)

m.c15 = Constraint(expr=m.x10**2 + m.x18**2 + m.x19**2 == 1)

m.c16 = Constraint(expr=m.x2**2*m.x20 + m.x6**2*m.x21 + m.x7**2*m.x22 + m.x8**2*m.x23 + m.x9**2*m.x24 + m.x10**2*m.x25
                         == 1)

m.c17 = Constraint(expr=m.x20*m.x2*m.x3 + m.x21*m.x6*m.x11 + m.x22*m.x7*m.x12 + m.x23*m.x8*m.x14 + m.x24*m.x9*m.x16 + 
                        m.x25*m.x10*m.x18 == 0)

m.c18 = Constraint(expr=m.x20*m.x2*m.x4 + m.x21*m.x6*m.x5 + m.x22*m.x7*m.x13 + m.x23*m.x8*m.x15 + m.x24*m.x9*m.x17 + 
                        m.x25*m.x10*m.x19 == 0)

m.c19 = Constraint(expr=m.x3**2*m.x20 + m.x11**2*m.x21 + m.x12**2*m.x22 + m.x14**2*m.x23 + m.x16**2*m.x24 + m.x18**2*
                        m.x25 == 1)

m.c20 = Constraint(expr=m.x20*m.x3*m.x4 + m.x21*m.x11*m.x5 + m.x22*m.x12*m.x13 + m.x23*m.x14*m.x15 + m.x24*m.x16*m.x17
                         + m.x25*m.x18*m.x19 == 0)

m.c21 = Constraint(expr=m.x4**2*m.x20 + m.x5**2*m.x21 + m.x13**2*m.x22 + m.x15**2*m.x23 + m.x17**2*m.x24 + m.x19**2*
                        m.x25 == 1)

m.c22 = Constraint(expr=   m.x20 + m.x21 + m.x22 + m.x23 + m.x24 + m.x25 == 3)

m.c23 = Constraint(expr=m.x6*m.x12*m.x4 - m.x7*m.x11*m.x4 + m.x7*m.x3*m.x5 - m.x2*m.x12*m.x5 - m.x6*m.x3*m.x13 + m.x2*
                        m.x11*m.x13 - m.x1 <= 0)

m.c24 = Constraint(expr=m.x7*m.x11*m.x4 - m.x6*m.x12*m.x4 - m.x7*m.x3*m.x5 + m.x2*m.x12*m.x5 + m.x6*m.x3*m.x13 - m.x2*
                        m.x11*m.x13 - m.x1 <= 0)

m.c25 = Constraint(expr=m.x6*m.x14*m.x4 - m.x8*m.x11*m.x4 + m.x8*m.x3*m.x5 - m.x2*m.x14*m.x5 - m.x6*m.x3*m.x15 + m.x2*
                        m.x11*m.x15 - m.x1 <= 0)

m.c26 = Constraint(expr=m.x8*m.x11*m.x4 - m.x6*m.x14*m.x4 - m.x8*m.x3*m.x5 + m.x2*m.x14*m.x5 + m.x6*m.x3*m.x15 - m.x2*
                        m.x11*m.x15 - m.x1 <= 0)

m.c27 = Constraint(expr=m.x6*m.x16*m.x4 - m.x9*m.x11*m.x4 + m.x9*m.x3*m.x5 - m.x2*m.x16*m.x5 - m.x6*m.x3*m.x17 + m.x2*
                        m.x11*m.x17 - m.x1 <= 0)

m.c28 = Constraint(expr=m.x9*m.x11*m.x4 - m.x6*m.x16*m.x4 - m.x9*m.x3*m.x5 + m.x2*m.x16*m.x5 + m.x6*m.x3*m.x17 - m.x2*
                        m.x11*m.x17 - m.x1 <= 0)

m.c29 = Constraint(expr=m.x6*m.x18*m.x4 - m.x10*m.x11*m.x4 + m.x10*m.x3*m.x5 - m.x2*m.x18*m.x5 - m.x6*m.x3*m.x19 + m.x2*
                        m.x11*m.x19 - m.x1 <= 0)

m.c30 = Constraint(expr=m.x10*m.x11*m.x4 - m.x6*m.x18*m.x4 - m.x10*m.x3*m.x5 + m.x2*m.x18*m.x5 + m.x6*m.x3*m.x19 - m.x2*
                        m.x11*m.x19 - m.x1 <= 0)

m.c31 = Constraint(expr=m.x7*m.x14*m.x4 - m.x8*m.x12*m.x4 + m.x8*m.x3*m.x13 - m.x2*m.x14*m.x13 - m.x7*m.x3*m.x15 + m.x2*
                        m.x12*m.x15 - m.x1 <= 0)

m.c32 = Constraint(expr=m.x8*m.x12*m.x4 - m.x7*m.x14*m.x4 - m.x8*m.x3*m.x13 + m.x2*m.x14*m.x13 + m.x7*m.x3*m.x15 - m.x2*
                        m.x12*m.x15 - m.x1 <= 0)

m.c33 = Constraint(expr=m.x7*m.x16*m.x4 - m.x9*m.x12*m.x4 + m.x9*m.x3*m.x13 - m.x2*m.x16*m.x13 - m.x7*m.x3*m.x17 + m.x2*
                        m.x12*m.x17 - m.x1 <= 0)

m.c34 = Constraint(expr=m.x9*m.x12*m.x4 - m.x7*m.x16*m.x4 - m.x9*m.x3*m.x13 + m.x2*m.x16*m.x13 + m.x7*m.x3*m.x17 - m.x2*
                        m.x12*m.x17 - m.x1 <= 0)

m.c35 = Constraint(expr=m.x7*m.x18*m.x4 - m.x10*m.x12*m.x4 + m.x10*m.x3*m.x13 - m.x2*m.x18*m.x13 - m.x7*m.x3*m.x19 + 
                        m.x2*m.x12*m.x19 - m.x1 <= 0)

m.c36 = Constraint(expr=m.x10*m.x12*m.x4 - m.x7*m.x18*m.x4 - m.x10*m.x3*m.x13 + m.x2*m.x18*m.x13 + m.x7*m.x3*m.x19 - 
                        m.x2*m.x12*m.x19 - m.x1 <= 0)

m.c37 = Constraint(expr=m.x8*m.x16*m.x4 - m.x9*m.x14*m.x4 + m.x9*m.x3*m.x15 - m.x2*m.x16*m.x15 - m.x8*m.x3*m.x17 + m.x2*
                        m.x14*m.x17 - m.x1 <= 0)

m.c38 = Constraint(expr=m.x9*m.x14*m.x4 - m.x8*m.x16*m.x4 - m.x9*m.x3*m.x15 + m.x2*m.x16*m.x15 + m.x8*m.x3*m.x17 - m.x2*
                        m.x14*m.x17 - m.x1 <= 0)

m.c39 = Constraint(expr=m.x8*m.x18*m.x4 - m.x10*m.x14*m.x4 + m.x10*m.x3*m.x15 - m.x2*m.x18*m.x15 - m.x8*m.x3*m.x19 + 
                        m.x2*m.x14*m.x19 - m.x1 <= 0)

m.c40 = Constraint(expr=m.x10*m.x14*m.x4 - m.x8*m.x18*m.x4 - m.x10*m.x3*m.x15 + m.x2*m.x18*m.x15 + m.x8*m.x3*m.x19 - 
                        m.x2*m.x14*m.x19 - m.x1 <= 0)

m.c41 = Constraint(expr=m.x9*m.x18*m.x4 - m.x10*m.x16*m.x4 + m.x10*m.x3*m.x17 - m.x2*m.x18*m.x17 - m.x9*m.x3*m.x19 + 
                        m.x2*m.x16*m.x19 - m.x1 <= 0)

m.c42 = Constraint(expr=m.x10*m.x16*m.x4 - m.x9*m.x18*m.x4 - m.x10*m.x3*m.x17 + m.x2*m.x18*m.x17 + m.x9*m.x3*m.x19 - 
                        m.x2*m.x16*m.x19 - m.x1 <= 0)

m.c43 = Constraint(expr=m.x7*m.x14*m.x5 - m.x8*m.x12*m.x5 + m.x8*m.x11*m.x13 - m.x6*m.x14*m.x13 - m.x7*m.x11*m.x15 + 
                        m.x6*m.x12*m.x15 - m.x1 <= 0)

m.c44 = Constraint(expr=m.x8*m.x12*m.x5 - m.x7*m.x14*m.x5 - m.x8*m.x11*m.x13 + m.x6*m.x14*m.x13 + m.x7*m.x11*m.x15 - 
                        m.x6*m.x12*m.x15 - m.x1 <= 0)

m.c45 = Constraint(expr=m.x7*m.x16*m.x5 - m.x9*m.x12*m.x5 + m.x9*m.x11*m.x13 - m.x6*m.x16*m.x13 - m.x7*m.x11*m.x17 + 
                        m.x6*m.x12*m.x17 - m.x1 <= 0)

m.c46 = Constraint(expr=m.x9*m.x12*m.x5 - m.x7*m.x16*m.x5 - m.x9*m.x11*m.x13 + m.x6*m.x16*m.x13 + m.x7*m.x11*m.x17 - 
                        m.x6*m.x12*m.x17 - m.x1 <= 0)

m.c47 = Constraint(expr=m.x7*m.x18*m.x5 - m.x10*m.x12*m.x5 + m.x10*m.x11*m.x13 - m.x6*m.x18*m.x13 - m.x7*m.x11*m.x19 + 
                        m.x6*m.x12*m.x19 - m.x1 <= 0)

m.c48 = Constraint(expr=m.x10*m.x12*m.x5 - m.x7*m.x18*m.x5 - m.x10*m.x11*m.x13 + m.x6*m.x18*m.x13 + m.x7*m.x11*m.x19 - 
                        m.x6*m.x12*m.x19 - m.x1 <= 0)

m.c49 = Constraint(expr=m.x8*m.x16*m.x5 - m.x9*m.x14*m.x5 + m.x9*m.x11*m.x15 - m.x6*m.x16*m.x15 - m.x8*m.x11*m.x17 + 
                        m.x6*m.x14*m.x17 - m.x1 <= 0)

m.c50 = Constraint(expr=m.x9*m.x14*m.x5 - m.x8*m.x16*m.x5 - m.x9*m.x11*m.x15 + m.x6*m.x16*m.x15 + m.x8*m.x11*m.x17 - 
                        m.x6*m.x14*m.x17 - m.x1 <= 0)

m.c51 = Constraint(expr=m.x8*m.x18*m.x5 - m.x10*m.x14*m.x5 + m.x10*m.x11*m.x15 - m.x6*m.x18*m.x15 - m.x8*m.x11*m.x19 + 
                        m.x6*m.x14*m.x19 - m.x1 <= 0)

m.c52 = Constraint(expr=m.x10*m.x14*m.x5 - m.x8*m.x18*m.x5 - m.x10*m.x11*m.x15 + m.x6*m.x18*m.x15 + m.x8*m.x11*m.x19 - 
                        m.x6*m.x14*m.x19 - m.x1 <= 0)

m.c53 = Constraint(expr=m.x9*m.x18*m.x5 - m.x10*m.x16*m.x5 + m.x10*m.x11*m.x17 - m.x6*m.x18*m.x17 - m.x9*m.x11*m.x19 + 
                        m.x6*m.x16*m.x19 - m.x1 <= 0)

m.c54 = Constraint(expr=m.x10*m.x16*m.x5 - m.x9*m.x18*m.x5 - m.x10*m.x11*m.x17 + m.x6*m.x18*m.x17 + m.x9*m.x11*m.x19 - 
                        m.x6*m.x16*m.x19 - m.x1 <= 0)

m.c55 = Constraint(expr=m.x8*m.x16*m.x13 - m.x9*m.x14*m.x13 + m.x9*m.x12*m.x15 - m.x7*m.x16*m.x15 - m.x8*m.x12*m.x17 + 
                        m.x7*m.x14*m.x17 - m.x1 <= 0)

m.c56 = Constraint(expr=m.x9*m.x14*m.x13 - m.x8*m.x16*m.x13 - m.x9*m.x12*m.x15 + m.x7*m.x16*m.x15 + m.x8*m.x12*m.x17 - 
                        m.x7*m.x14*m.x17 - m.x1 <= 0)

m.c57 = Constraint(expr=m.x8*m.x18*m.x13 - m.x10*m.x14*m.x13 + m.x10*m.x12*m.x15 - m.x7*m.x18*m.x15 - m.x8*m.x12*m.x19
                         + m.x7*m.x14*m.x19 - m.x1 <= 0)

m.c58 = Constraint(expr=m.x10*m.x14*m.x13 - m.x8*m.x18*m.x13 - m.x10*m.x12*m.x15 + m.x7*m.x18*m.x15 + m.x8*m.x12*m.x19
                         - m.x7*m.x14*m.x19 - m.x1 <= 0)

m.c59 = Constraint(expr=m.x9*m.x18*m.x13 - m.x10*m.x16*m.x13 + m.x10*m.x12*m.x17 - m.x7*m.x18*m.x17 - m.x9*m.x12*m.x19
                         + m.x7*m.x16*m.x19 - m.x1 <= 0)

m.c60 = Constraint(expr=m.x10*m.x16*m.x13 - m.x9*m.x18*m.x13 - m.x10*m.x12*m.x17 + m.x7*m.x18*m.x17 + m.x9*m.x12*m.x19
                         - m.x7*m.x16*m.x19 - m.x1 <= 0)

m.c61 = Constraint(expr=m.x9*m.x18*m.x15 - m.x10*m.x16*m.x15 + m.x10*m.x14*m.x17 - m.x8*m.x18*m.x17 - m.x9*m.x14*m.x19
                         + m.x8*m.x16*m.x19 - m.x1 <= 0)

m.c62 = Constraint(expr=m.x10*m.x16*m.x15 - m.x9*m.x18*m.x15 - m.x10*m.x14*m.x17 + m.x8*m.x18*m.x17 + m.x9*m.x14*m.x19
                         - m.x8*m.x16*m.x19 - m.x1 <= 0)
