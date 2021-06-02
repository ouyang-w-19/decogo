#  NLP written by GAMS Convert at 04/21/18 13:51:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          2        2        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          4        4        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          7        4        3        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(1E-6,1),initialize=0.51802)
m.x3 = Var(within=Reals,bounds=(1E-6,1),initialize=0.0511)
m.x4 = Var(within=Reals,bounds=(1E-6,1),initialize=0.43088)

m.obj = Objective(expr=log(3.9235*m.x2 + 6.0909*m.x3 + 0.92*m.x4)*(26.9071667605344*m.x2 + 41.7710875549227*m.x3 + 
                       6.30931398488382*m.x4) + 0.668686155614739*m.x2 - 1.14374230885457*m.x3 + 2.8906196099828*m.x4 + 
                       9.58716676053442*log(m.x2)*m.x2 + 16.9310875549227*log(m.x3)*m.x3 + 0.309313984883821*log(m.x4)*
                       m.x4 - 9.58716676053442*log(3.9235*m.x2 + 6.0909*m.x3 + 0.92*m.x4)*m.x2 - 16.9310875549227*log(
                       3.9235*m.x2 + 6.0909*m.x3 + 0.92*m.x4)*m.x3 - 0.309313984883821*log(3.9235*m.x2 + 6.0909*m.x3 + 
                       0.92*m.x4)*m.x4 + 18.32*log(m.x2)*m.x2 + 25.84*log(m.x3)*m.x3 + 7*log(m.x4)*m.x4 - 18.32*log(
                       3.664*m.x2 + 5.168*m.x3 + 1.4*m.x4)*m.x2 - 25.84*log(3.664*m.x2 + 5.168*m.x3 + 1.4*m.x4)*m.x3 - 7
                       *log(3.664*m.x2 + 5.168*m.x3 + 1.4*m.x4)*m.x4 + log(4.0643*m.x2 + 5.7409*m.x3 + 1.6741*m.x4)*(
                       4.0643*m.x2 + 5.7409*m.x3 + 1.6741*m.x4) + 4.0643*log(m.x2)*m.x2 + 5.7409*log(m.x3)*m.x3 + 1.6741
                       *log(m.x4)*m.x4 - 4.0643*log(4.0643*m.x2 + 3.22644664511275*m.x3 + 1.44980651607875*m.x4)*m.x2 - 
                       5.7409*log(5.31147575751424*m.x2 + 5.7409*m.x3 + 0.00729924451284409*m.x4)*m.x3 - 1.6741*log(
                       2.25846661774355*m.x2 + 3.70876916588753*m.x3 + 1.6741*m.x4)*m.x4 - 30.9714667605344*log(m.x2)*
                       m.x2 - 47.5119875549227*log(m.x3)*m.x3 - 7.98341398488382*log(m.x4)*m.x4, sense=minimize)

m.c2 = Constraint(expr=   m.x2 + m.x3 + m.x4 == 1)
