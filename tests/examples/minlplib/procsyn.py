#  NLP written by GAMS Convert at 04/21/18 13:54:00
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         28        1       18        9        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         21       21        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         93       64       29        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,10),initialize=0.1)
m.x4 = Var(within=Reals,bounds=(0,10),initialize=0.1)
m.x5 = Var(within=Reals,bounds=(0,10),initialize=0.1)
m.x6 = Var(within=Reals,bounds=(0,10),initialize=0.1)
m.x7 = Var(within=Reals,bounds=(0,10),initialize=0.1)
m.x8 = Var(within=Reals,bounds=(0,10),initialize=0.1)
m.x9 = Var(within=Reals,bounds=(0,10),initialize=0.1)
m.x10 = Var(within=Reals,bounds=(0,10),initialize=0.1)
m.x11 = Var(within=Reals,bounds=(0,10),initialize=0.1)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=0.05*(m.x1**2 + m.x2**3) + 0.175*(m.x1**2 + m.x2**3) + 0.025*(m.x1**2 + m.x2**3) + 0.1*(m.x1**2
                        + m.x2**3) + 0.35*(m.x1**2 + m.x2**3) + 0.05*(m.x1**2 + m.x2**3) + 0.05*(m.x1**2 + m.x2**3) + 
                       0.175*(m.x1**2 + m.x2**3) + 0.025*(m.x1**2 + m.x2**3) + 0.15*m.x3 + 0.525*m.x4 + 0.075*m.x5
                        + 0.3*m.x6 + 1.05*m.x7 + 0.15*m.x8 + 0.15*m.x9 + 0.525*m.x10 + 0.075*m.x11 + 0.1*m.x12
                        + 0.35*m.x13 + 0.05*m.x14 + 0.2*m.x15 + 0.7*m.x16 + 0.1*m.x17 + 0.1*m.x18 + 0.35*m.x19
                        + 0.05*m.x20 - 3.2, sense=minimize)

m.c2 = Constraint(expr=   m.x1 - 2*m.x3 - 2*m.x12 >= -1)

m.c3 = Constraint(expr=   m.x1 - 2*m.x4 - 2*m.x13 >= -1)

m.c4 = Constraint(expr=   m.x1 - 2*m.x5 - 2*m.x14 >= -1)

m.c5 = Constraint(expr=   m.x1 - 2*m.x6 - 2*m.x15 >= -3)

m.c6 = Constraint(expr=   m.x1 - 2*m.x7 - 2*m.x16 >= -3)

m.c7 = Constraint(expr=   m.x1 - 2*m.x8 - 2*m.x17 >= -3)

m.c8 = Constraint(expr=   m.x1 - 2*m.x9 - 2*m.x18 >= -5)

m.c9 = Constraint(expr=   m.x1 - 2*m.x10 - 2*m.x19 >= -5)

m.c10 = Constraint(expr=   m.x1 - 2*m.x11 - 2*m.x20 >= -5)

m.c11 = Constraint(expr=-(1/m.x3 + m.x12**2) + m.x2 >= 2.5)

m.c12 = Constraint(expr=-(1/m.x4 + m.x13**2) + m.x2 >= 6.5)

m.c13 = Constraint(expr=-(1/m.x5 + m.x14**2) + m.x2 >= 10.5)

m.c14 = Constraint(expr=-(1/m.x6 + m.x15**2) + m.x2 >= 3.5)

m.c15 = Constraint(expr=-(1/m.x7 + m.x16**2) + m.x2 >= 7.5)

m.c16 = Constraint(expr=-(1/m.x8 + m.x17**2) + m.x2 >= 11.5)

m.c17 = Constraint(expr=-(1/m.x9 + m.x18**2) + m.x2 >= 4.5)

m.c18 = Constraint(expr=-(1/m.x10 + m.x19**2) + m.x2 >= 8.5)

m.c19 = Constraint(expr=-(1/m.x11 + m.x20**2) + m.x2 >= 12.5)

m.c20 = Constraint(expr=m.x3**2 + 2*m.x12 <= 30)

m.c21 = Constraint(expr=m.x4**2 + 2*m.x13 <= 30)

m.c22 = Constraint(expr=m.x5**2 + 2*m.x14 <= 30)

m.c23 = Constraint(expr=m.x6**2 + 2*m.x15 <= 30)

m.c24 = Constraint(expr=m.x7**2 + 2*m.x16 <= 30)

m.c25 = Constraint(expr=m.x8**2 + 2*m.x17 <= 30)

m.c26 = Constraint(expr=m.x9**2 + 2*m.x18 <= 30)

m.c27 = Constraint(expr=m.x10**2 + 2*m.x19 <= 30)

m.c28 = Constraint(expr=m.x11**2 + 2*m.x20 <= 30)
