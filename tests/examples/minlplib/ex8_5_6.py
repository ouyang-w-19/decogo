#  NLP written by GAMS Convert at 04/21/18 13:51:48
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          5        5        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          7        7        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         21        9       12        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(None,None),initialize=0.333333333333333)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0.333333333333333)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0.333333333333333)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=2)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=1)

m.obj = Objective(expr=log(m.x2)*m.x2 + log(m.x3)*m.x3 + log(m.x4)*m.x4 - log(m.x5 - m.x7) + m.x5 - 0.353553390593274*
                       log((m.x5 + 2.41421356237309*m.x7)/(m.x5 - 0.414213562373095*m.x7))*m.x6/m.x7 + 1.42876598488588*
                       m.x2 + 1.27098480432594*m.x3 + 1.62663700075562*m.x4 - 1, sense=minimize)

m.c2 = Constraint(expr=m.x5**3 - m.x5**2*(1 - m.x7) + (-3*m.x7**2 - 2*m.x7 + m.x6)*m.x5 - m.x6*m.x7 + m.x7**3 + m.x7**2
                        == 0)

m.c3 = Constraint(expr=-(0.142724*m.x2*m.x2 + 0.206577*m.x2*m.x3 + 0.342119*m.x2*m.x4 + 0.206577*m.x3*m.x2 + 0.323084*
                       m.x3*m.x3 + 0.547748*m.x3*m.x4 + 0.342119*m.x4*m.x2 + 0.547748*m.x4*m.x3 + 0.968906*m.x4*m.x4)
                        + m.x6 == 0)

m.c4 = Constraint(expr= - 0.0815247*m.x2 - 0.0907391*m.x3 - 0.13705*m.x4 + m.x7 == 0)

m.c5 = Constraint(expr=   m.x2 + m.x3 + m.x4 == 1)
