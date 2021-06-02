#  NLP written by GAMS Convert at 04/21/18 13:51:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          2        2        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          4        4        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          7        4        3        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(1E-6,1),initialize=0.00565)
m.x3 = Var(within=Reals,bounds=(1E-6,1),initialize=0.99054)
m.x4 = Var(within=Reals,bounds=(1E-6,1),initialize=0.00381)

m.obj = Objective(expr=log(2.1055*m.x2 + 3.1878*m.x3 + 0.92*m.x4)*(15.3261663216011*m.x2 + 23.2043471859416*m.x3 + 
                       6.69678129464404*m.x4) + 1.04055250396734*m.x2 - 2.24199441248417*m.x3 + 3.1618173099828*m.x4 + 
                       6.4661663216011*log(m.x2/(2.1055*m.x2 + 3.1878*m.x3 + 0.92*m.x4))*m.x2 + 12.2043471859416*log(
                       m.x3/(2.1055*m.x2 + 3.1878*m.x3 + 0.92*m.x4))*m.x3 + 0.696781294644034*log(m.x4/(2.1055*m.x2 + 
                       3.1878*m.x3 + 0.92*m.x4))*m.x4 + 9.86*log(m.x2/(1.972*m.x2 + 2.4*m.x3 + 1.4*m.x4))*m.x2 + 12*log(
                       m.x3/(1.972*m.x2 + 2.4*m.x3 + 1.4*m.x4))*m.x3 + 7*log(m.x4/(1.972*m.x2 + 2.4*m.x3 + 1.4*m.x4))*
                       m.x4 + log(1.972*m.x2 + 2.4*m.x3 + 1.4*m.x4)*(1.972*m.x2 + 2.4*m.x3 + 1.4*m.x4) + 1.972*log(m.x2/
                       (1.972*m.x2 + 0.283910843616504*m.x3 + 3.02002220174195*m.x4))*m.x2 + 2.4*log(m.x3/(
                       1.45991339466884*m.x2 + 2.4*m.x3 + 0.415073537580851*m.x4))*m.x3 + 1.4*log(m.x4/(
                       0.602183324335333*m.x2 + 0.115623371371275*m.x3 + 1.4*m.x4))*m.x4 - 17.2981663216011*log(m.x2)*
                       m.x2 - 25.6043471859416*log(m.x3)*m.x3 - 8.09678129464404*log(m.x4)*m.x4, sense=minimize)

m.c2 = Constraint(expr=   m.x2 + m.x3 + m.x4 == 1)
