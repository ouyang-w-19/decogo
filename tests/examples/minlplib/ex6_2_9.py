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


m.x2 = Var(within=Reals,bounds=(1E-7,0.5),initialize=0.4998)
m.x3 = Var(within=Reals,bounds=(1E-7,0.5),initialize=0.0002)
m.x4 = Var(within=Reals,bounds=(1E-7,0.5),initialize=0.0451)
m.x5 = Var(within=Reals,bounds=(1E-7,0.5),initialize=0.4549)

m.obj = Objective(expr=log(4.8274*m.x2 + 0.92*m.x4)*(31.4830434782609*m.x2 + 6*m.x4) - 1.36551138119385*m.x2 + 
                       2.8555953099828*m.x4 + 11.5030434782609*log(m.x2/(4.8274*m.x2 + 0.92*m.x4))*m.x2 + 20.98*log(m.x2
                       /(4.196*m.x2 + 1.4*m.x4))*m.x2 + 7*log(m.x4/(4.196*m.x2 + 1.4*m.x4))*m.x4 + log(4.196*m.x2 + 1.4*
                       m.x4)*(4.196*m.x2 + 1.4*m.x4) + 1.62*log(m.x2/(7.52678200680961*m.x2 + 0.443737968424621*m.x4))*
                       m.x2 + 0.848*log(m.x2/(7.52678200680961*m.x2 + 0.443737968424621*m.x4))*m.x2 + 1.728*log(m.x2/(
                       1.82245052351472*m.x2 + 1.4300083598626*m.x4))*m.x2 + 1.4*log(m.x4/(0.504772348000588*m.x2 + 1.4*
                       m.x4))*m.x4 + log(4.8274*m.x3 + 0.92*m.x5)*(31.4830434782609*m.x3 + 6*m.x5) - 1.36551138119385*
                       m.x3 + 2.8555953099828*m.x5 + 11.5030434782609*log(m.x3/(4.8274*m.x3 + 0.92*m.x5))*m.x3 + 20.98*
                       log(m.x3/(4.196*m.x3 + 1.4*m.x5))*m.x3 + 7*log(m.x5/(4.196*m.x3 + 1.4*m.x5))*m.x5 + log(4.196*
                       m.x3 + 1.4*m.x5)*(4.196*m.x3 + 1.4*m.x5) + 1.62*log(m.x3/(7.52678200680961*m.x3 + 
                       0.443737968424621*m.x5))*m.x3 + 0.848*log(m.x3/(7.52678200680961*m.x3 + 0.443737968424621*m.x5))*
                       m.x3 + 1.728*log(m.x3/(1.82245052351472*m.x3 + 1.4300083598626*m.x5))*m.x3 + 1.4*log(m.x5/(
                       0.504772348000588*m.x3 + 1.4*m.x5))*m.x5 - 35.6790434782609*log(m.x2)*m.x2 - 7.4*log(m.x4)*m.x4
                        - 35.6790434782609*log(m.x3)*m.x3 - 7.4*log(m.x5)*m.x5, sense=minimize)

m.c2 = Constraint(expr=   m.x2 + m.x3 == 0.5)

m.c3 = Constraint(expr=   m.x4 + m.x5 == 0.5)
