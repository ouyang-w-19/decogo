#  NLP written by GAMS Convert at 04/21/18 13:54:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          8        1        7        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          9        9        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         23       15        8        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x2 = Var(within=Reals,bounds=(-2.1,2),initialize=0)
m.x3 = Var(within=Reals,bounds=(-3.2,3),initialize=0)
m.x4 = Var(within=Reals,bounds=(-4.3,4),initialize=0)
m.x5 = Var(within=Reals,bounds=(-5.4,5),initialize=0)
m.x6 = Var(within=Reals,bounds=(-6.5,6),initialize=0)
m.x7 = Var(within=Reals,bounds=(-7.6,7),initialize=0)
m.x8 = Var(within=Reals,bounds=(-8.7,8),initialize=0)

m.obj = Objective(expr=1.69*m.x1*m.x1 + 7*m.x1 + m.x1*m.x2 + 6*m.x2 + 2*m.x1*m.x3 + 5*m.x3 + 3*m.x1*m.x4 + 4*m.x4 + 4*
                       m.x1*m.x5 + 3*m.x5 + 5*m.x1*m.x6 + 2*m.x6 + 6*m.x1*m.x7 + m.x7 + 7*m.x1*m.x8 + m.x2*m.x1 + 1.69*
                       m.x2*m.x2 + m.x2*m.x3 + 2*m.x2*m.x4 + 3*m.x2*m.x5 + 4*m.x2*m.x6 + 5*m.x2*m.x7 + 6*m.x2*m.x8 + 2*
                       m.x3*m.x1 + m.x3*m.x2 + 1.69*m.x3*m.x3 + m.x3*m.x4 + 2*m.x3*m.x5 + 3*m.x3*m.x6 + 4*m.x3*m.x7 + 5*
                       m.x3*m.x8 + 3*m.x4*m.x1 + 2*m.x4*m.x2 + m.x4*m.x3 + 1.69*m.x4*m.x4 + m.x4*m.x5 + 2*m.x4*m.x6 + 3*
                       m.x4*m.x7 + 4*m.x4*m.x8 + 4*m.x5*m.x1 + 3*m.x5*m.x2 + 2*m.x5*m.x3 + m.x5*m.x4 + 1.69*m.x5*m.x5 + 
                       m.x5*m.x6 + 2*m.x5*m.x7 + 3*m.x5*m.x8 + 5*m.x6*m.x1 + 4*m.x6*m.x2 + 3*m.x6*m.x3 + 2*m.x6*m.x4 + 
                       m.x6*m.x5 + 1.69*m.x6*m.x6 + m.x6*m.x7 + 2*m.x6*m.x8 + 6*m.x7*m.x1 + 5*m.x7*m.x2 + 4*m.x7*m.x3 + 
                       3*m.x7*m.x4 + 2*m.x7*m.x5 + m.x7*m.x6 + 1.69*m.x7*m.x7 + m.x7*m.x8 + 7*m.x8*m.x1 + 6*m.x8*m.x2 + 
                       5*m.x8*m.x3 + 4*m.x8*m.x4 + 3*m.x8*m.x5 + 2*m.x8*m.x6 + m.x8*m.x7 + 1.69*m.x8*m.x8
                       , sense=minimize)

m.c1 = Constraint(expr= - m.x1 + m.x2 >= -1)

m.c2 = Constraint(expr= - m.x2 + m.x3 >= -1.05)

m.c3 = Constraint(expr= - m.x3 + m.x4 >= -1.1)

m.c4 = Constraint(expr= - m.x4 + m.x5 >= -1.15)

m.c5 = Constraint(expr= - m.x5 + m.x6 >= -1.2)

m.c6 = Constraint(expr= - m.x6 + m.x7 >= -1.25)

m.c7 = Constraint(expr= - m.x7 + m.x8 >= -1.3)
