#  NLP written by GAMS Convert at 04/21/18 13:51:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         18        2        0       16        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         11       11        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        118       18      100        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   m.x10, sense=minimize)

m.c2 = Constraint(expr=(1 - m.x1*m.x2)*m.x3*(-1 + exp(m.x5*(0.485 - 0.0052095*m.x7 - 0.0285132*m.x8))) + 23.3037*m.x2
                        - m.x10 <= 28.5132)

m.c3 = Constraint(expr=(1 - m.x1*m.x2)*m.x3*(-1 + exp(m.x5*(0.752 - 0.0100677*m.x7 - 0.1118467*m.x8))) + 101.779*m.x2
                        - m.x10 <= 111.8467)

m.c4 = Constraint(expr=(1 - m.x1*m.x2)*m.x3*(-1 + exp(m.x5*(0.869 - 0.0229274*m.x7 - 0.1343884*m.x8))) + 111.461*m.x2
                        - m.x10 <= 134.3884)

m.c5 = Constraint(expr=(1 - m.x1*m.x2)*m.x3*(-1 + exp(m.x5*(0.982 - 0.0202153*m.x7 - 0.2114823*m.x8))) + 191.267*m.x2
                        - m.x10 <= 211.4823)

m.c6 = Constraint(expr=(-(1 - m.x1*m.x2)*m.x3*(-1 + exp(m.x5*(0.485 - 0.0052095*m.x7 - 0.0285132*m.x8)))) - 23.3037*m.x2
                        - m.x10 <= -28.5132)

m.c7 = Constraint(expr=(-(1 - m.x1*m.x2)*m.x3*(-1 + exp(m.x5*(0.752 - 0.0100677*m.x7 - 0.1118467*m.x8)))) - 101.779*m.x2
                        - m.x10 <= -111.8467)

m.c8 = Constraint(expr=(-(1 - m.x1*m.x2)*m.x3*(-1 + exp(m.x5*(0.869 - 0.0229274*m.x7 - 0.1343884*m.x8)))) - 111.461*m.x2
                        - m.x10 <= -134.3884)

m.c9 = Constraint(expr=(-(1 - m.x1*m.x2)*m.x3*(-1 + exp(m.x5*(0.982 - 0.0202153*m.x7 - 0.2114823*m.x8)))) - 191.267*m.x2
                        - m.x10 <= -211.4823)

m.c10 = Constraint(expr=(1 - m.x1*m.x2)*m.x4*(-1 + exp(m.x6*(0.116 - 0.0052095*m.x7 + 0.0233037*m.x9))) - 28.5132*m.x1
                         - m.x10 <= -23.3037)

m.c11 = Constraint(expr=(1 - m.x1*m.x2)*m.x4*(-1 + exp(m.x6*(-0.502 - 0.0100677*m.x7 + 0.101779*m.x9))) - 111.8467*m.x1
                         - m.x10 <= -101.779)

m.c12 = Constraint(expr=(1 - m.x1*m.x2)*m.x4*(-1 + exp(m.x6*(0.166 - 0.0229274*m.x7 + 0.111461*m.x9))) - 134.3884*m.x1
                         - m.x10 <= -111.461)

m.c13 = Constraint(expr=(1 - m.x1*m.x2)*m.x4*(-1 + exp(m.x6*(-0.473 - 0.0202153*m.x7 + 0.191267*m.x9))) - 211.4823*m.x1
                         - m.x10 <= -191.267)

m.c14 = Constraint(expr=28.5132*m.x1 - (1 - m.x1*m.x2)*m.x4*(-1 + exp(m.x6*(0.116 - 0.0052095*m.x7 + 0.0233037*m.x9)))
                         - m.x10 <= 23.3037)

m.c15 = Constraint(expr=111.8467*m.x1 - (1 - m.x1*m.x2)*m.x4*(-1 + exp(m.x6*(-0.502 - 0.0100677*m.x7 + 0.101779*m.x9)))
                         - m.x10 <= 101.779)

m.c16 = Constraint(expr=134.3884*m.x1 - (1 - m.x1*m.x2)*m.x4*(-1 + exp(m.x6*(0.166 - 0.0229274*m.x7 + 0.111461*m.x9)))
                         - m.x10 <= 111.461)

m.c17 = Constraint(expr=211.4823*m.x1 - (1 - m.x1*m.x2)*m.x4*(-1 + exp(m.x6*(-0.473 - 0.0202153*m.x7 + 0.191267*m.x9)))
                         - m.x10 <= 191.267)

m.c18 = Constraint(expr=m.x1*m.x3 - m.x2*m.x4 == 0)
