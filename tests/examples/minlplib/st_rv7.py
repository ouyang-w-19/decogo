#  NLP written by GAMS Convert at 04/21/18 13:54:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         21        1        0       20        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         31       31        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        271      241       30        0
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
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=(-0.00165*m.x1**2) - 0.1914*m.x1 - 0.0004*m.x2**2 - 0.0384*m.x2 - 0.00285*m.x3**2 - 0.3876*m.x3
                        - 0.00155*m.x4**2 - 0.1116*m.x4 - 0.0038*m.x5**2 - 0.4636*m.x5 - 0.0044*m.x6**2 - 0.044*m.x6 - 
                       0.0046*m.x7**2 - 0.3588*m.x7 - 0.00085*m.x8**2 - 0.0272*m.x8 - 0.00165*m.x9**2 - 0.231*m.x9 - 
                       0.0025*m.x10**2 - 0.27*m.x10 - 0.00385*m.x11**2 - 0.308*m.x11 - 0.00355*m.x12**2 - 0.3692*m.x12
                        - 0.0015*m.x13**2 - 0.288*m.x13 - 0.0037*m.x14**2 - 0.407*m.x14 - 0.00125*m.x15**2 - 0.1175*
                       m.x15 - 0.00095*m.x16**2 - 0.1045*m.x16 - 0.0048*m.x17**2 - 0.1632*m.x17 - 0.0015*m.x18**2 - 
                       0.135*m.x18 - 0.0048*m.x19**2 - 0.0864*m.x19 - 0.0007*m.x20**2 - 0.1176*m.x20 - 0.0043*m.x21**2
                        - 0.645*m.x21 - 0.0045*m.x22**2 - 0.882*m.x22 - 0.00245*m.x23**2 - 0.3283*m.x23 - 0.0004*m.x24**
                       2 - 0.0648*m.x24 - 0.0048*m.x25**2 - 0.0864*m.x25 - 0.00485*m.x26**2 - 0.4753*m.x26 - 0.00025*
                       m.x27**2 - 0.046*m.x27 - 0.00435*m.x28**2 - 0.7917*m.x28 - 0.00365*m.x29**2 - 0.7008*m.x29 - 
                       0.0002*m.x30**2 - 0.0384*m.x30, sense=minimize)

m.c1 = Constraint(expr=   4*m.x1 + 7*m.x6 + 4*m.x7 + 8*m.x12 + m.x13 + 3*m.x14 + 8*m.x19 + 6*m.x20 + m.x25 + 8*m.x26
                        <= 425)

m.c2 = Constraint(expr=   7*m.x1 + 3*m.x2 + 7*m.x7 + 9*m.x8 + 9*m.x13 + 2*m.x14 + 6*m.x15 + 5*m.x20 + 7*m.x21 + 5*m.x26
                        + 8*m.x27 <= 450)

m.c3 = Constraint(expr=   7*m.x2 + 9*m.x3 + 8*m.x8 + 4*m.x9 + 3*m.x14 + 6*m.x15 + 4*m.x16 + 6*m.x21 + 5*m.x22 + 3*m.x27
                        + 2*m.x28 <= 380)

m.c4 = Constraint(expr=   6*m.x3 + 9*m.x4 + 7*m.x9 + 8*m.x10 + 8*m.x15 + 8*m.x16 + 6*m.x17 + 5*m.x22 + 3*m.x23 + 2*m.x28
                        + m.x29 <= 415)

m.c5 = Constraint(expr=   5*m.x4 + 5*m.x5 + 6*m.x10 + 2*m.x11 + 9*m.x16 + 6*m.x17 + 9*m.x18 + 9*m.x23 + 3*m.x24
                        + 3*m.x29 + 4*m.x30 <= 360)

m.c6 = Constraint(expr=   7*m.x5 + 5*m.x6 + 6*m.x11 + 6*m.x12 + 8*m.x17 + 5*m.x18 + m.x19 + 9*m.x24 + 6*m.x25 + 4*m.x30
                        <= 365)

