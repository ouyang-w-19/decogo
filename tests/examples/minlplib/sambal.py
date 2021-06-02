#  NLP written by GAMS Convert at 04/21/18 13:54:10
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         11       11        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         18       18        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         48       35       13        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,None),initialize=15)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=3)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=130)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=80)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=15)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=130)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=20)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=25)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=40)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=55)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=220)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(None,None),initialize=190)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=105)

m.obj = Objective(expr=0.0666666666666667*(15 - m.x1)**2 + 0.333333333333333*(3 - m.x2)**2 + 0.00769230769230769*(130 - 
                       m.x3)**2 + 0.0125*(80 - m.x4)**2 + 0.0666666666666667*(15 - m.x7)**2 + 0.00769230769230769*(130
                        - m.x8)**2 + 0.05*(20 - m.x9)**2 + 0.04*(25 - m.x10)**2 + 0.025*(40 - m.x11)**2 + 
                       0.0181818181818182*(55 - m.x12)**2 + 0.00454545454545455*(220 - m.x13)**2 + 0.00526315789473684*(
                       190 - m.x16)**2 + 0.00952380952380952*(105 - m.x17)**2, sense=minimize)

m.c1 = Constraint(expr= - m.x1 - m.x2 - m.x3 - m.x4 + m.x13 == 0)

m.c2 = Constraint(expr= - m.x5 + m.x14 == 0)

m.c3 = Constraint(expr= - m.x6 + m.x15 == 0)

m.c4 = Constraint(expr= - m.x7 - m.x8 - m.x9 + m.x16 == 0)

m.c5 = Constraint(expr= - m.x10 - m.x11 - m.x12 + m.x17 == 0)

m.c6 = Constraint(expr= - m.x5 - m.x6 + m.x13 == 0)

m.c7 = Constraint(expr= - m.x1 - m.x7 - m.x10 + m.x14 == 0)

m.c8 = Constraint(expr= - m.x2 - m.x8 - m.x11 + m.x15 == 0)

m.c9 = Constraint(expr= - m.x3 - m.x12 + m.x16 == 0)

m.c10 = Constraint(expr= - m.x4 - m.x9 + m.x17 == 0)
