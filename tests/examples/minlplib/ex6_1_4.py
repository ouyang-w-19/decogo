#  NLP written by GAMS Convert at 04/21/18 13:51:45
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
#         22        4       18        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(1E-6,1),initialize=7E-5)
m.x3 = Var(within=Reals,bounds=(1E-6,1),initialize=0.99686)
m.x4 = Var(within=Reals,bounds=(1E-6,1),initialize=0.00307)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0.000474076675116379)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0.997993046160137)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0.0126755759820888)

m.obj = Objective(expr=(0.28809 + log(m.x2))*m.x2 + (-0.29158 + log(m.x3))*m.x3 + (0.59336 + log(m.x4))*m.x4 + m.x2*(
                       1.44805026165593*m.x6 + 0.989428667054834*m.x7) + m.x3*(1.12676386427658*m.x5 + 1.00363012835441*
                       m.x7) + m.x4*(0.0347225450624344*m.x5 + 0.82681418300153*m.x6), sense=minimize)

m.c2 = Constraint(expr=m.x5*(m.x2 + 0.145002897355373*m.x3 + 0.989528214945409*m.x4) - m.x2 == 0)

m.c3 = Constraint(expr=m.x6*(0.293701311601799*m.x2 + m.x3 + 0.646291923054068*m.x4) - m.x3 == 0)

m.c4 = Constraint(expr=m.x7*(0.619143628558899*m.x2 + 0.239837817616513*m.x3 + m.x4) - m.x4 == 0)

m.c5 = Constraint(expr=   m.x2 + m.x3 + m.x4 == 1)
