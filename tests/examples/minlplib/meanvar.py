#  NLP written by GAMS Convert at 04/21/18 13:52:31
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          3        3        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          9        9        0        0        0        0        0        0
#  FX      1        1        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         23       16        7        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0.115,0.115),initialize=0.115)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=0)

m.obj = Objective(expr=0.5*(42.18*m.x3*m.x3 + 20.18*m.x3*m.x4 + 10.88*m.x3*m.x5 + 5.3*m.x3*m.x6 + 12.32*m.x3*m.x7 + 
                       23.84*m.x3*m.x8 + 17.41*m.x3*m.x9 + 20.18*m.x4*m.x3 + 70.89*m.x4*m.x4 + 21.58*m.x4*m.x5 + 15.41*
                       m.x4*m.x6 + 23.24*m.x4*m.x7 + 23.8*m.x4*m.x8 + 12.62*m.x4*m.x9 + 10.88*m.x5*m.x3 + 21.58*m.x5*
                       m.x4 + 25.51*m.x5*m.x5 + 9.6*m.x5*m.x6 + 22.63*m.x5*m.x7 + 13.22*m.x5*m.x8 + 4.7*m.x5*m.x9 + 5.3*
                       m.x6*m.x3 + 15.41*m.x6*m.x4 + 9.6*m.x6*m.x5 + 22.33*m.x6*m.x6 + 10.32*m.x6*m.x7 + 10.46*m.x6*m.x8
                        + m.x6*m.x9 + 12.32*m.x7*m.x3 + 23.24*m.x7*m.x4 + 22.63*m.x7*m.x5 + 10.32*m.x7*m.x6 + 30.01*m.x7
                       *m.x7 + 16.36*m.x7*m.x8 + 7.2*m.x7*m.x9 + 23.84*m.x8*m.x3 + 23.8*m.x8*m.x4 + 13.22*m.x8*m.x5 + 
                       10.46*m.x8*m.x6 + 16.36*m.x8*m.x7 + 42.23*m.x8*m.x8 + 9.9*m.x8*m.x9 + 17.41*m.x9*m.x3 + 12.62*
                       m.x9*m.x4 + 4.7*m.x9*m.x5 + m.x9*m.x6 + 7.2*m.x9*m.x7 + 9.9*m.x9*m.x8 + 16.42*m.x9*m.x9)
                       , sense=minimize)

m.c2 = Constraint(expr=   m.x2 - 0.1287*m.x3 - 0.1096*m.x4 - 0.0501*m.x5 - 0.1524*m.x6 - 0.0763*m.x7 - 0.1854*m.x8
                        - 0.062*m.x9 == 0)

m.c3 = Constraint(expr=   m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 == 1)
