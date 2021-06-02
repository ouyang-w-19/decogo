#  NLP written by GAMS Convert at 04/21/18 13:51:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         20        4        0       16        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         33       33        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        239       44      195        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,100),initialize=0)

m.obj = Objective(expr=-((18 - 6*m.x1 - 16*m.x4 - 15*m.x7 - 12*m.x10)*m.x18 + (18 - 6*m.x2 - 16*m.x5 - 15*m.x8 - 12*
                       m.x11)*m.x23 + (18 - 6*m.x3 - 16*m.x6 - 15*m.x9 - 12*m.x12)*m.x28 + (15 - 6*m.x1 - 16*m.x4 - 15*
                       m.x7 - 12*m.x10)*m.x19 + (15 - 6*m.x2 - 16*m.x5 - 15*m.x8 - 12*m.x11)*m.x24 + (15 - 6*m.x3 - 16*
                       m.x6 - 15*m.x9 - 12*m.x12)*m.x29 + (19 - 6*m.x1 - 16*m.x4 - 15*m.x7 - 12*m.x10)*m.x20 + (19 - 6*
                       m.x2 - 16*m.x5 - 15*m.x8 - 12*m.x11)*m.x25 + (19 - 6*m.x3 - 16*m.x6 - 15*m.x9 - 12*m.x12)*m.x30
                        + (16 - 6*m.x1 - 16*m.x4 - 15*m.x7 - 12*m.x10)*m.x21 + (16 - 6*m.x2 - 16*m.x5 - 15*m.x8 - 12*
                       m.x11)*m.x26 + (16 - 6*m.x3 - 16*m.x6 - 15*m.x9 - 12*m.x12)*m.x31 + (14 - 6*m.x1 - 16*m.x4 - 15*
                       m.x7 - 12*m.x10)*m.x22 + (14 - 6*m.x2 - 16*m.x5 - 15*m.x8 - 12*m.x11)*m.x27 + (14 - 6*m.x3 - 16*
                       m.x6 - 15*m.x9 - 12*m.x12)*m.x32) - 8*m.x13 - 5*m.x14 - 9*m.x15 - 6*m.x16 - 4*m.x17
                       , sense=minimize)

m.c2 = Constraint(expr=m.x7*m.x18 + m.x7*m.x19 + m.x7*m.x20 + m.x7*m.x21 + m.x7*m.x22 + m.x8*m.x23 + m.x8*m.x24 + m.x8*
                       m.x25 + m.x8*m.x26 + m.x8*m.x27 + m.x9*m.x28 + m.x9*m.x29 + m.x9*m.x30 + m.x9*m.x31 + m.x9*m.x32
                        <= 50)

m.c3 = Constraint(expr=   m.x13 + m.x18 + m.x23 + m.x28 <= 100)

m.c4 = Constraint(expr=   m.x14 + m.x19 + m.x24 + m.x29 <= 200)

m.c5 = Constraint(expr=   m.x15 + m.x20 + m.x25 + m.x30 <= 100)

m.c6 = Constraint(expr=   m.x16 + m.x21 + m.x26 + m.x31 <= 100)

m.c7 = Constraint(expr=   m.x17 + m.x22 + m.x27 + m.x32 <= 100)

m.c8 = Constraint(expr=(-2.5 + 3*m.x1 + m.x4 + m.x7 + 1.5*m.x10)*m.x18 + (-2.5 + 3*m.x2 + m.x5 + m.x8 + 1.5*m.x11)*m.x23
                        + (-2.5 + 3*m.x3 + m.x6 + m.x9 + 1.5*m.x12)*m.x28 - 0.5*m.x13 <= 0)

m.c9 = Constraint(expr=(-2 + m.x1 + 3*m.x4 + 2.5*m.x7 + 2.5*m.x10)*m.x18 + (-2 + m.x2 + 3*m.x5 + 2.5*m.x8 + 2.5*m.x11)*
                       m.x23 + (-2 + m.x3 + 3*m.x6 + 2.5*m.x9 + 2.5*m.x12)*m.x28 + 0.5*m.x13 <= 0)

