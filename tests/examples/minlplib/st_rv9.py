#  NLP written by GAMS Convert at 04/21/18 13:54:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         21        1        0       20        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         51       51        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        451      401       50        0
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
m.x31 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=(-0.00135*m.x1**2) - 0.0027*m.x1 - 0.0008*m.x2**2 - 0.0496*m.x2 - 0.00135*m.x3**2 - 0.0081*m.x3
                        - 0.0007*m.x4**2 - 0.0686*m.x4 - 0.0024*m.x5**2 - 0.0912*m.x5 - 0.00445*m.x6**2 - 0.6764*m.x6 - 
                       0.00165*m.x7**2 - 0.1914*m.x7 - 0.0004*m.x8**2 - 0.0384*m.x8 - 0.00285*m.x9**2 - 0.3876*m.x9 - 
                       0.00155*m.x10**2 - 0.1116*m.x10 - 0.0038*m.x11**2 - 0.4636*m.x11 - 0.0044*m.x12**2 - 0.044*m.x12
                        - 0.0046*m.x13**2 - 0.3588*m.x13 - 0.00085*m.x14**2 - 0.0272*m.x14 - 0.00165*m.x15**2 - 0.231*
                       m.x15 - 0.0025*m.x16**2 - 0.27*m.x16 - 0.00385*m.x17**2 - 0.308*m.x17 - 0.00355*m.x18**2 - 0.3692
                       *m.x18 - 0.0015*m.x19**2 - 0.288*m.x19 - 0.0037*m.x20**2 - 0.407*m.x20 - 0.00125*m.x21**2 - 
                       0.1175*m.x21 - 0.00095*m.x22**2 - 0.1045*m.x22 - 0.0048*m.x23**2 - 0.1632*m.x23 - 0.0015*m.x24**2
                        - 0.135*m.x24 - 0.0048*m.x25**2 - 0.0864*m.x25 - 0.0007*m.x26**2 - 0.1176*m.x26 - 0.0043*m.x27**
                       2 - 0.645*m.x27 - 0.0045*m.x28**2 - 0.882*m.x28 - 0.00245*m.x29**2 - 0.3283*m.x29 - 0.0004*m.x30
                       **2 - 0.0648*m.x30 - 0.0048*m.x31**2 - 0.0864*m.x31 - 0.00485*m.x32**2 - 0.4753*m.x32 - 0.00025*
                       m.x33**2 - 0.046*m.x33 - 0.00435*m.x34**2 - 0.7917*m.x34 - 0.00365*m.x35**2 - 0.7008*m.x35 - 
                       0.0002*m.x36**2 - 0.0384*m.x36 - 0.00205*m.x37**2 - 0.0164*m.x37 - 0.00165*m.x38**2 - 0.0891*
                       m.x38 - 0.00175*m.x39**2 - 0.0945*m.x39 - 0.0048*m.x40**2 - 0.7296*m.x40 - 0.00095*m.x41**2 - 
                       0.1045*m.x41 - 0.0048*m.x42**2 - 0.1632*m.x42 - 0.0015*m.x43**2 - 0.135*m.x43 - 0.0048*m.x44**2
                        - 0.0864*m.x44 - 0.0007*m.x45**2 - 0.1176*m.x45 - 0.0043*m.x46**2 - 0.645*m.x46 - 0.0045*m.x47**
                       2 - 0.882*m.x47 - 0.00245*m.x48**2 - 0.3283*m.x48 - 0.0004*m.x49**2 - 0.0648*m.x49 - 0.0048*m.x50
                       **2 - 0.0864*m.x50, sense=minimize)

m.c1 = Constraint(expr=   6*m.x1 + 5*m.x6 + 7*m.x7 + 2*m.x12 + 8*m.x13 + m.x14 + 9*m.x19 + 8*m.x20 + 6*m.x25 + m.x26
                        + 4*m.x31 + 9*m.x32 + 7*m.x33 + 4*m.x38 + 6*m.x39 + 6*m.x44 + m.x45 + 4*m.x50 <= 415)

m.c2 = Constraint(expr=   8*m.x1 + 7*m.x2 + 4*m.x7 + 7*m.x8 + 6*m.x13 + 9*m.x14 + 2*m.x15 + m.x20 + 5*m.x21 + m.x26
                        + 5*m.x27 + 3*m.x32 + 9*m.x33 + 5*m.x34 + m.x39 + m.x40 + m.x45 + 5*m.x46 <= 370)

