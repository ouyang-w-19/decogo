#  NLP written by GAMS Convert at 04/21/18 13:54:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         21        1        0       20        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         21       21        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        182      162       20        0
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

m.obj = Objective(expr=(-0.00055*m.x1**2) - 0.0583*m.x1 - 0.0019*m.x2**2 - 0.2318*m.x2 - 0.0002*m.x3**2 - 0.0108*m.x3 - 
                       0.00095*m.x4**2 - 0.1634*m.x4 - 0.0046*m.x5**2 - 0.138*m.x5 - 0.0035*m.x6**2 - 0.357*m.x6 - 
                       0.00315*m.x7**2 - 0.1953*m.x7 - 0.00475*m.x8**2 - 0.361*m.x8 - 0.0048*m.x9**2 - 0.1824*m.x9 - 
                       0.003*m.x10**2 - 0.162*m.x10 - 0.00265*m.x11**2 - 0.4346*m.x11 - 0.0017*m.x12**2 - 0.1054*m.x12
                        - 0.0012*m.x13**2 - 0.2376*m.x13 - 0.00295*m.x14**2 - 0.0059*m.x14 - 0.00315*m.x15**2 - 0.189*
                       m.x15 - 0.0021*m.x16**2 - 0.0252*m.x16 - 0.00225*m.x17**2 - 0.099*m.x17 - 0.0034*m.x18**2 - 
                       0.3604*m.x18 - 0.001*m.x19**2 - 0.022*m.x19 - 0.00305*m.x20**2 - 0.3294*m.x20, sense=minimize)

m.c1 = Constraint(expr=   8*m.x1 + 5*m.x6 + 4*m.x7 + 6*m.x12 + 6*m.x13 + 9*m.x14 + 5*m.x19 + m.x20 <= 220)

m.c2 = Constraint(expr=   3*m.x1 + 4*m.x2 + 3*m.x7 + 7*m.x8 + 4*m.x13 + 9*m.x14 + 3*m.x15 + 2*m.x20 <= 175)

m.c3 = Constraint(expr=   2*m.x2 + m.x3 + 6*m.x8 + 8*m.x9 + 9*m.x14 + 9*m.x15 + 8*m.x16 <= 215)

m.c4 = Constraint(expr=   7*m.x3 + m.x4 + 7*m.x9 + 9*m.x10 + 2*m.x15 + 4*m.x16 + 9*m.x17 <= 195)

m.c5 = Constraint(expr=   4*m.x4 + 4*m.x5 + m.x10 + 3*m.x11 + 7*m.x16 + 2*m.x17 + 8*m.x18 <= 145)

m.c6 = Constraint(expr=   9*m.x5 + 5*m.x6 + 5*m.x11 + 7*m.x12 + m.x17 + 4*m.x18 + 6*m.x19 <= 185)

m.c7 = Constraint(expr=   5*m.x1 + 5*m.x6 + 3*m.x7 + 8*m.x12 + 5*m.x13 + 9*m.x18 + 9*m.x19 + m.x20 <= 225)

m.c8 = Constraint(expr=   m.x1 + 9*m.x2 + 9*m.x7 + 3*m.x8 + 9*m.x13 + 7*m.x14 + 4*m.x19 + m.x20 <= 215)

m.c9 = Constraint(expr=   3*m.x1 + 6*m.x2 + 3*m.x3 + 4*m.x8 + 2*m.x9 + 6*m.x14 + 3*m.x15 + 8*m.x19 + m.x20 <= 175)

m.c10 = Constraint(expr=   m.x2 + 2*m.x3 + 8*m.x4 + 4*m.x9 + m.x10 + 9*m.x15 + 6*m.x16 <= 155)

m.c11 = Constraint(expr=   9*m.x3 + 3*m.x4 + 6*m.x5 + m.x10 + 6*m.x11 + 9*m.x16 + 8*m.x17 <= 210)

m.c12 = Constraint(expr=   6*m.x4 + 3*m.x5 + 3*m.x6 + 6*m.x11 + 3*m.x12 + 8*m.x17 + 9*m.x18 <= 190)

m.c13 = Constraint(expr=   9*m.x5 + 8*m.x6 + 2*m.x7 + 7*m.x12 + 8*m.x13 + 4*m.x18 + 3*m.x19 <= 205)

m.c14 = Constraint(expr=   4*m.x1 + 6*m.x6 + 9*m.x7 + m.x8 + 6*m.x13 + 9*m.x14 + 8*m.x19 + 6*m.x20 <= 245)

m.c15 = Constraint(expr=   7*m.x1 + 3*m.x2 + 7*m.x7 + 4*m.x8 + 2*m.x9 + m.x14 + 3*m.x15 + 5*m.x20 <= 160)

m.c16 = Constraint(expr=   7*m.x2 + 9*m.x3 + 7*m.x8 + 9*m.x9 + 5*m.x10 + 2*m.x15 + 6*m.x16 <= 225)

m.c17 = Constraint(expr=   6*m.x3 + 9*m.x4 + 8*m.x9 + 4*m.x10 + 2*m.x11 + 6*m.x16 + 4*m.x17 <= 195)

m.c18 = Constraint(expr=   5*m.x4 + 5*m.x5 + 7*m.x10 + 8*m.x11 + 9*m.x12 + 8*m.x17 + 6*m.x18 <= 240)

m.c19 = Constraint(expr=   7*m.x5 + 5*m.x6 + 6*m.x11 + 2*m.x12 + 8*m.x13 + 6*m.x18 + 9*m.x19 <= 215)

m.c20 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13
                         + m.x14 + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20 <= 200)