m.c10 = Constraint(expr=(-1.5 + 3*m.x1 + m.x4 + m.x7 + 1.5*m.x10)*m.x19 + (-1.5 + 3*m.x2 + m.x5 + m.x8 + 1.5*m.x11)*
                        m.x24 + (-1.5 + 3*m.x3 + m.x6 + m.x9 + 1.5*m.x12)*m.x29 + 0.5*m.x14 <= 0)

m.c11 = Constraint(expr=(-2.5 + m.x1 + 3*m.x4 + 2.5*m.x7 + 2.5*m.x10)*m.x19 + (-2.5 + m.x2 + 3*m.x5 + 2.5*m.x8 + 2.5*
                        m.x11)*m.x24 + (-2.5 + m.x3 + 3*m.x6 + 2.5*m.x9 + 2.5*m.x12)*m.x29 <= 0)

m.c12 = Constraint(expr=(-2 + 3*m.x1 + m.x4 + m.x7 + 1.5*m.x10)*m.x20 + (-2 + 3*m.x2 + m.x5 + m.x8 + 1.5*m.x11)*m.x25 + 
                        (-2 + 3*m.x3 + m.x6 + m.x9 + 1.5*m.x12)*m.x30 <= 0)

m.c13 = Constraint(expr=(-2.6 + m.x1 + 3*m.x4 + 2.5*m.x7 + 2.5*m.x10)*m.x20 + (-2.6 + m.x2 + 3*m.x5 + 2.5*m.x8 + 2.5*
                        m.x11)*m.x25 + (-2.6 + m.x3 + 3*m.x6 + 2.5*m.x9 + 2.5*m.x12)*m.x30 - 0.1*m.x15 <= 0)

m.c14 = Constraint(expr=(-2 + 3*m.x1 + m.x4 + m.x7 + 1.5*m.x10)*m.x21 + (-2 + 3*m.x2 + m.x5 + m.x8 + 1.5*m.x11)*m.x26 + 
                        (-2 + 3*m.x3 + m.x6 + m.x9 + 1.5*m.x12)*m.x31 <= 0)

m.c15 = Constraint(expr=(-2 + m.x1 + 3*m.x4 + 2.5*m.x7 + 2.5*m.x10)*m.x21 + (-2 + m.x2 + 3*m.x5 + 2.5*m.x8 + 2.5*m.x11)*
                        m.x26 + (-2 + m.x3 + 3*m.x6 + 2.5*m.x9 + 2.5*m.x12)*m.x31 + 0.5*m.x16 <= 0)

m.c16 = Constraint(expr=(-2 + 3*m.x1 + m.x4 + m.x7 + 1.5*m.x10)*m.x22 + (-2 + 3*m.x2 + m.x5 + m.x8 + 1.5*m.x11)*m.x27 + 
                        (-2 + 3*m.x3 + m.x6 + m.x9 + 1.5*m.x12)*m.x32 <= 0)

m.c17 = Constraint(expr=(-2 + m.x1 + 3*m.x4 + 2.5*m.x7 + 2.5*m.x10)*m.x22 + (-2 + m.x2 + 3*m.x5 + 2.5*m.x8 + 2.5*m.x11)*
                        m.x27 + (-2 + m.x3 + 3*m.x6 + 2.5*m.x9 + 2.5*m.x12)*m.x32 + 0.5*m.x17 <= 0)

m.c18 = Constraint(expr=   m.x1 + m.x4 + m.x7 + m.x10 == 1)

m.c19 = Constraint(expr=   m.x2 + m.x5 + m.x8 + m.x11 == 1)

m.c20 = Constraint(expr=   m.x3 + m.x6 + m.x9 + m.x12 == 1)
