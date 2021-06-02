#  NLP written by GAMS Convert at 04/21/18 13:51:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          8        2        0        6        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          6        6        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         35       11       24        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(1E-6,1),initialize=0.272)
m.x2 = Var(within=Reals,bounds=(1E-6,1),initialize=0.465)
m.x3 = Var(within=Reals,bounds=(1E-6,1),initialize=0.253)
m.x4 = Var(within=Reals,bounds=(20,80),initialize=54.254)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   m.x6, sense=minimize)

m.c2 = Constraint(expr=log(m.x1 + 0.48*m.x2 + 0.768*m.x3) + m.x1/(m.x1 + 0.48*m.x2 + 0.768*m.x3) + 1.55*m.x2/(1.55*m.x1
                        + m.x2 + 0.544*m.x3) + 0.566*m.x3/(0.566*m.x1 + 0.65*m.x2 + m.x3) + 2787.49800065313/(229.664 + 
                       m.x4) - m.x6 <= 10.7545020354713)

m.c3 = Constraint(expr=log(1.55*m.x1 + m.x2 + 0.544*m.x3) + 0.48*m.x1/(m.x1 + 0.48*m.x2 + 0.768*m.x3) + m.x2/(1.55*m.x1
                        + m.x2 + 0.544*m.x3) + 0.65*m.x3/(0.566*m.x1 + 0.65*m.x2 + m.x3) + 2665.5415812027/(219.726 + 
                       m.x4) - m.x6 <= 10.6349978691449)

m.c4 = Constraint(expr=log(0.566*m.x1 + 0.65*m.x2 + m.x3) + 0.768*m.x1/(m.x1 + 0.48*m.x2 + 0.768*m.x3) + 0.544*m.x2/(
                       1.55*m.x1 + m.x2 + 0.544*m.x3) + m.x3/(0.566*m.x1 + 0.65*m.x2 + m.x3) + 3643.31361767678/(239.726
                        + m.x4) - m.x6 <= 12.9738026256517)

m.c5 = Constraint(expr=(-log(m.x1 + 0.48*m.x2 + 0.768*m.x3)) - (m.x1/(m.x1 + 0.48*m.x2 + 0.768*m.x3) + 1.55*m.x2/(1.55*
                       m.x1 + m.x2 + 0.544*m.x3) + 0.566*m.x3/(0.566*m.x1 + 0.65*m.x2 + m.x3)) - 2787.49800065313/(
                       229.664 + m.x4) - m.x6 <= -10.7545020354713)

m.c6 = Constraint(expr=(-log(1.55*m.x1 + m.x2 + 0.544*m.x3)) - (0.48*m.x1/(m.x1 + 0.48*m.x2 + 0.768*m.x3) + m.x2/(1.55*
                       m.x1 + m.x2 + 0.544*m.x3) + 0.65*m.x3/(0.566*m.x1 + 0.65*m.x2 + m.x3)) - 2665.5415812027/(219.726
                        + m.x4) - m.x6 <= -10.6349978691449)

m.c7 = Constraint(expr=(-log(0.566*m.x1 + 0.65*m.x2 + m.x3)) - (0.768*m.x1/(m.x1 + 0.48*m.x2 + 0.768*m.x3) + 0.544*m.x2/
                       (1.55*m.x1 + m.x2 + 0.544*m.x3) + m.x3/(0.566*m.x1 + 0.65*m.x2 + m.x3)) - 3643.31361767678/(
                       239.726 + m.x4) - m.x6 <= -12.9738026256517)

m.c8 = Constraint(expr=   m.x1 + m.x2 + m.x3 == 1)
