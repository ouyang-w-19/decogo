#  NLP written by GAMS Convert at 04/21/18 13:54:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         22        1        0       21        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         31       31        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        623      593       30        0
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
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=14571.3167*m.x1 - 3*m.x1**2 - m.x2**2 - 37250.204*m.x2 - 7*m.x3**2 + 1578.40997*m.x3 - 7*m.x4**2
                        - 23199.31*m.x4 - 9*m.x5**2 - 36532.101*m.x5 - 4*m.x6**2 + 14991.9969*m.x6 - 6*m.x7**2 - 
                       46241.855*m.x7 - 8*m.x8**2 + 59634.0121*m.x8 - m.x9**2 + 11781.1616*m.x9 - m.x10**2 - 62617.461*
                       m.x10 - 6*m.x11**2 + 23226.6837*m.x11 - 7*m.x12**2 - 16497.431*m.x12 - m.x13**2 + 350.55924*m.x13
                        - 4*m.x14**2 + 25674.7606*m.x14 - 2*m.x15**2 + 56334.3262*m.x15 - 5*m.x16**2 - 2159.2486*m.x16
                        - 7*m.x17**2 + 30150.9571*m.x17 - 6*m.x18**2 - 13688.295*m.x18 - 9*m.x19**2 - 41755.296*m.x19 - 
                       9*m.x20**2 + 34911.6548*m.x20 - 6*m.x21**2 + 104801.315*m.x21 - 2*m.x22**2 - 47888.471*m.x22 - 7*
                       m.x23**2 - 10644.315*m.x23 - 5*m.x24**2 + 119299.448*m.x24 - 7*m.x25**2 + 27859.4823*m.x25 - 9*
                       m.x26**2 + 89793.8375*m.x26 - 8*m.x27**2 + 108734.2*m.x27 - 3*m.x28**2 - 31798.43*m.x28 - m.x29**
                       2 + 15961.706*m.x29 - 8*m.x30**2 - 5450.7111*m.x30, sense=minimize)

m.c1 = Constraint(expr= - 6*m.x1 + m.x2 - 9*m.x3 + 3*m.x5 + m.x6 + 4*m.x7 - 2*m.x8 + 8*m.x9 - 6*m.x10 - 4*m.x11
                        - 6*m.x13 + 3*m.x14 + 6*m.x15 + 2*m.x16 + m.x17 + 9*m.x18 + 8*m.x19 - 10*m.x20 - 4*m.x21
                        - 7*m.x22 - 8*m.x23 - m.x24 + 5*m.x25 - 7*m.x26 + 10*m.x27 - 3*m.x28 - 6*m.x29 - 7*m.x30 <= -5)

m.c2 = Constraint(expr= - 9*m.x1 - 8*m.x2 + 3*m.x3 - 5*m.x4 + 5*m.x5 + 6*m.x6 + 9*m.x7 - 7*m.x8 - m.x9 + 4*m.x10 + m.x11
                        + 3*m.x12 + 10*m.x13 - 6*m.x14 - 7*m.x15 - 5*m.x16 - 4*m.x17 - m.x18 - 5*m.x19 + 6*m.x21
                        - 4*m.x22 + 9*m.x23 - 5*m.x24 + 9*m.x25 + 5*m.x26 - m.x27 + 4*m.x28 + 6*m.x29 + 6*m.x30 <= 37)

m.c3 = Constraint(expr=   4*m.x1 + 3*m.x2 + 8*m.x3 - 8*m.x4 + 5*m.x5 - 9*m.x6 - 5*m.x7 + m.x8 - 7*m.x9 + 8*m.x10
                        + 4*m.x12 - 7*m.x13 - 6*m.x14 - 2*m.x15 - 4*m.x16 + 2*m.x17 + 9*m.x18 + 9*m.x19 - 8*m.x20
                        - 3*m.x21 + 7*m.x22 - 6*m.x23 + 3*m.x24 - 5*m.x25 - 7*m.x26 - 3*m.x27 + 2*m.x28 + m.x29
                        + 9*m.x30 <= 12)

