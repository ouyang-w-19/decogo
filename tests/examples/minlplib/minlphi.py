#  NLP written by GAMS Convert at 04/21/18 13:52:35
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         80       28        0       52        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         65       65        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        207      171       36        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,None),initialize=396)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(326,None),initialize=390)
m.x31 = Var(within=Reals,bounds=(0,304),initialize=0)
m.x32 = Var(within=Reals,bounds=(326,None),initialize=360)
m.x33 = Var(within=Reals,bounds=(0,304),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,1000),initialize=410)
m.x35 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,1000),initialize=380)
m.x37 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=76)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=26)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=0.4*((-1.15398 + 0.003375*m.x30)*m.x2 + (-0.30630793 + 0.000893*m.x31)*m.x3 + (-1.57608132 + 
                       0.004458*m.x32)*m.x4 + (-1.08593792 + 0.003176*m.x33)*m.x5 + 31.8928571428571*m.x14/(m.x30 - 
                       m.x36) + 31.8928571428571*m.x15/(1 + m.x31 - m.x37) + 31.8928571428571*m.x16/(m.x32 - m.x34) + 
                       31.8928571428571*m.x17/(1 + m.x33 - m.x35) + 31.8928571428571*m.x26/m.x38 + 31.8928571428571*
                       m.x27/(1 + m.x39) + 31.8928571428571*m.x28/m.x40 + 31.8928571428571*m.x29/(1 + m.x41) + 
                       31.8928571428571*m.x18/(421 - m.x34) + 31.8928571428571*m.x19/(421 - m.x35) + 31.8928571428571*
                       m.x20/(421 - m.x36) + 31.8928571428571*m.x21/(421 - m.x37) + 31.8928571428571*m.x22/(373 - m.x34)
                        + 31.8928571428571*m.x23/(373 - m.x35) + 31.8928571428571*m.x24/(373 - m.x36) + 31.8928571428571
                       *m.x25/(373 - m.x37)) + 12.95216*m.x18 + 12.95216*m.x19 + 12.95216*m.x20 + 12.95216*m.x21 + 
                       4.75228*m.x22 + 4.75228*m.x23 + 4.75228*m.x24 + 4.75228*m.x25 + 2.418*m.x26 + 2.418*m.x27 + 2.418
                       *m.x28 + 2.418*m.x29 + 67.56864, sense=minimize)

m.c2 = Constraint(expr=(-0.666666666666667*sqrt((-305 + m.x30)*(-325 + m.x30))) - 0.333333333333333*m.x30 + m.x38
                        - m.x42 + m.x46 == -105)

m.c3 = Constraint(expr=(-0.666666666666667*sqrt((-305 + m.x31)*(-325 + m.x31))) - 0.333333333333333*m.x31 + m.x39
                        - m.x43 + m.x47 == -105)

m.c4 = Constraint(expr=(-0.666666666666667*sqrt((-305 + m.x32)*(-325 + m.x32))) - 0.333333333333333*m.x32 + m.x40
                        - m.x44 + m.x48 == -105)

m.c5 = Constraint(expr=(-0.666666666666667*sqrt((-305 + m.x33)*(-325 + m.x33))) - 0.333333333333333*m.x33 + m.x41
                        - m.x45 + m.x49 == -105)

m.c6 = Constraint(expr=   m.x42 + m.x50 + m.x54 <= 0)

m.c7 = Constraint(expr=   m.x43 + m.x51 + m.x55 <= 1500)

m.c8 = Constraint(expr=   m.x44 + m.x52 + m.x56 <= 0)

m.c9 = Constraint(expr=   m.x45 + m.x53 + m.x57 <= 1500)

m.c10 = Constraint(expr=   m.x46 + m.x58 + m.x62 <= 0)

m.c11 = Constraint(expr=   m.x47 + m.x59 + m.x63 <= 1500)

m.c12 = Constraint(expr=   m.x48 + m.x60 + m.x64 <= 0)

m.c13 = Constraint(expr=   m.x49 + m.x61 + m.x65 <= 1500)

m.c14 = Constraint(expr=   m.x30 + m.x34 + m.x38 <= 1500)

m.c15 = Constraint(expr=   m.x31 + m.x35 + m.x39 <= 0)

m.c16 = Constraint(expr=   m.x32 + m.x36 + m.x40 <= 1500)

m.c17 = Constraint(expr=   m.x33 + m.x37 + m.x41 <= 0)

m.c18 = Constraint(expr=   0.9*m.x3 - m.x5 == 0)

m.c19 = Constraint(expr=   0.2*m.x2 - m.x4 == 0)

m.c20 = Constraint(expr=   m.x2 + m.x3 == 396)

m.c21 = Constraint(expr=   m.x2 <= 1500)

m.c22 = Constraint(expr=   m.x3 <= 0)

