#  NLP written by GAMS Convert at 04/21/18 13:51:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          4        4        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        5        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         13        3       10        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(1E-6,1),initialize=0.00421)
m.x3 = Var(within=Reals,bounds=(1E-6,1),initialize=0.99579)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0.0258947377097763)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0.998699779997328)

m.obj = Objective(expr=(0.06391 + log(m.x2))*m.x2 + (-0.02875 + log(m.x3))*m.x3 + 0.925356626778358*m.x2*m.x5 + 
                       0.746014540096753*m.x3*m.x4, sense=minimize)

m.c2 = Constraint(expr=m.x4*(m.x2 + 0.159040857374844*m.x3) - m.x2 == 0)

m.c3 = Constraint(expr=m.x5*(0.307941026821595*m.x2 + m.x3) - m.x3 == 0)

m.c4 = Constraint(expr=   m.x2 + m.x3 == 1)
