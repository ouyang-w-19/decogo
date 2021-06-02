#  NLP written by GAMS Convert at 04/21/18 13:52:28
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        1        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          4        4        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          4        1        3        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(None,None),initialize=500)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=-150)
m.x4 = Var(within=Reals,bounds=(-5,5),initialize=-0.2)

m.obj = Objective(expr=(127 - exp(-5*m.x4)*m.x3 - m.x2)**2 + (151 - exp(-3*m.x4)*m.x3 - m.x2)**2 + (379 - exp(-m.x4)*
                       m.x3 - m.x2)**2 + (421 - exp(5*m.x4)*m.x3 - m.x2)**2 + (460 - exp(3*m.x4)*m.x3 - m.x2)**2 + (426
                        - exp(m.x4)*m.x3 - m.x2)**2, sense=minimize)
