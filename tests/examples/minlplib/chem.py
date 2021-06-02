#  NLP written by GAMS Convert at 04/21/18 13:51:14
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          5        5        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         12       12        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         37       26       11        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0.001,None),initialize=0.001)
m.x2 = Var(within=Reals,bounds=(0.001,None),initialize=0.001)
m.x3 = Var(within=Reals,bounds=(0.001,None),initialize=0.001)
m.x4 = Var(within=Reals,bounds=(0.001,None),initialize=0.001)
m.x5 = Var(within=Reals,bounds=(0.001,None),initialize=0.001)
m.x6 = Var(within=Reals,bounds=(0.001,None),initialize=0.001)
m.x7 = Var(within=Reals,bounds=(0.001,None),initialize=0.001)
m.x8 = Var(within=Reals,bounds=(0.001,None),initialize=0.001)
m.x9 = Var(within=Reals,bounds=(0.001,None),initialize=0.001)
m.x10 = Var(within=Reals,bounds=(0.001,None),initialize=0.001)
m.x11 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)

m.obj = Objective(expr=(-6.05576803624071 + log(m.x1/m.x11))*m.x1 + (-17.1307680362407 + log(m.x2/m.x11))*m.x2 + (-
                       34.0207680362407 + log(m.x3/m.x11))*m.x3 + (-5.88076803624071 + log(m.x4/m.x11))*m.x4 + (-
                       24.6877680362407 + log(m.x5/m.x11))*m.x5 + (-14.9527680362407 + log(m.x6/m.x11))*m.x6 + (-
                       24.0667680362407 + log(m.x7/m.x11))*m.x7 + (-10.6747680362407 + log(m.x8/m.x11))*m.x8 + (-
                       26.6287680362407 + log(m.x9/m.x11))*m.x9 + (-22.1447680362407 + log(m.x10/m.x11))*m.x10
                       , sense=minimize)

m.c1 = Constraint(expr=   m.x1 + 2*m.x2 + 2*m.x3 + m.x6 + m.x10 == 2)

m.c2 = Constraint(expr=   m.x4 + 2*m.x5 + m.x6 + m.x7 == 1)

m.c3 = Constraint(expr=   m.x3 + m.x7 + m.x8 + 2*m.x9 + m.x10 == 1)

m.c5 = Constraint(expr= - m.x1 - m.x2 - m.x3 - m.x4 - m.x5 - m.x6 - m.x7 - m.x8 - m.x9 - m.x10 + m.x11 == 0)
