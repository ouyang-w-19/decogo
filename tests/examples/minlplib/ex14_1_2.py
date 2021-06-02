#  NLP written by GAMS Convert at 04/21/18 13:51:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         10        2        0        8        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          7        7        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         43       17       26        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0.0001,100),initialize=0.0001)
m.x2 = Var(within=Reals,bounds=(0.0001,100),initialize=0.0001)
m.x3 = Var(within=Reals,bounds=(0.0001,100),initialize=0.0001)
m.x4 = Var(within=Reals,bounds=(0.0001,100),initialize=0.0001)
m.x5 = Var(within=Reals,bounds=(0.0001,100),initialize=0.0001)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   m.x6, sense=minimize)

m.c2 = Constraint(expr=m.x1*m.x2 + m.x1 - 3*m.x5 == 0)

m.c3 = Constraint(expr=2.8845e-6*m.x2**2 + 4.4975e-7*m.x2 + 2*m.x1*m.x2 + m.x1 + 0.000545176668613029*m.x2*m.x3 + 
                       3.40735417883143e-5*m.x2*m.x4 + m.x3**2*m.x2 - 10*m.x5 - m.x6 <= 0)

m.c4 = Constraint(expr=(-2.8845e-6*m.x2**2) - 4.4975e-7*m.x2 - 2*m.x1*m.x2 - m.x1 - 0.000545176668613029*m.x2*m.x3 - 
                       3.40735417883143e-5*m.x2*m.x4 - m.x3**2*m.x2 + 10*m.x5 - m.x6 <= 0)

m.c5 = Constraint(expr=0.386*m.x3**2 + 0.000410621754172864*m.x3 + 0.000545176668613029*m.x2*m.x3 + 2*m.x3**2*m.x2
                        - 8*m.x5 - m.x6 <= 0)

m.c6 = Constraint(expr=(-0.386*m.x3**2) - 0.000410621754172864*m.x3 - 0.000545176668613029*m.x2*m.x3 - 2*m.x3**2*m.x2
                        + 8*m.x5 - m.x6 <= 0)

m.c7 = Constraint(expr=2*m.x4**2 + 3.40735417883143e-5*m.x2*m.x4 - 40*m.x5 - m.x6 <= 0)

m.c8 = Constraint(expr=(-2*m.x4**2) - 3.40735417883143e-5*m.x2*m.x4 + 40*m.x5 - m.x6 <= 0)

m.c9 = Constraint(expr=9.615e-7*m.x2**2 + 4.4975e-7*m.x2 + 0.193*m.x3**2 + 0.000410621754172864*m.x3 + m.x4**2 + m.x1*
                       m.x2 + m.x1 + 0.000545176668613029*m.x2*m.x3 + 3.40735417883143e-5*m.x2*m.x4 + m.x3**2*m.x2
                        - m.x6 <= 1)

m.c10 = Constraint(expr=(-9.615e-7*m.x2**2) - 4.4975e-7*m.x2 - 0.193*m.x3**2 - 0.000410621754172864*m.x3 - m.x4**2 - 
                        m.x1*m.x2 - m.x1 - 0.000545176668613029*m.x2*m.x3 - 3.40735417883143e-5*m.x2*m.x4 - m.x3**2*m.x2
                         - m.x6 <= -1)
