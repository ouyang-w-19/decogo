#  NLP written by GAMS Convert at 04/21/18 13:51:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          6        2        0        4        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        5        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         20        8       12        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(1E-6,1),initialize=0.624)
m.x2 = Var(within=Reals,bounds=(1E-6,1),initialize=0.376)
m.x3 = Var(within=Reals,bounds=(20,80),initialize=58.129)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   m.x5, sense=minimize)

m.c2 = Constraint(expr=log(m.x1 + 0.191987347447993*m.x2) + m.x1/(m.x1 + 0.191987347447993*m.x2) + 0.315693799947296*
                       m.x2/(0.315693799947296*m.x1 + m.x2) + 3643.31361767678/(239.726 + m.x3) - m.x5
                        <= 12.9738026256517)

m.c3 = Constraint(expr=log(0.315693799947296*m.x1 + m.x2) + 0.191987347447993*m.x1/(m.x1 + 0.191987347447993*m.x2) + 
                       m.x2/(0.315693799947296*m.x1 + m.x2) + 2755.64173589155/(219.161 + m.x3) - m.x5
                        <= 10.2081676704566)

m.c4 = Constraint(expr=(-log(m.x1 + 0.191987347447993*m.x2)) - (m.x1/(m.x1 + 0.191987347447993*m.x2) + 0.315693799947296
                       *m.x2/(0.315693799947296*m.x1 + m.x2)) - 3643.31361767678/(239.726 + m.x3) - m.x5
                        <= -12.9738026256517)

m.c5 = Constraint(expr=(-log(0.315693799947296*m.x1 + m.x2)) - (0.191987347447993*m.x1/(m.x1 + 0.191987347447993*m.x2)
                        + m.x2/(0.315693799947296*m.x1 + m.x2)) - 2755.64173589155/(219.161 + m.x3) - m.x5
                        <= -10.2081676704566)

m.c6 = Constraint(expr=   m.x1 + m.x2 == 1)
