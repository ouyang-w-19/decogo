#  NLP written by GAMS Convert at 04/21/18 13:51:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          3        3        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        5        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          9        5        4        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(1E-7,0.5),initialize=0.4994)
m.x3 = Var(within=Reals,bounds=(1E-7,0.5),initialize=0.0006)
m.x4 = Var(within=Reals,bounds=(1E-7,0.5),initialize=0.1179)
m.x5 = Var(within=Reals,bounds=(1E-7,0.5),initialize=0.3821)

m.obj = Objective(expr=log(m.x2/(8*m.x2 + m.x4))*m.x2 + log(m.x4/(8*m.x2 + m.x4))*m.x4 + 0.0696225416798359*m.x2 + 
                       0.752006*m.x4 + log(8*m.x2 + 1.6*m.x4)*(8*m.x2 + 1.6*m.x4) + 5*log(m.x2/(5.00000397494442*m.x2 + 
                       0.480353357956269*m.x4))*m.x2 + 3*log(m.x2/(8.96062592375197*m.x2 + 1.13841069150863*m.x4))*m.x2
                        + 1.6*log(m.x4/(1.69889877049372*m.x2 + 1.6*m.x4))*m.x4 + log(m.x3/(8*m.x3 + m.x5))*m.x3 + log(
                       m.x5/(8*m.x3 + m.x5))*m.x5 + 0.0696225416798359*m.x3 + 0.752006*m.x5 + log(8*m.x3 + 1.6*m.x5)*(8*
                       m.x3 + 1.6*m.x5) + 5*log(m.x3/(5.00000397494442*m.x3 + 0.480353357956269*m.x5))*m.x3 + 3*log(m.x3
                       /(8.96062592375197*m.x3 + 1.13841069150863*m.x5))*m.x3 + 1.6*log(m.x5/(1.69889877049372*m.x3 + 
                       1.6*m.x5))*m.x5 - 8*log(m.x2)*m.x2 - 1.6*log(m.x4)*m.x4 - 8*log(m.x3)*m.x3 - 1.6*log(m.x5)*m.x5
                       , sense=minimize)

m.c2 = Constraint(expr=   m.x2 + m.x3 == 0.5)

m.c3 = Constraint(expr=   m.x4 + m.x5 == 0.5)
