#  NLP written by GAMS Convert at 04/21/18 13:51:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         18       11        0        7        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         18       18        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         80       26       54        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,3.4329),initialize=0)
m.x2 = Var(within=Reals,bounds=(None,0.1627),initialize=0)
m.x3 = Var(within=Reals,bounds=(None,0.1139),initialize=0)
m.x4 = Var(within=Reals,bounds=(0.2539,None),initialize=0.2539)
m.x5 = Var(within=Reals,bounds=(None,0.0208),initialize=0)
m.x6 = Var(within=Reals,bounds=(2.0247,None),initialize=2.0247)
m.x7 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x8 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   m.x9, sense=minimize)

m.c2 = Constraint(expr=m.x8**4*m.x14 - m.x8**6*m.x16 - m.x8**2*m.x12 + m.x10 == 0)

m.c3 = Constraint(expr=m.x8**6*m.x17 - m.x8**4*m.x15 + m.x8**2*m.x13 - m.x11 == 0)

m.c4 = Constraint(expr= - m.x1 - 1.2721*m.x9 <= -3.4329)

m.c5 = Constraint(expr= - m.x2 - 0.06*m.x9 <= -0.1627)

m.c6 = Constraint(expr= - m.x3 - 0.0782*m.x9 <= -0.1139)

m.c7 = Constraint(expr=   m.x4 - 0.3068*m.x9 <= 0.2539)

m.c8 = Constraint(expr= - m.x5 - 0.0108*m.x9 <= -0.0208)

m.c9 = Constraint(expr=   m.x6 - 2.4715*m.x9 <= 2.0247)

m.c10 = Constraint(expr=   m.x7 + 9*m.x9 <= 1)

m.c11 = Constraint(expr=-(6.82079e-5*m.x1*m.x3*m.x4**2 + 6.82079e-5*m.x1*m.x2*m.x4*m.x5) + m.x10 == 0)

m.c12 = Constraint(expr=-(0.00076176*m.x2**2*m.x5**2 + 0.00076176*m.x3**2*m.x4**2 + 0.000402141*m.x1*m.x2*m.x5**2 + 
                        0.00337606*m.x1*m.x3*m.x4**2 + 6.82079e-5*m.x1*m.x4*m.x5 + 0.00051612*m.x2**2*m.x5*m.x6 + 
                        0.00337606*m.x1*m.x2*m.x4*m.x5 + 6.82079e-5*m.x1*m.x2*m.x4*m.x7 + 6.28987e-5*m.x1*m.x2*m.x5*m.x6
                         + 0.000402141*m.x1*m.x3*m.x4*m.x5 + 6.28987e-5*m.x1*m.x3*m.x4*m.x6 + 0.00152352*m.x2*m.x3*m.x4*
                        m.x5 + 0.00051612*m.x2*m.x3*m.x4*m.x6) + m.x11 == 0)

m.c13 = Constraint(expr=-(0.000402141*m.x5**2*m.x1 + 0.00152352*m.x5**2*m.x2 + 0.0552*m.x2**2*m.x5**2 + 0.0552*m.x3**2*
                        m.x4**2 + 0.0189477*m.x1*m.x2*m.x5**2 + 0.034862*m.x1*m.x3*m.x4**2 + 0.00336706*m.x1*m.x4*m.x5
                         + 6.82079e-5*m.x1*m.x4*m.x7 + 6.28987e-5*m.x1*m.x5*m.x6 + 0.00152352*m.x3*m.x4*m.x5 + 
                        0.00051612*m.x3*m.x4*m.x6 - 0.00234048*m.x3**2*m.x4*m.x6 + 0.034862*m.x1*m.x2*m.x4*m.x5 + 
                        0.0237398*m.x2**2*m.x5*m.x6 + 0.00152352*m.x2**2*m.x5*m.x7 + 0.00051612*m.x2**2*m.x6*m.x7 + 
                        0.00336706*m.x1*m.x2*m.x4*m.x7 + 0.00287416*m.x1*m.x2*m.x5*m.x6 + 0.000804282*m.x1*m.x2*m.x5*
                        m.x7 + 6.28987e-5*m.x1*m.x2*m.x6*m.x7 + 0.0189477*m.x1*m.x3*m.x4*m.x5 + 0.00287416*m.x1*m.x3*
                        m.x4*m.x6 + 0.000402141*m.x1*m.x3*m.x4*m.x7 + 0.1104*m.x2*m.x3*m.x4*m.x5 + 0.0237398*m.x2*m.x3*
                        m.x4*m.x6 + 0.00152352*m.x2*m.x3*m.x4*m.x7 - 0.00234048*m.x2*m.x3*m.x5*m.x6 + 0.00103224*m.x2*
                        m.x5*m.x6) + m.x12 == 0)

