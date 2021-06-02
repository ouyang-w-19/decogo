#  NLP written by GAMS Convert at 04/21/18 13:51:14
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         39       33        4        2        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         44       44        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        133       77       56        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,2000),initialize=200)
m.x2 = Var(within=Reals,bounds=(0,2000),initialize=200)
m.x3 = Var(within=Reals,bounds=(0,2000),initialize=200)
m.x4 = Var(within=Reals,bounds=(0,2000),initialize=200)
m.x5 = Var(within=Reals,bounds=(0,100),initialize=1.08002386572984)
m.x6 = Var(within=Reals,bounds=(0,100),initialize=1.25850763714561)
m.x7 = Var(within=Reals,bounds=(0,100),initialize=2.47224270643972)
m.x8 = Var(within=Reals,bounds=(0,100),initialize=2.08174548233022)
m.x9 = Var(within=Reals,bounds=(0,2000),initialize=250)
m.x10 = Var(within=Reals,bounds=(0,2000),initialize=250)
m.x11 = Var(within=Reals,bounds=(0,2000),initialize=250)
m.x12 = Var(within=Reals,bounds=(0,2000),initialize=250)
m.x13 = Var(within=Reals,bounds=(0.1,100),initialize=3)
m.x14 = Var(within=Reals,bounds=(0.1,100),initialize=3)
m.x15 = Var(within=Reals,bounds=(0.1,100),initialize=3)
m.x16 = Var(within=Reals,bounds=(0.1,100),initialize=3)
m.x17 = Var(within=Reals,bounds=(0,1),initialize=0.283078383128534)
m.x18 = Var(within=Reals,bounds=(0,1),initialize=0.383990781960791)
m.x19 = Var(within=Reals,bounds=(0,1),initialize=0.309951359679435)
m.x20 = Var(within=Reals,bounds=(0,1),initialize=0.580992426342466)
m.x21 = Var(within=Reals,bounds=(0,1),initialize=0.22769870931466)
m.x22 = Var(within=Reals,bounds=(0,1),initialize=0.249861958624235)
m.x23 = Var(within=Reals,bounds=(0,1),initialize=0.617797527645794)
m.x24 = Var(within=Reals,bounds=(0,1),initialize=0.428786587425074)
m.x25 = Var(within=Reals,bounds=(0,400),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,400),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,400),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,400),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,400),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,400),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,4),initialize=1)
m.x32 = Var(within=Reals,bounds=(0,4),initialize=1)
m.x33 = Var(within=Reals,bounds=(0,4),initialize=1)
m.x34 = Var(within=Reals,bounds=(0,4),initialize=1)
m.x35 = Var(within=Reals,bounds=(0,4),initialize=1.1)
m.x36 = Var(within=Reals,bounds=(0,4),initialize=1)
m.x37 = Var(within=Reals,bounds=(0.25,4),initialize=3.5)
m.x38 = Var(within=Reals,bounds=(0.25,4),initialize=3.5)
m.x39 = Var(within=Reals,bounds=(0.01,None),initialize=0.3)
m.x41 = Var(within=Reals,bounds=(0.001,None),initialize=0.171804999139287)
m.x42 = Var(within=Reals,bounds=(0.001,None),initialize=0.349221638418406)
m.x43 = Var(within=Reals,bounds=(0.001,None),initialize=15.7837604335036)
m.x44 = Var(within=Reals,bounds=(0.001,None),initialize=0.00311417990544524)

m.obj = Objective(expr= - m.x9 - m.x10 - m.x11 - m.x12, sense=minimize)

m.c2 = Constraint(expr=   m.x1 - m.x9 - m.x25 + m.x28 >= 0)

m.c3 = Constraint(expr= - 0.1*m.x1 + m.x2 - m.x10 - m.x26 + m.x29 >= 0)

m.c4 = Constraint(expr= - 0.2*m.x1 - 0.1*m.x2 + m.x3 - m.x11 - m.x27 + m.x30 >= 0)

m.c5 = Constraint(expr= - 0.2*m.x1 - 0.3*m.x2 - 0.1*m.x3 + m.x4 - m.x12 >= 0)

