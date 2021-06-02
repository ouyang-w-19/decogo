#  MINLP written by GAMS Convert at 04/21/18 13:54:54
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         13        1        0       12        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          9        1        2        6        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         33       25        8        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.i3 = Var(within=Integers,bounds=(0,15),initialize=1)
m.i4 = Var(within=Integers,bounds=(0,15),initialize=1)
m.i5 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i6 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i7 = Var(within=Integers,bounds=(0,5),initialize=1)
m.i8 = Var(within=Integers,bounds=(0,5),initialize=1)

m.obj = Objective(expr=   0.1*m.b1 + 0.2*m.b2 + m.i3 + m.i4, sense=minimize)

m.c2 = Constraint(expr=   460*m.i5 + 570*m.i7 <= 1900)

m.c3 = Constraint(expr=   460*m.i6 + 570*m.i8 <= 1900)

m.c4 = Constraint(expr= - 460*m.i5 - 570*m.i7 <= -1700)

m.c5 = Constraint(expr= - 460*m.i6 - 570*m.i8 <= -1700)

m.c6 = Constraint(expr=   m.i5 + m.i7 <= 5)

m.c7 = Constraint(expr=   m.i6 + m.i8 <= 5)

m.c8 = Constraint(expr=   m.b1 - m.i3 <= 0)

m.c9 = Constraint(expr=   m.b2 - m.i4 <= 0)

m.c10 = Constraint(expr= - 15*m.b1 + m.i3 <= 0)

m.c11 = Constraint(expr= - 15*m.b2 + m.i4 <= 0)

m.c12 = Constraint(expr=-(m.i3*m.i5 + m.i4*m.i6) <= -8)

m.c13 = Constraint(expr=-(m.i3*m.i7 + m.i4*m.i8) <= -7)
