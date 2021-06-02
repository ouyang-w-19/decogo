#  NLP written by GAMS Convert at 04/21/18 13:51:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         11       11        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         25       25        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         73       49       24        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,100),initialize=6)
m.x2 = Var(within=Reals,bounds=(0,100),initialize=2)
m.x3 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,100),initialize=3)
m.x7 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,100),initialize=21)
m.x9 = Var(within=Reals,bounds=(0,100),initialize=20)
m.x10 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,100),initialize=24)
m.x14 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,100),initialize=3)
m.x18 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,100),initialize=13)
m.x20 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,100),initialize=12)
m.x23 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,100),initialize=0)

m.obj = Objective(expr=300*m.x1 - 7*m.x1*m.x1 - 4*m.x2*m.x2 + 270*m.x2 - 6*m.x3*m.x3 + 460*m.x3 - 8*m.x4*m.x4 + 800*m.x4
                        - 12*m.x5*m.x5 + 740*m.x5 - 9*m.x6*m.x6 + 600*m.x6 - 14*m.x7*m.x7 + 540*m.x7 - 7*m.x8*m.x8 + 380
                       *m.x8 - 13*m.x9*m.x9 + 300*m.x9 - 12*m.x10*m.x10 + 490*m.x10 - 8*m.x11*m.x11 + 380*m.x11 - 4*
                       m.x12*m.x12 + 760*m.x12 - 7*m.x13*m.x13 + 430*m.x13 - 9*m.x14*m.x14 + 250*m.x14 - 16*m.x15*m.x15
                        + 390*m.x15 - 8*m.x16*m.x16 + 600*m.x16 - 4*m.x17*m.x17 + 210*m.x17 - 10*m.x18*m.x18 + 830*m.x18
                        - 21*m.x19*m.x19 + 470*m.x19 - 13*m.x20*m.x20 + 680*m.x20 - 17*m.x21*m.x21 + 360*m.x21 - 9*m.x22
                       *m.x22 + 290*m.x22 - 8*m.x23*m.x23 + 400*m.x23 - 4*m.x24*m.x24 + 310*m.x24, sense=minimize)

m.c2 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 == 8)

m.c3 = Constraint(expr=   m.x5 + m.x6 + m.x7 + m.x8 == 24)

m.c4 = Constraint(expr=   m.x9 + m.x10 + m.x11 + m.x12 == 20)

m.c5 = Constraint(expr=   m.x13 + m.x14 + m.x15 + m.x16 == 24)

m.c6 = Constraint(expr=   m.x17 + m.x18 + m.x19 + m.x20 == 16)

m.c7 = Constraint(expr=   m.x21 + m.x22 + m.x23 + m.x24 == 12)

m.c8 = Constraint(expr=   m.x1 + m.x5 + m.x9 + m.x13 + m.x17 + m.x21 == 29)

m.c9 = Constraint(expr=   m.x2 + m.x6 + m.x10 + m.x14 + m.x18 + m.x22 == 41)

m.c10 = Constraint(expr=   m.x3 + m.x7 + m.x11 + m.x15 + m.x19 + m.x23 == 13)

m.c11 = Constraint(expr=   m.x4 + m.x8 + m.x12 + m.x16 + m.x20 + m.x24 == 21)
