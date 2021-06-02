#  NLP written by GAMS Convert at 04/21/18 13:51:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         10       10        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         13       13        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         43        7       36        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(1E-7,0.2995),initialize=0.29949)
m.x3 = Var(within=Reals,bounds=(1E-7,0.2995),initialize=1E-5)
m.x4 = Var(within=Reals,bounds=(1E-7,0.1998),initialize=0.06551)
m.x5 = Var(within=Reals,bounds=(1E-7,0.1998),initialize=0.13429)
m.x6 = Var(within=Reals,bounds=(1E-7,0.4994),initialize=0.49873)
m.x7 = Var(within=Reals,bounds=(1E-7,0.4994),initialize=0.00067)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0.373197867737302)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0.000496390669236887)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0.137685122950498)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0.996764152762375)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0.71260468488485)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0.0203746428730577)

m.obj = Objective(expr=(log(m.x2) - log(m.x2 + m.x4 + m.x6))*m.x2 + (log(m.x4) - log(m.x2 + m.x4 + m.x6))*m.x4 + (log(
                       m.x6) - log(m.x2 + m.x4 + m.x6))*m.x6 + (log(m.x3) - log(m.x3 + m.x5 + m.x7))*m.x3 + (log(m.x5)
                        - log(m.x3 + m.x5 + m.x7))*m.x5 + (log(m.x7) - log(m.x3 + m.x5 + m.x7))*m.x7 + m.x2*(
                       1.44805026165593*m.x10 + 0.989428667054834*m.x12) + m.x4*(1.12676386427658*m.x8 + 
                       1.00363012835441*m.x12) + m.x6*(0.0347225450624344*m.x8 + 0.82681418300153*m.x10) + m.x3*(
                       1.44805026165593*m.x11 + 0.989428667054834*m.x13) + m.x5*(1.12676386427658*m.x9 + 
                       1.00363012835441*m.x13) + m.x7*(0.0347225450624344*m.x9 + 0.82681418300153*m.x11)
                       , sense=minimize)

m.c2 = Constraint(expr=m.x8*(m.x2 + 0.145002897355373*m.x4 + 0.989528214945409*m.x6) - m.x2 == 0)

m.c3 = Constraint(expr=m.x9*(m.x3 + 0.145002897355373*m.x5 + 0.989528214945409*m.x7) - m.x3 == 0)

m.c4 = Constraint(expr=m.x10*(0.293701311601799*m.x2 + m.x4 + 0.646291923054068*m.x6) - m.x4 == 0)

m.c5 = Constraint(expr=m.x11*(0.293701311601799*m.x3 + m.x5 + 0.646291923054068*m.x7) - m.x5 == 0)

m.c6 = Constraint(expr=m.x12*(0.619143628558899*m.x2 + 0.239837817616513*m.x4 + m.x6) - m.x6 == 0)

m.c7 = Constraint(expr=m.x13*(0.619143628558899*m.x3 + 0.239837817616513*m.x5 + m.x7) - m.x7 == 0)

m.c8 = Constraint(expr=   m.x2 + m.x3 == 0.2995)

m.c9 = Constraint(expr=   m.x4 + m.x5 == 0.1998)

m.c10 = Constraint(expr=   m.x6 + m.x7 == 0.4994)