m.c4 = Constraint(expr=   4*m.x1 - 2*m.x2 - 5*m.x3 + 9*m.x4 + 10*m.x5 + m.x6 - 6*m.x7 - 5*m.x8 + 9*m.x9 - 5*m.x10
                        - 8*m.x11 - 6*m.x12 + 3*m.x13 - 8*m.x14 + 2*m.x15 + 4*m.x16 - 4*m.x18 - 5*m.x19 - 7*m.x20
                        + 4*m.x21 + 4*m.x22 - 3*m.x23 - 8*m.x24 - 3*m.x25 - 9*m.x26 - m.x27 + 7*m.x28 + 3*m.x29
                        - 7*m.x30 <= -11)

m.c5 = Constraint(expr=   9*m.x1 + 4*m.x2 - m.x3 - 9*m.x4 + 8*m.x5 - 4*m.x7 - 2*m.x9 + 7*m.x10 - 2*m.x11 + 8*m.x12
                        + 2*m.x13 - 2*m.x14 - 6*m.x15 - 8*m.x16 - m.x17 - m.x18 + 7*m.x19 + 8*m.x20 - 4*m.x21 + 2*m.x22
                        + 2*m.x23 - 6*m.x24 + 5*m.x25 + 3*m.x26 + 5*m.x27 + 5*m.x28 + 7*m.x29 + 2*m.x30 <= 59)

m.c6 = Constraint(expr= - 2*m.x1 + 8*m.x2 + 5*m.x3 - 5*m.x5 + 9*m.x6 + 8*m.x7 - m.x8 - 7*m.x9 - m.x10 + 2*m.x11
                        + 7*m.x12 - 10*m.x13 + 9*m.x14 + 7*m.x15 + 5*m.x16 - 5*m.x17 + 4*m.x19 + 6*m.x20 - 10*m.x21
                        + 4*m.x22 + 2*m.x23 - 8*m.x24 - 8*m.x26 - 6*m.x27 + 7*m.x28 - 5*m.x29 - 9*m.x30 <= 26)

m.c7 = Constraint(expr=   5*m.x2 - 2*m.x4 - 4*m.x5 + 5*m.x6 + 3*m.x7 + 9*m.x8 + 8*m.x9 + 8*m.x11 + 8*m.x12 - 10*m.x13
                        + 9*m.x14 - 7*m.x15 + m.x16 - 3*m.x17 + 3*m.x18 - m.x19 + 5*m.x20 - 8*m.x21 - 3*m.x22 - 7*m.x23
                        + m.x24 + 5*m.x25 + 9*m.x26 - 7*m.x27 + 4*m.x28 + 4*m.x29 - 3*m.x30 <= 51)

m.c8 = Constraint(expr=   7*m.x1 - 5*m.x2 - 5*m.x3 - 4*m.x4 - 3*m.x5 + m.x6 - 7*m.x7 - 7*m.x8 - 8*m.x9 + 2*m.x10 - m.x11
                        + m.x12 + 5*m.x13 - 2*m.x14 + 10*m.x15 + m.x16 - 2*m.x17 - 2*m.x18 + 6*m.x19 - m.x20 - 9*m.x22
                        + m.x23 - 10*m.x24 + 3*m.x25 - 3*m.x27 - 2*m.x28 - 5*m.x29 - 4*m.x30 <= -24)

m.c9 = Constraint(expr= - 9*m.x1 - 9*m.x2 - 5*m.x3 + 8*m.x4 + 8*m.x6 + 4*m.x7 - 6*m.x8 - 7*m.x9 + 6*m.x10 + 5*m.x11
                        - 7*m.x12 + 5*m.x13 - 5*m.x14 - 5*m.x15 + 2*m.x16 - m.x17 + 2*m.x18 - 10*m.x19 - 10*m.x20
                        + 6*m.x21 + 10*m.x22 + 9*m.x23 - 6*m.x24 + 4*m.x25 + 2*m.x26 + 9*m.x27 + 9*m.x28 - 2*m.x29
                        <= 25)

