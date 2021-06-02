#  NLP written by GAMS Convert at 04/21/18 13:54:00
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


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(-100,100),initialize=2.28067255148468E-6)
m.x2 = Var(within=Reals,bounds=(-2,2),initialize=0.999139149741104)
m.x3 = Var(within=Reals,bounds=(-2,2),initialize=0.998154959548312)

m.obj = Objective(expr=m.x1, sense=minimize)

m.c1 = Constraint(expr=100*(m.x3 - m.x2**2)**2 + (1 - m.x2)**2 - m.x1 == 0)
