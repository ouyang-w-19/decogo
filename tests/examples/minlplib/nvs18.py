#  MINLP written by GAMS Convert at 04/21/18 13:52:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          7        1        6        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          7        1        0        6        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         43        1       42        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,200),initialize=1)
m.i2 = Var(within=Integers,bounds=(0,200),initialize=1)
m.i3 = Var(within=Integers,bounds=(0,200),initialize=1)
m.i4 = Var(within=Integers,bounds=(0,200),initialize=1)
m.i5 = Var(within=Integers,bounds=(0,200),initialize=1)
m.i6 = Var(within=Integers,bounds=(0,200),initialize=1)

m.obj = Objective(expr=7*m.i1**2 + 6*m.i2**2 + 0.2*m.i1 - 53.6*m.i2 + 8*m.i3**2 - 6*m.i3*m.i1 + 4*m.i3*m.i2 + 4.4*m.i3
                        + 6*m.i4**2 + 2*m.i4*m.i1 + 2*m.i4*m.i3 - 24.8*m.i4 + 7*m.i5**2 - 4*m.i5*m.i1 - 2*m.i5*m.i2 - 6*
                       m.i5*m.i3 - 104.8*m.i5 + 4*m.i6**2 + 2*m.i6*m.i1 - 4*m.i6*m.i2 - 4*m.i6*m.i3 - 2*m.i6*m.i4 + 6*
                       m.i6*m.i5 - 56.4*m.i6, sense=minimize)

m.c1 = Constraint(expr=(-9*m.i1**2) - 10*m.i1*m.i2 - 8*m.i2**2 - 5*m.i3**2 - 6*m.i3*m.i1 - 10*m.i3*m.i2 - 7*m.i4**2 - 10
                       *m.i4*m.i1 - 6*m.i4*m.i2 - 2*m.i4*m.i3 - 2*m.i5*m.i2 - 7*m.i5**2 - 6*m.i6*m.i1 - 2*m.i6*m.i2 - 2*
                       m.i6*m.i4 - 5*m.i6**2 >= -1800)

m.c2 = Constraint(expr=(-6*m.i1**2) - 8*m.i1*m.i2 - 6*m.i2**2 - 4*m.i3**2 - 2*m.i3*m.i1 - 2*m.i3*m.i2 - 8*m.i4**2 + 2*
                       m.i4*m.i1 + 10*m.i4*m.i2 - 2*m.i5*m.i1 - 6*m.i5*m.i2 + 6*m.i5*m.i4 + 7*m.i5**2 - 2*m.i6*m.i2 + 8*
                       m.i6*m.i3 + 2*m.i6*m.i4 - 4*m.i6*m.i5 - 8*m.i6**2 >= -1520)

m.c3 = Constraint(expr=(-9*m.i1**2) - 6*m.i2**2 - 8*m.i3**2 + 2*m.i2*m.i1 + 2*m.i3*m.i2 - 6*m.i4**2 + 4*m.i4*m.i1 + 4*
                       m.i4*m.i2 - 2*m.i4*m.i3 - 6*m.i5*m.i1 - 2*m.i5*m.i2 + 4*m.i5*m.i4 + 6*m.i5**2 + 2*m.i6*m.i1 + 4*
                       m.i6*m.i2 - 6*m.i6*m.i4 - 2*m.i6*m.i5 - 5*m.i6**2 >= -1000)

m.c4 = Constraint(expr=(-8*m.i1**2) - 4*m.i2**2 - 9*m.i3**2 - 7*m.i4**2 - 2*m.i2*m.i1 - 2*m.i3*m.i1 - 4*m.i3*m.i2 + 6*
                       m.i4*m.i1 + 2*m.i4*m.i2 - 2*m.i4*m.i3 - 6*m.i5*m.i1 - 4*m.i5*m.i2 - 2*m.i5*m.i3 + 6*m.i5*m.i4 + 6
                       *m.i5**2 - 10*m.i6*m.i1 - 10*m.i6*m.i3 + 4*m.i6*m.i4 - 2*m.i6*m.i5 - 7*m.i6**2 >= -1745)

m.c5 = Constraint(expr=2*m.i2*m.i1 - 4*m.i1**2 - 5*m.i2**2 - 6*m.i3*m.i1 - 8*m.i3**2 - 2*m.i4*m.i1 + 6*m.i4*m.i2 - 2*
                       m.i4*m.i3 - 6*m.i4**2 - 4*m.i5*m.i1 + 2*m.i5*m.i2 - 6*m.i5*m.i3 - 8*m.i5*m.i4 - 7*m.i5**2 + 4*
                       m.i6*m.i1 - 4*m.i6*m.i2 + 6*m.i6*m.i3 + 4*m.i6*m.i5 - 7*m.i6**2 >= -1070)

m.c6 = Constraint(expr=2*m.i2*m.i1 - 7*m.i1**2 - 7*m.i2**2 - 6*m.i3*m.i1 - 2*m.i3*m.i2 - 6*m.i3**2 - 2*m.i4*m.i1 + 2*
                       m.i4*m.i2 - 2*m.i4*m.i3 - 5*m.i4**2 - 2*m.i5*m.i1 - 4*m.i5*m.i3 + 2*m.i5*m.i4 - 5*m.i5**2 + 2*
                       m.i6*m.i1 - 4*m.i6*m.i2 + 4*m.i6*m.i3 + 2*m.i6*m.i4 + 6*m.i6*m.i5 - 9*m.i6**2 >= -990)
