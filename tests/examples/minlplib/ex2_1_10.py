#  NLP written by GAMS Convert at 04/21/18 13:51:44
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
#        221      201       20        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=4.348)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=62.609)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=0.5*(42*(52 + m.x11)**2 + 98*(3 + m.x12)**2 + 48*(-81 + m.x13)**2 + 91*(-30 + m.x14)**2 + 11*(85
                        + m.x15)**2 + 63*(-68 + m.x16)**2 + 61*(-27 + m.x17)**2 + 61*(81 + m.x18)**2 + 38*(-97 + m.x19)
                       **2 + 26*(73 + m.x20)**2) - 0.5*(63*(19 + m.x1)**2 + 15*(27 + m.x2)**2 + 44*(23 + m.x3)**2 + 91*(
                       53 + m.x4)**2 + 45*(42 + m.x5)**2 + 50*(-26 + m.x6)**2 + 89*(33 + m.x7)**2 + 58*(23 + m.x8)**2 + 
                       86*(-41 + m.x9)**2 + 82*(-19 + m.x10)**2), sense=minimize)

m.c2 = Constraint(expr=   3*m.x1 + 5*m.x2 + 5*m.x3 + 6*m.x4 + 4*m.x5 + 4*m.x6 + 5*m.x7 + 6*m.x8 + 4*m.x9 + 4*m.x10
                        + 8*m.x11 + 4*m.x12 + 2*m.x13 + m.x14 + m.x15 + m.x16 + 2*m.x17 + m.x18 + 7*m.x19 + 3*m.x20
                        <= 380)

m.c3 = Constraint(expr=   5*m.x1 + 4*m.x2 + 5*m.x3 + 4*m.x4 + m.x5 + 4*m.x6 + 4*m.x7 + 2*m.x8 + 5*m.x9 + 2*m.x10
                        + 3*m.x11 + 6*m.x12 + m.x13 + 7*m.x14 + 7*m.x15 + 5*m.x16 + 8*m.x17 + 7*m.x18 + 2*m.x19 + m.x20
                        <= 415)

m.c4 = Constraint(expr=   m.x1 + 5*m.x2 + 2*m.x3 + 4*m.x4 + 7*m.x5 + 3*m.x6 + m.x7 + 5*m.x8 + 7*m.x9 + 6*m.x10 + m.x11
                        + 7*m.x12 + 2*m.x13 + 4*m.x14 + 7*m.x15 + 5*m.x16 + 3*m.x17 + 4*m.x18 + m.x19 + 2*m.x20 <= 385)

m.c5 = Constraint(expr=   3*m.x1 + 2*m.x2 + 6*m.x3 + 3*m.x4 + 2*m.x5 + m.x6 + 6*m.x7 + m.x8 + 7*m.x9 + 3*m.x10 + 7*m.x11
                        + 7*m.x12 + 8*m.x13 + 2*m.x14 + 3*m.x15 + 4*m.x16 + 5*m.x17 + 8*m.x18 + m.x19 + 2*m.x20 <= 405)

m.c6 = Constraint(expr=   6*m.x1 + 6*m.x2 + 6*m.x3 + 4*m.x4 + 5*m.x5 + 2*m.x6 + 2*m.x7 + 4*m.x8 + 3*m.x9 + 2*m.x10
                        + 7*m.x11 + 5*m.x12 + 3*m.x13 + 6*m.x14 + 7*m.x15 + 5*m.x16 + 8*m.x17 + 4*m.x18 + 6*m.x19
                        + 3*m.x20 <= 470)

m.c7 = Constraint(expr=   5*m.x1 + 5*m.x2 + 2*m.x3 + m.x4 + 3*m.x5 + 5*m.x6 + 5*m.x7 + 7*m.x8 + 4*m.x9 + 3*m.x10
                        + 4*m.x11 + m.x12 + 7*m.x13 + 3*m.x14 + 8*m.x15 + 3*m.x16 + m.x17 + 6*m.x18 + 2*m.x19 + 8*m.x20
                        <= 415)

m.c8 = Constraint(expr=   3*m.x1 + 6*m.x2 + 6*m.x3 + 3*m.x4 + m.x5 + 6*m.x6 + m.x7 + 6*m.x8 + 7*m.x9 + m.x10 + 4*m.x11
                        + 3*m.x12 + m.x13 + 4*m.x14 + 3*m.x15 + 6*m.x16 + 4*m.x17 + 6*m.x18 + 5*m.x19 + 4*m.x20 <= 400)

m.c9 = Constraint(expr=   m.x1 + 2*m.x2 + m.x3 + 7*m.x4 + 8*m.x5 + 7*m.x6 + 6*m.x7 + 5*m.x8 + 8*m.x9 + 7*m.x10 + 2*m.x11
                        + 3*m.x12 + 5*m.x13 + 5*m.x14 + 4*m.x15 + 5*m.x16 + 4*m.x17 + 2*m.x18 + 2*m.x19 + 8*m.x20
                        <= 460)

m.c10 = Constraint(expr=   8*m.x1 + 5*m.x2 + 2*m.x3 + 5*m.x4 + 3*m.x5 + 8*m.x6 + m.x7 + 3*m.x8 + 3*m.x9 + 5*m.x10
                         + 4*m.x11 + 5*m.x12 + 5*m.x13 + 6*m.x14 + m.x15 + 7*m.x16 + m.x17 + 2*m.x18 + 2*m.x19 + 4*m.x20
                         <= 400)

m.c11 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13
                         + m.x14 + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20 <= 200)
