#  NLP written by GAMS Convert at 04/21/18 13:54:02
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         23       22        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         34       34        0        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         77       55       22        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(3,3),initialize=3)
m.x2 = Var(within=Reals,bounds=(3,None),initialize=3)
m.x3 = Var(within=Reals,bounds=(3,None),initialize=3)
m.x4 = Var(within=Reals,bounds=(3,None),initialize=3)
m.x5 = Var(within=Reals,bounds=(3,None),initialize=3)
m.x6 = Var(within=Reals,bounds=(3,None),initialize=3)
m.x7 = Var(within=Reals,bounds=(3,None),initialize=3)
m.x8 = Var(within=Reals,bounds=(3,None),initialize=3)
m.x9 = Var(within=Reals,bounds=(3,None),initialize=3)
m.x10 = Var(within=Reals,bounds=(3,None),initialize=3)
m.x11 = Var(within=Reals,bounds=(3,None),initialize=3)
m.x12 = Var(within=Reals,bounds=(0.95,None),initialize=0.95)
m.x13 = Var(within=Reals,bounds=(0.95,None),initialize=0.95)
m.x14 = Var(within=Reals,bounds=(0.95,None),initialize=0.95)
m.x15 = Var(within=Reals,bounds=(0.95,None),initialize=0.95)
m.x16 = Var(within=Reals,bounds=(0.95,None),initialize=0.95)
m.x17 = Var(within=Reals,bounds=(0.95,None),initialize=0.95)
m.x18 = Var(within=Reals,bounds=(0.95,None),initialize=0.95)
m.x19 = Var(within=Reals,bounds=(0.95,None),initialize=0.95)
m.x20 = Var(within=Reals,bounds=(0.95,None),initialize=0.95)
m.x21 = Var(within=Reals,bounds=(0.95,None),initialize=0.95)
m.x22 = Var(within=Reals,bounds=(0.95,None),initialize=0.95)
m.x23 = Var(within=Reals,bounds=(0.05,0.05),initialize=0.05)
m.x24 = Var(within=Reals,bounds=(0.05,0.0575),initialize=0.05)
m.x25 = Var(within=Reals,bounds=(0.05,0.066125),initialize=0.05)
m.x26 = Var(within=Reals,bounds=(0.05,0.07604375),initialize=0.05)
m.x27 = Var(within=Reals,bounds=(0.05,0.0874503125),initialize=0.05)
m.x28 = Var(within=Reals,bounds=(0.05,0.100567859375),initialize=0.05)
m.x29 = Var(within=Reals,bounds=(0.05,0.11565303828125),initialize=0.05)
m.x30 = Var(within=Reals,bounds=(0.05,0.133000994023437),initialize=0.05)
m.x31 = Var(within=Reals,bounds=(0.05,0.152951143126953),initialize=0.05)
m.x32 = Var(within=Reals,bounds=(0.05,0.175893814595996),initialize=0.05)
m.x33 = Var(within=Reals,bounds=(0.05,0.202277886785395),initialize=0.05)

m.obj = Objective(expr=-(0.95*log(m.x12) + 0.9025*log(m.x13) + 0.857375*log(m.x14) + 0.81450625*log(m.x15) + 
                       0.7737809375*log(m.x16) + 0.735091890625*log(m.x17) + 0.69833729609375*log(m.x18) + 
                       0.663420431289062*log(m.x19) + 0.630249409724609*log(m.x20) + 0.598736939238379*log(m.x21) + 
                       11.3760018455292*log(m.x22)), sense=minimize)

m.c1 = Constraint(expr=0.759835685651593*m.x1**0.25 - m.x12 - m.x23 == 0)

m.c2 = Constraint(expr=0.77686866556676*m.x2**0.25 - m.x13 - m.x24 == 0)

m.c3 = Constraint(expr=0.794283468039448*m.x3**0.25 - m.x14 - m.x25 == 0)

m.c4 = Constraint(expr=0.812088652256959*m.x4**0.25 - m.x15 - m.x26 == 0)

m.c5 = Constraint(expr=0.830292969275008*m.x5**0.25 - m.x16 - m.x27 == 0)

m.c6 = Constraint(expr=0.848905366318769*m.x6**0.25 - m.x17 - m.x28 == 0)

m.c7 = Constraint(expr=0.867934991180342*m.x7**0.25 - m.x18 - m.x29 == 0)

m.c8 = Constraint(expr=0.88739119671479*m.x8**0.25 - m.x19 - m.x30 == 0)

m.c9 = Constraint(expr=0.907283545436972*m.x9**0.25 - m.x20 - m.x31 == 0)

m.c10 = Constraint(expr=0.92762181422141*m.x10**0.25 - m.x21 - m.x32 == 0)

m.c11 = Constraint(expr=0.948415999107521*m.x11**0.25 - m.x22 - m.x33 == 0)

m.c12 = Constraint(expr= - m.x1 + m.x2 - m.x23 == 0)

m.c13 = Constraint(expr= - m.x2 + m.x3 - m.x24 == 0)

m.c14 = Constraint(expr= - m.x3 + m.x4 - m.x25 == 0)

m.c15 = Constraint(expr= - m.x4 + m.x5 - m.x26 == 0)

m.c16 = Constraint(expr= - m.x5 + m.x6 - m.x27 == 0)

m.c17 = Constraint(expr= - m.x6 + m.x7 - m.x28 == 0)

m.c18 = Constraint(expr= - m.x7 + m.x8 - m.x29 == 0)

m.c19 = Constraint(expr= - m.x8 + m.x9 - m.x30 == 0)

m.c20 = Constraint(expr= - m.x9 + m.x10 - m.x31 == 0)

m.c21 = Constraint(expr= - m.x10 + m.x11 - m.x32 == 0)

m.c22 = Constraint(expr=   0.03*m.x11 - m.x33 <= 0)
