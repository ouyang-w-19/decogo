#  NLP written by GAMS Convert at 04/21/18 13:54:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         12        1        0       11        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         21       21        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        226      206       20        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
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

m.obj = Objective(expr=540.792129732*m.x1 - 3*m.x1**2 - m.x2**2 + 92.0068003629*m.x2 - 7*m.x3**2 - 2390.75252039*m.x3 - 
                       7*m.x4**2 - 8085.40130479*m.x4 - 9*m.x5**2 - 4627.10173328*m.x5 - 4*m.x6**2 - 12452.7098353*m.x6
                        - 6*m.x7**2 + 9419.17874069*m.x7 - 8*m.x8**2 + 7689.14130566*m.x8 - m.x9**2 - 5154.76865125*m.x9
                        - m.x10**2 - 9814.99860313*m.x10 - 6*m.x11**2 - 3701.15304202*m.x11 - 7*m.x12**2 + 12818.4489533
                       *m.x12 - m.x13**2 - 7825.52846743*m.x13 - 4*m.x14**2 - 52.6053189782*m.x14 - 2*m.x15**2 + 
                       6727.68114413*m.x15 - 5*m.x16**2 + 6093.30280299*m.x16 - 7*m.x17**2 - 1139.49658357*m.x17 - 6*
                       m.x18**2 + 7666.77668727*m.x18 - 9*m.x19**2 + 7371.88647018*m.x19 - 9*m.x20**2 - 16412.9116807*
                       m.x20, sense=minimize)

m.c1 = Constraint(expr= - 6*m.x1 + m.x2 + m.x3 - 3*m.x4 - 9*m.x5 - 7*m.x6 - m.x8 + 3*m.x9 + 7*m.x10 + m.x11 + 7*m.x12
                        + 4*m.x13 - 2*m.x14 - 2*m.x15 + 3*m.x16 + 8*m.x17 - 3*m.x18 - 6*m.x19 - m.x20 <= 5)

m.c2 = Constraint(expr= - 9*m.x1 + 3*m.x2 - 8*m.x3 + 3*m.x4 + 3*m.x5 - 5*m.x7 + 9*m.x8 + 5*m.x9 - 2*m.x10 + 6*m.x11
                        - 7*m.x12 + 9*m.x13 - 7*m.x15 - 7*m.x16 - m.x17 - 5*m.x18 + 4*m.x19 + 9*m.x20 <= 8)

m.c3 = Constraint(expr=   4*m.x1 - 10*m.x2 + 3*m.x3 + 5*m.x4 + 8*m.x5 + 8*m.x6 - 8*m.x7 - 9*m.x8 + 5*m.x9 + 7*m.x10
                        - 9*m.x11 - 6*m.x12 - 5*m.x13 - 7*m.x14 + m.x15 + 3*m.x16 - 7*m.x17 - 7*m.x18 + 8*m.x19
                        + 3*m.x20 <= -5)

m.c4 = Constraint(expr=   4*m.x1 - 2*m.x2 - 2*m.x3 + 10*m.x4 - 5*m.x5 + 8*m.x6 + 9*m.x7 + 5*m.x8 + 10*m.x9 - 5*m.x10
                        + m.x11 + 4*m.x12 - 6*m.x13 + 2*m.x14 - 5*m.x15 + 2*m.x16 + 9*m.x17 + 6*m.x18 - 5*m.x19 - m.x20
                        <= 49)

m.c5 = Constraint(expr=   9*m.x1 - 9*m.x2 + 4*m.x3 - 3*m.x4 - m.x5 - 9*m.x6 - 9*m.x7 + 5*m.x8 + 8*m.x9 - 2*m.x10
                        - 7*m.x12 - 4*m.x13 + 7*m.x14 + 6*m.x16 - 2*m.x17 - m.x18 + 7*m.x19 + 6*m.x20 <= 17)

m.c6 = Constraint(expr= - 2*m.x1 - 2*m.x2 + 8*m.x3 - 5*m.x4 + 5*m.x5 + 8*m.x6 + 7*m.x8 - 5*m.x9 + m.x10 + 9*m.x11
                        - 8*m.x12 + 8*m.x13 + 2*m.x14 - m.x15 - 5*m.x16 - 7*m.x17 - 3*m.x18 - m.x19 + 4*m.x20 <= 22)

m.c7 = Constraint(expr=   4*m.x2 + 5*m.x3 + 10*m.x4 - 2*m.x7 - 7*m.x8 - 4*m.x9 - m.x10 + 5*m.x11 - 5*m.x12 + 3*m.x13
                        + 9*m.x14 + 9*m.x15 + 8*m.x17 - m.x18 + 4*m.x20 <= 46)

m.c8 = Constraint(expr=   7*m.x1 + 2*m.x2 - 5*m.x3 + 4*m.x4 - 5*m.x5 - 4*m.x7 - 10*m.x8 - 3*m.x9 - 4*m.x10 + m.x11
                        - 10*m.x12 - 7*m.x13 + m.x14 - 7*m.x15 - 2*m.x16 - 8*m.x17 + 6*m.x18 + 2*m.x19 + 10*m.x20
                        <= -23)

m.c9 = Constraint(expr= - 9*m.x1 + 9*m.x2 - 9*m.x3 + 5*m.x4 - 5*m.x5 - 4*m.x6 + 8*m.x7 + 4*m.x8 - 6*m.x10 + 8*m.x11
                        - 2*m.x12 + 4*m.x13 - 7*m.x14 - 6*m.x15 - 6*m.x16 - 7*m.x17 + 9*m.x18 + 6*m.x19 + 9*m.x20 <= 11)

m.c10 = Constraint(expr=   3*m.x1 + 5*m.x2 + 5*m.x3 + m.x4 + 4*m.x5 + 6*m.x6 + 9*m.x7 + 5*m.x8 + 7*m.x9 + 9*m.x10
                         + 7*m.x11 + 8*m.x12 + 7*m.x13 + 7*m.x14 + 9*m.x16 + 5*m.x17 + 5*m.x18 + m.x19 + 7*m.x20
                         <= 1210)

m.c11 = Constraint(expr=   0.123612846515*m.x1 + 0.164817128686*m.x2 - 0.247225693029*m.x3 + 0.329634257372*m.x4
                         + 0.288429975201*m.x5 + 0.329634257372*m.x6 + 0.0412042821715*m.x7 - 0.288429975201*m.x8
                         - 0.0412042821715*m.x9 + 0.412042821715*m.x10 - 0.247225693029*m.x11 - 0.0412042821715*m.x12
                         - 0.164817128686*m.x13 + 0.329634257372*m.x15 - 0.0412042821715*m.x16 - 0.0412042821715*m.x17
                         + 0.247225693029*m.x18 - 0.123612846515*m.x19 - 0.247225693029*m.x20 <= -5.52216398993)
