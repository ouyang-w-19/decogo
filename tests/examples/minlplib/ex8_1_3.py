#  NLP written by GAMS Convert at 04/21/18 13:51:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        1        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          3        3        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          3        1        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=(1 + (1 + m.x1 + m.x2)**2*(19 + 3*m.x1**2 - 14*m.x1 + 6*m.x1*m.x2 - 14*m.x2 + 3*m.x2**2))*(30 + (
                       2*m.x1 - 3*m.x2)**2*(18 + 12*m.x1**2 - 32*m.x1 - 36*m.x1*m.x2 + 48*m.x2 + 27*m.x2**2))
                       , sense=minimize)
