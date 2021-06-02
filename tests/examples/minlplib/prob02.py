#  MINLP written by GAMS Convert at 04/21/18 13:54:00
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          9        1        1        7        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          7        1        0        6        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         32       22       10        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(1,100),initialize=15)
m.i2 = Var(within=Integers,bounds=(1,100),initialize=4)
m.i3 = Var(within=Integers,bounds=(1,100),initialize=2)
m.i4 = Var(within=Integers,bounds=(1,100),initialize=5)
m.i5 = Var(within=Integers,bounds=(1,100),initialize=2)
m.i6 = Var(within=Integers,bounds=(1,100),initialize=7)

m.obj = Objective(expr=   8000*m.i1 - 330*m.i2 - 360*m.i3 - 370*m.i4 - 415*m.i5 - 435*m.i6, sense=minimize)

m.c2 = Constraint(expr=   330*m.i2 + 360*m.i3 + 370*m.i4 + 415*m.i5 + 435*m.i6 <= 8000)

m.c3 = Constraint(expr=   330*m.i2 + 360*m.i3 + 370*m.i4 + 415*m.i5 + 435*m.i6 >= 7700)

m.c4 = Constraint(expr=   m.i2 + m.i3 + m.i4 + m.i5 + m.i6 <= 20)

m.c5 = Constraint(expr=-m.i1*m.i2 <= -60)

m.c6 = Constraint(expr=-m.i1*m.i3 <= -30)

m.c7 = Constraint(expr=-m.i1*m.i4 <= -75)

m.c8 = Constraint(expr=-m.i1*m.i5 <= -30)

m.c9 = Constraint(expr=-m.i1*m.i6 <= -100)