m.c7 = Constraint(expr=   4*m.x1 + 5*m.x6 + 4*m.x7 + 4*m.x12 + 9*m.x13 + 6*m.x18 + 2*m.x19 + 2*m.x20 + 2*m.x25 + m.x26
                        <= 300)

m.c8 = Constraint(expr=   2*m.x1 + m.x2 + 3*m.x7 + 7*m.x8 + 9*m.x13 + 9*m.x14 + m.x19 + 4*m.x20 + 6*m.x21 + 5*m.x26
                        + 5*m.x27 <= 370)

m.c9 = Constraint(expr=   9*m.x1 + 7*m.x2 + m.x3 + 6*m.x8 + 8*m.x9 + 2*m.x14 + 4*m.x15 + m.x20 + 4*m.x21 + 7*m.x22
                        + 2*m.x27 + 4*m.x28 <= 370)

m.c10 = Constraint(expr=   3*m.x2 + 4*m.x3 + 4*m.x4 + 7*m.x9 + 9*m.x10 + 7*m.x15 + 2*m.x16 + 3*m.x21 + 2*m.x22 + 2*m.x23
                         + m.x28 + 8*m.x29 <= 320)

m.c11 = Constraint(expr=   8*m.x3 + 9*m.x4 + 5*m.x5 + m.x10 + 3*m.x11 + m.x16 + 4*m.x17 + 7*m.x22 + 6*m.x23 + 4*m.x24
                         + 2*m.x29 + 6*m.x30 <= 330)

m.c12 = Constraint(expr=   6*m.x4 + 5*m.x5 + 3*m.x6 + 5*m.x11 + 7*m.x12 + 9*m.x17 + 9*m.x18 + 4*m.x23 + m.x24 + 6*m.x25
                         + 2*m.x30 <= 325)

m.c13 = Constraint(expr=   3*m.x5 + 9*m.x6 + 3*m.x7 + 8*m.x12 + 5*m.x13 + 4*m.x18 + m.x19 + 3*m.x24 + 6*m.x25 + 5*m.x26
                         <= 285)

m.c14 = Constraint(expr=   6*m.x1 + 2*m.x6 + 4*m.x7 + 2*m.x8 + 9*m.x13 + 7*m.x14 + 8*m.x19 + 2*m.x20 + 8*m.x25 + 8*m.x26
                         + 6*m.x27 <= 425)

m.c15 = Constraint(expr=   m.x1 + 2*m.x2 + m.x7 + 4*m.x8 + m.x9 + 6*m.x14 + 3*m.x15 + 7*m.x20 + 6*m.x21 + 5*m.x26
                         + 7*m.x27 + 3*m.x28 <= 335)

m.c16 = Constraint(expr=   9*m.x2 + 3*m.x3 + 2*m.x8 + m.x9 + 6*m.x10 + 9*m.x15 + 6*m.x16 + 7*m.x21 + 6*m.x22 + 7*m.x27
                         + 5*m.x28 + 5*m.x29 <= 415)

m.c17 = Constraint(expr=   6*m.x3 + 3*m.x4 + 5*m.x9 + 6*m.x10 + 3*m.x11 + 9*m.x16 + 8*m.x17 + 7*m.x22 + 4*m.x23
                         + 7*m.x28 + m.x29 + 6*m.x30 <= 390)

m.c18 = Constraint(expr=   9*m.x4 + 8*m.x5 + 2*m.x10 + 7*m.x11 + 8*m.x12 + 8*m.x17 + 9*m.x18 + 2*m.x23 + m.x24 + 7*m.x29
                         + 3*m.x30 <= 410)

m.c19 = Constraint(expr=   6*m.x5 + 9*m.x6 + 9*m.x11 + 6*m.x12 + 9*m.x13 + 4*m.x18 + 3*m.x19 + 3*m.x24 + m.x25 + 9*m.x30
                         <= 370)

m.c20 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13
                         + m.x14 + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20 + m.x21 + m.x22 + m.x23 + m.x24 + m.x25
                         + m.x26 + m.x27 + m.x28 + m.x29 + m.x30 <= 400)
