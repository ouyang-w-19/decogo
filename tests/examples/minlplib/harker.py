#  NLP written by GAMS Convert at 04/21/18 13:52:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          8        8        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         21       21        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         61       41       20        0
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
m.x15 = Var(within=Reals,bounds=(0,None),initialize=25)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=25)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=25)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=25)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=25)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=25)

m.obj = Objective(expr=-(19*m.x15 - 0.1*m.x15**2 - 0.5*m.x18**2 - m.x18 - 0.005*m.x16**2 + 27*m.x16 - 0.4*m.x19**2 - 2*
                       m.x19 - 0.15*m.x17**2 + 30*m.x17 - 0.3*m.x20**2 - 1.5*m.x20 - (0.166666666666667*m.x1**3 + m.x1
                        + 0.0666666666666667*m.x2**3 + 2*m.x2 + 0.1*m.x3**3 + 3*m.x3 + 0.133333333333333*m.x4**3 + m.x4
                        + 0.1*m.x5**3 + 2*m.x5 + 0.0333333333333333*m.x6**3 + m.x6 + 0.0333333333333333*m.x7**3 + m.x7
                        + 0.166666666666667*m.x8**3 + 3*m.x8 + 0.0666666666666667*m.x9**3 + 2*m.x9 + 0.333333333333333*
                       m.x10**3 + m.x10 + 0.0833333333333333*m.x11**3 + 2*m.x11 + 0.0666666666666667*m.x12**3 + 2*m.x12
                        + 0.3*m.x13**3 + m.x13 + 0.266666666666667*m.x14**3 + 3*m.x14)), sense=minimize)

m.c1 = Constraint(expr=   m.x15 + m.x16 + m.x17 - m.x18 - m.x19 - m.x20 == 0)

m.c2 = Constraint(expr= - m.x1 - m.x2 + m.x5 + m.x8 - m.x15 + m.x18 == 0)

m.c3 = Constraint(expr= - m.x3 + m.x11 - m.x16 + m.x19 == 0)

m.c4 = Constraint(expr= - m.x4 + m.x12 - m.x17 + m.x20 == 0)

m.c5 = Constraint(expr=   m.x1 - m.x5 - m.x6 - m.x7 + m.x9 + m.x13 == 0)

m.c6 = Constraint(expr=   m.x2 + m.x6 - m.x8 - m.x9 - m.x10 + m.x14 == 0)

m.c7 = Constraint(expr=   m.x3 + m.x4 + m.x7 + m.x10 - m.x11 - m.x12 - m.x13 - m.x14 == 0)