m.c10 = Constraint(expr= - 9*m.x1 + 5*m.x2 - 3*m.x3 + m.x4 + 2*m.x5 + 2*m.x6 - 2*m.x7 - 4*m.x8 - 9*m.x9 + 5*m.x10
                         + 7*m.x11 - m.x12 - 4*m.x13 + 4*m.x14 - 5*m.x15 - 3*m.x16 + 10*m.x18 - 7*m.x19 + 2*m.x20
                         - 6*m.x21 + m.x22 - 3*m.x23 + 2*m.x24 + 5*m.x25 + 8*m.x26 + 9*m.x27 + 2*m.x28 - 8*m.x29
                         + 7*m.x30 <= 27)

m.c11 = Constraint(expr=   m.x1 - 3*m.x2 - 7*m.x3 - m.x4 + 7*m.x5 + 7*m.x6 - 2*m.x7 + 3*m.x8 - 3*m.x9 - m.x10 + 4*m.x11
                         + 10*m.x12 - 2*m.x13 - 4*m.x14 - 8*m.x15 + 4*m.x16 - 2*m.x17 - 7*m.x18 + 4*m.x19 - 9*m.x21
                         - 10*m.x22 + 7*m.x23 - m.x24 - 9*m.x25 - 10*m.x26 - 5*m.x27 - 3*m.x28 - m.x29 + 7*m.x30 <= -15)

m.c12 = Constraint(expr=   3*m.x1 + 3*m.x2 + 9*m.x4 - 2*m.x5 - 7*m.x6 - 7*m.x8 - 5*m.x9 + 9*m.x10 + 6*m.x11 - 6*m.x12
                         + 4*m.x13 + 6*m.x14 - 6*m.x15 - 7*m.x16 - 4*m.x17 + 3*m.x18 + 4*m.x19 - 9*m.x20 - 9*m.x21
                         + 7*m.x22 + 9*m.x23 - 8*m.x24 - 5*m.x25 + 2*m.x26 - 9*m.x27 + m.x28 - 5*m.x29 + 5*m.x30 <= 1)

m.c13 = Constraint(expr= - 10*m.x1 + 5*m.x2 + 8*m.x3 - 9*m.x4 + 7*m.x5 - 6*m.x6 - 7*m.x7 + 3*m.x8 - 7*m.x9 + 3*m.x10
                         + 4*m.x11 - m.x12 + 4*m.x13 + 6*m.x14 + 3*m.x15 - 7*m.x16 - 8*m.x17 - 3*m.x18 - m.x19 + m.x20
                         - 7*m.x21 - 9*m.x22 - 5*m.x23 + 4*m.x24 - 6*m.x25 + 4*m.x26 - 8*m.x27 - m.x28 + 6*m.x29
                         - 3*m.x30 <= -22)

m.c14 = Constraint(expr= - 2*m.x1 + 10*m.x2 + 8*m.x3 + 5*m.x4 - 5*m.x5 + 4*m.x6 + 2*m.x7 + 2*m.x8 + 6*m.x9 - m.x10
                         + 5*m.x11 - 4*m.x12 - 6*m.x13 - 2*m.x14 + 4*m.x15 - 3*m.x17 + m.x18 + 2*m.x19 - 2*m.x20
                         + 4*m.x21 - 2*m.x22 - 5*m.x23 - 2*m.x24 + m.x25 + m.x27 - 2*m.x28 + 6*m.x30 <= 44)

m.c15 = Constraint(expr= - 9*m.x1 - 3*m.x2 - 9*m.x3 + 5*m.x4 - 2*m.x5 - 7*m.x6 + 7*m.x7 + 6*m.x8 - m.x9 + 6*m.x10
                         - 10*m.x11 + 7*m.x13 - 4*m.x14 + 6*m.x15 + 7*m.x16 - 5*m.x17 + 5*m.x19 - 6*m.x20 - 4*m.x21
                         - 2*m.x23 + 7*m.x24 + 3*m.x25 - 9*m.x26 - 7*m.x27 - 5*m.x28 - 10*m.x29 + 3*m.x30 <= -9)

