#  NLP written by GAMS Convert at 04/21/18 13:51:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        1        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          2        2        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          2        1        1        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,10),initialize=6.325)

m.obj = Objective(expr=8.9248e-5*m.x1 - 0.0218343*m.x1**2 + 0.998266*m.x1**3 - 1.6995*m.x1**4 + 0.2*m.x1**5
                       , sense=minimize)