m.c14 = Constraint(expr=-(0.189477*m.x5**2*m.x1 + 0.1104*m.x5**2*m.x2 + 0.00051612*m.x5*m.x6 + m.x2**2*m.x5**2 + 
                        0.00076176*m.x2**2*m.x7**2 + m.x3**2*m.x4**2 + 0.1586*m.x1*m.x2*m.x5**2 + 0.000402141*m.x1*m.x2*
                        m.x7**2 + 0.0872*m.x1*m.x3*m.x4**2 + 0.034862*m.x1*m.x4*m.x5 + 0.00336706*m.x1*m.x4*m.x7 + 
                        0.00287416*m.x1*m.x5*m.x6 + 6.28987e-5*m.x1*m.x6*m.x7 + 0.00103224*m.x2*m.x6*m.x7 + 0.1104*m.x3*
                        m.x4*m.x5 + 0.0237398*m.x3*m.x4*m.x6 + 0.00152352*m.x3*m.x4*m.x7 - 0.00234048*m.x3*m.x5*m.x6 + 
                        0.1826*m.x2**2*m.x5*m.x6 + 0.1104*m.x2**2*m.x5*m.x7 + 0.0237398*m.x2**2*m.x6*m.x7 - 0.0848*m.x3
                        **2*m.x4*m.x6 + 0.0872*m.x1*m.x2*m.x4*m.x5 + 0.034862*m.x1*m.x2*m.x4*m.x7 + 0.0215658*m.x1*m.x2*
                        m.x5*m.x6 + 0.0378954*m.x1*m.x2*m.x5*m.x7 + 0.00287416*m.x1*m.x2*m.x6*m.x7 + 0.1586*m.x1*m.x3*
                        m.x4*m.x5 + 0.0215658*m.x1*m.x3*m.x4*m.x6 + 0.0189477*m.x1*m.x3*m.x4*m.x7 + 2*m.x2*m.x3*m.x4*
                        m.x5 + 0.1826*m.x2*m.x3*m.x4*m.x6 + 0.1104*m.x2*m.x3*m.x4*m.x7 - 0.0848*m.x2*m.x3*m.x5*m.x6 - 
                        0.00234048*m.x2*m.x3*m.x6*m.x7 + 0.00076176*m.x5**2 + 0.0474795*m.x2*m.x5*m.x6 + 0.000804282*
                        m.x1*m.x5*m.x7 + 0.00304704*m.x2*m.x5*m.x7) + m.x13 == 0)

m.c15 = Constraint(expr=-(0.1586*m.x5**2*m.x1 + 0.000402141*m.x7**2*m.x1 + 2*m.x5**2*m.x2 + 0.00152352*m.x7**2*m.x2 + 
                        0.0237398*m.x5*m.x6 + 0.00152352*m.x5*m.x7 + 0.00051612*m.x6*m.x7 + 0.0552*m.x2**2*m.x7**2 + 
                        0.0189477*m.x1*m.x2*m.x7**2 + 0.0872*m.x1*m.x4*m.x5 + 0.034862*m.x1*m.x4*m.x7 + 0.0215658*m.x1*
                        m.x5*m.x6 + 0.00287416*m.x1*m.x6*m.x7 + 0.0474795*m.x2*m.x6*m.x7 + 2*m.x3*m.x4*m.x5 + 0.1826*
                        m.x3*m.x4*m.x6 + 0.1104*m.x3*m.x4*m.x7 - 0.0848*m.x3*m.x5*m.x6 - 0.00234048*m.x3*m.x6*m.x7 + 2*
                        m.x2**2*m.x5*m.x7 + 0.1826*m.x2**2*m.x6*m.x7 + 0.0872*m.x1*m.x2*m.x4*m.x7 + 0.3172*m.x1*m.x2*
                        m.x5*m.x7 + 0.0215658*m.x1*m.x2*m.x6*m.x7 + 0.1586*m.x1*m.x3*m.x4*m.x7 + 2*m.x2*m.x3*m.x4*m.x7
                         - 0.0848*m.x2*m.x3*m.x6*m.x7 + 0.0552*m.x5**2 + 0.3652*m.x2*m.x5*m.x6 + 0.0378954*m.x1*m.x5*
                        m.x7 + 0.2208*m.x2*m.x5*m.x7) + m.x14 == 0)

m.c16 = Constraint(expr=-(0.0189477*m.x7**2*m.x1 + 0.1104*m.x7**2*m.x2 + 0.1826*m.x5*m.x6 + 0.1104*m.x5*m.x7 + 0.0237398
                        *m.x6*m.x7 + m.x2**2*m.x7**2 + 0.1586*m.x1*m.x2*m.x7**2 + 0.0872*m.x1*m.x4*m.x7 + 0.0215658*m.x1
                        *m.x6*m.x7 + 0.3652*m.x2*m.x6*m.x7 + 2*m.x3*m.x4*m.x7 - 0.0848*m.x3*m.x6*m.x7 + m.x5**2 + 
                        0.00076176*m.x7**2 + 0.3172*m.x1*m.x5*m.x7 + 4*m.x2*m.x5*m.x7) + m.x15 == 0)

m.c17 = Constraint(expr=-(0.1586*m.x7**2*m.x1 + 2*m.x7**2*m.x2 + 2*m.x5*m.x7 + 0.1826*m.x6*m.x7 + 0.0552*m.x7**2)
                         + m.x16 == 0)

m.c18 = Constraint(expr=-m.x7**2 + m.x17 == 0)
