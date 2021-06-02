#  NLP written by GAMS Convert at 04/21/18 13:51:12
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         13       10        1        2        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         14       14        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         41       13       28        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(1,16),initialize=6)
m.x2 = Var(within=Reals,bounds=(1,16),initialize=5)
m.x3 = Var(within=Reals,bounds=(1,16),initialize=6)
m.x4 = Var(within=Reals,bounds=(1,16),initialize=3)
m.x6 = Var(within=Reals,bounds=(1,1000),initialize=1000)
m.x7 = Var(within=Reals,bounds=(0.0001,None),initialize=1.6)
m.x8 = Var(within=Reals,bounds=(0.0001,None),initialize=0.3)
m.x9 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x10 = Var(within=Reals,bounds=(None,50),initialize=50)
m.x11 = Var(within=Reals,bounds=(100,None),initialize=600)
m.x12 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x13 = Var(within=Reals,bounds=(0.0001,None),initialize=0.0001)
m.x14 = Var(within=Reals,bounds=(0.01,None),initialize=0.01)

m.obj = Objective(expr=   m.x7 + m.x8, sense=minimize)

m.c2 = Constraint(expr=-1.42857142857143*m.x4*m.x6 + 10000*m.x8 == 0)

m.c3 = Constraint(expr=10*m.x7*m.x9 - 0.00968946189201592*(m.x1**4 - m.x2**4)*m.x3 == 0)

m.c4 = Constraint(expr=143.3076*m.x10*m.x4 - 10000*m.x7 == 0)

m.c5 = Constraint(expr=3.1415927*(0.001*m.x9)**3*m.x6 - 6e-6*m.x3*m.x4*m.x13 == 0)

m.c6 = Constraint(expr=101000*m.x12*m.x13 - 1.57079635*m.x6*m.x14 == 0)

m.c7 = Constraint(expr=log10(0.8 + 8.112*m.x3) - 10964781961.4318*m.x11**(-3.55) == 0)

m.c8 = Constraint(expr= - 0.5*m.x10 + m.x11 == 560)

m.c9 = Constraint(expr=   m.x1 - m.x2 >= 0)

m.c10 = Constraint(expr=0.0307*m.x4**2 - 0.3864*(0.0062831854*m.x1*m.x9)**2*m.x6 <= 0)

m.c11 = Constraint(expr=   101000*m.x12 - 15707.9635*m.x14 <= 0)

m.c12 = Constraint(expr=-(log(m.x1) - log(m.x2)) + m.x13 == 0)

m.c13 = Constraint(expr=-(m.x1**2 - m.x2**2) + m.x14 == 0)