m.c16 = Constraint(expr= - 2*m.x1 - 5*m.x2 + 8*m.x3 + 7*m.x4 + m.x5 - 8*m.x6 + 2*m.x7 - 5*m.x8 - 3*m.x9 + 4*m.x10
                         + 8*m.x11 + 8*m.x12 + 4*m.x13 - 6*m.x14 + 4*m.x15 + 6*m.x16 + 3*m.x17 + 7*m.x18 + 10*m.x19
                         - 2*m.x20 - 9*m.x21 + 2*m.x22 + 6*m.x23 - 8*m.x24 + 2*m.x25 - m.x26 - 8*m.x28 - 5*m.x29
                         - 9*m.x30 <= 29)

m.c17 = Constraint(expr=   4*m.x1 + 10*m.x2 - 7*m.x4 - m.x5 - 5*m.x6 + 9*m.x7 - m.x9 + 4*m.x10 - m.x12 + 7*m.x13
                         - 10*m.x14 + 5*m.x15 + m.x16 + 4*m.x17 - 10*m.x18 + 4*m.x19 + 3*m.x20 + 5*m.x22 + 8*m.x23
                         + 9*m.x24 - 3*m.x25 - 8*m.x27 - 2*m.x28 + 3*m.x29 - 9*m.x30 <= 39)

m.c18 = Constraint(expr=   2*m.x1 + 4*m.x2 - 10*m.x4 - 4*m.x5 - 10*m.x6 + m.x7 - 2*m.x8 + 6*m.x9 + 10*m.x10 - m.x11
                         - m.x12 - 8*m.x13 - 6*m.x14 + 3*m.x15 + 5*m.x16 - 5*m.x18 - 4*m.x19 + 3*m.x20 - m.x21 + 4*m.x22
                         - 5*m.x23 - 9*m.x24 - 6*m.x25 + 5*m.x26 + 7*m.x27 - m.x28 - m.x29 - 7*m.x30 <= -10)

m.c19 = Constraint(expr=   9*m.x1 + 5*m.x2 - 4*m.x3 + 4*m.x4 - 6*m.x5 - 2*m.x6 - 7*m.x7 - 6*m.x8 + 9*m.x9 + 9*m.x10
                         - 9*m.x11 + 6*m.x12 - 8*m.x13 + 10*m.x14 + 3*m.x15 - 4*m.x16 + 5*m.x17 + 3*m.x18 + 5*m.x19
                         + 4*m.x20 + m.x22 + 5*m.x23 - 8*m.x24 - 5*m.x25 - 9*m.x26 - 3*m.x27 - 4*m.x28 - 6*m.x29
                         + 5*m.x30 <= 20)

m.c20 = Constraint(expr=   5*m.x1 + 9*m.x2 + 2*m.x3 + 2*m.x4 + m.x5 + 7*m.x6 + 7*m.x7 + 5*m.x8 + 3*m.x9 + 7*m.x10
                         + 4*m.x11 + 2*m.x12 + 2*m.x13 + 4*m.x14 + 5*m.x15 + 9*m.x16 + 10*m.x17 + 5*m.x18 + m.x19
                         + 5*m.x20 + m.x21 + 8*m.x22 + 6*m.x23 + 8*m.x24 + 3*m.x25 + 2*m.x26 + 5*m.x27 + 4*m.x28
                         + 4*m.x29 + 10*m.x30 <= 1680)

m.c21 = Constraint(expr=   0.20403741*m.x1 + 0.20403741*m.x2 - 0.1165928*m.x3 - 0.2040374*m.x4 + 0.29148202*m.x5
                         + 0.08744461*m.x6 - 0.0291482*m.x7 + 0.26233382*m.x8 + 0.11659281*m.x9 + 0.17488921*m.x10
                         + 0.0291482*m.x11 + 0.0291482*m.x12 - 0.2040374*m.x13 + 0.26233382*m.x14 + 0.17488921*m.x15
                         - 0.2040374*m.x16 - 0.2623338*m.x17 - 0.0874446*m.x18 - 0.2331856*m.x19 - 0.2331856*m.x20
                         - 0.291482*m.x22 + 0.0291482*m.x23 + 0.20403741*m.x24 + 0.08744461*m.x26 + 0.14574101*m.x27
                         + 0.11659281*m.x28 - 0.291482*m.x29 - 0.1748892*m.x30 <= -36.228832)
