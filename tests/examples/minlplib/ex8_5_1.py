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


m.x2 = Var(within=Reals,bounds=(0,None),initialize=0.333333333333333)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0.333333333333333)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0.333333333333333)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=2)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=1)

m.obj = Objective(expr=log(m.x2)*m.x2 + log(m.x3)*m.x3 + log(m.x4)*m.x4 + m.x7/(m.x5 - m.x7) - log(m.x5 - m.x7) - 2*m.x6
                       /m.x5 + 0.430983578191493*m.x2 + 3.80082402249182*m.x3 + 2.92297302249182*m.x4, sense=minimize)

m.c2 = Constraint(expr=m.x5**3 - m.x5**2*(1 + m.x7) + m.x6*m.x5 - m.x6*m.x7 == 0)

m.c3 = Constraint(expr=-(0.37943*m.x2*m.x2 + 0.75885*m.x2*m.x3 + 0.48991*m.x2*m.x4 + 0.75885*m.x3*m.x2 + 0.8836*m.x3*
                       m.x3 + 0.23612*m.x3*m.x4 + 0.48991*m.x4*m.x2 + 0.23612*m.x4*m.x3 + 0.63263*m.x4*m.x4) + m.x6
                        == 0)

m.c4 = Constraint(expr= - 0.14998*m.x2 - 0.14998*m.x3 - 0.14998*m.x4 + m.x7 == 0)

m.c5 = Constraint(expr=   m.x2 + m.x3 + m.x4 == 1)
