#  NLP written by GAMS Convert at 04/21/18 13:52:11
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          2        2        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          3        3        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          5        2        3        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(900,None),initialize=900)
m.x2 = Var(within=Reals,bounds=(10,None),initialize=10)

m.obj = Objective(expr=116*(10000000/((10 + m.x1/m.x2)*(-288000 + 1440*m.x1)))**0.86 + 47300*m.x1/(-200 + m.x1)
                        - 47300, sense=minimize)

m.c2 = Constraint(expr=-2100*log10(41.1522633744856/m.x2) + m.x1 == 0)
