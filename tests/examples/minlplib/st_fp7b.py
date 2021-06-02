#  NLP written by GAMS Convert at 04/21/18 13:54:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         11        1        0       10        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         21       21        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        185      165       20        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=(-0.5*m.x1**2) - 5*m.x1 - 0.5*m.x2**2 - 5*m.x2 - 0.5*m.x3**2 - 5*m.x3 - 0.5*m.x4**2 - 5*m.x4 - 
                       0.5*m.x5**2 - 5*m.x5 - 0.5*m.x6**2 - 5*m.x6 - 0.5*m.x7**2 - 5*m.x7 - 0.5*m.x8**2 - 5*m.x8 - 0.5*
                       m.x9**2 - 5*m.x9 - 0.5*m.x10**2 - 5*m.x10 - 0.5*m.x11**2 - 5*m.x11 - 0.5*m.x12**2 - 5*m.x12 - 0.5
                       *m.x13**2 - 5*m.x13 - 0.5*m.x14**2 - 5*m.x14 - 0.5*m.x15**2 - 5*m.x15 - 0.5*m.x16**2 - 5*m.x16 - 
                       0.5*m.x17**2 - 5*m.x17 - 0.5*m.x18**2 - 5*m.x18 - 0.5*m.x19**2 - 5*m.x19 - 0.5*m.x20**2 - 5*m.x20
                       , sense=minimize)

m.c1 = Constraint(expr= - 3*m.x1 + 7*m.x2 - 5*m.x4 + m.x5 + m.x6 + 2*m.x8 - m.x9 - m.x10 - 9*m.x11 + 3*m.x12 + 5*m.x13
                        + m.x16 + 7*m.x17 - 7*m.x18 - 4*m.x19 - 6*m.x20 <= -5)

m.c2 = Constraint(expr=   7*m.x1 - 5*m.x3 + m.x4 + m.x5 + 2*m.x7 - m.x8 - m.x9 - 9*m.x10 + 3*m.x11 + 5*m.x12 + m.x15
                        + 7*m.x16 - 7*m.x17 - 4*m.x18 - 6*m.x19 - 3*m.x20 <= 2)

m.c3 = Constraint(expr= - 5*m.x2 + m.x3 + m.x4 + 2*m.x6 - m.x7 - m.x8 - 9*m.x9 + 3*m.x10 + 5*m.x11 + m.x14 + 7*m.x15
                        - 7*m.x16 - 4*m.x17 - 6*m.x18 - 3*m.x19 + 7*m.x20 <= -1)

m.c4 = Constraint(expr= - 5*m.x1 + m.x2 + m.x3 + 2*m.x5 - m.x6 - m.x7 - 9*m.x8 + 3*m.x9 + 5*m.x10 + m.x13 + 7*m.x14
                        - 7*m.x15 - 4*m.x16 - 6*m.x17 - 3*m.x18 + 7*m.x19 <= -3)

m.c5 = Constraint(expr=   m.x1 + m.x2 + 2*m.x4 - m.x5 - m.x6 - 9*m.x7 + 3*m.x8 + 5*m.x9 + m.x12 + 7*m.x13 - 7*m.x14
                        - 4*m.x15 - 6*m.x16 - 3*m.x17 + 7*m.x18 - 5*m.x20 <= 5)

m.c6 = Constraint(expr=   m.x1 + 2*m.x3 - m.x4 - m.x5 - 9*m.x6 + 3*m.x7 + 5*m.x8 + m.x11 + 7*m.x12 - 7*m.x13 - 4*m.x14
                        - 6*m.x15 - 3*m.x16 + 7*m.x17 - 5*m.x19 + m.x20 <= 4)

m.c7 = Constraint(expr=   2*m.x2 - m.x3 - m.x4 - 9*m.x5 + 3*m.x6 + 5*m.x7 + m.x10 + 7*m.x11 - 7*m.x12 - 4*m.x13
                        - 6*m.x14 - 3*m.x15 + 7*m.x16 - 5*m.x18 + m.x19 + m.x20 <= -1)

m.c8 = Constraint(expr=   2*m.x1 - m.x2 - m.x3 - 9*m.x4 + 3*m.x5 + 5*m.x6 + m.x9 + 7*m.x10 - 7*m.x11 - 4*m.x12 - 6*m.x13
                        - 3*m.x14 + 7*m.x15 - 5*m.x17 + m.x18 + m.x19 <= 0)

m.c9 = Constraint(expr= - m.x1 - m.x2 - 9*m.x3 + 3*m.x4 + 5*m.x5 + m.x8 + 7*m.x9 - 7*m.x10 - 4*m.x11 - 6*m.x12 - 3*m.x13
                        + 7*m.x14 - 5*m.x16 + m.x17 + m.x18 + 2*m.x20 <= 9)

m.c10 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13
                         + m.x14 + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20 <= 40)
