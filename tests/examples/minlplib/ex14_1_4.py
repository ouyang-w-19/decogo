#  NLP written by GAMS Convert at 04/21/18 13:51:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          5        1        0        4        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          4        4        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         14        8        6        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0.25,1),initialize=0.25)
m.x2 = Var(within=Reals,bounds=(1.5,6.28),initialize=1.5)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   m.x3, sense=minimize)

m.c1 = Constraint(expr=0.5*sin(m.x1*m.x2) - 0.5*m.x1 - 0.0795774703703634*m.x2 - m.x3 <= 0)

m.c2 = Constraint(expr=0.920422529629637*exp(2*m.x1) - 5.4365636*m.x1 + 0.865255957591193*m.x2 - m.x3
                        <= 2.5019678106022)

m.c3 = Constraint(expr=0.5*m.x1 - 0.5*sin(m.x1*m.x2) + 0.0795774703703634*m.x2 - m.x3 <= 0)

m.c5 = Constraint(expr=5.4365636*m.x1 - 0.920422529629637*exp(2*m.x1) - 0.865255957591193*m.x2 - m.x3
                        <= -2.5019678106022)