m.c6 = Constraint(expr=m.x31*m.x28 - m.x34*m.x25 + m.x32*m.x29 - m.x35*m.x26 + m.x33*m.x30 - m.x36*m.x27 <= 0)

m.c7 = Constraint(expr= - 0.005*m.x28 + m.x31 == 1)

m.c8 = Constraint(expr= - 0.0157*m.x29 + m.x32 == 1)

m.c9 = Constraint(expr= - 0.00178*m.x30 + m.x33 == 1)

m.c10 = Constraint(expr=   0.005*m.x25 + m.x34 == 1)

m.c11 = Constraint(expr=   0.001*m.x26 + m.x35 == 1.1)

m.c12 = Constraint(expr=   0.01*m.x27 + m.x36 == 1)

m.c13 = Constraint(expr=-100*(m.x39*m.x13)**(-0.674) + m.x9 == 0)

m.c14 = Constraint(expr=-230*(m.x39*m.x14)**(-0.246) + m.x10 == 0)

m.c15 = Constraint(expr=-220*(m.x39*m.x15)**(-0.587) + m.x11 == 0)

m.c16 = Constraint(expr=-450*(m.x39*m.x16)**(-0.352) + m.x12 == 0)

m.c17 = Constraint(expr=m.x17*m.x1 + m.x18*m.x2 + m.x19*m.x3 + m.x20*m.x4 <= 750)

m.c18 = Constraint(expr=m.x21*m.x1 + m.x22*m.x2 + m.x23*m.x3 + m.x24*m.x4 == 500)

m.c19 = Constraint(expr= - m.x5 + m.x13 - 0.1*m.x14 - 0.2*m.x15 - 0.2*m.x16 == 0)

m.c20 = Constraint(expr= - m.x6 + m.x14 - 0.1*m.x15 - 0.3*m.x16 == 0)

m.c21 = Constraint(expr= - m.x7 + m.x15 - 0.1*m.x16 == 0)

m.c22 = Constraint(expr= - m.x8 + m.x16 == 0)

m.c23 = Constraint(expr= - m.x37 + m.x38 == 0)

m.c24 = Constraint(expr=-(2.06748466257669*m.x38)**(-0.89) + m.x41 == 0)

m.c25 = Constraint(expr=-(1.25733634311512*m.x38)**(-0.71) + m.x42 == 0)

m.c26 = Constraint(expr=-(0.00908173562058528*m.x38)**(-0.8) + m.x43 == 0)

m.c27 = Constraint(expr=-(124.31328320802*m.x38)**(-0.95) + m.x44 == 0)

m.c28 = Constraint(expr=-(0.674 + 0.326/m.x41)**0.123595505617978 + 3.97*m.x17 == 0)

m.c29 = Constraint(expr=-(0.557 + 0.443/m.x42)**0.408450704225352 + 3.33*m.x18 == 0)

m.c30 = Constraint(expr=-(0.00900000000000001 + 0.991/m.x43)**0.25 + 1.67*m.x19 == 0)

m.c31 = Constraint(expr=-(0.99202 + 0.00798/m.x44)**0.0526315789473684 + 1.84*m.x20 == 0)

m.c32 = Constraint(expr=-(0.326 + 0.674*m.x41)**0.123595505617978 + 3.97*m.x21 == 0)

m.c33 = Constraint(expr=-(0.443 + 0.557*m.x42)**0.408450704225352 + 3.33*m.x22 == 0)

m.c34 = Constraint(expr=-(0.991 + 0.00900000000000001*m.x43)**0.25 + 1.67*m.x23 == 0)

m.c35 = Constraint(expr=-(0.00798 + 0.99202*m.x44)**0.0526315789473684 + 1.84*m.x24 == 0)

m.c36 = Constraint(expr=-m.x37*m.x21 + m.x5 - m.x17 == 0)

m.c37 = Constraint(expr=-m.x37*m.x22 + m.x6 - m.x18 == 0)

m.c38 = Constraint(expr=-m.x37*m.x23 + m.x7 - m.x19 == 0)

m.c39 = Constraint(expr=-m.x37*m.x24 + m.x8 - m.x20 == 0)
