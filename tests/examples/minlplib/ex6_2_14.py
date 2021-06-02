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


m.x2 = Var(within=Reals,bounds=(1E-7,0.5),initialize=0.0583)
m.x3 = Var(within=Reals,bounds=(1E-7,0.5),initialize=0.4417)
m.x4 = Var(within=Reals,bounds=(1E-7,0.5),initialize=0.408)
m.x5 = Var(within=Reals,bounds=(1E-7,0.5),initialize=0.092)

m.obj = Objective(expr=(log(m.x2/(m.x2 + m.x4)) + log(m.x2/(m.x2 + 0.095173*m.x4)))*m.x2 + (log(m.x4/(m.x2 + m.x4)) + 
                       log(m.x4/(0.30384*m.x2 + m.x4)))*m.x4 + log(m.x2 + 2.6738*m.x4)*(m.x2 + 2.6738*m.x4) + log(0.374*
                       m.x2 + m.x4)*(0.374*m.x2 + m.x4) + 2.6738*log(m.x4/(m.x2 + 2.6738*m.x4))*m.x4 + 0.374*log(m.x2/(
                       0.374*m.x2 + m.x4))*m.x2 + (log(m.x3/(m.x3 + m.x5)) + log(m.x3/(m.x3 + 0.095173*m.x5)))*m.x3 + (
                       log(m.x5/(m.x3 + m.x5)) + log(m.x5/(0.30384*m.x3 + m.x5)))*m.x5 + log(m.x3 + 2.6738*m.x5)*(m.x3
                        + 2.6738*m.x5) + log(0.374*m.x3 + m.x5)*(0.374*m.x3 + m.x5) + 2.6738*log(m.x5/(m.x3 + 2.6738*
                       m.x5))*m.x5 + 0.374*log(m.x3/(0.374*m.x3 + m.x5))*m.x3 - 3.6838*log(m.x2)*m.x2 - 1.59549*log(m.x4
                       )*m.x4 - 3.6838*log(m.x3)*m.x3 - 1.59549*log(m.x5)*m.x5, sense=minimize)

m.c2 = Constraint(expr=   m.x2 + m.x3 == 0.5)

m.c3 = Constraint(expr=   m.x4 + m.x5 == 0.5)
