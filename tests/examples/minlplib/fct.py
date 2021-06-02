#  DNLP written by GAMS Convert at 04/21/18 13:52:11
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         10       10        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         12       12        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         43       17       26        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(-10,5),initialize=2)
m.x9 = Var(within=Reals,bounds=(-10,5),initialize=2)
m.x10 = Var(within=Reals,bounds=(-10,5),initialize=2)
m.x11 = Var(within=Reals,bounds=(-10,5),initialize=2)
m.x12 = Var(within=Reals,bounds=(-10,5),initialize=2)

m.obj = Objective(expr=   2*m.x6 + m.x7, sense=minimize)

m.c2 = Constraint(expr=-(m.x8**2 + m.x9**2 + m.x10**2 + m.x11**2 + m.x12**2) + m.x7 == 0)

m.c3 = Constraint(expr= - m.x3 - m.x5 + m.x6 == 0)

m.c4 = Constraint(expr=-((m.x8**2 - m.x9)**2 + m.x10**2 + 2*m.x11**2 + (m.x12 - m.x9)**2) + m.x2 == 0)

m.c5 = Constraint(expr=-abs(sin(4*mod(m.x2,3.14159265358979))) + m.x3 == 0)

m.c6 = Constraint(expr=-((m.x8 + m.x9 - m.x10 + m.x11 - m.x12)**2 + 2*(m.x9 - m.x8 + m.x10 - m.x11 + m.x12)**2) + m.x4
                        == 0)

m.c7 = Constraint(expr=-abs(sin(3*mod(m.x4,3.14159265358979))) + m.x5 == 0)

m.c8 = Constraint(expr=3*m.x9**2 + m.x10**2 - 2*m.x11**2 + m.x12**2 + m.x8 == 0)

m.c9 = Constraint(expr=   m.x8 + 4*m.x9 - m.x10 + m.x11 - 3*m.x12 == 0)

m.c10 = Constraint(expr=m.x8**2 - m.x10**2 + 2*m.x9**2 - m.x11**2 - m.x12**2 == 0)
