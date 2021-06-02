#  NLP written by GAMS Convert at 04/21/18 13:54:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          2        1        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        5        0        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          7        3        4        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x4 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x5 = Var(within=Reals,bounds=(1,1),initialize=1)

m.obj = Objective(expr=(-1.9837 + m.x4 + m.x5)**2 + (-0.8393 + exp(-m.x1)*m.x4 + exp(-m.x2)*m.x5)**2 + (-0.4305 + exp(-2
                       *m.x1)*m.x4 + exp(-2*m.x2)*m.x5)**2 + (-0.2441 + exp(-3*m.x1)*m.x4 + exp(-3*m.x2)*m.x5)**2 + (-
                       0.1248 + exp(-4*m.x1)*m.x4 + exp(-4*m.x2)*m.x5)**2 + (-0.0981 + exp(-5*m.x1)*m.x4 + exp(-5*m.x2)*
                       m.x5)**2 + (-0.0549 + exp(-6*m.x1)*m.x4 + exp(-6*m.x2)*m.x5)**2 + (-0.0174 + exp(-7*m.x1)*m.x4 + 
                       exp(-7*m.x2)*m.x5)**2 + (-0.0249 + exp(-8*m.x1)*m.x4 + exp(-8*m.x2)*m.x5)**2 + (-0.0154 + exp(-9*
                       m.x1)*m.x4 + exp(-9*m.x2)*m.x5)**2 + (-0.0127 + exp(-10*m.x1)*m.x4 + exp(-10*m.x2)*m.x5)**2
                       , sense=minimize)

m.c1 = Constraint(expr=   m.x1 - m.x2 <= 0)
