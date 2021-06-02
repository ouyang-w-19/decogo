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


m.x2 = Var(within=Reals,bounds=(1E-6,1),initialize=0.7154)
m.x3 = Var(within=Reals,bounds=(1E-6,1),initialize=0.00336)
m.x4 = Var(within=Reals,bounds=(1E-6,1),initialize=0.28124)

m.obj = Objective(expr=log(2.4088*m.x2 + 8.8495*m.x3 + 2.0086*m.x4)*(10.4807341082197*m.x2 + 38.5043409542885*m.x3 + 
                       8.73945638067505*m.x4) + 0.303602206615077*m.x2 - 3.98949602721008*m.x3 + 0.0423576909050935*m.x4
                        + 0.240734108219679*log(m.x2)*m.x2 + 2.64434095428848*log(m.x3)*m.x3 + 0.399456380675047*log(
                       m.x4)*m.x4 - 0.240734108219679*log(2.4088*m.x2 + 8.8495*m.x3 + 2.0086*m.x4)*m.x2 - 
                       2.64434095428848*log(2.4088*m.x2 + 8.8495*m.x3 + 2.0086*m.x4)*m.x3 - 0.399456380675047*log(2.4088
                       *m.x2 + 8.8495*m.x3 + 2.0086*m.x4)*m.x4 + 11.24*log(m.x2)*m.x2 + 36.86*log(m.x3)*m.x3 + 9.34*log(
                       m.x4)*m.x4 - 11.24*log(2.248*m.x2 + 7.372*m.x3 + 1.868*m.x4)*m.x2 - 36.86*log(2.248*m.x2 + 7.372*
                       m.x3 + 1.868*m.x4)*m.x3 - 9.34*log(2.248*m.x2 + 7.372*m.x3 + 1.868*m.x4)*m.x4 + log(2.248*m.x2 + 
                       7.372*m.x3 + 1.868*m.x4)*(2.248*m.x2 + 7.372*m.x3 + 1.868*m.x4) + 2.248*log(m.x2)*m.x2 + 7.372*
                       log(m.x3)*m.x3 + 1.868*log(m.x4)*m.x4 - 2.248*log(2.248*m.x2 + 5.82088173817021*m.x3 + 
                       0.382446861901943*m.x4)*m.x2 - 7.372*log(0.972461133672523*m.x2 + 7.372*m.x3 + 1.1893141713454*
                       m.x4)*m.x3 - 1.868*log(1.86752460515164*m.x2 + 2.61699842799583*m.x3 + 1.868*m.x4)*m.x4 - 
                       12.7287341082197*log(m.x2)*m.x2 - 45.8763409542885*log(m.x3)*m.x3 - 10.607456380675*log(m.x4)*
                       m.x4, sense=minimize)

m.c2 = Constraint(expr=   m.x2 + m.x3 + m.x4 == 1)
