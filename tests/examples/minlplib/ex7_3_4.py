#  NLP written by GAMS Convert at 04/21/18 13:51:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         18        8        0       10        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         13       13        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         53       30       23        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   m.x12, sense=minimize)

m.c2 = Constraint(expr=m.x11**4*m.x10 - m.x11**2*m.x8 + m.x6 == 0)

m.c3 = Constraint(expr=m.x11**2*m.x9 - m.x7 == 0)

m.c4 = Constraint(expr= - m.x1 - m.x12 <= -10)

m.c5 = Constraint(expr=   m.x1 - m.x12 <= 10)

m.c6 = Constraint(expr=   m.x2 - 0.1*m.x12 <= 1)

m.c7 = Constraint(expr= - m.x2 - 0.1*m.x12 <= -1)

m.c8 = Constraint(expr= - m.x3 - 0.1*m.x12 <= -1)

m.c9 = Constraint(expr=   m.x3 - 0.1*m.x12 <= 1)

m.c10 = Constraint(expr= - m.x4 - 0.01*m.x12 <= -0.2)

m.c11 = Constraint(expr=   m.x4 - 0.01*m.x12 <= 0.2)

m.c12 = Constraint(expr= - m.x5 - 0.005*m.x12 <= -0.05)

m.c13 = Constraint(expr=   m.x5 - 0.005*m.x12 <= 0.05)

m.c14 = Constraint(expr=-54.387*m.x3*m.x2 + m.x6 == 0)

m.c15 = Constraint(expr=-0.2*(1364.67*m.x3*m.x2 - 147.15*m.x4*m.x3*m.x2) + 5.544*m.x5 + m.x7 == 0)

m.c16 = Constraint(expr=-3*(-9.81*m.x2**2*m.x3 - 9.81*m.x3*m.x1*m.x2 - 4.312*m.x3**2*m.x2 + 264.896*m.x3*m.x2 + m.x4*
                        m.x5 - 9.274*m.x5) + m.x8 == 0)

m.c17 = Constraint(expr=-(7*m.x3**2*m.x4*m.x2 - 64.918*m.x3**2*m.x2 + 380.067*m.x3*m.x2 + 3*m.x5*m.x2 + 3*m.x5*m.x1)
                         + m.x9 == 0)

m.c18 = Constraint(expr=-m.x3**2*m.x2*(7*m.x1 + 4*m.x2) + m.x10 == 0)
