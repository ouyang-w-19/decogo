#  NLP written by GAMS Convert at 04/21/18 13:54:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          3        3        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          8        8        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         11        7        4        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x6 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,3),initialize=0)

m.obj = Objective(expr=   m.x1 + m.x2, sense=minimize)

m.c1 = Constraint(expr=51.5712*m.x3*m.x5 + 20.7324*m.x3 - 25.7856*m.x5 + 14.9251*m.x3*m.x7 - 22.2988*m.x7 - 10.1409*m.x6
                       *m.x7 + 42.3401*m.x6 - m.x1 + m.x2 - 6.6425*m.x4 == -72.82)

m.c2 = Constraint(expr=   m.x3 == 1)