m.c23 = Constraint(expr=   m.x4 <= 1500)

m.c24 = Constraint(expr=   m.x5 <= 0)

m.c25 = Constraint(expr=   m.x10 - 0.0225*m.x30 - m.x58 + m.x62 == 24.7068)

m.c26 = Constraint(expr=   m.x11 - 0.013*m.x31 - m.x59 + m.x63 == 20.54087)

m.c27 = Constraint(expr=   m.x12 - 0.0043*m.x32 - m.x60 + m.x64 == 2.239778)

m.c28 = Constraint(expr=   m.x13 - 0.0156*m.x33 - m.x61 + m.x65 == 29.766048)

m.c29 = Constraint(expr=   m.x6 - m.x10 == 0)

m.c30 = Constraint(expr=   m.x7 - m.x11 == 0)

m.c31 = Constraint(expr=   m.x8 - m.x12 == 0)

m.c32 = Constraint(expr=   m.x9 - m.x13 == 0)

m.c33 = Constraint(expr=   m.x10 - m.x14 - m.x26 == 0)

m.c34 = Constraint(expr=   m.x11 - m.x15 - m.x27 == 0)

m.c35 = Constraint(expr=   m.x12 - m.x16 - m.x28 == 0)

m.c36 = Constraint(expr=   m.x13 - m.x17 - m.x29 == 0)

m.c37 = Constraint(expr=   m.x6 - m.x16 - m.x18 - m.x22 == 0)

m.c38 = Constraint(expr=   m.x7 - m.x17 - m.x19 - m.x23 == 0)

m.c39 = Constraint(expr=   m.x8 - m.x14 - m.x20 - m.x24 == 0)

m.c40 = Constraint(expr=   m.x9 - m.x15 - m.x21 - m.x25 == 0)

m.c41 = Constraint(expr= - m.x30 <= -341.92)

m.c42 = Constraint(expr= - m.x31 <= 1156.99)

m.c43 = Constraint(expr= - m.x32 <= -353.54)

m.c44 = Constraint(expr= - m.x33 <= 1158.08)

m.c45 = Constraint(expr=   m.x34 <= 411)

m.c46 = Constraint(expr=   m.x35 <= 411)

m.c47 = Constraint(expr=   m.x36 <= 411)

m.c48 = Constraint(expr=   m.x37 <= 411)

m.c49 = Constraint(expr= - 1.028*m.x30 + m.x34 - m.x50 + m.x54 == -341.95276)

m.c50 = Constraint(expr= - 1.05*m.x31 + m.x35 - m.x51 + m.x55 == -347.9205)

m.c51 = Constraint(expr= - 1.029*m.x32 + m.x36 - m.x52 + m.x56 == -355.03666)

m.c52 = Constraint(expr= - 1.005*m.x33 + m.x37 - m.x53 + m.x57 == -334.4486)

m.c53 = Constraint(expr= - m.x30 + m.x36 <= -10)

m.c54 = Constraint(expr= - m.x31 + m.x37 <= 1490)

m.c55 = Constraint(expr= - m.x32 + m.x34 <= 1490)

m.c56 = Constraint(expr= - m.x33 + m.x35 <= 1490)

m.c57 = Constraint(expr=   m.x34 <= 1863)

m.c58 = Constraint(expr=   m.x35 <= 1863)

m.c59 = Constraint(expr=   m.x36 <= 1863)

m.c60 = Constraint(expr=   m.x37 <= 1863)

m.c61 = Constraint(expr=   m.x14 <= 1500)

m.c62 = Constraint(expr=   m.x15 <= 0)

m.c63 = Constraint(expr=   m.x16 <= 0)

m.c64 = Constraint(expr=   m.x17 <= 0)

m.c65 = Constraint(expr=   m.x18 <= 1500)

m.c66 = Constraint(expr=   m.x19 <= 0)

m.c67 = Constraint(expr=   m.x20 <= 0)

m.c68 = Constraint(expr=   m.x21 <= 0)

m.c69 = Constraint(expr=   m.x22 <= 0)

m.c70 = Constraint(expr=   m.x23 <= 0)

m.c71 = Constraint(expr=   m.x24 <= 0)

m.c72 = Constraint(expr=   m.x25 <= 0)

m.c73 = Constraint(expr=   m.x26 <= 1500)

m.c74 = Constraint(expr=   m.x27 <= 0)

m.c75 = Constraint(expr=   m.x28 <= 1500)

m.c76 = Constraint(expr=   m.x29 <= 0)

m.c77 = Constraint(expr=   m.x6 + m.x10 <= 1500)

m.c78 = Constraint(expr=   m.x7 + m.x11 <= 0)

m.c79 = Constraint(expr=   m.x8 + m.x12 <= 1500)

m.c80 = Constraint(expr=   m.x9 + m.x13 <= 0)
