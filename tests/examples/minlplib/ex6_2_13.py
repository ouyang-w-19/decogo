#  NLP written by GAMS Convert at 04/21/18 13:51:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          4        4        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          7        7        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         13        7        6        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(1E-7,0.08),initialize=0.0739)
m.x3 = Var(within=Reals,bounds=(1E-7,0.08),initialize=0.0061)
m.x4 = Var(within=Reals,bounds=(1E-7,0.3),initialize=0.2773)
m.x5 = Var(within=Reals,bounds=(1E-7,0.3),initialize=0.0227)
m.x6 = Var(within=Reals,bounds=(1E-7,0.62),initialize=0.5731)
m.x7 = Var(within=Reals,bounds=(1E-7,0.62),initialize=0.0469)

m.obj = Objective(expr=log(m.x2/(3*m.x2 + 6*m.x4 + m.x6))*m.x2 + log(m.x4/(3*m.x2 + 6*m.x4 + m.x6))*m.x4 + log(m.x6/(3*
                       m.x2 + 6*m.x4 + m.x6))*m.x6 - 0.80323071133189*m.x2 + 1.79175946922805*m.x4 + 0.752006*m.x6 + 
                       log(3*m.x2 + 6*m.x4 + 1.6*m.x6)*(3*m.x2 + 6*m.x4 + 1.6*m.x6) + 2*log(m.x2/(2.00000019368913*m.x2
                        + 4.64593*m.x4 + 0.480353*m.x6))*m.x2 + log(m.x2/(1.00772874182154*m.x2 + 0.724703350369523*m.x4
                        + 0.947722362492017*m.x6))*m.x2 + 6*log(m.x4/(3.36359157977228*m.x2 + 6*m.x4 + 1.13841069150863*
                       m.x6))*m.x4 + 1.6*log(m.x6/(1.6359356134845*m.x2 + 3.39220996773471*m.x4 + 1.6*m.x6))*m.x6 + log(
                       m.x3/(3*m.x3 + 6*m.x5 + m.x7))*m.x3 + log(m.x5/(3*m.x3 + 6*m.x5 + m.x7))*m.x5 + log(m.x7/(3*m.x3
                        + 6*m.x5 + m.x7))*m.x7 - 0.80323071133189*m.x3 + 1.79175946922805*m.x5 + 0.752006*m.x7 + log(3*
                       m.x3 + 6*m.x5 + 1.6*m.x7)*(3*m.x3 + 6*m.x5 + 1.6*m.x7) + 2*log(m.x3/(2.00000019368913*m.x3 + 
                       4.64593*m.x5 + 0.480353*m.x7))*m.x3 + log(m.x3/(1.00772874182154*m.x3 + 0.724703350369523*m.x5 + 
                       0.947722362492017*m.x7))*m.x3 + 6*log(m.x5/(3.36359157977228*m.x3 + 6*m.x5 + 1.13841069150863*
                       m.x7))*m.x5 + 1.6*log(m.x7/(1.6359356134845*m.x3 + 3.39220996773471*m.x5 + 1.6*m.x7))*m.x7 - 3*
                       log(m.x2)*m.x2 - 6*log(m.x4)*m.x4 - 1.6*log(m.x6)*m.x6 - 3*log(m.x3)*m.x3 - 6*log(m.x5)*m.x5 - 
                       1.6*log(m.x7)*m.x7, sense=minimize)

m.c2 = Constraint(expr=   m.x2 + m.x3 == 0.08)

m.c3 = Constraint(expr=   m.x4 + m.x5 == 0.3)

m.c4 = Constraint(expr=   m.x6 + m.x7 == 0.62)
