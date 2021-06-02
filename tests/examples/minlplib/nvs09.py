#  MINLP written by GAMS Convert at 04/21/18 13:52:42
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        1        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         11        1        0       10        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         11        1       10        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(3,9),initialize=5)
m.i2 = Var(within=Integers,bounds=(3,9),initialize=5)
m.i3 = Var(within=Integers,bounds=(3,9),initialize=5)
m.i4 = Var(within=Integers,bounds=(3,9),initialize=5)
m.i5 = Var(within=Integers,bounds=(3,9),initialize=5)
m.i6 = Var(within=Integers,bounds=(3,9),initialize=5)
m.i7 = Var(within=Integers,bounds=(3,9),initialize=5)
m.i8 = Var(within=Integers,bounds=(3,9),initialize=5)
m.i9 = Var(within=Integers,bounds=(3,9),initialize=5)
m.i10 = Var(within=Integers,bounds=(3,9),initialize=5)

m.obj = Objective(expr=log((-2) + m.i1)**2 + log(10 - m.i1)**2 + log((-2) + m.i2)**2 + log(10 - m.i2)**2 + log((-2) + 
                       m.i3)**2 + log(10 - m.i3)**2 + log((-2) + m.i4)**2 + log(10 - m.i4)**2 + log((-2) + m.i5)**2 + 
                       log(10 - m.i5)**2 + log((-2) + m.i6)**2 + log(10 - m.i6)**2 + log((-2) + m.i7)**2 + log(10 - m.i7
                       )**2 + log((-2) + m.i8)**2 + log(10 - m.i8)**2 + log((-2) + m.i9)**2 + log(10 - m.i9)**2 + log((-
                       2) + m.i10)**2 + log(10 - m.i10)**2 - (m.i1*m.i2*m.i3*m.i4*m.i5*m.i6*m.i7*m.i8*m.i9*m.i10)**0.2
                       , sense=minimize)
