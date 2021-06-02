#  NLP written by GAMS Convert at 04/21/18 13:51:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          7        7        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          9        9        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         25        5       20        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(1E-7,0.5),initialize=0.4993)
m.x3 = Var(within=Reals,bounds=(1E-7,0.5),initialize=0.0007)
m.x4 = Var(within=Reals,bounds=(1E-7,0.5),initialize=0.3441)
m.x5 = Var(within=Reals,bounds=(1E-7,0.5),initialize=0.1559)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0.901221308981222)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0.0274569351394739)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0.691165161172019)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0.998619236157215)

m.obj = Objective(expr=(log(m.x2) - log(m.x2 + m.x4))*m.x2 + (log(m.x4) - log(m.x2 + m.x4))*m.x4 + (log(m.x3) - log(m.x3
                        + m.x5))*m.x3 + (log(m.x5) - log(m.x3 + m.x5))*m.x5 + 0.925356626778358*m.x2*m.x8 + 
                       0.746014540096753*m.x4*m.x6 + 0.925356626778358*m.x3*m.x9 + 0.746014540096753*m.x5*m.x7
                       , sense=minimize)

m.c2 = Constraint(expr=m.x6*(m.x2 + 0.159040857374844*m.x4) - m.x2 == 0)

m.c3 = Constraint(expr=m.x7*(m.x3 + 0.159040857374844*m.x5) - m.x3 == 0)

m.c4 = Constraint(expr=m.x8*(0.307941026821595*m.x2 + m.x4) - m.x4 == 0)

m.c5 = Constraint(expr=m.x9*(0.307941026821595*m.x3 + m.x5) - m.x5 == 0)

m.c6 = Constraint(expr=   m.x2 + m.x3 == 0.5)

m.c7 = Constraint(expr=   m.x4 + m.x5 == 0.5)
