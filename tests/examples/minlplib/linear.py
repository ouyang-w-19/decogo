#  DNLP written by GAMS Convert at 04/21/18 13:52:28
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         21       21        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         25       25        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        121      101       20        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x3 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x4 = Var(within=Reals,bounds=(-100,100),initialize=-92)
m.x5 = Var(within=Reals,bounds=(-100,100),initialize=-94)
m.x6 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x7 = Var(within=Reals,bounds=(-100,100),initialize=-94)
m.x8 = Var(within=Reals,bounds=(-100,100),initialize=-96)
m.x9 = Var(within=Reals,bounds=(-100,100),initialize=-83)
m.x10 = Var(within=Reals,bounds=(-100,100),initialize=-90)
m.x11 = Var(within=Reals,bounds=(-100,100),initialize=-93)
m.x12 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x13 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x14 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x15 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x16 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x17 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x18 = Var(within=Reals,bounds=(-100,100),initialize=-84)
m.x19 = Var(within=Reals,bounds=(-100,100),initialize=-83)
m.x20 = Var(within=Reals,bounds=(-100,100),initialize=-92)
m.x21 = Var(within=Reals,bounds=(-100,100),initialize=0)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=1)

m.obj = Objective(expr=abs(m.x2) + abs(m.x3) + abs(m.x4) + abs(m.x5) + abs(m.x6) + abs(m.x7) + abs(m.x8) + abs(m.x9) + 
                       abs(m.x10) + abs(m.x11) + abs(m.x12) + abs(m.x13) + abs(m.x14) + abs(m.x15) + abs(m.x16) + abs(
                       m.x17) + abs(m.x18) + abs(m.x19) + abs(m.x20) + abs(m.x21), sense=minimize)

m.c1 = Constraint(expr=   m.x2 + m.x22 + 85*m.x23 + 76*m.x24 + 44*m.x25 == 99)

m.c2 = Constraint(expr=   m.x3 + m.x22 + 82*m.x23 + 78*m.x24 + 42*m.x25 == 93)

m.c3 = Constraint(expr=   m.x4 + m.x22 + 75*m.x23 + 73*m.x24 + 42*m.x25 == 99)

m.c4 = Constraint(expr=   m.x5 + m.x22 + 74*m.x23 + 72*m.x24 + 44*m.x25 == 97)

m.c5 = Constraint(expr=   m.x6 + m.x22 + 76*m.x23 + 73*m.x24 + 43*m.x25 == 90)

m.c6 = Constraint(expr=   m.x7 + m.x22 + 74*m.x23 + 69*m.x24 + 46*m.x25 == 96)

m.c7 = Constraint(expr=   m.x8 + m.x22 + 73*m.x23 + 69*m.x24 + 46*m.x25 == 93)

m.c8 = Constraint(expr=   m.x9 + m.x22 + 96*m.x23 + 80*m.x24 + 36*m.x25 == 130)

m.c9 = Constraint(expr=   m.x10 + m.x22 + 93*m.x23 + 78*m.x24 + 36*m.x25 == 118)

m.c10 = Constraint(expr=   m.x11 + m.x22 + 70*m.x23 + 73*m.x24 + 37*m.x25 == 88)

m.c11 = Constraint(expr=   m.x12 + m.x22 + 82*m.x23 + 71*m.x24 + 46*m.x25 == 89)

m.c12 = Constraint(expr=   m.x13 + m.x22 + 80*m.x23 + 72*m.x24 + 45*m.x25 == 93)

m.c13 = Constraint(expr=   m.x14 + m.x22 + 77*m.x23 + 76*m.x24 + 42*m.x25 == 94)

m.c14 = Constraint(expr=   m.x15 + m.x22 + 67*m.x23 + 76*m.x24 + 50*m.x25 == 75)

m.c15 = Constraint(expr=   m.x16 + m.x22 + 82*m.x23 + 70*m.x24 + 48*m.x25 == 84)

m.c16 = Constraint(expr=   m.x17 + m.x22 + 76*m.x23 + 76*m.x24 + 41*m.x25 == 91)

m.c17 = Constraint(expr=   m.x18 + m.x22 + 74*m.x23 + 78*m.x24 + 31*m.x25 == 100)

m.c18 = Constraint(expr=   m.x19 + m.x22 + 71*m.x23 + 80*m.x24 + 29*m.x25 == 98)

m.c19 = Constraint(expr=   m.x20 + m.x22 + 70*m.x23 + 83*m.x24 + 39*m.x25 == 101)

m.c20 = Constraint(expr=   m.x21 + m.x22 + 64*m.x23 + 79*m.x24 + 38*m.x25 == 80)
