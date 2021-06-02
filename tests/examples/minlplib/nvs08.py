#  MINLP written by GAMS Convert at 04/21/18 13:52:42
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          4        1        3        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          4        2        0        2        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         13        6        7        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,200),initialize=1)
m.i2 = Var(within=Integers,bounds=(0,200),initialize=1)
m.x3 = Var(within=Reals,bounds=(0.001,200),initialize=1)

m.obj = Objective(expr=(-3 + m.i1)**2 + (-2 + m.i2)**2 + (4 + m.x3)**2, sense=minimize)

m.c1 = Constraint(expr=sqrt(m.x3) + m.i1 + 2*m.i2 >= 10)

m.c2 = Constraint(expr=0.240038406144983*m.i1**2 - m.i2 + 0.255036980362153*m.x3 >= -3)

m.c3 = Constraint(expr=m.i2**2 - 1/(m.x3**3*sqrt(m.x3)) - 4*m.i1 >= -12)
