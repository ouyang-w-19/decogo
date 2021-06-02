#  NLP written by GAMS Convert at 04/21/18 13:52:30
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        1        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          3        3        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          3        1        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(-3,3),initialize=-0.655668942)
m.x2 = Var(within=Reals,bounds=(-3,3),initialize=0.346914252)

m.obj = Objective(expr=exp(sin(50*m.x1)) + sin(60*exp(m.x2)) + sin(70*sin(m.x1)) + sin(sin(80*m.x2)) - sin(10*m.x1 + 10*
                       m.x2) + 0.25*(m.x1**2 + m.x2**2), sense=minimize)
