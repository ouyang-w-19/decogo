#  NLP written by GAMS Convert at 04/21/18 13:51:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          6        2        0        4        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          6        6        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         20        7       13        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x2 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x3 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x4 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x5 = Var(within=Reals,bounds=(-5,5),initialize=0)

m.obj = Objective(expr=(-1 + m.x1)**2 + (m.x1 - m.x2)**2 + (m.x2 - m.x3)**3 + (m.x3 - m.x4)**4 + (m.x4 - m.x5)**4
                       , sense=minimize)

m.c1 = Constraint(expr=m.x2**2 + m.x3**3 + m.x1 <= 6.24264068711929)

m.c2 = Constraint(expr=(-m.x3**3) - m.x2**2 - m.x1 <= -6.24264068711929)

m.c3 = Constraint(expr=-m.x3**2 + m.x2 + m.x4 <= 0.82842712474619)

m.c4 = Constraint(expr=m.x3**2 - m.x2 - m.x4 <= -0.82842712474619)

m.c5 = Constraint(expr=0.5*m.x1*m.x5 + 0.5*m.x1*m.x5 == 2)