m.c3 = Constraint(expr=   4*m.x2 + 7*m.x3 + 7*m.x8 + 8*m.x9 + 9*m.x14 + 3*m.x15 + 6*m.x16 + 2*m.x21 + 6*m.x22 + 5*m.x27
                        + 3*m.x28 + 4*m.x33 + 6*m.x34 + 6*m.x35 + 6*m.x40 + 6*m.x41 + 5*m.x46 + 3*m.x47 <= 410)

m.c4 = Constraint(expr=   m.x3 + 6*m.x4 + 8*m.x9 + 7*m.x10 + 9*m.x15 + 8*m.x16 + 8*m.x17 + 6*m.x22 + 5*m.x23 + 4*m.x28
                        + 2*m.x29 + 4*m.x34 + 7*m.x35 + 9*m.x36 + 6*m.x41 + 5*m.x42 + 4*m.x47 + 2*m.x48 <= 420)

m.c5 = Constraint(expr=   m.x4 + 5*m.x5 + 9*m.x10 + 6*m.x11 + 4*m.x16 + 9*m.x17 + 6*m.x18 + 7*m.x23 + 9*m.x24 + 8*m.x29
                        + 3*m.x30 + 7*m.x35 + 4*m.x36 + 3*m.x37 + 7*m.x42 + 9*m.x43 + 8*m.x48 + 3*m.x49 <= 405)

m.c6 = Constraint(expr=   4*m.x5 + 7*m.x6 + 3*m.x11 + 6*m.x12 + 2*m.x17 + 8*m.x18 + 5*m.x19 + 2*m.x24 + 9*m.x25
                        + 6*m.x30 + 4*m.x31 + 3*m.x36 + 6*m.x37 + 6*m.x38 + 2*m.x43 + 9*m.x44 + 6*m.x49 + 4*m.x50
                        <= 355)

m.c7 = Constraint(expr=   3*m.x1 + 5*m.x6 + 5*m.x7 + 7*m.x12 + 4*m.x13 + 4*m.x18 + 6*m.x19 + 2*m.x20 + 4*m.x25 + 2*m.x26
                        + m.x31 + 4*m.x32 + 4*m.x37 + 3*m.x38 + 4*m.x39 + 4*m.x44 + 2*m.x45 + m.x50 <= 290)

m.c8 = Constraint(expr=   5*m.x1 + 2*m.x2 + 3*m.x7 + 3*m.x8 + 5*m.x13 + 9*m.x14 + 9*m.x19 + m.x20 + 4*m.x21 + 6*m.x26
                        + 5*m.x27 + 3*m.x32 + 7*m.x33 + 3*m.x38 + 5*m.x39 + 4*m.x40 + 6*m.x45 + 5*m.x46 <= 370)

m.c9 = Constraint(expr=   m.x1 + 9*m.x2 + 7*m.x3 + 3*m.x8 + 6*m.x9 + 7*m.x14 + 2*m.x15 + m.x20 + m.x21 + 4*m.x22
                        + 5*m.x27 + 2*m.x28 + 6*m.x33 + 5*m.x34 + 4*m.x39 + 4*m.x40 + 4*m.x41 + 5*m.x46 + 2*m.x47
                        <= 335)

m.c10 = Constraint(expr=   6*m.x2 + 3*m.x3 + 4*m.x4 + 2*m.x9 + 7*m.x10 + 3*m.x15 + 7*m.x16 + 2*m.x21 + 3*m.x22 + 2*m.x23
                         + 6*m.x28 + m.x29 + 6*m.x34 + 7*m.x35 + 9*m.x40 + 3*m.x41 + 2*m.x42 + 6*m.x47 + m.x48 <= 340)

m.c11 = Constraint(expr=   2*m.x3 + 8*m.x4 + 9*m.x5 + m.x10 + m.x11 + 6*m.x16 + m.x17 + 6*m.x22 + 7*m.x23 + 6*m.x24
                         + 3*m.x29 + 2*m.x30 + 7*m.x35 + 6*m.x36 + 6*m.x41 + 7*m.x42 + 6*m.x43 + 3*m.x48 + 2*m.x49
                         <= 325)

