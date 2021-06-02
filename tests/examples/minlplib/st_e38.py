#  MINLP written by GAMS Convert at 04/21/18 13:54:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          4        1        1        2        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        3        0        2        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         11        5        6        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(18,100),initialize=18)
m.i2 = Var(within=Integers,bounds=(10,100),initialize=10)
m.x3 = Var(within=Reals,bounds=(40,80),initialize=40)
m.x4 = Var(within=Reals,bounds=(20,60),initialize=20)

m.obj = Objective(expr=0.0389*m.i1*m.x3*m.x4 + 0.1111312*m.x3**2*m.i2 + 0.012348046875*m.i1**2*m.x4 + 0.0775*m.i1**2*
                       m.x3, sense=minimize)

m.c1 = Constraint(expr= - 0.0625*m.i1 + 0.0193*m.x3 <= 0)

m.c2 = Constraint(expr= - 0.0625*m.i2 + 0.00954*m.x3 <= 0)

m.c3 = Constraint(expr=3.1415927*(m.x3**2*m.x4 + 1.33333333333333*m.x3**3) >= 1296000)
