#  MINLP written by GAMS Convert at 04/21/18 13:55:19
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         14       14        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         15       12        0        3        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         38       14       24        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(1,10),initialize=1)
m.i2 = Var(within=Integers,bounds=(1,100),initialize=15)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=1)
m.i5 = Var(within=Integers,bounds=(1,100),initialize=2)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0.8,None),initialize=0.8)

m.obj = Objective(expr=m.x13*m.x13 + m.x14*m.x14, sense=minimize)

m.c1 = Constraint(expr= - 12*m.i1 + m.i2 == 0)

m.c2 = Constraint(expr=-12.566370616/m.i2 + m.x3 == 0)

m.c3 = Constraint(expr= - 0.25*m.i2 + m.x4 == 0)

m.c4 = Constraint(expr= - m.x4 + m.i5 == -1)

m.c5 = Constraint(expr=sin(0.5*m.x3)*m.i1*m.x6 - sin(0.5*m.i1*m.x3) == 0)

m.c6 = Constraint(expr=-sin(1.570796327*m.i5/m.x4) + m.x9 == 0)

m.c7 = Constraint(expr=-m.x9*m.x6 + m.x15 == 0)

m.c8 = Constraint(expr=sin(1.5*m.x3)*m.i1*m.x7 - sin(1.5*m.i1*m.x3) == 0)

m.c9 = Constraint(expr=-sin(4.712388981*m.i5/m.x4) + m.x10 == 0)

m.c10 = Constraint(expr=-m.x10*m.x7 + m.x13 == 0)

m.c11 = Constraint(expr=sin(2.5*m.x3)*m.i1*m.x8 - sin(2.5*m.i1*m.x3) == 0)

m.c12 = Constraint(expr=-sin(7.853981635*m.i5/m.x4) + m.x11 == 0)

m.c13 = Constraint(expr=-m.x11*m.x8 + m.x14 == 0)
