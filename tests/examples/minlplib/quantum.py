#  DNLP written by GAMS Convert at 04/21/18 13:54:02
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


m.x2 = Var(within=Reals,bounds=(0.0001,10),initialize=1)
m.x3 = Var(within=Reals,bounds=(0.001,10),initialize=1)

m.obj = Objective(expr=0.5*m.x3**2*Gamma(2 - 0.5/m.x3)/Gamma(0.5/m.x3)*m.x2**(1/m.x3) + 0.5*Gamma(1.5/m.x3)/Gamma(0.5/
                       m.x3)*m.x2**(-1/m.x3) + Gamma(2.5/m.x3)/Gamma(0.5/m.x3)*m.x2**(-2/m.x3), sense=minimize)