m.c12 = Constraint(expr=   3*m.x4 + 6*m.x5 + 5*m.x6 + 6*m.x11 + 5*m.x12 + 8*m.x17 + 9*m.x18 + 6*m.x23 + 4*m.x24 + m.x25
                         + 5*m.x30 + 2*m.x31 + 5*m.x36 + 4*m.x37 + 6*m.x42 + 4*m.x43 + m.x44 + 5*m.x49 + 2*m.x50 <= 345)

m.c13 = Constraint(expr=   3*m.x5 + 3*m.x6 + 9*m.x7 + 3*m.x12 + 8*m.x13 + 9*m.x18 + 4*m.x19 + 4*m.x24 + 3*m.x25
                         + 6*m.x26 + 6*m.x31 + m.x32 + 6*m.x37 + 2*m.x38 + 4*m.x43 + 3*m.x44 + 6*m.x45 + 6*m.x50 <= 335)

m.c14 = Constraint(expr=   3*m.x1 + 8*m.x6 + 2*m.x7 + 4*m.x8 + 8*m.x13 + 9*m.x14 + 3*m.x19 + 8*m.x20 + m.x25 + 8*m.x26
                         + 8*m.x27 + 3*m.x32 + m.x33 + 5*m.x38 + 7*m.x39 + m.x44 + 8*m.x45 + 8*m.x46 <= 390)

m.c15 = Constraint(expr=   4*m.x1 + m.x2 + 9*m.x7 + m.x8 + 4*m.x9 + 9*m.x14 + 6*m.x15 + 6*m.x20 + 7*m.x21 + m.x26
                         + 5*m.x27 + 7*m.x28 + m.x33 + 8*m.x34 + 9*m.x39 + 2*m.x40 + m.x45 + 5*m.x46 + 7*m.x47 <= 400)

m.c16 = Constraint(expr=   3*m.x2 + 9*m.x3 + 4*m.x8 + 2*m.x9 + m.x10 + 3*m.x15 + 9*m.x16 + 7*m.x21 + 7*m.x22 + 8*m.x27
                         + 7*m.x28 + 5*m.x29 + 4*m.x34 + m.x35 + 6*m.x40 + 7*m.x41 + 8*m.x46 + 7*m.x47 + 5*m.x48 <= 380)

m.c17 = Constraint(expr=   9*m.x3 + 6*m.x4 + 9*m.x9 + 5*m.x10 + 6*m.x11 + 6*m.x16 + 9*m.x17 + 5*m.x22 + 7*m.x23
                         + 8*m.x28 + 7*m.x29 + m.x30 + m.x35 + 8*m.x36 + 5*m.x41 + 7*m.x42 + 8*m.x47 + 7*m.x48 + m.x49
                         <= 435)

m.c18 = Constraint(expr=   9*m.x4 + 9*m.x5 + 4*m.x10 + 2*m.x11 + 7*m.x12 + 4*m.x17 + 8*m.x18 + 3*m.x23 + 2*m.x24
                         + 2*m.x29 + 7*m.x30 + 3*m.x31 + 4*m.x36 + 9*m.x37 + 3*m.x42 + 2*m.x43 + 2*m.x48 + 7*m.x49
                         + 3*m.x50 <= 365)

m.c19 = Constraint(expr=   5*m.x5 + 6*m.x6 + 8*m.x11 + 9*m.x12 + 6*m.x13 + 6*m.x18 + 4*m.x19 + 3*m.x24 + 3*m.x25 + m.x30
                         + 9*m.x31 + 2*m.x32 + 4*m.x37 + 7*m.x38 + 3*m.x43 + 3*m.x44 + m.x49 + 9*m.x50 <= 365)

m.c20 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13
                         + m.x14 + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20 + m.x21 + m.x22 + m.x23 + m.x24 + m.x25
                         + m.x26 + m.x27 + m.x28 + m.x29 + m.x30 + m.x31 + m.x32 + m.x33 + m.x34 + m.x35 + m.x36 + m.x37
                         + m.x38 + m.x39 + m.x40 + m.x41 + m.x42 + m.x43 + m.x44 + m.x45 + m.x46 + m.x47 + m.x48 + m.x49
                         + m.x50 <= 400)
