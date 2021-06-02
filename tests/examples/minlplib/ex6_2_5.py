#  NLP written by GAMS Convert at 04/21/18 13:51:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          4        4        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         10       10        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         19       10        9        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(1E-7,40.30707),initialize=31.459)
m.x3 = Var(within=Reals,bounds=(1E-7,40.30707),initialize=0.901998)
m.x4 = Var(within=Reals,bounds=(1E-7,40.30707),initialize=1E-7)
m.x5 = Var(within=Reals,bounds=(1E-7,5.14979),initialize=3.10348)
m.x6 = Var(within=Reals,bounds=(1E-7,5.14979),initialize=9.6E-6)
m.x7 = Var(within=Reals,bounds=(1E-7,5.14979),initialize=1E-7)
m.x8 = Var(within=Reals,bounds=(1E-7,54.54314),initialize=26.1669)
m.x9 = Var(within=Reals,bounds=(1E-7,54.54314),initialize=15.0141)
m.x10 = Var(within=Reals,bounds=(1E-7,54.54314),initialize=1E-7)

m.obj = Objective(expr=(0.156969560191053 + log(m.x4/(m.x4 + m.x7 + m.x10)))*m.x4 + (0.156969560191053 + log(m.x7/(m.x4
                        + m.x7 + m.x10)))*m.x7 + (0.156969560191053 + log(m.x10/(m.x4 + m.x7 + m.x10)))*m.x10 + log(
                       3.9235*m.x2 + 6.0909*m.x5 + 0.92*m.x8)*(26.9071667605344*m.x2 + 41.7710875549227*m.x5 + 
                       6.30931398488382*m.x8) + 0.113370955614741*m.x2 - 2.43897680885457*m.x5 + 2.8555953099828*m.x8 + 
                       9.58716676053442*log(m.x2)*m.x2 + 16.9310875549227*log(m.x5)*m.x5 + 0.309313984883821*log(m.x8)*
                       m.x8 - 9.58716676053442*log(3.9235*m.x2 + 6.0909*m.x5 + 0.92*m.x8)*m.x2 - 16.9310875549227*log(
                       3.9235*m.x2 + 6.0909*m.x5 + 0.92*m.x8)*m.x5 - 0.309313984883821*log(3.9235*m.x2 + 6.0909*m.x5 + 
                       0.92*m.x8)*m.x8 + 18.32*log(m.x2)*m.x2 + 25.84*log(m.x5)*m.x5 + 7*log(m.x8)*m.x8 - 18.32*log(
                       3.664*m.x2 + 5.168*m.x5 + 1.4*m.x8)*m.x2 - 25.84*log(3.664*m.x2 + 5.168*m.x5 + 1.4*m.x8)*m.x5 - 7
                       *log(3.664*m.x2 + 5.168*m.x5 + 1.4*m.x8)*m.x8 + log(4.0643*m.x2 + 5.7409*m.x5 + 1.6741*m.x8)*(
                       4.0643*m.x2 + 5.7409*m.x5 + 1.6741*m.x8) + 4.0643*log(m.x2)*m.x2 + 5.7409*log(m.x5)*m.x5 + 1.6741
                       *log(m.x8)*m.x8 - 4.0643*log(4.0643*m.x2 + 3.22644664511275*m.x5 + 1.44980651607875*m.x8)*m.x2 - 
                       5.7409*log(5.31147575751424*m.x2 + 5.7409*m.x5 + 0.00729924451284409*m.x8)*m.x5 - 1.6741*log(
                       2.25846661774355*m.x2 + 3.70876916588753*m.x5 + 1.6741*m.x8)*m.x8 + log(3.9235*m.x3 + 6.0909*m.x6
                        + 0.92*m.x9)*(26.9071667605344*m.x3 + 41.7710875549227*m.x6 + 6.30931398488382*m.x9) + 
                       0.113370955614741*m.x3 - 2.43897680885457*m.x6 + 2.8555953099828*m.x9 + 9.58716676053442*log(m.x3
                       )*m.x3 + 16.9310875549227*log(m.x6)*m.x6 + 0.309313984883821*log(m.x9)*m.x9 - 9.58716676053442*
                       log(3.9235*m.x3 + 6.0909*m.x6 + 0.92*m.x9)*m.x3 - 16.9310875549227*log(3.9235*m.x3 + 6.0909*m.x6
                        + 0.92*m.x9)*m.x6 - 0.309313984883821*log(3.9235*m.x3 + 6.0909*m.x6 + 0.92*m.x9)*m.x9 + 18.32*
                       log(m.x3)*m.x3 + 25.84*log(m.x6)*m.x6 + 7*log(m.x9)*m.x9 - 18.32*log(3.664*m.x3 + 5.168*m.x6 + 
                       1.4*m.x9)*m.x3 - 25.84*log(3.664*m.x3 + 5.168*m.x6 + 1.4*m.x9)*m.x6 - 7*log(3.664*m.x3 + 5.168*
                       m.x6 + 1.4*m.x9)*m.x9 + log(4.0643*m.x3 + 5.7409*m.x6 + 1.6741*m.x9)*(4.0643*m.x3 + 5.7409*m.x6
                        + 1.6741*m.x9) + 4.0643*log(m.x3)*m.x3 + 5.7409*log(m.x6)*m.x6 + 1.6741*log(m.x9)*m.x9 - 4.0643*
                       log(4.0643*m.x3 + 3.22644664511275*m.x6 + 1.44980651607875*m.x9)*m.x3 - 5.7409*log(
                       5.31147575751424*m.x3 + 5.7409*m.x6 + 0.00729924451284409*m.x9)*m.x6 - 1.6741*log(
                       2.25846661774355*m.x3 + 3.70876916588753*m.x6 + 1.6741*m.x9)*m.x9 - 0.3658348*m.x2 - 0.3658348*
                       m.x3 - 0.9825555*m.x5 - 0.9825555*m.x6 - 0.3663657*m.x8 - 0.3663657*m.x9 - 30.9714667605344*log(
                       m.x2)*m.x2 - 47.5119875549227*log(m.x5)*m.x5 - 7.98341398488382*log(m.x8)*m.x8 - 30.9714667605344
                       *log(m.x3)*m.x3 - 47.5119875549227*log(m.x6)*m.x6 - 7.98341398488382*log(m.x9)*m.x9
                       , sense=minimize)

m.c2 = Constraint(expr=   m.x2 + m.x3 + m.x4 == 40.30707)

m.c3 = Constraint(expr=   m.x5 + m.x6 + m.x7 == 5.14979)

m.c4 = Constraint(expr=   m.x8 + m.x9 + m.x10 == 54.54314)
