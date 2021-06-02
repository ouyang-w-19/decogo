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


m.x2 = Var(within=Reals,bounds=(1E-7,0.2),initialize=0.19863)
m.x3 = Var(within=Reals,bounds=(1E-7,0.2),initialize=0.00137)
m.x4 = Var(within=Reals,bounds=(1E-7,0.4),initialize=0.00428)
m.x5 = Var(within=Reals,bounds=(1E-7,0.4),initialize=0.39572)
m.x6 = Var(within=Reals,bounds=(1E-7,0.4),initialize=0.39922)
m.x7 = Var(within=Reals,bounds=(1E-7,0.4),initialize=0.00078)

m.obj = Objective(expr=log(2.1055*m.x2 + 3.1878*m.x4 + 0.92*m.x6)*(15.3261663216011*m.x2 + 23.2043471859416*m.x4 + 
                       6.69678129464404*m.x6) - 2.46348749603266*m.x2 - 4.33155441248417*m.x4 - 0.626542690017204*m.x6
                        + 6.4661663216011*log(m.x2/(2.1055*m.x2 + 3.1878*m.x4 + 0.92*m.x6))*m.x2 + 12.2043471859416*log(
                       m.x4/(2.1055*m.x2 + 3.1878*m.x4 + 0.92*m.x6))*m.x4 + 0.696781294644034*log(m.x6/(2.1055*m.x2 + 
                       3.1878*m.x4 + 0.92*m.x6))*m.x6 + 9.86*log(m.x2/(1.972*m.x2 + 2.4*m.x4 + 1.4*m.x6))*m.x2 + 12*log(
                       m.x4/(1.972*m.x2 + 2.4*m.x4 + 1.4*m.x6))*m.x4 + 7*log(m.x6/(1.972*m.x2 + 2.4*m.x4 + 1.4*m.x6))*
                       m.x6 + log(1.972*m.x2 + 2.4*m.x4 + 1.4*m.x6)*(1.972*m.x2 + 2.4*m.x4 + 1.4*m.x6) + 1.972*log(m.x2/
                       (1.972*m.x2 + 0.283910843616504*m.x4 + 3.02002220174195*m.x6))*m.x2 + 2.4*log(m.x4/(
                       1.45991339466884*m.x2 + 2.4*m.x4 + 0.415073537580851*m.x6))*m.x4 + 1.4*log(m.x6/(
                       0.602183324335333*m.x2 + 0.115623371371275*m.x4 + 1.4*m.x6))*m.x6 + log(2.1055*m.x3 + 3.1878*m.x5
                        + 0.92*m.x7)*(15.3261663216011*m.x3 + 23.2043471859416*m.x5 + 6.69678129464404*m.x7) - 
                       2.46348749603266*m.x3 - 4.33155441248417*m.x5 - 0.626542690017204*m.x7 + 6.4661663216011*log(m.x3
                       /(2.1055*m.x3 + 3.1878*m.x5 + 0.92*m.x7))*m.x3 + 12.2043471859416*log(m.x5/(2.1055*m.x3 + 3.1878*
                       m.x5 + 0.92*m.x7))*m.x5 + 0.696781294644034*log(m.x7/(2.1055*m.x3 + 3.1878*m.x5 + 0.92*m.x7))*
                       m.x7 + 9.86*log(m.x3/(1.972*m.x3 + 2.4*m.x5 + 1.4*m.x7))*m.x3 + 12*log(m.x5/(1.972*m.x3 + 2.4*
                       m.x5 + 1.4*m.x7))*m.x5 + 7*log(m.x7/(1.972*m.x3 + 2.4*m.x5 + 1.4*m.x7))*m.x7 + log(1.972*m.x3 + 
                       2.4*m.x5 + 1.4*m.x7)*(1.972*m.x3 + 2.4*m.x5 + 1.4*m.x7) + 1.972*log(m.x3/(1.972*m.x3 + 
                       0.283910843616504*m.x5 + 3.02002220174195*m.x7))*m.x3 + 2.4*log(m.x5/(1.45991339466884*m.x3 + 2.4
                       *m.x5 + 0.415073537580851*m.x7))*m.x5 + 1.4*log(m.x7/(0.602183324335333*m.x3 + 0.115623371371275*
                       m.x5 + 1.4*m.x7))*m.x7 - 17.2981663216011*log(m.x2)*m.x2 - 25.6043471859416*log(m.x4)*m.x4 - 
                       8.09678129464404*log(m.x6)*m.x6 - 17.2981663216011*log(m.x3)*m.x3 - 25.6043471859416*log(m.x5)*
                       m.x5 - 8.09678129464404*log(m.x7)*m.x7, sense=minimize)

m.c2 = Constraint(expr=   m.x2 + m.x3 == 0.2)

m.c3 = Constraint(expr=   m.x4 + m.x5 == 0.4)

m.c4 = Constraint(expr=   m.x6 + m.x7 == 0.4)
