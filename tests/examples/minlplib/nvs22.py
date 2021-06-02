#  MINLP written by GAMS Convert at 04/21/18 13:52:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         10        5        5        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          9        5        0        4        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         31        7       24        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(1,200),initialize=2)
m.i2 = Var(within=Integers,bounds=(1,200),initialize=2)
m.i3 = Var(within=Integers,bounds=(1,20),initialize=2)
m.i4 = Var(within=Integers,bounds=(1,20),initialize=2)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=1)

m.obj = Objective(expr=1.10471*m.i3**2*m.i4 + 0.04811*m.i1*m.i2*(14 + m.i4), sense=minimize)

m.c1 = Constraint(expr=-4243.28147100424/(m.i3*m.i4) + m.x5 == 0)

m.c2 = Constraint(expr=-sqrt(0.25*m.i4**2 + (0.5*m.i1 + 0.5*m.i3)**2) + m.x7 == 0)

m.c3 = Constraint(expr=-(59405.9405940594 + 2121.64073550212*m.i4)*m.x7/(m.i3*m.i4*(0.0833333333333333*m.i4**2 + (0.5*
                       m.i1 + 0.5*m.i3)**2)) + m.x6 == 0)

m.c4 = Constraint(expr=-0.5*m.i4/m.x7 + m.x8 == 0)

m.c5 = Constraint(expr=-sqrt(m.x5**2 + 2*m.x5*m.x6*m.x8 + m.x6**2) >= -13600)

m.c6 = Constraint(expr=-504000/(m.i1**2*m.i2) >= -30000)

m.c7 = Constraint(expr=   m.i2 - m.i3 >= 0)

m.c8 = Constraint(expr=0.0204744897959184*sqrt(10000000000000*m.i2**3*m.i1*m.i1*m.i2**3)*(1 - 0.0282346219657891*m.i1)
                        >= 6000)

m.c9 = Constraint(expr=-2.1952/(m.i1**3*m.i2) >= -0.25)
